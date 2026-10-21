# diagnose westd 34685 gpu zero

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-34685-gpu-zero_20260522T174147_result.json`
- **Structured JSON:** [`49af2348822d5ff43511.json`](../../sessions/49/49af2348822d5ff43511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**误报，4 个实验全部健康运行。**

## 诊断结果

| 实验 | GPU | 利用率 | 显存 | 当前 step | 进度 | 速度 | 最新 checkpoint | 最新 loss |
|------|-----|--------|------|-----------|------|------|----------------|-----------|
| cutoff_s0 | cuda:0 | 98% | 62203/97887 MiB | ~28546 | 57% | ~1.07 it/s | 20000 | occ=0.0093, action=0.1016 |
| depth_s0 | cuda:1 | 25% | 62203/97887 MiB | ~30530 | 61% | ~1.05 it/s | 30000 | depth=0.0298, action=0.0728 |
| depth_s1 | cuda:2 | 99% | 62203/97887 MiB | ~30457 | 61% | ~1.03 it/s | 30000 | depth=0.0223, action=0.0864 |
| cutoff_s1 | cuda:3 | 99% | 62209/97887 MiB | ~30552 | 61% | ~1.06 it/s | 30000 | occ=0.0109, action=0.0869 |

**结论：**
- 4 个进程全部存活，GPU 利用率正常（GPU 1 的 25% 是 checkpoint 保存期间的瞬时读数，日志显示 depth_s0 在 step ~30486 附近有 ~10s 的保存延迟，与读数一致）
- cutoff_s0 进度稍落后（28.5k vs 30.5k），因为它是最后启动的（PID 最大），正常追赶中
- Loss 值合理，训练正常推进
- 预计剩余时间：cutoff_s0 ~5.5h，其余 3 个 ~5h

---
