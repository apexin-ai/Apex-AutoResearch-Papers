# Anonymous Repo Update Report

**Date**: 2026-05-23
**Commit**: c184e4e
**Author/Committer**: Anonymous <anonymous@example.com>

## Push Result

Force push **successful**: `91bcdb4...c184e4e main -> main (forced update)`

## Paper Files (25 files)

### LaTeX Sources
- abstract.tex, conclusion.tex, discussion.tex, experiments.tex, introduction.tex, main.tex, method.tex, related_work.tex
- responsibleNLPchecklist.tex (new)
- references.bib, main.bbl
- acl.sty, acl_natbib.bst

### Figures (12 files)
- pipeline_overview.pdf, label_decomposition.pdf, fig1_daf_scatter.pdf, dose_response.pdf, signal_reversal.pdf
- death_action_comparison.pdf, death_action_distribution.pdf, death_action_timeline.pdf (new)
- gen_fig1.py, gen_fig2.py (new), gen_pipeline.py, gen_signal_reversal.py

## Compilation Result

- **Pages**: 25
- **Undefined refs**: 0
- Compiled successfully with pdflatex (2 passes)

## Anonymization Check

All checks passed (CLEAN):
1. Usernames/IDs (caoxiaoyu, 1844118046): CLEAN
2. Chinese names: CLEAN
3. Server info (westd, autodl, 18266): CLEAN
4. University/institute names: CLEAN
5. Email addresses: CLEAN
6. API tokens (ghp_, sk-, hf_): CLEAN (only false positives: `hf_cache_dirs` variable, `risk-sensitive` text)

## Other Changes

- **README.md**: Updated "90.4% of it originates from death avoidance" -> "78.9% of non-tie routing labels arise from death asymmetry"
- **guided_router/README.md**: Updated "DAF=90.4%" -> "78.9% label fraction (DAF 88-90%)"
- **.gitignore**: Added `_pdf_images*/`
- Cleaned: _pdf_images/, *.aux, *.log, *.out, *.blg, *.fls, *.fdb_latexmk, main.pdf, *.png, SETUP_NOTES.md

## Notes

- `guided_router/framework_draft.md` still contains "DAF = 90.4%" in 3 places (internal design doc, not paper-facing; left as-is)
- Compilation done locally (not on server) due to SSH key auth mismatch; pdflatex version matches
