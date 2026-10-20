"""批量评估: 遍历 {实验}×{checkpoint} 组合，调用 inference.py 并汇总 metrics。

用法:
    python -m freige.eval.batch_eval \
        --experiments /root/autodl-tmp/grpo_ced_r5,/root/autodl-tmp/grpo_extract_r3 \
        --base_model /root/autodl-tmp/models/Qwen3-4B \
        --sft_adapter /root/autodl-tmp/sft_output \
        --data_path /root/autodl-tmp/data/docred \
        --output_dir /root/autodl-tmp/eval_results/batch \
        --checkpoints best,last
"""

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

from freige.eval.find_best_checkpoint import find_best_checkpoint


SUMMARY_METRICS = ["f1", "ign_f1", "evi_f1", "edcr", "format_ok_rate", "n_predictions", "n_truncated"]


def discover_checkpoints(exp_dir: Path) -> list[Path]:
    dirs = sorted(exp_dir.glob("checkpoint-*"), key=lambda p: int(p.name.split("-")[-1]))
    return dirs


def resolve_checkpoints(exp_dir: Path, mode: str) -> list[Path]:
    """根据 --checkpoints 参数解析要评估的 checkpoint 列表。"""
    all_ckpts = discover_checkpoints(exp_dir)
    if not all_ckpts:
        print(f"WARNING: no checkpoints in {exp_dir}", file=sys.stderr)
        return []

    if mode == "all":
        return all_ckpts

    tokens = [t.strip() for t in mode.split(",")]
    result = []
    seen = set()

    for tok in tokens:
        if tok == "last":
            path = all_ckpts[-1]
            if path not in seen:
                result.append(path)
                seen.add(path)
        elif tok == "best":
            info = find_best_checkpoint(str(exp_dir))
            if info:
                path = Path(info["path"])
                if path not in seen:
                    result.append(path)
                    seen.add(path)
            else:
                print(f"WARNING: could not find best checkpoint for {exp_dir}", file=sys.stderr)
        else:
            path = exp_dir / f"checkpoint-{tok}"
            if path.is_dir():
                if path not in seen:
                    result.append(path)
                    seen.add(path)
            else:
                print(f"WARNING: {path} does not exist, skipping", file=sys.stderr)

    return result


def run_single_eval(
    checkpoint_path: Path,
    base_model: str,
    sft_adapter: str | None,
    data_path: str,
    split: str,
    output_dir: Path,
    batch_size: int,
) -> dict | None:
    """调用 inference.py 评估单个 checkpoint，返回 metrics dict。"""
    output_dir.mkdir(parents=True, exist_ok=True)

    metrics_path = output_dir / "metrics.json"
    if metrics_path.exists():
        print(f"  SKIP (already evaluated): {metrics_path}")
        with open(metrics_path) as f:
            return json.load(f)

    cmd = [
        sys.executable, "-m", "freige.eval.inference",
        "--model_path", str(checkpoint_path),
        "--base_model", base_model,
        "--data_path", data_path,
        "--split", split,
        "--output_dir", str(output_dir),
        "--batch_size", str(batch_size),
    ]
    if sft_adapter:
        cmd.extend(["--sft_adapter", sft_adapter])

    print(f"  CMD: {' '.join(cmd)}")
    proc = subprocess.run(cmd, capture_output=True, text=True)

    if proc.returncode != 0:
        print(f"  FAILED (exit {proc.returncode}):", file=sys.stderr)
        print(proc.stderr[-2000:] if len(proc.stderr) > 2000 else proc.stderr, file=sys.stderr)
        err_path = output_dir / "error.log"
        err_path.write_text(f"STDOUT:\n{proc.stdout}\n\nSTDERR:\n{proc.stderr}")
        return None

    if metrics_path.exists():
        with open(metrics_path) as f:
            return json.load(f)

    print(f"  WARNING: inference completed but {metrics_path} not found", file=sys.stderr)
    return None


