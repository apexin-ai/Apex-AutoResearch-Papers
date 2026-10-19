# write related work expand

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_related-work-expand_20260515T031325_result.json`
- **Structured JSON:** [`8a57e271133b4bc08b0c.json`](../../sessions/8a/8a57e271133b4bc08b0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**扩展结果：20 → 32 独立引用**，分 4 个子节：

| 子节 | 引用数 | 新增 |
|------|--------|------|
| 2.1 Code Retrieval Methods | 10 | — (原有) |
| 2.2 Pre-trained Code Representations and Contrastive Learning | 14 | +7: CodeBERT, UniXcoder, CodeSage, SCodeR, InferCode, StarCoder2, Qwen2.5-Coder |
| 2.3 Hard Negative Mining | 7 | +2: STAR, RocketQA |
| 2.4 Code Structure Analysis (新) | 3 | +3: PDG, Joern/CPG, CodeQL |

新增子节 2.4 将 CodeQL、program dependence graph、code property graph 作为 StructFuse pipeline 的理论基础。Section 2.2 拆分为两部分：pre-trained code models 演进 + contrastive learning methods，并新增 decoder-only 模型段落（StarCoder2/Qwen2.5-Coder）呼应实验设置。Discussion 中的 6 个 inference-time graph methods 全部已在 2.1 中引用。

所有引用均经 WebSearch 验证 arXiv ID / 会议出处。`references.bib` 已创建，包含全部 32 条 bib 条目。

---
