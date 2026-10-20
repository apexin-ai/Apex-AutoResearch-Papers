# check d134 random s47 details

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-random-s47-details_20260518T162752_result.json`
- **Structured JSON:** [`91b2b72bcb2d4db92e4f.json`](../../sessions/91/91b2b72bcb2d4db92e4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是 `d134-4b-random-b01-s47` 训练的完整信息：

---

## 训练详情

| 项目 | 值 |
|---|---|
| **PID** | `91314` |
| **tmux session** | `d134-pipeline` (created Mon May 18 18:52:28 2026) |
| **GPU** | GPU 0 — NVIDIA RTX PRO 6000 Blackwell (85553 / 97887 MiB) |

### 训练命令
```bash
/root/miniconda3/bin/python3 scripts/train_grpo.py \
  --config configs/grpo_additive_random_b01.yaml \
  --data_path data/train_500_seed42.jsonl \
  --num_steps 500 \
  --seed 47 \
  --beta 0.1 \
  --reward_mode additive_random \
  --per_device_batch_size 2 \
  --gradient_accumulation_steps 4 \
  --output_dir /root/autodl-tmp/outputs/d134_4b_random_b01_s47 \
  --no_wandb
```

### 路径

| 类型 | 路径 |
|---|---|
| **数据** | `data/train_500_seed42.jsonl` (符合 C001) |
| **输出目录** | `/root/autodl-tmp/outputs/d134_4b_random_b01_s47/` |
| **checkpoint** | `checkpoint-200` (~15G, 4 shard safetensors) |
| **训练日志** | `/root/autodl-tmp/outputs/d134_4b_random_b01_s47/train.log` |
| **reward 日志** | `/root/autodl-tmp/outputs/d134_4b_random_b01_s47/reward_log.jsonl` |
| **base model** | `/root/autodl-tmp/models/Qwen3-4B` (来自 config) |

### 当前进度

| 指标 | 值 |
|---|---|
| **当前步数** | **249 / 500** (50%) |
| **速度** | ~15.15 s/step |
| **预计剩余** | ~1h03m |
| **最新 reward** | step 249: reward=0.5194, prove_rate=0.500, isr=0.045, parse_rate=1.000 |
| **上一步 reward** | step 248: reward=0.7855, prove_rate=0.750, isr=0.115, parse_rate=1.000 |

### 其他 tmux session
- `d134-cleaner` (created Mon May 18 20:02:21 2026) — 可能是磁盘清理相关

---
