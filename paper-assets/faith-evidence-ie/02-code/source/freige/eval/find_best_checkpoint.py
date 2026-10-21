"""从训练日志找到 reward 最高的 checkpoint。

用法:
    # 从 trainer_state.json（最后一个 checkpoint 包含完整历史）
    python -m freige.eval.find_best_checkpoint \
        --log_path ./outputs

    # 从实验目录（自动找最新的 trainer_state.json）
    python -m freige.eval.find_best_checkpoint \
        --exp_dir ./outputs

    # 指定排序指标
    python -m freige.eval.find_best_checkpoint \
        --exp_dir ./outputs \
        --sort_by rewards/f1_reward_fn/mean
"""

import argparse
import json
import re
import sys
from pathlib import Path


def find_latest_trainer_state(exp_dir: Path) -> Path | None:
    """找到实验目录中 step 最大的 checkpoint 的 trainer_state.json。"""
    pattern = re.compile(r"^checkpoint-(\d+)$")
    candidates = []
    for d in exp_dir.iterdir():
        if d.is_dir():
            m = pattern.match(d.name)
            if m:
                ts = d / "trainer_state.json"
                if ts.exists():
                    candidates.append((int(m.group(1)), ts))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    return candidates[-1][1]


def parse_log_history(log_path: Path) -> list[dict]:
    """解析 trainer_state.json 中的 log_history。"""
    with open(log_path) as f:
        state = json.load(f)
    return state.get("log_history", [])


def extract_reward_entries(log_history: list[dict]) -> list[dict]:
    """从 log_history 提取包含 reward 的条目。"""
    entries = []
    for entry in log_history:
        if "reward" in entry and "step" in entry:
            reward_keys = [k for k in entry if k.startswith("rewards/") and k.endswith("/mean")]
            row = {
                "step": entry["step"],
                "total_reward": entry["reward"],
            }
            for k in reward_keys:
                short = k.replace("rewards/", "").replace("/mean", "")
                row[short] = entry[k]
            if "reward_std" in entry:
                row["reward_std"] = entry["reward_std"]
            entries.append(row)
    return entries


def main():
    parser = argparse.ArgumentParser(description="找到 reward 最高的训练 step/checkpoint")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--log_path",
                       help="trainer_state.json 路径")
    group.add_argument("--exp_dir",
                       help="实验目录（自动找最新 trainer_state.json）")
    parser.add_argument("--sort_by", default="total_reward",
                        help="排序指标（默认 total_reward，也可用 f1_reward_fn 等）")
    parser.add_argument("--top_k", type=int, default=5,
                        help="显示 top-K 个 step（默认 5）")
    parser.add_argument("--save_csv", type=str, default=None,
                        help="导出全部记录到 CSV 文件")
    args = parser.parse_args()

    if args.log_path:
        log_path = Path(args.log_path)
    else:
        exp_dir = Path(args.exp_dir)
        log_path = find_latest_trainer_state(exp_dir)
        if not log_path:
            print(f"[ERROR] No trainer_state.json found in {exp_dir}")
            sys.exit(1)
        print(f"Using: {log_path}")

    log_history = parse_log_history(log_path)
    entries = extract_reward_entries(log_history)
    if not entries:
        print("[ERROR] No reward entries found in log_history")
        sys.exit(1)

    sort_key = args.sort_by
    valid_keys = set()
    for e in entries:
        valid_keys.update(e.keys())
    if sort_key not in valid_keys:
        print(f"[ERROR] Key '{sort_key}' not found. Available: {sorted(valid_keys)}")
        sys.exit(1)

    entries_sorted = sorted(entries, key=lambda x: x.get(sort_key, 0), reverse=True)

    print(f"\nTotal training steps logged: {len(entries)}")
    print(f"Sorting by: {sort_key}\n")

    reward_cols = sorted(set(entries[0].keys()) - {"step", "reward_std"})
    header = f"{'Rank':<5} {'Step':<8}"
    for col in reward_cols:
        header += f" {col:<20}"
    print(header)
    print("-" * len(header))

    for i, entry in enumerate(entries_sorted[:args.top_k]):
        row = f"{i+1:<5} {entry['step']:<8}"
        for col in reward_cols:
            val = entry.get(col, 0)
            row += f" {val:<20.6f}"
        print(row)

    best = entries_sorted[0]
    step = best["step"]
    print(f"\nBest step: {step}")
    print(f"Checkpoint dir: checkpoint-{step}")
    for k, v in sorted(best.items()):
        if k != "step":
            print(f"  {k}: {v:.6f}")

    if args.save_csv:
        import csv
        csv_path = Path(args.save_csv)
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = ["step"] + sorted(set(entries[0].keys()) - {"step"})
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for entry in sorted(entries, key=lambda x: x["step"]):
                writer.writerow(entry)
        print(f"\nCSV saved to {csv_path}")


if __name__ == "__main__":
    main()
