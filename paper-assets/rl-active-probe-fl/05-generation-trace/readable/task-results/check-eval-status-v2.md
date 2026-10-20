# check eval status v2

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-status-v2_20260514T082542_result.json`
- **Structured JSON:** [`eb2427c79e6923086b19.json`](../../sessions/eb/eb2427c79e6923086b19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### eval-sft-v1 (PID 18477, GPU 0)
- **状态**: 运行中，**24/202** samples 完成
- **GPU**: cuda:0, 17174 MiB 占用, 60% 利用率
- **速率**: ~10s/sample（16:22:11 → 16:26:06 完成 24 个）
- **预计剩余**: 178 × 10s ≈ **30 分钟**，ETA ~16:56

### eval-base-v2 (PID 18618, GPU 1)
- **状态**: 运行中，**23/202** samples 完成
- **GPU**: cuda:1, 16622 MiB 占用, 63% 利用率
- **速率**: ~10.1s/sample（16:22:12 → 16:26:05 完成 23 个）
- **预计剩余**: 179 × 10.1s ≈ **30 分钟**，ETA ~16:56

### Qwen3-30B-A3B 下载 (PID 12991)
- **已下载**: 15GB
- **活跃下载分片**:
  - `model-00012-of-00016.safetensors`: 17% (665M/3.71G) @ 338 kB/s
  - `model-00006-of-00016.safetensors`: 60% (2.24G/3.73G) @ 379 kB/s
  - `model-00005-of-00016.safetensors`: 58% (2.17G/3.73G) @ 356 kB/s
  - `model-00008-of-00016.safetensors`: 已完成 (4.23GB)
- **总速度**: ~1.4 MB/s（4 并行流）
- **模型总大小**: ~33GB（16 分片），还需下载 ~18GB
- **预计剩余**: ~3.5 小时

两个 eval 都正常推进，约 30 分钟后完成。Qwen3-30B-A3B 下载较慢（ModelScope CDN 速度一般），预计还需 3-4 小时。

---
