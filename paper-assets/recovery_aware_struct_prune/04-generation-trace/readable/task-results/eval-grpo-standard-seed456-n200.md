# eval grpo standard seed456 n200

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grpo_standard_seed456_n200_20260520T091434_result.json`
- **Structured JSON:** [`91608e5a5f6bdddf6b32.json`](../../sessions/91/91608e5a5f6bdddf6b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活，日志仅 2 行——模型 12.3GB 正在从磁盘加载到 CPU 内存（pruned model 的 non-uniform 架构加载较慢）。这是正常的，通常需要 5-10 分钟。

**总结：**

- **Registry**: `eval_gsm8k_grpo_standard_20_seed456` 已创建（PREPARING, parent=grpo_standard_20_seed456）
- **Job**: 已提交到 westd-29022 cuda:3, tmux session `eval_gsm8k_grpo_standard_20_seed456`, PID 221008
- **状态**: 模型加载中（12.3GB safetensors, non-uniform MLP），GPU 显存尚未占用
- **日志**: `~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed456.log`
- **预计**: 模型加载完成后 GPU 3 显存上升至 ~13GB，eval 约 2-3h 完成
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed456_n200.json`

---
