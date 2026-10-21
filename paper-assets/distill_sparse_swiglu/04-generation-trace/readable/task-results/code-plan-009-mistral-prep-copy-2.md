# code plan 009 mistral prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_009_mistral_prep_20260515T210759_result.json`
- **Structured JSON:** [`9510192ad1aee9f20efd.json`](../../sessions/95/9510192ad1aee9f20efd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### 代码兼容性：完全兼容，无需修改

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 模型维度从 config 读取 | ✅ | `num_hidden_layers`, `hidden_size`, `intermediate_size` 均从 `model.config` 取 |
| MLP 结构 | ✅ | MistralMLP 同样有 `gate_proj`/`up_proj`/`down_proj`/`act_fn` |
| 层级路径 `model.model.layers` | ✅ | Mistral 和 Llama 在 HF 中结构一致 |
| `AutoModelForCausalLM` | ✅ | 自动识别 MistralForCausalLM |
| Attention 实现 | ✅ | flash_attention_2 / sdpa 对 Mistral 均支持 |
| 梯度检查点 | ✅ | 调用 HF base class 方法，模型无关 |

### 架构对比（Mistral-7B-v0.3 vs Llama-3.1-8B）

| 参数 | Mistral-7B | Llama-3.1-8B |
|------|-----------|-------------|
| hidden_size | 4096 | 4096 |
| intermediate_size | 14336 | 14336 |
| num_hidden_layers | 32 | 32 |
| hidden_act | silu | silu |
| vocab_size | **32768** | **128256** |
| num_key_value_heads | 8 | 8 |

Predictor 参数量完全相同（因为 hidden_size 和 intermediate_size 一致）：每层 `4096×128 + 128 + 128×14336 + 14336 = 2,373,760`，32 层共约 **75.96M** 参数。

vocab_size 差异只影响 KL loss 的 logit 维度（32768 vs 128256），**显存占用更低**。

### GPU 状态：均在使用中

- GPU 0: 67.6GB/97.9GB (78%)
- GPU 1: 33.8GB/97.9GB (98%)

无法运行 dry-run，先准备命令。

### Dry-run 命令（等 GPU 空闲）

```bash
source /root/distill_sparse_swiglu/setup_env.sh
cd /root/distill_sparse_swiglu
TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py \
  --model_name_or_path /root/autodl-tmp/models/mistral-7b \
  --loss_type kl_normalized \
  --num_steps 5 \
  --batch_size 4 \
  --seq_len 2048 \
  --lr 1e-3 \
  --seed 42 \
  --sparsity_target 0.5 \
  --gpu 0 \
  --output_dir /root/distill_sparse_swiglu/checkpoints/mistral_kl_s42_dryrun \
  --gradient_checkpointing \
  --dataset wikitext-103
```

### 正式训练命令（1000 steps）

```bash
source /root/distill_sparse_swiglu/setup_env.sh
cd /root/distill_sparse_swiglu
TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python src/train.py \
  --model_name_or_path /root/autodl-tmp/models/mistral-7b \
  --loss_type kl_normalized \
  --num_steps 1000 \
  --batch_size 4 \
  --seq_len 2048 \
  --lr 1e-3 \
  --seed 42 \
  --sparsity_target 0.5 \
  --gpu 0 \
  --output_dir /root/distill_sparse_swiglu/checkpoints/mistral_kl_s42 \
  --gradient_checkpointing \
  --dataset wikitext-103 \
  --wandb_project distill_sparse_swiglu \
  --wandb_run_name mistral_kl_normalized_s42
```

模型文件（3 个 safetensors 分片 ~14.5GB + tokenizer）已确认完整。代码零改动即可直接运行 Mistral 训练。

---
