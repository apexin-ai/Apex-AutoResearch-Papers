"""Conditional Granger Causality Analysis: token_entropy vs ECE → diversity metrics."""
import json, os, sys, warnings
import numpy as np
import pandas as pd
from statsmodels.tsa.api import VAR
from itertools import product

warnings.filterwarnings("ignore")

BASE = "/root/autodl-tmp/distrib_canary_collapse/results"

EXPERIMENTS = {
    "a050_s42":   f"{BASE}/alpha_sweep/a050_s42/all_metrics.json",
    "a050_s43":   f"{BASE}/alpha_sweep/a050_s43/all_metrics.json",
    "a050_s44":   f"{BASE}/alpha_sweep/a050_s44/all_metrics.json",
    "a055_s42":   f"{BASE}/alpha_sweep/a055_s42_fp32/all_metrics.json",
    "a075_s42":   f"{BASE}/alpha_sweep/a075_s42/all_metrics.json",
    "a075_s43":   f"{BASE}/alpha_sweep/a075_s43/all_metrics.json",
    "a075_s44":   f"{BASE}/alpha_sweep/a075_s44/all_metrics.json",
    "pythia410m":  f"{BASE}/generalize/pythia410m_wiki_a100_s42/all_metrics.json",
    "opt1b":       f"{BASE}/generalize/opt1b_wiki_a100_s42/all_metrics.json",
    "pythia1b_c4": f"{BASE}/generalize/pythia1b_c4_a100_s42/all_metrics.json",
    "smollm3_3b":  f"{BASE}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/all_metrics.json",
}

CANARIES = ["token_entropy", "ece"]
DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]


def load_experiment(path):
    with open(path) as f:
        data = json.load(f)
    df = pd.DataFrame(data).sort_values("generation").reset_index(drop=True)
    return df


def conditional_granger(df, cause, effect, condition, maxlag=2):
    """
    Conditional Granger: does `cause` Granger-cause `effect` after controlling for `condition`?

    Compare:
    - Unrestricted: VAR on [effect, cause, condition]
    - Restricted:   VAR on [effect, condition] (cause excluded)

    Uses statsmodels VAR.test_causality which does an F-test.
    """
    cols_needed = [cause, effect, condition]
    if any(c not in df.columns for c in cols_needed):
        return None

    sub = df[cols_needed].dropna()
    T = len(sub)

    # Need enough observations for VAR estimation
    # VAR(p) needs T > p*k + k where k = number of variables
    results = {}
    for lag in range(1, maxlag + 1):
        k = 3  # unrestricted model variables
        min_obs = lag * k + k + 1
        if T < min_obs:
            results[lag] = {"p_value": np.nan, "F_stat": np.nan, "df": (np.nan, np.nan),
                           "note": f"T={T} too small for lag={lag}"}
            continue
        try:
            model = VAR(sub[[effect, cause, condition]])
            fitted = model.fit(lag)
            test = fitted.test_causality(caused=effect, causing=cause, kind='f')
            results[lag] = {
                "p_value": test.pvalue,
                "F_stat": test.test_statistic,
                "df": test.df,
            }
        except Exception as e:
            results[lag] = {"p_value": np.nan, "F_stat": np.nan, "note": str(e)[:80]}

    return results


def unconditional_granger(df, cause, effect, maxlag=2):
    """Unconditional (bivariate) Granger: cause → effect."""
    cols = [cause, effect]
    if any(c not in df.columns for c in cols):
        return None
    sub = df[cols].dropna()
    T = len(sub)
    results = {}
    for lag in range(1, maxlag + 1):
        k = 2
        min_obs = lag * k + k + 1
        if T < min_obs:
            results[lag] = {"p_value": np.nan, "F_stat": np.nan,
                           "note": f"T={T} too small for lag={lag}"}
            continue
        try:
            model = VAR(sub[[effect, cause]])
            fitted = model.fit(lag)
            test = fitted.test_causality(caused=effect, causing=cause, kind='f')
            results[lag] = {
                "p_value": test.pvalue,
                "F_stat": test.test_statistic,
                "df": test.df,
            }
        except Exception as e:
            results[lag] = {"p_value": np.nan, "F_stat": np.nan, "note": str(e)[:80]}
    return results


