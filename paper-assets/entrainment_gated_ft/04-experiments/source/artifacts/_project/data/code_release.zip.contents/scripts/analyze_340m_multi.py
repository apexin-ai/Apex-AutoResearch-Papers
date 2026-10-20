#!/usr/bin/env python3
"""Per-example multiplicity analysis for 340M multi-benchmark (HellaSwag, PIQA, ARC-Easy).
Computes alpha, pairwise Jaccard, convergence rho with exact permutation test.
Also loads 1.3B data for scale comparison."""
import json, os, itertools
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVAL_BASE_340M = os.path.join(PROJECT_ROOT, "lm_eval_clean", "340m_multi")
EVAL_BASE_1_3B = os.path.join(PROJECT_ROOT, "lm_eval_clean")
OUT_DIR = os.path.join(PROJECT_ROOT, "lm_eval_clean", "analysis")

ARCHS = ["GDN", "RetNet", "HGRN2"]
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
HYBRID_RATIOS = ["h24-1", "h12-1", "h6-1", "h3-1"]
ARCH_PAIRS = [("GDN", "RetNet"), ("GDN", "HGRN2"), ("RetNet", "HGRN2")]
N_PERM_JACCARD = 1000
np.random.seed(42)

BENCHMARKS = {
    "hellaswag": {"metric": "acc_norm", "task_file": "hellaswag.jsonl"},
    "piqa": {"metric": "acc", "task_file": "piqa.jsonl"},
    "arc_easy": {"metric": "acc", "task_file": "arc_easy.jsonl"},
}

MODEL_NAME_340M = {
    ("GDN", "pure"): "GDN-pure",
    ("GDN", "h24-1"): "GDN-h24-1",
    ("GDN", "h12-1"): "GDN-h12-1",
    ("GDN", "h6-1"): "GDN-h6-1",
    ("GDN", "h3-1"): "GDN-h3-1",
    ("RetNet", "pure"): "RetNet-pure",
    ("RetNet", "h24-1"): "RetNet-h24-1",
    ("RetNet", "h12-1"): "RetNet-h12-1",
    ("RetNet", "h6-1"): "RetNet-h6-1",
    ("RetNet", "h3-1"): "RetNet-h3-1",
    ("HGRN2", "pure"): "HGRN2-pure",
    ("HGRN2", "h24-1"): "HGRN2-h24-1",
    ("HGRN2", "h12-1"): "HGRN2-h12-1",
    ("HGRN2", "h6-1"): "HGRN2-h6-1",
    ("HGRN2", "h3-1"): "HGRN2-h3-1",
}

ARCH_PREFIXES_1_3B = {
    "GDN": "1.3B-100B-GatedDeltaNet",
    "RetNet": "1.3B-100B-RetNet",
    "HGRN2": "1.3B-100B-HGRN2",
}
RATIO_SUFFIXES_1_3B = {
    "pure": "-pure",
    "h24-1": "-hybrid-24-1",
    "h12-1": "-hybrid-12-1",
    "h6-1": "-hybrid-6-1",
    "h3-1": "-hybrid-3-1",
}

BENCHMARK_DIR_1_3B = {
    "hellaswag": "hellaswag",
    "piqa": "piqa",
    "arc_easy": "arc_easy",
}


def load_samples_340m(benchmark, arch, ratio):
    cfg = BENCHMARKS[benchmark]
    model_dir = MODEL_NAME_340M[(arch, ratio)]
    path = os.path.join(EVAL_BASE_340M, model_dir, "samples", cfg["task_file"])
    metric = cfg["metric"]
    results = {}
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            results[row["doc_id"]] = int(round(float(row[metric])))
    return results


def load_samples_1_3b(benchmark, arch, ratio):
    cfg = BENCHMARKS[benchmark]
    model_name = ARCH_PREFIXES_1_3B[arch] + RATIO_SUFFIXES_1_3B[ratio]
    bm_dir = BENCHMARK_DIR_1_3B[benchmark]
    path = os.path.join(EVAL_BASE_1_3B, bm_dir, model_name, "samples", f"{bm_dir}.jsonl")
    metric = cfg["metric"]
    results = {}
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            results[row["doc_id"]] = int(round(float(row[metric])))
    return results


def exact_spearman_p(x, y):
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


