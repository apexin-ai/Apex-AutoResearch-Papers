# Paper Audit Report: trace-verdict-study

**Date**: 2026-05-16  
**Scope**: Citation integrity, data consistency, cross-references, ARR compliance, formatting

---

## 1. Citation Audit

### 1.1 Cross-Check Results

| Check | Result |
|-------|--------|
| Cited keys in .tex files | 28 unique keys |
| Bib entries in references.bib | 28 entries |
| Cited but missing from bib | **0** |
| In bib but never cited | **0** |

**Status: PASS** — perfect 1:1 match between citations and bib entries.

### 1.2 Bib Entry Completeness

All 28 entries have title, author, year, and venue (booktitle/journal). Issues:

| Entry | Issue | Severity |
|-------|-------|----------|
| `xu2025cruxevalx` | Author field: "Ruiyang Xu and others" (truncated) | Minor |
| `spiess2025calibration` | Author field: "Claudio Spiess and David Gros and others" (truncated) | Minor |
| `foster2025mutation` | Author field: "Christopher Foster and others" (truncated) | Minor |
| `appt2024` | Missing pages field (TSE journal) | Minor |
| `zhou2024llm4patch` | Missing pages field (TSE journal) | Minor |
| `eguchi2025etcot` | Missing URL (workshop paper, no preprint link) | Minor |
| `widyasari2024fusefl` | Missing URL/DOI/pages | Minor |
| `yadavally2024ndslicer` | Missing URL/DOI/pages | Minor |

### 1.3 Bib Key Naming Issues (non-functional)

- `ferrando2025execute`: First author is Armengol-Estape, not Ferrando. Key is misleading but does not affect compilation.
- `qwen2025coder`: Entry has `year={2024}` but key says "2025". ArXiv paper is from Sept 2024. No functional impact.

---

## 2. Data Consistency

### 2.1 VOTA_no_ae Accuracy: 99.41% vs Registry 99.40%

The task flags that the registry value is 99.40% (from 99.405% raw). The paper consistently uses **99.41%** in all locations:
- Table 1 (experiments.tex): 99.41%§
- Table 2 (experiments.tex): 99.41%
- Text (experiments.tex line 93): "VOTA_no_ae = VOTA = 99.41%"
- Table full_qwen (appendix.tex): 99.41

**Assessment**: 99.405 → 99.41% is correct under round-half-up convention. If the registry uses round-half-even (banker's rounding), 99.405 → 99.40%. **Recommend verifying the raw value and picking one convention consistently.** Paper is internally consistent at 99.41%.

### 2.2 Decimal Place Consistency

All tables use 2-decimal format consistently. However, the **abstract** and **conclusion** use 1-decimal "85.6%" for loop_only, while Table 2 reports "85.63%".

| Location | Value |
|----------|-------|
| Abstract | "85.6%" |
| Introduction (line 26) | "85.6%" |
| Conclusion (line 17) | "85.6%" |
| Table 2 (tab:ablation) | "85.63%" |

**Severity**: Low. Rounding in prose summaries is acceptable but introduces minor inconsistency.

### 2.3 All Other Numbers

Cross-checked all repeated values (99.83%, 99.33%, 91.09%, 84.45%, 14.96pp, 81.76%, 75.13%, 6.64pp, 93.61%, etc.) — all consistent across locations.

---

## 3. Cross-Reference Audit

### 3.1 Label/Ref Match

| Check | Count |
|-------|-------|
| Labels defined | 33 |
| All \ref{} targets have matching \label{} | **Yes** |
| Dangling refs (ref without label) | **0** |

### 3.2 Orphaned Labels (defined but never referenced)

| Label | Location | Notes |
|-------|----------|-------|
| `sec:vota_examples` | appendix.tex:103 | Never \ref'd from any file |
| `sec:full_results` | appendix.tex:161 | Never \ref'd from any file |

**Severity**: Low. Appendix sections don't strictly need cross-references, but adding a pointer from the main text (e.g., "Full per-seed results in Appendix~\ref{sec:full_results}") would improve navigability.

### 3.3 Table/Figure Numbering

LaTeX auto-numbers; sequence is correct:
- Main text: Tables 1–3, Figures 1–2
- Appendix: Tables 4–14, Figures 3–4

No gaps or duplicates.

---

## 4. ARR Compliance

| Requirement | Status |
|-------------|--------|
| `[review]` mode (anonymous) | PASS — `\usepackage[review]{acl}` |
| Author anonymized | PASS — "Anonymous ACL submission" |
| Limitations section | PASS — comprehensive, 6 limitations |
| Ethics Statement | PASS — public data, no human subjects, minimal compute |
| No de-anonymization leaks | PASS — no GitHub URLs, author names, lab names, or affiliations |
| ARR checklist (arr_checklist.tex) | PASS — all sections A–F complete |
| Code/data release language | PASS — "upon acceptance" phrasing |

---

## 5. Format Issues

### 5.1 Table Caption Placement (CRITICAL)

**ACL style requires table captions ABOVE the table body.**

| File | Tables | Caption Position | Correct? |
|------|--------|-----------------|----------|
| experiments.tex | Tables 1, 2, 3 | **Below** (`\caption` after `\end{tabular}`) | NO |
| appendix.tex | Tables 4–14 | Above (`\caption` before `\begin{tabular}`) | YES |

**Fix required**: Move `\caption{...}\label{...}` to before `\begin{tabular}` in experiments.tex for all three tables.

### 5.2 Figure Caption Placement

All figures have captions below — correct per convention. PASS.

### 5.3 Condition Name Formatting Inconsistency

| Condition | Canonical Form | Deviant Form | Location |
|-----------|---------------|--------------|----------|
| VOTA_no_ae | `\texttt{VOTA\_no\_ae}` | `VOTA$-$AE` | appendix.tex per_class table (line 22) |
| full_trace_label_only | `\texttt{full\_trace\_label\_only}` | `label\_only` (no \texttt{}) | experiments.tex Table 3 |
| full_trace_label_only | `\texttt{full\_trace\_label\_only}` | `Full Trace (LO)` | appendix.tex per_class table (line 17) |

### 5.4 Appendix Label Format

All appendix labels use consistent `sec:snake_case` / `tab:snake_case` / `fig:snake_case` format. PASS.

---

## 6. Critical Issues (Must Fix)

1. **Table caption placement in experiments.tex** — Tables 1–3 have captions below the table body. ACL requires captions above. Move `\caption` + `\label` before `\begin{tabular}` for each.

## 7. Recommended Fixes (Should Fix)

2. **VOTA_no_ae naming in per_class table** — Change "VOTA$-$AE" to `\texttt{VOTA\_no\_ae}` for consistency (appendix.tex line 22).
3. **label_only naming in Table 3** — Add `\texttt{}` around `label\_only` in experiments.tex Table 3.
4. **"Full Trace (LO)" in per_class table** — Standardize to `\texttt{full\_trace\_label\_only}` or at minimum `\texttt{label\_only}` (appendix.tex line 17).
5. **85.6% vs 85.63%** — Either use 85.63% everywhere, or add "(rounded)" qualification in abstract/conclusion.

## 8. Optional Improvements

6. Add cross-references to orphaned appendix sections (`sec:vota_examples`, `sec:full_results`).
7. Complete truncated author lists in bib entries (xu2025cruxevalx, spiess2025calibration, foster2025mutation).
8. Add pages field to journal entries (appt2024, zhou2024llm4patch).
9. Add URL/DOI to widyasari2024fusefl and yadavally2024ndslicer.
10. Verify VOTA_no_ae raw value rounding convention (99.405 → 99.41% or 99.40%).
