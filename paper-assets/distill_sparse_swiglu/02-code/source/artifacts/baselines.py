"""Baseline sparsity methods: TEAL greedy allocation, WINA, R-Sparse.

All mask generators return dict[int, Tensor] mapping layer_idx to a 1-D
binary mask of shape (intermediate_dim,), compatible with evaluate.py's
evaluate_perplexity().
"""

import torch


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

@torch.no_grad()
def _collect_mlp_inputs_cpu(model, input_ids, calib_batch_size=4):
    """Dense forward pass — capture each layer's MLP input on CPU."""
    n_layers = len(model.model.layers)
    bufs = {i: [] for i in range(n_layers)}
    hooks = []

    for idx, layer in enumerate(model.model.layers):
        def _hook(idx_):
            def fn(module, inp, out):
                bufs[idx_].append(inp[0].detach().cpu())
            return fn
        hooks.append(layer.mlp.register_forward_hook(_hook(idx)))

    for s in range(0, input_ids.size(0), calib_batch_size):
        model(input_ids[s : s + calib_batch_size])

    for h in hooks:
        h.remove()

    return {i: torch.cat(bufs[i], dim=0) for i in range(n_layers)}


# ---------------------------------------------------------------------------
# TEAL greedy per-layer allocation (Algorithm 1 from the TEAL paper,
# adapted for MLP-intermediate-only sparsification in SwiGLU)
# ---------------------------------------------------------------------------

@torch.no_grad()
def _layer_error_curve(mlp, mlp_input_cpu, sparsity_levels, device,
                       chunk_size=4):
    """Reconstruction error at each sparsity level for one MLP layer.

    Uses a *static* mask derived from mean |intermediate| across calibration
    tokens (same masking strategy used at evaluation time).

    Returns
    -------
    errors : list[float]   — one MSE value per sparsity level
    mean_mag : Tensor       — shape (inter_dim,) on CPU, float32
    """
    gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn
    inter_dim = gp.out_features

    # --- pass 1: intermediates, dense outputs, magnitude accumulator ------
    inter_chunks, dense_chunks = [], []
    accum_mag = torch.zeros(inter_dim, dtype=torch.float32)
    total_tokens = 0

    for s in range(0, mlp_input_cpu.size(0), chunk_size):
        x = mlp_input_cpu[s : s + chunk_size].to(device)
        inter = af(gp(x)) * up(x)
        y_dense = dp(inter)
        accum_mag += inter.abs().float().sum(dim=(0, 1)).cpu()
        total_tokens += x.size(0) * x.size(1)
        inter_chunks.append(inter.cpu())
        dense_chunks.append(y_dense.cpu())
        del x, inter, y_dense

    mean_mag = accum_mag / total_tokens
    all_inter = torch.cat(inter_chunks, dim=0)
    all_dense = torch.cat(dense_chunks, dim=0)
    del inter_chunks, dense_chunks

    # --- pass 2: error at each sparsity level ----------------------------
    errors = []
    for sp in sparsity_levels:
        if sp <= 0.0:
            errors.append(0.0)
            continue

        num_keep = max(int(inter_dim * (1.0 - sp)), 1)
        thr = torch.topk(mean_mag, num_keep).values[-1]
        mask_1d = (mean_mag >= thr)                         # (D,) bool, CPU

        total_err = 0.0
        total_elem = 0
        for s in range(0, all_inter.size(0), chunk_size):
            ic = all_inter[s : s + chunk_size].to(device)
            dc = all_dense[s : s + chunk_size].to(device)
            m = mask_1d.unsqueeze(0).unsqueeze(0).to(
                device=device, dtype=ic.dtype
            )
            y_sp = dp(ic * m)
            total_err += (dc - y_sp).pow(2).sum().item()
            total_elem += dc.numel()
            del ic, dc, y_sp

        errors.append(total_err / max(total_elem, 1))

    del all_inter, all_dense
    return errors, mean_mag


