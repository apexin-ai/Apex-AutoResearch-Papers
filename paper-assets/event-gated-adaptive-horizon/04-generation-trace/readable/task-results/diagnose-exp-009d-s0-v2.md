# diagnose exp 009d s0 v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_009d_s0_v2_20260515T121027_result.json`
- **Structured JSON:** [`e39304a8c954090bd25a.json`](../../sessions/e3/e39304a8c954090bd25a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**错误信息**：
```
AttributeError: 'NoneType' object has no attribute 'glGetError'
```
发生在 `dm_control` → `PyOpenGL` → `OSMesa` 初始化链中。OSMesa 库存在（`/usr/lib/x86_64-linux-gnu/libOSMesa.so.8.0.0`），`dreamer.py` 也在第 7-8 行正确设置了 `MUJOCO_GL=osmesa` 和 `PYOPENGL_PLATFORM=osmesa`。

**根因**：缺少 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6`。

conda activate 后，conda 自带的 `libstdc++.so.6` 会覆盖系统版本，导致 OSMesa 加载失败（返回 None）。所有成功实验的脚本（`multi_seed_runs.sh`、`cheetah_run_experiments.sh` 等）都包含这个 export，但本次提交命令遗漏了。

**对比**：

失败命令：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py ...
```

成功模板（来自 `multi_seed_runs.sh`）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py ...
```

**修正命令**：
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0"
```

（`MUJOCO_GL` 和 `PYOPENGL_PLATFORM` 已在 dreamer.py 中设置，可省略；`LD_PRELOAD` 是唯一必须通过环境变量传入的。）

---
