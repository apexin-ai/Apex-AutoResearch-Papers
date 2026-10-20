# D114: AUROC Calculation Inconsistency — Root Cause Analysis

## Summary

The 3-seed analysis script reported AUROC values systematically **higher** by 0.013–0.034 compared to Paper Table 1. Root cause: `>` vs `>=` at the median boundary in binarization.

## Root Cause

| Script | Threshold | Location |
|--------|-----------|----------|
| `analyze_exp015_unified.py` (Table 1) | `F1 >= median` | line 124 |
| `evaluation.py:compute_auroc` (3-seed) | `F1 > median` | line 320 (old) |
| `analyze_exp012_rerun_5signal.py` | `F1 >= 1.0` | line 186 |

On SciERC NER (median F1 = 2/3), 65 instances sit at exactly the median. Reassigning them shifts AUROC by 0.013–0.042.

## Fix

`evaluation.py:compute_auroc` changed from `l > med` to `l >= med` (lines 321-322).

## Verification

All Paper Table 1 values reproduced to <0.0005 after fix.

## Appendix Correction

Paper appendix (Table multiseed) NER AUROC updated:
- Qwen: LP .579±.008, FK .600±.016, SJ .659±.016, VC .677±.011, EM .631±.013
- LLaMA: LP .565±.008, FK .593±.006, SJ .632±.012, VC .673±.009, EM .606±.005

Signal ranking VC>SJ>EM>FK>LP unchanged across all seeds.