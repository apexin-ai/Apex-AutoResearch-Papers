"""Analyze independent-lineage training reproducibility and external generalization."""

from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEED = 20260727
BOOTSTRAP_SAMPLES = 10_000
LINEAGE_NAMES = ("r00", "r01", "r02")


def load_summary(path: Path) -> dict:
    summary = json.loads(path.read_text())
    if (
        summary.get("repeats") != 3
        or summary.get("tampered_runs", 0)
        or summary.get("contract_violations", 0)
        or summary.get("n_infra_invalid", 0)
    ):
        raise ValueError(f"invalid formal summary: {path}")
    return summary


def load_task_means(result_dir: Path) -> dict[str, float]:
    load_summary(result_dir / "summary.json")
    grouped: dict[str, list[float]] = {}
    for path in result_dir.glob("*.rep*.json"):
        result = json.loads(path.read_text())
        grouped.setdefault(result["task"], []).append(float(result["passed"]))
    if not grouped or any(len(values) != 3 for values in grouped.values()):
        raise ValueError(f"incomplete formal task results: {result_dir}")
    return {
        task: sum(values) / len(values) for task, values in grouped.items()
    }


def bootstrap_external(
    generic: dict[str, float],
    lineages: dict[str, dict[str, float]],
    *,
    samples: int = BOOTSTRAP_SAMPLES,
    seed: int = SEED,
) -> tuple[float, float]:
    tasks = sorted(generic)
    if any(set(values) != set(tasks) for values in lineages.values()):
        raise ValueError("external task ids differ across Harnesses")
    rng = random.Random(seed)
    estimates = []
    for _ in range(samples):
        sampled = [tasks[rng.randrange(len(tasks))] for _ in tasks]
        lineage_gains = []
        for values in lineages.values():
            lineage_gains.append(
                sum(values[task] - generic[task] for task in sampled)
                / len(sampled)
            )
        estimates.append(sum(lineage_gains) / len(lineage_gains))
    estimates.sort()
    return (
        estimates[int(0.025 * (samples - 1))],
        estimates[int(0.975 * (samples - 1))],
    )


def analyze(root: Path = ROOT) -> dict:
    official = root / "results" / "official"
    train_generic = load_summary(
        official / "hidden-v001-tddgen_hidden-train" / "summary.json"
    )
    train_paths = {
        "r00": official / "hidden-v005-tddgen_hidden-train" / "summary.json",
        "r01": official / "q1confirm-r01-train" / "summary.json",
        "r02": official / "q1confirm-r02-train" / "summary.json",
    }
    train_summaries = {
        name: load_summary(path)
        for name, path in train_paths.items()
        if path.exists()
    }
    train_base = train_generic["pass_rate_mean"]
    train = {}
    qualified = []
    for name in LINEAGE_NAMES:
        if name not in train_summaries:
            continue
        summary = train_summaries[name]
        gain = summary["pass_rate_mean"] - train_base
        wave = max(
            train_generic.get("pass_rate_std", 0),
            summary.get("pass_rate_std", 0),
        )
        meets = gain >= 0.15 and gain > wave
        train[name] = {
            "score": summary["pass_rate_mean"],
            "gain": gain,
            "wave": wave,
            "qualified": meets,
        }
        if meets:
            qualified.append(name)

    external_generic_path = official / "q1confirm-v001-external"
    external_generic = (
        load_task_means(external_generic_path)
        if (external_generic_path / "summary.json").exists()
        else None
    )
    external_paths = {
        name: official / f"q1confirm-{name}-external"
        for name in LINEAGE_NAMES
    }
    external_lineages = {
        name: load_task_means(path)
        for name, path in external_paths.items()
        if (path / "summary.json").exists()
    }
    external = {}
    for name, values in external_lineages.items():
        if external_generic is None:
            continue
        gains = {
            task: values[task] - external_generic[task]
            for task in external_generic
        }
        external[name] = {
            "score": sum(values.values()) / len(values),
            "gain": sum(gains.values()) / len(gains),
            "task_gains": gains,
        }

    can_analyze_external = (
        len(qualified) >= 2
        and external_generic is not None
        and all(name in external_lineages for name in qualified)
    )
    all_train_observed = all(name in train_summaries for name in LINEAGE_NAMES)
    if len(qualified) < 2 and all_train_observed:
        decision = "evolution_not_reproducible"
        effect = None
        ci = None
    elif can_analyze_external:
        qualifying_results = {
            name: external_lineages[name] for name in qualified
        }
        gains = [external[name]["gain"] for name in qualified]
        effect = sum(gains) / len(gains)
        ci = bootstrap_external(external_generic, qualifying_results)
        if (
            effect >= 0.05
            and ci[0] > 0
            and all(gain > -0.05 for gain in gains)
        ):
            decision = "reproducible_generalization"
        elif (
            effect <= -0.05
            and ci[1] < 0
            and all(gain < 0.05 for gain in gains)
        ):
            decision = "reproducible_overfitting"
        else:
            decision = "inconclusive"
    else:
        decision = "matrix_incomplete"
        effect = None
        ci = None

    new_only = [
        name for name in ("r01", "r02")
        if name in qualified and name in external
    ]
    new_only_effect = (
        sum(external[name]["gain"] for name in new_only) / len(new_only)
        if new_only else None
    )
    expected_cells = [
        ("q1confirm-r02-train", train_paths["r02"]),
        ("q1confirm-v001-external", external_generic_path / "summary.json"),
        (
            "q1confirm-r00-external",
            external_paths["r00"] / "summary.json",
        ),
        (
            "q1confirm-r02-external",
            external_paths["r02"] / "summary.json",
        ),
        ("q1confirm-r01-train", train_paths["r01"]),
        (
            "q1confirm-r01-external",
            external_paths["r01"] / "summary.json",
        ),
    ]
    missing_cells = [name for name, path in expected_cells if not path.exists()]
    report = {
        "protocol": "q1-independent-lineage-confirmation",
        "seed": SEED,
        "bootstrap_samples": BOOTSTRAP_SAMPLES,
        "train_generic": train_base,
        "train": train,
        "qualified_lineages": qualified,
        "external_generic": (
            sum(external_generic.values()) / len(external_generic)
            if external_generic is not None
            else None
        ),
        "external": external,
        "external_effect_qualified": effect,
        "external_effect_ci95": ci,
        "new_lineages_only_effect": new_only_effect,
        "missing_cells": missing_cells,
        "decision_complete": decision != "matrix_incomplete",
        "decision": decision,
    }
    (official / "q1-confirmation-analysis.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    )
    return report


if __name__ == "__main__":
    print(json.dumps(analyze(), indent=2, ensure_ascii=False))
