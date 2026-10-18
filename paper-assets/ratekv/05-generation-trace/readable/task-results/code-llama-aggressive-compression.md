# code llama aggressive compression

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_aggressive_compression_20260514T052333_result.json`
- **Structured JSON:** [`0bb4485257faaa03dcaa.json`](../../sessions/0b/0bb4485257faaa03dcaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，registry 已更新为 RUNNING。

实验状态：
- **tmux session**: `llama_aggressive` on cuda:0
- **脚本**: `run_llama_aggressive.py` — 2 个 budget 点 (0.1875 / 0.125) × MCKP + uniform 2-bit eval
- **修正**: 任务指定的 max_2bit=36/27 太小无法达到目标 budget，已调整为 144/248
- **预计**: ~15-18min（baseline + uniform 4-bit ref + 2×(uniform 2-bit + MCKP) eval）

模型正在加载中，稍后可以用 `tail /root/ratekv/llama_aggressive.log` 查看进度。

---
