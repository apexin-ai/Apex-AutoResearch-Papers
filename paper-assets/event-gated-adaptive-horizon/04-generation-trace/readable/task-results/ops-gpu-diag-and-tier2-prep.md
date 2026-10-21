# ops gpu diag and tier2 prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-diag-and-tier2-prep_20260527T205945_result.json`
- **Structured JSON:** [`3e2a8ef9c6fb1a45bc55.json`](../../sessions/3e/3e2a8ef9c6fb1a45bc55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总如下。

---

## 1. GPU 诊断报告

### GPU 状态

| GPU | 型号 | 显存占用 | Compute Util |
|-----|------|---------|--------------|
| 0 | RTX PRO 6000 Blackwell 98GB | 53862 / 97887 MiB (55%) | **21%** |
| 1 | RTX PRO 6000 Blackwell 98GB | 4690 / 97887 MiB (5%) | **16%** |

### 训练进程

| 实验 | PID | GPU | Step | Return | CPU% |
|------|-----|-----|------|--------|------|
| exp_cheetah_008a_s2 | 652652 | cuda:0 | 28000/105K | 352-363 | 1419% |
| exp_cheetah_008a_s3 | 652815 | cuda:1 | 28000/105K | 164-226 | 1407% |

启动时间 04:22 UTC，运行 ~38min 完成 28K steps → **~737 steps/min** → **预计 06:45 UTC 完成**（约 1h45m 后）。

### 瓶颈分析

**低 GPU 利用率是正常的，不是瓶颈。** 原因：

1. **DMC proprio 用的是 DreamerV3-S 小模型**，`batch_size=10, batch_length=20`（dmc_proprio config override），GPU 瞬间算完
2. **CPU-bound 环境交互占主导** — MuJoCo 环境模拟是串行 CPU 操作，每个进程 ~1400% CPU（235 线程）
3. DreamerV3 的 train-env 交替模式决定了 GPU 大部分时间在等 CPU 产数据

**异常点**：GPU 0 显存 53.8GB 远高于 GPU 1 的 4.7GB，同一模型不应有此差异。可能是 CUDA 内存碎片或先前实验残留。不影响训练但值得留意。

---

## 2. Tier 2 实验命令（Walker 008d seed 6, 7）

参考实验 `exp_009e_008d_walker_s1` 的 spec：Walker Walk, trained dt_emb, subsample ON (`gate_subsample_max_dt=2`), `imag_horizon=8`, `gate_fixed_dt=2`, 105K steps。

代码版本：`dreamer.py` 最后修改 May 17 15:58，与当前运行实验一致。服务器无 git repo（代码通过 rsync 部署）。

```
exp_walker_008d_s6:
  gpu: cuda:0
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s6 --steps 105000 --seed 6 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8"

exp_walker_008d_s7:
  gpu: cuda:1
  command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_walker_008d_s7 --steps 105000 --seed 7 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8"
```

两个实验 ready to submit。等当前 cheetah 008a s2/s3 完成后（~06:45 UTC）即可启动。

---
