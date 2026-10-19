#!/usr/bin/env python3
import json
import pathlib
import sys


def main() -> None:
    base = pathlib.Path(sys.argv[1])
    detail_filter = sys.argv[2] if len(sys.argv) > 2 else None
    first_decision = None

    runs = sorted(
        path for path in base.iterdir()
        if path.is_dir() and path.name.endswith("_final30")
    )
    if not runs:
        runs = [base]

    for run in runs:
        files = list(run.rglob("*_QwenLocal_results.json"))
        fallback_tasks = []
        invalid_json = 0
        total_decisions = 0
        total_fallbacks = 0

        for result_path in files:
            try:
                result = json.loads(result_path.read_text())
            except (OSError, json.JSONDecodeError):
                invalid_json += 1
                continue

            decisions = result.get("decisions") or []
            if first_decision is None and decisions:
                first_decision = (result_path, decisions[0])

            fallback_count = int(
                result.get(
                    "fallback_decision_count",
                    sum(
                        1
                        for decision in decisions
                        if isinstance(decision, dict)
                        and isinstance(decision.get("metadata"), dict)
                        and decision["metadata"].get("fallback") is True
                    ),
                )
                or 0
            )
            total_fallbacks += fallback_count
            total_decisions += int(
                result.get(
                    "agent_decisions_made",
                    result.get("decisions_made", len(decisions)),
                )
                or 0
            )
            if fallback_count:
                fallback_tasks.append(
                    (result.get("task_id", result_path.parent.name), fallback_count)
                )

            if detail_filter and detail_filter in str(result_path):
                print(f"DETAIL_FILE={result_path}")
                print(
                    f"DETAIL_FALLBACK_COUNT={fallback_count} "
                    f"DETAIL_AGENT_DECISIONS={result.get('agent_decisions_made')}"
                )
                for index, decision in enumerate(decisions, start=1):
                    metadata = decision.get("metadata") or {}
                    print(
                        json.dumps(
                            {
                                "index": index,
                                "reasoning": decision.get("reasoning"),
                                "new_config": decision.get("new_config"),
                                "metadata": metadata,
                            },
                            ensure_ascii=True,
                            indent=2,
                        )[:12000]
                    )

        print(
            f"{run.name}: files={len(files)} decisions={total_decisions} "
            f"fallbacks={total_fallbacks} fallback_tasks={len(fallback_tasks)} "
            f"invalid_json={invalid_json}"
        )
        if fallback_tasks:
            print(
                "  "
                + ", ".join(
                    f"{task_id}:{count}" for task_id, count in fallback_tasks
                )
            )

    if first_decision:
        path, decision = first_decision
        print(f"FIRST_DECISION_FILE={path}")
        print(f"FIRST_DECISION_KEYS={sorted(decision)}")
        print(json.dumps(decision, ensure_ascii=True, indent=2)[:8000])


if __name__ == "__main__":
    main()
