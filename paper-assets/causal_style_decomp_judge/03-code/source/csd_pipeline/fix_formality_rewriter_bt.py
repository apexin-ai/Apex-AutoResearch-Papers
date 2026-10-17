# Fix formality rewriter independence: use ALL NLI-pass pairs (not consistent-only)
import json
import numpy as np
import pandas as pd
import choix
import statsmodels.api as sm
from scipy import stats
from statsmodels.genmod.cov_struct import Exchangeable
from statsmodels.genmod.families import Binomial
from statsmodels.genmod.generalized_estimating_equations import GEE

DATA_DIR = "/root/causal_style_decomp_judge/data"
PAIRWISE_FILE = f"{DATA_DIR}/pairwise_results_gpt4o_rewriter_formality_qwen32b.jsonl"
SCORED_FILE = f"{DATA_DIR}/scored_gpt4o_rewriter_formality_qwen32b.jsonl"
VERIFIED_FILE = f"{DATA_DIR}/verified_gpt4o_rewriter_formality.jsonl"
RESULTS_FILE = f"{DATA_DIR}/gpt4o_rewriter_formality_results.json"

NLI_THRESHOLD = 0.90
N_BOOT = 10000
SEED = 42
FORMAL, CASUAL = 0, 1


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def analyze_bt(pairwise_data):
    # ALL NLI-pass pairs — no consistent filter
    data = [r for r in pairwise_data if r.get("nli_cf", 0) >= NLI_THRESHOLD]

    comparisons = []
    pair_groups = {}

    for rec in data:
        pair_id = rec["id"]
        pcomps = []

        t1 = rec.get("trial1_choice")
        if t1 in ("A", "B"):
            # Trial 1: A=formal, B=casual
            pcomps.append((FORMAL, CASUAL) if t1 == "A" else (CASUAL, FORMAL))

        t2 = rec.get("trial2_choice")
        if t2 in ("A", "B"):
            # Trial 2: A=casual, B=formal
            pcomps.append((CASUAL, FORMAL) if t2 == "A" else (FORMAL, CASUAL))

        comparisons.extend(pcomps)
        pair_groups[pair_id] = pcomps

    if not comparisons:
        return None

    params = choix.ilsr_pairwise(2, comparisons, alpha=0.01)
    diff = params[FORMAL] - params[CASUAL]
    p_formal = 1.0 / (1.0 + np.exp(-diff))

    rng = np.random.RandomState(SEED)
    pair_ids = list(pair_groups.keys())
    n_pairs = len(pair_ids)
    boot_probs = []

    for _ in range(N_BOOT):
        idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_comps = []
        for i in idx:
            boot_comps.extend(pair_groups[pair_ids[i]])
        try:
            bp = choix.ilsr_pairwise(2, boot_comps, alpha=0.01)
            boot_probs.append(1.0 / (1.0 + np.exp(-(bp[FORMAL] - bp[CASUAL]))))
        except Exception:
            pass

    boot_probs = np.array(boot_probs)
    ci_lo, ci_hi = np.percentile(boot_probs, [2.5, 97.5])

    n_below = int(np.sum(boot_probs < 0.5))
    raw_p = n_below / len(boot_probs) if len(boot_probs) > 0 else 1.0
    if raw_p == 0:
        raw_p = 1.0 / len(boot_probs)

    return {
        "p_formal": round(float(p_formal), 4),
        "ci": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
        "p_value": round(float(raw_p), 4),
        "n_pairs": n_pairs,
        "n_comparisons": len(comparisons),
    }


