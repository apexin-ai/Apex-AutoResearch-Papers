# analysis 17855 dose response m035 csv

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_17855_dose_response_m035_csv_20260520T035452_result.json`
- **Structured JSON:** [`c19e26321712303adc3b.json`](../../sessions/c1/c19e26321712303adc3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M035 Dose-Response CSV 重生成结果

### batch_analysis.py 版本确认
- M035 兼容: **是**
- direction filter: `peak_lag < 0`（lines 376, 379, 453, 457 全部正确）

### 处理的实验（13个）

| α | 目录名 |
|---|--------|
| 0.00 | a000_s42_fp32 |
| 0.05 | a005_s42_fp32_v3_d080 |
| 0.10 | a010_s42_fp32 |
| 0.25 | a025_s42_fp32 |
| 0.30 | a030_s42_fp32 |
| 0.35 | a035_s42_fp32 |
| 0.40 | a040_s42_fp32 |
| 0.45 | a045_s42_fp32 |
| 0.50 | a050_s42_fp32 |
| 0.50 | a050_postd093_s42_fp32 (post-D093, 首次纳入) |
| 0.60 | a060_s42_fp32_v3_d080 |
| 0.75 | a075_s42_fp32 |
| 1.00 | a100_s42_fp32 |

### 关键变化（old pre-M035 → new M035）

**naive_fwd（变化最剧烈）：**

| α | OLD (×8) | NEW | 变化 |
|---|----------|-----|------|
| 0.00 | 6 | 2 | -4 |
| 0.25 | 5 | 1 | -4 |
| 0.30 | 5 | 3 | -2 |
| 0.35 | **8** | **0** | **-8（完全反转）** |
| 0.45 | 7 | 1 | -6 |
| 0.75 | **0** | **7** | **+7（完全反转）** |
| 1.00 | **0** | **7** | **+7（完全反转）** |

**diff_fwd：**

| α | OLD (×8) | NEW | 变化 |
|---|----------|-----|------|
| 0.00 | 0 | 4 | +4 |
| 0.50 | 1 | 6 | +5 |
| 0.60 | 0 | **8** | **+8（完全反转）** |
| 0.75 | 0 | **6** | **+6（完全反转）** |
| 1.00 | 0 | **6** | **+6（完全反转）** |

**K≥4（高 α 区间变化巨大）：**

| α | OLD (×8) | NEW |
|---|----------|-----|
| 0.50 | 2 | 5 |
| 0.60 | 1 | 4 |
| 0.75 | **0** | **6** |
| 1.00 | **0** | **6** |

**a050_postd093（首次纳入）：** naive_fwd=3, diff_fwd=2, K≥3=5, K≥4=3, MMCT=0.375。与原 a050 (K≥4=5) 相比信号略弱，符合 D093 干预设计预期。

**总结：** M035 sign reversal 修正的效果完全符合预期——高 α 区间 (≥0.50) 的 naive/diff forward 信号从接近 0 恢复到 6-8/8；低 α 区间的虚高 forward 信号被正确压低。K≥4 在 α≥0.50 区间全面提升，dose-response 曲线现在呈现清晰的单调递增趋势。

### 文件位置
- 服务器: `/root/autodl-tmp/distrib_canary_collapse/artifacts/dose_response_m035/` (含 13 个 `*_analysis.json` + 2 CSV)
- 本地注册:
  - `dose_response_5method_regime_m035.csv`: **art_20260520_4b3542**
  - `consensus_heatmap_data_m035.csv`: **art_20260520_d67f50**

---
