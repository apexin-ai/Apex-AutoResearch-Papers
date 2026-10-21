# ssh check sft standard 25 and next

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_sft_standard_25_and_next_20260523T172602_result.json`
- **Structured JSON:** [`da2a4976ed177ab62a9e.json`](../../sessions/da/da2a4976ed177ab62a9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 张 GPU 都在跑 eval_math500：

| GPU | PID | 运行时长 | 模型 |
|-----|-----|---------|------|
| 0 | 147923 | 57min | sft_rasp_20_westd |
| 1 | 145176 | 1h42m | grpo_rasp_alpha1p0_20_fair |
| 2 | 142486 | 2h23m | grpo_standard_20_fair |
| 3 | 142647 | 2h23m | sft_standard_20 |

**SFT 结果：成功**
- 1870 steps, 2 epochs, train_loss=0.8584, token_accuracy≈0.80
- checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors` (10.8GB)
- 完成时间: 2026-05-24 01:23

**GRPO 25% 启动：暂时无法启动**
- GPU 0 正在跑 eval_math500 (sft_rasp_20_westd)，已运行 57 分钟
- 需要等 eval 完成后才能启动 GRPO

要我等 eval 完成后自动启动 GRPO，还是你手动触发？

---
