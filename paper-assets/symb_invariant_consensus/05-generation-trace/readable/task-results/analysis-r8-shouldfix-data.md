# analysis r8 shouldfix data

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r8-shouldfix-data_20260520T201253_result.json`
- **Structured JSON:** [`a1d48408e9ad9860521d.json`](../../sessions/a1/a1d48408e9ad9860521d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three files written to `/root/symb_invariant_consensus/results/r8_shouldfix_data/`.

**Results:**

**W6 Seed Annotations**: 31 conditions documented. All primary experiments use seed=42; Z3 solver seeds are hardcoded to 42 globally. 4 multi-seed groups identified (Mistral FOLIO: s42/789, Qwen14B FOLIO: s42/123, Qwen7B LogiQA: s42/123/456, ICG Mistral: s42/123/456).

**W7 Dedup Ablation** (exp033 Mistral-7B FOLIO-204):
- Avg 69 constraints/problem → 45.4 (string dedup) → 39.3 (Z3 dedup)
- Z3 dedup catches ~10% more semantic duplicates than string match
- Accuracy: Z3 dedup **59.31%** > string dedup 55.88% > no dedup 54.41%
- No-dedup vs Z3-dedup: significant at p=0.013 (McNemar)
- String vs Z3 dedup: marginally significant at p=0.065

---
