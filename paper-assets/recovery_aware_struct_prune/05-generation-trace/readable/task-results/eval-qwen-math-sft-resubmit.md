# eval qwen math sft resubmit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen_math_sft_resubmit_20260520T112958_result.json`
- **Structured JSON:** [`c6bbabcb65c5efd72829.json`](../../sessions/c6/c6bbabcb65c5efd72829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在加载模型中，一切正常。

**提交完成：**

| 实验 | GPU | PID | tmux session | max_new_tokens |
|------|-----|-----|-------------|----------------|
| `eval_gsm8k_sft_qwen_cka_only_20` | cuda:0 | 18038 | eval_gsm8k_sft_qwen_cka_only_20 | 2048 |
| `eval_gsm8k_sft_qwen_standard_20` | cuda:1 | 18114 | eval_gsm8k_sft_qwen_standard_20 | 2048 |

两个实验 registry 状态已更新为 RUNNING。加了 `--max_new_tokens 2048` 限制生成长度，预计 N=200 在 30-60 分钟内完成（而非之前的 13-17 小时）。

---
