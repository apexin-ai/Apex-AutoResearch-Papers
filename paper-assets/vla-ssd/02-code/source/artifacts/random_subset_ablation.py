"""Random-subset ablation: verify dominant-24 head ablation effect is specific.

Strategy (optimized for speed):
  Phase 1 (GPU): Single forward pass through all frames. Hook layer 1 attention
    to cache per-head context vectors and non-instruction-only context vectors.
  Phase 2 (CPU): For each of 20 random 24-head subsets, reconstruct L1 features
    from cached intermediates (just layer 1 recomputation: o_proj + residual +
    layernorm + MLP).
  Phase 3: Train probes, compute statistics, generate plot.
"""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---

import argparse
import gc
import glob
import json
import os
import time

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from PIL import Image

NUM_IMAGE_TOKENS = 256
INST_START = 1 + NUM_IMAGE_TOKENS  # BOS(1) + image(256) = 257
NUM_HEADS = 32
HEAD_DIM = 128
HIDDEN_SIZE = 4096
INTERMEDIATE_SIZE = 11008

INSTRUCTION_HEADS_24 = [0,1,2,4,7,8,10,11,12,14,15,16,17,18,19,20,22,23,25,26,27,29,30,31]

SEED = 42
BATCH_SIZE = 256
LR = 1e-3
EPOCHS = 50
PATIENCE = 5
HIDDEN_DIM = 256
N_RANDOM = 20
N_ABLATE = 24


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model_path", default=f"{PROJECT_ROOT}/checkpoints/openvla-7b")
    p.add_argument("--data_dir", default=f"{PROJECT_ROOT}/data/libero/libero_goal/")
    p.add_argument("--output", default=f"{PROJECT_ROOT}/results/random_subset_ablation.json")
    p.add_argument("--fig_dir", default=f"{PROJECT_ROOT}/results/figures/")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--demos_per_task", type=int, default=50)
    p.add_argument("--n_random", type=int, default=N_RANDOM)
    return p.parse_args()


def task_desc_from_filename(fname):
    stem = Path(fname).stem.replace("_demo", "")
    return stem.replace("_", " ")


# =============================================================================
# Phase 1: GPU caching
# =============================================================================

class AttentionCacher:
    """Hook into layer 1 attention to capture per-head context vectors."""

    def __init__(self):
        self.full_context = None      # [32, 128] per frame
        self.non_inst_sum = None      # [32, 128] per frame
        self.non_inst_weight = None   # [32] per frame
        self.residual_last = None     # [4096] per frame

    def reset(self):
        self.full_context = None
        self.non_inst_sum = None
        self.non_inst_weight = None
        self.residual_last = None


def install_caching_hooks(model, cacher):
    """Install hooks that capture attention intermediates without modifying computation."""
    import transformers.models.llama.modeling_llama as llama_mod
    from transformers.models.llama.modeling_llama import repeat_kv

    layer1 = model.language_model.model.layers[1]
    layer1_attn = layer1.self_attn

    original_fn = llama_mod.eager_attention_forward

    def caching_eager_attention_forward(module, query, key, value, attention_mask,
                                        scaling, dropout=0.0, **kwargs):
        key_states = repeat_kv(key, module.num_key_value_groups)
        value_states = repeat_kv(value, module.num_key_value_groups)

        attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling
        if attention_mask is not None:
            causal_mask = attention_mask[:, :, :, :key_states.shape[-2]]
            attn_weights = attn_weights + causal_mask

        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query.dtype)

        # Cache attention intermediates for layer 1 only
        if module is layer1_attn:
            # attn_weights: [1, 32, seq, seq], value_states: [1, 32, seq, 128]
            w = attn_weights[0]  # [32, seq, seq]
            v = value_states[0]  # [32, seq, 128]
            last_pos = w.shape[1] - 1  # last token position

            w_last = w[:, last_pos, :]  # [32, seq]

            # full context: weighted sum over all positions
            # full_ctx[h] = w_last[h] @ v[h] = [128]
            full_ctx = torch.bmm(w_last.unsqueeze(1), v).squeeze(1)  # [32, 128]

            # non-instruction context: only positions < INST_START
            seq_len = w_last.shape[1]
            if INST_START < seq_len:
                w_non_inst = w_last[:, :INST_START]  # [32, INST_START]
                v_non_inst = v[:, :INST_START, :]     # [32, INST_START, 128]
                non_inst_s = torch.bmm(w_non_inst.unsqueeze(1), v_non_inst).squeeze(1)  # [32, 128]
                non_inst_w = w_non_inst.sum(dim=1)  # [32]
            else:
                non_inst_s = full_ctx.clone()
                non_inst_w = torch.ones(NUM_HEADS, device=w.device, dtype=w.dtype)

            cacher.full_context = full_ctx.cpu().float()
            cacher.non_inst_sum = non_inst_s.cpu().float()
            cacher.non_inst_weight = non_inst_w.cpu().float()

        attn_output = torch.matmul(attn_weights, value_states)
        attn_output = attn_output.transpose(1, 2).contiguous()
        return attn_output, attn_weights

    llama_mod.eager_attention_forward = caching_eager_attention_forward

    # Hook to capture residual input to layer 1
    def capture_residual(module, args, kwargs):
        hidden_states = args[0] if args else kwargs.get('hidden_states')
        cacher.residual_last = hidden_states[0, -1, :].detach().cpu().float()

    pre_hook = layer1.register_forward_pre_hook(capture_residual, with_kwargs=True)

    # Early exit after layer 1
    class EarlyExit(Exception):
        pass

    layer2 = model.language_model.model.layers[2]

    def early_exit_hook(module, args, kwargs):
        raise EarlyExit()

    exit_hook = layer2.register_forward_pre_hook(early_exit_hook, with_kwargs=True)

    return original_fn, [pre_hook, exit_hook], EarlyExit


