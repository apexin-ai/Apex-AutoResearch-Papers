# ops westd38929 collect k095 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-collect-k095-result_20260521T032736_result.json`
- **Structured JSON:** [`69e46e29d73682604d40.json`](../../sessions/69/69e46e29d73682604d40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### k=0.95 v2 (cuda:0) — 未完成，Task 10/10 进行中 (Ep 20/50)

已完成 9/10 tasks 的 per-task SR：

| Task | 物品 | SR |
|------|------|-----|
| 1 | alphabet soup | 0.800 |
| 2 | cream cheese | 0.420 |
| 3 | salad dressing | 0.700 |
| 4 | bbq sauce | 0.420 |
| 5 | ketchup | 0.880 |
| 6 | tomato sauce | 0.840 |
| 7 | butter | 0.600 |
| 8 | milk | 0.680 |
| 9 | chocolate pudding | 0.660 |
| 10 | orange juice | **Ep 20/50** (18/20 so far) |

Task 10 当前跑到 Ep 20/50，速度 2.0 eps/min，预计 ~15 分钟完成。

### k=0.7 v2 (cuda:1) — 未完成，Task 9/10 进行中 (Ep 20/50)

已完成 8/10 tasks：

| Task | 物品 | SR |
|------|------|-----|
| 1 | alphabet soup | 0.720 |
| 2 | cream cheese | 0.200 |
| 3 | salad dressing | 0.560 |
| 4 | bbq sauce | 0.380 |
| 5 | ketchup | 0.640 |
| 6 | tomato sauce | 0.520 |
| 7 | butter | 0.200 |
| 8 | milk | 0.240 |
| 9 | chocolate pudding | **Ep 20/50** (8/20 so far) |
| 10 | 未开始 | — |

Task 9 at Ep 20/50，速度 1.8 eps/min，预计 ~45 分钟完成全部。

### GPU 状态
- cuda:0: 91% util, 15.9GB/97.9GB — **占用中**
- cuda:1: 69% util, 15.9GB/97.9GB — **占用中**
- cuda:2/3: 空闲（不碰）

---
