# ops 10894 progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-progress-check_20260526T224023_result.json`
- **Structured JSON:** [`85d45633b17405c33ba8.json`](../../sessions/85/85d45633b17405c33ba8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总（May 27 06:40 UTC）

### GPU 使用
| GPU | 实验 | 温度 | 显存 | 利用率 |
|-----|------|------|------|--------|
| 0 | reverse_cutoff_s2_v2 | 73°C | 62G/98G | 99% |
| 1 | full_occ_ln_v2_s0 | 71°C | 62G/98G | 99% |
| 2 | full_occ_ln_v2_s1 | 70°C | 63G/98G | 96% |
| 3 | detach_ln_v2_s0 | 72°C | 62G/98G | 99% |

### 实验详情

| 实验 | 当前 step | 进度 | 速度 | 预计完成 (UTC) |
|------|-----------|------|------|----------------|
| **reverse_cutoff_s2_v2** | 47672/50005 | 95% | ~1.06 it/s | **~07:17** (约37分钟后) |
| **full_occ_ln_v2_s0** | ~15700/50005 (估算) | ~31% | ~1.08 it/s | **~15:30** |
| **full_occ_ln_v2_s1** | ~15500/50005 (估算) | ~31% | ~1.08 it/s | **~15:35** |
| **detach_ln_v2_s0** | ~15600/50005 (估算) | ~31% | ~1.08 it/s | **~15:33** |

### 备注
- **reverse_cutoff_s2_v2**: 即将完成，50000_chkpt 尚未生成（30k/40k chkpt 已存在）
- **后三个实验**: 之前的运行在 02:08-02:09 UTC 崩溃（exitcode 2），已用新 PID 重启。stdout 输出到 tmux 终端 (/dev/pts/1)，无独立日志文件，step 数基于 10000_chkpt 保存时间（~05:12）推算。wandb 未启用
- **三个实验 ETA ~15:30 UTC**，在 deadline（05-28 12:00 UTC）前约 20.5 小时完成，时间充足

### 磁盘
- `/root/autodl-tmp`: 171G / 250G（69%），剩余 80G，充足

---
