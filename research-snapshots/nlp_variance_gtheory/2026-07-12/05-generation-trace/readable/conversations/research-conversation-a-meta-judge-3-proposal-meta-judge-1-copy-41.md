# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/b9428c2b-d14e-454c-94b4-9d203535debc.jsonl`
- **Structured JSON:** [`7729783068e511e99258.json`](../../sessions/77/7729783068e511e99258.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:24:25.329Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:24:25.329Z",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have a comprehensive picture of the research landscape. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [NSRSA] Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment (arXiv 2603.21558, March 2026): 用 SymPy 做步骤级符号验证过滤训练数据，拒绝 ~34% 的\"lucky guess\"解。在 GSM8K 上用 Qwen3-4B 评估。确认 proposal 描述准确——NSRSA 确实在过滤后丢弃了诊断信息。\n- [SwS] Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025, OpenReview): 基于行为弱点的定向问题合成，7B 模型获得 10% 平均增益。使用 LLM-based 弱点识别，非符号化。Proposal 描述准确。\n- [Solver-Verifier Gap] Theoretical Modeling of LLM Self-Improvement Training Dynamics (ICLR 2026, arXiv 2507.00075): 理论建模 solver-verifier gap 驱动自改进，已发表于 ICLR 2026。Proposal 引用准确。\n- [Self-Play Information Gain] Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain (arXiv 2603.02218, March 2026): 揭示可持续自进化需要每轮迭代增加可学习信息。Proposer/Solver/Verifier 三角色框架。描述准确。\n- [VHG] Verifier-Backed Hard Problem Generation (arXiv 2605.06660, May 2026): 三方自博弈 + 符号/LLM 验证器，pass@1 从 56.8% 提升到 69.0%。验证器用于问题有效性验证，非步骤级诊断。描述准确。\n- [Hypothesis-Driven Error Analysis] Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis (arXiv 2604.04386, April 2026): 用 LLM 生成关于失败模式的假设 → 合成目标问题。将 Llama-3.3-70B 准确率从 77% 降至 45%。聚焦评估而非训练。\n- [WarriorMath] (arXiv 2508.01245, 2025): 缺陷感知框架，平均提升 12.57%。使用 LLM 协作的问题合成+渐进训练。\n- [Self-Error-Instruct] Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025): **Proposal 未提及但高度相关。** 通过错误类型聚类(error keyphrases → clustering → error types) 来泛化错误案例，合成针对性训练数据。核心思路（错误分类→定向合成）与 SymDiag 非常接近，只是用 LLM (GPT-4o) 而非符号化方法做错误分类。\n- [Adaptive Problem Generation via Symbolic Representations] (arXiv 2602.19187, Feb 2026): **Proposal 未提及但高度相关。** 在符号空间（SymPy/SMT）做问题表示和修改，闭环框架通过 prompt optimization 学习修改策略，自适应调整问题难度。与 SymDiag 的\"符号化+闭环\"主题高度重合。\n- [FoVer] Training Step-Level Reasoning Verifiers with Formal Verification Tools (arXiv 2505.15960, 2025): 用 Z3/Isabelle 自动标注步骤级错误标签训练 PRM。与 SymDiag 的步骤级符号验证主题相关。\n- [RV-Syn] (arXiv 2504.20426, 2026): 从结构化函数库构建计算图合成可验证数据，6.3% 增益。静态管线，非闭环。\n- [MathSmith] (arXiv 2508.05592, 2025): RL 训练的问题合成策略，9种难度策略。无诊断反馈。\n\n**调研总结**: 数学推理自改进是 2025-2026 年极度活跃的研究方向，存在多条并行线路：(1) 符号验证用于数据过滤(NSRSA)；(2) 弱点/缺陷感知的定向合成(SwS, WarriorMath, Self-Error-Instruct)；(3) 符号空间的问题生成(RV-Syn, Adaptive Problem Generation)；(4) 验证器驱动的自博弈(VHG)；(5) 自改进的理论分析(Solver-Verifier Gap, Self-Play Information Gain)。SymDiag 的定位是将线路(1)和(2)桥接起来——用符号诊断替代 LLM-based 弱点识别来驱动合成。**但 Self-Error-Instruct (ACL 2025) 已经在做\"错误分类→定向合成\"这件事，Adaptive Problem Generation (Feb 2026) 已经在做\"符号空间+闭环\"这件事。SymDiag 的真正增量是\"符号化的错误分类\"而非\"错误分类→定向合成\"这个范式本身。**\n\n【Trivial Alternative 检验】:\n存在两个 trivial-combination baseline 构成威胁：\n1. **NSRSA 过滤 + SwS 合成的简单管线拼接**：用 NSRSA 的符号验证做数据过滤，用 SwS 的行为弱点识别做定向合成。这个组合不需要 SymDiag 提出的\"诊断引擎\"和\"错误分类学\"，但可能获得大部分收益。SymDiag 的增量价值在于：符号诊断比 LLM 行为诊断更精确、更可靠、不会被模型 collapse 影响。但这个增量有多大需要实证——如果 LLM-based 弱点识别已经\"够好\"，符号诊断的边际价值可能有限。\n2. **Self-Error-Instruct 的思路 + SymPy 替代 GPT-4o**：Self-Error-Instruct 已经在做错误类型聚类→定向合成，SymDiag 本质上是用 SymPy 替代 GPT-4o 做错误分类。如果 SymPy 的分类能力有限（见下文前提假设检验），这个替换的价值可能不大。\n\n**增量价值的关键论点**是：符号验证不会随模型能力提升而失效（solver-verifier gap 理论支持），而 LLM-based 诊断可能被 collapse 污染。这是一个合理的理论论点，但其实际影响大小未知。\n\n【前提假设检验】:\n核心逻辑链中有 3 个未经验证的关键假设：\n\n1. **\"SymPy 能可靠地将错误分类为 fine-grained taxonomy\"**：这是最大的假设风险。SymPy 可以检测算术错误（arithmetic miscalculation），但要区分 \"algebraic manipulation error\" vs \"logical flow inconsistency\" vs \"constraint violation\" 需要对推理步骤做深层语义理解。SymPy 本质上是一个符号计算引擎，不是一个推理理解引擎。对于 AIME/OlympiadBench 级别的复杂推理（组合数学、数论证明、几何），SymPy 的步骤级诊断能力极其有限。Proposal 在这一点上没有给出任何可行性论证。\n\n2. **\"错误分类可以有意义地指导问题合成\"**：即使知道模型在\"代数变换\"上犯错多，如何让 GRPO-trained synthesizer 生成能精准\"probe\"代数变换弱点的问题？从错误类型到有效训练问题的映射是一个 non-trivial 的跳跃。\"per-category generation budgets allocated by error frequency and impact\" 听起来合理，但实际上这种 allocation 可能不如简单的基于难度的采样。\n\n3. **\"单调递增的可学习信息增益\"这一形式化保证**：Proposal 声称提供\"the first formal analysis connecting solver-verifier gap theory to diagnostic-driven synthesis\"，并证明\"monotonically increasing learnable information gain per iteration\"。这是一个非常强的数学声明。在实际系统中，信息增益取决于错误分类的准确性、合成问题的质量、模型学习动态等多个因素。将这些因素严格形式化并证明单调性，要么需要极度简化的假设（使定理无实际意义），要么是无法证明的。\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — SymDiag 的核心思路\"把符号验证从过滤器变成诊断引擎来驱动定向合成\"是一个合理的 gap-filling 贡献，但 novelty 的真实 delta 有限：\n   - Self-Error-Instruct (ACL 2025) 已经实现了\"错误分类→定向合成\"这个范式，只是用 LLM 而非符号方法做分类。SymDiag 的增量是\"换一种分类工具\"。\n   - Adaptive Problem Generation via Symbolic Representations (Feb 2026) 已经在符号空间做闭环问题生成。\n   - VHG (May 2026) 已经把符号验证器融入问题生成的自博弈循环。\n   - 剥离 surface differences 后，SymDiag 的核心新意在于\"SymPy 错误分类学 + 诊断条件化合成\"这个具体实例。这更接近 incremental combination 而非 paradigm shift。\n   - 如果这个 idea positive，审稿人大概率会说 \"I would have guessed that using diagnostic info helps\"——因为\"更多信息 > 更少信息\"是直觉上显而易见的。\n\n2. **Significance: 中** — 研究问题本身（数学推理自改进）非常重要且时效性强。如果 SymDiag 的方法确实有效：\n   - 对实践有价值：提供了一种不依赖 LLM 做弱点诊断的替代方案\n   - 理论贡献（形式化连接 solver-verifier gap 与诊断驱动合成）有潜在价值\n   - 但受限于符号验证的适用范围：仅适用于可符号化验证的数学问题，不具备向更广泛推理任务的泛化性\n   - 增量改进的幅度可能有限——NSRSA 的过滤 vs. 诊断驱动合成的差距可能不如预期大\n\n3. **Related Work: 中偏弱** — Proposal 列举了 11 篇参考文献，覆盖面看似广泛，但存在关键遗漏：\n   - **未提及 Self-Error-Instruct (ACL 2025)**：这是最直接的竞争对手，同样做\"错误分类→定向合成\"。遗漏此文显著削弱了 novelty claim 的可信度。\n   - **未提及 Adaptive Problem Generation via Symbolic Representations (Feb 2026)**：同样在符号空间做闭环问题生成。\n   - **未提及 FoVer (2025)**：同样用形式化工具做步骤级错误标注。\n   - 这些遗漏不是边缘文献——它们是直接挑战 SymDiag novelty 定位的核心竞争者。审稿人如果发现这些遗漏，会严重质疑 contribution 的新颖性。\n\n【概率估计】: 20% - 30%，中位 25%\n\n【估计理由】:\n- Novelty 维度是主要限制因素。核心思路（错误分类→定向合成）已有 Self-Error-Instruct 做过，符号空间闭环已有 Adaptive Problem Generation 做过。SymDiag 的真正增量——\"符号化的错误分类替代 LLM-based 分类\"——是一个有价值但 incremental 的贡献。\n- 关键前提假设（SymPy 能做 fine-grained error taxonomy）缺乏论证，且在复杂数学推理上可能不成立。\n- Significance 落在 \"timely but incremental\" 区间：如果 positive，审稿人更可能说 \"makes sense, not surprising\" 而非 \"surprising, didn't expect that\"。\n- Related work 遗漏了直接竞争者，如果审稿人熟悉 Self-Error-Instruct 或 Adaptive Problem Generation，会显著降低对 novelty 的评价。\n- 理论贡献（形式化保证）如果真的能严格证明会是亮点，但 \"monotonically increasing information gain\" 的声明过强，可能引发审稿人质疑。\n- Proposal 的工程质量和文献调研的全面性（对已引文献的描述准确）构成一定的下限保障。\n\n【主要风险】:\n1. **Novelty 被判为 incremental combination**：Self-Error-Instruct + 符号验证 ≈ SymDiag 的核心贡献；审稿人可能认为这只是将已有组件（NSRSA的符号验证 + SwS/Self-Error-Instruct的错误分类→合成范式）拼接在一起。\n2. **SymPy fine-grained error taxonomy 的可行性**：如果审稿人质疑 SymPy 在 AIME/Olympiad 级别问题上做 \"logical flow inconsistency\" vs \"constraint violation\" 分类的可靠性，整个方法的根基将受到动摇——这直接影响核心 contribution 的成立。\n```\n\nSources:\n- [NSRSA - Stabilizing Iterative Self-Training with Verified Reasoning](https://arxiv.org/abs/2603.21558)\n- [SwS - Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)\n- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)\n- [Self-Play Information Gain](https://arxiv.org/abs/2603.02218)\n- [VHG - Verifier-Backed Hard Problem Generation](https://arxiv.org/abs/2605.06660)\n- [Hypothesis-Driven Error Analysis](https://arxiv.org/abs/2604.04386)\n- [Self-Error-Instruct (ACL 2025)](https://arxiv.org/abs/2505.22591)\n- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)\n- [FoVer - Training Step-Level Reasoning Verifiers](https://arxiv.org/abs/2505.15960)\n- [RV-Syn](https://arxiv.org/abs/2504.20426)\n- [MathSmith](https://arxiv.org/abs/2508.05592)\n- [WarriorMath](https://arxiv.org/abs/2508.01245)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. NSRSA (arXiv 2603.21558, March 2026): 使用 SymPy 进行 step-level 符号验证来过滤自训练数据，在 GSM8K 上用 Qwen3-4B-Thinking 做了 5 轮迭代，拒绝了约 34% 的\"lucky guess\"解答，DPO reward accuracy 从 46% 提升到 63%，MATH-500 cross-task transfer +5.7pp。但仅在 GSM8K/MATH-500 上测试，验证后的诊断信息被丢弃。与本 proposal 的关系：SymDiag 声称在 NSRSA 基础上利用被丢弃的诊断信号——这一 gap 是真实存在的。\n\n2. SwS (NeurIPS 2025, OpenReview): 微软出品，在 RL 预训练阶段记录模型持续失败的问题，按类别分组提取共性概念，合成针对性新问题并按 budget 分配。在 Qwen2.5 (7B/32B) 上取得约 10%/7.7% 平均提升。使用 LLM-based 的弱点识别。与本 proposal 的关系：SymDiag 声称用 symbolic diagnosis 替代 SwS 的 LLM-based diagnosis，这是核心差异化点。\n\n3. Solver-Verifier Gap Theory (ICLR 2026, arXiv 2507.00075): 理论建模 LLM 自改进的训练动态，证明 solver-verifier 能力差距决定自改进的天花板，accuracy 呈指数趋近极限。与本 proposal 的关系：SymDiag 声称提供\"连接 solver-verifier gap 理论与 diagnostic-driven synthesis 的首个形式化分析\"——这是一个非常强的 claim。\n\n4. VHG (arXiv 2605.06660, May 2026, concurrent): 三方自博弈（setter-solver-verifier），使用 symbolic 和 LLM verifiers 来验证生成问题的有效性和难度，在多个 benchmark 上取得 56.8%→69.0% pass@1 提升。但 verifier 只用于问题验证，不做 step-level 错误诊断。与本 proposal 的关系：VHG 是最直接的竞争者，但确实不做 step-level error diagnosis → synthesis conditioning。\n\n5. WarriorMath (arXiv 2025): 用 LLM committee 评估缺陷，保留模型失败的数据进行训练，平均提升 12.57%。与本 proposal 的关系：同样是\"defect-aware\"思路但用 LLM-based 评估，SymDiag 声称 symbolic grounding 更可靠。\n\n6. Hypothesis-Driven Error Analysis (arXiv 2604.04386, April 2026, concurrent): 用 LLM 生成关于失败模式的假说来合成针对性 benchmark 问题，将 Llama-3.3-70B-Instruct 的准确率从 77% 降低到 45%。与本 proposal 的关系：类似的\"诊断→合成\"思路但缺乏 symbolic grounding，且专注 evaluation 而非 training。\n\n7. Self-Play Information Gain (arXiv 2603.02218, March 2026): 证明可持续自进化需要每轮迭代增加 learnable information，提出 Epiplexity 度量。与本 proposal 的关系：SymDiag 引用其理论框架声称\"monotonically increasing learnable information gain\"。\n\n8. RV-Syn (arXiv 2504.20426, 2026): 从结构化函数库构建 computational graphs 作为可验证解题蓝图，在 LLaMA-3-8B 上 +6.3%。但是静态 pipeline，不做迭代自改进。\n\n9. MathSmith (arXiv 2508.05592, 2025): RL 训练的问题合成策略，包含 weakness-focused variant generation 模块。\n\n- **调研总结**: 数学推理自改进领域在 2025-2026 年极其拥挤。核心赛道包括：(a) 符号验证用于过滤（NSRSA），(b) 弱点识别驱动合成（SwS, WarriorMath），(c) RL 训练的问题生成（MathSmith, VHG），(d) 理论建模（solver-verifier gap, self-play information gain）。SymDiag 声称占据的位置是\"(a)+(b)+(d) 的交叉点：symbolic diagnostic + targeted synthesis + formal guarantee\"，这个交叉点确实尚未被直接占据，但各组件均已独立存在。\n\n\n【Trivial Alternative 检验】:\n\n**存在明确的 trivial alternative 威胁。** 最直接的低成本替代方案是：\n\n1. **NSRSA filtering + SwS-style category-level weakness targeting**：在 NSRSA 的 symbolic 过滤之后，简单统计哪些**问题类别**（代数、几何、组合等）的通过率最低，然后像 SwS 那样按类别 budget 生成更多该类问题。这不需要 step-level error taxonomy，但可能捕获大部分收益。\n\n2. **NSRSA + 简单 error counting**：统计 SymPy 验证拒绝的解答中，哪一步被拒绝次数最多（step position），生成在相应步骤复杂度上加大难度的问题。不需要 fine-grained error taxonomy。\n\nSymDiag 的增量价值取决于一个关键假设：**知道模型\"为什么犯错\"（error type: arithmetic vs. algebraic vs. logical）比知道\"在什么问题上犯错\"（problem category）能提供显著更好的合成信号。** 但这个假设没有任何先验理论或实证支持。如果 error type conditioning 相对于 problem category conditioning 只带来边际改进，那么整个框架的 added value 会很有限。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的关键假设：\n\n1. **SymPy 能可靠地将错误分类到 proposed taxonomy（arithmetic miscalculation / algebraic manipulation / logical flow inconsistency / constraint violation）**。SymPy 擅长验证算术和代数等式是否成立，但\"logical flow inconsistency\"和\"constraint violation\"的自动分类远非 trivial——这需要理解问题语义和推理意图，可能已经超出了纯 symbolic computation 的能力边界。Proposal 没有讨论这个分类的准确率会是多少，也没有说明如何处理分类错误。\n\n2. **Error taxonomy conditioning 能有效转化为有区分度的问题生成**。即使诊断出\"arithmetic miscalculation\"，如何让 GRPO-trained synthesizer 生成专门考察 arithmetic accuracy 而非其他能力的问题？这个 conditioning mechanism 的有效性是未知的。用 GRPO reward 来激励 synthesizer 生成\"provoke specific error types\"的问题，reward signal 如何设计？Proposal 没有充分说明。\n\n3. **Formal convergence guarantee 的可交付性**。Proposal 声称将证明\"symbolic diagnosis maintains asymmetric verification preventing collapse while ensuring monotonically increasing learnable information gain per iteration\"。这把 solver-verifier gap theory（关于 self-improvement dynamics）和 self-play information gain theory（关于 learnable information）两个独立理论框架连接起来，并额外加入 error-taxonomy conditioning 的约束。这要么需要非常强的新理论贡献，要么会退化为对已有理论的 trivial 复述（\"因为我们用了 symbolic verifier 所以 gap 存在\"——这 NSRSA 已经隐含了）。\n\n4. **SymPy verification 能 scale 到 AIME/OlympiadBench 难度**。NSRSA 仅在 GSM8K（小学数学）和 MATH-500 上验证。AIME 和 OlympiadBench 涉及数论、组合、几何等需要远更复杂 symbolic reasoning 的领域，SymPy 的 step-level verification 在这些问题上的覆盖率和准确率是完全未知的。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — SymDiag 的核心贡献是将 symbolic verification 的 diagnostic 信号（而非仅 binary filter）用于 condition 问题合成。这个组合确实尚未被直接实现，但：\n   - NSRSA 已经实现了 SymPy step-level verification（诊断信息只需\"不丢弃\"即可获得）\n   - SwS 已经实现了 weakness-targeted synthesis with budget allocation\n   - VHG 已经实现了 verifier-backed problem generation with RL\n   - 核心\"新\"的部分是 error taxonomy → synthesis conditioning 这个 bridging mechanism，但这是一个相对 straightforward 的工程组合，不涉及方法论层面的根本创新\n   - 所声称的 formal convergence guarantee 如果真正 novel 且 non-trivial，可以显著提升 novelty，但基于前提假设检验中的分析，很可能会退化为对已有理论的 direct application\n   - 最关键的判断：**如果核心发现是 positive（error taxonomy conditioning 比 category-level targeting 效果好），审稿人的反应更可能是\"I would have guessed this\"而非\"surprising\"**\n\n2. **Significance: 中** — 问题方向完全成立：数学推理自改进是 2025-2026 年最热门的研究方向之一，\"don't discard diagnostic information\"的 insight 是合理的。但：\n   - 预期增量改进的幅度有限（从 NSRSA 的 filter-only 到 diagnostic-conditioned synthesis，改进空间受限于 error taxonomy 的有效性）\n   - 该框架的 generalizability 受限于 SymPy 可验证的问题范围——对于不容易 symbolic verify 的推理任务（如几何直觉、创造性 problem-solving），该框架不适用\n   - 如果 formal theory 部分能做得扎实，significance 可以上升到中偏强\n\n3. **Related Work: 强** — Proposal 对 related work 的覆盖非常全面，包括：\n   - 核心前置工作（NSRSA, SwS, Solver-Verifier Gap Theory, Self-Play Information Gain）\n   - 直接竞争者（VHG, WarriorMath, MathSmith, RV-Syn）\n   - 最新 concurrent work（VHG May 2026, Hypothesis-Driven Error Analysis April 2026）\n   - 差异化定位清晰（symbolic diagnosis vs. LLM-based diagnosis, diagnostic-conditioned synthesis vs. filter-only）\n   - 经调研验证，proposal 对各论文的描述基本准确（NSRSA 的 34% 拒绝率、SwS 的 10% 提升、VHG 的 69% pass@1 等均可核实）\n\n\n【概率估计】: 18% - 28%，中位 23%\n\n【估计理由】:\n- **Novelty 是限制上界的主要维度**。核心贡献是 well-motivated 的工程组合（symbolic diagnosis + targeted synthesis），但缺乏方法论层面的根本创新。在一个极度拥挤的领域中（2025-2026 年有超过 10 篇直接相关工作），\"把 A 的诊断信号接入 B 的合成框架\"很难让审稿人感到 surprised。\n- **Trivial alternative 威胁真实存在**。NSRSA filtering + SwS-style category targeting 是一个更简单、更直接的 baseline，如果实验中不能证明 fine-grained error taxonomy conditioning 显著优于 category-level targeting，整篇论文的核心 claim 就站不住。\n- **Formal convergence guarantee 是 high risk/high reward 的赌注**。如果能交付有实质意义的新理论结果（不是 trivial application of existing theory），概率可以上探 30%+；如果退化为\"因为 symbolic verifier 所以 gap 存在\"这种已知结论，则反而会被审稿人视为 overclaim。\n- **Related work 覆盖优秀**，不会因为 missing baselines 被拒，这提供了一个可靠的下限。\n- 概率没有更低是因为：问题方向完全正确，related work 极其完善，且 symbolic diagnosis → synthesis 这个特定 niche 确实没有被现有工作直接占据。\n\n【主要风险】:\n1. **Novelty 不足 / Trivial alternative**：审稿人可能认为\"使用已有 symbolic verifier 的诊断信息来 condition 已有的 weakness-targeted synthesis\"是一个 obvious next step，不构成足够的学术贡献。如果实验中 error-taxonomy-conditioned synthesis 相对 problem-category-conditioned synthesis 的提升不显著，核心 claim 直接崩塌。\n2. **Formal guarantee overclaim**：如果 convergence analysis 只是对 solver-verifier gap theory 的 trivial 套用（\"我们用了 symbolic verifier → gap 存在 → 不 collapse\"），审稿人会认为这是 overclaim 而非 contribution；如果要做 non-trivial 的理论，则交付风险极高。\n```\n\nSources:\n- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)\n- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)\n- [VHG: Verifier-Backed Hard Problem Generation](https://arxiv.org/abs/2605.06660)\n- [WarriorMath: Defect-aware Framework](https://arxiv.org/pdf/2508.01245)\n- [Hypothesis-Driven Error Analysis for Math Problem Generation](https://arxiv.org/html/2604.04386v1)\n- [Self-Play Information Gain](https://arxiv.org/abs/2603.02218)\n- [RV-Syn: Rational and Verifiable Mathematical Reasoning Data Synthesis](https://arxiv.org/abs/2504.20426)\n- [MathSmith: Synthetic Problem Generation with Reinforced Policy](https://arxiv.org/abs/2508.05592)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough research to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **NSRSA — \"Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment\"** (arXiv 2603.21558, March 2026):\n   - 已实现 SymPy 级别的 step-level 符号验证，包含算术运算校验、逻辑流一致性检查、领域约束验证。\n   - 在 GSM8K 上 Qwen3-4B-Thinking 经过 5 轮迭代达到 91.0%，filtering 拒绝了 ~34% 的\"幸运猜测\"。\n   - **关键：NSRSA 的符号验证器已经能分类错误类型（arithmetic, logical flow, domain constraints），只是将其用于过滤而非引导合成。本 proposal 的核心差异化 claim \"NSRSA 丢弃了诊断信号\" 成立，但从\"诊断用于过滤\"到\"诊断用于引导合成\"是一个 engineering-level 的扩展，不是 conceptual breakthrough。**\n\n2. **SwS — \"Self-aware Weakness-driven Problem Synthesis in RL for LLM Reasoning\"** (NeurIPS 2025, OpenReview):\n   - 通过模型 RL 训练过程中持续失败的问题提取核心 weakness concepts，合成针对性训练问题。\n   - 7B/32B 模型在 8 个 benchmark 上平均提升 10%/7.7%。\n   - 使用 LLM-based 弱点识别（behavioral level），不使用符号验证，不处理 collapse 问题。\n   - **与本 proposal 的关系：proposal 的核心 claim 是将 SwS 的 LLM-based 弱点诊断替换为符号诊断——这是一个模块化替换(modular substitution)。**\n\n3. **Solver-Verifier Gap Theory** (ICLR 2026, OpenReview):\n   - 建立了 self-improvement 的理论框架，证明持续提升需要 solver 与 verifier 之间的能力差距。\n   - 预测 self-improvement 的极限遵循指数收敛律。\n   - **本 proposal 声称要\"首次\"将此理论连接到 diagnostic-driven synthesis——但原论文的框架已经足够通用，将其应用到特定场景更多是 instantiation 而非理论突破。**\n\n4. **VHG — \"Verifier-Backed Hard Problem Generation\"** (arXiv 2605.06660, May 2026, 并行工作):\n   - 三方 self-play：setter-solver-verifier，同时使用 Hard (symbolic) 和 Soft (LLM) verifier。\n   - 在 general math benchmark 上将 pass@1 从 56.8% 提升到 69.0%。\n   - **VHG 已经将符号验证器整合进问题生成循环，只是验证用于 problem validation 而非 step-level error diagnosis。SymDiag 的差异化在于 step-level 诊断 → conditioned synthesis，但这个差异在概念层面比较窄。**\n\n5. **LEMMA — \"Learning from Errors for Mathematical Advancement\"** (ACL Findings 2025):\n   - 已实现错误类型分类(error-type taxonomy)，构建 error-corrective trajectories 用于训练。\n   - **直接证明了 error taxonomy → training data 的路径已被探索，虽然 LEMMA 用于 fine-tuning 而非 RL problem synthesis。**\n\n6. **Self-Error-Instruct (SEI)** (ACL 2025):\n   - 从 error types 泛化训练数据（而非从个案），解决个案依赖问题。\n   - **同样验证了 error-type-grounded 数据增强的路径。**\n\n7. **WarriorMath** (arXiv 2025): LLM-based defect-aware framework，12.57% 平均提升。\n8. **RV-Syn** (arXiv 2504.20426): 基于结构化函数库的可验证数学推理数据合成，6.3% 提升，静态管线。\n9. **MathSmith** (arXiv 2508.05592): RL-trained problem synthesis with difficulty strategies。\n10. **SvS** (arXiv 2508.14029): Self-play variational synthesis 维持 RLVR 多样性，Pass@32 提升 18-22%。\n11. **Hypothesis-Driven Error Analysis** (arXiv 2604.04386, April 2026): LLM 生成假设识别失败模式并合成针对性 benchmark，将 Llama-3.3-70B 准确率降至 45%。\n12. **Self-Play Information Gain** (arXiv 2603.02218, March 2026): 证明可持续自进化需要 learnable information 逐轮递增，识别 Proposer-Solver-Verifier 三角色。\n\n**调研总结**: 数学推理 self-improvement 领域在 2025-2026 年极度活跃且高度碎片化。符号验证用于过滤（NSRSA）、弱点导向合成（SwS）、验证器支持的问题生成（VHG）、错误类型分类用于训练（LEMMA, SEI）均已独立存在。本 proposal 的核心贡献是将这些已存在的组件整合进一个闭环框架并添加形式化分析，处于**组合/集成(combination/integration)**的位置，而非开辟新方向。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁。** 考虑以下低成本替代方案：\n1. 运行 NSRSA 的 SymPy 符号验证（已开源可用）\n2. 收集错误类型统计（NSRSA 验证器本身已输出错误分类）\n3. 将错误类型作为 prompt conditioning 让 LLM 合成更多该类型问题（无需 GRPO 训练 synthesizer）\n4. 用 NSRSA 的原始 filtering 管线训练\n\n这个 trivial pipeline 不需要 RL-trained synthesizer、不需要 formal convergence proof、不需要 per-category generation budgets，但可能达到类似效果。Proposal 的增量价值理论上在于：(a) GRPO-trained synthesizer 能比 prompt-based 合成产生更精准的针对性问题；(b) formal convergence guarantee 提供理论指导。但 (a) 需要实验证明 GRPO 合成器显著优于 prompt-based 合成（目前未论证），(b) 的理论贡献可能高度依赖于非平凡假设（见下）。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的关键假设：\n\n1. **\"SymPy 能可靠地进行 fine-grained step-level 错误分类\"**：NSRSA 证明了 SymPy 可以做 binary filtering（正确/错误），但将每个错误步骤准确分类为 {arithmetic miscalculation, algebraic manipulation error, logical flow inconsistency, constraint violation} 是一个显著更难的任务。SymPy 本质上是符号计算引擎，不是逻辑推理引擎——对\"logical flow inconsistency\"和\"constraint violation\"的检测能力未经验证。错误分类的准确性直接决定整个 pipeline 的有效性。\n\n2. **\"诊断条件化的合成能产生单调递增的 learnable information gain\"**：这是一个非常强的数学 claim。实际上，self-improvement 会饱和（solver-verifier gap 论文自己就证明了指数收敛到极限），所以\"单调递增\"只在 pre-saturation 阶段可能成立，且需要严格限定假设条件。如果假设条件过强（如要求 perfect 诊断精度、无界问题空间），则定理虽正确但实际意义有限。\n\n3. **\"Error taxonomy conditioning 能有效转化为 targeted problem synthesis\"**：从\"模型在算术计算上犯了很多错\"到\"合成更多需要算术计算的问题来训练它\"看似自然，但现有研究（SwS 的 limitation discussion）指出合成问题往往\"缺乏足够复杂度\"。用 RL (GRPO) 训练 synthesizer 是否能解决这个问题，是未经验证的假设。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中 (偏弱)** —\n   核心贡献是将 NSRSA 的符号诊断 + SwS 的弱点导向合成 + solver-verifier gap 的理论框架组合进一个闭环。但：\n   - NSRSA 已有 step-level 符号验证和错误分类（arXiv 2603.21558）\n   - SwS 已有 weakness-targeted synthesis via RL（NeurIPS 2025）\n   - VHG 已将符号验证器整合进生成循环（arXiv 2605.06660）\n   - LEMMA 和 SEI 已验证 error taxonomy → training data 路径（ACL 2025）\n   - 理论贡献声称\"首次连接 solver-verifier gap 到 diagnostic synthesis\"，但更可能是已有框架的 instantiation 而非独立理论突破\n   \n   **剔除 surface differences 后的真实 novelty delta**: \"用符号诊断的结构化输出 condition RL-trained synthesizer\" —— 这是一个 specific engineering design choice，而非 conceptual advance。如果核心发现是 positive（符号诊断引导的合成优于 LLM 引导的合成），审稿人大概率会说 **\"I would have guessed this\"** —— 因为符号验证比 LLM 验证更精确是常识性认知。\n\n2. **Significance: 中** —\n   研究问题本身（防止 self-improvement collapse + 提高训练数据效率）确实重要，2025-2026 年持续是热点。但：\n   - 如果证明 symbolic diagnosis > LLM diagnosis for synthesis conditioning，影响更多是对已有方法的**增量改进**而非范式转变\n   - 实验设计覆盖 GSM8K → AIME → OlympiadBench 跨度好，但 Qwen3-8B 规模偏小，可推广性到更大模型存疑\n   - 成果的可转移性受限：SymPy 验证主要适用于代数/算术类问题，对几何、组合、数论等数学子领域的覆盖度未知\n\n3. **Related Work: 中-强** —\n   Related work 覆盖面广泛且定位清晰，正确识别了 NSRSA, SwS, VHG, WarriorMath, RV-Syn, MathSmith, SvS, Hypothesis-Driven Error Analysis 等关键竞争工作，并对每个工作的差异化描述基本准确。但：\n   - 遗漏了 LEMMA (ACL 2025) 和 Self-Error-Instruct (ACL 2025)，这两篇直接使用 error taxonomy 构建训练数据，与 proposal 的核心思路高度相关\n   - 对 VHG 的差异化描述（\"verification only for problem validation—not step-level error diagnosis\"）稍显单薄，因为 VHG 的 symbolic verifier 也间接提供了问题有效性的诊断信号\n\n---\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】:\n本 proposal 处于 \"idea 方向站得住脚但内核薄弱\" 的区间。方向正确（symbolic verification for self-improvement 是真实且重要的研究方向），领域调研充分，但核心 novelty 是已有组件的组合/集成（NSRSA 的诊断 + SwS 的合成 + solver-verifier gap 的理论），而非独立的 conceptual advance。三个维度中，**Novelty 是限制上界的主要因素**：如果核心发现是 positive（符号诊断优于 LLM 诊断），审稿人会认为 \"expected\"；如果 negative，paper 的价值更低。形式化收敛保证的 claim 过强（\"单调递增 learnable information gain\"），可能在审稿中被质疑假设的合理性。Trivial alternative（NSRSA filtering + prompt-based targeted synthesis）构成实质威胁，需要实验明确证明 RL-trained synthesizer 的增量价值。\n\n【主要风险】:\n1. **Novelty 不足被拒**：审稿人可能认为 \"symbolic diagnosis → conditioned synthesis\" 是 NSRSA + SwS 的直接拼接，核心 insight \"用更精确的诊断引导更好的合成\" 缺乏 surprise —— 这是最可能的拒稿理由。\n2. **形式化 claim 站不住脚**：\"单调递增 learnable information gain\" 与 solver-verifier gap 论文自身预测的指数收敛极限矛盾；如果形式化分析需要过强假设才能成立，理论贡献会被审稿人视为 vacuous，反而成为减分项。\n```\n\nSources:\n- [NSRSA - Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [SwS - Self-aware Weakness-driven Problem Synthesis in RL for LLM Reasoning](https://openreview.net/forum?id=0jQUNQsZra)\n- [Solver-Verifier Gap Theory (ICLR 2026)](https://openreview.net/pdf?id=Hh7x3c0cZl)\n- [VHG - Verifier-Backed Hard Problem Generation for Mathematical Reasoning](https://arxiv.org/abs/2605.06660)\n- [Self-Play Information Gain](https://arxiv.org/abs/2603.02218)\n- [LEMMA - Learning from Errors for Mathematical Advancement in LLMs](https://arxiv.org/abs/2503.17439)\n- [Self-Error-Instruct](https://arxiv.org/abs/2505.22591)\n- [WarriorMath](https://arxiv.org/pdf/2508.01245)\n- [RV-Syn](https://arxiv.org/abs/2504.20426)\n- [MathSmith](https://arxiv.org/abs/2508.05592)\n- [SvS - Beyond Pass@1](https://arxiv.org/abs/2508.14029)\n- [Hypothesis-Driven Error Analysis](https://arxiv.org/abs/2604.04386)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Symbolic Diagnostic Verification for Targeted Math Self-Improvement\n\n## Core Problem\n\nCurrent self-improvement loops for math reasoning either use symbolic verification only for filtering (discarding rich diagnostic information) or use LLM-based weakness identification (which is unreliable and cannot prevent model collapse). Can step-level symbolic error diagnosis drive targeted problem synthesis to create provably stable, maximally informative self-improvement?\n\n## Research Opportunity\n\nNSRSA (March 2026) demonstrates that SymPy-based step-level verification rejects ~34% of 'lucky guess' solutions and prevents collapse on GSM8K, but completely discards the diagnostic signal after filtering. Simultaneously, SwS (NeurIPS 2025) shows weakness-targeted synthesis yields 10% gains, but its authors explicitly acknowledge that behavioral weakness identification is insufficient and synthetic problems 'lack sufficient complexity.' The solver-verifier gap theory (ICLR 2026) predicts that external symbolic verification uniquely enables sustained self-improvement because it cannot be 'fooled' by the generator. The convergence of these three threads creates an immediate opportunity: use symbolic verification not merely as a gate but as a structured diagnostic guide that drives targeted, formally verifiable problem generation.\n\n## Research Landscape\n\nSelf-improving math reasoning is actively studied but fragmented. NSRSA (2026) achieves 91.0% on GSM8K via symbolic filtering but only tests on GSM8K/MATH-500 and discards error diagnostics. SwS (NeurIPS 2025) achieves 10% average gains via behavioral weakness targeting but uses LLM-based diagnosis and doesn't address collapse. WarriorMath (2025) achieves 12.57% via LLM-based defect awareness. RV-Syn (arXiv 2026) generates verifiable data from computational graphs with 6.3% gains but is a static pipeline. MathSmith (2025) uses RL-trained problem synthesis with difficulty strategies but not diagnostic feedback. VHG (May 2026, concurrent) introduces three-party self-play with symbolic and LLM verifiers for hard problem generation, achieving 69.0% pass@1 on general math benchmarks, but uses verification only for problem validation—not step-level error diagnosis to guide synthesis. Hypothesis-Driven Error Analysis (April 2026, concurrent) uses LLM-generated hypotheses about failure modes to synthesize targeted benchmark problems but lacks symbolic grounding and focuses on evaluation rather than training. SvS (2025) uses variational problem synthesis to sustain RLVR diversity but does not target specific weaknesses. The theoretical foundation exists: the solver-verifier gap paper (ICLR 2026) proves self-improvement requires asymmetric verification, and the self-play information gain paper (March 2026) argues each iteration must increase learnable information. The missing piece is a unified framework where symbolic verification both prevents collapse AND guides what to generate through structured error diagnosis, closing the loop between diagnosis and synthesis with formal guarantees.\n\n## Proposed Approach\n\nWe propose SymDiag, a closed-loop self-improvement framework that transforms SymPy-based step-level verification from a binary filter into a structured diagnostic engine. In each iteration, a Qwen3-8B base model generates solutions, and the symbolic verifier classifies every erroneous step into a fine-grained taxonomy (arithmetic miscalculation, algebraic manipulation error, logical flow inconsistency, constraint violation) with precise step localization and severity scoring. This error taxonomy conditions an RL-trained problem synthesizer (using GRPO) to generate new problems that specifically probe the model's diagnosed weaknesses, with per-category generation budgets allocated by error frequency and downstream impact. We provide formal convergence analysis showing that symbolic diagnostic verification maintains a provable solver-verifier gap (preventing model collapse per ICLR 2026 theory) while diagnostic-conditioned synthesis ensures monotonically increasing learnable information gain per iteration (per the self-play information gain framework). We evaluate over 5 self-improvement iterations on GSM8K, MATH-500, AIME 2024-2025, and OlympiadBench, comparing against NSRSA (filter-only), SwS (LLM-diagnosed weakness targeting), and VHG (verifier-backed generation) baselines.\n\n## Detailed Description\n\nCurrent self-improvement approaches for mathematical reasoning either discard rich diagnostic information after symbolic verification (NSRSA) or rely on unreliable LLM-based weakness identification (SwS, WarriorMath). We introduce SymDiag, a closed-loop framework that repurposes SymPy-based step-level verification as a structured diagnostic engine driving targeted problem synthesis. Our symbolic verifier classifies solution errors into a fine-grained taxonomy—arithmetic miscalculation, algebraic manipulation failure, logical flow inconsistency, and constraint violation—with precise step localization and severity scoring. This taxonomy conditions a GRPO-trained problem synthesizer to generate problems specifically probing diagnosed weaknesses, with per-category budgets allocated by error frequency and impact. We provide the first formal analysis connecting the solver-verifier gap theory (ICLR 2026) to diagnostic-driven synthesis, proving that symbolic diagnosis maintains asymmetric verification preventing collapse while ensuring monotonically increasing learnable information gain per iteration. Experiments across GSM8K, MATH-500, AIME 2024-2025, and OlympiadBench compare against filter-only (NSRSA), LLM-diagnosed (SwS), and verifier-backed generation (VHG) baselines. Two concurrent works use verifiers for validation only (VHG) or LLM-based diagnosis (Hypothesis-Driven Error Analysis); SymDiag uniquely combines symbolic diagnostics with formal convergence guarantees.\n\n## Key References\n\n- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment (arXiv 2026)\n- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)\n- Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)\n- Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain (arXiv 2026)\n- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)\n- RV-Syn: Rational and Verifiable Mathematical Reasoning Data Synthesis based on Structured Function Library (arXiv 2026)\n- Verifier-Backed Hard Problem Generation for Mathematical Reasoning (arXiv 2026)\n- Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis (arXiv 2026)\n- MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy (arXiv 2025)\n- Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)\n- V-STaR: Training Verifiers for Self-Taught Reasoners (arXiv 2024)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~3000 H100-hours (1600 for 5 RL iterations on 8×H100, 800 for baseline reproduction, 600 for ablations), timeline: 8-10 weeks (2 weeks implementation, 5 weeks experiments, 2 weeks writing), estimated_gpu_cost: $7,500 (at ~$2.50/H100-hr spot pricing)\n- **human_in_loop**: gpu_hours: ~2500 H100-hours (Claude-assisted hyperparameter selection reduces wasted runs), timeline: 6-8 weeks, claude_api_cost: $300-500, estimated_gpu_cost: $6,250\n- **auto_research**: gpu_hours: ~4000 H100-hours (automated exploration of error taxonomy granularities and synthesis strategies), timeline: 4-6 weeks, claude_api_cost: $1,000-1,500, estimated_gpu_cost: $10,000, speed_bottleneck: RL training wall-clock time: ~40 hours per self-improvement iteration on 8×H100s; 5 sequential iterations impose a ~200hr critical path\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T08:24:25.332Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:24:25.332Z",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T08:24:25.346Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have a comprehensive picture of the research landscape. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [NSRSA] Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment (arXiv 2603.21558, March 2026): 用 SymPy 做步骤级符号验证过滤训练数据，拒绝 ~34% 的"lucky guess"解。在 GSM8K 上用 Qwen3-4B 评估。确认 proposal 描述准确——NSRSA 确实在过滤后丢弃了诊断信息。
- [SwS] Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025, OpenReview): 基于行为弱点的定向问题合成，7B 模型获得 10% 平均增益。使用 LLM-based 弱点识别，非符号化。Proposal 描述准确。
- [Solver-Verifier Gap] Theoretical Modeling of LLM Self-Improvement Training Dynamics (ICLR 2026, arXiv 2507.00075): 理论建模 solver-verifier gap 驱动自改进，已发表于 ICLR 2026。Proposal 引用准确。
- [Self-Play Information Gain] Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain (arXiv 2603.02218, March 2026): 揭示可持续自进化需要每轮迭代增加可学习信息。Proposer/Solver/Verifier 三角色框架。描述准确。
- [VHG] Verifier-Backed Hard Problem Generation (arXiv 2605.06660, May 2026): 三方自博弈 + 符号/LLM 验证器，pass@1 从 56.8% 提升到 69.0%。验证器用于问题有效性验证，非步骤级诊断。描述准确。
- [Hypothesis-Driven Error Analysis] Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis (arXiv 2604.04386, April 2026): 用 LLM 生成关于失败模式的假设 → 合成目标问题。将 Llama-3.3-70B 准确率从 77% 降至 45%。聚焦评估而非训练。
- [WarriorMath] (arXiv 2508.01245, 2025): 缺陷感知框架，平均提升 12.57%。使用 LLM 协作的问题合成+渐进训练。
- [Self-Error-Instruct] Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025): **Proposal 未提及但高度相关。** 通过错误类型聚类(error keyphrases → clustering → error types) 来泛化错误案例，合成针对性训练数据。核心思路（错误分类→定向合成）与 SymDiag 非常接近，只是用 LLM (GPT-4o) 而非符号化方法做错误分类。
- [Adaptive Problem Generation via Symbolic Representations] (arXiv 2602.19187, Feb 2026): **Proposal 未提及但高度相关。** 在符号空间（SymPy/SMT）做问题表示和修改，闭环框架通过 prompt optimization 学习修改策略，自适应调整问题难度。与 SymDiag 的"符号化+闭环"主题高度重合。
- [FoVer] Training Step-Level Reasoning Verifiers with Formal Verification Tools (arXiv 2505.15960, 2025): 用 Z3/Isabelle 自动标注步骤级错误标签训练 PRM。与 SymDiag 的步骤级符号验证主题相关。
- [RV-Syn] (arXiv 2504.20426, 2026): 从结构化函数库构建计算图合成可验证数据，6.3% 增益。静态管线，非闭环。
- [MathSmith] (arXiv 2508.05592, 2025): RL 训练的问题合成策略，9种难度策略。无诊断反馈。

