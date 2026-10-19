# CoRL 2026 Submission Checklist

**Paper:** How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation
**Deadline:** 2026-05-29 (Full Paper), Abstract was 2026-05-25
**Platform:** OpenReview (https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)
**Conference:** Nov 9-12, 2026, Austin, TX

---

## Main PDF

| Requirement | Status | Notes |
|---|---|---|
| Page limit: 8 pages main text | ⚠️ | **Overflows by ~2 lines** — Limitations section last sentence spills onto page 9. Must trim before submission. |
| Limitations section (within 8 pages) | ✅ | `\section{Limitations}` on page 8 (discussion.tex:20). Content overflows slightly. |
| Template: `\usepackage{corl_2026}` | ✅ | Submission mode (no `final` flag). main.tex:4 |
| Anonymous submission | ✅ | "Anonymous Authors" in main.tex:19, "Anonymous Submission" in PDF metadata |
| Appendix at end of same PDF | ✅ | Pages 11-18 (8 pages), 12 appendix sections |
| References | ✅ | Pages 9-10 (2 pages), references.bib exists |
| PDF file | ✅ | `main.pdf` — 925 KB, 18 pages total, compiled 2026-05-28 22:25 UTC |
| paper_switch.py verify | ✅ | All 21 replacement anchors match for both Scenario B and C |

### Page breakdown
- Pages 1-8: Main text (Introduction, Related Work, Method, Claims 1-3, Discussion, Limitations)
- Pages 9-10: References
- Pages 11-18: Appendix (8 pages)

---

## Supplementary Materials (OpenReview: single zip)

| Requirement | Status | Notes |
|---|---|---|
| Supplementary zip | ❌ Not prepared | Optional. Zip with code/extra material uploaded to OpenReview. |
| Code | ❌ Not linked | No anonymous code link in paper. Consider anonymous GitHub/zip. |
| Data | ❌ Not linked | SafeLIBERO is public; custom SDF data not released. |

---

## Video (Optional, External)

| Requirement | Status | Notes |
|---|---|---|
| Video (max 250MB, ~3 min) | ❌ Not prepared | PMLR disallows video in supplementary; must host externally (YouTube). Optional but encouraged. |

---

## OpenReview Form Fields

| Requirement | Status | Notes |
|---|---|---|
| Abstract text | ❓ To fill | Copy from abstract.tex |
| Keywords | ❓ To fill | "VLA safety, collision avoidance, action collapse, signed distance fields" (from main.tex:28) |
| Generative AI disclosure | ❓ To fill | Required — briefly describe LLM usage for research/writing |
| Reviewer registration | ❓ To verify | Required if any author has 3+ submissions to CoRL 2026 |
| Dual submission check | ✅ | Not submitted elsewhere (confirm with co-authors) |

---

## Critical Action Items

1. **🔴 FIX PAGE OVERFLOW** — Trim ~2 lines from main text (Limitations section overflows page 8). Options:
   - Tighten Limitations wording
   - Reduce spacing elsewhere in the paper
   - Use `\vspace{-Xpt}` sparingly

2. **🟡 Recompile PDF** after fixing overflow

3. **🟡 Supplementary zip** (optional) — If submitting code, create anonymous zip

4. **🟡 Fill OpenReview form** — Abstract, keywords, AI disclosure, author info

---

## Files in this directory

- `main.pdf` — Complete paper (main + references + appendix), ready for upload after page fix

## Source references

- Paper source: `docs/paper/` (main.tex + section .tex files)
- Figures: `artifacts/figures/` (fig1_teaser, fig2_displacement, fig3_scatter, fig5_lambda_curve, fig_overview, fig_oracle_bar, etc.)
- Style: `docs/paper/corl_2026.sty`
- Bibliography: `docs/paper/references.bib`
- paper_switch.py: `artifacts/paper_switch.py`
