#!/usr/bin/env python3
"""K: Robustness Analysis — SC construction methods under perturbations."""

import json
import math
import os
import sys
import numpy as np
from collections import defaultdict, Counter

BASE = "/root/autodl-tmp/struct_self_consist_ie"

SEED_FILES = {
    42: f"{BASE}/output/exp_021_inference/samples.jsonl",
    123: f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl",
    456: f"{BASE}/output/exp_021_fewnerd_n8_seed456/samples.jsonl",
    789: f"{BASE}/output/fewnerd_seed789_merged/samples.jsonl",
}

OUTPUT_DIR = f"{BASE}/output/k_robustness"
N_FULL = 8
THETA_MAJORITY = 0.5
N_REPEATS = 20
RNG_SEED = 42

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def compute_f1(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r)

def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances

def get_lp_weights(samples):
    lps = []
    for s in samples:
        lp = s.get("mean_logprob", None)
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]

def get_vc_weights(samples):
    N = len(samples)
    entity_counts = Counter()
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                seen.add(key)
    weights = []
    for s in samples:
        ents = set()
        for e in s.get("entities", []):
            ents.add((e["start"], e["end"], e["type"]))
        if ents:
            w = sum(entity_counts[k] for k in ents) / (N * len(ents))
        else:
            w = 1.0 / N
        weights.append(w)
    total = sum(weights)
    if total == 0:
        return [1.0 / N] * N
    return [w / total for w in weights]

def get_sj_weights(samples):
    N = len(samples)
    sets = []
    for s in samples:
        es = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        sets.append(es)
    weights = []
    for i in range(N):
        if N == 1:
            weights.append(1.0)
            continue
        total_j = 0.0
        for j in range(N):
            if j == i:
                continue
            a, b = sets[i], sets[j]
            if not a and not b:
                total_j += 1.0
            elif not a or not b:
                pass
            else:
                total_j += len(a & b) / len(a | b)
        weights.append(total_j / (N - 1))
    total = sum(weights)
    if total == 0:
        return [1.0 / N] * N
    return [w / total for w in weights]

