# research bib full audit

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bib-full-audit_20260517T082424_result.json`
- **Structured JSON:** [`fd8fda1e8798ed056fb1.json`](../../sessions/fd/fd8fda1e8798ed056fb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes applied. Final summary:

## Audit Results — 57 entries total

### Fixed (8 entries)

| Key | Issue | Severity |
|-----|-------|----------|
| `oneke-2025` | **14 of 17 author names were hallucinated.** Corrected to real 13 authors (Luo, Ru, Liu, Yuan, Sun, Zhang, Liang, Zhang, Zhou, Wei, Zheng, Wang, Chen) | CRITICAL |
| `volkanovska2024ner` → `volkanovska2025ner` | **2 co-authors fabricated** (Padó, Möller); paper is sole-authored. Title incomplete (missing "Domain-Specific Few-Shot"), year 2024→2025, vol 37→38, no 1→2. Cite key updated in `related_work.tex` | CRITICAL |
| `gliner2-2025` | Title wrong → corrected to "Schema-Driven Multi-Task Learning for Structured Information Extraction"; URL updated to ACL Anthology | Medium |
| `iepile-2024` | Title: "Schema-Based" → "Schema-Conditioned"; venue: ACL Short Papers (not main); added pages | Medium |
| `json-schema-bench-2025` | Title: outdated v1 title → "JSONSchemaBench: A Rigorous Benchmark..." | Medium |
| `parse-2025` | Upgraded from arXiv preprint to EMNLP 2025 Industry Track | Low |
| `bogdanov2024nuner` | Pages 11586–11600 → 11829–11841 | Low |
| `sclar-sensitivity-2024` | Missing subtitle — left as-is (common practice to cite main title only) | Noted |

### Correct (49 entries)
All remaining entries verified — authors, titles, years, and venues match authoritative sources.

---
