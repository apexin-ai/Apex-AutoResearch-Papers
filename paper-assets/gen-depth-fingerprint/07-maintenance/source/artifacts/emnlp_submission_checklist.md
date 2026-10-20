# EMNLP 2026 ARR Submission Pre-flight Checklist

**Paper**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains  
**Date**: 2026-05-16  
**Paper directory**: `artifacts/_project/paper/`

---

## 1. Anonymization

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1.1 | Author field | ✅ | `\author{Anonymous}` in `main.tex:15` |
| 1.2 | No institutional affiliations | ✅ | None found |
| 1.3 | No acknowledgments section | ✅ | Absent (correct for review) |
| 1.4 | No GitHub/GitLab/personal URLs | ✅ | No repository or personal URLs in any .tex |
| 1.5 | No funding/grant info | ✅ | None found |
| 1.6 | Conclusion release statement | ✅ | `conclusion.tex:11` says "will be released upon publication" — no URL provided, safe |
| 1.7 | PDF metadata | ⚠️ | **No compiled PDF found in paper directory. Compile and verify `pdfinfo` shows no author/creator metadata before submission.** |
| 1.8 | `_backup/` directory | ❌ | `artifacts/_project/paper/_backup/` contains 24 old .tex files (some with `\cite{placeholder}`). **Must exclude from submission package.** |

---

## 2. Page Count (8-page limit, excl. references + appendix)

Main body line counts (source lines, not formatted):

| Section | Lines | Tables | Figures |
|---------|-------|--------|---------|
| Abstract | 8 | 0 | 0 |
| Introduction | 42 | 0 | 0 |
| Related Work | 60 | 0 | 0 |
| Method | 95 | 0 | 0 |
| Results | 196 | 4 (+ table4.tex = 5) | 2 |
| Discussion | 86 | 0 | 0 |
| Conclusion | 11 | 0 | 0 |
| **Total** | **498** | **5** | **2** |

Not counted toward limit: Limitations (29 lines), Ethics (8 lines), References, Appendix (8 sections, 272 lines).

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 2.1 | Main body ≤ 8 pages | ⚠️ | **Estimated 7–9 pages. With 498 source lines + 5 tables + 2 figures in ACL two-column format, this is borderline. Must compile to verify.** Discussion section is substantial (86 lines, ~12 paragraphs). If over limit, Discussion is the primary candidate for trimming. |

---

## 3. Required Sections

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 3.1 | Abstract | ✅ | `abstract.tex`, included via `\input` |
| 3.2 | Introduction | ✅ | `introduction.tex`, `\section{Introduction}` |
| 3.3 | Related Work | ✅ | `related_work.tex`, `\section{Related Work}` |
| 3.4 | Method | ✅ | `method.tex`, `\section{Method}` |
| 3.5 | Results/Experiments | ✅ | `results.tex`, `\section{Results}` |
| 3.6 | Discussion | ✅ | `discussion.tex`, `\section{Discussion}` |
| 3.7 | Conclusion | ✅ | `conclusion.tex`, `\section{Conclusion}` |
| 3.8 | Limitations | ✅ | `limitations.tex`, `\section*{Limitations}` (unnumbered, correct) |
| 3.9 | Ethics Statement | ✅ | `ethics.tex`, `\section*{Ethics Statement}` (unnumbered, correct) |

---

## 4. References

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 4.1 | .bib file exists | ✅ | `references.bib` — 50 entries |
| 4.2 | All `\cite{}` keys defined in .bib | ✅ | 50 unique cited keys, all present in .bib (diff is empty) |
| 4.3 | All .bib entries cited | ✅ | 50 bib entries, all cited (no orphan entries) |
| 4.4 | No `\cite{placeholder}` in main files | ✅ | Only in `_backup/` (excluded from compilation) |
| 4.5 | Bib entry completeness | ⚠️ | Some entries lack page numbers or DOIs (e.g., `stamatatos_survey`, `koppel_authorship`, `aaronson_watermark`). Acceptable for ARR but recommend filling in for camera-ready. |

---

