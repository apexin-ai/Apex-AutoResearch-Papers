# ops diagnose 34685 io

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_34685_io_20260524T041301_result.json`
- **Structured JSON:** [`92a1dc0106a78364d0f0.json`](../../sessions/92/92a1dc0106a78364d0f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 磁盘类型：HDD RAID5（这是核心问题）
- `/dev/md127`: **3块 HDD 组成的 RAID5**（sdb, sdc, sdd），rotational=1
- RAID5 对并发随机写性能极差（需要 read-modify-write），是4进程并发 I/O 的最差选择

### 2. Checkpoint 同步写入确认
每个 checkpoint **15GB**，save_freq 全部是 **10000**。

| 实验 | 10000_chkpt | 20000_chkpt | 30000_chkpt |
|------|------------|------------|------------|
| cutoff_45k_s0 | 05:45 | 08:58 | — |
| cutoff_15k_s0 | 05:30 | 08:40 | **11:59** |
| cutoff_25k_s1 | **09:55:25** | 即将到来 | — |
| reverse_cutoff_s1 | **09:55:25** | 即将到来 | — |

**GPU 2 和 GPU 3 完全同步**——同时启动（06:32）、同速推进、同时保存。两个 15GB 同时写入 = 30GB 砸到 HDD RAID5 上。

### 3. 速度跌落模式分析

日志中观察到**两种**跌落模式：

**模式 A：大尖峰（checkpoint save）**
- 持续 30-90 秒，速度从 1.08 → 0.28 it/s（3.6s/it），降幅 75%
- 发生在 checkpoint 保存时（GPU 2/3 同步 save 时所有 4 个进程都受影响）

**模式 B：小尖峰（数据加载竞争）**
- 持续 3-5 个 iteration，速度从 1.08 → 0.95 it/s，降幅 10-15%
- **四个进程在同一 wall clock 时间同步出现**（例如 ~12:12 所有 4 个进程同时出现尖峰）
- 原因：4 个进程从同一 HDD RAID5 读取 tfrecord 数据，随机 seek 互相干扰

### 4. 额外问题
`checkpoint_rotation.sh` 只监控 `cutoff_s0 cutoff_s1 depth_s0 depth_s1`，**不匹配当前实验名**，旧 checkpoint 不会被清理。磁盘已用 274G/350G (79%)，继续积累会爆盘。

### 5. 建议

**优先级 1：错开 GPU 2/3 的 save 时机**
最简单的方式：在 cutoff_25k_s1 或 reverse_cutoff_s1 的下一个 checkpoint 后，用不同 save_freq（如 10000 vs 10001）或手动错开启动时间，避免两个 15GB 同时写入。

**优先级 2：只保存 LoRA adapter 权重**
当前每个 checkpoint 保存完整模型（4 个 safetensors ~14.5GB）+ adapter（~500MB）。如果代码支持只保存 adapter，checkpoint 大小从 15GB 降到 500MB，I/O 影响可忽略不计。

**优先级 3：修复 checkpoint_rotation.sh**
更新监控目录名匹配当前 4 个实验，避免磁盘打满。

**优先级 4：增大 save_freq**
如果不需要那么密的 checkpoint，改为 20000 减少一半写入事件。

**数据加载竞争无法根本解决**（硬件限制），但 checkpoint I/O 是可控的最大改善空间。

---
