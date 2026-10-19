# eval collect results and gpu status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-results-and-gpu-status_20260521T103110_result.json`
- **Structured JSON:** [`1e0dc7dbea84cefdc6dd.json`](../../sessions/1e/1e0dc7dbea84cefdc6dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part 1: s2-ckpt-2500 结果

**PID 865026 仍在运行**（已运行 1h2m30s），结果文件尚未生成。

已完成的邻近 s2 checkpoints 供参考：

| checkpoint | ToF | NoF | SYCONScore |
|---|---|---|---|
| s2-ckpt2000 | 0.0442 | 0.9779 | 0.0846 |
| s2-ckpt3000 | 0.0497 | 0.9503 | 0.0945 |

## Part 2: 28034 GPU 状态

| GPU | 显存 | 利用率 | 任务 |
|---|---|---|---|
| 0 | 16884/32607 MiB | 50% | eval **exp003s2-ckpt3500** (PID 867046, 29min) |
| 1 | 16864/32607 MiB | 47% | eval **exp003-ckpt8000** (PID 868607, 8min) |
| 2 | 2/32607 MiB | 0% | **空闲** |
| 3 | 16884/32607 MiB | 45% | eval **exp003s2-ckpt2500** (PID 865026, 1h2m) |

s2-ckpt2500 的 eval 时间已超过 1 小时，参考 s2-ckpt2000 耗时 4305s (~72min)、s2-ckpt3000 耗时 4488s (~75min)，预计还需约 10-15 分钟完成。

---
