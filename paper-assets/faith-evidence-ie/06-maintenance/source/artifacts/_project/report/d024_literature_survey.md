# D024 文献调研：CED Reward 的 Anti-Mode-Collapse 效应

## 背景

在 GRPO 训练中，CED reward（对比证据判别）在相同配置下显著优于 extraction-only 和 flat-NLI reward，后两者在 10-30 步内 mode collapse。假设：CED 提供的多维梯度信号增加了 reward landscape 复杂性，使 GRPO 多样性采样更不容易退化。

---

## 1. Reward Shaping for RLHF/GRPO Stability

### 1.1 GRPO 中的 Entropy/Mode Collapse 分析

**DAPO: An Open-Source LLM Reinforcement Learning System at Scale**
- 作者: ByteDance Seed Team
- 年份/Venue: 2025, arXiv:2503.14476
- 核心发现: PPO/GRPO 的对称 clipping 限制低概率 action 导致 entropy collapse；DAPO 提出 Clip-Higher（放宽上界）和 Dynamic Sampling 保持探索性，在 Qwen2.5-32B 上 AIME 2024 达 50 分。
- **与我们的关联**: CED reward 可能起到类似 Dynamic Sampling 的作用——提供更丰富的梯度信号维度，避免所有 sample 收敛到同一高 reward 策略。

**GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control**
- 作者: Su et al.
- 年份/Venue: 2025, arXiv:2508.03772
- 核心发现: 识别 GRPO 中的 conflict tokens（同位置 token 在不同 response 中获得相反 reward），保护它们跳过负更新；设置 entropy 阈值过滤易导致 policy collapse 的 completion。
- **与我们的关联**: CED reward 的对比机制天然区分了 evidence quality 维度上的 conflict，可能提供了隐式的 conflict token 保护。

**EDGE-GRPO: Entropy-Driven GRPO with Guided Error Correction for Advantage Diversity**
- 作者: Zhang, Wen, Wu, Huang
- 年份/Venue: 2025, arXiv:2507.21848
- 核心发现: GRPO 中 group 内 reward 相同导致 advantage collapse（frac_zero_std 问题）；通过 entropy-driven advantage 和 guided error correction 增加 advantage diversity。
- **与我们的关联**: 直接对应我们观察到的 frac_zero_std→0.9 现象。CED reward 作为额外 reward 维度，天然增加了 group 内 advantage variance，减轻 advantage collapse。这是最强的理论支撑之一。

**Dr. GRPO: Understanding R1-Zero-Like Training: A Critical Perspective**
- 作者: Liu et al. (Sea AI Lab)
- 年份/Venue: 2025, COLM 2025, arXiv:2503.20783
- 核心发现: GRPO 存在 optimization bias——response length normalization 人为增加长度偏好；Dr. GRPO 移除有偏归一化项，保持输出长度稳定且准确率提升（AIME 2024: 43.3% vs GRPO 36.0%）。
- **与我们的关联**: 说明 reward 设计中的 bias 直接影响 GRPO 稳定性。CED reward 的对比性质可能提供了更平衡的信号。

**DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO**
- 作者: Liu et al.
- 年份/Venue: 2025, arXiv:2512.21514
- 核心发现: 传统 GRPO 依赖 single-sample quality 作为 reward，驱动模型收敛到少数高 reward mode。DiverseGRPO 通过 spectral clustering 构建分布级表示，分配 exploratory reward 鼓励发现新 mode，实现 13-18% 语义多样性提升。
- **与我们的关联**: 我们的 CED reward 本质上也是在 reward 中引入了"多样性维度"——evidence 质量不同于 extraction accuracy，增加了 reward landscape 的模式数量。

### 1.2 Multi-Objective Reward 防 Mode Collapse

