# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/efb08a85-fb55-44d5-bd79-417b5e5200dd.jsonl`
- **Structured JSON:** [`6ce13c427cb4c0439009.json`](../../sessions/6c/6ce13c427cb4c0439009.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:34:51.787Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:34:51.787Z",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to conduct a thorough evaluation. Let me synthesize my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486) (arXiv, May 2025): 直接使用 MFRM 比较 10 个 LLM rater 与人类专家的评分效应。已经证明 MFRM 可用于 LLM 评估，但不涉及 contamination。本 proposal 的 MFRM 基础部分与此高度重叠。\n- [Dual Optimal: Make Your LLM Peer-like with Dignity](https://arxiv.org/abs/2604.00979) (arXiv, April 2026): 使用 MFRM 同时标定 judge severity、rubric difficulty 和 question complexity 来评估 LLM。这是最直接的竞争者之一：已在 LLM 评估中应用了 MFRM 的多 facet 标定，但没有建模 contamination。\n- [Using DG-IRT Model to Detect Test Cheating due to Item Compromise](https://link.springer.com/article/10.1007/s11336-012-9311-3) (Psychometrika, 2013): 确认为真实存在的论文。DG-IRT 通过 gating 机制将观测表现分解为真实能力分布和作弊分布。将其从教育作弊检测迁移到 LLM contamination 是本 proposal 的核心创新。\n- [ConStat: Performance-Based Contamination Detection in Large Language Models](https://arxiv.org/abs/2405.16281) (NeurIPS 2024): 通过参考基准比较来检测和量化 contamination，r²=0.94。proposal 中关于 ConStat 的描述准确。\n- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865) (arXiv, March 2026): 通过轮询分配消除 judge bias，但完全忽略 contamination。确认 proposal 中描述准确。\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534) (ICLR 2026): 揭示 generator-judge 关联性导致的 contamination 问题，只提供 post-hoc calibration 修正。确认存在且描述准确。\n- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://arxiv.org/pdf/2507.11405) (EMNLP 2025): 通过 fuzzy inference 调整 contamination-aware 准确率，但不建模 judge effects。确认存在。\n- [Judging the Judges](https://arxiv.org/abs/2604.23178) (arXiv, April 2026): 系统比较 9 种 debiasing 策略，发现 style bias 占主导 (0.76-0.92)，但不提供 measurement model 解释机制。确认存在且描述准确。\n- [Fiedler: Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939) (arXiv, May 2026): 引入 J/ΔJ 诊断指标，识别 shared-calibration 比较中的 sign-reversal failure mode。停留在 classical test theory，无 latent trait 建模。确认存在且描述准确。\n- [PSN-IRT: Lost in Benchmarks?](https://arxiv.org/abs/2505.15055) (AAAI 2026): 用神经 4PL IRT 进行 benchmark 评估，但不涉及 judge modeling 或 contamination correction。\n- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175) (arXiv 2025): 量化心理测量评估中的 LLM contamination（人格测试等），但与 LLM-as-a-judge 场景不同，也不做 joint 建模。\n- **调研总结**: LLM-as-a-judge 评估领域确实形成了两个独立研究簇——judge bias 纠正和 contamination 检测/调整，二者目前互不交叉。MFRM 已被多篇工作应用于 LLM 评估（rater effects 分析、judge severity 标定），但均不涉及 contamination 建模。DG-IRT 的 gating 机制在教育测量中有坚实基础，但尚无人将其迁移至 LLM contamination 场景。Proposal 所声称的 gap（joint judge severity + contamination susceptibility calibration）**经调研确认成立**。\n\n【Trivial Alternative 检验】:\n最直接的 trivial alternative 是 proposal 自身已列为 baseline (5) 的 **naive two-stage pipeline: CyclicJudge → DCR**——先做 judge bias 校正，再做 contamination 调整。这个 pipeline 不需要任何新的 psychometric model，只需串联两个现有工具。\n\n增量价值在哪？Proposal 的论证是：sequential estimation 忽略了 bias 和 contamination 之间的 interaction effects——一个 judge 的 severity 可能与被评模型的 contamination level 相关（例如，contaminated model 可能在某些 judge 上表现更好不是因为 judge bias，而是因为 memorized answer 碰巧匹配该 judge 的 preference）。joint estimation 理论上能更好地解纠缠这些因素。\n\n**但这个增量价值是否足够大是一个实证问题，尚未验证。** 如果两阶段 pipeline 的 Kendall-τ 与 G-MFRM 差距微小（如 0.01-0.02），审稿人会质疑 psychometric overhead 是否值得。这是本 proposal 最大的 trivial alternative 威胁。\n\n【前提假设检验】:\n逻辑链中有以下未经验证的假设：\n\n1. **Rank-1 乘法分解假设 (c_n · e_i)**: 假设 contamination 效应可以分解为 per-model susceptibility × per-item exposure 的乘法形式。这是一个很强的结构假设——实际中，不同模型对不同类型 item 的 contamination 模式可能不同（例如，某模型只在 coding 类 item 上 contaminated，另一个只在 knowledge 类上 contaminated）。Rank-1 AMMI 分解可能过于简化，但如果扩展到更高 rank 又面临 identifiability 问题。\n\n2. **ConStat 外部锚定的迁移性假设**: ConStat 的 r²=0.94 是在原论文特定实验条件下验证的。将其作为 ê_i 锚定信号用于 MT-Bench/Arena-Hard/WildBench 需要额外验证——这些 benchmark 的 item 类型（开放式对话 vs. 选择题/知识题）与 ConStat 原始验证场景可能不同。\n\n3. **Education-to-LLM 类比的有效性**: DG-IRT 中的 \"cheating\" 是二元的（考生要么看过题目要么没看过）。LLM 的 \"contamination\" 是梯度性的（部分记忆、间接暴露、通过类似数据泛化等）。Gating 机制是否能有效捕捉这种连续性 contamination 是一个开放问题。\n\n4. **Judge severity 参数 d_j 的稳定性**: 假设每个 judge 有一个稳定的 severity 参数。但 judge severity 可能随 item 类型、model quality tier 等变化（即存在 judge × item interaction），标准 MFRM 不建模这种交互。\n\n这些假设中，#1 和 #3 是最关键的——如果 rank-1 分解过于粗糙或 gating 机制无法捕捉梯度性 contamination，整个 framework 的增量价值将大幅缩水。\n\n【3 维度打分】:\n1. **Novelty: 中** — Proposal 所声称的 gap 经调研确认成立：目前确实没有工作联合建模 judge severity 和 contamination susceptibility。将 DG-IRT 从教育作弊检测迁移到 LLM contamination 是一个有创意的 cross-domain transfer。然而，核心创新本质上是**已有组件的组合**：MFRM 已被多次应用于 LLM 评估（arXiv:2505.18486, Dual Optimal arXiv:2604.00979），DG-IRT 的 gating 机制是 2013 年的既有方法，LLTM/AMMI 分解是经典技术，ConStat 是现成工具。Proposal 的贡献在于看到这些组件可以以有意义的方式组合——这是合格的 novelty，但不是 paradigm-shifting 的洞察。如果核心实验结果为 positive，审稿人更可能说 \"that makes sense, joint estimation should help\" 而非 \"surprising\"。\n\n2. **Significance: 中偏强** — 研究问题本身非常重要：LLM-as-a-judge 已成为 NLP 评估的主导范式，judge bias 和 contamination 都是严重影响评估可靠性的已知问题。将两个独立研究簇桥接起来有明确的方法论价值。如果 G-MFRM 能证明 joint correction 显著优于 sequential correction，将为社区提供一个有用的评估工具。但 significance 受限于两个因素：(a) 实际改进幅度可能有限（trivial alternative 威胁），(b) 随着模型训练数据透明度提升和 benchmark 动态化趋势，contamination 问题本身可能在逐渐被解决。\n\n3. **Related Work: 强** — Related work 覆盖异常全面，横跨 judge bias 和 contamination 两个 silo，引用了从 2013 年经典 psychometrics (DG-IRT, Fischer 1973) 到 2026 年 5 月最新 arXiv (Fiedler 2605.06939) 的广泛文献。经调研验证，所引论文均真实存在，描述基本准确。Gap 的定位清晰且经得起检验。唯一的小缺陷是未讨论 \"Dual Optimal\" (arXiv:2604.00979) 这篇已在 2026 年 4 月发表的、同样使用 MFRM 进行 LLM judge 标定的工作。\n\n【概率估计】: [28% - 38%] 中位 33%\n\n【估计理由】:\nIdea 处于 25-35% 和 35-45% 两个区间的交界地带，最终定位在 33%。\n\n向上的力量：(1) Gap 经调研确认真实存在——没有现有工作做 joint judge-contamination calibration；(2) 方法论选择 principled 而非 ad-hoc，有坚实的 psychometric 理论支撑；(3) Related work 覆盖极为全面，审稿人不太可能找到遗漏的关键工作；(4) DG-IRT → LLM contamination 的 cross-domain transfer 确实有创意。\n\n限制上界的因素：(1) **核心 novelty 是组合性的**——每个组件都已存在，创新在于\"看到它们可以组合\"，这降低了 surprise factor；(2) **trivial alternative 威胁真实**——naive two-stage pipeline 是一个非常强的 baseline，如果差距微小，paper 的价值主张将被严重削弱；(3) **核心假设未验证**——rank-1 contamination 分解和 DG-IRT gating 机制能否有效迁移到 LLM contamination 的连续性语境仍是开放问题。最主要的上界限制是维度 1 (Novelty)——如果 positive 结果不够 surprising，paper 的 ceiling 就是 \"solid but incremental\"。\n\n【主要风险】:\n1. **Trivial Alternative 风险**: Naive two-stage pipeline (CyclicJudge → DCR) 可能与 G-MFRM 表现相当，审稿人会以 \"unnecessary complexity\" 为由拒稿。Joint estimation 的理论优势在实际数据上可能不够大，尤其当 judge bias 和 contamination 之间的 interaction effect 本身就很小时。\n2. **组合性 Novelty 风险**: 审稿人可能认为 \"将 MFRM 和 DG-IRT 组合起来\" 是一个显而易见的想法一旦有人指出这个 gap，核心贡献可能被视为 \"engineering contribution\" 而非 \"conceptual advance\"——特别是在 MFRM 已被多次应用于 LLM 评估 (arXiv:2505.18486, Dual Optimal) 的情况下。\n```\n\nSources:\n- [Comparing Human and AI Rater Effects Using MFRM](https://arxiv.org/abs/2505.18486)\n- [Dual Optimal: Make Your LLM Peer-like with Dignity](https://arxiv.org/abs/2604.00979)\n- [DG-IRT: Detect Test Cheating due to Item Compromise](https://link.springer.com/article/10.1007/s11336-012-9311-3)\n- [ConStat: Performance-Based Contamination Detection](https://arxiv.org/abs/2405.16281)\n- [CyclicJudge: Mitigating Judge Bias Efficiently](https://arxiv.org/abs/2603.01865)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)\n- [Judging the Judges: Systematic Evaluation of Bias Mitigation](https://arxiv.org/abs/2604.23178)\n- [Fiedler: Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939)\n- [PSN-IRT: Lost in Benchmarks?](https://arxiv.org/abs/2505.15055)\n- [Quantifying Data Contamination in Psychometric Evaluations](https://arxiv.org/abs/2510.07175)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile the triage evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486) (arXiv, May 2025): 最直接的前置工作。将 MFRM 应用于 10 个 LLM rater 与人类专家的评分比较，验证了 MFRM 在 LLM 评分场景中的适用性。但该工作将 contamination 视为外部问题，不在 MFRM 内建模。本 proposal 声称在此基础上扩展，加入 contamination gating，这一增量是真实的。\n- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865) (arXiv, March 2026): Judge bias silo 的代表作。通过 round-robin assignment 消除 judge bias，但完全忽略 contamination。本 proposal 将其作为 baseline 之一。\n- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173/) (EMNLP 2025): Contamination silo 的代表作。通过 fuzzy inference system 合成 contamination scores 调整 raw accuracy，但忽略 judge effects。\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534) (ICLR 2026): 揭示了 generator-judge relatedness 导致的 preference leakage，仅提出 post-hoc contextual calibration。与本 proposal 关注的 contamination 类型不同（preference leakage vs. benchmark data contamination），但属于同一大问题域。\n- [ConStat: Statistical Detection and Quantification of Benchmark Contamination](https://openreview.net/forum?id=ZyVQqK7mcP) (NeurIPS 2024): 提供 black-box contamination 检测（r²=0.94），本 proposal 将其作为外部 exposure indicator 的核心来源。这是一个成熟且经过验证的工具。\n- [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939) (Fiedler, arXiv May 2026): 引入 J/ΔJ diagnostics 识别 sign-reversal failure modes，但停留在 classical test theory 框架内，未做 latent trait modeling。与本 proposal 的 psychometric 路线形成互补而非竞争。\n- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT](https://arxiv.org/abs/2505.15055) (AAAI 2026): 将 neural 4PL IRT 应用于 benchmark 评估，但不涉及 judge severity 和 contamination 的联合建模。\n- [DG-IRT](https://www.researchgate.net/publication/257678777) (Shu, Henson & Luecht, Psychometrika 2013): 原始 DG-IRT 模型，来自教育测量领域的 cheating detection。未被任何人迁移到 LLM 评估场景——这是本 proposal 的核心 cross-domain transfer。\n- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175) (arXiv 2025): 量化 psychometric inventories 中的 data contamination，但关注的是 personality/value questionnaires 而非 benchmark evaluation，且不涉及 judge bias。\n- 调研总结: 该领域明确存在两个研究 silo——judge bias correction 和 contamination detection——且截至 2026 年 5 月，**确实没有现有工作在单一 psychometric framework 内联合建模 judge severity 和 contamination susceptibility**。Proposal 的 gap claim 经验证成立。IRT/MFRM 在 LLM 评估中的应用正在快速增长，但均未实现 bias+contamination 的联合校准。\n\n【Trivial Alternative 检验】:\n最明显的 trivial alternative 是 proposal 自身识别的 **naive two-stage pipeline: CyclicJudge → DCR**（先做 bias correction，再做 contamination adjustment）。这个 baseline 成本低得多（无需构建新的 psychometric model、无需 MCMC、无需三阶段估计），且利用了两个已验证的现有方法。\n\nProposal 为什么认为 joint modeling 优于 sequential correction？隐含论证是：sequential correction 会 propagate errors——如果 bias correction 阶段不知道 contamination 的存在，它可能把 contamination-inflated performance 误归因到 judge severity 参数上，导致 severity 估计偏差，进而扭曲后续的 contamination adjustment。这个论证在理论上是合理的（psychometrics 文献中 joint > sequential 的一般性论证确实成立），但**增量价值的大小是一个纯粹的经验问题**。如果 Kendall-τ 的改善只有 0.01-0.02，psychometric 复杂度的正当性会被审稿人质疑。\n\n增量价值的关键在于：(1) bias 和 contamination 在实际数据中是否存在显著交互（如果它们近似正交，sequential correction 就够了）；(2) rank-1 decomposition c_n·e_i 是否能捕捉到足够的 contamination variance。\n\n【前提假设检验】:\n1. **Rank-1 contamination decomposition 假设**: c_n·e_i 假设 contamination 效果可以分解为 per-model susceptibility × per-item exposure 的乘积。这是一个**强结构性假设**。现实中，不同模型可能对不同类型的 items 有不同的 memorization patterns（例如，code items vs. reasoning items 的 contamination profile 可能因模型训练数据构成而异），这不是 rank-1 能捕捉的。虽然 proposal 引用 AMMI 传统来论证 identifiability，但 identifiability ≠ model adequacy。\n2. **External exposure indicators 的有效性假设**: Proposal 高度依赖 ConStat 的 r²=0.94 验证结果。但 ConStat 的验证是在特定条件下进行的，将其结果直接迁移到 G-MFRM 框架中作为 fixed covariates 使用时，是否仍然有效需要验证。特别是 ConStat 的 reference benchmark variants 需要手工构建（GPT-5.5/Claude-assisted rephrasing），这引入了额外的 construct validity 问题。\n3. **Chatbot Arena 人类投票作为 ground truth 的假设**: 使用 held-out Chatbot Arena human votes 作为 gold standard 来评估 Kendall-τ 改善，但 Chatbot Arena 本身的 noise 和 bias 是众所周知的（position bias、length bias 等）。用一个有偏的 ground truth 来验证 debiasing 方法，存在循环性风险。\n4. **Judge severity 的时间稳定性假设**: MFRM 假设 d_j 是一个稳定的 judge-level 参数，但 LLM judges 的 behavior 可能随 API version 更新、temperature 设置等因素变化。\n\n【3 维度打分】:\n1. Novelty: 【中】 — 核心贡献是将 DG-IRT 的 gating mechanism 从教育 cheating detection 迁移到 LLM contamination，并与 MFRM 的 multi-facet 结构融合。经验证，确实没有现有工作做过这个融合（gap claim 成立）。DG-IRT→LLM 的 cross-domain transfer 有创意，LLTM decomposition 的引入是合理的方法论选择。然而，novelty 的本质是**方法论组合/集成**而非**概念性突破**。每个组件（MFRM、DG-IRT gating、ConStat exposure indicators、LLTM decomposition）都是已有的，创新在于\"把它们放在一起\"。这种 integration novelty 在 EMNLP 审稿中通常被认可但不会被视为 exciting。审稿人可能会说：\"The contribution is incremental — it combines known components in a natural way.\"\n   \n2. Significance: 【中偏强】 — 研究问题毫无疑问是重要的：LLM-as-a-judge 评估已经成为 mainstream practice，且 bias 和 contamination 都是真实且严重的问题。如果 G-MFRM 能显著提升评估质量，其实际影响力会很大。框架产出的可解释性（per-model contamination estimates、per-judge severity calibrations）具有实用价值。但 significance 受限于一个关键不确定性：joint modeling 相对于 naive sequential pipeline 的 marginal improvement 可能不足以改变实际决策。此外，框架的复杂性（三阶段 MCMC、需要构建 reference benchmark variants）可能限制其在实践中的采用。\n\n3. Related Work: 【强】 — 相关工作覆盖异常全面。Proposal 准确地划分了 judge bias silo 和 contamination silo，引用了两个领域的关键论文（CyclicJudge、BiasScope、UDA、Bias-Bounded Evaluation、JudgeBiasBench 在 bias 侧；DCR、ConStat、Preference Leakage、LogProber 在 contamination 侧），以及 IRT-for-LLMs 的主要工作（PSN-IRT、MFRM for LLM raters）。差异化定位清晰且经验证准确。引用的关键论文（arXiv:2505.18486、DG-IRT Psychometrika 2013、ConStat NeurIPS 2024 等）均真实存在且描述准确。唯一的小问题是部分引用的会议/arXiv 论文（如 arXiv:2604.23178, arXiv:2605.06939）非常新，可能尚未被 peer review，但在 arXiv 时代这是可接受的。\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】: \n- Novelty 是中等的：gap 是真实的，方法论融合是合理的，但本质是 integration novelty 而非 conceptual breakthrough。核心发现如果是 positive（\"joint modeling > sequential correction\"），审稿人大概率会说 \"I would have guessed this\" ——联合建模优于分步修正是 psychometrics 领域的 common wisdom，迁移到 LLM 评估场景不构成 surprising finding。这将 novelty 上限锁定在\"中\"。\n- Significance 是中偏强的：问题重要且实用，但 marginal improvement 的不确定性和框架复杂度限制了上界。\n- Related work 是强的：但这主要防止了扣分，不会主动加分。\n- **上界主要被 Novelty 限制**：即使实验做得完美、improvement 显著，\"combining MFRM + DG-IRT + ConStat\" 的 novelty ceiling 也不高。审稿人对 \"integration papers\" 的天然抵触是主要风险。\n- **下界被 Significance 和 Related Work 托住**：问题的重要性和文献定位的清晰性使得即使 novelty 评分偏低，论文也不至于被直接拒绝——有机会通过 solid experiments 争取一些分数。\n\n【主要风险】:\n1. **\"Integration, not innovation\" 质疑**: 审稿人可能认为核心贡献仅是将已有组件（MFRM、DG-IRT、ConStat）组合在一起，每个组件都不是新的，组合方式虽然合理但也是 \"the natural thing to do\"，缺乏真正的 methodological surprise。\n2. **Marginal improvement over naive two-stage pipeline**: 如果 G-MFRM fair scores 相对于 CyclicJudge→DCR 的 Kendall-τ 改善在统计上不显著或实际幅度很小，整个 psychometric 框架的复杂度将无法被 justify。这是最致命的实验风险——idea 层面无法预判，但概率不低。\n```\n\nSources:\n- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)\n- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)\n- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173/)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)\n- [ConStat: Statistical Detection and Quantification of Benchmark Contamination (NeurIPS 2024)](https://openreview.net/forum?id=ZyVQqK7mcP)\n- [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939)\n- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT](https://arxiv.org/abs/2505.15055)\n- [DG-IRT (Shu, Henson & Luecht, Psychometrika 2013)](https://www.researchgate.net/publication/257678777)\n- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175)\n- [BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2602.09383)\n- [Adaptive Testing for LLM Evaluation: ATLAS](https://arxiv.org/abs/2511.04689)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model** (arXiv:2505.18486, May 2025):\n   直接前驱工作。已将 MFRM 应用于 10 个 LLM rater 与人类专家的比较，评估评分一致性和 rater effects。但完全未涉及 contamination 建模——contamination 被视为外部因素。本 proposal 在此基础上增加了 contamination facet，这一扩展是真实增量。\n\n2. **Using Deterministic, Gated IRT Model to Detect Test Cheating due to Item Compromise** (Shu, Henson & Luecht, Psychometrika 2013):\n   DG-IRT 的原始论文。提出将观测表现分解为 genuine ability 和 cheating-inflated 两个分布的 gating 机制。该方法在教育测量中有成熟验证，但从未被迁移到 LLM benchmark contamination 场景。跨领域迁移的 novelty claim 成立。\n\n3. **CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation** (arXiv:2603.01865, March 2026):\n   提出 round-robin judge 分配策略，通过方差分解将 benchmark score variance 分为 scenario/generation/judge/residual 四个分量。证明在固定 judge-call budget 下，cyclic 分配是最优策略。但完全不考虑 contamination。\n\n4. **DCR: Quantifying Data Contamination in LLMs Evaluation** (EMNLP 2025):\n   通过 fuzzy inference 产生统一的 DCR Factor 来调整 raw accuracy，量化 contamination 风险。在 9 个 LLM (0.5B-72B) 上验证，adjusted accuracy 误差在 4% 以内。但完全忽略 judge effects。\n\n5. **ConStat: Performance-Based Contamination Detection in Large Language Models** (NeurIPS 2024):\n   通过对比 primary benchmark 和 reference benchmark（rephrased/synthetic variants）的表现差异来检测和量化 contamination。完全 black-box，validated r²=0.94。本 proposal 将其作为 external exposure indicator 的核心来源。\n\n6. **Preference Leakage: A Contamination Problem in LLM-as-a-judge** (ICLR 2026):\n   揭示 data generator LLM 和 judge LLM 之间的 relatedness 导致 preference leakage。提出 post-hoc calibration，但未构建统一的 measurement model。\n\n7. **PSN-IRT: Lost in Benchmarks? Rethinking LLM Benchmarking with IRT** (AAAI 2026 Oral):\n   用 neural 4PL IRT 框架分析 11 个 benchmark 的 measurement quality，发现广泛的 saturation 和 contamination 问题。但不建模 judge severity，且 contamination 只作为事后诊断，不参与 ability estimation。\n\n8. **UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge** (AAAI 2026):\n   通过 neural K-factor 调整 Elo rating，minimizing inter-judge dispersion。纯 judge bias 方向，不考虑 contamination。\n\n9. **Bias and Uncertainty in LLM-as-a-Judge Estimation** (Fiedler, arXiv:2605.06939, May 2026):\n   提出 J/delta-J diagnostics，识别 shared-calibration 中的 sign-reversal failure modes。停留在 classical test theory，无 latent trait modeling。\n\n10. **Judging the Judges** (Soumik, arXiv:2604.23178, April 2026):\n    实证比较 9 种 debiasing 策略，发现 style bias dominant (0.76–0.92)。但只做经验比较，无 measurement model。\n\n- **调研总结**: LLM-as-a-judge 评估领域在 2025-2026 年经历了快速发展，但确认了 proposal 的核心 claim——judge bias correction 和 contamination detection 形成了两个独立的研究 silo，尚无工作在单一 psychometric 框架内联合建模二者。MFRM 已被应用于 LLM raters（arXiv:2505.18486），DG-IRT 在教育测量中成熟但未被迁移到 LLM 领域。这一 gap 是真实的。\n\n【Trivial Alternative 检验】:\n\nProposal 自身已识别出最关键的 trivial alternative：**两阶段串行 pipeline（CyclicJudge bias correction → DCR contamination adjustment）**。这一 pipeline 成本更低、实现更简单，且复用两个已验证的独立方法。\n\n增量价值主张在于：两阶段方法中，Stage 1 的 bias 估计可能被 contamination effects 混淆（contaminated items 上某些 model 表现异常好，这会扭曲 judge severity 的估计）；同理 Stage 2 的 contamination 调整未考虑 judge-specific bias。联合模型通过同时估计所有 facets 来避免这种 confounding。\n\n**但这一主张的说服力取决于 confounding 的实际量级。** 如果 judge bias 和 contamination 的交互效应较小（即近似可加），两阶段 pipeline 的损失可能微不足道。Proposal 没有提供理论论证说明为什么这种交互应该是 substantial 的——这是一个未被论证的关键环节。\n\n【前提假设检验】:\n\n1. **\"Judge severity 和 contamination susceptibility 之间存在 non-trivial interaction，使得 joint modeling 显著优于 sequential correction\"** ——这是整篇论文存在的理由，但完全是 assumed，无理论推导或 pilot data 支撑。如果这个 interaction 很小，整个框架的价值降低为\"更优雅的形式化\"而非\"更好的估计\"。\n\n2. **\"ConStat 的 exposure indicators 在 MT-Bench / Arena-Hard / WildBench 上仍然有效\"** ——ConStat 的 r²=0.94 是在其原始验证设置下得到的。将其作为 fixed covariate 输入 Stage 3，前提是这些 indicators 在新 benchmark 上保持高质量。如果质量下降，整个 Stage 2 → Stage 3 的 pipeline 都会受损。\n\n3. **\"Rank-1 decomposition (c_n · e_i) 足以捕捉 contamination pattern\"** ——真实 contamination 可能具有更复杂的 model-item 交互结构（例如某些 model 只在特定类型的 items 上受 contamination 影响）。Rank-1 是一个强假设，虽然提高了 identifiability，但可能牺牲了 model fit。\n\n4. **\"Chatbot Arena human votes 是 ground truth\"** ——这是验证标准的选择，但 Chatbot Arena 自身存在 self-selection bias、demographic bias 等已知问题。将其作为 gold standard 需要论证。\n\n【3 维度打分】:\n\n1. **Novelty: 中（偏强）**\n   \n   核心 novelty 有两层：(a) DG-IRT gating mechanism 从教育测量到 LLM evaluation 的跨领域迁移；(b) 在单一 MFRM 框架内联合建模 judge severity 和 contamination susceptibility。调研确认这一 gap 是真实的——arXiv:2505.18486 已将 MFRM 用于 LLM raters 但无 contamination，DG-IRT (Shu 2013) 处理 cheating 但未涉及 multi-judge 场景，CyclicJudge/DCR/Preference Leakage 分别只处理一个 silo。\n   \n   但限制 novelty 评分的是：这本质上是一个 **组合式创新**——将三个已有工具（MFRM + DG-IRT gating + ConStat indicators）按直觉拼接。对一个同时了解 psychometrics 和 LLM evaluation 的研究者来说，一旦识别出两个 silo 的 gap，这个组合方案是相当 natural 的下一步。hierarchical parameterization (c_n · e_i) 是标准的 rank-1 AMMI 分解，three-stage estimation 是常见的 two-step 方法的自然扩展。没有 \"surprising insight\"。\n\n2. **Significance: 中**\n   \n   研究问题本身很重要——LLM-as-a-judge evaluation 是 NLP 领域的核心基础设施，judge bias 和 contamination 是两个被广泛认知的痛点。CyclicJudge (2603.01865)、Fiedler (2605.06939)、Soumik (2604.23178) 等近期密集出现的工作证明了社区对此的关注。\n   \n   但 significance 受限于两个因素：(a) **实际受众窄**——需要运行三阶段 MCMC pipeline + ConStat reference variants 构建的方法，门槛远高于 CyclicJudge 的简单 round-robin。大多数 practitioner 不会采用如此复杂的方案；(b) **improvement 可能 marginal**——如果 joint model 只比 two-stage pipeline 高 2-3% Kendall-τ，审稿人可能认为不足以 justify psychometric machinery 的复杂性。\n\n3. **Related Work: 强**\n   \n   Proposal 对 literature 的覆盖非常全面和准确。两个 silo 的划分清晰，每篇论文的描述经验证基本准确（CyclicJudge 确实是 round-robin + variance decomposition，DCR 确实是 fuzzy inference + DCR Factor，ConStat 确实是 black-box reference comparison，Preference Leakage 确实发表于 ICLR 2026）。DG-IRT (Psychometrika 2013) 作为 inspiration 的引用也是准确的。Fiedler (2605.06939) 和 Soumik (2604.23178) 两篇 May/April 2026 的最新工作也被纳入，显示出对领域的持续跟踪。差异化定位（\"no existing work jointly models both facets\"）在调研中得到确认。\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】:\n- Related Work 维度的强表现确保了 paper 不会因 positioning 问题被拒，但它不提升 idea 的内核质量\n- Novelty 处于中（偏强）水平：gap 真实、组合有原创性，但本质是 \"natural next step\" 式的组合创新，缺乏 surprising insight。审稿人看到 positive results 后可能反应为 \"makes sense, I would have guessed joint modeling helps\"，而非 \"surprising, didn't expect this\"\n- Significance 是限制上界的主要因素：practical complexity 高（三阶段 MCMC + ConStat 变体构建）、受众窄、improvement 可能 marginal。NLP 领域对 psychometric measurement 的接受度有限，可能被认为 \"over-engineered for a problem with simpler solutions\"\n- 概率未能进入 35-45% 区间，因为核心 finding 即使 positive 也不够 surprising，且 trivial alternative (两阶段 pipeline) 的威胁未被理论性地排除\n\n【主要风险】:\n1. **Marginal improvement over naive two-stage pipeline**: 如果 G-MFRM fair scores 相对于 CyclicJudge → DCR 的 Kendall-τ 提升不显著（<3-5%），审稿人会认为 psychometric 复杂性不 justified，可能建议 reject with \"the added machinery doesn't buy enough\"\n2. **\"Engineering contribution, not scientific insight\" 的质疑**: 三个已有组件的拼接缺乏深层 insight 作为支撑——proposal 未论证为什么 judge bias 和 contamination 的交互效应应该是 substantial 的，这使得整个 framework 的必要性悬而未决。审稿人可能给出 \"well-executed but incremental\" 的评价\n```\n\nSources:\n- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)\n- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173/)\n- [ConStat: Performance-Based Contamination Detection in Large Language Models](https://arxiv.org/abs/2405.16281)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)\n- [PSN-IRT: Lost in Benchmarks? Rethinking LLM Benchmarking with IRT](https://arxiv.org/abs/2505.15055)\n- [UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge](https://arxiv.org/abs/2508.09724)\n- [Using Deterministic, Gated IRT Model to Detect Test Cheating](https://www.cambridge.org/core/journals/psychometrika/article/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E)\n- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)\n- [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939)\n- [Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)\n- [BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge](https://arxiv.org/abs/2602.09383)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation\n\n## Description\nWe propose the Gated Many-Facet Rasch Model (G-MFRM), which extends the standard MFRM from educational measurement with a DG-IRT-inspired contamination gating mechanism to jointly calibrate model ability, item difficulty, judge severity, and contamination susceptibility within a single psychometric framework. The critical methodological advance over the original proposal is a hierarchical contamination parameterization: instead of an overparameterized per-(model,item) contamination term c_nk (N×I free parameters, unidentifiable), we decompose contamination into per-model susceptibility c_n modulated by per-item exposure indicators e_i, giving c_n · e_i (N+I parameters). This follows the LLTM (Fischer 1973) design-matrix tradition and the AMMI multiplicative interaction decomposition, both with established identifiability guarantees. Crucially, exposure indicators e_i are estimated externally via ConStat reference benchmark comparison (fully black-box, validated r²=0.94), temporal pre/post-cutoff signals, and LogProber Safe Scores (gray-box) — resolving the circularity of using model-internal residuals to identify contamination. A three-stage estimation strategy ensures identification: (1) standard 3-facet MFRM producing ability, difficulty, and severity estimates plus person-fit diagnostics; (2) external exposure estimation from ConStat and temporal proxies; (3) joint Gated MFRM with fixed exposure indicators and informative priors from Stages 1–2, implemented via Bayesian MCMC in NumPyro. The n-gram overlap signal is dropped for proprietary models (training data undisclosed) and retained only as supplementary validation for open-weight models. Validation spans MT-Bench, Arena-Hard, and WildBench using 8+ LLM judges (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick). We demonstrate that G-MFRM fair scores achieve higher Kendall-τ rank correlation with held-out Chatbot Arena human votes than raw multi-judge averages, CyclicJudge bias-only correction, DCR contamination-only adjustment, Preference Leakage calibration, and a naive two-stage pipeline (CyclicJudge → DCR). Additional analyses include exposure indicator ablation, judge count sensitivity, facet fit statistics, person-fit validation of contamination estimates, and robustness to adversarial contamination (per ICLR 2026 fragility findings). The unified framework yields interpretable per-model contamination estimates, per-judge severity calibrations, and fair ability rankings — bridging the gap between the judge bias correction and contamination detection research silos.\n\n## Core Problem\nCan a hierarchical psychometric measurement model jointly estimate model ability, item difficulty, judge severity, and contamination susceptibility — with the contamination facet decomposed into identifiable per-model and per-item components anchored by external exposure proxies — to produce bias-and-contamination-corrected evaluation scores that outperform both siloed corrections and naive multi-judge averaging?\n\n## Opportunity\nThe LLM-as-a-judge evaluation literature has bifurcated into two silos: (1) judge bias correction methods (CyclicJudge round-robin, Bias-Bounded Evaluation, Soumik's 9-strategy comparison, UDA neural calibration, Fiedler's classical test theory diagnostics) and (2) contamination detection/adjustment methods (DCR Factor, ConStat, Preference Leakage calibration, person-fit screening). No existing work — including all arXiv submissions through May 2026 and ICLR/EMNLP 2026 proceedings — jointly models judge severity and contamination susceptibility within a single calibration framework. The Many-Facet Rasch Model (MFRM) from educational testing naturally accommodates multiple facets in a unified calibration. Recent work has applied MFRM to LLM raters (arXiv:2505.18486) but treats contamination as external. Critically, the Deterministic Gated IRT (DG-IRT) model from psychometric cheating detection (Shu, Henson & Luecht, Psychometrika 2013) provides the missing link: a principled gating mechanism that decomposes observed performance into genuine ability and contamination-inflated components. By combining MFRM's multi-facet structure with DG-IRT's gating logic and externally-anchored exposure indicators from ConStat, we obtain a unified, identifiable model that bridges the gap between these two research silos.\n\n## Landscape\n**Judge bias silo:** CyclicJudge (March 2026) eliminates judge bias via round-robin assignment but ignores contamination. IRT-GRM for judge reliability (Feb 2026) diagnoses judge consistency without modeling contamination. 'Judging the Judges' (Soumik, arXiv:2604.23178, April 2026) empirically compares 9 debiasing strategies across 5 judges, finding style bias dominant (0.76–0.92) but provides no measurement model explaining why strategies work. 'Bias and Uncertainty in LLM-as-a-Judge Estimation' (Fiedler, arXiv:2605.06939, May 2026) introduces formal J/delta-J diagnostics and identifies sign-reversal failure modes in shared-calibration comparisons, but stays within classical test theory without latent trait modeling. BiasScope (ICLR 2026) automates bias discovery post-hoc. Bias-Bounded Evaluation (March 2026) provides formal guarantees retaining 61–99% ranking correlation. JudgeBiasBench (March 2026) defines a taxonomy of 12 bias types across 4 dimensions. UDA (AAAI 2026) uses neural K-factor adjustment to reduce inter-judge standard deviation by 63.4%. **Contamination silo:** DCR Factor (EMNLP 2025) adjusts accuracy for contamination via fuzzy inference but ignores judge effects. Preference Leakage (ICLR 2026) quantifies generator-judge relatedness bias but proposes only post-hoc calibration. ConStat (NeurIPS 2024) computes contamination effects via reference benchmark comparison (r²=0.94 with true effects) — fully black-box. LogProber (2024) estimates per-item Safe Scores from token log-probabilities. 'On The Fragility of Benchmark Contamination Detection in Reasoning Models' (ICLR 2026) shows RL post-training obscures contamination signals, motivating multi-indicator approaches. **IRT for LLMs (no judge + contamination unification):** PSN-IRT (AAAI 2026) applies neural 4PL IRT to benchmark evaluation. MFRM has been applied to compare 10 LLM raters with human experts (May 2025) and to ChatGPT-4 essay scoring (RMAL 2024). **Gap:** No existing work jointly models judge severity and contamination susceptibility within a single psychometric calibration framework, nor has anyone adapted DG-IRT's gating mechanism from educational cheating detection to LLM benchmark contamination.\n\n## Approach\nWe propose a Gated Many-Facet Rasch Model (G-MFRM) that extends the standard MFRM with a DG-IRT-inspired contamination gating mechanism, using a three-stage estimation strategy that ensures identifiability.\n\n**Model formulation.** The core log-odds model is:\n\n  logit(P_nij) = θ_n − b_i − d_j + c_n · e_i\n\nwhere θ_n is model ability, b_i is item difficulty, d_j is judge severity, c_n is per-model contamination susceptibility, and e_i is per-item exposure level. The contamination term c_n · e_i replaces the overparameterized per-(model,item) c_nk from the original proposal: instead of N×I free parameters, this hierarchical decomposition requires only N + I parameters (or just N when e_i is externally anchored). This follows the LLTM (Linear Logistic Test Model, Fischer 1973) tradition of decomposing item parameters via a known or estimable design matrix, and is a rank-1 special case of the AMMI (Additive Main Effects and Multiplicative Interaction) decomposition, both with well-established identifiability guarantees.\n\nThe DG-IRT gating interpretation: when e_i ≈ 0 (unexposed item), the model reduces to the standard 3-facet MFRM measuring genuine ability; when e_i > 0, performance is inflated by c_n · e_i, where c_n captures how much each model benefits from data leakage. This directly mirrors DG-IRT's decomposition of observed performance into genuine and cheating-inflated distributions.\n\n**Three-stage estimation (resolving circularity).**\n\n*Stage 1 — Standard 3-facet MFRM:* Fit θ_n, b_i, d_j via Bayesian MCMC (NumPyro on GPU), ignoring contamination. This produces uncontaminated ability estimates and, critically, standardized residuals r_ni and person-fit statistics (lz, EMRi) per model.\n\n*Stage 2 — External exposure estimation:* Estimate e_i from external proxies that are independent of the MFRM fit, resolving the circularity the reviewer identified:\n  (a) ConStat delta scores: compare model performance on original benchmark items vs. rephrased/synthetic reference variants (fully black-box, validated r²=0.94 with true contamination effects);\n  (b) Temporal signals: performance gaps on items with pre-cutoff vs. post-cutoff variants (available for benchmarks with versioned items);\n  (c) LogProber Safe Scores: per-item memorization indicators from token log-probability analysis (gray-box; for models exposing logprobs: GPT-5.5, DeepSeek-V4, Qwen3, Llama 4).\n  These indicators are combined via a weighted composite (weights tuned on a held-out validation split) to produce ê_i. Person-fit statistics from Stage 1 serve as validation — models with high contamination should exhibit difficulty-insensitive response patterns (high Guttman errors, low lz) — but are NOT used to estimate e_i, avoiding circularity.\n\n*Stage 3 — Joint Gated MFRM:* Refit the full 4-facet model with ê_i as fixed (observed) covariates and c_n as latent parameters, using Stage 1 estimates as informative priors. Identifiability constraints: sum(c_n) = 0 (centered contamination susceptibility) and ê_i scale fixed from Stage 2. This yields contamination-corrected 'fair scores' θ̂_n — model ability estimates purged of both judge bias (via d_j) and contamination inflation (via c_n · ê_i).\n\n**N-gram overlap dropped for proprietary models.** Following the reviewer's feedback, we remove n-gram overlap as a contamination signal since OpenAI, Anthropic, and Google do not disclose training data. ConStat and temporal signals are fully black-box; LogProber requires only logprob access. For open-weight models with documented training data (DeepSeek-V4, Kimi K2.6, Qwen3, Llama 4), n-gram overlap can serve as supplementary validation of ê_i estimates.\n\n**Validation.** Experiments span MT-Bench, Arena-Hard, and WildBench using 8+ LLM judges: proprietary (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6) and open-weight (DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick). We construct reference benchmark variants for ConStat by GPT-5.5/Claude-assisted rephrasing (validated by human equivalence checking). We evaluate by demonstrating that G-MFRM fair scores θ̂_n achieve higher Kendall-τ rank correlation with held-out Chatbot Arena human votes than five baselines: (1) raw multi-judge averages, (2) CyclicJudge bias-only correction, (3) DCR Factor contamination-only adjustment, (4) Preference Leakage post-hoc calibration, and (5) a naive two-stage pipeline (CyclicJudge bias correction → DCR contamination adjustment) — the 'simpler baseline' that reviewers would demand to justify the psychometric overhead. Additional analyses include: (a) ablation of each exposure indicator's contribution to ê_i; (b) sensitivity analysis varying the number of judges (2, 4, 6, 8+); (c) facet fit statistics (infit/outfit MNSQ) to validate measurement quality; (d) comparison of Stage 1 person-fit flagging (lz, EMRi) against Stage 3 contamination estimates c_n as a validation of construct coherence; (e) robustness check against adversarial contamination following Wang et al. (ICLR 2026) fragility findings.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '180–250 (open-source judge inference via vLLM ~130h on A100-80GB; ConStat reference variant generation + evaluation ~30h; Bayesian MCMC fitting ~15h; ablations and sensitivity analysis ~50h)', 'timeline': '10–12 weeks (G-MFRM implementation + ConStat integration 3w, reference benchmark variant construction 2w, multi-judge data collection 3w, experiments and analysis 2w, paper writing 2w)', 'estimated_gpu_cost': '$450–625 (A100 spot at ~$2.50/hr) + ~$900 proprietary judge API calls (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6)'}, 'human_in_loop': {'gpu_hours': '180–250', 'timeline': '7–9 weeks (Claude accelerates G-MFRM implementation, ConStat integration, experiment scripting, and drafting)', 'claude_api_cost': '$100–150', 'estimated_gpu_cost': '$450–625 + ~$900 proprietary judge API calls'}, 'auto_research': {'gpu_hours': '180–250', 'timeline': '5–7 weeks', 'claude_api_cost': '$250–400 (end-to-end code generation, three-stage estimation pipeline, hyperparameter search, convergence diagnostics, paper writing)', 'estimated_gpu_cost': '$450–625 + ~$900 proprietary judge API calls', 'speed_bottleneck': 'Proprietary judge API rate limits (GPT-5.5/Claude batch quotas); ConStat reference variant quality validation; sequential three-stage MCMC convergence requiring iterative checks'}}\n\n## Inspired By\nCross-domain transfer of DG-IRT (Shu et al., Psychometrika 2013) gating mechanism from educational cheating detection to LLM contamination; MFRM multi-facet calibration for judge bias; LLTM (Fischer 1973) design-matrix decomposition for identifiable contamination parameterization; ConStat (NeurIPS 2024) external exposure indicators; combination of CyclicJudge judge modeling + ConStat contamination quantification + IRT measurement backbone.\n\n## Target Venues\n- AAAI 2027 (full paper: July 28, 2026)\n- ACL 2027 (ARR submission: August 3, 2026)\n- EACL 2027 (ARR submission: August 3, 2026)\n- NAACL 2027 (ARR submission: October 15, 2026)\n\n## Key References\n- Using Deterministic, Gated IRT Model to Detect Test Cheating due to Item Compromise (Shu, Henson & Luecht, Psychometrika 2013)\n- Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model (arXiv 2025)\n- ConStat: Statistical Detection and Quantification of Benchmark Contamination (NeurIPS 2024)\n- CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation (arXiv 2026)\n- Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory (arXiv 2026)\n- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)\n- DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)\n- Bias and Uncertainty in LLM-as-a-Judge Estimation (Fiedler, arXiv:2605.06939, May 2026)\n- Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines (Soumik, arXiv:2604.23178, April 2026)\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models (ICLR 2026)\n- BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation (ICLR 2026)\n- LogProber: Detecting Data Contamination via Token Log-Probability Analysis (arXiv 2024)\n- An application of many-facet Rasch measurement to evaluate automated essay scoring: A case of ChatGPT-4.0 (RMAL 2024)\n- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2026)\n- JudgeBiasBench: Evaluating and Mitigating Bias in LLM-Based Judges (arXiv 2026)\n- The Linear Logistic Test Model (Fischer, Psychometrika 1973)\n- Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT (AAAI 2026)\n- Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (NeurIPS 2023)\n- py-irt: A Scalable Item Response Theory Library for Python (INFORMS JoC 2023)\n- UDA: Unsupervised Debiasing Alignment for LLM Judges (AAAI 2026)\n- Evaluating Rater Effects of Large Language Models in Automated Essay Scoring (Educational Measurement 2026)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:34:51.790Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:34:51.790Z",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T04:34:51.802Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to conduct a thorough evaluation. Let me synthesize my findings.

---

```
【阶段】: Triage

【领域调研】:
- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486) (arXiv, May 2025): 直接使用 MFRM 比较 10 个 LLM rater 与人类专家的评分效应。已经证明 MFRM 可用于 LLM 评估，但不涉及 contamination。本 proposal 的 MFRM 基础部分与此高度重叠。
- [Dual Optimal: Make Your LLM Peer-like with Dignity](https://arxiv.org/abs/2604.00979) (arXiv, April 2026): 使用 MFRM 同时标定 judge severity、rubric difficulty 和 question complexity 来评估 LLM。这是最直接的竞争者之一：已在 LLM 评估中应用了 MFRM 的多 facet 标定，但没有建模 contamination。
- [Using DG-IRT Model to Detect Test Cheating due to Item Compromise](https://link.springer.com/article/10.1007/s11336-012-9311-3) (Psychometrika, 2013): 确认为真实存在的论文。DG-IRT 通过 gating 机制将观测表现分解为真实能力分布和作弊分布。将其从教育作弊检测迁移到 LLM contamination 是本 proposal 的核心创新。
- [ConStat: Performance-Based Contamination Detection in Large Language Models](https://arxiv.org/abs/2405.16281) (NeurIPS 2024): 通过参考基准比较来检测和量化 contamination，r²=0.94。proposal 中关于 ConStat 的描述准确。
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865) (arXiv, March 2026): 通过轮询分配消除 judge bias，但完全忽略 contamination。确认 proposal 中描述准确。
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534) (ICLR 2026): 揭示 generator-judge 关联性导致的 contamination 问题，只提供 post-hoc calibration 修正。确认存在且描述准确。
- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://arxiv.org/pdf/2507.11405) (EMNLP 2025): 通过 fuzzy inference 调整 contamination-aware 准确率，但不建模 judge effects。确认存在。
- [Judging the Judges](https://arxiv.org/abs/2604.23178) (arXiv, April 2026): 系统比较 9 种 debiasing 策略，发现 style bias 占主导 (0.76-0.92)，但不提供 measurement model 解释机制。确认存在且描述准确。
- [Fiedler: Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939) (arXiv, May 2026): 引入 J/ΔJ 诊断指标，识别 shared-calibration 比较中的 sign-reversal failure mode。停留在 classical test theory，无 latent trait 建模。确认存在且描述准确。
- [PSN-IRT: Lost in Benchmarks?](https://arxiv.org/abs/2505.15055) (AAAI 2026): 用神经 4PL IRT 进行 benchmark 评估，但不涉及 judge modeling 或 contamination correction。
- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175) (arXiv 2025): 量化心理测量评估中的 LLM contamination（人格测试等），但与 LLM-as-a-judge 场景不同，也不做 joint 建模。
- **调研总结**: LLM-as-a-judge 评估领域确实形成了两个独立研究簇——judge bias 纠正和 contamination 检测/调整，二者目前互不交叉。MFRM 已被多篇工作应用于 LLM 评估（rater effects 分析、judge severity 标定），但均不涉及 contamination 建模。DG-IRT 的 gating 机制在教育测量中有坚实基础，但尚无人将其迁移至 LLM contamination 场景。Proposal 所声称的 gap（joint judge severity + contamination susceptibility calibration）**经调研确认成立**。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是 proposal 自身已列为 baseline (5) 的 **naive two-stage pipeline: CyclicJudge → DCR**——先做 judge bias 校正，再做 contamination 调整。这个 pipeline 不需要任何新的 psychometric model，只需串联两个现有工具。

增量价值在哪？Proposal 的论证是：sequential estimation 忽略了 bias 和 contamination 之间的 interaction effects——一个 judge 的 severity 可能与被评模型的 contamination level 相关（例如，contaminated model 可能在某些 judge 上表现更好不是因为 judge bias，而是因为 memorized answer 碰巧匹配该 judge 的 preference）。joint estimation 理论上能更好地解纠缠这些因素。

**但这个增量价值是否足够大是一个实证问题，尚未验证。** 如果两阶段 pipeline 的 Kendall-τ 与 G-MFRM 差距微小（如 0.01-0.02），审稿人会质疑 psychometric overhead 是否值得。这是本 proposal 最大的 trivial alternative 威胁。

【前提假设检验】:
逻辑链中有以下未经验证的假设：

1. **Rank-1 乘法分解假设 (c_n · e_i)**: 假设 contamination 效应可以分解为 per-model susceptibility × per-item exposure 的乘法形式。这是一个很强的结构假设——实际中，不同模型对不同类型 item 的 contamination 模式可能不同（例如，某模型只在 coding 类 item 上 contaminated，另一个只在 knowledge 类上 contaminated）。Rank-1 AMMI 分解可能过于简化，但如果扩展到更高 rank 又面临 identifiability 问题。

2. **ConStat 外部锚定的迁移性假设**: ConStat 的 r²=0.94 是在原论文特定实验条件下验证的。将其作为 ê_i 锚定信号用于 MT-Bench/Arena-Hard/WildBench 需要额外验证——这些 benchmark 的 item 类型（开放式对话 vs. 选择题/知识题）与 ConStat 原始验证场景可能不同。

3. **Education-to-LLM 类比的有效性**: DG-IRT 中的 "cheating" 是二元的（考生要么看过题目要么没看过）。LLM 的 "contamination" 是梯度性的（部分记忆、间接暴露、通过类似数据泛化等）。Gating 机制是否能有效捕捉这种连续性 contamination 是一个开放问题。

4. **Judge severity 参数 d_j 的稳定性**: 假设每个 judge 有一个稳定的 severity 参数。但 judge severity 可能随 item 类型、model quality tier 等变化（即存在 judge × item interaction），标准 MFRM 不建模这种交互。

这些假设中，#1 和 #3 是最关键的——如果 rank-1 分解过于粗糙或 gating 机制无法捕捉梯度性 contamination，整个 framework 的增量价值将大幅缩水。

【3 维度打分】:
1. **Novelty: 中** — Proposal 所声称的 gap 经调研确认成立：目前确实没有工作联合建模 judge severity 和 contamination susceptibility。将 DG-IRT 从教育作弊检测迁移到 LLM contamination 是一个有创意的 cross-domain transfer。然而，核心创新本质上是**已有组件的组合**：MFRM 已被多次应用于 LLM 评估（arXiv:2505.18486, Dual Optimal arXiv:2604.00979），DG-IRT 的 gating 机制是 2013 年的既有方法，LLTM/AMMI 分解是经典技术，ConStat 是现成工具。Proposal 的贡献在于看到这些组件可以以有意义的方式组合——这是合格的 novelty，但不是 paradigm-shifting 的洞察。如果核心实验结果为 positive，审稿人更可能说 "that makes sense, joint estimation should help" 而非 "surprising"。

2. **Significance: 中偏强** — 研究问题本身非常重要：LLM-as-a-judge 已成为 NLP 评估的主导范式，judge bias 和 contamination 都是严重影响评估可靠性的已知问题。将两个独立研究簇桥接起来有明确的方法论价值。如果 G-MFRM 能证明 joint correction 显著优于 sequential correction，将为社区提供一个有用的评估工具。但 significance 受限于两个因素：(a) 实际改进幅度可能有限（trivial alternative 威胁），(b) 随着模型训练数据透明度提升和 benchmark 动态化趋势，contamination 问题本身可能在逐渐被解决。

3. **Related Work: 强** — Related work 覆盖异常全面，横跨 judge bias 和 contamination 两个 silo，引用了从 2013 年经典 psychometrics (DG-IRT, Fischer 1973) 到 2026 年 5 月最新 arXiv (Fiedler 2605.06939) 的广泛文献。经调研验证，所引论文均真实存在，描述基本准确。Gap 的定位清晰且经得起检验。唯一的小缺陷是未讨论 "Dual Optimal" (arXiv:2604.00979) 这篇已在 2026 年 4 月发表的、同样使用 MFRM 进行 LLM judge 标定的工作。

【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
Idea 处于 25-35% 和 35-45% 两个区间的交界地带，最终定位在 33%。

向上的力量：(1) Gap 经调研确认真实存在——没有现有工作做 joint judge-contamination calibration；(2) 方法论选择 principled 而非 ad-hoc，有坚实的 psychometric 理论支撑；(3) Related work 覆盖极为全面，审稿人不太可能找到遗漏的关键工作；(4) DG-IRT → LLM contamination 的 cross-domain transfer 确实有创意。

限制上界的因素：(1) **核心 novelty 是组合性的**——每个组件都已存在，创新在于"看到它们可以组合"，这降低了 surprise factor；(2) **trivial alternative 威胁真实**——naive two-stage pipeline 是一个非常强的 baseline，如果差距微小，paper 的价值主张将被严重削弱；(3) **核心假设未验证**——rank-1 contamination 分解和 DG-IRT gating 机制能否有效迁移到 LLM contamination 的连续性语境仍是开放问题。最主要的上界限制是维度 1 (Novelty)——如果 positive 结果不够 surprising，paper 的 ceiling 就是 "solid but incremental"。

【主要风险】:
1. **Trivial Alternative 风险**: Naive two-stage pipeline (CyclicJudge → DCR) 可能与 G-MFRM 表现相当，审稿人会以 "unnecessary complexity" 为由拒稿。Joint estimation 的理论优势在实际数据上可能不够大，尤其当 judge bias 和 contamination 之间的 interaction effect 本身就很小时。
2. **组合性 Novelty 风险**: 审稿人可能认为 "将 MFRM 和 DG-IRT 组合起来" 是一个显而易见的想法一旦有人指出这个 gap，核心贡献可能被视为 "engineering contribution" 而非 "conceptual advance"——特别是在 MFRM 已被多次应用于 LLM 评估 (arXiv:2505.18486, Dual Optimal) 的情况下。
```

Sources:
- [Comparing Human and AI Rater Effects Using MFRM](https://arxiv.org/abs/2505.18486)
- [Dual Optimal: Make Your LLM Peer-like with Dignity](https://arxiv.org/abs/2604.00979)
- [DG-IRT: Detect Test Cheating due to Item Compromise](https://link.springer.com/article/10.1007/s11336-012-9311-3)
- [ConStat: Performance-Based Contamination Detection](https://arxiv.org/abs/2405.16281)
- [CyclicJudge: Mitigating Judge Bias Efficiently](https://arxiv.org/abs/2603.01865)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)
- [Judging the Judges: Systematic Evaluation of Bias Mitigation](https://arxiv.org/abs/2604.23178)
- [Fiedler: Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939)
- [PSN-IRT: Lost in Benchmarks?](https://arxiv.org/abs/2505.15055)
- [Quantifying Data Contamination in Psychometric Evaluations](https://arxiv.org/abs/2510.07175)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile the triage evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486) (arXiv, May 2025): 最直接的前置工作。将 MFRM 应用于 10 个 LLM rater 与人类专家的评分比较，验证了 MFRM 在 LLM 评分场景中的适用性。但该工作将 contamination 视为外部问题，不在 MFRM 内建模。本 proposal 声称在此基础上扩展，加入 contamination gating，这一增量是真实的。
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865) (arXiv, March 2026): Judge bias silo 的代表作。通过 round-robin assignment 消除 judge bias，但完全忽略 contamination。本 proposal 将其作为 baseline 之一。
- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173/) (EMNLP 2025): Contamination silo 的代表作。通过 fuzzy inference system 合成 contamination scores 调整 raw accuracy，但忽略 judge effects。
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534) (ICLR 2026): 揭示了 generator-judge relatedness 导致的 preference leakage，仅提出 post-hoc contextual calibration。与本 proposal 关注的 contamination 类型不同（preference leakage vs. benchmark data contamination），但属于同一大问题域。
- [ConStat: Statistical Detection and Quantification of Benchmark Contamination](https://openreview.net/forum?id=ZyVQqK7mcP) (NeurIPS 2024): 提供 black-box contamination 检测（r²=0.94），本 proposal 将其作为外部 exposure indicator 的核心来源。这是一个成熟且经过验证的工具。
- [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939) (Fiedler, arXiv May 2026): 引入 J/ΔJ diagnostics 识别 sign-reversal failure modes，但停留在 classical test theory 框架内，未做 latent trait modeling。与本 proposal 的 psychometric 路线形成互补而非竞争。
- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT](https://arxiv.org/abs/2505.15055) (AAAI 2026): 将 neural 4PL IRT 应用于 benchmark 评估，但不涉及 judge severity 和 contamination 的联合建模。
- [DG-IRT](https://www.researchgate.net/publication/257678777) (Shu, Henson & Luecht, Psychometrika 2013): 原始 DG-IRT 模型，来自教育测量领域的 cheating detection。未被任何人迁移到 LLM 评估场景——这是本 proposal 的核心 cross-domain transfer。
- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175) (arXiv 2025): 量化 psychometric inventories 中的 data contamination，但关注的是 personality/value questionnaires 而非 benchmark evaluation，且不涉及 judge bias。
- 调研总结: 该领域明确存在两个研究 silo——judge bias correction 和 contamination detection——且截至 2026 年 5 月，**确实没有现有工作在单一 psychometric framework 内联合建模 judge severity 和 contamination susceptibility**。Proposal 的 gap claim 经验证成立。IRT/MFRM 在 LLM 评估中的应用正在快速增长，但均未实现 bias+contamination 的联合校准。

【Trivial Alternative 检验】:
最明显的 trivial alternative 是 proposal 自身识别的 **naive two-stage pipeline: CyclicJudge → DCR**（先做 bias correction，再做 contamination adjustment）。这个 baseline 成本低得多（无需构建新的 psychometric model、无需 MCMC、无需三阶段估计），且利用了两个已验证的现有方法。

Proposal 为什么认为 joint modeling 优于 sequential correction？隐含论证是：sequential correction 会 propagate errors——如果 bias correction 阶段不知道 contamination 的存在，它可能把 contamination-inflated performance 误归因到 judge severity 参数上，导致 severity 估计偏差，进而扭曲后续的 contamination adjustment。这个论证在理论上是合理的（psychometrics 文献中 joint > sequential 的一般性论证确实成立），但**增量价值的大小是一个纯粹的经验问题**。如果 Kendall-τ 的改善只有 0.01-0.02，psychometric 复杂度的正当性会被审稿人质疑。

增量价值的关键在于：(1) bias 和 contamination 在实际数据中是否存在显著交互（如果它们近似正交，sequential correction 就够了）；(2) rank-1 decomposition c_n·e_i 是否能捕捉到足够的 contamination variance。

【前提假设检验】:
1. **Rank-1 contamination decomposition 假设**: c_n·e_i 假设 contamination 效果可以分解为 per-model susceptibility × per-item exposure 的乘积。这是一个**强结构性假设**。现实中，不同模型可能对不同类型的 items 有不同的 memorization patterns（例如，code items vs. reasoning items 的 contamination profile 可能因模型训练数据构成而异），这不是 rank-1 能捕捉的。虽然 proposal 引用 AMMI 传统来论证 identifiability，但 identifiability ≠ model adequacy。
2. **External exposure indicators 的有效性假设**: Proposal 高度依赖 ConStat 的 r²=0.94 验证结果。但 ConStat 的验证是在特定条件下进行的，将其结果直接迁移到 G-MFRM 框架中作为 fixed covariates 使用时，是否仍然有效需要验证。特别是 ConStat 的 reference benchmark variants 需要手工构建（GPT-5.5/Claude-assisted rephrasing），这引入了额外的 construct validity 问题。
3. **Chatbot Arena 人类投票作为 ground truth 的假设**: 使用 held-out Chatbot Arena human votes 作为 gold standard 来评估 Kendall-τ 改善，但 Chatbot Arena 本身的 noise 和 bias 是众所周知的（position bias、length bias 等）。用一个有偏的 ground truth 来验证 debiasing 方法，存在循环性风险。
4. **Judge severity 的时间稳定性假设**: MFRM 假设 d_j 是一个稳定的 judge-level 参数，但 LLM judges 的 behavior 可能随 API version 更新、temperature 设置等因素变化。

【3 维度打分】:
1. Novelty: 【中】 — 核心贡献是将 DG-IRT 的 gating mechanism 从教育 cheating detection 迁移到 LLM contamination，并与 MFRM 的 multi-facet 结构融合。经验证，确实没有现有工作做过这个融合（gap claim 成立）。DG-IRT→LLM 的 cross-domain transfer 有创意，LLTM decomposition 的引入是合理的方法论选择。然而，novelty 的本质是**方法论组合/集成**而非**概念性突破**。每个组件（MFRM、DG-IRT gating、ConStat exposure indicators、LLTM decomposition）都是已有的，创新在于"把它们放在一起"。这种 integration novelty 在 EMNLP 审稿中通常被认可但不会被视为 exciting。审稿人可能会说："The contribution is incremental — it combines known components in a natural way."
   
2. Significance: 【中偏强】 — 研究问题毫无疑问是重要的：LLM-as-a-judge 评估已经成为 mainstream practice，且 bias 和 contamination 都是真实且严重的问题。如果 G-MFRM 能显著提升评估质量，其实际影响力会很大。框架产出的可解释性（per-model contamination estimates、per-judge severity calibrations）具有实用价值。但 significance 受限于一个关键不确定性：joint modeling 相对于 naive sequential pipeline 的 marginal improvement 可能不足以改变实际决策。此外，框架的复杂性（三阶段 MCMC、需要构建 reference benchmark variants）可能限制其在实践中的采用。

3. Related Work: 【强】 — 相关工作覆盖异常全面。Proposal 准确地划分了 judge bias silo 和 contamination silo，引用了两个领域的关键论文（CyclicJudge、BiasScope、UDA、Bias-Bounded Evaluation、JudgeBiasBench 在 bias 侧；DCR、ConStat、Preference Leakage、LogProber 在 contamination 侧），以及 IRT-for-LLMs 的主要工作（PSN-IRT、MFRM for LLM raters）。差异化定位清晰且经验证准确。引用的关键论文（arXiv:2505.18486、DG-IRT Psychometrika 2013、ConStat NeurIPS 2024 等）均真实存在且描述准确。唯一的小问题是部分引用的会议/arXiv 论文（如 arXiv:2604.23178, arXiv:2605.06939）非常新，可能尚未被 peer review，但在 arXiv 时代这是可接受的。

【概率估计】: [25% - 38%] 中位 30%

【估计理由】: 
- Novelty 是中等的：gap 是真实的，方法论融合是合理的，但本质是 integration novelty 而非 conceptual breakthrough。核心发现如果是 positive（"joint modeling > sequential correction"），审稿人大概率会说 "I would have guessed this" ——联合建模优于分步修正是 psychometrics 领域的 common wisdom，迁移到 LLM 评估场景不构成 surprising finding。这将 novelty 上限锁定在"中"。
- Significance 是中偏强的：问题重要且实用，但 marginal improvement 的不确定性和框架复杂度限制了上界。
- Related work 是强的：但这主要防止了扣分，不会主动加分。
- **上界主要被 Novelty 限制**：即使实验做得完美、improvement 显著，"combining MFRM + DG-IRT + ConStat" 的 novelty ceiling 也不高。审稿人对 "integration papers" 的天然抵触是主要风险。
- **下界被 Significance 和 Related Work 托住**：问题的重要性和文献定位的清晰性使得即使 novelty 评分偏低，论文也不至于被直接拒绝——有机会通过 solid experiments 争取一些分数。

【主要风险】:
1. **"Integration, not innovation" 质疑**: 审稿人可能认为核心贡献仅是将已有组件（MFRM、DG-IRT、ConStat）组合在一起，每个组件都不是新的，组合方式虽然合理但也是 "the natural thing to do"，缺乏真正的 methodological surprise。
2. **Marginal improvement over naive two-stage pipeline**: 如果 G-MFRM fair scores 相对于 CyclicJudge→DCR 的 Kendall-τ 改善在统计上不显著或实际幅度很小，整个 psychometric 框架的复杂度将无法被 justify。这是最致命的实验风险——idea 层面无法预判，但概率不低。
```

Sources:
- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)
- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173/)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)
- [ConStat: Statistical Detection and Quantification of Benchmark Contamination (NeurIPS 2024)](https://openreview.net/forum?id=ZyVQqK7mcP)
- [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939)
- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT](https://arxiv.org/abs/2505.15055)
- [DG-IRT (Shu, Henson & Luecht, Psychometrika 2013)](https://www.researchgate.net/publication/257678777)
- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175)
- [BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2602.09383)
- [Adaptive Testing for LLM Evaluation: ATLAS](https://arxiv.org/abs/2511.04689)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model** (arXiv:2505.18486, May 2025):
   直接前驱工作。已将 MFRM 应用于 10 个 LLM rater 与人类专家的比较，评估评分一致性和 rater effects。但完全未涉及 contamination 建模——contamination 被视为外部因素。本 proposal 在此基础上增加了 contamination facet，这一扩展是真实增量。

2. **Using Deterministic, Gated IRT Model to Detect Test Cheating due to Item Compromise** (Shu, Henson & Luecht, Psychometrika 2013):
   DG-IRT 的原始论文。提出将观测表现分解为 genuine ability 和 cheating-inflated 两个分布的 gating 机制。该方法在教育测量中有成熟验证，但从未被迁移到 LLM benchmark contamination 场景。跨领域迁移的 novelty claim 成立。

3. **CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation** (arXiv:2603.01865, March 2026):
   提出 round-robin judge 分配策略，通过方差分解将 benchmark score variance 分为 scenario/generation/judge/residual 四个分量。证明在固定 judge-call budget 下，cyclic 分配是最优策略。但完全不考虑 contamination。

4. **DCR: Quantifying Data Contamination in LLMs Evaluation** (EMNLP 2025):
   通过 fuzzy inference 产生统一的 DCR Factor 来调整 raw accuracy，量化 contamination 风险。在 9 个 LLM (0.5B-72B) 上验证，adjusted accuracy 误差在 4% 以内。但完全忽略 judge effects。

5. **ConStat: Performance-Based Contamination Detection in Large Language Models** (NeurIPS 2024):
   通过对比 primary benchmark 和 reference benchmark（rephrased/synthetic variants）的表现差异来检测和量化 contamination。完全 black-box，validated r²=0.94。本 proposal 将其作为 external exposure indicator 的核心来源。

6. **Preference Leakage: A Contamination Problem in LLM-as-a-judge** (ICLR 2026):
   揭示 data generator LLM 和 judge LLM 之间的 relatedness 导致 preference leakage。提出 post-hoc calibration，但未构建统一的 measurement model。

7. **PSN-IRT: Lost in Benchmarks? Rethinking LLM Benchmarking with IRT** (AAAI 2026 Oral):
   用 neural 4PL IRT 框架分析 11 个 benchmark 的 measurement quality，发现广泛的 saturation 和 contamination 问题。但不建模 judge severity，且 contamination 只作为事后诊断，不参与 ability estimation。

8. **UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge** (AAAI 2026):
   通过 neural K-factor 调整 Elo rating，minimizing inter-judge dispersion。纯 judge bias 方向，不考虑 contamination。

9. **Bias and Uncertainty in LLM-as-a-Judge Estimation** (Fiedler, arXiv:2605.06939, May 2026):
   提出 J/delta-J diagnostics，识别 shared-calibration 中的 sign-reversal failure modes。停留在 classical test theory，无 latent trait modeling。

10. **Judging the Judges** (Soumik, arXiv:2604.23178, April 2026):
    实证比较 9 种 debiasing 策略，发现 style bias dominant (0.76–0.92)。但只做经验比较，无 measurement model。

- **调研总结**: LLM-as-a-judge 评估领域在 2025-2026 年经历了快速发展，但确认了 proposal 的核心 claim——judge bias correction 和 contamination detection 形成了两个独立的研究 silo，尚无工作在单一 psychometric 框架内联合建模二者。MFRM 已被应用于 LLM raters（arXiv:2505.18486），DG-IRT 在教育测量中成熟但未被迁移到 LLM 领域。这一 gap 是真实的。

【Trivial Alternative 检验】:

Proposal 自身已识别出最关键的 trivial alternative：**两阶段串行 pipeline（CyclicJudge bias correction → DCR contamination adjustment）**。这一 pipeline 成本更低、实现更简单，且复用两个已验证的独立方法。

增量价值主张在于：两阶段方法中，Stage 1 的 bias 估计可能被 contamination effects 混淆（contaminated items 上某些 model 表现异常好，这会扭曲 judge severity 的估计）；同理 Stage 2 的 contamination 调整未考虑 judge-specific bias。联合模型通过同时估计所有 facets 来避免这种 confounding。

**但这一主张的说服力取决于 confounding 的实际量级。** 如果 judge bias 和 contamination 的交互效应较小（即近似可加），两阶段 pipeline 的损失可能微不足道。Proposal 没有提供理论论证说明为什么这种交互应该是 substantial 的——这是一个未被论证的关键环节。

【前提假设检验】:

1. **"Judge severity 和 contamination susceptibility 之间存在 non-trivial interaction，使得 joint modeling 显著优于 sequential correction"** ——这是整篇论文存在的理由，但完全是 assumed，无理论推导或 pilot data 支撑。如果这个 interaction 很小，整个框架的价值降低为"更优雅的形式化"而非"更好的估计"。

2. **"ConStat 的 exposure indicators 在 MT-Bench / Arena-Hard / WildBench 上仍然有效"** ——ConStat 的 r²=0.94 是在其原始验证设置下得到的。将其作为 fixed covariate 输入 Stage 3，前提是这些 indicators 在新 benchmark 上保持高质量。如果质量下降，整个 Stage 2 → Stage 3 的 pipeline 都会受损。

3. **"Rank-1 decomposition (c_n · e_i) 足以捕捉 contamination pattern"** ——真实 contamination 可能具有更复杂的 model-item 交互结构（例如某些 model 只在特定类型的 items 上受 contamination 影响）。Rank-1 是一个强假设，虽然提高了 identifiability，但可能牺牲了 model fit。

4. **"Chatbot Arena human votes 是 ground truth"** ——这是验证标准的选择，但 Chatbot Arena 自身存在 self-selection bias、demographic bias 等已知问题。将其作为 gold standard 需要论证。

【3 维度打分】:

1. **Novelty: 中（偏强）**
   
   核心 novelty 有两层：(a) DG-IRT gating mechanism 从教育测量到 LLM evaluation 的跨领域迁移；(b) 在单一 MFRM 框架内联合建模 judge severity 和 contamination susceptibility。调研确认这一 gap 是真实的——arXiv:2505.18486 已将 MFRM 用于 LLM raters 但无 contamination，DG-IRT (Shu 2013) 处理 cheating 但未涉及 multi-judge 场景，CyclicJudge/DCR/Preference Leakage 分别只处理一个 silo。
   
   但限制 novelty 评分的是：这本质上是一个 **组合式创新**——将三个已有工具（MFRM + DG-IRT gating + ConStat indicators）按直觉拼接。对一个同时了解 psychometrics 和 LLM evaluation 的研究者来说，一旦识别出两个 silo 的 gap，这个组合方案是相当 natural 的下一步。hierarchical parameterization (c_n · e_i) 是标准的 rank-1 AMMI 分解，three-stage estimation 是常见的 two-step 方法的自然扩展。没有 "surprising insight"。

2. **Significance: 中**
   
   研究问题本身很重要——LLM-as-a-judge evaluation 是 NLP 领域的核心基础设施，judge bias 和 contamination 是两个被广泛认知的痛点。CyclicJudge (2603.01865)、Fiedler (2605.06939)、Soumik (2604.23178) 等近期密集出现的工作证明了社区对此的关注。
   
   但 significance 受限于两个因素：(a) **实际受众窄**——需要运行三阶段 MCMC pipeline + ConStat reference variants 构建的方法，门槛远高于 CyclicJudge 的简单 round-robin。大多数 practitioner 不会采用如此复杂的方案；(b) **improvement 可能 marginal**——如果 joint model 只比 two-stage pipeline 高 2-3% Kendall-τ，审稿人可能认为不足以 justify psychometric machinery 的复杂性。

3. **Related Work: 强**
   
   Proposal 对 literature 的覆盖非常全面和准确。两个 silo 的划分清晰，每篇论文的描述经验证基本准确（CyclicJudge 确实是 round-robin + variance decomposition，DCR 确实是 fuzzy inference + DCR Factor，ConStat 确实是 black-box reference comparison，Preference Leakage 确实发表于 ICLR 2026）。DG-IRT (Psychometrika 2013) 作为 inspiration 的引用也是准确的。Fiedler (2605.06939) 和 Soumik (2604.23178) 两篇 May/April 2026 的最新工作也被纳入，显示出对领域的持续跟踪。差异化定位（"no existing work jointly models both facets"）在调研中得到确认。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】:
- Related Work 维度的强表现确保了 paper 不会因 positioning 问题被拒，但它不提升 idea 的内核质量
- Novelty 处于中（偏强）水平：gap 真实、组合有原创性，但本质是 "natural next step" 式的组合创新，缺乏 surprising insight。审稿人看到 positive results 后可能反应为 "makes sense, I would have guessed joint modeling helps"，而非 "surprising, didn't expect this"
- Significance 是限制上界的主要因素：practical complexity 高（三阶段 MCMC + ConStat 变体构建）、受众窄、improvement 可能 marginal。NLP 领域对 psychometric measurement 的接受度有限，可能被认为 "over-engineered for a problem with simpler solutions"
- 概率未能进入 35-45% 区间，因为核心 finding 即使 positive 也不够 surprising，且 trivial alternative (两阶段 pipeline) 的威胁未被理论性地排除

【主要风险】:
1. **Marginal improvement over naive two-stage pipeline**: 如果 G-MFRM fair scores 相对于 CyclicJudge → DCR 的 Kendall-τ 提升不显著（<3-5%），审稿人会认为 psychometric 复杂性不 justified，可能建议 reject with "the added machinery doesn't buy enough"
2. **"Engineering contribution, not scientific insight" 的质疑**: 三个已有组件的拼接缺乏深层 insight 作为支撑——proposal 未论证为什么 judge bias 和 contamination 的交互效应应该是 substantial 的，这使得整个 framework 的必要性悬而未决。审稿人可能给出 "well-executed but incremental" 的评价
```

Sources:
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)
- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173/)
- [ConStat: Performance-Based Contamination Detection in Large Language Models](https://arxiv.org/abs/2405.16281)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)
- [PSN-IRT: Lost in Benchmarks? Rethinking LLM Benchmarking with IRT](https://arxiv.org/abs/2505.15055)
- [UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge](https://arxiv.org/abs/2508.09724)
- [Using Deterministic, Gated IRT Model to Detect Test Cheating](https://www.cambridge.org/core/journals/psychometrika/article/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E)
- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)
- [Bias and Uncertainty in LLM-as-a-Judge Estimation](https://arxiv.org/abs/2605.06939)
- [Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)
- [BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge](https://arxiv.org/abs/2602.09383)


【原始 proposal（允许参考但不是主要依据）】:
# Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation

## Description
We propose the Gated Many-Facet Rasch Model (G-MFRM), which extends the standard MFRM from educational measurement with a DG-IRT-inspired contamination gating mechanism to jointly calibrate model ability, item difficulty, judge severity, and contamination susceptibility within a single psychometric framework. The critical methodological advance over the original proposal is a hierarchical contamination parameterization: instead of an overparameterized per-(model,item) contamination term c_nk (N×I free parameters, unidentifiable), we decompose contamination into per-model susceptibility c_n modulated by per-item exposure indicators e_i, giving c_n · e_i (N+I parameters). This follows the LLTM (Fischer 1973) design-matrix tradition and the AMMI multiplicative interaction decomposition, both with established identifiability guarantees. Crucially, exposure indicators e_i are estimated externally via ConStat reference benchmark comparison (fully black-box, validated r²=0.94), temporal pre/post-cutoff signals, and LogProber Safe Scores (gray-box) — resolving the circularity of using model-internal residuals to identify contamination. A three-stage estimation strategy ensures identification: (1) standard 3-facet MFRM producing ability, difficulty, and severity estimates plus person-fit diagnostics; (2) external exposure estimation from ConStat and temporal proxies; (3) joint Gated MFRM with fixed exposure indicators and informative priors from Stages 1–2, implemented via Bayesian MCMC in NumPyro. The n-gram overlap signal is dropped for proprietary models (training data undisclosed) and retained only as supplementary validation for open-weight models. Validation spans MT-Bench, Arena-Hard, and WildBench using 8+ LLM judges (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick). We demonstrate that G-MFRM fair scores achieve higher Kendall-τ rank correlation with held-out Chatbot Arena human votes than raw multi-judge averages, CyclicJudge bias-only correction, DCR contamination-only adjustment, Preference Leakage calibration, and a naive two-stage pipeline (CyclicJudge → DCR). Additional analyses include exposure indicator ablation, judge count sensitivity, facet fit statistics, person-fit validation of contamination estimates, and robustness to adversarial contamination (per ICLR 2026 fragility findings). The unified framework yields interpretable per-model contamination estimates, per-judge severity calibrations, and fair ability rankings — bridging the gap between the judge bias correction and contamination detection research silos.

## Core Problem
Can a hierarchical psychometric measurement model jointly estimate model ability, item difficulty, judge severity, and contamination susceptibility — with the contamination facet decomposed into identifiable per-model and per-item components anchored by external exposure proxies — to produce bias-and-contamination-corrected evaluation scores that outperform both siloed corrections and naive multi-judge averaging?

## Opportunity
The LLM-as-a-judge evaluation literature has bifurcated into two silos: (1) judge bias correction methods (CyclicJudge round-robin, Bias-Bounded Evaluation, Soumik's 9-strategy comparison, UDA neural calibration, Fiedler's classical test theory diagnostics) and (2) contamination detection/adjustment methods (DCR Factor, ConStat, Preference Leakage calibration, person-fit screening). No existing work — including all arXiv submissions through May 2026 and ICLR/EMNLP 2026 proceedings — jointly models judge severity and contamination susceptibility within a single calibration framework. The Many-Facet Rasch Model (MFRM) from educational testing naturally accommodates multiple facets in a unified calibration. Recent work has applied MFRM to LLM raters (arXiv:2505.18486) but treats contamination as external. Critically, the Deterministic Gated IRT (DG-IRT) model from psychometric cheating detection (Shu, Henson & Luecht, Psychometrika 2013) provides the missing link: a principled gating mechanism that decomposes observed performance into genuine ability and contamination-inflated components. By combining MFRM's multi-facet structure with DG-IRT's gating logic and externally-anchored exposure indicators from ConStat, we obtain a unified, identifiable model that bridges the gap between these two research silos.

## Landscape
**Judge bias silo:** CyclicJudge (March 2026) eliminates judge bias via round-robin assignment but ignores contamination. IRT-GRM for judge reliability (Feb 2026) diagnoses judge consistency without modeling contamination. 'Judging the Judges' (Soumik, arXiv:2604.23178, April 2026) empirically compares 9 debiasing strategies across 5 judges, finding style bias dominant (0.76–0.92) but provides no measurement model explaining why strategies work. 'Bias and Uncertainty in LLM-as-a-Judge Estimation' (Fiedler, arXiv:2605.06939, May 2026) introduces formal J/delta-J diagnostics and identifies sign-reversal failure modes in shared-calibration comparisons, but stays within classical test theory without latent trait modeling. BiasScope (ICLR 2026) automates bias discovery post-hoc. Bias-Bounded Evaluation (March 2026) provides formal guarantees retaining 61–99% ranking correlation. JudgeBiasBench (March 2026) defines a taxonomy of 12 bias types across 4 dimensions. UDA (AAAI 2026) uses neural K-factor adjustment to reduce inter-judge standard deviation by 63.4%. **Contamination silo:** DCR Factor (EMNLP 2025) adjusts accuracy for contamination via fuzzy inference but ignores judge effects. Preference Leakage (ICLR 2026) quantifies generator-judge relatedness bias but proposes only post-hoc calibration. ConStat (NeurIPS 2024) computes contamination effects via reference benchmark comparison (r²=0.94 with true effects) — fully black-box. LogProber (2024) estimates per-item Safe Scores from token log-probabilities. 'On The Fragility of Benchmark Contamination Detection in Reasoning Models' (ICLR 2026) shows RL post-training obscures contamination signals, motivating multi-indicator approaches. **IRT for LLMs (no judge + contamination unification):** PSN-IRT (AAAI 2026) applies neural 4PL IRT to benchmark evaluation. MFRM has been applied to compare 10 LLM raters with human experts (May 2025) and to ChatGPT-4 essay scoring (RMAL 2024). **Gap:** No existing work jointly models judge severity and contamination susceptibility within a single psychometric calibration framework, nor has anyone adapted DG-IRT's gating mechanism from educational cheating detection to LLM benchmark contamination.

## Approach
We propose a Gated Many-Facet Rasch Model (G-MFRM) that extends the standard MFRM with a DG-IRT-inspired contamination gating mechanism, using a three-stage estimation strategy that ensures identifiability.

**Model formulation.** The core log-odds model is:

  logit(P_nij) = θ_n − b_i − d_j + c_n · e_i

where θ_n is model ability, b_i is item difficulty, d_j is judge severity, c_n is per-model contamination susceptibility, and e_i is per-item exposure level. The contamination term c_n · e_i replaces the overparameterized per-(model,item) c_nk from the original proposal: instead of N×I free parameters, this hierarchical decomposition requires only N + I parameters (or just N when e_i is externally anchored). This follows the LLTM (Linear Logistic Test Model, Fischer 1973) tradition of decomposing item parameters via a known or estimable design matrix, and is a rank-1 special case of the AMMI (Additive Main Effects and Multiplicative Interaction) decomposition, both with well-established identifiability guarantees.

The DG-IRT gating interpretation: when e_i ≈ 0 (unexposed item), the model reduces to the standard 3-facet MFRM measuring genuine ability; when e_i > 0, performance is inflated by c_n · e_i, where c_n captures how much each model benefits from data leakage. This directly mirrors DG-IRT's decomposition of observed performance into genuine and cheating-inflated distributions.

**Three-stage estimation (resolving circularity).**

*Stage 1 — Standard 3-facet MFRM:* Fit θ_n, b_i, d_j via Bayesian MCMC (NumPyro on GPU), ignoring contamination. This produces uncontaminated ability estimates and, critically, standardized residuals r_ni and person-fit statistics (lz, EMRi) per model.

*Stage 2 — External exposure estimation:* Estimate e_i from external proxies that are independent of the MFRM fit, resolving the circularity the reviewer identified:
  (a) ConStat delta scores: compare model performance on original benchmark items vs. rephrased/synthetic reference variants (fully black-box, validated r²=0.94 with true contamination effects);
  (b) Temporal signals: performance gaps on items with pre-cutoff vs. post-cutoff variants (available for benchmarks with versioned items);
  (c) LogProber Safe Scores: per-item memorization indicators from token log-probability analysis (gray-box; for models exposing logprobs: GPT-5.5, DeepSeek-V4, Qwen3, Llama 4).
  These indicators are combined via a weighted composite (weights tuned on a held-out validation split) to produce ê_i. Person-fit statistics from Stage 1 serve as validation — models with high contamination should exhibit difficulty-insensitive response patterns (high Guttman errors, low lz) — but are NOT used to estimate e_i, avoiding circularity.

*Stage 3 — Joint Gated MFRM:* Refit the full 4-facet model with ê_i as fixed (observed) covariates and c_n as latent parameters, using Stage 1 estimates as informative priors. Identifiability constraints: sum(c_n) = 0 (centered contamination susceptibility) and ê_i scale fixed from Stage 2. This yields contamination-corrected 'fair scores' θ̂_n — model ability estimates purged of both judge bias (via d_j) and contamination inflation (via c_n · ê_i).

**N-gram overlap dropped for proprietary models.** Following the reviewer's feedback, we remove n-gram overlap as a contamination signal since OpenAI, Anthropic, and Google do not disclose training data. ConStat and temporal signals are fully black-box; LogProber requires only logprob access. For open-weight models with documented training data (DeepSeek-V4, Kimi K2.6, Qwen3, Llama 4), n-gram overlap can serve as supplementary validation of ê_i estimates.

**Validation.** Experiments span MT-Bench, Arena-Hard, and WildBench using 8+ LLM judges: proprietary (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6) and open-weight (DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick). We construct reference benchmark variants for ConStat by GPT-5.5/Claude-assisted rephrasing (validated by human equivalence checking). We evaluate by demonstrating that G-MFRM fair scores θ̂_n achieve higher Kendall-τ rank correlation with held-out Chatbot Arena human votes than five baselines: (1) raw multi-judge averages, (2) CyclicJudge bias-only correction, (3) DCR Factor contamination-only adjustment, (4) Preference Leakage post-hoc calibration, and (5) a naive two-stage pipeline (CyclicJudge bias correction → DCR contamination adjustment) — the 'simpler baseline' that reviewers would demand to justify the psychometric overhead. Additional analyses include: (a) ablation of each exposure indicator's contribution to ê_i; (b) sensitivity analysis varying the number of judges (2, 4, 6, 8+); (c) facet fit statistics (infit/outfit MNSQ) to validate measurement quality; (d) comparison of Stage 1 person-fit flagging (lz, EMRi) against Stage 3 contamination estimates c_n as a validation of construct coherence; (e) robustness check against adversarial contamination following Wang et al. (ICLR 2026) fragility findings.

## Resource Estimate
{'manual': {'gpu_hours': '180–250 (open-source judge inference via vLLM ~130h on A100-80GB; ConStat reference variant generation + evaluation ~30h; Bayesian MCMC fitting ~15h; ablations and sensitivity analysis ~50h)', 'timeline': '10–12 weeks (G-MFRM implementation + ConStat integration 3w, reference benchmark variant construction 2w, multi-judge data collection 3w, experiments and analysis 2w, paper writing 2w)', 'estimated_gpu_cost': '$450–625 (A100 spot at ~$2.50/hr) + ~$900 proprietary judge API calls (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6)'}, 'human_in_loop': {'gpu_hours': '180–250', 'timeline': '7–9 weeks (Claude accelerates G-MFRM implementation, ConStat integration, experiment scripting, and drafting)', 'claude_api_cost': '$100–150', 'estimated_gpu_cost': '$450–625 + ~$900 proprietary judge API calls'}, 'auto_research': {'gpu_hours': '180–250', 'timeline': '5–7 weeks', 'claude_api_cost': '$250–400 (end-to-end code generation, three-stage estimation pipeline, hyperparameter search, convergence diagnostics, paper writing)', 'estimated_gpu_cost': '$450–625 + ~$900 proprietary judge API calls', 'speed_bottleneck': 'Proprietary judge API rate limits (GPT-5.5/Claude batch quotas); ConStat reference variant quality validation; sequential three-stage MCMC convergence requiring iterative checks'}}

## Inspired By
Cross-domain transfer of DG-IRT (Shu et al., Psychometrika 2013) gating mechanism from educational cheating detection to LLM contamination; MFRM multi-facet calibration for judge bias; LLTM (Fischer 1973) design-matrix decomposition for identifiable contamination parameterization; ConStat (NeurIPS 2024) external exposure indicators; combination of CyclicJudge judge modeling + ConStat contamination quantification + IRT measurement backbone.

## Target Venues
- AAAI 2027 (full paper: July 28, 2026)
- ACL 2027 (ARR submission: August 3, 2026)
- EACL 2027 (ARR submission: August 3, 2026)
- NAACL 2027 (ARR submission: October 15, 2026)

## Key References
- Using Deterministic, Gated IRT Model to Detect Test Cheating due to Item Compromise (Shu, Henson & Luecht, Psychometrika 2013)
- Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model (arXiv 2025)
- ConStat: Statistical Detection and Quantification of Benchmark Contamination (NeurIPS 2024)
- CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation (arXiv 2026)
- Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory (arXiv 2026)
- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)
- DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)
- Bias and Uncertainty in LLM-as-a-Judge Estimation (Fiedler, arXiv:2605.06939, May 2026)
- Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines (Soumik, arXiv:2604.23178, April 2026)
- On The Fragility of Benchmark Contamination Detection in Reasoning Models (ICLR 2026)
- BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation (ICLR 2026)
- LogProber: Detecting Data Contamination via Token Log-Probability Analysis (arXiv 2024)
- An application of many-facet Rasch measurement to evaluate automated essay scoring: A case of ChatGPT-4.0 (RMAL 2024)
- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2026)
- JudgeBiasBench: Evaluating and Mitigating Bias in LLM-Based Judges (arXiv 2026)
- The Linear Logistic Test Model (Fischer, Psychometrika 1973)
- Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT (AAAI 2026)
- Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (NeurIPS 2023)
- py-irt: A Scalable Item Response Theory Library for Python (INFORMS JoC 2023)
- UDA: Unsupervised Debiasing Alignment for LLM Judges (AAAI 2026)
- Evaluating Rater Effects of Large Language Models in Automated Essay Scoring (Educational Measurement 2026)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a6fa40d9-2cc9-4fa1-9c34-597b05915d22",
  "type": "user",
  "uuid": "25486771-f18d-410d-ad0c-a56cd169b6b4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:34:51.801Z_

```json
{
  "parentUuid": "25486771-f18d-410d-ad0c-a56cd169b6b4",
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
  "uuid": "21ab0b47-4fc1-41d2-bc91-8cb153357aa6",
  "timestamp": "2026-05-20T04:34:51.801Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:34:51.801Z_

```json
{
  "parentUuid": "21ab0b47-4fc1-41d2-bc91-8cb153357aa6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1500008b-2dac-4863-be8a-cbf092349f33",
  "timestamp": "2026-05-20T04:34:51.801Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to conduct a thorough evaluatio…",
  "leafUuid": "1500008b-2dac-4863-be8a-cbf092349f33",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate joint judge bias and contamination correction framework",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:35:21.488Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews carefully to produce the Meta Judge synthesis.

**Review 1:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [28% - 38%] 中位 33%

**Review 2:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [25% - 38%] 中位 30%


**Review 3:**
- Novelty: 中（偏强）
- Significance: 中
- Related Work: 强
- Probability: [25% - 35%] 中位 30%

Now I'm calculating the aggregate statistics from the three median probabilities. The medians are 33%, 30%, and 30%, which gives me a mean of 31%. Computing the variance across these three values yields approximately 2, so the standard deviation comes out to around 1.41%.

Since I'm working with all three complete reviews rather than a sample, population standard deviation is the right choice here. With a standard deviation under 3%, the reviewers show strong consistency in their assessments.

Looking at where the reviewers converge, all three agree on novelty being 中 — the paper's core contribution is essentially combining existing components like MFRM, DG-IRT, and ConStat into an integrated approach. While each piece already exists, the combination represents a natural progression. The related work section also gets universal agreement for being comprehensive and well-positioned. All three reviewers also flag the same concern about a naive two-stage pipeline as a potential alternative.

There's also consensus around several structural risks: the rank-1 decomposition assumption in the c_n · e_i formulation could be too restrictive, ConStat's strong performance on its original benchmarks may not transfer to new ones, and the reliance on Chatbot Arena as ground truth warrants scrutiny. The "integration not innovation" framing emerges as a shared concern across all reviews.

Where they diverge is on how significant these issues are.  R1 and R2 rate the work as 中偏强 while R3 stays at 中. R3 also emphasizes practical adoption barriers more heavily—the narrow audience and implementation complexity. R1 uniquely flags the "Dual Optimal" paper as missing related work and raises questions about whether the education-to-LLM analogy holds up when comparing binary cheating to gradient contamination. R1 and R2 both worry about temporal stability of judge severity across API versions, whereas R3 doesn't explicitly mention this.

The consistency is quite high—standard deviation of 1.41% is well below the 3% threshold. All three reviewers converge on novelty being 中, significance ranging from 中 to 中偏强, and related work being 中偏强 to 强. The probability estimates cluster tightly around 30-33%.

Looking at the medians: the three estimates are 30%, 30%, and 33%, giving a median of 30%. The lower bounds (28%, 25%, 25%) median to 25%, and upper bounds (38%, 38%, 35%) median to 38%. Given this tight clustering, I should narrow the interval and anchor to the consensus. The final range is [26%-36%] with a median of 31%.

Now I'm moving to assess the implementation feasibility based on the proposal's resource estimates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1500008b-2dac-4863-be8a-cbf092349f33",
  "isSidechain": false,
  "requestId": "req_011CbDCT8CddnEyxfV3i99mh",
  "type": "assistant",
  "uuid": "f02a5a38-bd98-4475-8fe2-d7327e497f27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRRrWwhNZDVauNQyXu13he",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18406,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18406,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3165,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 18406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18406
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

_source line 9 · 2026-05-20T04:36:09.894Z_

【阶段】: Meta Judge
【三次中位】: [33%, 30%, 30%]  std=1.4%
【共识维度】:
- **Novelty = 中**（3/3）：核心贡献是已有组件（MFRM + DG-IRT gating + ConStat indicators）的组合式创新，gap 经调研确认真实存在，但组合方案被一致认为是 "natural next step"，缺乏 surprising insight。
- **Related Work = 强**（3/3）：覆盖全面，引用真实准确，两个 silo 的划分清晰，差异化定位经得起检验。
- **Trivial Alternative 威胁 = 中-高**（3/3）：naive two-stage pipeline（CyclicJudge → DCR）是最直接的威胁，joint modeling 的增量价值是未经验证的纯粹经验问题，若改善幅度微小（Kendall-τ Δ<0.02），框架复杂度将无法 justify。
- **Rank-1 分解假设风险 = 中**（3/3）：c_n · e_i 的 rank-1 AMMI 分解可能过于简化，真实 contamination 模式可能具有 model-item 类型交互结构。
- **ConStat 迁移性风险 = 中**（3/3）：ConStat 的 r²=0.94 是在原始验证条件下得到的，迁移到 MT-Bench/Arena-Hard/WildBench 需额外验证。
- **"Integration not innovation" 拒稿风险 = 高**（3/3）：审稿人可能认为贡献仅是 "well-executed engineering" 而非 "conceptual advance"。

【异常维度】:
- **"Dual Optimal" (arXiv:2604.00979) 遗漏**：仅 R1 提及，该论文同样使用 MFRM 进行 LLM judge 标定，是一个值得补充的近期竞争者，但不改变 gap 的成立性。降权处理——需在迭代中验证是否确实构成威胁。
- **Significance 分歧**：R1/R2 给"中偏强"，R3 给"中"（R3 更强调实际受众窄和采用门槛高）。分歧不大，综合为"中"。
- **教育→LLM 类比有效性**（二元 cheating vs. 梯度 contamination）：R1 单独作为重要前提假设提出，R2/R3 仅间接涉及。该担忧有道理但不改变整体判断。

【最终概率】: [26% - 36%] 中位 31%
【一致性】: 高
【综合理由】:
三位审稿人的评估高度一致（std=1.4%），在所有核心维度上形成了清晰共识：

1. **Novelty 天花板锁定在"中"**：三位审稿人一致认为，虽然 gap 是真实的（这一点经独立调研反复确认），但 DG-IRT + MFRM + ConStat 的组合对于同时了解 psychometrics 和 LLM evaluation 的研究者来说是 "the natural thing to do"。正面实验结果不会产生 surprise——审稿人更可能说 "makes sense" 而非 "didn't expect this"。这将 idea 天花板锁定在约 35-38%，无论实验做得多完美。

2. **Significance 被复杂度和 marginal improvement 不确定性压制**：R1/R2 给中偏强，R3 给中。综合考虑：问题本身确实重要（LLM-as-a-judge 是 NLP 核心基础设施），但三阶段 MCMC + ConStat 变体构建的实际门槛，以及 joint modeling 相对于 naive two-stage pipeline 的 marginal improvement 不确定性，共同限制了 significance。采用 R3 的更保守评估（宁缺毋滥原则）。

3. **Related Work 的强表现是防守性的**：三位一致给强，确保论文不会因 positioning 问题被拒，但不主动提升 novelty 得分。

4. **概率定位**：三个中位（33, 30, 30）的中位数是 30%。高一致性下取中位附近，考虑到 R1 稍高（33%）但 R2/R3 的更保守判断有更强的论证支撑（特别是 significance 的复杂度/受众限制论证），最终中位定在 31%。下界 26%（若 trivial alternative 实验结果 marginal improvement 微小 + 审稿人对 integration novelty 有天然抵触）。上界 36%（若 joint modeling 改善显著 + 审稿人认可 cross-domain transfer 的创意 + 实验执行完美）。

【建议】: 边缘（偏下）

当前 proposal 的 idea 质量天花板约 35-38%，由 Novelty 的组合性质限定。实验设计相对完整但三大未验证假设（rank-1 分解、ConStat 迁移性、joint vs. sequential 的增量价值）构成显著下行风险。进入迭代有提升空间，但需要在 idea framing 上找到更锐利的 novelty angle（而非仅仅加实验），否则概率很难突破 35%。

【实施评估】:
  - 计算资源: 180-250 GPU hours（A100-80GB），其中开源 judge 推理 ~130h（vLLM），ConStat 变体生成+评估 ~30h，Bayesian MCMC ~15h，消融实验 ~50h。GPU 成本 $450-625（A100 spot）+ ~$900 proprietary judge API 调用（GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6）
  - 数据需求: MT-Bench、Arena-Hard、WildBench（均公开可得）；需构建 reference benchmark variants（GPT-5.5/Claude 辅助改写）+ Chatbot Arena 人类投票数据（公开）
  - 人工介入: ConStat reference variant 的人工等价性验证（moderate 工作量，约 1-2 周）；无需大规模人工标注
  - 训练需求: 无模型训练需求（仅做推理和 Bayesian MCMC 拟合），复杂度主要在统计估计而非深度学习训练
  - 新 Benchmark: 不需要构建全新 benchmark，但需要为现有 benchmark 构建 rephrased/synthetic reference variants（ConStat 需要）
  - 预估周期: 7-12 周（取决于自动化程度），主要瓶颈为 proprietary judge API rate limits 和 ConStat 变体质量验证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f02a5a38-bd98-4475-8fe2-d7327e497f27",
  "isSidechain": false,
  "requestId": "req_011CbDCT8CddnEyxfV3i99mh",
  "type": "assistant",
  "uuid": "9715f4fe-2d72-4fc5-95bc-b8da0172e562",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRRrWwhNZDVauNQyXu13he",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18406,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18406,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3165,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 18406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18406
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to conduct a thorough evaluatio…",
  "leafUuid": "9715f4fe-2d72-4fc5-95bc-b8da0172e562",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate joint judge bias and contamination correction framework",
  "sessionId": "efb08a85-fb55-44d5-bd79-417b5e5200dd"
}
```

---
