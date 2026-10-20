# code r4 sf5 sf7 llama docred

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r4_sf5_sf7_llama_docred_20260517T105428_result.json`
- **Structured JSON:** [`a0f3add031eccec1ac9a.json`](../../sessions/a0/a0f3add031eccec1ac9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the summary:

**SF5: Llama DocRED Parse-Failure-Excluded**
- 91/998 (9.1%) documents are parse failures
- Violations unchanged (already excluded): DR=2.55%, CF=12.02%, ET=0%, RV=0%
- F1 after exclusion: E-F1=58.18 (+3.17pp), R-F1=6.51 (+0.23pp)
- Precision stays the same; recall improves because parse failure docs' gold items no longer penalize

**SF7: DocRED Fallback Coverage**
- DocRED effective semantic constraint coverage = **99.9%** (fallback rate = 0.08%)
- vs SciERC = 63.4% (fallback rate = 36.6%)
- The large discrepancy is a tokenization artifact: SciERC has multi-token types (2.87 mask calls per type field) where continuation tokens always conflict with semantic mask. DocRED types are all single-token, eliminating this inflation.

Results written to `artifacts/r4_sf5_sf7_results.md`.

---
