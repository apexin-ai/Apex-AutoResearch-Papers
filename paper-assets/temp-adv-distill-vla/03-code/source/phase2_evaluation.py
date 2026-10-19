#!/usr/bin/env python3
"""Evaluate fine-tuned models on LIBERO tasks.

Two evaluation modes:
  --mode offline : Action prediction accuracy on held-out demo data
                   (works without LIBERO simulator, uses VIP features)
  --mode online  : Rollout in LIBERO simulator, compute success rate
                   (requires libero + robosuite + mujoco)

Inputs:
  - Fine-tuned checkpoint (lite MLP or LoRA adapter)
  - VIP features / LIBERO HDF5 data (offline mode)
  - LIBERO environment (online mode)

Outputs:
  - Per-task and overall success rate / action MSE
  - Results JSON saved to --output-dir
"""

import argparse
import glob
import json
import os
import time

import h5py
import numpy as np
import torch
import torch.nn as nn


# ---------------------------------------------------------------------------
# Model definitions (must match training code)
# ---------------------------------------------------------------------------

class LiteActionHead(nn.Module):
    def __init__(self, input_dim=1024, hidden_dim=512, action_dim=7):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, action_dim),
        )

    def forward(self, x):
        return self.net(x)


# ---------------------------------------------------------------------------
# Offline Evaluation (action prediction on demo data)
# ---------------------------------------------------------------------------

