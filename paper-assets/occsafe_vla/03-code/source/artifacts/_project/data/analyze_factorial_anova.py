#!/usr/bin/env python3
"""
2x2 Factorial ANOVA analysis for OccSafe VLA experiment.

Factors:
  A: gradient_flow (ON / OFF)
  B: norm_type (BN / LN)
DV: CAR (Collision Avoidance Rate), range [0, 1]

Cells:
  1 = ON+BN (Full OCC BN, mvp_occ)
  2 = ON+LN (Full OCC LN, full_occ_ln)
  3 = OFF+BN (Detach BN, ablation_occ_detach)
  4 = OFF+LN (Detach LN, detach_ln)
  + Vanilla baseline (no OCC head)

Usage:
  python analyze_factorial_anova.py --demo
  python analyze_factorial_anova.py --data-json data.json
  python analyze_factorial_anova.py --cell1 0.746 0.654 --cell2 0.8 --cell3 0.77 --cell4 0.69 --vanilla 0.768
  python analyze_factorial_anova.py --demo --output-json results.json
"""

import argparse
import json
import sys
from itertools import combinations

import numpy as np
from scipy import stats

# ── Cell definitions ──────────────────────────────────────────────────

CELL_INFO = {
    "cell_1": {"name": "Full OCC BN",  "label": "cell_1", "gradient_flow": "ON",  "norm_type": "BN"},
    "cell_2": {"name": "Full OCC LN",  "label": "cell_2", "gradient_flow": "ON",  "norm_type": "LN"},
    "cell_3": {"name": "Detach BN",    "label": "cell_3", "gradient_flow": "OFF", "norm_type": "BN"},
    "cell_4": {"name": "Detach LN",    "label": "cell_4", "gradient_flow": "OFF", "norm_type": "LN"},
}

CELL_DISPLAY = {
    "cell_1": "Full OCC BN (cell_1)",
    "cell_2": "Full OCC LN (cell_2)",
    "cell_3": "Detach BN (cell_3)",
    "cell_4": "Detach LN (cell_4)",
    "vanilla": "Vanilla",
}

DEMO_DATA = {
    "cell_1": [0.746, 0.654, 0.774],
    "cell_2": [],
    "cell_3": [0.774, 0.736, 0.762, 0.768],
    "cell_4": [],
    "vanilla": [0.768],
}

ALL_KEYS = ["cell_1", "cell_2", "cell_3", "cell_4", "vanilla"]
CELL_KEYS = ["cell_1", "cell_2", "cell_3", "cell_4"]


# ── Helpers ───────────────────────────────────────────────────────────

def sig_stars(p):
    """Return significance stars for p-value."""
    if p is None or np.isnan(p):
        return ""
    if p < 0.001:
        return " ***"
    if p < 0.01:
        return " **"
    if p < 0.05:
        return " *"
    return ""


def cohens_d(a, b):
    """Cohen's d with pooled SD. Returns None if either group has n < 2."""
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2:
        return None
    s1, s2 = np.var(a, ddof=1), np.var(b, ddof=1)
    pooled = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    if pooled == 0:
        return 0.0
    return (np.mean(a) - np.mean(b)) / pooled


def mean_diff_ci(a, b, alpha=0.05):
    """Mean difference and Welch 95% CI. Returns (diff, ci_lo, ci_hi)."""
    n1, n2 = len(a), len(b)
    diff = np.mean(a) - np.mean(b)
    if n1 < 2 or n2 < 2:
        return diff, None, None
    s1n = np.var(a, ddof=1) / n1
    s2n = np.var(b, ddof=1) / n2
    se = np.sqrt(s1n + s2n)
    if se == 0:
        return diff, diff, diff
    df = (s1n + s2n) ** 2 / (s1n ** 2 / (n1 - 1) + s2n ** 2 / (n2 - 1))
    t_crit = stats.t.ppf(1 - alpha / 2, df)
    return diff, diff - t_crit * se, diff + t_crit * se


def ols_ss_resid(X, y):
    """Residual sum of squares from OLS fit."""
    beta, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    return float(np.sum((y - X @ beta) ** 2))


