#!/usr/bin/env python3
"""Cross-model DGS validation: verify DGS is model-agnostic (e.g. LLaMA data)."""

import argparse
import json
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import entity_strict_match


def parse_args():
    p = argparse.ArgumentParser(
        description="Cross-model DGS validation (model-agnostic check)"
    )
    p.add_argument(
        "--datasets", nargs="+", required=True,
        help="name:path pairs, e.g. LLaMA-SciERC:/path/to/samples.jsonl",
    )
    p.add_argument(
        "--reference-results", type=str, default=None,
        help="JSON from full_validation to compare against (optional)",
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
    boots = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
    boots.sort()
    return {
        "mean": float(arr.mean()),
        "ci_lo": float(boots[int(0.025 * n_boot)]),
        "ci_hi": float(boots[int(0.975 * n_boot)]),
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
    gold_list, greedy_list, dgs_list, lp_list = [], [], [], []
    greedy_f1s, dgs_f1s, lp_f1s, oracle_f1s = [], [], [], []
    n_degen = 0

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        samples = inst["samples"][:n_samples]
        greedy = inst["greedy"]

        sample_f1s = [per_instance_entity_f1(s["entities"], gold_ents) for s in samples]
        is_degen = len(set(round(f, 10) for f in sample_f1s)) == 1
        lp_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])

        if is_degen:
            selected_ents = greedy["entities"]
            n_degen += 1
        else:
            selected_ents = samples[lp_idx]["entities"]

        gold_list.append(gold_ents)
        greedy_list.append(greedy["entities"])
        dgs_list.append(selected_ents)
        lp_list.append(samples[lp_idx]["entities"])

        greedy_f1s.append(per_instance_entity_f1(greedy["entities"], gold_ents))
        dgs_f1s.append(per_instance_entity_f1(selected_ents, gold_ents))
        lp_f1s.append(per_instance_entity_f1(samples[lp_idx]["entities"], gold_ents))
        oracle_f1s.append(max(sample_f1s))

    n_total = len(instances)
    return {
        "dataset": name,
        "n_instances": n_total,
        "n_degenerate": n_degen,
        "degen_pct": round(n_degen / n_total * 100, 1),
        "macro": {
            "greedy": bootstrap_ci(greedy_f1s, n_boot, seed),
            "dgs": bootstrap_ci(dgs_f1s, n_boot, seed),
            "lp_all": bootstrap_ci(lp_f1s, n_boot, seed),
            "oracle": bootstrap_ci(oracle_f1s, n_boot, seed),
        },
        "micro": {
            "greedy": round(micro_f1_from_entity_lists(greedy_list, gold_list), 4),
            "dgs": round(micro_f1_from_entity_lists(dgs_list, gold_list), 4),
            "lp_all": round(micro_f1_from_entity_lists(lp_list, gold_list), 4),
        },
        "delta_dgs_minus_greedy": bootstrap_delta_ci(dgs_f1s, greedy_f1s, n_boot, seed),
        "delta_dgs_minus_lp": bootstrap_delta_ci(dgs_f1s, lp_f1s, n_boot, seed),
        "permutation_test": {
            "dgs_vs_greedy": paired_permutation_test(dgs_f1s, greedy_f1s, n_perm, seed),
            "dgs_vs_lp": paired_permutation_test(dgs_f1s, lp_f1s, n_perm, seed),
        },
    }


def print_report(r, ref=None):
    print(f"\n{'='*65}")
    print(f"Dataset: {r['dataset']}")
    print(f"{'='*65}")
    print(f"Instances: {r['n_instances']}, Degenerate: {r['n_degenerate']} ({r['degen_pct']}%)")
    print(f"\n{'Method':<12} {'Macro F1':>10} {'95% CI':>24} {'Micro F1':>10}")
    print("-" * 60)
    for key, label in [("greedy", "Greedy"), ("dgs", "DGS"), ("lp_all", "LP-all"), ("oracle", "Oracle")]:
        m = r["macro"][key]
        mic = r["micro"].get(key, "")
        mic_s = f"{mic:.4f}" if isinstance(mic, float) else ""
        print(f"{label:<12} {m['mean']:>10.4f} [{m['ci_lo']:.4f}, {m['ci_hi']:.4f}] {mic_s:>10}")

    d = r["delta_dgs_minus_greedy"]
    p = r["permutation_test"]["dgs_vs_greedy"]
    print(f"\nDGS-Greedy: {d['delta']:+.4f} [{d['ci_lo']:.4f}, {d['ci_hi']:.4f}] p={p['p_value']:.4f}")
    d2 = r["delta_dgs_minus_lp"]
    p2 = r["permutation_test"]["dgs_vs_lp"]
    print(f"DGS-LP:     {d2['delta']:+.4f} [{d2['ci_lo']:.4f}, {d2['ci_hi']:.4f}] p={p2['p_value']:.4f}")

    if ref:
        print(f"\n--- Cross-model comparison ---")
        for key in ["greedy", "dgs", "lp_all", "oracle"]:
            rm = ref["macro"][key]["mean"]
            cm = r["macro"][key]["mean"]
            print(f"  {key:<10} ref={rm:.4f} this={cm:.4f} diff={cm-rm:+.4f}")


def main():
    args = parse_args()
    if args.dry_run:
        print("DGS Cross-Model Validation [dry-run]")
        print(f"  datasets:          {args.datasets}")
        print(f"  reference_results: {args.reference_results}")
        print(f"  n_samples:         {args.n_samples}")
        print(f"  n_bootstrap:       {args.n_bootstrap}")
        print(f"  n_permutations:    {args.n_permutations}")
        print(f"  seed:              {args.seed}")
        print(f"  output:            {args.output}")
        return

    ref_data = None
    if args.reference_results and os.path.exists(args.reference_results):
        with open(args.reference_results) as f:
            ref_data = json.load(f)

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

        ref = None
        if ref_data:
            for ref_name in ref_data.get("datasets", {}):
                if ref_name.lower() in name.lower() or name.lower() in ref_name.lower():
                    ref = ref_data["datasets"][ref_name]
                    break
        print_report(result, ref)

    output = {
        "config": {
            "n_samples": args.n_samples,
            "n_bootstrap": args.n_bootstrap,
            "n_permutations": args.n_permutations,
            "seed": args.seed,
        },
        "datasets": all_results,
        "model_agnostic_check": {
            name: {
                "dgs_improves_over_greedy": r["delta_dgs_minus_greedy"]["delta"] > 0,
                "dgs_improves_over_lp": r["delta_dgs_minus_lp"]["delta"] > 0,
                "dgs_greedy_significant": r["permutation_test"]["dgs_vs_greedy"]["p_value"] < 0.05,
            }
            for name, r in all_results.items()
        },
    }

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nJSON saved to {args.output}")


if __name__ == "__main__":
    main()
