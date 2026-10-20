"""Convert sft_triples.jsonl → implicit SFT format for Condition (b) training.

Input:  results/sft_data_death_aware/sft_triples.jsonl
  Each line: {task_type, observation, action, action_history, label, ...}
  label ∈ {"det-preferred", "int-preferred"}

Output: results/ablation_implicit/implicit_sft.jsonl
  Each line: chat-format record for causal LM SFT:
    messages: [
      {"role": "system", "content": IMPLICIT_SYSTEM_PROMPT},
      {"role": "user",   "content": "Observation: ... \n Action history: ..."},
      {"role": "assistant", "content": "[SIMULATE] action" | "action"}
    ]

Conversion logic:
  - label contains "det" → assistant = "[SIMULATE] {action}"
    Meaning: the model should signal that deterministic simulation is preferred,
    then the downstream pipeline forks the env and does lookahead.
  - label contains "int" → assistant = "{action}"
    Meaning: the model directly outputs the action (internal LLM reasoning).

The [SIMULATE] token is a learnable routing signal — it's part of the
generated text, not a special token in the vocabulary. At inference time,
the output is parsed for this prefix to decide the routing path.

Usage:
  python src/ablation_data_converter.py [--input_path ...] [--output_path ...]
"""

import argparse
import json
import os
from collections import Counter
from typing import List, Dict, Any

IMPLICIT_SYSTEM_PROMPT = (
    "You are an agent in a ScienceWorld text environment. "
    "Given the current observation and action history, choose the next action. "
    "If you believe a deterministic simulation would produce a better outcome, "
    "prefix your action with [SIMULATE]. Otherwise, output the action directly."
)

DEFAULT_INPUT = "results/sft_data_death_aware/sft_triples.jsonl"
DEFAULT_OUTPUT = "results/ablation_implicit/implicit_sft.jsonl"


def format_action_history(history: List[str], max_actions: int = 5) -> str:
    """Keep most recent N actions as a compact summary."""
    recent = history[-max_actions:] if history else []
    if not recent:
        return "(none)"
    return " -> ".join(recent)


def convert_triple_to_chat(triple: Dict[str, Any]) -> Dict[str, Any]:
    """Convert one sft_triple record to chat-format SFT record.

    Returns dict with 'messages' list and metadata fields for filtering/debugging.
    """
    obs = triple["observation"]
    action = triple["action"]
    history = triple.get("action_history", [])
    label = triple["label"]

    user_content = (
        f"Observation: {obs}\n"
        f"Action history: {format_action_history(history)}"
    )

    if "det" in label:
        assistant_content = f"[SIMULATE] {action}"
        route = "deterministic"
    else:
        assistant_content = action
        route = "internal"

    return {
        "messages": [
            {"role": "system", "content": IMPLICIT_SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content},
        ],
        "task_type": triple.get("task_type", ""),
        "variation": triple.get("variation", -1),
        "step_idx": triple.get("step_idx", -1),
        "route_label": route,
    }


def convert_file(input_path: str, output_path: str) -> Dict[str, Any]:
    """Read sft_triples.jsonl, convert all records, write implicit_sft.jsonl.

    Returns summary statistics.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    stats = Counter()
    records = []

    with open(input_path) as f:
        for line in f:
            triple = json.loads(line)
            chat_rec = convert_triple_to_chat(triple)
            records.append(chat_rec)
            stats[chat_rec["route_label"]] += 1
            stats["total"] += 1

    with open(output_path, "w") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    summary = {
        "input_path": input_path,
        "output_path": output_path,
        "total_records": stats["total"],
        "deterministic_count": stats["deterministic"],
        "internal_count": stats["internal"],
        "det_ratio": stats["deterministic"] / stats["total"] if stats["total"] > 0 else 0,
    }

    print(f"Converted {summary['total_records']} records")
    print(f"  deterministic: {summary['deterministic_count']} ({summary['det_ratio']:.1%})")
    print(f"  internal:      {summary['internal_count']}")
    print(f"  output: {output_path}")
    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Convert sft_triples.jsonl to implicit SFT chat format"
    )
    parser.add_argument("--input_path", type=str, default=DEFAULT_INPUT)
    parser.add_argument("--output_path", type=str, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    summary = convert_file(args.input_path, args.output_path)

    summary_path = os.path.join(
        os.path.dirname(args.output_path), "conversion_summary.json"
    )
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
