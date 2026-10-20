# Data Reconciliation Check — Recursive Generation Depth Estimation

**Date**: 2026-05-15
**Scope**: All key numerical claims for the paper, cross-validated against authoritative sources.

---

## Data Source Inventory

| Source | Path | Role |
|--------|------|------|
| Pipeline pairwise_auc.json | `results/{cell}/pairwise_auc.json` | **Ground truth** for AUC |
| edd_sensitivity.json | `artifacts/atlas_v2/edd_sensitivity.json` | EDD analysis (uses pipeline AUC) |
| edd_analysis_9cell.json | `artifacts/atlas_v2/edd_analysis_9cell.json` | **DO NOT CITE** (5-fold CV, biased +0.03–0.08) |
| cross_comparison_9cell.json | `artifacts/atlas_v2/cross_comparison_9cell.json` | Cross-model/strategy rank correlations |
| monotonicity_scores_9cell.json | `artifacts/atlas_v2/monotonicity_scores_9cell.json` | Monotonicity Spearman ρ |
| feature_importance.json | `results/{cell}/feature_importance.json` | RF feature importance (Gini) |
| summary_9cell.json | `results/baseline_battery_9cell/summary_9cell.json` | Baseline method comparison (RF/LR/CORAL/DivEye) |
| cross_model_loo.json | `results/cross_model_loo.json` | Cross-model LOO raw results |
| cross_strategy_loo.json | `results/cross_strategy_loo.json` | Cross-strategy LOO raw results |
| Registry experiments | MCP registry | Experiment metadata & summary metrics |

**9 cells** = 3 models (Pythia-1.4B, GPT-2-XL, OLMo-1B) × 3 strategies (nucleus_p095, temperature_09, topk_k50).

---

## 1. Pairwise AUC (54 values: 9 cells × 6 pairs)

**Authoritative source**: `results/{cell}/pairwise_auc.json` (RF classifier, single 80/20 split)

### Pipeline AUC values (RF)

| Cell | d0v1 | d0v2 | d0v3 | d1v2 | d1v3 | d2v3 |
|------|------|------|------|------|------|------|
| pythia_nucleus | 0.9975 | 0.9995 | 0.9986 | 0.8607 | 0.9685 | 0.8005 |
| pythia_temp09 | 0.9968 | 0.9993 | 0.9991 | 0.8327 | 0.9590 | 0.7928 |
| pythia_topk50 | 0.9927 | 0.9983 | 0.9978 | 0.7518 | 0.9176 | 0.6918 |
| gpt2xl_nucleus | 0.9941 | 0.9965 | 0.9988 | 0.9131 | 0.9857 | 0.8829 |
| gpt2xl_temp09 | 0.9963 | 0.9992 | 1.0000 | 0.9367 | 0.9947 | 0.8815 |
| gpt2xl_topk50 | 0.9884 | 0.9973 | 0.9981 | 0.8259 | 0.9630 | 0.7708 |
| olmo_nucleus | 0.9834 | 0.9949 | 0.9989 | 0.8673 | 0.9806 | 0.8124 |
| olmo_temp09 | 0.9960 | 0.9997 | 0.9995 | 0.9010 | 0.9874 | 0.8214 |
| olmo_topk50 | 0.9930 | 0.9983 | 0.9991 | 0.8305 | 0.9591 | 0.7357 |

### Cross-validation

| Check | Result |
|-------|--------|
| edd_sensitivity.json consecutive_aucs vs pipeline | **All 27 values match exactly** (d0v1, d1v2, d2v3 for 9 cells) |
| Per-cell registry metrics vs pipeline | **All match exactly** (spot-checked all 9 cells) |
| edd_analysis_9cell.json vs pipeline | **Systematically higher** (+0.03–0.08), expected from 5-fold CV. NOT cited. |

**Status: CONSISTENT** — All citable sources agree on AUC values.

---

## 2. RF 4-Class Accuracy (9 cells)

**Authoritative source**: `results/baseline_battery_9cell/summary_9cell.json` (consistent evaluation across all cells and methods)

### Accuracy by method (summary_9cell.json)

