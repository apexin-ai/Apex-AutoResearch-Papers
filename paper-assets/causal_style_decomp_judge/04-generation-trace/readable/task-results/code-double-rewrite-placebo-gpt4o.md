# code double rewrite placebo gpt4o

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_double_rewrite_placebo_gpt4o_20260521T132448_result.json`
- **Structured JSON:** [`1b8a38006620d16ceae6.json`](../../sessions/1b/1b8a38006620d16ceae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果已保存到 `data/double_rewrite_placebo_gpt4o.json`。

## 结果

| | Formality | Verbosity |
|---|---|---|
| n_pairs (nli_dr≥0.90) | 81 | 43 |
| n_consistent | 44 | 32 |
| n_ties (inconsistent) | 37 (45.7%) | 11 (25.6%) |
| BT original wins | 14/44 = **31.8%** | 2/32 = **6.2%** |
| 95% CI | [18.2%, 45.5%] | [0%, 15.6%] |
| p-value | 0.0226 | ≈0 |
| Placebo | **FAILED** | **FAILED** |

GPT-4o 在两个轴上都显著偏离 50%，强烈偏好 double_rewrite 文本而非 original。Verbosity 尤其极端（仅 6.2% original wins）。这表明 GPT-4o 作为 judge 对 rewriting artifacts 存在系统性偏好——经过两轮改写的文本被认为"更好"，即使 style 和语义与原文一致。

---
