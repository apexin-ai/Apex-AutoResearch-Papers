# check server status 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-status-10894_20260527T033803_result.json`
- **Structured JSON:** [`8e4d3f4430b6211320f3.json`](../../sessions/8e/8e4d3f4430b6211320f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894 训练状态报告

### GPU 状态
| GPU | 利用率 | 显存使用 |
|-----|--------|----------|
| 0 | 99% | 62.2 / 97.9 GB |
| 1 | 92% | 62.2 / 97.9 GB |
| 2 | 99% | 62.2 / 97.9 GB |
| 3 | 99% | 62.2 / 97.9 GB |

### 训练进度（4/4 运行中）
| 实验 | GPU | PID | Step | 进度 | 速度 | 预计剩余 |
|------|-----|-----|------|------|------|----------|
| full_occ_ln_v2_s1c | 0 | 481426 | ~10964/50005 | 22% | ~1.08 it/s | ~10h |
| full_occ_ln_v2_s2 | 1 | 481643 | ~10947/50005 | 22% | ~1.07 it/s | ~10h |
| detach_ln_v2_s0c | 2 | 481988 | ~10934/50005 | 22% | ~1.08 it/s | ~10h |
| full_occ_ln_v2_s0d | 3 | 490883 | ~8437/50005 | 17% | ~1.06 it/s | ~11h |

前3个已跑~3h，s0d 晚启动约40min（已跑~2h20m）。按当前速度，预计完成时间：
- s1c/s2/s0c: ~May 28 00:00-01:00 UTC
- s0d: ~May 28 01:30-02:00 UTC

全部在 DDL (May 28 12:00 UTC) 前完成，余量充足。

### 已完成实验 50K checkpoint
- **full_occ_ln_s3_v2**: 存在
- **ablation_occ_detach_s3_v2**: 存在

---