**调研总结**: 数学推理自改进是 2025-2026 年极度活跃的研究方向，存在多条并行线路：(1) 符号验证用于数据过滤(NSRSA)；(2) 弱点/缺陷感知的定向合成(SwS, WarriorMath, Self-Error-Instruct)；(3) 符号空间的问题生成(RV-Syn, Adaptive Problem Generation)；(4) 验证器驱动的自博弈(VHG)；(5) 自改进的理论分析(Solver-Verifier Gap, Self-Play Information Gain)。SymDiag 的定位是将线路(1)和(2)桥接起来——用符号诊断替代 LLM-based 弱点识别来驱动合成。**但 Self-Error-Instruct (ACL 2025) 已经在做"错误分类→定向合成"这件事，Adaptive Problem Generation (Feb 2026) 已经在做"符号空间+闭环"这件事。SymDiag 的真正增量是"符号化的错误分类"而非"错误分类→定向合成"这个范式本身。**

【Trivial Alternative 检验】:
存在两个 trivial-combination baseline 构成威胁：
1. **NSRSA 过滤 + SwS 合成的简单管线拼接**：用 NSRSA 的符号验证做数据过滤，用 SwS 的行为弱点识别做定向合成。这个组合不需要 SymDiag 提出的"诊断引擎"和"错误分类学"，但可能获得大部分收益。SymDiag 的增量价值在于：符号诊断比 LLM 行为诊断更精确、更可靠、不会被模型 collapse 影响。但这个增量有多大需要实证——如果 LLM-based 弱点识别已经"够好"，符号诊断的边际价值可能有限。
2. **Self-Error-Instruct 的思路 + SymPy 替代 GPT-4o**：Self-Error-Instruct 已经在做错误类型聚类→定向合成，SymDiag 本质上是用 SymPy 替代 GPT-4o 做错误分类。如果 SymPy 的分类能力有限（见下文前提假设检验），这个替换的价值可能不大。

