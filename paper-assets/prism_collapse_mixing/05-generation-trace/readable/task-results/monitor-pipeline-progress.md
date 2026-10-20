# monitor pipeline progress

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_pipeline_progress_20260516T024428_result.json`
- **Structured JSON:** [`473ac46f179d29f5e338.json`](../../sessions/47/473ac46f179d29f5e338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pipeline 状态报告

### 当前阶段：**gen2_signal**（计算 gen2 信号指标）

两个子进程并行运行中：

| PID | 任务 | 运行时间 | CPU |
|-----|------|---------|-----|
| 156586 | `compute_signals.py` gen2_seed42 (cuda:0) | 1h05m | 2327% |
| 156587 | `compute_signals.py` gen2_seed137 (cuda:0) | 1h05m | 2400% |

### 已完成阶段

| 阶段 | 完成时间 | 状态 |
|------|---------|------|
| gen0 signals (预计算) | 02:18-02:39 | ✓ |
| gen1 mixing | 04:34 | ✓ |
| gen1 training | 05:27 | ✓ |
| gen1 signals | 06:41-06:42 | ✓ |
| gen1 correlation analysis | 09:20-09:21 | ✓ (verdict: **FAIL**, 两个 seed 均未通过) |
| gen2 mixing | 08:51 | ✓ |
| gen2 training | 09:40 | ✓ |
| **gen2 signals** | — | **进行中** |

### ETA

Gen1 信号计算耗时 ~1h14m（05:27→06:41）。Gen2 信号已运行 1h05m，预计 **~10 分钟内完成**。

### GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 36% | 2525 / 97887 MiB (2.6%) |
| cuda:1 | 37% | 2525 / 97887 MiB (2.6%) |

### 主进程

PID 197985，总运行时间 6h07m，状态正常。Gen2 信号完成后，pipeline 预计进入 gen2 correlation analysis 或 gen3 阶段（取决于 `run_pipeline.py` 配置的总 generation 数）。

---