**Safe RLHF: Constrained Value Alignment via Safe Reinforcement Learning from Human Feedback (Beaver)**
- 作者: Dai, Pan, Sun, Ji, Xu, Liu, Wang, Yang
- 年份/Venue: ICLR 2024 Spotlight, arXiv:2310.03295
- 核心发现: 训练独立的 reward model 和 cost model，通过 Lagrangian 优化同时最大化 reward 和满足 safety constraint。双目标优化避免了单一 reward 的盲区。
- **与我们的关联**: CED reward（evidence quality）+ extraction reward（F1）本质上是双目标优化，Safe RLHF 提供了多目标 RLHF 稳定性的理论先例。

**Directional Preference Alignment with Multi-Objective Rewards (DPA)**
- 作者: Wang et al.
- 年份/Venue: ACL 2024, arXiv:2402.18571
- 核心发现: 将用户偏好建模为 reward 空间中的方向向量，多目标 reward model 捕捉 diverse preference profiles。在 Mistral-7B 上验证用户可算术控制 trade-off（如 helpfulness vs verbosity）。
- **与我们的关联**: 理论上支持了多维 reward 空间比标量 reward 更能维持策略多样性的观点。

**Multi-Objective Direct Preference Optimization (MODPO)**
- 作者: Zhou et al.
- 年份/Venue: 2024, arXiv:2310.03708
- 核心发现: 无 RL 的多目标 DPO 扩展，理论上产生与 multi-objective RLHF 相同的最优解，产出 Pareto front 的语言模型，计算资源仅需 1/3。
- **与我们的关联**: 进一步证实多目标设置在偏好优化中的稳定性优势。

**Sotopia-RL: Reward Design for Social Intelligence**
- 作者: Wang et al.
- 年份/Venue: 2025, arXiv:2508.03905
- 核心发现: 将粗粒度 episode-level feedback 细化为 utterance-level 多维 reward；多维 reward 捕捉社交交互的丰富性，减少 reward hacking。
- **与我们的关联**: 与我们的发现高度一致——细粒度、多维 reward 天然抵抗 reward hacking 和 mode collapse。

**Multi-Objective Reinforcement Learning for Large Language Model Optimization: Visionary Perspective**
- 作者: Ramírez et al.
- 年份/Venue: 2025, arXiv:2509.21613
- 核心发现: 综述 MORL 在 LLM 中的应用，指出关键挑战包括 balancing objectives、Pareto-optimality、稳定性。明确提出多目标设置有助于避免单一 reward 的 overoptimization。
- **与我们的关联**: 为我们的发现提供了理论框架——CED 作为额外目标维度增加了 Pareto front 的复杂性。

### 1.3 Reward Shaping 与 Policy Optimization 稳定性

**Reward Shaping to Mitigate Reward Hacking in RLHF (PAR)**
- 作者: Fan et al.
- 年份/Venue: 2025, arXiv:2502.18770
- 核心发现: 提出两个 reward design 原则：(1) RL reward 应有界，(2) reward 应快速初始增长后逐渐收敛。PAR 方法在 AlpacaEval 2.0 上 win rate 高出 5+%。
- **与我们的关联**: CED reward 的对比性质天然有界（NLI score ∈ [0,1]），符合其提出的稳定 reward 设计原则。

**Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer (RPO)**
- 作者: Liu et al.
- 年份/Venue: NeurIPS 2024, arXiv:2405.16436
- 核心发现: 将 overoptimization 归因于分布偏移，提出 RPO 将 SFT loss 作为对抗性正则化项。
- **与我们的关联**: CED reward 可能起到类似正则化效果——对比信号约束模型不偏离 evidence 质量标准。

---

## 2. Mode Collapse in LLM RL Fine-tuning

### 2.1 Mode Collapse 的原因分析

**Understanding the Effects of RLHF on LLM Generalisation and Diversity**
- 作者: Kirk, Mediratta, Nalmpantis, Luketina, Hambro, Grefenstette, Raileanu
- 年份/Venue: ICLR 2024, arXiv:2310.06452
- 核心发现: RLHF 比 SFT 泛化更好，但显著降低输出多样性——生成文本结构重复、词汇单一、视角狭窄。存在 generalization-diversity tradeoff。
- **与我们的关联**: 我们的 extraction-only reward 正是这种 diversity collapse 的典型案例。CED reward 可能缓解了这一 tradeoff。

