# D150-P01: D127 Spec Curve & Shapley Values Audit vs D120 Canonical Pipeline

**Date**: 2026-05-20
**Auditor**: Claude (automated)

## D120 Canonical Pipeline Requirements

- Threshold criterion: `true_3sigma_d105` (D105 true 3σ with FDR correction)
- Pairs: 8 canonical — {token_entropy, ece} × {distinct_1, distinct_2, distinct_3, mauve}
- No perplexity
- n_perm: 5000
- Significance: FDR-corrected for diff_xcorr and perm_granger
- Direction filter: D111 corrected (`peak_lag < 0`)

---

## 1. D127 Specification Curve — **PASS**

**Script**: `scripts/d127_spec_curve.py` (ran 2026-05-20 ~09:54 on westd-17855)

| Check | Status | Evidence |
|-------|--------|----------|
| Threshold = true_3sigma_d105 | **PASS** | Line 106: `if criterion != 'true_3sigma_d105': skipped` — hard filter, non-3sigma data excluded by construction |
| 8 canonical pairs | **PASS** | Lines 30-35: exactly {token_entropy, ece} × {distinct_1, distinct_2, distinct_3, mauve} |
| No perplexity | **PASS** | Perplexity not in CANONICAL_PAIRS |
| n_perm = 5000 | **PASS** | Underlying data uses `run_5method_analysis_d102.py` with n_perm=5000 (confirmed in D120 analysis reports) |
| FDR-corrected significance | **PASS** | Lines 41-43: `significant_fdr` used for diff_xcorr and perm_granger |
| Output | 1160 specs, 29 experiments, 536 significant (46.2%) | |

**Note**: The script filters at read time — even if some underlying data files had old criteria, they would be excluded. The 29 included experiments all passed the `true_3sigma_d105` gate.

---

## 2. Shapley Values — **FAIL**

**File**: `artifacts/shapley_values.json` (computed 2026-05-17 09:41 on westd-19828)

| Check | Status | Evidence |
|-------|--------|----------|
| Threshold = true_3sigma_d105 | **FAIL** | Worker log shows underlying data had `"threshold_criterion": "3x_sigma_drift"` (α=0.0 s42). File `a000_s42/analysis/5method_leadlag.json` on 19828 was born 05-17 17:34, replaced AFTER shapley ran at 09:41. Shapley read pre-D105 data. |
| 8 canonical pairs (FPR) | **PASS** | `fpr_data`: 8 pairs/seed × 3 seeds = 24 obs |
| 8 canonical pairs (FNR) | **PARTIAL** | `reference_pairs`: only 6 pairs (excludes mauve). FNR evaluated on {token_entropy, ece} × {distinct_1, distinct_2, distinct_3} only. Deliberate choice due to mauve's low sensitivity, but deviates from full canonical set. |
| n_perm = 5000 | **PASS** | Log confirms `"n_perm": 5000` in data config |
| Coalition count = 32 | **PASS** | `"description": "True Shapley values (2^5=32 coalition enumeration)"`, 5 methods confirmed |
| 5 methods | **PASS** | naive_xcorr, diff_xcorr, threshold_onset, perm_granger, ty_granger |

### Impact of Threshold Mismatch

Per C008: `3x_sigma_drift` is a simple amplitude check; `true_3sigma_d105` is a statistical test with FDR correction. For moderate signals, these diverge significantly (C008 notes 0/8 vs 8/8 in some cases). The threshold_onset Shapley contributions (FPR = -0.065, FNR = -0.210) are computed from wrong underlying decisions.

The other 4 methods (naive_xcorr, diff_xcorr, perm_granger, ty_granger) do NOT depend on threshold_criterion, so their individual Shapley values are likely unaffected. But since Shapley values sum to the difference from grand coalition, changing one method's underlying data shifts all values.

---

## 3. Timeline

| Event | Date | Server |
|-------|------|--------|
| Shapley v2 computed | 2026-05-17 09:41 | westd-19828 (pre-D105 data) |
| Data file a000_s42 replaced | 2026-05-17 17:34 | westd-19828 |
| D127 spec curve run | 2026-05-20 09:54 | westd-17855 |
| D120 full recalculation | 2026-05-20 13:24+ | westd-19828, then westd-17855 (15:15) |

---

## Conclusion

| Component | Verdict |
|-----------|---------|
| D127 Spec Curve | **PASS** — D120-compliant by construction (hard filter on `true_3sigma_d105`) |
| Shapley Values | **FAIL** — computed from pre-D105 data (`3x_sigma_drift` threshold). Must recompute with current D120-compliant data. |

### Required Actions

1. **Recompute shapley_values.json** using current D120-compliant `5method_leadlag.json` files (which now have `true_3sigma_d105` on both servers)
2. **Decision needed**: should FNR reference_pairs include mauve (full 8) or remain at 6? Current exclusion is defensible but should be explicitly documented.
3. **Re-generate shapley bar chart** (`shapley_method_contribution.pdf`) after recompute
