# ACL Official Template Alignment Report

Date: 2026-05-25

## (a) Differences Found

### Style Files

| File | Result |
|------|--------|
| `acl.sty` | **Identical** to official (diff: 0 lines) |
| `acl_natbib.bst` | **Identical** to official (diff: 0 lines) |
| `acl_latex.tex` | **Identical** to official template (present in repo as reference) |

### Preamble (`main.tex` vs official `acl_latex.tex`)

| # | Item | Our `main.tex` | Official Template | Status |
|---|------|----------------|-------------------|--------|
| 1 | `\documentclass` | `[11pt]{article}` | `[11pt]{article}` | Match |
| 2 | `\usepackage[review]{acl}` | Present | Present | Match |
| 3 | `\usepackage{times}` | Present | Present | Match |
| 4 | `\usepackage{latexsym}` | Present | Present | Match |
| 5 | `\usepackage[T1]{fontenc}` | Present | Present | Match |
| 6 | `\usepackage[utf8]{inputenc}` | Present | Present | Match |
| 7 | `\usepackage{microtype}` | Present | Present | Match |
| 8 | `\usepackage{inconsolata}` | **Missing** | Present | See (b)#1 |
| 9 | `\usepackage{graphicx}` | Present | Present | Match |
| 10 | `\usepackage{booktabs}` | Present | Not in template | See (b)#2 |
| 11 | `\usepackage{amsmath}` | Present | Not in template | See (b)#2 |
| 12 | `\usepackage{amssymb}` | Present | Not in template | See (b)#2 |
| 13 | `\usepackage{multirow}` | Present | Not in template | See (b)#2 |
| 14 | `\usepackage{xcolor}` | **Was present (redundant)** | Not in template (loaded by `acl.sty` line 33) | **Fixed** |
| 15 | `\usepackage{subcaption}` | Present | Not in template | See (b)#2 |

### Other Structural Elements

| Item | Our Paper | Official Template | Status |
|------|-----------|-------------------|--------|
| `\author` format | `Anonymous ACL submission` | Template shows full author block; `acl.sty` auto-anonymizes in review mode | OK for review |
| `\begin{abstract}` | Via `\input{abstract}` | Inline | Equivalent |
| `\bibliographystyle` | Set by `acl.sty` to `acl_natbib` | Same | Match |
| `\bibliography` | `{references}` | `{custom}` | OK (different bib filename) |
| `\section*{Limitations}` | Present, before `\bibliography` | Present, before bibliography | Match |
| Appendix structure | `\appendix` then `\section{...}` | Same | Match |

## (b) Fixes Applied

### Fix 1: `inconsolata` package
- **Decision**: Not added
- **Reason**: `inconsolata.sty` is not installed on the build system. The official template states: "This is also not strictly necessary, and may be commented out." It only affects typewriter font (`\texttt{}`) aesthetics, which is cosmetic.

### Fix 2: Extra packages (`booktabs`, `amsmath`, `amssymb`, `multirow`, `subcaption`)
- **Decision**: Kept
- **Reason**: All are required by our paper content (tables with `\toprule`/`\midrule`/`\bottomrule`, math symbols like `\checkmark` and `\mathbf`, multirow table cells, subfigures). The official template explicitly allows additional packages.

### Fix 3: Redundant `\usepackage{xcolor}` (APPLIED)
- **Decision**: Removed
- **Reason**: `acl.sty` already loads `xcolor` at line 33 (`\usepackage{xcolor}`). Double-loading is redundant and can cause option clashes if different options are ever specified.

### Fix 4: Conclusion text trimmed for page limit (APPLIED)
- **Decision**: Compressed conclusion from 3 sentences to 2 sentences
- **Changes**:
  - Sentence 1: "consistent with" → "indicating" (minor wording)
  - Sentence 2: Compressed em-dash parenthetical, removed redundant words
  - Sentence 3 (future work): Removed entirely — the limitations section already covers needed future directions (diverse language pairs, alternative intervention methods)
- **Reason**: Main text (sections 1-6) overflowed page 8 by ~5 lines. After trimming, conclusion ends exactly at bottom of page 8.

## (c) Page Count

### Final Compilation Result
- **Total PDF pages**: 12
- **Main text (sections 1-6)**: Pages 1-8 (exactly 8 pages)
- **Limitations**: Page 9 (left column) — does not count toward limit per EMNLP 2026 rules
- **References**: Pages 9-11 — unlimited per EMNLP 2026 rules
- **Appendix**: Pages 11-12 — does not count toward limit

### Compliance
- EMNLP 2026 long paper limit: **8 pages** main text
- Current main text: **8 pages** (exact fit)
- Status: **COMPLIANT**

### Compilation Quality
- Errors: 0
- Overfull hbox: 2 (both in appendix tables, negligible: 4.5pt and 1.8pt)
- Underfull warnings: 17 (normal for two-column layout)
