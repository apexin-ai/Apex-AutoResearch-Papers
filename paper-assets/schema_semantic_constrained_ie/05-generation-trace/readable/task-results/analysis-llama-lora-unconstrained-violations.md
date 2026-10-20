# analysis llama lora unconstrained violations

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_lora_unconstrained_violations_20260515T174449_result.json`
- **Structured JSON:** [`303eebe08ee507851a2d.json`](../../sessions/30/303eebe08ee507851a2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是 LoRA fine-tuned vs base Llama unconstrained 对比：

| 指标 | Base Llama (unconstrained) | LoRA fine-tuned (unconstrained) | 变化 |
|------|-----|-----|-----|
| JSON Parse Rate | — | **100%** | — |
| ET violation | — | **0%** | — |
| RV violation | — | **0%** | — |
| **DR violation** | **13.3%** | **1.1%** | **↓ 12.2pp** |
| CF violation | — | **0%** | — |
| Entity F1 | 23.56% | **67.76%** | **↑ 44.2pp** |
| Entity P / R | — | 66.47% / 69.10% | — |
| Relation F1 | 2.68% | **45.45%** | **↑ 42.8pp** |
| Relation P / R | — | 43.20% / 47.95% | — |

**关键发现：** LoRA fine-tune 效果极其显著——DR violation 从 13.3% 降至 1.1%（↓92%），Entity F1 从 23.56% 跃升至 67.76%，Relation F1 从 2.68% 跃升至 45.45%。

剩余的 12 个 DR violation 主要集中在 Hyponym-of (4)、Evaluate-for (3)、Feature-of (2) 三种关系类型上，属于模型对少数复杂 type pair 约束的边缘错误。这说明即使 fine-tune 后仍有 1.1% 残余 DR violation，OntoCoDec constrained decoding 在 fine-tuned Llama 上仍有 composability 价值。

---
