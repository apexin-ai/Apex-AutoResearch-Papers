import json, math, sys
from scipy.stats import binomtest
from collections import Counter

def analyze_exp(name, path):
    with open(path) as f:
        data = json.load(f)
    
    summary = data["summary"]
    results = data["results"]
    n = summary["n_problems"]
    sc_acc = summary["sc_accuracy"]
    sica_acc = summary["sica_accuracy"]
    sc_correct_n = summary["sc_correct"]
    sica_correct_n = summary["sica_correct"]
    
    # Discordant pairs
    b = 0  # SICA correct, SC wrong
    c = 0  # SC correct, SICA wrong
    both_correct = 0
    both_wrong = 0
    
    # Per answer type
    gt_counts = Counter()
    gt_sc_correct = Counter()
    gt_sica_correct = Counter()
    
    # Entropy analysis
    entropy_data = []
    
    for r in results:
        sc_c = r["sc_correct"]
        sica_c = r["sica_correct"]
        gt = r["ground_truth"]
        
        gt_counts[gt] += 1
        if sc_c:
            gt_sc_correct[gt] += 1
        if sica_c:
            gt_sica_correct[gt] += 1
        
        if sica_c and not sc_c:
            b += 1
        elif sc_c and not sica_c:
            c += 1
        elif sc_c and sica_c:
            both_correct += 1
        else:
            both_wrong += 1
        
        # Entropy from SC vote distribution
        vote_dist = r["sc_vote_distribution"]
        total_votes = sum(vote_dist.values())
        if total_votes > 0:
            probs = [v / total_votes for v in vote_dist.values() if v > 0]
            entropy = -sum(p * math.log2(p) for p in probs)
        else:
            entropy = 0.0
        
        entropy_data.append({
            "entropy": entropy,
            "sc_correct": sc_c,
            "sica_correct": sica_c,
            "gt": gt
        })
    
    # McNemar test
    if b + c > 0:
        p_value = binomtest(b, b + c, 0.5).pvalue
    else:
        p_value = 1.0
    
    # Entropy bins
    bins = [
        ("low [0, 0.5)", 0.0, 0.5),
        ("medium [0.5, 1.0)", 0.5, 1.0),
        ("high [1.0+)", 1.0, float("inf"))
    ]
    entropy_breakdown = []
    for label, lo, hi in bins:
        subset = [e for e in entropy_data if lo <= e["entropy"] < hi]
        n_sub = len(subset)
        if n_sub > 0:
            sc_pct = 100 * sum(1 for e in subset if e["sc_correct"]) / n_sub
            sica_pct = 100 * sum(1 for e in subset if e["sica_correct"]) / n_sub
        else:
            sc_pct = sica_pct = 0.0
        entropy_breakdown.append({
            "bin": label,
            "n": n_sub,
            "sc_pct": round(sc_pct, 2),
            "sica_pct": round(sica_pct, 2),
            "delta": round(sica_pct - sc_pct, 2)
        })
    
    # Per answer type
    answer_types = sorted(gt_counts.keys())
    per_type = []
    for t in answer_types:
        n_t = gt_counts[t]
        sc_t = gt_sc_correct.get(t, 0)
        sica_t = gt_sica_correct.get(t, 0)
        per_type.append({
            "type": t,
            "n": n_t,
            "sc_correct": sc_t,
            "sc_pct": round(100 * sc_t / n_t, 2),
            "sica_correct": sica_t,
            "sica_pct": round(100 * sica_t / n_t, 2),
            "delta": round(100 * (sica_t - sc_t) / n_t, 2)
        })
    
    result = {
        "experiment": name,
        "n": n,
        "sc_accuracy_pct": round(100 * sc_acc, 2),
        "sica_accuracy_pct": round(100 * sica_acc, 2),
        "delta_pct": round(100 * (sica_acc - sc_acc), 2),
        "sc_correct": sc_correct_n,
        "sica_correct": sica_correct_n,
        "both_correct": both_correct,
        "both_wrong": both_wrong,
        "b_sica_correct_sc_wrong": b,
        "c_sc_correct_sica_wrong": c,
        "mcnemar_p_value": p_value,
        "significant_0.05": p_value < 0.05,
        "per_answer_type": per_type,
        "entropy_conditioned": entropy_breakdown
    }
    return result

# Analyze both experiments
exp052 = analyze_exp(
    "exp-052 (seed=123)",
    "/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json"
)
exp053 = analyze_exp(
    "exp-053 (seed=456)",
    "/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json"
)

# exp-033 reference values (from user's table)
exp033 = {
    "experiment": "exp-033 (seed=42)",
    "n": 204,
    "sc_accuracy_pct": 54.41,
    "sica_accuracy_pct": 59.31,
    "delta_pct": 4.90,
    "b_sica_correct_sc_wrong": 12,
    "c_sc_correct_sica_wrong": 2,
    "mcnemar_p_value": 0.013,
    "significant_0.05": True
}

