"""Compute inter-annotator agreement between two judges.

Metrics:
- Cohen's kappa for stage segmentation (4-class: localize/diagnose/patch/other)
- Cohen's kappa for quality assessment (binary: sound/flawed)
- Partially-good trajectory ratio
- Bootstrap 95% confidence intervals (1000 resamples)

Dependencies: scikit-learn, numpy.
"""

import json
from dataclasses import dataclass

import numpy as np
from sklearn.metrics import cohen_kappa_score


@dataclass
class AgreementReport:
    segmentation_kappa: float
    segmentation_kappa_ci: tuple[float, float]
    quality_kappa: float
    quality_kappa_ci: tuple[float, float]
    partially_good_ratio: float
    partially_good_ci: tuple[float, float]
    n_trajectories: int
    n_steps: int


def _bootstrap_kappa(
    labels_a: list, labels_b: list, n_bootstrap: int = 1000, seed: int = 42
) -> tuple[float, tuple[float, float]]:
    """Cohen's kappa with bootstrap 95% CI."""
    kappa = cohen_kappa_score(labels_a, labels_b)
    rng = np.random.RandomState(seed)
    n = len(labels_a)
    kappas = []
    for _ in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        a_sample = [labels_a[i] for i in idx]
        b_sample = [labels_b[i] for i in idx]
        if len(set(a_sample)) < 2 and len(set(b_sample)) < 2:
            kappas.append(1.0)
        else:
            try:
                kappas.append(cohen_kappa_score(a_sample, b_sample))
            except Exception:
                kappas.append(0.0)
    ci_low = float(np.percentile(kappas, 2.5))
    ci_high = float(np.percentile(kappas, 97.5))
    return kappa, (ci_low, ci_high)


def _bootstrap_ratio(
    values: list[bool], n_bootstrap: int = 1000, seed: int = 42
) -> tuple[float, tuple[float, float]]:
    """Bootstrap 95% CI for a binary proportion."""
    ratio = sum(values) / len(values) if values else 0.0
    rng = np.random.RandomState(seed)
    n = len(values)
    ratios = []
    for _ in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        sample = [values[i] for i in idx]
        ratios.append(sum(sample) / len(sample))
    ci_low = float(np.percentile(ratios, 2.5))
    ci_high = float(np.percentile(ratios, 97.5))
    return ratio, (ci_low, ci_high)


def is_partially_good(quality_labels: dict[str, str]) -> bool:
    """A trajectory is partially good if at least one early stage (localize/diagnose)
    is sound AND at least one later stage (diagnose/patch) is flawed."""
    has_early_sound = any(
        quality_labels.get(s) == "sound" for s in ["localize", "diagnose"]
    )
    has_late_flawed = any(
        quality_labels.get(s) == "flawed" for s in ["diagnose", "patch"]
    )
    return has_early_sound and has_late_flawed


def compute_agreement(
    segmentation_results: dict[str, dict],
    quality_results: dict[str, dict],
    judges: list[str],
    n_bootstrap: int = 1000,
) -> AgreementReport:
    """Compute agreement metrics between two judges.

    Args:
        segmentation_results: {instance_id: {judge: [{"step_index":..,"stage":..}]}}
        quality_results: {instance_id: {judge: {stage: {"assessment":..}}}}
        judges: Exactly 2 judge names.
        n_bootstrap: Bootstrap resamples for CI.
    """
    assert len(judges) == 2, f"Need exactly 2 judges, got {len(judges)}"
    j1, j2 = judges

    # Per-step segmentation labels
    seg_1, seg_2 = [], []
    for iid in segmentation_results:
        l1 = segmentation_results[iid].get(j1, [])
        l2 = segmentation_results[iid].get(j2, [])
        for i in range(min(len(l1), len(l2))):
            seg_1.append(l1[i]["stage"])
            seg_2.append(l2[i]["stage"])

    seg_kappa, seg_ci = _bootstrap_kappa(seg_1, seg_2, n_bootstrap)

    # Per-stage quality labels
    qual_1, qual_2 = [], []
    for iid in quality_results:
        for stage in ["localize", "diagnose", "patch"]:
            q1 = quality_results[iid].get(j1, {}).get(stage)
            q2 = quality_results[iid].get(j2, {}).get(stage)
            if q1 and q2:
                qual_1.append(q1["assessment"])
                qual_2.append(q2["assessment"])

    qual_kappa, qual_ci = _bootstrap_kappa(qual_1, qual_2, n_bootstrap)

    # Partially-good ratio (using first judge's assessments)
    pg_flags = []
    for iid in quality_results:
        q = quality_results[iid].get(j1, {})
        stage_assessments = {
            stage: q[stage]["assessment"]
            for stage in q
            if isinstance(q.get(stage), dict) and "assessment" in q[stage]
        }
        pg_flags.append(is_partially_good(stage_assessments))

    pg_ratio, pg_ci = _bootstrap_ratio(pg_flags, n_bootstrap)

    return AgreementReport(
        segmentation_kappa=seg_kappa,
        segmentation_kappa_ci=seg_ci,
        quality_kappa=qual_kappa,
        quality_kappa_ci=qual_ci,
        partially_good_ratio=pg_ratio,
        partially_good_ci=pg_ci,
        n_trajectories=len(segmentation_results),
        n_steps=len(seg_1),
    )


def format_report(report: AgreementReport) -> str:
    """Format agreement report for stdout."""
    return "\n".join([
        "=" * 60,
        "DiagPRM Annotation Agreement Report",
        "=" * 60,
        f"Trajectories: {report.n_trajectories}",
        f"Total steps:  {report.n_steps}",
        "",
        "--- Segmentation (4-class: localize/diagnose/patch/other) ---",
        f"Cohen's kappa:  {report.segmentation_kappa:.3f}"
        f"  95% CI [{report.segmentation_kappa_ci[0]:.3f}, {report.segmentation_kappa_ci[1]:.3f}]",
        "",
        "--- Quality Assessment (binary: sound/flawed) ---",
        f"Cohen's kappa:  {report.quality_kappa:.3f}"
        f"  95% CI [{report.quality_kappa_ci[0]:.3f}, {report.quality_kappa_ci[1]:.3f}]",
        "",
        "--- Partially-Good Trajectories ---",
        f"Ratio:          {report.partially_good_ratio:.3f}"
        f"  95% CI [{report.partially_good_ci[0]:.3f}, {report.partially_good_ci[1]:.3f}]",
        "=" * 60,
    ])


def save_report(report: AgreementReport, path: str) -> None:
    """Save agreement report as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump({
            "segmentation_kappa": report.segmentation_kappa,
            "segmentation_kappa_ci": list(report.segmentation_kappa_ci),
            "quality_kappa": report.quality_kappa,
            "quality_kappa_ci": list(report.quality_kappa_ci),
            "partially_good_ratio": report.partially_good_ratio,
            "partially_good_ci": list(report.partially_good_ci),
            "n_trajectories": report.n_trajectories,
            "n_steps": report.n_steps,
        }, f, indent=2)
