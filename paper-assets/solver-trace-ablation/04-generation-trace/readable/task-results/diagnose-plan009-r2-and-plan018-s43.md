# diagnose plan009 r2 and plan018 s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan009-r2-and-plan018-s43_20260514T114013_result.json`
- **Structured JSON:** [`da9876d466555f8f8e22.json`](../../sessions/da/da9876d466555f8f8e22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 实验 1: plan009-sft-baseline-s42-r2

**失败原因**: CUDA OOM at step 0 (backward pass)。GPU 冲突——plan018-additive-random-b01-s43 (PID 540910) 正在 cuda:1 上运行，占用 81.69 GiB，SFT 进程只剩 ~13 GiB，不够 backward pass。

**可重试**: Yes，需要确保目标 GPU 空闲。

**重试命令**:
```bash
export CUDA_VISIBLE_DEVICES=1  # 确认 GPU 空闲
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation
python3 scripts/train_sft.py \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 \
  --num_steps 200 --seed 42 --gpu 1 --no_wandb
```

---

### 实验 2: plan018-additive-random-b01-s43

**失败原因**: 磁盘满 (`No space left on device`, os error 28)。训练跑了 200/500 步后在 checkpoint save 时 safetensors 序列化失败。无 checkpoint 保存。

**可重试**: Yes，磁盘当前 142G/250G (57%)，有 109G 可用，直接重跑即可。

**重试命令**:
```bash
export CUDA_VISIBLE_DEVICES=1
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation
python3 scripts/train_grpo.py \
  --config configs/grpo_additive_random_b01.yaml \
  --data_path data/train_500_seed42.jsonl \
  --num_steps 500 --seed 43 --beta 0.1 \
  --reward_mode additive_random \
  --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43
```

---

**关联发现**: plan018-s43 (PID 540910) 就是导致 plan009-sft-r2 OOM 的那个进程——两个实验被分配到同一张 GPU (cuda:1)。Registry notes 已更新。

---
