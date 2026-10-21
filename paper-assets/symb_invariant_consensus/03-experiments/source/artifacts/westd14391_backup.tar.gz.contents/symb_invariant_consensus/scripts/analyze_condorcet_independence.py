import json
import os
import math
import sys
from collections import Counter
from pathlib import Path

RESULTS_DIR = Path("/root/symb_invariant_consensus/results")
VALID_ANSWERS = {"True", "False", "Unknown"}

MODELS = {
    "Mistral-7B": RESULTS_DIR / "exp033_mistral_7b_folio204" / "intermediates",
    "Qwen2.5-14B": RESULTS_DIR / "folio_204_14b" / "intermediates",
}

def load_problems(intermediates_dir, n=204):
    problems = []
    for i in range(n):
        fpath = intermediates_dir / f"folio_{i}.json"
        if not fpath.exists():
            continue
        with open(fpath) as f:
            data = json.load(f)
        sr = data["sica_result"]
        gt = data["problem"]["answer"]
        answers = [t["answer"] for t in sr["traces"] if t["answer"] in VALID_ANSWERS]
        problems.append({
            "problem_id": i,
            "ground_truth": gt,
            "answers": answers,
            "K": len(answers),
        })
    return problems

def compute_problem_metrics(prob):
    answers = prob["answers"]
    K = prob["K"]
    if K < 2:
        return None
    counts = Counter(answers)
    n_vals = list(counts.values())

    # Observed pairwise agreement: fraction of pairs that agree
    agree_pairs = sum(n * (n - 1) for n in n_vals)
    total_pairs = K * (K - 1)
    observed_agreement = agree_pairs / total_pairs

    # Plug-in expected agreement: sum(freq_i^2)
    marginal_concentration = sum((n / K) ** 2 for n in n_vals)

    # Raw violation (user's metric)
    violation_raw = observed_agreement - marginal_concentration

    # Entropy of answer distribution
    entropy = -sum((n / K) * math.log2(n / K) for n in n_vals if n > 0)

    # SC majority answer and correctness
    majority = counts.most_common(1)[0][0]
    sc_correct = int(majority == prob["ground_truth"])
    majority_frac = counts.most_common(1)[0][1] / K

    return {
        "problem_id": prob["problem_id"],
        "K": K,
        "ground_truth": prob["ground_truth"],
        "answer_distribution": dict(counts),
        "majority_answer": majority,
        "sc_correct": sc_correct,
        "majority_fraction": round(majority_frac, 4),
        "observed_agreement": round(observed_agreement, 6),
        "marginal_concentration": round(marginal_concentration, 6),
        "violation_raw": round(violation_raw, 6),
        "entropy": round(entropy, 4),
    }

def fleiss_kappa(all_metrics):
    """Compute Fleiss' Kappa across all problems.
    Uses GLOBAL marginals as the 'chance' baseline."""
    # Collect all answer counts
    global_counts = Counter()
    total_traces = 0
    for m in all_metrics:
        for ans, cnt in m["answer_distribution"].items():
            global_counts[ans] += cnt
        total_traces += m["K"]

    # Global marginal proportions
    p_global = {ans: cnt / total_traces for ans, cnt in global_counts.items()}
    P_e = sum(p ** 2 for p in p_global.values())

    # Mean observed agreement
    P_bar = sum(m["observed_agreement"] for m in all_metrics) / len(all_metrics)

    if abs(1 - P_e) < 1e-10:
        kappa = 1.0
    else:
        kappa = (P_bar - P_e) / (1 - P_e)

    return {
        "kappa": round(kappa, 4),
        "P_bar": round(P_bar, 4),
        "P_e": round(P_e, 4),
        "global_marginals": {k: round(v, 4) for k, v in p_global.items()},
        "total_traces": total_traces,
    }

