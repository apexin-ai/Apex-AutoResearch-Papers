"""
Numerical verification of Fisher Information for gamma in the 4PL+gamma IRT model.

Verifies three theoretical results:
  Theorem 1:   I(gamma) = sum w_ij * tau_ij^2    (conditional Fisher information)
  Corollary 1: E[I(gamma)] scales with AUC via bi-normal signal model
  Corollary 2: ME attenuation factor = sigma_tau^2 / (sigma_tau^2 + sigma_e^2)

Also compares analytic predictions with exp-004 empirical sweep results.

Input:  None (generates synthetic data internally)
Output: fisher_info_verification.json + printed comparison tables
"""

import json
import os
import sys
import numpy as np
from scipy.special import expit
from scipy.stats import norm

# ---------------------------------------------------------------------------
# Constants (matching simulation_sweep DGP)
# ---------------------------------------------------------------------------
N_ITEMS = 300
GAMMA_TRUE = 0.5
PI = 0.3  # contamination rate (BASE_EXPOSURE_RATE)
SEED = 42

AUC_VALUES = [0.55, 0.65, 0.80, 0.90, 0.95]
ME_SIGMA_VALUES = [0.0, 0.1, 0.3, 0.5, 1.0]
N_MODELS_DEFAULT = 50

N_REPS_SCORE = 10000    # MC reps for score variance
N_TAU_DRAWS = 100       # tau realizations for Corollary verification
N_ME_DRAWS = 200        # (tau, epsilon) draws for ME verification

PASS_LO, PASS_HI = 0.95, 1.05  # acceptance band for ratios

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SWEEP_RESULTS_DIR = os.path.join(
    os.path.dirname(SCRIPT_DIR), "simulation_sweep", "results"
)

# ---------------------------------------------------------------------------
# DGP helpers
# ---------------------------------------------------------------------------

def auc_to_sigma(target_auc):
    z = norm.ppf(target_auc)
    if z <= 0:
        return 1e6
    return 1.0 / (np.sqrt(2) * z)


def generate_item_params(rng, n_items):
    a = rng.lognormal(0, 0.5, n_items)
    b = rng.standard_normal(n_items)
    c = rng.beta(5, 20, n_items)
    d = rng.beta(20, 5, n_items)
    return a, b, c, d


def generate_exposure(rng, n_models, n_items, target_auc):
    gt = rng.binomial(1, PI, (n_models, n_items)).astype(float)
    sigma = auc_to_sigma(target_auc)
    noise = rng.standard_normal((n_models, n_items)) * sigma
    return gt + noise


def compute_model(theta, a, b, c, d, gamma, tau):
    eta = np.outer(np.ones(len(theta)), a) * (theta[:, None] - b[None, :]) + gamma * tau
    s = expit(eta)
    p = c[None, :] + (d[None, :] - c[None, :]) * s
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return eta, s, p


# ---------------------------------------------------------------------------
# Fisher Information computations
# ---------------------------------------------------------------------------

def fisher_analytic_4pl(tau, s, p, c, d):
    """I(gamma) = sum [(d-c)*s*(1-s)]^2 / [p*(1-p)] * tau^2"""
    dc = d[None, :] - c[None, :]
    w = (dc * s * (1 - s)) ** 2 / (p * (1 - p))
    return float(np.sum(w * tau ** 2))


def fisher_analytic_2pl(tau, p):
    """Under 2PL (c=0, d=1): I(gamma) = sum p*(1-p) * tau^2"""
    return float(np.sum(p * (1 - p) * tau ** 2))


def compute_weights_at_gamma0(theta, a, b, c, d):
    eta0 = np.outer(np.ones(len(theta)), a) * (theta[:, None] - b[None, :])
    s0 = expit(eta0)
    p0 = c[None, :] + (d[None, :] - c[None, :]) * s0
    p0 = np.clip(p0, 1e-12, 1 - 1e-12)
    dc = d[None, :] - c[None, :]
    w0 = (dc * s0 * (1 - s0)) ** 2 / (p0 * (1 - p0))
    return w0


