# analysis d073 probe status and figures

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-probe-status-and-figures_20260516T034350_result.json`
- **Structured JSON:** [`7b2e6f8b83fffc8cedab.json`](../../sessions/7b/7b2e6f8b83fffc8cedab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 valid PDFs, sizes match the server exactly.

---

## 进度报告

### Part A: Probe 状态

| 实验 | 状态 | 进度 | 预计完成 |
|------|------|------|----------|
| **d073-probe-bge-m3** | **DONE** | 100% | 已完成 |
| **d073-probe-e5-large** | RUNNING | Embedding 76% (114K/150K) | ~35 min embedding + ~10 min training |

**BGE-M3 结果：**

| 指标 | SWE In-Domain | Cross-Agent OH |
|------|--------------|----------------|
| Macro F1 | 0.941 | **0.666** |
| Accuracy | 0.953 | 0.724 |
| F1 (stagnation) | 0.915 | 0.527 |
| F1 (progress) | 0.968 | 0.806 |

- BGE-M3 cross-agent F1=0.666 vs Qwen3 cross-agent F1=0.598 → **+6.8pp**
- Registry 已更新为 DONE/success，metrics 已写入

### Part B: 论文图表

4 张 PDF 全部从服务器拉到本地 `figures/` 目录：

| 图 | 路径 | 大小 |
|----|------|------|
| Pareto Curve | `figures/pareto_curve.pdf` | 20KB |
| SHAP Feature Importance | `figures/d073/shap_feature_importance.pdf` | 230KB |
| Trajectory Visualization | `figures/d073/trajectory_visualization.pdf` | 26KB |
| Reliability Diagrams | `figures/d073/reliability_diagrams.pdf` | 20KB |

Reliability diagram 已存在于服务器（4 个子图 + 1 个合并图），无需重新生成。校准数据确认：GB silver ECE=0.003, gold ECE=0.114; RF silver ECE=0.005, gold ECE=0.156。

---
