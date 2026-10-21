# ssh check seed456 and launch eval westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_seed456_and_launch_eval_westb0_20260522T162111_result.json`
- **Structured JSON:** [`3e4e61c3936beafd8390.json`](../../sessions/3e/3e4e61c3936beafd8390.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 进程运行中（PID 224705, 533% CPU），正在从磁盘加载 12GB 模型权重到内存，GPU 尚未加载完成但进程状态正常。

## 训练结果
- **状态**: success（100/100 步完成，但最终 `save_model` 因磁盘满失败）
- **checkpoint**: 存在，`checkpoint-100/model.safetensors` = 12GB ✓
- **checkpoint 总大小**: 26G（已删除 15G optimizer.pt + 6.2G 损坏的 model.safetensors，释放 21G）
- **日志关键信息**: `100%|██████████| 100/100 [3:02:44<00:00, 109.64s/it]`，最终 save 报 `safetensors_rust.SafetensorError: No space left on device (os error 28)`

## eval 启动
- **PID**: 224705（子进程），224700（bash wrapper）
- **GPU**: cuda:0（CUDA_VISIBLE_DEVICES=0），模型加载中
- **GPU:1**: 被另一个 eval 占用（`eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2`, PID 220343）
- **命令**: `cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path .../grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path .../results/eval_gsm8k_grpo_random_20_seed456.json`
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log`

---
