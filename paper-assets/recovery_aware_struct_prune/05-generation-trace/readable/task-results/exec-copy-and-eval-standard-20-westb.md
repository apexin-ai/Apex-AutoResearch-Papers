# exec copy and eval standard 20 westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_copy_and_eval_standard_20_westb_20260521T233534_result.json`
- **Structured JSON:** [`5b4f36ae355725a2606e.json`](../../sessions/5b/5b4f36ae355725a2606e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器之间无法直连（互相无法解析 hostname）。

**跨服务器复制失败**——westb-23072 和 westd-29022 之间没有直连网络，rsync/scp 双向都不通。需要改用 westd 方案，或者通过本地中转（但 checkpoint ~12GB，中转耗时较长）。

建议切换到 **westd:1 方案**——直接在 westd-29022 上用 cuda:1 跑 eval，避免大文件传输。

---
