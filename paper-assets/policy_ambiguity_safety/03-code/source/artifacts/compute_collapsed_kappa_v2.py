#!/usr/bin/env python3
"""Compute collapsed κ for human failure mode annotations.

Reconstructs confusion matrix from appendix statistics:
  - κ = 0.15, exact match = 27.3%, n = 100
  - Ann1: spurious_compliance ≈ 48%
  - Ann2: structural_misparse ≈ 41%
  - Primary disagreement: SC ↔ SM
"""
import json
import numpy as np
from itertools import product as iterproduct

CATS = ["struct_misparse", "gap_filling", "boundary_viol", "partial_compl", "spurious_compl"]

def kappa_from_matrix(cm):
    n = cm.sum()
    if n == 0:
        return 0.0
    p_o = np.trace(cm) / n
    row_sums = cm.sum(axis=1) / n
    col_sums = cm.sum(axis=0) / n
    p_e = (row_sums * col_sums).sum()
    if p_e >= 1.0:
        return 1.0
    return (p_o - p_e) / (1 - p_e)

def collapse_matrix(cm, merge_indices):
    """Merge categories at merge_indices into first index."""
    n_old = cm.shape[0]
    keep = sorted(set(range(n_old)) - set(merge_indices[1:]))
    n_new = len(keep)
    new_cm = np.zeros((n_new, n_new))

    idx_map = {}
    for old_i in range(n_old):
        if old_i in merge_indices:
            idx_map[old_i] = keep.index(merge_indices[0])
        else:
            idx_map[old_i] = keep.index(old_i)

    for i in range(n_old):
        for j in range(n_old):
            new_cm[idx_map[i], idx_map[j]] += cm[i, j]
    return new_cm

def try_matrix(ann1, ann2, diag, sc_sm):
    """Build 5x5 matrix given marginals, diagonal, and SC→SM count."""
    n = 5
    cm = np.zeros((n, n), dtype=int)

    for i in range(n):
        cm[i, i] = diag[i]
    cm[4, 0] = sc_sm

    # Fill remaining cells greedily (row by row)
    for i in range(n):
        row_left = ann1[i] - cm[i, :].sum()
        if row_left < 0:
            return None
        for j in range(n):
            if i == j or cm[i, j] > 0:
                continue
            col_left = ann2[j] - cm[:, j].sum()
            alloc = min(row_left, max(0, col_left))
            cm[i, j] = alloc
            row_left -= alloc
        if row_left != 0:
            return None

    # Verify column sums
    for j in range(n):
        if cm[:, j].sum() != ann2[j]:
            return None

    return cm

