# code r17 k sensitivity

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r17_k_sensitivity_20260522T153245_result.json`
- **Structured JSON:** [`084fe174d082b47d326d.json`](../../sessions/08/084fe174d082b47d326d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated. Results:

| K | C% | B% | A% |
|---:|-----:|-----:|-----:|
| 3 | 39.37 | 20.46 | 40.17 |
| **5** | **31.32** | 17.56 | 51.11 |
| 7 | 32.72 | 17.77 | 49.50 |
| 10 | 35.92 | 16.49 | 47.59 |
| 20 | 32.93 | 15.41 | 51.66 |

- K=5 baseline: 31.32% — matches expected 31.3%
- K=3 inflates C% to 39.4% (under-stratification, expected)
- K≥5 range: 31.3%–35.9%, max |ΔC%| = 4.60pp — above the 3pp robustness threshold, driven by K=10 being elevated at 35.9% while K=5/7/20 cluster around 31–33%

Outputs saved to `artifacts/r17_k_sensitivity/`: report, CSV, and reproducible script.

---
