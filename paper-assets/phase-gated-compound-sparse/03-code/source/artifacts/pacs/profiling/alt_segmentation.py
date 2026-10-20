"""
Alternative Phase Segmentation: GMM + BIC and Quantile-based methods.

Developed as fallback when KDE tri-modal detection fails (e.g., unimodal
sparsity distributions where 82% of samples trigger KDE fallback).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

import numpy as np

try:
    from .phase_segmentation import Phase, PhaseAnnotation, PHASE_NAMES_BY_SPARSITY
except ImportError:
    # Fallback for environments without torch (phase_segmentation imports torch at top level).
    # Re-define the minimal dataclasses needed.
    from dataclasses import field as _field

    PHASE_NAMES_BY_SPARSITY = ["execution", "reasoning", "transition"]

    @dataclass
    class Phase:
        name: str
        start: int
        end: int
        mean_sparsity: float

        @property
        def token_indices(self) -> List[int]:
            return list(range(self.start, self.end))

    @dataclass
    class PhaseAnnotation:
        phases: List["Phase"]
        boundaries: List[int]
        sparsity: np.ndarray
        kde_x: np.ndarray
        kde_density: np.ndarray
        metadata: dict = _field(default_factory=dict)


# =====================================================================
# B1: GMM + BIC Diagnostics
# =====================================================================

@dataclass
class GMMDiagnostics:
    best_k: int
    bic_scores: dict
    means: np.ndarray
    stds: np.ndarray
    weights: np.ndarray
    assignments: np.ndarray
    posterior: np.ndarray


def fit_gmm_bic(
    sparsity_values: np.ndarray,
    max_k: int = 5,
    seed: int = 42,
) -> GMMDiagnostics:
    """Fit GMM with k=1..max_k, return BIC-optimal model."""
    from sklearn.mixture import GaussianMixture

    X = sparsity_values.reshape(-1, 1)
    best_bic = np.inf
    best_gmm = None
    bic_scores = {}

    for k in range(1, max_k + 1):
        gmm = GaussianMixture(n_components=k, random_state=seed, n_init=3)
        gmm.fit(X)
        bic = gmm.bic(X)
        bic_scores[k] = float(bic)
        if bic < best_bic:
            best_bic = bic
            best_gmm = gmm

    means = best_gmm.means_.flatten()
    sort_idx = np.argsort(means)
    means = means[sort_idx]
    stds = np.sqrt(best_gmm.covariances_.flatten())[sort_idx]
    weights = best_gmm.weights_[sort_idx]

    posteriors_raw = best_gmm.predict_proba(X)
    posteriors = posteriors_raw[:, sort_idx]
    assignments = np.argmax(posteriors, axis=1)

    return GMMDiagnostics(
        best_k=best_gmm.n_components,
        bic_scores=bic_scores,
        means=means,
        stds=stds,
        weights=weights,
        assignments=assignments,
        posterior=posteriors,
    )


# =====================================================================
# B2: Quantile-based Segmentation
# =====================================================================

@dataclass
class QuantileSegmentation:
    n_groups: int
    boundaries: np.ndarray
    assignments: np.ndarray
    group_stats: List[dict]
    group_names: List[str]


def segment_by_quantile(
    sparsity_values: np.ndarray,
    n_groups: int = 3,
    group_names: Optional[List[str]] = None,
) -> QuantileSegmentation:
    """Segment tokens into equal-sized groups by sparsity quantile."""
    if group_names is None:
        if n_groups == 3:
            group_names = ["low_sparsity", "mid_sparsity", "high_sparsity"]
        else:
            group_names = [f"group_{i}" for i in range(n_groups)]

    quantiles = np.linspace(0, 1, n_groups + 1)[1:-1]
    boundaries = np.quantile(sparsity_values, quantiles)

    assignments = np.digitize(sparsity_values, boundaries)

    group_stats = []
    for g in range(n_groups):
        mask = assignments == g
        vals = sparsity_values[mask]
        group_stats.append({
            "mean": float(np.mean(vals)) if len(vals) > 0 else 0.0,
            "std": float(np.std(vals)) if len(vals) > 0 else 0.0,
            "count": int(mask.sum()),
            "ratio": float(mask.sum() / len(sparsity_values)),
            "sparsity_range": (
                [float(vals.min()), float(vals.max())]
                if len(vals) > 0
                else [0.0, 0.0]
            ),
        })

    return QuantileSegmentation(
        n_groups=n_groups,
        boundaries=boundaries,
        assignments=assignments,
        group_stats=group_stats,
        group_names=group_names,
    )


# =====================================================================
# PhaseAnnotation Converter
# =====================================================================

def to_phase_annotation(
    assignments: np.ndarray,
    group_names: List[str],
    sparsity_values: np.ndarray,
    offset: int = 0,
    min_phase_length: int = 1,
) -> PhaseAnnotation:
    """Convert segment assignments to PhaseAnnotation format.

    Groups contiguous tokens with the same label into Phase objects,
    merging runs shorter than min_phase_length into the left neighbor.
    """
    seq_len = len(assignments)
    if seq_len == 0:
        return PhaseAnnotation(
            phases=[],
            boundaries=[],
            sparsity=sparsity_values,
            kde_x=np.array([]),
            kde_density=np.array([]),
            metadata={"method": "alt_segmentation"},
        )

    # Build contiguous Phase runs
    phases: list[Phase] = []
    run_start = 0
    for t in range(1, seq_len + 1):
        if t == seq_len or assignments[t] != assignments[run_start]:
            label = group_names[assignments[run_start]]
            phases.append(Phase(
                name=label,
                start=run_start + offset,
                end=t + offset,
                mean_sparsity=float(sparsity_values[run_start:t].mean()),
            ))
            if t < seq_len:
                run_start = t

    # Merge short phases into left neighbor
    if min_phase_length > 1 and len(phases) > 1:
        merged: list[Phase] = [phases[0]]
        for p in phases[1:]:
            if (p.end - p.start) < min_phase_length:
                prev = merged[-1]
                prev_len = prev.end - prev.start
                p_len = p.end - p.start
                merged[-1] = Phase(
                    name=prev.name,
                    start=prev.start,
                    end=p.end,
                    mean_sparsity=float(
                        (prev.mean_sparsity * prev_len + p.mean_sparsity * p_len)
                        / (prev_len + p_len)
                    ),
                )
            else:
                merged.append(p)
        phases = merged

    # Extract boundary positions (transitions between phases)
    boundaries = [p.start for p in phases[1:]]

    return PhaseAnnotation(
        phases=phases,
        boundaries=boundaries,
        sparsity=sparsity_values,
        kde_x=np.array([]),
        kde_density=np.array([]),
        metadata={"method": "alt_segmentation"},
    )


# =====================================================================
# Unified Interface
# =====================================================================

def segment_tokens(
    sparsity_values: np.ndarray,
    method: str = "kde",
    **kwargs,
) -> Tuple[np.ndarray, dict]:
    """Unified segmentation interface.

    Returns:
        assignments: (n_tokens,) int array, segment labels
        metadata: dict with method-specific diagnostics
    """
    if method == "gmm":
        diag = fit_gmm_bic(
            sparsity_values,
            max_k=kwargs.get("max_k", 5),
            seed=kwargs.get("seed", 42),
        )
        metadata = {
            "method": "gmm",
            "best_k": diag.best_k,
            "bic_scores": diag.bic_scores,
            "means": diag.means.tolist(),
            "stds": diag.stds.tolist(),
            "weights": diag.weights.tolist(),
        }
        return diag.assignments, metadata

    elif method == "quantile":
        n_groups = kwargs.get("n_groups", 3)
        group_names = kwargs.get("group_names", None)
        seg = segment_by_quantile(sparsity_values, n_groups=n_groups, group_names=group_names)
        metadata = {
            "method": "quantile",
            "n_groups": seg.n_groups,
            "boundaries": seg.boundaries.tolist(),
            "group_stats": seg.group_stats,
            "group_names": seg.group_names,
        }
        return seg.assignments, metadata

    elif method == "kde":
        from .phase_segmentation import PhaseSegmenter

        segmenter = PhaseSegmenter(**{
            k: v for k, v in kwargs.items()
            if k in ("bandwidth", "min_phase_length", "sparsity_threshold_ratio",
                      "kde_grid_points", "min_seq_length")
        })
        annotation = segmenter.segment_from_sparsity(sparsity_values)
        label_to_idx = {name: i for i, name in enumerate(PHASE_NAMES_BY_SPARSITY)}
        assignments = np.array([
            label_to_idx.get(p.name, 0)
            for p in annotation.phases
            for _ in range(p.start, p.end)
        ])
        metadata = {
            "method": "kde",
            "metadata": annotation.metadata,
        }
        return assignments, metadata

    else:
        raise ValueError(f"Unknown segmentation method: {method!r}. Use 'kde', 'gmm', or 'quantile'.")
