# code plan015B freeze dt emb

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan015B-freeze-dt-emb_20260515T085331_result.json`
- **Structured JSON:** [`0f9a5454ca41e9a2e97f.json`](../../sessions/0f/0f9a5454ca41e9a2e97f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

### 产出总结

**1. Detach 回滚** — 3 处修改已 `git checkout` 回滚（configs.yaml, networks.py, models.py）

**2. Freeze 实现** — commit `dccb867`，2 个文件 6 行改动：
- `configs.yaml:119` — `dt_emb_freeze: false`
- `models.py:96-98` — `WorldModel.__init__` 中 freeze（optimizer 创建前，确保 frozen param 不会被 optimizer 更新）
- `models.py:230-231` — `_train` 中 `RequiresGrad.__enter__` 后重新 freeze（因为 `requires_grad_(True)` 会覆盖）

**关键发现**: DreamerV3 的 `RequiresGrad` 上下文管理器会 `model.requires_grad_(True)` 覆盖所有参数，所以仅在 `__init__` 中 freeze 不够，必须在 `_train` 入口重新 freeze。

**3. Dry run** — step 200 无报错，requires_grad 验证正确

**4. 待执行提交命令**（等 009e 完成后提交到 cuda:1）：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && \
export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && \
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
nohup python -u dreamer.py --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_015b_frozen_dt_emb \
  --steps 105000 --seed 1 --compile False --device cuda:1 \
  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \
  --imag_horizon 8 --dt_emb_freeze True \
  > logdir/exp_015b_frozen_dt_emb.log 2>&1 &
```

---
