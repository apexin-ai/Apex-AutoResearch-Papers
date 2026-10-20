# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/fc14db4d-f1a3-4832-8b47-fcec9b6e5c52.jsonl`
- **Structured JSON:** [`a2defdecd64c8c2aa155.json`](../../sessions/a2/a2defdecd64c8c2aa155.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T13:21:09.921Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T13:21:09.921Z",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have comprehensive research data. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531) (Barkallah et al., arXiv May 2026): 本 proposal 的直接基础。提出 PF 格式——将证明分解为自包含模块，每个模块有显式前提、结论和自然语言证明。PF + Block Verification 在竞赛级和研究级基准上 Pareto-dominates LLM-as-judge，但在 ArxivMathGradingBench 上仍有 ~50% 的错误未被检出。本 proposal 本质上是 Barkallah et al. 的直接后续/扩展工作。\n\n2. [Safe: Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/) (Liu et al., ACL 2025): 首个使用 Lean 4 对 LLM 生成内容进行逐步形式化验证的框架，成功率 ~80% 但成本 4-8x。本 proposal 直接以此为\"可靠但昂贵\"的对标。\n\n3. [miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108) (NeurIPS 2025): 揭示端到端 autoformalization pipeline 的真实天花板——人工评审发现 autoformalization 准确率仅 66%（非 LLM 评估的 97%），combined with 70.8% proof search success → ~35% end-to-end。这是 proposal 论证 whole-proof autoformalization 不可行的核心依据。\n\n4. [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047) (Ganguly et al., NeurIPS 2025): **最直接的竞争工作**。使用 PCFG-based 不确定性进行选择性 SMT 形式化验证，error reduction 14-100%。Proposal 声称在三个维度上区分（不确定性来源、路由目标异质性、结构关键性），这一区分是成立的但属于同一研究方向的 variant。\n\n5. [HERMES](https://arxiv.org/abs/2511.18760) (Ospanov et al., ICML 2026): 在证明 **生成** 过程中交叉使用非形式推理和 Lean 4 验证，67% accuracy improvement，80% fewer FLOPs。但针对生成而非验证，且使用统一形式化而非选择性路由。\n\n6. [ThinkPRM](https://arxiv.org/abs/2504.16828) (2025): 数据高效的 verbalized PRM，仅用 PRM800K 1% 的标注即超越判别式 PRM。被列为 baseline。\n\n7. [Goedel-Prover-V2](https://arxiv.org/abs/2508.03613) (ICLR 2026): SOTA 定理证明器，miniF2F 88.1% pass@32。本 proposal 计划用其做 Tier 2 的 proof search。\n\n8. [StepFun-Formalizer-32B](https://ojs.aaai.org/index.php/AAAI/article/view/40691) (AAAI 2026): SOTA autoformalization 模型，FormalMATH-Lite BEq@1 40.5%。本 proposal 计划用其做 Tier 2 的 autoformalization。**注意：这篇已发表在 AAAI 2026，proposal 对其能力的描述准确。**\n\n9. [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450) (arXiv 2026): 发现通过 specialized prompt ensemble 可以使小模型在证明验证上逼近 frontier 模型（accuracy gap ~10%，但 consistency gap ~25%）。Proposal 正确地将其列为提升 LLM-only 验证上限的工作。\n\n10. [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940) (2024): 已证明 step-level formalization 比 whole-proof formalization 更 tractable。**这对 proposal 的 Claim 1 构成直接的 prior art 威胁——\"分块 formalization 比整体 formalization 更容易\" 这一洞见已有前人工作支撑。**\n\n11. [VERGE](https://arxiv.org/abs/2601.20055) (Singh et al., 2026): 使用 SMT solver 对 LLM 输出进行形式化验证和 semantic routing，但针对一阶逻辑 claims 而非数学证明块。\n\n- **调研总结**: 数学证明验证领域正处于\"LLM-cheap-unreliable vs. formal-expensive-reliable\"的权衡前沿。Ganguly et al. (NeurIPS 2025) 已开创了\"选择性形式化验证\"范式，HERMES (ICML 2026) 已展示了形式+非形式交叉的价值，Process-Driven Autoformalization (2024) 已证明 step-level formalization 更 tractable。本 proposal 处于这些方向的自然交汇处——是一个合理的\"下一步\"，但并非一个全新方向。\n\n【Trivial Alternative 检验】:\n\n存在多个 trivial alternative 威胁：\n\n(1) **PF + BV ensemble (N=5) alone**: Proposal 自身列为 baseline。如果 ensemble 已经能通过多数投票显著减少 false negative，那么增加 Tier 2 formal verification 的增量收益可能有限。关键问题是：BV ensemble 的 error detection recall 相对于单次 BV 能提升多少？如果 ensemble 已经从 ~50% 未检出降到 ~30%，那剩余的 ~20% gap 是否值得建设整个 Tier 2 pipeline？\n\n(2) **Simple heuristic routing**: 用 block step count + cited theorem count + BV confidence < threshold 作为路由信号——无需 ensemble disagreement 或 calibration。Proposal 承诺用 ablation #2 对比，这是正确的，但问题是：如果 heuristic-only routing 达到 dual-signal 的 80% 效果且成本低得多，核心 contribution 就被削弱。\n\n(3) **直接使用 \"Do We Need Frontier Models...\" (2604.02450) 的 specialized prompt ensemble**: 如果 prompt ensemble 能将 LLM-only 验证准确率提升 ~9%，这可能已经覆盖了 Tier 2 formal verification 能捕获的大部分增量错误。\n\n**增量价值在哪**: 如果 PF block-level autoformalization 成功率确实显著高于 raw NL formalization（Phase 0 验证），且 dual-signal routing 确实能精准定位\"confident-but-wrong\" blocks（ablation #7 验证），则增量价值成立。但这两个\"如果\"都未经验证。\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的关键假设：\n\n(1) **\"PF block 的自包含结构使 autoformalization 从根本上更 tractable\"**: 虽然 Process-Driven Autoformalization (2024) 支持 step-level > whole-proof，但 PF block ≠ step。PF block 可能包含多个推理步骤，其复杂度可能远超 miniF2F 级别的 single step。对于研究级证明中的 PF block，autoformalization 成功率可能仍然很低。**Phase 0 pilot 正是为了验证这一假设，说明作者意识到了这个风险——这是好的设计。**\n\n(2) **\"BV ensemble disagreement 是 block 正确性不确定性的可靠代理\"**: Ensemble disagreement 在分类任务上的有效性有大量文献支持，但在 **自然语言证明验证** 这一特殊任务上，disagreement 可能更多地反映 prompt sensitivity 而非真实不确定性。如果 5 个 BV pass 对同一错误 block 都 confident-wrong（LLM overconfidence 的已知问题），ensemble disagreement 就无法检测到。Proposal 声称 dependency criticality 可以缓解这一问题，但这假定错误集中在高 fan-out blocks——这一假设没有实证支撑。\n\n(3) **\"10-20% routing 即可捕获 LLM 漏检的大多数错误\"**: 这隐含假设 LLM 漏检的错误与 BV uncertainty / structural criticality 高度相关。但如果 LLM 漏检的错误恰恰是那些\"看起来正确、结构简单但推理微妙\"的 blocks——ensemble 可能也对它们高 confidence，dependency criticality 也不高——则 routing 完全失效。\n\n(4) **\"near-formal reliability\"的表述需要谨慎定义**: 如果 Tier 2 的 autoformalization+proof search end-to-end 成功率只有 50%（这已经比 whole-proof 的 35% 好很多），那被 route 到 Tier 2 的 blocks 中有一半的形式化验证会失败，需要 fallback 到 LLM 判断，这部分的 reliability 并不比 Tier 1 更好。\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — \n   - 核心洞见 \"分块更易 formalize\" 已有 Process-Driven Autoformalization (2024) 铺路，虽然本 proposal 用的是 PF block 而非 generic step，但方向性洞见不新。\n   - \"选择性形式化验证\" 的 paradigm 已被 Ganguly et al. (NeurIPS 2025) 建立。Proposal 在三个维度上的差异化（不确定性来源、cross-paradigm routing、structural criticality）是成立的，但属于同一 paradigm 内的 variant 而非范式创新。\n   - Ensemble disagreement + Platt scaling 是标准 UQ 方法论，dependency graph centrality 是标准图论工具。组合本身不构成方法论创新。\n   - **实质 novelty delta**: 将 PF block 作为 cross-paradigm routing 的桥接单元，这一具体架构实例化是新的。但审稿人可能会评价为 \"a natural next step that anyone in the field would think of given Barkallah et al. and Ganguly et al.\"\n   \n2. **Significance: 中** — \n   - **问题重要性高**: 数学证明验证是 AI4Math 的核心瓶颈，Hard2Verify (2025) 揭示了当前 SOTA verifier 的严重不足（78.3% → 37.3%）。在 LLM 生成能力快速提升的当下，verification 的 reliability gap 是一个真实且紧迫的问题。\n   - **如果成功，影响有限但正面**: 展示一条可行路径（selective formal verification），对社区有参考价值。但不太可能改变领域格局——更像是一个工程系统贡献。\n   - **结果的 surprisingness**: 如果核心发现是 positive（PF block autoformalization 成功率高于 raw NL，dual-signal routing 有效），审稿人可能会说 \"I would have guessed this — of course structured blocks are easier to formalize, and of course uncertainty-based routing helps.\" 这是一个 **验证性** 贡献而非 **发现性** 贡献。\n   - **泛化性受限**: 方法深度依赖 PF decomposition（Barkallah et al.），如果 PF 本身在某些数学领域不适用，整个 pipeline 就无法工作。\n\n3. **Related Work: 强** — \n   - 覆盖面极为全面：LLM-based verification (ThinkPRM, Hard2Verify, PRM 系列)、formal verification (Safe, miniF2F-Lean Revisited, Goedel-Prover-V2)、selective verification (Ganguly et al.)、hybrid (HERMES, VERGE, UCCI, ProofSketcher, ProofFlow) 均有覆盖。\n   - 与 Ganguly et al. 的三维度差异化清晰且准确。\n   - 与 HERMES 的区分（generation vs. verification, uniform vs. selective）准确。\n   - 所有关键引用经验证均真实存在，描述准确。StepFun-Formalizer-32B 的 AAAI 2026 发表、Goedel-Prover-V2 的 ICLR 2026 发表、miniF2F-Lean Revisited 的 NeurIPS 2025 发表均已确认。\n   - **唯一不足**: ArxivMathGradingBench 来自 Barkallah et al. (May 2026)——这是一篇仅 1 周前的 arXiv preprint，其 benchmark 的质量和被社区认可程度尚不确定。\n\n【概率估计】: [22% - 32%] 中位 26%\n\n【估计理由】: \n- **Novelty 是主要限制因素**。核心架构洞见（PF block 作为 formalization bridge + 选择性 routing）是 Barkallah et al. (2026) 和 Ganguly et al. (NeurIPS 2025) 的自然组合延伸。审稿人很可能给出 \"incremental over prior work\" 的评价。三个维度打分中 Novelty 中偏弱直接压低了上界。\n- **Significance 中等但不突出**。问题重要性毋庸置疑，但预期发现的 surprisingness 不足——核心结果如果 positive，更像是\"确认了大家的直觉\"而非\"挑战了已有认知\"。这是一个验证性系统贡献。\n- **Related Work 强是加分项**，但 related work 好只能确保不因覆盖不足被拒，不能补偿 novelty 不足。\n- **上界 32% 的条件**: 如果 Phase 0 pilot 展示 block-level autoformalization 成功率远超预期（如 >60%），且 confident-but-wrong analysis 揭示了有趣的 failure mode taxonomy，可能被部分审稿人视为有价值的实证发现。\n- **下界 22% 的条件**: 如果审稿人认为这本质是\"用标准 UQ 方法做 routing\"的系统工程工作，novelty 评价可能降至\"弱\"。\n\n【主要风险】: \n1. **\"Natural next step\" 风险**: 核心 idea 可被概括为 \"take Barkallah et al.'s PF blocks + Ganguly et al.'s selective verification idea → combine them\"。审稿人可能认为这个组合过于显而易见，缺乏深层洞见。\n2. **Verification bootstrap 悖论**: Tier 2 formal verification 的有效性严重依赖 block-level autoformalization 成功率，而当前 SOTA (StepFun-Formalizer-32B) 在 FormalMATH-Lite 上仅 40.5% BEq@1。如果 PF block 的 autoformalization 成功率不显著优于此，Tier 2 路由的实际增益将远低于预期——被 route 到 formal verification 的 block 有过半无法被成功 formalize，fallback 回 LLM 判断，整个 selective routing 架构的价值就被严重稀释。\n```\n\nSources:\n- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)\n- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)\n- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)\n- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)\n- [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)\n- [StepFun-Formalizer-32B (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/40691)\n- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450)\n- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)\n- [VERGE (2026)](https://arxiv.org/abs/2601.20055)\n- [Hard2Verify (2025)](https://arxiv.org/abs/2510.13744)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough information to conduct a thorough evaluation. Let me synthesize all my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **Safe (Liu et al., ACL 2025)**: 首个使用 Lean 4 对 LLM 生成内容进行逐步形式化验证的框架。每一步都自动形式化并用定理证明器验证，报告 ~80% 验证成功率，但带来 4-8x 计算开销。这是本 proposal Tier 2 \"全面形式化验证\"基线的直接来源。proposal 中对其成本和局限的描述与原论文一致。\n\n2. **Pseudo-Formalization (Barkallah et al., arXiv 2605.20531, May 2026)**: 提出将自然语言证明分解为自包含模块（PF blocks），每个模块有明确前提、结论和证明。Block Verification (BV) 算法逐模块验证。该论文非常新（2026年5月），是本 proposal 的核心基础设施依赖。proposal 对 PF 的描述准确。注意：该论文极其新近（仅发布数天），本 proposal 高度依赖其基础设施和方法。\n\n3. **Ganguly et al. \"Grammars of Formal Uncertainty\" (NeurIPS 2025)**: 使用 PCFG 建模 LLM 生成形式化产物（SMT-LIB）的不确定性，实现选择性验证，减少 14-100% 错误。这是本 proposal 最直接的竞争工作——同样是\"不确定性引导的选择性形式化验证\"。proposal 声称的三个差异点（uncertainty source、routing target heterogeneity、structural criticality）是真实的，但核心理念（用不确定性信号决定哪些部分需要形式化验证）高度重叠。\n\n4. **HERMES (Ospanov et al., ICML 2026)**: 在证明生成过程中交替使用非形式推理和 Lean 4 形式化验证，实现 67% 准确率提升、80% FLOPs 减少。关键区别：HERMES 解决的是**生成**问题（输出格式可控），本 proposal 解决的是**验证**问题（输入为任意自然语言）。这个区分是合理的。\n\n5. **miniF2F-Lean Revisited (NeurIPS 2025)**: 系统评估发现端到端自动形式化管线最佳准确率约 36%；LLM 评估报告的 97% 正确率经人工审核仅为 66%。该论文直接支撑了 proposal 中\"全证明自动形式化存在根本性可扩展性障碍\"的论点。数据基本吻合。\n\n6. **ThinkPRM (2025)**: 使用仅 1% 过程标签训练的 verbalized PRM，在多个 benchmark 上超越判别式 PRM。代表当前最强的数据高效逐步 LLM 验证器。proposal 将其作为 baseline 是合理的。\n\n7. **StepFun-Formalizer-32B (AAAI 2026)**: 在 FormalMATH-Lite 上 BEq@1 达 40.5%，是当前最强的自动形式化模型之一。Goedel-Prover-V2 在 miniF2F 上 pass@32 达 88.1%。两者都是 proposal Tier 2 的核心依赖工具。需注意：40.5% 是在竞赛级 statement-level 任务上的表现，研究级证明的 block-level 形式化成功率可能更低或更高，尚无直接证据。\n\n8. **VERGE (Singh et al., 2026)**: 将 LLM 输出分解为原子 claim，路由到 SMT solver 或 soft verifier。与本 proposal 的路由理念有概念重叠，但 VERGE 面向一阶逻辑 claim 验证，非数学证明 block 验证。\n\n9. **Process-Driven Autoformalization in Lean 4 (2024)**: 独立验证了步骤级形式化比全证明形式化更可行的假设，支撑了 proposal 的 Claim 1。\n\n10. **DiscoUQ / 集成不确定性量化 (2025-2026)**: 多智能体 LLM 系统的不确定性量化方法日趋成熟，ensemble disagreement 用于 UQ 已有成熟方法论。proposal 使用的 ensemble disagreement + Platt scaling 是标准做法，不构成方法论创新。\n\n- **调研总结**: 该领域正处于\"LLM 验证不够可靠、形式化验证太贵\"的瓶颈期，选择性/自适应验证是一个活跃且合理的研究方向。Ganguly et al. (NeurIPS 2025) 已经建立了\"不确定性引导选择性形式化验证\"的范式。本 proposal 在此基础上引入 PF block 作为形式化单元、ensemble disagreement 作为 UQ 信号、dependency-graph criticality 作为结构信号——属于在已有范式上的增量推进，而非范式创新。\n\n---\n\n【Trivial Alternative 检验】:\n\n存在以下更简单的替代方案需要考量：\n\n1. **随机路由 10-20% 的 blocks 到形式化验证**：如果 PF block 级自动形式化本身成功率较高（proposal 假设 >30%），那么随机选择 15% 的 blocks 进行形式化验证可能已经能捕获相当比例的错误，因为错误在 blocks 中的分布可能足够均匀。proposal 的不确定性校准 + 图关键性路由的增量价值需要与这个 trivial baseline 对比。proposal 的 ablation 4 (routing signal 消融) 部分覆盖了这一点，但没有明确包含 \"random routing\" baseline。\n\n2. **仅用 ensemble BV (N=5) + 专家 prompt ensemble，不做任何形式化验证**：proposal 引用的 arXiv 2604.02450 (2026) 表明 specialized prompt ensembles 能显著提升 LLM 验证的 ceiling。如果 ensemble BV + prompt engineering 能把错误检测率从 ~50% 提到 ~70%，那么额外引入 Lean 4 形式化验证的边际收益可能不足以 justify 系统复杂度。\n\n3. **Ganguly et al. 的方法直接迁移到 PF blocks**：将 PCFG-based uncertainty 直接应用于 PF block 的形式化产物，而不需要 ensemble BV disagreement 作为新的 UQ 信号。\n\n**增量价值判断**：proposal 的核心增量在于\"跨验证范式路由\"（LLM tier → formal tier）和\"dual signal\"（uncertainty × criticality）。如果消融实验证明 dual signal 显著优于 random routing 和 heuristic-only routing，增量价值成立。但这是一个**经验性赌注**，而非理论保证。\n\n---\n\n【前提假设检验】:\n\n核心逻辑链中存在以下未经验证的前提：\n\n1. **\"PF block 级自动形式化比全证明形式化本质上更可行\"（Claim 1 核心前提）**：虽然有直觉支撑（自包含、明确前提/结论），且 Process-Driven Autoformalization (2024) 间接支持了步骤级形式化的可行性，但**尚无直接实证**证明 PF block 格式在 StepFun-Formalizer 上的形式化成功率。Phase 0 pilot 设计为测试此假设，阈值设为 30%——但 StepFun-Formalizer-32B 在竞赛级 statement-level 任务上仅达 40.5%，研究级证明 block 的成功率可能更低。这是整个系统的**阿喀琉斯之踵**。\n\n2. **\"Ensemble disagreement 能有效捕获 LLM 验证中的 confident-but-wrong 错误\"**：proposal 承认了这一风险并通过 dependency criticality 作为补充信号来 mitigate。但 LLM 集成在数学推理中的校准质量本身尚不确定——如果所有集成成员系统性地在同类推理步骤上犯同样错误（correlated failures），disagreement 信号将失效。这一假设需要实证验证。\n\n3. **\"自动形式化失败 ≠ 验证失败，可以通过 fallback 策略处理\"**：如果 Tier 2 形式化成功率偏低（如 <40%），大量被路由到 Tier 2 的 blocks 会 fallback 到某种替代策略。此时系统退化为\"偶尔能做形式化验证的增强版 LLM 验证\"，相对于纯 LLM 验证的优势可能不显著。Ablation 8 的 sensitivity analysis (假设 30/50/70/90% 成功率) 部分覆盖了这一点，但如果实际落在 30% 区间，系统的 value proposition 将大幅削弱。\n\n4. **\"35% 端到端自动形式化成功率是'架构性'障碍\"**：proposal 将此归因于\"monolithic proofs 中无界的上下文依赖\"，但这可能只是当前工具的经验上限，而非理论硬限。miniF2F-v2（修正 benchmark 后）已将管线准确率提升到 70%。随着 autoformalizer 和 prover 的改进，这一\"障碍\"可能消退，削弱 proposal 的动机论证。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中（偏弱）**\n   - 核心理念\"用不确定性引导选择性形式化验证\"已由 Ganguly et al. (NeurIPS 2025) 建立。proposal 声称的三个差异点（UQ 信号来源、跨范式路由、结构关键性信号）是真实的 deltas，但属于同一范式内的变体，而非范式创新。\n   - PF block 作为形式化单元是 PF (Barkallah et al., 2026) 的自然延伸——论文本身就强调了模块化和自包含性。将 PF block 映射到 Lean 4 theorem statement 是顺理成章的下一步，难以称之为\"surprising\"。\n   - Ensemble disagreement 作为 UQ 信号、Platt scaling 作为校准方法、dependency graph 的 fan-out degree 作为关键性指标——这些都是各自领域的标准做法，组合在一起并未产生方法论创新。\n   - **核心问题**：如果最终结果是 positive（selective routing at 15% cost overhead catches 80% of errors），审稿人可能会说\"this is a well-engineered system\"而非\"this is surprising\"。\n   - 支撑：Ganguly et al. (NeurIPS 2025) 已证明选择性形式化验证可行；PDA (2024) 已证明步骤级形式化更可行；DiscoUQ (2025-2026) 已证明 ensemble disagreement 用于 UQ 的有效性。本 proposal 的\"新\"主要在组合层面。\n\n2. **Significance: 中-强（偏中）**\n   - **问题重要性高**：LLM 证明验证可靠性不足（Hard2Verify 上 PRM 从 78.3% 降至 37.3%）和形式化验证成本过高（Safe 的 4-8x 开销）之间的 gap 是真实且重要的。\n   - **实用价值潜力大**：如果系统成功工作，为研究级数学证明的自动化验证提供了一条实际可行的路径。\n   - **影响力受限**：方法高度依赖 PF 生态系统（PF decomposition + BV + specific benchmarks），可推广性受限。如果 PF 方法未被广泛采纳，本工作的影响力将局限在一个较小的 niche。\n   - **Conditional significance**：本工作的重要性高度依赖于 PF block 级形式化成功率。如果 Phase 0 pilot 失败（<30%），整个 narrative 的前提崩塌。\n\n3. **Related Work: 强**\n   - 对领域的覆盖非常全面：LLM 验证（PF+BV、ThinkPRM、PRM 模型）、形式化验证（Safe、自动形式化工具）、选择性/自适应方法（Ganguly、Qu）、相关但不同的系统（HERMES、VERGE、UCCI、ProofSketcher、ProofFlow）。\n   - 与每个相关工作的差异化定位清晰且准确。特别是对 Ganguly et al. 的三层差异分析（uncertainty source / routing target / structural criticality）和对 HERMES 的 generation-vs-verification 区分都是精确的。\n   - 引用的关键论文均已通过搜索验证真实存在，描述基本准确。miniF2F-Lean Revisited 的数据引用（~35% end-to-end / 66% autoformalization）与原文一致。\n   - **轻微不足**：未讨论 miniF2F-v2 修正后管线准确率提升到 70% 这一事实，这可能削弱\"35% 是架构性障碍\"的论点。\n\n---\n\n【概率估计】: 22% - 32%，中位 26%\n\n【估计理由】:\n- Related Work 维度为 强，说明作者对领域有深刻理解，定位清晰——这提供了坚实的下限保障。\n- Significance 维度 中-强，问题本身重要且实用，但高度依赖 PF 生态系统的采纳度。\n- **Novelty 维度是主要限制因素**。Ganguly et al. (NeurIPS 2025) 已建立了\"不确定性引导选择性形式化验证\"的范式，本 proposal 的核心贡献在于将此范式迁移到 PF block 上下文并添加结构关键性信号。这是真实的增量，但可能不足以让顶会审稿人认为是\"sufficient novelty\"。\n- 概率上界被 novelty 限制在 ~32%：即使实验结果完美，\"系统集成\"层面的贡献在顶会评审中通常难以获得高分。\n- 概率下界由 related work 质量和问题重要性支撑在 ~22%：即使审稿人对 novelty 有疑虑，扎实的实验和清晰的定位可以避免底分。\n\n【主要风险】:\n1. **Novelty 不足**：最直接的竞争对手 Ganguly et al. (NeurIPS 2025) 已建立了高度相似的范式（uncertainty-guided selective formal verification），审稿人可能认为本 proposal 仅是 Ganguly + PF 的自然组合，novelty delta 不足以支撑一篇顶会论文。\n2. **核心前提脆弱**：\"PF block 级自动形式化比全证明形式化本质上更可行\"是整个系统的基石，但目前无直接实证。如果 Phase 0 pilot 显示 block-level 端到端成功率与 whole-proof 相差不大（例如都在 30-40%），则 Claim 1 的论证基础将瓦解，系统的 value proposition 大幅削弱。\n```\n\nSources:\n- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)\n- [Pseudo-Formalization for Automatic Proof Verification (arXiv 2605.20531)](https://arxiv.org/abs/2605.20531)\n- [Ganguly et al. - Grammars of Formal Uncertainty (NeurIPS 2025)](https://openreview.net/forum?id=QfKpJ00t2L)\n- [HERMES: Efficient and Verifiable Mathematical Reasoning (ICML 2026)](https://arxiv.org/abs/2511.18760)\n- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [StepFun-Formalizer-32B (AAAI 2026)](https://arxiv.org/abs/2508.04440)\n- [Goedel-Prover-V2](https://arxiv.org/pdf/2508.03613)\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)\n- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)\n- [DiscoUQ: Structured Disagreement Analysis](https://arxiv.org/pdf/2603.20975)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2605.20531, May 2026)**:\n   本 proposal 的核心依赖。PF 将证明分解为自包含的模块（显式前提、结论、证明），PF+Block Verification 在奥赛和研究级数学上 Pareto-dominates LLM-as-judge baselines。该论文同时发布了 ArxivMathGradingBench（35篇论文，40个已知错误）。注意：这篇论文 **极其新**（2026年5月19日），仅比本评审日期早8天，代码可用性未知。\n\n2. **Safe (Liu et al., ACL 2025)**:\n   Universal step-level formal verification in Lean 4，每步都做 autoformalization + 证明搜索。Proposal 正确引用其 ~80% 成功率和 4-8x 成本。这是本 proposal 要 beat 的 cost baseline。\n\n3. **Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025)**:\n   **最直接的竞争工作**。已经实现了基于不确定性（PCFG entropy）的选择性形式化验证，在 SMT-LIB 域上获得 14-100% 的错误减少。核心差异：Ganguly 建模生成侧不确定性（LLM→SMT-LIB），本 proposal 建模验证侧不确定性（BV ensemble disagreement）；Ganguly 在单一验证范式内路由，本 proposal 跨范式（LLM→formal）路由；Ganguly 无结构信号，本 proposal 加入 dependency-graph criticality。差异化存在但属增量式。\n\n4. **HERMES (Ospanov et al., ICML 2026)**:\n   交织非形式推理与 Lean 4 验证的证明 **生成** 框架（67% accuracy improvement, 80% fewer FLOPs）。但面向证明生成（输出格式可控），非验证（输入为任意 NL）。不同 setting，非直接竞争。\n\n5. **VERGE (Singh et al., arXiv 2601.20055, 2026)**:\n   在 SMT solvers 和 LLM-ensemble 验证之间做路由，面向一阶逻辑 claims。概念上相似（跨验证范式路由），但领域不同（一阶逻辑 vs. 数学证明块）。\n\n6. **StepFun-Formalizer-32B (AAAI 2026)**:\n   当前 SOTA autoformalization 模型，BEq@1 = 40.5% on FormalMATH-Lite, 26.7% on ProverBench。这意味着即使是 SOTA 模型，statement-level autoformalization 成功率也只有 ~40%，这对 proposal 的 Tier 2 天花板构成实质威胁。\n\n7. **Goedel-Prover-V2-32B (ICLR 2026)**:\n   SOTA formal theorem prover, 88.1% on MiniF2F pass@32，支持 verifier-guided self-correction。这是 proposal Tier 2 proof search 的核心组件。\n\n8. **miniF2F-Lean Revisited (NeurIPS 2025)**:\n   审视 autoformalization 局限性。LLM 评估的 autoformalization 准确率 ~97%，但人工审查只有 ~66%。Proposal 引用的 \"~35% end-to-end success\" 来自 66% × ~70% 估算。\n\n9. **ThinkPRM (arXiv 2504.16828, 2025)**:\n   Verbalized PRM，用 1% process labels 超越 discriminative PRMs。当前最强的 data-efficient step-level LLM verifier。是重要的 LLM-only baseline。\n\n10. **\"Do We Need Frontier Models to Verify Mathematical Proofs?\" (arXiv 2604.02450, 2026)**:\n    Prompt ensemble 可以让小模型（如 Qwen3.5-35B）在证明验证上匹配 frontier models（accuracy +9.1%, consistency +15.9%）。这直接威胁 proposal 的增量价值——如果更好的 prompt engineering 就能大幅提升 LLM-only 验证的天花板，formal verification 的边际收益可能更小。\n\n11. **Process-Driven Autoformalization in Lean 4 (2024)**:\n    独立证据表明 step-level formalization 比 whole-proof approaches 更可行。支持 Claim 1。\n\n- **调研总结**: 这个领域正在快速发展。选择性验证（用不确定性路由到形式化验证）的概念已由 Ganguly et al. (NeurIPS 2025) 在 SMT 域建立。本 proposal 的核心贡献是将这一范式迁移到数学证明验证，并引入 PF block 结构作为 formalization bridge + dependency-graph criticality 作为补充路由信号。这是一个合理的系统级贡献，但属于现有范式的领域适配，非范式创新。\n\n\n【Trivial Alternative 检验】:\n\n存在两个 trivial alternative 威胁：\n\n**(a) 更强的 LLM-only ensemble。** arXiv 2604.02450 表明 specialized prompt ensemble 可以让小模型在证明验证上达到 frontier 水平。如果在 PF+BV 基础上加上 prompt ensemble（proposal 自己的 Baseline 3），已经能显著提升 LLM 验证天花板，那么额外引入 formal verification 的增量收益可能很小。**Proposal 确实包含了这个 baseline（Baseline 3），这是好的设计**，但如果 Baseline 3 已经很强，系统的核心价值主张就被削弱了。\n\n**(b) 无选择性的 block-level Safe。** 如果直接对所有 PF block 做 Safe-style formal verification（而非选择性路由），成本可能因为 block 的自包含性而比 whole-proof Safe 低很多。这样就不需要不确定性路由，架构大幅简化。Proposal 需要论证：即使 block-level 降低了单步 autoformalization 难度，universal block-level formal verification 仍然太贵，从而证明选择性路由的必要性。\n\n**增量价值在于**：如果 (1) block-level autoformalization 确实比 whole-proof 显著更好（Claim 1 成立），且 (2) LLM-only 验证的天花板确实有限（prompt ensemble 仍漏掉大量错误），且 (3) 10-20% 路由确实能捕捉大部分 LLM 遗漏的错误，那么系统确实在 cost-quality Pareto frontier 上开辟了一个有价值的新点。但这三个条件都是 empirical bets。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的假设：\n\n1. **\"PF block 的自包含性使 block-level autoformalization 显著优于 whole-proof autoformalization\"** — 这是 Claim 1 的核心。结构上合理（显式前提/结论消除了 context-completion 问题），Process-Driven Autoformalization (2024) 提供了间接支持，但 **没有直接实证**。StepFun-Formalizer 在 FormalMATH-Lite 上 BEq@1 只有 40.5%，而 PF block 的结构化输入能把这个数字提高多少是完全未知的。Phase 0 pilot 设计得当，但 30% 的 go/no-go 阈值已经很低。\n\n2. **\"BV ensemble disagreement 能有效识别 LLM 验证不可靠的 block\"** — 即 uncertainty calibration 的有效性假设。LLM 普遍存在 overconfidence 问题（所有 ensemble 成员可能一致但错误），proposal 自己也提到了 \"confident-but-wrong\" 风险，并引入 dependency criticality 作为缓解。但这个缓解只是启发式的，没有理论保证。如果 LLM 对某类错误系统性地 confident-but-wrong，不确定性路由在这些错误类型上就会失效。\n\n3. **\"10-20% 的路由比例足以达到 near-formal reliability\"** — 这是最关键的假设。它要求 LLM 验证的错误集中在高不确定性区域。如果错误在 uncertainty 空间中均匀分布，你需要验证远超 20% 的 block 才能接近 formal reliability，此时成本优势消失。\n\n4. **\"Block-level end-to-end formal verification 的成功率足够高，使 Tier 2 routing 有意义\"** — StepFun-Formalizer BEq@1=40.5% × Goedel-Prover-V2 proof search success rate。即使 block 结构有帮助，end-to-end 成功率若仍然只有 ~30-50%，那么被路由到 Tier 2 的 block 中有一半会 formalization failure，系统需要大量的 fallback 逻辑，削弱了 formal verification 的可靠性保证。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** —\n   选择性形式化验证 + 不确定性路由的范式已由 Ganguly et al. (NeurIPS 2025) 在 SMT 域建立。Proposal 的差异化（验证侧 uncertainty、跨范式路由、dependency criticality）是真实的但属增量式迁移。VERGE (2026) 也已经在做跨验证范式的路由（SMT vs LLM），虽然面向不同领域。PF block 作为 formalization bridge 的 architectural insight (Claim 1) 是最有 novelty 的部分，因为它利用了 PF 的特殊结构特征（自包含、显式前提/结论）——但 PF 本身是一篇 8 天前的论文，且 \"step-level formalization 比 whole-proof 更容易\" 已被 Process-Driven Autoformalization (2024) 独立证明。总体而言，这是一个 **competent combination of existing ideas with a genuinely useful architectural observation**，但不是一个会让审稿人说 \"I didn't think of that\" 的 idea。\n\n2. **Significance: 中偏强** —\n   研究问题（以可承受成本实现可靠的数学证明验证）非常重要且 timely。LLM-only 验证的天花板（Hard2Verify 上 78.3%→37.3%，ArxivMathGradingBench ~50% 漏检）与 universal formal verification 的高成本之间确实存在一个需要填补的 gap。如果 selective routing 有效，它提供了一条 practical path to scaling formal verification，对数学推理和 AI safety 都有价值。但 significance 受限于：(a) 这是一个 pipeline/systems 贡献，不引入新的理论理解；(b) prompt ensemble (arXiv 2604.02450) 可能已经大幅缩小了这个 gap，削弱了 formal verification 的边际价值。\n\n3. **Related Work: 强** —\n   覆盖全面且定位清晰。对 Ganguly et al. 的差异化沿三个维度展开且令人信服。HERMES 被正确定位为 generation setting。VERGE、UCCI、ProofSketcher、ProofFlow 等潜在混淆工作都被明确区分。ThinkPRM 和 prompt ensemble 作为 LLM-only 上界被包含在 baselines 中。引用的关键论文均经 WebSearch 验证存在且描述基本准确（miniF2F-Lean Revisited 的 ~35% end-to-end 估算来源合理；StepFun-Formalizer 的 40.5% BEq@1 准确；Ganguly 的 14-100% 错误减少准确）。唯一的小问题是 ArxivMathGradingBench 上的 \"~50% 错误未检出\" 无法从搜索结果中精确验证。\n\n\n【概率估计】: 22% - 32%，中位 26%\n\n【估计理由】:\nNovelty 是限制上界的主要维度。选择性验证 + uncertainty routing 的范式已存在 (Ganguly, NeurIPS 2025)，本 proposal 本质上是将该范式适配到数学证明验证领域并引入 PF block 结构。Claim 1 (PF block as formalization bridge) 是最有价值的 novelty，但它更多是一个 architectural observation 而非 surprising finding。如果核心实验是 positive（selective routing 以低成本达到 near-formal reliability），一个熟悉该领域的审稿人会说 \"makes sense, good engineering\" 而非 \"surprising\"。Related Work 极强，Significance 实在，但 idea 的 novelty ceiling 将概率限制在中位偏下区间。\n\n此外，以下因素加权了不确定性：\n- 核心依赖 PF (May 19, 2026) 是一篇仅 8 天前的论文，代码可用性和可复现性存疑\n- StepFun-Formalizer BEq@1 = 40.5% 暗示 Tier 2 天花板可能不够高，限制系统的实际可靠性增益\n- Prompt ensemble (arXiv 2604.02450) 可能是一个 strong trivial alternative，削弱 formal verification 的增量价值\n\n【主要风险】:\n1. **Novelty 不足风险**：审稿人可能将此视为 Ganguly et al. (NeurIPS 2025) 的 domain adaptation + PF 的直接 follow-up，认为 novelty delta 不足以构成独立贡献。\"Uncertainty-guided selective verification\" 的核心 idea 已被建立，PF block bridge 虽好但可被视为 PF paper 的 natural extension。\n2. **Trivial alternative 风险**：如果 PF + BV with specialized prompt ensemble (Baseline 3) 已经接近 selective formal verification 的 recall，审稿人会质疑 Tier 2 formal verification 的必要性——增加了大量 pipeline 复杂度但边际收益可能很小。\n```\n\nSources:\n- [Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., 2026)](https://arxiv.org/abs/2605.20531)\n- [Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)](https://aclanthology.org/2025.acl-long.594/)\n- [Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025)](https://arxiv.org/abs/2505.20047)\n- [HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)](https://arxiv.org/abs/2511.18760)\n- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., 2026)](https://arxiv.org/abs/2601.20055)\n- [StepFun-Formalizer (AAAI 2026)](https://arxiv.org/abs/2508.04440)\n- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)\n- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)\n- [ThinkPRM: Process Reward Models That Think (2025)](https://arxiv.org/abs/2504.16828)\n- [Do We Need Frontier Models to Verify Mathematical Proofs? (arXiv 2604.02450, 2026)](https://arxiv.org/abs/2604.02450)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition\n\n## Core Problem\n\nHow can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain and structurally critical proof blocks to formal verification?\n\n## Thesis and Contributions\n\nWe advance two claims, each supported by a corresponding contribution:\n\n**Claim 1 (Architectural Insight):** Modular proof decomposition — as instantiated by Pseudo-Formalization (Barkallah et al., 2026) — serves as a natural bridge between informal and formal verification of mathematical proofs. Each PF block's explicit typed premises map directly to Lean 4 hypothesis lists, its single explicit conclusion maps to a Lean 4 goal statement, and its self-contained nature eliminates the context-completion problem that fundamentally limits whole-proof autoformalization to ~35% end-to-end success (miniF2F-Lean Revisited, NeurIPS 2025). We empirically validate this by demonstrating that PF-block-level autoformalization achieves substantially higher success rates than raw-NL-fragment autoformalization in a controlled paired comparison.\n\n**Claim 2 (System Design):** Building on this bridge, we design a two-tier selective verification pipeline that combines calibrated uncertainty scoring with dependency-graph criticality to route only the 10-20% most uncertain or structurally critical blocks to Lean 4 formal verification. This achieves near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization, and represents a viable path toward scaling formal verification to research-level proofs — where whole-proof autoformalization is fundamentally intractable.\n\n## Research Opportunity\n\nWhole-proof autoformalization faces a fundamental scalability barrier: context-completion difficulties and compounding error across steps limit end-to-end success to ~35% even with SOTA tools (66% autoformalization accuracy × ~70% theorem proving success; miniF2F-Lean Revisited, NeurIPS 2025). This barrier does not diminish with stronger models — it is architectural, arising from the unbounded context dependencies in monolithic proofs. Consequently, universal formal verification (Safe, Liu et al., ACL 2025) imposes 4-8x cost overhead per step while still being limited by autoformalization failures. Meanwhile, LLM-only verification (PF+Block Verification; Barkallah et al., May 2026) is cheap but leaves ~50% of research-level errors undetected on ArxivMathGradingBench. PF's modular block structure offers a way through this impasse: self-contained blocks with explicit premises and conclusions are structurally aligned with formal theorem statements, making block-level autoformalization fundamentally more tractable than whole-proof autoformalization. Step-level formalization has independently been shown more tractable than whole-proof approaches (Process-Driven Autoformalization in Lean 4, 2024). By adding calibrated uncertainty and dependency-graph criticality as a dual triage signal, we can route only the most critical blocks to formal verification, catching errors that LLM verification misses while operating within the tractability boundary of block-level autoformalization.\n\n## Research Landscape\n\n**LLM-based verification (cheap, unreliable):** Best PRM drops from 78.3% to 37.3% on Hard2Verify (Pandit et al., 2025). PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026). ThinkPRM (2025) advances data-efficient verbalized PRMs outperforming discriminative PRMs with 1% of process labels, representing the current strongest step-level LLM verifier. Specialized prompt ensembles can close much of the gap between small and frontier models for proof verification (Do We Need Frontier Models to Verify Mathematical Proofs?, arXiv 2604.02450, 2026), raising the LLM-only performance ceiling.\n\n**Universal formal verification (reliable, expensive):** Safe verifies each step in Lean 4 with ~80% success at 4-8x cost (Liu et al., ACL 2025). End-to-end autoformalization achieves only ~35% success (miniF2F-Lean Revisited, NeurIPS 2025). StepFun-Formalizer-32B achieves BEq@1 of 40.5% on FormalMATH-Lite for statement-level autoformalization.\n\n**Selective/adaptive verification (emerging):** Ganguly et al. (NeurIPS 2025) achieve 14-100% error reduction via selective SMT-based formalization using PCFG-based uncertainty. Our work differs on three levels: (1) uncertainty source — Ganguly models generation-side distribution (LLM→SMT-LIB), we model verification-side judgment uncertainty (BV ensemble disagreement on existing proofs); (2) routing target heterogeneity — Ganguly routes within a single verification paradigm (verify vs. abstain on SMT), we route across fundamentally different paradigms (LLM verification → formal verification); (3) structural criticality — Ganguly uses no structural signal, we introduce dependency-graph criticality as an orthogonal routing dimension. Qu (arXiv 2026) achieves 44% fewer verifier calls via adaptive allocation on MATH but operates within LLM-tier verification only.\n\n**Proof generation vs. verification taxonomy:** HERMES (Ospanov et al., ICML 2026) interleaves informal reasoning with Lean 4 verification during proof generation, achieving 67% accuracy improvement with 80% fewer FLOPs — but addresses proof generation (where output format is controllable) with uniform formalization, not proof verification of arbitrary NL input. Our work addresses the fundamentally different verification setting where PF decomposition is necessary to create structured formalization targets from arbitrary input. VERGE (Singh et al., arXiv 2026) routes between SMT solvers and LLM-ensemble verification for first-order logic claims, not mathematical proof blocks. UCCI (arXiv 2026) provides calibrated uncertainty for LLM cascade routing (small→large model), not across formal/informal verification tiers. ProofSketcher (arXiv 2026) produces typed proof sketches without uncertainty-guided routing. ProofFlow (2025) uses dependency graphs for autoformalization fidelity but not for verification routing decisions.\n\n## Proposed Approach\n\n**Phase 0 — Pilot study (go/no-go).** Before full pipeline development, we validate the core architectural assumption: randomly sample 50-100 PF blocks across mathematical domains and difficulty levels, test StepFun-Formalizer-32B autoformalization success rate and Goedel-Prover-V2-32B proof search success rate, establish block-level end-to-end success rate baseline. Threshold: if end-to-end success rate < 30%, Tier 2 requires redesign (e.g., multi-shot formalization with compiler-feedback self-correction). Report decomposed success rates: formalization type-check rate → proof search success rate → end-to-end rate.\n\n**Tier 1 — LLM Block Verification with calibrated uncertainty.** Decompose proof into PF blocks (Barkallah et al., 2026) with explicit premises, conclusions, and dependency graphs. Run Block Verification using QwQ-32B with dual uncertainty scoring: (i) ensemble disagreement via N=5 stochastic forward passes with temperature sampling, (ii) token-level CoT entropy. Calibrate via Platt scaling on synthetic evaluation set and miniF2F verification data (NOT on ArxivMathGradingBench, which is reserved for evaluation only), with temperature scaling as calibration method ablation.\n\n**Dual-signal routing.** Route blocks based on: uncertainty score × dependency criticality (primary: fan-out degree in inter-block dependency DAG; supplementary sensitivity analysis: dominator nodes, betweenness centrality). This dual signal mitigates the \"confident-but-wrong\" risk inherent in LLM overconfidence: (a) ensemble disagreement captures inter-model uncertainty more reliably than single-model confidence; (b) dependency criticality provides an uncertainty-independent signal — high-fan-out blocks receive formal verification even if BV is confident; (c) structural difficulty heuristics (block-internal step count, cited theorem count) serve as additional features.\n\n**Why calibrated uncertainty, not just structural heuristics?** Simple heuristics (block length, step count) capture surface complexity but miss blocks that are structurally simple yet reasoning-subtle — e.g., a one-step block applying a theorem in a non-obvious way. Ensemble disagreement flags exactly these cases: when model copies disagree on a seemingly-simple block, this signals hidden reasoning difficulty invisible to structural features. We validate this claim via head-to-head ablation against heuristic-only routing.\n\n**Tier 2 — Selective formal verification.** Routed blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging PF block structure (premises→Lean 4 hypotheses, conclusion→Lean 4 goal, no context completion needed) — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction (up to k=3 retry rounds using Lean compiler feedback). Per-block timeout: 5 min; per-proof timeout: 30 min. Fallback strategy for autoformalization failure or proof search timeout is an ablation variable.\n\n## Evaluation Plan\n\n**Benchmarks:**\n- ArxivMathGradingBench (Barkallah et al., 2026): 35 papers, 40 known errors. Held-out evaluation only (not used for calibration). Error detection precision/recall/F1, bootstrap CI (1000 resamples), McNemar's test, effect size (Cohen's h). Supplementary: per-paper accuracy.\n- Synthetic Error Detection Set: 400-500 instances from Hard2Verify competition-level problems. Multi-source error construction: (i) LLM-generated incorrect proofs, (ii) controlled perturbation of correct proofs (deleted steps, swapped theorems, computation errors), (iii) extracted known-error steps from Hard2Verify annotations. Ground-truth verification via answer matching + Lean 4 proof for correct proofs. Human validation on 50-80 instance subsample (Cohen's κ). Used for calibration and as co-primary evaluation benchmark.\n- miniF2F Verification Protocol: Generate ≥8 candidate proofs per problem (≥100 problems) using QwQ-32B, evaluate verification precision/recall. Aligned with Safe's miniF2F setting.\n\n**Baselines (7 methods):**\n- PF + BV single-pass (Barkallah et al., 2026)\n- PF + BV ensemble (N=5, no routing to formal verification)\n- PF + BV with specialized prompt ensemble (per arXiv 2604.02450, 2026): best-effort LLM verification upper bound\n- ThinkPRM (2025): SOTA data-efficient verbalized PRM\n- Qwen2.5-Math-PRM-7B: strongest open-source discriminative PRM at comparable scale\n- Safe universal formalization (Liu et al., ACL 2025)\n- HERMES (Ospanov et al., ICML 2026): if applicable to verification setting\n\n**Cost framework:** Unified metric: GPU-seconds per proof. Detailed breakdown: PF decomposition + ensemble BV (5× single BV) + routing overhead + autoformalization (per routed block) + proof search including retries and timeouts + fallback cost for Tier 2 failures. Pareto curve (cost vs. error detection recall) plotting all methods.\n\n**Ablations (8 experiments):**\n1. Uncertainty signal decomposition: ensemble disagreement only / CoT entropy only / combined — AUROC, ECE, recall@fixed-cost\n2. Routing signal: uncertainty only / dependency criticality only / simple structural heuristic only / dual signal — recall and cost\n3. Ensemble size: N=3 / N=5 / N=7\n4. Autoformalization failure fallback: accept / reject / majority-vote re-verification\n5. Threshold sweep: routing percentage 5%-50% — Pareto curve\n6. **PF blocks vs. raw NL autoformalization (Contribution 1 validation):** Paired comparison on same proofs. PF block input vs. raw NL fragment input to StepFun-Formalizer-32B. Metrics: Lean 4 type-check rate, proof search success rate. Paired Wilcoxon signed-rank test. This is a core result, not merely an ablation.\n7. Confident-but-wrong analysis: proportion of BV errors at >0.8 confidence, fraction captured by dual-signal vs. uncertainty-only routing\n8. Tier 2 sensitivity analysis: system Pareto curves under assumed Tier 2 success rates of 30%/50%/70%/90%, demonstrating robustness\n\n**Calibration method ablation:** Platt scaling vs. temperature scaling, cross-validated on calibration set, evaluated by ECE and routing decision quality.\n\n## Key References\n\n- Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2026)\n- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)\n- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (Pandit et al., arXiv 2025)\n- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)\n- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (Ganguly et al., NeurIPS 2025)\n- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (Qu, arXiv 2026)\n- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., arXiv 2026)\n- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)\n- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)\n- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)\n- ThinkPRM: Process Reward Models That Think (2025)\n- Qwen2.5-Math-PRM (2025)\n- ProofSketcher (arXiv 2026)\n- UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing (arXiv 2026)\n- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (2025)\n- Do We Need Frontier Models to Verify Mathematical Proofs? (arXiv 2604.02450, 2026)\n- Process-Driven Autoformalization in Lean 4 (2024)\n\n## Resource Estimate\n\n- **Phase 0 pilot:** ~30-50 GPU-hours (A100-80GB), 1-2 weeks. Go/no-go decision point.\n- **Full pipeline (Phase 1-3):** GPU hours: 400-550 (ensemble BV ~80h; StepFun-Formalizer ~80h; Goedel-Prover-V2 proof search ~130h including retries/timeouts; synthetic set construction ~40h; baselines + ablations ~120-170h). CPU hours: ~60h (Lean 4 kernel type-checking). Timeline: 14-18 weeks (2-3 researchers), including 2-3 week contingency for PF pipeline reproduction if code unavailable.\n- **Estimated GPU cost:** $1200-1650\n- **Lean 4 proof search:** Per-block timeout 5 min, per-proof timeout 30 min. ArxivMathGradingBench single pass: ~9h wall-clock (35 papers × ~30 blocks × 15% routing × 3.5 min/block). Independent blocks parallelizable.\n- **Critical path:** Phase 0 pilot (weeks 1-2) → PF pipeline setup + synthetic set (weeks 2-5) → uncertainty calibration (weeks 5-8) → full pipeline + ablations (weeks 8-15) → analysis + writing (weeks 15-18)."
}
````

