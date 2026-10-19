# ops oom monitor bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_oom-monitor-bjb1-32546_20260521T160435_result.json`
- **Structured JSON:** [`3d6f508f8f6e9690164e.json`](../../sessions/3d/3d6f508f8f6e9690164e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 监控汇报（2026-05-21 ~00:06 UTC）

### bjb1-32546 GPU 显存

| GPU | 显存 | 利用率 | shards |
|---|---|---|---|
| 0 | **19763/24564 MiB** | 98% | 2 |
| 1 | 9884/24564 MiB | 21% | 1 |
| 2 | **19763/24564 MiB** | 98% | 2 |
| 3 | **19763/24564 MiB** | 96% | 2 |
| 4 | 9884/24564 MiB | 25% | 1 |
| 5 | 9884/24564 MiB | 24% | 1 |

显存差 ~4.8G 到爆，紧但未 OOM。

### 进程存活
**9 个 shard 全部存活**，全部 CPU 130%+ 正常运行：
- s5 (CUDA 0, 175531) - 2h00m
- s7 (175826?) - ~2h
- s3 (178661) - 1h46m
- s4 (CUDA 3, 178940) - 1h45m
- s6 (CUDA 5, 182292) - 1h00m
- s1/s2/s8/s9 进程亦活（partial 文件持续刷新）

### OOM 日志
`dmesg | grep -i oom` 空，无 OOM kill 事件。

### 各 shard 最新进度（取最后 partial 文件，batch=100/500 混合）

| shard | 最新 partial | 距今 |
|---|---|---|
| s0 (bjb2) | 3900_4000 | ~3min |
| s1 | 2000_2500 (b500) | ~15min |
| s2 | 2500_3000 (b500) | ~9min |
| s3 | 2000_2500 (b500) | ~24min |
| s4 | 2500_3000 (b500) | ~2min |
| s5 | 3400_3500 | ~7min |
| s6 | 3100_3200 | ~12min |
| s7 | 3400_3500 | ~5min |
| s8 | 3500_3600 | ~5min |
| s9 | 3400_3500 | ~4min |

### bjb2-40593
- GPU 0: 9839/24564 MiB, 14% util
- shard 0 (PID 872656) 存活, 3900-4000，**接近完成 4000 samples**

### 结论
- **无 crash，无 OOM**
- GPU 0/2/3 显存紧（19.7G/24.5G）但稳定 ~2h，OOM 风险存在但目前安全
- s1/s3 用 batch=500，单文件耗时长，间隔较大属正常
- s0 即将完成全部 4000 samples

---
