# code exp 006 fixed dt2 prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_006_fixed_dt2_prep_20260513T205612_result.json`
- **Structured JSON:** [`b5cef082371477f5f00b.json`](../../sessions/b5/b5cef082371477f5f00b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_005 正常运行（PID 51726，1071% CPU，已运行 5h）。

---

## 汇报

### 改动文件

**configs.yaml** (1 行)
- L114: 新增 `gate_fixed_dt: 0`

**models.py** (8 处, ~18 行净增)
- L188-196: `WorldModel._train` — `gate_fixed_dt > 0` 时跳过 gate curriculum，直接用固定 `effective_max_dt` 和 `gate_scale=0.0`
- L245: gate loss 条件追加 `and self._config.gate_fixed_dt == 0`，跳过 gate loss 计算
- L314: gate metrics 条件追加 `and self._config.gate_fixed_dt == 0`，跳过 gate_loss/gate_scale/entropy_bonus 日志
- L547: `_imagine` 中 `gate_active` 条件追加 `and config.gate_fixed_dt == 0`
- L562: fallback dt 改用 `torch.full((batch,), fixed, ...)` 支持任意固定值
- L572-573: `init_dt` 乘以 `gate_fixed_dt`，确保第一步也用固定 dt

### dry-run 结果
- 训练正常启动，无报错
- `gate_dt_mean=2.0`, `gate_dt_std=0.0`, `gate_dt_2_frac=1.0` — dt 恒定为 2
- gate_loss、gate_scale、gate_entropy_bonus 未输出（符合预期）
- exp_005 不受影响（仍在运行）

### exp_006_fixed_dt2 启动命令

```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && \
export MUJOCO_GL=osmesa && \
export PYOPENGL_PLATFORM=osmesa && \
CUDA_VISIBLE_DEVICES=0 python dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/fixed_dt2_v1_s1 \
  --steps 150000 \
  --seed 1 \
  --compile False \
  --device cuda:0 \
  --gate_enabled True \
  --gate_fixed_dt 2
```

### 预估训练时长
exp_005 的 fps ~6.69 步/秒。Fixed dt 省去 gate forward pass（~200K 参数），预估 fps ~7-8。150K 步约 **5-6 小时**。

---
