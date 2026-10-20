# ssh submit freeform conll cuda1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_freeform_conll_cuda1_20260522T130210_result.json`
- **Structured JSON:** [`ed087b1437a014b51f00.json`](../../sessions/ed/ed087b1437a014b51f00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 GPUs are occupied:
- **GPU 0**: PID 145028, running ~1 min (just started)
- **GPU 1**: PID 145036, running ~1 min (just started) — `exp_conll_freeform` or `exp_fewnerd_freeform` grabbed this
- **GPU 2**: PID 136811, running 1h36m
- **GPU 3**: PID 138176, running 1h33m

Two new experiments (`exp_conll_freeform` and `exp_fewnerd_freeform`) were submitted by another process seconds before mine and took GPU 0 and GPU 1. Our submission crashed on the GPU collision.

No GPU is currently free. Options:
1. **Wait** for one of the GPU 2/3 jobs (~1.5h running) to finish
2. **Kill** one of the two just-started freeform experiments if one of them is redundant with ours
3. Check if `exp_conll_freeform` is identical to what we need (making ours unnecessary)

Want me to check what command `exp_conll_freeform` is running to see if it already covers this ablation?

---
