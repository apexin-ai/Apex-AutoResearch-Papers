# ssh retry progress check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_retry-progress-check_20260518T075424_result.json`
- **Structured JSON:** [`91e1a2d0542acccf8a24.json`](../../sessions/91/91e1a2d0542acccf8a24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度汇报

### 当前状态
| 指标 | 值 |
|------|-----|
| 已完成 episodes | **41/200** (20.5%) |
| 已完成 tasks | **2/10** (chemistry-mix, find-animal) |
| 正在进行 | freeze (ep 2/20) |
| GPU0 利用率 | 100% |

### 已完成 task 结果
| Task | Death Rate | Success Rate |
|------|-----------|-------------|
| chemistry-mix | 50.0% | 15.0% |
| find-animal | 55.0% | 10.0% |

### 速度与 ETA
- 进程启动: 14:43 UTC，已运行 ~72 min
- 速率: **~1.76 min/episode**
- 剩余: 159 episodes
- 预估剩余时间: **~4.7 小时**
- 预估完成: **~20:40 UTC**

### 脚本是否支持 task-level 拆分
**不支持。** 当前 argparse 参数只有 `--n-values`, `--episodes-per-task`, `--max-steps`, `--model`, `--api-base`, `--output-dir`, `--seed`, `--dry-run`。没有 `--tasks` 或 `--skip-completed` 参数。task 列表硬编码在 `DEATH_PRONE_TASKS` 中。

### 10 个 task（按脚本顺序）
1. chemistry-mix ✅
2. find-animal ✅
3. **freeze** ← 进行中
4. grow-fruit
5. identify-life-stages-1
6. identify-life-stages-2
7. inclined-plane-determine-angle
8. lifespan-longest-lived
9. lifespan-longest-lived-then-shortest-lived
10. measure-melting-point-unknown-substance

### 拆分方案（需改脚本）
如果要并行，需要给脚本加 `--tasks` 参数。改动很小：把 `DEATH_PRONE_TASKS` 改为从 argparse 读取即可。拆分后：

- **进程 A (GPU0)**: 当前进程继续跑，不中断
- **进程 B (GPU1)**: 跑后 5 个 task: `inclined-plane-determine-angle`, `lifespan-longest-lived`, `lifespan-longest-lived-then-shortest-lived`, `measure-melting-point-unknown-substance`, 再加一个已跑完的前面 task 也不需要

但当前脚本单进程写同一个 output_dir，并行需要分 output_dir 再合并。是否要我加 `--tasks` 参数并启动第二个进程？

---
