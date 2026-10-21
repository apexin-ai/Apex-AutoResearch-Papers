# monitor v7 2 progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v7_2_progress_20260515T210548_result.json`
- **Structured JSON:** [`c6ec5cffed1dce79d0ff.json`](../../sessions/c6/c6ec5cffed1dce79d0ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_imm_anchor_v7_2 训练状态

| 指标 | 值 |
|------|-----|
| **当前 step** | 20000 / 30000 (66.7%) |
| **运行时间** | 1h46m |
| **速度** | 3.1 steps/s，稳定 |
| **GPU** | cuda:0, 55% 利用率, 2461 MiB / 97887 MiB |

### 最新 metrics (step 20000)
| 指标 | 值 |
|------|-----|
| action_loss | 0.0028 |
| margin_loss | 0.0000 |
| total_loss | 0.0028 |
| Δ (margin) | 0.3959 |
| grad_norm | 0.16 |
| lr | 2.84e-05 |

### LIP_MONITOR 趋势
| step | empirical_L | spectral_norm |
|------|-------------|---------------|
| 18000 | 0.1326 | 1.0003 |
| 18500 | 0.1954 | 1.0003 |
| 19000 | 0.2394 | 1.0004 |
| 19500 | 0.1818 | 1.0003 |
| 20000 | 0.1640 | 1.0004 |

### 分析
- **SN 稳定在 ~1.0003-1.0004**，spectral norm 约束有效
- **L_emp 在 0.13-0.24 范围波动**，相比早期（step 500 L_emp=0.0432, step 1000 L_emp=0.0638）有所上升，但仍然远小于 1，Lipschitz 约束满足
- **margin_loss 频繁为 0**（step 18150/18350/18850/19200/19400/19550/19600/19650/19850/20000），说明很多 batch 的 Δ 已经超过 margin δ=0.3，不触发 margin loss
- **grad_norm 偶有 spike**（step 18450 grad=8.68, step 19750 grad=11.99），但在 grad_clip=30.0 以内，未被裁剪
- 无 NaN、OOM 或异常

### 预计剩余时间
剩余 10000 steps ÷ 3.1 sps ≈ **54 分钟**，预计 ~05:00 UTC+8 完成（约 06:01）。

**注意**：进程使用的 config 文件是 `configs/imm_anchor_v7_1.yaml`，checkpoint 目录为 `checkpoints/imm_anchor_v7_1/`，不是 `v7_2`。最新 checkpoint 已保存到 step_020000。

---
