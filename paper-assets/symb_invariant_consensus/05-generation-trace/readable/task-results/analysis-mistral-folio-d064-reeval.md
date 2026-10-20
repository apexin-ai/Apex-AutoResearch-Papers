# analysis mistral folio d064 reeval

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral-folio-d064-reeval_20260522T125612_result.json`
- **Structured JSON:** [`bca2dfcdc1aaecd021a8.json`](../../sessions/bc/bca2dfcdc1aaecd021a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are in. Tiebreaking verification on the changed cases:

**Seed 123** — 2 SC ties resolved, 2 SICA ties resolved:
- SC `folio_2`: Unknown:4 vs False:4 → "False" wins alphabetically → gained 1 correct (gt=False)
- SC `folio_145`: 3-way tie (True:3, False:3, Unknown:3) → "False" wins → no accuracy change (gt=Unknown)
- SICA `folio_62`: False:30 vs Unknown:30 → "False" wins → lost 1 (gt=Unknown)
- SICA `folio_165`: False:35 vs Unknown:35 → "False" wins → gained 1 (gt=False)

**Seed 456** — 1 SC tie resolved, 0 SICA:
- SC `folio_16`: Unknown:6 vs False:6 → "False" wins → lost 1 (gt=Unknown)

All tiebreaks correctly use `sorted(tied_candidates)[0]`.

```
| Seed    | SC (%)      | SICA (%)    | Δ (pp)      | n   |
|---------|-------------|-------------|-------------|-----|
| 123     | 54.41       | 57.35       | +2.94       | 204 |
| 456     | 55.88       | 55.88       | +0.00       | 204 |
| 789     | 59.31       | 56.86       | -2.45       | 204 |
| Mean±SD | 56.53±2.51  | 56.70±0.75  | +0.16±2.70  | —   |
```

Verification checklist:
- [x] Tiebreaking = `sorted(tied_candidates)[0]` (alphabetical)
- [x] exp052 has 204 intermediates
- [x] exp053 has 204 intermediates
- [x] SC and SICA both use same tiebreaking logic
- [x] Mean = (seed123 + seed456 + seed789) / 3
- [x] SD = sample stdev (ddof=1)

---
