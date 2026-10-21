# review pre submission checklist

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_pre_submission_checklist_20260515T062759_result.json`
- **Structured JSON:** [`0f75679d0dcde8fe67d6.json`](../../sessions/0f/0f75679d0dcde8fe67d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pre-submission Checklist Report

### 1. Anonymization [PASS]
- `\author{Anonymous ACL submission}` — correctly anonymized (`main.tex:20`)
- `\usepackage[review]{acl}` — review mode enabled (`main.tex:3`)
- No author names, institutions, personal URLs, emails, or ORCIDs found in any .tex file
- No Acknowledgments section present
- GitHub URLs found only in bibliography entries (`relwork_new_entries.bib`, `main.bbl`) referencing third-party tool `guidance-ai/guidance` — not the authors' repo, acceptable

### 2. Format Compliance [PASS]
- **documentclass**: `\documentclass[11pt]{article}` with `\usepackage[review]{acl}` — standard ACL template (`main.tex:1,3`)
- **Font**: `\usepackage{times}` present (`main.tex:5`)
- **Paper size**: ACL template defaults to US Letter — correct
- **Margin overrides**: None found (no `\geometry`, `\setlength{\textwidth}`, `\addtolength`, etc.)

### 3. Appendix References [WARN]
- **Orphan references**: None — all `\ref{app:...}` have matching labels
- **Orphan labels** (defined but never `\ref`'d):
  - `\label{app:related_work}` — `appendix_related_work.tex:2`
  - `\label{app:discussion}` — `appendix_discussion.tex:4`
- Only `app:llama-per-relation` is actually cross-referenced from the main text (`section5_crossmodel_draft.tex:69`)
- The comment "Full discussion paragraphs moved to Appendix B" (`section7_conclusion_compressed.tex:2`) is a comment, not a proper `\ref` — readers have no way to navigate to these appendices

### 4. Figure/Table Numbering [PASS]
**Tables in main text** (in document order):
| # | Label | File |
|---|-------|------|
| Table 1 | `tab:prompt_comparison` | `section3_violation_landscape.tex:23` |
| Table 2 | `tab:scierc-ablation` | `section5_scierc_draft.tex:71` |
| Table 3 | `tab:docred-ablation` | `section5_docred_draft.tex:56` |
| Table 4 | `tab:cross-model` | `section5_crossmodel_draft.tex:45` |

**Tables in appendix:**
| # | Label | File |
|---|-------|------|
| Table 5 (or A1) | `tab:llama-per-relation-dr` | `appendix_llama_per_relation.tex:15` |

**Figures:**
| # | Label | File |
|---|-------|------|
| Figure 1 | `fig:per_relation_dr` | `section3_violation_landscape.tex:43` |

- Sequential, no gaps, no commented-out environments causing skips
- Note: draft files not `\input`'d (e.g., `paper_tables_draft.tex`, `section5_*_4796e8.tex`) contain duplicate labels but are harmless since they're excluded from compilation

### 5. Ethics/Limitations [FAIL]
- **Limitations**: Present as `\paragraph{Limitations.}` inside `\section{Discussion and Conclusion}` (`section7_conclusion_compressed.tex:29`). Content is ~4 lines. **However, EMNLP/ARR requires Limitations as a standalone `\section*{Limitations}` after the conclusion, not as a paragraph embedded within another section.** This will likely be flagged by the checklist reviewers.
- **Ethics Statement**: Not found anywhere. **WARNING** — recommended but not required by ARR policy.

---

### Needs Fix Summary
1. **[MUST FIX] Limitations section format** — Move `\paragraph{Limitations.}` out of Discussion and Conclusion into its own `\section*{Limitations}` between the conclusion and bibliography in `main.tex`. Current location: `section7_conclusion_compressed.tex:29-33`.
2. **[SHOULD FIX] Appendix cross-references** — Add `\ref{app:related_work}` and `\ref{app:discussion}` somewhere in the main text (e.g., "Extended related work in Appendix~\ref{app:related_work}; full discussion in Appendix~\ref{app:discussion}"), or remove the orphan appendices if not needed.
3. **[RECOMMENDED] Ethics Statement** — Add a brief `\section*{Ethics Statement}` (even 2-3 sentences) after Limitations. ARR reviewers increasingly expect it.

---
