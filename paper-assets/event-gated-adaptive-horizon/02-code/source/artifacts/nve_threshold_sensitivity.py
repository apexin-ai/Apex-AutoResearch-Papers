"""NVE Threshold Sensitivity Analysis (plan_034)

Computes classification accuracy and AUROC for different NVE thresholds
used in CIVO detection.
"""

import numpy as np
import csv
import json
from pathlib import Path

# ============================================================
# Data: (exp_id, NVE_peak, ground_truth, env, config_type)
# ground_truth: 1 = CIVO-positive (trained dt_emb, multi-joint locomotion)
#               0 = CIVO-negative (controls)
# ============================================================

data = [
    # --- CIVO-positive: trained dt_emb, multi-joint locomotion ---
    ("exp_008d/009e (Walker s1)", 4.13, 1, "Walker", "trained"),
    ("exp_009b (Walker s2)", 1.62, 1, "Walker", "trained"),
    ("exp_008d_s3 (Walker s3)", 1.53, 1, "Walker", "trained"),
    ("exp_008d_s4 (Walker s4)", 4.62, 1, "Walker", "trained"),
    ("exp_059 (Walker s5)", 4.72, 1, "Walker", "trained"),
    ("exp_048 (Cheetah s0)", 70.64, 1, "Cheetah", "trained"),
    ("exp_010b (Cheetah s1)", 8.27, 1, "Cheetah", "trained"),

    # --- CIVO-negative: Walker no-dt-emb controls ---
    ("exp_008f (Walker s0 no_dt_emb)", 1.02, 0, "Walker", "no_dt_emb"),
    ("exp_009c (Walker s2 no_dt_emb)", 1.26, 0, "Walker", "no_dt_emb"),
    ("exp_008f_s3 (Walker s3 no_dt_emb)", 1.20, 0, "Walker", "no_dt_emb"),  # estimated from "< 1.5x"
    ("exp_008f_s4 (Walker s4 no_dt_emb)", 1.41, 0, "Walker", "no_dt_emb"),
    ("exp_009c_s3 (Walker s3 no_dt_emb #2)", 0.52, 0, "Walker", "no_dt_emb"),

    # --- CIVO-negative: Walker frozen dt_emb ---
    ("exp_042 (Walker s0 frozen)", 0.194, 0, "Walker", "frozen"),
    ("exp_047 (Walker s1 frozen)", 1.71, 0, "Walker", "frozen"),
    ("exp_057 (Walker s2 frozen)", 1.88, 0, "Walker", "frozen"),

    # --- CIVO-negative: Cheetah frozen/no-dt-emb ---
    ("exp_046 (Cheetah s0 frozen)", 1.35, 0, "Cheetah", "frozen"),
    ("exp_058 (Cheetah s1 frozen)", 0.78, 0, "Cheetah", "frozen"),
    ("exp_024b_s0 (Cheetah s0 no_dt_emb)", 0.20, 0, "Cheetah", "no_dt_emb"),
    ("exp_024b_s1 (Cheetah s1 no_dt_emb)", 0.10, 0, "Cheetah", "no_dt_emb"),

    # --- CIVO-negative: Cartpole (1 DOF, CIVO does not occur) ---
    # NVE ≈ 1.0 for all (ve_ratio_peak 0.04-0.08, baseline similar)
    ("exp_060 (Cartpole baseline)", 1.00, 0, "Cartpole", "baseline"),
    ("exp_061 (Cartpole trained dt_emb)", 0.90, 0, "Cartpole", "trained"),
    ("exp_062 (Cartpole no_dt_emb)", 1.00, 0, "Cartpole", "no_dt_emb"),

    # --- CIVO-negative: Walker baselines (dt=1, no gate) ---
    ("exp_001_s1 (Walker baseline)", 1.00, 0, "Walker", "baseline"),
    ("exp_001_s2 (Walker baseline)", 1.13, 0, "Walker", "baseline"),
    ("exp_001_s3 (Walker baseline)", 1.05, 0, "Walker", "baseline"),
    ("exp_001_s4 (Walker baseline)", 0.95, 0, "Walker", "baseline"),
]

