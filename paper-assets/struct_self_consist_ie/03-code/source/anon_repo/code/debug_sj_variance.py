#!/usr/bin/env python3
"""Debug SJ selection delta variance + AUROC NaN across 4 FewNERD seeds.

Uses identical code for all seeds to isolate script-vs-seed variance.
Computes both hard Jaccard and soft Jaccard SJ selection for comparison.
"""
import json, os, sys, time
import numpy as np
from collections import Counter
from scipy.stats import spearmanr, rankdata

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
SEEDS = {
    42:  f"{BASE}/exp_021_inference/samples.jsonl",
    123: f"{BASE}/exp_021_fewnerd_n8_seed123/samples.jsonl",
    456: f"{BASE}/exp_021_fewnerd_n8_seed456/samples.jsonl",
    789: f"{BASE}/fewnerd_seed789_merged/samples.jsonl",
}

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)


def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2:
        return float("nan")
    n_pos, n_neg = (labels == 1).sum(), (labels == 0).sum()
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))


def compute_per_sample_sj_soft(inst):
    """Soft Jaccard (Hungarian span matching) per-sample scores."""
    samples = inst["samples"]
    N = len(samples)
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(
                samples[i].get("entities", []),
                samples[j].get("entities", [])
            )
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_per_sample_sj_hard(inst):
    """Hard set Jaccard (exact text+type matching) per-sample scores."""
    samples = inst["samples"]
    N = len(samples)
    sample_sets = []
    for s in samples:
        eset = set((e.get("text", ""), e.get("type", "")) for e in s.get("entities", []))
        sample_sets.append(eset)
    scores = []
    for k in range(N):
        jaccards = []
        for j in range(N):
            if j == k:
                continue
            inter = len(sample_sets[k] & sample_sets[j])
            union = len(sample_sets[k] | sample_sets[j])
            jaccards.append(inter / union if union > 0 else 1.0)
        scores.append(float(np.mean(jaccards)))
    return scores