| Cell | RF | LR | CORAL | DivEye | Best |
|------|-----|-----|-------|--------|------|
| pythia_nucleus | 0.7813 | 0.7497 | 0.7807 | 0.7817 | 0.7817 (DivEye) |
| pythia_temp09 | 0.7677 | 0.7413 | 0.7717 | 0.7660 | 0.7717 (CORAL) |
| pythia_topk50 | 0.6870 | 0.6833 | 0.6877 | 0.6840 | 0.6877 (CORAL) |
| gpt2xl_nucleus | 0.8397 | 0.8143 | 0.8433 | 0.8363 | 0.8433 (CORAL) |
| gpt2xl_temp09 | 0.8527 | 0.8110 | 0.8470 | 0.8263 | 0.8527 (RF) |
| gpt2xl_topk50 | 0.7540 | 0.7130 | 0.7480 | 0.7100 | 0.7540 (RF) |
| olmo_nucleus | 0.7877 | 0.7547 | 0.7960 | 0.7740 | 0.7960 (CORAL) |
| olmo_temp09 | 0.8270 | 0.8147 | 0.8210 | 0.8093 | 0.8270 (RF) |
| olmo_topk50 | 0.7370 | 0.7590 | 0.7563 | 0.7360 | 0.7590 (LR) |

**Mean accuracy across 9 cells**: RF=0.7705, LR=0.7601, CORAL=0.7835, DivEye=0.7693

### Cross-validation

| Check | Result |
|-------|--------|
| Registry `best_acc_matrix_rf` vs summary_9cell best_acc_4class | **Match** after rounding to 3 dp (registry stores best-method accuracy rounded) |
| Per-cell pipeline registry vs summary_9cell | **Differ by 0.5–1.3pp** — expected: different train/test splits and evaluation seeds |
| cross_comparison_9cell.json 5-fold CV accuracy | **Slightly different** (e.g., pythia_topk50: 0.688 single-split vs 0.688 5-fold) — same evaluation protocol yields similar results |

### ⚠️ Note on registry `best_acc_matrix_rf`

Despite the field name, registry `baseline_battery_9cell_001.best_acc_matrix_rf` stores the **best accuracy across all methods** (not RF-only), rounded to 3 decimal places. All 9 values match `summary_9cell.json` best_acc_4class when rounded.

### ⚠️ Note on per-cell pipeline accuracy vs baseline battery

Per-cell pipeline registry RF accuracy differs from summary_9cell.json RF accuracy because they use different random seeds/splits. Example: pythia_temp09 pipeline=0.7625, battery=0.7677. **For method comparison in the paper, use summary_9cell.json exclusively** to ensure consistent evaluation setup.

**Status: CONSISTENT** within each source. Use summary_9cell.json for all method-comparison claims.

---

## 3. EDD Values (9 cells × 4 thresholds)

**Authoritative source**: `artifacts/atlas_v2/edd_sensitivity.json` (computed from pipeline AUC)

### EDD matrix

| Cell | T=0.65 | T=0.70 | T=0.75 | T=0.80 |
|------|--------|--------|--------|--------|
| pythia_nucleus | 3 | 3 | 3 | 3 |
| pythia_temp09 | 3 | 3 | 3 | 2 |
| pythia_topk50 | 3 | 2 | 2 | 1 |
| gpt2xl_nucleus | 3 | 3 | 3 | 3 |
| gpt2xl_temp09 | 3 | 3 | 3 | 3 |
| gpt2xl_topk50 | 3 | 3 | 3 | 2 |
| olmo_nucleus | 3 | 3 | 3 | 3 |
| olmo_temp09 | 3 | 3 | 3 | 3 |
| olmo_topk50 | 3 | 3 | 2 | 2 |

**Key claims**:
- T=0.75: EDD=3 for **7/9** cells, EDD=2 for 2/9 (pythia_topk50, olmo_topk50) ✅
- T=0.80: EDD=3 for 5/9, EDD=2 for 3/9, EDD=1 for 1/9

### Cross-validation

| Check | Result |
|-------|--------|
| Registry atlas_v2_analysis edd_equals_3_at_T075 | **7/9** ✅ matches |
| Registry atlas_v2_analysis edd_distribution_T075 | **{2: 2, 3: 7}** ✅ matches |
| edd_analysis_9cell.json EDD at T=0.75 | **Agrees** (7/9 = 3), despite using 5-fold CV AUCs |
| edd_analysis_9cell.json EDD at T=0.80 | **Differs** for pythia_topk50 (edd_sensitivity=1, edd_analysis=2) — because 5-fold CV d1v2=0.836 > 0.80 vs pipeline d1v2=0.752 < 0.80 |

**Status: CONSISTENT** for citable sources. The edd_analysis_9cell.json divergence at T=0.80 is expected and irrelevant (not cited).

---

## 4. Feature Importance Ranking (9 cells)

**Authoritative source**: `results/{cell}/feature_importance.json` (RF Gini importance)

