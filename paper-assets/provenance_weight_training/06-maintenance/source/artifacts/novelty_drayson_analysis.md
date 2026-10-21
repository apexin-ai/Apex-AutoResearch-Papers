# Drayson et al. (EMNLP 2025) 差异化深度分析

> 分析日期: 2026-05-14
> 关联决策: D013

---

## 1. Drayson et al. 方法摘要

### 论文信息
| 字段 | 内容 |
|------|------|
| **标题** | Machine-generated text detection prevents language model collapse |
| **作者** | George Drayson, Emine Yilmaz, Vasileios Lampos |
| **单位** | University College London (UCL) |
| **Venue** | EMNLP 2025 Main Conference |
| **arXiv** | 2502.15654 |
| **代码** | https://github.com/GeorgeDrayson/model_collapse |

### 核心方法
- **公式**: wⱼ = (1−q(xⱼ))^b / Σₗ(1−q(xₗ))^b
  - q(x): ModernBERT 检测器输出的 machine-generated 概率
  - b ≥ 1: bias term，控制权重倾斜程度
- **采样**: Sampling Importance Resampling (SIR)，k=1.5 倍上采样 + rmax 上限防止单样本过度重复
- **检测器**: ModernBERT fine-tuned on MAGE dataset (AUC=0.986 in-domain, 0.943 OOD)

### b 的选择方式
- **验证集 empirical 选取，非 grid search，非 adaptive，无理论推导**
- 做法: "We select values for rmax and b by evaluating each model on the Wikitext-2 validation set after 1 generation of recursive training"
- 实际值: GPT-2/SmolLM-135M/360M → b=10; SmolLM-1.7B → b=1
- **无 b 敏感度分析或 ablation**

### 实验设置
- 数据: WikiText-2 (36,718 documents)
- 模型: GPT-2 124M, SmolLM2 135M/360M/1.7B
- 递归训练: 10 generations
- 解码策略: 6 种 (greedy, beam, pure sampling, temperature, top-k, nucleus)
- 评估: Perplexity, diversity (distinct-n), MAUVE

### 结果
- Perplexity 改善: −0.85% to −25.65%
- Diversity 增益: +3.44% to +14.62%
- MAUVE 提升: +8.46% to +20.92%

---

## 2. 差异化对比（核心表）

| 维度 | Drayson et al. (EMNLP 2025) | Ours (provenance_weight_training) |
|------|---------------------------|----------------------------------|
| **b 选择** | 验证集 empirical 选取，训练中固定 | Adaptive b*: per-batch 自适应推导 |
| **b 选择原理** | 无理论依据，启发式 | 基于 α_eff(b) 和 ESS 约束的 principled 推导 |
| **需要 validation set?** | 是（clean WikiText-2 validation） | 否（仅从 batch 统计量推导） |
| **污染比例假设** | 不假设已知（原文明确声明），但实验为控制设置 | 未知（从 detector score 分布估计） |
| **应用场景** | Model collapse prevention (recursive training) | Web corpus decontamination (unknown synthetic fraction) |
| **数据规模** | WikiText-2 (36K docs, ~4M tokens) | FineWeb subset (132M+ tokens) |
| **生成器设置** | 单一生成器 per experiment | 多生成器 cross-contamination |
| **检测器要求** | 强检测器 ModernBERT (AUC=0.986) | 轻量 TF-IDF+LR (AUC=0.939) 即可 |
| **动态性** | b 固定不变 | b* per-batch 动态调整 |
| **理论支撑** | 纯 empirical | 收敛理论 motivated α_eff(b) |
| **概念框架** | detect-and-reweight 作为一种方法 | soft-to-hard 连续谱统一框架 (b=0 → b→∞) |

---

## 3. Drayson et al. 的局限性（可在论文中引用）

