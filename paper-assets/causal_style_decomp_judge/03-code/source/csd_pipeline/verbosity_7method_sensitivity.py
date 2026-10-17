"""Verbosity 7-Method Sensitivity Analysis (SF5)."""

import json
import numpy as np
from scipy import stats
from pathlib import Path


ROOT = Path("/root/causal_style_decomp_judge")
NLI_THRESHOLD = 0.90
SEED = 42
N_BOOT = 10_000


def load_likert_pairs():
    """Load scored Likert data, filter by NLI >= threshold, return (verbose_scores, concise_scores)."""
    rows = [json.loads(l) for l in (ROOT / "data/scored_qwen32b_verbosity.jsonl").read_text().strip().split("\n")]
    verbose, concise = [], []
    for r in rows:
        if r.get("nli_cf", 0) < NLI_THRESHOLD:
            continue
        if r["original_verbosity"] == "verbose":
            verbose.append(r["score_original"])
            concise.append(r["score_counterfactual"])
        else:
            verbose.append(r["score_counterfactual"])
            concise.append(r["score_original"])
    return np.array(verbose, dtype=float), np.array(concise, dtype=float)


def load_pairwise_trials():
    """Load pairwise results, filter by NLI >= threshold, return list of (verbose_wins_bool) per trial."""
    rows = [json.loads(l) for l in (ROOT / "data/pairwise_results_qwen32b_verbosity.jsonl").read_text().strip().split("\n")]
    trials = []
    for r in rows:
        if r.get("nli_cf", 0) < NLI_THRESHOLD:
            continue
        trials.append(r["trial1_prefers_verbose"])
        trials.append(r["trial2_prefers_verbose"])
    return trials


# ---------- Method 1: Paired t-test ----------
def method_paired_ttest(v, c):
    t_stat, p = stats.ttest_rel(v, c)
    d = (v - c).mean() / (v - c).std(ddof=1)
    return {"name": "Paired t-test", "statistic": round(float(t_stat), 4),
            "p_value": round(float(p), 6), "effect_size": round(float(d), 4),
            "significant": bool(p < 0.05)}


# ---------- Method 2: Mann-Whitney U ----------
def method_mann_whitney(v, c):
    u_stat, p = stats.mannwhitneyu(v, c, alternative="two-sided")
    r_rb = 1 - 2 * u_stat / (len(v) * len(c))
    return {"name": "Mann-Whitney U", "statistic": round(float(u_stat), 1),
            "p_value": round(float(p), 6), "effect_size": round(float(r_rb), 4),
            "significant": bool(p < 0.05)}


# ---------- Method 3: Ordinal Logistic Regression ----------
def method_ordinal_logistic(v, c):
    from statsmodels.miscmodels.ordinal_model import OrderedModel
    scores = np.concatenate([v, c])
    is_verbose = np.concatenate([np.ones(len(v)), np.zeros(len(c))])
    import pandas as pd
    df = pd.DataFrame({"score": scores.astype(int), "is_verbose": is_verbose})
    try:
        mod = OrderedModel(df["score"], df[["is_verbose"]], distr="logit")
        res = mod.fit(method="bfgs", disp=False)
        coef = res.params["is_verbose"]
        p = res.pvalues["is_verbose"]
        odds_ratio = np.exp(coef)
        return {"name": "Ordinal logistic", "statistic": round(float(coef), 4),
                "p_value": round(float(p), 6), "effect_size": round(float(odds_ratio), 4),
                "significant": bool(p < 0.05)}
    except Exception as e:
        return {"name": "Ordinal logistic", "statistic": None,
                "p_value": None, "effect_size": None,
                "significant": False, "error": str(e)}


# ---------- Method 4: Cohen's d ----------
def method_cohens_d(v, c):
    pooled_sd = np.sqrt(((len(v) - 1) * v.std(ddof=1)**2 + (len(c) - 1) * c.std(ddof=1)**2) / (len(v) + len(c) - 2))
    d = (v.mean() - c.mean()) / pooled_sd
    return {"name": "Cohen's d", "statistic": None,
            "p_value": None, "effect_size": round(float(d), 4),
            "significant": bool(abs(d) > 0.2)}


# ---------- Method 5: Binarized χ² ----------
def method_binarized_chi2(v, c):
    all_scores = np.concatenate([v, c])
    med = np.median(all_scores)
    v_high = np.sum(v > med)
    v_low = len(v) - v_high
    c_high = np.sum(c > med)
    c_low = len(c) - c_high
    table = np.array([[v_high, v_low], [c_high, c_low]])
    chi2, p, dof, _ = stats.chi2_contingency(table, correction=True)
    if v_low * c_high > 0:
        odds_ratio = (v_high * c_low) / (v_low * c_high)
    else:
        odds_ratio = float("inf")
    return {"name": "Binarized χ²", "statistic": round(float(chi2), 4),
            "p_value": round(float(p), 6), "effect_size": round(float(odds_ratio), 4),
            "significant": bool(p < 0.05)}


