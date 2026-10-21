# monitor westd41074 attn object

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd41074_attn_object_20260525T144423_result.json`
- **Structured JSON:** [`e1c01e50cf7d4d8783f4.json`](../../sessions/e1/e1c01e50cf7d4d8783f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部进度已收集。汇总如下：

---

## westd-41074 实验进度总览

| GPU | 实验 | PID | 运行时间 | 进度 | ETA |
|-----|------|-----|---------|------|-----|
| **0** | **Attn k=0.9 Object** | 173847 | 4h23m | **Task 8/10 开始** (7 tasks 完成) | **~1.5h** |
| 1 | L2Norm k=0.5 Goal | 173920 | 4h23m | Task 7/10, Ep 30/50 | ~2h |
| 2 | Random k=0.5 Object | 259177 | 2h15m | Task 2/10, Ep 40/50 | ~8-10h |
| 3 | L2Norm k=0.5 Spatial | 264356 | 2h06m | Task 2/10, Ep 30/50 | ~10h |

---

### Attn k=0.9 Object (重点)

已完成 7 个 task 的 SR：

| Task | SR |
|------|-----|
| 1. alphabet soup → basket | 74.0% |
| 2. cream cheese → basket | 46.0% |
| 3. salad dressing → basket | 76.0% |
| 4. bbq sauce → basket | 38.0% |
| 5. ketchup → basket | 76.0% |
| 6. tomato sauce → basket | 74.0% |
| 7. butter → basket | 28.0% |

**当前累计：206/350 = 58.9% SR（前7 tasks）**

正在跑 Task 8（milk），速率 ~1.4-1.9 eps/min。还剩 Tasks 8-10 共 150 episodes，预计 **~1.5 小时后完成**（约 UTC 00:15 左右）。

### 其他实验
- **GPU 2/3 速度异常慢**（~0.7 eps/min vs GPU 0/1 的 ~1.5-1.9），可能是 spatial 和 random k=0.5 pruning 后推理变慢。这两个还需 8-10 小时。

### 结果 JSON
尚无新的完成文件。4 个实验均在运行中，eval_results/ 下没有对应的输出 JSON。

---
