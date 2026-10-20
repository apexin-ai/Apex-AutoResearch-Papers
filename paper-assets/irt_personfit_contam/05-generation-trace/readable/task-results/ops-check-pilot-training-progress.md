# ops check pilot training progress

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-pilot-training-progress_20260523T152416_result.json`
- **Structured JSON:** [`b542f6bf891e2440aede.json`](../../sessions/b5/b542f6bf891e2440aede.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Llama Pilot S1 训练进度

| 实验 | 进度 | Epoch | Loss | Token Acc | ETA |
|------|------|-------|------|-----------|-----|
| **15pct** | 1248/1335 (93%) | 2.0 | 1.451 | 0.6314 | ~2 min |
| **50pct** | 1184/2256 (52%) | ~1.0 | 1.532 | 0.6428 | ~21 min |

## GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 25.3/97.9 GB | 97% |
| 1 | 16.6/97.9 GB | 94% |
| 2 | 空闲 | 0% |
| 3 | 空闲 | 0% |

15pct 即将完成（~2分钟），50pct 还需约 21 分钟。两个训练分别跑在 GPU 0 和 GPU 1 上。

---
