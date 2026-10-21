# check hopper frozen s0 config

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_hopper-frozen-s0-config_20260527T055417_result.json`
- **Structured JSON:** [`a5f4ad09779cd0959e86.json`](../../sessions/a5/a5f4ad09779cd0959e86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果：exp_hopper_frozen_s0 (PID 612905)

**进程状态**: Ss+, 已运行 3h29m, 当前在 step 5000

### 命令行参数核验

| 配置项 | 期望值 | 实际值 | 状态 |
|--------|--------|--------|------|
| `--dt_emb_freeze` | True | True | ✅ |
| `--gate_enabled` | True | True | ✅ |
| `--gate_fixed_dt` | 2 | 2 | ✅ |
| `--gate_subsample_max_dt` | 2 | 2 | ✅ |
| `--imag_horizon` | 8 | 8 | ✅ |
| `--seed` | 0 | 0 | ✅ |
| `--device` | cuda:0 | cuda:0 | ✅ |
| `--task` | dmc_hopper_hop | dmc_hopper_hop | ✅ |
| `--logdir` | logdir/exp_hopper_frozen_s0 | logdir/exp_hopper_frozen_s0 | ✅ |
| `--steps` | 105000 | 105000 | ✅ |
| `--gate_dt_embed_dim 16` | 不应存在 | 未出现 | ✅ |

### 环境变量

| 变量 | 值 | 状态 |
|------|-----|------|
| `CUDA_VISIBLE_DEVICES` | 0 | ✅ |
| `MUJOCO_EGL_DEVICE_ID` | 0 | ✅ (与 cuda:0 匹配) |
| `MUJOCO_GL` | egl | ✅ |

### 初始日志

Step 5000 指标正常。`gate_dt_mean=2.0`, `gate_dt_std=0.0`, `gate_dt_2_frac=1.0` — 与 frozen (fixed_dt=2) 配置完全一致，gate 未学习，全部输出 dt=2。

**结论：全部 11 项配置验证通过，无异常。**

---