---

### Runtime record

_source line 2 · 2026-05-27T13:21:09.924Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T13:21:09.924Z",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T13:21:09.938Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have comprehensive research data. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531) (Barkallah et al., arXiv May 2026): 本 proposal 的直接基础。提出 PF 格式——将证明分解为自包含模块，每个模块有显式前提、结论和自然语言证明。PF + Block Verification 在竞赛级和研究级基准上 Pareto-dominates LLM-as-judge，但在 ArxivMathGradingBench 上仍有 ~50% 的错误未被检出。本 proposal 本质上是 Barkallah et al. 的直接后续/扩展工作。

2. [Safe: Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/) (Liu et al., ACL 2025): 首个使用 Lean 4 对 LLM 生成内容进行逐步形式化验证的框架，成功率 ~80% 但成本 4-8x。本 proposal 直接以此为"可靠但昂贵"的对标。

3. [miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108) (NeurIPS 2025): 揭示端到端 autoformalization pipeline 的真实天花板——人工评审发现 autoformalization 准确率仅 66%（非 LLM 评估的 97%），combined with 70.8% proof search success → ~35% end-to-end。这是 proposal 论证 whole-proof autoformalization 不可行的核心依据。

4. [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047) (Ganguly et al., NeurIPS 2025): **最直接的竞争工作**。使用 PCFG-based 不确定性进行选择性 SMT 形式化验证，error reduction 14-100%。Proposal 声称在三个维度上区分（不确定性来源、路由目标异质性、结构关键性），这一区分是成立的但属于同一研究方向的 variant。

