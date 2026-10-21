# 5-Phase Pipeline Result Audit — 2026-05-22

## Phase Legend

| Short | File | Phase |
|-------|------|-------|
| R² | `action_r2_probing.json` | Action R² probing |
| L1 | `l1_attention_profile.json` | L1 attention profile |
| CI | `cross_instruction_classification.json` | Cross-instruction classification |
| RSA | `rsa_analysis.json` | RSA analysis |
| CF | `counterfactual_combined.json` | Counterfactual sensitivity |

---

## Completeness Matrix

### OpenVLA (Llama-2-7B backbone)

| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |
|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|
| **Goal** | trained | `libero_goal/` | ✅ | ✅ | ✅ | ✅ | ❌ | **4/5** |
| **Goal** | untrained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |
| **Spatial** | trained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |
| **Spatial** | untrained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |
| **Object** | trained | `libero_object/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |
| **Object** | untrained | `libero_object_untrained/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |
| **Long** | trained | `libero_long/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |
| **Long** | untrained | `libero_long_untrained/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |

### TracVLA (Phi-3-Vision backbone)

| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |
|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|
| **Goal** | trained | `tracvla_goal/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Goal** | untrained | `tracvla_goal/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Spatial** | trained | `tracvla_spatial/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Spatial** | untrained | `tracvla_spatial/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Object** | trained | `tracvla_object/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Object** | untrained | `tracvla_object/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Long** | trained | `tracvla_long/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Long** | untrained | `tracvla_long/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |

### NORA

| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |
|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|
| **Goal** | trained | `nora_goal/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Goal** | untrained | `nora_goal/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Spatial** | trained | `nora_spatial/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |
| **Spatial** | untrained | `nora_spatial/untrained/` | ✅ | ✅ | ✅ | ❌ | ❌ | **3/5** |
| **Object** | trained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |
| **Object** | untrained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |
| **Long** | trained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |
| **Long** | untrained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |

---

## Aggregate Summary

| Metric | Count |
|--------|-------|
| Total cells (3 arch × 4 suite × 2 condition) | **24** |
| Complete (5/5) | **4** — OpenVLA Object (T+U), Long (T+U) |
| Partial (3–4/5) | **13** |
| Empty (0/5) | **7** — OpenVLA Goal-U, Spatial (T+U); NORA Object (T+U), Long (T+U) |
| Total files present | **95 / 120** |
| Total files missing | **25** |

### Missing phases breakdown

| Missing Phase | Affected Cells | Count |
|---------------|----------------|-------|
| **RSA** | All 8 TracVLA + all 4 NORA cells | **12** |
| **CF** | OpenVLA Goal-trained, NORA Spatial-untrained | **2** |
| **All 5 phases** | OpenVLA Goal-U, Spatial-T/U; NORA Object-T/U, Long-T/U | **7 cells × 5 = 35 missing files** |

---

## Registry Cross-Check

### Registry DONE/success but server files incomplete

| exp_id | Registry Status | Issue on Server |
|--------|----------------|-----------------|
| `nora_spatial_pipeline_v2` | DONE / success | `nora_spatial/untrained/` missing CF (3/5 not 5/5) |

### Server has results but no corresponding single registry entry

The following directories have complete/near-complete results assembled from multiple legacy experiments rather than a single pipeline run:
- `libero_goal/` — 4/5 files from multiple older experiments (no single "openvla_goal" registry entry with conclusion=success)
- `libero_object/` + `libero_object_untrained/` — assembled across `object_pipeline_ridge_v2`, `object_untrained_pipeline_v1`, etc.
- `libero_long/` + `libero_long_untrained/` — assembled from `openvla_long_pipeline_v1` (failed) + `openvla_long_cf_trained` (success) + `openvla_long_untrained_v1` (success)

### In-progress experiments filling gaps

| exp_id | Status | Target Gaps |
|--------|--------|-------------|
| `openvla_goal_standardized_v1` | **RUNNING** | OpenVLA Goal trained + untrained (all 5 phases) |
| `openvla_spatial_standardized_v1` | **PREPARING** | OpenVLA Spatial trained + untrained (all 5 phases) |
| `cf_batch_missing_v1` | **RUNNING** | Untrained CF for multiple cells (openvla object untrained, tracvla spatial/object/goal/long untrained) |

---

## Legacy / Non-Standard Data

These directories contain related data in older formats, **not** in the standardized 5-phase structure:

| Directory | Contents | Notes |
|-----------|----------|-------|
| `cross_instruction_spatial/` | `classification_results.json` | OpenVLA Spatial CI (legacy format) |
| `counterfactual_spatial/` | 6 files (per-condition + combined) | OpenVLA Spatial CF (legacy format) |
| `trained/`, `untrained/` (top-level) | `action_delta/`, `action_prediction/`, `temporal_distance/` | Old probe format (pre-standardization) |
| `trained_libero_goal/`, `untrained_libero_goal/` | Empty (0 json files) | Abandoned directories |
| `dinov2/`, `dinov2_libero_goal*/`, `oracle/`, etc. | Various old baselines | Control experiments, not part of 3×4 matrix |

---

## Critical Gaps Requiring Action

### Priority 1: Entire cells missing (0/5)
1. **OpenVLA Spatial** (trained + untrained) — `openvla_spatial_standardized_v1` in PREPARING, needs to start
2. **NORA Object** (trained + untrained) — no experiment registered
3. **NORA Long** (trained + untrained) — no experiment registered

### Priority 2: Phase gaps in otherwise-populated cells
4. **RSA missing across all TracVLA (8 cells) and all NORA (4 cells)** — systematic gap, 12 cells affected
5. **OpenVLA Goal trained** — missing CF only (1 file); `openvla_goal_standardized_v1` RUNNING should fill this
6. **OpenVLA Goal untrained** — `openvla_goal_standardized_v1` RUNNING should create this entire cell
7. **NORA Spatial untrained** — missing CF (registry says success but file absent)
