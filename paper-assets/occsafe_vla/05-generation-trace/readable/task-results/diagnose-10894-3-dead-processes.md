# diagnose 10894 3 dead processes

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_10894-3-dead-processes_20260527T103921_result.json`
- **Structured JSON:** [`7c0f2d8f66b19270ded4.json`](../../sessions/7c/7c0f2d8f66b19270ded4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：所有 4 个进程均存活

**进程没有消失。** PID 完全匹配，GPU 利用率 82-99%。只是 tmux session 断了（fd/0 → `/dev/pts/0 (deleted)`），但进程因 stdout/stderr 已重定向到日志文件而继续运行。

---

### 各实验状态

| 实验 | GPU | PID | 当前 step | 目标 | 速度 | 预计完成 (UTC) | 状态 |
|------|-----|-----|----------|------|------|---------------|------|
| full_occ_ln_v2_s1c_r2 | cuda:0 | 481426 | **34,305** / 50,005 | 50k | ~1.05 it/s | ~22:50 May 27 | 正常运行 |
| full_occ_ln_v2_s2_r2 | cuda:1 | 481643 | **34,449** / 50,005 | 50k | ~1.07 it/s | ~22:40 May 27 | 正常运行 |
| detach_ln_v2_s0c_r3 | cuda:2 | 543255 | **5,859** / 50,005 | 50k | ~1.06 it/s | ~06:20 May 28 | 正常运行 |
| full_occ_ln_s4 | cuda:3 | 553813 | **4,023** / 50,005 | 50k | ~1.05 it/s | ~06:50 May 28 | 正常运行 |

### Checkpoint 情况

- **s1c_r2**: `/root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/` — 有 20000_chkpt, 30000_chkpt（无 50000 yet）
- **s2_r2**: `/root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/` — 有 20000_chkpt, 30000_chkpt（无 50000 yet）
- **s0c_r3**: `/root/autodl-tmp/checkpoints/detach_ln_v2_s0c_r3/` — 仅 running checkpoint
- **s4**: `/root/autodl-tmp/checkpoints/full_occ_ln_s4/` — 仅 running checkpoint

### 日志路径

- s1c_r2 → `/root/runs/occsafe_vla/full_occ_ln_v2_s1c.log`
- s2_r2 → `/root/runs/occsafe_vla/full_occ_ln_v2_s2.log`
- s0c_r3 → `/root/autodl-tmp/checkpoints/detach_ln_v2_s0c_r3.log`
- s4 → `/root/autodl-tmp/checkpoints/full_occ_ln_s4.log`

### 关键信息

- **磁盘**: 45% (112G/250G)，不是磁盘问题
- **所有 4 个实验预计在 DDL（May 28 12:00 UTC）前完成**
- **空闲 GPU: 无** — 4 张卡全在跑
- tmux session 可能因网络断开或手动关闭消失，但进程不受影响（nohup/重定向保护了它们）

---
