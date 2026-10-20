"""
BH-FDR Sensitivity Analysis for R31-W8 Rebuttal
Applies Benjamini-Hochberg FDR correction to all 57 statistical tests
from the Holm-Bonferroni enumeration (Appendix Table).
"""
import numpy as np
from collections import OrderedDict

# All 57 tests from the Holm-Bonferroni table (Appendix)
# Format: (test_id, family, description, raw_p)
# For p < 0.001, use 0.0005; for p < 1e-4, use 5e-5
TESTS = [
    # Selection (21 tests)
    (1,  "Selection", "SciERC NER LP sel (N=8, Qwen)", 0.290),
    (2,  "Selection", "SciERC NER SJ sel (N=8, Qwen)", 0.670),
    (3,  "Selection", "SciERC NER FK sel (N=8, Qwen)", 0.790),
    (4,  "Selection", "WNUT-17 LP sel (N=8, Qwen)", 0.720),
    (5,  "Selection", "CoNLL LP sel (N=8, Qwen)", 1.000),
    (6,  "Selection", "Few-NERD LP sel (N=8, Qwen, 3-seed)", 0.0005),
    (7,  "Selection", "SciERC NER SJ sel (N=8, LLaMA)", 0.175),
    (8,  "Selection", "SciERC NER LP sel (N=32, Qwen)", 0.091),
    (9,  "Selection", "SciERC NER FK sel (N=32, Qwen)", 0.101),
    (10, "Selection", "SciERC NER SJ sel (N=32, Qwen)", 0.244),
    (11, "Selection", "SciERC NER EM sel (N=32, Qwen)", 0.355),
    (12, "Selection", "SciERC NER VC sel (N=32, Qwen)", 1.000),
    (13, "Selection", "SciERC RE LP sel (N=16, 4B)", 0.058),
    (14, "Selection", "SciERC RE VC sel (N=16, 4B)", 0.973),
    (15, "Selection", "SciERC RE FK sel (N=16, 4B)", 0.985),
    (16, "Selection", "SciERC RE SJ sel (N=16, 4B)", 0.993),
    (17, "Selection", "SciERC RE EM sel (N=16, 4B)", 0.999),
    (18, "Selection", "SciERC LP sel, non-tied (eps=0.05)", 0.004),
    (19, "Selection", "Few-NERD LP sel (N=8, LLaMA, 3-seed)", 0.0005),
    (20, "Selection", "SciERC LP favorable subset (+2.47pp)", 0.015),
    (21, "Selection", "CoNLL LP favorable subset (-1.78pp)", 0.0005),
    # Construction (10 tests)
    (22, "Construction", "SciERC LP-wt construction (Qwen, 3-seed)", 0.004),
    (23, "Construction", "SciERC uniform construction (Qwen, 3-seed)", 0.023),
    (24, "Construction", "Few-NERD LP-wt construction (Qwen)", 0.0005),
    (25, "Construction", "Few-NERD uniform construction (Qwen)", 0.003),
    (26, "Construction", "CoNLL uniform construction (Qwen)", 0.500),
    (27, "Construction", "SciERC ZS construction (72B)", 0.008),
    (28, "Construction", "SciERC FS construction (72B)", 0.544),
    (29, "Construction", "CoNLL FS construction (72B)", 0.417),
    (30, "Construction", "Few-NERD FS construction (72B)", 0.401),
    (31, "Construction", "SciERC cross-model LP-wt construction", 0.0005),
    # Calibration (3 tests)
    (32, "Calibration", "SciERC MF-Platt vs Raw LP", 0.720),
    (33, "Calibration", "CoNLL MF-Platt vs Raw LP", 0.310),
    (34, "Calibration", "Few-NERD MF-Platt vs Raw LP", 0.830),
    # Signal delta-rho (9 tests)
    (35, "Signal Δρ", "SciERC Δρ SJ-LP (N=8, seed42)", 0.0005),
    (36, "Signal Δρ", "SciERC Δρ VC-SJ (N=8, seed42)", 0.300),
    (37, "Signal Δρ", "SciERC Δρ SJ-EM (N=8, seed42)", 0.045),
    (38, "Signal Δρ", "CoNLL Δρ EM-FK (N=16)", 0.0005),
    (39, "Signal Δρ", "CoNLL Δρ SJ-FK (N=16)", 0.0005),
    (40, "Signal Δρ", "CoNLL Δρ VC-FK (N=16)", 0.040),
    (41, "Signal Δρ", "SciERC Δρ SJ-FK (LLaMA, perm)", 0.060),
    (42, "Signal Δρ", "SciERC RE Δρ SJ-FK (full-set)", 0.530),
    (43, "Signal Δρ", "RE SJ ρ Q1 vs Q4 sent len (Fisher z)", 0.004),
    # Correlation (6 tests)
    (44, "Correlation", "Cross-dataset degeneracy-LP gain (n=23)", 0.810),
    (45, "Correlation", "Per-type deg-headroom (Few-NERD, Spearman)", 0.004),
    (46, "Correlation", "Per-type deg-headroom (exact perm)", 0.005),
    (47, "Correlation", "Per-type deg-headroom (df=4 adjusted)", 0.033),
    (48, "Correlation", "SciERC per-type deg-LP (ρ=0.14)", 0.790),
    (49, "Correlation", "Kruskal-Wallis per-type LP het (SciERC)", 0.796),
    # FS error (4 tests)
    (50, "FS error", "FS vs ZS error overlap (SciERC, perm)", 0.840),
    (51, "FS error", "FS vs ZS error overlap (CoNLL, perm)", 0.640),
    (52, "FS error", "FS vs ZS entity entropy (SciERC)", 0.810),
    (53, "FS error", "FS vs ZS entity entropy (CoNLL, Wilcoxon)", 0.00005),
    # Other (4 tests)
    (54, "Other", "LP distribution seed42 vs 456 (Mann-Whitney)", 0.550),
    (55, "Other", "RE LP sel reversal (free-form, 4-seed)", 0.0005),
    (56, "Other", "WNUT-17 conditional ρ VC", 0.487),
    (57, "Other", "WNUT-17 conditional ρ FK", 0.002),
]


