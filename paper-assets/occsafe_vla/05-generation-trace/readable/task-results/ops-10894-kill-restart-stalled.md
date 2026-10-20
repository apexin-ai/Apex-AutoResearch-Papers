# ops 10894 kill restart stalled

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-kill-restart-stalled_20260526T235314_result.json`
- **Structured JSON:** [`08853e584a51f33ab8d1.json`](../../sessions/08/08853e584a51f33ab8d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Stall 根因
三个进程（390852, 391060, 391402）均在 step 270-275 静默挂起，日志中无任何 error/exception/OOM/NCCL 信息。进程状态 `Rsl`（多线程运行态），但 GPU util 0%。最可能原因：**数据管道或 NCCL 集合通信死锁**（torchrun 单节点单卡也会初始化 NCCL backend，某些 tf.data + torch dataloader 交互场景下可触发静默阻塞）。

### 2. 三个重启状态
全部成功提交：

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| full_occ_ln_v2_s0b | cuda:1 | 458224 | 启动中（550 MiB，加载模型） |
| full_occ_ln_v2_s1b | cuda:2 | 458541 | 启动中（550 MiB，加载模型） |
| detach_ln_v2_s0b | cuda:3 | 458889 | 启动中（550 MiB，加载模型） |

### 3. cuda:0 PID 433768
- **身份**: `detach_ln_v2_s1`（occ_detach=true, seed 43）
- **运行时间**: 27 分钟
- **GPU 显存**: 63004 MiB / 97887 MiB
- **GPU 利用率**: 99%
- **状态**: 正常运行
- cuda:0 上还有 PID 428963（16760 MiB），可能是配套的 eval 或数据加载进程

### 4. 磁盘
`/root/autodl-tmp`: 127G used / 250G total（51%），124G 可用，充足。

---
