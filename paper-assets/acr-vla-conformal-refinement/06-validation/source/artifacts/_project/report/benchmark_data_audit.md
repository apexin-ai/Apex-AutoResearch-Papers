# Full Benchmark Data Audit
Date: 2026-05-20

## Summary

| Category | Count | Details |
|----------|-------|---------|
| **Perfect matches** | 9/15 | Spatial-CRM, Long-CRM, Long-VLA (10/11), Goal-VLA, Obj-norm02-K10 (6/6), Obj-K5, Obj-VLA, Argmin-K10, Argmin-K5 |
| **Seeds in script but not in DONE+success registry** | 8 | See details below |
| **Seeds in registry but excluded from script** | 1 | Obj-CRM-norm02-K10 seed42 |
| **Value mismatches** | 0 | All common seeds have matching SR values |
| **Registry status anomalies** | 6 | Experiments with data but status ≠ DONE or conclusion ≠ success |

### Seeds in Script Not in DONE+success Registry

| Benchmark | Method | Seed | Script SR | Registry Status | Notes |
|-----------|--------|------|-----------|-----------------|-------|
| Spatial | VLA-only | 48 | 0.30 | DONE/failed | Director directive; data exists outside registry |
| Spatial | VLA-only | 49 | 0.29 | DONE/failed | Director directive; data exists outside registry |
| Spatial | VLA-only | 50 | 0.30 | PREPARING/success | SR=0.30 in registry but status not DONE |
| Long | VLA-only | 49 | 0.16 | PREPARING/None | No SR in registry; Director directive |
| Goal | CRM obs_only | 47 | 0.69 | PREPARING/None | SR=0.69 in registry metrics but status PREPARING |
| Object | CRM norm01 | 42 | 0.19 | DEPLOYED/success | SR=0.19 in registry but status DEPLOYED, not DONE |
| Object | Adaptive-K p50 | 42,43 | 0.16,0.16 | ALLOCATED/success | SR matches; status should be DONE |
| Object | Adaptive-K p75 | 42,43 | 0.12,0.13 | ALLOCATED/success | SR matches; status should be DONE |

---

## Per-Benchmark Details

### LIBERO-Spatial

#### CRM obs_only norm02 K=10
**Script**: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 51]
- values: {42: 0.35, 43: 0.34, 44: 0.36, 45: 0.34, 46: 0.33, 47: 0.32, 48: 0.35, 51: 0.36}

**Registry** (all DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-mag-obsonly-norm02 | 42 | 0.35 |
| eval-obs-only-spatial-norm02-seed43-r2 | 43 | 0.34 |
| eval-obs-only-spatial-norm02-seed44 | 44 | 0.36 |
| eval-obs-only-spatial-norm02-seed45 | 45 | 0.34 |
| eval-obs-only-spatial-norm02-seed46-r2 | 46 | 0.33 |
| eval-obs-only-spatial-norm02-seed47 | 47 | 0.32 |
| eval-obs-only-spatial-norm02-seed48 | 48 | 0.35 |
| eval-crm-spatial-k10-seed51 | 51 | 0.36 |

**Diff**: MATCH — all 8 seeds present with correct values.
- Note: eval-mag-obsonly-norm02 has `conclusion=negative` (not `success`), but SR=0.35 is valid data. Script correctly uses it.

#### VLA-only
**Script**: n=9, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50]
- values: {42: 0.30, 43: 0.29, 44: 0.31, 45: 0.27, 46: 0.30, 47: 0.30, 48: 0.30, 49: 0.29, 50: 0.30}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-vla-only-spatial-seed42 | 42 | 0.30 |
| eval-vla-only-spatial-seed43 | 43 | 0.29 |
| eval-vla-only-spatial-seed44 | 44 | 0.31 |
| eval-vla-only-spatial-seed45 | 45 | 0.27 |
| eval-vla-only-spatial-seed46 | 46 | 0.30 |
| eval-vla-only-spatial-seed47 | 47 | 0.30 |

**Diff**:
- **MISSING from DONE+success registry**: seeds 48, 49, 50
  - seed48: `eval-vla-only-spatial-seed48` status=DONE, conclusion=**failed** (no valid SR)
  - seed49: `eval-vla-only-spatial-seed49` status=DONE, conclusion=**failed** (no valid SR)
  - seed50: `eval-vla-only-spatial-seed50` status=**PREPARING**, conclusion=success, SR=0.30
- Script verification notes state: "VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive"
- **Risk**: Seeds 48/49 have no verifiable SR in registry. Data likely from external source (server JSON).

---

### LIBERO-Long

