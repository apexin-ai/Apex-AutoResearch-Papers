# paper cka figures

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_cka-figures_20260515T055352_result.json`
- **Structured JSON:** [`f6ce26943f6726fc7cb7.json`](../../sessions/f6/f6ce26943f6726fc7cb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**产出**

| 文件 | 路径 | 大小 |
|------|------|------|
| Fig A: Per-layer overlap bar chart | `results/figures/cka_per_layer_overlap.pdf` | 21K |
| Fig B: CKA heatmap (2×2) | `results/figures/cka_heatmap.pdf` | 32K |
| 绘图脚本 | `src/plot_cka_figures.py` | — |

**数据要点**

- **MLP overlap 全局偏高**（0.89–0.99），各层 neuron group 间 CKA 相似度极高，说明 MLP 内部冗余度大，剪枝空间充足
- **Attention overlap 变化明显**：浅层低（layer 0: 0.53），中深层高（layer 13: 0.86, layer 18: 0.86），表明中深层 attention head 间功能重叠严重
- **Top-3 高 overlap 层**（▼ 标注）：集中在中间层，这些是优先剪枝候选
- **Heatmap 对比**：高 overlap 层的 attention CKA 矩阵整体偏红（head 间高度相似），低 overlap 层则有明显的 head 分化（off-diagonal 值低）

---
