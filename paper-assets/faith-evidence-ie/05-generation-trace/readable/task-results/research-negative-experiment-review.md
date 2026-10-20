# research negative experiment review

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_negative_experiment_review_20260517T035208_result.json`
- **Structured JSON:** [`57fb9fb9fa57cb8a2afb.json`](../../sessions/57/57fb9fb9fa57cb8a2afb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/negative_review.md` 并注册 (art_20260517_c9070e)。

核心发现：
- **Group 1-3 (GRPO)**: 全线失败的真正根因是 QLoRA quantization（D052 最终确认，bf16 vs QLoRA Δ=+23.8pp），当时 lr sweep 浪费了约 12h
- **Group 4 (DPO)**: 1ep 中性 / 3ep 退化，pair 构造策略（基于 CED 而非 rel_f1）可能是根因
- **Group 2**: 三路 reward ablation 证明 CED 是 GRPO 唯一可用的 reward signal

3 条被忽视的改进线索：
1. **推理时 CED Reranking** — 无训练成本，直接过滤 distractor citations 提升 EDCR
2. **RSFT → bf16 GRPO 两阶段** — RSFT 稳 rel_f1 基础 + GRPO 在线优化 evidence 质量
3. **rel_f1-based DPO pair 构造** — 当前 CED pairs 只教 evidence 偏好，改用 F1 pairs 可能使 DPO 直接提升关系抽取

---
