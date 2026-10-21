# Camera-Ready Format Pre-Check Report

**Target:** EMNLP 2026 Findings (via ARR May 2025 submission)  
**Date:** 2026-05-17  
**Paper:** `docs/paper/main.tex`  
**Status:** Review submission (not camera-ready yet)

---

## 1. ARR/EMNLP 2026 Format Requirements

### Page Limits
- Long paper: 8 pages content + unlimited references + unlimited appendix
- Limitations section: up to 1 page, does not count toward page limit
- **Status:** ⚠️ Cannot verify without compilation. Content volume (intro ~2pp, related work ~1.5pp, method ~2.5pp, experiments ~4pp, discussion ~1pp, conclusion ~0.25pp) suggests the paper may be at or over the 8-page limit. **Compile and verify.**

### Document Class and Style
| Check | Status | Details |
|-------|--------|---------|
| `\documentclass[11pt]{article}` | ✅ Pass | Correct per ACL requirements |
| `\usepackage[review]{acl}` | ✅ Pass | Enables line numbers + anonymization |
| Line numbers enabled | ✅ Pass | `review` option sets `\acl@linenumberstrue` |
| Anonymous submission | ✅ Pass | Author = "Anonymous ARR Submission" |
| No acknowledgements | ✅ Pass | No acknowledgements section present |
| Font (Times) | ✅ Pass | `\usepackage{times}` loaded |
| Style file source | ⚠️ Verify | `acl.sty` present but cannot confirm it matches the latest from github.com/acl-org/acl-style-files. An `acl2023.sty` also exists (unused). Recommend downloading latest from official repo and diffing. |

### Required Sections
| Section | Status |
|---------|--------|
| Limitations | ✅ Present, before references (correct placement per ARR) |
| Responsible NLP Checklist | ✅ Addressed in Appendix A (`app:checklist`) |
| Ethics statement | ✅ Covered within checklist (potential risks item) |

---

## 2. Figure/Table Caption Self-Containment

All captions reviewed for independence from main text:

| Location | Caption Summary | Status |
|----------|----------------|--------|
| `method.tex:26` Tab 1 (Models) | ✅ Self-contained, defines all abbreviations |
| `experiments.tex:30` Tab 2 (Layer selection) | ✅ Footnotes explain all abbreviations |
| `experiments.tex:55` Tab 3 (HS vs text) | ✅ All metrics defined in caption |
| `experiments.tex:78` Fig 2 (Temporal window) | ✅ Self-contained with key numbers |
| `experiments.tex:103` Tab 4 (32B divergence) | ✅ Concise and independent |
| `experiments.tex:133` Tab 5 (Negative results) | ✅ Footnotes clarify each method |
| Appendix tables (6 total) | ✅ All self-contained |
| `appendix.tex:386` Fig (Pareto) | ✅ Self-contained |

**No undefined abbreviations found in captions.**

---

## 3. References (references.bib) Format Audit

### Entry Type Errors

❌ **`tenney2019bert` (line 151):** Uses `@article` with `journal` field, but this is a conference paper (ACL 2019). Should be:
```bibtex
@inproceedings{tenney2019bert,
  ...
  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  ...
}
```

❌ **`alain2017understanding` (line 244):** Uses `@article` with `journal = {Workshop track, International Conference on Learning Representations (ICLR)}`. Should be `@inproceedings` with `booktitle`, or `@misc`/`@inproceedings` with a workshop proceedings format.

### Venue Name Consistency

| Venue | Format Used | Consistent? |
|-------|-------------|-------------|
| NeurIPS | "Advances in Neural Information Processing Systems N (NeurIPS)" | ✅ Yes (4 entries) |
| ACL | "Proceedings of the Nth Annual Meeting of the Association for Computational Linguistics (ACL)" | ✅ Yes |
| EMNLP | "Proceedings of the YYYY Conference on Empirical Methods..." / "Findings of..." | ✅ Yes |
| ICML | "Proceedings of the Nth International Conference on Machine Learning (ICML)" | ✅ Yes |
| ICLR | "Proceedings of the International Conference on Learning Representations (ICLR)" | ✅ Yes (no edition number, but consistent across entries) |

### Year Format
✅ All entries use 4-digit years consistently.

### Empty/Missing Fields
✅ No empty fields detected. All entries have title, author, year, and URL.

### arXiv Preprints
⚠️ 14 of 31 entries are arXiv preprints (`@article` with `journal = {arXiv preprint arXiv:...}`). This is acceptable for a review submission but check whether any have been published at venues since upload (especially 2025-2026 preprints that may now have proceedings versions).

---

## 4. Residual Content Check

| Check | Status | Details |
|-------|--------|---------|
| TODO/FIXME | ✅ Clean | No occurrences in paper content (only in `acl_natbib.bst` template, acceptable) |
| `??` (undefined refs) | ✅ Clean | No occurrences |
| "undefined" text | ✅ Clean | Only LaTeX internal in .aux file |
| Commented-out blocks | ✅ Clean | No large commented-out sections |
| Em-dash (U+2014) | ✅ Clean | Zero occurrences in all section files |
| En-dash (U+2013) | ✅ Clean | Zero occurrences (number ranges use `--` correctly) |
| Unused figures | ⚠️ Note | `figures/fig3_model_dependency.pdf` and `.png` exist but are not referenced by any `\includegraphics` command |

---

## 5. Cross-Reference Integrity

✅ All `\cref{}` targets have matching `\label{}` definitions. Verified labels:
- 6 section labels in main text
- 5 subsection labels
- 5 table labels in main text
- 1 figure label in main text
- 12 appendix labels (sections + tables + figures)

⚠️ Minor inconsistency: `\label{sec:oracle}` in appendix uses `sec:` prefix instead of `app:` convention used by other appendix sections. Functional but inconsistent.

---

## Summary

### ❌ Must Fix (2 items)
1. **`tenney2019bert` bib entry type** (`references.bib:151`): Change `@article` to `@inproceedings`, rename `journal` to `booktitle`.
2. **`alain2017understanding` bib entry type** (`references.bib:244`): Change `@article` to `@inproceedings`, rename `journal` to `booktitle`.

### ⚠️ Should Verify (5 items)
1. **Page count**: Compile and verify main content fits within 8 pages. The volume of content (especially experiments + discussion) may exceed the limit.
2. **acl.sty version**: Confirm `acl.sty` matches the latest official ACL style file from https://github.com/acl-org/acl-style-files. The co-existing `acl2023.sty` suggests potential staleness.
3. **arXiv preprint updates**: Check if any of the 14 arXiv-only references now have published proceedings versions (especially: `trajguard`, `saferemind`, `safethink`, `safedream2026`, `hu2026refusal_dynamics`).
4. **Unused figure files**: `fig3_model_dependency.pdf/png` in figures directory are not referenced. Remove if unneeded to avoid submission bloat.
5. **Label naming**: `sec:oracle` in appendix breaks the `app:` naming convention. Low priority.

### ✅ Passing (all other items)
- Document class and review options correct
- Anonymization in place
- Line numbers enabled
- Limitations section present and correctly placed
- Responsible NLP Checklist addressed
- No residual TODO/FIXME/undefined references
- No AI-style dashes
- All captions self-contained
- All cross-references resolve
- Venue name formatting consistent in bib
- All referenced figures exist

---

*Generated by format pre-check audit. No files were modified.*
