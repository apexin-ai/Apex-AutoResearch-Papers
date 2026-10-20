"""D141: Entity-Level Majority Voting Merge Analysis

Proves entity-level merge can break instance-level selection ceiling.
For each test instance's N samples, entities are counted by (text, type)
frequency across samples. Merged outputs are constructed at various
thresholds and compared against greedy / LP-selection / oracle-selection.
"""

import json
import os
import sys
import numpy as np
from collections import Counter
from pathlib import Path

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import entity_strict_match

DATASETS = {
    "SciERC": "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
    "CoNLL": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl",
    "FewNERD": "/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
}
OUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/d141_entity_merge"


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                inst = json.loads(line)
                gold_ents = inst.get("gold", {}).get("entities", [])
                if len(gold_ents) == 0:
                    continue
                instances.append(inst)
    return instances


def instance_f1(pred_entities, gold_entities):
    tp, fp, fn = entity_strict_match(pred_entities, gold_entities)
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)


def build_entity_merge(samples, threshold_count):
    """Merge entities appearing in >= threshold_count samples.
    Groups by (text, type), picks most common (start, end) span."""
    counter = Counter()
    span_counter = {}
    span_to_entity = {}

    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["text"], e["type"])
            if key not in seen:
                counter[key] += 1
                seen.add(key)
            if key not in span_counter:
                span_counter[key] = Counter()
            span = (e["start"], e["end"])
            span_counter[key][span] += 1
            span_to_entity[(key[0], key[1], span[0], span[1])] = e

    merged = []
    for key, count in counter.items():
        if count >= threshold_count:
            best_span = span_counter[key].most_common(1)[0][0]
            merged.append(span_to_entity[(key[0], key[1], best_span[0], best_span[1])])
    return merged


def build_lp_weighted_merge(samples, logprobs, threshold=0.5):
    """Merge entities using softmax-weighted voting on sample logprobs.
    Keeps entities whose probability-weighted vote >= threshold."""
    lps = np.array(logprobs, dtype=float)
    weights = np.exp(lps - np.max(lps))
    weights = weights / weights.sum()

    entity_weight = {}
    span_counter = {}
    span_to_entity = {}

    for i, s in enumerate(samples):
        seen = set()
        for e in s.get("entities", []):
            key = (e["text"], e["type"])
            if key not in seen:
                entity_weight[key] = entity_weight.get(key, 0.0) + weights[i]
                seen.add(key)
            if key not in span_counter:
                span_counter[key] = Counter()
            span = (e["start"], e["end"])
            span_counter[key][span] += 1
            span_to_entity[(key[0], key[1], span[0], span[1])] = e

    merged = []
    for key, w in entity_weight.items():
        if w >= threshold:
            best_span = span_counter[key].most_common(1)[0][0]
            merged.append(span_to_entity[(key[0], key[1], best_span[0], best_span[1])])
    return merged


