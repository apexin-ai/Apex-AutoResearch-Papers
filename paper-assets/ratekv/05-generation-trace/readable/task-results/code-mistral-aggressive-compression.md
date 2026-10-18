# code mistral aggressive compression

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_aggressive_compression_20260514T055948_result.json`
- **Structured JSON:** [`caf9cd34ef4c950eeff2.json`](../../sessions/ca/caf9cd34ef4c950eeff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并在运行中：

- **tmux session**: `mistral_aggressive` on westd-37397 cuda:0
- **脚本**: `/root/ratekv/run_mistral_aggressive.py`
- **日志**: `mistral_aggressive.log` / `mistral_aggressive_tmux.log`
- **输出**: `mistral_aggressive_results.json`
- **Registry**: `mistral_aggressive_compression` → RUNNING
- **监控**: 每 5 分钟自动检查进度

模型已加载完成 (3/3 shards)，正在跑 baseline eval。预计整体运行 15-30 分钟（baseline + uniform 4-bit + 2 个 budget 各需 solver + eval）。

---
