# code correction poc debiased prompt

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_correction_poc_debiased_prompt_20260521T084611_result.json`
- **Structured JSON:** [`fe0b38e8e872f6515c31.json`](../../sessions/fe/fe0b38e8e872f6515c31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇报：

## Correction PoC: Debiased Prompt

### Qwen3-32B
| | P(formal) | 95% CI | p-value |
|---|---|---|---|
| Original | 66.5% | [58.5, 73.9] | p<0.0001 |
| Debiased | 60.8% | [53.4, 68.2] | p=0.0023 |
| **Reduction** | **5.7pp** | | **(34.5% of bias eliminated)** |

### GPT-4o
| | P(formal) | 95% CI | p-value |
|---|---|---|---|
| Original | 63.0% | [55.7, 70.3] | p=0.0004 |
| Debiased | 62.6% | [55.9, 69.3] | p<0.0001 |
| **Reduction** | **0.4pp** | | **(3.1% of bias eliminated)** |

附加观察：GPT-4o 在 debiased prompt 下有 5 个 trial 返回 "Neither"（拒绝选择），说明它能意识到内容等价但仍然在被迫选择时偏向 formal。

### Interpretation
**Ineffective** — debiased prompt 对两个 judge 的 formality bias 均无法消除：
- Qwen3-32B: 偏差下降 5.7pp（从 66.5→60.8%），但仍高度显著（p=0.0023），仅消除 34.5% 的 bias
- GPT-4o: 几乎无变化（0.4pp），bias 完全持续

**结论：formality bias 比 prompt-level intervention 更深层。** 这支持论文 C4 claim — simple prompt debiasing 不足以矫正 style preference，需要更 structural 的方法（如 CSD decomposition）。

输出文件：
- `data/pairwise_results_debiased_qwen32b_formality.jsonl`
- `data/pairwise_results_debiased_gpt4o_formality.jsonl`

---
