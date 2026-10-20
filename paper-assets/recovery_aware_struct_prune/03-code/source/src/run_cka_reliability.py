"""
CKA Reliability Analysis for RASP.

Validates the stability of structural scoring by:
1-3. Cross-model CKA split-half reliability (original vs pruned, per GQA group)
4.   F(h) split-half reliability for attention heads (intra-layer overlap)
5.   F(h) split-half reliability for MLP groups (intra-layer overlap)

Phases 1-3 address cross-model CKA stability.
Phases 4-5 address intra-layer F(h) stability (Claim 2 core metric).
"""

import argparse
import json
import logging
import os
import random
import sys

import numpy as np
import scipy.stats as stats
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def linear_cka(X, Y):
    """Linear CKA between two activation matrices. X: [n, p], Y: [n, q]."""
    X = X - X.mean(0)
    Y = Y - Y.mean(0)
    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()


def load_calibration_data(tokenizer, n_samples, max_length=512, seed=42):
    ds = load_dataset("openai/gsm8k", "main", split="train")
    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
    encodings = []
    for example in ds:
        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
        encodings.append(ids)
    return encodings


def collect_qproj_activations(model, calibration_data, device):
    """Collect per-head q_proj activations, mean-pooled over seq length.
    Returns dict[layer_idx] -> tensor[n_samples, n_heads_in_layer, head_dim] on CPU float32.
    """
    n_layers = model.config.num_hidden_layers
    head_dim = model.config.hidden_size // model.config.num_attention_heads

    q_outputs = {i: [] for i in range(n_layers)}
    hooks = []

    def make_hook(layer_idx):
        def fn(module, inp, out):
            q_outputs[layer_idx].append(out.detach().cpu())
        return fn

    for i in range(n_layers):
        h = model.model.layers[i].self_attn.q_proj.register_forward_hook(make_hook(i))
        hooks.append(h)

    model.eval()
    with torch.no_grad():
        for idx, enc in enumerate(calibration_data):
            input_ids = enc["input_ids"].to(device)
            attention_mask = enc["attention_mask"].to(device)
            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
            if (idx + 1) % 200 == 0:
                logger.info(f"  Forward pass {idx + 1}/{len(calibration_data)}")

    for h in hooks:
        h.remove()

    activations = {}
    for layer_idx in range(n_layers):
        out_dim = q_outputs[layer_idx][0].squeeze(0).shape[-1]
        n_heads = out_dim // head_dim
        per_head = []
        for t in q_outputs[layer_idx]:
            t = t.squeeze(0)  # [seq, n_heads * head_dim]
            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
            t = t.mean(dim=0)  # [n_heads, head_dim]
            per_head.append(t)
        activations[layer_idx] = torch.stack(per_head, dim=0).float()
        q_outputs[layer_idx] = None

    return activations


def collect_mlp_activations(model, calibration_data, device, n_groups=28):
    """Collect MLP gate_proj activations grouped into channel groups.
    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim] on CPU float32.
    """
    n_layers = model.config.num_hidden_layers
    intermediate_size = model.config.intermediate_size
    group_size = intermediate_size // n_groups

    gate_outputs = {i: [] for i in range(n_layers)}
    hooks = []

    def make_hook(layer_idx):
        def fn(module, inp, out):
            gate_outputs[layer_idx].append(out.detach().cpu())
        return fn

    for i in range(n_layers):
        h = model.model.layers[i].mlp.gate_proj.register_forward_hook(make_hook(i))
        hooks.append(h)

    model.eval()
    with torch.no_grad():
        for idx, enc in enumerate(calibration_data):
            input_ids = enc["input_ids"].to(device)
            attention_mask = enc["attention_mask"].to(device)
            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
            if (idx + 1) % 200 == 0:
                logger.info(f"  Forward pass {idx + 1}/{len(calibration_data)}")

    for h in hooks:
        h.remove()

    activations = {}
    for layer_idx in range(n_layers):
        per_group = []
        for t in gate_outputs[layer_idx]:
            t = t.squeeze(0)  # [seq, intermediate_size]
            t = t.mean(dim=0)  # [intermediate_size]
            usable = n_groups * group_size
            t = t[:usable].view(n_groups, group_size)
            per_group.append(t)
        activations[layer_idx] = torch.stack(per_group, dim=0).float()
        gate_outputs[layer_idx] = None

    return activations


