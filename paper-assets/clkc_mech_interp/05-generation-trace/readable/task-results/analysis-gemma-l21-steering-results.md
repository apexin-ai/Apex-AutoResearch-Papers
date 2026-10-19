# analysis gemma L21 steering results

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma-L21-steering-results_20260522T172754_result.json`
- **Structured JSON:** [`d5bf3ac34971b98e8ba9.json`](../../sessions/d5/d5bf3ac34971b98e8ba9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，`steering_107_gemma_L21` → **DONE (negative)**。

结果摘要：

| alpha | steering_flips | control_flips | p2c | c2p | Fisher p |
|-------|---------------|---------------|-----|-----|----------|
| -20 | 5 | 6 | 0 | 0 | 1.0 |
| -10 | 2 | 2 | 0 | 0 | 1.0 |
| -5 | 2 | 1 | 0 | 0 | 1.0 |
| +5 | 1 | 3 | 0 | 0 | 0.623 |
| +10 | 1 | 2 | 0 | 0 | 1.0 |
| +20 | 5 | 4 | 0 | 0 | 1.0 |

Probe accuracy 0.763, n=158。零方向性 flip，所有 alpha 无显著效应。与预期一致——L17 + L21 双层 negative，确认 Gemma steering 失败，与 Qwen 模式一致，steering 因果效应为 Llama-specific。

---
