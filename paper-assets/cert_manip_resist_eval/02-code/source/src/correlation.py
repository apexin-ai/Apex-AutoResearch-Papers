# Correlation Measurement: pairwise agreement, mutual information, Gaussian copula, bootstrap CI.
# Validates cross-family MI < within-family MI.

from typing import Any, Callable, Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy import stats

from src.utils import setup_logging

logger = setup_logging("correlation")


def _extract_winners(scores: List[Dict[str, Any]]) -> np.ndarray:
    """Convert score dicts to integer labels: A=0, B=1, tie=2."""
    mapping = {"A": 0, "B": 1, "tie": 2}
    return np.array([mapping.get(s.get("winner", "tie"), 2) for s in scores])


def pairwise_agreement(scores_i: List[Dict], scores_j: List[Dict]) -> float:
    """Fraction of samples where two judges agree on winner."""
    wi = _extract_winners(scores_i)
    wj = _extract_winners(scores_j)
    assert len(wi) == len(wj), "Score lists must have same length"
    return float(np.mean(wi == wj))


def pairwise_mi(
    scores_i: List[Dict],
    scores_j: List[Dict],
    correction: str = "miller_madow",
) -> float:
    """Mutual information between two judges' winner decisions.
    Uses plug-in estimator with optional Miller-Madow bias correction."""
    wi = _extract_winners(scores_i)
    wj = _extract_winners(scores_j)
    n = len(wi)

    # Joint and marginal counts
    labels = [0, 1, 2]
    joint = np.zeros((3, 3))
    for a, b in zip(wi, wj):
        joint[a, b] += 1

    # Plug-in MI
    p_joint = joint / n
    p_i = p_joint.sum(axis=1)
    p_j = p_joint.sum(axis=0)

    mi = 0.0
    for a in labels:
        for b in labels:
            if p_joint[a, b] > 0 and p_i[a] > 0 and p_j[b] > 0:
                mi += p_joint[a, b] * np.log(p_joint[a, b] / (p_i[a] * p_j[b]))

    if correction == "miller_madow":
        # Count non-zero bins for bias correction
        m_joint = np.sum(p_joint > 0)
        m_i = np.sum(p_i > 0)
        m_j = np.sum(p_j > 0)
        bias = (m_joint - m_i - m_j + 1) / (2 * n)
        mi += bias

    return float(mi)


def gaussian_copula_rho(scores_i: List[Dict], scores_j: List[Dict]) -> float:
    """Gaussian copula correlation via rank transformation."""
    wi = _extract_winners(scores_i).astype(float)
    wj = _extract_winners(scores_j).astype(float)

    # Add tiny noise to break ties for ranking
    rng = np.random.RandomState(0)
    wi_jittered = wi + rng.normal(0, 1e-6, len(wi))
    wj_jittered = wj + rng.normal(0, 1e-6, len(wj))

    # Rank transform to uniform marginals
    n = len(wi)
    rank_i = stats.rankdata(wi_jittered) / (n + 1)
    rank_j = stats.rankdata(wj_jittered) / (n + 1)

    # Transform to normal
    z_i = stats.norm.ppf(rank_i)
    z_j = stats.norm.ppf(rank_j)

    # Pearson correlation in the normal space
    rho = np.corrcoef(z_i, z_j)[0, 1]
    return float(rho)


