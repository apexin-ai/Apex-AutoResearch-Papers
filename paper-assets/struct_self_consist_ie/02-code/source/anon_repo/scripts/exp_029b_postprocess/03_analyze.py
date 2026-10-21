#!/usr/bin/env python3
"""exp_029b analysis: SciERC 10-epoch degeneracy comparison.

Computes:
1. Constant F1 gold-filtered degeneracy rate
2. LP selection F1 (best-of-N by logprob)
3. All 5 signals QE metrics (SJ, FK, VC, EM, LP)
4. Within-instance rho(LP, F1)
5. LP range statistics
6. Comparison table vs 5-epoch baseline (dynamic) and 3-epoch (exp_029a)
7. Conclusion judgment
"""
import json
import os
import sys
import warnings
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface, _extract_surface_keys, _ner_soft_jaccard_pair
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
INPUT_PATH = f"{BASE}/output/exp_029b_scierc_10epoch/samples.jsonl"
OUTPUT_DIR = f"{BASE}/output/exp_029b_scierc_10epoch"
SUBTASK = "ner"
N_SAMPLES = 8

# Dynamic baseline paths
BASELINE_3EPOCH_PATH = f"{BASE}/output/exp_029a_scierc_3epoch/comparison_report_fixed.json"
BASELINE_5EPOCH_SAMPLES_PATH = f"{BASE}/output/exp_012_rerun_1024/samples.jsonl"


def load_baseline_from_029a():
    """Load 3-epoch and 5-epoch baselines from exp_029a analysis results."""
    with open(BASELINE_3EPOCH_PATH) as f:
        data = json.load(f)

    ref_3epoch = {
        "degeneracy_cf1_pct": data["degeneracy"]["rate_pct"],
        "greedy_f1": data["basic"]["greedy_macro_f1"],
        "oracle_f1": data["basic"]["oracle_macro_f1"],
        "lp_sel_delta_pp": data["lp_selection"]["delta_pp"],
        "within_instance_median_rho": data["within_instance_rho"]["median"],
        "lp_range_mean": data["lp_range"]["mean"],
    }

    ref_5epoch = data["comparison_baseline"]["baseline_ref"]

    return ref_3epoch, ref_5epoch


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


def entity_strict_f1(pred_entities, gold_entities):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return f1


