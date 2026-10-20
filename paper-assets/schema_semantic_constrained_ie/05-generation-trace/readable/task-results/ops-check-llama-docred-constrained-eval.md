# ops check llama docred constrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_llama_docred_constrained_eval_20260516T021038_result.json`
- **Structured JSON:** [`1e9e57f47c2e4929153e.json`](../../sessions/1e/1e9e57f47c2e4929153e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇报：**

| 指标 | 状态 |
|------|------|
| 输出行数 | 410 / 998 (41%) |
| 进程 317464 | **ALIVE** |
| 进程 317469 | **ALIVE** |
| 日志 | 正常运行中（pad_token_id 设置消息） |

**决策：无需 resubmit。**

实验仍在正常运行（进程存活，日志正常输出）。EXIT_CODE=143 的告警可能是误报或来自一个旧的 wrapper 进程，实际推理进程仍在 cuda:0 上处理。当前进度 410/998，按速率预计还需数小时完成。

Registry 状态保持 RUNNING 不变，无需操作。

---
