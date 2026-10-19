"""
Numerical verification for Proposition (Mediation leakage boundedness).

The leakage coefficient is *implicitly* defined by the mediation bias equation

    plim tau_hat_direct(A*) = tau_direct + (1 - lambda(C)) * tau_indirect

i.e. lambda(C) := 1 - B(C) / tau_ind, where
    B(C)       = (Cov(g, f) - Cov(E[g|A*], E[f|A*])) / (sigma^2 + V_W)
    tau_ind    = Cov(g, f) / Var(T) = W / (sigma^2 + V),
    V          = Var(g(A)),
    V_B(C)     = Var(E[g|A*]),  V_W = V - V_B,
    W          = Cov(g, f) (population, under marginal pi),
    W_B(C)     = Cov(E[g|A*], E[f|A*]),  W_W = W - W_B.

Closed form:
    1 - lambda(C) = B(C) / tau_ind = W_W (sigma^2 + V) / [W (sigma^2 + V_W)].

We verify:
  (1) Proportional effects f = lambda0 * g:  lambda(C) in [0,1] for every C.
  (2) Non-proportional f (independent of g): lambda(C) can escape [0,1]; we
      report the empirical OOB rate (filtering trials with |tau_ind| < threshold
      since lambda = 1 - B/tau_ind is ill-conditioned near a zero indirect effect).
  (3) The diagnostic between-variance ratio lambda_V := V_B/V is always in [0,1]
      (law of total variance), independent of regime.
  (4) Endpoint identities: lambda(I) = 1 and lambda(rank-one C) = 0.

We additionally tag each non-proportional trial by the implied DGP sign
relationship (with tau_dir drawn independently): "sign-preserving" if
sign(tau_dir) = sign(tau_dir + tau_ind), else "sign-violating". This shows the
two are *not* equivalent in general: lambda(C) can fall outside [0,1] in either
regime, since lambda depends only on (pi, C, g, f, sigma^2), not on tau_dir.
"""

import json
from pathlib import Path

import numpy as np


RNG = np.random.default_rng(20260522)
N_TRIALS_PER_K = 10_000
KS = (3, 5, 7)
ATOL = 1e-9
SIGMA2_RANGE = (0.1, 2.0)
# Minimum |tau_ind| to avoid degenerate division (when f is near-orthogonal to g
# the indirect effect collapses and lambda = 1 - B/tau_ind is uninformative).
TAU_IND_MIN = 0.05


def sample_column_stochastic(K, rng):
    return rng.dirichlet(np.ones(K), size=K).T  # rows = a*, cols = a


def conditional_means(C, pi, vec):
    """Return (E[vec|A*=j] for each j, P(A*=j))."""
    joint = C * pi[None, :]                       # shape (K, K)
    p_astar = joint.sum(axis=1)                   # P(A*=j)
    safe = p_astar > 0
    cond = np.zeros_like(p_astar)
    cond[safe] = (joint[safe] @ vec) / p_astar[safe]
    return cond, p_astar


def compute_quantities(C, pi, g, f, sigma2):
    """Return dict with V, V_B, V_W, W, W_B, W_W, tau_ind, B, lambda, lambda_V."""
    mean_g = float(pi @ g)
    mean_f = float(pi @ f)
    g_c = g - mean_g
    f_c = f - mean_f

    V = float(np.sum(pi * g_c ** 2))
    W = float(np.sum(pi * g_c * f_c))

    Eg_astar, p_astar = conditional_means(C, pi, g)
    Ef_astar, _ = conditional_means(C, pi, f)

    Eg_c = Eg_astar - mean_g
    Ef_c = Ef_astar - mean_f
    V_B = float(np.sum(p_astar * Eg_c ** 2))
    W_B = float(np.sum(p_astar * Eg_c * Ef_c))

    V_W = V - V_B
    W_W = W - W_B

    var_T = sigma2 + V
    var_Ttilde = sigma2 + V_W

    tau_ind = W / var_T if var_T > 0 else np.nan
    B = W_W / var_Ttilde if var_Ttilde > 0 else np.nan
    if abs(tau_ind) < 1e-12:
        lam_implicit = np.nan
    else:
        lam_implicit = 1.0 - B / tau_ind

    lam_V = V_B / V if V > 0 else np.nan
    return {
        "V": V, "V_B": V_B, "V_W": V_W,
        "W": W, "W_B": W_B, "W_W": W_W,
        "tau_ind": tau_ind, "B": B,
        "lambda": lam_implicit, "lambda_V": lam_V,
    }


def summary(vals, name):
    arr = np.array([v for v in vals if v is not None and np.isfinite(v)])
    oob = int(((arr < -ATOL) | (arr > 1.0 + ATOL)).sum())
    return {
        "regime": name,
        "n_trials": int(arr.size),
        "n_out_of_bounds": oob,
        "oob_fraction": float(oob / max(arr.size, 1)),
        "min": float(arr.min()) if arr.size else None,
        "max": float(arr.max()) if arr.size else None,
        "mean": float(arr.mean()) if arr.size else None,
        "median": float(np.median(arr)) if arr.size else None,
        "p01": float(np.quantile(arr, 0.01)) if arr.size else None,
        "p99": float(np.quantile(arr, 0.99)) if arr.size else None,
    }


