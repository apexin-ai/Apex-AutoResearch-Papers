# analysis m1 bootstrap full

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m1-bootstrap-full_20260514T032201_result.json`
- **Structured JSON:** [`fddbb782f40067f400c8.json`](../../sessions/fd/fddbb782f40067f400c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量 Bootstrap CI 分析完成（n_boot=10000）。完整结果：

---

## Table 1: Phase Gradient = median(II_low) / median(II_high)

| Strategy | Sparsity | Gradient | 95% CI | p(MW) | Cohen's d |
|----------|----------|----------|--------|-------|-----------|
| importance | 0.15 | **14.27** | [12.12, 17.42] | 2.98e-116 | 0.71 |
| importance | 0.20 | **30.85** | [25.29, 41.28] | 5.88e-143 | 0.49 |
| importance | 0.25 | **55.44** | [44.71, 71.36] | 1.14e-151 | 0.45 |
| importance | 0.30 | **75.50** | [50.80, 95.24] | 2.19e-117 | 0.22 |
| random | 0.15 | 1.22 | [0.96, 1.52] | 6.36e-02 | 0.01 |
| random | 0.25 | 1.00 | [0.91, 1.10] | 8.30e-01 | 0.01 |

## Table 2: Per-Phase Median II (reconstructed)

| Strategy | Sparsity | high | mid | low |
|----------|----------|------|-----|-----|
| importance | 0.15 | 0.2073 | 0.7166 | 2.9582 |
| importance | 0.20 | 0.3525 | 1.5102 | 10.8759 |
| importance | 0.25 | 0.5390 | 4.8090 | 29.8800 |
| importance | 0.30 | 0.5576 | 7.5261 | 42.0989 |
| random | 0.15 | 0.1378 | 0.2655 | 0.1678 |
| random | 0.25 | 2.9539 | 2.6117 | 2.9534 |

## Table 3: Pairwise Mann-Whitney U Tests

| Strategy | Sparsity | Pair | U | p | r_rb |
|----------|----------|------|---|---|------|
| importance | 0.15 | low vs high | 215044 | 2.98e-116 | -0.8539 |
| | | low vs mid | 136674 | 8.50e-42 | -0.5399 |
| | | mid vs high | 163644 | 1.00e-60 | -0.6381 |
| importance | 0.20 | low vs high | 226011 | 5.88e-143 | -0.9484 |
| | | low vs mid | 147754 | 1.93e-62 | -0.6647 |
| | | mid vs high | 165808 | 8.60e-65 | -0.6597 |
| importance | 0.25 | low vs high | 229360 | 1.14e-151 | -0.9773 |
| | | low vs mid | 144637 | 3.33e-56 | -0.6296 |
| | | mid vs high | 183280 | 1.45e-102 | -0.8346 |
| importance | 0.30 | low vs high | 215534 | 2.19e-117 | -0.8581 |
| | | low vs mid | 119984 | 1.08e-18 | -0.3518 |
| | | mid vs high | 166917 | 6.29e-67 | -0.6708 |
| random | 0.15 | low vs high | 124014 | 6.36e-02 | -0.0691 |
| | | low vs mid | 71423 | 9.60e-07 | 0.1953 |
| | | mid vs high | 126721 | 4.62e-12 | -0.2685 |
| random | 0.25 | low vs high | 116924 | 8.30e-01 | -0.0080 |
| | | low vs mid | 94507 | 1.04e-01 | -0.0648 |
| | | mid vs high | 93917 | 1.23e-01 | 0.0599 |

## Table 4: Importance vs Random Gradient Comparison

| Sparsity | Imp Gradient | Rnd Gradient | Diff | p (two-sided) | Sig |
|----------|-------------|-------------|------|---------------|-----|
| 0.15 | 14.27 | 1.22 | 13.06 | 0.0000 | *** |
| 0.25 | 55.44 | 1.00 | 54.44 | 0.0000 | *** |

---

**核心发现：**
- Importance pruning 的 phase gradient 随 sparsity 单调递增（14.3x → 75.5x），所有 CI 远离 1.0，全部 p < 1e-100
- Random pruning gradient ≈ 1.0（无 phase 依赖），CI 包含 1.0
- 两组在 s=0.15 和 s=0.25 的 gradient 差异极显著（p ≈ 0）
- 结果保存于 `/root/autodl-tmp/pacs/analysis/bootstrap_results_full.json`

---
