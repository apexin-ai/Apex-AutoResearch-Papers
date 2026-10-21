#!/usr/bin/env python3
"""Compute per-example multiplicity metrics for WinoGrande and PIQA."""
import json, os, sys, random, itertools
from collections import defaultdict
import numpy as np

EVAL_BASE = "/root/entrainment_gated_ft/lm_eval_clean"
ARCHS = ["GDN", "RetNet", "HGRN2"]
ARCH_PREFIXES = {
    "GDN": "1.3B-100B-GatedDeltaNet",
    "RetNet": "1.3B-100B-RetNet",
    "HGRN2": "1.3B-100B-HGRN2",
}
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
RATIO_SUFFIXES = {
    "pure": "-pure",
    "h24-1": "-hybrid-24-1",
    "h12-1": "-hybrid-12-1",
    "h6-1": "-hybrid-6-1",
    "h3-1": "-hybrid-3-1",
}
ARCH_PAIRS = [("GDN", "RetNet"), ("GDN", "HGRN2"), ("RetNet", "HGRN2")]
N_PERM_JACCARD = 10000
random.seed(42)
np.random.seed(42)


def load_samples(benchmark, arch, ratio):
    model_name = ARCH_PREFIXES[arch] + RATIO_SUFFIXES[ratio]
    sample_file = os.path.join(EVAL_BASE, benchmark, model_name, "samples", f"{benchmark}.jsonl")
    if not os.path.exists(sample_file):
        print(f"MISSING: {sample_file}", file=sys.stderr)
        return None
    results = {}
    with open(sample_file) as f:
        for line in f:
            row = json.loads(line)
            doc_id = row["doc_id"]
            acc = row.get("acc", None)
            if acc is None:
                acc = row.get("exact_match", None)
            if acc is None:
                filtered = row.get("filtered_resps", [])
                target = row.get("target", None)
                if filtered and target is not None:
                    pred_idx = max(range(len(filtered)), key=lambda i: filtered[i][0])
                    acc = 1.0 if pred_idx == target else 0.0
            results[doc_id] = int(round(float(acc))) if acc is not None else None
    return results


def compute_per_example_classification(pure_preds, hybrid_preds, n_samples):
    n_helped = n_hurt = n_stayed_right = n_stayed_wrong = 0
    for doc_id in range(n_samples):
        p = pure_preds.get(doc_id)
        h = hybrid_preds.get(doc_id)
        if p is None or h is None:
            continue
        if p == 0 and h == 1:
            n_helped += 1
        elif p == 1 and h == 0:
            n_hurt += 1
        elif p == 1 and h == 1:
            n_stayed_right += 1
        else:
            n_stayed_wrong += 1
    total = n_helped + n_hurt + n_stayed_right + n_stayed_wrong
    return {
        "n_helped": n_helped,
        "n_hurt": n_hurt,
        "n_stayed_right": n_stayed_right,
        "n_stayed_wrong": n_stayed_wrong,
        "net_effect": n_helped - n_hurt,
        "pct_helped": round(100 * n_helped / total, 2) if total > 0 else 0,
        "pct_hurt": round(100 * n_hurt / total, 2) if total > 0 else 0,
    }


def compute_ambiguity(all_preds, ratio, n_samples):
    arch_preds = []
    for arch in ARCHS:
        preds = all_preds[arch][ratio]
        if preds is None:
            return None
        arch_preds.append(preds)
    dist = {"0_of_3": 0, "1_of_3": 0, "2_of_3": 0, "3_of_3": 0}
    n_ambiguous = 0
    for doc_id in range(n_samples):
        vals = [ap.get(doc_id) for ap in arch_preds]
        if None in vals:
            continue
        n_correct = sum(vals)
        dist[f"{n_correct}_of_3"] += 1
        if n_correct != 0 and n_correct != 3:
            n_ambiguous += 1
    total = sum(dist.values())
    return {
        "ambiguity_alpha": round(n_ambiguous / total, 6) if total > 0 else 0,
        "n_ambiguous": n_ambiguous,
        "n_samples": total,
        "disagreement_distribution": dist,
    }