**增量价值的关键论点**是：符号验证不会随模型能力提升而失效（solver-verifier gap 理论支持），而 LLM-based 诊断可能被 collapse 污染。这是一个合理的理论论点，但其实际影响大小未知。

【前提假设检验】:
核心逻辑链中有 3 个未经验证的关键假设：

1. **"SymPy 能可靠地将错误分类为 fine-grained taxonomy"**：这是最大的假设风险。SymPy 可以检测算术错误（arithmetic miscalculation），但要区分 "algebraic manipulation error" vs "logical flow inconsistency" vs "constraint violation" 需要对推理步骤做深层语义理解。SymPy 本质上是一个符号计算引擎，不是一个推理理解引擎。对于 AIME/OlympiadBench 级别的复杂推理（组合数学、数论证明、几何），SymPy 的步骤级诊断能力极其有限。Proposal 在这一点上没有给出任何可行性论证。

2. **"错误分类可以有意义地指导问题合成"**：即使知道模型在"代数变换"上犯错多，如何让 GRPO-trained synthesizer 生成能精准"probe"代数变换弱点的问题？从错误类型到有效训练问题的映射是一个 non-trivial 的跳跃。"per-category generation budgets allocated by error frequency and impact" 听起来合理，但实际上这种 allocation 可能不如简单的基于难度的采样。

