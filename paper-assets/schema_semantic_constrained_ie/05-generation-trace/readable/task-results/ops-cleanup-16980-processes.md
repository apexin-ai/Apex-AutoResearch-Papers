# ops cleanup 16980 processes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-16980-processes_20260520T082128_result.json`
- **Structured JSON:** [`b0284fb0692ba5adcea2.json`](../../sessions/b0/b0284fb0692ba5adcea2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程都是**本项目正在活跃运行的实验**，不应 kill。

| PID | 实验 | 命令 | 进度 | 状态 |
|-----|------|------|------|------|
| **728348** | d065 | `run_constrained_extraction.py` DocRED full dev, greedy, 4096 tokens | 188/~998 docs (~19%) | R (running)，输出文件仍在增长 |
| **732035** | d066 | `run_constrained_extraction.py` DocRED 200 docs, beam=2, 4096 tokens | 88/200 docs (44%) | R (running)，beam search 较慢但进程活跃 |

两个都从 `/root/schema_semantic_constrained_ie` 启动，输出写入 `/root/autodl-tmp/schema_outputs/`，d065 在两次查询间从 187→188 行确认仍在写入。**不是残留进程，保留不动。**

---
