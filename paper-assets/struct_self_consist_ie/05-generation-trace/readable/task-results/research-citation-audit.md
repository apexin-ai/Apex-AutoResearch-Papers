# research citation audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_audit_20260517T085237_result.json`
- **Structured JSON:** [`c489cbd2b33b6181268a.json`](../../sessions/c4/c489cbd2b33b6181268a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 49 citations verified. Here's the audit report.

```
=== Citation Audit ===

Total citations: 49
Verified (correct): 44
Critical issues: 2
Minor metadata issues: 3
Not found / fabricated: 0
```

---

### CRITICAL ISSUES

**1. `xie2024selfevaluation` — WRONG AUTHORS + WRONG VENUE**

- **Bib authors**: Xie, Jie; Lu, Kai; Dong, Rui; Pan, Liangming; Han, Qi; Wang, Shasha; Huang, Deyu; Zhang, Junlan
- **Real authors**: Jie Ren, Yao Zhao, Tu Vu, Peter J. Liu, Balaji Lakshminarayanan
- **Bib venue**: NeurIPS 2024 (main conference)
- **Real venue**: NeurIPS 2023 Workshop ("I Can't Believe It's Not Better")
- The paper at arXiv:2312.09300 exists, title matches, but the author list is entirely fabricated. This is a hallucinated citation entry.

**2. `deguchi2024centroid` — WRONG VENUE + MISSING AUTHORS**

- **Bib venue**: "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)"
- **Real venue**: **Findings of ACL 2024** (Bangkok, pages 11009–11018)
- **Bib authors** (3): Deguchi, Kamigaito, Watanabe
- **Real authors** (6): Deguchi, Sakai, Kamigaito, Watanabe, Tanaka, Utiyama — missing 3 co-authors

---

### MINOR METADATA ISSUES

**3. `tian2023calibration`** — Title truncated (missing "Fine-Tuned with Human Feedback"), missing 3 co-authors (Allan Zhou, Archit Sharma, Rafael Rafailov). Core attribution correct.

**4. `oh2026latentsc`** — Listed as `@article` (arXiv preprint) but also published at **AAAI 2026**. Could update venue.

**5. `chen2024usc`** — Booktitle "arXiv preprint (ICML 2024 Workshop ICL)" is an unusual hybrid format.

---

### ALL OTHER 44 CITATIONS: VERIFIED

Every remaining entry was confirmed via WebSearch: paper exists, authors match, venue/year correct.

**Recommended fixes**: The two critical entries (`xie2024selfevaluation` and `deguchi2024centroid`) need immediate correction in the bib file. Want me to fix them?

---