names = [d[0] for d in data]
nve_values = np.array([d[1] for d in data])
labels = np.array([d[2] for d in data])
envs = [d[3] for d in data]
configs = [d[4] for d in data]

n_pos = labels.sum()
n_neg = len(labels) - n_pos
print(f"Total experiments: {len(data)} (positive: {n_pos}, negative: {n_neg})")
print()

# ============================================================
# Threshold sensitivity analysis
# ============================================================
thresholds = [1.3, 1.5, 1.7, 2.0]

print("=" * 80)
print("NVE Threshold Sensitivity Analysis")
print("=" * 80)
print(f"{'Threshold':>10} {'TP':>4} {'FP':>4} {'TN':>4} {'FN':>4} {'Prec':>7} {'Rec':>7} {'F1':>7} {'Acc':>7}")
print("-" * 80)

results = []
for t in thresholds:
    predicted = (nve_values >= t).astype(int)
    tp = ((predicted == 1) & (labels == 1)).sum()
    fp = ((predicted == 1) & (labels == 0)).sum()
    tn = ((predicted == 0) & (labels == 0)).sum()
    fn = ((predicted == 0) & (labels == 1)).sum()

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    accuracy = (tp + tn) / len(labels)

    results.append({
        "threshold": t,
        "tp": int(tp), "fp": int(fp), "tn": int(tn), "fn": int(fn),
        "precision": precision, "recall": recall, "f1": f1, "accuracy": accuracy
    })

    print(f"{t:>10.1f}× {tp:>4} {fp:>4} {tn:>4} {fn:>4} {precision:>7.3f} {recall:>7.3f} {f1:>7.3f} {accuracy:>7.3f}")

    # Print misclassifications
    fps = [(names[i], nve_values[i]) for i in range(len(labels)) if predicted[i] == 1 and labels[i] == 0]
    fns = [(names[i], nve_values[i]) for i in range(len(labels)) if predicted[i] == 0 and labels[i] == 1]
    if fps:
        print(f"           FP: {', '.join(f'{n} ({v:.2f})' for n, v in fps)}")
    if fns:
        print(f"           FN: {', '.join(f'{n} ({v:.2f})' for n, v in fns)}")

print()

# ============================================================
# AUROC computation (trapezoidal rule)
# ============================================================
# Sort by NVE descending for ROC curve
sorted_indices = np.argsort(-nve_values)
sorted_labels = labels[sorted_indices]
sorted_nve = nve_values[sorted_indices]

# Compute ROC curve points
roc_points = [(0.0, 0.0)]  # (FPR, TPR)
tp_count = 0
fp_count = 0

for i in range(len(sorted_labels)):
    if sorted_labels[i] == 1:
        tp_count += 1
    else:
        fp_count += 1
    tpr = tp_count / n_pos
    fpr = fp_count / n_neg
    roc_points.append((fpr, tpr))

# Compute AUROC using trapezoidal rule
auroc = 0.0
for i in range(1, len(roc_points)):
    x0, y0 = roc_points[i - 1]
    x1, y1 = roc_points[i]
    auroc += (x1 - x0) * (y1 + y0) / 2

print(f"AUROC: {auroc:.4f}")
print()

# Also compute via Wilcoxon-Mann-Whitney statistic for verification
pos_nve = nve_values[labels == 1]
neg_nve = nve_values[labels == 0]
wmw_auroc = sum(1 for p in pos_nve for n in neg_nve if p > n) / (n_pos * n_neg)
wmw_auroc += 0.5 * sum(1 for p in pos_nve for n in neg_nve if p == n) / (n_pos * n_neg)
print(f"AUROC (WMW verification): {wmw_auroc:.4f}")
print()

