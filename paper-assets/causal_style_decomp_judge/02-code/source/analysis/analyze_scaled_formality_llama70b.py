"""Analyze Llama-3.3-70B pairwise + Likert results on n=355 scaled formality data."""

import json
import sys
import numpy as np
import pandas as pd
import choix
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.families import Binomial
from statsmodels.genmod.cov_struct import Exchangeable
from scipy import stats

N_BOOTSTRAP = 10000
SEED = 42

AXIS_CONFIG = {
    "orig_field": "original_formality",
    "pole_a": "formal", "pole_b": "casual",
    "pref_key": "prefers_formal",
}


def bt_pair_bootstrap(records, pref_key, n_bootstrap=N_BOOTSTRAP, seed=SEED):
    pair_groups = []
    for rec in records:
        pair_comps = []
        for trial in [1, 2]:
            pf = rec.get(f"trial{trial}_{pref_key}")
            if pf is None:
                continue
            pair_comps.append((0, 1) if pf else (1, 0))
        if pair_comps:
            pair_groups.append(pair_comps)

    all_comps = [c for g in pair_groups for c in g]
    n_pairs = len(pair_groups)
    params = choix.ilsr_pairwise(2, all_comps, alpha=0.01)
    p_pole_a = np.exp(params[0]) / np.sum(np.exp(params))

    rng = np.random.RandomState(seed)
    boot_p = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        bc = [c for i in idx for c in pair_groups[i]]
        try:
            bp = choix.ilsr_pairwise(2, bc, alpha=0.01)
            boot_p.append(np.exp(bp[0]) / np.sum(np.exp(bp)))
        except Exception:
            pass
    boot_p = np.array(boot_p)
    ci_lo, ci_hi = np.percentile(boot_p, [2.5, 97.5])
    n_below = np.sum(boot_p < 0.5)
    p_val = 2 * min(n_below, len(boot_p) - n_below) / len(boot_p)
    p_val = max(p_val, 1.0 / n_bootstrap)
    return {"n_pairs": n_pairs, "p_pole_a": float(p_pole_a),
            "ci_lo": float(ci_lo), "ci_hi": float(ci_hi), "p_val": float(p_val)}


def likert_analysis(scored_records):
    cfg = AXIS_CONFIG
    valid = [r for r in scored_records
             if r.get("score_original") is not None and r.get("score_counterfactual") is not None]
    style_s, plain_s = [], []
    for r in valid:
        if r[cfg["orig_field"]] == cfg["pole_a"]:
            style_s.append(r["score_original"])
            plain_s.append(r["score_counterfactual"])
        else:
            style_s.append(r["score_counterfactual"])
            plain_s.append(r["score_original"])

    style_s = np.array(style_s, dtype=float)
    plain_s = np.array(plain_s, dtype=float)
    diffs = style_s - plain_s
    ate = float(np.mean(diffs))
    pooled_std = np.sqrt((np.var(style_s, ddof=1) + np.var(plain_s, ddof=1)) / 2)
    cohen_d = float(ate / pooled_std) if pooled_std > 0 else 0.0
    non_zero = diffs[diffs != 0]
    if len(non_zero) > 0:
        _, wilcoxon_p = stats.wilcoxon(non_zero)
    else:
        wilcoxon_p = 1.0
    tie_rate = float(np.mean(diffs == 0))
    _, ttest_p = stats.ttest_rel(style_s, plain_s)

    return {"n": len(valid), "ate": ate, "cohen_d": cohen_d,
            "wilcoxon_p": float(wilcoxon_p), "ttest_p": float(ttest_p), "tie_rate": tie_rate}


