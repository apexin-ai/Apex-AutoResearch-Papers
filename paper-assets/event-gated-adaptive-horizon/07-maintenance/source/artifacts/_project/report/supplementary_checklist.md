# Supplementary Material Checklist

Generated: 2026-05-28

## 1. Code Repository

- [x] Supplementary code package exists (`artifacts/supplementary/code/`)
- [x] Full DreamerV3 codebase included (dreamer.py, models.py, networks.py, tools.py, exploration.py, parallel.py)
- [x] Environment wrappers included (dmc.py, maniskill.py, atari.py, crafter.py, etc.)
- [x] Config file included (`configs/configs.yaml`)
- [x] README.md with reproduction commands (trigger, frozen, ManiSkill examples)
- [x] requirements.txt with pinned versions
- [x] LICENSE file (MIT, "Anonymous Authors")
- [x] Analysis scripts included (`scripts/civo_detector.py`, gradient decomposition, NVE threshold analysis, bootstrap CIs)
- [x] Figure generation scripts included (`figures/fig2_nve_trajectory.py`, `fig6_collapse_pathways_d054.py`, `fig_style.py`)
- [x] Raw analysis data included (`analysis/` dir: gradient decomposition, bootstrap CIs, NVE threshold, etc.)
- [x] No author-identifying information in code (checked: no emails, no personal paths, no wandb project names)
- [ ] **Minor**: `code/envs/setup_scripts/minecraft.sh` references `github.com/NM512/minerl` -- this is the upstream DreamerV3 base repo (not author-identifying), but reviewer could question it. Consider noting in README that base code is from NM512/dreamerv3-torch.
- [ ] No standalone `artifacts/code/` README -- this directory has raw code files (models.py, networks.py, etc.) and CHANGES.md but no README. Only the `artifacts/supplementary/` package has a README.
- [ ] Supplementary package not yet zipped for upload (directory exists but no .zip archive)

## 2. Appendix Figures

All 16 `\includegraphics` references resolved successfully:

**Main text figures (3):**
- [x] `figures/paper/fig4_mechanism_diagram.pdf` (Introduction, Fig 1)
- [x] `figures/paper/fig1_learning_curves.pdf` (Results)
- [x] `figures/fig1_nve_trajectory.pdf` (Results)
- [x] `figures/paper/fig6_multiple_pathways.pdf` (Results)

**Appendix figures (12):**
- [x] `../../artifacts/figures/nve_roc_curve.pdf` (ROC curve, n=36)
- [x] `../../artifacts/figures/nve_threshold_prf.pdf` (Precision-Recall-F1 vs threshold)
- [x] `figures/paper/fig3_factorial_grid.pdf` (Factorial isolation)
- [x] `figures/paper/fig5_dt_amplification.pdf` (dt amplification)
- [x] `figures/paper/pairwise_heatmap.png` (Pairwise comparison)
- [x] `figures/value_vs_returns.pdf` (Value vs returns)
- [x] `figures/fig3_gradient_decomposition.pdf` (Gradient decomposition)
- [x] `figures/fig2_civo_decomposition.pdf` (CIVO decomposition)
- [x] `figures/fig4_entropy_dynamics.pdf` (Entropy dynamics)
- [x] `figures/dt_embedding_cosine_similarity.png` (dt embedding cosine sim)
- [x] `figures/paper/fig_temporal_ordering.pdf` (Temporal ordering)
- [x] `figures/actor_entropy_comparison.pdf` (Actor entropy comparison)

**Resolution paths:** Figures resolve via two mechanisms: (1) relative to `docs/paper/` (files in `docs/paper/figures/`), (2) via `\graphicspath{../../artifacts/}` (files in `artifacts/figures/`). All 16 figures confirmed present at their expected locations.

## 3. Supplementary Format

- [x] Appendix is part of main.tex (`\appendix\input{sections/appendix}` at line 78-79)
- [x] No external supplementary PDF referenced -- all appendix content is inline
- [x] CoRL 2026 format used (`corl_2026.sty`) -- CoRL allows unlimited appendix pages in main PDF
- [x] Paper compiles to 43 pages (main body + appendix + references)
- [x] No missing figure warnings in compilation log
- [x] No undefined references in compilation log
- [x] No undefined citations in compilation log
- [x] PDF metadata correct: Author="Anonymous Submission", Subject="Proceedings of the 10th Conference on Robot Learning (CoRL 2026)"
- [ ] Main body page count not verified against CoRL 2026 limit (typically 8+1 pages for main body; appendix unlimited). The 43-page total includes appendix -- need to verify main body alone fits within limit.

## 4. Submission Hygiene

- [x] No TODO/FIXME/XXX/HACK comments in any .tex files (all 8 section files + main.tex checked)
- [x] All 44 bib entries have title, year, and venue (booktitle or journal)
- [x] No severe overfull hbox warnings in compilation log
- [x] Anonymous authorship in main.tex ("Anonymous Authors, Anonymous Institution")
- [x] Keywords present: "World Models, Temporal Abstraction, Value Overestimation, DreamerV3"
- [x] All sections present: abstract, introduction, related_work, methodology, results, analysis, conclusion, appendix
- [x] Supplementary code anonymized (MIT License with "Anonymous Authors", no personal identifiers)
- [x] No wandb project names or API keys in supplementary code

## Missing Items (action required)

1. **Create supplementary .zip archive**: The supplementary materials exist as a directory (`artifacts/supplementary/`) but have not been packaged into a .zip file for upload. Run: `cd artifacts && zip -r supplementary.zip supplementary/`

2. **Verify main body page count**: The full PDF is 43 pages. CoRL typically allows 8 pages main + 1 page references + unlimited appendix. Need to confirm the main body (before `\appendix`) fits within the page limit. Check which page the appendix starts on.

3. **Consider noting NM512 base code**: The `minecraft.sh` script in supplementary references `github.com/NM512/minerl`. While this is the well-known upstream DreamerV3 repository (not author-identifying), the README should explicitly state the codebase is built on NM512/dreamerv3-torch to preempt reviewer questions about the reference.

4. **`artifacts/code/` has no README**: The raw code directory at `artifacts/code/` (separate from `artifacts/supplementary/code/`) lacks a README. This directory appears to be the working code, not the submission package. Confirm only `artifacts/supplementary/` is intended for submission.
