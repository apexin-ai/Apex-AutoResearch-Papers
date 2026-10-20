# analysis exp 029a

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_029a_20260518T005854_result.json`
- **Structured JSON:** [`a08cbaab49d05f509429.json`](../../sessions/a0/a08cbaab49d05f509429.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 steps complete. Registry updated, artifact registered.

---

## exp_029a Results Summary

**Verdict: SUCCESS** — Hypothesis confirmed. SciERC 3-epoch degeneracy (6.4%) is dramatically lower than 5-epoch baseline (17.8%), a −11.4pp reduction.

| Metric | 5-epoch (baseline) | 3-epoch (exp_029a) | Delta |
|---|---|---|---|
| Degeneracy (CF1%) | 17.8% | **6.4%** | **−11.4pp** |
| Greedy F1 | — | 0.6501 | |
| Oracle F1 | — | 0.7998 | |
| Headroom | — | 14.97pp | |
| LP sel delta | +0.42pp | −1.18pp | −1.60pp |
| Within-inst median ρ | 0.6667 | 0.3172 | |

**QE Signals (AUROC / global ρ):**

| Signal | AUROC | ρ | Selection F1 | Δ vs greedy |
|---|---|---|---|---|
| LP | 0.664 | 0.355 | 0.638 | −1.18pp |
| SJ | 0.744 | 0.516 | 0.621 | −2.93pp |
| FK | **0.752** | **0.530** | 0.622 | −2.82pp |
| EM | 0.634 | 0.335 | 0.585 | −6.54pp |
| VC | 0.736 | 0.507 | 0.585 | −6.49pp |

**Key observations:**
1. Epoch-degeneracy relationship generalizes from Few-NERD to SciERC — fewer epochs → substantially lower degeneracy
2. LP selection now hurts (−1.18pp vs +0.42pp at 5-epoch), consistent with lower LP discriminability at lower degeneracy
3. Within-instance ρ dropped (0.32 vs 0.67), also consistent — with less degenerate outputs, LP has less variance to exploit
4. FK remains the best QE signal by AUROC (0.752), followed by SJ (0.744) and VC (0.736)

---