5. [HERMES](https://arxiv.org/abs/2511.18760) (Ospanov et al., ICML 2026): 在证明 **生成** 过程中交叉使用非形式推理和 Lean 4 验证，67% accuracy improvement，80% fewer FLOPs。但针对生成而非验证，且使用统一形式化而非选择性路由。

6. [ThinkPRM](https://arxiv.org/abs/2504.16828) (2025): 数据高效的 verbalized PRM，仅用 PRM800K 1% 的标注即超越判别式 PRM。被列为 baseline。

7. [Goedel-Prover-V2](https://arxiv.org/abs/2508.03613) (ICLR 2026): SOTA 定理证明器，miniF2F 88.1% pass@32。本 proposal 计划用其做 Tier 2 的 proof search。

8. [StepFun-Formalizer-32B](https://ojs.aaai.org/index.php/AAAI/article/view/40691) (AAAI 2026): SOTA autoformalization 模型，FormalMATH-Lite BEq@1 40.5%。本 proposal 计划用其做 Tier 2 的 autoformalization。**注意：这篇已发表在 AAAI 2026，proposal 对其能力的描述准确。**

9. [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450) (arXiv 2026): 发现通过 specialized prompt ensemble 可以使小模型在证明验证上逼近 frontier 模型（accuracy gap ~10%，但 consistency gap ~25%）。Proposal 正确地将其列为提升 LLM-only 验证上限的工作。

10. [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940) (2024): 已证明 step-level formalization 比 whole-proof formalization 更 tractable。**这对 proposal 的 Claim 1 构成直接的 prior art 威胁——"分块 formalization 比整体 formalization 更容易" 这一洞见已有前人工作支撑。**

11. [VERGE](https://arxiv.org/abs/2601.20055) (Singh et al., 2026): 使用 SMT solver 对 LLM 输出进行形式化验证和 semantic routing，但针对一阶逻辑 claims 而非数学证明块。

- **调研总结**: 数学证明验证领域正处于"LLM-cheap-unreliable vs. formal-expensive-reliable"的权衡前沿。Ganguly et al. (NeurIPS 2025) 已开创了"选择性形式化验证"范式，HERMES (ICML 2026) 已展示了形式+非形式交叉的价值，Process-Driven Autoformalization (2024) 已证明 step-level formalization 更 tractable。本 proposal 处于这些方向的自然交汇处——是一个合理的"下一步"，但并非一个全新方向。

【Trivial Alternative 检验】:

存在多个 trivial alternative 威胁：

(1) **PF + BV ensemble (N=5) alone**: Proposal 自身列为 baseline。如果 ensemble 已经能通过多数投票显著减少 false negative，那么增加 Tier 2 formal verification 的增量收益可能有限。关键问题是：BV ensemble 的 error detection recall 相对于单次 BV 能提升多少？如果 ensemble 已经从 ~50% 未检出降到 ~30%，那剩余的 ~20% gap 是否值得建设整个 Tier 2 pipeline？

(2) **Simple heuristic routing**: 用 block step count + cited theorem count + BV confidence < threshold 作为路由信号——无需 ensemble disagreement 或 calibration。Proposal 承诺用 ablation #2 对比，这是正确的，但问题是：如果 heuristic-only routing 达到 dual-signal 的 80% 效果且成本低得多，核心 contribution 就被削弱。

(3) **直接使用 "Do We Need Frontier Models..." (2604.02450) 的 specialized prompt ensemble**: 如果 prompt ensemble 能将 LLM-only 验证准确率提升 ~9%，这可能已经覆盖了 Tier 2 formal verification 能捕获的大部分增量错误。

**增量价值在哪**: 如果 PF block-level autoformalization 成功率确实显著高于 raw NL formalization（Phase 0 验证），且 dual-signal routing 确实能精准定位"confident-but-wrong" blocks（ablation #7 验证），则增量价值成立。但这两个"如果"都未经验证。

【前提假设检验】:

核心逻辑链中有以下未经验证的关键假设：

(1) **"PF block 的自包含结构使 autoformalization 从根本上更 tractable"**: 虽然 Process-Driven Autoformalization (2024) 支持 step-level > whole-proof，但 PF block ≠ step。PF block 可能包含多个推理步骤，其复杂度可能远超 miniF2F 级别的 single step。对于研究级证明中的 PF block，autoformalization 成功率可能仍然很低。**Phase 0 pilot 正是为了验证这一假设，说明作者意识到了这个风险——这是好的设计。**

(2) **"BV ensemble disagreement 是 block 正确性不确定性的可靠代理"**: Ensemble disagreement 在分类任务上的有效性有大量文献支持，但在 **自然语言证明验证** 这一特殊任务上，disagreement 可能更多地反映 prompt sensitivity 而非真实不确定性。如果 5 个 BV pass 对同一错误 block 都 confident-wrong（LLM overconfidence 的已知问题），ensemble disagreement 就无法检测到。Proposal 声称 dependency criticality 可以缓解这一问题，但这假定错误集中在高 fan-out blocks——这一假设没有实证支撑。

(3) **"10-20% routing 即可捕获 LLM 漏检的大多数错误"**: 这隐含假设 LLM 漏检的错误与 BV uncertainty / structural criticality 高度相关。但如果 LLM 漏检的错误恰恰是那些"看起来正确、结构简单但推理微妙"的 blocks——ensemble 可能也对它们高 confidence，dependency criticality 也不高——则 routing 完全失效。

(4) **"near-formal reliability"的表述需要谨慎定义**: 如果 Tier 2 的 autoformalization+proof search end-to-end 成功率只有 50%（这已经比 whole-proof 的 35% 好很多），那被 route 到 Tier 2 的 blocks 中有一半的形式化验证会失败，需要 fallback 到 LLM 判断，这部分的 reliability 并不比 Tier 1 更好。

【3 维度打分】:

1. **Novelty: 中偏弱** — 
   - 核心洞见 "分块更易 formalize" 已有 Process-Driven Autoformalization (2024) 铺路，虽然本 proposal 用的是 PF block 而非 generic step，但方向性洞见不新。
   - "选择性形式化验证" 的 paradigm 已被 Ganguly et al. (NeurIPS 2025) 建立。Proposal 在三个维度上的差异化（不确定性来源、cross-paradigm routing、structural criticality）是成立的，但属于同一 paradigm 内的 variant 而非范式创新。
   - Ensemble disagreement + Platt scaling 是标准 UQ 方法论，dependency graph centrality 是标准图论工具。组合本身不构成方法论创新。
   - **实质 novelty delta**: 将 PF block 作为 cross-paradigm routing 的桥接单元，这一具体架构实例化是新的。但审稿人可能会评价为 "a natural next step that anyone in the field would think of given Barkallah et al. and Ganguly et al."
   
2. **Significance: 中** — 
   - **问题重要性高**: 数学证明验证是 AI4Math 的核心瓶颈，Hard2Verify (2025) 揭示了当前 SOTA verifier 的严重不足（78.3% → 37.3%）。在 LLM 生成能力快速提升的当下，verification 的 reliability gap 是一个真实且紧迫的问题。
   - **如果成功，影响有限但正面**: 展示一条可行路径（selective formal verification），对社区有参考价值。但不太可能改变领域格局——更像是一个工程系统贡献。
   - **结果的 surprisingness**: 如果核心发现是 positive（PF block autoformalization 成功率高于 raw NL，dual-signal routing 有效），审稿人可能会说 "I would have guessed this — of course structured blocks are easier to formalize, and of course uncertainty-based routing helps." 这是一个 **验证性** 贡献而非 **发现性** 贡献。
   - **泛化性受限**: 方法深度依赖 PF decomposition（Barkallah et al.），如果 PF 本身在某些数学领域不适用，整个 pipeline 就无法工作。

3. **Related Work: 强** — 
   - 覆盖面极为全面：LLM-based verification (ThinkPRM, Hard2Verify, PRM 系列)、formal verification (Safe, miniF2F-Lean Revisited, Goedel-Prover-V2)、selective verification (Ganguly et al.)、hybrid (HERMES, VERGE, UCCI, ProofSketcher, ProofFlow) 均有覆盖。
   - 与 Ganguly et al. 的三维度差异化清晰且准确。
   - 与 HERMES 的区分（generation vs. verification, uniform vs. selective）准确。
   - 所有关键引用经验证均真实存在，描述准确。StepFun-Formalizer-32B 的 AAAI 2026 发表、Goedel-Prover-V2 的 ICLR 2026 发表、miniF2F-Lean Revisited 的 NeurIPS 2025 发表均已确认。
   - **唯一不足**: ArxivMathGradingBench 来自 Barkallah et al. (May 2026)——这是一篇仅 1 周前的 arXiv preprint，其 benchmark 的质量和被社区认可程度尚不确定。

【概率估计】: [22% - 32%] 中位 26%

【估计理由】: 
- **Novelty 是主要限制因素**。核心架构洞见（PF block 作为 formalization bridge + 选择性 routing）是 Barkallah et al. (2026) 和 Ganguly et al. (NeurIPS 2025) 的自然组合延伸。审稿人很可能给出 "incremental over prior work" 的评价。三个维度打分中 Novelty 中偏弱直接压低了上界。
- **Significance 中等但不突出**。问题重要性毋庸置疑，但预期发现的 surprisingness 不足——核心结果如果 positive，更像是"确认了大家的直觉"而非"挑战了已有认知"。这是一个验证性系统贡献。
- **Related Work 强是加分项**，但 related work 好只能确保不因覆盖不足被拒，不能补偿 novelty 不足。
- **上界 32% 的条件**: 如果 Phase 0 pilot 展示 block-level autoformalization 成功率远超预期（如 >60%），且 confident-but-wrong analysis 揭示了有趣的 failure mode taxonomy，可能被部分审稿人视为有价值的实证发现。
- **下界 22% 的条件**: 如果审稿人认为这本质是"用标准 UQ 方法做 routing"的系统工程工作，novelty 评价可能降至"弱"。

【主要风险】: 
1. **"Natural next step" 风险**: 核心 idea 可被概括为 "take Barkallah et al.'s PF blocks + Ganguly et al.'s selective verification idea → combine them"。审稿人可能认为这个组合过于显而易见，缺乏深层洞见。
2. **Verification bootstrap 悖论**: Tier 2 formal verification 的有效性严重依赖 block-level autoformalization 成功率，而当前 SOTA (StepFun-Formalizer-32B) 在 FormalMATH-Lite 上仅 40.5% BEq@1。如果 PF block 的 autoformalization 成功率不显著优于此，Tier 2 路由的实际增益将远低于预期——被 route 到 formal verification 的 block 有过半无法被成功 formalize，fallback 回 LLM 判断，整个 selective routing 架构的价值就被严重稀释。
```

Sources:
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)
- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)
- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)
- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)
- [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)
- [StepFun-Formalizer-32B (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/40691)
- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450)
- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)
- [VERGE (2026)](https://arxiv.org/abs/2601.20055)
- [Hard2Verify (2025)](https://arxiv.org/abs/2510.13744)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough information to conduct a thorough evaluation. Let me synthesize all my findings.

---

```
【阶段】: Triage

【领域调研】:

1. **Safe (Liu et al., ACL 2025)**: 首个使用 Lean 4 对 LLM 生成内容进行逐步形式化验证的框架。每一步都自动形式化并用定理证明器验证，报告 ~80% 验证成功率，但带来 4-8x 计算开销。这是本 proposal Tier 2 "全面形式化验证"基线的直接来源。proposal 中对其成本和局限的描述与原论文一致。

2. **Pseudo-Formalization (Barkallah et al., arXiv 2605.20531, May 2026)**: 提出将自然语言证明分解为自包含模块（PF blocks），每个模块有明确前提、结论和证明。Block Verification (BV) 算法逐模块验证。该论文非常新（2026年5月），是本 proposal 的核心基础设施依赖。proposal 对 PF 的描述准确。注意：该论文极其新近（仅发布数天），本 proposal 高度依赖其基础设施和方法。

3. **Ganguly et al. "Grammars of Formal Uncertainty" (NeurIPS 2025)**: 使用 PCFG 建模 LLM 生成形式化产物（SMT-LIB）的不确定性，实现选择性验证，减少 14-100% 错误。这是本 proposal 最直接的竞争工作——同样是"不确定性引导的选择性形式化验证"。proposal 声称的三个差异点（uncertainty source、routing target heterogeneity、structural criticality）是真实的，但核心理念（用不确定性信号决定哪些部分需要形式化验证）高度重叠。

4. **HERMES (Ospanov et al., ICML 2026)**: 在证明生成过程中交替使用非形式推理和 Lean 4 形式化验证，实现 67% 准确率提升、80% FLOPs 减少。关键区别：HERMES 解决的是**生成**问题（输出格式可控），本 proposal 解决的是**验证**问题（输入为任意自然语言）。这个区分是合理的。

5. **miniF2F-Lean Revisited (NeurIPS 2025)**: 系统评估发现端到端自动形式化管线最佳准确率约 36%；LLM 评估报告的 97% 正确率经人工审核仅为 66%。该论文直接支撑了 proposal 中"全证明自动形式化存在根本性可扩展性障碍"的论点。数据基本吻合。

6. **ThinkPRM (2025)**: 使用仅 1% 过程标签训练的 verbalized PRM，在多个 benchmark 上超越判别式 PRM。代表当前最强的数据高效逐步 LLM 验证器。proposal 将其作为 baseline 是合理的。

7. **StepFun-Formalizer-32B (AAAI 2026)**: 在 FormalMATH-Lite 上 BEq@1 达 40.5%，是当前最强的自动形式化模型之一。Goedel-Prover-V2 在 miniF2F 上 pass@32 达 88.1%。两者都是 proposal Tier 2 的核心依赖工具。需注意：40.5% 是在竞赛级 statement-level 任务上的表现，研究级证明的 block-level 形式化成功率可能更低或更高，尚无直接证据。

8. **VERGE (Singh et al., 2026)**: 将 LLM 输出分解为原子 claim，路由到 SMT solver 或 soft verifier。与本 proposal 的路由理念有概念重叠，但 VERGE 面向一阶逻辑 claim 验证，非数学证明 block 验证。

9. **Process-Driven Autoformalization in Lean 4 (2024)**: 独立验证了步骤级形式化比全证明形式化更可行的假设，支撑了 proposal 的 Claim 1。

10. **DiscoUQ / 集成不确定性量化 (2025-2026)**: 多智能体 LLM 系统的不确定性量化方法日趋成熟，ensemble disagreement 用于 UQ 已有成熟方法论。proposal 使用的 ensemble disagreement + Platt scaling 是标准做法，不构成方法论创新。

- **调研总结**: 该领域正处于"LLM 验证不够可靠、形式化验证太贵"的瓶颈期，选择性/自适应验证是一个活跃且合理的研究方向。Ganguly et al. (NeurIPS 2025) 已经建立了"不确定性引导选择性形式化验证"的范式。本 proposal 在此基础上引入 PF block 作为形式化单元、ensemble disagreement 作为 UQ 信号、dependency-graph criticality 作为结构信号——属于在已有范式上的增量推进，而非范式创新。

---

【Trivial Alternative 检验】:

存在以下更简单的替代方案需要考量：

1. **随机路由 10-20% 的 blocks 到形式化验证**：如果 PF block 级自动形式化本身成功率较高（proposal 假设 >30%），那么随机选择 15% 的 blocks 进行形式化验证可能已经能捕获相当比例的错误，因为错误在 blocks 中的分布可能足够均匀。proposal 的不确定性校准 + 图关键性路由的增量价值需要与这个 trivial baseline 对比。proposal 的 ablation 4 (routing signal 消融) 部分覆盖了这一点，但没有明确包含 "random routing" baseline。

2. **仅用 ensemble BV (N=5) + 专家 prompt ensemble，不做任何形式化验证**：proposal 引用的 arXiv 2604.02450 (2026) 表明 specialized prompt ensembles 能显著提升 LLM 验证的 ceiling。如果 ensemble BV + prompt engineering 能把错误检测率从 ~50% 提到 ~70%，那么额外引入 Lean 4 形式化验证的边际收益可能不足以 justify 系统复杂度。

3. **Ganguly et al. 的方法直接迁移到 PF blocks**：将 PCFG-based uncertainty 直接应用于 PF block 的形式化产物，而不需要 ensemble BV disagreement 作为新的 UQ 信号。

**增量价值判断**：proposal 的核心增量在于"跨验证范式路由"（LLM tier → formal tier）和"dual signal"（uncertainty × criticality）。如果消融实验证明 dual signal 显著优于 random routing 和 heuristic-only routing，增量价值成立。但这是一个**经验性赌注**，而非理论保证。

---

【前提假设检验】:

核心逻辑链中存在以下未经验证的前提：

1. **"PF block 级自动形式化比全证明形式化本质上更可行"（Claim 1 核心前提）**：虽然有直觉支撑（自包含、明确前提/结论），且 Process-Driven Autoformalization (2024) 间接支持了步骤级形式化的可行性，但**尚无直接实证**证明 PF block 格式在 StepFun-Formalizer 上的形式化成功率。Phase 0 pilot 设计为测试此假设，阈值设为 30%——但 StepFun-Formalizer-32B 在竞赛级 statement-level 任务上仅达 40.5%，研究级证明 block 的成功率可能更低。这是整个系统的**阿喀琉斯之踵**。

2. **"Ensemble disagreement 能有效捕获 LLM 验证中的 confident-but-wrong 错误"**：proposal 承认了这一风险并通过 dependency criticality 作为补充信号来 mitigate。但 LLM 集成在数学推理中的校准质量本身尚不确定——如果所有集成成员系统性地在同类推理步骤上犯同样错误（correlated failures），disagreement 信号将失效。这一假设需要实证验证。

3. **"自动形式化失败 ≠ 验证失败，可以通过 fallback 策略处理"**：如果 Tier 2 形式化成功率偏低（如 <40%），大量被路由到 Tier 2 的 blocks 会 fallback 到某种替代策略。此时系统退化为"偶尔能做形式化验证的增强版 LLM 验证"，相对于纯 LLM 验证的优势可能不显著。Ablation 8 的 sensitivity analysis (假设 30/50/70/90% 成功率) 部分覆盖了这一点，但如果实际落在 30% 区间，系统的 value proposition 将大幅削弱。

4. **"35% 端到端自动形式化成功率是'架构性'障碍"**：proposal 将此归因于"monolithic proofs 中无界的上下文依赖"，但这可能只是当前工具的经验上限，而非理论硬限。miniF2F-v2（修正 benchmark 后）已将管线准确率提升到 70%。随着 autoformalizer 和 prover 的改进，这一"障碍"可能消退，削弱 proposal 的动机论证。

---

【3 维度打分】:

1. **Novelty: 弱-中（偏弱）**
   - 核心理念"用不确定性引导选择性形式化验证"已由 Ganguly et al. (NeurIPS 2025) 建立。proposal 声称的三个差异点（UQ 信号来源、跨范式路由、结构关键性信号）是真实的 deltas，但属于同一范式内的变体，而非范式创新。
   - PF block 作为形式化单元是 PF (Barkallah et al., 2026) 的自然延伸——论文本身就强调了模块化和自包含性。将 PF block 映射到 Lean 4 theorem statement 是顺理成章的下一步，难以称之为"surprising"。
   - Ensemble disagreement 作为 UQ 信号、Platt scaling 作为校准方法、dependency graph 的 fan-out degree 作为关键性指标——这些都是各自领域的标准做法，组合在一起并未产生方法论创新。
   - **核心问题**：如果最终结果是 positive（selective routing at 15% cost overhead catches 80% of errors），审稿人可能会说"this is a well-engineered system"而非"this is surprising"。
   - 支撑：Ganguly et al. (NeurIPS 2025) 已证明选择性形式化验证可行；PDA (2024) 已证明步骤级形式化更可行；DiscoUQ (2025-2026) 已证明 ensemble disagreement 用于 UQ 的有效性。本 proposal 的"新"主要在组合层面。

2. **Significance: 中-强（偏中）**
   - **问题重要性高**：LLM 证明验证可靠性不足（Hard2Verify 上 PRM 从 78.3% 降至 37.3%）和形式化验证成本过高（Safe 的 4-8x 开销）之间的 gap 是真实且重要的。
   - **实用价值潜力大**：如果系统成功工作，为研究级数学证明的自动化验证提供了一条实际可行的路径。
   - **影响力受限**：方法高度依赖 PF 生态系统（PF decomposition + BV + specific benchmarks），可推广性受限。如果 PF 方法未被广泛采纳，本工作的影响力将局限在一个较小的 niche。
   - **Conditional significance**：本工作的重要性高度依赖于 PF block 级形式化成功率。如果 Phase 0 pilot 失败（<30%），整个 narrative 的前提崩塌。

3. **Related Work: 强**
   - 对领域的覆盖非常全面：LLM 验证（PF+BV、ThinkPRM、PRM 模型）、形式化验证（Safe、自动形式化工具）、选择性/自适应方法（Ganguly、Qu）、相关但不同的系统（HERMES、VERGE、UCCI、ProofSketcher、ProofFlow）。
   - 与每个相关工作的差异化定位清晰且准确。特别是对 Ganguly et al. 的三层差异分析（uncertainty source / routing target / structural criticality）和对 HERMES 的 generation-vs-verification 区分都是精确的。
   - 引用的关键论文均已通过搜索验证真实存在，描述基本准确。miniF2F-Lean Revisited 的数据引用（~35% end-to-end / 66% autoformalization）与原文一致。
   - **轻微不足**：未讨论 miniF2F-v2 修正后管线准确率提升到 70% 这一事实，这可能削弱"35% 是架构性障碍"的论点。

---

【概率估计】: 22% - 32%，中位 26%

【估计理由】:
- Related Work 维度为 强，说明作者对领域有深刻理解，定位清晰——这提供了坚实的下限保障。
- Significance 维度 中-强，问题本身重要且实用，但高度依赖 PF 生态系统的采纳度。
- **Novelty 维度是主要限制因素**。Ganguly et al. (NeurIPS 2025) 已建立了"不确定性引导选择性形式化验证"的范式，本 proposal 的核心贡献在于将此范式迁移到 PF block 上下文并添加结构关键性信号。这是真实的增量，但可能不足以让顶会审稿人认为是"sufficient novelty"。
- 概率上界被 novelty 限制在 ~32%：即使实验结果完美，"系统集成"层面的贡献在顶会评审中通常难以获得高分。
- 概率下界由 related work 质量和问题重要性支撑在 ~22%：即使审稿人对 novelty 有疑虑，扎实的实验和清晰的定位可以避免底分。

【主要风险】:
1. **Novelty 不足**：最直接的竞争对手 Ganguly et al. (NeurIPS 2025) 已建立了高度相似的范式（uncertainty-guided selective formal verification），审稿人可能认为本 proposal 仅是 Ganguly + PF 的自然组合，novelty delta 不足以支撑一篇顶会论文。
2. **核心前提脆弱**："PF block 级自动形式化比全证明形式化本质上更可行"是整个系统的基石，但目前无直接实证。如果 Phase 0 pilot 显示 block-level 端到端成功率与 whole-proof 相差不大（例如都在 30-40%），则 Claim 1 的论证基础将瓦解，系统的 value proposition 大幅削弱。
```

Sources:
- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)
- [Pseudo-Formalization for Automatic Proof Verification (arXiv 2605.20531)](https://arxiv.org/abs/2605.20531)
- [Ganguly et al. - Grammars of Formal Uncertainty (NeurIPS 2025)](https://openreview.net/forum?id=QfKpJ00t2L)
- [HERMES: Efficient and Verifiable Mathematical Reasoning (ICML 2026)](https://arxiv.org/abs/2511.18760)
- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [StepFun-Formalizer-32B (AAAI 2026)](https://arxiv.org/abs/2508.04440)
- [Goedel-Prover-V2](https://arxiv.org/pdf/2508.03613)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)
- [DiscoUQ: Structured Disagreement Analysis](https://arxiv.org/pdf/2603.20975)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

1. **Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2605.20531, May 2026)**:
   本 proposal 的核心依赖。PF 将证明分解为自包含的模块（显式前提、结论、证明），PF+Block Verification 在奥赛和研究级数学上 Pareto-dominates LLM-as-judge baselines。该论文同时发布了 ArxivMathGradingBench（35篇论文，40个已知错误）。注意：这篇论文 **极其新**（2026年5月19日），仅比本评审日期早8天，代码可用性未知。

2. **Safe (Liu et al., ACL 2025)**:
   Universal step-level formal verification in Lean 4，每步都做 autoformalization + 证明搜索。Proposal 正确引用其 ~80% 成功率和 4-8x 成本。这是本 proposal 要 beat 的 cost baseline。

3. **Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025)**:
   **最直接的竞争工作**。已经实现了基于不确定性（PCFG entropy）的选择性形式化验证，在 SMT-LIB 域上获得 14-100% 的错误减少。核心差异：Ganguly 建模生成侧不确定性（LLM→SMT-LIB），本 proposal 建模验证侧不确定性（BV ensemble disagreement）；Ganguly 在单一验证范式内路由，本 proposal 跨范式（LLM→formal）路由；Ganguly 无结构信号，本 proposal 加入 dependency-graph criticality。差异化存在但属增量式。

4. **HERMES (Ospanov et al., ICML 2026)**:
   交织非形式推理与 Lean 4 验证的证明 **生成** 框架（67% accuracy improvement, 80% fewer FLOPs）。但面向证明生成（输出格式可控），非验证（输入为任意 NL）。不同 setting，非直接竞争。

5. **VERGE (Singh et al., arXiv 2601.20055, 2026)**:
   在 SMT solvers 和 LLM-ensemble 验证之间做路由，面向一阶逻辑 claims。概念上相似（跨验证范式路由），但领域不同（一阶逻辑 vs. 数学证明块）。

6. **StepFun-Formalizer-32B (AAAI 2026)**:
   当前 SOTA autoformalization 模型，BEq@1 = 40.5% on FormalMATH-Lite, 26.7% on ProverBench。这意味着即使是 SOTA 模型，statement-level autoformalization 成功率也只有 ~40%，这对 proposal 的 Tier 2 天花板构成实质威胁。

7. **Goedel-Prover-V2-32B (ICLR 2026)**:
   SOTA formal theorem prover, 88.1% on MiniF2F pass@32，支持 verifier-guided self-correction。这是 proposal Tier 2 proof search 的核心组件。

8. **miniF2F-Lean Revisited (NeurIPS 2025)**:
   审视 autoformalization 局限性。LLM 评估的 autoformalization 准确率 ~97%，但人工审查只有 ~66%。Proposal 引用的 "~35% end-to-end success" 来自 66% × ~70% 估算。

9. **ThinkPRM (arXiv 2504.16828, 2025)**:
   Verbalized PRM，用 1% process labels 超越 discriminative PRMs。当前最强的 data-efficient step-level LLM verifier。是重要的 LLM-only baseline。

10. **"Do We Need Frontier Models to Verify Mathematical Proofs?" (arXiv 2604.02450, 2026)**:
    Prompt ensemble 可以让小模型（如 Qwen3.5-35B）在证明验证上匹配 frontier models（accuracy +9.1%, consistency +15.9%）。这直接威胁 proposal 的增量价值——如果更好的 prompt engineering 就能大幅提升 LLM-only 验证的天花板，formal verification 的边际收益可能更小。

11. **Process-Driven Autoformalization in Lean 4 (2024)**:
    独立证据表明 step-level formalization 比 whole-proof approaches 更可行。支持 Claim 1。

- **调研总结**: 这个领域正在快速发展。选择性验证（用不确定性路由到形式化验证）的概念已由 Ganguly et al. (NeurIPS 2025) 在 SMT 域建立。本 proposal 的核心贡献是将这一范式迁移到数学证明验证，并引入 PF block 结构作为 formalization bridge + dependency-graph criticality 作为补充路由信号。这是一个合理的系统级贡献，但属于现有范式的领域适配，非范式创新。


【Trivial Alternative 检验】:

存在两个 trivial alternative 威胁：

**(a) 更强的 LLM-only ensemble。** arXiv 2604.02450 表明 specialized prompt ensemble 可以让小模型在证明验证上达到 frontier 水平。如果在 PF+BV 基础上加上 prompt ensemble（proposal 自己的 Baseline 3），已经能显著提升 LLM 验证天花板，那么额外引入 formal verification 的增量收益可能很小。**Proposal 确实包含了这个 baseline（Baseline 3），这是好的设计**，但如果 Baseline 3 已经很强，系统的核心价值主张就被削弱了。

**(b) 无选择性的 block-level Safe。** 如果直接对所有 PF block 做 Safe-style formal verification（而非选择性路由），成本可能因为 block 的自包含性而比 whole-proof Safe 低很多。这样就不需要不确定性路由，架构大幅简化。Proposal 需要论证：即使 block-level 降低了单步 autoformalization 难度，universal block-level formal verification 仍然太贵，从而证明选择性路由的必要性。

**增量价值在于**：如果 (1) block-level autoformalization 确实比 whole-proof 显著更好（Claim 1 成立），且 (2) LLM-only 验证的天花板确实有限（prompt ensemble 仍漏掉大量错误），且 (3) 10-20% 路由确实能捕捉大部分 LLM 遗漏的错误，那么系统确实在 cost-quality Pareto frontier 上开辟了一个有价值的新点。但这三个条件都是 empirical bets。


【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的假设：

1. **"PF block 的自包含性使 block-level autoformalization 显著优于 whole-proof autoformalization"** — 这是 Claim 1 的核心。结构上合理（显式前提/结论消除了 context-completion 问题），Process-Driven Autoformalization (2024) 提供了间接支持，但 **没有直接实证**。StepFun-Formalizer 在 FormalMATH-Lite 上 BEq@1 只有 40.5%，而 PF block 的结构化输入能把这个数字提高多少是完全未知的。Phase 0 pilot 设计得当，但 30% 的 go/no-go 阈值已经很低。

2. **"BV ensemble disagreement 能有效识别 LLM 验证不可靠的 block"** — 即 uncertainty calibration 的有效性假设。LLM 普遍存在 overconfidence 问题（所有 ensemble 成员可能一致但错误），proposal 自己也提到了 "confident-but-wrong" 风险，并引入 dependency criticality 作为缓解。但这个缓解只是启发式的，没有理论保证。如果 LLM 对某类错误系统性地 confident-but-wrong，不确定性路由在这些错误类型上就会失效。

3. **"10-20% 的路由比例足以达到 near-formal reliability"** — 这是最关键的假设。它要求 LLM 验证的错误集中在高不确定性区域。如果错误在 uncertainty 空间中均匀分布，你需要验证远超 20% 的 block 才能接近 formal reliability，此时成本优势消失。

4. **"Block-level end-to-end formal verification 的成功率足够高，使 Tier 2 routing 有意义"** — StepFun-Formalizer BEq@1=40.5% × Goedel-Prover-V2 proof search success rate。即使 block 结构有帮助，end-to-end 成功率若仍然只有 ~30-50%，那么被路由到 Tier 2 的 block 中有一半会 formalization failure，系统需要大量的 fallback 逻辑，削弱了 formal verification 的可靠性保证。


【3 维度打分】:

1. **Novelty: 中** —
   选择性形式化验证 + 不确定性路由的范式已由 Ganguly et al. (NeurIPS 2025) 在 SMT 域建立。Proposal 的差异化（验证侧 uncertainty、跨范式路由、dependency criticality）是真实的但属增量式迁移。VERGE (2026) 也已经在做跨验证范式的路由（SMT vs LLM），虽然面向不同领域。PF block 作为 formalization bridge 的 architectural insight (Claim 1) 是最有 novelty 的部分，因为它利用了 PF 的特殊结构特征（自包含、显式前提/结论）——但 PF 本身是一篇 8 天前的论文，且 "step-level formalization 比 whole-proof 更容易" 已被 Process-Driven Autoformalization (2024) 独立证明。总体而言，这是一个 **competent combination of existing ideas with a genuinely useful architectural observation**，但不是一个会让审稿人说 "I didn't think of that" 的 idea。

2. **Significance: 中偏强** —
   研究问题（以可承受成本实现可靠的数学证明验证）非常重要且 timely。LLM-only 验证的天花板（Hard2Verify 上 78.3%→37.3%，ArxivMathGradingBench ~50% 漏检）与 universal formal verification 的高成本之间确实存在一个需要填补的 gap。如果 selective routing 有效，它提供了一条 practical path to scaling formal verification，对数学推理和 AI safety 都有价值。但 significance 受限于：(a) 这是一个 pipeline/systems 贡献，不引入新的理论理解；(b) prompt ensemble (arXiv 2604.02450) 可能已经大幅缩小了这个 gap，削弱了 formal verification 的边际价值。

3. **Related Work: 强** —
   覆盖全面且定位清晰。对 Ganguly et al. 的差异化沿三个维度展开且令人信服。HERMES 被正确定位为 generation setting。VERGE、UCCI、ProofSketcher、ProofFlow 等潜在混淆工作都被明确区分。ThinkPRM 和 prompt ensemble 作为 LLM-only 上界被包含在 baselines 中。引用的关键论文均经 WebSearch 验证存在且描述基本准确（miniF2F-Lean Revisited 的 ~35% end-to-end 估算来源合理；StepFun-Formalizer 的 40.5% BEq@1 准确；Ganguly 的 14-100% 错误减少准确）。唯一的小问题是 ArxivMathGradingBench 上的 "~50% 错误未检出" 无法从搜索结果中精确验证。


【概率估计】: 22% - 32%，中位 26%

【估计理由】:
Novelty 是限制上界的主要维度。选择性验证 + uncertainty routing 的范式已存在 (Ganguly, NeurIPS 2025)，本 proposal 本质上是将该范式适配到数学证明验证领域并引入 PF block 结构。Claim 1 (PF block as formalization bridge) 是最有价值的 novelty，但它更多是一个 architectural observation 而非 surprising finding。如果核心实验是 positive（selective routing 以低成本达到 near-formal reliability），一个熟悉该领域的审稿人会说 "makes sense, good engineering" 而非 "surprising"。Related Work 极强，Significance 实在，但 idea 的 novelty ceiling 将概率限制在中位偏下区间。

此外，以下因素加权了不确定性：
- 核心依赖 PF (May 19, 2026) 是一篇仅 8 天前的论文，代码可用性和可复现性存疑
- StepFun-Formalizer BEq@1 = 40.5% 暗示 Tier 2 天花板可能不够高，限制系统的实际可靠性增益
- Prompt ensemble (arXiv 2604.02450) 可能是一个 strong trivial alternative，削弱 formal verification 的增量价值

【主要风险】:
1. **Novelty 不足风险**：审稿人可能将此视为 Ganguly et al. (NeurIPS 2025) 的 domain adaptation + PF 的直接 follow-up，认为 novelty delta 不足以构成独立贡献。"Uncertainty-guided selective verification" 的核心 idea 已被建立，PF block bridge 虽好但可被视为 PF paper 的 natural extension。
2. **Trivial alternative 风险**：如果 PF + BV with specialized prompt ensemble (Baseline 3) 已经接近 selective formal verification 的 recall，审稿人会质疑 Tier 2 formal verification 的必要性——增加了大量 pipeline 复杂度但边际收益可能很小。
```

Sources:
- [Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., 2026)](https://arxiv.org/abs/2605.20531)
- [Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)](https://aclanthology.org/2025.acl-long.594/)
- [Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025)](https://arxiv.org/abs/2505.20047)
- [HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)](https://arxiv.org/abs/2511.18760)
- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., 2026)](https://arxiv.org/abs/2601.20055)
- [StepFun-Formalizer (AAAI 2026)](https://arxiv.org/abs/2508.04440)
- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)
- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)
- [ThinkPRM: Process Reward Models That Think (2025)](https://arxiv.org/abs/2504.16828)
- [Do We Need Frontier Models to Verify Mathematical Proofs? (arXiv 2604.02450, 2026)](https://arxiv.org/abs/2604.02450)


【原始 proposal（允许参考但不是主要依据）】:
# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition

## Core Problem

How can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain and structurally critical proof blocks to formal verification?

## Thesis and Contributions

We advance two claims, each supported by a corresponding contribution:

**Claim 1 (Architectural Insight):** Modular proof decomposition — as instantiated by Pseudo-Formalization (Barkallah et al., 2026) — serves as a natural bridge between informal and formal verification of mathematical proofs. Each PF block's explicit typed premises map directly to Lean 4 hypothesis lists, its single explicit conclusion maps to a Lean 4 goal statement, and its self-contained nature eliminates the context-completion problem that fundamentally limits whole-proof autoformalization to ~35% end-to-end success (miniF2F-Lean Revisited, NeurIPS 2025). We empirically validate this by demonstrating that PF-block-level autoformalization achieves substantially higher success rates than raw-NL-fragment autoformalization in a controlled paired comparison.

**Claim 2 (System Design):** Building on this bridge, we design a two-tier selective verification pipeline that combines calibrated uncertainty scoring with dependency-graph criticality to route only the 10-20% most uncertain or structurally critical blocks to Lean 4 formal verification. This achieves near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization, and represents a viable path toward scaling formal verification to research-level proofs — where whole-proof autoformalization is fundamentally intractable.

## Research Opportunity

Whole-proof autoformalization faces a fundamental scalability barrier: context-completion difficulties and compounding error across steps limit end-to-end success to ~35% even with SOTA tools (66% autoformalization accuracy × ~70% theorem proving success; miniF2F-Lean Revisited, NeurIPS 2025). This barrier does not diminish with stronger models — it is architectural, arising from the unbounded context dependencies in monolithic proofs. Consequently, universal formal verification (Safe, Liu et al., ACL 2025) imposes 4-8x cost overhead per step while still being limited by autoformalization failures. Meanwhile, LLM-only verification (PF+Block Verification; Barkallah et al., May 2026) is cheap but leaves ~50% of research-level errors undetected on ArxivMathGradingBench. PF's modular block structure offers a way through this impasse: self-contained blocks with explicit premises and conclusions are structurally aligned with formal theorem statements, making block-level autoformalization fundamentally more tractable than whole-proof autoformalization. Step-level formalization has independently been shown more tractable than whole-proof approaches (Process-Driven Autoformalization in Lean 4, 2024). By adding calibrated uncertainty and dependency-graph criticality as a dual triage signal, we can route only the most critical blocks to formal verification, catching errors that LLM verification misses while operating within the tractability boundary of block-level autoformalization.

## Research Landscape

**LLM-based verification (cheap, unreliable):** Best PRM drops from 78.3% to 37.3% on Hard2Verify (Pandit et al., 2025). PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026). ThinkPRM (2025) advances data-efficient verbalized PRMs outperforming discriminative PRMs with 1% of process labels, representing the current strongest step-level LLM verifier. Specialized prompt ensembles can close much of the gap between small and frontier models for proof verification (Do We Need Frontier Models to Verify Mathematical Proofs?, arXiv 2604.02450, 2026), raising the LLM-only performance ceiling.

**Universal formal verification (reliable, expensive):** Safe verifies each step in Lean 4 with ~80% success at 4-8x cost (Liu et al., ACL 2025). End-to-end autoformalization achieves only ~35% success (miniF2F-Lean Revisited, NeurIPS 2025). StepFun-Formalizer-32B achieves BEq@1 of 40.5% on FormalMATH-Lite for statement-level autoformalization.

**Selective/adaptive verification (emerging):** Ganguly et al. (NeurIPS 2025) achieve 14-100% error reduction via selective SMT-based formalization using PCFG-based uncertainty. Our work differs on three levels: (1) uncertainty source — Ganguly models generation-side distribution (LLM→SMT-LIB), we model verification-side judgment uncertainty (BV ensemble disagreement on existing proofs); (2) routing target heterogeneity — Ganguly routes within a single verification paradigm (verify vs. abstain on SMT), we route across fundamentally different paradigms (LLM verification → formal verification); (3) structural criticality — Ganguly uses no structural signal, we introduce dependency-graph criticality as an orthogonal routing dimension. Qu (arXiv 2026) achieves 44% fewer verifier calls via adaptive allocation on MATH but operates within LLM-tier verification only.

**Proof generation vs. verification taxonomy:** HERMES (Ospanov et al., ICML 2026) interleaves informal reasoning with Lean 4 verification during proof generation, achieving 67% accuracy improvement with 80% fewer FLOPs — but addresses proof generation (where output format is controllable) with uniform formalization, not proof verification of arbitrary NL input. Our work addresses the fundamentally different verification setting where PF decomposition is necessary to create structured formalization targets from arbitrary input. VERGE (Singh et al., arXiv 2026) routes between SMT solvers and LLM-ensemble verification for first-order logic claims, not mathematical proof blocks. UCCI (arXiv 2026) provides calibrated uncertainty for LLM cascade routing (small→large model), not across formal/informal verification tiers. ProofSketcher (arXiv 2026) produces typed proof sketches without uncertainty-guided routing. ProofFlow (2025) uses dependency graphs for autoformalization fidelity but not for verification routing decisions.

## Proposed Approach

**Phase 0 — Pilot study (go/no-go).** Before full pipeline development, we validate the core architectural assumption: randomly sample 50-100 PF blocks across mathematical domains and difficulty levels, test StepFun-Formalizer-32B autoformalization success rate and Goedel-Prover-V2-32B proof search success rate, establish block-level end-to-end success rate baseline. Threshold: if end-to-end success rate < 30%, Tier 2 requires redesign (e.g., multi-shot formalization with compiler-feedback self-correction). Report decomposed success rates: formalization type-check rate → proof search success rate → end-to-end rate.

**Tier 1 — LLM Block Verification with calibrated uncertainty.** Decompose proof into PF blocks (Barkallah et al., 2026) with explicit premises, conclusions, and dependency graphs. Run Block Verification using QwQ-32B with dual uncertainty scoring: (i) ensemble disagreement via N=5 stochastic forward passes with temperature sampling, (ii) token-level CoT entropy. Calibrate via Platt scaling on synthetic evaluation set and miniF2F verification data (NOT on ArxivMathGradingBench, which is reserved for evaluation only), with temperature scaling as calibration method ablation.

**Dual-signal routing.** Route blocks based on: uncertainty score × dependency criticality (primary: fan-out degree in inter-block dependency DAG; supplementary sensitivity analysis: dominator nodes, betweenness centrality). This dual signal mitigates the "confident-but-wrong" risk inherent in LLM overconfidence: (a) ensemble disagreement captures inter-model uncertainty more reliably than single-model confidence; (b) dependency criticality provides an uncertainty-independent signal — high-fan-out blocks receive formal verification even if BV is confident; (c) structural difficulty heuristics (block-internal step count, cited theorem count) serve as additional features.

**Why calibrated uncertainty, not just structural heuristics?** Simple heuristics (block length, step count) capture surface complexity but miss blocks that are structurally simple yet reasoning-subtle — e.g., a one-step block applying a theorem in a non-obvious way. Ensemble disagreement flags exactly these cases: when model copies disagree on a seemingly-simple block, this signals hidden reasoning difficulty invisible to structural features. We validate this claim via head-to-head ablation against heuristic-only routing.

**Tier 2 — Selective formal verification.** Routed blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging PF block structure (premises→Lean 4 hypotheses, conclusion→Lean 4 goal, no context completion needed) — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction (up to k=3 retry rounds using Lean compiler feedback). Per-block timeout: 5 min; per-proof timeout: 30 min. Fallback strategy for autoformalization failure or proof search timeout is an ablation variable.

## Evaluation Plan

**Benchmarks:**
- ArxivMathGradingBench (Barkallah et al., 2026): 35 papers, 40 known errors. Held-out evaluation only (not used for calibration). Error detection precision/recall/F1, bootstrap CI (1000 resamples), McNemar's test, effect size (Cohen's h). Supplementary: per-paper accuracy.
- Synthetic Error Detection Set: 400-500 instances from Hard2Verify competition-level problems. Multi-source error construction: (i) LLM-generated incorrect proofs, (ii) controlled perturbation of correct proofs (deleted steps, swapped theorems, computation errors), (iii) extracted known-error steps from Hard2Verify annotations. Ground-truth verification via answer matching + Lean 4 proof for correct proofs. Human validation on 50-80 instance subsample (Cohen's κ). Used for calibration and as co-primary evaluation benchmark.
- miniF2F Verification Protocol: Generate ≥8 candidate proofs per problem (≥100 problems) using QwQ-32B, evaluate verification precision/recall. Aligned with Safe's miniF2F setting.

**Baselines (7 methods):**
- PF + BV single-pass (Barkallah et al., 2026)
- PF + BV ensemble (N=5, no routing to formal verification)
- PF + BV with specialized prompt ensemble (per arXiv 2604.02450, 2026): best-effort LLM verification upper bound
- ThinkPRM (2025): SOTA data-efficient verbalized PRM
- Qwen2.5-Math-PRM-7B: strongest open-source discriminative PRM at comparable scale
- Safe universal formalization (Liu et al., ACL 2025)
- HERMES (Ospanov et al., ICML 2026): if applicable to verification setting

**Cost framework:** Unified metric: GPU-seconds per proof. Detailed breakdown: PF decomposition + ensemble BV (5× single BV) + routing overhead + autoformalization (per routed block) + proof search including retries and timeouts + fallback cost for Tier 2 failures. Pareto curve (cost vs. error detection recall) plotting all methods.

**Ablations (8 experiments):**
1. Uncertainty signal decomposition: ensemble disagreement only / CoT entropy only / combined — AUROC, ECE, recall@fixed-cost
2. Routing signal: uncertainty only / dependency criticality only / simple structural heuristic only / dual signal — recall and cost
3. Ensemble size: N=3 / N=5 / N=7
4. Autoformalization failure fallback: accept / reject / majority-vote re-verification
5. Threshold sweep: routing percentage 5%-50% — Pareto curve
6. **PF blocks vs. raw NL autoformalization (Contribution 1 validation):** Paired comparison on same proofs. PF block input vs. raw NL fragment input to StepFun-Formalizer-32B. Metrics: Lean 4 type-check rate, proof search success rate. Paired Wilcoxon signed-rank test. This is a core result, not merely an ablation.
7. Confident-but-wrong analysis: proportion of BV errors at >0.8 confidence, fraction captured by dual-signal vs. uncertainty-only routing
8. Tier 2 sensitivity analysis: system Pareto curves under assumed Tier 2 success rates of 30%/50%/70%/90%, demonstrating robustness

**Calibration method ablation:** Platt scaling vs. temperature scaling, cross-validated on calibration set, evaluated by ECE and routing decision quality.

## Key References

- Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2026)
- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)
- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (Pandit et al., arXiv 2025)
- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)
- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (Ganguly et al., NeurIPS 2025)
- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (Qu, arXiv 2026)
- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., arXiv 2026)
- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)
- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)
- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)
- ThinkPRM: Process Reward Models That Think (2025)
- Qwen2.5-Math-PRM (2025)
- ProofSketcher (arXiv 2026)
- UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing (arXiv 2026)
- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (2025)
- Do We Need Frontier Models to Verify Mathematical Proofs? (arXiv 2604.02450, 2026)
- Process-Driven Autoformalization in Lean 4 (2024)

