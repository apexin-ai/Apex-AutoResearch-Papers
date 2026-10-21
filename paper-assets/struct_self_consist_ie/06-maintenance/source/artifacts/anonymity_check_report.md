## Anonymity Check Report

**Date:** 2026-05-23
**Paper:** "When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap"
**Target venue:** EMNLP 2026 (ARR submission)

---

### Review Mode Configuration

- [x] **review option:** `\usepackage[review]{acl}` — enabled (main.tex:3)
- [x] **author block:** `\author{Anonymous}` — properly anonymized (main.tex:30)
- [x] **`\aclfinalcopy`:** not present — correct for review submission
- [x] **acknowledgments:** no acknowledgments section exists — safe

---

### Identity Leaks Found

| File | Line | Content | Severity | Fix |
|------|------|---------|----------|-----|
| `figures/gen_fig_overview.py` | 298 | Hardcoded absolute path `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/...` | MEDIUM | **Fixed** — replaced with `os.path.dirname(os.path.abspath(__file__))` |
| `figures/_gen_n_scaling.py` | 55 | Hardcoded absolute path `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/...` | MEDIUM | **Fixed** — replaced with `os.path.join(os.path.dirname(...))` |
| `main.fls` | 1 | `PWD /home/ubuntu/.agent-ml-research-idea_gen_0514_1/...` | LOW | Auto-generated LaTeX auxiliary file; exclude from submission (not included in PDF) |

---

### Clean (No Issues)

- **Email addresses in .tex files:** none found
- **GitHub URLs in .tex files:** none (only standard ACL style file reference in `acl.sty`)
- **University/institution names in author context:** none (mentions in .tex are dataset examples, e.g., "University of Notre Dame" as a NER entity)
- **Grant/funding mentions:** none
- **ArXiv self-citations:** none
- **Self-referencing in references.bib:** no `note` fields, no "our work" markers
- **Chinese name patterns in author context:** none
- **qq.com / 163.com / gmail.com addresses:** none
- **`_gen_fig_bound.py`:** clean, no paths or identity info
- **All 17 .tex section files:** no identity leaks detected

---

### Summary

Paper is **anonymization-safe** for ARR submission. Two hardcoded paths in figure generation scripts were found and fixed. The `main.fls` file is auto-generated and should not be included in any submission package.