def load_pruned_model_with_meta(base_model_path, pruned_model_path, torch_dtype, device):
    """Load structurally pruned model via base model reconstruction + saved weights."""
    meta_path = os.path.join(pruned_model_path, "pruning_metadata.pt")
    pruning_meta = torch.load(meta_path, map_location="cpu", weights_only=True)

    src_dir = os.path.dirname(os.path.abspath(__file__))
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    from prune import prune_attention_heads, prune_mlp_channels

    logging.getLogger("prune").setLevel(logging.WARNING)
    model = AutoModelForCausalLM.from_pretrained(
        base_model_path, torch_dtype=torch_dtype, device_map="cpu", trust_remote_code=True
    )
    prune_attention_heads(model, pruning_meta["attn_keep_masks"])
    prune_mlp_channels(model, pruning_meta["mlp_keep_masks"])

    safetensor_files = sorted(
        [f for f in os.listdir(pruned_model_path) if f.endswith(".safetensors")]
    )
    if safetensor_files:
        from safetensors.torch import load_file
        state_dict = {}
        for f in safetensor_files:
            state_dict.update(load_file(os.path.join(pruned_model_path, f)))
    else:
        state_dict = torch.load(
            os.path.join(pruned_model_path, "pytorch_model.bin"),
            map_location="cpu", weights_only=True,
        )
    model.load_state_dict(state_dict)
    model.to(device)
    return model, pruning_meta


def compute_group_cka(orig_acts, pruned_acts, keep_masks, n_heads_orig, n_kv_heads,
                      sample_indices=None):
    """Compute per-GQA-group CKA between original and pruned representations.

    For each KV group, concatenates retained Q head activations from both models
    and computes linear CKA. Original uses all Q heads in the group, pruned uses
    only retained Q heads (CKA handles different feature dimensions).

    Returns dict[(layer, group)] -> float (or NaN if group fully pruned).
    """
    heads_per_kv = n_heads_orig // n_kv_heads
    n_layers = len(orig_acts)
    scores = {}

    for layer_idx in range(n_layers):
        orig_layer = orig_acts[layer_idx]   # [N, n_heads_orig, head_dim]
        pruned_layer = pruned_acts[layer_idx]  # [N, n_retained, head_dim]
        retained = keep_masks[layer_idx]

        if sample_indices is not None:
            orig_layer = orig_layer[sample_indices]
            pruned_layer = pruned_layer[sample_indices]

        for g in range(n_kv_heads):
            orig_head_range = list(range(g * heads_per_kv, (g + 1) * heads_per_kv))
            pruned_positions = [i for i, h in enumerate(retained) if h in orig_head_range]

            if not pruned_positions:
                scores[(layer_idx, g)] = float("nan")
                continue

            n = orig_layer.shape[0]
            orig_flat = orig_layer[:, orig_head_range, :].reshape(n, -1)
            pruned_flat = pruned_layer[:, pruned_positions, :].reshape(n, -1)
            scores[(layer_idx, g)] = linear_cka(orig_flat, pruned_flat)

    return scores


def scores_to_aligned_arrays(scores_a, scores_b):
    """Extract aligned non-NaN value arrays from two score dicts."""
    common = sorted(set(scores_a.keys()) & set(scores_b.keys()))
    a_vals, b_vals = [], []
    for k in common:
        va, vb = scores_a[k], scores_b[k]
        if (isinstance(va, float) and va != va) or (isinstance(vb, float) and vb != vb):
            continue
        a_vals.append(va)
        b_vals.append(vb)
    return np.array(a_vals), np.array(b_vals)


def compute_fh_scores(acts_dict, sample_indices=None):
    """Compute intra-layer F(h) for each structure.
    acts_dict: dict[layer_idx] -> tensor[n_samples, n_structs, dim]
    Returns dict[layer_idx] -> tensor[n_structs] of F(h) values.
    """
    fh = {}
    for layer_idx, acts in acts_dict.items():
        if sample_indices is not None:
            acts = acts[sample_indices]
        n_samples, n_structs, dim = acts.shape
        matrix = torch.zeros(n_structs, n_structs)
        for i in range(n_structs):
            matrix[i, i] = 1.0
            for j in range(i + 1, n_structs):
                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
                matrix[i, j] = val
                matrix[j, i] = val
        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
        fh[layer_idx] = scores
    return fh


