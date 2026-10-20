"""批量评估 GRPO 实验的多个 checkpoint。

用法:
    python -m freige.eval.batch_eval \
        --exp_dir ./outputs \
        --sft_adapter ./outputs \
        --output_dir ./outputs/eval_results
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def discover_checkpoints(exp_dir: Path) -> list[tuple[int, Path]]:
    """发现所有 checkpoint-N 子目录，按 step 排序。"""
    pattern = re.compile(r"^checkpoint-(\d+)$")
    results = []
    for d in exp_dir.iterdir():
        if d.is_dir():
            m = pattern.match(d.name)
            if m:
                results.append((int(m.group(1)), d))
    results.sort(key=lambda x: x[0])
    return results


def load_metrics(metrics_path: Path) -> dict | None:
    if metrics_path.exists():
        with open(metrics_path) as f:
            return json.load(f)
    return None


def run_eval(checkpoint_path: Path, sft_adapter: str, output_dir: Path,
             base_model: str, data_path: str, split: str,
             batch_size: int, max_new_tokens: int, seed: int,
             quantize: bool) -> dict | None:
    """运行单个 checkpoint 的评测，返回 metrics dict 或 None。"""
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable, "-m", "freige.eval.inference",
        "--model_path", str(checkpoint_path),
        "--sft_adapter", sft_adapter,
        "--base_model", base_model,
        "--data_path", data_path,
        "--split", split,
        "--batch_size", str(batch_size),
        "--max_new_tokens", str(max_new_tokens),
        "--seed", str(seed),
        "--output_dir", str(output_dir),
    ]
    if quantize:
        cmd.append("--quantize")
    else:
        cmd.append("--no-quantize")

    print(f"\n{'='*60}")
    print(f"[{datetime.now():%H:%M:%S}] Evaluating: {checkpoint_path.name}")
    print(f"  Output: {output_dir}")
    print(f"  Command: {' '.join(cmd)}")
    print(f"{'='*60}\n")

    result = subprocess.run(cmd, cwd=str(checkpoint_path.parent.parent))
    if result.returncode != 0:
        print(f"[ERROR] {checkpoint_path.name} eval failed (exit {result.returncode})")
        return None

    return load_metrics(output_dir / "metrics.json")


def main():
    parser = argparse.ArgumentParser(description="批量评估 GRPO checkpoints")
    parser.add_argument("--exp_dir", required=True,
                        help="实验输出目录（含 checkpoint-N 子目录）")
    parser.add_argument("--sft_adapter", required=True,
                        help="SFT adapter 路径")
    parser.add_argument("--output_dir", required=True,
                        help="评测结果输出目录")
    parser.add_argument("--base_model", default="./outputs")
    parser.add_argument("--data_path", default="./data/docred")
    parser.add_argument("--split", default="dev", choices=["dev", "test"])
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--resume", action="store_true",
                        help="跳过已有 metrics.json 的 checkpoint")
    parser.add_argument("--checkpoints", type=str, default=None,
                        help="指定要评测的 checkpoint（逗号分隔 step 数，如 '100,200,300'）")
    args = parser.parse_args()

    exp_dir = Path(args.exp_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    checkpoints = discover_checkpoints(exp_dir)
    if not checkpoints:
        print(f"[ERROR] No checkpoints found in {exp_dir}")
        sys.exit(1)

    if args.checkpoints:
        selected = set(int(s.strip()) for s in args.checkpoints.split(","))
        checkpoints = [(step, p) for step, p in checkpoints if step in selected]

    print(f"Found {len(checkpoints)} checkpoints: {[s for s, _ in checkpoints]}")

    summary = {}
    skipped = 0
    failed = 0

    for step, ckpt_path in checkpoints:
        ckpt_output = output_dir / ckpt_path.name

        if args.resume:
            existing = load_metrics(ckpt_output / "metrics.json")
            if existing:
                print(f"[SKIP] {ckpt_path.name} — already evaluated")
                summary[ckpt_path.name] = {
                    "step": step,
                    "f1": existing.get("f1"),
                    "ign_f1": existing.get("ign_f1"),
                    "evi_f1": existing.get("evi_f1"),
                    "evi_f1_joint": existing.get("evi_f1_joint"),
                    "edcr": existing.get("edcr"),
                    "format_ok_rate": existing.get("format_ok_rate"),
                }
                skipped += 1
                continue

        metrics = run_eval(
            ckpt_path, args.sft_adapter, ckpt_output,
            args.base_model, args.data_path, args.split,
            args.batch_size, args.max_new_tokens, args.seed,
            args.quantize,
        )
        if metrics:
            summary[ckpt_path.name] = {
                "step": step,
                "f1": metrics.get("f1"),
                "ign_f1": metrics.get("ign_f1"),
                "evi_f1": metrics.get("evi_f1"),
                "evi_f1_joint": metrics.get("evi_f1_joint"),
                "edcr": metrics.get("edcr"),
                "format_ok_rate": metrics.get("format_ok_rate"),
            }
        else:
            failed += 1

    summary_path = output_dir / "summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n{'='*60}")
    print(f"Summary saved to {summary_path}")
    print(f"  Total: {len(checkpoints)}, Evaluated: {len(summary) - skipped}, Skipped: {skipped}, Failed: {failed}")

    if summary:
        best_key = max(
            (k for k in summary if summary[k].get("f1") is not None),
            key=lambda k: summary[k]["f1"],
            default=None,
        )
        if best_key:
            b = summary[best_key]
            print(f"\n  Best by F1: {best_key} (step {b['step']})")
            print(f"    F1={b['f1']:.4f}  Ign-F1={b['ign_f1']:.4f}  Evi-F1(DREEAM)={b.get('evi_f1_joint',0):.4f}  Evi-F1(TP)={b['evi_f1']:.4f}  EDCR={b.get('edcr', 0):.4f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
