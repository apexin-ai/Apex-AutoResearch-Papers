# paper page compression

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_page-compression_20260524T123654_result.json`
- **Structured JSON:** [`2abab6a243fc1039f45e.json`](../../sessions/2a/2abab6a243fc1039f45e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Main text structure confirmed:
- Page 7: Diagnostic Framework (5.3), Escaping the Bottleneck (6)
- Page 8: Escaping the Bottleneck continues, Discussion and Conclusion (7), Limitations, References begin

The main text (sections 1-7, excluding Limitations) fits within 8 pages.

---

**Summary of changes:**

| Step | What | Savings estimate |
|------|------|-----------------|
| 1 | **Fig 4** (27 remediation strategies bar chart) moved from `analysis.tex` to `appendix.tex` (under `app:remediation`) | ~0.35 page |
| 2 | **Table 2** (`tab:frontier-scb`, BR across 9 models) moved from `analysis.tex` to `appendix.tex` (under `app:frontier-scb`) | ~0.3 page |
| 3 | **Related Work** compressed from 6 paragraphs to 4: merged "Distinction from CoT confirmation bias" and "Relationship to Huang" into "Neuro-symbolic reasoning"; trimmed redundant descriptions | ~0.4 page |

**Total estimated savings: ~1.05 pages** (related_work: 1661 bytes, analysis: 1828 bytes removed from main text).

All `\cite{}` commands preserved (60 citations verified). All `\ref{}` cross-references intact — labels now defined in appendix, and main text references updated to say "Appendix Table/Figure" where appropriate. Compiled PDF confirms main text fits within 8 pages.

---