3. **"单调递增的可学习信息增益"这一形式化保证**：Proposal 声称提供"the first formal analysis connecting solver-verifier gap theory to diagnostic-driven synthesis"，并证明"monotonically increasing learnable information gain per iteration"。这是一个非常强的数学声明。在实际系统中，信息增益取决于错误分类的准确性、合成问题的质量、模型学习动态等多个因素。将这些因素严格形式化并证明单调性，要么需要极度简化的假设（使定理无实际意义），要么是无法证明的。

【3 维度打分】:

1. **Novelty: 中偏弱** — SymDiag 的核心思路"把符号验证从过滤器变成诊断引擎来驱动定向合成"是一个合理的 gap-filling 贡献，但 novelty 的真实 delta 有限：
   - Self-Error-Instruct (ACL 2025) 已经实现了"错误分类→定向合成"这个范式，只是用 LLM 而非符号方法做分类。SymDiag 的增量是"换一种分类工具"。
   - Adaptive Problem Generation via Symbolic Representations (Feb 2026) 已经在符号空间做闭环问题生成。
   - VHG (May 2026) 已经把符号验证器融入问题生成的自博弈循环。
   - 剥离 surface differences 后，SymDiag 的核心新意在于"SymPy 错误分类学 + 诊断条件化合成"这个具体实例。这更接近 incremental combination 而非 paradigm shift。
   - 如果这个 idea positive，审稿人大概率会说 "I would have guessed that using diagnostic info helps"——因为"更多信息 > 更少信息"是直觉上显而易见的。

