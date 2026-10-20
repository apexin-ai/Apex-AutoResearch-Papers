# ssh kill cascade start d067

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_cascade_start_d067_20260519T232254_result.json`
- **Structured JSON:** [`05b88b6a8cdbfab5b10e.json`](../../sessions/05/05b88b6a8cdbfab5b10e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- **Killed**: d064 llama docred beam4 cascade（PID 122747/99652/99651），已运行 4.5h
- **Started**: d067 seed variance on GPU0（PID 132647），6 配置串行（qwen_scierc/llama_scierc/qwen_docred × seeds 123,456），每个跑 unconstrained + full_s1
- **GPU 分配**: GPU0 → d067, GPU1 → d066 beam sweep（不干扰）
- 因 GPU1 被 d066 占用，d067 全串行在 GPU0，预计 ~9h
- 报告已写入 `artifacts/_project/report/d067_start.md`

---
