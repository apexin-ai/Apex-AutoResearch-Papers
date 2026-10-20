# code d102 8b refilter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d102_8b_refilter_20260518T053346_result.json`
- **Structured JSON:** [`ca9e660bd36cdd1fa338.json`](../../sessions/ca/ca9e660bd36cdd1fa338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

### 8B CED scores 文件
`/root/autodl-tmp/rsft_scored_qwen3_8b/rsft_scores.jsonl` — 24216 条 scored records, 3027 unique docs

### Re-filter k=1 结果
- **输出路径**: `/root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl`
- **样本数**: 3018（每 doc 取 combined_score 最高的 1 条）
- **对比 k=3**: 9041 → 3018（质量更高，combined_score 均值 0.7609 vs 0.7322）
- 格式与 k=3 版本完全一致，已验证

### 4B Canonical RSFT 训练超参
| 参数 | 4B 值 | 8B k=3 值 |
|---|---|---|
| learning_rate | 2e-5 | 2e-5 |
| num_epochs | 3 | 3 |
| per_device_batch_size | 4 | 1 |
| gradient_accumulation_steps | 4 | 8 |
| warmup_steps | 100 | 100 |
| seed | 42 | 42 |
| LoRA rank/alpha | 64/128 | 64/128 |
| LoRA dropout | 0.05 | 0.05 |
| bf16 | True | True |
| save_steps | 50 | 50 |
| max_length | 2048 | 2048 |

### 推荐 8B k=1 训练命令

**Seed 42:**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=X HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python -m freige.training.rsft_trainer \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 \
  --rsft_data_path /root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl \
  --output_dir /root/autodl-tmp/rsft_output_qwen3_8b_k1 \
  --learning_rate 2e-5 \
  --num_epochs 3 \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --warmup_steps 100 \
  --save_steps 50 \
  --max_length 2048 \
  --seed 42 \
  --lora_rank 64 \
  --lora_alpha 128 \
  --bf16 \
  --wandb_project freige-rsft \
  --wandb_run_name rsft_qwen3_8b_k1_s42
```

**Seed 43:** (仅改 seed 和 output_dir/run_name)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=X HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python -m freige.training.rsft_trainer \
  --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B \
  --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 \
  --rsft_data_path /root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl \
  --output_dir /root/autodl-tmp/rsft_output_qwen3_8b_k1_s43 \
  --learning_rate 2e-5 \
  --num_epochs 3 \
  --per_device_batch_size 1 \
  --gradient_accumulation_steps 8 \
  --warmup_steps 100 \
  --save_steps 50 \
  --max_length 2048 \
  --seed 43 \
  --lora_rank 64 \
  --lora_alpha 128 \
  --bf16 \
  --wandb_project freige-rsft \
  --wandb_run_name rsft_qwen3_8b_k1_s43
```

提交前需替换 `CUDA_VISIBLE_DEVICES=X` 为实际空闲 GPU，并按 C001 先 `nvidia-smi` 确认显存。

---
