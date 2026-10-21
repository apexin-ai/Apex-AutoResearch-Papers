# analysis check 34685 gpu0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_34685_gpu0_20260525T052551_result.json`
- **Structured JSON:** [`c4d7a5c54490f105a4b0.json`](../../sessions/c4/c4d7a5c54490f105a4b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cutoff_25k_s2_v3 正常运行。**

| 项目 | 状态 |
|------|------|
| PID | 11510 |
| GPU | cuda:0，利用率 99%，显存 62194MiB / 97887MiB |
| 进度 | step 2529 / 50005（5%），速度 ~1.10 it/s |
| 已运行 | ~42 分钟 |
| 预计剩余 | ~12 小时 |
| 最近 aux 日志 | step=2500: occ_loss=0.0247, action_loss=0.2217 |
| checkpoint 目录 | `/root/autodl-tmp/checkpoints/cutoff_25k_s2_v3/` 已创建 |

check_job_status 找不到它是因为 tmux session 名可能不匹配。进程本身在正常训练，无异常。

---
