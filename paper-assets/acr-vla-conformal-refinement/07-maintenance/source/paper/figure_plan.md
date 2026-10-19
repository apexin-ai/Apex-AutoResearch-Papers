# Figure and Table Plan — ACR-VLA CoRL 2026

---

## Main Paper Figures

### Fig. 1: Pipeline Overview (Method)
- **Type**: Architecture diagram
- **Content**: Full ACR-VLA pipeline: Frozen VLA → K=10 flow-matching samples → CGS nonconformity scoring → argmin selection → CRM correction → clipped action output
- **Subpanels**: Show obs_only / perdof / scalar conditioning paths branching into CRM
- **Data source**: N/A (schematic)
- **Key message**: Sample-then-correct is a two-stage pipeline; CRM is lightweight (~250K params, ~3ms)
- **Tools**: TikZ or matplotlib
- **Priority**: HIGH — needed for abstract figure

### Fig. 2: Object Benchmark Main Results (Results §4.2)
- **Type**: Grouped bar chart
- **Content**: 6 methods × success rate on object 10-task benchmark
- **Methods**: obs_only 0.1, argmin K=10, VLA-only K=1, VLA-mean K=10, perdof 0.1, scalar 0.1
- **Data source**: `eval-acr-object-v4-obs-only`, `eval-argmin-only-object`, `eval-vla-only-object-k1`, `eval-acr-object-v4-small`, `eval-acr-object-v4-scalar` (seed=42 FINAL)
- **Error bars**: Bootstrap CI from seed=42+43 combined (pending seed=43)
- **Annotations**: +7.0pp arrow from argmin to obs_only; significance stars if Fisher p < 0.05
- **Key message**: obs_only CRM is the only method that significantly improves over sample selection
- **Priority**: HIGH — headline figure

### Fig. 3: Spatial Benchmark (Honest Negative) (Results §4.3)
- **Type**: Grouped bar chart (same style as Fig. 2)
- **Content**: 6 methods × success rate on spatial 10-task benchmark
- **Data source**: `eval-acr-spatial-v4-obs-only-r3`, `eval-argmin-only-spatial-r2`, `eval-acr-spatial-v4-small-r2`, `eval-acr-spatial-v4-scalar` (LOCKED)
- **Key message**: No CRM variant helps on spatial — all within noise of argmin
- **Priority**: HIGH — honest negative, must present

### Fig. 4: Magnitude Sensitivity Curve (Results §4.4)
- **Type**: Line plot with two curves
- **Content**: X-axis = correction norm (0.03, 0.05, 0.1, 0.2, 0.3); Y-axis = success rate; two lines: obs_only (stable) vs perdof (declining)
- **Data source**: Magnitude sweep D032 — `eval-mag-obsonly-norm005`, `eval-mag-obsonly-norm02`, `eval-mag-perdof-norm03`, and additional sweep experiments
- **Shaded region**: ±1 SE or bootstrap CI
- **Annotations**: Mark norm=1.42 → 0% as catastrophic failure point (off-chart callout)
- **Key message**: obs_only is uniquely robust to correction magnitude; perdof collapses at high norm
- **Priority**: HIGH — key empirical contribution

### Fig. 5: Per-Task Breakdown Heatmap (Results §4.2)
- **Type**: Heatmap (10 tasks × 6 methods)
- **Content**: Per-task success rates on object benchmark, color-coded (green=high, red=low)
- **Data source**: Per-task logs from all object eval runs
- **Key message**: obs_only improvement is distributed across tasks, not driven by a single task
- **Priority**: MEDIUM — strengthens claim if space allows, else appendix

---

## Main Paper Tables

### Table 1: Object Benchmark Results (Results §4.2)
- **Type**: Results table
- **Content**: Method | SR (seed=42) | SR (seed=43) | Combined | Δ vs argmin | Fisher p-value
- **Rows**: obs_only 0.1, argmin K=10, VLA-only K=1, VLA-mean K=10, perdof 0.1, scalar 0.1
- **Data source**: All object eval exp_ids (see outline §4.2) + seed=43 (pending)
- **Key message**: obs_only is statistically significantly better than all other methods
- **Priority**: HIGH

### Table 2: Spatial Benchmark Results (Results §4.3)
- **Type**: Results table (compact)
- **Content**: Method | SR (10-task)
- **Data source**: Spatial LOCKED results
- **Key message**: All methods within noise — presented as honest negative
- **Priority**: HIGH

### Table 3: Magnitude Sweep (Results §4.4)
- **Type**: Table (alternative to or supplementing Fig. 4)
- **Content**: norm | obs_only SR | perdof SR | Δ
- **Data source**: D032 magnitude sweep
- **Priority**: MEDIUM (Fig. 4 may suffice)

---

## Supplementary / Appendix Figures

### Fig. S1: CRM Training Loss Curves
- **Type**: Line plot
- **Content**: Training and validation L2 loss for obs_only, perdof, scalar CRM variants
- **Data source**: CRM training logs
- **Key message**: All variants converge; perdof's lower training loss doesn't translate to closed-loop performance

### Fig. S2: Per-Task Object Breakdown (Full Table)
- **Type**: Table
- **Content**: 10 tasks × 6 methods × 2 seeds, individual success counts
- **Data source**: All object eval runs
- **Priority**: Required for reviewer scrutiny

### Fig. S3: Correction Norm Distribution
- **Type**: Histogram / violin plot
- **Content**: Distribution of actual correction magnitudes ||δ|| produced by obs_only vs perdof CRM before clipping
- **Data source**: Inference logs from eval runs
- **Key message**: perdof produces larger raw corrections → more aggressive clipping → less stable behavior

### Fig. S4: Conformal Score Distribution
- **Type**: Histogram
- **Content**: Distribution of CGS nonconformity scores across K=10 samples
- **Data source**: Inference logs
- **Key message**: Conformal selection stage effectively identifies better samples (lower nonconformity ↔ closer to calibration distribution)

### Fig. S5: Compute Overhead Analysis
- **Type**: Table or bar chart
- **Content**: Inference time breakdown: VLA forward pass × K, CGS scoring, CRM correction
- **Data source**: Timing logs
- **Key message**: CRM adds ~3ms overhead; K=10 sampling is the dominant cost (same as ReconVLA)

---

## Production Notes

- All figures use consistent color scheme: obs_only = blue, argmin = gray, perdof = orange, scalar = green, VLA-only = light gray, VLA-mean = dark gray
- Error bars: bootstrap 95% CI where available, otherwise ±1 SE
- Font size ≥ 8pt for CoRL readability
- All bar charts include numerical labels on bars
- Seed=43 results will be added when available — figures designed to accommodate 2-seed data