def fisher_mc_score(tau, s, p, c, d, rng, n_reps=N_REPS_SCORE, batch_size=2000):
    """I(gamma) estimated via Var[score] over Monte Carlo y samples."""
    dc = d[None, :] - c[None, :]
    w_star = dc * s * (1 - s) / (p * (1 - p))
    tw = tau * w_star

    scores = []
    for start in range(0, n_reps, batch_size):
        bs = min(batch_size, n_reps - start)
        y = rng.binomial(1, np.broadcast_to(p, (bs,) + p.shape))
        sc = np.sum(tw[None, :, :] * (y - p[None, :, :]), axis=(1, 2))
        scores.append(sc)
    scores = np.concatenate(scores)
    return float(np.var(scores, ddof=0))


def fisher_expected_hessian(tau, theta, a, b, c, d, gamma):
    """I(gamma) via numerical 2nd derivative of E[log-lik]."""
    _, _, p_true = compute_model(theta, a, b, c, d, gamma, tau)
    h = 1e-5

    def E_ll(g):
        _, _, p = compute_model(theta, a, b, c, d, g, tau)
        return float(np.sum(p_true * np.log(p) + (1 - p_true) * np.log(1 - p)))

    return -(E_ll(gamma + h) - 2 * E_ll(gamma) + E_ll(gamma - h)) / h ** 2


# ---------------------------------------------------------------------------
# Verification routines
# ---------------------------------------------------------------------------

def verify_theorem1(n_models=N_MODELS_DEFAULT, auc=0.80):
    rng = np.random.default_rng(SEED)
    theta = rng.standard_normal(n_models)
    a, b, c, d = generate_item_params(rng, N_ITEMS)
    tau = generate_exposure(rng, n_models, N_ITEMS, auc)

    eta, s, p = compute_model(theta, a, b, c, d, GAMMA_TRUE, tau)

    I_analytic = fisher_analytic_4pl(tau, s, p, c, d)
    I_score = fisher_mc_score(tau, s, p, c, d, np.random.default_rng(SEED + 1))
    I_hessian = fisher_expected_hessian(tau, theta, a, b, c, d, GAMMA_TRUE)

    c0, d1 = np.zeros(N_ITEMS), np.ones(N_ITEMS)
    _, s2, p2 = compute_model(theta, a, b, c0, d1, GAMMA_TRUE, tau)
    I_2pl_simplified = fisher_analytic_2pl(tau, p2)
    I_2pl_general = fisher_analytic_4pl(tau, s2, p2, c0, d1)

    result = {
        "setting": f"AUC={auc}, N={n_models}, M={N_ITEMS}, gamma={GAMMA_TRUE}",
        "I_analytic_4pl": I_analytic,
        "I_mc_score": I_score,
        "I_expected_hessian": I_hessian,
        "ratio_score_over_analytic": I_score / I_analytic,
        "ratio_hessian_over_analytic": I_hessian / I_analytic,
        "I_2pl_simplified": I_2pl_simplified,
        "I_2pl_general_formula": I_2pl_general,
        "ratio_2pl_formulas": I_2pl_simplified / I_2pl_general,
    }
    return result


def verify_corollary1(n_models=N_MODELS_DEFAULT):
    rng = np.random.default_rng(SEED)
    theta = rng.standard_normal(n_models)
    a, b, c, d = generate_item_params(rng, N_ITEMS)

    w0 = compute_weights_at_gamma0(theta, a, b, c, d)
    W_total = float(np.sum(w0))
    W_bar = W_total / (n_models * N_ITEMS)

    results = []
    for auc in AUC_VALUES:
        sigma = auc_to_sigma(auc)
        E_tau_sq = sigma ** 2 + PI
        I_theory = W_total * E_tau_sq

        I_empirical_list = []
        for k in range(N_TAU_DRAWS):
            tau_k = generate_exposure(np.random.default_rng(SEED + 1000 + k),
                                     n_models, N_ITEMS, auc)
            I_empirical_list.append(float(np.sum(w0 * tau_k ** 2)))

        I_emp_mean = float(np.mean(I_empirical_list))
        I_emp_se = float(np.std(I_empirical_list) / np.sqrt(N_TAU_DRAWS))
        ratio = I_emp_mean / I_theory

        results.append({
            "auc": auc,
            "sigma_noise": sigma,
            "E_tau_sq": E_tau_sq,
            "Var_tau": sigma ** 2 + PI * (1 - PI),
            "I_theory": I_theory,
            "I_empirical_mean": I_emp_mean,
            "I_empirical_se": I_emp_se,
            "ratio": ratio,
        })

    return {"W_bar": W_bar, "W_total": W_total, "auc_sweep": results}


