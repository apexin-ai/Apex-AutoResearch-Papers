# CORAL Ordinal Regression 文献调研

> 调研日期：2026-05-19
> 目的：为 recursive_gen_depth_est 项目升级 CORAL ordinal regression 分类器提供文献支撑

---

## 1. CORAL 原始论文

**Wenzhi Cao, Vahid Mirjalili, Sebastian Raschka.** "Rank consistent ordinal regression for neural networks with application to age estimation." *Pattern Recognition Letters*, 140:325-331, 2020.
- arXiv: 1901.07884
- DOI: 10.1016/j.patrec.2020.11.008
- **Relevance**: CORAL 将 ordinal target 转化为 K-1 个二元分类子任务，通过 weight-sharing 约束保证 rank consistency（即预测的累积概率单调递减）。方法与网络架构无关，可直接嵌入任意分类器。我们项目将 d0-d3 generation depth 建模为 ordinal label，CORAL 是首选框架。PyTorch 实现：`coral-pytorch` (MIT license)。

---

## 2. Ordinal Regression 在 NLP/文本分类中的应用

### 2.1 Ordinal vs Nominal 文本分类对比

**Siva Rajesh Kasa, Aniket Goel, Karan Gupta, Sumegh Roychowdhury, Anish Bhanushali, Nikhil Pattisapu, Prasanna Srinivasa Murthy.** "Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques." *Findings of ACL 2024*.
- arXiv: 2405.11775
- **Relevance**: 直接比较 explicit ordinal loss (如 CORAL) 与 implicit ordinal semantics (PLM label embedding) 在文本分类中的效果。涵盖 sentiment analysis、rating prediction 等任务。发现 ordinal 方法在 ordinal metrics (MAE) 上显著优于 nominal classification，但在 nominal metrics (accuracy) 上存在 trade-off。提出 hybrid loss 平衡两者。**强烈推荐引用**：直接支撑我们选择 ordinal regression 而非 nominal classification 的决策。

### 2.2 Ordinal 建模用于 Essay Scoring

**Han Zhang, Jiamin Su, Li Liu.** "Decision-Level Ordinal Modeling for Multimodal Essay Scoring with Large Language Models." arXiv: 2603.14891, 2026.
- **Relevance**: 提出 DLOM，将 LLM-based essay scoring 建模为 ordinal decision（非标准文本生成），通过 distance-aware regularization 捕获评分等级间的有序关系。与我们将 generation depth 视为 ordinal variable 的思路一致。展示了 ordinal 建模在文本质量评估任务上的有效性。

### 2.3 关于 AI-Generated Text Detection

搜索结果表明：**目前没有论文将 ordinal regression 用于 AI-generated text detection**。该领域主流方法均为 binary classification (human vs AI) 或 multi-class nominal classification (GPT-4 vs Claude vs human)。我们将 ordinal regression 用于 recursive generation depth estimation 是一个**新颖的 framing**，可作为 novelty claim。

---

## 3. 竞品方法对比

### 3.1 CORN (Conditional Ordinal Regression for Neural Networks)

**Xintong Shi, Wenzhi Cao, Sebastian Raschka.** "Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities." *Pattern Analysis and Applications*, 2023.
- arXiv: 2111.08851
- **方法**: 通过 conditional probability chain rule 实现 rank consistency，无需 CORAL 的 weight-sharing 约束，表达能力更强。
- **vs CORAL**: 实验显示 CORN 在部分数据集上优于 CORAL，但计算成本更高（K-1 个独立分类器 vs 共享权重）。对我们 K=4 的小规模 ordinal 问题，CORAL 的 weight-sharing 不构成瓶颈，且实现更简单。
- **推荐**: 论文中作为 ablation 或 Discussion 中提及的替代方案。

### 3.2 THOR (Threshold-Based Ranking Loss)

