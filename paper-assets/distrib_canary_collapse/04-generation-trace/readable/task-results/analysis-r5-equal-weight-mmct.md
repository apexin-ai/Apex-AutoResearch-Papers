# analysis r5 equal weight mmct

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r5_equal_weight_mmct_20260520T204829_result.json`
- **Structured JSON:** [`384ed74931066e9ccdfc.json`](../../sessions/38/384ed74931066e9ccdfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**当前 consensus 系统已经是 equal-weight（每方法 1 票），不存在 FPR-inverse weighting。** 实际差异来自 D111 方向过滤（xcorr 方法要求 `peak_lag < 0`）。

### K≥3 对比汇总

| 实验 | α | T | Equal-weight K3 | Current K3 | Diff |
|------|-----|-----|-----------------|------------|------|
| a000_s42 | 0.00 | 10 | **2** | 0 | **+2** |
| a010_s42 | 0.10 | 10 | **2** | 0 | **+2** |
| a025_s42 | 0.25 | 10 | 0 | 0 | 0 |
| a025_s43 | 0.25 | 10 | 0 | 0 | 0 |
| a045_s42 | 0.45 | 10 | 0 | 0 | 0 |
| a045_s43 | 0.45 | 10 | 0 | 0 | 0 |
| a050_s42 | 0.50 | 10 | 6 | 6 | 0 |
| a060_s42_v4 | 0.60 | 10 | 0 | 0 | 0 |
| a075_s42 | 0.75 | 10 | 6 | 6 | 0 |
| t20/a100 | 1.00 | 20 | 6 | 6 | 0 |
| t20/a045 | 0.45 | 20 | **7** | 3 | **+4** |

### 关键结论

1. **3/11 实验有 K3 差异**，全部方向为 equal-weight 更高（去掉方向过滤 = 更多 false positives）
2. **NaiveXCorr 是主要驱动因素**：59 个 pair-level vote 差异中，57 个来自 NaiveXCorr 被方向过滤掉（它在大量 pair 上 significant 但 peak_lag > 0，即反向因果）
3. **null 实验 FPR 失控**：α=0.00 从 0→2 K≥3 pairs — 去掉方向过滤直接破坏 type-I error control
4. **强信号实验完全一致**：α≥0.50 T=10 的 K3 count 在两种方案下完全相同
5. **t20/a045 差异最大**（+4）：T=20 给 NaiveXCorr 更多 lag 组合空间，方向错误的显著性更多

**结论：不应采用去掉方向过滤的 equal-weight。当前系统（equal-weight + D111 方向过滤）已是最合理方案。**

---
