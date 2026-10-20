# exp qwen conll seed456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen_conll_seed456_20260518T092856_result.json`
- **Structured JSON:** [`99da7474a8445bb1f442.json`](../../sessions/99/99da7474a8445bb1f442.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Merged model cleaned up. Everything complete. Here's the comparison summary:

## CoNLL seed=456 vs seed=42

| Metric | seed=456 | seed=42 |
|--------|----------|---------|
| **greedy_f1** | 0.9068 | 0.9079 |
| **oracle_f1** | 0.9453 | 0.9468 |
| **headroom** | 3.84pp | 3.89pp |
| **degen (CF1 gold-filtered)** | 62.9% | 59.1% |

**Selection F1 (all signals below greedy):**

| Signal | seed=456 F1 | seed=456 delta | seed=42 delta |
|--------|-------------|----------------|---------------|
| SJ | 0.9025 | **-0.45pp** | -0.57pp |
| FK | 0.9018 | **-0.51pp** | -0.65pp |
| VC | 0.9001 | **-0.68pp** | -0.82pp |
| EM | 0.8996 | **-0.73pp** | -0.89pp |
| LP | 0.8997 | **-0.73pp** | -1.05pp |

**Summary line:**
```
seed=456: greedy_f1=0.9068, LP_sel_f1=0.8997, LP_delta=-0.73pp, degen=62.9%
vs seed=42: greedy_f1=0.9079, LP_delta=-1.05pp, degen=59.1%
```

**Conclusion:** The LP negative result is confirmed robust across seeds. At seed=456, LP delta is -0.73pp (vs -1.05pp at seed=42). All 5 signals are negative vs greedy on CoNLL, with degeneracy even higher (62.9% vs 59.1%). The negative LP delta is smaller in magnitude but still clearly negative. Self-consistency selection cannot beat greedy on CoNLL regardless of seed.

---