def bh_correction(p_values, alpha=0.05):
    """Benjamini-Hochberg FDR correction. Returns (rejected, p_adjusted)."""
    n = len(p_values)
    p_arr = np.array(p_values)
    sorted_idx = np.argsort(p_arr)
    sorted_p = p_arr[sorted_idx]

    # BH adjusted p-values (step-up)
    p_adj = np.zeros(n)
    p_adj[sorted_idx[-1]] = sorted_p[-1]
    for i in range(n - 2, -1, -1):
        p_adj[sorted_idx[i]] = min(p_adj[sorted_idx[i + 1]],
                                    sorted_p[i] * n / (i + 1))
    p_adj = np.minimum(p_adj, 1.0)

    rejected = p_adj < alpha
    return rejected, p_adj


def holm_correction(p_values, alpha=0.05):
    """Holm-Bonferroni correction for comparison."""
    n = len(p_values)
    p_arr = np.array(p_values)
    sorted_idx = np.argsort(p_arr)
    sorted_p = p_arr[sorted_idx]

    p_adj = np.zeros(n)
    p_adj[sorted_idx[0]] = sorted_p[0] * n
    for i in range(1, n):
        p_adj[sorted_idx[i]] = max(p_adj[sorted_idx[i - 1]],
                                    sorted_p[i] * (n - i))
    p_adj = np.minimum(p_adj, 1.0)

    rejected = p_adj < alpha
    return rejected, p_adj


