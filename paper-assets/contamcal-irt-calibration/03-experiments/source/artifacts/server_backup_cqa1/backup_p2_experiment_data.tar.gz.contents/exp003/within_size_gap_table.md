# Within-Size Aligned vs Para Gap Analysis (exp_003)

Controls for model-size confound by comparing d000 vs d100 within the same model size.
Only 1.5B and 3B have both d000 and d100 data points.

Gap = para_aligned accuracy - aligned accuracy (negative means para > aligned).

| Model Size | Dosage | Aligned Acc (%) | Para Acc (%) | Gap (para-aligned, pp) | N seeds |
|-----------|--------|-----------------|--------------|----------------------|---------|
| 1.5B      | d000   |           58.90 |        61.04 |                -2.14   |       2 |
| 1.5B      | d005   |           58.96 |        61.52 |                -2.56   |       2 |
| 1.5B      | d025   |           59.35 |        61.61 |                -2.26   |       2 |
| 1.5B      | d100   |           59.86 |        62.71 |                -2.85   |       2 |
| 3B        | d000   |           63.17 |        64.90 |                -1.73   |       2 |
| 3B        | d005   |           63.42 |        65.02 |                -1.59   |       2 |
| 3B        | d025   |           63.15 |        65.41 |                -2.26   |       2 |
| 3B        | d100   |           63.42 |        65.94 |                -2.52   |       2 |

### Contamination-attributable gap shift (d100 gap - d000 gap)

- **1.5B**: d100 gap (-2.85) - d000 gap (-2.14) = **-0.71 pp**
- **3B**: d100 gap (-2.52) - d000 gap (-1.73) = **-0.80 pp**
