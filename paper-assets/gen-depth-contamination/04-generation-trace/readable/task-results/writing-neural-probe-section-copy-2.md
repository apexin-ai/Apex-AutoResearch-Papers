# writing neural probe section

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_neural-probe-section_20260514T083932_result.json`
- **Structured JSON:** [`4782afc81c3dadd2f371.json`](../../sessions/47/4782afc81c3dadd2f371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。在 `experiments_c1.tex` 末尾（第 343–402 行）新增 `\subsection{Representation Dependence of $\Kempirical$}`（`\label{sec:neural_probe}`），包含：

- **Setup**: frozen Qwen-1.5B → MLP probe 架构描述
- **Results**: 内联对比表（15D vs Neural 各 depth pair AUC），报告 K*(neural)=3（2v3 AUC=0.6195 > θ=0.60）
- **K\* hierarchy**: $K^*_{\text{theory}} \geq K^*_{\text{neural}} \geq K^*_{\text{15D}}$
- **Interpretability–discriminability tradeoff**: 15D (deployable, model-free) vs neural (theoretical exploration, 100x+ compute)
- **Caveats**: 2v3 边界仅 +1.95pp 超 θ，措辞全用 "preliminary"
- **3 个 TODO 占位符**：`% TODO(exp-015-rerun): Pythia/OLMo K*(neural) results here`、`bootstrap CIs`、`cross-model comparison table`

与 discussion.tex 中已有的 neural probe 讨论（引用 `Table~\ref{tab:s7_neural_probe}`、报告相同数值）保持一致。

---