def analyze_dataset(name, instances):
    MAX_N = 8
    for inst in instances:
        inst["samples"] = inst["samples"][:MAX_N]
        if "logprobs" in inst:
            inst["logprobs"] = inst["logprobs"][:MAX_N]
    N = MAX_N
    n_inst = len(instances)
    print(f"\n{'='*60}")
    print(f"  {name}: {n_inst} instances, N={N}")
    print(f"{'='*60}")

    greedy_f1s = np.zeros(n_inst)
    lp_sel_f1s = np.zeros(n_inst)
    oracle_sel_f1s = np.zeros(n_inst)
    majority_f1s = np.zeros(n_inst)
    lp_weighted_f1s = np.zeros(n_inst)
    thresh_f1s = np.zeros((N, n_inst))  # thresh_f1s[k-1][i]
    sample_f1_matrix = np.zeros((n_inst, N))

    for i, inst in enumerate(instances):
        gold_ents = inst["gold"].get("entities", [])
        samples = inst["samples"]
        logprobs = inst.get("logprobs",
                            [s.get("mean_logprob", 0.0) for s in samples])

        # Greedy
        greedy_ents = inst.get("greedy", {}).get("entities", [])
        greedy_f1s[i] = instance_f1(greedy_ents, gold_ents)

        # Per-sample F1
        for j, s in enumerate(samples):
            sample_f1_matrix[i, j] = instance_f1(
                s.get("entities", []), gold_ents)

        # LP Selection
        best_lp_idx = int(np.argmax(logprobs))
        lp_sel_f1s[i] = sample_f1_matrix[i, best_lp_idx]

        # Oracle Selection
        oracle_sel_f1s[i] = sample_f1_matrix[i].max()

        # Majority Merge (>= N/2)
        maj_ents = build_entity_merge(samples, threshold_count=N / 2)
        majority_f1s[i] = instance_f1(maj_ents, gold_ents)

        # LP-Weighted Merge
        lp_ents = build_lp_weighted_merge(samples, logprobs, threshold=0.5)
        lp_weighted_f1s[i] = instance_f1(lp_ents, gold_ents)

        # Threshold Sweep k=1..N
        for k in range(1, N + 1):
            merged = build_entity_merge(samples, threshold_count=k)
            thresh_f1s[k - 1, i] = instance_f1(merged, gold_ents)

        if (i + 1) % 500 == 0:
            print(f"    processed {i+1}/{n_inst}")

    # Macro-averaged F1
    sweep_means = {k + 1: float(thresh_f1s[k].mean()) for k in range(N)}
    best_k = max(sweep_means, key=sweep_means.get)
    best_thresh_f1 = sweep_means[best_k]

    results = {
        "n_instances": n_inst,
        "N_samples": N,
        "greedy": round(float(greedy_f1s.mean()), 4),
        "lp_selection": round(float(lp_sel_f1s.mean()), 4),
        "oracle_selection": round(float(oracle_sel_f1s.mean()), 4),
        "majority_merge": round(float(majority_f1s.mean()), 4),
        "lp_weighted_merge": round(float(lp_weighted_f1s.mean()), 4),
        "best_threshold": best_k,
        "best_threshold_f1": round(best_thresh_f1, 4),
        "threshold_sweep": {str(k): round(v, 4) for k, v in sweep_means.items()},
    }

    # Also compute micro F1
    micro = {}
    for mname, arr_name in [("greedy", "greedy"), ("majority_merge", "majority"),
                             ("lp_weighted_merge", "lp_weighted")]:
        # recompute from raw counts
        total_tp = total_fp = total_fn = 0
        for idx, inst in enumerate(instances):
            gold_ents = inst["gold"].get("entities", [])
            if mname == "greedy":
                pred = inst.get("greedy", {}).get("entities", [])
            elif mname == "majority_merge":
                pred = build_entity_merge(inst["samples"], threshold_count=N / 2)
            else:
                lps = inst.get("logprobs",
                               [s.get("mean_logprob", 0.0) for s in inst["samples"]])
                pred = build_lp_weighted_merge(inst["samples"], lps, threshold=0.5)
            tp, fp, fn = entity_strict_match(pred, gold_ents)
            total_tp += tp
            total_fp += fp
            total_fn += fn
        p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
        r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
        f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        micro[mname] = round(f, 4)
    results["micro_f1"] = micro

    # Degenerate analysis
    degen_mask = (sample_f1_matrix.max(axis=1) == sample_f1_matrix.min(axis=1))
    n_degen = int(degen_mask.sum())
    degen_pct = n_degen / n_inst * 100

    if n_degen > 0:
        d_greedy = float(greedy_f1s[degen_mask].mean())
        d_majority = float(majority_f1s[degen_mask].mean())
        d_oracle = float(oracle_sel_f1s[degen_mask].mean())
        d_best_k = float(thresh_f1s[best_k - 1][degen_mask].mean())
        d_delta = d_majority - d_greedy
    else:
        d_greedy = d_majority = d_oracle = d_best_k = d_delta = float('nan')

    results["degenerate"] = {
        "n_degenerate": n_degen,
        "pct_degenerate": round(degen_pct, 2),
        "greedy_f1": round(d_greedy, 4),
        "majority_merge_f1": round(d_majority, 4),
        "oracle_f1": round(d_oracle, 4),
        "best_threshold_f1": round(d_best_k, 4),
        "delta_merge_vs_greedy": round(d_delta, 4),
    }

    # Non-degenerate analysis
    nondegen_mask = ~degen_mask
    n_nondegen = int(nondegen_mask.sum())
    if n_nondegen > 0:
        results["non_degenerate"] = {
            "n": n_nondegen,
            "greedy_f1": round(float(greedy_f1s[nondegen_mask].mean()), 4),
            "oracle_f1": round(float(oracle_sel_f1s[nondegen_mask].mean()), 4),
            "majority_merge_f1": round(float(majority_f1s[nondegen_mask].mean()), 4),
            "best_threshold_f1": round(float(thresh_f1s[best_k - 1][nondegen_mask].mean()), 4),
        }

    # Bootstrap 95% CI (1000 resamples)
    rng = np.random.RandomState(42)
    B = 1000
    methods_arr = {
        "greedy": greedy_f1s,
        "lp_selection": lp_sel_f1s,
        "oracle_selection": oracle_sel_f1s,
        "majority_merge": majority_f1s,
        "lp_weighted_merge": lp_weighted_f1s,
        "best_threshold_merge": thresh_f1s[best_k - 1],
    }

    ci = {}
    boot_samples = rng.choice(n_inst, (B, n_inst), replace=True)
    for mname, arr in methods_arr.items():
        boots = arr[boot_samples].mean(axis=1)
        lo, hi = float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))
        ci[mname] = {
            "mean": round(float(arr.mean()), 4),
            "ci_lo": round(lo, 4),
            "ci_hi": round(hi, 4),
        }

    # Difference CIs: merge methods vs oracle
    for mname in ["majority_merge", "lp_weighted_merge", "best_threshold_merge"]:
        diff = methods_arr[mname] - oracle_sel_f1s
        diff_boots = diff[boot_samples].mean(axis=1)
        lo, hi = float(np.percentile(diff_boots, 2.5)), float(np.percentile(diff_boots, 97.5))
        ci[f"{mname}_vs_oracle"] = {
            "mean_diff": round(float(diff.mean()), 4),
            "ci_lo": round(lo, 4),
            "ci_hi": round(hi, 4),
            "significant": bool(lo > 0 or hi < 0),
        }

    results["bootstrap_ci"] = ci

    # Print
    print(f"  Greedy:              {results['greedy']:.4f}")
    print(f"  LP Selection:        {results['lp_selection']:.4f}")
    print(f"  Oracle Selection:    {results['oracle_selection']:.4f}")
    print(f"  Majority Merge:      {results['majority_merge']:.4f}")
    print(f"  LP-Weighted Merge:   {results['lp_weighted_merge']:.4f}")
    print(f"  Best Thresh (k={best_k}):  {best_thresh_f1:.4f}")
    print(f"  Micro F1: greedy={micro['greedy']}, majority={micro['majority_merge']}, lp_wt={micro['lp_weighted_merge']}")
    ceiling_broken = best_thresh_f1 > results['oracle_selection']
    if ceiling_broken:
        print(f"  *** CEILING BROKEN: merge {best_thresh_f1:.4f} > oracle {results['oracle_selection']:.4f} ***")
    else:
        print(f"  Ceiling not broken: merge {best_thresh_f1:.4f} <= oracle {results['oracle_selection']:.4f}")
    print(f"  Degenerate: {n_degen}/{n_inst} ({degen_pct:.1f}%), Δ merge-greedy on degen: {d_delta:+.4f}")

    return results, sweep_means


