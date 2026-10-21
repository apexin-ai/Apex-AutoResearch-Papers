#!/usr/bin/env python3
"""exp_028 full signal analysis: 5-epoch vs 3-epoch convergence comparison.

Computes:
1. Constant F1 gold-filtered degeneracy rate
2. LP selection F1 (best-of-N by logprob)
3. All 5 signals QE metrics (SJ, FK, VC, EM, LP)
4. Within-instance rho(LP, F1)
5. LP range statistics
6. Comparison table vs exp-021 (3-epoch)
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
INPUT_PATH = f"{BASE}/output/exp_028_fewnerd_5epoch/samples.jsonl"
OUTPUT_DIR = f"{BASE}/output/exp_028_fewnerd_5epoch"
SUBTASK = "ner"
N_SAMPLES = 8

# exp-021 reference (3-epoch, N=8, 5000-instance subset, Constant F1 gold-filtered)
_EXP021_REF_PATH = f"{BASE}/output/exp_027_fewnerd_n16/paired_n8_baseline.json"
_EXP021_FALLBACK = {
    "degeneracy_cf1_pct": 12.0,
    "greedy_f1": 0.748,
    "lp_sel_f1": 0.7616,
    "lp_sel_delta_pp": 1.36,
}
try:
    with open(_EXP021_REF_PATH) as _f:
        _ref_data = json.load(_f)["n8"]
    EXP021_REF = {
        "degeneracy_cf1_pct": _ref_data["degeneracy_rate_pct"],
        "greedy_f1": _ref_data["greedy_f1"],
        "lp_sel_f1": _ref_data["lp_sel_f1"],
        "lp_sel_delta_pp": _ref_data["lp_delta_pp"],
    }
except (FileNotFoundError, KeyError, json.JSONDecodeError) as _e:
    print(f"WARNING: could not load {_EXP021_REF_PATH} ({_e}), using hardcoded fallback")
    EXP021_REF = _EXP021_FALLBACK


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


def entity_strict_f1(pred_entities, gold_entities):
    """Strict entity F1: match on (start, end, type)."""
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return f1


def get_sample_lp(sample, inst_logprobs, idx):
    """Get mean logprob for a sample."""
    if "mean_logprob" in sample:
        return sample["mean_logprob"]
    if inst_logprobs is not None and idx < len(inst_logprobs):
        return inst_logprobs[idx]
    if "cumulative_logprob" in sample:
        return sample["cumulative_logprob"] / max(sample.get("n_tokens", 1), 1)
    return None


def compute_signals(samples):
    """Compute all 5 signals for N samples."""
    n = len(samples)

    # LP: mean log-probability
    lp_scores = []
    for s in samples:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lp_scores.append(lp)

    # Surface key sets for FK, EM, VC
    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]

    # SJ: pairwise soft Jaccard, per-sample average
    sj_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            s = _ner_soft_jaccard_pair(samples[i].get("entities", []), samples[j].get("entities", []))
            sj_matrix[i][j] = s
            sj_matrix[j][i] = s
    np.fill_diagonal(sj_matrix, 1.0)
    sj_scores = [float(np.mean([sj_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]

    # FK: pairwise surface Jaccard (used as FK proxy in this codebase)
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

    # VC: voting confidence
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

    # EM: exact match count
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
    print("=" * 70)
    print("EXP_028: 5-epoch Few-NERD Convergence Analysis")
    print("=" * 70)

    # Load data
    print("\nLoading data...")
    data = load_data(INPUT_PATH)
    n_total = len(data)
    print(f"  Total instances: {n_total}")

    # Filter: gold entities non-empty (for degeneracy and main analysis)
    instances_gold = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    n_gold_filtered = len(instances_gold)
    print(f"  Gold-filtered instances: {n_gold_filtered}")

    # === 1. Constant F1 gold-filtered degeneracy ===
    print("\n--- 1. Degeneracy (Constant F1, gold-filtered) ---")
    constant_f1_count = 0
    greedy_f1s = np.zeros(n_gold_filtered)
    oracle_f1s = np.zeros(n_gold_filtered)
    all_sample_f1s = []

    for i, inst in enumerate(instances_gold):
        gold = inst["gold"]
        gold_entities = gold.get("entities", [])
        samples = inst["samples"][:N_SAMPLES]

        # Per-sample F1
        f1s = [entity_strict_f1(s.get("entities", []), gold_entities) for s in samples]
        all_sample_f1s.append(f1s)

        # Greedy F1
        if "greedy" in inst:
            greedy_f1s[i] = entity_strict_f1(inst["greedy"].get("entities", []), gold_entities)
        else:
            greedy_f1s[i] = f1s[0]

        oracle_f1s[i] = max(f1s)

        # Constant F1: all samples produce identical F1
        if len(set(round(f, 10) for f in f1s)) == 1:
            constant_f1_count += 1

    degeneracy_rate = constant_f1_count / n_gold_filtered * 100
    greedy_macro_f1 = float(greedy_f1s.mean())
    oracle_macro_f1 = float(oracle_f1s.mean())
    headroom_pp = (oracle_macro_f1 - greedy_macro_f1) * 100

    print(f"  Constant F1 degenerate: {constant_f1_count}/{n_gold_filtered} = {degeneracy_rate:.2f}%")
    print(f"  Greedy macro F1: {greedy_macro_f1:.4f}")
    print(f"  Oracle macro F1: {oracle_macro_f1:.4f}")
    print(f"  Headroom: {headroom_pp:.2f}pp")

    # === 2. LP selection F1 ===
    print("\n--- 2. LP Selection F1 (best-of-N by logprob) ---")
    lp_sel_f1s = np.zeros(n_gold_filtered)

    for i, inst in enumerate(instances_gold):
        samples = inst["samples"][:N_SAMPLES]
        inst_logprobs = inst.get("logprobs", None)
        lps = []
        for idx, s in enumerate(samples):
            lp = get_sample_lp(s, inst_logprobs, idx)
            lps.append(lp if lp is not None else -999)

        best_idx = int(np.argmax(lps))
        lp_sel_f1s[i] = all_sample_f1s[i][best_idx]

    lp_sel_macro_f1 = float(lp_sel_f1s.mean())
    lp_sel_delta_pp = (lp_sel_macro_f1 - greedy_macro_f1) * 100
    print(f"  LP selection F1: {lp_sel_macro_f1:.4f}")
    print(f"  LP selection delta: {lp_sel_delta_pp:+.2f}pp")

    # === 3. All 5 signals QE metrics ===
    print("\n--- 3. All 5 Signals: Spearman rho & AUROC ---")
    SIGNALS = ["LP", "SJ", "FK", "EM", "VC"]
    signal_selected_f1s = {sig: np.zeros(n_gold_filtered) for sig in SIGNALS}
    instance_max_signal = {sig: np.zeros(n_gold_filtered) for sig in SIGNALS}
    all_sample_scores = {sig: [] for sig in SIGNALS}
    all_oracle_labels = []

    for i, inst in enumerate(instances_gold):
        samples = inst["samples"][:N_SAMPLES]
        f1s = all_sample_f1s[i]
        oracle_idx = int(np.argmax(f1s))

        signals, _ = compute_signals(samples)

        for sig in SIGNALS:
            best_idx = int(np.argmax(signals[sig]))
            signal_selected_f1s[sig][i] = f1s[best_idx]
            instance_max_signal[sig][i] = float(np.max(signals[sig]))
            all_sample_scores[sig].extend(signals[sig])

        oracle_labels_i = [1 if k == oracle_idx else 0 for k in range(len(samples))]
        all_oracle_labels.extend(oracle_labels_i)

        if (i + 1) % 500 == 0:
            print(f"  Processed {i+1}/{n_gold_filtered}")

    qe_results = {}
    print(f"\n  {'Signal':<6} | {'AUROC':>7} | {'rho (global)':>12} | {'Sel F1':>7} | {'Delta':>8}")
    print(f"  {'-'*6}-+-{'-'*7}-+-{'-'*12}-+-{'-'*7}-+-{'-'*8}")

    for sig in SIGNALS:
        auroc = safe_auroc(all_oracle_labels, all_sample_scores[sig])
        rho_global, p_global = safe_spearmanr(instance_max_signal[sig], greedy_f1s)
        sel_f1 = float(signal_selected_f1s[sig].mean())
        delta = (sel_f1 - greedy_macro_f1) * 100

        qe_results[sig] = {
            "auroc": round(auroc, 4) if not np.isnan(auroc) else None,
            "spearman_global": round(rho_global, 4) if not np.isnan(rho_global) else None,
            "spearman_global_p": p_global,
            "selection_f1": round(sel_f1, 4),
            "selection_delta_pp": round(delta, 4),
        }

        auroc_s = f"{auroc:.4f}" if not np.isnan(auroc) else "N/A"
        rho_s = f"{rho_global:.4f}" if not np.isnan(rho_global) else "N/A"
        print(f"  {sig:<6} | {auroc_s:>7} | {rho_s:>12} | {sel_f1:.4f} | {delta:+.2f}pp")

    # === 4. Within-instance rho(LP, F1) ===
    print("\n--- 4. Within-instance rho(LP, F1) ---")
    within_rhos = []

    for i, inst in enumerate(instances_gold):
        samples = inst["samples"][:N_SAMPLES]
        inst_logprobs = inst.get("logprobs", None)
        f1s = np.array(all_sample_f1s[i])

        lps = []
        for idx, s in enumerate(samples):
            lp = get_sample_lp(s, inst_logprobs, idx)
            if lp is not None:
                lps.append(lp)
            else:
                break

        if len(lps) == N_SAMPLES:
            lp_arr = np.array(lps)
            if np.std(f1s) > 0 and np.std(lp_arr) > 0:
                rho, _ = spearmanr(lp_arr, f1s)
                if np.isfinite(rho):
                    within_rhos.append(rho)

    within_rho_arr = np.array(within_rhos) if within_rhos else np.array([])
    valid_pct = len(within_rhos) / n_gold_filtered * 100 if n_gold_filtered > 0 else 0

    print(f"  Valid instances: {len(within_rhos)}/{n_gold_filtered} ({valid_pct:.1f}%)")
    if len(within_rhos) > 0:
        print(f"  Mean rho: {np.mean(within_rho_arr):.4f}")
        print(f"  Median rho: {np.median(within_rho_arr):.4f}")
        print(f"  Std: {np.std(within_rho_arr):.4f}")

    # === 5. LP range ===
    print("\n--- 5. LP Range ---")
    lp_ranges = []

    for i, inst in enumerate(instances_gold):
        samples = inst["samples"][:N_SAMPLES]
        inst_logprobs = inst.get("logprobs", None)
        lps = []
        for idx, s in enumerate(samples):
            lp = get_sample_lp(s, inst_logprobs, idx)
            if lp is not None:
                lps.append(lp)

        if len(lps) == N_SAMPLES:
            lp_ranges.append(max(lps) - min(lps))

    lp_range_arr = np.array(lp_ranges) if lp_ranges else np.array([0.0])
    print(f"  Mean LP range: {np.mean(lp_range_arr):.6f}")
    print(f"  Std LP range: {np.std(lp_range_arr):.6f}")
    print(f"  Median LP range: {np.median(lp_range_arr):.6f}")

    # === 6. Comparison table vs exp-021 ===
    print("\n--- 6. Comparison: 3-epoch (exp-021) vs 5-epoch (exp-028) ---")
    print(f"\n  {'Metric':<25} | {'3-epoch (exp-021)':>18} | {'5-epoch (exp-028)':>18} | {'Delta':>8}")
    print(f"  {'-'*25}-+-{'-'*18}-+-{'-'*18}-+-{'-'*8}")

    rows = [
        ("Degeneracy (CF1) %", f"{EXP021_REF['degeneracy_cf1_pct']:.1f}%", f"{degeneracy_rate:.1f}%",
         f"{degeneracy_rate - EXP021_REF['degeneracy_cf1_pct']:+.1f}pp"),
        ("Greedy F1", f"{EXP021_REF['greedy_f1']:.4f}", f"{greedy_macro_f1:.4f}",
         f"{(greedy_macro_f1 - EXP021_REF['greedy_f1'])*100:+.2f}pp"),
        ("LP sel F1", f"{EXP021_REF['lp_sel_f1']:.4f}", f"{lp_sel_macro_f1:.4f}",
         f"{(lp_sel_macro_f1 - EXP021_REF['lp_sel_f1'])*100:+.2f}pp"),
        ("LP sel delta (pp)", f"+{EXP021_REF['lp_sel_delta_pp']:.2f}", f"{lp_sel_delta_pp:+.2f}",
         f"{lp_sel_delta_pp - EXP021_REF['lp_sel_delta_pp']:+.2f}"),
        ("SJ rho", "N/A", f"{qe_results['SJ']['spearman_global']}" if qe_results['SJ']['spearman_global'] else "N/A", ""),
        ("LP range mean", "N/A", f"{np.mean(lp_range_arr):.6f}", ""),
    ]

    for label, ref, exp028, delta in rows:
        print(f"  {label:<25} | {ref:>18} | {exp028:>18} | {delta:>8}")

    # === 7. Conclusion judgment ===
    print("\n--- 7. Conclusion ---")
    if degeneracy_rate <= 15.0:
        conclusion = "SUCCESS"
        msg = "5-epoch degeneracy <= 15% (comparable to 3-epoch). Confirms low degeneracy is a structural property of Few-NERD, not under-convergence."
    elif degeneracy_rate > 20.0:
        conclusion = "NEGATIVE"
        msg = "5-epoch degeneracy > 20% (significantly higher than 3-epoch). Few-NERD low degeneracy may be due to under-convergence. Paper narrative needs revision."
    else:
        conclusion = "BORDERLINE"
        msg = f"5-epoch degeneracy {degeneracy_rate:.1f}% is in 15-20% borderline range. Director judgment needed."

    print(f"  Verdict: {conclusion}")
    print(f"  {msg}")

    # === Save JSON results ===
    results = {
        "experiment": "exp_028",
        "description": "5-epoch LoRA Few-NERD convergence test",
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
        "comparison_exp021": {
            "exp021_ref": EXP021_REF,
            "degeneracy_delta_pp": round(degeneracy_rate - EXP021_REF["degeneracy_cf1_pct"], 4),
            "greedy_f1_delta": round(greedy_macro_f1 - EXP021_REF["greedy_f1"], 4),
            "lp_sel_delta_delta": round(lp_sel_delta_pp - EXP021_REF["lp_sel_delta_pp"], 4),
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
