# code plan 010 llm rephrase fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-010-llm-rephrase-fix_20260517T010546_result.json`
- **Structured JSON:** [`3f0b85eee28cd4b31a7e.json`](../../sessions/3f/3f0b85eee28cd4b31a7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过：

- **Original binary F1 = 0.6918** — 在预期 ~0.69-0.70 范围内（主实验 Table 3 的 0.7014），确认 Bug 1 已修复
- **3-class multiclass F1 = 0.7385** — 合理范围，确认 Bug 2 已修复
- **Binary 不是 0.93** — 证明不再是 gen-0 vs gen-1+ 的 trivial task

结果：
| Condition | Binary F1 | Multiclass F1 |
|-----------|-----------|---------------|
| Original  | 0.6918 [0.6749, 0.7067] | 0.7385 [0.7269, 0.7496] |
| LLM Rephrased | 0.6471 [0.6308, 0.6619] | 0.6672 [0.6548, 0.6796] |
| Drop | -0.0447 | -0.0713 |

Edit distance ratio: 0.5071, avg 1.69 sentences replaced per text. Results saved to `llm_rephrase_results.json`.

---
