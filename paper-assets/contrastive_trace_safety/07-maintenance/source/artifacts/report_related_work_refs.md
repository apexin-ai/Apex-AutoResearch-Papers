# Related Work References (43 papers)

## A) Hidden-State Safety Detection (9篇)

- **Representation Engineering: A Top-Down Approach to AI Transparency** (Zou et al., 2023, arXiv 2310.01405)
  关系: 奠基性工作，提出从表示空间读取/控制高层概念（honesty, harmlessness等），本文的 hidden-state probing 方法直接继承此范式

- **SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals** (Anonymous, 2025, EMNLP Findings)
  关系: 用 safety prober 监控内部状态，检测到不安全内容时激活 refusal head，与本文的 HS probe 检测机制最直接相关

- **SIREN: LLM Safety From Within — Detecting Harmful Content with Internal Representations** (Anonymous, 2025, arXiv 2604.18519)
  关系: 通过 linear probing 定位 safety neurons 并用 layer-weighted 策略聚合，与本文 layer 选择和 probe 设计直接对标

- **How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States** (Zhou et al., 2024, EMNLP Findings)
  关系: 用弱分类器分析中间隐状态，发现 LLM 在早期层就能识别恶意输入，支持本文在特定层做 probing 的设计选择

- **Obfuscated Activations Bypass LLM Latent-Space Defenses** (Bailey et al., 2024, arXiv 2412.09565)
  关系: 展示 latent-space 防御（包括 probes）可被对抗性攻击绕过，本文需讨论 robustness limitation

- **Improving Alignment and Robustness with Circuit Breakers** (Zou et al., 2024, arXiv 2406.04313)
  关系: Representation Rerouting 将有害表示重路由到正交空间，是 hidden-state 层面安全干预的代表方法

- **Representation Bending for Large Language Model Safety** (Yousefpour et al., 2025, ACL)
  关系: RepBend 通过弯曲有害表示方向实现安全对齐，与本文检测有害表示的方向互补

- **Towards Understanding Safety Alignment: A Mechanistic Perspective from Safety Neurons** (Anonymous, 2024, arXiv 2406.14144)
  关系: 通过 activation contrasting 定位 safety neurons（约5%参数），patch 这些神经元可恢复90%安全性能，支持本文 probing 特定层的合理性

- **Understanding and Enhancing Safety Mechanisms of LLMs via Safety-Specific Neuron** (Anonymous, 2025, ICLR)
  关系: 发现 safety neurons 不到1%参数且集中在前几层 self-attention，为本文的层选择策略提供理论依据

## B) Reasoning Model Safety (8篇)

- **When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models** (Anonymous, 2025, arXiv 2510.21285)
  关系: 定义 Self-Jailbreak 现象并提出 Chain-of-Guardrails (CoG) 缓解方案，本文的检测方法正是为此现象设计

- **Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training** (Anonymous, 2025, arXiv 2510.20956)
  关系: 发现 benign reasoning training 后模型会自我越狱，无需对抗性 prompt，直接构成本文的问题动机

- **H-CoT: Hijacking the Chain-of-Thought Safety Reasoning Mechanism to Jailbreak Large Reasoning Models** (Anonymous, 2025, arXiv 2502.12893)
  关系: 通过劫持 CoT 安全推理路径实现越狱（拒绝率从98%降至2%），本文的检测方法可作为对此攻击的防御

- **The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1** (Anonymous, 2025, arXiv 2502.12659)
  关系: 系统评估 DeepSeek-R1 安全风险，100% attack success rate on HarmBench，证明 reasoning model 安全问题的严重性

- **Large Reasoning Models Are Autonomous Jailbreak Agents** (Hagendorff et al., 2026, Nature Communications)
  关系: LRM 可自主规划多轮攻击绕过其他模型安全机制（97%成功率），展示 reasoning 能力被滥用的风险

- **SafeChain: Safety of Language Models with Long Chain-of-Thought Reasoning Capabilities** (Anonymous, 2025, ACL Findings)
  关系: 首个 CoT 风格安全训练数据集，评估13个LRM的安全性，提出 ZeroThink/LessThink/MoreThink 解码策略

- **Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety** (Anonymous, 2025, arXiv 2507.11473)
  关系: 论证 CoT 监控作为安全机制的机遇与脆弱性，本文的 hidden-state 方法可作为 text-based CoT 监控的互补

- **When Safety Fails Before the Answer: Benchmarking Harmful Behavior Detection in Reasoning Chains (HarmThoughts)** (Anonymous, 2025, arXiv 2604.19001)
  关系: 提供 1018 条越狱推理 trace 的 16 类句子级标注，可作为本文的评估数据来源

## C) Change-Point Detection (6篇)

- **Bayesian Online Changepoint Detection** (Adams & MacKay, 2007, arXiv 0710.3742)
  关系: BOCPD 经典算法，计算当前 run length 的后验分布，本文的 temporal probing 中 window 划分思想受此启发

- **Neural Network-Based CUSUM for Online Change-Point Detection** (Gong & Lee, 2023, arXiv 2210.17312)
  关系: 将 CUSUM 与神经网络结合实现在线变点检测，本文的 windowed feature 方法与此思路类似

- **Automatic Change-Point Detection in Time Series via Deep Learning** (Li et al., 2024, JRSSB)
  关系: 用 CNN 学习多种变点类型特征，类比本文用 temporal window 捕捉 safety commitment 变化点

- **Unsupervised Concept Drift Detection Based on Parallel Activations of Neural Network** (Anonymous, 2024, arXiv 2404.07776)
  关系: 直接利用神经网络激活值检测分布漂移，与本文监控 hidden state 随 token 位置变化的方法直接对应

