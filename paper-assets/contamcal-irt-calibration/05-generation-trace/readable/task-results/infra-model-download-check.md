# infra model download check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model-download-check_20260518T200636_result.json`
- **Structured JSON:** [`c1d3a322c22372ff4b78.json`](../../sessions/c1/c1d3a322c22372ff4b78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

| 模型 | 状态 | 说明 |
|---|---|---|
| **Phi-4** | 不完整 → 补下载中 | 缺 shard 5/6，PID 58480 后台下载 |
| **OLMo-2-1124-7B** | 不完整 → 补下载中 | 缺 shard 3/6，PID 58553 后台下载 |
| **Gemma-2-9B** | 完整 | 8/8 shards, ~35GB |
| **Qwen2.5-14B** | 完整 | 8/8 shards, ~28GB |

注意：服务器上的 OLMo 是 `allenai/OLMo-2-1124-7B`，不是任务中提到的 `OLMo-2-7B-0325`。两个缺失 shard 的下载已后台启动，每个约 4.6GB，预计几分钟到十几分钟完成。

---
