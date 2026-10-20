# Figure Audit Report

Date: 2026-05-15

## Summary

Paper contains **3 custom figures** (excluding ACL template examples). All files exist and contain valid, publication-quality content.

## `\includegraphics` Inventory

| # | File | Location in Paper | Exists | Size | Quality |
|---|------|-------------------|--------|------|---------|
| 1 | `figures/paper/fig_pipeline.pdf` | `sections/method.tex:10` (Figure 1) | YES | 44K (PDF) / 219K (PNG) | Good — three-panel system overview (Data Preparation → Weak Supervision → Detection Methods), clean layout, readable text |
| 2 | `figures/paper/fig_data_scaling.pdf` | `sections/experiments.tex:139` (Figure 2) | YES | 17K (PDF) / 93K (PNG) | Good — line plot with data annotations, 3 methods (RF, GB, Probe), clear legend and axis labels |
| 3 | `figures/paper/fig_lf_temporal.pdf` | `sections/experiments.tex:179` (Figure 3) | YES | 31K (PDF) / 167K (PNG) | Good — bar chart comparing LF temporal roles across SWE-Agent and OpenHands, role reversal annotation included |

## Cross-reference Check

All `Figure~\ref{fig_*}` references in the paper resolve to existing `\label` + `\includegraphics` pairs:

- `\ref{fig:pipeline}` → `method.tex` (referenced in `introduction.tex:19`, `method.tex:6`)
- `\ref{fig:data_scaling}` → `experiments.tex` (referenced in `experiments.tex:132`)
- `\ref{fig:lf_temporal}` → `experiments.tex` (referenced in `experiments.tex:148`)

No orphan references. No figures defined but never referenced.

## Appendix / Analysis Sections

`sections/appendix.tex` and `sections/analysis.tex` contain **no `\includegraphics` or `\ref{fig}` references**. All appendix results are presented as tables only.

## Potentially Missing Figures (from task brief)

| Topic | Status | Assessment |
|-------|--------|------------|
| Data scaling curve | PRESENT | `fig_data_scaling.pdf` — covers this exactly |
| Temporal dynamics (LF) | PRESENT | `fig_lf_temporal.pdf` — covers this exactly |
| Feature overlap visualization | NOT IN PAPER | Not referenced in any tex file. The paper discusses feature importance via text + tables (cmd_rep ablation in experiments.tex). Could add a feature importance heatmap or Venn diagram of LF overlap, but not required for current framing |
| Pipeline overview figure | PRESENT | `fig_pipeline.pdf` — covers this exactly |
| Cross-agent transfer comparison | NOT IN PAPER | Transfer results are in Table 2 (main results). A grouped bar chart comparing SWE-Agent vs OpenHands per method could be useful but the table is dense enough to convey the story |

## Generation Scripts

All figures have corresponding generation scripts in `figures/paper/`:
- `gen_fig_pipeline.py` (9.6K)
- `gen_fig_data_scaling.py` (2.5K)
- `gen_fig_lf_temporal.py` (3.9K)

## Verdict

**No action required.** All referenced figures exist, are non-empty, contain correct publication-quality content matching their captions, and have reproducible generation scripts. No broken references.

The two "potentially missing" topics (feature overlap visualization, cross-agent transfer comparison) are adequately covered by tables in the current paper and would be optional additions rather than gaps.