def verify_corollary2(n_models=N_MODELS_DEFAULT, auc=0.80):
    rng = np.random.default_rng(SEED)
    theta = rng.standard_normal(n_models)
    a, b, c, d = generate_item_params(rng, N_ITEMS)

    w0 = compute_weights_at_gamma0(theta, a, b, c, d)

    sigma_noise = auc_to_sigma(auc)
    sigma_tau_sq = sigma_noise ** 2 + PI * (1 - PI)

    results = []
    for sigma_e in ME_SIGMA_VALUES:
        sigma_e_sq = sigma_e ** 2
        attenuation_theory = sigma_tau_sq / (sigma_tau_sq + sigma_e_sq) if sigma_e > 0 else 1.0

        I_oracle_list, I_me_list = [], []
        for k in range(N_ME_DRAWS):
            rng_tau = np.random.default_rng(SEED + 2000 + k)
            tau_k = generate_exposure(rng_tau, n_models, N_ITEMS, auc)
            tau_c = tau_k - PI  # center

            I_oracle_list.append(float(np.sum(w0 * tau_c ** 2)))

            if sigma_e == 0:
                I_me_list.append(I_oracle_list[-1])
            else:
                rng_eps = np.random.default_rng(SEED + 3000 + k)
                eps = rng_eps.standard_normal(tau_k.shape) * sigma_e
                tau_obs = tau_c + eps
                lam = sigma_tau_sq / (sigma_tau_sq + sigma_e_sq)
                tau_post = lam * tau_obs
                I_me_list.append(float(np.sum(w0 * tau_post ** 2)))

        I_oracle_mean = float(np.mean(I_oracle_list))
        I_me_mean = float(np.mean(I_me_list))
        ratio_emp = I_me_mean / I_oracle_mean

        results.append({
            "sigma_e": sigma_e,
            "attenuation_theory": attenuation_theory,
            "ratio_empirical": ratio_emp,
            "I_oracle_mean": I_oracle_mean,
            "I_me_mean": I_me_mean,
        })

    return {"sigma_tau_sq": sigma_tau_sq, "auc": auc, "me_sweep": results}


def _load_all_exp004_conditions():
    """Load conditions from individual result files + sweep summary."""
    conditions = []
    if not os.path.isdir(SWEEP_RESULTS_DIR):
        return conditions

    for fname in sorted(os.listdir(SWEEP_RESULTS_DIR)):
        if fname == "sweep_summary.json" or not fname.endswith(".json"):
            continue
        fpath = os.path.join(SWEEP_RESULTS_DIR, fname)
        with open(fpath) as f:
            data = json.load(f)
        cfg = data.get("config", {})
        runs = data.get("runs", [])
        ok_runs = [r for r in runs if r.get("success", False)]
        if not ok_runs:
            continue
        ci_widths = [r["ci95_width"] for r in ok_runs]
        gamma_sds = [r["gamma_sd"] for r in ok_runs]
        excludes_zero = [r.get("ci95_excludes_zero", False) for r in ok_runs]
        conditions.append({
            "condition_id": data.get("condition_id", fname.replace(".json", "")),
            "auc": cfg.get("auc", 0),
            "n_models": cfg.get("n_models", 0),
            "ci95_width_avg": float(np.mean(ci_widths)),
            "gamma_sd_avg": float(np.mean(gamma_sds)),
            "n_runs": len(ok_runs),
            "frac_excludes_zero": float(np.mean(excludes_zero)),
        })
    return conditions


