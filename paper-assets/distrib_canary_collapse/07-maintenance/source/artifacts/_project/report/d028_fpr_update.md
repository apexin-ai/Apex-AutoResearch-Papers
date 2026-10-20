# D028: FPR Ground Truth Update — alpha=0.0 Null Control

**Date**: 2026-05-15
**Status**: Complete
**Motivation**: Reviewer Phase 2 found differenced_xcorr has 50% sig rate at alpha=0.0, invalidating it as FPR ground truth.

---

## 1. alpha=0.0 Null Control FPR (Key Figure)

At alpha=0.0 (no canary injection), any significance is by definition a false positive.

| Method | FPR_p_raw | Sig/Total | FPR_p_fdr (BH) | Sig_fdr/Total |
|--------|:---------:|:---------:|:---------------:|:-------------:|
| naive | **100%** | 8/8 | **100%** | 8/8 |
| differenced | **50%** | 4/8 | **37.5%** | 3/8 |
| threshold | **62.5%** | 5/8 | **62.5%** | 5/8 |
| permutation_granger | **0%** | 0/8 | **0%** | 0/8 |
| TY | **0%** | 0/8 | **0%** | 0/8 |

**Key takeaway**: Only permG and TY have 0% FPR under null. naive/differenced/threshold all produce false positives under no-signal conditions, confirming they are unreliable as standalone tests.

**FDR note**: threshold has no p-values (non-statistical onset test), so BH correction is not applicable. For differenced, BH drops 1 marginal case (p=0.0447 -> adjusted above 0.05).

### Per-pair detail at alpha=0.0

| Pair | naive_p | diff_p | thresh | permG_p | TY_p |
|------|---------|--------|--------|---------|------|
| token_entropy->distinct_1 | 0.0025 | 0.0002 | sig | 0.059 | 0.892 |
| token_entropy->distinct_2 | 0.0061 | 0.0033 | sig | 0.094 | 0.858 |
| token_entropy->distinct_3 | 0.0073 | 0.0447 | sig | 0.081 | 0.971 |
| token_entropy->perplexity | 0.0000 | 0.0000 | sig | 0.670 | 0.314 |
| ece->distinct_1 | 0.0053 | 0.0514 | sig | 0.955 | 0.094 |
| ece->distinct_2 | 0.0097 | 0.1928 | non-sig | 0.549 | 0.093 |
| ece->distinct_3 | 0.0224 | 0.2027 | non-sig | 0.351 | 0.103 |
| ece->perplexity | 0.0188 | 0.0960 | non-sig | 0.366 | 0.801 |

---

## 2. Consensus FPR/FNR (differenced ground truth — deprecated)

This table uses the **old** differenced_xcorr ground truth from MVP 4-seed data. Retained for reference but **superseded** by the null control FPR in Section 1.

| Method | FPR (diff GT) | FNR (consensus GT) |
|--------|:---:|:---:|
| naive_pearson | 100.0% | 0.0% |
| differenced_xcorr | 0.0% | 0.0% |
| threshold_onset | 9.1% | 0.0% |
| toda_yamamoto | 0.0% | 25.0% |
| permutation_granger | 0.0% | 4.2% |
| consensus (>=4/5) | 0.0% | 0.0% |

**Before/After**: The old table used differenced as FPR ground truth (N_neg=11 seeds). The new null control FPR (Section 1) is the correct FPR estimate.

---

## 3. LOO FPR/FNR (supplementary)

Leave-one-out consensus ground truth (K-2 of remaining K-1 methods):

| Method | FPR_loo | FNR_loo | FP | FN | N_pos | N_neg | LOO_robust |
|--------|:------:|:------:|:--:|:--:|:-----:|:-----:|:----------:|
| naive_pearson | 97.5% | 0.0% | 39 | 0 | 24 | 40 | 6 |
| differenced_xcorr | 72.5% | 0.0% | 29 | 0 | 24 | 40 | 6 |
| threshold_onset | 27.5% | 0.0% | 11 | 0 | 24 | 40 | 6 |
| toda_yamamoto | 18.8% | 43.8% | 6 | 14 | 32 | 32 | 8 |
| permutation_granger | 12.5% | 28.1% | 4 | 9 | 32 | 32 | 8 |

