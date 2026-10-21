# ops cleanup qwen and start rasp eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_qwen_and_start_rasp_eval_20260518T165953_result.json`
- **Structured JSON:** [`fdbff29597e7006bc17b.json`](../../sessions/fd/fdbff29597e7006bc17b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**删除完成**: Qwen2.5-Math-7B 15GB 已释放，数据盘 85% (38G 可用)。

**当前 eval 进度**:

| Eval | GPU | 进度 | Acc | 预估剩余时间 |
|------|------|------|-----|-------------|
| Standard (PID 823050) | cuda:0 | 155/1319 (12%) | 25.3% | ~2.5h |
| CKA-only (PID 822503) | cuda:1 | 241/1319 (18%) | 40.5% | ~1.7h |

`eval_unstructured_20` 已完成（5/17），但其 tmux session 仍占着 cuda:1 的位置，CKA-only 正在使用 cuda:1。

两张卡都在跑，无空闲 GPU。CKA-only 预计先完成（约 1.7h 后，~02:40 UTC）。RASP eval 需等其中一个结束后启动。

---
