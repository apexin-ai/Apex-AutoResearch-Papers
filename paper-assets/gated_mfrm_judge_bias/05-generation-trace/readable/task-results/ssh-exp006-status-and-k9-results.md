# ssh exp006 status and k9 results

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp006_status_and_k9_results_20260523T002849_result.json`
- **Structured JSON:** [`9b464a2371c8187bff8e.json`](../../sessions/9b/9b464a2371c8187bff8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the summary:

---

**exp-006 Status:**

| k | subsets done | raw_average τ | sequential τ | joint_gmfrm τ | status |
|---|---|---|---|---|---|
| k=2 | 9/10 | 0.755±0.088 | — (in results_full) | — (in results_full) | MCMC fits done (s1-s9) |
| k=4 | 10/10 | 0.779±0.041 | — (in results_full) | — (in results_full) | MCMC fits done (s0-s9) |
| k=6 | 6.5/10 | 0.800±0.030 | 7/10 seq done | 6/10 joint done | **warmup 24% on next fit** |
| k=8 | — | 0.786±0.000 | not started | not started | queued after k=6 |
| k=9 | **1/1 DONE** | **0.786** | **0.786** | **0.857** | **COMPLETE** |

**Session status:**
- `exp006_k9`: **DEAD** (completed successfully, results saved)
- `exp006_full`: **ALIVE** — currently fitting k=6, warmup at 24% (732/3000, ~4.57 it/s)

**k=9 result (the headline):** joint_gmfrm τ=0.857 vs sequential/raw_average τ=0.786. Joint outperforms by +0.071.

**k=6 ETA:** ~13 min per MCMC fit. 7 more fits remaining for k6 → ~1.5h for k=6. Then k=8 needs 20 fits → ~4.3h. **Total exp006_full remaining: ~6 hours.**

**Note:** results_k9/results.json is truncated (216 bytes, invalid JSON) — likely a write-flush issue at process exit. The CSV results are intact and complete.

---
