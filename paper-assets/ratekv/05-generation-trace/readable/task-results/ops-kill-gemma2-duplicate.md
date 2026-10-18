# ops kill gemma2 duplicate

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_gemma2_duplicate_20260514T221120_result.json`
- **Structured JSON:** [`3d6faf7e23f753b5473c.json`](../../sessions/3d/3d6faf7e23f753b5473c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 项目 | 状态 |
|------|------|
| **PID 269018** (重复 Gemma-2) | 已 kill (SIGTERM，未需 force kill) |
| **PID 268242** (Gemma-2 hires) | 运行中，**21/336** heads，已 8min，ETA ~121min，cuda:0 |
| **PID 264489** (Mistral v4) | 运行中，**159/256** heads，已 35min，ETA ~21min，cuda:1 |

**GPU 使用：**

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU 0 | 20.2 GB / 97.9 GB | 100% |
| GPU 1 | 17.9 GB / 97.9 GB | 100% |

Mistral v4 约 21 分钟后完成。Gemma-2 刚开始，预计还需约 2 小时。

---
