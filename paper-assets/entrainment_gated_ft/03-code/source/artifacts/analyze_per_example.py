#!/usr/bin/env python3
"""Per-example analysis for BoolQ and HellaSwag across 15 models."""
import json
import os
import sys
import numpy as np
from itertools import combinations
from scipy.stats import spearmanr

BASE = "/root/entrainment_gated_ft/lm_eval_clean"
ARCHS = ["GatedDeltaNet", "RetNet", "HGRN2"]
RATIOS = ["pure", "hybrid-24-1", "hybrid-12-1", "hybrid-6-1", "hybrid-3-1"]
RATIO_LABELS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
ATTN_RATIO_RANK = [0, 1, 2, 3, 4]  # pure=0 (no attn), h3-1=4 (most attn)

def model_name(arch, ratio):
    return f"1.3B-100B-{arch}-{ratio}"

def load_samples(task, arch, ratio):
    mname = model_name(arch, ratio)
    path = os.path.join(BASE, task, mname, "samples", f"{task}.jsonl")
    samples = {}
    with open(path) as f:
        for line in f:
            s = json.loads(line)
            samples[s["doc_id"]] = s["acc"]
    return samples

def classification(pure_acc, hybrid_acc, doc_ids):
    helped, hurt, stayed_right, stayed_wrong = [], [], [], []
    for d in doc_ids:
        p, h = pure_acc[d], hybrid_acc[d]
        if p == 0 and h == 1: helped.append(d)
        elif p == 1 and h == 0: hurt.append(d)
        elif p == 1 and h == 1: stayed_right.append(d)
        else: stayed_wrong.append(d)
    return helped, hurt, stayed_right, stayed_wrong

def jaccard(setA, setB):
    a, b = set(setA), set(setB)
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union > 0 else 0.0

def jaccard_null(sizeA, sizeB, N):
    expected_inter = sizeA * sizeB / N
    expected_union = sizeA + sizeB - expected_inter
    return expected_inter / expected_union if expected_union > 0 else 0.0

def jaccard_max(sizeA, sizeB):
    m = min(sizeA, sizeB)
    denom = sizeA + sizeB - m
    return m / denom if denom > 0 else 0.0

def normalized_es(j_obs, j_null, j_max):
    denom = j_max - j_null
    return (j_obs - j_null) / denom if denom > 1e-12 else 0.0

def permutation_test(setA, setB, N, n_perms=10000):
    j_obs = jaccard(setA, setB)
    sA, sB = len(setA), len(setB)
    count = 0
    all_ids = np.arange(N)
    for _ in range(n_perms):
        permA = set(np.random.choice(all_ids, sA, replace=False).tolist())
        permB = set(np.random.choice(all_ids, sB, replace=False).tolist())
        if jaccard(permA, permB) >= j_obs:
            count += 1
    return count / n_perms

