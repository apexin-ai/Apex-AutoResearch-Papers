# analysis r15 taskB beam998 status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r15_taskB_beam998_status_20260521T014634_result.json`
- **Structured JSON:** [`eb47ac8af2441d31e12c.json`](../../sessions/eb/eb47ac8af2441d31e12c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 beam=4 998-doc 推理任务均在运行中：

| 实验 | 服务器 | 进度 | 已运行 | 预计剩余 | ETA (CST) |
|------|--------|------|--------|----------|-----------|
| Qwen beam4 998 | westd-21461 | 606/998 (61%) | ~5.5h | ~3.5h | ~13:20 |
| Llama beam4 998 | westd-16980 | 579/998 (58%) | ~4.0h | ~3.0h | ~12:50 |

Llama 日志中有少量 FAIL 条目（超时 ~115s），其余文档正常（10-35s/doc）。两个任务的 PID 均存活。

临时状态已保存到本地和服务器。完成后需重新检查以运行评估和 50-doc 对比。

---
