# check cpi table7 missing data

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cpi_table7_missing_data_20260522T163614_result.json`
- **Structured JSON:** [`04623483456496133728.json`](../../sessions/04/04623483456496133728.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已找到。以下是结果报告：

---

## 报告

### 1. CPI 值全部存在

p75_ppl、p50_ppl、p25_ppl、mean_ppl 的 Avg CPI 值**均存在**于原始数据中，不是真正缺失：

| Feature | Avg CPI | Avg Rank | Boot Median | 95% CI |
|---------|---------|----------|-------------|--------|
| **p75_ppl** | 0.0628 | 3.1 | 3.1 | [2.8, 3.6] |
| **p50_ppl** | 0.0155 | 5.0 | 5.0 | [4.0, 6.7] |
| **p25_ppl** | 0.0119 | 5.8 | 5.8 | [4.2, 7.9] |
| **mean_ppl** | 0.0084 | 6.3 | 6.8 | [5.1, 8.6] |

### 2. Rank CI Width 数据

| Feature | CI Width |
|---------|----------|
| p75_ppl | 0.78 |
| p50_ppl | 2.67 |
| p25_ppl | 3.67 |
| mean_ppl | 3.44 |

### 3. Family-level 数据

| Family | Avg PI | Avg Rank |
|--------|--------|----------|
| surprisal | 0.0890 | 7.3 |
| perplexity | 0.0388 | 7.5 |
| lexical | 0.0043 | 9.7 |
| ngram_entropy | 0.0013 | 15.7 |
| repetition | 0.0007 | 16.5 |

### 4. 原始数据文件路径

- **汇总**: `/root/autodl-tmp/recursive_gen_depth_est/results/conditional_pi/summary.json`
- **Family 分组**: `/root/autodl-tmp/recursive_gen_depth_est/results/conditional_pi/family_grouped.json`
- **Bootstrap ranks**: `/root/autodl-tmp/recursive_gen_depth_est/results/conditional_pi/bootstrap_ranks.json`
- **Per-cell PI**: `/root/autodl-tmp/recursive_gen_depth_est/results/conditional_pi/per_cell_pi.json`
- **生成的 LaTeX**: `/root/autodl-tmp/recursive_gen_depth_est/results/conditional_pi/latex_table.tex`

**结论**：论文 Table 7 中的 "---" 不应存在——原始实验已计算出所有 19 个特征的完整 CPI 值。生成的 `latex_table.tex` 也包含这些值。问题可能出在论文手动编辑时遗漏了这些数据。

---