def remove_caching_hooks(model, original_fn, hooks):
    import transformers.models.llama.modeling_llama as llama_mod
    llama_mod.eager_attention_forward = original_fn
    for h in hooks:
        h.remove()


def load_model(model_path, device):
    from transformers import AutoModelForVision2Seq, AutoProcessor

    processor = AutoProcessor.from_pretrained(
        model_path, trust_remote_code=True, local_files_only=True
    )
    model = AutoModelForVision2Seq.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
        local_files_only=True,
    )
    model = model.to(device).eval()
    print(f"Model loaded on {device}")
    return model, processor


def cache_all_frames(model, processor, data_dir, demos_per_task, device):
    """Phase 1: run all frames through model, cache attention intermediates."""
    cacher = AttentionCacher()
    original_fn, hooks, EarlyExit = install_caching_hooks(model, cacher)

    hdf5_files = sorted(glob.glob(os.path.join(data_dir, "*.hdf5")))
    task_names = [task_desc_from_filename(f) for f in hdf5_files]

    all_full_context = []      # list of [32, 128] tensors
    all_non_inst_sum = []      # list of [32, 128] tensors
    all_non_inst_weight = []   # list of [32] tensors
    all_residual_last = []     # list of [4096] tensors
    all_actions = []           # list of action arrays
    task_boundaries = []       # (task_idx, demo_idx, n_frames) tuples

    total_frames = 0
    t0 = time.time()

    for task_idx, (hdf5_path, task_name) in enumerate(zip(hdf5_files, task_names)):
        print(f"\n  Task {task_idx}: {task_name}")
        prompt = f"In: What action should the robot take to {task_name}?\nOut:"

        f = h5py.File(hdf5_path, "r")
        data = f["data"]
        demo_keys = sorted(data.keys(), key=lambda x: int(x.split("_")[1]))[:demos_per_task]

        for demo_idx, dk in enumerate(demo_keys):
            imgs_np = data[dk]["obs"]["agentview_rgb"][:]
            acts_np = np.asarray(data[dk]["actions"], dtype=np.float32)
            n_frames = len(imgs_np)

            for frame_idx in range(n_frames):
                img = Image.fromarray(imgs_np[frame_idx])
                inputs = processor(text=[prompt], images=[img], return_tensors="pt")
                inputs = {k: v.to(device) for k, v in inputs.items()}

                cacher.reset()
                try:
                    with torch.no_grad(), torch.amp.autocast("cuda", dtype=torch.float16):
                        model(**inputs)
                except EarlyExit:
                    pass

                all_full_context.append(cacher.full_context)
                all_non_inst_sum.append(cacher.non_inst_sum)
                all_non_inst_weight.append(cacher.non_inst_weight)
                all_residual_last.append(cacher.residual_last)

                del inputs
                total_frames += 1

            all_actions.append(acts_np)
            task_boundaries.append((task_idx, demo_idx, n_frames))

            if (demo_idx + 1) % 10 == 0:
                elapsed = time.time() - t0
                fps = total_frames / elapsed
                print(f"    {demo_idx+1}/{len(demo_keys)} demos, {total_frames} frames, {fps:.1f} fps")

        f.close()
        gc.collect()
        torch.cuda.empty_cache()

    remove_caching_hooks(model, original_fn, hooks)

    elapsed = time.time() - t0
    print(f"\nPhase 1 complete: {total_frames} frames in {elapsed/60:.1f} min ({total_frames/elapsed:.1f} fps)")

    # Stack into arrays
    cache = {
        "full_context": torch.stack(all_full_context),       # [N, 32, 128]
        "non_inst_sum": torch.stack(all_non_inst_sum),       # [N, 32, 128]
        "non_inst_weight": torch.stack(all_non_inst_weight), # [N, 32]
        "residual_last": torch.stack(all_residual_last),     # [N, 4096]
        "actions": all_actions,                               # list of arrays
        "task_boundaries": task_boundaries,                   # list of (task, demo, nframes)
        "task_names": task_names,
    }
    return cache


