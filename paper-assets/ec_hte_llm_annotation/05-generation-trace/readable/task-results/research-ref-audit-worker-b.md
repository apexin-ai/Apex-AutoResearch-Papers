# research ref audit worker B

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-B_20260526T104748_result.json`
- **Structured JSON:** [`8619c759c5a51b7e3644.json`](../../sessions/86/8619c759c5a51b7e3644.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written. All 71 entries verified. Here's the summary:

**4 issues found across 71 entries:**

| Entry | Severity | Problem |
|---|---|---|
| `black2000racial` | **HIGH** | Bib contains a disability-programs paper (AER 2002) but tex cites it for "racial misclassification in administrative data" — the paper has nothing to do with racial misclassification. Citation context is factually wrong. |
| `wood2018challenges` | MEDIUM | Wrong page numbers: bib says 5179-5186, correct is 4586-4598 |
| `dorn2022sharp` | MEDIUM | Wrong DOI: bib has `...2064774`, correct is `...2069572` |
| `pangakis2023automated` | MEDIUM | Bib lists venue as EMNLP 2023 Findings but paper not found in ACL Anthology; appears to be arXiv-only |

**All 10 high-risk entries confirmed as real papers** — no hallucinated references. The `black2000racial` issue is the most critical: a reviewer would immediately flag citing a disability-programs paper for claims about racial misclassification.

---
