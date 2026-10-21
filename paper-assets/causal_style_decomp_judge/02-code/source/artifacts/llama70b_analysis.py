"""Llama-3.3-70B-Instruct analysis: BT + Likert ATE + GEE for formality & verbosity."""

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

AXIS_CONFIG = {
    "formality": {
        "poles": ("formal", "casual"),
        "field": "original_formality",
        "prefers_key": "trial{}_prefers_formal",
        "pairwise_file": "pairwise_results_llama70b_formality.jsonl",
        "likert_file": "scored_llama70b_formality.jsonl",
    },
    "verbosity": {
        "poles": ("verbose", "concise"),
        "field": "original_verbosity",
        "prefers_key": "trial{}_prefers_verbose",
        "pairwise_file": "pairwise_results_llama70b_verbosity.jsonl",
        "likert_file": "scored_llama70b_verbosity.jsonl",
    },
}


def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def nli_filter(records, threshold=NLI_THRESHOLD):
    return [r for r in records if r.get("nli_cf", 0) >= threshold]


def bt_analysis(records, axis):
    import choix
    cfg = AXIS_CONFIG[axis]
    pole_a = cfg["poles"][0]
    prefers_key = cfg["prefers_key"]

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
                pair_comps.append((0, 1))
            else:
                pair_comps.append((1, 0))
        if pair_comps:
            comparisons.extend(pair_comps)
            pair_groups.append(pair_comps)

    n_pairs = len(pair_groups)
    n_comp = len(comparisons)
    consistent = sum(1 for pg in pair_groups if len(pg) == 2 and pg[0] == pg[1])
    consistency_rate = consistent / n_pairs if n_pairs > 0 else 0

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
    n_below = np.sum(boot_p < 0.5)
    p_val = max(n_below / len(boot_p), 1.0 / N_BOOTSTRAP) if n_below == 0 else n_below / len(boot_p)

    return {
        "axis": axis, "pole_a": pole_a, "n_pairs": n_pairs, "n_comp": n_comp,
        "p_a": float(p_a), "ci_lo": float(ci_lo), "ci_hi": float(ci_hi),
        "p_val": float(p_val), "consistency_rate": float(consistency_rate),
    }


def likert_ate(records, axis):
    cfg = AXIS_CONFIG[axis]
    field = cfg["field"]
    pole_a = cfg["poles"][0]

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
    n = len(diffs)
    ate = float(np.mean(diffs))
    ties = int(np.sum(diffs == 0))
    tie_rate = ties / n if n > 0 else 0.0

    non_zero = diffs[diffs != 0]
    if len(non_zero) > 0:
        _, wilcoxon_p = stats.wilcoxon(non_zero)
    else:
        wilcoxon_p = 1.0

    sd = np.std(diffs, ddof=1)
    cohens_d = ate / sd if sd > 0 else 0.0

    mean_style = float(np.mean(style_scores))
    mean_plain = float(np.mean(plain_scores))

    return {
        "ate": ate, "p": float(wilcoxon_p), "d": float(cohens_d),
        "tie_rate": float(tie_rate), "n": n,
        "mean_style": mean_style, "mean_plain": mean_plain,
    }


def gee_decomposition(records, axis):
    cfg = AXIS_CONFIG[axis]
    pole_a, pole_b = cfg["poles"]
    field = cfg["field"]

    rows = []
    pair_idx = 0
    for rec in records:
        if not rec.get("trial1_choice") or not rec.get("trial2_choice"):
            continue
        original_pole = rec.get(field)
        if original_pole not in (pole_a, pole_b):
            continue

        # Trial 1: pole_a in position A
        is_original_in_A_t1 = 1.0 if original_pole == pole_a else 0.0
        chose_A_t1 = 1.0 if rec["trial1_choice"] == "A" else 0.0
        rows.append({"pair_id": pair_idx, "is_style_in_A": 1.0,
                      "is_original_in_A": is_original_in_A_t1, "chose_A": chose_A_t1})

        # Trial 2: pole_b in position A (pole_a in position B)
        is_original_in_A_t2 = 1.0 if original_pole == pole_b else 0.0
        chose_A_t2 = 1.0 if rec["trial2_choice"] == "A" else 0.0
        rows.append({"pair_id": pair_idx, "is_style_in_A": 0.0,
                      "is_original_in_A": is_original_in_A_t2, "chose_A": chose_A_t2})
        pair_idx += 1

    df = pd.DataFrame(rows)
    exog = sm.add_constant(df[["is_style_in_A", "is_original_in_A"]])
    model = GEE(df["chose_A"], exog, groups=df["pair_id"],
                family=Binomial(), cov_struct=Exchangeable())
    fit = model.fit()

    results = {"n_pairs": pair_idx}
    for i, name in enumerate(["style", "originality"]):
        idx = i + 1
        coef = fit.params.iloc[idx]
        p = fit.pvalues.iloc[idx]
        ci = fit.conf_int().iloc[idx]
        or_val = np.exp(coef)
        or_lo = np.exp(ci.iloc[0])
        or_hi = np.exp(ci.iloc[1])
        results[name] = {
            "or": float(or_val), "or_ci": [float(or_lo), float(or_hi)], "p": float(p),
        }
    return results


