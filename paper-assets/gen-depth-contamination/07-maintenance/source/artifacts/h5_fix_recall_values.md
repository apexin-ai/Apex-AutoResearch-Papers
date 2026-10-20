# H5: Tab s3c OBD Per-Depth Recall Fix

## Problem

Tab s3c (appendix.tex:205) OBD-LightGBM per-depth recall values weighted sum = 38.0%, but OBD overall accuracy = 38.6% (registry `exp_011_llm_zeroshot.odb_baseline_5class_acc`).

## Root Cause

The per-depth values in Tab s3c came from a later rebuttal analysis (exp_D_obd_n500_v2.json) that used different hyperparameters (n_est=200, md=6, nl=31) and possibly different classification logic ("v2 logic: 6-class argmax, no capping/merge"). The original exp_011 used the pipeline's standard multiclass LightGBM (n_est=300, md=8, nl=63).

## Reproduction Method

- Data: `data_exp016_qwen_base/features.csv` (30,000 samples, depths 0-5)
- Model: 6-class multiclass LightGBM, 5-fold GroupKFold CV (pipeline params: n_est=300, md=8, nl=63)
- Sample: first 100 doc_ids per depth (depths 0-4), N=500
- Result: 193/500 = **38.6%** (exact match)

Script: `scripts/fix_recall_6class.py`, output: `/tmp/fix_recall_6class.log`

## Old Values (wrong)

| Depth 0 | Depth 1 | Depth 2 | Depth 3 | Depth 4 | Sum |
|---------|---------|---------|---------|---------|-----|
| 96      | 39      | 14      | 19      | 22      | 190/500 = 38.0% |

## New Values (correct)

| Depth 0 | Depth 1 | Depth 2 | Depth 3 | Depth 4 | Sum |
|---------|---------|---------|---------|---------|-----|
| 94      | 44      | 17      | 15      | 23      | 193/500 = 38.6% |

## Verification

94 + 44 + 17 + 15 + 23 = 193 correct out of 500 = 38.6% = 0.386 ✓

## Changes Required in LaTeX

### appendix.tex line 205

Old:
```latex
OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
```

New:
```latex
OBD-LightGBM & \textbf{94} & \textbf{44} & 17 & 15 & 23 \\
```

Bold pattern unchanged: OBD still has highest recall at Depth 0 (94 > 77, 69) and Depth 1 (44 > 21, 19).

### Caption consideration (appendix.tex line 198)

Current caption: "OBD's nominal overall accuracy gap originates from depth-0"

With corrected values, OBD's advantage over GPT-5.5 by depth:
- D0: +17, D1: +25, D2: -21, D3: -9, D4: +15

The largest gap contribution is now Depth 1 (+25), not Depth 0 (+17). Caption could be updated to "from depths 0--1" but this is a minor wording issue, not a numerical error.

## GPT-5.5 and Claude rows

No changes needed. Both are self-consistent with their confusion matrices in Tab s3:
- GPT-5.5: 77+19+38+24+8 = 166/500 = 0.332 ✓
- Claude: 69+21+28+10+37 = 165/499 = 0.331 ✓
