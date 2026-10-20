# analysis eval humaneval 1p5b cka only

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_1p5b_cka_only_20260519T132640_result.json`
- **Structured JSON:** [`3c946e64ca53989b972c.json`](../../sessions/3c/3c946e64ca53989b972c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1.5B CKA-only HumanEval @2048 结果

| 指标 | SFT CKA-only 20% 1.5B | GRPO CKA-only 20% 1.5B |
|------|----------------------|------------------------|
| **pass@1** | **0.61%** (1/164) | **0.00%** (0/164) |
| stderr | ±0.0061 | ±0.0000 |
| avg_response_length | 1968.8 | 1977.7 |
| median_response_length | 2048.0 | 2048.0 |
| wall_clock | ~97 min | ~97 min |
| EXIT_CODE | 0 | 0 |

## 严重问题：模型输出自然语言而非代码

两个模型几乎所有 164 题都产生 **SyntaxError**——生成的不是 Python 代码，而是自然语言描述（"The function checks if..."、"Okay, I need to write..."）。median_response_length = 2048 说明绝大多数 sample 都撞了 max_tokens 上限还在输出文本，没有产生有效代码。

SFT 唯一通过的 1 题可能是碰巧生成了可执行片段。GRPO 则 0/164 全军覆没。

## 1.5B vs 7B 对比

| 方法 | 7B pass@1 | 1.5B pass@1 | 差距 |
|------|-----------|-------------|------|
| CKA-only SFT | 20.12% (33/164) | 0.61% (1/164) | -19.51pp |
| CKA-only GRPO | 20.12% (33/164) | 0.00% (0/164) | -20.12pp |

1.5B CKA-only 模型在 HumanEval 上实质性地丧失了代码生成能力。7B 的 CKA-only 至少还保留了约 20% pass@1，1.5B 直接退化为自然语言输出模式。这说明 **1.5B 模型在 20% 结构化剪枝 + CKA-only 恢复后，代码能力完全崩溃**——模型容量不足以在剪枝后仅靠 CKA alignment 恢复编程技能。SFT/GRPO 微调也未能挽救。

---
