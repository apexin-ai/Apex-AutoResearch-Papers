# verify br recompute qwen14b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_br-recompute-qwen14b_20260522T211003_result.json`
- **Structured JSON:** [`56ef50528ec7948d0f1a.json`](../../sessions/56/56ef50528ec7948d0f1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Computation complete. Here are the results:

## BR Recomputation: Qwen2.5-14B FOLIO (D061)

### Data Source
exp036 (`results/exp036_qwen25_14b_folio204/`), using SICA scores from intermediates as constraint weight proxy (per-trace constraint cache not available for this experiment).

### D061 Tiebreaking Impact on SC
- **Old** (insertion-order tiebreaking): 158/204 = 77.45%, 46 wrong
- **D061** (alphabetical tiebreaking): 155/204 = 75.98%, **49 wrong**
- 3 problems became wrong: `folio_16`, `folio_49`, `folio_95` (all had tied SC votes; alphabetical picks wrong answer)

### BR Results

| | n_err | BR | 95% CI |
|---|---|---|---|
| Paper (old) | 50* | 3.93 | [2.44, 7.11] |
| D061 recomputed | **49** | **3.85** | **[2.85, 5.53]** |

\* The old BR=3.93 was computed from a different data source (exp-026/folio_204_14b, now deleted).

### 3 Flipped Problems Detail
All have tied votes (6:6 split) and balanced gold_frac ~0.45–0.50:

| PID | Gold | Old SC | D061 SC | gold_frac |
|---|---|---|---|---|
| folio_16 | Unknown | Unknown | False | 0.456 |
| folio_49 | Unknown | Unknown | True | 0.486 |
| folio_95 | True | True | False | 0.501 |

### Summary
- **n_err_old**: 50 (from exp-026 data, now obsolete)
- **n_err_new**: 49 (exp036 D061)
- **BR_old**: 3.93
- **BR_new**: **3.85**
- Change: -0.08 (within CI noise)

The 3 newly-wrong problems have near-balanced constraint support (~50% gold), so adding them to the error set increases mean gold_frac slightly, pulling BR down. The difference is minimal and doesn't change the paper's conclusion (BR > 1, confirming symbolic confirmation bias).

---
