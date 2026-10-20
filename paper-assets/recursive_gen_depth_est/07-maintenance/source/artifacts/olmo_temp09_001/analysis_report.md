# olmo_temp09_001 实验分析报告

**实验**: OLMo-1B + temperature-only τ=0.9 递归生成深度估计
**日期**: 2026-05-15
**状态**: **SUCCESS**

---

## 1. Pipeline 概要

| 阶段 | 状态 | 备注 |
|------|------|------|
| LoRA finetune ×3 | ✅ | depth_0/1/2, 3 epochs each |
| Generate ×3 | ✅ | depth_1/2/3, 5000 samples each |
| Feature extraction | ✅ | OLMo-1B perplexity features |
| 4-class classification | ✅ | RF + LR |
| 3-class classification | ✅ | d1/d2/d3 only |
| 3-class filtered | ✅ | code contamination removed |

## 2. Finetune Loss

| Depth | Final Loss |
|-------|-----------|
| depth_0 | 2.2684 |
| depth_1 | 1.6294 |
| depth_2 | 1.1769 |

Loss 逐层递减，符合预期（递归生成的文本分布逐渐窄化，更易拟合）。

## 3. Code Contamination

| Depth | Broad Filter | Narrow Filter |
|-------|-------------|---------------|
| depth_0 | 25 (0.5%) | 20 (0.4%) |
| depth_1 | 78 (1.6%) | 35 (0.7%) |
| depth_2 | 21 (0.4%) | 17 (0.3%) |
| depth_3 | 11 (0.2%) | 11 (0.2%) |

Code contamination 极低，不影响分类结果。depth_1 broad filter 略高（1.6%），但 narrow filter 仅 0.7%。

## 4. 4-Class Classification

| Classifier | Accuracy | 95% CI |
|-----------|----------|--------|
| Random Forest | **82.03%** | [80.87%, 83.20%] |
| Logistic Regression | 81.55% | [80.35%, 82.80%] |
| Random Baseline | 25.60% | - |
| Majority Baseline | 25.00% | - |

**Per-class (RF)**:

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| depth-0 | 1.00 | 1.00 | 1.00 |
| depth-1 | 0.91 | 0.87 | 0.89 |
| depth-2 | 0.66 | 0.66 | 0.66 |
| depth-3 | 0.73 | 0.76 | 0.74 |

depth-0 完美分离。主要混淆在 depth-2/3 之间。

## 5. Pairwise AUC (Random Forest)

| Pair | AUC |
|------|-----|
| d0 vs d1 | 0.9960 |
| d0 vs d2 | 0.9997 |
| d0 vs d3 | 0.9995 |
| **d1 vs d2** | **0.9010** |
| d1 vs d3 | 0.9874 |
| **d2 vs d3** | **0.8214** |

所有 pairwise AUC > 0.82，最弱分离 d2v3=0.8214 仍然良好。

## 6. 3-Class Classification (d1/d2/d3)

| Classifier | Accuracy | 95% CI |
|-----------|----------|--------|
| Random Forest | 75.73% | [74.10%, 77.27%] |
| Logistic Regression | 76.10% | [74.60%, 77.67%] |

**3-Class Filtered** (code removed):

| Classifier | Accuracy | 95% CI |
|-----------|----------|--------|
| Random Forest | **77.57%** | [75.96%, 79.15%] |
| Logistic Regression | 77.13% | [75.69%, 78.61%] |

Filtered 版本略优于未过滤版本（+1.84pp RF），说明去除 code contamination 后分类更纯净。

### 3-Class Pairwise AUC (RF)

| Pair | Unfiltered | Filtered |
|------|-----------|----------|
| d1 vs d2 | 0.8895 | 0.8923 |
| d1 vs d3 | 0.9900 | 0.9916 |
| d2 vs d3 | 0.8344 | 0.8391 |

## 7. Feature Importance (Top-5)

| Feature | Importance |
|---------|-----------|
| p90_ppl | 19.87% |
| var_surprisal | 17.41% |
| p75_ppl | 12.63% |
| mean_surprisal | 11.39% |
| p50_ppl | 5.10% |

Perplexity 分位数和 surprisal 统计量占据主导地位，合计 top-5 贡献 66.4%。

## 8. 对比分析

### vs OLMo Nucleus Baseline (cross_model_olmo_002)

| Metric | OLMo temp09 | OLMo nucleus | Δ |
|--------|------------|-------------|---|
| 4-class RF acc | **82.03%** | 78.77% | **+3.26pp** |
| 4-class LR acc | **81.55%** | 75.08% | **+6.47pp** |
| 3-class RF acc | 75.73% | 74.40% | +1.33pp |
| 3-class LR acc | **76.10%** | 70.83% | **+5.27pp** |
| d0v1 AUC (RF) | **0.9960** | 0.9834 | +0.0126 |
| d1v2 AUC (RF) | **0.9010** | 0.8673 | **+0.0337** |
| d2v3 AUC (RF) | **0.8214** | 0.8124 | +0.0090 |
| d1v3 AUC (RF) | **0.9874** | 0.9806 | +0.0068 |

**结论**: OLMo temp09 全面优于 OLMo nucleus baseline。4-class RF 提升 +3.26pp，LR 提升更大 +6.47pp。关键 pairwise d1v2 AUC 提升 +3.37%，说明 temperature-only 解码在 OLMo 上产生更强的深度分离信号。

### vs Pythia temp09 (pythia_temp09_001, 同策略跨模型)

| Metric | OLMo temp09 | Pythia temp09 | Δ |
|--------|------------|--------------|---|
| 4-class RF acc | **82.03%** | 76.25% | **+5.78pp** |
| 4-class LR acc | **81.55%** | 74.05% | **+7.50pp** |
| d0v1 AUC (RF) | 0.9960 | 0.9968 | -0.0008 |
| d1v2 AUC (RF) | **0.9010** | 0.8327 | **+0.0683** |
| d2v3 AUC (RF) | **0.8214** | 0.7928 | **+0.0286** |
| d1v3 AUC (RF) | **0.9874** | 0.9590 | +0.0284 |

**结论**: 同一 temperature-only τ=0.9 策略下，OLMo-1B 显著优于 Pythia-1.4B。4-class RF 差距 +5.78pp，关键 d1v2 AUC 差距 +6.83%。OLMo 在递归生成中产生更大的统计分布漂移，更易被检测。

## 9. 总结

### 判定: **SUCCESS** ✅

- 4-class acc = 82.03% > 40% ✓
- d1v2 AUC = 0.9010 > 0.6 ✓

### 关键发现

1. **OLMo + temp09 是目前所有实验中 4-class 准确率最高的配置** (82.03%)
2. Temperature-only 解码在 OLMo 上效果优于 nucleus sampling (+3.26pp)
3. OLMo 在 temp09 策略下显著优于 Pythia (+5.78pp)，说明模型架构/训练数据对递归深度可检测性有重要影响
4. depth-0 完美分离（F1=1.00），主要瓶颈在 depth-2 vs depth-3 区分（AUC=0.8214）
5. Code contamination 极低（narrow ≤0.7%），filtered 版本甚至略优
6. Perplexity 分位数（p90/p75/p50）和 surprisal 统计量是最重要的区分特征
