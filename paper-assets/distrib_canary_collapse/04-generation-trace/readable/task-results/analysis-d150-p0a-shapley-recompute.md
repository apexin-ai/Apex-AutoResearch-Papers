# analysis d150 p0a shapley recompute

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d150_p0a_shapley_recompute_20260520T134235_result.json`
- **Structured JSON:** [`581630bde730cfa5bca7.json`](../../sessions/58/581630bde730cfa5bca7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：

**`artifacts/shapley_v2/shapley_values_v2.json`** — 完整 Shapley 值（60 个数据源，4 null + 56 signal experiments，32 coalition enumeration）

**`artifacts/shapley_v2/shapley_method_contribution.pdf`** — 三面板 grouped bar chart

### 主结果摘要（6-pair FNR, Combined = FPR + FNR，越负越好）

| Method | FPR Shapley | FNR Shapley | Combined |
|---|---|---|---|
| **perm_granger** | +0.000 | −0.164 | **−0.164** (最优) |
| **diff_xcorr** | +0.174 | −0.303 | **−0.128** |
| ty_granger | +0.039 | −0.060 | −0.021 |
| threshold_onset | +0.112 | −0.022 | +0.090 |
| naive_xcorr | +0.612 | −0.452 | +0.160 (最差) |

关键发现：perm_granger 零 FPR 贡献 + 中等 FNR 减少 = 综合最佳。naive_xcorr 虽然 FNR 减少最强（−0.452），但 FPR 代价太大（+0.612）。8-pair robustness 结果趋势一致。

---
