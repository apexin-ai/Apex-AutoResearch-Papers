# research kl distill literature

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_kl-distill-literature_20260515T142708_result.json`
- **Structured JSON:** [`3edb446759df955475e7.json`](../../sessions/3e/3edb446759df955475e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研完成。`literature_map.yaml` 已写入，包含 20 篇论文，覆盖 4 个方向。

**核心发现：我们的工作有明确的 novelty gap。**

1. **KL for sparsity predictor training**: 无先例。现有 predictor（DejaVu, ShadowLLM）用 BCE；SPON 用 KL 但训练 bias correction 而非 predictor；其余方案（TEAL, CATS, R-Sparse, SVD-CSP）是 training-free。

2. **Output distribution preservation**: Minitron (NeurIPS 2024) 验证 logit-only KL 优于 intermediate matching；SPON (ICML 2026) 用 KL 做 dense/sparse distribution matching——两者都支持我们"KL 优于 BCE"的核心假设。

3. **SPON**: 最接近的竞争者，但 SPON 是 input-independent 的全局 bias correction，我们是 input-dependent 的 per-token predictor，更灵活。

4. **Predictor-based sparsity**: 关键 competitor 是 DIP（MLSys 2025），其结论是 SwiGLU sparsity pattern 难以预测所以放弃 predictor。我们需要用 KL-trained predictor 证明这个结论可以被推翻。

**Related work 定位建议**: 论文中应重点对比 TEAL (baseline)、DejaVu/ShadowLLM (BCE predictor)、SPON (KL bias)、DIP (predictor-free SwiGLU)。

---
