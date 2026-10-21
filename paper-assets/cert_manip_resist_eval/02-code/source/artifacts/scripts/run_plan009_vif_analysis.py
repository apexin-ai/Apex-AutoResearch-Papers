"""Plan 009: VIF + Multicollinearity analysis for all 12 regression conditions."""

import json
import numpy as np
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
from statsmodels.stats.multitest import multipletests
from scipy.optimize import minimize

EPS = 0.001

STEP2V3_PATH = "/root/cert_manip_resist_eval/artifacts/results/results_step2v3_regression_20260522_031307.json"
TAXONOMY_PATH = "/root/cert_manip_resist_eval/artifacts/results/results_taxonomy_broadspectrum_20260522_044539.json"
OUTPUT_PATH = "/root/cert_manip_resist_eval/artifacts/results/results_plan009_vif_analysis.json"


def load_condition_data(panels, dataset, attack):
    """Extract (log_keff, log_eta_max, log_asr) arrays for a condition."""
    log_keff = []
    log_eta_max = []
    log_asr = []
    for p in panels:
        k = p["k_eff"][dataset]
        eta = p["eta_max_by_attack"][dataset][attack]
        asr = p["asr_by_attack"][dataset][attack]
        log_keff.append(np.log(k))
        log_eta_max.append(np.log(eta + EPS))
        log_asr.append(np.log(asr + EPS))
    return np.array(log_keff), np.array(log_eta_max), np.array(log_asr)


def compute_vif(log_keff, log_eta_max):
    """Compute VIF for log_keff and log_eta_max."""
    X = np.column_stack([log_keff, log_eta_max])
    X_with_const = add_constant(X)
    vif_keff = variance_inflation_factor(X_with_const, 1)
    vif_eta = variance_inflation_factor(X_with_const, 2)
    return vif_keff, vif_eta


def compute_partial_correlation(log_keff, log_eta_max, log_asr):
    """Partial correlation of K_eff with ASR, controlling for η_max."""
    # Residualize log_keff on log_eta_max
    X_eta = add_constant(log_eta_max)
    res_keff = OLS(log_keff, X_eta).fit().resid
    # Residualize log_asr on log_eta_max
    res_asr = OLS(log_asr, X_eta).fit().resid
    r, p = stats.pearsonr(res_keff, res_asr)
    return r, p


def compute_residualized_regression(log_keff, log_eta_max, log_asr):
    """Regress log_asr on residualized log_keff (after removing η_max effect)."""
    X_eta = add_constant(log_eta_max)
    resid_keff = OLS(log_keff, X_eta).fit().resid
    X_resid = add_constant(resid_keff)
    model = OLS(log_asr, X_resid).fit()
    beta = model.params[1]
    p = model.pvalues[1]
    return beta, p


def compute_ols(log_keff, log_eta_max, log_asr):
    """Standard OLS: log_asr ~ const + log_keff + log_eta_max."""
    X = add_constant(np.column_stack([log_keff, log_eta_max]))
    model = OLS(log_asr, X).fit()
    return {
        "keff_beta": model.params[1],
        "keff_p": model.pvalues[1],
        "eta_max_beta": model.params[2],
        "eta_max_p": model.pvalues[2],
        "r_squared": model.rsquared,
    }


def beta_log_likelihood(params, y, X):
    """Negative log-likelihood for beta regression. y in (0,1), X includes const."""
    beta_coefs = params[:-1]
    phi = np.exp(params[-1])  # precision parameter, ensure positive
    mu = 1.0 / (1.0 + np.exp(-X @ beta_coefs))  # logit link
    mu = np.clip(mu, 1e-10, 1 - 1e-10)
    a = mu * phi
    b = (1 - mu) * phi
    a = np.clip(a, 1e-10, None)
    b = np.clip(b, 1e-10, None)
    ll = np.sum(
        (a - 1) * np.log(y) + (b - 1) * np.log(1 - y)
        - (np.log(stats.beta.pdf(y, a, b) + 1e-300) - ((a - 1) * np.log(y) + (b - 1) * np.log(1 - y)))
    )
    # Direct beta log-likelihood
    ll = np.sum(stats.beta.logpdf(y, a, b))
    return -ll


