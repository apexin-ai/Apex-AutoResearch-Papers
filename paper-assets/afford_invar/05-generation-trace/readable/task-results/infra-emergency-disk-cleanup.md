# infra emergency disk cleanup

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_emergency-disk-cleanup_20260520T000516_result.json`
- **Structured JSON:** [`82537c436bcd87eaf62e.json`](../../sessions/82/82537c436bcd87eaf62e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 执行结果

### 磁盘状态
| | 清理前 | 清理后 |
|---|---|---|
| 根分区 `/root` | 30G / **100%** (276K 剩余) | 30G / **33%** (21G 剩余) |
| 数据盘 `/root/autodl-tmp` | 125G / 36% | 140G / 40% (211G 剩余) |

### 删除的 checkpoint
afford 目录 (`libero_goal_no_noops+afford+b2+lr0.0005+a0.1/`) 删除了 8 个 checkpoint，每个 756M，共释放 ~6G：
- checkpoint-1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000

**保留**：checkpoint-500, checkpoint-1000

### 软链接
```
/root/afford_invar/runs -> /root/autodl-tmp/afford_invar/runs
```
创建成功，两个子目录均可正常访问。

### 训练进程状态
- **phase1_lconsist_v1_cont (PID 116255)**：已死亡（被 signal 15 kill）。无活跃训练进程。
- **phase1_oft_baseline**：无对应 python 进程在运行。
- **phase1_transfer_v1**：已 kill，transfer 目录的 18 个 checkpoint（含不完整的 checkpoint-9000）已迁移到数据盘。
- 当前服务器上 **无任何训练进程在运行**，只有系统服务（tensorboard、jupyter、sshd）。

---