## Resource Estimate

- **Phase 0 pilot:** ~30-50 GPU-hours (A100-80GB), 1-2 weeks. Go/no-go decision point.
- **Full pipeline (Phase 1-3):** GPU hours: 400-550 (ensemble BV ~80h; StepFun-Formalizer ~80h; Goedel-Prover-V2 proof search ~130h including retries/timeouts; synthetic set construction ~40h; baselines + ablations ~120-170h). CPU hours: ~60h (Lean 4 kernel type-checking). Timeline: 14-18 weeks (2-3 researchers), including 2-3 week contingency for PF pipeline reproduction if code unavailable.
- **Estimated GPU cost:** $1200-1650
- **Lean 4 proof search:** Per-block timeout 5 min, per-proof timeout 30 min. ArxivMathGradingBench single pass: ~9h wall-clock (35 papers × ~30 blocks × 15% routing × 3.5 min/block). Independent blocks parallelizable.
- **Critical path:** Phase 0 pilot (weeks 1-2) → PF pipeline setup + synthetic set (weeks 2-5) → uncertainty calibration (weeks 5-8) → full pipeline + ablations (weeks 8-15) → analysis + writing (weeks 15-18).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ac2a4d5e-7536-426f-9423-63ada1d2961b",
  "type": "user",
  "uuid": "0a9205a8-2420-4de0-a954-1cda4c45371b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T13:21:09.936Z_