def compute_fh_reliability(acts_dict, n_splits, seed, structure_name):
    """Split-half reliability of F(h) rankings across all layers.
    Returns list of per-split result dicts with Spearman rho.
    """
    n_total = next(iter(acts_dict.values())).shape[0]
    split_results = []
    for i in range(n_splits):
        rng = np.random.RandomState(seed + i)
        perm = rng.permutation(n_total)
        half = n_total // 2
        idx_a = sorted(perm[:half].tolist())
        idx_b = sorted(perm[half:2 * half].tolist())

        logger.info(f"  Split {i}: computing F(h) on half A ({len(idx_a)} samples)...")
        fh_a = compute_fh_scores(acts_dict, idx_a)
        logger.info(f"  Split {i}: computing F(h) on half B ({len(idx_b)} samples)...")
        fh_b = compute_fh_scores(acts_dict, idx_b)

        vals_a, vals_b = [], []
        for layer_idx in sorted(fh_a.keys()):
            vals_a.extend(fh_a[layer_idx].tolist())
            vals_b.extend(fh_b[layer_idx].tolist())

        rho, p = stats.spearmanr(vals_a, vals_b)
        split_results.append({"split": i, "rho": float(rho), "p_value": float(p),
                              "n_structures": len(vals_a)})
        logger.info(f"  Split {i} {structure_name}: rho={rho:.4f}, p={p:.2e}, n={len(vals_a)}")
    return split_results


