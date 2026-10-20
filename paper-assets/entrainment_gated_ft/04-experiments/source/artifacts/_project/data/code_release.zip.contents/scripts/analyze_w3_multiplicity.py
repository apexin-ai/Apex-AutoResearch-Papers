#!/usr/bin/env python3
"""Per-example multiplicity analysis for WinoGrande and PIQA."""
import json, os, itertools
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVAL_BASE = os.path.join(PROJECT_ROOT, "lm_eval_clean")
OUT_DIR = os.path.join(EVAL_BASE, "analysis")
ARCHS = ["GDN", "RetNet", "HGRN2"]
ARCH_PREFIXES = {
    "GDN": "1.3B-100B-GatedDeltaNet",
    "RetNet": "1.3B-100B-RetNet",
    "HGRN2": "1.3B-100B-HGRN2",
}
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
HYBRID_RATIOS = ["h24-1", "h12-1", "h6-1", "h3-1"]
RATIO_SUFFIXES = {
    "pure": "-pure",
    "h24-1": "-hybrid-24-1",
    "h12-1": "-hybrid-12-1",
    "h6-1": "-hybrid-6-1",
    "h3-1": "-hybrid-3-1",
}
ARCH_PAIRS = [("GDN", "RetNet"), ("GDN", "HGRN2"), ("RetNet", "HGRN2")]
N_PERM_JACCARD = 10000
np.random.seed(42)


def load_samples(benchmark, arch, ratio):
    model_name = ARCH_PREFIXES[arch] + RATIO_SUFFIXES[ratio]
    path = os.path.join(EVAL_BASE, benchmark, model_name, "samples", f"{benchmark}.jsonl")
    results = {}
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            results[row["doc_id"]] = int(round(float(row["acc"])))
    return results


def exact_spearman_p(x, y):
    """Exact two-tailed p-value for Spearman correlation with small n."""
    from scipy.stats import spearmanr
    n = len(x)
    observed_rho, _ = spearmanr(x, y)
    count = 0
    total = 0
    for perm in itertools.permutations(range(n)):
        y_perm = [y[i] for i in perm]
        rho, _ = spearmanr(x, y_perm)
        total += 1
        if abs(rho) >= abs(observed_rho):
            count += 1
    return float(observed_rho), count / total