def joint_granger(df, causes, effect, maxlag=2):
    """Joint Granger: [token_entropy, ece] → effect simultaneously."""
    cols = causes + [effect]
    if any(c not in df.columns for c in cols):
        return None
    sub = df[cols].dropna()
    T = len(sub)
    results = {}
    for lag in range(1, maxlag + 1):
        k = len(cols)
        min_obs = lag * k + k + 1
        if T < min_obs:
            results[lag] = {"p_value": np.nan, "F_stat": np.nan,
                           "note": f"T={T} too small for lag={lag}"}
            continue
        try:
            model = VAR(sub[[effect] + causes])
            fitted = model.fit(lag)
            test = fitted.test_causality(caused=effect, causing=causes, kind='f')
            results[lag] = {
                "p_value": test.pvalue,
                "F_stat": test.test_statistic,
                "df": test.df,
            }
        except Exception as e:
            results[lag] = {"p_value": np.nan, "F_stat": np.nan, "note": str(e)[:80]}
    return results


# ─── Main analysis ───
all_results = {}

for exp_name, path in EXPERIMENTS.items():
    if not os.path.exists(path):
        print(f"SKIP {exp_name}: file not found")
        continue

    df = load_experiment(path)
    T = len(df)
    print(f"\n{'='*60}")
    print(f"Experiment: {exp_name}  (T={T})")
    print(f"{'='*60}")

    exp_results = {"T": T, "tests": {}}

    for downstream in DOWNSTREAMS:
        if downstream not in df.columns:
            print(f"  SKIP {downstream}: not in data")
            continue

        print(f"\n  Target: {downstream}")
        print(f"  {'─'*50}")

        pair_results = {}

        # 1. Unconditional: entropy → downstream
        ug_ent = unconditional_granger(df, "token_entropy", downstream)
        pair_results["uncond_entropy"] = ug_ent

        # 2. Unconditional: ECE → downstream
        ug_ece = unconditional_granger(df, "ece", downstream)
        pair_results["uncond_ece"] = ug_ece

        # 3. Conditional: entropy → downstream | ECE
        cg_ent = conditional_granger(df, "token_entropy", downstream, "ece")
        pair_results["cond_entropy_given_ece"] = cg_ent

        # 4. Conditional: ECE → downstream | entropy
        cg_ece = conditional_granger(df, "ece", downstream, "token_entropy")
        pair_results["cond_ece_given_entropy"] = cg_ece

        # 5. Joint: [entropy, ECE] → downstream
        jg = joint_granger(df, ["token_entropy", "ece"], downstream)
        pair_results["joint"] = jg

        # Print summary for lag=1
        lag = 1
        fmt = lambda r: f"F={r[lag]['F_stat']:.3f}, p={r[lag]['p_value']:.4f}" if r and lag in r and not np.isnan(r[lag].get('p_value', np.nan)) else "N/A"

        print(f"    Uncond entropy→{downstream}:        {fmt(ug_ent)}")
        print(f"    Uncond ECE→{downstream}:            {fmt(ug_ece)}")
        print(f"    Cond entropy→{downstream}|ECE:      {fmt(cg_ent)}")
        print(f"    Cond ECE→{downstream}|entropy:      {fmt(cg_ece)}")
        print(f"    Joint [entropy,ECE]→{downstream}:   {fmt(jg)}")

        exp_results["tests"][downstream] = pair_results

    all_results[exp_name] = exp_results


# ─── Summary table ───
print("\n\n" + "="*80)
print("SUMMARY TABLE: Conditional vs Unconditional Granger (lag=1, p-values)")
print("="*80)

header = f"{'Experiment':<16} {'Downstream':<12} {'Uncond TE':>10} {'Uncond ECE':>10} {'Cond TE|ECE':>12} {'Cond ECE|TE':>12} {'Joint':>10}"
print(header)
print("─" * len(header))

sig_counts = {"uncond_entropy": 0, "uncond_ece": 0,
              "cond_entropy_given_ece": 0, "cond_ece_given_entropy": 0, "joint": 0}