---

## 4. Phase 2 FDR-Corrected Sig Rates

Per-(alpha, method) BH FDR correction applied to Phase 2 panel data.

### Before (raw p < 0.05)

| Method | alpha=0.0 | alpha=0.25 | alpha=0.5 | alpha=1.0 |
|--------|:---------:|:----------:|:---------:|:---------:|
| naive | 100% (8/8) | 100% (8/8) | 100% (8/8) | 100% (32/32) |
| differenced | 50% (4/8) | 25% (2/8) | 100% (8/8) | 100% (32/32) |
| threshold | 62% (5/8) | 38% (3/8) | 100% (8/8) | 100% (32/32) |
| permG | 0% (0/8) | **25% (2/8)** | **25% (2/8)** | 75% (24/32) |
| TY | 0% (0/8) | **62% (5/8)** | 0% (0/8) | 59% (19/32) |

### After (BH FDR-corrected)

| Method | alpha=0.0 | alpha=0.25 | alpha=0.5 | alpha=1.0 |
|--------|:---------:|:----------:|:---------:|:---------:|
| naive | 100% (8/8) | 100% (8/8) | 100% (8/8) | 100% (32/32) |
| differenced | **38% (3/8)** | 25% (2/8) | 100% (8/8) | 100% (32/32) |
| threshold | 62% (5/8) | 38% (3/8) | 100% (8/8) | 100% (32/32) |
| permG | 0% (0/8) | **0% (0/8)** | **0% (0/8)** | 75% (24/32) |
| TY | 0% (0/8) | **38% (3/8)** | 0% (0/8) | 59% (19/32) |

### Key changes from FDR correction

1. **permG at alpha=0.25 and 0.5**: 25% -> **0%**. Both raw-significant p-values were marginal and killed by BH. This strengthens permG's specificity profile.
2. **TY at alpha=0.25**: 62% -> **38%**. Two of 5 significant results did not survive BH. (**C001 constraint**: TY non-monotonicity across alpha is still artifact-suspect, single seed, do NOT cite in paper.)
3. **differenced at alpha=0.0**: 50% -> **38%**. One marginal case (p=0.0447) dropped.

---

## 5. Code Changes

### consensus_framework.py

- `compute_fpr_fnr()` renamed to `compute_fpr_fnr_diff()` (deprecated differenced ground truth)
- **New functions added**:
  - `_bh_fdr(pvals, alpha=0.05)` — Benjamini-Hochberg FDR correction
  - `load_null_control_data(phase2_path)` — Load alpha=0.0 records with BH correction
  - `compute_fpr_null_control(phase2_path)` — Compute FPR from null control
  - `compute_phase2_fdr_sig_rates(phase2_path)` — FDR-corrected Phase 2 sig rates
- **Constants**: `PHASE2_METHOD_MAP`, `PHASE2_METHODS`
- File grew from 494 to 644 lines

### Generated artifacts (on server)

- `results/analysis/d028_fpr_null_control.json` — Full FPR analysis
- `results/analysis/d028_fpr_null_control_full.json` — Comprehensive output with Phase 2 FDR rates

---

## 6. Preserved Key Figures

- **Cohen's kappa = 0.185** (from prior analysis, unchanged)
- **alpha=0.0 FPR table** (Section 1) — new key figure for paper
- **C001 constraint active**: TY alpha=0.25 non-monotonicity NOT for paper use

---

## 7. Caveats

- Phase 2 alpha=0.0 data is **single seed (42)**, 8 pairs. FPR estimates have wide confidence intervals.
- threshold_onset is a non-statistical test (no p-value), so FDR correction cannot be applied to it.
- BH FDR was applied per-(alpha, method) family. Pooled BH across all methods at alpha=0.0 gives slightly different results (naive drops from 100% to 75%).
