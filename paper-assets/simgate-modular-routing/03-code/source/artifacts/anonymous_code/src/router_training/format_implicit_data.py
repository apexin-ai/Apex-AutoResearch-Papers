"""Convert labeled step data to implicit SFT chat format.

Conversion: "det-preferred" label -> assistant = "[SIMULATE] {action}"
            "internal-preferred"  -> assistant = "{action}"

Input:  --data_dir results/counterfactual (reads {task}/labeled_steps.jsonl per task)
Output: --output_dir data/implicit_sft/implicit_sft.jsonl
"""

import argparse
import json
import os
import glob
from collections import Counter
from typing import List, Dict, Any, Optional

SIMULATE_PREFIX = "[SIMULATE]"

IMPLICIT_SYSTEM_PROMPT = (
    "You are an agent in a ScienceWorld text environment. "
    "Given the current observation and action history, choose the next action. "
    "If you believe a deterministic simulation would produce a better outcome, "
    "prefix your action with [SIMULATE]. Otherwise, output the action directly."
)

RAW_LABEL_MAP = {
    "internal-preferred": "internal",
    "det-preferred": "deterministic",
}


def format_record(record: Dict) -> Optional[Dict]:
    """Convert a labeled step to chat-format SFT record."""
    raw_label = record.get("label", "")
    route_label = RAW_LABEL_MAP.get(raw_label)
    if route_label is None:
        return None

    task_type = record.get("task_type", "unknown")
    observation = record.get("observation", "")
    action = record.get("action", "")
    action_history = record.get("action_history", [])

    history_str = " -> ".join(action_history[-5:]) if action_history else "(none)"

    user_content = (
        f"Task: {task_type}\n"
        f"Observation: {observation}\n"
        f"Action history: {history_str}\n"
        f"Choose your next action."
    )

    if route_label == "deterministic":
        assistant_content = f"{SIMULATE_PREFIX} {action}"
    else:
        assistant_content = action

    return {
        "messages": [
            {"role": "system", "content": IMPLICIT_SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content},
        ],
        "route_label": route_label,
        "task_type": task_type,
        "variation": record.get("variation", 0),
        "step_idx": record.get("step_idx", 0),
    }


def main():
    parser = argparse.ArgumentParser(description="Format labeled data for implicit SFT")
    parser.add_argument("--data_dir", type=str, default=None,
                        help="Directory with {task_type}/labeled_steps.jsonl")
    parser.add_argument("--data_path", type=str, default=None,
                        help="Single JSONL file (sft_triples.jsonl)")
    parser.add_argument("--output_dir", type=str, default="data/implicit_sft")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    files = []
    if args.data_path:
        files = [args.data_path]
    elif args.data_dir:
        files = sorted(glob.glob(os.path.join(args.data_dir, "*/labeled_steps.jsonl")))
        if not files:
            files = sorted(glob.glob(os.path.join(args.data_dir, "*.jsonl")))

    records = []
    for fp in files:
        with open(fp) as f:
            for line in f:
                if not line.strip():
                    continue
                raw = json.loads(line)
                formatted = format_record(raw)
                if formatted is not None:
                    records.append(formatted)

    out_path = os.path.join(args.output_dir, "implicit_sft.jsonl")
    with open(out_path, "w") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")

    label_counts = Counter(r["route_label"] for r in records)
    print(f"Formatted {len(records)} records -> {out_path}")
    print(f"Label distribution: {dict(label_counts)}")


if __name__ == "__main__":
    main()
