# analysis plan 015 auth scope direction

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_015_auth_scope_direction_20260521T105822_result.json`
- **Structured JSON:** [`6c721da71afc62ea2438.json`](../../sessions/6c/6c721da71afc62ea2438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，artifact 已注册 (`art_20260521_8c7e5d`)。

**结果摘要：**

| Model | n | Escalation | Rate |
|-------|---|-----------|------|
| GPT-4.1 | 23 | 19 | 82.6% |
| GPT-5.4 | 32 | 23 | 71.9% |
| DeepSeek-V3 | 30 | 20 | 66.7% |
| Qwen3-235B | 13 | 7 | 53.8% |
| Claude Sonnet 4.6 | 6 | 3 | 50.0% |
| **Pooled** | **104** | **72** | **69.2%** |

- Binomial test: p = 5.5×10⁻⁵（显著 > 50%）
- Conservative refusal: **0 例**（所有模型均为 0）
- 4/5 模型 escalation 占多数（Claude Sonnet 恰好 50% 但 n=6 样本太小）

核心发现：authorization scope 违规完全没有"过度拒绝"方向，要么是 escalation（69.2%），要么是 assumption_based_action/scope_misapplication 等非方向性错误（30.8%）。这比单纯的 escalation > restriction 更强——restriction 根本不存在。

---