# =============================================================================
# Phase 2: CPU reconstruction of L1 features
# =============================================================================

def extract_layer1_weights(model):
    """Extract layer 1 weights needed for reconstruction."""
    layer1 = model.language_model.model.layers[1]
    weights = {
        "o_proj": layer1.self_attn.o_proj.weight.detach().cpu().float(),     # [4096, 4096]
        "gate_proj": layer1.mlp.gate_proj.weight.detach().cpu().float(),     # [11008, 4096]
        "up_proj": layer1.mlp.up_proj.weight.detach().cpu().float(),         # [11008, 4096]
        "down_proj": layer1.mlp.down_proj.weight.detach().cpu().float(),     # [4096, 11008]
        "post_attn_norm_weight": layer1.post_attention_layernorm.weight.detach().cpu().float(),  # [4096]
        "norm_eps": layer1.post_attention_layernorm.variance_epsilon,
    }
    return weights


def rms_norm(x, weight, eps):
    """RMSNorm: x * weight / sqrt(mean(x^2) + eps)"""
    variance = x.pow(2).mean(dim=-1, keepdim=True)
    x_normed = x * torch.rsqrt(variance + eps)
    return x_normed * weight


def reconstruct_l1_features(cache, weights, ablate_heads):
    """Reconstruct L1 last-token features for a given set of ablated heads.

    For ablated heads: use non_inst_sum / non_inst_weight (renormalized attention)
    For non-ablated heads: use full_context (original attention)
    """
    N = cache["full_context"].shape[0]
    full_ctx = cache["full_context"]          # [N, 32, 128]
    non_inst_s = cache["non_inst_sum"]        # [N, 32, 128]
    non_inst_w = cache["non_inst_weight"]     # [N, 32]
    residual = cache["residual_last"]         # [N, 4096]

    # Build per-head context: ablated heads get renormalized non-inst context
    context = full_ctx.clone()  # [N, 32, 128]
    if ablate_heads is not None and len(ablate_heads) > 0:
        heads = list(ablate_heads)
        # ablated_context[h] = non_inst_sum[h] / non_inst_weight[h]
        denom = non_inst_w[:, heads].unsqueeze(-1).clamp(min=1e-9)  # [N, len(heads), 1]
        context[:, heads, :] = non_inst_s[:, heads, :] / denom

    # Flatten heads: [N, 32, 128] -> [N, 4096]
    concat_ctx = context.reshape(N, HIDDEN_SIZE)

    # o_proj: Linear(4096, 4096) - weight is [4096, 4096], output = input @ weight.T
    attn_out = concat_ctx @ weights["o_proj"].T  # [N, 4096]

    # Residual connection
    post_attn = residual + attn_out  # [N, 4096]

    # Post-attention RMSNorm
    normed = rms_norm(post_attn, weights["post_attn_norm_weight"], weights["norm_eps"])

    # MLP: SwiGLU
    gate = normed @ weights["gate_proj"].T   # [N, 11008]
    up = normed @ weights["up_proj"].T       # [N, 11008]
    mlp_out = (nn.functional.silu(gate) * up) @ weights["down_proj"].T  # [N, 4096]

    # Final residual
    output = post_attn + mlp_out  # [N, 4096]

    return output.numpy()


