# analysis near chance fix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_near-chance-fix_20260525T094538_result.json`
- **Structured JSON:** [`0ff64ac2ccf96b50b726.json`](../../sessions/0f/0ff64ac2ccf96b50b726.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LaTeX syntax looks correct. Table has the right column count (8 columns for `llcccccc`), all rows have 8 entries.

---

## Summary

### 1. Diagnosis: Fractional logit bug root cause
`GLMResults` in statsmodels **has no `get_robustcov_results` method**. The near_chance script called `gf.get_robustcov_results(cov_type='cluster', groups=cint)` which raised `AttributeError`, silently caught by `except Exception`, appending 1.0 for every condition. The V2 script correctly uses `model.fit(cov_type='cluster', cov_kwds={'groups': groups})` to re-fit with clustered SE.

### 2. Fix applied and verified
Replaced the broken `get_robustcov_results` approach with V2's `model.fit(cov_type='cluster')` approach. Re-ran full sensitivity analysis (560s). Results:

### 3. Complete K3/K5/K7 comparison

**K=3:**
| Metric | Full (455) | Filtered (286) | Δ |
|--------|-----------|----------------|---|
| OLS K_eff | 11/12 | 12/12 | +1 |
| WCB K_eff | 3/12 | 4/12 | +1 |
| Frac K_eff | 8/12 | 9/12 | +1 |
| WCB η_max | 4/12 | 1/12 | -3 |
| β_std | 0.349 | 0.480 | +0.131 |
| R² | 0.340 | 0.333 | -0.007 |

**K=5:**
| Metric | Full (3003) | Filtered (1287) | Δ |
|--------|------------|-----------------|---|
| OLS K_eff | 12/12 | 11/12 | -1 |
| WCB K_eff | 7/12 | 7/12 | 0 |
| Frac K_eff | 10/12 | 11/12 | +1 |
| WCB η_max | 2/12 | 0/12 | -2 |
| β_std | 0.437 | 0.512 | +0.075 |
| R² | 0.285 | 0.256 | -0.028 |

**K=7:**
| Metric | Full (6435) | Filtered (1716) | Δ |
|--------|------------|-----------------|---|
| OLS K_eff | 12/12 | 11/12 | -1 |
| WCB K_eff | 8/12 | 2/12 | -6 |
| Frac K_eff | 10/12 | 11/12 | +1 |
| WCB η_max | 1/12 | 0/12 | -1 |
| β_std | 0.401 | 0.385 | -0.016 |
| R² | 0.244 | 0.203 | -0.041 |

### 4. Appendix updated
- Added "Frac" column to table with all 6 data points
- Added sentence about frac logit improving after filtering at every K
- Added η_max paragraph showing WCB η drops from 4→1, 2→0, 1→0 — near-chance models drive η_max significance
- Revised conclusion: K_eff robust at all K, η_max is not

---
