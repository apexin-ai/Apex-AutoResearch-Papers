# monitor training progress 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-34685_20260527T024936_result.json`
- **Structured JSON:** [`f1ebc065d3d69bbc7c26.json`](../../sessions/f1/f1ebc065d3d69bbc7c26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前服务器时间: 2026-05-27 10:51 +0800 (02:51 UTC)

| exp_id | PID | 存活 | 当前 step | max_steps | 进度% | 剩余时间 | ETA (UTC) |
|--------|-----|------|-----------|-----------|-------|----------|-----------|
| detach_ln_v2_s1_35 | 681124 | ✓ | 12274 | 50005 | 24.5% | ~9h42m | May 27 ~12:33 |
| detach_ln_s4 | 677568 | ✓ | 12333 | 50005 | 24.7% | ~9h40m | May 27 ~12:31 |
| ablation_occ_detach_s4 | 735898 | ✓ | 9522 | 50005 | 19.0% | ~10h19m | May 27 ~13:10 |
| mvp_occ_s4 | 736253 | ✓ | 9502 | 50005 | 19.0% | ~10h22m | May 27 ~13:13 |

**GPU 状态 (westd-34685):**

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 99% | 62203/97887 MiB (64%) |
| 1 | 73% | 62203/97887 MiB (64%) |
| 2 | 99% | 62203/97887 MiB (64%) |
| 3 | 97% | 63037/97887 MiB (64%) |

**最新 loss (AUX log):**
- detach_ln_s4 @12300: occ=0.0095, action=0.1504
- ablation_occ_detach_s4 @9500: occ=0.0217, action=0.1226
- mvp_occ_s4 @9500: occ=0.0088, action=0.1377

**结论:** 4 个实验全部正常运行，速度 ~1.08 it/s。预计全部在 May 27 ~13:13 UTC 前完成，远早于 DDL (May 28 12:00 UTC)，有 ~23h 余量。GPU 1 利用率略低 (73%)，但无异常。

---
