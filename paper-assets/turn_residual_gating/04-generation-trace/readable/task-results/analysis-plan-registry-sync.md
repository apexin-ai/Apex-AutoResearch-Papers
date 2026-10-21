# analysis plan registry sync

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_registry_sync_20260522T045410_result.json`
- **Structured JSON:** [`2b95153fe7d751b40ae9.json`](../../sessions/2b/2b95153fe7d751b40ae9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

These registry IDs don't exist in registry.yaml — that's why they show as orphaned. The plan entries have `status: done` with results inline, but point to non-existent registry entries. Since the task says not to modify fields other than `registry_id`, and these registry IDs simply don't exist in the registry, there's nothing to fix here — they're correctly identified as orphaned because their registry entries were never created.

**Summary of changes made:**

| Plan | Change |
|------|--------|
| plan_009 | Added `registry_id: llama_phase1_gar_diag` → now resolves to DONE/success |
| plan_010 | Added `registry_id: llama_tg_s42` → now resolves to DONE/success |
| plan_012 | Added `registry_id: llama_eval_s42` → now resolves to DONE/success |
| plan_019 | Added `registry_id: v7_tg_s123` → now resolves to DONE/success |
| plan_023 | Changed `phase2_tg_s42_v8b_ss_fixed` → `phase2_tg_s42_v8b_resume` → now resolves to DONE/success |

**Coverage improved from ~50% to 59.1% (13/22 done).** Remaining gaps: 4 planned, 1 running, 2 failed, 2 orphaned (plan_015/017 — their `worker_analysis_*` registry IDs don't exist in registry.yaml).

---
