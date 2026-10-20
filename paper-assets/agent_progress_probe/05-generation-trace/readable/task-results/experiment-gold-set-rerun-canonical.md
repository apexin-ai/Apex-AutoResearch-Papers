# experiment gold set rerun canonical

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_gold-set-rerun-canonical_20260515T090134_result.json`
- **Structured JSON:** [`efb53156a5fc962902d5.json`](../../sessions/ef/efb53156a5fc962902d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both runs complete. Here are the corrected results:

---

## Gold Exclusion Impact

- **39 gold windows excluded** from 10,634 training windows (both scripts confirmed)
- `evaluate_gold_set.py` already had this fix; `gold_bootstrap_ci.py` was missing it

## Corrected Eval Results (evaluate_gold_set.py)

| Model | N | Macro-F1 | Accuracy |
|---|---|---|---|
| MV Labels | 195 | 0.7184 | 0.7487 |
| GRU Probe | 132 | 0.7348 | 0.7348 |
| **Structural RF** | 195 | **0.7516** | 0.7744 |
| **Structural GB** | 195 | **0.7644** | 0.7897 |
| TWV Labels | 136 | 0.7184 | 0.7279 |
| TWV Probe | 132 | 0.7684 | 0.7727 |

## Corrected Bootstrap Results (gold_bootstrap_ci.py)

On shared windows (with gold exclusion):
- GB: 0.8023, RF: 0.8041 (bootstrap uses different evaluation path)

| Test | Delta | 95% CI | p-value | Sig? |
|---|---|---|---|---|
| GB vs MV | +0.0839 | [+0.032, +0.138] | 0.0005 | **YES** |
| GB vs GRU Probe | +0.0499 | [-0.016, +0.120] | 0.0698 | NO |
| RF vs GB | +0.0018 | [-0.015, +0.020] | 0.4775 | NO |
| TWV Probe vs GB | -0.0163 | [-0.067, +0.031] | 0.2536 | NO |
| TWV Probe vs GRU | +0.0336 | [-0.029, +0.099] | 0.1499 | NO |

## Comparison with Pre-Fix Numbers

| Model | Before (eval) | After (eval) | Before (bootstrap) | After (bootstrap) |
|---|---|---|---|---|
| **GB** | 0.760 | **0.764** | 0.802 | **0.802** |
| **RF** | 0.757 | **0.752** | — | **0.804** |

Key observations:
- GB eval F1 rose slightly 0.760→0.764 (lr 0.1→0.05 helped marginally, gold exclusion had minimal effect since evaluate_gold_set.py already had it)
- RF eval F1 dropped slightly 0.757→0.752 (n_estimators 200→100)
- Bootstrap GB was already 0.802 (pre-fix) and stays at 0.802 — the gold exclusion in bootstrap was the main fix, but the hyperparameter change (lr 0.05) and gold exclusion effectively cancel out
- RF and GB are now statistically indistinguishable (p=0.48)
- Only GB vs MV is significant (p=0.0005)

---