def analyze_seed(seed, path):
    print(f"\n{'='*60}")
    print(f"Seed {seed}: {path}")
    print(f"{'='*60}")

    data = []
    with open(path) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    n_total = len(data)
    gold_filtered = [inst for inst in data if inst["gold"].get("entities", [])]
    N = len(gold_filtered)
    n_samples = len(gold_filtered[0]["samples"])
    print(f"  Total: {n_total}, Gold-filtered: {N}, N_samples: {n_samples}")

    greedy_f1s = np.zeros(N)
    oracle_f1s = np.zeros(N)
    all_sample_f1s = np.zeros((N, n_samples))

    # Selection arrays
    sj_soft_sel = np.zeros(N)
    sj_hard_sel = np.zeros(N)
    lp_sel = np.zeros(N)

    t0 = time.time()
    for i, inst in enumerate(gold_filtered):
        greedy_f1s[i] = per_instance_f1(inst["greedy"], inst["gold"], subtask="ner")
        for j, s in enumerate(inst["samples"]):
            all_sample_f1s[i, j] = per_instance_f1(s, inst["gold"], subtask="ner")
        oracle_f1s[i] = all_sample_f1s[i].max()

        # LP selection
        per_sample_lp = np.array([s.get("mean_logprob", float("-inf")) for s in inst["samples"]])
        lp_sel[i] = all_sample_f1s[i, int(np.argmax(per_sample_lp))]

        # SJ soft selection
        sj_soft_scores = compute_per_sample_sj_soft(inst)
        sj_soft_sel[i] = all_sample_f1s[i, int(np.argmax(sj_soft_scores))]

        # SJ hard selection
        sj_hard_scores = compute_per_sample_sj_hard(inst)
        sj_hard_sel[i] = all_sample_f1s[i, int(np.argmax(sj_hard_scores))]

        if (i + 1) % 5000 == 0:
            print(f"  Processed {i+1}/{N}")

    elapsed = time.time() - t0
    greedy_macro = float(greedy_f1s.mean())
    oracle_macro = float(oracle_f1s.mean())

    sj_soft_delta = (float(sj_soft_sel.mean()) - greedy_macro) * 100
    sj_hard_delta = (float(sj_hard_sel.mean()) - greedy_macro) * 100
    lp_delta = (float(lp_sel.mean()) - greedy_macro) * 100

    # AUROC debug: check label distribution with greedy_f1 > median
    median_f1 = float(np.median(greedy_f1s))
    labels_median = (greedy_f1s > median_f1).astype(int)
    n_pos_median = int(labels_median.sum())
    n_neg_median = int((1 - labels_median).sum())

    print(f"\n  AUROC debug (greedy_f1 > median):")
    print(f"    median_f1 = {median_f1:.6f}")
    print(f"    n_pos (>median) = {n_pos_median}, n_neg (<=median) = {n_neg_median}")
    print(f"    unique labels = {len(np.unique(labels_median))}")

    # Try sklearn AUROC to reproduce NaN
    from sklearn.metrics import roc_auc_score
    lp_values = np.array([float(np.mean([s.get("mean_logprob", float("nan"))
                           for s in inst["samples"] if s.get("mean_logprob") is not None]))
                           for inst in gold_filtered])
    valid = np.isfinite(lp_values) & np.isfinite(greedy_f1s)
    median_f1_v = float(np.median(greedy_f1s[valid]))
    labels_v = (greedy_f1s[valid] > median_f1_v).astype(int)
    print(f"    valid count = {valid.sum()}")
    print(f"    median_f1 (valid) = {median_f1_v:.6f}")
    print(f"    labels_v unique = {np.unique(labels_v, return_counts=True)}")

    try:
        sklearn_auroc = float(roc_auc_score(labels_v, lp_values[valid]))
        print(f"    sklearn roc_auc_score(LP) = {sklearn_auroc}")
    except Exception as e:
        print(f"    sklearn roc_auc_score(LP) RAISED: {e}")

    # safe_auroc with same labels
    sa = safe_auroc(lp_values[valid], labels_v)
    print(f"    safe_auroc(LP) = {sa}")

    result = {
        "seed": seed,
        "n_filtered": N,
        "greedy_f1": round(greedy_macro, 4),
        "oracle_f1": round(oracle_macro, 4),
        "headroom_pp": round((oracle_macro - greedy_macro) * 100, 2),
        "lp_delta_pp": round(lp_delta, 2),
        "sj_soft_delta_pp": round(sj_soft_delta, 2),
        "sj_hard_delta_pp": round(sj_hard_delta, 2),
        "sj_soft_minus_hard_pp": round(sj_soft_delta - sj_hard_delta, 2),
        "elapsed_s": round(elapsed, 1),
    }

    print(f"\n  Results (elapsed {elapsed:.0f}s):")
    print(f"    Greedy F1:       {greedy_macro:.4f}")
    print(f"    Oracle F1:       {oracle_macro:.4f}")
    print(f"    LP delta:        {lp_delta:+.2f}pp")
    print(f"    SJ soft delta:   {sj_soft_delta:+.2f}pp")
    print(f"    SJ hard delta:   {sj_hard_delta:+.2f}pp")
    print(f"    soft - hard:     {sj_soft_delta - sj_hard_delta:+.2f}pp")

    return result


def main():
    t0 = time.time()
    all_results = {}

    for seed, path in sorted(SEEDS.items()):
        if not os.path.exists(path):
            print(f"\nSkipping seed {seed}: {path} not found")
            continue
        all_results[seed] = analyze_seed(seed, path)

    # Summary table
    print(f"\n{'='*80}")
    print("SUMMARY: SJ SELECTION DELTA COMPARISON (same code for all seeds)")
    print(f"{'='*80}")
    print(f"{'Seed':>6} {'Greedy':>8} {'LP Δpp':>8} {'SJ_soft Δpp':>12} {'SJ_hard Δpp':>12} {'soft-hard':>10}")
    print("-" * 62)
    for seed in sorted(all_results.keys()):
        r = all_results[seed]
        print(f"{seed:>6} {r['greedy_f1']:>8.4f} {r['lp_delta_pp']:>+8.2f} "
              f"{r['sj_soft_delta_pp']:>+12.2f} {r['sj_hard_delta_pp']:>+12.2f} "
              f"{r['sj_soft_minus_hard_pp']:>+10.2f}")

    # Stats
    soft_deltas = [all_results[s]["sj_soft_delta_pp"] for s in sorted(all_results.keys())]
    hard_deltas = [all_results[s]["sj_hard_delta_pp"] for s in sorted(all_results.keys())]
    print(f"\nSJ soft delta: mean={np.mean(soft_deltas):+.2f}, std={np.std(soft_deltas):.2f}, range={max(soft_deltas)-min(soft_deltas):.2f}")
    print(f"SJ hard delta: mean={np.mean(hard_deltas):+.2f}, std={np.std(hard_deltas):.2f}, range={max(hard_deltas)-min(hard_deltas):.2f}")

    total_elapsed = time.time() - t0
    print(f"\nTotal elapsed: {total_elapsed:.0f}s")

    # Save results
    out_path = f"{BASE}/debug_sj_variance_results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
