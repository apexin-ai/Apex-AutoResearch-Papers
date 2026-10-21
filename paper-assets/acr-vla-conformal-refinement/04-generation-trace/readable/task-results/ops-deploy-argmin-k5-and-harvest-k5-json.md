# ops deploy argmin k5 and harvest k5 json

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-argmin-k5-and-harvest-k5-json_20260519T113449_result.json`
- **Structured JSON:** [`4a917eb264850c2cb5f3.json`](../../sessions/4a/4a917eb264850c2cb5f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个 seeds 数据已收集。汇总结果：

---

## 三个任务汇总

### 1. bjb2-40593 实验状态 — 全部在跑

| 实验 | 进度 | 状态 |
|---|---|---|
| spatial-seed43 | 5/10 tasks | 在跑 |
| scalar-seed45-r2 | 9/10 tasks | 在跑，即将完成 |
| random-selection-seed46-r2 | 3/10 tasks | 在跑 |

GPU 利用率 99%，无需干预。

### 2. bjb1-32546 K=5 argmin 部署 — 3 个已提交

| exp_id | GPU | Seed |
|---|---|---|
| eval-argmin-object-k5-seed42 | cuda:0 | 42 |
| eval-argmin-object-k5-seed43 | cuda:2 | 43 |
| eval-argmin-object-k5-seed45 | cuda:5 | 45 |

seed44 已在 bjb2-28827 运行，GPU 5 改用 seed45。timeout 16h，registry 已标记 RUNNING。

### 3. K=5 obs_only ε=0.2 全 7 seeds SR（JSON 直读）

| Seed | SR | 服务器 |
|---|---|---|
| seed42 | 14% | bjb1-18228 |
| seed43 | 19% | bjb2-28827 |
| seed44 | 17% | bjb2-28827 |
| seed45 | 15% | bjb2-28827 |
| seed46 | 16% | bjb1-18228 |
| seed47 | 13% | bjb1-18228 |
| seed48 | 18% | bjb1-32546 |

**Mean: 16.0% ± 2.2% (SD)**

---