def eval_offline(args):
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"=== Offline Evaluation on {device} ===", flush=True)

    task_names = _get_task_names(args)
    results = {}

    for task_name in task_names:
        short = task_name.replace("pick_up_the_", "").replace(
            "_and_place_it_in_the_basket", "")
        print(f"\nEvaluating: {short}", flush=True)

        feat_path = os.path.join(args.features_dir, f"{task_name}.pt")
        if not os.path.exists(feat_path):
            print(f"  SKIP: no features", flush=True)
            continue

        # Load features
        feat_data = torch.load(feat_path, map_location="cpu",
                               weights_only=False)
        features = feat_data["features"]
        traj_ids = feat_data["traj_ids"]

        # Load actions
        hdf5_path = os.path.join(args.data_dir, f"{task_name}_demo.hdf5")
        if not os.path.exists(hdf5_path):
            print(f"  SKIP: no HDF5 data", flush=True)
            continue
        all_actions = []
        with h5py.File(hdf5_path, "r") as hf:
            demo_keys = sorted(
                [k for k in hf["data"].keys() if k.startswith("demo_")],
                key=lambda x: int(x.split("_")[1]),
            )
            for dk in demo_keys:
                all_actions.append(
                    torch.from_numpy(hf[f"data/{dk}/actions"][:]).float())
        actions = torch.cat(all_actions, 0)

        min_len = min(len(features), len(actions))
        features = features[:min_len]
        actions = actions[:min_len]

        # Train/eval split: last 10 demos as eval
        unique_trajs = torch.unique(traj_ids[:min_len])
        n_eval_trajs = max(1, len(unique_trajs) // 5)
        eval_traj_ids = unique_trajs[-n_eval_trajs:]
        eval_mask = torch.zeros(min_len, dtype=torch.bool)
        for tid in eval_traj_ids:
            eval_mask |= (traj_ids[:min_len] == tid)

        eval_features = features[eval_mask]
        eval_actions = actions[eval_mask]

        if len(eval_features) == 0:
            print(f"  SKIP: no eval data", flush=True)
            continue

        # Load model checkpoint
        ckpt_path_best = os.path.join(
            args.checkpoint_dir, f"{task_name}_best.pt")
        ckpt_path_last = os.path.join(
            args.checkpoint_dir, f"{task_name}_last.pt")
        ckpt_path = ckpt_path_best if os.path.exists(ckpt_path_best) \
            else ckpt_path_last
        if not os.path.exists(ckpt_path):
            print(f"  SKIP: no checkpoint at {ckpt_path}", flush=True)
            continue

        ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
        model = LiteActionHead(input_dim=1024, action_dim=7).to(device)
        model.load_state_dict(ckpt["model"])
        model.eval()

        # Predict
        with torch.no_grad():
            pred = model(eval_features.to(device)).cpu()

        # Metrics
        mse = ((pred - eval_actions) ** 2).mean().item()
        mse_per_dim = ((pred - eval_actions) ** 2).mean(dim=0).tolist()
        mae = (pred - eval_actions).abs().mean().item()

        # Per-dim correlation
        corr_per_dim = []
        for d in range(7):
            c = np.corrcoef(pred[:, d].numpy(), eval_actions[:, d].numpy())
            corr_per_dim.append(round(float(c[0, 1]), 4))

        results[task_name] = {
            "mse": round(mse, 6),
            "mae": round(mae, 6),
            "mse_per_dim": [round(v, 6) for v in mse_per_dim],
            "corr_per_dim": corr_per_dim,
            "n_eval_samples": int(eval_mask.sum()),
            "n_eval_trajs": int(n_eval_trajs),
            "checkpoint": ckpt_path,
        }
        print(f"  MSE={mse:.6f}  MAE={mae:.6f}  "
              f"n_eval={int(eval_mask.sum())}", flush=True)

    # Summary
    if results:
        mean_mse = np.mean([r["mse"] for r in results.values()])
        mean_mae = np.mean([r["mae"] for r in results.values()])
        summary = {
            "mode": "offline",
            "n_tasks": len(results),
            "mean_mse": round(float(mean_mse), 6),
            "mean_mae": round(float(mean_mae), 6),
            "per_task": results,
        }
    else:
        summary = {"mode": "offline", "n_tasks": 0, "error": "no tasks"}

    os.makedirs(args.output_dir, exist_ok=True)
    tag = os.path.basename(args.checkpoint_dir)
    out_path = os.path.join(args.output_dir, f"phase2_eval_{tag}.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults saved: {out_path}", flush=True)

    # Table
    print(f"\n{'=' * 70}")
    print(f"{'Task':30s} {'MSE':>10s} {'MAE':>10s} {'Eval N':>8s}")
    print("-" * 70)
    for task, r in results.items():
        short = task.replace("pick_up_the_", "").replace(
            "_and_place_it_in_the_basket", "")
        print(f"{short:30s} {r['mse']:10.6f} {r['mae']:10.6f} "
              f"{r['n_eval_samples']:8d}")
    if results:
        print(f"\n{'Mean':30s} {mean_mse:10.6f} {mean_mae:10.6f}")
    print(f"{'=' * 70}")


# ---------------------------------------------------------------------------
# Online Evaluation (LIBERO simulator rollout)
# ---------------------------------------------------------------------------

def eval_online(args):
    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"=== Online LIBERO Evaluation on {device} ===", flush=True)

    try:
        import robosuite
    except ImportError:
        print("ERROR: robosuite not installed. "
              "Install with: pip install robosuite", flush=True)
        return
    try:
        import libero
        from libero.libero import benchmark
    except ImportError:
        print("ERROR: libero not installed. "
              "Install from: https://github.com/Lifelong-Robot-Learning/LIBERO",
              flush=True)
        return

    # For full VLA online eval, we need the OpenVLA model
    try:
        from transformers import AutoModelForVision2Seq, AutoProcessor
        from peft import PeftModel
    except ImportError:
        print("ERROR: transformers/peft not installed", flush=True)
        return

    print("Loading model for online evaluation...", flush=True)

    # Load base model
    model = AutoModelForVision2Seq.from_pretrained(
        args.model_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
    ).to(device)
    processor = AutoProcessor.from_pretrained(
        args.model_path, trust_remote_code=True,
    )

    # Load LoRA adapter if specified
    adapter_dir = args.adapter_dir
    if adapter_dir and os.path.exists(adapter_dir):
        print(f"Loading LoRA adapter from {adapter_dir}", flush=True)
        model = PeftModel.from_pretrained(model, adapter_dir)
        model = model.merge_and_unload()
    model.eval()

    # Get norm stats
    stats_path = os.path.join(args.model_path, "dataset_statistics.json")
    with open(stats_path) as f:
        all_stats = json.load(f)
    norm_stats = all_stats.get(args.dataset_name,
                               list(all_stats.values())[0])

    # Run LIBERO evaluation
    task_names = _get_task_names(args)
    results = {}

    for task_name in task_names:
        short = task_name.replace("pick_up_the_", "").replace(
            "_and_place_it_in_the_basket", "")
        print(f"\nRollout: {short} ({args.episodes} episodes)", flush=True)

        successes = 0
        for ep in range(args.episodes):
            success = _run_episode(
                model, processor, norm_stats, task_name, device,
                max_steps=args.max_episode_steps,
            )
            if success:
                successes += 1
            if (ep + 1) % 10 == 0:
                print(f"  {ep + 1}/{args.episodes}: "
                      f"SR={successes / (ep + 1):.1%}", flush=True)

        sr = successes / max(args.episodes, 1)
        results[task_name] = {
            "success_rate": round(sr, 4),
            "successes": successes,
            "episodes": args.episodes,
        }
        print(f"  {short}: SR={sr:.1%} ({successes}/{args.episodes})",
              flush=True)

    # Summary
    if results:
        mean_sr = np.mean([r["success_rate"] for r in results.values()])
        summary = {
            "mode": "online",
            "n_tasks": len(results),
            "mean_success_rate": round(float(mean_sr), 4),
            "per_task": results,
        }
    else:
        summary = {"mode": "online", "n_tasks": 0}

    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, "phase2_eval_online.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults saved: {out_path}", flush=True)

    print(f"\n{'=' * 50}")
    print(f"{'Task':30s} {'SR':>8s}")
    print("-" * 50)
    for task, r in results.items():
        short = task.replace("pick_up_the_", "").replace(
            "_and_place_it_in_the_basket", "")
        print(f"{short:30s} {r['success_rate']:8.1%}")
    if results:
        print(f"\n{'Mean':30s} {mean_sr:8.1%}")
    print(f"{'=' * 50}")


