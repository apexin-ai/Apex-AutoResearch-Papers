# urgent 5090 disk cleanup

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_5090_disk_cleanup_20260521T024751_result.json`
- **Structured JSON:** [`318a208caf332df3d0a1.json`](../../sessions/31/318a208caf332df3d0a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果**：92% → 49%，释放 108GB（21GB → 129GB 可用）。32B inference 不受影响，保护目录完整。

| 已删除 | 大小 |
|--------|------|
| HF cache Qwen2.5-32B 原始下载 | 62GB |
| HF cache Llama 模型 | 21GB |
| HF cache Qwen3-8B | 16GB |
| 32B LoRA adapter（已合并） | 9.1GB |
| HF hub cache + /tmp 临时文件 | ~4.4GB |

---