def analyze_gee(pairwise_data):
    # ALL NLI-pass pairs — no consistent filter
    data = [r for r in pairwise_data if r.get("nli_cf", 0) >= NLI_THRESHOLD]

    X_rows, y_rows, pair_ids = [], [], []
    pair_idx = 0

    for rec in data:
        if not rec.get("trial1_choice") or not rec.get("trial2_choice"):
            continue
        original_pole = rec.get("original_formality")
        if original_pole not in ("formal", "casual"):
            continue

        # Trial 1: A=formal, B=casual
        is_formal_in_A = 1.0
        is_original_in_A = 1.0 if original_pole == "formal" else 0.0
        chose_A = 1.0 if rec["trial1_choice"] == "A" else 0.0
        X_rows.append([is_formal_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        # Trial 2: A=casual, B=formal
        is_formal_in_A = 0.0
        is_original_in_A = 1.0 if original_pole == "casual" else 0.0
        chose_A = 1.0 if rec["trial2_choice"] == "A" else 0.0
        X_rows.append([is_formal_in_A, is_original_in_A])
        y_rows.append(chose_A)
        pair_ids.append(pair_idx)

        pair_idx += 1

    X = np.array(X_rows)
    y = np.array(y_rows)
    pair_arr = np.array(pair_ids)

    df = pd.DataFrame({
        "chose_A": y,
        "is_formal_in_A": X[:, 0],
        "is_original_in_A": X[:, 1],
        "pair_id": pair_arr,
    })

    exog = sm.add_constant(df[["is_formal_in_A", "is_original_in_A"]])
    model = GEE(
        df["chose_A"],
        exog,
        groups=df["pair_id"],
        family=Binomial(),
        cov_struct=Exchangeable(),
    )
    fit = model.fit()

    style_or = float(np.exp(fit.params.iloc[1]))
    style_p = float(fit.pvalues.iloc[1])
    orig_or = float(np.exp(fit.params.iloc[2]))
    orig_p = float(fit.pvalues.iloc[2])

    return {
        "style_or": round(style_or, 2),
        "style_p": round(style_p, 4),
        "orig_or": round(orig_or, 2),
        "orig_p": round(orig_p, 4),
    }


def analyze_likert(scored_data):
    data = [r for r in scored_data if r.get("nli_cf", 0) >= NLI_THRESHOLD]

    formal_scores, casual_scores = [], []
    for r in data:
        s_orig = r.get("score_original")
        s_cf = r.get("score_counterfactual")
        if s_orig is None or s_cf is None:
            continue
        if r["original_formality"] == "formal":
            formal_scores.append(s_orig)
            casual_scores.append(s_cf)
        else:
            casual_scores.append(s_orig)
            formal_scores.append(s_cf)

    formal_arr = np.array(formal_scores, dtype=float)
    casual_arr = np.array(casual_scores, dtype=float)
    ate = float(np.mean(formal_arr) - np.mean(casual_arr))

    diffs = formal_arr - casual_arr
    non_zero = diffs[diffs != 0]
    _, p = stats.wilcoxon(non_zero) if len(non_zero) > 0 else (None, 1.0)

    tie_rate = float(np.mean(diffs == 0))
    pooled_sd = np.sqrt(
        ((len(formal_arr) - 1) * np.var(formal_arr, ddof=1)
         + (len(casual_arr) - 1) * np.var(casual_arr, ddof=1))
        / (len(formal_arr) + len(casual_arr) - 2)
    )
    d = ate / pooled_sd if pooled_sd > 0 else 0

    return {
        "ate": round(ate, 4),
        "p": round(float(p), 4),
        "d": round(d, 4),
        "tie_rate": round(tie_rate, 3),
        "n": len(formal_scores),
        "mean_formal": round(float(np.mean(formal_arr)), 4),
        "mean_casual": round(float(np.mean(casual_arr)), 4),
    }


def main():
    pairwise_data = load_jsonl(PAIRWISE_FILE)
    scored_data = load_jsonl(SCORED_FILE)
    verified = load_jsonl(VERIFIED_FILE)

    n_total = len(verified)
    n_pass = sum(1 for r in verified if r.get("passed_cf", False))
    nli_rate = n_pass / n_total if n_total > 0 else 0

    print(f"NLI pass: {n_pass}/{n_total} ({nli_rate*100:.1f}%)")
    print(f"Pairwise records: {len(pairwise_data)}")

    bt = analyze_bt(pairwise_data)
    gee = analyze_gee(pairwise_data)
    likert = analyze_likert(scored_data)

    bt_sig = bt["p_value"] < 0.05 if bt else False
    likert_insig = likert["p"] >= 0.05
    blindspot = bt_sig and likert_insig

    baseline = {"bt_p_formal": 0.665, "gee_style_or": 4.20, "gee_orig_or": 4.70}

    results = {
        "experiment": "gpt4o_rewriter_formality_independence",
        "rewriter": "GPT-4o",
        "judge": "Qwen3-32B",
        "dataset": "LLMBar",
        "axis": "formality",
        "n_total": n_total,
        "n_nli_pass": n_pass,
        "nli_rate": round(nli_rate, 3),
        "bt": bt,
        "gee": gee,
        "likert": likert,
        "blindspot": blindspot,
        "baseline_comparison": {
            "qwen32b_rewriter_bt_p_formal": baseline["bt_p_formal"],
            "gpt4o_rewriter_bt_p_formal": bt["p_formal"] if bt else None,
            "delta_pp": round((bt["p_formal"] - baseline["bt_p_formal"]) * 100, 1) if bt else None,
            "ci_overlap": bool(bt["ci"][0] <= baseline["bt_p_formal"] <= bt["ci"][1]) if bt else None,
        },
        "note": "Fixed: using ALL NLI-pass pairs, not consistent-only",
    }

    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*70}")
    print("  GPT-4o Rewriter Formality — FIXED (all NLI-pass pairs)")
    print(f"{'='*70}")

    if bt:
        print(f"\n  BT P(formal) = {bt['p_formal']*100:.1f}%  "
              f"CI [{bt['ci'][0]*100:.1f}%, {bt['ci'][1]*100:.1f}%]  "
              f"p = {bt['p_value']}")
        print(f"  N = {bt['n_pairs']} pairs, {bt['n_comparisons']} comparisons")

    if gee:
        print(f"\n  GEE Style OR = {gee['style_or']}  (p = {gee['style_p']})")
        print(f"  GEE Orig OR  = {gee['orig_or']}  (p = {gee['orig_p']})")

    if likert:
        print(f"\n  Likert ATE = {likert['ate']}  p = {likert['p']}  d = {likert['d']}")
        print(f"  Tie rate = {likert['tie_rate']}  N = {likert['n']}")

    print(f"\n  Blindspot: {'YES' if blindspot else 'NO'}")

    if bt:
        print(f"\n  vs Baseline (Qwen3-32B rewriter):")
        print(f"    Qwen3-32B BT = {baseline['bt_p_formal']*100:.1f}%")
        print(f"    GPT-4o    BT = {bt['p_formal']*100:.1f}%")
        delta = (bt["p_formal"] - baseline["bt_p_formal"]) * 100
        overlap = bt["ci"][0] <= baseline["bt_p_formal"] <= bt["ci"][1]
        print(f"    Delta = {delta:+.1f}pp, CI overlap: {overlap}")

    print(f"{'='*70}")
    print(f"\nResults written to {RESULTS_FILE}")


if __name__ == "__main__":
    main()
