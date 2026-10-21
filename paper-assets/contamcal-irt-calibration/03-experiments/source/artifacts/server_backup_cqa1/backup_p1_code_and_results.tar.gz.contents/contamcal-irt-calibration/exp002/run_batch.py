"""
Batch runner for exp-002 signal pipeline.

Orchestrates compute_signals.py across all (dosage, benchmark) combos for a given
model size. Supports dry-run, GPU selection, resume (skips completed tasks), and
parallel or sequential execution.

Usage:
  python run_batch.py --model-size 0.5B --dry-run           # verify pipeline
  python run_batch.py --model-size 0.5B --gpu 3             # run all on GPU 3
  python run_batch.py --model-size 0.5B --gpu 3 --only d005 # single dosage
"""

import argparse
import json
import logging
import os
import subprocess
import sys
from pathlib import Path

os.environ.setdefault("HF_DATASETS_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")

logger = logging.getLogger(__name__)

# --- Path conventions ---
CHECKPOINT_ROOT = "/root/autodl-tmp/exp001/checkpoints"
SFT_DATA_ROOT = "/root/autodl-tmp/exp001/sft_data"
EVAL_RESULTS_ROOT = "/root/autodl-tmp/exp001/eval_results"
OUTPUT_ROOT = "/root/autodl-tmp/exp002/signals"
LABELS_ROOT = "/root/autodl-tmp/exp001/sft_data"
CACHE_DIR = "/root/autodl-tmp/.hf_cache"
BASE_MODEL_ROOT = "/root/autodl-tmp/.hf_cache/Qwen"

DOSAGES = ["d000", "d005", "d025", "d100"]
BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]
SEED = "s42"

MODEL_SIZE_TO_NAME = {
    "0.5B": "Qwen2.5-0.5B",
    "1.5B": "Qwen2.5-1.5B",
    "3B": "Qwen2.5-3B",
}

DOSAGE_TO_NUM = {"d000": "000", "d005": "005", "d025": "025", "d050": "050", "d100": "100"}


def checkpoint_path(model_name: str, dosage: str) -> str:
    return f"{CHECKPOINT_ROOT}/{model_name}_{dosage}_{SEED}/lora_adapter"


def base_model_path(model_name: str) -> str:
    return f"{BASE_MODEL_ROOT}/{model_name}"


def sft_data_path(dosage: str) -> str:
    return f"{SFT_DATA_ROOT}/sft_dosage_{DOSAGE_TO_NUM[dosage]}.jsonl"


def ref_checkpoint_path(model_name: str) -> str:
    """D016: reference model = 0% dosage fine-tuned model."""
    return checkpoint_path(model_name, "d000")


def eval_results_path(model_name: str, dosage: str) -> str:
    return f"{EVAL_RESULTS_ROOT}/{model_name}_{dosage}_{SEED}/eval_results.json"


def para_eval_results_path(model_name: str, dosage: str) -> str:
    return f"{EVAL_RESULTS_ROOT}/{model_name}_{dosage}_{SEED}_para/eval_results.json"


def labels_path(benchmark: str, dosage: str) -> str:
    return f"{LABELS_ROOT}/contamination_labels_{benchmark}_{dosage}.json"


def output_dir_for(model_name: str, dosage: str) -> str:
    return f"{OUTPUT_ROOT}/{model_name}_{dosage}_{SEED}"


def merged_output_exists(model_name: str, dosage: str, benchmark: str) -> bool:
    outdir = output_dir_for(model_name, dosage)
    merged = Path(outdir) / f"signals_merged_{benchmark}.json"
    return merged.exists()


def build_task(model_name: str, dosage: str, benchmark: str, gpu: str,
               dry_run: bool, max_items: int) -> dict:
    """Build a single signal computation task."""
    ckpt = checkpoint_path(model_name, dosage)
    ref_ckpt = ref_checkpoint_path(model_name)
    base = base_model_path(model_name)
    outdir = output_dir_for(model_name, dosage)

    cmd = [
        sys.executable, "compute_signals.py",
        "--model-path", base,
        "--adapter-path", ckpt,
        "--benchmark", benchmark,
        "--signal", "all",
        "--ref-model-path", ref_ckpt,
        "--sft-data-dir", SFT_DATA_ROOT,
        "--output-dir", outdir,
        "--cache-dir", CACHE_DIR,
    ]

    # ConStat (S3): pass eval paths if available
    orig_eval = eval_results_path(model_name, dosage)
    para_eval = para_eval_results_path(model_name, dosage)
    if os.path.exists(orig_eval) and os.path.exists(para_eval):
        cmd.extend(["--original-eval-paths", orig_eval])
        cmd.extend(["--paraphrase-eval-paths", para_eval])

    model_id = f"{model_name}_{dosage}_{SEED}"
    return {
        "model_id": model_id,
        "dosage": dosage,
        "benchmark": benchmark,
        "signals": "all",
        "gpu": gpu,
        "cmd": cmd,
        "outdir": outdir,
    }