def write_summary(results: list[dict], output_dir: Path):
    """将所有结果写入 summary.json 和 summary.csv。"""
    summary_json = output_dir / "summary.json"
    with open(summary_json, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSummary JSON: {summary_json}")

    if not results:
        return

    csv_path = output_dir / "summary.csv"
    fieldnames = ["experiment", "checkpoint", "step"] + SUMMARY_METRICS
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            row = {
                "experiment": r["experiment"],
                "checkpoint": r["checkpoint"],
                "step": r["step"],
            }
            metrics = r.get("metrics", {})
            for m in SUMMARY_METRICS:
                val = metrics.get(m, "")
                if isinstance(val, float):
                    val = round(val, 6)
                row[m] = val
            writer.writerow(row)
    print(f"Summary CSV:  {csv_path}")

    print(f"\n{'='*80}")
    print(f"{'Experiment':<30} {'Ckpt':<15} {'F1':>8} {'Ign-F1':>8} {'Evi-F1':>8} {'EDCR':>8} {'FmtOK':>8}")
    print(f"{'-'*80}")
    for r in results:
        m = r.get("metrics", {})
        status = "FAIL" if m == {} else ""
        print(
            f"{r['experiment']:<30} {r['checkpoint']:<15} "
            f"{m.get('f1', 0):>8.4f} {m.get('ign_f1', 0):>8.4f} "
            f"{m.get('evi_f1', 0):>8.4f} {m.get('edcr', 0):>8.4f} "
            f"{m.get('format_ok_rate', 0):>7.1%} {status}"
        )
    print(f"{'='*80}")


def main():
    parser = argparse.ArgumentParser(description="Batch evaluation across experiments × checkpoints.")
    parser.add_argument("--experiments", required=True,
                        help="Comma-separated experiment dirs (e.g. /path/grpo_ced_r5,/path/grpo_extract_r3)")
    parser.add_argument("--base_model", default="/root/autodl-tmp/models/Qwen3-4B",
                        help="Base model path (default: Qwen3-4B)")
    parser.add_argument("--sft_adapter", default=None,
                        help="SFT adapter path (for GRPO checkpoints)")
    parser.add_argument("--data_path", required=True,
                        help="DocRED data directory")
    parser.add_argument("--split", default="dev", choices=["dev", "test"])
    parser.add_argument("--checkpoints", default="best,last",
                        help="'all' / 'best,last' / comma-separated step numbers (default: best,last)")
    parser.add_argument("--output_dir", required=True,
                        help="Directory for aggregated results")
    parser.add_argument("--batch_size", type=int, default=8,
                        help="Batch size for inference (default: 8)")
    args = parser.parse_args()

    exp_dirs = [Path(p.strip()) for p in args.experiments.split(",")]
    output_root = Path(args.output_dir)
    output_root.mkdir(parents=True, exist_ok=True)

    all_results = []
    total = 0
    success = 0

    for exp_dir in exp_dirs:
        exp_name = exp_dir.name
        print(f"\n{'='*60}")
        print(f"Experiment: {exp_name} ({exp_dir})")

        if not exp_dir.is_dir():
            print(f"  ERROR: directory does not exist, skipping", file=sys.stderr)
            continue

        ckpts = resolve_checkpoints(exp_dir, args.checkpoints)
        if not ckpts:
            print(f"  No checkpoints to evaluate")
            continue

        print(f"  Checkpoints: {[c.name for c in ckpts]}")

        for ckpt_path in ckpts:
            total += 1
            ckpt_name = ckpt_path.name
            step = int(ckpt_name.split("-")[-1])
            eval_output = output_root / exp_name / ckpt_name

            print(f"\n  [{total}] {exp_name}/{ckpt_name} (step {step})")

            metrics = run_single_eval(
                checkpoint_path=ckpt_path,
                base_model=args.base_model,
                sft_adapter=args.sft_adapter,
                data_path=args.data_path,
                split=args.split,
                output_dir=eval_output,
                batch_size=args.batch_size,
            )

            entry = {
                "experiment": exp_name,
                "checkpoint": ckpt_name,
                "step": step,
                "metrics": metrics or {},
                "output_dir": str(eval_output),
            }
            all_results.append(entry)

            if metrics:
                success += 1
                print(f"  → F1={metrics.get('f1', 0):.4f}  Evi-F1={metrics.get('evi_f1', 0):.4f}")

    print(f"\n\nCompleted: {success}/{total} evaluations succeeded")
    write_summary(all_results, output_root)


if __name__ == "__main__":
    main()
