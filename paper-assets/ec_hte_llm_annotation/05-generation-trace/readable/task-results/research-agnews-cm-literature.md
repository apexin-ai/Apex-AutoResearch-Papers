# research agnews cm literature

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_agnews-cm-literature_20260524T152852_result.json`
- **Structured JSON:** [`bcf332d1ce5f78989f36.json`](../../sessions/bc/bcf332d1ce5f78989f36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/agnews_cm_literature.md`。

核心发现：
- **找到完整 4×4 confusion matrix**：arXiv:2506.18501 报告了 ChatGPT 和 DeepSeek 在 AG News 上的完整 CM（n=80）
- **主要混淆模式**：Business→World 是最大误分类方向（ChatGPT 45%误分），Sports 最容易（90-100% recall）
- **多精度级别**：弱 LLM ~80%、中 GPT-4 ~85%、强 GPT-4o/Claude ~88-91%，可构造不同强度的 CM
- **MNLI**：未找到标准 MNLI 的完整 CM，但从 FraCaS 数据确认 Neutral 是最难类别，已基于文献模式构造了推荐 CM
- **推荐方案**：直接使用 arXiv:2506.18501 的 CM 结构作为基础，按目标 accuracy 水平缩放误差率

---
