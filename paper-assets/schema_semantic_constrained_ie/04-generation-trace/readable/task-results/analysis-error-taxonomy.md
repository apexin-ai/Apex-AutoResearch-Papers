# analysis error taxonomy

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error_taxonomy_20260519T151303_result.json`
- **Structured JSON:** [`42359582c0abaaf32e76.json`](../../sessions/42/42359582c0abaaf32e76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/report/error_taxonomy_analysis.md`。

核心发现：

- **Tokenizer collision = 0%**（所有配置）：S1 constrained decoding 完全消除了 token 级别的约束违规
- **SciERC 以 Non-local CF 为主**（63–88%）：宽松 schema 下 DR 违规少，主要问题是跨 triple 类型不一致（TCR 可解决）
- **DocRED Qwen 以 Semantic Confusion 为主**（64%）：模型选了合法类型但 (head_type, tail_type) pair 不满足 DR 约束
- **DocRED Llama 以 Fundamental Schema Conflict 为主**（63%）：entity 参与的多个 relation 的 DR 约束互相矛盾，无任何单一类型可满足——这是不可消除的理论上限
- SC 可通过增强 S1（加入 DR pair 约束）消除；NL-CF 已被 TCR 消除；FSC 是 schema 固有限制，不可消除

---
