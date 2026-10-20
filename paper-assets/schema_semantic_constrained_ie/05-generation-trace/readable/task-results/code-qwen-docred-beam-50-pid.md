# code qwen docred beam 50 pid

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_docred_beam_50_pid_20260517T035200_result.json`
- **Structured JSON:** [`5cd279231304c89670ad.json`](../../sessions/5c/5cd279231304c89670ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PID: 409855**（主进程，另有一个重复实例 PID 410078）

**进度: 11/50 docs**

参数确认：`--dataset docred --decoding_strategy beam --num_beams 4 --max_samples 50`，输出到 `outputs/w9_qwen_docred_beam_50.jsonl`。

注意：有两个相同的 beam search 进程在跑（409855 和 410078），可能会写同一个输出文件产生冲突。需要 kill 其中一个吗？

---
