#!/usr/bin/env python3
"""Heterogeneous-Temperature Sampling for Entity Construction.

Mix samples from T_low and T_high to break degeneracy while retaining precision.
Evaluates multiple mix ratios with threshold-sweep majority vote.

exp_id: exp_backup1_het_temp
Parent: exp_mrsc_multi_round (post MRSC/LSC negative)
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_samples(path, max_instances=0):
    data = []
    with open(path) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    if max_instances > 0:
        data = data[:max_instances]
    return data


def load_paired_data(t_low_path, t_high_path, max_instances=0):
    """Load and align T_low / T_high samples by instance id."""
    raw_low = load_samples(t_low_path, max_instances=0)
    raw_high = load_samples(t_high_path, max_instances=0)

    low_by_id = {inst["id"]: inst for inst in raw_low}
    high_by_id = {inst["id"]: inst for inst in raw_high}

    common_ids = sorted(set(low_by_id) & set(high_by_id))
    if not common_ids:
        low_by_text = {inst["text"]: inst for inst in raw_low}
        high_by_text = {inst["text"]: inst for inst in raw_high}
        common_texts = sorted(set(low_by_text) & set(high_by_text))
        if not common_texts:
            print("ERROR: no overlapping instances between T_low and T_high", file=sys.stderr)
            sys.exit(1)
        paired = []
        for t in common_texts:
            lo, hi = low_by_text[t], high_by_text[t]
            paired.append({
                "id": lo.get("id", t[:60]),
                "text": t,
                "gold": lo["gold"],
                "t_low_samples": lo["samples"],
                "t_high_samples": hi["samples"],
            })
    else:
        paired = []
        for iid in common_ids:
            lo, hi = low_by_id[iid], high_by_id[iid]
            paired.append({
                "id": iid,
                "text": lo["text"],
                "gold": lo["gold"],
                "t_low_samples": lo["samples"],
                "t_high_samples": hi["samples"],
            })

    if max_instances > 0:
        paired = paired[:max_instances]

    print(f"Paired instances: {len(paired)}  "
          f"(T_low={len(raw_low)}, T_high={len(raw_high)}, overlap={len(paired)})")
    return paired


# ---------------------------------------------------------------------------
# Entity helpers
# ---------------------------------------------------------------------------

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def entity_set_text(entities):
    """Fallback: use (text, type) when offsets are unreliable."""
    return {(e["text"], e["type"]) for e in entities}


def compute_prf(pred_set, gold_set):
    if not pred_set and not gold_set:
        return 1.0, 1.0, 1.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set) if pred_set else 0.0
    r = tp / len(gold_set) if gold_set else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) else 0.0
    return p, r, f1


# ---------------------------------------------------------------------------
# Majority vote with threshold sweep
# ---------------------------------------------------------------------------

def majority_vote_entities(samples, threshold):
    """Return entity set where agreement >= threshold."""
    N = len(samples)
    if N == 0:
        return set()
    counts = defaultdict(int)
    for s in samples:
        for e in entity_set(s.get("entities", [])):
            counts[e] += 1
    return {e for e, c in counts.items() if c / N >= threshold}


def best_threshold_f1(paired_data, pool_key, thresholds):
    """Sweep thresholds, return (best_f1, best_theta, all_f1s)."""
    results_by_theta = {}
    for theta in thresholds:
        tp_total, pred_total, gold_total = 0, 0, 0
        for inst in paired_data:
            gold = entity_set(inst["gold"].get("entities", []))
            pred = majority_vote_entities(inst[pool_key], theta)
            tp_total += len(pred & gold)
            pred_total += len(pred)
            gold_total += len(gold)
        p = tp_total / pred_total if pred_total else 0.0
        r = tp_total / gold_total if gold_total else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) else 0.0
        results_by_theta[theta] = f1

    best_theta = max(results_by_theta, key=results_by_theta.get)
    return results_by_theta[best_theta], best_theta, results_by_theta


# ---------------------------------------------------------------------------
# Sampling / mixing
# ---------------------------------------------------------------------------

def mix_samples(t_low_samples, t_high_samples, k_low, k_high, rng):
    """Random mix: k_low from T_low + k_high from T_high."""
    n_low = min(k_low, len(t_low_samples))
    n_high = min(k_high, len(t_high_samples))
    idx_low = rng.choice(len(t_low_samples), n_low, replace=False)
    idx_high = rng.choice(len(t_high_samples), n_high, replace=False)
    return [t_low_samples[i] for i in idx_low] + [t_high_samples[i] for i in idx_high]


def subsample_pure(samples, n, rng):
    """Random subsample n from a single pool."""
    n = min(n, len(samples))
    idx = rng.choice(len(samples), n, replace=False)
    return [samples[i] for i in idx]


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def compute_degeneracy(paired_data, pool_key):
    """Fraction of instances where all samples produce the same entity set."""
    n_degen = 0
    for inst in paired_data:
        samples = inst[pool_key]
        if not samples:
            continue
        sets = [frozenset(entity_set(s.get("entities", []))) for s in samples]
        if len(set(sets)) == 1:
            n_degen += 1
    return n_degen / len(paired_data) if paired_data else 0.0


def compute_oracle_f1(paired_data, pool_key):
    """Best single-sample F1 per instance, then micro-average."""
    tp_total, pred_total, gold_total = 0, 0, 0
    for inst in paired_data:
        gold = entity_set(inst["gold"].get("entities", []))
        best_f1 = -1.0
        best_pred = set()
        for s in inst[pool_key]:
            pred = entity_set(s.get("entities", []))
            _, _, f1 = compute_prf(pred, gold)
            if f1 > best_f1:
                best_f1 = f1
                best_pred = pred
        tp_total += len(best_pred & gold)
        pred_total += len(best_pred)
        gold_total += len(gold)
    p = tp_total / pred_total if pred_total else 0.0
    r = tp_total / gold_total if gold_total else 0.0
    return 2 * p * r / (p + r) if (p + r) else 0.0


def compute_agreement_stats(paired_data, pool_key):
    """Per-entity agreement distribution across samples."""
    all_agreements = []
    for inst in paired_data:
        samples = inst[pool_key]
        N = len(samples)
        if N == 0:
            continue
        counts = defaultdict(int)
        for s in samples:
            for e in entity_set(s.get("entities", [])):
                counts[e] += 1
        for e, c in counts.items():
            all_agreements.append(c / N)
    if not all_agreements:
        return {"mean": 0, "std": 0, "median": 0, "n_entities": 0}
    arr = np.array(all_agreements)
    return {
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr)),
        "median": float(np.median(arr)),
        "n_entities": len(arr),
        "pct_below_50": float(np.mean(arr < 0.5) * 100),
        "pct_above_75": float(np.mean(arr >= 0.75) * 100),
    }


def compute_mean_unique_outputs(paired_data, pool_key):
    """Mean number of distinct entity sets across samples per instance."""
    uniques = []
    for inst in paired_data:
        samples = inst[pool_key]
        if not samples:
            continue
        sets = [frozenset(entity_set(s.get("entities", []))) for s in samples]
        uniques.append(len(set(sets)))
    return float(np.mean(uniques)) if uniques else 0.0


def compute_lp_range(paired_data, pool_key):
    """Within-instance logprob range (max - min mean_logprob)."""
    ranges = []
    for inst in paired_data:
        lps = []
        for s in inst[pool_key]:
            if "mean_logprob" in s:
                lps.append(s["mean_logprob"])
        if len(lps) >= 2:
            ranges.append(max(lps) - min(lps))
    if not ranges:
        return None
    arr = np.array(ranges)
    return {"mean": float(np.mean(arr)), "std": float(np.std(arr)), "n": len(arr)}


# ---------------------------------------------------------------------------
# Single configuration evaluation
# ---------------------------------------------------------------------------

THRESHOLDS = [round(t, 2) for t in np.arange(0.10, 0.95, 0.05)]


def evaluate_pool(paired_data, pool_key):
    """Full evaluation on a named pool."""
    best_f1, best_theta, f1_by_theta = best_threshold_f1(
        paired_data, pool_key, THRESHOLDS
    )
    degeneracy = compute_degeneracy(paired_data, pool_key)
    oracle = compute_oracle_f1(paired_data, pool_key)
    agreement = compute_agreement_stats(paired_data, pool_key)
    unique_outputs = compute_mean_unique_outputs(paired_data, pool_key)
    lp_range = compute_lp_range(paired_data, pool_key)

    return {
        "best_f1": best_f1,
        "best_theta": best_theta,
        "f1_by_theta": {str(k): v for k, v in f1_by_theta.items()},
        "degeneracy": degeneracy,
        "oracle_f1": oracle,
        "agreement": agreement,
        "mean_unique_outputs": unique_outputs,
        "lp_range": lp_range,
    }


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run_experiment(paired_data, n_total, mix_ratios, n_repeats, seed):
    """Run all mix ratios + baselines with repeated random sampling."""
    rng = np.random.RandomState(seed)
    all_results = {}

    configs = []
    for k_low, k_high in mix_ratios:
        configs.append((f"mix_{k_low}:{k_high}", k_low, k_high))
    configs.append((f"pure_t_low_{n_total}", n_total, 0))
    configs.append((f"pure_t_high_{n_total}", 0, n_total))

    for config_name, k_low, k_high in configs:
        print(f"\n{'='*60}")
        print(f"Config: {config_name}  (k_low={k_low}, k_high={k_high}, repeats={n_repeats})")
        print(f"{'='*60}")

        repeat_results = []
        for rep in range(n_repeats):
            rep_seed = rng.randint(0, 2**31)
            rep_rng = np.random.RandomState(rep_seed)

            for inst in paired_data:
                if k_low > 0 and k_high > 0:
                    inst["_pool"] = mix_samples(
                        inst["t_low_samples"], inst["t_high_samples"],
                        k_low, k_high, rep_rng
                    )
                elif k_high == 0:
                    inst["_pool"] = subsample_pure(inst["t_low_samples"], k_low, rep_rng)
                else:
                    inst["_pool"] = subsample_pure(inst["t_high_samples"], k_high, rep_rng)

            metrics = evaluate_pool(paired_data, "_pool")
            repeat_results.append(metrics)

        agg = aggregate_repeats(repeat_results)
        all_results[config_name] = agg

        print(f"  F1:          {agg['best_f1_mean']:.4f} ± {agg['best_f1_std']:.4f}  (θ modes: {agg['best_theta_modes']})")
        print(f"  Degeneracy:  {agg['degeneracy_mean']:.4f} ± {agg['degeneracy_std']:.4f}")
        print(f"  Oracle F1:   {agg['oracle_f1_mean']:.4f} ± {agg['oracle_f1_std']:.4f}")
        print(f"  Unique outs: {agg['unique_outputs_mean']:.2f} ± {agg['unique_outputs_std']:.2f}")
        agree = agg["agreement_mean_mean"]
        print(f"  Agreement:   mean={agree:.4f}, <50%={agg['agreement_pct_below_50_mean']:.1f}%, ≥75%={agg['agreement_pct_above_75_mean']:.1f}%")

    return all_results


def aggregate_repeats(repeat_results):
    """Aggregate metrics across repeated random samplings."""
    f1s = [r["best_f1"] for r in repeat_results]
    thetas = [r["best_theta"] for r in repeat_results]
    degens = [r["degeneracy"] for r in repeat_results]
    oracles = [r["oracle_f1"] for r in repeat_results]
    uniques = [r["mean_unique_outputs"] for r in repeat_results]
    agree_means = [r["agreement"]["mean"] for r in repeat_results]
    agree_below50 = [r["agreement"]["pct_below_50"] for r in repeat_results]
    agree_above75 = [r["agreement"]["pct_above_75"] for r in repeat_results]

    from collections import Counter
    theta_counts = Counter(thetas)
    theta_modes = [t for t, _ in theta_counts.most_common(3)]

    agg = {
        "best_f1_mean": float(np.mean(f1s)),
        "best_f1_std": float(np.std(f1s)),
        "best_f1_all": f1s,
        "best_theta_modes": theta_modes,
        "degeneracy_mean": float(np.mean(degens)),
        "degeneracy_std": float(np.std(degens)),
        "oracle_f1_mean": float(np.mean(oracles)),
        "oracle_f1_std": float(np.std(oracles)),
        "unique_outputs_mean": float(np.mean(uniques)),
        "unique_outputs_std": float(np.std(uniques)),
        "agreement_mean_mean": float(np.mean(agree_means)),
        "agreement_pct_below_50_mean": float(np.mean(agree_below50)),
        "agreement_pct_above_75_mean": float(np.mean(agree_above75)),
    }

    f1_by_theta_all = defaultdict(list)
    for r in repeat_results:
        for theta_str, f1 in r["f1_by_theta"].items():
            f1_by_theta_all[theta_str].append(f1)
    agg["f1_by_theta_mean"] = {
        k: float(np.mean(v)) for k, v in f1_by_theta_all.items()
    }

    lp_ranges = [r["lp_range"] for r in repeat_results if r["lp_range"] is not None]
    if lp_ranges:
        agg["lp_range_mean"] = float(np.mean([lr["mean"] for lr in lp_ranges]))
    else:
        agg["lp_range_mean"] = None

    return agg


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------

def print_summary_table(results, t_low_label, t_high_label):
    print(f"\n{'='*80}")
    print(f"SUMMARY: {t_low_label} vs {t_high_label}")
    print(f"{'='*80}")

    header = f"{'Config':<22} {'F1 (best θ)':<18} {'Degen':<12} {'Oracle':<12} {'Unique':<10} {'Agree':<10}"
    print(header)
    print("-" * 80)

    sorted_keys = sorted(results.keys(), key=lambda k: (
        0 if "pure_t_low" in k else (2 if "pure_t_high" in k else 1),
        k
    ))

    for name in sorted_keys:
        r = results[name]
        f1_str = f"{r['best_f1_mean']:.4f}±{r['best_f1_std']:.4f}"
        degen_str = f"{r['degeneracy_mean']:.4f}"
        oracle_str = f"{r['oracle_f1_mean']:.4f}"
        unique_str = f"{r['unique_outputs_mean']:.2f}"
        agree_str = f"{r['agreement_mean_mean']:.4f}"
        print(f"{name:<22} {f1_str:<18} {degen_str:<12} {oracle_str:<12} {unique_str:<10} {agree_str:<10}")

    print()
    t_low_key = [k for k in results if "pure_t_low" in k]
    t_high_key = [k for k in results if "pure_t_high" in k]
    if t_low_key and t_high_key:
        f1_low = results[t_low_key[0]]["best_f1_mean"]
        f1_high = results[t_high_key[0]]["best_f1_mean"]
        best_mix = max(
            ((k, v) for k, v in results.items() if "mix_" in k),
            key=lambda x: x[1]["best_f1_mean"]
        )
        f1_mix = best_mix[1]["best_f1_mean"]
        print(f"Best mix: {best_mix[0]}  F1={f1_mix:.4f}")
        print(f"  vs pure_t_low:  Δ={f1_mix - f1_low:+.4f}")
        print(f"  vs pure_t_high: Δ={f1_mix - f1_high:+.4f}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Heterogeneous-Temperature Sampling for Entity Construction")
    p.add_argument("--t_low_path", required=True, help="T_low samples JSONL")
    p.add_argument("--t_high_path", required=True, help="T_high samples JSONL")
    p.add_argument("--t_low_label", default="T_low", help="Label for T_low (e.g. 'T=0.8')")
    p.add_argument("--t_high_label", default="T_high", help="Label for T_high (e.g. 'T=1.0')")
    p.add_argument("--output_dir", required=True)
    p.add_argument("--n_total", type=int, default=8, help="Total pool size per instance")
    p.add_argument("--n_repeats", type=int, default=10)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_instances", type=int, default=0, help="0 = all")
    p.add_argument("--mix_ratios", type=str, default="2:6,3:5,4:4,5:3,6:2",
                   help="Comma-separated k_low:k_high ratios")
    return p.parse_args()


def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    mix_ratios = []
    for ratio_str in args.mix_ratios.split(","):
        kl, kh = ratio_str.strip().split(":")
        kl, kh = int(kl), int(kh)
        assert kl + kh == args.n_total, f"mix ratio {kl}:{kh} doesn't sum to {args.n_total}"
        mix_ratios.append((kl, kh))

    print(f"T_low:  {args.t_low_label}  <- {args.t_low_path}")
    print(f"T_high: {args.t_high_label} <- {args.t_high_path}")
    print(f"Mix ratios: {mix_ratios}")
    print(f"N_total={args.n_total}, repeats={args.n_repeats}, seed={args.seed}")
    print()

    paired = load_paired_data(args.t_low_path, args.t_high_path, args.max_instances)

    n_low_samples = [len(inst["t_low_samples"]) for inst in paired]
    n_high_samples = [len(inst["t_high_samples"]) for inst in paired]
    print(f"T_low samples/instance:  min={min(n_low_samples)}, max={max(n_low_samples)}, "
          f"mean={np.mean(n_low_samples):.1f}")
    print(f"T_high samples/instance: min={min(n_high_samples)}, max={max(n_high_samples)}, "
          f"mean={np.mean(n_high_samples):.1f}")

    has_lp = any("mean_logprob" in s for inst in paired for s in inst["t_low_samples"][:1])
    print(f"Logprobs available: {has_lp}")

    n_gold_empty = sum(1 for inst in paired if not inst["gold"].get("entities"))
    print(f"Gold-empty instances: {n_gold_empty}")
    print()

    results = run_experiment(paired, args.n_total, mix_ratios, args.n_repeats, args.seed)

    print_summary_table(results, args.t_low_label, args.t_high_label)

    output = {
        "config": {
            "t_low_path": args.t_low_path,
            "t_high_path": args.t_high_path,
            "t_low_label": args.t_low_label,
            "t_high_label": args.t_high_label,
            "n_total": args.n_total,
            "n_repeats": args.n_repeats,
            "seed": args.seed,
            "mix_ratios": [f"{kl}:{kh}" for kl, kh in mix_ratios],
            "n_instances": len(paired),
            "has_logprobs": has_lp,
        },
        "results": results,
    }

    out_path = os.path.join(args.output_dir, "het_temp_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
