# ops label only code check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_label_only_code_check_20260520T172049_result.json`
- **Structured JSON:** [`7f81b8574983531209f0.json`](../../sessions/7f/7f81b8574983531209f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### label_only 是否对所有模型通用

**是，完全通用。** 训练脚本无任何模型特定逻辑：

- `--label_only_loss` 标志触发 `to_prompt_completion()` 格式化 + `completion_only_loss=True`
- `to_prompt_completion()` 仅调用 `tokenizer.apply_chat_template()`，对任何有 chat template 的模型都适用
- CodeLlama-13B-Instruct 和 Qwen-1.5B-Instruct 均有 chat template（已确认 `tokenizer_config.json`）
- LoRA target modules (`q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`) 对两种架构都适用
- `deepseek_label_only_seed42` checkpoint 已存在，证明跨模型可用

### 是否需要特殊参数

不需要额外参数，标准 `--label_only_loss` 即可。但注意：

- **CodeLlama-13B 需要 `--gradient_checkpointing`**（13B 参数量，类似 Qwen-7B 约束）
- **模型路径不同**：
  - Qwen-1.5B: `/root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct`
  - CodeLlama-13B: `/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf`（不在项目 models/ 目录下）

### 训练命令

**Qwen-1.5B:**
```bash
/root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct \
  --label_only_loss \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_label_only \
  --wandb_run_name qwen15b_full_trace_label_only_seed42
```

**CodeLlama-13B:**
```bash
/root/miniconda3/bin/python /root/trace-verdict-study/train/train_sft.py \
  --condition full_trace \
  --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf \
  --label_only_loss \
  --gradient_checkpointing \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_label_only \
  --wandb_run_name codellama13b_full_trace_label_only_seed42
```

### 当前已有的 label_only checkpoints

| 模型 | 已有 seeds |
|------|-----------|
| Qwen-7B | 42, 123, 456 |
| DeepSeek | 42 |
| Qwen-1.5B | **无** |
| CodeLlama-13B | **无** |

---