def compare_exp004():
    conditions = _load_all_exp004_conditions()
    if not conditions:
        return None

    rng = np.random.default_rng(SEED)
    theta_pool = rng.standard_normal(200)
    a, b, c, d = generate_item_params(rng, N_ITEMS)

    comparisons = []
    for entry in conditions:
        auc = entry["auc"]
        n_models = entry["n_models"]
        ci_width_obs = entry["ci95_width_avg"]

        theta = theta_pool[:n_models]
        w0 = compute_weights_at_gamma0(theta, a, b, c, d)
        W_total = float(np.sum(w0))

        sigma = auc_to_sigma(auc)
        E_tau_sq = sigma ** 2 + PI
        I_cond = W_total * E_tau_sq

        sigma_post_cond = 1.0 / np.sqrt(I_cond + 1.0)
        ci_width_cond = 2 * 1.96 * sigma_post_cond

        comparisons.append({
            "condition": entry["condition_id"],
            "auc": auc,
            "n_models": n_models,
            "n_runs": entry["n_runs"],
            "I_conditional": I_cond,
            "sigma_post_conditional": sigma_post_cond,
            "ci_width_conditional": ci_width_cond,
            "ci_width_observed": ci_width_obs,
            "ratio_obs_over_cond": ci_width_obs / ci_width_cond if ci_width_cond > 0 else float("inf"),
            "frac_excludes_zero": entry["frac_excludes_zero"],
        })

    min_auc_for_detection_cond = 0.0
    for auc_test in np.arange(0.50, 1.00, 0.001):
        sigma_t = auc_to_sigma(auc_test)
        E_t2 = sigma_t ** 2 + PI
        theta_50 = theta_pool[:50]
        w_t = compute_weights_at_gamma0(theta_50, a, b, c, d)
        I_t = float(np.sum(w_t)) * E_t2
        needed = (1.96 / abs(GAMMA_TRUE)) ** 2
        if I_t + 1.0 > needed:
            min_auc_for_detection_cond = auc_test
            break

    return {
        "conditions": comparisons,
        "min_auc_conditional_prediction": min_auc_for_detection_cond,
        "note": (
            "The conditional Fisher information assumes all other parameters "
            "(theta, a, b, c, d) are known. The Bayesian posterior integrates "
            "over these, yielding wider CIs. The ratio_obs_over_cond column "
            "shows how much wider the observed CI is relative to the conditional "
            "lower bound."
        ),
    }


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def check_ratio(name, ratio):
    if PASS_LO <= ratio <= PASS_HI:
        return "PASS"
    else:
        return "WARNING"


def print_theorem1(res):
    print(f"\n  Setting: {res['setting']}")
    print(f"  {'Method':<25s} {'I(gamma)':>14s} {'Ratio':>10s} {'Status':>8s}")
    print(f"  {'-'*60}")
    print(f"  {'Analytic (4PL)':<25s} {res['I_analytic_4pl']:>14.2f} {'---':>10s} {'---':>8s}")

    r1 = res["ratio_score_over_analytic"]
    print(f"  {'MC score variance':<25s} {res['I_mc_score']:>14.2f} {r1:>10.4f} {check_ratio('score', r1):>8s}")

    r2 = res["ratio_hessian_over_analytic"]
    print(f"  {'Expected Hessian':<25s} {res['I_expected_hessian']:>14.2f} {r2:>10.4f} {check_ratio('hessian', r2):>8s}")

    r3 = res["ratio_2pl_formulas"]
    print(f"\n  2PL cross-check: simplified={res['I_2pl_simplified']:.2f}, "
          f"general={res['I_2pl_general_formula']:.2f}, ratio={r3:.6f}")


def print_corollary1(res):
    print(f"\n  W_bar = {res['W_bar']:.6f},  W_total = {res['W_total']:.2f}")
    print(f"\n  {'AUC':>6s} {'sigma':>8s} {'E[tau^2]':>10s} {'I_theory':>12s} "
          f"{'I_empirical':>12s} {'Ratio':>8s} {'Status':>8s}")
    print(f"  {'-'*70}")
    for r in res["auc_sweep"]:
        ratio = r["ratio"]
        status = check_ratio("auc", ratio)
        print(f"  {r['auc']:>6.2f} {r['sigma_noise']:>8.3f} {r['E_tau_sq']:>10.3f} "
              f"{r['I_theory']:>12.1f} {r['I_empirical_mean']:>12.1f} "
              f"{ratio:>8.4f} {status:>8s}")