def run():
    results = {"per_K": {}, "regimes": {}}
    pooled = {
        "proportional": [],
        "nonprop_sign_preserving": [],
        "nonprop_sign_violating": [],
        "lambda_V_all": [],
    }

    for K in KS:
        prop_lams, sp_lams, sv_lams = [], [], []
        lamV_all = []

        for _ in range(N_TRIALS_PER_K):
            C = sample_column_stochastic(K, RNG)
            pi = RNG.dirichlet(np.ones(K))
            g = RNG.normal(size=K)
            sigma2 = float(RNG.uniform(*SIGMA2_RANGE))

            # (1) Proportional: f = lam0 * g
            lam0 = float(RNG.normal())
            while abs(lam0) < 1e-3:
                lam0 = float(RNG.normal())
            f_prop = lam0 * g
            q_prop = compute_quantities(C, pi, g, f_prop, sigma2)
            if np.isfinite(q_prop["lambda"]):
                prop_lams.append(q_prop["lambda"])
            lamV_all.append(q_prop["lambda_V"])

            # (2) Non-proportional: independent f. Filter |tau_ind| > threshold
            # so that lambda = 1 - B/tau_ind is not driven by a near-zero denominator.
            f_np = RNG.normal(size=K)
            q_np = compute_quantities(C, pi, g, f_np, sigma2)
            tau_ind = q_np["tau_ind"]
            if not (np.isfinite(q_np["lambda"]) and abs(tau_ind) >= TAU_IND_MIN):
                continue
            tau_dir = float(RNG.normal())
            tau_total = tau_dir + tau_ind
            if np.sign(tau_dir) == np.sign(tau_total):
                sp_lams.append(q_np["lambda"])
            else:
                sv_lams.append(q_np["lambda"])

        results["per_K"][K] = {
            "proportional":             summary(prop_lams, "proportional"),
            "nonprop_sign_preserving":  summary(sp_lams,   "nonprop_sign_preserving"),
            "nonprop_sign_violating":   summary(sv_lams,   "nonprop_sign_violating"),
            "lambda_V":                 summary(lamV_all,  "lambda_V"),
        }
        pooled["proportional"].extend(prop_lams)
        pooled["nonprop_sign_preserving"].extend(sp_lams)
        pooled["nonprop_sign_violating"].extend(sv_lams)
        pooled["lambda_V_all"].extend(lamV_all)

    results["regimes"]["proportional"]            = summary(pooled["proportional"],
                                                            "proportional (pooled)")
    results["regimes"]["nonprop_sign_preserving"] = summary(pooled["nonprop_sign_preserving"],
                                                            "nonprop_sign_preserving (pooled)")
    results["regimes"]["nonprop_sign_violating"]  = summary(pooled["nonprop_sign_violating"],
                                                            "nonprop_sign_violating (pooled)")
    results["regimes"]["lambda_V"]                = summary(pooled["lambda_V_all"],
                                                            "lambda_V (pooled)")

    # Analytic endpoint checks at K=3
    K_ref = 3
    pi_ref = np.array([0.4, 0.35, 0.25])
    g_ref = np.array([-0.7, 0.2, 1.1])
    f_ref = 1.3 * g_ref
    sigma2_ref = 0.5
    q_I = compute_quantities(np.eye(K_ref), pi_ref, g_ref, f_ref, sigma2_ref)
    q_U = compute_quantities(np.full((K_ref, K_ref), 1.0 / K_ref),
                             pi_ref, g_ref, f_ref, sigma2_ref)
    results["endpoint_check_K3"] = {
        "lambda_at_identity":  q_I["lambda"],
        "lambda_at_uniform_C": q_U["lambda"],
        "lambda_V_at_identity":  q_I["lambda_V"],
        "lambda_V_at_uniform_C": q_U["lambda_V"],
    }

    out_path = Path(__file__).with_name("verify_lambda_bound_results.json")
    out_path.write_text(json.dumps(results, indent=2))

    # Console summary
    print("=" * 78)
    print("Implicit lambda(C) := 1 - B(C)/tau_ind")
    print("=" * 78)
    for regime in ("proportional", "nonprop_sign_preserving", "nonprop_sign_violating"):
        s = results["regimes"][regime]
        print(f"[{regime:30s}]  n={s['n_trials']:6d}  "
              f"range=[{s['min']:.4g}, {s['max']:.4g}]  "
              f"OOB={s['n_out_of_bounds']:6d} ({100*s['oob_fraction']:.2f}%)  "
              f"median={s['median']:.4f}")
    s = results["regimes"]["lambda_V"]
    print(f"[{'lambda_V = V_B/V (diagnostic)':30s}]  n={s['n_trials']:6d}  "
          f"range=[{s['min']:.4g}, {s['max']:.4g}]  "
          f"OOB={s['n_out_of_bounds']:6d}")
    print()
    ec = results["endpoint_check_K3"]
    print(f"Endpoint (K=3): lambda(I) = {ec['lambda_at_identity']:.12f} (expect 1.0)")
    print(f"Endpoint (K=3): lambda(uniform C) = {ec['lambda_at_uniform_C']:.12e} (expect 0.0)")
    print()
    print(f"Results written to {out_path}")

    # Sanity assertions (proportional should be exact; others are empirical)
    prop_s = results["regimes"]["proportional"]
    assert prop_s["n_out_of_bounds"] == 0, (
        f"Proportional case violated bound: {prop_s['n_out_of_bounds']} of "
        f"{prop_s['n_trials']} trials outside [0,1]"
    )
    lamV_s = results["regimes"]["lambda_V"]
    assert lamV_s["n_out_of_bounds"] == 0, (
        f"lambda_V violated bound: {lamV_s['n_out_of_bounds']} of "
        f"{lamV_s['n_trials']} trials outside [0,1]"
    )
    assert abs(ec["lambda_at_identity"] - 1.0) < 1e-9
    assert abs(ec["lambda_at_uniform_C"]) < 1e-9


if __name__ == "__main__":
    run()
