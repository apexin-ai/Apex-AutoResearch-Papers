# infra kill 018s2 residual

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-018s2-residual_20260516T225113_result.json`
- **Structured JSON:** [`e8ae7505e1465b4a4a85.json`](../../sessions/e8/e8ae7505e1465b4a4a85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 018_s2 残留进程
- PID 612881 已成功 kill（原来占 cuda:0 约 3257MiB）

### 008d 状态 (cuda:0)
- PID 628482，运行 ~2 分钟，正常
- 显存 3257MiB，GPU-Util 23%，cuda:0 现在只有它一个进程

### 019a 状态 (cuda:1)
- **PID 628871 不存在**，cuda:1 上显存 1MiB，无任何进程
- 019a 似乎已经退出或未成功启动

### 最终 nvidia-smi

| GPU | 显存占用 | GPU-Util | 进程 |
|-----|---------|----------|------|
| cuda:0 | 3276MiB / 97887MiB | 23% | 628482 (008d) |
| cuda:1 | 1MiB / 97887MiB | 0% | 无 |

**需要关注**：019a (PID 628871) 已不在运行，cuda:1 空闲。是否需要重启 019a？

---
