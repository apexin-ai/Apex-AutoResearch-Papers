# analysis r16 beam998 status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16_beam998_status_20260521T025747_result.json`
- **Structured JSON:** [`6c6163d9bbfbe8df2904.json`](../../sessions/6c/6c6163d9bbfbe8df2904.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Status report written.

**Summary:**

| Experiment | Server | Progress | Elapsed | Avg/doc | ETA |
|---|---|---|---|---|---|
| Qwen beam4 998 | westd-21461 | 739/998 (74.0%) | 6h38m | 32.3s | ~2h20m |
| Llama beam4 998 | westd-16980 | 741/998 (74.2%) | 5h12m | 25.3s | ~1h48m |

Both experiments are healthy and progressing. Llama is ~27% faster per document. Neither has completed yet — no metrics to extract. The Qwen log shows occasional FAIL documents (timeouts at ~128s), but most process normally in 15-60s.

Estimated completion: Llama ~12:48 UTC, Qwen ~13:20 UTC today.

---
