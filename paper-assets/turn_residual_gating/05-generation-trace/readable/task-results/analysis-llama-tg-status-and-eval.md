# analysis llama tg status and eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_tg_status_and_eval_20260521T012333_result.json`
- **Structured JSON:** [`5b10248a00d25775d7eb.json`](../../sessions/5b/5b10248a00d25775d7eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Training still running.** Current status:

| Metric | Value |
|--------|-------|
| PID | 199643 (elapsed 5h17m) |
| GPU | RTX PRO 6000 Blackwell, 63.4/102 GB, 99% util |
| Current step | Epoch 1, Step 7650 |
| Optimizer step | ~1950 / 3000 (65%) |
| Gate mean | 0.929 (converged from 0.818 at init) |
| Gate std | 0.059 |
| L_NTP | ~0.76–1.10 (normal range) |
| L_GAR | ~0.0001–0.004 (near zero → GAR constraint satisfied) |
| L_DIV | 0.0000 |

**Gate profile (step 1900)** shows the expected V-shape — L25 lowest at 0.746, early/late layers near 0.97–0.99. This matches the Qwen-2.5 pattern where middle-to-late layers have lower gates.

**Config recap:** Llama-3.1-8B-Instruct, ultrachat_8k, LoRA + ThreadGate, gate_lr=0.002 (10× base), grad_accum=8, total 3000 optimizer steps.

**ETA:** At ~6.15 optimizer steps/min, ~1050 steps remaining → **~2h50m to completion** (roughly 12:00 UTC).

No action needed now — will check back when it should be done to start eval.

---