## 5. Figures and Tables

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 5.1 | Figure files exist | ✅ | `fig1_differential_response.pdf` ✅, `fig3_baseline_comparison.png` ✅ (both in `../chart/`) |
| 5.2 | `\graphicspath` correct | ✅ | `main.tex:11`: `\graphicspath{{../chart/}}` |
| 5.3 | Unused figure files | ⚠️ | `fig2_logo_performance.png`, `fig4_downstream_negative.pdf/.png` exist in `chart/` but are not referenced. Clean up before submission to reduce package size. |
| 5.4 | All `\ref{}` targets defined | ✅ | All cross-references (sections, tables, figures, appendices) have matching `\label{}` definitions |

---

## 6. Appendix / Supplementary Materials

8 appendix sections in `main.tex`, ordered:

| # | Appendix | Label | File |
|---|----------|-------|------|
| A | Length Confound Analysis | `app:length` | `appendix_length.tex` |
| B | Prompt Type Generalization | `app:prompt-type` | `appendix_prompt_type.tex` |
| C | Finer-Grained Depth Classification | `app:finer-depth` | `appendix_finer_depth.tex` |
| D | End-to-End Depth Classification (QLoRA) | `app:qlora` | `appendix_qlora.tex` |
| E | Leave-One-Feature-Out Analysis | `app:lofo` | `appendix_lofo.tex` |
| F | Confusion Matrix | `app:confusion` | `appendix_confusion_matrix.tex` |
| G | Classifier Sensitivity | `app:classifier` | `appendix_classifier.tex` |
| H | Human-Edit Robustness | `app:human-edit` | `appendix_human_edit.tex` |

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 6.1 | All appendix files exist | ✅ | All 8 files present |
| 6.2 | Sampling Sensitivity sub-section | ⚠️ | `app:sampling-sensitivity` is a `\subsection*` inside Appendix G (`appendix_classifier.tex:32`). The label resolves to the parent section. Cross-refs from `discussion.tex:9` and `limitations.tex:27` will point to Appendix G, not the subsection header. Consider promoting to its own appendix section if precise cross-referencing is needed. |

---

## 7. ACL/EMNLP Format

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 7.1 | Document class | ✅ | `\documentclass[11pt]{article}` |
| 7.2 | ACL style package | ✅ | `\usepackage[review]{acl}` — review mode enables anonymization + line numbers |
| 7.3 | Bibliography style | ✅ | `\bibliography{references}` — `acl.sty` sets `acl_natbib` style automatically |
| 7.4 | Required packages | ✅ | `times`, `latexsym`, `graphicx`, `booktabs`, `amsmath` all loaded |
| 7.5 | `acl.sty` in submission | ⚠️ | **Verify `acl.sty` (2023 version) is included in the submission directory or available. Not found in the paper directory — must be added.** |

---

## 8. Summary

| Category | ✅ Pass | ❌ Fail | ⚠️ Verify |
|----------|---------|---------|-----------|
| Anonymization | 6 | 1 | 1 |
| Page count | — | — | 1 |
| Required sections | 9 | 0 | 0 |
| References | 4 | 0 | 1 |
| Figures/Tables | 2 | 0 | 2 |
| Appendix | 1 | 0 | 1 |
| Format | 4 | 0 | 1 |
| **Total** | **26** | **1** | **6** |

### Action Items (must fix)

1. **❌ Remove `_backup/` directory** from submission package (`paper/_backup/` — 24 stale .tex files, some containing `\cite{placeholder}`)

### Action Items (verify before submission)

1. **⚠️ Compile PDF and check page count** — estimated 7–9 pages, must be ≤ 8. If over, trim Discussion (86 lines, most expendable).
2. **⚠️ Check PDF metadata** after compilation — ensure no author/creator info leaks via `pdfinfo`.
3. **⚠️ Include `acl.sty`** — the ACL 2023 style file must be present in the submission directory.
4. **⚠️ Clean up unused figures** — `fig2_logo_performance.png`, `fig4_downstream_negative.*` in `chart/`.
5. **⚠️ `app:sampling-sensitivity` cross-ref precision** — currently a `\subsection*` inside Appendix G; consider promoting to its own appendix.
6. **⚠️ Fill missing bib metadata** for camera-ready (page numbers, DOIs for some entries).
