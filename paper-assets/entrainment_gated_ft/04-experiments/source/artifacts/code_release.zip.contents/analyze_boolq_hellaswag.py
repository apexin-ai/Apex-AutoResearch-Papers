#!/usr/bin/env python3
"""BoolQ + HellaSwag per-example analysis for entrainment_gated_ft project."""
import json, os
import numpy as np
from itertools import permutations
from scipy.stats import spearmanr

EVAL_BASE = "/root/entrainment_gated_ft/lm_eval_clean"
OUTPUT_DIR = "/root/entrainment_gated_ft/analysis_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ARCHS = ["GatedDeltaNet", "RetNet", "HGRN2"]
ARCH_SHORT = {"GatedDeltaNet": "GDN", "RetNet": "RetNet", "HGRN2": "HGRN2"}
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
RATIO_DIR = {"pure": "pure", "h24-1": "hybrid-24-1", "h12-1": "hybrid-12-1", "h6-1": "hybrid-6-1", "h3-1": "hybrid-3-1"}
ARCH_PAIRS = [("GDN", "RetNet"), ("GDN", "HGRN2"), ("RetNet", "HGRN2")]
ARCH_FROM_SHORT = {"GDN": "GatedDeltaNet", "RetNet": "RetNet", "HGRN2": "HGRN2"}

BENCHMARKS = {
    "boolq": {"expected_n": 3270},
    "hellaswag": {"expected_n": 10042}
}

def load_accs(benchmark, arch, ratio):
    dir_name = f"1.3B-100B-{arch}-{RATIO_DIR[ratio]}"
    path = f"{EVAL_BASE}/{benchmark}/{dir_name}/samples/{benchmark}.jsonl"
    accs = []
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            acc_field = "acc_norm" if benchmark == "hellaswag" else "acc"
            accs.append((d["doc_id"], int(d[acc_field])))
    accs.sort(key=lambda x: x[0])
    return [a for _, a in accs]

def jaccard(set_a, set_b):
    if not set_a and not set_b:
        return 0.0
    union = set_a | set_b
    return len(set_a & set_b) / len(union) if union else 0.0

def jaccard_null(a_size, b_size, n):
    exp = a_size * b_size / n
    denom = a_size + b_size - exp
    return exp / denom if denom > 0 else 0.0

def jaccard_max(a_size, b_size):
    m = min(a_size, b_size)
    denom = a_size + b_size - m
    return m / denom if denom > 0 else 0.0

def normalized_es(j_obs, j_null, j_max):
    denom = j_max - j_null
    return (j_obs - j_null) / denom if denom > 0 else 0.0

def permutation_test(set_a_size, set_b_size, n_total, j_obs, n_perms=10000, seed=42):
    rng = np.random.RandomState(seed)
    count = 0
    indices = np.arange(n_total)
    for _ in range(n_perms):
        perm_a = set(rng.choice(n_total, set_a_size, replace=False))
        perm_b = set(rng.choice(n_total, set_b_size, replace=False))
        j_perm = len(perm_a & perm_b) / len(perm_a | perm_b) if (perm_a | perm_b) else 0
        if j_perm >= j_obs:
            count += 1
    return count / n_perms

def spearman_exact(x, y):
    rho, _ = spearmanr(x, y)
    n = len(x)
    count = 0
    total = 0
    for perm in permutations(y):
        r, _ = spearmanr(x, list(perm))
        total += 1
        if abs(r) >= abs(rho):
            count += 1
    return rho, count / total

