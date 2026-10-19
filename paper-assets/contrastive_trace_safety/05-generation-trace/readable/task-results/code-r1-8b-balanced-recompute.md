# code r1 8b balanced recompute

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r1_8b_balanced_recompute_20260516T222042_result.json`
- **Structured JSON:** [`c7ba85c3c92bddd69e74.json`](../../sessions/c7/c7ba85c3c92bddd69e74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. All r1-8b metrics recomputed with unified balanced config. Results:

| Method | Acc | Coverage | Lead | Pre-CP FPR | Precision |
|--------|-----|----------|------|------------|-----------|
| Text Static | 68.6% | 34.9% | +9.8 | 0.2576 | 0.4160 |
| Text Temporal W=15 | 72.9% | 60.5% | +10.3 | 0.2053 | 0.4720 |
| HS Static LR L14 | 81.7% | 46.5% | -2.0 | 0.0965 | 0.6926 |
| HS Temporal LR W=5 | 82.0% | 67.4% | +0.6 | 0.1020 | 0.6855 |
| HS Temporal LR W=10 | 81.4% | 69.8% | +0.3 | 0.0986 | 0.6827 |
| HS Temporal LR W=15 | 81.3% | 62.8% | -0.1 | 0.0877 | 0.6972 |
| HS GRU Multi-7L | 81.8±1.0% | 72.9±4.0% | +4.5±3.0 | 0.1654±0.0413 | 0.6221±0.0443 |

Outputs saved:
- `artifacts/r1_8b_balanced_recompute/full_results.json`
- `artifacts/r1_8b_balanced_recompute/paper_table.md`
- Project knowledge file `memory.md` updated

---
