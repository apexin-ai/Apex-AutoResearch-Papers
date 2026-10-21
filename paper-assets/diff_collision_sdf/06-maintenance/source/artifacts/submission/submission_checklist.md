# CoRL 2026 Submission Checklist

**Paper:** How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation
**Deadline:** 2026-05-29 (Full Paper), Abstract was 2026-05-25
**Platform:** OpenReview (https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)
**Conference:** Nov 9-12, 2026, Austin, TX

---

## Main PDF

| Requirement | Status | Notes |
|---|---|---|
| Page limit: 8 pages main text | ✅ | Limitations ends on page 8 with 2-3 lines margin. |
| Limitations section (within 8 pages) | ✅ | `\section{Limitations}` on page 8 (discussion.tex). Fully contained. |
| Template: `\usepackage{corl_2026}` | ✅ | Submission mode (no `final` flag). main.tex:4 |
| Anonymous submission | ✅ | "Anonymous Authors" in main.tex:19, "Anonymous Submission" in PDF metadata |
| Appendix at end of same PDF | ✅ | Pages 10-17 (8 pages), 12 appendix sections |
| References | ✅ | Page 9, references.bib exists |
| PDF file | ✅ | `main.pdf` — 17 pages total, MD5: `36165c45ddaba8cb06df2dcf0113cac7` |
| paper_switch.py verify | ✅ | 19/19 replacement anchors match for both Scenario B and C |

### Page breakdown
- Pages 1-8: Main text (Introduction, Related Work, Method, Claims 1-3, Conclusion, Limitations)
- Page 9: References
- Pages 10-17: Appendix (8 pages)

---

## Supplementary Materials (OpenReview: single zip)

| Requirement | Status | Notes |
|---|---|---|
| Supplementary zip | ✅ | `artifacts/supplementary/supplementary.zip` — 76KB, 28 files |
| Code | ✅ | Included in zip: training, eval, analysis, figure scripts + README |
| Data | ✅ | README documents SafeLIBERO source + SDF ground truth format |

---

## Video (Optional, External)

| Requirement | Status | Notes |
|---|---|---|
| Video (max 250MB, ~3 min) | ❌ Not prepared | Optional. PMLR disallows video in supplementary; must host externally. |

---

## OpenReview Form Fields

| Requirement | Status | Notes |
|---|---|---|
| Abstract text | ✅ | Prepared in `openreview_fields.md` |
| Keywords | ✅ | "VLA safety, collision avoidance, action collapse, signed distance fields, evaluation metrics, robot manipulation, diffusion policy, safety benchmarks" |
| TL;DR | ✅ | 211 chars, covers 3 core findings |
| Generative AI disclosure | ✅ | Prepared in `openreview_fields.md` |
| Reviewer registration | ⏳ At submission | Confirm at least one author commits to reviewing |
| Dual submission check | ✅ | Not submitted elsewhere |

---

## Critical Action Items

1. ~~**🔴 FIX PAGE OVERFLOW**~~ ✅ Done — Limitations trimmed, page 8 ends with 2-3 lines margin
2. ~~**🟡 Recompile PDF**~~ ✅ Done — MD5: `36165c45ddaba8cb06df2dcf0113cac7`
3. ~~**🟡 Supplementary zip**~~ ✅ Done — 76KB, README + code archive
4. ~~**🟡 Fill OpenReview form**~~ ✅ Done — `openreview_fields.md` prepared with all fields

---

## Files in this directory

- `main.pdf` — Complete paper (main + references + appendix), ready for upload
- `openreview_fields.md` — Pre-filled OpenReview form fields

## Source references

- Paper source: `docs/paper/` (main.tex + section .tex files)
- Figures: `artifacts/figures/` (fig1_teaser, fig2_displacement, fig3_scatter, fig5_lambda_curve, fig_overview, fig_oracle_bar, etc.)
- Style: `docs/paper/corl_2026.sty`
- Bibliography: `docs/paper/references.bib`
- paper_switch.py: `artifacts/paper_switch.py`
- Supplementary: `artifacts/supplementary/supplementary.zip`
