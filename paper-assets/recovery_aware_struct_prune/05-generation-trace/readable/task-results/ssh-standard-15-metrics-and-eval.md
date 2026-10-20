# ssh standard 15 metrics and eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_standard_15_metrics_and_eval_20260520T142215_result.json`
- **Structured JSON:** [`4316e30c4abde5f63152.json`](../../sessions/43/4316e30c4abde5f63152.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项验证全部通过。

## grpo_standard_15_v2 最终指标
- **loss**: 0.01142 (step 100), avg train_loss: 0.0395
- **reward**: 0.1375 (reward_std: 0.2778)
- **kl**: 0.004099
- **训练时间**: 21m49s (1309s), 13.09s/it
- **checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2/` — model.safetensors (13G), checkpoint-100, config.json, tokenizer

## eval_gsm8k_grpo_standard_15_v2 提交结果
- **PID**: 256586 (python), 父进程 256581
- **验证结果**: 进程存活 ✓ (1m29s) | GPU memory ✓ (13292MiB on cuda:3, 77% util) | 日志输出 ✓ (Evaluating 0/1319 started)
- **状态**: **RUNNING**
- **日志**: `~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_15_v2.log`
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json`

---
