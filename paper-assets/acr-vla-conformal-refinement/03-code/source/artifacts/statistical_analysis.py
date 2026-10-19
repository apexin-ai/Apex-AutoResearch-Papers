#!/usr/bin/env python3
"""
Statistical analysis of ACR-VLA Conformal Refinement experiments.
Compares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.
Also includes Argmin and Adaptive-K baselines.

Primary CRM config for Object: norm02 (ε=0.2), K=10.
"""

import numpy as np
from scipy import stats

def print_separator(char='=', width=80):
    print(char * width)

def print_group_stats(name, values):
    arr = np.array(values)
    print(f"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, "
          f"min={arr.min():.4f}, max={arr.max():.4f}")
    print(f"    values: {[round(v, 4) for v in values]}")

def run_tests(name_a, vals_a, name_b, vals_b):
    a = np.array(vals_a)
    b = np.array(vals_b)

    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)
    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')

    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /
                         (len(a) + len(b) - 2))
    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')

    diff = a.mean() - b.mean()
    diff_pct = diff * 100

    print(f"\n  {name_a} vs {name_b}:")
    print(f"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)")
    print(f"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}")
    print(f"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}")
    print(f"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})")

    return t_pval, u_pval

# ============================================================================
# DATA (from registry, conclusion=success, 2026-05-20)
# Each seed appears once; r2/r3 supersedes earlier runs.
# ============================================================================

# --- LIBERO-Spatial ---
# CRM obs_only norm02 K=10 (seeds 42-48, 51) — D083 corrected
crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35, 0.36]  # s42(mag-obsonly-norm02), s43-r2, s44, s45, s46-r2, s47, s48, s51

# VLA-only Spatial (seeds 42-50)
vla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50

# --- LIBERO-Long ---
# CRM obs_only Long (seeds 42-47, 50)
crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50

# VLA-only Long (seeds 42-52)
vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s50, s51, s52 (seed49 removed: PREPARING/no registry data)

# --- LIBERO-Goal ---
# CRM obs_only Goal (seeds 42-47)
crm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47

# VLA-only Goal (seeds 42-46, 49)
vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49

# --- LIBERO-Object ---
# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48) — D084: n=6 locked, seed42=0.20 appendix only
crm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2

# Supplementary: CRM obs_only norm01 (seeds 42-48)
crm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48

# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)
crm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48

# VLA-only Object (seeds 42-50, using r2 for seed45)
vla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50

# --- Argmin Object ---
# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)
argmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47
argmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45

# --- Random Selection Object (plan_600) ---
random_selection_object = [0.11, 0.09, 0.11, 0.10]  # s42, s43, s44, s45

# --- Adaptive-K Object ---
adaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44
adaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44
adaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44
adaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44


# ============================================================================
# ANALYSIS
# ============================================================================

print_separator()
print("STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments")
print("All success rates are fractions (0.0 to 1.0)")
print("Object benchmark primary CRM config: norm02 (ε=0.2), K=10")
print_separator()

# ============================================================================
# 1. LIBERO-SPATIAL
# ============================================================================
print("\n1. LIBERO-SPATIAL")
print_separator('-')
print_group_stats("CRM obs_only (n=8)", crm_spatial)
print_group_stats("VLA-only (n=9)", vla_spatial)
run_tests("CRM", crm_spatial, "VLA-only", vla_spatial)

# ============================================================================
# 2. LIBERO-LONG
# ============================================================================
print("\n\n2. LIBERO-LONG")
print_separator('-')
print_group_stats("CRM obs_only (n=7)", crm_long)
print_group_stats("VLA-only (n=10)", vla_long)
run_tests("CRM", crm_long, "VLA-only", vla_long)

# ============================================================================
# 3. LIBERO-GOAL
# ============================================================================
print("\n\n3. LIBERO-GOAL")
print_separator('-')
print_group_stats("CRM obs_only (n=6)", crm_goal)
print_group_stats("VLA-only (n=6)", vla_goal)
run_tests("CRM", crm_goal, "VLA-only", vla_goal)

# ============================================================================
# 4. LIBERO-OBJECT (primary: norm02 K=10)
# ============================================================================
print("\n\n4. LIBERO-OBJECT")
print_separator('-')

print("\n  [PRIMARY: CRM norm02 K=10]")
print_group_stats("CRM obs_only norm02 K=10 (n=6)", crm_object)
print_group_stats("VLA-only (n=8)", vla_object)
run_tests("CRM norm02 K=10", crm_object, "VLA-only", vla_object)

print("\n  [Supplementary: CRM norm01]")
print_group_stats("CRM obs_only norm01 (n=6)", crm_object_norm01)
run_tests("CRM norm01", crm_object_norm01, "VLA-only", vla_object)

print("\n  [Supplementary: CRM norm02 K=5]")
print_group_stats("CRM obs_only norm02 K=5 (n=7)", crm_object_k5)
run_tests("CRM norm02 K=5", crm_object_k5, "VLA-only", vla_object)

# ============================================================================
# 5. ARGMIN BASELINES (Object)
# ============================================================================
print("\n\n5. ARGMIN BASELINES (Object)")
print_separator('-')
print_group_stats("Argmin K=10 (n=5)", argmin_object_k10)
print_group_stats("Argmin K=5 (n=4)", argmin_object_k5)
print_group_stats("VLA-only (n=8)", vla_object)
print_group_stats("CRM norm02 K=10 (n=6)", crm_object)

print("\n  Argmin K=10 vs VLA-only:")
run_tests("Argmin K=10", argmin_object_k10, "VLA-only", vla_object)
print("\n  Argmin K=10 vs CRM norm02 K=10:")
run_tests("Argmin K=10", argmin_object_k10, "CRM norm02", crm_object)

