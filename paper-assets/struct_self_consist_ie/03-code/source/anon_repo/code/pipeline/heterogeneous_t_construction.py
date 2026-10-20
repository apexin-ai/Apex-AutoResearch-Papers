#!/usr/bin/env python3
"""Heterogeneous-T entity construction experiment (DGEC Exp C).

Hypothesis: mixing samples from T=0.7 (conservative) and T=1.0 (diverse)
breaks degeneracy while preserving signal quality, improving construction
over single-T pools.
"""

import json
import math
import os
import sys
import numpy as np
from collections import defaultdict, Counter
from sklearn.model_selection import KFold

BASE = "/root/autodl-tmp/struct_self_consist_ie"

T07_PATH = f"{BASE}/output/exp_lp_scierc_t07/samples.jsonl"
T10_PATHS = {
    42: f"{BASE}/output/exp_026_t10_seed42/samples.jsonl",
    123: f"{BASE}/output/exp_026_t10_seed123/samples.jsonl",
    456: f"{BASE}/output/exp_026_t10_seed456/samples.jsonl",
}
T08_PATHS = {
    123: f"{BASE}/output/exp_026_t08_seed123/samples.jsonl",
    456: f"{BASE}/output/exp_026_t08_seed456/samples.jsonl",
}

OUTPUT_DIR = f"{BASE}/output/exp_dgec_heterogeneous_t"
N_BOOT = 10000
THETA_FIXED = 0.25
THETA_GRID = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]


def load_data(path, gold_filter=True):
    instances = {}
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances[obj["id"]] = obj
    return instances


def entity_set(entities):
    return frozenset((e["start"], e["end"], e["type"]) for e in entities)


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


def compute_degeneracy(instances):
    """Fraction of instances where all samples produce identical entity set."""
    n_degen = 0
    for inst in instances:
        sets = [entity_set(s.get("entities", [])) for s in inst["samples"]]
        if len(set(sets)) == 1:
            n_degen += 1
    return n_degen / len(instances) if instances else 0.0


def compute_mean_unique_outputs(instances):
    """Mean number of distinct entity sets across samples per instance."""
    counts = []
    for inst in instances:
        sets = [entity_set(s.get("entities", [])) for s in inst["samples"]]
        counts.append(len(set(sets)))
    return float(np.mean(counts))


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


def paired_bootstrap_test(f1s_a, f1s_b, n_boot=10000):
    """One-sided test: H1 is mean(b) > mean(a). Returns (obs_diff, p_value)."""
    a = np.array(f1s_a)
    b = np.array(f1s_b)
    obs_diff = float(np.mean(b) - np.mean(a))
    n = len(a)
    rng = np.random.RandomState(42)
    count = 0
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        if np.mean(b[idx]) - np.mean(a[idx]) <= 0:
            count += 1
    return obs_diff, count / n_boot


def cv_theta_search(instances, gold_sets, weight_fn=None, n_folds=5):
    indices = np.arange(len(instances))
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)
    fold_thetas = []
    fold_f1s = []
    for train_idx, test_idx in kf.split(indices):
        best_theta, best_f1 = 0.5, -1
        for theta in THETA_GRID:
            f1s = []
            for i in train_idx:
                samples = instances[i]["samples"]
                ws = weight_fn(samples) if weight_fn else None
                pred = weighted_construction(samples, theta, weights=ws)
                f1s.append(compute_f1(pred, gold_sets[i]))
            mean_f1 = np.mean(f1s)
            if mean_f1 > best_f1:
                best_f1 = mean_f1
                best_theta = theta
        f1s = []
        for i in test_idx:
            samples = instances[i]["samples"]
            ws = weight_fn(samples) if weight_fn else None
            pred = weighted_construction(samples, best_theta, weights=ws)
            f1s.append(compute_f1(pred, gold_sets[i]))
        fold_thetas.append(best_theta)
        fold_f1s.append(float(np.mean(f1s)))
    return {
        "F1": float(np.mean(fold_f1s)),
        "std": float(np.std(fold_f1s)),
        "fold_f1s": fold_f1s,
        "fold_thetas": fold_thetas,
    }


