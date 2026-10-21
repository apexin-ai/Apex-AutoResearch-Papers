# Covariate Shift Literature Survey

## 研究背景

Cross-strategy LOO 实验发现：temperature sampling (τ=0.9) 导致递归生成文本的统计特征（尤其 p90_ppl）系统性低约一个深度级别——temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化后跨策略分类器 AUC 大幅恢复（GPT-2 XL d1v2: 0.13→0.68, OLMo: 0.25→0.83），证实这是分布偏移而非信号消失。

---

## 直接相关 (Direct)

### D1. Marchi et al. — "Heat Death of Generative Models in Closed-Loop Learning"
- **作者**: Matteo Marchi, Stefano Soatto, Pratik Chaudhari, Paulo Tabuada
- **Venue**: ICASSP 2025 (arXiv: 2404.02325)
- **关联程度**: **Direct**
- **核心发现**:
  - 用动力系统工具证明：**任何非平凡温度 (T≠1) 都会导致生成分布渐近退化**
  - T<1: 产生"expanding dynamics"，放大概率差异，驱动 mode collapse（集中到少数输出）
  - T>1: 产生"contractive dynamics"，抑制概率差异，驱动向均匀分布收敛
  - T=1: 不稳定平衡，需要外部数据注入维持稳定
  - 退化是不可逆的："unless a copy of the pre-generative-models Internet is preserved, eventually no model will be trained effectively"
- **与我们发现的关联**: **最直接的理论支撑**。我们的 τ=0.9 属于 T<1 regime，Marchi 的理论预测此时概率差异被放大，加速向 mode collapse 收敛。这精确解释了为何 temp09 在每个深度的 p90_ppl 系统性更低——模型更快收敛到低困惑度的 attractor 分布。
- **可引用结论**: "Any non-trivial temperature leads the model to asymptotically degenerate. Either the generative distribution collapses to a small set of outputs, or becomes uniform over a large set of outputs."

### D2. Dohmatob et al. — "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
- **作者**: Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, Julia Kempe
- **Venue**: ICML 2024 (arXiv: 2402.07043)
- **关联程度**: **Direct**
- **核心发现**:
  - 区分了两种不同的尾部畸变机制：
    - **Top-p/Top-k → "tail cutting"**: 在 rank k 处硬截断
    - **Temperature scaling → "tail narrowing"**: 调整幂律指数，q_i^T ∝ i^{-β/T}
  - Temperature 通过连续缩窄尾部影响分布，而非离散截断
  - Tail cutting 产生 plateau behavior（Theorem 2.1），tail narrowing 产生更缓慢但持续的衰减（Corollary 2.3）
- **与我们发现的关联**: **直接解释了 temperature 与 truncation 方法为何产生不同的统计指纹**。Temperature 的 tail narrowing 改变的是分布形状而非边界，导致特征空间中的系统性偏移而非噪声增加。这正是我们观察到的协变量偏移的数学基础。
- **可引用结论**: "Temperature scaling causes 'tail narrowing' by adjusting the power-law exponent β, producing different degradation patterns from the 'tail cutting' of top-p/top-k truncation."

### D3. Drayson et al. — "Machine-generated text detection prevents language model collapse"
- **作者**: Drayson et al.
- **Venue**: EMNLP 2025 (arXiv: 2502.15654)
- **关联程度**: **Direct**
- **核心发现**:
  - 在 GPT-2 (124M) 和 SmolLM2 (360M) 上测试了多种采样策略在 99 代递归训练中的退化轨迹
  - **Temperature sampling (τ=0.9) 产生了最重复的输出**，多样性下降约 70%
  - 退化速率排序：deterministic (greedy/beam) > temperature > pure sampling > top-k > nucleus
  - 跨策略困惑度轨迹（Gen 0→99）:
    - Temperature: 29.23→44.55 (GPT-2), 13.96→24.88 (SmolLM2)
    - Top-k: 29.31→48.36 (GPT-2), 13.96→19.86 (SmolLM2)
    - Nucleus: 中等退化
  - Temperature 的困惑度上升反而比 top-k 温和，但多样性损失更严重——说明温度让模型收敛到更窄但更"流畅"的分布
- **与我们发现的关联**: **最直接的实证支持**。我们观察到 temp09 的 p90_ppl 更低恰好对应 Drayson 发现的"温度使输出更重复但困惑度上升更温和"。Temperature 不是简单地加速退化，而是将分布推向更确定性的 attractor——低困惑度、低多样性。
- **可引用结论**: "Temperature sampling led to the most repetitive outputs after recursive training, with diversity decreasing by approximately 70%, while perplexity degradation was more moderate than deterministic methods."

