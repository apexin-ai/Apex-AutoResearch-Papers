# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/af047939-0d18-428f-9efd-271e8167c3b0.jsonl`
- **Structured JSON:** [`567f5f0e8b59c6a399b5.json`](../../sessions/56/567f5f0e8b59c6a399b5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T01:55:13.014Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T01:55:13.014Z",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough assessment. Here is my evaluation:\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】:\n存在一个严重的 trivial alternative 威胁，proposal 未充分回应：\n\n**为什么不对所有 retrieval call 都使用 hybrid BM25+dense+NLI reranking？** 如果 NLI-based contrastive reranking 能提高 verification query 的质量，为什么它不会同时提高 discovery query 的质量？proposal 声称 BM25 适合 discovery 因为\"keyword-rich\"，但这是假设而非论证。一个不需要任何 intent classification 的 trivial baseline —— 统一使用更强的 hybrid pipeline —— 可能达到类似效果且更简单。如果这个 baseline 表现接近，那么 intent classification 的增量价值（也就是整篇论文的核心贡献）就被消解了。\n\nProposal 计划了 BM25-only ablation（dual-intent tokens + 标准 retrieval），但这测试的是 \"intent tokens 本身有没有用\"，而非 \"intent classification vs. 统一用更强 pipeline\"。真正致命的 ablation 是：**对所有 query 统一使用 hybrid+NLI，不做 intent classification**。这一组被遗漏。\n\n第二个 trivial alternative：AutoRefine 的 &lt;refine> step 在 post-retrieval 阶段蒸馏证据，已经在 HotpotQA/MuSiQue 上取得了大幅提升。如果 post-retrieval refinement 能弥补 query construction 阶段的不足，upstream 的 intent differentiation 增量价值可能很小。\n\n**增量价值辩护（proposal 可以但未能做到的）：** intent classification 的真正价值应该在于 verification mode 主动寻找 disconfirming evidence（通过 contrastive query），这是一种 structurally different 的检索意图，不能通过简单使用更强的 pipeline 来实现。但 proposal 对\"为什么 disconfirming evidence 不能通过统一 pipeline 获取\"的论证薄弱。\n\n\n【前提假设检验】:\n核心 claim 的逻辑链中有 3 个未经充分验证的假设：\n\n1. **\"Verification query 需要 disconfirming evidence，而这与 topical relevance 信号反相关\"** —— 这是核心逻辑的关键环节，但论证不足。包含 refuting evidence 的文档往往也是高度 topically relevant 的（例如，反驳 \"X 出生在纽约\" 的文档通常也是关于 X 的）。真正反相关的是 evidential valence 和 retrieval signal，但 dense retrieval 的 semantic matching 本身并不只优化 topical relevance —— 它可以捕捉到 semantic 层面的 contrastive 关系。这个假设如果不成立，整个 \"为什么需要 differentiated pipeline\" 的论证就塌了。\n\n2. **\"Heuristic rules 可以可靠地从 reasoning traces 中分类 intent\"** —— 虽然设置了 75% accuracy 的 go/no-go 门槛，但 heuristic classification 的噪声在 RL 训练中会被放大。如果 30% 的 intent labels 是错误的，RL 在错误 label 上训练的 query construction 策略可能比不分类更差。Proposal 假设 \"默认 fallback 到 discovery 是安全的\"，但如果 heuristic 把 discovery 错标为 verification（false positive），会在不需要 contrastive query 的地方强行使用 contrastive pipeline，可能降低性能。\n\n3. **\"500 GRPO steps 足以让 RL 发现 sophisticated verification query strategies\"** —— 这被定位为 \"co-equal contribution\"，但 RL 在 500 steps 内是否能在 query formulation 这个 secondary action space 上学到 beyond-template 的策略是未经验证的。Proposal 引用 RAFTS 证明 \"LLM-generated contrastive formulations outperform templates\"，但 RAFTS 使用的是大模型 zero-shot generation，不是 7B 模型在 500 RL steps 内学习的结果。将一个希望性发现定位为 co-equal contribution 是有风险的。\n\n\n【3 维度打分】:\n\n1. Novelty: 【弱-中】\n   \n   核心贡献是 \"operationalize an existing observation\" —— 将 ReaLM-Retrieve Section 6.9 中已经识别出的 verification retrieval pattern 显式化，配以不同的检索 pipeline。这是一个 natural next step，而非 surprising insight。任何仔细阅读 ReaLM-Retrieve 的研究者都可能想到 \"为什么不根据 intent 使用不同策略\"。\n   \n   与最相关 5-10 篇近期工作比较后的真实 novelty delta：\n   - vs. ReaLM-Retrieve: delta 是 \"显式分类 + 不同 pipeline\"，属于 operationalization\n   - vs. Veri-R1: delta 是 \"differentiated query construction\"，但 Veri-R1 本身只用 3B 模型，场景不完全可比\n   - vs. RAFTS: delta 是 \"集成到 RL 循环\"，属于 integration\n   - vs. AutoRefine: delta 是 \"pre-retrieval intent 分类 vs. post-retrieval refinement\"，是互补而非替代\n   - vs. HARIS: delta 是 \"binary intent + differentiated pipeline vs. hierarchical agents\"，不同设计但解决类似问题\n   \n   剔除 surface differences（不同的 token format、不同的 pipeline 组合）之后，核心 insight 只有一条：**retrieval intent 应该被显式分类并用不同策略处理**。这更接近 engineering contribution 而非 conceptual breakthrough。\n   \n   第二个贡献 \"RL-discovered query strategies\" 在实验之前只是一个希望，不能作为 novelty 评估的依据。\n\n2. Significance: 【中】\n   \n   研究问题是重要的 —— reasoning-augmented retrieval 是当前 NLP 的热点方向，如何提升 retrieval 质量确实是关键瓶颈（Shakya et al. 2026 的发现强化了这一点）。\n   \n   但显著性受限于：\n   - **结果预期方向的可预测性**：如果 differentiated retrieval 表现更好，审稿人大概率会说 \"I would have guessed this\" 而非 \"surprising\"。Binary intent classification 提升性能是直觉上合理的结果。\n   - **问题的窄度**：这是 reasoning-augmented RAG 中 query construction 阶段的一个 specific 优化。影响面限于使用 RL-trained reasoning+retrieval 的系统。\n   - **可推广性受限**：binary taxonomy（discovery/verification）是否是最优分类？框架声称可扩展，但论文只测试 binary。\n   \n   如果结果是 negative（differentiation 不帮助或帮助很小），论文的贡献更多是 empirical insight（\"显式分类不如隐式学习\"），这也有价值但 significance 更低。\n\n3. Related Work: 【强】\n   \n   Related work 覆盖极为全面。我在 web search 中未找到 proposal 遗漏的重要近期工作。对每篇相关工作的差异化定位准确且清晰。特别值得肯定的是：\n   - 对 ReaLM-Retrieve、Veri-R1、HARIS 等最近期工作的深入分析\n   - 对 gap 的结构化总结（5 个轴向的系统化梳理）\n   - 对每个相关方法\"做了什么 + 没做什么\"的精确定位\n   \n   这是整个 proposal 最强的部分。唯一微弱的遗漏：没有充分讨论 FAIR-RAG（adaptive iterative refinement）和 Q-PRM（adaptive query rewriting），但这些不直接威胁 novelty claim。\n\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】:\nRelated Work 维度强（不拉后腿），但 Novelty 弱-中 和 Significance 中 共同限制了上界。\n\n核心问题在于：这篇论文的 intellectual contribution 是 \"operationalize an existing observation with known techniques\"。Binary intent classification 是 obvious next step；hybrid BM25+dense+NLI 是已知技术的组合；GRPO training 是在 Search-R1 框架上的增量修改。审稿人最可能的反应是 \"reasonable engineering contribution, but the core idea is not surprising enough for main conference\"。\n\n概率没有落入 15-18% 区间是因为：(a) gap 确实存在且被充分论证，(b) related work 定位清晰，(c) 如果 RL-discovered query patterns 出现 surprising 结果，论文有上行空间。但这个上行空间依赖于实验结果，而非 idea 本身的质量。\n\n概率没有达到 28%+ 是因为：(a) trivial alternative 威胁严重且未回应，(b) 核心 claim 的前提假设（disconfirming evidence 与 topical relevance 反相关）论证薄弱，(c) \"RL-discovered strategies\" 作为 co-equal contribution 在实验前是空洞的。\n\n**限制上界的关键维度是 Novelty** —— 即使 significance 提升到\"中-强\"，idea 的 incremental nature（operationalize + integrate known techniques）在 top-tier 会议上是硬伤。\n\n【主要风险】:\n1. **Trivial alternative 被审稿人发现**：审稿人大概率会问 \"为什么不对所有 query 统一使用你的 hybrid+NLI pipeline？如果统一使用更强 pipeline 效果接近，intent classification 的价值在哪？\" 如果这组 ablation 结果不利，论文核心贡献被消解。\n2. **\"Operationalize an obvious observation\" 被视为 incremental**：核心 insight 来自 ReaLM-Retrieve 的 Section 6.9，proposal 本质上是 \"take their observation and act on it\"。审稿人可能判定这是一个 well-executed follow-up study 而非独立的 main conference contribution，尤其在 novelty 维度给出 borderline-reject 分数。\n```\n\nSources:\n- [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384)\n- [HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification](https://arxiv.org/html/2506.07528v1)\n- [Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation](https://arxiv.org/html/2603.10143)\n- [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/pdf/2503.09516)\n- [RAFTS: Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments](https://arxiv.org/html/2406.09815v1)\n- [ReaLM-Retrieve: When to Retrieve During Reasoning](https://arxiv.org/html/2604.26649)\n- [DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop QA](https://arxiv.org/html/2504.18243)\n- [FAIR-RAG: Faithful Adaptive Iterative Refinement for RAG](https://arxiv.org/html/2510.22344v1)\n- [Q-PRM: Adaptive Query Rewriting for RAG](https://aclanthology.org/2025.findings-emnlp.817.pdf)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】:\n\n存在两个严重的 trivial alternative 威胁：\n\n1. **统一使用 hybrid BM25+dense+NLI reranking 处理所有 query（无需 intent 分类）**：\n   如果 hybrid retrieval + NLI reranking 对 verification query 有效，为什么不对所有 query 都使用它？Proposal 声称 BM25 对 discovery query \"更合适\"因为它们是 keyword-rich 的，但这只能论证 BM25 不差，不能论证 hybrid 会更差。一个 reviewer 完全可以要求一个 \"uniform hybrid for all queries\" baseline——如果它表现接近，则 intent classification 的增量价值趋近于零。Proposal 没有讨论这个 trivial alternative。\n\n2. **让 RL 隐式学习 query 差异化（无需显式 intent token）**：\n   在 Search-R1 的 RL 训练中，模型已经可以自由生成任意 query 文本。如果 reward signal 足够清晰（EM + faithfulness），模型应该自然学会在需要验证时写出 contrastive query，无需 &lt;discover>/&lt;verify> 的显式约束。显式 intent token 可能反而限制了模型的灵活性。这个 alternative 的增量成本几乎为零（只是调整 reward），却可能达到类似效果。Proposal 的反论（\"implicit adaptation cannot capture the distinction because verification is anti-correlated with topical relevance\"）存在逻辑跳跃——RL 优化的是下游 EM/F1，不是 topical relevance。\n\n增量价值在于：如果可以证明 (a) uniform hybrid 显著不如 differentiated pipeline，且 (b) 显式 intent token 显著优于让 RL 隐式学习差异化，则 intent classification + differentiated pipeline 的组合有真实增量。但这两个条件目前都是未验证假设。\n\n【前提假设检验】:\n\n核心逻辑链条中存在以下未验证假设：\n\n1. **\"隐式 query adaptation 无法捕捉 discovery/verification 区分\"**（最关键假设）：\n   论证基于 \"verification 需要 disconfirming evidence，而 learned query generator 优化 topical relevance\"。但 RL-trained query generator（如 Search-R1）优化的是下游任务表现（EM/F1），不是 topical relevance。如果 disconfirming evidence 有助于提高 EM，RL 应当能隐式学会检索它。这个论证把 dense retriever 的训练目标与 RL policy 的训练目标混为一谈。\n\n2. **\"ReaLM-Retrieve Section 6.9 的 31% verification rate 可推广到 Search-R1 + Qwen2.5-7B 设置\"**：\n   ReaLM-Retrieve 使用 DeepSeek-R1-Distill-Qwen-32B 且有自己的 QueryGen 架构，其观察到的 verification pattern 可能与模型规模和架构高度相关。在 7B 模型 + 不同 RL 框架下，verification retrieval 是否仍然是一个 distinct 且 beneficial 的 pattern 是未知的。\n\n3. **\"|entailment - contradiction| 是 verification retrieval 的正确 reranking 信号\"**：\n   一个文档可以与 claim 有强 entailment/contradiction 关系但事实上不相关或不可靠。这个指标衡量的是 NLI 模型的判断置信度，不一定等于 \"evidentially informative\"。\n\n4. **\"二元分类（discovery/verification）是最优粒度\"**：\n   这个假设虽有合理论证（minimal distinction capturing most variance），但本质上是便利性选择而非有理论支撑的设计。实际 reasoning chain 中的 retrieval intent 可能有更丰富的结构（clarification, comparison, quantification 等）。\n\n【3 维度打分】:\n\n  1. Novelty: 【弱-中】 — 核心贡献是 \"operationalize an observation from ReaLM-Retrieve\"——将 ReaLM-Retrieve 自己观察到但未利用的 discovery/verification 区分变为显式机制。这是一个合理但 obvious-in-hindsight 的 next step：任何读过 ReaLM-Retrieve Section 6.9 的研究者都会想到\"既然 verification retrieval 有不同 pattern，为什么不做不同处理\"。Intent classification + differentiated pipeline 的组合在 reasoning-augmented RAG 中是新的，但各组件（BM25/dense hybrid、NLI reranking、contrastive query、RL token format）都来自已有工作的直接拼装。\"RL-discovered query strategies\" 作为 co-equal contribution 是投机性的——它依赖于一个尚不确定的实验发现，不构成方法论创新。与最相关 5-10 篇近期工作比较后，剥离 surface differences 剩余的 novelty delta 是：显式 intent token + pipeline routing。这是一个 engineering-level 的差异，而非 conceptual-level 的。\n\n  2. Significance: 【中】 — 研究问题本身是重要的：reasoning-augmented retrieval 中 query construction 的质量确实是瓶颈，这一点被 Shakya et al. (2026) 和 ReaLM-Retrieve 的 failure analysis 共同证实。但这个 specific proposal 的影响力受限于：(a) binary intent taxonomy 可能过于粗糙，预期改进幅度有限；(b) 即使 positive，结果大概率是 \"moderate improvement on benchmarks\"（~2-5% F1），reviewer 会说 \"I would have guessed this would help a bit\"，不会说 \"surprising\"；(c) 方法的可推广性受限于需要 NLI reranker 和 dense retriever 的额外基础设施，增加了 deployment 复杂度。不过，如果 RL-discovered query patterns 分析做得好，有一定的 analytical insight 价值。\n\n  3. Related Work: 【强】 — 这是 proposal 最突出的优点。对 2024-2026 年的 reasoning-augmented retrieval 领域做了非常系统的梳理，沿 5 个维度（implicit adaptation, timing/volume control, reasoning-retrieval coordination, post-retrieval quality, verification）清晰分类，差异化定位明确。ReaLM-Retrieve、Veri-R1、AutoRefine、CoRAG、DeepControl、RAFTS、HARIS、Reason and Verify 等均有准确描述和定位。Gap identification 是 genuine 的——确实没有现有系统在 sequential reasoning chain 中做 explicit intent classification + differentiated query construction。唯一的小瑕疵是对 ReaLM-Retrieve Section 6.9 的数据过度依赖作为动机的全部基础。\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】:\nRelated Work 的覆盖和 gap identification 是 strong 的，证明了作者对领域的深入理解，这为论文的 \"positioning\" 质量提供了保底。但 Novelty 是核心限制因素：idea 的本质是 \"operationalize an obvious next step from ReaLM-Retrieve's observation\"，属于 incremental engineering contribution 而非 conceptual breakthrough。更严重的是，两个 trivial alternative（uniform hybrid for all, implicit RL learning）构成真实威胁，且 proposal 中未充分讨论。Significance 受限于预期结果的 \"I would have guessed this\" 性质——即使 positive results，审稿人不太可能认为 surprising。综合来看，这是一个 \"方向正确、positioning 优秀但 idea 内核偏薄\" 的 proposal，典型的 25% 区间。但 trivial alternative 威胁和核心假设的逻辑跳跃将上界压到 ~28%，中位值降至 22%。\n\n【主要风险】:\n1. **Trivial alternative 致命威胁**：Reviewer 几乎必然要求 \"uniform hybrid retrieval for all queries\" baseline，如果该 baseline 接近 dual-intent 的表现，则 intent classification 的增量价值被否定，论文核心贡献坍塌。\n2. **核心前提的逻辑跳跃**：\"implicit adaptation cannot capture discovery/verification distinction because verification is anti-correlated with topical relevance\" 的论证将 dense retriever 的训练目标与 RL policy 的训练目标混淆——RL 优化下游 EM/F1，不是 topical relevance。如果 RL 本身就能隐式学会差异化 query construction，显式 intent token 可能是多余的 inductive bias。\n```\n\n**补充说明**：\n\n这个 proposal 在**形式完善度**上是顶级的——compute budget 精确到小时、NLI model separation 的 circularity 论证、per-step training calibration、contingency plan 等都显示了极高的工程规划能力。但正如评估原则所强调的，形式完善度 ≠ idea 好。透过这些精心设计的细节看本质，核心 claim 是：\"显式区分 retrieval intent 并用不同 pipeline 处理比让 RL 隐式学习更好\"——这个 claim 的说服力取决于是否能排除 trivial alternatives，而这恰恰是 proposal 目前最薄弱的环节。\n\nSources:\n- [ReaLM-Retrieve: When to Retrieve During Reasoning](https://arxiv.org/abs/2604.26649)\n- [Veri-R1: Claim Verification via Online RL](https://arxiv.org/abs/2510.01932)\n- [AutoRefine: Search and Refine During Think](https://arxiv.org/abs/2505.11277)\n- [Search-R1: Training LLMs to Reason and Leverage Search Engines](https://arxiv.org/abs/2503.09516)\n- [HARIS: Coordinating Search-Informed Reasoning](https://arxiv.org/abs/2506.07528)\n- [Contrastive Retrieval-Augmented Generation on Experience](https://aclanthology.org/2025.findings-acl.1224.pdf)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】:\n\n存在两个有威胁性的 trivial alternatives：\n\n1. **\"All-Hybrid\" baseline**: 对所有 retrieval call 一律使用 hybrid BM25+dense + NLI reranking，完全跳过 intent 分类。如果 hybrid retrieval 本身就优于 BM25-only（proposal 自己引用了 \"hybrid retrieval improves recall by 15-30%\"），那最简单的做法就是对所有 query 都用 hybrid pipeline。Intent 分类的增量价值只有在\"discovery queries 用 hybrid 反而变差\"时才成立——这是一个未经验证的假设。Proposal 暗示\"contrastive query 可能干扰 exploratory retrieval\"，但这缺乏理论或实证依据。如果 all-hybrid 的性能与 dual-intent 差异不大（例如 <1% F1），审稿人会说\"the classification adds complexity without commensurate gain\"。\n\n2. **AutoRefine-style post-retrieval refinement**: AutoRefine 已经在相同 framework (Search-R1/veRL/GRPO) 上通过 post-retrieval evidence distillation 实现了大幅提升（HotpotQA: 0.405 vs 0.297, MuSiQue: 0.157 vs 0.066）。如果 post-retrieval refinement 能在不修改 query construction 的情况下达到类似效果，那 dual-intent retrieval 的增量价值就被大幅压缩。Proposal 需要证明 query construction differentiation 提供的增益是 orthogonal to（且无法被替代 by）post-retrieval refinement。\n\n增量价值声称点：proposal 认为 verification query 需要\"actively seek disconfirming evidence, which is anti-correlated with topical relevance\" —— 这是其最核心的理论支点。但这个论点本身是 assertion 而非 evidence：没有实证表明 learned query generators 无法隐式学到这一点，也没有理论解释为什么 continuous embedding space 在数学上无法编码 contrastive retrieval intent。\n\n【前提假设检验】:\n\n核心逻辑链: \"ReaLM-Retrieve 观察到 verification retrieval 是一个 distinct pattern → 这种 pattern 需要 structurally different queries → explicit classification + differentiated pipelines 优于 implicit adaptation → binary taxonomy 足以捕捉 intent variation\"\n\n逻辑链中的未验证假设：\n\n(a) **\"Implicit adaptation 无法 capture 这个 structural distinction\"**: Proposal 断言 \"Implicit query adaptation via learned representations cannot capture this structural distinction because a verification query should actively seek disconfirming evidence, which is anti-correlated with the topical relevance signal.\" 这是整个 idea 最关键的假设，但它缺乏支撑。ReaLM-Retrieve 的 QueryGen 是 learned cross-attention，理论上完全可以在 continuous space 里编码 contrastive intent —— 只是 ReaLM-Retrieve 没有显式优化这一点，不等于 continuous representation 原则上做不到。如果一个更好训练的 implicit query generator 就能解决问题，显式分类就变成不必要的 overhead。\n\n(b) **Binary taxonomy 的充分性**: ReaLM-Retrieve 识别了三种 pattern (early resolution 42%, verification 31%, failed retrieval 12%)。Proposal 将 early resolution 和 failed retrieval 合并为 \"discovery\"，但 early resolution (已找到答案但还在 retrieval) 和 genuine exploration (需要新信息) 的 retrieval needs 截然不同。这种强制合并可能丢失重要信息。\n\n(c) **Heuristic classification 的可靠性**: 用文本匹配 (\"therefore\", \"this means\") 来分类 intent 是一个相当粗糙的 proxy。Reasoning traces 中 claim-like statements 和 question-like statements 可能没有清晰的语法分界，特别是在 Qwen2.5-7B 这个 scale 的模型上。75% heuristic accuracy 是一个 low bar，意味着 25% 的 intent 被错分，在 RL training 中可能引入 systematic noise。\n\n(d) **NLI reranking by |entailment − contradiction| 能 surface 高质量 verification evidence**: DeBERTa-v3-base NLI 模型在 out-of-domain Wikipedia passages 上的 entailment/contradiction 判断可能不够 reliable，特别是对于隐含的、需要推理的 claims。如果 NLI scoring 本身噪声很大，整个 verification pipeline 的信号质量就会被拖累。\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   — 核心 gap 是真实的：目前确实没有系统在 reasoning chain 内做 explicit intent classification + differentiated query construction。搜索确认了这一点。\n   — 但 novelty 的\"真实程度\"需要打折：(i) 核心 insight 直接来自 ReaLM-Retrieve Section 6.9 的观察，proposal 自称 \"we make it actionable\"——这是 operationalization，不是 discovery；(ii) 各个组件（BM25、dense retrieval、NLI reranking、GRPO training、intent tokens）全部是已有的，组合方式虽然新但属于 engineering novelty；(iii) \"co-equal contribution\" 的 RL-discovered query strategies 完全是 speculative，属于\"如果结果好就是 novelty\"的 outcome-dependent claim。\n   — 与最相关 5 篇近期工作（ReaLM-Retrieve, Veri-R1, AutoRefine, CoRAG, RAFTS）比较，剔除 surface differences 后剩余 novelty：一个 binary intent classifier + routing logic。这是 real but thin。\n\n2. Significance: 【中】\n   — 研究问题本身重要：reasoning-augmented retrieval 是 2025-2026 的热点方向，intent-aware retrieval 是一个 natural next step。\n   — 但 \"surprising\" 测试不通过：如果核心发现是 positive（intent-differentiated retrieval 优于 uniform retrieval），大多数审稿人会说 \"I would have guessed this — of course different retrieval needs benefit from different strategies.\" 缺乏反直觉元素。\n   — 方法高度耦合于 Search-R1/veRL/GRPO 框架，推广性有限。结论是否能 generalize 到其他 reasoning-retrieval systems (如 proprietary models 的 tool use) 不清楚。\n   — 如果 improvement 幅度较小（如 1-2% F1），这个 significance 会进一步下降。\n\n3. Related Work: 【强】\n   — 覆盖非常全面：ReaLM-Retrieve, Veri-R1, CoRAG, AutoRefine, DeepControl, RAG-Star, RAFTS, HARIS, AgentIR, Reason and Verify, R1-Searcher++, REPAIR, FIRE 等均有覆盖。\n   — 差异化定位清晰：对每篇工作都精确说明了\"它做了什么、不做什么、和我们的区别在哪\"。\n   — 搜索验证后确认：proposal 声称的 gap（没有系统在 sequential reasoning chain 内 explicitly classify intent + differentiate query construction）在我搜索范围内是成立的。\n   — 唯一小问题：HARIS (Jun 2025) 的两层 agent 架构中 reasoning agent 向 search agent 委派\"targeted queries\"，这与 intent differentiation 有一定相似性，proposal 可以更细致地区分。\n\n【概率估计】: [22% - 32%] 中位 27%\n\n【估计理由】:\nRelated Work 维度是强项，说明 gap 定位准确、positioning 清晰。但概率上限被 Novelty 和 Significance 共同压制：\n\n(1) Novelty 是 operationalization 而非 discovery —— 核心 insight 借自 ReaLM-Retrieve，组件全部已有，真正的 delta 是 routing logic + 一个 binary classifier，这在 EMNLP 主会的 novelty bar 下偏薄。\n\n(2) Significance 受限于 \"I would have guessed this\" 效应 —— positive result 不 surprising，negative result 也不 surprising（因为 heuristic classification 可能太粗糙）。缺乏无论结果如何都能产出深刻 insight 的 dual-outcome 保障。\n\n(3) Trivial alternative 威胁真实存在 —— all-hybrid baseline 和 AutoRefine-style post-retrieval refinement 都可能 match 或 subsume 大部分 gain，审稿人很可能要求这两个 ablation，而 proposal 的 compute budget 已经非常紧张。\n\n(4) \"Co-equal contribution\"（RL-discovered query strategies）是 outcome-dependent —— 如果 RL 没有发现有趣的 query patterns，这个 contribution 就不存在，论文变成单纯的 intent routing + 小幅性能提升。\n\n(5) 竞争激烈：RAG+Reasoning 是 2025-2026 最拥挤的赛道之一，EMNLP 在这个方向的 submission 密度极高，incremental improvements 的接受门槛显著提高。\n\n概率区间 22-32% 反映了：idea 方向正确、gap 真实、positioning 清晰（下限不低于 22%），但 novelty thin + 预期结果不 surprising + trivial alternative 威胁（上限被压制在 32%）。\n\n【主要风险】:\n1. **Trivial Alternative 致命威胁**：All-hybrid baseline（对所有 query 统一使用 hybrid BM25+dense + NLI reranking，不做 intent 分类）可能达到与 dual-intent 相近的性能。如果 ablation 证明 intent classification 的 marginal gain 很小，整个 paper 的 contribution 会塌缩为 \"we confirmed that hybrid retrieval is better than BM25-only\"——这不是一个 publishable finding。\n2. **\"Expected Result\" 风险**：核心发现若为 positive，审稿人大概率反应为 \"intuitive, not surprising\"。缺乏反直觉元素意味着论文必须靠 (a) 大幅度性能提升 或 (b) 深刻的 analytical insights（如 RL-discovered strategies）来弥补——两者都是 outcome-dependent，无法在 idea 层面保证。\n```\n\nSources:\n- [ReaLM-Retrieve: When to Retrieve During Reasoning](https://arxiv.org/abs/2604.26649)\n- [Veri-R1: Toward Precise and Faithful Claim Verification via Online RL](https://arxiv.org/abs/2510.01932)\n- [Search-R1: Training LLMs to Reason and Leverage Search Engines](https://arxiv.org/abs/2503.09516)\n- [HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search](https://arxiv.org/abs/2506.07528)\n- [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384)\n- [CoRAG: Chain-of-Retrieval Augmented Generation](https://arxiv.org/abs/2501.14342)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG\n\n**状态**: 待审阅  \n**级别**: top-tier  \n**创建时间**: 2026-05-15T16:06:37.791174+00:00\n\n## 描述\nWe propose Dual-Intent Retrieval, a method that explicitly classifies each retrieval call within a reasoning model's chain-of-thought as either discovery-intent (seeking new evidence to advance reasoning) or verification-intent (seeking evidence to confirm or refute an intermediate claim), then applies structurally different query construction and retrieval strategies for each. Discovery queries use standard BM25 retrieval, matching its strength at keyword-rich information-seeking queries. Verification queries use a hybrid BM25+dense retrieval pipeline with NLI-based contrastive reranking: given an intermediate claim, the model generates contrastive queries (seeded by templates during SFT, refined through RL), retrieves via both BM25 and E5-base-v2 dense retrieval, and re-ranks by evidential discriminativeness using DeBERTa-v3-base NLI scoring, surfacing documents that most clearly support or refute the claim.\n\nThis operationalizes an insight that ReaLM-Retrieve empirically observed but did not act upon: its behavioral analysis (Section 6.9) identifies 'verification retrievals' as a distinct pattern in 31% of cases that reduces backtracking by 18%, while its failure analysis finds that over-retrieval during exploration accounts for 31% of failures. Despite observing that retrieval intent varies structurally, ReaLM-Retrieve's QueryGen maps all retrieval calls through the same learned embedding space without differentiating strategy. Even Veri-R1 (Oct 2025), which trains verification-specific RL policies via GRPO with a multi-component reward (label + evidence IoU + format + validity), uses uniform query construction across all search turns. We make this insight actionable.\n\nThe approach addresses a broader gap: ReaLM-Retrieve adapts queries implicitly without distinguishing purpose; CoRAG (NeurIPS 2025) reformulates queries iteratively but uniformly; DeepControl (ICLR 2026 Workshop) controls retrieval volume, not query strategy; AutoRefine (NeurIPS 2025) refines evidence post-retrieval; RAG-Star (NAACL 2025) verifies answers in MCTS with uniform retrieval; Veri-R1 (Oct 2025) trains verification-specific RL but uses uniform query construction; RAFTS (ACL 2024) demonstrates contrastive argument synthesis for fact-checking but operates standalone; Reason and Verify (Mar 2026) structures verification taxonomies for biomedical RAG but applies uniform retrieval. None classify intent and differentiate query construction within RL-trained sequential reasoning.\n\nThe contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format. The latter is a co-equal contribution: the structured format creates a rich action space for GRPO to discover sophisticated verification strategies (e.g., negation patterns, contrastive framing, claim-type-specific formulations) that humans might not manually design — and the query evolution analysis in Phase 3 is positioned as a key expected finding.\n\nBuilt atop Search-R1's open-source RL framework using Qwen2.5-7B (chosen over Qwen3-8B to avoid a known 10-20× GRPO training speed regression in veRL), we introduce intent tokens (&lt;discover>/&lt;verify>) and train via GRPO with a composite reward combining answer correctness and faithfulness. A critical design choice: we use different NLI model families for verification reranking (DeBERTa-v3-base, 184M params) vs. faithfulness reward (RoBERTa-large-NLI, 355M params) to prevent circular optimization where the policy learns to game its own reward signal. Intent labels are bootstrapped via heuristic rules for SFT cold start, then refined through RL. The &lt;verify>claim ||| query&lt;/verify> format allows RL to learn sophisticated query formulations beyond initial templates, following RAFTS's insight that LLM-generated contrastive formulations outperform fixed templates. We evaluate on six benchmarks — MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER — against Search-R1, IRCoT, AutoRefine, RAG-Star, and Veri-R1 baselines (with model-scale caveats for Veri-R1's 3B models and ReaLM-Retrieve's 32B). StrategyQA tests implicit multi-hop reasoning where the model must infer what type of evidence to seek; FEVER is the canonical claim verification benchmark directly comparable with Veri-R1's evaluation; HOVER tests multi-hop verification — together providing comprehensive coverage of both the discovery and verification aspects of our contribution. A mandatory pilot validates that discovery/verification intent is distinguishable — well-motivated given ReaLM-Retrieve's 31% verification rate.\n\n**Compute budget with verified arithmetic:** The entire pipeline fits within ~202 H100-hours (hard cap ≤210). Phase 2 (the dominant cost) runs 2 GRPO training configurations × 500 steps each on 8×H100. Per-step time is ~75 sec (range: 65-90 sec; calibrated from veRL benchmarks showing 60-70 sec/step for Qwen2.5-7B on 8×A800, ms-swift issue #3302, with Search-R1 retrieval overhead partially offset by H100 throughput). Per run: 500 steps × 75 sec = 10.4 wall-hours × 8 GPUs = ~83 H100-hours. Two runs = ~166 H100-hours. Plus overhead (pilot 5h, SFT 5h, NLI 8h, eval 18h) = ~202 H100-hours. 500 steps matches Search-R1's own protocol and exceeds AutoRefine's 300-step convergence; GRPO risks reward collapse beyond 500 steps, making this a well-calibrated choice. Contingency: reduce to 400 steps if per-step exceeds 90 sec, giving ~196h total.\n\nPrimary target: AAAI 2027 (abstract ~July 21, full paper ~July 28, 2026), providing a comfortable ~10-week window. The May 25, 2026 ARR cycle — the last eligible for EMNLP 2026 (commitment deadline August 2, 2026; note: there is no June ARR cycle, as ARR switched to 10-week review cycles) — is a stretch goal only. ICLR 2027 (~October 2026) serves as a fallback for extended experiments.\n\n## 核心问题\nCurrent reasoning-augmented retrieval systems optimize various aspects of the retrieval-reasoning interface — when to retrieve (ReaLM-Retrieve), how much to retrieve (DeepControl), how to refine retrieved evidence (AutoRefine), and how to coordinate retrieval with reasoning structure (DualRAG, HARIS) — yet all treat query construction as a single undifferentiated process. ReaLM-Retrieve's learned QueryGen module generates context-adaptive query representations via cross-attention to reasoning step embeddings, adapting queries implicitly through learned representations. Critically, ReaLM-Retrieve's own behavioral analysis (Section 6.9) empirically identifies 'verification retrievals' as a distinct pattern in 31% of cases — reducing backtracking by 18% — and its failure analysis finds that 'over-retrieval during exploration' accounts for 31% of failures (Section 7.3). These observations directly evidence that retrieval intent varies structurally within reasoning chains and that intent-mismatched retrieval actively degrades performance. Yet ReaLM-Retrieve does not operationalize this insight: its QueryGen maps all retrieval calls through the same continuous embedding space, conflating exploratory and confirmatory information needs. No system explicitly classifies the purpose of each retrieval call within a reasoning chain and applies structurally different query construction strategies accordingly. Even Veri-R1 (Oct 2025), which specifically trains models for claim verification via GRPO with iterative retrieval across up to 3 search turns, applies the same uniform query construction strategy across all retrieval calls — further evidencing that the discovery/verification distinction is not operationalized even in verification-specialized systems. Within a reasoning chain, a retrieval call seeking new evidence to explore an unknown sub-question (discovery) requires broad, recall-oriented queries, while one checking whether a specific intermediate claim holds (verification) requires targeted, claim-contrastive queries that seek both supporting and refuting evidence. Implicit query adaptation via learned representations cannot capture this structural distinction because a verification query should actively seek disconfirming evidence, which is anti-correlated with the topical relevance signal that learned query generators optimize for. This intent-blind retrieval means verification-stage retrievals return topically relevant but evidentially uninformative documents, degrading reasoning faithfulness. The problem is compounded by evidence that retrieval can actively hurt reasoning when poorly matched to reasoning needs — Shakya et al. (2026) show that traces including retrieval perform slightly worse than CoT without retrieval, but that adaptive retrieval (choosing when to retrieve) improves overall performance, suggesting that retrieval quality and intent matching — not just retrieval timing or volume — is a critical bottleneck.\n\n## 机遇 / Why Now\nReaLM-Retrieve empirically observed that retrieval intent varies within reasoning chains — identifying verification retrievals (31% of cases) as a distinct beneficial pattern and over-retrieval during exploration (31% of failures) as a primary failure mode — but did not operationalize this insight. We make it actionable via explicit intent classification and structurally differentiated query construction.\n\nReasoning models now produce long CoT traces with explicit intermediate claims that create a structurally exploitable retrieval signal: 'retrieve evidence to check claim X' is functionally distinct from 'retrieve evidence to answer question Y,' and these two modes demand different query construction strategies — yet no existing system makes this distinction explicit and operationalizes it at query construction time.\n\nRecent work has advanced adjacent aspects of this space without addressing this core gap. On implicit query adaptation: ReaLM-Retrieve (Apr 2026) uses a learned single-layer transformer decoder QueryGen that generates context-adaptive 768-dim query embeddings via cross-attention to reasoning step representations, achieving 71.2% F1 on MuSiQue (+11.8% over standard RAG) with only 1.8 retrieval calls — but its learned representations adapt queries implicitly without distinguishing retrieval purpose, and its own error analysis reveals this as a limitation. On retrieval-verification in tree search: RAG-Star (NAACL 2025) uses retrieval-augmented verification within MCTS, scoring answer-document consistency to guide tree search backpropagation, but applies uniform retrieval for every sub-query and operates in tree-structured (not sequential) reasoning. On iterative query reformulation: CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling, achieving SOTA on KILT, but applies the same reformulation strategy regardless of whether the model needs exploration or confirmation. On retrieval control: DeepControl (ICLR 2026 Workshop) measures marginal information utility to control retrieval continuation and granularity (+9.4% over Search-R1 on Qwen2.5-7B), but controls how much to retrieve, not how to construct purpose-differentiated queries. On evidence refinement: AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls with retrieval-specific rewards via GRPO, dramatically improving multi-hop QA, but refines evidence post-retrieval without differentiating query construction. On reasoning-aware retrieval embeddings: AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification. On RL-trained claim verification: Veri-R1 (Oct 2025) trains Qwen2.5-3B-Instruct via GRPO for iterative claim verification on FEVEROUS/FEVER/HOVER/SciFACT, improving joint accuracy by 30% and doubling evidence scores — but applies the same query strategy across all search turns despite being verification-specialized. On domain-specific structured verification: Reason and Verify (Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N — but applies uniform retrieval without intent classification and is not RL-trained.\n\nThe precise gap: existing systems adapt query representations implicitly through learned embeddings (ReaLM-Retrieve, CoRAG, AgentIR), reformulate queries iteratively (CoRAG), control retrieval volume (DeepControl), refine evidence post-retrieval (AutoRefine, SURE-RAG, Entropic Claim Resolution), verify answers in tree search (RAG-Star), train verification-specific RL policies with uniform retrieval (Veri-R1), or structure verification taxonomies in domain-specific settings (Reason and Verify) — but none explicitly classifies retrieval intent as discovery vs. verification and applies structurally different query construction strategies for each, particularly claim-contrastive retrieval that actively seeks disconfirming evidence for verification-intent calls. ReaLM-Retrieve's own analysis shows this distinction exists and matters; Veri-R1's uniform approach to verification-specific retrieval confirms it remains unaddressed even in the most targeted systems. We operationalize it.\n\n## 方法思路\nWe build a dual-intent retrieval module on top of the open-source Search-R1 framework that introduces explicit intent-differentiated query formulation into reasoning-augmented retrieval. The approach has four phases designed to fit within ~200 H100-hours and ~11 days.\n\n**Model choice: Qwen2.5-7B.** We use Qwen2.5-7B as the primary model, not Qwen3-8B. This is a deliberate choice motivated by a known, unresolved training speed regression: Qwen3-8B exhibits 10-20× slower generation during veRL GRPO training compared to Qwen2.5-7B (veRL GitHub issues #1580, #3816), with each step taking ~1 hour instead of minutes. The root cause appears to be Qwen3's thinking mode generating excessively long outputs (~7000 tokens vs ~1000 tokens), and this affects even non-thinking configurations due to architectural differences in how vLLM handles Qwen3. Qwen2.5-7B is the backbone Search-R1 was originally validated on, with proven GRPO training efficiency and 24% average relative improvement on QA benchmarks. We use Qwen2.5-7B-Base for the primary experiments, consistent with Search-R1's original evaluation.\n\n**Phase 0 — Pilot Feasibility (Day 1, ~5 H100-hours):** Generate reasoning traces on 500 MuSiQue training examples using standard Search-R1 with Qwen2.5-7B. Apply heuristic rules to classify each &lt;search> call: if the preceding reasoning contains an explicit claim or assertion ('X is Y', 'therefore', 'this means') followed by retrieval, label it VERIFY; if it contains a question decomposition or information-seeking pattern ('I need to find', 'what is', sub-question form), label it DISCOVER. Manually inspect 100 labeled examples and compute distribution statistics. Go/no-go: proceed only if both categories appear with ≥15% frequency and heuristic accuracy ≥75%. This threshold is well-motivated: ReaLM-Retrieve's analysis found verification retrievals comprise 31% of cases, suggesting ≥15% is easily achievable.\n\n**Phase 1 — Implementation (Days 2-4):** Extend the Search-R1 token format: replace the single &lt;search>query&lt;/search> with two intent-tagged variants: &lt;discover>query&lt;/discover> and &lt;verify>claim ||| query&lt;/verify>. The verify format includes both the claim and an optional model-generated query, enabling RL to learn sophisticated query formulations beyond templates. This dual-format design serves a deeper purpose beyond mere classification: by structuring verification retrieval as explicit claim ||| query pairs, we give the RL optimization a rich action space in which to develop intent-specific query patterns. The model must learn not just what to search for, but how to construct queries that surface evidence specifically relevant to confirming or refuting its tentative claim — a fundamentally different skill from exploratory information-seeking. Implement differentiated query processing in the search environment:\n\n(a) Discovery mode — pass the query to BM25, return top-3 results (same as baseline). BM25 is appropriate for discovery queries because they tend to be keyword-rich and information-seeking, matching BM25's lexical matching strength.\n\n(b) Verification mode — uses a hybrid retrieval pipeline to address the limitation that BM25 performs poorly on semantically-oriented contrastive queries. Extract the claim and the model-generated query (or, during SFT cold-start, generate a contrastive query pair via templates: 'evidence supporting [claim]' / 'evidence contradicting [claim]'). Retrieve top-3 via BM25 (lexical match on claim content) and top-3 via dense retrieval (E5-base-v2, which Search-R1 already supports as a retrieval backend) using the contrastive queries. Pool the 6 results, re-rank by evidential discriminativeness using an NLI cross-encoder (cross-encoder/nli-deberta-v3-base, 184M params) to score entailment and contradiction, returning the top-3 documents ranked by |entailment − contradiction| score (most discriminative first). The hybrid BM25+dense approach is motivated by evidence that hybrid retrieval improves recall by 15-30% over either method alone, and dense retrieval is critical for semantic matching on contrastive queries where keywords like 'supporting'/'contradicting' are uninformative for BM25. Note: Search-R1 provides pre-built E5-base-v2 FAISS indexes for its Wikipedia corpus, eliminating index-building overhead.\n\n**Template limitation and RL-learned query refinement (co-equal contribution):** We acknowledge that template-based contrastive queries ('evidence supporting/contradicting [claim]') are simplistic — real verification needs are more nuanced (causal claims require different evidence patterns than factual or temporal claims). The &lt;verify>claim ||| query&lt;/verify> format is specifically designed to allow the model to learn more sophisticated query formulations through RL. During SFT cold-start, templates provide the initial format. During GRPO training, the model is free to generate arbitrary text in the query field, learning from outcome rewards which query formulations yield the most useful evidence. This follows RAFTS's (ACL 2024) insight that LLM-generated contrastive arguments outperform fixed templates, but integrates the learning directly into the RL loop rather than requiring a separate generation step. We position the RL-discovered verification query strategies as a co-equal contribution alongside the intent taxonomy itself: if the model learns to use negation patterns, hedge framing, contrastive structures, or claim-type-specific formulations that humans would not manually design, this constitutes a compelling finding about how structured action spaces enable emergent strategy discovery through reward optimization.\n\nSFT cold start: relabel heuristically-classified Search-R1 traces with intent tokens and fine-tune Qwen2.5-7B-Base for ~100 steps to learn the new format.\n\nNote on Search-R1 RL algorithm: Search-R1 supports both PPO and GRPO via separate training scripts (train_ppo.sh and train_grpo.sh) built on the veRL framework. We use the GRPO configuration for training efficiency and stability, consistent with recent work (AutoRefine, DeepControl, Veri-R1) that also builds on Search-R1 with GRPO.\n\n**NLI model separation to avoid reward circularity:** A critical design decision is using different NLI models for verification reranking vs. faithfulness reward computation, to prevent a circular optimization where the model learns to game its own reward signal. During verification-intent retrieval, documents are reranked by |entailment − contradiction| via cross-encoder/nli-deberta-v3-base (DeBERTa architecture, 184M params). The faithfulness reward component uses a different model family: ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli (RoBERTa-large architecture, 355M params, trained on SNLI+MNLI+FEVER+ANLI). Using different architectures (DeBERTa disentangled attention vs. RoBERTa standard attention) and different training data distributions ensures the models have different decision boundaries, preventing the policy from learning to select documents that trivially satisfy the reward without genuinely improving evidential quality. The circularity concern is real: if the same model ranks documents and scores faithfulness, the optimization target reduces to 'retrieve documents that this specific model scores highly on' rather than 'retrieve genuinely informative evidence.' Different models with different inductive biases prevent this collapse.\n\n**NLI reranking cost analysis:** DeBERTa-v3-base (184M params) processes ~800-1200 sentence pairs/sec on a single H100. During GRPO training with global batch size B=256, average R=2.5 retrieval calls per sample, and estimated verification fraction V=0.4, total NLI pairs per step = B × R × V × 6 = 256 × 2.5 × 0.4 × 6 ≈ 1,536 pairs. At 1,000 pairs/sec, this adds ~1.5 seconds per step. The RoBERTa-large reward model (355M params) processes ~400-600 pairs/sec; with ~3 claims per trace × 256 samples = ~768 pairs, adding ~1.5 seconds per step. Combined NLI overhead is ~3 seconds per step. Compared to the LLM forward/backward pass on 8×H100 with Qwen2.5-7B, total NLI overhead is ~5-10% — manageable without dedicated hardware. To minimize memory contention, we run NLI inference on CPU (adding ~10-15 sec per step, still <25% overhead) or allocate a fraction of one GPU's memory. We budget an additional ~8 H100-hours for NLI overhead across all training runs.\n\n**Phase 2 — RL Training (Days 5-8, ~166 H100-hours on 8×H100):** Train with GRPO using a composite reward: R = α·EM(answer) + (1−α)·faithfulness, where faithfulness is the fraction of intermediate claims in the reasoning trace that are supported (entailment > 0.5) by at least one retrieved document, scored by the RoBERTa-large NLI model (distinct from the DeBERTa reranker). Set α = 0.7 (tunable). Run two configurations: (1) full dual-intent with hybrid contrastive verification retrieval (primary), (2) standard Search-R1 baseline with GRPO (ablation: no intent). The BM25-only ablation (dual-intent tokens with standard retrieval for both modes) is deferred to save compute; it can be added as a reduced-scale 250-step run (~28 H100-hours) if the primary runs finish under budget.\n\n**Per-run compute arithmetic:** Each run uses 500 training steps on 8×H100, matching Search-R1's own training protocol (the original Search-R1 paper trains for exactly 500 steps with checkpoints every 100 steps). Per-step time estimate: the veRL GRPO benchmark shows 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with NuminaMath-TIR (ms-swift issue #3302). Search-R1's multi-turn retrieval adds overhead from search engine calls during rollout generation (~2-4 search calls per trajectory with BM25 latency <50ms each) and longer context sequences (max_prompt_length=4096 vs ~2048 for math). H100's ~1.3× throughput advantage over A800 partially offsets this overhead. We estimate ~75 sec/step (range: 65-90 sec), yielding: 500 steps × 75 sec = 37,500 sec ≈ 10.4 wall-hours per run. Per-run GPU-hours: 10.4 wall-hours × 8 GPUs = **~83 H100-hours**. Two runs total: **~166 H100-hours**. **Contingency:** if per-step time exceeds 90 sec, reduce to 400 steps per run — still above AutoRefine's 300-step convergence point — giving 400 × 90 sec ≈ 10.0 wall-hours × 8 GPUs ≈ 80 H100-hours per run, ~160 H100-hours total for Phase 2.\n\n**Convergence justification for 500 steps:** 500 steps matches Search-R1's own training protocol, where the original paper uses exactly 500 steps for both Qwen2.5-3B and Qwen2.5-7B with GRPO. AutoRefine (NeurIPS 2025), built on the same Search-R1/veRL/GRPO stack, trains for only 300 steps and achieves its reported gains (HotpotQA: 0.405 F1, MuSiQue: 0.157 F1). GRPO-LEAD converges in ~200 steps with top-performing checkpoints selected via validation. Empirical GRPO training dynamics show gradient norms stabilize by step 40, with most accuracy gains in the first 200-300 steps. Additionally, GRPO is known to risk reward collapse when trained for too many steps, further motivating 500 steps as a well-calibrated choice rather than a compromise.\n\n**Phase 3 — Evaluation & Analysis (Days 9-11, ~18 H100-hours):** Evaluate on MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER (6 benchmarks). MuSiQue, HotpotQA, and 2WikiMultiHopQA are standard multi-hop QA benchmarks requiring compositional reasoning with explicit decomposition. StrategyQA requires implicit multi-hop reasoning where the decomposition strategy is not given — the model must infer what type of evidence to seek, making it an ideal showcase for intent-differentiated retrieval since the discovery/verification transition is not signaled by the question structure but must emerge from the model's reasoning process. FEVER is the canonical fact verification benchmark (185K claims, supported/refuted/NEI) — essential for a method whose core contribution involves verification-intent retrieval, and directly comparable with Veri-R1's evaluation on the same benchmark. HOVER is a multi-hop claim verification benchmark requiring evidence from 2-4 Wikipedia articles, testing both discovery (finding relevant articles across hops) and verification (confirming multi-hop claims against aggregated evidence). Metrics: answer F1/EM, faithfulness (claim-support rate), retrieval precision/recall on supporting evidence. Baselines: Search-R1 (reproduced with GRPO), IRCoT, and ReaLM-Retrieve (reported numbers with model-scale caveats, as their best results use DeepSeek-R1-Distill-Qwen-32B). Additional comparisons: AutoRefine (reported numbers, NeurIPS 2025), RAG-Star (reported numbers from Llama-3.1-8B-Instruct), Veri-R1 (reported numbers on HOVER and FEVER, with model-scale caveats since Veri-R1 uses Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct while we use 7B; we will report per-parameter efficiency where feasible to enable fair comparison). Analysis: (a) intent distribution — what fraction of retrievals are classified as discovery vs. verification across all six benchmarks, and how this compares to ReaLM-Retrieve's observed 31% verification rate, (b) per-intent retrieval quality — does verification mode retrieve more evidentially discriminative documents (measured by |entailment − contradiction| spread), (c) comparison with implicit adaptation — does explicit intent classification outperform ReaLM-Retrieve's learned QueryGen on verification-heavy reasoning chains, (d) NLI model separation analysis — compare performance with same-model vs. different-model reranking/reward to quantify circularity effects, (e) **query evolution analysis (key expected finding)** — do RL-learned verification queries diverge from initial templates, and what patterns emerge (claim-type-specific formulations, negation patterns, contrastive framing, hedge structures, etc.)? This analysis is positioned as a key finding, not merely a diagnostic: if RL discovers intent-specific query patterns that humans wouldn't write — e.g., systematically different query structures for causal vs. factual vs. temporal claims — that constitutes a compelling result in its own right, demonstrating that the structured &lt;verify>claim ||| query&lt;/verify> format enables emergent strategy discovery through reward optimization, (f) error analysis — when does intent misclassification degrade performance, (g) case studies showing how contrastive verification queries surface disconfirming evidence that standard and implicitly-adapted queries miss, (h) StrategyQA-specific analysis — does intent-differentiated retrieval show disproportionate gains on implicit decomposition tasks where the model must infer retrieval intent without explicit question structure?\n\n**Design justifications:** The binary discovery/verification taxonomy is the minimal distinction that captures the most variance in retrieval intent within reasoning chains. This choice is now directly grounded in ReaLM-Retrieve's empirical findings: their three behavioral patterns (early resolution 42%, verification 31%, failed retrieval 12%) naturally collapse into our binary taxonomy — early resolution and failed retrieval are both discovery-intent (information-seeking), while verification retrievals map directly to our verification-intent. The choice is further motivated by Shakya et al.'s (2026) finding that retrieval during exploration can hurt reasoning while adaptive retrieval helps — suggesting that the exploration/confirmation axis is the primary dimension along which retrieval intent varies. Finer categories (clarification, disambiguation, quantitative validation) are subsumed: clarification and disambiguation are discovery subtypes, quantitative/causal verification are verification subtypes. Binary classification is also more robust with limited RL training budget and avoids the need for multi-class intent supervision. The framework is extensible to additional intent types via new tokens.\n\nThe key distinction from related approaches: ReaLM-Retrieve's QueryGen learns a continuous mapping from reasoning states to query embeddings, and its own analysis reveals that verification retrievals are a distinct beneficial pattern — but it does not operationalize this insight by applying different retrieval pipelines. Veri-R1 trains verification-specific RL policies with a multi-component reward (label + evidence IoU + format + validity) but uses the same uniform query strategy across all search turns — even its emergent 'fine-grained subclaim-level decomposition' is not structurally supported by differentiated retrieval. Our approach makes intent classification explicit and applies structurally different retrieval pipelines — critically, verification queries use hybrid BM25+dense retrieval with NLI-based contrastive reranking to actively seek disconfirming evidence, which is anti-correlated with topical relevance maximization. RAG-Star uses retrieval for verification within MCTS but verifies candidate answers at tree nodes with uniform relevance-based retrieval, not intermediate claims with contrastive queries. AutoRefine's &lt;refine> step distills evidence post-retrieval but doesn't change how queries are constructed. CoRAG reformulates queries iteratively but applies the same reformulation strategy regardless of intent. DeepControl controls retrieval volume and timing but not query construction strategy. RAFTS (ACL 2024) demonstrates that contrastive argument synthesis improves fact verification, but operates as a standalone pipeline — we integrate contrastive retrieval directly into the RL-trained reasoning loop. Reason and Verify (Mar 2026) structures verification with an eight-category taxonomy for biomedical RAG but applies uniform retrieval — we address a different dimension (retrieval pipeline differentiation) in a domain-general RL-trained setting.\n\nThe contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format — the latter being a co-equal contribution that may yield insights about how structured action spaces enable emergent retrieval strategies.\n\nFallback: if claim extraction quality is poor in the reasoning trace (e.g., no clear propositional claim before a retrieval call), default to discovery mode — this is safe because discovery mode is equivalent to the baseline.\n\n## 研究现状\nThe reasoning-augmented retrieval landscape in 2025-2026 has advanced along five axes — implicit query adaptation, retrieval timing/volume control, retrieval-reasoning coordination, post-retrieval evidence quality, and reasoning-stage verification — creating a rich but precisely gapped design space.\n\n**Implicit query adaptation.** ReaLM-Retrieve achieves 71.2% F1 on MuSiQue with 1.8 retrieval calls by combining step-level uncertainty-based retrieval timing with a learned QueryGen module (single-layer transformer decoder, 512 hidden dim, 8 attention heads) that cross-attends to current reasoning step embeddings, producing context-adaptive 768-dim query representations for ColBERTv2 dense retrieval. The +11.8% F1 improvement on MuSiQue (+10.1% average across three benchmarks) demonstrates that adaptive query generation substantially outperforms static queries. Crucially, ReaLM-Retrieve's own behavioral analysis (Section 6.9) identifies three dominant retrieval patterns: 'early resolution' (42% of cases, yielding 23% shorter reasoning chains), 'verification retrievals' (31%, reducing backtracking by 18%), and 'failed retrievals' (12%, extending chains by 8%). Its failure analysis (Section 7.3) finds that over-retrieval during exploratory reasoning phases accounts for 31% of failures by 'disrupting productive chains by prematurely committing to hypotheses.' These observations directly evidence that retrieval intent varies structurally and that intent-mismatched retrieval degrades performance — yet QueryGen's cross-attention mechanism learns a single continuous mapping from reasoning states to query embeddings, conflating exploratory and confirmatory needs into the same representation space. CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling training, establishing SOTA on KILT with >10-point EM improvements on multi-hop QA, but applies uniform reformulation strategy regardless of retrieval purpose. AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification.\n\n**Retrieval timing and volume control.** DeepControl (ICLR 2026 Workshop) formalizes information utility as U(e) = ρ·Novelty + (1−ρ)·Effectiveness, using an annealed control-forcing curriculum to train retrieval continuation and granularity control, achieving +9.4% on Qwen2.5-7B over RL baselines across seven benchmarks. R1-Searcher++ trains models to decide whether to use internal knowledge or external search. Shakya et al. (Feb 2026) find that 'traces including retrieval actually perform worse compared to CoT' while the model's decision to adaptively avoid retrieval improves overall performance — suggesting that retrieval quality and intent matching matters more than retrieval quantity.\n\n**Retrieval-reasoning coordination.** Search-R1 trains LLMs via RL (supporting both PPO and GRPO) to issue search queries within reasoning, achieving +41%/+20% on QA benchmarks for 7B/3B models, with Qwen2.5-7B as the primary validated backbone. AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls that distills evidence from ~600 to ~100-200 tokens, trained with GRPO using dual rewards (answer correctness + retrieval quality), achieving major gains on multi-hop QA (HotpotQA: 0.405 vs 0.297 Search-R1; MuSiQue: 0.157 vs 0.066). DualRAG (ACL 2025) coordinates reasoning-augmented querying with progressive knowledge aggregation. HARIS (arXiv 2506.07528, Jun 2025) uses a hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B, evaluating on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop) for claim verification — but with uniform search strategy across all retrieval calls. IRCoT interleaves retrieval at fixed intervals.\n\n**Post-retrieval evidence quality.** SURE-RAG (May 2026) scores claim-evidence pairs for sufficiency. Entropic Claim Resolution (Mar 2026) selects discriminative evidence via entropy minimization. RAFTS (ACL 2024) synthesizes contrastive supporting/refuting arguments from retrieved passages via LLM-based generation with a two-stage BM25+dense retrieval pipeline for standalone fact verification — demonstrating that contrastive evidence framing improves verification accuracy, but operating as a standalone fact-checking system rather than integrated in reasoning RL loops. Reason and Verify (arXiv 2603.10143, Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct. Though domain-specific (biomedical) and not RL-trained, it demonstrates concurrent interest in structured verification within RAG, using BGE cross-encoder reranking and rationale grounding — but applies uniform retrieval without intent classification. REPAIR (Jan 2026) uses reasoning plans for mid-course correction during reranking. All operate downstream of query construction.\n\n**Reasoning-stage verification.** RAG-Star (NAACL 2025) uses MCTS for deliberative reasoning with retrieval-augmented verification: for each MCTS node, retrieval checks answer-document consistency (scoring 1=unverifiable, 2=conflict, 3=aligned) with query- and answer-aware reward modeling. However, RAG-Star verifies candidate answers at MCTS tree nodes using uniform retrieval, not intermediate claims within sequential reasoning chains, and does not use contrastive queries to actively seek disconfirming evidence. Veri-R1 (arXiv 2510.01932, Oct 2025) is the most directly comparable RL-based verification system: it trains Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct via GRPO for iterative claim verification with up to 3 search turns, using a 4-component reward (label correctness +2, evidence IoU, format compliance, validity weight). Evaluated on FEVEROUS, EX-FEVER, FEVER, SciFACT, and HOVER, Veri-R1 improves joint accuracy by up to 30% and doubles evidence scores vs baselines. Open-source and built on Search-R1/veRL. Critically, despite being designed specifically for claim verification, Veri-R1 does NOT differentiate retrieval intent — all search queries use the same uniform strategy, whether the model is exploring for initial evidence or confirming a tentative conclusion. Its case analysis shows Online RL naturally develops 'fine-grained subclaim-level decomposition,' but this emergent behavior is not structurally supported by differentiated retrieval pipelines. FIRE (NAACL Findings 2025) uses confidence-based iterative retrieval for fact-checking with 7.6× cost reduction but applies the same query strategy per iteration. 'Don't Let It Hallucinate' (NeurIPS 2025) transforms queries into logical premises for pre-generation verification, operating before reasoning chains begin. VERITAS rewards faithful reasoning but doesn't modify retrieval.\n\n**The gap.** All existing systems either (a) adapt query representations implicitly through learned embeddings without distinguishing retrieval purpose — even when their own analysis shows the distinction exists and matters (ReaLM-Retrieve, CoRAG, AgentIR), (b) control retrieval timing/volume without differentiating query construction (DeepControl, R1-Searcher++), (c) refine evidence post-retrieval without improving the upstream query (AutoRefine, SURE-RAG, ECR, RAFTS), (d) verify answers in tree search or pre-generation without contrastive query construction within sequential reasoning (RAG-Star, FIRE, Don't Let It Hallucinate), (e) train verification-specific RL policies but still use uniform query construction across all search turns (Veri-R1), or (f) structure verification taxonomies in domain-specific settings without intent-differentiated retrieval (Reason and Verify). No system explicitly classifies retrieval intent as discovery vs. verification within sequential reasoning chains and applies structurally different query construction strategies for each — particularly claim-contrastive retrieval that actively seeks disconfirming evidence during verification.\n\n## 目标 Venue\n- AAAI 2027 (abstract ~July 21, 2026; full paper ~July 28, 2026 — primary target with comfortable ~10-week window for experiments, analysis, and paper writing)\n- ARR May 25, 2026 → EMNLP 2026 (commitment deadline August 2, 2026) — stretch goal only, requires aggressive 10-day execution with pre-existing Search-R1/veRL familiarity; note: this is the last eligible ARR cycle for EMNLP 2026, as the next ARR cycle (August 3, 2026) falls after the EMNLP commitment deadline; no June ARR cycle exists due to ARR's switch to 10-week review cycles\n- ICLR 2027 (expected ~October 2026 — fallback allowing additional model scales, extended ablations, or supplementary benchmarks)\n\n## 关键参考\n- Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (arXiv 2503.09516, Mar 2025) — base framework; supports PPO and GRPO via veRL, &lt;search> token format; validated on Qwen2.5-7B with 24% average relative improvement; trains for 500 GRPO steps with checkpoints every 100 steps; provides pre-built BM25 and E5 FAISS indexes for Wikipedia corpus\n- When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (arXiv 2604.26649, Apr 2026) — learned QueryGen module (single-layer transformer decoder, cross-attention to reasoning step embeddings, 768-dim adaptive query representations); +11.8% F1 on MuSiQue (71.2%), +10.1% average across 3 benchmarks; Section 6.9 identifies verification retrievals (31% of cases) as a distinct pattern reducing backtracking by 18%; Section 7.3 identifies over-retrieval during exploration as 31% of failures; implicitly adaptive but not intent-differentiated despite observing the need\n- RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement (NAACL 2025, Jiang et al.) — MCTS-based reasoning with retrieval-augmented verification at tree nodes (answer-document consistency scoring), query- and answer-aware reward modeling; verifies candidate answers in tree search with uniform retrieval, not intermediate claims with contrastive queries\n- Chain-of-Retrieval Augmented Generation [CoRAG] (NeurIPS 2025, arXiv 2501.14342) — dynamic query reformulation via rejection sampling training, SOTA on KILT, >10-point EM on multi-hop QA; reformulates queries based on evolving state but without intent differentiation\n- Scaling Search-Augmented LLM Reasoning via Adaptive Information Control [DeepControl] (arXiv 2602.01672, ICLR 2026 Workshop SPOT) — information utility = ρ·Novelty + (1−ρ)·Effectiveness, retrieval continuation and granularity control with annealed curriculum; +9.4% on Qwen2.5-7B over RL baselines; controls retrieval volume, not query construction strategy\n- Search and Refine During Think [AutoRefine] (NeurIPS 2025, arXiv 2505.11277) — &lt;refine> step distilling evidence between search calls, GRPO with dual rewards (answer + retrieval quality); trains for 300 steps on Search-R1/veRL/GRPO stack and achieves convergence; HotpotQA: 0.405 vs 0.297 Search-R1, MuSiQue: 0.157 vs 0.066; refines evidence post-retrieval without intent-differentiated query construction\n- Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments [RAFTS] (ACL 2024) — LLM-based contrastive supporting/refuting argument synthesis with two-stage BM25+dense retrieval pipeline; demonstrates contrastive evidence framing improves verification; standalone system, not integrated in reasoning RL\n- Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning (arXiv 2510.01932, Oct 2025) — GRPO-trained iterative claim verification with Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct on FEVEROUS/EX-FEVER/FEVER/SciFACT/HOVER; 4-component reward (label correctness + evidence IoU + format compliance + validity weight); improves joint accuracy by 30%, doubles evidence scores; does NOT differentiate retrieval intent despite being verification-focused; open-source on Search-R1/veRL; most directly comparable RL-based verification baseline\n- HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification (arXiv 2506.07528, Jun 2025) — hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B; evaluates on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop); uniform search strategy without intent differentiation\n- Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation (arXiv 2603.10143, Mar 2026) — biomedical RAG with eight-category verification taxonomy, explicit sub-claim grounding, BGE cross-encoder reranking; 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct; domain-specific but demonstrates concurrent interest in structured verification within RAG; uniform retrieval without intent classification\n- R1-Searcher++: Incentivizing Dynamic Knowledge Acquisition of LLMs via RL (arXiv 2505.17005, May 2025) — internal vs. external knowledge distinction, not intent within external retrieval\n- REPAIR: Adaptive Retrieval for Reasoning-Intensive Retrieval (arXiv 2601.04618, Jan 2026) — reasoning plans for reranking; operates post-retrieval, not at query construction\n- FIRE: Fact-checking with Iterative Retrieval and Verification (NAACL Findings 2025) — confidence-based iterative retrieval; 7.6× cost reduction but same query strategy per iteration\n- Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning (NeurIPS 2025) — pre-generation premise verification, not during reasoning chain\n- Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (arXiv 2602.07213, Shakya et al., Feb 2026) — traces with retrieval perform slightly worse than CoT; adaptive retrieval (choosing when to retrieve) improves overall performance; directly motivates that retrieval quality and intent matching matters more than retrieval volume\n- DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop QA (ACL 2025) — dual reasoning-retrieval processes but uniform retrieval strategy\n- AgentIR: Reasoning-Aware Retrieval for Deep Research Agents (arXiv 2603.04384, Mar 2026) — encodes reasoning traces in embeddings but uniform intent across all retrieval calls\n- SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective RAG (arXiv, May 2026) — post-retrieval claim-evidence scoring\n- Entropic Claim Resolution: Uncertainty-Driven Evidence Selection for RAG (arXiv, Mar 2026) — post-retrieval evidence selection via entropy minimization\n- Beyond Correctness: Rewarding Faithful Reasoning in RAG [VERITAS] (arXiv, Oct 2025) — faithfulness reward for generators, not retrieval modification\n- Interleaving Retrieval with Chain-of-Thought Reasoning [IRCoT] (ACL 2023) — fixed-interval retrieval baseline\n- Adaptive-RAG: Learning to Adapt Retrieval-Augmented LLMs through Question Complexity (NAACL 2024)\n- veRL GitHub issues #1580, #3816 — Qwen3-8B GRPO training 10-20× slower than Qwen2.5-7B due to generation speed regression; motivates our model choice\n- ms-swift GitHub issue #3302 — GRPO training speed benchmark: 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with veRL; calibrates our per-step compute estimate\n\n## 资源估算\n### auto_research\n- **claude_api_cost**: $200-400 (est. 2000-4000 turns for autonomous experiment design and paper drafting)\n- **estimated_gpu_cost**: ~$630 (210h × ~$3.00/hr)\n- **gpu_hours**: ≤210 H100-hours (hard budget cap). Agent must track cumulative GPU-hours (wall-time × GPUs, not wall-time alone) and prioritize: primary dual-intent run (~83h) and baseline run (~83h) are mandatory; BM25-only ablation at 250 steps (~42h) is included only if cumulative spend remains ≤168h after the two primary runs. If approaching cap, agent reduces ablation steps or skips lowest-priority analysis.\n- **gpu_utilization**: ~85-95% utilization; agent pipelines experiments continuously\n- **risk_note**: Agent should implement early stopping on reward plateau detection (GRPO risks reward collapse beyond ~500 steps); if pilot feasibility fails (intent categories not distinguishable), agent should pivot to testing contrastive verification queries without intent classification\n- **speed_bottleneck**: Primary bottleneck is sequential GRPO runs on 8 GPUs (~10.4 wall-hours each at 75 sec/step); BM25 index pre-built, E5 FAISS index downloadable from Search-R1; NLI inference adds ~5-10% per-step overhead\n- **team**: 0 (initial setup and final review only)\n- **timeline**: 6-9 days with 8×H100 available\n\n### human_in_loop\n- **claude_api_cost**: $100-200 (est. 1000-2000 turns for code generation and experiment analysis)\n- **estimated_gpu_cost**: ~$606-630 (202-210h × ~$3.00/hr)\n- **gpu_hours**: ~202-210 H100-hours. Base plan (~202h) plus agent-proposed extensions with human approval: reduced-scale BM25-only ablation (250 steps on 8×H100 = 250 × 75 sec ≈ 5.2 wall-hours × 8 GPUs ≈ ~42h), reward weighting variants, or heuristic threshold tuning. Extensions prioritized by expected information value within remaining budget.\n- **gpu_utilization**: ~55-70% utilization; agent queues experiments while human reviews\n- **risk_note**: Composite faithfulness+correctness reward may need human judgment on α weighting if RL training shows reward hacking on the faithfulness component; if per-step time exceeds 90 sec, human approves step-count reduction to 400\n- **team**: 1 researcher, ~20-30min/day reviewing proposals and results\n- **timeline**: 2-3 weeks\n\n### manual\n- **estimated_gpu_cost**: ~$606 (202h × ~$3.00/hr H100 spot pricing)\n- **gpu_hours**: ~202 H100-hours total (range: 183-215 depending on per-step training speed). Breakdown with explicit wall-time × GPU arithmetic: Phase 0 pilot: ~5h (generation only, 1-2 GPUs); Phase 1 SFT cold start: ~5h (100 SFT steps); Phase 2 GRPO training: 2 runs × 500 steps × ~75 sec/step = 2 × (10.4 wall-hours × 8 GPUs) = ~166h; NLI overhead during training: ~8h; Phase 3 evaluation on 6 benchmarks: ~18h. Dense index building: ~0h (Search-R1 provides pre-built E5-base-v2 FAISS indexes). Per-step calibration: veRL GRPO benchmarks show 60-70 sec/step for Qwen2.5-7B on 8×A800 (ms-swift issue #3302); we estimate ~75 sec/step for Search-R1 on 8×H100, accounting for retrieval overhead partially offset by H100 throughput advantage. Contingency: if per-step exceeds 90 sec, reduce to 400 steps/run (above AutoRefine's 300-step convergence), giving 2 × (10.0 wall-hours × 8 GPUs) = ~160h for Phase 2, ~196h total.\n- **gpu_utilization**: ~40-50% effective utilization; GPUs idle during implementation, debugging, and analysis phases\n- **team**: 1 researcher with RL and retrieval experience\n- **timeline**: 10-12 days (10 days with 8×H100 and familiarity with Search-R1/veRL codebase; 12 days otherwise)\n\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T01:55:13.018Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T01:55:13.018Z",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T01:55:13.033Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough assessment. Here is my evaluation:

---

```
【阶段】: Triage

【Trivial Alternative 检验】:
存在一个严重的 trivial alternative 威胁，proposal 未充分回应：

**为什么不对所有 retrieval call 都使用 hybrid BM25+dense+NLI reranking？** 如果 NLI-based contrastive reranking 能提高 verification query 的质量，为什么它不会同时提高 discovery query 的质量？proposal 声称 BM25 适合 discovery 因为"keyword-rich"，但这是假设而非论证。一个不需要任何 intent classification 的 trivial baseline —— 统一使用更强的 hybrid pipeline —— 可能达到类似效果且更简单。如果这个 baseline 表现接近，那么 intent classification 的增量价值（也就是整篇论文的核心贡献）就被消解了。

Proposal 计划了 BM25-only ablation（dual-intent tokens + 标准 retrieval），但这测试的是 "intent tokens 本身有没有用"，而非 "intent classification vs. 统一用更强 pipeline"。真正致命的 ablation 是：**对所有 query 统一使用 hybrid+NLI，不做 intent classification**。这一组被遗漏。

第二个 trivial alternative：AutoRefine 的 &lt;refine> step 在 post-retrieval 阶段蒸馏证据，已经在 HotpotQA/MuSiQue 上取得了大幅提升。如果 post-retrieval refinement 能弥补 query construction 阶段的不足，upstream 的 intent differentiation 增量价值可能很小。

**增量价值辩护（proposal 可以但未能做到的）：** intent classification 的真正价值应该在于 verification mode 主动寻找 disconfirming evidence（通过 contrastive query），这是一种 structurally different 的检索意图，不能通过简单使用更强的 pipeline 来实现。但 proposal 对"为什么 disconfirming evidence 不能通过统一 pipeline 获取"的论证薄弱。


【前提假设检验】:
核心 claim 的逻辑链中有 3 个未经充分验证的假设：

1. **"Verification query 需要 disconfirming evidence，而这与 topical relevance 信号反相关"** —— 这是核心逻辑的关键环节，但论证不足。包含 refuting evidence 的文档往往也是高度 topically relevant 的（例如，反驳 "X 出生在纽约" 的文档通常也是关于 X 的）。真正反相关的是 evidential valence 和 retrieval signal，但 dense retrieval 的 semantic matching 本身并不只优化 topical relevance —— 它可以捕捉到 semantic 层面的 contrastive 关系。这个假设如果不成立，整个 "为什么需要 differentiated pipeline" 的论证就塌了。

2. **"Heuristic rules 可以可靠地从 reasoning traces 中分类 intent"** —— 虽然设置了 75% accuracy 的 go/no-go 门槛，但 heuristic classification 的噪声在 RL 训练中会被放大。如果 30% 的 intent labels 是错误的，RL 在错误 label 上训练的 query construction 策略可能比不分类更差。Proposal 假设 "默认 fallback 到 discovery 是安全的"，但如果 heuristic 把 discovery 错标为 verification（false positive），会在不需要 contrastive query 的地方强行使用 contrastive pipeline，可能降低性能。

3. **"500 GRPO steps 足以让 RL 发现 sophisticated verification query strategies"** —— 这被定位为 "co-equal contribution"，但 RL 在 500 steps 内是否能在 query formulation 这个 secondary action space 上学到 beyond-template 的策略是未经验证的。Proposal 引用 RAFTS 证明 "LLM-generated contrastive formulations outperform templates"，但 RAFTS 使用的是大模型 zero-shot generation，不是 7B 模型在 500 RL steps 内学习的结果。将一个希望性发现定位为 co-equal contribution 是有风险的。


【3 维度打分】:

1. Novelty: 【弱-中】
   
   核心贡献是 "operationalize an existing observation" —— 将 ReaLM-Retrieve Section 6.9 中已经识别出的 verification retrieval pattern 显式化，配以不同的检索 pipeline。这是一个 natural next step，而非 surprising insight。任何仔细阅读 ReaLM-Retrieve 的研究者都可能想到 "为什么不根据 intent 使用不同策略"。
   
   与最相关 5-10 篇近期工作比较后的真实 novelty delta：
   - vs. ReaLM-Retrieve: delta 是 "显式分类 + 不同 pipeline"，属于 operationalization
   - vs. Veri-R1: delta 是 "differentiated query construction"，但 Veri-R1 本身只用 3B 模型，场景不完全可比
   - vs. RAFTS: delta 是 "集成到 RL 循环"，属于 integration
   - vs. AutoRefine: delta 是 "pre-retrieval intent 分类 vs. post-retrieval refinement"，是互补而非替代
   - vs. HARIS: delta 是 "binary intent + differentiated pipeline vs. hierarchical agents"，不同设计但解决类似问题
   
   剔除 surface differences（不同的 token format、不同的 pipeline 组合）之后，核心 insight 只有一条：**retrieval intent 应该被显式分类并用不同策略处理**。这更接近 engineering contribution 而非 conceptual breakthrough。
   
   第二个贡献 "RL-discovered query strategies" 在实验之前只是一个希望，不能作为 novelty 评估的依据。

2. Significance: 【中】
   
   研究问题是重要的 —— reasoning-augmented retrieval 是当前 NLP 的热点方向，如何提升 retrieval 质量确实是关键瓶颈（Shakya et al. 2026 的发现强化了这一点）。
   
   但显著性受限于：
   - **结果预期方向的可预测性**：如果 differentiated retrieval 表现更好，审稿人大概率会说 "I would have guessed this" 而非 "surprising"。Binary intent classification 提升性能是直觉上合理的结果。
   - **问题的窄度**：这是 reasoning-augmented RAG 中 query construction 阶段的一个 specific 优化。影响面限于使用 RL-trained reasoning+retrieval 的系统。
   - **可推广性受限**：binary taxonomy（discovery/verification）是否是最优分类？框架声称可扩展，但论文只测试 binary。
   
   如果结果是 negative（differentiation 不帮助或帮助很小），论文的贡献更多是 empirical insight（"显式分类不如隐式学习"），这也有价值但 significance 更低。

3. Related Work: 【强】
   
   Related work 覆盖极为全面。我在 web search 中未找到 proposal 遗漏的重要近期工作。对每篇相关工作的差异化定位准确且清晰。特别值得肯定的是：
   - 对 ReaLM-Retrieve、Veri-R1、HARIS 等最近期工作的深入分析
   - 对 gap 的结构化总结（5 个轴向的系统化梳理）
   - 对每个相关方法"做了什么 + 没做什么"的精确定位
   
   这是整个 proposal 最强的部分。唯一微弱的遗漏：没有充分讨论 FAIR-RAG（adaptive iterative refinement）和 Q-PRM（adaptive query rewriting），但这些不直接威胁 novelty claim。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
Related Work 维度强（不拉后腿），但 Novelty 弱-中 和 Significance 中 共同限制了上界。

核心问题在于：这篇论文的 intellectual contribution 是 "operationalize an existing observation with known techniques"。Binary intent classification 是 obvious next step；hybrid BM25+dense+NLI 是已知技术的组合；GRPO training 是在 Search-R1 框架上的增量修改。审稿人最可能的反应是 "reasonable engineering contribution, but the core idea is not surprising enough for main conference"。

概率没有落入 15-18% 区间是因为：(a) gap 确实存在且被充分论证，(b) related work 定位清晰，(c) 如果 RL-discovered query patterns 出现 surprising 结果，论文有上行空间。但这个上行空间依赖于实验结果，而非 idea 本身的质量。

概率没有达到 28%+ 是因为：(a) trivial alternative 威胁严重且未回应，(b) 核心 claim 的前提假设（disconfirming evidence 与 topical relevance 反相关）论证薄弱，(c) "RL-discovered strategies" 作为 co-equal contribution 在实验前是空洞的。

**限制上界的关键维度是 Novelty** —— 即使 significance 提升到"中-强"，idea 的 incremental nature（operationalize + integrate known techniques）在 top-tier 会议上是硬伤。

【主要风险】:
1. **Trivial alternative 被审稿人发现**：审稿人大概率会问 "为什么不对所有 query 统一使用你的 hybrid+NLI pipeline？如果统一使用更强 pipeline 效果接近，intent classification 的价值在哪？" 如果这组 ablation 结果不利，论文核心贡献被消解。
2. **"Operationalize an obvious observation" 被视为 incremental**：核心 insight 来自 ReaLM-Retrieve 的 Section 6.9，proposal 本质上是 "take their observation and act on it"。审稿人可能判定这是一个 well-executed follow-up study 而非独立的 main conference contribution，尤其在 novelty 维度给出 borderline-reject 分数。
```

Sources:
- [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384)
- [HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification](https://arxiv.org/html/2506.07528v1)
- [Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation](https://arxiv.org/html/2603.10143)
- [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/pdf/2503.09516)
- [RAFTS: Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments](https://arxiv.org/html/2406.09815v1)
- [ReaLM-Retrieve: When to Retrieve During Reasoning](https://arxiv.org/html/2604.26649)
- [DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop QA](https://arxiv.org/html/2504.18243)
- [FAIR-RAG: Faithful Adaptive Iterative Refinement for RAG](https://arxiv.org/html/2510.22344v1)
- [Q-PRM: Adaptive Query Rewriting for RAG](https://aclanthology.org/2025.findings-emnlp.817.pdf)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:

存在两个严重的 trivial alternative 威胁：

1. **统一使用 hybrid BM25+dense+NLI reranking 处理所有 query（无需 intent 分类）**：
   如果 hybrid retrieval + NLI reranking 对 verification query 有效，为什么不对所有 query 都使用它？Proposal 声称 BM25 对 discovery query "更合适"因为它们是 keyword-rich 的，但这只能论证 BM25 不差，不能论证 hybrid 会更差。一个 reviewer 完全可以要求一个 "uniform hybrid for all queries" baseline——如果它表现接近，则 intent classification 的增量价值趋近于零。Proposal 没有讨论这个 trivial alternative。

2. **让 RL 隐式学习 query 差异化（无需显式 intent token）**：
   在 Search-R1 的 RL 训练中，模型已经可以自由生成任意 query 文本。如果 reward signal 足够清晰（EM + faithfulness），模型应该自然学会在需要验证时写出 contrastive query，无需 &lt;discover>/&lt;verify> 的显式约束。显式 intent token 可能反而限制了模型的灵活性。这个 alternative 的增量成本几乎为零（只是调整 reward），却可能达到类似效果。Proposal 的反论（"implicit adaptation cannot capture the distinction because verification is anti-correlated with topical relevance"）存在逻辑跳跃——RL 优化的是下游 EM/F1，不是 topical relevance。

增量价值在于：如果可以证明 (a) uniform hybrid 显著不如 differentiated pipeline，且 (b) 显式 intent token 显著优于让 RL 隐式学习差异化，则 intent classification + differentiated pipeline 的组合有真实增量。但这两个条件目前都是未验证假设。

【前提假设检验】:

核心逻辑链条中存在以下未验证假设：

1. **"隐式 query adaptation 无法捕捉 discovery/verification 区分"**（最关键假设）：
   论证基于 "verification 需要 disconfirming evidence，而 learned query generator 优化 topical relevance"。但 RL-trained query generator（如 Search-R1）优化的是下游任务表现（EM/F1），不是 topical relevance。如果 disconfirming evidence 有助于提高 EM，RL 应当能隐式学会检索它。这个论证把 dense retriever 的训练目标与 RL policy 的训练目标混为一谈。

2. **"ReaLM-Retrieve Section 6.9 的 31% verification rate 可推广到 Search-R1 + Qwen2.5-7B 设置"**：
   ReaLM-Retrieve 使用 DeepSeek-R1-Distill-Qwen-32B 且有自己的 QueryGen 架构，其观察到的 verification pattern 可能与模型规模和架构高度相关。在 7B 模型 + 不同 RL 框架下，verification retrieval 是否仍然是一个 distinct 且 beneficial 的 pattern 是未知的。

3. **"|entailment - contradiction| 是 verification retrieval 的正确 reranking 信号"**：
   一个文档可以与 claim 有强 entailment/contradiction 关系但事实上不相关或不可靠。这个指标衡量的是 NLI 模型的判断置信度，不一定等于 "evidentially informative"。

4. **"二元分类（discovery/verification）是最优粒度"**：
   这个假设虽有合理论证（minimal distinction capturing most variance），但本质上是便利性选择而非有理论支撑的设计。实际 reasoning chain 中的 retrieval intent 可能有更丰富的结构（clarification, comparison, quantification 等）。

【3 维度打分】:

  1. Novelty: 【弱-中】 — 核心贡献是 "operationalize an observation from ReaLM-Retrieve"——将 ReaLM-Retrieve 自己观察到但未利用的 discovery/verification 区分变为显式机制。这是一个合理但 obvious-in-hindsight 的 next step：任何读过 ReaLM-Retrieve Section 6.9 的研究者都会想到"既然 verification retrieval 有不同 pattern，为什么不做不同处理"。Intent classification + differentiated pipeline 的组合在 reasoning-augmented RAG 中是新的，但各组件（BM25/dense hybrid、NLI reranking、contrastive query、RL token format）都来自已有工作的直接拼装。"RL-discovered query strategies" 作为 co-equal contribution 是投机性的——它依赖于一个尚不确定的实验发现，不构成方法论创新。与最相关 5-10 篇近期工作比较后，剥离 surface differences 剩余的 novelty delta 是：显式 intent token + pipeline routing。这是一个 engineering-level 的差异，而非 conceptual-level 的。

  2. Significance: 【中】 — 研究问题本身是重要的：reasoning-augmented retrieval 中 query construction 的质量确实是瓶颈，这一点被 Shakya et al. (2026) 和 ReaLM-Retrieve 的 failure analysis 共同证实。但这个 specific proposal 的影响力受限于：(a) binary intent taxonomy 可能过于粗糙，预期改进幅度有限；(b) 即使 positive，结果大概率是 "moderate improvement on benchmarks"（~2-5% F1），reviewer 会说 "I would have guessed this would help a bit"，不会说 "surprising"；(c) 方法的可推广性受限于需要 NLI reranker 和 dense retriever 的额外基础设施，增加了 deployment 复杂度。不过，如果 RL-discovered query patterns 分析做得好，有一定的 analytical insight 价值。

  3. Related Work: 【强】 — 这是 proposal 最突出的优点。对 2024-2026 年的 reasoning-augmented retrieval 领域做了非常系统的梳理，沿 5 个维度（implicit adaptation, timing/volume control, reasoning-retrieval coordination, post-retrieval quality, verification）清晰分类，差异化定位明确。ReaLM-Retrieve、Veri-R1、AutoRefine、CoRAG、DeepControl、RAFTS、HARIS、Reason and Verify 等均有准确描述和定位。Gap identification 是 genuine 的——确实没有现有系统在 sequential reasoning chain 中做 explicit intent classification + differentiated query construction。唯一的小瑕疵是对 ReaLM-Retrieve Section 6.9 的数据过度依赖作为动机的全部基础。

【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
Related Work 的覆盖和 gap identification 是 strong 的，证明了作者对领域的深入理解，这为论文的 "positioning" 质量提供了保底。但 Novelty 是核心限制因素：idea 的本质是 "operationalize an obvious next step from ReaLM-Retrieve's observation"，属于 incremental engineering contribution 而非 conceptual breakthrough。更严重的是，两个 trivial alternative（uniform hybrid for all, implicit RL learning）构成真实威胁，且 proposal 中未充分讨论。Significance 受限于预期结果的 "I would have guessed this" 性质——即使 positive results，审稿人不太可能认为 surprising。综合来看，这是一个 "方向正确、positioning 优秀但 idea 内核偏薄" 的 proposal，典型的 25% 区间。但 trivial alternative 威胁和核心假设的逻辑跳跃将上界压到 ~28%，中位值降至 22%。

【主要风险】:
1. **Trivial alternative 致命威胁**：Reviewer 几乎必然要求 "uniform hybrid retrieval for all queries" baseline，如果该 baseline 接近 dual-intent 的表现，则 intent classification 的增量价值被否定，论文核心贡献坍塌。
2. **核心前提的逻辑跳跃**："implicit adaptation cannot capture discovery/verification distinction because verification is anti-correlated with topical relevance" 的论证将 dense retriever 的训练目标与 RL policy 的训练目标混淆——RL 优化下游 EM/F1，不是 topical relevance。如果 RL 本身就能隐式学会差异化 query construction，显式 intent token 可能是多余的 inductive bias。
```

**补充说明**：

这个 proposal 在**形式完善度**上是顶级的——compute budget 精确到小时、NLI model separation 的 circularity 论证、per-step training calibration、contingency plan 等都显示了极高的工程规划能力。但正如评估原则所强调的，形式完善度 ≠ idea 好。透过这些精心设计的细节看本质，核心 claim 是："显式区分 retrieval intent 并用不同 pipeline 处理比让 RL 隐式学习更好"——这个 claim 的说服力取决于是否能排除 trivial alternatives，而这恰恰是 proposal 目前最薄弱的环节。

Sources:
- [ReaLM-Retrieve: When to Retrieve During Reasoning](https://arxiv.org/abs/2604.26649)
- [Veri-R1: Claim Verification via Online RL](https://arxiv.org/abs/2510.01932)
- [AutoRefine: Search and Refine During Think](https://arxiv.org/abs/2505.11277)
- [Search-R1: Training LLMs to Reason and Leverage Search Engines](https://arxiv.org/abs/2503.09516)
- [HARIS: Coordinating Search-Informed Reasoning](https://arxiv.org/abs/2506.07528)
- [Contrastive Retrieval-Augmented Generation on Experience](https://aclanthology.org/2025.findings-acl.1224.pdf)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:

存在两个有威胁性的 trivial alternatives：

1. **"All-Hybrid" baseline**: 对所有 retrieval call 一律使用 hybrid BM25+dense + NLI reranking，完全跳过 intent 分类。如果 hybrid retrieval 本身就优于 BM25-only（proposal 自己引用了 "hybrid retrieval improves recall by 15-30%"），那最简单的做法就是对所有 query 都用 hybrid pipeline。Intent 分类的增量价值只有在"discovery queries 用 hybrid 反而变差"时才成立——这是一个未经验证的假设。Proposal 暗示"contrastive query 可能干扰 exploratory retrieval"，但这缺乏理论或实证依据。如果 all-hybrid 的性能与 dual-intent 差异不大（例如 <1% F1），审稿人会说"the classification adds complexity without commensurate gain"。

2. **AutoRefine-style post-retrieval refinement**: AutoRefine 已经在相同 framework (Search-R1/veRL/GRPO) 上通过 post-retrieval evidence distillation 实现了大幅提升（HotpotQA: 0.405 vs 0.297, MuSiQue: 0.157 vs 0.066）。如果 post-retrieval refinement 能在不修改 query construction 的情况下达到类似效果，那 dual-intent retrieval 的增量价值就被大幅压缩。Proposal 需要证明 query construction differentiation 提供的增益是 orthogonal to（且无法被替代 by）post-retrieval refinement。

增量价值声称点：proposal 认为 verification query 需要"actively seek disconfirming evidence, which is anti-correlated with topical relevance" —— 这是其最核心的理论支点。但这个论点本身是 assertion 而非 evidence：没有实证表明 learned query generators 无法隐式学到这一点，也没有理论解释为什么 continuous embedding space 在数学上无法编码 contrastive retrieval intent。

【前提假设检验】:

核心逻辑链: "ReaLM-Retrieve 观察到 verification retrieval 是一个 distinct pattern → 这种 pattern 需要 structurally different queries → explicit classification + differentiated pipelines 优于 implicit adaptation → binary taxonomy 足以捕捉 intent variation"

逻辑链中的未验证假设：

(a) **"Implicit adaptation 无法 capture 这个 structural distinction"**: Proposal 断言 "Implicit query adaptation via learned representations cannot capture this structural distinction because a verification query should actively seek disconfirming evidence, which is anti-correlated with the topical relevance signal." 这是整个 idea 最关键的假设，但它缺乏支撑。ReaLM-Retrieve 的 QueryGen 是 learned cross-attention，理论上完全可以在 continuous space 里编码 contrastive intent —— 只是 ReaLM-Retrieve 没有显式优化这一点，不等于 continuous representation 原则上做不到。如果一个更好训练的 implicit query generator 就能解决问题，显式分类就变成不必要的 overhead。

(b) **Binary taxonomy 的充分性**: ReaLM-Retrieve 识别了三种 pattern (early resolution 42%, verification 31%, failed retrieval 12%)。Proposal 将 early resolution 和 failed retrieval 合并为 "discovery"，但 early resolution (已找到答案但还在 retrieval) 和 genuine exploration (需要新信息) 的 retrieval needs 截然不同。这种强制合并可能丢失重要信息。

(c) **Heuristic classification 的可靠性**: 用文本匹配 ("therefore", "this means") 来分类 intent 是一个相当粗糙的 proxy。Reasoning traces 中 claim-like statements 和 question-like statements 可能没有清晰的语法分界，特别是在 Qwen2.5-7B 这个 scale 的模型上。75% heuristic accuracy 是一个 low bar，意味着 25% 的 intent 被错分，在 RL training 中可能引入 systematic noise。

(d) **NLI reranking by |entailment − contradiction| 能 surface 高质量 verification evidence**: DeBERTa-v3-base NLI 模型在 out-of-domain Wikipedia passages 上的 entailment/contradiction 判断可能不够 reliable，特别是对于隐含的、需要推理的 claims。如果 NLI scoring 本身噪声很大，整个 verification pipeline 的信号质量就会被拖累。

【3 维度打分】:

1. Novelty: 【中】
   — 核心 gap 是真实的：目前确实没有系统在 reasoning chain 内做 explicit intent classification + differentiated query construction。搜索确认了这一点。
   — 但 novelty 的"真实程度"需要打折：(i) 核心 insight 直接来自 ReaLM-Retrieve Section 6.9 的观察，proposal 自称 "we make it actionable"——这是 operationalization，不是 discovery；(ii) 各个组件（BM25、dense retrieval、NLI reranking、GRPO training、intent tokens）全部是已有的，组合方式虽然新但属于 engineering novelty；(iii) "co-equal contribution" 的 RL-discovered query strategies 完全是 speculative，属于"如果结果好就是 novelty"的 outcome-dependent claim。
   — 与最相关 5 篇近期工作（ReaLM-Retrieve, Veri-R1, AutoRefine, CoRAG, RAFTS）比较，剔除 surface differences 后剩余 novelty：一个 binary intent classifier + routing logic。这是 real but thin。

2. Significance: 【中】
   — 研究问题本身重要：reasoning-augmented retrieval 是 2025-2026 的热点方向，intent-aware retrieval 是一个 natural next step。
   — 但 "surprising" 测试不通过：如果核心发现是 positive（intent-differentiated retrieval 优于 uniform retrieval），大多数审稿人会说 "I would have guessed this — of course different retrieval needs benefit from different strategies." 缺乏反直觉元素。
   — 方法高度耦合于 Search-R1/veRL/GRPO 框架，推广性有限。结论是否能 generalize 到其他 reasoning-retrieval systems (如 proprietary models 的 tool use) 不清楚。
   — 如果 improvement 幅度较小（如 1-2% F1），这个 significance 会进一步下降。

3. Related Work: 【强】
   — 覆盖非常全面：ReaLM-Retrieve, Veri-R1, CoRAG, AutoRefine, DeepControl, RAG-Star, RAFTS, HARIS, AgentIR, Reason and Verify, R1-Searcher++, REPAIR, FIRE 等均有覆盖。
   — 差异化定位清晰：对每篇工作都精确说明了"它做了什么、不做什么、和我们的区别在哪"。
   — 搜索验证后确认：proposal 声称的 gap（没有系统在 sequential reasoning chain 内 explicitly classify intent + differentiate query construction）在我搜索范围内是成立的。
   — 唯一小问题：HARIS (Jun 2025) 的两层 agent 架构中 reasoning agent 向 search agent 委派"targeted queries"，这与 intent differentiation 有一定相似性，proposal 可以更细致地区分。

【概率估计】: [22% - 32%] 中位 27%

【估计理由】:
Related Work 维度是强项，说明 gap 定位准确、positioning 清晰。但概率上限被 Novelty 和 Significance 共同压制：

(1) Novelty 是 operationalization 而非 discovery —— 核心 insight 借自 ReaLM-Retrieve，组件全部已有，真正的 delta 是 routing logic + 一个 binary classifier，这在 EMNLP 主会的 novelty bar 下偏薄。

(2) Significance 受限于 "I would have guessed this" 效应 —— positive result 不 surprising，negative result 也不 surprising（因为 heuristic classification 可能太粗糙）。缺乏无论结果如何都能产出深刻 insight 的 dual-outcome 保障。

(3) Trivial alternative 威胁真实存在 —— all-hybrid baseline 和 AutoRefine-style post-retrieval refinement 都可能 match 或 subsume 大部分 gain，审稿人很可能要求这两个 ablation，而 proposal 的 compute budget 已经非常紧张。

(4) "Co-equal contribution"（RL-discovered query strategies）是 outcome-dependent —— 如果 RL 没有发现有趣的 query patterns，这个 contribution 就不存在，论文变成单纯的 intent routing + 小幅性能提升。

(5) 竞争激烈：RAG+Reasoning 是 2025-2026 最拥挤的赛道之一，EMNLP 在这个方向的 submission 密度极高，incremental improvements 的接受门槛显著提高。

概率区间 22-32% 反映了：idea 方向正确、gap 真实、positioning 清晰（下限不低于 22%），但 novelty thin + 预期结果不 surprising + trivial alternative 威胁（上限被压制在 32%）。

【主要风险】:
1. **Trivial Alternative 致命威胁**：All-hybrid baseline（对所有 query 统一使用 hybrid BM25+dense + NLI reranking，不做 intent 分类）可能达到与 dual-intent 相近的性能。如果 ablation 证明 intent classification 的 marginal gain 很小，整个 paper 的 contribution 会塌缩为 "we confirmed that hybrid retrieval is better than BM25-only"——这不是一个 publishable finding。
2. **"Expected Result" 风险**：核心发现若为 positive，审稿人大概率反应为 "intuitive, not surprising"。缺乏反直觉元素意味着论文必须靠 (a) 大幅度性能提升 或 (b) 深刻的 analytical insights（如 RL-discovered strategies）来弥补——两者都是 outcome-dependent，无法在 idea 层面保证。
```

Sources:
- [ReaLM-Retrieve: When to Retrieve During Reasoning](https://arxiv.org/abs/2604.26649)
- [Veri-R1: Toward Precise and Faithful Claim Verification via Online RL](https://arxiv.org/abs/2510.01932)
- [Search-R1: Training LLMs to Reason and Leverage Search Engines](https://arxiv.org/abs/2503.09516)
- [HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search](https://arxiv.org/abs/2506.07528)
- [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384)
- [CoRAG: Chain-of-Retrieval Augmented Generation](https://arxiv.org/abs/2501.14342)


【原始 proposal（允许参考但不是主要依据）】:
# Dual-Intent Retrieval: Intent-Differentiated Query Formulation for Reasoning-Augmented RAG

**状态**: 待审阅  
**级别**: top-tier  
**创建时间**: 2026-05-15T16:06:37.791174+00:00

## 描述
We propose Dual-Intent Retrieval, a method that explicitly classifies each retrieval call within a reasoning model's chain-of-thought as either discovery-intent (seeking new evidence to advance reasoning) or verification-intent (seeking evidence to confirm or refute an intermediate claim), then applies structurally different query construction and retrieval strategies for each. Discovery queries use standard BM25 retrieval, matching its strength at keyword-rich information-seeking queries. Verification queries use a hybrid BM25+dense retrieval pipeline with NLI-based contrastive reranking: given an intermediate claim, the model generates contrastive queries (seeded by templates during SFT, refined through RL), retrieves via both BM25 and E5-base-v2 dense retrieval, and re-ranks by evidential discriminativeness using DeBERTa-v3-base NLI scoring, surfacing documents that most clearly support or refute the claim.

This operationalizes an insight that ReaLM-Retrieve empirically observed but did not act upon: its behavioral analysis (Section 6.9) identifies 'verification retrievals' as a distinct pattern in 31% of cases that reduces backtracking by 18%, while its failure analysis finds that over-retrieval during exploration accounts for 31% of failures. Despite observing that retrieval intent varies structurally, ReaLM-Retrieve's QueryGen maps all retrieval calls through the same learned embedding space without differentiating strategy. Even Veri-R1 (Oct 2025), which trains verification-specific RL policies via GRPO with a multi-component reward (label + evidence IoU + format + validity), uses uniform query construction across all search turns. We make this insight actionable.

The approach addresses a broader gap: ReaLM-Retrieve adapts queries implicitly without distinguishing purpose; CoRAG (NeurIPS 2025) reformulates queries iteratively but uniformly; DeepControl (ICLR 2026 Workshop) controls retrieval volume, not query strategy; AutoRefine (NeurIPS 2025) refines evidence post-retrieval; RAG-Star (NAACL 2025) verifies answers in MCTS with uniform retrieval; Veri-R1 (Oct 2025) trains verification-specific RL but uses uniform query construction; RAFTS (ACL 2024) demonstrates contrastive argument synthesis for fact-checking but operates standalone; Reason and Verify (Mar 2026) structures verification taxonomies for biomedical RAG but applies uniform retrieval. None classify intent and differentiate query construction within RL-trained sequential reasoning.

The contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format. The latter is a co-equal contribution: the structured format creates a rich action space for GRPO to discover sophisticated verification strategies (e.g., negation patterns, contrastive framing, claim-type-specific formulations) that humans might not manually design — and the query evolution analysis in Phase 3 is positioned as a key expected finding.

Built atop Search-R1's open-source RL framework using Qwen2.5-7B (chosen over Qwen3-8B to avoid a known 10-20× GRPO training speed regression in veRL), we introduce intent tokens (&lt;discover>/&lt;verify>) and train via GRPO with a composite reward combining answer correctness and faithfulness. A critical design choice: we use different NLI model families for verification reranking (DeBERTa-v3-base, 184M params) vs. faithfulness reward (RoBERTa-large-NLI, 355M params) to prevent circular optimization where the policy learns to game its own reward signal. Intent labels are bootstrapped via heuristic rules for SFT cold start, then refined through RL. The &lt;verify>claim ||| query&lt;/verify> format allows RL to learn sophisticated query formulations beyond initial templates, following RAFTS's insight that LLM-generated contrastive formulations outperform fixed templates. We evaluate on six benchmarks — MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER — against Search-R1, IRCoT, AutoRefine, RAG-Star, and Veri-R1 baselines (with model-scale caveats for Veri-R1's 3B models and ReaLM-Retrieve's 32B). StrategyQA tests implicit multi-hop reasoning where the model must infer what type of evidence to seek; FEVER is the canonical claim verification benchmark directly comparable with Veri-R1's evaluation; HOVER tests multi-hop verification — together providing comprehensive coverage of both the discovery and verification aspects of our contribution. A mandatory pilot validates that discovery/verification intent is distinguishable — well-motivated given ReaLM-Retrieve's 31% verification rate.

**Compute budget with verified arithmetic:** The entire pipeline fits within ~202 H100-hours (hard cap ≤210). Phase 2 (the dominant cost) runs 2 GRPO training configurations × 500 steps each on 8×H100. Per-step time is ~75 sec (range: 65-90 sec; calibrated from veRL benchmarks showing 60-70 sec/step for Qwen2.5-7B on 8×A800, ms-swift issue #3302, with Search-R1 retrieval overhead partially offset by H100 throughput). Per run: 500 steps × 75 sec = 10.4 wall-hours × 8 GPUs = ~83 H100-hours. Two runs = ~166 H100-hours. Plus overhead (pilot 5h, SFT 5h, NLI 8h, eval 18h) = ~202 H100-hours. 500 steps matches Search-R1's own protocol and exceeds AutoRefine's 300-step convergence; GRPO risks reward collapse beyond 500 steps, making this a well-calibrated choice. Contingency: reduce to 400 steps if per-step exceeds 90 sec, giving ~196h total.

Primary target: AAAI 2027 (abstract ~July 21, full paper ~July 28, 2026), providing a comfortable ~10-week window. The May 25, 2026 ARR cycle — the last eligible for EMNLP 2026 (commitment deadline August 2, 2026; note: there is no June ARR cycle, as ARR switched to 10-week review cycles) — is a stretch goal only. ICLR 2027 (~October 2026) serves as a fallback for extended experiments.

## 核心问题
Current reasoning-augmented retrieval systems optimize various aspects of the retrieval-reasoning interface — when to retrieve (ReaLM-Retrieve), how much to retrieve (DeepControl), how to refine retrieved evidence (AutoRefine), and how to coordinate retrieval with reasoning structure (DualRAG, HARIS) — yet all treat query construction as a single undifferentiated process. ReaLM-Retrieve's learned QueryGen module generates context-adaptive query representations via cross-attention to reasoning step embeddings, adapting queries implicitly through learned representations. Critically, ReaLM-Retrieve's own behavioral analysis (Section 6.9) empirically identifies 'verification retrievals' as a distinct pattern in 31% of cases — reducing backtracking by 18% — and its failure analysis finds that 'over-retrieval during exploration' accounts for 31% of failures (Section 7.3). These observations directly evidence that retrieval intent varies structurally within reasoning chains and that intent-mismatched retrieval actively degrades performance. Yet ReaLM-Retrieve does not operationalize this insight: its QueryGen maps all retrieval calls through the same continuous embedding space, conflating exploratory and confirmatory information needs. No system explicitly classifies the purpose of each retrieval call within a reasoning chain and applies structurally different query construction strategies accordingly. Even Veri-R1 (Oct 2025), which specifically trains models for claim verification via GRPO with iterative retrieval across up to 3 search turns, applies the same uniform query construction strategy across all retrieval calls — further evidencing that the discovery/verification distinction is not operationalized even in verification-specialized systems. Within a reasoning chain, a retrieval call seeking new evidence to explore an unknown sub-question (discovery) requires broad, recall-oriented queries, while one checking whether a specific intermediate claim holds (verification) requires targeted, claim-contrastive queries that seek both supporting and refuting evidence. Implicit query adaptation via learned representations cannot capture this structural distinction because a verification query should actively seek disconfirming evidence, which is anti-correlated with the topical relevance signal that learned query generators optimize for. This intent-blind retrieval means verification-stage retrievals return topically relevant but evidentially uninformative documents, degrading reasoning faithfulness. The problem is compounded by evidence that retrieval can actively hurt reasoning when poorly matched to reasoning needs — Shakya et al. (2026) show that traces including retrieval perform slightly worse than CoT without retrieval, but that adaptive retrieval (choosing when to retrieve) improves overall performance, suggesting that retrieval quality and intent matching — not just retrieval timing or volume — is a critical bottleneck.

## 机遇 / Why Now
ReaLM-Retrieve empirically observed that retrieval intent varies within reasoning chains — identifying verification retrievals (31% of cases) as a distinct beneficial pattern and over-retrieval during exploration (31% of failures) as a primary failure mode — but did not operationalize this insight. We make it actionable via explicit intent classification and structurally differentiated query construction.

Reasoning models now produce long CoT traces with explicit intermediate claims that create a structurally exploitable retrieval signal: 'retrieve evidence to check claim X' is functionally distinct from 'retrieve evidence to answer question Y,' and these two modes demand different query construction strategies — yet no existing system makes this distinction explicit and operationalizes it at query construction time.

Recent work has advanced adjacent aspects of this space without addressing this core gap. On implicit query adaptation: ReaLM-Retrieve (Apr 2026) uses a learned single-layer transformer decoder QueryGen that generates context-adaptive 768-dim query embeddings via cross-attention to reasoning step representations, achieving 71.2% F1 on MuSiQue (+11.8% over standard RAG) with only 1.8 retrieval calls — but its learned representations adapt queries implicitly without distinguishing retrieval purpose, and its own error analysis reveals this as a limitation. On retrieval-verification in tree search: RAG-Star (NAACL 2025) uses retrieval-augmented verification within MCTS, scoring answer-document consistency to guide tree search backpropagation, but applies uniform retrieval for every sub-query and operates in tree-structured (not sequential) reasoning. On iterative query reformulation: CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling, achieving SOTA on KILT, but applies the same reformulation strategy regardless of whether the model needs exploration or confirmation. On retrieval control: DeepControl (ICLR 2026 Workshop) measures marginal information utility to control retrieval continuation and granularity (+9.4% over Search-R1 on Qwen2.5-7B), but controls how much to retrieve, not how to construct purpose-differentiated queries. On evidence refinement: AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls with retrieval-specific rewards via GRPO, dramatically improving multi-hop QA, but refines evidence post-retrieval without differentiating query construction. On reasoning-aware retrieval embeddings: AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification. On RL-trained claim verification: Veri-R1 (Oct 2025) trains Qwen2.5-3B-Instruct via GRPO for iterative claim verification on FEVEROUS/FEVER/HOVER/SciFACT, improving joint accuracy by 30% and doubling evidence scores — but applies the same query strategy across all search turns despite being verification-specialized. On domain-specific structured verification: Reason and Verify (Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N — but applies uniform retrieval without intent classification and is not RL-trained.

The precise gap: existing systems adapt query representations implicitly through learned embeddings (ReaLM-Retrieve, CoRAG, AgentIR), reformulate queries iteratively (CoRAG), control retrieval volume (DeepControl), refine evidence post-retrieval (AutoRefine, SURE-RAG, Entropic Claim Resolution), verify answers in tree search (RAG-Star), train verification-specific RL policies with uniform retrieval (Veri-R1), or structure verification taxonomies in domain-specific settings (Reason and Verify) — but none explicitly classifies retrieval intent as discovery vs. verification and applies structurally different query construction strategies for each, particularly claim-contrastive retrieval that actively seeks disconfirming evidence for verification-intent calls. ReaLM-Retrieve's own analysis shows this distinction exists and matters; Veri-R1's uniform approach to verification-specific retrieval confirms it remains unaddressed even in the most targeted systems. We operationalize it.

## 方法思路
We build a dual-intent retrieval module on top of the open-source Search-R1 framework that introduces explicit intent-differentiated query formulation into reasoning-augmented retrieval. The approach has four phases designed to fit within ~200 H100-hours and ~11 days.

**Model choice: Qwen2.5-7B.** We use Qwen2.5-7B as the primary model, not Qwen3-8B. This is a deliberate choice motivated by a known, unresolved training speed regression: Qwen3-8B exhibits 10-20× slower generation during veRL GRPO training compared to Qwen2.5-7B (veRL GitHub issues #1580, #3816), with each step taking ~1 hour instead of minutes. The root cause appears to be Qwen3's thinking mode generating excessively long outputs (~7000 tokens vs ~1000 tokens), and this affects even non-thinking configurations due to architectural differences in how vLLM handles Qwen3. Qwen2.5-7B is the backbone Search-R1 was originally validated on, with proven GRPO training efficiency and 24% average relative improvement on QA benchmarks. We use Qwen2.5-7B-Base for the primary experiments, consistent with Search-R1's original evaluation.

**Phase 0 — Pilot Feasibility (Day 1, ~5 H100-hours):** Generate reasoning traces on 500 MuSiQue training examples using standard Search-R1 with Qwen2.5-7B. Apply heuristic rules to classify each &lt;search> call: if the preceding reasoning contains an explicit claim or assertion ('X is Y', 'therefore', 'this means') followed by retrieval, label it VERIFY; if it contains a question decomposition or information-seeking pattern ('I need to find', 'what is', sub-question form), label it DISCOVER. Manually inspect 100 labeled examples and compute distribution statistics. Go/no-go: proceed only if both categories appear with ≥15% frequency and heuristic accuracy ≥75%. This threshold is well-motivated: ReaLM-Retrieve's analysis found verification retrievals comprise 31% of cases, suggesting ≥15% is easily achievable.

**Phase 1 — Implementation (Days 2-4):** Extend the Search-R1 token format: replace the single &lt;search>query&lt;/search> with two intent-tagged variants: &lt;discover>query&lt;/discover> and &lt;verify>claim ||| query&lt;/verify>. The verify format includes both the claim and an optional model-generated query, enabling RL to learn sophisticated query formulations beyond templates. This dual-format design serves a deeper purpose beyond mere classification: by structuring verification retrieval as explicit claim ||| query pairs, we give the RL optimization a rich action space in which to develop intent-specific query patterns. The model must learn not just what to search for, but how to construct queries that surface evidence specifically relevant to confirming or refuting its tentative claim — a fundamentally different skill from exploratory information-seeking. Implement differentiated query processing in the search environment:

(a) Discovery mode — pass the query to BM25, return top-3 results (same as baseline). BM25 is appropriate for discovery queries because they tend to be keyword-rich and information-seeking, matching BM25's lexical matching strength.

(b) Verification mode — uses a hybrid retrieval pipeline to address the limitation that BM25 performs poorly on semantically-oriented contrastive queries. Extract the claim and the model-generated query (or, during SFT cold-start, generate a contrastive query pair via templates: 'evidence supporting [claim]' / 'evidence contradicting [claim]'). Retrieve top-3 via BM25 (lexical match on claim content) and top-3 via dense retrieval (E5-base-v2, which Search-R1 already supports as a retrieval backend) using the contrastive queries. Pool the 6 results, re-rank by evidential discriminativeness using an NLI cross-encoder (cross-encoder/nli-deberta-v3-base, 184M params) to score entailment and contradiction, returning the top-3 documents ranked by |entailment − contradiction| score (most discriminative first). The hybrid BM25+dense approach is motivated by evidence that hybrid retrieval improves recall by 15-30% over either method alone, and dense retrieval is critical for semantic matching on contrastive queries where keywords like 'supporting'/'contradicting' are uninformative for BM25. Note: Search-R1 provides pre-built E5-base-v2 FAISS indexes for its Wikipedia corpus, eliminating index-building overhead.

**Template limitation and RL-learned query refinement (co-equal contribution):** We acknowledge that template-based contrastive queries ('evidence supporting/contradicting [claim]') are simplistic — real verification needs are more nuanced (causal claims require different evidence patterns than factual or temporal claims). The &lt;verify>claim ||| query&lt;/verify> format is specifically designed to allow the model to learn more sophisticated query formulations through RL. During SFT cold-start, templates provide the initial format. During GRPO training, the model is free to generate arbitrary text in the query field, learning from outcome rewards which query formulations yield the most useful evidence. This follows RAFTS's (ACL 2024) insight that LLM-generated contrastive arguments outperform fixed templates, but integrates the learning directly into the RL loop rather than requiring a separate generation step. We position the RL-discovered verification query strategies as a co-equal contribution alongside the intent taxonomy itself: if the model learns to use negation patterns, hedge framing, contrastive structures, or claim-type-specific formulations that humans would not manually design, this constitutes a compelling finding about how structured action spaces enable emergent strategy discovery through reward optimization.

SFT cold start: relabel heuristically-classified Search-R1 traces with intent tokens and fine-tune Qwen2.5-7B-Base for ~100 steps to learn the new format.

Note on Search-R1 RL algorithm: Search-R1 supports both PPO and GRPO via separate training scripts (train_ppo.sh and train_grpo.sh) built on the veRL framework. We use the GRPO configuration for training efficiency and stability, consistent with recent work (AutoRefine, DeepControl, Veri-R1) that also builds on Search-R1 with GRPO.

**NLI model separation to avoid reward circularity:** A critical design decision is using different NLI models for verification reranking vs. faithfulness reward computation, to prevent a circular optimization where the model learns to game its own reward signal. During verification-intent retrieval, documents are reranked by |entailment − contradiction| via cross-encoder/nli-deberta-v3-base (DeBERTa architecture, 184M params). The faithfulness reward component uses a different model family: ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli (RoBERTa-large architecture, 355M params, trained on SNLI+MNLI+FEVER+ANLI). Using different architectures (DeBERTa disentangled attention vs. RoBERTa standard attention) and different training data distributions ensures the models have different decision boundaries, preventing the policy from learning to select documents that trivially satisfy the reward without genuinely improving evidential quality. The circularity concern is real: if the same model ranks documents and scores faithfulness, the optimization target reduces to 'retrieve documents that this specific model scores highly on' rather than 'retrieve genuinely informative evidence.' Different models with different inductive biases prevent this collapse.

**NLI reranking cost analysis:** DeBERTa-v3-base (184M params) processes ~800-1200 sentence pairs/sec on a single H100. During GRPO training with global batch size B=256, average R=2.5 retrieval calls per sample, and estimated verification fraction V=0.4, total NLI pairs per step = B × R × V × 6 = 256 × 2.5 × 0.4 × 6 ≈ 1,536 pairs. At 1,000 pairs/sec, this adds ~1.5 seconds per step. The RoBERTa-large reward model (355M params) processes ~400-600 pairs/sec; with ~3 claims per trace × 256 samples = ~768 pairs, adding ~1.5 seconds per step. Combined NLI overhead is ~3 seconds per step. Compared to the LLM forward/backward pass on 8×H100 with Qwen2.5-7B, total NLI overhead is ~5-10% — manageable without dedicated hardware. To minimize memory contention, we run NLI inference on CPU (adding ~10-15 sec per step, still <25% overhead) or allocate a fraction of one GPU's memory. We budget an additional ~8 H100-hours for NLI overhead across all training runs.

**Phase 2 — RL Training (Days 5-8, ~166 H100-hours on 8×H100):** Train with GRPO using a composite reward: R = α·EM(answer) + (1−α)·faithfulness, where faithfulness is the fraction of intermediate claims in the reasoning trace that are supported (entailment > 0.5) by at least one retrieved document, scored by the RoBERTa-large NLI model (distinct from the DeBERTa reranker). Set α = 0.7 (tunable). Run two configurations: (1) full dual-intent with hybrid contrastive verification retrieval (primary), (2) standard Search-R1 baseline with GRPO (ablation: no intent). The BM25-only ablation (dual-intent tokens with standard retrieval for both modes) is deferred to save compute; it can be added as a reduced-scale 250-step run (~28 H100-hours) if the primary runs finish under budget.

**Per-run compute arithmetic:** Each run uses 500 training steps on 8×H100, matching Search-R1's own training protocol (the original Search-R1 paper trains for exactly 500 steps with checkpoints every 100 steps). Per-step time estimate: the veRL GRPO benchmark shows 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with NuminaMath-TIR (ms-swift issue #3302). Search-R1's multi-turn retrieval adds overhead from search engine calls during rollout generation (~2-4 search calls per trajectory with BM25 latency <50ms each) and longer context sequences (max_prompt_length=4096 vs ~2048 for math). H100's ~1.3× throughput advantage over A800 partially offsets this overhead. We estimate ~75 sec/step (range: 65-90 sec), yielding: 500 steps × 75 sec = 37,500 sec ≈ 10.4 wall-hours per run. Per-run GPU-hours: 10.4 wall-hours × 8 GPUs = **~83 H100-hours**. Two runs total: **~166 H100-hours**. **Contingency:** if per-step time exceeds 90 sec, reduce to 400 steps per run — still above AutoRefine's 300-step convergence point — giving 400 × 90 sec ≈ 10.0 wall-hours × 8 GPUs ≈ 80 H100-hours per run, ~160 H100-hours total for Phase 2.

**Convergence justification for 500 steps:** 500 steps matches Search-R1's own training protocol, where the original paper uses exactly 500 steps for both Qwen2.5-3B and Qwen2.5-7B with GRPO. AutoRefine (NeurIPS 2025), built on the same Search-R1/veRL/GRPO stack, trains for only 300 steps and achieves its reported gains (HotpotQA: 0.405 F1, MuSiQue: 0.157 F1). GRPO-LEAD converges in ~200 steps with top-performing checkpoints selected via validation. Empirical GRPO training dynamics show gradient norms stabilize by step 40, with most accuracy gains in the first 200-300 steps. Additionally, GRPO is known to risk reward collapse when trained for too many steps, further motivating 500 steps as a well-calibrated choice rather than a compromise.

**Phase 3 — Evaluation & Analysis (Days 9-11, ~18 H100-hours):** Evaluate on MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, and HOVER (6 benchmarks). MuSiQue, HotpotQA, and 2WikiMultiHopQA are standard multi-hop QA benchmarks requiring compositional reasoning with explicit decomposition. StrategyQA requires implicit multi-hop reasoning where the decomposition strategy is not given — the model must infer what type of evidence to seek, making it an ideal showcase for intent-differentiated retrieval since the discovery/verification transition is not signaled by the question structure but must emerge from the model's reasoning process. FEVER is the canonical fact verification benchmark (185K claims, supported/refuted/NEI) — essential for a method whose core contribution involves verification-intent retrieval, and directly comparable with Veri-R1's evaluation on the same benchmark. HOVER is a multi-hop claim verification benchmark requiring evidence from 2-4 Wikipedia articles, testing both discovery (finding relevant articles across hops) and verification (confirming multi-hop claims against aggregated evidence). Metrics: answer F1/EM, faithfulness (claim-support rate), retrieval precision/recall on supporting evidence. Baselines: Search-R1 (reproduced with GRPO), IRCoT, and ReaLM-Retrieve (reported numbers with model-scale caveats, as their best results use DeepSeek-R1-Distill-Qwen-32B). Additional comparisons: AutoRefine (reported numbers, NeurIPS 2025), RAG-Star (reported numbers from Llama-3.1-8B-Instruct), Veri-R1 (reported numbers on HOVER and FEVER, with model-scale caveats since Veri-R1 uses Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct while we use 7B; we will report per-parameter efficiency where feasible to enable fair comparison). Analysis: (a) intent distribution — what fraction of retrievals are classified as discovery vs. verification across all six benchmarks, and how this compares to ReaLM-Retrieve's observed 31% verification rate, (b) per-intent retrieval quality — does verification mode retrieve more evidentially discriminative documents (measured by |entailment − contradiction| spread), (c) comparison with implicit adaptation — does explicit intent classification outperform ReaLM-Retrieve's learned QueryGen on verification-heavy reasoning chains, (d) NLI model separation analysis — compare performance with same-model vs. different-model reranking/reward to quantify circularity effects, (e) **query evolution analysis (key expected finding)** — do RL-learned verification queries diverge from initial templates, and what patterns emerge (claim-type-specific formulations, negation patterns, contrastive framing, hedge structures, etc.)? This analysis is positioned as a key finding, not merely a diagnostic: if RL discovers intent-specific query patterns that humans wouldn't write — e.g., systematically different query structures for causal vs. factual vs. temporal claims — that constitutes a compelling result in its own right, demonstrating that the structured &lt;verify>claim ||| query&lt;/verify> format enables emergent strategy discovery through reward optimization, (f) error analysis — when does intent misclassification degrade performance, (g) case studies showing how contrastive verification queries surface disconfirming evidence that standard and implicitly-adapted queries miss, (h) StrategyQA-specific analysis — does intent-differentiated retrieval show disproportionate gains on implicit decomposition tasks where the model must infer retrieval intent without explicit question structure?

**Design justifications:** The binary discovery/verification taxonomy is the minimal distinction that captures the most variance in retrieval intent within reasoning chains. This choice is now directly grounded in ReaLM-Retrieve's empirical findings: their three behavioral patterns (early resolution 42%, verification 31%, failed retrieval 12%) naturally collapse into our binary taxonomy — early resolution and failed retrieval are both discovery-intent (information-seeking), while verification retrievals map directly to our verification-intent. The choice is further motivated by Shakya et al.'s (2026) finding that retrieval during exploration can hurt reasoning while adaptive retrieval helps — suggesting that the exploration/confirmation axis is the primary dimension along which retrieval intent varies. Finer categories (clarification, disambiguation, quantitative validation) are subsumed: clarification and disambiguation are discovery subtypes, quantitative/causal verification are verification subtypes. Binary classification is also more robust with limited RL training budget and avoids the need for multi-class intent supervision. The framework is extensible to additional intent types via new tokens.

The key distinction from related approaches: ReaLM-Retrieve's QueryGen learns a continuous mapping from reasoning states to query embeddings, and its own analysis reveals that verification retrievals are a distinct beneficial pattern — but it does not operationalize this insight by applying different retrieval pipelines. Veri-R1 trains verification-specific RL policies with a multi-component reward (label + evidence IoU + format + validity) but uses the same uniform query strategy across all search turns — even its emergent 'fine-grained subclaim-level decomposition' is not structurally supported by differentiated retrieval. Our approach makes intent classification explicit and applies structurally different retrieval pipelines — critically, verification queries use hybrid BM25+dense retrieval with NLI-based contrastive reranking to actively seek disconfirming evidence, which is anti-correlated with topical relevance maximization. RAG-Star uses retrieval for verification within MCTS but verifies candidate answers at tree nodes with uniform relevance-based retrieval, not intermediate claims with contrastive queries. AutoRefine's &lt;refine> step distills evidence post-retrieval but doesn't change how queries are constructed. CoRAG reformulates queries iteratively but applies the same reformulation strategy regardless of intent. DeepControl controls retrieval volume and timing but not query construction strategy. RAFTS (ACL 2024) demonstrates that contrastive argument synthesis improves fact verification, but operates as a standalone pipeline — we integrate contrastive retrieval directly into the RL-trained reasoning loop. Reason and Verify (Mar 2026) structures verification with an eight-category taxonomy for biomedical RAG but applies uniform retrieval — we address a different dimension (retrieval pipeline differentiation) in a domain-general RL-trained setting.

The contribution is dual: (1) explicit intent classification with structurally differentiated retrieval pipelines, and (2) RL-discovered verification query strategies that emerge from the &lt;verify>claim ||| query&lt;/verify> format — the latter being a co-equal contribution that may yield insights about how structured action spaces enable emergent retrieval strategies.

Fallback: if claim extraction quality is poor in the reasoning trace (e.g., no clear propositional claim before a retrieval call), default to discovery mode — this is safe because discovery mode is equivalent to the baseline.

## 研究现状
The reasoning-augmented retrieval landscape in 2025-2026 has advanced along five axes — implicit query adaptation, retrieval timing/volume control, retrieval-reasoning coordination, post-retrieval evidence quality, and reasoning-stage verification — creating a rich but precisely gapped design space.

**Implicit query adaptation.** ReaLM-Retrieve achieves 71.2% F1 on MuSiQue with 1.8 retrieval calls by combining step-level uncertainty-based retrieval timing with a learned QueryGen module (single-layer transformer decoder, 512 hidden dim, 8 attention heads) that cross-attends to current reasoning step embeddings, producing context-adaptive 768-dim query representations for ColBERTv2 dense retrieval. The +11.8% F1 improvement on MuSiQue (+10.1% average across three benchmarks) demonstrates that adaptive query generation substantially outperforms static queries. Crucially, ReaLM-Retrieve's own behavioral analysis (Section 6.9) identifies three dominant retrieval patterns: 'early resolution' (42% of cases, yielding 23% shorter reasoning chains), 'verification retrievals' (31%, reducing backtracking by 18%), and 'failed retrievals' (12%, extending chains by 8%). Its failure analysis (Section 7.3) finds that over-retrieval during exploratory reasoning phases accounts for 31% of failures by 'disrupting productive chains by prematurely committing to hypotheses.' These observations directly evidence that retrieval intent varies structurally and that intent-mismatched retrieval degrades performance — yet QueryGen's cross-attention mechanism learns a single continuous mapping from reasoning states to query embeddings, conflating exploratory and confirmatory needs into the same representation space. CoRAG (NeurIPS 2025) dynamically reformulates queries based on evolving reasoning state via rejection sampling training, establishing SOTA on KILT with >10-point EM improvements on multi-hop QA, but applies uniform reformulation strategy regardless of retrieval purpose. AgentIR (Mar 2026) encodes reasoning traces into retrieval embeddings for intent-aware retrieval but treats all retrieval calls uniformly without intent classification.

**Retrieval timing and volume control.** DeepControl (ICLR 2026 Workshop) formalizes information utility as U(e) = ρ·Novelty + (1−ρ)·Effectiveness, using an annealed control-forcing curriculum to train retrieval continuation and granularity control, achieving +9.4% on Qwen2.5-7B over RL baselines across seven benchmarks. R1-Searcher++ trains models to decide whether to use internal knowledge or external search. Shakya et al. (Feb 2026) find that 'traces including retrieval actually perform worse compared to CoT' while the model's decision to adaptively avoid retrieval improves overall performance — suggesting that retrieval quality and intent matching matters more than retrieval quantity.

**Retrieval-reasoning coordination.** Search-R1 trains LLMs via RL (supporting both PPO and GRPO) to issue search queries within reasoning, achieving +41%/+20% on QA benchmarks for 7B/3B models, with Qwen2.5-7B as the primary validated backbone. AutoRefine (NeurIPS 2025) introduces a &lt;refine> step between search calls that distills evidence from ~600 to ~100-200 tokens, trained with GRPO using dual rewards (answer correctness + retrieval quality), achieving major gains on multi-hop QA (HotpotQA: 0.405 vs 0.297 Search-R1; MuSiQue: 0.157 vs 0.066). DualRAG (ACL 2025) coordinates reasoning-augmented querying with progressive knowledge aggregation. HARIS (arXiv 2506.07528, Jun 2025) uses a hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B, evaluating on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop) for claim verification — but with uniform search strategy across all retrieval calls. IRCoT interleaves retrieval at fixed intervals.

**Post-retrieval evidence quality.** SURE-RAG (May 2026) scores claim-evidence pairs for sufficiency. Entropic Claim Resolution (Mar 2026) selects discriminative evidence via entropy minimization. RAFTS (ACL 2024) synthesizes contrastive supporting/refuting arguments from retrieved passages via LLM-based generation with a two-stage BM25+dense retrieval pipeline for standalone fact verification — demonstrating that contrastive evidence framing improves verification accuracy, but operating as a standalone fact-checking system rather than integrated in reasoning RL loops. Reason and Verify (arXiv 2603.10143, Mar 2026) integrates explicit sub-claim grounding with an eight-category verification taxonomy for biomedical RAG, achieving 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct. Though domain-specific (biomedical) and not RL-trained, it demonstrates concurrent interest in structured verification within RAG, using BGE cross-encoder reranking and rationale grounding — but applies uniform retrieval without intent classification. REPAIR (Jan 2026) uses reasoning plans for mid-course correction during reranking. All operate downstream of query construction.

**Reasoning-stage verification.** RAG-Star (NAACL 2025) uses MCTS for deliberative reasoning with retrieval-augmented verification: for each MCTS node, retrieval checks answer-document consistency (scoring 1=unverifiable, 2=conflict, 3=aligned) with query- and answer-aware reward modeling. However, RAG-Star verifies candidate answers at MCTS tree nodes using uniform retrieval, not intermediate claims within sequential reasoning chains, and does not use contrastive queries to actively seek disconfirming evidence. Veri-R1 (arXiv 2510.01932, Oct 2025) is the most directly comparable RL-based verification system: it trains Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct via GRPO for iterative claim verification with up to 3 search turns, using a 4-component reward (label correctness +2, evidence IoU, format compliance, validity weight). Evaluated on FEVEROUS, EX-FEVER, FEVER, SciFACT, and HOVER, Veri-R1 improves joint accuracy by up to 30% and doubles evidence scores vs baselines. Open-source and built on Search-R1/veRL. Critically, despite being designed specifically for claim verification, Veri-R1 does NOT differentiate retrieval intent — all search queries use the same uniform strategy, whether the model is exploring for initial evidence or confirming a tentative conclusion. Its case analysis shows Online RL naturally develops 'fine-grained subclaim-level decomposition,' but this emergent behavior is not structurally supported by differentiated retrieval pipelines. FIRE (NAACL Findings 2025) uses confidence-based iterative retrieval for fact-checking with 7.6× cost reduction but applies the same query strategy per iteration. 'Don't Let It Hallucinate' (NeurIPS 2025) transforms queries into logical premises for pre-generation verification, operating before reasoning chains begin. VERITAS rewards faithful reasoning but doesn't modify retrieval.

**The gap.** All existing systems either (a) adapt query representations implicitly through learned embeddings without distinguishing retrieval purpose — even when their own analysis shows the distinction exists and matters (ReaLM-Retrieve, CoRAG, AgentIR), (b) control retrieval timing/volume without differentiating query construction (DeepControl, R1-Searcher++), (c) refine evidence post-retrieval without improving the upstream query (AutoRefine, SURE-RAG, ECR, RAFTS), (d) verify answers in tree search or pre-generation without contrastive query construction within sequential reasoning (RAG-Star, FIRE, Don't Let It Hallucinate), (e) train verification-specific RL policies but still use uniform query construction across all search turns (Veri-R1), or (f) structure verification taxonomies in domain-specific settings without intent-differentiated retrieval (Reason and Verify). No system explicitly classifies retrieval intent as discovery vs. verification within sequential reasoning chains and applies structurally different query construction strategies for each — particularly claim-contrastive retrieval that actively seeks disconfirming evidence during verification.

## 目标 Venue
- AAAI 2027 (abstract ~July 21, 2026; full paper ~July 28, 2026 — primary target with comfortable ~10-week window for experiments, analysis, and paper writing)
- ARR May 25, 2026 → EMNLP 2026 (commitment deadline August 2, 2026) — stretch goal only, requires aggressive 10-day execution with pre-existing Search-R1/veRL familiarity; note: this is the last eligible ARR cycle for EMNLP 2026, as the next ARR cycle (August 3, 2026) falls after the EMNLP commitment deadline; no June ARR cycle exists due to ARR's switch to 10-week review cycles
- ICLR 2027 (expected ~October 2026 — fallback allowing additional model scales, extended ablations, or supplementary benchmarks)

## 关键参考
- Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning (arXiv 2503.09516, Mar 2025) — base framework; supports PPO and GRPO via veRL, &lt;search> token format; validated on Qwen2.5-7B with 24% average relative improvement; trains for 500 GRPO steps with checkpoints every 100 steps; provides pre-built BM25 and E5 FAISS indexes for Wikipedia corpus
- When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models [ReaLM-Retrieve] (arXiv 2604.26649, Apr 2026) — learned QueryGen module (single-layer transformer decoder, cross-attention to reasoning step embeddings, 768-dim adaptive query representations); +11.8% F1 on MuSiQue (71.2%), +10.1% average across 3 benchmarks; Section 6.9 identifies verification retrievals (31% of cases) as a distinct pattern reducing backtracking by 18%; Section 7.3 identifies over-retrieval during exploration as 31% of failures; implicitly adaptive but not intent-differentiated despite observing the need
- RAG-Star: Enhancing Deliberative Reasoning with Retrieval Augmented Verification and Refinement (NAACL 2025, Jiang et al.) — MCTS-based reasoning with retrieval-augmented verification at tree nodes (answer-document consistency scoring), query- and answer-aware reward modeling; verifies candidate answers in tree search with uniform retrieval, not intermediate claims with contrastive queries
- Chain-of-Retrieval Augmented Generation [CoRAG] (NeurIPS 2025, arXiv 2501.14342) — dynamic query reformulation via rejection sampling training, SOTA on KILT, >10-point EM on multi-hop QA; reformulates queries based on evolving state but without intent differentiation
- Scaling Search-Augmented LLM Reasoning via Adaptive Information Control [DeepControl] (arXiv 2602.01672, ICLR 2026 Workshop SPOT) — information utility = ρ·Novelty + (1−ρ)·Effectiveness, retrieval continuation and granularity control with annealed curriculum; +9.4% on Qwen2.5-7B over RL baselines; controls retrieval volume, not query construction strategy
- Search and Refine During Think [AutoRefine] (NeurIPS 2025, arXiv 2505.11277) — &lt;refine> step distilling evidence between search calls, GRPO with dual rewards (answer + retrieval quality); trains for 300 steps on Search-R1/veRL/GRPO stack and achieves convergence; HotpotQA: 0.405 vs 0.297 Search-R1, MuSiQue: 0.157 vs 0.066; refines evidence post-retrieval without intent-differentiated query construction
- Retrieval Augmented Fact Verification by Synthesizing Contrastive Arguments [RAFTS] (ACL 2024) — LLM-based contrastive supporting/refuting argument synthesis with two-stage BM25+dense retrieval pipeline; demonstrates contrastive evidence framing improves verification; standalone system, not integrated in reasoning RL
- Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning (arXiv 2510.01932, Oct 2025) — GRPO-trained iterative claim verification with Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct on FEVEROUS/EX-FEVER/FEVER/SciFACT/HOVER; 4-component reward (label correctness + evidence IoU + format compliance + validity weight); improves joint accuracy by 30%, doubles evidence scores; does NOT differentiate retrieval intent despite being verification-focused; open-source on Search-R1/veRL; most directly comparable RL-based verification baseline
- HARIS: Coordinating Search-Informed Reasoning and Reasoning-Guided Search in Claim Verification (arXiv 2506.07528, Jun 2025) — hierarchical two-agent architecture (reasoning + search) with GRPO training on Qwen3-4B; evaluates on EX-FEVER (80.12% F1 on 2-hop) and HOVER (61.00% accuracy on 4-hop); uniform search strategy without intent differentiation
- Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation (arXiv 2603.10143, Mar 2026) — biomedical RAG with eight-category verification taxonomy, explicit sub-claim grounding, BGE cross-encoder reranking; 89.1% on BioASQ-Y/N with Llama-3-8B-Instruct; domain-specific but demonstrates concurrent interest in structured verification within RAG; uniform retrieval without intent classification
- R1-Searcher++: Incentivizing Dynamic Knowledge Acquisition of LLMs via RL (arXiv 2505.17005, May 2025) — internal vs. external knowledge distinction, not intent within external retrieval
- REPAIR: Adaptive Retrieval for Reasoning-Intensive Retrieval (arXiv 2601.04618, Jan 2026) — reasoning plans for reranking; operates post-retrieval, not at query construction
- FIRE: Fact-checking with Iterative Retrieval and Verification (NAACL Findings 2025) — confidence-based iterative retrieval; 7.6× cost reduction but same query strategy per iteration
- Don't Let It Hallucinate: Premise Verification via Retrieval-Augmented Logical Reasoning (NeurIPS 2025) — pre-generation premise verification, not during reasoning chain
- Adaptive Retrieval helps Reasoning in LLMs — but mostly if it's not used (arXiv 2602.07213, Shakya et al., Feb 2026) — traces with retrieval perform slightly worse than CoT; adaptive retrieval (choosing when to retrieve) improves overall performance; directly motivates that retrieval quality and intent matching matters more than retrieval volume
- DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop QA (ACL 2025) — dual reasoning-retrieval processes but uniform retrieval strategy
- AgentIR: Reasoning-Aware Retrieval for Deep Research Agents (arXiv 2603.04384, Mar 2026) — encodes reasoning traces in embeddings but uniform intent across all retrieval calls
- SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective RAG (arXiv, May 2026) — post-retrieval claim-evidence scoring
- Entropic Claim Resolution: Uncertainty-Driven Evidence Selection for RAG (arXiv, Mar 2026) — post-retrieval evidence selection via entropy minimization
- Beyond Correctness: Rewarding Faithful Reasoning in RAG [VERITAS] (arXiv, Oct 2025) — faithfulness reward for generators, not retrieval modification
- Interleaving Retrieval with Chain-of-Thought Reasoning [IRCoT] (ACL 2023) — fixed-interval retrieval baseline
- Adaptive-RAG: Learning to Adapt Retrieval-Augmented LLMs through Question Complexity (NAACL 2024)
- veRL GitHub issues #1580, #3816 — Qwen3-8B GRPO training 10-20× slower than Qwen2.5-7B due to generation speed regression; motivates our model choice
- ms-swift GitHub issue #3302 — GRPO training speed benchmark: 60-70 sec/step for Qwen2.5-7B full-parameter GRPO on 8×A800 with veRL; calibrates our per-step compute estimate

## 资源估算
### auto_research
- **claude_api_cost**: $200-400 (est. 2000-4000 turns for autonomous experiment design and paper drafting)
- **estimated_gpu_cost**: ~$630 (210h × ~$3.00/hr)
- **gpu_hours**: ≤210 H100-hours (hard budget cap). Agent must track cumulative GPU-hours (wall-time × GPUs, not wall-time alone) and prioritize: primary dual-intent run (~83h) and baseline run (~83h) are mandatory; BM25-only ablation at 250 steps (~42h) is included only if cumulative spend remains ≤168h after the two primary runs. If approaching cap, agent reduces ablation steps or skips lowest-priority analysis.
- **gpu_utilization**: ~85-95% utilization; agent pipelines experiments continuously
- **risk_note**: Agent should implement early stopping on reward plateau detection (GRPO risks reward collapse beyond ~500 steps); if pilot feasibility fails (intent categories not distinguishable), agent should pivot to testing contrastive verification queries without intent classification
- **speed_bottleneck**: Primary bottleneck is sequential GRPO runs on 8 GPUs (~10.4 wall-hours each at 75 sec/step); BM25 index pre-built, E5 FAISS index downloadable from Search-R1; NLI inference adds ~5-10% per-step overhead
- **team**: 0 (initial setup and final review only)
- **timeline**: 6-9 days with 8×H100 available

### human_in_loop
- **claude_api_cost**: $100-200 (est. 1000-2000 turns for code generation and experiment analysis)
- **estimated_gpu_cost**: ~$606-630 (202-210h × ~$3.00/hr)
- **gpu_hours**: ~202-210 H100-hours. Base plan (~202h) plus agent-proposed extensions with human approval: reduced-scale BM25-only ablation (250 steps on 8×H100 = 250 × 75 sec ≈ 5.2 wall-hours × 8 GPUs ≈ ~42h), reward weighting variants, or heuristic threshold tuning. Extensions prioritized by expected information value within remaining budget.
- **gpu_utilization**: ~55-70% utilization; agent queues experiments while human reviews
- **risk_note**: Composite faithfulness+correctness reward may need human judgment on α weighting if RL training shows reward hacking on the faithfulness component; if per-step time exceeds 90 sec, human approves step-count reduction to 400
- **team**: 1 researcher, ~20-30min/day reviewing proposals and results
- **timeline**: 2-3 weeks

### manual
- **estimated_gpu_cost**: ~$606 (202h × ~$3.00/hr H100 spot pricing)
- **gpu_hours**: ~202 H100-hours total (range: 183-215 depending on per-step training speed). Breakdown with explicit wall-time × GPU arithmetic: Phase 0 pilot: ~5h (generation only, 1-2 GPUs); Phase 1 SFT cold start: ~5h (100 SFT steps); Phase 2 GRPO training: 2 runs × 500 steps × ~75 sec/step = 2 × (10.4 wall-hours × 8 GPUs) = ~166h; NLI overhead during training: ~8h; Phase 3 evaluation on 6 benchmarks: ~18h. Dense index building: ~0h (Search-R1 provides pre-built E5-base-v2 FAISS indexes). Per-step calibration: veRL GRPO benchmarks show 60-70 sec/step for Qwen2.5-7B on 8×A800 (ms-swift issue #3302); we estimate ~75 sec/step for Search-R1 on 8×H100, accounting for retrieval overhead partially offset by H100 throughput advantage. Contingency: if per-step exceeds 90 sec, reduce to 400 steps/run (above AutoRefine's 300-step convergence), giving 2 × (10.0 wall-hours × 8 GPUs) = ~160h for Phase 2, ~196h total.
- **gpu_utilization**: ~40-50% effective utilization; GPUs idle during implementation, debugging, and analysis phases
- **team**: 1 researcher with RL and retrieval experience
- **timeline**: 10-12 days (10 days with 8×H100 and familiarity with Search-R1/veRL codebase; 12 days otherwise)



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b92099dc-fbbc-4359-91fd-1bc45d61b7d2",
  "type": "user",
  "uuid": "e2e011fb-7a56-4a0f-97f0-394d7cd2ee29",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T01:55:13.031Z_

```json
{
  "parentUuid": "e2e011fb-7a56-4a0f-97f0-394d7cd2ee29",
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
  "uuid": "0b1d07c8-c8aa-4b65-b7c0-354ac67639f9",
  "timestamp": "2026-05-16T01:55:13.031Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T01:55:13.031Z_

```json
{
  "parentUuid": "0b1d07c8-c8aa-4b65-b7c0-354ac67639f9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4a1311f4-bb65-4867-8acd-687e377ef479",
  "timestamp": "2026-05-16T01:55:13.031Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a thorough assess…",
  "leafUuid": "4a1311f4-bb65-4867-8acd-687e377ef479",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Dual-Intent Retrieval for Reasoning-Augmented RAG",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0"
}
```

---

### Assistant

_source line 8 · 2026-05-16T01:55:51.287Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them according to the Meta Judge format.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability: [18% - 28%] 中位 22%


**Reviewer 2:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability: [18% - 28%] 中位 22%
**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 27%

Now I'm calculating the aggregate statistics across all three reviewers. The median probabilities are 22%, 22%, and 27%, which gives me a mean of approximately 23.7% and a median of 22%. I'm also computing the standard deviation to understand the spread in reviewer assessments. The mean is 23.67, and calculating the sample standard deviation gives me about 2.89%, which puts this right at the boundary between high and medium consistency. Now I'm looking at which points have consensus across the reviewers and identifying any outliers.

All three reviewers agree on several key issues: novelty ranges from weak-to-medium or medium, significance is solidly medium, and related work coverage is strong. There's very strong consensus around the all-hybrid baseline being a trivial alternative, with additional agreement that post-retrieval refinement and implicit RL learning are also problematic. The reviewers consistently note this feels incremental and unsurprising, and they're flagging the RL-discovered strategies as a concern.

The core assumption about disconfirming evidence being anti-correlated with topical relevance is weak across all three reviews, and there are concerns about the heuristic classification reliability and whether the binary taxonomy is sufficient. A few points stand out as unique: R2 makes a sharp observation about RL optimizing embedding/F1 metrics rather than topical relevance itself, R3 distinguishes between early resolution and genuine exploration within the discovery framing, and R1 quantifies around 30% intent label errors.

R3 emerges as slightly more generous on novelty, rating it as medium rather than weak-to-medium like the others, and assigns a higher probability of 27% compared to 22% from R1 and R2. The standard deviation of about 2.9% suggests borderline consistency, so I'm gravitating toward the median range of 22-24%. Given the principle of being conservative with acceptance, I should lean toward the lower end of that range.

Looking at the bounds across all three reviews: the lower bounds cluster at 18% (two reviewers) and 22% (one), while the upper bounds are mostly 28% with one at 32%. Taking the median of these bounds gives me a lower bound of 18% and upper bound of 28%, with the central estimate around 23%—slightly above the two stricter reviewers but well below R3's more generous assessment.

Now I need to move on to the implementation assessment. The reviewers didn't provide formal implementation sections, but the proposal itself contains those details, so I'll extract what's relevant from there and then prepare the final Meta Judge output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a1311f4-bb65-4867-8acd-687e377ef479",
  "isSidechain": false,
  "requestId": "req_011Cb5R3MwC5BzC9zxkzPxJ6",
  "type": "assistant",
  "uuid": "540c0b62-b993-43be-ae80-9da852652a6b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaV9Vy9XPYpQrhJaoN2Vy5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28327,
      "cache_read_input_tokens": 11374,
      "output_tokens": 4097,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4097,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 28327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28327
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

_source line 9 · 2026-05-16T01:56:54.083Z_

【阶段】: Meta Judge
【三次中位】: [22%, 22%, 27%]  std=2.9%
【共识维度】:
- **Novelty 弱-中（3/3）**：三位审稿人一致认为核心贡献是"operationalize an existing observation from ReaLM-Retrieve Section 6.9"，属于 incremental engineering contribution 而非 conceptual breakthrough。各组件（BM25/dense hybrid、NLI reranking、GRPO、intent tokens）均为已有技术的拼装。
- **Significance 中（3/3）**：三位均认为研究问题本身重要，但预期结果缺乏反直觉性（"I would have guessed this"），positive result 不 surprising。
- **Related Work 强（3/3）**：三位一致高度肯定 gap identification 和 positioning 质量，确认 proposal 声称的 gap 在搜索范围内成立。这是 proposal 最强维度，无争议。
- **Trivial Alternative "All-Hybrid" 致命威胁（3/3）**：三位均独立识别出"统一使用 hybrid BM25+dense+NLI reranking 处理所有 query"这一 trivial baseline，认为若其性能接近 dual-intent，则 intent classification 的增量价值被消解。这是最强共识信号。
- **核心假设"disconfirming evidence 与 topical relevance 反相关"论证薄弱（3/3）**：三位均指出该假设是 assertion 而非 evidence，是整个 idea 理论基础最脆弱的环节。
- **"Co-equal contribution"（RL-discovered strategies）为 outcome-dependent 投机（3/3）**：三位一致认为这不构成方法论创新，在实验前是空洞的 claim。
- **AutoRefine post-retrieval refinement 作为替代路径的威胁（2/3，R1+R3）**：若 post-retrieval refinement 能弥补 query construction 的不足，upstream intent differentiation 的增量价值被压缩。
- **Heuristic classification 可靠性隐忧（2/3，R1+R3）**：25% 错误率在 RL 训练中可能引入系统性噪声。
- **Implicit RL learning 作为替代路径（2/3，R1+R2）**：RL 优化下游 EM/F1 而非 topical relevance，可能隐式学会差异化 query construction，无需显式 intent token。

【异常维度】:
- **R3 给 Novelty "中"而非"弱-中"**：R3 对"组合的新颖性"稍微宽松，但仍承认是 "real but thin"。与 R1/R2 的判断差距不大，属于 rubric 边界的主观判断差异，非实质性分歧。降权处理，不影响综合判断。
- **R3 "binary taxonomy 中 early resolution 与 genuine exploration 合并丢失信息"**：仅 R3 明确提出。有一定道理但不构成致命问题（proposal 有合理论证），降权。
- **R2 "RL 训练目标与 dense retriever 训练目标混淆"**：R2 独有的尖锐表述——指出 proposal 将 RL policy 优化目标（EM/F1）与 dense retriever 的 topical relevance 目标混为一谈。这实际上是核心假设薄弱性的一个具体表现，与共识维度重叠，不视为真正异常。

【最终概率】: [18% - 28%] 中位 23%
【一致性】: 高（偏中）
【综合理由】:
三位审稿人在所有关键维度上高度一致：Novelty 弱-中、Significance 中、Related Work 强。std=2.9% 处于高一致与中一致的边界，但 rubric 判决几乎完全收敛（唯一差异是 R3 的 Novelty 从"弱-中"微调至"中"，且 R3 自己也承认 novelty 是 "real but thin"），因此实质一致性高。

中位 23% 的推导逻辑：
1. **Related Work 强**提供了 ~20% 的保底（gap 真实、positioning 清晰、不会因 related work 覆盖不足被直接拒稿）
2. **Novelty 弱-中**严格限制上界——operationalize an obvious next step + 已有技术的拼装，在 EMNLP 主会的 novelty bar 下属于 borderline-reject 级别。即使实验完美，idea 质量天花板约 ~30%
3. **Significance 中**进一步压缩——"I would have guessed this" 效应意味着即使 positive results 也缺乏 surprise value，需要大幅度性能提升或深刻 analytical insight 来补偿，但两者都是 outcome-dependent
4. **三位一致的 trivial alternative 威胁**（all-hybrid baseline）是最强下行风险——若该 ablation 表现接近，论文核心贡献坍塌。这将概率上界从理论上的 ~30% 压至 ~28%
5. R3 略高（27%）但其自身论证也承认 novelty thin + trivial alternative 真实，更高概率主要反映对"方向正确"的更宽松权重。按"宁缺毋滥"原则，综合中位偏向两位更严格的审稿人（22%），但不完全忽略 R3 的合理性，因此微调至 23%

**概率未低于 18% 的理由**：gap 确实存在且被充分论证（3/3 确认）、related work 覆盖极强、如果 RL-discovered patterns 出现 surprising 结果有上行空间、形式完善度高（计算规划精确、contingency plan 完备）。

**概率未高于 28% 的理由**：Novelty 的 incremental nature 是硬伤；trivial alternative 威胁真实且未回应；核心理论假设论证薄弱；co-equal contribution 是空洞的 outcome-dependent claim；RAG+Reasoning 赛道极度拥挤，incremental improvement 的接受门槛已显著提高。

【建议】: 边缘（偏不推荐）
【实施评估】:
  - 计算资源: ~202-210 H100-hours（硬上限），需 8×H100 集群约 10-11 天。Phase 2 GRPO 训练为主要成本（~166 H100-hours），规划精确且有 contingency plan（400 steps fallback）。预算合理但紧张，BM25-only ablation 已被 deprioritize，而三位审稿人一致要求的 all-hybrid ablation 未被纳入计算预算，需额外 ~42-83 H100-hours。
  - 数据需求: 6 个公开 benchmark（MuSiQue, HotpotQA, 2WikiMultiHopQA, StrategyQA, FEVER, HOVER），均公开可得。Search-R1 提供预构建 BM25 和 E5-base-v2 FAISS 索引，无需自建索引。无新数据收集需求。
  - 人工介入: 最低限度——Phase 0 需人工检查 100 个 heuristic 标注样本（~2-3 小时），Phase 3 需人工审查 case studies。无大规模人工标注。auto_research 模式下几乎全自动，human_in_loop 模式 ~20-30min/day。
  - 训练需求: 需要模型训练。SFT cold start ~100 steps（~5 H100-hours）+ GRPO RL 训练 2 runs × 500 steps（~166 H100-hours）。基座模型 Qwen2.5-7B（非从头训练）。额外 NLI 模型（DeBERTa-v3-base 184M + RoBERTa-large 355M）为预训练模型直接使用，无需训练。
  - 新 Benchmark: 不需要。使用现有公开 benchmark。
  - 预估周期: 自动模式 6-9 天，人工模式 10-12 天，留出 paper writing 时间后：主目标 AAAI 2027（~10 周窗口，充裕）；ARR May 25 → EMNLP 2026（stretch goal，极紧张）。**关键风险**：三位审稿人一致要求的 all-hybrid ablation 未在原始计算预算内，若需补充该实验（审稿人几乎必然要求），周期可能延长 2-3 天，预算增加 ~42-83 H100-hours。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "540c0b62-b993-43be-ae80-9da852652a6b",
  "isSidechain": false,
  "requestId": "req_011Cb5R3MwC5BzC9zxkzPxJ6",
  "type": "assistant",
  "uuid": "1b09e966-f01d-4b74-bf97-e1057223f999",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaV9Vy9XPYpQrhJaoN2Vy5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28327,
      "cache_read_input_tokens": 11374,
      "output_tokens": 4097,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4097,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 28327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28327
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a thorough assess…",
  "leafUuid": "1b09e966-f01d-4b74-bf97-e1057223f999",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Dual-Intent Retrieval for Reasoning-Augmented RAG",
  "sessionId": "af047939-0d18-428f-9efd-271e8167c3b0"
}
```

---