# Cross-seed summary
import numpy as np
deltas = [exp033["delta_pct"], exp052["delta_pct"], exp053["delta_pct"]]
sc_accs = [exp033["sc_accuracy_pct"], exp052["sc_accuracy_pct"], exp053["sc_accuracy_pct"]]
sica_accs = [exp033["sica_accuracy_pct"], exp052["sica_accuracy_pct"], exp053["sica_accuracy_pct"]]

cross_seed = {
    "seeds": [exp033, exp052, exp053],
    "mean_sc": round(float(np.mean(sc_accs)), 2),
    "std_sc": round(float(np.std(sc_accs, ddof=1)), 2),
    "mean_sica": round(float(np.mean(sica_accs)), 2),
    "std_sica": round(float(np.std(sica_accs, ddof=1)), 2),
    "mean_delta": round(float(np.mean(deltas)), 2),
    "std_delta": round(float(np.std(deltas, ddof=1)), 2)
}

full_result = {
    "exp052": exp052,
    "exp053": exp053,
    "exp033_reference": exp033,
    "cross_seed_summary": cross_seed
}

# Save
out_path = "/root/symb_invariant_consensus/results/seed_replication_analysis.json"
with open(out_path, "w") as f:
    json.dump(full_result, f, indent=2)

# Print results
print("=" * 80)
print("SEED REPLICATION ANALYSIS")
print("=" * 80)

for exp in [exp052, exp053]:
    print(f"\n{'='*60}")
    print(f"{exp['experiment']}")
    print(f"{'='*60}")
    print(f"  n={exp['n']}  SC={exp['sc_accuracy_pct']}% ({exp['sc_correct']}/204)  SICA={exp['sica_accuracy_pct']}% ({exp['sica_correct']}/204)  delta={exp['delta_pct']:+.2f}%")
    print(f"  Contingency: both_correct={exp['both_correct']}  both_wrong={exp['both_wrong']}  b(SICA+SC-)={exp['b_sica_correct_sc_wrong']}  c(SC+SICA-)={exp['c_sc_correct_sica_wrong']}")
    print(f"  McNemar p={exp['mcnemar_p_value']:.4f}  sig={'*' if exp['significant_0.05'] else 'ns'}")
    print(f"\n  Per Answer Type:")
    print(f"  {'Type':<10} {'n':>4} {'SC%':>7} {'SICA%':>7} {'delta':>7}")
    for t in exp["per_answer_type"]:
        print(f"  {t['type']:<10} {t['n']:>4} {t['sc_pct']:>7.2f} {t['sica_pct']:>7.2f} {t['delta']:>+7.2f}")
    print(f"\n  Entropy-Conditioned:")
    print(f"  {'Bin':<20} {'n':>4} {'SC%':>7} {'SICA%':>7} {'delta':>7}")
    for e in exp["entropy_conditioned"]:
        print(f"  {e['bin']:<20} {e['n']:>4} {e['sc_pct']:>7.2f} {e['sica_pct']:>7.2f} {e['delta']:>+7.2f}")

print(f"\n{'='*80}")
print("CROSS-SEED SUMMARY (FOLIO-204, Mistral-7B, K=12, T=0.7)")
print("=" * 80)
print(f"{'Seed':<20} {'n':>4} {'SC%':>7} {'SICA%':>7} {'delta':>7} {'b':>4} {'c':>4} {'p-value':>8} {'sig':>4}")
print("-" * 80)
rows = [
    ("42 (exp-033)", 204, 54.41, 59.31, 4.90, 12, 2, 0.013, "*"),
    ("123 (exp-052)", 204, exp052["sc_accuracy_pct"], exp052["sica_accuracy_pct"], exp052["delta_pct"],
     exp052["b_sica_correct_sc_wrong"], exp052["c_sc_correct_sica_wrong"], exp052["mcnemar_p_value"],
     "*" if exp052["significant_0.05"] else "ns"),
    ("456 (exp-053)", 204, exp053["sc_accuracy_pct"], exp053["sica_accuracy_pct"], exp053["delta_pct"],
     exp053["b_sica_correct_sc_wrong"], exp053["c_sc_correct_sica_wrong"], exp053["mcnemar_p_value"],
     "*" if exp053["significant_0.05"] else "ns"),
]
for r in rows:
    print(f"{r[0]:<20} {r[1]:>4} {r[2]:>7.2f} {r[3]:>7.2f} {r[4]:>+7.2f} {r[5]:>4} {r[6]:>4} {r[7]:>8.4f} {r[8]:>4}")
print("-" * 80)
cs = cross_seed
print(f"{'Mean ± std':<20} {'':>4} {cs['mean_sc']:>5.2f}±{cs['std_sc']:<4.2f} {cs['mean_sica']:>5.2f}±{cs['std_sica']:<4.2f} {cs['mean_delta']:>+5.2f}±{cs['std_delta']:<4.2f}")

# Correlation: SC baseline vs delta
print(f"\n--- SC baseline vs delta correlation ---")
print(f"  SC baselines: {sc_accs}")
print(f"  Deltas:       {deltas}")
corr = float(np.corrcoef(sc_accs, deltas)[0, 1])
print(f"  Pearson r = {corr:.4f}")
print(f"  (negative r supports capability-trap hypothesis: higher SC baseline -> smaller SICA gain)")

print(f"\nSaved to: {out_path}")
