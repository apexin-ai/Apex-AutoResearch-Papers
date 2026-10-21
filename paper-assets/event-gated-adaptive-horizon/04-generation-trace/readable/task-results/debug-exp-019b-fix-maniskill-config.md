# debug exp 019b fix maniskill config

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_exp_019b_fix_maniskill_config_20260517T033711_result.json`
- **Structured JSON:** [`d1ec5f629425e38ecfc8.json`](../../sessions/d1/d1ec5f629425e38ecfc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**错误原因**：`configs.yaml` 中没有名为 `maniskill` 的配置块。可用的 ManiSkill 配置块是：
- `maniskill_state` (PickCube-v1)
- `maniskill_stackcube` (StackCube-v1)
- `maniskill_peginsertion` (PegInsertionSide-v1)

**修复**：将 `--configs defaults maniskill` 改为 `--configs defaults maniskill_state`。无需修改代码。

**Dry-run 结果**：通过。环境正常创建，obs shape `(42,)`，action shape `(8,)`，训练跑到 step 2600，`train_return=4.7`。

**正确的重新提交命令**：

```bash
bash -c "unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 1 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_019b_pickcube_civo_trigger"
```

唯一改动：`maniskill` → `maniskill_state`。

---
