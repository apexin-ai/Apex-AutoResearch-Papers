# code llm rephrase fix resume

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llm-rephrase-fix-resume_20260517T005911_result.json`
- **Structured JSON:** [`dd841109cc79a31d6778.json`](../../sessions/dd/dd841109cc79a31d6778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

| Condition | Binary F1 | CI | Multiclass F1 |
|-----------|-----------|-----|---------------|
| Original | 0.9343 | [0.926, 0.942] | 0.4739 |
| LLM Rephrased | 0.7118 | [0.694, 0.730] | 0.3301 |

**关键发现**：
- Binary F1 下降 -0.2225 (23.8% 相对下降)
- LLM rephrase binary F1 = 0.7118 > random 5% replacement 的 0.6496
- 但 LLM rephrase 造成的绝对下降（-0.2225）远大于 5% random replacement（-0.0457）

这和预期相反：LLM rephrase 虽然保持了更高的绝对 F1（0.712 vs 0.650），但因为 edit distance 更大（avg ratio = 0.507，即改了约 50% 的文本），实际扰动量远超 5% random replacement。这说明 LLM rephrase 是更激进的攻击，但 depth fingerprint 仍保持了 0.71+ 的检测能力。

---
