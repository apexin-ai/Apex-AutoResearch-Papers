"""Measure correction span by error type — P1 gate analysis.

For each classified failure, finds the matching expert trajectory and computes
how many expert action steps remain from the failure_step onward.
Groups by error_type and runs Kruskal-Wallis test.

Input:
  - classified_errors.jsonl (error_type, failure_step, game_file)
  - alfworld_sft.json (expert/ETO trajectories)

Output:
  - Per error_type statistics (mean/median/std of correction_span)
  - Kruskal-Wallis H-test p-value
  - Optional: per-trajectory JSONL results

Dependencies: numpy, scipy
"""

import argparse
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

logger = logging.getLogger("measure_correction")


def normalize_game_file(game_file: str) -> str:
    """Extract <task_dir>/<trial_dir> as matching key.

    Expert:     data/json_2.1.1/train/<task>/<trial>
    Trajectory: /root/.../json_2.1.1/train/<task>/<trial>/game.tw-pddl
    """
    gf = game_file.rstrip("/")
    if gf.endswith("/game.tw-pddl"):
        gf = gf[: -len("/game.tw-pddl")]
    parts = gf.split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else gf


def count_expert_action_steps(expert: dict) -> int:
    """Count gpt turns with 'Action:' in expert trajectory."""
    return sum(
        1
        for m in expert["conversations"]
        if m["from"] == "gpt" and "Action:" in m.get("value", "")
    )


def load_expert_index(path: str) -> dict:
    with open(path) as f:
        experts = json.load(f)
    index = {}
    for ex in experts:
        index[normalize_game_file(ex["game_file"])] = ex
    logger.info("Loaded %d experts, %d unique game_files", len(experts), len(index))
    return index


def load_classified(path: str) -> list:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    logger.info("Loaded %d classified trajectories", len(records))
    return records


def compute_correction_spans(classified: list, expert_index: dict) -> list:
    results = []
    matched = unmatched = 0

    for rec in classified:
        if rec.get("error_type") in ("unknown", None):
            continue

        key = normalize_game_file(rec.get("game_file", ""))
        expert = expert_index.get(key)
        if expert is None:
            unmatched += 1
            logger.debug("No expert for: %s", key)
            continue

        matched += 1
        expert_steps = count_expert_action_steps(expert)
        failure_step = max(1, rec.get("failure_step", 1))
        correction_span = max(1, expert_steps - failure_step + 1)

        results.append(
            {
                "task_id": rec.get("task_id"),
                "game_file": rec.get("game_file", ""),
                "error_type": rec["error_type"],
                "failure_step": failure_step,
                "expert_total_steps": expert_steps,
                "correction_span": correction_span,
                "llm_correction_horizon": rec.get("correction_horizon", -1),
                "rule_correction_horizon": rec.get("rule_correction_horizon", -1),
            }
        )

    logger.info("Matched %d, unmatched %d", matched, unmatched)
    return results


def run_analysis(results: list) -> dict:
    by_type = defaultdict(list)
    for r in results:
        by_type[r["error_type"]].append(r["correction_span"])

    per_type = {}
    for et in ("action", "verification", "planning"):
        spans = by_type.get(et, [])
        if spans:
            arr = np.array(spans, dtype=float)
            per_type[et] = {
                "count": len(spans),
                "mean": float(np.mean(arr)),
                "median": float(np.median(arr)),
                "std": float(np.std(arr)),
                "min": int(np.min(arr)),
                "max": int(np.max(arr)),
            }
        else:
            per_type[et] = {"count": 0}

    groups = [by_type[et] for et in ("action", "verification", "planning") if by_type.get(et)]
    kw = None
    if len(groups) >= 2 and all(len(g) >= 1 for g in groups):
        h, p = stats.kruskal(*groups)
        kw = {"H_statistic": float(h), "p_value": float(p)}

    return {"per_type": per_type, "kruskal_wallis": kw, "total": len(results)}


def print_report(analysis: dict):
    print("\n" + "=" * 60)
    print("CORRECTION SPAN ANALYSIS")
    print("=" * 60)
    print(f"\nTotal analyzed: {analysis['total']}")
    print(f"\n{'Type':<15} {'N':>5} {'Mean':>8} {'Median':>8} {'Std':>8} {'Min':>5} {'Max':>5}")
    print("-" * 60)

    for et in ("action", "verification", "planning"):
        s = analysis["per_type"].get(et, {})
        n = s.get("count", 0)
        if n > 0:
            print(
                f"{et:<15} {n:>5} {s['mean']:>8.2f} {s['median']:>8.1f} "
                f"{s['std']:>8.2f} {s['min']:>5} {s['max']:>5}"
            )
        else:
            print(f"{et:<15}     0        -        -        -     -     -")

    kw = analysis.get("kruskal_wallis")
    if kw:
        sig = (
            "***"
            if kw["p_value"] < 0.001
            else "**" if kw["p_value"] < 0.01 else "*" if kw["p_value"] < 0.05 else "ns"
        )
        print(f"\nKruskal-Wallis: H={kw['H_statistic']:.3f}, p={kw['p_value']:.4f} ({sig})")
        if kw["p_value"] < 0.05:
            print("-> Significant difference across error types (p < 0.05)")
        else:
            print("-> No significant difference (p >= 0.05)")
    else:
        print("\nKruskal-Wallis: insufficient groups (need >= 2 with data)")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Measure correction span by error type (P1 gate)"
    )
    parser.add_argument(
        "--classified",
        type=str,
        default="data/classified/classified_errors.jsonl",
        help="Classified errors JSONL",
    )
    parser.add_argument(
        "--expert",
        type=str,
        default="eto_repo/data/alfworld_sft.json",
        help="Expert trajectories JSON",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Save per-trajectory JSONL results",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s %(message)s")

    expert_index = load_expert_index(args.expert)
    classified = load_classified(args.classified)
    results = compute_correction_spans(classified, expert_index)

    if not results:
        logger.error("No matched trajectories. Check game_file normalization.")
        sys.exit(1)

    analysis = run_analysis(results)
    print_report(analysis)

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w") as f:
            f.write(json.dumps({"_summary": analysis}, ensure_ascii=False) + "\n")
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        logger.info("Saved %d results to %s", len(results), out)


if __name__ == "__main__":
    main()
