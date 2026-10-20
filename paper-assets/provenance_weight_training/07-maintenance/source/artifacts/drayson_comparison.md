# Drayson et al. (EMNLP 2025) 深度对比分析

> 日期: 2026-05-14 | 关联: D013 新颖性风险

---

## 1. Drayson 方法总结（200 字）

Drayson et al. 提出 **detect-and-reweight** 防止语言模型在递归训练中坍塌。核心公式：**wⱼ = (1−q(xⱼ))^b / Σₗ(1−q(xₗ))^b**，其中 q(x) 为 ModernBERT 检测器输出的 machine-generated 概率。通过 Sampling Importance Resampling (SIR) 按权重重采样训练数据，上采样可能为人类撰写的内容。检测器在 MAGE 数据集上 fine-tune，in-domain AUC=0.986，OOD AUC=0.943。b 值通过在 WikiText-2 验证集上 1 代递归训练后评估选取（GPT-2/SmolLM 135M/360M 用 b=10，SmolLM 1.7B 用 b=1）。实验在 4 个模型（GPT-2 124M, SmolLM 135M/360M/1.7B）上进行 10 代递归训练，覆盖 6 种解码策略。结果：PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。**b 在整个训练过程中固定，无自适应机制。**

---

## 2. 我们 vs Drayson 对比表

| 维度 | Drayson et al. (EMNLP 2025) | 我们 (Adaptive b*) |
|------|---------------------------|-------------------|
| **b 选择方法** | 验证集 empirical 选取，per-model 固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态调整 |
| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，证明轻量检测器即可 |
| **污染设置** | 不假设已知比例（原文明确声明），但实验为控制设置 | 未知比例（从 batch 统计量在线估计） |
| **理论基础** | 无（SIR 启发式，无 b 选取理论） | 收敛理论 motivated α_eff(b) 推导 + 连续谱统一框架 |
| **计算开销** | 需 per-model validation run（等价于 grid search） | 零额外 validation cost，从 batch 统计量直接计算 |
| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练中的未知污染 |
| **数据规模** | WikiText-2 (36K docs, ~2M tokens) | FineWeb subset (132M+ tokens) |
| **生成器** | 单一生成器 per experiment | 多生成器 cross-contamination |
| **动态性** | b 固定（训练全程不变） | b* per-batch 自适应 |
| **框架贡献** | 提出 detect-and-reweight 方法 | 统一 soft-to-hard 连续谱 (b=0 uniform → b→∞ hard filter) |

---

## 3. 三个关键差异化论点（Related Work 可用）

### 论点 1: From Heuristic to Principled（最直接）

> Drayson et al. (2025) demonstrate that detect-and-reweight with w=(1−q)^b effectively prevents model collapse, but their bias term b is selected empirically per model via validation-set evaluation after one generation of recursive training. This requires a labeled validation set and separate tuning runs for each model architecture. We derive a principled, batch-adaptive b* from convergence-theory-inspired α_eff(b) with ESS constraints, eliminating validation-based tuning while matching or exceeding their best heuristic choices.

### 论点 2: Unknown Contamination Proportion（差异化最强）

> Prior detect-and-reweight approaches (Drayson et al., 2025) operate under controlled recursive training where contamination fractions are known by experimental design. In contrast, we address the realistic web-corpus scenario where neither the contamination proportion nor a clean validation set is available. Our adaptive b* is derived solely from batch-level detector statistics, making it applicable to large-scale pretraining where contamination is organic and unquantified.

### 论点 3: Lightweight Detector Sufficiency（实用性角度）

> Drayson et al. rely on ModernBERT (150M parameters, AUC=0.986), a state-of-the-art neural detector requiring GPU inference over the entire training corpus. We demonstrate that a simple TF-IDF + logistic regression detector (AUC=0.939) suffices when paired with our adaptive b*, reducing detector compute by orders of magnitude. This suggests the reweighting mechanism's effectiveness depends more on principled exponent selection than on detector precision.

---

## 4. Golden Ratio Weighting 总结（100 字）

He & Xu (arXiv 2502.18049, 2025) 理论证明在递归训练中混合真实与合成数据时，最优权重 **w\* = (√(k²+4k)−k)/2**（k=真实/合成样本比）。当 k=1 时 w\*=1/φ≈0.618（黄金比例倒数）。在高斯分布估计、GLM、非参数估计三种设置下验证。**局限**：纯理论工作，假设已知污染比例，未涉及检测器或 LLM 实验，不处理 unknown/online 设置。

---

## 5. 其他相关论文一句话总结

| 论文 | Venue | 一句话 |
|------|-------|--------|
| **Strong Model Collapse** (Dohmatob & Feng et al.) | ICLR 2025 (Spotlight), arXiv:2410.04840 | 理论证明即使 0.1% 合成数据污染也会导致 scaling law 失效，更大模型反而放大坍塌 |
| **Dynamic Loss-Based Sample Reweighting** (Sow et al., IBM/OSU/TUM) | ICLR 2025, arXiv:2502.06733 | 基于 per-sample loss 的在线重加权（LinUpper/Quadratic/Extremes + softmax temperature），不使用检测器，纯 loss signal 驱动，7B 模型验证有效 |
| **DoReMi** (Xie et al.) | NeurIPS 2023 | 域级别权重优化（Group DRO + 小模型代理），不处理 instance-level 污染 |
| **DSIR** (Xie et al.) | NeurIPS 2023 | N-gram 特征重要性采样选择数据子集匹配目标分布 |
| **Escaping Model Collapse via Synthetic Data Verification** | arXiv:2510.16657 | 提出验证机制筛选合成数据质量，与我们的 detection-based 方法互补 |

---

## 6. 搜索来源

- Drayson et al.: [arXiv:2502.15654](https://arxiv.org/abs/2502.15654) | [HTML](https://arxiv.org/html/2502.15654) | [GitHub](https://github.com/GeorgeDrayson/model_collapse)
- Golden Ratio Weighting: [arXiv:2502.18049](https://arxiv.org/abs/2502.18049)
- Strong Model Collapse: [arXiv:2410.04840](https://arxiv.org/abs/2410.04840) | [ICLR 2025](https://openreview.net/forum?id=et5l9qPUhm)
- Dynamic Loss-Based Reweighting: [arXiv:2502.06733](https://arxiv.org/abs/2502.06733) | [GitHub](https://github.com/sowmaster/Sample-Level-Loss-Reweighting-ICLR-2025)
