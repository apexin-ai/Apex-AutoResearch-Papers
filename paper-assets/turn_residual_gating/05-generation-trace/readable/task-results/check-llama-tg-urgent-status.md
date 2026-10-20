# check llama tg urgent status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama_tg_urgent_status_20260521T012753_result.json`
- **Structured JSON:** [`fc20e30d0a2185e18c82.json`](../../sessions/fc/fc20e30d0a2185e18c82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Training still running.** Here's the status:

### Current Progress

| Metric | Value |
|--------|-------|
| Optimizer step | ~1956 / 3000 (65%) |
| Micro step | Epoch 1 Step 7650 / 24000 total |
| Epochs | 1.96 / 3 |
| L_NTP | ~0.75–1.1 (normal range) |
| L_GAR | ≈ 0 (converged since step ~800) |
| Gate mean | 0.929 |
| Gate std | 0.059 |
| Gate range | [0.746, 0.992] |
| GPU mem | 63.4 GB / ~102 GB |
| Wall clock | 5h 21m |

### Gate Layer Profile (step 1900)
Early layers (L0-L8): 0.95–0.99 (nearly pass-through)
Mid layers (L9-L18): 0.92–0.97
Late layers (L19-L28): **0.75–0.89** (most modulation)
Final layers (L29-L31): 0.89–0.95 (recovering)

L25 is the lowest at **0.746** — consistent with the Qwen pattern where late layers show the most gate opening.

### ETA Calculation
- Rate: 321 min / 1956 steps = 0.164 min/step
- Remaining: ~1044 steps × 0.164 = **~171 min ≈ 2h 51m**
- Expected completion: **~3 hours from now** (roughly 19:00 UTC)

### Checkpoint Status
- Epoch 0 checkpoint saved: `runs/phase2_llama_tg_s42/epoch_0/`
- Epoch 1 checkpoint saving in progress: `runs/phase2_llama_tg_s42/epoch_1/` (gate_params.pt + lora/)
- No `train_config.json` yet (written at end)

### Early Observations
- Gate dynamics match Qwen v7: L_GAR converges to ~0 quickly, gate values drift upward (0.82 → 0.93), late layers differentiate most
- The "deep-layer opening" pattern (L24-L28 lowest) is **replicating across architectures** — good sign for C5 cross-model claim

Training is healthy and on track. No action needed until completion. Want me to set up monitoring to check back in ~3 hours and auto-launch eval when done?

---
