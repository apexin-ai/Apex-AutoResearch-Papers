# eval qwen math gsm8k both

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen_math_gsm8k_both_20260520T105041_result.json`
- **Structured JSON:** [`81a9723b9df6e19a5456.json`](../../sessions/81/81a9723b9df6e19a5456.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张 GPU 已经在跑 GSM8K 评估：

| GPU | PID | 模型 | 状态 |
|-----|-----|------|------|
| cuda:0 | 14641 | `sft_qwen_math_cka_only_20/checkpoint-935` (epoch 1) | 运行中 |
| cuda:1 | 14719 | `sft_standard_20_qwen_math/checkpoint-935` (epoch 1) | 运行中 |

**问题**：CKA-only 正在评估的是 epoch 1 的 checkpoint-935，而不是任务要求优先使用的 epoch 2 模型 (`sft_qwen_math_cka_only_20_final`)。Standard 评估符合要求。

另外两个进程都没有指定 `--output_path`，结果会写到默认位置。

需要决定：
1. **等当前跑完** — 先拿 epoch 1 结果，之后再跑 epoch 2
2. **杀掉 CKA-only (PID 14641)** — 用 epoch 2 模型重跑

哪个方案？

---
