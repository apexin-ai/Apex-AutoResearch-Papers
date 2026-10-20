# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/593076ab-eb07-425a-a678-91f40f4205a2.jsonl`
- **Structured JSON:** [`340acb5e7828f020f1c9.json`](../../sessions/34/340acb5e7828f020f1c9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:55:12.421Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:55:12.421Z",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [PURE / \"Stop Summation: Min-Form Credit Assignment\"](https://arxiv.org/abs/2504.15275) (NeurIPS 2025): 提出 min-form credit assignment 替代 summation-form，显著缓解 PRM reward hacking，在 Qwen2.5-Math-7B 上 MATH-500 达 82.6%。是本 proposal 的直接基础之一（提供 A^min 组件）。\n- [PROGRS / \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"](https://arxiv.org/abs/2604.02341) (arXiv Apr 2026): 使用 frozen quantile-regression PRM + outcome-conditioned centering，在 trajectory 级别校正 PRM bias（MATH-500 74.9% vs DAPO 69.7%）。**这是本 proposal 最近的竞争对手**——同样使用 calibrated PRM，但只做 trajectory-level correction，不做 per-step uncertainty gating。\n- [GRPO-λ](https://arxiv.org/abs/2510.00194) (ICLR 2026): 用 eligibility traces 改进 GRPO 的 credit assignment，7B 模型平均提升 3-4.5 分。信任 PRM 输出是 uniform 的。\n- [Park et al. / \"Know What You Don't Know\"](https://arxiv.org/abs/2506.09338) (NeurIPS 2025): 提出 quantile regression 校准 PRM 置信度，产生校准后的 confidence intervals。**核心发现：PRM 系统性过估成功概率。** 仅应用于 test-time scaling，未用于 RL training。这是本 proposal 的另一个直接基础（提供 CI width 信号）。\n- [\"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\"](https://arxiv.org/abs/2602.01034) (arXiv Feb 2026): 提出 Step-wise Marginal Information Gain + Decoupled Masking 做 per-step process-outcome credit mixing。**概念上与本 proposal 最相近**——也是 per-step 级别的 process-outcome 混合，但使用 Monte Carlo 内在信息增益信号而非 PRM 校准置信度。\n- [UCAS / \"Unlocking Exploration in RLVR\"](https://openreview.net/forum?id=CTmu1mqDuz) (arXiv 2025): 使用 policy model 自身 logit uncertainty 做 advantage shaping。与本 proposal 的区别：UCAS 用 policy-side uncertainty（随训练漂移），UGCA 用 external frozen PRM uncertainty（稳定）。\n- [VPPO / \"Save the Good Prefix\"](https://arxiv.org/abs/2601.18984) (arXiv Jan 2026): 用 PRM 定位首个错误步，施加 binary prefix reward + suffix penalty。是 per-step gating 的退化（hard）形式。\n- [\"Reward Under Attack\"](https://arxiv.org/abs/2603.06621) (arXiv Mar 2026): 证明 PRM 在 adversarial RL 优化下可被系统性利用为\"fluency detectors\"——PRM score >0.9 但 ground-truth accuracy <4%。直接为 uncertainty-aware PRM trust 提供动机。\n- [Distributional PRM](https://arxiv.org/abs/2605.06785) (arXiv May 2026): 通过 conditional optimal transport 达到 SOTA 校准水平，同样仅面向 test-time scaling。\n\n**调研总结**: Process-supervised RL for math reasoning 是一个极度拥挤的赛道（2025-2026 年涌现大量工作）。PRM 校准技术已成熟（Park et al., Distributional PRM），但目前仅用于 test-time scaling；PROGRS 首次将 calibrated PRM 引入 RL training 但仅做 trajectory-level 校正。Per-step process-outcome mixing 已有工作（\"Discovering Process-Outcome Credit\"）但使用 MC 信息增益而非 PRM 校准置信度。本 proposal 定位在\"per-step × verifier calibration\"象限，这个具体交叉点确实空白。\n\n【Trivial Alternative 检验】:\n存在若干更简单的替代方案，proposal 已部分预见并尝试辩护：\n1. **用 raw PRM score magnitude 作为 gating 信号**（而非 CI width）: Proposal 辩称 score ≠ confidence（PRM 可对错误预测产生窄区间、高置信），这个论点合理但需要实证。若实验中 raw score gating 与 CI width gating 差距不大，则核心 novelty 大打折扣。\n2. **直接对低置信步骤施加 global clipping/truncation**: 这是一个更简单的 baseline，proposal 辩称会丢失 partially confident 步骤的信息，但 clipping 的损失有多大是未知的。\n3. **PROGRS trajectory-level centering + PURE min-form**: 不需要 per-step gating，直接组合两者。这可能是最 threatening 的 trivial alternative——如果 trajectory-level 校正已经足够好，per-step 的增量价值可能很小。\n\n**增量价值的关键依赖**: 必须证明 per-step 异质性确实显著（即同一 trajectory 内不同步骤的 PRM 校准质量差异足够大，使得 trajectory-level 处理不够用）。这是一个合理但未经验证的前提。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有以下未验证环节：\n1. **CI width ↔ PRM reliability（核心假设）**: 校准后 CI 宽度确实代理 PRM 逐步预测可靠性。这是整个方法的基石。Proposal 设计了验证实验（w_i quantile bins vs. PRM accuracy），但如果这个相关性不强，整个方法就失去了基础。需要注意：quantile regression 校准的是 success probability 的置信区间，不是 PRM \"对不对\"的置信——这两者有微妙区别。\n2. **Frozen PRM 校准在 policy drift 下保持有效**: PRM 是在初始 rollouts 上校准的，但随着 RL 训练推进，policy 生成的 reasoning 分布会发生漂移。Proposal 设计了 longitudinal tracking 来监控，但这是一个真实的风险——如果校准退化严重，需要周期性 re-calibration，这会增加复杂度和成本。\n3. **Process credit 的 bias 主要来自 PRM miscalibration 而非 structural aggregation**: Proposal 承认 min-form 本身有 structural aggregation bias（UGCA 不声称解决它），但假设 per-step miscalibration bias 是可以通过 gating 解决的主导问题。如果 structural bias 才是主导因素，gating 的效果会有限。\n\n【3 维度打分】:\n1. **Novelty: 中** — 具体组合确实是新的：calibrated PRM CI width → per-step process-outcome sigmoid gating → RL training。没有现有工作恰好做这件事。但这本质上是对已有组件的工程组合：PRM 校准（Park et al. NeurIPS 2025）+ per-step credit mixing（概念上与 arXiv 2602.01034 同构，只是换了信号源）+ min-form credit（PURE）+ GRPO。智识贡献在于 bias-variance tradeoff framing，这是优雅的但不是 surprising 的——\"当 verifier 不确定时少信任它\"是一个直觉上 obvious 的策略。相对于 PROGRS 的增量是 trajectory-level → per-step（粒度提升），相对于 \"Discovering Process-Outcome Credit\" 的增量是 MC information gain → calibrated CI width（信号源替换，更高效但概念上类似）。两个增量都是 meaningful 但都不是 surprising。\n\n2. **Significance: 中** — 问题本身（PRM miscalibration 导致 reward hacking）是真实且重要的，\"Reward Under Attack\"（arXiv 2603.06621）提供了强有力的动机。\"Verifier-Uncertainty-Aware RL\" 的一般化框架有潜在的广泛适用性。但实际影响力受限于：(a) math reasoning RL 赛道极度拥挤，每几周就有新方法出现，单个方法的影响力被稀释；(b) 核心发现如果是 positive（\"per-step uncertainty gating 比 trajectory-level centering 好几个点\"），审稿人很可能的反应是 \"makes sense, nice result\" 而非 \"surprising, I wouldn't have guessed this\"——因为 per-step 优于 trajectory-level 在直觉上是预期内的；(c) 如果是 negative（效果不显著），论文的贡献就退化为一个 negative result + analysis paper。\n\n3. **Related Work: 强** — 这是本 proposal 最突出的优点。文献覆盖全面且准确：2×2 positioning matrix（signal source × granularity）清晰地定位了 UGCA 的位置。对 UCAS、ConfClip、PROGRS、\"Discovering Process-Outcome Credit\"、VPPO 等竞争工作的差异化分析具体且有说服力。引用的论文经核实真实存在且描述准确（PURE NeurIPS 2025 ✓、Park et al. NeurIPS 2025 ✓、PROGRS arXiv 2604.02341 ✓、Reward Under Attack arXiv 2603.06621 ✓）。Jia et al. (ICML 2025) 提供的理论 backing 被恰当引用。\n\n【概率估计】: [25% - 35%] 中位 28%\n\n【估计理由】: Related Work 维度强，说明作者对领域有深入理解且定位清晰——这保证了 proposal 的下限。Novelty 和 Significance 都是\"中\"：核心组合确实是新的（gap 真实存在），但 intellectual surprise 有限——\"用 PRM 置信度做 per-step gating\"是一个 natural next step，审稿人不太可能感到 surprised。上界主要被 **Novelty** 限制：在一个极度拥挤的赛道上，一个 \"natural combination of existing components\" 的工作很难超过 35%，即使执行完美。下界由 Related Work 的扎实程度和 gap 的真实性托住，不会低于 25%。\n\n【主要风险】:\n1. **\"Obvious next step\" 感知风险**: 审稿人可能认为将 PRM 校准从 test-time 拓展到 training-time、从 trajectory-level 细化到 per-step 是一个工程上自然的演进，缺乏足够的 intellectual depth 或 surprising insight。在 math reasoning RL 这个过度拥挤的赛道上，这种 perception 对中稿概率杀伤力很大。\n2. **核心假设脆弱性**: CI width ↔ PRM per-step reliability 的相关性如果不够强（或者在 policy drift 下快速退化），整个方法的理论基础就会动摇。更危险的是，如果 ablation 中 raw PRM score gating 效果接近 CI width gating，则 calibration 这一核心技术贡献的增量价值就被严重削弱。\n```\n\nSources:\n- [PURE - Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)\n- [PROGRS - LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341)\n- [GRPO-λ: Credit Assignment improves LLM Reasoning](https://arxiv.org/abs/2510.00194)\n- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)\n- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)\n- [UCAS - Unlocking Exploration in RLVR](https://openreview.net/forum?id=CTmu1mqDuz)\n- [VPPO - Save the Good Prefix](https://arxiv.org/abs/2601.18984)\n- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)\n- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)\n- [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- Park et al., \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" (NeurIPS 2025): 提出 PRM 的 quantile regression 校准方法，产出逐步置信区间，但仅用于 test-time scaling，未用于 RL 训练。UGCA 的 CI width 计算直接依赖此工作的开源代码。\n- PROGRS / \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\" (arXiv 2604.02341, 2026): 将校准过的 PRM（frozen quantile-regression PRM）引入 RL 训练，但采用 trajectory-level outcome-conditioned centering——同一 trajectory 内所有 step 接受相同的 centering 处理。MATH-500 上 74.9% vs DAPO 69.7%。这是 UGCA 最直接的上游竞争者，UGCA 的核心增量在于从 trajectory-level 升级到 per-step。\n- PURE / \"Stop Summation\" (NeurIPS 2025): 提出 min-form credit assignment，缓解 reward hacking，MATH-500 82.6%。UGCA 的 process credit 分支直接采用 PURE 的 min-form advantage。\n- \"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\" (arXiv 2602.01034, 2026): 通过 Monte Carlo estimation 的 Step-wise Marginal Information Gain 实现 per-step process-outcome credit mixing。与 UGCA 在 per-step 粒度上直接竞争，但使用 intrinsic information gain 而非外部校准不确定性作为 gating 信号。计算成本更高（需额外 MC rollouts）。\n- SSVPO (ICLR 2026): 基于 Sequential Shapley Values 的 step-level credit assignment，7 个 benchmark 上显著优于 GRPO/DAPO/VinePPO 等，精度提升达 11.6%。这是 per-step credit assignment 的另一条强竞争路线，proposal 中未提及。\n- RTMC (arXiv 2604.11037, Apr 2026): 利用 rollout tree 实现 per-step Q-value estimation，无需 learned critic。也是 per-step credit 的竞争方法，proposal 中未提及。\n- UCAS (arXiv 2510.10649, 2025): 用 policy model 自身的 logit uncertainty 做 advantage shaping。与 UGCA 共享 \"uncertainty-aware credit\" 的 high-level idea，但 uncertainty source 不同（policy-side vs. external PRM calibration）。\n- Jia et al., \"Do We Need to Verify Step by Step?\" (ICML 2025): 证明 outcome supervision 统计上不难于 process supervision，为 UGCA 的 fallback-to-outcome-credit 提供理论保障。\n- \"Reward Under Attack\" (arXiv 2603.06621, 2026): 证明 PRM 可被 adversarially exploit（PRM score >0.9 但 ground-truth accuracy <4%），直接 motivate uncertainty-aware 的 PRM 使用方式。\n- Distributional PRM (arXiv 2605.06785, May 2026): 通过 conditional optimal transport 实现 SOTA PRM 校准，但仅用于 test-time。\n- SPRO / Self-Guided Process Reward Optimization (2025): 从 policy model 自身派生 process rewards，不依赖外部 PRM。\n- PROF-GRPO / Blend-PRM-GRPO (2025): 以固定权重混合 PRM 与 outcome rewards，非自适应。\n\n- 调研总结: 2025-2026 年 process-aware RL for math reasoning 领域极其活跃。Per-step credit assignment 已有多条路线（SSVPO-Shapley、RTMC-rollout tree、Process-Outcome Credit-MC info gain、VPPO-binary gating）。PRM 校准技术已成熟（Park et al., Distributional PRM）。PROGRS 首次将校准 PRM 引入 RL 但止步于 trajectory-level。UGCA 的定位是\"用校准 PRM 的 per-step CI width 做自适应 process-outcome 插值\"，这个具体组合确实未被占据，但它是将现有成熟组件（校准 PRM + min-form credit + GRPO）用一个 sigmoid gating 函数拼接而成的组合式贡献。\n\n【Trivial Alternative 检验】:\n存在多个 simpler alternatives 构成威胁：\n1. **Raw PRM score magnitude 作为 gating**: proposal 本身讨论了此点并给出了\"score ≠ confidence\"的反驳，但审稿人可能要求 empirical 验证这一区分是否 material（即两者差距有多大）。如果 ablation 显示 raw score gating 与 CI width gating 性能差异微弱，UGCA 的增量价值将大幅缩水。\n2. **PROGRS trajectory-level centering 已是强 baseline**: 如果 PROGRS 的 trajectory-level correction 已经捕获了 80%+ 的收益，per-step gating 的 marginal gain 可能不显著。这是最核心的 trivial alternative 威胁——UGCA 必须 empirically 证明 per-step adaptivity 相比 trajectory-level 有 meaningful 的差距。\n3. **简单 per-step hard thresholding**（CI width 超过阈值就完全 fallback to outcome credit）：如果与 soft sigmoid gating 差异不大，则 sigmoid 形式的理论推导变得 cosmetic。\n4. **SSVPO / RTMC 等不依赖 PRM 的 per-step credit 方法**: 如果这些方法在不使用 PRM 的情况下就能实现 comparable 的 per-step credit assignment，UGCA 依赖外部 PRM + 校准的路线就显得 over-engineered。\n\n增量价值关键取决于: per-step PRM calibration confidence 是否比 trajectory-level correction 或非 PRM-based per-step 方法提供 meaningful 的额外信号。这一点目前是假设，尚未验证。\n\n【前提假设检验】:\n核心 claim 的逻辑链存在以下未验证环节：\n\n1. **CI width 是 PRM reliability 的良好 proxy**（关键假设）: proposal 假设\"校准后的置信区间宽度越大 → PRM 在该 step 上越不可靠\"。但 quantile regression 校准的目标是让 CI 覆盖率符合名义覆盖率（如 80% CI 实际覆盖 80% 的真实值），这并不直接等价于\"CI 宽 → prediction error 大\"。宽 CI 可能反映 inherent aleatoric uncertainty（步骤本身有多种合理做法）而非 PRM epistemic failure。proposal 计划了 Spearman correlation 验证，但如果相关性弱，整个方法就失去根基。\n\n2. **Cross-family PRM 校准迁移假设**: Qwen2.5-Math-PRM-7B 在 Qwen3 系列模型的 rollouts 上仍然保持良好校准。Proposal 承认了这一风险并计划验证，但如果校准严重退化，CI width 的信息量将大幅下降。\n\n3. **Frozen PRM 校准在 policy drift 下的稳定性**: RL 训练改变 policy 的输出分布，frozen PRM 的校准可能随训练进行而退化。Proposal 计划了纵向校准追踪（每 25% checkpoint），但未提出明确的 re-calibration 机制——仅说\"discuss periodic re-calibration as mitigation\"。\n\n4. **Gaussian 噪声假设下的最优插值推导**: sigmoid 形式的 gating function 来自\"PRM score noise 方差正比于 w_i²\"的简化假设。实际 PRM 误差分布可能远非 Gaussian，推导的 prescriptive 价值有限。\n\n5. **Process credit = low-variance, outcome credit = unbiased 的二分法过于简化**: 实际中 GRPO 的 group-relative advantage 并非完全\"unbiased\"（取决于 group 内 sample diversity），PURE 的 min-form advantage 的 bias 来源不仅是 PRM miscalibration 还有 min-form 本身的 structural bias（proposal 承认了这一点但声称不解决）。\n\n【3 维度打分】:\n\n1. Novelty: 中 — \n   UGCA 填补的具体 gap（per-step PRM calibration confidence → adaptive process-outcome credit interpolation）确实未被现有工作占据。但这是一个 **组合式贡献**：将三个已有成熟组件（Park et al. 的 quantile calibration、PURE 的 min-form credit、GRPO 的 outcome credit）用一个 sigmoid gating 函数拼接。核心技术贡献本质上是一个 gating equation（α_i = σ(−(w_i − τ)/β)）。与 \"Discovering Process-Outcome Credit\"(arXiv 2602.01034) 相比，UGCA 用 external calibrated uncertainty 替代 intrinsic information gain 做 per-step gating，这是一个 design choice 的差异，不是 paradigm 级别的创新。proposal 未引用 SSVPO (ICLR 2026) 和 RTMC (Apr 2026) 两个直接竞争的 per-step credit assignment 工作，这些方法无需 PRM 校准即可实现自适应 per-step credit，对 UGCA 的必要性构成挑战。bias-variance tradeoff 的理论 framing 是加分项，但在简化假设下的推导其 prescriptive 价值有限。\n\n2. Significance: 中 — \n   研究问题（PRM miscalibration 导致 reward hacking）确实重要且 timely，\"Reward Under Attack\" (arXiv 2603.06621) 的发现直接 motivate 了这一方向。但 significance 受限于：(a) 如果 marginal gain over PROGRS 不显著，实际影响有限；(b) 方法仅在 math reasoning 上验证，跨领域泛化为 future work；(c) \"Verifier-Uncertainty-Aware RL\" 的 broader principle 虽有价值，但当前 instantiation 过于 narrow（单一 PRM、单一 domain）来支撑这个宏大叙事。若核心实验发现 positive（per-step gating 显著优于 PROGRS），审稿人可能的反应更接近 \"makes sense, reasonable engineering\" 而非 \"surprising\"。\n\n3. Related Work: 中偏强 — \n   Related work 覆盖面广、组织清晰（2×2 design space table 很好）。对 PROGRS、PURE、Process-Outcome Credit、UCAS、ConfClip、VPPO 等均有准确定位。但存在重要遗漏：(a) **SSVPO** (ICLR 2026) 是 step-level credit assignment 的重要竞争工作（11.6% accuracy gain over GRPO），完全未提及；(b) **RTMC** (Apr 2026) 是另一条 per-step credit 路线，未提及；(c) **SPRO** (2025) 和 **PROF-GRPO/Blend** 等 process-outcome mixing 方法未充分讨论。这些遗漏意味着 proposal 的 \"gap\" 叙事可能面临审稿人质疑——\"per-step credit 已有多条不依赖 PRM 校准的路线，为什么你的方法必要？\"\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \nNovelty 是主要限制因素。核心贡献是一个 well-motivated 但 incremental 的组合：用现成的校准 CI width 做 sigmoid gating 来插值两种已有 credit assignment 方式。idea 的 \"surprising quotient\" 低——一旦知道 PRM 有校准不确定性信息，\"用它来 gate credit assignment\" 是 most obvious next step。Significance 取决于 marginal gain 的大小（这是 empirical 问题），但 idea 本身的 ceiling 受限于组合性质。Related work 覆盖较好但有关键遗漏（SSVPO, RTMC），可能导致 novelty claim 被削弱。\n\n上界受限于 Novelty（组合式贡献 + 核心技术薄）和 trivial alternative 威胁（PROGRS trajectory-level 可能已足够好）。下界由 idea 方向的合理性、清晰的理论 framing、以及 PRM miscalibration 问题的真实性支撑。\n\n【主要风险】: \n1. **\"Incremental combination\" 判决**: 审稿人极可能指出 UGCA = Park et al. calibration + PURE min-form + GRPO + sigmoid gating，核心技术贡献仅为一个 gating equation，novelty insufficient for a top venue。\n2. **Per-step gating 的 marginal value 不明**: 如果 PROGRS 的 trajectory-level centering 已捕获大部分收益，或 SSVPO/RTMC 等非 PRM 路线已提供 comparable per-step credit，则 UGCA 的 raison d'être 被根本削弱。\n```\n\nSources:\n- [PROGRS - LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341)\n- [PURE - Stop Summation: Min-Form Credit Assignment](https://openreview.net/forum?id=3Sxby0hH1q)\n- [Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)\n- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)\n- [SSVPO: Effective Step-Level Credit Assignment](https://openreview.net/forum?id=g33DGvnHYd)\n- [RTMC: Step-Level Credit Assignment via Rollout Trees](https://arxiv.org/abs/2604.11037)\n- [UCAS: Unlocking Exploration in RLVR](https://arxiv.org/abs/2510.10649)\n- [Jia et al. - Do We Need to Verify Step by Step?](https://arxiv.org/abs/2502.10581)\n- [Reward Under Attack: Analyzing Robustness of PRMs](https://arxiv.org/abs/2603.06621)\n- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)\n- [GRPO-λ / GRPO is Secretly a Process Reward Model](https://openreview.net/forum?id=CTmu1mqDuz)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning\" [PURE] (NeurIPS 2025): 提出 min-form 替代 summation-form credit assignment 以缓解 reward hacking。假设 PRM score 可靠，不做 per-step 可信度区分。本 proposal 的核心 process credit 来源。\n  \n- \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\" [PROGRS] (arXiv 2604.02341, 2026): 使用 frozen quantile-regression PRM + outcome-conditioned centering。在 trajectory level 做校准修正（incorrect trajectories 的 PRM scores 归零中心化），MATH-500 达 74.9% vs DAPO 69.7%。是本 proposal 最直接的竞争对手——同样使用 calibrated PRM，但在 trajectory level 而非 per-step level 操作。\n\n- \"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\" (arXiv 2602.01034, 2026): 提出 Step-wise Marginal Information Gain + Decoupled Masking 做 per-step process-outcome credit mixing，但基于 Monte Carlo estimation 的 intrinsic information gain，非 PRM calibration confidence。计算开销更大。是 per-step mixing 维度的竞争者，但 signal source 不同。\n\n- \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" (Park et al., NeurIPS 2025): 提出 quantile regression 校准 PRM，生成 calibrated confidence intervals。仅用于 test-time scaling（instance-adaptive compute allocation），未将 uncertainty 反馈到 RL training。本 proposal 的技术基座——直接复用其校准方法。\n\n- \"Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport\" (arXiv 2605.06785, May 2026): PRM 校准的最新 SOTA，同样仅用于 test-time scaling。\n\n- GRPO-λ (arXiv 2510.00194, ICLR 2026): eligibility traces 改善 credit assignment，但均匀信任 PRM outputs。\n\n- UCAS (arXiv 2510.10649, 2025): 用 policy 模型自身 logit uncertainty 做 advantage shaping。信号来源是 policy-side，随训练漂移。\n\n- ConfClip (arXiv 2509.17730, 2025): 用 policy confidence 加权 reward。同样是 policy-side signal。\n\n- \"Reward Under Attack\" (arXiv 2603.06621, 2026): 证明 PRM 在 adversarial RL 下 systematically exploitable，PRM scores >0.9 而 accuracy <4%。直接支持 proposal 的 motivation。\n\n- Jia et al. \"Do We Need to Verify Step by Step?\" (ICML 2025): 理论证明 outcome supervision 统计难度不高于 process supervision。为 fallback to outcome credit 提供理论保障。\n\n- VPPO / \"Save the Good Prefix\" (arXiv 2601.18984, 2026): binary first-error gating，per-step 但 hard threshold。\n\n- \"Reducing Credit Assignment Variance via Counterfactual Reasoning Paths\" (arXiv 2605.16302, 2026): 用 counterfactual comparison 做 per-step credit，signal source 不同。\n\n- \"From Reasoning to Agentic: Credit Assignment in RL for LLMs\" (arXiv 2604.09459, 2026): 2024.01–2026.04 credit assignment 综述，覆盖了这个领域的完整 taxonomy。\n\n- 调研总结: 数学推理 RL 中的 credit assignment 是 2025-2026 最活跃的研究方向之一。当前格局沿两轴分化：(1) signal source（verifier calibration vs. intrinsic/structural）和 (2) granularity（per-step vs. trajectory-level）。PROGRS 占据了 \"verifier calibration × trajectory-level\" 象限；\"Discovering Process-Outcome Credit\" 占据了 \"intrinsic × per-step\" 象限。本 proposal 定位于 \"verifier calibration × per-step\" 象限，这一组合确实未被直接占据。但 PROGRS 的 trajectory-level centering 和 \"Discovering Process-Outcome Credit\" 的 per-step mixing 各自覆盖了 UGCA 的一个维度。\n\n\n【Trivial Alternative 检验】:\n\n存在几个成本更低的替代方案需要考量：\n\n(1) **Hard threshold gating**：直接丢弃 CI width 超过阈值的 PRM step（α∈{0,1}），不做 soft sigmoid 插值。这比 soft gating 简单得多，proposal 将其作为 ablation 对照，但如果 hard gating 效果接近，soft gating 的增量 contribution 就很薄。\n\n(2) **PROGRS + 简单 per-step PRM score filtering**：在 PROGRS 的 trajectory-level centering 基础上，对低 confidence 的 step 做简单 clipping（如去掉 bottom 20% confidence 的 step rewards）。这不需要 sigmoid gating 函数、bias-variance framing 等理论构造，但可能捕获大部分收益。\n\n(3) **Raw PRM score magnitude 作为 gating signal**：proposal 认为这混淆了 \"prediction\" 和 \"confidence\"，指出 PRM 可以在错误预测上有高 confidence。这是一个有效的区分点，但需要实证验证两者差距有多大。\n\n增量价值的核心在于：calibrated CI width 比 raw score magnitude 或简单阈值方法能更精准地识别 PRM 不可靠的 step。如果这个区分在实证中不显著，UGCA 的核心贡献就会大打折扣。Proposal 的 ablation 设计覆盖了这些对比（ablation 3 和 4），说明作者意识到了这个威胁，但 idea 层面的风险仍然存在：如果 soft calibrated gating 仅比 hard thresholding 好 0.5-1%，reviewer 会质疑是否值得引入这套机制。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的环节：\n\n(1) **CI width ↔ PRM prediction reliability 的相关性假设**。这是整个方法的基石。Quantile regression 产生的 CI width 衡量的是 PRM 对 \"该 step 后续能否导向正确答案\" 的预测不确定性，但这不一定等价于 \"PRM 的 step-level 评估是否准确\"。一个 PRM 可能对某类 step 系统性地给出窄 CI 但偏差很大（confident but wrong），也可能给出宽 CI 但方向正确。Proposal 设计了 core assumption validation（per-step w_i quantile bins vs. PRM accuracy），但这是实验层面的验证，idea 层面这个假设是核心弱点。\n\n(2) **Frozen PRM 在 policy drift 下保持 calibration 的假设**。随着 RL training 推进，policy 生成的 rollout 分布会偏离 PRM 训练数据分布。PRM 的 calibration quality 可能因此退化。Proposal 设计了 longitudinal tracking（每 25% 进度检查 ECE/Brier score），但这只是诊断而非修复。如果退化显著，整个 gating 机制的基础就动摇了。\n\n(3) **Bias-variance framing 的严格性**。将 outcome credit 称为 \"unbiased\" 是一个简化——GRPO 的 group-relative advantage 在有限 sample 下也存在 sampling bias。将 process credit 的 \"bias\" 完全归因于 PRM miscalibration 也忽略了 min-form 本身的 structural bias（proposal 承认了这一点但声称不解决它）。sigmoid gating 的 MSE-optimal 推导依赖 Gaussian noise 假设，实际 PRM 误差分布可能远非 Gaussian。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 具体组合（per-step PRM calibrated CI width → sigmoid gating → process-outcome credit interpolation）在现有文献中确实未被占据，2×2 design space 定位清晰。但核心 insight——\"当 verifier 不确定时少信任它\"——是高度直觉性的，conceptual leap 较小。与 PROGRS 的差异是 \"trajectory-level → per-step\"，与 \"Discovering Process-Outcome Credit\" 的差异是 \"MC information gain → calibrated CI width\"。两者都是沿已有维度的渐进延伸，而非开辟新维度。Park et al. (NeurIPS 2025) 的 quantile regression 方法被直接复用而非改进。sigmoid gating 函数虽有理论推导（Gaussian 假设下 MSE-optimal），但形式上是标准的 soft interpolation。\n\n2. **Significance: 中偏强** — 研究问题确实重要：PRM miscalibration 导致 reward hacking 是 math reasoning RL 的核心痛点（\"Reward Under Attack\" 给出了触目惊心的数据），且整个 process-supervised RL 领域正在快速发展。UGCA 提出的 \"Verifier-Uncertainty-Aware RL\" 原则有一定的 generalizable insight（适用于任何 imperfect step-level verifier），这比纯技术改进有更大的影响力。但 proposal 明确将实验 scope 限制在 math reasoning，cross-domain generalization 留作 future work，这限制了即时的 significance。此外，如果核心 positive result 成立（per-step uncertainty gating 比 trajectory-level centering 更好），reviewer 的反应更可能是 \"makes sense, expected\" 而非 \"surprising\"。\n\n3. **Related Work: 强** — 这是 proposal 最突出的优点。2×2 design space taxonomy 是优秀的 positioning 工具。对 ~20 篇高度相关工作的覆盖非常全面，包括 NeurIPS 2025、ICLR 2026、ICML 2025 的最新工作。与每篇工作的差异化定位清晰且准确（我通过调研验证了引用的准确性）。对 PROGRS、\"Discovering Process-Outcome Credit\"、UCAS、ConfClip 等最直接竞争者的技术区分是精准的。唯一小缺陷：未提及 \"From Reasoning to Agentic: Credit Assignment in RL for LLMs\" (arXiv 2604.09459, 2026) 这篇综述，以及 \"Reducing Credit Assignment Variance via Counterfactual Reasoning Paths\" (arXiv 2605.16302, 2026) 这篇 per-step credit 工作，但这不影响核心 positioning。\n\n\n【概率估计】: [28% - 38%] 中位 32%\n\n【估计理由】: \nNovelty 为\"中\"而非\"强\"是概率上界的主要限制因素。核心 insight（trust uncertain verifier signals less）方向高度可预测，conceptual leap 有限，属于 design space 中一个自然但未填充的格点，而非paradigm-level 创新。这意味着即使实验结果 positive，审稿人的反应更可能是 \"well-executed incremental work\" 而非 \"this changes how I think about the problem\"。Significance 中偏强（问题确实重要 + generalization principle 有价值），Related Work 强（positioning exemplary），这两项将概率托住在 28% 以上。但 trivial alternative 威胁真实存在——如果 PROGRS + 简单 per-step filtering 已能获得大部分收益，或者 hard gating 与 soft gating 差距不大，核心贡献的增量价值就会被压缩。中位 32% 反映了：idea 方向正确、定位精准、有真实的 novelty delta，但 delta 的量级可能不足以让 top venue reviewer 写出 \"strong accept\"。\n\n【主要风险】: \n1. **Novelty 被认为 incremental**：reviewer 可能认为 \"从 trajectory-level calibration (PROGRS) 到 per-step calibration\" 只是 granularity 的自然细化，不构成足够的 intellectual contribution；核心 gating 机制（sigmoid on CI width）过于 straightforward。\n2. **Core assumption fragility**：CI width 与 PRM prediction reliability 的相关性假设如果在实验中不强（如 Spearman 相关 < 0.3），整个方法的理论基础就会瓦解——而这个假设在 idea 层面缺乏先验保证，完全依赖实证验证。\n```\n\nSources:\n- [PURE: Stop Summation (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)\n- [PROGRS: LLM Reasoning with Process Rewards (arXiv 2604.02341)](https://arxiv.org/abs/2604.02341)\n- [Discovering Process-Outcome Credit (arXiv 2602.01034)](https://arxiv.org/abs/2602.01034)\n- [Know What You Don't Know: PRM Calibration (Park et al., NeurIPS 2025)](https://openreview.net/forum?id=hzMkfIrdDT)\n- [Distributional Process Reward Models (arXiv 2605.06785)](https://arxiv.org/abs/2605.06785)\n- [GRPO-λ (ICLR 2026)](https://openreview.net/forum?id=iRWqcnBlLQ)\n- [UCAS: Uncertainty-aware Advantage Shaping](https://arxiv.org/abs/2510.10649)\n- [ConfClip (arXiv 2509.17730)](https://arxiv.org/abs/2509.17730)\n- [Reward Under Attack (arXiv 2603.06621)](https://arxiv.org/pdf/2603.06621)\n- [Jia et al., ICML 2025: Do We Need to Verify Step by Step?](https://icml.cc/virtual/2025/poster/46497)\n- [From Reasoning to Agentic: Credit Assignment Survey (arXiv 2604.09459)](https://arxiv.org/html/2604.09459v1)\n- [Reducing Credit Assignment Variance (arXiv 2605.16302)](https://arxiv.org/html/2605.16302)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL\n\n## Core Problem\n\nProcess-aware RL methods (PURE, GRPO-λ, PRL, PRPO, PROGRS) treat PRM step-level scores as equally trustworthy or apply only trajectory-level corrections, yet PRMs are demonstrably miscalibrated—overestimating success on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals. Two distinct bias sources compound this problem: (a) PRM miscalibration bias—PRM scores deviate from true step correctness probabilities, varying in severity across step types (e.g., well-calibrated on computational steps but poorly calibrated on conceptual reasoning); (b) aggregation bias—structural artifacts of the credit assignment form itself (e.g., min-form's conservative lower-bound effect). Existing methods address neither bias source adaptively at the per-step level. The per-step heterogeneity of PRM calibration quality means that global or trajectory-level corrections cannot fully resolve (a)—adaptive per-step treatment is necessary.\n\n## Research Opportunity\n\nPRM calibration methods have matured rapidly (quantile regression [Park et al., NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling. PROGRS (arXiv Apr 2026) brings a calibrated PRM into RL training but applies trajectory-level outcome-conditioned centering—a deterministic rule that does not use per-step uncertainty information. No work uses PRM per-step calibration confidence to adaptively gate credit assignment during RL training. Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision, ensuring fallback to outcome credit preserves learning guarantees. This frames a principled bias-variance tradeoff: process credit provides low-variance but potentially biased (when PRM is miscalibrated) signal; outcome credit is unbiased but high-variance (sparse, trajectory-level). The optimal per-step interpolation depends on local PRM reliability—precisely what calibrated confidence intervals quantify.\n\n## Research Landscape\n\nWe organize the design space along two axes—**signal source** (what drives credit allocation) and **granularity** (per-step vs. trajectory-level)—yielding four quadrants:\n\n| | Per-step | Trajectory-level |\n|---|---|---|\n| **Verifier calibration** | **UGCA (ours)** | PROGRS |\n| **Intrinsic / structural** | Process-Outcome Credit (arXiv 2602.01034) | GRPO, DAPO |\n\n**Process-aware RL (uniform PRM trust).** PURE (NeurIPS 2025) replaces summation-form with min-form credit assignment (82.6% MATH-500, 82.5% AMC23 on Qwen2.5-Math-7B) but assumes PRM scores are reliable. GRPO-λ (arXiv 2510.00194, ICLR 2026) adds eligibility traces to GRPO, improving math scores by 3–4.5 points on 7B models but trusts PRM outputs uniformly. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) using fixed structural alignment. PRL (arXiv 2026) improves reasoning through process reward learning without conditioning on PRM reliability. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals.\n\n**Calibrated PRM in RL (trajectory-level).** PROGRS (arXiv 2604.02341, Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% MATH-500 vs 69.7% DAPO), shifting incorrect-trajectory PRM scores to zero mean within each prompt group. This addresses systematic PRM bias at trajectory level but does not use per-step uncertainty information—all steps within a trajectory receive the same centering treatment regardless of individual calibration quality.\n\n**Per-step process-outcome mixing (non-uncertainty-based).** \"Discovering Process-Outcome Credit\" (arXiv 2602.01034) proposes Step-wise Marginal Information Gain + Decoupled Masking for per-step process-outcome credit mixing via Monte Carlo estimation of intrinsic information gain—computationally heavier (requiring additional MC rollouts) and subject to higher estimation variance than calibration-derived uncertainty. VPPO / \"Save the Good Prefix\" (arXiv 2601.18984) uses PRM to localize the first error step and applies binary prefix reward + suffix penalty—a degenerate (hard) form of per-step gating that cannot gracefully handle PRM uncertainty on ambiguous steps.\n\n**Implicit process credit in GRPO.** Sullivan et al. (arXiv 2509.21154, ICLR 2026) prove GRPO + ORM under shared-prefix conditions is equivalent to PRM-aware RL with a Monte-Carlo-based implicit PRM. This implies vanilla GRPO already carries implicit process credit, but this credit is uniform across steps—not adaptive to PRM confidence. UGCA provides the missing per-step adaptivity.\n\n**Confidence-based reward modulation.** UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty. ConfClip (arXiv 2509.17730) uses policy model confidence to weight rewards in RLVR. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement for reward modulation in general RLHF. All three use policy-side or ensemble-based uncertainty signals that shift with training, whereas UGCA uses an external frozen verifier's calibrated uncertainty—stable, independent of policy training dynamics, and specifically designed to interpolate between process and outcome credit sources rather than simply scaling rewards.\n\n**PRM calibration.** Park et al. (NeurIPS 2025) introduce quantile-regression calibration for PRMs. Distributional PRM (arXiv 2605.06785, May 2026) achieves state-of-the-art calibration via conditional optimal transport, targeting only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL. TP-GRPO (arXiv Jul 2025) uses generative PRM at the thought level with intrinsic signals, not PRM calibration.\n\n**PRM vulnerability.** \"Reward Under Attack\" (arXiv 2603.06621) demonstrates PRMs are systematically exploitable as \"fluency detectors\"—achieving PRM scores >0.9 while ground-truth accuracy <4% under adversarial RL optimization—directly motivating uncertainty-aware trust in PRM signals.\n\n**Gap.** The specific combination—per-step PRM calibration confidence driving adaptive process-outcome credit interpolation during RL training, framed as an uncertainty-driven bias-variance tradeoff—remains unaddressed.\n\n## Proposed Approach\n\nUGCA frames credit assignment as a per-step bias-variance tradeoff. Process credit (PURE-style min-form advantage A^min) provides dense, low-variance signal but inherits PRM miscalibration bias—distinct from the structural aggregation bias of min-form itself, which UGCA does not claim to resolve. Outcome credit (GRPO group-relative advantage A^GRPO) is unbiased (based on verifiable correctness) but high-variance (sparse, trajectory-level). The key insight is separating what the verifier predicts (PRM score) from how confident the verifier is (calibrated confidence interval width)—the former determines the reward signal, the latter determines how much to trust it.\n\nWe equip the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting open-source code from Park et al., NeurIPS 2025), then define a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. The advantage at step i is A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i: high-confidence PRM steps (small w_i, high α) lean on low-variance process credit; uncertain steps (large w_i, low α) gracefully degrade to unbiased outcome credit.\n\n**Why not simpler alternatives?** (1) Using raw PRM score magnitude as gating signal conflates \"the PRM thinks this step is correct\" with \"the PRM is confident about this step\"—a PRM can produce narrow, high-confidence intervals around a wrong prediction. Calibrated CI width separates prediction from confidence. (2) Global clipping/truncation of low-confidence PRM scores discards useful information on partially confident steps. (3) PROGRS's trajectory-level centering treats all steps within a trajectory uniformly despite heterogeneous per-step calibration quality.\n\n**Theoretical grounding.** (1) Jia et al. (ICML 2025) prove outcome supervision is statistically no harder than process supervision, ensuring degradation to outcome credit preserves learning guarantees. (2) Under simplifying assumptions (Gaussian noise on PRM scores with variance proportional to w_i²), the MSE-optimal interpolation weight takes a sigmoid-like form in w_i (formal derivation in appendix), providing a prescriptive justification for the gating function form.\n\n## Experimental Design\n\n**Models.** Qwen3-8B and Qwen3-1.7B, trained on MATH training set (8K prompts) using modified GRPO objective atop PURE codebase with veRL framework. Calibrated PRM frozen throughout.\n\n**Baselines.** 8B: GRPO, DAPO, PURE, GRPO-λ, PROGRS (5 baselines). 1.7B: all 8B baselines + PRPO + VPPO (7 baselines), providing complete coverage of fixed process-outcome mixing strategies (PRPO: parametric shift; VPPO: binary first-error gating).\n\n**Benchmarks.** MATH-500, AMC23, AIME 2024, AIME 2025, OlympiadBench, MinervaMath. Pass@1 as primary metric; Pass@8 on AIME benchmarks to increase statistical power (30-problem sets).\n\n**Reward hacking quantification.**\n- PRM-Accuracy Gap (PAG): periodic rollout sampling during training, plotting mean PRM score vs. ground-truth pass rate as overoptimization curves.\n- Per-step uncertainty-conditioned accuracy: steps binned by w_i into 5 quantile bins, reporting per-bin step correctness.\n- Reward hacking rate: proportion of trajectories where PRM score > threshold but final answer incorrect.\n\n**Core assumption validation.** Per-step w_i quantile bins with PRM step-level prediction accuracy (not just policy correctness): if narrow-w_i bins show higher PRM accuracy, the core assumption (CI width proxies PRM reliability) is confirmed. Report Spearman rank correlation between w_i and PRM prediction error.\n\n**Longitudinal PRM calibration tracking.** At every 25% training progress checkpoint, compute ECE and Brier score of frozen PRM on freshly sampled rollouts. Plot calibration quality vs. training progress and gating coefficient α distribution drift. If significant degradation detected, discuss periodic re-calibration as mitigation.\n\n**Cross-family PRM validation.** ECE and Brier score of calibrated Qwen2.5-Math-PRM-7B on Qwen3-8B initial rollouts vs. Qwen2.5 rollouts. If significant degradation, perform additional quantile calibration fine-tuning on Qwen3 data.\n\n**Ablation studies (Qwen3-1.7B, 3 seeds each).**\n- Boundary cases: α≡1 (pure PURE) and α≡0 (pure GRPO).\n- Hard vs. soft gating: binary threshold (α∈{0,1}) vs. sigmoid.\n- Raw PRM score gating: α_i = σ(PRM_score_i) vs. calibrated CI width gating.\n- Calibrated vs. uncalibrated: raw PRM score variance as uncertainty proxy vs. calibrated CI width.\n- Hyperparameters: threshold τ, temperature β, quantile level.\n\n**Statistical rigor.** 1.7B: 3 seeds, mean ± std. 8B: top 2 configs × 3 seeds + evaluation-level bootstrap CIs (1000 resamples).\n\n**Compute fairness.** Per-method training wall-clock time and FLOPs. PRM calibration cost as separate one-time overhead. Accuracy-vs-compute Pareto curves. Theoretical FLOPs comparison with \"Discovering Process-Outcome Credit\" (arXiv 2602.01034) to justify not running as direct baseline (MC estimation overhead makes compute-normalized comparison unfavorable).\n\n## Broader Significance\n\nUGCA instantiates a general principle—Verifier-Uncertainty-Aware RL: when training with imperfect verifiers, credit assignment should adapt to per-instance verifier confidence. Math reasoning is a clean testbed where PRM uncertainty is measurable and calibratable. The framework generalizes to any domain with imperfect step-level verifiers (code generation, scientific reasoning, agentic tasks). We scope experiments to math reasoning and leave cross-domain validation as future work.\n\n## Key References\n\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)\n- GRPO-λ / GRPO is Secretly a Process Reward Model (arXiv 2510.00194 / arXiv 2509.21154, ICLR 2026)\n- LLM Reasoning with Process Rewards for Outcome-Guided Steps [PROGRS] (arXiv 2604.02341, 2026)\n- Discovering Process-Outcome Credit in Multi-Step LLM Reasoning (arXiv 2602.01034, 2026)\n- Save the Good Prefix: Precise Error Penalization via Process-Supervised RL [VPPO] (arXiv 2601.18984, 2026)\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (Park et al., NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv 2605.06785, 2026)\n- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (Jia et al., ICML 2025)\n- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping [UCAS] (arXiv 2025)\n- ConfClip: Confidence-Weighted and Clipped Reward for RL in LLMs (arXiv 2509.17730, 2025)\n- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)\n- PRL: Process Reward Learning Improves LLMs' Reasoning Ability (arXiv 2026)\n- Error Typing for Smarter Rewards [PathFinder-PRM] (arXiv 2025)\n- Process Reinforcement through Implicit Rewards [PRIME] (arXiv 2025)\n- Uncertainty-Aware Reward Discounting (arXiv Apr 2026)\n- Reward Under Attack: Analyzing Robustness and Hackability of PRMs (arXiv 2603.06621, 2026)\n- DAPO: An Open-Source LLM Reinforcement Learning System at Scale (2025)\n- Good Learners Think Their Thinking [TP-GRPO] (arXiv Jul 2025)\n\n## Resource Estimate\n\n- **GPU compute**: ~2900 H100-hours (PRM quantile calibration: 100h; cross-family validation: 20h; Qwen3-1.7B ablations + baselines ~14 configs × 3 seeds: 840h; Qwen3-8B comparison 6 configs (top 2 × 3 seeds + 4 × 1 seed): 1600h; PROGRS/GRPO-λ reproduction development: 80h; DAPO/PROGRS/extra baseline runs: 200h; evaluation + diagnostics: 60h)\n- **Timeline**: 8 weeks (wk1–2: PRM calibration + cross-family validation + PURE/veRL integration + PROGRS core reproduction; wk3–4: 1.7B full ablation sweep + PRPO/VPPO baselines + core assumption validation; wk5–6: 8B runs vs all baselines + longitudinal calibration tracking; wk7: reward-hacking analysis, PAG curves, Pareto curves, per-step visualization; wk8: paper writing and submission)\n- **Estimated GPU cost**: ~$7,250 (H100 spot ~$2.50/hr)"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T08:55:12.425Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:55:12.425Z",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T08:55:12.437Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:
- [PURE / "Stop Summation: Min-Form Credit Assignment"](https://arxiv.org/abs/2504.15275) (NeurIPS 2025): 提出 min-form credit assignment 替代 summation-form，显著缓解 PRM reward hacking，在 Qwen2.5-Math-7B 上 MATH-500 达 82.6%。是本 proposal 的直接基础之一（提供 A^min 组件）。
- [PROGRS / "LLM Reasoning with Process Rewards for Outcome-Guided Steps"](https://arxiv.org/abs/2604.02341) (arXiv Apr 2026): 使用 frozen quantile-regression PRM + outcome-conditioned centering，在 trajectory 级别校正 PRM bias（MATH-500 74.9% vs DAPO 69.7%）。**这是本 proposal 最近的竞争对手**——同样使用 calibrated PRM，但只做 trajectory-level correction，不做 per-step uncertainty gating。
- [GRPO-λ](https://arxiv.org/abs/2510.00194) (ICLR 2026): 用 eligibility traces 改进 GRPO 的 credit assignment，7B 模型平均提升 3-4.5 分。信任 PRM 输出是 uniform 的。
- [Park et al. / "Know What You Don't Know"](https://arxiv.org/abs/2506.09338) (NeurIPS 2025): 提出 quantile regression 校准 PRM 置信度，产生校准后的 confidence intervals。**核心发现：PRM 系统性过估成功概率。** 仅应用于 test-time scaling，未用于 RL training。这是本 proposal 的另一个直接基础（提供 CI width 信号）。
- ["Discovering Process-Outcome Credit in Multi-Step LLM Reasoning"](https://arxiv.org/abs/2602.01034) (arXiv Feb 2026): 提出 Step-wise Marginal Information Gain + Decoupled Masking 做 per-step process-outcome credit mixing。**概念上与本 proposal 最相近**——也是 per-step 级别的 process-outcome 混合，但使用 Monte Carlo 内在信息增益信号而非 PRM 校准置信度。
- [UCAS / "Unlocking Exploration in RLVR"](https://openreview.net/forum?id=CTmu1mqDuz) (arXiv 2025): 使用 policy model 自身 logit uncertainty 做 advantage shaping。与本 proposal 的区别：UCAS 用 policy-side uncertainty（随训练漂移），UGCA 用 external frozen PRM uncertainty（稳定）。
- [VPPO / "Save the Good Prefix"](https://arxiv.org/abs/2601.18984) (arXiv Jan 2026): 用 PRM 定位首个错误步，施加 binary prefix reward + suffix penalty。是 per-step gating 的退化（hard）形式。
- ["Reward Under Attack"](https://arxiv.org/abs/2603.06621) (arXiv Mar 2026): 证明 PRM 在 adversarial RL 优化下可被系统性利用为"fluency detectors"——PRM score >0.9 但 ground-truth accuracy <4%。直接为 uncertainty-aware PRM trust 提供动机。
- [Distributional PRM](https://arxiv.org/abs/2605.06785) (arXiv May 2026): 通过 conditional optimal transport 达到 SOTA 校准水平，同样仅面向 test-time scaling。

**调研总结**: Process-supervised RL for math reasoning 是一个极度拥挤的赛道（2025-2026 年涌现大量工作）。PRM 校准技术已成熟（Park et al., Distributional PRM），但目前仅用于 test-time scaling；PROGRS 首次将 calibrated PRM 引入 RL training 但仅做 trajectory-level 校正。Per-step process-outcome mixing 已有工作（"Discovering Process-Outcome Credit"）但使用 MC 信息增益而非 PRM 校准置信度。本 proposal 定位在"per-step × verifier calibration"象限，这个具体交叉点确实空白。

【Trivial Alternative 检验】:
存在若干更简单的替代方案，proposal 已部分预见并尝试辩护：
1. **用 raw PRM score magnitude 作为 gating 信号**（而非 CI width）: Proposal 辩称 score ≠ confidence（PRM 可对错误预测产生窄区间、高置信），这个论点合理但需要实证。若实验中 raw score gating 与 CI width gating 差距不大，则核心 novelty 大打折扣。
2. **直接对低置信步骤施加 global clipping/truncation**: 这是一个更简单的 baseline，proposal 辩称会丢失 partially confident 步骤的信息，但 clipping 的损失有多大是未知的。
3. **PROGRS trajectory-level centering + PURE min-form**: 不需要 per-step gating，直接组合两者。这可能是最 threatening 的 trivial alternative——如果 trajectory-level 校正已经足够好，per-step 的增量价值可能很小。

**增量价值的关键依赖**: 必须证明 per-step 异质性确实显著（即同一 trajectory 内不同步骤的 PRM 校准质量差异足够大，使得 trajectory-level 处理不够用）。这是一个合理但未经验证的前提。

【前提假设检验】:
核心 claim 的逻辑链条中有以下未验证环节：
1. **CI width ↔ PRM reliability（核心假设）**: 校准后 CI 宽度确实代理 PRM 逐步预测可靠性。这是整个方法的基石。Proposal 设计了验证实验（w_i quantile bins vs. PRM accuracy），但如果这个相关性不强，整个方法就失去了基础。需要注意：quantile regression 校准的是 success probability 的置信区间，不是 PRM "对不对"的置信——这两者有微妙区别。
2. **Frozen PRM 校准在 policy drift 下保持有效**: PRM 是在初始 rollouts 上校准的，但随着 RL 训练推进，policy 生成的 reasoning 分布会发生漂移。Proposal 设计了 longitudinal tracking 来监控，但这是一个真实的风险——如果校准退化严重，需要周期性 re-calibration，这会增加复杂度和成本。
3. **Process credit 的 bias 主要来自 PRM miscalibration 而非 structural aggregation**: Proposal 承认 min-form 本身有 structural aggregation bias（UGCA 不声称解决它），但假设 per-step miscalibration bias 是可以通过 gating 解决的主导问题。如果 structural bias 才是主导因素，gating 的效果会有限。

【3 维度打分】:
1. **Novelty: 中** — 具体组合确实是新的：calibrated PRM CI width → per-step process-outcome sigmoid gating → RL training。没有现有工作恰好做这件事。但这本质上是对已有组件的工程组合：PRM 校准（Park et al. NeurIPS 2025）+ per-step credit mixing（概念上与 arXiv 2602.01034 同构，只是换了信号源）+ min-form credit（PURE）+ GRPO。智识贡献在于 bias-variance tradeoff framing，这是优雅的但不是 surprising 的——"当 verifier 不确定时少信任它"是一个直觉上 obvious 的策略。相对于 PROGRS 的增量是 trajectory-level → per-step（粒度提升），相对于 "Discovering Process-Outcome Credit" 的增量是 MC information gain → calibrated CI width（信号源替换，更高效但概念上类似）。两个增量都是 meaningful 但都不是 surprising。

2. **Significance: 中** — 问题本身（PRM miscalibration 导致 reward hacking）是真实且重要的，"Reward Under Attack"（arXiv 2603.06621）提供了强有力的动机。"Verifier-Uncertainty-Aware RL" 的一般化框架有潜在的广泛适用性。但实际影响力受限于：(a) math reasoning RL 赛道极度拥挤，每几周就有新方法出现，单个方法的影响力被稀释；(b) 核心发现如果是 positive（"per-step uncertainty gating 比 trajectory-level centering 好几个点"），审稿人很可能的反应是 "makes sense, nice result" 而非 "surprising, I wouldn't have guessed this"——因为 per-step 优于 trajectory-level 在直觉上是预期内的；(c) 如果是 negative（效果不显著），论文的贡献就退化为一个 negative result + analysis paper。

3. **Related Work: 强** — 这是本 proposal 最突出的优点。文献覆盖全面且准确：2×2 positioning matrix（signal source × granularity）清晰地定位了 UGCA 的位置。对 UCAS、ConfClip、PROGRS、"Discovering Process-Outcome Credit"、VPPO 等竞争工作的差异化分析具体且有说服力。引用的论文经核实真实存在且描述准确（PURE NeurIPS 2025 ✓、Park et al. NeurIPS 2025 ✓、PROGRS arXiv 2604.02341 ✓、Reward Under Attack arXiv 2603.06621 ✓）。Jia et al. (ICML 2025) 提供的理论 backing 被恰当引用。

【概率估计】: [25% - 35%] 中位 28%

【估计理由】: Related Work 维度强，说明作者对领域有深入理解且定位清晰——这保证了 proposal 的下限。Novelty 和 Significance 都是"中"：核心组合确实是新的（gap 真实存在），但 intellectual surprise 有限——"用 PRM 置信度做 per-step gating"是一个 natural next step，审稿人不太可能感到 surprised。上界主要被 **Novelty** 限制：在一个极度拥挤的赛道上，一个 "natural combination of existing components" 的工作很难超过 35%，即使执行完美。下界由 Related Work 的扎实程度和 gap 的真实性托住，不会低于 25%。

【主要风险】:
1. **"Obvious next step" 感知风险**: 审稿人可能认为将 PRM 校准从 test-time 拓展到 training-time、从 trajectory-level 细化到 per-step 是一个工程上自然的演进，缺乏足够的 intellectual depth 或 surprising insight。在 math reasoning RL 这个过度拥挤的赛道上，这种 perception 对中稿概率杀伤力很大。
2. **核心假设脆弱性**: CI width ↔ PRM per-step reliability 的相关性如果不够强（或者在 policy drift 下快速退化），整个方法的理论基础就会动摇。更危险的是，如果 ablation 中 raw PRM score gating 效果接近 CI width gating，则 calibration 这一核心技术贡献的增量价值就被严重削弱。
```

Sources:
- [PURE - Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)
- [PROGRS - LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341)
- [GRPO-λ: Credit Assignment improves LLM Reasoning](https://arxiv.org/abs/2510.00194)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)
- [UCAS - Unlocking Exploration in RLVR](https://openreview.net/forum?id=CTmu1mqDuz)
- [VPPO - Save the Good Prefix](https://arxiv.org/abs/2601.18984)
- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)
- [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- Park et al., "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (NeurIPS 2025): 提出 PRM 的 quantile regression 校准方法，产出逐步置信区间，但仅用于 test-time scaling，未用于 RL 训练。UGCA 的 CI width 计算直接依赖此工作的开源代码。
- PROGRS / "LLM Reasoning with Process Rewards for Outcome-Guided Steps" (arXiv 2604.02341, 2026): 将校准过的 PRM（frozen quantile-regression PRM）引入 RL 训练，但采用 trajectory-level outcome-conditioned centering——同一 trajectory 内所有 step 接受相同的 centering 处理。MATH-500 上 74.9% vs DAPO 69.7%。这是 UGCA 最直接的上游竞争者，UGCA 的核心增量在于从 trajectory-level 升级到 per-step。
- PURE / "Stop Summation" (NeurIPS 2025): 提出 min-form credit assignment，缓解 reward hacking，MATH-500 82.6%。UGCA 的 process credit 分支直接采用 PURE 的 min-form advantage。
- "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning" (arXiv 2602.01034, 2026): 通过 Monte Carlo estimation 的 Step-wise Marginal Information Gain 实现 per-step process-outcome credit mixing。与 UGCA 在 per-step 粒度上直接竞争，但使用 intrinsic information gain 而非外部校准不确定性作为 gating 信号。计算成本更高（需额外 MC rollouts）。
- SSVPO (ICLR 2026): 基于 Sequential Shapley Values 的 step-level credit assignment，7 个 benchmark 上显著优于 GRPO/DAPO/VinePPO 等，精度提升达 11.6%。这是 per-step credit assignment 的另一条强竞争路线，proposal 中未提及。
- RTMC (arXiv 2604.11037, Apr 2026): 利用 rollout tree 实现 per-step Q-value estimation，无需 learned critic。也是 per-step credit 的竞争方法，proposal 中未提及。
- UCAS (arXiv 2510.10649, 2025): 用 policy model 自身的 logit uncertainty 做 advantage shaping。与 UGCA 共享 "uncertainty-aware credit" 的 high-level idea，但 uncertainty source 不同（policy-side vs. external PRM calibration）。
- Jia et al., "Do We Need to Verify Step by Step?" (ICML 2025): 证明 outcome supervision 统计上不难于 process supervision，为 UGCA 的 fallback-to-outcome-credit 提供理论保障。
- "Reward Under Attack" (arXiv 2603.06621, 2026): 证明 PRM 可被 adversarially exploit（PRM score >0.9 但 ground-truth accuracy <4%），直接 motivate uncertainty-aware 的 PRM 使用方式。
- Distributional PRM (arXiv 2605.06785, May 2026): 通过 conditional optimal transport 实现 SOTA PRM 校准，但仅用于 test-time。
- SPRO / Self-Guided Process Reward Optimization (2025): 从 policy model 自身派生 process rewards，不依赖外部 PRM。
- PROF-GRPO / Blend-PRM-GRPO (2025): 以固定权重混合 PRM 与 outcome rewards，非自适应。

- 调研总结: 2025-2026 年 process-aware RL for math reasoning 领域极其活跃。Per-step credit assignment 已有多条路线（SSVPO-Shapley、RTMC-rollout tree、Process-Outcome Credit-MC info gain、VPPO-binary gating）。PRM 校准技术已成熟（Park et al., Distributional PRM）。PROGRS 首次将校准 PRM 引入 RL 但止步于 trajectory-level。UGCA 的定位是"用校准 PRM 的 per-step CI width 做自适应 process-outcome 插值"，这个具体组合确实未被占据，但它是将现有成熟组件（校准 PRM + min-form credit + GRPO）用一个 sigmoid gating 函数拼接而成的组合式贡献。

【Trivial Alternative 检验】:
存在多个 simpler alternatives 构成威胁：
1. **Raw PRM score magnitude 作为 gating**: proposal 本身讨论了此点并给出了"score ≠ confidence"的反驳，但审稿人可能要求 empirical 验证这一区分是否 material（即两者差距有多大）。如果 ablation 显示 raw score gating 与 CI width gating 性能差异微弱，UGCA 的增量价值将大幅缩水。
2. **PROGRS trajectory-level centering 已是强 baseline**: 如果 PROGRS 的 trajectory-level correction 已经捕获了 80%+ 的收益，per-step gating 的 marginal gain 可能不显著。这是最核心的 trivial alternative 威胁——UGCA 必须 empirically 证明 per-step adaptivity 相比 trajectory-level 有 meaningful 的差距。
3. **简单 per-step hard thresholding**（CI width 超过阈值就完全 fallback to outcome credit）：如果与 soft sigmoid gating 差异不大，则 sigmoid 形式的理论推导变得 cosmetic。
4. **SSVPO / RTMC 等不依赖 PRM 的 per-step credit 方法**: 如果这些方法在不使用 PRM 的情况下就能实现 comparable 的 per-step credit assignment，UGCA 依赖外部 PRM + 校准的路线就显得 over-engineered。

增量价值关键取决于: per-step PRM calibration confidence 是否比 trajectory-level correction 或非 PRM-based per-step 方法提供 meaningful 的额外信号。这一点目前是假设，尚未验证。

【前提假设检验】:
核心 claim 的逻辑链存在以下未验证环节：

1. **CI width 是 PRM reliability 的良好 proxy**（关键假设）: proposal 假设"校准后的置信区间宽度越大 → PRM 在该 step 上越不可靠"。但 quantile regression 校准的目标是让 CI 覆盖率符合名义覆盖率（如 80% CI 实际覆盖 80% 的真实值），这并不直接等价于"CI 宽 → prediction error 大"。宽 CI 可能反映 inherent aleatoric uncertainty（步骤本身有多种合理做法）而非 PRM epistemic failure。proposal 计划了 Spearman correlation 验证，但如果相关性弱，整个方法就失去根基。

2. **Cross-family PRM 校准迁移假设**: Qwen2.5-Math-PRM-7B 在 Qwen3 系列模型的 rollouts 上仍然保持良好校准。Proposal 承认了这一风险并计划验证，但如果校准严重退化，CI width 的信息量将大幅下降。

3. **Frozen PRM 校准在 policy drift 下的稳定性**: RL 训练改变 policy 的输出分布，frozen PRM 的校准可能随训练进行而退化。Proposal 计划了纵向校准追踪（每 25% checkpoint），但未提出明确的 re-calibration 机制——仅说"discuss periodic re-calibration as mitigation"。

4. **Gaussian 噪声假设下的最优插值推导**: sigmoid 形式的 gating function 来自"PRM score noise 方差正比于 w_i²"的简化假设。实际 PRM 误差分布可能远非 Gaussian，推导的 prescriptive 价值有限。

5. **Process credit = low-variance, outcome credit = unbiased 的二分法过于简化**: 实际中 GRPO 的 group-relative advantage 并非完全"unbiased"（取决于 group 内 sample diversity），PURE 的 min-form advantage 的 bias 来源不仅是 PRM miscalibration 还有 min-form 本身的 structural bias（proposal 承认了这一点但声称不解决）。

【3 维度打分】:

1. Novelty: 中 — 
   UGCA 填补的具体 gap（per-step PRM calibration confidence → adaptive process-outcome credit interpolation）确实未被现有工作占据。但这是一个 **组合式贡献**：将三个已有成熟组件（Park et al. 的 quantile calibration、PURE 的 min-form credit、GRPO 的 outcome credit）用一个 sigmoid gating 函数拼接。核心技术贡献本质上是一个 gating equation（α_i = σ(−(w_i − τ)/β)）。与 "Discovering Process-Outcome Credit"(arXiv 2602.01034) 相比，UGCA 用 external calibrated uncertainty 替代 intrinsic information gain 做 per-step gating，这是一个 design choice 的差异，不是 paradigm 级别的创新。proposal 未引用 SSVPO (ICLR 2026) 和 RTMC (Apr 2026) 两个直接竞争的 per-step credit assignment 工作，这些方法无需 PRM 校准即可实现自适应 per-step credit，对 UGCA 的必要性构成挑战。bias-variance tradeoff 的理论 framing 是加分项，但在简化假设下的推导其 prescriptive 价值有限。

2. Significance: 中 — 
   研究问题（PRM miscalibration 导致 reward hacking）确实重要且 timely，"Reward Under Attack" (arXiv 2603.06621) 的发现直接 motivate 了这一方向。但 significance 受限于：(a) 如果 marginal gain over PROGRS 不显著，实际影响有限；(b) 方法仅在 math reasoning 上验证，跨领域泛化为 future work；(c) "Verifier-Uncertainty-Aware RL" 的 broader principle 虽有价值，但当前 instantiation 过于 narrow（单一 PRM、单一 domain）来支撑这个宏大叙事。若核心实验发现 positive（per-step gating 显著优于 PROGRS），审稿人可能的反应更接近 "makes sense, reasonable engineering" 而非 "surprising"。

3. Related Work: 中偏强 — 
   Related work 覆盖面广、组织清晰（2×2 design space table 很好）。对 PROGRS、PURE、Process-Outcome Credit、UCAS、ConfClip、VPPO 等均有准确定位。但存在重要遗漏：(a) **SSVPO** (ICLR 2026) 是 step-level credit assignment 的重要竞争工作（11.6% accuracy gain over GRPO），完全未提及；(b) **RTMC** (Apr 2026) 是另一条 per-step credit 路线，未提及；(c) **SPRO** (2025) 和 **PROF-GRPO/Blend** 等 process-outcome mixing 方法未充分讨论。这些遗漏意味着 proposal 的 "gap" 叙事可能面临审稿人质疑——"per-step credit 已有多条不依赖 PRM 校准的路线，为什么你的方法必要？"

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Novelty 是主要限制因素。核心贡献是一个 well-motivated 但 incremental 的组合：用现成的校准 CI width 做 sigmoid gating 来插值两种已有 credit assignment 方式。idea 的 "surprising quotient" 低——一旦知道 PRM 有校准不确定性信息，"用它来 gate credit assignment" 是 most obvious next step。Significance 取决于 marginal gain 的大小（这是 empirical 问题），但 idea 本身的 ceiling 受限于组合性质。Related work 覆盖较好但有关键遗漏（SSVPO, RTMC），可能导致 novelty claim 被削弱。

上界受限于 Novelty（组合式贡献 + 核心技术薄）和 trivial alternative 威胁（PROGRS trajectory-level 可能已足够好）。下界由 idea 方向的合理性、清晰的理论 framing、以及 PRM miscalibration 问题的真实性支撑。

【主要风险】: 
1. **"Incremental combination" 判决**: 审稿人极可能指出 UGCA = Park et al. calibration + PURE min-form + GRPO + sigmoid gating，核心技术贡献仅为一个 gating equation，novelty insufficient for a top venue。
2. **Per-step gating 的 marginal value 不明**: 如果 PROGRS 的 trajectory-level centering 已捕获大部分收益，或 SSVPO/RTMC 等非 PRM 路线已提供 comparable per-step credit，则 UGCA 的 raison d'être 被根本削弱。
```

Sources:
- [PROGRS - LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/abs/2604.02341)
- [PURE - Stop Summation: Min-Form Credit Assignment](https://openreview.net/forum?id=3Sxby0hH1q)
- [Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)
- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)
- [SSVPO: Effective Step-Level Credit Assignment](https://openreview.net/forum?id=g33DGvnHYd)
- [RTMC: Step-Level Credit Assignment via Rollout Trees](https://arxiv.org/abs/2604.11037)
- [UCAS: Unlocking Exploration in RLVR](https://arxiv.org/abs/2510.10649)
- [Jia et al. - Do We Need to Verify Step by Step?](https://arxiv.org/abs/2502.10581)
- [Reward Under Attack: Analyzing Robustness of PRMs](https://arxiv.org/abs/2603.06621)
- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)
- [GRPO-λ / GRPO is Secretly a Process Reward Model](https://openreview.net/forum?id=CTmu1mqDuz)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

- "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning" [PURE] (NeurIPS 2025): 提出 min-form 替代 summation-form credit assignment 以缓解 reward hacking。假设 PRM score 可靠，不做 per-step 可信度区分。本 proposal 的核心 process credit 来源。
  
- "LLM Reasoning with Process Rewards for Outcome-Guided Steps" [PROGRS] (arXiv 2604.02341, 2026): 使用 frozen quantile-regression PRM + outcome-conditioned centering。在 trajectory level 做校准修正（incorrect trajectories 的 PRM scores 归零中心化），MATH-500 达 74.9% vs DAPO 69.7%。是本 proposal 最直接的竞争对手——同样使用 calibrated PRM，但在 trajectory level 而非 per-step level 操作。

- "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning" (arXiv 2602.01034, 2026): 提出 Step-wise Marginal Information Gain + Decoupled Masking 做 per-step process-outcome credit mixing，但基于 Monte Carlo estimation 的 intrinsic information gain，非 PRM calibration confidence。计算开销更大。是 per-step mixing 维度的竞争者，但 signal source 不同。

- "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (Park et al., NeurIPS 2025): 提出 quantile regression 校准 PRM，生成 calibrated confidence intervals。仅用于 test-time scaling（instance-adaptive compute allocation），未将 uncertainty 反馈到 RL training。本 proposal 的技术基座——直接复用其校准方法。

- "Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport" (arXiv 2605.06785, May 2026): PRM 校准的最新 SOTA，同样仅用于 test-time scaling。

- GRPO-λ (arXiv 2510.00194, ICLR 2026): eligibility traces 改善 credit assignment，但均匀信任 PRM outputs。

- UCAS (arXiv 2510.10649, 2025): 用 policy 模型自身 logit uncertainty 做 advantage shaping。信号来源是 policy-side，随训练漂移。

- ConfClip (arXiv 2509.17730, 2025): 用 policy confidence 加权 reward。同样是 policy-side signal。

- "Reward Under Attack" (arXiv 2603.06621, 2026): 证明 PRM 在 adversarial RL 下 systematically exploitable，PRM scores >0.9 而 accuracy <4%。直接支持 proposal 的 motivation。

- Jia et al. "Do We Need to Verify Step by Step?" (ICML 2025): 理论证明 outcome supervision 统计难度不高于 process supervision。为 fallback to outcome credit 提供理论保障。

- VPPO / "Save the Good Prefix" (arXiv 2601.18984, 2026): binary first-error gating，per-step 但 hard threshold。

- "Reducing Credit Assignment Variance via Counterfactual Reasoning Paths" (arXiv 2605.16302, 2026): 用 counterfactual comparison 做 per-step credit，signal source 不同。

- "From Reasoning to Agentic: Credit Assignment in RL for LLMs" (arXiv 2604.09459, 2026): 2024.01–2026.04 credit assignment 综述，覆盖了这个领域的完整 taxonomy。

- 调研总结: 数学推理 RL 中的 credit assignment 是 2025-2026 最活跃的研究方向之一。当前格局沿两轴分化：(1) signal source（verifier calibration vs. intrinsic/structural）和 (2) granularity（per-step vs. trajectory-level）。PROGRS 占据了 "verifier calibration × trajectory-level" 象限；"Discovering Process-Outcome Credit" 占据了 "intrinsic × per-step" 象限。本 proposal 定位于 "verifier calibration × per-step" 象限，这一组合确实未被直接占据。但 PROGRS 的 trajectory-level centering 和 "Discovering Process-Outcome Credit" 的 per-step mixing 各自覆盖了 UGCA 的一个维度。


【Trivial Alternative 检验】:

存在几个成本更低的替代方案需要考量：

(1) **Hard threshold gating**：直接丢弃 CI width 超过阈值的 PRM step（α∈{0,1}），不做 soft sigmoid 插值。这比 soft gating 简单得多，proposal 将其作为 ablation 对照，但如果 hard gating 效果接近，soft gating 的增量 contribution 就很薄。

(2) **PROGRS + 简单 per-step PRM score filtering**：在 PROGRS 的 trajectory-level centering 基础上，对低 confidence 的 step 做简单 clipping（如去掉 bottom 20% confidence 的 step rewards）。这不需要 sigmoid gating 函数、bias-variance framing 等理论构造，但可能捕获大部分收益。

(3) **Raw PRM score magnitude 作为 gating signal**：proposal 认为这混淆了 "prediction" 和 "confidence"，指出 PRM 可以在错误预测上有高 confidence。这是一个有效的区分点，但需要实证验证两者差距有多大。

增量价值的核心在于：calibrated CI width 比 raw score magnitude 或简单阈值方法能更精准地识别 PRM 不可靠的 step。如果这个区分在实证中不显著，UGCA 的核心贡献就会大打折扣。Proposal 的 ablation 设计覆盖了这些对比（ablation 3 和 4），说明作者意识到了这个威胁，但 idea 层面的风险仍然存在：如果 soft calibrated gating 仅比 hard thresholding 好 0.5-1%，reviewer 会质疑是否值得引入这套机制。


【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的环节：

(1) **CI width ↔ PRM prediction reliability 的相关性假设**。这是整个方法的基石。Quantile regression 产生的 CI width 衡量的是 PRM 对 "该 step 后续能否导向正确答案" 的预测不确定性，但这不一定等价于 "PRM 的 step-level 评估是否准确"。一个 PRM 可能对某类 step 系统性地给出窄 CI 但偏差很大（confident but wrong），也可能给出宽 CI 但方向正确。Proposal 设计了 core assumption validation（per-step w_i quantile bins vs. PRM accuracy），但这是实验层面的验证，idea 层面这个假设是核心弱点。

(2) **Frozen PRM 在 policy drift 下保持 calibration 的假设**。随着 RL training 推进，policy 生成的 rollout 分布会偏离 PRM 训练数据分布。PRM 的 calibration quality 可能因此退化。Proposal 设计了 longitudinal tracking（每 25% 进度检查 ECE/Brier score），但这只是诊断而非修复。如果退化显著，整个 gating 机制的基础就动摇了。

(3) **Bias-variance framing 的严格性**。将 outcome credit 称为 "unbiased" 是一个简化——GRPO 的 group-relative advantage 在有限 sample 下也存在 sampling bias。将 process credit 的 "bias" 完全归因于 PRM miscalibration 也忽略了 min-form 本身的 structural bias（proposal 承认了这一点但声称不解决它）。sigmoid gating 的 MSE-optimal 推导依赖 Gaussian noise 假设，实际 PRM 误差分布可能远非 Gaussian。


【3 维度打分】:

1. **Novelty: 中** — 具体组合（per-step PRM calibrated CI width → sigmoid gating → process-outcome credit interpolation）在现有文献中确实未被占据，2×2 design space 定位清晰。但核心 insight——"当 verifier 不确定时少信任它"——是高度直觉性的，conceptual leap 较小。与 PROGRS 的差异是 "trajectory-level → per-step"，与 "Discovering Process-Outcome Credit" 的差异是 "MC information gain → calibrated CI width"。两者都是沿已有维度的渐进延伸，而非开辟新维度。Park et al. (NeurIPS 2025) 的 quantile regression 方法被直接复用而非改进。sigmoid gating 函数虽有理论推导（Gaussian 假设下 MSE-optimal），但形式上是标准的 soft interpolation。

2. **Significance: 中偏强** — 研究问题确实重要：PRM miscalibration 导致 reward hacking 是 math reasoning RL 的核心痛点（"Reward Under Attack" 给出了触目惊心的数据），且整个 process-supervised RL 领域正在快速发展。UGCA 提出的 "Verifier-Uncertainty-Aware RL" 原则有一定的 generalizable insight（适用于任何 imperfect step-level verifier），这比纯技术改进有更大的影响力。但 proposal 明确将实验 scope 限制在 math reasoning，cross-domain generalization 留作 future work，这限制了即时的 significance。此外，如果核心 positive result 成立（per-step uncertainty gating 比 trajectory-level centering 更好），reviewer 的反应更可能是 "makes sense, expected" 而非 "surprising"。

3. **Related Work: 强** — 这是 proposal 最突出的优点。2×2 design space taxonomy 是优秀的 positioning 工具。对 ~20 篇高度相关工作的覆盖非常全面，包括 NeurIPS 2025、ICLR 2026、ICML 2025 的最新工作。与每篇工作的差异化定位清晰且准确（我通过调研验证了引用的准确性）。对 PROGRS、"Discovering Process-Outcome Credit"、UCAS、ConfClip 等最直接竞争者的技术区分是精准的。唯一小缺陷：未提及 "From Reasoning to Agentic: Credit Assignment in RL for LLMs" (arXiv 2604.09459, 2026) 这篇综述，以及 "Reducing Credit Assignment Variance via Counterfactual Reasoning Paths" (arXiv 2605.16302, 2026) 这篇 per-step credit 工作，但这不影响核心 positioning。


【概率估计】: [28% - 38%] 中位 32%

【估计理由】: 
Novelty 为"中"而非"强"是概率上界的主要限制因素。核心 insight（trust uncertain verifier signals less）方向高度可预测，conceptual leap 有限，属于 design space 中一个自然但未填充的格点，而非paradigm-level 创新。这意味着即使实验结果 positive，审稿人的反应更可能是 "well-executed incremental work" 而非 "this changes how I think about the problem"。Significance 中偏强（问题确实重要 + generalization principle 有价值），Related Work 强（positioning exemplary），这两项将概率托住在 28% 以上。但 trivial alternative 威胁真实存在——如果 PROGRS + 简单 per-step filtering 已能获得大部分收益，或者 hard gating 与 soft gating 差距不大，核心贡献的增量价值就会被压缩。中位 32% 反映了：idea 方向正确、定位精准、有真实的 novelty delta，但 delta 的量级可能不足以让 top venue reviewer 写出 "strong accept"。

【主要风险】: 
1. **Novelty 被认为 incremental**：reviewer 可能认为 "从 trajectory-level calibration (PROGRS) 到 per-step calibration" 只是 granularity 的自然细化，不构成足够的 intellectual contribution；核心 gating 机制（sigmoid on CI width）过于 straightforward。
2. **Core assumption fragility**：CI width 与 PRM prediction reliability 的相关性假设如果在实验中不强（如 Spearman 相关 < 0.3），整个方法的理论基础就会瓦解——而这个假设在 idea 层面缺乏先验保证，完全依赖实证验证。
```

Sources:
- [PURE: Stop Summation (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)
- [PROGRS: LLM Reasoning with Process Rewards (arXiv 2604.02341)](https://arxiv.org/abs/2604.02341)
- [Discovering Process-Outcome Credit (arXiv 2602.01034)](https://arxiv.org/abs/2602.01034)
- [Know What You Don't Know: PRM Calibration (Park et al., NeurIPS 2025)](https://openreview.net/forum?id=hzMkfIrdDT)
- [Distributional Process Reward Models (arXiv 2605.06785)](https://arxiv.org/abs/2605.06785)
- [GRPO-λ (ICLR 2026)](https://openreview.net/forum?id=iRWqcnBlLQ)
- [UCAS: Uncertainty-aware Advantage Shaping](https://arxiv.org/abs/2510.10649)
- [ConfClip (arXiv 2509.17730)](https://arxiv.org/abs/2509.17730)
- [Reward Under Attack (arXiv 2603.06621)](https://arxiv.org/pdf/2603.06621)
- [Jia et al., ICML 2025: Do We Need to Verify Step by Step?](https://icml.cc/virtual/2025/poster/46497)
- [From Reasoning to Agentic: Credit Assignment Survey (arXiv 2604.09459)](https://arxiv.org/html/2604.09459v1)
- [Reducing Credit Assignment Variance (arXiv 2605.16302)](https://arxiv.org/html/2605.16302)


【原始 proposal（允许参考但不是主要依据）】:
# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL

## Core Problem

Process-aware RL methods (PURE, GRPO-λ, PRL, PRPO, PROGRS) treat PRM step-level scores as equally trustworthy or apply only trajectory-level corrections, yet PRMs are demonstrably miscalibrated—overestimating success on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals. Two distinct bias sources compound this problem: (a) PRM miscalibration bias—PRM scores deviate from true step correctness probabilities, varying in severity across step types (e.g., well-calibrated on computational steps but poorly calibrated on conceptual reasoning); (b) aggregation bias—structural artifacts of the credit assignment form itself (e.g., min-form's conservative lower-bound effect). Existing methods address neither bias source adaptively at the per-step level. The per-step heterogeneity of PRM calibration quality means that global or trajectory-level corrections cannot fully resolve (a)—adaptive per-step treatment is necessary.

## Research Opportunity

PRM calibration methods have matured rapidly (quantile regression [Park et al., NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling. PROGRS (arXiv Apr 2026) brings a calibrated PRM into RL training but applies trajectory-level outcome-conditioned centering—a deterministic rule that does not use per-step uncertainty information. No work uses PRM per-step calibration confidence to adaptively gate credit assignment during RL training. Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision, ensuring fallback to outcome credit preserves learning guarantees. This frames a principled bias-variance tradeoff: process credit provides low-variance but potentially biased (when PRM is miscalibrated) signal; outcome credit is unbiased but high-variance (sparse, trajectory-level). The optimal per-step interpolation depends on local PRM reliability—precisely what calibrated confidence intervals quantify.

## Research Landscape

We organize the design space along two axes—**signal source** (what drives credit allocation) and **granularity** (per-step vs. trajectory-level)—yielding four quadrants:

| | Per-step | Trajectory-level |
|---|---|---|
| **Verifier calibration** | **UGCA (ours)** | PROGRS |
| **Intrinsic / structural** | Process-Outcome Credit (arXiv 2602.01034) | GRPO, DAPO |

**Process-aware RL (uniform PRM trust).** PURE (NeurIPS 2025) replaces summation-form with min-form credit assignment (82.6% MATH-500, 82.5% AMC23 on Qwen2.5-Math-7B) but assumes PRM scores are reliable. GRPO-λ (arXiv 2510.00194, ICLR 2026) adds eligibility traces to GRPO, improving math scores by 3–4.5 points on 7B models but trusts PRM outputs uniformly. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) using fixed structural alignment. PRL (arXiv 2026) improves reasoning through process reward learning without conditioning on PRM reliability. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals.

**Calibrated PRM in RL (trajectory-level).** PROGRS (arXiv 2604.02341, Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% MATH-500 vs 69.7% DAPO), shifting incorrect-trajectory PRM scores to zero mean within each prompt group. This addresses systematic PRM bias at trajectory level but does not use per-step uncertainty information—all steps within a trajectory receive the same centering treatment regardless of individual calibration quality.

**Per-step process-outcome mixing (non-uncertainty-based).** "Discovering Process-Outcome Credit" (arXiv 2602.01034) proposes Step-wise Marginal Information Gain + Decoupled Masking for per-step process-outcome credit mixing via Monte Carlo estimation of intrinsic information gain—computationally heavier (requiring additional MC rollouts) and subject to higher estimation variance than calibration-derived uncertainty. VPPO / "Save the Good Prefix" (arXiv 2601.18984) uses PRM to localize the first error step and applies binary prefix reward + suffix penalty—a degenerate (hard) form of per-step gating that cannot gracefully handle PRM uncertainty on ambiguous steps.

**Implicit process credit in GRPO.** Sullivan et al. (arXiv 2509.21154, ICLR 2026) prove GRPO + ORM under shared-prefix conditions is equivalent to PRM-aware RL with a Monte-Carlo-based implicit PRM. This implies vanilla GRPO already carries implicit process credit, but this credit is uniform across steps—not adaptive to PRM confidence. UGCA provides the missing per-step adaptivity.

**Confidence-based reward modulation.** UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty. ConfClip (arXiv 2509.17730) uses policy model confidence to weight rewards in RLVR. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement for reward modulation in general RLHF. All three use policy-side or ensemble-based uncertainty signals that shift with training, whereas UGCA uses an external frozen verifier's calibrated uncertainty—stable, independent of policy training dynamics, and specifically designed to interpolate between process and outcome credit sources rather than simply scaling rewards.

**PRM calibration.** Park et al. (NeurIPS 2025) introduce quantile-regression calibration for PRMs. Distributional PRM (arXiv 2605.06785, May 2026) achieves state-of-the-art calibration via conditional optimal transport, targeting only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL. TP-GRPO (arXiv Jul 2025) uses generative PRM at the thought level with intrinsic signals, not PRM calibration.

**PRM vulnerability.** "Reward Under Attack" (arXiv 2603.06621) demonstrates PRMs are systematically exploitable as "fluency detectors"—achieving PRM scores >0.9 while ground-truth accuracy <4% under adversarial RL optimization—directly motivating uncertainty-aware trust in PRM signals.

**Gap.** The specific combination—per-step PRM calibration confidence driving adaptive process-outcome credit interpolation during RL training, framed as an uncertainty-driven bias-variance tradeoff—remains unaddressed.

## Proposed Approach

UGCA frames credit assignment as a per-step bias-variance tradeoff. Process credit (PURE-style min-form advantage A^min) provides dense, low-variance signal but inherits PRM miscalibration bias—distinct from the structural aggregation bias of min-form itself, which UGCA does not claim to resolve. Outcome credit (GRPO group-relative advantage A^GRPO) is unbiased (based on verifiable correctness) but high-variance (sparse, trajectory-level). The key insight is separating what the verifier predicts (PRM score) from how confident the verifier is (calibrated confidence interval width)—the former determines the reward signal, the latter determines how much to trust it.

We equip the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting open-source code from Park et al., NeurIPS 2025), then define a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. The advantage at step i is A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i: high-confidence PRM steps (small w_i, high α) lean on low-variance process credit; uncertain steps (large w_i, low α) gracefully degrade to unbiased outcome credit.

**Why not simpler alternatives?** (1) Using raw PRM score magnitude as gating signal conflates "the PRM thinks this step is correct" with "the PRM is confident about this step"—a PRM can produce narrow, high-confidence intervals around a wrong prediction. Calibrated CI width separates prediction from confidence. (2) Global clipping/truncation of low-confidence PRM scores discards useful information on partially confident steps. (3) PROGRS's trajectory-level centering treats all steps within a trajectory uniformly despite heterogeneous per-step calibration quality.

**Theoretical grounding.** (1) Jia et al. (ICML 2025) prove outcome supervision is statistically no harder than process supervision, ensuring degradation to outcome credit preserves learning guarantees. (2) Under simplifying assumptions (Gaussian noise on PRM scores with variance proportional to w_i²), the MSE-optimal interpolation weight takes a sigmoid-like form in w_i (formal derivation in appendix), providing a prescriptive justification for the gating function form.

## Experimental Design

**Models.** Qwen3-8B and Qwen3-1.7B, trained on MATH training set (8K prompts) using modified GRPO objective atop PURE codebase with veRL framework. Calibrated PRM frozen throughout.

**Baselines.** 8B: GRPO, DAPO, PURE, GRPO-λ, PROGRS (5 baselines). 1.7B: all 8B baselines + PRPO + VPPO (7 baselines), providing complete coverage of fixed process-outcome mixing strategies (PRPO: parametric shift; VPPO: binary first-error gating).

**Benchmarks.** MATH-500, AMC23, AIME 2024, AIME 2025, OlympiadBench, MinervaMath. Pass@1 as primary metric; Pass@8 on AIME benchmarks to increase statistical power (30-problem sets).

**Reward hacking quantification.**
- PRM-Accuracy Gap (PAG): periodic rollout sampling during training, plotting mean PRM score vs. ground-truth pass rate as overoptimization curves.
- Per-step uncertainty-conditioned accuracy: steps binned by w_i into 5 quantile bins, reporting per-bin step correctness.
- Reward hacking rate: proportion of trajectories where PRM score > threshold but final answer incorrect.

**Core assumption validation.** Per-step w_i quantile bins with PRM step-level prediction accuracy (not just policy correctness): if narrow-w_i bins show higher PRM accuracy, the core assumption (CI width proxies PRM reliability) is confirmed. Report Spearman rank correlation between w_i and PRM prediction error.

**Longitudinal PRM calibration tracking.** At every 25% training progress checkpoint, compute ECE and Brier score of frozen PRM on freshly sampled rollouts. Plot calibration quality vs. training progress and gating coefficient α distribution drift. If significant degradation detected, discuss periodic re-calibration as mitigation.

**Cross-family PRM validation.** ECE and Brier score of calibrated Qwen2.5-Math-PRM-7B on Qwen3-8B initial rollouts vs. Qwen2.5 rollouts. If significant degradation, perform additional quantile calibration fine-tuning on Qwen3 data.

**Ablation studies (Qwen3-1.7B, 3 seeds each).**
- Boundary cases: α≡1 (pure PURE) and α≡0 (pure GRPO).
- Hard vs. soft gating: binary threshold (α∈{0,1}) vs. sigmoid.
- Raw PRM score gating: α_i = σ(PRM_score_i) vs. calibrated CI width gating.
- Calibrated vs. uncalibrated: raw PRM score variance as uncertainty proxy vs. calibrated CI width.
- Hyperparameters: threshold τ, temperature β, quantile level.

**Statistical rigor.** 1.7B: 3 seeds, mean ± std. 8B: top 2 configs × 3 seeds + evaluation-level bootstrap CIs (1000 resamples).

**Compute fairness.** Per-method training wall-clock time and FLOPs. PRM calibration cost as separate one-time overhead. Accuracy-vs-compute Pareto curves. Theoretical FLOPs comparison with "Discovering Process-Outcome Credit" (arXiv 2602.01034) to justify not running as direct baseline (MC estimation overhead makes compute-normalized comparison unfavorable).

## Broader Significance

UGCA instantiates a general principle—Verifier-Uncertainty-Aware RL: when training with imperfect verifiers, credit assignment should adapt to per-instance verifier confidence. Math reasoning is a clean testbed where PRM uncertainty is measurable and calibratable. The framework generalizes to any domain with imperfect step-level verifiers (code generation, scientific reasoning, agentic tasks). We scope experiments to math reasoning and leave cross-domain validation as future work.

## Key References

- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)
- GRPO-λ / GRPO is Secretly a Process Reward Model (arXiv 2510.00194 / arXiv 2509.21154, ICLR 2026)
- LLM Reasoning with Process Rewards for Outcome-Guided Steps [PROGRS] (arXiv 2604.02341, 2026)
- Discovering Process-Outcome Credit in Multi-Step LLM Reasoning (arXiv 2602.01034, 2026)
- Save the Good Prefix: Precise Error Penalization via Process-Supervised RL [VPPO] (arXiv 2601.18984, 2026)
- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (Park et al., NeurIPS 2025)
- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv 2605.06785, 2026)
- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (Jia et al., ICML 2025)
- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping [UCAS] (arXiv 2025)
- ConfClip: Confidence-Weighted and Clipped Reward for RL in LLMs (arXiv 2509.17730, 2025)
- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)
- PRL: Process Reward Learning Improves LLMs' Reasoning Ability (arXiv 2026)
- Error Typing for Smarter Rewards [PathFinder-PRM] (arXiv 2025)
- Process Reinforcement through Implicit Rewards [PRIME] (arXiv 2025)
- Uncertainty-Aware Reward Discounting (arXiv Apr 2026)
- Reward Under Attack: Analyzing Robustness and Hackability of PRMs (arXiv 2603.06621, 2026)
- DAPO: An Open-Source LLM Reinforcement Learning System at Scale (2025)
- Good Learners Think Their Thinking [TP-GRPO] (arXiv Jul 2025)

## Resource Estimate

- **GPU compute**: ~2900 H100-hours (PRM quantile calibration: 100h; cross-family validation: 20h; Qwen3-1.7B ablations + baselines ~14 configs × 3 seeds: 840h; Qwen3-8B comparison 6 configs (top 2 × 3 seeds + 4 × 1 seed): 1600h; PROGRS/GRPO-λ reproduction development: 80h; DAPO/PROGRS/extra baseline runs: 200h; evaluation + diagnostics: 60h)
- **Timeline**: 8 weeks (wk1–2: PRM calibration + cross-family validation + PURE/veRL integration + PROGRS core reproduction; wk3–4: 1.7B full ablation sweep + PRPO/VPPO baselines + core assumption validation; wk5–6: 8B runs vs all baselines + longitudinal calibration tracking; wk7: reward-hacking analysis, PAG curves, Pareto curves, per-step visualization; wk8: paper writing and submission)
- **Estimated GPU cost**: ~$7,250 (H100 spot ~$2.50/hr)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ff543999-411a-4dd6-a4db-3d23c6c3fec6",
  "type": "user",
  "uuid": "0232c38b-0af0-4bc7-86cf-dde1d6631dce",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:55:12.436Z_

```json
{
  "parentUuid": "0232c38b-0af0-4bc7-86cf-dde1d6631dce",
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
  "uuid": "65beb905-4f5f-43a4-a14d-91d5de5c05fe",
  "timestamp": "2026-05-27T08:55:12.436Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:55:12.436Z_

```json
{
  "parentUuid": "65beb905-4f5f-43a4-a14d-91d5de5c05fe",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "62994700-7648-4764-9c88-cd9d21e992c0",
  "timestamp": "2026-05-27T08:55:12.436Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a thorough evalua…",
  "leafUuid": "62994700-7648-4764-9c88-cd9d21e992c0",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-gated credit assignment for math reasoning RL",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:55:39.869Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewer assessments and synthesize them as the Meta Judge.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [25% - 35%] 中位 28%

**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 中偏强


- Probability: [22% - 33%] 中位 27%

**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [28% - 38%] 中位 32%

Now I'm calculating the aggregate statistics across all three reviewers. The median probabilities are 28%, 27%, and 32%, which average to 29% with a median of 28%. The standard deviation comes out to about 2.16%, showing fairly tight clustering around the central estimate.

Looking at where the reviewers converge, there's strong agreement across the board on novelty being moderate, with all three identifying the core contribution as an obvious next step lacking conceptual surprise. The related work assessments are consistently positive, and all three reviewers flag the same critical vulnerabilities: the threat of simpler trajectory-level alternatives, fragility in the confidence interval assumptions tied to PRM reliability, calibration drift risks from frozen PRM weights, and the danger of using raw PRM scores as a gating mechanism. The incremental combination concern also appears across all reviewers, either explicitly or implicitly.

On significance, R3 leans slightly more optimistic by invoking the "Verifier-Uncertainty-Aware RL" principle, while R1 and R2 both argue this principle is too narrowly applied in the current work. For related work, R2 stands alone in flagging SSVPO and RTMC as notable omissions, whereas R1 and R3 rate the coverage as strong. R3 also appears to diverge on significance with a marginally stronger assessment, though the exact reasoning trails off.

Given the standard deviation is under 3%, the reviewers are quite aligned. The three ranges overlap substantially in the [28-33] band, and the median of the three median estimates lands around 28%. Following the principle to narrow the interval when consistency is high, I'm settling on approximately 25-34% with a central estimate of 29%.

Now I'm reviewing the implementation details from the proposal—they're planning to use about 2900 H100-hours at roughly $7,250, complete the work in 8 weeks, leverage public datasets like MATH for training, and conduct RL fine-tuning on smaller Qwen models without requiring new benchmarks or significant human oversight.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62994700-7648-4764-9c88-cd9d21e992c0",
  "isSidechain": false,
  "requestId": "req_011CbSnxzVsfBa8KAbgFhzxK",
  "type": "assistant",
  "uuid": "95c024f2-56af-4551-9948-86f176a1ddfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114rsuskuvkdNRxyEy4tK5R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17786,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2878,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 17786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17786
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

_source line 9 · 2026-05-27T08:56:20.391Z_

【阶段】: Meta Judge
【三次中位】: [28%, 27%, 32%]  std=2.2%
【共识维度】: 
- **Novelty = 中**（3/3 一致）：核心贡献是已有成熟组件（Park et al. quantile calibration + PURE min-form + GRPO）的 sigmoid gating 组合，"当 verifier 不确定时少信任它"是高度直觉性、conceptual leap 有限的 obvious next step
- **Related Work = 强/中偏强**（3/3 正面）：2×2 design space positioning 清晰，文献覆盖全面且准确，差异化分析到位
- **Trivial alternative 威胁真实**（3/3 提及）：PROGRS trajectory-level centering 可能已捕获大部分收益；raw PRM score gating 可能接近 CI width gating；hard threshold 可能接近 soft sigmoid
- **CI width ↔ PRM reliability 假设脆弱**（3/3 提及）：这是整个方法的基石，但 quantile regression 校准的 CI width 不直接等价于 PRM prediction error，宽 CI 可能反映 aleatoric uncertainty 而非 epistemic failure
- **Frozen PRM calibration drift 风险**（3/3 提及）：policy drift 下校准退化是真实风险，proposal 仅有诊断无修复机制
- **"Incremental combination" 感知**（3/3 提及）：审稿人极可能认为核心技术贡献仅为一个 gating equation
- **Significance = 中**（2/3 一致，R3 稍高）：问题本身重要但增量结果在直觉上 "expected"，难以 surprise reviewer

【异常维度】: 
- **R2 独有**：指出 SSVPO (ICLR 2026) 和 RTMC (Apr 2026) 两个 per-step credit assignment 竞争工作的遗漏，认为这些无需 PRM 校准的路线对 UGCA 必要性构成挑战，将 Related Work 降为"中偏强"。R1/R3 均未提及此遗漏——可能因为这两个工作的 signal source 与 UGCA 不同（structural vs. verifier calibration），不直接威胁 UGCA 在 2×2 design space 中的定位。但 R2 的论点有道理：如果 per-step credit 不需要 PRM 校准就能做好，UGCA 的 raison d'être 被削弱。**处理：部分采信，作为 Related Work 的小缺陷计入，但不改变整体"强"的判断——UGCA 的 positioning 仍然在其象限内成立，遗漏可在迭代中补上。**
- **R3 独有**：Significance 给"中偏强"，理由是"Verifier-Uncertainty-Aware RL"原则有 generalizable insight。但 R1/R2 均认为当前 instantiation 过于 narrow 不足以支撑这个宏大叙事。**处理：降权，以 R1/R2 的"中"为准——principle 的价值取决于实证范围，单一 domain 不够。**

【最终概率】: [25% - 33%] 中位 28%
【一致性】: 高（std=2.2% < 3%）
【综合理由】: 三位审稿人在所有核心维度上高度收敛：Novelty=中是概率天花板的决定因素（3/3），Related Work=强是下限的支撑（3/3），trivial alternative 威胁和核心假设脆弱性是主要风险（3/3）。高一致性下取中位附近并缩窄区间。中位 28% 由以下逻辑确定：(1) Novelty=中 + Significance=中 在 AAAI 级别会议上的天花板约 35%（即使执行完美），而本 proposal 还面临多个真实的 trivial alternative 威胁和核心假设风险，将上界压至 33%；(2) Related Work 的扎实程度、gap 的真实性、问题的重要性将下界托在 25%；(3) R3 的 32% 中位略高于 R1/R2，主要因为 Significance 打分偏高，但该偏高基于对"general principle"价值的乐观估计，在 2/3 审稿人持保守态度下应降权。最终中位取 28%，略偏向 R1/R2 的更严格估计。

【建议】: 边缘（中位 28% 低于 36% 通过线，但 idea 方向正确、定位清晰，有通过迭代优化提升至边缘区间的空间。核心瓶颈在 Novelty——需要找到比"obvious next step"更锐利的 insight 角度。）

【实施评估】:
  - 计算资源: ~2900 H100-hours（约 $7,250 spot price），包含 PRM 校准 100h、1.7B 消融 840h、8B 对比 1600h、baseline 复现 280h、评估 60h。资源需求中等偏高但在学术实验室可承受范围内
  - 数据需求: MATH 训练集 8K prompts（公开）、评测用 MATH-500/AMC23/AIME 2024&2025/OlympiadBench/MinervaMath（均公开可得）。无特殊数据障碍
  - 人工介入: 最小——主要是 PROGRS/GRPO-λ 等 baseline 的工程复现工作，以及 PRM 校准 pipeline 搭建。无需人工标注
  - 训练需求: 需要 RL 训练 Qwen3-8B 和 Qwen3-1.7B，以及 PRM quantile regression 校准微调。模型规模适中，单次训练约数十至百小时 H100
  - 新 Benchmark: 不需要，使用现有标准 benchmark
  - 预估周期: 8 周（含论文写作），timeline 紧凑但可行，前提是 veRL + PURE codebase 集成顺利且 baseline 复现无重大障碍

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95c024f2-56af-4551-9948-86f176a1ddfc",
  "isSidechain": false,
  "requestId": "req_011CbSnxzVsfBa8KAbgFhzxK",
  "type": "assistant",
  "uuid": "49a6a0b5-4c1a-4556-8f39-a4dfce1469b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114rsuskuvkdNRxyEy4tK5R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17786,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2878,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 17786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17786
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a thorough evalua…",
  "leafUuid": "49a6a0b5-4c1a-4556-8f39-a4dfce1469b2",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-gated credit assignment for math reasoning RL",
  "sessionId": "593076ab-eb07-425a-a678-91f40f4205a2"
}
```

---