### Top-2 features per cell

| Cell | #1 | #2 | p90_ppl in top-2? | var_surprisal in top-2? |
|------|-----|-----|:-:|:-:|
| pythia_nucleus | var_surprisal (0.169) | p90_ppl (0.158) | ✅ | ✅ |
| pythia_temp09 | var_surprisal (0.178) | p90_ppl (0.150) | ✅ | ✅ |
| pythia_topk50 | var_surprisal (0.176) | p90_ppl (0.135) | ✅ | ✅ |
| gpt2xl_nucleus | p90_ppl (0.208) | var_surprisal (0.208) | ✅ | ✅ |
| gpt2xl_temp09 | p90_ppl (0.263) | mean_surprisal (0.148) | ✅ | ❌ (#4, 0.121) |
| gpt2xl_topk50 | p90_ppl (0.244) | p75_ppl (0.137) | ✅ | ❌ (#4, 0.090) |
| olmo_nucleus | p90_ppl (0.180) | var_surprisal (0.161) | ✅ | ✅ |
| olmo_temp09 | p90_ppl (0.199) | var_surprisal (0.174) | ✅ | ✅ |
| olmo_topk50 | p90_ppl (0.217) | var_surprisal (0.168) | ✅ | ✅ |

**Claims**: p90_ppl in top-2 = **9/9** ✅, var_surprisal in top-2 = **7/9** ✅

### Cross-validation

| Check | Result |
|-------|--------|
| Registry atlas_v2_analysis p90_ppl_in_top2 | **"9/9"** ✅ |
| Registry atlas_v2_analysis var_surprisal_in_top2 | **"7/9"** ✅ |
| Per-cell registry top_features lists | **Consistent** (all list p90_ppl and var_surprisal in top-5) |

**Status: CONSISTENT**

---

## 5. Cross-Model Rank Correlation

**Authoritative source**: `artifacts/atlas_v2/cross_comparison_9cell.json`

### All 18 pairwise Spearman ρ values

**Cross-model** (9 pairs):

| Pair | ρ |
|------|---|
| pythia vs gpt2xl (nucleus) | 0.861 |
| pythia vs olmo (nucleus) | 0.619 |
| gpt2xl vs olmo (nucleus) | 0.858 |
| pythia vs gpt2xl (temp09) | 0.882 |
| pythia vs olmo (temp09) | 0.819 |
| gpt2xl vs olmo (temp09) | 0.914 |
| pythia vs gpt2xl (topk50) | 0.840 |
| pythia vs olmo (topk50) | 0.884 |
| gpt2xl vs olmo (topk50) | 0.954 |

Cross-model only: mean=0.848, range=[0.619, 0.954]

**Cross-strategy** (9 pairs):

| Pair | ρ |
|------|---|
| nucleus vs temp09 (Pythia) | 0.814 |
| nucleus vs topk50 (Pythia) | 0.842 |
| temp09 vs topk50 (Pythia) | 0.925 |
| nucleus vs temp09 (GPT-2 XL) | 0.949 |
| nucleus vs topk50 (GPT-2 XL) | 0.940 |
| temp09 vs topk50 (GPT-2 XL) | 0.923 |
| nucleus vs temp09 (OLMo) | 0.896 |
| nucleus vs topk50 (OLMo) | 0.811 |
| temp09 vs topk50 (OLMo) | 0.891 |

Cross-strategy only: mean=0.888, range=[0.811, 0.949]

**All 18 pairs**: mean=**0.868**, range=**[0.619, 0.954]**

### Cross-validation

| Check | Result |
|-------|--------|
| cross_comparison_9cell.json summary rank_corr_mean | **0.868** ✅ (mean of all 18 pairs) |
| cross_comparison_9cell.json summary rank_corr_range | **[0.619, 0.954]** ✅ |
| Registry atlas_v2_analysis cross_model_rank_corr_mean | **0.868** ✅ |
| Registry atlas_v2_analysis cross_model_rank_corr_range | **"[0.619, 0.954]"** ✅ |

### ⚠️ Labeling clarification

The registry field `cross_model_rank_corr_mean = 0.868` and the JSON `summary.rank_corr_mean = 0.868` are the mean of **all 18 pairwise** correlations (cross-model + cross-strategy combined), not cross-model only. Pure cross-model mean is 0.848.

**Recommendation**: If the paper claims "cross-model feature importance rank correlation mean 0.868", either:
- (a) Change to "pairwise feature importance rank correlation mean 0.868" (all 18 pairs), or
- (b) Use the cross-model-only mean 0.848 and keep the "cross-model" label.

The range [0.619, 0.954] is valid for both since min and max both come from cross-model pairs.

**Status: VALUES CONSISTENT**, but label needs clarification.

---

## 6. Cross-Model LOO Accuracy (3 rotations)

**Authoritative source**: `results/cross_model_loo.json` + registry `cross_model_loo_v1`

| Rotation | Accuracy | CI 95% | d1v2 AUC | d2v3 AUC |
|----------|----------|--------|----------|----------|
| Hold-out Pythia | 0.6242 | [0.6206, 0.6282] | 0.5617 | 0.6534 |
| Hold-out OLMo | 0.6921 | [0.6886, 0.6959] | 0.7687 | 0.6862 |
| Hold-out GPT-2 XL | 0.6756 | [0.6719, 0.6792] | 0.8157 | 0.6639 |
| **Mean** | **0.6640** | | | |

**Claim**: mean 66.4% ✅

### Cross-validation

| Check | Result |
|-------|--------|
| Registry cross_model_loo_v1 mean_acc | **0.664** ✅ |
| Registry cross_model_loo_v1 per-rotation | **All match** JSON exactly |
| Registry cross_model_loo_001 (same exp, different entry) | **All match** |
| Computed mean: (0.6242+0.6921+0.6756)/3 | **0.6640** ✅ |

**Status: CONSISTENT**

---

## 7. Cross-Strategy LOO Accuracy (9 rotations)

**Authoritative source**: `results/cross_strategy_loo.json` + registry `cross_strategy_loo_001`

| Model | Hold-out | Accuracy | d1v2 AUC | d2v3 AUC |
|-------|----------|----------|----------|----------|
| Pythia | nucleus | 0.6935 | 0.6903 | 0.7626 |
| Pythia | temp09 | 0.6281 | 0.5760 | 0.7240 |
| Pythia | topk50 | 0.5151 | 0.6393 | 0.5801 |
| GPT-2 XL | nucleus | 0.5993 | 0.7826 | 0.4985 |
| GPT-2 XL | temp09 | 0.5609 | 0.1288 | 0.6366 |
| GPT-2 XL | topk50 | 0.5364 | 0.8308 | 0.7222 |
| OLMo | nucleus | 0.6538 | 0.7931 | 0.6076 |
| OLMo | temp09 | 0.5816 | 0.2529 | 0.7015 |
| OLMo | topk50 | 0.5488 | 0.8549 | 0.7107 |
| **Mean** | | **0.5908** | | |

**Claim**: mean 59.1% ✅ (0.5908 → 59.1%)

### Cross-validation

| Check | Result |
|-------|--------|
| Registry cross_strategy_loo_001 mean_4class_acc | **0.5908** ✅ |
| Registry per-rotation values | **All 9 match** JSON exactly |
| Computed mean: sum/9 | **0.5908** ✅ |

**Status: CONSISTENT**

---

## 8. Monotonicity ρ

**Authoritative source**: `artifacts/atlas_v2/monotonicity_scores_9cell.json`

### Key features ρ by cell

| Cell | p90_ppl ρ | var_surprisal ρ |
|------|-----------|----------------|
| pythia_nucleus | -1.0 | -1.0 |
| pythia_temp09 | -1.0 | -1.0 |
| pythia_topk50 | -1.0 | -1.0 |
| gpt2xl_nucleus | -1.0 | -1.0 |
| gpt2xl_temp09 | -1.0 | -1.0 |
| gpt2xl_topk50 | -1.0 | -1.0 |
| olmo_nucleus | -1.0 | -1.0 |
| olmo_temp09 | -1.0 | -1.0 |
| olmo_topk50 | -1.0 | -1.0 |

**All** p90_ppl and var_surprisal have ρ = **-1.0** (p = 0.0) across all 9 cells — perfect monotonic decrease with depth.

p75_ppl also ρ = -1.0 in all 9 cells. mean_surprisal ρ = -1.0 in all cells where reported. mean_ppl has non-monotonic behavior in some cells (e.g., pythia_topk50 ρ = -0.6, olmo_topk50 ρ = 0.2).

**Status: CONSISTENT**

---

## 9. Baseline Comparison (CORAL / DivEye / CE-MLP)

### Single-cell (Pythia nucleus only)

**Authoritative source**: Registry `baseline_battery_001`

| Method | 4-class Acc | d1v2 AUC |
|--------|------------|----------|
| RF | 0.781 | — |
| LR | 0.750 | — |
| CORAL | 0.7807 | 0.8179 |
| DivEye | 0.7817 | 0.8654 |
| CE-MLP | 0.749 | — |

CE-MLP caveat: "may be undertrained (5 epochs)"

### 9-cell comparison

**Authoritative source**: `results/baseline_battery_9cell/summary_9cell.json`

Mean 4-class accuracy across 9 cells:
- **CORAL**: 0.784 (best)
- **RF**: 0.771
- **DivEye**: 0.769
- **LR**: 0.760

Finding: **CORAL ≈ RF > DivEye > LR**, max per-cell gap ~4.4pp (gpt2xl_topk50: RF 0.754 vs DivEye 0.710)

### Cross-validation

| Check | Result |
|-------|--------|
| Registry finding "RF ≈ CORAL > DivEye > LR, max gap ~4pp" | ✅ consistent |
| Registry "GPT-2 XL temp09 best (85.3%)" | ✅ gpt2xl_temp09 RF=0.8527 is highest single-cell accuracy |
| baseline_battery_001 pythia_nucleus vs summary_9cell.json pythia_nucleus | ✅ CORAL 0.7807=0.7807, DivEye 0.7817=0.7817 |

**Status: CONSISTENT**

---

## Summary of Conflicts

| # | Issue | Severity | Resolution |
|---|-------|----------|------------|
| 1 | Registry `best_acc_matrix_rf` stores best-across-methods, not RF-only | Low (naming) | Use summary_9cell.json directly; ignore misleading field name |
| 2 | Per-cell pipeline accuracy ≠ baseline battery accuracy (different splits) | Low (expected) | Use summary_9cell.json for method comparison; use per-cell pipeline for AUC |
| 3 | Registry `cross_model_rank_corr_mean=0.868` includes cross-strategy pairs | Medium (labeling) | Paper should say "pairwise" (all 18 pairs) or use 0.848 for cross-model-only |
| 4 | edd_analysis_9cell.json AUC systematically biased +0.03–0.08 | N/A | Already excluded from paper citations |

**No data integrity conflicts found.** All citable values are internally consistent across their authoritative sources.

---

## Paper-Safe Citation Guide

| Claim | Value | Authoritative Source |
|-------|-------|---------------------|
| RF 4-class accuracy range | 68.7%–85.3% | summary_9cell.json (RF column) |
| Best single-cell accuracy | 85.3% (GPT-2 XL, temp09) | summary_9cell.json gpt2xl_temp09.rf |
| Pairwise AUC (any cell, any pair) | See §1 table | results/{cell}/pairwise_auc.json |
| d1v2 AUC range (RF) | 0.752–0.937 | Pipeline pairwise_auc.json |
| d2v3 AUC range (RF) | 0.692–0.882 | Pipeline pairwise_auc.json |
| EDD=3 at T=0.75 | 7/9 cells | edd_sensitivity.json |
| EDD distribution at T=0.75 | {EDD=2: 2, EDD=3: 7} | edd_sensitivity.json |
| EDD distribution at T=0.80 | {EDD=1: 1, EDD=2: 3, EDD=3: 5} | edd_sensitivity.json |
| p90_ppl in top-2 features | 9/9 cells | results/{cell}/feature_importance.json |
| var_surprisal in top-2 features | 7/9 cells | results/{cell}/feature_importance.json |
| Pairwise rank correlation mean | 0.868 (all 18 pairs) | cross_comparison_9cell.json |
| Cross-model rank corr mean | 0.848 (9 cross-model pairs only) | cross_comparison_9cell.json (computed) |
| Rank correlation range | [0.619, 0.954] | cross_comparison_9cell.json |
| Cross-model LOO mean acc | 66.4% | cross_model_loo.json / registry cross_model_loo_v1 |
| Cross-strategy LOO mean acc | 59.1% | cross_strategy_loo.json / registry cross_strategy_loo_001 |
| Monotonicity ρ (p90_ppl, var_surprisal) | -1.0 (all 9 cells) | monotonicity_scores_9cell.json |
| Baseline ordering | CORAL ≈ RF > DivEye > LR | summary_9cell.json |
| Baseline max per-cell gap | ~4pp | summary_9cell.json |
| CE-MLP accuracy (Pythia nucleus) | 74.9% (undertrained) | Registry baseline_battery_001 |
| CORAL mean 9-cell accuracy | 78.4% | summary_9cell.json |
| DivEye mean 9-cell accuracy | 76.9% | summary_9cell.json |
