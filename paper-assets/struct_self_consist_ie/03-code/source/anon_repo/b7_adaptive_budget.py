"""B7 Adaptive Sampling Budget Analysis.

Compare uniform N=8 vs adaptive (high-conf N=2, low-conf N=8).
"""
import json
import os
import numpy as np
from collections import defaultdict

# ---------------------------------------------------------------
# Data paths
# ---------------------------------------------------------------
BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
DATASETS = {
    "fewnerd_qwen3_8b": f"{BASE}/exp_021_inference/samples.jsonl",
    "scierc_qwen3_8b": f"{BASE}/exp_029b_scierc_10epoch/samples.jsonl",
}
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/b7_adaptive_budget"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------
# Entity construction & evaluation
# ---------------------------------------------------------------
def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def entity_majority_vote(samples, threshold=0.5):
    counts = defaultdict(int)
    N = len(samples)
    for s in samples:
        for e in s.get("entities", []):
            counts[(e["start"], e["end"], e["type"])] += 1
    return {k for k, c in counts.items() if c / N >= threshold}

def compute_tp_fp_fn(pred_set, gold_set):
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return tp, fp, fn

def micro_prf(tp_total, fp_total, fn_total):
    if tp_total == 0:
        return 0.0, 0.0, 0.0
    p = tp_total / (tp_total + fp_total)
    r = tp_total / (tp_total + fn_total)
    f = 2 * p * r / (p + r)
    return p, r, f

def instance_f1(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r)

# ---------------------------------------------------------------
# Load data
# ---------------------------------------------------------------
def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            instances.append(json.loads(line))
    return instances