def fmt(val, dec=4):
    if val is None:
        return "N/A"
    return f"{val:.{dec}f}"


# ── Core analyses ─────────────────────────────────────────────────────

def descriptive_stats(data):
    """Compute mean, std, n, 95% CI for each group."""
    result = {}
    for key in ALL_KEYS:
        vals = data.get(key, [])
        if not vals:
            result[key] = {"name": CELL_DISPLAY[key], "n": 0,
                           "mean": None, "std": None, "ci_lo": None, "ci_hi": None}
            continue
        arr = np.array(vals, dtype=float)
        n = len(arr)
        mean = float(np.mean(arr))
        if n >= 2:
            sd = float(np.std(arr, ddof=1))
            se = sd / np.sqrt(n)
            tc = stats.t.ppf(0.975, n - 1)
            ci_lo, ci_hi = mean - tc * se, mean + tc * se
        else:
            sd = ci_lo = ci_hi = None
        result[key] = {"name": CELL_DISPLAY[key], "n": n,
                       "mean": mean, "std": sd, "ci_lo": ci_lo, "ci_hi": ci_hi}
    return result


def assumption_checks(data):
    """Shapiro-Wilk per cell (n>=3) and Levene's test across cells (n>=2)."""
    result = {}

    shapiro = {}
    for key in ALL_KEYS:
        vals = data.get(key, [])
        if len(vals) >= 3:
            w, p = stats.shapiro(vals)
            shapiro[key] = {"name": CELL_DISPLAY[key], "W": float(w), "p": float(p)}
    result["shapiro"] = shapiro

    groups = [np.array(data[k], dtype=float) for k in CELL_KEYS
              if data.get(k) and len(data[k]) >= 2]
    if len(groups) >= 2:
        w, p = stats.levene(*groups)
        result["levene"] = {"W": float(w), "p": float(p)}
    else:
        result["levene"] = None

    return result


def _build_anova_arrays(data):
    """Build y, a, b arrays from cell data using effect coding (-1/+1)."""
    y_list, a_list, b_list = [], [], []
    for key in CELL_KEYS:
        vals = data.get(key, [])
        if not vals:
            continue
        info = CELL_INFO[key]
        a_code = 1.0 if info["gradient_flow"] == "ON" else -1.0
        b_code = 1.0 if info["norm_type"] == "BN" else -1.0
        for v in vals:
            y_list.append(v)
            a_list.append(a_code)
            b_list.append(b_code)
    return np.array(y_list), np.array(a_list), np.array(b_list)


def _all_four_cells(data):
    return all(data.get(k) for k in CELL_KEYS)


def factorial_anova_type2(data):
    """2-way ANOVA with Type II SS via nested model comparisons."""
    if not _all_four_cells(data):
        return None

    y, a, b = _build_anova_arrays(data)
    n = len(y)
    if n - 4 <= 0:
        return None

    ab = a * b
    ones = np.ones(n)

    ss_full = ols_ss_resid(np.column_stack([ones, a, b, ab]), y)
    ss_ab   = ols_ss_resid(np.column_stack([ones, a, b]), y)
    ss_a    = ols_ss_resid(np.column_stack([ones, a]), y)
    ss_b    = ols_ss_resid(np.column_stack([ones, b]), y)

    SS_A  = ss_b  - ss_ab    # R(A | B)
    SS_B  = ss_a  - ss_ab    # R(B | A)
    SS_AB = ss_ab - ss_full  # R(AB | A, B)
    SS_resid = ss_full
    SS_total = float(np.sum((y - np.mean(y)) ** 2))

    df_resid = n - 4
    MS_A  = SS_A / 1
    MS_B  = SS_B / 1
    MS_AB = SS_AB / 1
    MS_resid = SS_resid / df_resid

    def f_and_p(ms_eff):
        if MS_resid == 0:
            return float("inf"), 0.0
        f = ms_eff / MS_resid
        return float(f), float(stats.f.sf(f, 1, df_resid))

    F_A, p_A = f_and_p(MS_A)
    F_B, p_B = f_and_p(MS_B)
    F_AB, p_AB = f_and_p(MS_AB)

    return {
        "gradient_flow": {"SS": SS_A, "df": 1, "MS": MS_A,
                          "F": F_A, "p": p_A,
                          "eta2_partial": SS_A / (SS_A + SS_resid)},
        "norm_type":     {"SS": SS_B, "df": 1, "MS": MS_B,
                          "F": F_B, "p": p_B,
                          "eta2_partial": SS_B / (SS_B + SS_resid)},
        "interaction":   {"SS": SS_AB, "df": 1, "MS": MS_AB,
                          "F": F_AB, "p": p_AB,
                          "eta2_partial": SS_AB / (SS_AB + SS_resid)},
        "residual":      {"SS": SS_resid, "df": df_resid, "MS": MS_resid},
        "total":         {"SS": SS_total, "df": n - 1},
        "n": n,
    }