1. **b 选择需要 per-model validation**：每换一个模型都要重新在验证集上搜 b，SmolLM-1.7B 的 b=1 与其他模型的 b=10 差异巨大，无解释
2. **已知污染比例**：实验中精确控制 synthetic/real 混合比，不反映真实 web scraping 场景
3. **单生成器**：每个实验只有一个 LLM 生成 synthetic data，未考虑多源交叉污染
4. **小规模数据**：WikiText-2 仅 36K documents，无法验证方法在 web-scale 的效果
5. **无 b 敏感度分析**：不知道 b 选错（如 b=5 vs b=10）的代价有多大
6. **Resampling 而非 soft weighting**：SIR 本质是离散选择，失去 gradient-level 的细粒度控制

---

## 4. 其他相关工作

| 方法 | Venue | Adaptive? | Weight 选择方式 | 数据规模 | 与我们的关系 |
|------|-------|-----------|----------------|---------|------------|
| **Golden Ratio Weighting** (He & Xu, 2025) | arXiv 2502.18049 | ❌ | Closed-form w*=1/φ (假设已知比例) | Theoretical + simulation | 理论互补：他们 derive 最优混合比，我们 derive 最优权重指数 |
| **Escaping Collapse** (Amin et al., 2025) | NeurIPS 2025 | ✅ | Boosting-inspired iterative reweighting | Curated (math/coding) | 思路类似但机制不同：他们用 boosting 聚焦难样本，我们用 detector score 降权污染 |
| **Dynamic Loss Reweighting** (Sow et al., 2025) | ICLR 2025 | ✅ | Loss-based + temperature annealing | SlimPajama/FineWeb, up to 7B | 互补：他们按 loss 加权（不区分污染），我们按 provenance 加权 |
| **DoReMi** (Xie et al., 2023) | NeurIPS 2023 | ✅ (domain) | Group DRO 小模型代理优化 | The Pile (800GB) | 域级 vs 实例级：他们优化域权重，我们优化实例权重 |
| **DSIR** (Xie et al., 2023) | NeurIPS 2023 | ❌ | Importance weights via n-gram features | The Pile (100M docs) | 数据选择 vs 权重调整：不同目标 |
| **IR-DRO** (Chen et al., 2024) | arXiv 2024 | 半自适应 | KL-regularized softmax, r=10 fixed | C4, up to 7B | 中等 loss 样本重加权，不使用 provenance 信号 |
| **TapWeight** (2025) | PMC 2025 | ✅ | Bilevel optimization for task-adaptive objectives | Task-adaptive pretraining | 任务导向 vs 数据质量导向 |
| **GREATS** (Wang et al., 2024) | NeurIPS 2024 | ✅ | Taylor expansion + greedy batch selection | LLM pretraining scale | 在线选择 vs 在线加权 |
| **Strong Model Collapse** (Dohmatob et al., 2025) | ICLR 2025 | N/A (theory) | N/A | Theoretical | 理论动机：证明微量污染即导致坍塌 |
| **DCR** (Xu et al., 2025) | EMNLP 2025 | N/A (eval) | Fuzzy inference system | 9 LLMs, 0.5B-72B | 评估阶段校正，非训练阶段 |

---

## 5. 核心发现：无人做过 adaptive b* for contamination weighting

在 2024-2026 文献搜索范围内，**没有找到任何工作将 contamination detection score 的权重指数 b 进行自适应/理论推导**。现有格局：

- Drayson: 固定 b（empirical validation）
- Golden Ratio: closed-form weight（但假设已知比例，且是混合比而非权重指数）
- Dynamic Loss Reweighting: 按 loss 自适应（不使用 detector score）
- DoReMi: domain-level 自适应（非 instance-level）
- Amin et al.: boosting-inspired 迭代（不使用 contamination score）

**我们的 adaptive b* 填补了一个明确的空白**: instance-level contamination-score-based 权重中，b 的 principled 自适应选择。

---

## 6. 建议的 Related Work 定位策略

### 推荐叙事：Angle A+B 组合

**Intro/Abstract (强调问题设置差异 — Angle B)**:
> Prior work on contamination-aware training requires per-model validation-set tuning to select b (Drayson et al., 2025) or assumes known contamination fractions (Golden Ratio Weighting). We address the realistic web-scale scenario where neither clean validation sets nor known proportions are available.