# ---------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------
def run_analysis(dataset_name, instances):
    print(f"\n{'='*60}")
    print(f"Dataset: {dataset_name} ({len(instances)} instances)")
    print(f"{'='*60}")

    # Extract greedy LP for each instance
    greedy_lps = []
    for inst in instances:
        glp = inst["greedy"]["mean_logprob"]
        greedy_lps.append(glp)

    greedy_lps = np.array(greedy_lps)
    median_lp = np.median(greedy_lps)
    print(f"Greedy LP: mean={greedy_lps.mean():.4f}, median={median_lp:.4f}, "
          f"min={greedy_lps.min():.4f}, max={greedy_lps.max():.4f}")

    # Split: high-conf = LP >= median (higher = more confident, less negative)
    high_conf_idx = [i for i in range(len(instances)) if greedy_lps[i] >= median_lp]
    low_conf_idx = [i for i in range(len(instances)) if greedy_lps[i] < median_lp]
    print(f"High-conf (LP >= {median_lp:.4f}): {len(high_conf_idx)} instances")
    print(f"Low-conf  (LP <  {median_lp:.4f}): {len(low_conf_idx)} instances")

    # Strategy 1: Uniform N=8 (all instances, all 8 samples)
    # Strategy 2: Adaptive (high-conf N=2, low-conf N=8)
    # Strategy 3: Greedy only (baseline)

    strategies = {
        "greedy": {},
        "uniform_n8": {},
        "adaptive_h2_l8": {},
        "adaptive_h1_l8": {},
        "uniform_n2": {},
    }

    # Per-instance results
    for i, inst in enumerate(instances):
        gold = entity_set(inst["gold"]["entities"])
        samples = inst["samples"]
        greedy_pred = entity_set(inst["greedy"]["entities"])

        # Greedy
        strategies["greedy"][i] = (greedy_pred, gold)

        # Uniform N=8: all 8 samples, threshold=0.5
        pred_n8 = entity_majority_vote(samples[:8], threshold=0.5)
        strategies["uniform_n8"][i] = (pred_n8, gold)

        # Uniform N=2: only first 2 samples
        pred_n2 = entity_majority_vote(samples[:2], threshold=0.5)
        strategies["uniform_n2"][i] = (pred_n2, gold)

        # Adaptive: high-conf gets N=2, low-conf gets N=8
        if i in set(high_conf_idx):
            pred_adaptive = entity_majority_vote(samples[:2], threshold=0.5)
            strategies["adaptive_h2_l8"][i] = (pred_adaptive, gold)
        else:
            pred_adaptive = entity_majority_vote(samples[:8], threshold=0.5)
            strategies["adaptive_h2_l8"][i] = (pred_adaptive, gold)

        # Adaptive variant: high-conf gets N=1 (greedy), low-conf gets N=8
        if i in set(high_conf_idx):
            strategies["adaptive_h1_l8"][i] = (greedy_pred, gold)
        else:
            pred_adaptive2 = entity_majority_vote(samples[:8], threshold=0.5)
            strategies["adaptive_h1_l8"][i] = (pred_adaptive2, gold)

    # Compute metrics for each strategy
    results = {}
    M = len(instances)

    for strat_name, preds in strategies.items():
        tp_total, fp_total, fn_total = 0, 0, 0
        f1_per_instance = []
        f1_high = []
        f1_low = []

        for i in range(M):
            pred_set, gold_set = preds[i]
            tp, fp, fn = compute_tp_fp_fn(pred_set, gold_set)
            tp_total += tp
            fp_total += fp
            fn_total += fn
            f1_i = instance_f1(pred_set, gold_set)
            f1_per_instance.append(f1_i)
            if i in set(high_conf_idx):
                f1_high.append(f1_i)
            else:
                f1_low.append(f1_i)

        p, r, f = micro_prf(tp_total, fp_total, fn_total)
        macro_f1 = np.mean(f1_per_instance)
        macro_f1_high = np.mean(f1_high) if f1_high else 0.0
        macro_f1_low = np.mean(f1_low) if f1_low else 0.0

        # Sample count
        if strat_name == "greedy":
            total_samples = M  # 1 per instance
        elif strat_name == "uniform_n8":
            total_samples = M * 8
        elif strat_name == "uniform_n2":
            total_samples = M * 2
        elif strat_name == "adaptive_h2_l8":
            total_samples = len(high_conf_idx) * 2 + len(low_conf_idx) * 8
        elif strat_name == "adaptive_h1_l8":
            total_samples = len(high_conf_idx) * 1 + len(low_conf_idx) * 8

        results[strat_name] = {
            "micro_p": round(p * 100, 2),
            "micro_r": round(r * 100, 2),
            "micro_f1": round(f * 100, 2),
            "macro_f1": round(macro_f1 * 100, 2),
            "macro_f1_high_conf": round(macro_f1_high * 100, 2),
            "macro_f1_low_conf": round(macro_f1_low * 100, 2),
            "total_samples": total_samples,
            "samples_vs_uniform8": round(total_samples / (M * 8) * 100, 1),
            "tp": tp_total, "fp": fp_total, "fn": fn_total,
        }

        print(f"\n  {strat_name}:")
        print(f"    Micro F1={f*100:.2f}  P={p*100:.2f}  R={r*100:.2f}")
        print(f"    Macro F1={macro_f1*100:.2f}  (high={macro_f1_high*100:.2f}, low={macro_f1_low*100:.2f})")
        print(f"    Samples: {total_samples} ({total_samples/(M*8)*100:.1f}% of uniform N=8)")

    # Efficiency analysis
    uniform_f1 = results["uniform_n8"]["micro_f1"]
    adaptive_f1 = results["adaptive_h2_l8"]["micro_f1"]
    adaptive_samples_pct = results["adaptive_h2_l8"]["samples_vs_uniform8"]
    savings = 100 - adaptive_samples_pct
    f1_loss = uniform_f1 - adaptive_f1

    print(f"\n  Summary:")
    print(f"    Adaptive saves {savings:.1f}% samples, F1 delta = {f1_loss:+.2f}")

    # Additional: sweep different high-conf sample counts
    sweep_results = {}
    for n_high in [1, 2, 3, 4, 5, 6, 7]:
        tp_t, fp_t, fn_t = 0, 0, 0
        for i, inst in enumerate(instances):
            gold = entity_set(inst["gold"]["entities"])
            samples = inst["samples"]
            if i in set(high_conf_idx):
                if n_high == 1:
                    pred = entity_set(inst["greedy"]["entities"])
                else:
                    pred = entity_majority_vote(samples[:n_high], threshold=0.5)
            else:
                pred = entity_majority_vote(samples[:8], threshold=0.5)
            tp, fp, fn = compute_tp_fp_fn(pred, gold)
            tp_t += tp
            fp_t += fp
            fn_t += fn
        _, _, f = micro_prf(tp_t, fp_t, fn_t)
        total_s = len(high_conf_idx) * n_high + len(low_conf_idx) * 8
        sweep_results[f"adaptive_h{n_high}_l8"] = {
            "micro_f1": round(f * 100, 2),
            "total_samples": total_s,
            "samples_pct": round(total_s / (M * 8) * 100, 1),
            "f1_delta_vs_uniform8": round(f * 100 - uniform_f1, 2),
            "savings_pct": round((1 - total_s / (M * 8)) * 100, 1),
        }

    print(f"\n  Sweep (high-conf N varies, low-conf fixed N=8):")
    for k, v in sweep_results.items():
        print(f"    {k}: F1={v['micro_f1']:.2f}, "
              f"delta={v['f1_delta_vs_uniform8']:+.2f}, "
              f"savings={v['savings_pct']:.1f}%")

    # Confidence percentile sweep
    percentile_results = {}
    for pct in [25, 33, 50, 67, 75]:
        threshold_lp = np.percentile(greedy_lps, 100 - pct)
        hi_idx = [i for i in range(M) if greedy_lps[i] >= threshold_lp]
        lo_idx = [i for i in range(M) if greedy_lps[i] < threshold_lp]
        tp_t, fp_t, fn_t = 0, 0, 0
        for i, inst in enumerate(instances):
            gold = entity_set(inst["gold"]["entities"])
            samples = inst["samples"]
            if i in set(hi_idx):
                pred = entity_majority_vote(samples[:2], threshold=0.5)
            else:
                pred = entity_majority_vote(samples[:8], threshold=0.5)
            tp, fp, fn = compute_tp_fp_fn(pred, gold)
            tp_t += tp
            fp_t += fp
            fn_t += fn
        _, _, f = micro_prf(tp_t, fp_t, fn_t)
        total_s = len(hi_idx) * 2 + len(lo_idx) * 8
        percentile_results[f"top{pct}pct_h2_l8"] = {
            "high_conf_pct": pct,
            "n_high": len(hi_idx),
            "n_low": len(lo_idx),
            "micro_f1": round(f * 100, 2),
            "total_samples": total_s,
            "samples_pct": round(total_s / (M * 8) * 100, 1),
            "f1_delta_vs_uniform8": round(f * 100 - uniform_f1, 2),
            "savings_pct": round((1 - total_s / (M * 8)) * 100, 1),
        }

    print(f"\n  Percentile sweep (top X% as high-conf, h=2, l=8):")
    for k, v in percentile_results.items():
        print(f"    {k}: F1={v['micro_f1']:.2f}, "
              f"delta={v['f1_delta_vs_uniform8']:+.2f}, "
              f"savings={v['savings_pct']:.1f}%, "
              f"hi={v['n_high']}, lo={v['n_low']}")

    return {
        "n_instances": M,
        "median_greedy_lp": round(float(median_lp), 6),
        "greedy_lp_stats": {
            "mean": round(float(greedy_lps.mean()), 6),
            "std": round(float(greedy_lps.std()), 6),
            "min": round(float(greedy_lps.min()), 6),
            "max": round(float(greedy_lps.max()), 6),
        },
        "n_high_conf": len(high_conf_idx),
        "n_low_conf": len(low_conf_idx),
        "strategies": results,
        "sweep_high_conf_n": sweep_results,
        "percentile_sweep": percentile_results,
    }

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------
all_results = {}
for name, path in DATASETS.items():
    print(f"\nLoading {name} from {path}...")
    instances = load_data(path)
    all_results[name] = run_analysis(name, instances)