def bootstrap_ci(
    metric_fn: Callable,
    scores_i: List[Dict],
    scores_j: List[Dict],
    n_boot: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> Tuple[float, float]:
    """Bootstrap confidence interval for any pairwise metric."""
    rng = np.random.RandomState(seed)
    n = len(scores_i)
    boot_values = []

    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        si = [scores_i[i] for i in idx]
        sj = [scores_j[i] for i in idx]
        boot_values.append(metric_fn(si, sj))

    boot_values = np.array(boot_values)
    lower = float(np.percentile(boot_values, 100 * alpha / 2))
    upper = float(np.percentile(boot_values, 100 * (1 - alpha / 2)))
    return lower, upper


def compute_all_pairwise(
    all_scores: Dict[str, List[Dict]],
    n_boot: int = 1000,
) -> pd.DataFrame:
    """Compute agreement, MI, and copula rho for all judge pairs.
    Returns a DataFrame with columns: judge_i, judge_j, agreement, mi, copula_rho, plus CIs."""
    judge_ids = sorted(all_scores.keys())
    rows = []

    for i, ji in enumerate(judge_ids):
        for j, jj in enumerate(judge_ids):
            if j <= i:
                continue
            si = all_scores[ji]
            sj = all_scores[jj]

            agr = pairwise_agreement(si, sj)
            mi = pairwise_mi(si, sj)
            rho = gaussian_copula_rho(si, sj)

            agr_ci = bootstrap_ci(pairwise_agreement, si, sj, n_boot=n_boot)
            mi_ci = bootstrap_ci(pairwise_mi, si, sj, n_boot=n_boot)
            rho_ci = bootstrap_ci(gaussian_copula_rho, si, sj, n_boot=n_boot)

            rows.append({
                "judge_i": ji,
                "judge_j": jj,
                "agreement": agr,
                "agreement_ci_lower": agr_ci[0],
                "agreement_ci_upper": agr_ci[1],
                "mi": mi,
                "mi_ci_lower": mi_ci[0],
                "mi_ci_upper": mi_ci[1],
                "copula_rho": rho,
                "copula_rho_ci_lower": rho_ci[0],
                "copula_rho_ci_upper": rho_ci[1],
            })

    df = pd.DataFrame(rows)
    logger.info(f"Computed pairwise metrics for {len(rows)} pairs")
    return df


def validate_cross_vs_within(
    df: pd.DataFrame,
    family_map: Dict[str, str],
) -> Dict[str, Any]:
    """Check that cross-family MI < within-family MI."""
    df = df.copy()
    df["family_i"] = df["judge_i"].map(family_map)
    df["family_j"] = df["judge_j"].map(family_map)
    df["same_family"] = df["family_i"] == df["family_j"]

    within = df[df["same_family"]]["mi"]
    cross = df[~df["same_family"]]["mi"]

    result = {
        "within_family_mi_mean": float(within.mean()) if len(within) > 0 else None,
        "cross_family_mi_mean": float(cross.mean()) if len(cross) > 0 else None,
        "hypothesis_holds": bool(
            len(within) > 0 and len(cross) > 0 and cross.mean() < within.mean()
        ),
        "mannwhitney_U": None,
        "mannwhitney_p": None,
        "permutation_p": None,
    }

    if len(within) >= 1 and len(cross) >= 1:
        # Mann-Whitney U: H1 = cross MI < within MI (one-sided)
        if len(within) >= 2 and len(cross) >= 2:
            u_stat, u_p = stats.mannwhitneyu(
                cross.values, within.values, alternative="less"
            )
            result["mannwhitney_U"] = float(u_stat)
            result["mannwhitney_p"] = float(u_p)

        # Permutation test (more robust for small N)
        all_vals = np.concatenate([cross.values, within.values])
        n_cross = len(cross)
        observed_diff = cross.mean() - within.mean()
        rng = np.random.RandomState(42)
        n_perm = 10000
        count_le = 0
        for _ in range(n_perm):
            rng.shuffle(all_vals)
            perm_diff = all_vals[:n_cross].mean() - all_vals[n_cross:].mean()
            if perm_diff <= observed_diff:
                count_le += 1
        result["permutation_p"] = count_le / n_perm

    logger.info(
        f"Within-family MI: {result['within_family_mi_mean']:.4f}, "
        f"Cross-family MI: {result['cross_family_mi_mean']:.4f}, "
        f"Hypothesis holds: {result['hypothesis_holds']}, "
        f"Mann-Whitney p: {result['mannwhitney_p']}, "
        f"Permutation p: {result['permutation_p']}"
    )
    return result
