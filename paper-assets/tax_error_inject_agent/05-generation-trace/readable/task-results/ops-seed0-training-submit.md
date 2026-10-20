# ops seed0 training submit

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed0-training-submit_20260514T175725_result.json`
- **Structured JSON:** [`f77125488183d6ee6d5c.json`](../../sessions/f7/f77125488183d6ee6d5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个训练都在正常跑，无需清理重提交。

| 会话 | GPU | 进度 | 预计剩余 |
|------|-----|------|---------|
| v4-taxei-seed0 | cuda:1 | 449/3387 (13%) | ~1h30m |
| v4-random-seed0 | cuda:2 | 443/3387 (13%) | ~1h32m |
| v4-vanilla-seed0 | cuda:0 | 416/1635 (25%) | ~44m |

loss 都在正常下降（~0.5-0.6），训练速度 ~2s/it，一切正常。

---
