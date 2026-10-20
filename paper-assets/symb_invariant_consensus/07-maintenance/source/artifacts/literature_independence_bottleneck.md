# Literature Survey: Independence Bottleneck in LLM Self-Consistency

> 调研日期: 2026-05-19 | 覆盖范围: 2024-2026 | 共 23 篇论文

---

## 1. LLM Reasoning Diversity & Self-Consistency Limitations

### 1.1 Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity
- **Authors**: Jiayi Zhang, Simon Yu, Derek Chong, Anthony Sicilia, Michael R. Tomz, Christopher D. Manning, Weiyan Shi
- **Venue**: arXiv 2510.01171 (Oct 2025), under review
- **核心发现**: Post-training alignment 导致 LLM 产生 mode collapse，根本原因是 preference data 中的 typicality bias（人类标注者系统性偏好典型/流畅文本）。提出 Verbalized Sampling (VS)，通过 prompting 让模型显式输出 response 分布，diversity 提升 2-3x，无需额外训练。
- **与我们的关系**: 直接解释了 SICA 中同模型采样 trace 高度同源的 data-level 根因——alignment 训练压缩了输出分布。VS 的 prompting 策略可作为打破 independence bottleneck 的轻量级 baseline。

### 1.2 Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling
- **Authors**: Aggarwal & Deshpande
- **Venue**: NAACL 2025 (Long Paper)
- **核心发现**: 标准 SC 对所有 sample 同等对待，仅基于 final answer 一致性做停止决策，缺乏区分 reasoning 质量的机制。RASC 动态评估 output 和 rationale，提升采样效率和 reasoning faithfulness。
- **与我们的关系**: 揭示了 SC 的结构性缺陷：它不区分 reasoning path 质量，这与 SICA 的约束独立性问题互补——即使 path 多样，如果约束来源相同，增加 K 也无法提供新信息。

### 1.3 Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning
- **Authors**: Gisang Lee et al.
- **Venue**: arXiv 2410.09780 (Oct 2024)
- **核心发现**: 不同 prompting 方法（Text CoT / Code / Cumulative Reasoning）探索不同的搜索空间，且问题越难区分越明显。均匀混合多种方法的 sample 可以在减少 ~43% 采样次数的情况下达到最大搜索空间覆盖。
- **与我们的关系**: 直接证据：同一模型的单一 prompting 方式产生的 trace 搜索空间高度重叠。多 prompting 策略是打破 independence bottleneck 的实用手段，可与 SICA 的 cross-model 策略结合。

### 1.4 Confidence Improves Self-Consistency in LLMs
- **Authors**: (2025)
- **Venue**: arXiv 2502.06233 (Feb 2025)
- **核心发现**: 在 SC 投票中引入 confidence weighting 可以提升准确率。但 greedy decoding 牺牲 diversity 和 robustness，beam search 产生的 reasoning 多样性系统性低于 random sampling。
- **与我们的关系**: 确认了 SC 中 diversity-accuracy 的 tension：提高 confidence 可以改善投票质量，但不能解决底层的 independence 问题。SICA 需要在 confidence 和 independence 之间找到新的平衡点。

---

## 2. LLM Debate & Multi-Agent Reasoning

### 2.1 Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate
- **Authors**: Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, Zhaopeng Tu
- **Venue**: EMNLP 2024 (Main)
- **核心发现**: 提出 Multi-Agent Debate (MAD) 框架，agents 以 "tit for tat" 方式辩论，judge 管理过程。适度的对抗水平效果最好；过强则偏离正确答案。LLM 作为 judge 在 agent 异构时可能不公平。
- **与我们的关系**: MAD 通过 debate 机制引入结构化 diversity，但仍受限于同模型的 "思维同质性"。这与 SICA 的 independence bottleneck 本质相同——debate 不等于独立。

### 2.2 Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate (DMAD)
- **Authors**: (2025)
- **Venue**: ICLR 2025
- **核心发现**: MAD 即使分配不同 persona，agents 仍使用同质化思维过程（fixed mental set）。借鉴心理学 mental set 理论，DMAD 强制 agents 使用不同的 reasoning approach（如代数 vs 几何 vs 枚举），打破固定思维模式。
- **与我们的关系**: 核心相关——DMAD 的 "mental set" 概念直接对应 SICA 的 independence bottleneck。即使 K 很大，如果 traces 共享相同的 reasoning approach，约束也是冗余的。DMAD 的 diverse reasoning strategy 可以启发 SICA 的约束生成多样化。