def compute_signals(samples):
    n = len(samples)

    lp_scores = []
    for s in samples:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lp_scores.append(lp)

    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]

    sj_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            s = _ner_soft_jaccard_pair(samples[i].get("entities", []), samples[j].get("entities", []))
            sj_matrix[i][j] = s
            sj_matrix[j][i] = s
    np.fill_diagonal(sj_matrix, 1.0)
    sj_scores = [float(np.mean([sj_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]

    fk_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            fk_matrix[i][j] = s
            fk_matrix[j][i] = s
    np.fill_diagonal(fk_matrix, 1.0)
    fk_scores = [float(np.mean([fk_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]

    all_keys_count = Counter()
    for ks in key_sets:
        for key in ks:
            all_keys_count[key] += 1
    vc_scores = []
    for ks in key_sets:
        if not ks:
            vc_scores.append(0.0)
        else:
            fracs = [all_keys_count[key] / n for key in ks]
            vc_scores.append(float(np.mean(fracs)))

    em_scores = [float(sum(1 for j in range(n) if j != k and key_sets[k] == key_sets[j])) for k in range(n)]

    return {"LP": lp_scores, "SJ": sj_scores, "FK": fk_scores, "EM": em_scores, "VC": vc_scores}, key_sets


def safe_spearmanr(x, y):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        if len(set(x)) < 2 or len(set(y)) < 2:
            return float('nan'), float('nan')
        r, p = spearmanr(x, y)
        return float(r), float(p)


def safe_auroc(labels, scores):
    from sklearn.metrics import roc_auc_score
    if len(set(labels)) < 2 or len(set(scores)) < 2:
        return float('nan')
    return roc_auc_score(labels, scores)


def main():
    print("=" * 60)
    print("  exp_029b: SciERC 10-epoch LoRA Degeneracy Analysis")
    print("=" * 60)

    # Load dynamic baselines
    print("\n--- Loading baselines ---")
    ref_3epoch, ref_5epoch = load_baseline_from_029a()
    print(f"  5-epoch baseline: degeneracy={ref_5epoch['degeneracy_cf1_pct']:.1f}%, "
          f"lp_sel_delta={ref_5epoch['lp_sel_delta_pp']:+.2f}pp, "
          f"within_rho_med={ref_5epoch['within_instance_median_rho']:.4f}")
    print(f"  3-epoch baseline: degeneracy={ref_3epoch['degeneracy_cf1_pct']:.1f}%, "
          f"lp_sel_delta={ref_3epoch['lp_sel_delta_pp']:+.2f}pp, "
          f"within_rho_med={ref_3epoch['within_instance_median_rho']:.4f}")

    # Load data
    print(f"\n--- 1. Loading data from {INPUT_PATH} ---")
    instances = load_data(INPUT_PATH)
    n_total = len(instances)
    print(f"  Loaded {n_total} instances")

    # Gold filter
    gold_nonempty = []
    for inst in instances:
        gold_raw = inst.get("gold_entities", inst.get("gold", []))
        gold = gold_raw.get("entities", []) if isinstance(gold_raw, dict) else gold_raw
        if isinstance(gold, list) and len(gold) > 0:
            gold_nonempty.append(inst)
        elif isinstance(gold, dict) and len(gold) > 0:
            gold_nonempty.append(inst)
    n_gold_filtered = len(gold_nonempty)
    print(f"  Gold-filtered: {n_gold_filtered} (removed {n_total - n_gold_filtered} empty-gold)")

    # === 2. Degeneracy (Constant F1) ===
    print("\n--- 2. Degeneracy (CF1 gold-filtered) ---")
    constant_f1_count = 0
    greedy_f1_list = []
    oracle_f1_list = []
    lp_sel_f1_list = []
    within_rhos = []
    lp_ranges = []

    for inst in gold_nonempty:
        samples = inst.get("samples", [])
        if len(samples) < N_SAMPLES:
            continue

        gold_raw = inst.get("gold_entities", inst.get("gold", []))
        gold = gold_raw.get("entities", []) if isinstance(gold_raw, dict) else gold_raw

        f1_scores = []
        lp_scores = []
        for s in samples[:N_SAMPLES]:
            pred = s.get("entities", [])
            f1 = entity_strict_f1(pred, gold)
            f1_scores.append(f1)
            lp = s.get("mean_logprob")
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            lp_scores.append(lp)

        if len(set(f1_scores)) == 1:
            constant_f1_count += 1

        greedy_f1_list.append(f1_scores[0])
        oracle_f1_list.append(max(f1_scores))

        best_lp_idx = int(np.argmax(lp_scores))
        lp_sel_f1_list.append(f1_scores[best_lp_idx])

        lp_range = max(lp_scores) - min(lp_scores)
        lp_ranges.append(lp_range)

        if len(set(f1_scores)) >= 2 and len(set(lp_scores)) >= 2:
            rho, _ = safe_spearmanr(lp_scores, f1_scores)
            if not np.isnan(rho):
                within_rhos.append(rho)

    degeneracy_rate = 100.0 * constant_f1_count / n_gold_filtered if n_gold_filtered > 0 else 0.0
    print(f"  Constant F1 instances: {constant_f1_count}/{n_gold_filtered} = {degeneracy_rate:.2f}%")

    # === 3. Basic metrics ===
    print("\n--- 3. Basic Metrics ---")
    greedy_macro_f1 = float(np.mean(greedy_f1_list)) if greedy_f1_list else 0.0
    oracle_macro_f1 = float(np.mean(oracle_f1_list)) if oracle_f1_list else 0.0
    headroom_pp = (oracle_macro_f1 - greedy_macro_f1) * 100
    lp_sel_macro_f1 = float(np.mean(lp_sel_f1_list)) if lp_sel_f1_list else 0.0
    lp_sel_delta_pp = (lp_sel_macro_f1 - greedy_macro_f1) * 100

    print(f"  Greedy F1:  {greedy_macro_f1:.4f}")
    print(f"  Oracle F1:  {oracle_macro_f1:.4f}")
    print(f"  Headroom:   {headroom_pp:.2f} pp")
    print(f"  LP sel F1:  {lp_sel_macro_f1:.4f} ({lp_sel_delta_pp:+.2f} pp)")

    # === 4. QE Signals ===
    print("\n--- 4. QE Signals (global) ---")
    all_instance_f1 = []
    all_signals = {"LP": [], "SJ": [], "FK": [], "EM": [], "VC": []}

    for inst in gold_nonempty:
        samples = inst.get("samples", [])
        if len(samples) < N_SAMPLES:
            continue
        gold_raw = inst.get("gold_entities", inst.get("gold", []))
        gold = gold_raw.get("entities", []) if isinstance(gold_raw, dict) else gold_raw
        samps = samples[:N_SAMPLES]

        signals, _ = compute_signals(samps)

        for s_idx, s in enumerate(samps):
            pred = s.get("entities", [])
            f1 = entity_strict_f1(pred, gold)
            all_instance_f1.append(f1)
            for sig_name in all_signals:
                all_signals[sig_name].append(signals[sig_name][s_idx])

    median_f1 = float(np.median(all_instance_f1)) if all_instance_f1 else 0.0
    binary_labels = [1 if f >= median_f1 else 0 for f in all_instance_f1]

    qe_results = {}
    for sig_name in ["LP", "SJ", "FK", "EM", "VC"]:
        scores = all_signals[sig_name]
        rho, p = safe_spearmanr(scores, all_instance_f1)
        auroc = safe_auroc(binary_labels, scores)

        sel_f1s = []
        for i in range(0, len(scores), N_SAMPLES):
            chunk_scores = scores[i:i+N_SAMPLES]
            chunk_f1s = all_instance_f1[i:i+N_SAMPLES]
            if chunk_scores:
                best_idx = int(np.argmax(chunk_scores))
                sel_f1s.append(chunk_f1s[best_idx])
        sel_f1 = float(np.mean(sel_f1s)) if sel_f1s else 0.0
        sel_delta = (sel_f1 - greedy_macro_f1) * 100

        qe_results[sig_name] = {
            "auroc": round(auroc, 4) if not np.isnan(auroc) else None,
            "spearman_global": round(rho, 4) if not np.isnan(rho) else None,
            "spearman_global_p": round(p, 10) if not np.isnan(p) else None,
            "selection_f1": round(sel_f1, 4),
            "selection_delta_pp": round(sel_delta, 2),
        }
        print(f"  {sig_name}: AUROC={auroc:.4f}, rho={rho:.4f}, sel_delta={sel_delta:+.2f}pp")

    # === 5. Within-instance rho ===
    print("\n--- 5. Within-Instance rho(LP, F1) ---")
    within_rho_arr = np.array(within_rhos) if within_rhos else np.array([])
    lp_range_arr = np.array(lp_ranges) if lp_ranges else np.array([])
    valid_pct = 100.0 * len(within_rhos) / n_gold_filtered if n_gold_filtered > 0 else 0.0

    if len(within_rhos) > 0:
        print(f"  Mean:   {np.mean(within_rho_arr):.4f}")
        print(f"  Median: {np.median(within_rho_arr):.4f}")
        print(f"  Std:    {np.std(within_rho_arr):.4f}")
        print(f"  Valid:  {len(within_rhos)}/{n_gold_filtered} ({valid_pct:.1f}%)")
    else:
        print("  No valid within-instance rho computed")

    print(f"\n  LP range mean:   {np.mean(lp_range_arr):.6f}")
    print(f"  LP range median: {np.median(lp_range_arr):.6f}")

    # === 6. Comparison Table ===
    print("\n--- 6. Comparison Table ---")
    hdr = f"  {'Metric':<25} | {'5-epoch':>18} | {'3-epoch':>18} | {'10-epoch':>18} | {'vs 5ep':>10} | {'vs 3ep':>10}"
    print(hdr)
    print(f"  {'-'*25}-+-{'-'*18}-+-{'-'*18}-+-{'-'*18}-+-{'-'*10}-+-{'-'*10}")

    rows = [
        ("Degeneracy (CF1) %",
         f"{ref_5epoch['degeneracy_cf1_pct']:.1f}%",
         f"{ref_3epoch['degeneracy_cf1_pct']:.1f}%",
         f"{degeneracy_rate:.1f}%",
         f"{degeneracy_rate - ref_5epoch['degeneracy_cf1_pct']:+.1f}pp",
         f"{degeneracy_rate - ref_3epoch['degeneracy_cf1_pct']:+.1f}pp"),
        ("Greedy F1",
         "N/A",
         f"{ref_3epoch['greedy_f1']:.4f}",
         f"{greedy_macro_f1:.4f}",
         "",
         f"{(greedy_macro_f1 - ref_3epoch['greedy_f1'])*100:+.2f}pp"),
        ("Oracle F1",
         "N/A",
         f"{ref_3epoch['oracle_f1']:.4f}",
         f"{oracle_macro_f1:.4f}",
         "",
         f"{(oracle_macro_f1 - ref_3epoch['oracle_f1'])*100:+.2f}pp"),
        ("Headroom (pp)",
         "N/A",
         f"{(ref_3epoch['oracle_f1'] - ref_3epoch['greedy_f1'])*100:.2f}",
         f"{headroom_pp:.2f}",
         "",
         ""),
        ("LP sel delta (pp)",
         f"{ref_5epoch['lp_sel_delta_pp']:+.2f}",
         f"{ref_3epoch['lp_sel_delta_pp']:+.2f}",
         f"{lp_sel_delta_pp:+.2f}",
         f"{lp_sel_delta_pp - ref_5epoch['lp_sel_delta_pp']:+.2f}",
         f"{lp_sel_delta_pp - ref_3epoch['lp_sel_delta_pp']:+.2f}"),
        ("Within-inst med rho",
         f"{ref_5epoch['within_instance_median_rho']:.4f}",
         f"{ref_3epoch['within_instance_median_rho']:.4f}",
         f"{np.median(within_rho_arr):.4f}" if len(within_rhos) > 0 else "N/A",
         "",
         ""),
        ("LP range mean",
         "N/A",
         f"{ref_3epoch['lp_range_mean']:.6f}",
         f"{np.mean(lp_range_arr):.6f}",
         "",
         ""),
    ]

    for label, v5, v3, v10, d5, d3 in rows:
        print(f"  {label:<25} | {v5:>18} | {v3:>18} | {v10:>18} | {d5:>10} | {d3:>10}")

    # === 7. Conclusion ===
    print("\n--- 7. Conclusion ---")
    if degeneracy_rate > ref_5epoch["degeneracy_cf1_pct"]:
        conclusion = "CONFIRMED"
        msg = (f"10-epoch degeneracy ({degeneracy_rate:.1f}%) > 5-epoch ({ref_5epoch['degeneracy_cf1_pct']:.1f}%) "
               f"> 3-epoch ({ref_3epoch['degeneracy_cf1_pct']:.1f}%). "
               f"Epoch-degeneracy monotonic relationship confirmed for SciERC: more epochs produce higher degeneracy.")
    elif degeneracy_rate > ref_3epoch["degeneracy_cf1_pct"]:
        conclusion = "PARTIAL"
        msg = (f"10-epoch degeneracy ({degeneracy_rate:.1f}%) > 3-epoch ({ref_3epoch['degeneracy_cf1_pct']:.1f}%) "
               f"but <= 5-epoch ({ref_5epoch['degeneracy_cf1_pct']:.1f}%). Monotonicity not fully confirmed.")
    else:
        conclusion = "NEGATIVE"
        msg = (f"10-epoch degeneracy ({degeneracy_rate:.1f}%) <= 3-epoch ({ref_3epoch['degeneracy_cf1_pct']:.1f}%). "
               f"No epoch-degeneracy trend. Unexpected result.")

    print(f"  Verdict: {conclusion}")
    print(f"  {msg}")

    # === Save JSON ===
    results = {
        "experiment": "exp_029b",
        "description": "SciERC 10-epoch LoRA degeneracy test",
        "n_total": n_total,
        "n_gold_filtered": n_gold_filtered,
        "n_samples": N_SAMPLES,
        "degeneracy": {
            "definition": "Constant F1 gold-filtered",
            "constant_f1_count": constant_f1_count,
            "gold_filtered_total": n_gold_filtered,
            "rate_pct": round(degeneracy_rate, 4),
        },
        "basic": {
            "greedy_macro_f1": round(greedy_macro_f1, 4),
            "oracle_macro_f1": round(oracle_macro_f1, 4),
            "headroom_pp": round(headroom_pp, 4),
        },
        "lp_selection": {
            "f1": round(lp_sel_macro_f1, 4),
            "delta_pp": round(lp_sel_delta_pp, 4),
        },
        "qe_signals": qe_results,
        "within_instance_rho": {
            "mean": round(float(np.mean(within_rho_arr)), 4) if len(within_rhos) > 0 else None,
            "median": round(float(np.median(within_rho_arr)), 4) if len(within_rhos) > 0 else None,
            "std": round(float(np.std(within_rho_arr)), 4) if len(within_rhos) > 0 else None,
            "valid_count": len(within_rhos),
            "valid_pct": round(valid_pct, 2),
        },
        "lp_range": {
            "mean": round(float(np.mean(lp_range_arr)), 6),
            "std": round(float(np.std(lp_range_arr)), 6),
            "median": round(float(np.median(lp_range_arr)), 6),
        },
        "comparison_5epoch": {
            "source": "dynamic from exp_029a comparison_report_fixed.json",
            "baseline_ref": ref_5epoch,
            "degeneracy_delta_pp": round(degeneracy_rate - ref_5epoch["degeneracy_cf1_pct"], 4),
            "lp_sel_delta_delta": round(lp_sel_delta_pp - ref_5epoch["lp_sel_delta_pp"], 4),
        },
        "comparison_3epoch": {
            "source": BASELINE_3EPOCH_PATH,
            "baseline_ref": ref_3epoch,
            "degeneracy_delta_pp": round(degeneracy_rate - ref_3epoch["degeneracy_cf1_pct"], 4),
            "lp_sel_delta_delta": round(lp_sel_delta_pp - ref_3epoch["lp_sel_delta_pp"], 4),
        },
        "conclusion": {
            "verdict": conclusion,
            "message": msg,
        },
    }

    output_path = os.path.join(OUTPUT_DIR, "analysis_results.json")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