**KL-Regularized Reinforcement Learning is Designed to Mode Collapse**
- 作者: GX-Chen et al.
- 年份/Venue: 2025, arXiv:2510.20817
- 核心发现: KL 正则化的 mode collapse 不仅因为 reverse KL 的 mode-seeking 性质，更因为低正则化强度和等值 verifiable reward 天然指定了单峰目标分布。提出 reward rescaling 诱导多峰分布。
- **与我们的关联**: **关键理论支撑**。我们的 extraction-only reward（format+F1）本质上是"等值 verifiable reward"——多数正确 extraction 获得相似分数，天然单峰。CED 引入的 evidence quality 维度打破了这种等值性，使目标分布多峰化。

**On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization**
- 作者: Xu et al.
- 年份/Venue: 2024, arXiv:2405.16455; JASA 2025
- 核心发现: RLHF 的 KL 正则化存在固有 algorithmic bias，导致 preference collapse（少数偏好被忽略）。提出 Preference Matching (PM) RLHF 通过 ODE 推导的正则化项平衡多样化和 reward 最大化，提升 29-41%。
- **与我们的关联**: 单一 reward 的 preference collapse 可解释 flat-NLI 和 extraction-only 的快速 collapse。CED 的多维信号天然提供了 preference matching 式的多样化压力。

### 2.2 Reward Overoptimization

**Scaling Laws for Reward Model Overoptimization**
- 作者: Gao, Schulman, Hilton
- 年份/Venue: ICML 2023, arXiv:2210.10760
- 核心发现: 优化 proxy reward 的关系遵循可预测的 scaling law——RL 和 BoN 采样有不同的功能形式；过度优化导致 gold reward 下降。系数随 reward model 参数量平滑缩放。
- **与我们的关联**: 经典参考。我们的 extraction-only reward 可能更容易被 overoptimize（低维 proxy），而 CED 增加了 reward 维度使 overoptimization 更困难。

**Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms**
- 作者: Rafailov et al.
- 年份/Venue: 2024, arXiv:2406.02900
- 核心发现: Overoptimization 在 DPO 等 direct alignment 方法中同样存在，甚至在一个 epoch 之前就出现，说明这是 preference-based alignment 的固有问题。
- **与我们的关联**: 强化了 reward design（而非仅算法选择）是防止 overoptimization 的关键。

**Reward Model Ensembles Help Mitigate Overoptimization**
- 作者: Coste et al.
- 年份/Venue: ICLR 2024, arXiv:2310.02743
- 核心发现: Ensemble-based conservative optimization 几乎消除 overoptimization，BoN 采样性能提升 70%。结合 KL penalty 完全防止 PPO 的 overoptimization。
- **与我们的关联**: 多 reward signal 的 ensemble 效果类似于我们的多维 reward。CED+F1 可视为一种 implicit reward ensemble。

**InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling**
- 作者: Chen et al.
- 年份/Venue: NeurIPS 2024, arXiv:2402.09345
- 核心发现: 通过 variational information bottleneck 过滤 reward model 中与人类偏好无关的信息，减少 reward hacking。发现 overoptimization 与 IB latent space 中的 outlier 相关。
- **与我们的关联**: CED reward 直接基于 NLI 模型而非 learned reward model，可能天然具有更少的 spurious features。

### 2.3 DeepSeek-R1 与 GRPO 实践

**DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning**
- 作者: DeepSeek Team
- 年份/Venue: 2025, Nature, arXiv:2501.12948
- 核心发现: 纯 GRPO + correctness reward 可激发 LLM 推理能力（R1-Zero），但存在 reward hacking（如语言混合、重复 pattern）。最终采用 SFT + RL 的 pipeline 稳定训练。
- **与我们的关联**: R1-Zero 的 reward hacking 正是单维 reward 的典型问题。CED 的多维信号可视为一种隐式的 format/quality constraint。

