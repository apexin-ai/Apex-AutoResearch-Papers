# analysis n3 fold std bootstrap

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n3_fold_std_bootstrap_20260515T110542_result.json`
- **Structured JSON:** [`1d9e394f29d05fb71e0c.json`](../../sessions/1d/1d9e394f29d05fb71e0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part A: 9-cell RF 5-fold CV (mean_acc ± std)

| Cell | Accuracy | d0v1 AUC | d1v2 AUC | d2v3 AUC |
|------|----------|----------|----------|----------|
| pythia_nucleus095 | 78.68 ± 0.64 | 0.9965 ± 0.0010 | 0.8714 ± 0.0059 | 0.8117 ± 0.0089 |
| pythia_temp09 | 76.74 ± 0.87 | 0.9953 ± 0.0012 | 0.8421 ± 0.0107 | 0.7951 ± 0.0095 |
| pythia_topk50 | 68.84 ± 0.36 | 0.9904 ± 0.0021 | 0.7552 ± 0.0104 | 0.6913 ± 0.0113 |
| gpt2xl_nucleus095 | 84.11 ± 0.40 | 0.9930 ± 0.0016 | 0.9153 ± 0.0048 | 0.8890 ± 0.0047 |
| gpt2xl_temp09 | **85.86 ± 0.20** | 0.9965 ± 0.0005 | 0.9413 ± 0.0052 | 0.8855 ± 0.0062 |
| gpt2xl_topk50 | 75.93 ± 0.81 | 0.9903 ± 0.0021 | 0.8402 ± 0.0114 | 0.7612 ± 0.0150 |
| olmo_nucleus095 | 78.92 ± 0.39 | 0.9838 ± 0.0018 | 0.8712 ± 0.0099 | 0.8181 ± 0.0072 |
| olmo_temp09 | 82.12 ± 0.77 | 0.9954 ± 0.0016 | 0.8986 ± 0.0085 | 0.8347 ± 0.0087 |
| olmo_topk50 | 74.49 ± 0.71 | 0.9940 ± 0.0020 | 0.8226 ± 0.0088 | 0.7372 ± 0.0116 |

Fold-level std 范围 0.20%–0.87%，非常稳定。

### Part B: Bootstrap significance (Pythia nucleus, 1000 iterations)

| Comparison | Diff | 95% CI | p-value | Sig |
|------------|------|--------|---------|-----|
| RF vs CORAL | +0.60pp | [+0.01, +1.16] | 0.048 | * |
| RF vs DivEye | +0.50pp | [−0.09, +1.06] | 0.096 | ns |
| RF vs CE-MLP | +3.77pp | [+3.18, +4.33] | <0.001 | *** |

RF 显著优于 CE-MLP (p<0.001)，边际显著优于 CORAL (p=0.048)，与 DivEye 无显著差异 (p=0.096)。

产出文件已保存：
- `results/n3_fold_metrics.json`
- `results/n3_bootstrap_significance.json`

---
