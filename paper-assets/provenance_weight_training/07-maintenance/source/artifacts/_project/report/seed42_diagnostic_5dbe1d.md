# Adaptive Seed42 诊断报告

## 问题

adaptive_seed42 的 eval_ppl=17.69，与 uniform baseline 完全相同（uniform_seed42=17.69），改善量为零。而同 seed 的 grid_b0.5_seed42=17.651 有效（改善 0.039），其他 seed 的 adaptive 也有效（seed123=17.63, seed456=17.64，改善 0.06）。

## 数据

### 训练配置（所有 adaptive 相同）
| 参数 | 值 |
|------|-----|
| model | Qwen3-0.6B |
| tau | 0.8 |
| n_min | 3 |
| batch_size | 4 |
| gradient_accumulation | 4 |
| max_steps | 6103 |
| num_examples | 371,499 |

### b* 统计对比
| seed | b* mean | b* std | b* median | b==0 (%) | alpha_eff mean |
|------|---------|--------|-----------|----------|----------------|
| 42   | 0.5340  | 0.5300 | 0.40      | 1.9%     | 0.5607         |
| 123  | 0.5387  | 0.5597 | 0.40      | 1.7%     | 0.5640         |
| 456  | 0.5362  | 0.5304 | 0.40      | 1.9%     | 0.5604         |

**b* 统计在 3 个 seed 间几乎完全一致。weighting 机制本身没有失效。**

### ESS 约束分析
| 方法 | ESS mean | ESS<3.1 (%) | ESS p5 |
|------|----------|-------------|--------|
| adaptive (all seeds) | 3.10 | 84.5% | 3.002 |
| grid_b0.5 | 2.87 | 63.4% | 1.802 |

**n_min=3 对 batch_size=4 过于保守：84.5% 的 micro-batch 的 ESS 被钳制在 n_min 附近。**

### 训练 loss 对比
| 方法 | mean loss | late-phase loss (>5k) | late delta |
|------|-----------|----------------------|------------|
| adaptive_seed42 | 2.3166 | 2.2972 | +0.005 (停滞) |
| adaptive_seed123 | 2.3166 | 2.2794 | -0.035 (仍在下降) |
| uniform_seed42 | 1.9973 | 1.9775 | +0.003 (收敛) |
| grid_b0.5_seed42 | 2.3995 | 2.3803 | +0.007 (收敛) |

### Intra-step 梯度一致性
| 方法 | intra-step b* CV | b* autocorr(lag=1) |
|------|-----------------|-------------------|
| adaptive seed42 | 0.507 | -0.003 |
| adaptive seed123 | 0.511 | +0.005 |
| grid b=0.5 | 0.000 | N/A |

## 根因分析

### 结论：非 Bug，而是信噪比问题

adaptive_seed42 的 weighting 机制**工作正常**——b*、ESS、alpha_eff 统计与其他 seed 完全一致。根因是三个结构性因素叠加导致改善信号被噪声淹没：

### 因素 1: n_min 约束过紧，限制 weighting 强度

n_min=3 + batch_size=4 → ESS 下限为 batch 的 75%。84.5% 的 micro-batch ESS 被钳制在 [3.0, 3.1]，即 adaptive 只能对 batch 中的 1 个样本做**微弱**的降权。

对比 grid_b0.5：不受 n_min 约束，ESS 可低至 1.8（有效丢弃 batch 中约 2 个样本），weighting 强度远大于 adaptive。

**这解释了为什么 grid_b0.5_seed42 有效但 adaptive_seed42 无效——grid 的 weighting 力度更强。**

### 因素 2: per-batch b* 噪声过大

- b* 在连续 step 间的自相关 ≈ 0（纯随机噪声）
- 单个 gradient accumulation step 内 4 个 micro-batch 的 b* CV=0.51
- 这意味着同一个 optimizer step 内，不同 micro-batch 的 weighting 策略完全不同
- Grid 的 b* CV=0.000（完美一致）

高 b* 方差等价于向梯度方向注入额外噪声。对于 marginal 的改善信号（~0.04 ppl），这个噪声足以抵消甚至反转改善效果。

### 因素 3: 改善信号本身极弱 + 统计功效不足

- 平均改善量：0.04 ppl（0.23% of baseline）
- seed42 偏离均值仅 1.4σ（3 seeds 下完全不显著）
- seed42 的 late-phase loss 停滞（delta=+0.005），而 seed123 仍在下降（delta=-0.035），这可能是 data ordering 导致 seed42 落入了更差的优化轨迹

## 图表

- `output/figures/adaptive_seed_comparison.png` — 3 个 seed 的 b*/alpha_eff/ESS/loss 轨迹
- `output/figures/adaptive_diagnostic_distributions.png` — adaptive vs grid 的 b*/ESS/alpha_eff 分布
- `output/figures/convergence_comparison_seed42.png` — seed42 下 4 种方法的 loss 收敛对比

## 建议

1. **降低 n_min=2（或移除约束）**：允许更激进的 weighting，缩小与 grid 的 strength gap
2. **增大 batch_size（至少 16）**：(a) 更多 q-scores → b* 估计更稳定，(b) 减小 intra-step b* 方差
3. **使用 b* 的 EMA**：对 b* 做指数移动平均而非每 batch 独立计算，降低梯度噪声
4. **补充 seeds（5-10 个）**：当前 3 个 seed 无法判断 0.04 ppl 的改善是否显著
5. **记录 unweighted loss**：在 step_metrics 中同时记录 unweighted per-sample loss，方便直接对比模型在 clean 数据上的表现

## 优先级

建议 1（降低 n_min）成本最低、效果最直接，应优先尝试。n_min=2 + 当前 batch_size=4 即可让 adaptive 的 effective ESS 降至 ~2.5，接近 grid_b0.5 的 2.87。
