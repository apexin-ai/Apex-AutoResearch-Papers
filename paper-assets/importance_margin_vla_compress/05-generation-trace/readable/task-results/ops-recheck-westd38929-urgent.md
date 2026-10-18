# ops recheck westd38929 urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_recheck-westd38929-urgent_20260520T150725_result.json`
- **Structured JSON:** [`d99fe407b452916b7a2a.json`](../../sessions/d9/d99fe407b452916b7a2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结果

### 1. GPU 状态：全部 4 卡正常运行，无空闲

| GPU | PID | 实验 | 显存 | GPU-Util | 运行时间 | 状态 |
|-----|--------|------|------|----------|---------|------|
| 0 | 787425 | OpenVLA l2norm k=0.5 libero_object | 15961MiB | 69% | 2h13m | **运行中** (Task 5/10) |
| 1 | 788043 | OpenVLA l2norm k=0.3 libero_object | 16089MiB | 63% | 2h12m | **运行中** (Task 5/10) |
| 2 | 796062 | OpenVLA l2norm k=0.9 libero_object | 15961MiB | 91% | 1h50m | **运行中** |
| 3 | 796839 | OpenVLA l2norm k=0.95 libero_object | 15961MiB | 70% | 1h49m | **运行中** |

GPU 0 **不是空闲**——进程状态 `Rl`（running, multi-threaded），69% GPU 利用率，正在跑 Task 5/10 (ketchup)，进度正常（~1.8 eps/min）。

### 2. 已完成实验（X-VLA l2norm prune, libero_object）

| keep_ratio | SR | 备注 |
|------------|------|------|
| k=0.1 | **0.0%** | 剪太狠，完全崩 |
| k=0.2 | **5.2%** | |
| k=0.3 | **23.0%** | |
| k=0.5 | **42.6%** | |
| k=0.7 | **56.2%** | |
| k=0.9 | **97.6%** | |
| k=0.95 | **99.0%** | |
| k=1.0 | **99.2%** | baseline（无剪枝） |

### 3. 崩溃实验：无

全部进程存活，无崩溃。

### 4. 空闲 GPU：无

4 卡全满。当前 4 个 OpenVLA 评估预计还需 ~2-3 小时完成（每个 10 tasks × 50 eps，目前在 Task 4-5）。

---
