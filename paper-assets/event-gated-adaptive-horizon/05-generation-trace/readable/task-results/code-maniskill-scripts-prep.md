# code maniskill scripts prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_maniskill-scripts-prep_20260516T192950_result.json`
- **Structured JSON:** [`83c1588842f433126941.json`](../../sessions/83/83c1588842f433126941.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建并注册：

**019a** `exp_019a_pickcube_baseline.sh` — PickCube baseline 重启，修正点：
- `MUJOCO_GL=egl` + `MUJOCO_EGL_DEVICE_ID=${EGL_ID}`
- `--checkpoint_every 25000`
- logdir 改为代码目录下 `logdir/exp_019a_pickcube_baseline`

**019b** `exp_019b_pickcube_civo_trigger.sh` — PickCube CIVO trigger，在 019a 基础上加：
- `--gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8`
- `gate_dt_embed_dim` 保持默认 32（trained dt_emb）

两个脚本均使用 `${CUDA_ID}` / `${EGL_ID}` 占位符，提交时指定即可。服务器验证 `maniskill_state` config 和所有 gate 参数均存在。

---