# =============================================================================
# Phase 3: Probe training and statistics
# =============================================================================

class ActionMLPProbe(nn.Module):
    def __init__(self, in_dim=HIDDEN_SIZE, out_dim=7, hidden_dim=HIDDEN_DIM):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim),
        )

    def forward(self, x):
        return self.net(x)


def build_train_val_from_features(features, cache):
    """Build (x_t, a_{t+1}) pairs with 80/20 per-task split."""
    task_boundaries = cache["task_boundaries"]
    actions = cache["actions"]
    task_names = cache["task_names"]
    n_tasks = len(task_names)

    # Group demos by task
    task_demos = {i: [] for i in range(n_tasks)}
    offset = 0
    for idx, (task_idx, demo_idx, n_frames) in enumerate(task_boundaries):
        task_demos[task_idx].append((offset, n_frames, idx))
        offset += n_frames

    X_tr_list, y_tr_list = [], []
    X_val_list, y_val_list = [], []
    val_task_labels = []

    action_idx = 0
    for task_idx in range(n_tasks):
        demos = task_demos[task_idx]
        n_demos = len(demos)
        n_train = int(n_demos * 0.8)

        for i, (frame_offset, n_frames, boundary_idx) in enumerate(demos):
            feat = features[frame_offset:frame_offset + n_frames]
            act = actions[action_idx]
            action_idx += 1

            T = min(len(feat), len(act))
            if T < 2:
                continue

            x = torch.from_numpy(feat[:T-1].copy()).float()
            y = torch.from_numpy(act[1:T].copy()).float()

            if i < n_train:
                X_tr_list.append(x)
                y_tr_list.append(y)
            else:
                X_val_list.append(x)
                y_val_list.append(y)
                val_task_labels.extend([task_idx] * len(x))

    X_tr = torch.cat(X_tr_list)
    y_tr = torch.cat(y_tr_list)
    X_val = torch.cat(X_val_list)
    y_val = torch.cat(y_val_list)
    val_task_labels = np.array(val_task_labels)

    return X_tr, y_tr, X_val, y_val, val_task_labels


def train_and_eval(X_tr, y_tr, X_val, y_val, val_task_labels, task_names, device="cpu"):
    """Train probe and evaluate. Returns mean_R2 across tasks."""
    torch.manual_seed(SEED)
    np.random.seed(SEED)

    # Z-score normalization
    mean = X_tr.mean(dim=0)
    std = X_tr.std(dim=0).clamp(min=1e-8)
    X_tr_n = (X_tr - mean) / std
    X_val_n = (X_val - mean) / std

    y_mean = y_tr.mean(dim=0)
    y_std = y_tr.std(dim=0).clamp(min=1e-8)
    y_tr_n = (y_tr - y_mean) / y_std
    y_val_n = (y_val - y_mean) / y_std

    probe = ActionMLPProbe().to(device)
    optimizer = torch.optim.Adam(probe.parameters(), lr=LR)
    criterion = nn.MSELoss()

    X_tr_d = X_tr_n.to(device)
    y_tr_d = y_tr_n.to(device)
    X_val_d = X_val_n.to(device)
    y_val_d = y_val_n.to(device)

    best_val_loss = float("inf")
    patience_counter = 0
    best_state = None

    n_train = len(X_tr_d)
    for epoch in range(EPOCHS):
        probe.train()
        perm = torch.randperm(n_train, device=device)
        epoch_loss = 0.0
        n_batches = 0
        for i in range(0, n_train, BATCH_SIZE):
            idx = perm[i:i+BATCH_SIZE]
            pred = probe(X_tr_d[idx])
            loss = criterion(pred, y_tr_d[idx])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1

        probe.eval()
        with torch.no_grad():
            val_pred = probe(X_val_d)
            val_loss = criterion(val_pred, y_val_d).item()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            best_state = {k: v.clone() for k, v in probe.state_dict().items()}
        else:
            patience_counter += 1
            if patience_counter >= PATIENCE:
                break

    probe.load_state_dict(best_state)
    probe.eval()

    with torch.no_grad():
        val_pred = probe(X_val_d).cpu()

    # Compute per-task R²
    y_val_orig = y_val
    val_pred_orig = val_pred * y_std + y_mean

    n_tasks = len(task_names)
    per_task_r2 = {}
    for t in range(n_tasks):
        mask = val_task_labels == t
        if mask.sum() == 0:
            continue
        y_t = y_val_orig[mask]
        p_t = val_pred_orig[mask]
        ss_res = ((y_t - p_t) ** 2).sum().item()
        ss_tot = ((y_t - y_t.mean(dim=0)) ** 2).sum().item()
        r2 = 1 - ss_res / max(ss_tot, 1e-9)
        per_task_r2[task_names[t]] = round(r2, 4)

    mean_r2 = np.mean(list(per_task_r2.values()))
    return round(float(mean_r2), 4), per_task_r2


