# Table 2 (Scaling Analysis) — Variance Basis

## Answer

**Table 2 has no error bars.** It reports raw per-seed accuracy values from two **training seeds** (42, 123) and their arithmetic mean.

## Evidence

### Table structure
- Columns: `Method | Size | s42 | s123 | Mean | Δ 4B→8B`
- No ± notation anywhere in the table
- "Mean" = simple arithmetic average of two seed values

### Training seeds used
- Seeds 42 and 123, both trained in full bfloat16 precision (controlled comparison)
- Source: experiments.tex §3.3: "two matched seeds (42, 123), all trained in full bfloat16 precision to ensure a controlled comparison"

### Registry verification
Values in Table 2 match individual-seed experiment records exactly:

| Method | Size | s42 (registry) | s123 (registry) | Table Mean |
|--------|------|-----------------|------------------|------------|
| CLS    | 4B   | 87.83 (multi-seed-core) | 89.52 (multi-seed-core) | 88.68 |
| CLS    | 8B   | 90.48 (model-size-scaling-cls8b) | 89.40 (cls8b-seed123) | 89.94 |
| CWM    | 4B   | 87.51 (cwm-baseline) | 87.20 (cwm-seed123) | 87.36 |
| CWM    | 8B   | 87.67 (model-size-scaling-cwm8b) | 86.98 (cwm8b-seed123) | 87.33 |
| Traj   | 4B   | 85.27* | 86.72* | 86.00 |
| Traj   | 8B   | 87.60 (qwen3-8b-traj-func-s42) | 87.79 (qwen3-8b-traj-func-s123) | 87.70 |

### Bootstrap in surrounding text
The clustered bootstrap mentioned after Table 2 ("3-seed superset, p = 0.0066, 95% CI [1.80, 2.71]") tests whether the CLS–CWM gap widening from 4B to 8B is statistically significant. This is a **separate statistical test**, not an error bar for Table 2 values.

## Reviewer Q5 response draft

> Table 2 reports individual accuracy values for each of two training seeds (42, 123) along with their arithmetic mean. There are no error bars in this table; the per-seed values are shown directly. The clustered bootstrap analysis (p = 0.0066) referenced in the text tests the significance of the CLS–CWM gap widening and uses a 3-seed superset (42, 123, 456) with 10K resamples over 114 problem clusters, consistent with the statistical methodology described in §3.1.
