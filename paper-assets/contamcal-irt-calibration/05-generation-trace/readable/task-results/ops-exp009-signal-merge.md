# ops exp009 signal merge

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp009_signal_merge_20260517T105255_result.json`
- **Structured JSON:** [`5267833698f3cfb1acb5.json`](../../sessions/52/5267833698f3cfb1acb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。6 个 merged 文件已生成：

| 模型 | benchmark | items |
|---|---|---|
| Qwen2.5-0.5B-Instruct | arc_challenge | 1,172 |
| Qwen2.5-0.5B-Instruct | gsm8k | 1,319 |
| Qwen2.5-0.5B-Instruct | mmlu | 14,042 |
| Qwen2.5-1.5B-Instruct | arc_challenge | 1,172 |
| Qwen2.5-1.5B-Instruct | gsm8k | 1,319 |
| Qwen2.5-1.5B-Instruct | mmlu | 14,042 |

每个文件包含 `index`, `benchmark`, `s1_embedding`, `s2_minkpp`, `s3_constat`(null), `s4_selfcritique`，格式与 3B-Instruct 的 merged 文件一致。

---