def permutation_anova(data, n_perm=10000, seed=42):
    """Permutation test for each ANOVA effect (permute y, recompute F)."""
    if not _all_four_cells(data):
        return None

    y, a, b = _build_anova_arrays(data)
    n = len(y)
    if n - 4 <= 0:
        return None

    ab = a * b
    ones = np.ones(n)
    X_full = np.column_stack([ones, a, b, ab])
    X_ab   = np.column_stack([ones, a, b])
    X_a    = np.column_stack([ones, a])
    X_b    = np.column_stack([ones, b])

    rng = np.random.RandomState(seed)

    def compute_f(yy):
        sf = ols_ss_resid(X_full, yy)
        ms_r = sf / (n - 4)
        if ms_r == 0:
            return float("inf"), float("inf"), float("inf")
        fa = (ols_ss_resid(X_b, yy) - ols_ss_resid(X_ab, yy)) / ms_r
        fb = (ols_ss_resid(X_a, yy) - ols_ss_resid(X_ab, yy)) / ms_r
        fab = (ols_ss_resid(X_ab, yy) - sf) / ms_r
        return fa, fb, fab

    obs_fa, obs_fb, obs_fab = compute_f(y)
    cnt_a = cnt_b = cnt_ab = 0

    for _ in range(n_perm):
        yp = rng.permutation(y)
        fa, fb, fab = compute_f(yp)
        if fa >= obs_fa:
            cnt_a += 1
        if fb >= obs_fb:
            cnt_b += 1
        if fab >= obs_fab:
            cnt_ab += 1

    denom = n_perm + 1
    return {
        "gradient_flow": {"F_obs": obs_fa, "p_perm": (cnt_a + 1) / denom},
        "norm_type":     {"F_obs": obs_fb, "p_perm": (cnt_b + 1) / denom},
        "interaction":   {"F_obs": obs_fab, "p_perm": (cnt_ab + 1) / denom},
        "n_perm": n_perm,
    }


def simple_effects_analysis(data):
    """Simple effects: gradient_flow at each norm_type level and vice versa."""
    pairs = [
        ("grad_flow_at_BN",  "cell_1", "cell_3", "Full OCC BN", "Detach BN"),
        ("grad_flow_at_LN",  "cell_2", "cell_4", "Full OCC LN", "Detach LN"),
        ("norm_type_at_ON",  "cell_1", "cell_2", "Full OCC BN", "Full OCC LN"),
        ("norm_type_at_OFF", "cell_3", "cell_4", "Detach BN",   "Detach LN"),
    ]
    result = {}
    for label, k1, k2, g1, g2 in pairs:
        v1, v2 = data.get(k1, []), data.get(k2, [])
        if not v1 or not v2:
            continue
        a1, a2 = np.array(v1), np.array(v2)
        if len(a1) >= 2 and len(a2) >= 2:
            t, p = stats.ttest_ind(a1, a2)
            t, p = float(t), float(p)
        else:
            t = p = None
        result[label] = {"groups": (g1, g2), "t": t, "p": p,
                         "d": cohens_d(a1, a2)}
    return result


