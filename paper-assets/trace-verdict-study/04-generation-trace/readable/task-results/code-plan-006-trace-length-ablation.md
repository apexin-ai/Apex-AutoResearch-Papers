# code plan 006 trace length ablation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_006_trace_length_ablation_20260515T230203_result.json`
- **Structured JSON:** [`b3e03815564292a1d73b.json`](../../sessions/b3/b3e03815564292a1d73b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

**Dry-run 验证通过：**
- `--max_trace_tokens 2048` 参数正常工作
- 0/4720 条 trace 被截断（原始 trace 最大 1958 tokens < 2048），确认是有效控制组
- 训练 step 正常完成，~38s/step

**GPU 占用：**
- cuda:0: `deepseek_full_trace_seed42_v3`（不碰）
- cuda:1: `full_trace_256tok_seed42`（步骤 6/444，~15s/step，预计还需 **~1.8 小时**训练 + eval）

2048tok 实验已准备好，但需等 cuda:1 释放。提交命令：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=1 python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace --max_trace_tokens 2048 \
  --model_path /root/autodl-tmp/trace-verdict-study-models/Qwen2.5-Coder-7B-Instruct \
  --gradient_checkpointing --gpu 0 --seed 42 \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_2048tok_seed42 \
  --wandb_project trace-verdict-study --wandb_run_name full_trace_2048tok_seed42"
```

需要等 256tok 跑完后再提交，还是有其他安排？

---