2. **Significance: 中** — 研究问题本身（数学推理自改进）非常重要且时效性强。如果 SymDiag 的方法确实有效：
   - 对实践有价值：提供了一种不依赖 LLM 做弱点诊断的替代方案
   - 理论贡献（形式化连接 solver-verifier gap 与诊断驱动合成）有潜在价值
   - 但受限于符号验证的适用范围：仅适用于可符号化验证的数学问题，不具备向更广泛推理任务的泛化性
   - 增量改进的幅度可能有限——NSRSA 的过滤 vs. 诊断驱动合成的差距可能不如预期大

3. **Related Work: 中偏弱** — Proposal 列举了 11 篇参考文献，覆盖面看似广泛，但存在关键遗漏：
   - **未提及 Self-Error-Instruct (ACL 2025)**：这是最直接的竞争对手，同样做"错误分类→定向合成"。遗漏此文显著削弱了 novelty claim 的可信度。
   - **未提及 Adaptive Problem Generation via Symbolic Representations (Feb 2026)**：同样在符号空间做闭环问题生成。
   - **未提及 FoVer (2025)**：同样用形式化工具做步骤级错误标注。
   - 这些遗漏不是边缘文献——它们是直接挑战 SymDiag novelty 定位的核心竞争者。审稿人如果发现这些遗漏，会严重质疑 contribution 的新颖性。

【概率估计】: 20% - 30%，中位 25%

【估计理由】:
- Novelty 维度是主要限制因素。核心思路（错误分类→定向合成）已有 Self-Error-Instruct 做过，符号空间闭环已有 Adaptive Problem Generation 做过。SymDiag 的真正增量——"符号化的错误分类替代 LLM-based 分类"——是一个有价值但 incremental 的贡献。
- 关键前提假设（SymPy 能做 fine-grained error taxonomy）缺乏论证，且在复杂数学推理上可能不成立。
- Significance 落在 "timely but incremental" 区间：如果 positive，审稿人更可能说 "makes sense, not surprising" 而非 "surprising, didn't expect that"。
- Related work 遗漏了直接竞争者，如果审稿人熟悉 Self-Error-Instruct 或 Adaptive Problem Generation，会显著降低对 novelty 的评价。
- 理论贡献（形式化保证）如果真的能严格证明会是亮点，但 "monotonically increasing information gain" 的声明过强，可能引发审稿人质疑。
- Proposal 的工程质量和文献调研的全面性（对已引文献的描述准确）构成一定的下限保障。

【主要风险】:
1. **Novelty 被判为 incremental combination**：Self-Error-Instruct + 符号验证 ≈ SymDiag 的核心贡献；审稿人可能认为这只是将已有组件（NSRSA的符号验证 + SwS/Self-Error-Instruct的错误分类→合成范式）拼接在一起。
2. **SymPy fine-grained error taxonomy 的可行性**：如果审稿人质疑 SymPy 在 AIME/Olympiad 级别问题上做 "logical flow inconsistency" vs "constraint violation" 分类的可靠性，整个方法的根基将受到动摇——这直接影响核心 contribution 的成立。
```

Sources:
- [NSRSA - Stabilizing Iterative Self-Training with Verified Reasoning](https://arxiv.org/abs/2603.21558)
- [SwS - Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)
- [Self-Play Information Gain](https://arxiv.org/abs/2603.02218)
- [VHG - Verifier-Backed Hard Problem Generation](https://arxiv.org/abs/2605.06660)
- [Hypothesis-Driven Error Analysis](https://arxiv.org/abs/2604.04386)
- [Self-Error-Instruct (ACL 2025)](https://arxiv.org/abs/2505.22591)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [FoVer - Training Step-Level Reasoning Verifiers](https://arxiv.org/abs/2505.15960)
- [RV-Syn](https://arxiv.org/abs/2504.20426)
- [MathSmith](https://arxiv.org/abs/2508.05592)
- [WarriorMath](https://arxiv.org/abs/2508.01245)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

1. NSRSA (arXiv 2603.21558, March 2026): 使用 SymPy 进行 step-level 符号验证来过滤自训练数据，在 GSM8K 上用 Qwen3-4B-Thinking 做了 5 轮迭代，拒绝了约 34% 的"lucky guess"解答，DPO reward accuracy 从 46% 提升到 63%，MATH-500 cross-task transfer +5.7pp。但仅在 GSM8K/MATH-500 上测试，验证后的诊断信息被丢弃。与本 proposal 的关系：SymDiag 声称在 NSRSA 基础上利用被丢弃的诊断信号——这一 gap 是真实存在的。

2. SwS (NeurIPS 2025, OpenReview): 微软出品，在 RL 预训练阶段记录模型持续失败的问题，按类别分组提取共性概念，合成针对性新问题并按 budget 分配。在 Qwen2.5 (7B/32B) 上取得约 10%/7.7% 平均提升。使用 LLM-based 的弱点识别。与本 proposal 的关系：SymDiag 声称用 symbolic diagnosis 替代 SwS 的 LLM-based diagnosis，这是核心差异化点。

3. Solver-Verifier Gap Theory (ICLR 2026, arXiv 2507.00075): 理论建模 LLM 自改进的训练动态，证明 solver-verifier 能力差距决定自改进的天花板，accuracy 呈指数趋近极限。与本 proposal 的关系：SymDiag 声称提供"连接 solver-verifier gap 理论与 diagnostic-driven synthesis 的首个形式化分析"——这是一个非常强的 claim。

4. VHG (arXiv 2605.06660, May 2026, concurrent): 三方自博弈（setter-solver-verifier），使用 symbolic 和 LLM verifiers 来验证生成问题的有效性和难度，在多个 benchmark 上取得 56.8%→69.0% pass@1 提升。但 verifier 只用于问题验证，不做 step-level 错误诊断。与本 proposal 的关系：VHG 是最直接的竞争者，但确实不做 step-level error diagnosis → synthesis conditioning。

5. WarriorMath (arXiv 2025): 用 LLM committee 评估缺陷，保留模型失败的数据进行训练，平均提升 12.57%。与本 proposal 的关系：同样是"defect-aware"思路但用 LLM-based 评估，SymDiag 声称 symbolic grounding 更可靠。

6. Hypothesis-Driven Error Analysis (arXiv 2604.04386, April 2026, concurrent): 用 LLM 生成关于失败模式的假说来合成针对性 benchmark 问题，将 Llama-3.3-70B-Instruct 的准确率从 77% 降低到 45%。与本 proposal 的关系：类似的"诊断→合成"思路但缺乏 symbolic grounding，且专注 evaluation 而非 training。

7. Self-Play Information Gain (arXiv 2603.02218, March 2026): 证明可持续自进化需要每轮迭代增加 learnable information，提出 Epiplexity 度量。与本 proposal 的关系：SymDiag 引用其理论框架声称"monotonically increasing learnable information gain"。

8. RV-Syn (arXiv 2504.20426, 2026): 从结构化函数库构建 computational graphs 作为可验证解题蓝图，在 LLaMA-3-8B 上 +6.3%。但是静态 pipeline，不做迭代自改进。

9. MathSmith (arXiv 2508.05592, 2025): RL 训练的问题合成策略，包含 weakness-focused variant generation 模块。

- **调研总结**: 数学推理自改进领域在 2025-2026 年极其拥挤。核心赛道包括：(a) 符号验证用于过滤（NSRSA），(b) 弱点识别驱动合成（SwS, WarriorMath），(c) RL 训练的问题生成（MathSmith, VHG），(d) 理论建模（solver-verifier gap, self-play information gain）。SymDiag 声称占据的位置是"(a)+(b)+(d) 的交叉点：symbolic diagnostic + targeted synthesis + formal guarantee"，这个交叉点确实尚未被直接占据，但各组件均已独立存在。


【Trivial Alternative 检验】:

**存在明确的 trivial alternative 威胁。** 最直接的低成本替代方案是：

1. **NSRSA filtering + SwS-style category-level weakness targeting**：在 NSRSA 的 symbolic 过滤之后，简单统计哪些**问题类别**（代数、几何、组合等）的通过率最低，然后像 SwS 那样按类别 budget 生成更多该类问题。这不需要 step-level error taxonomy，但可能捕获大部分收益。

2. **NSRSA + 简单 error counting**：统计 SymPy 验证拒绝的解答中，哪一步被拒绝次数最多（step position），生成在相应步骤复杂度上加大难度的问题。不需要 fine-grained error taxonomy。

SymDiag 的增量价值取决于一个关键假设：**知道模型"为什么犯错"（error type: arithmetic vs. algebraic vs. logical）比知道"在什么问题上犯错"（problem category）能提供显著更好的合成信号。** 但这个假设没有任何先验理论或实证支持。如果 error type conditioning 相对于 problem category conditioning 只带来边际改进，那么整个框架的 added value 会很有限。


【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的关键假设：

1. **SymPy 能可靠地将错误分类到 proposed taxonomy（arithmetic miscalculation / algebraic manipulation / logical flow inconsistency / constraint violation）**。SymPy 擅长验证算术和代数等式是否成立，但"logical flow inconsistency"和"constraint violation"的自动分类远非 trivial——这需要理解问题语义和推理意图，可能已经超出了纯 symbolic computation 的能力边界。Proposal 没有讨论这个分类的准确率会是多少，也没有说明如何处理分类错误。

2. **Error taxonomy conditioning 能有效转化为有区分度的问题生成**。即使诊断出"arithmetic miscalculation"，如何让 GRPO-trained synthesizer 生成专门考察 arithmetic accuracy 而非其他能力的问题？这个 conditioning mechanism 的有效性是未知的。用 GRPO reward 来激励 synthesizer 生成"provoke specific error types"的问题，reward signal 如何设计？Proposal 没有充分说明。

3. **Formal convergence guarantee 的可交付性**。Proposal 声称将证明"symbolic diagnosis maintains asymmetric verification preventing collapse while ensuring monotonically increasing learnable information gain per iteration"。这把 solver-verifier gap theory（关于 self-improvement dynamics）和 self-play information gain theory（关于 learnable information）两个独立理论框架连接起来，并额外加入 error-taxonomy conditioning 的约束。这要么需要非常强的新理论贡献，要么会退化为对已有理论的 trivial 复述（"因为我们用了 symbolic verifier 所以 gap 存在"——这 NSRSA 已经隐含了）。

4. **SymPy verification 能 scale 到 AIME/OlympiadBench 难度**。NSRSA 仅在 GSM8K（小学数学）和 MATH-500 上验证。AIME 和 OlympiadBench 涉及数论、组合、几何等需要远更复杂 symbolic reasoning 的领域，SymPy 的 step-level verification 在这些问题上的覆盖率和准确率是完全未知的。


【3 维度打分】:

1. **Novelty: 中偏弱** — SymDiag 的核心贡献是将 symbolic verification 的 diagnostic 信号（而非仅 binary filter）用于 condition 问题合成。这个组合确实尚未被直接实现，但：
   - NSRSA 已经实现了 SymPy step-level verification（诊断信息只需"不丢弃"即可获得）
   - SwS 已经实现了 weakness-targeted synthesis with budget allocation
   - VHG 已经实现了 verifier-backed problem generation with RL
   - 核心"新"的部分是 error taxonomy → synthesis conditioning 这个 bridging mechanism，但这是一个相对 straightforward 的工程组合，不涉及方法论层面的根本创新
   - 所声称的 formal convergence guarantee 如果真正 novel 且 non-trivial，可以显著提升 novelty，但基于前提假设检验中的分析，很可能会退化为对已有理论的 direct application
   - 最关键的判断：**如果核心发现是 positive（error taxonomy conditioning 比 category-level targeting 效果好），审稿人的反应更可能是"I would have guessed this"而非"surprising"**

2. **Significance: 中** — 问题方向完全成立：数学推理自改进是 2025-2026 年最热门的研究方向之一，"don't discard diagnostic information"的 insight 是合理的。但：
   - 预期增量改进的幅度有限（从 NSRSA 的 filter-only 到 diagnostic-conditioned synthesis，改进空间受限于 error taxonomy 的有效性）
   - 该框架的 generalizability 受限于 SymPy 可验证的问题范围——对于不容易 symbolic verify 的推理任务（如几何直觉、创造性 problem-solving），该框架不适用
   - 如果 formal theory 部分能做得扎实，significance 可以上升到中偏强

3. **Related Work: 强** — Proposal 对 related work 的覆盖非常全面，包括：
   - 核心前置工作（NSRSA, SwS, Solver-Verifier Gap Theory, Self-Play Information Gain）
   - 直接竞争者（VHG, WarriorMath, MathSmith, RV-Syn）
   - 最新 concurrent work（VHG May 2026, Hypothesis-Driven Error Analysis April 2026）
   - 差异化定位清晰（symbolic diagnosis vs. LLM-based diagnosis, diagnostic-conditioned synthesis vs. filter-only）
   - 经调研验证，proposal 对各论文的描述基本准确（NSRSA 的 34% 拒绝率、SwS 的 10% 提升、VHG 的 69% pass@1 等均可核实）


【概率估计】: 18% - 28%，中位 23%

【估计理由】:
- **Novelty 是限制上界的主要维度**。核心贡献是 well-motivated 的工程组合（symbolic diagnosis + targeted synthesis），但缺乏方法论层面的根本创新。在一个极度拥挤的领域中（2025-2026 年有超过 10 篇直接相关工作），"把 A 的诊断信号接入 B 的合成框架"很难让审稿人感到 surprised。
- **Trivial alternative 威胁真实存在**。NSRSA filtering + SwS-style category targeting 是一个更简单、更直接的 baseline，如果实验中不能证明 fine-grained error taxonomy conditioning 显著优于 category-level targeting，整篇论文的核心 claim 就站不住。
- **Formal convergence guarantee 是 high risk/high reward 的赌注**。如果能交付有实质意义的新理论结果（不是 trivial application of existing theory），概率可以上探 30%+；如果退化为"因为 symbolic verifier 所以 gap 存在"这种已知结论，则反而会被审稿人视为 overclaim。
- **Related work 覆盖优秀**，不会因为 missing baselines 被拒，这提供了一个可靠的下限。
- 概率没有更低是因为：问题方向完全正确，related work 极其完善，且 symbolic diagnosis → synthesis 这个特定 niche 确实没有被现有工作直接占据。

【主要风险】:
1. **Novelty 不足 / Trivial alternative**：审稿人可能认为"使用已有 symbolic verifier 的诊断信息来 condition 已有的 weakness-targeted synthesis"是一个 obvious next step，不构成足够的学术贡献。如果实验中 error-taxonomy-conditioned synthesis 相对 problem-category-conditioned synthesis 的提升不显著，核心 claim 直接崩塌。
2. **Formal guarantee overclaim**：如果 convergence analysis 只是对 solver-verifier gap theory 的 trivial 套用（"我们用了 symbolic verifier → gap 存在 → 不 collapse"），审稿人会认为这是 overclaim 而非 contribution；如果要做 non-trivial 的理论，则交付风险极高。
```