def pairwise_comparisons(data):
    """All pairwise t-tests with Bonferroni correction + each cell vs Vanilla."""
    groups = {}
    for key in ALL_KEYS:
        vals = data.get(key, [])
        if vals:
            groups[key] = np.array(vals, dtype=float)

    keys = list(groups.keys())
    n_comp = len(list(combinations(keys, 2)))

    all_pairs = []
    for k1, k2 in combinations(keys, 2):
        a, b_arr = groups[k1], groups[k2]
        d = cohens_d(a, b_arr)
        diff, ci_lo, ci_hi = mean_diff_ci(a, b_arr)
        if len(a) >= 2 and len(b_arr) >= 2:
            t, p = stats.ttest_ind(a, b_arr)
            p_bonf = min(float(p) * n_comp, 1.0)
            t, p = float(t), float(p)
        else:
            t = p = p_bonf = None
        all_pairs.append({
            "group_1": CELL_DISPLAY[k1], "group_2": CELL_DISPLAY[k2],
            "key_1": k1, "key_2": k2,
            "mean_diff": diff, "ci_lo": ci_lo, "ci_hi": ci_hi,
            "t": t, "p_raw": p, "p_bonferroni": p_bonf, "cohens_d": d,
        })

    vs_vanilla = []
    if "vanilla" in groups:
        for key in CELL_KEYS:
            if key not in groups:
                continue
            a, b_arr = groups[key], groups["vanilla"]
            d = cohens_d(a, b_arr)
            diff, ci_lo, ci_hi = mean_diff_ci(a, b_arr)
            if len(a) >= 2 and len(b_arr) >= 2:
                t, p = stats.ttest_ind(a, b_arr)
                t, p = float(t), float(p)
            else:
                t = p = None
            vs_vanilla.append({
                "cell": CELL_DISPLAY[key], "key": key,
                "mean_diff": diff, "ci_lo": ci_lo, "ci_hi": ci_hi,
                "t": t, "p": p, "cohens_d": d,
            })

    return {"all_pairs": all_pairs, "vs_vanilla": vs_vanilla}


# ── Main analysis runner ──────────────────────────────────────────────

def run_analysis(data):
    results = {}
    results["descriptive"] = descriptive_stats(data)
    results["assumptions"] = assumption_checks(data)
    results["anova"] = factorial_anova_type2(data)
    results["permutation"] = permutation_anova(data)

    if results["anova"] and results["anova"]["interaction"]["p"] < 0.05:
        results["simple_effects"] = simple_effects_analysis(data)
    else:
        results["simple_effects"] = None

    results["pairwise"] = pairwise_comparisons(data)
    return results


# ── Report printer ────────────────────────────────────────────────────

