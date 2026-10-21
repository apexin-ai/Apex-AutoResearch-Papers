#!/usr/bin/env python3
"""NVE threshold sensitivity analysis for rebuttal (plan_034).
Uses B2 definition: any CIVO detection (transient or sustained).
No external dependencies required."""

import os
import math

# Format: (name, env, nve_peak, civo_positive, mechanism)
DATA = [
    # Walker Walk: complete_results table
    ("001_s1",       "walker", 1.00,   0, "baseline"),
    ("006",          "walker", 4.83,   1, "trained dt_emb, sustained CIVO"),
    ("008d_s1",      "walker", 4.12,   1, "trained dt_emb, full collapse"),
    ("009b_s2",      "walker", 1.62,   1, "trained dt_emb, transient CIVO"),
    ("008d_s3",      "walker", 1.53,   1, "trained dt_emb, late-onset"),
    ("008d_s4",      "walker", 4.62,   1, "trained dt_emb, full collapse"),
    ("059_s5",       "walker", 4.72,   1, "trained dt_emb, self-correcting CIVO"),
    ("008f_s1",      "walker", 0.97,   0, "no dt_emb"),
    ("008f_s4",      "walker", 1.41,   0, "no dt_emb"),
    ("009c_s3",      "walker", 1.04,   0, "no dt_emb"),
    ("008a_s0",      "walker", 0.93,   0, "unexposed emb"),
    ("008a_s1",      "walker", 0.83,   0, "unexposed emb"),
    ("008a_s2",      "walker", 0.89,   0, "unexposed emb"),
    ("015b",         "walker", 1.45,   0, "frozen emb, grad starvation"),
    ("022b",         "walker", 0.63,   0, "frozen+Gumbel"),
    ("042",          "walker", 0.19,   0, "frozen dedicated"),
    ("047",          "walker", 1.71,   0, "frozen s1, transient self-corr (not CIVO)"),
    ("057",          "walker", 1.88,   0, "frozen s2, transient self-corr (not CIVO)"),
    ("018_s1",       "walker", 1.66,   1, "Full-SGS, partial mitig (CIVO+)"),
    ("008e_v3_s1",   "walker", 0.94,   0, "mitigation s1"),
    ("008e_v3_s2",   "walker", 3.78,   0, "IRD, non-CIVO"),
    ("008e_v3_s3",   "walker", 4.02,   1, "CIVO collapse"),
    ("008e_v3_s4",   "walker", 0.99,   0, "mitigation s4"),
    # Cheetah Run: complete_results table
    ("010b",         "cheetah", 8.27,   1, "trained dt_emb, collapsed"),
    ("010b_s0",      "cheetah", 108.52, 1, "trained dt_emb, full collapse"),
    ("021",          "cheetah", 9.94,   1, "SGS cheetah, transient CIVO"),
    ("024b_s0",      "cheetah", 0.20,   0, "no dt_emb"),
    ("024b_s1",      "cheetah", 0.10,   0, "no dt_emb"),
    ("008a_ch_s0",   "cheetah", 1.08,   0, "unexposed emb"),
    ("008a_ch_s1",   "cheetah", 1.29,   0, "unexposed emb"),
    ("046",          "cheetah", 1.35,   0, "frozen, no CIVO"),
    ("058",          "cheetah", 0.78,   0, "frozen, no CIVO"),
]


def clopper_pearson(k, n, alpha=0.05):
    """Exact binomial CI for proportion k/n."""
    if n == 0:
        return 0.0, 1.0
    if k == 0:
        lo = 0.0
    else:
        lo = _beta_ppf(alpha / 2, k, n - k + 1)
    if k == n:
        hi = 1.0
    else:
        hi = _beta_ppf(1 - alpha / 2, k + 1, n - k)
    return lo, hi


def _beta_ppf(p, a, b):
    """Approximate beta inverse CDF using normal approximation."""
    mean = a / (a + b)
    var = (a * b) / ((a + b) ** 2 * (a + b + 1))
    sd = math.sqrt(var)
    from math import erf
    z = _norm_ppf(p)
    return max(0.0, min(1.0, mean + z * sd))


def _norm_ppf(p):
    """Approximate inverse normal CDF (Abramowitz & Stegun)."""
    if p <= 0:
        return -5.0
    if p >= 1:
        return 5.0
    if p < 0.5:
        return -_norm_ppf(1 - p)
    t = math.sqrt(-2 * math.log(1 - p))
    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308
    return t - (c0 + c1 * t + c2 * t * t) / (1 + d1 * t + d2 * t * t + d3 * t * t * t)


