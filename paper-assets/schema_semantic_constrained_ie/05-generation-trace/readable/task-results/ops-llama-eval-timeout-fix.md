# ops llama eval timeout fix

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_eval_timeout_fix_20260515T231151_result.json`
- **Structured JSON:** [`2d92675215010cfb2b95.json`](../../sessions/2d/2d92675215010cfb2b95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 项目 | 状态 |
|------|------|
| **原进程** | 已死亡 — kill timeout PID 303529 时信号传播杀掉了 python 子进程 303530 |
| **JSONL 进度** | 被 kill 时 775/998，当前 783/998（resume 已续跑 8 个新样本） |
| **Resume 验证** | 无重复（grep 确认），文件以 append 模式追加 |
| **timeout 状态** | 已解除 — 新进程用 nohup 启动，无 timeout wrapper |
| **新进程** | PID 312925，GPU 0 (16364 MiB)，运行正常 |
| **预计完成** | 剩余 ~215 样本 × ~15s ≈ 54min，无超时风险 |
| **GPU 1** | Qwen eval (PID 304011) 仍在正常运行，17418 MiB |

**注意**：`timeout` 收到 SIGTERM 时会把信号转发给整个子进程组，`kill &lt;timeout_pid>` 无法单独杀 timeout 而保留子进程。今后如需解除 timeout，应先将子进程 `disown` 或用 `kill -STOP` + `setsid` 隔离进程组后再杀 timeout。

---
