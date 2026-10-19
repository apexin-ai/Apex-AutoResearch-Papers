# diagnose spatial k10 seed46 47 and idle gpus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_spatial-k10-seed46-47-and-idle-gpus_20260519T161323_result.json`
- **Structured JSON:** [`782dda34d71186b2ddaa.json`](../../sessions/78/782dda34d71186b2ddaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. seed46 (bjb2-28827) — 正在运行

- **PID 871615**: 存活，状态 `Ss+`，已运行 48 分钟
- **GPU cuda:3**: 29% util, 3660 MiB / 24564 MiB — 正常工作中
- **进度**: 5/10 tasks 完成，无输出 JSON（尚未写入）
- **已完成 tasks 的 success rate**:
  - `pick_up_bowl_between_plate_and_ramekin → plate`: **90%** (9/10)
  - `pick_up_bowl_next_to_ramekin → plate`: **100%** (10/10)
  - `pick_up_bowl_from_table_center → plate`: **0%** (0/10)
  - `pick_up_bowl_on_cookie_box → plate`: **30%** (3/10)
  - `pick_up_bowl_in_top_drawer → plate`: **10%** (1/10)

### 2. seed47 (bjb1-32546) — 正在运行

- **PID 972439**: 存活，状态 `Ss+`，已运行 46 分钟
- **GPU cuda:1**: 37% util, 3661 MiB / 24564 MiB — 正常工作中
- **进度**: 5/10 tasks 完成，无输出 JSON
- **已完成 tasks 的 success rate**:
  - `pick_up_bowl_between_plate_and_ramekin → plate`: **80%** (8/10)
  - `pick_up_bowl_next_to_ramekin → plate`: **90%** (9/10)
  - `pick_up_bowl_from_table_center → plate`: **0%** (0/10)
  - `pick_up_bowl_on_cookie_box → plate`: **30%** (3/10)
  - `pick_up_bowl_in_top_drawer → plate`: **10%** (1/10)

**结论**: 两个实验状态正常，不是卡住/死亡/从未启动。PREPARING 状态只是 tracker 未更新。预计再 ~45 分钟完成剩余 5 个 tasks。

---

### 3. 全服务器 GPU 空闲情况

| 服务器 | GPU | Util | Mem Used | 状态 |
|--------|-----|------|----------|------|
| **bjb2-28827** | cuda:0 | 0% | 1 MiB | **IDLE** |
| | cuda:1 | 17% | 1906 MiB | 占用 |
| | cuda:2 | 17% | 1906 MiB | 占用 |
| | cuda:3 | 29% | 3660 MiB | seed46 实验 |
| | cuda:4 | 0% | 1 MiB | **IDLE** |
| | cuda:5 | 0% | 1 MiB | **IDLE** |
| **bjb1-32546** | cuda:0 | 0% | 2 MiB | **IDLE** |
| | cuda:1 | 37% | 3661 MiB | seed47 实验 |
| | cuda:2 | 0% | 2 MiB | **IDLE** |
| | cuda:3 | 0% | 2 MiB | **IDLE** |
| | cuda:4 | 0% | 2 MiB | **IDLE** |
| | cuda:5 | 0% | 2 MiB | **IDLE** |
| **bjb1-18228** | cuda:0 | 21% | 2411 MiB | 占用 |
| | cuda:1 | 0% | 1 MiB | **IDLE** |
| | cuda:2 | 23% | 2411 MiB | 占用 |
| | cuda:3 | 23% | 2411 MiB | 占用 |
| **bjb2-40593** | cuda:0 | 97% | 5765 MiB | 高负载 |

**空闲 GPU 汇总**: bjb2-28827 有 3 个空闲 (0/4/5)，bjb1-32546 有 5 个空闲 (0/2/3/4/5)，bjb1-18228 有 1 个空闲 (1)。共 **9 个 GPU 完全空闲**。

---