**Method (统一框架 — Angle C)**:
> We formalize detect-and-reweight as a soft-to-hard continuum parameterized by b ∈ [0,∞), unifying uniform training (b=0), soft reweighting (finite b), and hard filtering (b→∞). Drayson et al.'s fixed-b approach and standard deduplication are special cases.

**Experiments (直接对比 — Angle A)**:
> Our adaptive b* matches or exceeds the performance of oracle-tuned fixed b, eliminating the per-model validation cost of prior approaches.

**Related Work (明确 credit + differentiate)**:
> Closest to our work, Drayson et al. (2025) demonstrated that detect-and-reweight with w=(1-q)^b prevents model collapse in recursive training. However, their b is a model-specific hyperparameter requiring validation-set tuning (b=10 for ≤360M models, b=1 for 1.7B), with no theoretical guidance for selection. We derive b* from batch-level detector statistics via α_eff(b) with ESS constraints, making the approach fully automatic and applicable without clean validation data.

### Related Work 段落中应覆盖的工作分组

1. **Contamination-aware training**: Drayson et al. (2025) — closest work, same formula
2. **Optimal data mixing theory**: Golden Ratio (He & Xu, 2025), Strong Collapse (Dohmatob et al., 2025)
3. **Sample reweighting for pretraining**: Dynamic Loss (Sow et al., 2025), IR-DRO (Chen et al., 2024)
4. **Domain-level data optimization**: DoReMi (Xie et al., 2023), DSIR (Xie et al., 2023)
5. **Boosting-inspired curation**: Amin et al. (NeurIPS 2025)
6. **Contamination detection**: DCR (Xu et al., 2025), Min-K% Prob (Shi et al., 2024)

---

## 7. 对 Paper Framing 的影响

### 风险评估
- **风险**: Reviewer 可能认为 "同一公式，只是优化了超参数" = incremental
- **缓解**: 强调问题设置根本不同（unknown proportion + no validation set），adaptive b* 不是 "tuning a hyperparameter" 而是 "deriving the optimal operating point from theory"

### Framing 调整建议
1. **不要把 formula 当作我们的贡献** — 明确 credit Drayson 的公式，我们的贡献是 b* 的 principled derivation + unknown proportion setting
2. **提升概念层次** — soft-to-hard continuum 框架比 "adaptive b" 更有概念贡献
3. **实验设计** — 必须包含:
   - adaptive b* vs fixed b (at Drayson's values: 1, 10) 的对比
   - unknown proportion 设置下 adaptive b* 的鲁棒性
   - 比 Drayson 大得多的数据规模 (132M+ tokens vs 4M tokens)
4. **Lightweight detector** — 展示 TF-IDF+LR 足够好，降低了方法的实用门槛

---

## 8. 参考文献

- [Drayson et al. (arXiv:2502.15654)](https://arxiv.org/abs/2502.15654) — Machine-generated text detection prevents language model collapse, EMNLP 2025
- [Golden Ratio Weighting (arXiv:2502.18049)](https://arxiv.org/abs/2502.18049) — Golden Ratio Weighting Prevents Model Collapse
- [Escaping Collapse (NeurIPS 2025)](https://neurips.cc/virtual/2025/loc/san-diego/poster/115205) — Amin et al., boosting-inspired curation
- [Dynamic Loss Reweighting (ICLR 2025)](https://arxiv.org/abs/2502.06733) — Sow et al., instance-level loss-based reweighting
- [DoReMi (NeurIPS 2023)](https://arxiv.org/abs/2305.10429) — Xie et al., domain-level DRO reweighting
- [DSIR (NeurIPS 2023)](https://arxiv.org/abs/2302.03169) — Xie et al., importance-weighted data selection
- [IR-DRO (arXiv 2024)](https://arxiv.org/abs/2402.14270) — Chen et al., instance reweighting via DRO
- [GREATS (NeurIPS 2024)](https://openreview.net/forum?id=232VcN8tSx) — Wang et al., greedy online batch selection
- [DCR (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/) — Xu et al., contamination quantification for evaluation
- [Strong Model Collapse (ICLR 2025)](https://openreview.net/forum?id=et5l9qPUhm) — Dohmatob et al., theoretical collapse analysis
