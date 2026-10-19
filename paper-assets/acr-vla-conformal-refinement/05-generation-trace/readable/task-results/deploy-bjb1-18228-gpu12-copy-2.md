# deploy bjb1 18228 gpu12

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-gpu12_20260524T201758_result.json`
- **Structured JSON:** [`d92932ed804aa2123c84.json`](../../sessions/d9/d92932ed804aa2123c84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常运行：

| GPU | 实验 | Registry ID | 状态 |
|-----|------|-------------|------|
| 1 | CRM norm005 Object s48 | `crm-norm005-object-s48` | RUNNING, 10 tasks loaded |
| 2 | CRM norm005 Goal s49 | `crm-norm005-goal-s49` | RUNNING, 10 tasks loaded |

过程中发现 `crm_smolvla_3suite_v1/crm_best.pt` 不在 bjb1-18228 上，已从 bjb2-40593 通过 scp 传输（1.3 MB）。

---
