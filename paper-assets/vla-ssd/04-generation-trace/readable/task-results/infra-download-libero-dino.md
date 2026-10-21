# infra download libero dino

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download-libero-dino_20260515T052657_result.json`
- **Structured JSON:** [`86cb441cc1f82d158e78.json`](../../sessions/86/86cb441cc1f82d158e78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出报告

### 1. LIBERO 下载状态
- **数据源**: `yifengzhu-hf/LIBERO-datasets` (HuggingFace)
- **完成**: 3/10 HDF5 文件（~2.1GB）
- **下载中**: 7 个文件正在后台下载（PID 6224 存活）
- **总大小**: 当前 7.8GB（含 libero_90 的 7 个文件和缓存）
- **预计**: 剩余 7 个文件按当前速度约 10-15 分钟完成
- **路径**: `/root/autodl-tmp/vla-ssd/data/libero/libero_10/`

### 2. DINO-V2 下载状态
- **验证通过**: 304.4M 参数，1.2GB
- **路径**: `/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/`

### 3. 符号链接状态
- `data` → `/root/autodl-tmp/vla-ssd/data` ✓
- `checkpoints` → `/root/autodl-tmp/vla-ssd/checkpoints` ✓
- `features` → `/root/autodl-tmp/vla-ssd/features` ✓

### 4. 磁盘空间
- 数据盘 250GB，已用 12GB，剩余 239GB（充足）

> LIBERO 下载仍在后台进行（PID 6224），可稍后用 `tail -5 /tmp/download_libero3.log` 和 `find /root/autodl-tmp/vla-ssd/data/libero/libero_10/ -name "*.hdf5" | wc -l` 检查是否完成。

---
