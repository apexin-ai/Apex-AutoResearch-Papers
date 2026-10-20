# ssh 10894 progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_10894_progress_check_20260526T054914_result.json`
- **Structured JSON:** [`a993fe36b33c92021b94.json`](../../sessions/a9/a993fe36b33c92021b94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894 训练进度 (2026-05-26)

| exp_id | GPU | step/50K | 进度% | occ_loss | action_loss | 速度 | ETA |
|--------|-----|----------|-------|----------|-------------|------|-----|
| cutoff_45k_s2_v2 | cuda:0 | 42934/50005 | **85.9%** | 0.0131 | 0.0569 | 1.07 it/s | ~1h50m |
| mvp_occ_s3_v2 | cuda:1 | 31800/50005 | **63.6%** | 0.0104 | 0.0688 | 1.07 it/s | ~4h44m |
| full_occ_ln_s3_v2 | cuda:2 | 31700/50005 | **63.4%** | 0.0092 | 0.0559 | 1.07 it/s | ~4h45m |
| ablation_occ_detach_s3_v2 | cuda:3 | 31600/50005 | **63.2%** | 0.0125 | 0.0669 | 1.06 it/s | ~4h49m |

**进程状态**: 4 个全部存活。PID 4212 (cutoff) 已运行 12h13m，其余 3 个 ~9h07m。

**GPU 利用率**: 全部 99%，显存 62.2/95.6 GB (~65%)

**磁盘**: `/root/autodl-tmp` 156G/250G (63%)，剩余 95G，充足

**备注**: cutoff_45k_s2_v2 预计最先完成（~1h50m 后）；其余 3 个实验进度接近，预计 ~4h45m 后完成。full_occ_ln_s3_v2 的 occ_loss 最低 (0.0092)，ablation_occ_detach 最高 (0.0125)。

---
