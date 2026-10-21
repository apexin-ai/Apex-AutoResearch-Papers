# prep hopper phase2 validation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_hopper_phase2_validation_20260527T030515_result.json`
- **Structured JSON:** [`19cf5acb5655656ae7f3.json`](../../sessions/19/19cf5acb5655656ae7f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 2 预验证报告

### 磁盘状态
`/root/autodl-tmp/`: **247GB 可用**（仅用 3.2G/250G）。远超 20GB 要求。✓

### Phase 1 进度
| 实验 | 当前 step | 目标 | 进度 |
|------|-----------|------|------|
| exp_hopper_baseline | 5,000 | 105,000 | ~5% |
| exp_hopper_trained_s0 | 5,000 | 105,000 | ~5% |

两个 Phase 1 实验刚启动不久，距离完成还需较长时间。

### Phase 2 logdir 冲突检查
- `logdir/exp_hopper_frozen_s0` — 不存在 ✓
- `logdir/exp_hopper_trained_s1` — 不存在 ✓

### GPU
2x NVIDIA RTX PRO 6000 Blackwell (96GB each) — 双卡可用 ✓

### CLI 参数验证

**exp_hopper_trained_s1** — 所有参数有效 ✓
- `--gate_enabled`, `--gate_fixed_dt`, `--gate_subsample_max_dt`, `--gate_dt_embed_dim`(configs.yaml L111), `--imag_horizon` 均存在

**exp_hopper_frozen_s0** — ⚠️ 有问题：
| 参数 | 状态 |
|------|------|
| `--gate_dt_embed_dim 16` | ✓ 有效（configs.yaml L111，默认 32） |
| `--gate_freeze_dt_embed True` | ❌ **不存在** |

正确的 flag 是 **`--dt_emb_freeze True`**（configs.yaml L128，models.py L96-97 实现）。

### 第二个问题：exp_hopper_trained_s1 设备不一致

任务描述说用 `cuda:1, EGL_DEVICE_ID=1`，但实际命令中写的是 `--device cuda:0`。如果意图是双卡并行跑两个实验，应改为 `--device cuda:1`。

### 修正后的 exp_hopper_frozen_s0 命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_dt_embed_dim 16 --dt_emb_freeze True --imag_horizon 8
```

### 修正后的 exp_hopper_trained_s1 命令（如果要用 cuda:1）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s1 --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8
```

### 风险总结
1. **🔴 阻塞**：`--gate_freeze_dt_embed` flag 不存在，必须改为 `--dt_emb_freeze`
2. **🟡 注意**：exp_hopper_trained_s1 命令中 `--device cuda:0` 与描述中 `cuda:1` 不一致，需确认意图
3. **🟡 注意**：frozen 实验用 `--gate_dt_embed_dim 16`（非默认 32），确认这是有意为之

---
