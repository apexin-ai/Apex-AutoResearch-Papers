# CLS Multi-Seed Summary (Table 3 Data)

Generated: 2026-05-20

## Per-Seed Results

### Qwen3-8B CLS (repo-level, n=3)

| Seed | Accuracy | F1_macro | F1_fail | F1_pass |
|------|----------|----------|---------|---------|
| s42 | 84.48 | 78.17 | 66.43 | 89.91 |
| s123 | 85.60 | 78.38 | 65.89 | 90.87 |
| s456 | 84.40 | 76.19 | 62.21 | 90.17 |

### DeepSeek-Coder-6.7B CLS (repo-level, n=2)

| Seed | Accuracy | F1_macro | F1_fail | F1_pass |
|------|----------|----------|---------|---------|
| s42 | 82.61 | 75.07 | 61.35 | 88.78 |
| s456 | 86.15 | 80.43 | 69.84 | 91.01 |
| ~~s123~~ | 74.93 | — | — | — | *(excluded: config confound)* |

### Qwen3-8B TRAJ baseline (repo-level, n=3)

| Seed | Accuracy | F1_macro | F1_fail | F1_pass |
|------|----------|----------|---------|---------|
| s42 | 72.92 | 72.90 | — | — |
| s123 | 77.08 | 76.59 | 73.17 | 80.00 |
| s456 | 70.83 | 70.63 | 73.08 | 68.18 |

### Majority Baseline: 72.96% (predict all pass)

## Aggregated Statistics (mean ± std)

| Model | Formulation | n | Accuracy | F1_macro | F1_fail | F1_pass |
|-------|-------------|---|----------|----------|---------|---------|
| Qwen3-8B | CLS | 3 | 84.83 ± 0.67 | 77.58 ± 1.21 | 64.84 ± 2.30 | 90.32 ± 0.50 |
| DeepSeek-6.7B | CLS | 2 | 84.38 ± 2.50 | 77.75 ± 3.79 | 65.59 ± 6.00 | 89.90 ± 1.58 |
| Qwen3-8B | TRAJ | 3 | 73.61 ± 3.18 | 73.37 ± 3.01 | 73.12 ± 0.06† | 74.09 ± 8.36† |
| — | Majority | — | 72.96 | — | — | — |

†TRAJ F1_fail/F1_pass: n=2 (s42 per-class F1 not in registry)

## 95% Confidence Intervals

| Model | Formulation | n | t_crit | Accuracy CI | F1_macro CI |
|-------|-------------|---|--------|-------------|-------------|
| Qwen3-8B | CLS | 3 | 4.303 | [83.16, 86.50] | [74.58, 80.58] |
| DeepSeek-6.7B | CLS | 2 | 12.706 | [61.89, 106.87] | [43.70, 111.80] |
| Qwen3-8B | TRAJ | 3 | 4.303 | [65.71, 81.51] | [65.90, 80.84] |

## CLS vs TRAJ Gap (Qwen3-8B)

- Accuracy gap: 11.22 pp (84.83 − 73.61)
- F1_macro gap: 4.21 pp (77.58 − 73.37)

## LaTeX-Ready (copy-paste for Table 3)

```
Qwen3-8B CLS & 3 & 84.8$\pm$0.7 & 77.6$\pm$1.2 & 64.8$\pm$2.3 & 90.3$\pm$0.5 \\
DeepSeek-6.7B CLS & 2 & 84.4$\pm$2.5 & 77.8$\pm$3.8 & 65.6$\pm$6.0 & 89.9$\pm$1.6 \\
Qwen3-8B TRAJ & 3 & 73.6$\pm$3.2 & 73.4$\pm$3.0 & — & — \\
Majority & — & 73.0 & — & — & — \\
```
