#!/usr/bin/env python3
"""
2x2 Factorial ANOVA for OccSafe VLA v2 experiments.
Gradient Flow (Full/Detach) x Norm Type (BN/LN) on CAR metric.

Usage:
  python run_v2_anova.py                    # use built-in data
  python run_v2_anova.py --json data.json   # load from JSON file

JSON format:
{
  "cell1_full_bn": [0.746, 0.654, 0.776],
  "cell2_full_ln": [0.740, ...],
  "cell3_detach_bn": [0.774, 0.736, 0.762, 0.794],
  "cell4_detach_ln": [0.802, ...],
  "vanilla": [0.768]
}
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

try:
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    HAS_STATSMODELS = True
except ImportError:
    HAS_STATSMODELS = False


# ── Default data (update as eval results come in) ──────────────────────

DEFAULT_DATA = {
    "cell1_full_bn": [0.746, 0.654, 0.776],
    "cell2_full_ln": [0.740],
    "cell3_detach_bn": [0.774, 0.736, 0.762, 0.794],
    "cell4_detach_ln": [0.802],
    "vanilla": [0.768, 0.745],
}

CELL_META = {
    "cell1_full_bn": {"gradient_flow": "Full", "norm_type": "BN"},
    "cell2_full_ln": {"gradient_flow": "Full", "norm_type": "LN"},
    "cell3_detach_bn": {"gradient_flow": "Detach", "norm_type": "BN"},
    "cell4_detach_ln": {"gradient_flow": "Detach", "norm_type": "LN"},
}


def load_data(json_path=None):
    if json_path:
        with open(json_path) as f:
            return json.load(f)
    return DEFAULT_DATA.copy()


def build_dataframe(data):
    rows = []
    for cell_key, meta in CELL_META.items():
        if cell_key not in data:
            continue
        for v in data[cell_key]:
            rows.append({
                "gradient_flow": meta["gradient_flow"],
                "norm_type": meta["norm_type"],
                "car": v,
            })
    return pd.DataFrame(rows)


def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    if n1 < 2 and n2 < 2:
        return float('nan')
    m1, m2 = np.mean(g1), np.mean(g2)
    s1 = np.var(g1, ddof=1) if n1 > 1 else 0
    s2 = np.var(g2, ddof=1) if n2 > 1 else 0
    denom = n1 + n2 - 2
    if denom <= 0:
        return float('nan')
    sp = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / denom)
    return (m2 - m1) / sp if sp > 0 else float('nan')


def bootstrap_ci(arr, n_boot=10000, ci=95, seed=42):
    rng = np.random.default_rng(seed)
    boot_means = np.array([
        rng.choice(arr, size=len(arr), replace=True).mean()
        for _ in range(n_boot)
    ])
    lo = (100 - ci) / 2
    hi = 100 - lo
    return np.percentile(boot_means, [lo, hi]), boot_means


def bootstrap_diff_ci(g1, g2, n_boot=10000, ci=95, seed=42):
    rng = np.random.default_rng(seed)
    diffs = []
    for _ in range(n_boot):
        b1 = rng.choice(g1, size=len(g1), replace=True).mean()
        b2 = rng.choice(g2, size=len(g2), replace=True).mean()
        diffs.append(b2 - b1)
    diffs = np.array(diffs)
    lo = (100 - ci) / 2
    hi = 100 - lo
    return np.percentile(diffs, [lo, hi]), diffs


def run_anova(data):
    df = build_dataframe(data)
    vanilla = np.array(data.get("vanilla", []))

    P = print
    P("=" * 72)
    P("2x2 Factorial ANOVA: Gradient Flow (Full/Detach) x Norm Type (BN/LN)")
    P("Dependent variable: CAR (Collision Avoidance Rate)")
    P("=" * 72)

    # ── Cell descriptives ──
    P("\n1. DESCRIPTIVE STATISTICS")
    P("-" * 50)
    cell_arrays = {}
    for cell_key in CELL_META:
        vals = data.get(cell_key, [])
        arr = np.array(vals) if vals else np.array([])
        cell_arrays[cell_key] = arr
        if len(arr) == 0:
            P(f"  {cell_key:20s}: NO DATA")
        elif len(arr) == 1:
            P(f"  {cell_key:20s}: n={len(arr)}, mean={arr.mean():.4f}")
        else:
            P(f"  {cell_key:20s}: n={len(arr)}, mean={arr.mean():.4f}, "
              f"sd={arr.std(ddof=1):.4f}, range=[{arr.min():.3f}, {arr.max():.3f}]")

    if len(vanilla) > 0:
        if len(vanilla) == 1:
            P(f"  {'vanilla':20s}: n={len(vanilla)}, mean={vanilla.mean():.4f}")
        else:
            P(f"  {'vanilla':20s}: n={len(vanilla)}, mean={vanilla.mean():.4f}, "
              f"sd={vanilla.std(ddof=1):.4f}")

    if len(df) < 4:
        P("\n  ** Too few total observations for ANOVA (N < 4). **")
        P("  ** Only descriptives and bootstrap CIs are shown. **")
        _bootstrap_section(cell_arrays, vanilla, P)
        return

    # ── Marginal means ──
    P("\n  Marginal means:")
    margin_grad = df.groupby('gradient_flow')['car'].agg(['mean', 'count'])
    margin_norm = df.groupby('norm_type')['car'].agg(['mean', 'count'])
    for idx, row in margin_grad.iterrows():
        P(f"    {idx:8s}: mean={row['mean']:.4f}  (n={int(row['count'])})")
    for idx, row in margin_norm.iterrows():
        P(f"    {idx:8s}: mean={row['mean']:.4f}  (n={int(row['count'])})")
    P(f"    Grand mean: {df['car'].mean():.4f}  (N={len(df)})")

    # ── Assumption checks ──
    P(f"\n2. ASSUMPTION CHECKS")
    P("-" * 50)

    groups = [arr for arr in cell_arrays.values() if len(arr) >= 2]
    if len(groups) >= 2:
        lev_stat, lev_p = stats.levene(*groups)
        P(f"  Levene's test: F={lev_stat:.4f}, p={lev_p:.4f}  "
          f"{'[OK]' if lev_p >= 0.05 else '[VIOLATED]'}")
    else:
        P("  Levene's test: skipped (need >= 2 groups with n >= 2)")

    for cell_key, arr in cell_arrays.items():
        if len(arr) < 3:
            P(f"  Shapiro-Wilk {cell_key}: n={len(arr)}, too few for normality test")
        else:
            w, sw_p = stats.shapiro(arr)
            P(f"  Shapiro-Wilk {cell_key}: W={w:.4f}, p={sw_p:.4f}  "
              f"{'[OK]' if sw_p >= 0.05 else '[non-normal]'}")

    min_n = min(len(a) for a in cell_arrays.values() if len(a) > 0)
    if min_n < 3:
        P(f"\n  WARNING: Min cell size n={min_n}. Low power, interpret with caution.")

    # ── ANOVA ──
    P(f"\n3. 2x2 ANOVA (Type III SS)")
    P("-" * 50)

    if not HAS_STATSMODELS:
        P("  statsmodels not installed — falling back to scipy F-tests")
        _scipy_fallback_anova(df, cell_arrays, P)
    else:
        _statsmodels_anova(df, cell_arrays, P)

    # ── Pairwise comparisons ──
    P(f"\n4. PAIRWISE COMPARISONS (Cohen's d)")
    P("-" * 50)

    full_all = df[df['gradient_flow'] == 'Full']['car'].values
    detach_all = df[df['gradient_flow'] == 'Detach']['car'].values
    bn_all = df[df['norm_type'] == 'BN']['car'].values
    ln_all = df[df['norm_type'] == 'LN']['car'].values

    d_grad = cohens_d(full_all, detach_all)
    d_norm = cohens_d(bn_all, ln_all)
    P(f"  Detach vs Full (main): d = {d_grad:+.4f}  (positive = Detach > Full)")
    P(f"  LN vs BN (main):      d = {d_norm:+.4f}  (positive = LN > BN)")

    # Simple effects
    P(f"\n  Simple effects:")
    pairs = [
        ("cell1_full_bn", "cell3_detach_bn", "Detach vs Full within BN"),
        ("cell2_full_ln", "cell4_detach_ln", "Detach vs Full within LN"),
        ("cell1_full_bn", "cell2_full_ln", "LN vs BN within Full"),
        ("cell3_detach_bn", "cell4_detach_ln", "LN vs BN within Detach"),
    ]
    for c1, c2, label in pairs:
        a1, a2 = cell_arrays[c1], cell_arrays[c2]
        if len(a1) < 1 or len(a2) < 1:
            P(f"    {label}: insufficient data")
            continue
        d = cohens_d(a1, a2)
        diff = a2.mean() - a1.mean()
        d_str = f"{d:+.4f}" if not np.isnan(d) else "n/a"
        if len(a1) >= 2 and len(a2) >= 2:
            t_stat, t_p = stats.ttest_ind(a1, a2, equal_var=True)
            P(f"    {label}: diff={diff:+.4f}, d={d_str}, t={t_stat:.3f}, p={t_p:.4f}")
        else:
            P(f"    {label}: diff={diff:+.4f}, d={d_str}")

    # ── Bootstrap CIs ──
    _bootstrap_section(cell_arrays, vanilla, P)

    # ── vs Vanilla ──
    P(f"\n6. COMPARISON VS VANILLA")
    P("-" * 50)
    van_mean = vanilla.mean() if len(vanilla) > 0 else float('nan')
    if np.isnan(van_mean):
        P("  No vanilla data provided.")
    else:
        P(f"  Vanilla CAR: {van_mean:.4f} (n={len(vanilla)})")
        for cell_key, arr in cell_arrays.items():
            if len(arr) == 0:
                continue
            diff = arr.mean() - van_mean
            direction = "above" if diff >= 0 else "below"
            pct = abs(diff) / van_mean * 100
            line = f"  {cell_key:20s}: mean={arr.mean():.4f}, diff={diff:+.4f} ({pct:.1f}% {direction})"
            if len(arr) >= 2:
                t_stat, t_p = stats.ttest_1samp(arr, van_mean)
                line += f", t={t_stat:.3f}, p={t_p:.4f}"
            P(line)
        P(f"\n  Grand mean OCC: {df['car'].mean():.4f} vs Vanilla: {van_mean:.4f} "
          f"(diff={df['car'].mean() - van_mean:+.4f})")

    # ── Non-parametric ──
    P(f"\n7. NON-PARAMETRIC CHECK")
    P("-" * 50)
    groups_kw = [arr for arr in cell_arrays.values() if len(arr) >= 1]
    if len(groups_kw) >= 2:
        h_stat, kw_p = stats.kruskal(*groups_kw)
        P(f"  Kruskal-Wallis H={h_stat:.4f}, p={kw_p:.4f}")
    else:
        P("  Not enough groups for Kruskal-Wallis")

    # ── Summary ──
    P(f"\n8. SUMMARY")
    P("-" * 50)
    total_n = len(df)
    cell_ns = {k: len(v) for k, v in cell_arrays.items()}
    P(f"  Total N={total_n}, cell sizes: {cell_ns}")
    P(f"  Grand mean CAR: {df['car'].mean():.4f}")
    if len(vanilla) > 0:
        P(f"  Vanilla CAR: {van_mean:.4f}")

    best_cell = max(cell_arrays.items(), key=lambda x: x[1].mean() if len(x[1]) > 0 else -1)
    P(f"  Best cell: {best_cell[0]} (mean={best_cell[1].mean():.4f})")

    if min_n < 3:
        P(f"\n  CAVEATS:")
        P(f"    - Min cell n={min_n}. Power is low; non-significant p != no effect.")
        P(f"    - Bootstrap CIs for small n have limited resolution.")
        P(f"    - Results are exploratory until all seeds complete.")


def _statsmodels_anova(df, cell_arrays, P):
    model = ols('car ~ C(gradient_flow, Sum) * C(norm_type, Sum)', data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=3)

    ss_resid = anova_table.loc['Residual', 'sum_sq']

    P(f"\n  {'Source':<25s} {'SS':>10s} {'df':>4s} {'F':>10s} {'p':>10s} {'eta2_p':>8s}")
    P(f"  {'-'*67}")

    label_map = {}
    for idx in anova_table.index:
        s = str(idx)
        if ':' in s:
            label_map[idx] = 'Gradient x Norm'
        elif 'gradient' in s.lower():
            label_map[idx] = 'Gradient Flow'
        elif 'norm' in s.lower():
            label_map[idx] = 'Norm Type'
        else:
            label_map[idx] = s

    for idx, row in anova_table.iterrows():
        label = label_map.get(idx, str(idx))
        ss = row.get('sum_sq', np.nan)
        d = row.get('df', np.nan)
        f_val = row.get('F', np.nan)
        p_val = row.get('PR(>F)', np.nan)

        if label in ('Intercept', 'Residual'):
            if pd.notna(f_val):
                P(f"  {label:<25s} {ss:>10.6f} {d:>4.0f} {f_val:>10.4f} {p_val:>10.4f}")
            else:
                P(f"  {label:<25s} {ss:>10.6f} {d:>4.0f}")
            continue

        eta2_p = ss / (ss + ss_resid) if (ss + ss_resid) > 0 else 0
        if pd.notna(f_val):
            P(f"  {label:<25s} {ss:>10.6f} {d:>4.0f} {f_val:>10.4f} {p_val:>10.4f} {eta2_p:>8.4f}")
        else:
            P(f"  {label:<25s} {ss:>10.6f} {d:>4.0f} {'':>10s} {'':>10s} {eta2_p:>8.4f}")

    P(f"\n  Partial eta-squared interpretation: small=0.01, medium=0.06, large=0.14")


def _scipy_fallback_anova(df, cell_arrays, P):
    full = df[df['gradient_flow'] == 'Full']['car'].values
    detach = df[df['gradient_flow'] == 'Detach']['car'].values
    if len(full) >= 2 and len(detach) >= 2:
        f_grad, p_grad = stats.f_oneway(full, detach)
        P(f"  Gradient Flow: F={f_grad:.4f}, p={p_grad:.4f}")

    bn = df[df['norm_type'] == 'BN']['car'].values
    ln = df[df['norm_type'] == 'LN']['car'].values
    if len(bn) >= 2 and len(ln) >= 2:
        f_norm, p_norm = stats.f_oneway(bn, ln)
        P(f"  Norm Type:     F={f_norm:.4f}, p={p_norm:.4f}")

    P("  Interaction: requires statsmodels (pip install statsmodels)")


def _bootstrap_section(cell_arrays, vanilla, P):
    P(f"\n5. BOOTSTRAP 95% CI (10000 resamples)")
    P("-" * 50)
    P(f"  Cell mean CIs:")
    for cell_key, arr in cell_arrays.items():
        if len(arr) == 0:
            continue
        (ci_lo, ci_hi), _ = bootstrap_ci(arr, n_boot=10000)
        P(f"    {cell_key:20s}: mean={arr.mean():.4f}, 95% CI=[{ci_lo:.4f}, {ci_hi:.4f}]")

    if len(vanilla) > 0:
        (ci_lo, ci_hi), _ = bootstrap_ci(vanilla, n_boot=10000)
        P(f"    {'vanilla':20s}: mean={vanilla.mean():.4f}, 95% CI=[{ci_lo:.4f}, {ci_hi:.4f}]")

    # Bootstrap CI for key contrasts
    P(f"\n  Contrast CIs (bootstrap difference of means):")
    contrasts = [
        ("cell3_detach_bn", "cell1_full_bn", "Detach_BN - Full_BN"),
        ("cell4_detach_ln", "cell2_full_ln", "Detach_LN - Full_LN"),
        ("cell2_full_ln", "cell1_full_bn", "Full_LN - Full_BN"),
        ("cell4_detach_ln", "cell3_detach_bn", "Detach_LN - Detach_BN"),
    ]
    for c1, c2, label in contrasts:
        a1, a2 = cell_arrays.get(c1, np.array([])), cell_arrays.get(c2, np.array([]))
        if len(a1) == 0 or len(a2) == 0:
            P(f"    {label:30s}: insufficient data")
            continue
        (ci_lo, ci_hi), diffs = bootstrap_diff_ci(a2, a1, n_boot=10000)
        obs_diff = a1.mean() - a2.mean()
        P(f"    {label:30s}: diff={obs_diff:+.4f}, 95% CI=[{ci_lo:+.4f}, {ci_hi:+.4f}]")

    # Main effect contrasts
    all_full = np.concatenate([cell_arrays.get("cell1_full_bn", []),
                                cell_arrays.get("cell2_full_ln", [])])
    all_detach = np.concatenate([cell_arrays.get("cell3_detach_bn", []),
                                  cell_arrays.get("cell4_detach_ln", [])])
    all_bn = np.concatenate([cell_arrays.get("cell1_full_bn", []),
                              cell_arrays.get("cell3_detach_bn", [])])
    all_ln = np.concatenate([cell_arrays.get("cell2_full_ln", []),
                              cell_arrays.get("cell4_detach_ln", [])])

    if len(all_full) >= 1 and len(all_detach) >= 1:
        (ci_lo, ci_hi), _ = bootstrap_diff_ci(all_full, all_detach, n_boot=10000)
        obs = all_detach.mean() - all_full.mean()
        P(f"    {'Detach - Full (main)':30s}: diff={obs:+.4f}, 95% CI=[{ci_lo:+.4f}, {ci_hi:+.4f}]")

    if len(all_bn) >= 1 and len(all_ln) >= 1:
        (ci_lo, ci_hi), _ = bootstrap_diff_ci(all_bn, all_ln, n_boot=10000)
        obs = all_ln.mean() - all_bn.mean()
        P(f"    {'LN - BN (main)':30s}: diff={obs:+.4f}, 95% CI=[{ci_lo:+.4f}, {ci_hi:+.4f}]")


def main():
    parser = argparse.ArgumentParser(description="2x2 Factorial ANOVA for OccSafe VLA v2")
    parser.add_argument("--json", type=str, default=None,
                        help="Path to JSON file with cell data")
    args = parser.parse_args()

    data = load_data(args.json)

    print(f"Data source: {'JSON: ' + args.json if args.json else 'built-in defaults'}")
    print()
    run_anova(data)


if __name__ == "__main__":
    main()
