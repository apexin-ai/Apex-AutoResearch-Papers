# ops sync experiment plan v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_experiment_plan_v2_20260519T172921_result.json`
- **Structured JSON:** [`5f356cf32af22f2f7866.json`](../../sessions/5f/5f356cf32af22f2f7866.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已更新完成。变更摘要：

**plan_019 notes**:
- 8B RSFT 从 "2-seed" 更新为 "3-seed"，新增 s43 DONE (ign_f1=0.5471)，更新 mean=0.5433, std=0.49pp
- 8B no-evidence eval: 从 "r1 DONE/killed, r2 RUNNING" 更新为 "r2 DONE (ign_f1=0.5336, tax=-0.78pp)"
- 1.7B 2048-token retry 保持 RUNNING
- 剩余项简化为 "LLaMA s43/s44"（8B 3rd RSFT seed 已完成）

**plan_d112 notes**:
- d112_rsft_s44_eval_bf16 从 "RUNNING" 更新为 "DONE (ign_f1=0.5152)"
- 新增 "CED scoring DONE (3014 selected)"
- d112_rsft_no_evidence_eval_r3 保持 RUNNING

---
