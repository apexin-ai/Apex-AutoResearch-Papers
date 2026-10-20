# NVE Threshold Sensitivity Analysis

**Date**: 2026-05-15
**Task**: plan_034
**Metric**: NVE = (value_mean / eval_return) / (baseline_value_mean / baseline_eval_return) at matching steps

## Experiment Summary

| Experiment | GT Label | Max NVE | Final NVE | Mean Last-3 |
|---|---|---|---|---|
| exp_001_baseline | healthy (ref) | 1.0023 | 1.0006 | 1.0001 |
| exp_006_fixed_dt2 | collapsed | **4.8355** | 4.8355 | 2.9188 |
| exp_007_fixed_dt4 | collapsed | 1.9667 | 0.1507 | 0.4601 |
| exp_008a_no_subsample_dt2 | healthy | 1.7241 | 0.5886 | 0.6841 |
| exp_008c_no_subsample_dt2_h8 | collapsed | 1.2264 | 0.5822 | 0.6894 |
| exp_008d_subsample_on_h8 | collapsed | **4.1245** | 4.1245 | 2.6415 |
| exp_008e_v3_walker_s1 | healthy | 1.9338 | 0.8025 | 0.7726 |
| exp_008e_v3_walker_s2 | collapsed | **3.7825** | 3.7825 | 1.9345 |
| exp_008f_no_dt_embed_subsample_on_h8 | healthy | 1.0230 | 0.2976 | 0.4937 |

## Baseline V/E Reference

| Step | Baseline V/E |
|---|---|
| 25K | 0.087 |
| 35K | 0.241 |
| 45K | 0.331 |
| 55K | 0.404 |
| 65K | 0.563 |
| 75K | 0.719 |
| 85K | 0.701 |
| 95K | 0.632 |
| 105K | 0.656 |

## Classification at Requested Thresholds (Max NVE strategy)

Baseline excluded from classification (N=8: 5 collapsed, 3 healthy).

| Threshold | TP | TN | FP | FN | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|---|---|---|---|
| 1.3 | 4 | 1 | 2 | 1 | 0.6250 | 0.6667 | 0.8000 | 0.7273 |
| 1.5 | 4 | 1 | 2 | 1 | 0.6250 | 0.6667 | 0.8000 | 0.7273 |
| 1.7 | 4 | 1 | 2 | 1 | 0.6250 | 0.6667 | 0.8000 | 0.7273 |
| 2.0 | 3 | 3 | 0 | 2 | 0.7500 | 1.0000 | 0.6000 | 0.7500 |

**Error analysis at threshold=1.3-1.7:**
- FP: exp_008a (max NVE 1.72, healthy), exp_008e_v3_s1 (max NVE 1.93, healthy) — both spike early at 25K then settle
- FN: exp_008c (max NVE 1.23, collapsed) — never exceeds any tested threshold

**Error analysis at threshold=2.0:**
- FN: exp_007 (max NVE 1.97), exp_008c (max NVE 1.23) — collapsed but low NVE

## AUROC

| Strategy | AUROC | Notes |
|---|---|---|
| **Max NVE (any step)** | **0.8667** | Best discriminator |
| Mean Last-3 NVE | 0.7333 | |
| Final Step NVE | 0.6667 | Worst — collapsed exps that die early get low final NVE |

Score distributions (Max NVE):
- Collapsed: min=1.23, mean=3.19, max=4.84
- Healthy: min=1.02, mean=1.56, max=1.93

## Optimal Threshold

**Recommended: Max NVE strategy, threshold = 1.95**

| Metric | Value |
|---|---|
| TP | 4 |
| TN | 3 |
| FP | 0 |
| FN | 1 (exp_008c) |
| Accuracy | **0.8750** |
| Precision | **1.0000** |
| Recall | 0.8000 |
| F1 | **0.8889** |

The sole misclassification is **exp_008c_no_subsample_dt2_h8** (max NVE = 1.23), which collapses through a different mechanism — eval performance degrades but the value/eval ratio stays near baseline levels.

## Key Findings

1. **Max NVE is the best single-number classifier** (AUROC 0.87). Final NVE fails because collapsed experiments where both value and eval drop to zero produce low NVE.

2. **Threshold 1.95 is the sweet spot**: perfect precision (no false alarms), 80% recall, F1=0.89. The requested thresholds (1.3-1.7) have too many FPs; 2.0 loses one true positive (exp_007).

3. **Two failure modes that NVE misses:**
   - **exp_007_fixed_dt4**: value and eval both collapse to near-zero. NVE spikes only briefly at 25K (1.97) then drops. Barely caught at threshold < 1.97.
   - **exp_008c**: NVE never exceeds 1.23. This is a collapse where the critic stays calibrated relative to (bad) performance — NVE alone cannot detect it.

4. **Early-step spikes are noise, not signal**: healthy experiments (008a, 008e_s1) show NVE > 1.7 at step 25K due to noisy early training, then normalize. A robust classifier should either (a) skip early steps or (b) require NVE > threshold sustained over multiple checkpoints.

## Recommendation for Production Use

- Use **Max NVE ≥ 1.95** as primary collapse detector (high precision)
- Add a secondary check: **eval_return at final step < 50% of baseline** to catch exp_008c-type failures where NVE stays low but performance is poor
- Optionally, ignore steps before 35K to reduce false positives from early training noise
