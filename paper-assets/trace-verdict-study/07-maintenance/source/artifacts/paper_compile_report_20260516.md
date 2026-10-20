# Paper Compilation Report — 2026-05-16

## Compilation Status: SUCCESS (with non-critical warnings)

**Output**: `main.pdf` — 18 pages, 322,768 bytes

## Page Structure

| Section | Pages | Count |
|---------|-------|-------|
| Body (Introduction → Conclusion) | 1–13 | **13 pages** |
| References | 14–15 | 2 pages |
| Appendix | 15–18 | ~3 pages |
| **Total** | | **18 pages** |

**⚠ Body exceeds 8-page limit (13 pages).** Needs trimming before submission.

## Figures

All 4 figures present and rendered:

| Figure | File | Size | Page |
|--------|------|------|------|
| fig1_trace_overview.pdf | 37 KB | 6 |
| fig2_calibration.pdf | 18 KB | 9 |
| fig3_cross_model_gap.pdf | 33 KB | 10 |
| fig4_trace_length.pdf | 17 KB | — |

No missing figure warnings.

## References

- **BibTeX**: 27 entries, 0 warnings, 0 errors
- **Undefined references**: 0
- **Undefined citations**: 0

## LaTeX Errors (non-critical)

3 errors from `acl.sty` compatibility with TeX Live 2022:

1. `Package keyval Error: sargin undefined` — geometry.sty version mismatch
2. `LaTeX Error: Missing \begin{document}` — cascading from #1
3. `Package caption Error: 10pt undefined` — cascading from acl.sty

These do not affect PDF output but indicate the TeX Live 2022 installation is older than what acl.sty expects. Upgrading `texlive-latex-extra` or using a newer TeX Live would resolve them.

## Warnings Summary

| Type | Count | Severity |
|------|-------|----------|
| Overfull hbox | 8 | Low |
| Underfull hbox/vbox | 181 | Low |
| Undefined references | 0 | — |
| Missing figures | 0 | — |

## Critical Issues

1. **Body page count (13) exceeds 8-page limit** — must reduce by ~5 pages before submission