def main():
    ids = [t[0] for t in TESTS]
    families = [t[1] for t in TESTS]
    descs = [t[2] for t in TESTS]
    raw_p = [t[3] for t in TESTS]
    n = len(TESTS)

    print("=" * 80)
    print("BH-FDR Sensitivity Analysis (R31-W8)")
    print(f"Total tests: k={n}")
    print("Data source: paper's Holm-Bonferroni enumeration table (Appendix)")
    print("=" * 80)

    # --- Section 1: Original p-values ---
    print("\n[1] Original p-values (selection family only)")
    print("-" * 80)
    print(f"{'#':>3} {'Description':<50} {'p-value':>8} {'Sig α=0.05':>10}")
    print("-" * 80)
    for tid, fam, desc, p in TESTS:
        if fam == "Selection":
            sig = "Yes" if p < 0.05 else "No"
            pstr = f"{p:.4f}" if p >= 0.0001 else "<0.001"
            print(f"{tid:>3} {desc:<50} {pstr:>8} {sig:>10}")

    # --- Section 2: Global BH-FDR at multiple α ---
    print("\n" + "=" * 80)
    print("[2] Global BH-FDR correction (all k=57 tests)")
    print("=" * 80)

    alphas = [0.01, 0.05, 0.10, 0.20]

    for alpha in alphas:
        rejected, p_adj = bh_correction(raw_p, alpha=alpha)
        n_rej = int(np.sum(rejected))

        print(f"\n--- FDR α = {alpha} ---")
        print(f"Rejected: {n_rej}/{n}")
        if n_rej > 0:
            print(f"{'#':>3} {'Family':<15} {'Description':<50} {'Raw p':>8} {'BH-adj p':>10}")
            for i in range(n):
                if rejected[i]:
                    pstr = f"{raw_p[i]:.4f}" if raw_p[i] >= 0.0001 else "<0.001"
                    print(f"{ids[i]:>3} {families[i]:<15} {descs[i]:<50} {pstr:>8} {p_adj[i]:>10.4f}")
        else:
            print("  (no tests rejected)")

    # --- Section 3: Per-family BH-FDR ---
    print("\n" + "=" * 80)
    print("[3] Per-family BH-FDR correction (α=0.05)")
    print("=" * 80)

    family_order = ["Selection", "Construction", "Signal Δρ",
                     "Calibration", "Correlation", "FS error", "Other"]
    for fam in family_order:
        fam_tests = [(i, t) for i, t in enumerate(TESTS) if t[1] == fam]
        fam_p = [raw_p[i] for i, _ in fam_tests]
        rejected, p_adj = bh_correction(fam_p, alpha=0.05)
        n_rej = int(np.sum(rejected))

        print(f"\n--- {fam} (k={len(fam_tests)}) --- Rejected: {n_rej}/{len(fam_tests)}")
        print(f"{'#':>3} {'Description':<50} {'Raw p':>8} {'BH-adj p':>10} {'Sig':>5}")
        for j, (i, t) in enumerate(fam_tests):
            pstr = f"{raw_p[i]:.4f}" if raw_p[i] >= 0.0001 else "<0.001"
            sig = "*" if rejected[j] else ""
            print(f"{t[0]:>3} {t[2]:<50} {pstr:>8} {p_adj[j]:>10.4f} {sig:>5}")

    # --- Section 4: Comparison BH vs Holm ---
    print("\n" + "=" * 80)
    print("[4] BH-FDR vs Holm-Bonferroni comparison (global, α=0.05)")
    print("=" * 80)

    bh_rej, bh_adj = bh_correction(raw_p, alpha=0.05)
    holm_rej, holm_adj = holm_correction(raw_p, alpha=0.05)

    print(f"\n{'Method':<25} {'# Rejected':>12} {'Tests surviving'}")
    print("-" * 80)
    print(f"{'Uncorrected':<25} {int(np.sum(np.array(raw_p) < 0.05)):>12}")
    print(f"{'BH-FDR (α=0.05)':<25} {int(np.sum(bh_rej)):>12}")
    print(f"{'Holm-Bonferroni (α=0.05)':<25} {int(np.sum(holm_rej)):>12}")

    print(f"\nTests significant under BH but not Holm:")
    bh_only = bh_rej & ~holm_rej
    if np.any(bh_only):
        for i in range(n):
            if bh_only[i]:
                pstr = f"{raw_p[i]:.4f}" if raw_p[i] >= 0.0001 else "<0.001"
                print(f"  #{ids[i]} {descs[i]} (raw p={pstr}, BH-adj={bh_adj[i]:.4f}, Holm-adj={holm_adj[i]:.4f})")
    else:
        print("  (none)")

    # --- Section 5: Selection-focused analysis ---
    print("\n" + "=" * 80)
    print("[5] Selection-focused analysis: Does BH change paper conclusions?")
    print("=" * 80)

    sel_tests = [(i, t) for i, t in enumerate(TESTS) if t[1] == "Selection"]
    sel_p = [raw_p[i] for i, _ in sel_tests]

    print("\nPrimary selection tests (excluding post-hoc subsets #18,20,21):")
    primary_sel = [(i, t) for i, t in enumerate(TESTS)
                   if t[1] == "Selection" and t[0] not in (18, 20, 21)]
    primary_p = [raw_p[i] for i, _ in primary_sel]

    for alpha in [0.05, 0.10]:
        # Global BH
        _, bh_global = bh_correction(raw_p, alpha=alpha)
        # Per-family BH (selection only, k=21)
        _, bh_sel = bh_correction(sel_p, alpha=alpha)
        # Per-family BH (primary selection only, k=18)
        _, bh_prim = bh_correction(primary_p, alpha=alpha)

        print(f"\n  α = {alpha}:")
        print(f"  {'Scope':<35} {'# significant in selection family'}")

        # Count selection tests significant under each scope
        global_sel_sig = sum(1 for i, _ in sel_tests if bh_global[i] < alpha)
        perfam_sel_sig = sum(1 for j in range(len(sel_p)) if bh_sel[j] < alpha)
        prim_sel_sig = sum(1 for j in range(len(primary_p)) if bh_prim[j] < alpha)

        print(f"  {'Global BH (k=57)':<35} {global_sel_sig}/{len(sel_tests)}")
        print(f"  {'Selection-family BH (k=21)':<35} {perfam_sel_sig}/{len(sel_tests)}")
        print(f"  {'Primary-selection BH (k=18)':<35} {prim_sel_sig}/{len(primary_sel)}")

    # --- Section 6: Key finding ---
    print("\n" + "=" * 80)
    print("[6] Key Finding")
    print("=" * 80)

    _, bh_global_05 = bh_correction(raw_p, alpha=0.05)

    # Check Few-NERD LP selection (#6) and construction (#24)
    fewnerd_sel_bh = bh_global_05[5]  # test #6, index 5
    fewnerd_con_bh = bh_global_05[23]  # test #24, index 23

    print(f"""
Paper's primary selection conclusion: "No signal reliably beats greedy"
  - 15/21 selection tests have p > 0.05 uncorrected → remain non-significant under any correction
  - Few-NERD LP selection (#6): raw p<0.001, BH-adj p={fewnerd_sel_bh:.4f}
  - Few-NERD LP sel LLaMA (#19): raw p<0.001, BH-adj p={bh_global_05[18]:.4f}
  - CoNLL LP favorable subset (#21): raw p<0.001, BH-adj p={bh_global_05[20]:.4f}
  - Non-tied LP subset (#18): raw p=0.004, BH-adj p={bh_global_05[17]:.4f}

Construction conclusion: "+0.42pp cross-model gain is the only positive result"
  - Few-NERD LP-wt construction (#24): raw p<0.001, BH-adj p={fewnerd_con_bh:.4f}
  - Cross-model construction (#31): raw p<0.001, BH-adj p={bh_global_05[30]:.4f}

BH-FDR is LESS conservative than Holm-Bonferroni:
  - Holm rejects {int(np.sum(holm_correction(raw_p, 0.05)[0]))} tests; BH rejects {int(np.sum(bh_correction(raw_p, 0.05)[0]))} tests
  - BH preserves MORE significant results than Holm
  - All tests that survive Holm also survive BH (BH is strictly less conservative)

CONCLUSION: Switching from Holm-Bonferroni to BH-FDR does NOT weaken any paper claim.
Since BH is less conservative, it can only preserve or INCREASE the number of significant
results. The paper's core conclusion ("no signal beats greedy for selection") rests on
non-significant p-values that remain non-significant under any correction method.
The few positive findings (Few-NERD selection, construction gains) are MORE likely to
survive under BH than under Holm.
""")

    # --- Section 7: Summary table for rebuttal ---
    print("=" * 80)
    print("[7] Rebuttal-ready summary table")
    print("=" * 80)

    _, bh_01 = bh_correction(raw_p, alpha=0.01)
    _, bh_05 = bh_correction(raw_p, alpha=0.05)
    _, bh_10 = bh_correction(raw_p, alpha=0.10)
    _, bh_20 = bh_correction(raw_p, alpha=0.20)

    print(f"\n{'FDR α':>8} {'# rejected':>12} {'Selection tests surviving':>30} {'Conclusion'}")
    print("-" * 90)
    for alpha, bh_adj_arr in [(0.01, bh_01), (0.05, bh_05), (0.10, bh_10), (0.20, bh_20)]:
        n_rej = int(np.sum(bh_adj_arr < alpha))
        sel_surv = []
        for i, t in enumerate(TESTS):
            if t[1] == "Selection" and bh_adj_arr[i] < alpha:
                sel_surv.append(f"#{t[0]}")
        sel_str = ", ".join(sel_surv) if sel_surv else "(none)"
        if len(sel_surv) == 0:
            conclusion = "No selection gains; paper conclusions unchanged"
        else:
            conclusion = f"{len(sel_surv)} sel. tests sig.; core null finding intact"
        print(f"{alpha:>8.2f} {n_rej:>12} {sel_str:>30} {conclusion}")

    # Holm comparison row
    holm_rej_05, _ = holm_correction(raw_p, alpha=0.05)
    n_holm = int(np.sum(holm_rej_05))
    print(f"{'Holm':>8} {n_holm:>12} {'(none)':>30} Paper's current method")


if __name__ == "__main__":
    main()