### D4. Shumailov et al. — "AI models collapse when trained on recursively generated data"
- **作者**: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal
- **Venue**: Nature, 2024
- **关联程度**: **Direct**
- **核心发现**:
  - 建立了 model collapse 的实证框架：反复用模型自身输出训练下一代，性能逐代递减
  - 关键机制是 **tail erosion**: 每一代生成更少的尾部样本，下一代从更偏的分布学习
  - 困惑度在 40 代递归中单调递增
  - 实验使用标准采样 (T=1)，**未系统比较不同采样策略**
- **与我们发现的关联**: 提供了递归生成退化的基本框架。我们的工作扩展了这一框架——不仅仅是训练递归（train-on-output），而是纯推理递归（feed output back as input），且揭示了采样策略间的差异。
- **可引用结论**: "Indiscriminate use of model-generated content in training causes irreversible defects, in which tails of the original content distribution disappear."

---

## 间接相关 (Indirect)

### I1. Dohmatob et al. — "Strong Model Collapse"
- **作者**: Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe
- **Venue**: ICLR 2025 Spotlight (arXiv: 2410.04840)
- **关联程度**: Indirect
- **核心发现**: 即使训练集中合成数据比例极小（1/1000），仍会导致 model collapse。更大的模型可能放大 collapse。
- **与我们发现的关联**: 解释了为何递归生成的深度效应如此系统性——每一步的微小偏差都会累积。

### I2. Alemohammad et al. — "Self-Consuming Generative Models Go MAD"
- **作者**: Sina Alemohammad, Josue Casco-Rodriguez, et al.
- **Venue**: ICLR 2024 (arXiv: 2307.01850)
- **关联程度**: Indirect
- **核心发现**:
  - 无偏采样：modes 漂移并最终合并为一个大 cluster
  - 有偏采样：保持精度但多样性坍缩（高 precision、零 recall）
  - 没有足够新鲜真实数据，质量或多样性必然递减
- **与我们发现的关联**: Temperature τ=0.9 可视为一种轻微有偏采样（向高概率 token 偏移），符合其"biased sampling → 精度保持但多样性下降"的模式。

### I3. Holtzman et al. — "The Curious Case of Neural Text Degeneration"
- **作者**: Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, Yejin Choi
- **Venue**: ICLR 2020 (arXiv: 1904.09751)
- **关联程度**: Indirect
- **核心发现**:
  - Temperature + top-k 组合导致文本退化为重复模式
  - 关键概念："unreliable tail"——数万个低概率 token 在聚合中被过度代表
  - Nucleus sampling 动态调整候选池，优于固定温度或 top-k
- **与我们发现的关联**: 建立了 temperature 与 truncation 方法在生成质量上的根本差异。我们的 cross-strategy 实验扩展了这一认识到递归深度维度。

### I4. Finlayson et al. — "Closing the Curious Case of Neural Text Degeneration"
- **作者**: Matthew Finlayson, John Hewitt, Alexander Koller, Swabha Swayamdipta, Ashish Sabharwal
- **Venue**: ICLR 2024 (arXiv: 2310.01693)
- **关联程度**: Indirect
- **核心发现**:
  - Truncation sampling 有效消除 softmax bottleneck 导致的误差
  - 开发了精确采样方法，利用 softmax bottleneck 的已知误差源
- **与我们发现的关联**: 解释了为何 nucleus/top-k（截断方法）与 temperature（缩放方法）在递归生成中产生不同的统计指纹——它们处理 softmax bottleneck 的方式根本不同。

### I5. Gehrmann et al. — "GLTR: Statistical Detection and Visualization of Generated Text"
- **作者**: Sebastian Gehrmann, Hendrik Strobelt, Alexander Rush
- **Venue**: ACL 2019 (arXiv: 1906.04043)
- **关联程度**: Indirect
- **核心发现**:
  - 使用统计特征（top-k token fraction、log-likelihood、rank、entropy）检测生成文本
  - 生成文本倾向于在每个位置选择最可能的词，而自然写作更频繁地选择"意外"词
- **与我们发现的关联**: 我们的特征体系（perplexity percentiles 等）延续了 GLTR 的统计检测哲学。GLTR 表明不同生成策略产生不同的统计指纹，我们进一步发现这些指纹在递归深度维度上存在系统性偏移。

