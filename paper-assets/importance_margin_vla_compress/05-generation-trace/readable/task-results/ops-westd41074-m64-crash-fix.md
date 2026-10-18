# ops westd41074 m64 crash fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-m64-crash-fix_20260521T032717_result.json`
- **Structured JSON:** [`3d0585013bd9376856fe.json`](../../sessions/3d/3d0585013bd9376856fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实际情况与任务预期完全不同。总结如下：

## 现状分析

### GPU 3 (PID 738642) — 不是僵尸
PID 738642 是一个**健康运行的 M64 v4 新训练**，10:44:22 启动，从 step 0 开始（非 resume），当前已到 step 1250，正常训练中（sps=0.5）。nvidia-smi 的 0% GPU util 是采样时机问题。

### M64 checkpoint — 全部丢失
磁盘上没有任何 M64 checkpoint 文件。旧训练在 step 50000 save 时 crash，之前的 step 10000-40000 checkpoint 要么被清理了，要么从未保存。**无法从 step 40000 resume。**

### M96 (PID 68539, GPU 2) — 正常运行
M96 训练在 step 41800，正常推进中。

### 磁盘空间
57GB 可用，已足够。M128 目录有 38GB 的 checkpoint（checkpoint.pt + checkpoint_step20000.pt），如需要可清理。

## 结论

**无需操作。** M64 v4 已经有人重新启动，从头训练，当前 step 1250。kill 僵尸和 resume 训练两个步骤都不需要执行。

需要确认：
1. M64 从头训练是否符合预期？还是需要 kill 掉重新想办法？
2. M128 的 38GB checkpoint 是否可以清理（保留最新的一个）？

---
