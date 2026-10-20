# paper cohens d text update

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_cohens_d_text_update_20260514T092101_result.json`
- **Structured JSON:** [`762642f833e474a6f4b0.json`](../../sessions/76/762642f833e474a6f4b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clean. Here's the summary:

---

## 变更总览

### 数据来源
Per-problem paired Cohen's d (B=10000)，来自 `rebootstrap_b10000_results.json`。

**重要说明**: 新 bootstrap 只计算了 median_diff 的 CI，未单独计算 Cohen's d 的 CI。因此 Cohen's d 表的 CI 列改为展示 $\widetilde{\Delta}$（中位数差）及其 bootstrap CI。

### 各文件变更

| 文件 | 改动数 | 具体内容 |
|------|--------|----------|
| **results.tex** | 10处 | 表 caption 改为标注 $\widetilde{\Delta}$ CI；表头 `95% CI` → `$\widetilde{\Delta}$ [95% CI]`；4行表数据全部替换（d值+median_diff CI）；脚注加 "marginal at s=0.15"；3处正文 d 值更新（§5.4 + §5.5） |
| **abstract.tex** | 2处 | `0.44 (small) to 0.80 (large)` → `0.61 (medium) to 1.13 (large)`；`d > 0.5` → `d ≥ 0.72` |
| **introduction.tex** | 2处 | `d=0.44 (small) to d=0.80 (large)` → `d=0.61 (medium) to d=1.13 (large)`；`d > 0.5 ... d=0.28, CI spanning zero` → `d ≥ 0.72 ... d=0.37, marginal` |
| **conclusion.tex** | 2处 | `d=0.44 (small) to d=0.80 (large)` → `d=0.61 (medium) to d=1.13 (large)`；`d > 0.5` → `d ≥ 0.72` |
| **discussion.tex** | 0处 | 已有新值（line 29: 0.607, 0.725, 0.953, 1.126 / 0.371, 0.722, 1.233, 1.439） |
| **analysis.tex** | 0处 | 无 Cohen's d 引用 |
| **background/methodology/related_work** | 0处 | 无 Cohen's d 引用 |

### Cohen's d 表新数据 (Table 4)

| s | DS d | DS $\widetilde{\Delta}$ [CI] | QW d | QW $\widetilde{\Delta}$ [CI] |
|---|------|------|------|------|
| 0.15 | 0.61 (medium) | 0.32 [0.20, 0.47] | 0.37 (small)^ns | 0.05 [-0.01, 0.11] |
| 0.20 | 0.73 (medium) | 1.15 [0.66, 1.26] | 0.72 (medium) | 0.21 [0.07, 0.40] |
| 0.25 | 0.95 (large) | 3.97 [2.83, 5.29] | 1.23 (large) | 1.11 [0.61, 1.47] |
| 0.30 | 1.13 (large) | 9.94 [8.39, 16.65] | 1.44 (large) | 2.62 [1.72, 3.65] |

### Effect size 分类确认
- 旧 DeepSeek 范围 "small → large" → 新 "medium → large"
- 旧 Qwen s015 无标签 → 新 "small"（marginal）
- 所有分类标签已按 Cohen 标准更新（small < 0.5, medium 0.5–0.8, large ≥ 0.8）

---
