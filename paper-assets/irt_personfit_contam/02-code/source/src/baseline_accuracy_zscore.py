"""Accuracy z-score baseline for contamination detection."""

import json
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "artifacts", "accuracy_zscore_baseline")
os.makedirs(OUT_DIR, exist_ok=True)

MODEL_NAMES = [
    "360GPT2-Pro", "DeepSeek-V3", "Doubao-pro", "Gemini-1.5",
    "Gemma-2B-it", "Hunyuan-Turbo", "Mistral-7B-Instruct-v0.1",
    "Moonshot-v1", "Qwen-Plus", "Qwen2.5-3B-Instruct",
    "Vicuna-7B-v1.3", "Yi-Lightning",
]

BENCHMARK_RANGES = {
    "arc_c":     (0, 295),
    "gsm8k":     (10004, 11323),
    "hellaswag": (11323, 21365),
    "humaneval": (21365, 21529),
    "mmlu":      (27029, 41071),
}

# --- Load data ---
responses = np.loadtxt(
    os.path.join(ROOT, "artifacts", "psn_irt_phase_b", "combine.csv"),
    delimiter=","
)
assert responses.shape == (12, 41871), f"Unexpected shape: {responses.shape}"

lz_df = pd.read_csv(
    os.path.join(ROOT, "artifacts", "phase_b_two_sided_v2", "empirical_pvalues.csv")
)

pf_df = pd.read_csv(
    os.path.join(ROOT, "artifacts", "phase_b_two_sided_v2", "personfit_matrix_v2.csv")
)

# --- Compute per-benchmark accuracy from raw responses ---
rows = []
for bench, (start, end) in BENCHMARK_RANGES.items():
    accs = responses[:, start:end].mean(axis=1)
    mu, sigma = accs.mean(), accs.std(ddof=0)
    for mid in range(12):
        z = (accs[mid] - mu) / sigma if sigma > 0 else 0.0
        rows.append({
            "model": MODEL_NAMES[mid],
            "benchmark": bench,
            "accuracy": accs[mid],
            "z_score": z,
            "z_flagged": abs(z) > 1.96,
        })

df = pd.DataFrame(rows)

# --- Merge lz* results ---
lz_lookup = {}
for _, r in lz_df.iterrows():
    lz_lookup[(r["model_name"], r["benchmark"])] = r["flagged_bh"]

pf_lookup = {}
for _, r in pf_df.iterrows():
    pf_lookup[(r["model_name"], r["benchmark"])] = r["lz_star"]

df["lz_star"] = df.apply(lambda r: pf_lookup.get((r["model"], r["benchmark"]), np.nan), axis=1)
df["lz_flagged"] = df.apply(lambda r: lz_lookup.get((r["model"], r["benchmark"]), False), axis=1)
df["agreement"] = df["z_flagged"] == df["lz_flagged"]

# --- Save zscore_results.csv ---
df.to_csv(os.path.join(OUT_DIR, "zscore_results.csv"), index=False)
print(f"Saved zscore_results.csv ({len(df)} rows)")

# --- Confusion matrix ---
tp = ((df["z_flagged"]) & (df["lz_flagged"])).sum()
fp = ((df["z_flagged"]) & (~df["lz_flagged"])).sum()
fn = ((~df["z_flagged"]) & (df["lz_flagged"])).sum()
tn = ((~df["z_flagged"]) & (~df["lz_flagged"])).sum()

agreement_rate = df["agreement"].mean()
z_count = df["z_flagged"].sum()
lz_count = df["lz_flagged"].sum()

# --- Gemini-1.5 MMLU case study ---
gem = df[(df["model"] == "Gemini-1.5") & (df["benchmark"] == "mmlu")].iloc[0]
gemini_case = {
    "model": "Gemini-1.5",
    "benchmark": "mmlu",
    "accuracy": float(gem["accuracy"]),
    "z_score": float(gem["z_score"]),
    "lz_star": float(gem["lz_star"]),
    "z_flagged": bool(gem["z_flagged"]),
    "lz_flagged": bool(gem["lz_flagged"]),
}

summary = {
    "agreement_rate": float(agreement_rate),
    "z_flagged_count": int(z_count),
    "lz_flagged_count": int(lz_count),
    "total_cells": len(df),
    "confusion_matrix": {"TP": int(tp), "FP": int(fp), "FN": int(fn), "TN": int(tn)},
    "gemini15_mmlu_case": gemini_case,
}

with open(os.path.join(OUT_DIR, "comparison_summary.json"), "w") as f:
    json.dump(summary, f, indent=2)
