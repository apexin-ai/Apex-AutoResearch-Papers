# paper d044 critical fixes

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d044_critical_fixes_20260516T095301_result.json`
- **Structured JSON:** [`2f9bb8820d925b21d75d.json`](../../sessions/2f/2f9bb8820d925b21d75d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Structure:
- Pages 1–2: intro/setup
- Page 3–5: results.tex  
- Page 6: sdgd_negative.tex
- Page 6–7: discussion.tex (includes conclusion)
- Page 7–8: checklist

Body content (intro through conclusion) ends on page 7. ≤ 8 pages confirmed.

---

**Summary of corrections:**

| # | File | Line | Before | After |
|---|------|------|--------|-------|
| 1 | abstract.tex | 4 | "MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding." | "Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend." |
| 2 | discussion.tex | 13 | "confusability-aware batch composition recovers +1.4\,pp on RE where span reconciliation is unnecessary" | "confusability-aware grouping yields a directionally consistent but non-significant improvement (+1.4\,pp, $p\approx 0.19$)" |
| 3 | results.tex | 67 | "into gaps reaching 31.2\,pp under extreme-batch comparison" | "into quartile gaps of 3.9--5.3\,pp under typical batching, reaching 31.2\,pp only under extreme-batch construction" |
| 4 | results.tex | 65, 72 | "quasi-experimental" (×2) | "controlled stratified comparison" (×2) |
| 5 | results.tex | after line 124 | (none) | New paragraph on 80-rel null result (IQR=0.033, n=25, slope=+0.221, p=0.762) |

**Compilation**: Clean — no undefined citations, no broken references.  
**Pages**: 15 total; body (intro–conclusion) = 7 pages (≤ 8 ✓).

---
