# Figure Quality Audit — v14

## Summary
- Total figures: 25 (Figures 1–5 in main paper, Figures 6–25 in appendix)
- Issues found: 8 (critical: 1, minor: 7)

**Critical**: 21 Type 3 font instances across 9 pages, affecting 14 figures. Most ML venues (NeurIPS, ICML, ICLR, CoRL) reject PDFs containing Type 3 fonts.

---

## Per-Figure Results

### Figure 1 (page 2): Analysis Framework
- Font size: ✓ — All labels ≥8pt; panel titles, box text, and annotations readable
- Resolution: ✓ — Vector diagram, clean rendering
- Color accessibility: ✓ — Blue/orange/green/purple palette, no red-green conflict
- Legend clarity: ✓ — Panel labels (a)(b)(c) clear, internal labels present
- Axis labels: N/A (diagram)
- Type 3 fonts: ✓ — No Type 3 fonts on page 1–2

### Figure 2 (page 5): Cross-architecture evaluation matrix
- Font size: ✗ — Cell values (~7pt) are borderline; row/column headers adequate
- Resolution: ✓ — Vector heatmap
- Color accessibility: ✓ — Blue gradient scale; red borders structurally distinct
- Legend clarity: ✓ — "Trained"/"Reference" sections clearly labeled; gray = missing
- Axis labels: ✓ — Architecture and task names labeled
- Type 3 fonts: ✗ — **3 Type 3 fonts detected on page 5**

### Figure 3 (page 6): Layer-wise action-probe ΔP (LIBERO-Goal, readout token)
- Font size: ✓ — Axis labels, tick values, legend text all ≥8pt
- Resolution: ✓ — Vector line plots
- Color accessibility: ✓ — Solid vs dashed lines with distinct colors
- Legend clarity: ✓ — Legend entries clearly labeled in each panel
- Axis labels: ✓ — x: layer index, y: ΔP, both labeled
- Type 3 fonts: ✓ — No Type 3 fonts on page 6

### Figure 4 (page 7): Counterfactual sensitivity across architectures
- Font size: ✗ — Single-column figure with many conditions; some bar labels and condition names ~7pt
- Resolution: ✓ — Vector bar charts
- Color accessibility: ✓ — Distinct hues for each condition
- Legend clarity: ✓ — Condition names present
- Axis labels: ✓ — Present with metric names
- Type 3 fonts: ✓ — No Type 3 fonts on page 7

### Figure 5 (page 8): L1 instruction-domain head counts (trained vs. reference)
- Font size: ✓ — Architecture names and axis labels ≥8pt
- Resolution: ✓ — Vector bar charts
- Color accessibility: ✓ — Distinct bar colors; blue dominant palette
- Legend clarity: ✓ — Clear legend with architecture/condition labels
- Axis labels: ✓ — Present
- Type 3 fonts: ✓ — No Type 3 fonts on page 8

### Figure 6 (page 16): Three similarity metrics (RSA, Linear CKA, RBF Kernel CKA)
- Font size: ✗ — Rotated x-axis labels are small (~7pt); panel titles and y-axis adequate
- Resolution: ✓ — Vector bar charts
- Color accessibility: ✓ — Multiple distinct hues
- Legend clarity: ✓ — Legend entries present
- Axis labels: ✓ — Panel titles include metric names; axes labeled
- Type 3 fonts: ✗ — **5 Type 3 fonts detected on page 16**

### Figure 7 (page 16): RSA with action space across representation sources
- Font size: ✓ — Bar labels and axis text adequate
- Resolution: ✓ — Vector bar chart
- Color accessibility: ✓ — Distinct colors
- Legend clarity: ✓ — Source labels present
- Axis labels: ✓ — Present
- Type 3 fonts: ✗ — **Shares page 16 Type 3 fonts (5 instances)**

### Figure 8 (page 17): Per-layer RSA (trained and reference models)
- Font size: ✓ — Axis labels and legend text ≥8pt
- Resolution: ✓ — Vector line plots
- Color accessibility: ✓ — Different line styles and colors
- Legend clarity: ✓ — Trained/reference clearly labeled
- Axis labels: ✓ — Layer index on x, RSA on y
- Type 3 fonts: ✗ — **1 Type 3 font detected on page 17**

### Figure 9 (pages 17–18): Per-layer action probe ΔP across training stages
- Font size: ✓ — Axis labels adequate; legend text ≥8pt
- Resolution: ✓ — Vector line plots
- Color accessibility: ✓ — Multiple line colors with distinct styles
- Legend clarity: ✗ — Many legend entries (5+ conditions); somewhat crowded but functional
- Axis labels: ✓ — Present
- Type 3 fonts: ✗ — **Shares page 17 Type 3 font**

