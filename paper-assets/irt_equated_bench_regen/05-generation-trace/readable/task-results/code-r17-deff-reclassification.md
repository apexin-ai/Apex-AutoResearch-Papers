# code r17 deff reclassification

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r17_deff_reclassification_20260522T153259_result.json`
- **Structured JSON:** [`36cd206d448b14cd4101.json`](../../sessions/36/36cd206d448b14cd4101.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

2229 lines = 2228 data rows + header. Correct.

**Done.** Outputs in `artifacts/r17_deff_reclassification/`:

- **`deff_reclassification_report.md`** — full breakdown
- **`deff_reclassification_results.csv`** — 2228 reclassified items

Key findings:
- **100% of C→non-C reclassifications are C→A via significance loss** (assertions verified — all have |Δ_MH| ≥ 1.5 and adj_p ≥ 0.05)
- Simple DEFF: 269/3918 C items reclassified (6.9%), 74% near-miss (adj_p 0.05–0.10)
- Weighted DEFF: 2228/3918 reclassified (56.9%), 65.5% clearly non-significant (adj_p ≥ 0.10)
- Simple is a strict subset of weighted (every simple-reclassified item is also weighted-reclassified)

---
