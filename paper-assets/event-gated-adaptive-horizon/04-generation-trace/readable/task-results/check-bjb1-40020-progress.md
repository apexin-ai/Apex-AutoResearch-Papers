# check bjb1 40020 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1_40020_progress_20260520T051545_result.json`
- **Structured JSON:** [`69dbdc9ed5165fc97f2d.json`](../../sessions/69/69dbdc9ed5165fc97f2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都正常推进，已脱离 8K 区间。

| 实验 | 当前 step | eval_return | GPU | GPU Util | FPS | 状态 |
|------|-----------|-------------|-----|----------|-----|------|
| **exp_027** (TCN, σ=0.2) | **45000** / 210K | 315.6 | GPU 0 (4090) | 13% | 7.7 | 正常 |
| **exp_028** (RAVE, ceil=1.5) | **45000** / 210K | 166.9 | GPU 1 (4090) | 1% | 7.8 | 正常 |

两个实验约 1.5 小时前启动（11:48/11:49），已完成约 21% 进度。exp_027 的 return 明显高于 exp_028（315 vs 167）。GPU util 偏低是正常的（dreamer 有大量 CPU 端 env step）。无报错。

---
