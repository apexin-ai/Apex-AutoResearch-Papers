# Drayson et al. (EMNLP 2025) 新颖性差异化调研报告

> 调研日期: 2026-05-14
> 关联决策: D013

---

## 1. Drayson et al. 摘要

### 论文信息
- **全名**: Machine-generated text detection prevents language model collapse
- **作者**: George Drayson, Emine Yilmaz, Vasileios Lampos
- **单位**: University College London (UCL)
- **Venue**: EMNLP 2025 Main Conference (arXiv: 2502.15654)
- **代码**: https://github.com/GeorgeDrayson/model_collapse

### 方法
- **公式**: wⱼ = (1−q(xⱼ))^b / Σₗ(1−q(xₗ))^b
  - q(x): ModernBERT 检测器输出的 machine-generated 概率（AUC=0.986 in-domain, 0.943 OOD）
  - b ≥ 1: bias term，控制权重分布倾斜程度
- **采样策略**: Sampling Importance Resampling (SIR)——按权重有放回采样 n×k 个样本（k=1.5），加 rmax 上限防止单样本过度重复
- **检测器**: ModernBERT fine-tuned on MAGE dataset，label smoothing α=0.1，temperature scaling 校准

### b 的选择方式
- **验证集选取，非 grid search，也非 adaptive**
- 具体做法："We select values for rmax and b by evaluating each model on the Wikitext-2 validation set after 1 generation of recursive training"
- 实际使用的值：
  - GPT-2 (124M): b=10
  - SmolLM 135M: b=10
  - SmolLM 360M: b=10
  - SmolLM 1.7B: b=1
- **无系统性的 b 敏感度分析或 ablation**

### 实验设置
- **数据**: WikiText-2 (36,718 training documents)
- **模型**: GPT-2 124M, SmolLM2 135M/360M/1.7B (2 model families, 4 models)
- **递归训练**: 10 generations of recursive fine-tuning
- **解码策略**: 6 种 (greedy, beam search, pure sampling, temperature, top-k, nucleus)
- **污染场景**: 3 种 mixing configurations (α,β,γ)，从 equal splits 到 cross-generational accumulation
- **评估指标**: Perplexity, diversity (distinct-n), MAUVE (semantic similarity)

### 主要 Claims
1. 模型坍塌受解码策略选择显著影响
2. 训练一个提供校准置信度估计的 MGT 检测器
3. 使用检测器输出通过引导数据重采样防止坍塌
4. 跨 4 个 LLM、2 个模型家族、6 种解码策略验证
5. 某些设置下甚至超越 "Oracle"（完美检测器）

### 结果
- Perplexity 改善: −0.85% to −25.65%
- Diversity 增益: +3.44% to +14.62%
- MAUVE 提升: +8.46% to +20.92%

---

## 2. 与我们方法的关键差异点

| 维度 | Drayson et al. (EMNLP 2025) | 我们 (provenance_weight_training) |
|------|---------------------------|----------------------------------|
| **b 选择** | 验证集 empirical 选取，固定于整个训练过程 | Adaptive b*：从 batch 统计量自适应推导，无需 grid search |
| **b 选择原则** | 无理论依据，启发式 | 基于 α_eff(b) 和 ESS 约束的 principled 推导 |
| **检测器** | ModernBERT (AUC=0.986)，强检测器 | TF-IDF + LR (AUC=0.939)，证明轻量检测器即可 |
| **污染比例** | 不假设已知（原文明确声明），但实验为控制设置 | 未知（从 batch 统计量估计 effective real fraction） |
| **应用场景** | Model collapse prevention (recursive training) | Web corpus contamination (unknown synthetic fraction) |
| **数据规模** | WikiText-2 (36K documents) | 132M+ tokens (FineWeb subset) |
| **生成器** | Single-generator-per-experiment | Multi-generator (cross-contamination) |
| **理论支撑** | 无（纯 empirical） | 收敛理论 motivated α_eff(b) 推导 |
| **框架贡献** | detect-and-reweight 作为一种方法 | soft-to-hard 连续谱统一框架 (b=0 → b→∞) |
| **动态性** | b 在训练中固定 | b* per-batch 自适应调整 |

### 核心差异化总结
Drayson et al. 提出了 detect-and-reweight 的框架和公式，但 b 的选择是 heuristic + model-specific validation。我们的贡献是：
1. **Adaptive b* without validation-set tuning**：通过 α_eff(b) 和 ESS 约束从 batch 统计量推导 b*，替代 per-model validation-based empirical selection
2. **Lightweight detector sufficiency**：证明不需要 SOTA 检测器
3. **Unknown proportion setting**（辅助）：方法自然适用于污染比例未知的场景，但此点非 vs Drayson 的核心差异（Drayson 原文也不假设已知比例）

---

## 3. 相关工作对比表

