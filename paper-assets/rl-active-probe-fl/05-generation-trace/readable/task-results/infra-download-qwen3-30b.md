# infra download qwen3 30b

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download-qwen3-30b_20260514T070406_result.json`
- **Structured JSON:** [`5c6034c89f8e36ddaa10.json`](../../sessions/5c/5c6034c89f8e36ddaa10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载已在后台运行，汇报如下：

- **PID**: 12985
- **状态**: 正在并行下载 16 个 safetensors 分片（每片 ~3.7GB）
- **当前速度**: 0.4-1.2 MB/s（多线程并行）
- **预估模型总大小**: ~60GB（16 × 3.7GB）
- **磁盘可用**: 215GB，充裕
- **不影响 GPU**: 纯 CPU + 网络 IO，GPU 0 的 GRPO 训练和 GPU 1 的 eval-base 不受影响

后续查进度：`tail -5 /tmp/download_qwen3_30b.log`

---