# Efficiency summary
print("\n" + "="*60)
print("OVERALL EFFICIENCY SUMMARY")
print("="*60)
for name, res in all_results.items():
    u8 = res["strategies"]["uniform_n8"]
    a28 = res["strategies"]["adaptive_h2_l8"]
    a18 = res["strategies"]["adaptive_h1_l8"]
    greedy = res["strategies"]["greedy"]
    print(f"\n{name}:")
    print(f"  Greedy:          F1={greedy['micro_f1']:.2f}  ({greedy['total_samples']} samples, {greedy['samples_vs_uniform8']:.1f}%)")
    print(f"  Uniform N=2:     F1={res['strategies']['uniform_n2']['micro_f1']:.2f}  ({res['strategies']['uniform_n2']['total_samples']} samples, {res['strategies']['uniform_n2']['samples_vs_uniform8']:.1f}%)")
    print(f"  Uniform N=8:     F1={u8['micro_f1']:.2f}  ({u8['total_samples']} samples, 100%)")
    print(f"  Adaptive h2/l8:  F1={a28['micro_f1']:.2f}  ({a28['total_samples']} samples, {a28['samples_vs_uniform8']:.1f}%)")
    print(f"  Adaptive h1/l8:  F1={a18['micro_f1']:.2f}  ({a18['total_samples']} samples, {a18['samples_vs_uniform8']:.1f}%)")
    f1_loss_28 = u8['micro_f1'] - a28['micro_f1']
    savings_28 = 100 - a28['samples_vs_uniform8']
    f1_loss_18 = u8['micro_f1'] - a18['micro_f1']
    savings_18 = 100 - a18['samples_vs_uniform8']
    print(f"  h2/l8: saves {savings_28:.1f}%, F1 loss={f1_loss_28:.2f}")
    print(f"  h1/l8: saves {savings_18:.1f}%, F1 loss={f1_loss_18:.2f}")
    # Best sweep point
    best_sweep = min(res["sweep_high_conf_n"].items(),
                     key=lambda x: abs(x[1]["f1_delta_vs_uniform8"]))
    print(f"  Best sweep: {best_sweep[0]} → F1={best_sweep[1]['micro_f1']:.2f}, "
          f"savings={best_sweep[1]['savings_pct']:.1f}%")