def compute_beta_regression(log_keff, log_eta_max, raw_asr):
    """Beta regression: ASR ~ logit(K_eff, η_max). Returns coefs and approx p-values via Hessian."""
    y = np.clip(raw_asr, 1e-6, 1 - 1e-6)
    X = add_constant(np.column_stack([log_keff, log_eta_max]))
    n_beta = X.shape[1]

    # Initial values from OLS on logit(y)
    logit_y = np.log(y / (1 - y))
    ols_init = OLS(logit_y, X).fit()
    x0 = np.append(ols_init.params, np.log(5.0))  # init phi=5

    result = minimize(
        beta_log_likelihood, x0, args=(y, X),
        method="Nelder-Mead", options={"maxiter": 10000, "xatol": 1e-8, "fatol": 1e-8}
    )

    if not result.success:
        result = minimize(
            beta_log_likelihood, x0, args=(y, X),
            method="Powell", options={"maxiter": 10000}
        )

    coefs = result.x[:n_beta]

    # Numerical Hessian for standard errors
    eps_h = 1e-5
    n_params = len(result.x)
    hess = np.zeros((n_params, n_params))
    f0 = beta_log_likelihood(result.x, y, X)
    for i in range(n_params):
        for j in range(n_params):
            x_pp = result.x.copy()
            x_pp[i] += eps_h
            x_pp[j] += eps_h
            x_pm = result.x.copy()
            x_pm[i] += eps_h
            x_pm[j] -= eps_h
            x_mp = result.x.copy()
            x_mp[i] -= eps_h
            x_mp[j] += eps_h
            x_mm = result.x.copy()
            x_mm[i] -= eps_h
            x_mm[j] -= eps_h
            hess[i, j] = (
                beta_log_likelihood(x_pp, y, X)
                - beta_log_likelihood(x_pm, y, X)
                - beta_log_likelihood(x_mp, y, X)
                + beta_log_likelihood(x_mm, y, X)
            ) / (4 * eps_h * eps_h)

    try:
        cov = np.linalg.inv(hess)
        se = np.sqrt(np.abs(np.diag(cov)))
        z_keff = coefs[1] / se[1] if se[1] > 0 else 0
        z_eta = coefs[2] / se[2] if se[2] > 0 else 0
        p_keff = 2 * (1 - stats.norm.cdf(abs(z_keff)))
        p_eta = 2 * (1 - stats.norm.cdf(abs(z_eta)))
    except np.linalg.LinAlgError:
        p_keff = np.nan
        p_eta = np.nan

    return {
        "keff_coef": float(coefs[1]),
        "eta_max_coef": float(coefs[2]),
        "keff_p": float(p_keff),
        "eta_max_p": float(p_eta),
    }


def analyze_condition(panels, dataset, attack):
    """Full multicollinearity analysis for one condition."""
    log_keff, log_eta_max, log_asr = load_condition_data(panels, dataset, attack)

    # Raw ASR for beta regression
    raw_asr = np.array([p["asr_by_attack"][dataset][attack] for p in panels])

    # 1. VIF
    vif_keff, vif_eta = compute_vif(log_keff, log_eta_max)

    # 2. Partial correlation
    partial_r, partial_p = compute_partial_correlation(log_keff, log_eta_max, log_asr)

    # 3. Residualized K_eff
    resid_beta, resid_p = compute_residualized_regression(log_keff, log_eta_max, log_asr)

    # 4. Standard OLS
    ols = compute_ols(log_keff, log_eta_max, log_asr)

    # 5. Beta regression
    beta_reg = compute_beta_regression(log_keff, log_eta_max, raw_asr)

    return {
        "n_panels": len(panels),
        "vif_keff": round(float(vif_keff), 4),
        "vif_eta_max": round(float(vif_eta), 4),
        "partial_r_keff": round(float(partial_r), 4),
        "partial_r_keff_p": round(float(partial_p), 6),
        "residualized_keff_beta": round(float(resid_beta), 4),
        "residualized_keff_p": round(float(resid_p), 6),
        "ols_keff_beta": round(float(ols["keff_beta"]), 4),
        "ols_keff_p": round(float(ols["keff_p"]), 6),
        "ols_eta_max_beta": round(float(ols["eta_max_beta"]), 4),
        "ols_eta_max_p": round(float(ols["eta_max_p"]), 6),
        "ols_r_squared": round(float(ols["r_squared"]), 4),
        "beta_reg_keff_coef": round(float(beta_reg["keff_coef"]), 4),
        "beta_reg_keff_p": round(float(beta_reg["keff_p"]), 6),
        "beta_reg_eta_max_coef": round(float(beta_reg["eta_max_coef"]), 4),
        "beta_reg_eta_max_p": round(float(beta_reg["eta_max_p"]), 6),
    }


