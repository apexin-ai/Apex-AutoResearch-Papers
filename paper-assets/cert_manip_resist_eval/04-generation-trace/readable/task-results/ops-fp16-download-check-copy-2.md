# ops fp16 download check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fp16-download-check_20260525T125212_result.json`
- **Structured JSON:** [`144e4df4a2a3a15d1775.json`](../../sessions/14/144e4df4a2a3a15d1775.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 模型 | PID | 进程状态 | Shards | 完整 |
|------|-----|---------|--------|------|
| Qwen2.5-14B FP16 | 75403 | DONE | **6/8** | ❌ 缺 shard 1, 2 |
| Qwen2.5-32B FP16 | 10163 | DONE | **15/17** | ❌ 缺 shard 15, 16 |
| Llama-3.1-8B AWQ | 81922 | DONE | 2/2 | ✅ |

**全部完成: NO** — 两个 FP16 模型进程已退出但 shard 不全，下载可能中途失败，需要重新触发。

**磁盘可用: 111 GB** (250G 中已用 140G, 56%)

---
