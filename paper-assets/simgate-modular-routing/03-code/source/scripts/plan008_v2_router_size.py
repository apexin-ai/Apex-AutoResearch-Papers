#!/usr/bin/env python3
"""Plan-008 v2: Router Size Ablation — Qwen3-0.6B / 1.7B / 4B.

Fixes from v1:
  Bug 1: Use generative eval (generate + parse_output) instead of logit argmax.
  Bug 2: All Qwen3 family (unified architecture).
  Bug 3: Episode-level stratified split consistent between train and eval.

Usage:
  python scripts/plan008_v2_router_size.py              # Full run (3 models x 3 epochs)
  python scripts/plan008_v2_router_size.py --dry-run    # 1 epoch each, confirm no errors
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime

PROJECT_ROOT = "/root/autodl-tmp/simgate-modular-routing"
DATA_DIR = os.path.join(PROJECT_ROOT, "data/plan-004-implicit")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results/plan-008-v2")

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["WANDB_MODE"] = "offline"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

DEVICE_ID = 0
SEED = 42
LR = 2e-5

MODELS = [
    {
        "name": "qwen3-0.6b",
        "model_path": "/root/autodl-tmp/models/Qwen/Qwen3-0.6B",
        "output_dir": os.path.join(PROJECT_ROOT, "checkpoints/plan-008-v2-qwen3-0.6b"),
        "batch_size": 4,
        "gradient_accumulation_steps": 8,
    },
    {
        "name": "qwen3-1.7b",
        "model_path": "/root/autodl-tmp/models/Qwen/Qwen3-1.7B",
        "output_dir": os.path.join(PROJECT_ROOT, "checkpoints/plan-008-v2-qwen3-1.7b"),
        "batch_size": 4,
        "gradient_accumulation_steps": 8,
    },
    {
        "name": "qwen3-4b",
        "model_path": "/root/autodl-tmp/models/Qwen/Qwen3-4B",
        "output_dir": os.path.join(PROJECT_ROOT, "checkpoints/plan-008-v2-qwen3-4b"),
        "batch_size": 4,
        "gradient_accumulation_steps": 8,
    },
]


def resolve_model_path(path):
    if os.path.exists(path):
        return path
    parent = os.path.dirname(path)
    basename = os.path.basename(path)
    alt = basename.replace(".", "___").replace("-", "___")
    alt_path = os.path.join(parent, alt)
    if os.path.exists(alt_path):
        return alt_path
    # Try replacing only dots
    alt2 = basename.replace(".", "___")
    alt2_path = os.path.join(parent, alt2)
    if os.path.exists(alt2_path):
        return alt2_path
    # Scan directory
    if os.path.isdir(parent):
        for d in os.listdir(parent):
            normalized = d.replace("___", ".").replace("___", "-")
            if normalized == basename or d.lower() == basename.lower():
                return os.path.join(parent, d)
    return path


def train_model(cfg, epochs):
    model_path = resolve_model_path(cfg["model_path"])
    if not os.path.exists(model_path):
        print(f"ERROR: Model not found: {cfg['model_path']} (resolved: {model_path})")
        return None

    cmd = [
        sys.executable,
        os.path.join(PROJECT_ROOT, "src/training/implicit_router_sft.py"),
        "train",
        "--data_dir", DATA_DIR,
        "--model_name", model_path,
        "--epochs", str(epochs),
        "--batch_size", str(cfg["batch_size"]),
        "--gradient_accumulation_steps", str(cfg["gradient_accumulation_steps"]),
        "--upsample_minority",
        "--lr", str(LR),
        "--output_dir", cfg["output_dir"],
        "--seed", str(SEED),
        "--gpu_id", str(DEVICE_ID),
    ]

    print(f"\n{'='*60}")
    print(f"Training {cfg['name']} | epochs={epochs} bs={cfg['batch_size']} ga={cfg['gradient_accumulation_steps']}")
    print(f"  model: {model_path}")
    print(f"  output: {cfg['output_dir']}")
    print(f"{'='*60}\n", flush=True)

    t0 = time.time()
    result = subprocess.run(cmd)
    elapsed = time.time() - t0

    sentinel = os.path.join(cfg["output_dir"], "TRAINING_COMPLETE")
    if result.returncode != 0 or not os.path.exists(sentinel):
        # For 4B model, retry with smaller batch if OOM
        if cfg["name"] == "qwen3-4b" and cfg["batch_size"] > 2:
            print(f"Training failed for {cfg['name']}, retrying with batch_size=2, ga=16...")
            cfg["batch_size"] = 2
            cfg["gradient_accumulation_steps"] = 16
            return train_model(cfg, epochs)
        print(f"ERROR: Training failed for {cfg['name']} (exit={result.returncode}, elapsed={elapsed/60:.1f}min)")
        return None

    print(f"Training {cfg['name']} done in {elapsed/60:.1f} min")
    return cfg["output_dir"]


def get_eval_loss(output_dir):
    state_path = os.path.join(output_dir, "trainer_state.json")
    if not os.path.exists(state_path):
        for d in sorted(os.listdir(output_dir)):
            sp = os.path.join(output_dir, d, "trainer_state.json")
            if os.path.exists(sp):
                state_path = sp
                break
    if not os.path.exists(state_path):
        return float("nan")
    with open(state_path) as f:
        state = json.load(f)
    best = float("inf")
    for entry in state.get("log_history", []):
        if "eval_loss" in entry:
            best = min(best, entry["eval_loss"])
    return best if best < float("inf") else float("nan")


def eval_model(adapter_path, base_model_path, model_name):
    """Run generative evaluation using eval_routing_metrics.run_eval."""
    src_dir = os.path.join(PROJECT_ROOT, "src")
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    from eval_routing_metrics import run_eval

    output_path = os.path.join(RESULTS_DIR, f"eval_{model_name}.json")
    resolved_base = resolve_model_path(base_model_path)

    print(f"\n{'='*60}")
    print(f"Evaluating {model_name}")
    print(f"  adapter: {adapter_path}")
    print(f"  base: {resolved_base}")
    print(f"{'='*60}\n", flush=True)

    results = run_eval(
        adapter_path=adapter_path,
        base_model=resolved_base,
        data_dir=DATA_DIR,
        gpu_id=DEVICE_ID,
        max_new_tokens=128,
        output_path=output_path,
    )
    return results


def main():
    parser = argparse.ArgumentParser(description="Plan-008 v2: Router Size Ablation")
    parser.add_argument("--dry-run", action="store_true", help="1 epoch, confirm no errors")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--eval-only", action="store_true", help="Skip training, eval existing checkpoints")
    args = parser.parse_args()

    epochs = 1 if args.dry_run else args.epochs
    os.makedirs(RESULTS_DIR, exist_ok=True)

    summary = {"models": {}, "timestamp": datetime.now().isoformat(), "seed": SEED}

    for cfg in MODELS:
        name = cfg["name"]
        print(f"\n{'#'*60}")
        print(f"# Model: {name}")
        print(f"{'#'*60}")

        # Train
        if not args.eval_only:
            output_dir = train_model(cfg, epochs)
            if output_dir is None:
                summary["models"][name] = {"status": "TRAIN_FAILED"}
                continue
        else:
            output_dir = cfg["output_dir"]
            if not os.path.exists(os.path.join(output_dir, "TRAINING_COMPLETE")):
                print(f"Skipping {name}: no TRAINING_COMPLETE sentinel")
                summary["models"][name] = {"status": "NO_CHECKPOINT"}
                continue

        # Eval loss from trainer
        eval_loss = get_eval_loss(output_dir)

        # Generative eval
        adapter_path = os.path.join(output_dir, "final_adapter")
        try:
            eval_results = eval_model(adapter_path, cfg["model_path"], name)
            model_metrics = {
                "status": "OK",
                "eval_loss": round(eval_loss, 4) if eval_loss == eval_loss else None,
                "balanced_accuracy": eval_results.get("balanced_accuracy"),
                "accuracy": eval_results.get("accuracy"),
                "internal_recall": eval_results.get("internal_recall"),
                "internal_precision": eval_results.get("internal_precision"),
                "internal_f1": eval_results.get("internal_f1"),
                "det_recall": eval_results.get("det_recall"),
                "det_precision": eval_results.get("det_precision"),
                "det_f1": eval_results.get("det_f1"),
                "confusion_matrix": eval_results.get("confusion_matrix"),
                "val_size": eval_results.get("val_size"),
                "val_label_dist": eval_results.get("val_label_dist"),
                "pred_dist": eval_results.get("pred_dist"),
                "batch_size": cfg["batch_size"],
                "gradient_accumulation_steps": cfg["gradient_accumulation_steps"],
                "checkpoint_dir": output_dir,
            }
        except Exception as e:
            print(f"ERROR: Eval failed for {name}: {e}")
            import traceback
            traceback.print_exc()
            model_metrics = {
                "status": "EVAL_FAILED",
                "eval_loss": round(eval_loss, 4) if eval_loss == eval_loss else None,
                "error": str(e),
            }

        summary["models"][name] = model_metrics

        # Save intermediate
        intermediate_path = os.path.join(RESULTS_DIR, f"result_{name}.json")
        with open(intermediate_path, "w") as f:
            json.dump(model_metrics, f, indent=2)
        print(f"[Saved] {intermediate_path}")

        # Free GPU memory between models
        import torch
        import gc
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    # Summary
    summary_path = os.path.join(RESULTS_DIR, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'='*60}")
    print(f"DONE — {summary_path}")
    print(f"{'='*60}")
    for name, m in summary["models"].items():
        if m.get("status") == "OK":
            print(f"  {name}: bal_acc={m['balanced_accuracy']}, "
                  f"int_recall={m['internal_recall']}, det_recall={m['det_recall']}, "
                  f"eval_loss={m['eval_loss']}")
        else:
            print(f"  {name}: {m.get('status', 'UNKNOWN')}")


if __name__ == "__main__":
    main()
