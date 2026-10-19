# ops pi05 download urgent

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pi05_download_urgent_20260522T144046_result.json`
- **Structured JSON:** [`8e761b661d1c970142bc.json`](../../sessions/8e/8e761b661d1c970142bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## pi0.5 下载状态

**状态：Running** — gsutil 进程活跃（多个 `-m cp` worker，PID 399232+，19:48 启动）

**进度：7.0 / 11.6 GiB（~60%）**

| 指标 | 值 |
|------|-----|
| 磁盘实际写入 | 7.0 GiB |
| 文件表观大小 | 11.6 GiB（6 个 .gstmp 稀疏文件） |
| 30min 增量 | 5.9→7.0 GiB（+1.1 GiB） |
| 当前速度 | ~625 KiB/s |
| 剩余 | ~4.6 GiB |
| **预估 ETA** | **~2h（约 00:45）** |

6 个大权重分片（ocdbt.process_0/d/）都还在下载中（.gstmp 后缀），小文件（norm_stats.json、_METADATA、_sharding 等）已完成。

---
