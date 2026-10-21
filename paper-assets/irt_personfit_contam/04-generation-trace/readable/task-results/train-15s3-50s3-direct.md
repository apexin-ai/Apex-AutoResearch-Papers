# train 15s3 50s3 direct

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_15s3-50s3-direct_20260522T180810_result.json`
- **Structured JSON:** [`05d36525fe085bcb73d6.json`](../../sessions/05/05d36525fe085bcb73d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。完整 3×3 矩阵：

### lz* 值矩阵

| Condition | s1 | s2 | s3 |
|-----------|--------|--------|--------|
| **15%** | 3.8494 | 4.9400 | 5.4436 |
| **25%** | 2.6429 | 2.2300 | 4.7800 |
| **50%** | 7.2892 | 4.7000 | 2.8695 |

### Cohen's d (|d|) 矩阵

| Condition | s1 | s2 | s3 |
|-----------|------|------|------|
| **15%** | 6.57 | 5.09 | 4.41 |
| **25%** | 8.22 | 8.78 | 5.31 |
| **50%** | 1.90 | 5.42 | 7.91 |

### Per-condition 统计

| Level | mean\|d\| | SD | range |
|-------|-----------|------|--------------|
| 15% | 5.36 | 1.11 | [4.41, 6.57] |
| 25% | 7.43 | 1.86 | [5.31, 8.78] |
| 50% | 5.07 | 3.02 | [1.90, 7.91] |

所有 condition 的 lz* 均远低于 clean baseline (mean=8.68)，|d| 均 ≥ 1.90。50% 的 seed 间方差最大 (SD=3.02)，25% 检测最稳定。

---