Sources:
- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)
- [VHG: Verifier-Backed Hard Problem Generation](https://arxiv.org/abs/2605.06660)
- [WarriorMath: Defect-aware Framework](https://arxiv.org/pdf/2508.01245)
- [Hypothesis-Driven Error Analysis for Math Problem Generation](https://arxiv.org/html/2604.04386v1)
- [Self-Play Information Gain](https://arxiv.org/abs/2603.02218)
- [RV-Syn: Rational and Verifiable Mathematical Reasoning Data Synthesis](https://arxiv.org/abs/2504.20426)
- [MathSmith: Synthetic Problem Generation with Reinforced Policy](https://arxiv.org/abs/2508.05592)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough research to provide a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

1. **NSRSA — "Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment"** (arXiv 2603.21558, March 2026):
   - 已实现 SymPy 级别的 step-level 符号验证，包含算术运算校验、逻辑流一致性检查、领域约束验证。
   - 在 GSM8K 上 Qwen3-4B-Thinking 经过 5 轮迭代达到 91.0%，filtering 拒绝了 ~34% 的"幸运猜测"。
   - **关键：NSRSA 的符号验证器已经能分类错误类型（arithmetic, logical flow, domain constraints），只是将其用于过滤而非引导合成。本 proposal 的核心差异化 claim "NSRSA 丢弃了诊断信号" 成立，但从"诊断用于过滤"到"诊断用于引导合成"是一个 engineering-level 的扩展，不是 conceptual breakthrough。**

2. **SwS — "Self-aware Weakness-driven Problem Synthesis in RL for LLM Reasoning"** (NeurIPS 2025, OpenReview):
   - 通过模型 RL 训练过程中持续失败的问题提取核心 weakness concepts，合成针对性训练问题。
   - 7B/32B 模型在 8 个 benchmark 上平均提升 10%/7.7%。
   - 使用 LLM-based 弱点识别（behavioral level），不使用符号验证，不处理 collapse 问题。
   - **与本 proposal 的关系：proposal 的核心 claim 是将 SwS 的 LLM-based 弱点诊断替换为符号诊断——这是一个模块化替换(modular substitution)。**

3. **Solver-Verifier Gap Theory** (ICLR 2026, OpenReview):
   - 建立了 self-improvement 的理论框架，证明持续提升需要 solver 与 verifier 之间的能力差距。
   - 预测 self-improvement 的极限遵循指数收敛律。
   - **本 proposal 声称要"首次"将此理论连接到 diagnostic-driven synthesis——但原论文的框架已经足够通用，将其应用到特定场景更多是 instantiation 而非理论突破。**

4. **VHG — "Verifier-Backed Hard Problem Generation"** (arXiv 2605.06660, May 2026, 并行工作):
   - 三方 self-play：setter-solver-verifier，同时使用 Hard (symbolic) 和 Soft (LLM) verifier。
   - 在 general math benchmark 上将 pass@1 从 56.8% 提升到 69.0%。
   - **VHG 已经将符号验证器整合进问题生成循环，只是验证用于 problem validation 而非 step-level error diagnosis。SymDiag 的差异化在于 step-level 诊断 → conditioned synthesis，但这个差异在概念层面比较窄。**

5. **LEMMA — "Learning from Errors for Mathematical Advancement"** (ACL Findings 2025):
   - 已实现错误类型分类(error-type taxonomy)，构建 error-corrective trajectories 用于训练。
   - **直接证明了 error taxonomy → training data 的路径已被探索，虽然 LEMMA 用于 fine-tuning 而非 RL problem synthesis。**

6. **Self-Error-Instruct (SEI)** (ACL 2025):
   - 从 error types 泛化训练数据（而非从个案），解决个案依赖问题。
   - **同样验证了 error-type-grounded 数据增强的路径。**

7. **WarriorMath** (arXiv 2025): LLM-based defect-aware framework，12.57% 平均提升。
8. **RV-Syn** (arXiv 2504.20426): 基于结构化函数库的可验证数学推理数据合成，6.3% 提升，静态管线。
9. **MathSmith** (arXiv 2508.05592): RL-trained problem synthesis with difficulty strategies。
10. **SvS** (arXiv 2508.14029): Self-play variational synthesis 维持 RLVR 多样性，Pass@32 提升 18-22%。
11. **Hypothesis-Driven Error Analysis** (arXiv 2604.04386, April 2026): LLM 生成假设识别失败模式并合成针对性 benchmark，将 Llama-3.3-70B 准确率降至 45%。
12. **Self-Play Information Gain** (arXiv 2603.02218, March 2026): 证明可持续自进化需要 learnable information 逐轮递增，识别 Proposer-Solver-Verifier 三角色。

**调研总结**: 数学推理 self-improvement 领域在 2025-2026 年极度活跃且高度碎片化。符号验证用于过滤（NSRSA）、弱点导向合成（SwS）、验证器支持的问题生成（VHG）、错误类型分类用于训练（LEMMA, SEI）均已独立存在。本 proposal 的核心贡献是将这些已存在的组件整合进一个闭环框架并添加形式化分析，处于**组合/集成(combination/integration)**的位置，而非开辟新方向。

---

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁。** 考虑以下低成本替代方案：
1. 运行 NSRSA 的 SymPy 符号验证（已开源可用）
2. 收集错误类型统计（NSRSA 验证器本身已输出错误分类）
3. 将错误类型作为 prompt conditioning 让 LLM 合成更多该类型问题（无需 GRPO 训练 synthesizer）
4. 用 NSRSA 的原始 filtering 管线训练

这个 trivial pipeline 不需要 RL-trained synthesizer、不需要 formal convergence proof、不需要 per-category generation budgets，但可能达到类似效果。Proposal 的增量价值理论上在于：(a) GRPO-trained synthesizer 能比 prompt-based 合成产生更精准的针对性问题；(b) formal convergence guarantee 提供理论指导。但 (a) 需要实验证明 GRPO 合成器显著优于 prompt-based 合成（目前未论证），(b) 的理论贡献可能高度依赖于非平凡假设（见下）。

---

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的关键假设：

1. **"SymPy 能可靠地进行 fine-grained step-level 错误分类"**：NSRSA 证明了 SymPy 可以做 binary filtering（正确/错误），但将每个错误步骤准确分类为 {arithmetic miscalculation, algebraic manipulation error, logical flow inconsistency, constraint violation} 是一个显著更难的任务。SymPy 本质上是符号计算引擎，不是逻辑推理引擎——对"logical flow inconsistency"和"constraint violation"的检测能力未经验证。错误分类的准确性直接决定整个 pipeline 的有效性。

2. **"诊断条件化的合成能产生单调递增的 learnable information gain"**：这是一个非常强的数学 claim。实际上，self-improvement 会饱和（solver-verifier gap 论文自己就证明了指数收敛到极限），所以"单调递增"只在 pre-saturation 阶段可能成立，且需要严格限定假设条件。如果假设条件过强（如要求 perfect 诊断精度、无界问题空间），则定理虽正确但实际意义有限。

3. **"Error taxonomy conditioning 能有效转化为 targeted problem synthesis"**：从"模型在算术计算上犯了很多错"到"合成更多需要算术计算的问题来训练它"看似自然，但现有研究（SwS 的 limitation discussion）指出合成问题往往"缺乏足够复杂度"。用 RL (GRPO) 训练 synthesizer 是否能解决这个问题，是未经验证的假设。

---

【3 维度打分】:

1. **Novelty: 弱-中 (偏弱)** —
   核心贡献是将 NSRSA 的符号诊断 + SwS 的弱点导向合成 + solver-verifier gap 的理论框架组合进一个闭环。但：
   - NSRSA 已有 step-level 符号验证和错误分类（arXiv 2603.21558）
   - SwS 已有 weakness-targeted synthesis via RL（NeurIPS 2025）
   - VHG 已将符号验证器整合进生成循环（arXiv 2605.06660）
   - LEMMA 和 SEI 已验证 error taxonomy → training data 路径（ACL 2025）
   - 理论贡献声称"首次连接 solver-verifier gap 到 diagnostic synthesis"，但更可能是已有框架的 instantiation 而非独立理论突破
   
   **剔除 surface differences 后的真实 novelty delta**: "用符号诊断的结构化输出 condition RL-trained synthesizer" —— 这是一个 specific engineering design choice，而非 conceptual advance。如果核心发现是 positive（符号诊断引导的合成优于 LLM 引导的合成），审稿人大概率会说 **"I would have guessed this"** —— 因为符号验证比 LLM 验证更精确是常识性认知。

2. **Significance: 中** —
   研究问题本身（防止 self-improvement collapse + 提高训练数据效率）确实重要，2025-2026 年持续是热点。但：
   - 如果证明 symbolic diagnosis > LLM diagnosis for synthesis conditioning，影响更多是对已有方法的**增量改进**而非范式转变
   - 实验设计覆盖 GSM8K → AIME → OlympiadBench 跨度好，但 Qwen3-8B 规模偏小，可推广性到更大模型存疑
   - 成果的可转移性受限：SymPy 验证主要适用于代数/算术类问题，对几何、组合、数论等数学子领域的覆盖度未知

3. **Related Work: 中-强** —
   Related work 覆盖面广泛且定位清晰，正确识别了 NSRSA, SwS, VHG, WarriorMath, RV-Syn, MathSmith, SvS, Hypothesis-Driven Error Analysis 等关键竞争工作，并对每个工作的差异化描述基本准确。但：
   - 遗漏了 LEMMA (ACL 2025) 和 Self-Error-Instruct (ACL 2025)，这两篇直接使用 error taxonomy 构建训练数据，与 proposal 的核心思路高度相关
   - 对 VHG 的差异化描述（"verification only for problem validation—not step-level error diagnosis"）稍显单薄，因为 VHG 的 symbolic verifier 也间接提供了问题有效性的诊断信号

---

【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
本 proposal 处于 "idea 方向站得住脚但内核薄弱" 的区间。方向正确（symbolic verification for self-improvement 是真实且重要的研究方向），领域调研充分，但核心 novelty 是已有组件的组合/集成（NSRSA 的诊断 + SwS 的合成 + solver-verifier gap 的理论），而非独立的 conceptual advance。三个维度中，**Novelty 是限制上界的主要因素**：如果核心发现是 positive（符号诊断优于 LLM 诊断），审稿人会认为 "expected"；如果 negative，paper 的价值更低。形式化收敛保证的 claim 过强（"单调递增 learnable information gain"），可能在审稿中被质疑假设的合理性。Trivial alternative（NSRSA filtering + prompt-based targeted synthesis）构成实质威胁，需要实验明确证明 RL-trained synthesizer 的增量价值。

【主要风险】:
1. **Novelty 不足被拒**：审稿人可能认为 "symbolic diagnosis → conditioned synthesis" 是 NSRSA + SwS 的直接拼接，核心 insight "用更精确的诊断引导更好的合成" 缺乏 surprise —— 这是最可能的拒稿理由。
2. **形式化 claim 站不住脚**："单调递增 learnable information gain" 与 solver-verifier gap 论文自身预测的指数收敛极限矛盾；如果形式化分析需要过强假设才能成立，理论贡献会被审稿人视为 vacuous，反而成为减分项。
```

Sources:
- [NSRSA - Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [SwS - Self-aware Weakness-driven Problem Synthesis in RL for LLM Reasoning](https://openreview.net/forum?id=0jQUNQsZra)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://openreview.net/pdf?id=Hh7x3c0cZl)
- [VHG - Verifier-Backed Hard Problem Generation for Mathematical Reasoning](https://arxiv.org/abs/2605.06660)
- [Self-Play Information Gain](https://arxiv.org/abs/2603.02218)
- [LEMMA - Learning from Errors for Mathematical Advancement in LLMs](https://arxiv.org/abs/2503.17439)
- [Self-Error-Instruct](https://arxiv.org/abs/2505.22591)
- [WarriorMath](https://arxiv.org/pdf/2508.01245)
- [RV-Syn](https://arxiv.org/abs/2504.20426)
- [MathSmith](https://arxiv.org/abs/2508.05592)
- [SvS - Beyond Pass@1](https://arxiv.org/abs/2508.14029)
- [Hypothesis-Driven Error Analysis](https://arxiv.org/abs/2604.04386)


【原始 proposal（允许参考但不是主要依据）】:
# Symbolic Diagnostic Verification for Targeted Math Self-Improvement

## Core Problem

Current self-improvement loops for math reasoning either use symbolic verification only for filtering (discarding rich diagnostic information) or use LLM-based weakness identification (which is unreliable and cannot prevent model collapse). Can step-level symbolic error diagnosis drive targeted problem synthesis to create provably stable, maximally informative self-improvement?

## Research Opportunity

NSRSA (March 2026) demonstrates that SymPy-based step-level verification rejects ~34% of 'lucky guess' solutions and prevents collapse on GSM8K, but completely discards the diagnostic signal after filtering. Simultaneously, SwS (NeurIPS 2025) shows weakness-targeted synthesis yields 10% gains, but its authors explicitly acknowledge that behavioral weakness identification is insufficient and synthetic problems 'lack sufficient complexity.' The solver-verifier gap theory (ICLR 2026) predicts that external symbolic verification uniquely enables sustained self-improvement because it cannot be 'fooled' by the generator. The convergence of these three threads creates an immediate opportunity: use symbolic verification not merely as a gate but as a structured diagnostic guide that drives targeted, formally verifiable problem generation.

## Research Landscape

Self-improving math reasoning is actively studied but fragmented. NSRSA (2026) achieves 91.0% on GSM8K via symbolic filtering but only tests on GSM8K/MATH-500 and discards error diagnostics. SwS (NeurIPS 2025) achieves 10% average gains via behavioral weakness targeting but uses LLM-based diagnosis and doesn't address collapse. WarriorMath (2025) achieves 12.57% via LLM-based defect awareness. RV-Syn (arXiv 2026) generates verifiable data from computational graphs with 6.3% gains but is a static pipeline. MathSmith (2025) uses RL-trained problem synthesis with difficulty strategies but not diagnostic feedback. VHG (May 2026, concurrent) introduces three-party self-play with symbolic and LLM verifiers for hard problem generation, achieving 69.0% pass@1 on general math benchmarks, but uses verification only for problem validation—not step-level error diagnosis to guide synthesis. Hypothesis-Driven Error Analysis (April 2026, concurrent) uses LLM-generated hypotheses about failure modes to synthesize targeted benchmark problems but lacks symbolic grounding and focuses on evaluation rather than training. SvS (2025) uses variational problem synthesis to sustain RLVR diversity but does not target specific weaknesses. The theoretical foundation exists: the solver-verifier gap paper (ICLR 2026) proves self-improvement requires asymmetric verification, and the self-play information gain paper (March 2026) argues each iteration must increase learnable information. The missing piece is a unified framework where symbolic verification both prevents collapse AND guides what to generate through structured error diagnosis, closing the loop between diagnosis and synthesis with formal guarantees.

## Proposed Approach

We propose SymDiag, a closed-loop self-improvement framework that transforms SymPy-based step-level verification from a binary filter into a structured diagnostic engine. In each iteration, a Qwen3-8B base model generates solutions, and the symbolic verifier classifies every erroneous step into a fine-grained taxonomy (arithmetic miscalculation, algebraic manipulation error, logical flow inconsistency, constraint violation) with precise step localization and severity scoring. This error taxonomy conditions an RL-trained problem synthesizer (using GRPO) to generate new problems that specifically probe the model's diagnosed weaknesses, with per-category generation budgets allocated by error frequency and downstream impact. We provide formal convergence analysis showing that symbolic diagnostic verification maintains a provable solver-verifier gap (preventing model collapse per ICLR 2026 theory) while diagnostic-conditioned synthesis ensures monotonically increasing learnable information gain per iteration (per the self-play information gain framework). We evaluate over 5 self-improvement iterations on GSM8K, MATH-500, AIME 2024-2025, and OlympiadBench, comparing against NSRSA (filter-only), SwS (LLM-diagnosed weakness targeting), and VHG (verifier-backed generation) baselines.

## Detailed Description

Current self-improvement approaches for mathematical reasoning either discard rich diagnostic information after symbolic verification (NSRSA) or rely on unreliable LLM-based weakness identification (SwS, WarriorMath). We introduce SymDiag, a closed-loop framework that repurposes SymPy-based step-level verification as a structured diagnostic engine driving targeted problem synthesis. Our symbolic verifier classifies solution errors into a fine-grained taxonomy—arithmetic miscalculation, algebraic manipulation failure, logical flow inconsistency, and constraint violation—with precise step localization and severity scoring. This taxonomy conditions a GRPO-trained problem synthesizer to generate problems specifically probing diagnosed weaknesses, with per-category budgets allocated by error frequency and impact. We provide the first formal analysis connecting the solver-verifier gap theory (ICLR 2026) to diagnostic-driven synthesis, proving that symbolic diagnosis maintains asymmetric verification preventing collapse while ensuring monotonically increasing learnable information gain per iteration. Experiments across GSM8K, MATH-500, AIME 2024-2025, and OlympiadBench compare against filter-only (NSRSA), LLM-diagnosed (SwS), and verifier-backed generation (VHG) baselines. Two concurrent works use verifiers for validation only (VHG) or LLM-based diagnosis (Hypothesis-Driven Error Analysis); SymDiag uniquely combines symbolic diagnostics with formal convergence guarantees.

## Key References

- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment (arXiv 2026)
- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)
- Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)
- Self-Play Only Evolves When Self-Synthetic Pipeline Ensures Learnable Information Gain (arXiv 2026)
- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)
- RV-Syn: Rational and Verifiable Mathematical Reasoning Data Synthesis based on Structured Function Library (arXiv 2026)
- Verifier-Backed Hard Problem Generation for Mathematical Reasoning (arXiv 2026)
- Automatically Generating Hard Math Problems from Hypothesis-Driven Error Analysis (arXiv 2026)
- MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy (arXiv 2025)
- Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)
- V-STaR: Training Verifiers for Self-Taught Reasoners (arXiv 2024)

## Resource Estimate

- **manual**: gpu_hours: ~3000 H100-hours (1600 for 5 RL iterations on 8×H100, 800 for baseline reproduction, 600 for ablations), timeline: 8-10 weeks (2 weeks implementation, 5 weeks experiments, 2 weeks writing), estimated_gpu_cost: $7,500 (at ~$2.50/H100-hr spot pricing)
- **human_in_loop**: gpu_hours: ~2500 H100-hours (Claude-assisted hyperparameter selection reduces wasted runs), timeline: 6-8 weeks, claude_api_cost: $300-500, estimated_gpu_cost: $6,250
- **auto_research**: gpu_hours: ~4000 H100-hours (automated exploration of error taxonomy granularities and synthesis strategies), timeline: 4-6 weeks, claude_api_cost: $1,000-1,500, estimated_gpu_cost: $10,000, speed_bottleneck: RL training wall-clock time: ~40 hours per self-improvement iteration on 8×H100s; 5 sequential iterations impose a ~200hr critical path


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f2999051-732c-4175-8a92-500da9be9c10",
  "type": "user",
  "uuid": "f37c0d8e-b220-434d-8974-0a4369a71c3b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:24:25.343Z_

```json
{
  "parentUuid": "f37c0d8e-b220-434d-8974-0a4369a71c3b",
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
  "uuid": "a03622d7-4495-4f42-b693-6b459b0e8345",
  "timestamp": "2026-05-27T08:24:25.343Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:24:25.343Z_

```json
{
  "parentUuid": "a03622d7-4495-4f42-b693-6b459b0e8345",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f0658470-a162-41d9-9cc5-da2a02cd3288",
  "timestamp": "2026-05-27T08:24:25.343Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have a comprehensive picture of the research landscape.…",
  "leafUuid": "f0658470-a162-41d9-9cc5-da2a02cd3288",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate SymDiag proposal for math self-improvement research",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:25:11.584Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them according to the Meta Judge format.

## Extracting key data points

**Reviewer 1:**
- Probability: [20% - 30%], median 25%
- Novelty: 中偏弱
- Significance: 中
- Related Work: 中偏弱
- Key concerns: Self-Error-Instruct (ACL 2025) and Adaptive Problem Generation (Feb 2026) not cited; SymPy fine-grained taxonomy feasibility; trivial alternative threat; formal guarantee overclaim
- Key missing refs: Self-Error-Instruct, Adaptive Problem Generation via Symbolic Representations, FoVer


**Reviewer 2:**
- Probability: [18% - 28%], median 23%
- Novelty: 中偏弱
- Significance: 中
- Related Work: 强
- Key concerns: Trivial alternative (NSRSA + SwS category targeting); SymPy classification capability; formal convergence guarantee deliverability; scaling to AIME/Olympiad
- Related work coverage considered excellent with no major missing references

**Reviewer 3:**
- Probability: [18% - 28%], median 22%
- Novelty: 弱-中 (偏弱)
- Significance: 中
- Related Work: 中-强
- Key concerns: Combination/integration nature; formal claim contradicts solver-verifier gap predictions; trivial alternative
- Missing references: LEMMA and Self-Error-Instruct from ACL 2025

Now I'm calculating the acceptance probability across all three reviewers. The medians are 25%, 23%, and 22%, giving a mean of 23.3% with a standard deviation around 1.25%, indicating fairly consistent skepticism across reviewers.

Looking at where the reviewers align, there's strong consensus that novelty is weak to medium, significance is medium, and the core contribution is essentially combining existing components. All three flagged the trivial alternative threat and concerns about the SymPy error taxonomy feasibility, plus the overclaimed formal convergence guarantee. The "I would have guessed this" reaction appears in multiple reviews. The main disagreement is on related work coverage, where one reviewer found it weak, another found it strong, and the third somewhere in between. Looking at the resource requirements, the proposal needs substantial compute—around 3000 H100-hours with an 8-10 week timeline and an 8×H100 cluster. The RL training is the critical bottleneck, requiring roughly 200 hours across five sequential iterations at 40 hours each.

Across all three reviewers, there's striking agreement with a standard deviation of only about 1.25% and medians clustering between 22-25%. This consistency points to a clear consensus: novelty is the main limiting factor, significance is moderate, and there are legitimate concerns about whether SymPy can reliably diagnose issues and whether the formal guarantees hold up. Taking the median of the three medians at 23%, and given how tightly the reviewers align, I should anchor my estimate there while staying conservative.

The lower bounds converge around 18% and upper bounds around 28%, so I'll narrow the interval to [18% - 27%] with a median of 22%.

Since the most generous reviewer sits at 25% and the principle says not to exceed the most lenient assessment, my median of 22% respects that constraint while leaning toward the stricter reviewers as the guidelines suggest.

At 22% this falls well below typical acceptance thresholds, so my recommendation is "不推荐", though there are potential paths forward if the key issues get addressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0658470-a162-41d9-9cc5-da2a02cd3288",
  "isSidechain": false,
  "requestId": "req_011CbSkcrHUHyGWKhDDDaTWZ",
  "type": "assistant",
  "uuid": "7069e2d4-d980-4041-a36e-614f93d2566b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MLsNEoHguAEZwtxa2o25fK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21950,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3854,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21950
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

_source line 9 · 2026-05-27T08:25:54.875Z_

【阶段】: Meta Judge
【三次中位】: [25%, 23%, 22%]  std=1.25%
【共识维度】:
- **Novelty = 中偏弱至弱（3/3 一致）**：三位审稿人均认为核心贡献是已有组件的组合/集成（NSRSA 的符号诊断 + SwS 的弱点合成 + solver-verifier gap 理论），而非 conceptual breakthrough。三人均使用了"I would have guessed this"或等价表述来描述预期的审稿人反应。
- **Significance = 中（3/3 一致）**：研究方向正确且时效性强，但预期贡献为增量改进而非范式转变，且受限于 SymPy 可验证的问题范围。
- **Trivial Alternative 威胁真实存在（3/3 一致）**：NSRSA filtering + SwS/prompt-based category-level targeting 即可获得大部分收益，fine-grained error taxonomy conditioning 的边际价值未经论证。
- **SymPy fine-grained error taxonomy 可行性存疑（3/3 一致）**：SymPy 擅长算术/代数验证，但对"logical flow inconsistency"和"constraint violation"的分类能力远超其设计能力边界，在 AIME/OlympiadBench 级别问题上覆盖率未知。
- **Formal convergence guarantee 过强/高风险（3/3 一致）**："monotonically increasing learnable information gain"的声明要么需要过强假设（使定理 vacuous），要么无法证明。R3 额外指出该 claim 与 solver-verifier gap 论文自身预测的指数收敛极限存在张力。
- **Related Work 遗漏 Self-Error-Instruct（2/3 一致，R1+R3）**：Self-Error-Instruct (ACL 2025) 已实现"错误类型分类→定向数据合成"的范式，是最直接的竞争者，proposal 未提及。
【异常维度】:
- **Related Work 整体评分分歧**：R1 评"中偏弱"（强调遗漏致命），R2 评"强"（认为覆盖全面），R3 评"中-强"。R2 是 outlier（未发现 Self-Error-Instruct 遗漏问题）。鉴于 R1 和 R3 均独立发现了 Self-Error-Instruct 这一关键遗漏，R2 对 Related Work 的"强"评级应降权。综合判定 Related Work = **中**。
- **R1 独有发现：Adaptive Problem Generation via Symbolic Representations (Feb 2026)**——在符号空间做闭环问题生成，与 SymDiag 的"符号化+闭环"主题高度重合。仅 R1 提及，属于有价值但非致命的补充信息，适度采信。
- **R3 独有发现：LEMMA (ACL Findings 2025)**——错误类型分类用于构建训练数据。仅 R3 提及，与 Self-Error-Instruct 方向相近，进一步强化了"error taxonomy → training data 路径已被探索"的共识判断。
【最终概率】: [18% - 27%] 中位 23%
【一致性】: 高
【综合理由】: 三位审稿人在所有核心维度上高度一致（std=1.25%），均将 Novelty 识别为概率上限的主要约束。综合逻辑如下：(1) Novelty 天花板：核心贡献是"符号诊断信号 condition 问题合成"这一 specific engineering bridge，而非新范式——Self-Error-Instruct (ACL 2025) 已实现"错误分类→定向合成"，NSRSA 已有符号验证，SwS 已有 RL 合成。SymDiag 的真实增量是"用 SymPy 替代 LLM 做错误分类"，这是一个合理但 incremental 的模块替换。(2) 可行性风险叠加：SymPy fine-grained taxonomy 的可行性、formal guarantee 的可交付性、error taxonomy conditioning 的实际增益——这三个未验证假设构成 cascading risk。(3) 下限保障：研究方向完全正确且时效性强，proposal 工程质量好，对已引文献描述准确，实验设计跨度合理（GSM8K→AIME→OlympiadBench）。这些因素阻止概率跌破 18%。(4) 中位取 23%（偏向 R2=23% 和 R3=22% 的更严格端），上界缩窄至 27%（相比 R1 的 30% 更保守），反映高一致性下的收敛判断。
【建议】: 边缘（偏不推荐）——idea 方向正确但 novelty 内核薄弱，需要在迭代中显著强化差异化定位、补齐关键遗漏文献、降低 formal claim 的风险，才有可能进入可投稿区间。当前距 36% 阈值有明显差距，但非 KILL——核心 gap（符号诊断驱动合成）确实未被直接占据，有提升空间。
【实施评估】:
  - 计算资源: ~3000 H100-hours（8×H100 集群），含 1600h 用于 5 轮 RL 迭代训练、800h 基线复现、600h 消融实验。按 spot pricing ~$2.50/H100-hr 估算 GPU 成本约 $7,500。RL 训练关键路径约 200h（每轮迭代 ~40h × 5 轮串行）。
  - 数据需求: GSM8K（公开）、MATH-500（公开）、AIME 2024-2025（公开）、OlympiadBench（公开）。数据获取无障碍。
  - 人工介入: 需要人工设计和验证 SymPy error taxonomy 的分类规则（尤其是"logical flow inconsistency"和"constraint violation"的操作化定义），预估 1-2 周专家工作量。可能需要人工标注少量 ground truth 来评估分类准确率。
  - 训练需求: 需要训练 Qwen3-8B 基座模型（5 轮 self-improvement 迭代）和 GRPO-trained problem synthesizer。模型规模 8B，单轮训练约 40h on 8×H100。
  - 新 Benchmark: 不需要构建新 benchmark，使用现有公开数据集。但需要构建 SymPy error taxonomy 的分类体系和评估指标（非标准 benchmark，属于方法论组件）。
  - 预估周期: 8-10 周（2 周实现 + 5 周实验 + 2 周写作）。主要瓶颈是 RL 训练的串行关键路径（~200h ≈ 8.3 天）和 SymPy 诊断引擎的工程实现复杂度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7069e2d4-d980-4041-a36e-614f93d2566b",
  "isSidechain": false,
  "requestId": "req_011CbSkcrHUHyGWKhDDDaTWZ",
  "type": "assistant",
  "uuid": "792ab179-d543-497b-9be6-ec86ab052bd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MLsNEoHguAEZwtxa2o25fK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21950,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3854,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21950
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have a comprehensive picture of the research landscape.…",
  "leafUuid": "792ab179-d543-497b-9be6-ec86ab052bd3",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate SymDiag proposal for math self-improvement research",
  "sessionId": "b9428c2b-d14e-454c-94b4-9d203535debc"
}
```

---
