# ops bce 3lr eval now

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bce-3lr-eval-now_20260516T203844_result.json`
- **Structured JSON:** [`8486d8a56c4a237ce9a1.json`](../../sessions/84/8486d8a56c4a237ce9a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个 eval 成功完成。汇总结果：

| LR | BCE Loss | Sparsity | WikiText-2 PPL | vs KL (11.79) |
|----|----------|----------|---------------|---------------|
| 1e-4 | 0.7158 | 0.514 | **42.99** | +31.20 (3.6× worse) |
| 1e-3 | 0.6781 | 0.506 | **48.40** | +36.61 (4.1× worse) |
| 3e-3 | 0.6632 | 0.504 | **38.02** | +26.23 (3.2× worse) |

**结论：所有 BCE+Gumbel+Lagrangian PPL (38–48) 都远差于 KL baseline PPL=11.79。**

- 最好的 BCE (LR=3e-3, PPL=38.02) 仍比 KL 差 3.2×
- BCE loss 更低不等于 PPL 更好——LR=1e-3 的 BCE loss 最低之一但 PPL 最差
- 这有力证明了 **loss function 本身（BCE vs KL）是关键差异因素**，而非框架/训练设置差异

注意：LR=1e-4 的 model-level sparsity 为 0.469（所有层 0.500），而 LR=1e-3 有一层 (Layer 28) 为 0.000 导致 model-level 0.484。LR=3e-3 的 PPL 最优可能与其 sparsity 分布有关，需检查其 layer-wise 数据确认。

---
