# ops gpu patrol harvest deploy round2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-patrol-harvest-deploy-round2_20260518T070028_result.json`
- **Structured JSON:** [`902ef54ce8fdd892ab57.json`](../../sessions/90/902ef54ce8fdd892ab57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部巡检完成。

---

### 服务器状态

| 服务器 | GPU | 显存占用 | 状态 | 运行实验 |
|--------|-----|----------|------|----------|
| **bjb2-28827** | 0 | 3768 MiB | 🔴 忙 | eval-obs-only-norm01-s42 |
| | 1 | 3804 MiB | 🔴 忙 | eval-obs-only-object-norm02-k5-seed43 |
| | 2 | 4736 MiB | 🔴 忙 | eval-perdof-norm01-s42 |
| | 3 | 3804 MiB | 🔴 忙 | eval-perdof-object-norm02-seed48 |
| | 4 | 4700 MiB | 🔴 忙 | eval-random-selection-object-seed43 |
| | 5 | 3342 MiB | 🔴 忙 | eval-random-selection-object-seed44 |
| **bjb1-32546** | 0 | 3805 MiB | 🔴 忙 | eval-dc-r2 |
| | 1 | 3343 MiB | 🔴 忙 | eval-obs-only-object-norm005-seed44 |
| | 2 | 3343 MiB | 🔴 忙 | eval-obs-only-object-norm005-seed45 |
| | 3 | 3805 MiB | 🔴 忙 | eval-obs-only-object-norm01-seed46-r2 |
| | 4 | 2411 MiB | 🔴 忙 | eval-perdof-object-norm005-seed44 |
| | 5 | 3805 MiB | 🔴 忙 | eval-perdof-object-norm01-seed43 |
| **bjb1-18228** | 0 | 4735 MiB | 🔴 忙 | eval-obs-only-object-norm02-seed48 |
| | 1 | 2875 MiB | 🔴 忙 | eval-obs-only-object-norm01-seed48 |
| | 2 | 3342 MiB | 🔴 忙 | eval-obs-only-object-norm03-seed48 |
| | 3 | 2410 MiB | 🔴 忙 | eval-perdof-norm02-seed45-r3 |
| **bjb2-40593** | 0 | 2338 MiB | 🔴 忙 | eval-random-selection-object-seed42 (nohup) |

**空闲 GPU：0**

---

### 新完成实验（误标修正）

| 实验ID | SR | 原标记 | 修正为 |
|--------|-----|--------|--------|
| eval-perdof-object-default-seed46 | 0.00 | failed | **negative** ✅ |
| eval-obs-only-object-norm02-k5-seed42 | 0.14 | failed | **success** ✅ |
| eval-obs-only-object-norm01-seed45 | 0.14 | failed | **success** ✅ |
| eval-perdof-object-norm01-seed46 | 0.10 | PREPARING | **DONE/negative** ✅ |

---

### 新部署实验

无。全部 17 张 GPU 均在运行中，无法部署。

---

### 剩余队列（5 个实验等待空闲 GPU）

| 优先级 | 实验 | 命令关键参数 |
|--------|------|-------------|
| 1 | K=5 seed44 | obs_only, K=5, norm02, seed44 |
| 2 | perdof default seed43 | perdof, uncapped, seed43 |
| 3 | perdof default seed45 | perdof, uncapped, seed45 |
| 4 | obs_only norm02 seed43 r3 | obs_only, norm02, seed43 重试 |
| 5 | perdof norm03 seed44 | perdof, norm03, seed44 |

---
