# analyze bce comp staged s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_bce_comp_staged_s42_20260515T182256_result.json`
- **Structured JSON:** [`d6c3c52fcd7edbdd013f.json`](../../sessions/d6/d6c3c52fcd7edbdd013f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

---

**实验 bce_comp_staged_s42 分析完成。**

核心结论：**Negative result — compensation 无法挽救 BCE 方案。**

| 指标 | BCE-only | BCE+comp | KL-only |
|------|---------|----------|---------|
| Per-token PPL | 27.96 | **25.44** | **9.21** |
| TEAL PPL | 44.54 | 44.54 | **12.08** |
| Sparsity | 0.496 | 0.558 | 0.498 |
| PPL↑ vs dense | 357% | 316% | 50% |

- Compensation 仅改善 ~9%（27.96→25.44），comp_loss 从 0.0053 下降到 0.0033 表明网络在学习但改善空间有限
- BCE+comp 仍比 KL-only 差 2.8 倍（25.44 vs 9.21）
- **Claim 1 强化**：KL distillation 通过端到端输出对齐隐式学到 neuron 重要性排序，BCE 将所有 neuron 等权对待是根本缺陷，compensation 只能做有限修补

---