def evaluate_pool(instances, label):
    """Full evaluation of a sample pool: degeneracy, construction, bootstrap."""
    gold_sets = [entity_set(inst["gold"].get("entities", [])) for inst in instances]

    greedy_f1s = [
        compute_f1(entity_set(inst["greedy"].get("entities", [])), gold_sets[i])
        for i, inst in enumerate(instances)
    ]

    degen = compute_degeneracy(instances)
    mean_unique = compute_mean_unique_outputs(instances)

    # Fixed-theta construction
    uniform_f1s = []
    vc_f1s = []
    for i, inst in enumerate(instances):
        pred = weighted_construction(inst["samples"], THETA_FIXED)
        uniform_f1s.append(compute_f1(pred, gold_sets[i]))
        vc_ws = get_vc_weights(inst["samples"])
        pred = weighted_construction(inst["samples"], THETA_FIXED, weights=vc_ws)
        vc_f1s.append(compute_f1(pred, gold_sets[i]))

    uniform_diff, uniform_p = paired_bootstrap_test(greedy_f1s, uniform_f1s, N_BOOT)
    vc_diff, vc_p = paired_bootstrap_test(greedy_f1s, vc_f1s, N_BOOT)

    # CV theta search
    uniform_cv = cv_theta_search(instances, gold_sets, weight_fn=None)
    vc_cv = cv_theta_search(instances, gold_sets, weight_fn=get_vc_weights)

    return {
        "label": label,
        "n_instances": len(instances),
        "n_samples": len(instances[0]["samples"]),
        "greedy_f1": float(np.mean(greedy_f1s)),
        "degeneracy": degen,
        "mean_unique_outputs": mean_unique,
        "uniform_fixed": {
            "theta": THETA_FIXED,
            "F1": float(np.mean(uniform_f1s)),
            "delta_vs_greedy": uniform_diff,
            "p_vs_greedy": uniform_p,
            "significant": uniform_p < 0.05,
        },
        "vc_fixed": {
            "theta": THETA_FIXED,
            "F1": float(np.mean(vc_f1s)),
            "delta_vs_greedy": vc_diff,
            "p_vs_greedy": vc_p,
            "significant": vc_p < 0.05,
        },
        "uniform_cv": uniform_cv,
        "vc_cv": vc_cv,
        "_greedy_f1s": greedy_f1s,
        "_uniform_f1s": uniform_f1s,
        "_vc_f1s": vc_f1s,
    }


def cross_pool_bootstrap(pool_a_instances, pool_b_instances, gold_sets, label):
    """Compare two pools at fixed theta. Returns delta and p for uniform and VC."""
    a_uniform, a_vc, b_uniform, b_vc = [], [], [], []
    for i in range(len(pool_a_instances)):
        sa = pool_a_instances[i]["samples"]
        sb = pool_b_instances[i]["samples"]
        gold = gold_sets[i]

        a_uniform.append(compute_f1(weighted_construction(sa, THETA_FIXED), gold))
        b_uniform.append(compute_f1(weighted_construction(sb, THETA_FIXED), gold))

        a_vc_ws = get_vc_weights(sa)
        b_vc_ws = get_vc_weights(sb)
        a_vc.append(compute_f1(weighted_construction(sa, THETA_FIXED, weights=a_vc_ws), gold))
        b_vc.append(compute_f1(weighted_construction(sb, THETA_FIXED, weights=b_vc_ws), gold))

    u_diff, u_p = paired_bootstrap_test(a_uniform, b_uniform, N_BOOT)
    v_diff, v_p = paired_bootstrap_test(a_vc, b_vc, N_BOOT)

    return {
        "label": label,
        "theta": THETA_FIXED,
        "uniform": {
            "pool_a_f1": float(np.mean(a_uniform)),
            "pool_b_f1": float(np.mean(b_uniform)),
            "delta": u_diff,
            "p": u_p,
            "significant": u_p < 0.05,
        },
        "vc": {
            "pool_a_f1": float(np.mean(a_vc)),
            "pool_b_f1": float(np.mean(b_vc)),
            "delta": v_diff,
            "p": v_p,
            "significant": v_p < 0.05,
        },
    }


def mix_samples(inst_low, inst_high, n_low=4, n_high=4):
    return {
        "id": inst_low["id"],
        "text": inst_low["text"],
        "gold": inst_low["gold"],
        "greedy": inst_low["greedy"],
        "samples": inst_low["samples"][:n_low] + inst_high["samples"][:n_high],
    }


