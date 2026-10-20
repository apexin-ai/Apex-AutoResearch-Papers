# ops gpu rescue 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-rescue-34685_20260526T104241_result.json`
- **Structured JSON:** [`dea6cc61f505848bbfe6.json`](../../sessions/de/dea6cc61f505848bbfe6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**所有 4 个训练进程都在运行，未死。** nvidia-smi 的 0% 利用率只是快照瞬时值。

| GPU | 实验 | PID | 当前步数 | 进度 | 正常速度 |
|-----|------|-----|----------|------|---------|
| 0 | vanilla_v2_s1 | 419275 | ~6930/50005 | 14% | ~1.09 it/s |
| 1 | vanilla_v2_s2 | 419510 | ~6955/50005 | 14% | ~1.09 it/s |
| 2 | detach_ln_s3 | 419786 | ~6913/50005 | 14% | ~1.09 it/s |
| 3 | cutoff_25k_s1_v2 | 453661 | ~5519/50005 | 11% | ~1.09 it/s |

### 关键问题：CKA 分析进程导致严重降速

PID 460707 (`v2_cka_analysis.py`) 在 18:38 启动，占用 **1863% CPU**（18+ 核心），虽然设了 `CUDA_VISIBLE_DEVICES=""`不用 GPU，但正在严重抢占 CPU 资源。

从日志可以看到，最近训练速度从 **1.09 it/s 骤降到 10-15s/it**（降速 10-15 倍）。四个训练进程都受影响。

### ETA 估算

| 场景 | 最慢实验（cutoff_25k_s1_v2, 剩余 44486 步） | 预计完成时间 |
|------|---------------------------------------------|------------|
| 正常速度 1.09 it/s | ~11.3h | **5/27 06:00** |
| 当前降速 ~10s/it | ~124h (5天+) | **远超 DDL** |

**CKA 分析是关键阻塞**。如果不停掉或限制它，4 个训练都会严重延迟。

需要 kill CKA 分析进程 (PID 460707) 吗？

---
