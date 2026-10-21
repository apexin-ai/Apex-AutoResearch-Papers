# eval oracle folio regen

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_oracle-folio-regen_20260518T153028_result.json`
- **Structured JSON:** [`13b931c99f30a9d63c02.json`](../../sessions/13/13b931c99f30a9d63c02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here's the report:

## exp-031-oracle-folio-regen Results

| Metric | exp-031 (new) | exp-021 (old) |
|---|---|---|
| **Oracle SICA accuracy** | **89.71%** (183/204) | 88.24% (180/204) |
| SC accuracy | 75.49% (154/204) | 79.41% (162/204) |
| SICA(self) accuracy | 74.51% (152/204) | 79.41% (162/204) |
| **Oracle vs SC delta** | **+14.22pp** | +8.82pp |
| McNemar p-value | **2.0e-07** | 6.15e-05 |
| McNemar b/c | b=29, c=0 | - |
| Z3 gold agreement | 95.10% (194/204) | 94.6% (193/204) |
| FOL parse success | 204/204 (100%) | 204/204 (100%) |

**Per answer type (oracle / SC):**
| Type | n | Oracle | SC | Z3 agree |
|---|---|---|---|---|
| True | 72 | 97.2% | 93.1% | 95.8% |
| False | 63 | 93.6% | 87.3% | 92.1% |
| Unknown | 69 | **78.3%** | 46.4% | 97.1% |

**Key findings:**
- Oracle accuracy improved from 88.24% to **89.71%** (+1.47pp) despite different traces
- Delta vs SC dramatically increased from +8.82pp to **+14.22pp** (SC baseline dropped from 79.41% to 75.49% with new traces)
- McNemar b=29, c=0: oracle corrected 29 SC errors while never losing
- Biggest gain on **Unknown** problems: +31.9pp (78.3% vs 46.4%)
- 21 oracle errors: 18 from Z3 correct but no supporting trace, 3 from Z3 wrong + SC also wrong
- Conclusion unchanged from exp-021: **constraint extraction quality is the bottleneck, not the aggregation mechanism**

---
