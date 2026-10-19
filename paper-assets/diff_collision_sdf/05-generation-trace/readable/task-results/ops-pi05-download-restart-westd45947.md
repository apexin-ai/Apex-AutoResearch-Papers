# ops pi05 download restart westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pi05_download_restart_westd45947_20260522T183902_result.json`
- **Structured JSON:** [`eaede420dac4cd110649.json`](../../sessions/ea/eaede420dac4cd110649.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**pi0.5 base 权重已经存在，不需要重新下载。**

下载日志 `/root/autodl-tmp/pi05_download.log` 显示之前通过 gsutil 从 GCS 下载已完成（`DOWNLOAD_COMPLETE`）。

当前状态汇总：

| 权重 | 路径 | 大小 | 状态 |
|------|------|------|------|
| pi0 base | `/root/autodl-tmp/openpi_weights/pi0_base/` | ~13GB (safetensors) | 完整 |
| pi0.5 base | `/root/autodl-tmp/.cache/openpi/openpi-assets/checkpoints/pi05_base/` | 12GB (orbax/ocdbt) | 完整 |
| pi0.5 libero | `/root/autodl-tmp/openpi_weights/pi05_libero/` | 12GB | 完整 |

磁盘空间：`/root/autodl-tmp/` 250GB 总容量，已用 105GB，剩余 146GB（42%），充裕。

pi0.5 base 的 checkpoint 是 openpi 原生的 orbax 格式（params 目录含 ocdbt shards），不是 HuggingFace safetensors 格式。这是 openpi 框架的标准格式，可以直接用于 eval。

---