def main():
    with open(STEP2V3_PATH) as f:
        step2v3 = json.load(f)
    with open(TAXONOMY_PATH) as f:
        taxonomy = json.load(f)

    datasets = ["mmlu", "arc_challenge"]
    step2v3_attacks = ["prompt_injection", "sycophancy", "score_manipulation"]
    taxonomy_attacks = ["verbosity_bias", "position_bias", "authority_bias"]

    conditions = {}
    all_eta_max_p = []
    condition_names = []

    # Process Step2v3
    for ds in datasets:
        for atk in step2v3_attacks:
            name = f"{ds}×{atk}"
            print(f"Analyzing {name}...")
            result = analyze_condition(step2v3["all_20_panels"], ds, atk)
            conditions[name] = result
            all_eta_max_p.append(result["ols_eta_max_p"])
            condition_names.append(name)

    # Process Taxonomy
    for ds in datasets:
        for atk in taxonomy_attacks:
            name = f"{ds}×{atk}"
            print(f"Analyzing {name}...")
            result = analyze_condition(taxonomy["all_20_panels"], ds, atk)
            conditions[name] = result
            all_eta_max_p.append(result["ols_eta_max_p"])
            condition_names.append(name)

    # 4. Bonferroni and FDR corrections on eta_max p-values
    p_array = np.array(all_eta_max_p)

    # Bonferroni
    bonferroni_p = np.minimum(p_array * len(p_array), 1.0)

    # Benjamini-Hochberg FDR
    _, fdr_p, _, _ = multipletests(p_array, method="fdr_bh")

    for i, name in enumerate(condition_names):
        conditions[name]["eta_max_bonferroni_p"] = round(float(bonferroni_p[i]), 6)
        conditions[name]["eta_max_fdr_p"] = round(float(fdr_p[i]), 6)

    # Summary
    vif_keffs = [conditions[n]["vif_keff"] for n in condition_names]
    resid_sig = sum(1 for n in condition_names if conditions[n]["residualized_keff_p"] < 0.05)
    bonf_sig = sum(1 for n in condition_names if conditions[n]["eta_max_bonferroni_p"] < 0.05)
    fdr_sig = sum(1 for n in condition_names if conditions[n]["eta_max_fdr_p"] < 0.05)

    # Beta vs OLS concordance: same significance conclusion for both K_eff and η_max
    concordant = 0
    for n in condition_names:
        c = conditions[n]
        ols_keff_sig = c["ols_keff_p"] < 0.05
        beta_keff_sig = c["beta_reg_keff_p"] < 0.05
        ols_eta_sig = c["ols_eta_max_p"] < 0.05
        beta_eta_sig = c["beta_reg_eta_max_p"] < 0.05
        if ols_keff_sig == beta_keff_sig and ols_eta_sig == beta_eta_sig:
            concordant += 1

    summary = {
        "mean_vif_keff": round(float(np.mean(vif_keffs)), 4),
        "max_vif_keff": round(float(np.max(vif_keffs)), 4),
        "min_vif_keff": round(float(np.min(vif_keffs)), 4),
        "keff_residualized_sig_count": f"{resid_sig}/12",
        "eta_max_bonferroni_sig_count": f"{bonf_sig}/12",
        "eta_max_fdr_sig_count": f"{fdr_sig}/12",
        "beta_vs_ols_concordance": f"{concordant}/12",
    }

    output = {
        "conditions": conditions,
        "summary": summary,
        "metadata": {
            "epsilon": EPS,
            "alpha": 0.05,
            "n_conditions": 12,
            "step2v3_attacks": step2v3_attacks,
            "taxonomy_attacks": taxonomy_attacks,
            "datasets": datasets,
        },
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to {OUTPUT_PATH}")
    print(f"\n=== SUMMARY ===")
    print(f"Mean VIF(K_eff): {summary['mean_vif_keff']} (range: {summary['min_vif_keff']}-{summary['max_vif_keff']})")
    print(f"K_eff residualized significant: {summary['keff_residualized_sig_count']}")
    print(f"η_max Bonferroni significant: {summary['eta_max_bonferroni_sig_count']}")
    print(f"η_max FDR significant: {summary['eta_max_fdr_sig_count']}")
    print(f"Beta vs OLS concordance: {summary['beta_vs_ols_concordance']}")

    print(f"\n=== PER-CONDITION DETAILS ===")
    for name in condition_names:
        c = conditions[name]
        print(f"\n{name}:")
        print(f"  VIF: K_eff={c['vif_keff']}, η_max={c['vif_eta_max']}")
        print(f"  Partial r(K_eff|η_max): r={c['partial_r_keff']}, p={c['partial_r_keff_p']}")
        print(f"  Residualized K_eff: β={c['residualized_keff_beta']}, p={c['residualized_keff_p']}")
        print(f"  OLS: K_eff β={c['ols_keff_beta']} p={c['ols_keff_p']}, η_max β={c['ols_eta_max_beta']} p={c['ols_eta_max_p']}")
        print(f"  η_max corrected: Bonferroni p={c['eta_max_bonferroni_p']}, FDR p={c['eta_max_fdr_p']}")
        print(f"  Beta reg: K_eff coef={c['beta_reg_keff_coef']} p={c['beta_reg_keff_p']}, η_max coef={c['beta_reg_eta_max_coef']} p={c['beta_reg_eta_max_p']}")


if __name__ == "__main__":
    main()
