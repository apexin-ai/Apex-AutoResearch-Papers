# infra check m64 m96 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-m64-m96-status_20260520T030558_result.json`
- **Structured JSON:** [`28450e3c3118e9f06627.json`](../../sessions/28/28450e3c3118e9f06627.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

```
westd-41074:
  GPU 0: train_openvla_sc_m128_vtconly_seed42  PID=26118  启动=02:33  30119MiB  0% util
  GPU 1: 空闲 (0MiB) — C5 RoboFlamingo 已释放 ✓
  GPU 2: train_openvla_sc_m96_seed42   PID=63701  启动=10:47  28490MiB  51% util ← M=96
  GPU 3: train_openvla_sc_m64_seed42   PID=63780  启动=10:47  27462MiB   0% util ← M=64

westd-27271:
  GPU 0: train_openvla_sc_m128_seed42  PID=841334  启动=02:38  32285MiB  18% util
  GPU 1: train_openvla_sc_m32_seed42   PID=855140  启动=08:16  25982MiB   0% util ← M=32

M=96 启动状态: YES
  PID=63701, 启动 10:47:15, 当前 step=250/100000, loss=4.29, sps=0.5
  trainable=403177472 (5.07%), wandb=offline-64kpy4bf
  预计 100k steps 耗时: ~55h (0.5 sps)

M=64 启动状态: YES
  PID=63780, 启动 10:47:17, 当前 step=300/100000, loss=4.09, sps=0.6
  trainable=403046400 (5.07%), wandb=offline-h0ynctgj
  预计 100k steps 耗时: ~46h (0.6 sps)
```

两个 M-sweep 实验均已成功启动约 20 分钟，loss 正常下降（初始 16-18 → 当前 4.0-4.3），梯度稳定收敛。M=64 因 token 数更少，sps 略快（0.6 vs 0.5）。GPU 1 已如 D095 决定释放。

---
