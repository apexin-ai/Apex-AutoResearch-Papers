# ssh eval random rho02

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_random_rho02_20260517T053650_result.json`
- **Structured JSON:** [`42d90f42106878c4ba48.json`](../../sessions/42/42d90f42106878c4ba48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都**未完成**。

## 训练状态报告

### random_reweight_v2_seed42
- **进度**: ~5870/6103 steps (96%)
- **当前速度**: 2.12s/step (纯训练), eval 每 500 步耗时 ~44min
- **ETA**: ~50 min（含 step 6000 处的 eval）
- **最新 eval_loss**: 3.035 (step 5000 处)
- **最新 train_loss**: weighted ~1.86, unweighted ~2.43 (step_metrics at step 5499)
- **Checkpoint**: `/root/autodl-tmp/output/models/random_reweight_v2_seed42/checkpoint-5000/`
- **GPU**: CUDA:0

### rho02_adaptive_tau09_seed42
- **进度**: 3118/6103 steps (51%)
- **当前速度**: 2.67s/step (纯训练), eval 每 500 步耗时 ~44min
- **ETA**: ~6.5 hours（含 6 次 eval 暂停）
- **最新 eval_loss**: 3.034 (step 3000 处)
- **最新 train_loss**: weighted ~2.93, unweighted ~2.40 (step_metrics at step 3062)
- **Checkpoint**: `/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/checkpoint-3000/`
- **GPU**: CUDA:1

### 关键发现
- 两个实验的 `max_steps=6103`（200M tokens / 32768 tokens_per_step）
- 每次 eval 遍历全部 holdout 数据，耗时 ~44 min，严重拖慢总训练时间
- random_reweight_v2 约 50 min 后完成，rho02 还需 ~6.5 小时
- 两个实验的 eval_loss 当前非常接近（3.035 vs 3.034），rho02 可能在后续 steps 拉开差距

**按指令不跑 eval，等训练完成后再执行。** 需要我 50 分钟后回来对 random_reweight_v2 跑 eval 吗？

---
