# analysis atlas v2 prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_atlas-v2-prep_20260515T020901_result.json`
- **Structured JSON:** [`27d5770557b72f151128.json`](../../sessions/27/27d5770557b72f151128.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete Atlas v2 analysis summary.

---

## Atlas v2 — 8/9 Cells Analysis Summary

### 产出文件
- `artifacts/atlas_v2/atlas_v2_data.json` — 8-cell 数据集
- `artifacts/atlas_v2/atlas_v2_results.json` — 完整分析结果
- `artifacts/atlas_v2/edd_sensitivity.json` — EDD 阈值敏感性
- `artifacts/atlas_v2/atlas_summary.json` — 含 monotonicity 及 feature clustering
- `scripts/atlas_v2_complete.py` — 分析脚本

### 1. Monotonicity Scores

**AUC 单调性（consecutive AUC 递降）**：所有 8 cells 均为 **1.0000**（完美单调）。d0v1 > d1v2 > d2v3 在每个 cell 都成立。

**Feature-level 单调性（mean |score|）**：
| Cell | mean\|score\| | 完美单调特征数 |
|------|-------------|--------------|
| gpt2xl_temp09 | 0.9649 | 18/19 |
| pythia_nucleus | 0.8947 | 16/19 |
| pythia_temp09 | 0.8245 | 14/19 |
| gpt2xl_nucleus | 0.7894 | 13/19 |
| olmo_temp09 | 0.7894 | 13/19 |
| pythia_topk50 | 0.7192 | 11/19 |
| olmo_nucleus | 0.7192 | 11/19 |
| olmo_topk50 | **0.6489** | **9/19** |

范围：**[0.6489, 0.9649]**

### 2. EDD Threshold Sensitivity

| Cell | th=0.65 | th=0.70 | th=0.75 | th=0.80 |
|------|---------|---------|---------|---------|
| pythia_nucleus | 3 | 3 | 3 | 3 |
| pythia_temp09 | 3 | 3 | 3 | **2** |
| pythia_topk50 | 3 | **2** | **2** | **1** |
| olmo_nucleus | 3 | 3 | 3 | 3 |
| olmo_temp09 | 3 | 3 | 3 | 3 |
| olmo_topk50 | 3 | 3 | **2** | **2** |
| gpt2xl_nucleus | 3 | 3 | 3 | 3 |
| gpt2xl_temp09 | 3 | 3 | 3 | 3 |
| **Mean** | **3.0000** | **2.8750** | **2.7500** | **2.5000** |

**EDD 饱和 cells**（所有阈值 EDD=3）：pythia_nucleus, olmo_nucleus, olmo_temp09, gpt2xl_nucleus, gpt2xl_temp09 — **5/8 cells**

**最敏感**：pythia_topk50（EDD: 3→1，range=2）
**最不敏感**：5 cells 并列（range=0）

### 3. Cross-Model / Cross-Strategy 一致性

**Cross-model rank correlation (Spearman rho of feature importance)**:
- nucleus_p095: ρ = 0.8005
- temperature_09: ρ = 0.7461
- topk_k50: ρ = 0.7363（仅 2 模型）

**Cross-cell Jaccard (top-5 features)**:
- 全局 mean = 0.7500 ± 0.1443
- Same-model: Pythia=1.0, OLMo=0.6667, GPT-2 XL=0.6667
- Same-strategy: nucleus=0.7778, temp09=0.7778, topk50=0.6667

**Universal top-5 features**：p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl
- var_surprisal 最稳定（CV=0.1323），mean_ppl 最不稳定（CV=0.8580）

### 4. Signal Strength Heatmap (RF acc)

|  | nucleus | temp09 | topk50 |
|--|---------|--------|--------|
| Pythia | 0.7815 | 0.7625 | 0.6963 |
| OLMo | 0.7877 | 0.8203 | 0.7420 |
| GPT-2 XL | 0.8333 | 0.8542 | — |

Mean: 0.7847, Std: 0.0482, Range: [0.6963, 0.8542]

### Key takeaways
1. **完美 AUC 单调性**：8/8 cells，depth degradation signal 在所有 model×strategy 组合中一致递降
2. **EDD 饱和现象明显**：62.5% 的 cells 在所有阈值下 EDD=3（最大深度仍可区分），only topk50 策略出现 EDD 下降
3. **topk50 是最弱信号策略**：在 Pythia 和 OLMo 上都导致最低 acc 和最早的 EDD 衰减
4. **GPT-2 XL + temp09 是最强组合**：最高 acc (0.8542)、最高 feature 单调性 (0.9649)、EDD 全程饱和
5. **Feature importance 跨模型一致性高**（mean Jaccard=0.75），perplexity 相关特征（p90_ppl, var_surprisal）普遍主导

---