def run_pair(t_low_data, t_high_data, t_low_label, t_high_label, n_low=4, n_high=4):
    common_ids = sorted(set(t_low_data.keys()) & set(t_high_data.keys()))
    print(f"  Common instances: {len(common_ids)}", flush=True)

    # M030: verify greedy
    greedy_match = sum(
        1 for iid in common_ids
        if json.dumps(t_low_data[iid]["greedy"].get("entities", []), sort_keys=True)
        == json.dumps(t_high_data[iid]["greedy"].get("entities", []), sort_keys=True)
    )
    print(f"  M030 greedy match: {greedy_match}/{len(common_ids)}", flush=True)

    t_low_instances = [t_low_data[iid] for iid in common_ids]
    t_high_instances = [t_high_data[iid] for iid in common_ids]
    mixed_instances = [
        mix_samples(t_low_data[iid], t_high_data[iid], n_low, n_high)
        for iid in common_ids
    ]
    gold_sets = [entity_set(t_low_data[iid]["gold"].get("entities", [])) for iid in common_ids]

    print(f"  Evaluating {t_low_label} only...", flush=True)
    r_low = evaluate_pool(t_low_instances, f"{t_low_label}_only")

    print(f"  Evaluating {t_high_label} only...", flush=True)
    r_high = evaluate_pool(t_high_instances, f"{t_high_label}_only")

    print(f"  Evaluating mixed ({n_low}+{n_high})...", flush=True)
    r_mixed = evaluate_pool(mixed_instances, f"mixed_{t_low_label}_{t_high_label}")

    # Cross-pool: mixed vs high-T
    print("  Cross-pool bootstrap (mixed vs high-T)...", flush=True)
    cross = cross_pool_bootstrap(
        t_high_instances, mixed_instances, gold_sets,
        f"mixed_vs_{t_high_label}"
    )

    # Remove internal F1 vectors before serialization
    for r in [r_low, r_high, r_mixed]:
        for k in list(r.keys()):
            if k.startswith("_"):
                del r[k]

    result = {
        "t_low": t_low_label,
        "t_high": t_high_label,
        "n_low": n_low,
        "n_high": n_high,
        "n_instances": len(common_ids),
        "m030_greedy_match": f"{greedy_match}/{len(common_ids)}",
        "pool_low": r_low,
        "pool_high": r_high,
        "pool_mixed": r_mixed,
        "cross_mixed_vs_high": cross,
    }

    # Print summary
    print(f"\n  {'Pool':<15} {'Degen':>7} {'UniqueOut':>9} {'Greedy':>8} {'Unif':>8} {'VC':>8}", flush=True)
    print(f"  {'-'*60}", flush=True)
    for name, r in [(t_low_label, r_low), (t_high_label, r_high), ("Mixed", r_mixed)]:
        sig_u = "*" if r["uniform_fixed"]["significant"] else " "
        sig_v = "*" if r["vc_fixed"]["significant"] else " "
        print(
            f"  {name:<15} {r['degeneracy']:>7.4f} {r['mean_unique_outputs']:>9.2f} "
            f"{r['greedy_f1']:>8.4f} {r['uniform_fixed']['F1']:>7.4f}{sig_u} "
            f"{r['vc_fixed']['F1']:>7.4f}{sig_v}",
            flush=True,
        )
    cx = cross
    sig_u = "*" if cx["uniform"]["significant"] else ""
    sig_v = "*" if cx["vc"]["significant"] else ""
    print(f"\n  Cross (mixed vs {t_high_label}):", flush=True)
    print(f"    Uniform: Δ={cx['uniform']['delta']:+.4f} p={cx['uniform']['p']:.4f}{sig_u}", flush=True)
    print(f"    VC:      Δ={cx['vc']['delta']:+.4f} p={cx['vc']['p']:.4f}{sig_v}", flush=True)

    return result


