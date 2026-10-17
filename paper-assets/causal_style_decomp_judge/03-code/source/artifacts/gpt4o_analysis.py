"""GPT-4o full statistical analysis: Likert ATE + Bradley-Terry + GEE decomposition."""

import json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.cov_struct import Exchangeable
from statsmodels.genmod.families import Binomial
from scipy import stats

DATA_DIR = "/root/causal_style_decomp_judge/data"
NLI_THRESHOLD = 0.90
N_BOOTSTRAP = 10000
SEED = 42


def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def nli_filter(records, threshold=NLI_THRESHOLD):
    return [r for r in records if r.get("nli_cf", 0) >= threshold]


# ============================================================
# 1 & 2: Likert ATE
# ============================================================

def likert_ate(records, axis):
    """Compute ATE from Likert scores. Returns dict with ATE, p, d, tie_rate."""
    if axis == "verbosity":
        field = "original_verbosity"
        pole_a = "verbose"
    else:
        field = "original_register"
        pole_a = "academic"

    style_scores = []
    plain_scores = []

    for rec in records:
        orig = rec.get(field)
        s_orig = rec.get("score_original")
        s_cf = rec.get("score_counterfactual")
        if orig is None or s_orig is None or s_cf is None:
            continue
        if orig == pole_a:
            style_scores.append(s_orig)
            plain_scores.append(s_cf)
        else:
            style_scores.append(s_cf)
            plain_scores.append(s_orig)

    style_scores = np.array(style_scores, dtype=float)
    plain_scores = np.array(plain_scores, dtype=float)
    diffs = style_scores - plain_scores

    ate = np.mean(diffs)
    n = len(diffs)
    ties = np.sum(diffs == 0)
    tie_rate = ties / n

    # Wilcoxon signed-rank (exclude ties)
    non_zero = diffs[diffs != 0]
    if len(non_zero) > 0:
        wilcoxon_stat, wilcoxon_p = stats.wilcoxon(non_zero)
    else:
        wilcoxon_stat, wilcoxon_p = 0, 1.0

    # Paired t-test
    t_stat, t_p = stats.ttest_rel(style_scores, plain_scores)

    # Cohen's d (paired)
    sd = np.std(diffs, ddof=1)
    cohens_d = ate / sd if sd > 0 else 0.0

    return {
        "axis": axis,
        "n": n,
        "ate": ate,
        "wilcoxon_p": wilcoxon_p,
        "t_p": t_p,
        "cohens_d": cohens_d,
        "tie_rate": tie_rate,
    }


# ============================================================
# 3 & 4: Bradley-Terry with pair-level bootstrap
# ============================================================

def bt_analysis(records, axis):
    import choix

    if axis == "verbosity":
        prefers_key = "trial{}_prefers_verbose"
        pole_a = "verbose"
    else:
        prefers_key = "trial{}_prefers_academic"
        pole_a = "academic"

    pair_groups = []
    comparisons = []
    for rec in records:
        pair_comps = []
        for trial in [1, 2]:
            key = prefers_key.format(trial)
            prefers_a = rec.get(key)
            if prefers_a is None:
                continue
            if prefers_a:
                pair_comps.append((0, 1))  # pole_a wins
            else:
                pair_comps.append((1, 0))  # pole_b wins
        if pair_comps:
            comparisons.extend(pair_comps)
            pair_groups.append(pair_comps)

    n_pairs = len(pair_groups)
    n_comp = len(comparisons)

    params = choix.ilsr_pairwise(2, comparisons, alpha=0.01)
    p_a = np.exp(params[0]) / (np.exp(params[0]) + np.exp(params[1]))

    rng = np.random.RandomState(SEED)
    boot_p = []
    for _ in range(N_BOOTSTRAP):
        sampled_idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_comps = []
        for i in sampled_idx:
            boot_comps.extend(pair_groups[i])
        try:
            bp = choix.ilsr_pairwise(2, boot_comps, alpha=0.01)
            boot_p.append(np.exp(bp[0]) / (np.exp(bp[0]) + np.exp(bp[1])))
        except Exception:
            pass

    boot_p = np.array(boot_p)
    ci_lo = np.percentile(boot_p, 2.5)
    ci_hi = np.percentile(boot_p, 97.5)

    # Two-tailed p-value
    if p_a >= 0.5:
        n_extreme = np.sum(boot_p <= (1 - p_a))
    else:
        n_extreme = np.sum(boot_p >= (1 - p_a))
    # Also compute as proportion below 0.5
    n_below = np.sum(boot_p < 0.5)
    p_val = 2 * min(n_below, len(boot_p) - n_below) / len(boot_p)
    if p_val == 0:
        p_val = 1.0 / N_BOOTSTRAP

    return {
        "axis": axis,
        "pole_a": pole_a,
        "n_pairs": n_pairs,
        "n_comp": n_comp,
        "p_style": p_a,
        "ci_lo": ci_lo,
        "ci_hi": ci_hi,
        "p_val": p_val,
    }


# ============================================================
# 5 & 6: GEE Decomposition
# ============================================================

