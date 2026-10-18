# ops stop oft download cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_stop-oft-download-cqa1_20260520T085735_result.json`
- **Structured JSON:** [`1df653758d961e4a9490.json`](../../sessions/1d/1df653758d961e4a9490.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果**：

- **OFT 下载进程**：无活跃下载进程，无需 kill
- **OFT 模型文件**：HF cache 中无 OFT 相关模型目录，无需清理大文件
- **已清理**：`/tmp/openvla_oft_analysis.log`（日志文件，体积可忽略）
- **当前磁盘**：
  - 根分区：14G/30G（45%）
  - 数据盘：154G/250G（62%）

磁盘并非 94%，OFT 下载可能之前已被停止或从未在此服务器启动。无需进一步操作。

---