total_tests = 0

for exp_name, exp_data in all_results.items():
    for downstream, tests in exp_data["tests"].items():
        def get_p(test_key):
            r = tests.get(test_key)
            if r and 1 in r and not np.isnan(r[1].get("p_value", np.nan)):
                return r[1]["p_value"]
            return np.nan

        p_ue = get_p("uncond_entropy")
        p_uc = get_p("uncond_ece")
        p_ce = get_p("cond_entropy_given_ece")
        p_cc = get_p("cond_ece_given_entropy")
        p_j = get_p("joint")

        def fmt_p(p):
            if np.isnan(p): return "N/A"
            star = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "." if p < 0.1 else ""
            return f"{p:.4f}{star}"

        print(f"{exp_name:<16} {downstream:<12} {fmt_p(p_ue):>10} {fmt_p(p_uc):>10} {fmt_p(p_ce):>12} {fmt_p(p_cc):>12} {fmt_p(p_j):>10}")

        total_tests += 1
        if not np.isnan(p_ue) and p_ue < 0.05: sig_counts["uncond_entropy"] += 1
        if not np.isnan(p_uc) and p_uc < 0.05: sig_counts["uncond_ece"] += 1
        if not np.isnan(p_ce) and p_ce < 0.05: sig_counts["cond_entropy_given_ece"] += 1
        if not np.isnan(p_cc) and p_cc < 0.05: sig_counts["cond_ece_given_entropy"] += 1
        if not np.isnan(p_j) and p_j < 0.05: sig_counts["joint"] += 1


print(f"\n{'─'*80}")
print(f"Significance counts (p<0.05) out of {total_tests} tests:")
for k, v in sig_counts.items():
    print(f"  {k:<30}: {v}/{total_tests} ({100*v/total_tests:.1f}%)")


# ─── Redundancy analysis ───
print("\n\n" + "="*80)
print("REDUNDANCY ANALYSIS")
print("="*80)

# For each experiment × downstream, classify the pattern
patterns = {"both_independent": 0, "entropy_only": 0, "ece_only": 0,
            "redundant": 0, "neither": 0, "na": 0}

for exp_name, exp_data in all_results.items():
    for downstream, tests in exp_data["tests"].items():
        def get_p(test_key):
            r = tests.get(test_key)
            if r and 1 in r and not np.isnan(r[1].get("p_value", np.nan)):
                return r[1]["p_value"]
            return np.nan

        p_ue = get_p("uncond_entropy")
        p_uc = get_p("uncond_ece")
        p_ce = get_p("cond_entropy_given_ece")
        p_cc = get_p("cond_ece_given_entropy")

        if np.isnan(p_ce) or np.isnan(p_cc):
            patterns["na"] += 1
            continue

        ent_indep = p_ce < 0.05
        ece_indep = p_cc < 0.05

        if ent_indep and ece_indep:
            patterns["both_independent"] += 1
        elif ent_indep and not ece_indep:
            patterns["entropy_only"] += 1
        elif not ent_indep and ece_indep:
            patterns["ece_only"] += 1
        elif p_ue < 0.05 or p_uc < 0.05:
            patterns["redundant"] += 1
        else:
            patterns["neither"] += 1

print("Pattern classification (based on conditional p<0.05):")
for pattern, count in patterns.items():
    print(f"  {pattern:<20}: {count}")

# Softer threshold analysis (p<0.10)
print("\nSofter threshold (p<0.10):")
patterns10 = {"both_independent": 0, "entropy_only": 0, "ece_only": 0,
              "redundant": 0, "neither": 0, "na": 0}

