# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/109a48db-eb76-493e-b397-860b884c6c7a.jsonl`
- **Structured JSON:** [`4738d717b2905926d77b.json`](../../sessions/47/4738d717b2905926d77b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:10:53.670Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:10:53.670Z",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have enough information to write a thorough assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【致命问题 — 投稿目标与论文主题完全不匹配】\n\n在进入常规 rubric 之前，必须首先指出一个**致命的 scope mismatch**：\n\nCoRL 2026（Conference on Robot Learning）是一个**机器人学习**会议。其 Call for Papers 明确声明：\n> \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n> \"Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 的主题是 **LLM-as-a-Judge 评估系统的对抗鲁棒性认证**，完全属于 NLP/ML evaluation 领域，与机器人学习**零相关**。全文没有任何机器人感知、控制、操作、运动规划、sim-to-real 等内容。\n\n**这篇论文投 CoRL 2026 几乎 100% 会被 desk reject，不会进入审稿流程。**\n\n以下评估假设将此 proposal 投向更合适的场景（如 NeurIPS/ICML/ICLR 主会或 EMNLP），以对 idea 本身进行客观分析。\n\n---\n\n【领域调研】:\n\n- **\"Security in LLM-as-a-Judge: A Comprehensive SoK\"** (arXiv 2603.29403, 2026): 系统梳理了 LLM judge 的安全威胁，分析了 863 篇论文中 45 篇相关工作。报告 open-source judge 模型在多种攻击下有较高 ASR。本 proposal 引用的 50-68% ASR 数据与此一致。\n\n- **Robertson & Koyejo, \"Let's Measure Information Step-by-Step\"** (arXiv 2508.05469, 2025): 证明 bounded f-divergence（如 TVD）在对抗攻击下维持多项式保障，unbounded measures（如 KL）指数退化。**这是本 proposal 的直接前驱——已在单评估器场景建立了认证框架。** 本 proposal 声称的 novelty 是从单评估器扩展到多评估器。\n\n- **Kaneko & Baldwin, \"Bits Leaked per Query\"** (arXiv 2510.17000, NeurIPS 2025 Spotlight): 建立了信息论下界 N_min ≥ log₂(1/ε)/I_max，描述攻破单个 LLM 需要的最小查询数。本 proposal 承认此工作并声称提供 multi-judge 扩展。\n\n- **\"Improving Your Model Ranking on Chatbot Arena by Vote Rigging\"** (ICML 2025): 证明 ~1000 票的 omnipresent rigging 可改善排名 15 位。本 proposal 引用此数据点。\n\n- **\"Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards\"** (ICML 2025): 同样证明 ~1000 票可改变排名，且提出了具体缓解方案并与 Chatbot Arena 合作部署。\n\n- **Qiu et al., \"Truthfulness Despite Weak Supervision\"** (arXiv 2601.20299, ICLR 2026): peer prediction 机制用于 LLM 评估，在面对欺骗模型时优于 LLM-as-a-Judge。\n\n- **Kim et al., \"Correlated Errors in Large Language Models\"** (arXiv 2506.07962): 大规模实证评估发现 LLM 错误显著相关——350+ 模型中，当两个模型都犯错时，60% 的情况下犯同一个错。**这直接影响本 proposal 的核心假设——多 judge 的独立性/相关性参数 ρ 的取值。**\n\n- **\"How Independent are Large Language Models?\"** (arXiv 2604.07650, 2026): 提出审计 LLM 行为纠缠程度并重新加权 verifier ensemble 的统计框架。**这与本 proposal 的目标高度重叠——同样关注 LLM ensemble 中相关性对集成效果的影响。**\n\n- **\"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection\"** (arXiv 2602.08003, 2026): 从信息论角度分析 LLM ensemble 选择。\n\n- **调研总结**: LLM-as-a-Judge 的对抗鲁棒性是一个活跃领域。单模型场景的信息论下界（Kaneko & Baldwin）和认证保障（Robertson & Koyejo）已建立。LLM 间错误相关性已被实证量化（Kim et al.）。peer prediction 激励机制也在并行发展。本 proposal 定位在\"从单 judge 到多 judge 的认证扩展\"，是一个**自然的增量步骤**，而非paradigm shift。同时，2026 年初已有多篇工作从不同角度研究 LLM ensemble 的相关性和信息论性质。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在多个更简单的替代方案值得审视：**\n\n1. **Majority voting + diverse model selection**: 最朴素的多 judge 鲁棒化方案。虽然本 proposal 正确指出 majority voting \"不能提供认证保障\"，但实际部署中，经验性的 majority voting 配合 Kim et al. 量化的跨家族多样性选择，可能已经覆盖了绝大多数实际攻击场景。认证保障（certified bounds）在 ML 安全领域的历史表明，certified defense 往往与 empirical defense 之间存在巨大 gap——certified robustness 社区在 vision 领域的经验教训就是如此。\n\n2. **直接应用 Robertson & Koyejo 的单模型认证 + 简单聚合**: 如果对每个 judge 分别计算 f-divergence 认证，然后用简单独立性假设组合，是否能达到类似效果？Proposal 的核心增量——处理相关性——在实际中增量可能有限，尤其考虑到 copula 模型本身也是近似。\n\n3. **本 proposal 承认的 practical margins 很modest**: K=7 时认证 manipulation-cost 倍数为 2.6-3.7×。这个倍数是否足以改变实际决策？如果攻击者从需要 1000 次查询变为需要 3000 次，这在实际中是否构成有意义的防线？\n\n**增量价值**: 主要在理论层面——提供了第一个 multi-judge manipulation cost 的 formal scaling law。但从实际防御角度看，增量价值不明确。\n\n---\n\n【前提假设检验】:\n\n1. **Gaussian copula 假设**: 核心结果 K_eff = 1+(K-1)·exp(-2·I_max) 依赖于 equicorrelated Gaussian copula 模型。这是一个**强参数化假设**，尤其对 LLM judges 这种高度非线性、离散输出的系统。Proposal 没有论证为什么 copula 模型是 LLM judge 相关性的合理模型，也没有讨论模型误设（model misspecification）的后果。\n\n2. **ρ~0.4-0.5 的相关性估计**: Proposal 引用 Turkmen et al. 和 Kim et al. 来估计跨家族 judge 的 copula 相关性。但 Kim et al. 测量的是**错误相关性**（60% agreement when both err），不是 copula 参数。从错误相关性到 copula ρ 的映射需要额外假设，且可能对模型族选择高度敏感。\n\n3. **\"independent channels\" 假设在 SDPI 组合中的适用性**: SDPI 的 multiplicative decay 依赖于通道独立性。但不同 LLM judges 共享训练数据、RLHF 流程、甚至基础架构，它们的\"通道\"并非独立。Proposal 用 copula 处理相关性，但 SDPI 组合论证的前提——\"perturbation decays multiplicatively across independent channels\"——与 copula 模型之间的衔接逻辑需要仔细验证。\n\n4. **α ∈ [0.35, 0.65] 的 exponent 估计**: 这个范围非常宽（几乎覆盖了从\"接近独立\"到\"高度相关\"的全部 regime），使得核心结论——\"manipulation cost scales as Ω(K^α)\"——在实际意义上变得模糊。如果 α 的真实值接近 0.35 的低端，K=7 时的 bounds 就很弱。\n\n5. **\"任意未来攻击\"的保障 claim**: Proposal 声称 bounds \"hold against arbitrary future attacks\"。但这依赖于相关性模型的正确性——如果未来攻击能利用 judges 之间的相关性结构（而非独立地攻击每个 judge），copula 模型可能低估实际攻击效果。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心贡献是将 Kaneko & Baldwin 的单模型 info-theoretic bounds 扩展到多 judge 场景，同时处理 judge 间相关性。技术工具（SDPI、Fano inequality、Gaussian copula）均为已有工具的标准应用，非新方法论。\"三支柱证明策略\"听起来复杂，实质是将已知工具拼接到新场景。最关键的是，2026 年初已有多篇工作从信息论角度研究 LLM ensemble（arXiv 2602.08003, arXiv 2604.07650），本 proposal 的 novelty 空间正在被快速压缩。Robertson & Koyejo 在单模型场景已建立了 f-divergence 认证框架；Kaneko & Baldwin 已建立了 info-theoretic attack cost bounds。从\"单 judge\"到\"多 judge + 相关性处理\"是一个**自然但增量的扩展**，审稿人很可能说\"this is a natural next step, but not surprising\"。\n\n2. **Significance: 中** — \n   LLM 评估鲁棒性是一个重要且活跃的问题，有实际意义（Chatbot Arena 操纵、judge 安全等）。但 certified bounds 的实际影响力在 ML 安全领域一直受限——vision 领域的 certified robustness 经验表明，认证保障和实际防御之间往往有巨大 gap。本 proposal 承认的 practical margins（2.6-3.7× for K=7）也支持这一担忧。此外，该 proposal 如果投向 NLP/ML 主会（而非 CoRL），其 significance 取决于社区对\"formal guarantees for LLM evaluation\"这一方向的接受度——目前社区更偏重 empirical robustness 而非 certified robustness。\n\n3. **Related Work: 中** — \n   Proposal 对直接前驱工作的覆盖较好（Robertson & Koyejo, Kaneko & Baldwin, arena manipulation papers, peer prediction）。但有几个遗漏：(a) arXiv 2604.07650 \"How Independent are Large Language Models?\" 是一个高度相关的 concurrent work，未被提及；(b) arXiv 2602.08003 关于 LLM ensemble 的信息论视角也未提及；(c) Turkmen et al. 的 copula 模型原始论文我未能通过搜索验证其存在和内容，可能是一个较小众的引用或引用描述不够准确；(d) 部分引用的论文（如 \"Yang et al., ICLR 2026 Workshop AIMS\"）我未能验证其存在。\n\n---\n\n【概率估计】（假设投向合适场景如 ICML/NeurIPS/ICLR，而非 CoRL）: [15% - 25%] 中位 20%\n\n【概率估计】（投 CoRL 2026）: [0% - 3%] 中位 1%\n— CoRL 明确要求 robotics focus，desk reject 概率极高。\n\n【估计理由】:\n- **对于合适场景 (ICML/NeurIPS/ICLR)**: Novelty 弱-中是主要限制因素。核心贡献是已有工具到新场景的自然扩展，而非方法论创新。Practical margins modest，certified robustness 在 ML 评估领域的接受度不如 empirical approaches。同时 2026 年的 concurrent works 正在快速压缩 novelty 空间。不过，问题定义清晰、理论框架完整、方向正确，如果执行出色可以接近 25%。\n- **对于 CoRL**: 这篇论文与 CoRL 的 scope 完全不匹配，几乎确定被 desk reject。\n\n【主要风险】:\n1. **Venue mismatch（致命）**: 投 CoRL 2026 是一个根本性的 scope 错误。CoRL 明确要求 robotics focus，本文纯属 NLP/ML evaluation，会被退稿不审。\n2. **Incremental novelty**: 即使投向合适场景，\"从单 judge 到多 judge 的 info-theoretic bounds 扩展\"很可能被审稿人判定为 natural extension with limited surprise。核心结论——\"more diverse judges = harder to manipulate\"——是大多数研究者的直觉预期，formal proof 的增量价值需要更强的 motivating scenario 来支撑。\n```\n\nSources:\n- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/pdf/2603.29403)\n- [Robertson & Koyejo - Let's Measure Information Step-by-Step](https://arxiv.org/abs/2508.05469)\n- [Kaneko & Baldwin - Bits Leaked per Query](https://arxiv.org/abs/2510.17000)\n- [Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)](https://arxiv.org/html/2501.17858)\n- [Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)](https://arxiv.org/pdf/2501.07493)\n- [Qiu et al. - Truthfulness Despite Weak Supervision](https://arxiv.org/pdf/2601.20299)\n- [Kim et al. - Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962)\n- [How Independent are Large Language Models?](https://arxiv.org/pdf/2604.07650)\n- [Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection](https://arxiv.org/pdf/2602.08003)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CAP: Comparative Augmented Prompting (ICLR 2026)](https://openreview.net/forum?id=wYU6OYFvid)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough information to perform a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：venue 严重不匹配】\n\n本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。但 proposal 内容是关于 LLM-as-judge 评估系统的信息论对抗鲁棒性认证——完全是 NLP evaluation / trustworthy AI / information theory 方向的工作，与机器人学习没有任何关联。\n\nCoRL 2026 Call for Papers 的明确主题包括：机器人感知与控制的学习表征、机器人基础模型、模仿学习、机器人强化学习、机器人安全与对齐、操作/导航/运动/驾驶/飞行中的应用、sim-to-real transfer 等。本 proposal 不涉及任何机器人相关内容。\n\n这属于 desk reject 级别的 scope mismatch。适合的投稿 venue 应为 NeurIPS、ICML、ICLR、AAAI 或 ACL/EMNLP。\n\n以下评估仍按 idea 本身的学术质量进行（假设投稿至合适 venue），但概率估计会同时给出两个版本。\n\n---\n\n【领域调研】:\n\n- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403) (2026): 系统梳理 LLM judge 的对抗攻击面，发现开源 judge 平均 ASR 50-68%，但 7 模型 diverse committee 可将 ASR 降至 10-19%。这是本 proposal 最直接的 empirical 背景，但该 SoK 本身已经证明 multi-judge committee 的经验有效性。\n  \n- [Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs](https://arxiv.org/abs/2510.17000) — Kaneko & Baldwin (NeurIPS 2025 Spotlight): 建立了单模型攻击成本的信息论下界 N_min ≥ log₂(1/ε)/I_max。本 proposal 声称将其推广到多 judge 场景，这是 novelty claim 的核心支点。\n\n- [Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes](https://arxiv.org/abs/2508.05469) — Robertson & Koyejo (2025): 证明了 bounded f-divergence（如 TVD）为单评估器提供多项式级抗操纵保证，unbounded measures（如 KL）则指数退化。本 proposal 在此基础上做多 judge 组合。\n\n- [Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962) — Kim et al. (ICML 2025): 关键发现：即使不同架构、不同 provider 的大模型也存在高度相关的错误（60% error agreement），直接挑战了 \"多样 judge = 独立 channel\" 的假设。\n\n- [Improving Your Model Ranking on Chatbot Arena by Vote Rigging](https://arxiv.org/abs/2501.17858) (ICML 2025): 证明 arena 排名可被几百票操纵翻转。与本 proposal 的动机吻合。\n\n- [Truthful Data Acquisition via Peer Prediction / Evaluating LLMs Using Peer Prediction](https://arxiv.org/abs/2601.20299) — Qiu et al. (2026): peer prediction 方法通过 BNE 实现 incentive-compatibility，解决 LLM judge truthfulness 问题。本 proposal 声称与其互补（peer prediction 解决 incentive，本文解决 adversarial cost scaling），但两者的边界并不完全清晰。\n\n- [Multi-head Ensemble of Smoothed Classifiers for Certified Robustness](https://arxiv.org/abs/2211.10882) (2022): 多分类器 ensemble + randomized smoothing 的 certified radius 研究。本 proposal 声称独立 judge 时恢复 √K 的 certified radius scaling，这正是 randomized smoothing 的已知结果。\n\n- Yang et al. (ICLR 2026 Workshop AIMS): 无法验证此引用的存在。搜索未找到匹配论文。\n- Turkmen et al. equicorrelated model: 无法在 LLM 评估语境中找到此具体引用。\n\n- **调研总结**: LLM-as-judge 的对抗鲁棒性是一个活跃领域。单 judge 的信息论下界（Kaneko & Baldwin）和 f-divergence 认证（Robertson & Koyejo）已建立。multi-judge committee 的经验有效性已在 SoK 中被广泛验证（ASR 降至 10-19%）。本 proposal 的定位是填补\"多 judge 操纵成本的 formal scaling law\"这一理论空白。这个 gap 确实存在，但属于理论完备性补全，而非开辟新方向。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在强 trivial alternative 威胁。** SoK (2026) 已经实证证明，7 个架构多样的模型组成的 committee 可将 ASR 从 50-68% 降至 10-19%。这一经验结果不需要任何信息论机制。\n\n本 proposal 的 certified bound 对 K=7 cross-family ensemble 给出的是 2.6-3.7× 的操纵成本倍增——数值上相当温和。增量价值的核心论点是\"certification vs empirical\"：certified bound 对任意未来攻击成立，而经验 ASR 只对已测试攻击成立。这在 certified robustness 社区是被接受的论点，但在评审中经常遭遇 \"practical margins too small\" 的批评。\n\n简言之：**如果审稿人的标准是\"对实践有指导意义\"，trivial alternative（直接用多样 committee）几乎同样有效；如果标准是\"理论保证的本质不同\"，则有增量价值，但幅度有限。**\n\n---\n\n【前提假设检验】:\n\n本 proposal 的核心逻辑链存在以下未经验证的关键假设：\n\n1. **Judge 通道独立性假设**：SDPI composition 的核心前提是 judges 作为独立 channel 处理扰动。但 Kim et al. (ICML 2025) 的实证发现直接否定了这一点——即使不同架构、不同 provider 的 LLM 也有高度相关的错误（60% agreement when both err）。Gaussian copula 模型试图处理相关性，但用单参数 ρ 刻画复杂的跨模型依赖结构是一个强简化。\n\n2. **Gaussian copula 的适用性**：equicorrelated Gaussian copula 假设所有 judge pair 有相同的相关系数 ρ，现实中不同 judge pair 的相关性差异很大（同系列模型 vs 跨系列模型）。这个假设的违反会导致 K_eff 的估计偏差。\n\n3. **I_max 的可操作性**：信息论下界中的 I_max（每次查询泄露的最大互信息）在实际中如何测量？Kaneko & Baldwin 的单模型设定中这已经是一个挑战；推广到多 judge 组合后，这个量的估计变得更加复杂。\n\n4. **\"Adversarial dual of task-performance scaling\" 的类比是否严谨？** 操纵成本的 scaling 和 task performance 的 scaling 在数学结构上并不对称——一个是对抗性下界，一个是协作性上界，将它们类比为\"dual\"是一个修辞策略，不是严格的数学对偶。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — \n   核心理论 gap（多 judge 操纵成本的 formal scaling）确实存在，但这属于\"理论完备性填补\"而非\"范式创新\"。具体而言：\n   - 独立 judge 情况恢复 √K scaling，这是 randomized smoothing 的已知结论（[Multi-head Ensemble, 2022](https://arxiv.org/abs/2211.10882)）\n   - 相关性导致 effective K 下降的定性结论是直觉性的，Gaussian copula 的闭式解只是给出了定量公式\n   - 三个 proof pillar（SDPI、Fano decomposition、Gaussian copula）都是现有工具的组合应用，而非新方法论\n   - 如果核心结果是 positive（证明了 scaling law），审稿人很可能说 **\"I would have guessed this\"** 而非 \"surprising\"\n\n2. **Significance: 中** — \n   LLM evaluation 的对抗鲁棒性是一个重要且实际的问题。但：\n   - 2.6-3.7× 的 certified bound 在实践中影响有限，尤其是 SoK 已证明 empirical committee 的有效性\n   - 理论贡献的影响主要限于 \"certification\" 子社区\n   - 对更广泛的 ML 社区，这个结果的 actionable insight 有限——结论本质上是 \"用更多更多样的 judge\"，这已经是业界共识\n   - **对 CoRL 社区：significance 为零**，完全不在 scope 内\n\n3. **Related Work: 中偏强** — \n   相关工作覆盖面较广，恰当地引用了 Kaneko & Baldwin、Robertson & Koyejo、SoK、Kim et al. 等关键论文。但存在问题：\n   - Yang et al. (ICLR 2026 Workshop AIMS) 无法验证\n   - Turkmen et al. 的 equicorrelated model 在 LLM 语境中无法找到\n   - 与 [Multi-head Ensemble of Smoothed Classifiers](https://arxiv.org/abs/2211.10882) 的关系（独立 judge = √K scaling）应被明确讨论但未提及\n   - 与 [Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection](https://arxiv.org/abs/2602.08003) 的关系未提及\n\n---\n\n【概率估计】: \n\n- **投稿 CoRL 2026: 2-5%，中位 3%**（基本确定 desk reject，topic 完全 out of scope）\n- **投稿合适 venue（NeurIPS/ICML/ICLR）: 18-28%，中位 22%**\n\n【估计理由】: \n\n**CoRL 估计**：本 proposal 涉及零机器人学习内容，属于 scope mismatch 导致的几乎确定被拒。\n\n**合适 venue 估计**：idea 有真实的理论 gap，但三个因素限制上界：\n(a) Novelty 限制上界——核心结论（多样独立 judge → √K scaling，相关性 → 退化）符合直觉，审稿人不太会觉得 \"surprising\"；\n(b) Trivial alternative 压力——empirical multi-judge committee 已被证明有效，certified bound 的增量价值有限；\n(c) 前提假设脆弱——Gaussian copula 的 equicorrelated 假设与 Kim et al. 的实证发现存在张力。\n上界被 Novelty 和 Trivial Alternative 共同压制在 ~28%。\n\n【主要风险】: \n1. **\"I would have guessed this\" 风险**：核心理论结果（操纵成本随 judge 数量多项式增长、相关性降低有效性）在定性上是显而易见的，审稿人可能认为 Gaussian copula 闭式解只是\"把直觉写成公式\"，缺乏真正的 intellectual surprise。\n2. **Venue scope mismatch（如投 CoRL）**：这是投稿 CoRL 的致命问题。即使 idea 质量更高也无法通过 scope 关。强烈建议改投 NeurIPS 2026 或 ICML 2026 等 ML theory/trustworthy AI track。\n```\n\n---\n\n**总结**：这个 proposal 在 idea 质量上属于\"有真实理论 gap、execution 合理但 surprise 不足\"的类型。在合适的 venue（NeurIPS/ICML）可以一搏（~22%），但投 CoRL 几乎必然被拒——这是一篇关于 LLM 评估信息论鲁棒性的纯理论工作，与 Conference on Robot Learning 的 scope 完全不相关。**最紧急的建议是更换投稿 venue。**\n\nSources:\n- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403)\n- [Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs](https://arxiv.org/abs/2510.17000)\n- [Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes](https://arxiv.org/abs/2508.05469)\n- [Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962)\n- [Improving Your Model Ranking on Chatbot Arena by Vote Rigging](https://arxiv.org/abs/2501.17858)\n- [Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction](https://arxiv.org/abs/2601.20299)\n- [Multi-head Ensemble of Smoothed Classifiers for Certified Robustness](https://arxiv.org/abs/2211.10882)\n- [Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection](https://arxiv.org/abs/2602.08003)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to perform a thorough evaluation. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **\"Security in LLM-as-a-Judge: A Comprehensive SoK\" (arXiv 2603.29403, April 2026)**:\n   对 LLM-as-Judge 安全性的系统化综述，覆盖 863 篇文献，筛选 45 篇。报告开源 judge 模型平均 attack success rate 50–68%（如 Gemma-3-4B 达 65.9%），验证了 proposal 引用的威胁数据基本准确。\n\n2. **Robertson & Koyejo, \"Let's Measure Information Step-by-Step\" (arXiv 2508.05469, Aug 2025)**:\n   提出用 f-divergence（尤其是 TVD-MI）替代传统 judge query 进行 LLM 评估。核心结果(Theorem 3.3)：bounded f-divergence 在 mode-collapse 攻击下保持多项式保证，unbounded (KL) 则指数退化。TVD-MI 在攻击下 AUC 0.70-0.77 vs. 传统 judge 0.50。**这是 proposal 引用的 single-evaluator certification 基础，已验证存在且描述准确。**\n\n3. **Kaneko & Baldwin, \"Bits Leaked per Query\" (arXiv 2510.17000, NeurIPS 2025 Spotlight)**:\n   信息论框架证明 N_min ≥ log₂(1/ε)/I_max 的攻击查询下界。验证了 proposal 对该工作的引用准确。**关键：这是 single-model 攻击成本下界，proposal 声称要将其扩展到 multi-judge——这是合理的研究方向。**\n\n4. **Kim et al., \"Correlated Errors in Large Language Models\" (ICML 2025 Poster, arXiv 2506.07962)**:\n   对 350+ LLMs 大规模实证，发现模型错误高度相关（同一数据集上两模型同时犯错的一致率达 60%）。更大更准的模型即使架构不同也有高相关性。**这直接挑战了 proposal 的乐观假设——ρ~0.4-0.5 的 copula 相关性可能低估了实际相关性，特别是对强模型。**\n\n5. **\"Improving Your Model Ranking on Chatbot Arena by Vote Rigging\" (ICML 2025)**:\n   证明 omnipresent rigging 策略只需数百票即可操纵排名，甚至目标模型未被采样时也有效。验证了 proposal 引用的 arena 操纵威胁。\n\n6. **Qiu et al., \"Truthfulness Despite Weak Supervision\" (arXiv 2601.20299, 2026)**:\n   peer prediction 方法用于 LLM 评估和后训练，基于互预测性奖励诚实回答。**部分验证 proposal 引用的 peer prediction 方向，但具体声称的\"ICLR 2026 via BNE\"未能独立验证。**\n\n7. **Certified Robustness for Ensemble Models (OpenReview, various)**:\n   randomized smoothing 在 ensemble 上的 certified radius 扩展是成熟领域。√K scaling 对 independent classifiers 已是已知结果。\n\n8. **CoRL 2026 Call for Papers (corl.org)**:\n   主题范围：robot perception/control 的表征学习、机器人基础模型、模仿学习、强化学习控制物理机器人、robot safety、manipulation/navigation/locomotion/driving/flight。**明确要求 \"Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\"**\n\n- **调研总结**: LLM-as-Judge 的对抗鲁棒性是一个活跃且重要的研究方向（NeurIPS/ICML/ICLR 级别）。single-evaluator 的 certification（Robertson & Koyejo）和 single-model 攻击下界（Kaneko & Baldwin）已建立；multi-judge 的 manipulation-cost scaling 是一个自然但尚未被正式填补的 gap。**然而，此 proposal 投稿的目标是 CoRL（Conference on Robot Learning），这是一个纯粹的机器人学习会议，与 LLM 评估鲁棒性的信息论证明完全不在同一学科范畴。**\n\n\n【⚠️ 致命问题：会议-论文 Scope 严重不匹配】\n\n在进入三维度评估之前，必须首先指出一个**致命的结构性问题**：\n\n**本 proposal 是一篇纯信息论 + LLM 评估安全的理论工作，目标投稿会议是 CoRL 2026（Conference on Robot Learning）。** CoRL 的 scope 严格限定在 robot learning：机器人感知、控制、基础模型（for robotics）、模仿学习、强化学习（for physical robots）、robot safety（指机器人安全，非 LLM 评估安全）。CoRL 明确鼓励 real-robot experiments 或 sim-to-real transfer 证据。\n\n本 proposal：\n- 无任何机器人实验或机器人应用场景\n- 核心贡献是信息论证明（SDPI contraction, Fano decomposition, Gaussian copula）\n- 应用场景是 LLM chatbot arena 和 LLM-as-Judge 评估\n- 没有任何与 robot learning 的连接点\n\n**这意味着即使 idea 本身质量很高，在 CoRL 也大概率被 desk reject 或在 AC meta-review 阶段因 out-of-scope 被拒。** 此论文的自然投稿目标应该是 NeurIPS / ICML / ICLR / AAAI 的 trustworthy ML / evaluation track，或 AISTATS / ALT 等理论会议。\n\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。**\n\n1. **Majority Voting + Cross-family Diversity**: 实践中，使用 K 个多样化 LLM judge 进行多数投票（majority voting）已经是一种常见做法，且其抗操纵性随 K 自然增长。Proposal 自己承认 majority voting 存在，但声称其\"fundamentally cannot provide\"相同保证。然而，问题是：certified bound 与 majority voting 的 empirical robustness 之间的**实际 gap** 有多大？Proposal 给出的 certified 改进仅为 2.6–3.7× for K=7，而审稿人可能会问：如果 majority voting 在实践中已经提供了类似水平的鲁棒性（即使没有形式化保证），certified bound 的增量价值是什么？\n\n2. **直接应用 Randomized Smoothing 文献**: proposal 承认 independent judges 下 √K scaling 与 randomized smoothing 一致。如果核心贡献退化为\"将 randomized smoothing 的 certified radius 从 image classifiers 搬到 LLM judge ensembles\"，novelty 就被显著压缩。真正的 novelty 在于 correlation-aware 的 degradation 函数 g(I_max)，但这也可以被视为 Gaussian copula 模型下的一个 straightforward calculation。\n\n**增量价值的核心在于**: (a) 形式化保证本身的价值——\"against arbitrary future attacks\"；(b) correlation-aware scaling 的实用指导意义。但 (a) 在 practical impact 上可能较弱（certified bounds 通常很 loose），(b) 的结论——\"越不相关的 judges 越好\"——是直觉显然的。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条存在以下**未经验证的假设**：\n\n1. **Gaussian Copula 假设的适用性**: 整个 closed-form 结果（K_eff = 1+(K-1)·exp(-2·I_max)）依赖于 equicorrelated Gaussian copula 模型。LLM judge 的联合错误结构是否服从 Gaussian copula？Kim et al. (ICML 2025) 的实证发现（大模型错误高度相关，且相关性非均匀）表明 equicorrelated 假设可能过于简化。如果实际相关结构不是 equicorrelated 的（比如存在 cluster 结构——同 family 内高相关，cross-family 低相关），则 K_eff 公式可能不成立。\n\n2. **SDPI Contraction 要求 Independent Channels**: SDPI composition 要求各 judge 作为 independent channels。但 LLM judges 共享训练数据（大量互联网文本）、可能共享 RLHF 偏好数据，因此其 \"channels\" 在根本上不是独立的。Proposal 没有讨论当 channel independence 假设被违反时，bound 如何退化。\n\n3. **ρ~0.4-0.5 的估计可靠性**: proposal 声称 cross-family ensembles 的 copula 相关性为 ρ~0.4-0.5，引用 Turkmen et al. 和 Kim et al.。但 Kim et al. 实际发现了\"更大更准的模型即使架构不同也有高度相关错误\"——这暗示 state-of-the-art models 的 ρ 可能远高于 0.5。如果 ρ → 1，则 K_eff → 1，certified bounds 退化为 trivial。\n\n4. **α ∈ [0.35, 0.65] 的实际含义**: 在 pessimistic 端 α=0.35 下，K=7 的 certified manipulation-cost bound 仅为 ~2.6×。这意味着攻击者仅需 2.6 倍的成本即可突破保证——审稿人可能认为这在实践中不够有意义。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中 (偏弱)** —\n   - 从 single-judge certification (Robertson & Koyejo 2025) 和 single-model attack bounds (Kaneko & Baldwin, NeurIPS 2025) 扩展到 multi-judge 是**自然的下一步**，但也正因\"自然\"，审稿人不太可能觉得 surprising。\n   - 核心数学工具（SDPI contraction, Fano inequality, Gaussian copula）均为成熟工具的**直接组合应用**，而非方法论创新。\n   - Independent judges 下 √K scaling 等价于 randomized smoothing 的已知结果，proposal 自己也承认这一点。\n   - 真正新的部分是 correlation-aware 的 g(I_max) 函数，但在 Gaussian copula 假设下这是一个相对 straightforward 的推导。\n   - **与 Kaneko & Baldwin 的关系**：该工作已提供 single-model 的 information-theoretic attack cost lower bound；将其 compose 到 K 个 model 上，在 independent case 下是教科书级别的 composition，在 correlated case 下是 copula 模型下的 standard calculation。\n\n2. **Significance: 中** —\n   - LLM evaluation robustness 是一个重要且及时的问题（SoK 确认了广泛的攻击面，Kim et al. 确认了错误相关性问题）。\n   - \"Certifiable\"保证有理论价值——与 certified adversarial defense 类比是合理的。\n   - **但实际 impact 存疑**: (a) 2.6-3.7× 的 certified bound 在实践中可能不够 compelling；(b) certified bounds 在 adversarial ML 中通常远 looser 于 empirical robustness，审稿人可能质疑实用性；(c) \"越多样越好\"的核心 takeaway 是直觉显然的。\n   - **致命的 venue 问题**: 即使 significance 对 NLP/ML 评估社区是中等的，对 CoRL（robot learning）社区的 significance 接近于零。\n\n3. **Related Work: 中-强 (偏中)** —\n   - 引用的核心论文基本经过验证：Robertson & Koyejo (2025) ✓，Kaneko & Baldwin (NeurIPS 2025) ✓，Kim et al. (ICML 2025) ✓，Arena vote rigging (ICML 2025) ✓，SoK (2026) ✓。\n   - 差异化定位清晰：single-judge certification → multi-judge scaling gap。\n   - **但部分引用无法验证**: Qiu et al. \"ICLR 2026 via BNE\"、Chen et al. \"NeurIPS 2025 dominant-strategy DMI\"、Yang et al. \"ICLR 2026 Workshop AIMS\" 的具体出处未能通过 web search 独立确认。如果这些引用是虚构的或描述不准确的，将严重损害可信度。\n   - 缺少对 ensemble certified robustness (image classification) 文献的充分讨论——既然 √K scaling 在 randomized smoothing 中已知，需要明确解释与这些工作的区别。\n\n\n【概率估计】: 1% - 5%，中位 2%\n\n【估计理由】:\n这个概率估计几乎**完全由 venue mismatch 决定**。本 proposal 是一篇纯信息论 + LLM 评估安全的理论工作，与 CoRL（Conference on Robot Learning）的 scope 完全不匹配。CoRL 要求论文与 robot learning 相关，鼓励 real-robot experiments 或 sim-to-real evidence。本文没有任何机器人相关内容。在 CoRL，此论文极大概率在 AC 初筛或 reviewer assignment 阶段就因 out-of-scope 被拒。\n\n**如果转投到合适的 venue（NeurIPS/ICML/ICLR trustworthy ML track）**，估计概率为 **18%-28%，中位 22%**。理由：idea 方向站得住脚（填补 multi-judge manipulation cost scaling gap），但核心发现不够 surprising（成熟工具的直接组合，high-level 结论符合直觉），存在显著的 trivial alternative 威胁（majority voting + diversity），且 Gaussian copula 假设可能与实际 LLM 错误结构不匹配（Kim et al. 的实证对此构成挑战）。Novelty 偏弱是限制上界的主要维度。\n\n【主要风险】:\n1. **致命的 venue-scope 不匹配**: 投稿 CoRL 相当于自杀式投稿。即使 idea 有价值，也会因 out-of-scope 被拒，浪费一个投稿周期。这是最需要立即纠正的问题。\n2. **Novelty 不足以支撑 top venue**: 核心贡献是成熟信息论工具（SDPI + Fano + Gaussian copula）在 LLM judge 场景的组合应用，审稿人可能评价为 \"technically correct but incremental\"——single-to-multi judge 的 extension 在 independent case 下是 textbook composition，在 correlated case 下是 standard copula calculation，high-level conclusion（\"more diverse judges = harder to attack\"）是 expected 的。\n```\n\nSources:\n- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/html/2603.29403)\n- [Robertson & Koyejo - Let's Measure Information Step-by-Step](https://arxiv.org/abs/2508.05469)\n- [Kaneko & Baldwin - Bits Leaked per Query](https://arxiv.org/abs/2510.17000)\n- [Kim et al. - Correlated Errors in Large Language Models (ICML 2025)](https://arxiv.org/pdf/2506.07962)\n- [Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)](https://arxiv.org/abs/2501.17858)\n- [Qiu et al. - Truthfulness Despite Weak Supervision](https://arxiv.org/pdf/2601.20299)\n- [Certified Robustness for Ensemble Models](https://openreview.net/pdf?id=IUYthV32lbK)\n- [Boosting Randomized Smoothing with Variance Reduced Classifiers](https://www.sri.inf.ethz.ch/blog/smoothens)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Is LLM-as-a-Judge Robust?](https://arxiv.org/abs/2402.14016)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure\n\n## Description\nLLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, via BNE; Chen et al., NeurIPS 2025, via dominant-strategy DMI), and Kaneko & Baldwin (NeurIPS 2025 spotlight) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling—the adversarial dual of the task-performance scaling recently established by Yang et al. (ICLR 2026 Workshop AIMS). We bridge this gap by proving that adversarial manipulation cost grows as Ω(K^{g(I_max)}) where g is an explicit decreasing function of inter-judge signal correlation, derived via a three-pillar proof strategy: (1) SDPI contraction composition (Polyanskiy & Wu) showing perturbation decays multiplicatively across independent channels; (2) Fano-ensemble decomposition (Morishita et al., ICML 2022) separating relevance, redundancy, and combination loss; (3) Gaussian-copula closed form—adapting Turkmen et al.'s equicorrelated model, we derive K_eff = 1+(K-1)·exp(-2·I_max). Under the copula model, g(I_max) = ½·log(K_eff)/log(K), which equals ½ for independent judges (matching √K certified radius scaling from randomized smoothing) and degrades gracefully with correlation. For cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025), providing certified manipulation-cost bounds of 2.6–3.7× for K=7. We frame this as certifiable robustness for LLM evaluation: just as certified adversarial defenses provide provable guarantees despite sometimes modest empirical margins, our protocol certifies per-evaluation manipulation-resistance bounds that hold against arbitrary future attacks—a guarantee majority voting fundamentally cannot provide. We validate against RobustJudge's 15 realistic attack methods, reporting certified bounds alongside empirical ASR, with sensitivity analysis for α ∈ [0.2, 0.8].\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:10:53.672Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:10:53.672Z",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:10:53.683Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have enough information to write a thorough assessment. Let me compile my findings.

---

```
【阶段】: Triage

【致命问题 — 投稿目标与论文主题完全不匹配】

在进入常规 rubric 之前，必须首先指出一个**致命的 scope mismatch**：

CoRL 2026（Conference on Robot Learning）是一个**机器人学习**会议。其 Call for Papers 明确声明：
> "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
> "Submissions without a robotics focus will be returned without review."

本 proposal 的主题是 **LLM-as-a-Judge 评估系统的对抗鲁棒性认证**，完全属于 NLP/ML evaluation 领域，与机器人学习**零相关**。全文没有任何机器人感知、控制、操作、运动规划、sim-to-real 等内容。

**这篇论文投 CoRL 2026 几乎 100% 会被 desk reject，不会进入审稿流程。**

以下评估假设将此 proposal 投向更合适的场景（如 NeurIPS/ICML/ICLR 主会或 EMNLP），以对 idea 本身进行客观分析。

---

【领域调研】:

- **"Security in LLM-as-a-Judge: A Comprehensive SoK"** (arXiv 2603.29403, 2026): 系统梳理了 LLM judge 的安全威胁，分析了 863 篇论文中 45 篇相关工作。报告 open-source judge 模型在多种攻击下有较高 ASR。本 proposal 引用的 50-68% ASR 数据与此一致。

- **Robertson & Koyejo, "Let's Measure Information Step-by-Step"** (arXiv 2508.05469, 2025): 证明 bounded f-divergence（如 TVD）在对抗攻击下维持多项式保障，unbounded measures（如 KL）指数退化。**这是本 proposal 的直接前驱——已在单评估器场景建立了认证框架。** 本 proposal 声称的 novelty 是从单评估器扩展到多评估器。

- **Kaneko & Baldwin, "Bits Leaked per Query"** (arXiv 2510.17000, NeurIPS 2025 Spotlight): 建立了信息论下界 N_min ≥ log₂(1/ε)/I_max，描述攻破单个 LLM 需要的最小查询数。本 proposal 承认此工作并声称提供 multi-judge 扩展。

- **"Improving Your Model Ranking on Chatbot Arena by Vote Rigging"** (ICML 2025): 证明 ~1000 票的 omnipresent rigging 可改善排名 15 位。本 proposal 引用此数据点。

- **"Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards"** (ICML 2025): 同样证明 ~1000 票可改变排名，且提出了具体缓解方案并与 Chatbot Arena 合作部署。

- **Qiu et al., "Truthfulness Despite Weak Supervision"** (arXiv 2601.20299, ICLR 2026): peer prediction 机制用于 LLM 评估，在面对欺骗模型时优于 LLM-as-a-Judge。

- **Kim et al., "Correlated Errors in Large Language Models"** (arXiv 2506.07962): 大规模实证评估发现 LLM 错误显著相关——350+ 模型中，当两个模型都犯错时，60% 的情况下犯同一个错。**这直接影响本 proposal 的核心假设——多 judge 的独立性/相关性参数 ρ 的取值。**

- **"How Independent are Large Language Models?"** (arXiv 2604.07650, 2026): 提出审计 LLM 行为纠缠程度并重新加权 verifier ensemble 的统计框架。**这与本 proposal 的目标高度重叠——同样关注 LLM ensemble 中相关性对集成效果的影响。**

- **"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection"** (arXiv 2602.08003, 2026): 从信息论角度分析 LLM ensemble 选择。

- **调研总结**: LLM-as-a-Judge 的对抗鲁棒性是一个活跃领域。单模型场景的信息论下界（Kaneko & Baldwin）和认证保障（Robertson & Koyejo）已建立。LLM 间错误相关性已被实证量化（Kim et al.）。peer prediction 激励机制也在并行发展。本 proposal 定位在"从单 judge 到多 judge 的认证扩展"，是一个**自然的增量步骤**，而非paradigm shift。同时，2026 年初已有多篇工作从不同角度研究 LLM ensemble 的相关性和信息论性质。

---

【Trivial Alternative 检验】:

**存在多个更简单的替代方案值得审视：**

1. **Majority voting + diverse model selection**: 最朴素的多 judge 鲁棒化方案。虽然本 proposal 正确指出 majority voting "不能提供认证保障"，但实际部署中，经验性的 majority voting 配合 Kim et al. 量化的跨家族多样性选择，可能已经覆盖了绝大多数实际攻击场景。认证保障（certified bounds）在 ML 安全领域的历史表明，certified defense 往往与 empirical defense 之间存在巨大 gap——certified robustness 社区在 vision 领域的经验教训就是如此。

2. **直接应用 Robertson & Koyejo 的单模型认证 + 简单聚合**: 如果对每个 judge 分别计算 f-divergence 认证，然后用简单独立性假设组合，是否能达到类似效果？Proposal 的核心增量——处理相关性——在实际中增量可能有限，尤其考虑到 copula 模型本身也是近似。

3. **本 proposal 承认的 practical margins 很modest**: K=7 时认证 manipulation-cost 倍数为 2.6-3.7×。这个倍数是否足以改变实际决策？如果攻击者从需要 1000 次查询变为需要 3000 次，这在实际中是否构成有意义的防线？

**增量价值**: 主要在理论层面——提供了第一个 multi-judge manipulation cost 的 formal scaling law。但从实际防御角度看，增量价值不明确。

---

【前提假设检验】:

1. **Gaussian copula 假设**: 核心结果 K_eff = 1+(K-1)·exp(-2·I_max) 依赖于 equicorrelated Gaussian copula 模型。这是一个**强参数化假设**，尤其对 LLM judges 这种高度非线性、离散输出的系统。Proposal 没有论证为什么 copula 模型是 LLM judge 相关性的合理模型，也没有讨论模型误设（model misspecification）的后果。

2. **ρ~0.4-0.5 的相关性估计**: Proposal 引用 Turkmen et al. 和 Kim et al. 来估计跨家族 judge 的 copula 相关性。但 Kim et al. 测量的是**错误相关性**（60% agreement when both err），不是 copula 参数。从错误相关性到 copula ρ 的映射需要额外假设，且可能对模型族选择高度敏感。

3. **"independent channels" 假设在 SDPI 组合中的适用性**: SDPI 的 multiplicative decay 依赖于通道独立性。但不同 LLM judges 共享训练数据、RLHF 流程、甚至基础架构，它们的"通道"并非独立。Proposal 用 copula 处理相关性，但 SDPI 组合论证的前提——"perturbation decays multiplicatively across independent channels"——与 copula 模型之间的衔接逻辑需要仔细验证。

4. **α ∈ [0.35, 0.65] 的 exponent 估计**: 这个范围非常宽（几乎覆盖了从"接近独立"到"高度相关"的全部 regime），使得核心结论——"manipulation cost scales as Ω(K^α)"——在实际意义上变得模糊。如果 α 的真实值接近 0.35 的低端，K=7 时的 bounds 就很弱。

5. **"任意未来攻击"的保障 claim**: Proposal 声称 bounds "hold against arbitrary future attacks"。但这依赖于相关性模型的正确性——如果未来攻击能利用 judges 之间的相关性结构（而非独立地攻击每个 judge），copula 模型可能低估实际攻击效果。

---

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是将 Kaneko & Baldwin 的单模型 info-theoretic bounds 扩展到多 judge 场景，同时处理 judge 间相关性。技术工具（SDPI、Fano inequality、Gaussian copula）均为已有工具的标准应用，非新方法论。"三支柱证明策略"听起来复杂，实质是将已知工具拼接到新场景。最关键的是，2026 年初已有多篇工作从信息论角度研究 LLM ensemble（arXiv 2602.08003, arXiv 2604.07650），本 proposal 的 novelty 空间正在被快速压缩。Robertson & Koyejo 在单模型场景已建立了 f-divergence 认证框架；Kaneko & Baldwin 已建立了 info-theoretic attack cost bounds。从"单 judge"到"多 judge + 相关性处理"是一个**自然但增量的扩展**，审稿人很可能说"this is a natural next step, but not surprising"。

2. **Significance: 中** — 
   LLM 评估鲁棒性是一个重要且活跃的问题，有实际意义（Chatbot Arena 操纵、judge 安全等）。但 certified bounds 的实际影响力在 ML 安全领域一直受限——vision 领域的 certified robustness 经验表明，认证保障和实际防御之间往往有巨大 gap。本 proposal 承认的 practical margins（2.6-3.7× for K=7）也支持这一担忧。此外，该 proposal 如果投向 NLP/ML 主会（而非 CoRL），其 significance 取决于社区对"formal guarantees for LLM evaluation"这一方向的接受度——目前社区更偏重 empirical robustness 而非 certified robustness。

3. **Related Work: 中** — 
   Proposal 对直接前驱工作的覆盖较好（Robertson & Koyejo, Kaneko & Baldwin, arena manipulation papers, peer prediction）。但有几个遗漏：(a) arXiv 2604.07650 "How Independent are Large Language Models?" 是一个高度相关的 concurrent work，未被提及；(b) arXiv 2602.08003 关于 LLM ensemble 的信息论视角也未提及；(c) Turkmen et al. 的 copula 模型原始论文我未能通过搜索验证其存在和内容，可能是一个较小众的引用或引用描述不够准确；(d) 部分引用的论文（如 "Yang et al., ICLR 2026 Workshop AIMS"）我未能验证其存在。

---

【概率估计】（假设投向合适场景如 ICML/NeurIPS/ICLR，而非 CoRL）: [15% - 25%] 中位 20%

【概率估计】（投 CoRL 2026）: [0% - 3%] 中位 1%
— CoRL 明确要求 robotics focus，desk reject 概率极高。

【估计理由】:
- **对于合适场景 (ICML/NeurIPS/ICLR)**: Novelty 弱-中是主要限制因素。核心贡献是已有工具到新场景的自然扩展，而非方法论创新。Practical margins modest，certified robustness 在 ML 评估领域的接受度不如 empirical approaches。同时 2026 年的 concurrent works 正在快速压缩 novelty 空间。不过，问题定义清晰、理论框架完整、方向正确，如果执行出色可以接近 25%。
- **对于 CoRL**: 这篇论文与 CoRL 的 scope 完全不匹配，几乎确定被 desk reject。

【主要风险】:
1. **Venue mismatch（致命）**: 投 CoRL 2026 是一个根本性的 scope 错误。CoRL 明确要求 robotics focus，本文纯属 NLP/ML evaluation，会被退稿不审。
2. **Incremental novelty**: 即使投向合适场景，"从单 judge 到多 judge 的 info-theoretic bounds 扩展"很可能被审稿人判定为 natural extension with limited surprise。核心结论——"more diverse judges = harder to manipulate"——是大多数研究者的直觉预期，formal proof 的增量价值需要更强的 motivating scenario 来支撑。
```

Sources:
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/pdf/2603.29403)
- [Robertson & Koyejo - Let's Measure Information Step-by-Step](https://arxiv.org/abs/2508.05469)
- [Kaneko & Baldwin - Bits Leaked per Query](https://arxiv.org/abs/2510.17000)
- [Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)](https://arxiv.org/html/2501.17858)
- [Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)](https://arxiv.org/pdf/2501.07493)
- [Qiu et al. - Truthfulness Despite Weak Supervision](https://arxiv.org/pdf/2601.20299)
- [Kim et al. - Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962)
- [How Independent are Large Language Models?](https://arxiv.org/pdf/2604.07650)
- [Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection](https://arxiv.org/pdf/2602.08003)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CAP: Comparative Augmented Prompting (ICLR 2026)](https://openreview.net/forum?id=wYU6OYFvid)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough information to perform a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【⚠️ 致命前置问题：venue 严重不匹配】

本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。但 proposal 内容是关于 LLM-as-judge 评估系统的信息论对抗鲁棒性认证——完全是 NLP evaluation / trustworthy AI / information theory 方向的工作，与机器人学习没有任何关联。

CoRL 2026 Call for Papers 的明确主题包括：机器人感知与控制的学习表征、机器人基础模型、模仿学习、机器人强化学习、机器人安全与对齐、操作/导航/运动/驾驶/飞行中的应用、sim-to-real transfer 等。本 proposal 不涉及任何机器人相关内容。

这属于 desk reject 级别的 scope mismatch。适合的投稿 venue 应为 NeurIPS、ICML、ICLR、AAAI 或 ACL/EMNLP。

以下评估仍按 idea 本身的学术质量进行（假设投稿至合适 venue），但概率估计会同时给出两个版本。

---

【领域调研】:

- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403) (2026): 系统梳理 LLM judge 的对抗攻击面，发现开源 judge 平均 ASR 50-68%，但 7 模型 diverse committee 可将 ASR 降至 10-19%。这是本 proposal 最直接的 empirical 背景，但该 SoK 本身已经证明 multi-judge committee 的经验有效性。
  
- [Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs](https://arxiv.org/abs/2510.17000) — Kaneko & Baldwin (NeurIPS 2025 Spotlight): 建立了单模型攻击成本的信息论下界 N_min ≥ log₂(1/ε)/I_max。本 proposal 声称将其推广到多 judge 场景，这是 novelty claim 的核心支点。

- [Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes](https://arxiv.org/abs/2508.05469) — Robertson & Koyejo (2025): 证明了 bounded f-divergence（如 TVD）为单评估器提供多项式级抗操纵保证，unbounded measures（如 KL）则指数退化。本 proposal 在此基础上做多 judge 组合。

- [Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962) — Kim et al. (ICML 2025): 关键发现：即使不同架构、不同 provider 的大模型也存在高度相关的错误（60% error agreement），直接挑战了 "多样 judge = 独立 channel" 的假设。

- [Improving Your Model Ranking on Chatbot Arena by Vote Rigging](https://arxiv.org/abs/2501.17858) (ICML 2025): 证明 arena 排名可被几百票操纵翻转。与本 proposal 的动机吻合。

- [Truthful Data Acquisition via Peer Prediction / Evaluating LLMs Using Peer Prediction](https://arxiv.org/abs/2601.20299) — Qiu et al. (2026): peer prediction 方法通过 BNE 实现 incentive-compatibility，解决 LLM judge truthfulness 问题。本 proposal 声称与其互补（peer prediction 解决 incentive，本文解决 adversarial cost scaling），但两者的边界并不完全清晰。

- [Multi-head Ensemble of Smoothed Classifiers for Certified Robustness](https://arxiv.org/abs/2211.10882) (2022): 多分类器 ensemble + randomized smoothing 的 certified radius 研究。本 proposal 声称独立 judge 时恢复 √K 的 certified radius scaling，这正是 randomized smoothing 的已知结果。

- Yang et al. (ICLR 2026 Workshop AIMS): 无法验证此引用的存在。搜索未找到匹配论文。
- Turkmen et al. equicorrelated model: 无法在 LLM 评估语境中找到此具体引用。

- **调研总结**: LLM-as-judge 的对抗鲁棒性是一个活跃领域。单 judge 的信息论下界（Kaneko & Baldwin）和 f-divergence 认证（Robertson & Koyejo）已建立。multi-judge committee 的经验有效性已在 SoK 中被广泛验证（ASR 降至 10-19%）。本 proposal 的定位是填补"多 judge 操纵成本的 formal scaling law"这一理论空白。这个 gap 确实存在，但属于理论完备性补全，而非开辟新方向。

---

【Trivial Alternative 检验】:

**存在强 trivial alternative 威胁。** SoK (2026) 已经实证证明，7 个架构多样的模型组成的 committee 可将 ASR 从 50-68% 降至 10-19%。这一经验结果不需要任何信息论机制。

本 proposal 的 certified bound 对 K=7 cross-family ensemble 给出的是 2.6-3.7× 的操纵成本倍增——数值上相当温和。增量价值的核心论点是"certification vs empirical"：certified bound 对任意未来攻击成立，而经验 ASR 只对已测试攻击成立。这在 certified robustness 社区是被接受的论点，但在评审中经常遭遇 "practical margins too small" 的批评。

简言之：**如果审稿人的标准是"对实践有指导意义"，trivial alternative（直接用多样 committee）几乎同样有效；如果标准是"理论保证的本质不同"，则有增量价值，但幅度有限。**

---

【前提假设检验】:

本 proposal 的核心逻辑链存在以下未经验证的关键假设：

1. **Judge 通道独立性假设**：SDPI composition 的核心前提是 judges 作为独立 channel 处理扰动。但 Kim et al. (ICML 2025) 的实证发现直接否定了这一点——即使不同架构、不同 provider 的 LLM 也有高度相关的错误（60% agreement when both err）。Gaussian copula 模型试图处理相关性，但用单参数 ρ 刻画复杂的跨模型依赖结构是一个强简化。

2. **Gaussian copula 的适用性**：equicorrelated Gaussian copula 假设所有 judge pair 有相同的相关系数 ρ，现实中不同 judge pair 的相关性差异很大（同系列模型 vs 跨系列模型）。这个假设的违反会导致 K_eff 的估计偏差。

3. **I_max 的可操作性**：信息论下界中的 I_max（每次查询泄露的最大互信息）在实际中如何测量？Kaneko & Baldwin 的单模型设定中这已经是一个挑战；推广到多 judge 组合后，这个量的估计变得更加复杂。

4. **"Adversarial dual of task-performance scaling" 的类比是否严谨？** 操纵成本的 scaling 和 task performance 的 scaling 在数学结构上并不对称——一个是对抗性下界，一个是协作性上界，将它们类比为"dual"是一个修辞策略，不是严格的数学对偶。

---

【3 维度打分】:

1. **Novelty: 中偏弱** — 
   核心理论 gap（多 judge 操纵成本的 formal scaling）确实存在，但这属于"理论完备性填补"而非"范式创新"。具体而言：
   - 独立 judge 情况恢复 √K scaling，这是 randomized smoothing 的已知结论（[Multi-head Ensemble, 2022](https://arxiv.org/abs/2211.10882)）
   - 相关性导致 effective K 下降的定性结论是直觉性的，Gaussian copula 的闭式解只是给出了定量公式
   - 三个 proof pillar（SDPI、Fano decomposition、Gaussian copula）都是现有工具的组合应用，而非新方法论
   - 如果核心结果是 positive（证明了 scaling law），审稿人很可能说 **"I would have guessed this"** 而非 "surprising"

2. **Significance: 中** — 
   LLM evaluation 的对抗鲁棒性是一个重要且实际的问题。但：
   - 2.6-3.7× 的 certified bound 在实践中影响有限，尤其是 SoK 已证明 empirical committee 的有效性
   - 理论贡献的影响主要限于 "certification" 子社区
   - 对更广泛的 ML 社区，这个结果的 actionable insight 有限——结论本质上是 "用更多更多样的 judge"，这已经是业界共识
   - **对 CoRL 社区：significance 为零**，完全不在 scope 内

3. **Related Work: 中偏强** — 
   相关工作覆盖面较广，恰当地引用了 Kaneko & Baldwin、Robertson & Koyejo、SoK、Kim et al. 等关键论文。但存在问题：
   - Yang et al. (ICLR 2026 Workshop AIMS) 无法验证
   - Turkmen et al. 的 equicorrelated model 在 LLM 语境中无法找到
   - 与 [Multi-head Ensemble of Smoothed Classifiers](https://arxiv.org/abs/2211.10882) 的关系（独立 judge = √K scaling）应被明确讨论但未提及
   - 与 [Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection](https://arxiv.org/abs/2602.08003) 的关系未提及

---

【概率估计】: 

- **投稿 CoRL 2026: 2-5%，中位 3%**（基本确定 desk reject，topic 完全 out of scope）
- **投稿合适 venue（NeurIPS/ICML/ICLR）: 18-28%，中位 22%**

【估计理由】: 

**CoRL 估计**：本 proposal 涉及零机器人学习内容，属于 scope mismatch 导致的几乎确定被拒。

**合适 venue 估计**：idea 有真实的理论 gap，但三个因素限制上界：
(a) Novelty 限制上界——核心结论（多样独立 judge → √K scaling，相关性 → 退化）符合直觉，审稿人不太会觉得 "surprising"；
(b) Trivial alternative 压力——empirical multi-judge committee 已被证明有效，certified bound 的增量价值有限；
(c) 前提假设脆弱——Gaussian copula 的 equicorrelated 假设与 Kim et al. 的实证发现存在张力。
上界被 Novelty 和 Trivial Alternative 共同压制在 ~28%。

【主要风险】: 
1. **"I would have guessed this" 风险**：核心理论结果（操纵成本随 judge 数量多项式增长、相关性降低有效性）在定性上是显而易见的，审稿人可能认为 Gaussian copula 闭式解只是"把直觉写成公式"，缺乏真正的 intellectual surprise。
2. **Venue scope mismatch（如投 CoRL）**：这是投稿 CoRL 的致命问题。即使 idea 质量更高也无法通过 scope 关。强烈建议改投 NeurIPS 2026 或 ICML 2026 等 ML theory/trustworthy AI track。
```

---

**总结**：这个 proposal 在 idea 质量上属于"有真实理论 gap、execution 合理但 surprise 不足"的类型。在合适的 venue（NeurIPS/ICML）可以一搏（~22%），但投 CoRL 几乎必然被拒——这是一篇关于 LLM 评估信息论鲁棒性的纯理论工作，与 Conference on Robot Learning 的 scope 完全不相关。**最紧急的建议是更换投稿 venue。**

Sources:
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403)
- [Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs](https://arxiv.org/abs/2510.17000)
- [Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes](https://arxiv.org/abs/2508.05469)
- [Correlated Errors in Large Language Models](https://arxiv.org/abs/2506.07962)
- [Improving Your Model Ranking on Chatbot Arena by Vote Rigging](https://arxiv.org/abs/2501.17858)
- [Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction](https://arxiv.org/abs/2601.20299)
- [Multi-head Ensemble of Smoothed Classifiers for Certified Robustness](https://arxiv.org/abs/2211.10882)
- [Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection](https://arxiv.org/abs/2602.08003)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to perform a thorough evaluation. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:

1. **"Security in LLM-as-a-Judge: A Comprehensive SoK" (arXiv 2603.29403, April 2026)**:
   对 LLM-as-Judge 安全性的系统化综述，覆盖 863 篇文献，筛选 45 篇。报告开源 judge 模型平均 attack success rate 50–68%（如 Gemma-3-4B 达 65.9%），验证了 proposal 引用的威胁数据基本准确。

2. **Robertson & Koyejo, "Let's Measure Information Step-by-Step" (arXiv 2508.05469, Aug 2025)**:
   提出用 f-divergence（尤其是 TVD-MI）替代传统 judge query 进行 LLM 评估。核心结果(Theorem 3.3)：bounded f-divergence 在 mode-collapse 攻击下保持多项式保证，unbounded (KL) 则指数退化。TVD-MI 在攻击下 AUC 0.70-0.77 vs. 传统 judge 0.50。**这是 proposal 引用的 single-evaluator certification 基础，已验证存在且描述准确。**

3. **Kaneko & Baldwin, "Bits Leaked per Query" (arXiv 2510.17000, NeurIPS 2025 Spotlight)**:
   信息论框架证明 N_min ≥ log₂(1/ε)/I_max 的攻击查询下界。验证了 proposal 对该工作的引用准确。**关键：这是 single-model 攻击成本下界，proposal 声称要将其扩展到 multi-judge——这是合理的研究方向。**

4. **Kim et al., "Correlated Errors in Large Language Models" (ICML 2025 Poster, arXiv 2506.07962)**:
   对 350+ LLMs 大规模实证，发现模型错误高度相关（同一数据集上两模型同时犯错的一致率达 60%）。更大更准的模型即使架构不同也有高相关性。**这直接挑战了 proposal 的乐观假设——ρ~0.4-0.5 的 copula 相关性可能低估了实际相关性，特别是对强模型。**

5. **"Improving Your Model Ranking on Chatbot Arena by Vote Rigging" (ICML 2025)**:
   证明 omnipresent rigging 策略只需数百票即可操纵排名，甚至目标模型未被采样时也有效。验证了 proposal 引用的 arena 操纵威胁。

6. **Qiu et al., "Truthfulness Despite Weak Supervision" (arXiv 2601.20299, 2026)**:
   peer prediction 方法用于 LLM 评估和后训练，基于互预测性奖励诚实回答。**部分验证 proposal 引用的 peer prediction 方向，但具体声称的"ICLR 2026 via BNE"未能独立验证。**

7. **Certified Robustness for Ensemble Models (OpenReview, various)**:
   randomized smoothing 在 ensemble 上的 certified radius 扩展是成熟领域。√K scaling 对 independent classifiers 已是已知结果。

8. **CoRL 2026 Call for Papers (corl.org)**:
   主题范围：robot perception/control 的表征学习、机器人基础模型、模仿学习、强化学习控制物理机器人、robot safety、manipulation/navigation/locomotion/driving/flight。**明确要求 "Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."**

- **调研总结**: LLM-as-Judge 的对抗鲁棒性是一个活跃且重要的研究方向（NeurIPS/ICML/ICLR 级别）。single-evaluator 的 certification（Robertson & Koyejo）和 single-model 攻击下界（Kaneko & Baldwin）已建立；multi-judge 的 manipulation-cost scaling 是一个自然但尚未被正式填补的 gap。**然而，此 proposal 投稿的目标是 CoRL（Conference on Robot Learning），这是一个纯粹的机器人学习会议，与 LLM 评估鲁棒性的信息论证明完全不在同一学科范畴。**


【⚠️ 致命问题：会议-论文 Scope 严重不匹配】

在进入三维度评估之前，必须首先指出一个**致命的结构性问题**：

**本 proposal 是一篇纯信息论 + LLM 评估安全的理论工作，目标投稿会议是 CoRL 2026（Conference on Robot Learning）。** CoRL 的 scope 严格限定在 robot learning：机器人感知、控制、基础模型（for robotics）、模仿学习、强化学习（for physical robots）、robot safety（指机器人安全，非 LLM 评估安全）。CoRL 明确鼓励 real-robot experiments 或 sim-to-real transfer 证据。

本 proposal：
- 无任何机器人实验或机器人应用场景
- 核心贡献是信息论证明（SDPI contraction, Fano decomposition, Gaussian copula）
- 应用场景是 LLM chatbot arena 和 LLM-as-Judge 评估
- 没有任何与 robot learning 的连接点

**这意味着即使 idea 本身质量很高，在 CoRL 也大概率被 desk reject 或在 AC meta-review 阶段因 out-of-scope 被拒。** 此论文的自然投稿目标应该是 NeurIPS / ICML / ICLR / AAAI 的 trustworthy ML / evaluation track，或 AISTATS / ALT 等理论会议。


【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

1. **Majority Voting + Cross-family Diversity**: 实践中，使用 K 个多样化 LLM judge 进行多数投票（majority voting）已经是一种常见做法，且其抗操纵性随 K 自然增长。Proposal 自己承认 majority voting 存在，但声称其"fundamentally cannot provide"相同保证。然而，问题是：certified bound 与 majority voting 的 empirical robustness 之间的**实际 gap** 有多大？Proposal 给出的 certified 改进仅为 2.6–3.7× for K=7，而审稿人可能会问：如果 majority voting 在实践中已经提供了类似水平的鲁棒性（即使没有形式化保证），certified bound 的增量价值是什么？

2. **直接应用 Randomized Smoothing 文献**: proposal 承认 independent judges 下 √K scaling 与 randomized smoothing 一致。如果核心贡献退化为"将 randomized smoothing 的 certified radius 从 image classifiers 搬到 LLM judge ensembles"，novelty 就被显著压缩。真正的 novelty 在于 correlation-aware 的 degradation 函数 g(I_max)，但这也可以被视为 Gaussian copula 模型下的一个 straightforward calculation。

**增量价值的核心在于**: (a) 形式化保证本身的价值——"against arbitrary future attacks"；(b) correlation-aware scaling 的实用指导意义。但 (a) 在 practical impact 上可能较弱（certified bounds 通常很 loose），(b) 的结论——"越不相关的 judges 越好"——是直觉显然的。


【前提假设检验】:

核心 claim 的逻辑链条存在以下**未经验证的假设**：

1. **Gaussian Copula 假设的适用性**: 整个 closed-form 结果（K_eff = 1+(K-1)·exp(-2·I_max)）依赖于 equicorrelated Gaussian copula 模型。LLM judge 的联合错误结构是否服从 Gaussian copula？Kim et al. (ICML 2025) 的实证发现（大模型错误高度相关，且相关性非均匀）表明 equicorrelated 假设可能过于简化。如果实际相关结构不是 equicorrelated 的（比如存在 cluster 结构——同 family 内高相关，cross-family 低相关），则 K_eff 公式可能不成立。

2. **SDPI Contraction 要求 Independent Channels**: SDPI composition 要求各 judge 作为 independent channels。但 LLM judges 共享训练数据（大量互联网文本）、可能共享 RLHF 偏好数据，因此其 "channels" 在根本上不是独立的。Proposal 没有讨论当 channel independence 假设被违反时，bound 如何退化。

3. **ρ~0.4-0.5 的估计可靠性**: proposal 声称 cross-family ensembles 的 copula 相关性为 ρ~0.4-0.5，引用 Turkmen et al. 和 Kim et al.。但 Kim et al. 实际发现了"更大更准的模型即使架构不同也有高度相关错误"——这暗示 state-of-the-art models 的 ρ 可能远高于 0.5。如果 ρ → 1，则 K_eff → 1，certified bounds 退化为 trivial。

4. **α ∈ [0.35, 0.65] 的实际含义**: 在 pessimistic 端 α=0.35 下，K=7 的 certified manipulation-cost bound 仅为 ~2.6×。这意味着攻击者仅需 2.6 倍的成本即可突破保证——审稿人可能认为这在实践中不够有意义。


【3 维度打分】:

1. **Novelty: 弱-中 (偏弱)** —
   - 从 single-judge certification (Robertson & Koyejo 2025) 和 single-model attack bounds (Kaneko & Baldwin, NeurIPS 2025) 扩展到 multi-judge 是**自然的下一步**，但也正因"自然"，审稿人不太可能觉得 surprising。
   - 核心数学工具（SDPI contraction, Fano inequality, Gaussian copula）均为成熟工具的**直接组合应用**，而非方法论创新。
   - Independent judges 下 √K scaling 等价于 randomized smoothing 的已知结果，proposal 自己也承认这一点。
   - 真正新的部分是 correlation-aware 的 g(I_max) 函数，但在 Gaussian copula 假设下这是一个相对 straightforward 的推导。
   - **与 Kaneko & Baldwin 的关系**：该工作已提供 single-model 的 information-theoretic attack cost lower bound；将其 compose 到 K 个 model 上，在 independent case 下是教科书级别的 composition，在 correlated case 下是 copula 模型下的 standard calculation。

2. **Significance: 中** —
   - LLM evaluation robustness 是一个重要且及时的问题（SoK 确认了广泛的攻击面，Kim et al. 确认了错误相关性问题）。
   - "Certifiable"保证有理论价值——与 certified adversarial defense 类比是合理的。
   - **但实际 impact 存疑**: (a) 2.6-3.7× 的 certified bound 在实践中可能不够 compelling；(b) certified bounds 在 adversarial ML 中通常远 looser 于 empirical robustness，审稿人可能质疑实用性；(c) "越多样越好"的核心 takeaway 是直觉显然的。
   - **致命的 venue 问题**: 即使 significance 对 NLP/ML 评估社区是中等的，对 CoRL（robot learning）社区的 significance 接近于零。

3. **Related Work: 中-强 (偏中)** —
   - 引用的核心论文基本经过验证：Robertson & Koyejo (2025) ✓，Kaneko & Baldwin (NeurIPS 2025) ✓，Kim et al. (ICML 2025) ✓，Arena vote rigging (ICML 2025) ✓，SoK (2026) ✓。
   - 差异化定位清晰：single-judge certification → multi-judge scaling gap。
   - **但部分引用无法验证**: Qiu et al. "ICLR 2026 via BNE"、Chen et al. "NeurIPS 2025 dominant-strategy DMI"、Yang et al. "ICLR 2026 Workshop AIMS" 的具体出处未能通过 web search 独立确认。如果这些引用是虚构的或描述不准确的，将严重损害可信度。
   - 缺少对 ensemble certified robustness (image classification) 文献的充分讨论——既然 √K scaling 在 randomized smoothing 中已知，需要明确解释与这些工作的区别。


【概率估计】: 1% - 5%，中位 2%

【估计理由】:
这个概率估计几乎**完全由 venue mismatch 决定**。本 proposal 是一篇纯信息论 + LLM 评估安全的理论工作，与 CoRL（Conference on Robot Learning）的 scope 完全不匹配。CoRL 要求论文与 robot learning 相关，鼓励 real-robot experiments 或 sim-to-real evidence。本文没有任何机器人相关内容。在 CoRL，此论文极大概率在 AC 初筛或 reviewer assignment 阶段就因 out-of-scope 被拒。

**如果转投到合适的 venue（NeurIPS/ICML/ICLR trustworthy ML track）**，估计概率为 **18%-28%，中位 22%**。理由：idea 方向站得住脚（填补 multi-judge manipulation cost scaling gap），但核心发现不够 surprising（成熟工具的直接组合，high-level 结论符合直觉），存在显著的 trivial alternative 威胁（majority voting + diversity），且 Gaussian copula 假设可能与实际 LLM 错误结构不匹配（Kim et al. 的实证对此构成挑战）。Novelty 偏弱是限制上界的主要维度。

【主要风险】:
1. **致命的 venue-scope 不匹配**: 投稿 CoRL 相当于自杀式投稿。即使 idea 有价值，也会因 out-of-scope 被拒，浪费一个投稿周期。这是最需要立即纠正的问题。
2. **Novelty 不足以支撑 top venue**: 核心贡献是成熟信息论工具（SDPI + Fano + Gaussian copula）在 LLM judge 场景的组合应用，审稿人可能评价为 "technically correct but incremental"——single-to-multi judge 的 extension 在 independent case 下是 textbook composition，在 correlated case 下是 standard copula calculation，high-level conclusion（"more diverse judges = harder to attack"）是 expected 的。
```

Sources:
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/html/2603.29403)
- [Robertson & Koyejo - Let's Measure Information Step-by-Step](https://arxiv.org/abs/2508.05469)
- [Kaneko & Baldwin - Bits Leaked per Query](https://arxiv.org/abs/2510.17000)
- [Kim et al. - Correlated Errors in Large Language Models (ICML 2025)](https://arxiv.org/pdf/2506.07962)
- [Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)](https://arxiv.org/abs/2501.17858)
- [Qiu et al. - Truthfulness Despite Weak Supervision](https://arxiv.org/pdf/2601.20299)
- [Certified Robustness for Ensemble Models](https://openreview.net/pdf?id=IUYthV32lbK)
- [Boosting Randomized Smoothing with Variance Reduced Classifiers](https://www.sri.inf.ethz.ch/blog/smoothens)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Is LLM-as-a-Judge Robust?](https://arxiv.org/abs/2402.14016)


【原始 proposal（允许参考但不是主要依据）】:
# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure

## Description
LLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, via BNE; Chen et al., NeurIPS 2025, via dominant-strategy DMI), and Kaneko & Baldwin (NeurIPS 2025 spotlight) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling—the adversarial dual of the task-performance scaling recently established by Yang et al. (ICLR 2026 Workshop AIMS). We bridge this gap by proving that adversarial manipulation cost grows as Ω(K^{g(I_max)}) where g is an explicit decreasing function of inter-judge signal correlation, derived via a three-pillar proof strategy: (1) SDPI contraction composition (Polyanskiy & Wu) showing perturbation decays multiplicatively across independent channels; (2) Fano-ensemble decomposition (Morishita et al., ICML 2022) separating relevance, redundancy, and combination loss; (3) Gaussian-copula closed form—adapting Turkmen et al.'s equicorrelated model, we derive K_eff = 1+(K-1)·exp(-2·I_max). Under the copula model, g(I_max) = ½·log(K_eff)/log(K), which equals ½ for independent judges (matching √K certified radius scaling from randomized smoothing) and degrades gracefully with correlation. For cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025), providing certified manipulation-cost bounds of 2.6–3.7× for K=7. We frame this as certifiable robustness for LLM evaluation: just as certified adversarial defenses provide provable guarantees despite sometimes modest empirical margins, our protocol certifies per-evaluation manipulation-resistance bounds that hold against arbitrary future attacks—a guarantee majority voting fundamentally cannot provide. We validate against RobustJudge's 15 realistic attack methods, reporting certified bounds alongside empirical ASR, with sensitivity analysis for α ∈ [0.2, 0.8].


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "33e0c6c4-233f-460e-8e57-9e390864f000",
  "type": "user",
  "uuid": "129bda1a-84ba-47ce-a052-ee3f518bbb4b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:10:53.682Z_

```json
{
  "parentUuid": "129bda1a-84ba-47ce-a052-ee3f518bbb4b",
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
  "uuid": "92b06b49-9b31-43e7-a719-f1f8b4053d99",
  "timestamp": "2026-05-20T03:10:53.682Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:10:53.682Z_

```json
{
  "parentUuid": "92b06b49-9b31-43e7-a719-f1f8b4053d99",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "103cde2b-e3f2-4491-b4eb-e7947f511d2d",
  "timestamp": "2026-05-20T03:10:53.682Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information to write a thorough assessment.…",
  "leafUuid": "103cde2b-e3f2-4491-b4eb-e7947f511d2d",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation adversarial robustness",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:11:25.191Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as the Meta Judge.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 中
- CoRL probability: [0% - 3%] 中位 1%
- Appropriate venue (ICML/NeurIPS/ICLR): [15% - 25%] 中位 20%
- Fatal issue: Venue mismatch (CoRL has no robotics content)
- Key concerns: Incremental novelty, trivial alternatives, Gaussian copula assumptions


**Reviewer 2:**
- Novelty: 中偏弱
- Significance: 中
- Related Work: 中偏强
- CoRL probability: 2-5%, 中位 3%
- Appropriate venue: 18-28%, 中位 22%
- Fatal issue: Venue mismatch
- Key concerns: "I would have guessed this" risk, trivial alternative, copula assumptions

**Reviewer 3:**
- Novelty: 弱-中 (偏弱)
- Significance: 中
- Related Work: 中-强 (偏中)
- CoRL probability: [continuing to assess...]

Compiling the acceptance probabilities across all three reviewers: CoRL estimates cluster tightly around 2-3% with minimal variance, while appropriate venue estimates converge at 22% across the board. The critical finding is that venue mismatch emerges as a fatal flaw with unanimous agreement, alongside concerns about insufficient novelty and the copula assumptions underlying the work. All three reviewers also flagged issues with verifying certain citations, and there are a few concerns that only individual reviewers raised—one flagged a highly overlapping concurrent paper on LLM independence, another questioned whether the "adversarial dual" framing is mathematically rigorous, and a third wants more discussion of ensemble certified robustness literature. Looking at the convergence metrics, the CoRL scores show very tight agreement across reviewers with minimal variance, while venue appropriateness ratings cluster around 20-22%.

For CoRL 2026 specifically, all three reviewers essentially agree this would be a desk reject, giving a final probability estimate of 1-4% with a median of 2%. If submitted to a more appropriate venue, the convergence around 20-22% suggests roughly a 16-26% acceptance range with a median of 21%. Since the proposal targets CoRL, that's the primary estimate to focus on.

The work is primarily theoretical and would need moderate computational resources to validate against RobustJudge's attack methods using multiple LLM judges, along with chat-based data collection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "103cde2b-e3f2-4491-b4eb-e7947f511d2d",
  "isSidechain": false,
  "requestId": "req_011CbD63jYGkPDkzcZSJeu4x",
  "type": "assistant",
  "uuid": "af7fbbbf-18c4-4e03-8981-d1311e071bf7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EH8DG56f3qreT9gaDRSgF3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15426,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3263,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 15426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15426
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

_source line 9 · 2026-05-20T03:12:09.735Z_

【阶段】: Meta Judge
【三次中位】: [20%, 22%, 22%]  std=0.9%（合适 venue）；[1%, 3%, 2%]  std=0.8%（CoRL 2026 实际目标）
【共识维度】:
- **Venue Mismatch（致命）**：3/3 审稿人一致判定——proposal 是纯信息论 + LLM 评估安全的理论工作，与 CoRL（Conference on Robot Learning）的 scope 零交集，几乎确定 desk reject。这是迄今为止最强共识信号。
- **Novelty（弱-中）**：3/3 一致——核心贡献是 SDPI + Fano + Gaussian copula 三个成熟工具在 multi-judge 场景的组合应用，属于"自然的下一步"（natural next step），审稿人大概率反应为"I would have guessed this"。独立 judge 下 √K scaling 是 randomized smoothing 已知结论；correlated case 是 copula 假设下的 standard calculation。
- **Significance（中）**：3/3 一致——问题方向重要且及时，但 certified bound 的 practical margins 较弱（K=7 时仅 2.6-3.7×），certified vs empirical 的 gap 在 ML 安全领域是老问题。
- **Trivial Alternative 威胁（显著）**：3/3 一致——majority voting + cross-family diversity 已被 SoK (2026) 实证验证可将 ASR 从 50-68% 降至 10-19%，不需要任何信息论机制。Certified bound 的增量价值不明确。
- **Gaussian Copula 假设脆弱性**：3/3 一致——equicorrelated 假设与 Kim et al. (ICML 2025) 的实证发现（大模型错误高度相关、相关结构非均匀）存在直接张力。ρ~0.4-0.5 可能低估实际相关性，尤其对 SOTA 模型。
- **SDPI Channel Independence 前提存疑**：3/3 一致——LLM judges 共享训练数据和 RLHF 流程，"independent channels" 假设在根本上不成立。
- **部分引用不可验证**：2/3 审稿人无法验证 Yang et al. (ICLR 2026 Workshop AIMS) 和 Turkmen et al. equicorrelated model 的存在，可信度受损。
- **Related Work（中/中偏强）**：3/3 一致——核心前驱引用覆盖较好，但存在遗漏和不可验证引用。

【异常维度】:
- 仅 R1 强调 arXiv 2604.07650 "How Independent are Large Language Models?" 与 proposal 目标"高度重叠"——R2/R3 未特别标注此 concurrent work 的重叠威胁。但 R1 的判断有搜索支撑，应适度纳入。
- 仅 R2 指出"adversarial dual of task-performance scaling"这一类比是修辞策略而非严格数学对偶——观察合理但非关键维度。
- 仅 R3 明确提到需补充 ensemble certified robustness（image classification）文献讨论——与 R1/R2 的 randomized smoothing √K 共识一致，只是 R3 表述更具体。

【最终概率】: [1% - 4%] 中位 2%（CoRL 2026 实际投稿目标）；[16% - 26%] 中位 21%（若转投合适 venue 如 NeurIPS/ICML/ICLR）
【一致性】: 高（两组估计的 std 均 < 1%，rubric 各维度判决高度一致，无任何维度出现方向性分歧）
【综合理由】:

**1. CoRL 概率（主估计）：** 三位审稿人对 venue mismatch 的判定完全一致且论据充分——CoRL CFP 明确要求 robotics focus 和 real-robot / sim-to-real 证据，本 proposal 无任何机器人相关内容。三个中位（1%, 3%, 2%）极度收敛，我取 2% 作为最终中位，保留 1-4% 区间以覆盖极小概率的"AC 破格考虑"情形。实质上这是 desk reject。

**2. 合适 venue 概率（参考估计）：** 三个中位（20%, 22%, 22%）同样高度收敛。取 21% 作为最终中位。上界受 Novelty 弱-中 的天花板压制——三位审稿人一致认为核心结论不 surprising，成熟工具组合应用。下界受 Significance 中 和问题方向正确的支撑。Trivial alternative 威胁和 copula 假设脆弱性进一步限制上界。

**3. 异常处理：** R1 关于 arXiv 2604.07650 的 overlap 警告虽只有一人提出，但有搜索依据，纳入为次要风险点但不影响整体判决。其余异常均为表述差异而非方向性分歧，不需调整。

**4. 整体判断：** 这是一个"方向正确、gap 真实、但 surprise 不足 + venue 致命错误"的 proposal。即使 idea 本身在合适 venue 有 ~21% 的概率，投 CoRL 等同于废弃这次投稿机会。

【建议】: KILL（投 CoRL）/ 边缘偏不推荐（若转投合适 venue，需显著强化 novelty）

【实施评估】:
  - 计算资源: 中等——需调用 K=3-7 个商业/开源 LLM（DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick 等）作为 judge，运行 RobustJudge 的 15 种攻击方法。估计需数千次 API 调用，成本约 $500-2000。无 GPU 训练需求。
  - 数据需求: Chatbot Arena 公开数据 + RobustJudge benchmark（需确认公开可得性）。不需要私有数据。
  - 人工介入: 低——主要是理论证明和实验代码编写，无需人工标注。
  - 训练需求: 无模型训练——使用现有 LLM 作为 judge，仅需推理。
  - 新 Benchmark: 不需要构建新 benchmark，复用 RobustJudge。
  - 预估周期: 理论证明 2-4 周 + 实验验证 3-4 周 + 写作 2-3 周 ≈ 2-3 个月。但前提是先解决 venue 选择问题——CoRL 2026 deadline 前的所有努力在当前方向下都是浪费。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af7fbbbf-18c4-4e03-8981-d1311e071bf7",
  "isSidechain": false,
  "requestId": "req_011CbD63jYGkPDkzcZSJeu4x",
  "type": "assistant",
  "uuid": "4499c39a-2e1d-4bea-9731-2ee25da1a399",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EH8DG56f3qreT9gaDRSgF3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15426,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15426,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3263,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 15426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15426
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information to write a thorough assessment.…",
  "leafUuid": "4499c39a-2e1d-4bea-9731-2ee25da1a399",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Multi-judge LLM evaluation adversarial robustness",
  "sessionId": "109a48db-eb76-493e-b397-860b884c6c7a"
}
```

---
