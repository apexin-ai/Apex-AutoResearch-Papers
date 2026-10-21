# check s3 training health

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_s3_training_health_20260525T142435_result.json`
- **Structured JSON:** [`2d493232bd16896a2e16.json`](../../sessions/2d/2d493232bd16896a2e16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 健康状态汇总

### 进程存活
全部存活，运行时长 ~3h08m：
| PID | 实验 | etime | RSS |
|-----|------|-------|-----|
| 256611 | mvp_occ_s3 | 3:07:56 | 3.5GB |
| 256695 | full_occ_ln_s3 | 3:07:51 | 3.5GB |
| 257041 | ablation_occ_detach_s3 | 3:07:46 | 3.5GB |

### 训练进度

| 实验 | 当前 step | 进度 | 速度 | tqdm 剩余 | 预计 ETA |
|------|-----------|------|------|-----------|----------|
| ablation_occ_detach_s3 | 10718/50005 | 21.4% | 1.07-1.08 it/s | ~10h09m | ~May 25 16:20 UTC |
| mvp_occ_s3 | 10761/50005 | 21.5% | 1.07-1.08 it/s | ~10h09m | ~May 25 16:20 UTC |
| full_occ_ln_s3 | 10728/50005 | 21.5% | 1.07-1.08 it/s | ~10h08m | ~May 25 16:20 UTC |

注：tqdm 估计基于瞬时速度。考虑 checkpoint 暂停（每次 ~5min），实际 ETA 可能再晚 30-40min，约 **May 25 17:00 UTC**。比原先预估的 May 26 08:15 提前约 15 小时。

### v2 代码确认

| 实验 | [AUX] count | [OCC] count | 状态 |
|------|-------------|-------------|------|
| ablation_occ_detach_s3 | 108 | 0 | v2 ✅ |
| mvp_occ_s3 | 108 | 0 | v2 ✅ |
| full_occ_ln_s3 | 108 | 0 | v2 ✅ |

### 最新 [AUX] 日志（step 10700）
- **ablation_occ_detach_s3**: occ_loss=0.0127, action_loss=0.1216
- **mvp_occ_s3**: occ_loss=0.0115, action_loss=0.1416
- **full_occ_ln_s3**: occ_loss=0.0084, action_loss=0.1562

三个实验全部健康运行，v2 代码确认无误。

---