def effective_K(kappa_val, K_nominal):
    """Effective number of independent traces given ICC ~ kappa."""
    if kappa_val <= 0:
        return K_nominal
    return K_nominal / (1 + (K_nominal - 1) * kappa_val)

def bin_by_entropy(all_metrics, n_bins=3):
    """Split problems into low/medium/high entropy bins."""
    entropies = [m["entropy"] for m in all_metrics]
    sorted_e = sorted(entropies)
    n = len(sorted_e)
    thresholds = [sorted_e[n // 3], sorted_e[2 * n // 3]]

    bins = {"low": [], "medium": [], "high": []}
    for m in all_metrics:
        if m["entropy"] <= thresholds[0]:
            bins["low"].append(m)
        elif m["entropy"] <= thresholds[1]:
            bins["medium"].append(m)
        else:
            bins["high"].append(m)
    return bins, thresholds

def summarize(metrics_list):
    if not metrics_list:
        return {}
    n = len(metrics_list)
    keys = ["observed_agreement", "marginal_concentration", "violation_raw", "entropy"]
    summary = {"n": n}
    for k in keys:
        vals = [m[k] for m in metrics_list]
        mean_v = sum(vals) / n
        sorted_v = sorted(vals)
        median_v = sorted_v[n // 2]
        std_v = (sum((v - mean_v) ** 2 for v in vals) / n) ** 0.5
        summary[k] = {
            "mean": round(mean_v, 4),
            "median": round(median_v, 4),
            "std": round(std_v, 4),
        }
    sc_acc = sum(m["sc_correct"] for m in metrics_list) / n
    summary["sc_accuracy"] = round(sc_acc, 4)
    return summary


def main():
    all_results = {}

    for model_name, intermed_dir in MODELS.items():
        print(f"\n{'='*60}")
        print(f"Processing: {model_name}")
        print(f"  Dir: {intermed_dir}")
        if not intermed_dir.exists():
            print(f"  WARNING: directory not found, skipping")
            continue

        problems = load_problems(intermed_dir)
        print(f"  Loaded {len(problems)} problems")

        all_metrics = []
        for p in problems:
            m = compute_problem_metrics(p)
            if m is not None:
                all_metrics.append(m)

        print(f"  Valid problems (K>=2): {len(all_metrics)}")

        # Overall Fleiss' Kappa
        fk = fleiss_kappa(all_metrics)
        K_nom = int(round(sum(m["K"] for m in all_metrics) / len(all_metrics)))
        K_eff = effective_K(fk["kappa"], K_nom)

        # Summary stats
        overall_summary = summarize(all_metrics)

        # Entropy bins
        bins, thresholds = bin_by_entropy(all_metrics)
        bin_summaries = {}
        for bname, bmetrics in bins.items():
            bin_summaries[bname] = summarize(bmetrics)
            if bmetrics:
                bfk = fleiss_kappa(bmetrics)
                bin_summaries[bname]["fleiss_kappa"] = bfk["kappa"]
                bin_summaries[bname]["effective_K"] = round(
                    effective_K(bfk["kappa"], K_nom), 2
                )

        model_result = {
            "model": model_name,
            "n_problems": len(all_metrics),
            "K_nominal": K_nom,
            "fleiss_kappa": fk,
            "effective_K": round(K_eff, 2),
            "overall_summary": overall_summary,
            "entropy_bins": bin_summaries,
            "entropy_thresholds": [round(t, 4) for t in thresholds],
            "per_problem": all_metrics,
        }
        all_results[model_name] = model_result

        # Print summary table
        s = overall_summary
        print(f"\n  Overall Summary:")
        print(f"    SC Accuracy:            {s['sc_accuracy']:.4f}")
        print(f"    Fleiss' Kappa:           {fk['kappa']:.4f}")
        print(f"    Global Marginals:        {fk['global_marginals']}")
        print(f"    P_bar (mean agreement):  {fk['P_bar']:.4f}")
        print(f"    P_e (chance agreement):  {fk['P_e']:.4f}")
        print(f"    Effective K (of {K_nom}):     {K_eff:.2f}")
        print(f"    Mean Observed Agreement: {s['observed_agreement']['mean']:.4f}")
        print(f"    Mean Marginal Conc.:     {s['marginal_concentration']['mean']:.4f}")
        print(f"    Mean Violation (raw):    {s['violation_raw']['mean']:.4f}")
        print(f"    Mean Entropy:            {s['entropy']['mean']:.4f}")

        print(f"\n  Per Entropy Bin (thresholds: {thresholds[0]:.3f}, {thresholds[1]:.3f}):")
        print(f"  {'Bin':<8} {'n':>4} {'SC Acc':>8} {'Agreement':>10} {'Marg Conc':>10} {'Violation':>10} {'Kappa':>8} {'Eff K':>7}")
        for bname in ["low", "medium", "high"]:
            bs = bin_summaries[bname]
            if not bs:
                continue
            print(f"  {bname:<8} {bs['n']:>4} {bs['sc_accuracy']:>8.4f} "
                  f"{bs['observed_agreement']['mean']:>10.4f} "
                  f"{bs['marginal_concentration']['mean']:>10.4f} "
                  f"{bs['violation_raw']['mean']:>10.4f} "
                  f"{bs.get('fleiss_kappa', 0):>8.4f} "
                  f"{bs.get('effective_K', 0):>7.2f}")

    # Cross-model comparison table
    print(f"\n\n{'='*60}")
    print("Cross-Model Comparison")
    print(f"{'='*60}")
    header = f"{'Model':<15} {'n':>4} {'SC Acc':>8} {'Agreement':>10} {'Expected':>10} {'Violation':>10} {'Kappa':>8} {'Eff K':>7}"
    print(header)
    print("-" * len(header))
    for mname, mr in all_results.items():
        s = mr["overall_summary"]
        fk = mr["fleiss_kappa"]
        print(f"{mname:<15} {mr['n_problems']:>4} {s['sc_accuracy']:>8.4f} "
              f"{s['observed_agreement']['mean']:>10.4f} "
              f"{s['marginal_concentration']['mean']:>10.4f} "
              f"{s['violation_raw']['mean']:>10.4f} "
              f"{fk['kappa']:>8.4f} "
              f"{mr['effective_K']:>7.2f}")

    print(f"\nPer Entropy Bin:")
    header2 = f"{'Model':<15} {'Bin':<8} {'n':>4} {'SC Acc':>8} {'Agreement':>10} {'Expected':>10} {'Violation':>10} {'Kappa':>8} {'Eff K':>7}"
    print(header2)
    print("-" * len(header2))
    for mname, mr in all_results.items():
        for bname in ["low", "medium", "high"]:
            bs = mr["entropy_bins"][bname]
            if not bs:
                continue
            print(f"{mname:<15} {bname:<8} {bs['n']:>4} {bs['sc_accuracy']:>8.4f} "
                  f"{bs['observed_agreement']['mean']:>10.4f} "
                  f"{bs['marginal_concentration']['mean']:>10.4f} "
                  f"{bs['violation_raw']['mean']:>10.4f} "
                  f"{bs.get('fleiss_kappa', 0):>8.4f} "
                  f"{bs.get('effective_K', 0):>7.2f}")

    # Save results
    out_path = RESULTS_DIR / "condorcet_independence_analysis.json"
    # Remove per_problem for the saved file to keep it manageable, save separately
    save_results = {}
    for mname, mr in all_results.items():
        save_copy = {k: v for k, v in mr.items() if k != "per_problem"}
        save_results[mname] = save_copy

    save_results["_per_problem"] = {
        mname: mr["per_problem"] for mname, mr in all_results.items()
    }

    with open(out_path, "w") as f:
        json.dump(save_results, f, indent=2)
    print(f"\nResults saved to {out_path}")

if __name__ == "__main__":
    main()
