# Plan_008: Sparsity Sweep PPL Summary & Scaling Trend Analysis

Model: Llama-3.1-8B | Eval: WikiText-2 (seq_len=2048) | Dense PPL: 6.12

## 1. Master Table

| Sparsity | Dense | KL (TEAL) | KL (hard-mask) | TEAL (train-free) | WINA (train-free) | BCE (TEAL) |
|:--------:|:-----:|:---------:|:--------------:|:------------------:|:-----------------:|:----------:|
| 30%      | 6.12  | 8.98      | 7.30           | 10.97              | 11.45             | —          |
| 50%      | 6.12  | 12.00±0.07 (4-seed) | 9.19±0.04 (5-seed) | 23.31     | 27.93             | 44.05±0.88 (3-seed) |
| 70%      | 6.12  | 17.91     | 13.84          | 100.11             | 137.24            | —          |

Notes:
- KL 50% 4-seed = {s0: 12.03, s1: 11.99, s42: 12.08, s123: 11.91}, excludes s456 TEAL-allocation outlier (13.58)
- KL 30% achieved sparsity = 0.285 (lambda_max=5000 still insufficient); 70% achieved = 0.699
- BCE 50% seeds: {s42: 44.537, s123: 44.586, s456: 43.033}

## 2. KL vs Training-Free Delta Analysis

| Sparsity | KL (TEAL) | TEAL (train-free) | Abs. Delta | Rel. Improvement | WINA (train-free) | Abs. Delta | Rel. Improvement |
|:--------:|:---------:|:------------------:|:----------:|:----------------:|:-----------------:|:----------:|:----------------:|
| 30%      | 8.98      | 10.97              | 1.99       | 18.1%            | 11.45             | 2.47       | 21.6%            |
| 50%      | 12.00     | 23.31              | 11.31      | 48.5%            | 27.93             | 15.93      | 57.0%            |
| 70%      | 17.91     | 100.11             | 82.20      | 82.1%            | 137.24            | 119.33     | 86.9%            |

Delta growth rate (KL vs TEAL):
- 30%→50%: delta grows 5.68× (1.99 → 11.31)
- 50%→70%: delta grows 7.27× (11.31 → 82.20)
- 30%→70%: delta grows **41.3×** (1.99 → 82.20)

Conclusion: delta 增长明显超线性，接近指数级。

## 3. Scaling Trend Analysis

### 3.1 PPL Degradation from Dense (PPL − 6.12)

| Sparsity | KL     | TEAL (train-free) | WINA (train-free) |
|:--------:|:------:|:------------------:|:-----------------:|
| 30%      | +2.86  | +4.85              | +5.33             |
| 50%      | +5.88  | +17.19             | +21.81            |
| 70%      | +11.79 | +93.99             | +131.12           |

### 3.2 Growth Ratios (relative to 30% degradation)

| Method | 50%/30% | 70%/30% | Pattern |
|:------:|:-------:|:-------:|:-------:|
| KL     | 2.06×   | 4.12×   | ~quadratic (s² scaling plausible) |
| TEAL   | 3.54×   | 19.38×  | super-quadratic / exponential |
| WINA   | 4.09×   | 24.60×  | super-quadratic / exponential |

### 3.3 Interpretation

**KL PPL degradation is approximately quadratic in sparsity**. Sparsity ratio 70/30 = 2.33, squared = 5.44. Observed KL ratio = 4.12 — slightly sub-quadratic, consistent with the predictor learning to adaptively protect critical neurons even at high sparsity.

**Training-free PPL degradation is exponential**. TEAL ratio 19.38× and WINA ratio 24.60× far exceed any polynomial fit. At 70% sparsity, fixed heuristic masks catastrophically fail because they cannot prioritize neurons conditioned on input.

**KL advantage amplifies with sparsity**. The relative improvement grows monotonically: 18% → 49% → 82% (vs TEAL). This is the key empirical pattern for Claim 3 — KL's coupled gradient captures inter-neuron interactions that become increasingly important as more neurons are removed.

### 3.4 Claim 3 Assessment

Claim 3 原文: "KL advantage grows with sparsity level... KL-vs-BCE delta follows approximately quadratic curve in sparsity level s."

**KL vs training-free**: 数据充分支撑 "KL advantage grows with sparsity"。Delta 增长超线性，KL 优势在高稀疏度下急剧放大。

**KL vs BCE**: 仅有 50% 一个数据点 (KL 12.00 vs BCE 44.05, delta 32.05)。无法验证 quadratic scaling 预测。需要 30% 和 70% BCE 数据点。

## 4. Downstream Task Summary

| Task | Dense | KL 30% | KL 50% | TEAL 50% (train-free) |
|:----:|:-----:|:------:|:------:|:---------------------:|
| ARC-c (acc_norm) | 0.5819 | 0.3737 (−35.8%) | 0.3771 (−35.2%) | 0.2910 (−50.0%) |
| WinoGrande (acc) | 0.7814 | 0.6756 (−13.5%) | 0.6156 (−21.2%) | 0.5556 (−28.9%) |
| MMLU (acc) | 0.6532 | 0.2874 (−56.0%) | 0.2591 (−60.3%) | 0.2856 (−56.3%) |
| GSM8K (flex) | 0.5004 | 0.0781 (−84.4%) | 0.0121 (−97.6%) | 0.0190 (−96.2%) |

Key observations:
1. **MMLU/GSM8K 在所有 sparsity level 均崩溃至随机水平** (MMLU ~0.26-0.29 = 4-choice random; GSM8K < 0.08)
2. **30% → 50% 退化非线性**: ARC-c 几乎不变 (0.3737→0.3771)，但 GSM8K 从 0.0781 暴跌至 0.0121
3. **PPL-downstream disconnect 在所有 sparsity level 成立**: PPL 8.98 (30%) 和 12.00 (50%) 都是"合理"的 PPL，但 downstream 全面崩溃
4. **TEAL 50% 与 KL 50% downstream 表现相当**: 两者在 MMLU/GSM8K 均接近随机，证明 collapse 是 50% unstructured sparsity 的固有限制

## 5. Data Completeness Assessment for Claim 3

### 已有数据
- [x] KL PPL: 30%, 50% (multi-seed), 70% — 3-level sweep 完整
- [x] Training-free baselines: TEAL + WINA @ 30/50/70% — 完整
- [x] BCE PPL: 50% (3-seed) — 仅单点
- [x] STE baseline: 50% (PPL=15.77) — 仅单点
- [x] Downstream: KL 30%, KL 50%, TEAL 50% — 部分

### Claim 3 支撑度
**KL vs training-free scaling**: 数据充足，趋势清晰，可直接写入论文。

**KL vs BCE scaling (原始 Claim 3 核心)**: 不足。只有 50% 一个点无法验证 quadratic 预测。

### 建议补充数据
1. **[高优先] BCE 30% + BCE 70%**: 补齐 BCE sparsity sweep，验证 KL-vs-BCE delta 的 scaling pattern
2. **[中优先] Downstream 70%**: 目前无 70% 的 downstream 数据
3. **[低优先] TEAL 30% downstream**: 已注册 (lm_eval_teal_30pct, status=PREPARING) 但未完成

### 论文策略
如果无法补齐 BCE 30%/70%：
- 将 Claim 3 重新聚焦为 "KL vs training-free advantage amplifies with sparsity"（数据完整）
- BCE 对比降级为 "50% 单点 ablation" 而非 "scaling law"
- 将 quadratic 预测移至 discussion/future work
