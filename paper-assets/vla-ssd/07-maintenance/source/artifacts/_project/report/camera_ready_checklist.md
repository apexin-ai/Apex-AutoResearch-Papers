# Camera-Ready Checklist — v14

## Summary
- Total checks: 12
- Passed: 11
- Failed: 1 (critical: 0, minor: 1)

## Detailed Results

### 1. Page Limit (CoRL 2026: body ≤ 8 pages)
- Status: ✓
- Body: pages 1–8 (exactly 8 pages)
- References: pages 9–12
- Appendix: pages 12–42
- Total: 42 pages
- Note: `\enlargethispage{8\baselineskip}` in discussion.tex stretches the final body page. Content fits within 8 pages but this is aggressive spacing manipulation (see Issues).

### 2. Author Anonymity
- Status: ✓
- `\author{Anonymous}` in main.tex
- No acknowledgments section in the paper
- No identifying information in headers/footers
- "Use of Generative AI" paragraph mentions tools (Claude, GPT-4) only, no author names
- corl_2026 style handles anonymous formatting

### 3. Citation Format
- Status: ✓
- natbib loaded with `[square,numbers]` by corl_2026.sty
- Bibliography style: `corlabbrvnat`
- Produces squared-number format [1], [2], etc. as required

### 4. Citation Completeness
- Status: ✓
- 55 unique citation keys in .tex files
- 55 entries in references.bib
- 0 orphan bib entries (all cited)
- 0 missing bib entries (all have .bib matches)
- `verify_references` online check: 41/55 verified, 2 not found in OpenAlex (hancock2025actions — 2025 preprint; elhage2021 — Anthropic technical report), 12 first-author mismatches (mostly consortium/large-author papers where API returns a different first author — not actual errors)

### 5. Reference Resolution
- Status: ✓
- 0 undefined references in compilation log
- No "??" markers in PDF
- All 74 `\ref{}` targets have matching `\label{}` definitions
- 0 duplicate labels
- 136 labels defined total (62 unreferenced — normal for large appendix)

### 6. Cross-Reference Integrity (Body ↔ Appendix)
- Status: ✓
- All cross-references from body sections to appendix labels resolve correctly
- Appendix sections referenced from body: `sec:openvla_methods_appendix`, `sec:openvla_deepdive_appendix`, `sec:delta_r2_threshold`, `sec:nlp_control_appendix`, `sec:claim_evidence_appendix`, `sec:cka_appendix`, `sec:bonferroni_correction`, `sec:cross_arch_r2`, `sec:extended_discussion_appendix`, `sec:action_trajectory`, `sec:linear_probe`, `sec:label_permutation`, `sec:mechanistic_interpretation`, `sec:threshold_sensitivity`, `sec:cf_details_appendix`, `sec:cross_benchmark_appendix`
- All verified present in appendix.tex

### 7. LaTeX Source Cleanliness
- Status: ✓
- 0 TODO/FIXME/XXX/HACK/TEMP comments
- 0 `\textcolor` debug markers
- 0 hardcoded "Table X"/"Figure X" references (all use `\ref{}`)

### 8. Package Conflicts
- Status: ✓
- Packages loaded: corl_2026, inputenc(utf8), fontenc(T1), lmodern, url, booktabs, amsfonts, amsmath, nicefrac, microtype, graphicx, enumitem, wrapfig
- natbib loaded by corl_2026.sty (not duplicated in main.tex)
- No conflicting packages detected

### 9. Bib Entry Completeness
- Status: ✓
- All 55 entries have required fields (title, author, year)
- Venue information present for all entries (booktitle/journal/eprint)

### 10. Compilation Warnings
- Status: ✓ (no critical warnings)
- `h` float specifier → `ht`: 25 instances (all in appendix tables — cosmetic, normal)
- hyperref Unicode token warnings: 10 instances (math symbols in section titles — cosmetic, no visible issue in PDF)
- wrapfig warning: 1 instance (stationary wrapfigure forced to float — cosmetic)
- No undefined references, no rerun needed

### 11. Paper Consistency
- Status: ✓
- Numbers in abstract/conclusion consistent with experiments section
- Notation consistent across sections (Δ, ×, ρ used uniformly)
- Metric qualifiers consistent (Cohen's d, R², Δ R²)
- `check_paper_consistency` flagged 2 false-positive "missing bib" in corl_example.tex (not included in paper) and 3 false-positive "orphan bib" (hewitt2019control, lakens2017equivalence, nili2014toolbox — all actually cited in appendix.tex)

### 12. Anonymity Deep Check
- Status: ✓
- No university/lab names in text
- No grant numbers
- No URLs pointing to author pages/repos
- "Code and data will be released upon acceptance" — appropriate for anonymous submission

## Issues (sorted by severity)

1. **[MINOR]** `\enlargethispage{8\baselineskip}` in `discussion.tex` line 1 — adds ~8 lines of vertical space to page 8 to fit the Discussion/Conclusion section. The content does fit, but this is aggressive spacing manipulation. Some reviewers/ACs flag this. Consider whether the conclusion can be tightened by 2–3 lines to remove or reduce this stretch. If the conference has a camera-ready formatting check, this may trigger a warning.

## Notes

- **corl_example.tex** is present in the directory but NOT included via `\input` in main.tex. Its `\cite{Gauss1857}` and `\cite{Lagrange1788}` have no bib entries, but this is irrelevant since the file is a template example.
- **Online reference verification**: 2 entries not found in OpenAlex (hancock2025actions, elhage2021) are recent preprints/technical reports not yet indexed — not actual citation errors.
- **First-author mismatches** in 12 entries are API artifacts (consortium papers, Chinese naming conventions, etc.) — all titles and years match correctly.
