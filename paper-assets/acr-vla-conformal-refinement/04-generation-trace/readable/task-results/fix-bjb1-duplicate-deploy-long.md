# fix bjb1 duplicate deploy long

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bjb1-duplicate-deploy-long_20260526T144114_result.json`
- **Structured JSON:** [`a2b2332b4c4598973bd0.json`](../../sessions/a2/a2b2332b4c4598973bd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bjb1-18228 cuda:0 (13765 MiB) 和 cuda:1 (9545 MiB) 已上 GPU，cuda:3 还在加载中。bjb1-32546 两个也在加载中。模型加载正常推进。

## 部署完成总结

### bjb1-18228（已 kill 重复，部署 3 个 Long VLA-only）

| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| pi05-vla-only-long-s42-4090-r3 | cuda:0 | 338021 | 运行中，13765 MiB |
| pi05-vla-only-long-s43-4090 | cuda:1 | 338482 | 运行中，9545 MiB |
| pi05-vla-only-long-s44-4090 | cuda:3 | 339339 | 模型加载中 |

- cuda:2 未动

### bjb1-32546（部署 2 个）

| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| pi05-vla-only-goal-s44-4090 | cuda:3 | 872072 | 模型加载中 |
| pi05-vla-only-object-s43-4090 | cuda:5 | 872361 | 模型加载中 |

- 原有 cuda:3 上的 spatial k2mean 实验 (PID 268191) 已 kill
- bjb1-32546 所有 GPU 均空闲，仅在 cuda:3/5 部署了新实验

---
