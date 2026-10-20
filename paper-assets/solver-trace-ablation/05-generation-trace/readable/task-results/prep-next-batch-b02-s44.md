# prep next batch b02 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_next-batch-b02-s44_20260516T043006_result.json`
- **Structured JSON:** [`c3ff318b50dccc0da8a4.json`](../../sessions/c3/c3ff318b50dccc0da8a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. 当前训练进度

| 实验 | PID | Step | 已运行 | 速率 | 预计剩余 |
|---|---|---|---|---|---|
| sweep-isr-b02-s42 | 633657 | **146/500** | 20m10s | ~8.3s/step | **~49 min** |
| sweep-isr-b02-s43 | 633515 | **128/500** | 20m16s | ~9.5s/step | **~59 min** |

GPU 状态：cuda:0 93% (80GB/98GB), cuda:1 90% (85GB/98GB) — 正常。

两个实验约 **1 小时内完成**（~05:20-05:30 UTC）。

零奖励 batch 比例：s42 75/147 (51%), s43 66/129 (51%) — GRPO 正常范围，不算 collapse。

### 2. b02-s44 提交准备

| 检查项 | 状态 |
|---|---|
| Config `grpo_additive_bonus_b02.yaml` | OK, data_path=`train_500_seed42.jsonl` (C001) |
| 模型 `/root/autodl-tmp/models/Qwen3-4B` | OK |
| 脚本 `classify_h7.py` | OK (22KB) |
| `save_total_limit=1` (C003) | OK, hardcoded in `train_grpo.py` |
| 磁盘 | 54GB free (79%) — 够用 |

**就绪。** 提交命令（等 GPU 释放后）：

```bash
# C007: 先 nvidia-smi 确认 GPU 已释放
# C002/C005: 显式 export
export CUDA_VISIBLE_DEVICES=0   # 选先释放的那张卡
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation
python3 scripts/train_grpo.py \
  --config configs/grpo_additive_bonus_b02.yaml \
  --seed 44 --num_steps 500 --num_generations 4 \
  --output_dir /root/autodl-tmp/outputs/sweep_isr_b02_s44 \
  --no_wandb
```

### 3. 异常

无。dry-run（`--help`）需要 `ssh_execute` 才能运行，但所有文件和路径已确认存在。

---