@torch.no_grad()
def teal_greedy_allocation_masks(model, input_ids, sparsity_target=0.5,
                                 step_size=0.05, calib_batch_size=4,
                                 device="cuda"):
    """TEAL paper's greedy error-minimization per-layer allocation.

    1. Dense forward pass → capture MLP inputs (CPU).
    2. Per layer: build reconstruction-error curve over candidate sparsities.
    3. Greedy loop: raise sparsity in the layer whose marginal error is smallest.
    4. Return static magnitude masks at the allocated per-layer sparsities.
    """
    n_layers = len(model.model.layers)
    max_sp = 0.90

    levels = [round(i * step_size, 4) for i in range(int(max_sp / step_size) + 1)]
    if levels[0] != 0.0:
        levels.insert(0, 0.0)

    print("  [greedy] collecting MLP inputs ...")
    mlp_inputs = _collect_mlp_inputs_cpu(model, input_ids, calib_batch_size)

    error_table = {}
    mean_mags = {}
    for li in range(n_layers):
        errs, mag = _layer_error_curve(
            model.model.layers[li].mlp, mlp_inputs[li], levels, device,
            chunk_size=4,
        )
        error_table[li] = errs
        mean_mags[li] = mag
        sp10_idx = min(2, len(errs) - 1)
        sp50_idx = min(10, len(errs) - 1)
        print(f"    layer {li:2d}  err@{levels[sp10_idx]:.0%}={errs[sp10_idx]:.6f}"
              f"  err@{levels[sp50_idx]:.0%}={errs[sp50_idx]:.6f}")

    del mlp_inputs
    torch.cuda.empty_cache()

    # --- greedy -----------------------------------------------------------
    cur = {i: 0 for i in range(n_layers)}

    def avg_sp():
        return sum(levels[cur[i]] for i in range(n_layers)) / n_layers

    print(f"  [greedy] running allocation (target={sparsity_target}) ...")
    while avg_sp() < sparsity_target:
        best_l, best_m = None, float("inf")
        for li in range(n_layers):
            ci = cur[li]
            if ci + 1 >= len(levels):
                continue
            marginal = error_table[li][ci + 1] - error_table[li][ci]
            if marginal < best_m:
                best_m = marginal
                best_l = li
        if best_l is None:
            break
        cur[best_l] += 1

    per_layer_sp = {i: levels[cur[i]] for i in range(n_layers)}
    print("  [greedy] allocation result:")
    for i in range(n_layers):
        print(f"    Layer {i:2d}: {per_layer_sp[i]:.2f}")
    print(f"  [greedy] global avg: {avg_sp():.4f}")

    # --- generate masks from pre-computed mean magnitudes -----------------
    inter_dim = model.model.layers[0].mlp.gate_proj.out_features
    masks = {}
    for li in range(n_layers):
        sp = per_layer_sp[li]
        if sp <= 0:
            masks[li] = torch.ones(inter_dim, dtype=torch.bfloat16)
        else:
            nk = max(int(inter_dim * (1.0 - sp)), 1)
            thr = torch.topk(mean_mags[li], nk).values[-1]
            masks[li] = (mean_mags[li] >= thr).to(torch.bfloat16)

    return masks


# ---------------------------------------------------------------------------
# WINA – Weight-Informed Neuron Activation  (Microsoft, ICLR 2026)
#
# score_i = mean|intermediate_i| × ‖down_proj_{:,i}‖_2
# Global top-K across all layers.
# ---------------------------------------------------------------------------

