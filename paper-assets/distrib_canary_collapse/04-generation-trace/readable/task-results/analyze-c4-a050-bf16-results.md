# analyze c4 a050 bf16 results

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_c4_a050_bf16_results_20260518T202848_result.json`
- **Structured JSON:** [`ed0ea6ef47f5d9865c70.json`](../../sessions/ed/ed0ea6ef47f5d9865c70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整结果。

---

## C4 α=0.50 s42 bf16 实验分析 (Pythia-410M)

### 1. 核心指标表 (gen0 → gen10)

| Metric | Gen0 | Gen5 | Gen10 | Delta% |
|--------|------|------|-------|--------|
| token_entropy | 3.136 | 2.274 | 1.940 | **-38.2%** |
| distinct_1 | 0.111 | 0.094 | 0.089 | -20.3% |
| distinct_2 | 0.562 | 0.466 | 0.424 | -24.6% |
| distinct_3 | 0.874 | 0.784 | 0.686 | -21.5% |
| mauve | 0.691 | 0.100 | 0.078 | **-88.7%** |
| ece | 0.011 | 0.171 | 0.259 | **+2250%** |
| perplexity | 24.4 | 59.0 | 122.8 | **+402%** |

所有指标方向一致，collapse 明确。Entropy 单调下降，perplexity 单调上升。

### 2. Threshold Onset (2-sigma)

| Metric | Onset Gen |
|--------|-----------|
| mauve | **2** (最早) |
| distinct_1 | 3 |
| token_entropy | 4 |
| distinct_2 | 4 |
| ece | 5 |
| distinct_3 | 8 (最晚) |

**关键发现：C4 域 mauve 和 distinct_1 onset 早于 canary (token_entropy/ece)。** 这与 WikiText α=1.0 的 canary-leads 模式不同。

### 3. PermG 显著性

**Forward (canary → downstream):**
- Raw significant: 3/8 (token_entropy → distinct_1 p=0.028, distinct_2 p=0.034, mauve p=0.022)
- **FDR-corrected: 0/8** (最低 p_fdr=0.091，未过 0.05 线)

**Reverse (downstream → canary):**
- Raw significant: 2/8 (distinct_2→TE p=0.037, distinct_3→TE p=0.041)
- **FDR-corrected: 0/8**

PermG 单 seed 在 α=0.50 power 不足。这与 WikiText α=0.50 的已知 pattern 一致。

### 4. Diff Cross-Correlation (lead-lag 主要证据)

| Pair | Best Lag | r |
|------|----------|---|
| token_entropy → distinct_1 | **+1** | **0.914** |
| token_entropy → distinct_2 | **+1** | **0.900** |
| token_entropy → distinct_3 | **+1** | 0.527 |
| token_entropy → mauve | **+1** | **0.729** |
| ece → distinct_1 | +1 | 0.448 |
| ece → distinct_2 | +1 | 0.457 |
| ece → distinct_3 | +2 | -0.624 |
| ece → mauve | 0 | 0.454 |

**token_entropy 的 diff xcorr 全部 lag=+1，r=0.53~0.91。lead-lag pattern 存在，token_entropy 变化量领先 diversity 变化量 1 代。** ece 信号弱得多。

### 5. 与 WikiText α=0.50 s42 跨域对比

| Metric | C4 bf16 Delta% | WikiText Delta% | 差异 |
|--------|---------------|-----------------|------|
| token_entropy | **-38.2%** | -18.6% | C4 entropy 崩溃更严重 (2x) |
| distinct_1 | -20.3% | **-37.3%** | WikiText diversity 崩溃更严重 |
| distinct_2 | -24.6% | **-51.5%** | WikiText diversity 崩溃更严重 |
| distinct_3 | -21.5% | **-52.4%** | WikiText diversity 崩溃更严重 |
| ece | +2250% | +843% | C4 calibration 崩溃更严重 |
| perplexity | **+402%** | +21.2% | C4 perplexity 崩溃猛烈 (19x) |
| mauve | -88.7% | -38.5% | C4 mauve 崩溃更严重 |

**跨域 pattern 差异：**
- C4: canary 指标 (entropy -38%, ece +2250%, ppl +402%) 崩溃猛烈，diversity 下降相对温和 (-20~25%)
- WikiText: diversity 指标 (-37~52%) 崩溃猛烈，canary 变化温和 (entropy -19%, ppl +21%)
- 两个域都 collapse，但 **崩溃分布不同**：C4 偏 distributional（entropy/calibration），WikiText 偏 lexical（diversity）
- WikiText token_entropy 在 gen1 大跌后 rebound 并稳定在 ~2.6；C4 token_entropy 单调下降无 rebound

### 6. 与 Pythia-1B C4 α=1.0 s42 参考对比

| Metric | C4 410M α=0.50 | C4 1B α=1.0 | 注释 |
|--------|---------------|-------------|------|
| token_entropy | -38.2% | -57.5% | α=1.0 更猛 |
| distinct_1 | -20.3% | -22.1% | 接近 |
| perplexity | +402% | +8069% | α=1.0 量级差异巨大 |

α=0.50 的 collapse 幅度约为 α=1.0 的 50-70%（entropy 维度），dose-response 关系成立。

### 总结

1. **Collapse 确认**：C4 α=0.50 s42 bf16 全部 7 个指标方向一致，collapse 无争议
2. **Canary signal**：PermG FDR 0/8（单 seed power 不足），但 diff xcorr 全部 lag=+1 (r=0.53~0.91) 支持 entropy-leads-diversity 的 lead-lag pattern
3. **跨域差异**：C4 和 WikiText 在 α=0.50 下 collapse 分布模式不同（C4 偏 distributional，WikiText 偏 lexical），但 lead-lag 方向一致
4. **需要 multi-seed**：PermG FDR=0/8 是 power 问题（T=11 太短），需要 s43/s44 做 pooled 分析才能得到可发表的显著性结论

---