#### CRM obs_only
**Script**: n=7, seeds=[42, 43, 44, 45, 46, 47, 50]
- values: {42: 0.17, 43: 0.15, 44: 0.20, 45: 0.18, 46: 0.18, 47: 0.17, 50: 0.14}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-crm-long-seed42 | 42 | 0.17 |
| eval-crm-long-seed43 | 43 | 0.15 |
| eval-crm-long-seed44 | 44 | 0.20 |
| eval-crm-long-seed45 | 45 | 0.18 |
| eval-crm-long-seed46 | 46 | 0.18 |
| eval-crm-long-seed47 | 47 | 0.17 |
| eval-crm-long-seed50 | 50 | 0.14 |

**Diff**: PERFECT MATCH — all 7 seeds present with correct values.

#### VLA-only
**Script**: n=11, seeds=[42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
- values: {42: 0.11, 43: 0.13, 44: 0.12, 45: 0.17, 46: 0.18, 47: 0.14, 48: 0.14, 49: 0.16, 50: 0.16, 51: 0.15, 52: 0.17}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-vla-only-long-seed42 | 42 | 0.11 |
| eval-vla-only-long-seed43 | 43 | 0.13 |
| eval-vla-only-long-seed44 | 44 | 0.12 |
| eval-vla-only-long-seed45 | 45 | 0.17 |
| eval-vla-only-long-seed46 | 46 | 0.18 |
| eval-vla-only-long-seed47 | 47 | 0.14 |
| eval-vla-only-long-seed48 | 48 | 0.14 |
| eval-vla-only-long-seed50 | 50 | 0.16 |
| eval-vla-only-long-seed51 | 51 | 0.15 |
| eval-vla-only-long-seed52 | 52 | 0.17 |

**Diff**:
- **MISSING from registry**: seed 49
  - `eval-vla-only-long-seed49`: status=**PREPARING**, conclusion=None, SR=None
- Script includes seed49=0.16. Data source unclear — no SR in registry, experiment never completed.
- **Risk**: Unverifiable data point. Should be removed or re-run.

---

### LIBERO-Goal

#### CRM obs_only
**Script**: n=6, seeds=[42, 43, 44, 45, 46, 47]
- values: {42: 0.67, 43: 0.72, 44: 0.64, 45: 0.65, 46: 0.72, 47: 0.69}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-crm-goal-seed42 | 42 | 0.67 |
| eval-crm-goal-seed43 | 43 | 0.72 |
| eval-crm-goal-seed44-r2 | 44 | 0.64 |
| eval-crm-goal-seed45-r2 | 45 | 0.65 |
| eval-crm-goal-seed46 | 46 | 0.72 |

**Diff**:
- **MISSING from DONE+success registry**: seed 47
  - `eval-crm-goal-seed47`: status=**PREPARING**, conclusion=None, SR=0.69 (in metrics)
- Script verification notes: "CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry)."
- SR value 0.69 exists in registry metrics despite PREPARING status. Likely manually populated.
- **Action**: Update registry status to DONE+success when experiment completes, or verify data source.

#### VLA-only
**Script**: n=6, seeds=[42, 43, 44, 45, 46, 49]
- values: {42: 0.71, 43: 0.69, 44: 0.73, 45: 0.63, 46: 0.71, 49: 0.65}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-vla-only-goal-seed42 | 42 | 0.71 |
| eval-vla-only-goal-seed43 | 43 | 0.69 |
| eval-vla-only-goal-seed44-r2 | 44 | 0.73 |
| eval-vla-only-goal-seed45 | 45 | 0.63 |
| eval-vla-only-goal-seed46 | 46 | 0.71 |
| eval-vla-only-goal-seed49 | 49 | 0.65 |

**Diff**: PERFECT MATCH — all 6 seeds present with correct values.

---

### LIBERO-Object

#### CRM obs_only norm02 K=10 (PRIMARY)
**Script**: n=6, seeds=[43, 44, 45, 46, 47, 48]
- values: {43: 0.16, 44: 0.16, 45: 0.16, 46: 0.15, 47: 0.20, 48: 0.18}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-acr-object-obs-only-norm02 | 42 | 0.22 |
| eval-obs-only-object-norm02-seed43-r2 | 43 | 0.16 |
| eval-obs-only-object-norm02-seed44-r2 | 44 | 0.16 |
| eval-obs-only-object-norm02-seed45 | 45 | 0.16 |
| eval-obs-only-object-norm02-seed46 | 46 | 0.15 |
| eval-obs-only-object-norm02-seed47 | 47 | 0.20 |
| eval-obs-only-object-norm02-seed48-r2 | 48 | 0.18 |

**Diff**:
- **In registry but NOT in script**: seed 42 (SR=0.22)
  - `eval-acr-object-obs-only-norm02`: early experiment, SR=0.22 is a significant outlier vs seeds 43-48 range (0.15-0.20)
  - Likely excluded due to different eval setup (earlier code version, possibly different n_rollouts)
  - **Decision**: Exclusion is reasonable if eval config differs. Should be documented.

#### CRM obs_only norm01 (Supplementary)
**Script**: n=6, seeds=[42, 44, 45, 46, 47, 48]
- values: {42: 0.19, 44: 0.16, 45: 0.17, 46: 0.18, 47: 0.17, 48: 0.18}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-obs-only-object-norm01-seed44 | 44 | 0.16 |
| eval-obs-only-object-norm01-seed45-r2 | 45 | 0.17 |
| eval-obs-only-object-norm01-seed46-r3 | 46 | 0.18 |
| eval-obs-only-object-norm01-seed47 | 47 | 0.17 |
| eval-obs-only-object-norm01-seed48 | 48 | 0.18 |

**Diff**:
- **MISSING from DONE+success registry**: seed 42
  - `eval-obs-only-object-norm01-seed42`: status=**DEPLOYED** (not DONE), conclusion=success, SR=0.19
  - `eval-obs-only-object-norm01-seed42-r2`: status=DONE, conclusion=**failed**
- Script uses seed42=0.19 from the DEPLOYED experiment.
- **Action**: Update `eval-obs-only-object-norm01-seed42` status to DONE.
- Note: seed45 has two entries (original SR=0.14, r2 SR=0.17). Script correctly uses r2=0.17.

#### CRM obs_only norm02 K=5 (Supplementary)
**Script**: n=7, seeds=[42, 43, 44, 45, 46, 47, 48]
- values: {42: 0.14, 43: 0.19, 44: 0.17, 45: 0.15, 46: 0.16, 47: 0.13, 48: 0.18}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-obs-only-object-norm02-k5-seed42 | 42 | 0.14 |
| eval-obs-only-object-norm02-k5-seed43 | 43 | 0.19 |
| eval-obs-only-object-norm02-k5-seed44 | 44 | 0.17 |
| eval-obs-only-object-norm02-k5-seed45 | 45 | 0.15 |
| eval-obs-only-object-norm02-k5-seed46 | 46 | 0.16 |
| eval-obs-only-object-norm02-k5-seed47 | 47 | 0.13 |
| eval-obs-only-object-norm02-k5-seed48 | 48 | 0.18 |

**Diff**: PERFECT MATCH — all 7 seeds present with correct values.

#### VLA-only
**Script**: n=8, seeds=[42, 43, 44, 45, 46, 47, 48, 50]
- values: {42: 0.12, 43: 0.12, 44: 0.10, 45: 0.11, 46: 0.13, 47: 0.10, 48: 0.10, 50: 0.09}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-vla-only-object (seed42) | 42 | 0.12 |
| eval-vla-only-object-seed43 | 43 | 0.12 |
| eval-vla-only-object-seed44-r2 | 44 | 0.10 |
| eval-vla-only-object-seed45-r2 | 45 | 0.11 |
| eval-vla-only-object-seed46 | 46 | 0.13 |
| eval-vla-only-object-seed47 | 47 | 0.10 |
| eval-vla-only-object-seed48 | 48 | 0.10 |
| eval-vla-only-object-seed50 | 50 | 0.09 |

**Diff**: PERFECT MATCH — all 8 seeds present with correct values.
- Note: `eval-openvla-object-vla-only-seed42-v2` (SR=0.69) is OpenVLA (different model), correctly excluded.
- Note: seed45 has r1=0.09, r2=0.11. Script correctly uses r2.

#### Argmin K=10
**Script**: n=5, seeds=[43, 44, 45, 46, 47]
- values: {43: 0.17, 44: 0.13, 45: 0.12, 46: 0.10, 47: 0.10}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-argmin-object-seed43 | 43 | 0.17 |
| eval-argmin-object-seed44-r2 | 44 | 0.13 |
| eval-argmin-object-seed45 | 45 | 0.12 |
| eval-argmin-object-seed46 | 46 | 0.10 |
| eval-argmin-object-seed47 | 47 | 0.10 |

**Diff**: PERFECT MATCH — all 5 seeds present with correct values.
- Note: seed43=0.17 is a severe outlier (others 0.10-0.13). Script verification notes flag this as unverifiable (JSON not found on any server).

#### Argmin K=5
**Script**: n=4, seeds=[42, 43, 44, 45]
- values: {42: 0.15, 43: 0.13, 44: 0.11, 45: 0.13}

**Registry** (DONE+success):

| exp_id | seed | SR |
|--------|------|----|
| eval-argmin-object-k5-seed42 | 42 | 0.15 |
| eval-argmin-object-k5-seed43 | 43 | 0.13 |
| eval-argmin-object-k5-seed44-r2 | 44 | 0.11 |
| eval-argmin-object-k5-seed45 | 45 | 0.13 |

**Diff**: PERFECT MATCH — all 4 seeds present with correct values.

#### Adaptive-K
**Script**: 4 thresholds × 3 seeds each (seeds 42, 43, 44)

| Threshold | seed42 | seed43 | seed44 |
|-----------|--------|--------|--------|
| p25 | 0.15 | 0.13 | 0.15 |
| p50 | 0.16 | 0.16 | 0.14 |
| p75 | 0.12 | 0.13 | 0.16 |
| p90 | 0.12 | 0.14 | 0.14 |

**Registry** (DONE+success only):

| Threshold | Registry Seeds (DONE+success) | Missing |
|-----------|-------------------------------|---------|
| p25 | 42 ✓, 43 ✓, 44 ✓ | — |
| p50 | 44 ✓ | **42, 43** |
| p75 | 44 ✓ | **42, 43** |
| p90 | 42 ✓, 43 ✓, 44 ✓ | — |

**Diff**:
- p25, p90: PERFECT MATCH
- p50 seed42/43: `eval-adaptive-k-p50-seed42` and `eval-adaptive-k-p50-seed43` have status=**ALLOCATED** (not DONE), but conclusion=success and SR values match script exactly (0.16, 0.16)
- p75 seed42/43: `eval-adaptive-k-p75-seed42` and `eval-adaptive-k-p75-seed43` have status=**ALLOCATED** (not DONE), but conclusion=success and SR values match script exactly (0.12, 0.13)
- **Action**: Update these 4 experiments' status from ALLOCATED → DONE.

---

## Registry Status Anomalies

Experiments with valid data but incorrect status:

| exp_id | Current Status | Should Be | SR |
|--------|---------------|-----------|-----|
| eval-adaptive-k-p50-seed42 | ALLOCATED | DONE | 0.16 |
| eval-adaptive-k-p50-seed43 | ALLOCATED | DONE | 0.16 |
| eval-adaptive-k-p75-seed42 | ALLOCATED | DONE | 0.12 |
| eval-adaptive-k-p75-seed43 | ALLOCATED | DONE | 0.13 |
| eval-obs-only-object-norm01-seed42 | DEPLOYED | DONE | 0.19 |
| eval-vla-only-spatial-seed50 | PREPARING | DONE | 0.30 |
| eval-crm-goal-seed47 | PREPARING | DONE (if verified) | 0.69 |

---

## Recommended Actions

### High Priority (data integrity)
1. **VLA-Long seed49** (SR=0.16): No registry data, no verifiable source. Either re-run the experiment or remove from script.
2. **VLA-Spatial seeds 48/49**: Registry shows conclusion=failed. Verify the Director-provided values (0.30, 0.29) against server JSON. If unverifiable, remove.

### Medium Priority (registry hygiene)
3. **Fix 4 Adaptive-K statuses**: ALLOCATED → DONE for p50-seed42, p50-seed43, p75-seed42, p75-seed43.
4. **Fix norm01-seed42 status**: DEPLOYED → DONE for `eval-obs-only-object-norm01-seed42`.
5. **Fix VLA-Spatial seed50 status**: PREPARING → DONE for `eval-vla-only-spatial-seed50`.
6. **Resolve CRM-Goal seed47**: Either complete the experiment and update status, or document the data source.

### Low Priority (documentation)
7. **Document Object CRM norm02 K=10 seed42 exclusion**: `eval-acr-object-obs-only-norm02` (SR=0.22) is excluded from the primary analysis. Add a comment explaining why (different eval config / outlier).

---

## Appendix: Spatial K=5 Cross-check

The registry also contains Spatial norm02 K=5 experiments (not used in primary analysis):

| exp_id | seed | SR |
|--------|------|----|
| eval-obs-only-spatial-norm02-k5-seed42 | 42 | 0.35 |
| eval-obs-only-spatial-norm02-k5-seed43 | 43 | 0.32 |
| eval-obs-only-spatial-norm02-k5-seed44-r2 | 44 | 0.37 |
| eval-obs-only-spatial-norm02-k5-seed45-r2 | 45 | 0.34 |

These are not included in the statistical script but are available for supplementary analysis if needed.
