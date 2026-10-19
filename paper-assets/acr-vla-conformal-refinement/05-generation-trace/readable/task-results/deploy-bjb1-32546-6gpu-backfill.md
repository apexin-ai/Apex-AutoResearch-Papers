# deploy bjb1 32546 6gpu backfill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-6gpu-backfill_20260523T201046_result.json`
- **Structured JSON:** [`41a7bc85083c10a31bbc.json`](../../sessions/41/41a7bc85083c10a31bbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

| GPU | 实验 | Registry ID | PID | GPU 显存 |
|-----|------|-------------|-----|----------|
| cuda:0 | Object CRM s46 | eval-supp-crm-norm005-obj-s46 | 102927 | 5731 MiB |
| cuda:1 | Long VLA-only s45 | eval-supp-long-vla-only-s45 | 103128 | 5481 MiB |
| cuda:2 | Long Adaptive s45 | eval-supp-long-adapt-tau025-s45 | 103397 | 6138 MiB |
| cuda:3 | Long CRM s45 | eval-supp-long-crm-norm005-s45 | 103675 | 5284 MiB |
| cuda:4 | Long Reconvla s45 | eval-supp-long-reconvla-s45 | 103942 | 4584 MiB |
| cuda:5 | Goal Adaptive s45 | eval-supp-goal-adapt-tau025-s45 | 104216 | 4937 MiB |

6/6 GPU 满载，6/6 日志正常（10 tasks loaded），6/6 Registry 已标记 RUNNING。

---
