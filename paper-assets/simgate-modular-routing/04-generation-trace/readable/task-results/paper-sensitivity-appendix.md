# paper sensitivity appendix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_sensitivity-appendix_20260521T005702_result.json`
- **Structured JSON:** [`aba2a290a32a8c7a7f96.json`](../../sessions/ab/aba2a290a32a8c7a7f96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

### 产出总结

**1. 添加的 LaTeX 内容**（main.tex 行 279-300，Cross-Model Verification 之后）

新增 `\section{DAF Sensitivity to Zero-Death Task Types}`，包含三模型对比表（Table `tab:daf-sensitivity`）：

| Model | DAF (11 tasks) | DAF (10 tasks) |
|-------|---------------|---------------|
| Qwen2.5-7B-Instruct | 90.4% [81.4, 99.1] | 100.0% [100.0, 100.0] |
| Llama-3.1-8B-Instruct | 88.2% [80.0, 95.1] | 97.0% [91.5, 100.0] |
| Gemma-2-9B-it | 89.7% [79.5, 98.4] | 99.9% [99.7, 100.0] |

所有数值通过 `scripts/daf_sensitivity_3model.py` 从原始 episode 数据独立计算验证（episode-level bootstrap, B=10,000, seed=42）。

**2. 数值一致性分析**

- **96.8% 不存在于论文中**。`0.9698` 是 Pearson r 值（main.tex:89），不是 DAF
- 主文 Qwen DAF=90.4% 与 cross-model 数据完全一致
- Gemma 有额外 task（boil, melt）和 40 条 find-non-living-thing episodes，标准化为 11 canonical tasks、20 eps/task 后 DAF=89.7%，与 analysis.json 一致
- 排除 find-non-living-thing 后三模型 DAF 均 ≥97%，CI 收窄

**3. 编译结果**

- **0 errors**
- 4 undefined refs：均为预存 `sec:experiments`（NLP checklist），非本次修改引入
- **17 pages**（主文 ≤8 页 + appendix + checklist，未改变主文长度）

---
