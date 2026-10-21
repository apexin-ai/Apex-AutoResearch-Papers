#!/usr/bin/env python3
"""DGS ablation: independent contribution of degeneracy gating vs LP discriminativeness."""

import argparse
import json
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import entity_strict_match


def parse_args():
    p = argparse.ArgumentParser(
        description="DGS ablation: degen-only vs lp-only vs full"
    )
    p.add_argument(
        "--datasets", nargs="+", required=True,
        help="name:path pairs, e.g. SciERC:/path/to/samples.jsonl",
    )
    p.add_argument("--n-samples", type=int, default=8)
    p.add_argument("--n-bootstrap", type=int, default=10000)
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


def compute_instance_features(inst, n_samples=8):
    gold_ents = inst["gold"]["entities"]
    samples = inst["samples"][:n_samples]
    greedy = inst["greedy"]

    sample_f1s = [per_instance_entity_f1(s["entities"], gold_ents) for s in samples]
    is_degenerate = len(set(round(f, 10) for f in sample_f1s)) == 1

    lps = [s["mean_logprob"] for s in samples]
    lp_range = max(lps) - min(lps)
    lp_idx = max(range(len(samples)), key=lambda i: lps[i])

    return {
        "is_degenerate": is_degenerate,
        "lp_range": lp_range,
        "greedy_f1": per_instance_entity_f1(greedy["entities"], gold_ents),
        "lp_f1": per_instance_entity_f1(samples[lp_idx]["entities"], gold_ents),
        "oracle_f1": max(sample_f1s),
    }


STRATEGIES = ["greedy", "lp_all", "dgs_degen_only", "dgs_lp_only", "dgs_full"]
LABELS = {
    "greedy": "Greedy",
    "lp_all": "LP-all",
    "dgs_degen_only": "DGS-degen-only",
    "dgs_lp_only": "DGS-lp-only",
    "dgs_full": "DGS-full",
}


def apply_strategy(feat, strategy, lp_thresh):
    g, lp = feat["greedy_f1"], feat["lp_f1"]
    if strategy == "greedy":
        return g
    if strategy == "lp_all":
        return lp
    if strategy == "dgs_degen_only":
        return g if feat["is_degenerate"] else lp
    if strategy == "dgs_lp_only":
        return lp if feat["lp_range"] > lp_thresh else g
    if strategy == "dgs_full":
        if feat["is_degenerate"]:
            return g
        return lp if feat["lp_range"] > lp_thresh else g
    raise ValueError(strategy)


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


def analyze_dataset(instances, name, n_samples, n_boot, seed):
    feats = [compute_instance_features(inst, n_samples) for inst in instances]
    lp_ranges = [f["lp_range"] for f in feats]
    lp_thresh = float(np.median(lp_ranges))

    n_degen = sum(1 for f in feats if f["is_degenerate"])
    n_lp_gated = sum(1 for f in feats if f["lp_range"] > lp_thresh)
    n_both = sum(1 for f in feats if not f["is_degenerate"] and f["lp_range"] > lp_thresh)

    strategy_results = {}
    for strat in STRATEGIES:
        f1s = [apply_strategy(f, strat, lp_thresh) for f in feats]
        strategy_results[strat] = bootstrap_ci(f1s, n_boot, seed)

    oracle_ci = bootstrap_ci([f["oracle_f1"] for f in feats], n_boot, seed)

    return {
        "dataset": name,
        "n_instances": len(instances),
        "n_degenerate": n_degen,
        "degen_pct": round(n_degen / len(instances) * 100, 1),
        "lp_range_median_threshold": round(lp_thresh, 6),
        "n_lp_gated": n_lp_gated,
        "n_both_gates_active": n_both,
        "strategies": strategy_results,
        "oracle": oracle_ci,
    }


def print_report(r):
    print(f"\n{'='*65}")
    print(f"Dataset: {r['dataset']} (n={r['n_instances']})")
    print(f"Degenerate: {r['n_degenerate']} ({r['degen_pct']}%)")
    print(f"LP range threshold (median): {r['lp_range_median_threshold']:.6f}")
    print(f"LP-gated: {r['n_lp_gated']}, Both gates active: {r['n_both_gates_active']}")
    print(f"{'='*65}")
    print(f"\n{'Strategy':<18} {'Macro F1':>10} {'95% CI':>24}")
    print("-" * 56)
    for strat in STRATEGIES:
        ci = r["strategies"][strat]
        print(f"{LABELS[strat]:<18} {ci['mean']:>10.4f} [{ci['ci_lo']:.4f}, {ci['ci_hi']:.4f}]")
    oc = r["oracle"]
    print(f"{'Oracle':<18} {oc['mean']:>10.4f} [{oc['ci_lo']:.4f}, {oc['ci_hi']:.4f}]")

    best_strat = max(STRATEGIES, key=lambda s: r["strategies"][s]["mean"])
    print(f"\nBest strategy: {LABELS[best_strat]} ({r['strategies'][best_strat]['mean']:.4f})")


def main():
    args = parse_args()
    if args.dry_run:
        print("DGS Ablation [dry-run]")
        print(f"  datasets:    {args.datasets}")
        print(f"  n_samples:   {args.n_samples}")
        print(f"  n_bootstrap: {args.n_bootstrap}")
        print(f"  seed:        {args.seed}")
        print(f"  output:      {args.output}")
        print(f"  strategies:  {', '.join(LABELS[s] for s in STRATEGIES)}")
        return

    all_results = {}
    for ds in args.datasets:
        name, path = ds.split(":", 1)
        print(f"Loading {name} from {path}...")
        instances = load_instances(path, args.n_samples)
        print(f"  {len(instances)} instances loaded")
        result = analyze_dataset(instances, name, args.n_samples, args.n_bootstrap, args.seed)
        all_results[name] = result
        print_report(result)

    output = {
        "config": {
            "n_samples": args.n_samples,
            "n_bootstrap": args.n_bootstrap,
            "seed": args.seed,
            "strategies": STRATEGIES,
            "strategy_labels": LABELS,
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