def gee_decomposition(records, axis):
    if axis == "verbosity":
        field = "original_verbosity"
        pole_a = "verbose"
        pole_b = "concise"
    else:
        field = "original_register"
        pole_a = "academic"
        pole_b = "conversational"

    X_rows, y_rows, pair_ids = [], [], []
    pair_idx = 0

    for rec in records:
        if not rec.get("trial1_choice") or not rec.get("trial2_choice"):
            continue
        original_pole = rec.get(field)
        if original_pole not in (pole_a, pole_b):
            continue

        # Trial 1: A=pole_a, B=pole_b
        is_style_in_A = 1.0
        is_original_in_A = 1.0 if original_pole == pole_a else 0.0
        chose_A = 1.0 if rec["trial1_choice"] == "A" else 0.0
        X_rows.append([is_style_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        # Trial 2: A=pole_b, B=pole_a
        is_style_in_A = 0.0
        is_original_in_A = 1.0 if original_pole == pole_b else 0.0
        chose_A = 1.0 if rec["trial2_choice"] == "A" else 0.0
        X_rows.append([is_style_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        pair_idx += 1

    X = np.array(X_rows)
    y = np.array(y_rows)
    pair_ids = np.array(pair_ids)

    df = pd.DataFrame({
        "chose_A": y,
        "is_style_in_A": X[:, 0],
        "is_original_in_A": X[:, 1],
        "pair_id": pair_ids,
    })

    exog = sm.add_constant(df[["is_style_in_A", "is_original_in_A"]])
    model = GEE(
        df["chose_A"], exog, groups=df["pair_id"],
        family=Binomial(), cov_struct=Exchangeable(),
    )
    fit = model.fit()

    results = {"n_pairs": pair_idx}
    for i, name in enumerate(["style", "originality"]):
        idx = i + 1
        coef = fit.params.iloc[idx]
        se = fit.bse.iloc[idx]
        p = fit.pvalues.iloc[idx]
        ci = fit.conf_int().iloc[idx]
        or_val = np.exp(coef)
        or_lo = np.exp(ci.iloc[0])
        or_hi = np.exp(ci.iloc[1])
        results[name] = {
            "or": or_val, "or_ci": (or_lo, or_hi), "p": p,
            "coef": coef, "se": se,
        }

    return results


# ============================================================
# Main
# ============================================================

def fmt_p(p):
    if p < 0.0001:
        return "< 0.0001"
    return f"{p:.4f}"


def main():
    results_likert = []
    results_bt = []
    results_gee = []
    errors = []

    # --- Likert ATE ---
    for axis, fname in [("verbosity", "scored_gpt4o_verbosity.jsonl"),
                        ("register", "scored_gpt4o_register.jsonl")]:
        try:
            records = load_records(f"{DATA_DIR}/{fname}")
            filtered = nli_filter(records)
            r = likert_ate(filtered, axis)
            results_likert.append(r)
            print(f"[Likert {axis}] n={r['n']}, ATE={r['ate']:.4f}")
        except Exception as e:
            errors.append(f"Likert {axis}: {e}")
            print(f"[Likert {axis}] FAILED: {e}")

    # --- Bradley-Terry ---
    for axis, fname in [("verbosity", "pairwise_results_gpt4o_verbosity.jsonl"),
                        ("register", "pairwise_results_gpt4o_register.jsonl")]:
        try:
            records = load_records(f"{DATA_DIR}/{fname}")
            filtered = nli_filter(records)
            r = bt_analysis(filtered, axis)
            results_bt.append(r)
            print(f"[BT {axis}] n_pairs={r['n_pairs']}, P({r['pole_a']})={r['p_style']:.4f}")
        except Exception as e:
            errors.append(f"BT {axis}: {e}")
            print(f"[BT {axis}] FAILED: {e}")

    # --- GEE ---
    for axis, fname in [("verbosity", "pairwise_results_gpt4o_verbosity.jsonl"),
                        ("register", "pairwise_results_gpt4o_register.jsonl")]:
        try:
            records = load_records(f"{DATA_DIR}/{fname}")
            filtered = nli_filter(records)
            r = gee_decomposition(filtered, axis)
            results_gee.append({"axis": axis, **r})
            print(f"[GEE {axis}] n_pairs={r['n_pairs']}, style OR={r['style']['or']:.4f}")
        except Exception as e:
            errors.append(f"GEE {axis}: {e}")
            print(f"[GEE {axis}] FAILED: {e}")

    # --- Summary ---
    print("\n" + "=" * 60)
    print("=== GPT-4o Statistical Analysis Summary ===")
    print("=" * 60)

    print("\nLIKERT ATE:")
    print(f"| {'Axis':<10} | {'ATE':<7} | {'p (Wilcoxon)':<13} | {'Cohen d':<8} | {'Tie Rate':<9} |")
    print(f"|{'-'*12}|{'-'*9}|{'-'*15}|{'-'*10}|{'-'*11}|")
    for r in results_likert:
        print(f"| {r['axis']:<10} | {r['ate']:>+.4f} | {fmt_p(r['wilcoxon_p']):<13} | {r['cohens_d']:>+.4f} | {r['tie_rate']:.4f}   |")

    print("\nBRADLEY-TERRY:")
    print(f"| {'Axis':<10} | {'P(style)':<9} | {'CI [lo, hi]':<18} | {'p-value':<10} |")
    print(f"|{'-'*12}|{'-'*11}|{'-'*20}|{'-'*12}|")
    for r in results_bt:
        print(f"| {r['axis']:<10} | {r['p_style']:.4f}   | [{r['ci_lo']:.4f}, {r['ci_hi']:.4f}] | {fmt_p(r['p_val']):<10} |")

    print("\nGEE DECOMPOSITION:")
    print(f"| {'Axis':<10} | {'Style OR':<9} | {'Style p':<10} | {'Orig OR':<8} | {'Orig p':<10} |")
    print(f"|{'-'*12}|{'-'*11}|{'-'*12}|{'-'*10}|{'-'*12}|")
    for r in results_gee:
        s = r["style"]
        o = r["originality"]
        print(f"| {r['axis']:<10} | {s['or']:.4f}   | {fmt_p(s['p']):<10} | {o['or']:.4f}  | {fmt_p(o['p']):<10} |")

    if errors:
        print(f"\nFAILED ANALYSES ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")

    print("\nDone.")


if __name__ == "__main__":
    main()
