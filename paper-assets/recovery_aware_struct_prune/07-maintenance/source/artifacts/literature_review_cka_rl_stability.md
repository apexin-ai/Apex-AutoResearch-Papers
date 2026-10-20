# 文献综述：CKA/功能多样性与 RL 训练稳定性的关系

**日期**: 2026-05-15
**背景**: RASP (CKA-aware pruning) 保留功能独特结构，但 GRPO 恢复连续 3 次 collapse；Standard (importance-only) 相同配置下展现健康学习信号。

---

## 一、直接相关论文

### 1. Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning
- **Authors**: OpenReview submission (anonymous)
- **Year**: 2025 (ICLR 2026 under review)
- **Venue**: OpenReview (https://openreview.net/forum?id=Cy8Qa4gAst)
- **核心内容**: 提出用 RLVR (Reinforcement Learning with Verifiable Reward) 替代 SFT 做剪枝后恢复训练。发现 structured pruning 降低数学推理能力但未完全摧毁，SFT 仅模仿训练数据中的推理轨迹导致性能瓶颈和数据效率低，而 RLVR 可实现 "self-healing" 达到 95%+ recovery。
- **与我们的关系**: **直接竞品/参照**。他们用 standard importance pruning + RLVR 成功——但**没有报告测试其他 pruning criterion**。论文聚焦 recovery method 的创新，pruning criterion 是固定变量。**没有 CKA-aware pruning 的对比实验**。
- **对 diversity tax 假说**: 中性。他们的成功不能反驳我们的发现，因为他们用的是 standard pruning（保留冗余），恰好与我们的机制假说一致。

### 2. Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models
- **Authors**: arXiv:2512.02185
- **Year**: 2025
- **Venue**: arXiv preprint
- **核心内容**: 分析为什么现有剪枝方法在推理 LLM 上即使 20% sparsity 也严重崩溃。**根因：calibration data、pruning objective 与模型 decode-time reasoning behavior 之间的 mismatch**。提出用模型自身推理轨迹做 calibration。
- **与我们的关系**: **高度相关**。他们的 "calibration mismatch" 概念与我们的发现呼应——CKA criterion 优化的是表征多样性保留，但这未必与 RL recovery 的需求对齐。不同的 pruning objective 产生不同的 recovery 动力学。
- **对 diversity tax 假说**: **间接支持**。验证了 pruning criterion 选择对后续训练有重大影响，暗示 criterion × recovery 交互效应的存在。

### 3. Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions
- **Authors**: arXiv:2605.07271
- **Year**: 2026 (May)
- **Venue**: arXiv preprint
- **核心内容**: 提出 Decision Margin 和 Option Frequency 两个指标分析层剪枝引起的 performance collapse。发现网络分为 Silent Phase（模型无法预测正确答案，分布坍缩到单一选项）和 Decisive Phase（正确预测涌现，分布均衡）。剪枝破坏 phase transition 导致 collapse。
- **与我们的关系**: 机制层面高度相关。CKA-aware pruning 可能破坏了 Silent→Decisive 的 phase transition 路径，使得 RL 训练无法引导模型从 collapse 中恢复。
- **对 diversity tax 假说**: **间接支持**。功能多样的结构如果恰好是 Decisive Phase 的"脚手架"，移除冗余反而破坏了 phase transition 所需的缓冲。

### 4. The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in RLVR
- **Authors**: arXiv:2509.07430
- **Year**: 2025
- **Venue**: OpenReview (https://openreview.net/forum?id=xPEsxcO7F7)
- **核心内容**: RLVR 中 reverse-KL divergence 的 mode-seeking 特性是 diversity collapse 的根因。模型输出趋同、policy entropy collapse，丧失探索新解的能力。提出用 forward-KL 和 JS-divergence 替代。
- **与我们的关系**: **高度相关**。如果 CKA-aware pruning 已经移除了冗余结构（减少了表征空间的"备用路径"），GRPO 中的 reverse-KL 机制会加速 mode collapse——模型没有足够的冗余结构来维持多样采样。Standard pruning 保留冗余 → 有更多 mode 可供 GRPO 探索 → 不易 collapse。
- **对 diversity tax 假说**: **强支持**。直接佐证了"功能多样性 + RLVR 的 mode-seeking divergence = 双重压缩效应"的机制。

### 5. DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards
- **Authors**: arXiv:2603.16157
- **Year**: 2026
- **Venue**: arXiv preprint
- **核心内容**: 提出 Dynamic Jensen-Shannon Replay，用动态参考分布和 JS-divergence 正则化防止 RLVR 中的 diversity collapse。
- **与我们的关系**: 进一步证实 RLVR diversity collapse 是一个已知且活跃的研究问题。我们的发现增加了 pruning criterion 这个新维度。
- **对 diversity tax 假说**: **支持**。

---

## 二、机制理论支撑论文

### 6. In Value-Based Deep RL, a Pruned Network is a Good Network
- **Authors**: Obando-Ceron et al.
- **Year**: 2024
- **Venue**: ICML 2024
- **核心内容**: Gradual magnitude pruning 在 deep RL 中大幅提升性能。关键机制：**剪枝降低 gradient colinearity（梯度共线性），减少 gradient interference，提升 plasticity**。稀疏网络的梯度冲突显著弱于密集网络。
- **与我们的关系**: **关键理论基础**。但他们发现的是 element-wise pruning 的好处（保留结构多样性的同时去除冗余参数）。CKA-aware structured pruning 做的是相反的事——它在 group level 保留功能独特结构，但每个保留的 group 内部是完整的、功能特化的。这可能导致 **group 间梯度方向过于正交 → RL 的 reward signal 无法同时驱动所有 group → gradient conflict → collapse**。
- **对 diversity tax 假说**: **强支持机制解释**。Element-wise pruning 减少 gradient interference（好事），但 CKA-aware structured pruning 可能在 group level 增加了 gradient conflict（坏事）。

### 7. Sparsity-Driven Plasticity in Multi-Task Reinforcement Learning
- **Authors**: arXiv:2508.06871
- **Year**: 2025
- **Venue**: OpenReview
- **核心内容**: GMP 和 SET 稀疏化方法在 MTRL 中增强 plasticity，缓解 neuron dormancy 和 representational collapse。**Actor-only pruning (81%) 优于 dense baseline (73%) 和 global pruning (75%)**。
- **与我们的关系**: 进一步证实稀疏性可以帮助 RL plasticity——但前提是稀疏性引入了结构上的"呼吸空间"。CKA-aware pruning 的问题不在于稀疏性本身，而在于保留的结构过于"紧致"缺乏冗余缓冲。
- **对 diversity tax 假说**: **支持**。

### 8. Loss of Plasticity in Continual Deep Reinforcement Learning
- **Authors**: Abbas et al.
- **Year**: 2023 (Nature 2024 follow-up)
- **Venue**: AAAI 2023 / Nature 2024
- **核心内容**: Deep RL 中 plasticity loss 的系统性研究。表现为：gradient interference → premature convergence、representational collapse → feature diversity 下降、neuronal saturation/dormancy → 有效容量减少。**唯一持久维持 plasticity 的方法是持续注入多样性（如 continual backpropagation 中的 neuron reinitialization）**。
- **与我们的关系**: **核心理论**。CKA-aware pruning 移除冗余 → 减少了网络中的"多样性储备" → RL 训练时没有可重新初始化/重新利用的结构 → 加速 plasticity loss → collapse。Standard pruning 偶然保留冗余结构 = 天然的"多样性储备"。
- **对 diversity tax 假说**: **强支持**。

### 9. Frustratingly Easy Regularization on Representation Can Boost Deep RL
- **Authors**: He et al.
- **Year**: 2023
- **Venue**: CVPR 2023
- **核心内容**: Q-network 的学习表征应满足 "distinguishable representation property"。实际中 DRL agent 常违反此性质导致次优策略。简单的表征正则化（PEER）可大幅提升性能。
- **与我们的关系**: 间接相关。CKA-aware pruning 保留的"功能独特"结构理论上应促进 distinguishable representation，但在 RL 优化中反而可能因为过于独特导致 reward signal 无法有效传播。
- **对 diversity tax 假说**: 中性偏支持。

---

## 三、相关但间接的论文

### 10. PASER: Post-Training Data Selection for Efficient Pruned LLM Recovery
- **Authors**: arXiv:2502.12594
- **Year**: 2025
- **Venue**: OpenReview
- **核心内容**: 剪枝后不同能力退化程度不均匀，需要自适应数据选择来高效恢复。用 4-20% 数据即可显著恢复能力。
- **与我们的关系**: 证实 pruning 后能力退化是非均匀的，不同恢复策略需要适配剪枝造成的特定损伤模式。CKA pruning 和 standard pruning 造成不同的损伤模式 → 需要不同的恢复策略。
- **对 diversity tax 假说**: 间接支持 criterion × recovery 交互效应。

### 11. Comparing Rewinding and Fine-tuning in Neural Network Pruning
- **Authors**: Renda et al.
- **Year**: 2020
- **Venue**: ICLR 2020
- **核心内容**: Weight rewinding 优于 standard fine-tuning 作为剪枝后恢复方法。不同 pruning 决策需要不同的恢复策略。
- **与我们的关系**: 经典工作，证实 pruning criterion 与 recovery method 之间存在交互效应，但仅限 supervised learning 场景，未涉及 RL。

### 12. Dynamic Vocabulary Pruning: Stable LLM-RL by Taming the Tail
- **Authors**: arXiv:2512.23087
- **Year**: 2025
- **Venue**: arXiv preprint
- **核心内容**: LLM-RL 训练不稳定的根因是 log-probability mismatch——低概率 token 区域对数值噪声极度敏感。提出 Dynamic Vocabulary Pruning 约束 RL 目标到"安全"词表。
- **与我们的关系**: 揭示了 RL 训练在概率分布尾部的脆弱性。CKA-aware 剪枝可能改变了模型的输出分布形状，扩大了低概率区域的不稳定性。
- **对 diversity tax 假说**: 间接支持（提供了另一条 collapse 机制路径）。

### 13. Proactive Gradient Conflict Mitigation in Multi-Task Learning: A Sparse Training Perspective
- **Authors**: arXiv:2411.18615
- **Year**: 2024
- **Venue**: arXiv preprint
- **核心内容**: 稀疏训练本身可以减少 gradient conflict。当不同任务需要特化知识时，gradient conflict 会降低整体性能。
- **与我们的关系**: GRPO 本质上是多目标优化（accuracy reward + format reward + KL penalty）。CKA-aware pruning 保留的功能特化结构可能加剧了不同 reward signal 之间的 gradient conflict。

---

## 四、回答四个核心问题

### Q1: 是否有先例报告 CKA-guided pruning 在 RL/RLHF 场景下的失败？

**没有。** 文献中 CKA 用于 pruning 的工作（URI thesis, Lachance 2024; Layer Pruning with Consensus, 2024）均仅在 supervised 评估下验证。Self-Healing (ICLR 2026 review) 用 RLVR 做恢复但用的是 standard importance pruning。**CKA-guided pruning + RL recovery 这个组合是文献空白。**

### Q2: 是否有理论/实证研究解释"功能多样性"如何影响 RL 优化稳定性？

**有间接证据，但无直接研究。**
- Abbas et al. (2023/Nature 2024) 证明 plasticity 需要持续的多样性注入；
- Obando-Ceron et al. (ICML 2024) 证明 pruning 减少 gradient interference 有利于 RL；
- Choice of Divergence (2025) 证明 RLVR 本身有 diversity collapse 倾向。

但**没有论文研究过"保留功能多样性（去除冗余）是否反而损害 RL 训练"**。这个方向是反直觉的——直觉上保留多样性应该有利，但我们的实验表明在 RL 场景下，冗余（而非多样性）才是稳定性的关键。

### Q3: Self-Healing (ICLR 2026) 是否测试了其他 pruning criterion？

**搜索结果表明没有。** Self-Healing 论文聚焦 recovery method 的创新（RLVR vs SFT），pruning 方面使用的是标准 structured pruning（基于 importance/magnitude）。未报告对 CKA-aware、GraSP、或其他 criterion 的对比。

### Q4: 是否有论文讨论过 "pruning criterion × recovery method interaction"？

**仅有有限的监督学习先例：**
- Renda et al. (ICLR 2020): rewinding vs fine-tuning 对不同 pruning 的交互
- PASER (2025): 不同剪枝损伤模式需要不同数据来恢复
- Think Before You Prune (2025): calibration mismatch 概念

**在 RL recovery 场景下完全没有。** "Pruning criterion × RL-based recovery method interaction" 是一个未被研究的方向。

---

## 五、总结：Novelty 评估

### 现有文献已知的
1. RLVR 可以有效恢复 pruned model（Self-Healing, 2025）
2. RLVR 存在 diversity collapse 问题（Choice of Divergence, 2025; DyJR, 2026）
3. Pruning 可以提升 RL plasticity（Obando-Ceron, 2024; Sparsity-Driven Plasticity, 2025）
4. Pruning criterion 选择影响下游性能（Think Before You Prune, 2025）
5. Pruning 后不同能力退化非均匀（PASER, 2025; Decision Representation, 2026）

### 我们发现的 novel 之处
1. **CKA-guided pruning × RL recovery 的交互失败** — 文献空白，从未有人测试过
2. **"Diversity Tax" 假说** — 功能多样性保留（去冗余）在 RL 场景下反而有害 — 反直觉且无先例
3. **冗余作为 RL plasticity buffer 的机制** — 现有 plasticity 文献讨论的是 sparsity（element-wise），不是 structural redundancy 的保护作用
4. **Pruning criterion × recovery method 交互在 RL 场景下的首个实证** — Renda 2020 仅限 supervised，无人在 RL 做过

### Novelty 评级：**高**

这个 negative finding 填补了两个活跃研究方向（pruning for LLM + RLVR recovery）交叉处的重要空白。特别是 "diversity tax" 假说——功能多样性在 supervised recovery 和 RL recovery 下表现出截然不同的效用——如果得到更多实验验证，可以成为一个有影响力的 insight。

---

## Sources

- [Self-Healing: Recovering Pruned Large Reasoning Models via RL](https://openreview.net/forum?id=Cy8Qa4gAst)
- [Think Before You Prune: Self-Reflective Structured Pruning](https://arxiv.org/abs/2512.02185)
- [Understanding Performance Collapse in Layer-Pruned LLMs](https://arxiv.org/abs/2605.07271)
- [The Choice of Divergence: Mitigating Diversity Collapse in RLVR](https://arxiv.org/abs/2509.07430)
- [DyJR: Preserving Diversity in RLVR](https://arxiv.org/abs/2603.16157)
- [In Value-Based Deep RL, a Pruned Network is a Good Network](https://arxiv.org/abs/2402.12479) (ICML 2024)
- [Sparsity-Driven Plasticity in Multi-Task RL](https://arxiv.org/abs/2508.06871)
- [Loss of Plasticity in Continual Deep RL](https://arxiv.org/abs/2303.07507) (Nature 2024)
- [Frustratingly Easy Regularization on Representation (PEER)](https://arxiv.org/abs/2205.14557) (CVPR 2023)
- [PASER: Post-Training Data Selection for Pruned LLM Recovery](https://arxiv.org/abs/2502.12594)
- [Comparing Rewinding and Fine-tuning in Pruning](https://arxiv.org/abs/2003.02389) (ICLR 2020)
- [Dynamic Vocabulary Pruning: Stable LLM-RL](https://arxiv.org/abs/2512.23087)
- [Proactive Gradient Conflict Mitigation via Sparse Training](https://arxiv.org/abs/2411.18615)
- [Network Sparsity Unlocks Scaling in Deep RL](https://arxiv.org/abs/2506.17204) (ICML 2025)
- [Layer Pruning with Consensus](https://arxiv.org/abs/2411.14345)
- [CKA-RL: Continual Knowledge Adaptation for RL](https://github.com/Fhujinwu/CKA-RL) (NeurIPS 2025)
- [LaCo: LLM Pruning via Layer Collapse](https://arxiv.org/abs/2402.11187)
- [When Fewer Layers Break More Chains](https://arxiv.org/abs/2510.22228)
