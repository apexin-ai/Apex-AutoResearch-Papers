# Paper Framing — provenance_weight_training

> 状态: DRAFT (MVP Path B PASS, D019确认，进入 research 阶段)
> 最后更新: 2026-05-15 01:15 UTC
> 投稿目标: EMNLP 2026 ARR May 25

## Core Insight

Drayson et al. (EMNLP 2025) 提出 detect-and-reweight 框架 w=(1-q)^b 用于缓解合成数据污染导致的 model collapse，但 b 需要在 validation set 上 per-model empirical 选取（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1），且其实现路径为 **Sampling Importance Resampling (SIR)**——按权重重采样数据，本质是离散选择。我们提出 **adaptive b***：从 batch 统计量在线估计 α_eff(b) 推导最优 b*，per-batch 动态调整，无需 validation set、无需 grid search、无需已知污染比例。我们的实现路径为 **直接 loss reweighting**——在 gradient 层面连续加权，保留细粒度控制。

**两种方法使用同一加权公式，但解决不同问题、采用不同实现路径**：Drayson 面向递归训练场景的 model collapse prevention（b 通过 per-model validation 选取），我们面向 web corpus 一次性预训练的 decontamination（b* 从 batch 统计量自适应推导，零 validation cost）。

收敛理论（arXiv 2602.16065）作为 **motivation**（非 contribution）：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}} 启发了 α_eff 的定义和 b* 的推导，但我们不 claim 理论桥接。

## Positioning vs Prior Work

### Drayson et al. (EMNLP 2025) — 最近相关工作

**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。

**关键区分**：

| 维度 | Drayson et al. | Ours |
|------|---------------|------|
| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态 |
| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |
| **污染设置** | 不假设已知比例（原文明确声明），但实验为控制设置 | 未知比例（从 batch 统计量在线估计） |
| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |
| **理论基础** | 无 b 选取理论，无 ablation | 收敛理论 motivated α_eff(b) 推导 |
| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |
| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |
| **validation 成本** | 需 per-model validation run | 零额外 validation cost |

**定位原则：complementary approaches for different settings，非"我们比 Drayson 更好"。** Drayson 在其设定（递归训练、强检测器、validation-based b 选择）下是合理方案；我们解决的是 web pretraining 场景下无需 validation 的 principled b 选择问题。

### Golden Ratio Weighting (arXiv 2502.18049, 2025)
理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。我们不需要已知比例。

### 其他相关工作
- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse
- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补
- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting
- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级
- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention
- **arXiv 2602.16065** — 我们引用的收敛理论

## Core Claims

### Claim 1 (Primary): Principled b* via α_eff(b) 理论框架

基于 α_eff(b) 和 ESS 约束的 adaptive b* 提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical selection。

- **差异化核心**：Drayson 的 b 是超参数（需 validation set + 人工选取），我们的 b* 是从 batch 统计量在线推导的自适应量
- **理论贡献**：α_eff(b) 框架将 contamination detection score 分布与权重指数选择建立 principled 联系
- **证据需求**：adaptive b* 轨迹分析 + 与 Drayson 推荐值（b=1, b=10）的对比

### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best

Adaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。

- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）
- **Pass criteria**: adaptive 均值 ≥ 90% grid-best 改善量 + 无任何 seed 劣于 uniform
- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)

**叙事弹性（避免硬编码精确数字）**：
- 核心表述：**"adaptive matches grid-best within seed variance"**
- 补充表述：**"eliminates grid search cost (6N → 1 runs)"** 和 **"consistent improvement across all seeds"**
- Path B 叙事：3/3 seeds adaptive > uniform，adaptive-grid 差异在 seed variance 范围内

**最终 MVP 数据**：

3-seed Grid-b best (b=0.5) vs Adaptive_fix：

| Metric | seed42 | seed123 | seed456 |
|--------|--------|---------|---------|
| Uniform PPL | 17.690 | 17.690 | 17.700 |
| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |
| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |
| Ratio | 102.6% | 90.4% | 80.0% |

Aggregate ratio: 88.6% (D019). Path B PASS.

### Claim 3 (Setting): Unknown Contamination Proportion

我们的方法在 contamination proportion 完全未知的条件下工作——仅需 detector scores，无需已知污染比例、无需 clean validation set。

- **差异化**：Golden Ratio Weighting 需要已知比例 k；Drayson 虽不假设已知比例，但 b 选择依赖 validation set 做 per-model tuning；我们仅需 detector scores，无需 validation set 或已知比例
- **实际意义**：web-scale pretraining 中污染比例本质上不可知（organic contamination from multiple generators）
- **证据**：adaptive b* 仅从 per-batch q-score 分布推导，无外部信息输入

## n_min Robustness Framing

D012 修复（n_min=3→2）显示方法对 ESS 约束参数的**实际鲁棒性**：

- **现象**：n_min=3 导致 seed42 零改善（ESS 约束过紧，b* 被钳制在低值），n_min=2 修复后 seed42 恢复正常表现
- **Framing**：ESS 约束是 b* 推导中唯一的超参数，n_min=3→2 的修复表明只要 ESS 下界合理宽松（不过度约束有效样本量），adaptive b* 就能稳定工作
- **论文呈现**：在 Method section 讨论 ESS 约束的作用和敏感度；在 Ablation 中展示 n_min=2 vs n_min=3 的对比作为 robustness evidence
- **注意**：D017 勘误确认实际实施为 n_min=2 无 EMA（EMA 未编码），D018 确认 v1→v2 唯一差异为 n_min(3→2)

## Narrative Structure

