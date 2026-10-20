# PDF Visual Check Report

**Date:** 2026-05-19
**File:** main.pdf (32 pages, 2.9 MB)

---

## 1. Compilation Results

| Metric | Count |
|--------|-------|
| Errors | 0 |
| Warnings | 9 |
| Undefined references | 0 |
| Overfull hboxes | 8 |
| Underfull hboxes | 217 |

---

## 2. Check Results

### a) Page Count and Structure

| Check | Result | Detail |
|-------|--------|--------|
| Main body ≤ 8 pages | **FAIL** | Conclusion (§6) starts at bottom of p.8 and overflows ~1 paragraph onto p.9 before Limitations begins |
| Limitations/Ethics placement | PASS | Limitations starts mid-p.9, Ethics on p.10 |
| References placement | PASS | Starts p.10 right column |
| Appendix placement | PASS | Starts p.13 (Appendix A) through p.32 (Appendix Z.2) |

**Page map (main body):**

| Page | Sections |
|------|----------|
| 1 | Abstract, §1 Introduction |
| 2 | §1 cont., §2 Related Work |
| 3 | §2 cont., §3 Method |
| 4 | §3 cont. |
| 5 | §3 cont., §4 Results |
| 6 | §4.1, §4.2, Table 1 |
| 7 | Figure 1, §4 cont. |
| 8 | Table 2, §4.3, §5 Discussion, §6 Conclusion (starts) |
| 9 | §6 Conclusion (OVERFLOW ~1 para), Limitations |
| 10 | Ethics, Compute, Software, References |
| 11-12 | References |
| 13-32 | Appendices A–Z.2 |

### b) Anonymization

| Check | Result | Detail |
|-------|--------|--------|
| \author field | PASS | "Anonymous ACL submission" |
| No author/institution names | PASS | None found in any .tex file |
| No deanonymization phrases | PASS | No "our previous work", personal URLs, etc. |
| No GitHub usernames | PASS | Only ACL style repo URL |

### c) Line Numbers

| Check | Result | Detail |
|-------|--------|--------|
| Review mode enabled | PASS | `\usepackage[review]{acl}` + `\linenumbers` |
| Visible in PDF | PASS | Line numbers visible on text pages |

### d) Figure Rendering

| Figure | Page | Result | Detail |
|--------|------|--------|--------|
| Fig 1 (strip plot) | 7 | PASS | DDR strip plot, legend readable, significance stars visible |
| Fig 2 (violin plots) | 15 | PASS | 7 subpanels, clear labels, p-values annotated |
| Fig 3 (confusion matrix) | 18 | PASS | Heatmap renders correctly |
| Fig 4 (per-gen LOGO) | 19 | PASS | Bar chart with error bars |
| Fig 5 (DDR trends) | 25 | PASS | Pooled mean + per-generator traces |
| Fig 6 (UMAP) | 25 | PASS | 2D projection renders correctly |
| Fig 8 (cross-temp F1) | 26 | PASS | Bar chart readable |
| Fig 9 (DDR scatter) | 28 | PASS | Scatter plot with labeled regions |
| Fig 10 (holdout split) | 29 | PASS | Scatter with markers and legend |
| Fig 11 (transfer heatmap) | 30 | PASS | 8×8 heatmap with annotations and color bar |
| Fig 12 (convergence dynamics) | 32 | PASS | Two panels, y-axis "Cohen's d (effect size)", correct |

All 12 referenced figure files exist in `../chart/`.

### e) Cross References

| Check | Result | Detail |
|-------|--------|--------|
| Broken "??" in PDF | PASS | None found |
| Undefined citations | PASS | No warnings in .log |
| Undefined labels | PASS | No warnings in .log |

### f) Tables

| Check | Result | Detail |
|-------|--------|--------|
| Table 1 (LOGO, p.6) | PASS | 8 generators, numbers aligned, columns clear |
| Table 2 (baselines, p.8) | PASS | Alignment correct, N/A entries present |
| Appendix tables (3–35) | PASS | All within margins, properly formatted |
| Font sizes | WARNING | Table 34 (p.31, 8×8 transfer matrix) uses borderline ~6pt font |

### g) Format Compliance

| Check | Result | Detail |
|-------|--------|--------|
| ACL 2023 format | PASS | Two-column layout correct |
| Font sizes | PASS | Body, headers, captions all standard |
| Page margins | PASS | Consistent throughout |
| Column spacing | PASS | Standard gap |
| Text overflow | WARNING | 3 appendix overfull hboxes >30pt (62.7pt in appendix_qlora, 43.6pt in appendix_tost, 36.0pt in appendix_instruct) — may cause visible margin bleed |

---

## 3. Issues Summary

### CRITICAL

1. **Page limit violation**: §6 Conclusion overflows from p.8 onto p.9 (~1 paragraph). EMNLP 2026 mandates main text ≤ 8 pages. Must cut/compress text to fit Conclusion entirely on p.8.

### WARNING

2. **Appendix overfull hboxes**: 3 cases >30pt in appendix files (appendix_qlora: 62.7pt, appendix_tost: 43.6pt, appendix_instruct: 36.0pt). Likely visible margin overflow in appendix. Cosmetic but unprofessional.
3. **Table 34 font size**: Borderline ~6pt in 8×8 transfer matrix (p.31). Legible but tight.

---

## 4. Overall Assessment

**NOT READY FOR SUBMISSION** — one critical issue must be fixed:

- The main body exceeds 8 pages (Conclusion spills onto p.9). Need to cut ~0.5–1 paragraph from the main body to pull Conclusion back onto p.8.

After fixing the page overflow, recommend also addressing the large overfull hboxes in appendix for polish. All other checks pass.
