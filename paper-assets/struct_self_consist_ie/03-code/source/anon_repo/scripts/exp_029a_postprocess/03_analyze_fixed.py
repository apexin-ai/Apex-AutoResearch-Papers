#!/usr/bin/env python3
"""exp_029a analysis: SciERC 3-epoch vs 5-epoch degeneracy comparison.

Fixed version: computes baseline from exp-012 raw data instead of
hardcoding values copied from Few-NERD (exp_028).

Computes:
1. Constant F1 gold-filtered degeneracy rate
2. LP selection F1 (best-of-N by logprob)
3. All 5 signals QE metrics (SJ, FK, VC, EM, LP)
4. Within-instance rho(LP, F1)
5. LP range statistics
6. Comparison table vs exp-012 (SciERC 5-epoch baseline, computed from raw data)
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
INPUT_PATH = f"{BASE}/output/exp_029a_scierc_3epoch/samples.jsonl"
OUTPUT_DIR = f"{BASE}/output/exp_029a_scierc_3epoch"
BASELINE_PATH = f"{BASE}/output/exp_012_rerun_1024/samples.jsonl"
SUBTASK = "ner"
N_SAMPLES = 8


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


def compute_baseline_from_exp012(path):
    """Compute baseline metrics from exp-012 (SciERC 5-epoch) raw inference data."""
    print(f"Computing baseline from exp-012: {path}")
    instances = load_data(path)

    instances_gold = [inst for inst in instances
                      if len(inst.get("gold", {}).get("entities", [])) > 0]
    n_gold_filtered = len(instances_gold)

    constant_f1_count = 0
    greedy_f1s = np.zeros(n_gold_filtered)
    within_rhos = []

    for i, inst in enumerate(instances_gold):
        gold = inst["gold"]
        gold_entities = gold.get("entities", [])
        samples = inst["samples"][:N_SAMPLES]

        f1s = [entity_strict_f1(s.get("entities", []), gold_entities) for s in samples]

        if "greedy" in inst:
            greedy_f1s[i] = entity_strict_f1(inst["greedy"].get("entities", []), gold_entities)
        else:
            greedy_f1s[i] = f1s[0]

        if len(set(round(f, 10) for f in f1s)) == 1:
            constant_f1_count += 1

        lps = []
        inst_logprobs = inst.get("logprobs", [])
        for j, s in enumerate(samples):
            lp = s.get("mean_logprob")
            if lp is None and j < len(inst_logprobs):
                lp = inst_logprobs[j]
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            lps.append(lp)

        if len(set(round(f, 10) for f in f1s)) >= 2 and len(set(round(l, 10) for l in lps)) >= 2:
            r, _ = safe_spearmanr(lps, f1s)
            if not np.isnan(r):
                within_rhos.append(r)

    degeneracy_rate = 100.0 * constant_f1_count / n_gold_filtered
    greedy_macro_f1 = float(np.mean(greedy_f1s))

    # LP selection
    lp_sel_f1s = np.zeros(n_gold_filtered)
    for i, inst in enumerate(instances_gold):
        gold = inst["gold"]
        gold_entities = gold.get("entities", [])
        samples = inst["samples"][:N_SAMPLES]
        inst_logprobs = inst.get("logprobs", [])

        best_lp = -float('inf')
        best_sample = samples[0]
        for j, s in enumerate(samples):
            lp = s.get("mean_logprob")
            if lp is None and j < len(inst_logprobs):
                lp = inst_logprobs[j]
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            if lp is not None and lp > best_lp:
                best_lp = lp
                best_sample = s
        lp_sel_f1s[i] = entity_strict_f1(best_sample.get("entities", []), gold_entities)

    lp_sel_macro_f1 = float(np.mean(lp_sel_f1s))
    lp_sel_delta_pp = (lp_sel_macro_f1 - greedy_macro_f1) * 100

    within_rho_arr = np.array(within_rhos)
    baseline = {
        "degeneracy_cf1_pct": round(degeneracy_rate, 4),
        "lp_sel_delta_pp": round(lp_sel_delta_pp, 4),
        "within_instance_median_rho": round(float(np.median(within_rho_arr)), 4) if len(within_rhos) > 0 else None,
        "within_instance_mean_rho": round(float(np.mean(within_rho_arr)), 4) if len(within_rhos) > 0 else None,
        "greedy_macro_f1": round(greedy_macro_f1, 4),
        "n_gold_filtered": n_gold_filtered,
        "within_rho_valid_count": len(within_rhos),
    }

    print(f"  Baseline degeneracy: {baseline['degeneracy_cf1_pct']:.1f}%")
    print(f"  Baseline LP sel delta: {baseline['lp_sel_delta_pp']:+.2f}pp")
    print(f"  Baseline within-inst median rho: {baseline['within_instance_median_rho']}")
    print(f"  Baseline within-inst mean rho: {baseline['within_instance_mean_rho']}")
    print(f"  Baseline greedy F1: {baseline['greedy_macro_f1']:.4f}")
    return baseline


def main():
    print("=" * 60)
    print("exp_029a Analysis: SciERC 3-epoch vs 5-epoch (FIXED)")
    print("  Baseline computed from exp-012 raw data")
    print("=" * 60)

    # Compute baseline from exp-012 raw data
    BASELINE_REF = compute_baseline_from_exp012(BASELINE_PATH)

    instances = load_data(INPUT_PATH)
    n_total = len(instances)
    print(f"\nTotal instances: {n_total}")

    instances_gold = [inst for inst in instances
                      if len(inst.get("gold", {}).get("entities", [])) > 0]
    n_gold_filtered = len(instances_gold)
    print(f"Gold-filtered (non-empty gold entities): {n_gold_filtered}")

    # === 1. Degeneracy ===
    print("\n--- 1. Degeneracy (Constant F1, gold-filtered) ---")
    constant_f1_count = 0
    greedy_f1s = np.zeros(n_gold_filtered)
    oracle_f1s = np.zeros(n_gold_filtered)
    all_sample_f1s = []

    for i, inst in enumerate(instances_gold):
        gold = inst["gold"]
        gold_entities = gold.get("entities", [])
        samples = inst["samples"][:N_SAMPLES]

        f1s = [entity_strict_f1(s.get("entities", []), gold_entities) for s in samples]
        all_sample_f1s.append(f1s)

        if "greedy" in inst:
            greedy_f1s[i] = entity_strict_f1(inst["greedy"].get("entities", []), gold_entities)
        else:
            greedy_f1s[i] = f1s[0]

        oracle_f1s[i] = max(f1s)

        if len(set(round(f, 10) for f in f1s)) == 1:
            constant_f1_count += 1

    degeneracy_rate = 100.0 * constant_f1_count / n_gold_filtered
    greedy_macro_f1 = float(np.mean(greedy_f1s))
    oracle_macro_f1 = float(np.mean(oracle_f1s))
    headroom_pp = (oracle_macro_f1 - greedy_macro_f1) * 100

    print(f"  Constant F1 instances: {constant_f1_count} / {n_gold_filtered}")
    print(f"  Degeneracy rate: {degeneracy_rate:.1f}%")
    print(f"  Greedy F1: {greedy_macro_f1:.4f}")
    print(f"  Oracle F1: {oracle_macro_f1:.4f}")
    print(f"  Headroom: {headroom_pp:.2f}pp")

    # === 2. LP Selection ===
    print("\n--- 2. LP Selection F1 ---")
    lp_sel_f1s = np.zeros(n_gold_filtered)
    for i, inst in enumerate(instances_gold):
        gold = inst["gold"]
        gold_entities = gold.get("entities", [])
        samples = inst["samples"][:N_SAMPLES]
        inst_logprobs = inst.get("logprobs", [])

        best_lp = -float('inf')
        best_sample = samples[0]
        for j, s in enumerate(samples):
            lp = s.get("mean_logprob")
            if lp is None and j < len(inst_logprobs):
                lp = inst_logprobs[j]
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            if lp is not None and lp > best_lp:
                best_lp = lp
                best_sample = s

        lp_sel_f1s[i] = entity_strict_f1(best_sample.get("entities", []), gold_entities)

    lp_sel_macro_f1 = float(np.mean(lp_sel_f1s))
    lp_sel_delta_pp = (lp_sel_macro_f1 - greedy_macro_f1) * 100

    print(f"  LP selection F1: {lp_sel_macro_f1:.4f}")
    print(f"  LP selection delta: {lp_sel_delta_pp:+.2f}pp")

    # === 3. QE Signals ===
    print("\n--- 3. QE Signals (AUROC, global rho, selection F1, delta) ---")
    all_signal_scores = {sig: [] for sig in ["LP", "SJ", "FK", "EM", "VC"]}
    all_f1_scores = []

    for i, inst in enumerate(instances_gold):
        gold = inst["gold"]
        gold_entities = gold.get("entities", [])
        samples = inst["samples"][:N_SAMPLES]

        f1s = [entity_strict_f1(s.get("entities", []), gold_entities) for s in samples]
        signals, _ = compute_signals(samples)

        for sig_name in ["LP", "SJ", "FK", "EM", "VC"]:
            for j in range(len(samples)):
                all_signal_scores[sig_name].append(signals[sig_name][j])
                if sig_name == "LP":
                    all_f1_scores.append(f1s[j])

    qe_results = {}
    for sig_name in ["LP", "SJ", "FK", "EM", "VC"]:
        scores_arr = np.array(all_signal_scores[sig_name])
        f1_arr = np.array(all_f1_scores)

        rho, p = safe_spearmanr(scores_arr, f1_arr)

        median_f1 = float(np.median(f1_arr))
        binary_labels = (f1_arr >= median_f1).astype(int)
        auroc = safe_auroc(binary_labels, scores_arr)

        sel_f1s = np.zeros(n_gold_filtered)
        for ii, inst in enumerate(instances_gold):
            gold = inst["gold"]
            gold_entities = gold.get("entities", [])
            samples = inst["samples"][:N_SAMPLES]
            sigs_inst, _ = compute_signals(samples)
            best_idx = int(np.argmax(sigs_inst[sig_name]))
            sel_f1s[ii] = entity_strict_f1(samples[best_idx].get("entities", []), gold_entities)

        sel_macro_f1 = float(np.mean(sel_f1s))
        sel_delta_pp = (sel_macro_f1 - greedy_macro_f1) * 100

        qe_results[sig_name] = {
            "auroc": round(auroc, 4) if not np.isnan(auroc) else None,
            "spearman_global": round(rho, 4) if not np.isnan(rho) else None,
            "selection_f1": round(sel_macro_f1, 4),
            "selection_delta_pp": round(sel_delta_pp, 2),
        }

        print(f"  {sig_name}: AUROC={qe_results[sig_name]['auroc']}, rho={qe_results[sig_name]['spearman_global']}, "
              f"sel_F1={sel_macro_f1:.4f}, delta={sel_delta_pp:+.2f}pp")

    # === 4. Within-instance rho(LP, F1) ===
    print("\n--- 4. Within-instance LP-F1 correlation ---")
    within_rhos = []
    for i, inst in enumerate(instances_gold):
        gold = inst["gold"]
        gold_entities = gold.get("entities", [])
        samples = inst["samples"][:N_SAMPLES]

        f1s = [entity_strict_f1(s.get("entities", []), gold_entities) for s in samples]
        lps = []
        inst_logprobs = inst.get("logprobs", [])
        for j, s in enumerate(samples):
            lp = s.get("mean_logprob")
            if lp is None and j < len(inst_logprobs):
                lp = inst_logprobs[j]
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            lps.append(lp)

        if len(set(round(f, 10) for f in f1s)) >= 2 and len(set(round(l, 10) for l in lps)) >= 2:
            r, _ = safe_spearmanr(lps, f1s)
            if not np.isnan(r):
                within_rhos.append(r)

    within_rho_arr = np.array(within_rhos)
    valid_pct = 100.0 * len(within_rhos) / n_gold_filtered if n_gold_filtered > 0 else 0

    print(f"  Valid instances: {len(within_rhos)} / {n_gold_filtered} ({valid_pct:.1f}%)")
    if len(within_rhos) > 0:
        print(f"  Mean rho: {np.mean(within_rho_arr):.4f}")
        print(f"  Median rho: {np.median(within_rho_arr):.4f}")
        print(f"  Std rho: {np.std(within_rho_arr):.4f}")

    # === 5. LP Range ===
    print("\n--- 5. LP Range Statistics ---")
    lp_ranges = []
    for inst in instances_gold:
        samples = inst["samples"][:N_SAMPLES]
        inst_logprobs = inst.get("logprobs", [])
        lps = []
        for j, s in enumerate(samples):
            lp = s.get("mean_logprob")
            if lp is None and j < len(inst_logprobs):
                lp = inst_logprobs[j]
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            lps.append(lp)
        lp_ranges.append(max(lps) - min(lps))

    lp_range_arr = np.array(lp_ranges)
    print(f"  Mean LP range: {np.mean(lp_range_arr):.6f}")
    print(f"  Std LP range: {np.std(lp_range_arr):.6f}")
    print(f"  Median LP range: {np.median(lp_range_arr):.6f}")

    # === 6. Comparison Table ===
    print("\n--- 6. Comparison: exp-012 (5-epoch) vs exp_029a (3-epoch) ---")
    print(f"  {'Metric':<25} | {'5-epoch (exp-012)':>18} | {'3-epoch (029a)':>18} | {'Delta':>8}")
    print(f"  {'-'*25}-+-{'-'*18}-+-{'-'*18}-+-{'-'*8}")

    within_median_029a = f"{np.median(within_rho_arr):.4f}" if len(within_rhos) > 0 else "N/A"
    within_median_baseline = f"{BASELINE_REF['within_instance_median_rho']:.4f}" if BASELINE_REF['within_instance_median_rho'] is not None else "N/A"

    rows = [
        ("Degeneracy (CF1) %", f"{BASELINE_REF['degeneracy_cf1_pct']:.1f}%", f"{degeneracy_rate:.1f}%",
         f"{degeneracy_rate - BASELINE_REF['degeneracy_cf1_pct']:+.1f}pp"),
        ("Greedy F1", f"{BASELINE_REF['greedy_macro_f1']:.4f}", f"{greedy_macro_f1:.4f}",
         f"{(greedy_macro_f1 - BASELINE_REF['greedy_macro_f1'])*100:+.2f}pp"),
        ("Oracle F1", "N/A", f"{oracle_macro_f1:.4f}", ""),
        ("Headroom (pp)", "N/A", f"{headroom_pp:.2f}", ""),
        ("LP sel delta (pp)", f"{BASELINE_REF['lp_sel_delta_pp']:+.2f}", f"{lp_sel_delta_pp:+.2f}",
         f"{lp_sel_delta_pp - BASELINE_REF['lp_sel_delta_pp']:+.2f}"),
        ("Within-inst median rho", within_median_baseline, within_median_029a, ""),
        ("Within-inst mean rho",
         f"{BASELINE_REF['within_instance_mean_rho']:.4f}" if BASELINE_REF['within_instance_mean_rho'] is not None else "N/A",
         f"{np.mean(within_rho_arr):.4f}" if len(within_rhos) > 0 else "N/A", ""),
        ("LP range mean", "N/A", f"{np.mean(lp_range_arr):.6f}", ""),
    ]

    for label, ref, exp029a, delta in rows:
        print(f"  {label:<25} | {ref:>18} | {exp029a:>18} | {delta:>8}")

    # === 7. Conclusion ===
    print("\n--- 7. Conclusion ---")
    if degeneracy_rate < BASELINE_REF["degeneracy_cf1_pct"]:
        conclusion = "SUCCESS"
        msg = (f"3-epoch degeneracy ({degeneracy_rate:.1f}%) < 5-epoch ({BASELINE_REF['degeneracy_cf1_pct']:.1f}%). "
               f"Confirms epoch-degeneracy relationship holds for SciERC: fewer epochs produce lower degeneracy.")
    elif degeneracy_rate == BASELINE_REF["degeneracy_cf1_pct"]:
        conclusion = "BORDERLINE"
        msg = f"3-epoch degeneracy ({degeneracy_rate:.1f}%) == 5-epoch. No clear effect."
    else:
        conclusion = "NEGATIVE"
        msg = (f"3-epoch degeneracy ({degeneracy_rate:.1f}%) >= 5-epoch ({BASELINE_REF['degeneracy_cf1_pct']:.1f}%). "
               f"Epoch-degeneracy hypothesis not confirmed for SciERC.")

    print(f"  Verdict: {conclusion}")
    print(f"  {msg}")

    # === Save JSON ===
    results = {
        "experiment": "exp_029a",
        "description": "SciERC 3-epoch LoRA degeneracy test (FIXED: baseline from exp-012 raw data)",
        "baseline_source": "exp-012 (SciERC 5-epoch, rank=32) computed from raw inference data",
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
        "comparison_baseline": {
            "baseline_ref": BASELINE_REF,
            "degeneracy_delta_pp": round(degeneracy_rate - BASELINE_REF["degeneracy_cf1_pct"], 4),
            "lp_sel_delta_delta": round(lp_sel_delta_pp - BASELINE_REF["lp_sel_delta_pp"], 4),
        },
        "conclusion": {
            "verdict": conclusion,
            "message": msg,
        },
    }

    output_path = os.path.join(OUTPUT_DIR, "comparison_report_fixed.json")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
