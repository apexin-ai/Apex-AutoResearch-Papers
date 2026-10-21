#!/usr/bin/env python3
"""Two-way ANOVA variance decomposition + convergence rate fitting for DDR mechanistic grounding."""

import os
import sys
import warnings
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

warnings.filterwarnings("ignore")

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "..", "supplement", "data", "features_all_models.csv")
OUT_DIR = BASE

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay", "ttr", "hapax_ratio"]
LOCATION_FEATURES = {"entropy_mean", "ttr", "hapax_ratio"}
SHAPE_FEATURES = {"entropy_max", "entropy_min", "tail_decay"}

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
df = pd.read_csv(DATA_PATH)
df["depth"] = df["depth"].astype(str)
df["generator"] = df["model_name"].astype(str)
print(f"Loaded {len(df)} rows, {df['generator'].nunique()} generators, depths {sorted(df['depth'].unique())}")

# ---------------------------------------------------------------------------
# Analysis A: Two-way ANOVA variance decomposition
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("ANALYSIS A: Two-way ANOVA η² Decomposition (Type II)")
print("=" * 80)

anova_rows = []
for feat in FEATURES:
    sub = df[["depth", "generator", feat]].dropna()
    model = ols(f"{feat} ~ C(depth) * C(generator)", data=sub).fit()
    table = anova_lm(model, typ=2)

    ss_total = table["sum_sq"].sum()
    row = {"feature": feat}
    for source, label in [("C(depth)", "depth"), ("C(generator)", "generator"), ("C(depth):C(generator)", "interaction")]:
        row[f"eta2_{label}"] = table.loc[source, "sum_sq"] / ss_total
    row["eta2_residual"] = table.loc["Residual", "sum_sq"] / ss_total
    row["eta2_sum"] = sum(v for k, v in row.items() if k.startswith("eta2_"))

    for source, label in [("C(depth)", "depth"), ("C(generator)", "generator"), ("C(depth):C(generator)", "interaction")]:
        row[f"F_{label}"] = table.loc[source, "F"]
        row[f"p_{label}"] = table.loc[source, "PR(>F)"]

    anova_rows.append(row)

anova_df = pd.DataFrame(anova_rows)

print(f"\n{'Feature':<16} {'η²(depth)':>11} {'η²(gen)':>11} {'η²(inter)':>11} {'η²(resid)':>11} {'Σ':>7}")
print("-" * 72)
for _, r in anova_df.iterrows():
    print(f"{r['feature']:<16} {r['eta2_depth']:11.4f} {r['eta2_generator']:11.4f} "
          f"{r['eta2_interaction']:11.4f} {r['eta2_residual']:11.4f} {r['eta2_sum']:7.4f}")

print("\nSignificance (p-values):")
print(f"{'Feature':<16} {'p(depth)':>12} {'p(gen)':>12} {'p(inter)':>12}")
print("-" * 56)
for _, r in anova_df.iterrows():
    pd_str = f"{r['p_depth']:.2e}" if r['p_depth'] < 0.001 else f"{r['p_depth']:.4f}"
    pg_str = f"{r['p_generator']:.2e}" if r['p_generator'] < 0.001 else f"{r['p_generator']:.4f}"
    pi_str = f"{r['p_interaction']:.2e}" if r['p_interaction'] < 0.001 else f"{r['p_interaction']:.4f}"
    print(f"{r['feature']:<16} {pd_str:>12} {pg_str:>12} {pi_str:>12}")

anova_out = anova_df[["feature", "eta2_depth", "eta2_generator", "eta2_interaction", "eta2_residual", "eta2_sum"]]
anova_out.to_csv(os.path.join(OUT_DIR, "anova_table.csv"), index=False, float_format="%.6f")

# ---------------------------------------------------------------------------
# Analysis A': LaTeX table
# ---------------------------------------------------------------------------
feat_labels = {
    "entropy_mean": r"$\bar{H}$ (Ent. Mean)",
    "entropy_std": r"$\sigma_H$ (Ent. Std)",
    "entropy_min": r"$H_{\min}$ (Ent. Min)",
    "entropy_max": r"$H_{\max}$ (Ent. Max)",
    "tail_decay": r"$\beta$ (Tail Decay)",
    "ttr": r"TTR",
    "hapax_ratio": r"Hapax Ratio",
}

lines = []
lines.append(r"\begin{table}[t]")
lines.append(r"\centering")
lines.append(r"\caption{Two-way ANOVA variance decomposition ($\eta^2$) for depth $\times$ generator. "
             r"Location features show dominant depth effects; shape features are architecture-invariant.}")
lines.append(r"\label{tab:anova_decomposition}")
lines.append(r"\small")
lines.append(r"\begin{tabular}{l cccc}")
lines.append(r"\toprule")
lines.append(r"Feature & $\eta^2_{\text{depth}}$ & $\eta^2_{\text{gen}}$ & $\eta^2_{\text{inter}}$ & $\eta^2_{\text{resid}}$ \\")
lines.append(r"\midrule")

