# D029 FDR Fix Verification Report

**Date**: 2026-05-15 17:55 UTC
**Server**: westd-19828
**Script**: `consensus_framework.py`

## 1. Code Fix Confirmation

`consensus_framework.py` line 85-91 (load_sig_matrix):

```python
if apply_fdr:
    if method == "threshold_onset":
        # Non-statistical test, no FDR version exists
        sig[mi, pi, si] = seed_rec[method].get("significant", False)
    else:
        sig[mi, pi, si] = seed_rec[method].get("significant_fdr", False)
else:
    sig[mi, pi, si] = seed_rec[method].get("significant", False)
```

Logic: `threshold_onset` (non-statistical) reads `significant`; all other methods read `significant_fdr` when FDR is applied.

## 2. Timestamp Comparison

| File | Before rerun | After rerun |
|------|-------------|-------------|
| consensus_framework.py | May 15 17:34 | (unchanged) |
| consensus_classification.json | May 15 17:34 | **May 15 17:55** |
| sensitivity_analysis.json | May 15 17:34 | **May 15 17:55** |
| fpr_fnr_table.json | May 15 17:34 | **May 15 17:55** |

## 3. sig_count_seed Comparison

| Method | Pre-fix (expected) | Post-fix (actual) | Delta |
|--------|-------------------|-------------------|-------|
| naive_pearson | 64 | 63 | -1 |
| differenced_xcorr | 53 | 53 | 0 |
| threshold_onset | 35 | 35 | 0 |
| **toda_yamamoto** | **26** | **24** | **-2** |
| **permutation_granger** | **34** | **27** | **-7** |

- `permutation_granger`: 34 → 27 (matches expected ~27)
- `toda_yamamoto`: 26 → 24 (matches expected ~24)
- `threshold_onset`: unchanged at 35 (correct — uses `significant`, not `significant_fdr`)

## 4. Robust Pairs (6, unchanged)

| # | Pair | Methods agreeing | Status |
|---|------|-----------------|--------|
| 1 | token_entropy→distinct_1 | 5/5 | ROBUST |
| 2 | token_entropy→distinct_2 | 5/5 | ROBUST |
| 3 | token_entropy→distinct_3 | 5/5 | ROBUST |
| 4 | ece→distinct_1 | 4/5 | ROBUST |
| 5 | ece→distinct_2 | 4/5 | ROBUST |
| 6 | ece→distinct_3 | 4/5 | ROBUST |

6 robust pairs confirmed. Composition identical to pre-fix.

## 5. FPR/FNR Table (Post-fix)

| Method | FPR | FNR | sig_count_pair | sig_count_seed |
|--------|-----|-----|----------------|----------------|
| naive_pearson | 100.0% | 0.0% | 16 | 63 |
| differenced_xcorr | 0.0% | 0.0% | 12 | 53 |
| threshold_onset | 9.1% | 0.0% | 9 | 35 |
| toda_yamamoto | 0.0% | 25.0% | 3 | 24 |
| permutation_granger | 0.0% | 4.2% | 6 | 27 |
| **consensus** | **0.0%** | **0.0%** | **6** | — |

Ground truth:
- FPR: differenced_xcorr (seed level), N_neg=11
- FNR: consensus (>=4/5 methods, >=3/4 seeds), N_pos=24

## 6. Verification Status

All checks pass:
- [x] Code fix in place (explicit threshold_onset branch)
- [x] Output timestamps newer than code timestamp
- [x] perm_granger sig_count_seed: 34 → 27
- [x] toda_yamamoto sig_count_seed: 26 → 24
- [x] 6 robust pairs unchanged
- [x] Consensus FPR = 0.0%
- [x] Files synced to local artifacts
