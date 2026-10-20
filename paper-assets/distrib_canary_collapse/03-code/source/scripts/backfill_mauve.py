"""Backfill null mauve scores in iterative training metrics.

Scans experiment directories for gen_X/metrics.json with mauve=null,
recomputes mauve using cached gpt2-large, and updates metrics in-place.

Usage:
    python scripts/backfill_mauve.py --exp-dirs results/phase_diagram/t15_* --ref-data data/wikitext103_5k
    python scripts/backfill_mauve.py --exp-dirs results/phase_diagram/t15_* --dry-run  # scan only
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_HUB_OFFLINE"] = "1"

import argparse
import json
import glob
import shutil
import random
import multiprocessing as mp
from pathlib import Path


def find_null_mauve_gens(exp_dirs):
    """Scan experiment directories for gens with null mauve scores."""
    tasks = []
    for exp_dir in exp_dirs:
        exp_path = Path(exp_dir)
        if not exp_path.exists():
            print(f"[WARN] Experiment dir not found: {exp_dir}")
            continue
        gen_dirs = sorted(exp_path.glob("gen_*"), key=lambda p: int(p.name.split("_")[1]))
        for gen_dir in gen_dirs:
            metrics_path = gen_dir / "metrics.json"
            if not metrics_path.exists():
                print(f"[SKIP] No metrics.json: {gen_dir}")
                continue
            synth_path = gen_dir / "synthetic_data"
            if not synth_path.exists():
                print(f"[SKIP] No synthetic_data: {gen_dir}")
                continue
            with open(metrics_path) as f:
                metrics = json.load(f)
            if metrics.get("mauve") is not None:
                continue
            tasks.append({
                "gen_dir": str(gen_dir),
                "metrics_path": str(metrics_path),
                "synth_path": str(synth_path),
                "exp_name": exp_path.name,
                "gen_name": gen_dir.name,
            })
    return tasks


def compute_single(args):
    """Compute mauve for a single gen directory."""
    task, ref_data_path, gpu_id = args
    os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)

    import mauve
    from datasets import load_from_disk

    gen_dir = task["gen_dir"]
    metrics_path = task["metrics_path"]
    synth_path = task["synth_path"]
    label = f"{task['exp_name']}/{task['gen_name']}"

    try:
        synth_ds = load_from_disk(synth_path)
        gen_texts = synth_ds["text"]

        ref_ds = load_from_disk(ref_data_path)
        ref_texts = ref_ds["text"]
        n = len(gen_texts)
        if len(ref_texts) > n:
            random.seed(42)
            ref_texts = random.sample(list(ref_texts), n)
        elif len(ref_texts) < n:
            gen_texts = list(gen_texts)[:len(ref_texts)]

        print(f"[COMPUTE] {label}: {len(gen_texts)} texts, GPU {gpu_id}")
        result = mauve.compute_mauve(
            p_text=list(ref_texts),
            q_text=list(gen_texts),
            featurize_model_name="gpt2-large",
            max_text_length=256,
            device_id=0,  # 0 because CUDA_VISIBLE_DEVICES remaps
        )
        score = float(result.mauve)

        # Backup and update metrics
        shutil.copy2(metrics_path, metrics_path + ".bak")
        with open(metrics_path) as f:
            metrics = json.load(f)
        metrics["mauve"] = score
        with open(metrics_path, "w") as f:
            json.dump(metrics, f, indent=2)

        print(f"[DONE] {label}: mauve={score:.6f}")
        return label, score, None

    except Exception as e:
        print(f"[ERROR] {label}: {e}")
        return label, None, str(e)


def main():
    parser = argparse.ArgumentParser(description="Backfill null mauve scores")
    parser.add_argument("--exp-dirs", nargs="+", required=True, help="Experiment directories")
    parser.add_argument("--ref-data", default="data/wikitext103_5k", help="Reference dataset path")
    parser.add_argument("--num-gpus", type=int, default=1, help="Number of GPUs for parallel computation")
    parser.add_argument("--dry-run", action="store_true", help="Scan only, don't compute")
    parser.add_argument("--max-gens", type=int, default=None, help="Max gens to process (for testing)")
    args = parser.parse_args()

    # Expand globs in exp-dirs (shell may not expand them)
    exp_dirs = []
    for d in args.exp_dirs:
        expanded = sorted(glob.glob(d))
        if expanded:
            exp_dirs.extend(expanded)
        else:
            exp_dirs.append(d)

    print(f"Scanning {len(exp_dirs)} experiment directories...")
    tasks = find_null_mauve_gens(exp_dirs)

    if args.max_gens is not None:
        tasks = tasks[:args.max_gens]

    print(f"\nFound {len(tasks)} gens with null mauve:")
    for t in tasks:
        print(f"  {t['exp_name']}/{t['gen_name']}")

    if args.dry_run or not tasks:
        if not tasks:
            print("\nNothing to backfill.")
        return

    print(f"\nComputing mauve with {args.num_gpus} GPU(s)...")

    # Assign GPUs round-robin
    work_items = [(task, args.ref_data, i % args.num_gpus) for i, task in enumerate(tasks)]

    if args.num_gpus == 1:
        results = [compute_single(item) for item in work_items]
    else:
        with mp.Pool(args.num_gpus) as pool:
            results = pool.map(compute_single, work_items)

    # Summary
    success = sum(1 for _, s, _ in results if s is not None)
    failed = sum(1 for _, s, _ in results if s is None)
    print(f"\n{'='*60}")
    print(f"Backfill complete: {success} succeeded, {failed} failed")
    if failed:
        for label, _, err in results:
            if err:
                print(f"  FAILED: {label}: {err}")


if __name__ == "__main__":
    main()
