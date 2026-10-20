# analysis phase0 summary table

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase0-summary-table_20260517T184857_result.json`
- **Structured JSON:** [`db3f783a3db6facbf12b.json`](../../sessions/db/db3f783a3db6facbf12b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已写入。以下是完整数据表。

---

## Phase 0 完整数据表 (Pythia-410M, 100% Synthetic, 10 Generations)

### 核心指标

| Gen | eff_rank | log_det | ppl | hellaswag | distinct4 | train_loss | sigma1 |
|-----|----------|---------|-----|-----------|-----------|------------|--------|
| 0 | 417.55 | 2366.68 | 9.5536 | 0.4130 | 0.7414 | | 1942.82 |
| 1 | 491.77 | 2464.76 | 11.3832 | 0.3897 | 0.6256 | 1.6228 | 803.96 |
| 2 | 496.44 | 2469.93 | 13.5810 | 0.3764 | 0.5154 | 1.2682 | 712.03 |
| 3 | 493.31 | 2440.57 | 16.2464 | 0.3658 | 0.4900 | 1.1340 | 700.68 |
| 4 | 485.67 | 2405.05 | 19.8041 | 0.3558 | 0.4679 | 1.0980 | 729.59 |
| 5 | 479.21 | 2370.17 | 24.5927 | 0.3439 | 0.4630 | 1.0474 | 741.02 |
| 6 | 473.00 | 2335.17 | 30.9139 | 0.3311 | 0.4655 | 1.0252 | 758.40 |
| 7 | 464.20 | 2304.19 | 38.8888 | 0.3187 | 0.4474 | 1.0151 | 791.28 |
| 8 | 456.76 | 2252.12 | 49.2899 | 0.3103 | 0.4401 | 0.9868 | 797.66 |
| 9 | 448.45 | 2207.57 | 63.3248 | 0.3009 | 0.4262 | 0.9968 | 814.13 |
| 10 | 442.46 | 2178.95 | 76.7808 | 0.2951 | 0.4259 | 0.9782 | 825.72 |

### 派生指标 (per-gen deltas)

| Gen | ppl_growth_factor | hellaswag_delta | eff_rank_delta | log_det_delta |
|-----|-------------------|-----------------|----------------|---------------|
| 0 | | | | |
| 1 | 1.1915 | -0.0233 | +74.22 | +98.08 |
| 2 | 1.1930 | -0.0132 | +4.67 | +5.17 |
| 3 | 1.1963 | -0.0107 | -3.13 | -29.36 |
| 4 | 1.2190 | -0.0100 | -7.64 | -35.52 |
| 5 | 1.2418 | -0.0119 | -6.47 | -34.88 |
| 6 | 1.2570 | -0.0127 | -6.20 | -35.01 |
| 7 | 1.2579 | -0.0124 | -8.81 | -30.97 |
| 8 | 1.2675 | -0.0084 | -7.44 | -52.07 |
| 9 | 1.2848 | -0.0094 | -8.31 | -44.55 |
| 10 | 1.2125 | -0.0059 | -5.99 | -28.62 |

### 汇总统计

| 指标 | 值 |
|------|-----|
| decline_rate_ratio (eff_rank) | **2.43** (Gen 6-10 衰减速率 / Gen 1-5 衰减速率, >1 = 加速坍缩) |
| decline_rate_ratio (log_det) | **1.65** |
| total_ppl_growth (gen10/gen0) | **8.04x** |
| total_hellaswag_drop (gen0 - gen10) | **0.1179** (从 0.413 降到 0.295) |

### 关键观察

- **eff_rank 先升后降**：Gen 0→2 从 417.55 升至 496.44（初代合成训练反而提升多样性），Gen 2 之后单调下降至 442.46
- **sigma1 先骤降后持续上升**：Gen 0 的 1942.82 是原始预训练模型的主导奇异值，Gen 1 骤降至 803.96 后从 Gen 3 起持续攀升至 825.72，反映频谱越来越集中于少数方向
- **ppl 增长因子逐代递增**：从 1.19 (Gen 1) 升至 1.28 (Gen 9)，Gen 10 略回落至 1.21，整体呈加速趋势
- **distinct4 在 Gen 5-6 出现平台**：0.4630 → 0.4655（微升），之后继续下降

CSV 已保存至 `/root/spectral_collapse_ews/results/phase0_summary.csv`。

---
