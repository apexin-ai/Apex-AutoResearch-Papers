#!/usr/bin/env python3
"""Analyze exp-021 Few-NERD inference results.

Input:  samples.jsonl (same format as SciERC: id, text, gold, samples, greedy)
Output: results.json + formatted stdout tables for paper
"""

import argparse
import json
import os
import sys
import warnings
import numpy as np
from collections import Counter, defaultdict
from scipy import stats as scipy_stats

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys
from unified_metrics import compute_entity_f1, compute_degeneracy

SUBTASK = "ner"
SIGNALS = ["LP", "SJ", "FK", "EM", "VC"]
SEED = 42

# Source: exp_012_rerun_1024/samples.jsonl, gold-filtered n=529, mean_LP, 2026-05-18
# Computed by unified_tab_fewnerd_metrics.py (same code path as Few-NERD)
SCIERC_REF = {
    "n": 529, "greedy": 0.6439, "oracle": 0.7758, "headroom": 13.19,
    "degen": 17.8, "lp_rho": 0.205, "lp_delta": 0.61,
}

# Source: exp002_conll2003/samples.jsonl, gold-filtered n=2756, mean_LP, 2026-05-18
# Computed by unified_tab_fewnerd_metrics.py (same code path as Few-NERD)
CONLL_REF = {
    "n": 2756, "greedy": 0.9079, "oracle": 0.9483, "headroom": 4.04,
    "degen": 59.1, "lp_rho": 0.302, "lp_delta": -1.05,
}


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_signals(samples):
    n = len(samples)
    lp_scores = []
    for s in samples:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lp_scores.append(lp)

    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]

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

    sj_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            s = _ner_soft_jaccard_pair(samples[i].get("entities", []), samples[j].get("entities", []))
            sj_matrix[i][j] = s
            sj_matrix[j][i] = s
    np.fill_diagonal(sj_matrix, 1.0)
    sj_scores = [float(np.mean([sj_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]

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


def safe_auroc(labels, scores):
    from sklearn.metrics import roc_auc_score
    if len(set(labels)) < 2 or len(set(scores)) < 2:
        return float('nan')
    return roc_auc_score(labels, scores)


def safe_spearmanr(x, y):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        if len(set(x)) < 2 or len(set(y)) < 2:
            return float('nan'), float('nan')
        r, p = scipy_stats.spearmanr(x, y)
        return float(r), float(p)


def main():
    parser = argparse.ArgumentParser(description="Analyze Few-NERD exp-021 inference results")
    parser.add_argument("--input_dir", default="output/exp_021_inference/",
                        help="Directory containing samples.jsonl")
    parser.add_argument("--output_dir", default=None,
                        help="Output directory (default: same as input_dir)")
    parser.add_argument("--bootstrap_b", type=int, default=5000,
                        help="Number of bootstrap iterations")
    args = parser.parse_args()

    if args.output_dir is None:
        args.output_dir = args.input_dir

    base = "/root/autodl-tmp/struct_self_consist_ie"
    input_path = os.path.join(base, args.input_dir, "samples.jsonl")
    output_path = os.path.join(base, args.output_dir, "results.json")
    os.makedirs(os.path.join(base, args.output_dir), exist_ok=True)

    data = load_data(input_path)
    instances = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    N = len(instances)
    total_raw = len(data)
    n_samples = len(instances[0]["samples"]) if instances else 0
    print(f"Loaded {total_raw} instances, {N} after filtering gold-empty, {n_samples} samples each")

    rng = np.random.RandomState(SEED)

    # First pass: compute all metrics per instance
    greedy_f1s = np.zeros(N)
    oracle_f1s = np.zeros(N)
    signal_selected_f1s = {sig: np.zeros(N) for sig in SIGNALS}
    instance_max_signal = {sig: np.zeros(N) for sig in SIGNALS}
    instance_mean_lp = np.zeros(N)
    lp_ranges = np.zeros(N)
    degen_flags = np.zeros(N, dtype=bool)
    instance_types = []

    # For AUROC: store per-sample scores and oracle labels
    all_sample_scores = {sig: [] for sig in SIGNALS}
    all_oracle_labels = []

    for i, inst in enumerate(instances):
        gold = inst["gold"]
        greedy = inst["greedy"]
        samples = inst["samples"]

        greedy_f1s[i] = compute_entity_f1(greedy.get("entities", []), gold.get("entities", []))
        sample_f1s = np.array([compute_entity_f1(s.get("entities", []), gold.get("entities", [])) for s in samples])
        oracle_f1s[i] = sample_f1s.max()
        oracle_idx = int(np.argmax(sample_f1s))

        signals, key_sets = compute_signals(samples)
        lp_ranges[i] = max(signals["LP"]) - min(signals["LP"])

        degen_flags[i] = compute_degeneracy(sample_f1s.tolist())

        for sig in SIGNALS:
            best_idx = int(np.argmax(signals[sig]))
            signal_selected_f1s[sig][i] = sample_f1s[best_idx]
            instance_max_signal[sig][i] = float(np.max(signals[sig]))
            if sig == "LP":
                instance_mean_lp[i] = float(np.mean(signals[sig]))
            all_sample_scores[sig].extend(signals[sig])

        oracle_labels_i = [1 if k == oracle_idx else 0 for k in range(len(samples))]
        all_oracle_labels.extend(oracle_labels_i)

        types_here = set(e["type"] for e in gold.get("entities", []))
        instance_types.append(types_here)

        if (i + 1) % 200 == 0:
            print(f"  Processed {i+1}/{N}")

    # === 1. Basic metrics ===
    greedy_macro = float(greedy_f1s.mean())
    oracle_macro = float(oracle_f1s.mean())
    headroom = (oracle_macro - greedy_macro) * 100
    zero_f1_rate = float(np.mean(greedy_f1s == 0)) * 100
    degeneracy_rate = float(degen_flags.mean()) * 100

    print(f"\n{'='*70}")
    print("1. BASIC METRICS")
    print(f"{'='*70}")
    print(f"  Greedy macro F1:   {greedy_macro:.4f}  (pilot ref: 0.804)")
    print(f"  Oracle macro F1:   {oracle_macro:.4f}")
    print(f"  Headroom:          {headroom:.2f}pp")
    print(f"  Zero-F1 rate:      {zero_f1_rate:.1f}%  (pilot ref: 14.2%)")
    print(f"  Degeneracy rate:   {degeneracy_rate:.1f}%")
    print(f"  LP range (median): {float(np.median(lp_ranges)):.4f}")

    # === 2. QE metrics ===
    print(f"\n{'='*70}")
    print("2. QE METRICS (AUROC [diagnostic only] & Spearman)")
    print(f"{'='*70}")

    qe_results = {}
    for sig in SIGNALS:
        auroc = safe_auroc(all_oracle_labels, all_sample_scores[sig])

        if sig == "LP":
            rho_global, p_global = safe_spearmanr(instance_mean_lp, greedy_f1s)
        else:
            rho_global, p_global = safe_spearmanr(instance_max_signal[sig], greedy_f1s)

        non_degen_mask = ~degen_flags
        if non_degen_mask.sum() > 10:
            if sig == "LP":
                rho_cond, p_cond = safe_spearmanr(
                    instance_mean_lp[non_degen_mask],
                    greedy_f1s[non_degen_mask])
            else:
                rho_cond, p_cond = safe_spearmanr(
                    instance_max_signal[sig][non_degen_mask],
                    greedy_f1s[non_degen_mask])
        else:
            rho_cond, p_cond = float('nan'), float('nan')

        qe_results[sig] = {
            "auroc": round(auroc, 4) if not np.isnan(auroc) else None,
            "spearman_global": round(rho_global, 4) if not np.isnan(rho_global) else None,
            "spearman_global_p": round(p_global, 6) if not np.isnan(p_global) else None,
            "spearman_conditional": round(rho_cond, 4) if not np.isnan(rho_cond) else None,
            "spearman_conditional_p": round(p_cond, 6) if not np.isnan(p_cond) else None,
        }

    fmt = lambda v: f"{v:.4f}" if v is not None else "N/A"
    print(f"  {'Signal':<6} | {'AUROC':>7} | {'ρ (global)':>11} | {'ρ (cond)':>10}")
    print(f"  {'-'*6}-+-{'-'*7}-+-{'-'*11}-+-{'-'*10}")
    for sig in SIGNALS:
        q = qe_results[sig]
        print(f"  {sig:<6} | {fmt(q['auroc']):>7} | {fmt(q['spearman_global']):>11} | {fmt(q['spearman_conditional']):>10}")

    # === 3. Selection metrics ===
    print(f"\n{'='*70}")
    print("3. SELECTION METRICS")
    print(f"{'='*70}")

    selection_results = {}
    print(f"  {'Signal':<6} | {'Sel F1':>7} | {'Δ (pp)':>8}")
    print(f"  {'-'*6}-+-{'-'*7}-+-{'-'*8}")
    for sig in SIGNALS:
        sel_f1 = float(signal_selected_f1s[sig].mean())
        delta = (sel_f1 - greedy_macro) * 100
        selection_results[sig] = {"f1": round(sel_f1, 4), "delta_pp": round(delta, 4)}
        print(f"  {sig:<6} | {sel_f1:.4f} | {delta:+.2f}pp")

    # === 4. Bootstrap CI ===
    B = args.bootstrap_b
    print(f"\n{'='*70}")
    print(f"4. BOOTSTRAP CI (B={B})")
    print(f"{'='*70}")

    bootstrap_results = {}
    primary_signals = SIGNALS

    for sig in primary_signals:
        boot_deltas = np.zeros(B)
        for b in range(B):
            idx = rng.choice(N, size=N, replace=True)
            boot_deltas[b] = (signal_selected_f1s[sig][idx].mean() - greedy_f1s[idx].mean()) * 100
        ci_lo = float(np.percentile(boot_deltas, 2.5))
        ci_hi = float(np.percentile(boot_deltas, 97.5))
        p_value = float(np.mean(boot_deltas <= 0))
        bootstrap_results[sig] = {
            "mean_delta_pp": round(float(boot_deltas.mean()), 4),
            "ci_95_lo_pp": round(ci_lo, 4),
            "ci_95_hi_pp": round(ci_hi, 4),
            "p_value": round(p_value, 6),
            "significant_005": p_value < 0.05,
        }

    print(f"  {'Signal':<6} | {'Mean Δ':>8} | {'95% CI':>18} | {'p-value':>10} | Sig?")
    print(f"  {'-'*6}-+-{'-'*8}-+-{'-'*18}-+-{'-'*10}-+-{'-'*5}")
    for sig in primary_signals:
        r = bootstrap_results[sig]
        sig_mark = "***" if r["p_value"] < 0.001 else ("**" if r["p_value"] < 0.01 else ("*" if r["p_value"] < 0.05 else ""))
        print(f"  {sig:<6} | {r['mean_delta_pp']:+8.4f} | [{r['ci_95_lo_pp']:+.4f}, {r['ci_95_hi_pp']:+.4f}] | {r['p_value']:.6f} | {sig_mark}")

    # === 5. Cross-dataset comparison ===
    print(f"\n{'='*70}")
    print("5. CROSS-DATASET COMPARISON")
    print(f"{'='*70}")

    lp_sel = selection_results["LP"]
    fewnerd_row = {
        "greedy": greedy_macro, "oracle": oracle_macro,
        "headroom": headroom,
        "lp_rho": qe_results["LP"]["spearman_global"],
        "lp_delta": lp_sel["delta_pp"],
    }

    print(f"  {'Dataset':<10} | {'Greedy':>7} | {'Oracle':>7} | {'Hdroom':>7} | {'LP ρ':>6} | {'LP Δ':>7}")
    print(f"  {'-'*10}-+-{'-'*7}-+-{'-'*7}-+-{'-'*7}-+-{'-'*6}-+-{'-'*7}")
    print(f"  {'SciERC':<10} | {SCIERC_REF['greedy']:.4f} | {SCIERC_REF['oracle']:.4f} | {SCIERC_REF['headroom']:+.1f}pp | {SCIERC_REF['lp_rho']:.3f} | {SCIERC_REF['lp_delta']:+.2f}pp")
    rho_s = f"{fewnerd_row['lp_rho']:.3f}" if fewnerd_row['lp_rho'] is not None else "N/A"
    print(f"  {'Few-NERD':<10} | {fewnerd_row['greedy']:.4f} | {fewnerd_row['oracle']:.4f} | {fewnerd_row['headroom']:+.1f}pp | {rho_s:>5} | {fewnerd_row['lp_delta']:+.2f}pp")
    print(f"  {'CoNLL':<10} | {CONLL_REF['greedy']:.4f} | {CONLL_REF['oracle']:.4f} | {CONLL_REF['headroom']:+.1f}pp | {CONLL_REF['lp_rho']:.3f} | {CONLL_REF['lp_delta']:+.2f}pp")

    # === 6. Entity type grouped analysis ===
    print(f"\n{'='*70}")
    print("6. ENTITY TYPE GROUPED ANALYSIS")
    print(f"{'='*70}")

    all_types = set()
    for types in instance_types:
        all_types.update(types)

    type_stats = {}
    for t in sorted(all_types):
        mask = np.array([t in types for types in instance_types])
        count = int(mask.sum())
        if count < 5:
            continue
        g_f1 = float(greedy_f1s[mask].mean())
        o_f1 = float(oracle_f1s[mask].mean())
        lp_f1 = float(signal_selected_f1s["LP"][mask].mean())
        lp_delta = (lp_f1 - g_f1) * 100
        zero_rate = float(np.mean(greedy_f1s[mask] == 0)) * 100
        type_stats[t] = {
            "count": count, "greedy_f1": round(g_f1, 4),
            "oracle_f1": round(o_f1, 4), "lp_selection_f1": round(lp_f1, 4),
            "lp_delta_pp": round(lp_delta, 4), "zero_f1_rate": round(zero_rate, 1),
        }

    print(f"  {'Type':<20} | {'N':>5} | {'Greedy':>7} | {'Oracle':>7} | {'LP Sel':>7} | {'LP Δ':>7} | {'Zero%':>5}")
    print(f"  {'-'*20}-+-{'-'*5}-+-{'-'*7}-+-{'-'*7}-+-{'-'*7}-+-{'-'*7}-+-{'-'*5}")
    for t in sorted(type_stats.keys(), key=lambda x: -type_stats[x]["count"]):
        ts = type_stats[t]
        zero_mark = " <-" if ts["zero_f1_rate"] > 20 else ""
        print(f"  {t:<20} | {ts['count']:>5} | {ts['greedy_f1']:.4f} | {ts['oracle_f1']:.4f} | {ts['lp_selection_f1']:.4f} | {ts['lp_delta_pp']:+.2f}pp | {ts['zero_f1_rate']:>4.1f}%{zero_mark}")

    # === Save results ===
    results = {
        "meta": {"input": input_path, "n_total": total_raw, "n_filtered": N, "n_samples": n_samples},
        "basic": {
            "greedy_macro_f1": greedy_macro, "oracle_macro_f1": oracle_macro,
            "headroom_pp": headroom, "zero_f1_rate_pct": zero_f1_rate,
            "degeneracy_rate_pct": degeneracy_rate,
            "lp_range_median": float(np.median(lp_ranges)),
        },
        "qe": qe_results,
        "selection": selection_results,
        "bootstrap": bootstrap_results,
        "cross_dataset": {"scierc": SCIERC_REF, "fewnerd": fewnerd_row, "conll": CONLL_REF},
        "entity_types": type_stats,
    }

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
