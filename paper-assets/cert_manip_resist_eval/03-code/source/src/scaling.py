# Scaling Analysis: K_eff vs ASR across panel sizes, Spearman rho, log-log regression.
# Core claim: higher K_eff -> lower ASR, with predictable scaling.

from typing import Any, Dict, List, Tuple

import numpy as np
from scipy import stats

from src.utils import setup_logging

logger = setup_logging("scaling")


def spearman_correlation(
    keff_values: List[float],
    asr_values: List[float],
) -> Tuple[float, float]:
    """Spearman rank correlation between K_eff and ASR.
    Expects negative correlation (higher K_eff -> lower ASR)."""
    rho, p_value = stats.spearmanr(keff_values, asr_values)
    logger.info(f"Spearman rho = {rho:.4f}, p = {p_value:.4e}")
    return float(rho), float(p_value)


def loglog_regression(
    keff_values: List[float],
    asr_values: List[float],
    n_bootstrap: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> Dict[str, float]:
    """Log-log regression: log(ASR) = beta * log(K_eff) + intercept.
    Returns slope (beta), intercept, R^2, and bootstrap CI for beta."""
    keff = np.array(keff_values)
    asr = np.array(asr_values)

    # Filter out zero/negative ASR for log transform
    valid = (asr > 0) & (keff > 0)
    if valid.sum() < 3:
        logger.warning("Too few valid points for log-log regression")
        return {"beta": float("nan"), "intercept": float("nan"), "r_squared": float("nan")}

    log_keff = np.log(keff[valid])
    log_asr = np.log(asr[valid])

    slope, intercept, r_value, p_value, std_err = stats.linregress(log_keff, log_asr)

    # Bootstrap CI for slope
    rng = np.random.RandomState(seed)
    n = len(log_keff)
    boot_slopes = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        s, _, _, _, _ = stats.linregress(log_keff[idx], log_asr[idx])
        boot_slopes.append(s)
    boot_slopes = np.array(boot_slopes)
    ci_lower = float(np.percentile(boot_slopes, 100 * alpha / 2))
    ci_upper = float(np.percentile(boot_slopes, 100 * (1 - alpha / 2)))

    result = {
        "beta": float(slope),
        "intercept": float(intercept),
        "r_squared": float(r_value ** 2),
        "p_value": float(p_value),
        "std_err": float(std_err),
        "beta_ci_lower": ci_lower,
        "beta_ci_upper": ci_upper,
    }
    logger.info(
        f"Log-log regression: beta={slope:.4f} [{ci_lower:.4f}, {ci_upper:.4f}], "
        f"R^2={r_value**2:.4f}, p={p_value:.4e}"
    )
    return result


def collect_scaling_data(
    panel_asr_results: Dict[str, List[Dict[str, Any]]],
    keff_results: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Merge panel ASR results with K_eff values for scaling analysis.
    Produces one row per (panel, attack, dataset) combination."""
    # Build K_eff lookup: tuple(sorted(judge_ids)) -> keff
    keff_lookup = {}
    for entry in keff_results:
        key = tuple(sorted(entry["judge_ids"]))
        keff_lookup[key] = entry

    data_points = []
    for ptype, panel_results in panel_asr_results.items():
        for pr in panel_results:
            key = tuple(sorted(pr["judge_ids"]))
            keff_entry = keff_lookup.get(key, {})

            data_points.append({
                "judge_ids": pr["judge_ids"],
                "panel_type": ptype,
                "k": pr["k"],
                "n_unique_families": pr.get("n_unique_families", 0),
                "asr": pr["asr"],
                "k_eff_empirical": keff_entry.get("k_eff_empirical"),
                "k_eff_formula": keff_entry.get("k_eff_formula"),
                "attack_name": pr.get("attack_name", "unknown"),
                "dataset": pr.get("dataset", "unknown"),
            })

    return data_points


def run_scaling_analysis(
    data_points: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Full scaling analysis on collected data points."""
    keff_values = [d["k_eff_empirical"] for d in data_points if d.get("k_eff_empirical")]
    asr_values = [d["asr"] for d in data_points if d.get("k_eff_empirical")]

    if len(keff_values) < 3:
        logger.warning("Insufficient data points for scaling analysis")
        return {"error": "insufficient_data", "n_points": len(keff_values)}

    rho, p_val = spearman_correlation(keff_values, asr_values)
    regression = loglog_regression(keff_values, asr_values)

    # Separate homo vs hetero
    homo_asr = [d["asr"] for d in data_points if d["panel_type"] == "homo"]
    hetero_asr = [d["asr"] for d in data_points if d["panel_type"] == "hetero"]

    result = {
        "n_data_points": len(keff_values),
        "spearman_rho": rho,
        "spearman_p": p_val,
        "loglog_regression": regression,
        "homo_asr_mean": float(np.mean(homo_asr)) if homo_asr else None,
        "hetero_asr_mean": float(np.mean(hetero_asr)) if hetero_asr else None,
        "asr_reduction": (
            float(1 - np.mean(hetero_asr) / np.mean(homo_asr))
            if homo_asr and hetero_asr and np.mean(homo_asr) > 0
            else None
        ),
    }
    logger.info(f"Scaling analysis: {len(keff_values)} points, rho={rho:.3f}")
    return result