---

## 3. Contrastive Reward in RL

### 3.1 Contrastive Likelihood/Reward 方法

**CTRL-RAG: Contrastive Likelihood Reward Based Reinforcement Learning for Context-Faithful RAG Models**
- 作者: (未详)
- 年份/Venue: 2026, arXiv:2603.04406
- 核心发现: 首个专为 RAG 设计的 RL 方法，使用 Contrastive Likelihood Reward (CLR) 优化 context faithfulness——直接优化 response 在有/无 evidence 条件下的 log-likelihood 差值。单独或结合 correctness reward 均有效。
- **与我们的关联**: **最直接的先例**。我们的 CED reward 同样通过对比有/无 evidence 来衡量 faithfulness。CTRL-RAG 证明 contrastive reward 在 RL 中可行且有效，但他们未分析 anti-mode-collapse 效应——这是我们的独特贡献。

**Improving Factuality of Abstractive Summarization via Contrastive Reward Learning**
- 作者: Chern et al.
- 年份/Venue: TrustNLP Workshop 2023, arXiv:2307.04507
- 核心发现: 提出 contrastive reward learning 框架，让摘要模型直接从 factuality metrics 的反馈中学习，使用 diverse beam search 生成候选摘要进行对比训练。
- **与我们的关联**: 早期 contrastive reward 用于 factuality 的先例。我们将对比从训练时的 sample selection 推进到了 reward signal 本身。

**CLIFF: Contrastive Learning for Improving Faithfulness and Factuality in Abstractive Summarization**
- 作者: Cao, Wang
- 年份/Venue: EMNLP 2021, arXiv:2109.09209
- 核心发现: 利用 reference summary（正例）和自动生成的错误摘要（负例）进行对比学习，设计 4 种负样本策略模拟 BART/PEGASUS 的常见错误。在 XSum 和 CNN/DM 上稳定提升 factuality。
- **与我们的关联**: 奠基性工作——证明对比学习可用于 faithfulness。我们的 CED 将这一思想从训练目标扩展到 RL reward signal。

### 3.2 NLI-based Reward

**Improving Factual Consistency of News Summarization by Contrastive Preference Optimization (CPO)**
- 作者: Feng et al.
- 年份/Venue: EMNLP 2024 Findings, arXiv:2310.19347
- 核心发现: 训练 NLI model 进行 consistency detection，将其作为 RL 的 reward model。CPO 分离 LLM 生成 faithful/fake content 的倾向，显著提升摘要可靠性。
- **与我们的关联**: NLI 作为 reward 的直接先例。但他们使用 flat NLI（非对比），我们的 CED 通过对比增强了 NLI signal 的判别力。

**PrefixNLI: Detecting Factual Inconsistencies as Soon as They Arise**
- 作者: (未详)
- 年份/Venue: 2025, arXiv:2511.01359
- 核心发现: NLI 模型广泛用于评估 factual consistency，可在生成时通过 beam reranking 或训练时通过 RL reward 提供反馈。提出 prefix-level entailment 检测，比 baseline NLI 模型提升 5-14 F1。
- **与我们的关联**: 支持 NLI-based reward 在 RL 中的可行性。Prefix-level 检测思想可作为未来改进 CED 的方向。

### 3.3 Evidence-based Reward Design

**Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning**
- 作者: (未详)
- 年份/Venue: 2025, arXiv:2605.08061
- 核心发现: 将 reward 分解为加权的可验证 criteria，用 LLM judge 评分，配合 GRPO 优化。Rubric-based reward 比单一 reward 更能泛化。
- **与我们的关联**: CED 可视为一种 rubric-grounded reward——evidence faithfulness 是 extraction 任务中的一个可验证 criterion。

