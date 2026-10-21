# Plan-004 Condition (b): Convert labeled step data to implicit SFT chat format.
#
# Input:  --data_dir results/plan_c (reads {task}/labeled_steps.jsonl per task)
#    or:  --sft_triples_path results/sft_data_death_aware/sft_triples.jsonl
# Output: --output_dir data/plan-004-implicit/implicit_sft.jsonl
#
# Conversion: "det-preferred" label → assistant = "[SIMULATE] {action}"
#             "internal-preferred"  → assistant = "{action}"
#
# Dependencies: none (standalone data formatting)

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
    "internal": "internal",
    "deterministic": "deterministic",
}


def format_action_history(history: List[str], max_actions: int = 5) -> str:
    recent = history[-max_actions:] if history else []
    if not recent:
        return "(none)"
    return " -> ".join(recent)


def convert_record(record: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Convert a labeled step record to chat-format SFT record.

    Returns None if the label is not recognized (e.g. no-preference).
    """
    raw_label = record.get("label", "")
    route = RAW_LABEL_MAP.get(raw_label)
    if route is None:
        return None

    obs = record["observation"]
    action = record["action"]
    history = record.get("action_history", [])

    user_content = (
        f"Observation: {obs}\n"
        f"Action history: {format_action_history(history)}"
    )

    if route == "deterministic":
        assistant_content = f"{SIMULATE_PREFIX} {action}"
    else:
        assistant_content = action

    return {
        "messages": [
            {"role": "system", "content": IMPLICIT_SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content},
        ],
        "task_type": record.get("task_type", record.get("task_name", "")),
        "variation": record.get("variation", -1),
        "step_idx": record.get("step_idx", -1),
        "route_label": route,
    }


def load_records_from_dir(data_dir: str) -> List[Dict]:
    """Load labeled_steps.jsonl from each task subdirectory."""
    pattern = os.path.join(data_dir, "*", "labeled_steps.jsonl")
    files = sorted(glob.glob(pattern))
    if not files:
        flat = os.path.join(data_dir, "labeled_steps.jsonl")
        if os.path.exists(flat):
            files = [flat]
    if not files:
        raise FileNotFoundError(f"No labeled_steps.jsonl found in {data_dir}")

    records = []
    for fpath in files:
        fallback_task = os.path.basename(os.path.dirname(fpath))
        with open(fpath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                if "task_type" not in rec and "task_name" not in rec:
                    rec["task_type"] = fallback_task
                records.append(rec)
    return records


def load_records_from_file(path: str) -> List[Dict]:
    """Load sft_triples.jsonl (single file)."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def convert_all(records: List[Dict], output_path: str) -> Dict[str, Any]:
    """Convert records and write implicit_sft.jsonl. Returns summary stats."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    stats = Counter()
    converted = []
    for rec in records:
        chat_rec = convert_record(rec)
        if chat_rec is None:
            stats["skipped"] += 1
            continue
        converted.append(chat_rec)
        stats[chat_rec["route_label"]] += 1
        stats["total"] += 1

    with open(output_path, "w") as f:
        for rec in converted:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    summary = {
        "output_path": output_path,
        "total_records": stats["total"],
        "deterministic_count": stats["deterministic"],
        "internal_count": stats["internal"],
        "skipped": stats["skipped"],
        "det_ratio": stats["deterministic"] / stats["total"] if stats["total"] > 0 else 0,
    }

    print(f"Converted {summary['total_records']} records ({summary['skipped']} skipped)")
    print(f"  deterministic: {summary['deterministic_count']} ({summary['det_ratio']:.1%})")
    print(f"  internal:      {summary['internal_count']}")
    print(f"  output: {output_path}")
    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Convert labeled step data to implicit SFT chat format for Plan-004 Condition (b)"
    )
    parser.add_argument("--data_dir", type=str, default=None,
                        help="Directory with {task}/labeled_steps.jsonl (e.g. results/plan_c)")
    parser.add_argument("--sft_triples_path", type=str, default=None,
                        help="Single sft_triples.jsonl file (alternative to --data_dir)")
    parser.add_argument("--output_dir", type=str, default="data/plan-004-implicit",
                        help="Output directory for implicit_sft.jsonl")
    args = parser.parse_args()

    if args.data_dir:
        records = load_records_from_dir(args.data_dir)
        print(f"Loaded {len(records)} records from {args.data_dir}")
    elif args.sft_triples_path:
        records = load_records_from_file(args.sft_triples_path)
        print(f"Loaded {len(records)} records from {args.sft_triples_path}")
    else:
        parser.error("Must specify --data_dir or --sft_triples_path")

    output_path = os.path.join(args.output_dir, "implicit_sft.jsonl")
    summary = convert_all(records, output_path)

    summary_path = os.path.join(args.output_dir, "conversion_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary saved to {summary_path}")


if __name__ == "__main__":
    main()