def analyze_benchmark(benchmark, loader_fn, label="340M"):
    print(f"\n{'='*60}")
    print(f"Analyzing {benchmark} ({label})")
    print(f"{'='*60}")

    all_preds = {}
    for arch in ARCHS:
        all_preds[arch] = {}
        for ratio in RATIOS:
            preds = loader_fn(benchmark, arch, ratio)
            nc = sum(1 for v in preds.values() if v == 1)
            print(f"  {arch} {ratio}: {len(preds)} samples, acc={nc/len(preds):.4f}")
            all_preds[arch][ratio] = preds

    doc_ids = set()
    for arch in ARCHS:
        for ratio in RATIOS:
            doc_ids.update(all_preds[arch][ratio].keys())
    n_samples = max(doc_ids) + 1
    print(f"n_samples = {n_samples}")

    # A) Ambiguity alpha
    print("\n--- Ambiguity alpha ---")
    ambiguity = {}

    # All 15 models
    for ratio in RATIOS:
        n_ambiguous = 0
        total_valid = 0
        for d in range(n_samples):
            vals = [all_preds[arch][ratio].get(d) for arch in ARCHS]
            vals = [v for v in vals if v is not None]
            if len(vals) < 2:
                continue
            total_valid += 1
            if len(set(vals)) > 1:
                n_ambiguous += 1
        alpha = n_ambiguous / total_valid if total_valid > 0 else 0
        ambiguity[f"per_ratio_{ratio}"] = round(alpha, 6)
        print(f"  per_ratio {ratio}: alpha={alpha:.4f} ({n_ambiguous}/{total_valid})")

    # Alpha across ALL 15 models
    n_ambiguous_all = 0
    total_valid_all = 0
    for d in range(n_samples):
        vals = []
        for arch in ARCHS:
            for ratio in RATIOS:
                v = all_preds[arch][ratio].get(d)
                if v is not None:
                    vals.append(v)
        if len(vals) < 2:
            continue
        total_valid_all += 1
        if len(set(vals)) > 1:
            n_ambiguous_all += 1
    alpha_all = n_ambiguous_all / total_valid_all if total_valid_all > 0 else 0
    ambiguity["alpha_all_15"] = round(alpha_all, 6)
    print(f"  ALL 15 models: alpha={alpha_all:.4f} ({n_ambiguous_all}/{total_valid_all})")

    # Pure-only alpha (3 pure models)
    n_ambiguous_pure = 0
    total_valid_pure = 0
    for d in range(n_samples):
        vals = [all_preds[arch]["pure"].get(d) for arch in ARCHS]
        vals = [v for v in vals if v is not None]
        if len(vals) < 2:
            continue
        total_valid_pure += 1
        if len(set(vals)) > 1:
            n_ambiguous_pure += 1
    alpha_pure = n_ambiguous_pure / total_valid_pure if total_valid_pure > 0 else 0
    ambiguity["alpha_pure_only"] = round(alpha_pure, 6)
    print(f"  Pure-only (3 models): alpha={alpha_pure:.4f} ({n_ambiguous_pure}/{total_valid_pure})")

    # B) Per-example classification (helped/hurt)
    per_example = {}
    for arch in ARCHS:
        per_example[arch] = {}
        pure = all_preds[arch]["pure"]
        for ratio in HYBRID_RATIOS:
            hyb = all_preds[arch][ratio]
            h = sum(1 for d in range(n_samples) if pure.get(d) == 0 and hyb.get(d) == 1)
            r = sum(1 for d in range(n_samples) if pure.get(d) == 1 and hyb.get(d) == 0)
            per_example[arch][ratio] = {"n_helped": h, "n_hurt": r}

    # C) Convergence sigma + Spearman
    print("\n--- Convergence sigma ---")
    convergence = {}
    sigmas = []
    for ratio in RATIOS:
        accs_list = []
        for arch in ARCHS:
            preds = all_preds[arch][ratio]
            correct = sum(1 for v in preds.values() if v == 1)
            total_v = len(preds)
            accs_list.append(correct / total_v if total_v > 0 else 0)
        sigma = float(np.std(accs_list))
        sigmas.append(sigma)
        convergence[ratio] = {"sigma": round(sigma, 6), "accs": [round(a, 4) for a in accs_list]}
        print(f"  {ratio:5s}: sigma={sigma:.6f} accs={[f'{a:.4f}' for a in accs_list]}")

    attention_fracs = [0.0, 1/24, 1/12, 1/6, 1/3]
    rho, p_exact = exact_spearman_p(attention_fracs, sigmas)
    convergence["spearman"] = {
        "rho": round(rho, 4),
        "p_exact_two_tailed": round(p_exact, 4),
        "x_values": attention_fracs,
        "y_values": [round(s, 6) for s in sigmas],
    }
    print(f"  Spearman rho={rho:.4f}, p_exact={p_exact:.4f}")

    # D) Cross-architecture Jaccard
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

    # Compute mean Jaccard across all ratios and pairs
    all_j_helped = []
    all_j_hurt = []
    for ratio in HYBRID_RATIOS:
        for pair_name in jaccard_analysis[ratio]:
            all_j_helped.append(jaccard_analysis[ratio][pair_name]["helped"]["J"])
            all_j_hurt.append(jaccard_analysis[ratio][pair_name]["hurt"]["J"])
    jaccard_summary = {
        "mean_J_helped": round(float(np.mean(all_j_helped)), 4),
        "mean_J_hurt": round(float(np.mean(all_j_hurt)), 4),
    }

    result = {
        "benchmark": benchmark,
        "scale": label,
        "metric_used": BENCHMARKS[benchmark]["metric"],
        "n_samples": n_samples,
        "ambiguity": ambiguity,
        "convergence_sigma": convergence,
        "per_example_classification": per_example,
        "jaccard_analysis": jaccard_analysis,
        "jaccard_summary": jaccard_summary,
    }
    return result


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results_340m = {}
    results_1_3b = {}

    for bm in BENCHMARKS:
        print(f"\n\n{'#'*70}")
        print(f"# BENCHMARK: {bm}")
        print(f"{'#'*70}")
        results_340m[bm] = analyze_benchmark(bm, load_samples_340m, "340M")
        results_1_3b[bm] = analyze_benchmark(bm, load_samples_1_3b, "1.3B")

    # Scale comparison table
    scale_comparison = {}
    for bm in BENCHMARKS:
        a340 = results_340m[bm]["ambiguity"]["alpha_all_15"]
        a13b = results_1_3b[bm]["ambiguity"]["alpha_all_15"]
        ap340 = results_340m[bm]["ambiguity"]["alpha_pure_only"]
        ap13b = results_1_3b[bm]["ambiguity"]["alpha_pure_only"]
        rho340 = results_340m[bm]["convergence_sigma"]["spearman"]["rho"]
        p340 = results_340m[bm]["convergence_sigma"]["spearman"]["p_exact_two_tailed"]
        rho13b = results_1_3b[bm]["convergence_sigma"]["spearman"]["rho"]
        p13b = results_1_3b[bm]["convergence_sigma"]["spearman"]["p_exact_two_tailed"]
        jh340 = results_340m[bm]["jaccard_summary"]["mean_J_helped"]
        jh13b = results_1_3b[bm]["jaccard_summary"]["mean_J_helped"]
        jr340 = results_340m[bm]["jaccard_summary"]["mean_J_hurt"]
        jr13b = results_1_3b[bm]["jaccard_summary"]["mean_J_hurt"]
        scale_comparison[bm] = {
            "340M_alpha_all": a340,
            "1.3B_alpha_all": a13b,
            "delta_alpha_all": round(a340 - a13b, 6),
            "340M_alpha_pure": ap340,
            "1.3B_alpha_pure": ap13b,
            "delta_alpha_pure": round(ap340 - ap13b, 6),
            "340M_convergence_rho": rho340,
            "340M_convergence_p": p340,
            "1.3B_convergence_rho": rho13b,
            "1.3B_convergence_p": p13b,
            "340M_mean_J_helped": jh340,
            "1.3B_mean_J_helped": jh13b,
            "340M_mean_J_hurt": jr340,
            "1.3B_mean_J_hurt": jr13b,
        }

    # Determine conclusion
    deltas = [scale_comparison[bm]["delta_alpha_all"] for bm in BENCHMARKS]
    rhos_same_sign = all(
        (scale_comparison[bm]["340M_convergence_rho"] < 0) == (scale_comparison[bm]["1.3B_convergence_rho"] < 0)
        for bm in BENCHMARKS
    )
    max_delta = max(abs(d) for d in deltas)
    if max_delta < 0.05 and rhos_same_sign:
        conclusion = "scale_invariant"
    elif max_delta > 0.10:
        conclusion = "scale_dependent"
    else:
        conclusion = "mixed"

    final_output = {
        "scale_comparison": scale_comparison,
        "per_benchmark_340m": results_340m,
        "per_benchmark_1_3b": results_1_3b,
        "conclusion": conclusion,
        "summary": {
            "340M_mean_alpha": round(float(np.mean([scale_comparison[bm]["340M_alpha_all"] for bm in BENCHMARKS])), 4),
            "1.3B_mean_alpha": round(float(np.mean([scale_comparison[bm]["1.3B_alpha_all"] for bm in BENCHMARKS])), 4),
            "max_absolute_delta": round(max_delta, 4),
            "convergence_signs_consistent": rhos_same_sign,
        }
    }

    out_path = os.path.join(OUT_DIR, "340m_multi_bench_analysis.json")
    with open(out_path, "w") as f:
        json.dump(final_output, f, indent=2)
    print(f"\n\nSaved: {out_path}")

    # Print summary
    print("\n\n" + "="*70)
    print("SCALE COMPARISON SUMMARY")
    print("="*70)
    print(f"{'Benchmark':<12} {'340M α_all':<12} {'1.3B α_all':<12} {'Δ':<10} {'340M ρ':<10} {'1.3B ρ':<10}")
    print("-"*70)
    for bm in BENCHMARKS:
        sc = scale_comparison[bm]
        print(f"{bm:<12} {sc['340M_alpha_all']:<12.4f} {sc['1.3B_alpha_all']:<12.4f} {sc['delta_alpha_all']:<10.4f} {sc['340M_convergence_rho']:<10.4f} {sc['1.3B_convergence_rho']:<10.4f}")
    print(f"\nConclusion: {conclusion}")


if __name__ == "__main__":
    main()