def print_report(results):
    W = 76
    print("=" * W)
    print("  2x2 Factorial ANOVA Report: OccSafe VLA Experiment")
    print("  Factors: gradient_flow (ON/OFF) x norm_type (BN/LN)")
    print("=" * W)

    # 1. Descriptive
    print("\n1. DESCRIPTIVE STATISTICS")
    print("-" * W)
    print(f"  {'Group':<28} {'n':>3}  {'Mean':>8}  {'SD':>8}  {'95% CI':>22}")
    desc = results["descriptive"]
    for key in ALL_KEYS:
        d = desc[key]
        if d["n"] == 0:
            print(f"  {d['name']:<28} {'0':>3}  {'--':>8}  {'--':>8}  {'(no data)':>22}")
        elif d["n"] == 1:
            print(f"  {d['name']:<28} {d['n']:>3}  {fmt(d['mean']):>8}  {'--':>8}  {'(n=1)':>22}")
        else:
            ci = f"[{fmt(d['ci_lo'])}, {fmt(d['ci_hi'])}]"
            print(f"  {d['name']:<28} {d['n']:>3}  {fmt(d['mean']):>8}  {fmt(d['std']):>8}  {ci:>22}")

    # 2. Assumptions
    print("\n2. ASSUMPTION CHECKS")
    print("-" * W)
    assump = results["assumptions"]
    print("  Shapiro-Wilk normality test (H0: data is normal):")
    if assump["shapiro"]:
        for key, sw in assump["shapiro"].items():
            print(f"    {sw['name']:<28} W = {fmt(sw['W'])}, p = {fmt(sw['p'])}{sig_stars(sw['p'])}")
    else:
        print("    (insufficient data, need n >= 3)")
    print()
    if assump["levene"]:
        lv = assump["levene"]
        print(f"  Levene's test (homogeneity of variance): W = {fmt(lv['W'])}, p = {fmt(lv['p'])}{sig_stars(lv['p'])}")
    else:
        print("  Levene's test: skipped (need >= 2 groups with n >= 2)")

    # 3. ANOVA
    print("\n3. 2-WAY ANOVA (Type II SS)")
    print("-" * W)
    anova = results["anova"]
    if anova is None:
        print("  SKIPPED: requires all 4 cells populated and total N >= 5")
    else:
        hdr = f"  {'Source':<18} {'SS':>10} {'df':>4} {'MS':>10} {'F':>8} {'p':>9} {'eta2_p':>8}"
        print(hdr)
        print(f"  {'─' * 18} {'─' * 10} {'─' * 4} {'─' * 10} {'─' * 8} {'─' * 9} {'─' * 8}")
        for eff in ["gradient_flow", "norm_type", "interaction"]:
            e = anova[eff]
            print(f"  {eff:<18} {fmt(e['SS']):>10} {e['df']:>4} {fmt(e['MS']):>10} "
                  f"{fmt(e['F']):>8} {fmt(e['p']):>9}{sig_stars(e['p'])} {fmt(e['eta2_partial']):>8}")
        r = anova["residual"]
        print(f"  {'Residual':<18} {fmt(r['SS']):>10} {r['df']:>4} {fmt(r['MS']):>10}")
        t = anova["total"]
        print(f"  {'Total':<18} {fmt(t['SS']):>10} {t['df']:>4}")
        print(f"\n  N = {anova['n']}")

        if results["simple_effects"]:
            print("\n  Simple Effects (interaction p < .05):")
            for label, se in results["simple_effects"].items():
                g1, g2 = se["groups"]
                d_str = fmt(se["d"]) if se["d"] is not None else "N/A"
                t_str = fmt(se["t"]) if se["t"] is not None else "N/A"
                p_str = fmt(se["p"]) if se["p"] is not None else "N/A"
                stars = sig_stars(se["p"]) if se["p"] is not None else ""
                print(f"    {label}: {g1} vs {g2}")
                print(f"      t = {t_str}, p = {p_str}{stars}, d = {d_str}")

    # 4. Permutation
    print("\n4. PERMUTATION TEST (n = 10,000)")
    print("-" * W)
    perm = results["permutation"]
    if perm is None:
        print("  SKIPPED: requires all 4 cells populated")
    else:
        print("  (Primary inference for small-sample factorial design)")
        print(f"  {'Effect':<18} {'F_obs':>10} {'p_perm':>10}")
        print(f"  {'─' * 18} {'─' * 10} {'─' * 10}")
        for eff in ["gradient_flow", "norm_type", "interaction"]:
            e = perm[eff]
            print(f"  {eff:<18} {fmt(e['F_obs']):>10} {fmt(e['p_perm']):>10}{sig_stars(e['p_perm'])}")

    # 5. Pairwise
    print("\n5. PAIRWISE COMPARISONS")
    print("-" * W)
    pw = results["pairwise"]

    print("  All pairs (Bonferroni-corrected):")
    hdr = f"  {'Comparison':<48} {'dmean':>7} {'t':>7} {'p_bonf':>8} {'d':>7}"
    print(hdr)
    print(f"  {'─' * 48} {'─' * 7} {'─' * 7} {'─' * 8} {'─' * 7}")
    for pair in pw["all_pairs"]:
        comp = f"{pair['group_1']} vs {pair['group_2']}"
        if len(comp) > 48:
            comp = comp[:45] + "..."
        print(f"  {comp:<48} {fmt(pair['mean_diff']):>7} "
              f"{fmt(pair['t']):>7} "
              f"{fmt(pair['p_bonferroni']):>8}"
              f"{sig_stars(pair['p_bonferroni']) if pair['p_bonferroni'] is not None else ''} "
              f"{fmt(pair['cohens_d']):>7}")

    print()
    print("  Each cell vs Vanilla:")
    if pw["vs_vanilla"]:
        print(f"  {'Cell':<28} {'dmean':>7} {'95% CI of diff':>22} {'t':>7} {'p':>8} {'d':>7}")
        print(f"  {'─' * 28} {'─' * 7} {'─' * 22} {'─' * 7} {'─' * 8} {'─' * 7}")
        for v in pw["vs_vanilla"]:
            if v["ci_lo"] is not None:
                ci = f"[{v['ci_lo']:+.4f}, {v['ci_hi']:+.4f}]"
            else:
                ci = "N/A"
            print(f"  {v['cell']:<28} {fmt(v['mean_diff']):>7} {ci:>22} "
                  f"{fmt(v['t']):>7} {fmt(v['p']):>8}"
                  f"{sig_stars(v['p']) if v['p'] is not None else ''} "
                  f"{fmt(v['cohens_d']):>7}")
    else:
        print("  (no Vanilla data)")

    # 6. Key comparison
    print(f"\n6. KEY COMPARISON: Detach BN vs Vanilla")
    print("-" * W)
    target = None
    for v in pw["vs_vanilla"]:
        if v["key"] == "cell_3":
            target = v
            break
    if target:
        print(f"  Mean difference:  {fmt(target['mean_diff'])}")
        if target["ci_lo"] is not None:
            print(f"  95% CI of diff:   [{target['ci_lo']:+.4f}, {target['ci_hi']:+.4f}]")
        if target["cohens_d"] is not None:
            d_val = abs(target["cohens_d"])
            mag = ("negligible" if d_val < 0.2 else "small" if d_val < 0.5
                   else "medium" if d_val < 0.8 else "large")
            print(f"  Cohen's d:        {target['cohens_d']:.4f} ({mag})")
        if target["t"] is not None:
            print(f"  t = {target['t']:.4f}, p = {target['p']:.4f}{sig_stars(target['p'])}")
        else:
            print("  t-test: N/A (Vanilla n=1, insufficient for parametric test)")
        print("  Interpretation: Detach BN ~ Vanilla => OCC without gradient has no effect")
    else:
        print("  (insufficient data for this comparison)")

    print("\n" + "=" * W)
    print("  * p < .05   ** p < .01   *** p < .001")
    print("  eta2_p = partial eta-squared;  d = Cohen's d")
    print("=" * W)


