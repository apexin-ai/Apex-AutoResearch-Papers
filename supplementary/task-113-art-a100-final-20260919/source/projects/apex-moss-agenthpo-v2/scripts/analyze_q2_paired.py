"""Analyze the pre-registered paired-feedback interaction for Q2."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEED = 20260727
BOOTSTRAP_SAMPLES = 10_000

CONDITIONS = {
    "tdd": {
        ("G", "V0"): "q2paired-v001-tdd-v0",
        ("S", "V0"): "q2paired-v005-tdd-v0",
        ("G", "V1"): "hidden-v001-tddgen_hidden-val",
        ("S", "V1"): "hidden-v005-tddgen_hidden-val",
    },
    "spec": {
        ("G", "V0"): "hidden-v001-specgen_hidden-val",
        ("S", "V0"): "hidden-v005-specgen_hidden-val",
        ("G", "V1"): "q2paired-v001-spec-v1",
        ("S", "V1"): "q2paired-v005-spec-v1",
    },
}


def load_task_means(result_dir: Path) -> dict[str, float]:
    summary = json.loads((result_dir / "summary.json").read_text())
    if (
        summary.get("repeats") != 3
        or summary.get("tampered_runs", 0)
        or summary.get("contract_violations", 0)
        or summary.get("n_infra_invalid", 0)
    ):
        raise ValueError(f"invalid formal result: {result_dir}")
    grouped: dict[str, list[float]] = {}
    for path in result_dir.glob("*.rep*.json"):
        result = json.loads(path.read_text())
        grouped.setdefault(result["task"], []).append(float(result["passed"]))
    if not grouped or any(len(values) != 3 for values in grouped.values()):
        raise ValueError(f"incomplete three-repeat result: {result_dir}")
    return {
        task: sum(values) / len(values) for task, values in grouped.items()
    }


def task_interactions(
    block_results: dict[tuple[str, str], dict[str, float]]
) -> dict[str, float]:
    task_sets = [set(values) for values in block_results.values()]
    if not task_sets or any(tasks != task_sets[0] for tasks in task_sets[1:]):
        raise ValueError("paired conditions do not contain identical task ids")
    interactions = {}
    for task in sorted(task_sets[0]):
        gain_v1 = (
            block_results[("S", "V1")][task]
            - block_results[("G", "V1")][task]
        )
        gain_v0 = (
            block_results[("S", "V0")][task]
            - block_results[("G", "V0")][task]
        )
        interactions[task] = gain_v1 - gain_v0
    return interactions


def bootstrap_ci(
    blocks: dict[str, dict[str, float]],
    *,
    samples: int = BOOTSTRAP_SAMPLES,
    seed: int = SEED,
) -> tuple[float, float]:
    rng = random.Random(seed)
    values = {name: list(tasks.values()) for name, tasks in blocks.items()}
    estimates = []
    for _ in range(samples):
        block_means = []
        for block_values in values.values():
            drawn = [
                block_values[rng.randrange(len(block_values))]
                for _ in block_values
            ]
            block_means.append(sum(drawn) / len(drawn))
        estimates.append(sum(block_means) / len(block_means))
    estimates.sort()
    return (
        estimates[int(0.025 * (samples - 1))],
        estimates[int(0.975 * (samples - 1))],
    )


def analyze(root: Path = ROOT) -> dict:
    official = root / "results" / "official"
    blocks = {}
    condition_scores = {}
    for block, mapping in CONDITIONS.items():
        block_results = {
            condition: load_task_means(official / tag)
            for condition, tag in mapping.items()
        }
        blocks[block] = task_interactions(block_results)
        condition_scores[block] = {
            f"{harness}_{level}": sum(tasks.values()) / len(tasks)
            for (harness, level), tasks in block_results.items()
        }

    block_effects = {
        block: sum(tasks.values()) / len(tasks)
        for block, tasks in blocks.items()
    }
    interaction_all = sum(block_effects.values()) / len(block_effects)
    ci_low, ci_high = bootstrap_ci(blocks)
    if (
        interaction_all >= 0.10
        and ci_low > 0
        and all(effect >= 0 for effect in block_effects.values())
    ):
        decision = "confirmed_feedback_shape_specialization"
    elif interaction_all <= 0:
        decision = "direction_refuted"
    else:
        decision = "inconclusive"

    report = {
        "protocol": "q2-paired-feedback-confirmation",
        "seed": SEED,
        "bootstrap_samples": BOOTSTRAP_SAMPLES,
        "condition_scores": condition_scores,
        "block_interactions": block_effects,
        "interaction_all": interaction_all,
        "interaction_all_ci95": [ci_low, ci_high],
        "decision": decision,
        "task_interactions": blocks,
    }
    output = official / "q2-paired-analysis.json"
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(analyze(args.root), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
