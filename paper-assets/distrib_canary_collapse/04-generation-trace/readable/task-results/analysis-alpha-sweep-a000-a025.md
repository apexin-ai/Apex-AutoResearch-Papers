# analysis alpha sweep a000 a025

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha-sweep-a000-a025_20260515T012151_result.json`
- **Structured JSON:** [`3c39022d88e0eb455fa4.json`](../../sessions/3c/3c39022d88e0eb455fa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是双点对比总结：

---

## α-Sweep 双点分析结果

### 1. Naive Cross-Correlation: α=0.25 vs α=0.0

| Pair | α=0.0 lag | α=0.0 |r| | α=0.0 FDR-sig | α=0.25 lag | α=0.25 |r| | α=0.25 FDR-sig |
|------|-----------|---------|-------------|------------|----------|--------------|
| token_entropy→distinct_1 | 2 | 0.867 | n.s. | **1** | **0.948** | **SIG** |
| token_entropy→distinct_2 | 2 | 0.826 | n.s. | **1** | **0.925** | **SIG** |
| token_entropy→distinct_3 | 2 | 0.816 | n.s. | **1** | **0.895** | **SIG** |
| token_entropy→perplexity | 0 | 0.985 | SIG | 0 | 0.982 | SIG |
| ece→distinct_1 | 0 | 0.772 | n.s. | **3** | **0.948** | **SIG** |
| ece→distinct_2 | 0 | 0.737 | n.s. | **3** | **0.956** | **SIG** |
| ece→distinct_3 | 0 | 0.676 | n.s. | **2** | **0.951** | **SIG** |
| ece→perplexity | -3 | 0.793 | n.s. | -1 | 0.770 | SIG |

### 2. 关键发现

**Q1: α=0.25 vs α=0.0 的 canary→diversity cross-correlation 差异**
- 差异巨大。α=0.0 全部 n.s.（FDR 校正后），α=0.25 **全部 8/8 FDR-significant**。
- token_entropy→distinct 的 |r| 从 ~0.82 提升到 ~0.92，且 p 值下降 1-2 个数量级。

**Q2: α=0.25 下 Permutation Granger 是否显著**
- FDR 校正后 **全部 n.s.**。raw p 中 token_entropy→distinct_1 (F=163.24, p=0.015) 接近显著但 FDR 校正后 p=0.12。这与 11 个时间点的统计功效不足一致。

**Q3: Canary lead-lag 在 α=0.25 下是否与 MVP 一致**
- **一致性良好**。token_entropy 在 α=0.25 下 **lag=1**（canary 领先 diversity 1 代），符合 canary 先行信号的假设。
- ece 的 lag=2~3，也显示 canary 领先。

**Q4: α=0.0 null control 是否无显著 lead-lag**
- **基本符合预期**。FDR 校正后仅 token_entropy→perplexity 显著（但 lag=0，同步相关，非因果先行），其余全部 n.s.。Toda-Yamamoto 和 Permutation Granger 全部 n.s.。

### 3. Consensus Pairs（≥2 方法一致）

仅在 α=0.25 下出现，且仅限 token_entropy：
- **token_entropy → distinct_1**: naive_xcorr + Toda-Yamamoto (lag=1)
- **token_entropy → distinct_2**: naive_xcorr + Toda-Yamamoto (lag=1)
- **token_entropy → distinct_3**: naive_xcorr + Toda-Yamamoto (lag=1)

α=0.0 下零 consensus pairs。

### 4. 总结

α=0.25 相对 α=0.0 呈现清晰的 dose-response：注入 25% 的 distributional canary collapse 就足以产生 statistically significant 且 temporally leading 的 canary→diversity 信号。null control (α=0.0) 如预期几乎无显著 lead-lag，确认信号来自 α 干预而非 baseline drift。Granger 因果类方法因样本量限制（11 代）功效不足，但 Toda-Yamamoto 在 token_entropy→distinct 对上通过了 FDR 校正。

---
