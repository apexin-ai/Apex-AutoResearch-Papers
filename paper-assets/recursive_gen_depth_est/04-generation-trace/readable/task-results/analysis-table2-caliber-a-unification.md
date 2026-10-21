# analysis table2 caliber a unification

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table2_caliber_a_unification_20260518T170347_result.json`
- **Structured JSON:** [`e1d3b440cb07a65735ef.json`](../../sessions/e1/e1d3b440cb07a65735ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已写入。以下是完整对照表和口径确认。

---

## 完整对照表

| Cell | 旧Table2 4class | Battery 4class | 差值(pp) | 旧d1-d3括号 | Battery d1-d3 BA | 差值(pp) |
|------|:-:|:-:|:-:|:-:|:-:|:-:|
| pythia_nucleus | 78.2 | 78.1 | -0.1 | 71.2 | 70.9 | -0.3 |
| pythia_temp09 | 76.3 | 76.8 | +0.5 | 70.6 | 69.1 | -1.5 |
| pythia_topk50 | 69.6 | 68.7 | -0.9 | 58.8 | 58.4 | -0.4 |
| olmo_nucleus | 78.8 | 78.8 | 0.0 | 75.0 | 72.1 | -2.9 |
| olmo_temp09 | 82.0 | 82.7 | +0.7 | 76.3 | 77.0 | +0.7 |
| olmo_topk50 | 74.2 | 73.7 | -0.5 | 66.1 | 65.1 | -1.0 |
| gpt2xl_nucleus | 83.3 | 84.0 | +0.7 | 79.0 | 78.9 | -0.1 |
| gpt2xl_temp09 | 85.4 | 85.3 | -0.1 | 82.6 | 80.5 | -2.1 |
| gpt2xl_topk50 | 76.6 | 75.4 | -1.2 | 69.5 | 67.7 | -1.8 |
| **均值** | **78.27** | **78.16** | **-0.1** | **72.12** | **71.09** | **-1.0** |

## d1-d3 均值验证

Battery 9 cells d1-d3 BA 均值 = **71.09%** → 与 Abstract 的 71.1% 一致 ✓

旧 Table 2 括号均值 = **72.12%** → 与 Abstract 的 71.1% 不一致（差 1.0pp）

## 口径确认 — 严重问题

**当前 all_results.json（battery 数据）实际配置：**

| 参数 | 论文 caption 声称 | 代码实际 | 口径 A 目标 |
|------|:-:|:-:|:-:|
| 交叉验证 | 5-fold CV | **单次 70/15/15 split** | 5-fold CV |
| RF trees | 200 | **100** (`_make_baseline` line 836) | 200 |
| StandardScaler | 未说明 | **是** (line 595) | 无 |
| 数据量 | 未说明 | 20000样本/cell, 750/class test | - |

`d1d3_balanced_acc.json` 中 `"classifier": "RandomForest (n_estimators=200)"` 是 `compute_reviewer_metrics.py` 中的**硬编码字符串**，与实际代码不符。

**结论：旧 Table 2 和 battery 数据都不是口径 A。要统一到口径 A 需要重新跑实验：5-fold CV、200 trees、去掉 StandardScaler。**

JSON 已保存至 `results/reviewer_metrics/table2_caliber_a_comparison.json`。

---