### Figure 10 (page 18): Random-Subset Ablation (ΔP increase from ablating L1 heads)
- Font size: ✓ — Statistical annotations, axis labels all readable
- Resolution: ✓ — Vector scatter/line plot
- Color accessibility: ✓ — Few distinct colors
- Legend clarity: ✓ — Clear legend entries
- Axis labels: ✓ — Present with descriptive labels
- Type 3 fonts: ✓ — No Type 3 fonts on page 18

### Figure 11 (page 20): Dose-response gradient (Cohen's d vs. ablated heads)
- Font size: ✓ — Labels, annotations, error bars all readable
- Resolution: ✓ — Vector line plot
- Color accessibility: ✓ — Blue line + red dashed control (blue/red is colorblind-safe)
- Legend clarity: ✓ — Present
- Axis labels: ✓ — "Number of heads ablated" (x), "Cohen's d" (y)
- Type 3 fonts: ✓ — No Type 3 fonts on page 20

### Figure 12 (page 22): Pretrained LLM representation diagnostics under visual input
- Font size: ✓ — Multi-panel with adequate text sizes
- Resolution: ✓ — Vector line plots
- Color accessibility: ✓ — Distinct line colors
- Legend clarity: ✓ — Present
- Axis labels: ✓ — Present
- Type 3 fonts: ✗ — **1 Type 3 font detected on page 22**

### Figure 13 (page 22): Per-layer action probe ΔP (linear vs. MLP probes)
- Font size: ✓ — 4 conditions clearly labeled; legend text ≥8pt
- Resolution: ✓ — Vector line plots
- Color accessibility: ✓ — Different colors and line styles (solid/dashed)
- Legend clarity: ✓ — 4 entries, well-spaced
- Axis labels: ✓ — "Layer" (x), "Action R²" (y)
- Type 3 fonts: ✗ — **Shares page 22 Type 3 font**

### Figure 14 (page 23): Functional probe R² for action prediction
- Font size: ✓ — Bar labels and axis text adequate
- Resolution: ✓ — Vector bar chart
- Color accessibility: ✓ — Distinct colors
- Legend clarity: ✓ — Present
- Axis labels: ✓ — Present
- Type 3 fonts: ✗ — **4 Type 3 fonts detected on page 23**

### Figure 15 (page 23): (a) Peak Shift: Trained vs Untrained, (b) Instruction Content Control
- Font size: ✓ — Both panels have adequate text sizes
- Resolution: ✓ — Vector plots
- Color accessibility: ✓ — Blue/orange in (a), distinct colors in (b)
- Legend clarity: ✓ — Present in both panels
- Axis labels: ✓ — Present
- Type 3 fonts: ✗ — **Shares page 23 Type 3 fonts (4 instances)**

### Figure 16 (page 24): Cross-validation RSA/R² on LIBERO-Goal vs LIBERO-Spatial
- Font size: ✓ — Adequate text sizes
- Resolution: ✓ — Vector line plots
- Color accessibility: ✓ — Distinct conditions
- Legend clarity: ✓ — Present
- Axis labels: ✓ — Present
- Type 3 fonts: ✗ — **2 Type 3 fonts detected on page 24**

### Figure 17 (page 27): Label permutation control
- Font size: ✓ — Labels and annotations readable
- Resolution: ✓ — Vector bar chart with scatter overlay
- Color accessibility: ✗ — Uses red and green bars together; problematic for red-green colorblind readers (protanopia/deuteranopia)
- Legend clarity: ✓ — "Real data" vs "Shuffled labels" present
- Axis labels: ✓ — Present
- Type 3 fonts: ✓ — No Type 3 fonts on page 27

### Figure 18 (page 29): Cross-instruction 10-way classification accuracy
- Font size: ✓ — 3 conditions, adequate legend and axis text
- Resolution: ✓ — Vector line plot
- Color accessibility: ✓ — 3 distinct colors
- Legend clarity: ✓ — Present
- Axis labels: ✓ — "Layer" (x), accuracy (y)
- Type 3 fonts: ✗ — **1 Type 3 font detected on page 29**

### Figure 19 (page 30): Instruction-dominant head active layers (OpenVLA + Phi-3V)
- Font size: ✓ — Layer indices small but readable; legend text adequate
- Resolution: ✓ — Vector bar/line charts
- Color accessibility: ✓ — Trained/untrained/reference in distinct colors
- Legend clarity: ✓ — Present with condition labels
- Axis labels: ✓ — "Layer" (x), head counts (y)
- Type 3 fonts: ✓ — No Type 3 fonts on page 30

### Figure 20 (page 31): L1 instruction-dominant head fractions across three architectures
- Font size: ✓ — Architecture labels and bar values adequate
- Resolution: ✓ — Vector bar chart
- Color accessibility: ✓ — Distinct colors
- Legend clarity: ✓ — Present
- Axis labels: ✓ — Present
- Type 3 fonts: ✗ — **2 Type 3 fonts detected on page 31**

