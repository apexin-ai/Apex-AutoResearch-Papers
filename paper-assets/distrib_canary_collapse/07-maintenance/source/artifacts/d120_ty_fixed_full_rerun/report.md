# D120: TY Granger Bug Fix — Full Rerun Results

**Date**: 2026-05-20
**Bug**: `signonly` parameter passed to statsmodels TY Granger (not supported), causing all TY results = 0/8
**Fix**: Removed `signonly` parameter from `run_5method_analysis_d102.py`
**Scope**: 17 complete alpha_sweep experiments reanalyzed on westd-17855

## Validation

**a050_s42_fp32**: TY=3/8, K≥3=6/8 ✓ (matches Reviewer independent verification)

## Full Dose-Response Table (TY Fixed)

### WikiText Experiments

| exp_id | α | seed | naive_fwd | diff_fdr | thresh | perm_fdr | perm_rev | **TY** | K≥3 | K≥4 |
|--------|------|------|-----------|----------|--------|----------|----------|--------|-----|-----|
| a010_s42_fp32 | 0.10 | 42 | 3 | 6 | 0 | 0 | 0 | **0** | 0 | 0 |
| a010_s43_fp32 | 0.10 | 43 | 4 | 7 | 2 | 3 | 0 | **3** | 4 | 2 |
| a025_s42_fp32 | 0.25 | 42 | 1 | 3 | 0 | 0 | 0 | **2** | 0 | 0 |
| a025_s43_fp32 | 0.25 | 43 | 0 | 0 | 0 | 0 | 0 | **1** | 0 | 0 |
| a025_s44_fp32 | 0.25 | 44 | 1 | 0 | 0 | 0 | 0 | **0** | 0 | 0 |
| a030_s42_fp32 | 0.30 | 42 | 3 | 4 | 0 | 0 | 0 | **3** | 1 | 0 |
| a035_s42_fp32 | 0.35 | 42 | 0 | 4 | 0 | 0 | 0 | **1** | 0 | 0 |
| a040_s42_fp32 | 0.40 | 42 | 4 | 3 | 0 | 0 | 0 | **4** | 1 | 0 |
| a045_s42_fp32 | 0.45 | 42 | 1 | 6 | 0 | 0 | 0 | **1** | 0 | 0 |
| a050_s42_fp32 | 0.50 | 42 | 3 | 7 | 4 | 6 | 0 | **3** | 6 | 3 |
| a050_s43_fp32 | 0.50 | 43 | 2 | 6 | 6 | 6 | 0 | **0** | 5 | 1 |
| a050_s44_fp32 | 0.50 | 44 | 5 | 8 | 0 | 6 | 0 | **0** | 3 | 0 |
| a060_s43_fp32 | 0.60 | 43 | 1 | 6 | 0 | 0 | 0 | **1** | 0 | 0 |
| a075_s42_fp32 | 0.75 | 42 | 7 | 6 | 0 | 6 | 0 | **3** | 6 | 3 |

### C4 Experiments

| exp_id | α | seed | naive_fwd | diff_fdr | thresh | perm_fdr | perm_rev | **TY** | K≥3 | K≥4 |
|--------|------|------|-----------|----------|--------|----------|----------|--------|-----|-----|
| c4_a025_s42_fp32 | 0.25 | 42 | 4 | 8 | 2 | 0 | 0 | **4** | 3 | 0 |
| c4_a050_s42_fp32 | 0.50 | 42 | 4 | 8 | 0 | 8 | 7 | **2** | 6 | 0 |
| c4_a075_s42_fp32 | 0.75 | 42 | 8 | 8 | 0 | 8 | 0 | **3** | 8 | 3 |

## TY Fix Impact: Before → After Comparison

Before fix: TY=0/8 for all experiments (bug: `signonly` not supported).

| exp_id | α | TY (fixed) | K≥3 before | K≥3 after | Δ K≥3 | K≥4 before | K≥4 after | Δ K≥4 |
|--------|------|------------|------------|-----------|-------|------------|-----------|-------|
| a010_s42_fp32 | 0.10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| a010_s43_fp32 | 0.10 | 3 | 4 | 4 | 0 | 1 | 2 | +1 |
| a025_s42_fp32 | 0.25 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| a025_s43_fp32 | 0.25 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| a025_s44_fp32 | 0.25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| a030_s42_fp32 | 0.30 | 3 | 0 | 1 | **+1** | 0 | 0 | 0 |
| a035_s42_fp32 | 0.35 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| a040_s42_fp32 | 0.40 | 4 | 0 | 1 | **+1** | 0 | 0 | 0 |
| a045_s42_fp32 | 0.45 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| a050_s42_fp32 | 0.50 | 3 | 5 | 6 | **+1** | 2 | 3 | **+1** |
| a050_s43_fp32 | 0.50 | 0 | 5 | 5 | 0 | 1 | 1 | 0 |
| a050_s44_fp32 | 0.50 | 0 | 3 | 3 | 0 | 0 | 0 | 0 |
| a060_s43_fp32 | 0.60 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| a075_s42_fp32 | 0.75 | 3 | 6 | 6 | 0 | 0 | 3 | **+3** |
| c4_a025_s42_fp32 | 0.25 | 4 | 0 | 3 | **+3** | 0 | 0 | 0 |
| c4_a050_s42_fp32 | 0.50 | 2 | 4 | 6 | **+2** | 0 | 0 | 0 |
| c4_a075_s42_fp32 | 0.75 | 3 | 8 | 8 | 0 | 0 | 3 | **+3** |

## Summary Statistics

### TY Distribution (fixed)
- TY=0/8: 4 experiments (a010_s42, a025_s44, a050_s43, a050_s44)
- TY=1/8: 4 experiments (a025_s43, a035, a045, a060_s43)
- TY=2/8: 2 experiments (a025_s42, c4_a050)
- TY=3/8: 5 experiments (a010_s43, a030, a050_s42, a075, c4_a075)
- TY=4/8: 2 experiments (a040, c4_a025)
- **Non-zero TY: 13/17 experiments (76%)**

### K≥3 Changes
- K≥3 increased in **6/17 experiments** due to TY fix
- WikiText: a030 (+1), a040 (+1), a050_s42 (+1)
- C4: c4_a025 (+3), c4_a050 (+2)
- No experiment had K≥3 decrease (TY only adds votes)

### K≥4 Changes
- K≥4 increased in **4/17 experiments**
- a010_s43 (+1), a050_s42 (+1), a075 (+3), c4_a075 (+3)

### Dose-Response Pattern

The overall dose-response pattern is **preserved** after TY fix:
- α≤0.25: K≥3 remains 0/8 in most WikiText experiments (weak signal)
- α=0.50: K≥3 = 3–6/8 across seeds (strong signal, seed-dependent)
- α=0.75: K≥3 = 6–8/8 (very strong signal)
- C4 shows stronger signal at lower α (c4_a025 now K≥3=3/8 with TY contribution)

**TY fix does not alter the qualitative dose-response conclusion.** It modestly strengthens consensus at medium-to-high α and provides substantial lift in C4 experiments where other methods had borderline agreement.

### Seed Variability in TY
TY shows notable seed variability (consistent with C003 constraint for low α):
- α=0.10: seed 42→TY=0, seed 43→TY=3
- α=0.25: seed 42→TY=2, seed 43→TY=1, seed 44→TY=0
- α=0.50: seed 42→TY=3, seed 43→TY=0, seed 44→TY=0

This confirms TY is useful as a consensus contributor but unreliable as a standalone measure, especially at low α.