@torch.no_grad()
def wina_global_masks(model, input_ids, sparsity_target=0.5,
                      calib_batch_size=4):
    """WINA: activation magnitude weighted by down_proj column norms."""
    n_layers = len(model.model.layers)
    device = input_ids.device

    col_norms = {}
    for li in range(n_layers):
        W = model.model.layers[li].mlp.down_proj.weight        # (hidden, inter)
        col_norms[li] = W.float().norm(dim=0).cpu()             # (inter,)

    accum_mag = {}
    n_batches = 0
    saved = {}

    for li, layer in enumerate(model.model.layers):
        saved[li] = layer.mlp.forward
        mlp = layer.mlp
        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn

        def _fwd(lidx, _gp, _up, _dp, _af):
            def f(x):
                inter = _af(_gp(x)) * _up(x)
                mag = inter.abs().float().mean(dim=(0, 1)).cpu()
                if lidx not in accum_mag:
                    accum_mag[lidx] = mag
                else:
                    accum_mag[lidx] = accum_mag[lidx] + mag
                return _dp(inter)
            return f

        layer.mlp.forward = _fwd(li, gp, up, dp, af)

    for s in range(0, input_ids.size(0), calib_batch_size):
        model(input_ids[s : s + calib_batch_size])
        n_batches += 1

    for li, f in saved.items():
        model.model.layers[li].mlp.forward = f

    all_scores = []
    for li in sorted(accum_mag):
        mean = accum_mag[li] / n_batches
        score = mean * col_norms[li]
        all_scores.append((li, score))

    concat = torch.cat([s for _, s in all_scores])
    num_keep = int(len(concat) * (1.0 - sparsity_target))
    threshold = torch.topk(concat, num_keep).values[-1]

    masks = {}
    for li, score in all_scores:
        masks[li] = (score >= threshold).to(torch.bfloat16)
    return masks


@torch.no_grad()
def wina_greedy_allocation_masks(model, input_ids, sparsity_target=0.5,
                                 step_size=0.05, calib_batch_size=4,
                                 device="cuda"):
    """WINA scoring + TEAL-style greedy per-layer allocation.

    Same greedy loop as teal_greedy_allocation_masks but masks are generated
    using WINA scores (|act| × ‖W_col‖) instead of plain magnitude.
    """
    n_layers = len(model.model.layers)
    max_sp = 0.90
    levels = [round(i * step_size, 4)
              for i in range(int(max_sp / step_size) + 1)]
    if levels[0] != 0.0:
        levels.insert(0, 0.0)

    col_norms = {}
    for li in range(n_layers):
        W = model.model.layers[li].mlp.down_proj.weight
        col_norms[li] = W.float().norm(dim=0).cpu()

    print("  [wina-greedy] collecting MLP inputs ...")
    mlp_inputs = _collect_mlp_inputs_cpu(model, input_ids, calib_batch_size)

    error_table = {}
    wina_scores = {}

    for li in range(n_layers):
        mlp = model.model.layers[li].mlp
        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn
        inter_dim = gp.out_features

        accum_mag = torch.zeros(inter_dim, dtype=torch.float32)
        total_tokens = 0
        inter_chunks, dense_chunks = [], []

        for s in range(0, mlp_inputs[li].size(0), 4):
            x = mlp_inputs[li][s : s + 4].to(device)
            inter = af(gp(x)) * up(x)
            y_dense = dp(inter)
            accum_mag += inter.abs().float().sum(dim=(0, 1)).cpu()
            total_tokens += x.size(0) * x.size(1)
            inter_chunks.append(inter.cpu())
            dense_chunks.append(y_dense.cpu())
            del x, inter, y_dense

        mean_mag = accum_mag / total_tokens
        w_score = mean_mag * col_norms[li]
        wina_scores[li] = w_score

        all_inter = torch.cat(inter_chunks, dim=0)
        all_dense = torch.cat(dense_chunks, dim=0)
        del inter_chunks, dense_chunks

        errs = []
        for sp in levels:
            if sp <= 0.0:
                errs.append(0.0)
                continue
            nk = max(int(inter_dim * (1.0 - sp)), 1)
            thr = torch.topk(w_score, nk).values[-1]
            mask_1d = (w_score >= thr)

            t_err, t_elem = 0.0, 0
            for s in range(0, all_inter.size(0), 4):
                ic = all_inter[s : s + 4].to(device)
                dc = all_dense[s : s + 4].to(device)
                m = mask_1d.unsqueeze(0).unsqueeze(0).to(
                    device=device, dtype=ic.dtype
                )
                y_sp = dp(ic * m)
                t_err += (dc - y_sp).pow(2).sum().item()
                t_elem += dc.numel()
                del ic, dc, y_sp
            errs.append(t_err / max(t_elem, 1))

        error_table[li] = errs
        del all_inter, all_dense

        if li % 8 == 0:
            print(f"    layer {li:2d}  err@10%={errs[min(2,len(errs)-1)]:.6f}"
                  f"  err@50%={errs[min(10,len(errs)-1)]:.6f}")

    del mlp_inputs
    torch.cuda.empty_cache()

    cur = {i: 0 for i in range(n_layers)}

    def avg_sp():
        return sum(levels[cur[i]] for i in range(n_layers)) / n_layers

    while avg_sp() < sparsity_target:
        best_l, best_m = None, float("inf")
        for li in range(n_layers):
            ci = cur[li]
            if ci + 1 >= len(levels):
                continue
            marginal = error_table[li][ci + 1] - error_table[li][ci]
            if marginal < best_m:
                best_m = marginal
                best_l = li
        if best_l is None:
            break
        cur[best_l] += 1

    per_layer_sp = {i: levels[cur[i]] for i in range(n_layers)}
    print("  [wina-greedy] allocation:")
    for i in range(n_layers):
        print(f"    Layer {i:2d}: {per_layer_sp[i]:.2f}")
    print(f"  [wina-greedy] global avg: {avg_sp():.4f}")

    inter_dim = model.model.layers[0].mlp.gate_proj.out_features
    masks = {}
    for li in range(n_layers):
        sp = per_layer_sp[li]
        if sp <= 0:
            masks[li] = torch.ones(inter_dim, dtype=torch.bfloat16)
        else:
            nk = max(int(inter_dim * (1.0 - sp)), 1)
            thr = torch.topk(wina_scores[li], nk).values[-1]
            masks[li] = (wina_scores[li] >= thr).to(torch.bfloat16)

    return masks


