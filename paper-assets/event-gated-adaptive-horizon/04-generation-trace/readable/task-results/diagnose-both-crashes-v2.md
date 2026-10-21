# diagnose both crashes v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_both_crashes_v2_20260515T121214_result.json`
- **Structured JSON:** [`13346655b084d48530e7.json`](../../sessions/13/13346655b084d48530e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已成功启动，正在正常运行。

## 诊断结论

**共同根因**: conda 环境的 `libstdc++.so.6` 只支持到 `GLIBCXX_3.4.26`，而系统的 `libOSMesa.so` → `libLLVM-15.so.1` 需要 `GLIBCXX_3.4.30`。导致 PyOpenGL 无法加载 GL backend，`_p.GL` 为 `None`，触发 `AttributeError: 'NoneType' object has no attribute 'glGetError'`。

**修复**: 启动命令中添加两个环境变量：
- `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6` — 强制使用系统的新版 libstdc++
- `MUJOCO_GL=osmesa` — 指定 dm_control 使用 OSMesa 渲染

**当前状态**:
- `exp_009d_baseline_walker_s0` (cuda:0) — 已启动，创建环境中
- `exp_015b_frozen_dt_emb` (cuda:1) — 已启动，正在 prefill dataset

注意：exp_015b 的 device 我改成了 `cuda:1`（原命令写的 `cuda:0`，与 exp_009d 冲突）。

---
