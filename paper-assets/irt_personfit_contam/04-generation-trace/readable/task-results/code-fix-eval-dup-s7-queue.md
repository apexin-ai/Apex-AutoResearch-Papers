# code fix eval dup s7 queue

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-eval-dup-s7-queue_20260521T073939_result.json`
- **Structured JSON:** [`0eb33a47cb42733d3046.json`](../../sessions/0e/0eb33a47cb42733d3046.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 1. 重复进程 kill
- PID 96262: **已 kill** ✓

### 2. Eval 结果

| | lz* | acc | theta |
|---|---|---|---|
| **s4** (seed=301) | 8.967 | 0.6786 | -0.109 |
| **s5** (seed=302) | 8.532 | 0.6787 | -0.088 |

Registry 已更新（metrics + checkpoint_path + log_path）。

### 3. s7 训练
- PID 99214, **GPU 0** (实际落在 GPU 0 而非 GPU 3，`--gpu 3` 参数未按预期工作)
- 237 steps, 正常推进中
- Registry: RUNNING

### 4. s8 训练
- PID 99807, **GPU 3** (通过 `CUDA_VISIBLE_DEVICES=3` 正确放置)
- 939 steps (batch size 较小因为单卡显存分配不同), 正常推进中
- Registry: RUNNING

### 5. GPU 状态

| GPU | 显存占用 | 进程 |
|-----|---------|------|
| 0 | 46 GB / 98 GB | eval s5 残留 (8.6GB) + train s7 (37.7GB) |
| 1 | 23 GB / 98 GB | train s6 |
| 2 | 7.6 GB / 98 GB | train_grpo |
| 3 | 21.5 GB / 98 GB | train s8 |

注意：s7 的 `--gpu 3` 没生效，实际用了 GPU 0。如果后续启动需要精确控制 GPU，建议统一用 `CUDA_VISIBLE_DEVICES` 方式（如 s8 所用）。

---
