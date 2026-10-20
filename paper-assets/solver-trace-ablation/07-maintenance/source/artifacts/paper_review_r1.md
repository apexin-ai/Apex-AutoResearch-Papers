# Paper Review Round 1 — solver-trace-ablation

**Date**: 2026-05-14
**Target venue**: EMNLP 2026 (DDL 2026-05-25)
**Source**: `paper/main.tex` (current main document)
**Compile result**: ✅ Builds; 14 pages total (6 main + 2 references + 6 appendix)

---

## TL;DR

Compiles successfully and respects all hard content constraints (D051 enforced, s44 marked as gaming, 7-mode taxonomy consistent, ISR* unified, H7=0% under random correctly stated, SFT 92.9%, premise-matched 1.06×). Main body is **6 pages** — comfortably under the 8-page limit. Two **P0 blockers**: 6 missing `.bib` entries cause undefined-citation warnings on every compile, and the `\bibliography` line is correct but bib has no entries for `proofwriter`, `prontoqa`, `thinkprm`, `versaprm`, `rprm`, `metr-reward-hacking`. One **P1**: `fig:prolog-comparison` (Fig 4) is labeled but never `\ref`'d.

---

## P0 — Must fix before submission

### P0-1. Six missing bibliography entries (undefined citations)

Persistent natbib warnings on every compile pass. These citation keys appear in `.tex` but have no entry in `references.bib`:

| Key                  | Cited in                                    |
|----------------------|---------------------------------------------|
| `proofwriter`        | `related_work.tex:10`                       |
| `prontoqa`           | `related_work.tex:10`                       |
| `thinkprm`           | `related_work.tex:15`                       |
| `versaprm`           | `related_work.tex:15`                       |
| `rprm`               | `related_work.tex:15`                       |
| `metr-reward-hacking`| `related_work.tex:19`                       |

`writing_plan.yaml` literature_strategy lists `proofwriter` as a must-cite. All six render as `[?]` placeholders in the PDF (visible in current `main.pdf`).

**Action**: Add 6 BibTeX entries to `references.bib`.

### P0-2. Verify `[?]` placeholders are gone after fix

Re-run full pipeline (`pdflatex → bibtex → pdflatex → pdflatex`) and confirm `Citation … undefined` warnings disappear.

---

## P1 — Should fix

### P1-1. `fig:prolog-comparison` labeled but never referenced

`appendix.tex:412` defines `\label{fig:prolog-comparison}` for Fig 4 (`fig4_prolog_comparison.pdf`), but no `\ref{fig:prolog-comparison}` exists anywhere. The figure floats on page 12 of the appendix without a textual call-out — readers cannot tell what passage it illustrates.

**Action**: Add a `(Figure~\ref{fig:prolog-comparison})` reference inside `\paragraph{Prolog: universal Goodhart via three distinct pathways.}` in `appendix.tex` (around lines 421–426), since that paragraph describes exactly what the figure shows.

### P1-2. Duplicate `\label` on same table

Two appendix tables each carry two consecutive `\label`s pointing to the same float:

- `appendix.tex:325-326`: `\label{tab:fol-detailed}` + `\label{tab:beta01-3seed}` (FOL detailed table)
- `appendix.tex:377-378`: `\label{tab:prolog-detailed}` + `\label{tab:prolog-crosslogic}` (Prolog table)

Technically valid (later label wins for the float counter), but the unused alias (`tab:fol-detailed`, `tab:prolog-detailed`) wastes label-space. Both unused aliases generate `tab:fol-detailed` etc as silent dangling labels.

**Action**: Drop the unused label of each pair. The currently-cross-referenced names are `tab:beta01-3seed` and `tab:prolog-crosslogic` — keep these, delete the other two.

### P1-3. One unused entry in `references.bib`

`math-shepherd` is in the bib but never cited (the `lightman-verify-step,math-shepherd` group cite was edited away at some point, but `math-shepherd` remained in the file).

**Action**: Either cite it (it appears in `writing_plan.yaml` cluster `verification-reward`) or remove the entry.

### P1-4. Stale legacy file `paper.tex`

`paper.tex` is a leftover earlier main file. It (a) `\input{discussion}` which does not exist (would break compile), (b) carries an outdated title (`"Solver Trace Ablation Reveals Meta-Level Goodhart's Law\\in Neurosymbolic Reasoning"`) different from `main.tex`'s current title, and (c) leaves a stale `paper.pdf` / `paper.aux` / `paper.bbl` in the directory that could confuse the submission packaging.

**Recommendation**: Delete `paper.tex`, `paper.aux`, `paper.bbl`, `paper.blg`, `paper.log`, `paper.out`, `paper.pdf`. Only `main.*` should remain. (If keeping for archival reasons, at least rename `paper.tex` → `paper_legacy.tex.unused` so it is not mistaken for the current file.)

---

## P2 — Nice to have

### P2-1. Section labels never `\ref`'d

`sec:experiments`, `sec:introduction`, `sec:limitations`, `sec:method`, `sec:rewards`, `sec:sta`, `sec:task`, `sec:taxonomy-method`, `eq:isr`, `app:detailed-results` are defined but never referenced. Acceptable (sections have natural numbering) but slightly noisy in the `.aux`. Leave or prune as preference.

### P2-2. Underfull `\hbox` warnings

Many lines have low-badness underfull hbox warnings (esp. in two-column narrow boxes). None are visually disastrous; ignore unless the polished PDF shows obvious river/whitespace issues.