for exp_name, exp_data in all_results.items():
    for downstream, tests in exp_data["tests"].items():
        def get_p(test_key):
            r = tests.get(test_key)
            if r and 1 in r and not np.isnan(r[1].get("p_value", np.nan)):
                return r[1]["p_value"]
            return np.nan

        p_ue = get_p("uncond_entropy")
        p_uc = get_p("uncond_ece")
        p_ce = get_p("cond_entropy_given_ece")
        p_cc = get_p("cond_ece_given_entropy")

        if np.isnan(p_ce) or np.isnan(p_cc):
            patterns10["na"] += 1
            continue

        ent_indep = p_ce < 0.10
        ece_indep = p_cc < 0.10

        if ent_indep and ece_indep:
            patterns10["both_independent"] += 1
        elif ent_indep and not ece_indep:
            patterns10["entropy_only"] += 1
        elif not ent_indep and ece_indep:
            patterns10["ece_only"] += 1
        elif p_ue < 0.10 or p_uc < 0.10:
            patterns10["redundant"] += 1
        else:
            patterns10["neither"] += 1

for pattern, count in patterns10.items():
    print(f"  {pattern:<20}: {count}")


# ─── Correlation between canaries ───
print("\n\n" + "="*80)
print("CANARY INTER-CORRELATION (entropy vs ECE)")
print("="*80)

for exp_name, path in EXPERIMENTS.items():
    if not os.path.exists(path):
        continue
    df = load_experiment(path)
    if "token_entropy" in df.columns and "ece" in df.columns:
        r = df["token_entropy"].corr(df["ece"])
        print(f"  {exp_name:<16}: r = {r:+.4f}")


# ─── Effect size (partial R²) ───
print("\n\n" + "="*80)
print("EFFECT SIZE: Partial R² from VAR(1)")
print("="*80)

for exp_name, path in EXPERIMENTS.items():
    if not os.path.exists(path):
        continue
    df = load_experiment(path)
    T = len(df)
    if T < 7:
        continue

    print(f"\n  {exp_name} (T={T}):")
    for downstream in DOWNSTREAMS:
        if downstream not in df.columns:
            continue

        cols_full = [downstream, "token_entropy", "ece"]
        cols_no_ent = [downstream, "ece"]
        cols_no_ece = [downstream, "token_entropy"]

        try:
            sub = df[cols_full].dropna()
            if len(sub) < 7:
                continue

            # Full model R²
            m_full = VAR(sub).fit(1)
            resid_full = m_full.resid[downstream]
            ss_full = (resid_full**2).sum()

            # Without entropy
            m_no_ent = VAR(df[cols_no_ent].dropna()).fit(1)
            resid_no_ent = m_no_ent.resid[downstream]
            ss_no_ent = (resid_no_ent**2).sum()

            # Without ECE
            m_no_ece = VAR(df[cols_no_ece].dropna()).fit(1)
            resid_no_ece = m_no_ece.resid[downstream]
            ss_no_ece = (resid_no_ece**2).sum()

            # Partial R²
            partial_r2_ent = 1.0 - ss_full / ss_no_ent if ss_no_ent > 0 else np.nan
            partial_r2_ece = 1.0 - ss_full / ss_no_ece if ss_no_ece > 0 else np.nan

            print(f"    {downstream:<12}: partial_R²(entropy)={partial_r2_ent:+.4f}, partial_R²(ECE)={partial_r2_ece:+.4f}")
        except Exception as e:
            print(f"    {downstream:<12}: ERROR {str(e)[:60]}")


# ─── Save full results as JSON ───
output = {
    "meta": {
        "analysis": "Conditional Granger Causality",
        "canaries": CANARIES,
        "downstreams": DOWNSTREAMS,
        "method": "VAR F-test via statsmodels",
    },
    "results": {}
}

for exp_name, exp_data in all_results.items():
    exp_out = {"T": exp_data["T"], "pairs": {}}
    for downstream, tests in exp_data["tests"].items():
        pair_out = {}
        for test_key, lag_results in tests.items():
            if lag_results is None:
                continue
            pair_out[test_key] = {}
            for lag, r in lag_results.items():
                pair_out[test_key][str(lag)] = {
                    k: (float(v) if isinstance(v, (int, float, np.floating)) else
                        [float(x) for x in v] if isinstance(v, tuple) else v)
                    for k, v in r.items()
                }
        exp_out["pairs"][downstream] = pair_out
    output["results"][exp_name] = exp_out

out_path = "/root/autodl-tmp/distrib_canary_collapse/results/analysis/conditional_granger_v2.json"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\n\nResults saved to {out_path}")
