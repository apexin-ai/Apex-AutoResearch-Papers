# ops post restart2 status 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart2-status-29046_20260519T131052_result.json`
- **Structured JSON:** [`d34b55c934169b4185da.json`](../../sessions/d3/d34b55c934169b4185da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均在正常运行。

### GPU 状态
| GPU | 利用率 | 显存占用 | 温度 |
|-----|--------|----------|------|
| 0 | 93% | 66.9 GB / 96 GB | 65°C |
| 1 | 98% | 38.2 GB / 96 GB | 68°C |

### exp-003 (R3-only GRPO, GPU 1)
- **进度**: 2561 / 8000 (32%)
- **已运行**: ~20h 19m
- **ETA**: ~40h
- **最近 R3 reward**: 0.56 ~ 0.68，step 2560 汇总 mean=0.6795, std=0.4722

### exp002v2-recalib (Cosine + Recalib, GPU 0)
- **进度**: 1615 / 8000 (20%)
- **已运行**: ~6h 30m
- **ETA**: ~31h 30m
- **最近 R1 值**: -0.06 ~ -0.16（仍为负，尚未转正）
- **R3**: 0.81 ~ 0.99（稳定高位）
- **combined**: 0.57 ~ 0.73

---