### 2.3 Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning
- **Authors**: Wu, Li et al.
- **Venue**: arXiv 2511.07784 (Nov 2025)
- **核心发现**: 通过 Knight-Knave-Spy 逻辑谜题的受控实验发现：intrinsic reasoning strength 和 group diversity 是 debate 成功的主要驱动力，结构参数（顺序、confidence 可见性）影响有限。Majority pressure 会抑制独立纠错。
- **与我们的关系**: 关键发现：majority pressure 抑制独立性。这直接映射到 SICA 场景——当多数 trace 收敛到相同（错误）约束时，少数正确 trace 的信号被淹没。Group diversity（异构模型）是关键。

### 2.4 ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning
- **Authors**: (2026)
- **Venue**: arXiv 2602.00127 (Jan 2026)
- **核心发现**: 将 LLM reasoning 建模为 aligned delegation game，principal 向 agents 委托任务，agents 生成 candidate solutions。理论证明在公平比较下 ALIGN 比 single-agent 更优，且分析 relaxes independence assumptions（允许 correlated answers）。
- **与我们的关系**: 理论框架直接相关——ALIGN 明确 relaxes 了 independence assumption，承认 candidate answers 之间存在 correlation，仍能提供 performance guarantee。这为 SICA 在非独立约束下的理论分析提供了参考。

### 2.5 From Belief Entrenchment to Robust Reasoning in LLM Agents (DReaMAD)
- **Authors**: (2025)
- **Venue**: arXiv 2503.16814 (Mar 2025)
- **核心发现**: MAD 中的 belief entrenchment 有两个根因：(1) 模型的 biased static initial belief，(2) homogenized debate dynamics 放大多数观点。DReaMAD 通过 strategic prior knowledge elicitation 修正初始 belief，通过 enforcing perspective diversity 重塑 debate dynamics，accuracy +9.5% over ReAct。
- **与我们的关系**: "Homogenized debate dynamics" 是 independence bottleneck 在 debate 场景的具体表现。DReaMAD 的两阶段策略（修正 prior + 强制 diversity）可以直接迁移到 SICA：先 diversify 约束来源，再防止约束收敛。

### 2.6 Self-Debate Reinforcement Learning (SDRL)
- **Authors**: Chenxi Liu, Yanshuo Chen, Ruibo Chen et al.
- **Venue**: arXiv 2601.22297 (Jan 2026)
- **核心发现**: 当前 RLVR 训练 LLM 独立解题，未训练其从不同 rationale 中学习。SDRL 联合优化 initial response 和 debate-conditioned response，使单一模型同时成为好的 solver 和好的 debate participant。
- **与我们的关系**: SDRL 的关键 insight 是：模型需要被显式训练以利用 diverse reasoning trajectories。这暗示 SICA 的 independence bottleneck 部分源于模型本身未被训练去生成独立约束。

---

## 3. Contrastive Reasoning & Independent Constraint Generation

### 3.1 Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning
- **Authors**: (2026)
- **Venue**: arXiv 2602.18232 (Feb 2026)
- **核心发现**: Reasoning uncertainty 高度局部化——少量 low-confidence tokens 贡献了大部分 reasoning errors。通过在 low-confidence 位置构造 contrastive reference（high-confidence tokens 用 placeholder 替换）并减去其分布，选择性干预解码过程。
- **与我们的关系**: 提供了识别 reasoning 中 "薄弱环节" 的方法。SICA 可以借鉴：对 trace 中 low-confidence 区域施加更强的约束验证，或者利用 confidence 差异来评估约束的独立性。

### 3.2 Distillation Contrastive Decoding: Improving LLMs Reasoning with Contrastive Decoding and Distillation
- **Authors**: Phuc Phan, Hieu Tran, Long Phan
- **Venue**: arXiv 2402.14874 (Feb 2024)
- **核心发现**: 标准 Contrastive Decoding 需要 expert + amateur 两个模型。DCD 用 Contrastive CoT Prompting + Distillation（Dropout/Quantization）在单模型内构造对比信号，消除了对 amateur model 的需求，减少内存开销。
- **与我们的关系**: DCD 展示了在单模型内生成 contrastive signal 的可能性。这对 SICA 有启发：可以通过 perturbed/degraded 版本的 trace 来生成与原始 trace 相对独立的约束。

