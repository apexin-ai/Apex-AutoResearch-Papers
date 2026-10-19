"""
Precompute SmolVLA obs_features and K action samples for ACR-VLA conformal refinement.

For each LIBERO demo timestep:
  1. Encode observation prefix through VLM → obs_features (960D mean-pooled hidden states)
  2. Generate K action chunks via flow-matching with shared KV cache
  3. Extract ground-truth action chunk from dataset

Input:
  - LIBERO HDF5 demo files (agentview_rgb, eye_in_hand_rgb, ee_states, actions)
  - Pretrained SmolVLA model (lerobot/smolvla_libero format)

Output (per benchmark):
  - obs_features.pt:    (N, 960)               float32
  - k_samples.pt:       (N, K, h_eff, act_dim) float32
  - expert_actions.pt:  (N, h_eff, act_dim)    float32
  - manifest.json:      metadata

Dependencies: lerobot, torch, h5py, safetensors

Usage:
  python lerobot_precompute.py --benchmark object
  python lerobot_precompute.py --benchmark spatial --K 10 --batch_size 8
  python lerobot_precompute.py --benchmark object --max_demos 2 --dry_run  # quick test
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

import torch
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from smolvla_wrapper import SmolVLAWrapper
from utils import (
    load_libero_demos, build_training_samples, set_seed,
    CORRECTION_DIM, FULL_ACTION_DIM, H_EFF, OBS_DIM, CHUNK_SIZE,
)


def parse_args():
    p = argparse.ArgumentParser(description="Precompute SmolVLA features for ACR-VLA")
    p.add_argument("--benchmark", type=str, nargs="+", default=["object"],
                   choices=["object", "spatial", "goal", "long", "90"])
    p.add_argument("--cache_dir", type=str,
                   default="/root/autodl-tmp/crm_cache_smolvla/")
    p.add_argument("--model_path", type=str,
                   default="/root/autodl-tmp/models/smolvla_libero/")
    p.add_argument("--data_dir", type=str,
                   default="/root/autodl-tmp/libero_data/")
    p.add_argument("--K", type=int, default=10)
    p.add_argument("--h_eff", type=int, default=H_EFF)
    p.add_argument("--action_dim", type=int, default=CORRECTION_DIM,
                   help="Action dim to save (6=pose only, 7=pose+gripper)")
    p.add_argument("--max_demos_per_task", type=int, default=20)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--device", type=str, default="cuda")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--save_every", type=int, default=500,
                   help="Save partial checkpoint every N samples")
    p.add_argument("--dry_run", action="store_true",
                   help="Process only first 2 demos per task for quick validation")
    p.add_argument("--resume_from", type=int, default=0,
                   help="Skip first N samples (for resuming interrupted runs)")
    return p.parse_args()


def precompute_benchmark(wrapper, args, benchmark):
    cache_dir = Path(args.cache_dir) / benchmark
    cache_dir.mkdir(parents=True, exist_ok=True)

    max_demos = 2 if args.dry_run else args.max_demos_per_task
    print(f"\n[precompute] Loading {benchmark} demos from {args.data_dir}...")
    trajectories = load_libero_demos(
        benchmark, data_dir=args.data_dir, max_demos_per_task=max_demos,
    )
    print(f"[precompute] {len(trajectories)} trajectories loaded")

    samples = build_training_samples(
        trajectories, h_eff=args.h_eff, action_dim=args.action_dim,
    )
    total = len(samples)
    print(f"[precompute] {total} timestep samples to process")

    if args.resume_from > 0:
        samples = samples[args.resume_from:]
        print(f"[precompute] Resuming from index {args.resume_from}, "
              f"{len(samples)} remaining")

    all_obs_features = []
    all_k_samples = []
    all_expert_actions = []
    partial_idx = 0
    t0 = time.time()

    for start in range(0, len(samples), args.batch_size):
        end = min(start + args.batch_size, len(samples))
        batch = samples[start:end]

        batch_obs = [{
            "agentview_rgb": s["agentview_rgb"],
            "eye_in_hand_rgb": s["eye_in_hand_rgb"],
            "ee_states": s["ee_states"],
            "task_name": s["task_name"],
        } for s in batch]

        obs_feat, k_actions = wrapper.get_obs_features_and_samples_batch(
            batch_obs, K=args.K,
        )
        # obs_feat: (B, 960), k_actions: (B, K, chunk_size, FULL_ACTION_DIM)

        # Slice to h_eff and action_dim
        k_actions_sliced = k_actions[:, :, :args.h_eff, :args.action_dim]
        expert_batch = torch.tensor(
            np.stack([s["expert_action"] for s in batch]),
            dtype=torch.float32,
        )

        all_obs_features.append(obs_feat.cpu())
        all_k_samples.append(k_actions_sliced.cpu())
        all_expert_actions.append(expert_batch)

        processed = args.resume_from + start + len(batch)
        if processed % args.save_every < args.batch_size or end == len(samples):
            elapsed = time.time() - t0
            rate = (start + len(batch)) / elapsed if elapsed > 0 else 0
            remaining = len(samples) - (start + len(batch))
            eta = remaining / rate if rate > 0 else 0
            print(f"  [{benchmark}] {processed}/{args.resume_from + total} "
                  f"({rate:.1f} samples/s, ETA: {eta/60:.1f}min)", flush=True)

        # Periodic partial save
        if (start + len(batch)) % args.save_every < args.batch_size and all_obs_features:
            partial_start = partial_idx * args.save_every + args.resume_from
            partial_end = processed
            partial_path = cache_dir / f"partial_s0_{partial_start}_{partial_end}.pt"
            torch.save({
                "obs_features": torch.cat(all_obs_features, dim=0),
                "k_samples": torch.cat(all_k_samples, dim=0),
                "expert_actions": torch.cat(all_expert_actions, dim=0),
            }, partial_path)
            partial_idx += 1

    # Concatenate all results
    obs_features_all = torch.cat(all_obs_features, dim=0)
    k_samples_all = torch.cat(all_k_samples, dim=0)
    expert_actions_all = torch.cat(all_expert_actions, dim=0)

    N = obs_features_all.shape[0]
    print(f"\n[precompute] Saving {N} samples to {cache_dir}")
    print(f"  obs_features: {obs_features_all.shape}")
    print(f"  k_samples:    {k_samples_all.shape}")
    print(f"  expert_actions: {expert_actions_all.shape}")

    torch.save(obs_features_all, cache_dir / "obs_features.pt")
    torch.save(k_samples_all, cache_dir / "k_samples.pt")
    torch.save(expert_actions_all, cache_dir / "expert_actions.pt")

    manifest = {
        "benchmark": benchmark,
        "n_samples": N,
        "K": args.K,
        "obs_dim": OBS_DIM,
        "action_dim": args.action_dim,
        "h_eff": args.h_eff,
        "vla_backbone": "smolvla",
        "model_path": args.model_path,
    }
    (cache_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))

    elapsed = time.time() - t0
    print(f"[precompute] {benchmark}: {N} samples in {elapsed/60:.1f}min")

    return N


def validate_output(cache_dir, benchmark, K, h_eff, action_dim):
    """Sanity check on saved cache files."""
    bd = Path(cache_dir) / benchmark
    obs = torch.load(bd / "obs_features.pt", map_location="cpu", weights_only=True)
    ks = torch.load(bd / "k_samples.pt", map_location="cpu", weights_only=True)
    ea = torch.load(bd / "expert_actions.pt", map_location="cpu", weights_only=True)
    manifest = json.loads((bd / "manifest.json").read_text())

    N = obs.shape[0]
    checks = []

    # Shape checks
    checks.append(("obs_features shape", obs.shape == (N, OBS_DIM)))
    checks.append(("k_samples shape", ks.shape == (N, K, h_eff, action_dim)))
    checks.append(("expert_actions shape", ea.shape == (N, h_eff, action_dim)))
    checks.append(("manifest n_samples", manifest["n_samples"] == N))

    # NaN/Inf checks
    checks.append(("obs_features no NaN", not torch.isnan(obs).any()))
    checks.append(("k_samples no NaN", not torch.isnan(ks).any()))
    checks.append(("expert_actions no NaN", not torch.isnan(ea).any()))
    checks.append(("obs_features no Inf", not torch.isinf(obs).any()))
    checks.append(("k_samples no Inf", not torch.isinf(ks).any()))

    # Value range checks
    checks.append(("obs_features mean reasonable",
                    0.001 < obs.abs().mean().item() < 100))
    checks.append(("k_samples range reasonable",
                    ks.abs().max().item() < 50))

    # K-sample diversity: different noise → different actions
    if K >= 2:
        pair_diff = (ks[:, 0] - ks[:, 1]).norm(dim=-1).mean().item()
        checks.append(("K-sample diversity > 0", pair_diff > 0.001))

    print(f"\n[validate] {benchmark} ({N} samples):")
    all_pass = True
    for name, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        if not passed:
            all_pass = False

    # Print summary stats
    print(f"\n  obs_features: mean={obs.mean():.4f}, std={obs.std():.4f}, "
          f"min={obs.min():.4f}, max={obs.max():.4f}")
    print(f"  k_samples:    mean={ks.mean():.4f}, std={ks.std():.4f}, "
          f"range=[{ks.min():.4f}, {ks.max():.4f}]")
    print(f"  expert_actions: mean={ea.mean():.4f}, std={ea.std():.4f}")
    if K >= 2:
        print(f"  K-sample pairwise L2 (mean): {pair_diff:.6f}")

    return all_pass


def main():
    args = parse_args()
    print(f"[lerobot_precompute] args: {vars(args)}")

    set_seed(args.seed)

    print(f"[precompute] Loading SmolVLA from {args.model_path}")
    wrapper = SmolVLAWrapper(pretrained_path=args.model_path, device=args.device)
    print(f"[precompute] Model loaded. VLM hidden_size={wrapper.vlm_hidden_size}")

    for bm in args.benchmark:
        precompute_benchmark(wrapper, args, bm)
        validate_output(args.cache_dir, bm, args.K, args.h_eff, args.action_dim)


if __name__ == "__main__":
    main()
