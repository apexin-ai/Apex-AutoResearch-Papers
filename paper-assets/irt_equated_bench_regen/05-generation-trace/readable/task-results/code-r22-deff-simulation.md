# code r22 deff simulation

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r22_deff_simulation_20260523T081051_result.json`
- **Structured JSON:** [`a0292660ae88de7629cc.json`](../../sessions/a0/a0292660ae88de7629cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 outputs are generated. Summary:

**Simulation results** (2000 items, 30% GT DIF, 50 seeds per scenario):

| Scenario | DEFF(simple) | DEFF(weighted) | Emp MH DEFF | Adj C%(s) | Adj C%(w) | Winner |
|---|---|---|---|---|---|---|
| **B (METABENCH-like)** | 3.08 | 9.93 | 5.45 | **26.8%** (−3.2%) | 1.6% (−28.4%) | **Simple** |
| C (extreme skew) | 1.78 | 7.51 | 5.50 | **37.4%** (+7.4%) | 2.4% (−27.6%) | **Simple** |
| D (homog ICC) | 3.00 | 9.57 | 7.04 | **34.1%** (+4.1%) | 2.2% (−27.8%) | **Simple** |

**Key mechanism**: MH stratification reduces effective DEFF to 3.7–7.0 (far below the analytical DEFF of 8–26). Simple-mean DEFF (≈3) is much closer to this reduced effective DEFF than weighted-mean (≈10), so its Rao-Scott correction preserves true DIF items while weighted overcorrects and destroys signal.

For Scenario B (mimicking METABENCH), simple-mean recovers GT within 3.2 percentage points — nearly matching the paper's empirical finding of Adj C% = 29.2% vs GT ≈ 30%.

---