def compute_convergence(all_preds, n_samples):
    result = {}
    sigmas = []
    for ratio in RATIOS:
        accs = {}
        for arch in ARCHS:
            preds = all_preds[arch][ratio]
            if preds is None:
                continue
            correct = sum(1 for d in range(n_samples) if preds.get(d) == 1)
            total = sum(1 for d in range(n_samples) if preds.get(d) is not None)
            accs[arch] = round(correct / total, 4) if total > 0 else 0
        sigma = round(np.std(list(accs.values())), 6) if len(accs) == 3 else None
        result[ratio] = {"sigma": sigma, "accs": accs}
        if sigma is not None:
            sigmas.append(sigma)

    if len(sigmas) == 5:
        rho, p = exact_spearman_test(list(range(5)), sigmas)
        result["spearman"] = {
            "rho": round(rho, 6) if rho is not None else None,
            "p_exact_two_tailed": round(p, 6) if p is not None else None,
            "n_permutations": 120,
        }
    return result


def spearman_rho(x, y):
    n = len(x)
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    d = rx - ry
    return 1 - 6 * np.sum(d ** 2) / (n * (n ** 2 - 1))


def exact_spearman_test(x, y):
    n = len(x)
    obs_rho = spearman_rho(x, y)
    count_ge = 0
    total = 0
    for perm in itertools.permutations(range(n)):
        perm_y = [y[i] for i in perm]
        r = spearman_rho(x, perm_y)
        if abs(r) >= abs(obs_rho) - 1e-10:
            count_ge += 1
        total += 1
    return obs_rho, count_ge / total


def compute_jaccard(set_a, set_b, N):
    a = set(set_a)
    b = set(set_b)
    intersection = len(a & b)
    union = len(a | b)
    j_obs = intersection / union if union > 0 else 0
    na, nb = len(a), len(b)
    denom = N * (na + nb) - na * nb
    j_null = (na * nb) / denom if denom > 0 else 0
    j_max = min(na, nb) / max(na, nb) if max(na, nb) > 0 else 0
    if abs(j_max - j_null) < 1e-10:
        norm_es = 0
    else:
        norm_es = (j_obs - j_null) / (j_max - j_null)

    count_ge = 0
    all_indices = list(range(N))
    for _ in range(N_PERM_JACCARD):
        perm = random.sample(all_indices, na + nb)
        pa = set(perm[:na])
        pb = set(perm[na:])
        pi = len(pa & pb)
        pu = len(pa | pb)
        pj = pi / pu if pu > 0 else 0
        if pj >= j_obs - 1e-10:
            count_ge += 1
    p_val = count_ge / N_PERM_JACCARD

    return {
        "J_obs": round(j_obs, 4),
        "J_null": round(j_null, 4),
        "J_max": round(j_max, 4),
        "normalized_ES": round(norm_es, 4),
        "p_value_permutation": round(p_val, 4),
        "n_permutations": N_PERM_JACCARD,
        "sizes": [na, nb],
    }