### P2-3. Acknowledge dataset description in writing plan vs paper

`writing_plan.yaml` line 92 still describes the eval set as "ProofWriter-FOL-100" while the actual paper uses FOLIO. Paper text is consistent (FOLIO throughout), but `writing_plan.yaml` is stale. Fix the plan or note that it is frozen.

### P2-4. Single seed used in `tab:goodhart-landscape` Exec-only / β=0.3 rows

Caption already calls this out (`$^\dagger$Seed~42`), so it is honest. Just confirming reviewers will see this.

---

## Hard-constraint compliance check (all PASS)

| Constraint | Status | Evidence |
|------------|--------|----------|
| D051: no "2.4×" anywhere | ✅ PASS | `grep "2\.4"` over `*.tex` returns no matches |
| Premise-count-matched 1.06× present | ✅ PASS | `abstract.tex:6`, `introduction.tex:22, 29`, `experiments.tex:83`, `appendix.tex:102` |
| s44 marked as gaming (not genuine) | ✅ PASS | `experiments.tex:96` "s44 query-as-fact gaming"; `appendix.tex:411` caption "three distinct gaming pathways"; `appendix.tex:394` table row marks 0% N-H with footnote |
| 7-mode taxonomy (not 6) | ✅ PASS | `introduction.tex:31`, `method.tex:63`, `experiments.tex:13` (footnote), `conclusion.tex:7`, `appendix.tex:122` all say "seven" / "7" |
| Proved-only ISR* used uniformly | ✅ PASS | `experiments.tex:13` defines ISR$^*$; tables use `\textbf{ISR$^*$}` (`appendix.tex:331,382`); appendix line 320 explicitly states "ISR values are proved-only ISR$^*$" |
| H7=0% under random | ✅ PASS | `abstract.tex:6` "0\% under matched random controls"; `experiments.tex:76` "all three random controls show \emph{zero} H7 (0/256)"; `introduction.tex:22` |
| Conclusion embedding GRPO-universal range | ✅ PASS | Range stated as **68–97%** in `experiments.tex:77`, `experiments.tex:109`, `appendix.tex:170`. Spec said "68-100% or similar" — 68–97% is the empirically supported figure and is internally consistent. |
| SFT 92.9% non-hacking | ✅ PASS | `abstract.tex:4`, `introduction.tex:19,28`, `experiments.tex:41`, `experiments.tex:105` (figure caption), `appendix.tex:339` (table) |
| C006: distinguish exec-only-Prolog low-ISR (redundancy) vs exec+STA high-ISR (gaming) | ✅ PASS | `experiments.tex:95`, `conclusion.tex:10`, `appendix.tex:93–96` |

---

## Cross-reference check

All `\ref` / `\autoref` targets resolve. All tables and figures expected by the spec exist:

| Expected | Defined at | Referenced |
|----------|-----------|------------|
| `tab:goodhart-landscape` | `experiments.tex:70` | ✅ |
| `tab:beta01-3seed` | `appendix.tex:326` | ✅ (`experiments.tex:38,77`, `appendix.tex:102`) |
| `tab:prolog-crosslogic` | `appendix.tex:378` | ✅ (`experiments.tex:94`, `appendix.tex:143`) |
| `tab:hacking-taxonomy-app` | `appendix.tex:144` | ✅ (`experiments.tex:13`) |
| `tab:hyperparams` | `appendix.tex:13` | ✅ (`appendix.tex:6`) |
| `fig:sta-overview` | `method.tex:8` | ✅ (`introduction.tex:13` via `\autoref`, `method.tex` body) |
| `fig:isr-collapse` | `experiments.tex:25` | ✅ (`experiments.tex:29`) |
| `fig:hacking-composition` | `experiments.tex:106` | ✅ (`experiments.tex:77,111`) |
| `fig:prolog-comparison` | `appendix.tex:412` | ❌ **never referenced** (P1-1) |

---

## Compile log

```
pdflatex 1 → bibtex → pdflatex 2 → pdflatex 3 → pdflatex 4
Output: main.pdf, 14 pages, 510 KB.
Errors: 0
Undefined citations: 6 (see P0-1)
Undefined references: 0
Multiply-defined labels: 0 (the duplicate \label cases use unique key names so no clash)
Underfull/Overfull: cosmetic only
```

---

## Page-count estimate

Based on `main.log` shipout markers:

- **Pages 1–6**: title, abstract, introduction, related work, method, experiments, conclusion (=Discussion+Conclusion), limitations
- **Pages 7–8**: references
- **Pages 9–14**: appendix (with Fig 4 on page 12)

**Main body = 6 pages.** ACL/EMNLP main limit is 8 pages excluding references and appendix → ~2 pages of headroom available for any expansion the reviewers request. References+appendix have no page limit.

---

## Action checklist (in order)

1. **[P0]** Add the 6 missing `.bib` entries → re-run full compile chain → verify zero undefined-citation warnings.
2. **[P1]** Add `\ref{fig:prolog-comparison}` callout in `appendix.tex` near line 421.
3. **[P1]** Drop duplicate `\label`s in two appendix tables.
4. **[P1]** Decide on `math-shepherd` (cite or remove).
5. **[P1]** Delete legacy `paper.tex` and its stale build artifacts.
6. **[P2]** Optional: clean up unused section labels.
7. Final compile & spot-check of generated PDF (visual inspection of figures, tables, citation rendering).
