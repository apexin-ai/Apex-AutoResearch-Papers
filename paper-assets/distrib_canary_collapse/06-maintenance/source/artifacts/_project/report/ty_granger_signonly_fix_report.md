# TY Granger `signonly` Bug Fix Report

**Date**: 2026-05-20
**Server**: westd-17855
**File**: `run_5method_analysis_d102.py` (line 223)

## Bug

```python
# BEFORE (line 223):
test_result = result.test_causality(causing=1, caused=0, signonly=False)
f_stat = float(test_result.summary().data[0][1])
p_value = float(test_result.summary().data[0][2])
```

`signonly` is not a valid parameter for `statsmodels.tsa.vector_ar.var_model.VARResults.test_causality()` (v0.14.6). Valid params: `caused, causing, kind, signif`. Every TY call threw `TypeError`, caught by except → `significant=False` → TY=0/8 everywhere.

## Fix

```python
# AFTER:
test_result = result.test_causality(causing=1, caused=0, kind="f")
f_stat = float(test_result.test_statistic)
p_value = float(test_result.pvalue)
```

Backup: `run_5method_analysis_d102.py.bak_pre_ty_fix`

## Verification (3 experiments on westd-17855)

| exp_id | α | TY_before | TY_after | PermG_fwd | diff_fdr_fwd | K≥3_before | K≥3_after |
|--------|-----|-----------|----------|-----------|--------------|------------|-----------|
| a050_s42_fp32 | 0.50 | 0/8 | **3/8** | 6/8 | 7/8 | 5/8 | **6/8** |
| a075_s42_fp32 | 0.75 | 0/8 | **3/8** | 6/8 | 6/8 | 6/8 | 6/8 |
| pythia410m_wiki_a100_s43 | 1.00 | 0/8 | **4/8** | 6/8 | 6/8 | 6/8 | 6/8 |

### Per-pair TY detail (forward, post-fix)

**a050 (α=0.50)**:
- token_entropy→distinct_1: F=636.6, **p=0.0016** ✓
- token_entropy→distinct_2: F=10.2, p=0.091
- token_entropy→distinct_3: F=159.7, **p=0.006** ✓
- token_entropy→mauve: F=1.2, p=0.486
- ece→distinct_1: F=1.7, p=0.393
- ece→distinct_2: F=0.2, p=0.859
- ece→distinct_3: F=56.2, **p=0.018** ✓
- ece→mauve: F=0.2, p=0.882

**a075 (α=0.75)**:
- token_entropy→distinct_2: F=19.5, **p=0.049** ✓
- ece→distinct_1: F=5.7, **p=0.029** ✓
- ece→distinct_2: F=6.5, **p=0.021** ✓

**pythia410m (α=1.0)**:
- token_entropy→distinct_2: F=6.2, **p=0.024** ✓
- token_entropy→distinct_3: F=19.1, **p=0.001** ✓
- ece→distinct_2: F=60.5, **p=0.016** ✓
- ece→distinct_3: F=544.2, **p=0.002** ✓

## Impact on K≥3

- a050: K≥3 from 5/8 → **6/8** (token_entropy→distinct_1 gained TY vote: 2→3)
- a075, pythia410m: K≥3 unchanged at 6/8 (TY adds votes to already-robust pairs)

## 19828 Status

19828 has a different TY implementation (manual OLS + Wald F-test, no `test_causality()` call). Not affected by this bug. No sync needed.

## Note: Table display alignment

The printed table has a column alignment issue — TY_F column shows PermFDR value. **JSON output is correct** (verified by direct JSON read). Display-only bug, does not affect data.
