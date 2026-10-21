# ops 10894 progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-progress-check_20260526T192927_result.json`
- **Structured JSON:** [`cd677989870f5194ab62.json`](../../sessions/cd/cd677989870f5194ab62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况清楚了。汇报如下：

---

## 训练进度汇报（westd-10894）

### GPU 状态
| GPU | 利用率 | 显存使用 |
|-----|--------|----------|
| cuda:0 | 99% | 62.2/97.9 GB |
| cuda:1 | 41% | 62.2/97.9 GB |
| cuda:2 | 80% | 63.0/97.9 GB |
| cuda:3 | 83% | 62.2/97.9 GB |

4 GPU 全部活跃。

---

### 1. reverse_cutoff_s2_v2 (PID 170605, cuda:0)
- **当前步数**: 36248 / 50005
- **进度**: **72.5%**
- **速度**: 1.08 it/s
- **已运行**: 10h26m
- **剩余**: ~3h33m
- **预计完成**: 约 May 27 07:00 (UTC+8)
- **Checkpoints**: `20000_chkpt`, `30000_chkpt`
- **最新 loss** (step 36200): occ=0.0198, action=0.0713

**状态正常，稳定推进中。**

---

### 2. full_occ_ln_v2_s0 (PID 390852, cuda:1)
### 3. full_occ_ln_v2_s1 (PID 391060, cuda:2)
### 4. detach_ln_v2_s0 (PID 391402, cuda:3)

这 3 个实验**之前的进程崩溃了**（exitcode 2，崩溃时间 ~02:08-02:09 UTC+8），随后被重启，**从 step 0 重新训练**。

| 实验 | PID | 已运行 | 估算当前步数 | 进度 | Checkpoints |
|------|-----|--------|-------------|------|-------------|
| full_occ_ln_v2_s0 | 390852 | 1h07m | ~4300 | ~8.6% | 无 |
| full_occ_ln_v2_s1 | 391060 | 1h05m | ~4200 | ~8.4% | 无 |
| detach_ln_v2_s0 | 391402 | 1h05m | ~4200 | ~8.4% | 无 |

- **速度**: ~1.08 it/s
- **剩余**: ~11.8h
- **预计完成**: 约 May 27 15:00-16:00 (UTC+8)

注意：train.log 在 step ~275 后停止写入（输出到 tmux 终端 /dev/pts/1），步数是基于运行时间和速度估算的。

---

### DDL 风险评估
DDL: **2026-05-28 20:00 UTC+8**

- reverse_cutoff_s2_v2: 约 May 27 07:00 完成 → **无风险**
- 其余 3 个: 约 May 27 15:00-16:00 完成 → **无风险**，还有 ~28h 余量

### 需关注
3 个实验崩溃原因是 exitcode 2（可能是代码错误或参数问题），虽然重启后正在运行，但建议确认崩溃原因防止再次中断。

---
