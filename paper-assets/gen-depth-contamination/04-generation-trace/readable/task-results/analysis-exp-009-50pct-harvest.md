# analysis exp 009 50pct harvest

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009_50pct_harvest_20260517T101851_result.json`
- **Structured JSON:** [`795540b57a3aef82d0c4.json`](../../sessions/79/795540b57a3aef82d0c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果如下：

---

## exp-009 v3 ratio_50 完整结果

**状态**: 15/15 文件全部到齐（含 graduated_seed4，17:23 完成）

### Table 1: Mean±Std

| Strategy | MMLU | HellaSwag |
|----------|------|-----------|
| no_filter | 0.6063±0.0013 | 0.6680±0.0005 |
| binary_ours | 0.6088±0.0011 | 0.6731±0.0004 |
| graduated | 0.6062±0.0009 | 0.6679±0.0002 |

### Table 2: Paired t-test

| Comparison | ΔMMLU | p(MMLU) | ΔHellaSwag | p(HellaSwag) |
|---|---|---|---|---|
| binary_ours vs no_filter | +0.0025 | 0.0377* | +0.0051 | 0.00002*** |
| graduated vs no_filter | -0.0001 | 0.890 | -0.0001 | 0.706 |
| graduated vs binary_ours | -0.0026 | 0.0257* | -0.0052 | 0.00003*** |

### Table 3: Raw Data

| Strategy | Seed | MMLU | HellaSwag |
|---|---|---|---|
| binary_ours | 0 | 0.6092 | 0.6733 |
| binary_ours | 1 | 0.6076 | 0.6729 |
| binary_ours | 2 | 0.6085 | 0.6725 |
| binary_ours | 3 | 0.6104 | 0.6737 |
| binary_ours | 4 | 0.6083 | 0.6732 |
| graduated | 0 | 0.6068 | 0.6680 |
| graduated | 1 | 0.6070 | 0.6680 |
| graduated | 2 | 0.6068 | 0.6679 |
| graduated | 3 | 0.6053 | 0.6676 |
| graduated | 4 | 0.6051 | 0.6679 |
| no_filter | 0 | 0.6064 | 0.6680 |
| no_filter | 1 | 0.6082 | 0.6681 |
| no_filter | 2 | 0.6045 | 0.6678 |
| no_filter | 3 | 0.6067 | 0.6688 |
| no_filter | 4 | 0.6058 | 0.6673 |

### 关键发现

- **binary_ours 显著优于 no_filter**: MMLU +0.25pp (p=0.038), HellaSwag +0.51pp (p<0.001)
- **graduated ≈ no_filter**: 两个指标差异均无统计显著性 (p>0.7)
- **binary_ours 显著优于 graduated**: 效果差异与 binary_ours vs no_filter 对称

结论：在 50% 污染比例下，binary_ours 策略有效保护了模型性能，而 graduated 策略未展现优势（表现等同于不过滤）。

已保存至: `/root/autodl-tmp/gen-depth-contamination/artifacts/exp009_v3_ratio_50_final.json`

---
