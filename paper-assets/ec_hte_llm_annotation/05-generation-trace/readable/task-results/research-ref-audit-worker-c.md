# research ref audit worker C

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-C_20260526T104757_result.json`
- **Structured JSON:** [`5496dd02a1363c88287c.json`](../../sessions/54/5496dd02a1363c88287c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written. Here's the summary:

**71 entries verified. No hallucinated papers.** All are real publications.

**8 issues found:**

| Severity | Key | Problem |
|----------|-----|---------|
| **HIGH** | `black2000racial` | **Wrong paper in bib.** Bib has a paper about disability programs/coal booms, but tex cites it for "racial misclassification in administrative data." Complete mismatch. |
| **HIGH** | `dorn2022sharp` | Wrong DOI (`2064774` → should be `2069572`). Currently uncited. |
| **MEDIUM** | `wood2018challenges` | Wrong pages (`5179--5186` → should be `4586--4598`). Currently uncited. |
| **MEDIUM** | `patrini2017making` | Possibly wrong pages (`1944--1952`). Needs verification. Currently uncited. |
| **MEDIUM** | `sui2026ppci` | Citation context says "outcome-side misclassification" but paper is about conditional inference at test points. |
| **MEDIUM** | `mozer2026ppi` | Citation context says "arm-specific PPI" but paper is about PPI = difference estimator equivalence. |
| **LOW** | `bu2023forestiv` | Key says "bu2023" but authors are Yang et al. and year is 2022. Content correct. |
| **LOW** | `tornberg2024chatgpt` | Key says 2024, year field correctly says 2025. |

**30 of 71 entries are not cited** in any tex file — should be cleaned up or cited.

The `black2000racial` issue is the most urgent: the tex makes a factual claim attributed to the wrong paper.

---
