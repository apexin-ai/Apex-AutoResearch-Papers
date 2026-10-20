# TracVLA Trained Metrics (2026-05-21)
## ⚠️ C001: Untrained data MISSING for both. Numbers only, NO conclusions.

## TracVLA SPATIAL (tracvla_spatial_full_v2) — TRAINED

### R² Probing (Ridge)
| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0    | 0.8059    | 0.6656         |
| L4    | 0.8091    | 0.7954         |
| L8    | 0.8134    | 0.7908         |
| L12   | 0.8231    | 0.7980         |
| L16   | 0.8311    | 0.8035         |
| L20   | 0.8310    | 0.7981         |
| L24   | 0.8169    | 0.7463         |
| L28   | 0.8223    | 0.6150         |
| L31   | 0.7907    | 0.6712         |
| PEAK  | 0.8347@L19| 0.8090@L17     |

### L1 Attention Profile
- 30/32 heads instruction-dominant
- Top: head_8(0.945), head_26(0.913), head_19(0.903)
- Bottom: head_13(0.45), head_22(0.474)

### Cross-Instruction Classification (10-way)
- L0 image_mean: 1.0, L0 last_preaction: 0.923
- L1+ all positions: 1.0

### Counterfactual (Cohen's d ranking)
| Condition    | Cohen's d | MSE    |
|-------------|-----------|--------|
| empty       | 1.3268    | 0.1072 |
| shuffled    | 1.2947    | 0.0937 |
| paraphrased | 1.1825    | 0.0715 |
| wrong       | 1.1724    | 0.0795 |

---

## TracVLA OBJECT (tracvla_object_full_v1) — TRAINED

### R² Probing (Ridge)
| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0    | 0.7458    | 0.6214         |
| L4    | 0.7531    | 0.7290         |
| L8    | 0.7562    | 0.7506         |
| L12   | 0.7589    | 0.7418         |
| L16   | 0.7687    | 0.7544         |
| L20   | 0.7728    | 0.7354         |
| L24   | 0.7620    | 0.6605         |
| L28   | 0.7661    | 0.5039         |
| L31   | 0.7483    | 0.4699         |
| PEAK  | 0.7757@L22| 0.7636@L9      |

### L1 Attention Profile
- 30/32 heads instruction-dominant
- Top: head_8(0.939), head_26(0.920), head_19(0.901)
- Bottom: head_13(0.472), head_22(0.472)

### Cross-Instruction Classification (10-way)
- L0 image_mean: 1.0, L0 last_preaction: 0.858
- L1+ all positions: 1.0

### Counterfactual (Cohen's d ranking)
| Condition    | Cohen's d | MSE    |
|-------------|-----------|--------|
| empty       | 1.2117    | 0.1359 |
| shuffled    | 1.1643    | 0.1061 |
| wrong       | 1.0595    | 0.0948 |
| paraphrased | 0.9711    | 0.0925 |
