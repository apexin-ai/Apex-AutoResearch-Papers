# code rsft train config

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft-train-config_20260515T022446_result.json`
- **Structured JSON:** [`5dd60ca35f54fac04614.json`](../../sessions/5d/5dd60ca35f54fac04614.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法和导入均通过。下面是汇总结果。

---

## 验证结果

### 已满足项

| 项目 | 状态 |
|------|------|
| SFT 训练框架复用 | ✅ 相同 SFTConfig/SFTTrainer, chat template, SYSTEM_PROMPT |
| LoRA 结构一致 | ✅ r=64, alpha=128, dropout=0.05, 7 target modules 完全一致 |
| SFT adapter merge | ✅ base → PeftModel.from_pretrained → merge_and_unload → 新 LoRA |
| CED 数据加载 | ✅ JSONL 格式，ced_score 加权采样 |
| 多 GPU 支持 | ✅ accelerate_4gpu.yaml + deepspeed_zero2.json 已配置，`--deepspeed` 参数已有 |
| bf16 / gradient checkpointing | ✅ |

### 新增修改

| 修改 | 内容 |
|------|------|
| `TrainerCallback` import | 新增 |
| `prepare_eval_data()` | 加载 DocRED dev set，构建 task eval prompts + gold + loss-based eval dataset |
| `TaskEvalCallback` | 每个 epoch 结束时：generate on dev subset → parse → 计算 F1/Ign-F1/Evi-F1/EDCR → log to W&B |
| eval_loss 支持 | `eval_strategy="epoch"`, `eval_dataset` 传入 trainer |
| 新 CLI 参数 | `--eval_data_dir`, `--eval_max_docs`(50), `--max_new_tokens`(1024) |

### SFT vs RSFT 超参对比

| 参数 | SFT warmup | RSFT 默认 | 说明 |
|------|-----------|----------|------|
| learning_rate | 2e-4 | **2e-5** | 10x 低，合理——从 warmup checkpoint 继续 |
| per_device_batch_size | 1 | **4** | RSFT 样本更短 (max_length=2048 vs 4096) |
| gradient_accumulation | 16 | **4** | effective bs: SFT=16, RSFT=16 (4×4) |
| warmup | ratio=0.05 | **steps=100** | |
| max_length | 4096 | **2048** | RSFT 生成数据一般更短 |
| epochs | 3 | 3 | 相同 |

### 显存估算 (单卡 RTX 5090 32GB)

- Qwen3-4B bf16: ~8GB
- LoRA trainable: ~250MB
- Optimizer (AdamW): ~500MB
- Activations (bs=4, seq=2048, grad ckpt): ~8-10GB
- 总计: ~17-19GB → **单卡可行**，4 GPU 更从容

### 完整训练命令

**单卡：**
```bash
cd /root/autodl-tmp && \
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
python -m freige.training.rsft_trainer \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --sft_adapter /root/autodl-tmp/sft_output \
    --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \
    --output_dir /root/autodl-tmp/rsft_output \
    --learning_rate 2e-5 \
    --num_epochs 3 \
    --per_device_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lora_rank 64 --lora_alpha 128 \
    --weighted_sampling \
    --eval_data_dir /root/autodl-tmp/data/docred \
    --eval_max_docs 50 \
    --wandb_run_name rsft-ced-r1 \
    --seed 42
```

**4 GPU (accelerate + DeepSpeed ZeRO-2)：**
```bash
cd /root/autodl-tmp && \
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
accelerate launch --config_file freige/configs/accelerate_4gpu.yaml \
    -m freige.training.rsft_trainer \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --sft_adapter /root/autodl-tmp/sft_output \
    --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl \
    --output_dir /root/autodl-tmp/rsft_output \
    --learning_rate 2e-5 \
    --num_epochs 3 \
    --per_device_batch_size 4 \
    --gradient_accumulation_steps 1 \
    --lora_rank 64 --lora_alpha 128 \
    --weighted_sampling \
    --eval_data_dir /root/autodl-tmp/data/docred \
    --eval_max_docs 50 \
    --deepspeed freige/configs/deepspeed_zero2.json \
    --wandb_run_name rsft-ced-r1-4gpu \
    --seed 42
```

注意：4 GPU 时 `gradient_accumulation_steps=1`（effective bs = 4×4=16，与单卡一致）。WeightedRandomSampler 在 DDP 下不生效，Accelerate 会替换 sampler。

### 预估训练时间

假设 ~3000 RSFT 样本，effective bs=16:
- ~188 steps/epoch × 3 epochs = ~564 steps
- 单卡 RTX 5090: ~2-3 min/epoch → **~10 min total**
- 4 GPU: ~1 min/epoch → **~5 min total**
- Task eval (50 docs generate): ~3-5 min/epoch

### 待完成前置

`/root/autodl-tmp/rsft_filtered/rsft_train.jsonl` 尚不存在，需先完成 CED score → filter 流程生成训练数据。

---
