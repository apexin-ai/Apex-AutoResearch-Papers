# analysis n2 roberta feature overlap

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n2_roberta_feature_overlap_20260515T132452_result.json`
- **Structured JSON:** [`54cb99e13756e05519c3.json`](../../sessions/54/54cb99e13756e05519c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RoBERTa Feature Overlap 分析结果

### RoBERTa Probing R²（Top-5 → Bottom-3）

| Feature | RoBERTa R² | DeBERTa R² |
|---------|-----------|-----------|
| bigram_entropy | **0.829** | 0.72 |
| rep_2gram | **0.819** | **0.82** |
| mean_surprisal | **0.818** | 0.78 |
| type_token_ratio | **0.811** | **0.85** |
| trigram_entropy | **0.789** | 0.69 |
| ... | ... | ... |
| var_ppl | **-4215.8** | -28.1 |
| mean_ppl | **-9.50** | -4.2 |
| p10_ppl | -0.30 | — |

### Overlap 指标

| 指标 | RoBERTa | DeBERTa |
|------|---------|---------|
| Spearman ρ (RF vs Model) | **-0.456** (p=0.050) | **-0.484** (p=0.036) |
| Top-5 overlap | **0/10** | **0/10** |
| Top-10 overlap | **2/18** (trigram_entropy, var_surprisal) | — |
| Top-10 Jaccard | 0.111 | — |

### RoBERTa Top-5 vs RF Top-5

- **RF**: var_surprisal, p90_ppl, p50_ppl, skewness_ppl, var_ppl
- **RoBERTa**: bigram_entropy, rep_2gram, mean_surprisal, type_token_ratio, trigram_entropy

### Feature Group 对比

| Group | RoBERTa Probing R² | RF Importance |
|-------|-------------------|---------------|
| ngram_entropy | 0.809 | 0.0019 |
| repetition | 0.777 | 0.0014 |
| surprisal | 0.758 | **0.103** |
| lexical_diversity | 0.698 | 0.0009 |
| ppl_quantiles | 0.229 | **0.018** |
| ppl_central | -4.50 | 0.011 |
| ppl_spread | -1405.4 | 0.006 |

### 总结

RoBERTa 与 DeBERTa 的 feature overlap 分析高度一致：**两个模型都擅长表面文本特征（n-gram entropy、repetition、lexical diversity，R²>0.7），但对 RF 最重要的 perplexity 类特征（var_ppl、mean_ppl）完全失败（R²远低于0）**。Spearman ρ 几乎相同（RoBERTa -0.456 vs DeBERTa -0.484），Top-5 overlap 均为 0——这证实了 transformer 模型与 RF 关注的特征空间是系统性正交的，而非单一模型的偶然现象。RoBERTa 在 var_ppl 上的崩溃更极端（R²=-4215 vs DeBERTa 的 -28），进一步说明 token-level perplexity 分布的高阶统计量是 transformer 表征的盲区。

---
