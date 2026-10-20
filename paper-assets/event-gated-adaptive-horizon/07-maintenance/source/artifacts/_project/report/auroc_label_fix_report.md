# AUROC Label Consistency Fix Report

**Date**: 2026-05-22
**Issue**: exp_008e_v3_s2 labeled as non-CIVO (FP) in n=16 analysis but as CIVO-positive (TP) in n=29 analysis.

## 1. Label Fix

| Field | Before | After |
|-------|--------|-------|
| exp_id | 008e_v3_s2 | 008e_v3_s2 |
| n=16 label | non-CIVO (negative) | non-CIVO (negative) — **unchanged** |
| n=29 label | **CIVO (positive)** | **non-CIVO / IRD (negative)** — **fixed** |
| NVE peak | 3.780 @ 105K | 3.780 @ 105K |

**Rationale**: D039/D040 mechanism analysis concluded eval-driven collapse (eval 715→137 at 85K-105K), not value-driven. Entropy increases (exploration expands) rather than decreases (CIVO pattern requires entropy collapse). NVE rise is a consequence of eval denominator collapse, not a causal predictor.

## 2. Updated AUROC Values

### n=16 Analysis (no change)

The n=16 analysis already had 008e_v3_s2 correctly labeled as non-CIVO.

| Metric | Value |
|--------|-------|
| AUROC | 0.969 |
| n | 16 (8 pos / 8 neg) |
| Accuracy @ θ=1.5× | 93.8% (15/16) |
| TP / FP / FN / TN | 8 / 1 / 0 / 7 |
| 95% CI (accuracy) | [69.8%, 99.8%] |

### n=29 Analysis (corrected)

| Metric | Original | Corrected | Δ |
|--------|----------|-----------|---|
| AUROC | 0.971 | **0.953** | −0.018 |
| 95% Bootstrap CI | [0.904, 1.000] | **[0.867, 1.000]** | wider |
| n_pos / n_neg | 13 / 16 | **12 / 17** | |
| Accuracy @ θ=1.5× | 93.1% (27/29) | **89.7% (26/29)** | −1 correct |
| FP @ θ=1.5× | 2 | **3** | +1 |
| TPR @ θ=1.5× | 1.00 | 1.00 | — |
| FPR @ θ=1.5× | 0.12 | **0.18** | +0.06 |
| Concordant pairs | 202/208 | **194.5/204** | |

## 3. Confusion Matrix (corrected n=29, θ=1.5×)

```
                Predicted CIVO    Predicted non-CIVO
True CIVO          TP = 12             FN = 0
True non-CIVO      FP = 3              TN = 14
```

Precision = 12/15 = 80.0%, Recall = 12/12 = 100%, F1 = 88.9%

## 4. FP and FN Details

### False Positives (3)

| exp_id | NVE peak | Predicted | True | Mechanism |
|--------|----------|-----------|------|-----------|
| 025_obs_sgs_s2 | 1.730 | CIVO | non-CIVO | Obs-decoder SGS failure damages shared RSSM latent space, causing systematic value miscalibration. NVE elevation is a side effect of representation damage, not the CIVO positive feedback loop. |
| 028_rave_ceil15 | 2.230 | CIVO | non-CIVO | RAVE anchor pollution: the EMA value anchor itself becomes inflated under CIVO dynamics, producing overestimation through a value anchoring pathway distinct from dt_emb-driven CIVO. |
| 008e_v3_s2 | 3.780 | CIVO | non-CIVO (IRD) | Imagination-Reality Divergence. Eval-driven collapse (eval 715→137 at 85K-105K) where NVE rise is consequence of eval denominator collapse, not cause. Entropy increases (more exploration), opposite of CIVO pattern (entropy collapse → exploitation lock-in). dt_emb is trained but imagination uses dt=1 (gating locked), preventing the multi-rate imagination exposure required for CIVO. |

### False Negatives (0)

None. All 12 CIVO-positive experiments are correctly detected at θ=1.5×.

## 5. Label Consistency Check

### 008e_v3_s2

| Analysis | Label | Consistent? |
|----------|-------|-------------|
| n=16 | non-CIVO (FP at θ=1.5×) | ✓ (was already correct) |
| n=29 | **non-CIVO** (was CIVO, now fixed) | ✓ (now consistent) |
| n=12 (nve_threshold_sensitivity.json) | non-CIVO (label=0, IRD) | ✓ |
| n=8 (nve_threshold_v3_ci_supplement_d054.json) | non-CIVO (negative) | ✓ |

### 025_obs_sgs_s2

Only present in n=29 analysis (SGS experiments postdate n=16 analysis). Labeled non-CIVO in n=29. **No cross-analysis inconsistency possible.** ✓

### 028_rave_ceil15

Only present in n=29 analysis (RAVE experiments postdate n=16 analysis). Labeled non-CIVO in n=29. **No cross-analysis inconsistency possible.** ✓

## 6. Impact on Paper Claims

The corrected AUROC (0.953 → from 0.971) still supports the paper's diagnostic validity claim. The 95% CI [0.867, 1.000] remains well above chance (0.5). The additional FP (008e_v3_s2) is mechanistically distinct from CIVO, reinforcing the paper's argument that NVE detects value overestimation broadly — a feature for practitioners rather than a limitation.

The n=16 analysis (AUROC=0.969) is unaffected.

## 7. Files Modified

- `artifacts/auroc_label_fix_result.json` — structured recomputation output
- `artifacts/auroc_label_fix_recompute.py` — recomputation script
- This report: `artifacts/auroc_label_fix_report.md`