def analyze_task(task):
    print(f"\n{'='*60}")
    print(f"Analyzing: {task}")
    print(f"{'='*60}")

    # Load all models
    all_data = {}
    for arch in ARCHS:
        for ratio in RATIOS:
            all_data[(arch, ratio)] = load_samples(task, arch, ratio)

    doc_ids = sorted(all_data[(ARCHS[0], RATIOS[0])].keys())
    N = len(doc_ids)
    print(f"Total samples: {N}")

    result = {"task": task, "N": N}

    # A. Per-example classification
    classifications = {}
    for arch in ARCHS:
        pure = all_data[(arch, "pure")]
        for ratio in RATIOS[1:]:  # hybrid only
            hybrid = all_data[(arch, ratio)]
            helped, hurt, sr, sw = classification(pure, hybrid, doc_ids)
            key = f"{arch}_{ratio}"
            classifications[key] = {
                "helped": len(helped), "hurt": len(hurt),
                "stayed_right": len(sr), "stayed_wrong": len(sw),
                "helped_ids": helped, "hurt_ids": hurt,
                "net_gain": len(helped) - len(hurt),
            }
            print(f"  {key}: helped={len(helped)}, hurt={len(hurt)}, net={len(helped)-len(hurt)}")
    result["classifications"] = {k: {kk: vv for kk, vv in v.items() if kk != "helped_ids" and kk != "hurt_ids"}
                                  for k, v in classifications.items()}

    # B. Cross-architecture Jaccard (helped & hurt separately)
    cross_jaccard = {}
    arch_pairs = list(combinations(ARCHS, 2))
    for ratio in RATIOS[1:]:
        for category in ["helped", "hurt"]:
            for a1, a2 in arch_pairs:
                k1 = f"{a1}_{ratio}"
                k2 = f"{a2}_{ratio}"
                s1 = set(classifications[k1][f"{category}_ids"])
                s2 = set(classifications[k2][f"{category}_ids"])
                j = jaccard(s1, s2)
                jn = jaccard_null(len(s1), len(s2), N)
                jm = jaccard_max(len(s1), len(s2))
                nes = normalized_es(j, jn, jm)
                pval = permutation_test(s1, s2, N) if len(s1) > 0 and len(s2) > 0 else 1.0
                key = f"{ratio}_{category}_{a1}_vs_{a2}"
                cross_jaccard[key] = {
                    "J_obs": round(j, 4), "J_null": round(jn, 4),
                    "J_max": round(jm, 4), "NES": round(nes, 4),
                    "p_value": round(pval, 4),
                    "size_A": len(s1), "size_B": len(s2),
                }
                print(f"  Jaccard {key}: J={j:.4f}, NES={nes:.4f}, p={pval:.4f}")
    result["cross_jaccard"] = cross_jaccard

    # D. Ambiguity α (Marx 2020): fraction where >=2 of 3 archs disagree on direction
    ambiguity = {}
    for ratio in RATIOS[1:]:
        disagree_count = 0
        for d in doc_ids:
            directions = []
            for arch in ARCHS:
                p = all_data[(arch, "pure")][d]
                h = all_data[(arch, ratio)][d]
                directions.append(h - p)  # +1=helped, -1=hurt, 0=same
            signs = [1 if x > 0 else (-1 if x < 0 else 0) for x in directions]
            nonzero = [s for s in signs if s != 0]
            if len(nonzero) >= 2 and len(set(nonzero)) > 1:
                disagree_count += 1
        alpha = disagree_count / N
        ambiguity[ratio] = {"alpha": round(alpha, 4), "disagree_count": disagree_count}
        print(f"  Ambiguity α ({ratio}): {alpha:.4f} ({disagree_count}/{N})")
    result["ambiguity"] = ambiguity

    # E. Convergence σ + Spearman ρ
    convergence = {}
    for ratio_idx, ratio in enumerate(RATIOS):
        per_sample_accs = []
        for d in doc_ids:
            accs = [all_data[(arch, ratio)][d] for arch in ARCHS]
            per_sample_accs.append(np.std(accs))
        mean_sigma = float(np.mean(per_sample_accs))
        convergence[ratio] = {"mean_sigma": round(mean_sigma, 4)}
        print(f"  Convergence σ ({ratio}): {mean_sigma:.4f}")

    sigmas = [convergence[r]["mean_sigma"] for r in RATIOS]
    rho, pval = spearmanr(ATTN_RATIO_RANK, sigmas)
    convergence["spearman_rho"] = round(float(rho), 4)
    convergence["spearman_p"] = round(float(pval), 4)
    print(f"  Spearman ρ(attn_rank, σ): {rho:.4f}, p={pval:.4f}")
    result["convergence"] = convergence

    return result

if __name__ == "__main__":
    np.random.seed(42)
    results = {}
    for task in ["boolq", "hellaswag"]:
        results[task] = analyze_task(task)
        outpath = f"/root/entrainment_gated_ft/{task}_per_example.json"
        with open(outpath, "w") as f:
            json.dump(results[task], f, indent=2)
        print(f"\nSaved: {outpath}")

    print("\n\n=== SUMMARY ===")
    for task in ["boolq", "hellaswag"]:
        r = results[task]
        print(f"\n{task.upper()} (N={r['N']}):")
        alphas = [r["ambiguity"][ratio]["alpha"] for ratio in RATIOS[1:]]
        print(f"  Ambiguity α range: {min(alphas):.4f} - {max(alphas):.4f}")
        j_vals = [v["J_obs"] for v in r["cross_jaccard"].values()]
        print(f"  Jaccard range: {min(j_vals):.4f} - {max(j_vals):.4f}")
        print(f"  Convergence ρ: {r['convergence']['spearman_rho']:.4f} (p={r['convergence']['spearman_p']:.4f})")
