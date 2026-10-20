# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/4ee6b29f-5a23-4738-a05f-6cfccfd34472.jsonl`
- **Structured JSON:** [`7b33c72d29764f55fdf1.json`](../../sessions/7b/7b33c72d29764f55fdf1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:40:16.712Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:40:16.712Z",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct the evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **TCRM — \"Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling\"** (arXiv 2604.22981, April 2026):\n   核心主张与本 proposal 高度重叠。TCRM 在 Bradley-Terry loss 之上加 MC 和 TD 正则项，证明最优解等于条件期望（即 value function）。在 ProcessBench 上达到 44.9% F1（无需 step-level 标注），中间 token 的 pairwise accuracy 从 50% 提升到 88.9%。本质上也是 \"reward model = value function + TD training\"。虽然 TCRM 面向 general RLHF 而非数学推理 PRM-RL，但核心概念移动（\"用 TD 训练 RM 使其成为 value function\"）与 VF-PRM 大面积重合。**这是对 proposal novelty 的最大威胁。**\n\n2. **SHAPE — \"Stage-aware Hierarchical Advantage via Potential Estimation\"** (ACL 2026, arXiv 2604.06636):\n   **直接竞争者。** 显式引用 Ng et al. (1999) PBRS，用 Monte Carlo 估计 potentials，应用于 GRPO advantage 修改。实验显示 +3% accuracy、30% fewer tokens。Proposal 正确识别了其局限（MC rollout 而非 learned V(s_t)），但 SHAPE 的存在表明 PBRS+LLM reasoning 不再是 \"open gap\"，而是 \"已有初步实现，需要改进\" 的状态。\n\n3. **PURE — \"Stop Summation: Min-Form Credit Assignment\"** (NeurIPS 2025, arXiv 2504.15275):\n   提出 min-form credit assignment 替代 sum-form，显著缓解 reward hacking。Proposal 声称将给出 sum/min 在 PBRS 框架下的理论解释，这是一个有价值的理论贡献，但 PURE 的实证结论已经被社区广泛接受。\n\n4. **PRIME — \"Process Reinforcement through Implicit Rewards\"** (ICLR 2026, arXiv 2502.01456):\n   从 ORM token probabilities 提取隐式 process rewards，自身论文已承认 \"可视为 PBRS 其中 q-value 是 potential\"。Qwen2.5-Math-7B-Base 上 +15.1% average improvement。这意味着 PBRS 在 PRM-RL 中的应用**已经被隐式实现且验证有效**。\n\n5. **TDRM — \"Smooth Reward Models with Temporal Difference\"** (arXiv 2509.15110, Sep 2025):\n   用 n-step TD learning 训练 PRM，tree-search 提升 23.7%，20× data efficiency。与 VF-PRM 共享 \"用 TD 学习训练 reward model\" 的核心技术选择，但仍需 step-level 标注。\n\n6. **PAV — \"Rewarding Progress\"** (ICLR 2025):\n   计算 step reward 为 MC success probability 的变化量——这在概念上与 PBRS potential difference 等价，但未建立形式化联系。Proposal 正确指出了这一点。\n\n7. **DuaShepherd** (arXiv 2506.17533, June 2025):\n   分离 correctness 和 potential 两个 reward head，MATH500/ProcessBench SOTA，但仅在 inference-time（best-of-N）评估。\n\n8. **rePIRL** (arXiv 2602.07832, Feb 2026):\n   用 inverse RL 框架统一现有 PRM 训练方法，声称是第一个将 IRL 推广到 LLM reasoning 的工作。\n\n9. **CRM — \"Conditional Reward Modeling\"** (ICLR 2026):\n   将 step reward 定义为条件概率 P(correct|s_{1:t})，在 BoN/beam search/RL 全面评测，但无 PBRS 保证。\n\n10. **Credit Assignment Survey — \"From Reasoning to Agentic\"** (arXiv 2604.09459, April 2026):\n    覆盖 47 种方法，proposal 声称该 survey 未识别 \"trained neural V(s_t) + explicit PBRS + RL training\" 这一特定组合。\n\n- **调研总结**: PRM-RL credit assignment 是 2025-2026 年最拥挤的研究前沿之一。PBRS 已被 SHAPE 显式实现（MC potentials）、被 PRIME 隐式实现（token probabilities）、被 TCRM 通过 TD 正则化部分实现。VF-PRM 的特定组合（trained V(s_t) via TD(λ) + PBRS formula + GRPO integration）确实尚未被精确填充，但构成该组合的**每个单独组件都已有近期工作覆盖**，proposal 的贡献更多是\"组合+理论统一\"而非\"新范式\"。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁。** \n\n最直接的替代方案：PRIME（已有 ICLR 2026）已经隐式实现了 PBRS（其论文自称 \"viewable as PBRS where q-value is the potential\"），且不需要额外训练单独的 value function，直接从 ORM token probabilities 提取。如果 PRIME + GRPO 已经在相同 setting（Qwen2.5-Math-7B）上取得 +15.1% 改进，VF-PRM 需要证明 explicit V(s_t) training 显著优于 PRIME 的 implicit 方式。\n\n另一个替代：SHAPE（ACL 2026）已经显式使用 PBRS，只是用 MC rollout 而非 learned V(s_t)。VF-PRM 的增量价值在于 \"amortized neural V(s_t) 比 MC rollout 更高效且支持 online updates\"。这是一个合理但**量级有限**的改进——MC rollout 的成本在 SHAPE 中已被证明可控（30% fewer tokens），neural V(s_t) 能否带来实质性的进一步提升是存疑的。\n\n**增量价值的核心**在两个地方：(1) sum/min aggregation 在 PBRS 下的形式化证明——这是纯理论贡献；(2) learned V(s_t) 相比 MC potentials 的效率优势。前者有价值但不够 \"surprising\"；后者需要实证支撑。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **\"V(s_t) ≈ P(correct | prefix₁:t) 可以用 TD(λ) + outcome-only supervision 高效且准确地训练\"**——这是最关键的前提。TCRM 已经表明 TD 正则化可以诱导 temporal coherence，但 TCRM 是在 Bradley-Terry preference data 上训练的，而 VF-PRM 只用 binary outcome labels。二者的数据分布完全不同。用纯 outcome labels 做 TD(λ) 训练 V(s_t) 的质量——特别是对中间步骤的估值准确性——是未经验证的。TD(λ) 在 tabular/small-state RL 中的收敛性质不能直接迁移到 LLM 推理的高维、非平稳状态空间。\n\n2. **\"PBRS 的 policy invariance guarantee 在 LLM RL（GRPO）setting 中依然成立\"**——Ng et al. (1999) 的 policy invariance 定理基于 MDP 假设（Markov property、tabular or function approximation with adequate representational capacity）。LLM reasoning 的 state 是可变长度的 token sequence，GRPO 是一种 on-policy approximate 算法，其与 PBRS 定理前提的匹配度存疑。Proposal 声称 \"provably preserves the optimal policy\"，但这个 \"provably\" 的前提条件在实际 setting 中可能不满足。\n\n3. **\"sum-form 对应 telescoping potential with unbounded shaping magnitude\" 可以严格证明**——这需要看具体证明。Sum-form aggregation（Σ PRM_scores）和 PBRS 中的 telescoping sum 之间的映射是否严格，取决于 PRM scores 的具体数学性质。如果 PRM 本身不是一个满足 PBRS potential 条件的函数，这个映射可能只是 approximate analogy 而非 formal proof。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中（偏弱）**\n   \n   理由：VF-PRM 的核心贡献是\"组合+理论统一\"：将 TD-trained V(s_t)、PBRS formula、GRPO training 三者显式结合。但：\n   - TCRM (April 2026) 已经证明 \"reward models = value functions + TD training\"，核心概念移动被覆盖；\n   - SHAPE (ACL 2026) 已经显式实现 PBRS for LLM reasoning；\n   - PRIME (ICLR 2026) 已经隐式实现 PBRS for RL training 且自我承认这一联系；\n   - TDRM (Sep 2025) 已经使用 TD learning 训练 PRM。\n   \n   剩余的 novelty delta 主要在：(a) 理论上统一 sum/min aggregation under PBRS——这是有价值的但属于 \"elegant formalization of known phenomena\" 而非 \"surprising new finding\"；(b) explicit neural V(s_t) 而非 MC rollout potentials——这是 implementation choice 层面的差异。在如此拥挤的竞争环境中，剔除 surface differences 后的 novelty 有限。\n\n2. **Significance: 中**\n   \n   理由：研究问题本身非常重要——PRM-RL integration 的 credit assignment 是 LLM reasoning 的核心挑战，RARL survey 将其列为 open problem。但：\n   - 如果实验结果是 \"VF-PRM 在 MATH500 上比 PURE 高 2-3%\"，审稿人很可能反应是 \"I would have guessed this\"——用 learned value function 替代 heuristic aggregation 当然应该更好，这不 surprising；\n   - 理论贡献（PBRS 统一 sum/min）的实际影响取决于社区是否认为 \"我们需要一个理论来解释 PURE 的实验发现\"——考虑到 PURE 已被 NeurIPS 接受且其实证结论被广泛采纳，理论解释的边际价值有限；\n   - 对领域的可推广性：框架是否能推广到数学推理之外（代码生成、agent 场景）未被讨论。\n\n3. **Related Work: 强**\n   \n   理由：这是 proposal 的最大亮点。作者对相关工作的覆盖极其全面——PURE、PRIME、SHAPE、TDRM、CRM、DuaShepherd、PAV、SPAE、DVPO、RARL survey、credit assignment survey 均被准确识别和定位。特别是：\n   - 正确识别了 SHAPE 作为 critical concurrent work 并精确描述了其局限；\n   - 正确描述了 PRIME 的 PBRS 联系；\n   - 正确描述了 PAV 的概念等价性；\n   - 对每篇论文的差异化定位清晰（best-of-N vs RL、MC vs neural、step vs token）。\n   \n   **但有一个重要遗漏：TCRM (arXiv 2604.22981, April 2026) 未被提及**——这篇论文直接主张 \"reward models are secretly value functions\" 并使用 TD 正则化，与 VF-PRM 的核心概念高度重叠。在最终提交前必须纳入讨论。\n\n---\n\n【概率估计】: 18% - 30%，中位 23%\n\n【估计理由】:\n- **Novelty 是主要限制因素**。在 TCRM、SHAPE、PRIME、TDRM 四篇直接竞争工作存在的前提下，VF-PRM 的 novelty delta 被显著压缩。核心概念移动（\"RM = V function + TD training\" 和 \"PBRS for LLM reasoning\"）均已被近期工作覆盖，剩余贡献集中在\"组合\"和\"理论统一\"层面。\n- **Significance 的上界受限于 \"expected\" 性质**。如果核心实验结果是 positive（VF-PRM > PURE/PRIME），审稿人大概率反应是 \"makes sense, not surprising\"——用 principled value function + PBRS 替代 heuristic aggregation 自然应该更好。这限制了论文的 impact narrative。\n- **Related Work 覆盖出色**是 positive signal，说明作者对领域有深入理解，但这属于执行质量而非 idea 质量。\n- **理论贡献**（PBRS 统一 sum/min）是最有差异化价值的部分，如果证明严谨且 insight 深刻，有可能将概率推向上界。但如果只是 \"straightforward formalization\"，则价值有限。\n- 上界 30% 对应：理论证明确实深刻 + 实验显著超越所有 baselines + TCRM 被充分 differentiate；下界 18% 对应：理论被审稿人认为 trivial formalization + 实验改进 marginal + TCRM/SHAPE 的 novelty 挤压。\n\n【主要风险】:\n1. **Novelty 被 concurrent work 瓦解**：TCRM (April 2026, 未被 proposal 提及) 已实现 \"RM as value function + TD training\"，SHAPE 已实现 \"explicit PBRS for LLM reasoning\"。审稿人可能认为 VF-PRM 是这两个已知方向的 straightforward combination，缺乏 sufficient novelty increment。\n2. **\"Expected positive\" 问题**：核心实验若 positive，审稿人会认为这是 \"the principled approach beats heuristic, as expected\"——无 surprise value。论文的 acceptance 需要远超预期的实验改进幅度（e.g., >5% on MATH500 over PURE），或者理论贡献被认为独立有价值，两者均不确定。\n```\n\nSources:\n- [TCRM: Reward Models Are Secretly Value Functions](https://arxiv.org/abs/2604.22981)\n- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation](https://arxiv.org/abs/2604.06636)\n- [PURE: Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)\n- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)\n- [TDRM: Smooth Reward Models with Temporal Difference](https://arxiv.org/abs/2509.15110)\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)\n- [PAV: Rewarding Progress](https://arxiv.org/abs/2410.08146)\n- [CRM: Conditional Reward Modeling](https://openreview.net/forum?id=4DJoBOQNd0)\n- [rePIRL: Learn PRM with Inverse RL](https://arxiv.org/abs/2602.07832)\n- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)\n- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/abs/2602.09305)\n- [Credit Assignment Survey: From Reasoning to Agentic](https://arxiv.org/abs/2604.09459)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a well-informed assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- SHAPE (ACL 2026, arXiv:2604.06636): 最直接的竞争工作。明确引用 Ng et al. (1999) PBRS 理论，将 Monte Carlo 估计的 potential 应用于 LLM 推理，在 GRPO 的 advantage 计算中注入 PBRS 项，实现 +3% 准确率和 30% token 减少。但使用 training-free MC rollout 估计 potential（非学习的 value function），且仅修改 GRPO advantage 而非作为独立 PRM 训练目标。\n\n- PURE (NeurIPS 2025, arXiv:2504.15275): 证明 sum-form credit assignment 导致 reward hacking（甚至在训练初期就 collapse），提出 min-form credit assignment 显著缓解。但仅提供经验性证据，缺乏理论解释——这恰恰是本 proposal 声称要填补的 gap。在 3 个 base model 上，min-form 在 30% steps 内达到 verifiable reward 方法的可比性能。\n\n- PRIME (ICLR 2026, arXiv:2502.01456): 从 ORM token probabilities 中提取 implicit process rewards，实现 online PRM 更新。论文本身承认\"可以被视为 PBRS，其中 q-value 是 potential function\"，但使用启发式提取而非显式 value function 训练。\n\n- TDRM (arXiv:2509.15110): 应用 TD learning 平滑 PRM 标签，tree-search 提升 23.7%，数据效率提升 20×。但仍需要 step-level annotations，且目的是平滑现有标签而非从头训练 value function。技术路径与本 proposal 有重叠但目标不同。\n\n- CRM (ICLR 2026, OpenReview): 将 step rewards 建模为条件概率 P(correct|s_{1:t})，在 BoN、beam search 和 RL 三个场景评估。缺乏 PBRS 保证，仍使用 MC 估计的 step labels。\n\n- DuaShepherd (arXiv:2506.17533): 分离 correctness 和 potential reward 两个头，multi-head 架构。MATH500/ProcessBench SOTA。但仅评估 inference-time (BoN)，未用于 RL 训练。\n\n- PAV (ICLR 2025, arXiv:2410.08146): 将 step reward 定义为 \"progress\"——prover policy 在执行该 step 前后成功率的变化。概念上与 PBRS potential differences 完全一致，但未建立正式 PBRS 联系，也未训练专门模型。比 ORM 5× compute efficient，RL 中 6× sample efficient。\n\n- SPAE (arXiv:2601.03823): Training-free 方法，用 probing 提取中间 confidence 和 correctness 作为 \"Step Potential\" 信号。PBRS-inspired potential differences + 启发式复合指标。\n\n- Credit Assignment Survey (arXiv:2604.09459): 覆盖 47 种 CA 方法，按 token/segment/step/turn 粒度和方法论分类。**未识别 \"trained neural V(s_t) + explicit PBRS step rewards + RL training\" 这一具体组合为已有方法**。\n\n- Bootstrapped Reward Shaping (arXiv:2501.00989): 在经典 RL 中使用 agent 当前 value estimate 作为 PBRS 的 potential function，有 tabular 收敛证明和 Atari 实验。但未应用于 LLM 推理。\n\n- DVPO (ICLR 2026, arXiv:2502.16944): 预训练 Global Value Model 作为 frozen critic，40% less GPU memory。但在 response-level 操作，非 step-level process supervision。\n\n- 调研总结: PRM-RL integration 是 2025-2026 年最激烈竞争的前沿方向。PBRS 理论已通过 SHAPE 被引入 LLM 推理领域（MC rollout 路线），TDRM 已将 TD learning 引入 PRM 训练，PRIME 已注意到 PBRS 联系但未显式实现。\"训练 neural V(s_t) + 显式 PBRS 推导 step rewards + 用于 RL 训练\"这一精确组合确实是 open gap，但其各个组成部分已在不同工作中被分别探索。本 proposal 处于多条已有工作线索的交叉点——这既是机遇（整合价值），也是风险（novelty 被分散）。\n\n\n【Trivial Alternative 检验】:\n\n存在两个显著的 trivial alternative 威胁：\n\n(1) **SHAPE 的 MC rollout 路线**: SHAPE 已经使用 PBRS + MC 估计的 potential 实现了 +3% 准确率提升和 30% token 减少。本 proposal 的核心增量是\"用 trained neural V(s_t) 替代 MC rollout V(s_t)\"——但这是一个 amortization 工程优化，而非概念性创新。如果 MC rollout 在质量上并不显著劣于 neural V(s_t)（尤其考虑到 VinePPO 等工作表明 MC 估计在 language environment 中可以很有效），那增量价值有限。\n\n(2) **PURE min-form + 标准 PRM**: 直接使用 PURE 的 min-form credit assignment + 现有 PRM 训练方法已经能取得不错效果。本 proposal 提供理论解释但未必带来实践提升——\"解释为什么 min works better\"的学术价值取决于是否产生可操作的改进。\n\n**增量价值所在**: (a) 理论统一——将 sum/min/product 统一为 PBRS 框架下不同 potential function 的特例，提供 PURE 经验发现的首个理论解释；(b) 无需 step annotation——TD(λ) + outcome-only supervision 比 TDRM（需要 step labels）更 practical；(c) online value function update 支持 RL 训练中的持续适应。这些增量价值是真实的，但核心问题是理论解释和 amortization 是否足以构成顶会级贡献。\n\n\n【前提假设检验】:\n\n核心逻辑链中有 3 个关键未验证假设：\n\n(1) **\"TD(λ) 能在 LLM reasoning 的 state space 上训练出准确的 V(s_t)\"**: 这是最大的风险假设。现有趋势恰恰相反——GRPO 移除了 value network（因为 value function 在 LLM RL 中训练困难且不稳定），VinePPO 的工作明确指出 value networks \"barely outperform random baselines when comparing alternative steps\"。在如此高维、稀疏反馈的 state space 中，TD(λ) + outcome-only supervision 是否能训练出质量足够好的 V(s_t) 是一个重大实证问题。\n\n(2) **\"sum-form aggregation 可以 reduce to telescoping potential with unbounded shaping magnitude\"的数学推导**: 虽然 proposal 声称会提供 formal proofs，但将离散 PRM scores 的 sum 映射到 continuous PBRS 框架需要特定的数学假设。这些假设在 LLM reasoning 的实际设置中是否成立需要验证。\n\n(3) **\"amortized neural V(s_t) 优于 MC rollout V(s_t)\"**: SHAPE 使用 MC rollout 已取得不错效果。在 language environment 中 MC rollout 相对 cheap（只需要 forward pass），而 neural V(s_t) 引入了额外的 training cost 和 approximation error。net benefit 并非显然为正。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 核心贡献是将 PBRS 理论与 PRM training 的显式整合，以及将 sum/min/product aggregation 统一为 PBRS 特例的理论分析。这确实是一个未被填补的 gap——credit assignment survey (arXiv:2604.09459) 确认 \"trained neural V(s_t) + explicit PBRS + RL training\" 组合不存在于已有文献中。然而，各组成部分均已被独立探索：SHAPE 已在 LLM 推理中实现 PBRS（MC 路线），TDRM 已将 TD learning 用于 PRM，PRIME 已指出 PBRS 联系，PAV 已概念性地使用 potential differences。理论统一（aggregation → PBRS 特例）是最有价值的 novelty delta，但一旦建立 PBRS 框架，sum 的 telescoping 性质和 min 的 truncation 性质是相对直接的推论。总体而言，novelty 是真实的但属于增量整合型，而非范式转换型。\n\n2. **Significance: 中偏强** — 问题非常重要且时机恰好。PRM-RL integration 是 2025-2026 年 LLM reasoning 领域最核心的开放问题之一。RARL survey 明确将 \"principled aggregation design guidelines\" 列为 central open problem。如果理论分析确实能为 aggregation 选择提供可操作的指导（而不仅仅是事后解释），实际影响力会很大。但 significance 的上限受制于这些理论洞见是否能转化为 consistently better 的实践结果——如果最终只是\"理论上更优雅但实践上和 PURE/SHAPE 差不多\"，影响力会打折。\n\n3. **Related Work: 强** — 这是 proposal 最突出的优势。对竞争格局的理解极其透彻：准确识别了 SHAPE、PURE、PRIME、TDRM、CRM、DuaShepherd、PAV、SPAE 等所有关键工作，精确描述了每篇的贡献和局限，并清晰定位了本 proposal 填补的具体 gap。特别值得注意的是对 concurrent work SHAPE 的诚实处理——不回避最直接的竞争，而是明确阐述差异化（learned vs. MC potentials）。这种 landscape awareness 在我的调研中得到了完全验证。\n\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】:\nNovelty 是真实的但属于增量整合型（\"principled combination of known ingredients\"），这决定了上限不会太高。最核心的 novelty——aggregation schemes 的 PBRS 理论统一——虽然新颖但可能被视为\"连接已知理论的 straightforward application\"。SHAPE (ACL 2026) 作为极度接近的 concurrent work 是最大的 novelty 压力源；审稿人可能认为 \"MC rollout → learned V(s_t)\" 是工程改进而非概念突破。Significance 较强——问题很重要，时机好——这拉高了下限（不太可能因为\"问题不重要\"被拒）。Related work 是强项，降低了被拒的概率但不增加中稿概率。\n\n限制上界的维度是 **Novelty**：在 SHAPE、PRIME、TDRM、PAV 等工作的包围下，剩余的 novelty delta 需要审稿人认可\"理论统一 + 学习型 value function\"的组合价值。如果审稿人认为理论贡献是 straightforward，上界会被压到 25% 左右；如果审稿人重视理论统一的实用价值，可达 38%。\n\n此外，前提假设检验中的第(1)点——TD(λ) 在 LLM state space 上能否训练出质量足够好的 V(s_t)——是一个方向性风险。如果 value function 训练不出来，整个 framework 的实践价值就不存在，只剩理论分析，这对顶会投稿来说可能不够。\n\n【主要风险】:\n1. **Novelty 被 SHAPE 挤压**: SHAPE (ACL 2026) 已经将 PBRS 引入 LLM reasoning 并取得正面结果。审稿人很可能将本 proposal 视为 SHAPE 的 incremental variant（\"learned potential instead of MC potential\"），如果 performance gain 不显著，novelty 评分可能被压至 borderline。\n2. **Value function 训练可行性逆趋势**: 当前 LLM RL 领域的主流趋势是远离 value networks（GRPO 移除 value model，VinePPO 表明 value networks 在 LLM 中表现差），本 proposal 逆势而行要训练 neural V(s_t)。如果 V(s_t) 训练效果不理想，不仅实验不好看，还会动摇 framework 的实用性论证。\n```\n\nSources:\n- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/html/2604.06636)\n- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275)\n- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)\n- [TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference](https://arxiv.org/abs/2509.15110)\n- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://openreview.net/forum?id=4DJoBOQNd0)\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)\n- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146)\n- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)\n- [Credit Assignment Survey: From Reasoning to Agentic](https://arxiv.org/abs/2604.09459)\n- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/abs/2602.09305)\n- [Bootstrapped Reward Shaping](https://arxiv.org/pdf/2501.00989)\n- [DVPO: Pretrain Value, Not Reward](https://arxiv.org/html/2502.16944)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **SHAPE (ACL 2026, arXiv 2604.06636)**: 最直接的竞争者。显式引用 Ng et al. (1999) 将 PBRS 应用于 LLM 推理，使用 Monte Carlo 估计的 potential 函数，修改 GRPO 的 advantage 计算。实现 +3% 准确率、30% token 减少。与本 proposal 的核心差异仅在于 MC rollout potentials vs. learned neural value function。\n\n2. **PRIME (ICLR 2026, arXiv 2502.01456)**: 从 ORM 的 token 概率中隐式提取 process reward，论文自身已明确指出\"可视为 PBRS，其中 q-value 即 potential function\"。这意味着 PBRS 与 process reward 的理论联系已在 PRIME 中被公开讨论，尽管 PRIME 未显式训练 value function。\n\n3. **PURE (NeurIPS 2025, arXiv 2504.15275)**: 发现 sum-form credit assignment 导致 reward hacking，min-form 显著缓解。基于 Qwen2.5-Math-7B 的 PURE 在 AMC23 达到 82.5%。提供了纯经验证据但无理论解释——本 proposal 声称要提供这个理论解释。\n\n4. **TDRM (arXiv 2509.15110, Sep 2025)**: 已经使用 TD learning 训练 PRM，将 value 估计作为 process reward。实现 tree-search +23.7%、20× 数据效率。与本 proposal 共享\"用 TD 训练 value-function-like model\"的核心技术路径，但 TDRM 未将输出显式框架为 PBRS potential。\n\n5. **PAV (ICLR 2025, arXiv 2410.08146)**: 将 step reward 定义为\"progress\"——即 MC 成功概率的变化 ΔP(correct)。这在概念上等同于 F_t = V(s_{t+1}) − V(s_t)，只是未建立与 PBRS 的形式联系。\n\n6. **DuaShepherd (arXiv 2506.17533, June 2025)**: 分离 correctness 和 potential 两个 reward head，在 MATH500/ProcessBench 上达到 SOTA。证明了 correctness 和 potential 是正交信号——支持本 proposal 的论点，但只在 inference-time (best-of-N) 评估。\n\n7. **CRM (ICLR 2026, arXiv 2509.26578)**: 将 step reward 建模为条件概率 P(correct|s_{1:t})，在 RL 训练中评估。无 PBRS 保证但缓解了 reward hacking。\n\n8. **SPAE (arXiv 2601.03823, Jan 2026)**: Training-free 的 PBRS-inspired potential difference 方法，使用启发式复合指标。\n\n9. **DVPO (ICLR 2026, arXiv 2502.16944)**: 预训练 frozen Global Value Model 作为 universal critic，但在 response-level 而非 step-level。\n\n10. **RARL Survey (arXiv 2602.09305, Feb 2026)**: 系统梳理 reward modeling 范式，明确指出\"不同 aggregation scheme 产生 divergent policy behavior，principled design guidelines 缺失\"。\n\n- **调研总结**: PRM-RL 集成是 2025-2026 年最活跃的研究前沿之一。PBRS 与 LLM 推理的结合已有多项工作从不同角度触及：SHAPE 显式应用 PBRS（MC potentials）、PRIME 隐式使用 PBRS、PAV 在概念上等同于 potential difference、TDRM 用 TD 训练 value model。本 proposal 处于这些工作的交叉点，试图用\"显式训练 neural V(s_t) + PBRS 步级 reward + RL 训练\"这一特定组合来统一现有方法。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁：\n- **TDRM + potential difference**: 直接取 TDRM 已训练好的 TD-based reward model 的输出，计算相邻步的差值作为 shaped reward。这几乎就是 VF-PRM 的核心操作，但不需要重新设计训练框架。\n- **SHAPE 的 MC potentials**: SHAPE 已证明用 MC rollout 估计 potential 配合 PBRS 即可获得 +3% 提升和 30% token 减少。Neural value function 相对于 MC estimation 的增量价值不明确——MC 估计可能在给定计算预算下更准确（无函数近似误差）。\n- **PRIME 的隐式 PBRS**: PRIME 已经在实践中隐式使用 PBRS 并取得强结果。将其\"显式化\"的实际收益需要实证。\n\n增量价值主要体现在：(a) 理论统一——证明 sum/min 是 PBRS 的退化特例；(b) 避免 MC rollout 的推理开销；(c) 支持在线更新。但 (a) 更偏理论贡献，(b)(c) 的实际优势幅度待验证。\n\n【前提假设检验】:\n核心 claim 的逻辑链中有几个未经验证的假设：\n\n1. **\"Neural V(s_t) 优于 MC potential estimation\"**: 这是相对于 SHAPE 的关键差异化论点，但未有理论或实证支撑。函数近似引入 bias（value function approximation error），而 MC estimation 有 variance 但无 bias。在 LLM reasoning 的 episode 通常较短（几十步）的场景下，MC 估计可能足够精确，neural approximation 的优势不明显。\n\n2. **\"Formal PBRS guarantees 在实践中有意义\"**: Ng et al. (1999) 的 policy invariance 定理要求精确的 potential function。当 V(s_t) 是一个有近似误差的 neural network 时，PBRS 的理论保证不再严格成立。Proposal 没有讨论 approximate PBRS 的误差传播。\n\n3. **\"证明 sum/min 是退化特例会带来实际改进\"**: 理论上证明 sum-form 导致 reward hacking 可以解释 PURE 的发现，但这个证明本身不直接产生更好的方法。如果 PURE 的 min-form 已经 empirically 有效，那么\"解释为什么它有效\"的价值更偏理论 insight 而非方法改进。\n\n4. **\"TD(λ) + outcome-only supervision 能训练出高质量 V(s_t)\"**: 虽然 TDRM 证明了 TD 训练的可行性，但 TDRM 使用的是 step-level annotations。仅用 outcome labels 做 TD(λ) 时，信号极度稀疏（每个 episode 只有一个 binary signal），value function 的学习效率和质量存疑。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 本 proposal 的每个组件都有 closely related 的先驱工作：TD 训练 → TDRM；PBRS 显式应用 → SHAPE；PBRS 隐式使用 → PRIME；potential difference → PAV；correctness vs. value 分离 → DuaShepherd。真正的 novelty delta 在于将这些组件以一种特定方式组合，并提供理论统一框架（证明 sum/min 是 PBRS 退化）。这个理论贡献是 genuine 的——credit assignment survey (Apr 2026) 确认这一精确组合尚无先例——但属于\"对已知理论（PBRS, 1999）的自然应用到当前热点问题\"，而非概念性突破。SHAPE (ACL 2026) 是最直接的 threat：它已经做了\"PBRS + LLM reasoning\"，本 proposal 的差异化仅在于 neural vs. MC potentials，这更像是一个 engineering variant 而非 conceptual advance。\n\n2. **Significance: 中偏强** — 研究问题本身高度重要：PRM-RL 集成中 aggregation scheme 的理论缺失是 RARL survey 明确指出的 open problem。如果理论证明 solid 且 empirical gains 显著，对该领域有实际推动作用。然而，practical significance 受限于：(a) PURE 的 min-form 已经 empirically 有效，\"为什么有效\"的解释价值低于\"什么更有效\"；(b) 该领域竞争极度激烈，多项同期工作在快速蚕食 novelty space；(c) 贡献的可推广性主要限于 mathematical reasoning 场景。\n\n3. **Related Work: 强** — Proposal 对领域的把握出色。覆盖了 PRIME、PURE、SHAPE、TDRM、CRM、DuaShepherd、DVPO、PAV、SPAE 及两篇 survey，对每篇工作的差异化定位清晰且准确（经调研验证，所有引用的论文真实存在，描述基本准确）。特别是对 SHAPE 作为 critical concurrent work 的识别和差异化分析到位。唯一可改进的是：应更深入讨论与 TDRM 的技术路径重叠，以及 PRIME 中已公开的 PBRS 连接意味着什么。\n\n【概率估计】: [22% - 35%] 中位 28%\n\n【估计理由】:\n- Related Work 维度强，说明 proposal 作者对领域有深刻理解，不会因 ignorance of prior work 被拒，这拉高了下限。\n- Significance 中偏强——问题确实重要，AAAI 审稿人会认同 PRM-RL 集成值得研究。\n- **Novelty 是上界的主要限制因素**。核心问题是：当审稿人看到 SHAPE 已在 ACL 2026 做了 \"explicit PBRS + LLM reasoning\"，PRIME 已讨论了 PBRS connection，TDRM 已用 TD 训练 value model 时，会问\"这篇论文真正 new 的是什么？\" 答案是\"learned neural potential + 理论统一 sum/min\"，这个 delta 是 real 但 modest。\n- 审稿人很可能说 \"I would have guessed this\"——将 PBRS（一个 1999 年的经典结果）应用到 PRM 是一个自然的 next step，而非 surprising insight。这将概率限制在 35% 以下。\n- 如果 empirical results 能显著 beat PURE/SHAPE/PRIME (>2% on MATH500, >5% on AIME)，概率可推至上界；如果只是 marginal improvement 或 comparable，概率在下界附近。\n\n【主要风险】:\n1. **Novelty 被 SHAPE 严重稀释**: SHAPE (ACL 2026) 已显式应用 PBRS 到 LLM reasoning 并取得显著效果。审稿人会视本 proposal 为 SHAPE 的 incremental variant（neural vs. MC potentials），而非独立贡献。本 proposal 的理论统一部分可能被视为\"对 PURE 发现的 post-hoc rationalization\"而非 forward-looking insight。\n2. **\"Natural application of known theory\" 风险**: 将 Ng et al. (1999) 的经典 PBRS 定理应用到 PRM 是领域内任何熟悉 RL theory 的人都会想到的方向（PRIME 已经提到了这个连接）。审稿人可能认为这是一个 \"low-hanging fruit\" 而非 genuine intellectual contribution。\n```\n\nSources:\n- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/html/2604.06636)\n- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)\n- [PRIME: Process Reinforcement through Implicit Rewards (ICLR 2026)](https://openreview.net/forum?id=CmyqMn3HeJ)\n- [TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference](https://arxiv.org/abs/2509.15110)\n- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning (ICLR 2026)](https://openreview.net/forum?id=4DJoBOQNd0)\n- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (ICLR 2025)](https://arxiv.org/abs/2410.08146)\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)\n- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)\n- [DVPO: Pretrain Value, Not Reward: Decoupled Value Policy Optimization (ICLR 2026)](https://openreview.net/forum?id=qirGds1BmK)\n- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/abs/2602.09305)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Potential-Valued Process Rewards for Principled Step-Level Credit Assignment\n\n## Core Problem\n\nCurrent PRMs are trained as step-correctness classifiers but heuristically repurposed as RL reward signals via aggregation (sum, min, product), causing either reward hacking or information loss. No principled framework connects PRM design to RL training quality, despite potential-based reward shaping (PBRS) theory guaranteeing policy invariance — a well-known result never practically implemented for step-level process rewards in mathematical reasoning.\n\n## Research Opportunity\n\nThree independent 2025-2026 findings converge: (1) the RARL survey confirms PBRS 'lacks practical PRM implementation' for reasoning RL; (2) DuaShepherd proves step correctness and step value (potential) are orthogonal signals — yet all existing PRMs train only on correctness; (3) PURE demonstrates that sum-form PRM aggregation causes training collapse, while min-form loses useful gradient information, but provides no theoretical justification for why min works better. Training a PRM as a state value function V(s_t) = P(correct | prefix₁:t) and deriving step rewards as potential differences r_t = γV(s_{t+1}) − V(s_t) would unify these findings: PBRS guarantees no policy distortion, value-function training requires only outcome labels (no expensive step annotations), and the framework naturally subsumes sum/min/product as suboptimal special cases with specific potential-function choices.\n\n## Research Landscape\n\nPRM-RL integration is the most contested frontier. PURE (NeurIPS 2025) showed min-form credit assignment avoids reward hacking that collapses sum-form training 'even at the beginning,' but provides only empirical justification. TDRM (Sep 2025) applies TD learning to smooth PRM labels, achieving 23.7% improvement in tree-search and 20× data efficiency, but still requires step-level annotations and doesn't address the aggregation problem. CRM (ICLR 2026) models step rewards as conditional probabilities P(correct|s_{1:t}) causally linked to outcomes, evaluating on best-of-N, beam search, AND RL — but lacks PBRS guarantees and still uses MC-estimated step labels. PRIME (ICLR 2026) extracts implicit process rewards from ORM token probabilities and is acknowledged as 'viewable as PBRS where q-value is the potential,' but uses heuristic extraction rather than explicit value function training. DuaShepherd (June 2025) separates correctness and potential reward heads, achieving SOTA on MATH500/ProcessBench, but evaluates only at inference time (best-of-N), not RL training. DVPO (ICLR 2026) pretrains a Global Value Model for general RLHF with 40% less GPU memory, but operates at response-level, not step-level process supervision. The RARL survey (Feb 2026) catalogs reward modeling paradigms and identifies the central open problem: 'Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent.' CRITICAL CONCURRENT WORK: SHAPE (ACL 2026) applies PBRS with Monte Carlo-estimated potentials to LLM reasoning, explicitly citing Ng et al. (1999), achieving +3% accuracy with 30% fewer tokens — but uses training-free MC rollouts (not a learned value function) and only modifies GRPO advantages rather than serving as a standalone PRM training objective. SPAE (Jan 2026) uses training-free PBRS-inspired potential differences with a heuristic composite metric. PAV (ICLR 2025) estimates step 'progress' as change in MC success probability, conceptually identical to PBRS but without formal connection or a trained model. The credit assignment survey (Apr 2026) covers 47 methods across token/segment/step/turn granularity and does NOT identify the specific combination of trained neural V(s_t) + explicit PBRS step rewards + RL training as an existing method — suggesting this precise integration remains an open gap.\n\n## Proposed Approach\n\nTrain a Process Reward Model as an explicit state value function V(s_t) ≈ P(correct | prefix₁:t) on Qwen2.5-Math-7B using TD(λ) with only binary outcome supervision, requiring no step-level annotations. Derive dense step-level rewards via the classical PBRS formula F_t = γV(s_{t+1}) − V(s_t), which provably preserves the optimal policy under Ng et al. (1999). Provide formal proofs that sum-form aggregation reduces to a telescoping potential with unbounded shaping magnitude (explaining reward hacking) while min-form corresponds to a truncated potential (explaining gradient information loss), thereby unifying PURE's empirical findings under PBRS theory. Integrate these shaped rewards into GRPO training of a policy model with online value function updates, comparing against PRIME, PURE, SHAPE (MC potentials), and TDRM baselines. Evaluate on MATH500, GSM8K, AIME 2024, and ProcessBench, with ablations on discount factor γ, TD(λ) parameters, and amortized neural versus Monte Carlo potential estimation.\n\n## Detailed Description\n\nWe propose Value-Function Process Reward Models (VF-PRM), a principled framework that trains PRMs as state value functions and derives step-level rewards via potential-based reward shaping (PBRS). Current PRMs are trained as step-correctness classifiers but heuristically repurposed as RL rewards through aggregation (sum, min, product), causing reward hacking or information loss with no theoretical justification for aggregation choice. VF-PRM trains V(s_t) ≈ P(correct | prefix₁:t) using TD(λ) with outcome-only supervision, then computes step rewards as F_t = γV(s_{t+1}) − V(s_t). By the Ng et al. (1999) policy invariance theorem, these shaped rewards provably preserve the optimal policy while providing dense gradients. We prove that existing sum-form and min-form aggregations correspond to specific suboptimal potential function choices, providing the first theoretical explanation for PURE's empirical findings and PRIME's implicit PBRS connection. Unlike concurrent work SHAPE (ACL 2026) which uses expensive Monte Carlo rollout potentials, our amortized neural value function requires no inference-time rollouts and supports online updates during RL training. Experiments with Qwen2.5-Math-7B and GRPO training target consistent improvements over PURE, PRIME, SHAPE, and TDRM baselines across MATH500 (beating PURE's 82.6%), GSM8K, and AIME 2024 (beating TDRM's 36.7%).\n\n## Key References\n\n- Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping (ICML 1999)\n- Process Reinforcement through Implicit Rewards — PRIME (ICLR 2026)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025)\n- Smooth Reward Models with Temporal Difference for LLM RL and Inference — TDRM (arXiv 2025)\n- Linking Process to Outcome: Conditional Reward Modeling — CRM (ICLR 2026)\n- DuaShepherd: Integrating Stepwise Correctness and Potential Rewards (arXiv 2025)\n- Pretrain Value, Not Reward: Decoupled Value Policy Optimization — DVPO (ICLR 2026)\n- SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning (ACL 2026)\n- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning — PAV (ICLR 2025)\n- Step Potential Advantage Estimation — SPAE (arXiv 2026)\n- Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation — RARL survey (arXiv 2026)\n- From Reasoning to Agentic: Credit Assignment in RL for LLMs (arXiv 2026)\n- Outcome-supervised Value Models for Planning in Mathematical Reasoning — OVM (NAACL 2024)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~2,400 H100-hours (VF-PRM training ~200h, GRPO RL runs ×6-8 ablations ~2,000h, eval ~200h), timeline: 12-16 weeks (sequential: 3w infrastructure, 4w VF-PRM training & tuning, 4w RL experiments, 3w analysis & writing), estimated_gpu_cost: $5,000-7,000 (H100 at ~$2.50/GPU-hr on Lambda/RunPod)\n- **human_in_loop**: gpu_hours: ~2,000 H100-hours (fewer failed runs via Claude-assisted debugging and config generation), timeline: 8-11 weeks (2w infra, 3w VF-PRM, 3w RL experiments, 2w writing), claude_api_cost: $300-500 (code generation, experiment analysis, paper drafting), estimated_gpu_cost: $4,000-6,000\n- **auto_research**: gpu_hours: ~2,500 H100-hours (broader automated hyperparameter sweeps), timeline: 5-7 weeks (parallelized experiment scheduling, automated analysis), claude_api_cost: $600-1,200 (orchestration, iterative experiment design, full paper generation), estimated_gpu_cost: $5,000-7,500, speed_bottleneck: RL training wallclock: ~36h per GRPO run on 8×H100 is irreducibly sequential; 6-8 ablation runs cannot be fully parallelized without 48-64 GPUs\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T08:40:16.716Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:40:16.716Z",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T08:40:16.729Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct the evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

1. **TCRM — "Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling"** (arXiv 2604.22981, April 2026):
   核心主张与本 proposal 高度重叠。TCRM 在 Bradley-Terry loss 之上加 MC 和 TD 正则项，证明最优解等于条件期望（即 value function）。在 ProcessBench 上达到 44.9% F1（无需 step-level 标注），中间 token 的 pairwise accuracy 从 50% 提升到 88.9%。本质上也是 "reward model = value function + TD training"。虽然 TCRM 面向 general RLHF 而非数学推理 PRM-RL，但核心概念移动（"用 TD 训练 RM 使其成为 value function"）与 VF-PRM 大面积重合。**这是对 proposal novelty 的最大威胁。**

2. **SHAPE — "Stage-aware Hierarchical Advantage via Potential Estimation"** (ACL 2026, arXiv 2604.06636):
   **直接竞争者。** 显式引用 Ng et al. (1999) PBRS，用 Monte Carlo 估计 potentials，应用于 GRPO advantage 修改。实验显示 +3% accuracy、30% fewer tokens。Proposal 正确识别了其局限（MC rollout 而非 learned V(s_t)），但 SHAPE 的存在表明 PBRS+LLM reasoning 不再是 "open gap"，而是 "已有初步实现，需要改进" 的状态。

3. **PURE — "Stop Summation: Min-Form Credit Assignment"** (NeurIPS 2025, arXiv 2504.15275):
   提出 min-form credit assignment 替代 sum-form，显著缓解 reward hacking。Proposal 声称将给出 sum/min 在 PBRS 框架下的理论解释，这是一个有价值的理论贡献，但 PURE 的实证结论已经被社区广泛接受。

4. **PRIME — "Process Reinforcement through Implicit Rewards"** (ICLR 2026, arXiv 2502.01456):
   从 ORM token probabilities 提取隐式 process rewards，自身论文已承认 "可视为 PBRS 其中 q-value 是 potential"。Qwen2.5-Math-7B-Base 上 +15.1% average improvement。这意味着 PBRS 在 PRM-RL 中的应用**已经被隐式实现且验证有效**。

5. **TDRM — "Smooth Reward Models with Temporal Difference"** (arXiv 2509.15110, Sep 2025):
   用 n-step TD learning 训练 PRM，tree-search 提升 23.7%，20× data efficiency。与 VF-PRM 共享 "用 TD 学习训练 reward model" 的核心技术选择，但仍需 step-level 标注。

6. **PAV — "Rewarding Progress"** (ICLR 2025):
   计算 step reward 为 MC success probability 的变化量——这在概念上与 PBRS potential difference 等价，但未建立形式化联系。Proposal 正确指出了这一点。

7. **DuaShepherd** (arXiv 2506.17533, June 2025):
   分离 correctness 和 potential 两个 reward head，MATH500/ProcessBench SOTA，但仅在 inference-time（best-of-N）评估。

8. **rePIRL** (arXiv 2602.07832, Feb 2026):
   用 inverse RL 框架统一现有 PRM 训练方法，声称是第一个将 IRL 推广到 LLM reasoning 的工作。

9. **CRM — "Conditional Reward Modeling"** (ICLR 2026):
   将 step reward 定义为条件概率 P(correct|s_{1:t})，在 BoN/beam search/RL 全面评测，但无 PBRS 保证。

10. **Credit Assignment Survey — "From Reasoning to Agentic"** (arXiv 2604.09459, April 2026):
    覆盖 47 种方法，proposal 声称该 survey 未识别 "trained neural V(s_t) + explicit PBRS + RL training" 这一特定组合。

- **调研总结**: PRM-RL credit assignment 是 2025-2026 年最拥挤的研究前沿之一。PBRS 已被 SHAPE 显式实现（MC potentials）、被 PRIME 隐式实现（token probabilities）、被 TCRM 通过 TD 正则化部分实现。VF-PRM 的特定组合（trained V(s_t) via TD(λ) + PBRS formula + GRPO integration）确实尚未被精确填充，但构成该组合的**每个单独组件都已有近期工作覆盖**，proposal 的贡献更多是"组合+理论统一"而非"新范式"。

---

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁。** 

最直接的替代方案：PRIME（已有 ICLR 2026）已经隐式实现了 PBRS（其论文自称 "viewable as PBRS where q-value is the potential"），且不需要额外训练单独的 value function，直接从 ORM token probabilities 提取。如果 PRIME + GRPO 已经在相同 setting（Qwen2.5-Math-7B）上取得 +15.1% 改进，VF-PRM 需要证明 explicit V(s_t) training 显著优于 PRIME 的 implicit 方式。

另一个替代：SHAPE（ACL 2026）已经显式使用 PBRS，只是用 MC rollout 而非 learned V(s_t)。VF-PRM 的增量价值在于 "amortized neural V(s_t) 比 MC rollout 更高效且支持 online updates"。这是一个合理但**量级有限**的改进——MC rollout 的成本在 SHAPE 中已被证明可控（30% fewer tokens），neural V(s_t) 能否带来实质性的进一步提升是存疑的。

**增量价值的核心**在两个地方：(1) sum/min aggregation 在 PBRS 下的形式化证明——这是纯理论贡献；(2) learned V(s_t) 相比 MC potentials 的效率优势。前者有价值但不够 "surprising"；后者需要实证支撑。

---

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **"V(s_t) ≈ P(correct | prefix₁:t) 可以用 TD(λ) + outcome-only supervision 高效且准确地训练"**——这是最关键的前提。TCRM 已经表明 TD 正则化可以诱导 temporal coherence，但 TCRM 是在 Bradley-Terry preference data 上训练的，而 VF-PRM 只用 binary outcome labels。二者的数据分布完全不同。用纯 outcome labels 做 TD(λ) 训练 V(s_t) 的质量——特别是对中间步骤的估值准确性——是未经验证的。TD(λ) 在 tabular/small-state RL 中的收敛性质不能直接迁移到 LLM 推理的高维、非平稳状态空间。

2. **"PBRS 的 policy invariance guarantee 在 LLM RL（GRPO）setting 中依然成立"**——Ng et al. (1999) 的 policy invariance 定理基于 MDP 假设（Markov property、tabular or function approximation with adequate representational capacity）。LLM reasoning 的 state 是可变长度的 token sequence，GRPO 是一种 on-policy approximate 算法，其与 PBRS 定理前提的匹配度存疑。Proposal 声称 "provably preserves the optimal policy"，但这个 "provably" 的前提条件在实际 setting 中可能不满足。

3. **"sum-form 对应 telescoping potential with unbounded shaping magnitude" 可以严格证明**——这需要看具体证明。Sum-form aggregation（Σ PRM_scores）和 PBRS 中的 telescoping sum 之间的映射是否严格，取决于 PRM scores 的具体数学性质。如果 PRM 本身不是一个满足 PBRS potential 条件的函数，这个映射可能只是 approximate analogy 而非 formal proof。

---

【3 维度打分】:

1. **Novelty: 中（偏弱）**
   
   理由：VF-PRM 的核心贡献是"组合+理论统一"：将 TD-trained V(s_t)、PBRS formula、GRPO training 三者显式结合。但：
   - TCRM (April 2026) 已经证明 "reward models = value functions + TD training"，核心概念移动被覆盖；
   - SHAPE (ACL 2026) 已经显式实现 PBRS for LLM reasoning；
   - PRIME (ICLR 2026) 已经隐式实现 PBRS for RL training 且自我承认这一联系；
   - TDRM (Sep 2025) 已经使用 TD learning 训练 PRM。
   
   剩余的 novelty delta 主要在：(a) 理论上统一 sum/min aggregation under PBRS——这是有价值的但属于 "elegant formalization of known phenomena" 而非 "surprising new finding"；(b) explicit neural V(s_t) 而非 MC rollout potentials——这是 implementation choice 层面的差异。在如此拥挤的竞争环境中，剔除 surface differences 后的 novelty 有限。

2. **Significance: 中**
   
   理由：研究问题本身非常重要——PRM-RL integration 的 credit assignment 是 LLM reasoning 的核心挑战，RARL survey 将其列为 open problem。但：
   - 如果实验结果是 "VF-PRM 在 MATH500 上比 PURE 高 2-3%"，审稿人很可能反应是 "I would have guessed this"——用 learned value function 替代 heuristic aggregation 当然应该更好，这不 surprising；
   - 理论贡献（PBRS 统一 sum/min）的实际影响取决于社区是否认为 "我们需要一个理论来解释 PURE 的实验发现"——考虑到 PURE 已被 NeurIPS 接受且其实证结论被广泛采纳，理论解释的边际价值有限；
   - 对领域的可推广性：框架是否能推广到数学推理之外（代码生成、agent 场景）未被讨论。

3. **Related Work: 强**
   
   理由：这是 proposal 的最大亮点。作者对相关工作的覆盖极其全面——PURE、PRIME、SHAPE、TDRM、CRM、DuaShepherd、PAV、SPAE、DVPO、RARL survey、credit assignment survey 均被准确识别和定位。特别是：
   - 正确识别了 SHAPE 作为 critical concurrent work 并精确描述了其局限；
   - 正确描述了 PRIME 的 PBRS 联系；
   - 正确描述了 PAV 的概念等价性；
   - 对每篇论文的差异化定位清晰（best-of-N vs RL、MC vs neural、step vs token）。
   
   **但有一个重要遗漏：TCRM (arXiv 2604.22981, April 2026) 未被提及**——这篇论文直接主张 "reward models are secretly value functions" 并使用 TD 正则化，与 VF-PRM 的核心概念高度重叠。在最终提交前必须纳入讨论。

---

【概率估计】: 18% - 30%，中位 23%

【估计理由】:
- **Novelty 是主要限制因素**。在 TCRM、SHAPE、PRIME、TDRM 四篇直接竞争工作存在的前提下，VF-PRM 的 novelty delta 被显著压缩。核心概念移动（"RM = V function + TD training" 和 "PBRS for LLM reasoning"）均已被近期工作覆盖，剩余贡献集中在"组合"和"理论统一"层面。
- **Significance 的上界受限于 "expected" 性质**。如果核心实验结果是 positive（VF-PRM > PURE/PRIME），审稿人大概率反应是 "makes sense, not surprising"——用 principled value function + PBRS 替代 heuristic aggregation 自然应该更好。这限制了论文的 impact narrative。
- **Related Work 覆盖出色**是 positive signal，说明作者对领域有深入理解，但这属于执行质量而非 idea 质量。
- **理论贡献**（PBRS 统一 sum/min）是最有差异化价值的部分，如果证明严谨且 insight 深刻，有可能将概率推向上界。但如果只是 "straightforward formalization"，则价值有限。
- 上界 30% 对应：理论证明确实深刻 + 实验显著超越所有 baselines + TCRM 被充分 differentiate；下界 18% 对应：理论被审稿人认为 trivial formalization + 实验改进 marginal + TCRM/SHAPE 的 novelty 挤压。

【主要风险】:
1. **Novelty 被 concurrent work 瓦解**：TCRM (April 2026, 未被 proposal 提及) 已实现 "RM as value function + TD training"，SHAPE 已实现 "explicit PBRS for LLM reasoning"。审稿人可能认为 VF-PRM 是这两个已知方向的 straightforward combination，缺乏 sufficient novelty increment。
2. **"Expected positive" 问题**：核心实验若 positive，审稿人会认为这是 "the principled approach beats heuristic, as expected"——无 surprise value。论文的 acceptance 需要远超预期的实验改进幅度（e.g., >5% on MATH500 over PURE），或者理论贡献被认为独立有价值，两者均不确定。
```

Sources:
- [TCRM: Reward Models Are Secretly Value Functions](https://arxiv.org/abs/2604.22981)
- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation](https://arxiv.org/abs/2604.06636)
- [PURE: Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)
- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)
- [TDRM: Smooth Reward Models with Temporal Difference](https://arxiv.org/abs/2509.15110)
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)
- [PAV: Rewarding Progress](https://arxiv.org/abs/2410.08146)
- [CRM: Conditional Reward Modeling](https://openreview.net/forum?id=4DJoBOQNd0)
- [rePIRL: Learn PRM with Inverse RL](https://arxiv.org/abs/2602.07832)
- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)
- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/abs/2602.09305)
- [Credit Assignment Survey: From Reasoning to Agentic](https://arxiv.org/abs/2604.09459)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make a well-informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

- SHAPE (ACL 2026, arXiv:2604.06636): 最直接的竞争工作。明确引用 Ng et al. (1999) PBRS 理论，将 Monte Carlo 估计的 potential 应用于 LLM 推理，在 GRPO 的 advantage 计算中注入 PBRS 项，实现 +3% 准确率和 30% token 减少。但使用 training-free MC rollout 估计 potential（非学习的 value function），且仅修改 GRPO advantage 而非作为独立 PRM 训练目标。

- PURE (NeurIPS 2025, arXiv:2504.15275): 证明 sum-form credit assignment 导致 reward hacking（甚至在训练初期就 collapse），提出 min-form credit assignment 显著缓解。但仅提供经验性证据，缺乏理论解释——这恰恰是本 proposal 声称要填补的 gap。在 3 个 base model 上，min-form 在 30% steps 内达到 verifiable reward 方法的可比性能。

- PRIME (ICLR 2026, arXiv:2502.01456): 从 ORM token probabilities 中提取 implicit process rewards，实现 online PRM 更新。论文本身承认"可以被视为 PBRS，其中 q-value 是 potential function"，但使用启发式提取而非显式 value function 训练。

- TDRM (arXiv:2509.15110): 应用 TD learning 平滑 PRM 标签，tree-search 提升 23.7%，数据效率提升 20×。但仍需要 step-level annotations，且目的是平滑现有标签而非从头训练 value function。技术路径与本 proposal 有重叠但目标不同。

- CRM (ICLR 2026, OpenReview): 将 step rewards 建模为条件概率 P(correct|s_{1:t})，在 BoN、beam search 和 RL 三个场景评估。缺乏 PBRS 保证，仍使用 MC 估计的 step labels。

- DuaShepherd (arXiv:2506.17533): 分离 correctness 和 potential reward 两个头，multi-head 架构。MATH500/ProcessBench SOTA。但仅评估 inference-time (BoN)，未用于 RL 训练。

- PAV (ICLR 2025, arXiv:2410.08146): 将 step reward 定义为 "progress"——prover policy 在执行该 step 前后成功率的变化。概念上与 PBRS potential differences 完全一致，但未建立正式 PBRS 联系，也未训练专门模型。比 ORM 5× compute efficient，RL 中 6× sample efficient。

- SPAE (arXiv:2601.03823): Training-free 方法，用 probing 提取中间 confidence 和 correctness 作为 "Step Potential" 信号。PBRS-inspired potential differences + 启发式复合指标。

- Credit Assignment Survey (arXiv:2604.09459): 覆盖 47 种 CA 方法，按 token/segment/step/turn 粒度和方法论分类。**未识别 "trained neural V(s_t) + explicit PBRS step rewards + RL training" 这一具体组合为已有方法**。

- Bootstrapped Reward Shaping (arXiv:2501.00989): 在经典 RL 中使用 agent 当前 value estimate 作为 PBRS 的 potential function，有 tabular 收敛证明和 Atari 实验。但未应用于 LLM 推理。

- DVPO (ICLR 2026, arXiv:2502.16944): 预训练 Global Value Model 作为 frozen critic，40% less GPU memory。但在 response-level 操作，非 step-level process supervision。

- 调研总结: PRM-RL integration 是 2025-2026 年最激烈竞争的前沿方向。PBRS 理论已通过 SHAPE 被引入 LLM 推理领域（MC rollout 路线），TDRM 已将 TD learning 引入 PRM 训练，PRIME 已注意到 PBRS 联系但未显式实现。"训练 neural V(s_t) + 显式 PBRS 推导 step rewards + 用于 RL 训练"这一精确组合确实是 open gap，但其各个组成部分已在不同工作中被分别探索。本 proposal 处于多条已有工作线索的交叉点——这既是机遇（整合价值），也是风险（novelty 被分散）。


【Trivial Alternative 检验】:

存在两个显著的 trivial alternative 威胁：

(1) **SHAPE 的 MC rollout 路线**: SHAPE 已经使用 PBRS + MC 估计的 potential 实现了 +3% 准确率提升和 30% token 减少。本 proposal 的核心增量是"用 trained neural V(s_t) 替代 MC rollout V(s_t)"——但这是一个 amortization 工程优化，而非概念性创新。如果 MC rollout 在质量上并不显著劣于 neural V(s_t)（尤其考虑到 VinePPO 等工作表明 MC 估计在 language environment 中可以很有效），那增量价值有限。

(2) **PURE min-form + 标准 PRM**: 直接使用 PURE 的 min-form credit assignment + 现有 PRM 训练方法已经能取得不错效果。本 proposal 提供理论解释但未必带来实践提升——"解释为什么 min works better"的学术价值取决于是否产生可操作的改进。

**增量价值所在**: (a) 理论统一——将 sum/min/product 统一为 PBRS 框架下不同 potential function 的特例，提供 PURE 经验发现的首个理论解释；(b) 无需 step annotation——TD(λ) + outcome-only supervision 比 TDRM（需要 step labels）更 practical；(c) online value function update 支持 RL 训练中的持续适应。这些增量价值是真实的，但核心问题是理论解释和 amortization 是否足以构成顶会级贡献。


【前提假设检验】:

核心逻辑链中有 3 个关键未验证假设：

(1) **"TD(λ) 能在 LLM reasoning 的 state space 上训练出准确的 V(s_t)"**: 这是最大的风险假设。现有趋势恰恰相反——GRPO 移除了 value network（因为 value function 在 LLM RL 中训练困难且不稳定），VinePPO 的工作明确指出 value networks "barely outperform random baselines when comparing alternative steps"。在如此高维、稀疏反馈的 state space 中，TD(λ) + outcome-only supervision 是否能训练出质量足够好的 V(s_t) 是一个重大实证问题。

(2) **"sum-form aggregation 可以 reduce to telescoping potential with unbounded shaping magnitude"的数学推导**: 虽然 proposal 声称会提供 formal proofs，但将离散 PRM scores 的 sum 映射到 continuous PBRS 框架需要特定的数学假设。这些假设在 LLM reasoning 的实际设置中是否成立需要验证。

(3) **"amortized neural V(s_t) 优于 MC rollout V(s_t)"**: SHAPE 使用 MC rollout 已取得不错效果。在 language environment 中 MC rollout 相对 cheap（只需要 forward pass），而 neural V(s_t) 引入了额外的 training cost 和 approximation error。net benefit 并非显然为正。


【3 维度打分】:

1. **Novelty: 中** — 核心贡献是将 PBRS 理论与 PRM training 的显式整合，以及将 sum/min/product aggregation 统一为 PBRS 特例的理论分析。这确实是一个未被填补的 gap——credit assignment survey (arXiv:2604.09459) 确认 "trained neural V(s_t) + explicit PBRS + RL training" 组合不存在于已有文献中。然而，各组成部分均已被独立探索：SHAPE 已在 LLM 推理中实现 PBRS（MC 路线），TDRM 已将 TD learning 用于 PRM，PRIME 已指出 PBRS 联系，PAV 已概念性地使用 potential differences。理论统一（aggregation → PBRS 特例）是最有价值的 novelty delta，但一旦建立 PBRS 框架，sum 的 telescoping 性质和 min 的 truncation 性质是相对直接的推论。总体而言，novelty 是真实的但属于增量整合型，而非范式转换型。

2. **Significance: 中偏强** — 问题非常重要且时机恰好。PRM-RL integration 是 2025-2026 年 LLM reasoning 领域最核心的开放问题之一。RARL survey 明确将 "principled aggregation design guidelines" 列为 central open problem。如果理论分析确实能为 aggregation 选择提供可操作的指导（而不仅仅是事后解释），实际影响力会很大。但 significance 的上限受制于这些理论洞见是否能转化为 consistently better 的实践结果——如果最终只是"理论上更优雅但实践上和 PURE/SHAPE 差不多"，影响力会打折。

3. **Related Work: 强** — 这是 proposal 最突出的优势。对竞争格局的理解极其透彻：准确识别了 SHAPE、PURE、PRIME、TDRM、CRM、DuaShepherd、PAV、SPAE 等所有关键工作，精确描述了每篇的贡献和局限，并清晰定位了本 proposal 填补的具体 gap。特别值得注意的是对 concurrent work SHAPE 的诚实处理——不回避最直接的竞争，而是明确阐述差异化（learned vs. MC potentials）。这种 landscape awareness 在我的调研中得到了完全验证。


【概率估计】: [25% - 38%] 中位 30%

【估计理由】:
Novelty 是真实的但属于增量整合型（"principled combination of known ingredients"），这决定了上限不会太高。最核心的 novelty——aggregation schemes 的 PBRS 理论统一——虽然新颖但可能被视为"连接已知理论的 straightforward application"。SHAPE (ACL 2026) 作为极度接近的 concurrent work 是最大的 novelty 压力源；审稿人可能认为 "MC rollout → learned V(s_t)" 是工程改进而非概念突破。Significance 较强——问题很重要，时机好——这拉高了下限（不太可能因为"问题不重要"被拒）。Related work 是强项，降低了被拒的概率但不增加中稿概率。

限制上界的维度是 **Novelty**：在 SHAPE、PRIME、TDRM、PAV 等工作的包围下，剩余的 novelty delta 需要审稿人认可"理论统一 + 学习型 value function"的组合价值。如果审稿人认为理论贡献是 straightforward，上界会被压到 25% 左右；如果审稿人重视理论统一的实用价值，可达 38%。

此外，前提假设检验中的第(1)点——TD(λ) 在 LLM state space 上能否训练出质量足够好的 V(s_t)——是一个方向性风险。如果 value function 训练不出来，整个 framework 的实践价值就不存在，只剩理论分析，这对顶会投稿来说可能不够。

【主要风险】:
1. **Novelty 被 SHAPE 挤压**: SHAPE (ACL 2026) 已经将 PBRS 引入 LLM reasoning 并取得正面结果。审稿人很可能将本 proposal 视为 SHAPE 的 incremental variant（"learned potential instead of MC potential"），如果 performance gain 不显著，novelty 评分可能被压至 borderline。
2. **Value function 训练可行性逆趋势**: 当前 LLM RL 领域的主流趋势是远离 value networks（GRPO 移除 value model，VinePPO 表明 value networks 在 LLM 中表现差），本 proposal 逆势而行要训练 neural V(s_t)。如果 V(s_t) 训练效果不理想，不仅实验不好看，还会动摇 framework 的实用性论证。
```

Sources:
- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/html/2604.06636)
- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275)
- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)
- [TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference](https://arxiv.org/abs/2509.15110)
- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://openreview.net/forum?id=4DJoBOQNd0)
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)
- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146)
- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)
- [Credit Assignment Survey: From Reasoning to Agentic](https://arxiv.org/abs/2604.09459)
- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/abs/2602.09305)
- [Bootstrapped Reward Shaping](https://arxiv.org/pdf/2501.00989)
- [DVPO: Pretrain Value, Not Reward](https://arxiv.org/html/2502.16944)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **SHAPE (ACL 2026, arXiv 2604.06636)**: 最直接的竞争者。显式引用 Ng et al. (1999) 将 PBRS 应用于 LLM 推理，使用 Monte Carlo 估计的 potential 函数，修改 GRPO 的 advantage 计算。实现 +3% 准确率、30% token 减少。与本 proposal 的核心差异仅在于 MC rollout potentials vs. learned neural value function。

2. **PRIME (ICLR 2026, arXiv 2502.01456)**: 从 ORM 的 token 概率中隐式提取 process reward，论文自身已明确指出"可视为 PBRS，其中 q-value 即 potential function"。这意味着 PBRS 与 process reward 的理论联系已在 PRIME 中被公开讨论，尽管 PRIME 未显式训练 value function。

3. **PURE (NeurIPS 2025, arXiv 2504.15275)**: 发现 sum-form credit assignment 导致 reward hacking，min-form 显著缓解。基于 Qwen2.5-Math-7B 的 PURE 在 AMC23 达到 82.5%。提供了纯经验证据但无理论解释——本 proposal 声称要提供这个理论解释。

4. **TDRM (arXiv 2509.15110, Sep 2025)**: 已经使用 TD learning 训练 PRM，将 value 估计作为 process reward。实现 tree-search +23.7%、20× 数据效率。与本 proposal 共享"用 TD 训练 value-function-like model"的核心技术路径，但 TDRM 未将输出显式框架为 PBRS potential。

5. **PAV (ICLR 2025, arXiv 2410.08146)**: 将 step reward 定义为"progress"——即 MC 成功概率的变化 ΔP(correct)。这在概念上等同于 F_t = V(s_{t+1}) − V(s_t)，只是未建立与 PBRS 的形式联系。

6. **DuaShepherd (arXiv 2506.17533, June 2025)**: 分离 correctness 和 potential 两个 reward head，在 MATH500/ProcessBench 上达到 SOTA。证明了 correctness 和 potential 是正交信号——支持本 proposal 的论点，但只在 inference-time (best-of-N) 评估。

7. **CRM (ICLR 2026, arXiv 2509.26578)**: 将 step reward 建模为条件概率 P(correct|s_{1:t})，在 RL 训练中评估。无 PBRS 保证但缓解了 reward hacking。

8. **SPAE (arXiv 2601.03823, Jan 2026)**: Training-free 的 PBRS-inspired potential difference 方法，使用启发式复合指标。

9. **DVPO (ICLR 2026, arXiv 2502.16944)**: 预训练 frozen Global Value Model 作为 universal critic，但在 response-level 而非 step-level。

10. **RARL Survey (arXiv 2602.09305, Feb 2026)**: 系统梳理 reward modeling 范式，明确指出"不同 aggregation scheme 产生 divergent policy behavior，principled design guidelines 缺失"。

- **调研总结**: PRM-RL 集成是 2025-2026 年最活跃的研究前沿之一。PBRS 与 LLM 推理的结合已有多项工作从不同角度触及：SHAPE 显式应用 PBRS（MC potentials）、PRIME 隐式使用 PBRS、PAV 在概念上等同于 potential difference、TDRM 用 TD 训练 value model。本 proposal 处于这些工作的交叉点，试图用"显式训练 neural V(s_t) + PBRS 步级 reward + RL 训练"这一特定组合来统一现有方法。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁：
- **TDRM + potential difference**: 直接取 TDRM 已训练好的 TD-based reward model 的输出，计算相邻步的差值作为 shaped reward。这几乎就是 VF-PRM 的核心操作，但不需要重新设计训练框架。
- **SHAPE 的 MC potentials**: SHAPE 已证明用 MC rollout 估计 potential 配合 PBRS 即可获得 +3% 提升和 30% token 减少。Neural value function 相对于 MC estimation 的增量价值不明确——MC 估计可能在给定计算预算下更准确（无函数近似误差）。
- **PRIME 的隐式 PBRS**: PRIME 已经在实践中隐式使用 PBRS 并取得强结果。将其"显式化"的实际收益需要实证。

增量价值主要体现在：(a) 理论统一——证明 sum/min 是 PBRS 的退化特例；(b) 避免 MC rollout 的推理开销；(c) 支持在线更新。但 (a) 更偏理论贡献，(b)(c) 的实际优势幅度待验证。

【前提假设检验】:
核心 claim 的逻辑链中有几个未经验证的假设：

1. **"Neural V(s_t) 优于 MC potential estimation"**: 这是相对于 SHAPE 的关键差异化论点，但未有理论或实证支撑。函数近似引入 bias（value function approximation error），而 MC estimation 有 variance 但无 bias。在 LLM reasoning 的 episode 通常较短（几十步）的场景下，MC 估计可能足够精确，neural approximation 的优势不明显。

2. **"Formal PBRS guarantees 在实践中有意义"**: Ng et al. (1999) 的 policy invariance 定理要求精确的 potential function。当 V(s_t) 是一个有近似误差的 neural network 时，PBRS 的理论保证不再严格成立。Proposal 没有讨论 approximate PBRS 的误差传播。

3. **"证明 sum/min 是退化特例会带来实际改进"**: 理论上证明 sum-form 导致 reward hacking 可以解释 PURE 的发现，但这个证明本身不直接产生更好的方法。如果 PURE 的 min-form 已经 empirically 有效，那么"解释为什么它有效"的价值更偏理论 insight 而非方法改进。

4. **"TD(λ) + outcome-only supervision 能训练出高质量 V(s_t)"**: 虽然 TDRM 证明了 TD 训练的可行性，但 TDRM 使用的是 step-level annotations。仅用 outcome labels 做 TD(λ) 时，信号极度稀疏（每个 episode 只有一个 binary signal），value function 的学习效率和质量存疑。

【3 维度打分】:

1. **Novelty: 中** — 本 proposal 的每个组件都有 closely related 的先驱工作：TD 训练 → TDRM；PBRS 显式应用 → SHAPE；PBRS 隐式使用 → PRIME；potential difference → PAV；correctness vs. value 分离 → DuaShepherd。真正的 novelty delta 在于将这些组件以一种特定方式组合，并提供理论统一框架（证明 sum/min 是 PBRS 退化）。这个理论贡献是 genuine 的——credit assignment survey (Apr 2026) 确认这一精确组合尚无先例——但属于"对已知理论（PBRS, 1999）的自然应用到当前热点问题"，而非概念性突破。SHAPE (ACL 2026) 是最直接的 threat：它已经做了"PBRS + LLM reasoning"，本 proposal 的差异化仅在于 neural vs. MC potentials，这更像是一个 engineering variant 而非 conceptual advance。

2. **Significance: 中偏强** — 研究问题本身高度重要：PRM-RL 集成中 aggregation scheme 的理论缺失是 RARL survey 明确指出的 open problem。如果理论证明 solid 且 empirical gains 显著，对该领域有实际推动作用。然而，practical significance 受限于：(a) PURE 的 min-form 已经 empirically 有效，"为什么有效"的解释价值低于"什么更有效"；(b) 该领域竞争极度激烈，多项同期工作在快速蚕食 novelty space；(c) 贡献的可推广性主要限于 mathematical reasoning 场景。

3. **Related Work: 强** — Proposal 对领域的把握出色。覆盖了 PRIME、PURE、SHAPE、TDRM、CRM、DuaShepherd、DVPO、PAV、SPAE 及两篇 survey，对每篇工作的差异化定位清晰且准确（经调研验证，所有引用的论文真实存在，描述基本准确）。特别是对 SHAPE 作为 critical concurrent work 的识别和差异化分析到位。唯一可改进的是：应更深入讨论与 TDRM 的技术路径重叠，以及 PRIME 中已公开的 PBRS 连接意味着什么。

【概率估计】: [22% - 35%] 中位 28%

【估计理由】:
- Related Work 维度强，说明 proposal 作者对领域有深刻理解，不会因 ignorance of prior work 被拒，这拉高了下限。
- Significance 中偏强——问题确实重要，AAAI 审稿人会认同 PRM-RL 集成值得研究。
- **Novelty 是上界的主要限制因素**。核心问题是：当审稿人看到 SHAPE 已在 ACL 2026 做了 "explicit PBRS + LLM reasoning"，PRIME 已讨论了 PBRS connection，TDRM 已用 TD 训练 value model 时，会问"这篇论文真正 new 的是什么？" 答案是"learned neural potential + 理论统一 sum/min"，这个 delta 是 real 但 modest。
- 审稿人很可能说 "I would have guessed this"——将 PBRS（一个 1999 年的经典结果）应用到 PRM 是一个自然的 next step，而非 surprising insight。这将概率限制在 35% 以下。
- 如果 empirical results 能显著 beat PURE/SHAPE/PRIME (>2% on MATH500, >5% on AIME)，概率可推至上界；如果只是 marginal improvement 或 comparable，概率在下界附近。

【主要风险】:
1. **Novelty 被 SHAPE 严重稀释**: SHAPE (ACL 2026) 已显式应用 PBRS 到 LLM reasoning 并取得显著效果。审稿人会视本 proposal 为 SHAPE 的 incremental variant（neural vs. MC potentials），而非独立贡献。本 proposal 的理论统一部分可能被视为"对 PURE 发现的 post-hoc rationalization"而非 forward-looking insight。
2. **"Natural application of known theory" 风险**: 将 Ng et al. (1999) 的经典 PBRS 定理应用到 PRM 是领域内任何熟悉 RL theory 的人都会想到的方向（PRIME 已经提到了这个连接）。审稿人可能认为这是一个 "low-hanging fruit" 而非 genuine intellectual contribution。
```

Sources:
- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/html/2604.06636)
- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)
- [PRIME: Process Reinforcement through Implicit Rewards (ICLR 2026)](https://openreview.net/forum?id=CmyqMn3HeJ)
- [TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference](https://arxiv.org/abs/2509.15110)
- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning (ICLR 2026)](https://openreview.net/forum?id=4DJoBOQNd0)
- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (ICLR 2025)](https://arxiv.org/abs/2410.08146)
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)
- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)
- [DVPO: Pretrain Value, Not Reward: Decoupled Value Policy Optimization (ICLR 2026)](https://openreview.net/forum?id=qirGds1BmK)
- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/abs/2602.09305)


【原始 proposal（允许参考但不是主要依据）】:
# Potential-Valued Process Rewards for Principled Step-Level Credit Assignment

## Core Problem

Current PRMs are trained as step-correctness classifiers but heuristically repurposed as RL reward signals via aggregation (sum, min, product), causing either reward hacking or information loss. No principled framework connects PRM design to RL training quality, despite potential-based reward shaping (PBRS) theory guaranteeing policy invariance — a well-known result never practically implemented for step-level process rewards in mathematical reasoning.

## Research Opportunity

Three independent 2025-2026 findings converge: (1) the RARL survey confirms PBRS 'lacks practical PRM implementation' for reasoning RL; (2) DuaShepherd proves step correctness and step value (potential) are orthogonal signals — yet all existing PRMs train only on correctness; (3) PURE demonstrates that sum-form PRM aggregation causes training collapse, while min-form loses useful gradient information, but provides no theoretical justification for why min works better. Training a PRM as a state value function V(s_t) = P(correct | prefix₁:t) and deriving step rewards as potential differences r_t = γV(s_{t+1}) − V(s_t) would unify these findings: PBRS guarantees no policy distortion, value-function training requires only outcome labels (no expensive step annotations), and the framework naturally subsumes sum/min/product as suboptimal special cases with specific potential-function choices.

## Research Landscape

PRM-RL integration is the most contested frontier. PURE (NeurIPS 2025) showed min-form credit assignment avoids reward hacking that collapses sum-form training 'even at the beginning,' but provides only empirical justification. TDRM (Sep 2025) applies TD learning to smooth PRM labels, achieving 23.7% improvement in tree-search and 20× data efficiency, but still requires step-level annotations and doesn't address the aggregation problem. CRM (ICLR 2026) models step rewards as conditional probabilities P(correct|s_{1:t}) causally linked to outcomes, evaluating on best-of-N, beam search, AND RL — but lacks PBRS guarantees and still uses MC-estimated step labels. PRIME (ICLR 2026) extracts implicit process rewards from ORM token probabilities and is acknowledged as 'viewable as PBRS where q-value is the potential,' but uses heuristic extraction rather than explicit value function training. DuaShepherd (June 2025) separates correctness and potential reward heads, achieving SOTA on MATH500/ProcessBench, but evaluates only at inference time (best-of-N), not RL training. DVPO (ICLR 2026) pretrains a Global Value Model for general RLHF with 40% less GPU memory, but operates at response-level, not step-level process supervision. The RARL survey (Feb 2026) catalogs reward modeling paradigms and identifies the central open problem: 'Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent.' CRITICAL CONCURRENT WORK: SHAPE (ACL 2026) applies PBRS with Monte Carlo-estimated potentials to LLM reasoning, explicitly citing Ng et al. (1999), achieving +3% accuracy with 30% fewer tokens — but uses training-free MC rollouts (not a learned value function) and only modifies GRPO advantages rather than serving as a standalone PRM training objective. SPAE (Jan 2026) uses training-free PBRS-inspired potential differences with a heuristic composite metric. PAV (ICLR 2025) estimates step 'progress' as change in MC success probability, conceptually identical to PBRS but without formal connection or a trained model. The credit assignment survey (Apr 2026) covers 47 methods across token/segment/step/turn granularity and does NOT identify the specific combination of trained neural V(s_t) + explicit PBRS step rewards + RL training as an existing method — suggesting this precise integration remains an open gap.

## Proposed Approach

Train a Process Reward Model as an explicit state value function V(s_t) ≈ P(correct | prefix₁:t) on Qwen2.5-Math-7B using TD(λ) with only binary outcome supervision, requiring no step-level annotations. Derive dense step-level rewards via the classical PBRS formula F_t = γV(s_{t+1}) − V(s_t), which provably preserves the optimal policy under Ng et al. (1999). Provide formal proofs that sum-form aggregation reduces to a telescoping potential with unbounded shaping magnitude (explaining reward hacking) while min-form corresponds to a truncated potential (explaining gradient information loss), thereby unifying PURE's empirical findings under PBRS theory. Integrate these shaped rewards into GRPO training of a policy model with online value function updates, comparing against PRIME, PURE, SHAPE (MC potentials), and TDRM baselines. Evaluate on MATH500, GSM8K, AIME 2024, and ProcessBench, with ablations on discount factor γ, TD(λ) parameters, and amortized neural versus Monte Carlo potential estimation.

## Detailed Description

We propose Value-Function Process Reward Models (VF-PRM), a principled framework that trains PRMs as state value functions and derives step-level rewards via potential-based reward shaping (PBRS). Current PRMs are trained as step-correctness classifiers but heuristically repurposed as RL rewards through aggregation (sum, min, product), causing reward hacking or information loss with no theoretical justification for aggregation choice. VF-PRM trains V(s_t) ≈ P(correct | prefix₁:t) using TD(λ) with outcome-only supervision, then computes step rewards as F_t = γV(s_{t+1}) − V(s_t). By the Ng et al. (1999) policy invariance theorem, these shaped rewards provably preserve the optimal policy while providing dense gradients. We prove that existing sum-form and min-form aggregations correspond to specific suboptimal potential function choices, providing the first theoretical explanation for PURE's empirical findings and PRIME's implicit PBRS connection. Unlike concurrent work SHAPE (ACL 2026) which uses expensive Monte Carlo rollout potentials, our amortized neural value function requires no inference-time rollouts and supports online updates during RL training. Experiments with Qwen2.5-Math-7B and GRPO training target consistent improvements over PURE, PRIME, SHAPE, and TDRM baselines across MATH500 (beating PURE's 82.6%), GSM8K, and AIME 2024 (beating TDRM's 36.7%).

## Key References

- Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping (ICML 1999)
- Process Reinforcement through Implicit Rewards — PRIME (ICLR 2026)
- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025)
- Smooth Reward Models with Temporal Difference for LLM RL and Inference — TDRM (arXiv 2025)
- Linking Process to Outcome: Conditional Reward Modeling — CRM (ICLR 2026)
- DuaShepherd: Integrating Stepwise Correctness and Potential Rewards (arXiv 2025)
- Pretrain Value, Not Reward: Decoupled Value Policy Optimization — DVPO (ICLR 2026)
- SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning (ACL 2026)
- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning — PAV (ICLR 2025)
- Step Potential Advantage Estimation — SPAE (arXiv 2026)
- Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation — RARL survey (arXiv 2026)
- From Reasoning to Agentic: Credit Assignment in RL for LLMs (arXiv 2026)
- Outcome-supervised Value Models for Planning in Mathematical Reasoning — OVM (NAACL 2024)

## Resource Estimate

- **manual**: gpu_hours: ~2,400 H100-hours (VF-PRM training ~200h, GRPO RL runs ×6-8 ablations ~2,000h, eval ~200h), timeline: 12-16 weeks (sequential: 3w infrastructure, 4w VF-PRM training & tuning, 4w RL experiments, 3w analysis & writing), estimated_gpu_cost: $5,000-7,000 (H100 at ~$2.50/GPU-hr on Lambda/RunPod)
- **human_in_loop**: gpu_hours: ~2,000 H100-hours (fewer failed runs via Claude-assisted debugging and config generation), timeline: 8-11 weeks (2w infra, 3w VF-PRM, 3w RL experiments, 2w writing), claude_api_cost: $300-500 (code generation, experiment analysis, paper drafting), estimated_gpu_cost: $4,000-6,000
- **auto_research**: gpu_hours: ~2,500 H100-hours (broader automated hyperparameter sweeps), timeline: 5-7 weeks (parallelized experiment scheduling, automated analysis), claude_api_cost: $600-1,200 (orchestration, iterative experiment design, full paper generation), estimated_gpu_cost: $5,000-7,500, speed_bottleneck: RL training wallclock: ~36h per GRPO run on 8×H100 is irreducibly sequential; 6-8 ablation runs cannot be fully parallelized without 48-64 GPUs


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c4b23ecb-227a-458b-804d-193bb2538d29",
  "type": "user",
  "uuid": "b2cc94f2-8d6d-484a-ae9e-16a385720b3c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:40:16.727Z_

```json
{
  "parentUuid": "b2cc94f2-8d6d-484a-ae9e-16a385720b3c",
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
  "uuid": "6b4e3b45-5a9f-4c02-99b8-266b387ef9d7",
  "timestamp": "2026-05-27T08:40:16.727Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:40:16.728Z_

```json
{
  "parentUuid": "6b4e3b45-5a9f-4c02-99b8-266b387ef9d7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7789b9de-dd71-4e98-93e6-5b0a410d35d8",
  "timestamp": "2026-05-27T08:40:16.728Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct the evaluation. L…",
  "leafUuid": "7789b9de-dd71-4e98-93e6-5b0a410d35d8",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal on value-function process rewards",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:40:46.457Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Novelty: 中（偏弱）
- Significance: 中
- Related Work: 强
- Probability: [18% - 30%] 中位 23%

**Reviewer 2:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [25% - 38%] 中位 30%


**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [22% - 35%] 中位 28%

Now I'm looking at the three median probabilities—23%, 30%, and 28%—and calculating their aggregate statistics. The mean comes to 27%, the median is 28%, and the standard deviation is around 2.6, which shows fairly tight agreement among the reviewers.

With a standard deviation in the 3-7% range, this falls into the "中一致" category, so I should widen the interval slightly and lean toward the stricter assessment. Let me check which dimensions have consensus across reviewers.

Most of the key issues show strong agreement: all three reviewers identify novelty as "中", flag SHAPE as the primary threat, recognize PRIME's implicit PBRS connection, and raise concerns about TD(λ) training feasibility. They also converge on viewing this as a combination of known techniques, with the theoretical contribution around sum/min operations under PBRS being the main novelty differentiator. There are a few outlier positions—R1 specifically calls out TCRM—but the core assessment is quite aligned.

R1 flagged a paper on temporally coherent reward modeling that directly challenges VF-PRM's core premise about reward models being value functions, which is a valid and important finding the other reviewers missed. This shifts my view of R1's lower novelty rating and 23% probability estimate as potentially more justified than initially apparent. Looking at the three median probabilities of 23%, 28%, and 30%, I need to synthesize these into a final assessment.

Given the medium consistency across reviewers and the principle of being conservative with acceptance, I'm leaning toward the stricter end of the range. R1's discovery of the TCRM paper is a genuine additional threat that should pull the estimate down, but all three reviewers agree the related work is comprehensive, which provides some floor. My final estimate is around 26% with a range of 20-33%, acknowledging R1's stricter but well-supported assessment while not dismissing R2 and R3's points about the significance of the work.

Now I'm moving on to assess the implementation feasibility based on the proposal's resource estimates and the reviewers' feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7789b9de-dd71-4e98-93e6-5b0a410d35d8",
  "isSidechain": false,
  "requestId": "req_011CbSmpyBuEKuEA4pBMCH1q",
  "type": "assistant",
  "uuid": "c8203172-2042-4182-8af2-e59aa66a3346",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015St8hTBKHf3LJveuSMTWbP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22248,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3568,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 22248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22248
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

_source line 9 · 2026-05-27T08:41:36.606Z_

【阶段】: Meta Judge
【三次中位】: [23%, 28%, 30%]  std=3.6%
【共识维度】:
- **Novelty = 中**（3/3 一致，R1 略偏弱至"中偏弱"，R2/R3 均为"中"）：核心判断一致——VF-PRM 是"已知组件的 principled combination"，每个组件（TD 训练→TDRM、PBRS 应用→SHAPE、PBRS 隐式联系→PRIME、potential difference→PAV）均已有近期先驱工作覆盖，真正的 novelty delta 集中在理论统一（sum/min→PBRS 退化特例）和 learned V(s_t) vs. MC rollout 的具体技术选择上。
- **Significance = 中至中偏强**（R1 判中，R2/R3 判中偏强）：3/3 一致认为问题本身高度重要（RARL survey 确认为 open problem），但 practical significance 受限于"expected positive"问题——用 principled approach 胜过 heuristic 不 surprising。
- **Related Work = 强**（3/3 一致）：proposal 对竞争格局的覆盖出色，对 SHAPE/PURE/PRIME/TDRM 等每篇工作的差异化定位准确。
- **SHAPE 是最大 novelty 威胁**（3/3 一致）：SHAPE (ACL 2026) 已显式将 PBRS 应用于 LLM reasoning，本 proposal 相对 SHAPE 的差异化仅在 neural vs. MC potentials，3 位审稿人均质疑此增量是否构成顶会级 conceptual advance。
- **TD(λ) 训练可行性风险**（3/3 一致）：在 LLM RL 主流趋势远离 value network（GRPO 移除 value model、VinePPO 表明 value networks 表现差）的背景下，仅用 outcome-only supervision 做 TD(λ) 训练 V(s_t) 的质量是重大实证风险。
- **PBRS policy invariance 前提可能不满足**（R1/R3 明确指出，R2 隐含）：Ng et al. (1999) 定理基于 MDP 假设，LLM reasoning 的高维非平稳状态空间下"provably preserves optimal policy"的 claim 存疑。
- **理论贡献是最有价值的 novelty delta**（3/3 一致）：但 3/3 同时担忧该理论贡献可能被视为"straightforward formalization"或"post-hoc rationalization of PURE's findings"。

【异常维度】:
- **R1 独家发现 TCRM (arXiv 2604.22981, April 2026) 未被 proposal 引用**：该论文标题为"Reward Models Are Secretly Value Functions"，核心主张与 VF-PRM 高度重叠（用 TD 正则化使 RM 成为 value function），R2/R3 未提及此论文。经判断，这是 R1 的有效发现而非 outlier——TCRM 的核心概念移动（"RM = value function + TD training"）确实直接覆盖了 VF-PRM 的核心 framing，构成额外的 novelty 压力。**采信此发现，应上调 novelty 风险。**
- **R1 的 Novelty 评级"中偏弱"**略低于 R2/R3 的"中"：考虑到 R1 额外发现了 TCRM 这一直接竞争者，该评级差异有合理依据，不视为 outlier。

【最终概率】: [20% - 33%] 中位 26%
【一致性】: 中
【综合理由】:
三份评审在所有核心维度上高度趋同：Novelty 是主要限制因素（增量整合型而非范式转换型），Significance 受"expected positive"问题制约，Related Work 是明确强项但不加概率。Std=3.6% 属中一致区间，按规则加宽区间并偏向更严格方向。

R1 的 TCRM 发现是有效的降权因素——该论文（April 2026）标题直接宣称"Reward Models Are Secretly Value Functions"并使用 TD 正则化，与 VF-PRM 的核心 framing 大面积重叠，而 proposal 未提及，构成额外 novelty 威胁。这使最终概率向 R1 的更严格评估倾斜。

最终中位 26% 的定位逻辑：
- **天花板（~33%）**：理论证明 sum/min→PBRS 退化确实深刻且非 trivial + 实验显著 beat 所有 baselines（PURE/SHAPE/PRIME >3%）+ TCRM 被充分 differentiate
- **地板（~20%）**：理论被视为 straightforward formalization + 实验改进 marginal + TCRM/SHAPE 双重 novelty 挤压 + V(s_t) 训练不出理想效果
- 综合后的估计不超过三份评审中最宽松的 R2（中位 30%），且偏向最严的 R1 方向

【建议】: 边缘（偏不推荐）

该 proposal 有真实的学术价值（理论统一框架、问题重要性、相关工作掌握出色），但在当前极度拥挤的竞争环境中（SHAPE/TCRM/PRIME/TDRM 四重 novelty 挤压），剩余的 novelty delta 较薄。建议进入迭代优化流程，重点方向：(1) 强化理论贡献的深度和不可替代性（不能只是 straightforward formalization）；(2) 必须纳入 TCRM 讨论并明确差异化；(3) 实验设计需要制造 "surprise"——不能只是 "principled method beats heuristic as expected"。若优化后理论贡献被认可为 genuine insight 且实验有超预期结果，有可能推至 35%+ 的边缘可接受区间。

【实施评估】:
- **计算资源**: ~2,000-2,500 H100-hours（VF-PRM 训练 ~200h + GRPO RL 6-8 组消融实验 ~2,000h + 评测 ~200h），预估 GPU 成本 $4,000-7,500（H100 @ ~$2.50/hr，Lambda/RunPod 等平台）。需 8×H100 节点，单次 GRPO 训练 ~36h 为不可压缩瓶颈。
- **数据需求**: 公开数据集（MATH500、GSM8K、AIME 2024、ProcessBench），均可直接获取。VF-PRM 训练仅需 binary outcome labels（无需昂贵的 step-level 标注），这是方法论优势。
- **人工介入**: 中等。理论证明需要研究者手工推导和验证（PBRS 下 sum/min 的形式化证明）；实验调参（TD(λ) 参数、discount factor γ）需要人工判断。无需人工标注数据。
- **训练需求**: 需要训练 (1) Value function V(s_t)（基于 Qwen2.5-Math-7B 架构，TD(λ) + outcome supervision）和 (2) Policy model（GRPO 训练）。模型规模 7B，单次训练可控。核心风险在 V(s_t) 的训练质量——这是整个框架的前提。
- **新 Benchmark**: 不需要。使用现有标准 benchmark（MATH500、GSM8K、AIME 2024、ProcessBench）。
- **预估周期**: 8-16 周（取决于自动化程度）。关键路径：基础设施搭建 2-3 周 → VF-PRM 训练与调优 3-4 周 → RL 实验 3-4 周 → 分析与写作 2-3 周。RL 训练的 wallclock time 是瓶颈，6-8 组消融无法在 8×H100 上完全并行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8203172-2042-4182-8af2-e59aa66a3346",
  "isSidechain": false,
  "requestId": "req_011CbSmpyBuEKuEA4pBMCH1q",
  "type": "assistant",
  "uuid": "27ec2714-a7cd-4867-bc6b-eecc44c85146",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015St8hTBKHf3LJveuSMTWbP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22248,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3568,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 22248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22248
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct the evaluation. L…",
  "leafUuid": "27ec2714-a7cd-4867-bc6b-eecc44c85146",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal on value-function process rewards",
  "sessionId": "4ee6b29f-5a23-4738-a05f-6cfccfd34472"
}
```

---
