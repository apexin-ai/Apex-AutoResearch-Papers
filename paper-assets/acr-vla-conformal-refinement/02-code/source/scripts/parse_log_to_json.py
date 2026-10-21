#!/usr/bin/env python3
"""Parse evaluate.py log output into standard JSON format."""

import ast
import json
import re
import sys


def parse_log(log_path):
    with open(log_path) as f:
        text = f.read()

    # Extract args dict from "[evaluate] args: {...}"
    args_match = re.search(r"\[evaluate\] args: ({.*})", text)
    if args_match:
        args = ast.literal_eval(args_match.group(1))
    else:
        args = {}

    mode = args.get("mode", "unknown")
    baseline_mode = args.get("baseline_mode", "single")
    benchmark = args.get("benchmark", "unknown")
    n_rollouts = args.get("n_rollouts", 0)

    # Extract per-task results: "[task_name] success rate: X.X% (N/M)"
    per_task = {}
    for m in re.finditer(
        r"^\[([^\]]+)\] success rate: [\d.]+% \((\d+)/(\d+)\)",
        text,
        re.MULTILINE,
    ):
        task_name = m.group(1)
        successes = int(m.group(2))
        total = int(m.group(3))
        per_task[task_name] = {
            "success_rate": successes / total if total > 0 else 0.0,
            "successes": successes,
            "total": total,
        }

    # Compute overall
    total_successes = sum(t["successes"] for t in per_task.values())
    total_rollouts = sum(t["total"] for t in per_task.values())
    overall_rate = total_successes / total_rollouts if total_rollouts > 0 else 0.0

    return {
        "mode": mode,
        "baseline_mode": baseline_mode,
        "benchmark": benchmark,
        "n_rollouts": n_rollouts,
        "overall_success_rate": overall_rate,
        "per_task": per_task,
    }


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <log_file> <output_json>")
        sys.exit(1)

    result = parse_log(sys.argv[1])

    from pathlib import Path
    out = Path(sys.argv[2])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2))

    n_tasks = len(result["per_task"])
    print(f"Parsed {n_tasks} tasks, overall SR: {result['overall_success_rate']:.1%} "
          f"({sum(t['successes'] for t in result['per_task'].values())}/"
          f"{sum(t['total'] for t in result['per_task'].values())})")
    print(f"Saved to {sys.argv[2]}")


if __name__ == "__main__":
    main()
