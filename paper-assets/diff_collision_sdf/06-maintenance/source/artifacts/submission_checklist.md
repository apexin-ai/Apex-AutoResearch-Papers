# CoRL 2026 OpenReview Submission Checklist

Generated: 2026-05-29

## Required Fields

| # | Field | Status | Details |
|---|-------|--------|---------|
| 1 | **Title** | ✅ Ready | "How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation" |
| 2 | **Abstract** | ✅ Ready | "Vision-Language-Action (VLA) models report high Collision Avoid..." (541 chars) |
| 3 | **Keywords** | ✅ Ready | VLA safety, collision avoidance, action collapse, signed distance fields |
| 4 | **TL;DR** | ✅ Ready | "99.6% of collision-free VLA episodes are frozen-robot artifacts; EE-only SDF refinement worsens safety by rotating unmonitored arm links into obstacles; collision-free demonstrations alone drive avoidance gains." (211 chars) |
| 5 | **Main PDF** | ✅ Ready | See Files section below |
| 6 | **Supplementary** | ✅ Ready | `artifacts/supplementary/supplementary.zip` — code archive with README, training/eval scripts, figure generation, analysis tools |
| 7 | **Author info** | ⏳ At submission | Enter real author names/emails/affiliations on OpenReview (not in PDF — double-blind) |
| 8 | **Conflicts of interest** | ⏳ At submission | Enter institutional and personal conflicts on OpenReview |
| 9 | **Reciprocal reviewing** | ⏳ At submission | At least one author must commit to reviewing; exempt if serving as AC/SAC/chair |

## Files

| File | Path | Status | Details |
|------|------|--------|---------|
| **Main PDF** | `docs/paper/main.pdf` | ✅ | md5: `36165c45ddaba8cb06df2dcf0113cac7`, 17 pages total (8 main + 1 refs + 8 appendix), 793 KB |
| **Supplementary ZIP** | `artifacts/supplementary/supplementary.zip` | ✅ | Code archive with README + training/eval/analysis/figure scripts |
| **Video** | — | ❌ Missing | No .mp4 found; CoRL strongly encourages ≤250 MB, ≤3 min overview video |
| **Code** | — | ❓ Not linked | No code URL in paper; consider anonymous GitHub/code supplement |

## Compliance

| # | Requirement | Status | Details |
|---|-------------|--------|---------|
| 1 | **Double-blind** | ✅ Pass | PDF author: "Anonymous Author(s)"; metadata: "Anonymous Submission"; no author names/affiliations/GitHub links found in .tex files |
| 2 | **Page limit (≤8 main)** | ✅ Pass | Main content (Introduction through Limitations) = exactly 8 pages |
| 3 | **Limitations section** | ✅ Present | Section 8 on page 8 — covers simulation-only scope, dfCAR assumptions, EE-only scope, seed count, statistical power |
| 4 | **Acknowledgments** | ⚠️ Not present | Not required for submission (add after acceptance); does not count toward page limit |
| 5 | **References** | ✅ Present | Page 9+; uses `references.bib` |
| 6 | **Appendix** | ✅ Present | Pages 10–17; does not count toward page limit |
| 7 | **LaTeX template** | ✅ Correct | Uses `\usepackage{corl_2026}` |
| 8 | **No dual submission** | ⏳ Self-certify | Must confirm paper is not under review elsewhere |
| 9 | **Footer** | ✅ Correct | "Submitted to the 10th Conference on Robot Learning (CoRL 2026). Do not distribute." |

## Action Items Before Submission

1. **Draft TL;DR** — e.g., "Over 99% of reported collision-free episodes in diffusion VLAs are action-collapse artifacts; EE-only SDF supervision provides no significant safety benefit beyond collision-free demonstrations."
2. **Prepare supplementary materials** — video demo, code archive, or supplementary PDF (single ZIP on OpenReview)
3. **Enter author info and conflicts** on OpenReview at submission time
4. **Confirm reciprocal review commitment** — at least one author must agree to review
5. **Confirm no dual submission** — verify paper is not submitted elsewhere

## Reference Links

- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 OpenReview Portal](https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)