# ============================================================================
# 5b. RANDOM SELECTION BASELINE (Object)
# ============================================================================
print("\n\n5b. RANDOM SELECTION BASELINE (Object, plan_600)")
print_separator('-')
print_group_stats("Random Selection K=10 (n=4)", random_selection_object)
print_group_stats("VLA-only (n=8)", vla_object)
print_group_stats("CRM norm02 K=10 (n=6)", crm_object)

print("\n  Random Selection vs VLA-only:")
run_tests("Random Sel", random_selection_object, "VLA-only", vla_object)
print("\n  Random Selection vs CRM norm02 K=10:")
run_tests("Random Sel", random_selection_object, "CRM norm02", crm_object)

# ============================================================================
# 6. ADAPTIVE-K BASELINES (Object)
# ============================================================================
print("\n\n6. ADAPTIVE-K BASELINES (Object)")
print_separator('-')
print_group_stats("Adaptive-K p25 (n=3)", adaptive_k_p25)
print_group_stats("Adaptive-K p50 (n=3)", adaptive_k_p50)
print_group_stats("Adaptive-K p75 (n=3)", adaptive_k_p75)
print_group_stats("Adaptive-K p90 (n=3)", adaptive_k_p90)
all_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90
print_group_stats("Adaptive-K all (n=12)", all_adaptive)
print_group_stats("VLA-only (n=8)", vla_object)
print_group_stats("CRM norm02 K=10 (n=6)", crm_object)

print("\n  Adaptive-K (all) vs VLA-only:")
run_tests("Adaptive-K all", all_adaptive, "VLA-only", vla_object)
print("\n  Adaptive-K (all) vs CRM norm02 K=10:")
run_tests("Adaptive-K all", all_adaptive, "CRM norm02", crm_object)

# ============================================================================
# 7. SUMMARY TABLE
# ============================================================================
print("\n")
print_separator()
print("SUMMARY TABLE")
print_separator()
print(f"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}")
print_separator('-')

def get_vla_baseline(bench):
    if bench == "LIBERO-Spatial": return vla_spatial
    if bench == "LIBERO-Long": return vla_long
    if bench == "LIBERO-Goal": return vla_goal
    if bench == "LIBERO-Object": return vla_object
    return None

def print_summary_row(bench, method, vals, is_vla=False):
    arr = np.array(vals)
    n = len(arr)
    mean = arr.mean()
    std = arr.std(ddof=1)
    baseline = get_vla_baseline(bench)
    if is_vla or baseline is None:
        print(f"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}")
    else:
        bl_arr = np.array(baseline)
        diff = mean - bl_arr.mean()
        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)
        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'
        print(f"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}")

print_summary_row("LIBERO-Spatial", "CRM obs_only", crm_spatial)
print_summary_row("LIBERO-Spatial", "VLA-only", vla_spatial, is_vla=True)
print()
print_summary_row("LIBERO-Long", "CRM obs_only", crm_long)
print_summary_row("LIBERO-Long", "VLA-only", vla_long, is_vla=True)
print()
print_summary_row("LIBERO-Goal", "CRM obs_only", crm_goal)
print_summary_row("LIBERO-Goal", "VLA-only", vla_goal, is_vla=True)
print()
print_summary_row("LIBERO-Object", "CRM norm02 K=10", crm_object)
print_summary_row("LIBERO-Object", "CRM norm01 (supp)", crm_object_norm01)
print_summary_row("LIBERO-Object", "CRM norm02 K=5 (supp)", crm_object_k5)
print_summary_row("LIBERO-Object", "VLA-only", vla_object, is_vla=True)
print_summary_row("LIBERO-Object", "Argmin K=10", argmin_object_k10)
print_summary_row("LIBERO-Object", "Argmin K=5", argmin_object_k5)
print_summary_row("LIBERO-Object", "Random Sel K=10", random_selection_object)
print_summary_row("LIBERO-Object", "Adaptive-K (all)", all_adaptive)

# ============================================================================
# 8. KEY SIGNIFICANCE RESULTS
# ============================================================================
print("\n")
print_separator()
print("KEY SIGNIFICANCE RESULTS")
print_separator()

tests = [
    ("Spatial: CRM vs VLA", crm_spatial, vla_spatial),
    ("Long: CRM vs VLA", crm_long, vla_long),
    ("Goal: CRM vs VLA", crm_goal, vla_goal),
    ("Object(norm02): CRM vs VLA", crm_object, vla_object),
    ("Object(norm01-supp): CRM vs VLA", crm_object_norm01, vla_object),
    ("Object: Argmin-K10 vs VLA", argmin_object_k10, vla_object),
    ("Object: CRM-norm02 vs Argmin-K10", crm_object, argmin_object_k10),
    ("Object: RandomSel vs VLA", random_selection_object, vla_object),
    ("Object: CRM-norm02 vs RandomSel", crm_object, random_selection_object),
    ("Object: Adaptive-K vs VLA", all_adaptive, vla_object),
    ("Object: CRM-norm02 vs Adaptive-K", crm_object, all_adaptive),
]

print(f"\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}")
print('-' * 85)
for name, a, b in tests:
    arr_a, arr_b = np.array(a), np.array(b)
    diff = arr_a.mean() - arr_b.mean()
    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)
    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')
    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /
                         (len(a) + len(b) - 2))
    d = diff / pooled_std if pooled_std > 0 else float('inf')
    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'
    print(f"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}")

# ============================================================================
# 9. VERIFICATION NOTES
# ============================================================================
print("\n")
print_separator()
print("VERIFICATION NOTES")
print_separator()
print("- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).")
print("  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).")
print("  Registry value retained but unverified.")
print("- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).")
print("- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).")
print("- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.")

print("\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant")
print()
print_separator()
print("END OF ANALYSIS")
print_separator()
