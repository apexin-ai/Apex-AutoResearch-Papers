#!/usr/bin/env python3
"""D140 Task A: Oracle Degeneracy-Gated LP Selection Analysis.

Enhanced version with bootstrap 95% CI and report generation.
"""

import json
import os
import sys
import numpy as np
from collections import defaultdict

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from evaluation import entity_strict_match, _prf

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "SciERC": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
    "CoNLL": f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
    "Few-NERD": f"{BASE}/output/exp_021_inference/samples.jsonl",
}

N_BOOTSTRAP = 1000
SEED = 42


def load_data(path):
    data = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            inst = json.loads(line)
            if len(inst["gold"].get("entities", [])) > 0:
                data.append(inst)
    return data


def get_tp_fp_fn(pred, gold):
    return entity_strict_match(
        pred.get("entities", []), gold.get("entities", [])
    )


def micro_f1_from_counts(tp, fp, fn):
    return _prf(tp, fp, fn)["f1"]


def compute_instance_data(data):
    """Precompute per-instance tp/fp/fn for greedy, LP, oracle, and gated selections."""
    instances = []
    for inst in data:
        gold = inst["gold"]
        samples = inst["samples"]
        greedy = inst["greedy"]

        g_tp, g_fp, g_fn = get_tp_fp_fn(greedy, gold)

        sample_f1s = []
        sample_lps = []
        sample_counts = []
        for s in samples:
            tp, fp, fn = get_tp_fp_fn(s, gold)
            f1_i = _prf(tp, fp, fn)["f1"]
            sample_f1s.append(f1_i)
            sample_lps.append(s.get("mean_logprob", s.get("cumulative_logprob", 0)))
            sample_counts.append((tp, fp, fn))

        best_idx = max(range(len(sample_f1s)), key=lambda i: sample_f1s[i])
        lp_idx = max(range(len(sample_lps)), key=lambda i: sample_lps[i])
        is_degenerate = len(set(round(f, 10) for f in sample_f1s)) == 1

        o_tp, o_fp, o_fn = sample_counts[best_idx]
        l_tp, l_fp, l_fn = sample_counts[lp_idx]

        if is_degenerate:
            ga_tp, ga_fp, ga_fn = g_tp, g_fp, g_fn
        else:
            ga_tp, ga_fp, ga_fn = l_tp, l_fp, l_fn

        instances.append({
            "degenerate": is_degenerate,
            "greedy": (g_tp, g_fp, g_fn),
            "oracle": (o_tp, o_fp, o_fn),
            "lp": (l_tp, l_fp, l_fn),
            "gated": (ga_tp, ga_fp, ga_fn),
            "greedy_f1": _prf(g_tp, g_fp, g_fn)["f1"],
            "lp_f1": _prf(l_tp, l_fp, l_fn)["f1"],
            "oracle_f1": _prf(o_tp, o_fp, o_fn)["f1"],
            "gated_f1": _prf(ga_tp, ga_fp, ga_fn)["f1"],
        })
    return instances


def aggregate_micro_f1(instances, key, subset=None):
    tp = fp = fn = 0
    for inst in instances:
        if subset == "degenerate" and not inst["degenerate"]:
            continue
        if subset == "non_degenerate" and inst["degenerate"]:
            continue
        t, f_p, f_n = inst[key]
        tp += t
        fp += f_p
        fn += f_n
    return micro_f1_from_counts(tp, fp, fn)


def bootstrap_ci(instances, key, subset=None, n_boot=N_BOOTSTRAP, seed=SEED):
    rng = np.random.RandomState(seed)
    filtered = instances
    if subset == "degenerate":
        filtered = [i for i in instances if i["degenerate"]]
    elif subset == "non_degenerate":
        filtered = [i for i in instances if not i["degenerate"]]

    if len(filtered) == 0:
        return 0.0, 0.0, 0.0

    n = len(filtered)
    boot_f1s = []
    for _ in range(n_boot):
        idxs = rng.randint(0, n, size=n)
        tp = fp = fn = 0
        for idx in idxs:
            t, f_p, f_n = filtered[idx][key]
            tp += t
            fp += f_p
            fn += f_n
        boot_f1s.append(micro_f1_from_counts(tp, fp, fn))

    boot_f1s.sort()
    lo = boot_f1s[int(0.025 * n_boot)]
    hi = boot_f1s[int(0.975 * n_boot)]
    mean = np.mean(boot_f1s)
    return mean, lo, hi