### I6. Cross-Domain AI Text Detection Literature (GenAI Detection Task 3, RAID dataset)
- **Venue**: EMNLP 2025 / Various
- **关联程度**: Indirect
- **核心发现**:
  - 检测器在闭域（同生成器同配置）表现好，跨域显著下降
  - RAID 数据集覆盖 11 个模型 × 4 种解码策略 × 11 种体裁
  - 不同生成配置之间的分布偏移是检测泛化的主要瓶颈
- **与我们发现的关联**: 我们的 cross-strategy LOO 实验正是在测量这种跨解码策略的分布偏移。z-score 标准化恢复 AUC 的方法提供了一种简洁的跨策略泛化方案。

---

## 背景相关 (Background)

### B1. Sugiyama et al. — "Covariate Shift Adaptation by Importance Weighted Cross Validation"
- **Venue**: JMLR, 2007
- **关联程度**: Background
- **核心**: 协变量偏移下通过重要性加权修正训练风险。理论基础 for 我们的 z-score 标准化方法——z-score 可视为一种简化的分布对齐。

### B2. Escaping Mode Collapse in LLM Generation via Geometric Regulation
- **Venue**: arXiv 2025 (2605.00435)
- **关联程度**: Background
- **核心**: Mode collapse 在自回归文本生成中表现为"从显式循环到逐渐失去多样性和轨迹过早收敛"。概率重整或解码启发式无法可靠解决。

---

## 新颖性评估

**我们的发现: "Accelerated convergence under temperature sampling in recursive generation depth estimation"**

**新颖性等级: partially-known**

已知部分：
1. Temperature ≠ 1 导致递归生成退化（Marchi et al., 2024）— 理论层面已证明
2. Temperature 通过 tail narrowing 而非 tail cutting 改变分布（Dohmatob et al., 2024）— 机制已阐明
3. Temperature τ=0.9 在递归训练中产生最重复输出（Drayson et al., 2025）— 经验已观察

**我们的新颖贡献**:
1. **深度偏移量化**: 首次精确量化了 temperature 的加速效应——temp09 depth N ≈ nucleus/topk depth N+1，即"一个深度级别的偏移"。现有文献仅定性描述退化加速，未给出跨策略的深度等价关系。
2. **协变量偏移框架**: 将不同采样策略之间的差异明确建模为协变量偏移问题（而非简单的"不同策略不同效果"），这一框架化在递归生成/深度估计文献中是新的。
3. **z-score 修正方法**: 证明简单的 z-score 标准化即可大幅恢复跨策略分类器性能（AUC 0.13→0.68），提供了一种实用的跨策略泛化方案。现有文献中未见类似方法应用于此场景。
4. **推理递归 vs 训练递归**: 现有 model collapse 文献主要研究 train-on-output 范式，我们研究的是 inference-time recursive generation（将输出作为下一轮输入），场景不同但退化机制相似。

---

## 推荐引用（论文 Discussion 段）

### 用于说明 temperature 加速收敛的理论基础:
> Marchi et al. (2024) proved that any non-trivial temperature in closed-loop generative learning leads to asymptotic degeneration, with T<1 amplifying probability differences and driving mode collapse. Our empirical observation that τ=0.9 shifts depth-wise feature distributions by approximately one depth level is consistent with this theoretical prediction.

### 用于区分 temperature 与 truncation 的退化机制:
> Unlike top-p and top-k sampling which produce "tail cutting" through hard truncation, temperature scaling causes "tail narrowing" by continuously adjusting the power-law exponent (Dohmatob et al., 2024). This mechanistic difference explains why temperature-sampled text exhibits systematic covariate shift rather than merely increased noise in our cross-strategy experiments.

### 用于支持 temperature 退化的实证证据:
> Drayson et al. (2025) found that temperature sampling (τ=0.9) led to the most repetitive outputs in recursive training, with diversity decreasing by ~70% while perplexity degradation remained more moderate than deterministic methods. This pattern—lower diversity with relatively preserved fluency—aligns with our finding that temperature-generated text converges faster to a low-perplexity attractor distribution.

### 用于将协变量偏移与 model collapse 框架联系:
> The model collapse phenomenon (Shumailov et al., 2024) demonstrates that tail erosion accumulates across recursive generations. We extend this framework to show that different sampling strategies induce systematically different convergence rates, creating a covariate shift that can be corrected via simple z-score normalization of depth-wise features.

### 用于说明跨策略检测泛化问题:
> Cross-domain AI text detection benchmarks (e.g., RAID) have shown that detectors trained on one generation configuration often fail to generalize to others. Our z-score normalization approach addresses a specific instance of this challenge: correcting for the systematic feature-space shift between temperature scaling and truncation-based sampling strategies.
