# code crm loss variants

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_crm-loss-variants_20260522T045621_result.json`
- **Structured JSON:** [`bf0429d672d3016af03a.json`](../../sessions/bf/bf0429d672d3016af03a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个训练全部正常运行：

| exp_id | GPU | loss_type | Epoch 1 val_loss | PID |
|--------|-----|-----------|----------|-----|
| crm-loss-mse-baseline | cuda:0 | mse | 0.008373 | 845069 |
| crm-loss-perdof | cuda:1 | perdof_weighted | (logging) | 845281 |
| crm-loss-conformal | cuda:2 | conformal_guided | 0.037526 | 845499 |
| crm-loss-combined | cuda:3 | combined | (starting) | 845729 |

## 产出总结

**1. 代码改动**
- `src/train_crm.py`（549→601 行）：
  - 新增 `--loss_type` 参数（mse/perdof_weighted/conformal_guided/combined）
  - 新增 `--lambda_conf` 参数（default 0.1）
  - 新增 `_argmin_to_expert()`：选取 K 样本中最接近 expert 的那个
  - 新增 `_compute_loss()`：统一 loss 分发函数
  - 训练前从训练集计算 DOF inverse-variance weights（用于 perdof_weighted/combined）
  - 训练循环、augmentation、validation 三处 loss 均替换为 `_compute_loss` 调用

**2. 数据确认**
- Cache: `/root/autodl-tmp/crm_cache_v5/object/`（14570 samples, K=10, obs_dim=960, action_dim=6, h_eff=5）
- OBS_DIM = **960**（SmolVLA hidden_size，不是 1536/2048）
- SmolVLA 模型: `/root/autodl-tmp/models/smolvla_libero/`

**3. 4 个训练 PID**
- crm-loss-mse-baseline: PID 845069 (cuda:0)
- crm-loss-perdof: PID 845281 (cuda:1)
- crm-loss-conformal: PID 845499 (cuda:2)
- crm-loss-combined: PID 845729 (cuda:3)

**4. 预估完成时间**
每 epoch ~3 分钟，50 epochs ≈ 2.5 小时。conformal/combined 因额外 argmin 计算略慢，约 3 小时。预计 UTC 08:00 前完成。

---
