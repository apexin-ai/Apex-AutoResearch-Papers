# ops westd10894 reconnect

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd10894_reconnect_20260523T033737_result.json`
- **Structured JSON:** [`160d0110f022a6482ca1.json`](../../sessions/16/160d0110f022a6482ca1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## westd-10894 状态

### 1. 连接：成功
4x NVIDIA RTX PRO 6000 Blackwell (96GB each)，uptime 158 天。

### 2. cutoff_s2 训练：**存活，正常运行中**
- PID: 275630，运行约 3 小时
- 当前 step: **~21990 / 50005** (44%)
- 速度: ~2.06 it/s
- GPU 0 显存占用: 43021 MiB / 97887 MiB
- 已保存 checkpoint: 10000_chkpt, 20000_chkpt
- 预计剩余时间: ~3h47m（约 15:30 完成）

### 3. 磁盘状态
| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 21G | 9.1G | 70% |
| /root/autodl-tmp | 250G | 126G | 125G | 51% |

磁盘充足，无风险。

### 4. 关键 checkpoint 完整性
| 条件 | 50000 checkpoint |
|------|-----------------|
| ablation_occ_detach_s2 | ✓ |
| ablation_random_occ_s2 | ✓ |
| depth_s2 | ✓ |
| depth_s3 | ✓ |
| cutoff_s2 | 训练中 (当前 ~22k/50k) |

注：vanilla_s2 的 checkpoint 目录不存在（只有一个 `vanilla_s2_train.log` 文件），detach_s0 和 random_s0 的 checkpoint 也不在这台机器上（可能在其他服务器）。

### 5. 无需恢复操作
训练进程正常运行，tmux session `cutoff_s2` 存活，无需干预。

---