- **Novelty-Aware Concept Drift Detection for Neural Networks** (Anonymous, 2024, Neurocomputing)
  关系: 在 hidden layer 特征上检测概念漂移，方法论上与本文的 temporal probing 跨 token 位置检测安全状态变化一致

- **Bayesian Online Prediction of Change Points** (Agudelo-Espana et al., 2020, AISTATS)
  关系: 扩展 BOCPD 到预测模式和 AR 依赖，为本文的 online safety monitoring 场景提供理论工具

## D) Probe Methodology (7篇)

- **Understanding Intermediate Layers Using Linear Classifier Probes** (Alain & Bengio, 2017, ICLR Workshop)
  关系: 开创性工作，提出用 linear probe 理解网络中间层表示，本文的 probing 方法论直接源于此

- **Designing and Interpreting Probes with Control Tasks** (Hewitt & Liang, 2019, EMNLP)
  关系: 提出 selectivity 指标和 control task 方法论，本文评估 probe 质量时需参考此框架

- **Probing Classifiers: Promises, Shortcomings, and Advances** (Belinkov, 2022, Computational Linguistics)
  关系: Probing 方法论综述，系统讨论 probe 的 expressiveness vs memorization 权衡，为本文方法论提供理论背景

- **Measuring Faithfulness in Chain-of-Thought Reasoning** (Lanham et al., 2023, Anthropic)
  关系: 发现 CoT 忠实度随模型变大而下降，为本文"text probe 不可靠，需要 HS probe"的论点提供动机

- **Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting** (Turpin et al., 2023, NeurIPS)
  关系: 证明 CoT 可系统性地不忠实于模型真实推理，直接支撑本文核心论点：需要 hidden state 而非 text 来检测安全承诺

- **Reasoning Models Don't Always Say What They Think** (Chen et al., 2025, Anthropic)
  关系: 发现 reasoning model 的 CoT faithfulness 低至 25-39%，直接论证 text-based 监控的局限性和 hidden-state 方法的必要性

- **Monitoring Latent World States in Language Models with Propositional Probes** (Anonymous, 2024, OpenReview)
  关系: 用命题级 probe 监控 LM 的隐式世界状态，方法论上与本文监控 safety commitment 状态类似

## E) Reasoning Models General (6篇)

- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek-AI, 2025, arXiv 2501.12948)
  关系: DeepSeek-R1 技术报告，本文实验的主要目标模型之一（DeepSeek-R1-Distill-Qwen-8B）

- **QwQ-32B: Embracing the Power of Reinforcement Learning** (Qwen Team, 2025)
  关系: QwQ 技术报告，32B 参数通过 RL 达到 R1 级推理能力，本文讨论的 reasoning model 家族之一

- **OpenAI o1 System Card** (OpenAI, 2024, arXiv 2412.16720)
  关系: o1 安全评估，展示 deliberative alignment 的安全性能，作为 reasoning model 安全的参考基线

- **Deliberative Alignment: Reasoning Enables Safer Language Models** (Guan et al., 2024, arXiv 2412.16339)
  关系: 提出让模型在 CoT 中显式引用安全策略的对齐方法，与本文检测安全承诺变化的目标互补

- **Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Parameters** (Snell et al., 2024, ICLR 2025)
  关系: Test-time compute scaling 的理论基础，解释为何 reasoning model 产生长 CoT trace

- **Marco-o1: Towards Open Large Reasoning Models for Real-World Solutions** (AIDC-AI, 2024)
  关系: 用 MCTS 扩展推理路径的开源 reasoning model，展示 reasoning model 的多样性

## F) Jailbreak Attacks & Defenses (8篇)

- **Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG)** (Zou et al., 2023, arXiv 2307.15043)
  关系: 提出 Greedy Coordinate Gradient 优化对抗性后缀，经典 token-level 攻击方法，本文实验中的攻击类型参考

- **AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models** (Liu et al., 2024, ICLR)
  关系: 用遗传算法生成语义连贯的越狱 prompt，比 GCG 更隐蔽，代表 semantic-level 攻击

- **AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs** (Liu et al., 2025, ICLR Spotlight)
  关系: 自动发现和组合越狱策略的 lifelong agent，展示攻击方法的持续进化

- **Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)** (Chao et al., 2024, arXiv 2310.08419)
  关系: 用 attacker LLM 迭代生成 prompt-level 越狱，代表 black-box multi-turn 攻击

- **Improving Alignment and Robustness with Circuit Breakers** (Zou et al., 2024, arXiv 2406.04313)
  关系: Representation rerouting 防御，将有害表示重路由到正交空间，hidden-state 层面的防御代表

- **PARDEN, Can You Repeat That? Defending against Jailbreaks via Repetition** (Anonymous, 2024, OpenReview)
  关系: 通过让模型重复自身输出检测越狱，text-based 防御方法，与本文 HS-based 方法对比

- **X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents** (Anonymous, 2025)
  关系: Multi-turn 自适应越狱框架，展示多轮交互场景下的攻防博弈

- **Towards Understanding Jailbreak Attacks in LLMs** (Anonymous, 2024, EMNLP)
  关系: 系统性分析越狱攻击的机制分类，为本文讨论不同攻击类型下检测效果提供参考框架

---

## 总计: 44 篇（去重后约 42 篇，Circuit Breakers 和 Deliberative Alignment 在 A/E/F 中重复出现）

按主题分布:
- A) Hidden-state safety detection: 9篇
- B) Reasoning model safety: 8篇
- C) Change-point detection: 6篇
- D) Probe methodology: 7篇
- E) Reasoning models general: 6篇
- F) Jailbreak attacks & defenses: 8篇
