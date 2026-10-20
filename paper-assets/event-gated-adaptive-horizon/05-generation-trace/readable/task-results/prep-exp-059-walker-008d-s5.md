# prep exp 059 walker 008d s5

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp_059_walker_008d_s5_20260524T030707_result.json`
- **Structured JSON:** [`6d4b19e3dadf86138d39.json`](../../sessions/6d/6d4b19e3dadf86138d39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成

**Seed**: 5（seeds 0-4 均已被使用或可能被使用）

**Registry**: `exp_059_walker_trained_s5` 已创建，状态 PENDING，等待审批。

**训练命令**（部署到 bjb1-45299:cuda:1）：

```bash
CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --gate_enabled True \
  --gate_fixed_dt 2 \
  --gate_subsample_max_dt 2 \
  --gate_subsample_min_dt 1 \
  --imag_horizon 8 \
  --seed 5 \
  --steps 210000 \
  --checkpoint_every 25000 \
  --compile False \
  --device cuda:0 \
  --logdir ./logdir/exp_059_walker_trained_s5
```

**注意**: s3 模板实际跑了 105000 步，你指定了 210000。如果需要与 s3 完全一致应改为 105000。

---
