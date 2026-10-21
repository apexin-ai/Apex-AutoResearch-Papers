# analysis sf3 qwq l60 rerun

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf3_qwq_l60_rerun_20260519T152102_result.json`
- **Structured JSON:** [`855312eb975d28679ea0.json`](../../sessions/85/855312eb975d28679ea0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results with L60 corrected:

| Method | HS BA | Text BA | Gap | p |
|---|---|---|---|---|
| **linear** | 0.6747 | 0.6006 | **+7.4pp** | 0.0017 |
| **quadratic** | 0.5805 | 0.5901 | -1.0pp | 0.6384 |

The linear gap is +7.4pp (vs. expected ~3.7pp from original R12). The gap is larger than expected but directionally consistent — the difference could come from R12 using W=3 with a different PCA/bootstrap setup or different text embeddings. The key finding holds: linear residualization preserves HS advantage, quadratic residualization absorbs it (gap goes to -1.0pp, non-significant).

Output files:
- `qwq_l60_w3_results.json` — separate corrected results
- `qwq_w3_results.json` — updated
- `report.txt` — appended with "L60 corrected" section

---
