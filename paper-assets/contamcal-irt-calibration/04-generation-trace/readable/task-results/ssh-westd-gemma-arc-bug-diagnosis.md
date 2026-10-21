# ssh westd gemma arc bug diagnosis

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-gemma-arc-bug-diagnosis_20260519T095919_result.json`
- **Structured JSON:** [`0d88d19c72fcd1be516f.json`](../../sessions/0d/0d88d19c72fcd1be516f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diff 确认改动正确。两处改动：
1. `evaluate_mcq`（line 211-213）
2. `evaluate_paraphrased`（line 497-499）

逻辑：当 tokenizer 有 chat_template 时，mc_suffix（"The answer is "）从 user turn 移到 model turn 开头。logprob 在 "The answer is " 之后取，这是正确的答案完成位置。

---

## 完整诊断报告

### 1. 根因分析

**Bug**: `evaluate_mcq` 中，logprob-based eval 使用 chat template 时，prompt 格式为：

```
&lt;start_of_turn>user
[25-shot fewshot]...The answer is &lt;end_of_turn>
&lt;start_of_turn>model\n   ← compute_choice_logprobs 在此取 logits
```

`compute_choice_logprobs()` 在最后一个 token 位置（`model\n` 之后）取 logits。在这个位置，模型处于 "response generation mode"，对 token "A" 有系统性先验（logprob ~-3.0），而其他选项 logprob 极低（-5 到 -12）。导致 ARC 25-shot（1990 tokens）时 97.9% 预测 "A"。

**为什么仅 d005 受影响**:
- d005 的 5% contamination SFT 数据包含 MCQ 格式（user:question, assistant:"The answer is X."），强化了模型在 model turn 开始位置的 chat 行为。但 5% contamination 不足以让模型学会正确回答 ARC 题目。
- d000（0%）的 LoRA 影响较弱，model turn 位置仍能传递 fewshot 信号
- d025/d050（25%/50%）有足够多的 contaminated ARC 题目覆盖了位置偏差

**为什么 MMLU 不受影响**: 5-shot MMLU 仅 328 tokens，prompt 短到模型在 model turn 位置仍能区分选项。ARC 25-shot 的 1990 tokens 使信号稀释，默认 A 先验主导。

### 2. 修复方案

已在 evaluate.py 中修改两处（`evaluate_mcq` 和 `evaluate_paraphrased`）：当 tokenizer 有 chat_template 时，将 "The answer is " 从 user turn 移到 model turn 开头。

**验证结果**（d005 模型，前 10 个 ARC 题）：
- Buggy: **1/10** correct
- Fixed: **8/10** correct
- No chat template: **8/10** correct

### 3. 影响范围

- **ARC-Challenge**: d005 从 ~22.95% 恢复到正常水平（预期 ~75-80%）
- **MMLU**: 可能轻微变化（已经正常，但 logprob 位置更准确可能改善几个百分点）
- **其他 model family**: 同样受益（logprob 位置更准确），但变化可能很小因为它们已经能正常工作
- **Generation-based eval**: 不受影响

### 4. 重跑计划

需要重跑的评估（按优先级）：
1. **Gemma-2-9B d005** ARC + MMLU（验证修复）
2. **Gemma-2-9B d000/d025/d050/d100** ARC + MMLU（确保一致性）
3. 其他 model family（Qwen, Phi, OLMo）的 ARC + MMLU（可选，因为 logprob 位置改变可能影响结果）

---
