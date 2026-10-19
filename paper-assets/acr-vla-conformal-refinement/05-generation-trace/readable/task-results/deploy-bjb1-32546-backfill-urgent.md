# deploy bjb1 32546 backfill urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-backfill-urgent_20260528T082124_result.json`
- **Structured JSON:** [`a5384fcbaa3f6c21a5bb.json`](../../sessions/a5/a5384fcbaa3f6c21a5bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个计划实验和 4 个备选都已完成或在运行中：

| GPU | 计划 exp_id | 状态 |
|-----|------------|------|
| cuda:0 | smolvla-crm-norm005-spatial-s42-d149 | **DONE** (success) |
| cuda:1 | smolvla-crm-norm005-k10-object-s44-cqa1 | **DONE** (success) |
| cuda:2 | eval-supp-adapt-tau025-spatial-s46 | **RUNNING** (其他服务器) |
| cuda:3 | eval-supp-long-adapt-tau025-s47-r2 | **DONE** (negative) |
| cuda:4 | eval-supp-spatial-k2mean-s47 | **RUNNING** (其他服务器) |
| cuda:5 | eval-obs-only-object-norm005-seed75 | **DONE** (success) |

**备选列表同样全部已完成或运行中：**
- eval-obs-only-object-norm01-seed74 → DONE
- eval-obs-only-object-norm003-seed73 → DONE
- eval-obs-only-object-norm005-seed64 → DONE
- smolvla-adapt-tau015-object-s42-cqa1 → RUNNING

bjb1-32546 的 6 张 GPU 全部空闲可用，但已无可部署的实验。需要你提供新的实验列表。

---
