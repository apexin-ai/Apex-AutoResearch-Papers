# code cuda1 utilize

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cuda1-utilize_20260521T073413_result.json`
- **Structured JSON:** [`f906040a79d11492af0f.json`](../../sessions/f9/f906040a79d11492af0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 GPU 均已占满，**没有空闲 GPU**：

| GPU | PID | 任务 | 启动时间 |
|-----|-----|------|---------|
| 0 | 92119 | eval_lz.py clean_s4 | 15:18 |
| 0 | 96262 | eval_lz.py clean_s4 (第2个?) | 15:33 |
| 1 | 96745 | **train.py clean_s6** | 15:34 |
| 2 | 97296 | **train.py clean_s7** | 15:34 |
| 3 | 94961 | eval_lz.py clean_s5 | 15:25 |

**cuda:1 已被 s6 训练占用（23102 MiB），cuda:2 已被 s7 训练占用（14256 MiB）。** s7 已启动，不需要再跑。

此外 GPU 0 上跑了两个 clean_s4 eval 进程，可能有重复。

---
