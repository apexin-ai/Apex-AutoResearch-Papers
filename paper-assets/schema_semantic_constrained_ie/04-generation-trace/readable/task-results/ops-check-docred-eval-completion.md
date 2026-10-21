# ops check docred eval completion

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_docred_eval_completion_20260515T232506_result.json`
- **Structured JSON:** [`c27806806acdf7835e75.json`](../../sessions/c2/c27806806acdf7835e75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Llama DocRED Unconstrained Eval
- **进程状态**: running (PID 312925, elapsed 10:25)
- **输出行数**: 819/998 (从 775 resume，+44 samples in ~10min)
- **速率**: ~4.2 samples/min → 剩余 179 samples → **预计 ~43 min 后完成**
- **日志**: resume 日志仅有 pad_token 警告，无进度行（进度输出可能被 buffer）

## Qwen DocRED Unconstrained Eval
- **进程状态**: running (PID 304006/304011, elapsed 3:21:40)
- **输出行数**: 582/998
- **日志进度**: [487/998]（log 有 450 条 "OK E="，与输出文件差异可能因 buffer）
- **速率**: ~2.9 samples/min → 剩余 ~416 samples → **预计 ~2.4h 后完成**

## GPU 状态
- cuda:0: 16413 MiB used, 89% util (Llama)
- cuda:1: 17427 MiB used, 87% util (Qwen)

两个 eval 都还在跑，都没完成。Llama 预计 ~43 分钟内结束，Qwen 预计 ~2.5 小时。

---
