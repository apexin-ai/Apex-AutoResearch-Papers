# paper mistral consistency fix

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_mistral-consistency-fix_20260519T055808_result.json`
- **Structured JSON:** [`85376683c5ba4b156be9.json`](../../sessions/85/85376683c5ba4b156be9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 dash 引入。

### 修改摘要

| # | 文件 | Before | After |
|---|------|--------|-------|
| 1 | experiments.tex:228 | "KL's downstream advantage is consistent: HS +8.8pp, ARC +9.0pp, WG +5.6pp" | "KL outperforms TEAL on 5 of 6 downstream tasks … GSM8K is the sole reversal (11.1% vs. 15.9%, Table ref)" |
| 2 | abstract.tex:6 | "Both PPL and downstream advantages hold across architectures (Mistral-7B: ARC +9.0pp, WG +5.6pp)" | "PPL and downstream advantages hold on most tasks … KL wins 5 of 6 … GSM8K reverses" |
| 3 | introduction.tex:16 | "both PPL and downstream advantages hold (ARC +9.0pp, WG +5.6pp)" | "KL wins on PPL and 5 of 6 downstream tasks … GSM8K reverses" |
| 4 | limitations.tex:5 | (无 Mistral GSM8K 段落) | 新增 Mistral GSM8K 反转讨论段落，插入在 Qwen-14B MMLU 段之前 |
| 5 | appendix.tex:364 | "generalizes across architectures." | "generalizes on 5 of 6 tasks; GSM8K is the sole reversal." |
| 6 | ethics.tex:3 | benchmark 列表缺 HellaSwag/PIQA | 添加 HellaSwag, PIQA |
| 7 | ethics.tex:32 | few-shot 列表缺 HellaSwag/PIQA | 添加 HellaSwag 10-shot, PIQA 0-shot |

编译通过，0 errors，无 em-dash/en-dash。

---