# Recommendation
print("\n" + "="*60)
print("RECOMMENDATION")
print("="*60)
for name, res in all_results.items():
    u8_f1 = res["strategies"]["uniform_n8"]["micro_f1"]
    # Find the most efficient adaptive strategy with <0.5 F1 loss
    candidates = []
    for k, v in res["sweep_high_conf_n"].items():
        if abs(v["f1_delta_vs_uniform8"]) <= 0.5:
            candidates.append((k, v))
    if candidates:
        best = max(candidates, key=lambda x: x[1]["savings_pct"])
        print(f"  {name}: Use {best[0]} — saves {best[1]['savings_pct']:.1f}% "
              f"with only {abs(best[1]['f1_delta_vs_uniform8']):.2f} F1 loss")
    else:
        print(f"  {name}: No adaptive strategy within 0.5 F1 of uniform N=8")

# Save JSON
output = {
    "experiment": "B7_adaptive_sampling_budget",
    "description": "Compare uniform N=8 vs adaptive allocation based on greedy LP confidence",
    "method": "Split instances by median greedy mean_logprob; high-conf uses fewer samples, low-conf uses N=8. Entity construction via majority vote (threshold=0.5).",
    "datasets": all_results,
}
out_path = os.path.join(OUTPUT_DIR, "adaptive_analysis.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nSaved to {out_path}")