def weighted_construction(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        seen = set()
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += w
                seen.add(key)
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed

METHODS = ["greedy", "majority_vote", "uniform", "lp_weighted", "vc_weighted", "sj_weighted"]

def apply_method(method, samples, greedy=None):
    if method == "greedy":
        if greedy is not None:
            return entity_set(greedy.get("entities", []))
        return entity_set(samples[0].get("entities", []))
    N = len(samples)
    theta = THETA_MAJORITY if method == "majority_vote" else 2.0 / N
    if method in ("majority_vote", "uniform"):
        return weighted_construction(samples, theta)
    elif method == "lp_weighted":
        ws = get_lp_weights(samples)
        return weighted_construction(samples, theta, weights=ws)
    elif method == "vc_weighted":
        ws = get_vc_weights(samples)
        return weighted_construction(samples, theta, weights=ws)
    elif method == "sj_weighted":
        ws = get_sj_weights(samples)
        return weighted_construction(samples, theta, weights=ws)

def seed_robustness(all_data):
    print("\n=== Task 1: Seed Robustness ===", flush=True)
    results = {}
    for method in METHODS:
        seed_f1s = {}
        for seed, data in sorted(all_data.items()):
            f1s = []
            for inst in data:
                gold = entity_set(inst["gold"]["entities"])
                greedy = inst.get("greedy", inst["samples"][0])
                pred = apply_method(method, inst["samples"], greedy=greedy)
                f1s.append(compute_f1(pred, gold))
            seed_f1s[seed] = float(np.mean(f1s))
        vals = list(seed_f1s.values())
        results[method] = {
            "per_seed": {str(k): v for k, v in seed_f1s.items()},
            "mean": float(np.mean(vals)),
            "std": float(np.std(vals, ddof=0)),
            "range": float(max(vals) - min(vals)),
        }
        print(f"  {method:15s}: mean={results[method]['mean']*100:.2f}  std={results[method]['std']*100:.3f}  range={results[method]['range']*100:.3f}", flush=True)
    return results

def n_robustness(all_data):
    print("\n=== Task 2: N Robustness (Subsampling) ===", flush=True)
    rng = np.random.RandomState(RNG_SEED)
    data = all_data[42]
    sub_ns = [2, 4, 6]
    results = {}
    for method in METHODS:
        if method == "greedy":
            f1s = []
            for inst in data:
                gold = entity_set(inst["gold"]["entities"])
                greedy = inst.get("greedy", inst["samples"][0])
                pred = apply_method(method, inst["samples"], greedy=greedy)
                f1s.append(compute_f1(pred, gold))
            base_f1 = float(np.mean(f1s))
            results[method] = {
                "N8_f1": base_f1,
                "sub_n": {str(n): {"mean": base_f1, "std": 0.0, "all_f1s": [base_f1] * N_REPEATS} for n in sub_ns},
            }
            print(f"  {method:15s}: N=8 F1={base_f1*100:.2f} (constant)", flush=True)
            continue
        full_f1s = []
        for inst in data:
            gold = entity_set(inst["gold"]["entities"])
            pred = apply_method(method, inst["samples"])
            full_f1s.append(compute_f1(pred, gold))
        base_f1 = float(np.mean(full_f1s))
        method_results = {"N8_f1": base_f1, "sub_n": {}}
        for sub_n in sub_ns:
            repeat_f1s = []
            for rep in range(N_REPEATS):
                indices = rng.choice(N_FULL, size=sub_n, replace=False)
                instance_f1s = []
                for inst in data:
                    gold = entity_set(inst["gold"]["entities"])
                    sub_samples = [inst["samples"][i] for i in indices]
                    pred = apply_method(method, sub_samples)
                    instance_f1s.append(compute_f1(pred, gold))
                repeat_f1s.append(float(np.mean(instance_f1s)))
                if (rep + 1) % 5 == 0:
                    print(f"    {method} N={sub_n} rep={rep+1}/{N_REPEATS}", flush=True)
            method_results["sub_n"][str(sub_n)] = {
                "mean": float(np.mean(repeat_f1s)),
                "std": float(np.std(repeat_f1s)),
                "all_f1s": repeat_f1s,
            }
            print(f"  {method:15s} N={sub_n}: {np.mean(repeat_f1s)*100:.2f} +/- {np.std(repeat_f1s)*100:.3f}", flush=True)
        results[method] = method_results
    return results

def dropout_robustness(all_data):
    print("\n=== Task 3: Sample Dropout ===", flush=True)
    rng = np.random.RandomState(RNG_SEED + 1)
    data = all_data[42]
    drop_counts = [1, 2, 3]
    results = {}
    for method in METHODS:
        if method == "greedy":
            f1s = []
            for inst in data:
                gold = entity_set(inst["gold"]["entities"])
                greedy = inst.get("greedy", inst["samples"][0])
                pred = apply_method(method, inst["samples"], greedy=greedy)
                f1s.append(compute_f1(pred, gold))
            base_f1 = float(np.mean(f1s))
            results[method] = {
                "N8_f1": base_f1,
                "dropout": {str(d): {"mean_f1": base_f1, "mean_drop": 0.0, "std": 0.0} for d in drop_counts},
            }
            print(f"  {method:15s}: N=8 F1={base_f1*100:.2f} (not affected)", flush=True)
            continue
        full_f1s = []
        for inst in data:
            gold = entity_set(inst["gold"]["entities"])
            pred = apply_method(method, inst["samples"])
            full_f1s.append(compute_f1(pred, gold))
        base_f1 = float(np.mean(full_f1s))
        method_results = {"N8_f1": base_f1, "dropout": {}}
        for drop_n in drop_counts:
            repeat_f1s = []
            for rep in range(N_REPEATS):
                drop_indices = set(rng.choice(N_FULL, size=drop_n, replace=False))
                keep_indices = [i for i in range(N_FULL) if i not in drop_indices]
                instance_f1s = []
                for inst in data:
                    gold = entity_set(inst["gold"]["entities"])
                    sub_samples = [inst["samples"][i] for i in keep_indices]
                    pred = apply_method(method, sub_samples)
                    instance_f1s.append(compute_f1(pred, gold))
                repeat_f1s.append(float(np.mean(instance_f1s)))
            mean_f1 = float(np.mean(repeat_f1s))
            method_results["dropout"][str(drop_n)] = {
                "mean_f1": mean_f1,
                "mean_drop": float(base_f1 - mean_f1),
                "std": float(np.std(repeat_f1s)),
                "all_f1s": repeat_f1s,
            }
            print(f"  {method:15s} drop={drop_n}: {mean_f1*100:.2f}  D={-(base_f1 - mean_f1)*100:.3f}pp", flush=True)
        results[method] = method_results
    return results

def type_analysis(all_data):
    print("\n=== Task 4: Entity Type Analysis ===", flush=True)
    data = all_data[42]
    type_counts = Counter()
    for inst in data:
        for e in inst["gold"]["entities"]:
            type_counts[e["type"]] += 1
    print(f"  Entity types: {len(type_counts)}", flush=True)
    for t, c in type_counts.most_common():
        print(f"    {t}: {c}", flush=True)
    results = {"type_counts": dict(type_counts.most_common()), "per_type": {}}
    for method in METHODS:
        type_tp = defaultdict(int)
        type_fp = defaultdict(int)
        type_fn = defaultdict(int)
        for inst in data:
            gold_entities = inst["gold"]["entities"]
            greedy = inst.get("greedy", inst["samples"][0])
            pred_set = apply_method(method, inst["samples"], greedy=greedy)
            gold_by_type = defaultdict(set)
            for e in gold_entities:
                gold_by_type[e["type"]].add((e["start"], e["end"], e["type"]))
            pred_by_type = defaultdict(set)
            for key in pred_set:
                pred_by_type[key[2]].add(key)
            all_types = set(gold_by_type.keys()) | set(pred_by_type.keys())
            for t in all_types:
                g = gold_by_type.get(t, set())
                p = pred_by_type.get(t, set())
                tp = len(g & p)
                type_tp[t] += tp
                type_fp[t] += len(p) - tp
                type_fn[t] += len(g) - tp
        type_f1s = {}
        for t in type_counts:
            tp = type_tp[t]
            fp = type_fp[t]
            fn = type_fn[t]
            if tp == 0:
                type_f1s[t] = 0.0
            else:
                p_val = tp / (tp + fp)
                r_val = tp / (tp + fn)
                type_f1s[t] = 2 * p_val * r_val / (p_val + r_val)
        results["per_type"][method] = type_f1s
        print(f"  {method} done", flush=True)
    construction_methods = [m for m in METHODS if m != "greedy"]
    type_variance = {}
    for t in type_counts:
        f1s = [results["per_type"][m][t] for m in construction_methods]
        type_variance[t] = {
            "std": float(np.std(f1s)),
            "range": float(max(f1s) - min(f1s)),
            "best_method": construction_methods[int(np.argmax(f1s))],
            "worst_method": construction_methods[int(np.argmin(f1s))],
        }
    results["inter_method_variance"] = type_variance
    sorted_types = sorted(type_counts.items(), key=lambda x: x[1])
    n_types = len(sorted_types)
    rare_types = set(t for t, _ in sorted_types[:n_types // 3])
    common_types = set(t for t, _ in sorted_types[-n_types // 3:])
    rare_common = {"rare_types": sorted(rare_types), "common_types": sorted(common_types)}
    for method in METHODS:
        rare_f1s = [results["per_type"][method][t] for t in rare_types if t in results["per_type"][method]]
        common_f1s = [results["per_type"][method][t] for t in common_types if t in results["per_type"][method]]
        rare_common[method] = {
            "rare_mean_f1": float(np.mean(rare_f1s)) if rare_f1s else 0.0,
            "common_mean_f1": float(np.mean(common_f1s)) if common_f1s else 0.0,
            "gap": float(np.mean(common_f1s) - np.mean(rare_f1s)) if rare_f1s and common_f1s else 0.0,
        }
    results["rare_vs_common"] = rare_common
    return results

def make_plots(seed_res, n_res, dropout_res, output_dir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    construction_methods = [m for m in METHODS if m != "greedy"]
    colors = {"majority_vote": "#e74c3c", "uniform": "#3498db", "lp_weighted": "#2ecc71",
              "vc_weighted": "#9b59b6", "sj_weighted": "#f39c12"}
    ax = axes[0]
    x = np.arange(len(construction_methods))
    means = [seed_res[m]["mean"] * 100 for m in construction_methods]
    stds = [seed_res[m]["std"] * 100 for m in construction_methods]
    ax.bar(x, means, yerr=stds, capsize=5,
           color=[colors[m] for m in construction_methods], alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels([m.replace("_", "\n") for m in construction_methods], fontsize=8)
    ax.set_ylabel("F1 (%)")
    ax.set_title("(a) Cross-Seed Stability")
    ax.axhline(seed_res["greedy"]["mean"] * 100, color="gray", linestyle="--", linewidth=1, label="greedy")
    ax.legend(fontsize=8)
    ymin = min(means) - max(stds) - 1
    ymax = max(means) + max(stds) + 1
    ax.set_ylim(ymin, ymax)
    ax = axes[1]
    ns = [2, 4, 6, 8]
    for method in construction_methods:
        y = []
        yerr = []
        for n in ns:
            if n == 8:
                y.append(n_res[method]["N8_f1"] * 100)
                yerr.append(0.0)
            else:
                y.append(n_res[method]["sub_n"][str(n)]["mean"] * 100)
                yerr.append(n_res[method]["sub_n"][str(n)]["std"] * 100)
        ax.errorbar(ns, y, yerr=yerr, marker="o", label=method.replace("_", " "),
                     color=colors[method], capsize=3, linewidth=1.5, markersize=5)
    ax.set_xlabel("Number of samples (N)")
    ax.set_ylabel("F1 (%)")
    ax.set_title("(b) N-Sensitivity")
    ax.set_xticks(ns)
    ax.legend(fontsize=7, loc="lower right")
    ax = axes[2]
    drops = [0, 1, 2, 3]
    for method in construction_methods:
        y = [dropout_res[method]["N8_f1"] * 100]
        yerr_vals = [0.0]
        for d in [1, 2, 3]:
            y.append(dropout_res[method]["dropout"][str(d)]["mean_f1"] * 100)
            yerr_vals.append(dropout_res[method]["dropout"][str(d)]["std"] * 100)
        ax.errorbar(drops, y, yerr=yerr_vals, marker="s", label=method.replace("_", " "),
                     color=colors[method], capsize=3, linewidth=1.5, markersize=5)
    ax.set_xlabel("Samples dropped")
    ax.set_ylabel("F1 (%)")
    ax.set_title("(c) Dropout Resilience")
    ax.set_xticks(drops)
    ax.legend(fontsize=7, loc="lower left")
    plt.tight_layout()
    path = os.path.join(output_dir, "robustness_plot.png")
    plt.savefig(path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"\nPlot saved: {path}", flush=True)

def write_summary(seed_res, n_res, dropout_res, type_res, output_dir):
    lines = ["# K: Robustness Analysis — Summary\n"]
    lines.append("Dataset: FewNERD | Model: Qwen 7B FT | N=8 | Seeds: 42, 123, 456, 789\n")
    lines.append("## 1. Seed Robustness\n")
    lines.append("| Method | Mean F1 (%) | Std (%) | Range (%) |")
    lines.append("|--------|------------|---------|-----------|")
    for m in METHODS:
        r = seed_res[m]
        lines.append(f"| {m} | {r['mean']*100:.2f} | {r['std']*100:.3f} | {r['range']*100:.3f} |")
    construction_methods = [m for m in METHODS if m != "greedy"]
    most_stable = min(construction_methods, key=lambda m: seed_res[m]["std"])
    lines.append(f"\n**Most seed-stable construction method**: `{most_stable}` (std={seed_res[most_stable]['std']*100:.3f}%)\n")
    lines.append("## 2. N Robustness (Subsampling)\n")
    lines.append("| Method | N=2 | N=4 | N=6 | N=8 | Sensitivity (mean std) |")
    lines.append("|--------|-----|-----|-----|-----|----------------------|")
    for m in construction_methods:
        r = n_res[m]
        stds = [r["sub_n"][str(n)]["std"] for n in [2, 4, 6]]
        mean_sens = np.mean(stds)
        n2 = r["sub_n"]["2"]["mean"] * 100
        n4 = r["sub_n"]["4"]["mean"] * 100
        n6 = r["sub_n"]["6"]["mean"] * 100
        n8 = r["N8_f1"] * 100
        lines.append(f"| {m} | {n2:.2f} | {n4:.2f} | {n6:.2f} | {n8:.2f} | {mean_sens*100:.3f} |")
    least_sensitive = min(construction_methods, key=lambda m: np.mean([n_res[m]["sub_n"][str(n)]["std"] for n in [2, 4, 6]]))
    lines.append(f"\n**Least N-sensitive**: `{least_sensitive}`\n")
    lines.append("## 3. Dropout Resilience\n")
    lines.append("| Method | Drop=1 D (pp) | Drop=2 D (pp) | Drop=3 D (pp) | Avg D (pp) |")
    lines.append("|--------|--------------|--------------|--------------|-----------|")
    for m in construction_methods:
        r = dropout_res[m]
        d1 = r["dropout"]["1"]["mean_drop"] * 100
        d2 = r["dropout"]["2"]["mean_drop"] * 100
        d3 = r["dropout"]["3"]["mean_drop"] * 100
        avg = (d1 + d2 + d3) / 3
        lines.append(f"| {m} | {d1:.3f} | {d2:.3f} | {d3:.3f} | {avg:.3f} |")
    most_resilient = min(construction_methods, key=lambda m: sum(dropout_res[m]["dropout"][str(d)]["mean_drop"] for d in [1,2,3]))
    lines.append(f"\n**Most dropout-resilient**: `{most_resilient}`\n")
    lines.append("## 4. Entity Type Analysis\n")
    lines.append(f"Total entity types: {len(type_res['type_counts'])}\n")
    var_items = sorted(type_res["inter_method_variance"].items(), key=lambda x: x[1]["range"], reverse=True)
    lines.append("### Types with largest inter-method F1 range\n")
    lines.append("| Type | Count | Range (%) | Best Method | Worst Method |")
    lines.append("|------|-------|-----------|-------------|-------------|")
    for t, v in var_items[:10]:
        lines.append(f"| {t} | {type_res['type_counts'][t]} | {v['range']*100:.2f} | {v['best_method']} | {v['worst_method']} |")
    lines.append("\n### Rare vs Common Types\n")
    lines.append("| Method | Rare F1 (%) | Common F1 (%) | Gap (pp) |")
    lines.append("|--------|------------|--------------|----------|")
    for m in METHODS:
        rc = type_res["rare_vs_common"][m]
        lines.append(f"| {m} | {rc['rare_mean_f1']*100:.2f} | {rc['common_mean_f1']*100:.2f} | {rc['gap']*100:.2f} |")
    lines.append("\n## 5. Overall Robustness Ranking\n")
    scores = {}
    for m in construction_methods:
        seed_rank = sorted(construction_methods, key=lambda x: seed_res[x]["std"]).index(m)
        n_rank = sorted(construction_methods, key=lambda x: np.mean([n_res[x]["sub_n"][str(n)]["std"] for n in [2, 4, 6]])).index(m)
        drop_rank = sorted(construction_methods, key=lambda x: sum(dropout_res[x]["dropout"][str(d)]["mean_drop"] for d in [1,2,3])).index(m)
        avg_rank = (seed_rank + n_rank + drop_rank) / 3
        scores[m] = {"seed_rank": seed_rank+1, "n_rank": n_rank+1, "drop_rank": drop_rank+1, "avg_rank": avg_rank+1}
    lines.append("| Method | Seed Rank | N Rank | Dropout Rank | Avg Rank |")
    lines.append("|--------|-----------|--------|-------------|----------|")
    for m in sorted(construction_methods, key=lambda x: scores[x]["avg_rank"]):
        s = scores[m]
        lines.append(f"| {m} | {s['seed_rank']} | {s['n_rank']} | {s['drop_rank']} | {s['avg_rank']:.1f} |")
    best = min(construction_methods, key=lambda x: scores[x]["avg_rank"])
    lines.append(f"\n**Overall most robust method**: `{best}`\n")
    path = os.path.join(output_dir, "summary.md")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"Summary saved: {path}", flush=True)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Loading data...", flush=True)
    all_data = {}
    for seed, path in sorted(SEED_FILES.items()):
        if not os.path.exists(path):
            print(f"  SKIP seed {seed}: {path} not found")
            continue
        data = load_data(path, gold_filter=True)
        all_data[seed] = data
        print(f"  Seed {seed}: {len(data)} instances, N={len(data[0]['samples'])}", flush=True)
    seed_res = seed_robustness(all_data)
    with open(os.path.join(OUTPUT_DIR, "seed_robustness.json"), "w") as f:
        json.dump(seed_res, f, indent=2)
    print("  -> seed_robustness.json saved", flush=True)
    n_res = n_robustness(all_data)
    with open(os.path.join(OUTPUT_DIR, "n_robustness.json"), "w") as f:
        json.dump(n_res, f, indent=2)
    print("  -> n_robustness.json saved", flush=True)
    dropout_res = dropout_robustness(all_data)
    with open(os.path.join(OUTPUT_DIR, "dropout_robustness.json"), "w") as f:
        json.dump(dropout_res, f, indent=2)
    print("  -> dropout_robustness.json saved", flush=True)
    type_res = type_analysis(all_data)
    with open(os.path.join(OUTPUT_DIR, "type_analysis.json"), "w") as f:
        json.dump(type_res, f, indent=2)
    print("  -> type_analysis.json saved", flush=True)
    make_plots(seed_res, n_res, dropout_res, OUTPUT_DIR)
    write_summary(seed_res, n_res, dropout_res, type_res, OUTPUT_DIR)
    print("\n=== All done! ===", flush=True)

if __name__ == "__main__":
    main()