def bootstrap_delta_ci(instances, key_a, key_b, subset=None, n_boot=N_BOOTSTRAP, seed=SEED):
    """Bootstrap CI for (key_a - key_b) delta."""
    rng = np.random.RandomState(seed)
    filtered = instances
    if subset == "degenerate":
        filtered = [i for i in instances if i["degenerate"]]
    elif subset == "non_degenerate":
        filtered = [i for i in instances if not i["degenerate"]]

    if len(filtered) == 0:
        return 0.0, 0.0, 0.0

    n = len(filtered)
    deltas = []
    for _ in range(n_boot):
        idxs = rng.randint(0, n, size=n)
        tp_a = fp_a = fn_a = 0
        tp_b = fp_b = fn_b = 0
        for idx in idxs:
            t, f_p, f_n = filtered[idx][key_a]
            tp_a += t; fp_a += f_p; fn_a += f_n
            t, f_p, f_n = filtered[idx][key_b]
            tp_b += t; fp_b += f_p; fn_b += f_n
        f1_a = micro_f1_from_counts(tp_a, fp_a, fn_a)
        f1_b = micro_f1_from_counts(tp_b, fp_b, fn_b)
        deltas.append(f1_a - f1_b)

    deltas.sort()
    lo = deltas[int(0.025 * n_boot)]
    hi = deltas[int(0.975 * n_boot)]
    mean = np.mean(deltas)
    return mean, lo, hi


