#!/usr/bin/env python3
"""2×2 Factorial ANOVA: gradient_flow (ON/OFF) × norm_type (BN/LN) on CAR.

Usage:
  python factorial_anova.py                          # Run with current data
  python factorial_anova.py --update-cell 2 --car 0.73 --exp-id full_occ_ln_v2_s1c_r2
  python factorial_anova.py --show-data              # Print data JSON
  python factorial_anova.py --reset                  # Reset to hardcoded defaults
"""

import argparse
import json
import os
import sys
import warnings
from pathlib import Path

import numpy as np
from scipy import stats

warnings.filterwarnings("ignore")

DATA_FILE = Path(__file__).parent / "factorial_data.json"

DEFAULT_DATA = {
    "vanilla": {
        "values": [0.768, 0.748, 0.720],
        "exp_ids": ["vanilla_retrain_s0", "vanilla_v2_s1", "vanilla_v2_s2"],
    },
    "cell1_full_occ_bn": {
        "label": "Full OCC BN (Grad ON + BN)",
        "grad": "ON", "norm": "BN",
        "values": [0.746, 0.654, 0.776],
        "exp_ids": ["full_occ_retrain_s0", "full_occ_bn_v2_s1", "mvp_occ_s3_v2"],
    },
    "cell2_full_occ_ln": {
        "label": "Full OCC LN (Grad ON + LN)",
        "grad": "ON", "norm": "LN",
        "values": [0.740],
        "exp_ids": ["full_occ_ln_s3_v2"],
    },
    "cell3_detach_bn": {
        "label": "Detach BN (Grad OFF + BN)",
        "grad": "OFF", "norm": "BN",
        "values": [0.774, 0.736, 0.762, 0.794],
        "exp_ids": ["detach_bn_v2_s0", "detach_bn_v2_s1", "detach_bn_v2_s2", "ablation_occ_detach_s3_v2"],
    },
    "cell4_detach_ln": {
        "label": "Detach LN (Grad OFF + LN)",
        "grad": "OFF", "norm": "LN",
        "values": [0.802],
        "exp_ids": ["detach_ln_s3"],
    },
}

CELL_KEYS = {
    1: "cell1_full_occ_bn",
    2: "cell2_full_occ_ln",
    3: "cell3_detach_bn",
    4: "cell4_detach_ln",
}


def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return json.loads(json.dumps(DEFAULT_DATA))


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {DATA_FILE}")


def desc_stats(vals):
    a = np.array(vals)
    n = len(a)
    mean = a.mean()
    if n > 1:
        sd = a.std(ddof=1)
        se = stats.sem(a)
        ci = stats.t.interval(0.95, n - 1, loc=mean, scale=se)
    else:
        sd = float("nan")
        ci = (mean, mean)
    return n, mean, sd, ci


