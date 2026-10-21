# ssh scierc n32 results mv

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scierc_n32_results_mv_20260522T040555_result.json`
- **Structured JSON:** [`6984b34f893cadf44173.json`](../../sessions/69/6984b34f893cadf44173.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three SciERC N-scaling recomputes done. Complete results (all strict MV, gold-nonempty filtered):

### SciERC N-scaling (seed42, NER, strict MV)

| Metric | N=8 | N=16 | N=32 |
|---|---|---|---|
| **greedy_f1** | 0.6683 | 0.6651 | 0.6629 |
| **mv_strict_f1** | 0.6558 | 0.6622 | 0.6706 |
| **Δ_SC strict (pp)** | -1.24 | -0.29 | +0.78 |
| **mv_incl_f1** | 0.6640 | 0.6782 | 0.6708 |
| **oracle_f1** | 0.7840 | 0.8179 | 0.8399 |
| **degeneracy_rate** | 13.4% | 7.6% | 3.6% |
| **α_crit_eff_strict** | 0.3859 | 0.3597 | 0.3438 |

Key observations:
- Strict MV only becomes positive at N=32 (+0.78pp); N=8 and N=16 are negative
- Degeneracy rate drops monotonically: 13.4% → 7.6% → 3.6%
- Oracle headroom grows with N: 0.78 → 0.82 → 0.84
- The N=16 greedy_f1 differs slightly across runs (0.6651 vs report.json 0.6621) because recompute filters gold-empty instances

Data sources:
- N=8: `output/scierc_mf4v2_seed42/`
- N=16: `output/exp_001_seed42_v2/`
- N=32: `output/scierc_n32_s42/`

---
