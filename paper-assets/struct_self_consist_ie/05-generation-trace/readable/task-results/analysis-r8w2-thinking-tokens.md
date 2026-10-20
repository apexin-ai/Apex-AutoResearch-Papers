# analysis r8w2 thinking tokens

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r8w2_thinking_tokens_20260515T224012_result.json`
- **Structured JSON:** [`a6c299a2fdcb7bc85619.json`](../../sessions/a6/a6c299a2fdcb7bc85619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `output/review_round8/r8w2_thinking_token_analysis.json`。

结果：

| | SciERC 4B | CoNLL 4B |
|---|---|---|
| instances | 551 | 3,453 |
| mean tokens | 213 | 59 |
| thinking ratio | 2.34% | 8.49% |
| median LP shift | 0.0015 nats | 0.000007 nats |
| selection changed | 8/551 (1.5%) | 0/3,453 (0.0%) |

**Method B**（无 per-token logprobs）。没有 Qwen3-8B SciERC 数据，用 Qwen3-4B CoNLL 作对比。

**结论**：Thinking tokens 的 LP 稀释效应可忽略（< 3% of LP range）。CoNLL 无 thinking tokens 但 LP 压缩更强（tied=95.8% vs SciERC 60.3%），直接排除 thinking tokens 是 LP 压缩的成因。累积 LP 排序完全不受影响（constant offset）。

---
