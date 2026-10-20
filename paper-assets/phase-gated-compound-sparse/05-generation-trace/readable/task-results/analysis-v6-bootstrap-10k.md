# analysis v6 bootstrap 10k

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v6-bootstrap-10k_20260514T044601_result.json`
- **Structured JSON:** [`68c3423028efaba2d260.json`](../../sessions/68/68c3423028efaba2d260.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

analyze_v6_complete.py 成功运行，B=10000。以下是完整结果：

---

## Part 1: V6 四组实验 Metrics

| Sparsity | Phase | n (non-null) | Median | Mean | Std |
|----------|-------|-------------|--------|------|-----|
| **s015** | high | 43 | 0.2266 | 0.2874 | 0.2719 |
| | mid | 32 | 0.7432 | 1.6858 | 2.7778 |
| | low | 24 | 2.8762 | 8.5161 | 15.4338 |
| **s020** | high | 42 | 0.3353 | 0.4936 | 0.5491 |
| | mid | 28 | 1.6733 | 4.9538 | 10.8443 |
| | low | 21 | 9.2538 | 25.8764 | 35.6782 |
| **s025** | high | 42 | 0.6641 | 0.8842 | 0.9003 |
| | mid | 23 | 5.3067 | 10.0570 | 14.4768 |
| | low | 21 | 24.1619 | 71.8854 | 113.6517 |
| **s030** | high | 40 | 0.8833 | 1.5151 | 2.7019 |
| | mid | 22 | 7.2706 | 78.8215 | 296.0726 |
| | low | 20 | 34.6937 | 1163.9677 | 4226.1852 |

每组 per_problem_ii count = 50 problems（non-null 数量因 phase 而异，见上表 n 列）。

---

## Part 2: Bootstrap CI 表 (B=10000, problem-level resampling)

### Paired variant（同一 problem 同时有 ii_high 和 ii_low）

| Sparsity | Gradient | 95% CI | p(g≤1) | n_paired |
|----------|----------|--------|--------|----------|
| s015 | 11.53 | [3.49, 23.78] | 0.0000 | 22 |
| s020 | 11.05 | [5.42, 69.27] | 0.0000 | 19 |
| s025 | 35.72 | [9.52, 101.54] | 0.0000 | 19 |
| s030 | 41.92 | [19.14, 299.76] | 0.0000 | 16 |

### Unpaired variant（独立重采样 high/low）

| Sparsity | Gradient | 95% CI | p(g≤1) | n_high | n_low |
|----------|----------|--------|--------|--------|-------|
| s015 | 12.69 | [4.96, 28.45] | 0.0000 | 43 | 24 |
| s020 | 27.60 | [6.55, 75.16] | 0.0000 | 42 | 21 |
| s025 | 36.38 | [13.19, 97.61] | 0.0000 | 42 | 21 |
| s030 | 39.28 | [21.87, 129.59] | 0.0000 | 40 | 20 |

所有 sparsity 下 p(g≤1) = 0.0000，gradient 显著大于 1（低重要性 phase 的 II 远高于高重要性 phase）。

### Crossover check（importance vs random）

- s025、s030 出现 crossover：importance 在 high phase 优于 random，但 mid/low phase random 更优
- s015、s020 无 crossover：random 在所有 phase 均优

---

## Part 3: JSON 结果文件

`/root/autodl-tmp/pacs/analysis/v6_analysis_results.json`

---