### Figure 21 (page 31): L1 attention from readout token across three conditions
- Font size: ✗ — Head index labels on x-axis are numerous and small (~6–7pt)
- Resolution: ✓ — Vector stacked bar chart
- Color accessibility: ✓ — Instruction/image/BOS categories in distinct colors
- Legend clarity: ✓ — 3 categories labeled
- Axis labels: ✓ — "Head Index" (x), attention fraction (y)
- Type 3 fonts: ✗ — **Shares page 31 Type 3 fonts (2 instances)**

### Figure 22 (page 32): Instruction-dominant heads and mean text attention fraction
- Font size: ✓ — Two-panel with adequate text
- Resolution: ✓ — Vector bar/line chart
- Color accessibility: ✓ — 3 conditions with distinct colors/markers
- Legend clarity: ✓ — Present
- Axis labels: ✓ — "Layer" (x), respective metrics (y)
- Type 3 fonts: ✗ — **2 Type 3 fonts detected on page 32**

### Figure 23 (page 39): ΔP across training pathways
- Font size: ✓ — Labels and legend adequate
- Resolution: ✓ — Vector line plot with shaded CIs
- Color accessibility: ✓ — Blue/orange/green lines
- Legend clarity: ✓ — 3 conditions clearly labeled
- Axis labels: ✓ — Present
- Type 3 fonts: ✓ — No Type 3 fonts on page 39

### Figure 24 (page 41): NLP fine-tuning controls produce flat R² profiles
- Font size: ✓ — Multi-panel bar charts, labels adequate
- Resolution: ✓ — Vector bar charts
- Color accessibility: ✓ — Distinct colors per panel
- Legend clarity: ✓ — Each panel titled
- Axis labels: ✓ — Present
- Type 3 fonts: ✓ — No Type 3 fonts on page 41

### Figure 25 (page 41): Claim-evidence-scope summary
- Font size: ✗ — Dense text in diagram cells; some cell content approaches ~7pt
- Resolution: ✓ — Vector diagram with clean text
- Color accessibility: ✓ — Colored section headers distinguish categories
- Legend clarity: N/A (structured diagram)
- Axis labels: N/A (structured diagram)
- Type 3 fonts: ✓ — No Type 3 fonts on page 41

---

## Issues Summary (sorted by severity)

### Critical

1. **[CRITICAL] Type 3 fonts in 14 figures across 9 pages** — 21 Type 3 font instances detected (pages 5, 16, 17, 22, 23, 24, 29, 31, 32). Affected figures: 2, 6, 7, 8, 9, 12, 13, 14, 15, 16, 18, 20, 21, 22. These are matplotlib-generated figures where font rendering falls back to bitmap Type 3 glyphs. Most ML venues (NeurIPS, ICML, ICLR, CoRL) explicitly reject PDFs with Type 3 fonts. **Fix**: Set `matplotlib.rcParams['pdf.fonttype'] = 42` and `matplotlib.rcParams['ps.fonttype'] = 42` before generating all figures, then re-export.

### Minor

2. **[MINOR] Figure 2 (p5): Small heatmap cell values** — Numeric values inside cells are ~7pt, borderline for print readability. Consider increasing figure width or font size in the heatmap annotation.
3. **[MINOR] Figure 4 (p7): Dense bar labels in single-column figure** — Condition names and some axis text approach ~7pt due to the figure being compressed into a single column. Consider making it a full-width figure or reducing the number of displayed conditions.
4. **[MINOR] Figure 6 (p16): Small rotated x-axis labels** — Rotated bar labels are ~7pt. Readable but tight. Consider abbreviating or increasing font size.
5. **[MINOR] Figure 9 (p17–18): Crowded legend** — 5+ training-stage conditions make the legend dense. Functional but could benefit from spacing or splitting into separate panels.
6. **[MINOR] Figure 17 (p27): Red-green color pair** — Uses red and green bars for real vs shuffled conditions, which is problematic for protanopia/deuteranopia (~8% of males). Consider blue/orange or add hatching patterns.
7. **[MINOR] Figure 21 (p31): Dense x-axis head indices** — Numerous individual head index labels (~6–7pt) on x-axis. Consider showing every Nth label or grouping.
8. **[MINOR] Figure 25 (p41): Dense diagram text** — Some cell content in the claim-evidence-scope summary approaches ~7pt. Consider increasing figure size or reducing text density.

---

## Recommendations

### Immediate (before submission)
1. **Eliminate all Type 3 fonts** — Add to matplotlib rc setup:
   ```python
   import matplotlib
   matplotlib.rcParams['pdf.fonttype'] = 42
   matplotlib.rcParams['ps.fonttype'] = 42
   ```
   Re-generate all 14 affected figures and recompile.

### Suggested (quality improvements)
2. Increase Figure 2 cell annotation font size from ~7pt to ≥8pt
3. Consider making Figure 4 full-width or reducing condition density
4. Replace red-green palette in Figure 17 with blue-orange or add texture/hatching
5. Thin x-axis tick labels in Figure 21 (show every 4th head index)