### 3.3 CRANE: Reasoning with Constrained LLM Generation
- **Authors**: (2025)
- **Venue**: arXiv 2502.09061 (Feb 2025)
- **核心发现**: 严格的语法约束会降低 LLM reasoning 能力（有理论解释）。但通过 carefully designed additional rules augmenting output grammar，可以同时保持 reasoning 能力和语法正确性。CRANE 在 accuracy 上比 unconstrained decoding 高达 +10%。
- **与我们的关系**: 直接相关——CRANE 证明了 constraints 和 reasoning 之间存在 tension，但可以通过精心设计来调和。这对 SICA 的约束设计有指导意义：约束不应过于 restrictive 以免损害 reasoning diversity。

### 3.4 Scientific Knowledge-driven Decoding Constraints (SciDC)
- **Authors**: (2026)
- **Venue**: arXiv 2604.06603 (Apr 2026)
- **核心发现**: 将领域知识（工业配方、临床诊断、逆合成）转化为多层标准化规则作为 decoding constraints，平均 accuracy +12%。证明了来自外部知识的约束比模型自身的 "implicit knowledge" 更可靠。
- **与我们的关系**: SciDC 的核心思路——将外部独立知识源转化为 decoding constraints——与 SICA 打破 independence bottleneck 的方向一致：从模型外部引入独立于 reasoning trace 的约束来源。

---

## 4. Test-Time Compute Scaling & Process Reward Models

### 4.1 Mode-Conditioning Unlocks Superior Test-Time Scaling
- **Authors**: Chen Henry Wu et al.
- **Venue**: arXiv 2512.01127 (Dec 2025)
- **核心发现**: Parallel sampling 的效果受限于 diversity collapse——finetuning 和 RL 会导致 generations 集中到少数 dominant modes。Mode-Conditioning (ModC) 通过 specialist models 或 mode-specific prefixes 显式分配 compute 到不同 reasoning modes，实现 4x efficiency gain。
- **与我们的关系**: Diversity collapse 是 SICA independence bottleneck 的 test-time scaling 视角表述。ModC 的 mode-conditioning 策略可以直接用于 SICA：为不同 trace 指定不同的 reasoning mode，从而生成更独立的约束。

### 4.2 GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning
- **Authors**: Jian Zhao, Runze Liu et al.
- **Venue**: AAAI 2026 (arXiv 2504.00891)
- **核心发现**: 现有 PRM 是 discriminative scoring，能力有限且泛化差。GenPRM 将 process supervision 重新定义为 generative task（CoT + code verification → judgment），解决了 PRM 不能 scale test-time compute 的问题。
- **与我们的关系**: GenPRM 的 generative verification 思路与 SICA 的 symbolic constraint verification 互补。PRM 评估 reasoning step 质量，SICA 评估约束一致性——两者可以融合为更强的 verification framework。

### 4.3 Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning (ADAPT)
- **Authors**: Ho-Lam Chung et al.
- **Venue**: arXiv 2506.04611 (Jun 2025)
- **核心发现**: 综述 TTS 方法（sampling-based / search-based / trajectory optimization）。关键观察：reasoning-optimized models 产生 less diverse outputs，限制 TTS 效果。提出 ADAPT（Diversity Aware Prefix fine-Tuning），用 8x less compute 达到 80% accuracy。
- **与我们的关系**: 直接证据：reasoning 优化（如 RLHF/RLVF）损害了 output diversity。这解释了为什么 SICA 在强 reasoning model 上反而可能遇到更严重的 independence bottleneck。ADAPT 的 prefix tuning 是潜在的 lightweight fix。

### 4.4 Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling
- **Authors**: Runze Liu et al.
- **Venue**: arXiv 2502.06703 (Feb 2025), ICLR 2025
- **核心发现**: Compute-optimal TTS 策略高度依赖 policy model、PRM 和问题难度的组合。在正确的 TTS 策略下，1B 模型可以超越 405B 模型（MATH-500），0.5B 超越 GPT-4o。
- **与我们的关系**: 证明了 test-time compute allocation 的巨大潜力。但 diversity 是前提——如果 samples 不独立，增加 compute 的边际收益递减。这为 SICA 的 independence bottleneck 提供了经济学视角：打破 bottleneck = 提高 test-time compute 的 ROI。

---

## 5. LLM Self-Correction Limitations

### 5.1 Large Language Models Cannot Self-Correct Reasoning Yet
- **Authors**: Jie Huang, Xinyun Chen et al.
- **Venue**: ICLR 2024
- **核心发现**: LLM 在没有 external feedback 的情况下无法可靠地 self-correct reasoning。Self-correction 有时会把正确答案翻转为错误答案。Intrinsic self-correction（仅用模型自身反馈）系统性失败。
- **与我们的关系**: 奠基性工作。Self-correction 失败的根因与 independence bottleneck 相同：模型用自身的（有偏的）知识去验证自身的（有偏的）输出，缺乏独立的 verification 信号。SICA 的 symbolic constraints 正是试图提供这种独立信号。

