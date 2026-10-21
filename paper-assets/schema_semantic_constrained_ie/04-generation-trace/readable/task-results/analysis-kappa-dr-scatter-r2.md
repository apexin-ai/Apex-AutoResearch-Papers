# analysis kappa dr scatter r2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kappa_dr_scatter_r2_20260519T174039_result.json`
- **Structured JSON:** [`9833c18e7a08da98850b.json`](../../sessions/98/9833c18e7a08da98850b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出完成：

**文件**:
1. `artifacts/figures/kappa_vs_dr_scatter.pdf` / `.png` — scatter plot
2. `artifacts/figures/plot_kappa_dr_scatter.py` — 绘图脚本
3. `artifacts/figures/kappa_dr_data.json` — 原始数据
4. `artifacts/_project/report/kappa_dr_scatter_data.md` — 数据表

**核心发现**:
- 99 个有预测的 relation 点（7 SciERC + 92 DocRED），OLS R²=0.184, p=9.3e-6
- 跨数据集呈**负相关**（slope=−17.7）：SciERC 约束宽松（κ∈[0.03, 0.53]）但 DR 更高，DocRED 约束紧（κ∈[0.58, 0.97]）但 74/92 个关系 DR=0%
- 这是 **Simpson's paradox**：DocRED 的粗粒度 entity type（LOC/ORG/PER/...）让 LLM 的世界知识足以自然遵守 type 约束，即使无显式约束；SciERC 的细粒度学术 type（Task/Method/Material/...）更容易混淆
- 高 DR outlier：Evaluate-for (38.7%), Compare (35.0%), product/material (26.1%), subclass of (17.4%)

---
