# analysis r16 supplementary

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16_supplementary_20260521T031651_result.json`
- **Structured JSON:** [`ae70af263bd482370caa.json`](../../sessions/ae/ae70af263bd482370caa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 sub-tasks complete. Results written to `artifacts/r16_verification/task_c_supplementary.json`.

**Summary:**

| Sub-task | Key Finding |
|---|---|
| **WikiEvents κ̄** | **0.029** — extremely tight (vs SciERC 0.38, DocRED 0.82). 27 entity types, 56 event types, avg 21.2 valid pairs per event type out of 729 possible. |
| **70B CF** | 7.01% on DocRED (no SciERC 70B exists). 2–3× higher than 8B ZS (2.57%), 20–30× higher than 8B FT (0.2%). Primarily a ZS→FT gap, INT4 quantization likely contributes. |
| **Citations** | Both **REAL**. regino2025kgcurator → GenAIK@COLING 2025; formattax2026 → arXiv 2604.03616. |
| **±0.6pp R-F1** | **Holds for RE** (max \|Δ\|=0.30pp on SciERC+DocRED). **Exceeds on WikiEvents**: Llama FT Arg-F1 delta = −1.07pp. If the claim scopes to R-F1 only it's accurate; if covering all datasets, needs widening to ±1.1pp or explicit exclusion of WikiEvents (where CIs overlap). |

---
