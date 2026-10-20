# analysis 3seed partial ttest

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3seed_partial_ttest_20260513T214831_result.json`
- **Structured JSON:** [`d5d75b8611d328262bfb.json`](../../sessions/d5/d5d75b8611d328262bfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。关键发现：

### PPL

| 比较 | t | p | Cohen's d | 显著？ |
|------|---|---|-----------|--------|
| Random vs Uncurated | -2.07 | 0.108 | -1.69 | n.s. |
| Random vs External | -1.67 | 0.171 | -1.36 | n.s. |
| External vs Uncurated | -0.29 | 0.790 | -0.23 | n.s. |
| RGDS vs Random | 10.48 | **0.046** | 12.13 | **sig** |
| RGDS vs External | 8.70 | **0.026** | 8.89 | **sig** |
| RGDS vs Uncurated | 8.56 | **0.028** | 8.80 | **sig** |

**PPL ANOVA (Normal Cluster)**: F=1.98, **p=0.219** → 三方法无显著差异，支持 "normal cluster" framing。

### Rare n-gram

| 比较 | t | p | Cohen's d | 显著？ |
|------|---|---|-----------|--------|
| Random vs Uncurated | 3.47 | **0.025** | 2.84 | **sig** |
| Random vs External | -1.84 | 0.140 | -1.50 | n.s. |
| External vs Uncurated | 4.59 | **0.010** | 3.75 | **sig** |
| RGDS vs Random | -7.35 | 0.067 | -8.47 | n.s. (borderline) |
| RGDS vs External | -7.91 | **0.047** | -8.66 | **sig** |
| RGDS vs Uncurated | -5.66 | 0.074 | -6.23 | n.s. (borderline) |

**Rare n-gram ANOVA**: F=13.01, **p=0.007** → 三方法在 rare n-gram 上**有显著差异**。Uncurated 显著低于 Random 和 External（说明未筛选数据稀释了罕见 n-gram）。

### Ratio

External vs RGDS: t=14.22, **p=0.005**, d=10.07 → 极显著。

### 总结

- **PPL normal cluster 成立**：Random/External/Uncurated PPL 无显著差异 (p=0.22)，RGDS 与三者均显著不同 (p<0.05, d>8)
- **Rare n-gram normal cluster 不成立**：三方法间有显著差异 (ANOVA p=0.007)，主要是 Uncurated 偏低
- RGDS vs 其他的 Welch t-test 中，n=2 导致两个 rare n-gram 比较 borderline (p≈0.067-0.074)，第 3 个 seed 完成后大概率变显著
- Random vs Uncurated PPL p=0.108，与之前一致，n=3 仍不够达显著

---
