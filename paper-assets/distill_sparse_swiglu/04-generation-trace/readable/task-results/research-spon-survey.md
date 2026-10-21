# research spon survey

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_spon-survey_20260515T103818_result.json`
- **Structured JSON:** [`5bfe57bffbe0d199090a.json`](../../sessions/5b/5bfe57bffbe0d199090a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研结果已写入 `memory.md`。核心发现总结：

**SPON**:
- 论文 "Resting Neurons, Active Insights" (arXiv 2512.12744)，每层注入 1 个 learnable input-independent bias vector 作为稀疏化后的 representational anchor
- 用 **KL divergence** (distribution matching) 训练，完成后 bias 可吸收进模型权重，**零推理开销**
- 50% sparsity 下一致优于 TEAL baseline
- 截至今日未找到公开代码仓库，具体超参数需阅读全文

**竞品格局**:
- DejaVu/PowerInfer/TurboSparse 用 **BCE** 训练 predictor，我们用 **KL** 是核心差异化
- ProSparse/TurboSparse 需替换激活函数，我们**保留 SwiGLU** 是优势
- MaskLLM 用 **Gumbel Softmax** 做 differentiable mask sampling，验证了 Gumbel 方向可行性

**Phase 2 组合路径**: KL Predictor 决定 mask → SPON bias vectors 补偿误差，两者互补，SPON 训练成本极低（每层仅 hidden_dim 个参数）。

---
