# K_eff Formula Validation: compare MI-based empirical K_eff vs. analytical formula.
# Formula: K_eff = 1 + (K-1) * exp(-2 * I_max)  [worst-case, uses max pairwise MI]
# Empirical: K_eff from all pairwise copula rho   [uses full correlation structure]
# Supplementary: von Neumann entropy K* = 2^H(Σ)  [eigenspectrum-based diversity]

from typing import Any, Dict, List

import numpy as np
import pandas as pd

from src.utils import setup_logging

logger = setup_logging("keff")


def empirical_keff_from_rho(rho_matrix: np.ndarray) -> float:
    """MI-based empirical K_eff from pairwise copula rho matrix.
    K_eff = (1/K) Σ_i [1 + Σ_{j≠i} (1 - ρ_ij²)]
    Under Gaussian copula, 1-ρ² = exp(-2·MI), making this consistent
    with formula_keff. Difference: empirical uses all pairwise ρ,
    formula uses only I_max (worst-case pair)."""
    K = rho_matrix.shape[0]
    if K <= 1:
        return 1.0
    total = 0.0
    for i in range(K):
        k_eff_i = 1.0
        for j in range(K):
            if j != i:
                k_eff_i += 1.0 - rho_matrix[i, j] ** 2
        total += k_eff_i
    return float(total / K)


def von_neumann_kstar(rho_matrix: np.ndarray) -> float:
    """Effective diversity via von Neumann entropy: K* = 2^{H(Σ)}.
    H(Σ) = -Σ (λ_k / tr(Σ)) · log2(λ_k / tr(Σ)).
    Independent validation metric from eigenspectrum."""
    eigenvalues = np.linalg.eigvalsh(rho_matrix)
    eigenvalues = np.maximum(eigenvalues, 1e-12)
    trace = np.sum(eigenvalues)
    p = eigenvalues / trace
    entropy = -np.sum(p * np.log2(p))
    return float(2 ** entropy)


def formula_keff(K: int, I_max: float) -> float:
    """Analytical K_eff: 1 + (K-1) * exp(-2 * I_max).
    K: number of judges in panel.
    I_max: maximum pairwise mutual information among panel members."""
    return 1.0 + (K - 1) * np.exp(-2.0 * I_max)


def build_rho_matrix(
    pairwise_df: pd.DataFrame,
    judge_ids: List[str],
    metric: str = "copula_rho",
) -> np.ndarray:
    """Build K x K correlation matrix from pairwise DataFrame."""
    K = len(judge_ids)
    rho = np.eye(K)
    id_to_idx = {jid: i for i, jid in enumerate(judge_ids)}

    for _, row in pairwise_df.iterrows():
        ji, jj = row["judge_i"], row["judge_j"]
        if ji in id_to_idx and jj in id_to_idx:
            i, j = id_to_idx[ji], id_to_idx[jj]
            rho[i, j] = row[metric]
            rho[j, i] = row[metric]

    return rho


def get_max_pairwise_mi(
    pairwise_df: pd.DataFrame,
    judge_ids: List[str],
) -> float:
    """Get maximum pairwise MI among a set of judges."""
    mask = (
        pairwise_df["judge_i"].isin(judge_ids) & pairwise_df["judge_j"].isin(judge_ids)
    )
    subset = pairwise_df[mask]
    if len(subset) == 0:
        return 0.0
    return float(subset["mi"].max())


def validate_keff(
    pairwise_df: pd.DataFrame,
    panels: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Compare formula K_eff vs empirical effective rank for each panel.
    panels: list of dicts with 'judge_ids' key."""
    results = []

    for panel_info in panels:
        judge_ids = panel_info["judge_ids"]
        K = len(judge_ids)

        # Empirical K_eff: from all pairwise copula rho (MI-based, Option A)
        rho_mat = build_rho_matrix(pairwise_df, judge_ids, metric="copula_rho")
        k_eff_empirical = empirical_keff_from_rho(rho_mat)

        # Formula K_eff: from max pairwise MI (worst-case bound)
        I_max = get_max_pairwise_mi(pairwise_df, judge_ids)
        k_eff_formula = formula_keff(K, I_max)

        # Supplementary: von Neumann entropy K* (Option B)
        k_star = von_neumann_kstar(rho_mat)

        deviation = abs(k_eff_empirical - k_eff_formula)
        rel_deviation = deviation / max(k_eff_empirical, 1e-8)

        entry = {
            "judge_ids": judge_ids,
            "K": K,
            "I_max": I_max,
            "k_eff_empirical": k_eff_empirical,
            "k_eff_formula": k_eff_formula,
            "k_star_von_neumann": k_star,
            "deviation": deviation,
            "relative_deviation": rel_deviation,
            "panel_type": panel_info.get("panel_type", "unknown"),
        }
        results.append(entry)

        logger.info(
            f"Panel {judge_ids}: K_eff empirical={k_eff_empirical:.3f}, "
            f"formula={k_eff_formula:.3f}, K*={k_star:.3f}, deviation={deviation:.3f}"
        )

    return results
