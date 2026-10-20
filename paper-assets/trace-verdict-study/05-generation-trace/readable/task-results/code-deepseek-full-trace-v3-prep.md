# code deepseek full trace v3 prep

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deepseek_full_trace_v3_prep_20260515T183349_result.json`
- **Structured JSON:** [`e97be6b47d9bcdd0590b.json`](../../sessions/e9/e97be6b47d9bcdd0590b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。汇总结果：

**1. `load_best_model_at_end` 状态**: 已在 L148-151 注释掉（`# TEMP_DISABLED:`），连同 `save_total_limit`、`metric_for_best_model`、`greater_is_better`，**无需再修改**。

**2. Chat-template-aware truncation**: 完好。`to_chat_text()` (L38) 和 `to_prompt_completion()` (L50-51) 都通过 `apply_chat_template` 格式化后再传给 SFTTrainer，由 `max_length=2048` 统一截断，避免了 v1 先截断再套 template 导致 label 被吃掉的问题。

**3. v2 残留 checkpoint**: 不存在，无冲突。

**4. 模型路径**: 已确认存在，含 safetensors 和 tokenizer 文件。

**5. Dry-run**: `--help` 正常返回，无报错。

**6. 完整训练启动命令**（注意：实际脚本是 `train/train_sft.py`，参数名与任务描述不同）:

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
python /root/trace-verdict-study/train/train_sft.py \
  --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct \
  --condition full_trace \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3 \
  --seed 42 \
  --gradient_checkpointing \
  --wandb_run_name deepseek_full_trace_seed42_v3
```

---
