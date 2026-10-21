# pythia_topk50_001 实验分析报告

## 实验配置
- 模型: Pythia-1.4B, LoRA r=16
- 采样: top-k k=50, temperature=1.0
- 数据: 5000 samples/depth, 4 depths (d0-d3)
- Pipeline: 3x finetune + 3x generate + feature extraction + classification

## 核心指标

| 指标 | 值 |
|------|-----|
| RF 4-class acc | **69.6%** (CI: 68.3%-71.1%, chance 25%) |
| LR 4-class acc | 68.2% |
| RF 3-class acc (d1-d3) | **59.2%** (CI: 57.5%-61.1%, chance 33.3%) |
| RF 3-class filtered acc | **61.3%** (CI: 59.3%-63.1%) |

## Pairwise AUC (Random Forest)

| Pair | topk50 | baseline (nucleus) | temp09 |
|------|--------|-------------------|--------|
| d0v1 | 0.9927 | 0.9975 | — |
| d0v2 | 0.9983 | — | — |
| d0v3 | 0.9978 | — | — |
| d1v2 | **0.7518** | 0.8607 | 0.8327 |
| d1v3 | 0.9176 | — | — |
| d2v3 | **0.6918** | 0.8005 | 0.7928 |

## vs Baseline (nucleus p=0.95) 对比

| Metric | topk50 | baseline | Δ |
|--------|--------|----------|------|
| 4-class acc | 69.6% | 78.2% | **-8.6pp** |
| 3-class acc | 59.2% | 70.8% | **-11.6pp** |
| d0v1 AUC | 0.9927 | 0.9975 | -0.005 |
| d1v2 AUC | 0.7518 | 0.8607 | **-0.109** |
| d2v3 AUC | 0.6918 | 0.8005 | **-0.109** |

## vs temp09 对比

| Metric | topk50 | temp09 | Δ |
|--------|--------|--------|------|
| 4-class acc | 69.6% | 76.25% | **-6.65pp** |
| 3-class acc | 59.2% | 69.83% | **-10.6pp** |
| d1v2 AUC | 0.7518 | 0.8327 | -0.081 |
| d2v3 AUC | 0.6918 | 0.7928 | -0.101 |

## Feature Importance

Top-5 与 baseline **完全一致**:
1. var_surprisal (0.176)
2. p90_ppl (0.135)
3. mean_ppl (0.112)
4. mean_surprisal (0.070)
5. p75_ppl (0.061)

## Finetune Loss
- depth_0: 2.2406
- depth_1: 1.6704
- depth_2: 1.4374

## Code Contamination (narrow filter)
- d0: 0.4%, d1: 7.7%, d2: 12.3%, d3: 13.1%
- 高于 baseline，top-k 产生更多 code-like text
- Filtered 3-class (61.3%) > unfiltered (59.2%)，code 不是深度信号的主因

## 结论: SUCCESS

深度信号在 top-k 采样下存在（69.6% >> 25% chance, d1v2 AUC 0.7518 >> 0.5），满足 PASS 条件。

但信号强度低于 baseline (-8.6pp) 和 temp09 (-6.65pp)，超出 5pp 阈值。排序: **nucleus > temp09 > topk50**。

Feature importance 排序一致，表明三种策略下深度信号的统计特征模式相同，差异仅在信号强度。

**解读**: Top-k 的硬截断（仅保留概率最高的 k 个 token）比 nucleus/temperature 的软概率重分配丢失了更多深度相关的分布特征，但核心信号仍可检测。跨策略泛化**定性成立**，但**定量存在衰减**。