def analyze_dataset(name, path):
    if not os.path.exists(path):
        print(f"SKIP {name}: {path} not found")
        return None

    data = load_data(path)
    n_total = len(data)
    instances = compute_instance_data(data)

    n_degenerate = sum(1 for i in instances if i["degenerate"])
    n_nondeg = n_total - n_degenerate
    n_samples = len(data[0]["samples"]) if data else 0

    print(f"\n{'='*60}")
    print(f"{name}: {n_total} instances (gold-filtered), N={n_samples} samples/inst")
    print(f"  Degenerate: {n_degenerate}/{n_total} ({100*n_degenerate/n_total:.1f}%)")

    # Point estimates
    greedy_f1 = aggregate_micro_f1(instances, "greedy")
    oracle_f1 = aggregate_micro_f1(instances, "oracle")
    lp_f1 = aggregate_micro_f1(instances, "lp")
    gated_f1 = aggregate_micro_f1(instances, "gated")

    nondeg_greedy_f1 = aggregate_micro_f1(instances, "greedy", "non_degenerate")
    nondeg_lp_f1 = aggregate_micro_f1(instances, "lp", "non_degenerate")
    nondeg_oracle_f1 = aggregate_micro_f1(instances, "oracle", "non_degenerate")
    deg_greedy_f1 = aggregate_micro_f1(instances, "greedy", "degenerate")

    print(f"  Greedy F1:   {greedy_f1*100:.4f}")
    print(f"  LP F1:       {lp_f1*100:.4f}  (delta: {(lp_f1-greedy_f1)*100:+.4f})")
    print(f"  Oracle F1:   {oracle_f1*100:.4f}")
    print(f"  Gated F1:    {gated_f1*100:.4f}  (delta: {(gated_f1-greedy_f1)*100:+.4f})")
    print(f"  NonDeg LP:   {nondeg_lp_f1*100:.4f}  (vs greedy: {(nondeg_lp_f1-nondeg_greedy_f1)*100:+.4f})")

    # Bootstrap CIs
    print("  Computing bootstrap CIs...")
    ci_greedy = bootstrap_ci(instances, "greedy")
    ci_lp = bootstrap_ci(instances, "lp")
    ci_oracle = bootstrap_ci(instances, "oracle")
    ci_gated = bootstrap_ci(instances, "gated")

    ci_lp_vs_greedy = bootstrap_delta_ci(instances, "lp", "greedy")
    ci_gated_vs_greedy = bootstrap_delta_ci(instances, "gated", "greedy")
    ci_gated_vs_lp = bootstrap_delta_ci(instances, "gated", "lp")

    ci_nondeg_lp = bootstrap_ci(instances, "lp", "non_degenerate")
    ci_nondeg_greedy = bootstrap_ci(instances, "greedy", "non_degenerate")
    ci_nondeg_oracle = bootstrap_ci(instances, "oracle", "non_degenerate")
    ci_nondeg_lp_vs_greedy = bootstrap_delta_ci(instances, "lp", "greedy", "non_degenerate")

    ci_deg_greedy = bootstrap_ci(instances, "greedy", "degenerate")

    result = {
        "dataset": name,
        "n_samples_per_instance": n_samples,
        "total_instances": n_total,
        "degenerate_count": n_degenerate,
        "non_degenerate_count": n_nondeg,
        "degeneracy_rate_pct": round(100 * n_degenerate / n_total, 4),
        "overall": {
            "greedy_f1": round(greedy_f1 * 100, 4),
            "lp_f1": round(lp_f1 * 100, 4),
            "oracle_f1": round(oracle_f1 * 100, 4),
            "gated_f1": round(gated_f1 * 100, 4),
            "lp_vs_greedy": round((lp_f1 - greedy_f1) * 100, 4),
            "gated_vs_greedy": round((gated_f1 - greedy_f1) * 100, 4),
            "gated_vs_lp": round((gated_f1 - lp_f1) * 100, 4),
            "ci_greedy": [round(x * 100, 4) for x in ci_greedy],
            "ci_lp": [round(x * 100, 4) for x in ci_lp],
            "ci_oracle": [round(x * 100, 4) for x in ci_oracle],
            "ci_gated": [round(x * 100, 4) for x in ci_gated],
            "ci_lp_vs_greedy": [round(x * 100, 4) for x in ci_lp_vs_greedy],
            "ci_gated_vs_greedy": [round(x * 100, 4) for x in ci_gated_vs_greedy],
            "ci_gated_vs_lp": [round(x * 100, 4) for x in ci_gated_vs_lp],
        },
        "non_degenerate": {
            "count": n_nondeg,
            "greedy_f1": round(nondeg_greedy_f1 * 100, 4),
            "lp_f1": round(nondeg_lp_f1 * 100, 4),
            "oracle_f1": round(nondeg_oracle_f1 * 100, 4),
            "lp_vs_greedy": round((nondeg_lp_f1 - nondeg_greedy_f1) * 100, 4),
            "ci_greedy": [round(x * 100, 4) for x in ci_nondeg_greedy],
            "ci_lp": [round(x * 100, 4) for x in ci_nondeg_lp],
            "ci_oracle": [round(x * 100, 4) for x in ci_nondeg_oracle],
            "ci_lp_vs_greedy": [round(x * 100, 4) for x in ci_nondeg_lp_vs_greedy],
        },
        "degenerate": {
            "count": n_degenerate,
            "greedy_f1": round(deg_greedy_f1 * 100, 4),
            "ci_greedy": [round(x * 100, 4) for x in ci_deg_greedy],
        },
    }

    print(f"  Bootstrap CI (LP vs Greedy): [{ci_lp_vs_greedy[1]*100:+.4f}, {ci_lp_vs_greedy[2]*100:+.4f}]")
    print(f"  Bootstrap CI (Gated vs LP):  [{ci_gated_vs_lp[1]*100:+.4f}, {ci_gated_vs_lp[2]*100:+.4f}]")
    print(f"  NonDeg LP vs Greedy CI:      [{ci_nondeg_lp_vs_greedy[1]*100:+.4f}, {ci_nondeg_lp_vs_greedy[2]*100:+.4f}]")

    return result


def fmt_ci(ci_list):
    """Format [mean, lo, hi] as string."""
    return f"[{ci_list[1]:+.4f}, {ci_list[2]:+.4f}]"


