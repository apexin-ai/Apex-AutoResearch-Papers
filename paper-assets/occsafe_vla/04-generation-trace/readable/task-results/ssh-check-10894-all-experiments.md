# ssh check 10894 all experiments

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_10894_all_experiments_20260525T183632_result.json`
- **Structured JSON:** [`789dd406546896580cec.json`](../../sessions/78/789dd406546896580cec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

**关键发现：这 4 个实验不是 12 小时前提交的——日志显示它们于 2026-05-26 ~01:36 UTC 启动，运行仅约 1 小时。**

---

### cutoff_45k_s2_v2: **STILL_RUNNING**
- 进程状态：alive (PID 4212, uptime 1h00m)
- 当前 step：3715/50005 (7.4%)
- checkpoint：无（目录为空，尚未到第一个 save_freq=10000）
- 最新 loss：step=3700, occ_loss=0.0118, action_loss=0.1504
- 速度：~1.08 it/s
- 预计完成：~May 26 14:30 UTC（剩余 ~12h）

### mvp_occ_s3_v2: **STILL_RUNNING**
- 进程状态：alive (PID 11641, uptime 53m)
- 当前 step：3301/50005 (6.6%)
- checkpoint：仅有之前训练的 10000_chkpt、20000_chkpt（v2 无新 checkpoint）
- 最新 loss：step=3300, occ_loss=0.0197, action_loss=0.1226
- 速度：~1.09 it/s
- 预计完成：~May 26 14:30 UTC（剩余 ~12h）

### full_occ_ln_s3_v2: **STILL_RUNNING**
- 进程状态：alive (PID 6947, uptime 57m)
- 当前 step：3504/50005 (7.0%)
- checkpoint：仅有之前训练的 10000_chkpt、20000_chkpt（v2 无新 checkpoint）
- 最新 loss：step=3500, occ_loss=0.0098, action_loss=0.1216
- 速度：~1.08 it/s
- 预计完成：~May 26 14:30 UTC（剩余 ~12h）

### ablation_occ_detach_s3_v2: **STILL_RUNNING**
- 进程状态：alive (PID 7161, uptime 57m)
- 当前 step：3509/50005 (7.0%)
- checkpoint：仅有之前训练的 10000_chkpt、20000_chkpt（v2 无新 checkpoint）
- 最新 loss：step=3500, occ_loss=0.0174, action_loss=0.0962
- 速度：~1.08 it/s
- 预计完成：~May 26 14:30 UTC（剩余 ~12h）

---

### GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 99% | 62209/97887 MiB | 占用 (cutoff_45k_s2_v2) |
| cuda:1 | 99% | 62203/97887 MiB | 占用 (mvp_occ_s3_v2) |
| cuda:2 | 99% | 63037/97887 MiB | 占用 (full_occ_ln_s3_v2) |
| cuda:3 | 98% | 62209/97887 MiB | 占用 (ablation_occ_detach_s3_v2) |

**4 张 GPU 全部被占用，无空闲 GPU。**

---

### 需关注

1. **时间线不匹配**：你说 12 小时前提交，但实际日志起始时间是 May 26 01:36 UTC（约 1 小时前）。进度条也从 step 0 开始。这些要么是重新提交的，要么之前的 run 崩溃后被重启了。之前的退出记录中没有这 4 个实验的 exit file，说明之前没有以这些 exp_id 提交过。

2. **resume 实验的 max_steps=50005**：三个 resume 实验的进度条显示 X/50005，且 step 从 0 计数。初始 loss 很低（action_loss 0.08~0.10），确认是从 20K checkpoint resume 的。但 tqdm 显示要跑完 50005 步，意味着总步数可能是 20K + 50K = 70K 而非预期的 50K。如果实际意图是训练到 global 50K steps，可能需要确认代码逻辑。

---