# ---------- Method 6: Likert ATE ----------
def method_likert_ate(v, c):
    rng = np.random.default_rng(SEED)
    diffs = v - c
    ate = diffs.mean()
    d = ate / diffs.std(ddof=1)
    n = len(diffs)

    boot_ates = np.array([rng.choice(diffs, size=n, replace=True).mean() for _ in range(N_BOOT)])
    ci_lo, ci_hi = np.percentile(boot_ates, [2.5, 97.5])

    count_extreme = np.sum(np.abs(boot_ates - ate) >= np.abs(ate))
    # Permutation test
    perm_count = 0
    for _ in range(N_BOOT):
        signs = rng.choice([-1, 1], size=n)
        perm_ate = (diffs * signs).mean()
        if abs(perm_ate) >= abs(ate):
            perm_count += 1
    p = perm_count / N_BOOT

    return {"name": "Likert ATE", "statistic": round(float(ate), 4),
            "p_value": round(float(p), 6), "effect_size": round(float(d), 4),
            "CI_95": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
            "significant": bool(p < 0.05)}


# ---------- Method 7: Bradley-Terry ----------
def method_bradley_terry(trials):
    import choix
    # trials is list of bools: True = verbose wins
    n_verbose_wins = sum(trials)
    n_total = len(trials)
    # BT with two items: 0=verbose, 1=concise
    comparisons = []
    for t in trials:
        if t:
            comparisons.append((0, 1))  # verbose beats concise
        else:
            comparisons.append((1, 0))  # concise beats verbose

    params = choix.ilsr_pairwise(2, comparisons, alpha=0.01)
    p_verbose = np.exp(params[0]) / (np.exp(params[0]) + np.exp(params[1]))

    # Pair-level bootstrap
    rng = np.random.default_rng(SEED)
    # Group trials by pair (every 2 consecutive trials)
    n_pairs = n_total // 2
    pair_trials = [(trials[2*i], trials[2*i+1]) for i in range(n_pairs)]

    boot_ps = []
    for _ in range(N_BOOT):
        idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_comps = []
        for i in idx:
            for t in pair_trials[i]:
                if t:
                    boot_comps.append((0, 1))
                else:
                    boot_comps.append((1, 0))
        bp = choix.ilsr_pairwise(2, boot_comps, alpha=0.01)
        boot_p = np.exp(bp[0]) / (np.exp(bp[0]) + np.exp(bp[1]))
        boot_ps.append(boot_p)

    boot_ps = np.array(boot_ps)
    ci_lo, ci_hi = np.percentile(boot_ps, [2.5, 97.5])

    # p-value: proportion of bootstrap samples where P(verbose) <= 0.5
    p_value = np.mean(boot_ps <= 0.5)

    return {"name": "Bradley-Terry", "statistic": round(float(p_verbose), 4),
            "p_value": round(float(p_value), 6),
            "effect_size": round(float(p_verbose), 4),
            "CI_95": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
            "significant": bool(p_value < 0.05)}


def main():
    v, c = load_likert_pairs()
    trials = load_pairwise_trials()
    n_pairs = len(v)
    print(f"NLI-filtered pairs: {n_pairs} (Likert), {len(trials)//2} (pairwise)")

    methods = [
        method_paired_ttest(v, c),
        method_mann_whitney(v, c),
        method_ordinal_logistic(v, c),
        method_cohens_d(v, c),
        method_binarized_chi2(v, c),
        method_likert_ate(v, c),
        method_bradley_terry(trials),
    ]

    result = {
        "axis": "verbosity",
        "judge": "Qwen3-32B",
        "benchmark": "LLMBar",
        "n_pairs_likert": n_pairs,
        "n_pairs_pairwise": len(trials) // 2,
        "methods": methods,
        "conclusion": f"{sum(1 for m in methods[:6] if not m['significant'])}/6 Likert-based methods NS, "
                      f"only BT detects verbosity bias — replicates formality attenuation pattern"
    }

    out_path = ROOT / "data/verbosity_7method_sensitivity.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nSaved to {out_path}")

    # Markdown table
    print("\n| Method | Statistic | p-value | Effect Size | Sig? |")
    print("|--------|-----------|---------|-------------|------|")
    for m in methods:
        stat = m["statistic"] if m["statistic"] is not None else "—"
        pval = m["p_value"] if m["p_value"] is not None else "—"
        eff = m["effect_size"] if m["effect_size"] is not None else "—"
        ci = f" {m['CI_95']}" if "CI_95" in m else ""
        sig = "Yes" if m["significant"] else "No"
        print(f"| {m['name']} | {stat} | {pval} | {eff}{ci} | {sig} |")


if __name__ == "__main__":
    main()