**Information-Theoretic Reward Decomposition for Generalizable RLHF**
- 作者: (未详)
- 年份/Venue: 2025, arXiv:2504.06020
- 核心发现: 将 reward 分解为 prompt-free reward（仅由 response 决定）和 prompt-related reward（由 prompt+response 共同决定），提升 reward 泛化性。
- **与我们的关联**: CED reward 的 evidence 维度本质上是 prompt-related reward（依赖输入 evidence），而 format reward 是 prompt-free reward。这种分解可能是 CED 稳定性的来源之一。

---

## 4. 对 Paper Story 的建议

### 4.1 核心定位

CED 的 anti-mode-collapse 效应应定位为 **surprising finding + principled explanation**，而非 main contribution：

- **Main contribution**: CED reward design 本身——对比 evidence 判别作为 IE GRPO 的 reward signal
- **Surprising finding**: CED 不仅提升 evidence faithfulness，还显著防止 mode collapse
- **Principled explanation**: 可通过以下文献链条论证
  1. GRPO 的 advantage collapse 是已知问题（EDGE-GRPO, DAPO）
  2. 单维/等值 reward 天然导致单峰目标分布（GX-Chen et al., 2025）
  3. 多目标 reward 增加 reward landscape 复杂性，维持策略多样性（DiverseGRPO, Safe RLHF, Sotopia-RL）
  4. CED 作为额外的 evidence quality 维度，打破了 extraction-only reward 的等值性

### 4.2 建议的论文叙事结构

1. **Motivation**: IE 任务中 evidence faithfulness 重要但被忽视
2. **Method**: CED reward design
3. **Main results**: CED 提升 faithfulness metrics
4. **Analysis section**: 发现 anti-mode-collapse 效应
   - 实验对比：CED vs extraction-only vs flat-NLI 的 training dynamics
   - 指标：frac_zero_std, entropy, reward trajectory
   - 理论解释：引用 GX-Chen et al.（等值 reward 导致单峰分布）和 EDGE-GRPO（advantage collapse）
   - 与 multi-objective reward 文献的联系

### 4.3 可引用的关键论文（按重要性排序）

| 优先级 | 论文 | 引用理由 |
|--------|------|----------|
| **必引** | GX-Chen et al. 2025 (KL-RL mode collapse) | 直接解释等值 reward 为何 collapse |
| **必引** | EDGE-GRPO (Zhang et al. 2025) | frac_zero_std / advantage collapse 的定义和分析 |
| **必引** | DAPO (ByteDance 2025) | GRPO entropy collapse 的标准参考 |
| **必引** | CTRL-RAG (2026) | contrastive reward for faithfulness 的最近先例 |
| **强烈推荐** | Kirk et al. 2024 (RLHF diversity) | RLHF diversity loss 的经典分析 |
| **强烈推荐** | DiverseGRPO (Liu et al. 2025) | diversity-aware reward design 的直接类比 |
| **强烈推荐** | Gao et al. 2023 (scaling laws) | reward overoptimization 的经典引用 |
| **推荐** | Safe RLHF (Dai et al. 2024) | multi-objective RLHF 的先例 |
| **推荐** | CLIFF (Cao & Wang 2021) | contrastive learning for faithfulness 的奠基工作 |
| **推荐** | CPO (Feng et al. 2024) | NLI as reward 的直接先例 |

### 4.4 差异化论点

我们的发现与现有文献的关键差异：
1. **CTRL-RAG** 证明 contrastive reward 可用于 faithfulness，但未分析 training stability 效应
2. **DiverseGRPO** 通过显式 diversity reward 防 collapse，我们的 CED 是隐式的——evidence quality 维度自然增加了多样性
3. **EDGE-GRPO** 通过 entropy-driven advantage 解决 advantage collapse，我们的 CED 通过增加 reward 维度自然增加 advantage variance
4. **GX-Chen et al.** 的理论预测（等值 reward → 单峰分布）直接解释了为什么 extraction-only collapse 而 CED 不 collapse

这使得 CED 的 anti-collapse 效应成为一个 **empirically validated instance of a theoretically predicted phenomenon**——既有实验证据又有理论支撑，非常适合作为论文的 analysis highlight。
