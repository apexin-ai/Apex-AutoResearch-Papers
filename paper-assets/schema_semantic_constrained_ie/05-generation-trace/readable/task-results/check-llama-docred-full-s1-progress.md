# check llama docred full s1 progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama_docred_full_s1_progress_20260514T194059_result.json`
- **Structured JSON:** [`dbc44b3ddf6c2169ec80.json`](../../sessions/db/dbc44b3ddf6c2169ec80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**`llama_docred_full_s1` 实验状态：**

| 指标 | 值 |
|------|-----|
| 进程 | **alive** (PID 194295, 已运行 4h59m52s) |
| 进度 | **882 / 998** docs (88.4%) |
| GPU 0 | RTX PRO 6000 Blackwell, 85% 利用率, 17.1 / 97.9 GB |
| GPU 1 | 空闲 |

**ETA 估算：**
- 882 docs / 300 min ≈ 2.94 docs/min
- 剩余 116 docs → **约 39 分钟**（预计 ~20:19 UTC 完成）

**注意：** 日志显示大量 "Grammar-first fallback triggered"（semantic mask 消除了所有 grammar-valid tokens，skip_count 已累计到 43）。功能上不影响推理完成，但说明 Llama 在部分文档上 semantic 约束与 grammar 约束冲突较多，值得后续分析。

---
