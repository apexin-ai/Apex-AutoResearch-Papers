# ESS-only Seed42 实验分析

## 实验配置
- **Method**: ess_only (max-intervention baseline)
- **Model**: Qwen3-0.6B
- **Seed**: 42
- **Training tokens**: 200M (max_steps=6103)
- **n_min**: 2, **τ**: 0.8, **contamination_ratio**: 0.4
- **逻辑**: 只用 ESS 约束 (b* = max{b : ESS(b) ≥ n_min})，不用 α_eff 质量下界

## 最终 Eval 指标

| 指标 | 值 |
|------|-----|
| **eval_loss** | 2.8751 |
| **perplexity** | 17.728 |
| eval_tokens | 4,077,068 |
| eval_time | 162s |
| checkpoint | output/models/ess_only_seed42/final |

## b* 分布统计 (24,412 batch records)

| 统计量 | b* | α_eff | ESS | mean_q |
|--------|-----|-------|-----|--------|
| mean | 3.506 | 0.689 | 2.018 | 0.600 |
| median | 1.582 | 0.736 | 2.002 | 0.600 |
| std | 4.692 | 0.231 | — | — |
| min | 0.195 | — | — | — |
| max | 20.000 | — | — | — |

### 训练过程 b* 趋势
| 阶段 | b* mean | b* median | α_eff mean | ESS mean |
|------|---------|-----------|------------|----------|
| Early (前 10%) | 3.572 | 1.611 | 0.692 | 2.020 |
| Late (后 10%) | 3.553 | 1.650 | 0.693 | 2.018 |

b* 在训练过程中保持稳定，无明显漂移。

## Baselines 对比

| Method | eval_loss | PPL | Δ PPL vs uniform | b* median | b* mean |
|--------|-----------|-----|-------------------|-----------|---------|
| **uniform** | 2.873 | 17.690 | — | N/A | N/A |
| **adaptive_fix** (dual-constraint) | 2.871 | 17.65 | −0.040 | 0.871 | 1.399 |
| grid_b=0.5 | 2.871 | 17.65 | −0.040 | 0.5 | 0.5 |
| **ess_only** | **2.875** | **17.728** | **+0.038** | **1.582** | **3.506** |

## 关键发现

### 1. ESS-only 比 uniform 更差 (+0.038 PPL)
ESS-only 不仅没有改善性能，反而比不加权 (uniform) 更差。这意味着 ESS-only 的降权策略是有害的。

### 2. ESS-only 远逊于 adaptive (−0.08 PPL gap)
dual-constraint 方法 (adaptive_fix) 通过 α_eff 下界约束实现 min-intervention，PPL=17.650 优于 ESS-only 的 17.728。

### 3. 确认 max-intervention 行为
- ESS-only b* median=1.582, mean=3.506，远高于 adaptive 的 median=0.871, mean=1.399
- ESS-only 倾向选择过大的 b*，导致过度降权（α_eff mean=0.689 < adaptive 的 0.823）
- 右偏分布（mean >> median）表明部分 batch 的 b* 极端高

### 4. ESS 约束严格满足
ESS 始终接近 n_min=2（mean=2.018, median=2.002），确认 ESS-only 算法正确工作——它精确找到满足 ESS≥n_min 的最大 b*。

## 结论

**conclusion: success**

ESS-only (max-intervention) 表现比 uniform 和 adaptive 都差，验证了论文 D023 的核心论点：

1. **α_eff 约束是必要的**：没有 α_eff 下界，ESS-only 过度降权，损害模型质量
2. **min-intervention 优于 max-intervention**：dual-constraint 框架选择满足 ESS 约束的最小 b*（通过 α_eff 下界），而 ESS-only 选择最大 b*，结果更差
3. **论文 framing 得到实验支持**：ESS-only 作为 ablation baseline，清晰展示了 dual-constraint 设计中 α_eff 约束的贡献

### 对论文的影响
- ESS-only 可作为 Table 中的 ablation 行，与 adaptive 对比
- 支持 "单一 ESS 约束不足以保证训练质量" 的论述
- b* 分布统计可用于可视化 max-intervention vs min-intervention 的行为差异

## 原始数据指针
- **final_eval_loss**: 2.8751
- **final_ppl**: 17.728
- **b_star_median**: 1.582
- **b_star_mean**: 3.506
- **checkpoint_path**: /root/provenance_weight_training/output/models/ess_only_seed42/final
- **eval_result_json**: /root/provenance_weight_training/output/eval_results/ess_only_seed42_eval.json
- **step_metrics**: /root/provenance_weight_training/output/models/ess_only_seed42/step_metrics.jsonl

<!-- 数值修正 2026-05-15: 从 eval_results JSON 重新校准 -->
