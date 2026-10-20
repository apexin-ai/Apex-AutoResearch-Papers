# CoRL 2026 Submission Checklist

## OpenReview Required Fields

| Field | Status | Content/Notes |
|-------|--------|---------------|
| Title | Ready | Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis |
| Abstract | Ready | 5-sentence version (updated 2026-05-26), no inline numbers |
| Keywords | Ready | Vision-Language-Action models, Representational analysis, Instruction routing, Cross-architecture comparison, Fine-tuning analysis, Attention profiling, Action probing, Robotic manipulation |
| Author list | **PENDING** | Requires user confirmation |
| Main PDF | Ready | main.pdf, 40 pages (8 body + refs + appendix) |
| Supplementary | See below | CoRL allows appendix in main PDF |
| Conflicts of interest | **PENDING** | Requires user input |
| Code/data availability | N/A | "Code and data will be released upon acceptance" (§6) |

## Format Compliance

| Check | Status | Notes |
|-------|--------|-------|
| Template | PASS | `corl_2026.sty` (2026-01-10 revision by Y. Sung) |
| Body ≤ 8 pages | PASS | Conclusion ends on p.8, References start on p.9 |
| Anonymous submission | PASS | `\author{Anonymous}`, no de-anonymizing info |
| Font embedding | **WARNING** | All fonts embedded, but 23/25 figures contain Type 3 (bitmap) fonts from matplotlib DejaVu Sans. Fix: re-render all matplotlib figures with `plt.rcParams['pdf.fonttype'] = 42`. See "Type 3 Font Fix" below |
| Figure resolution | PASS | All figures are vector PDF (≥300 DPI equivalent) |
| References format | PASS | natbib with squared numbers per corl_2026.sty |
| Compilation | PASS | 0 errors, 0 undefined refs, 0 multiply-defined labels |

## Supplementary / Appendix

CoRL historically allows appendix pages after references in the main PDF (same as NeurIPS/ICML convention used by the template). No separate supplementary.zip required unless submitting code/data. Current setup (appendix after references in main.pdf) is compliant.

## Type 3 Font Fix (if required)

23 of 25 figure PDFs contain Type 3 bitmap fonts (DejaVu Sans from matplotlib). Only `fig_overview.pdf` and `fig_l1_attention.pdf` are clean.

**Fix**: Add to ALL matplotlib plotting scripts:
```python
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
```
Then re-run all scripts to regenerate figure PDFs. This converts Type 3 → TrueType (Type 42).

**Affected scripts** (need fonttype=42 added):
- plot_r2_collapse.py
- plot_counterfactual_bar.py
- plot_label_permutation.py
- plot_nlp_control_overlay.py
- plot_training_dynamics.py
- (plus ~18 other figures generated on remote server)

**Note**: Some conferences (IEEE) strictly reject Type 3; CoRL/NeurIPS-style venues typically accept them but Type 42 is best practice. Director decision needed on whether to fix before submission.

## Pre-Submission Actions

- [ ] User confirms OpenReview account + author list
- [ ] User confirms conflicts of interest
- [ ] (Optional) Fix Type 3 fonts in matplotlib figures
- [ ] User manually submits on OpenReview (Agent cannot access)
- [ ] Verify PDF renders correctly on OpenReview after upload

## Files to Submit

| File | Location | Purpose |
|------|----------|---------|
| main.pdf | docs/paper/main.pdf | Main submission (body + refs + appendix) |

## Deadlines

| Milestone | Date |
|-----------|------|
| Abstract | 2026-05-26 11:59 UTC |
| Full paper | 2026-05-29 11:59 UTC |