def main():
    all_results = {}

    for axis in ["formality", "verbosity"]:
        cfg = AXIS_CONFIG[axis]
        pole_a = cfg["poles"][0]
        print(f"\n{'='*60}")
        print(f"  Llama-3.3-70B — {axis.upper()}")
        print(f"{'='*60}")

        result = {"judge": "Llama-3.3-70B-Instruct", "axis": axis}

        # BT
        try:
            pw_path = f"{DATA_DIR}/{cfg['pairwise_file']}"
            pw_records = nli_filter(load_records(pw_path))
            bt = bt_analysis(pw_records, axis)
            result["bt"] = {
                "p_" + pole_a: bt["p_a"],
                "ci": [bt["ci_lo"], bt["ci_hi"]],
                "p_value": bt["p_val"],
                "n_pairs": bt["n_pairs"],
                "n_comparisons": bt["n_comp"],
            }
            result["consistency_rate"] = bt["consistency_rate"]
            result["n_pairs"] = bt["n_pairs"]
            print(f"  BT P({pole_a}): {bt['p_a']:.4f} [{bt['ci_lo']:.4f}, {bt['ci_hi']:.4f}], p={bt['p_val']:.4f}")
        except Exception as e:
            print(f"  BT FAILED: {e}")
            result["bt"] = {"error": str(e)}

        # Likert
        try:
            lk_path = f"{DATA_DIR}/{cfg['likert_file']}"
            lk_records = nli_filter(load_records(lk_path))
            lk = likert_ate(lk_records, axis)
            result["likert"] = lk
            print(f"  Likert ATE: {lk['ate']:+.4f}, p={lk['p']:.4f}, d={lk['d']:+.4f}")
        except Exception as e:
            print(f"  Likert FAILED: {e}")
            result["likert"] = {"error": str(e)}

        # GEE
        try:
            gee = gee_decomposition(pw_records, axis)
            result["gee"] = {
                "style_or": gee["style"]["or"],
                "style_p": gee["style"]["p"],
                "orig_or": gee["originality"]["or"],
                "orig_p": gee["originality"]["p"],
                "style_or_ci": gee["style"]["or_ci"],
                "orig_or_ci": gee["originality"]["or_ci"],
            }
            print(f"  GEE style OR: {gee['style']['or']:.4f} (p={gee['style']['p']:.4f})")
            print(f"  GEE orig OR:  {gee['originality']['or']:.4f} (p={gee['originality']['p']:.4f})")
        except Exception as e:
            print(f"  GEE FAILED: {e}")
            result["gee"] = {"error": str(e)}

        # Blindspot
        bt_p = result.get("bt", {}).get("p_value", 1.0)
        lk_p = result.get("likert", {}).get("p", 0.0)
        result["blindspot"] = (bt_p < 0.05) and (lk_p >= 0.05)
        print(f"  Blindspot: {result['blindspot']} (BT p={bt_p:.4f}, Likert p={lk_p:.4f})")

        all_results[axis] = result

        # Save per-axis
        out_path = f"{DATA_DIR}/llama70b_{axis}_results.json"
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"  Saved: {out_path}")

    # Summary
    print(f"\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    for axis, r in all_results.items():
        bt = r.get("bt", {})
        lk = r.get("likert", {})
        gee = r.get("gee", {})
        pole_key = [k for k in bt if k.startswith("p_") and k != "p_value"]
        bt_val = bt.get(pole_key[0], "?") if pole_key else "?"
        print(f"\n  {axis}:")
        print(f"    BT win rate: {bt_val}")
        print(f"    Likert ATE: {lk.get('ate', '?')}")
        print(f"    GEE style OR: {gee.get('style_or', '?')}")
        print(f"    Blindspot: {r.get('blindspot', '?')}")

    print("\nDone.")


if __name__ == "__main__":
    main()
