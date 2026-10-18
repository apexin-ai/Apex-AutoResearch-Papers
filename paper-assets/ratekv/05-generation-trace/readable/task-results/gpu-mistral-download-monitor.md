# gpu mistral download monitor

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_mistral_download_monitor_20260514T212840_result.json`
- **Structured JSON:** [`3c2d4ff0e12dd4090eae.json`](../../sessions/3c/3c2d4ff0e12dd4090eae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**报告：**

| 项目 | 状态 |
|------|------|
| 下载进程 | PID 262493 运行中，3 shard 各 ~50%（2.4-2.6G / ~4.9G） |
| 监控脚本 | PID 263305，后台轮询等待下载结束后自动执行 4 项验证 |
| 验证结果 | 完成后写入 `/tmp/mistral_verify_result.txt` |
| 清理 | 已删除 `mistral-7b-v0.3/`（12G 不完整）和 `AI-ModelScope/`（空壳），释放 ~12GB |
| 预计完成 | 下载约 5-10 分钟，验证约 1-2 分钟 |

查看结果：`cat /tmp/mistral_verify_result.txt`

---
