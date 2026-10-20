# infra fix training timeout

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-training-timeout_20260520T091346_result.json`
- **Structured JSON:** [`4e02baa3d4594a85e29b.json`](../../sessions/4e/4e02baa3d4594a85e29b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据清晰了。以下是完整诊断和建议。

---

## 诊断结果

### 1. Timeout（已修复，但有副作用）

- 3 个 `timeout 64800` (18h) 进程包裹训练
- **kill timeout 时，SIGTERM 被转发给了子进程组，训练一起被杀**
- 无 checkpoint（save_freq=10000，只完成 ~1900 步）
- **已重启** 3 个训练（无 timeout），当前正在跑

### 2. I/O + GPU 瓶颈根因

**主要瓶颈是 GPU 0 竞争，而非纯 I/O：**

| 资源 | 竞争情况 |
|------|----------|
| **GPU 0** | 训练 s0 (62 GB) + **10 个 occ 提取进程** (各 557 MB, 共 5.6 GB)，利用率 99% |
| GPU 1/2 | 仅训练 s1/s2，正常 |
| CPU | 3 训练 (~5400% total) + 11 occ (~3300% total)，208 核够用但 sys 18%（调度开销） |
| 磁盘 md0 | 训练读 data + occ 读 datasets，I/O wait 0% 但 RAID 吞吐被分享 |

**训练速度特征**（重启后仍存在）：
- 基线 ~1.0-1.05 s/it
- 周期性 spike 到 2.5-3.4 s/it（每 ~15 步一次）
- 平均被拉到 ~1.5-1.8 s/it

### 3. Occ 提取状态

- 10 个任务（task 0-9）已跑 ~2h，产出 10 个 hdf5 文件 (24 MB)
- 文件在过去 20 秒内无增长 → 还在计算中间步骤，远未完成
- 每个进程 ~2.3 GB RAM + 254 线程 + GPU 渲染

### 建议：SIGSTOP occ 提取

**暂停（不是 kill）occ 提取**，理由：
- **有 occ**：~1.8 s/it 均值 → 50005 步需 ~25h
- **无 occ**：~1.02 s/it → 50005 步需 ~14.2h，节省 ~11h
- SIGSTOP 保留进程状态和 GPU 显存，训练完成后 SIGCONT 恢复

是否立即执行 SIGSTOP？

---
