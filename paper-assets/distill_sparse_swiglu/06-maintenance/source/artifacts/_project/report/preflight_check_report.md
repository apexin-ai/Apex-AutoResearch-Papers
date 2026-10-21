# Pre-flight Check Report (2026-05-19)

## Summary: PASS (2 minor warnings)

## 1. LaTeX Compilation: ✅
- No errors. `latexmk -pdf` reports "All targets up-to-date".
- 4 warnings, all identical: `'h' float specifier changed to 'ht'` (benign).

## 2. Page Count: ✅
- Total PDF pages: 17
- Body (through Conclusion): **8 pages** (pages 1-8). Conclusion ends on page 8.
- Limitations + Ethics: page 9 (exempt from limit)
- References: pages 10-11 (exempt)
- Appendix: pages 12-17 (exempt)
- ARR Long Paper limit is 8 body pages. **Exactly at limit.**

## 3. Citation Completeness: ✅
- 0 undefined citation warnings in `main.log`.
- 0 bibtex errors in `main.blg`.
- 46 unique `\cite` commands across tex files; 47 bib entries. All resolved.

## 4. Anonymization: ✅
- `\usepackage[review]{acl}` confirmed (line 2, main.tex).
- `\author{Anonymous}` confirmed (line 24, main.tex).
- No author names, institution names, or personal URLs (github.com/*, huggingface.co/*) found in any tex file.

## 5. Figure/Table Reference Consistency: ⚠️ Minor
- 0 undefined references in `main.log`.
- All `\ref{}` commands point to existing `\label{}` entries.
- **24 labels defined but never `\ref`'d.** Most are benign (section/equation labels for structure). Notable:
  - `fig:overview` (method.tex:151): figure exists but is never referenced in text.
  - 3 appendix sections never referenced from body: `app:stability`, `app:tau_sensitivity`, `app:training_convergence`.
  - 4 appendix tables never directly referenced: `tab:14b`, `tab:ood`, `tab:tau_sensitivity`, `tab:training_convergence` (their parent appendix sections `app:14b` and `app:ood` ARE referenced for the first two; the latter two are not).
- **Recommendation**: Add `\ref` for `fig:overview` or remove if unused. Consider referencing or removing the 3 orphan appendix sections.

## 6. Ethics/Limitations: ✅
- `ethics.tex`: 43 lines, substantive content. Full Responsible NLP Research Checklist (sections A-E) with specific answers. No blanket N/A on applicable items.
- `limitations.tex`: 11 lines, substantive content covering: PPL as proxy limitation, per-target training cost, GSM8K reversal, OOD gap, C1 ablation scope, seed variance, wall-clock caveat, future directions.

## 7. Table Number Cross-check: ✅
Three numbers sampled from Table 2 (`tab:main`):

| Value | Location | exp_id annotation | Consistent? |
|-------|----------|-------------------|-------------|
| KL global 30% PPL 8.96±0.02 | experiments.tex:49 | `kl30_3seed_global` | ✅ naming matches 3-seed KL at 30% global |
| TEAL 50% PPL 23.31 | experiments.tex:54 | `bench_teal50` | ✅ naming matches TEAL benchmark at 50% |
| BCE 2700 steps PPL 28.13±0.20 | experiments.tex:57 | `bce50_3seed` | ✅ naming matches BCE 50% 3-seed |

All sampled values have exp_id annotations with naming conventions consistent with the described experimental configuration.

## 8. AI Writing Style (Bonus): ✅
- 0 em-dashes (U+2014) in tex files.
- 0 explanatory en-dashes in tex files.
- No violations of dash prohibition rule.
