# ssh w7 backup and analyze

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w7_backup_and_analyze_20260523T011207_result.json`
- **Structured JSON:** [`af549be221fd7bffdd61.json`](../../sessions/af/af549be221fd7bffdd61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

```
Backup: OK (81 lines confirmed, seed 0-19 complete)
Rerun process: KILLED
Analysis exit: SUCCESS
```

### Wilcoxon Tests (20 seeds)

| Metric | Variant | Full med | Var med | Δ median | W | p | Sig |
|--------|---------|----------|---------|----------|---|---|-----|
| θ RMSE | No Severity | 0.1240 | 0.1285 | +0.0018 | 73 | 2.45e-01 | n.s. |
| θ RMSE | Binary Gate | 0.1240 | 0.1391 | +0.0123 | 1 | 3.81e-06 | *** |
| θ RMSE | Staged Est. | 0.1240 | 0.2595 | +0.1258 | 0 | 1.91e-06 | *** |
| c RMSE | No Severity | 0.5379 | 0.5774 | +0.0412 | 14 | 2.10e-04 | *** |
| c RMSE | Binary Gate | 0.5379 | 0.7672 | +0.2461 | 0 | 1.91e-06 | *** |
| c RMSE | Staged Est. | 0.5379 | 1.4037 | +0.7510 | 0 | 1.91e-06 | *** |
| θ τ | No Severity | 0.9233 | 0.9224 | -0.0016 | 64 | 3.44e-01 | n.s. |
| θ τ | Binary Gate | 0.9233 | 0.9078 | -0.0106 | 12 | 5.15e-04 | *** |
| θ τ | Staged Est. | 0.9233 | 0.8482 | -0.0751 | 0 | 8.84e-05 | *** |

### Variant Summary (mean ± std)

| Variant | θ_RMSE | c_RMSE | θ_τ | n |
|---------|--------|--------|-----|---|
| **Full G-MFRM** | 0.1243±0.0164 | 0.5933±0.2242 | 0.9224±0.0097 | 20 |
| No Severity | 0.1266±0.0160 | 0.6292±0.2425 | 0.9216±0.0097 | 20 |
| Binary Gate | 0.1371±0.0161 | 0.8326±0.2257 | 0.9093±0.0140 | 20 |
| Staged Est. | 0.2539±0.0448 | 1.3823±0.1635 | 0.8393±0.0349 | 20 |

### Generated files

| File | Size |
|------|------|
| ablation_boxplots.pdf | 21 KB |
| ablation_boxplots.png | 151 KB |
| theta_tau_boxplot.pdf | 18 KB |
| theta_tau_boxplot.png | 96 KB |
| wilcoxon_tests.csv | 1.3 KB |

**关键发现**：No Severity 在 θ RMSE 和 θ τ 上与 Full G-MFRM 无显著差异（p=0.25, p=0.34），但 c RMSE 显著恶化（p=2.1e-4）。Binary Gate 和 Staged Est. 在所有指标上均显著劣于 Full G-MFRM（p<0.001）。

---
