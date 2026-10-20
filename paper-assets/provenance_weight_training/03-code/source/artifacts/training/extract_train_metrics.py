#!/usr/bin/env python3
"""Extract train_loss and other metrics from HuggingFace Trainer output.

Two sources, tried in order:
  1. trainer_state.json in output_dir (ground truth from HF Trainer)
  2. stdout log file — parse the final summary dict printed by Trainer

Usage:
  python extract_train_metrics.py --output_dir /path/to/output/model_dir
  python extract_train_metrics.py --log_file /path/to/training.log
  python extract_train_metrics.py --output_dir /path/to/dir --log_file /path/to/log

Output: JSON dict to stdout with keys: train_loss, train_runtime, train_steps_per_second,
        train_samples_per_second, total_steps, epoch, source (which method succeeded).
"""
import argparse
import json
import os
import re
import sys
import glob


def from_trainer_state(output_dir: str) -> dict | None:
    """Extract from trainer_state.json (most reliable)."""
    candidates = [
        os.path.join(output_dir, "trainer_state.json"),
        os.path.join(output_dir, "final", "trainer_state.json"),
    ]
    for ckpt in sorted(glob.glob(os.path.join(output_dir, "checkpoint-*")),
                        key=lambda p: int(p.split("-")[-1]), reverse=True):
        candidates.append(os.path.join(ckpt, "trainer_state.json"))

    for path in candidates:
        if os.path.isfile(path):
            with open(path) as f:
                state = json.load(f)
            result = {}
            if "train_loss" in state:
                result["train_loss"] = state["train_loss"]
            if "log_history" in state and state["log_history"]:
                last = state["log_history"][-1]
                for key in ["train_loss", "train_runtime", "train_samples_per_second",
                            "train_steps_per_second", "total_flos", "epoch"]:
                    if key in last and key not in result:
                        result[key] = last[key]
            if "max_steps" in state:
                result["total_steps"] = state["max_steps"]
            if "train_loss" in result:
                result["source"] = f"trainer_state:{path}"
                return result
    return None


def from_log_file(log_file: str) -> dict | None:
    """Extract from stdout log by finding the HF Trainer summary dict.

    HF Trainer prints a line like:
      {'train_runtime': 12955.83, ..., 'train_loss': 10.7422, 'epoch': 0.26}
    at the very end of training. We parse that specific line.
    """
    if not os.path.isfile(log_file):
        return None

    summary_pattern = re.compile(
        r"\{[^{}]*'train_loss'\s*:\s*[\d.]+[^{}]*'train_runtime'\s*:\s*[\d.]+[^{}]*\}"
        r"|"
        r"\{[^{}]*'train_runtime'\s*:\s*[\d.]+[^{}]*'train_loss'\s*:\s*[\d.]+[^{}]*\}"
    )

    with open(log_file) as f:
        lines = f.readlines()

    for line in reversed(lines):
        line = line.strip()
        m = summary_pattern.search(line)
        if m:
            dict_str = m.group(0).replace("'", '"')
            try:
                data = json.loads(dict_str)
                if "train_loss" in data:
                    data["source"] = f"log_file:{log_file}"
                    return data
            except json.JSONDecodeError:
                continue

    # Fallback: look for train_loss in any dict-like line near end
    for line in reversed(lines[-50:]):
        line = line.strip()
        if "train_loss" in line and "train_runtime" in line:
            try:
                dict_str = line.replace("'", '"')
                lbrace = dict_str.index("{")
                rbrace = dict_str.rindex("}") + 1
                data = json.loads(dict_str[lbrace:rbrace])
                if "train_loss" in data:
                    data["source"] = f"log_file:{log_file}"
                    return data
            except (json.JSONDecodeError, ValueError):
                continue

    return None


def main():
    parser = argparse.ArgumentParser(description="Extract HF Trainer metrics")
    parser.add_argument("--output_dir", help="Model output directory")
    parser.add_argument("--log_file", help="Training stdout log file")
    args = parser.parse_args()

    if not args.output_dir and not args.log_file:
        print(json.dumps({"error": "Provide --output_dir and/or --log_file"}))
        sys.exit(1)

    result = None
    if args.output_dir:
        result = from_trainer_state(args.output_dir)
    if result is None and args.log_file:
        result = from_log_file(args.log_file)

    if result is None:
        print(json.dumps({"error": "Could not find train_loss in any source"}))
        sys.exit(1)

    print(json.dumps(result))


if __name__ == "__main__":
    main()