def main():
    parser = argparse.ArgumentParser(description="Batch runner for exp-002 signal pipeline")
    parser.add_argument("--model-size", type=str, required=True,
                        choices=list(MODEL_SIZE_TO_NAME.keys()))
    parser.add_argument("--gpu", type=str, default=None,
                        help="GPU device ID (e.g., '3')")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run each task on max 5 items")
    parser.add_argument("--max-items", type=int, default=None,
                        help="Max items per benchmark (overrides dry-run default)")
    parser.add_argument("--only", type=str, nargs="+", default=None,
                        help="Run only specific dosages (e.g., --only d005 d100)")
    parser.add_argument("--only-benchmarks", type=str, nargs="+", default=None,
                        help="Run only specific benchmarks (e.g., --only-benchmarks mmlu)")
    parser.add_argument("--skip-completed", action="store_true", default=True,
                        help="Skip tasks with existing merged output (default: True)")
    parser.add_argument("--no-skip", action="store_true",
                        help="Force re-run even if output exists")
    parser.add_argument("--print-only", action="store_true",
                        help="Print commands without executing")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    model_name = MODEL_SIZE_TO_NAME[args.model_size]
    dosages = args.only if args.only else DOSAGES
    benchmarks = args.only_benchmarks if args.only_benchmarks else BENCHMARKS
    skip_completed = not args.no_skip

    # Build task list
    tasks = []
    skipped = []
    for dosage in dosages:
        ckpt = checkpoint_path(model_name, dosage)
        if not os.path.exists(ckpt):
            logger.warning("Checkpoint not found, skipping: %s", ckpt)
            continue
        for benchmark in benchmarks:
            if skip_completed and merged_output_exists(model_name, dosage, benchmark):
                skipped.append(f"{model_name}_{dosage}_{SEED}/{benchmark}")
                continue
            task = build_task(model_name, dosage, benchmark, args.gpu,
                              args.dry_run, args.max_items)
            tasks.append(task)

    # Summary
    logger.info("=" * 60)
    logger.info("exp-002 Signal Pipeline Batch Runner")
    logger.info("=" * 60)
    logger.info("Model: %s (%s)", model_name, args.model_size)
    logger.info("Dosages: %s", dosages)
    logger.info("Benchmarks: %s", benchmarks)
    logger.info("Tasks to run: %d", len(tasks))
    logger.info("Skipped (completed): %d %s", len(skipped),
                skipped if skipped else "")
    logger.info("Dry-run: %s", args.dry_run)
    logger.info("GPU: %s", args.gpu or "auto")
    logger.info("=" * 60)

    if args.print_only:
        for task in tasks:
            print(f"\n# {task['model_id']} / {task['benchmark']} ({task['signals']})")
            print(" ".join(task["cmd"]))
        return

    # Execute tasks sequentially
    results = {}
    for i, task in enumerate(tasks, 1):
        task_id = f"{task['model_id']}/{task['benchmark']}"
        logger.info("[%d/%d] Running: %s (signals: %s)", i, len(tasks),
                    task_id, task["signals"])

        try:
            env = os.environ.copy()
            if task.get("gpu") is not None and "CUDA_VISIBLE_DEVICES" not in os.environ:
                env["CUDA_VISIBLE_DEVICES"] = str(task["gpu"])
            result = subprocess.run(
                task["cmd"],
                cwd="/root/contamcal-irt-calibration/exp002",
                capture_output=True, text=True, timeout=14400,
                env=env,
            )
            if result.returncode == 0:
                results[task_id] = "PASS"
                logger.info("[%d/%d] PASS: %s", i, len(tasks), task_id)
            else:
                results[task_id] = f"FAIL (rc={result.returncode})"
                logger.error("[%d/%d] FAIL: %s\nstderr: %s", i, len(tasks),
                             task_id, result.stderr[-500:])
        except subprocess.TimeoutExpired:
            results[task_id] = "TIMEOUT"
            logger.error("[%d/%d] TIMEOUT: %s", i, len(tasks), task_id)
        except Exception as e:
            results[task_id] = f"ERROR: {e}"
            logger.error("[%d/%d] ERROR: %s — %s", i, len(tasks), task_id, e)

    # Summary
    logger.info("\n" + "=" * 60)
    logger.info("BATCH SUMMARY")
    logger.info("=" * 60)
    for task_id, status in results.items():
        marker = "PASS" if status == "PASS" else "FAIL"
        logger.info("  [%s] %s: %s", marker, task_id, status)

    n_pass = sum(1 for v in results.values() if v == "PASS")
    n_total = len(results)
    logger.info("Result: %d/%d passed", n_pass, n_total)

    # Write batch report
    report_path = Path(OUTPUT_ROOT) / f"batch_report_{model_name}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "model_name": model_name,
        "model_size": args.model_size,
        "dry_run": args.dry_run,
        "tasks_run": n_total,
        "tasks_passed": n_pass,
        "skipped": skipped,
        "results": results,
    }
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    logger.info("Batch report saved to %s", report_path)

    sys.exit(0 if n_pass == n_total else 1)


if __name__ == "__main__":
    main()
