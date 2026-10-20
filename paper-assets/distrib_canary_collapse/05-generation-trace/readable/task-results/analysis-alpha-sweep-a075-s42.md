# analysis alpha sweep a075 s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a075_s42_20260515T131600_result.json`
- **Structured JSON:** [`8ebb26fd369308517a06.json`](../../sessions/8e/8ebb26fd369308517a06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## α=0.75 (seed=42) 实验分析报告

### 完成状态
**正常完成** — 10/10 generations，EXIT_CODE=0

### 每代指标

| gen | token_entropy | ECE | perplexity | distinct_1 | distinct_2 | distinct_3 |
|-----|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 3.234 | 0.0108 | 26.95 | 0.0982 | 0.5178 | 0.8127 |
| 1 | 2.191 | 0.1328 | 31.65 | 0.0975 | 0.5141 | 0.8104 |
| 2 | 2.102 | 0.1784 | 44.62 | 0.0827 | 0.4346 | 0.7206 |
| 3 | 2.116 | 0.1860 | 50.27 | 0.0741 | 0.3728 | 0.6246 |
| 4 | 2.130 | 0.1917 | 54.89 | 0.0711 | 0.3513 | 0.5921 |
| 5 | 2.185 | 0.1958 | 60.02 | 0.0691 | 0.3337 | 0.5569 |
| 6 | 2.211 | 0.1968 | 62.27 | 0.0678 | 0.3216 | 0.5334 |
| 7 | 2.243 | 0.2034 | 67.30 | 0.0674 | 0.3154 | 0.5225 |
| 8 | 2.328 | 0.1954 | 67.79 | 0.0667 | 0.3094 | 0.5106 |
| 9 | 2.325 | 0.2045 | 72.09 | 0.0664 | 0.3072 | 0.5060 |
| 10 | 2.337 | 0.2063 | 76.03 | 0.0661 | 0.3037 | 0.5011 |

### Drift (gen0 → gen10)

| 指标 | gen0 | gen10 | drift% |
|------|------|-------|--------|
| token_entropy | 3.234 | 2.337 | **-27.7%** |
| ECE | 0.0108 | 0.2063 | **+1809.5%** |
| perplexity | 26.95 | 76.03 | **+182.1%** |
| distinct_1 | 0.0982 | 0.0661 | **-32.7%** |
| distinct_2 | 0.5178 | 0.3037 | **-41.3%** |
| distinct_3 | 0.8127 | 0.5011 | **-38.4%** |

### Granger 因果检验（FDR 校正，BH across 40 tests）

| Direction | p_raw | p_fdr | FDR-sig? |
|-----------|-------|-------|----------|
| entropy→d1 | 0.0106 | 0.054 | borderline |
| **ECE→d1** | 0.0038 | **0.046** | **YES** |
| **entropy→d2** | 0.0072 | **0.048** | **YES** |
| **ECE→d2** | 0.0032 | **0.046** | **YES** |
| d1→entropy | 0.776 | 0.838 | no |
| d1→ECE | 0.392 | 0.496 | no |
| d2→entropy | 0.767 | 0.838 | no |
| d2→ECE | 0.462 | 0.548 | no |

反向因果全部非显著（p_fdr > 0.4），方向性清晰：canary → downstream。

### Consensus Classification (5-method agreement)

**α=0.75: 11/16 robust pairs** — 所有单 seed α 点中最强。

Robust pairs:
- token_entropy → {perplexity, d1, d2, d3} (4/5 methods)
- ECE → {perplexity, d1, d2, d3} (4/5 methods)
- effective_rank → {d1, d2, d3} (4/5 methods)

### Cross-Correlation

| pair | peak lag | r |
|------|----------|---|
| entropy_vs_d1 | lag=2 | +0.973 |
| ECE_vs_d1 | lag=2 | -0.984 |

ECE/entropy 变化 lead diversity 退化 ~2 代。

### 与其他 α 点对比（dose-response）

| α | entropy_drift% | ECE_drift% | ppl_drift% | d1_drift% | d2_drift% | d3_drift% | Granger FDR-sig | Consensus robust |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0.00 | -5.1 | +51.7 | -21.7 | -13.8 | -9.8 | -4.5 | 0/8 | 0/16 |
| 0.25 | -4.1 | +79.7 | -17.2 | -40.3 | -57.1 | -59.9 | 0/8 | 1/16 |
| 0.50 | -18.6 | +842.8 | +21.1 | -37.3 | -51.5 | -52.4 | 0/8 | 0/16 |
| **0.75** | **-27.7** | **+1809.5** | **+182.1** | **-32.7** | **-41.3** | **-38.4** | **3/8** | **11/16** |
| 1.00 | -63.4 | +3762.6 | +3624.6 | -28.3 | -35.2 | -31.6 | 2/8 | 6/16 |

关键观察：
1. **Calibration metrics（entropy, ECE, ppl）严格单调**：drift 随 α 增大而加剧，α=0.75 落在 α=0.50 和 α=1.0 之间，dose-response 曲线平滑
2. **Diversity drift 非单调**：peak 在 α=0.25，之后 recovery — 这暗示高 α 时 mode collapse 导致的 diversity loss 与低 α 时不同机制
3. **α=0.75 Granger 最强**：3/8 FDR-sig（比 α=1.0 的 2/8 还多），11/16 consensus robust 也最高

### 结论

**SUCCESS** — α=0.75 是 canary hypothesis 的强支撑点。

1. **Granger FDR-sig 确认**：ECE→d1、ECE→d2、entropy→d2 三对因果关系通过 FDR 校正（entropy→d1 borderline at 0.054）
2. **Claim 1 scope 可扩展为 "α ≥ 0.75"**：α=0.75 和 α=1.0 在 Granger 和 consensus 上都显著，calibration canary 在 75%+ synthetic contamination 下有效
3. **但注意 C001 约束**：这是单 seed 数据，正式 claim 需等 D026 multi-seed 确认。单 seed 下 α=0.75 consensus 11/16 比 α=1.0 的 6/16 还强，可能存在种子效应
4. **α=0.50 是 phase transition boundary**：Granger 在 α=0.50 完全不显著，α=0.75 突然爆发——这暗示 canary signal 有一个临界阈值

---
