# review related work completeness

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_related-work-completeness_20260524T023100_result.json`
- **Structured JSON:** [`d83caf6fea12ced1e6cb.json`](../../sessions/d8/d83caf6fea12ced1e6cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。报告已写入 `artifacts/related_work_review.md`。

核心发现：

**P0 建议补充 4 篇**：
1. Conformal prediction for NER（arXiv 2601.16999）— 与本文 QE + selective prediction 直接互补
2. Inference-aware fine-tuning for BoN（ICLR 2025）— 训练端优化 BoN 的互补方向，reviewer 可能质疑
3. Beyond majority voting（EMNLP 2025）— 聚合理论框架，与 entity-level voting 直接相关
4. Assessment of generative NER（arXiv 2601.17898）— 生成式 NER 系统评估，与实验设置对应

**主要不足**：缺少训练端 BoN 优化的对比视角、NER 不确定性量化最新进展未覆盖、bib 中 `muennighoff2025s1` 已存在但正文未引用。

---
