# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/3ef25cbe-392f-4452-b762-81b977742f79.jsonl`
- **Structured JSON:** [`047f4bc6487d5cc59d2f.json`](../../sessions/04/047f4bc6487d5cc59d2f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T09:31:16.977Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T09:31:16.977Z",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- SHAPE (arXiv 2604.06636, ACL 2026): 最直接的竞争者。已经在 LLM 推理中显式实现了 PBRS，使用 MC 估计的势函数修改 GRPO 的优势函数，报告了 +3% 准确率和 30% token 压缩。与本 proposal 的核心区别仅在于 MC 势 vs. 学习的神经势函数。\n- PAV — \"Rewarding Progress\" (ICLR 2025 Spotlight, arXiv 2410.08146): 将 step reward 定义为\"进展\"——执行一步前后 MC 成功概率的变化——概念上与 PBRS 势差高度相似。已实现 6× sample efficiency 和 7%+ 准确率提升。被接为 Spotlight，说明社区对这种思路认可度高。\n- PURE (NeurIPS 2025, arXiv 2504.15275): Min-form credit assignment 解决了 sum-form 导致的 reward hacking，纯实证方案无理论框架。本 proposal 提出用 PBRS 理论统一解释 sum/min/product 聚合的行为差异，这是对 PURE 观察的理论补全。\n- BSRS — Bootstrapped Reward Shaping (AAAI 2025, arXiv 2501.00989): 在标准 RL 中已提出用 agent 当前 V 估计作为 PBRS 势函数，提供了 tabular 收敛证明和 Atari 验证。这是本 proposal\"学习 V + PBRS\"核心思路的直接前身，只是在标准 RL 而非 LLM 场景。\n- CRM — Conditional Reward Modeling (ICLR 2026): 将 step reward 建模为条件概率 P(correct|s_{1:t})，捕捉步骤间因果关系。覆盖 BoN、beam search、RL 三场景，但无 PBRS 保证。\n- PRIME (ICLR 2026, arXiv 2502.01456): 从 ORM token 概率中提取隐式过程奖励，自身已被社区认为\"可视为 PBRS where q-value is the potential\"。在无需显式 PRM 训练的情况下实现了有竞争力的 RL 训练结果。\n- TDRM (arXiv 2509.15110, Sep 2025): 已将 TD learning 应用于 PRM 平滑，实现 20× 数据效率，但需要 step-level annotations。本 proposal 使用 TD(λ) + outcome-only supervision，是关键区别。\n- OVM (NAACL 2024, arXiv 2311.09724): 用 outcome supervision 训练 V(s_t) 用于推理规划（beam search），是本 proposal 在 V(s_t) 训练思路上最直接的知识前驱。区别在训练方法（TD(λ) vs. MC returns）和用途（PBRS step rewards vs. beam search pruning）。\n- VinePPO (NeurIPS 2024, arXiv 2410.01679): 证明 PPO 中的 value network 在 LLM 推理任务中\"几乎不比随机基线好\"，这是本 proposal 试图解决的核心动机之一。但 VinePPO 的解法是绕开 V（用 MC 估计），而非修复 V。\n- RL^V (arXiv 2505.04842, 2025): 联合训练 LLM 作为推理器和验证器，恢复 value function。与本 proposal 动机相同（\"把 V 带回来\"），但路径不同（self-verification vs. separate model + PBRS）。\n- SPAE (arXiv 2601.03823, Jan 2026): Training-free PBRS-inspired 势差方法，使用探测机制提取 confidence 和 correctness 信号。无需训练的轻量方案。\n- DuaShepherd (arXiv 2506.17533, June 2025): 双头架构分离 correctness 和 potential reward。验证了二者确实捕捉不同信号。但仅评估推理阶段（BoN），未涉及 RL 训练。\n- RARL Survey (arXiv 2602.09305, Feb 2026): 明确指出\"不同聚合方案产生截然不同的策略行为，但原则性设计指南仍然缺失\"——本 proposal 试图填补的空白。\n\n- 调研总结: PRM 的 step-level credit assignment 是 2025-2026 年 LLM RL 领域最热门的子方向之一，已有多篇顶会论文从不同角度切入（PURE 做聚合实证、PAV 做进展度量、SHAPE 做 MC-PBRS、PRIME 做隐式奖励、CRM 做条件概率建模）。这个领域极度拥挤。本 proposal 的独特定位是\"学习神经 V + 显式 PBRS + 理论统一框架\"，各单独组件均有前驱（BSRS 做学习 V-PBRS、OVM 做 outcome-supervised V、TDRM 做 TD 训练），核心 novelty 在于 (1) 将聚合方案统一为 PBRS 特例的理论框架，(2) 在 LLM reasoning 场景中将 BSRS 思路与 outcome-only supervision 结合。\n\n\n【Trivial Alternative 检验】:\n存在多个成本更低的替代方案构成直接威胁：\n1. **SHAPE 的 MC-PBRS**: 无需训练额外模型，直接用 MC rollouts 估计势函数，已实现 +3% 准确率。如果 VF-PRM 的学习 V 相比 MC 估计没有显著优势（特别是在短-中长度推理问题上 MC 方差可控时），VF-PRM 的额外训练成本难以证成。\n2. **PRIME 的隐式 PBRS**: 无需显式 PRM 训练，从 ORM token 概率直接提取 step reward，已被社区认为\"可视为 PBRS\"，且在 ICLR 2026 被接收。\n3. **PAV 的进展度量**: 概念上等价于 PBRS 势差，ICLR 2025 Spotlight，已证明 6× sample efficiency。\n\nVF-PRM 的增量价值在于：(a) 推理成本 O(1) vs. MC 的 O(K·T)，在超长推理链上有计算优势；(b) 在线可更新避免分布偏移（PAV 固定于初始 prover policy）；(c) 理论统一框架提供解释力。但这些增量是否足够\"surprising\"是关键问题。\n\n\n【前提假设检验】:\n核心逻辑链中有两个未经充分验证的环节：\n\n1. **\"TD(λ) + outcome-only supervision 能训练出足够准确的 V(s_t)\"**: 这是整个方法成立的前提。VinePPO 已经证明在线训练的 value network 在 LLM 推理中极不可靠。Proposal 认为这是因为在线 critic 依赖\"noisy policy rollouts\"，而 VF-PRM 用 ground-truth outcome labels 训练单独模型所以更稳定。但这个论证并不充分——VinePPO 的发现暗示 V(s_t) 在 LLM 推理的高维序列空间中本身就难以学习，不仅仅是噪声问题。TD(λ) 的 bootstrapping 是否引入了更多偏差（尤其在 V 估计初期不准确时）也未验证。\n\n2. **\"PBRS 的 policy invariance 保证在 approximate setting 中有实际意义\"**: Ng et al. 1999 的理论保证基于表格/精确设定。在深度神经网络函数逼近 + 有限训练步数 + 非平稳策略分布的实际 LLM RL 中，policy invariance 仅是渐近性质，可能不产生实际优势。BSRS 在 Atari 中验证了这一点的可行性，但 LLM 的动作空间（token vocabulary）和状态空间（自然语言序列）与 Atari 有本质区别。\n\n\n【3 维度打分】:\n  1. Novelty: 中 — 核心方法是对已有组件的组合：学习 V 作 PBRS 势函数 (BSRS, AAAI 2025)、outcome-supervised V 训练 (OVM, NAACL 2024)、TD 学习用于 PRM (TDRM, 2025)、PBRS 应用于 LLM 推理 (SHAPE, ACL 2026; PAV, ICLR 2025)。各单独组件均有近期前驱。真正新颖的是将 PRM 聚合方案（sum/min/product）统一为 PBRS 特例的理论框架——这是一个有价值的理论贡献，但其本质是为已知实证现象（PURE 的 min > sum）提供事后解释，而非预测性新发现。在如此拥挤的赛道上，\"better motivated combination of known ingredients\" 的 novelty delta 有限。\n\n  2. Significance: 中 — 问题本身无疑重要：step-level credit assignment 是 LLM RL 的核心瓶颈，RARL survey 明确指出\"principled design guidelines remain absent\"。理论统一框架如果成立，对社区有长期参考价值。但实际影响取决于 VF-PRM 能否在实验中显著超越 SHAPE/PAV/PRIME 等已有方案。如果差距不大，这将沦为一个\"理论上更优雅但实践上并不更好\"的工作——这类论文在顶会中接收率较低。此外，该方法受限于需要额外训练一个 value model 的计算开销，在\"推理 scaling\"成为主流趋势的当下，computation overhead 是实际部署的障碍。\n\n  3. Related Work: 强 — 覆盖极为全面，识别了 15+ 篇高度相关论文，对每一篇的定位和差异化都有具体说明。特别是对 SHAPE (MC-PBRS)、PAV (progress-as-potential)、BSRS (learned V-PBRS)、OVM (outcome-supervised V) 的差异化论证是清晰且诚实的。Survey 级别的文献覆盖是明确的优势。唯一的小隐患是部分引用的会议年份/状态可能尚未最终确认（如 ACL 2026 SHAPE），但对 proposal 阶段而言可以接受。\n\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \nRelated Work 覆盖是强项，但不直接决定接收率。Novelty 是核心瓶颈：这个 idea 的本质是\"将 BSRS (AAAI 2025) 的思路迁移到 LLM reasoning 场景 + 加上聚合方案的 PBRS 理论统一\"——这是一个 well-motivated combination，但在 SHAPE (ACL 2026) 已经做了 PBRS + LLM reasoning、BSRS (AAAI 2025) 已经做了 learned V + PBRS 的背景下，组合的增量 novelty 有限。理论统一贡献（sum/min/product → PBRS 特例）是真实的 delta，但属于\"解释已知现象\"而非\"预测新现象\"，审稿人可能评价为 \"nice but incremental\"。Significance 受制于实践优势的不确定性——如果实验结果仅与 SHAPE/PRIME/PAV 持平或微幅领先，论文将很难获得足够的审稿人热情。上界被 Novelty 限制：即使实验完美执行，核心 insight (\"用学习的 V 做 PBRS 比 MC 做 PBRS 更好\") 是审稿人\"would have guessed this\"的范畴，不是反直觉发现。\n\n【主要风险】: \n1. **\"Better engineering of known ideas\" 定性风险**: 审稿人可能认为 VF-PRM = BSRS + OVM + TDRM 的组合应用于 LLM 场景，各组件均已发表，组合的 intellectual contribution 不够一篇独立论文。\n2. **Trivial alternative 竞争力风险**: 如果 SHAPE 的 training-free MC-PBRS 在实验中表现与 VF-PRM 差距不大（尤其在中等长度推理链上），审稿人会质疑为什么需要额外训练一个 value model——Occam's razor 将倾向于更简单的方案。\n```\n\nSources:\n- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation](https://arxiv.org/abs/2604.06636)\n- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146)\n- [PURE: Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)\n- [BSRS: Bootstrapped Reward Shaping (AAAI 2025)](https://arxiv.org/abs/2501.00989)\n- [CRM: Linking Process to Outcome: Conditional Reward Modeling](https://openreview.net/forum?id=4DJoBOQNd0)\n- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)\n- [TDRM: Smooth Reward Models with Temporal Difference](https://arxiv.org/abs/2509.15110)\n- [OVM: Outcome-supervised Value Models for Planning](https://arxiv.org/abs/2311.09724)\n- [VinePPO: Refining Credit Assignment in RL Training of LLMs](https://arxiv.org/abs/2410.01679)\n- [RL^V: Putting the Value Back in RL](https://arxiv.org/abs/2505.04842)\n- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)\n- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/html/2602.09305v1)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- SHAPE (arXiv 2604.06636, ACL 2026): 最直接的竞争者。显式引用 Ng et al. (1999) PBRS，使用 MC rollout 估计 potential，修改 GRPO advantage，实现 +3% accuracy / -30% tokens。关键区别：training-free MC potentials vs. VF-PRM 的 learned neural V。但 SHAPE 已经证明 PBRS 在 LLM reasoning RL 中可行。\n- PAV (ICLR 2025 Spotlight, arXiv 2410.08146): 定义 step reward = progress (MC success probability 的变化量)，本质上就是 PBRS potential difference 的无折扣版本。RL 场景下实现 6× sample efficiency、7%+ accuracy gain。与 VF-PRM 的核心 idea 高度重叠，差异主要在 MC vs. learned V 和是否有 formal PBRS formulation。\n- PURE (NeurIPS 2025, arXiv 2504.15275): 证明 min-form 比 sum-form 更抗 reward hacking，但只提供经验观察，无理论框架。VF-PRM 的 PBRS 统一分析解释了 PURE 的现象。\n- BSRS (AAAI 2025, arXiv 2501.00989): 在标准 RL (tabular + Atari) 中使用 agent 当前 V 估计作为 PBRS potential，提供收敛证明。VF-PRM 本质上是 BSRS idea 在 LLM reasoning 场景的迁移。\n- OVM (NAACL 2024, arXiv 2311.09724): 用 outcome supervision 训练 V(s_t)，用于 inference-time planning（beam search）。VF-PRM 把 OVM 的 V 从 inference-time 扩展到 RL training，并改用 TD(λ) 替代 MC returns。\n- PRIME (ICLR 2026, arXiv 2502.01456): 从 ORM token probabilities 提取隐式 process reward，自称 \"viewable as PBRS where q-value is the potential\"。已在 ICLR 2026 接收。\n- CRM (ICLR 2026, OpenReview): 将 step reward 建模为条件概率 P(correct|s_{1:t})，ICLR 2026 接收。无 PBRS 保证。\n- TDRM (arXiv 2509.15110): 使用 TD learning 来平滑 PRM labels，但需要 step-level annotations。VF-PRM 仅需 outcome-only supervision。\n- DuaShepherd (arXiv 2506.17533, June 2025): 双头架构分离 correctness 和 potential，SOTA on MATH500/ProcessBench，但仅评估 inference-time (BoN)。VF-PRM 的 training-usage misalignment 论点部分受其启发。\n- VinePPO (NeurIPS 2024, arXiv 2410.01679): 证明 PPO 的 value network 在 LLM reasoning 中 \"consistently provide inaccurate estimates\"，MC rollout 作为替代。这既是 VF-PRM 的动机来源，也是最大的风险来源——VF-PRM 声称单独训练的 V 比 PPO critic 更准确，但尚未验证。\n- RL^V (arXiv 2505.04842, revised Apr 2026): 联合训练 LLM 为 reasoner + verifier，20%+ MATH boost。互补方向（自验证 vs. 独立 V model）。\n- RARL Survey (arXiv 2602.09305, Feb 2026): 明确指出 \"Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent\"——VF-PRM 正好填补此空缺。\n\n- 调研总结: PRM + RL 的 credit assignment 是 2025-2026 最活跃的 LLM reasoning 子领域之一。PBRS 已被 SHAPE 和 PRIME 显式/隐式引入，PAV 的 progress-based reward 与 PBRS potential difference 高度相似。VF-PRM 的独特定位是 \"learned neural V + TD(λ) + explicit PBRS + RL training + 理论统一\"，但每个组件都已在其他工作中出现，核心贡献是将它们 cohesively 组合并提供 PBRS-based 理论分析。\n\n【Trivial Alternative 检验】:\n存在两个直接的 trivial alternative 威胁：\n1. **SHAPE 的 MC-PBRS**：SHAPE 已经在 LLM reasoning RL 中使用了 PBRS + MC-estimated potentials。VF-PRM 的增量是用 learned V 替代 MC rollouts，声称低方差 + 可更新。但如果 SHAPE 的 MC potentials 在实践中已经足够好（+3% accuracy, -30% tokens），那 learned V 的额外收益可能有限。VF-PRM 的增量价值需要证明 learned V 在 long-horizon / 复杂问题上显著优于 MC potentials——这是合理的论点（MC 的 O(K·T) cost），但尚未验证。\n2. **PAV 的 progress reward**：PAV 使用 MC 估计的 progress (Δ success probability) 作为 step reward，概念上与 PBRS potential difference 几乎等价。PAV 已经在 RL 训练中取得了 6× sample efficiency。VF-PRM 相对于 PAV 的增量是 formal PBRS guarantee + 可在线更新的 learned V——这些是真实的差异，但审稿人可能会质疑实际 gap 有多大。\n\n增量价值所在：(a) 理论统一 framework 解释了为什么 sum-form hacks、min-form loses information，这是 SHAPE/PAV 都没有提供的；(b) amortized cost 在 long-horizon 问题上有实际优势。但这些增量是否足以支撑一篇完整论文，取决于实验中 learned V vs. MC 的实际 gap。\n\n【前提假设检验】:\n核心逻辑链有以下未经验证的关键假设：\n1. **\"独立训练的 V(s_t) 比 PPO online critic 更准确\"**——这是整个 proposal 的核心前提。VinePPO 证明 PPO 的 value network 不可靠，VF-PRM 声称独立训练 + ground-truth outcome labels 可以解决。但\"独立训练\"是否真的解决了根本问题（LLM reasoning 的状态空间巨大、V function 本身难以拟合）尚不清楚。如果 learned V 同样不准确，F_t = γV(s_{t+1}) − V(s_t) 会引入大量噪声，可能不如 MC estimates。\n2. **\"TD(λ) 优于 MC returns for V training\"**——proposal 声称 TD(λ) 提供更好的 bias-variance tradeoff，但在 LLM reasoning 的长序列环境中，TD bootstrapping 的 bias 可能很大（因为 V 本身不准确时 bootstrap target 也不准确），λ=1 退化为 MC returns。这个 tradeoff 在 LLM reasoning 特定场景下的表现是未知的。\n3. **\"Online VF-PRM updates 可以防止 staleness 而不 destabilize training\"**——在 RL 训练中同时更新 reward model 和 policy 是已知的不稳定因素（moving target problem）。Proposal 提到了 update frequency ablation，但是否能稳定训练是实验层面的未知。\n4. **\"V(s_t) 准确时 F_t ≈ A(s_t, a_t)\"**——这个数学关系在理想条件下成立，但在 LLM 的 token-level / step-level 混合 MDP 中，step boundary 的定义（\"\\n\\n\"）是 heuristic 的，F_t 是否真的近似 advantage 取决于 step 粒度是否匹配 decision granularity。\n\n其中假设 1 是最关键的——如果 learned V 不比 MC 好，整个 proposal 的 raison d'être 就不存在了。\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   理由：VF-PRM 的每个组件都已在现有工作中出现：outcome-supervised V(s_t) (OVM, NAACL 2024)、V 作为 PBRS potential (BSRS, AAAI 2025)、PBRS 用于 LLM reasoning (SHAPE, ACL 2026; PRIME, ICLR 2026)、progress-based step reward ≈ potential difference (PAV, ICLR 2025)。VF-PRM 的贡献是将这些组件 cohesively 组合，并提供 PBRS-based 的 PRM 聚合统一理论。这个理论统一是真实且有价值的——PURE 的 min > sum 现象得到了 PBRS 框架下的解释——但它更像是\"用已知理论解释已观察到的经验现象\"，而不是提出新的理论。相较于 SHAPE 和 PAV，VF-PRM 的 novelty delta 主要在 learned V vs. MC 和理论分析，属于 incremental improvement 而非 paradigm shift。审稿人可能会说 \"this is a natural combination of existing ideas\"。\n\n2. Significance: 【中偏强】\n   理由：研究问题本身非常重要——PRM 的 training-usage misalignment 和 credit assignment 是 2025-2026 LLM reasoning 的核心开放问题（RARL survey 明确指出）。如果 VF-PRM 显著优于 SHAPE/PAV/PURE，这对该领域的实践有直接影响。理论统一 framework 对理解现有方法有启发价值。但影响力受限于：(a) 这是一个已经非常拥挤的子领域，SHAPE/PAV/PURE/PRIME/CRM 已经提供了多种可用方案；(b) 实际增量可能有限——如果 learned V 只比 MC 好 1-2%，实践影响不大。\n\n3. Related Work: 【强】\n   理由：Related work 覆盖极为全面——涵盖了 PURE、SHAPE、PAV、PRIME、CRM、TDRM、DuaShepherd、OVM、BSRS、VinePPO、RL^V、DVPO、SPAE 等几乎所有相关工作，且每篇都有清晰的差异化定位。Proposal 还引用了两篇最新 survey (RARL, credit assignment)，并利用 survey 的 gap identification 来 justify 自身贡献。这种级别的 related work 覆盖和 positioning 在审稿中是加分项。唯一可能的遗漏是一些与 token-level credit assignment 相关的最新工作（如 Q#），但总体覆盖已经远超平均水平。\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】:\n- Related Work（强）确保了 proposal 不会因定位不清或遗漏关键工作而被拒，这是稳定的加分项\n- Significance（中偏强）意味着审稿人会认可问题的重要性\n- Novelty（中）是主要限制因素：每个组件都有 prior art（OVM, BSRS, SHAPE, PAV），组合虽然 coherent 但审稿人可能认为是 \"engineering contribution\"。SHAPE（ACL 2026）已经显式使用 PBRS，PAV（ICLR 2025 Spotlight）已经使用 progress-based step rewards 用于 RL training。VF-PRM 的增量（learned V vs. MC + 理论统一）是真实的但可能不够 surprising。\n- 理论贡献（统一分析）在审稿中是 double-edged：如果审稿人认为这些 proofs 是 PBRS 的直接应用（straightforward），那理论贡献的 perceived novelty 会降低\n- 上界（38%）对应\"learned V 在实验中显著优于 MC，理论分析被认为有启发价值\"的情景\n- 下界（25%）对应\"审稿人认为这是 BSRS + OVM 在 LLM 场景的直接迁移，novelty insufficient\"的情景\n\n【主要风险】:\n1. **\"Combination, not contribution\" 风险**：最可能的拒稿理由。审稿人可能认为 VF-PRM 是 OVM 的 V(s_t) + BSRS 的 V-as-potential + SHAPE 的 PBRS-in-LLM 的直接组合，每个组件都不新颖，组合也不够 surprising。尤其是 SHAPE 已经在 ACL 2026 接收了 PBRS + LLM reasoning 这个 idea。\n2. **核心前提可能不成立**：如果 learned V(s_t) 并不比 VinePPO/SHAPE 的 MC estimates 显著更准确（LLM reasoning 的高维状态空间可能使神经网络 V 的拟合同样困难），那 VF-PRM 相对于 SHAPE/PAV 的实际优势将非常有限，proposal 的核心 selling point 将被大幅削弱。\n```\n\nSources:\n- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/abs/2604.06636)\n- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146)\n- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275)\n- [BSRS: Bootstrapped Reward Shaping](https://arxiv.org/abs/2501.00989)\n- [OVM: Outcome-supervised Value Models for Planning in Mathematical Reasoning](https://arxiv.org/abs/2311.09724)\n- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)\n- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://openreview.net/forum?id=4DJoBOQNd0)\n- [TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference](https://arxiv.org/abs/2509.15110)\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards for Mathematical Reasoning](https://arxiv.org/abs/2506.17533)\n- [VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment](https://arxiv.org/abs/2410.01679)\n- [RL^V: Putting the Value Back in RL](https://arxiv.org/abs/2505.04842)\n- [DVPO: Pretrain Value, Not Reward: Decoupled Value Policy Optimization](https://arxiv.org/abs/2502.16944)\n- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)\n- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/abs/2602.09305)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have comprehensive information about the research landscape. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **SHAPE (arXiv 2604.06636, ACL 2026)**: 直接竞争者。已将 PBRS 引入 LLM 推理，使用 MC rollout 估算 potential，修改 GRPO advantage，实现 +3% 准确率和 30% token 节省。与 VF-PRM 的关键区别在于 SHAPE 使用 training-free MC 估算而非 learned neural V。但 SHAPE 已经证明 PBRS 在 LLM 推理中的有效性。\n\n2. **PAV / Rewarding Progress (arXiv 2410.08146, ICLR 2025 Spotlight)**: 概念上最接近的工作。将 step reward 定义为 progress（MC 成功概率的变化），本质上就是 PBRS 的 potential difference。实现了 6× sample efficiency 和 7%+ accuracy gain。与 VF-PRM 的区别：PAV 使用 per-step MC rollouts（O(K·T) 成本），VF-PRM 用 amortized neural V。\n\n3. **PURE (arXiv 2504.15275, NeurIPS 2025)**: 发现 min-form credit assignment 避免 reward hacking，sum-form 会 collapse。纯经验发现，缺乏理论解释。VF-PRM 的理论贡献之一就是用 PBRS 框架解释 PURE 的经验发现。\n\n4. **BSRS (arXiv 2501.00989, AAAI 2025)**: 直接使用 agent 当前 V 估计作为 PBRS potential。提供了 tabular 收敛证明和 Atari 验证。VF-PRM 本质上是 BSRS 思想在 LLM reasoning 场景的延伸。\n\n5. **OVM (NAACL 2024 Findings)**: 最直接的智识前驱。用 outcome supervision 训练 V(s_t)，用于 beam search pruning。VF-PRM 与 OVM 的区别：(1) TD(λ) vs MC returns 训练；(2) PBRS difference 作为 step reward vs 直接用 V(s_t) 做 beam search。\n\n6. **PRIME (arXiv 2502.01456, ICLR 2026)**: 从 ORM token 概率提取 implicit process rewards，作者自己承认\"可视为 PBRS where q-value is the potential\"。但使用启发式提取而非显式 value function 训练。\n\n7. **CRM (ICLR 2026)**: 将 step reward 建模为条件概率 P(correct|s_{1:t})。缺乏 PBRS policy invariance 保证。\n\n8. **TDRM (arXiv 2509.15110)**: 用 TD 学习平滑 PRM labels，但需要 step-level annotations。VF-PRM 使用 TD(λ) 但仅需 outcome supervision。\n\n9. **RL^V (arXiv 2505.04842)**: 解决相同动机——\"主流 RL 方法抛弃了 learned value function\"。联合训练 LLM 作为 reasoner 和 generative verifier。与 VF-PRM 互补：RL^V 走自验证路线，VF-PRM 走 separate value model + formal PBRS 路线。\n\n10. **VinePPO (NeurIPS 2024)**: 证明 PPO 中的 value networks \"consistently provide inaccurate estimates\"，改用 MC-based estimates。VF-PRM 需要回应这个发现——为什么 VF-PRM 的 V 不会遇到同样的问题。\n\n11. **SPAE (arXiv 2601.03823)**: Training-free PBRS-inspired potential differences，使用 composite heuristic metric。\n\n12. **DuaShepherd (arXiv 2506.17533)**: 分离 correctness 和 potential reward heads，实证证明二者 orthogonal。\n\n- **调研总结**: Process reward + PBRS 在 LLM reasoning 中是 2025-2026 极其拥挤的赛道。SHAPE 已经将 PBRS 显式引入 LLM reasoning（MC-based），PAV 已经在用 potential difference 做 step reward（MC-based），BSRS 已经在用 learned V 做 PBRS potential（Atari）。VF-PRM 的定位是这些方向的交汇点——\"learned neural V + explicit PBRS + LLM RL training\"——这个精确组合确实尚未被实现，但每个组件都已存在于不同工作中。真正的增量 novelty 在于 **理论统一**（用 PBRS 解释 aggregation schemes 的成败）而非方法本身。\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁**:\n\n1. **SHAPE + 蒸馏**: 最直接的替代——先用 SHAPE 的 MC rollouts 生成 potential estimates，然后训练一个 neural network 拟合这些 MC estimates（知识蒸馏）。这比 TD(λ) 方法更简单，且能继承 MC 的无偏性。VF-PRM 需要论证 TD(λ) 训练 V(s_t) 优于这种蒸馏方案，否则增量价值不清晰。\n\n2. **OVM + PBRS difference**: OVM 已经训练了 V(s_t)（用 MC returns），直接在 OVM 的 V(s_t) 上计算 F_t = γV(s_{t+1}) − V(s_t) 就行。VF-PRM 的 TD(λ) 训练相比 OVM 的 MC 训练的优势是什么？Proposal 声称 TD(λ) 提供更好的 bias-variance tradeoff，但这需要实证验证。\n\n3. **PRIME 本身**: PRIME 已经通过 implicit PRM 实现了高效的 process rewards，其隐式 PBRS 结构已被作者承认。VF-PRM 的 explicit PBRS 是否比 PRIME 的 implicit PBRS 更优？\n\n**增量价值主要在理论层面**: VF-PRM 的真正增量在于（a）理论统一 aggregation schemes，（b）提供 formal PBRS 保证。实践层面的增量（learned V vs MC potentials）需要实验证明。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的假设：\n\n1. **\"TD(λ) + outcome-only supervision 能训练出足够准确的 V(s_t)\"** — 这是整个方法的基石，但 VinePPO 已经证明 PPO 中的 value networks \"consistently provide inaccurate estimates\"。VF-PRM 声称因为使用 ground-truth outcome labels 和 separate model 所以不同，但这是**未经验证的假设**。如果 V(s_t) 不够准确，PBRS 的 F_t 就是噪声而非有效信号，整个方法就会失败。这是最关键的前提假设。\n\n2. **\"F_t 近似 advantage function 时提供 maximally informative dense gradients\"** — 理论上正确，但前提是 V(s_t) 足够准确。在 LLM reasoning 中，state space 极其高维（每个 token sequence 是一个 state），V(s_t) 的泛化能力存疑。特别是 reasoning chain 的中间状态可能非常 diverse，7B 模型的 V head 是否能准确估计这些状态的 value？\n\n3. **\"Online updates every k GRPO steps 能防止 distribution shift 导致的 staleness\"** — 这是一个合理但未经验证的设计选择。如果 policy 变化快于 V 的更新频率，PBRS 的 policy invariance 保证就会被打破（因为 V 不再对应当前 policy 的 value function）。\n\n4. **\"PBRS 的 policy invariance 在 function approximation setting 下仍然成立\"** — Ng et al. (1999) 的理论保证是在 tabular MDP 下证明的。在 deep RL / LLM 的 function approximation setting 下，PBRS 的 policy invariance 不严格成立。BSRS 在 deep RL 中也只是提供了 tabular 收敛证明。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   - **加分**: 理论统一贡献（用 PBRS 框架解释 sum-form/min-form 的成败）是真正的新颖点，目前没有看到任何现有工作做这个理论分析。RARL survey 和 credit assignment survey 都确认这是 open problem。testable prediction（|F_t| 分布随 V 改善而收敛）也是新的。\n   - **减分**: 方法层面，VF-PRM 是 BSRS（AAAI 2025, learned V as PBRS potential）+ OVM（NAACL 2024, outcome-supervised V training）+ TDRM（TD learning for PRM）的自然组合。SHAPE（ACL 2026）和 PAV（ICLR 2025）已经在 LLM reasoning 中实现了 PBRS / potential-difference 的 step reward。每个组件已存在，VF-PRM 是交汇点。\n   - 总结：理论贡献是 novel 的，方法贡献是 incremental synthesis。整体 novelty 为\"中\"而非\"强\"，因为方法的核心 insight（\"用 learned V 做 PBRS potential for LLM RL\"）在看到 BSRS + OVM + SHAPE 之后是一个 natural next step，审稿人可能会说 \"this combination was expected.\"\n\n2. **Significance: 中偏强** — \n   - **加分**: Credit assignment in LLM RL 是当前最重要的研究问题之一。PRM aggregation 的理论理解确实缺乏（RARL survey 明确指出）。如果理论统一成立，对整个 PRM + RL 社区都有指导意义。问题的重要性和时效性毋庸置疑。\n   - **减分**: 实际影响取决于 VF-PRM 是否在实验中显著优于 SHAPE / PAV / PURE 等已有方法。如果实验提升有限，理论统一虽好但 impact 打折。此外，领域移动极快，这些方法可能在论文发表前就被更新的范式（如 scaling test-time compute directly）supersede。\n\n3. **Related Work: 强** — \n   - Proposal 对相关工作的覆盖非常全面且准确。所有我调研到的关键竞争者（SHAPE, PAV, PURE, BSRS, OVM, PRIME, CRM, TDRM, RL^V, VinePPO, DuaShepherd, SPAE）都被提及，且差异化定位清晰。\n   - 特别值得肯定的是：(1) 对 PAV 和 SHAPE 的精确区分（MC vs learned, fixed vs online-updateable）；(2) 对 BSRS 的 honest positioning（承认 VF-PRM 是 BSRS 在 LLM reasoning 的延伸）；(3) 对 OVM 的智识传承定位准确；(4) 引用了两个 survey 确认 open problem。\n   - 微小不足：可以更显式地讨论 PAV 和 SHAPE 的实验结果，以论证 learned V 相比 MC 的实际优势有多少空间。\n\n【概率估计】: [28% - 38%] 中位 32%\n\n【估计理由】: \n- **Novelty（中）**是主要限制因素。方法是已有组件的 natural synthesis（BSRS + OVM + SHAPE 的交汇），审稿人很可能说 \"the combination is straightforward\"。理论统一贡献是加分项，但仅靠理论贡献在 AAAI 中稿偏难，除非实验上能展示出显著优势。\n- **Significance（中偏强）**提供了上行空间。问题确实重要且时效性强，如果实验结果证明 learned V 相比 MC methods（SHAPE/PAV）有显著优势，概率可以到 38%+。\n- **Related Work（强）**确保 proposal 不会因为 positioning 不当被拒，这是一个重要但非决定性的加分。\n- 上界限制来自 novelty：在这个极其拥挤的赛道上，synthesis-type 工作需要非常强的实验结果来弥补方法 novelty 的不足。理论贡献虽好，但 PBRS 理论本身不新（1999），应用到 LLM 的 adaptation 虽有技术含量但不足以 carry 全文。\n- 下界来自理论统一的真实价值：即使方法增量有限，用 PBRS 解释 sum-form 的 reward hacking 和 min-form 的成功是对该领域的 genuine theoretical contribution，且有 testable predictions。这不会被完全否定。\n\n【主要风险】: \n1. **\"Natural combination\" 质疑**: 审稿人很可能指出 VF-PRM = BSRS (AAAI'25) + OVM (NAACL'24) adapted to LLM RL，核心方法 novelty 不足。SHAPE (ACL'26) 已经证明 PBRS works for LLM reasoning，PAV (ICLR'25) 已经用 potential difference 做 step reward——VF-PRM 的实质增量仅是\"用 learned V 替代 MC rollouts\"，这更像是一个 engineering improvement 而非 conceptual advance。\n2. **V(s_t) 精度假设的脆弱性**: VinePPO 已经证明 LLM RL 中 value networks 估计不准。VF-PRM 声称 separate model + ground-truth labels 解决了这个问题，但如果实验中 V(s_t) 仍然不够准确（尤其在 distribution shift 时），整个 PBRS 框架就会退化为噪声信号，实验结果可能不如 SHAPE 的 MC-based 方法（无偏但高方差 vs 有偏但低方差的权衡可能不利于 VF-PRM）。\n```\n\n---\n\nSources:\n- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/abs/2604.06636)\n- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146)\n- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275)\n- [BSRS: Bootstrapped Reward Shaping](https://arxiv.org/abs/2501.00989)\n- [OVM: Outcome-supervised Value Models for Planning in Mathematical Reasoning](https://arxiv.org/abs/2311.09724)\n- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)\n- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://openreview.net/forum?id=4DJoBOQNd0)\n- [TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference](https://arxiv.org/abs/2509.15110)\n- [RL^V: Putting the Value Back in RL](https://arxiv.org/abs/2505.04842)\n- [VinePPO: Refining Credit Assignment in RL Training of LLMs](https://arxiv.org/abs/2410.01679)\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)\n- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)\n- [PBRS Topic Overview](https://www.emergentmind.com/topics/potential-based-reward-shaping-pbrs)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Potential-Valued Process Rewards for Principled Step-Level Credit Assignment\n\n## Core Problem\n\nCurrent Process Reward Models (PRMs) suffer from a fundamental training-usage misalignment: they are trained as step-correctness classifiers (\"is this step right?\") but repurposed as RL reward signals (\"how good is this step?\"). DuaShepherd (arXiv 2025, June 2025) empirically proves these are orthogonal signals — step correctness and step value (potential) capture different information — yet all existing PRMs train only on correctness. This misalignment forces practitioners to aggregate step-level correctness scores into RL rewards via heuristic schemes (sum, min, product), causing either reward hacking or information loss. No principled framework connects PRM design to RL training quality, despite potential-based reward shaping (PBRS) theory (Ng et al., ICML 1999) guaranteeing policy invariance — a well-known result never practically implemented as a PRM training objective for step-level process rewards in mathematical reasoning.\n\nMore broadly, mainstream LLM RL methods (GRPO, Leave-one-out PPO) have abandoned learned value functions in favor of empirically estimated returns (RL^V, arXiv 2025), while VinePPO (NeurIPS 2024) demonstrated that value networks in standard PPO \"consistently provide inaccurate estimates and struggle to rank alternative steps correctly.\" This creates a paradox: value functions are theoretically essential for credit assignment but practically unreliable in LLM RL. VF-PRM addresses this by training V(s_t) as a separate model with stable outcome supervision via TD(λ), rather than as an online critic dependent on noisy policy rollouts.\n\n## Headline Contributions\n\n1. **Theoretical Unification of PRM Aggregation under PBRS**: First framework to subsume PRM aggregation schemes (sum, min, product) under PBRS theory. We prove sum-form reduces to a telescoping potential with unbounded shaping magnitude (explaining PURE's observed reward hacking), min-form corresponds to a truncated potential (explaining gradient information loss), and learned V(s_t)-based PBRS provides adaptive magnitude control — the shaping magnitude self-regulates through value function accuracy, yielding a testable prediction: as V(s_t) improves during online training, |F_t| distributions should converge toward the advantage function's distribution.\n\n2. **Elimination of Training-Usage Misalignment**: VF-PRM directly trains V(s_t) ≈ P(correct | prefix₁:t) as a state value function using TD(λ) with outcome-only supervision, then derives step rewards via the PBRS formula F_t = γV(s_{t+1}) − V(s_t). Unlike correctness-trained PRMs heuristically repurposed as rewards, VF-PRM's training objective is natively aligned with its downstream RL usage. Unlike VinePPO's online critic (trained on noisy policy rollouts), VF-PRM uses ground-truth outcome labels and a separate model architecture, providing more stable V estimates. Online updates during RL training further prevent staleness as policy distribution shifts.\n\n3. **Amortized Neural Potentials with Bias-Variance Characterization**: Unlike SHAPE (ACL 2026) which uses training-free MC rollout potentials (unbiased but high-variance, cost O(K·T) per step for K rollouts over T steps), and unlike PAV (ICLR 2025) which uses MC-estimated progress without formal PBRS guarantees, VF-PRM's learned neural value function provides amortized, low-variance potential estimates via a single forward pass. We characterize this as a bias-variance tradeoff validated through neural vs. MC ablation.\n\n## Research Landscape\n\n**Aggregation problem (empirical only)**: PURE (NeurIPS 2025) showed min-form credit assignment avoids reward hacking that collapses sum-form training, achieving 82.6% on MATH500, but provides only empirical justification with no theoretical framework. VF-PRM provides the missing PBRS-based explanation and a principled alternative.\n\n**TD learning for PRMs (requires step annotations)**: TDRM (Sep 2025) applies TD learning to smooth PRM labels, achieving 23.7% improvement in tree-search and 20× data efficiency, but requires step-level annotations. VF-PRM uses TD(λ) for value function training with outcome-only supervision.\n\n**Conditional probability modeling (no PBRS guarantees)**: CRM (ICLR 2026) models step rewards as conditional probabilities P(correct|s_{1:t}), evaluating on best-of-N, beam search, and RL across six benchmarks, but lacks PBRS policy invariance guarantees.\n\n**Implicit PBRS (heuristic extraction)**: PRIME (ICLR 2026) extracts implicit process rewards from ORM token probabilities and is acknowledged as \"viewable as PBRS where q-value is the potential,\" but uses heuristic extraction rather than explicit value function training.\n\n**Dual-head separation (inference-only)**: DuaShepherd (June 2025) separates correctness and potential reward heads, achieving SOTA on MATH500/ProcessBench, but evaluates only inference-time (best-of-N).\n\n**MC-based PBRS (training-free, no learned V)**: SHAPE (ACL 2026) applies PBRS with Monte Carlo-estimated potentials, explicitly citing Ng et al. (1999), achieving +3% accuracy with 30% fewer tokens — but uses training-free MC rollouts and only modifies GRPO advantages. SPAE (Jan 2026, arXiv 2026) uses training-free PBRS-inspired potential differences with a heuristic composite metric. PAV (ICLR 2025 Spotlight) defines step reward as progress (change in MC success probability), achieving 6× sample efficiency and 7%+ accuracy gain in RL — conceptually closest to PBRS potential differences but with three critical distinctions from VF-PRM: (1) PAV uses per-step MC rollouts (O(K·T) cost, non-scalable for long-horizon problems) vs. VF-PRM's amortized single-pass neural V; (2) PAV's estimates are fixed to the initial prover policy vs. VF-PRM's online-updateable V; (3) PAV lacks formal γ-discounted PBRS formulation and policy invariance guarantees.\n\n**Response-level value pretraining**: DVPO (ICLR 2026) pretrains a Global Value Model for general RLHF with 40% less GPU memory, but operates at response-level, not step-level.\n\n**Outcome-supervised value models (inference-only, no PBRS)**: OVM (NAACL 2024) is the closest intellectual predecessor — it trains V(s_t) with outcome supervision for planning in mathematical reasoning, proving \"outcome-supervised guided decoding is secretly a value model.\" VF-PRM differs in: (1) Training: TD(λ) bootstrapping vs. MC returns regression, offering better bias-variance tradeoff for long-horizon reasoning; (2) Usage: PBRS potential differences F_t = γV(s_{t+1}) − V(s_t) as step rewards vs. direct V(s_t) for beam search pruning; (3) Scenario: RL training (reward hacking vulnerability) vs. inference-time planning.\n\n**Restoring value functions in LLM RL**: RL^V (arXiv 2025, revised Apr 2026) addresses the same motivation — \"prevalent RL methods abandon the learned value function\" — by jointly training LLM as reasoner and generative verifier, achieving 20%+ boost on MATH with parallel sampling. VF-PRM takes a complementary path: separate value model with formal PBRS guarantees rather than self-verification.\n\n**Learned V as PBRS potential in standard RL**: BSRS (AAAI 2025) proposes using the agent's current V estimate as PBRS potential, providing tabular convergence proofs and Atari validation. VF-PRM extends this idea to LLM reasoning with three key adaptations: (1) outcome-only supervision (no per-step rewards available in LLM reasoning); (2) step boundary handling unique to natural language sequences; (3) theoretical unification of PRM aggregation schemes, which BSRS does not address.\n\n**Survey coverage**: The RARL survey (Feb 2026, arXiv 2026) identifies the central open problem: \"Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent.\" The credit assignment survey (Apr 2026, arXiv 2026) covers 47 methods and does NOT identify trained neural V(s_t) + explicit PBRS step rewards + RL training as an existing method.\n\n## Proposed Approach\n\n**VF-PRM Training**: Train V(s_t) ≈ P(correct | prefix₁:t) on Qwen2.5-Math-7B and Qwen2.5-Math-1.5B using TD(λ) with binary outcome supervision only. Step boundaries defined by \"\\n\\n\" (double newline), consistent with PURE's segmentation for comparability. Training employs: target network (periodic sync for stable TD targets), gradient clipping on value head, and outcome labels as terminal rewards. Unlike PPO's online critic (VinePPO's finding: inaccurate V estimates from noisy rollouts), VF-PRM trains a separate model on ground-truth outcome labels, providing fundamentally more stable learning signal.\n\n**PBRS Step Rewards**: Dense step-level rewards via F_t = γV(s_{t+1}) − V(s_t), provably preserving optimal policy (Ng et al., 1999). When V(s_t) accurately approximates the true value, F_t approximates the advantage A(s_t, a_t), providing maximally informative dense gradients.\n\n**Theoretical Results**: Formal proofs that: (a) sum-form ≡ telescoping potential with unbounded shaping magnitude; (b) min-form ≡ truncated potential with gradient information loss; (c) learned V-based PBRS with approximation error ε introduces bounded policy suboptimality proportional to ε. Testable prediction: VF-PRM's |F_t| distribution should exhibit adaptive magnitude control — converging toward advantage-like distributions as V improves, unlike the fixed magnitude profiles of sum/min.\n\n**RL Integration**: GRPO training with online VF-PRM updates. Update schedule: VF-PRM updated every k GRPO steps (k ∈ {50, 100, 500} as hyperparameter) using on-policy trajectories. Ablation covers frozen / infrequent (k=500) / frequent (k=50) update regimes.\n\n## Evaluation Plan\n\n**Training Data**: RL training uses MATH training set problems as prompt source, consistent with PRIME/PURE setups. All baselines re-implemented under identical conditions (same base model, same SFT checkpoint, same training data, same training steps) for controlled comparison.\n\n**Baselines** (8 methods): (1) Vanilla GRPO (outcome reward only, no PRM); (2) PRIME (ICLR 2026); (3) PURE (NeurIPS 2025, min-form); (4) SHAPE (ACL 2026, MC potentials); (5) TDRM (arXiv 2025); (6) CRM (ICLR 2026); (7) VF-PRM with V(s_t) as direct step score (no PBRS difference — isolating PBRS contribution); (8) OVM-style MC-returns V(s_t) + PBRS (isolating TD(λ) vs. MC training method).\n\n**Benchmarks**: GSM8K (easy/sanity check), MATH500 (medium), AMC 2023 (medium-hard), AIME 2024 (hard), ProcessBench (reward quality). Five benchmarks covering full difficulty gradient.\n\n**Model Scales**: Qwen2.5-Math-7B (primary) and Qwen2.5-Math-1.5B (generalization).\n\n**Evaluation Scenarios**: (1) RL training — GRPO with each reward method, report final accuracy; (2) Best-of-N inference (N=8, 16, 64) — V(s_T) as solution-level reranker; (3) Tree-search / beam search (beam width=4, 8, 16) — V(s_t) as step-level node evaluator, directly comparable to OVM and TDRM.\n\n**Ablations**: (a) γ ∈ {0.9, 0.95, 0.99, 1.0}; (b) λ ∈ {0, 0.5, 0.8, 1.0}; (c) Neural V vs. MC potential estimation; (d) Frozen / infrequent / frequent VF-PRM updates; (e) PBRS isolation: direct V(s_t) score vs. F_t = γV(s_{t+1}) − V(s_t); (f) Step granularity: \"\\n\\n\" vs. sentence-level vs. token-level segmentation.\n\n**Theory Verification**: (a) Shaping magnitude |F_t| distribution under sum/min/product/PBRS during training — verify unbounded magnitude for sum-form, truncated for min-form, adaptive for PBRS; (b) Training dynamics: reward, validation accuracy, KL divergence from reference policy over training steps; (c) V estimation quality tracking: correlation between V(s_t) predictions and MC-estimated ground truth over training.\n\n**Compute-Normalized Comparison**: Total compute budget table per method (PRM training + RL training + inference-time rollouts). Include compute-matched comparison showing accuracy at equivalent total compute.\n\n## Key References\n\n- Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping — Ng et al. (ICML 1999)\n- Process Reinforcement through Implicit Rewards — PRIME (ICLR 2026)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025)\n- Smooth Reward Models with Temporal Difference for LLM RL and Inference — TDRM (arXiv 2025)\n- Linking Process to Outcome: Conditional Reward Modeling — CRM (ICLR 2026)\n- DuaShepherd: Integrating Stepwise Correctness and Potential Rewards (arXiv 2025)\n- Pretrain Value, Not Reward: Decoupled Value Policy Optimization — DVPO (ICLR 2026)\n- SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning (ACL 2026)\n- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning — PAV (ICLR 2025)\n- Step Potential Advantage Estimation — SPAE (arXiv 2026)\n- Reward Modeling for Reinforcement Learning-Based LLM Reasoning — RARL survey (arXiv 2026)\n- From Reasoning to Agentic: Credit Assignment in RL for LLMs (arXiv 2026)\n- Outcome-supervised Value Models for Planning in Mathematical Reasoning — OVM (NAACL 2024)\n- Bootstrapped Reward Shaping — BSRS (AAAI 2025)\n- VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment (NeurIPS 2024)\n- Putting the Value Back in RL: Better Test-Time Scaling by Unifying LLM Reasoners With Verifiers — RL^V (arXiv 2025)\n\n## Resource Estimate\n\n- **manual**: ~3,600 H100-hours (VF-PRM training ×2 scales ~350h, OVM baseline training ~150h, GRPO RL ×9 baselines/ablations ×2 scales ~2,400h, inference eval (BoN+tree-search) ~300h, theory verification ~400h), timeline: 14-18 weeks, estimated_gpu_cost: $8,000-10,000\n- **human_in_loop**: ~3,000 H100-hours, timeline: 10-13 weeks, claude_api_cost: $400-600, estimated_gpu_cost: $6,500-8,500\n- **auto_research**: ~3,800 H100-hours, timeline: 7-10 weeks, claude_api_cost: $800-1,500, estimated_gpu_cost: $8,500-11,000, speed_bottleneck: RL training wallclock ~36h per GRPO run on 8×H100"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T09:31:16.980Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T09:31:16.980Z",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T09:31:16.995Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- SHAPE (arXiv 2604.06636, ACL 2026): 最直接的竞争者。已经在 LLM 推理中显式实现了 PBRS，使用 MC 估计的势函数修改 GRPO 的优势函数，报告了 +3% 准确率和 30% token 压缩。与本 proposal 的核心区别仅在于 MC 势 vs. 学习的神经势函数。
- PAV — "Rewarding Progress" (ICLR 2025 Spotlight, arXiv 2410.08146): 将 step reward 定义为"进展"——执行一步前后 MC 成功概率的变化——概念上与 PBRS 势差高度相似。已实现 6× sample efficiency 和 7%+ 准确率提升。被接为 Spotlight，说明社区对这种思路认可度高。
- PURE (NeurIPS 2025, arXiv 2504.15275): Min-form credit assignment 解决了 sum-form 导致的 reward hacking，纯实证方案无理论框架。本 proposal 提出用 PBRS 理论统一解释 sum/min/product 聚合的行为差异，这是对 PURE 观察的理论补全。
- BSRS — Bootstrapped Reward Shaping (AAAI 2025, arXiv 2501.00989): 在标准 RL 中已提出用 agent 当前 V 估计作为 PBRS 势函数，提供了 tabular 收敛证明和 Atari 验证。这是本 proposal"学习 V + PBRS"核心思路的直接前身，只是在标准 RL 而非 LLM 场景。
- CRM — Conditional Reward Modeling (ICLR 2026): 将 step reward 建模为条件概率 P(correct|s_{1:t})，捕捉步骤间因果关系。覆盖 BoN、beam search、RL 三场景，但无 PBRS 保证。
- PRIME (ICLR 2026, arXiv 2502.01456): 从 ORM token 概率中提取隐式过程奖励，自身已被社区认为"可视为 PBRS where q-value is the potential"。在无需显式 PRM 训练的情况下实现了有竞争力的 RL 训练结果。
- TDRM (arXiv 2509.15110, Sep 2025): 已将 TD learning 应用于 PRM 平滑，实现 20× 数据效率，但需要 step-level annotations。本 proposal 使用 TD(λ) + outcome-only supervision，是关键区别。
- OVM (NAACL 2024, arXiv 2311.09724): 用 outcome supervision 训练 V(s_t) 用于推理规划（beam search），是本 proposal 在 V(s_t) 训练思路上最直接的知识前驱。区别在训练方法（TD(λ) vs. MC returns）和用途（PBRS step rewards vs. beam search pruning）。
- VinePPO (NeurIPS 2024, arXiv 2410.01679): 证明 PPO 中的 value network 在 LLM 推理任务中"几乎不比随机基线好"，这是本 proposal 试图解决的核心动机之一。但 VinePPO 的解法是绕开 V（用 MC 估计），而非修复 V。
- RL^V (arXiv 2505.04842, 2025): 联合训练 LLM 作为推理器和验证器，恢复 value function。与本 proposal 动机相同（"把 V 带回来"），但路径不同（self-verification vs. separate model + PBRS）。
- SPAE (arXiv 2601.03823, Jan 2026): Training-free PBRS-inspired 势差方法，使用探测机制提取 confidence 和 correctness 信号。无需训练的轻量方案。
- DuaShepherd (arXiv 2506.17533, June 2025): 双头架构分离 correctness 和 potential reward。验证了二者确实捕捉不同信号。但仅评估推理阶段（BoN），未涉及 RL 训练。
- RARL Survey (arXiv 2602.09305, Feb 2026): 明确指出"不同聚合方案产生截然不同的策略行为，但原则性设计指南仍然缺失"——本 proposal 试图填补的空白。

- 调研总结: PRM 的 step-level credit assignment 是 2025-2026 年 LLM RL 领域最热门的子方向之一，已有多篇顶会论文从不同角度切入（PURE 做聚合实证、PAV 做进展度量、SHAPE 做 MC-PBRS、PRIME 做隐式奖励、CRM 做条件概率建模）。这个领域极度拥挤。本 proposal 的独特定位是"学习神经 V + 显式 PBRS + 理论统一框架"，各单独组件均有前驱（BSRS 做学习 V-PBRS、OVM 做 outcome-supervised V、TDRM 做 TD 训练），核心 novelty 在于 (1) 将聚合方案统一为 PBRS 特例的理论框架，(2) 在 LLM reasoning 场景中将 BSRS 思路与 outcome-only supervision 结合。


【Trivial Alternative 检验】:
存在多个成本更低的替代方案构成直接威胁：
1. **SHAPE 的 MC-PBRS**: 无需训练额外模型，直接用 MC rollouts 估计势函数，已实现 +3% 准确率。如果 VF-PRM 的学习 V 相比 MC 估计没有显著优势（特别是在短-中长度推理问题上 MC 方差可控时），VF-PRM 的额外训练成本难以证成。
2. **PRIME 的隐式 PBRS**: 无需显式 PRM 训练，从 ORM token 概率直接提取 step reward，已被社区认为"可视为 PBRS"，且在 ICLR 2026 被接收。
3. **PAV 的进展度量**: 概念上等价于 PBRS 势差，ICLR 2025 Spotlight，已证明 6× sample efficiency。

VF-PRM 的增量价值在于：(a) 推理成本 O(1) vs. MC 的 O(K·T)，在超长推理链上有计算优势；(b) 在线可更新避免分布偏移（PAV 固定于初始 prover policy）；(c) 理论统一框架提供解释力。但这些增量是否足够"surprising"是关键问题。


【前提假设检验】:
核心逻辑链中有两个未经充分验证的环节：

1. **"TD(λ) + outcome-only supervision 能训练出足够准确的 V(s_t)"**: 这是整个方法成立的前提。VinePPO 已经证明在线训练的 value network 在 LLM 推理中极不可靠。Proposal 认为这是因为在线 critic 依赖"noisy policy rollouts"，而 VF-PRM 用 ground-truth outcome labels 训练单独模型所以更稳定。但这个论证并不充分——VinePPO 的发现暗示 V(s_t) 在 LLM 推理的高维序列空间中本身就难以学习，不仅仅是噪声问题。TD(λ) 的 bootstrapping 是否引入了更多偏差（尤其在 V 估计初期不准确时）也未验证。

2. **"PBRS 的 policy invariance 保证在 approximate setting 中有实际意义"**: Ng et al. 1999 的理论保证基于表格/精确设定。在深度神经网络函数逼近 + 有限训练步数 + 非平稳策略分布的实际 LLM RL 中，policy invariance 仅是渐近性质，可能不产生实际优势。BSRS 在 Atari 中验证了这一点的可行性，但 LLM 的动作空间（token vocabulary）和状态空间（自然语言序列）与 Atari 有本质区别。


【3 维度打分】:
  1. Novelty: 中 — 核心方法是对已有组件的组合：学习 V 作 PBRS 势函数 (BSRS, AAAI 2025)、outcome-supervised V 训练 (OVM, NAACL 2024)、TD 学习用于 PRM (TDRM, 2025)、PBRS 应用于 LLM 推理 (SHAPE, ACL 2026; PAV, ICLR 2025)。各单独组件均有近期前驱。真正新颖的是将 PRM 聚合方案（sum/min/product）统一为 PBRS 特例的理论框架——这是一个有价值的理论贡献，但其本质是为已知实证现象（PURE 的 min > sum）提供事后解释，而非预测性新发现。在如此拥挤的赛道上，"better motivated combination of known ingredients" 的 novelty delta 有限。

  2. Significance: 中 — 问题本身无疑重要：step-level credit assignment 是 LLM RL 的核心瓶颈，RARL survey 明确指出"principled design guidelines remain absent"。理论统一框架如果成立，对社区有长期参考价值。但实际影响取决于 VF-PRM 能否在实验中显著超越 SHAPE/PAV/PRIME 等已有方案。如果差距不大，这将沦为一个"理论上更优雅但实践上并不更好"的工作——这类论文在顶会中接收率较低。此外，该方法受限于需要额外训练一个 value model 的计算开销，在"推理 scaling"成为主流趋势的当下，computation overhead 是实际部署的障碍。

  3. Related Work: 强 — 覆盖极为全面，识别了 15+ 篇高度相关论文，对每一篇的定位和差异化都有具体说明。特别是对 SHAPE (MC-PBRS)、PAV (progress-as-potential)、BSRS (learned V-PBRS)、OVM (outcome-supervised V) 的差异化论证是清晰且诚实的。Survey 级别的文献覆盖是明确的优势。唯一的小隐患是部分引用的会议年份/状态可能尚未最终确认（如 ACL 2026 SHAPE），但对 proposal 阶段而言可以接受。


【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Related Work 覆盖是强项，但不直接决定接收率。Novelty 是核心瓶颈：这个 idea 的本质是"将 BSRS (AAAI 2025) 的思路迁移到 LLM reasoning 场景 + 加上聚合方案的 PBRS 理论统一"——这是一个 well-motivated combination，但在 SHAPE (ACL 2026) 已经做了 PBRS + LLM reasoning、BSRS (AAAI 2025) 已经做了 learned V + PBRS 的背景下，组合的增量 novelty 有限。理论统一贡献（sum/min/product → PBRS 特例）是真实的 delta，但属于"解释已知现象"而非"预测新现象"，审稿人可能评价为 "nice but incremental"。Significance 受制于实践优势的不确定性——如果实验结果仅与 SHAPE/PRIME/PAV 持平或微幅领先，论文将很难获得足够的审稿人热情。上界被 Novelty 限制：即使实验完美执行，核心 insight ("用学习的 V 做 PBRS 比 MC 做 PBRS 更好") 是审稿人"would have guessed this"的范畴，不是反直觉发现。

【主要风险】: 
1. **"Better engineering of known ideas" 定性风险**: 审稿人可能认为 VF-PRM = BSRS + OVM + TDRM 的组合应用于 LLM 场景，各组件均已发表，组合的 intellectual contribution 不够一篇独立论文。
2. **Trivial alternative 竞争力风险**: 如果 SHAPE 的 training-free MC-PBRS 在实验中表现与 VF-PRM 差距不大（尤其在中等长度推理链上），审稿人会质疑为什么需要额外训练一个 value model——Occam's razor 将倾向于更简单的方案。
```

Sources:
- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation](https://arxiv.org/abs/2604.06636)
- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146)
- [PURE: Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)
- [BSRS: Bootstrapped Reward Shaping (AAAI 2025)](https://arxiv.org/abs/2501.00989)
- [CRM: Linking Process to Outcome: Conditional Reward Modeling](https://openreview.net/forum?id=4DJoBOQNd0)
- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)
- [TDRM: Smooth Reward Models with Temporal Difference](https://arxiv.org/abs/2509.15110)
- [OVM: Outcome-supervised Value Models for Planning](https://arxiv.org/abs/2311.09724)
- [VinePPO: Refining Credit Assignment in RL Training of LLMs](https://arxiv.org/abs/2410.01679)
- [RL^V: Putting the Value Back in RL](https://arxiv.org/abs/2505.04842)
- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)
- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/html/2602.09305v1)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- SHAPE (arXiv 2604.06636, ACL 2026): 最直接的竞争者。显式引用 Ng et al. (1999) PBRS，使用 MC rollout 估计 potential，修改 GRPO advantage，实现 +3% accuracy / -30% tokens。关键区别：training-free MC potentials vs. VF-PRM 的 learned neural V。但 SHAPE 已经证明 PBRS 在 LLM reasoning RL 中可行。
- PAV (ICLR 2025 Spotlight, arXiv 2410.08146): 定义 step reward = progress (MC success probability 的变化量)，本质上就是 PBRS potential difference 的无折扣版本。RL 场景下实现 6× sample efficiency、7%+ accuracy gain。与 VF-PRM 的核心 idea 高度重叠，差异主要在 MC vs. learned V 和是否有 formal PBRS formulation。
- PURE (NeurIPS 2025, arXiv 2504.15275): 证明 min-form 比 sum-form 更抗 reward hacking，但只提供经验观察，无理论框架。VF-PRM 的 PBRS 统一分析解释了 PURE 的现象。
- BSRS (AAAI 2025, arXiv 2501.00989): 在标准 RL (tabular + Atari) 中使用 agent 当前 V 估计作为 PBRS potential，提供收敛证明。VF-PRM 本质上是 BSRS idea 在 LLM reasoning 场景的迁移。
- OVM (NAACL 2024, arXiv 2311.09724): 用 outcome supervision 训练 V(s_t)，用于 inference-time planning（beam search）。VF-PRM 把 OVM 的 V 从 inference-time 扩展到 RL training，并改用 TD(λ) 替代 MC returns。
- PRIME (ICLR 2026, arXiv 2502.01456): 从 ORM token probabilities 提取隐式 process reward，自称 "viewable as PBRS where q-value is the potential"。已在 ICLR 2026 接收。
- CRM (ICLR 2026, OpenReview): 将 step reward 建模为条件概率 P(correct|s_{1:t})，ICLR 2026 接收。无 PBRS 保证。
- TDRM (arXiv 2509.15110): 使用 TD learning 来平滑 PRM labels，但需要 step-level annotations。VF-PRM 仅需 outcome-only supervision。
- DuaShepherd (arXiv 2506.17533, June 2025): 双头架构分离 correctness 和 potential，SOTA on MATH500/ProcessBench，但仅评估 inference-time (BoN)。VF-PRM 的 training-usage misalignment 论点部分受其启发。
- VinePPO (NeurIPS 2024, arXiv 2410.01679): 证明 PPO 的 value network 在 LLM reasoning 中 "consistently provide inaccurate estimates"，MC rollout 作为替代。这既是 VF-PRM 的动机来源，也是最大的风险来源——VF-PRM 声称单独训练的 V 比 PPO critic 更准确，但尚未验证。
- RL^V (arXiv 2505.04842, revised Apr 2026): 联合训练 LLM 为 reasoner + verifier，20%+ MATH boost。互补方向（自验证 vs. 独立 V model）。
- RARL Survey (arXiv 2602.09305, Feb 2026): 明确指出 "Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent"——VF-PRM 正好填补此空缺。

- 调研总结: PRM + RL 的 credit assignment 是 2025-2026 最活跃的 LLM reasoning 子领域之一。PBRS 已被 SHAPE 和 PRIME 显式/隐式引入，PAV 的 progress-based reward 与 PBRS potential difference 高度相似。VF-PRM 的独特定位是 "learned neural V + TD(λ) + explicit PBRS + RL training + 理论统一"，但每个组件都已在其他工作中出现，核心贡献是将它们 cohesively 组合并提供 PBRS-based 理论分析。

【Trivial Alternative 检验】:
存在两个直接的 trivial alternative 威胁：
1. **SHAPE 的 MC-PBRS**：SHAPE 已经在 LLM reasoning RL 中使用了 PBRS + MC-estimated potentials。VF-PRM 的增量是用 learned V 替代 MC rollouts，声称低方差 + 可更新。但如果 SHAPE 的 MC potentials 在实践中已经足够好（+3% accuracy, -30% tokens），那 learned V 的额外收益可能有限。VF-PRM 的增量价值需要证明 learned V 在 long-horizon / 复杂问题上显著优于 MC potentials——这是合理的论点（MC 的 O(K·T) cost），但尚未验证。
2. **PAV 的 progress reward**：PAV 使用 MC 估计的 progress (Δ success probability) 作为 step reward，概念上与 PBRS potential difference 几乎等价。PAV 已经在 RL 训练中取得了 6× sample efficiency。VF-PRM 相对于 PAV 的增量是 formal PBRS guarantee + 可在线更新的 learned V——这些是真实的差异，但审稿人可能会质疑实际 gap 有多大。

增量价值所在：(a) 理论统一 framework 解释了为什么 sum-form hacks、min-form loses information，这是 SHAPE/PAV 都没有提供的；(b) amortized cost 在 long-horizon 问题上有实际优势。但这些增量是否足以支撑一篇完整论文，取决于实验中 learned V vs. MC 的实际 gap。

【前提假设检验】:
核心逻辑链有以下未经验证的关键假设：
1. **"独立训练的 V(s_t) 比 PPO online critic 更准确"**——这是整个 proposal 的核心前提。VinePPO 证明 PPO 的 value network 不可靠，VF-PRM 声称独立训练 + ground-truth outcome labels 可以解决。但"独立训练"是否真的解决了根本问题（LLM reasoning 的状态空间巨大、V function 本身难以拟合）尚不清楚。如果 learned V 同样不准确，F_t = γV(s_{t+1}) − V(s_t) 会引入大量噪声，可能不如 MC estimates。
2. **"TD(λ) 优于 MC returns for V training"**——proposal 声称 TD(λ) 提供更好的 bias-variance tradeoff，但在 LLM reasoning 的长序列环境中，TD bootstrapping 的 bias 可能很大（因为 V 本身不准确时 bootstrap target 也不准确），λ=1 退化为 MC returns。这个 tradeoff 在 LLM reasoning 特定场景下的表现是未知的。
3. **"Online VF-PRM updates 可以防止 staleness 而不 destabilize training"**——在 RL 训练中同时更新 reward model 和 policy 是已知的不稳定因素（moving target problem）。Proposal 提到了 update frequency ablation，但是否能稳定训练是实验层面的未知。
4. **"V(s_t) 准确时 F_t ≈ A(s_t, a_t)"**——这个数学关系在理想条件下成立，但在 LLM 的 token-level / step-level 混合 MDP 中，step boundary 的定义（"\n\n"）是 heuristic 的，F_t 是否真的近似 advantage 取决于 step 粒度是否匹配 decision granularity。

其中假设 1 是最关键的——如果 learned V 不比 MC 好，整个 proposal 的 raison d'être 就不存在了。

【3 维度打分】:

1. Novelty: 【中】
   理由：VF-PRM 的每个组件都已在现有工作中出现：outcome-supervised V(s_t) (OVM, NAACL 2024)、V 作为 PBRS potential (BSRS, AAAI 2025)、PBRS 用于 LLM reasoning (SHAPE, ACL 2026; PRIME, ICLR 2026)、progress-based step reward ≈ potential difference (PAV, ICLR 2025)。VF-PRM 的贡献是将这些组件 cohesively 组合，并提供 PBRS-based 的 PRM 聚合统一理论。这个理论统一是真实且有价值的——PURE 的 min > sum 现象得到了 PBRS 框架下的解释——但它更像是"用已知理论解释已观察到的经验现象"，而不是提出新的理论。相较于 SHAPE 和 PAV，VF-PRM 的 novelty delta 主要在 learned V vs. MC 和理论分析，属于 incremental improvement 而非 paradigm shift。审稿人可能会说 "this is a natural combination of existing ideas"。

2. Significance: 【中偏强】
   理由：研究问题本身非常重要——PRM 的 training-usage misalignment 和 credit assignment 是 2025-2026 LLM reasoning 的核心开放问题（RARL survey 明确指出）。如果 VF-PRM 显著优于 SHAPE/PAV/PURE，这对该领域的实践有直接影响。理论统一 framework 对理解现有方法有启发价值。但影响力受限于：(a) 这是一个已经非常拥挤的子领域，SHAPE/PAV/PURE/PRIME/CRM 已经提供了多种可用方案；(b) 实际增量可能有限——如果 learned V 只比 MC 好 1-2%，实践影响不大。

3. Related Work: 【强】
   理由：Related work 覆盖极为全面——涵盖了 PURE、SHAPE、PAV、PRIME、CRM、TDRM、DuaShepherd、OVM、BSRS、VinePPO、RL^V、DVPO、SPAE 等几乎所有相关工作，且每篇都有清晰的差异化定位。Proposal 还引用了两篇最新 survey (RARL, credit assignment)，并利用 survey 的 gap identification 来 justify 自身贡献。这种级别的 related work 覆盖和 positioning 在审稿中是加分项。唯一可能的遗漏是一些与 token-level credit assignment 相关的最新工作（如 Q#），但总体覆盖已经远超平均水平。

【概率估计】: [25% - 38%] 中位 30%

【估计理由】:
- Related Work（强）确保了 proposal 不会因定位不清或遗漏关键工作而被拒，这是稳定的加分项
- Significance（中偏强）意味着审稿人会认可问题的重要性
- Novelty（中）是主要限制因素：每个组件都有 prior art（OVM, BSRS, SHAPE, PAV），组合虽然 coherent 但审稿人可能认为是 "engineering contribution"。SHAPE（ACL 2026）已经显式使用 PBRS，PAV（ICLR 2025 Spotlight）已经使用 progress-based step rewards 用于 RL training。VF-PRM 的增量（learned V vs. MC + 理论统一）是真实的但可能不够 surprising。
- 理论贡献（统一分析）在审稿中是 double-edged：如果审稿人认为这些 proofs 是 PBRS 的直接应用（straightforward），那理论贡献的 perceived novelty 会降低
- 上界（38%）对应"learned V 在实验中显著优于 MC，理论分析被认为有启发价值"的情景
- 下界（25%）对应"审稿人认为这是 BSRS + OVM 在 LLM 场景的直接迁移，novelty insufficient"的情景

【主要风险】:
1. **"Combination, not contribution" 风险**：最可能的拒稿理由。审稿人可能认为 VF-PRM 是 OVM 的 V(s_t) + BSRS 的 V-as-potential + SHAPE 的 PBRS-in-LLM 的直接组合，每个组件都不新颖，组合也不够 surprising。尤其是 SHAPE 已经在 ACL 2026 接收了 PBRS + LLM reasoning 这个 idea。
2. **核心前提可能不成立**：如果 learned V(s_t) 并不比 VinePPO/SHAPE 的 MC estimates 显著更准确（LLM reasoning 的高维状态空间可能使神经网络 V 的拟合同样困难），那 VF-PRM 相对于 SHAPE/PAV 的实际优势将非常有限，proposal 的核心 selling point 将被大幅削弱。
```

Sources:
- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/abs/2604.06636)
- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146)
- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275)
- [BSRS: Bootstrapped Reward Shaping](https://arxiv.org/abs/2501.00989)
- [OVM: Outcome-supervised Value Models for Planning in Mathematical Reasoning](https://arxiv.org/abs/2311.09724)
- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)
- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://openreview.net/forum?id=4DJoBOQNd0)
- [TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference](https://arxiv.org/abs/2509.15110)
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards for Mathematical Reasoning](https://arxiv.org/abs/2506.17533)
- [VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment](https://arxiv.org/abs/2410.01679)
- [RL^V: Putting the Value Back in RL](https://arxiv.org/abs/2505.04842)
- [DVPO: Pretrain Value, Not Reward: Decoupled Value Policy Optimization](https://arxiv.org/abs/2502.16944)
- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)
- [RARL Survey: Reward Modeling for RL-Based LLM Reasoning](https://arxiv.org/abs/2602.09305)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have comprehensive information about the research landscape. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. **SHAPE (arXiv 2604.06636, ACL 2026)**: 直接竞争者。已将 PBRS 引入 LLM 推理，使用 MC rollout 估算 potential，修改 GRPO advantage，实现 +3% 准确率和 30% token 节省。与 VF-PRM 的关键区别在于 SHAPE 使用 training-free MC 估算而非 learned neural V。但 SHAPE 已经证明 PBRS 在 LLM 推理中的有效性。

2. **PAV / Rewarding Progress (arXiv 2410.08146, ICLR 2025 Spotlight)**: 概念上最接近的工作。将 step reward 定义为 progress（MC 成功概率的变化），本质上就是 PBRS 的 potential difference。实现了 6× sample efficiency 和 7%+ accuracy gain。与 VF-PRM 的区别：PAV 使用 per-step MC rollouts（O(K·T) 成本），VF-PRM 用 amortized neural V。

3. **PURE (arXiv 2504.15275, NeurIPS 2025)**: 发现 min-form credit assignment 避免 reward hacking，sum-form 会 collapse。纯经验发现，缺乏理论解释。VF-PRM 的理论贡献之一就是用 PBRS 框架解释 PURE 的经验发现。

4. **BSRS (arXiv 2501.00989, AAAI 2025)**: 直接使用 agent 当前 V 估计作为 PBRS potential。提供了 tabular 收敛证明和 Atari 验证。VF-PRM 本质上是 BSRS 思想在 LLM reasoning 场景的延伸。

5. **OVM (NAACL 2024 Findings)**: 最直接的智识前驱。用 outcome supervision 训练 V(s_t)，用于 beam search pruning。VF-PRM 与 OVM 的区别：(1) TD(λ) vs MC returns 训练；(2) PBRS difference 作为 step reward vs 直接用 V(s_t) 做 beam search。

6. **PRIME (arXiv 2502.01456, ICLR 2026)**: 从 ORM token 概率提取 implicit process rewards，作者自己承认"可视为 PBRS where q-value is the potential"。但使用启发式提取而非显式 value function 训练。

7. **CRM (ICLR 2026)**: 将 step reward 建模为条件概率 P(correct|s_{1:t})。缺乏 PBRS policy invariance 保证。

8. **TDRM (arXiv 2509.15110)**: 用 TD 学习平滑 PRM labels，但需要 step-level annotations。VF-PRM 使用 TD(λ) 但仅需 outcome supervision。

9. **RL^V (arXiv 2505.04842)**: 解决相同动机——"主流 RL 方法抛弃了 learned value function"。联合训练 LLM 作为 reasoner 和 generative verifier。与 VF-PRM 互补：RL^V 走自验证路线，VF-PRM 走 separate value model + formal PBRS 路线。

10. **VinePPO (NeurIPS 2024)**: 证明 PPO 中的 value networks "consistently provide inaccurate estimates"，改用 MC-based estimates。VF-PRM 需要回应这个发现——为什么 VF-PRM 的 V 不会遇到同样的问题。

11. **SPAE (arXiv 2601.03823)**: Training-free PBRS-inspired potential differences，使用 composite heuristic metric。

12. **DuaShepherd (arXiv 2506.17533)**: 分离 correctness 和 potential reward heads，实证证明二者 orthogonal。

- **调研总结**: Process reward + PBRS 在 LLM reasoning 中是 2025-2026 极其拥挤的赛道。SHAPE 已经将 PBRS 显式引入 LLM reasoning（MC-based），PAV 已经在用 potential difference 做 step reward（MC-based），BSRS 已经在用 learned V 做 PBRS potential（Atari）。VF-PRM 的定位是这些方向的交汇点——"learned neural V + explicit PBRS + LLM RL training"——这个精确组合确实尚未被实现，但每个组件都已存在于不同工作中。真正的增量 novelty 在于 **理论统一**（用 PBRS 解释 aggregation schemes 的成败）而非方法本身。

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁**:

1. **SHAPE + 蒸馏**: 最直接的替代——先用 SHAPE 的 MC rollouts 生成 potential estimates，然后训练一个 neural network 拟合这些 MC estimates（知识蒸馏）。这比 TD(λ) 方法更简单，且能继承 MC 的无偏性。VF-PRM 需要论证 TD(λ) 训练 V(s_t) 优于这种蒸馏方案，否则增量价值不清晰。

2. **OVM + PBRS difference**: OVM 已经训练了 V(s_t)（用 MC returns），直接在 OVM 的 V(s_t) 上计算 F_t = γV(s_{t+1}) − V(s_t) 就行。VF-PRM 的 TD(λ) 训练相比 OVM 的 MC 训练的优势是什么？Proposal 声称 TD(λ) 提供更好的 bias-variance tradeoff，但这需要实证验证。

3. **PRIME 本身**: PRIME 已经通过 implicit PRM 实现了高效的 process rewards，其隐式 PBRS 结构已被作者承认。VF-PRM 的 explicit PBRS 是否比 PRIME 的 implicit PBRS 更优？

**增量价值主要在理论层面**: VF-PRM 的真正增量在于（a）理论统一 aggregation schemes，（b）提供 formal PBRS 保证。实践层面的增量（learned V vs MC potentials）需要实验证明。

【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的假设：

1. **"TD(λ) + outcome-only supervision 能训练出足够准确的 V(s_t)"** — 这是整个方法的基石，但 VinePPO 已经证明 PPO 中的 value networks "consistently provide inaccurate estimates"。VF-PRM 声称因为使用 ground-truth outcome labels 和 separate model 所以不同，但这是**未经验证的假设**。如果 V(s_t) 不够准确，PBRS 的 F_t 就是噪声而非有效信号，整个方法就会失败。这是最关键的前提假设。

2. **"F_t 近似 advantage function 时提供 maximally informative dense gradients"** — 理论上正确，但前提是 V(s_t) 足够准确。在 LLM reasoning 中，state space 极其高维（每个 token sequence 是一个 state），V(s_t) 的泛化能力存疑。特别是 reasoning chain 的中间状态可能非常 diverse，7B 模型的 V head 是否能准确估计这些状态的 value？

3. **"Online updates every k GRPO steps 能防止 distribution shift 导致的 staleness"** — 这是一个合理但未经验证的设计选择。如果 policy 变化快于 V 的更新频率，PBRS 的 policy invariance 保证就会被打破（因为 V 不再对应当前 policy 的 value function）。

4. **"PBRS 的 policy invariance 在 function approximation setting 下仍然成立"** — Ng et al. (1999) 的理论保证是在 tabular MDP 下证明的。在 deep RL / LLM 的 function approximation setting 下，PBRS 的 policy invariance 不严格成立。BSRS 在 deep RL 中也只是提供了 tabular 收敛证明。

【3 维度打分】:

1. **Novelty: 中** — 
   - **加分**: 理论统一贡献（用 PBRS 框架解释 sum-form/min-form 的成败）是真正的新颖点，目前没有看到任何现有工作做这个理论分析。RARL survey 和 credit assignment survey 都确认这是 open problem。testable prediction（|F_t| 分布随 V 改善而收敛）也是新的。
   - **减分**: 方法层面，VF-PRM 是 BSRS（AAAI 2025, learned V as PBRS potential）+ OVM（NAACL 2024, outcome-supervised V training）+ TDRM（TD learning for PRM）的自然组合。SHAPE（ACL 2026）和 PAV（ICLR 2025）已经在 LLM reasoning 中实现了 PBRS / potential-difference 的 step reward。每个组件已存在，VF-PRM 是交汇点。
   - 总结：理论贡献是 novel 的，方法贡献是 incremental synthesis。整体 novelty 为"中"而非"强"，因为方法的核心 insight（"用 learned V 做 PBRS potential for LLM RL"）在看到 BSRS + OVM + SHAPE 之后是一个 natural next step，审稿人可能会说 "this combination was expected."

2. **Significance: 中偏强** — 
   - **加分**: Credit assignment in LLM RL 是当前最重要的研究问题之一。PRM aggregation 的理论理解确实缺乏（RARL survey 明确指出）。如果理论统一成立，对整个 PRM + RL 社区都有指导意义。问题的重要性和时效性毋庸置疑。
   - **减分**: 实际影响取决于 VF-PRM 是否在实验中显著优于 SHAPE / PAV / PURE 等已有方法。如果实验提升有限，理论统一虽好但 impact 打折。此外，领域移动极快，这些方法可能在论文发表前就被更新的范式（如 scaling test-time compute directly）supersede。

3. **Related Work: 强** — 
   - Proposal 对相关工作的覆盖非常全面且准确。所有我调研到的关键竞争者（SHAPE, PAV, PURE, BSRS, OVM, PRIME, CRM, TDRM, RL^V, VinePPO, DuaShepherd, SPAE）都被提及，且差异化定位清晰。
   - 特别值得肯定的是：(1) 对 PAV 和 SHAPE 的精确区分（MC vs learned, fixed vs online-updateable）；(2) 对 BSRS 的 honest positioning（承认 VF-PRM 是 BSRS 在 LLM reasoning 的延伸）；(3) 对 OVM 的智识传承定位准确；(4) 引用了两个 survey 确认 open problem。
   - 微小不足：可以更显式地讨论 PAV 和 SHAPE 的实验结果，以论证 learned V 相比 MC 的实际优势有多少空间。

【概率估计】: [28% - 38%] 中位 32%

【估计理由】: 
- **Novelty（中）**是主要限制因素。方法是已有组件的 natural synthesis（BSRS + OVM + SHAPE 的交汇），审稿人很可能说 "the combination is straightforward"。理论统一贡献是加分项，但仅靠理论贡献在 AAAI 中稿偏难，除非实验上能展示出显著优势。
- **Significance（中偏强）**提供了上行空间。问题确实重要且时效性强，如果实验结果证明 learned V 相比 MC methods（SHAPE/PAV）有显著优势，概率可以到 38%+。
- **Related Work（强）**确保 proposal 不会因为 positioning 不当被拒，这是一个重要但非决定性的加分。
- 上界限制来自 novelty：在这个极其拥挤的赛道上，synthesis-type 工作需要非常强的实验结果来弥补方法 novelty 的不足。理论贡献虽好，但 PBRS 理论本身不新（1999），应用到 LLM 的 adaptation 虽有技术含量但不足以 carry 全文。
- 下界来自理论统一的真实价值：即使方法增量有限，用 PBRS 解释 sum-form 的 reward hacking 和 min-form 的成功是对该领域的 genuine theoretical contribution，且有 testable predictions。这不会被完全否定。

【主要风险】: 
1. **"Natural combination" 质疑**: 审稿人很可能指出 VF-PRM = BSRS (AAAI'25) + OVM (NAACL'24) adapted to LLM RL，核心方法 novelty 不足。SHAPE (ACL'26) 已经证明 PBRS works for LLM reasoning，PAV (ICLR'25) 已经用 potential difference 做 step reward——VF-PRM 的实质增量仅是"用 learned V 替代 MC rollouts"，这更像是一个 engineering improvement 而非 conceptual advance。
2. **V(s_t) 精度假设的脆弱性**: VinePPO 已经证明 LLM RL 中 value networks 估计不准。VF-PRM 声称 separate model + ground-truth labels 解决了这个问题，但如果实验中 V(s_t) 仍然不够准确（尤其在 distribution shift 时），整个 PBRS 框架就会退化为噪声信号，实验结果可能不如 SHAPE 的 MC-based 方法（无偏但高方差 vs 有偏但低方差的权衡可能不利于 VF-PRM）。
```

---

Sources:
- [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/abs/2604.06636)
- [PAV: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146)
- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275)
- [BSRS: Bootstrapped Reward Shaping](https://arxiv.org/abs/2501.00989)
- [OVM: Outcome-supervised Value Models for Planning in Mathematical Reasoning](https://arxiv.org/abs/2311.09724)
- [PRIME: Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456)
- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://openreview.net/forum?id=4DJoBOQNd0)
- [TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference](https://arxiv.org/abs/2509.15110)
- [RL^V: Putting the Value Back in RL](https://arxiv.org/abs/2505.04842)
- [VinePPO: Refining Credit Assignment in RL Training of LLMs](https://arxiv.org/abs/2410.01679)
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)
- [SPAE: Step Potential Advantage Estimation](https://arxiv.org/abs/2601.03823)
- [PBRS Topic Overview](https://www.emergentmind.com/topics/potential-based-reward-shaping-pbrs)


【原始 proposal（允许参考但不是主要依据）】:
# Potential-Valued Process Rewards for Principled Step-Level Credit Assignment

## Core Problem

Current Process Reward Models (PRMs) suffer from a fundamental training-usage misalignment: they are trained as step-correctness classifiers ("is this step right?") but repurposed as RL reward signals ("how good is this step?"). DuaShepherd (arXiv 2025, June 2025) empirically proves these are orthogonal signals — step correctness and step value (potential) capture different information — yet all existing PRMs train only on correctness. This misalignment forces practitioners to aggregate step-level correctness scores into RL rewards via heuristic schemes (sum, min, product), causing either reward hacking or information loss. No principled framework connects PRM design to RL training quality, despite potential-based reward shaping (PBRS) theory (Ng et al., ICML 1999) guaranteeing policy invariance — a well-known result never practically implemented as a PRM training objective for step-level process rewards in mathematical reasoning.

More broadly, mainstream LLM RL methods (GRPO, Leave-one-out PPO) have abandoned learned value functions in favor of empirically estimated returns (RL^V, arXiv 2025), while VinePPO (NeurIPS 2024) demonstrated that value networks in standard PPO "consistently provide inaccurate estimates and struggle to rank alternative steps correctly." This creates a paradox: value functions are theoretically essential for credit assignment but practically unreliable in LLM RL. VF-PRM addresses this by training V(s_t) as a separate model with stable outcome supervision via TD(λ), rather than as an online critic dependent on noisy policy rollouts.

## Headline Contributions

1. **Theoretical Unification of PRM Aggregation under PBRS**: First framework to subsume PRM aggregation schemes (sum, min, product) under PBRS theory. We prove sum-form reduces to a telescoping potential with unbounded shaping magnitude (explaining PURE's observed reward hacking), min-form corresponds to a truncated potential (explaining gradient information loss), and learned V(s_t)-based PBRS provides adaptive magnitude control — the shaping magnitude self-regulates through value function accuracy, yielding a testable prediction: as V(s_t) improves during online training, |F_t| distributions should converge toward the advantage function's distribution.

2. **Elimination of Training-Usage Misalignment**: VF-PRM directly trains V(s_t) ≈ P(correct | prefix₁:t) as a state value function using TD(λ) with outcome-only supervision, then derives step rewards via the PBRS formula F_t = γV(s_{t+1}) − V(s_t). Unlike correctness-trained PRMs heuristically repurposed as rewards, VF-PRM's training objective is natively aligned with its downstream RL usage. Unlike VinePPO's online critic (trained on noisy policy rollouts), VF-PRM uses ground-truth outcome labels and a separate model architecture, providing more stable V estimates. Online updates during RL training further prevent staleness as policy distribution shifts.

3. **Amortized Neural Potentials with Bias-Variance Characterization**: Unlike SHAPE (ACL 2026) which uses training-free MC rollout potentials (unbiased but high-variance, cost O(K·T) per step for K rollouts over T steps), and unlike PAV (ICLR 2025) which uses MC-estimated progress without formal PBRS guarantees, VF-PRM's learned neural value function provides amortized, low-variance potential estimates via a single forward pass. We characterize this as a bias-variance tradeoff validated through neural vs. MC ablation.

## Research Landscape

**Aggregation problem (empirical only)**: PURE (NeurIPS 2025) showed min-form credit assignment avoids reward hacking that collapses sum-form training, achieving 82.6% on MATH500, but provides only empirical justification with no theoretical framework. VF-PRM provides the missing PBRS-based explanation and a principled alternative.

**TD learning for PRMs (requires step annotations)**: TDRM (Sep 2025) applies TD learning to smooth PRM labels, achieving 23.7% improvement in tree-search and 20× data efficiency, but requires step-level annotations. VF-PRM uses TD(λ) for value function training with outcome-only supervision.

**Conditional probability modeling (no PBRS guarantees)**: CRM (ICLR 2026) models step rewards as conditional probabilities P(correct|s_{1:t}), evaluating on best-of-N, beam search, and RL across six benchmarks, but lacks PBRS policy invariance guarantees.

**Implicit PBRS (heuristic extraction)**: PRIME (ICLR 2026) extracts implicit process rewards from ORM token probabilities and is acknowledged as "viewable as PBRS where q-value is the potential," but uses heuristic extraction rather than explicit value function training.

**Dual-head separation (inference-only)**: DuaShepherd (June 2025) separates correctness and potential reward heads, achieving SOTA on MATH500/ProcessBench, but evaluates only inference-time (best-of-N).

**MC-based PBRS (training-free, no learned V)**: SHAPE (ACL 2026) applies PBRS with Monte Carlo-estimated potentials, explicitly citing Ng et al. (1999), achieving +3% accuracy with 30% fewer tokens — but uses training-free MC rollouts and only modifies GRPO advantages. SPAE (Jan 2026, arXiv 2026) uses training-free PBRS-inspired potential differences with a heuristic composite metric. PAV (ICLR 2025 Spotlight) defines step reward as progress (change in MC success probability), achieving 6× sample efficiency and 7%+ accuracy gain in RL — conceptually closest to PBRS potential differences but with three critical distinctions from VF-PRM: (1) PAV uses per-step MC rollouts (O(K·T) cost, non-scalable for long-horizon problems) vs. VF-PRM's amortized single-pass neural V; (2) PAV's estimates are fixed to the initial prover policy vs. VF-PRM's online-updateable V; (3) PAV lacks formal γ-discounted PBRS formulation and policy invariance guarantees.

**Response-level value pretraining**: DVPO (ICLR 2026) pretrains a Global Value Model for general RLHF with 40% less GPU memory, but operates at response-level, not step-level.

**Outcome-supervised value models (inference-only, no PBRS)**: OVM (NAACL 2024) is the closest intellectual predecessor — it trains V(s_t) with outcome supervision for planning in mathematical reasoning, proving "outcome-supervised guided decoding is secretly a value model." VF-PRM differs in: (1) Training: TD(λ) bootstrapping vs. MC returns regression, offering better bias-variance tradeoff for long-horizon reasoning; (2) Usage: PBRS potential differences F_t = γV(s_{t+1}) − V(s_t) as step rewards vs. direct V(s_t) for beam search pruning; (3) Scenario: RL training (reward hacking vulnerability) vs. inference-time planning.

**Restoring value functions in LLM RL**: RL^V (arXiv 2025, revised Apr 2026) addresses the same motivation — "prevalent RL methods abandon the learned value function" — by jointly training LLM as reasoner and generative verifier, achieving 20%+ boost on MATH with parallel sampling. VF-PRM takes a complementary path: separate value model with formal PBRS guarantees rather than self-verification.

**Learned V as PBRS potential in standard RL**: BSRS (AAAI 2025) proposes using the agent's current V estimate as PBRS potential, providing tabular convergence proofs and Atari validation. VF-PRM extends this idea to LLM reasoning with three key adaptations: (1) outcome-only supervision (no per-step rewards available in LLM reasoning); (2) step boundary handling unique to natural language sequences; (3) theoretical unification of PRM aggregation schemes, which BSRS does not address.

**Survey coverage**: The RARL survey (Feb 2026, arXiv 2026) identifies the central open problem: "Different aggregation schemes produce divergent policy behaviors, yet principled design guidelines remain absent." The credit assignment survey (Apr 2026, arXiv 2026) covers 47 methods and does NOT identify trained neural V(s_t) + explicit PBRS step rewards + RL training as an existing method.

## Proposed Approach

**VF-PRM Training**: Train V(s_t) ≈ P(correct | prefix₁:t) on Qwen2.5-Math-7B and Qwen2.5-Math-1.5B using TD(λ) with binary outcome supervision only. Step boundaries defined by "\n\n" (double newline), consistent with PURE's segmentation for comparability. Training employs: target network (periodic sync for stable TD targets), gradient clipping on value head, and outcome labels as terminal rewards. Unlike PPO's online critic (VinePPO's finding: inaccurate V estimates from noisy rollouts), VF-PRM trains a separate model on ground-truth outcome labels, providing fundamentally more stable learning signal.

**PBRS Step Rewards**: Dense step-level rewards via F_t = γV(s_{t+1}) − V(s_t), provably preserving optimal policy (Ng et al., 1999). When V(s_t) accurately approximates the true value, F_t approximates the advantage A(s_t, a_t), providing maximally informative dense gradients.

**Theoretical Results**: Formal proofs that: (a) sum-form ≡ telescoping potential with unbounded shaping magnitude; (b) min-form ≡ truncated potential with gradient information loss; (c) learned V-based PBRS with approximation error ε introduces bounded policy suboptimality proportional to ε. Testable prediction: VF-PRM's |F_t| distribution should exhibit adaptive magnitude control — converging toward advantage-like distributions as V improves, unlike the fixed magnitude profiles of sum/min.

**RL Integration**: GRPO training with online VF-PRM updates. Update schedule: VF-PRM updated every k GRPO steps (k ∈ {50, 100, 500} as hyperparameter) using on-policy trajectories. Ablation covers frozen / infrequent (k=500) / frequent (k=50) update regimes.

## Evaluation Plan

**Training Data**: RL training uses MATH training set problems as prompt source, consistent with PRIME/PURE setups. All baselines re-implemented under identical conditions (same base model, same SFT checkpoint, same training data, same training steps) for controlled comparison.

**Baselines** (8 methods): (1) Vanilla GRPO (outcome reward only, no PRM); (2) PRIME (ICLR 2026); (3) PURE (NeurIPS 2025, min-form); (4) SHAPE (ACL 2026, MC potentials); (5) TDRM (arXiv 2025); (6) CRM (ICLR 2026); (7) VF-PRM with V(s_t) as direct step score (no PBRS difference — isolating PBRS contribution); (8) OVM-style MC-returns V(s_t) + PBRS (isolating TD(λ) vs. MC training method).

**Benchmarks**: GSM8K (easy/sanity check), MATH500 (medium), AMC 2023 (medium-hard), AIME 2024 (hard), ProcessBench (reward quality). Five benchmarks covering full difficulty gradient.

**Model Scales**: Qwen2.5-Math-7B (primary) and Qwen2.5-Math-1.5B (generalization).

**Evaluation Scenarios**: (1) RL training — GRPO with each reward method, report final accuracy; (2) Best-of-N inference (N=8, 16, 64) — V(s_T) as solution-level reranker; (3) Tree-search / beam search (beam width=4, 8, 16) — V(s_t) as step-level node evaluator, directly comparable to OVM and TDRM.

**Ablations**: (a) γ ∈ {0.9, 0.95, 0.99, 1.0}; (b) λ ∈ {0, 0.5, 0.8, 1.0}; (c) Neural V vs. MC potential estimation; (d) Frozen / infrequent / frequent VF-PRM updates; (e) PBRS isolation: direct V(s_t) score vs. F_t = γV(s_{t+1}) − V(s_t); (f) Step granularity: "\n\n" vs. sentence-level vs. token-level segmentation.

**Theory Verification**: (a) Shaping magnitude |F_t| distribution under sum/min/product/PBRS during training — verify unbounded magnitude for sum-form, truncated for min-form, adaptive for PBRS; (b) Training dynamics: reward, validation accuracy, KL divergence from reference policy over training steps; (c) V estimation quality tracking: correlation between V(s_t) predictions and MC-estimated ground truth over training.

**Compute-Normalized Comparison**: Total compute budget table per method (PRM training + RL training + inference-time rollouts). Include compute-matched comparison showing accuracy at equivalent total compute.

## Key References

- Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping — Ng et al. (ICML 1999)
- Process Reinforcement through Implicit Rewards — PRIME (ICLR 2026)
- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025)
- Smooth Reward Models with Temporal Difference for LLM RL and Inference — TDRM (arXiv 2025)
- Linking Process to Outcome: Conditional Reward Modeling — CRM (ICLR 2026)
- DuaShepherd: Integrating Stepwise Correctness and Potential Rewards (arXiv 2025)
- Pretrain Value, Not Reward: Decoupled Value Policy Optimization — DVPO (ICLR 2026)
- SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning (ACL 2026)
- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning — PAV (ICLR 2025)
- Step Potential Advantage Estimation — SPAE (arXiv 2026)
- Reward Modeling for Reinforcement Learning-Based LLM Reasoning — RARL survey (arXiv 2026)
- From Reasoning to Agentic: Credit Assignment in RL for LLMs (arXiv 2026)
- Outcome-supervised Value Models for Planning in Mathematical Reasoning — OVM (NAACL 2024)
- Bootstrapped Reward Shaping — BSRS (AAAI 2025)
- VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment (NeurIPS 2024)
- Putting the Value Back in RL: Better Test-Time Scaling by Unifying LLM Reasoners With Verifiers — RL^V (arXiv 2025)

## Resource Estimate

- **manual**: ~3,600 H100-hours (VF-PRM training ×2 scales ~350h, OVM baseline training ~150h, GRPO RL ×9 baselines/ablations ×2 scales ~2,400h, inference eval (BoN+tree-search) ~300h, theory verification ~400h), timeline: 14-18 weeks, estimated_gpu_cost: $8,000-10,000
- **human_in_loop**: ~3,000 H100-hours, timeline: 10-13 weeks, claude_api_cost: $400-600, estimated_gpu_cost: $6,500-8,500
- **auto_research**: ~3,800 H100-hours, timeline: 7-10 weeks, claude_api_cost: $800-1,500, estimated_gpu_cost: $8,500-11,000, speed_bottleneck: RL training wallclock ~36h per GRPO run on 8×H100

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c90a75f0-9661-4152-b95e-7b207055a5a9",
  "type": "user",
  "uuid": "ecb72327-7937-4ca9-9d24-0052c5adda47",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T09:31:16.993Z_

```json
{
  "parentUuid": "ecb72327-7937-4ca9-9d24-0052c5adda47",
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
  "uuid": "6b0cb30f-891f-45ec-9934-e8c150c2816d",
  "timestamp": "2026-05-27T09:31:16.993Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T09:31:16.993Z_

```json
{
  "parentUuid": "6b0cb30f-891f-45ec-9934-e8c150c2816d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f9c0511a-0c8b-4338-8a14-a5c611205453",
  "timestamp": "2026-05-27T09:31:16.993Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research context. Let me compile my eval…",
  "leafUuid": "f9c0511a-0c8b-4338-8a14-a5c611205453",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate VF-PRM proposal for LLM reasoning",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79"
}
```

---

### Assistant

_source line 8 · 2026-05-27T09:31:53.522Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

**Three reviewers' probability estimates:**
- R1: [22% - 33%] 中位 27%
- R2: [25% - 38%] 中位 30%
- R3: [28% - 38%] 中位 32%

Medians: 27%, 30%, 32%
Mean of medians: 29.7%
Median of medians: 30%
Std of medians: ~2.5%

This is high consistency (std < 3%).


Now I'm looking at where the reviewers align and where they diverge. All three unanimously rate novelty as medium—they see VF-PRM as a straightforward combination of existing techniques (BSRS, OVM, SHAPE/PAV) where the main contribution is the theoretical framework explaining how different aggregation methods work. However, on significance, R2 and R3 lean toward medium-strong while R1 appears more conservative.

The reviewers are unanimous on the strength of the related work section, praising its breadth and clear positioning. They also all flag the same core vulnerability: the risk that this feels like an expected engineering combination rather than a conceptual advance. And they all point to a shared technical concern—the fragility of assuming accurate value function estimates, which prior work like VinePPO has shown to be problematic.

The main experimental hurdle is demonstrating that VF-PRM meaningfully outperforms SHAPE, which already achieves solid gains with just training-free Monte Carlo estimates. R3 adds another threat I hadn't fully considered: SHAPE could be trivially improved by distilling the Monte Carlo estimates into a neural network, which might close the gap without needing the full VF-PRM machinery. Meanwhile, R1 and R3 both note that the policy invariance guarantees from Ng 1999 don't cleanly transfer to function approximation settings, and R1 is slightly more skeptical overall than the other two reviewers.

Looking at the median acceptance probabilities—27%, 30%, and 32%—there's strong agreement across reviewers with less than 3% standard deviation. All three converge on medium novelty and strong related work coverage, though significance assessments vary slightly. Given this consistency, I should anchor to the median range and tighten the interval rather than spread it wide. The three ranges overlap substantially, so I'm looking for their intersection to establish a narrower, more defensible estimate. % - 35%] with median at 29%, applying the conservative principle since all three estimates show high consistency around the 28-33% range.

Now I'm moving on to synthesize the implementation assessment by combining the resource estimates from the proposal with feedback from the three reviews.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9c0511a-0c8b-4338-8a14-a5c611205453",
  "isSidechain": false,
  "requestId": "req_011CbSqiYvhWJVFkL9iFEoNi",
  "type": "assistant",
  "uuid": "1c5e731d-4bc6-44a4-b7f0-578b6585ce99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9FMru7XXrPpy625EZk7A6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19017,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19017,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3187,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 19017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19017
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

_source line 9 · 2026-05-27T09:32:30.757Z_

【阶段】: Meta Judge
【三次中位】: [27%, 30%, 32%]  std=2.5%
【共识维度】: 
- **Novelty = 中**（3/3 一致）：VF-PRM 是 BSRS (AAAI'25) + OVM (NAACL'24) + SHAPE/PAV 思路的自然交汇，每个组件均有近期前驱。理论统一贡献（PBRS 解释 sum/min/product 聚合）是真实 delta，但属于"用已知理论解释已知经验现象"，非预测性新发现。三位审稿人均用"natural combination / incremental synthesis"定性。
- **Related Work = 强**（3/3 一致）：覆盖 15+ 篇高相关工作，差异化定位清晰且诚实（特别是对 BSRS、OVM、SHAPE、PAV 的 positioning），引用两篇 survey 确认 open problem。
- **Significance = 中至中偏强**（2/3 判为中偏强，1/3 判为中）：问题本身极其重要（credit assignment in LLM RL），RARL survey 明确指出 gap。但实际影响取决于实验中能否显著超越 SHAPE/PAV/PRIME。
- **"Natural combination" 拒稿风险**（3/3 一致识别）：最可能的拒稿理由。审稿人极可能说"this is BSRS adapted to LLM reasoning + theoretical analysis of known phenomena"。
- **V(s_t) 精度假设脆弱性**（3/3 一致识别）：VinePPO 已证明 value networks 在 LLM RL 中不可靠。VF-PRM 声称 separate model + ground-truth labels 解决此问题，但这是未经验证的核心前提，若不成立则整个方法 raison d'être 消失。
- **SHAPE 作为首要 trivial alternative**（3/3 一致识别）：training-free MC-PBRS 已实现 +3% accuracy / -30% tokens，VF-PRM 的 learned V 相比 MC 的增量价值需要强实验支撑。
- **PBRS policy invariance 在近似设定下的有效性存疑**（2/3 显式提及）：Ng 1999 为 tabular 证明，function approximation 下仅有渐近意义。

【异常维度】: 
- R3 独有地提出"SHAPE + 蒸馏"作为额外 trivial alternative（先用 MC 生成 potential estimates，再蒸馏到 neural net）——这是一个有效但次要的威胁，不改变整体判断。
- R2 独有提及 Q# 作为可能遗漏的 related work——minor，不影响 Related Work 维度的"强"判定。
- R1 对 Significance 判定略严（纯"中"），R2/R3 给"中偏强"——2/3 共识偏向"中偏强"，但差异不大。

【最终概率】: [25% - 35%] 中位 29%
【一致性】: 高
【综合理由】: 
三位审稿人高度一致（std=2.5%，远低于 3% 阈值），在所有关键维度上共识清晰：Novelty 是主要瓶颈，Related Work 是稳定加分，Significance 居中偏上但受限于实验结果不确定性。据此取中位附近并缩窄区间：

- **中位 29%**（略低于三位中位的算术均值 29.7%，体现"宁缺毋滥"原则）：三位审稿人均认为方法层面是 incremental synthesis，理论层面是事后解释而非预测性发现。在 SHAPE (ACL'26) 已显式实现 PBRS + LLM reasoning、BSRS (AAAI'25) 已实现 learned V + PBRS 的背景下，VF-PRM 的组合增量有限。理论统一贡献有真实价值但不足以单独 carry 一篇顶会。
- **上界 35%**（低于 R2/R3 的 38%，受 R1 更严格的上界 33% 制约）：对应"learned V 在实验中显著优于 MC methods + 理论分析被审稿人高度认可"的乐观情景。但即便如此，novelty 天花板限制了上行空间。
- **下界 25%**（高于 R1 的 22%，因三位一致性高故收窄）：对应"审稿人判定为 BSRS 的直接迁移 + 理论贡献被视为 straightforward PBRS application"的悲观情景。Related Work 的强覆盖提供了下限保护。

【建议】: 边缘（偏不推荐侧）
【实施评估】:
  - 计算资源: ~3,000–3,800 H100-hours（约 $6,500–$11,000 GPU 费用），需 8×H100 节点，单次 GRPO 训练约 36h wall-clock
  - 数据需求: MATH 训练集作为 RL prompt source（公开可得）；outcome labels 为二元正确/错误（无需 step-level annotation，这是相对于 TDRM 的优势）
  - 人工介入: 低——主要在超参调优和实验分析阶段；若采用 human-in-loop 模式可省约 20% 计算
  - 训练需求: 需训练 VF-PRM value model（Qwen2.5-Math-7B/1.5B 两个 scale）+ 9 个 baseline/ablation 的 GRPO RL 训练 × 2 scale，训练量大
  - 新 Benchmark: 不需要——使用现有 GSM8K / MATH500 / AMC 2023 / AIME 2024 / ProcessBench
  - 预估周期: 10–18 周（取决于自动化程度和 GPU 可用性），RL 训练的 wall-clock 是主要瓶颈

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c5e731d-4bc6-44a4-b7f0-578b6585ce99",
  "isSidechain": false,
  "requestId": "req_011CbSqiYvhWJVFkL9iFEoNi",
  "type": "assistant",
  "uuid": "e683832c-531b-47ba-a467-82f3f99e9eac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9FMru7XXrPpy625EZk7A6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19017,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19017,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3187,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 19017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19017
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research context. Let me compile my eval…",
  "leafUuid": "e683832c-531b-47ba-a467-82f3f99e9eac",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate VF-PRM proposal for LLM reasoning",
  "sessionId": "3ef25cbe-392f-4452-b762-81b977742f79"
}
```

---
