# ops check constrained eval status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_constrained_eval_status_20260516T021024_result.json`
- **Structured JSON:** [`96a133aa92570c2a186a.json`](../../sessions/96/96a133aa92570c2a186a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在运行中，汇总：

| 实验 | PID | 状态 | 运行时间 | 进度 | 速度 | 预估剩余 |
|------|-----|------|----------|------|------|----------|
| **Llama constrained eval** | 317469 (Rl) | Running | 1h44m | 409/998 (41%) | ~15s/sample | ~2.5h |
| **Qwen constrained eval** | 321568 (Rl) | Running | 16m | 48/998 (4.8%) | ~20s/sample | ~5.3h |

- 两个进程状态都是 `Rl`（运行中），正常产出 jsonl 结果
- Llama 推理速度更快（~15s/sample vs Qwen ~20s/sample），预计约 2.5 小时后完成
- Qwen 启动较晚，预计约 5 小时后完成

---
