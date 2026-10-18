# exp feature ablation collect phase1

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_feature_ablation_collect_phase1_20260515T185659_result.json`
- **Structured JSON:** [`1e35a851986d15939d5d.json`](../../sessions/1e/1e35a851986d15939d5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Feature Ablation Phase 1 结果汇总

### 1. Top-K Ablation（9/9 cells 完成）

| Cell | k=1 | k=3 | k=5 | k=10 | k=19(all) | Top-1 |
|------|-----|-----|-----|------|-----------|-------|
| pythia_nucleus | 62.1% | 73.3% | 77.0% | 78.1% | 78.8% | var_surprisal |
| pythia_temp09 | 64.0% | 72.8% | 74.9% | 76.5% | 76.7% | var_surprisal |
| pythia_topk50 | 56.3% | 64.9% | 66.5% | 68.6% | 68.8% | var_surprisal |
| gpt2xl_nucleus | 64.4% | 80.0% | 82.7% | 83.8% | 84.2% | var_surprisal |
| **gpt2xl_temp09** | **80.3%** | **83.5%** | **84.9%** | **85.8%** | **86.0%** | **p90_ppl** |
| gpt2xl_topk50 | 69.4% | 71.2% | 73.8% | 75.8% | 75.9% | p90_ppl |
| olmo_nucleus | 63.7% | 74.7% | 76.6% | 79.0% | 79.0% | p90_ppl |
| olmo_temp09 | 65.7% | 78.6% | 81.1% | 82.2% | 82.1% | var_surprisal |
| olmo_topk50 | 56.0% | 69.8% | 73.3% | 74.3% | 74.7% | var_surprisal |

**跨 cell 一致性**：
- **var_surprisal + p90_ppl 是所有 9 cells 的 top-2**（var_surprisal 在 6/9 cells 排 #1，p90_ppl 在 3/9 排 #1）
- Top-3 恒为 perplexity/surprisal 分布统计量（+ p50_ppl 或 p75_ppl）
- **k=3 达到全特征 93% 精度**（平均），k=5 达到 96%

### 2. Category Ablation（单类别精度，chance = 25%）

| Cell | Perplexity(9) | Surprisal(3) | Lexical(2) | N-gram Ent(2) | Repetition(3) |
|------|:---:|:---:|:---:|:---:|:---:|
| pythia_nucleus | 77.0% | 74.7% | 47.4% | 43.3% | 45.4% |
| pythia_temp09 | 74.3% | 73.3% | 48.4% | 44.8% | 47.1% |
| pythia_topk50 | 66.2% | 64.7% | 41.5% | 37.3% | 38.7% |
| gpt2xl_nucleus | 82.3% | 79.4% | 44.4% | 37.0% | 42.0% |
| gpt2xl_temp09 | 84.6% | 80.0% | 46.4% | 39.9% | 43.7% |
| gpt2xl_topk50 | 73.5% | 65.5% | 39.7% | 30.2% | 36.1% |
| olmo_nucleus | 77.7% | 73.1% | 52.1% | 43.5% | 49.5% |
| olmo_temp09 | 81.3% | 78.7% | 53.0% | 47.0% | 51.5% |
| olmo_topk50 | 73.4% | 70.6% | 42.8% | 32.7% | 39.7% |

**Perplexity #1 (9/9), Surprisal #2 (9/9)**。Perplexity 单独达到全模型 92-99% 精度。Lexical/ngram_entropy/repetition 贡献有限（近 chance 到 53%）。

### 3. Leave-One-Group-Out（去掉一类后精度下降）

| Category | Mean Δ (pp) | Worst Cell Δ | Rank |
|----------|:-----------:|:------------:|:----:|
| **Perplexity** | **-3.53** | -8.07 (gpt2xl_topk50) | **#1** |
| Surprisal | -0.54 | -1.01 (pythia_temp09) | #2 |
| Repetition | -0.22 | -0.60 (pythia_temp09) | #3 |
| Lexical | -0.10 | -0.31 (olmo_temp09) | #4 |
| N-gram Entropy | -0.06 | -0.37 (pythia_nucleus) | #5 |

Perplexity 的影响是第二名的 **6.5 倍**。去掉 lexical/ngram_entropy/repetition 基本无影响 (<0.3pp)。

### 4. PCA 有效维度

| 指标 | Mean | Range |
|------|:----:|:-----:|
| 90% variance | 6.4 components | 6-7 |
| 95% variance | 8.1 components | 7-9 |
| 99% variance | 12.2 components | 11-13 |

19 个特征的有效维度约 6-7，高度冗余。

### 5. VIF（多重共线性）

14-16/19 个特征 VIF > 10。极端高值：rep_3gram (526-638), bigram_entropy (312-345), rep_2gram (210-376), trigram_entropy (279-320), mean_surprisal (79-127)。RF 对共线性 robust，但这也解释了为什么小特征子集表现接近全集。

### 6. Forward Selection 进度（Phase 2）

v2 已完成 **4/9 cells**（pythia_nucleus, pythia_temp09, pythia_topk50, olmo_nucleus），olmo_temp09 正在运行。剩余 5 cells 预计还需 60-90 分钟。

已完成的 4 cells 一致模式：var_surprisal 或 p90_ppl 为 step 1（单特征 56-64%），step 2-3 加入 perplexity 分位数快速爬升，plateau 在 k=14-16。

### R3-N3 (Feature Importance) 支撑

这些结果为 R3-N3 提供完整证据链：

1. **Perplexity 分布统计量是主导信号** — 3 个特征捕获 93% 精度，perplexity 类单独接近全集精度
2. **跨 cell 完全一致** — var_surprisal + p90_ppl 在 3 个模型 × 3 个策略的全部 9 cells 中均为 top-2
3. **特征冗余高** — PCA 有效维度 ~6-7，VIF 普遍 >10，但 RF 能 robust 处理
4. **解释 RF > Transformer** — DeBERTa/RoBERTa 表征中 var_surprisal (R²=-4216) 和 p90_ppl 几乎不可编码，这正是最重要的特征，解释了 transformer 比 RF 低 ~20pp

---