# =============================================================================
# Main
# =============================================================================

def main():
    args = parse_args()
    device = f"cuda:{args.gpu}"

    print("=" * 60)
    print("Random-Subset Ablation Experiment")
    print("=" * 60)

    # --- Phase 1: Cache attention intermediates ---
    print("\n[Phase 1] Loading model and caching attention intermediates...")
    model, processor = load_model(args.model_path, device)

    t0 = time.time()
    cache = cache_all_frames(model, processor, args.data_dir, args.demos_per_task, device)

    # Extract layer 1 weights for reconstruction
    layer1_weights = extract_layer1_weights(model)

    # Free GPU memory
    del model, processor
    gc.collect()
    torch.cuda.empty_cache()
    print(f"Model unloaded. Phase 1 took {(time.time()-t0)/60:.1f} min")

    # --- Phase 2: Reconstruct features for each condition ---
    print("\n[Phase 2] Reconstructing L1 features for each condition...")

    # Baseline (no ablation)
    print("  Computing baseline (no ablation)...")
    t1 = time.time()
    baseline_features = reconstruct_l1_features(cache, layer1_weights, ablate_heads=None)
    print(f"    Reconstruction took {time.time()-t1:.1f}s")

    print("  Training baseline probe...")
    X_tr, y_tr, X_val, y_val, val_task_labels = build_train_val_from_features(baseline_features, cache)
    print(f"    Train: {len(X_tr)}, Val: {len(X_val)}")
    baseline_r2, baseline_per_task = train_and_eval(X_tr, y_tr, X_val, y_val, val_task_labels, cache["task_names"])
    print(f"    Baseline R² = {baseline_r2}")
    del baseline_features, X_tr, y_tr, X_val, y_val

    # Dominant-24 ablation
    print("\n  Computing dominant-24 ablation...")
    t1 = time.time()
    dom_features = reconstruct_l1_features(cache, layer1_weights, ablate_heads=INSTRUCTION_HEADS_24)
    print(f"    Reconstruction took {time.time()-t1:.1f}s")

    print("  Training dominant-24 probe...")
    X_tr, y_tr, X_val, y_val, val_task_labels = build_train_val_from_features(dom_features, cache)
    dominant_r2, dominant_per_task = train_and_eval(X_tr, y_tr, X_val, y_val, val_task_labels, cache["task_names"])
    dominant_r2_increase = round(dominant_r2 - baseline_r2, 4)
    print(f"    Dominant-24 R² = {dominant_r2}, increase = {dominant_r2_increase}")
    del dom_features, X_tr, y_tr, X_val, y_val

    # Random subsets
    print(f"\n  Computing {args.n_random} random-24 ablations...")
    random_results = []
    for i in range(args.n_random):
        rng = np.random.RandomState(i)
        random_heads = sorted(rng.choice(NUM_HEADS, size=N_ABLATE, replace=False).tolist())

        t1 = time.time()
        rand_features = reconstruct_l1_features(cache, layer1_weights, ablate_heads=random_heads)
        recon_time = time.time() - t1

        X_tr, y_tr, X_val, y_val, val_task_labels = build_train_val_from_features(rand_features, cache)
        rand_r2, rand_per_task = train_and_eval(X_tr, y_tr, X_val, y_val, val_task_labels, cache["task_names"])
        r2_increase = round(rand_r2 - baseline_r2, 4)

        random_results.append({
            "seed": i,
            "ablated_heads": random_heads,
            "r2": rand_r2,
            "r2_increase": r2_increase,
            "per_task_r2": rand_per_task,
        })
        print(f"    [{i+1}/{args.n_random}] seed={i}, heads={random_heads[:5]}..., "
              f"R²={rand_r2}, increase={r2_increase} ({recon_time:.1f}s)")

        del rand_features, X_tr, y_tr, X_val, y_val
        gc.collect()

    # --- Phase 3: Statistics ---
    print("\n[Phase 3] Computing statistics...")
    increases = [r["r2_increase"] for r in random_results]
    random_mean = float(np.mean(increases))
    random_sd = float(np.std(increases, ddof=1))
    z_score = (dominant_r2_increase - random_mean) / max(random_sd, 1e-9)
    percentile = float(np.mean([1 for x in increases if x <= dominant_r2_increase])) * 100
    # One-sample t-test: is dominant_r2_increase significantly > random mean?
    from scipy import stats
    t_stat, p_two_sided = stats.ttest_1samp(increases, dominant_r2_increase)
    p_value = float(p_two_sided / 2) if t_stat < 0 else 1 - float(p_two_sided / 2)

    print(f"\n{'='*60}")
    print("RESULTS")
    print(f"{'='*60}")
    print(f"  Baseline R²:           {baseline_r2}")
    print(f"  Dominant-24 R²:        {dominant_r2}")
    print(f"  Dominant-24 increase:  {dominant_r2_increase}")
    print(f"  Random-24 mean:        {random_mean:.4f} ± {random_sd:.4f}")
    print(f"  z-score:               {z_score:.2f}")
    print(f"  Percentile:            {percentile:.1f}%")
    print(f"  p-value (one-sided):   {p_value:.6f}")

    # Save results
    output = {
        "baseline_r2": baseline_r2,
        "baseline_per_task_r2": baseline_per_task,
        "dominant_r2": dominant_r2,
        "dominant_r2_increase": dominant_r2_increase,
        "dominant_per_task_r2": dominant_per_task,
        "dominant_heads": INSTRUCTION_HEADS_24,
        "random_iterations": random_results,
        "statistics": {
            "random_mean": round(random_mean, 4),
            "random_sd": round(random_sd, 4),
            "z_score": round(z_score, 2),
            "percentile": round(percentile, 1),
            "p_value": round(p_value, 6),
            "n_random": args.n_random,
            "n_ablate": N_ABLATE,
        },
        "metadata": {
            "probe": f"MLP({HIDDEN_SIZE},{HIDDEN_DIM},7)",
            "optimizer": f"Adam lr={LR}",
            "epochs": EPOCHS,
            "patience": PATIENCE,
            "batch_size": BATCH_SIZE,
            "seed": SEED,
            "target": "next_action a_{t+1} from feature at time t",
            "normalization": "z-score (train mean/std)",
            "split": "80/20 per-task by demo index",
            "readout": "last_token at L1",
            "demos_per_task": args.demos_per_task,
            "n_tasks": len(cache["task_names"]),
            "reconstruction": "cached attention intermediates + layer1 recomputation",
        }
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {args.output}")

    # --- Generate plot ---
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs(args.fig_dir, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(increases, bins=10, color="#4C72B0", edgecolor="white", alpha=0.8, label="Random-24 subsets")
    ax.axvline(dominant_r2_increase, color="red", linewidth=2, linestyle="--",
               label=f"Dominant-24 ({dominant_r2_increase:.4f})")
    ax.axvline(random_mean, color="gray", linewidth=1, linestyle=":",
               label=f"Random mean ({random_mean:.4f})")
    ax.set_xlabel("R² increase (ablated - baseline)")
    ax.set_ylabel("Count")
    ax.set_title(f"Random-Subset Ablation (n={args.n_random})\n"
                 f"z={z_score:.2f}, p={p_value:.4f}, percentile={percentile:.0f}%")
    ax.legend(fontsize=9)
    plt.tight_layout()

    pdf_path = os.path.join(args.fig_dir, "fig_random_subset_ablation.pdf")
    png_path = os.path.join(args.fig_dir, "fig_random_subset_ablation.png")
    fig.savefig(pdf_path, dpi=150, bbox_inches="tight")
    fig.savefig(png_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Figure saved to {pdf_path}")


if __name__ == "__main__":
    main()
