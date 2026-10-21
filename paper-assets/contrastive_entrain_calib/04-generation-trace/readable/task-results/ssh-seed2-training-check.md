# ssh seed2 training check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed2-training-check_20260522T021055_result.json`
- **Structured JSON:** [`da2c8d936b25efe0f634.json`](../../sessions/da/da2c8d936b25efe0f634.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003-s2 训练状态

**进程**: 存活，已运行 2天1小时54分钟

**当前进度**: step **6143/8000** (77%)，比之前的 4106 前进了 ~2037 步

**速度**: ~25.0s/step

**ETA**: 剩余 1857 步 × 25s ≈ **12.9 小时**，预计约 5月22日 23:00 完成

**关键指标** (最近几个 logging step):
- loss: 0.0007–0.0008
- reward mean: 0.58–0.67
- kl: 0.017–0.019
- entropy: 0.30–0.32

**Checkpoint 列表** (29046 上):

| Checkpoint | 时间 | 状态 |
|---|---|---|
| ckpt-500 ~ ckpt-4000 | 5/20–5/21 | 旧 |
| **ckpt-4500** | 5/21 22:30 | **新** |
| **ckpt-5000** | 5/22 02:04 | **新** |
| **ckpt-5500** | 5/22 05:36 | **新** |
| **ckpt-6000** | 5/22 09:10 | **新** |

ckpt-4000 之后新增了 4 个 checkpoint（4500/5000/5500/6000）。ckpt-6500 预计约 5月22日 12:40 生成。

需要我检查 28034 上是否已有这些 checkpoint，或准备 SCP 命令？

---
