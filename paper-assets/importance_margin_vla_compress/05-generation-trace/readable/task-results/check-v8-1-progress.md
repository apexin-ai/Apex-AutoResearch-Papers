# check v8 1 progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v8_1-progress_20260516T034659_result.json`
- **Structured JSON:** [`0239d3629b0102a410fa.json`](../../sessions/02/0239d3629b0102a410fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v8_1 训练状态

| 指标 | 值 |
|------|------|
| **当前 step** | 6200 / 30000 (20.7%) |
| **最新 checkpoint** | step_006000 (1.19GB, 11:46:19 保存) |
| **速度** | 3.1 steps/s，~16.2s per 50 steps |
| **最新 loss** | total=0.0039, action=0.0039, margin=0.0 |
| **Δ (margin)** | 0.679 |
| **LR** | 9.25e-05 (衰减中) |
| **Lip 监控** | empirical_L=0.0976, spectral_norm=1.0003 (稳定) |

**GPU 利用率**:

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 87% | 2.5 / 97.9 GB |
| 1 | RTX PRO 6000 Blackwell | 83% | 10.4 / 97.9 GB |

**预计剩余时间**: 剩余 23800 steps ÷ 3.1 sps ≈ **7677s ≈ 2小时8分钟**（约 13:55 完成）。

训练正常运行，loss 收敛良好，Lipschitz 约束稳定在 ~0.1 / spectral norm ~1.0。

---
