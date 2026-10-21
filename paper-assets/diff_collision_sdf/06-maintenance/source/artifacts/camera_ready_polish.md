# Camera-Ready Polish Checklist

## Priority A (Should Fix)

- [ ] `fig:overview` never referenced in text — Figure 1 (overview) is defined but no `\ref{fig:overview}` appears anywhere; add explicit reference in intro paragraph — introduction.tex:7
- [ ] "Collision Avoidance Rates" (plural) in abstract vs "Collision Avoidance Rate" (singular) everywhere else; standardize to singular — abstract.tex:2 vs introduction.tex:10, method.tex:5
- [ ] SSR abbreviation never expanded — first use "SSR\,=\,TSR\,$\cap$\,CAR" defines the formula but never spells out "Safe Success Rate" (or whatever it stands for) — claim3.tex:36
- [ ] MDE abbreviation never defined — used in claim3.tex:59 ("MDE ${\approx}$ 5.6\,pp") and discussion.tex:7 without expansion to "Minimum Detectable Effect"
- [ ] `\citep` vs `\cite` inconsistency — related_work.tex:12 uses `\citep{zhang2025safevla}` and `\citep{hu2025vlsa}`; appendix.tex:323 uses `\citep{hu2022lora}`; all other citations use `\cite`. Mixing may produce different bracket styles depending on natbib config
- [ ] Equations never cross-referenced — `eq:car_f` (method.tex:31) and `eq:total_loss` (method.tex:39) are labeled but never referenced via `\eqref` or `Eq.~\ref`; either reference them or remove the labels
- [ ] Section cross-reference style inconsistent — introduction.tex:16,18,20 use `Section~\ref{}`; claim2.tex:3 and discussion.tex:3 use `\S\ref{}`; related_work.tex:15 uses `\S\ref{}`. Pick one convention and apply uniformly
- [ ] Duplicate `\label` on same section — appendix.tex:153-154 has both `\label{sec:appendix_pertask}` and `\label{sec:appendix_pertask_oracle}` on consecutive lines for the same section; `sec:appendix_pertask` is never referenced and should be removed

## Priority B (Nice to Have)

- [ ] CAR decimal precision inconsistent in Table 4 — claim3.tex:17-20: LoRA-only reports 54.83, SDF λ=0.005 reports 54.5 (should be 54.50), SDF λ=0.1 reports 57.00. Standardize all means to same decimal places
- [ ] Table environment mismatch — claim1.tex:11 uses `\begin{tabular*}{\linewidth}` while all other tables use `\begin{tabular}`. Standardize
- [ ] Table font size inconsistency in appendix — appendix.tex:74 (`tab:dfcar_threshold`) uses `\footnotesize` while all other appendix tables use `\small`
- [ ] Appendix table placement specifier — all appendix tables use `[h]` which LaTeX often overrides; consider `[ht]` or `[htbp]` to avoid "float too large" warnings
- [ ] Sub-figure labeling style inconsistent — fig:overview caption (introduction.tex:6) uses `\textbf{(a)}`, `\textbf{(b)}`, `\textbf{(c)}` but fig:scatter_and_oracle (claim1.tex:27) and fig:lambda_and_fingerprint (claim3.tex:31) use plain `(Left)`/`(Right)`. Pick one convention
- [ ] "n.s." not expanded — introduction.tex:6 (overview figure caption) uses "n.s." without defining it. While standard in statistics, expanding once ("not significant, n.s.") aids non-specialist readers
- [ ] `\label{sec:oracle_setup}` placed at end of paragraph, not at `\subsection` — method.tex:46 attaches the label to the end of a paragraph rather than a section/subsection heading, which is fragile for cross-references
- [ ] `\label{sec:anticorrelation}` mid-paragraph — claim1.tex:30 defines this label inline mid-sentence; never referenced. Remove or relocate
- [ ] `\label{sec:tsr_collapse}` on `\paragraph` — claim3.tex:35; never referenced from outside. Remove if unused
- [ ] `\label{sec:lambda_high}` on `\paragraph` — claim3.tex:58; never referenced. Remove if unused
- [ ] `jacquet2025neuralnmpc` missing volume/pages — references.bib:170; journal article with no volume, number, or page range (may be in-press; add "to appear" note if so)

## Priority C (Cosmetic)

- [ ] ~15 leftover figure versions in `artifacts/figures/` (fig_overview_pb_v1 through v13, fig1_teaser_v2, fig2_plan_a/b, etc.) — not included in paper; clean up before camera-ready archive submission
- [ ] "100+ experiments" in introduction.tex:14 — consider `$>$100 experiments` for typographic consistency with other numeric comparisons in the paper
- [ ] BibTeX key naming inconsistent — most keys follow `authorYYYYkeyword` (e.g., `black2024pi0`) but `cofreeevla2026`, `depthvla2025` omit author prefix. Not reader-visible but aids maintainability
- [ ] No `\hypersetup` for PDF metadata — main.tex has no `\hypersetup{pdftitle=..., pdfauthor=...}`; camera-ready PDF should carry correct metadata (update `pdfauthor` when de-anonymizing)
- [ ] `\keywords` placement — main.tex:28 places `\keywords` after `\input{abstract}`; verify `corl_2026.sty` expects this ordering (some styles require keywords inside the abstract environment)
- [ ] Unreferenced appendix section labels (not harmful but noisy) — `sec:appendix_multiseed`, `sec:appendix_displacement`, `sec:appendix_tsr_pertask`, `sec:appendix_pertask_car`, `sec:appendix_ssr`, `sec:appendix_stepwise`, `sec:appendix_spatial_bowl`, `sec:appendix_eval_seed`, `sec:appendix_tsr_collapse`, `sec:conclusion`, `sec:limitations`, `sec:intro`, `sec:method`, `sec:benchmark`, `sec:sdf_aux`. Many are structural anchors (standard); consider removing truly orphaned ones
- [ ] Figures have both PDF and PNG versions — LaTeX will prefer PDF (vector), which is correct; ensure no `\includegraphics` call accidentally specifies `.png` extension to avoid raster fallback
