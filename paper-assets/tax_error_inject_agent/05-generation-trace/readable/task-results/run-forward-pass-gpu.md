# run forward pass gpu

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_forward-pass-gpu_20260515T153743_result.json`
- **Structured JSON:** [`7076f3919a52622dde46.json`](../../sessions/70/7076f3919a52622dde46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's the final summary:

**Experiment `v4-training-dynamics-forward` — DONE (success)**

| Checkpoint | Clean Loss | Injected Loss | Gap |
|---|---|---|---|
| Vanilla | 0.6853 | — | — |
| TaxEI Full | 0.7712 | 0.6139 | -0.1573 |
| Random Full | 0.7354 | 0.5902 | -0.1452 |
| TaxEI 10% | 0.6628 | 0.6464 | -0.0164 |
| TaxEI 25% | 0.7010 | 0.5740 | -0.1270 |
| TaxEI 50% | 0.8516 | 0.6547 | -0.1969 |

**TaxEI Full per-operator loss:** C1=0.5932, P2=0.6161, P1=0.6165, C4=0.6298

**Key findings:**
- Clear dose-response: injected-clean gap widens monotonically from -0.016 (10%) → -0.127 (25%) → -0.197 (50%)
- C1_ContextTruncation consistently has the lowest loss (most memorized)
- Higher injection rates also degrade clean sample loss significantly (0.663 → 0.701 → 0.852)
- 3 plots generated: dose_response, operator_breakdown, subset_comparison

Registry updated with full metrics, conclusion=success, status=DONE. Artifact registered.

---
