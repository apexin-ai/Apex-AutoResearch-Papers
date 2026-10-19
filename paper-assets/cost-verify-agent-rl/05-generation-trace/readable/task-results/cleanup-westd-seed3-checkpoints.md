# cleanup westd seed3 checkpoints

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_westd_seed3_checkpoints_20260521T084651_result.json`
- **Structured JSON:** [`3a9f9437afcac33c80a0.json`](../../sessions/3a/3a9f9437afcac33c80a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

删除完成。

| | 删除前 | 删除后 |
|---|---|---|
| 已用 | 144G (58%) | 79G (32%) |
| 可用 | 107G | 172G |
| 释放 | — | **~65G** |

`exp029-seed3/` 目录已删除。剩余 checkpoints 目录下还有 9 个子目录（exp029_seed3、gae_baseline、各 SFT/eval 等）。

---