def generate_summary(results):
    lines = [
        "# Heterogeneous-T Entity Construction — Results",
        "",
        "## Experiment Design",
        "- **Hypothesis**: Mixed-T pools (T=0.7 conservative + T=1.0 diverse) break degeneracy,",
        "  improving entity construction over single-T pools.",
        "- **Pool composition**: 4 samples from T_low + 4 samples from T_high = 8 total",
        "- **Dataset**: SciERC NER (551 instances, gold-filtered)",
        f"- **Fixed θ**: {THETA_FIXED} (matching construction_variants baseline)",
        f"- **Bootstrap**: B={N_BOOT}, paired, one-sided",
        "",
    ]

    for key, r in sorted(results.items()):
        if key == "aggregate":
            continue
        lines.append(f"## {key}")
        lines.append(f"Instances: {r['n_instances']}, M030 greedy match: {r['m030_greedy_match']}")
        lines.append("")

        lines.append("### Degeneracy & Diversity")
        lines.append("| Pool | Degeneracy | Mean Unique Outputs |")
        lines.append("|------|-----------|-------------------|")
        for pname, pkey in [(r["t_low"], "pool_low"), (r["t_high"], "pool_high"), ("Mixed", "pool_mixed")]:
            p = r[pkey]
            lines.append(f"| {pname} | {p['degeneracy']:.4f} | {p['mean_unique_outputs']:.2f} |")
        lines.append("")

        lines.append(f"### Construction at θ={THETA_FIXED} (vs Greedy)")
        lines.append("| Pool | Greedy | Uniform | ΔF1 | p | VC | ΔF1 | p |")
        lines.append("|------|--------|---------|-----|---|----|----|---|")
        for pname, pkey in [(r["t_low"], "pool_low"), (r["t_high"], "pool_high"), ("Mixed", "pool_mixed")]:
            p = r[pkey]
            su = "\\*" if p["uniform_fixed"]["significant"] else ""
            sv = "\\*" if p["vc_fixed"]["significant"] else ""
            lines.append(
                f"| {pname} | {p['greedy_f1']:.4f} | "
                f"{p['uniform_fixed']['F1']:.4f} | {p['uniform_fixed']['delta_vs_greedy']:+.4f}{su} | "
                f"{p['uniform_fixed']['p_vs_greedy']:.4f} | "
                f"{p['vc_fixed']['F1']:.4f} | {p['vc_fixed']['delta_vs_greedy']:+.4f}{sv} | "
                f"{p['vc_fixed']['p_vs_greedy']:.4f} |"
            )
        lines.append("")

        lines.append("### CV-Optimized Construction")
        lines.append("| Pool | Uniform CV F1 | θ modes | VC CV F1 | θ modes |")
        lines.append("|------|-------------|---------|----------|---------|")
        for pname, pkey in [(r["t_low"], "pool_low"), (r["t_high"], "pool_high"), ("Mixed", "pool_mixed")]:
            p = r[pkey]
            lines.append(
                f"| {pname} | {p['uniform_cv']['F1']:.4f}±{p['uniform_cv']['std']:.4f} | "
                f"{p['uniform_cv']['fold_thetas']} | "
                f"{p['vc_cv']['F1']:.4f}±{p['vc_cv']['std']:.4f} | "
                f"{p['vc_cv']['fold_thetas']} |"
            )
        lines.append("")

        cx = r["cross_mixed_vs_high"]
        lines.append(f"### Cross-Pool: Mixed vs {r['t_high']} (at θ={cx['theta']})")
        sig_u = " **significant**" if cx["uniform"]["significant"] else " n.s."
        sig_v = " **significant**" if cx["vc"]["significant"] else " n.s."
        lines.append(
            f"- Uniform: mixed={cx['uniform']['pool_b_f1']:.4f} vs "
            f"{r['t_high']}={cx['uniform']['pool_a_f1']:.4f}, "
            f"Δ={cx['uniform']['delta']:+.4f}, p={cx['uniform']['p']:.4f}{sig_u}"
        )
        lines.append(
            f"- VC: mixed={cx['vc']['pool_b_f1']:.4f} vs "
            f"{r['t_high']}={cx['vc']['pool_a_f1']:.4f}, "
            f"Δ={cx['vc']['delta']:+.4f}, p={cx['vc']['p']:.4f}{sig_v}"
        )
        lines.append("")

    if "aggregate" in results:
        agg = results["aggregate"]
        lines.append("## Aggregate Across Seeds")
        lines.append("")
        lines.append("### Degeneracy")
        for key in ["t_low", "t_high", "mixed"]:
            d = agg["degeneracy"]
            lines.append(f"- {key}: {d[key]:.4f}")
        lines.append("")
        lines.append("### Construction F1 (fixed θ)")
        for method in ["uniform", "vc"]:
            m = agg[f"{method}_construction"]
            lines.append(f"- {method}: low={m['low_f1']:.4f}, high={m['high_f1']:.4f}, mixed={m['mixed_f1']:.4f}")
            lines.append(f"  cross Δ(mixed-high) = {m['cross_delta']:.4f}")
        lines.append("")

    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading T=0.7 data...", flush=True)
    t07_data = load_data(T07_PATH)
    print(f"  {len(t07_data)} instances", flush=True)

    results = {}

    # Primary: T=0.7 + T=1.0 for each seed
    for seed, t10_path in sorted(T10_PATHS.items()):
        if not os.path.exists(t10_path):
            print(f"SKIP T=1.0 seed {seed}", flush=True)
            continue
        print(f"\n{'='*60}", flush=True)
        print(f"  T=0.7 + T=1.0 seed={seed}", flush=True)
        print(f"{'='*60}", flush=True)
        t10_data = load_data(t10_path)
        key = f"t07_t10_s{seed}"
        results[key] = run_pair(t07_data, t10_data, "T=0.7", "T=1.0", n_low=4, n_high=4)
        results[key]["seed"] = seed

    # Secondary: T=0.8 + T=1.0
    for seed, t08_path in sorted(T08_PATHS.items()):
        t10_path = T10_PATHS.get(seed)
        if not os.path.exists(t08_path) or not t10_path or not os.path.exists(t10_path):
            continue
        print(f"\n{'='*60}", flush=True)
        print(f"  T=0.8 + T=1.0 seed={seed}", flush=True)
        print(f"{'='*60}", flush=True)
        t08_data = load_data(t08_path)
        t10_data = load_data(t10_path)
        key = f"t08_t10_s{seed}"
        results[key] = run_pair(t08_data, t10_data, "T=0.8", "T=1.0", n_low=4, n_high=4)
        results[key]["seed"] = seed

    # Aggregate T=0.7+T=1.0 results
    t07_t10_keys = [k for k in results if k.startswith("t07_t10_")]
    if len(t07_t10_keys) > 1:
        agg = {
            "n_seeds": len(t07_t10_keys),
            "seeds": [results[k]["seed"] for k in t07_t10_keys],
            "degeneracy": {
                "t_low": float(np.mean([results[k]["pool_low"]["degeneracy"] for k in t07_t10_keys])),
                "t_high": float(np.mean([results[k]["pool_high"]["degeneracy"] for k in t07_t10_keys])),
                "mixed": float(np.mean([results[k]["pool_mixed"]["degeneracy"] for k in t07_t10_keys])),
            },
        }
        for method in ["uniform", "vc"]:
            fkey = f"{method}_fixed"
            agg[f"{method}_construction"] = {
                "low_f1": float(np.mean([results[k]["pool_low"][fkey]["F1"] for k in t07_t10_keys])),
                "high_f1": float(np.mean([results[k]["pool_high"][fkey]["F1"] for k in t07_t10_keys])),
                "mixed_f1": float(np.mean([results[k]["pool_mixed"][fkey]["F1"] for k in t07_t10_keys])),
                "cross_delta": float(np.mean([
                    results[k]["cross_mixed_vs_high"][method]["delta"] for k in t07_t10_keys
                ])),
                "cross_p_values": [
                    results[k]["cross_mixed_vs_high"][method]["p"] for k in t07_t10_keys
                ],
            }
        results["aggregate"] = agg

    # Save
    out_path = os.path.join(OUTPUT_DIR, "heterogeneous_t_results.json")
    serializable = json.loads(json.dumps(results, default=float))
    with open(out_path, "w") as f:
        json.dump(serializable, f, indent=2)
    print(f"\nResults saved to: {out_path}", flush=True)

    summary = generate_summary(results)
    summary_path = os.path.join(OUTPUT_DIR, "summary.md")
    with open(summary_path, "w") as f:
        f.write(summary)
    print(f"Summary saved to: {summary_path}", flush=True)

    print("\nDONE", flush=True)


if __name__ == "__main__":
    main()
