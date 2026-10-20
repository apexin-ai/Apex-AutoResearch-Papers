# 状态检查报告 (2026-05-19 06:52 UTC)

## 1. 8B RSFT s44 训练状态

- **PID 581524**: 运行中，GPU 1，26944MiB/32607MiB
- **命令**: `python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --rsft_data_path /root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_qwen3_8b_k1_s44 --seed 44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --bf16 --lora_rank 64 --lora_alpha 128 --lora_dropout 0.05 --wandb_run_name rsft_8b_k1_s44`
- **进度**: checkpoint-450/1134 (~40%)，参考 s43 用时 48min，预计还需约 30min
- **日志**: 无专用日志文件（未找到 plan019_8b_rsft_s44.log）
- **参考**: 8B RSFT s43 已完成 (1134/1134, train_loss=0.386, 48min)

## 2. 1.7B RSFT Seed Expansion 脚本

**不存在。** 上一个 Worker 未创建 seed expansion 脚本：
- `/root/autodl-tmp/scripts/seed_expansion/` 目录不存在
- 全服务器搜索无 seed_expansion 相关文件

### 1.7B RSFT 现有资源

| 资源 | 路径 | 状态 |
|------|------|------|
| Base model | `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` | ✓ |
| SFT s42 adapter | `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16` | ✓ |
| SFT s43 adapter | `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed43` | ✓ |
| SFT s44 adapter | `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed44` | ✓ |
| RSFT scored data (k1) | `/root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl` | ✓ (3021 samples) |
| RSFT s42 output | `/root/autodl-tmp/rsft_output_qwen3_1_7b_k1` | ✓ 已完成 (567 steps, 15min) |
| RSFT s43 output | 不存在 | ❌ 待训练 |
| RSFT s44 output | 不存在 | ❌ 待训练 |

### 1.7B RSFT s42 训练参数（从 d102 log 提取）

- data: `/root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl` (3021 samples)
- base_model: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`
- sft_adapter: `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16`
- LoRA: r=64, alpha=128, dropout=0.05
- 训练时间: ~15min (899s)

### 需要创建的 1.7B RSFT 脚本

两个 seed（s43, s44）都需要训练，参数与 s42 相同但改 seed 和 output_dir：
- s43: `--seed 43 --output_dir /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s43`
- s44: `--seed 44 --output_dir /root/autodl-tmp/rsft_output_qwen3_1_7b_k1_s44`

## 3. GPU 使用

| GPU | PID | 任务 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 579965 | 4B SFT s42 re-eval | 10198MiB/32607MiB | 52% |
| 1 | 581524 | **8B RSFT s44 训练** | 26944MiB/32607MiB | 80% |
| 2 | 577861 | 8B SFT s44 eval | 18518MiB/32607MiB | 66% |
| 3 | 571120 | GRPO bf16 g4 ckpt200 eval | 11378MiB/32607MiB | 54% |

**所有 4 张 GPU 均被占用，无空闲卡可用。**

## 4. 磁盘状态

- `/root/autodl-tmp`: 158GB/250GB used, **93GB free** (64%)

## 5. 关键发现

1. 8B RSFT s44 在 GPU 1 运行中，约 40% 进度，预计 ~30min 完成
2. **1.7B RSFT seed expansion 脚本未被上一个 Worker 创建**，需要从头设置
3. 所有 4 张 GPU 被占用，1.7B RSFT s43/s44 需等 GPU 释放后才能开始
4. 1.7B RSFT 所有输入数据（scored data、SFT adapters）已就绪，只缺训练执行
5. 磁盘空间充足 (93GB free)
