#!/usr/bin/env python3
"""DGS full validation across datasets with statistical significance testing."""

import argparse
import json
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import entity_strict_match


def parse_args():
    p = argparse.ArgumentParser(
        description="DGS full validation with bootstrap CI and permutation test"
    )
    p.add_argument(
        "--datasets", nargs="+", required=True,
        help="name:path pairs, e.g. SciERC:/path/to/samples.jsonl",
    )
    p.add_argument("--n-samples", type=int, default=8)
    p.add_argument("--n-bootstrap", type=int, default=10000)
    p.add_argument("--n-permutations", type=int, default=10000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", type=str, default=None, help="Output JSON path")
    p.add_argument("--dry-run", action="store_true", help="Print config and exit")
    return p.parse_args()


def load_instances(path, n_samples=8):
    instances = []
    with open(path) as f:
        for line in f:
            inst = json.loads(line)
            inst["samples"] = inst["samples"][:n_samples]
            instances.append(inst)
    return instances


def per_instance_entity_f1(pred_entities, gold_entities):
    tp, fp, fn = entity_strict_match(pred_entities, gold_entities)
    if tp + fp == 0 and tp + fn == 0:
        return 1.0
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def dgs_select(inst, n_samples=8):
    gold_ents = inst["gold"]["entities"]
    samples = inst["samples"][:n_samples]
    greedy = inst["greedy"]

    sample_f1s = [per_instance_entity_f1(s["entities"], gold_ents) for s in samples]
    is_degenerate = len(set(round(f, 10) for f in sample_f1s)) == 1

    lp_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])

    if is_degenerate:
        selected_ents = greedy["entities"]
        method = "greedy"
    else:
        selected_ents = samples[lp_idx]["entities"]
        method = "lp"

    return {
        "is_degenerate": is_degenerate,
        "greedy_f1": per_instance_entity_f1(greedy["entities"], gold_ents),
        "dgs_f1": per_instance_entity_f1(selected_ents, gold_ents),
        "lp_f1": per_instance_entity_f1(samples[lp_idx]["entities"], gold_ents),
        "oracle_f1": max(sample_f1s),
        "selected_entities": selected_ents,
        "greedy_entities": greedy["entities"],
        "lp_entities": samples[lp_idx]["entities"],
        "gold_entities": gold_ents,
        "method": method,
    }


def micro_f1_from_entity_lists(pred_list, gold_list):
    total_tp = total_fp = total_fn = 0
    for pred, gold in zip(pred_list, gold_list):
        tp, fp, fn = entity_strict_match(pred, gold)
        total_tp += tp
        total_fp += fp
        total_fn += fn
    if total_tp == 0:
        return 0.0
    p = total_tp / (total_tp + total_fp)
    r = total_tp / (total_tp + total_fn)
    return 2 * p * r / (p + r)


