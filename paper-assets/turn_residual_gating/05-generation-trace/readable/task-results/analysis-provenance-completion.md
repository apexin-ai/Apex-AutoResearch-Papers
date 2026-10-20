# analysis provenance completion

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_provenance_completion_20260522T042945_result.json`
- **Structured JSON:** [`56dc3c7a76180598f8ac.json`](../../sessions/56/56dc3c7a76180598f8ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

29 non-deprecated items in the file. The checker counts 27 (likely excluding C050 positioning + C056 limitation as non-empirical). Of 27, 24 are now tier2, 3 remain tier3. These 3 are likely items where the metric-level mapping can't be automatically verified.

**Summary:**

**Provenance coverage: 22/27 → 24/27** (+2)

What was done:
1. **Fixed 6 claims** (C019, C021, C024, C028, C033, C039) — replaced placeholder `exp_007`/`exp_008` with actual experiment IDs:
   - `exp_007` → `analysis_gradient_conflict` (gradient conflict data)
   - `exp_007` → `phase2_tg_s42_v7` (gate conditioning, inference gate values, TF/AR GAR gap)
   - `exp_008` → `phase2_tg_s42_v9_pcgrad` (PCGrad experiment)

2. **Fixed 1 table + 2 figures** — updated `tab:grad-conflict`, `fig_gate_shift`, `fig_training_pcgrad` references

3. **Added evidence** to C050 (positioning) and C056 (limitation) — previously had empty evidence arrays

4. **Cleaned up** deprecated test entries (C017, C018, deprecated table/figure duplicates)

5. **Filled registry spec** for `phase2_tg_s42` (added data_path, data_count, model_name, seed, checkpoint_path) and `phase2_tg_s42_v6` (added command, server, data_path, data_count, model_name, seed)

Remaining 3 tier3 items likely require exact metric-name matching that goes beyond ID-level provenance tracing.

---
