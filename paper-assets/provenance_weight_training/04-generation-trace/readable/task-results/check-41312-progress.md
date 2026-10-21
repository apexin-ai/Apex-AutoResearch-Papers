# check 41312 progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_41312_progress_20260517T114416_result.json`
- **Structured JSON:** [`449c423add694f404c5b.json`](../../sessions/44/449c423add694f404c5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 实验进度总览（2026-05-17 19:44 UTC）

所有 4 个进程健康运行，GPU 利用率正常。

| 实验 | PID | GPU | 当前step/总step | 进度 | 最近 loss | 速度 | 预计剩余 |
|---|---|---|---|---|---|---|---|
| **grid_b0_2_seed42** | 45224 | cuda:3 (100%, 75GB) | 5829/6103 | **95.5%** | ~1.73 (unwt) | ~7.1s/step | ~32 min |
| **llama3b_uniform_seed42** | 3112 | cuda:0 (100%, 71GB) | 5800/6103 | **95.0%** | ~1.74 (unwt) | 5.21s/step | ~26 min |
| **llama3b_adaptive_seed42** | 4005 | cuda:1 (79%, 71GB) | 5678/6103 | **93.0%** | ~1.80 (unwt) | 5.38s/step | ~38 min |
| **batchsize16_nmin8_seed42** | 50284 | cuda:2 (90%, 90GB) | 4999/6103 | **81.9%** | ~2.06 (unwt) | ~7.7s/step | ~2.4h |

### 关键信息

- **所有实验进度远超预期**：grid_b0_2 预期 92% 实际 95.5%，uniform 预期 65% 实际 95.0%，adaptive 预期 64% 实际 93.0%，batchsize16 预期 35% 实际 81.9%
- **前 3 个实验将在 ~30-40 分钟内完成**（约 20:10-20:25 UTC）
- **batchsize16 预计 ~22:10 UTC 完成**
- grid_b0_2 有一个完成监控脚本（PID 76220），完成后会写入 `/tmp/grid_b0_2_done`
- 两个 Llama-3B 实验有 wandb 上传进程在运行
- 总步数均为 6103（200M tokens / 32768 tokens_per_step）

---
