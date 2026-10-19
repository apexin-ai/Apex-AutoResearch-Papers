# deploy bjb1 32546 backfill 3gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-backfill-3gpu_20260523T083803_result.json`
- **Structured JSON:** [`9822fed38d5fa1894363.json`](../../sessions/98/9822fed38d5fa1894363.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就位。GPU 显存占用确认：

| GPU | 实验 | 显存 |
|-----|------|------|
| cuda:0 | eval-supp-adapt-tau025-object-s43 | 5014 MiB |
| cuda:1 | eval-supp-crm-norm005-goal-s43 | 5149 MiB |
| cuda:2 | eval-supp-adapt-tau025-goal-s43 | 2676 MiB |
| cuda:3 | train-crm-unified-4suite-r6（已有） | 544 MiB |
| cuda:4 | eval-supp-crm-norm005-object-s43 | 1789 MiB |
| cuda:5 | eval-supp-crm-norm005-spatial-s44（已有） | 2072 MiB |

6 个 GPU 全部在用。部署了 4 个新实验：
- **优先 3 个**：Object Adaptive tau=0.25 s43、Goal CRM norm=0.05 s43、Goal Adaptive tau=0.25 s43
- **备选 1 个**：Object CRM norm=0.05 s43

---
