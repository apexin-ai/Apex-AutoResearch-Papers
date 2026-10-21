# audit tex number consistency

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tex_number_consistency_20260521T181547_result.json`
- **Structured JSON:** [`b827f60797c4706c16c9.json`](../../sessions/b8/b827f60797c4706c16c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Found the provenance. The 147× was manually changed from 150× in a review-fix commit, but neither matches the actual ratio. Now I have all the data needed for the final report.

---

## Cross-Check Report: Paper Numbers vs Source JSON

### Check 1: MAPE Numbers
**Source**: `artifacts/theory_empirical_mape.json`

| Number | Paper | Source JSON | Status |
|--------|-------|-------------|--------|
| Grand MAPE | 2.0% | 1.997% (→2.00%) | ✅ |
| Confounding MAPE | 0.5% | 0.49% | ✅ |
| IV MAPE | 5.5% | 5.51% | ✅ |
| Per-topology values (7) | all match | all match | ✅ |

**Result**: All MAPE numbers consistent.

---

### Check 2: plan006 ASV / Empirical Numbers
**Source**: `artifacts/plan006_full_filtered_stats.json`, `artifacts/plan006/asv_empirical_results.json`

| Number | Paper | Source JSON | Status |
|--------|-------|-------------|--------|
| 126 scenarios, 18 configs | ✅ | ✅ | ✅ |
| HumAID IV bias range | 12.4–42.1% | 12.4–42.1% | ✅ |
| HumAID exposure range | 9.0–17.4% | 9.0–17.4% | ✅ |
| HumAID med+frontdoor | 10.7–14.8% | med 10.8–14.8%, fd 10.7–14.7% (combined = 10.7–14.8%) | ✅ |
| HumAID collider | 4.1–5.6% | 4.1–5.6% | ✅ |
| HumAID confounding | 4.9–6.2% | 4.9–6.2% | ✅ |
| HumAID M-bias | 5.1–6.5% | 5.1–6.5% | ✅ |
| HumAID mean / IV bias | 12.2% / 30.3% | 12.2% / 30.3% | ✅ |
| CivilComments IV bias | 116.5% | 116.5% | ✅ |
| CivilComments 21/21 ASV-unsafe | 21/21 | 21/21 | ✅ |
| Zero sign flips (98 scenarios) | 0 | 0 | ✅ |
| 7B-to-235B ratio | 1.24 | 1.2403 | ✅ |
| K=10 ASV ranges (IV) | 0.31–0.83 | 0.31–0.83 | ✅ |
| K=10 ASV ranges (med) | 0.62–0.90 | 0.62–0.90 | ✅ |
| K=10 ASV ranges (frontdoor) | 0.62–0.91 | 0.62–0.91 | ✅ |
| K=10 ASV ranges (exposure) | 0.65–1.11 | 0.65–1.11 | ✅ |
| **VAST mean bias** | **65.3%** | **65.36%** → should round to **65.4%** | ❌ minor |
| **VAST IV bias** | **252.3%** | **252.63%** → should round to **252.6%** | ❌ minor |
| **CivilComments mean bias** | **36.9%** | **36.98%** → should round to **37.0%** | ❌ minor |
| **K=10 ASV-unsafe count** | **31/56 (55.4%)** | **JSON field says 32/56** | ❌ see note |

**Note on 31/56 vs 32/56**: The JSON `asv_unsafe_magnitude` counts all scenarios where bias exceeds the threshold (32). The paper counts scenarios where ASV < 1.0 (31), excluding one exposure config with ASV=1.1136 that is above-threshold but not actually "unsafe." **The paper's 31 is conceptually correct**, but it mismatches the JSON field value. The JSON field label is misleading.

---

### Check 3: plan008 Binarization Numbers
**Source**: `artifacts/plan008_binarization_collapse/report/plan_008_binarization_collapse.py` (no JSON output file exists)

| Number | Paper | Derivation | Status |
|--------|-------|------------|--------|
| **147×** | **147×** | **0.926/0.006 = 154.3×** | **❌ WRONG** |
| Δ̄ = 0.006 (M-bias) | 0.006 | from script (unverifiable) | ⚠️ |
| Δ̄ = 0.926 (IV) | 0.926 | from script (unverifiable) | ⚠️ |
| 14% sign flip (exposure) | 14% | from script | ⚠️ |
| 17.5% sign flip (IV) | 17.5% | from script | ⚠️ |

**The 147× is arithmetically inconsistent with the stated endpoints (0.006 and 0.926).** Git history shows it was changed from 150× to 147× in commit `21f51c4` ("W3 150→147") — both are wrong. The correct ratio is **154.3×** (or ~154×).

---

### Check 4: Correction Method Numbers
**Source**: `artifacts/plan007_rmse_correction_results.json`, `artifacts/ppi_empirical_validation.json`

| Number | Paper | Source JSON | Status |
|--------|-------|-------------|--------|
| PPI++ RMSE reduction | 47.0% | 47.0 | ✅ |
| PPI++ coverage | 96.8% | 96.8 | ✅ |
| PPI++ M-bias harm | -88.0% | -88.0 | ✅ |
| MC-SIMEX grand mean | 13.3% | 13.3 | ✅ |
| MC-SIMEX IV | 59.4% | 59.4 | ✅ |
| MC-SIMEX frontdoor | -62.4% | -62.4 | ✅ |
| MC-SIMEX exposure | -9.8% | -9.8 | ✅ |
| DSL confounding | 48.0% | 48.0 | ✅ |
| DSL mediation | 52.9% | 52.9 | ✅ |
| DSL M-bias | -267% | -266.9 → -267% | ✅ |
| DSL IV | -206% | -206.1 → -206% | ✅ |
| Empirical PPI++ confounding | 85.9% | 85.9% | ✅ |
| Empirical PPI++ frontdoor | 75.1% | 75.1% | ✅ |
| Empirical PPI++ IV | -79.2% | -79.2% | ✅ |
| Empirical MC-SIMEX collider | 66.5% | 66.5% | ✅ |
| Empirical MC-SIMEX M-bias | 56.5% | 56.5% | ✅ |
| Empirical MC-SIMEX exposure | 53.5% | 53.5% | ✅ |
| Empirical MC-SIMEX mediation | 66.4% | 66.4% | ✅ |
| Empirical MC-SIMEX frontdoor K=10 | 70.3% | 70.3% | ✅ |
| PPI++ confounding RMSE (case study) | 83.2% | 83.2 | ✅ |
| MC-SIMEX confounding (case study) | 35.1% | 35.1 | ✅ |

**Result**: All correction numbers perfectly consistent.

---

### Check 5: Other Quantitative Claims
**Source**: Various (Table 1 numbers from Monte Carlo simulation — no JSON artifact found)

| Number | Context | Status |
|--------|---------|--------|
| 83.4% exposure sign reversal | Table 1, abstract, throughout | ⚠️ No JSON source found; internally consistent across paper |
| 52.6% IV sign reversal | Table 1, abstract, throughout | ⚠️ No JSON source found |
| 85% exposure violation | Table 1, experiments.tex | ⚠️ Dirichlet log shows 84.9% (different sampling method) |
| 13.7% violation at diag≥0.7 | experiments.tex, abstract | ✅ matches `mvp_exposure_dirichlet_subspace_output.log` |
| 2.1% sign rev at diag≥0.7 | experiments.tex, abstract | ✅ matches log |
| 11.7% amplif at diag≥0.7 | experiments.tex, abstract | ✅ matches log |
| 11.9% violation at diag≥0.9 | experiments.tex | ✅ matches log |

---

## Summary

| Category | Count |
|----------|-------|
| ❌ **Needs fix** | **1** (147× should be ~154×) |
| ❌ Minor rounding | **3** (VAST 65.3%→65.4%, 252.3%→252.6%, CivilComments 36.9%→37.0%) |
| ❌ JSON mismatch (paper arguably correct) | **1** (31/56 vs 32/56) |
| ⚠️ No JSON source to verify | ~5 (Table 1 simulation numbers, binarization Δ̄ values) |
| ✅ Consistent | **40+** numbers verified |

### Action items:
1. **Fix 147× → ~154×** (or update Δ̄ endpoints to be consistent). This appears in: `experiments.tex:101`, `abstract.tex`, `conclusion.tex`, `introduction.tex`, `appendix_proofs.tex:586`.
2. **Optional**: Fix 3 minor rounding inconsistencies (65.3→65.4, 252.3→252.6, 36.9→37.0).
3. **Optional**: Align JSON `asv_unsafe_magnitude` field with the paper's definition (ASV < 1.0 = 31/56, not just non-null ASV = 32/56).

---
