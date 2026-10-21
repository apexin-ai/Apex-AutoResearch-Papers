# check d134 s51 and original seeds

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-s51-and-original-seeds_20260518T154305_result.json`
- **Structured JSON:** [`5a90425c15277da09b55.json`](../../sessions/5a/5a90425c15277da09b55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are the results:

---

## s51 ISR Status

```
Step: 45/500
GPU: 87% util, 84793 MiB used
ETA: ~1h50m
Latest rewards: step43=0.386, step44=0.129, step45=0.000 (sporadic signal, still early)
classify.json already exists (from pipeline pre-run, keys: n_total/n_proved/h7*/h1*)
```

Training is running normally at step 45/500.

---

## Original Seeds Audit

| Condition | Seed | Dir Found | Classify/Taxonomy File | Format | Keys | Compatible w/ C013 |
|-----------|------|-----------|----------------------|--------|------|-------------------|
| **ISR** | s42 | N (files only) | `plan002_..._s42_taxonomy_unified.json` | taxonomy_unified | proved/H7/H1_exact/H1_near/H8/genuine | **YES** (C013 standard) |
| ISR | s42 | N | `plan002_..._s42_1000_taxonomy_unified.json` | taxonomy_unified | same as above | **YES** (1000-step variant) |
| ISR | s43 | **N** | **None** | — | — | **MISSING** |
| ISR | s44 | **N** | **None** | — | — | **MISSING** |
| ISR | s45 | Y (1000-step) | `h7_classification.json` | h7 only | results | **NO** (h7-only, no full taxonomy) |
| ISR | s46 | **N** | **None** | — | — | **MISSING** |
| **Random** | s42 | N (file only) | `plan018_random_s42_taxonomy_verification.json` | verification | total/proved/taxonomy/verification | **Partial** (different schema) |
| Random | s43 | **N** | **None** | — | — | **MISSING** |
| Random | s44 | Y (r2 dir) | `taxonomy.json` | taxonomy | eval_results (flat) | **NO** (different schema) |
| Random | s45 | N (log only) | **None** | — | — | **MISSING** |
| Random | s46 | **N** | **None** | — | — | **MISSING** |

### Summary

- **Only ISR s42** has C013-compatible `taxonomy_unified` format (proved/H7/H1_exact/H1_near/H8/genuine).
- **ISR s43, s44, s46** and **Random s43, s45, s46**: no classify/taxonomy data at all, no checkpoints (deleted by disk cleanup).
- **ISR s45**: has checkpoint + h7_classification only (no full taxonomy).
- **Random s42, s44**: have taxonomy files but in incompatible older schemas.
- Checkpoints: only ISR s45 retains model weights. All others were cleaned up — re-eval from checkpoint is impossible for those seeds.

---