def gee_analysis(pairwise_records):
    cfg = AXIS_CONFIG
    rows = []
    for i, r in enumerate(pairwise_records):
        orig = r[cfg["orig_field"]]
        rows.append({"pair_id": i, "is_style_in_A": 1.0,
                      "is_original_in_A": 1.0 if orig == cfg["pole_a"] else 0.0,
                      "chose_A": 1.0 if r["trial1_choice"] == "A" else 0.0})
        rows.append({"pair_id": i, "is_style_in_A": 0.0,
                      "is_original_in_A": 1.0 if orig == cfg["pole_b"] else 0.0,
                      "chose_A": 1.0 if r["trial2_choice"] == "A" else 0.0})

    df = pd.DataFrame(rows)
    exog = sm.add_constant(df[["is_style_in_A", "is_original_in_A"]])
    model = GEE(df["chose_A"], exog, groups=df["pair_id"],
                family=Binomial(), cov_struct=Exchangeable())
    result = model.fit()

    def _or_ci(name):
        c = result.params[name]
        se = result.bse[name]
        lo = np.exp(c - 1.96 * se)
        hi = np.exp(c + 1.96 * se)
        return float(np.exp(c)), float(result.pvalues[name]), float(lo), float(hi)

    s_or, s_p, s_lo, s_hi = _or_ci("is_style_in_A")
    o_or, o_p, o_lo, o_hi = _or_ci("is_original_in_A")

    return {"style_or": s_or, "style_p": s_p, "style_ci": [s_lo, s_hi],
            "orig_or": o_or, "orig_p": o_p, "orig_ci": [o_lo, o_hi]}


def fp(p):
    return "< 0.0001" if p < 0.0001 else f"{p:.4f}"


def main():
    data_dir = "/root/causal_style_decomp_judge/data"
    pw_path = f"{data_dir}/pairwise_results_scaled_formality_llama70b.jsonl"
    sc_path = f"{data_dir}/scored_scaled_formality_llama70b.jsonl"
    output_path = f"{data_dir}/analysis_scaled_formality_llama70b.json"

    with open(pw_path) as f:
        pw_all = [json.loads(l) for l in f if l.strip()]

    with open(sc_path) as f:
        sc_all = [json.loads(l) for l in f if l.strip()]

    print(f"Loaded {len(pw_all)} pairwise, {len(sc_all)} scored records")

    # Filter to consistent pairwise only
    pw_consistent = [r for r in pw_all if r.get("consistent", False)]
    print(f"Consistent pairwise: {len(pw_consistent)}/{len(pw_all)}")

    bt = bt_pair_bootstrap(pw_consistent, AXIS_CONFIG["pref_key"])
    lk = likert_analysis(sc_all)
    gee = gee_analysis(pw_consistent)

    bt_sig = bt["p_val"] < 0.05
    likert_sig = lk["wilcoxon_p"] < 0.05
    blindspot = bt_sig and not likert_sig

    results = {
        "judge": "Llama-3.3-70B-Instruct",
        "axis": "formality",
        "n_total": len(pw_all),
        "n_consistent": len(pw_consistent),
        "bt": bt,
        "likert": lk,
        "gee": gee,
        "bt_significant": bt_sig,
        "likert_significant": likert_sig,
        "blindspot": blindspot,
    }

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print("  Llama-3.3-70B x Formality (Scaled n=355)")
    print(f"{'='*60}")
    print(f"Pairs: {bt['n_pairs']} (consistent: {len(pw_consistent)}/{len(pw_all)})")
    print(f"BT: P(formal)={bt['p_pole_a']*100:.1f}% "
          f"[{bt['ci_lo']*100:.1f}%, {bt['ci_hi']*100:.1f}%], "
          f"p={fp(bt['p_val'])}")
    print(f"Likert: Cohen's d={lk['cohen_d']:.3f}, "
          f"ATE={lk['ate']:.3f}, "
          f"Wilcoxon p={fp(lk['wilcoxon_p'])}, "
          f"ttest p={fp(lk['ttest_p'])}, "
          f"tie_rate={lk['tie_rate']*100:.1f}%")
    print(f"GEE: Style OR={gee['style_or']:.2f} [{gee['style_ci'][0]:.2f}, {gee['style_ci'][1]:.2f}] p={fp(gee['style_p'])}, "
          f"Orig OR={gee['orig_or']:.2f} [{gee['orig_ci'][0]:.2f}, {gee['orig_ci'][1]:.2f}] p={fp(gee['orig_p'])}")
    print(f"Blindspot: {'YES' if blindspot else 'No'}")
    print(f"\nComparison with Qwen3-32B on same data:")
    print(f"  Qwen3: BT=67.5%, Style OR=2.15, Orig OR=4.99")
    print(f"  Llama: BT={bt['p_pole_a']*100:.1f}%, Style OR={gee['style_or']:.2f}, Orig OR={gee['orig_or']:.2f}")
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
