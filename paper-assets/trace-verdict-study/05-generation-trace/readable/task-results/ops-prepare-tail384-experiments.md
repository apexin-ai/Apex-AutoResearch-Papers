# ops prepare tail384 experiments

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_tail384_experiments_20260518T113843_result.json`
- **Structured JSON:** [`5290f83019a600445a49.json`](../../sessions/52/5290f83019a600445a49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

```
tail-384 支持状态: 需要生成数据（代码已就绪）

代码改动（已完成）:
1. 新建 /root/trace-verdict-study/data/format_tail_truncation_384.py（基于 512 版本，MAX_TRACE_TOKENS=384）
2. train_sft.py --condition choices 已添加 full_trace_tail_384

数据生成命令:
cd /root/trace-verdict-study && /root/miniconda3/bin/python data/format_tail_truncation_384.py

4 个实验命令:

1. qwen7b_full_trace_tail384_seed42:
cd /root/trace-verdict-study && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python train/train_sft.py \
  --condition full_trace_tail_384 \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_tail_384_seed42 \
  --wandb_run_name full_trace_tail_384_seed42 \
  --seed 42 --max_steps -1 --gradient_checkpointing

2. deepseek_full_trace_tail384_seed42:
cd /root/trace-verdict-study && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python train/train_sft.py \
  --condition full_trace_tail_384 \
  --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail384_seed42 \
  --wandb_run_name deepseek_full_trace_tail384_seed42 \
  --seed 42 --max_steps -1

3. qwen15b_full_trace_tail384_seed42:
cd /root/trace-verdict-study && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python train/train_sft.py \
  --condition full_trace_tail_384 \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail384_seed42 \
  --wandb_run_name qwen15b_full_trace_tail384_seed42 \
  --seed 42 --max_steps -1

4. codellama13b_full_trace_tail384_seed42:
cd /root/trace-verdict-study && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python train/train_sft.py \
  --condition full_trace_tail_384 \
  --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf/ \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail384_seed42 \
  --wandb_run_name codellama13b_full_trace_tail384_seed42 \
  --seed 42 --max_steps -1 --gradient_checkpointing

潜在问题:
- CodeLlama-13B: 之前的 tail 实验未用 --label_only_loss，此处保持一致。如需加上需单独确认。
- Qwen-7B 和 CodeLlama-13B 加了 --gradient_checkpointing（约束 C002 + 13B 显存需求）。
- 必须先运行数据生成脚本，预计耗时 2-3 分钟。
```

---