def generate_report(results, out_dir):
    lines = []
    lines.append("# D140: Oracle Degeneracy-Gated LP Selection Analysis")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("Degeneracy = all N samples have identical entity-level F1 (oracle cannot improve).")
    lines.append("Gated selection = LP selection on non-degenerate instances, greedy on degenerate.")
    lines.append("")

    # Main table
    lines.append("## Overall Results")
    lines.append("")
    hdr = "| Dataset | N_inst | N_samp | Degen% | Greedy_F1 | LP_F1 | Oracle_F1 | Gated_F1 | LP_vs_Greedy | Gated_vs_LP |"
    sep = "|---------|--------|--------|--------|-----------|-------|-----------|----------|--------------|-------------|"
    lines.append(hdr)
    lines.append(sep)
    for r in results:
        o = r["overall"]
        lines.append(
            f"| {r['dataset']} | {r['total_instances']} | {r['n_samples_per_instance']} "
            f"| {r['degeneracy_rate_pct']:.1f}% "
            f"| {o['greedy_f1']:.4f} | {o['lp_f1']:.4f} | {o['oracle_f1']:.4f} | {o['gated_f1']:.4f} "
            f"| {o['lp_vs_greedy']:+.4f} | {o['gated_vs_lp']:+.4f} |"
        )
    lines.append("")

    # Bootstrap CI table
    lines.append("## Bootstrap 95% CI for Key Deltas (1000 resamples)")
    lines.append("")
    hdr2 = "| Dataset | LP_vs_Greedy | CI_95 | Gated_vs_Greedy | CI_95 | Gated_vs_LP | CI_95 |"
    sep2 = "|---------|-------------|-------|-----------------|-------|-------------|-------|"
    lines.append(hdr2)
    lines.append(sep2)
    for r in results:
        o = r["overall"]
        lines.append(
            f"| {r['dataset']} "
            f"| {o['lp_vs_greedy']:+.4f} | {fmt_ci(o['ci_lp_vs_greedy'])} "
            f"| {o['gated_vs_greedy']:+.4f} | {fmt_ci(o['ci_gated_vs_greedy'])} "
            f"| {o['gated_vs_lp']:+.4f} | {fmt_ci(o['ci_gated_vs_lp'])} |"
        )
    lines.append("")

    # Non-degenerate subset
    lines.append("## Non-Degenerate Subset Analysis (Core: LP effectiveness where oracle can improve)")
    lines.append("")
    hdr3 = "| Dataset | N_nondeg | Greedy_F1 | LP_F1 | Oracle_F1 | LP_vs_Greedy | CI_95 |"
    sep3 = "|---------|----------|-----------|-------|-----------|--------------|-------|"
    lines.append(hdr3)
    lines.append(sep3)
    for r in results:
        nd = r["non_degenerate"]
        lines.append(
            f"| {r['dataset']} | {nd['count']} "
            f"| {nd['greedy_f1']:.4f} | {nd['lp_f1']:.4f} | {nd['oracle_f1']:.4f} "
            f"| {nd['lp_vs_greedy']:+.4f} | {fmt_ci(nd['ci_lp_vs_greedy'])} |"
        )
    lines.append("")

    # Degenerate subset
    lines.append("## Degenerate Subset (All samples identical F1)")
    lines.append("")
    hdr4 = "| Dataset | N_degen | Degen% | Greedy_F1 | CI_95 |"
    sep4 = "|---------|---------|--------|-----------|-------|"
    lines.append(hdr4)
    lines.append(sep4)
    for r in results:
        d = r["degenerate"]
        lines.append(
            f"| {r['dataset']} | {d['count']} | {r['degeneracy_rate_pct']:.1f}% "
            f"| {d['greedy_f1']:.4f} | {fmt_ci(d['ci_greedy'])} |"
        )
    lines.append("")

    # Key findings
    lines.append("## Key Findings")
    lines.append("")
    for r in results:
        o = r["overall"]
        nd = r["non_degenerate"]
        lines.append(f"### {r['dataset']}")
        lines.append(f"- Degeneracy rate: {r['degeneracy_rate_pct']:.1f}% ({r['degenerate_count']}/{r['total_instances']})")
        lines.append(f"- Overall LP vs Greedy: {o['lp_vs_greedy']:+.4f} CI {fmt_ci(o['ci_lp_vs_greedy'])}")
        lines.append(f"- Non-degenerate LP vs Greedy: {nd['lp_vs_greedy']:+.4f} CI {fmt_ci(nd['ci_lp_vs_greedy'])}")
        lines.append(f"- Gated vs ungated LP: {o['gated_vs_lp']:+.4f} CI {fmt_ci(o['ci_gated_vs_lp'])}")
        lines.append(f"- Oracle F1 gap (overall): {o['oracle_f1'] - o['greedy_f1']:+.4f}")
        lines.append("")

    report = "\n".join(lines)
    report_path = f"{out_dir}/report.md"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"\nReport saved to {report_path}")
    return report


def main():
    out_dir = f"{BASE}/output/d140_oracle_gated"
    os.makedirs(out_dir, exist_ok=True)

    all_results = []
    for name, path in DATASETS.items():
        r = analyze_dataset(name, path)
        if r:
            all_results.append(r)

    out_path = f"{out_dir}/results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")

    report = generate_report(all_results, out_dir)
    print("\n" + report)


if __name__ == "__main__":
    main()