### 5.2 When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs
- **Authors**: Ryo Kamoi et al.
- **Venue**: TACL 2024
- **核心发现**: (1) 没有工作成功展示了仅用 prompted LLM 反馈的 self-correction（除特殊适合任务外）；(2) Self-correction 在有 reliable external feedback 时有效；(3) Large-scale fine-tuning 可以 enable self-correction。许多研究存在不公平评估。
- **与我们的关系**: 综述性确认：self-correction 需要 external feedback。这支持 SICA 的方法论——symbolic invariant checking 提供了一种 external（或至少 structurally independent）的 feedback 机制。但 independence bottleneck 意味着如果 constraints 也来自同一模型，这个 "external" 信号并不真正独立。

### 5.3 Large Language Models Can Self-Correct with Key Condition Verification (ProCo)
- **Authors**: Zhenyu Wu, Qingkai Zeng, Zhihan Zhang, Zhaoxuan Tan, Chao Shen, Meng Jiang
- **Venue**: EMNLP 2024 (Main)
- **核心发现**: 提出 verify-then-correct 框架：mask 问题中的 key condition，将当前 response 加入构造 verification question，预测被 mask 的 condition 来验证 response。GPT-3.5-Turbo 在 QA 上 +6.8 EM，arithmetic +14.1 accuracy。
- **与我们的关系**: ProCo 的 key condition masking 是一种巧妙的 "伪独立" 验证——通过信息隐藏创造条件上的独立性。这个思路可以直接应用到 SICA：通过部分信息隐藏来生成与原始 trace 条件独立的约束。

### 5.4 Training Language Models to Self-Correct via Reinforcement Learning (SCoRe)
- **Authors**: (Google DeepMind)
- **Venue**: ICLR 2025 (Oral)
- **核心发现**: SFT 和标准 RL 的 self-correction 失败源于 distribution shift（训练纠正 base model 错误但无法纠正自身错误）和 behavior collapse（第二轮仅做表面修改）。SCoRe 在模型自身分布下训练 + 正则化，MATH +15.6%, HumanEval +9.1%。
- **与我们的关系**: Distribution shift 和 behavior collapse 是 independence bottleneck 在 self-correction 中的具体表现。SCoRe 通过在模型自身分布上训练来缓解——这暗示 SICA 也需要考虑约束生成器的分布特性。

### 5.5 Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis
- **Authors**: (2026)
- **Venue**: arXiv 2601.00828 (Jan 2026)
- **核心发现**: Accuracy-Correction Paradox：弱模型（GPT-3.5, 66% accuracy）的 intrinsic correction rate 是强模型（DeepSeek, 94% accuracy）的 1.6x（26.8% vs 16.7%）。将 self-correction 分解为三个子能力：error detection、error localization、error correction。
- **与我们的关系**: Accuracy-Correction Paradox 对 SICA 有直接启示：强模型的约束可能更准确但更同质（independence bottleneck 更严重），弱模型的约束可能更 diverse 但噪声更大。这指向一个 sweet spot：使用 moderately capable 模型或异构模型组合来平衡 accuracy 和 independence。

---

## 跨主题综合分析

### Independence Bottleneck 的多视角确认

| 视角 | 关键论文 | 核心证据 |
|------|---------|---------|
| Data-level | Verbalized Sampling | Typicality bias → mode collapse |
| Training-level | ADAPT, ModC | RL/RLHF → diversity collapse |
| Sampling-level | Expanding Search Space | 单一 prompting → 搜索空间重叠 |
| Debate-level | DReaMAD, DMAD | Homogenized dynamics, mental set |
| Self-correction-level | Huang et al., Kamoi et al. | 无外部反馈 → 系统性失败 |
| Theoretical | ALIGN | 显式 relax independence assumption |

### 潜在突破方向（基于文献）

1. **Multi-mode constraint generation**: ModC + Expanding Search Space 的思路——为不同 trace 指定不同 reasoning mode
2. **Information-hiding verification**: ProCo 的 key condition masking——通过信息隐藏创造条件独立性
3. **Cross-model heterogeneity**: Can LLM Agents Really Debate? 的 evidence——异构模型是 diversity 的主要驱动力
4. **External knowledge constraints**: SciDC 的思路——从外部知识源引入独立约束
5. **Diversity-aware training**: SDRL + SCoRe 的思路——显式训练模型生成 diverse/independent 约束
