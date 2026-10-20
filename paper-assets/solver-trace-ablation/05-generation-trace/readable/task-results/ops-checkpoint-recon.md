# ops checkpoint recon

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_checkpoint-recon_20260515T071001_result.json`
- **Structured JSON:** [`43d89ea4ca04f1dd26e2.json`](../../sessions/43/43d89ea4ca04f1dd26e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 1. plan002-b01-s42 checkpoint-500
**不存在。** 整个 `/root/autodl-tmp/outputs/plan002_additive_b01_s42/` 目录都不存在。需要从头训练。

### 2. train_grpo.py 是否支持 resume
**不支持。** grep `resume` 无匹配，argparse 参数列表中也没有 resume 相关参数。只能从头跑。

### 3. 完整提交命令

**GRPO ISR β=0.1 s42（从头 1000 步）：**
```bash
export CUDA_VISIBLE_DEVICES=0
cd /root/solver-trace-ablation
python3 scripts/train_grpo.py \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --reward_mode execution_sta \
  --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42 \
  --num_steps 1000 \
  --beta 0.1 \
  --seed 42 \
  --no_wandb
```

**SFT baseline s43：**
```bash
export CUDA_VISIBLE_DEVICES=1
cd /root/solver-trace-ablation
python3 scripts/train_sft.py \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s43 \
  --num_steps 500 \
  --seed 43 \
  --no_wandb \
  --gpu 1
```

注：SFT 脚本自带 `--gpu` 参数内部设 CUDA_VISIBLE_DEVICES，但按 C002/C005 约束仍应外部 `export` 显式设置。

### 4. GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 0 MiB | 0% |
| 1 | 0 MiB | 0% |

**两张卡均空闲，可同时提交两个实验。**

---
