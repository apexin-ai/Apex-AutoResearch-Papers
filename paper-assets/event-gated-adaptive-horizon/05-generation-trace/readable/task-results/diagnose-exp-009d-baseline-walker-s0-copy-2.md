# diagnose exp 009d baseline walker s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_009d_baseline_walker_s0_20260515T121115_result.json`
- **Structured JSON:** [`9ce8e325ca73efe25b7a.json`](../../sessions/9c/9ce8e325ca73efe25b7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断报告

### 失败根因

**dm_control 的 OpenGL 渲染后端初始化失败。** 具体错误：

```
AttributeError: 'NoneType' object has no attribute 'glGetError'
```

调用链：`dreamer.py` → `dmc.DeepMindControl` → `from dm_control import suite` → dm_control 尝试加载 OSMesa 渲染器 → PyOpenGL 无法正确绑定 GL 库。

**根本原因：** 环境变量 `MUJOCO_GL` 和 `PYOPENGL_PLATFORM` 均未设置。dm_control 默认尝试 OSMesa，但 PyOpenGL 在当前环境下无法正确加载 OSMesa GL context。服务器有 NVIDIA GPU，应使用 EGL 后端进行 headless GPU 渲染。

### 建议修复

在训练命令中添加环境变量，将渲染后端切换为 EGL：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0"
```

关键改动：`python dreamer.py` → `MUJOCO_GL=egl python dreamer.py`

### cuda:0 当前状态

- **可用。** 两块 NVIDIA RTX PRO 6000 Blackwell (各 96GB)，GPU 利用率 0%，无任何进程占用
- 磁盘：250GB 数据盘仅用 13GB (5%)，空间充足

---