def bootstrap_ci(values, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    arr = np.array(values)
    n = len(arr)
    if n == 0:
        return {"mean": 0.0, "ci_lo": 0.0, "ci_hi": 0.0}
    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
    boot_means.sort()
    return {
        "mean": float(arr.mean()),
        "ci_lo": float(boot_means[int(0.025 * n_boot)]),
        "ci_hi": float(boot_means[int(0.975 * n_boot)]),
    }


def bootstrap_delta_ci(a, b, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    a_arr, b_arr = np.array(a), np.array(b)
    n = len(a_arr)
    if n == 0:
        return {"delta": 0.0, "ci_lo": 0.0, "ci_hi": 0.0, "significant": False}
    deltas = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        deltas.append(a_arr[idx].mean() - b_arr[idx].mean())
    deltas = sorted(deltas)
    lo = deltas[int(0.025 * n_boot)]
    hi = deltas[int(0.975 * n_boot)]
    return {
        "delta": float((a_arr - b_arr).mean()),
        "ci_lo": float(lo),
        "ci_hi": float(hi),
        "significant": bool(lo > 0 or hi < 0),
    }


def paired_permutation_test(a, b, n_perm=10000, seed=42):
    rng = np.random.RandomState(seed)
    a_arr, b_arr = np.array(a), np.array(b)
    observed = a_arr.mean() - b_arr.mean()
    diff = a_arr - b_arr
    n = len(diff)
    count = 0
    for _ in range(n_perm):
        signs = rng.choice([-1, 1], size=n)
        if abs((diff * signs).mean()) >= abs(observed):
            count += 1
    return {"observed_delta": float(observed), "p_value": float(count / n_perm)}


def analyze_dataset(instances, name, n_samples, n_boot, n_perm, seed):
    results = [dgs_select(inst, n_samples) for inst in instances]

    greedy_f1s = [r["greedy_f1"] for r in results]
    dgs_f1s = [r["dgs_f1"] for r in results]
    lp_f1s = [r["lp_f1"] for r in results]
    oracle_f1s = [r["oracle_f1"] for r in results]

    n_total = len(results)
    n_degen = sum(1 for r in results if r["is_degenerate"])

    golds = [r["gold_entities"] for r in results]
    micro_greedy = micro_f1_from_entity_lists([r["greedy_entities"] for r in results], golds)
    micro_dgs = micro_f1_from_entity_lists([r["selected_entities"] for r in results], golds)
    micro_lp = micro_f1_from_entity_lists([r["lp_entities"] for r in results], golds)

    greedy_ci = bootstrap_ci(greedy_f1s, n_boot, seed)
    dgs_ci = bootstrap_ci(dgs_f1s, n_boot, seed)
    lp_ci = bootstrap_ci(lp_f1s, n_boot, seed)
    oracle_ci = bootstrap_ci(oracle_f1s, n_boot, seed)
    delta_dgs_greedy = bootstrap_delta_ci(dgs_f1s, greedy_f1s, n_boot, seed)
    delta_dgs_lp = bootstrap_delta_ci(dgs_f1s, lp_f1s, n_boot, seed)

    perm_dgs_greedy = paired_permutation_test(dgs_f1s, greedy_f1s, n_perm, seed)
    perm_dgs_lp = paired_permutation_test(dgs_f1s, lp_f1s, n_perm, seed)

    degen_results = [r for r in results if r["is_degenerate"]]
    nondegen_results = [r for r in results if not r["is_degenerate"]]

    strat = {}
    if degen_results:
        strat["degenerate"] = {
            "n": len(degen_results),
            "greedy_f1": bootstrap_ci([r["greedy_f1"] for r in degen_results], n_boot, seed),
            "oracle_f1": bootstrap_ci([r["oracle_f1"] for r in degen_results], n_boot, seed),
        }
    if nondegen_results:
        nd_g = [r["greedy_f1"] for r in nondegen_results]
        nd_l = [r["lp_f1"] for r in nondegen_results]
        nd_o = [r["oracle_f1"] for r in nondegen_results]
        strat["nondegenerate"] = {
            "n": len(nondegen_results),
            "greedy_f1": bootstrap_ci(nd_g, n_boot, seed),
            "lp_f1": bootstrap_ci(nd_l, n_boot, seed),
            "oracle_f1": bootstrap_ci(nd_o, n_boot, seed),
            "delta_lp_greedy": bootstrap_delta_ci(nd_l, nd_g, n_boot, seed),
        }

    return {
        "dataset": name,
        "n_instances": n_total,
        "n_degenerate": n_degen,
        "degen_pct": round(n_degen / n_total * 100, 1),
        "macro": {"greedy": greedy_ci, "dgs": dgs_ci, "lp_all": lp_ci, "oracle": oracle_ci},
        "micro": {
            "greedy": round(micro_greedy, 4),
            "dgs": round(micro_dgs, 4),
            "lp_all": round(micro_lp, 4),
        },
        "delta_dgs_minus_greedy": delta_dgs_greedy,
        "delta_dgs_minus_lp": delta_dgs_lp,
        "permutation_test": {
            "dgs_vs_greedy": perm_dgs_greedy,
            "dgs_vs_lp": perm_dgs_lp,
        },
        "stratified": strat,
    }


def print_report(result):
    d = result
    print(f"\n{'='*60}")
    print(f"Dataset: {d['dataset']}")
    print(f"{'='*60}")
    print(f"Instances: {d['n_instances']}, Degenerate: {d['n_degenerate']} ({d['degen_pct']}%)")
    print(f"\n{'Method':<12} {'Macro F1':>10} {'95% CI':>24} {'Micro F1':>10}")
    print("-" * 60)
    for key, label in [("greedy", "Greedy"), ("dgs", "DGS"), ("lp_all", "LP-all"), ("oracle", "Oracle")]:
        m = d["macro"][key]
        mic = d["micro"].get(key, "")
        mic_s = f"{mic:.4f}" if isinstance(mic, float) else ""
        print(f"{label:<12} {m['mean']:>10.4f} [{m['ci_lo']:.4f}, {m['ci_hi']:.4f}] {mic_s:>10}")

    delta = d["delta_dgs_minus_greedy"]
    perm = d["permutation_test"]["dgs_vs_greedy"]
    sig = "*" if perm["p_value"] < 0.05 else ""
    print(f"\nDGS-Greedy: {delta['delta']:+.4f} [{delta['ci_lo']:.4f}, {delta['ci_hi']:.4f}] p={perm['p_value']:.4f}{sig}")

    delta2 = d["delta_dgs_minus_lp"]
    perm2 = d["permutation_test"]["dgs_vs_lp"]
    sig2 = "*" if perm2["p_value"] < 0.05 else ""
    print(f"DGS-LP:     {delta2['delta']:+.4f} [{delta2['ci_lo']:.4f}, {delta2['ci_hi']:.4f}] p={perm2['p_value']:.4f}{sig2}")

    if "degenerate" in d["stratified"]:
        s = d["stratified"]["degenerate"]
        print(f"\nDegenerate ({s['n']}): Greedy={s['greedy_f1']['mean']:.4f} Oracle={s['oracle_f1']['mean']:.4f}")
    if "nondegenerate" in d["stratified"]:
        s = d["stratified"]["nondegenerate"]
        dl = s["delta_lp_greedy"]
        print(f"Non-degen ({s['n']}): Greedy={s['greedy_f1']['mean']:.4f} LP={s['lp_f1']['mean']:.4f} Oracle={s['oracle_f1']['mean']:.4f} LP-Gre={dl['delta']:+.4f}")


def main():
    args = parse_args()
    if args.dry_run:
        print("DGS Full Validation [dry-run]")
        print(f"  datasets:       {args.datasets}")
        print(f"  n_samples:      {args.n_samples}")
        print(f"  n_bootstrap:    {args.n_bootstrap}")
        print(f"  n_permutations: {args.n_permutations}")
        print(f"  seed:           {args.seed}")
        print(f"  output:         {args.output}")
        return

    all_results = {}
    for ds in args.datasets:
        name, path = ds.split(":", 1)
        print(f"Loading {name} from {path}...")
        instances = load_instances(path, args.n_samples)
        print(f"  {len(instances)} instances loaded")
        result = analyze_dataset(
            instances, name, args.n_samples,
            args.n_bootstrap, args.n_permutations, args.seed,
        )
        all_results[name] = result
        print_report(result)

    output = {
        "config": {
            "n_samples": args.n_samples,
            "n_bootstrap": args.n_bootstrap,
            "n_permutations": args.n_permutations,
            "seed": args.seed,
        },
        "datasets": all_results,
    }

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nJSON saved to {args.output}")


if __name__ == "__main__":
    main()