def plot_threshold_curves(all_results, out_path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = {'SciERC': '#1f77b4', 'CoNLL': '#ff7f0e', 'FewNERD': '#2ca02c'}

    for name, (results, sweep) in all_results.items():
        ks = sorted(sweep.keys())
        f1s = [sweep[k] for k in ks]
        c = colors.get(name, None)
        ax.plot(ks, f1s, marker='o', markersize=4, label=f"{name} merge (N={results['N_samples']})", color=c)
        ax.axhline(y=results['oracle_selection'], color=c, linestyle='--', alpha=0.5,
                    label=f"{name} oracle={results['oracle_selection']:.4f}")
        ax.axhline(y=results['greedy'], color=c, linestyle=':', alpha=0.3)

    ax.set_xlabel("Threshold k (entity in >= k samples)", fontsize=11)
    ax.set_ylabel("Macro-averaged Entity F1", fontsize=11)
    ax.set_title("Entity-Level Merge: Threshold Sweep vs Oracle Ceiling", fontsize=12)
    ax.legend(fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"  Plot saved to {out_path}")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    all_results = {}
    all_sweep = {}

    for name, path in DATASETS.items():
        print(f"\nLoading {name}...")
        instances = load_data(path)
        # Gold filter: skip instances with no gold entities
        instances = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
        # N=8 truncation: unify all datasets to 8 samples
        for inst in instances:
            inst["samples"] = inst["samples"][:8]
            if "logprobs" in inst:
                inst["logprobs"] = inst["logprobs"][:8]
        results, sweep = analyze_dataset(name, instances)
        all_results[name] = results
        all_sweep[name] = (results, sweep)

        # Save intermediate results immediately
        with open(os.path.join(OUT_DIR, "results.json"), "w") as f:
            json.dump(all_results, f, indent=2)

    # Plot
    plot_path = os.path.join(OUT_DIR, "threshold_curve.png")
    plot_threshold_curves(all_sweep, plot_path)

    # Generate report.md
    lines = ["## Entity-Level Merge Results\n"]
    lines.append("| Dataset | Greedy | LP_Sel | Oracle_Sel | Majority_Merge | LP_Weighted | Best_Thresh | Best_k |")
    lines.append("|---------|--------|--------|------------|----------------|-------------|-------------|--------|")
    for name, r in all_results.items():
        lines.append(
            f"| {name} | {r['greedy']:.4f} | {r['lp_selection']:.4f} | "
            f"{r['oracle_selection']:.4f} | {r['majority_merge']:.4f} | "
            f"{r['lp_weighted_merge']:.4f} | {r['best_threshold_f1']:.4f} | {r['best_threshold']} |"
        )

    lines.append("\n## Micro F1 (for reference)")
    lines.append("| Dataset | Greedy | Majority_Merge | LP_Weighted |")
    lines.append("|---------|--------|----------------|-------------|")
    for name, r in all_results.items():
        m = r["micro_f1"]
        lines.append(f"| {name} | {m['greedy']:.4f} | {m['majority_merge']:.4f} | {m['lp_weighted_merge']:.4f} |")

    lines.append("\n## Bootstrap 95% CI")
    for name, r in all_results.items():
        lines.append(f"\n### {name}")
        lines.append("| Method | Mean | 95% CI |")
        lines.append("|--------|------|--------|")
        for mname in ["greedy", "lp_selection", "oracle_selection",
                       "majority_merge", "lp_weighted_merge", "best_threshold_merge"]:
            c = r["bootstrap_ci"][mname]
            lines.append(f"| {mname} | {c['mean']:.4f} | [{c['ci_lo']:.4f}, {c['ci_hi']:.4f}] |")
        lines.append("")
        lines.append("| Merge vs Oracle | Mean Δ | 95% CI | Significant |")
        lines.append("|-----------------|--------|--------|-------------|")
        for mname in ["majority_merge_vs_oracle", "lp_weighted_merge_vs_oracle",
                       "best_threshold_merge_vs_oracle"]:
            c = r["bootstrap_ci"][mname]
            sig = "YES" if c["significant"] else "NO"
            lines.append(f"| {mname} | {c['mean_diff']:+.4f} | [{c['ci_lo']:+.4f}, {c['ci_hi']:+.4f}] | {sig} |")

    lines.append("\n## Degenerate Subset Analysis")
    lines.append("| Dataset | Degen% | N_degen | Greedy | Merge_on_Degen | Oracle_on_Degen | Δ_Merge_vs_Greedy |")
    lines.append("|---------|--------|---------|--------|----------------|-----------------|-------------------|")
    for name, r in all_results.items():
        d = r["degenerate"]
        lines.append(
            f"| {name} | {d['pct_degenerate']:.1f}% | {d['n_degenerate']} | "
            f"{d['greedy_f1']:.4f} | {d['majority_merge_f1']:.4f} | "
            f"{d['oracle_f1']:.4f} | {d['delta_merge_vs_greedy']:+.4f} |"
        )

    if any("non_degenerate" in r for r in all_results.values()):
        lines.append("\n## Non-Degenerate Subset")
        lines.append("| Dataset | N | Greedy | Oracle | Majority_Merge | Best_Thresh |")
        lines.append("|---------|---|--------|--------|----------------|-------------|")
        for name, r in all_results.items():
            if "non_degenerate" in r:
                nd = r["non_degenerate"]
                lines.append(
                    f"| {name} | {nd['n']} | {nd['greedy_f1']:.4f} | "
                    f"{nd['oracle_f1']:.4f} | {nd['majority_merge_f1']:.4f} | "
                    f"{nd['best_threshold_f1']:.4f} |"
                )

    lines.append("\n## Threshold Sweep Detail")
    for name, r in all_results.items():
        lines.append(f"\n### {name} (N={r['N_samples']})")
        lines.append("| k | F1 |")
        lines.append("|---|------|")
        for k in sorted(r["threshold_sweep"].keys(), key=int):
            marker = " <-- best" if int(k) == r["best_threshold"] else ""
            lines.append(f"| {k} | {r['threshold_sweep'][k]:.4f}{marker} |")

    lines.append("\n## Threshold Curves\n![Threshold Curve](threshold_curve.png)")

    report_path = os.path.join(OUT_DIR, "report.md")
    with open(report_path, "w") as f:
        f.write("\n".join(lines))
    print(f"\n  Report saved to {report_path}")
    print(f"  Results saved to {os.path.join(OUT_DIR, 'results.json')}")


if __name__ == "__main__":
    main()