def print_corollary2(res):
    print(f"\n  sigma_tau^2 = {res['sigma_tau_sq']:.4f} (AUC={res['auc']})")
    print(f"\n  {'sigma_e':>8s} {'Atten_theory':>14s} {'Ratio_emp':>12s} "
          f"{'I_oracle':>12s} {'I_ME':>12s} {'Status':>8s}")
    print(f"  {'-'*70}")
    for r in res["me_sweep"]:
        status = check_ratio("me", r["ratio_empirical"] / r["attenuation_theory"]) \
            if r["attenuation_theory"] > 0 else "PASS"
        print(f"  {r['sigma_e']:>8.2f} {r['attenuation_theory']:>14.4f} "
              f"{r['ratio_empirical']:>12.4f} "
              f"{r['I_oracle_mean']:>12.1f} {r['I_me_mean']:>12.1f} {status:>8s}")


def print_exp004(res):
    if res is None:
        print("\n  No exp-004 results found.")
        return
    print(f"\n  Conditional prediction: gamma detectable for all AUC >= "
          f"{res['min_auc_conditional_prediction']:.3f} (N=50, M=300)")
    print(f"\n  {'Condition':<30s} {'Runs':>5s} {'CI_obs':>8s} {'CI_cond':>8s} "
          f"{'Ratio':>8s} {'Excl0':>8s}")
    print(f"  {'-'*73}")
    for c in res["conditions"]:
        excl = f"{c['frac_excludes_zero']:.0%}"
        print(f"  {c['condition']:<30s} {c['n_runs']:>5d} {c['ci_width_observed']:>8.4f} "
              f"{c['ci_width_conditional']:>8.4f} "
              f"{c['ratio_obs_over_cond']:>8.1f} {excl:>8s}")
    print(f"\n  Note: {res['note']}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    all_results = {}
    all_pass = True

    print("=" * 65)
    print("  Theorem 1: Analytic vs Numerical Fisher Information")
    print("=" * 65)
    thm1 = verify_theorem1()
    all_results["theorem1"] = thm1
    print_theorem1(thm1)
    for key in ("ratio_score_over_analytic", "ratio_hessian_over_analytic"):
        if not (PASS_LO <= thm1[key] <= PASS_HI):
            all_pass = False

    print("\n" + "=" * 65)
    print("  Corollary 1: AUC -- Information Relationship")
    print("=" * 65)
    cor1 = verify_corollary1()
    all_results["corollary1"] = cor1
    print_corollary1(cor1)
    for r in cor1["auc_sweep"]:
        if not (PASS_LO <= r["ratio"] <= PASS_HI):
            all_pass = False

    print("\n" + "=" * 65)
    print("  Corollary 2: Measurement Error Attenuation")
    print("=" * 65)
    cor2 = verify_corollary2()
    all_results["corollary2"] = cor2
    print_corollary2(cor2)
    for r in cor2["me_sweep"]:
        if r["attenuation_theory"] > 0:
            check = r["ratio_empirical"] / r["attenuation_theory"]
            if not (PASS_LO <= check <= PASS_HI):
                all_pass = False

    print("\n" + "=" * 65)
    print("  Comparison with exp-004 Empirical Results")
    print("=" * 65)
    exp4 = compare_exp004()
    all_results["exp004_comparison"] = exp4
    print_exp004(exp4)

    # Save JSON
    out_path = os.path.join(SCRIPT_DIR, "fisher_info_verification.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, default=float)
    print(f"\nResults saved to {out_path}")

    print("\n" + "=" * 65)
    if all_pass:
        print("  ALL VERIFICATIONS PASSED")
    else:
        print("  WARNING: Some verifications outside [0.95, 1.05] band")
    print("=" * 65)

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
