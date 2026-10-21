# ops accelerate openvla checkpoint download

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_accelerate-openvla-checkpoint-download_20260520T235105_result.json`
- **Structured JSON:** [`bd5abab022e18a93f5dd.json`](../../sessions/bd/bd5abab022e18a93f5dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载脚本 (PID 686161) 持续稳定运行中。

**当前状态总结：**

| Checkpoint | 进度 |
|------------|------|
| `libero-spatial` | shard 2 ✓ shard 3 ✓ shard 4 ✓ 小文件 ✓ / **shard 1 需修复** |
| `libero-goal` | shard 1 ✓ (16MiB/s) / **shard 2 下载中** / shard 3-4 待下载 |
| `libero-10` | 待开始 |

**方案：** `aria2c -x16 + hf-mirror.com`（无代理），16 MiB/s
**加速效果：** 原 60+ 小时 → 现约 40 分钟（64x 加速）
**PID:** 686161
**预计完成：** ~08:40（UTC+8 约 08:40）

**脚本完成后待做：**
1. 删除 spatial shard 1 的损坏文件，重新下载
2. 验证全部 3 个 checkpoint 的 safetensors 完整性
3. 清理 .aria2 和 .cache 文件

下载进程后台运行，不会因 SSH 断开而中断。你可以等它完成后让我做最终验证，或我继续轮询。

---
