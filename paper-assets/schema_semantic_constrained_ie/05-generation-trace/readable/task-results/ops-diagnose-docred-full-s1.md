# ops diagnose docred full s1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_docred_full_s1_20260514T023934_result.json`
- **Structured JSON:** [`893283a6219625d8bc35.json`](../../sessions/89/893283a6219625d8bc35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：实验失败**

| 项目 | 状态 |
|------|------|
| 进程 PID 152032 | 已退出 |
| 完成度 | 87/998 行 (8.7%) |
| 崩溃原因 | 不明（无 OOM、无日志，静默退出） |
| 文件最后写入 | 10:35 |
| GPU 现状 | cuda:0 被 grammar_only (PID 150766, 134/998) 占用，cuda:1 空闲 |

已完成：
- registry 更新了 notes（需要重跑）
- cron 已清除

**重跑建议**：等 grammar_only 完成后在 cuda:0 重跑，或立即用 cuda:1 启动。建议加 `nohup ... > /tmp/docred_full_s1.log 2>&1 &` 以便捕获崩溃日志。

---
