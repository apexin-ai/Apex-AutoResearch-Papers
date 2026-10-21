# analysis gee interaction

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gee-interaction_20260522T045522_result.json`
- **Structured JSON:** [`9459d7a4e59514b79c8b.json`](../../sessions/94/9459d7a4e59514b79c8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GEE Interaction Analysis 结果

### Interaction term (style × originality): OR [95% CI], p-value

| Judge | Axis | N | Interaction OR | 95% CI | p |
|---|---|---|---|---|---|
| GPT-4o | Formality | 88 | 0.661 | [0.183, 2.383] | 0.527 |
| GPT-4o | Verbosity | 86 | 1.269 | [0.371, 4.344] | 0.705 |
| GPT-4o | Register | 94 | 2.601 | [0.740, 9.148] | 0.136 |
| Qwen3-32B | Formality | 88 | 0.518 | [0.142, 1.891] | 0.320 |
| Qwen3-32B | Verbosity | 86 | 0.450 | [0.125, 1.616] | 0.221 |
| Qwen3-32B | Register | 94 | 0.555 | [0.148, 2.084] | 0.383 |
| Llama-70B | Formality | 88 | 0.968 | [0.248, 3.780] | 0.963 |
| Llama-70B | Verbosity | 86 | 1.103 | [0.340, 3.577] | 0.870 |

### 结论

**0/8 个 interaction term 达到显著**（所有 p > 0.13）。CI 全部宽且跨越 1.0，最接近显著的是 GPT-4o Register（OR=2.60, p=0.136）。Additive model（style + originality 无交互项）是充分的——style 和 originality 的效应独立叠加，不存在 style × originality 的调节效应。

---
