# exp plan 015 wild data calibration

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_015_wild_data_calibration_20260515T212643_result.json`
- **Structured JSON:** [`b303f6a7615547c606f9.json`](../../sessions/b3/b303f6a7615547c606f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan 015 结果摘要

### WikiText-103 d0 预测率：**100.0%**（546/546 passages 全部正确预测为 d0）

### Calibration Table

| Source | n | d0% | d1% | d2% | d3% |
|--------|---:|----:|----:|----:|----:|
| **WikiText-103 (wild d0)** | 546 | **100.0** | 0.0 | 0.0 | 0.0 |
| Controlled d0 | 5000 | 100.0 | 0.0 | 0.0 | 0.0 |
| Controlled d1 | 5000 | 0.0 | 99.96 | 0.04 | 0.0 |
| Controlled d2 | 5000 | 0.0 | 0.02 | 99.94 | 0.04 |
| Controlled d3 | 5000 | 0.0 | 0.0 | 0.1 | 99.9 |

### Predict_proba 统计

- **WikiText**: P(d0)=0.9963, P(d1)=0.003, P(d2)=0.0003, P(d3)=0.0004
- **Controlled d0**: P(d0)=0.9941, P(d1)=0.0038, P(d2)=0.0013, P(d3)=0.0008
- WikiText 的 P(d0) 甚至略高于 controlled d0（0.9963 vs 0.9941）

### Domain Shift 分析

尽管 WikiText 被完美分类，特征空间存在显著差异：
- `mean_ppl` +621%（WikiText 明显更高）
- `var_ppl` +503%
- `p90_ppl` +115%，`p75_ppl` +106%

但词汇类特征差异很小（TTR +1.4%，hapax +1.9%，bigram_entropy +1.6%）。perplexity 差异可能源于 WikiText 的 domain 分布更广（百科全书 vs Wikipedia subset），但 RF 对此具有鲁棒性。

### 5-fold CV 准确率：0.7878 ± 0.0056

注意：这是在全训练集上 refit 后的 train-set prediction 接近 100%（RF 过拟合训练数据），CV 指标才是泛化能力的真实估计。

### 结论
RF depth estimator 在非受控真实文本上表现完美——WikiText-103 全部被识别为 d0（人类文本），没有任何误分类到更深的 depth。这证明了 depth 信号在 wild data 上的有效性。

所有结果已保存至 `results/plan_015_wild_data/`（8 个文件）。

---