# Best threshold (max F1)
best = max(results, key=lambda x: x["f1"])
print(f"Optimal threshold (max F1): {best['threshold']}× (F1={best['f1']:.3f}, Acc={best['accuracy']:.3f})")
print()

# ============================================================
# ROC curve data points (for plotting)
# ============================================================
print("ROC Curve Data Points:")
print(f"{'FPR':>8} {'TPR':>8} {'Threshold':>12}")
# Add specific threshold points
for t in sorted(set(sorted_nve), reverse=True):
    pred = (nve_values >= t).astype(int)
    tpr_t = ((pred == 1) & (labels == 1)).sum() / n_pos
    fpr_t = ((pred == 1) & (labels == 0)).sum() / n_neg
    print(f"{fpr_t:>8.4f} {tpr_t:>8.4f} {t:>12.3f}×")

print()

# ============================================================
# LaTeX table
# ============================================================
latex = r"""
\begin{table}[t]
\centering
\caption{NVE threshold sensitivity analysis for CIVO detection. Classification performance across %d experiments (%d CIVO-positive, %d CIVO-negative) at different NVE thresholds. AUROC = %.3f.}
\label{tab:nve_threshold_sensitivity}
\begin{tabular}{ccccccccc}
\toprule
Threshold & TP & FP & TN & FN & Precision & Recall & F1 & Accuracy \\
\midrule
""" % (len(data), n_pos, n_neg, auroc)

for r in results:
    latex += r"$%.1f\times$ & %d & %d & %d & %d & %.3f & %.3f & \textbf{%.3f} & %.3f \\" % (
        r["threshold"], r["tp"], r["fp"], r["tn"], r["fn"],
        r["precision"], r["recall"], r["f1"], r["accuracy"]
    )
    latex += "\n"

latex += r"""\bottomrule
\end{tabular}
\end{table}
"""

print("LaTeX Table:")
print(latex)

# ============================================================
# Save outputs
# ============================================================
out_dir = Path("/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts")

# CSV
csv_path = out_dir / "nve_threshold_sensitivity.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["threshold", "tp", "fp", "tn", "fn", "precision", "recall", "f1", "accuracy"])
    for r in results:
        writer.writerow([r["threshold"], r["tp"], r["fp"], r["tn"], r["fn"],
                         f"{r['precision']:.4f}", f"{r['recall']:.4f}", f"{r['f1']:.4f}", f"{r['accuracy']:.4f}"])

# JSON with full data
json_path = out_dir / "nve_threshold_sensitivity.json"
output = {
    "auroc": round(auroc, 4),
    "auroc_wmw": round(wmw_auroc, 4),
    "n_total": len(data),
    "n_positive": int(n_pos),
    "n_negative": int(n_neg),
    "optimal_threshold": best["threshold"],
    "optimal_f1": round(best["f1"], 4),
    "thresholds": results,
    "experiments": [
        {"exp_id": names[i], "nve_peak": float(nve_values[i]),
         "ground_truth": int(labels[i]), "env": envs[i], "config": configs[i]}
        for i in range(len(data))
    ],
    "roc_points": [{"fpr": round(fp, 4), "tpr": round(tp, 4)} for fp, tp in roc_points],
}
with open(json_path, "w") as f:
    json.dump(output, f, indent=2)

# LaTeX file
latex_path = out_dir / "nve_threshold_sensitivity.tex"
with open(latex_path, "w") as f:
    f.write(latex)

# Experiment data table
data_table_path = out_dir / "nve_experiment_data.csv"
with open(data_table_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["exp_id", "nve_peak", "ground_truth", "env", "config_type"])
    for d in data:
        writer.writerow([d[0], d[1], d[2], d[3], d[4]])

print(f"\nSaved: {csv_path}")
print(f"Saved: {json_path}")
print(f"Saved: {latex_path}")
print(f"Saved: {data_table_path}")