print(f"Saved comparison_summary.json")

# --- Comparison report ---
report = f"""# Accuracy Z-Score vs. lz* Comparison Report

## Method
- **Accuracy z-score**: For each benchmark, compute per-model accuracy from raw binary responses,
  then z_i = (acc_i - mean) / std across 12 models. Flag if |z| > 1.96.
- **lz* (person-fit)**: Standardized log-likelihood ratio from IRT model, flagged via BH-corrected
  empirical p-values (alpha=0.05).

## Results

| Metric | Value |
|--------|-------|
| Z-score flagged | {z_count}/60 |
| lz* flagged | {lz_count}/60 |
| Agreement rate | {agreement_rate:.3f} |
| TP (both flag) | {tp} |
| FP (z-only flag) | {fp} |
| FN (lz*-only flag) | {fn} |
| TN (neither flag) | {tn} |

## Gemini-1.5 MMLU Case Study

| Metric | Value |
|--------|-------|
| Accuracy | {gemini_case['accuracy']:.6f} |
| Z-score | {gemini_case['z_score']:.3f} |
| lz* | {gemini_case['lz_star']:.3f} |
| Z-flagged | {gemini_case['z_flagged']} |
| lz*-flagged | {gemini_case['lz_flagged']} |

Gemini-1.5 achieves near-perfect MMLU accuracy. The z-score captures that this is an
outlier in terms of overall performance, but it cannot distinguish *how* the model achieved
that score. The lz* statistic ({gemini_case['lz_star']:.1f}) is far more extreme because it
detects that the *pattern* of correct/incorrect responses is aberrant given the model's
estimated ability — the model gets too many hard items right and too few easy items wrong,
a signature consistent with memorization rather than genuine ability.

## What Accuracy Z-Score Captures vs. Misses

**Captures**: Models with unusually high or low overall accuracy on a benchmark relative to
the cohort. Useful as a coarse screening tool.

**Misses**: Item-level response pattern aberrance. Two models with identical accuracy can have
very different lz* values if one shows a natural difficulty gradient while the other shows
flat performance across difficulty levels. With only 12 models, the z-score also suffers
from low statistical power — the threshold |z|>1.96 assumes normality in a sample of 12.

**lz* advantage**: Leverages full item-level response patterns and IRT difficulty parameters.
It detects contamination signatures (memorized hard items, careless easy items) that
aggregate accuracy cannot capture. This is especially important when contamination is
partial — a model might memorize only the hardest items, leaving overall accuracy within
a normal range while producing a highly aberrant response pattern.
"""

with open(os.path.join(OUT_DIR, "comparison_report.md"), "w") as f:
    f.write(report)
print("Saved comparison_report.md")

# --- Scatter plot: z-score vs lz* ---
fig, ax = plt.subplots(figsize=(8, 6))
colors = {"arc_c": "#e41a1c", "gsm8k": "#377eb8", "hellaswag": "#4daf4a",
          "humaneval": "#984ea3", "mmlu": "#ff7f00"}

for bench in BENCHMARK_RANGES:
    sub = df[df["benchmark"] == bench]
    ax.scatter(sub["z_score"], sub["lz_star"], c=colors[bench], label=bench,
               s=60, alpha=0.8, edgecolors="white", linewidth=0.5)

ax.axhline(y=1.96, color="gray", ls="--", lw=0.8, alpha=0.5)
ax.axhline(y=-1.96, color="gray", ls="--", lw=0.8, alpha=0.5)
ax.axvline(x=1.96, color="gray", ls="--", lw=0.8, alpha=0.5)
ax.axvline(x=-1.96, color="gray", ls="--", lw=0.8, alpha=0.5)

ax.set_xlabel("Accuracy Z-Score", fontsize=12)
ax.set_ylabel("lz* Statistic", fontsize=12)
ax.set_title("Accuracy Z-Score vs. lz* Person-Fit Statistic", fontsize=13)
ax.legend(title="Benchmark", fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "zscore_vs_lzstar.png"), dpi=150, bbox_inches="tight")
print("Saved zscore_vs_lzstar.png")

# --- Print summary ---
print(f"\n=== Summary ===")
print(f"Z-score flagged: {z_count}/60")
print(f"lz* flagged:     {lz_count}/60")
print(f"Agreement rate:  {agreement_rate:.3f}")
print(f"Confusion: TP={tp}, FP={fp}, FN={fn}, TN={tn}")
print(f"\nGemini-1.5 MMLU: acc={gemini_case['accuracy']:.6f}, z={gemini_case['z_score']:.3f}, lz*={gemini_case['lz_star']:.3f}")
