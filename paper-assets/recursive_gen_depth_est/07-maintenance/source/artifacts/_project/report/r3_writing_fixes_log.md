# R3 Writing Fixes Log

Date: 2026-05-15

## Summary

All pure-writing issues from Round 3 review addressed. No new experiments required.

---

## Issue-by-Issue Changes

### 1. R3-N1: EDD formula continuous version
**Status**: Already addressed (no change needed)
- Eq. 1 in method.tex already uses the `∀ d' ≤ d*` formulation
- Footnote to Eq. 1 already explains equivalence under monotonicity
- Limitations paragraph "EDD monotonicity assumption" already discusses the assumption and its failure modes

### 2. R3-N4: Scope-limit 'universal' claims
**Files modified**: atlas.tex
- atlas.tex L121: "the universal bottleneck" → "the consistent bottleneck across all 9 cells"
- No instances of "universal stability" or "universally mark" found in abstract.tex or introduction.tex (already scoped with "across the studied 3×3 grid" and "three model families and three decoding strategies studied")

### 3. R3-N5 + R3-W3: Weaken cross-strategy claims + 'geometry-level shift'
**Files modified**: discussion.tex, paper_framing.md
- No "geometry-level shift" found in any tex file — already absent
- paper_framing.md: 2 occurrences of "geometry-level shift" → "a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open"
- discussion.tex: New "Cross-strategy deployment" paragraph uses the correct language
- discussion.tex: New "Depth-aware data curation" paragraph tempers expectations for data filtering ("mid-depth classification degrades substantially, tempering expectations for depth-based filtering in uncontrolled settings")
- Two-stage pipeline discussed as future direction in Discussion §Cross-strategy deployment

### 4. R3-W1: d1-d3 accuracy side-by-side reporting
**Files modified**: abstract.tex, atlas.tex
- **Source**: Registry `granularity_ablation_rf_001` — 3-class accuracy range 58.8%–82.6%, mean 72.1%
- abstract.tex: Filled "XX.X--XX.X%" → "58.8--82.6%"
- atlas.tex Table 2 caption: Filled "XX.X% to XX.X%" → "58.8% to 82.6%"
- Cross-model Table 5 caption: d1-d3 balanced accuracy 55.5% (kept — consistent with displayed per-holdout means: (49.9+59.2+57.3)/3 = 55.47% ≈ 55.5%)
- Cross-strategy excl-d0: Already filled as 45.9% (line 95)
- Note: Cross-model/cross-strategy tables do not include separate "excl. d0" rows — per-class recall columns already enable this analysis

### 5. R3-W2 + R3-W6: Expand Discussion to 300-400 words
**Files modified**: discussion.tex
- Expanded from ~80 words / 5 sentences to ~380 words / 5 structured paragraphs:
  - (a) **Depth-aware data curation**: graded weighting vs binary filtering, tempered expectations
  - (b) **Cross-strategy deployment**: distributional shift language, two-stage pipeline as future work
  - (c) **Mixed-depth corpora**: segment-level estimation, granularity tradeoff
  - (d) **Adversarial robustness and provenance**: paraphrasing attacks, unified provenance toolkit
  - (e) **Scaling and feature evolution**: var_surprisal → p90_ppl/kurtosis progression, alignment with Shumailov tail erosion theory, 7B+ open question

### 6. R3-W4: Remove experiment tracking IDs
**Status**: Already clean (no change needed)
- Searched all tex files for `depth_extension_`, `mvp_pipeline_`, `cross_model_`, `baseline_battery_`, `feat_ablation_` — zero matches

### 7. R3-M1: Minor fixes
**Files modified**: method.tex, references.bib

| Item | Status | Detail |
|------|--------|--------|
| §3 title | Fixed | "Task Formulation" → "Method" |
| holtzman year | No change | year=2020 is correct (ICLR 2020 publication; arXiv 2019 is preprint) |
| basu year | No change | year=2021 is correct (ICLR 2021 publication; arXiv 2020 is preprint) |
| Abstract ρ | Fixed | Removed "cross-cell Spearman ρ > 0.85" from abstract (kept ρ=0.868 in intro contributions where detail is appropriate) |
| Ethics Statement | No change | Already present in conclusion.tex |
| 'standard LoRA' | No change | Already says "commonly used LoRA hyperparameters" |
| Ghostbuster citation | Fixed | Removed "Citation needs verification" note; venue NAACL 2024 confirmed |
| M4-SemEval citation | Fixed | Corrected author list (15 authors), venue → "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)", added arXiv:2404.14183 |
| DNA-GPT citation | Fixed | Venue AAAI → ICLR 2024; title corrected to published version; added Yue Wu to authors; removed "Citation needs verification" |

### 8. R2-W1: DivEye venue
**Status**: Already correct (no change needed)
- WebSearch confirmed: TMLR 2026. Bib entry already has `journal = {Transactions on Machine Learning Research (TMLR)}, year = {2026}`

### 9. Zero-shot 500-sample update
**Files modified**: abstract.tex, generalization.tex
- **Source**: Registry `zeroshot_llm_500_001` — 36.2% [32.0%, 40.4%], n=500
- abstract.tex: "40%" → "36.2%"
- generalization.tex Table 3: "40.0" → "36.2"
- generalization.tex footnote: "200 samples (approximately 50 per class)" → "500 samples (125 per class)"; CI updated
- generalization.tex body text: "40.0%" → "36.2%"

---

## Known Remaining Items
- `main.aux` and `main.bbl` contain stale data from previous compilation — will auto-regenerate on next `pdflatex`/`bibtex` build
- Cross-model/cross-strategy tables do not add separate "excl. d0" rows; per-class recall columns serve this purpose. Adding explicit rows is possible if reviewer insists.