def run_anova(data):
    try:
        import pandas as pd
        from statsmodels.formula.api import ols
        from statsmodels.stats.anova import anova_lm
        from statsmodels.stats.multicomp import pairwise_tukeyhsd
    except ImportError:
        print("ERROR: pip install statsmodels pandas")
        sys.exit(1)

    van = np.array(data["vanilla"]["values"])

    # --- Descriptive Statistics ---
    print("=" * 72)
    print("  DESCRIPTIVE STATISTICS")
    print("=" * 72)
    hdr = f"{'Condition':<25} {'n':>3} {'Mean':>7} {'SD':>7} {'95% CI':>20}"
    print(hdr)
    print("-" * 65)

    n, m, sd, ci = desc_stats(van)
    print(f"{'Vanilla (no OCC)':<25} {n:>3} {m:>7.3f} {sd:>7.3f}  [{ci[0]:.3f}, {ci[1]:.3f}]")

    rows = []
    for cid in [1, 2, 3, 4]:
        key = CELL_KEYS[cid]
        cell = data[key]
        vals = cell["values"]
        n, m, sd, ci = desc_stats(vals)
        ci_str = f"[{ci[0]:.3f}, {ci[1]:.3f}]" if n > 1 else "  [n=1, no CI]"
        sd_str = f"{sd:>7.3f}" if n > 1 else "    n/a"
        print(f"Cell {cid} {cell['label']:<19} {n:>3} {m:>7.3f} {sd_str}  {ci_str}")
        for v in vals:
            rows.append({
                "CAR": v,
                "gradient_flow": cell["grad"],
                "norm_type": cell["norm"],
                "cell": f"Cell{cid}",
            })

    df = pd.DataFrame(rows)
    N = len(df)

    # --- Marginal means ---
    print(f"\nMarginal means:")
    for fac, levels in [("gradient_flow", ["ON", "OFF"]), ("norm_type", ["BN", "LN"])]:
        for lv in levels:
            sub = df[df[fac] == lv]["CAR"]
            print(f"  {fac}={lv}: mean={sub.mean():.3f} (n={len(sub)})")

    # --- 2×2 ANOVA ---
    print("\n" + "=" * 72)
    print("  2×2 FACTORIAL ANOVA  (Type III SS, unbalanced)")
    print("=" * 72)

    if N < 6:
        print(f"\n  ⚠ N={N} total observations — low power, interpret with caution.\n")

    model = ols("CAR ~ C(gradient_flow) * C(norm_type)", data=df).fit()
    aov = anova_lm(model, typ=3)

    ss_resid = aov.loc["Residual", "sum_sq"]
    for idx in aov.index:
        if idx not in ("Residual", "Intercept"):
            ss_eff = aov.loc[idx, "sum_sq"]
            aov.loc[idx, "ηp²"] = ss_eff / (ss_eff + ss_resid)

    print(aov.to_string(float_format=lambda x: f"{x:.4f}"))

    print("\nSummary:")
    for idx in aov.index:
        if idx in ("Residual", "Intercept"):
            continue
        p = aov.loc[idx, "PR(>F)"]
        eta = aov.loc[idx, "ηp²"]
        sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "†" if p < 0.1 else "ns"
        sz = "large" if eta > 0.14 else "medium" if eta > 0.06 else "small"
        clean_name = idx.replace("C(", "").replace(")", "").replace(":", " × ")
        print(f"  {clean_name}: F={aov.loc[idx, 'F']:.3f}, p={p:.4f} {sig}, ηp²={eta:.3f} ({sz})")

    # --- Post-hoc ---
    print("\n" + "=" * 72)
    print("  POST-HOC: Tukey HSD across cells")
    print("=" * 72)
    try:
        tukey = pairwise_tukeyhsd(df["CAR"], df["cell"], alpha=0.05)
        print(tukey.summary())
    except Exception as e:
        print(f"  Tukey HSD failed: {e}")
        print("  (Likely too few groups or n=1 cells; add more data and retry)")

    # --- Each cell vs Vanilla ---
    print("\n" + "=" * 72)
    print("  CELL vs VANILLA  (Welch t-test, Bonferroni α=0.0125)")
    print("=" * 72)
    alpha_bonf = 0.05 / 4
    for cid in [1, 2, 3, 4]:
        key = CELL_KEYS[cid]
        cell = data[key]
        vals = np.array(cell["values"])
        if len(vals) < 2:
            diff = vals.mean() - van.mean()
            print(f"  Cell {cid} ({cell['label']}): n=1, no t-test. Δ={diff:+.3f}")
            continue
        t, p = stats.ttest_ind(vals, van, equal_var=False)
        pooled_sd = np.sqrt((vals.std(ddof=1) ** 2 + van.std(ddof=1) ** 2) / 2)
        d = (vals.mean() - van.mean()) / pooled_sd if pooled_sd > 0 else 0
        sig = "*" if p < alpha_bonf else "ns"
        print(f"  Cell {cid} ({cell['label']}): t={t:.3f}, p={p:.4f} {sig}, d={d:+.2f}, Δ={vals.mean() - van.mean():+.3f}")

    # --- Detach (OFF) pooled vs Vanilla ---
    print("\n" + "-" * 72)
    off_vals = np.array(data["cell3_detach_bn"]["values"] + data["cell4_detach_ln"]["values"])
    on_vals = np.array(data["cell1_full_occ_bn"]["values"] + data["cell2_full_occ_ln"]["values"])
    print(f"  Pooled Grad-OFF vs Vanilla: mean={off_vals.mean():.3f} vs {van.mean():.3f}")
    if len(off_vals) >= 2:
        t, p = stats.ttest_ind(off_vals, van, equal_var=False)
        print(f"    t={t:.3f}, p={p:.4f}")
    print(f"  Pooled Grad-ON  vs Vanilla: mean={on_vals.mean():.3f} vs {van.mean():.3f}")
    if len(on_vals) >= 2:
        t, p = stats.ttest_ind(on_vals, van, equal_var=False)
        print(f"    t={t:.3f}, p={p:.4f}")

    # --- LaTeX Table ---
    print("\n" + "=" * 72)
    print("  LaTeX TABLE 1")
    print("=" * 72)
    print(r"""
\begin{table}[t]
\centering
\caption{Constraint Adherence Rate (CAR) across 2$\times$2 factorial conditions.
  Each entry: 50-rollout SafeLIBERO evaluation.}
\label{tab:factorial_car}
\begin{tabular}{llccc}
\toprule
Gradient Flow & Norm & $n$ & CAR (mean $\pm$ sd) & vs.\ Vanilla $p$ \\
\midrule""")

    n_v, m_v, sd_v, _ = desc_stats(van)
    print(f"\\multicolumn{{2}}{{l}}{{Vanilla (no OCC)}} & {n_v} & ${m_v:.3f} \\pm {sd_v:.3f}$ & --- \\\\")
    print(r"\midrule")

    for cid in [1, 2, 3, 4]:
        key = CELL_KEYS[cid]
        cell = data[key]
        vals = np.array(cell["values"])
        n_c, m_c, sd_c, _ = desc_stats(vals)
        sd_str = f"{sd_c:.3f}" if n_c > 1 else "---"
        if n_c >= 2:
            _, p = stats.ttest_ind(vals, van, equal_var=False)
            p_str = f"${p:.3f}$" if p >= 0.001 else "$<$0.001"
        else:
            p_str = "---"
        print(f"{cell['grad']} & {cell['norm']} & {n_c} & ${m_c:.3f} \\pm {sd_str}$ & {p_str} \\\\")

    print(r"""\bottomrule
\end{tabular}
\end{table}""")

    # --- ANOVA summary table for LaTeX ---
    print(r"""
% ANOVA summary (paste into paper if needed)
% Source                          | SS     | df | F     | p     | ηp²
""")
    for idx in aov.index:
        if idx in ("Residual", "Intercept"):
            continue
        clean = idx.replace("C(", "").replace(")", "").replace(":", " × ")
        print(f"% {clean:<35} {aov.loc[idx,'sum_sq']:.4f}  {int(aov.loc[idx,'df']):>2}  {aov.loc[idx,'F']:.3f}  {aov.loc[idx,'PR(>F)']:.4f}  {aov.loc[idx,'ηp²']:.3f}")
    print(f"% {'Residual':<35} {ss_resid:.4f}  {int(aov.loc['Residual','df']):>2}")


def main():
    parser = argparse.ArgumentParser(description="2×2 Factorial ANOVA for OccSafe VLA")
    parser.add_argument("--update-cell", type=int, choices=[1, 2, 3, 4])
    parser.add_argument("--car", type=float)
    parser.add_argument("--exp-id", type=str, default="")
    parser.add_argument("--reset", action="store_true")
    parser.add_argument("--show-data", action="store_true")
    args = parser.parse_args()

    if args.reset:
        save_data(DEFAULT_DATA)
        print("Reset to defaults.")
        return

    data = load_data()

    if args.update_cell is not None and args.car is not None:
        key = CELL_KEYS[args.update_cell]
        data[key]["values"].append(args.car)
        if args.exp_id:
            data[key]["exp_ids"].append(args.exp_id)
        save_data(data)
        cell = data[key]
        print(f"Added CAR={args.car} to Cell {args.update_cell} ({cell['label']})")
        print(f"  Now n={len(cell['values'])}: {cell['values']}")
        print()

    if args.show_data:
        print(json.dumps(data, indent=2))
        return

    run_anova(data)


if __name__ == "__main__":
    main()
