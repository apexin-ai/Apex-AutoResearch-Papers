# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/25902491-0c31-4aa9-8a18-f63aa0c72ebc.jsonl`
- **Structured JSON:** [`1107db05be425e57df2b.json`](../../sessions/11/1107db05be425e57df2b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:13:04.616Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:13:04.616Z",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make a well-grounded assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. \"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\" (arXiv 2505.18486, May 2025):\n   直接竞争工作。已将 MFRM 应用于 LLM 评分场景，比较了 10 个 LLM（GPT-4o、Claude 3.5 Sonnet、Gemini 等）与人类评分者的 rater effects。证明 MFRM 在 LLM-as-rater 场景下是可行的，但未涉及 contamination 矫正。本 proposal 的 \"将 MFRM 引入 LLM 评估\" 这一 claim 的 novelty 因此被显著削弱——核心框架的应用已有先例。\n\n2. \"CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation\" (arXiv 2603.01865, March 2026):\n   Proposal 明确列为 baseline。CyclicJudge 用 round-robin 分配消除 judge bias，证明在固定 budget 下是最优策略。方法极其简洁（无需训练，无需参数估计）。这构成了强有力的 trivial alternative 威胁——CyclicJudge 不需要 Bayesian MCMC 就能 \"精确消除\" bias。\n\n3. \"ConStat: Performance-Based Contamination Detection in Large Language Models\" (NeurIPS 2024):\n   Proposal 依赖 ConStat 作为外部 exposure 估计的核心信号源（claimed r²=0.94）。ConStat 本身是 black-box 方法，已在 NeurIPS 2024 发表，是成熟工具。Proposal 的 contamination 检测并非原创，而是 ConStat 的下游消费者。\n\n4. \"DCR: Quantifying Data Contamination in LLMs Evaluation\" (EMNLP 2025):\n   Proposal 明确列为 baseline。DCR 提供 contamination-aware adjusted accuracy，已解决 contamination 量化+调整的核心问题，但仅针对 benchmark 本身的 accuracy，未涉及 judge-as-evaluator 场景。\n\n5. \"Preference Leakage: A Contamination Problem in LLM-as-a-judge\" (arXiv 2502.01534, Feb 2025):\n   Proposal 列为 baseline。定义了 LLM-as-judge 特有的 contamination 问题（data generator 与 judge 的 relatedness），但处理方式是识别和量化，非 joint calibration。\n\n6. \"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\" (arXiv 2604.23178, April 2026):\n   极其近期的 directly relevant 工作。首次在统一框架下比较 9 种 debiasing 策略 × 5 个 judge × 3 个 benchmark × 4 种 bias 类型。Proposal 未引用此工作。该工作的 meta-debiasing pipeline 可能与 G-MFRM 的定位形成直接竞争。\n\n7. \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" (arXiv 2505.15055, May 2025):\n   IRT 应用于 LLM 评估的代表性工作。表明 IRT/psychometric 方法在 LLM benchmark 领域已是活跃的、趋向拥挤的研究方向。\n\n8. LogProber (arXiv 2408.14352, updated June 2025):\n   Proposal 所依赖的 gray-box contamination 信号之一。已发表的独立工作，非 proposal 原创贡献。\n\n- 调研总结: LLM-as-judge bias correction 和 benchmark contamination detection 分别已有成熟且活跃的研究线（CyclicJudge、\"Judging the Judges\" 等针对 bias；ConStat、DCR、Preference Leakage 针对 contamination）。MFRM 已被直接应用于 LLM rater 评估（2505.18486）。IRT/psychometric 方法在 LLM 评估领域已趋于拥挤。本 proposal 的核心定位——\"joint bias + contamination correction\"——是一个尚未被直接解决的 gap，但其每个组成部件均为现有工作的组合/应用，且存在强 trivial alternative（CyclicJudge + DCR 两阶段 pipeline）。\n\n\n【Trivial Alternative 检验】:\n\n存在明确的 trivial alternative：CyclicJudge（round-robin，零参数，已证明 budget 最优）+ ConStat/DCR 后处理过滤contaminated items。这个两阶段 pipeline：\n- 不需要 Bayesian MCMC 推断\n- 不需要 hierarchical parameterization\n- 不需要 NumPyro 实现\n- CyclicJudge 已被证明在固定 budget 下精确消除 bias\n\nProposal 自己也将 \"naive two-stage pipeline (CyclicJudge → DCR)\" 列为 baseline，但关键问题是：**joint calibration 相比这个 trivial pipeline 的增量价值有多大？** 如果 Kendall-τ 提升仅为 0.01-0.03，那么 G-MFRM 的复杂性（MCMC、三阶段估计、NumPyro pipeline）就难以 justify。\n\nProposal 的增量价值理论上在于：(a) bias 和 contamination 存在交互效应，joint model 能捕捉这种交互；(b) 产生可解释的 per-model contamination estimates 和 per-judge severity calibrations。但 (a) 是否成立是一个未验证的经验性假设，(b) 的实际价值取决于用户是否真正需要这些 interpretable diagnostics（而非仅需要一个 fair ranking）。\n\n\n【前提假设检验】:\n\n核心逻辑链中存在以下未经验证的关键假设：\n\n1. **Contamination 的可加性/可乘性分解假设**：c_n · e_i 假设 contamination 效应可以分解为 model susceptibility × item exposure 的乘积形式。真实的 contamination 可能具有更复杂的结构——例如 partial memorization（模型记住了 item 的某些特征但非完整答案）、style contamination（通过训练数据中的相似文本而非直接暴露）。LLTM/AMMI 的 identifiability guarantee 成立的前提是分解结构正确，但这一前提本身未被验证。\n\n2. **External exposure estimation 的充分性和准确性假设**：ConStat 的 r²=0.94 是在其原始验证场景下的数据。将其 exposure indicators 迁移到 MT-Bench、Arena-Hard、WildBench 等不同类型的 benchmark（对话质量评估 vs. 标准 NLP benchmark）时，是否仍然准确？对话评估 benchmark 的 contamination 模式可能与 ConStat 原始验证的 multiple-choice benchmark 有本质区别。\n\n3. **Bias 和 contamination 的可分离性假设**：MFRM 框架将 judge severity 和 model contamination 作为独立 facets 处理。但在 LLM-as-judge 场景中，某些 \"bias\" 可能正是 contamination 的表现（例如 self-preference bias 本质上是一种 preference leakage/contamination）。如果两者存在 confounding，joint model 反而可能产生不可识别性问题。\n\n4. **Rasch model 的单维性假设**：MFRM 假设 ability 是单维的。但 LLM 的 \"ability\" 在对话评估中是高度多维的（安全性、helpfulness、创造性、factuality 等）。这一假设违反可能导致 model misspecification。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中（偏弱）**\n   - MFRM 已被应用于 LLM rater 评估（arXiv 2505.18486），核心框架的 \"引入\" 不再新颖。\n   - IRT/psychometric 方法在 LLM 评估中已是拥挤方向（2505.15055, 2605.07046, 2605.00238 等）。\n   - 每个组件（MFRM、ConStat、LogProber、CyclicJudge）均为现有工作的直接应用或消费。\n   - 真正新颖的部分是 \"joint bias + contamination calibration\" 这一组合以及 hierarchical contamination parameterization，但这属于 incremental combination novelty 而非 conceptual breakthrough。\n   - DG-IRT-inspired gating mechanism 虽然是合理的方法论选择，但本质上是将已有的 IRT contamination modeling 技术嫁接到 MFRM 上。\n   - 审稿人大概率会评价为 \"a technically competent integration of known techniques, but the novelty is limited to the combination itself.\"\n\n2. **Significance: 中**\n   - 研究问题本身重要且及时——LLM-as-judge 的 bias 和 contamination 是被广泛关注的问题（2025-2026 年有大量相关工作）。\n   - 但 **\"joint correction provides substantial improvement over sequential correction\" 这一核心价值命题尚未被验证**。如果 joint model 仅带来边际提升，significance 会大幅下降。\n   - 框架的适用范围有限：要求 8+ 个 LLM judges、ConStat 外部信号、LogProber access——这些条件在实际应用中可能不总是满足。\n   - 产出的 interpretable diagnostics（per-model contamination, per-judge severity）具有一定实际价值，但审稿人可能会问 \"who actually needs this granularity?\"\n   - **⚠️ 严重的会议匹配问题**：此 proposal 是纯 NLP evaluation/psychometrics 工作，与 CoRL（Conference on Robot Learning）的 scope 完全不匹配。CoRL 聚焦于 robot learning、manipulation、perception、control。即使 idea 质量可接受，在 CoRL 投稿几乎必然 desk reject。应投 ACL、EMNLP、NeurIPS、ICML 等。\n\n3. **Related Work: 中-强（偏中）**\n   - Proposal 覆盖了核心 baselines（CyclicJudge、DCR、Preference Leakage）和依赖工具（ConStat、LogProber）。\n   - 定位清晰：将自己置于 \"bias-only\" 和 \"contamination-only\" 两条研究线的交汇点。\n   - 但缺失了几个关键近期工作：\n     * arXiv 2505.18486：直接将 MFRM 用于 LLM rater 评估——这是最直接的 prior art，未被引用是重大遗漏。\n     * arXiv 2604.23178 \"Judging the Judges\"：统一框架比较 9 种 debiasing 策略——与 proposal 的 \"unified framework\" 定位直接竞争。\n     * arXiv 2505.15055 \"Lost in Benchmarks\"：IRT 用于 LLM benchmarking 的代表性工作。\n   - 这些遗漏可能导致审稿人质疑 novelty claim 的 credibility。\n\n\n【概率估计】: \n\n对于 NLP/ML 顶会（ACL/EMNLP/NeurIPS）: [20% - 30%]，中位 25%\n对于 CoRL 2026（用户指定会议）: [0% - 5%]，中位 2%\n\n【估计理由】:\n\nIdea 本身处于 \"方向正确、有真实但有限的 novelty delta\" 的档位。核心 claim 的逻辑链完整但不够 surprising——\"将 bias correction 和 contamination correction 联合建模优于分开做\" 这一结论如果成立，审稿人大概率会说 \"makes sense, I would have guessed this\"，而不会说 \"surprising\"。这把 idea 质量锚定在 25-35% 区间的下部。\n\n进一步削弱的因素：(a) MFRM 用于 LLM 评估已有先例（2505.18486），novelty claim 的一条重要支柱被削弱；(b) CyclicJudge 作为 trivial alternative 的威胁真实存在——如果 CyclicJudge + DCR 两阶段 pipeline 效果接近，joint model 的复杂性难以 justify；(c) 核心前提假设（contamination 可乘性分解、ConStat 跨 benchmark 迁移性）未经验证。\n\nNovelty（弱-中）是限制上界的主要维度——即使实验做得完美，一个 \"technically sound integration of existing techniques\" 在顶会的接受概率上界也受限。\n\n**对于 CoRL 2026：这是一个纯 NLP evaluation/psychometrics proposal，与 CoRL 的 robot learning scope 完全不匹配，预期 desk reject。**\n\n【主要风险】:\n\n1. **Trivial alternative 风险**: CyclicJudge（零参数 round-robin）+ ConStat/DCR 后处理可能以极低成本达到 80-90% 的效果。如果 joint model 的提升不显著，整个工作的 value proposition 坍塌。审稿人几乎必然会追问 \"What's the marginal gain of joint calibration over the naive pipeline?\"\n\n2. **Novelty 被挤压风险**: MFRM 用于 LLM 评估已有直接先例（2505.18486）；IRT for LLM evaluation 是拥挤方向；每个组件均非原创。审稿人可能判定 contribution 仅为 \"engineering integration\" 而非 \"methodological advance\"。\n```\n\n---\n\n**⚠️ 附加重要提醒：会议选择问题**\n\n此 proposal 是关于 LLM-as-judge 评估中的 psychometric calibration，属于 NLP evaluation methodology 领域。**CoRL (Conference on Robot Learning) 完全不是合适的投稿目标**——CoRL 聚焦于机器人学习、操控、感知、运动控制等。建议考虑 ACL、EMNLP、NeurIPS (Datasets and Benchmarks track)、或 COLM 作为投稿目标。会议匹配问题是独立于 idea 质量的，但会直接导致 desk rejection。\n\nSources:\n- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)\n- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)\n- [ConStat: Performance-Based Contamination Detection in Large Language Models](https://arxiv.org/abs/2405.16281)\n- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173.pdf)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)\n- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)\n- [Lost in Benchmarks? Rethinking Large Language Model Benchmarking with IRT](https://arxiv.org/abs/2505.15055)\n- [LogProber: Disentangling confidence from contamination in LLM responses](https://arxiv.org/abs/2408.14352)\n- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile the triage.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 严重的投稿方向问题】:\n本 proposal 是一篇 LLM-as-Judge 评估方法论论文（心理计量学 + 污染检测），与 CoRL（Conference on Robot Learning）的收稿范围完全不匹配。CoRL 2026 Call for Papers 明确要求 \"Submissions without a robotics focus will be returned without review\"。该 proposal 不含任何机器人学习内容，投稿 CoRL 大概率会被 desk-reject。适合的目标会议应为 ACL / EMNLP / NeurIPS / ICML。以下评估基于 idea 本身质量，不考虑具体会议，但此方向性错误需首先纠正。\n\n【领域调研】:\n- [Dual Optimal: Make Your LLM Peer-like with Dignity](https://arxiv.org/abs/2604.00979) (arXiv 2026.04): **直接竞争**。已将 MFRM 应用于 LLM 评估，使用心理计量 IRT 校准协议来分离模型能力与 judge bias。与本 proposal 的核心框架高度重叠。\n- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865) (arXiv 2026.03): 提出 round-robin judge 分配策略，用单 judge 成本精确消除 bias。proposal 将其列为 baseline，定位合理。\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534) (arXiv 2025.02): 发现 judge-generator 关联性导致的偏好泄漏，提出该问题比已知 bias 更难检测。proposal 将其列为 baseline。\n- [ConStat: Performance-Based Contamination Detection](https://arxiv.org/abs/2405.16281) (NeurIPS 2024): proposal 的核心外部信号之一。ConStat 通过参考 benchmark 比较检测污染，但其设计目标是闭卷 benchmark，对 MT-Bench 等开放式 benchmark 的适用性存疑。\n- [LogProber: Disentangling confidence from contamination](https://arxiv.org/abs/2408.14352) (arXiv 2024-2025): proposal 使用的灰箱污染检测信号，提供 Safe Score。\n- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://arxiv.org/abs/2507.11405) (arXiv 2025): 提供污染调整准确率（Acc_adj），proposal 将其列为 baseline。\n- [A Judge-Aware Ranking Framework for Evaluating LLMs without Ground Truth](https://arxiv.org/abs/2601.21817) (arXiv 2026.01): **直接竞争但 proposal 未引用**。使用统计模型建模 judge bias 进行排名，有最大似然估计和渐近性质证明。\n- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178) (arXiv 2026.04): 对 LLM-as-judge 偏差缓解策略的首个系统性统一 benchmark，proposal 未引用。\n- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485) (arXiv 2026.03): 理论性更强的 judge bias 校正，proposal 未引用。\n- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT](https://arxiv.org/abs/2505.15055) (arXiv 2025.05): PSN-IRT 框架对 benchmark 质量（含污染）的系统分析，发现广泛污染和测量质量问题。\n- **\"DG-IRT\"**: proposal 声称受 \"DG-IRT\" 启发其 gating 机制，但多轮搜索未找到名为 \"DG-IRT\" 的已发表模型。该引用的真实性存疑。\n\n- **调研总结**: IRT/心理计量方法应用于 LLM 评估是 2025-2026 年的活跃方向，多篇并行工作。MFRM 已被 Dual Optimal 应用于 LLM 评估。Judge bias 校正和 benchmark 污染检测各有独立的成熟工作，但将两者在统一框架内联合建模的工作尚未见正式发表。本 proposal 定位在 \"bridging bias and contamination silos\" 的交汇处，有一定差异化空间，但面临来自 Dual Optimal（MFRM 部分）和多个 bias 校正工作的挤压。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁：\n1. **简单两阶段流水线**（CyclicJudge 去 bias → ConStat 标记污染项并移除）：工程成本极低，proposal 自身也列为 baseline。关键问题是 G-MFRM 的联合建模相比这个 pipeline 的增量收益是否实质性的（而非统计噪声范围内的微小 Kendall-τ 提升）。\n2. **多样化 judge 集合 + 简单 trimmed mean / median**：使用 8+ 个不同 judge 然后取中位数，已经能大幅稀释单个 judge 的 bias 和 contamination 偏差。无需复杂框架。\n3. **Judge-Aware Ranking Framework**（arXiv 2601.21817）已提供带理论保证的 judge bias 建模方案，可能以更简洁的方式达到类似效果。\n\n增量价值论证尚不充分：proposal 声称 \"higher Kendall-τ\" 但这是待验证的 claim，且效果大小（effect size）未知。如果提升仅有 0.02-0.03 的 τ 差异，审稿人会质疑复杂框架的必要性。\n\n【前提假设检验】:\n核心 claim 的逻辑链条存在以下未验证假设：\n\n1. **\"污染在开放式 benchmark 中构成显著问题\" — 未充分论证**。ConStat 和 DCR 的设计目标是闭卷 benchmark（MMLU、C-Eval 等有标准答案）。对 MT-Bench、Arena-Hard、WildBench 等开放式评估 benchmark，污染的定义、表现形式和严重程度完全不同。Preference Leakage 论文明确指出 \"the issue of data contamination in open-ended benchmarks is less severe since there are no standard answers\"。如果效应不显著，整个 contamination gating 机制就在解决一个不存在的问题。\n\n2. **\"污染效应可分解为 c_n · e_i（模型敏感度 × 题目暴露度）\" — 强结构性假设**。这假设污染是可乘性分解的，但实际污染可能高度非线性：某些模型可能在特定题目上过拟合而在其他暴露题目上完全不受影响。乘法分解的适用性需要实证支持，而非仅靠 LLTM/AMMI 传统的类比论证。\n\n3. **\"ConStat 外部信号在开放式 benchmark 上可靠（r²=0.94）\" — 迁移假设**。该 r² 数据来自 ConStat 原论文在闭卷 benchmark 上的验证。将其直接应用于开放式 benchmark 的 exposure indicator 估计，存在未验证的域迁移风险。\n\n4. **\"DG-IRT\" 引用不可验证**。proposal 声称其 gating 机制受 \"DG-IRT\" 启发，但该模型在公开文献中不可查证。如果这是一个不存在的引用，会严重影响学术可信度。\n\n【3 维度打分】:\n  1. Novelty: 弱到中 — \n     MFRM 应用于 LLM 评估已被 \"Dual Optimal\"（2604.00979）实现，且 IRT 方法在 LLM 评估中已是 2025-2026 年的热点（PSN-IRT、Judge-Aware Ranking 等）。本 proposal 的增量 novelty 在于联合建模 judge bias 和 contamination 的 gating 机制，但：(a) 乘法分解 c_n · e_i 是标准 LLTM/AMMI 技术的直接应用；(b) 外部信号（ConStat、LogProber）均为现有工具的直接调用；(c) 三阶段估计策略本质上是\"先分别估计，再联合微调\"的常见 pipeline。如果审稿人已经看过 Dual Optimal 和 Judge-Aware Ranking，会认为本文是一个工程组合而非概念创新。核心发现如果 positive，审稿人的反应更可能是 \"makes sense, I would have expected this to work\" 而非 \"surprising\"。\n\n  2. Significance: 中 — \n     研究问题本身（LLM-as-judge 评估的可靠性）是重要且时效性强的。2025-2026 年 LLM 评估可靠性是社区关注焦点。但本框架的实际影响力受限于：(a) 框架复杂度高（Bayesian MCMC + NumPyro + 三阶段 + 多外部信号），部署门槛远高于 CyclicJudge 等轻量方案；(b) 适用范围窄——仅针对 multi-judge 评估场景，而实践中很多评估只用单个 judge；(c) \"bridging two silos\" 的叙事虽有吸引力，但如果两个 silo 的分别解决方案（CyclicJudge + ConStat）简单组合就足够好，统一框架的实用价值就会大打折扣。\n\n  3. Related Work: 弱 — \n     存在关键遗漏：(a) **Dual Optimal**（2604.00979）是最直接的竞争者（MFRM + LLM 评估），proposal 完全未提及；(b) **Judge-Aware Ranking Framework**（2601.21817）用统计模型处理 judge bias 并有理论保证，未引用；(c) **Judging the Judges**（2604.23178）对 bias 缓解策略的系统性评估，未引用；(d) **\"DG-IRT\"** 引用不可验证。此外，proposal 对现有工作差异化定位的论证依赖于 \"没有工作同时处理 bias 和 contamination\" 这一 gap，但没有充分论证为什么这两个问题必须在同一模型内联合处理（而非 pipeline 组合）。\n\n【概率估计】: [15% - 25%] 中位 20%\n（注：此估计基于 idea 质量投稿至 appropriate NLP/ML venue 如 ACL/EMNLP/NeurIPS。若投稿 CoRL，因完全超出收稿范围，估计为 ~0%，大概率 desk-reject。）\n\n【估计理由】: \nIdea 处于 \"方向站得住脚但内核薄弱\" 区间。研究问题是真实的，但：(1) Novelty 受到 Dual Optimal 和 Judge-Aware Ranking 等并行工作的严重挤压，核心贡献更像工程组合而非概念创新；(2) trivial alternative（两阶段 pipeline）的威胁明确存在且 proposal 未充分论证增量价值；(3) 核心前提假设（污染在开放式 benchmark 上的显著性、c_n·e_i 分解的适用性）均未经验证。上界被 Novelty 维度限制——即使实验完美，审稿人仍会质疑 \"what's genuinely new here beyond wiring existing tools into an existing model\"。\n\n【主要风险】: \n1. **Novelty 不足风险**：Dual Optimal 已将 MFRM 应用于 LLM 评估，Judge-Aware Ranking 已用统计模型处理 judge bias。审稿人会认为本文是在已有框架上叠加已有工具，增量 novelty 有限。\n2. **前提假设崩塌风险**：如果开放式 benchmark 上的污染效应本就很小（Preference Leakage 论文的发现支持这一可能），整个 contamination gating 机制就成了过度工程化的解决方案，审稿人会质疑 \"is this problem real enough to warrant this complexity?\"\n```\n\n---\n\n**Sources:**\n- [Dual Optimal: Make Your LLM Peer-like with Dignity](https://arxiv.org/abs/2604.00979)\n- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)\n- [ConStat: Performance-Based Contamination Detection in LLMs](https://arxiv.org/abs/2405.16281)\n- [LogProber: Disentangling confidence from contamination in LLM responses](https://arxiv.org/abs/2408.14352)\n- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://arxiv.org/abs/2507.11405)\n- [A Judge-Aware Ranking Framework for Evaluating LLMs without Ground Truth](https://arxiv.org/abs/2601.21817)\n- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)\n- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485)\n- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT](https://arxiv.org/abs/2505.15055)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [LLM-as-a-Judge: 2026 Guide](https://labelyourdata.com/articles/llm-as-a-judge)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a well-grounded assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. Jiao, Song & Lee, \"Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model\" (arXiv 2505.18486, May 2025):\n   直接用 MFRM 对 10 个 LLM 做 rater effect 分析，与人类评分者对比。证明 MFRM 已被应用到 LLM-as-judge 场景，本 proposal 的 MFRM 部分（Stage 1）不再是新贡献。\n\n2. Choi et al., \"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\" (arXiv 2602.00521, Jan 2026):\n   用 GRM-IRT 对 LLM judge 的可靠性做两阶段诊断（intrinsic consistency + human alignment）。与本 proposal 共享 \"用心理测量模型分析 LLM judge\" 的核心思路，但未处理 contamination。\n\n3. CyclicJudge (arXiv 2603.01865, Mar 2026):\n   提出 round-robin judge 分配策略消除 judge bias，方差分解成 scenario/generation/judge/residual 成分。在 MT-Bench 和 MindEval 上验证。本 proposal 将其作为 baseline。\n\n4. ConStat (NeurIPS 2024, de Koninck et al.):\n   基于参考 benchmark 对比的 performance-based contamination 检测，报告 r²=0.94。本 proposal 依赖此作为外部 exposure indicator 来源。\n\n5. DCR: Quantifying Data Contamination (EMNLP 2025):\n   轻量级 contamination 量化框架，输出 DCR Factor 调整 raw accuracy，在 9 个 LLM 上误差 ≤4%。本 proposal 作为 baseline。\n\n6. Preference Leakage (arXiv 2502.01534, Feb 2025, ICLR 2026 接收):\n   揭示 LLM judge 与被评估模型同源时的 preference contamination，实验确认 bias 普遍存在。本 proposal 作为 baseline。\n\n7. LogProber (arXiv 2408.14352, Aug 2024):\n   基于 logprob 曲线面积检测 contamination 的灰盒方法。本 proposal 用作 exposure indicator 信号源之一。\n\n8. \"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT\" (arXiv 2505.15055, May 2025):\n   用 IRT 重新审视 LLM leaderboard 排名不一致性，但未处理 judge bias 或 contamination。\n\n9. Shu et al., \"Using Deterministic Gated IRT Model to Detect Test Cheating due to Item Compromise\" (psychometrics 文献):\n   原始 DG-IRT 模型，用 gating 机制区分 compromised/uncompromised item 上的表现。本 proposal 的 contamination gating 直接源于此。\n\n- 调研总结：IRT/MFRM 应用于 LLM 评估已成 2025-2026 热点方向，judge bias 和 benchmark contamination 各有成熟方法。但目前**两个子领域仍是独立的**：bias correction 工作（CyclicJudge、方差分解）不处理 contamination，contamination detection（ConStat、DCR、LogProber）不处理 judge bias。本 proposal 的定位是 **bridge this gap**，用单一心理测量框架统一两者。这个 \"gap\" 是真实存在的。\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative 是 proposal 自己已列出的 baseline：**naive two-stage pipeline (CyclicJudge → DCR)**——先用 CyclicJudge 做 judge bias 消除，再用 DCR Factor 做 contamination 调整。这个 pipeline 成本极低、实现简单。\n\nProposal 声称 joint estimation 优于 sequential pipeline 的关键论据是：bias 和 contamination 存在交互效应——一个 contaminated model 在 biased judge 面前会获得双重膨胀/压缩分数，sequential correction 无法捕获这种交互。这个论据在理论上成立，但 **交互效应的实际大小是一个未经验证的经验问题**。如果交互效应很小（例如 Kendall-τ 改善 < 0.02），则 joint framework 的额外复杂度（Bayesian MCMC、三阶段估计）难以justify。\n\n**增量价值取决于交互效应的真实大小**。如果 joint > sequential 的 margin 是实质性的（τ 改善 > 0.05），则有清晰的增量价值；如果 margin 微小，则 trivial alternative 几乎等效。\n\n【前提假设检验】:\n\n1. **乘法分解假设 c_n · e_i**：假定 contamination 可分解为 \"模型固有的 contamination 易感性\" × \"题目暴露程度\"，这意味着一个模型对所有 exposed items 的 contamination 程度是按相同比例缩放的。实际上，contamination 可能是 item-specific 的（某些模型可能记住了特定题目而非按比例），这个乘法假设过于简化。虽然 proposal 引用 LLTM 和 AMMI 的 identifiability 保证，但 identifiability ≠ validity——模型可识别不等于模型正确。\n\n2. **外部 exposure indicators 的准确性假设**：Stage 3 将 ConStat/LogProber 的 exposure 估计作为 **fixed** 输入。但 ConStat 的 r²=0.94 是在特定 benchmark 和特定条件下测得的，跨 benchmark/跨模型的泛化性未经验证。如果 exposure indicators 本身有系统偏差，整个 G-MFRM 的 contamination 估计会被污染。\n\n3. **Chatbot Arena 人类投票作为 ground truth**：这是领域标准做法，但 Arena 投票本身有 selection bias（用户倾向提交特定类型 query）、population bias（用户群不代表general population）等已知问题。用它作为唯一的外部效标可能导致 \"optimizing for Arena correlation\" 而非真正的 \"fair ability ranking\"。\n\n4. **Judge 数量假设**：8 个 judge 是否足够支撑 MFRM 的参数估计（N×I 个 observations 分散到 severity/ability/difficulty/contamination 参数）？多面 Rasch 模型通常要求每个 facet 有充足样本量，8 个 judge 的 severity 估计可能不稳定。这更偏实验设计问题，但也涉及 idea 的核心 claim 能否被验证。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心贡献是 \"MFRM + contamination gating 的整合\"。每个组件单独来看都不新：MFRM 已被 Jiao et al. (2505.18486) 用于 LLM 评估；contamination detection 有 ConStat (NeurIPS 2024)、DCR (EMNLP 2025) 成熟方案；IRT 用于 LLM-as-judge 有 Choi et al. (2602.00521)；DG-IRT gating 来自 psychometrics 文献。Novelty 在于 **特定的整合方式**（hierarchical parameterization c_n·e_i + external exposure indicators + three-stage estimation），这是合理但 **expected** 的工程整合——了解两个子领域的研究者都会想到 \"为什么不把 bias correction 和 contamination detection 放在一起\"。差异化不在于 \"想到了\"，而在于 \"具体怎么做\"，而具体做法（乘法分解、external indicators 作 fixed input、informative priors）都是心理测量学的标准技术。不够 surprising，但也不 trivial。\n\n2. **Significance: 中** —\n   研究问题本身重要且真实——LLM-as-judge 的 bias 和 contamination 确实是两个独立研究 silo，需要被统一。但 **实际影响面偏窄**：(a) 只影响运行 multi-judge LLM 评估的研究者/平台；(b) 核心发现若 positive（\"joint > sequential\"），审稿人大概率反应是 \"I would have guessed this\"——直觉上联合建模应该优于 sequential，这不 surprising；(c) per-model contamination 估计和 per-judge severity calibration 的 \"可解释性\" 是锦上添花而非刚需——实际使用者更关心最终排名质量而非中间参数。\n\n3. **Related Work: 强** —\n   Proposal 对两个子领域（judge bias: CyclicJudge; contamination: ConStat, DCR, LogProber, Preference Leakage）的覆盖全面，差异化定位清晰（\"第一个统一两者的 psychometric framework\"）。每个 baseline 都被明确命名并纳入实验对比。唯一的轻微不足是对 IRT-for-LLM 的最新工作（如 Choi et al. 2602.00521、\"Lost in Benchmarks\" 2505.15055）未明确提及其作为 related work 如何差异化。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】:\nNovelty 是中等——整合的 idea 方向正确但 expected，核心发现若 positive 不具 surprise value（\"joint > sequential\" 是直觉预期）。Significance 中等——问题真实但受众窄、影响力有限。Related Work 强——定位清晰、baseline 全面，这会保护下限。三维综合来看，这是一篇 **solid integration paper**，但不是 idea-driven paper。上界被 Novelty 和 Significance 限制：缺乏 surprising/counterintuitive 的核心发现来推动分数进入 35%+ 区间。下界由 Related Work 的完整性和问题的真实性保护。\n\n额外风险：**CoRL 2026 是 Conference on Robot Learning，而本 proposal 是纯 NLP/ML evaluation 方法论工作，与 robotics 完全无关。如果确实投 CoRL，几乎必然 desk reject。** 建议目标会议为 ACL/EMNLP/NeurIPS/ICML。此处概率估计基于 idea 质量本身（假设投对了 venue），不考虑 venue mismatch。\n\n【主要风险】:\n1. **Trivial alternative 威胁**：naive two-stage pipeline (CyclicJudge → DCR) 可能在实验中与 G-MFRM 表现接近（Kendall-τ 差距微小），使得整个复杂框架的增量价值被质疑为 \"over-engineering for marginal gains\"。\n2. **\"I would have guessed this\" 风险**：核心 claim \"joint calibration > sequential correction\" 是直觉预期，审稿人可能认为这是一个 expected result 而非 surprising finding，导致 contribution 被低估。\n```\n\nSources:\n- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)\n- [Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory](https://arxiv.org/abs/2602.00521)\n- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)\n- [ConStat: Performance-Based Contamination Detection in Large Language Models](https://arxiv.org/abs/2405.16281)\n- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173/)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)\n- [LogProber: Disentangling confidence from contamination in LLM responses](https://arxiv.org/abs/2408.14352)\n- [Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory](https://arxiv.org/abs/2505.15055)\n- [Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise](https://www.researchgate.net/publication/257678777)\n- [Improving LLM Leaderboards with Psychometrical Methodology](https://arxiv.org/pdf/2501.17200)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation\n\n## Description\nWe propose the Gated Many-Facet Rasch Model (G-MFRM), which extends the standard MFRM from educational measurement with a DG-IRT-inspired contamination gating mechanism to jointly calibrate model ability, item difficulty, judge severity, and contamination susceptibility within a single psychometric framework. The critical methodological advance over the original proposal is a hierarchical contamination parameterization: instead of an overparameterized per-(model,item) contamination term c_nk (N×I free parameters, unidentifiable), we decompose contamination into per-model susceptibility c_n modulated by per-item exposure indicators e_i, giving c_n · e_i (N+I parameters). This follows the LLTM (Fischer 1973) design-matrix tradition and the AMMI multiplicative interaction decomposition, both with established identifiability guarantees. Crucially, exposure indicators e_i are estimated externally via ConStat reference benchmark comparison (fully black-box, validated r²=0.94), temporal pre/post-cutoff signals, and LogProber Safe Scores (gray-box) — resolving the circularity of using model-internal residuals to identify contamination. A three-stage estimation strategy ensures identification: (1) standard 3-facet MFRM producing ability, difficulty, and severity estimates plus person-fit diagnostics; (2) external exposure estimation from ConStat and temporal proxies; (3) joint Gated MFRM with fixed exposure indicators and informative priors from Stages 1–2, implemented via Bayesian MCMC in NumPyro. The n-gram overlap signal is dropped for proprietary models (training data undisclosed) and retained only as supplementary validation for open-weight models. Validation spans MT-Bench, Arena-Hard, and WildBench using 8+ LLM judges (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick). We demonstrate that G-MFRM fair scores achieve higher Kendall-τ rank correlation with held-out Chatbot Arena human votes than raw multi-judge averages, CyclicJudge bias-only correction, DCR contamination-only adjustment, Preference Leakage calibration, and a naive two-stage pipeline (CyclicJudge → DCR). Additional analyses include exposure indicator ablation, judge count sensitivity, facet fit statistics, person-fit validation of contamination estimates, and robustness to adversarial contamination (per ICLR 2026 fragility findings). The unified framework yields interpretable per-model contamination estimates, per-judge severity calibrations, and fair ability rankings — bridging the gap between the judge bias correction and contamination detection research silos.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:13:04.620Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:13:04.620Z",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:13:04.631Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make a well-grounded assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model" (arXiv 2505.18486, May 2025):
   直接竞争工作。已将 MFRM 应用于 LLM 评分场景，比较了 10 个 LLM（GPT-4o、Claude 3.5 Sonnet、Gemini 等）与人类评分者的 rater effects。证明 MFRM 在 LLM-as-rater 场景下是可行的，但未涉及 contamination 矫正。本 proposal 的 "将 MFRM 引入 LLM 评估" 这一 claim 的 novelty 因此被显著削弱——核心框架的应用已有先例。

2. "CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation" (arXiv 2603.01865, March 2026):
   Proposal 明确列为 baseline。CyclicJudge 用 round-robin 分配消除 judge bias，证明在固定 budget 下是最优策略。方法极其简洁（无需训练，无需参数估计）。这构成了强有力的 trivial alternative 威胁——CyclicJudge 不需要 Bayesian MCMC 就能 "精确消除" bias。

3. "ConStat: Performance-Based Contamination Detection in Large Language Models" (NeurIPS 2024):
   Proposal 依赖 ConStat 作为外部 exposure 估计的核心信号源（claimed r²=0.94）。ConStat 本身是 black-box 方法，已在 NeurIPS 2024 发表，是成熟工具。Proposal 的 contamination 检测并非原创，而是 ConStat 的下游消费者。

4. "DCR: Quantifying Data Contamination in LLMs Evaluation" (EMNLP 2025):
   Proposal 明确列为 baseline。DCR 提供 contamination-aware adjusted accuracy，已解决 contamination 量化+调整的核心问题，但仅针对 benchmark 本身的 accuracy，未涉及 judge-as-evaluator 场景。

5. "Preference Leakage: A Contamination Problem in LLM-as-a-judge" (arXiv 2502.01534, Feb 2025):
   Proposal 列为 baseline。定义了 LLM-as-judge 特有的 contamination 问题（data generator 与 judge 的 relatedness），但处理方式是识别和量化，非 joint calibration。

6. "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines" (arXiv 2604.23178, April 2026):
   极其近期的 directly relevant 工作。首次在统一框架下比较 9 种 debiasing 策略 × 5 个 judge × 3 个 benchmark × 4 种 bias 类型。Proposal 未引用此工作。该工作的 meta-debiasing pipeline 可能与 G-MFRM 的定位形成直接竞争。

7. "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" (arXiv 2505.15055, May 2025):
   IRT 应用于 LLM 评估的代表性工作。表明 IRT/psychometric 方法在 LLM benchmark 领域已是活跃的、趋向拥挤的研究方向。

8. LogProber (arXiv 2408.14352, updated June 2025):
   Proposal 所依赖的 gray-box contamination 信号之一。已发表的独立工作，非 proposal 原创贡献。

- 调研总结: LLM-as-judge bias correction 和 benchmark contamination detection 分别已有成熟且活跃的研究线（CyclicJudge、"Judging the Judges" 等针对 bias；ConStat、DCR、Preference Leakage 针对 contamination）。MFRM 已被直接应用于 LLM rater 评估（2505.18486）。IRT/psychometric 方法在 LLM 评估领域已趋于拥挤。本 proposal 的核心定位——"joint bias + contamination correction"——是一个尚未被直接解决的 gap，但其每个组成部件均为现有工作的组合/应用，且存在强 trivial alternative（CyclicJudge + DCR 两阶段 pipeline）。


【Trivial Alternative 检验】:

存在明确的 trivial alternative：CyclicJudge（round-robin，零参数，已证明 budget 最优）+ ConStat/DCR 后处理过滤contaminated items。这个两阶段 pipeline：
- 不需要 Bayesian MCMC 推断
- 不需要 hierarchical parameterization
- 不需要 NumPyro 实现
- CyclicJudge 已被证明在固定 budget 下精确消除 bias

Proposal 自己也将 "naive two-stage pipeline (CyclicJudge → DCR)" 列为 baseline，但关键问题是：**joint calibration 相比这个 trivial pipeline 的增量价值有多大？** 如果 Kendall-τ 提升仅为 0.01-0.03，那么 G-MFRM 的复杂性（MCMC、三阶段估计、NumPyro pipeline）就难以 justify。

Proposal 的增量价值理论上在于：(a) bias 和 contamination 存在交互效应，joint model 能捕捉这种交互；(b) 产生可解释的 per-model contamination estimates 和 per-judge severity calibrations。但 (a) 是否成立是一个未验证的经验性假设，(b) 的实际价值取决于用户是否真正需要这些 interpretable diagnostics（而非仅需要一个 fair ranking）。


【前提假设检验】:

核心逻辑链中存在以下未经验证的关键假设：

1. **Contamination 的可加性/可乘性分解假设**：c_n · e_i 假设 contamination 效应可以分解为 model susceptibility × item exposure 的乘积形式。真实的 contamination 可能具有更复杂的结构——例如 partial memorization（模型记住了 item 的某些特征但非完整答案）、style contamination（通过训练数据中的相似文本而非直接暴露）。LLTM/AMMI 的 identifiability guarantee 成立的前提是分解结构正确，但这一前提本身未被验证。

2. **External exposure estimation 的充分性和准确性假设**：ConStat 的 r²=0.94 是在其原始验证场景下的数据。将其 exposure indicators 迁移到 MT-Bench、Arena-Hard、WildBench 等不同类型的 benchmark（对话质量评估 vs. 标准 NLP benchmark）时，是否仍然准确？对话评估 benchmark 的 contamination 模式可能与 ConStat 原始验证的 multiple-choice benchmark 有本质区别。

3. **Bias 和 contamination 的可分离性假设**：MFRM 框架将 judge severity 和 model contamination 作为独立 facets 处理。但在 LLM-as-judge 场景中，某些 "bias" 可能正是 contamination 的表现（例如 self-preference bias 本质上是一种 preference leakage/contamination）。如果两者存在 confounding，joint model 反而可能产生不可识别性问题。

4. **Rasch model 的单维性假设**：MFRM 假设 ability 是单维的。但 LLM 的 "ability" 在对话评估中是高度多维的（安全性、helpfulness、创造性、factuality 等）。这一假设违反可能导致 model misspecification。


【3 维度打分】:

1. **Novelty: 弱-中（偏弱）**
   - MFRM 已被应用于 LLM rater 评估（arXiv 2505.18486），核心框架的 "引入" 不再新颖。
   - IRT/psychometric 方法在 LLM 评估中已是拥挤方向（2505.15055, 2605.07046, 2605.00238 等）。
   - 每个组件（MFRM、ConStat、LogProber、CyclicJudge）均为现有工作的直接应用或消费。
   - 真正新颖的部分是 "joint bias + contamination calibration" 这一组合以及 hierarchical contamination parameterization，但这属于 incremental combination novelty 而非 conceptual breakthrough。
   - DG-IRT-inspired gating mechanism 虽然是合理的方法论选择，但本质上是将已有的 IRT contamination modeling 技术嫁接到 MFRM 上。
   - 审稿人大概率会评价为 "a technically competent integration of known techniques, but the novelty is limited to the combination itself."

2. **Significance: 中**
   - 研究问题本身重要且及时——LLM-as-judge 的 bias 和 contamination 是被广泛关注的问题（2025-2026 年有大量相关工作）。
   - 但 **"joint correction provides substantial improvement over sequential correction" 这一核心价值命题尚未被验证**。如果 joint model 仅带来边际提升，significance 会大幅下降。
   - 框架的适用范围有限：要求 8+ 个 LLM judges、ConStat 外部信号、LogProber access——这些条件在实际应用中可能不总是满足。
   - 产出的 interpretable diagnostics（per-model contamination, per-judge severity）具有一定实际价值，但审稿人可能会问 "who actually needs this granularity?"
   - **⚠️ 严重的会议匹配问题**：此 proposal 是纯 NLP evaluation/psychometrics 工作，与 CoRL（Conference on Robot Learning）的 scope 完全不匹配。CoRL 聚焦于 robot learning、manipulation、perception、control。即使 idea 质量可接受，在 CoRL 投稿几乎必然 desk reject。应投 ACL、EMNLP、NeurIPS、ICML 等。

3. **Related Work: 中-强（偏中）**
   - Proposal 覆盖了核心 baselines（CyclicJudge、DCR、Preference Leakage）和依赖工具（ConStat、LogProber）。
   - 定位清晰：将自己置于 "bias-only" 和 "contamination-only" 两条研究线的交汇点。
   - 但缺失了几个关键近期工作：
     * arXiv 2505.18486：直接将 MFRM 用于 LLM rater 评估——这是最直接的 prior art，未被引用是重大遗漏。
     * arXiv 2604.23178 "Judging the Judges"：统一框架比较 9 种 debiasing 策略——与 proposal 的 "unified framework" 定位直接竞争。
     * arXiv 2505.15055 "Lost in Benchmarks"：IRT 用于 LLM benchmarking 的代表性工作。
   - 这些遗漏可能导致审稿人质疑 novelty claim 的 credibility。


【概率估计】: 

对于 NLP/ML 顶会（ACL/EMNLP/NeurIPS）: [20% - 30%]，中位 25%
对于 CoRL 2026（用户指定会议）: [0% - 5%]，中位 2%

【估计理由】:

Idea 本身处于 "方向正确、有真实但有限的 novelty delta" 的档位。核心 claim 的逻辑链完整但不够 surprising——"将 bias correction 和 contamination correction 联合建模优于分开做" 这一结论如果成立，审稿人大概率会说 "makes sense, I would have guessed this"，而不会说 "surprising"。这把 idea 质量锚定在 25-35% 区间的下部。

进一步削弱的因素：(a) MFRM 用于 LLM 评估已有先例（2505.18486），novelty claim 的一条重要支柱被削弱；(b) CyclicJudge 作为 trivial alternative 的威胁真实存在——如果 CyclicJudge + DCR 两阶段 pipeline 效果接近，joint model 的复杂性难以 justify；(c) 核心前提假设（contamination 可乘性分解、ConStat 跨 benchmark 迁移性）未经验证。

Novelty（弱-中）是限制上界的主要维度——即使实验做得完美，一个 "technically sound integration of existing techniques" 在顶会的接受概率上界也受限。

**对于 CoRL 2026：这是一个纯 NLP evaluation/psychometrics proposal，与 CoRL 的 robot learning scope 完全不匹配，预期 desk reject。**

【主要风险】:

1. **Trivial alternative 风险**: CyclicJudge（零参数 round-robin）+ ConStat/DCR 后处理可能以极低成本达到 80-90% 的效果。如果 joint model 的提升不显著，整个工作的 value proposition 坍塌。审稿人几乎必然会追问 "What's the marginal gain of joint calibration over the naive pipeline?"

2. **Novelty 被挤压风险**: MFRM 用于 LLM 评估已有直接先例（2505.18486）；IRT for LLM evaluation 是拥挤方向；每个组件均非原创。审稿人可能判定 contribution 仅为 "engineering integration" 而非 "methodological advance"。
```

---

**⚠️ 附加重要提醒：会议选择问题**

此 proposal 是关于 LLM-as-judge 评估中的 psychometric calibration，属于 NLP evaluation methodology 领域。**CoRL (Conference on Robot Learning) 完全不是合适的投稿目标**——CoRL 聚焦于机器人学习、操控、感知、运动控制等。建议考虑 ACL、EMNLP、NeurIPS (Datasets and Benchmarks track)、或 COLM 作为投稿目标。会议匹配问题是独立于 idea 质量的，但会直接导致 desk rejection。

Sources:
- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)
- [ConStat: Performance-Based Contamination Detection in Large Language Models](https://arxiv.org/abs/2405.16281)
- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173.pdf)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)
- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)
- [Lost in Benchmarks? Rethinking Large Language Model Benchmarking with IRT](https://arxiv.org/abs/2505.15055)
- [LogProber: Disentangling confidence from contamination in LLM responses](https://arxiv.org/abs/2408.14352)
- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile the triage.

---

```
【阶段】: Triage

【⚠️ 严重的投稿方向问题】:
本 proposal 是一篇 LLM-as-Judge 评估方法论论文（心理计量学 + 污染检测），与 CoRL（Conference on Robot Learning）的收稿范围完全不匹配。CoRL 2026 Call for Papers 明确要求 "Submissions without a robotics focus will be returned without review"。该 proposal 不含任何机器人学习内容，投稿 CoRL 大概率会被 desk-reject。适合的目标会议应为 ACL / EMNLP / NeurIPS / ICML。以下评估基于 idea 本身质量，不考虑具体会议，但此方向性错误需首先纠正。

【领域调研】:
- [Dual Optimal: Make Your LLM Peer-like with Dignity](https://arxiv.org/abs/2604.00979) (arXiv 2026.04): **直接竞争**。已将 MFRM 应用于 LLM 评估，使用心理计量 IRT 校准协议来分离模型能力与 judge bias。与本 proposal 的核心框架高度重叠。
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865) (arXiv 2026.03): 提出 round-robin judge 分配策略，用单 judge 成本精确消除 bias。proposal 将其列为 baseline，定位合理。
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534) (arXiv 2025.02): 发现 judge-generator 关联性导致的偏好泄漏，提出该问题比已知 bias 更难检测。proposal 将其列为 baseline。
- [ConStat: Performance-Based Contamination Detection](https://arxiv.org/abs/2405.16281) (NeurIPS 2024): proposal 的核心外部信号之一。ConStat 通过参考 benchmark 比较检测污染，但其设计目标是闭卷 benchmark，对 MT-Bench 等开放式 benchmark 的适用性存疑。
- [LogProber: Disentangling confidence from contamination](https://arxiv.org/abs/2408.14352) (arXiv 2024-2025): proposal 使用的灰箱污染检测信号，提供 Safe Score。
- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://arxiv.org/abs/2507.11405) (arXiv 2025): 提供污染调整准确率（Acc_adj），proposal 将其列为 baseline。
- [A Judge-Aware Ranking Framework for Evaluating LLMs without Ground Truth](https://arxiv.org/abs/2601.21817) (arXiv 2026.01): **直接竞争但 proposal 未引用**。使用统计模型建模 judge bias 进行排名，有最大似然估计和渐近性质证明。
- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178) (arXiv 2026.04): 对 LLM-as-judge 偏差缓解策略的首个系统性统一 benchmark，proposal 未引用。
- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485) (arXiv 2026.03): 理论性更强的 judge bias 校正，proposal 未引用。
- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT](https://arxiv.org/abs/2505.15055) (arXiv 2025.05): PSN-IRT 框架对 benchmark 质量（含污染）的系统分析，发现广泛污染和测量质量问题。
- **"DG-IRT"**: proposal 声称受 "DG-IRT" 启发其 gating 机制，但多轮搜索未找到名为 "DG-IRT" 的已发表模型。该引用的真实性存疑。

- **调研总结**: IRT/心理计量方法应用于 LLM 评估是 2025-2026 年的活跃方向，多篇并行工作。MFRM 已被 Dual Optimal 应用于 LLM 评估。Judge bias 校正和 benchmark 污染检测各有独立的成熟工作，但将两者在统一框架内联合建模的工作尚未见正式发表。本 proposal 定位在 "bridging bias and contamination silos" 的交汇处，有一定差异化空间，但面临来自 Dual Optimal（MFRM 部分）和多个 bias 校正工作的挤压。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁：
1. **简单两阶段流水线**（CyclicJudge 去 bias → ConStat 标记污染项并移除）：工程成本极低，proposal 自身也列为 baseline。关键问题是 G-MFRM 的联合建模相比这个 pipeline 的增量收益是否实质性的（而非统计噪声范围内的微小 Kendall-τ 提升）。
2. **多样化 judge 集合 + 简单 trimmed mean / median**：使用 8+ 个不同 judge 然后取中位数，已经能大幅稀释单个 judge 的 bias 和 contamination 偏差。无需复杂框架。
3. **Judge-Aware Ranking Framework**（arXiv 2601.21817）已提供带理论保证的 judge bias 建模方案，可能以更简洁的方式达到类似效果。

增量价值论证尚不充分：proposal 声称 "higher Kendall-τ" 但这是待验证的 claim，且效果大小（effect size）未知。如果提升仅有 0.02-0.03 的 τ 差异，审稿人会质疑复杂框架的必要性。

【前提假设检验】:
核心 claim 的逻辑链条存在以下未验证假设：

1. **"污染在开放式 benchmark 中构成显著问题" — 未充分论证**。ConStat 和 DCR 的设计目标是闭卷 benchmark（MMLU、C-Eval 等有标准答案）。对 MT-Bench、Arena-Hard、WildBench 等开放式评估 benchmark，污染的定义、表现形式和严重程度完全不同。Preference Leakage 论文明确指出 "the issue of data contamination in open-ended benchmarks is less severe since there are no standard answers"。如果效应不显著，整个 contamination gating 机制就在解决一个不存在的问题。

2. **"污染效应可分解为 c_n · e_i（模型敏感度 × 题目暴露度）" — 强结构性假设**。这假设污染是可乘性分解的，但实际污染可能高度非线性：某些模型可能在特定题目上过拟合而在其他暴露题目上完全不受影响。乘法分解的适用性需要实证支持，而非仅靠 LLTM/AMMI 传统的类比论证。

3. **"ConStat 外部信号在开放式 benchmark 上可靠（r²=0.94）" — 迁移假设**。该 r² 数据来自 ConStat 原论文在闭卷 benchmark 上的验证。将其直接应用于开放式 benchmark 的 exposure indicator 估计，存在未验证的域迁移风险。

4. **"DG-IRT" 引用不可验证**。proposal 声称其 gating 机制受 "DG-IRT" 启发，但该模型在公开文献中不可查证。如果这是一个不存在的引用，会严重影响学术可信度。

【3 维度打分】:
  1. Novelty: 弱到中 — 
     MFRM 应用于 LLM 评估已被 "Dual Optimal"（2604.00979）实现，且 IRT 方法在 LLM 评估中已是 2025-2026 年的热点（PSN-IRT、Judge-Aware Ranking 等）。本 proposal 的增量 novelty 在于联合建模 judge bias 和 contamination 的 gating 机制，但：(a) 乘法分解 c_n · e_i 是标准 LLTM/AMMI 技术的直接应用；(b) 外部信号（ConStat、LogProber）均为现有工具的直接调用；(c) 三阶段估计策略本质上是"先分别估计，再联合微调"的常见 pipeline。如果审稿人已经看过 Dual Optimal 和 Judge-Aware Ranking，会认为本文是一个工程组合而非概念创新。核心发现如果 positive，审稿人的反应更可能是 "makes sense, I would have expected this to work" 而非 "surprising"。

  2. Significance: 中 — 
     研究问题本身（LLM-as-judge 评估的可靠性）是重要且时效性强的。2025-2026 年 LLM 评估可靠性是社区关注焦点。但本框架的实际影响力受限于：(a) 框架复杂度高（Bayesian MCMC + NumPyro + 三阶段 + 多外部信号），部署门槛远高于 CyclicJudge 等轻量方案；(b) 适用范围窄——仅针对 multi-judge 评估场景，而实践中很多评估只用单个 judge；(c) "bridging two silos" 的叙事虽有吸引力，但如果两个 silo 的分别解决方案（CyclicJudge + ConStat）简单组合就足够好，统一框架的实用价值就会大打折扣。

  3. Related Work: 弱 — 
     存在关键遗漏：(a) **Dual Optimal**（2604.00979）是最直接的竞争者（MFRM + LLM 评估），proposal 完全未提及；(b) **Judge-Aware Ranking Framework**（2601.21817）用统计模型处理 judge bias 并有理论保证，未引用；(c) **Judging the Judges**（2604.23178）对 bias 缓解策略的系统性评估，未引用；(d) **"DG-IRT"** 引用不可验证。此外，proposal 对现有工作差异化定位的论证依赖于 "没有工作同时处理 bias 和 contamination" 这一 gap，但没有充分论证为什么这两个问题必须在同一模型内联合处理（而非 pipeline 组合）。

【概率估计】: [15% - 25%] 中位 20%
（注：此估计基于 idea 质量投稿至 appropriate NLP/ML venue 如 ACL/EMNLP/NeurIPS。若投稿 CoRL，因完全超出收稿范围，估计为 ~0%，大概率 desk-reject。）

【估计理由】: 
Idea 处于 "方向站得住脚但内核薄弱" 区间。研究问题是真实的，但：(1) Novelty 受到 Dual Optimal 和 Judge-Aware Ranking 等并行工作的严重挤压，核心贡献更像工程组合而非概念创新；(2) trivial alternative（两阶段 pipeline）的威胁明确存在且 proposal 未充分论证增量价值；(3) 核心前提假设（污染在开放式 benchmark 上的显著性、c_n·e_i 分解的适用性）均未经验证。上界被 Novelty 维度限制——即使实验完美，审稿人仍会质疑 "what's genuinely new here beyond wiring existing tools into an existing model"。

【主要风险】: 
1. **Novelty 不足风险**：Dual Optimal 已将 MFRM 应用于 LLM 评估，Judge-Aware Ranking 已用统计模型处理 judge bias。审稿人会认为本文是在已有框架上叠加已有工具，增量 novelty 有限。
2. **前提假设崩塌风险**：如果开放式 benchmark 上的污染效应本就很小（Preference Leakage 论文的发现支持这一可能），整个 contamination gating 机制就成了过度工程化的解决方案，审稿人会质疑 "is this problem real enough to warrant this complexity?"
```

---

**Sources:**
- [Dual Optimal: Make Your LLM Peer-like with Dignity](https://arxiv.org/abs/2604.00979)
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)
- [ConStat: Performance-Based Contamination Detection in LLMs](https://arxiv.org/abs/2405.16281)
- [LogProber: Disentangling confidence from contamination in LLM responses](https://arxiv.org/abs/2408.14352)
- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://arxiv.org/abs/2507.11405)
- [A Judge-Aware Ranking Framework for Evaluating LLMs without Ground Truth](https://arxiv.org/abs/2601.21817)
- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)
- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/abs/2603.05485)
- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT](https://arxiv.org/abs/2505.15055)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [LLM-as-a-Judge: 2026 Guide](https://labelyourdata.com/articles/llm-as-a-judge)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a well-grounded assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. Jiao, Song & Lee, "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model" (arXiv 2505.18486, May 2025):
   直接用 MFRM 对 10 个 LLM 做 rater effect 分析，与人类评分者对比。证明 MFRM 已被应用到 LLM-as-judge 场景，本 proposal 的 MFRM 部分（Stage 1）不再是新贡献。

2. Choi et al., "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory" (arXiv 2602.00521, Jan 2026):
   用 GRM-IRT 对 LLM judge 的可靠性做两阶段诊断（intrinsic consistency + human alignment）。与本 proposal 共享 "用心理测量模型分析 LLM judge" 的核心思路，但未处理 contamination。

3. CyclicJudge (arXiv 2603.01865, Mar 2026):
   提出 round-robin judge 分配策略消除 judge bias，方差分解成 scenario/generation/judge/residual 成分。在 MT-Bench 和 MindEval 上验证。本 proposal 将其作为 baseline。

4. ConStat (NeurIPS 2024, de Koninck et al.):
   基于参考 benchmark 对比的 performance-based contamination 检测，报告 r²=0.94。本 proposal 依赖此作为外部 exposure indicator 来源。

5. DCR: Quantifying Data Contamination (EMNLP 2025):
   轻量级 contamination 量化框架，输出 DCR Factor 调整 raw accuracy，在 9 个 LLM 上误差 ≤4%。本 proposal 作为 baseline。

6. Preference Leakage (arXiv 2502.01534, Feb 2025, ICLR 2026 接收):
   揭示 LLM judge 与被评估模型同源时的 preference contamination，实验确认 bias 普遍存在。本 proposal 作为 baseline。

7. LogProber (arXiv 2408.14352, Aug 2024):
   基于 logprob 曲线面积检测 contamination 的灰盒方法。本 proposal 用作 exposure indicator 信号源之一。

8. "Lost in Benchmarks? Rethinking LLM Benchmarking with IRT" (arXiv 2505.15055, May 2025):
   用 IRT 重新审视 LLM leaderboard 排名不一致性，但未处理 judge bias 或 contamination。

9. Shu et al., "Using Deterministic Gated IRT Model to Detect Test Cheating due to Item Compromise" (psychometrics 文献):
   原始 DG-IRT 模型，用 gating 机制区分 compromised/uncompromised item 上的表现。本 proposal 的 contamination gating 直接源于此。

- 调研总结：IRT/MFRM 应用于 LLM 评估已成 2025-2026 热点方向，judge bias 和 benchmark contamination 各有成熟方法。但目前**两个子领域仍是独立的**：bias correction 工作（CyclicJudge、方差分解）不处理 contamination，contamination detection（ConStat、DCR、LogProber）不处理 judge bias。本 proposal 的定位是 **bridge this gap**，用单一心理测量框架统一两者。这个 "gap" 是真实存在的。

【Trivial Alternative 检验】:

最直接的 trivial alternative 是 proposal 自己已列出的 baseline：**naive two-stage pipeline (CyclicJudge → DCR)**——先用 CyclicJudge 做 judge bias 消除，再用 DCR Factor 做 contamination 调整。这个 pipeline 成本极低、实现简单。

Proposal 声称 joint estimation 优于 sequential pipeline 的关键论据是：bias 和 contamination 存在交互效应——一个 contaminated model 在 biased judge 面前会获得双重膨胀/压缩分数，sequential correction 无法捕获这种交互。这个论据在理论上成立，但 **交互效应的实际大小是一个未经验证的经验问题**。如果交互效应很小（例如 Kendall-τ 改善 < 0.02），则 joint framework 的额外复杂度（Bayesian MCMC、三阶段估计）难以justify。

**增量价值取决于交互效应的真实大小**。如果 joint > sequential 的 margin 是实质性的（τ 改善 > 0.05），则有清晰的增量价值；如果 margin 微小，则 trivial alternative 几乎等效。

【前提假设检验】:

1. **乘法分解假设 c_n · e_i**：假定 contamination 可分解为 "模型固有的 contamination 易感性" × "题目暴露程度"，这意味着一个模型对所有 exposed items 的 contamination 程度是按相同比例缩放的。实际上，contamination 可能是 item-specific 的（某些模型可能记住了特定题目而非按比例），这个乘法假设过于简化。虽然 proposal 引用 LLTM 和 AMMI 的 identifiability 保证，但 identifiability ≠ validity——模型可识别不等于模型正确。

2. **外部 exposure indicators 的准确性假设**：Stage 3 将 ConStat/LogProber 的 exposure 估计作为 **fixed** 输入。但 ConStat 的 r²=0.94 是在特定 benchmark 和特定条件下测得的，跨 benchmark/跨模型的泛化性未经验证。如果 exposure indicators 本身有系统偏差，整个 G-MFRM 的 contamination 估计会被污染。

3. **Chatbot Arena 人类投票作为 ground truth**：这是领域标准做法，但 Arena 投票本身有 selection bias（用户倾向提交特定类型 query）、population bias（用户群不代表general population）等已知问题。用它作为唯一的外部效标可能导致 "optimizing for Arena correlation" 而非真正的 "fair ability ranking"。

4. **Judge 数量假设**：8 个 judge 是否足够支撑 MFRM 的参数估计（N×I 个 observations 分散到 severity/ability/difficulty/contamination 参数）？多面 Rasch 模型通常要求每个 facet 有充足样本量，8 个 judge 的 severity 估计可能不稳定。这更偏实验设计问题，但也涉及 idea 的核心 claim 能否被验证。

【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是 "MFRM + contamination gating 的整合"。每个组件单独来看都不新：MFRM 已被 Jiao et al. (2505.18486) 用于 LLM 评估；contamination detection 有 ConStat (NeurIPS 2024)、DCR (EMNLP 2025) 成熟方案；IRT 用于 LLM-as-judge 有 Choi et al. (2602.00521)；DG-IRT gating 来自 psychometrics 文献。Novelty 在于 **特定的整合方式**（hierarchical parameterization c_n·e_i + external exposure indicators + three-stage estimation），这是合理但 **expected** 的工程整合——了解两个子领域的研究者都会想到 "为什么不把 bias correction 和 contamination detection 放在一起"。差异化不在于 "想到了"，而在于 "具体怎么做"，而具体做法（乘法分解、external indicators 作 fixed input、informative priors）都是心理测量学的标准技术。不够 surprising，但也不 trivial。

2. **Significance: 中** —
   研究问题本身重要且真实——LLM-as-judge 的 bias 和 contamination 确实是两个独立研究 silo，需要被统一。但 **实际影响面偏窄**：(a) 只影响运行 multi-judge LLM 评估的研究者/平台；(b) 核心发现若 positive（"joint > sequential"），审稿人大概率反应是 "I would have guessed this"——直觉上联合建模应该优于 sequential，这不 surprising；(c) per-model contamination 估计和 per-judge severity calibration 的 "可解释性" 是锦上添花而非刚需——实际使用者更关心最终排名质量而非中间参数。

3. **Related Work: 强** —
   Proposal 对两个子领域（judge bias: CyclicJudge; contamination: ConStat, DCR, LogProber, Preference Leakage）的覆盖全面，差异化定位清晰（"第一个统一两者的 psychometric framework"）。每个 baseline 都被明确命名并纳入实验对比。唯一的轻微不足是对 IRT-for-LLM 的最新工作（如 Choi et al. 2602.00521、"Lost in Benchmarks" 2505.15055）未明确提及其作为 related work 如何差异化。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】:
Novelty 是中等——整合的 idea 方向正确但 expected，核心发现若 positive 不具 surprise value（"joint > sequential" 是直觉预期）。Significance 中等——问题真实但受众窄、影响力有限。Related Work 强——定位清晰、baseline 全面，这会保护下限。三维综合来看，这是一篇 **solid integration paper**，但不是 idea-driven paper。上界被 Novelty 和 Significance 限制：缺乏 surprising/counterintuitive 的核心发现来推动分数进入 35%+ 区间。下界由 Related Work 的完整性和问题的真实性保护。

额外风险：**CoRL 2026 是 Conference on Robot Learning，而本 proposal 是纯 NLP/ML evaluation 方法论工作，与 robotics 完全无关。如果确实投 CoRL，几乎必然 desk reject。** 建议目标会议为 ACL/EMNLP/NeurIPS/ICML。此处概率估计基于 idea 质量本身（假设投对了 venue），不考虑 venue mismatch。

【主要风险】:
1. **Trivial alternative 威胁**：naive two-stage pipeline (CyclicJudge → DCR) 可能在实验中与 G-MFRM 表现接近（Kendall-τ 差距微小），使得整个复杂框架的增量价值被质疑为 "over-engineering for marginal gains"。
2. **"I would have guessed this" 风险**：核心 claim "joint calibration > sequential correction" 是直觉预期，审稿人可能认为这是一个 expected result 而非 surprising finding，导致 contribution 被低估。
```

Sources:
- [Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model](https://arxiv.org/abs/2505.18486)
- [Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory](https://arxiv.org/abs/2602.00521)
- [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865)
- [ConStat: Performance-Based Contamination Detection in Large Language Models](https://arxiv.org/abs/2405.16281)
- [DCR: Quantifying Data Contamination in LLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1173/)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)
- [LogProber: Disentangling confidence from contamination in LLM responses](https://arxiv.org/abs/2408.14352)
- [Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory](https://arxiv.org/abs/2505.15055)
- [Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise](https://www.researchgate.net/publication/257678777)
- [Improving LLM Leaderboards with Psychometrical Methodology](https://arxiv.org/pdf/2501.17200)


【原始 proposal（允许参考但不是主要依据）】:
# Gated Many-Facet Rasch Measurement for Joint Judge Bias and Contamination Correction in LLM Evaluation

## Description
We propose the Gated Many-Facet Rasch Model (G-MFRM), which extends the standard MFRM from educational measurement with a DG-IRT-inspired contamination gating mechanism to jointly calibrate model ability, item difficulty, judge severity, and contamination susceptibility within a single psychometric framework. The critical methodological advance over the original proposal is a hierarchical contamination parameterization: instead of an overparameterized per-(model,item) contamination term c_nk (N×I free parameters, unidentifiable), we decompose contamination into per-model susceptibility c_n modulated by per-item exposure indicators e_i, giving c_n · e_i (N+I parameters). This follows the LLTM (Fischer 1973) design-matrix tradition and the AMMI multiplicative interaction decomposition, both with established identifiability guarantees. Crucially, exposure indicators e_i are estimated externally via ConStat reference benchmark comparison (fully black-box, validated r²=0.94), temporal pre/post-cutoff signals, and LogProber Safe Scores (gray-box) — resolving the circularity of using model-internal residuals to identify contamination. A three-stage estimation strategy ensures identification: (1) standard 3-facet MFRM producing ability, difficulty, and severity estimates plus person-fit diagnostics; (2) external exposure estimation from ConStat and temporal proxies; (3) joint Gated MFRM with fixed exposure indicators and informative priors from Stages 1–2, implemented via Bayesian MCMC in NumPyro. The n-gram overlap signal is dropped for proprietary models (training data undisclosed) and retained only as supplementary validation for open-weight models. Validation spans MT-Bench, Arena-Hard, and WildBench using 8+ LLM judges (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Kimi K2.6, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick). We demonstrate that G-MFRM fair scores achieve higher Kendall-τ rank correlation with held-out Chatbot Arena human votes than raw multi-judge averages, CyclicJudge bias-only correction, DCR contamination-only adjustment, Preference Leakage calibration, and a naive two-stage pipeline (CyclicJudge → DCR). Additional analyses include exposure indicator ablation, judge count sensitivity, facet fit statistics, person-fit validation of contamination estimates, and robustness to adversarial contamination (per ICLR 2026 fragility findings). The unified framework yields interpretable per-model contamination estimates, per-judge severity calibrations, and fair ability rankings — bridging the gap between the judge bias correction and contamination detection research silos.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "859199c6-0985-4c84-8af3-a4930f87b8a2",
  "type": "user",
  "uuid": "949cc108-8069-43f0-93e7-2f695ee0866d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:13:04.630Z_

```json
{
  "parentUuid": "949cc108-8069-43f0-93e7-2f695ee0866d",
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
  "uuid": "f56597d6-52af-4439-8330-4fb0f571d566",
  "timestamp": "2026-05-20T03:13:04.630Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:13:04.630Z_

```json
{
  "parentUuid": "f56597d6-52af-4439-8330-4fb0f571d566",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "056b112f-4eb3-4973-95c1-dc7b1250222c",
  "timestamp": "2026-05-20T03:13:04.630Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make a well-grounded asse…",
  "leafUuid": "056b112f-4eb3-4973-95c1-dc7b1250222c",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint judge bias and contamination correction for LLM evaluation",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:13:45.251Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments systematically as Meta Judge.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Novelty: 弱-中（偏弱）
- Significance: 中 (but flagged CoRL mismatch as fatal)
- Related Work: 中-强（偏中）
- Probability (for NLP venue): [20%-30%] 中位 25%
- Probability (for CoRL): [0%-5%] 中位 2%


**Reviewer 2:**
- Novelty: 弱到中
- Significance: 中
- Related Work: 弱
- Probability (for NLP venue): [15%-25%] 中位 20%

**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability (for NLP venue): [22%-33%] 中位 27%

Now I'm calculating the aggregate statistics from these three probability estimates. The medians are 25%, 20%, and 27%, which gives me a mean of 24% and a median of 25%. I'm computing the standard deviation to understand the spread in their assessments.

The standard deviation comes out to about 2.94%, which suggests fairly tight agreement among reviewers on the overall acceptance probability. Now I'm looking at where the reviewers actually converge and where they diverge. All three flagged the venue mismatch as a fatal issue, and they all settled on medium significance. The novelty assessments cluster toward the weaker end, with reviewers 1 and 2 more critical than reviewer 3.

There's strong consensus that the two-stage pipeline combining CyclicJudge with DCR poses a serious threat to the paper's novelty claims. Similarly, all three reviewers questioned whether the multiplicative decomposition assumption holds without verification, and they all expressed concern about whether ConStat's strong performance on closed benchmarks would transfer to open-ended evaluation scenarios. On the MFRM application specifically, reviewers 1 and 3 cite the same prior work while reviewer 2 references a different paper, but they're all saying the same thing—this isn't a novel contribution.

The divergence starts to emerge when looking at related work coverage, where reviewer 1 takes a different stance than the others. 中-强, R2 says 弱, R3 says 强. This is a major divergence.
   - R2's "弱" is based on missing Dual Optimal (2604.00979), Judge-Aware Ranking (2601.21817), Judging the Judges (2604.23178), and DG-IRT unverifiable reference.
   - R3's "强" is based on comprehensive coverage of baselines and clear positioning.
   - R1 is in between, noting some missing works but overall decent coverage.
   - R2's concerns about missing works are substantive - Dual Optimal is a direct competitor. R3 may not have found Dual Optimal. I should weigh R2's assessment more heavily here since missing a direct competitor is a serious gap.

2. **DG-IRT reference verifiability**: R2 couldn't find it and flags it as potentially non-existent, but R3 located a psychometrics paper by Shu et al. on the Deterministic Gated IRT Model, which validates the reference. However, R2 raises a critical point about benchmark contamination severity - they cite the Preference Leakage paper showing contamination is less severe in open-ended benchmarks, whereas R1 and R3 only note the transfer risk without this nuance. If contamination isn't actually a problem for these benchmarks, the entire proposal might be addressing a non-issue.

3. **Consistency assessment**: The median standard deviation across reviewers is around 2.94%, putting us right at the boundary between high and medium consistency, and the rubric scores show notable divergence especially in Related Work ratings.

Given the medium consistency level, I should apply the stricter interpretation and use R2's assessment as the floor - they're at 20% median. For an appropriate NLP venue, the novelty is capped at weak-to-medium, significance is medium, related work is divergent but R2's missing Dual Optimal concern is substantive, there's strong consensus on the trivial alternative threat, and all three flag core assumption issues.

For the probability bounds, I'm settling on 15-28% with a median around 22%, while CoRL drops to essentially 1% given the unanimous desk reject assessment.

Looking at the implementation side, the approach relies on Bayesian MCMC inference through NumPyro, requires 8+ LLM judges which creates significant API costs, and uses external tools like ConStat and LogProber alongside standard benchmarks like MT-Bench and Arena-Hard with human votes as validation - the compute is moderate but the data collection is the real bottleneck.

The pipeline is mostly automated with minimal human intervention, no model training required since this is a psychometric framework rather than neural network work, no new benchmark creation needed, and the whole thing should take 2-3 months from implementation through experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "056b112f-4eb3-4973-95c1-dc7b1250222c",
  "isSidechain": false,
  "requestId": "req_011CbD6DPRq36ZYnXom36d74",
  "type": "assistant",
  "uuid": "edee3395-ccb2-4abb-929d-d3bc4aed1f99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vC9V4qVMm4dVXWuJg9iho",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14672,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4236,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14672
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

_source line 9 · 2026-05-20T03:14:38.213Z_

【阶段】: Meta Judge
【三次中位】: [25%, 20%, 27%]  std=2.9%
【共识维度】:
- **CoRL venue mismatch（致命）**: 3/3 审稿人一致判定本 proposal 与 CoRL（Conference on Robot Learning）收稿范围完全不匹配，几乎必然 desk reject。最强共识信号。
- **Novelty（弱-中）**: R1"弱-中偏弱"、R2"弱到中"、R3"中"。2/3 偏弱端，R3 稍宽松。核心共识：MFRM 已被应用于 LLM 评估（R1/R3 引 arXiv 2505.18486，R2 引 Dual Optimal 2604.00979），IRT/psychometric 方向已拥挤，整合本身是 expected engineering combination 而非 conceptual breakthrough。
- **Significance（中）**: 3/3 一致。问题真实但受众窄，核心发现若 positive 是 expected result（"I would have guessed this"），缺乏 surprise value。
- **Trivial alternative 威胁（强）**: 3/3 一致标记 CyclicJudge + DCR 两阶段 pipeline 为明确威胁，增量价值未经验证。
- **c_n · e_i 乘法分解假设（未验证）**: 3/3 一致质疑该结构性假设的适用性，identifiability ≠ validity。
- **ConStat 跨 benchmark 迁移风险（中）**: 3/3 均指出 r²=0.94 来自闭卷 benchmark，迁移到开放式 benchmark（MT-Bench、Arena-Hard、WildBench）未经验证。
- **框架复杂度过高风险（中）**: 3/3 均提到 Bayesian MCMC + NumPyro + 三阶段估计 + 多外部信号的复杂度门槛远高于轻量替代方案。

【异常维度】:
- **Related Work 判定严重分歧**: R2"弱"（基于 Dual Optimal 2604.00979、Judge-Aware Ranking 2601.21817 等关键遗漏）vs R3"强"（认为 baseline 覆盖全面、定位清晰）vs R1"中-强偏中"。处理方式：R2 指出的 Dual Optimal（直接将 MFRM 用于 LLM 评估）是实质性竞争者遗漏，R3 未检索到该工作导致评估过宽松。采信 R2 的具体证据，Related Work 综合评定为**中偏弱**——baseline 覆盖尚可但关键竞争者遗漏。
- **DG-IRT 引用可验证性**: 仅 R2 质疑"DG-IRT"不可查证。R3 找到了 Shu et al. 的心理测量学原始文献（"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise"），确认该引用存在。R2 的这一担忧被 R3 的发现化解，降权处理。
- **开放式 benchmark 污染严重性存疑**: R2 独立引用 Preference Leakage 论文原文证据——"the issue of data contamination in open-ended benchmarks is less severe since there are no standard answers"——质疑整个 contamination gating 机制是否在解决一个实际不显著的问题。R1/R3 提及迁移风险但未走到这一步。此异常点具有实质性威胁：若开放式 benchmark 污染效应本就微弱，整个 proposal 的 contamination 维度价值大幅缩水。不完全降权，标记为需验证的重要风险。

【最终概率】: [15% - 28%] 中位 22%
（注：以上为投稿至 appropriate NLP/ML venue（ACL/EMNLP/NeurIPS）的估计。若投 CoRL 2026：[0% - 3%] 中位 1%，近乎确定 desk reject。）

【一致性】: 中（std=2.9% 在边界，但 Related Work 维度存在跨审稿人严重分歧，整体偏中一致性；按规则偏向更严格的 R2）

【综合理由】:

三位审稿人在核心判断上高度收敛：(1) CoRL 完全不是合适的 venue；(2) Novelty 被 MFRM 已有 LLM 评估应用（2505.18486）和 IRT 方向拥挤显著压缩；(3) trivial alternative（CyclicJudge + DCR pipeline）威胁真实存在；(4) 核心假设（c_n·e_i 分解、ConStat 迁移性）均未经验证。

Novelty 综合定为**弱-中**：R1/R2 一致偏弱，R3 稍宽松但也仅给"中"。核心贡献是已有技术的工程整合，缺乏 conceptual surprise。这直接限制概率天花板——即使实验完美，"technically sound integration of known techniques" 在顶会的天花板约 30-32%。

Significance 综合定为**中**：3/3 一致。问题真实但核心发现是 expected result。

Related Work 综合定为**中偏弱**：R2 发现的 Dual Optimal（2604.00979）遗漏是实质性的——该工作已将 MFRM 用于 LLM 评估，是最直接的 prior art。R3 评"强"但未检索到这一竞争者，属于信息不完整导致的过宽松评估。R1 处于中间。采信 R2 的具体证据将此维度定为中偏弱。

处理分歧：Related Work 是唯一高分歧维度。按"宁缺毋滥"原则偏向 R2（最严格），因其提供了具体的遗漏证据（Dual Optimal、Judge-Aware Ranking）而非主观印象。

最终中位 22% 位于 R2（20%）与 R1（25%）之间、偏向 R2，反映了中一致性下偏严格的原则。上界 28% 低于 R3 的 33%，因 Related Work 降级和 R2 发现的竞争者遗漏进一步压缩了天花板。

【建议】: 不推荐（CoRL 2026）/ 边缘偏不推荐（NLP venue，需大幅修改）

核心问题不仅是 idea 质量（边缘），更是**会议选择完全错误**。若确实投 CoRL，建议 KILL。若改投 ACL/EMNLP/NeurIPS，idea 本身处于"有可行空间但需实质性加强"的档位，具体需要：(a) 补充 Dual Optimal 等关键竞争者的差异化论证；(b) 用实验或理论论证 joint calibration 相比 trivial pipeline 的实质性增量价值；(c) 验证或修正核心前提假设（开放式 benchmark 污染严重性、c_n·e_i 分解适用性）。

【实施评估】:
  - 计算资源: 中等。MCMC 推断本身可在单 GPU 或 CPU 集群上完成（NumPyro + JAX），但需运行 8+ LLM judge 对 3 个 benchmark 全量评测，API 调用成本约 $2,000-5,000（取决于模型定价和评测规模）。
  - 数据需求: MT-Bench、Arena-Hard、WildBench 均公开可得；Chatbot Arena 人类投票数据通过 LMSYS 公开数据集获取；ConStat 参考 benchmark 数据公开。数据获取无障碍。
  - 人工介入: 极少。全流程自动化，仅需人工设计实验配置和解读结果。无需人工标注。
  - 训练需求: 无需模型训练。核心是统计推断（Bayesian MCMC），非神经网络训练。NumPyro MCMC 采样时间预计数小时级（取决于数据规模和采样链数）。
  - 新 Benchmark: 不需要构建新 benchmark。使用现有公开 benchmark。
  - 预估周期: 2-3 个月。其中 LLM judge 评测数据收集约 2-3 周；ConStat/LogProber exposure 估计约 1 周；G-MFRM 实现 + 调试约 2-3 周；实验运行 + 分析约 2-3 周；论文撰写约 3-4 周。可并行压缩至 2 个月。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edee3395-ccb2-4abb-929d-d3bc4aed1f99",
  "isSidechain": false,
  "requestId": "req_011CbD6DPRq36ZYnXom36d74",
  "type": "assistant",
  "uuid": "94f132b9-89be-4c2f-bf4b-93fb6fcbd471",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vC9V4qVMm4dVXWuJg9iho",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14672,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4236,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14672
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make a well-grounded asse…",
  "leafUuid": "94f132b9-89be-4c2f-bf4b-93fb6fcbd471",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint judge bias and contamination correction for LLM evaluation",
  "sessionId": "25902491-0c31-4aa9-8a18-f63aa0c72ebc"
}
```

---
