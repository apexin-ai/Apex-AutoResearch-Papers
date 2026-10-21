"""Analyze log-probability baseline vs consistency signals.

Computes Spearman rho, Kendall tau, AUROC, and quartile analysis
comparing mean_logprob against soft_jaccard and fleiss_kappa.
"""

import json
import sys
import numpy as np
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')

from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl"
REPORT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/analysis_report.json"


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


def auroc_simple(scores, labels):
    """Compute AUROC without sklearn dependency."""
    scores = np.array(scores, dtype=float)
    labels = np.array(labels, dtype=int)
    if len(set(labels)) < 2:
        return float('nan')
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    n_pos, n_neg = len(pos), len(neg)
    if n_pos == 0 or n_neg == 0:
        return float('nan')
    count = 0.0
    for p in pos:
        count += np.sum(p > neg) + 0.5 * np.sum(p == neg)
    return count / (n_pos * n_neg)


def corr(x, y, method="spearman"):
    x, y = np.array(x, dtype=float), np.array(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return 0.0, 1.0, int(np.sum(mask))
    if method == "spearman":
        r = spearmanr(x, y)
    else:
        r = kendalltau(x, y)
    return float(r.statistic), float(r.pvalue), len(x)


def analyze_subtask(instances, subtask):
    """Full analysis for one subtask. Returns dict of metrics."""
    # Per-instance greedy F1
    greedy_f1s = [per_instance_f1(inst["greedy"], inst["gold"], subtask) for inst in instances]

    # Consistency scores
    consistency = compute_all_consistency_scores(
        instances, subtask=subtask,
    )
    fk = consistency["fleiss_kappa"]
    sj = consistency["soft_jaccard"]

    # Per-instance mean logprob (avg over N=8 samples)
    mean_logprobs = [
        float(np.mean([s["mean_logprob"] for s in inst["samples"]]))
        for inst in instances
    ]

    # Greedy logprob
    greedy_logprobs = [inst["greedy"]["mean_logprob"] for inst in instances]

    # Filter: gold-non-empty only (full set)
    if subtask == "ner":
        valid = [i for i, inst in enumerate(instances) if inst["gold"].get("entities")]
    else:
        valid = [i for i, inst in enumerate(instances) if inst["gold"].get("relations")]

    n_gold_empty = len(instances) - len(valid)
    f1_v = [greedy_f1s[i] for i in valid]
    fk_v = [fk[i] for i in valid]
    sj_v = [sj[i] for i in valid]
    lp_v = [mean_logprobs[i] for i in valid]
    glp_v = [greedy_logprobs[i] for i in valid]

    # Conditional set: exclude greedy_F1=0 instances (knowledge-gap)
    cond_valid = [i for i in valid if greedy_f1s[i] > 0]
    n_all_zero = len(valid) - len(cond_valid)

    f1_c = [greedy_f1s[i] for i in cond_valid]
    fk_c = [fk[i] for i in cond_valid]
    sj_c = [sj[i] for i in cond_valid]
    lp_c = [mean_logprobs[i] for i in cond_valid]
    glp_c = [greedy_logprobs[i] for i in cond_valid]

    # Compute all metrics
    signals = {
        "soft_jaccard": (sj_v, sj_c),
        "fleiss_kappa": (fk_v, fk_c),
        "mean_logprob": (lp_v, lp_c),
        "greedy_logprob": (glp_v, glp_c),
    }

    # Median-split labels for AUROC (fallback to >= when > yields single-class labels)
    median_f1_v = float(np.median(f1_v))
    labels_v = [1 if f > median_f1_v else 0 for f in f1_v]
    if len(set(labels_v)) < 2:
        labels_v = [1 if f >= median_f1_v else 0 for f in f1_v]
    median_f1_c = float(np.median(f1_c))
    labels_c = [1 if f > median_f1_c else 0 for f in f1_c]
    if len(set(labels_c)) < 2:
        labels_c = [1 if f >= median_f1_c else 0 for f in f1_c]

    results = {}
    for name, (vals_full, vals_cond) in signals.items():
        rho_f, p_f, n_f = corr(vals_full, f1_v, "spearman")
        tau_f, ptau_f, _ = corr(vals_full, f1_v, "kendall")
        auroc_f = auroc_simple(vals_full, labels_v)

        rho_c, p_c, n_c = corr(vals_cond, f1_c, "spearman")
        tau_c, ptau_c, _ = corr(vals_cond, f1_c, "kendall")
        auroc_c = auroc_simple(vals_cond, labels_c)

        results[name] = {
            "full": {"rho": rho_f, "p_rho": p_f, "tau": tau_f, "p_tau": ptau_f, "auroc": auroc_f, "n": n_f},
            "cond": {"rho": rho_c, "p_rho": p_c, "tau": tau_c, "p_tau": ptau_c, "auroc": auroc_c, "n": n_c},
        }

    # Quartile analysis on full set
    sorted_idx = np.argsort(lp_v)
    q_size = len(sorted_idx) // 4
    quartiles = []
    for q in range(4):
        start = q * q_size
        end = (q + 1) * q_size if q < 3 else len(sorted_idx)
        qi = sorted_idx[start:end]
        qf1 = [f1_v[i] for i in qi]
        qlp = [lp_v[i] for i in qi]
        quartiles.append({
            "q": q + 1,
            "logprob_range": [float(min(qlp)), float(max(qlp))],
            "mean_f1": float(np.mean(qf1)),
            "n": len(qi),
        })

    return {
        "n_total": len(instances),
        "n_gold_nonempty": len(valid),
        "n_gold_empty": n_gold_empty,
        "n_conditional": len(cond_valid),
        "n_all_zero_filtered": n_all_zero,
        "median_f1_full": median_f1_v,
        "signals": results,
        "quartiles": quartiles,
    }


def print_table(subtask, analysis):
    """Pretty-print the comparison table."""
    print(f"\n{'='*80}")
    print(f"  Confidence Signal Comparison ({subtask.upper()}, Full Set, n={analysis['n_gold_nonempty']})")
    print(f"{'='*80}")
    print(f"  {'Signal':<20} | {'ρ_spearman':>10} | {'p-value':>10} | {'τ_kendall':>10} | {'AUROC':>7}")
    print(f"  {'-'*20}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*7}")

    for name in ["soft_jaccard", "fleiss_kappa", "mean_logprob", "greedy_logprob"]:
        m = analysis["signals"][name]["full"]
        auroc_s = f"{m['auroc']:.4f}" if not np.isnan(m['auroc']) else "N/A"
        print(f"  {name:<20} | {m['rho']:>+10.4f} | {m['p_rho']:>10.2e} | {m['tau']:>+10.4f} | {auroc_s:>7}")

    print(f"\n  Conditional Set (n={analysis['n_conditional']}, filtered {analysis['n_all_zero_filtered']} all-F1=0)")
    print(f"  {'Signal':<20} | {'ρ_spearman':>10} | {'p-value':>10} | {'τ_kendall':>10} | {'AUROC':>7}")
    print(f"  {'-'*20}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*7}")

    for name in ["soft_jaccard", "fleiss_kappa", "mean_logprob", "greedy_logprob"]:
        m = analysis["signals"][name]["cond"]
        auroc_s = f"{m['auroc']:.4f}" if not np.isnan(m['auroc']) else "N/A"
        print(f"  {name:<20} | {m['rho']:>+10.4f} | {m['p_rho']:>10.2e} | {m['tau']:>+10.4f} | {auroc_s:>7}")

    print(f"\n  Quartile Analysis (by mean_logprob, Full Set):")
    for q in analysis["quartiles"]:
        print(f"    Q{q['q']} [logprob {q['logprob_range'][0]:.3f}..{q['logprob_range'][1]:.3f}]: "
              f"mean_F1={q['mean_f1']:.4f} (n={q['n']})")

    sj = analysis["signals"]["soft_jaccard"]["full"]["rho"]
    lp = analysis["signals"]["mean_logprob"]["full"]["rho"]
    winner = "SJ" if sj > lp else "LOGPROB"
    delta = abs(sj - lp)
    print(f"\n  >>> {winner} WINS (ρ_SJ={sj:+.4f} vs ρ_LP={lp:+.4f}, delta={delta:.4f})")


def main():
    print("Loading data ...")
    instances = load_data(DATA_PATH)
    print(f"Loaded {len(instances)} instances")

    report = {}
    for subtask in ["ner", "re"]:
        analysis = analyze_subtask(instances, subtask)
        print_table(subtask, analysis)
        report[subtask] = analysis

    # Save report
    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2, default=lambda x: None if isinstance(x, float) and np.isnan(x) else x)
    print(f"\nReport saved to {REPORT_PATH}")

    # Final verdict
    ner_sj = report["ner"]["signals"]["soft_jaccard"]["full"]["rho"]
    ner_lp = report["ner"]["signals"]["mean_logprob"]["full"]["rho"]
    re_sj = report["re"]["signals"]["soft_jaccard"]["full"]["rho"]
    re_lp = report["re"]["signals"]["mean_logprob"]["full"]["rho"]

    print(f"\n{'='*80}")
    print(f"  FINAL VERDICT")
    print(f"{'='*80}")
    print(f"  NER: SJ ρ={ner_sj:+.4f} vs LogProb ρ={ner_lp:+.4f} → {'SJ wins' if ner_sj > ner_lp else 'LogProb wins'}")
    print(f"  RE:  SJ ρ={re_sj:+.4f} vs LogProb ρ={re_lp:+.4f} → {'SJ wins' if re_sj > re_lp else 'LogProb wins'}")

    if ner_sj > ner_lp:
        print("  => Strong contribution: structural consistency outperforms naive logprob baseline")
    else:
        print("  => Needs reframing: logprob baseline is competitive or better")
    print(f"{'='*80}")


if __name__ == "__main__":
    main()
