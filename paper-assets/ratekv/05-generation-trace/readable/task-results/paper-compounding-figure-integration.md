# paper compounding figure integration

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compounding_figure_integration_20260515T194603_result.json`
- **Structured JSON:** [`fc55477b5d257219272e.json`](../../sessions/fc/fc55477b5d257219272e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成了 `fig_compounding_curves.pdf`（三模型 compounding curves，symlog x + log y），并在 `experiments.tex` 中新增了 `\subsection{Cross-Architecture Compounding}`（§3.3，在 KIVI 段和 Downstream Evaluation 之间），包含：

- `Figure~\ref{fig:compounding_cross}` 引用新图
- 三条曲线的定量分析：Llama 在 k=256 爆到 1519（188×），Qwen 到 98.75（10.1×），Mistral 最抗打到 45.28（6.4×）
- 所有模型在 k≤8 时 PPL 增量 ≤2.5%，验证 cardinality constraint regime
- 各架构 compounding onset 阈值（Qwen ~32, Llama ~64, Mistral ~128），直接支撑 architecture-specific k selection

生成脚本在 `generate_compounding_curves.py`，artifact 已注册 (`art_20260515_dfb641`)。

---
