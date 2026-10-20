# research prepare unpruned grpo westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_prepare-unpruned-grpo-westd_20260515T172005_result.json`
- **Structured JSON:** [`9722501b9a274d344669.json`](../../sessions/97/9722501b9a274d344669.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

301 行，与 westb 一致。所有准备工作完成。

---

## 报告

### 1. Base Model
- **路径**: `/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B/`
- **状态**: 已在 westd，包含 2 个 safetensors 文件 + config.json + tokenizer

### 2. 代码
- **train_grpo_v5.py**: 已从 westb 同步到 westd，301 行，验证通过
- **model_utils.py**: 已在 westd
- **数据**: GSM8K 从 HuggingFace 在线加载，无需本地数据文件

### 3. 依赖
| 包 | 版本 |
|---|---|
| torch | 2.11.0+cu128 |
| transformers | 5.8.1 |
| trl | 1.4.0 |
| datasets | 4.8.5 |
| accelerate | 1.13.0 |
| bitsandbytes | 0.49.2 (新装) |
| peft | 0.19.1 (新装) |

### 4. 磁盘
- `/root/autodl-tmp/`: 250GB 总量，46GB 可用
- GRPO 3 个 checkpoint × ~15GB = ~45GB → **刚好够用**，save_total_limit=3 会滚动删除

### 5. GPU 状态
- **cuda:0**: 占用 ~51GB（SFT 训练中）
- **cuda:1**: 占用 ~51GB（SFT 训练中）
- **dry-run 跳过**：两块 GPU 都在跑 SFT

### 6. 完整启动命令

```bash
cd /root/recovery_aware_struct_prune/src && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 nohup python train_grpo_v5.py \
  --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_baseline \
  --gpu 0 \
  --max_completion_length 1024 \
  --beta 0.01 \
  --temperature 0.4 \
  --repetition_penalty 1.15 \
  --format_reward_weight 0.1 \
  --gradient_checkpointing true \
  --optim adamw_bnb_8bit \
  --loss_type dapo \
  --learning_rate 1e-6 \
  --max_steps 100 \
  --save_total_limit 3 \
  --save_steps 50 \
  --reward_desert_patience 50 \
  --run_name grpo_unpruned_baseline \
  > /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_baseline.log 2>&1 &
```

### 阻塞项
- **cuda:0 被 SFT 占用**。需等 SFT 完成或被 kill 后才能启动 GRPO baseline。无其他阻塞项。

---