def compute_jaccard(set_a, set_b, N):
    a, b = set(set_a), set(set_b)
    na, nb = len(a), len(b)
    intersection = len(a & b)
    union = len(a | b)
    J = intersection / union if union > 0 else 0.0
    ei = na * nb / N if N > 0 else 0
    eu = na + nb - ei
    J_null = ei / eu if eu > 0 else 0.0
    J_max = min(na, nb) / max(na, nb) if max(na, nb) > 0 else 0.0
    nES = (J - J_null) / (J_max - J_null) if abs(J_max - J_null) > 1e-10 else 0.0
    if na == 0 or nb == 0:
        p = 1.0
    else:
        count_ge = 0
        for _ in range(N_PERM_JACCARD):
            pa = set(np.random.choice(N, na, replace=False))
            pb = set(np.random.choice(N, nb, replace=False))
            pj = len(pa & pb) / len(pa | pb) if len(pa | pb) > 0 else 0
            if pj >= J - 1e-10:
                count_ge += 1
        p = count_ge / N_PERM_JACCARD
    return {
        "J": round(J, 4), "J_null": round(J_null, 4), "J_max": round(J_max, 4),
        "nES": round(nES, 4), "p": round(p, 4),
        "n_A": na, "n_B": nb, "n_intersection": intersection,
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
            nc = sum(1 for v in preds.values() if v == 1)
            print(f"  {arch} {ratio}: {len(preds)} samples, acc={nc/len(preds):.4f}")
            all_preds[arch][ratio] = preds

    n_samples = max(max(all_preds[a][r].keys()) for a in ARCHS for r in RATIOS) + 1
    print(f"n_samples = {n_samples}")

    # A) Per-example classification
    print("\n--- Per-example classification ---")
    per_example = {}
    for arch in ARCHS:
        per_example[arch] = {}
        pure = all_preds[arch]["pure"]
        for ratio in HYBRID_RATIOS:
            hyb = all_preds[arch][ratio]
            h = sum(1 for d in range(n_samples) if pure.get(d) == 0 and hyb.get(d) == 1)
            r = sum(1 for d in range(n_samples) if pure.get(d) == 1 and hyb.get(d) == 0)
            sr = sum(1 for d in range(n_samples) if pure.get(d) == 1 and hyb.get(d) == 1)
            sw = sum(1 for d in range(n_samples) if pure.get(d) == 0 and hyb.get(d) == 0)
            per_example[arch][ratio] = {
                "n_helped": h, "n_hurt": r,
                "n_stayed_right": sr, "n_stayed_wrong": sw,
                "net_effect": h - r
            }
            print(f"  {arch:6s} {ratio:5s}: helped={h:3d} hurt={r:3d} net={h-r:+d}")

    # B) Ambiguity alpha
    print("\n--- Ambiguity ---")
    ambiguity = {}
    for ratio in RATIOS:
        dist = {"0_of_3": 0, "1_of_3": 0, "2_of_3": 0, "3_of_3": 0}
        for d in range(n_samples):
            vals = [all_preds[arch][ratio].get(d) for arch in ARCHS]
            if None in vals:
                continue
            nc = sum(vals)
            dist[f"{nc}_of_3"] += 1
        total_valid = sum(dist.values())
        n_ambiguous = dist["1_of_3"] + dist["2_of_3"]
        alpha = n_ambiguous / total_valid if total_valid > 0 else 0
        ambiguity[ratio] = {
            "alpha": round(alpha, 6),
            "n_ambiguous": n_ambiguous,
            "disagreement_distribution": dist,
        }
        print(f"  {ratio:5s}: alpha={alpha:.4f} dist={dist}")

    # D) Convergence sigma
    print("\n--- Convergence sigma ---")
    convergence = {}
    sigmas = []
    for ratio in RATIOS:
        accs_list = []
        for arch in ARCHS:
            preds = all_preds[arch][ratio]
            correct = sum(1 for d in range(n_samples) if preds.get(d) == 1)
            total_v = sum(1 for d in range(n_samples) if preds.get(d) is not None)
            accs_list.append(correct / total_v if total_v > 0 else 0)
        sigma = float(np.std(accs_list))
        sigmas.append(sigma)
        n_unan_correct = n_unan_wrong = n_split = 0
        for d in range(n_samples):
            vals = [all_preds[arch][ratio].get(d) for arch in ARCHS]
            if None in vals:
                continue
            nc = sum(vals)
            if nc == 3:
                n_unan_correct += 1
            elif nc == 0:
                n_unan_wrong += 1
            else:
                n_split += 1
        convergence[ratio] = {
            "mean_sigma": round(sigma, 6),
            "n_unanimous_correct": n_unan_correct,
            "n_unanimous_wrong": n_unan_wrong,
            "n_split": n_split,
        }
        print(f"  {ratio:5s}: sigma={sigma:.6f} unan_right={n_unan_correct} unan_wrong={n_unan_wrong} split={n_split}")

    rho, p_exact = exact_spearman_p(list(range(5)), sigmas)
    convergence["spearman"] = {
        "rho": round(rho, 4),
        "p_exact_two_tailed": round(p_exact, 4),
        "n_permutations": 120,
    }
    print(f"  Spearman rho={rho:.4f}, p_exact={p_exact:.4f}")

    pe_json = {
        "benchmark": benchmark,
        "n_samples": n_samples,
        "architectures": ARCHS,
        "ratios": RATIOS,
        "per_example_classification": per_example,
        "convergence_sigma": convergence,
        "ambiguity": ambiguity,
    }

    # C) Cross-architecture Jaccard overlap
    print("\n--- Jaccard analysis ---")
    jaccard_analysis = {}
    for ratio in HYBRID_RATIOS:
        jaccard_analysis[ratio] = {}
        for a1, a2 in ARCH_PAIRS:
            pair_name = f"{a1}_vs_{a2}"
            pure_a1, hyb_a1 = all_preds[a1]["pure"], all_preds[a1][ratio]
            pure_a2, hyb_a2 = all_preds[a2]["pure"], all_preds[a2][ratio]
            helped_a1 = {d for d in range(n_samples) if pure_a1.get(d) == 0 and hyb_a1.get(d) == 1}
            hurt_a1 = {d for d in range(n_samples) if pure_a1.get(d) == 1 and hyb_a1.get(d) == 0}
            helped_a2 = {d for d in range(n_samples) if pure_a2.get(d) == 0 and hyb_a2.get(d) == 1}
            hurt_a2 = {d for d in range(n_samples) if pure_a2.get(d) == 1 and hyb_a2.get(d) == 0}
            j_helped = compute_jaccard(helped_a1, helped_a2, n_samples)
            j_hurt = compute_jaccard(hurt_a1, hurt_a2, n_samples)
            jaccard_analysis[ratio][pair_name] = {"helped": j_helped, "hurt": j_hurt}
            print(f"  {ratio:5s} {pair_name}: J_h={j_helped['J']:.4f}(p={j_helped['p']:.4f}) J_r={j_hurt['J']:.4f}(p={j_hurt['p']:.4f})")

    jc_json = {
        "benchmark": benchmark,
        "n_samples": n_samples,
        "jaccard_analysis": jaccard_analysis,
    }
    return pe_json, jc_json


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for benchmark in ["winogrande", "piqa"]:
        pe_json, jc_json = analyze_benchmark(benchmark)
        pe_path = os.path.join(OUT_DIR, f"{benchmark}_per_example.json")
        jc_path = os.path.join(OUT_DIR, f"{benchmark}_jaccard_analysis.json")
        with open(pe_path, "w") as f:
            json.dump(pe_json, f, indent=2)
        print(f"Saved {pe_path}")
        with open(jc_path, "w") as f:
            json.dump(jc_json, f, indent=2)
        print(f"Saved {jc_path}")
    print("\nDONE")


if __name__ == "__main__":
    main()
