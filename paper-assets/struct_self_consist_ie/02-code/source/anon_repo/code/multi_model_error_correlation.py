"""Multi-model error correlation analysis for cross-model ensemble.

Analyzes per-instance entity F1 correlation between Qwen3-8B-FT and
LLaMA-3.1-8B-Instruct across SciERC, CoNLL, and FewNERD. Tests whether
cross-family models have lower error correlation, explaining why
cross-model ensemble yields +0.42pp improvement.

Outputs:
  - Correlation matrix (Pearson + Spearman) per dataset
  - Instance-level agreement breakdown (both-correct / both-wrong / disagree)
  - Entity-level ensemble simulation (union / intersection)
  - JSON report
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

BASE_DIR = Path("/root/autodl-tmp/struct_self_consist_ie")

DATA_CONFIGS = {
    "SciERC": {
        "Qwen3-8B-FT": "output/exp_001_seed42_v2/samples.jsonl",
        "LLaMA-3.1-8B": "output/exp_007_llama_n16/samples.jsonl",
    },
    "CoNLL": {
        "Qwen3-8B-FT": "output/exp_002_conll_n16/samples.jsonl",
        "LLaMA-3.1-8B": "output/exp_017_llama_conll_n16/samples.jsonl",
    },
    "FewNERD": {
        "Qwen3-8B-FT": "output/exp_027_fewnerd_n16/samples.jsonl",
        "LLaMA-3.1-8B": "output/llama_fewnerd_s42/samples.jsonl",
    },
}

MODEL_FAMILY = {
    "Qwen3-8B-FT": "Qwen",
    "LLaMA-3.1-8B": "Meta",
}


def load_samples(path):
    data = {}
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            data[d["id"]] = d
    return data


def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def compute_instance_f1(pred_entities, gold_entities):
    pred = entity_set(pred_entities)
    gold = entity_set(gold_entities)
    if not gold and not pred:
        return 1.0
    if not gold or not pred:
        return 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return 2 * p * r / (p + r)


def compute_prf(pred, gold):
    if not gold and not pred:
        return 1.0, 1.0, 1.0
    if not pred:
        return 0.0, 0.0, 0.0
    if not gold:
        return 0.0, 0.0, 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    f1 = 2 * p * r / (p + r)
    return p, r, f1


def majority_vote_entities(samples, threshold=0.5):
    N = len(samples)
    entity_votes = defaultdict(int)
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_votes[key] += 1
                seen.add(key)
    result = []
    for (start, end, etype), count in entity_votes.items():
        if count / N > threshold:
            result.append({"start": start, "end": end, "type": etype})
    return result


def analyze_dataset(dataset_name, model_paths):
    model_names = list(model_paths.keys())
    model_data = {}
    for mname, path in model_paths.items():
        full_path = BASE_DIR / path
        if not full_path.exists():
            print(f"  WARNING: {full_path} not found, skipping {mname}")
            continue
        model_data[mname] = load_samples(str(full_path))
        print(f"  {mname}: {len(model_data[mname])} instances loaded")

    if len(model_data) < 2:
        return {"error": "insufficient models"}

    common_ids = set.intersection(*[set(d.keys()) for d in model_data.values()])
    common_ids = sorted(common_ids)
    print(f"  Common instances: {len(common_ids)}")

    if len(common_ids) == 0:
        return {"error": "no common instances"}

    greedy_f1 = {m: [] for m in model_names}
    sc_f1 = {m: [] for m in model_names}

    for iid in common_ids:
        for m in model_names:
            inst = model_data[m][iid]
            gold_ents = inst["gold"]["entities"]
            greedy_ents = inst["greedy"]["entities"]
            greedy_f1[m].append(compute_instance_f1(greedy_ents, gold_ents))
            sc_ents = majority_vote_entities(inst["samples"])
            sc_f1[m].append(compute_instance_f1(sc_ents, gold_ents))

    greedy_f1 = {m: np.array(v) for m, v in greedy_f1.items()}
    sc_f1 = {m: np.array(v) for m, v in sc_f1.items()}

    m1, m2 = model_names[0], model_names[1]

    def corr_stats(arr1, arr2):
        pearson_r, pearson_p = stats.pearsonr(arr1, arr2)
        spearman_r, spearman_p = stats.spearmanr(arr1, arr2)
        return {
            "pearson_r": round(float(pearson_r), 4),
            "pearson_p": round(float(pearson_p), 6),
            "spearman_r": round(float(spearman_r), 4),
            "spearman_p": round(float(spearman_p), 6),
        }

    greedy_corr = corr_stats(greedy_f1[m1], greedy_f1[m2])
    sc_corr = corr_stats(sc_f1[m1], sc_f1[m2])

    greedy_err = {m: 1 - greedy_f1[m] for m in model_names}
    error_corr = corr_stats(greedy_err[m1], greedy_err[m2])

    PERFECT = 0.999
    both_perfect = 0
    both_imperfect = 0
    m1_better = 0
    m2_better = 0
    both_zero = 0

    for i in range(len(common_ids)):
        f1_1 = greedy_f1[m1][i]
        f1_2 = greedy_f1[m2][i]
        if f1_1 >= PERFECT and f1_2 >= PERFECT:
            both_perfect += 1
        elif f1_1 < PERFECT and f1_2 < PERFECT:
            both_imperfect += 1
            if f1_1 == 0 and f1_2 == 0:
                both_zero += 1
        elif f1_1 >= PERFECT:
            m1_better += 1
        else:
            m2_better += 1

    n = len(common_ids)
    agreement = {
        "n_instances": n,
        "both_perfect": both_perfect,
        "both_perfect_pct": round(100 * both_perfect / n, 1),
        "both_imperfect": both_imperfect,
        "both_imperfect_pct": round(100 * both_imperfect / n, 1),
        "both_zero": both_zero,
        m1 + "_only_perfect": m1_better,
        m1 + "_only_perfect_pct": round(100 * m1_better / n, 1),
        m2 + "_only_perfect": m2_better,
        m2 + "_only_perfect_pct": round(100 * m2_better / n, 1),
        "disagree_total": m1_better + m2_better,
        "disagree_pct": round(100 * (m1_better + m2_better) / n, 1),
    }

    model_perf = {}
    for m in model_names:
        total_tp, total_fp, total_fn = 0, 0, 0
        for iid in common_ids:
            inst = model_data[m][iid]
            pred = entity_set(inst["greedy"]["entities"])
            gold = entity_set(inst["gold"]["entities"])
            tp = len(pred & gold)
            total_tp += tp
            total_fp += len(pred) - tp
            total_fn += len(gold) - tp
        micro_p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
        micro_r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
        micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0
        model_perf[m] = {
            "micro_p": round(micro_p * 100, 2),
            "micro_r": round(micro_r * 100, 2),
            "micro_f1": round(micro_f1 * 100, 2),
            "macro_f1": round(float(np.mean(greedy_f1[m])) * 100, 2),
        }

    ensemble_results = {}
    for strategy in ["union", "intersection"]:
        total_tp, total_fp, total_fn = 0, 0, 0
        per_inst_f1 = []
        for iid in common_ids:
            gold = entity_set(model_data[m1][iid]["gold"]["entities"])
            pred1 = entity_set(model_data[m1][iid]["greedy"]["entities"])
            pred2 = entity_set(model_data[m2][iid]["greedy"]["entities"])
            if strategy == "union":
                pred = pred1 | pred2
            else:
                pred = pred1 & pred2
            tp = len(pred & gold)
            total_tp += tp
            total_fp += len(pred) - tp
            total_fn += len(gold) - tp
            _, _, f1 = compute_prf(pred, gold)
            per_inst_f1.append(f1)
        micro_p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
        micro_r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
        micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0
        ensemble_results[strategy] = {
            "micro_p": round(micro_p * 100, 2),
            "micro_r": round(micro_r * 100, 2),
            "micro_f1": round(micro_f1 * 100, 2),
            "macro_f1": round(float(np.mean(per_inst_f1)) * 100, 2),
        }

    sc_ensemble_f1_list = []
    total_tp, total_fp, total_fn = 0, 0, 0
    for iid in common_ids:
        gold_ents = model_data[m1][iid]["gold"]["entities"]
        gold = entity_set(gold_ents)
        merged_samples = model_data[m1][iid]["samples"] + model_data[m2][iid]["samples"]
        merged_ents = majority_vote_entities(merged_samples)
        pred = entity_set(merged_ents)
        tp = len(pred & gold)
        total_tp += tp
        total_fp += len(pred) - tp
        total_fn += len(gold) - tp
        _, _, f1 = compute_prf(pred, gold)
        sc_ensemble_f1_list.append(f1)
    micro_p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    micro_r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0
    ensemble_results["sc_merged_vote"] = {
        "micro_p": round(micro_p * 100, 2),
        "micro_r": round(micro_r * 100, 2),
        "micro_f1": round(micro_f1 * 100, 2),
        "macro_f1": round(float(np.mean(sc_ensemble_f1_list)) * 100, 2),
    }

    type_errors = {m: defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0}) for m in model_names}
    for iid in common_ids:
        gold_ents = model_data[m1][iid]["gold"]["entities"]
        gold = entity_set(gold_ents)
        for m in model_names:
            pred = entity_set(model_data[m][iid]["greedy"]["entities"])
            tp_set = pred & gold
            fp_set = pred - gold
            fn_set = gold - pred
            for s, e, t in tp_set:
                type_errors[m][t]["tp"] += 1
            for s, e, t in fp_set:
                type_errors[m][t]["fp"] += 1
            for s, e, t in fn_set:
                type_errors[m][t]["fn"] += 1

    type_f1 = {}
    all_types = set()
    for m in model_names:
        all_types.update(type_errors[m].keys())
    for t in sorted(all_types):
        type_f1[t] = {}
        for m in model_names:
            te = type_errors[m][t]
            tp = te["tp"]
            p = tp / (tp + te["fp"]) if (tp + te["fp"]) > 0 else 0
            r = tp / (tp + te["fn"]) if (tp + te["fn"]) > 0 else 0
            f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0
            type_f1[t][m] = round(f1 * 100, 2)

    return {
        "dataset": dataset_name,
        "n_common": len(common_ids),
        "models": model_names,
        "model_performance": model_perf,
        "correlation": {
            "greedy_f1": greedy_corr,
            "sc_f1": sc_corr,
            "greedy_error": error_corr,
        },
        "agreement": agreement,
        "ensemble": ensemble_results,
        "per_type_f1": type_f1,
    }


def print_report(results):
    print("\n" + "=" * 80)
    print("MULTI-MODEL ERROR CORRELATION ANALYSIS")
    print("=" * 80)

    for r in results:
        if "error" in r:
            print("\n%s: %s" % (r.get("dataset", "?"), r["error"]))
            continue

        ds = r["dataset"]
        m1, m2 = r["models"]
        print("\n" + "-" * 80)
        print("Dataset: %s  (%d instances)" % (ds, r["n_common"]))
        print("-" * 80)

        print("\n  Model Performance (greedy, micro-F1):")
        for m in r["models"]:
            mp = r["model_performance"][m]
            print("    %-20s: P=%.2f  R=%.2f  F1=%.2f" % (m, mp["micro_p"], mp["micro_r"], mp["micro_f1"]))

        print("\n  Correlation (%s vs %s):" % (m1, m2))
        for metric, label in [("greedy_f1", "Greedy F1"), ("sc_f1", "SC F1"), ("greedy_error", "Error(1-F1)")]:
            c = r["correlation"][metric]
            print("    %-15s: Pearson r=%.4f (p=%.2e)  Spearman rho=%.4f (p=%.2e)" % (
                label, c["pearson_r"], c["pearson_p"], c["spearman_r"], c["spearman_p"]))

        a = r["agreement"]
        print("\n  Instance Agreement (greedy, F1=1.0 threshold):")
        print("    Both perfect:      %5d  (%.1f%%)" % (a["both_perfect"], a["both_perfect_pct"]))
        print("    Both imperfect:    %5d  (%.1f%%)" % (a["both_imperfect"], a["both_imperfect_pct"]))
        print("      of which F1=0:   %5d" % a["both_zero"])
        print("    %s only perfect: %5d  (%.1f%%)" % (m1, a[m1+"_only_perfect"], a[m1+"_only_perfect_pct"]))
        print("    %s only perfect: %5d  (%.1f%%)" % (m2, a[m2+"_only_perfect"], a[m2+"_only_perfect_pct"]))
        print("    Disagree total:    %5d  (%.1f%%)" % (a["disagree_total"], a["disagree_pct"]))

        print("\n  Ensemble Simulation (micro-F1):")
        best_single = max(r["model_performance"][m]["micro_f1"] for m in r["models"])
        for strat, label in [("union", "Union (high recall)"), ("intersection", "Intersection (high prec)"),
                             ("sc_merged_vote", "SC merged vote")]:
            e = r["ensemble"][strat]
            delta = e["micro_f1"] - best_single
            sign = "+" if delta >= 0 else ""
            print("    %-30s: P=%.2f  R=%.2f  F1=%.2f  (%s%.2f vs best single)" % (
                label, e["micro_p"], e["micro_r"], e["micro_f1"], sign, delta))

        print("\n  Per-Type F1 (top-10 types):")
        type_items = sorted(r["per_type_f1"].items(),
                            key=lambda x: max(x[1].values()), reverse=True)[:10]
        header = "    %-30s" % "Type"
        for m in r["models"]:
            header += "  %15s" % m
        header += "  %8s" % "Delta"
        print(header)
        for t, mf1 in type_items:
            row = "    %-30s" % t
            vals = []
            for m in r["models"]:
                v = mf1.get(m, 0)
                vals.append(v)
                row += "  %15.2f" % v
            row += "  %8.2f" % abs(vals[0] - vals[1])
            print(row)

    print("\n" + "=" * 80)
    print("CROSS-DATASET SUMMARY")
    print("=" * 80)

    valid = [r for r in results if "error" not in r]
    if valid:
        print("\n  %-12s %10s %10s %10s %12s %10s %12s" % (
            "Dataset", "Pearson r", "Spearman r", "Disagree%", "Best Single", "Union F1", "SC-Merge F1"))
        for r in valid:
            c = r["correlation"]["greedy_f1"]
            a = r["agreement"]
            best = max(r["model_performance"][m]["micro_f1"] for m in r["models"])
            union_f1 = r["ensemble"]["union"]["micro_f1"]
            sc_merge = r["ensemble"]["sc_merged_vote"]["micro_f1"]
            print("  %-12s %10.4f %10.4f %9.1f%% %12.2f %10.2f %12.2f" % (
                r["dataset"], c["pearson_r"], c["spearman_r"], a["disagree_pct"], best, union_f1, sc_merge))

        all_pearson = [r["correlation"]["greedy_f1"]["pearson_r"] for r in valid]
        all_disagree = [r["agreement"]["disagree_pct"] for r in valid]
        print("\n  Mean Pearson r: %.4f" % np.mean(all_pearson))
        print("  Mean disagree%%: %.1f%%" % np.mean(all_disagree))

    print("\n" + "-" * 80)
    print("HYPOTHESIS ASSESSMENT")
    print("-" * 80)
    if valid:
        avg_pearson = np.mean([r["correlation"]["greedy_f1"]["pearson_r"] for r in valid])
        avg_disagree = np.mean([r["agreement"]["disagree_pct"] for r in valid])
        if avg_pearson < 0.5:
            print("  Cross-family error correlation is LOW (mean Pearson r=%.4f)" % avg_pearson)
            print("  -> Models make errors on different instances -> ensemble diversity is high")
        elif avg_pearson < 0.7:
            print("  Cross-family error correlation is MODERATE (mean Pearson r=%.4f)" % avg_pearson)
            print("  -> Some complementarity exists but limited")
        else:
            print("  Cross-family error correlation is HIGH (mean Pearson r=%.4f)" % avg_pearson)
            print("  -> Models share similar error patterns -> ensemble diversity is limited")

        improvements = []
        for r in valid:
            best = max(r["model_performance"][m]["micro_f1"] for m in r["models"])
            sc_merge = r["ensemble"]["sc_merged_vote"]["micro_f1"]
            improvements.append(sc_merge - best)
        avg_imp = np.mean(improvements)
        print("  Mean SC-merged ensemble improvement: %+.2fpp over best single model" % avg_imp)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str,
                        default=str(BASE_DIR / "output" / "multi_model_correlation"))
    parser.add_argument("--datasets", nargs="+", default=list(DATA_CONFIGS.keys()))
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    results = []
    for ds in args.datasets:
        if ds not in DATA_CONFIGS:
            print("Unknown dataset: %s" % ds)
            continue
        print("\nAnalyzing %s..." % ds)
        r = analyze_dataset(ds, DATA_CONFIGS[ds])
        results.append(r)

    print_report(results)

    report_path = os.path.join(args.output_dir, "error_correlation_report.json")
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print("\nReport saved to %s" % report_path)


if __name__ == "__main__":
    main()
