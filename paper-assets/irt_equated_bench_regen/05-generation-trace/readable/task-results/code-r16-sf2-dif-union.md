# code r16 sf2 dif union

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r16_sf2_dif_union_20260522T133157_result.json`
- **Structured JSON:** [`1c95bb30a7a000653cb3.json`](../../sessions/1c/1c95bb30a7a000653cb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both output files are written:

- **`artifacts/r16_dif_union/dif_union_results.csv`** — 1,787 rows with per-item DIF classification flags
- **`artifacts/r16_dif_union/dif_union_report.md`** — full report

Key numbers:

| | Sig criterion (BH p<0.05) | Effect criterion (\|β\|≥0.5) |
|---|---|---|
| Only Uniform (ETS C) | 208 (11.6%) | 288 (16.1%) |
| Only Non-uniform | 377 (21.1%) | 317 (17.7%) |
| Both | 314 (17.6%) | 234 (13.1%) |
| **Union** | **899 (50.3%)** | **839 (47.0%)** |
| Jaccard | 0.349 | 0.279 |

Union is 47–50% — well above the 35% threshold. Overlap is moderate (Jaccard ~0.28–0.35), confirming that uniform and non-uniform DIF capture partially distinct item sets. Non-uniform DIF adds ~21% unique items that MH alone misses.

---