# ── JSON serialization ────────────────────────────────────────────────

def to_native(obj):
    """Convert numpy types to Python native for JSON."""
    if isinstance(obj, dict):
        return {k: to_native(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_native(v) for v in obj]
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj


# ── CLI ───────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="2x2 Factorial ANOVA for OccSafe VLA")
    p.add_argument("--demo", action="store_true", help="Run with built-in demo data")
    p.add_argument("--data-json", type=str, help="Path to JSON data file")
    p.add_argument("--cell1", nargs="*", type=float, default=None)
    p.add_argument("--cell2", nargs="*", type=float, default=None)
    p.add_argument("--cell3", nargs="*", type=float, default=None)
    p.add_argument("--cell4", nargs="*", type=float, default=None)
    p.add_argument("--vanilla", nargs="*", type=float, default=None)
    p.add_argument("--output-json", type=str, help="Save results to JSON")
    p.add_argument("--n-perm", type=int, default=10000, help="Number of permutations")
    return p.parse_args()


def load_data(args):
    if args.demo:
        return DEMO_DATA.copy()
    if args.data_json:
        with open(args.data_json) as f:
            return json.load(f)
    return {
        "cell_1": args.cell1 or [],
        "cell_2": args.cell2 or [],
        "cell_3": args.cell3 or [],
        "cell_4": args.cell4 or [],
        "vanilla": args.vanilla or [],
    }


def main():
    args = parse_args()
    data = load_data(args)

    if not any(data.get(k) for k in CELL_KEYS):
        print("ERROR: No cell data. Use --demo, --data-json, or --cell1/2/3/4.")
        sys.exit(1)

    results = run_analysis(data)
    print_report(results)

    if args.output_json:
        with open(args.output_json, "w") as f:
            json.dump(to_native(results), f, indent=2)
        print(f"\nResults saved to: {args.output_json}")


if __name__ == "__main__":
    main()
