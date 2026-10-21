# deploy westd object paired r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-object-paired-r2_20260526T135616_result.json`
- **Structured JSON:** [`a1cc40094dc8cb56e977.json`](../../sessions/a1/a1cc40094dc8cb56e977.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-49937 全部 6 个实验部署完成，运行正常。**

| # | exp_id | GPU | PID | VRAM | util |
|---|--------|-----|-----|------|------|
| 1 | westd-pi05-crm-k2-object-s42 | cuda:0 | 491271 | 13969 MiB | 39% |
| 2 | westd-pi05-crm-k2-object-s43 | cuda:1 | 491696 | 13969 MiB | 38% |
| 3 | westd-pi05-crm-k2-object-s44 | cuda:2 | 492088 | 13969 MiB | 41% |
| 4 | westd-pi05-adaptive-object-s42-paired | cuda:3 | 492479 | 13903 MiB | 33% |
| 5 | westd-pi05-adaptive-object-s43-paired | cuda:4 | 492867 | 13903 MiB | 37% |
| 6 | westd-pi05-adaptive-object-s44-paired | cuda:5 | 493251 | 13903 MiB | 54% |

- 6 张 GPU 各有 1 个 python 进程，无碰撞
- 每个进程 ~14 GB VRAM，GPU 利用率 33-54%
- CRM s42/s43 已进入 rollout（task 1: 5/5 success），其余正在加载 task
- Registry 全部标记为 RUNNING，spec 完整

---
