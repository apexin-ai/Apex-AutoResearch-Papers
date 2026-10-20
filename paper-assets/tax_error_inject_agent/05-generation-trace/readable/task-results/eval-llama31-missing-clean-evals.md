# eval llama31 missing clean evals

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama31-missing-clean-evals_20260516T145259_result.json`
- **Structured JSON:** [`b5b1384c0f6bc46e82cf.json`](../../sessions/b5/b5b1384c0f6bc46e82cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three tasks complete. Summary:

| Registry Entry | Status | Key Metric |
|---|---|---|
| `eval-llama31-random-s0-clean` | DONE | success_rate=0.745 |
| `eval-llama31-taxei-s42-clean` | DONE | success_rate=0.766 |
| `llama31-vanilla-s123-eval` | DONE | recovery_rate=0.702, detection_rate=0.213 |

**llama31-vanilla-s123 injected eval details:**
- Recovery rate 0.702 (33/47 episodes OK under injection)
- Detection rate 0.213 (10/47 detected the injected error)
- Best recovery: C1_context_truncation (0.75), C4_observation_masking (0.727)
- Best detection: C4_observation_masking (0.364), P1_step_order_swap (0.333)
- Worst detection: C1 and P2 both at 0.083
- pick_heat_then_place_in_recep had 100% recovery (8/8)

---