# ---------------------------------------------------------------------------
# R-Sparse – Rank-Aware Activation Sparsity  (VITA-Group, ICLR 2025)
#
# Sparse channels selected by magnitude; non-sparse routed to low-rank path
# from offline SVD of down_proj.  Current implementation: mask-only (no LR
# compensation).  TODO: add LR compensation forward for full R-Sparse.
# ---------------------------------------------------------------------------

@torch.no_grad()
def r_sparse_masks(model, input_ids, sparsity_target=0.5, rank=64,
                   calib_batch_size=4, device="cuda"):
    """R-Sparse: magnitude-based channel selection (mask-only, no LR comp).

    The full R-Sparse method also applies low-rank compensation for pruned
    channels.  That requires a custom forward (not a static mask), so this
    function only returns the sparse-channel masks for evaluation under the
    existing evaluate_perplexity() framework.
    """
    n_layers = len(model.model.layers)
    inter_dim = model.model.layers[0].mlp.gate_proj.out_features

    mlp_inputs = _collect_mlp_inputs_cpu(model, input_ids, calib_batch_size)

    masks = {}
    for li in range(n_layers):
        mlp = model.model.layers[li].mlp
        gp, up, af = mlp.gate_proj, mlp.up_proj, mlp.act_fn

        accum = torch.zeros(inter_dim, dtype=torch.float32)
        total = 0
        for s in range(0, mlp_inputs[li].size(0), 4):
            x = mlp_inputs[li][s : s + 4].to(device)
            inter = af(gp(x)) * up(x)
            accum += inter.abs().float().sum(dim=(0, 1)).cpu()
            total += x.size(0) * x.size(1)
            del x, inter
        mean_mag = accum / total

        nk = max(int(inter_dim * (1.0 - sparsity_target)), 1)
        thr = torch.topk(mean_mag, nk).values[-1]
        masks[li] = (mean_mag >= thr).to(torch.bfloat16)

    del mlp_inputs
    return masks


def r_sparse_svd_cache(model, rank=64):
    """Precompute low-rank SVD of each down_proj for R-Sparse compensation.

    Returns dict[layer_idx -> (U_r, S_r, Vh_r)] where U_r @ diag(S_r) @ Vh_r
    approximates down_proj.weight with rank-r truncation.

    TODO: integrate into a custom MLP forward that routes pruned channels
    through the low-rank path at inference time.
    """
    cache = {}
    for li, layer in enumerate(model.model.layers):
        W = layer.mlp.down_proj.weight.float()   # (hidden, inter)
        U, S, Vh = torch.linalg.svd(W, full_matrices=False)
        cache[li] = (U[:, :rank].clone(), S[:rank].clone(), Vh[:rank, :].clone())
    return cache
