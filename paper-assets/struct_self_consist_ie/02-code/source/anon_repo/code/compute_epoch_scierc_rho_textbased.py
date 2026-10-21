"""Compute within-instance Spearman rho(LP, F1) for SciERC epoch ablation.

Uses text-based (text, type) entity matching, consistent with tab:within_rho.
Does NOT import evaluation.py (which uses span-based matching for D146).
"""
import json
import numpy as np
from scipy.stats import spearmanr

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "3-epoch": f"{BASE}/output/exp_029a_scierc_3epoch/samples.jsonl",
    "5-epoch": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
    "10-epoch": f"{BASE}/output/exp_029b_scierc_10epoch/samples.jsonl",
}


def entity_set_text(entities):
    """Text-based entity set: (text, type) tuples."""
    return {(e["text"], e["type"]) for e in entities}


def f1_text(pred_ents, gold_ents):
    """Per-instance entity F1 using text-based matching."""
    pred_set = entity_set_text(pred_ents)
    gold_set = entity_set_text(gold_ents)
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def compute_within_rho(path):
    with open(path) as f:
        records = [json.loads(line) for line in f if line.strip()]

    rhos = []
    n_constant_lp = 0
    n_constant_f1 = 0
    n_too_few = 0
    n_gold_empty = 0

    greedy_f1s = []
    lp_sel_f1s = []

    for rec in records:
        gold_ents = rec.get("gold", {}).get("entities", [])
        if not gold_ents:
            n_gold_empty += 1
            continue

        gold_set = entity_set_text(gold_ents)
        samples = rec.get("samples", [])
        if len(samples) < 3:
            n_too_few += 1
            continue

        lps = []
        f1s = []
        for s in samples:
            lp = s.get("mean_logprob")
            if lp is None:
                continue
            f1 = f1_text(s.get("entities", []), gold_ents)
            lps.append(lp)
            f1s.append(f1)

        if len(lps) < 3:
            n_too_few += 1
            continue

        # Greedy F1
        greedy = rec.get("greedy")
        if greedy:
            g_f1 = f1_text(greedy.get("entities", []), gold_ents)
        else:
            g_f1 = 0.0
        greedy_f1s.append(g_f1)

        # LP-selected F1
        best_lp_idx = int(np.argmax(lps))
        lp_sel_f1s.append(f1s[best_lp_idx])

        if len(set(lps)) < 2:
            n_constant_lp += 1
            continue
        if len(set(f1s)) < 2:
            n_constant_f1 += 1
            continue

        rho_val, _ = spearmanr(lps, f1s)
        if not np.isnan(rho_val):
            rhos.append(rho_val)

    rhos = np.array(rhos)
    n_total = len(records)
    n_valid = len(rhos)

    greedy_mean = float(np.mean(greedy_f1s)) if greedy_f1s else 0.0
    lp_sel_mean = float(np.mean(lp_sel_f1s)) if lp_sel_f1s else 0.0
    lp_delta_pp = (lp_sel_mean - greedy_mean) * 100

    return {
        "n_total": n_total,
        "n_gold_empty": n_gold_empty,
        "n_too_few": n_too_few,
        "n_constant_lp": n_constant_lp,
        "n_constant_f1": n_constant_f1,
        "n_valid": n_valid,
        "median_rho": round(float(np.median(rhos)), 4) if n_valid > 0 else None,
        "mean_rho": round(float(np.mean(rhos)), 4) if n_valid > 0 else None,
        "std_rho": round(float(np.std(rhos)), 4) if n_valid > 0 else None,
        "pct_positive": round(float((rhos > 0).mean() * 100), 1) if n_valid > 0 else None,
        "q25": round(float(np.percentile(rhos, 25)), 4) if n_valid > 0 else None,
        "q75": round(float(np.percentile(rhos, 75)), 4) if n_valid > 0 else None,
        "greedy_f1": round(greedy_mean, 4),
        "lp_sel_f1": round(lp_sel_mean, 4),
        "lp_delta_pp": round(lp_delta_pp, 2),
    }


if __name__ == "__main__":
    print("=" * 70)
    print("SciERC Epoch Ablation: Within-Instance rho(LP, F1)")
    print("Matching: TEXT-BASED (text, type)")
    print("=" * 70)

    all_results = {}
    for label, path in DATASETS.items():
        print(f"\n--- {label} ---")
        print(f"  Path: {path}")
        result = compute_within_rho(path)
        all_results[label] = result
        for k, v in result.items():
            print(f"  {k}: {v}")

    print("\n" + "=" * 70)
    print("SUMMARY TABLE (text-based matching)")
    print(f"{'Epoch':<12} {'median_rho':>12} {'mean_rho':>12} {'%pos':>8} {'n_valid':>8} {'n_total':>8} {'LP_delta_pp':>12}")
    print("-" * 72)
    for label in ["3-epoch", "5-epoch", "10-epoch"]:
        r = all_results[label]
        print(f"{label:<12} {r['median_rho']:>12} {r['mean_rho']:>12} {r['pct_positive']:>8} {r['n_valid']:>8} {r['n_total']:>8} {r['lp_delta_pp']:>12}")

    out_path = f"{BASE}/output/epoch_scierc_textbased_rho.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to {out_path}")
