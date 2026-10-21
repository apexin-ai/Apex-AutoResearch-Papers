# verify hopper hop env and commands

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_hopper-hop-env-and-commands_20260527T025247_result.json`
- **Structured JSON:** [`a4af2c34d58716f8701c.json`](../../sessions/a4/a4af2c34d58716f8701c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成，输出结果：

---

```
环境验证: OK (obs_spec: ['position', 'velocity', 'touch'], act_spec: (4,))
Task 名: dmc_hopper_hop
GPU: cuda:0 ~49GB 已用/98GB 总计(0% util) / cuda:1 空闲(0MB/98GB)
磁盘: 247 GB 可用 (/root/autodl-tmp/)

Dry-run: OK ([5000] eval_return 0.1 / eval_length 500.0 / eval_episodes 10.0)
```

### 训练命令

**exp_hopper_baseline** (seed=0, 标准 DreamerV3):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_baseline --steps 105000 --seed 0 --compile False --device cuda:0"
```

**exp_hopper_trained_s0** (seed=0, trained dt_emb):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 32"
```

**exp_hopper_trained_s1** (seed=1, trained dt_emb):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_trained_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 32"
```

**exp_hopper_frozen_s0** (seed=0, frozen dt_emb):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 32 --dt_emb_freeze True"
```

**exp_hopper_frozen_s1** (seed=1, frozen dt_emb):
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_hopper_hop --logdir logdir/exp_hopper_frozen_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 32 --dt_emb_freeze True"
```

### Flag 映射说明

用户指定的 flag 与实际代码 flag 的对应：
| 用户说的 | 实际 flag | 值 |
|---------|----------|---|
| `--gate_dt_embed_dim` | `--gate_dt_embed_dim` | 32 (configs.yaml 默认即 32) |
| `--subsample` | `--gate_subsample_max_dt` | 2 |
| `--gate_horizon 8` | `--imag_horizon` | 8 |
| `--freeze_dt_embed` | `--dt_emb_freeze` | True |

`eval_every` 默认 10000（configs.yaml `eval_every: 1e4`），与现有实验一致，无需显式传入。

---