def compute_metrics(data, threshold):
    tp = fn = fp = tn = 0
    for name, env, nve, label, mech in data:
        pred = 1 if nve >= threshold else 0
        if label == 1 and pred == 1: tp += 1
        elif label == 1 and pred == 0: fn += 1
        elif label == 0 and pred == 1: fp += 1
        else: tn += 1
    n = tp + tn + fp + fn
    acc = (tp + tn) / n
    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tpr
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
    ci_lo, ci_hi = clopper_pearson(tp + tn, n)
    return {
        "threshold": threshold, "n": n,
        "TP": tp, "FP": fp, "FN": fn, "TN": tn,
        "accuracy": acc, "ci_lo": ci_lo, "ci_hi": ci_hi,
        "TPR": tpr, "FPR": fpr,
        "precision": prec, "recall": rec, "f1": f1,
    }


def compute_auroc(data):
    labels = [d[3] for d in data]
    scores = [d[2] for d in data]
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    concordant = 0.0
    for i in range(len(labels)):
        if labels[i] == 1:
            for j in range(len(labels)):
                if labels[j] == 0:
                    if scores[i] > scores[j]:
                        concordant += 1.0
                    elif scores[i] == scores[j]:
                        concordant += 0.5
    return concordant / (n_pos * n_neg)


def format_table(results, title):
    lines = [f"## {title}\n"]
    n_pos = results[0]['TP'] + results[0]['FN']
    n_neg = results[0]['TN'] + results[0]['FP']
    lines.append(f"n = {results[0]['n']} (n_pos = {n_pos}, n_neg = {n_neg})\n")
    lines.append("| Threshold | TP | FP | FN | TN | Accuracy [95% CI] | TPR | FPR | Precision | F1 |")
    lines.append("|-----------|----|----|----|----|-------------------|-----|-----|-----------|-----|")
    for r in results:
        lines.append(
            f"| {r['threshold']:.1f}x | {r['TP']} | {r['FP']} | {r['FN']} | {r['TN']} | "
            f"{r['accuracy']:.1%} [{r['ci_lo']:.1%}, {r['ci_hi']:.1%}] | "
            f"{r['TPR']:.3f} | {r['FPR']:.3f} | {r['precision']:.3f} | {r['f1']:.3f} |"
        )
    return "\n".join(lines)


def error_details(data, threshold):
    fps = [(name, nve, mech) for name, env, nve, label, mech in data if label == 0 and nve >= threshold]
    fns = [(name, nve, mech) for name, env, nve, label, mech in data if label == 1 and nve < threshold]
    lines = []
    if fps:
        lines.append(f"\n**False positives at {threshold}x:**")
        for name, nve, mech in fps:
            lines.append(f"- {name}: NVE={nve:.2f}x ({mech})")
    if fns:
        lines.append(f"\n**False negatives at {threshold}x:**")
        for name, nve, mech in fns:
            lines.append(f"- {name}: NVE={nve:.2f}x ({mech})")
    return "\n".join(lines)


def main():
    thresholds = [1.3, 1.5, 1.7, 2.0]

    all_data = DATA
    walker_data = [d for d in DATA if d[1] == "walker"]
    cheetah_data = [d for d in DATA if d[1] == "cheetah"]

    all_results = [compute_metrics(all_data, t) for t in thresholds]
    walker_results = [compute_metrics(walker_data, t) for t in thresholds]
    cheetah_results = [compute_metrics(cheetah_data, t) for t in thresholds]

    auroc_all = compute_auroc(all_data)
    auroc_walker = compute_auroc(walker_data)
    auroc_cheetah = compute_auroc(cheetah_data)

    md = ["# NVE Threshold Sensitivity Analysis (B2: Any CIVO Detection)\n"]
    md.append("Generated: 2026-05-24\n")
    md.append("Data source: Appendix Table complete_results (all Walker + Cheetah seeds with NVE values)\n")

    md.append(format_table(all_results, f"All Environments (Walker + Cheetah, n={len(all_data)}, AUROC={auroc_all:.3f})"))
    md.append(error_details(all_data, 1.5))
    md.append("")
    md.append(format_table(walker_results, f"Walker Walk (n={len(walker_data)}, AUROC={auroc_walker:.3f})"))
    md.append(error_details(walker_data, 1.5))
    md.append("")
    md.append(format_table(cheetah_results, f"Cheetah Run (n={len(cheetah_data)}, AUROC={auroc_cheetah:.3f})"))
    md.append(error_details(cheetah_data, 1.5))

    md.append("\n## Per-Experiment Data\n")
    md.append("| Experiment | Env | NVE Peak | CIVO (B2) | Mechanism |")
    md.append("|-----------|-----|----------|-----------|-----------|")
    for name, env, nve, label, mech in sorted(all_data, key=lambda x: -x[2]):
        md.append(f"| {name} | {env} | {nve:.2f}x | {'**+**' if label else '-'} | {mech} |")

    output = "\n".join(md)

    outpath = "/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/nve_threshold_sensitivity.md"
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w") as f:
        f.write(output)

    print(output)
    print(f"\n\nSaved to {outpath}")


if __name__ == "__main__":
    main()