def main():
    parser = argparse.ArgumentParser(description="CKA Reliability Analysis for RASP scoring")
    parser.add_argument("--original_model", type=str, required=True)
    parser.add_argument("--pruned_model", type=str, default=None)
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--num_samples", type=int, default=1024)
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--n_splits", type=int, default=5)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16",
                        choices=["float16", "bfloat16", "float32"])
    parser.add_argument("--mlp_groups", type=int, default=28,
                        help="Number of MLP channel groups per layer")
    parser.add_argument("--skip_cross_model", action="store_true",
                        help="Skip Phase 1-3 (cross-model CKA); only run F(h) reliability")
    args = parser.parse_args()

    if not args.skip_cross_model and not args.pruned_model:
        parser.error("--pruned_model is required unless --skip_cross_model is set")

    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu_id}" if torch.cuda.is_available() else "cpu")
    torch_dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16,
                   "float32": torch.float32}[args.dtype]

    logger.info("Loading tokenizer and calibration data...")
    tokenizer = AutoTokenizer.from_pretrained(args.original_model, trust_remote_code=True)
    calibration_data = load_calibration_data(tokenizer, args.num_samples, args.max_length,
                                             args.seed)
    n_total = len(calibration_data)
    logger.info(f"Loaded {n_total} calibration samples")

    # --- Load original model and collect all activations ---
    logger.info("Loading original model...")
    orig_model = AutoModelForCausalLM.from_pretrained(
        args.original_model, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True
    )
    config = orig_model.config
    n_heads_orig = config.num_attention_heads
    n_kv_heads = config.num_key_value_heads
    n_layers = config.num_hidden_layers
    heads_per_kv = n_heads_orig // n_kv_heads
    logger.info(f"Architecture: {n_layers}L x {n_heads_orig}Q x {n_kv_heads}KV "
                f"({heads_per_kv} Q/KV group, {n_layers * n_kv_heads} total groups)")

    logger.info("Collecting original model q_proj activations...")
    orig_acts = collect_qproj_activations(orig_model, calibration_data, device)

    logger.info("Collecting original model MLP gate_proj activations...")
    orig_mlp_acts = collect_mlp_activations(orig_model, calibration_data, device, args.mlp_groups)

    del orig_model
    torch.cuda.empty_cache()
    logger.info("Original model freed. All activations cached on CPU.")

    output = {
        "config": {
            "original_model": args.original_model,
            "num_samples": n_total,
            "n_layers": n_layers,
            "n_heads_original": n_heads_orig,
            "n_kv_heads": n_kv_heads,
            "heads_per_kv": heads_per_kv,
            "total_gqa_groups": n_layers * n_kv_heads,
            "mlp_groups": args.mlp_groups,
            "seed": args.seed,
        },
    }

    # --- Phase 1-3: Cross-model CKA (optional) ---
    if not args.skip_cross_model:
        logger.info("Loading pruned model...")
        pruned_model, pruning_meta = load_pruned_model_with_meta(
            args.original_model, args.pruned_model, torch_dtype, device
        )
        keep_masks = pruning_meta["attn_keep_masks"]
        logger.info("Collecting pruned model activations...")
        pruned_acts = collect_qproj_activations(pruned_model, calibration_data, device)
        del pruned_model
        torch.cuda.empty_cache()
        logger.info("Pruned model freed.")

        # Phase 1: Full CKA scores
        logger.info("=" * 50)
        logger.info("Phase 1: Full CKA scores (N=%d)...", n_total)
        full_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,
                                        n_heads_orig, n_kv_heads)
        valid_scores = {k: v for k, v in full_scores.items()
                        if not (isinstance(v, float) and v != v)}
        vals = np.array(list(valid_scores.values()))
        logger.info(f"Valid groups: {len(valid_scores)}/{n_layers * n_kv_heads}")
        logger.info(f"CKA: mean={vals.mean():.4f}, std={vals.std():.4f}, "
                    f"range=[{vals.min():.4f}, {vals.max():.4f}]")

        # Phase 2: Split-half reliability (cross-model)
        logger.info("=" * 50)
        logger.info("Phase 2: Split-half reliability (%d splits)...", args.n_splits)
        cross_split_results = []
        for i in range(args.n_splits):
            rng = np.random.RandomState(args.seed + i)
            perm = rng.permutation(n_total)
            half = n_total // 2
            idx_a = sorted(perm[:half].tolist())
            idx_b = sorted(perm[half:2 * half].tolist())

            scores_a = compute_group_cka(orig_acts, pruned_acts, keep_masks,
                                         n_heads_orig, n_kv_heads, idx_a)
            scores_b = compute_group_cka(orig_acts, pruned_acts, keep_masks,
                                         n_heads_orig, n_kv_heads, idx_b)
            arr_a, arr_b = scores_to_aligned_arrays(scores_a, scores_b)
            rho, p = stats.spearmanr(arr_a, arr_b)
            cross_split_results.append({"split": i, "rho": float(rho), "p_value": float(p),
                                        "n_groups": len(arr_a)})
            logger.info(f"  Split {i}: rho={rho:.4f}, p={p:.2e}")

        cross_mean_rho = float(np.mean([r["rho"] for r in cross_split_results]))
        cross_std_rho = float(np.std([r["rho"] for r in cross_split_results]))

        # Phase 3: Calibration size sensitivity
        logger.info("=" * 50)
        logger.info("Phase 3: Calibration size sensitivity...")
        size_results = []
        for n_sub in [128, 256, 512]:
            if n_sub >= n_total:
                continue
            rng = np.random.RandomState(args.seed)
            sub_idx = sorted(rng.permutation(n_total)[:n_sub].tolist())

            sub_scores = compute_group_cka(orig_acts, pruned_acts, keep_masks,
                                           n_heads_orig, n_kv_heads, sub_idx)
            ref_vals, sub_vals = scores_to_aligned_arrays(full_scores, sub_scores)
            rho, p = stats.spearmanr(ref_vals, sub_vals)
            size_results.append({"n_samples": n_sub, "rho_vs_full": float(rho),
                                 "p_value": float(p)})
            logger.info(f"  N={n_sub}: rho={rho:.4f} vs N={n_total}")

        del pruned_acts
        torch.cuda.empty_cache()

        per_group = {}
        for (l, g), v in full_scores.items():
            key = f"layer{l}_group{g}"
            per_group[key] = None if (isinstance(v, float) and v != v) else float(v)

        output["config"]["pruned_model"] = args.pruned_model
        output["config"]["valid_gqa_groups"] = len(valid_scores)
        output["per_group_cka_scores"] = per_group
        output["cka_summary"] = {
            "mean": float(vals.mean()),
            "std": float(vals.std()),
            "min": float(vals.min()),
            "max": float(vals.max()),
            "median": float(np.median(vals)),
        }
        output["split_half_reliability"] = {
            "per_split": cross_split_results,
            "mean_rho": cross_mean_rho,
            "std_rho": cross_std_rho,
            "pass": cross_mean_rho > 0.9,
        }
        output["size_sensitivity"] = {
            "reference_n": n_total,
            "per_size": size_results,
            "all_pass_0.9": all(s["rho_vs_full"] > 0.9 for s in size_results),
        }

    # --- Phase 4: F(h) attention head split-half reliability ---
    logger.info("=" * 50)
    logger.info("Phase 4: F(h) attention head split-half reliability (%d splits)...",
                args.n_splits)
    attn_fh_results = compute_fh_reliability(orig_acts, args.n_splits, args.seed, "attn_heads")
    attn_mean_rho = float(np.mean([r["rho"] for r in attn_fh_results]))
    attn_std_rho = float(np.std([r["rho"] for r in attn_fh_results]))
    attn_pass = attn_mean_rho > 0.9
    logger.info(f"Attn F(h) reliability: mean_rho={attn_mean_rho:.4f} +/- {attn_std_rho:.4f} "
                f"{'PASS' if attn_pass else 'FAIL'}")

    output["fh_attn_reliability"] = {
        "per_split": attn_fh_results,
        "mean_rho": attn_mean_rho,
        "std_rho": attn_std_rho,
        "pass": attn_pass,
    }

    del orig_acts
    torch.cuda.empty_cache()

    # --- Phase 5: F(h) MLP group split-half reliability ---
    logger.info("=" * 50)
    logger.info("Phase 5: F(h) MLP group split-half reliability (%d splits)...", args.n_splits)
    mlp_fh_results = compute_fh_reliability(orig_mlp_acts, args.n_splits, args.seed, "mlp_groups")
    mlp_mean_rho = float(np.mean([r["rho"] for r in mlp_fh_results]))
    mlp_std_rho = float(np.std([r["rho"] for r in mlp_fh_results]))
    mlp_pass = mlp_mean_rho > 0.9
    logger.info(f"MLP F(h) reliability: mean_rho={mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f} "
                f"{'PASS' if mlp_pass else 'FAIL'}")

    output["fh_mlp_reliability"] = {
        "per_split": mlp_fh_results,
        "mean_rho": mlp_mean_rho,
        "std_rho": mlp_std_rho,
        "pass": mlp_pass,
    }

    del orig_mlp_acts
    torch.cuda.empty_cache()

    # --- Save results ---
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    logger.info(f"Results saved to {args.output}")

    # --- Print summary ---
    print(f"\n{'=' * 60}")
    print("CKA Reliability Analysis")
    print(f"{'=' * 60}")

    if not args.skip_cross_model:
        print(f"\nCross-model CKA (Phase 1-3):")
        print(f"  GQA groups: {len(valid_scores)}/{n_layers * n_kv_heads} valid")
        print(f"  CKA scores: {vals.mean():.4f} +/- {vals.std():.4f} "
              f"[{vals.min():.4f}, {vals.max():.4f}]")
        sh_pass = "PASS" if cross_mean_rho > 0.9 else "FAIL"
        print(f"  Split-half reliability ({args.n_splits} splits):")
        print(f"    rho = {cross_mean_rho:.4f} +/- {cross_std_rho:.4f}  {sh_pass} "
              f"(threshold: 0.9)")
        for r in cross_split_results:
            print(f"      Split {r['split']}: rho={r['rho']:.4f}")
        print(f"  Size sensitivity (vs N={n_total}):")
        for s in size_results:
            sv = "PASS" if s["rho_vs_full"] > 0.9 else "FAIL"
            print(f"    N={s['n_samples']:4d}: rho={s['rho_vs_full']:.4f}  {sv}")

    print(f"\nF(h) Attention head reliability (Phase 4):")
    ah_label = "PASS" if attn_pass else "FAIL"
    print(f"  rho = {attn_mean_rho:.4f} +/- {attn_std_rho:.4f}  {ah_label} (threshold: 0.9)")
    for r in attn_fh_results:
        print(f"    Split {r['split']}: rho={r['rho']:.4f}")

    print(f"\nF(h) MLP group reliability (Phase 5):")
    mh_label = "PASS" if mlp_pass else "FAIL"
    print(f"  rho = {mlp_mean_rho:.4f} +/- {mlp_std_rho:.4f}  {mh_label} (threshold: 0.9)")
    for r in mlp_fh_results:
        print(f"    Split {r['split']}: rho={r['rho']:.4f}")

    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
