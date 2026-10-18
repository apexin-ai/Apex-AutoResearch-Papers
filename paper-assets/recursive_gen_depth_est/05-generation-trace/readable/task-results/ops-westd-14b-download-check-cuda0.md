# ops westd 14b download check cuda0

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_14b_download_check_cuda0_20260517T182519_result.json`
- **Structured JSON:** [`90e2740f3be51e69a9cf.json`](../../sessions/90/90e2740f3be51e69a9cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**14B 下载状态：完成 ✓**
- 模型路径：`/root/autodl-tmp/models/Qwen2.5-14B`
- 8/8 shards 全部下载，总计 ~28GB，文件完整
- 下载时间：约 01:27 - 01:55 (May 18)

**westd-48862 GPU 状态：**
- `cuda:0`: 0 MiB / 97887 MiB — 完全空闲 ✓
- `cuda:1`: 0 MiB / 97887 MiB — 完全空闲 ✓

**启动 14B scale validation 的问题：**
- westd-48862 上没有 `qwen25_14b_scale_validation.py` 和 `run_qwen25_14b_scale_validation.sh`
- gpu-6000pro-2 上的脚本硬编码模型路径为 `/root/autodl-tmp/models/qwen25_14b`（小写），而 westd-48862 下载的目录名是 `Qwen2.5-14B`（原始名）
- 需要：
  1. 将脚本从 gpu-6000pro-2 复制到 westd-48862（或直接在 westd-48862 创建）
  2. 修改 `MODEL_PATH` 为 `/root/autodl-tmp/models/Qwen2.5-14B`

要我把脚本同步过去并调整路径后启动？

---
