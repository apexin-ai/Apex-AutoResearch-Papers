# ops restart pi05 download

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart_pi05_download_20260522T171532_result.json`
- **Structured JSON:** [`caef44d6ee6e70c99649.json`](../../sessions/ca/caef44d6ee6e70c99649.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载正在进行中。gsutil 正在以 ~16 MiB/s 从 GCS 下载 11.6 GiB 的 pi05_base，预估 ~12 分钟完成。

结果汇总：

1. **模型 repo**: `gs://openpi-assets/checkpoints/pi05_base/params`（GCS，非 HuggingFace）+ `gs://openpi-assets/checkpoints/pi05_base/assets`
2. **下载 PID**: `417255`，日志路径 `/root/autodl-tmp/pi05_download.log`
3. **初始状态**: gsutil 正在下载，已完成 ~500MB / 11.6GB（~4%），速度 ~16 MiB/s，ETA ~12 分钟
4. **磁盘空间**: 数据盘 159G 可用（250G 总，92G 已用），充足。缓存目标 `/root/autodl-tmp/.cache/openpi/openpi-assets/checkpoints/pi05_base/`
5. **缓存位置**: 设置了 `OPENPI_DATA_HOME=/root/autodl-tmp/.cache/openpi` 避免写根分区（仅 14G 可用）

下载完成后 openpi 训练时会自动找到缓存的权重。params 下载完会继续下载 assets（norm_stats 等）。

---
