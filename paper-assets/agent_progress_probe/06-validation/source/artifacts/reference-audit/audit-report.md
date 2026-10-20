# Reference Audit Report

**Date:** 2026-05-15
**Paper:** "Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision"
**Bib file:** `docs/paper/references.bib`

---

## Summary

| Metric | Count |
|--------|-------|
| Total bib entries | 46 |
| Total unique citation keys in .tex | 46 |
| Missing citations (cited but no bib entry) | 0 |
| Orphan entries (bib entry but never cited) | 0 |
| Verified via WebSearch (2025-2026 papers) | 13/13 |
| Hallucinated references | 0 |
| Issues found | 3 |

---

## Issues Found

### 1. [severity: warning] `chen2025monitoring` — Author name error

**Bib entry:** `Neelay Joshi`
**Actual author (per OpenReview, ICLR 2025 proceedings):** `Nitish Joshi`

Multiple sources (OpenReview, ICLR virtual site, citing papers) consistently list the second author as "Nitish Joshi", not "Neelay Joshi."

**Status:** FIXED in references.bib

---

### 2. [severity: info] `ratner2017snorkel` — Year inconsistency between key and field

**Bib key:** `ratner2017snorkel` (implies 2017)
**Year field:** `2018`
**Actual:** PVLDB Vol. 11, No. 3 published November 2017; VLDB conference presentation was August 2018.

Since the entry type is `@article` citing `Proceedings of the VLDB Endowment`, and PVLDB publication date is November 2017, the year field should be `2017` to match the key.

**Status:** FIXED — year changed to 2017

---

### 3. [severity: info] AAAI venue name inconsistency

Two entries cite AAAI with different booktitle formats:
- `safranchik2020linkedhmm`: `AAAI Conference on Artificial Intelligence`
- `ratner2019snorkelmetal`: `Proceedings of the AAAI Conference on Artificial Intelligence`

**Status:** FIXED — standardized both to `Proceedings of the AAAI Conference on Artificial Intelligence`

---

## Verification Log (2025-2026 References)

All 13 recent references (2025-2026) verified via WebSearch:

| Key | arXiv/Venue | Status |
|-----|-------------|--------|
| `xi2025agentprm` | arXiv:2511.08325 | Verified |
| `choudhury2025prm` | arXiv:2502.10325 | Verified |
| `li2026toolprmbench` | arXiv:2601.12294 | Verified |
| `wang2026planrewardbench` | arXiv:2604.08178 | Verified |
| `chen2025monitoring` | ICLR 2025 Workshop | Verified |
| `kale2025weaktostrong` | arXiv:2508.19461 | Verified |
| `fan2026agentrm` | arXiv:2601.22154 | Verified |
| `qiu2026dataprm` | arXiv:2604.24198 | Verified |
| `orlanski2026slopcodebench` | arXiv:2603.24755 | Verified |
| `cemri2025multiagentfail` | arXiv:2503.13657 | Verified |
| `zhu2025agentfail` | arXiv:2509.25370 | Verified |
| `george2025cycledetection` | arXiv:2511.10650 | Verified |
| `pipis2025reasoningloop` | arXiv:2512.12895 | Verified |
| `liu2026trajad` | arXiv:2602.06443 | Verified |
| `zhang2025qwen3embedding` | arXiv:2506.05176 | Verified |

---

## Field Completeness Check

All 46 entries have required fields (title, author, year, venue). Observations:
- ArXiv preprints lack volume/pages — standard practice, no action needed
- `kaufman2012leakage` is the only article entry with full volume/number metadata
- `vanderaalst2016processmining` (book) has publisher and edition — complete
- "and others" used consistently for author truncation across all entries

---

## Cross-Reference Matrix

All .tex files checked: `abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `analysis.tex`, `conclusion.tex`, `limitations.tex`, `appendix.tex`

Citation commands found: `\citep{}`, `\citet{}`, `\citeauthor{}`

Every `\cite` key maps to a bib entry; every bib entry is cited at least once.
