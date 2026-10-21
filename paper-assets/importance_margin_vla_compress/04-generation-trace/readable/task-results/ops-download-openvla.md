# ops download openvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download_openvla_20260517T134148_result.json`
- **Structured JSON:** [`afe72b4b4446d18f6e43.json`](../../sessions/af/afe72b4b4446d18f6e43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘空间不足。`/root/autodl-tmp` 只剩 25GB 可用，但 4 个 OpenVLA checkpoint 总计约 60GB。

当前状态：
- 总容量: 250GB
- 已用: 226GB (91%)
- 可用: 25GB

需要约 60GB（4×~15GB），缺口约 35GB。

**选项：**
1. 只下载 base model (`openvla-7b`, ~15GB) + 代码仓库，跳过 3 个 fine-tuned checkpoints
2. 清理现有文件腾出空间
3. 换到其他有空间的服务器

需要你决定如何处理。要我先看看 `/root/autodl-tmp` 下有什么可以清理的吗？

---
