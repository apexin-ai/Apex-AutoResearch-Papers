# NVE Threshold Sensitivity Audit Note

**Date:** 2026-05-17
**Trigger:** Reviewer identified that `nve_threshold_sensitivity.json` omitted exp_008e_v3_s2.

## 1. What Changed

exp_008e_v3_s2 (trained dt_emb, dt=1 imagination, H=15, seed 2) was missing from the analysis. This experiment has peak NVE = 3.78x at 105K steps but is **not** CIVO — it is Imagination-Reality Divergence (IRD), where eval collapse (715 -> 137) precedes and causes the passive NVE rise, the opposite of CIVO's causal direction. Label = 0.

At threshold = 1.5x, this experiment is a false positive (NVE > 1.5x but not CIVO).

## 2. Before / After Comparison (threshold = 1.5x)

| Metric | Before (11 exp) | After (12 exp) |
|--------|-----------------|-----------------|
| n_experiments | 11 (3 pos / 8 neg) | 12 (3 pos / 9 neg) |
| TP / FP / TN / FN | 3 / 0 / 8 / 0 | 3 / 1 / 8 / 0 |
| Accuracy | 1.000 (11/11) | 0.917 (11/12) |
| Precision | 1.000 | 0.750 (3/4) |
| Recall | 1.000 | 1.000 |
| F1 | 1.000 | 0.857 (6/7) |
| AUROC | 1.000 | 0.926 (25/27) |

## 3. Full Threshold Sweep (12 experiments)

| Threshold | TP | FP | TN | FN | Accuracy | Precision | Recall | F1 |
|-----------|----|----|----|----|----------|-----------|--------|-----|
| 1.3x | 3 | 3 | 6 | 0 | 0.750 | 0.500 | 1.000 | 0.667 |
| **1.5x** | **3** | **1** | **8** | **0** | **0.917** | **0.750** | **1.000** | **0.857** |
| 1.7x | 1 | 1 | 8 | 2 | 0.750 | 0.500 | 0.333 | 0.400 |
| 2.0x | 1 | 1 | 8 | 2 | 0.750 | 0.500 | 0.333 | 0.400 |

AUROC = 25/27 = 0.926. Computed via Wilcoxon-Mann-Whitney: exp_008e_v3_s2 (3.78, label=0) creates 2 discordant pairs with positives 1.619 and 1.528.

## 4. Accuracy Claim Discrepancy: "7/8" vs "11/12"

### Paper claim: "7/8 seeds (AUROC=0.933)"

- **Source:** framing_b_reaudit.md, method.md (DIFF-M7), nve_sensitivity_table.tex (Task B2)
- **Basis:** 8 non-baseline experimental conditions. 3 positive (CIVO: exp_008d, exp_009b, exp_008d_civo_trigger_s3) / 5 negative (non-CIVO non-baseline).
- **Excludes:** 3 baseline entries (baseline_s1, exp_009a_baseline_walker_s2, exp_009d_baseline_walker_s1) and 1 duplicate seed (exp_008e_v3_s1, same condition as s2).

### Corrected JSON: "11/12 = 0.917"

- **Basis:** All 12 experiments including baselines and both 008e_v3 seeds. 3 positive / 9 negative.
- **Includes:** Everything in the 7/8 set plus 3 baselines and exp_008e_v3_s1.

### Key difference

The two numbers measure the same threshold on different experiment pools:

| Scope | Experiments | Pos/Neg | Accuracy @1.5x | AUROC |
|-------|-------------|---------|-----------------|-------|
| Non-baseline only (paper B2) | 8 | 3/5 | 7/8 = 0.875 | 0.867* |
| All experiments (JSON) | 12 | 3/9 | 11/12 = 0.917 | 0.926 |

*The paper claims AUROC = 0.933 for the 8-experiment set. This is **incorrect**. With 3 positives (peaks: 4.13, 1.62, 1.53) and 5 negatives (including 3.78), there are 2 discordant pairs (not 1), giving AUROC = 13/15 = 0.867, not 14/15 = 0.933.

### AUROC=0.933 error analysis

AUROC = 0.933 = 14/15 requires exactly 1 discordant pair among 15. But exp_008e_v3_s2 (3.78) ranks above both exp_009b (1.619) and exp_008d_civo_trigger_s3 (1.528), creating 2 discordant pairs. There is no valid 3-positive / 5-negative subset of this data that yields AUROC = 14/15.

## 5. What the Paper Needs to Say

1. **Replace** any "perfect classification" / "AUROC=1.0" claims at threshold 1.5x with the corrected numbers.
2. **Fix AUROC** in nve_sensitivity_table.tex: B2 AUROC should be 0.867, not 0.933.
3. **Clarify scope** when citing accuracy numbers:
   - "11/12 (0.917)" if reporting over all experiments including baselines
   - "7/8 (0.875)" if reporting over non-baseline conditions only
4. **Explain the FP:** exp_008e_v3_s2 exceeds NVE 1.5x via IRD (eval collapse drives passive NVE rise), not CIVO (NVE rise drives eval decline). This is already well-handled in Section 4.6 (failure taxonomy) of results.md. The paper should reference this distinction when presenting diagnostic accuracy.
5. **Implication for the NVE diagnostic:** NVE > 1.5x is a necessary condition for CIVO but not sufficient. Trajectory shape analysis (NVE rise precedes vs. follows eval decline) is needed to distinguish CIVO from IRD. This is a limitation worth acknowledging, and strengthens the case for the three-failure-mode taxonomy.
