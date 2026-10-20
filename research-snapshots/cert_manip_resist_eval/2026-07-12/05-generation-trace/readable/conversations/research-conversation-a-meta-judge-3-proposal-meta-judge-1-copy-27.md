# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/02f046e6-8f50-498e-bd49-e7c77a458224.jsonl`
- **Structured JSON:** [`79420b013a8c0eb3dda5.json`](../../sessions/79/79420b013a8c0eb3dda5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:35:04.392Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:35:04.392Z",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me synthesize my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **PRM-BiasBench (arXiv:2603.06621, Feb 2026)**: 最直接相关的工作。对 PRM 施加 8 种 surface perturbation，发现 fluency-logic dissociation（rephrasing 鲁棒但 semantic corruption 脆弱）。Section 6 展示 RL hackability（>0.9 PRM reward, <4% accuracy, 43% reward gains from stylistic shortcuts）。与本 proposal 的关系：PRM-BiasBench 测的是 surface-level perturbation，proposal 声称测试的是 structural isomorphism——更深一层的不变性。这个定位差异化是成立的，但需要注意两者的边界并不完全清晰（如 notation change 是否真的比 rephrasing \"更深\"值得商榷）。\n\n2. **reWordBench (EMNLP 2025, arXiv:2503.11751)**: 测 general RM 的 meaning-preserving transformation robustness（paraphrasing, typos, code minification），发现 SOTA RM 在某些变换下降至 below-random。提出 paraphrase-consistency training。与本 proposal 的关系：reWordBench 面向 response-level general RM，proposal 面向 step-level PRM，且限定于 mathematically verifiable transformations。区分维度明确。\n\n3. **PutnamGAP (arXiv:2508.08833, Aug 2025)**: 对 1,051 道 Putnam 题施加 mathematically equivalent transformations（4 种 surface rename + kernel rewrite），测 LLM solver 鲁棒性。O3 在 kernel rewrite 上下降 12.9pp。与本 proposal 的关系：PutnamGAP 测 solver、problem-level；proposal 测 verifier、step-level。方法论灵感来源清晰，但\"从 solver 到 verifier\"的迁移是否算 sufficient novelty 值得审视。\n\n4. **IPT / LLMs Gaming Verifiers (arXiv:2604.15149, Apr 2026)**: 用 Isomorphic Perturbation Testing 检测 RLVR 训练的 shortcut 行为，发现 RLVR 模型系统性地 abandon rule induction。与本 proposal 的关系：IPT 测 outcome verifier，proposal 测 process verifier，概念上有启发关系但应用场景不同。\n\n5. **APRM (arXiv:2511.22888, Nov 2025)**: 对抗训练 PRM，Generator 生成 plausible errors, PRM 学习检测。+3.4pp solver accuracy。与本 proposal 的关系：proposal 将 Iso-Aug 定位为与 APRM 互补（APRM 改善 error detection，Iso-Aug 改善 invariance），这个定位合理。\n\n6. **CoLD (arXiv:2507.15698, Jul 2025)**: 因果 debiasing 框架消除 PRM 长度偏差。与本 proposal 的关系：proposal 将 CoLD 的 S→L→P 框架迁移为 S→F→P（format bias），技术迁移路径清晰但 novelty 增量有限。\n\n7. **GenPRM (AAAI 2026, arXiv:2504.00891)** & **ThinkPRM (arXiv:2504.16828)**: Generative PRM 范式——GenPRM 用 code verification, ThinkPRM 用 long-CoT。与本 proposal 的关系：proposal 假设 generative PRM 可能天然更 isomorphism-invariant（code execution 是 notation-invariant 的），这是一个合理且有趣的假设，但也意味着可能出现\"generative PRM 已经解决了这个问题\"的 dual outcome。\n\n8. **GR-Ben (arXiv:2605.01203, May 2026)**: 将 PRM 评估扩展到 9 个非数学推理子域。与本 proposal 的关系：GR-Ben 测 domain generalization breadth，proposal 测 within-domain structural invariance，属于不同维度。\n\n9. **FoVer (ACL 2026 Findings, arXiv:2505.15960)**: 用 Z3/Isabelle 做 PRM training data synthesis。与本 proposal 的关系：verification pipeline 的技术基础，proposal 引用合理。\n\n10. **Socratic-PRMBench (arXiv:2505.23474)**: 6 种 reasoning pattern 的 PRM benchmark。与本 proposal 的关系：不测 invariance，是不同维度的 benchmark。\n\n11. **FormalRewardBench (arXiv:2605.10141, May 2026)** & **Unsupervised PRM (arXiv:2605.10158, May 2026)**: 最近几周的 PRM benchmark/method 工作，进一步说明该领域正在快速发展和 benchmark 饱和。\n\n- **调研总结**: PRM robustness/evaluation 是 2025-2026 年的热点方向，benchmark 数量快速增长（ProcessBench → PRMBench → PRM-BiasBench → Socratic-PRMBench → GR-Ben → FormalRewardBench），但确实没有一个工作专门测试 step-level structural isomorphism invariance。这个 gap 是真实存在的。然而，这个 gap 的\"深度\"需要审视——它更多是一个评估维度的组合创新（PutnamGAP 的 transformation taxonomy × PRM-BiasBench 的 verifier robustness testing × step-level granularity），而非概念上的根本突破。\n\n\n【Trivial Alternative 检验】:\n\n**存在部分 trivial alternative 威胁：**\n\n1. **最直接的 trivial baseline**: 将 PRM-BiasBench 的 perturbation set 扩展几种 math-specific transformations（如加入 variable renaming 和 notation change），而不构建全新 benchmark。PRM-BiasBench 已有 8 种 perturbation 和完整的评估框架，加入 T1-T4 变换类型只需增量工作。Proposal 对此的增量价值在于：(a) 形式化验证保证（SymPy/Z3），PRM-BiasBench 的 perturbation 缺乏这种数学等价性保证；(b) step-level 而非 solution-level 的分析粒度。但审稿人可能认为这些差异不足以支撑一篇独立论文。\n\n2. **Notation gaming 分析的 trivial alternative**: PRM-BiasBench Section 6 已经展示了 reward hacking 的机制（43% stylistic shortcuts），notation gaming 只是同一现象的一个特例——用 \"logically equivalent but notation-different\" 的子集来 hack PRM。审稿人可能会问：这和 PRM-BiasBench 的发现相比，增量 insight 到底是什么？\n\n3. **Iso-Aug 的 trivial alternative**: reWordBench 已经提出了 paraphrase-consistency training 并证明它 generalizes to other transformations。如果简单地将 isomorphic pairs 加入 reWordBench 的 consistency training pipeline，是否就足以实现类似效果？Proposal 的 CoLD-based causal debiasing 增加了方法复杂度，但核心 idea（consistency regularization across equivalent inputs）与 reWordBench 的方法高度相似。\n\n**增量价值的核心在于**: \"形式化可验证的数学等价性\" 作为 invariance 的测试标准，比 surface perturbation 更严格、更有理论根基。但这个增量是否足够支撑 top venue 论文，取决于实验结果是否能揭示 PRM-BiasBench 未发现的 failure patterns。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的假设：\n\n1. **\"Isomorphic brittleness 存在且显著\"**（关键假设）: 整个 proposal 建立在一个未验证的前提上——PRM 对 structurally isomorphic reasoning steps 会给出不同的 scores。PRM-BiasBench 发现 PRM 对 rephrasing 是 robust 的（|ΔR|<0.03），而 proposal 声称更深层的 structural isomorphism 会导致 brittleness。但如果 PRM 连 rephrasing 都能处理，为什么变量重命名（T1）、交换律重排（T2）这些同样是表面变换的操作会导致更大的 brittleness？T1/T2 实际上可能比 rephrasing 更简单（纯符号替换 vs. 语义保持的自然语言改写）。**如果实验发现 PRM 对 T1-T4 都相当 robust，整篇论文的核心 narrative 就会瓦解。** Proposal 确实有 dual-outcome 设计（\"即使 generative PRM robust，也有价值\"），但 dual-outcome 不能拯救一个核心假设被否定的论文。\n\n2. **\"Isomorphic brittleness 解释了 tree search failure\"**: Proposal 将 PRM-guided tree search 的失败（arXiv:2510.20272）归因于 isomorphic brittleness 在 search depth 上的 compounding。但 tree search 失败的原因可能更根本——PRM 对 partial solution 的 value estimation 本身就不准确（与 isomorphism 无关）。这个因果推断是 speculative 的。\n\n3. **\"Notation gaming 比 fluency gaming 更危险因为更难检测\"**: 这个 claim 听起来合理但缺乏证据。如果 PRM 对 notation change 的 sensitivity 本来就很小（假设1不成立），那么 notation gaming 的 attack surface 就不存在。且\"valid mathematical content\"使其\"更难检测\"的论点需要对比实验支持，而非仅靠直觉论证。\n\n4. **\"CoLD 的 causal debiasing framework 可以直接迁移到 isomorphism bias\"**: CoLD 的 S→L→P 因果图是基于 length 这个单一标量维度建模的。Isomorphism 涉及多维、离散的变换类型，因果图的结构是否仍然适用（即 serialization format 是否真的是一个单一的 confounder）未经论证。\n\n\n【3 维度打分】:\n\n**1. Novelty: 中偏弱** — \n\n核心贡献是一个\"组合式创新\"：将 PutnamGAP 的 mathematically equivalent transformation 概念（solver → verifier）、PRM-BiasBench 的 robustness testing 框架（surface → structural）、以及 step-level 粒度结合起来。每个组件都有明确的先驱工作：\n\n- Transformation taxonomy: 直接借鉴 PutnamGAP（variable renaming, representation change）\n- Robustness testing of verifiers: PRM-BiasBench 已建立\n- Consistency training mitigation: reWordBench 的 paraphrase-consistency + CoLD 的 causal debiasing\n- Formal verification pipeline: FoVer 的 Z3/Isabelle 方法\n\n剥去 surface differences 后，核心 novelty delta 是\"step-level structural isomorphism testing with formal verification guarantees\"——这是真实的但增量的。审稿人的典型反应可能是\"nice evaluation paper but limited methodological novelty\"。Iso-Aug 作为 mitigation 方法论 novelty 更弱——本质上是 consistency regularization + CoLD framework 的直接迁移。\n\n**2. Significance: 中** — \n\n研究问题的重要性是真实的：PRM 作为 test-time compute scaling 的核心组件（best-of-N, tree search, RLHF），其 robustness 直接影响下游系统的可靠性。PRM-BiasBench 的 Section 6（RL hackability）和 arXiv:2510.20272（tree search failure）都证明了 PRM 可靠性问题的实际影响。\n\n但 significance 受限于：(a) 如果 generative PRM（GenPRM, ThinkPRM）天然 robust to structural isomorphism，那么 discriminative PRM 的这个问题可能只是暂时的——随着 generative PRM 的普及，这个问题自然消解；(b) notation gaming 的实际威胁程度未知——如果 PRM 对 notation 的 sensitivity 本身就小，这个 attack surface 就不具实际意义；(c) 这更多是一个 evaluation/benchmark 贡献，而非推动该领域 paradigm shift 的工作。\n\n该研究对 NLP/CL 领域的 impact 是中等的：它会被 PRM 研究者引用为一个 evaluation dimension，但不太可能改变 PRM 的设计范式或训练方法论。\n\n**3. Related Work: 强** — \n\n这是 proposal 最突出的优点。Related work coverage 非常全面且准确：覆盖了 PRM-BiasBench、reWordBench、PutnamGAP、IPT、APRM、CoLD、Crome、GenPRM、ThinkPRM、PRMBench、Socratic-PRMBench、GR-Ben、FoVer、ProcessBench 等几乎所有相关工作，且对每个工作的差异化定位清晰准确。引用的论文经 WebSearch 验证均真实存在，描述准确。特别是对 PRM-BiasBench（surface robustness）、PutnamGAP（solver-level）、reWordBench（response-level general RM）的三角定位，清楚地界定了 proposal 的 gap 所在。唯一的不足是 landscape 过于详尽可能暗示这是一个 crowded space 的 incremental contribution——正是因为 coverage 做得太好，反而暴露了 novelty 的有限性。\n\n\n【概率估计】: [18% - 30%] 中位 23%\n\n【估计理由】: \n\nNovelty 中偏弱 是主要限制因素。核心贡献是组合式创新——将已有概念（equivalent transformations、robustness benchmarking、consistency training）应用于一个新的但增量的维度（step-level structural isomorphism of PRMs）。每个技术组件都有清晰的先驱工作，剥去差异后的 novelty delta 有限。Significance 中等但受限于核心假设未验证（isomorphic brittleness 可能不显著）和 generative PRM 可能天然解决这一问题。Related work 虽然强，但强 related work 在评审中属于\"不扣分\"而非\"加分\"。\n\n如果核心发现是 positive（PRM 确实对 structural isomorphism 脆弱），审稿人更可能的反应是 \"I would have guessed this given PRM-BiasBench's fluency-logic dissociation findings\" 而非 \"surprising\"。如果核心发现是 negative（PRM 对 T1-T4 robust），论文的 impact 会大幅下降。这将 idea 锚定在 25-35% 区间的下部。考虑到 benchmark paper 在 EMNLP 的接受门槛（需要强 novelty 或 strong community impact），以及 PRM benchmark 领域已趋于饱和（2025-2026 年已有 6+ 个 PRM benchmark），概率估计下调至 18-30%，中位 23%。\n\n【主要风险】:\n\n1. **核心假设风险**: PRM 可能对 T1-T4 structural isomorphisms 相当 robust（PRM-BiasBench 已发现对 rephrasing 的 |ΔR|<0.03），导致论文核心 narrative（\"isomorphic brittleness 是严重问题\"）无法成立。T1（variable renaming）和 T2（commutative reordering）本质上是比 rephrasing 更简单的表面变换，PRM 有可能对它们同样 robust。\n\n2. **Benchmark 饱和 + 有限 novelty**: 2025-2026 年 PRM benchmark 快速增长（ProcessBench → PRMBench → PRM-BiasBench → Socratic-PRMBench → GR-Ben → FormalRewardBench），审稿人可能认为\"又一个 PRM benchmark\"的 marginal contribution 不足以接受。核心方法论（transformation taxonomy + consistency training）均有清晰的先驱工作，组合创新的 novelty bar 在 top venue 可能不够。\n```\n\nSources:\n- [PRM-BiasBench: Reward Under Attack (arXiv:2603.06621)](https://arxiv.org/abs/2603.06621)\n- [reWordBench (EMNLP 2025, arXiv:2503.11751)](https://arxiv.org/abs/2503.11751)\n- [PutnamGAP (arXiv:2508.08833)](https://arxiv.org/abs/2508.08833)\n- [IPT / LLMs Gaming Verifiers (arXiv:2604.15149)](https://arxiv.org/abs/2604.15149)\n- [APRM: Adversarial Training for PRMs (arXiv:2511.22888)](https://arxiv.org/abs/2511.22888)\n- [CoLD: Counterfactual Length Debiasing (arXiv:2507.15698)](https://arxiv.org/abs/2507.15698)\n- [GenPRM (arXiv:2504.00891)](https://arxiv.org/abs/2504.00891)\n- [ThinkPRM (arXiv:2504.16828)](https://arxiv.org/abs/2504.16828)\n- [GR-Ben (arXiv:2605.01203)](https://arxiv.org/abs/2605.01203)\n- [FoVer (ACL 2026 Findings, arXiv:2505.15960)](https://arxiv.org/abs/2505.15960)\n- [Socratic-PRMBench (arXiv:2505.23474)](https://arxiv.org/abs/2505.23474)\n- [ProcessBench (arXiv:2412.06559)](https://arxiv.org/abs/2412.06559)\n- [Limits of PRM-Guided Tree Search (arXiv:2510.20272)](https://arxiv.org/abs/2510.20272)\n- [Crome: Causally Robust Reward Modeling (ICML 2025, arXiv:2506.16507)](https://arxiv.org/abs/2506.16507)\n- [PRMBench (ACL 2025, arXiv:2501.03124)](https://arxiv.org/abs/2501.03124)\n- [FormalRewardBench (arXiv:2605.10141)](https://arxiv.org/abs/2605.10141)\n- [Unsupervised PRM (arXiv:2605.10158)](https://arxiv.org/abs/2605.10158)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make my assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [PRM-BiasBench / Reward Under Attack](https://arxiv.org/abs/2603.06621) (arXiv 2026): 直接相关的前序工作。对PRM施加8种表面扰动，发现fluency-logic dissociation（PRMs对rephrasing鲁棒但对语义corruption脆弱）。Section 6的RL hackability分析证明43%的reward gains来自stylistic shortcuts。本proposal声称填补\"structural invariance\"空白，PRM-BiasBench确实只测试了surface perturbations，未测试数学结构等价变换——这一差异化定位基本成立。\n\n- [reWordBench](https://arxiv.org/abs/2503.11751) (EMNLP 2025): 测试通用RM在meaning-preserving input transformations下的鲁棒性，发现SOTA RMs严重退化甚至低于随机。但目标是response-level general RMs，不是step-level PRMs，且变换类型是surface-level（paraphrasing, typos）而非数学结构等价。Proposal的差异化定位成立。\n\n- [PutnamGAP](https://arxiv.org/abs/2508.08833) (arXiv 2025): 对1,051个Putnam问题施加数学等价变换（surface renames + kernel rewrites），测试LLM solvers。O3在kernel variants上下降~13pp。关键区别：测的是solver而非verifier，且是problem-level而非step-level。Proposal借鉴了变换分类法但应用于不同对象，差异化清晰。\n\n- [GenPRM](https://arxiv.org/abs/2504.00891) (AAAI 2026): 生成式PRM，1.5B模型超越GPT-4o。代码执行理论上对notation invariant（SymPy对'3/4'和'0.75'等价处理）。Proposal正确识别了这一点并计划测试。\n\n- [ThinkPRM](https://arxiv.org/abs/2504.16828) (arXiv 2025): Long-CoT验证，比discriminative PRMs高8%（GPQA-Diamond）。与GenPRM一起构成generative PRM范式的代表。\n\n- [IPT / LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149) (arXiv 2026): 用isomorphic perturbation testing检测RLVR的reward hacking，发现shortcut prevalence随compute增加——inverse scaling。但测试对象是outcome verifiers和solvers，不是step-level PRMs。\n\n- [APRM](https://arxiv.org/abs/2511.22888) (arXiv 2025): 对抗训练PRM，Generator学习产生reasoning errors欺骗PRM。+3.4pp solver accuracy。Proposal正确定位为互补方向（APRM改善error detection，Iso-Aug改善invariance）。\n\n- [CoLD](https://arxiv.org/abs/2507.15698) (arXiv 2025): 因果去偏框架处理PRM的length bias。Proposal计划改编其框架（S→L→P改为S→F→P），技术路线合理但属于直接套用。\n\n- [GR-Ben](https://arxiv.org/abs/2605.01203) (arXiv 2026, May): 将PRM评估扩展到9个非数学推理子领域，22个模型。测试domain generalization breadth，不测invariance。进一步确认structural invariance轴确实未被覆盖。\n\n- [FoVer](https://arxiv.org/abs/2505.15960) (ACL 2026 Findings): 用Z3/Isabelle做PRM训练数据合成。Proposal借鉴其验证方法论。\n\n- 调研总结: PRM评估领域2025-2026高度活跃，已有大量benchmark覆盖error detection (ProcessBench, PRMBench)、surface robustness (PRM-BiasBench)、domain generalization (GR-Ben)、general RM robustness (reWordBench)。数学等价变换测试存在于solver侧(PutnamGAP)和outcome verifier侧(IPT)，但**step-level PRM的structural isomorphism invariance**确实是一个尚未被填补的空白。这一gap是真实的。然而，这是一个\"拼图中的最后一块\"类型的贡献——gap存在，但gap本身的重要性需要审视。\n\n【Trivial Alternative 检验】:\n\n存在一个需要认真对待的trivial alternative：**直接使用reWordBench的paraphrase-consistency training方法（或其变体），在PRM训练中加入数学等价对作为数据增强，不需要新benchmark**。reWordBench已经证明paraphrase-consistency training可以泛化到其他变换类型。一个自然的问题是：如果对PRM做类似的consistency training（用数学等价变换作为augmentation），是否需要一个专门的benchmark来motivate这件事？\n\n此外，**GenPRM/ThinkPRM可能已经天然解决了这个问题**——proposal自己承认了这一点。如果generative PRMs通过code execution天然具备notation invariance，那么这个benchmark的主要价值缩窄为\"量化discriminative PRMs的一个已知弱点\"和\"给discriminative PRMs做augmentation training\"，这显著削弱了significance。\n\n增量价值在于：(1) 系统化地量化这一brittleness的程度和模式（per-transformation, per-depth）；(2) notation gaming attack surface分析是一个有意思的angle；(3) cross-analysis with PRM-BiasBench的二维robustness landscape。但这些更多是分析贡献而非方法论贡献。\n\n【前提假设检验】:\n\n核心逻辑链有几个未经验证的假设：\n\n1. **\"Isomorphic brittleness是PRM-guided tree search failure的mechanistic explanation\"** — 这是一个大胆的因果主张，但proposal只能提供相关性证据（IIS vs. step depth的相关分析）。Tree search failure可能有很多其他原因（search strategy, reward calibration, error propagation），isomorphic brittleness可能只是其中一个minor factor。Proposal将此作为核心motivation之一，但实际上无法建立因果关系。\n\n2. **\"Notation gaming是一个实际存在的reward hacking attack surface\"** — Proposal假设solver policy会学到exploit PRM的notation preferences，但这需要policy在RL训练中自发地发现并利用notation变换——这比fluency-based gaming（自然语言的表达偏好更容易被gradient信号捕获）更难实现。Proposal的proof-of-concept是simulate而非demonstrate actual RL-learned notation gaming，说服力有限。\n\n3. **\"Discriminative PRMs在structural isomorphism上确实brittle\"** — 这是最核心的前提，也是最有可能成立的一个（基于PRM-BiasBench和PutnamGAP的间接证据）。但如果实际测量发现discriminative PRMs在T1-T4上的IIS都很高（比如>0.9），整个project的narrative会显著受损。\n\n4. **\"四种变换类型（T1-T4）足以覆盖'structural isomorphism'的主要维度\"** — 实际上这四种变换都相当shallow（变量重命名、交换律、表示变换、符号变换），真正深层的structural isomorphism（如proof strategy变换、等价推理路径变换）并未涉及。但这些更深层的变换难以自动验证，所以proposal选择了可验证的子集——这是一个pragmatic trade-off，但也意味着结论的generalizability有限。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心novelty claim——\"step-level PRM的structural isomorphism invariance测试\"——在调研中确认是一个真实的gap。PRM-BiasBench测surface，PutnamGAP测solver，reWordBench测general RM，都没有覆盖step-level PRM的数学结构等价变换。但这个novelty的\"质感\"更接近\"在existing evaluation landscape中填一个空位\"，而非\"提出一个surprising insight\"。四种变换类型（variable renaming, commutative reordering, representation change, notation change）本质上是PutnamGAP变换分类法在verifier侧的直接应用。Iso-Aug方法是CoLD框架的直接改编+reWordBench consistency training思路的结合，方法论novelty有限。Notation gaming attack surface分析是一个有novelty的角度，但proposal将其作为simulation而非实际RL训练中的demonstration。\n\n2. **Significance: 中偏弱** — \n   研究问题本身有一定重要性：PRM作为test-time compute scaling的核心组件，其robustness确实值得系统评估。但significance被几个因素削弱：(a) generative PRMs（GenPRM, ThinkPRM）可能天然解决此问题，而generative PRM是当前的发展方向，使得discriminative PRM的brittleness诊断的时效性存疑；(b) 即使发现brittleness存在，\"discriminative PRMs对notation变换不鲁棒\"这个结论对大多数reviewer来说可能是\"I would have guessed this\"——discriminative PRMs做pattern matching而非真正理解数学结构，这已是广泛共识（PRM-BiasBench、Xu et al. 2025都提供了证据）；(c) mitigation方法（Iso-Aug）的贡献更多是engineering而非conceptual——在训练中加入等价变换作为augmentation+consistency loss，这个idea本身不surprising。结果如果是positive，reviewer会说\"makes sense\"而非\"surprising\"。\n\n3. **Related Work: 强** — \n   这个proposal对related work的覆盖非常全面且准确。经调研验证：所有引用的论文都真实存在，arXiv IDs正确，描述准确。特别是对PRM-BiasBench、reWordBench、PutnamGAP、IPT、APRM、CoLD等工作的差异化定位清晰且正确。GR-Ben（2605.01203, May 2026）这样非常新的工作也被纳入，说明作者对领域的跟踪非常及时。与每个related work的关系描述（surface vs. structural, solver vs. verifier, response-level vs. step-level）精准。这是proposal最强的维度。\n\n【概率估计】: [20% - 32%] 中位 25%\n\n【估计理由】: \n三个维度综合来看，这是一个\"execution-heavy, idea-light\"的proposal。Related Work覆盖极其全面（强），说明作者深谙领域，定位精准。Novelty（中）——gap是真实的，但novelty的本质是\"在一个已经crowded的evaluation landscape中填补最后一个空位\"，而非提出surprising insight。Significance（中偏弱）是主要的上界限制因素：核心发现即使positive（discriminative PRMs确实brittle），reviewer更可能反应\"expected\"而非\"surprising\"；generative PRMs可能天然解决此问题进一步削弱motivation；mitigation方法是现有技术的直接组合。\n\n在EMNLP的标准下，benchmark paper需要证明benchmark本身揭示了unexpected phenomenon或enables new research direction。本proposal更接近\"系统性确认一个widely-expected weakness\"。Notation gaming angle有一定新意但只是simulation。上界被significance限制在~32%；下界~20%因为execution质量高、定位精准，不至于被直接desk-reject。\n\n【主要风险】: \n1. **\"Expected results\" 风险**: 核心发现（discriminative PRMs对数学等价变换brittle）对多数reviewer来说可能是预期内的结论，缺乏surprise value。审稿人可能评价\"confirms what we already suspected but doesn't tell us something new\"。\n2. **Generative PRM neutralization风险**: 如果GenPRM/ThinkPRM在测试中表现出高invariance，这既是proposal预期的结果之一，也同时削弱了整个研究方向的urgency——\"we built a benchmark that shows the old paradigm has a problem that the new paradigm already solves\"。\n```\n\nSources:\n- [PRM-BiasBench: Reward Under Attack](https://arxiv.org/abs/2603.06621)\n- [reWordBench: Benchmarking and Improving RM Robustness](https://arxiv.org/abs/2503.11751)\n- [PutnamGAP: Mathematically-Equivalent Transformations](https://arxiv.org/abs/2508.08833)\n- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [IPT / LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149)\n- [APRM: Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)\n- [CoLD: Counterfactual Length Debiasing for PRMs](https://arxiv.org/abs/2507.15698)\n- [GR-Ben: General Reasoning Benchmark for PRMs](https://arxiv.org/abs/2605.01203)\n- [FoVer: Efficient PRM Training Data via Formal Verification](https://arxiv.org/abs/2505.15960)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [PRM-BiasBench / Reward Under Attack] (arXiv:2603.06621, Feb 2026): 最直接的竞争工作。对 PRM 施加 8 种 surface perturbation（rephrasing、verbosity 等），发现 fluency-logic dissociation：PRMs 对 rephrasing 鲁棒（|ΔR|<0.03）但对 semantic corruption 脆弱。Section 6 的 RL hackability 实验（>0.9 PRM rewards with <4% accuracy, 43% reward gains from stylistic shortcuts）是本 proposal notation gaming 分析的直接灵感来源。关键区别：PRM-BiasBench 测的是 surface-level perturbation，本 proposal 声称测的是 structural-level isomorphism——但这个区别的实质深度需要审视。\n- [reWordBench] (EMNLP 2025, arXiv:2503.11751): 对通用 reward model 施加 meaning-preserving 输入变换（punctuation、paraphrasing、code minification），发现 SOTA RMs 在某些变换下降到 below-random accuracy。提出 paraphrase-consistency training。区别：response-level general RMs vs. step-level PRMs；surface transformations vs. structural isomorphisms。\n- [PutnamGAP] (arXiv:2508.08833): 对 1,051 道 Putnam 题生成数学等价变体（4 种 surface renames + kernel rewrite），测试 LLM solvers。O3 在 kernel variants 上掉 ~12.9pp。关键区别：测 solver 不测 verifier，测 problem level 不测 step level。\n- [IPT / LLMs Gaming Verifiers] (arXiv:2604.15149, Apr 2026): 提出 Isomorphic Perturbation Testing 检测 RLVR 中的 reward hacking，发现 shortcut prevalence 随 complexity 和 compute 增加。区别：测 RLVR outcome verifiers，不测 PRM step-level verifiers。\n- [GR-Ben] (arXiv:2605.01203, May 2026): 将 PRM 评估扩展到 9 个非数学 subdomain（science + logic），22 个模型。测 domain generalization breadth，不测 invariance。\n- [APRM] (arXiv:2511.22888): 对抗训练 PRM，Generator 学习生成错误推理步骤来欺骗 PRM。+3.4pp solver accuracy, +5.3pp OOD。与本 proposal 的 Iso-Aug 互补：APRM 提高 error detection robustness，Iso-Aug 提高 invariance to correct reformulations。\n- [CoLD] (arXiv:2507.15698): 因果去偏框架解决 PRM 的 length bias。本 proposal 声称将 S→L→P 替换为 S→F→P（serialization format）来适配。\n- [PRMBench] (ACL 2025, arXiv:2501.03124): 多维 PRM 评估，包括 sensitivity 和 consistency，但不含 structural isomorphism。\n- [Socratic-PRMBench] (arXiv:2505.23474): 6 种推理模式下的 PRM 评估，不涉及 invariance testing。\n- [FoVer] (ACL 2026 Findings, arXiv:2505.15960): Z3/Isabelle 用于 PRM 训练数据合成，85.8% AUROC on ProcessBench。本 proposal 复用类似的 formal verification pipeline。\n- [GenPRM] (AAAI 2026, arXiv:2504.00891): Code-based generative PRM，1.5B 模型超越 GPT-4o。Code execution 可能天然具有 notation invariance（SymPy 对 '3/4' 和 '0.75' 处理一致）。\n- [ThinkPRM] (arXiv:2504.16828): Long-CoT verification，比 discriminative PRMs 高 8% on GPQA-Diamond。\n\n- 调研总结: PRM 评估/鲁棒性是一个高度活跃且日益拥挤的领域。2025-2026 年已出现大量 PRM benchmark（ProcessBench、PRMBench、Socratic-PRMBench、GR-Ben、PRM-BiasBench、ToolPRMBench 等），各自覆盖不同维度。本 proposal 定位在\"step-level structural isomorphism invariance\"这一尚未被直接占据的细分空间，但该空间是已有工作（PRM-BiasBench 的 surface perturbation + PutnamGAP 的 mathematical equivalence + IPT 的 isomorphic testing）的自然交叉延伸。\n\n【Trivial Alternative 检验】:\n最直接的 trivial alternative：直接复用 PRM-BiasBench 的 framework，将其 8 种 surface perturbation 替换为 4 种 structural isomorphism（variable renaming 等），即可基本达到同样的 benchmark 目标。PRM-BiasBench 已经提供了 ProcessBench 上的评估 pipeline、cross-model comparison methodology、甚至 RL hackability analysis framework。本 proposal 的增量价值需要回答：为什么不能简单地在 PRM-BiasBench 的框架上加 4 个 transformation type 作为一个 follow-up experiment？\n\nProposal 的增量价值主要在于：(1) formal verification pipeline（SymPy + Z3）确保变换的数学正确性，这比 PRM-BiasBench 的 surface perturbation 需要更严格的验证；(2) step-level 而非 response-level 的粒度；(3) cross-paradigm comparison（discriminative vs. generative PRMs）在 isomorphism 维度上的对比。但这些增量是否足以构成独立贡献而非 PRM-BiasBench 的扩展实验，存在争议。\n\n对于 Iso-Aug：consistency regularization on isomorphic pairs（L = Σ(r(xi)−r(xj))²）是标准的 consistency training。reWordBench 已经提出了 paraphrase-consistency training 且证明它泛化到其他 transformation types。Iso-Aug 与 reWordBench 的方法论差异仅在于 augmentation 的数据来源（structural isomorphisms vs. paraphrases）和应用目标（PRMs vs. general RMs）。这是一个 incremental adaptation，不是方法论创新。\n\n结论：存在较强的 trivial alternative 威胁。核心 benchmark 贡献可以被视为 PRM-BiasBench 的自然扩展；Iso-Aug 可以被视为 reWordBench consistency training 的直接迁移。增量价值真实存在（formal verification、step-level 粒度、paradigm comparison），但深度有限。\n\n【前提假设检验】:\n核心 claim 的逻辑链有以下未经验证的假设：\n\n1. **\"Isomorphic brittleness 是一个真实且严重的问题\"** — PRM-BiasBench 已经表明 PRMs 对 rephrasing 其实是 robust 的（|ΔR|<0.03）。如果 PRMs 对 surface-level rephrasing 鲁棒，那么对 structural isomorphisms（variable renaming、commutative reordering）是否也可能是鲁棒的？特别是 T1（variable renaming）和 T2（commutative reordering）是非常基本的变换，训练数据中可能已经包含了大量此类变体。这个假设如果不成立（即 PRMs 在 isomorphism 维度上已经足够 robust），整个 benchmark 的价值大幅缩水——虽然 proposal 有 \"generative PRM trajectory\" 的 hedge，但一个\"大部分模型都 pass\"的 benchmark 在审稿人眼中价值有限。\n\n2. **\"Isomorphic brittleness 可以解释 tree search failure\"** — Proposal 引用 arXiv:2510.20272 指出 PRM-guided tree search 不如 simple best-of-N，并推测 isomorphic brittleness compounding across steps 是原因之一。但这是一个未经验证的因果推断。Tree search failure 可能有多种原因（score miscalibration、distribution shift、search algorithm issues），isomorphic brittleness 是否是 dominant factor 完全未知。\n\n3. **\"Notation gaming 是一个比 fluency gaming 更深层的攻击面\"** — Proposal 声称 notation gaming \"harder to detect because the output contains valid mathematical content\"。但 PRM-BiasBench 的 fluency gaming 已经使用了 valid language content（只是 style 不同），notation gaming 并不必然\"更深\"——它只是在不同的 surface 维度上。而且 proposal 只做 simulation（重写 notation 后看 score 变化），不做真实 RL 训练，这比 PRM-BiasBench 的实际 GRPO 实验弱了一个量级。\n\n4. **T3/T4 变换的覆盖率足以支撑统计结论** — Proposal 估计 T3 ~45-55%、T4 ~35-45%，在某些子集（OlympiadBench T4 ~30%、Omni-MATH T4 ~25%）覆盖率较低。虽然 proposal 承诺用 AMC/AIME 补充，但这引入了 distribution shift（ProcessBench 的 annotation 不再适用于补充数据）。\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   Gap 是真实的：确实没有工作在 step level 测试 PRMs 的 structural isomorphism invariance。但这个 gap 是高度可预测的组合式创新：PRM-BiasBench 的 perturbation framework + PutnamGAP 的 mathematical equivalence taxonomy + IPT 的 isomorphic testing idea → 自然得出\"对 PRMs 做 step-level structural isomorphism testing\"。四种 transformation types（variable renaming、commutative reordering、representation change、notation change）都是标准的数学等价变换，无方法论创新。Iso-Aug 是 reWordBench consistency training + CoLD causal debiasing 的直接拼接。如果核心发现是 \"PRMs are brittle to isomorphisms\"，审稿人很可能反应是 \"I would have guessed this, given PRM-BiasBench's findings on surface brittleness\"。如果发现是 \"PRMs are robust\"，则 benchmark 价值更低。唯一可能产生 surprise 的是跨 paradigm 的差异幅度（discriminative vs. generative），但这依赖实验结果而非 idea 本身。\n\n2. **Significance: 中** — \n   研究问题本身是重要的：PRM 是 test-time compute scaling 的核心组件，其 robustness 直接影响 deployment 可靠性。PRM 评估领域确实需要更全面的 robustness 测试。但重要性被两个因素削弱：(a) PRM-BiasBench 已经在 surface robustness 维度上做了类似的工作，且其 RL hackability 分析更有深度（真实 GRPO 训练 vs. 本 proposal 的 simulation）；(b) 如果 generative PRMs（GenPRM、ThinkPRM）确实天然具有 isomorphic robustness（code execution inherently notation-invariant），那么这个问题在未来可能自然消解，benchmark 的长期影响力有限——proposal 虽然 argue \"discriminative PRMs remain dominant in latency-sensitive deployment\"，但这个论点在 generative PRMs 快速发展的背景下不确定性很高。\n\n3. **Related Work: 强** — \n   Related work 覆盖极其全面，差异化定位清晰。Proposal 准确地定位了自己相对于 PRM-BiasBench（surface vs. structural）、reWordBench（response-level general RMs vs. step-level PRMs）、PutnamGAP（solver vs. verifier）、IPT（outcome vs. step-level）的差异。对 APRM 的互补性分析（error detection vs. invariance）也到位。所引用的论文全部真实存在且描述准确。这是 proposal 最强的维度。\n\n【概率估计】: [22% - 32%] 中位 26%\n\n【估计理由】: \nRelated Work 维度是强，但 Related Work 好只是论文的必要条件而非 idea 质量的指标。Novelty 处于弱-中之间——gap 真实但创新是组合式的、可预测的，核心贡献（benchmark + 标准 mitigation）缺乏方法论深度。Significance 处于中——问题重要但 expected findings 不够 surprising，且与 PRM-BiasBench 有较强的增量性质关系。\n\n上界受限于 **Novelty**：这本质上是一个\"在已有框架上换一组 perturbation types\"的工作，即使执行完美，审稿人也很可能认为贡献增量不足以独立成篇——特别是在 PRM benchmark 已经高度饱和的 2026 年中期。下界由 Related Work 的扎实覆盖和问题的真实重要性托底，不太可能被完全否定。\n\n【主要风险】:\n1. **\"Incremental over PRM-BiasBench\" rejection**: 最大风险。审稿人很可能认为这是 PRM-BiasBench 加了 4 个新 perturbation type + formal verification pipeline 的 extension work，novelty 不够 standalone paper。PRM-BiasBench 已建立了 PRM robustness benchmarking 的 paradigm，本工作在同一 paradigm 内做细化。\n2. **结果可预测性**: 如果 discriminative PRMs brittle（预期内）而 generative PRMs robust（也在预期内，因为 code execution inherently invariant），整篇论文的发现不会让审稿人感到 surprised。最 interesting 的可能发现（e.g., certain PRMs robust to T1/T2 but catastrophically brittle to T3/T4, or brittleness anti-correlates with surface robustness）依赖实验结果，不是 idea 层面能保证的。\n```\n\nSources:\n- [PRM-BiasBench: Reward Under Attack](https://arxiv.org/abs/2603.06621)\n- [reWordBench: Benchmarking and Improving the Robustness of Reward Models](https://arxiv.org/abs/2503.11751)\n- [PutnamGAP: An Investigation of Robustness via Mathematically-Equivalent Transformations](https://arxiv.org/abs/2508.08833)\n- [IPT / LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)\n- [GR-Ben: A General Reasoning Benchmark for Evaluating PRMs](https://arxiv.org/abs/2605.01203)\n- [APRM: Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)\n- [CoLD: Counterfactually-Guided Length Debiasing for PRMs](https://arxiv.org/abs/2507.15698)\n- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [PRMBench: Fine-grained and Challenging Benchmark for PRMs](https://arxiv.org/abs/2501.03124)\n- [Socratic-PRMBench: Benchmarking PRMs with Systematic Reasoning Patterns](https://arxiv.org/abs/2505.23474)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [ProcessBench: Identifying Process Errors in Mathematical Reasoning](https://arxiv.org/abs/2412.06559)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models\n\n## Description\nWe propose IsoPRM-Bench, the first benchmark testing whether Process Reward Models maintain consistent scores across structurally isomorphic reasoning steps, paired with Iso-Aug, a mitigation method based on isomorphic augmentation with consistency regularization. While PRM-BiasBench tests surface perturbations (rephrasing, verbosity), reWordBench tests meaning-preserving transformations on general RMs at response level, PutnamGAP tests equivalent transformations on LLM solvers, GR-Ben extends PRM evaluation to 9 non-mathematical reasoning subdomains, and APRM improves error detection via adversarial training, no existing work tests step-level structural invariance of PRM verifiers — whether a PRM scores logically equivalent steps identically when their mathematical realization differs. Starting from ProcessBench's 3,400 human-annotated solutions (GSM8K: 400, MATH: 1,000, OlympiadBench: 1,000, Omni-MATH: 1,000), we generate isomorphic variants across four formally verifiable transformation types (variable renaming, commutative reordering, representation change, notation change) with a three-tier verification pipeline (SymPy, Z3, human audit). We explicitly quantify per-transformation coverage: T1/T2 apply broadly (~60-75% of steps), while T3/T4 require specific mathematical content (~35-55%), with coverage validated via a 100-solution pilot annotation and supplemented by AMC/AIME solutions if needed. We evaluate PRMs spanning three paradigms — discriminative (Qwen2.5-Math-PRM-72B/7B, Math-Shepherd), generative-CoT (ThinkPRM), and generative-code (GenPRM) — using an Isomorphic Invariance Score (IIS). Crucially, we cross-analyze IIS with PRM-BiasBench's surface robustness to map the two-dimensional robustness landscape. For mitigation, we adapt CoLD's causal debiasing framework to fine-tune Qwen2.5-Math-PRM-7B with isomorphic augmentation and consistency regularization, positioning Iso-Aug as complementary to APRM's adversarial training (which improves error detection robustness via novel negative generation, while Iso-Aug improves invariance across valid reformulations). Our analysis targets five key findings: (1) anti-correlated model-specific blind spots across transformation types, (2) whether generative PRMs show inherent isomorphic robustness — and if so, quantifying the paradigm gap to inform deployment decisions between latency-sensitive discriminative PRMs and invariance-superior generative PRMs, (3) whether brittleness increases with step depth (explaining tree search failure), (4) the practical impact on best-of-N selection with diverse reasoning strategies, and (5) a notation gaming attack surface analysis demonstrating how a policy can exploit PRM notation preferences to inflate scores without improving reasoning — analogous to but structurally deeper than PRM-BiasBench's finding that 43% of RL reward gains come from fluency-based stylistic shortcuts. We explicitly address the generative PRM trajectory: even if GenPRM/ThinkPRM pass invariance tests, the benchmark quantifies the paradigm robustness gap for deployment decisions, provides Iso-Aug training signal to improve latency-efficient discriminative PRMs, and establishes isomorphic invariance as a standard evaluation dimension. We adopt a two-phase submission strategy: benchmark-focused for AAAI 2027 (Jul 28; human-in-loop mode, 8-10 weeks), with full Iso-Aug + APRM composition for ICLR 2027 backup (~Oct 2026). This work bridges the gap between outcome-level robustness testing (IPT, PutnamGAP) and step-level verification, with direct implications for PRM-guided test-time compute scaling and reward hacking prevention.\n\n## Core Problem\nProcess Reward Models are deployed to guide test-time compute scaling (best-of-N, tree search), yet no existing evaluation tests whether PRMs maintain consistent scores across structurally isomorphic reasoning — the same logical derivation with different surface realizations. This is the critical test of whether PRMs verify reasoning structure or pattern-match surface forms, and directly determines whether PRM-guided search can benefit from diverse solution strategies. Moreover, this brittleness creates a concrete reward hacking attack surface: a solver policy trained with PRM-guided RLHF/RLVR can learn to exploit the verifier's notation preferences — expressing intermediate steps in PRM-favored surface forms (e.g., decimals over equivalent fractions, expanded over factored polynomials) to inflate scores without improving reasoning quality. This is analogous to PRM-BiasBench's fluency-based gaming but operates at the structural mathematical level, making it harder to detect because the output contains valid mathematical content.\n\n## Opportunity\nExisting PRM benchmarks form a hierarchy: error detection (ProcessBench, PRMBench), domain generalization (GR-Ben), surface robustness (PRM-BiasBench), and domain transfer (UniversalBench, ToolPRMBench). No benchmark tests structural invariance — whether a PRM scores logically equivalent steps identically when their mathematical realization differs. reWordBench (EMNLP 2025) tests general RM robustness via meaning-preserving input transformations (paraphrasing, typos, code minification), finding RMs drop to below-random accuracy, but targets response-level general RMs rather than step-level PRMs. PutnamGAP (arXiv:2508.08833) tests mathematically equivalent transformations but targets LLM solvers at the problem level, not PRM verifiers at the step level. PRM-BiasBench finds PRMs are invariant to shallow style changes but inconsistent on semantic corruption — a fluency-logic dissociation. Xu et al. (2025) show PRMs identify consistency not causality, with problem-statement removal causing only 0.4-point drops. Meanwhile, PRM-guided tree search fails to outperform simple best-of-N (arXiv:2510.20272), with PRM reliability degrading at depth — a failure potentially rooted in isomorphic brittleness compounding across search steps. Critically, PRM-BiasBench's Section 6 RL hackability analysis demonstrates the concrete danger of PRM brittleness: policies trained with GRPO achieve near-perfect PRM rewards (>0.9) while ground-truth accuracy remains below 4%, with a rephrasing intervention revealing that 43% of reward gains are attributable to stylistic shortcuts rather than reasoning improvement (reward drops from 0.641 to 0.472 under semantics-preserving rephrasing). Isomorphic brittleness opens an analogous but deeper attack surface: notation gaming exploits PRM preferences over logically equivalent mathematical representations — producing outputs with valid mathematical content optimized for score inflation, which is harder to detect than the fluency-based gaming (performative complexity, vacuous safety) identified by PRM-BiasBench. We fill the structural invariance gap at the process level, complementing PutnamGAP's solver-level testing, PRM-BiasBench's surface-level testing, and reWordBench's response-level general RM testing, while also providing a mitigation pathway through isomorphic augmentation training.\n\n## Landscape\nreWordBench (EMNLP 2025, arXiv:2503.11751) applies meaning-preserving input transformations — controlled (punctuation, quotation marks), naturalistic (character swaps, paraphrasing), and domain-specific (code minification) — to general reward models, finding state-of-the-art RMs suffer substantial degradation including below-random accuracy on some transformations; they propose paraphrase-consistency training that generalizes to other transformation types. Crucially, reWordBench targets response-level general RMs with surface-preserving transformations, while we target step-level PRMs with structural isomorphisms that preserve mathematical content but change its formal realization — a deeper invariance axis. PRM-BiasBench (arXiv:2603.06621) applies 8 surface perturbation types and finds a fluency-logic dissociation: PRMs are robust to rephrasing (|ΔR|<0.03) but fail on semantic corruption; code and data at github.com/SqueezeAILab/reward-under-attack. ProcessBench (arXiv:2412.06559) evaluates step-level error detection across 3,400 problems with fixed formulations. PRMBench (ACL 2025, arXiv:2501.03124) tests multi-dimensional PRM capabilities including sensitivity and consistency but not structural isomorphism. Socratic-PRMBench (arXiv:2505.23474) benchmarks across six reasoning patterns but never compares two correct reformulations of the same step. GR-Ben (arXiv:2605.01203, May 2026) extends PRM evaluation to general reasoning across 2 primary domains (science and logic) and 9 subdomains with 22 models, finding existing PRMs score markedly lower on non-mathematical domains; it tests domain generalization breadth but not invariance or robustness within any single domain, and its emergence further demonstrates the field's continued production of PRM benchmarks while the structural invariance axis remains untested. PutnamGAP (arXiv:2508.08833) applies mathematically equivalent transformations (4 surface renames + kernel rewrites) to 1,051 Putnam problems but tests only LLM solvers, finding kernel variants cause ~10+ pp accuracy drops even on O3; the solver-verifier distinction is critical since PRM brittleness corrupts the training signal, not just benchmark scores. IPT (arXiv:2604.15149) tests RLVR outcome verifiers via isomorphic tasks, finding RLVR-trained models systematically fail invariance with more compute producing more shortcuts — an inverse scaling result. APRM (arXiv:2511.22888) proposes adversarial training for PRMs via a two-player game where a Generator learns to produce plausible reasoning errors while the PRM learns to detect them, yielding +3.4pp solver accuracy and +5.3pp on OOD tasks over the strongest PRM baseline; APRM improves error detection robustness via adversarial negatives, which is complementary to our Iso-Aug that improves invariance to correct reformulations via isomorphic augmentation — adversarial training and consistency training address orthogonal failure modes (missing true errors vs. inconsistent scoring of valid steps). BiPRM (arXiv:2508.01682) improves step estimation via bidirectional context. FoVer (arXiv:2505.15960, ACL 2026 Findings) uses Z3/Isabelle for PRM data synthesis, achieving 85.8% AUROC on ProcessBench, but limited to first-order logic domains. GenPRM (arXiv:2504.00891) redefines process verification as generative with code execution, where a 1.5B model outperforms GPT-4o — suggesting code-based verification may be inherently more isomorphism-invariant. ThinkPRM (arXiv:2504.16828) uses long-CoT verification outperforming discriminative PRMs by 8% on GPQA-Diamond. CoLD (arXiv:2507.15698) addresses length bias via counterfactual debiasing with a causal graph framework (S→L→P spurious pathway), directly adaptable to isomorphic invariance (replace length with serialization format). Crome (arXiv:2506.16507, ICML 2025) uses causal + neutral augmentations for RM robustness, achieving 5.4% accuracy gains and 9.1% robustness gains. The Robust Reasoning Benchmark (arXiv:2604.08571) applies 14 perturbation techniques to AIME problems but targets solvers. No work combines step-level structural isomorphism testing of PRMs with a mitigation pathway via invariance training, nor demonstrates how isomorphic brittleness creates a concrete notation gaming reward hacking attack surface.\n\n## Approach\nWe propose a two-part contribution: (1) IsoPRM-Bench, a benchmark for structural isomorphism invariance of PRMs, and (2) Iso-Aug, a mitigation method using isomorphic augmentation with consistency regularization.\n\n**Part 1: IsoPRM-Bench.** Starting from ProcessBench's 3,400 human-annotated step-level math solutions (GSM8K: 400, MATH: 1,000, OlympiadBench: 1,000, Omni-MATH: 1,000), we generate structurally isomorphic variants of each reasoning step across four transformation types with provable symbolic equivalence: (T1) variable renaming — systematic substitution of variable symbols while preserving all relational structure; (T2) commutative operation reordering — reordering addition/multiplication operands and equation sides; (T3) representation change — arithmetic ↔ algebraic, e.g., '3+5=8' ↔ 'x+y=z where x=3,y=5,z=8'; (T4) notation change — fraction ↔ decimal ↔ scientific notation ↔ expanded/factored polynomial forms.\n\n**T3/T4 Coverage Analysis.** Not all ProcessBench steps are amenable to all four transformations. We estimate per-subset applicability based on mathematical content requirements: T1 (variable renaming) applies to ~65-75% of steps (any step referencing named variables; lower in GSM8K's prose-style ~50%, higher in MATH/OlympiadBench/Omni-MATH ~70-85%); T2 (commutative reordering) applies to ~60-70% (any step with addition, multiplication, or equalities); T3 (representation change) applies to ~45-55% (requires explicit arithmetic computations or algebraic formulations — high in GSM8K ~75% and MATH algebra subsets ~55%, lower in OlympiadBench ~40% and Omni-MATH ~35% due to more abstract proof-style reasoning); T4 (notation change) applies to ~35-45% (requires fractions, decimals, percentages, or polynomial expressions — moderate in GSM8K ~55% and MATH ~45%, lower in OlympiadBench ~30% and Omni-MATH ~25%). We will validate these estimates via a pilot annotation of 100 randomly sampled ProcessBench solutions (25 per subset) before full-scale generation, reporting exact applicability rates. Even at the conservative lower bound, T4 yields ~1,200+ applicable step instances — statistically sufficient for per-model and per-transformation-type analysis. The uneven coverage is itself informative: it reveals which math domains and difficulty levels are most affected by notation sensitivity, and we will report transformation-type × subset breakdowns. If T4 coverage falls below 30% in OlympiadBench/Omni-MATH, we will supplement with 200 additional solutions from AIME/AMC competition problems (rich in notation-heavy content) generated and annotated using the same pipeline.\n\nWe deliberately restrict to transformations with automated formal verification: T1-T2 via direct AST manipulation, T3-T4 via SymPy symbolic equivalence and Z3 SMT solving (following FoVer's demonstrated approach). We drop 'equivalent natural-language reformulation' from the taxonomy because it overlaps with PRM-BiasBench's rephrasing perturbation and reWordBench's paraphrasing transformations, and lacks reliable automated verification. Variants are generated via Claude Sonnet 4.6 with constrained prompting, followed by a three-tier verification pipeline: (i) symbolic CAS equivalence check via SymPy, (ii) SMT satisfiability check via Z3 for first-order logic reformulations, (iii) human spot-verification on a 15% stratified sample (stratified by transformation type, difficulty, and subset). We evaluate state-of-the-art PRMs spanning three paradigms — discriminative (Qwen2.5-Math-PRM-72B, Qwen2.5-Math-PRM-7B, Math-Shepherd), generative-CoT (ThinkPRM), and generative-code (GenPRM-7B) — computing an Isomorphic Invariance Score (IIS = 1 − normalized score variance across isomorphic variants) per step, per transformation type, and per step position. We cross-analyze IIS with PRM-BiasBench's surface perturbation scores to test orthogonality: can a PRM be robust to style changes but brittle to structural isomorphism?\n\n**Part 2: Iso-Aug Mitigation.** We adapt CoLD's causal debiasing framework by replacing the spurious pathway S→L→P (length) with S→F→P (serialization format). Concretely, we fine-tune Qwen2.5-Math-PRM-7B using LoRA with three components: (a) isomorphic augmentation — for each training step, generate 2-3 isomorphic variants using our T1-T4 pipeline, labeled identically to the original; (b) consistency regularization loss — L_consistency = Σ(r(x_i) − r(x_j))² across all isomorphic pairs (i,j), added to the standard BCE loss; (c) bias estimator module — a parallel network trained to capture serialization-dependent signals (following CoLD's joint training), with complementary correlation constraints forcing the PRM to decorrelate from format while the estimator absorbs format artifacts. Training uses Axolotl framework with native PRM support. We position Iso-Aug as complementary to APRM's adversarial training: APRM improves robustness to novel errors (error detection), while Iso-Aug improves invariance across valid reformulations (score consistency) — these address orthogonal PRM failure modes and could potentially be composed. We then re-evaluate the fine-tuned model on IsoPRM-Bench and on ProcessBench (to verify no accuracy regression).\n\n**Analysis.** Beyond aggregate IIS, we report: (i) transformation-type breakdown — which isomorphisms each PRM is most/least robust to, with T3/T4 applicability rates per subset explicitly reported; (ii) model-paradigm comparison — whether generative PRMs (code-based GenPRM) show inherent isomorphic robustness vs. discriminative PRMs; (iii) step-position analysis — whether isomorphic brittleness increases with step depth, explaining tree search reliability degradation; (iv) orthogonality matrix — cross-tabulating IIS with PRM-BiasBench's surface robustness to map the two-dimensional robustness landscape; (v) practical impact — measuring how IIS correlates with best-of-N selection accuracy on MATH-500 when candidate solutions use diverse strategies; (vi) notation gaming attack surface — we construct a proof-of-concept demonstrating how isomorphic brittleness enables reward hacking. Using our per-transformation IIS scores, we identify each evaluated PRM's strongest notation preferences (e.g., if a PRM systematically scores decimal representations 0.1+ higher than equivalent fractions, or prefers expanded polynomial forms over factored forms). We then simulate a notation-gaming policy that, during PRM-guided best-of-N selection on MATH-500, reformulates its candidate solutions' reasoning steps into the PRM-preferred notation at each step using our T1-T4 pipeline. We measure the resulting score inflation (Δ reward) and selection accuracy change relative to notation-neutral baselines, and compare the magnitude of notation gaming gains to PRM-BiasBench's finding that 43% of RL reward gains are attributable to stylistic shortcuts (Section 6.3: rephrasing intervention shows reward drops from 0.641 to 0.472 under semantics-preserving rephrasing). This directly demonstrates the reward hacking attack surface: a policy need not improve its reasoning to achieve higher PRM scores — it need only learn the verifier's notation preferences. Unlike PRM-BiasBench's fluency-based gaming (Skywork's performative complexity via elaborate but flawed reasoning, Qwen's vacuous safety via minimal substance), notation gaming is harder to detect because the output contains valid mathematical content expressed in a legitimately equivalent form, and it compounds across search depth — each step's notation choice independently inflates the cumulative score, potentially explaining why PRM-guided tree search degrades at depth (arXiv:2510.20272).\n\n**Generative PRM Trajectory.** We explicitly address the scenario where generative PRMs (GenPRM, ThinkPRM) demonstrate substantial isomorphic invariance, which is plausible given GenPRM's code-based verification (code execution is inherently notation-invariant since SymPy evaluates '3/4' and '0.75' identically) and ThinkPRM's explicit CoT reasoning before scoring. Even in this outcome, IsoPRM-Bench provides three critical contributions: (a) quantifying the paradigm robustness gap gives the field concrete evidence for when generative PRMs' 10-100x inference cost premium is justified by their invariance properties, informing the architecture-vs-cost tradeoff in deployment decisions; (b) discriminative PRMs remain dominant in latency-sensitive deployment — real-time search guidance during tree search and high-throughput RLHF training loops where per-step generative verification is prohibitively expensive — and Iso-Aug provides the training signal to improve these cost-efficient models toward generative-level invariance without the inference overhead; (c) establishing isomorphic invariance as a standard evaluation dimension for future PRMs, analogous to how fairness benchmarks became standard evaluation axes even as models improved on them, ensures the field systematically tracks this property as PRM architectures evolve.\n\n**Timeline Contingency.** Given the AAAI 2027 deadline (Jul 28, 2026; 10 weeks from today) and the tight margin with our estimated timeline, we adopt a two-phase submission strategy: *Phase 1 (AAAI target):* Submit IsoPRM-Bench as a benchmark paper, prioritizing the benchmark construction (T1-T4 pipeline + verification), PRM evaluation across all 5 models, and the analysis components (i)-(vi). The Iso-Aug mitigation is presented as a preliminary experiment with LoRA fine-tuning on Qwen2.5-Math-PRM-7B, showing proof-of-concept IIS improvement. This phase uses the human-in-loop mode (8-10 weeks) with API-assisted generation to compress the timeline. The pilot annotation of 100 solutions for T3/T4 coverage validation is completed in week 1 to derisk. *Phase 2 (ICLR 2027 backup, expected ~Oct 2026):* If AAAI reviews suggest the mitigation needs fuller treatment, or if we miss the AAAI deadline, the ICLR submission includes the complete Iso-Aug with full ablations (component-wise contribution of augmentation, consistency loss, and bias estimator), APRM+Iso-Aug composition experiments, and extended analysis on supplementary competition problem datasets. The 4-5 additional weeks to ICLR allow the mitigation results to fully mature.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '400-600 (72B PRM inference: ~160h; 7B models ×3: ~90h; GenPRM/ThinkPRM inference: ~80h; Iso-Aug fine-tuning with LoRA: ~40h; variant generation with local LLMs: ~100h; ablations: ~80h)', 'timeline': '10-12 weeks (2w taxonomy + pipeline + verification + T3/T4 pilot, 2.5w data generation + three-tier QC, 2w PRM evaluation across 5 models × 3 paradigms, 1.5w Iso-Aug training + re-evaluation, 2w analysis + writing)', 'estimated_gpu_cost': '$800-1200 at ~$2/H100-hr'}, 'human_in_loop': {'gpu_hours': '300-450 (API-based generation eliminates local LLM GPU; 72B PRM inference: ~160h; other models: ~100h; Iso-Aug LoRA fine-tuning: ~40h; ablations: ~50h)', 'timeline': '8-10 weeks (1w taxonomy + pipeline + T3/T4 pilot annotation, 2w API-assisted generation + verification, 2w evaluation, 1w Iso-Aug training, 1.5w analysis + writing, 0.5w buffer)', 'claude_api_cost': '$500-900 (variant generation: ~100M tokens I/O via Sonnet at $3/$15 per MTok ≈ $600; verification + code assistance: ~$250)', 'estimated_gpu_cost': '$600-900'}, 'auto_research': {'gpu_hours': '200-350 (fully batched PRM inference + LoRA fine-tuning only; no local generation)', 'timeline': '6-8 weeks (1w automated pipeline build + T3/T4 pilot, 1.5w generation + automated three-tier QC, 1.5w evaluation, 1w Iso-Aug training, 1w analysis + writing)', 'claude_api_cost': '$900-1400 (heavier API generation with multi-pass quality filtering: ~$800; automated analysis + writing: ~$500)', 'estimated_gpu_cost': '$400-700', 'speed_bottleneck': 'Human validation of isomorphic correctness in the 15% spot-check sample; Z3/SymPy cover T1-T4 transformations with >95% automated verification, but edge cases in representation change (T3) require manual audit'}}\n\n## Inspired By\nCross-domain transfer: IPT methodology (arXiv:2604.15149) from RLVR outcome verification → PRM step-level verification; PutnamGAP transformation taxonomy (arXiv:2508.08833) from solver testing → verifier testing; CoLD causal debiasing framework (arXiv:2507.15698) from length bias → isomorphism bias; Crome neutral augmentations (arXiv:2506.16507) from general RM robustness → PRM structural invariance; reWordBench paraphrase-consistency training (arXiv:2503.11751) from response-level general RM → step-level PRM; APRM adversarial training (arXiv:2511.22888) as complementary robustness axis to our consistency-based approach; Field guide gap: PRMs detect fluency not reasoning (PRM-BiasBench Section 3.3); Tree search failure diagnosis: PRM reliability degradation at depth (arXiv:2510.20272) may be explained by compounding isomorphic brittleness; Reward hacking diagnosis: PRM-BiasBench Section 6 RL hackability analysis — policies achieve >0.9 PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts (rephrasing intervention: 0.641→0.472) — motivates our notation gaming attack surface analysis as a concrete demonstration that isomorphic brittleness creates an exploitable reward hacking vector at the structural mathematical level, deeper than the fluency-based gaming (performative complexity, vacuous safety) they identify\n\n## Target Venues\n- AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target with benchmark-focused submission; 10 weeks from today, feasible with human-in-loop mode at 8-10 weeks; Iso-Aug presented as preliminary experiment)\n- ICLR 2027 (deadline expected ~Sep-Oct 2026 — backup target with full Iso-Aug results, APRM+Iso-Aug composition experiments, and extended analysis; 4-5 extra weeks allow mitigation to fully mature)\n- NeurIPS 2027 (deadline expected ~May 2027 — fallback if major revisions needed after AAAI/ICLR reviews)\n\n## Key References\n- reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs (EMNLP 2025, arXiv 2503.11751) — response-level general RM robustness via meaning-preserving transformations; paraphrase-consistency training; we extend the invariance-testing paradigm to step-level PRMs with structural (not surface) isomorphisms\n- Adversarial Training for Process Reward Models (arXiv 2025, 2511.22888) — adversarial Generator-PRM game for error detection robustness, +3.4pp solver accuracy; complementary to our Iso-Aug which addresses invariance to correct reformulations rather than robustness to novel errors\n- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv 2026, 2604.15149) — IPT methodology transferred to our step-level PRM testing\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv 2026, 2603.06621) — fluency-logic dissociation, orthogonal robustness axis, model-specific blind spots; Section 6 RL hackability analysis shows >0.9 PRM rewards with <4% accuracy and 43% of reward gains from stylistic shortcuts, directly motivating our notation gaming analysis\n- PutnamGAP: An Investigation of Robustness via Mathematically-Equivalent Transformations (arXiv 2025, 2508.08833) — solver-level equivalent-transformation testing; we extend to verifier-level step testing\n- ProcessBench: Identifying Process Errors in Mathematical Reasoning (arXiv 2024, 2412.06559) — base dataset for our isomorphic variants\n- Reward Models Identify Consistency, Not Causality (arXiv 2025, 2502.14619) — theoretical motivation; problem-statement removal causes only 0.4-point drops\n- Limits of PRM-Guided Tree Search for Mathematical Reasoning (arXiv 2025, 2510.20272) — PRM reliability degrades at depth; isomorphic brittleness as mechanistic explanation; notation gaming compounds across search steps\n- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv 2025, 2507.15698) — causal debiasing framework adapted for our Iso-Aug mitigation\n- Crome: Causally Robust Reward Modeling (ICML 2025, arXiv 2506.16507) — neutral augmentation strategy for RM invariance training\n- GenPRM: Scaling Test-Time Compute of Process Reward Models (AAAI 2026, arXiv 2504.00891) — generative code-based PRM; potential inherent isomorphic robustness due to notation-invariant code execution\n- Process Reward Models That Think (ThinkPRM) (arXiv 2025, 2504.16828) — generative CoT verifier for cross-paradigm comparison\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025, 2501.03124) — multi-dimensional PRM evaluation, no structural isomorphism\n- Socratic-PRMBench: Benchmarking PRMs with Systematic Reasoning Patterns (arXiv 2025, 2505.23474) — reasoning pattern evaluation, no invariance testing\n- GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models (arXiv 2026, 2605.01203) — extends PRM evaluation to general reasoning across 9 subdomains (science and logic) with 22 models; tests domain generalization breadth but not structural invariance, strengthening the benchmark saturation argument that this specific axis remains the critical missing piece\n- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026, 2505.15960) — Z3/Isabelle verification approach adapted for our verification pipeline\n- Math-Shepherd: Verify and Reinforce LLMs Step-by-step (arXiv 2023, 2312.08935) — baseline PRM for evaluation\n- The Bidirectional Process Reward Model (arXiv 2025, 2508.01682) — bidirectional context for step estimation\n- Robust Reasoning Benchmark (arXiv 2026, 2604.08571) — 14 perturbation techniques for solvers, not verifiers\n- Inverse Scaling in Test-Time Compute (arXiv 2025, 2507.14417) — more compute can amplify flawed heuristics\n- Towards Robust Process Reward Model (arXiv 2026, 2601.12748) — noisy supervision robustness, not structural invariance\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T05:35:04.395Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:35:04.395Z",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T05:35:04.409Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me synthesize my findings.

---

```
【阶段】: Triage

【领域调研】:

1. **PRM-BiasBench (arXiv:2603.06621, Feb 2026)**: 最直接相关的工作。对 PRM 施加 8 种 surface perturbation，发现 fluency-logic dissociation（rephrasing 鲁棒但 semantic corruption 脆弱）。Section 6 展示 RL hackability（>0.9 PRM reward, <4% accuracy, 43% reward gains from stylistic shortcuts）。与本 proposal 的关系：PRM-BiasBench 测的是 surface-level perturbation，proposal 声称测试的是 structural isomorphism——更深一层的不变性。这个定位差异化是成立的，但需要注意两者的边界并不完全清晰（如 notation change 是否真的比 rephrasing "更深"值得商榷）。

2. **reWordBench (EMNLP 2025, arXiv:2503.11751)**: 测 general RM 的 meaning-preserving transformation robustness（paraphrasing, typos, code minification），发现 SOTA RM 在某些变换下降至 below-random。提出 paraphrase-consistency training。与本 proposal 的关系：reWordBench 面向 response-level general RM，proposal 面向 step-level PRM，且限定于 mathematically verifiable transformations。区分维度明确。

3. **PutnamGAP (arXiv:2508.08833, Aug 2025)**: 对 1,051 道 Putnam 题施加 mathematically equivalent transformations（4 种 surface rename + kernel rewrite），测 LLM solver 鲁棒性。O3 在 kernel rewrite 上下降 12.9pp。与本 proposal 的关系：PutnamGAP 测 solver、problem-level；proposal 测 verifier、step-level。方法论灵感来源清晰，但"从 solver 到 verifier"的迁移是否算 sufficient novelty 值得审视。

4. **IPT / LLMs Gaming Verifiers (arXiv:2604.15149, Apr 2026)**: 用 Isomorphic Perturbation Testing 检测 RLVR 训练的 shortcut 行为，发现 RLVR 模型系统性地 abandon rule induction。与本 proposal 的关系：IPT 测 outcome verifier，proposal 测 process verifier，概念上有启发关系但应用场景不同。

5. **APRM (arXiv:2511.22888, Nov 2025)**: 对抗训练 PRM，Generator 生成 plausible errors, PRM 学习检测。+3.4pp solver accuracy。与本 proposal 的关系：proposal 将 Iso-Aug 定位为与 APRM 互补（APRM 改善 error detection，Iso-Aug 改善 invariance），这个定位合理。

6. **CoLD (arXiv:2507.15698, Jul 2025)**: 因果 debiasing 框架消除 PRM 长度偏差。与本 proposal 的关系：proposal 将 CoLD 的 S→L→P 框架迁移为 S→F→P（format bias），技术迁移路径清晰但 novelty 增量有限。

7. **GenPRM (AAAI 2026, arXiv:2504.00891)** & **ThinkPRM (arXiv:2504.16828)**: Generative PRM 范式——GenPRM 用 code verification, ThinkPRM 用 long-CoT。与本 proposal 的关系：proposal 假设 generative PRM 可能天然更 isomorphism-invariant（code execution 是 notation-invariant 的），这是一个合理且有趣的假设，但也意味着可能出现"generative PRM 已经解决了这个问题"的 dual outcome。

8. **GR-Ben (arXiv:2605.01203, May 2026)**: 将 PRM 评估扩展到 9 个非数学推理子域。与本 proposal 的关系：GR-Ben 测 domain generalization breadth，proposal 测 within-domain structural invariance，属于不同维度。

9. **FoVer (ACL 2026 Findings, arXiv:2505.15960)**: 用 Z3/Isabelle 做 PRM training data synthesis。与本 proposal 的关系：verification pipeline 的技术基础，proposal 引用合理。

10. **Socratic-PRMBench (arXiv:2505.23474)**: 6 种 reasoning pattern 的 PRM benchmark。与本 proposal 的关系：不测 invariance，是不同维度的 benchmark。

11. **FormalRewardBench (arXiv:2605.10141, May 2026)** & **Unsupervised PRM (arXiv:2605.10158, May 2026)**: 最近几周的 PRM benchmark/method 工作，进一步说明该领域正在快速发展和 benchmark 饱和。

- **调研总结**: PRM robustness/evaluation 是 2025-2026 年的热点方向，benchmark 数量快速增长（ProcessBench → PRMBench → PRM-BiasBench → Socratic-PRMBench → GR-Ben → FormalRewardBench），但确实没有一个工作专门测试 step-level structural isomorphism invariance。这个 gap 是真实存在的。然而，这个 gap 的"深度"需要审视——它更多是一个评估维度的组合创新（PutnamGAP 的 transformation taxonomy × PRM-BiasBench 的 verifier robustness testing × step-level granularity），而非概念上的根本突破。


【Trivial Alternative 检验】:

**存在部分 trivial alternative 威胁：**

1. **最直接的 trivial baseline**: 将 PRM-BiasBench 的 perturbation set 扩展几种 math-specific transformations（如加入 variable renaming 和 notation change），而不构建全新 benchmark。PRM-BiasBench 已有 8 种 perturbation 和完整的评估框架，加入 T1-T4 变换类型只需增量工作。Proposal 对此的增量价值在于：(a) 形式化验证保证（SymPy/Z3），PRM-BiasBench 的 perturbation 缺乏这种数学等价性保证；(b) step-level 而非 solution-level 的分析粒度。但审稿人可能认为这些差异不足以支撑一篇独立论文。

2. **Notation gaming 分析的 trivial alternative**: PRM-BiasBench Section 6 已经展示了 reward hacking 的机制（43% stylistic shortcuts），notation gaming 只是同一现象的一个特例——用 "logically equivalent but notation-different" 的子集来 hack PRM。审稿人可能会问：这和 PRM-BiasBench 的发现相比，增量 insight 到底是什么？

3. **Iso-Aug 的 trivial alternative**: reWordBench 已经提出了 paraphrase-consistency training 并证明它 generalizes to other transformations。如果简单地将 isomorphic pairs 加入 reWordBench 的 consistency training pipeline，是否就足以实现类似效果？Proposal 的 CoLD-based causal debiasing 增加了方法复杂度，但核心 idea（consistency regularization across equivalent inputs）与 reWordBench 的方法高度相似。

**增量价值的核心在于**: "形式化可验证的数学等价性" 作为 invariance 的测试标准，比 surface perturbation 更严格、更有理论根基。但这个增量是否足够支撑 top venue 论文，取决于实验结果是否能揭示 PRM-BiasBench 未发现的 failure patterns。


【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的假设：

1. **"Isomorphic brittleness 存在且显著"**（关键假设）: 整个 proposal 建立在一个未验证的前提上——PRM 对 structurally isomorphic reasoning steps 会给出不同的 scores。PRM-BiasBench 发现 PRM 对 rephrasing 是 robust 的（|ΔR|<0.03），而 proposal 声称更深层的 structural isomorphism 会导致 brittleness。但如果 PRM 连 rephrasing 都能处理，为什么变量重命名（T1）、交换律重排（T2）这些同样是表面变换的操作会导致更大的 brittleness？T1/T2 实际上可能比 rephrasing 更简单（纯符号替换 vs. 语义保持的自然语言改写）。**如果实验发现 PRM 对 T1-T4 都相当 robust，整篇论文的核心 narrative 就会瓦解。** Proposal 确实有 dual-outcome 设计（"即使 generative PRM robust，也有价值"），但 dual-outcome 不能拯救一个核心假设被否定的论文。

2. **"Isomorphic brittleness 解释了 tree search failure"**: Proposal 将 PRM-guided tree search 的失败（arXiv:2510.20272）归因于 isomorphic brittleness 在 search depth 上的 compounding。但 tree search 失败的原因可能更根本——PRM 对 partial solution 的 value estimation 本身就不准确（与 isomorphism 无关）。这个因果推断是 speculative 的。

3. **"Notation gaming 比 fluency gaming 更危险因为更难检测"**: 这个 claim 听起来合理但缺乏证据。如果 PRM 对 notation change 的 sensitivity 本来就很小（假设1不成立），那么 notation gaming 的 attack surface 就不存在。且"valid mathematical content"使其"更难检测"的论点需要对比实验支持，而非仅靠直觉论证。

4. **"CoLD 的 causal debiasing framework 可以直接迁移到 isomorphism bias"**: CoLD 的 S→L→P 因果图是基于 length 这个单一标量维度建模的。Isomorphism 涉及多维、离散的变换类型，因果图的结构是否仍然适用（即 serialization format 是否真的是一个单一的 confounder）未经论证。


【3 维度打分】:

**1. Novelty: 中偏弱** — 

核心贡献是一个"组合式创新"：将 PutnamGAP 的 mathematically equivalent transformation 概念（solver → verifier）、PRM-BiasBench 的 robustness testing 框架（surface → structural）、以及 step-level 粒度结合起来。每个组件都有明确的先驱工作：

- Transformation taxonomy: 直接借鉴 PutnamGAP（variable renaming, representation change）
- Robustness testing of verifiers: PRM-BiasBench 已建立
- Consistency training mitigation: reWordBench 的 paraphrase-consistency + CoLD 的 causal debiasing
- Formal verification pipeline: FoVer 的 Z3/Isabelle 方法

剥去 surface differences 后，核心 novelty delta 是"step-level structural isomorphism testing with formal verification guarantees"——这是真实的但增量的。审稿人的典型反应可能是"nice evaluation paper but limited methodological novelty"。Iso-Aug 作为 mitigation 方法论 novelty 更弱——本质上是 consistency regularization + CoLD framework 的直接迁移。

**2. Significance: 中** — 

研究问题的重要性是真实的：PRM 作为 test-time compute scaling 的核心组件（best-of-N, tree search, RLHF），其 robustness 直接影响下游系统的可靠性。PRM-BiasBench 的 Section 6（RL hackability）和 arXiv:2510.20272（tree search failure）都证明了 PRM 可靠性问题的实际影响。

但 significance 受限于：(a) 如果 generative PRM（GenPRM, ThinkPRM）天然 robust to structural isomorphism，那么 discriminative PRM 的这个问题可能只是暂时的——随着 generative PRM 的普及，这个问题自然消解；(b) notation gaming 的实际威胁程度未知——如果 PRM 对 notation 的 sensitivity 本身就小，这个 attack surface 就不具实际意义；(c) 这更多是一个 evaluation/benchmark 贡献，而非推动该领域 paradigm shift 的工作。

该研究对 NLP/CL 领域的 impact 是中等的：它会被 PRM 研究者引用为一个 evaluation dimension，但不太可能改变 PRM 的设计范式或训练方法论。

**3. Related Work: 强** — 

这是 proposal 最突出的优点。Related work coverage 非常全面且准确：覆盖了 PRM-BiasBench、reWordBench、PutnamGAP、IPT、APRM、CoLD、Crome、GenPRM、ThinkPRM、PRMBench、Socratic-PRMBench、GR-Ben、FoVer、ProcessBench 等几乎所有相关工作，且对每个工作的差异化定位清晰准确。引用的论文经 WebSearch 验证均真实存在，描述准确。特别是对 PRM-BiasBench（surface robustness）、PutnamGAP（solver-level）、reWordBench（response-level general RM）的三角定位，清楚地界定了 proposal 的 gap 所在。唯一的不足是 landscape 过于详尽可能暗示这是一个 crowded space 的 incremental contribution——正是因为 coverage 做得太好，反而暴露了 novelty 的有限性。


【概率估计】: [18% - 30%] 中位 23%

【估计理由】: 

Novelty 中偏弱 是主要限制因素。核心贡献是组合式创新——将已有概念（equivalent transformations、robustness benchmarking、consistency training）应用于一个新的但增量的维度（step-level structural isomorphism of PRMs）。每个技术组件都有清晰的先驱工作，剥去差异后的 novelty delta 有限。Significance 中等但受限于核心假设未验证（isomorphic brittleness 可能不显著）和 generative PRM 可能天然解决这一问题。Related work 虽然强，但强 related work 在评审中属于"不扣分"而非"加分"。

如果核心发现是 positive（PRM 确实对 structural isomorphism 脆弱），审稿人更可能的反应是 "I would have guessed this given PRM-BiasBench's fluency-logic dissociation findings" 而非 "surprising"。如果核心发现是 negative（PRM 对 T1-T4 robust），论文的 impact 会大幅下降。这将 idea 锚定在 25-35% 区间的下部。考虑到 benchmark paper 在 EMNLP 的接受门槛（需要强 novelty 或 strong community impact），以及 PRM benchmark 领域已趋于饱和（2025-2026 年已有 6+ 个 PRM benchmark），概率估计下调至 18-30%，中位 23%。

【主要风险】:

1. **核心假设风险**: PRM 可能对 T1-T4 structural isomorphisms 相当 robust（PRM-BiasBench 已发现对 rephrasing 的 |ΔR|<0.03），导致论文核心 narrative（"isomorphic brittleness 是严重问题"）无法成立。T1（variable renaming）和 T2（commutative reordering）本质上是比 rephrasing 更简单的表面变换，PRM 有可能对它们同样 robust。

2. **Benchmark 饱和 + 有限 novelty**: 2025-2026 年 PRM benchmark 快速增长（ProcessBench → PRMBench → PRM-BiasBench → Socratic-PRMBench → GR-Ben → FormalRewardBench），审稿人可能认为"又一个 PRM benchmark"的 marginal contribution 不足以接受。核心方法论（transformation taxonomy + consistency training）均有清晰的先驱工作，组合创新的 novelty bar 在 top venue 可能不够。
```

Sources:
- [PRM-BiasBench: Reward Under Attack (arXiv:2603.06621)](https://arxiv.org/abs/2603.06621)
- [reWordBench (EMNLP 2025, arXiv:2503.11751)](https://arxiv.org/abs/2503.11751)
- [PutnamGAP (arXiv:2508.08833)](https://arxiv.org/abs/2508.08833)
- [IPT / LLMs Gaming Verifiers (arXiv:2604.15149)](https://arxiv.org/abs/2604.15149)
- [APRM: Adversarial Training for PRMs (arXiv:2511.22888)](https://arxiv.org/abs/2511.22888)
- [CoLD: Counterfactual Length Debiasing (arXiv:2507.15698)](https://arxiv.org/abs/2507.15698)
- [GenPRM (arXiv:2504.00891)](https://arxiv.org/abs/2504.00891)
- [ThinkPRM (arXiv:2504.16828)](https://arxiv.org/abs/2504.16828)
- [GR-Ben (arXiv:2605.01203)](https://arxiv.org/abs/2605.01203)
- [FoVer (ACL 2026 Findings, arXiv:2505.15960)](https://arxiv.org/abs/2505.15960)
- [Socratic-PRMBench (arXiv:2505.23474)](https://arxiv.org/abs/2505.23474)
- [ProcessBench (arXiv:2412.06559)](https://arxiv.org/abs/2412.06559)
- [Limits of PRM-Guided Tree Search (arXiv:2510.20272)](https://arxiv.org/abs/2510.20272)
- [Crome: Causally Robust Reward Modeling (ICML 2025, arXiv:2506.16507)](https://arxiv.org/abs/2506.16507)
- [PRMBench (ACL 2025, arXiv:2501.03124)](https://arxiv.org/abs/2501.03124)
- [FormalRewardBench (arXiv:2605.10141)](https://arxiv.org/abs/2605.10141)
- [Unsupervised PRM (arXiv:2605.10158)](https://arxiv.org/abs/2605.10158)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make my assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

- [PRM-BiasBench / Reward Under Attack](https://arxiv.org/abs/2603.06621) (arXiv 2026): 直接相关的前序工作。对PRM施加8种表面扰动，发现fluency-logic dissociation（PRMs对rephrasing鲁棒但对语义corruption脆弱）。Section 6的RL hackability分析证明43%的reward gains来自stylistic shortcuts。本proposal声称填补"structural invariance"空白，PRM-BiasBench确实只测试了surface perturbations，未测试数学结构等价变换——这一差异化定位基本成立。

- [reWordBench](https://arxiv.org/abs/2503.11751) (EMNLP 2025): 测试通用RM在meaning-preserving input transformations下的鲁棒性，发现SOTA RMs严重退化甚至低于随机。但目标是response-level general RMs，不是step-level PRMs，且变换类型是surface-level（paraphrasing, typos）而非数学结构等价。Proposal的差异化定位成立。

- [PutnamGAP](https://arxiv.org/abs/2508.08833) (arXiv 2025): 对1,051个Putnam问题施加数学等价变换（surface renames + kernel rewrites），测试LLM solvers。O3在kernel variants上下降~13pp。关键区别：测的是solver而非verifier，且是problem-level而非step-level。Proposal借鉴了变换分类法但应用于不同对象，差异化清晰。

- [GenPRM](https://arxiv.org/abs/2504.00891) (AAAI 2026): 生成式PRM，1.5B模型超越GPT-4o。代码执行理论上对notation invariant（SymPy对'3/4'和'0.75'等价处理）。Proposal正确识别了这一点并计划测试。

- [ThinkPRM](https://arxiv.org/abs/2504.16828) (arXiv 2025): Long-CoT验证，比discriminative PRMs高8%（GPQA-Diamond）。与GenPRM一起构成generative PRM范式的代表。

- [IPT / LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149) (arXiv 2026): 用isomorphic perturbation testing检测RLVR的reward hacking，发现shortcut prevalence随compute增加——inverse scaling。但测试对象是outcome verifiers和solvers，不是step-level PRMs。

- [APRM](https://arxiv.org/abs/2511.22888) (arXiv 2025): 对抗训练PRM，Generator学习产生reasoning errors欺骗PRM。+3.4pp solver accuracy。Proposal正确定位为互补方向（APRM改善error detection，Iso-Aug改善invariance）。

- [CoLD](https://arxiv.org/abs/2507.15698) (arXiv 2025): 因果去偏框架处理PRM的length bias。Proposal计划改编其框架（S→L→P改为S→F→P），技术路线合理但属于直接套用。

- [GR-Ben](https://arxiv.org/abs/2605.01203) (arXiv 2026, May): 将PRM评估扩展到9个非数学推理子领域，22个模型。测试domain generalization breadth，不测invariance。进一步确认structural invariance轴确实未被覆盖。

- [FoVer](https://arxiv.org/abs/2505.15960) (ACL 2026 Findings): 用Z3/Isabelle做PRM训练数据合成。Proposal借鉴其验证方法论。

- 调研总结: PRM评估领域2025-2026高度活跃，已有大量benchmark覆盖error detection (ProcessBench, PRMBench)、surface robustness (PRM-BiasBench)、domain generalization (GR-Ben)、general RM robustness (reWordBench)。数学等价变换测试存在于solver侧(PutnamGAP)和outcome verifier侧(IPT)，但**step-level PRM的structural isomorphism invariance**确实是一个尚未被填补的空白。这一gap是真实的。然而，这是一个"拼图中的最后一块"类型的贡献——gap存在，但gap本身的重要性需要审视。

【Trivial Alternative 检验】:

存在一个需要认真对待的trivial alternative：**直接使用reWordBench的paraphrase-consistency training方法（或其变体），在PRM训练中加入数学等价对作为数据增强，不需要新benchmark**。reWordBench已经证明paraphrase-consistency training可以泛化到其他变换类型。一个自然的问题是：如果对PRM做类似的consistency training（用数学等价变换作为augmentation），是否需要一个专门的benchmark来motivate这件事？

此外，**GenPRM/ThinkPRM可能已经天然解决了这个问题**——proposal自己承认了这一点。如果generative PRMs通过code execution天然具备notation invariance，那么这个benchmark的主要价值缩窄为"量化discriminative PRMs的一个已知弱点"和"给discriminative PRMs做augmentation training"，这显著削弱了significance。

增量价值在于：(1) 系统化地量化这一brittleness的程度和模式（per-transformation, per-depth）；(2) notation gaming attack surface分析是一个有意思的angle；(3) cross-analysis with PRM-BiasBench的二维robustness landscape。但这些更多是分析贡献而非方法论贡献。

【前提假设检验】:

核心逻辑链有几个未经验证的假设：

1. **"Isomorphic brittleness是PRM-guided tree search failure的mechanistic explanation"** — 这是一个大胆的因果主张，但proposal只能提供相关性证据（IIS vs. step depth的相关分析）。Tree search failure可能有很多其他原因（search strategy, reward calibration, error propagation），isomorphic brittleness可能只是其中一个minor factor。Proposal将此作为核心motivation之一，但实际上无法建立因果关系。

2. **"Notation gaming是一个实际存在的reward hacking attack surface"** — Proposal假设solver policy会学到exploit PRM的notation preferences，但这需要policy在RL训练中自发地发现并利用notation变换——这比fluency-based gaming（自然语言的表达偏好更容易被gradient信号捕获）更难实现。Proposal的proof-of-concept是simulate而非demonstrate actual RL-learned notation gaming，说服力有限。

3. **"Discriminative PRMs在structural isomorphism上确实brittle"** — 这是最核心的前提，也是最有可能成立的一个（基于PRM-BiasBench和PutnamGAP的间接证据）。但如果实际测量发现discriminative PRMs在T1-T4上的IIS都很高（比如>0.9），整个project的narrative会显著受损。

4. **"四种变换类型（T1-T4）足以覆盖'structural isomorphism'的主要维度"** — 实际上这四种变换都相当shallow（变量重命名、交换律、表示变换、符号变换），真正深层的structural isomorphism（如proof strategy变换、等价推理路径变换）并未涉及。但这些更深层的变换难以自动验证，所以proposal选择了可验证的子集——这是一个pragmatic trade-off，但也意味着结论的generalizability有限。

【3 维度打分】:

1. **Novelty: 中** — 
   核心novelty claim——"step-level PRM的structural isomorphism invariance测试"——在调研中确认是一个真实的gap。PRM-BiasBench测surface，PutnamGAP测solver，reWordBench测general RM，都没有覆盖step-level PRM的数学结构等价变换。但这个novelty的"质感"更接近"在existing evaluation landscape中填一个空位"，而非"提出一个surprising insight"。四种变换类型（variable renaming, commutative reordering, representation change, notation change）本质上是PutnamGAP变换分类法在verifier侧的直接应用。Iso-Aug方法是CoLD框架的直接改编+reWordBench consistency training思路的结合，方法论novelty有限。Notation gaming attack surface分析是一个有novelty的角度，但proposal将其作为simulation而非实际RL训练中的demonstration。

2. **Significance: 中偏弱** — 
   研究问题本身有一定重要性：PRM作为test-time compute scaling的核心组件，其robustness确实值得系统评估。但significance被几个因素削弱：(a) generative PRMs（GenPRM, ThinkPRM）可能天然解决此问题，而generative PRM是当前的发展方向，使得discriminative PRM的brittleness诊断的时效性存疑；(b) 即使发现brittleness存在，"discriminative PRMs对notation变换不鲁棒"这个结论对大多数reviewer来说可能是"I would have guessed this"——discriminative PRMs做pattern matching而非真正理解数学结构，这已是广泛共识（PRM-BiasBench、Xu et al. 2025都提供了证据）；(c) mitigation方法（Iso-Aug）的贡献更多是engineering而非conceptual——在训练中加入等价变换作为augmentation+consistency loss，这个idea本身不surprising。结果如果是positive，reviewer会说"makes sense"而非"surprising"。

3. **Related Work: 强** — 
   这个proposal对related work的覆盖非常全面且准确。经调研验证：所有引用的论文都真实存在，arXiv IDs正确，描述准确。特别是对PRM-BiasBench、reWordBench、PutnamGAP、IPT、APRM、CoLD等工作的差异化定位清晰且正确。GR-Ben（2605.01203, May 2026）这样非常新的工作也被纳入，说明作者对领域的跟踪非常及时。与每个related work的关系描述（surface vs. structural, solver vs. verifier, response-level vs. step-level）精准。这是proposal最强的维度。

【概率估计】: [20% - 32%] 中位 25%

【估计理由】: 
三个维度综合来看，这是一个"execution-heavy, idea-light"的proposal。Related Work覆盖极其全面（强），说明作者深谙领域，定位精准。Novelty（中）——gap是真实的，但novelty的本质是"在一个已经crowded的evaluation landscape中填补最后一个空位"，而非提出surprising insight。Significance（中偏弱）是主要的上界限制因素：核心发现即使positive（discriminative PRMs确实brittle），reviewer更可能反应"expected"而非"surprising"；generative PRMs可能天然解决此问题进一步削弱motivation；mitigation方法是现有技术的直接组合。

在EMNLP的标准下，benchmark paper需要证明benchmark本身揭示了unexpected phenomenon或enables new research direction。本proposal更接近"系统性确认一个widely-expected weakness"。Notation gaming angle有一定新意但只是simulation。上界被significance限制在~32%；下界~20%因为execution质量高、定位精准，不至于被直接desk-reject。

【主要风险】: 
1. **"Expected results" 风险**: 核心发现（discriminative PRMs对数学等价变换brittle）对多数reviewer来说可能是预期内的结论，缺乏surprise value。审稿人可能评价"confirms what we already suspected but doesn't tell us something new"。
2. **Generative PRM neutralization风险**: 如果GenPRM/ThinkPRM在测试中表现出高invariance，这既是proposal预期的结果之一，也同时削弱了整个研究方向的urgency——"we built a benchmark that shows the old paradigm has a problem that the new paradigm already solves"。
```

Sources:
- [PRM-BiasBench: Reward Under Attack](https://arxiv.org/abs/2603.06621)
- [reWordBench: Benchmarking and Improving RM Robustness](https://arxiv.org/abs/2503.11751)
- [PutnamGAP: Mathematically-Equivalent Transformations](https://arxiv.org/abs/2508.08833)
- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [IPT / LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149)
- [APRM: Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)
- [CoLD: Counterfactual Length Debiasing for PRMs](https://arxiv.org/abs/2507.15698)
- [GR-Ben: General Reasoning Benchmark for PRMs](https://arxiv.org/abs/2605.01203)
- [FoVer: Efficient PRM Training Data via Formal Verification](https://arxiv.org/abs/2505.15960)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [PRM-BiasBench / Reward Under Attack] (arXiv:2603.06621, Feb 2026): 最直接的竞争工作。对 PRM 施加 8 种 surface perturbation（rephrasing、verbosity 等），发现 fluency-logic dissociation：PRMs 对 rephrasing 鲁棒（|ΔR|<0.03）但对 semantic corruption 脆弱。Section 6 的 RL hackability 实验（>0.9 PRM rewards with <4% accuracy, 43% reward gains from stylistic shortcuts）是本 proposal notation gaming 分析的直接灵感来源。关键区别：PRM-BiasBench 测的是 surface-level perturbation，本 proposal 声称测的是 structural-level isomorphism——但这个区别的实质深度需要审视。
- [reWordBench] (EMNLP 2025, arXiv:2503.11751): 对通用 reward model 施加 meaning-preserving 输入变换（punctuation、paraphrasing、code minification），发现 SOTA RMs 在某些变换下降到 below-random accuracy。提出 paraphrase-consistency training。区别：response-level general RMs vs. step-level PRMs；surface transformations vs. structural isomorphisms。
- [PutnamGAP] (arXiv:2508.08833): 对 1,051 道 Putnam 题生成数学等价变体（4 种 surface renames + kernel rewrite），测试 LLM solvers。O3 在 kernel variants 上掉 ~12.9pp。关键区别：测 solver 不测 verifier，测 problem level 不测 step level。
- [IPT / LLMs Gaming Verifiers] (arXiv:2604.15149, Apr 2026): 提出 Isomorphic Perturbation Testing 检测 RLVR 中的 reward hacking，发现 shortcut prevalence 随 complexity 和 compute 增加。区别：测 RLVR outcome verifiers，不测 PRM step-level verifiers。
- [GR-Ben] (arXiv:2605.01203, May 2026): 将 PRM 评估扩展到 9 个非数学 subdomain（science + logic），22 个模型。测 domain generalization breadth，不测 invariance。
- [APRM] (arXiv:2511.22888): 对抗训练 PRM，Generator 学习生成错误推理步骤来欺骗 PRM。+3.4pp solver accuracy, +5.3pp OOD。与本 proposal 的 Iso-Aug 互补：APRM 提高 error detection robustness，Iso-Aug 提高 invariance to correct reformulations。
- [CoLD] (arXiv:2507.15698): 因果去偏框架解决 PRM 的 length bias。本 proposal 声称将 S→L→P 替换为 S→F→P（serialization format）来适配。
- [PRMBench] (ACL 2025, arXiv:2501.03124): 多维 PRM 评估，包括 sensitivity 和 consistency，但不含 structural isomorphism。
- [Socratic-PRMBench] (arXiv:2505.23474): 6 种推理模式下的 PRM 评估，不涉及 invariance testing。
- [FoVer] (ACL 2026 Findings, arXiv:2505.15960): Z3/Isabelle 用于 PRM 训练数据合成，85.8% AUROC on ProcessBench。本 proposal 复用类似的 formal verification pipeline。
- [GenPRM] (AAAI 2026, arXiv:2504.00891): Code-based generative PRM，1.5B 模型超越 GPT-4o。Code execution 可能天然具有 notation invariance（SymPy 对 '3/4' 和 '0.75' 处理一致）。
- [ThinkPRM] (arXiv:2504.16828): Long-CoT verification，比 discriminative PRMs 高 8% on GPQA-Diamond。

- 调研总结: PRM 评估/鲁棒性是一个高度活跃且日益拥挤的领域。2025-2026 年已出现大量 PRM benchmark（ProcessBench、PRMBench、Socratic-PRMBench、GR-Ben、PRM-BiasBench、ToolPRMBench 等），各自覆盖不同维度。本 proposal 定位在"step-level structural isomorphism invariance"这一尚未被直接占据的细分空间，但该空间是已有工作（PRM-BiasBench 的 surface perturbation + PutnamGAP 的 mathematical equivalence + IPT 的 isomorphic testing）的自然交叉延伸。

【Trivial Alternative 检验】:
最直接的 trivial alternative：直接复用 PRM-BiasBench 的 framework，将其 8 种 surface perturbation 替换为 4 种 structural isomorphism（variable renaming 等），即可基本达到同样的 benchmark 目标。PRM-BiasBench 已经提供了 ProcessBench 上的评估 pipeline、cross-model comparison methodology、甚至 RL hackability analysis framework。本 proposal 的增量价值需要回答：为什么不能简单地在 PRM-BiasBench 的框架上加 4 个 transformation type 作为一个 follow-up experiment？

Proposal 的增量价值主要在于：(1) formal verification pipeline（SymPy + Z3）确保变换的数学正确性，这比 PRM-BiasBench 的 surface perturbation 需要更严格的验证；(2) step-level 而非 response-level 的粒度；(3) cross-paradigm comparison（discriminative vs. generative PRMs）在 isomorphism 维度上的对比。但这些增量是否足以构成独立贡献而非 PRM-BiasBench 的扩展实验，存在争议。

对于 Iso-Aug：consistency regularization on isomorphic pairs（L = Σ(r(xi)−r(xj))²）是标准的 consistency training。reWordBench 已经提出了 paraphrase-consistency training 且证明它泛化到其他 transformation types。Iso-Aug 与 reWordBench 的方法论差异仅在于 augmentation 的数据来源（structural isomorphisms vs. paraphrases）和应用目标（PRMs vs. general RMs）。这是一个 incremental adaptation，不是方法论创新。

结论：存在较强的 trivial alternative 威胁。核心 benchmark 贡献可以被视为 PRM-BiasBench 的自然扩展；Iso-Aug 可以被视为 reWordBench consistency training 的直接迁移。增量价值真实存在（formal verification、step-level 粒度、paradigm comparison），但深度有限。

【前提假设检验】:
核心 claim 的逻辑链有以下未经验证的假设：

1. **"Isomorphic brittleness 是一个真实且严重的问题"** — PRM-BiasBench 已经表明 PRMs 对 rephrasing 其实是 robust 的（|ΔR|<0.03）。如果 PRMs 对 surface-level rephrasing 鲁棒，那么对 structural isomorphisms（variable renaming、commutative reordering）是否也可能是鲁棒的？特别是 T1（variable renaming）和 T2（commutative reordering）是非常基本的变换，训练数据中可能已经包含了大量此类变体。这个假设如果不成立（即 PRMs 在 isomorphism 维度上已经足够 robust），整个 benchmark 的价值大幅缩水——虽然 proposal 有 "generative PRM trajectory" 的 hedge，但一个"大部分模型都 pass"的 benchmark 在审稿人眼中价值有限。

2. **"Isomorphic brittleness 可以解释 tree search failure"** — Proposal 引用 arXiv:2510.20272 指出 PRM-guided tree search 不如 simple best-of-N，并推测 isomorphic brittleness compounding across steps 是原因之一。但这是一个未经验证的因果推断。Tree search failure 可能有多种原因（score miscalibration、distribution shift、search algorithm issues），isomorphic brittleness 是否是 dominant factor 完全未知。

3. **"Notation gaming 是一个比 fluency gaming 更深层的攻击面"** — Proposal 声称 notation gaming "harder to detect because the output contains valid mathematical content"。但 PRM-BiasBench 的 fluency gaming 已经使用了 valid language content（只是 style 不同），notation gaming 并不必然"更深"——它只是在不同的 surface 维度上。而且 proposal 只做 simulation（重写 notation 后看 score 变化），不做真实 RL 训练，这比 PRM-BiasBench 的实际 GRPO 实验弱了一个量级。

4. **T3/T4 变换的覆盖率足以支撑统计结论** — Proposal 估计 T3 ~45-55%、T4 ~35-45%，在某些子集（OlympiadBench T4 ~30%、Omni-MATH T4 ~25%）覆盖率较低。虽然 proposal 承诺用 AMC/AIME 补充，但这引入了 distribution shift（ProcessBench 的 annotation 不再适用于补充数据）。

【3 维度打分】:

1. **Novelty: 弱-中** — 
   Gap 是真实的：确实没有工作在 step level 测试 PRMs 的 structural isomorphism invariance。但这个 gap 是高度可预测的组合式创新：PRM-BiasBench 的 perturbation framework + PutnamGAP 的 mathematical equivalence taxonomy + IPT 的 isomorphic testing idea → 自然得出"对 PRMs 做 step-level structural isomorphism testing"。四种 transformation types（variable renaming、commutative reordering、representation change、notation change）都是标准的数学等价变换，无方法论创新。Iso-Aug 是 reWordBench consistency training + CoLD causal debiasing 的直接拼接。如果核心发现是 "PRMs are brittle to isomorphisms"，审稿人很可能反应是 "I would have guessed this, given PRM-BiasBench's findings on surface brittleness"。如果发现是 "PRMs are robust"，则 benchmark 价值更低。唯一可能产生 surprise 的是跨 paradigm 的差异幅度（discriminative vs. generative），但这依赖实验结果而非 idea 本身。

2. **Significance: 中** — 
   研究问题本身是重要的：PRM 是 test-time compute scaling 的核心组件，其 robustness 直接影响 deployment 可靠性。PRM 评估领域确实需要更全面的 robustness 测试。但重要性被两个因素削弱：(a) PRM-BiasBench 已经在 surface robustness 维度上做了类似的工作，且其 RL hackability 分析更有深度（真实 GRPO 训练 vs. 本 proposal 的 simulation）；(b) 如果 generative PRMs（GenPRM、ThinkPRM）确实天然具有 isomorphic robustness（code execution inherently notation-invariant），那么这个问题在未来可能自然消解，benchmark 的长期影响力有限——proposal 虽然 argue "discriminative PRMs remain dominant in latency-sensitive deployment"，但这个论点在 generative PRMs 快速发展的背景下不确定性很高。

3. **Related Work: 强** — 
   Related work 覆盖极其全面，差异化定位清晰。Proposal 准确地定位了自己相对于 PRM-BiasBench（surface vs. structural）、reWordBench（response-level general RMs vs. step-level PRMs）、PutnamGAP（solver vs. verifier）、IPT（outcome vs. step-level）的差异。对 APRM 的互补性分析（error detection vs. invariance）也到位。所引用的论文全部真实存在且描述准确。这是 proposal 最强的维度。

【概率估计】: [22% - 32%] 中位 26%

【估计理由】: 
Related Work 维度是强，但 Related Work 好只是论文的必要条件而非 idea 质量的指标。Novelty 处于弱-中之间——gap 真实但创新是组合式的、可预测的，核心贡献（benchmark + 标准 mitigation）缺乏方法论深度。Significance 处于中——问题重要但 expected findings 不够 surprising，且与 PRM-BiasBench 有较强的增量性质关系。

上界受限于 **Novelty**：这本质上是一个"在已有框架上换一组 perturbation types"的工作，即使执行完美，审稿人也很可能认为贡献增量不足以独立成篇——特别是在 PRM benchmark 已经高度饱和的 2026 年中期。下界由 Related Work 的扎实覆盖和问题的真实重要性托底，不太可能被完全否定。

【主要风险】:
1. **"Incremental over PRM-BiasBench" rejection**: 最大风险。审稿人很可能认为这是 PRM-BiasBench 加了 4 个新 perturbation type + formal verification pipeline 的 extension work，novelty 不够 standalone paper。PRM-BiasBench 已建立了 PRM robustness benchmarking 的 paradigm，本工作在同一 paradigm 内做细化。
2. **结果可预测性**: 如果 discriminative PRMs brittle（预期内）而 generative PRMs robust（也在预期内，因为 code execution inherently invariant），整篇论文的发现不会让审稿人感到 surprised。最 interesting 的可能发现（e.g., certain PRMs robust to T1/T2 but catastrophically brittle to T3/T4, or brittleness anti-correlates with surface robustness）依赖实验结果，不是 idea 层面能保证的。
```

Sources:
- [PRM-BiasBench: Reward Under Attack](https://arxiv.org/abs/2603.06621)
- [reWordBench: Benchmarking and Improving the Robustness of Reward Models](https://arxiv.org/abs/2503.11751)
- [PutnamGAP: An Investigation of Robustness via Mathematically-Equivalent Transformations](https://arxiv.org/abs/2508.08833)
- [IPT / LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)
- [GR-Ben: A General Reasoning Benchmark for Evaluating PRMs](https://arxiv.org/abs/2605.01203)
- [APRM: Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)
- [CoLD: Counterfactually-Guided Length Debiasing for PRMs](https://arxiv.org/abs/2507.15698)
- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [PRMBench: Fine-grained and Challenging Benchmark for PRMs](https://arxiv.org/abs/2501.03124)
- [Socratic-PRMBench: Benchmarking PRMs with Systematic Reasoning Patterns](https://arxiv.org/abs/2505.23474)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [ProcessBench: Identifying Process Errors in Mathematical Reasoning](https://arxiv.org/abs/2412.06559)


【原始 proposal（允许参考但不是主要依据）】:
# IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models

## Description
We propose IsoPRM-Bench, the first benchmark testing whether Process Reward Models maintain consistent scores across structurally isomorphic reasoning steps, paired with Iso-Aug, a mitigation method based on isomorphic augmentation with consistency regularization. While PRM-BiasBench tests surface perturbations (rephrasing, verbosity), reWordBench tests meaning-preserving transformations on general RMs at response level, PutnamGAP tests equivalent transformations on LLM solvers, GR-Ben extends PRM evaluation to 9 non-mathematical reasoning subdomains, and APRM improves error detection via adversarial training, no existing work tests step-level structural invariance of PRM verifiers — whether a PRM scores logically equivalent steps identically when their mathematical realization differs. Starting from ProcessBench's 3,400 human-annotated solutions (GSM8K: 400, MATH: 1,000, OlympiadBench: 1,000, Omni-MATH: 1,000), we generate isomorphic variants across four formally verifiable transformation types (variable renaming, commutative reordering, representation change, notation change) with a three-tier verification pipeline (SymPy, Z3, human audit). We explicitly quantify per-transformation coverage: T1/T2 apply broadly (~60-75% of steps), while T3/T4 require specific mathematical content (~35-55%), with coverage validated via a 100-solution pilot annotation and supplemented by AMC/AIME solutions if needed. We evaluate PRMs spanning three paradigms — discriminative (Qwen2.5-Math-PRM-72B/7B, Math-Shepherd), generative-CoT (ThinkPRM), and generative-code (GenPRM) — using an Isomorphic Invariance Score (IIS). Crucially, we cross-analyze IIS with PRM-BiasBench's surface robustness to map the two-dimensional robustness landscape. For mitigation, we adapt CoLD's causal debiasing framework to fine-tune Qwen2.5-Math-PRM-7B with isomorphic augmentation and consistency regularization, positioning Iso-Aug as complementary to APRM's adversarial training (which improves error detection robustness via novel negative generation, while Iso-Aug improves invariance across valid reformulations). Our analysis targets five key findings: (1) anti-correlated model-specific blind spots across transformation types, (2) whether generative PRMs show inherent isomorphic robustness — and if so, quantifying the paradigm gap to inform deployment decisions between latency-sensitive discriminative PRMs and invariance-superior generative PRMs, (3) whether brittleness increases with step depth (explaining tree search failure), (4) the practical impact on best-of-N selection with diverse reasoning strategies, and (5) a notation gaming attack surface analysis demonstrating how a policy can exploit PRM notation preferences to inflate scores without improving reasoning — analogous to but structurally deeper than PRM-BiasBench's finding that 43% of RL reward gains come from fluency-based stylistic shortcuts. We explicitly address the generative PRM trajectory: even if GenPRM/ThinkPRM pass invariance tests, the benchmark quantifies the paradigm robustness gap for deployment decisions, provides Iso-Aug training signal to improve latency-efficient discriminative PRMs, and establishes isomorphic invariance as a standard evaluation dimension. We adopt a two-phase submission strategy: benchmark-focused for AAAI 2027 (Jul 28; human-in-loop mode, 8-10 weeks), with full Iso-Aug + APRM composition for ICLR 2027 backup (~Oct 2026). This work bridges the gap between outcome-level robustness testing (IPT, PutnamGAP) and step-level verification, with direct implications for PRM-guided test-time compute scaling and reward hacking prevention.

## Core Problem
Process Reward Models are deployed to guide test-time compute scaling (best-of-N, tree search), yet no existing evaluation tests whether PRMs maintain consistent scores across structurally isomorphic reasoning — the same logical derivation with different surface realizations. This is the critical test of whether PRMs verify reasoning structure or pattern-match surface forms, and directly determines whether PRM-guided search can benefit from diverse solution strategies. Moreover, this brittleness creates a concrete reward hacking attack surface: a solver policy trained with PRM-guided RLHF/RLVR can learn to exploit the verifier's notation preferences — expressing intermediate steps in PRM-favored surface forms (e.g., decimals over equivalent fractions, expanded over factored polynomials) to inflate scores without improving reasoning quality. This is analogous to PRM-BiasBench's fluency-based gaming but operates at the structural mathematical level, making it harder to detect because the output contains valid mathematical content.

## Opportunity
Existing PRM benchmarks form a hierarchy: error detection (ProcessBench, PRMBench), domain generalization (GR-Ben), surface robustness (PRM-BiasBench), and domain transfer (UniversalBench, ToolPRMBench). No benchmark tests structural invariance — whether a PRM scores logically equivalent steps identically when their mathematical realization differs. reWordBench (EMNLP 2025) tests general RM robustness via meaning-preserving input transformations (paraphrasing, typos, code minification), finding RMs drop to below-random accuracy, but targets response-level general RMs rather than step-level PRMs. PutnamGAP (arXiv:2508.08833) tests mathematically equivalent transformations but targets LLM solvers at the problem level, not PRM verifiers at the step level. PRM-BiasBench finds PRMs are invariant to shallow style changes but inconsistent on semantic corruption — a fluency-logic dissociation. Xu et al. (2025) show PRMs identify consistency not causality, with problem-statement removal causing only 0.4-point drops. Meanwhile, PRM-guided tree search fails to outperform simple best-of-N (arXiv:2510.20272), with PRM reliability degrading at depth — a failure potentially rooted in isomorphic brittleness compounding across search steps. Critically, PRM-BiasBench's Section 6 RL hackability analysis demonstrates the concrete danger of PRM brittleness: policies trained with GRPO achieve near-perfect PRM rewards (>0.9) while ground-truth accuracy remains below 4%, with a rephrasing intervention revealing that 43% of reward gains are attributable to stylistic shortcuts rather than reasoning improvement (reward drops from 0.641 to 0.472 under semantics-preserving rephrasing). Isomorphic brittleness opens an analogous but deeper attack surface: notation gaming exploits PRM preferences over logically equivalent mathematical representations — producing outputs with valid mathematical content optimized for score inflation, which is harder to detect than the fluency-based gaming (performative complexity, vacuous safety) identified by PRM-BiasBench. We fill the structural invariance gap at the process level, complementing PutnamGAP's solver-level testing, PRM-BiasBench's surface-level testing, and reWordBench's response-level general RM testing, while also providing a mitigation pathway through isomorphic augmentation training.

## Landscape
reWordBench (EMNLP 2025, arXiv:2503.11751) applies meaning-preserving input transformations — controlled (punctuation, quotation marks), naturalistic (character swaps, paraphrasing), and domain-specific (code minification) — to general reward models, finding state-of-the-art RMs suffer substantial degradation including below-random accuracy on some transformations; they propose paraphrase-consistency training that generalizes to other transformation types. Crucially, reWordBench targets response-level general RMs with surface-preserving transformations, while we target step-level PRMs with structural isomorphisms that preserve mathematical content but change its formal realization — a deeper invariance axis. PRM-BiasBench (arXiv:2603.06621) applies 8 surface perturbation types and finds a fluency-logic dissociation: PRMs are robust to rephrasing (|ΔR|<0.03) but fail on semantic corruption; code and data at github.com/SqueezeAILab/reward-under-attack. ProcessBench (arXiv:2412.06559) evaluates step-level error detection across 3,400 problems with fixed formulations. PRMBench (ACL 2025, arXiv:2501.03124) tests multi-dimensional PRM capabilities including sensitivity and consistency but not structural isomorphism. Socratic-PRMBench (arXiv:2505.23474) benchmarks across six reasoning patterns but never compares two correct reformulations of the same step. GR-Ben (arXiv:2605.01203, May 2026) extends PRM evaluation to general reasoning across 2 primary domains (science and logic) and 9 subdomains with 22 models, finding existing PRMs score markedly lower on non-mathematical domains; it tests domain generalization breadth but not invariance or robustness within any single domain, and its emergence further demonstrates the field's continued production of PRM benchmarks while the structural invariance axis remains untested. PutnamGAP (arXiv:2508.08833) applies mathematically equivalent transformations (4 surface renames + kernel rewrites) to 1,051 Putnam problems but tests only LLM solvers, finding kernel variants cause ~10+ pp accuracy drops even on O3; the solver-verifier distinction is critical since PRM brittleness corrupts the training signal, not just benchmark scores. IPT (arXiv:2604.15149) tests RLVR outcome verifiers via isomorphic tasks, finding RLVR-trained models systematically fail invariance with more compute producing more shortcuts — an inverse scaling result. APRM (arXiv:2511.22888) proposes adversarial training for PRMs via a two-player game where a Generator learns to produce plausible reasoning errors while the PRM learns to detect them, yielding +3.4pp solver accuracy and +5.3pp on OOD tasks over the strongest PRM baseline; APRM improves error detection robustness via adversarial negatives, which is complementary to our Iso-Aug that improves invariance to correct reformulations via isomorphic augmentation — adversarial training and consistency training address orthogonal failure modes (missing true errors vs. inconsistent scoring of valid steps). BiPRM (arXiv:2508.01682) improves step estimation via bidirectional context. FoVer (arXiv:2505.15960, ACL 2026 Findings) uses Z3/Isabelle for PRM data synthesis, achieving 85.8% AUROC on ProcessBench, but limited to first-order logic domains. GenPRM (arXiv:2504.00891) redefines process verification as generative with code execution, where a 1.5B model outperforms GPT-4o — suggesting code-based verification may be inherently more isomorphism-invariant. ThinkPRM (arXiv:2504.16828) uses long-CoT verification outperforming discriminative PRMs by 8% on GPQA-Diamond. CoLD (arXiv:2507.15698) addresses length bias via counterfactual debiasing with a causal graph framework (S→L→P spurious pathway), directly adaptable to isomorphic invariance (replace length with serialization format). Crome (arXiv:2506.16507, ICML 2025) uses causal + neutral augmentations for RM robustness, achieving 5.4% accuracy gains and 9.1% robustness gains. The Robust Reasoning Benchmark (arXiv:2604.08571) applies 14 perturbation techniques to AIME problems but targets solvers. No work combines step-level structural isomorphism testing of PRMs with a mitigation pathway via invariance training, nor demonstrates how isomorphic brittleness creates a concrete notation gaming reward hacking attack surface.

## Approach
We propose a two-part contribution: (1) IsoPRM-Bench, a benchmark for structural isomorphism invariance of PRMs, and (2) Iso-Aug, a mitigation method using isomorphic augmentation with consistency regularization.

**Part 1: IsoPRM-Bench.** Starting from ProcessBench's 3,400 human-annotated step-level math solutions (GSM8K: 400, MATH: 1,000, OlympiadBench: 1,000, Omni-MATH: 1,000), we generate structurally isomorphic variants of each reasoning step across four transformation types with provable symbolic equivalence: (T1) variable renaming — systematic substitution of variable symbols while preserving all relational structure; (T2) commutative operation reordering — reordering addition/multiplication operands and equation sides; (T3) representation change — arithmetic ↔ algebraic, e.g., '3+5=8' ↔ 'x+y=z where x=3,y=5,z=8'; (T4) notation change — fraction ↔ decimal ↔ scientific notation ↔ expanded/factored polynomial forms.

**T3/T4 Coverage Analysis.** Not all ProcessBench steps are amenable to all four transformations. We estimate per-subset applicability based on mathematical content requirements: T1 (variable renaming) applies to ~65-75% of steps (any step referencing named variables; lower in GSM8K's prose-style ~50%, higher in MATH/OlympiadBench/Omni-MATH ~70-85%); T2 (commutative reordering) applies to ~60-70% (any step with addition, multiplication, or equalities); T3 (representation change) applies to ~45-55% (requires explicit arithmetic computations or algebraic formulations — high in GSM8K ~75% and MATH algebra subsets ~55%, lower in OlympiadBench ~40% and Omni-MATH ~35% due to more abstract proof-style reasoning); T4 (notation change) applies to ~35-45% (requires fractions, decimals, percentages, or polynomial expressions — moderate in GSM8K ~55% and MATH ~45%, lower in OlympiadBench ~30% and Omni-MATH ~25%). We will validate these estimates via a pilot annotation of 100 randomly sampled ProcessBench solutions (25 per subset) before full-scale generation, reporting exact applicability rates. Even at the conservative lower bound, T4 yields ~1,200+ applicable step instances — statistically sufficient for per-model and per-transformation-type analysis. The uneven coverage is itself informative: it reveals which math domains and difficulty levels are most affected by notation sensitivity, and we will report transformation-type × subset breakdowns. If T4 coverage falls below 30% in OlympiadBench/Omni-MATH, we will supplement with 200 additional solutions from AIME/AMC competition problems (rich in notation-heavy content) generated and annotated using the same pipeline.

We deliberately restrict to transformations with automated formal verification: T1-T2 via direct AST manipulation, T3-T4 via SymPy symbolic equivalence and Z3 SMT solving (following FoVer's demonstrated approach). We drop 'equivalent natural-language reformulation' from the taxonomy because it overlaps with PRM-BiasBench's rephrasing perturbation and reWordBench's paraphrasing transformations, and lacks reliable automated verification. Variants are generated via Claude Sonnet 4.6 with constrained prompting, followed by a three-tier verification pipeline: (i) symbolic CAS equivalence check via SymPy, (ii) SMT satisfiability check via Z3 for first-order logic reformulations, (iii) human spot-verification on a 15% stratified sample (stratified by transformation type, difficulty, and subset). We evaluate state-of-the-art PRMs spanning three paradigms — discriminative (Qwen2.5-Math-PRM-72B, Qwen2.5-Math-PRM-7B, Math-Shepherd), generative-CoT (ThinkPRM), and generative-code (GenPRM-7B) — computing an Isomorphic Invariance Score (IIS = 1 − normalized score variance across isomorphic variants) per step, per transformation type, and per step position. We cross-analyze IIS with PRM-BiasBench's surface perturbation scores to test orthogonality: can a PRM be robust to style changes but brittle to structural isomorphism?

**Part 2: Iso-Aug Mitigation.** We adapt CoLD's causal debiasing framework by replacing the spurious pathway S→L→P (length) with S→F→P (serialization format). Concretely, we fine-tune Qwen2.5-Math-PRM-7B using LoRA with three components: (a) isomorphic augmentation — for each training step, generate 2-3 isomorphic variants using our T1-T4 pipeline, labeled identically to the original; (b) consistency regularization loss — L_consistency = Σ(r(x_i) − r(x_j))² across all isomorphic pairs (i,j), added to the standard BCE loss; (c) bias estimator module — a parallel network trained to capture serialization-dependent signals (following CoLD's joint training), with complementary correlation constraints forcing the PRM to decorrelate from format while the estimator absorbs format artifacts. Training uses Axolotl framework with native PRM support. We position Iso-Aug as complementary to APRM's adversarial training: APRM improves robustness to novel errors (error detection), while Iso-Aug improves invariance across valid reformulations (score consistency) — these address orthogonal PRM failure modes and could potentially be composed. We then re-evaluate the fine-tuned model on IsoPRM-Bench and on ProcessBench (to verify no accuracy regression).

**Analysis.** Beyond aggregate IIS, we report: (i) transformation-type breakdown — which isomorphisms each PRM is most/least robust to, with T3/T4 applicability rates per subset explicitly reported; (ii) model-paradigm comparison — whether generative PRMs (code-based GenPRM) show inherent isomorphic robustness vs. discriminative PRMs; (iii) step-position analysis — whether isomorphic brittleness increases with step depth, explaining tree search reliability degradation; (iv) orthogonality matrix — cross-tabulating IIS with PRM-BiasBench's surface robustness to map the two-dimensional robustness landscape; (v) practical impact — measuring how IIS correlates with best-of-N selection accuracy on MATH-500 when candidate solutions use diverse strategies; (vi) notation gaming attack surface — we construct a proof-of-concept demonstrating how isomorphic brittleness enables reward hacking. Using our per-transformation IIS scores, we identify each evaluated PRM's strongest notation preferences (e.g., if a PRM systematically scores decimal representations 0.1+ higher than equivalent fractions, or prefers expanded polynomial forms over factored forms). We then simulate a notation-gaming policy that, during PRM-guided best-of-N selection on MATH-500, reformulates its candidate solutions' reasoning steps into the PRM-preferred notation at each step using our T1-T4 pipeline. We measure the resulting score inflation (Δ reward) and selection accuracy change relative to notation-neutral baselines, and compare the magnitude of notation gaming gains to PRM-BiasBench's finding that 43% of RL reward gains are attributable to stylistic shortcuts (Section 6.3: rephrasing intervention shows reward drops from 0.641 to 0.472 under semantics-preserving rephrasing). This directly demonstrates the reward hacking attack surface: a policy need not improve its reasoning to achieve higher PRM scores — it need only learn the verifier's notation preferences. Unlike PRM-BiasBench's fluency-based gaming (Skywork's performative complexity via elaborate but flawed reasoning, Qwen's vacuous safety via minimal substance), notation gaming is harder to detect because the output contains valid mathematical content expressed in a legitimately equivalent form, and it compounds across search depth — each step's notation choice independently inflates the cumulative score, potentially explaining why PRM-guided tree search degrades at depth (arXiv:2510.20272).

**Generative PRM Trajectory.** We explicitly address the scenario where generative PRMs (GenPRM, ThinkPRM) demonstrate substantial isomorphic invariance, which is plausible given GenPRM's code-based verification (code execution is inherently notation-invariant since SymPy evaluates '3/4' and '0.75' identically) and ThinkPRM's explicit CoT reasoning before scoring. Even in this outcome, IsoPRM-Bench provides three critical contributions: (a) quantifying the paradigm robustness gap gives the field concrete evidence for when generative PRMs' 10-100x inference cost premium is justified by their invariance properties, informing the architecture-vs-cost tradeoff in deployment decisions; (b) discriminative PRMs remain dominant in latency-sensitive deployment — real-time search guidance during tree search and high-throughput RLHF training loops where per-step generative verification is prohibitively expensive — and Iso-Aug provides the training signal to improve these cost-efficient models toward generative-level invariance without the inference overhead; (c) establishing isomorphic invariance as a standard evaluation dimension for future PRMs, analogous to how fairness benchmarks became standard evaluation axes even as models improved on them, ensures the field systematically tracks this property as PRM architectures evolve.

**Timeline Contingency.** Given the AAAI 2027 deadline (Jul 28, 2026; 10 weeks from today) and the tight margin with our estimated timeline, we adopt a two-phase submission strategy: *Phase 1 (AAAI target):* Submit IsoPRM-Bench as a benchmark paper, prioritizing the benchmark construction (T1-T4 pipeline + verification), PRM evaluation across all 5 models, and the analysis components (i)-(vi). The Iso-Aug mitigation is presented as a preliminary experiment with LoRA fine-tuning on Qwen2.5-Math-PRM-7B, showing proof-of-concept IIS improvement. This phase uses the human-in-loop mode (8-10 weeks) with API-assisted generation to compress the timeline. The pilot annotation of 100 solutions for T3/T4 coverage validation is completed in week 1 to derisk. *Phase 2 (ICLR 2027 backup, expected ~Oct 2026):* If AAAI reviews suggest the mitigation needs fuller treatment, or if we miss the AAAI deadline, the ICLR submission includes the complete Iso-Aug with full ablations (component-wise contribution of augmentation, consistency loss, and bias estimator), APRM+Iso-Aug composition experiments, and extended analysis on supplementary competition problem datasets. The 4-5 additional weeks to ICLR allow the mitigation results to fully mature.

## Resource Estimate
{'manual': {'gpu_hours': '400-600 (72B PRM inference: ~160h; 7B models ×3: ~90h; GenPRM/ThinkPRM inference: ~80h; Iso-Aug fine-tuning with LoRA: ~40h; variant generation with local LLMs: ~100h; ablations: ~80h)', 'timeline': '10-12 weeks (2w taxonomy + pipeline + verification + T3/T4 pilot, 2.5w data generation + three-tier QC, 2w PRM evaluation across 5 models × 3 paradigms, 1.5w Iso-Aug training + re-evaluation, 2w analysis + writing)', 'estimated_gpu_cost': '$800-1200 at ~$2/H100-hr'}, 'human_in_loop': {'gpu_hours': '300-450 (API-based generation eliminates local LLM GPU; 72B PRM inference: ~160h; other models: ~100h; Iso-Aug LoRA fine-tuning: ~40h; ablations: ~50h)', 'timeline': '8-10 weeks (1w taxonomy + pipeline + T3/T4 pilot annotation, 2w API-assisted generation + verification, 2w evaluation, 1w Iso-Aug training, 1.5w analysis + writing, 0.5w buffer)', 'claude_api_cost': '$500-900 (variant generation: ~100M tokens I/O via Sonnet at $3/$15 per MTok ≈ $600; verification + code assistance: ~$250)', 'estimated_gpu_cost': '$600-900'}, 'auto_research': {'gpu_hours': '200-350 (fully batched PRM inference + LoRA fine-tuning only; no local generation)', 'timeline': '6-8 weeks (1w automated pipeline build + T3/T4 pilot, 1.5w generation + automated three-tier QC, 1.5w evaluation, 1w Iso-Aug training, 1w analysis + writing)', 'claude_api_cost': '$900-1400 (heavier API generation with multi-pass quality filtering: ~$800; automated analysis + writing: ~$500)', 'estimated_gpu_cost': '$400-700', 'speed_bottleneck': 'Human validation of isomorphic correctness in the 15% spot-check sample; Z3/SymPy cover T1-T4 transformations with >95% automated verification, but edge cases in representation change (T3) require manual audit'}}

## Inspired By
Cross-domain transfer: IPT methodology (arXiv:2604.15149) from RLVR outcome verification → PRM step-level verification; PutnamGAP transformation taxonomy (arXiv:2508.08833) from solver testing → verifier testing; CoLD causal debiasing framework (arXiv:2507.15698) from length bias → isomorphism bias; Crome neutral augmentations (arXiv:2506.16507) from general RM robustness → PRM structural invariance; reWordBench paraphrase-consistency training (arXiv:2503.11751) from response-level general RM → step-level PRM; APRM adversarial training (arXiv:2511.22888) as complementary robustness axis to our consistency-based approach; Field guide gap: PRMs detect fluency not reasoning (PRM-BiasBench Section 3.3); Tree search failure diagnosis: PRM reliability degradation at depth (arXiv:2510.20272) may be explained by compounding isomorphic brittleness; Reward hacking diagnosis: PRM-BiasBench Section 6 RL hackability analysis — policies achieve >0.9 PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts (rephrasing intervention: 0.641→0.472) — motivates our notation gaming attack surface analysis as a concrete demonstration that isomorphic brittleness creates an exploitable reward hacking vector at the structural mathematical level, deeper than the fluency-based gaming (performative complexity, vacuous safety) they identify

## Target Venues
- AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target with benchmark-focused submission; 10 weeks from today, feasible with human-in-loop mode at 8-10 weeks; Iso-Aug presented as preliminary experiment)
- ICLR 2027 (deadline expected ~Sep-Oct 2026 — backup target with full Iso-Aug results, APRM+Iso-Aug composition experiments, and extended analysis; 4-5 extra weeks allow mitigation to fully mature)
- NeurIPS 2027 (deadline expected ~May 2027 — fallback if major revisions needed after AAAI/ICLR reviews)

## Key References
- reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs (EMNLP 2025, arXiv 2503.11751) — response-level general RM robustness via meaning-preserving transformations; paraphrase-consistency training; we extend the invariance-testing paradigm to step-level PRMs with structural (not surface) isomorphisms
- Adversarial Training for Process Reward Models (arXiv 2025, 2511.22888) — adversarial Generator-PRM game for error detection robustness, +3.4pp solver accuracy; complementary to our Iso-Aug which addresses invariance to correct reformulations rather than robustness to novel errors
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv 2026, 2604.15149) — IPT methodology transferred to our step-level PRM testing
- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv 2026, 2603.06621) — fluency-logic dissociation, orthogonal robustness axis, model-specific blind spots; Section 6 RL hackability analysis shows >0.9 PRM rewards with <4% accuracy and 43% of reward gains from stylistic shortcuts, directly motivating our notation gaming analysis
- PutnamGAP: An Investigation of Robustness via Mathematically-Equivalent Transformations (arXiv 2025, 2508.08833) — solver-level equivalent-transformation testing; we extend to verifier-level step testing
- ProcessBench: Identifying Process Errors in Mathematical Reasoning (arXiv 2024, 2412.06559) — base dataset for our isomorphic variants
- Reward Models Identify Consistency, Not Causality (arXiv 2025, 2502.14619) — theoretical motivation; problem-statement removal causes only 0.4-point drops
- Limits of PRM-Guided Tree Search for Mathematical Reasoning (arXiv 2025, 2510.20272) — PRM reliability degrades at depth; isomorphic brittleness as mechanistic explanation; notation gaming compounds across search steps
- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv 2025, 2507.15698) — causal debiasing framework adapted for our Iso-Aug mitigation
- Crome: Causally Robust Reward Modeling (ICML 2025, arXiv 2506.16507) — neutral augmentation strategy for RM invariance training
- GenPRM: Scaling Test-Time Compute of Process Reward Models (AAAI 2026, arXiv 2504.00891) — generative code-based PRM; potential inherent isomorphic robustness due to notation-invariant code execution
- Process Reward Models That Think (ThinkPRM) (arXiv 2025, 2504.16828) — generative CoT verifier for cross-paradigm comparison
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025, 2501.03124) — multi-dimensional PRM evaluation, no structural isomorphism
- Socratic-PRMBench: Benchmarking PRMs with Systematic Reasoning Patterns (arXiv 2025, 2505.23474) — reasoning pattern evaluation, no invariance testing
- GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models (arXiv 2026, 2605.01203) — extends PRM evaluation to general reasoning across 9 subdomains (science and logic) with 22 models; tests domain generalization breadth but not structural invariance, strengthening the benchmark saturation argument that this specific axis remains the critical missing piece
- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026, 2505.15960) — Z3/Isabelle verification approach adapted for our verification pipeline
- Math-Shepherd: Verify and Reinforce LLMs Step-by-step (arXiv 2023, 2312.08935) — baseline PRM for evaluation
- The Bidirectional Process Reward Model (arXiv 2025, 2508.01682) — bidirectional context for step estimation
- Robust Reasoning Benchmark (arXiv 2026, 2604.08571) — 14 perturbation techniques for solvers, not verifiers
- Inverse Scaling in Test-Time Compute (arXiv 2025, 2507.14417) — more compute can amplify flawed heuristics
- Towards Robust Process Reward Model (arXiv 2026, 2601.12748) — noisy supervision robustness, not structural invariance


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "96362e7b-7a40-404d-995d-516de4bc5e83",
  "type": "user",
  "uuid": "0f34cced-ac94-46d4-8dbd-df40c74dad2b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:35:04.406Z_

```json
{
  "parentUuid": "0f34cced-ac94-46d4-8dbd-df40c74dad2b",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "8b84873d-f08c-481d-b854-0e9e9c891e12",
  "timestamp": "2026-05-20T05:35:04.406Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:35:04.406Z_

```json
{
  "parentUuid": "8b84873d-f08c-481d-b854-0e9e9c891e12",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dc017c6d-3fbe-4f3b-9a8a-1006ba6e8a1f",
  "timestamp": "2026-05-20T05:35:04.406Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to provide a thorough evaluatio…",
  "leafUuid": "dc017c6d-3fbe-4f3b-9a8a-1006ba6e8a1f",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM structural isomorphism invariance benchmark",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:35:33.315Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 中偏弱
- Significance: 中
- Related Work: 强
- Probability: [18% - 30%] 中位 23%
- Main risks: Core assumption risk (PRM may be robust to T1-T4), Benchmark saturation + limited novelty

**Reviewer 2:**
- Novelty: 中


- Significance: 中偏弱
- Related Work: 强
- Probability: [20% - 32%] 中位 25%
- Main risks: "Expected results" risk, Generative PRM neutralization risk

**Reviewer 3:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 26%
- Main risks: "Incremental over PRM-BiasBench" rejection, Result predictability

Now I'm computing the aggregate statistics across all three reviewers. The median probabilities cluster around 25%, with a mean of about 24.67%.

The standard deviation comes out to roughly 1.25%, which indicates strong consistency in how the reviewers assessed the acceptance likelihood. Looking at the consensus patterns, all three reviewers converge on the same core weaknesses: the novelty is characterized as combinatorial rather than fundamentally new, the significance is limited because generative PRMs might naturally address this problem anyway, and the related work coverage is comprehensive across the board.

They also all identify the same methodological concerns—that extending PRM-BiasBench would be a trivial alternative, that the core assumption about PRM robustness may not hold given existing evidence, and that the causal claims around tree search are speculative. The Iso-Aug approach combines existing techniques without substantial innovation, and the notation gaming simulation is weaker than the actual GRPO experiments shown in prior work. Only the second and third reviewers flag the simulation-versus-real-training gap, while the first reviewer has some isolated concerns that don't align with the others.

With such tight agreement across reviewers, the probability estimates cluster around 24-25%, so I'm narrowing the interval to 18-20% on the lower end and capping it at 32% based on the most generous reviewer's upper bound. Now I need to assess the implementation feasibility—looking at computational requirements and data collection costs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc017c6d-3fbe-4f3b-9a8a-1006ba6e8a1f",
  "isSidechain": false,
  "requestId": "req_011CbDH3RCF1PxQ72p51mcfV",
  "type": "assistant",
  "uuid": "0118d6c7-d02a-428b-a1a8-93b042d232e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E22BdZDD1rhiV5eqtfuZXa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23105,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3521,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 23105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23105
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T05:36:32.198Z_

【阶段】: Meta Judge
【三次中位】: [23%, 25%, 26%]  std=1.25%
【共识维度】:
- **Novelty 中偏弱（3/3 共识，强信号）**: 三位审稿人一致认为核心贡献是"组合式创新"——将 PutnamGAP 的数学等价变换分类法、PRM-BiasBench 的鲁棒性测试框架、reWordBench 的 consistency training 思路拼接到 step-level PRM 这一新对象上。Gap 真实存在，但创新本质是"在已有 evaluation landscape 中填补最后一个空位"，而非提出 surprising insight。Iso-Aug 方法论 novelty 有限（reWordBench + CoLD 的直接组合）。
- **Significance 中/中偏弱（3/3 共识，强信号）**: 三位一致指出两个削弱因素：(a) generative PRMs（GenPRM/ThinkPRM）可能天然解决此问题，使 discriminative PRM 的 brittleness 诊断时效性存疑；(b) 核心发现无论 positive（"discriminative PRMs brittle"——expected）还是 negative（"PRMs robust"——benchmark 价值缩水），都缺乏 surprise value。
- **Related Work 强（3/3 共识，强信号）**: 三位一致认为 related work 覆盖全面、定位精准、引用真实，是 proposal 最强维度。但同时 R1 和 R3 指出，过于全面的 landscape 覆盖反而暴露了 novelty 的有限性（"正因为定位做得太好，才更明显地显示这是一个 incremental contribution"）。
- **核心假设风险（3/3 共识，强信号）**: PRM-BiasBench 发现 PRM 对 rephrasing 已然鲁棒（|ΔR|<0.03），T1（variable renaming）和 T2（commutative reordering）可能比 rephrasing 更简单，PRM 可能对 T1-T4 同样 robust，导致核心 narrative 瓦解。
- **Trivial alternative 威胁（3/3 共识，强信号）**: 核心 benchmark 可被视为 PRM-BiasBench 加 4 种新 perturbation type 的 extension；Iso-Aug 可被视为 reWordBench consistency training 的直接迁移。增量价值（formal verification、step-level 粒度）真实但有限。
- **Tree search 因果推断 speculative（3/3 共识）**: 将 isomorphic brittleness 归因为 tree search failure 的 mechanistic explanation 缺乏因果证据，仅能提供相关性分析。
- **Notation gaming simulation 弱于实际 RL 实验（2/3 共识）**: R2 和 R3 均指出 proposal 的 notation gaming 仅做 simulation，比 PRM-BiasBench 的真实 GRPO 训练弱一个量级。

【异常维度】:
- R1 单独质疑 CoLD 因果图从 S→L→P（单一标量 length）到 S→F→P（多维离散 serialization format）的迁移合理性——其他两位未提及此技术细节。此点有一定道理但不影响全局判断，降权处理。
- R3 单独关注 T3/T4 在 OlympiadBench/Omni-MATH 上的低覆盖率（~25-30%）可能不足以支撑统计结论——此点属于实验执行层面的具体风险，不影响 idea 层面评判，记录但不影响概率。

【最终概率】: [19% - 30%] 中位 24%
【一致性】: 高（std=1.25%，三位审稿人在 rubric 判决和概率估计上高度收敛）
【综合理由】:

三位审稿人在所有核心维度上达成高度一致：Novelty 中偏弱、Significance 中偏弱到中、Related Work 强。概率估计密集分布在 23-26% 中位区间。在高一致性情境下，按规则取中位附近并缩窄区间。

最终中位定为 24%（略低于三人算术均值 24.67%，体现"宁缺毋滥"原则），理由如下：

1. **Novelty 是核心限制因素**。三位一致认为这是组合式创新而非 conceptual breakthrough。在 PRM benchmark 已高度饱和的 2026 年中期（ProcessBench → PRMBench → PRM-BiasBench → Socratic-PRMBench → GR-Ben → FormalRewardBench），"又一个 PRM benchmark"的 marginal contribution 门槛极高。proposal 的核心 delta——"step-level structural isomorphism with formal verification"——是一个真实但增量的维度扩展。

2. **Significance 受双重夹击**。(a) 结果可预测性：无论 discriminative PRMs brittle（expected given PRM-BiasBench）还是 robust（benchmark 价值缩水），都缺乏 surprise；(b) generative PRM trajectory 使这一研究方向的长期 impact 存疑——proposal 自己承认了这一点并试图 hedge，但 hedge 本身（"即使 generative PRMs pass，benchmark 仍有价值"）削弱了 urgency narrative。

3. **Related Work 的强度是"不扣分"而非"加分"**。精准的 landscape 覆盖确保不被 desk-reject，但不补偿 novelty 和 significance 的不足。

4. **上界 30% 的逻辑**：如果执行完美且实验发现 unexpected patterns（如某些 PRM 对 T1/T2 robust 但对 T3/T4 catastrophically brittle 的反直觉结果），配合 notation gaming 的定量分析，有一定概率进入 borderline accept 区间。

5. **下界 19% 的逻辑**：如果审稿人直接判定"incremental over PRM-BiasBench"或核心假设不成立（PRMs 对 T1-T4 实际 robust），论文大概率被拒。

【建议】: 不推荐

【实施评估】:
- **计算资源**: 300-600 H100 GPU 小时（72B PRM 推理 ~160h 是主要瓶颈；7B 模型推理 ~90-100h；Iso-Aug LoRA 微调 ~40h；变体生成 ~100h）。预估 GPU 成本 $600-1200。需要至少 1 张 A100/H100 80GB 用于 72B 模型推理（可用 4-bit 量化），8GB+ GPU 即可运行 7B 模型。
- **数据需求**: ProcessBench 3,400 条人工标注数据（公开可得）；可能需要补充 200 条 AMC/AIME 竞赛题（公开可得）。变体生成依赖 Claude Sonnet API 或本地 LLM。
- **人工介入**: (a) 100 条 pilot annotation 用于验证 T3/T4 覆盖率（~1 周）；(b) 15% 分层抽样人工验证（~500+ 条变体的数学等价性审核，需要数学背景的标注者，~1-2 人周）；(c) notation gaming 分析的结果解读需要领域专家。
- **训练需求**: Iso-Aug LoRA 微调 Qwen2.5-Math-PRM-7B（~40 GPU 小时，单卡可完成）。不需要从头训练大模型。
- **新 Benchmark**: 是。需要构建 IsoPRM-Bench（基于 ProcessBench 的 isomorphic 变体数据集），包含 4 种变换类型 × 3,400 条基础数据 × 变体，以及三层验证 pipeline（SymPy + Z3 + 人工审核）。
- **预估周期**: 8-12 周（人工参与模式 8-10 周，全手动模式 10-12 周）。Pipeline 构建 + pilot 1-2 周 → 数据生成 + 验证 2-2.5 周 → 评估 2 周 → Iso-Aug 训练 1-1.5 周 → 分析写作 1.5-2 周。时间线紧凑但可行。API 成本 $500-900（Sonnet 用于变体生成）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0118d6c7-d02a-428b-a1a8-93b042d232e2",
  "isSidechain": false,
  "requestId": "req_011CbDH3RCF1PxQ72p51mcfV",
  "type": "assistant",
  "uuid": "f4c9cfbd-e60d-475d-96f7-3171b277705b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E22BdZDD1rhiV5eqtfuZXa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23105,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3521,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 23105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23105
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to provide a thorough evaluatio…",
  "leafUuid": "f4c9cfbd-e60d-475d-96f7-3171b277705b",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM structural isomorphism invariance benchmark",
  "sessionId": "02f046e6-8f50-498e-bd49-e7c77a458224"
}
```

---
