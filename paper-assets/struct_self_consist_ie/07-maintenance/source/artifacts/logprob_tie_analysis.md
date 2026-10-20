# Logprob Tie Analysis — SciERC NER (exp_012_rerun_1024)

**Data**: Qwen SciERC joint (NER+RE), N=8, seed=42, max_tokens=1024, 551 instances

---

## 1. Logprob Range Distribution

Mean logprob range (max−min across 8 samples per instance):

| Statistic | Value |
|-----------|-------|
| Mean | 0.0623 |
| Median | 0.0413 |
| P25 | 0.0265 |
| P75 | 0.0693 |
| P90 | 0.1221 |
| P95 | 0.1770 |
| Max | 0.6083 |

**Logprob 值极度集中**：median range 仅 0.041，意味着一半 instance 的 8 个样本 mean_logprob 差异不到 0.04。

## 2. Tie 比例 vs ε 阈值

| ε (range < ε = "tied") | Tied instances | 比例 |
|------------------------|----------------|------|
| 0.001 | 6/551 | 1.1% |
| 0.005 | 8/551 | 1.5% |
| 0.01 | 11/551 | 2.0% |
| 0.02 | 78/551 | 14.2% |
| **0.05** | **329/551** | **59.7%** |
| 0.10 | 461/551 | 83.7% |
| 0.20 | 532/551 | 96.6% |
| 0.50 | 548/551 | 99.5% |

**关键发现**：以 ε=0.05 为标准，**60% 的 instance logprob 值几乎无差异**，选择退化为近似随机。

## 3. 整体 Selection Performance

| Strategy | NER F1 | RE F1 |
|----------|--------|-------|
| Greedy | 0.6436 | 0.4909 |
| Random sample (mean) | 0.6059 | — |
| **Logprob-best** | **0.6495** | 0.4442 |
| Logprob-worst | 0.5098 | — |
| Oracle | 0.7775 | — |

Logprob-best 在 NER 上仅比 greedy 高 +0.006，Oracle gap 高达 +0.13，说明 selection 远未饱和。

## 4. Non-Tied 子集上的 Selection Performance

| 阈值 (range ≥) | N (占比) | Greedy F1 | LP-best F1 | Diff | p-value | Win/Lose/Tie |
|---------------|----------|-----------|------------|------|---------|-------------|
| 0.01 | 540 (98%) | 0.6407 | 0.6463 | +0.006 | 0.422 | 60/70/410 |
| 0.02 | 473 (86%) | 0.6276 | 0.6356 | +0.008 | 0.289 | 56/61/356 |
| **0.05** | **222 (40%)** | **0.5863** | **0.6133** | **+0.027** | **0.010** | 29/20/173 |
| 0.10 | 90 (16%) | 0.5680 | 0.6029 | +0.035 | 0.079 | 13/8/69 |
| 0.20 | 19 (3%) | 0.6649 | 0.7108 | +0.046 | 0.295 | 4/1/14 |

**核心结论**：在 logprob 有足够区分度的子集 (range ≥ 0.05, 40% data) 上，logprob selection **显著优于** greedy (p=0.01)。随着区分度增大，logprob 优势单调递增 (+0.027 → +0.035 → +0.046)。

## 5. Within-Instance Logprob-F1 Correlation

| Metric | Value |
|--------|-------|
| Mean Spearman ρ (mean_logprob ↔ NER F1) | 0.1823 |
| Median ρ | 0.2852 |
| % positive ρ | 64.3% |

Stratified by logprob range:

| Range bin | N instances | Mean ρ | N with variance |
|-----------|------------|--------|----------------|
| < 0.01 | 11 | +0.319 | 4 |
| 0.01–0.05 | 318 | +0.084 | 255 |
| 0.05–0.1 | 132 | +0.252 | 110 |
| **0.1–0.5** | **87** | **+0.390** | 76 |
| ≥ 0.5 | 3 | +0.506 | 3 |

**Logprob 信号随区分度增大而显著增强**：range 在 0.1-0.5 时 ρ=0.39，说明 logprob 本身包含质量信号，但被极窄的数值范围压缩了。

## 6. Structural Consistency (SJ) vs Logprob 对比

### 整体

| Strategy | NER F1 |
|----------|--------|
| Greedy | 0.6436 |
| Logprob-best | 0.6495 |
| SJ-best | 0.6505 |
| Oracle | 0.7775 |

### Non-tied 子集

| Subset | Greedy | LP-best | SJ-best | SJ vs LP (p) |
|--------|--------|---------|---------|--------------|
| range ≥ 0.05 (N=222) | 0.5863 | **0.6133** | 0.6066 | -0.007, p=0.62 |
| range ≥ 0.1 (N=90) | 0.5680 | **0.6029** | 0.5659 | -0.037, p=0.12 |

**意外发现**：在 logprob non-tied 子集上，logprob selection 实际 **优于** SJ。说明 logprob 在有足够 spread 时是有效的 quality signal。

### Tie 对比

| Signal | Tied 比例 | 定义 |
|--------|----------|------|
| Logprob (range < 0.05) | **59.7%** | 数值压缩严重 |
| SJ (range ≤ 0) | **12.5%** | 大部分有区分度 |

**SJ 的优势在于 spread 而非 signal quality**：SJ median range = 0.57，远大于 logprob 的 0.041。SJ 很少 tied (12.5%)，因此能在更多 instance 上做有效 selection。

### 两者一致性

Logprob-best 和 SJ-best 选中同一个 sample 的比例仅 **14.3%** — 两种信号捕获不同维度的质量。

## 7. Length Bias

| Correlation | Spearman ρ | p |
|------------|-----------|---|
| mean_logprob ↔ n_tokens | +0.339 | 1.3e-118 |
| mean_logprob ↔ NER F1 | +0.305 | 1.6e-95 |
| n_tokens ↔ NER F1 | +0.112 | 7.1e-14 |

- Mean logprob selection F1: 0.6495 (length-normalized)
- Cumulative logprob selection F1: 0.6002 (无 normalization)

Length normalization 至关重要 — cumulative logprob 甚至不如 greedy。但 logprob-best 并不系统性偏好最长样本 (length rank = 0.43, 略偏短)。

## 8. 综合结论

### Ties 是 logprob selection 表现差的主要原因

1. **60% instance logprob 几乎 tied** (range < 0.05)，selection 退化为近随机
2. **在 non-tied 子集上 logprob 有效**：range ≥ 0.05 时显著优于 greedy (p=0.01, +0.027 F1)，甚至优于 SJ
3. **信号强度随 spread 单调递增**：ρ 从 0.08 (tight) 增长到 0.39 (spread)

### 为什么 SJ 整体表现更好

不是因为 SJ 是更好的 quality signal，而是因为 **SJ 几乎不 tied** (仅 12.5%)。SJ 的区分度来自离散的集合比较 (Jaccard)，天然有更大 spread；而 logprob 是连续概率的平均值，在 LLM 对 IE 任务高度自信时被压缩到极窄区间。

### Implication

- Logprob 包含有效的质量信号（在有 spread 时 ρ≈0.39），但被数值压缩问题严重限制
- 两种信号仅 14.3% 一致 → **组合潜力大**
- 未来方向：(a) 放大 logprob spread (temperature scaling, calibration)；(b) logprob + SJ 联合 scoring
