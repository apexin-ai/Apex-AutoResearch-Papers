# diagnose qwen25 14b scale 002

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen25_14b_scale_002_20260517T143600_result.json`
- **Structured JSON:** [`16514b98a9d59dcae9a6.json`](../../sessions/16/16514b98a9d59dcae9a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：**

**失败原因**：模型下载阶段网络故障。aria2 下载 `model-00005-of-00008.safetensors` 时与 `cas-bridge.xethub.hf.co` 的 TLS 连接被异常终止（`SSL/TLS handshake failure: The TLS connection was non-properly terminated`），导致 EXIT_CODE=1。实验从未进入 Python 训练阶段。

**当前模型状态**：8 个 shards 中仅 1-3 完整（各 ~3.8GB），shard 4 部分下载（有 .aria2 控制文件），5-8 缺失。磁盘空间充足（103GB 可用）。

**修复方案**：
1. 直接重新提交实验 — 脚本有 skip-existing 逻辑，会从 shard 4 断点续传
2. 建议在下载脚本中为 aria2 添加 `--max-tries=5 --retry-wait=10` 避免瞬态 TLS 故障再次导致整个实验失败

---
