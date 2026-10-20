# cleanup tmux

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_tmux_20260515T162831_result.json`
- **Structured JSON:** [`8d8425bd5201b14f70b1.json`](../../sessions/8d/8d8425bd5201b14f70b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前有 3 个 tmux session，但没有 `exp_001_n16_seed456`。现有 session：
- `exp_011_ood_conll_to_scierc`
- `exp_017_llama_conll_n16_r1024`
- `exp_017_llama_conll_n16_s456_r1024`

目标 session `exp_001_n16_seed456` 不存在，可能已经被清理过了。需要 kill 这些现有 session 吗？

---
