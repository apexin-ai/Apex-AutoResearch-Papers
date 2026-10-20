"""
Extract 3-class confusion matrix (gen-0/gen-1/gen-2+) from 6-gen LOGO results.
Aggregates all held-out fold predictions.
"""
import json
import numpy as np

with open("/root/gen-depth-fingerprint/results/multi_classify_results.json") as f:
    data = json.load(f)

logo = data["leave_one_generator_out"]

# Aggregate 5x5 confusion matrices across all 6 held-out generators
agg_cm5 = np.zeros((5, 5), dtype=int)
generators = []
per_gen_cm3 = {}

for gen, metrics in logo.items():
    if gen.startswith("_"):
        continue
    generators.append(gen)
    cm5 = np.array(metrics["confusion_matrix"])
    agg_cm5 += cm5
    
    # Collapse to 3 classes: 0->0, 1->1, 2+3+4->2
    cm3 = np.zeros((3, 3), dtype=int)
    cm3[0, 0] = cm5[0, 0]
    cm3[0, 1] = cm5[0, 1]
    cm3[0, 2] = cm5[0, 2:].sum()
    cm3[1, 0] = cm5[1, 0]
    cm3[1, 1] = cm5[1, 1]
    cm3[1, 2] = cm5[1, 2:].sum()
    cm3[2, 0] = cm5[2:, 0].sum()
    cm3[2, 1] = cm5[2:, 1].sum()
    cm3[2, 2] = cm5[2:, 2:].sum()
    per_gen_cm3[gen] = cm3.tolist()

# Collapse aggregated 5x5 to 3x3
cm3_agg = np.zeros((3, 3), dtype=int)
cm3_agg[0, 0] = agg_cm5[0, 0]
cm3_agg[0, 1] = agg_cm5[0, 1]
cm3_agg[0, 2] = agg_cm5[0, 2:].sum()
cm3_agg[1, 0] = agg_cm5[1, 0]
cm3_agg[1, 1] = agg_cm5[1, 1]
cm3_agg[1, 2] = agg_cm5[1, 2:].sum()
cm3_agg[2, 0] = agg_cm5[2:, 0].sum()
cm3_agg[2, 1] = agg_cm5[2:, 1].sum()
cm3_agg[2, 2] = agg_cm5[2:, 2:].sum()

total = cm3_agg.sum()
cm3_pct = (cm3_agg / cm3_agg.sum(axis=1, keepdims=True) * 100).round(1)

labels = ["gen-0", "gen-1", "gen-2+"]

print("=== Aggregated 3×3 Confusion Matrix (absolute) ===")
print(f"{'':12s} {'Pred gen-0':>12s} {'Pred gen-1':>12s} {'Pred gen-2+':>12s} {'Total':>8s}")
for i in range(3):
    row_total = cm3_agg[i].sum()
    print(f"True {labels[i]:6s} {cm3_agg[i,0]:12d} {cm3_agg[i,1]:12d} {cm3_agg[i,2]:12d} {row_total:8d}")

print("\n=== Aggregated 3×3 Confusion Matrix (row %) ===")
print(f"{'':12s} {'Pred gen-0':>12s} {'Pred gen-1':>12s} {'Pred gen-2+':>12s}")
for i in range(3):
    print(f"True {labels[i]:6s} {cm3_pct[i,0]:11.1f}% {cm3_pct[i,1]:11.1f}% {cm3_pct[i,2]:11.1f}%")

# Gen-1 error analysis
gen1_total = cm3_agg[1].sum()
gen1_correct = cm3_agg[1, 1]
gen1_as_gen0 = cm3_agg[1, 0]
gen1_as_gen2p = cm3_agg[1, 2]

print(f"\n=== Gen-1 Error Analysis ===")
print(f"Total gen-1 samples: {gen1_total}")
print(f"Correctly classified: {gen1_correct} ({gen1_correct/gen1_total*100:.1f}%)")
print(f"Misclassified as gen-0: {gen1_as_gen0} ({gen1_as_gen0/gen1_total*100:.1f}%)")
print(f"Misclassified as gen-2+: {gen1_as_gen2p} ({gen1_as_gen2p/gen1_total*100:.1f}%)")
print(f"Error ratio (gen-0 / gen-2+): {gen1_as_gen0/gen1_as_gen2p:.2f}" if gen1_as_gen2p > 0 else "")

# Save results
results = {
    "confusion_matrix_3class_absolute": cm3_agg.tolist(),
    "confusion_matrix_3class_row_pct": cm3_pct.tolist(),
    "labels": labels,
    "total_samples": int(total),
    "per_generator_3class": {k: v for k, v in per_gen_cm3.items()},
    "gen1_error_analysis": {
        "total": int(gen1_total),
        "correct": int(gen1_correct),
        "correct_pct": round(gen1_correct / gen1_total * 100, 1),
        "misclassified_as_gen0": int(gen1_as_gen0),
        "misclassified_as_gen0_pct": round(gen1_as_gen0 / gen1_total * 100, 1),
        "misclassified_as_gen2p": int(gen1_as_gen2p),
        "misclassified_as_gen2p_pct": round(gen1_as_gen2p / gen1_total * 100, 1),
    },
    "generators": generators,
}

with open("/root/gen-depth-fingerprint/results/confusion_matrix_results.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to /root/gen-depth-fingerprint/results/confusion_matrix_results.json")
