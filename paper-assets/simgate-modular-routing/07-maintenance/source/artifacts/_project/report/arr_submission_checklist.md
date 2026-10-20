# ARR/EMNLP 2026 Submission Compliance Checklist

**Paper:** Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld  
**Target:** EMNLP 2026 via ACL Rolling Review  
**DDL:** 2026-05-25  
**Checked:** 2026-05-17  

---

## Part 1: Format Compliance

### Anonymization
| Item | Status | Notes |
|------|--------|-------|
| `\usepackage[review]{acl}` | ✅ | Line 3 of main.tex |
| `\author{Anonymous}` | ✅ | Line 20 of main.tex |
| No self-identifying citations | ✅ | Grep found no "our previous/earlier work" patterns |
| PDF Author metadata empty | ✅ | `pdfinfo` shows Author field blank |
| PDF Title metadata empty | ✅ | No identifying info in PDF properties |
| No Acknowledgments section | ✅ | Correctly omitted for review version |
| No tracked links (Dropbox etc.) | ✅ | No such links found |

### Page Limits (Long Paper: 8 pages content)
| Item | Status | Notes |
|------|--------|-------|
| Content pages (Sec 1-6) | ✅ | Fits within 8 pages (Conclusion ends on page 8) |
| Limitations section | ✅ | Present, starts on page 8 (does not count toward limit) |
| Ethics Statement | ✅ | Present on page 9 (does not count toward limit) |
| References | ✅ | Pages 9-10 (does not count toward limit) |
| Appendix | ✅ | Pages 10-15 (does not count toward limit, double-column format) |

### Template & Formatting
| Item | Status | Notes |
|------|--------|-------|
| Official ACL style file | ✅ | `acl.sty` from `github.com/acl-org/acl-style-files/` (line 2-4 of acl.sty) |
| Paper size (A4) | ✅ | Official `acl.sty` sets `a4paper` (line 103 of acl.sty) |
| Margins (2.5cm) | ✅ | Set by `acl.sty` geometry options |
| Font size (11pt) | ✅ | `\documentclass[11pt]{article}` |
| Line numbers enabled | ✅ | `[review]` option enables line numbers automatically |
| Page numbers enabled | ✅ | `[review]` option enables page numbers |
| Two-column format | ✅ | Set by `acl.sty` |
| Appendix double-column | ✅ | Verified in PDF pages 10-15 |

### Required Packages
| Item | Status | Notes |
|------|--------|-------|
| times font | ✅ | `\usepackage{times}` |
| T1 fontenc | ✅ | `\usepackage[T1]{fontenc}` |
| utf8 inputenc | ✅ | `\usepackage[utf8]{inputenc}` |
| microtype | ✅ | `\usepackage{microtype}` |

---

## Part 2: Required Sections

| Section | Status | Notes |
|---------|--------|-------|
| Abstract | ✅ | Present (abstract.tex) |
| Limitations | ✅ | Dedicated section in main.tex (after Conclusion, before References) |
| Ethics Statement | ✅ | Present in main.tex |
| Responsible NLP Checklist | ❌→✅ | **Created:** `responsibleNLPchecklist.tex` (see Part 3) |

### Action Required: Include Checklist in Paper
The checklist file has been created at `docs/paper/responsibleNLPchecklist.tex`. To include it in the paper, add the following line in `main.tex` **after** the appendix sections (before `\end{document}`):

```latex
\input{responsibleNLPchecklist}
```

---

## Part 3: Responsible NLP Research Checklist

| Question | Answer | Section Reference |
|----------|--------|-------------------|
| **A1** Limitations described? | Yes | Limitations section |
| **A2** Potential risks discussed? | Yes | Ethics Statement |
| **B1** Artifact creators cited? | Yes | Throughout (ScienceWorld, ALFWorld, MATH, models) |
| **B2** License/terms discussed? | **No** | ⚠️ Not explicitly stated |
| **B3** Consistent with intended use? | Yes (implicit) | Sec 2-3 |
| **B4** PII/offensive content checked? | N/A | Simulation data only |
| **B5** Artifact documentation? | Yes | Sec 2, Appendix C, E |
| **B6** Relevant statistics reported? | Yes | Tables 1-8, Sec 3 |
| **C1** Parameters/compute reported? | Partial | Ethics Statement (40 GPU-hrs); GPU model not named |
| **C2** Hyperparameters reported? | Yes | Table 6 (Appendix E) |
| **C3** Descriptive statistics reported? | Yes | CIs, mean±std throughout |
| **C4** Package settings reported? | Yes | vLLM, LoRA config in Table 6 |
| **D1-D5** Human annotators? | N/A | No human annotation |
| **E1** AI assistant use disclosed? | Yes | Stated in checklist |

---

## Part 4: Issues & Fixes

### Must Fix Before Submission

| # | Issue | Fix |
|---|-------|-----|
| 1 | Responsible NLP Checklist not included as appendix | Add `\input{responsibleNLPchecklist}` before `\end{document}` in main.tex. File created at `docs/paper/responsibleNLPchecklist.tex` |
| 2 | B2 (license/terms) not addressed | Add one sentence to Ethics Statement: "ScienceWorld, ALFWorld, and MATH are released under permissive open-source licenses (Apache 2.0 / MIT). All language models are publicly available." |
| 3 | C1 (GPU model) not fully specified | Add GPU model name to Ethics Statement, e.g., "on two NVIDIA RTX 3090 GPUs" (or actual GPU used) |

### Recommended (Not Required)

| # | Item | Notes |
|---|------|-------|
| 4 | Run `acl-pubcheck` | Validates formatting compliance automatically. Install: `pip install acl-pubcheck`, run: `python -m acl_pubcheck --paper main.pdf` |
| 5 | Preprint field on OpenReview | If paper is on arXiv, must declare in submission form |
| 6 | Supplementary materials | If submitting code/data as supplementary, package as anonymized .zip/.tgz |
| 7 | OpenReview profiles | All authors must have complete OpenReview profiles before submission |
| 8 | Reviewer assignment | Authors must register for reviewing within 48 hours of submission deadline |

---

## Summary

- **Compliance status:** 3 items to fix (all straightforward), 5 recommended actions
- **Critical:** Add the Responsible NLP Checklist as appendix before submission
- **Format:** Template, anonymization, page limits, line numbers all compliant
- **Content:** Limitations and Ethics sections present and substantive
