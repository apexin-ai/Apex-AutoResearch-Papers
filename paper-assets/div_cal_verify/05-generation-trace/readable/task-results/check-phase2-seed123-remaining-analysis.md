# check phase2 seed123 remaining analysis

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase2_seed123_remaining_analysis_20260513T151658_result.json`
- **Structured JSON:** [`2ec473d1bd683acfdae2.json`](../../sessions/2e/2ec473d1bd683acfdae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **phase2_seed123_remaining** 已完成，registry 已更新为 DONE/success。

## 结果汇总

运行时间：18:04 → 20:27 CST（约 2h23min）

### Uncurated (seed=123)

| Gen | PPL | RankMe | kNN | Rare | Corr |
|-----|------|--------|------|-------|-------|
| 0 | 36.69 | 277.86 | 0.988 | 0.0293 | -0.0222 |
| 1 | 45.29 | 297.08 | 0.988 | 0.0192 | -0.0554 |
| 2 | 53.76 | 301.88 | 0.988 | 0.0137 | -0.0448 |
| 3 | 53.76 | 300.70 | 0.988 | 0.0116 | -0.0365 |
| 4 | 54.33 | 298.78 | 0.988 | 0.0107 | -0.0471 |
| 5 | 53.00 | 293.21 | 0.988 | 0.0100 | -0.0370 |
| 6 | 49.87 | 295.35 | 0.988 | 0.0101 | -0.0477 |
| 7 | **46.15** | 290.13 | 0.988 | 0.0093 | -0.0755 |

PPL 先升后降（gen4 峰值 54.33 → gen7 回到 46.15），rare n-gram 持续下降。

### RGDS (seed=123)

| Gen | PPL | RankMe | kNN | Rare | Corr | Ratio |
|-----|------|--------|------|-------|-------|-------|
| 0 | 36.71 | 272.68 | 0.988 | 0.0293 | -0.0116 | 0.9997 |
| 1 | 42.81 | 286.96 | 0.988 | 0.0186 | -0.0544 | 0.9066 |
| 2 | 47.35 | 291.31 | 0.988 | 0.0142 | -0.0569 | 0.8604 |
| 3 | 52.64 | 295.72 | 0.988 | 0.0119 | -0.0185 | 0.8689 |
| 4 | 52.74 | 294.90 | 0.988 | 0.0101 | -0.0042 | 0.8863 |
| 5 | 60.62 | 294.93 | 0.988 | 0.0087 | -0.0036 | 0.7809 |
| 6 | 75.03 | 299.36 | 0.988 | 0.0070 | -0.0119 | 0.6789 |
| 7 | **81.57** | 298.35 | 0.988 | 0.0062 | -0.0312 | 0.5236 |

RGDS 的 PPL 单调上升（36.71 → 81.57），selection ratio 持续下降（1.0 → 0.52），表明 RGDS 越来越积极地过滤数据，但 PPL 退化明显比 uncurated 更严重。

---
