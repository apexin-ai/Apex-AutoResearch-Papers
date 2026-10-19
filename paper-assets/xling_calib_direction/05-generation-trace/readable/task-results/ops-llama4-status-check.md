# ops llama4 status check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama4-status-check_20260521T100435_result.json`
- **Structured JSON:** [`0d1bca919c49a1cf7512.json`](../../sessions/0d/0d1bca919c49a1cf7512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 下载状态：进行中

**PID 69801 运行中**，已运行 1h47m。

### 进度明细（14 shards）

| Shard | 状态 | 进度 | ETA |
|-------|------|------|-----|
| 01 | **完成** | 100% | — |
| 02 | **完成** | 100% | — |
| 03 | **完成** | 100% | — |
| 04 | 下载中 | 97% (4.50/4.65G) | ~3 min |
| 05 | 下载中 | 72% (3.33/4.64G) | ~25 min |
| 06 | 下载中 | 73% (3.39/4.64G) | ~23 min |
| 07 | 下载中 | 64% (2.96/4.64G) | ~48 min |
| 08 | **完成** | 100% | — |
| 09 | **完成** | 100% | — |
| 10 | 下载中 | 41% (1.89/4.64G) | ~51 min |
| 11 | 下载中 | 13% (622M/4.64G) | ~111 min |
| 12 | 下载中 | 12% (569M/4.64G) | ~73 min |
| 13 | 下载中 | 2% (45M/2.81G) | ~38 min |
| 14 | 未开始/未显示 | — | — |

### 汇总

- **已完成**: 5/14 shards
- **已下载大小**: 45 GB / ~63 GB（约 71%）
- **下载速度**: 600 KB/s ~ 1.3 MB/s（ModelScope CDN）
- **瓶颈**: shard-11（13%，速度 649 KB/s）
- **预计完成时间**: 约 **1h50m 后**（~下午时间取决于当前时区）
- **模型路径**: `/root/autodl-tmp/models/Llama4-Scout-W4A16/RedHatAI/Llama-4-Scout-17B-16E-Instruct-quantized___w4a16/`
- **config.json**: 已存在

下载完成后再执行 shard 验证。

---
