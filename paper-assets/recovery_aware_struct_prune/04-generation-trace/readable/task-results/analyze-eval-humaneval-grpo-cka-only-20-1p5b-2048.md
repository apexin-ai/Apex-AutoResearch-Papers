# analyze eval humaneval grpo cka only 20 1p5b 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_humaneval_grpo_cka_only_20_1p5b_2048_20260519T132652_result.json`
- **Structured JSON:** [`084d2954bcd026586502.json`](../../sessions/08/084d2954bcd026586502.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **pass@1: 0.0%**
- **n_correct: 0**
- **n_total: 164**
- **W&B run_id**: 无（日志中未提及 W&B）

**严重问题 — 模型输出全是自然语言，不是代码：**

所有 164 题全部 SyntaxError。模型没有生成 Python 代码，而是输出 chain-of-thought 式的自然语言推理文本（如 "Okay, I need to write a Python function..."、"The function checks if..."），直到撞上 `max_tokens=2048` 截断，从未产出可执行代码。

- **avg_response_length**: 1977.7 tokens
- **median_response_length**: 2048 tokens（即绝大多数响应都被截断）

这说明 GRPO + CKA-only 20% 剪枝后的 1.5B 模型的 code generation 能力已完全丧失，模型退化为纯文本推理模式。

**路径信息：**
- checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b`
- results JSON: `/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_1p5b_2048.json`
- log: `~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log`

---
