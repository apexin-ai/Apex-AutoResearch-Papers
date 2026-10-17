#!/usr/bin/env python3
"""DocRED Ridge Regression: analytic solution from correlation matrix.

For standardized data, ridge coefficients are:
    β_ridge = (R_xx + λI)^{-1} r_xy
GCV selects λ. Mathematically equivalent to RidgeCV on actual data.
"""
import json
import numpy as np
from pathlib import Path

n = 110

# Correlations (verified against partial_r = -0.3476 and R²_full = 0.5949)
r_bcs_acc = -0.7602
r_cent_acc = -0.7344  # negative (same direction as BCS; corr_BCS_cent = 0.99)
r_bcs_cent = 0.9901

R_xx = np.array([[1.0, r_bcs_cent],
                 [r_bcs_cent, 1.0]])
r_xy = np.array([r_bcs_acc, r_cent_acc])

# --- OLS ---
beta_ols = np.linalg.solve(R_xx, r_xy)
R2_ols = float(beta_ols @ r_xy)

# --- Ridge path + GCV ---
alphas = np.logspace(-4, 4, 500)
best_gcv, best_alpha, best_beta = np.inf, None, None
ridge_bcs_coefs = []

for alpha in alphas:
    A = R_xx + alpha * np.eye(2)
    beta = np.linalg.solve(A, r_xy)
    ridge_bcs_coefs.append(beta[0])

    rss = 1.0 - 2 * beta @ r_xy + beta @ R_xx @ beta
    df_eff = np.trace(R_xx @ np.linalg.inv(A))
    gcv = n * rss / (n - df_eff) ** 2

    if gcv < best_gcv:
        best_gcv, best_alpha, best_beta = gcv, alpha, beta.copy()

ridge_bcs_coefs = np.array(ridge_bcs_coefs)
R2_ridge = float(1.0 - (1.0 - 2 * best_beta @ r_xy + best_beta @ R_xx @ best_beta))

# --- Sign robustness proof ---
# β_BCS = [(1+λ)·r_{ba} - r_{bc}·r_{ca}] / [(1+λ)² - r_{bc}²]
# Numerator = (1+λ)·(-0.7602) - 0.9901·(-0.7344) = -(1+λ)·0.7602 + 0.7271
# At λ=0: -0.7602 + 0.7271 = -0.0331 < 0
# For λ>0: numerator = -0.0331 - λ·0.7602, strictly decreasing → always negative.
# Denominator > 0 for all λ ≥ 0 (since (1+λ)² ≥ 1 > r_bc²=0.98).
# Therefore β_BCS < 0 for ALL λ ≥ 0.

always_negative = bool(np.all(ridge_bcs_coefs < 0))

print(f"OLS (std): β_BCS={beta_ols[0]:.4f}, β_cent={beta_ols[1]:.4f}, R²={R2_ols:.4f}")
print(f"GCV λ = {best_alpha:.6f}")
print(f"Ridge (std): β_BCS={best_beta[0]:.4f}, β_cent={best_beta[1]:.4f}, R²={R2_ridge:.4f}")
print(f"BCS always negative: {always_negative}")
print(f"BCS coef range over λ∈[1e-4,1e4]: [{ridge_bcs_coefs.min():.4f}, {ridge_bcs_coefs.max():.4f}]")

# --- Also compute at several interpretable λ values ---
lambda_table = {}
for lam in [0.01, 0.1, 1.0, 10.0, 100.0]:
    b = np.linalg.solve(R_xx + lam * np.eye(2), r_xy)
    lambda_table[str(lam)] = {
        "bcs_coefficient": round(float(b[0]), 4),
        "centrality_coefficient": round(float(b[1]), 4),
    }

result = {
    "method": "Ridge regression (analytic from correlation matrix, GCV λ selection)",
    "data_source": "exp_docred_bcs_expanded: 110 DocRED batches (96-type pool, count_16+32)",
    "n_batches": n,
    "correlation_matrix": {
        "r_BCS_accuracy": r_bcs_acc,
        "r_centrality_accuracy": r_cent_acc,
        "r_BCS_centrality": r_bcs_cent,
        "VIF": round(1 / (1 - r_bcs_cent ** 2), 1),
    },
    "gcv_selected_alpha": round(float(best_alpha), 6),
    "r2_ridge": round(R2_ridge, 4),
    "standardized_coefficients": {
        "bcs_coefficient": round(float(best_beta[0]), 4),
        "centrality_coefficient": round(float(best_beta[1]), 4),
    },
    "ols_standardized_coefficients": {
        "bcs_coefficient": round(float(beta_ols[0]), 4),
        "centrality_coefficient": round(float(beta_ols[1]), 4),
        "r2": round(R2_ols, 4),
    },
    "ridge_path_at_selected_lambdas": lambda_table,
    "sign_robustness": {
        "bcs_negative_for_all_lambda": always_negative,
        "bcs_coef_range": [round(float(ridge_bcs_coefs.min()), 4), round(float(ridge_bcs_coefs.max()), 4)],
        "analytic_proof": (
            "β_BCS = [(1+λ)·r_{BCS,y} − r_{BCS,cent}·r_{cent,y}] / [(1+λ)² − r²_{BCS,cent}]. "
            "Numerator = −(1+λ)·0.7602 + 0.7271 = −0.0331 − λ·0.7602, "
            "monotonically decreasing in λ and negative at λ=0. "
            "Denominator > 0. Hence β_BCS < 0 for all λ ≥ 0."
        ),
    },
    "note": (
        "Analytic ridge from the 3-variable correlation matrix is equivalent to "
        "RidgeCV on standardized data for any given λ. GCV replaces k-fold CV. "
        "The extreme VIF (50.9) confirms high multicollinearity; ridge stabilizes "
        "the coefficients. The BCS coefficient is provably negative for all λ ≥ 0."
    ),
}

out_path = Path(__file__).parent / "docred_ridge_regression.json"
with open(out_path, "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print(f"\nSaved → {out_path}")
print(json.dumps(result, indent=2, ensure_ascii=False))