def analyze_benchmark(benchmark):
    print(f"\n{'='*60}")
    print(f"Analyzing {benchmark}")
    print(f"{'='*60}")

    all_preds = {}
    for arch in ARCHS:
        all_preds[arch] = {}
        for ratio in RATIOS:
            preds = load_samples(benchmark, arch, ratio)
            all_preds[arch][ratio] = preds
            if preds is not None:
                n_correct = sum(1 for v in preds.values() if v == 1)
                print(f"  {arch} {ratio}: {len(preds)} samples, acc={n_correct/len(preds):.4f}")
            else:
                print(f"  {arch} {ratio}: MISSING")

    first_valid = None
    for arch in ARCHS:
        for ratio in RATIOS:
            if all_preds[arch][ratio] is not None:
                first_valid = all_preds[arch][ratio]
                break
        if first_valid:
            break
    if first_valid is None:
        print("ERROR: No valid predictions found!")
        return None, None
    n_samples = max(first_valid.keys()) + 1
    print(f"\nn_samples = {n_samples}")

    # per-example classification
    per_example = {}
    for arch in ARCHS:
        per_example[arch] = {}
        pure_preds = all_preds[arch]["pure"]
        if pure_preds is None:
            continue
        for ratio in RATIOS[1:]:
            hybrid_preds = all_preds[arch][ratio]
            if hybrid_preds is None:
                continue
            per_example[arch][ratio] = compute_per_example_classification(pure_preds, hybrid_preds, n_samples)

    # ambiguity
    ambiguity = {}
    for ratio in RATIOS:
        result = compute_ambiguity(all_preds, ratio, n_samples)
        if result:
            ambiguity[ratio] = result
            print(f"  Ambiguity {ratio}: alpha={result['ambiguity_alpha']:.4f}")

    # convergence
    convergence = compute_convergence(all_preds, n_samples)

    per_example_json = {
        "benchmark": benchmark,
        "n_samples": n_samples,
        "architectures": ARCHS,
        "ratios": RATIOS,
        "per_example_classification": per_example,
        "ambiguity": ambiguity,
        "convergence_sigma": convergence,
    }

    # Jaccard analysis
    jaccard = {}
    for ratio in RATIOS[1:]:
        jaccard[ratio] = {}
        for a1, a2 in ARCH_PAIRS:
            pair_name = f"{a1}-{a2}"
            pure_a1 = all_preds[a1]["pure"]
            hybrid_a1 = all_preds[a1][ratio]
            pure_a2 = all_preds[a2]["pure"]
            hybrid_a2 = all_preds[a2][ratio]
            if any(x is None for x in [pure_a1, hybrid_a1, pure_a2, hybrid_a2]):
                continue

            helped_a1 = {d for d in range(n_samples) if pure_a1.get(d) == 0 and hybrid_a1.get(d) == 1}
            hurt_a1 = {d for d in range(n_samples) if pure_a1.get(d) == 1 and hybrid_a1.get(d) == 0}
            helped_a2 = {d for d in range(n_samples) if pure_a2.get(d) == 0 and hybrid_a2.get(d) == 1}
            hurt_a2 = {d for d in range(n_samples) if pure_a2.get(d) == 1 and hybrid_a2.get(d) == 0}

            jaccard[ratio][f"{pair_name}_helped"] = compute_jaccard(helped_a1, helped_a2, n_samples)
            jaccard[ratio][f"{pair_name}_hurt"] = compute_jaccard(hurt_a1, hurt_a2, n_samples)
            print(f"  Jaccard {ratio} {pair_name}_helped: J={jaccard[ratio][f'{pair_name}_helped']['J_obs']:.4f}")

    jaccard_json = {
        "benchmark": benchmark,
        "n_samples": n_samples,
        "arch_pairs": [f"{a}-{b}" for a, b in ARCH_PAIRS],
        "jaccard_analysis": jaccard,
    }

    return per_example_json, jaccard_json


def main():
    out_dir = "/root/entrainment_gated_ft/lm_eval_clean/analysis"
    os.makedirs(out_dir, exist_ok=True)

    for benchmark in ["winogrande", "piqa"]:
        pe_json, jc_json = analyze_benchmark(benchmark)
        if pe_json:
            with open(os.path.join(out_dir, f"{benchmark}_per_example.json"), "w") as f:
                json.dump(pe_json, f, indent=2)
            print(f"Saved {benchmark}_per_example.json")
        if jc_json:
            with open(os.path.join(out_dir, f"{benchmark}_jaccard_analysis.json"), "w") as f:
                json.dump(jc_json, f, indent=2)
            print(f"Saved {benchmark}_jaccard_analysis.json")

    print("\nDONE")


if __name__ == "__main__":
    main()
