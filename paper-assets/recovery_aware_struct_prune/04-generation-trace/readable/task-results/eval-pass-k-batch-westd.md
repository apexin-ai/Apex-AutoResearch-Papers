# eval pass k batch westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_pass_k_batch_westd_20260516T164155_result.json`
- **Structured JSON:** [`5288a56eb1b40a5a7376.json`](../../sessions/52/5288a56eb1b40a5a7376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验均已成功启动：

| exp_id | GPU | 模型 | 状态 |
|--------|-----|------|------|
| `eval_pass_k8_unpruned_qwen_math` | cuda:1 | grpo_unpruned_v2 | 已开始生成 (Pass@8 eval: 0/200) |
| `eval_pass_k8_rasp_20_sft_qwen_math` | cuda:2 | sft_qwen_math_rasp_20 | 模型加载中 (pruned MLP) |
| `eval_pass_k8_rasp_20_grpo_qwen_math` | cuda:3 | grpo_rasp_qwen_math | 模型加载中 (pruned MLP) |

PID: 25336 / 25437 / 25531。预计 ~30min 完成（200 prompts × 8 samples = 1600 generations/GPU）。

---
