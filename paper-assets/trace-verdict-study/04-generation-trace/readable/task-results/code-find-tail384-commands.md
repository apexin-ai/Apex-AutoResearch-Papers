# code find tail384 commands

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_find_tail384_commands_20260518T130503_result.json`
- **Structured JSON:** [`bcd4b814d87886ae81b9.json`](../../sessions/bc/bcd4b814d87886ae81b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 tail-384 实验**已经训练完成**（都有 `final/` 目录和 3 个 checkpoint）。

以下是基于 `train_sft.py` 参数和已有实验命名模式构造的命令模板：

---

**1. DeepSeek-6.7B tail-384 on cuda:0**

```bash
source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_384 \
  --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail384_seed42 \
  --wandb_run_name deepseek_full_trace_tail384_seed42 \
  --gpu 0 \
  --seed 42
```

**2. Qwen-7B tail-384 on cuda:1**

```bash
source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace_tail_384 \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_tail384_seed42 \
  --wandb_run_name qwen7b_full_trace_tail384_seed42 \
  --gpu 1 \
  --seed 42 \
  --gradient_checkpointing
```

---

注意：两个实验的 checkpoint 目录已存在且都有 `final/`，说明**已经训练完成**。如果要重新训练，需要先清空或更换 output_dir。

---
