#!/usr/bin/env python3
"""Recompute n=29 AUROC after fixing 008e_v3_s2 label from CIVO to non-CIVO (IRD)."""

import numpy as np
import json

# n=29 data from ROC curve analysis, with 008e_v3_s2 FIXED to non-CIVO
experiments = [
    # (exp_id, max_nve, true_label)  1=CIVO, 0=non-CIVO
    ("024b_ch_s1",       0.100, 0),
    ("024b_ch_s0",       0.200, 0),
    ("008a_unexp_s2",    0.333, 0),
    ("008a_unexp_s1",    0.430, 0),
    ("015b_frozen",      0.467, 0),
    ("008a_ch_unexp_s1", 0.478, 0),
    ("008a_ch_unexp_s0", 0.490, 0),
    ("009c_s3",          0.520, 0),
    ("008e_v3_s1",       0.800, 0),
    ("027_tcn_s0_σ02",   0.908, 0),
    ("008e_v3_s4",       0.990, 0),
    ("008f_s3",          1.000, 0),
    ("022b_nocurr",      1.220, 0),
    ("008f_s4",          1.410, 0),
    ("025_obs_sgs_s2",   1.730, 0),  # SGS failure, not CIVO
    ("028_rave_ceil15",  2.230, 0),  # anchor pollution, not CIVO
    ("008e_v3_s2",       3.780, 0),  # FIXED: was CIVO, now non-CIVO (IRD)
    ("008d_s3",          1.530, 1),
    ("027_tcn_s1",       1.637, 1),
    ("018v2_sgs_s1",     1.660, 1),
    ("019b",             3.780, 1),
    ("027_tcn_s0",       3.965, 1),
    ("008e_v3_s3",       4.020, 1),
    ("009e_s1",          4.120, 1),
    ("008d_s4",          4.620, 1),
    ("010b_s1",          8.270, 1),
    ("021_sgs_cheetah",  9.940, 1),
    ("016e_sgs_s1",     10.420, 1),
    ("010b_s0",         70.640, 1),
]

ids = [e[0] for e in experiments]
scores = [e[1] for e in experiments]
labels = [e[2] for e in experiments]

n_pos = sum(labels)
n_neg = len(labels) - n_pos
print(f"n={len(labels)}, positive={n_pos}, negative={n_neg}")


def compute_auroc(labs, scs):
    np_ = sum(labs)
    nn_ = len(labs) - np_
    if np_ == 0 or nn_ == 0:
        return float("nan")
    concordant = 0.0
    for i in range(len(labs)):
        if labs[i] == 1:
            for j in range(len(labs)):
                if labs[j] == 0:
                    if scs[i] > scs[j]:
                        concordant += 1.0
                    elif scs[i] == scs[j]:
                        concordant += 0.5
    return concordant / (np_ * nn_)


auroc = compute_auroc(labels, scores)
print(f"\nAUROC (corrected n=29): {auroc:.4f}")
print(f"Concordant pairs: {auroc * n_pos * n_neg:.1f} / {n_pos * n_neg}")

# Bootstrap CI
rng = np.random.RandomState(42)
n_bootstrap = 10000
n = len(labels)
aurocs = []
for _ in range(n_bootstrap):
    idx = rng.choice(n, size=n, replace=True)
    bl = [labels[i] for i in idx]
    bs = [scores[i] for i in idx]
    if sum(bl) == 0 or sum(bl) == len(bl):
        continue
    a = compute_auroc(bl, bs)
    if not np.isnan(a):
        aurocs.append(a)

ci_lo = np.percentile(aurocs, 2.5)
ci_hi = np.percentile(aurocs, 97.5)
print(f"95% Bootstrap CI: [{ci_lo:.3f}, {ci_hi:.3f}] (n_bootstrap={len(aurocs)})")

# Confusion matrix at θ=1.5×
threshold = 1.5
preds = [1 if s >= threshold else 0 for s in scores]
tp = sum(1 for l, p in zip(labels, preds) if l == 1 and p == 1)
tn = sum(1 for l, p in zip(labels, preds) if l == 0 and p == 0)
fp = sum(1 for l, p in zip(labels, preds) if l == 0 and p == 1)
fn = sum(1 for l, p in zip(labels, preds) if l == 1 and p == 0)
acc = (tp + tn) / len(labels)
prec = tp / (tp + fp) if (tp + fp) > 0 else 0
rec = tp / (tp + fn) if (tp + fn) > 0 else 0
f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0

print(f"\n--- Confusion matrix at θ=1.5× ---")
print(f"TP={tp}  FP={fp}")
print(f"FN={fn}  TN={tn}")
print(f"Accuracy: {acc:.4f} ({tp+tn}/{len(labels)})")
print(f"Precision: {prec:.4f}")
print(f"Recall: {rec:.4f}")
print(f"F1: {f1:.4f}")
print(f"TPR: {rec:.2f}, FPR: {fp/n_neg:.2f}")

# Detail FP and FN
print(f"\n--- FP details ---")
for eid, s, l, p in zip(ids, scores, labels, preds):
    if l == 0 and p == 1:
        print(f"  {eid}: NVE={s:.3f}, true=non-CIVO, predicted=CIVO")

print(f"\n--- FN details ---")
for eid, s, l, p in zip(ids, scores, labels, preds):
    if l == 1 and p == 0:
        print(f"  {eid}: NVE={s:.3f}, true=CIVO, predicted=non-CIVO")

# Compare with original
print(f"\n--- Comparison ---")
print(f"Original n=29: AUROC=0.971, CI=[0.904, 1.000], 13P/16N, FP=2 at θ=1.5×")
print(f"Corrected n=29: AUROC={auroc:.3f}, CI=[{ci_lo:.3f}, {ci_hi:.3f}], {n_pos}P/{n_neg}N, FP={fp} at θ=1.5×")
print(f"AUROC change: {auroc - 0.971:+.3f}")

output = {
    "corrected_n29": {
        "n": len(labels),
        "n_positive": n_pos,
        "n_negative": n_neg,
        "auroc": round(auroc, 4),
        "auroc_ci_95": [round(ci_lo, 3), round(ci_hi, 3)],
        "threshold_1_5x": {
            "TP": tp, "FP": fp, "FN": fn, "TN": tn,
            "accuracy": round(acc, 4),
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1": round(f1, 4),
            "TPR": round(rec, 4),
            "FPR": round(fp/n_neg, 4),
        },
        "false_positives": [
            {"exp_id": eid, "nve": s, "mechanism": ""}
            for eid, s, l, p in zip(ids, scores, labels, preds) if l == 0 and p == 1
        ],
    },
    "original_n29": {
        "auroc": 0.971,
        "auroc_ci_95": [0.904, 1.000],
        "n_positive": 13,
        "n_negative": 16,
    },
    "label_fix": {
        "exp_id": "008e_v3_s2",
        "old_label": "CIVO (positive)",
        "new_label": "non-CIVO / IRD (negative)",
        "reason": "D039/D040 mechanism analysis: eval-driven collapse, not value-driven. Entropy increases (exploration), not decreases (CIVO pattern).",
    },
}

with open("/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/auroc_label_fix_result.json", "w") as f:
    json.dump(output, f, indent=2)

print("\nSaved to artifacts/auroc_label_fix_result.json")