for benchmark, bconf in BENCHMARKS.items():
    print(f"\n{'='*60}")
    print(f"Analyzing {benchmark}")
    print(f"{'='*60}")

    data = {}
    for arch in ARCHS:
        data[arch] = {}
        for ratio in RATIOS:
            data[arch][ratio] = load_accs(benchmark, arch, ratio)
            print(f"  {ARCH_SHORT[arch]:6s} {ratio:6s}: N={len(data[arch][ratio])}, acc={np.mean(data[arch][ratio]):.4f}")

    N = bconf["expected_n"]
    assert all(len(data[a][r]) == N for a in ARCHS for r in RATIOS), "Sample count mismatch!"

    # A. Per-example classification
    per_example = {}
    for arch in ARCHS:
        short = ARCH_SHORT[arch]
        per_example[short] = {}
        pure = data[arch]["pure"]
        for ratio in RATIOS[1:]:
            hybrid = data[arch][ratio]
            helped = sum(1 for p, h in zip(pure, hybrid) if p == 0 and h == 1)
            hurt = sum(1 for p, h in zip(pure, hybrid) if p == 1 and h == 0)
            stayed_right = sum(1 for p, h in zip(pure, hybrid) if p == 1 and h == 1)
            stayed_wrong = sum(1 for p, h in zip(pure, hybrid) if p == 0 and h == 0)
            per_example[short][ratio] = {
                "n_helped": helped, "n_hurt": hurt,
                "n_stayed_right": stayed_right, "n_stayed_wrong": stayed_wrong,
                "net_effect": helped - hurt,
                "pct_helped": round(helped / N * 100, 2),
                "pct_hurt": round(hurt / N * 100, 2)
            }

    # B+C. Jaccard analysis
    jaccard_results = {}
    for ratio in RATIOS[1:]:
        jaccard_results[ratio] = {}
        sets = {}
        for arch in ARCHS:
            short = ARCH_SHORT[arch]
            pure = data[arch]["pure"]
            hybrid = data[arch][ratio]
            helped_set = {i for i, (p, h) in enumerate(zip(pure, hybrid)) if p == 0 and h == 1}
            hurt_set = {i for i, (p, h) in enumerate(zip(pure, hybrid)) if p == 1 and h == 0}
            sets[short] = {"helped": helped_set, "hurt": hurt_set}

        for a_name, b_name in ARCH_PAIRS:
            pair_key = f"{a_name}-{b_name}"
            for category in ["helped", "hurt"]:
                set_a = sets[a_name][category]
                set_b = sets[b_name][category]
                j_obs = jaccard(set_a, set_b)
                j_n = jaccard_null(len(set_a), len(set_b), N)
                j_m = jaccard_max(len(set_a), len(set_b))
                n_es = normalized_es(j_obs, j_n, j_m)
                p_val = permutation_test(len(set_a), len(set_b), N, j_obs)
                key = f"{pair_key}_{category}"
                jaccard_results[ratio][key] = {
                    "J_obs": round(j_obs, 4),
                    "J_null": round(j_n, 4),
                    "J_max": round(j_m, 4),
                    "normalized_ES": round(n_es, 4),
                    "p_value_permutation": round(p_val, 4),
                    "n_permutations": 10000,
                    "sizes": [len(set_a), len(set_b)]
                }
                print(f"  {ratio} {pair_key} {category}: J={j_obs:.4f} J_null={j_n:.4f} nES={n_es:.4f} p={p_val:.4f}")

    # D. Ambiguity alpha
    ambiguity = {}
    for ratio in RATIOS:
        preds = [data[arch][ratio] for arch in ARCHS]
        votes = [sum(preds[a][i] for a in range(3)) for i in range(N)]
        n_ambiguous = sum(1 for v in votes if v != 0 and v != 3)
        ambiguity[ratio] = {
            "ambiguity_alpha": round(n_ambiguous / N, 6),
            "n_ambiguous": n_ambiguous,
            "n_samples": N,
            "disagreement_distribution": {
                "0_of_3": sum(1 for v in votes if v == 0),
                "1_of_3": sum(1 for v in votes if v == 1),
                "2_of_3": sum(1 for v in votes if v == 2),
                "3_of_3": sum(1 for v in votes if v == 3),
            }
        }
        print(f"  {ratio} ambiguity_alpha={ambiguity[ratio]['ambiguity_alpha']:.4f}")

    # E. Convergence sigma + Spearman
    convergence = {}
    sigmas = []
    for ratio in RATIOS:
        accs = [np.mean(data[arch][ratio]) for arch in ARCHS]
        sigma = float(np.std(accs))
        convergence[ratio] = {
            "sigma": round(sigma, 6),
            "accs": {ARCH_SHORT[arch]: round(np.mean(data[arch][ratio]), 4) for arch in ARCHS}
        }
        sigmas.append(sigma)

    rho, p_exact = spearman_exact(list(range(len(RATIOS))), sigmas)
    convergence["spearman"] = {"rho": round(rho, 4), "p_exact_two_tailed": round(p_exact, 4), "n_permutations": 120}
    print(f"  Spearman rho={rho:.4f}, p={p_exact:.4f}")

    # Save per_example JSON
    per_example_output = {
        "benchmark": benchmark,
        "n_samples": N,
        "architectures": list(ARCH_SHORT.values()),
        "ratios": RATIOS,
        "per_example_classification": per_example,
        "ambiguity": ambiguity,
        "convergence_sigma": convergence
    }
    with open(f"{OUTPUT_DIR}/{benchmark}_per_example.json", "w") as f:
        json.dump(per_example_output, f, indent=2)
    print(f"  Wrote {OUTPUT_DIR}/{benchmark}_per_example.json")

    # Save Jaccard JSON
    jaccard_output = {
        "benchmark": benchmark,
        "n_samples": N,
        "arch_pairs": [f"{a}-{b}" for a, b in ARCH_PAIRS],
        "jaccard_analysis": jaccard_results
    }
    with open(f"{OUTPUT_DIR}/{benchmark}_jaccard_analysis.json", "w") as f:
        json.dump(jaccard_output, f, indent=2)
    print(f"  Wrote {OUTPUT_DIR}/{benchmark}_jaccard_analysis.json")

print(f"\nDone! 4 files in {OUTPUT_DIR}")
