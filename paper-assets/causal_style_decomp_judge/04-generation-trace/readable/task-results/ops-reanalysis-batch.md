# ops reanalysis batch

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_reanalysis_batch_20260520T234525_result.json`
- **Structured JSON:** [`155d90adeddeafd10c49.json`](../../sessions/15/155d90adeddeafd10c49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部完成。以下是完整报告：

---

## exp-011: NLI Threshold Sensitivity

### Formality axis (n=100)
```
Threshold    N pass     Pass%      NLI mean     BS mean      PW N     PW win%    PW p
0.70         89         89.0       0.9894       0.8799       47       72.3       0.0031
0.75         89         89.0       0.9894       0.8799       47       72.3       0.0031
0.80         89         89.0       0.9894       0.8799       47       72.3       0.0031
0.85         89         89.0       0.9894       0.8799       47       72.3       0.0031
0.90         88         88.0       0.9906       0.8798       46       73.9       0.0016
0.95         85         85.0       0.9925       0.8794       45       73.3       0.0025

NLI distribution: mean=0.8956, std=0.2792, min=0.0001, max=0.9990
formal (n=59): NLI mean=0.8793
casual (n=41): NLI mean=0.9190
```

**关键发现：** 0.70→0.90 阈值范围内 pass rate 几乎不变（89%→88%），说明 NLI 分布是双峰的（大部分样本要么 >0.90 要么很低），**0.90 阈值不在 cliff edge 上**。Pairwise win rate 在所有阈值下稳定在 72-74%，p<0.005，结论 robust。

### Tone axis (n=20)
```
Threshold    N pass     Pass%      NLI mean     BS mean
0.70         13         65.0       0.9903       0.9399
0.75         13         65.0       0.9903       0.9399
...
0.95         13         65.0       0.9903       0.9399

NLI distribution: mean=0.7039, std=0.4208
assertive (n=13): NLI mean=0.6559
hedging (n=7): NLI mean=0.7930
```

**关键发现：** Tone 在 0.70 阈值下 pass rate = 65%，比 formality 的 89% 低很多。7/20 样本 NLI < 0.70，说明 tone counterfactual 质量显著差于 formality。Assertive 方向的 NLI 尤其低（0.6559），暗示 assertive→hedging 的 rewrite 改变了更多内容。

---

## exp-012: Consistency Filter Bias Analysis

```
Total valid: 98
Consistent:   55 (56.1%)
Inconsistent: 43 (43.9%)

--- NLI Score ---
Consistent (n=55):   mean=0.8588, std=0.3270
Inconsistent (n=43): mean=0.9383, std=0.2056
Mann-Whitney U: U=1214.0, p=0.824367
KS test: D=0.1383, p=0.680267

--- BERTScore ---
Consistent (n=55):   mean=0.8547
Inconsistent (n=43): mean=0.8847
Mann-Whitney U: U=965.0, p=0.120293

--- Response Length ---
Original length — consistent: mean=560, inconsistent: mean=733
  Mann-Whitney U: p=0.137405
|orig-cf| length diff — consistent: mean=110, inconsistent: mean=127
  Mann-Whitney U: p=0.714958

--- Position Bias ---
Consistent (n=55): Trial1 A rate=69.1%, Trial2 A rate=30.9%
Inconsistent (n=43): Trial1 A rate=55.8%, Trial2 A rate=55.8%

--- Interpretation ---
✓ No significant systematic bias detected in consistency filter
```

**关键发现：** 
- NLI、BERTScore、response length 在 consistent/inconsistent 组间**均无显著差异**（所有 p > 0.12）
- 43.9% 的不一致率合理
- Consistent 组的 position bias 符合预期（Trial1 A=69%, Trial2 A=31%，互补），inconsistent 组则 Trial1/Trial2 都是 55.8%（随机）
- **结论：一致性过滤不引入系统性偏差**

---

## exp-014: Logistic Decomposition

### Direction-Asymmetry Analysis
```
Consistent pairs: 55

--- formal→casual (n=33) ---
formal wins: 26/33 (78.8%)
95% CI (Wilson): [0.6225, 0.8932]
Sign test p: 0.001319  ← Significant: YES
Interpretation: formal=original → formal win = prefer ORIGINAL
  Formality effect and original preference are CONFOUNDED

--- casual→formal (n=22) ---
formal wins: 12/22 (54.5%)
95% CI (Wilson): [0.3466, 0.7308]
Sign test p: 0.831812  ← Significant: NO
Interpretation: casual=original → formal win = prefer REWRITE
  This subset cleanly isolates formality effect from original preference
```

### Logistic Regression
```
Observations: 196 (2 trials × 98 records)

Intercept (position A bias): -0.5851

formal_effect:
  Coefficient: 0.7928 (SE=0.3117)
  95% CI (bootstrap): [0.2029, 1.4304]
  Odds ratio: 2.2095
  z=2.5434, p=0.010979  ← Significant: YES

original_effect:
  Coefficient: 0.5958 (SE=0.3012)
  95% CI (bootstrap): [0.0135, 1.1914]
  Odds ratio: 1.8145
  z=1.9781, p=0.047914  ← Significant: YES
```

**关键发现：**
- **Formality effect**: coefficient=0.79, OR=2.21, p=0.011 — 显著。控制 original preference 后，formal 版本仍有 2.2x 的 odds 被偏好
- **Original preference effect**: coefficient=0.60, OR=1.81, p=0.048 — 勉强显著。judges 倾向选择原始版本（OR=1.81）
- **casual→formal 子集**（关键隔离子集）：formal win rate = 54.5%，CI 跨 50%，not significant。在这个 formality effect 与 original preference 对冲的子集中，formality bias 被 original preference 几乎完全抵消
- **formal→casual 子集**：78.8% formal wins（p=0.001），但这里两个效应混淆叠加，不能单独归因

---