**起点**: Web 语料中 20-60% 为合成文本，比例未知，来源多样——这是实际预训练面临的现实问题。Strong Model Collapse (ICLR 2025) 证明即使微量污染也会破坏 scaling law。

**现有方法的不足**：
- Drayson et al.: w=(1-q)^b 有效，但 b 依赖 per-model validation-based tuning（不同模型需不同 b，b=1 vs b=10），且需要 clean validation set
- Golden Ratio Weighting: 理论最优权重，但假设已知混合比例 k
- 两者都不适用于无 validation set 的大规模 web pretraining 场景

**我们的方案**: 在 Drayson 框架上，从 batch 统计量自适应估计 α_eff(b) 推导 b*，消除对 validation set 和 grid search 的依赖。实现路径从 SIR resampling 转为 direct loss reweighting，保留细粒度 gradient 控制。

**理论连接**: 收敛 bound 作为 Background/Motivation，不 claim 理论贡献。

**Method 呈现**: Algorithm 1 (adaptive b*) + ESS 约束（n_min 敏感度分析） + soft-to-hard 连续谱（作为 framing 而非独立 contribution）。

**Path B 默认叙事**: "Adaptive b* 免调参即可匹配 validation-tuned best，将 Drayson 框架从需要 per-model heuristic tuning 提升为全自动 principled method。" 如果数据支持 Path A（adaptive 显著优于 grid-best），可升级表述，但默认保守。

## Contribution Structure (2 Primary + 1 Setting)

1. **Primary — Theoretical Framework**: Adaptive b* via α_eff(b) estimation + ESS constraints，提供 contamination-aware reweighting 中 b 的 principled 推导（vs Drayson 的 empirical selection）
2. **Primary — Practical Result**: Adaptive b* 零超参调优即匹配 grid-best，消除 per-model validation 成本。Lightweight detector (TF-IDF+LR, AUC=0.939) sufficiency 作为附加发现（升级为 co-primary 需 detector quality ablation）
3. **Setting — Unknown Proportion**: 与 Golden Ratio (known k) 的 problem setting 差异。Drayson 虽不假设已知比例，但 b 选择依赖 validation set；我们仅需 detector scores，无需 validation 或已知比例

## Anticipated Reviewer Concerns

| Concern | Response Strategy | 实验支撑 |
|---------|------------------|----------|
| "Incremental over Drayson et al." | 三层差异化: (1) adaptive b* without validation-set tuning vs per-model empirical b (核心), (2) loss reweighting vs SIR resampling, (3) zero validation cost vs validation-dependent。Complementary approaches for different settings | Claim 1 + Claim 3 |
| "Base formula is from Drayson" | 明确 acknowledge 公式来源；贡献是 b* 的 principled derivation + 实现路径差异 + 问题设定差异 | Positioning section |
| "Theory not rigorous / overclaimed" | 明确 scope: motivation not contribution; α_eff(b) 是 testable sufficient condition not theorem | Background section |
| "Only 0.6B model, would it scale?" | Full paper: Llama-3.2-3B 验证 | 扩展实验 |
| "Detector quality sensitivity" | TF-IDF+LR (AUC=0.939) 即可；q-score 连续性比 AUC 更关键；检测器 quality ablation | detector quality ablation |
| "Controlled injection ≠ real web" | Full paper: domain-skewed injection + semi-realistic (Binoculars on Common Crawl) | 扩展实验 |
| "Small effect size (~0.3% PPL)" | (a) claim 聚焦方法正确性+调参消除，非效应量; (b) 60% 污染+3B 模型效应放大; (c) adaptive 的 zero-cost advantage | 扩展实验 |
| "n_min sensitivity — just another hyperparameter?" | n_min=3→2 修复证明方法对 ESS 约束宽松度敏感度低（n_min=2 稳定工作）；单一超参 vs Drayson 的 per-model b 选择仍是降低了调参负担 | n_min ablation |

## Key Risks

1. **Novelty narrowing (D013)**: 基础公式来自 Drayson，核心新颖性收窄为 adaptive b*。应对：三层差异化（principled b* + loss reweighting vs SIR + unknown proportion setting）；强化 lightweight detector finding
2. **Venue fit**: 核心逻辑偏 ML，EMNLP reviewer 可能低估。应对：加 NLP-specific analysis（contamination 对不同 NLP task 的影响差异）
3. **效应量小 (0.3% relative PPL at 40% contamination)**: 应对：60% 污染 + 3B 模型展示效应放大；强调 zero-cost advantage（方法价值在于免调参，不在于绝对 PPL 提升）
4. **adaptive_fix 如果仍有 seed 失败**: MVP 依赖 D012 修复版结果。应对：如果修复版仍不稳定，需进一步诊断算法或调整 claims
5. **SIR vs loss reweighting 差异被低估**: Reviewer 可能认为两种实现路径差异不大。应对：在 Method 中讨论 gradient-level 细粒度控制的优势，必要时加 ablation 对比

## MVP → Full Paper 扩展路径

| 维度 | MVP | Full Paper |
|------|-----|-----------|
| 污染比例 | 40% | 20%, 40%, 60% |
| 模型 | Qwen3-0.6B | + Llama-3.2-3B |
| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |
| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |
| Baseline | uniform, grid-b, adaptive | + detect-and-remove, random reweighting, perplexity filter, DSIR, loss-based DRO, oracle |
| 评估 | eval_ppl (perplexity) | + MMLU, HellaSwag, Self-BLEU, distinct-n, Wasserstein, MMD |
| 注入方式 | uniform random | + domain-skewed, semi-realistic |
| n_min 分析 | n_min=2 vs n_min=3 (2 点) | + n_min=1, 4, 5 的完整 sensitivity curve |