```json
{
  "parentUuid": "0a9205a8-2420-4de0-a954-1cda4c45371b",
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
  "uuid": "dcecb207-b9d6-441b-89ad-b562fae78a80",
  "timestamp": "2026-05-27T13:21:09.936Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T13:21:09.936Z_

```json
{
  "parentUuid": "dcecb207-b9d6-441b-89ad-b562fae78a80",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e3602a4d-2fec-4bf9-8920-984b99a91c65",
  "timestamp": "2026-05-27T13:21:09.936Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive research data. Let me compile my eval…",
  "leafUuid": "e3602a4d-2fec-4bf9-8920-984b99a91c65",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate mathematical proof verification proposal",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52"
}
```

---

### Assistant

_source line 8 · 2026-05-27T13:21:28.328Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 中偏弱
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 26%

**Reviewer 2:**
- Novelty: 弱-中（偏弱）
- Significance: 中-强（偏中）


- Related Work: 强
- Probability: [22% - 32%] 中位 26%

**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [22% - 32%] 中位 26%

All three reviewers converge on identical acceptance probabilities with zero variance, which signals remarkable consistency. The consensus points to novelty as the primary weakness across all evaluations, while related work coverage is uniformly strong.

The core concern is that Gang et al.'s selective formal verification framework already covers similar ground, making this feel like an incremental extension rather than a fundamental advance. The autoformalization success rate of the PF block is the critical vulnerability, and the ensemble approach risks propagating confident but incorrect predictions. There's also a strong baseline threat from prompt ensemble methods that could achieve comparable results more simply. R3 rates novelty slightly more favorably than R1 and R2, but this modest difference doesn't shift the overall assessment.

What's striking is that despite these nuanced disagreements on novelty and significance, all three reviewers converge on the exact same probability range of 22%-32% with a median of 26% and zero standard deviation. Given this exceptional alignment, I should take the median estimate and tighten the interval to something like 23%-30% centered at 26%. Now I need to pull together what the reviewers said about implementation feasibility from the resource section to complete the assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3602a4d-2fec-4bf9-8920-984b99a91c65",
  "isSidechain": false,
  "requestId": "req_011CbT9FHd3EmjbYWUmqbUgW",
  "type": "assistant",
  "uuid": "a10ddf9c-3e55-4e00-9a0a-e6e84179a287",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sj8NJeDt6Ghr8QgMWhV9jP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20077,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2726,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20077,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2726,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20077
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

_source line 9 · 2026-05-27T13:22:14.918Z_

【阶段】: Meta Judge
【三次中位】: [26%, 26%, 26%]  std=0%
【共识维度】:
- **Novelty: 中偏弱（3/3 一致，最强共识）** — 三位审稿人均认为 Ganguly et al. (NeurIPS 2025) 已建立"不确定性引导选择性形式化验证"范式，本 proposal 属于该范式向 PF block 领域的增量迁移。R1 称"a natural next step that anyone in the field would think of"，R2 称"同一范式内的变体，而非范式创新"，R3 称"competent combination of existing ideas"。三人均指出 ensemble disagreement + Platt scaling + graph centrality 都是各自领域的标准工具，组合本身不构成方法论创新。
- **Related Work: 强（3/3 一致）** — 覆盖全面、定位精准、引用验证准确。对 Ganguly 三维度差异化和 HERMES generation-vs-verification 区分的评价一致为"清晰且准确"。
- **Significance: 中至中偏强（3/3 基本一致）** — 问题重要性毋庸置疑（Hard2Verify 78.3%→37.3%，ArxivMathGradingBench ~50% 漏检），但预期结果的 surprisingness 不足，更像验证性/系统工程贡献而非发现性贡献。
- **核心前提脆弱风险（3/3 一致）** — PF block 级 autoformalization 成功率无直接实证，StepFun-Formalizer BEq@1 仅 40.5%，Tier 2 天花板存疑。Phase 0 pilot 设计被认可但 30% go/no-go 阈值已经很低。
- **Trivial alternative 威胁（3/3 一致）** — prompt ensemble (arXiv 2604.02450) 和纯 BV ensemble (N=5) 可能已覆盖大部分增量收益，formal verification 的边际价值存疑。
- **Confident-but-wrong 风险（3/3 一致）** — 如果 LLM 对某类错误系统性 overconfident，ensemble disagreement 信号失效，dependency criticality 只是启发式缓解，无理论保证。

【异常维度】:
- R2 单独提到 miniF2F-v2 修正后管线准确率提升到 70%，可能削弱"35% 是架构性障碍"的论点 — 其他两位未涉及，但该观察有一定效力，可能进一步削弱动机论证的坚实程度。不过此点不改变总体判断方向，仅微幅增加下行风险。
- R1 单独提到"跷跷板"式的 verification bootstrap 悖论表述最为尖锐（Tier 2 成功率低时系统退化为"偶尔能做形式化验证的增强版 LLM 验证"）— 其他两位也触及此问题但措辞不同，本质为同一关切，不算真正异常。

【最终概率】: [22% - 30%] 中位 26%
【一致性】: 高（std=0%，三位审稿人独立给出完全相同的区间和中位数）
【综合理由】:
这是我见过的最高一致性评审结果——三位审稿人在完全独立的情况下给出了完全相同的 [22%-32%] 中位 26% 估计，且在所有核心维度（Novelty 为主要限制因素、Related Work 强但无法补偿 novelty 不足、核心前提脆弱、trivial alternative 威胁真实）上高度一致。

鉴于高一致性，按规则缩窄区间。上界从 32% 收窄至 30%，理由是：三位审稿人给出 32% 上界的条件（Phase 0 大幅超预期 + confident-but-wrong 分析揭示有趣 taxonomy）本身属于乐观情景，而三位审稿人同时提到的 trivial alternative 威胁（prompt ensemble 可能已覆盖大部分增量）和 R2 提到的 miniF2F-v2 修正后动机论证被削弱，使乐观情景的概率降低。下界维持 22%，因 Related Work 强和问题重要性提供了坚实的下限保障。

**核心判断**：这是一篇领域理解深刻、实验设计周全、定位清晰的 proposal，但其核心 idea 是两个已有范式（Ganguly 的选择性验证 + Barkallah 的 PF block）的自然组合，novelty delta 不足以跨过顶会门槛。审稿人最可能的评价是"well-engineered system, incremental over prior work"。

【建议】: 不推荐（中位 26% 显著低于 36% 阈值，且三位审稿人高度一致，无上调空间）

【实施评估】:
- 计算资源: 总计 ~430-600 GPU-hours (A100-80GB)，预估成本 $1200-1650。Phase 0 pilot 约 30-50 GPU-hours。资源需求合理，不构成瓶颈。
- 数据需求: ArxivMathGradingBench（35篇论文，来自 Barkallah et al. 2026，公开性存疑——论文仅发布 8 天）；Hard2Verify（公开）；miniF2F（公开）；需自建 400-500 实例的合成错误检测集。数据可得性基本可行但依赖 PF 代码/数据的公开程度。
- 人工介入: 合成错误检测集需人工验证 50-80 实例子集（Cohen's κ），约 20-40 人时。Phase 0 pilot 可能需要人工审核 autoformalization 结果。整体人工需求可控。
- 训练需求: 不需要从头训练模型。Platt scaling / temperature scaling 的校准训练量极小。所有核心组件（QwQ-32B、StepFun-Formalizer-32B、Goedel-Prover-V2-32B）均为推理时使用，无训练开销。
- 新 Benchmark: 需构建合成错误检测集（400-500 实例），工作量约 40 GPU-hours + 人工验证。不需要构建全新的大规模 benchmark。
- 预估周期: 14-18 周（2-3 名研究者），含 2-3 周 PF pipeline 复现的 contingency。关键路径：Phase 0 (2周) → PF 搭建+合成集 (3周) → 校准 (3周) → 全 pipeline+消融 (7周) → 分析写作 (3周)。**风险点**：PF (May 2026) 代码可用性未知，如需从论文复现可能增加 2-4 周。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a10ddf9c-3e55-4e00-9a0a-e6e84179a287",
  "isSidechain": false,
  "requestId": "req_011CbT9FHd3EmjbYWUmqbUgW",
  "type": "assistant",
  "uuid": "e1d6405d-40d2-4e43-bab9-e3d277da82d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sj8NJeDt6Ghr8QgMWhV9jP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20077,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2726,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20077,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2726,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20077
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive research data. Let me compile my eval…",
  "leafUuid": "e1d6405d-40d2-4e43-bab9-e3d277da82d9",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate mathematical proof verification proposal",
  "sessionId": "fc14db4d-f1a3-4832-8b47-fcec9b6e5c52"
}
```

---