| 方法 | Venue | Adaptive b/weight? | b/weight 选择方式 | 数据规模 | 主要贡献 |
|------|-------|-------------------|------------------|---------|---------|
| **Drayson et al. (2025)** | EMNLP 2025 | ❌ | 验证集 empirical (b=1 or 10) | WikiText-2 (36K docs) | detect-and-reweight 防止 model collapse |
| **Ours** | targeting EMNLP 2026 | ✅ | α_eff(b) + ESS 约束推导 b* | 132M+ tokens | adaptive b* 替代 grid search |
| **DoReMi** (Xie et al.) | NeurIPS 2023 | ✅ (domain-level) | Group DRO 小模型代理优化 | The Pile (800GB) | 域权重优化加速预训练 |
| **DSIR** (Xie et al.) | NeurIPS 2023 | ❌ | Importance weights via n-gram features | The Pile (100M docs) | 数据选择匹配目标分布 |
| **IR-DRO** (Chen et al.) | arXiv 2024 | 半自适应 | KL-regularized softmax, r=10 fixed | C4, up to 7B model | 中等 loss 样本重加权 |
| **Dynamic Loss Reweighting** (Sow et al.) | ICLR 2025 | ✅ | Loss-based + temperature annealing | SlimPajama/FineWeb, up to 7B | 动态 loss-based 重加权 |
| **GREATS** (Wang et al.) | NeurIPS 2024 | ✅ | Taylor expansion + greedy selection | LLM pretraining scale | 在线 batch 选择 |
| **Golden Ratio** (2025) | arXiv | ❌ | Closed-form w* = (√(k²+4k)−k)/2 | Theoretical | 已知比例下最优混合权重 |
| **DCR** (Xu et al.) | EMNLP 2025 | N/A (evaluation) | Fuzzy inference system | 9 LLMs, 0.5B-72B | 评估阶段污染校正因子 |
| **"How Much Can We Forget"** | ICML 2025 | N/A (analysis) | N/A | up to 1.6B, 40B tokens | 污染遗忘动态分析 |
| **Strong Model Collapse** (Dohmatob et al.) | ICLR 2025 | N/A (theory) | N/A | Theoretical | 证明 0.1% 污染导致坍塌 |
| **Amin et al. (NeurIPS 2025)** | NeurIPS 2025 | ✅ | Boosting-inspired iterative | Curated (math/coding) | 弱标注器引导重加权 |

---

## 4. 关键发现

### 没有人做过 adaptive b* for contamination weighting
在搜索范围内（2024-2026），没有找到任何工作将 contamination detection score 的权重指数 b 进行自适应推导。现有工作要么：
- 固定/启发式选择 b (Drayson)
- 不使用 detection score，而是基于 loss (IR-DRO, Dynamic Loss Reweighting)
- 在 domain-level 而非 instance-level 做自适应 (DoReMi)
- 假设已知污染比例 (Golden Ratio)

### Drayson 的局限性（可在论文中明确指出）
1. b 选择需要 per-model validation run（实质是 grid search with validation）
2. 单生成器设置（不反映真实 web 多源污染）
3. 小规模数据（WikiText-2）
4. 无 b 敏感度分析（不知道 b 选错的代价）
5. b 选择依赖 validation set（每个新模型需重新 tune），无法零成本迁移

---

## 5. 建议的差异化 Narrative（3 个备选角度）

### Angle A: "From Heuristic to Principled"（推荐——最直接）
> Drayson et al. demonstrated that detect-and-reweight with w=(1-q)^b prevents model collapse, but left b as a model-specific hyperparameter requiring validation-set tuning. We derive a principled, batch-adaptive b* from convergence-theory-inspired α_eff(b) with ESS constraints, eliminating the need for grid search while matching or exceeding the best heuristic choice.

**优势**: 直接承认 Drayson 的贡献，将我们定位为在同一框架内的 principled extension。
**风险**: Reviewer 可能认为 "just optimizing a hyperparameter" = incremental。

### Angle B: "Unknown Proportion Setting"（差异化最强）
> Prior work on contamination-aware training requires labeled validation sets for b selection (Drayson et al.) or assumes known contamination fractions (Golden Ratio). We address the realistic web scenario where neither a clean validation set nor known proportions are available, deriving adaptive weights solely from batch-level detector statistics.

**优势**: 问题设置本身就与 Drayson 不同（他们知道混合比例），更贴近真实应用。
**风险**: 需要在实验中明确展示 "unknown proportion" 设置的价值。

### Angle C: "Soft-to-Hard Continuum Framework"（概念贡献最大）
> We unify detect-and-remove, detect-and-reweight, and uniform training as points on a soft-to-hard continuum parameterized by b, where b* is the detector-quality-driven optimal operating point. This reframes the "reweight vs. remove" debate as a continuous optimization problem, with Drayson et al.'s fixed-b approach as a special case.

**优势**: 提升概念层次，从 "优化一个超参数" 变为 "统一框架"。
**风险**: 需要 ablation 支撑（不同 b 值的连续谱效果图）。

### 建议策略
**主打 Angle A + B 组合**，Angle C 作为 Method section 的框架呈现。具体叙事：
- Abstract/Intro: 强调 Angle B（unknown proportion is the realistic setting）
- Method: 用 Angle C 的框架呈现算法
- Experiments: 用 Angle A 的对比展示结果（adaptive vs grid-search）
- Related Work: 明确 credit Drayson，指出他们是 closest work

---

## 6. 引用格式建议

```bibtex
@inproceedings{drayson2025machine,
  title={Machine-generated text detection prevents language model collapse},
  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
  booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
  year={2025}
}
```

---

## Sources
- [Drayson et al. (arXiv)](https://arxiv.org/abs/2502.15654)
- [Drayson et al. (HTML)](https://arxiv.org/html/2502.15654)
- [GitHub: model_collapse](https://github.com/GeorgeDrayson/model_collapse)
- [DoReMi (NeurIPS 2023)](https://arxiv.org/abs/2305.10429)
- [DSIR (NeurIPS 2023)](https://arxiv.org/abs/2302.03169)
- [IR-DRO / "Take the Bull by the Horns"](https://arxiv.org/abs/2402.14270)
- [Dynamic Loss-Based Reweighting (ICLR 2025)](https://arxiv.org/html/2502.06733v1)
- [GREATS (NeurIPS 2024)](https://openreview.net/forum?id=232VcN8tSx)
- [DCR (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/)
- [How Much Can We Forget (ICML 2025)](https://arxiv.org/abs/2410.03249)
- [Strong Model Collapse (ICLR 2025)](https://openreview.net/forum?id=et5l9qPUhm)
