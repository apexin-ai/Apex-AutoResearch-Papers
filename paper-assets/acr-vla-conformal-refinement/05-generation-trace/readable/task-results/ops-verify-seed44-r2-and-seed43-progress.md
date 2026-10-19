# ops verify seed44 r2 and seed43 progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-seed44-r2-and-seed43-progress_20260516T045552_result.json`
- **Structured JSON:** [`ae9f4cb86615f5bea229.json`](../../sessions/ae/ae9f4cb86615f5bea229.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 任务 1：bjb1-18228 — r2 存活确认

| PID | 任务 | GPU | 状态 | 运行时长 | 显存 |
|-----|------|-----|------|---------|------|
| 428117 | argmin r2 (seed44) | cuda:3 | **存活** (Ss) | 3h23m | 4681 MiB |
| 428406 | obs_only r2 (seed44) | cuda:2 | **存活** (Ss) | 3h23m | 4717 MiB |

**r3 子进程 (430990, 431194)：已死。**

### 任务 2：bjb1-32546 — obs_only ε=0.2 seed43 r2 进度

PID 148788 **存活**，已运行 9h57m。

当前进度：**8/10 tasks 完成**（第 8 个 milk 正在跑 rollout 5/10）。已完成 tasks 成绩：

| Task | Success Rate |
|------|-------------|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 10% (1/10) |
| salad_dressing | 20% (2/10) |
| bbq_sauce | 40% (4/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 10% (1/10) |
| butter | 10% (1/10) |
| milk | 进行中 (1/5 so far) |

JSON 输出文件尚未生成（评估完成后才写入）。

### 任务 3：全局 GPU 占用

**bjb1-18228** (4× A5000 24GB)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 2410/24564 MiB | 17% | 占用 |
| 1 | 1/24564 MiB | 0% | **空闲** |
| 2 | 4735/24564 MiB | 23% | 占用 (obs_only r2) |
| 3 | 4699/24564 MiB | 20% | 占用 (argmin r2) |

**bjb1-32546** (6× A5000 24GB)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 1943/24564 MiB | 23% | 占用 |
| 1 | 2/24564 MiB | 0% | **空闲** |
| 2 | 1942/24564 MiB | 21% | 占用 |
| 3 | 2411/24564 MiB | 24% | 占用 (seed43 r2) |
| 4 | 1943/24564 MiB | 23% | 占用 |
| 5 | 1942/24564 MiB | 23% | 占用 |

**bjb2-28827** (6× A5000 24GB)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 2410/24564 MiB | 18% | 占用 |
| 1 | 2411/24564 MiB | 18% | 占用 |
| 2 | 2875/24564 MiB | 19% | 占用 |
| 3 | 2875/24564 MiB | 19% | 占用 |
| 4 | 2411/24564 MiB | 18% | 占用 |
| 5 | 1941/24564 MiB | 19% | 占用 |

**bjb2-40593** (1× A5000 24GB)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 1870/24564 MiB | 11% | 占用 |

**空闲 GPU：bjb1-18228 GPU1、bjb1-32546 GPU1，共 2 块。**

---
