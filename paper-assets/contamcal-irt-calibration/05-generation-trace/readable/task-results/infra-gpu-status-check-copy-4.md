# infra gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260514T131206_result.json`
- **Structured JSON:** [`a6b8668c0b5d3fb9fcf7.json`](../../sessions/a6/a6b8668c0b5d3fb9fcf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: 占用 - compute_signals.py (0.5B_d005) PID 373251, 7384MiB, 34%
GPU 1: 占用 - evaluate.py (1.5B_d005_aligned) PID 365739, 5848MiB, 52%
GPU 2: 占用 - evaluate.py (0.5B_d005_aligned) PID 356787, 8284MiB, 37%
GPU 3: 占用 - evaluate.py (3B_d100_aligned)   PID 362942, 8976MiB, 69%
GPU 4: 占用 - evaluate.py (3B_d005_aligned)   PID 373931, 8976MiB, 95%
GPU 5: 空闲 - 0MiB, 0%
```

**关键确认：**
- **cuda:4**：未释放，正在跑 `exp_001_eval_3B_d005_aligned`（PID 373931，21:09 启动，GPU 95%满载）
- **cuda:5**：已释放，完全空闲
- **exp_001_eval_3B_d005_aligned**：在 cuda:4 上运行（`CUDA_VISIBLE_DEVICES=4`）

**活跃 tmux sessions**（从 ps 可见）：
- `exp_001_sft_0pct_05B`（PID 208932，历史 session）

**活跃 python 进程**：
| PID | GPU | 任务 | 启动时间 | 备注 |
|-----|-----|------|---------|------|
| 373251 | 0 | compute_signals 0.5B_d005 (exp002) | 21:06 | run_batch.py 调度 |
| 365739 | 1 | eval 1.5B_d005_aligned | 20:32 | |
| 356787 | 2 | eval 0.5B_d005_aligned | 19:15 | 已跑近2小时 |
| 362942 | 3 | eval 3B_d100_aligned | 20:06 | |
| 373931 | 4 | eval 3B_d005_aligned | 21:09 | |
| 318424 | - | zombie `&lt;defunct>` | 14:52 | 0.5B_raw eval 残留僵尸进程 |

**注意**：PID 318424 是僵尸进程（`&lt;defunct>`），原为 `eval 0.5B_raw`，已不占资源但未被回收。

---
