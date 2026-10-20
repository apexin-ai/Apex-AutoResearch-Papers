# exp pooled irt gsm8k

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pooled_irt_gsm8k_20260514T201558_result.json`
- **Structured JSON:** [`8e9c9e8e6b6821493295.json`](../../sessions/8e/8e9c9e8e6b6821493295.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job started successfully. Key startup info:

| | |
|---|---|
| **Models** | **10** (0.5B: 4 dosages [0,5,25,100], 1.5B: 3 dosages [0,5,100], 3B: 3 dosages [0,5,100]) |
| **Items** | 1319 (GSM8K) |
| **Exposure** | 0.5B uses exp-002 delta signals; 1.5B + 3B fallback to oracle dosage (signals not yet computed) |
| **NUTS** | 4 chains × 1000 samples, fitting in progress |
| **Mean accuracy** | 0.444 |

The 1.5B/3B oracle fallback is expected — once those signals complete, the experiment can be re-run with real exposure. NUTS sampling is underway; should complete in 10–30 min. Want me to check back for results?

---