groups = [
    ("Location", ["entropy_mean", "ttr", "hapax_ratio"]),
    ("Shape", ["entropy_max", "entropy_min", "tail_decay"]),
    ("Intermediate", ["entropy_std"]),
]

for gi, (gname, feats) in enumerate(groups):
    lines.append(rf"\multicolumn{{5}}{{l}}{{\textit{{{gname} features}}}} \\")
    for feat in feats:
        r = anova_df[anova_df["feature"] == feat].iloc[0]
        def fmt_eta(val, is_dominant=False):
            s = f"{val:.3f}"
            if is_dominant and val > 0.1:
                return rf"\textbf{{{s}}}"
            return s

        depth_dom = feat in LOCATION_FEATURES
        lines.append(
            f"  {feat_labels[feat]} & "
            f"{fmt_eta(r['eta2_depth'], depth_dom)} & "
            f"{fmt_eta(r['eta2_generator'], not depth_dom)} & "
            f"{fmt_eta(r['eta2_interaction'])} & "
            f"{fmt_eta(r['eta2_residual'])} \\\\"
        )
    if gi < len(groups) - 1:
        lines.append(r"\addlinespace")

lines.append(r"\bottomrule")
lines.append(r"\end{tabular}")
lines.append(r"\end{table}")

with open(os.path.join(OUT_DIR, "anova_table.tex"), "w") as f:
    f.write("\n".join(lines) + "\n")

# ---------------------------------------------------------------------------
# Analysis B: Per-feature convergence rate fitting
# ---------------------------------------------------------------------------
print("\n" + "=" * 80)
print("ANALYSIS B: Exponential Convergence Rate Fitting  f(d) = a·exp(-λ·d) + c")
print("=" * 80)

def exp_decay(d, a, lam, c):
    return a * np.exp(-lam * d) + c

conv_rows = []
generators = sorted(df["model_name"].unique())

for feat in FEATURES:
    for gen in generators:
        sub = df[df["model_name"] == gen]
        means = sub.groupby("depth")[feat].mean().reset_index()
        means["depth_num"] = means["depth"].astype(float)
        means = means.sort_values("depth_num")

        x = means["depth_num"].values
        y = means[feat].values

        a0 = y[0] - y[-1] if len(y) > 1 else np.std(y)
        c0 = y[-1] if len(y) > 1 else np.mean(y)

        try:
            popt, pcov = curve_fit(exp_decay, x, y, p0=[a0, 0.5, c0], maxfev=10000)
            a_fit, lam_fit, c_fit = popt
            y_pred = exp_decay(x, *popt)
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
        except (RuntimeError, ValueError):
            a_fit, lam_fit, c_fit, r2 = np.nan, np.nan, np.nan, np.nan

        conv_rows.append({
            "feature": feat,
            "generator": gen,
            "a": a_fit,
            "lambda": lam_fit,
            "c": c_fit,
            "R2": r2,
        })

conv_df = pd.DataFrame(conv_rows)
conv_df.to_csv(os.path.join(OUT_DIR, "convergence_rates.csv"), index=False, float_format="%.6f")

print(f"\n{'Feature':<16} {'λ (mean±std)':>20} {'R² (mean)':>10} {'Category':>14}")
print("-" * 65)
for feat in FEATURES:
    sub = conv_df[conv_df["feature"] == feat]
    valid = sub.dropna(subset=["lambda"])
    lam_mean = valid["lambda"].mean()
    lam_std = valid["lambda"].std()
    r2_mean = valid["R2"].mean()
    cat = "Location" if feat in LOCATION_FEATURES else ("Shape" if feat in SHAPE_FEATURES else "Intermediate")
    print(f"{feat:<16} {lam_mean:8.4f} ± {lam_std:<8.4f} {r2_mean:10.4f} {cat:>14}")

print("\n--- Group comparison ---")
for group_name, group_feats in [("Location", LOCATION_FEATURES), ("Shape", SHAPE_FEATURES)]:
    sub = conv_df[conv_df["feature"].isin(group_feats)].dropna(subset=["lambda"])
    print(f"{group_name:>10}: λ = {sub['lambda'].mean():.4f} ± {sub['lambda'].std():.4f}  "
          f"(R² = {sub['R2'].mean():.4f})")

print("\n--- Per-generator λ detail (location features) ---")
print(f"{'Generator':<20}", end="")
for feat in sorted(LOCATION_FEATURES):
    print(f" {feat:>14}", end="")
print()
print("-" * (20 + 15 * len(LOCATION_FEATURES)))
for gen in generators:
    print(f"{gen:<20}", end="")
    for feat in sorted(LOCATION_FEATURES):
        row = conv_df[(conv_df["feature"] == feat) & (conv_df["generator"] == gen)]
        if len(row) and not np.isnan(row.iloc[0]["lambda"]):
            print(f" {row.iloc[0]['lambda']:14.4f}", end="")
        else:
            print(f" {'N/A':>14}", end="")
    print()

print(f"\nFiles saved to {OUT_DIR}/")
print("  anova_table.csv")
print("  anova_table.tex")
print("  convergence_rates.csv")