def main():
    target_kappa = 0.15
    target_match_pct = 27.3
    n = 100

    # SM=0, GF=1, BV=2, PC=3, SC=4
    # Known: Ann1 SC ≈ 48, Ann2 SM ≈ 41

    best = None
    best_err = float('inf')

    # Search over plausible marginals
    for ann1_sm in range(5, 18):
        for ann1_gf in range(8, 22):
            for ann1_bv in range(5, 20):
                ann1_pc = 100 - ann1_sm - ann1_gf - ann1_bv - 48
                if ann1_pc < 1 or ann1_pc > 20:
                    continue
                ann1 = [ann1_sm, ann1_gf, ann1_bv, ann1_pc, 48]

                for ann2_sc in range(3, 18):
                    for ann2_gf in range(8, 25):
                        for ann2_bv in range(5, 22):
                            ann2_pc = 100 - 41 - ann2_gf - ann2_bv - ann2_sc
                            if ann2_pc < 1 or ann2_pc > 20:
                                continue
                            ann2 = [41, ann2_gf, ann2_bv, ann2_pc, ann2_sc]

                            # Compute p_e
                            p_e = sum(a * b for a, b in zip(ann1, ann2)) / (n * n)

                            # Required p_o
                            req_po = p_e + target_kappa * (1 - p_e)
                            req_diag = round(req_po * n)

                            if abs(req_diag - target_match_pct * n / 100) > 1.5:
                                continue

                            # Quick feasibility
                            max_diag = [min(a, b) for a, b in zip(ann1, ann2)]
                            if req_diag > sum(max_diag):
                                continue

                            # Try a few diagonal distributions
                            for d_sc in range(min(4, max_diag[4] + 1)):
                                rem = req_diag - d_sc
                                for d_sm in range(min(max_diag[0] + 1, rem + 1)):
                                    rem2 = rem - d_sm
                                    for d_gf in range(min(max_diag[1] + 1, rem2 + 1)):
                                        rem3 = rem2 - d_gf
                                        for d_bv in range(min(max_diag[2] + 1, rem3 + 1)):
                                            d_pc = rem3 - d_bv
                                            if d_pc < 0 or d_pc > max_diag[3]:
                                                continue

                                            diag = [d_sm, d_gf, d_bv, d_pc, d_sc]

                                            # SC→SM confusion
                                            max_sc_sm = min(48 - d_sc, 41 - d_sm)
                                            for sc_sm in range(max(15, max_sc_sm - 5), max_sc_sm + 1):
                                                if sc_sm < 0:
                                                    continue
                                                cm = try_matrix(ann1, ann2, diag, sc_sm)
                                                if cm is None:
                                                    continue

                                                k = kappa_from_matrix(cm)
                                                m = np.trace(cm) / n * 100
                                                err = abs(k - target_kappa) + abs(m - target_match_pct) / 100

                                                if err < best_err:
                                                    best_err = err
                                                    best = {
                                                        'cm': cm.copy(),
                                                        'kappa': k,
                                                        'match': m,
                                                        'ann1': ann1[:],
                                                        'ann2': ann2[:]
                                                    }
                                                    if err < 0.005:
                                                        break
                                            if best and best_err < 0.005:
                                                break
                                        if best and best_err < 0.005:
                                            break
                                    if best and best_err < 0.005:
                                        break
                                if best and best_err < 0.005:
                                    break
                            if best and best_err < 0.005:
                                break
                        if best and best_err < 0.005:
                            break
                    if best and best_err < 0.005:
                        break
                if best and best_err < 0.005:
                    break
            if best and best_err < 0.005:
                break
        if best and best_err < 0.005:
            break

    if best is None:
        print("ERROR: Could not find consistent matrix")
        return

    cm = best['cm']

    print("=" * 60)
    print("5-CATEGORY CONFUSION MATRIX (reconstructed)")
    print("=" * 60)
    print(f"\n{'':>14}", end="")
    for c in CATS:
        print(f"{c[:8]:>9}", end="")
    print(f"  {'RowSum':>6}")
    for i, cat in enumerate(CATS):
        print(f"{cat[:13]:>14}", end="")
        for j in range(5):
            print(f"{cm[i,j]:>9}", end="")
        print(f"  {cm[i,:].sum():>6}")
    print(f"{'ColSum':>14}", end="")
    for j in range(5):
        print(f"{cm[:,j].sum():>9}", end="")
    print()

    print(f"\n5-category κ = {best['kappa']:.4f}")
    print(f"5-category exact match = {best['match']:.1f}%")
    print(f"SC→SM confusion count = {cm[4,0]}")

    # 4-category: merge SM(0) + SC(4) → policy_misinterpretation
    cm4 = collapse_matrix(cm.astype(float), [0, 4])
    cats4 = ["policy_misinterp", "gap_filling", "boundary_viol", "partial_compl"]
    k4 = kappa_from_matrix(cm4)
    m4 = np.trace(cm4) / n * 100

    print(f"\n{'=' * 60}")
    print("4-CATEGORY (SM + SC → policy_misinterpretation)")
    print(f"{'=' * 60}")
    print(f"\n{'':>14}", end="")
    for c in cats4:
        print(f"{c[:8]:>9}", end="")
    print(f"  {'RowSum':>6}")
    for i, cat in enumerate(cats4):
        print(f"{cat[:13]:>14}", end="")
        for j in range(len(cats4)):
            print(f"{cm4[i,j]:>9.0f}", end="")
        print(f"  {cm4[i,:].sum():>6.0f}")
    print(f"{'ColSum':>14}", end="")
    for j in range(len(cats4)):
        print(f"{cm4[:,j].sum():>9.0f}", end="")
    print()

    print(f"\n4-category κ = {k4:.4f}")
    print(f"4-category exact match = {m4:.1f}%")

    # 3-category: misinterpretation / gap-filling+partial / boundary
    cm3 = collapse_matrix(cm4, [1, 3])
    cats3 = ["policy_misinterp", "gap+partial", "boundary_viol"]
    k3 = kappa_from_matrix(cm3)
    m3 = np.trace(cm3) / n * 100

    print(f"\n{'=' * 60}")
    print("3-CATEGORY (misinterpretation / gap+partial / boundary)")
    print(f"{'=' * 60}")
    print(f"\n3-category κ = {k3:.4f}")
    print(f"3-category exact match = {m3:.1f}%")

    # Sensitivity: vary SC→SM count
    print(f"\n{'=' * 60}")
    print("SENSITIVITY: collapsed κ vs SC↔SM confusion intensity")
    print(f"{'=' * 60}")
    print(f"\nUsing same marginals, varying SC→SM count:")
    print(f"{'SC→SM':>6}  {'5-κ':>6}  {'4-κ':>6}  {'5-match':>7}  {'4-match':>7}")

    for sc_sm_test in range(10, min(49, 42)):
        cm_t = try_matrix(best['ann1'], best['ann2'],
                         [cm[i,i] for i in range(5)], sc_sm_test)
        if cm_t is None:
            continue
        k5_t = kappa_from_matrix(cm_t)
        cm4_t = collapse_matrix(cm_t.astype(float), [0, 4])
        k4_t = kappa_from_matrix(cm4_t)
        m5_t = np.trace(cm_t) / n * 100
        m4_t = np.trace(cm4_t) / n * 100
        print(f"{sc_sm_test:>6}  {k5_t:>6.3f}  {k4_t:>6.3f}  {m5_t:>6.1f}%  {m4_t:>6.1f}%")

    # Save results
    results = {
        "note": "Confusion matrix reconstructed from appendix statistics",
        "constraints": {
            "target_kappa": 0.15,
            "target_match": "27.3%",
            "ann1_SC": "~48%",
            "ann2_SM": "~41%",
            "primary_disagreement": "SC ↔ SM"
        },
        "original_5cat": {
            "kappa": round(best['kappa'], 4),
            "exact_match_pct": round(best['match'], 1),
            "ann1_marginals": {CATS[i]: best['ann1'][i] for i in range(5)},
            "ann2_marginals": {CATS[i]: best['ann2'][i] for i in range(5)},
            "sc_to_sm_confusion": int(cm[4, 0]),
        },
        "collapsed_4cat": {
            "kappa": round(k4, 4),
            "exact_match_pct": round(m4, 1),
            "merge": "structural_misparse + spurious_compliance → policy_misinterpretation",
        },
        "collapsed_3cat": {
            "kappa": round(k3, 4),
            "exact_match_pct": round(m3, 1),
            "merge": "gap_filling + partial_compliance → gap+partial",
        },
    }

    out = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/human_collapsed_kappa.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out}")


if __name__ == "__main__":
    main()
