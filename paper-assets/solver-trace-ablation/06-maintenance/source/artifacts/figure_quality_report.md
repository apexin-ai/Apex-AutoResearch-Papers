# Figure Quality Report — EMNLP 2026 Submission Readiness

**Date**: 2026-05-14 (updated)  
**Files audited**: `paper/figures/{fig1_sta_overview,fig2_isr_collapse,fig3_hacking_composition,fig4_prolog_comparison}.pdf`  
**Target venue**: EMNLP 2026 (ACL format, 2-column, `\columnwidth`=3.3in, `\textwidth`=6.75in)

---

## Verdict

| Figure | Status | Blocking Issues |
|--------|--------|-----------------|
| fig1_sta_overview | **FAIL → FIXED** | Text unreadable (2.6pt effective); needs `figure*` |
| fig2_isr_collapse | **FAIL → FIXED** | Text unreadable (3.5pt effective); oversized for single column |
| fig3_hacking_composition | **FAIL → FIXED** | Text unreadable (2.4pt effective); needs `figure*`; duplicate `\label` |
| fig4_prolog_comparison | **FAIL → FIXED** | Text unreadable (2.3pt effective); needs `figure*` |

---

## CRITICAL Issues Found

### C1. All figures have unreadable text after LaTeX scaling

Every figure was generated at matplotlib `figsize` much wider than its LaTeX target. When scaled to `\columnwidth` (3.3in), fonts shrink below ACL minimum (8pt).

| Figure | Natural Width | LaTeX Target | Scale | Smallest Font → Effective |
|--------|--------------|-------------|-------|--------------------------|
| fig1 | 11.63in | 3.13in | 0.27× | 9.5pt → **2.6pt** |
| fig2 | 6.77in | 3.13in | 0.46× | 7.5pt → **3.5pt** |
| fig3 | 9.77in | 2.97in | 0.30× | 8.0pt → **2.4pt** |
| fig4 | 10.02in | 3.30in | 0.33× | 7.0pt → **2.3pt** |

**Fix applied**: Regenerated all figures at target dimensions with ≥ 8pt fonts.

### C2. fig1, fig3, fig4 placed in single-column `figure` but are multi-panel layouts

These wide panoramic layouts cannot render legibly at 3.3in column width.

**Fix applied**: Updated LaTeX to `\begin{figure*}[t]` with `width=\textwidth`.

### C3. fig4 has two generation scripts with conflicting data

| Seed | `figures/paper/gen_fig4.py` (old) | `paper/figures/gen_fig4.py` (canonical) | Delta |
|------|----------------------------------|-----------------------------------------|-------|
| s44 Prolog ISR* | 0.081 | 0.387 | **+0.306 (4.8×)** |

**Status**: Old script is stale. Canonical script data used for regeneration. **User must verify s44 Prolog ISR* against eval_sta.py before submission.**

---

## MODERATE Issues

### M1. fig2 missing step-0 data point
Task specification lists 4 checkpoints (PR=0.12/0.32/0.93/0.96, ISR=0.064/0.642/0.132/0.003). Figure only has 3 (steps 100/500/1000). Step-0 baseline (PR=0.12, ISR=0.064) omitted.
**Status**: Not added — requires user confirmation of step-0 data.

### M2. fig3 duplicate `\label{fig:hacking-composition}`
Present in both `experiments.tex:106` and `appendix.tex:150`.
**Fix applied**: Appendix copy uses `fig:hacking-composition-app`.

### M3. fig3 ISR β=0.1 s42 Genuine discrepancy
Figure shows 32.1%, appendix table shows 30.9%. 1.2pp difference.
**Status**: Not changed — requires user decision on canonical value.

---

## Passing Checks

| Check | Status |
|-------|--------|
| Vector graphics (not rasterized) | ✅ Matplotlib PDF backend — pure vector |
| Font embedding (pdf.fonttype=42) | ✅ TrueType outlines — ACL-compliant |
| Colorblind-safe palette | ✅ Okabe-Ito colors throughout |
| Captions in .tex (not in figures) | ✅ |
| File sizes reasonable | ✅ 33–37 KB |
| fig2 data accuracy (3 points) | ✅ PR/ISR values match |
| fig3 bars sum to 100% | ✅ All 7 conditions |
| fig4 right panel gaming modes | ✅ 3/3 seeds 100% gaming |

---

## Fixes Applied

### Dimension fixes

| Figure | Before | After | LaTeX env |
|--------|--------|-------|-----------|
| fig1 | figsize=(14, 4.5) | figsize=(6.75, 2.8) | `figure*` + `\textwidth` |
| fig2 | figsize=(7, 6) | figsize=(3.25, 4.5) | `figure` + `\columnwidth` |
| fig3 | figsize=(10, 5) | figsize=(6.75, 3.3) | `figure*` + `\textwidth` |
| fig4 | figsize=(10, 4.5) | figsize=(6.75, 3.0) | `figure*` + `\textwidth` |

### Font sizes (all ≥ 8pt at natural size)
- Title: 10pt
- Axis labels: 9pt  
- Tick labels: 8pt
- Annotations/legends: 8pt
- Minimum: 8pt

### LaTeX changes
- `method.tex`: `figure` → `figure*`, width → `\textwidth`
- `experiments.tex`: fig3 `figure` → `figure*`, width → `\textwidth`
- `appendix.tex`: fig3 label → `fig:hacking-composition-app`, fig4 `figure` → `figure*`, width → `\textwidth`

---

## Remaining User Actions

1. **[VERIFY]** fig4 Prolog s44 ISR* = 0.387 against eval_sta.py output
2. **[DECIDE]** Add step-0 baseline to fig2? (PR=0.12, ISR=0.064)
3. **[DECIDE]** fig3 ISR β=0.1 s42 Genuine: 32.1% or 30.9%?
4. **[CLEANUP]** Delete `figures/paper/gen_fig4.py` (stale data)
