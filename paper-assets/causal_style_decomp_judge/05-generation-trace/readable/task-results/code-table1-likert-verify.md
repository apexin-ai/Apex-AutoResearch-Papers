# code table1 likert verify

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_table1_likert_verify_20260524T051619_result.json`
- **Structured JSON:** [`c9559be129248fff8c3b.json`](../../sessions/c9/c9559be129248fff8c3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果汇总：

**产出文件**：
- 脚本：`/root/causal_style_decomp_judge/analysis/compute_table1_likert.py`
- CSV：`/root/causal_style_decomp_judge/analysis/table1_verified.csv`

**关键发现**：
- Llama-70B register 有 1 条 `score_counterfactual: null` 记录，已跳过（94→93）
- 所有 13 个 judge×axis 组合的 Cohen's d 均非常小（|d| < 0.10），效应量可忽略
- 所有 Wilcoxon p-value 远大于 0.05（最小 0.28），无统计显著性

| Judge | Axis | N | Cohen's d | Wilcoxon p |
|---|---|---|---|---|
| GPT-4o | formality | 88 | -0.04 | 0.91 |
| GPT-4o | verbosity | 86 | 0.05 | 0.40 |
| GPT-4o | register | 94 | 0.00 | 0.78 |
| Qwen3-32B | formality | 88 | -0.05 | 0.46 |
| Qwen3-32B | verbosity | 86 | 0.04 | 0.39 |
| Qwen3-32B | register | 94 | -0.07 | 0.37 |
| Llama-70B | formality | 88 | 0.01 | 0.53 |
| Llama-70B | verbosity | 86 | 0.02 | 0.28 |
| Llama-70B | register | 93 | 0.02 | 0.52 |
| Gemini-Flash | formality | 88 | -0.08 | 0.31 |
| Gemini-Flash | verbosity | 86 | 0.05 | 0.37 |
| Claude | formality | 88 | -0.02 | 0.72 |
| Claude | verbosity | 86 | -0.04 | 0.74 |

---
