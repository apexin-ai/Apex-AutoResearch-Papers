# D112 RSFT s44 Training Prep

## 1. CED Scoring 输出确认

| 项目 | 值 |
|------|-----|
| 数据路径 | `/root/autodl-tmp/rsft_scored_4b_sft_s44/rsft_train.jsonl` |
| 样本数 | 3014 |
| 格式 | JSONL: `{input, output, ced_score, doc_id, generation_idx, format_reward, f1_reward, combined_score}` |
| 创建时间 | 2026-05-19 12:32 |
| 选择策略 | top_k=1, CED scoring (τ=0.5) |
| 权重 | format:0.2, f1:0.4, ced:0.4 |
| selected combined_score | mean=0.741, median=0.740, min=0.267, max=0.999 |
| selected f1_reward | mean=0.676, median=0.692 |
| selected ced_reward | mean=0.676, median=0.694 |

数据格式与 `rsft_trainer.py` 兼容（需要 `input`, `output`, `ced_score` 字段）。

## 2. 关键路径

| 资源 | 路径 |
|------|------|
| Base model | `/root/autodl-tmp/models/Qwen3-4B` |
| SFT s44 adapter | `/root/autodl-tmp/sft_output_seed44/` |
| RSFT 训练数据 | `/root/autodl-tmp/rsft_scored_4b_sft_s44/rsft_train.jsonl` |
| Eval data | `/root/autodl-tmp/data/docred` |
| 训练脚本 | `freige.training.rsft_trainer` |
| 输出目录 | `/root/autodl-tmp/d112_rsft_output_4b_sft_s44` |

## 3. ⚠️ 已有 RSFT 输出

以下两个目录已存在，均在 CED scoring 之后（2026-05-19 21:02）创建：
- `/root/autodl-tmp/rsft_output_4b_sft_s44/` — QLoRA 版本
- `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16/` — bf16 版本（D112 eval 脚本引用此路径）

D112 eval 脚本 `scripts/d112/eval_d112_rsft_bf16.sh` 已引用 `rsft_output_4b_sft_s44_bf16` 作为 RSFT adapter。**训练可能已完成。** 如需重训，建议使用新输出目录避免覆盖。

## 4. 超参数配置

基于 rsft_trainer.py 默认值 + 已有 RSFT output (r=64, alpha=128) 配置：

| 参数 | 值 | 说明 |
|------|-----|------|
| learning_rate | 2e-5 | 默认值 |
| num_epochs | 3 | 默认值 |
| per_device_batch_size | 4 | 默认值 |
| gradient_accumulation_steps | 4 | effective_bs=16 |
| warmup_steps | 100 | 默认值 |
| max_length | 2048 | 默认值 |
| lora_rank | 64 | 与 SFT adapter 一致 |
| lora_alpha | 128 | 与 SFT adapter 一致 |
| lora_dropout | 0.05 | 默认值 |
| bf16 | True | 默认值 |
| quantize | False | bf16 全精度，不用 QLoRA |
| weighted_sampling | True | CED score 加权采样 |
| save_steps | 50 | 默认值 |
| seed | 42 | 默认值 |

## 5. 训练命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/freige

export CUDA_VISIBLE_DEVICES=2
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export WANDB_PROJECT=freige-rsft

nohup python -m freige.training.rsft_trainer \
    --base_model /root/autodl-tmp/models/Qwen3-4B \
    --sft_adapter /root/autodl-tmp/sft_output_seed44 \
    --rsft_data_path /root/autodl-tmp/rsft_scored_4b_sft_s44/rsft_train.jsonl \
    --output_dir /root/autodl-tmp/d112_rsft_output_4b_sft_s44 \
    --learning_rate 2e-5 \
    --num_epochs 3 \
    --per_device_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --warmup_steps 100 \
    --max_length 2048 \
    --lora_rank 64 \
    --lora_alpha 128 \
    --lora_dropout 0.05 \
    --bf16 \
    --weighted_sampling \
    --save_steps 50 \
    --save_total_limit 5 \
    --eval_data_dir /root/autodl-tmp/data/docred \
    --eval_max_docs 50 \
    --wandb_run_name d112_rsft_4b_s44 \
    --seed 42 \
    > /tmp/d112_rsft_s44_train.log 2>&1 &
echo $!
```

## 6. GPU / 资源预估

**GPU 状态 (2026-05-21):**

| GPU | 已用 | 总量 | 空闲 |
|-----|------|------|------|
| 0 | 18.9 GB | 97.9 GB | 79.0 GB |
| 1 | 32.5 GB | 97.9 GB | 65.4 GB |
| **2** | **6.2 GB** | **97.9 GB** | **91.7 GB** |
| 3 | 19.6 GB | 97.9 GB | 78.3 GB |

**推荐 GPU 2**（空闲最多）。

**内存需求预估 (4B bf16 + LoRA r=64):**
- 模型权重: ~8 GB
- LoRA 参数 + optimizer states: ~4-6 GB
- 激活值 (gradient checkpointing): ~5-8 GB
- 总计: ~20-25 GB

**训练时间预估:**
- Steps/epoch: ceil(3014 / 16) = 189
- Total steps: 189 × 3 = 567
- RTX 5090 throughput (~4B bf16 LoRA): ~1.5-2 s/step
- 预估总时间: **~15-20 分钟**

## 7. 训练后操作

1. 验证 adapter 输出: `ls /root/autodl-tmp/d112_rsft_output_4b_sft_s44/adapter_model.safetensors`
2. 如果用新输出目录，需更新 D112 eval 脚本中的 `RSFT_ADAPTER` 路径
3. Registry 注册实验
4. 运行 eval: `bash scripts/d112/eval_d112_rsft_bf16.sh`（需修改路径指向新 adapter）

## 8. 注意事项

- **C002/C003 约束**: 命令已设置 `CUDA_VISIBLE_DEVICES=2`
- **C001 约束**: eval 前需确认目标 GPU 显存占用 < 2GB
- 如果 GPU 2 被占用，可选 GPU 0 或 GPU 3 (均有 ~78GB 空闲)
- 已有 `rsft_output_4b_sft_s44_bf16` 可能就是 D112 的训练结果，建议先确认是否需要重训
