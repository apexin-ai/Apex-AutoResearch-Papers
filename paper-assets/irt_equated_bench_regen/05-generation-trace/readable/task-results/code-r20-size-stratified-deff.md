# code r20 size stratified deff

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r20_size_stratified_deff_20260522T192219_result.json`
- **Structured JSON:** [`b55f25b835e27a701abe.json`](../../sessions/b5/b55f25b835e27a701abe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 deliverables produced. Summary of results:

**Part A1 — Size-Stratified DEFF:**

| Tier | Families | Mean m̄ | ICC | DEFF | Adj C% |
|------|----------|--------|------|------|--------|
| 2–10 | 9 | 5.3 | 0.2458 | 2.07 | 31.3% |
| 11–50 | 11 | 22.1 | 0.2264 | 5.78 | 24.6% |
| 51–200 | 8 | 91.4 | 0.1365 | 13.34 | 13.7% |
| >200 | 2 | 431.0 | 0.0817 | 36.11 | 9.0% |
| Simple m̄ | 30 | 62.8 | 0.0465 | 3.87 | **29.2%** |
| Weighted m̄ | 30 | 254.5 | 0.0465 | 12.79 | **13.5%** |

Per-tier ICC is much higher than overall ICC (0.08–0.25 vs 0.047) because the ANOVA ICC computed across all 30 families is diluted by size heterogeneity. The parameterization curve shows a smooth monotonic decrease from ~31% to ~8% as m̄ increases from 2 to 350.

**Part A2 — Family Sensitivity:**

| | Fine-grained | Coarse |
|--|-------------|--------|
| Families | 30 | 22 |
| DEFF (simple) | 3.87 | 3.57 |
| DEFF (weighted) | 12.79 | 12.81 |
| C% (simple) | 29.2% | 29.4% |
| C% (weighted) | 13.5% | 13.2% |

Coarse grouping barely changes the adjusted C% — ICC drops (0.047→0.030) because merged sub-families are heterogeneous, but larger m̄ (63→86) compensates, yielding nearly identical DEFF. The result is robust to family definition choice.

---
