# ops check docred progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_docred_progress_20260514T042951_result.json`
- **Structured JSON:** [`f0f3639250bafb91e68e.json`](../../sessions/f0/f0f3639250bafb91e68e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均在运行，GPU 利用率正常 (83-84%)。

| 实验 | 进度 | 速度 | 预估完成 (UTC) |
|------|------|------|----------------|
| grammar_only | 454/998 (45.5%) | 174.9 docs/hr | ~07:38 |
| full_s1 | 315/998 (31.6%) | 185.1 docs/hr | ~08:12 |

注意：PID 157042 的 CPU/MEM 显示 0.0%，可能是 shell wrapper，但 GPU 1 活跃确认实验在跑。报告已写入 `artifacts/docred_progress_check.md`。

---
