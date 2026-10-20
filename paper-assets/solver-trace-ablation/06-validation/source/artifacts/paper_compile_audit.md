# Paper Compile & Format Audit

- **Source**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/`
- **Date**: 2026-05-14
- **Tooling**: TeX Live 2025 / Debian, `pdflatex` + `bibtex` (4 passes: pdflatex → bibtex → pdflatex → pdflatex → pdflatex)
- **Compile result**: SUCCESS — `main.pdf`, 18 pages, 519 KB
- **Template**: ACL 2023 (`\usepackage[review]{acl}`)
- **Body word count**: 6 511 words across abstract → conclusion (excluding refs/appendix)

---

## CRITICAL (blocks submission)

### C1. Body exceeds ACL 8-page limit by ~5 pages
- **Body content (Introduction §1 through Conclusion §6) ends mid-page 13.** ACL 2023 long-paper rules allow 8 pages of main content (refs and appendix unlimited).
- Page-by-page mapping of `main.pdf`:
  | Page | Content |
  |------|---------|
  | 1–4 | Title, abstract, §1 Introduction, §2 Related Work (starts p.2) |
  | 5 | §3 Method (starts) |
  | 6 | Fig. 1 (STA overview) |
  | 7–9 | §3 Method (cont.) |
  | 9 | §4 Experiments (starts mid-page) |
  | 9–13 | §4 Experiments incl. Tables 1–4, Figs. 2–4 |
  | 13 | §5 Discussion + §6 Conclusion (left col), References begin in right col line 1013 |
  | 13–14 | References |
  | 15–18 | Appendix A–C |
- **Action required**: cut ~5 pages from body. Likely targets: §2 Related Work (969 w, currently ~1 page), §3 Method (1 068 w + Fig. 1 spans p.5–9), §4 Experiments (2 392 w with 4 tables + 3 figures). Consider moving Table 4 / detailed taxonomy or per-seed numbers to appendix, tightening Related Work, and collapsing the Discussion limitations + future work paragraphs.

---

## WARNING (should fix before submission)

### W1. Overfull \hbox in body tables (6 instances)
Tables in `experiments.tex` overflow the column. Visible as text bleeding past column edge.
- L97–114 (Table 1, $\beta{=}0.1$ ISR vs Rand): **44.4 pt** overfull → likely the long caption.
- L111: **12.4 pt** detected — last row of Table 1.
- L147–166 (Table 2, cross-logic): **22.9 pt** — caption with many `$^\dagger$` footnote markers.
- L201–214 (Table 4, hacking taxonomy): **3.7 / 10.3 / 4.5 pt** — column entries (`$n_{\text{comp}}{\uparrow}$, ISR${\to}$0` etc.) too wide.
- **Action**: tighten captions (footnotes can become table notes below), shorten in-cell macros, or widen via `\setlength{\tabcolsep}` shrink (already at 3pt), or use `\resizebox`.

### W2. `\float specifier 'h' changed to 'ht'` (1 instance)
- Source: `appendix.tex` line 13 — `\begin{table}[h]`.
- Cosmetic; ACL style nudges floats. **Action**: change `[h]` → `[t]` or `[ht]` to suppress warning.

### W3. Unused `\label` declarations (14)
Labels defined but never `\ref`'d. Indicates abandoned numbering or copy-paste leftovers:
- Section labels: `sec:introduction`, `sec:conclusion`, `sec:grpo`, `sec:rewards`, `sec:sta`, `sec:task`, `sec:taxonomy-method`
- Equation labels: `eq:isr`, `eq:rexec`, `eq:additive-isr`, `eq:additive-random`
- Appendix labels: `app:setup`, `app:hacking-modes`, `app:detailed-results`
- **Action**: either reference them (e.g., point readers from body to appendix sections) or delete the `\label{}`. Section labels are usually fine to keep for future reference; equation labels suggest equations should be cited by number in prose.

### W4. Overfull \hbox in appendix verbatim/tables (8 instances)
Source: `appendix.tex` — hyperparameter table (L17–59: **89.5 pt**), verbatim code examples (L85, L109, L177, L201, L248–290: 16–86 pt).
- Verbatim examples (FOL/Prolog snippets) exceed `\columnwidth`. Single-column layout, but ACL 2-column shows clipping.
- **Action**: wrap long verbatim lines, or switch to `\begin{lstlisting}[breaklines]` with breakable code listings. Hyperparam table can use `\small` or `\setlength{\tabcolsep}{3pt}` (already small — may need column-wrap or move to single-column appendix layout).

---

## INFO (advisory, not blocking)

### I1. Cross-references
- **0** undefined references. All `\ref`/`\autoref` resolve to existing labels.
- **0** undefined citations. `bibtex` ran clean (`main.blg` shows no warnings).
- **No** `??` in PDF output.

### I2. Bibliography integrity
- **33 bib entries / 33 cited** — perfect 1:1 match. No orphan bib entries; no missing definitions.
- No placeholder / `TODO` / `PLACEHOLDER` strings in any `.tex` or `.bib` file.
- All entry types use BibTeX-standard fields. The reference style `acl_natbib.bst` renders correctly.

### I3. Figures
- All 4 `\includegraphics` paths resolve to existing PDFs:
  - `figures/fig1_sta_overview.pdf` (method.tex)
  - `figures/fig2_isr_collapse.pdf` (experiments.tex)
  - `figures/fig3_hacking_composition.pdf` (experiments.tex)
  - `figures/fig4_prolog_comparison.pdf` (experiments.tex)
- Each figure has a non-empty caption and `\label`. All are referenced in body text.
- Note: `figures/fig2_isr_collapse.png` exists alongside the `.pdf` — harmless duplicate.

### I4. Underfull \hbox warnings (~85 instances)
All are typographic justification badness (loose interword spacing in narrow ACL columns). Not visible defects; safe to ignore unless aggressive polish is desired.

### I5. Compile passes
- After 4 pdflatex passes, no `Rerun to get cross-references right` or `Package lineno` warnings remain. Build is stable.

---

## Summary

| Severity | Count | Topic |
|----------|-------|-------|
| CRITICAL | 1 | Body content exceeds 8-page ACL limit by 5 pages |
| WARNING | 4 | 6 body-table overfulls, `[h]→[ht]` float warning, 14 unused labels, 8 appendix overfulls |
| INFO | 5 | Refs/cites/figures all clean, build stable |

**Next action**: address C1 (cut body to 8 pages) before any cosmetic fixes. W3/W4 can be batched in a final pass.
