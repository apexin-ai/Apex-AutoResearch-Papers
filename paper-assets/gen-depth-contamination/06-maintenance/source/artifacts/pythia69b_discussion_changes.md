# Pythia-6.9B Discussion + Appendix Changes (2026-05-21)

## Part 1: Discussion Paragraph Added

File: `docs/paper/discussion.tex`, after line 36 (end of "Boundary cases and scale effect" paragraph).

**New paragraph (exact text):**

```latex
\paragraph{Decoding strategy as confound.}
Pythia-6.9B under greedy decoding yields $\Kempirical{=}2$ (1v2 $\auc = 0.854$), but switching to nucleus sampling ($p{=}0.95$) reduces the boundary to $\Kempirical{=}1$ (1v2 $\auc = 0.596$), providing direct evidence that greedy repetition artifacts inflate depth separability.
The borderline 1v2 score (2 of 5 folds exceed $\theta{=}0.60$) illustrates that the $\Kempirical$ boundary is continuous rather than a binary cliff.
Comparing Pythia-1.4B ($\Kempirical{=}2$, 1v2 $\auc = 0.654$) with Pythia-6.9B ($\Kempirical{=}1$, 1v2 $\auc = 0.596$) further confirms that increased model scale does not monotonically raise $\Kempirical$.
```

## Part 2: Appendix Table Updated

File: `docs/paper/appendix.tex`, table `tab:kstar_ci_extended`.

**Changes:**
- Added new column: Pythia-6.9B (nucleus) with footnote marker `$^\S$`
- Data added:
  - 0v1: .9599
  - 1v2: .5955
  - 2v3: .5298
  - 3v4: .5135
  - 4v5: -- (not available)
- Added footnote: `$^\S$Pythia-6.9B: nucleus sampling ($p{=}0.95$); all other Pythia entries use greedy decoding.`
- Updated caption: "6/9 conditions" (was 6/8), added "Pythia-6.9B" to K*=1 list
- Updated tabular column count from 15 to 17

**JSD decay table:** No JSD table exists in the appendix; JSD data (0v1: 0.1259, 1v2: 0.0084) not inserted.

## Part 3: Compilation

- Build: **SUCCESS** (no errors)
- Total pages: 20 (main body: 7 pages, Limitations+References start page 8, Appendix pages 9-20)
- Main text within 8-page limit: **YES**
