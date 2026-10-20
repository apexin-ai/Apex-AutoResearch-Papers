# ssh exp 017 final collect

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_017_final_collect_20260523T034516_result.json`
- **Structured JSON:** [`994f48c39393879ad019.json`](../../sessions/99/994f48c39393879ad019.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_017 (r=0.2, seed43) Gen 10 完成。

## exp_017 Gen 10 最终 Metrics (seed43)

| 指标 | 值 |
|------|-----|
| **log_det (SLV)** | 2455.78 |
| **eff_rank** | 505.98 |
| **PPL** | 13.40 |
| **distinct-4** | 0.2453 |
| **train_loss** | 0.9375 |
| **sigma1** | 714.87 |

## 2-Seed 均值 & CV (seed42 vs seed43)

| 指标 | seed42 | seed43 | Mean | Std | CV% |
|------|--------|--------|------|-----|-----|
| **SLV** | 2479.70 | 2455.78 | 2467.74 | 16.92 | 0.69% |
| **eff_rank** | 511.30 | 505.98 | 508.64 | 3.76 | 0.74% |
| **PPL** | 13.83 | 13.40 | 13.62 | 0.30 | 2.24% |
| **D-4** | 0.520 | 0.245 | 0.383 | 0.194 | 50.8% |

所有谱指标（SLV, eff_rank）跨 seed 高度一致（CV < 1%）。PPL 也稳定（CV 2.2%）。D-4 变异大（CV 50.8%），两个 seed 趋势一致（单调下降）但绝对值差距显著。

**exp_018 进度**: Gen 1 样本生成中（8960/25000）。

---
