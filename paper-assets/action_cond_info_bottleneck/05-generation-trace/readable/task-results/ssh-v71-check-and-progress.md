# ssh v71 check and progress

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v71-check-and-progress_20260517T032648_result.json`
- **Structured JSON:** [`3ec617bbc11733123013.json`](../../sessions/3e/3ec617bbc11733123013.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. v7.1 scorer-only 脚本

**脚本存在**：`/root/acib/scripts/run_v7.1_scorer_only.sh`（913 bytes, May 17 04:38）

内容：
```bash
python3 -u scripts/train_acib.py \
  --model_id lerobot/smolvla_libero \
  --dataset_id lerobot/libero \
  --data_root /root/autodl-tmp/libero_dataset \
  --hidden_dim 64 \
  --alpha 0.01 --beta 0.01 --beta_warmup_steps 1000 \
  --mode soft --condition_source language --conditioning_mode concat \
  --lambda_contrastive 0.1 --diversity_lambda 0.1 --lambda_ent 0.0 \
  --steps 20000 --batch_size 64 --lr 1e-4 --warmup_steps 1000 --grad_clip 1.0 \
  --save_freq 5000 --dtype bfloat16 \
  --gpu 0 --seed 42 \
  --train_scorer_only \
  --freeze_action_expert \
  --output_dir /root/autodl-tmp/acib_v7.1_scorer_only
```

**代码支持完整**：
- `acib/config.py:19` — `freeze_action_expert: bool = False`
- `acib/config.py:20` — `train_scorer_only: bool = False`
- `acib/acib_policy.py:199` — freeze 逻辑实现
- `acib/acib_policy.py:202` — scorer_only 逻辑实现
- `scripts/train_acib.py` — argparse 参数 + 训练逻辑分支均已实现

### 2. alpha=0.0 进度

- **libero_spatial**：正在跑第 4 个 task（`libero_spatial_3`），已完成 task 0/1/2 的 video 目录
- 当前 rollout 进度 ~28%/280 steps，running_success_rate=0.0%
- 尚无 `eval_info.json`（suite 未完成）
- 4 suites 总共要跑（spatial/object/goal/10），当前还在 spatial 阶段

### 3. alpha=0.3 进度

- **libero_spatial**：正在跑第 1 个 task（`libero_spatial_0`），episode 39/50（78%）
- 刚启动不久，spatial suite 的第一个 task 即将完成

---
