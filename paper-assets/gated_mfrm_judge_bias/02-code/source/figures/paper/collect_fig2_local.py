"""Collect per-model sequential bias data locally (no GPU needed).

Uses the mvp_002 DGP (N=50, I=100, J=8, rho=0.6) and a fast MLE-based
MFRM fit instead of MCMC, then applies the same sequential correction.
"""
import numpy as np
import pandas as pd
from scipy.special import expit
from scipy.optimize import minimize
from scipy import stats

N_SEEDS = 20
RHO = 0.6


def generate_mvp002_data(seed=42):
    rng = np.random.default_rng(seed)
    N, I, J = 50, 100, 8
    theta = rng.standard_normal(N)
    b = rng.standard_normal(I)
    d = rng.normal(0, 0.5, size=J)
    c = np.abs(rng.normal(0, 1.5, size=N))
    n_high = int(I * 0.3)
    e = np.zeros(I)
    idx = rng.permutation(I)
    e[idx[:n_high]] = rng.uniform(0.7, 1.0, size=n_high)
    e[idx[n_high:]] = rng.uniform(0.0, 0.2, size=I - n_high)
    d_std = d.std()
    if d_std < 1e-8:
        d_std = 1.0
    z_s = rng.standard_normal(J)
    s = 0.8 * (-RHO * (d / d_std) + np.sqrt(1 - RHO**2) * z_s)
    contamination = c[:, None, None] * e[None, :, None] * (1.0 + s[None, None, :])
    logits = theta[:, None, None] - b[None, :, None] - d[None, None, :] + contamination
    probs = expit(logits)
    responses = rng.binomial(1, probs).astype(np.float64)
    return {
        "responses": responses,
        "true_params": {"theta": theta, "b": b, "d": d, "c": c, "e": e, "s": s},
        "config": {"N": N, "I": I, "J": J, "rho": RHO, "seed": seed},
    }


def fit_mfrm_mle(Y, N, I, J):
    """Fast MLE fit of 3-facet Rasch model via L-BFGS-B."""
    n_params = N + I + J
    x0 = np.zeros(n_params)

    def neg_loglik(params):
        theta = params[:N]
        theta = theta - theta.mean()
        b = params[N:N+I]
        d = params[N+I:N+I+J]
        logits = theta[:, None, None] - b[None, :, None] - d[None, None, :]
        p = expit(logits)
        p = np.clip(p, 1e-10, 1 - 1e-10)
        ll = (Y * np.log(p) + (1 - Y) * np.log(1 - p)).sum()
        # L2 regularization (weak priors matching NumPyro priors)
        reg = 0.5 * (theta**2).sum() + 0.5 * (b**2).sum() + 2.0 * (d**2).sum()
        return -(ll - reg)

    def grad(params):
        theta = params[:N]
        theta = theta - theta.mean()
        b = params[N:N+I]
        d = params[N+I:N+I+J]
        logits = theta[:, None, None] - b[None, :, None] - d[None, None, :]
        p = expit(logits)
        residuals = Y - p  # (N, I, J)
        g_theta = residuals.sum(axis=(1, 2)) - theta
        g_theta = g_theta - g_theta.mean()
        g_b = -residuals.sum(axis=(0, 2)) - b
        g_d = -residuals.sum(axis=(0, 1)) - 4.0 * d
        return -np.concatenate([g_theta, g_b, g_d])

    res = minimize(neg_loglik, x0, jac=grad, method="L-BFGS-B",
                   options={"maxiter": 500, "ftol": 1e-8})
    theta_hat = res.x[:N]
    theta_hat = theta_hat - theta_hat.mean()
    b_hat = res.x[N:N+I]
    d_hat = res.x[N+I:N+I+J]
    return theta_hat, b_hat, d_hat


def fit_sequential_mle(data, e_values):
    """Sequential estimator: MFRM MLE + OLS residual correction."""
    cfg = data["config"]
    N, I, J = cfg["N"], cfg["I"], cfg["J"]
    Y = data["responses"]

    theta_mfrm, b_hat, d_hat = fit_mfrm_mle(Y, N, I, J)

    logits_hat = theta_mfrm[:, None, None] - b_hat[None, :, None] - d_hat[None, None, :]
    pred = expit(logits_hat)
    residuals = Y - pred
    r_ni = residuals.mean(axis=2)

    c_hat = np.zeros(N)
    e_centered = e_values - e_values.mean()
    e_var = (e_centered**2).sum()
    if e_var > 1e-10:
        for n in range(N):
            c_hat[n] = (r_ni[n] * e_centered).sum() / e_var

    mean_e = e_values.mean()
    theta_seq = theta_mfrm - c_hat * mean_e
    theta_seq = theta_seq - theta_seq.mean()
    return theta_seq


rows = []
for seed in range(N_SEEDS):
    print(f"  seed {seed}/{N_SEEDS}", end="", flush=True)
    data = generate_mvp002_data(seed=seed)
    theta_true = data["true_params"]["theta"]
    theta_true_centered = theta_true - theta_true.mean()
    c_true = data["true_params"]["c"]
    e_values = data["true_params"]["e"]

    theta_seq = fit_sequential_mle(data, e_values)
    bias = theta_seq - theta_true_centered

    N = len(theta_true)
    for n in range(N):
        rows.append({
            "seed": seed, "model_id": n,
            "c_true": float(c_true[n]),
            "theta_true": float(theta_true_centered[n]),
            "theta_seq": float(theta_seq[n]),
            "bias": float(bias[n]),
        })
    print(" done", flush=True)

df = pd.DataFrame(rows)
out = "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig2_permodel_data.csv"
df.to_csv(out, index=False)

r, p = stats.pearsonr(df["c_true"], df["bias"])
print(f"\nPearson r={r:.4f}, p={p:.2e} (N={len(df)} points)")
print(f"Saved to {out}")
