# ops hellaswag collect results

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_hellaswag-collect-results_20260521T103556_result.json`
- **Structured JSON:** [`57f483a219edbd87127a.json`](../../sessions/57/57f483a219edbd87127a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 进程状态：仍在运行

| 任务 | 当前进度 | GPU |
|------|----------|-----|
| Seed43 eval | 正在跑 gen1（PID 568262） | GPU 0 |
| Seed44 eval | 正在跑 gen5（PID 568031，~83% loglikelihood） | GPU 0 |

### HellaSwag acc_norm 结果

| Gen | Seed42 | Seed43 | Seed44 | Mean | Std |
|-----|--------|--------|--------|------|-----|
| 0 | 0.4130 | MISS | 0.4130 | 0.4130 | 0.0000 |
| 1 | 0.3897 | MISS | 0.3911 | 0.3904 | 0.0010 |
| 2 | 0.3764 | MISS | 0.3841 | 0.3803 | 0.0054 |
| 3 | 0.3658 | MISS | 0.3721 | 0.3690 | 0.0045 |
| 4 | 0.3558 | MISS | 0.3554 | 0.3556 | 0.0003 |
| 5 | 0.3439 | MISS | MISS | — | — |
| 6 | 0.3311 | MISS | MISS | — | — |
| 7 | 0.3187 | MISS | MISS | — | — |
| 8 | 0.3103 | MISS | MISS | — | — |
| 9 | 0.3009 | MISS | MISS | — | — |
| 10 | 0.2951 | MISS | MISS | — | — |

**完成度**: Seed42 11/11, Seed43 0/11, Seed44 5/11（gen0-4完成，gen5正在跑）

### σ₁ 数据（3 seeds 完整，gen 0-10）

| Gen | Seed42 | Seed43 | Seed44 |
|-----|--------|--------|--------|
| 0 | 1942.82 | 1942.82 | 1942.82 |
| 1 | 803.96 | 814.61 | 808.07 |
| 2 | 712.03 | 718.12 | 726.02 |
| 3 | 700.68 | 715.54 | 709.96 |
| 4 | 729.59 | 723.06 | 715.90 |
| 5 | 741.02 | 753.63 | 753.04 |
| 6 | 758.40 | 765.98 | 769.53 |
| 7 | 791.28 | 790.03 | 783.82 |
| 8 | 797.66 | 813.31 | 808.25 |
| 9 | 814.13 | 858.36 | 850.72 |
| 10 | 825.72 | 886.08 | 911.87 |

σ₁ 数据还有 per-layer 版本（`alternative_ews_comparison.json` 含 attn_dense_sigma1 和 ffn_down_sigma1），但仅 seed42 有。

**预计剩余时间**：每个 gen 约 6-7 分钟。Seed44 还需 ~6 gen × 7min ≈ 42min，Seed43 还需 ~10 gen × 7min ≈ 70min。两者共享 GPU 0 可能串行运行，总计约 2 小时完成全部。

---