**Tzeviya Sylvia Fuchs, Joseph Keshet.** "THOR: Threshold-Based Ranking Loss for Ordinal Regression." arXiv: 2205.04864, 2022.
- **方法**: 预定义 category boundary，学习将输入映射到 score space，用 threshold-based pairwise loss 最小化 MAE。
- **vs CORAL**: 回归式方法，不产生显式 class probability；CORAL 产生每个 rank 的概率，更适合我们需要 confidence calibration 的场景。

### 3.3 Binary Decomposition (Frank & Hall)

**Eibe Frank, Mark Hall.** "A Simple Approach to Ordinal Classification." *ECML 2001*, pp. 145-156.
- **方法**: 将 K-class ordinal 问题分解为 K-1 个二元分类任务，是 CORAL 的概念前身。
- **vs CORAL**: Frank & Hall 的方法不保证 rank consistency（各二元分类器独立训练可能产生矛盾预测），CORAL 通过 weight-sharing 解决此问题。
- **推荐**: Related Work 中作为经典基线引用。

### 3.4 Multiple Output CNN (OR-CNN)

**Zhenxing Niu, Mo Zhou, Le Wang, Xinbo Gao, Gang Hua.** "Ordinal Regression with Multiple Output CNN for Age Estimation." *CVPR 2016*, pp. 4920-4928.
- **方法**: 多输出 CNN 同时训练 K-1 个二元分类子问题，利用共享特征捕获任务间相关性。
- **vs CORAL**: OR-CNN 不保证 rank consistency，CORAL 在理论上解决了这一缺陷。

### 3.5 Proportional Odds Model (POM)

**Peter McCullagh.** "Regression Models for Ordinal Data." *JRSS Series B*, 42(2):109-142, 1980.
- **方法**: 经典统计 ordinal regression，假设 proportional odds（所有阈值共享相同回归系数）。
- **vs CORAL**: POM 是线性模型，CORAL 是其 deep learning 推广。可在 Related Work 中作为理论根基引用。

---

## 4. 综述论文

### 4.1 经典综述

**Pedro A. Gutiérrez, María Pérez-Ortiz, Javier Sánchez-Monedero, Francisco Fernandez-Navarro, César Hervás-Martínez.** "Ordinal regression methods: survey and experimental study." *IEEE TKDE*, 28(1):127-146, 2016.
- 系统分类 ordinal regression 方法，实验比较多种方法在 ordinal metrics 上的表现。经典引用。

### 4.2 最新综述

**Jinhong Wang, Jintai Chen, Jian Liu, Dongqi Tang, Danny Z. Chen, Jian Wu.** "A Survey on Ordinal Regression: Applications, Advances and Prospects." arXiv: 2503.00952, 2025.
- 覆盖最新 deep ordinal regression 方法，分为 continuous space discretization、distribution ordering learning、ambiguous instance delving 三类。主要聚焦 CV，NLP 覆盖较少。

---

## 5. 推荐引用策略

### Related Work 必引（4 篇）
1. **Cao et al. 2020 (CORAL)** — 我们的核心方法，必须引用并详细说明
2. **Kasa et al. 2024 (ACL Findings)** — 支撑 ordinal vs nominal 在文本分类中的优势论证
3. **Frank & Hall 2001** — ordinal binary decomposition 经典方法，positioning CORAL 的改进
4. **Gutiérrez et al. 2016** — ordinal regression 综述，展示调研深度

### Method Section 推荐引（2 篇）
5. **Shi et al. 2023 (CORN)** — 作为 CORAL 的替代方案讨论选择理由
6. **McCullagh 1980 (POM)** — CORAL 的统计学理论根基

### Discussion/Novelty Claim 可引（2 篇）
7. **Zhang et al. 2026 (DLOM)** — ordinal modeling 用于文本质量评估的最新工作，支撑我们的 framing
8. **Niu et al. 2016 (OR-CNN)** — CORAL 解决的 rank inconsistency 问题出处

### 工具引用
9. **coral-pytorch** — `pip install coral-pytorch`，MIT license，Raschka 团队维护，含 text data (TripAdvisor) tutorial
