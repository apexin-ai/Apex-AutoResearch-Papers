# Paper Compile Check — 2026-05-15

## Summary

| Item | Status |
|------|--------|
| Compilation | ✓ Success (no errors) |
| Total pages | 19 |
| Body pages | 8 (within ACL limit) |
| References | ~2 pages (9–10) |
| Appendix | 9 pages (11–19) |
| Undefined refs | None |
| Missing citations | None |
| Rerun needed | No |

## Warnings

### Critical: None

### Overfull hbox (2)
Both in **appendix** tables — no impact on body page limit:
- `appendix.tex` lines 92–108: Table (Fisher's exact tests) — 107pt too wide
- `appendix.tex` lines 508–527: Table (3-seed results) — 191pt too wide

### Underfull vbox: 3
### Underfull hbox: 111 (mostly normal paragraph formatting)

### Hyperref warnings (cosmetic)
- 7× "Token not allowed in a PDF string (Unicode)" — math symbols in section titles, no functional impact

### Float specifier
- 2× `'h' float specifier changed to 'ht'` — normal LaTeX behavior

## Verdict

Paper compiles cleanly. Body fits within 8-page ACL limit. No undefined references or citations. Two wide tables in appendix should be wrapped in `\resizebox{\columnwidth}{!}{...}` before camera-ready but are acceptable for review submission.