def _run_episode(model, processor, norm_stats, task_name, device,
                 max_steps=300):
    """Run one LIBERO episode and return success boolean.

    This is a placeholder implementation. The actual rollout logic depends
    on LIBERO's API and the model's inference protocol. It should be adapted
    once the LIBERO environment is set up.
    """
    try:
        from libero.libero import benchmark
        from libero.libero.envs import OffScreenRenderEnv
    except ImportError:
        return False

    # Create environment
    bm = benchmark.get_benchmark("libero_object")
    task_idx = None
    for i, t in enumerate(bm.get_task_names()):
        if task_name in t or t in task_name:
            task_idx = i
            break
    if task_idx is None:
        return False

    task = bm.get_task(task_idx)
    env_args = {
        "bddl_file_name": task.problem_folder,
        "camera_heights": 256,
        "camera_widths": 256,
    }
    env = OffScreenRenderEnv(**env_args)
    env.seed(0)
    obs = env.reset()

    from PIL import Image as PILImage

    for step in range(max_steps):
        img = obs["agentview_image"]
        pil_img = PILImage.fromarray(img)
        instruction = ("In: What action should the robot take to "
                       + task_name.replace("_", " ") + "?\nOut:")

        inputs = processor(text=instruction, images=[pil_img],
                           return_tensors="pt").to(device)

        with torch.no_grad():
            action = model.predict_action(**inputs)

        obs, reward, done, info = env.step(action.cpu().numpy())
        if done:
            env.close()
            return info.get("success", reward > 0)

    env.close()
    return False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_task_names(args):
    if args.task:
        return [args.task]
    feat_files = sorted(glob.glob(
        os.path.join(args.features_dir, "*.pt")))
    return [os.path.basename(f).replace(".pt", "") for f in feat_files]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="LIBERO evaluation for Phase 2")

    p.add_argument("--mode", choices=["offline", "online"],
                   default="offline")

    # Task
    p.add_argument("--task", type=str, default=None)

    # Data
    p.add_argument("--data-dir", type=str,
                   default="./data/libero/libero_object")
    p.add_argument("--features-dir", type=str,
                   default="./artifacts/vip_features_all")

    # Model (offline: lite checkpoint; online: VLA + adapter)
    p.add_argument("--checkpoint-dir", type=str,
                   default="./artifacts/phase2_checkpoints")
    p.add_argument("--model-path", type=str,
                   default="/root/autodl-tmp/models/"
                           "openvla-7b-finetuned-libero-spatial")
    p.add_argument("--adapter-dir", type=str, default=None,
                   help="LoRA adapter dir for online eval")
    p.add_argument("--dataset-name", type=str, default="libero_spatial")

    # Online eval params
    p.add_argument("--episodes", type=int, default=50)
    p.add_argument("--max-episode-steps", type=int, default=300)

    # Output
    p.add_argument("--output-dir", type=str, default="./artifacts")
    p.add_argument("--device", type=str, default="cuda:0")

    # Debug
    p.add_argument("--dry-run", action="store_true")

    return p.parse_args()


def main():
    args = parse_args()
    if args.dry_run:
        args.episodes = 1

    if args.mode == "offline":
        eval_offline(args)
    else:
        eval_online(args)


if __name__ == "__main__":
    main()
