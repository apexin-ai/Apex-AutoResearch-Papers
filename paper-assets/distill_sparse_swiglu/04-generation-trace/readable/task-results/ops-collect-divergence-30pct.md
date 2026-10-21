# ops collect divergence 30pct

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-divergence-30pct_20260519T123938_result.json`
- **Structured JSON:** [`ff870ec7702c2f332589.json`](../../sessions/ff/ff870ec7702c2f332589.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在可用 MCP 工具列表中。artifact 文件已写入本地，跳过注册步骤。

结果汇总：

**30% Sparsity Mask Divergence (64 samples, 131K tokens)**

| 指标 | 30% Sparsity | 50% Sparsity |
|------|-------------|-------------|
| Mean Jaccard Distance | **46.26%** | **68.24%** |
| Min Layer Distance | 36.14% (L31) | — |
| Max Layer Distance | 60.01% (L27) | — |

关键发现：
- 30% sparsity 的 mask divergence 显著低于 50%（46.26% vs 68.24%），低约 22 个百分点
- **最稳定层**：Layers 15-18（中层）和 Layer 31（末层），Jaccard dist 36-39%
- **最不稳定层**：Layers 25-29（后层），Jaccard dist 54-60%
- KL sparsity 与 Jaccard distance 强相关（高 KL = 高 divergence）
- Neuron-level disagree rate (L16): 8.71%

Artifact 已写入 `artifacts/mask_divergence_30pct_64samples.md`。

---
