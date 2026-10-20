# ops launch humaneval sft cka only 20 cuda2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch_humaneval_sft_cka_only_20_cuda2_20260519T031235_result.json`
- **Structured JSON:** [`cd044d01317ffb89cbbf.json`](../../sessions/cd/cd044d01317ffb89cbbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now let me also check the GRPO model and prepare the command.

**已启动的任务状态:**
- **Eval**: HumanEval SFT CKA-only @2048 
- **服务器**: westd-29022 cuda:2
- **tmux**: `eval_humaneval_sft_cka_only_20_2048`
- **PID**: 63783
- **GPU**: 96% 利用率，12989 MiB
- **进度**: 推理已开始，164 problems
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048.json`

**GRPO CKA-only HumanEval 准备命令**（等 cuda:1 释放后使用）:

GRPO 模型确认存在：`/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/model.safetensors`（12GB）

```bash
# 在 westd-29022 上执行
tmux new-session -d -s eval_humaneval_grpo_cka_only_20_2048 \
  "cd /root/recovery_aware_struct_prune/src && \
   CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python eval_humaneval.py \
   --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 \
   --max_new_tokens 2048 \
   --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.json \
   2>&1 | tee /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.log"
```

---
