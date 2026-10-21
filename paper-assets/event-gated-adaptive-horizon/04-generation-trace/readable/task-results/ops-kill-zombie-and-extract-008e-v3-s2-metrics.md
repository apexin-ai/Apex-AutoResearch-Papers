# ops kill zombie and extract 008e v3 s2 metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-zombie-and-extract-008e_v3_s2-metrics_20260515T062237_result.json`
- **Structured JSON:** [`c2b6c5c054cddd48488c.json`](../../sessions/c2/c2b6c5c054cddd48488c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成。

---

### 产出汇总

**Task 1: Kill 僵尸进程** — PID 43442 已不存在（进程已自行退出）。GPU 占用确认：仅 142513 (009a, cuda:0, 4156 MiB) 和 119108 (009e, cuda:1, 2742 MiB)，无 008e_v3_s2 残留。

**Task 2: 完整 metrics 表格**

| step | eval_return | value_mean | actor_entropy | ve | nve |
|-----:|----------:|----------:|----------:|-----:|-----:|
| 5K | 39.27 | 0.00 | 8.239 | — | — |
| 15K | 180.85 | 3.91 | 2.352 | — | — |
| 25K | 211.82 | 30.27 | 0.170 | 0.143 | 1.64 |
| 35K | 320.39 | 79.75 | -3.498 | 0.249 | 1.03 |
| 45K | 356.93 | 125.25 | -4.915 | 0.351 | 1.06 |
| 55K | 418.32 | 172.89 | -5.121 | 0.413 | 1.02 |
| 65K | 435.09 | 220.47 | -5.135 | 0.507 | 0.90 |
| 75K | 576.54 | 272.64 | -5.224 | 0.473 | 0.66 |
| **85K** | **715.21** | **339.30** | **-5.208** | 0.474 | 0.68 |
| **95K** | **452.43** | **384.39** | **-4.529** | 0.850 | 1.34 |
| **105K** | **136.96** | **339.84** | **-3.828** | 2.481 | 3.78 |

Director 要求确认的数值全部匹配。actor_entropy 从 -5.21@85K 回升到 -3.83@105K，与 collapse 期间策略退化一致。

**Task 3: Registry 已更新** — 新增 `actor_entropy_trajectory`（11 个 checkpoint）、完整精度 `value_trajectory`、`actor_entropy_collapse_signature` 字段。

---
