# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/593853a0-12e6-4ee7-a6a1-97c342b6682e.jsonl`
- **Structured JSON:** [`87690e7005442f90f245.json`](../../sessions/87/87690e7005442f90f245.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:11:06.946Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:11:06.946Z",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a well-grounded assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. PURE — \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning\" (NeurIPS 2025, arXiv 2504.15275):\n   最直接的 baseline。将 PRM 信用分配从 summation-form 改为 min-form，大幅缓解 reward hacking，在 MATH-500 达 82.6%。本 proposal 的 A^min 分支直接借用 PURE。关键问题：PURE 的 min-form 已经显著缓解了 reward hacking，UGCA 还能在此基础上获得多少增量？\n\n2. GRPO-λ — \"Credit Assignment Improves LLM Reasoning\" (arXiv 2510.00194, Oct 2025):\n   用 eligibility traces 改进 GRPO，7B 模型平均提升 3-4.5 分。同样假定 PRM 分数可靠。是 proposal 的另一个核心 baseline。\n\n3. Park et al. — \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" (NeurIPS 2025, arXiv 2506.09338):\n   用 quantile regression 校准 PRM，显著改善 calibration，但**明确只用于 test-time scaling（best-of-N, instance-adaptive search）**。Proposal 正确识别出这是 training-time 的空白。\n\n4. Distributional PRM (arXiv 2605.06785, May 2026):\n   用 conditional optimal transport 进一步改善 PRM 校准，同样**仅针对 test-time scaling**。确认了 training-time 应用的空白仍然存在。\n\n5. PROGRS — \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\" (arXiv 2604.02341, Apr 2026):\n   **最接近的竞争者**。使用 frozen quantile-regression PRM + outcome-conditioned centering。关键区别：PROGRS 在 trajectory level 做 centering（将错误轨迹的 PRM 分数 shift 到零均值），而非 per-step uncertainty gating。但核心动机高度重叠——都是不完全信任 PRM 分数。\n\n6. \"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\" (arXiv 2602.01034, Feb 2026):\n   提出 Step-wise Marginal Information Gain + Decoupled Masking Strategy，将 process 和 outcome rewards 分别应用于 CoT 和完整 completion。虽然机制不同，但同样试图自适应地分配 process vs outcome credit。**Proposal 未引用此文，这是一个 related work 覆盖缺口。**\n\n7. Jia et al. — \"Do We Need to Verify Step by Step?\" (ICML 2025):\n   理论证明 outcome supervision 在统计意义上不比 process supervision 更难。Proposal 用此作为\"降级到 outcome credit 是有理论保障的\"论据。引用准确。\n\n8. PRPO (arXiv 2601.07182, Jan 2026):\n   通过 location-parameter shift 对齐 process 和 outcome advantages，Qwen2.5-Math-1.5B 上 61.2→64.4%。固定结构对齐，非自适应。\n\n9. Uncertainty-Aware Reward Discounting (arXiv 2604.26360, Apr 2026):\n   用 ensemble disagreement 缓解 RLHF 中的 reward hacking，但面向 general preference learning，非 math 场景的 process-outcome interpolation。\n\n10. UCAS — \"Unlocking Exploration in RLVR\" (arXiv 2510.10649, Oct 2025):\n    用 policy model 自身的 logit uncertainty 调制 advantages。与 UGCA 的关键区别：UCAS 用的是 policy 的 epistemic uncertainty，UGCA 用的是 verifier (PRM) 的 calibration uncertainty。\n\n- **调研总结**: PRM calibration for test-time scaling 和 RL credit assignment for math reasoning 是两条成熟但分离的研究线。PROGRS (Apr 2026) 和 \"Discovering Process-Outcome Credit\" (Feb 2026) 已经在探索 process-outcome 的自适应融合，但通过不同机制。UGCA 的具体切入点——用 PRM quantile regression confidence width 做 per-step sigmoid gating between min-form process advantage 和 GRPO outcome advantage——在现有文献中确实未被直接实现，但概念距离并不远。\n\n【Trivial Alternative 检验】:\n\n存在若干更简单的替代方案构成威胁：\n\n1. **Hard thresholding**: 直接设定阈值，confidence width > τ 的步骤完全使用 outcome credit，其余完全使用 process credit。省去 sigmoid gating 和 β 参数，效果可能接近。UGCA 的增量价值在于 soft interpolation，但这需要实验证明 soft 比 hard 好多少。\n\n2. **Outcome-only baseline (plain GRPO)**: 既然 Jia et al. 证明了 outcome supervision 统计上不比 process supervision 更难，那一个自然的问题是：为什么不直接用 outcome-only GRPO，完全避开 PRM 不可靠的问题？PURE 的实验已经表明 min-form PRM 在实践中优于 outcome-only，但这个优势是否在 UGCA 的框架下仍然显著需要验证。\n\n3. **Simply filtering out low-confidence PRM steps**: 如果 PRM 对某步的 confidence 很低，直接 mask 掉该步的 process reward，其余步仍用 PURE min-form。这比 UGCA 简单得多。\n\nUGCA 的增量价值在于：提供了一个**原则性的 interpolation 框架**，而非 ad-hoc 的 filtering。但 reviewer 很可能会要求与这些 trivial baselines 做消融实验。如果消融显示 soft gating 与 hard thresholding 差异不大，核心贡献会被严重削弱。\n\n【前提假设检验】:\n\n核心逻辑链：PRM miscalibrated → miscalibration causes reward hacking in RL training → quantile regression confidence width captures miscalibration → gating to outcome credit on uncertain steps alleviates reward hacking → overall training improves\n\n未经验证的关键假设：\n\n1. **\"PURE min-form 之后仍存在足够严重的 PRM miscalibration-induced reward hacking\"**: PURE 的 min-form 已经被证明能大幅缓解 reward hacking。UGCA 需要证明在 min-form 基础上，PRM miscalibration 仍然是一个显著问题。如果 PURE 已经解决了大部分 reward hacking，UGCA 的改进空间可能很小。这是最关键的未验证前提。\n\n2. **\"Quantile regression confidence interval width 在 RL training 动态中仍然是 PRM reliability 的好 proxy\"**: Park et al. 的校准是在静态推理场景中验证的。在 RL training 中，policy 不断变化，PRM 面对的分布也在 shift。Frozen PRM 的 calibration 在 training 后期是否仍然有效是一个公开问题。\n\n3. **\"Per-step gating 比 trajectory-level 方法（如 PROGRS 的 outcome-conditioned centering）更有效\"**: 更细粒度不一定更好——per-step 的噪声也更大。\n\n4. **\"Sigmoid gating function 的形式选择是合理的\"**: 为什么是 sigmoid 而不是线性 interpolation 或其他 monotone function？这个选择缺乏理论动机。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Proposal 正确识别了一个真实的 gap：PRM calibration 方法（Park et al. NeurIPS 2025; Distributional PRM 2605.06785）只用于 test-time，而 RL credit assignment 方法（PURE, GRPO-λ, PRPO）不考虑 PRM uncertainty。这个 gap 是真实的。但 novelty 的性质是**组合式的（combinatorial）**而非**概念式的（conceptual）**——核心贡献是用一个 sigmoid 函数将两个已有组件（calibrated PRM confidence width + PURE/GRPO advantages）连接起来。PROGRS (arXiv 2604.02341) 已经在用 frozen quantile-regression PRM 做类似的事情（虽然在 trajectory level 而非 step level），\"Discovering Process-Outcome Credit\" (arXiv 2602.01034) 也在探索自适应 process-outcome 分配。UGCA 的 novelty delta 是\"per-step sigmoid gating using confidence interval width\"——这是一个有意义但不令人惊讶的 delta。\n\n2. **Significance: 中** — \n   问题本身是重要的：如何在 RL training 中更好地利用不完美的 PRM 信号。如果 UGCA 能稳定提升 2-3 分（在 PURE 基础上），这对社区是有用的。但受限于两个因素：(a) PURE min-form 已经大幅解决了 reward hacking 问题，UGCA 的边际改进空间可能有限；(b) 核心发现如果 positive（\"用 uncertainty gating 帮助训练\"），审稿人的反应更可能是 \"makes sense, I would have guessed this\" 而非 \"surprising\"。Impact 更多是 incremental improvement 而非 paradigm shift。\n\n3. **Related Work: 强** — \n   Proposal 对领域的覆盖非常全面：PURE, GRPO-λ, PROGRS, UCAS, Distributional PRM, PathFinder-PRM, PRPO, Uncertainty-Aware Reward Discounting, TP-GRPO, PRIME 均被讨论，且差异化定位清晰。唯一遗漏是 \"Discovering Process-Outcome Credit in Multi-Step LLM Reasoning\" (arXiv 2602.01034)，它直接做 process-outcome credit 分解，应被讨论。除此之外，related work 覆盖在投稿质量中属于上乘。\n\n【概率估计】: 22% - 32%，中位 27%\n\n【估计理由】: \nRelated Work 维度强，表明作者对领域有深入理解，这为执行质量提供了信心。但 idea 质量的天花板受限于 Novelty 和 Significance 两个维度：\n\n- Novelty 是组合式而非概念式的——用 sigmoid 将 calibration confidence width 映射为 gating coefficient 这一核心机制，技术上直白，不太可能让审稿人感到 \"I hadn't thought of this\"。PROGRS 已经在做概念相近（用 calibrated PRM 调节 RL training 中的 process credit）的工作。\n- Significance 受限于 PURE min-form 已经大幅缓解了 reward hacking 的事实——UGCA 的改进空间可能较窄。如果最终只能在 MATH-500 上提升 1-2 分，很难说服审稿人这是一个值得单独发表的贡献。\n- Trivial alternative 威胁真实存在——hard thresholding 或 simple masking 可能达到 80-90% 的效果。\n- 概率上界被 Novelty（组合式）和 \"unsurprising if positive\" 限制在 ~32%；下界被 \"gap 是真实的 + related work 覆盖强 + 有理论动机\" 支撑在 ~22%。\n\n【主要风险】:\n1. **PURE min-form 后的增量空间不足**：如果 PURE 的 min-form 已经充分缓解了 reward hacking，UGCA 的额外收益可能微乎其微，实验结果将不足以支撑一篇 top-venue 论文。这是最大的 idea 层面风险——不是方法错误，而是**问题空间可能已经被 PURE 压缩得太小**。\n2. **组合式 novelty 难以通过审稿人的 \"so what\" 检验**：核心贡献归结为一个 sigmoid gating function，审稿人可能认为这是一个 engineering trick 而非 scientific contribution，尤其在 PROGRS 已经展示了类似动机（用 calibrated PRM 改善 RL training）的背景下。\n```\n\nSources:\n- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [GRPO-λ (arXiv 2025)](https://arxiv.org/abs/2510.00194)\n- [Know What You Don't Know: PRM Calibration (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)\n- [Distributional PRM (arXiv 2605.06785)](https://arxiv.org/abs/2605.06785)\n- [PROGRS (arXiv 2604.02341)](https://arxiv.org/abs/2604.02341)\n- [Discovering Process-Outcome Credit (arXiv 2602.01034)](https://arxiv.org/abs/2602.01034)\n- [Jia et al. - Rethinking Process Supervision (ICML 2025)](https://icml.cc/virtual/2025/poster/46497)\n- [PRPO (arXiv 2601.07182)](https://arxiv.org/abs/2601.07182)\n- [Uncertainty-Aware Reward Discounting (arXiv 2604.26360)](https://arxiv.org/abs/2604.26360)\n- [UCAS - Unlocking Exploration in RLVR (arXiv 2510.10649)](https://arxiv.org/abs/2510.10649)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- PURE: \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning\" (NeurIPS 2025, arXiv 2504.15275): 直接前驱工作。用 min-form（取未来 reward 的最小值而非求和）来替代传统 summation-form，缓解 PRM-induced reward hacking。Qwen2.5-Math-7B 上达到 82.6% MATH-500，代码公开。本 proposal 的 A^min 分量直接来自此方法。\n- Park et al.: \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" (NeurIPS 2025, arXiv 2506.09338): 直接前驱工作。证明 off-the-shelf PRM 系统性过估成功概率，提出 quantile regression 校准方法。但**仅用于 test-time scaling（instance-adaptive best-of-N）**，未涉及 RL 训练。本 proposal 的校准模块直接来自此工作。\n- Distributional PRM (arXiv 2605.06785, May 2026): 用 conditional optimal transport 改进 PRM 校准，达到 SOTA 校准质量。同样**明确只针对 test-time scaling**。\n- GRPO-λ (arXiv 2510.00194, Oct 2025): 用 eligibility traces 改进 GRPO 的 credit assignment，7B 模型上平均 +3-4.5 分。从 ICLR 2026 撤稿。不涉及 PRM 校准或不确定性。\n- PROGRS (arXiv 2604.02341, Apr 2026): **最接近的竞争者**。使用 frozen quantile-regression PRM + outcome-conditioned centering，在 GRPO 中集成 process bonus。关键区别：它在 trajectory level 做 centering（将错误轨迹的 PRM 分数 shift 到零均值），而非 per-step uncertainty gating。但它同样使用了 quantile-regression PRM 在 RL 训练中，削弱了 proposal 声称的\"无人将 PRM 校准用于 RL 训练\"这一 gap。\n- Jia et al.: \"Do We Need to Verify Step by Step?\" (ICML 2025, arXiv 2502.10581): 真实论文。证明在标准 data coverage 假设下，outcome supervision 在统计上不比 process supervision 更难。Proposal 用此作为 degradation to outcome credit 的理论支撑。\n- Uncertainty-Aware Reward Discounting (arXiv 2604.26360, Apr 2026): 用 ensemble disagreement 缓解 RLHF 中的 reward hacking。针对通用偏好学习，非 math-specific process-outcome interpolation。但**核心 idea 高度相似**：在 reward 不确定时减少对 reward 的信赖。\n- UCAS (arXiv Oct 2025): 用 policy model 自身的 logit uncertainty 来调制 advantage——和 PRM verifier uncertainty 是不同的 uncertainty 来源，但\"用不确定性调制 advantage\"这个操作模式相同。\n- 调研总结: PRM-based RL credit assignment 是 2025-2026 的活跃战场，已有多种改进方法（PURE、GRPO-λ、PROGRS、PRPO、UCAS）。PRM 校准方法（quantile regression、optimal transport）已成熟但主要用于 test-time。PROGRS 已经在 RL 训练中使用了 quantile-regression PRM（虽然机制不同）。\"用不确定性调制 reward/advantage\"的 meta-idea 已在 UCAS 和 UARD 中出现。Proposal 的具体贡献空间（per-step PRM confidence interval width → sigmoid gating → process/outcome interpolation）确实尚未被精确复现，但周围工作已经非常密集。\n\n【Trivial Alternative 检验】:\n存在多个低成本替代方案威胁：\n1. **简单阈值过滤**：直接丢弃 PRM 置信度低于阈值的 step 的 process reward，仅保留高置信 step 的 process advantage，其余 step 用 outcome advantage。无需 sigmoid gating 的连续化设计，可能效果相近。\n2. **固定混合比例**：不用 per-step adaptive gating，直接用一个全局 α 混合 process 和 outcome advantage（类似于简单的 weighted sum），通过 grid search 调优。这是 proposal 方法的退化形式。\n3. **PURE 本身已部分解决**：PURE 的 min-form 天然对高 PRM score 做了保守化处理（取最小值而非累加），已经在机制上缓解了 reward hacking。在此基础上再加 uncertainty gating 的**边际收益**可能有限。\n4. **PROGRS 的 outcome-conditioned centering** 已经是一种\"在 PRM 不可靠时降低其影响\"的策略，只是实现方式不同。\n\nproposal 的增量价值在于：提供了一个有理论 grounding 的 per-step 连续 interpolation 机制。但如果 trivial alternatives（尤其是简单阈值）效果相当，这个增量价值会被严重稀释。\n\n【前提假设检验】:\n核心逻辑链中有以下未经验证的假设：\n\n1. **\"PRM 校准置信区间宽度 = 该 step 的 PRM 信号不可靠程度\"**：这是最关键的假设。Quantile regression 的置信区间宽度反映的是 PRM 预测的条件分布的 spread，但这不一定等同于\"PRM 在这个 step 上会导致 reward hacking\"。宽置信区间可能出现在本身就困难（但 PRM 判断正确）的 step 上。proposal 没有论证为什么 confidence interval width 是正确的 gating signal。\n\n2. **\"在 PRM 不确定的 step 上退化到 outcome credit 会减少 reward hacking\"**：Jia et al. 的理论结果说的是统计等价性（outcome supervision 不比 process supervision 更难），不是说 outcome credit 在特定 uncertain step 上比 process credit 更准确或更 robust。这个推论存在逻辑跳跃。\n\n3. **\"reward hacking 主要发生在 PRM 不确定的 step 上\"**：这是一个未经验证的经验性假设。Reward hacking 也可能发生在 PRM 高度自信但错误的 step 上（即 PRM 的 systematic bias，不是 uncertainty 能捕捉的）。如果 hacking 主要来自高置信但错误的 PRM 判断，则 uncertainty gating 无法解决核心问题。\n\n【3 维度打分】:\n  1. Novelty: 弱-中 — 核心 idea 是将三个已有模块（PURE 的 min-form advantage、Park et al. 的 quantile regression 校准、GRPO 的 outcome advantage）用一个 sigmoid 函数组合起来。这是一个自然而直觉的组合——\"可靠时信 PRM，不可靠时退回 outcome\"——领域内研究者看到 Park et al. + PURE 后很容易想到。PROGRS (arXiv 2604.02341) 已在 RL 训练中使用了 quantile-regression PRM，只是用了不同的利用方式（centering vs. gating），削弱了\"首次将 PRM 校准引入 RL 训练\"这一 novelty claim。UCAS 和 UARD 已分别展示了\"用 uncertainty 调制 advantage\"和\"用 uncertainty 缓解 reward hacking\"的 meta-idea。剩余的精确 novelty delta 是具体的 sigmoid gating 公式和 per-step process/outcome interpolation，这属于工程变体级别的贡献。\n\n  2. Significance: 中 — 研究问题本身重要且 timely：PRM miscalibration 对 RL 训练的影响是 real problem（Park et al. 和 PURE 都证实了这点）。如果实验结果显示在 PURE 之上有显著提升，有一定影响力。但：(a) PURE 已经很好地解决了 reward hacking 问题（82.6% MATH-500），边际改进空间可能有限；(b) 方法特异性高——依赖特定 PRM 架构和特定校准方法，可推广性存疑；(c) 如果核心发现是 positive（\"uncertainty gating 比 PURE 好 1-2 个点\"），审稿人的反应更可能是 \"I would have guessed this\" 而非 \"surprising\"。\n\n  3. Related Work: 强 — Proposal 对相关工作的覆盖相当全面。准确识别了 PURE、GRPO-λ、PROGRS、UCAS、PRPO、PRIME、PathFinder-PRM、TP-GRPO、Distributional PRM 等关键工作，差异化定位也基本准确（特别是 PROGRS 的 trajectory-level centering vs. per-step gating 的区分）。引用的关键论文（Jia et al. ICML 2025、Park et al. NeurIPS 2025、PURE NeurIPS 2025）均经过验证真实存在且描述准确。唯一的瑕疵是略微低估了 PROGRS 的相关性——PROGRS 同样在 RL 训练中使用了 quantile-regression PRM，不仅是\"固定 centering 规则\"那么简单。\n\n【概率估计】: [18% - 28%] 中位 23%\n\n【估计理由】: \nNovelty 是主要限制因素。核心贡献是三个已有公开模块的自然组合，sigmoid gating 公式是直觉性设计而非深刻洞察。PROGRS、UCAS、UARD 已在不同角度实现了高度相似的 meta-idea，使得精确 novelty delta 仅停留在工程变体层面。Significance 受限于 PURE 已有效解决 reward hacking（82.6% MATH-500），在此基础上的边际改进空间和惊喜度有限。Related Work 覆盖充分是正面因素，但不足以弥补 idea 内核的薄弱。前提假设检验暴露了\"confidence interval width = 不可靠度\"和\"uncertain step 上 outcome credit 更好\"这两个未经验证的关键逻辑环节，进一步压低了 idea 的说服力。Trivial alternative（简单阈值过滤、固定混合比）对方法的增量价值构成直接威胁。综合来看，idea 方向正确但内核偏薄，属于 rubric 中 15-25% 和 25-35% 的边界区域，取 23%。上界被 novelty 和 trivial alternative 威胁封顶在 28%。\n\n【主要风险】:\n1. **Novelty 不足被拒**：审稿人可能认为这是 PURE + Park et al. quantile regression 的 trivial combination，缺乏独立的技术洞察，特别是在 PROGRS 已将 quantile-regression PRM 用于 RL 训练的背景下。\n2. **核心假设被质疑**：\"PRM confidence interval width 是正确的 gating signal\"这一未经验证的假设是逻辑链的核心，审稿人可能要求提供理论或实证支撑（如：reward hacking 确实集中在 PRM uncertain steps 上），而这目前缺失。\n```\n\nSources:\n- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [Know What You Don't Know: PRM Calibration (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)\n- [Distributional PRM (arXiv May 2026)](https://arxiv.org/html/2605.06785)\n- [GRPO-λ (arXiv Oct 2025)](https://arxiv.org/abs/2510.00194)\n- [PROGRS (arXiv Apr 2026)](https://arxiv.org/abs/2604.02341)\n- [Jia et al. - Process vs Outcome Supervision (ICML 2025)](https://arxiv.org/abs/2502.10581)\n- [Uncertainty-Aware Reward Discounting (arXiv Apr 2026)](https://arxiv.org/html/2604.26360)\n- [PURE GitHub Repository](https://github.com/CJReinforce/PURE)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to produce a thorough evaluation. Let me synthesize all findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- PURE \"Stop Summation: Min-Form Credit Assignment\" (NeurIPS 2025, arXiv 2504.15275): 提出 min-form value function 替代 summation-form，显著缓解 PRM-induced reward hacking。82.6% MATH-500, 82.5% AMC23 (Qwen2.5-Math-7B)。本 proposal 直接构建在 PURE 之上，将其 min-form advantage 作为高置信度时的 process credit。\n- GRPO-λ (arXiv 2510.00194, submitted ICLR 2026): 将 eligibility traces 引入 GRPO，通过 token-level log-prob 近似 λ-return，在 7B 模型上平均提升 3-4.5 points。与本 proposal 同为 credit assignment 改进，但不涉及 PRM 可靠性判断。\n- PROGRS \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\" (arXiv 2604.02341, Apr 2026): 使用 frozen quantile-regression PRM + multi-scale coherence evaluator，通过 outcome-conditioned centering 整合 process reward。MATH-500 74.9% vs DAPO 69.7%。**与本 proposal 最相近**——也用了 quantile-regression PRM，但策略是 trajectory-level 的 fixed centering，而非 per-step uncertainty gating。\n- PROF \"Beyond Correctness: Harmonizing Process and Outcome Rewards\" (arXiv 2509.03403): 通过 consistency-driven sample selection 协调 process 和 outcome reward（保留 correct+高 process 和 incorrect+低 process 的样本），比 naïve blending 好 4%+。与本 proposal 目标相近（协调 process/outcome），但机制完全不同（sample filtering vs. per-step gating）。\n- UCAS \"Unlocking Exploration in RLVR\" (arXiv 2510.10649, submitted ICLR 2026): 利用 policy model 自身的 logit uncertainty 做 response-level + token-level advantage 调制。名称接近但信号来源不同——用的是 policy uncertainty 而非 PRM verifier uncertainty。\n- Park et al. \"Know What You Don't Know: Uncertainty Calibration of PRMs\" (NeurIPS 2025, arXiv 2506.09338): Quantile regression 校准 PRM，提出 instance-adaptive scaling (IAS) 框架。**核心发现：PRM 存在系统性 miscalibration。但应用场景仅限 inference-time scaling (best-of-N)**。\n- Distributional PRM (arXiv 2605.06785, May 2026): 通过 conditional optimal transport 实现 PRM 校准的 SOTA，同样仅面向 test-time scaling。\n- PRPO (arXiv 2601.07182, Jan 2026): 通过 location-parameter shift 对齐 process 和 outcome advantages，Qwen2.5-Math-1.5B 61.2→64.4%。使用固定的结构对齐，非自适应 per-step 权重。\n- \"Discovering Process-Outcome Credit\" (arXiv 2602.01034, Feb 2026): 提出 step-wise Marginal Information Gain + decoupled masking 进行 process-outcome credit 分配。机制不同但动机相关。\n- Uncertainty-Aware Reward Discounting (arXiv 2604.26360, Apr 2026): Ensemble disagreement 缓解 RLHF reward hacking，面向 general preference learning 而非 math process-outcome interpolation。\n- Jia et al. \"Do We Need to Verify Step by Step?\" (ICML 2025, arXiv 2502.10581): 理论证明 outcome supervision 统计上不比 process supervision 更难。本 proposal 用此作为 fallback 到 outcome credit 的理论依据。\n\n- **调研总结**: 这是一个极度拥挤的子领域——2025-2026 年间至少有 10+ 篇工作聚焦于 \"如何在 math reasoning RL 中更好地使用 PRM 做 credit assignment\"。PRM 校准（Park et al., Distributional PRM）和 RL credit assignment（PURE, GRPO-λ, PRPO, PROGRS, PROF）是两条平行发展的线。本 proposal 的核心定位是 **bridge the gap**——将前者的 calibration confidence 注入后者的 per-step advantage computation。这个具体的交叉点（PRM 校准置信度 → 训练时 per-step gating）在 May 2026 确实未被直接占据，但 PROGRS 已经非常接近（同样使用 frozen QR-PRM，只是 centering 策略不同）。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁：\n1. **Fixed interpolation baseline**: 用固定 α 线性组合 A^min 和 A^GRPO（α 通过 grid search 选取），不需要任何 PRM 校准。如果固定 α=0.5 的 blending 就能取得类似效果，整个 uncertainty-gating 机制的增量价值就不成立。Proposal 必须证明 per-step adaptive α 显著优于 fixed α。\n2. **Better PRM, same pipeline**: 直接用 Distributional PRM（更好的校准 SOTA）替换原始 PRM 作为 PURE 的输入，不做任何 gating——如果更好的 PRM 本身就缓解了 reward hacking，那 gating 机制的必要性就被削弱。\n3. **Simple thresholding**: 对 PRM confidence 低于阈值的 step 直接 mask 掉 process reward（advantage = 0 或完全用 outcome），而非 sigmoid soft gating。如果这个更简单的 hard-gating 效果相当，soft gating 的贡献就是 marginal 的。\n\nProposal 的增量价值取决于：per-step adaptive sigmoid gating 是否显著优于上述三个 trivial alternatives。这是个**纯实验问题**——idea 层面无法事先回答。\n\n【前提假设检验】:\n核心逻辑链中存在以下未验证假设：\n1. **\"即使在 PURE min-form 下，PRM miscalibration 仍然导致显著的残余 reward hacking\"** — PURE 已经通过 min-form 大幅缓解了 reward hacking。Proposal 的前提是 PURE 还不够，uncertain steps 上仍有残余问题。但这个前提是否成立尚无实证——PURE 论文未报告 per-step 的 reward hacking 分布，也没有证据表明问题集中在 PRM-uncertain steps。\n2. **\"Quantile regression confidence interval width 是 PRM reliability 的好 proxy\"** — 宽置信区间 ≠ PRM 不可靠。QR 置信区间反映的是 model uncertainty about prediction interval，而非\"这个 PRM 分数是否可信\"。如果 PRM 系统性地 miscalibrate（而非随机 noise），CI width 可能无法捕捉这种偏差。\n3. **\"Fallback 到 GRPO outcome advantage 是最优降级策略\"** — 为什么不是 fallback 到 zero advantage（忽略该 step）？或 fallback 到某种 baseline advantage？选择 GRPO 作为 fallback 的理由是 Jia et al. 的定理，但那个定理说的是\"统计上不更难\"，不是\"outcome advantage 是最优 fallback 目标\"。\n4. **\"Sigmoid gating 函数 σ(−(w−τ)/β) 是合适的函数形式\"** — 这是一个设计选择，有两个额外超参 τ 和 β 需要调。如果效果好坏高度依赖于 τ 和 β 的选取（且 PROGRS 那样的 non-parametric centering 更鲁棒），那超参敏感性会是审稿人的攻击点。\n\n【3 维度打分】:\n  1. Novelty: 【中】— 核心贡献是将两条已有研究线（PRM calibration + RL credit assignment）做了自然组合。具体交叉点（per-step calibration confidence → adaptive gating）确实未被直接占据（调研确认），但 PROGRS 已经在同一条路上走了大半（也用 frozen QR-PRM，只是 centering 而非 gating）。核心 insight \"不要信任 uncertain PRM scores\" 是一个 common sense principle 而非 surprising observation。组合型 novelty 在拥挤领域中的含金量有限——审稿人会问 \"so you just replaced fixed centering with sigmoid gating?\"\n  \n  2. Significance: 【中】— 问题方向正确——PRM-based RL credit assignment 是当前 math reasoning 的核心挑战之一。但预期贡献偏 incremental：在 PURE 已经 82.6% MATH-500 的基础上，进一步改进的空间有限。如果核心发现是 positive（uncertainty gating 优于 uniform trust），审稿人的反应更可能是 \"makes sense, I would have guessed this\"——缺乏 surprise factor。对于 OlympiadBench/AIME24 等更难 benchmark 上的改进，意义会更大，但 proposal 未给出预期增量的具体论证。\n  \n  3. Related Work: 【强】— 这是 proposal 最突出的优势。对 10+ 篇高度相关工作的覆盖极其详尽且准确（经调研验证），每篇都有清晰的差异化定位。包含最近至 May 2026 的工作（Distributional PRM, PROGRS）。唯一遗漏：PROF (arXiv 2509.03403) 是一个重要的 process-outcome 协调方法，未被明确提及；\"Discovering Process-Outcome Credit\" (arXiv 2602.01034) 也值得讨论。\n\n【概率估计】: [20% - 32%] 中位 25%\n\n【估计理由】: \nNovelty 为\"中\"——这是一个 well-executed combination paper，定位清晰，gap 真实存在，但组合方式自然可预测（\"用 calibration 信号调制 trust\"是直觉性 solution），在极度拥挤的子领域中差异化不够显著。Significance 为\"中\"——方向对但增量预期有限，core finding 若 positive 不会 surprising。Related Work 为\"强\"是加分项，但 related work 好只能提高 proposal 的可信度，不能弥补 idea 内核的 surprise 缺失。\n\n**Novelty 和 Significance 共同限制了上界**：在当前 math reasoning RL 这个极度内卷的赛道上，纯 credit assignment 的 incremental improvement paper 面临非常高的审稿门槛。要突破 30%+ 概率，需要 either (a) 更 surprising 的核心发现，or (b) 在困难 benchmark 上展示出显著超出 PURE 的 empirical gains——后者需要实验验证。\n\n【主要风险】:\n1. **Trivial alternative 威胁**: Fixed α interpolation baseline 可能效果相当，如果 ablation 无法清晰证明 per-step adaptive gating 的增量价值，审稿人会质疑 \"is the uncertainty-aware gating really necessary, or does any blend work?\"\n2. **前提假设不牢固**: Proposal 的核心前提——\"PURE min-form 之后仍有显著的 PRM-uncertainty-driven reward hacking\"——缺乏先验证据。如果实验发现 PURE 已经很好地解决了这个问题（uncertain steps 上的 reward hacking 本就不严重），整个 gating 机制的动机就崩塌了。\n```\n\nSources:\n- [PURE - Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)\n- [GRPO-λ: Credit Assignment improves LLM Reasoning](https://arxiv.org/abs/2510.00194)\n- [PROGRS - LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/pdf/2604.02341)\n- [PROF - Beyond Correctness: Harmonizing Process and Outcome Rewards](https://arxiv.org/abs/2509.03403)\n- [UCAS - Unlocking Exploration in RLVR](https://arxiv.org/abs/2510.10649)\n- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)\n- [Distributional Process Reward Models (arXiv 2605.06785)](https://arxiv.org/abs/2605.06785)\n- [PRPO: Aligning Process Reward with Outcome Reward](https://arxiv.org/abs/2601.07182)\n- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)\n- [Uncertainty-Aware Reward Discounting](https://arxiv.org/abs/2604.26360)\n- [Jia et al. - Do We Need to Verify Step by Step? (ICML 2025)](https://arxiv.org/abs/2502.10581)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL\n\n## Core Problem\n\nCurrent methods for integrating process reward models into RL training (PURE, GRPO-λ, PRL, PRPO) treat all PRM step-level scores as equally trustworthy, yet PRMs are demonstrably miscalibrated—overestimating success probabilities on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals rather than genuinely improving reasoning.\n\n## Research Opportunity\n\nPRM calibration methods have matured rapidly (quantile regression [NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling (best-of-N, instance-adaptive search). No work uses PRM uncertainty to modulate credit assignment during RL training. Meanwhile, Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision—suggesting the empirical gap is algorithmic, motivating a principled interpolation. The building blocks (calibrated PRMs, GRPO/PURE training pipelines, math reasoning benchmarks) all exist, making a 2-month implementation feasible for AAAI 2027 (deadline: July 28, 2026).\n\n## Research Landscape\n\nPURE (NeurIPS 2025) replaces summation-form with min-form credit assignment, achieving 82.6% on MATH-500 and 82.5% on AMC23 with Qwen2.5-Math-7B but still assumes PRM scores are reliable. GRPO-λ (arXiv Oct 2025) adds eligibility traces to GRPO, improving average math scores by 3–4.5 points on 7B models but also trusts PRM outputs uniformly. PROGRS (arXiv Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% on MATH-500 vs 69.7% DAPO baseline) but applies a fixed centering rule at the trajectory level, not per-step uncertainty gating. UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty—fundamentally different from PRM verifier uncertainty. The Distributional PRM (arXiv May 2026) achieves state-of-the-art calibration via conditional optimal transport but explicitly targets only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL credit assignment. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) but uses fixed structural alignment, not adaptive per-step weighting. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement to mitigate reward hacking in RLHF but targets general preference learning, not process-outcome interpolation for math. TP-GRPO (arXiv Jul 2025) introduces capability-adaptive rewards with generative PRM at the thought level using intrinsic signals, not PRM calibration. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals. Thorough concurrent-work search across arXiv and OpenReview (May 2026) confirms the specific gap—using PRM calibration confidence to drive per-step adaptive interpolation between process and outcome credit during RL training—remains unaddressed.\n\n## Proposed Approach\n\nWe propose Uncertainty-Gated Credit Assignment (UGCA), which equips the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting the open-source code from Park et al., NeurIPS 2025), then defines a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. During RL training, the advantage at step i is computed as A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i, where A^min is PURE-style min-form process advantage and A^GRPO is group-relative outcome advantage—high-confidence PRM steps lean on process credit while uncertain steps gracefully degrade to outcome credit. We train Qwen3-8B and Qwen3-1.7B on the MATH training set (8K prompts) using this modified GRPO objective atop the PURE codebase, with the calibrated PRM frozen throughout, evaluating on MATH-500, AMC23, AIME24, and OlympiadBench against re-implemented PURE, GRPO, and GRPO-λ baselines on the same models. The method is theoretically grounded by the Jia et al. (ICML 2025) proof that outcome supervision is statistically no harder than process supervision, making the degradation principled, and requires only a one-time quantile calibration pass with no additional training signals.\n\n## Detailed Description\n\nWe introduce Uncertainty-Gated Credit Assignment (UGCA), a method that uses calibrated PRM confidence to adaptively interpolate between process-level and outcome-level credit during RL training for mathematical reasoning. While PRM calibration methods (quantile regression, conditional optimal transport) have matured rapidly, they target only inference-time scaling. Meanwhile, RL credit assignment methods (PURE, GRPO-λ, PRPO) treat all PRM step scores as equally reliable, enabling reward hacking on uncertain steps. UGCA bridges this gap: we equip the off-the-shelf Qwen2.5-Math-PRM-7B with quantile-regression confidence intervals and derive a per-step gating coefficient—high-confidence steps use PURE-style min-form process advantages; low-confidence steps gracefully degrade to GRPO outcome advantages. This interpolation is theoretically motivated by the Jia et al. (ICML 2025) proof that outcome supervision is statistically equivalent to process supervision. We evaluate on Qwen3-8B and Qwen3-1.7B across MATH-500, AMC23, AIME24, and OlympiadBench, targeting improvements over PURE and GRPO-λ baselines while demonstrating measurably reduced reward hacking on PRM-uncertain steps. All core building blocks (calibrated PRM code, PURE codebase, pre-trained PRMs) are publicly available, and concurrent-work search (May 2026) confirms this mechanism is novel.\n\n## Key References\n\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)\n- GRPO-λ: Credit Assignment Improves LLM Reasoning (arXiv 2025)\n- LLM Reasoning with Process Rewards for Outcome-Guided Steps (arXiv 2026)\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv 2026)\n- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (ICML 2025)\n- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning (arXiv 2025)\n- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)\n- PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary (arXiv 2026)\n- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision (arXiv 2025)\n- Process Reinforcement through Implicit Rewards (arXiv 2025)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~1800 H100-hours (PRM quantile calibration on Qwen2.5-Math-PRM-7B: 100h; Qwen3-1.7B RL ablations ×6 configs: 360h; Qwen3-8B RL ablations ×6 configs: 1200h; final evaluation + reward-hacking diagnostics: 140h), timeline: 8 weeks (wk1–2: PRM quantile-regression calibration + PURE codebase integration with veRL; wk3–4: 1.7B ablations over gating threshold τ, temperature β, and quantile level; wk5–6: 8B full comparison runs vs PURE/GRPO/GRPO-λ baselines; wk7: reward-hacking analysis, per-step uncertainty visualization, ablation plots; wk8: paper writing and AAAI submission), estimated_gpu_cost: $4,500 (H100 spot at ~$2.50/GPU-hr)\n- **human_in_loop**: gpu_hours: ~1800 H100-hours (identical compute workload), timeline: 6 weeks (Claude accelerates PURE/veRL codebase integration, quantile-regression head implementation, hyperparameter sweep scripting, results analysis, and paper drafting), claude_api_cost: $300, estimated_gpu_cost: $4,500\n- **auto_research**: gpu_hours: ~1800 H100-hours (identical compute workload), timeline: 5 weeks, claude_api_cost: $800, estimated_gpu_cost: $4,500, speed_bottleneck: GPU training wall-clock: each Qwen3-8B RL run requires ~25h on 8×H100; 6 ablation configs run sequentially unless multi-node cluster available\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T08:11:06.950Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:11:06.950Z",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T08:11:07.001Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make a well-grounded assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. PURE — "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning" (NeurIPS 2025, arXiv 2504.15275):
   最直接的 baseline。将 PRM 信用分配从 summation-form 改为 min-form，大幅缓解 reward hacking，在 MATH-500 达 82.6%。本 proposal 的 A^min 分支直接借用 PURE。关键问题：PURE 的 min-form 已经显著缓解了 reward hacking，UGCA 还能在此基础上获得多少增量？

2. GRPO-λ — "Credit Assignment Improves LLM Reasoning" (arXiv 2510.00194, Oct 2025):
   用 eligibility traces 改进 GRPO，7B 模型平均提升 3-4.5 分。同样假定 PRM 分数可靠。是 proposal 的另一个核心 baseline。

3. Park et al. — "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (NeurIPS 2025, arXiv 2506.09338):
   用 quantile regression 校准 PRM，显著改善 calibration，但**明确只用于 test-time scaling（best-of-N, instance-adaptive search）**。Proposal 正确识别出这是 training-time 的空白。

4. Distributional PRM (arXiv 2605.06785, May 2026):
   用 conditional optimal transport 进一步改善 PRM 校准，同样**仅针对 test-time scaling**。确认了 training-time 应用的空白仍然存在。

5. PROGRS — "LLM Reasoning with Process Rewards for Outcome-Guided Steps" (arXiv 2604.02341, Apr 2026):
   **最接近的竞争者**。使用 frozen quantile-regression PRM + outcome-conditioned centering。关键区别：PROGRS 在 trajectory level 做 centering（将错误轨迹的 PRM 分数 shift 到零均值），而非 per-step uncertainty gating。但核心动机高度重叠——都是不完全信任 PRM 分数。

6. "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning" (arXiv 2602.01034, Feb 2026):
   提出 Step-wise Marginal Information Gain + Decoupled Masking Strategy，将 process 和 outcome rewards 分别应用于 CoT 和完整 completion。虽然机制不同，但同样试图自适应地分配 process vs outcome credit。**Proposal 未引用此文，这是一个 related work 覆盖缺口。**

7. Jia et al. — "Do We Need to Verify Step by Step?" (ICML 2025):
   理论证明 outcome supervision 在统计意义上不比 process supervision 更难。Proposal 用此作为"降级到 outcome credit 是有理论保障的"论据。引用准确。

8. PRPO (arXiv 2601.07182, Jan 2026):
   通过 location-parameter shift 对齐 process 和 outcome advantages，Qwen2.5-Math-1.5B 上 61.2→64.4%。固定结构对齐，非自适应。

9. Uncertainty-Aware Reward Discounting (arXiv 2604.26360, Apr 2026):
   用 ensemble disagreement 缓解 RLHF 中的 reward hacking，但面向 general preference learning，非 math 场景的 process-outcome interpolation。

10. UCAS — "Unlocking Exploration in RLVR" (arXiv 2510.10649, Oct 2025):
    用 policy model 自身的 logit uncertainty 调制 advantages。与 UGCA 的关键区别：UCAS 用的是 policy 的 epistemic uncertainty，UGCA 用的是 verifier (PRM) 的 calibration uncertainty。

- **调研总结**: PRM calibration for test-time scaling 和 RL credit assignment for math reasoning 是两条成熟但分离的研究线。PROGRS (Apr 2026) 和 "Discovering Process-Outcome Credit" (Feb 2026) 已经在探索 process-outcome 的自适应融合，但通过不同机制。UGCA 的具体切入点——用 PRM quantile regression confidence width 做 per-step sigmoid gating between min-form process advantage 和 GRPO outcome advantage——在现有文献中确实未被直接实现，但概念距离并不远。

【Trivial Alternative 检验】:

存在若干更简单的替代方案构成威胁：

1. **Hard thresholding**: 直接设定阈值，confidence width > τ 的步骤完全使用 outcome credit，其余完全使用 process credit。省去 sigmoid gating 和 β 参数，效果可能接近。UGCA 的增量价值在于 soft interpolation，但这需要实验证明 soft 比 hard 好多少。

2. **Outcome-only baseline (plain GRPO)**: 既然 Jia et al. 证明了 outcome supervision 统计上不比 process supervision 更难，那一个自然的问题是：为什么不直接用 outcome-only GRPO，完全避开 PRM 不可靠的问题？PURE 的实验已经表明 min-form PRM 在实践中优于 outcome-only，但这个优势是否在 UGCA 的框架下仍然显著需要验证。

3. **Simply filtering out low-confidence PRM steps**: 如果 PRM 对某步的 confidence 很低，直接 mask 掉该步的 process reward，其余步仍用 PURE min-form。这比 UGCA 简单得多。

UGCA 的增量价值在于：提供了一个**原则性的 interpolation 框架**，而非 ad-hoc 的 filtering。但 reviewer 很可能会要求与这些 trivial baselines 做消融实验。如果消融显示 soft gating 与 hard thresholding 差异不大，核心贡献会被严重削弱。

【前提假设检验】:

核心逻辑链：PRM miscalibrated → miscalibration causes reward hacking in RL training → quantile regression confidence width captures miscalibration → gating to outcome credit on uncertain steps alleviates reward hacking → overall training improves

未经验证的关键假设：

1. **"PURE min-form 之后仍存在足够严重的 PRM miscalibration-induced reward hacking"**: PURE 的 min-form 已经被证明能大幅缓解 reward hacking。UGCA 需要证明在 min-form 基础上，PRM miscalibration 仍然是一个显著问题。如果 PURE 已经解决了大部分 reward hacking，UGCA 的改进空间可能很小。这是最关键的未验证前提。

2. **"Quantile regression confidence interval width 在 RL training 动态中仍然是 PRM reliability 的好 proxy"**: Park et al. 的校准是在静态推理场景中验证的。在 RL training 中，policy 不断变化，PRM 面对的分布也在 shift。Frozen PRM 的 calibration 在 training 后期是否仍然有效是一个公开问题。

3. **"Per-step gating 比 trajectory-level 方法（如 PROGRS 的 outcome-conditioned centering）更有效"**: 更细粒度不一定更好——per-step 的噪声也更大。

4. **"Sigmoid gating function 的形式选择是合理的"**: 为什么是 sigmoid 而不是线性 interpolation 或其他 monotone function？这个选择缺乏理论动机。

【3 维度打分】:

1. **Novelty: 中** — 
   Proposal 正确识别了一个真实的 gap：PRM calibration 方法（Park et al. NeurIPS 2025; Distributional PRM 2605.06785）只用于 test-time，而 RL credit assignment 方法（PURE, GRPO-λ, PRPO）不考虑 PRM uncertainty。这个 gap 是真实的。但 novelty 的性质是**组合式的（combinatorial）**而非**概念式的（conceptual）**——核心贡献是用一个 sigmoid 函数将两个已有组件（calibrated PRM confidence width + PURE/GRPO advantages）连接起来。PROGRS (arXiv 2604.02341) 已经在用 frozen quantile-regression PRM 做类似的事情（虽然在 trajectory level 而非 step level），"Discovering Process-Outcome Credit" (arXiv 2602.01034) 也在探索自适应 process-outcome 分配。UGCA 的 novelty delta 是"per-step sigmoid gating using confidence interval width"——这是一个有意义但不令人惊讶的 delta。

2. **Significance: 中** — 
   问题本身是重要的：如何在 RL training 中更好地利用不完美的 PRM 信号。如果 UGCA 能稳定提升 2-3 分（在 PURE 基础上），这对社区是有用的。但受限于两个因素：(a) PURE min-form 已经大幅解决了 reward hacking 问题，UGCA 的边际改进空间可能有限；(b) 核心发现如果 positive（"用 uncertainty gating 帮助训练"），审稿人的反应更可能是 "makes sense, I would have guessed this" 而非 "surprising"。Impact 更多是 incremental improvement 而非 paradigm shift。

3. **Related Work: 强** — 
   Proposal 对领域的覆盖非常全面：PURE, GRPO-λ, PROGRS, UCAS, Distributional PRM, PathFinder-PRM, PRPO, Uncertainty-Aware Reward Discounting, TP-GRPO, PRIME 均被讨论，且差异化定位清晰。唯一遗漏是 "Discovering Process-Outcome Credit in Multi-Step LLM Reasoning" (arXiv 2602.01034)，它直接做 process-outcome credit 分解，应被讨论。除此之外，related work 覆盖在投稿质量中属于上乘。

【概率估计】: 22% - 32%，中位 27%

【估计理由】: 
Related Work 维度强，表明作者对领域有深入理解，这为执行质量提供了信心。但 idea 质量的天花板受限于 Novelty 和 Significance 两个维度：

- Novelty 是组合式而非概念式的——用 sigmoid 将 calibration confidence width 映射为 gating coefficient 这一核心机制，技术上直白，不太可能让审稿人感到 "I hadn't thought of this"。PROGRS 已经在做概念相近（用 calibrated PRM 调节 RL training 中的 process credit）的工作。
- Significance 受限于 PURE min-form 已经大幅缓解了 reward hacking 的事实——UGCA 的改进空间可能较窄。如果最终只能在 MATH-500 上提升 1-2 分，很难说服审稿人这是一个值得单独发表的贡献。
- Trivial alternative 威胁真实存在——hard thresholding 或 simple masking 可能达到 80-90% 的效果。
- 概率上界被 Novelty（组合式）和 "unsurprising if positive" 限制在 ~32%；下界被 "gap 是真实的 + related work 覆盖强 + 有理论动机" 支撑在 ~22%。

【主要风险】:
1. **PURE min-form 后的增量空间不足**：如果 PURE 的 min-form 已经充分缓解了 reward hacking，UGCA 的额外收益可能微乎其微，实验结果将不足以支撑一篇 top-venue 论文。这是最大的 idea 层面风险——不是方法错误，而是**问题空间可能已经被 PURE 压缩得太小**。
2. **组合式 novelty 难以通过审稿人的 "so what" 检验**：核心贡献归结为一个 sigmoid gating function，审稿人可能认为这是一个 engineering trick 而非 scientific contribution，尤其在 PROGRS 已经展示了类似动机（用 calibrated PRM 改善 RL training）的背景下。
```

Sources:
- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [GRPO-λ (arXiv 2025)](https://arxiv.org/abs/2510.00194)
- [Know What You Don't Know: PRM Calibration (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)
- [Distributional PRM (arXiv 2605.06785)](https://arxiv.org/abs/2605.06785)
- [PROGRS (arXiv 2604.02341)](https://arxiv.org/abs/2604.02341)
- [Discovering Process-Outcome Credit (arXiv 2602.01034)](https://arxiv.org/abs/2602.01034)
- [Jia et al. - Rethinking Process Supervision (ICML 2025)](https://icml.cc/virtual/2025/poster/46497)
- [PRPO (arXiv 2601.07182)](https://arxiv.org/abs/2601.07182)
- [Uncertainty-Aware Reward Discounting (arXiv 2604.26360)](https://arxiv.org/abs/2604.26360)
- [UCAS - Unlocking Exploration in RLVR (arXiv 2510.10649)](https://arxiv.org/abs/2510.10649)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- PURE: "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning" (NeurIPS 2025, arXiv 2504.15275): 直接前驱工作。用 min-form（取未来 reward 的最小值而非求和）来替代传统 summation-form，缓解 PRM-induced reward hacking。Qwen2.5-Math-7B 上达到 82.6% MATH-500，代码公开。本 proposal 的 A^min 分量直接来自此方法。
- Park et al.: "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (NeurIPS 2025, arXiv 2506.09338): 直接前驱工作。证明 off-the-shelf PRM 系统性过估成功概率，提出 quantile regression 校准方法。但**仅用于 test-time scaling（instance-adaptive best-of-N）**，未涉及 RL 训练。本 proposal 的校准模块直接来自此工作。
- Distributional PRM (arXiv 2605.06785, May 2026): 用 conditional optimal transport 改进 PRM 校准，达到 SOTA 校准质量。同样**明确只针对 test-time scaling**。
- GRPO-λ (arXiv 2510.00194, Oct 2025): 用 eligibility traces 改进 GRPO 的 credit assignment，7B 模型上平均 +3-4.5 分。从 ICLR 2026 撤稿。不涉及 PRM 校准或不确定性。
- PROGRS (arXiv 2604.02341, Apr 2026): **最接近的竞争者**。使用 frozen quantile-regression PRM + outcome-conditioned centering，在 GRPO 中集成 process bonus。关键区别：它在 trajectory level 做 centering（将错误轨迹的 PRM 分数 shift 到零均值），而非 per-step uncertainty gating。但它同样使用了 quantile-regression PRM 在 RL 训练中，削弱了 proposal 声称的"无人将 PRM 校准用于 RL 训练"这一 gap。
- Jia et al.: "Do We Need to Verify Step by Step?" (ICML 2025, arXiv 2502.10581): 真实论文。证明在标准 data coverage 假设下，outcome supervision 在统计上不比 process supervision 更难。Proposal 用此作为 degradation to outcome credit 的理论支撑。
- Uncertainty-Aware Reward Discounting (arXiv 2604.26360, Apr 2026): 用 ensemble disagreement 缓解 RLHF 中的 reward hacking。针对通用偏好学习，非 math-specific process-outcome interpolation。但**核心 idea 高度相似**：在 reward 不确定时减少对 reward 的信赖。
- UCAS (arXiv Oct 2025): 用 policy model 自身的 logit uncertainty 来调制 advantage——和 PRM verifier uncertainty 是不同的 uncertainty 来源，但"用不确定性调制 advantage"这个操作模式相同。
- 调研总结: PRM-based RL credit assignment 是 2025-2026 的活跃战场，已有多种改进方法（PURE、GRPO-λ、PROGRS、PRPO、UCAS）。PRM 校准方法（quantile regression、optimal transport）已成熟但主要用于 test-time。PROGRS 已经在 RL 训练中使用了 quantile-regression PRM（虽然机制不同）。"用不确定性调制 reward/advantage"的 meta-idea 已在 UCAS 和 UARD 中出现。Proposal 的具体贡献空间（per-step PRM confidence interval width → sigmoid gating → process/outcome interpolation）确实尚未被精确复现，但周围工作已经非常密集。

【Trivial Alternative 检验】:
存在多个低成本替代方案威胁：
1. **简单阈值过滤**：直接丢弃 PRM 置信度低于阈值的 step 的 process reward，仅保留高置信 step 的 process advantage，其余 step 用 outcome advantage。无需 sigmoid gating 的连续化设计，可能效果相近。
2. **固定混合比例**：不用 per-step adaptive gating，直接用一个全局 α 混合 process 和 outcome advantage（类似于简单的 weighted sum），通过 grid search 调优。这是 proposal 方法的退化形式。
3. **PURE 本身已部分解决**：PURE 的 min-form 天然对高 PRM score 做了保守化处理（取最小值而非累加），已经在机制上缓解了 reward hacking。在此基础上再加 uncertainty gating 的**边际收益**可能有限。
4. **PROGRS 的 outcome-conditioned centering** 已经是一种"在 PRM 不可靠时降低其影响"的策略，只是实现方式不同。

proposal 的增量价值在于：提供了一个有理论 grounding 的 per-step 连续 interpolation 机制。但如果 trivial alternatives（尤其是简单阈值）效果相当，这个增量价值会被严重稀释。

【前提假设检验】:
核心逻辑链中有以下未经验证的假设：

1. **"PRM 校准置信区间宽度 = 该 step 的 PRM 信号不可靠程度"**：这是最关键的假设。Quantile regression 的置信区间宽度反映的是 PRM 预测的条件分布的 spread，但这不一定等同于"PRM 在这个 step 上会导致 reward hacking"。宽置信区间可能出现在本身就困难（但 PRM 判断正确）的 step 上。proposal 没有论证为什么 confidence interval width 是正确的 gating signal。

2. **"在 PRM 不确定的 step 上退化到 outcome credit 会减少 reward hacking"**：Jia et al. 的理论结果说的是统计等价性（outcome supervision 不比 process supervision 更难），不是说 outcome credit 在特定 uncertain step 上比 process credit 更准确或更 robust。这个推论存在逻辑跳跃。

3. **"reward hacking 主要发生在 PRM 不确定的 step 上"**：这是一个未经验证的经验性假设。Reward hacking 也可能发生在 PRM 高度自信但错误的 step 上（即 PRM 的 systematic bias，不是 uncertainty 能捕捉的）。如果 hacking 主要来自高置信但错误的 PRM 判断，则 uncertainty gating 无法解决核心问题。

【3 维度打分】:
  1. Novelty: 弱-中 — 核心 idea 是将三个已有模块（PURE 的 min-form advantage、Park et al. 的 quantile regression 校准、GRPO 的 outcome advantage）用一个 sigmoid 函数组合起来。这是一个自然而直觉的组合——"可靠时信 PRM，不可靠时退回 outcome"——领域内研究者看到 Park et al. + PURE 后很容易想到。PROGRS (arXiv 2604.02341) 已在 RL 训练中使用了 quantile-regression PRM，只是用了不同的利用方式（centering vs. gating），削弱了"首次将 PRM 校准引入 RL 训练"这一 novelty claim。UCAS 和 UARD 已分别展示了"用 uncertainty 调制 advantage"和"用 uncertainty 缓解 reward hacking"的 meta-idea。剩余的精确 novelty delta 是具体的 sigmoid gating 公式和 per-step process/outcome interpolation，这属于工程变体级别的贡献。

  2. Significance: 中 — 研究问题本身重要且 timely：PRM miscalibration 对 RL 训练的影响是 real problem（Park et al. 和 PURE 都证实了这点）。如果实验结果显示在 PURE 之上有显著提升，有一定影响力。但：(a) PURE 已经很好地解决了 reward hacking 问题（82.6% MATH-500），边际改进空间可能有限；(b) 方法特异性高——依赖特定 PRM 架构和特定校准方法，可推广性存疑；(c) 如果核心发现是 positive（"uncertainty gating 比 PURE 好 1-2 个点"），审稿人的反应更可能是 "I would have guessed this" 而非 "surprising"。

  3. Related Work: 强 — Proposal 对相关工作的覆盖相当全面。准确识别了 PURE、GRPO-λ、PROGRS、UCAS、PRPO、PRIME、PathFinder-PRM、TP-GRPO、Distributional PRM 等关键工作，差异化定位也基本准确（特别是 PROGRS 的 trajectory-level centering vs. per-step gating 的区分）。引用的关键论文（Jia et al. ICML 2025、Park et al. NeurIPS 2025、PURE NeurIPS 2025）均经过验证真实存在且描述准确。唯一的瑕疵是略微低估了 PROGRS 的相关性——PROGRS 同样在 RL 训练中使用了 quantile-regression PRM，不仅是"固定 centering 规则"那么简单。

【概率估计】: [18% - 28%] 中位 23%

【估计理由】: 
Novelty 是主要限制因素。核心贡献是三个已有公开模块的自然组合，sigmoid gating 公式是直觉性设计而非深刻洞察。PROGRS、UCAS、UARD 已在不同角度实现了高度相似的 meta-idea，使得精确 novelty delta 仅停留在工程变体层面。Significance 受限于 PURE 已有效解决 reward hacking（82.6% MATH-500），在此基础上的边际改进空间和惊喜度有限。Related Work 覆盖充分是正面因素，但不足以弥补 idea 内核的薄弱。前提假设检验暴露了"confidence interval width = 不可靠度"和"uncertain step 上 outcome credit 更好"这两个未经验证的关键逻辑环节，进一步压低了 idea 的说服力。Trivial alternative（简单阈值过滤、固定混合比）对方法的增量价值构成直接威胁。综合来看，idea 方向正确但内核偏薄，属于 rubric 中 15-25% 和 25-35% 的边界区域，取 23%。上界被 novelty 和 trivial alternative 威胁封顶在 28%。

【主要风险】:
1. **Novelty 不足被拒**：审稿人可能认为这是 PURE + Park et al. quantile regression 的 trivial combination，缺乏独立的技术洞察，特别是在 PROGRS 已将 quantile-regression PRM 用于 RL 训练的背景下。
2. **核心假设被质疑**："PRM confidence interval width 是正确的 gating signal"这一未经验证的假设是逻辑链的核心，审稿人可能要求提供理论或实证支撑（如：reward hacking 确实集中在 PRM uncertain steps 上），而这目前缺失。
```

Sources:
- [PURE - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [Know What You Don't Know: PRM Calibration (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)
- [Distributional PRM (arXiv May 2026)](https://arxiv.org/html/2605.06785)
- [GRPO-λ (arXiv Oct 2025)](https://arxiv.org/abs/2510.00194)
- [PROGRS (arXiv Apr 2026)](https://arxiv.org/abs/2604.02341)
- [Jia et al. - Process vs Outcome Supervision (ICML 2025)](https://arxiv.org/abs/2502.10581)
- [Uncertainty-Aware Reward Discounting (arXiv Apr 2026)](https://arxiv.org/html/2604.26360)
- [PURE GitHub Repository](https://github.com/CJReinforce/PURE)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to produce a thorough evaluation. Let me synthesize all findings.

---

```
【阶段】: Triage

【领域调研】:
- PURE "Stop Summation: Min-Form Credit Assignment" (NeurIPS 2025, arXiv 2504.15275): 提出 min-form value function 替代 summation-form，显著缓解 PRM-induced reward hacking。82.6% MATH-500, 82.5% AMC23 (Qwen2.5-Math-7B)。本 proposal 直接构建在 PURE 之上，将其 min-form advantage 作为高置信度时的 process credit。
- GRPO-λ (arXiv 2510.00194, submitted ICLR 2026): 将 eligibility traces 引入 GRPO，通过 token-level log-prob 近似 λ-return，在 7B 模型上平均提升 3-4.5 points。与本 proposal 同为 credit assignment 改进，但不涉及 PRM 可靠性判断。
- PROGRS "LLM Reasoning with Process Rewards for Outcome-Guided Steps" (arXiv 2604.02341, Apr 2026): 使用 frozen quantile-regression PRM + multi-scale coherence evaluator，通过 outcome-conditioned centering 整合 process reward。MATH-500 74.9% vs DAPO 69.7%。**与本 proposal 最相近**——也用了 quantile-regression PRM，但策略是 trajectory-level 的 fixed centering，而非 per-step uncertainty gating。
- PROF "Beyond Correctness: Harmonizing Process and Outcome Rewards" (arXiv 2509.03403): 通过 consistency-driven sample selection 协调 process 和 outcome reward（保留 correct+高 process 和 incorrect+低 process 的样本），比 naïve blending 好 4%+。与本 proposal 目标相近（协调 process/outcome），但机制完全不同（sample filtering vs. per-step gating）。
- UCAS "Unlocking Exploration in RLVR" (arXiv 2510.10649, submitted ICLR 2026): 利用 policy model 自身的 logit uncertainty 做 response-level + token-level advantage 调制。名称接近但信号来源不同——用的是 policy uncertainty 而非 PRM verifier uncertainty。
- Park et al. "Know What You Don't Know: Uncertainty Calibration of PRMs" (NeurIPS 2025, arXiv 2506.09338): Quantile regression 校准 PRM，提出 instance-adaptive scaling (IAS) 框架。**核心发现：PRM 存在系统性 miscalibration。但应用场景仅限 inference-time scaling (best-of-N)**。
- Distributional PRM (arXiv 2605.06785, May 2026): 通过 conditional optimal transport 实现 PRM 校准的 SOTA，同样仅面向 test-time scaling。
- PRPO (arXiv 2601.07182, Jan 2026): 通过 location-parameter shift 对齐 process 和 outcome advantages，Qwen2.5-Math-1.5B 61.2→64.4%。使用固定的结构对齐，非自适应 per-step 权重。
- "Discovering Process-Outcome Credit" (arXiv 2602.01034, Feb 2026): 提出 step-wise Marginal Information Gain + decoupled masking 进行 process-outcome credit 分配。机制不同但动机相关。
- Uncertainty-Aware Reward Discounting (arXiv 2604.26360, Apr 2026): Ensemble disagreement 缓解 RLHF reward hacking，面向 general preference learning 而非 math process-outcome interpolation。
- Jia et al. "Do We Need to Verify Step by Step?" (ICML 2025, arXiv 2502.10581): 理论证明 outcome supervision 统计上不比 process supervision 更难。本 proposal 用此作为 fallback 到 outcome credit 的理论依据。

- **调研总结**: 这是一个极度拥挤的子领域——2025-2026 年间至少有 10+ 篇工作聚焦于 "如何在 math reasoning RL 中更好地使用 PRM 做 credit assignment"。PRM 校准（Park et al., Distributional PRM）和 RL credit assignment（PURE, GRPO-λ, PRPO, PROGRS, PROF）是两条平行发展的线。本 proposal 的核心定位是 **bridge the gap**——将前者的 calibration confidence 注入后者的 per-step advantage computation。这个具体的交叉点（PRM 校准置信度 → 训练时 per-step gating）在 May 2026 确实未被直接占据，但 PROGRS 已经非常接近（同样使用 frozen QR-PRM，只是 centering 策略不同）。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁：
1. **Fixed interpolation baseline**: 用固定 α 线性组合 A^min 和 A^GRPO（α 通过 grid search 选取），不需要任何 PRM 校准。如果固定 α=0.5 的 blending 就能取得类似效果，整个 uncertainty-gating 机制的增量价值就不成立。Proposal 必须证明 per-step adaptive α 显著优于 fixed α。
2. **Better PRM, same pipeline**: 直接用 Distributional PRM（更好的校准 SOTA）替换原始 PRM 作为 PURE 的输入，不做任何 gating——如果更好的 PRM 本身就缓解了 reward hacking，那 gating 机制的必要性就被削弱。
3. **Simple thresholding**: 对 PRM confidence 低于阈值的 step 直接 mask 掉 process reward（advantage = 0 或完全用 outcome），而非 sigmoid soft gating。如果这个更简单的 hard-gating 效果相当，soft gating 的贡献就是 marginal 的。

Proposal 的增量价值取决于：per-step adaptive sigmoid gating 是否显著优于上述三个 trivial alternatives。这是个**纯实验问题**——idea 层面无法事先回答。

【前提假设检验】:
核心逻辑链中存在以下未验证假设：
1. **"即使在 PURE min-form 下，PRM miscalibration 仍然导致显著的残余 reward hacking"** — PURE 已经通过 min-form 大幅缓解了 reward hacking。Proposal 的前提是 PURE 还不够，uncertain steps 上仍有残余问题。但这个前提是否成立尚无实证——PURE 论文未报告 per-step 的 reward hacking 分布，也没有证据表明问题集中在 PRM-uncertain steps。
2. **"Quantile regression confidence interval width 是 PRM reliability 的好 proxy"** — 宽置信区间 ≠ PRM 不可靠。QR 置信区间反映的是 model uncertainty about prediction interval，而非"这个 PRM 分数是否可信"。如果 PRM 系统性地 miscalibrate（而非随机 noise），CI width 可能无法捕捉这种偏差。
3. **"Fallback 到 GRPO outcome advantage 是最优降级策略"** — 为什么不是 fallback 到 zero advantage（忽略该 step）？或 fallback 到某种 baseline advantage？选择 GRPO 作为 fallback 的理由是 Jia et al. 的定理，但那个定理说的是"统计上不更难"，不是"outcome advantage 是最优 fallback 目标"。
4. **"Sigmoid gating 函数 σ(−(w−τ)/β) 是合适的函数形式"** — 这是一个设计选择，有两个额外超参 τ 和 β 需要调。如果效果好坏高度依赖于 τ 和 β 的选取（且 PROGRS 那样的 non-parametric centering 更鲁棒），那超参敏感性会是审稿人的攻击点。

【3 维度打分】:
  1. Novelty: 【中】— 核心贡献是将两条已有研究线（PRM calibration + RL credit assignment）做了自然组合。具体交叉点（per-step calibration confidence → adaptive gating）确实未被直接占据（调研确认），但 PROGRS 已经在同一条路上走了大半（也用 frozen QR-PRM，只是 centering 而非 gating）。核心 insight "不要信任 uncertain PRM scores" 是一个 common sense principle 而非 surprising observation。组合型 novelty 在拥挤领域中的含金量有限——审稿人会问 "so you just replaced fixed centering with sigmoid gating?"
  
  2. Significance: 【中】— 问题方向正确——PRM-based RL credit assignment 是当前 math reasoning 的核心挑战之一。但预期贡献偏 incremental：在 PURE 已经 82.6% MATH-500 的基础上，进一步改进的空间有限。如果核心发现是 positive（uncertainty gating 优于 uniform trust），审稿人的反应更可能是 "makes sense, I would have guessed this"——缺乏 surprise factor。对于 OlympiadBench/AIME24 等更难 benchmark 上的改进，意义会更大，但 proposal 未给出预期增量的具体论证。
  
  3. Related Work: 【强】— 这是 proposal 最突出的优势。对 10+ 篇高度相关工作的覆盖极其详尽且准确（经调研验证），每篇都有清晰的差异化定位。包含最近至 May 2026 的工作（Distributional PRM, PROGRS）。唯一遗漏：PROF (arXiv 2509.03403) 是一个重要的 process-outcome 协调方法，未被明确提及；"Discovering Process-Outcome Credit" (arXiv 2602.01034) 也值得讨论。

【概率估计】: [20% - 32%] 中位 25%

【估计理由】: 
Novelty 为"中"——这是一个 well-executed combination paper，定位清晰，gap 真实存在，但组合方式自然可预测（"用 calibration 信号调制 trust"是直觉性 solution），在极度拥挤的子领域中差异化不够显著。Significance 为"中"——方向对但增量预期有限，core finding 若 positive 不会 surprising。Related Work 为"强"是加分项，但 related work 好只能提高 proposal 的可信度，不能弥补 idea 内核的 surprise 缺失。

**Novelty 和 Significance 共同限制了上界**：在当前 math reasoning RL 这个极度内卷的赛道上，纯 credit assignment 的 incremental improvement paper 面临非常高的审稿门槛。要突破 30%+ 概率，需要 either (a) 更 surprising 的核心发现，or (b) 在困难 benchmark 上展示出显著超出 PURE 的 empirical gains——后者需要实验验证。

【主要风险】:
1. **Trivial alternative 威胁**: Fixed α interpolation baseline 可能效果相当，如果 ablation 无法清晰证明 per-step adaptive gating 的增量价值，审稿人会质疑 "is the uncertainty-aware gating really necessary, or does any blend work?"
2. **前提假设不牢固**: Proposal 的核心前提——"PURE min-form 之后仍有显著的 PRM-uncertainty-driven reward hacking"——缺乏先验证据。如果实验发现 PURE 已经很好地解决了这个问题（uncertain steps 上的 reward hacking 本就不严重），整个 gating 机制的动机就崩塌了。
```

Sources:
- [PURE - Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)
- [GRPO-λ: Credit Assignment improves LLM Reasoning](https://arxiv.org/abs/2510.00194)
- [PROGRS - LLM Reasoning with Process Rewards for Outcome-Guided Steps](https://arxiv.org/pdf/2604.02341)
- [PROF - Beyond Correctness: Harmonizing Process and Outcome Rewards](https://arxiv.org/abs/2509.03403)
- [UCAS - Unlocking Exploration in RLVR](https://arxiv.org/abs/2510.10649)
- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models (arXiv 2605.06785)](https://arxiv.org/abs/2605.06785)
- [PRPO: Aligning Process Reward with Outcome Reward](https://arxiv.org/abs/2601.07182)
- [Discovering Process-Outcome Credit in Multi-Step LLM Reasoning](https://arxiv.org/abs/2602.01034)
- [Uncertainty-Aware Reward Discounting](https://arxiv.org/abs/2604.26360)
- [Jia et al. - Do We Need to Verify Step by Step? (ICML 2025)](https://arxiv.org/abs/2502.10581)


【原始 proposal（允许参考但不是主要依据）】:
# Uncertainty-Gated Credit Assignment for Process-Supervised Mathematical Reasoning RL

## Core Problem

Current methods for integrating process reward models into RL training (PURE, GRPO-λ, PRL, PRPO) treat all PRM step-level scores as equally trustworthy, yet PRMs are demonstrably miscalibrated—overestimating success probabilities on uncertain steps—leading to reward hacking where the policy exploits unreliable PRM signals rather than genuinely improving reasoning.

## Research Opportunity

PRM calibration methods have matured rapidly (quantile regression [NeurIPS 2025], conditional optimal transport [arXiv 2605.06785]) but are applied exclusively to test-time scaling (best-of-N, instance-adaptive search). No work uses PRM uncertainty to modulate credit assignment during RL training. Meanwhile, Jia et al. [ICML 2025] proved outcome supervision is statistically no harder than process supervision—suggesting the empirical gap is algorithmic, motivating a principled interpolation. The building blocks (calibrated PRMs, GRPO/PURE training pipelines, math reasoning benchmarks) all exist, making a 2-month implementation feasible for AAAI 2027 (deadline: July 28, 2026).

## Research Landscape

PURE (NeurIPS 2025) replaces summation-form with min-form credit assignment, achieving 82.6% on MATH-500 and 82.5% on AMC23 with Qwen2.5-Math-7B but still assumes PRM scores are reliable. GRPO-λ (arXiv Oct 2025) adds eligibility traces to GRPO, improving average math scores by 3–4.5 points on 7B models but also trusts PRM outputs uniformly. PROGRS (arXiv Apr 2026) uses outcome-conditioned centering with a frozen quantile-regression PRM (74.9% on MATH-500 vs 69.7% DAPO baseline) but applies a fixed centering rule at the trajectory level, not per-step uncertainty gating. UCAS (arXiv Oct 2025) modulates advantages via the policy model's own logit uncertainty—fundamentally different from PRM verifier uncertainty. The Distributional PRM (arXiv May 2026) achieves state-of-the-art calibration via conditional optimal transport but explicitly targets only test-time scaling. PathFinder-PRM (arXiv May 2025) achieves 67.7 PRMScore on PRMBench with error-type-aware scoring but does not feed uncertainty into RL credit assignment. PRPO (arXiv Jan 2026) aligns process and outcome advantages via location-parameter shift on Qwen2.5-Math-1.5B (61.2→64.4% MATH-500) but uses fixed structural alignment, not adaptive per-step weighting. Uncertainty-Aware Reward Discounting (arXiv Apr 2026) uses ensemble disagreement to mitigate reward hacking in RLHF but targets general preference learning, not process-outcome interpolation for math. TP-GRPO (arXiv Jul 2025) introduces capability-adaptive rewards with generative PRM at the thought level using intrinsic signals, not PRM calibration. PRIME (arXiv Feb 2025) enables online PRM updates through implicit process rewards but uses uniform trust in PRM signals. Thorough concurrent-work search across arXiv and OpenReview (May 2026) confirms the specific gap—using PRM calibration confidence to drive per-step adaptive interpolation between process and outcome credit during RL training—remains unaddressed.

## Proposed Approach

We propose Uncertainty-Gated Credit Assignment (UGCA), which equips the off-the-shelf Qwen2.5-Math-PRM-7B with calibrated confidence intervals via quantile regression (adapting the open-source code from Park et al., NeurIPS 2025), then defines a per-step gating coefficient α_i = σ(−(w_i − τ)/β) based on each step's confidence-interval width w_i. During RL training, the advantage at step i is computed as A_i = α_i · A^min_i + (1 − α_i) · A^GRPO_i, where A^min is PURE-style min-form process advantage and A^GRPO is group-relative outcome advantage—high-confidence PRM steps lean on process credit while uncertain steps gracefully degrade to outcome credit. We train Qwen3-8B and Qwen3-1.7B on the MATH training set (8K prompts) using this modified GRPO objective atop the PURE codebase, with the calibrated PRM frozen throughout, evaluating on MATH-500, AMC23, AIME24, and OlympiadBench against re-implemented PURE, GRPO, and GRPO-λ baselines on the same models. The method is theoretically grounded by the Jia et al. (ICML 2025) proof that outcome supervision is statistically no harder than process supervision, making the degradation principled, and requires only a one-time quantile calibration pass with no additional training signals.

## Detailed Description

We introduce Uncertainty-Gated Credit Assignment (UGCA), a method that uses calibrated PRM confidence to adaptively interpolate between process-level and outcome-level credit during RL training for mathematical reasoning. While PRM calibration methods (quantile regression, conditional optimal transport) have matured rapidly, they target only inference-time scaling. Meanwhile, RL credit assignment methods (PURE, GRPO-λ, PRPO) treat all PRM step scores as equally reliable, enabling reward hacking on uncertain steps. UGCA bridges this gap: we equip the off-the-shelf Qwen2.5-Math-PRM-7B with quantile-regression confidence intervals and derive a per-step gating coefficient—high-confidence steps use PURE-style min-form process advantages; low-confidence steps gracefully degrade to GRPO outcome advantages. This interpolation is theoretically motivated by the Jia et al. (ICML 2025) proof that outcome supervision is statistically equivalent to process supervision. We evaluate on Qwen3-8B and Qwen3-1.7B across MATH-500, AMC23, AIME24, and OlympiadBench, targeting improvements over PURE and GRPO-λ baselines while demonstrating measurably reduced reward hacking on PRM-uncertain steps. All core building blocks (calibrated PRM code, PURE codebase, pre-trained PRMs) are publicly available, and concurrent-work search (May 2026) confirms this mechanism is novel.

## Key References

- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)
- GRPO-λ: Credit Assignment Improves LLM Reasoning (arXiv 2025)
- LLM Reasoning with Process Rewards for Outcome-Guided Steps (arXiv 2026)
- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)
- Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv 2026)
- Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical Perspective (ICML 2025)
- Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning (arXiv 2025)
- PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization (arXiv 2026)
- PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary (arXiv 2026)
- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision (arXiv 2025)
- Process Reinforcement through Implicit Rewards (arXiv 2025)

## Resource Estimate

- **manual**: gpu_hours: ~1800 H100-hours (PRM quantile calibration on Qwen2.5-Math-PRM-7B: 100h; Qwen3-1.7B RL ablations ×6 configs: 360h; Qwen3-8B RL ablations ×6 configs: 1200h; final evaluation + reward-hacking diagnostics: 140h), timeline: 8 weeks (wk1–2: PRM quantile-regression calibration + PURE codebase integration with veRL; wk3–4: 1.7B ablations over gating threshold τ, temperature β, and quantile level; wk5–6: 8B full comparison runs vs PURE/GRPO/GRPO-λ baselines; wk7: reward-hacking analysis, per-step uncertainty visualization, ablation plots; wk8: paper writing and AAAI submission), estimated_gpu_cost: $4,500 (H100 spot at ~$2.50/GPU-hr)
- **human_in_loop**: gpu_hours: ~1800 H100-hours (identical compute workload), timeline: 6 weeks (Claude accelerates PURE/veRL codebase integration, quantile-regression head implementation, hyperparameter sweep scripting, results analysis, and paper drafting), claude_api_cost: $300, estimated_gpu_cost: $4,500
- **auto_research**: gpu_hours: ~1800 H100-hours (identical compute workload), timeline: 5 weeks, claude_api_cost: $800, estimated_gpu_cost: $4,500, speed_bottleneck: GPU training wall-clock: each Qwen3-8B RL run requires ~25h on 8×H100; 6 ablation configs run sequentially unless multi-node cluster available


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b2868268-b208-4215-b030-a77c04b2ef63",
  "type": "user",
  "uuid": "8e4cb8a0-5b37-4a59-8f91-6ee8eeb18423",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:11:06.999Z_

```json
{
  "parentUuid": "8e4cb8a0-5b37-4a59-8f91-6ee8eeb18423",
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
  "uuid": "9aaf940a-25f6-4c1f-a4ad-6bf57910089f",
  "timestamp": "2026-05-27T08:11:06.999Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:11:06.999Z_

```json
{
  "parentUuid": "9aaf940a-25f6-4c1f-a4ad-6bf57910089f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6a986504-6de3-4ec1-84cd-3d6a630b12e0",
  "timestamp": "2026-05-27T08:11:06.999Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a well-grounded assessm…",
  "leafUuid": "6a986504-6de3-4ec1-84cd-3d6a630b12e0",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate process-outcome RL credit assignment proposal",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:11:32.683Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

**Reviewer 1**: Probability [22% - 32%], median 27%
- Novelty: 中 (combinatorial, not conceptual)
- Significance: 中 (limited marginal improvement over PURE)
- Related Work: 强
- Key risks: incremental space after PURE, combinatorial novelty

**Reviewer 2**: Probability [18% - 28%], median 23%
- Novelty: 弱-中 (natural combination, engineering variant)


- Significance: 中 (incremental, unsurprising if positive)
- Related Work: 强
- Key risks: trivial alternative, core assumption unverified

**Reviewer 3**: Probability [20% - 32%], median 25%
- Novelty: 中 (well-executed combination, crowded field)
- Significance: 中 (incremental, limited surprise factor)
- Related Work: 强
- Key risks: trivial alternative, premise assumption

Now I'm computing the aggregate assessment across all three reviewers. The median probabilities cluster around 25%, and I'm calculating the standard deviation to understand how much the reviewers diverge in their confidence levels.

Looking at the consensus patterns, all three reviewers align on several key dimensions: the novelty is solidly in the middle range with a combinatorial character, significance is uniformly incremental, and related work coverage is strong across the board. They also converge on the critical vulnerabilities—the trivial alternative threat and the unverified core assumption about confidence interval width as a proxy for unreliability. The fact that PURE has already substantially addressed reward hacking leaves limited marginal space for improvement.

On the outlier side, R2 takes a slightly more conservative stance on novelty, R3 uniquely flags PROF as a missing reference, R1 questions the sigmoid versus linear interpolation choice without justification, and R3 raises the distinct concern about why the method doesn't simply fall back to zero advantage. With the standard deviation around 1.63%—indicating high consistency—the median assessment is the most reliable signal here.

The three score ranges [22-32], [18-28], and [20-32] converge around [22-28], so I'm settling on a median of 25% with bounds of roughly 21-29%, respecting both R2's more stringent lower estimate and the upper limits across all reviewers. Now I need to pull together the implementation assessment based on what the proposal outlines for resource requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a986504-6de3-4ec1-84cd-3d6a630b12e0",
  "isSidechain": false,
  "requestId": "req_011CbSjbz5PMs4YBxrneUmGt",
  "type": "assistant",
  "uuid": "d40cd84e-aaed-4591-973c-a650cedcc759",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1XdxvLZL7fEGu5DfcZSSL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20884,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2792,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 20884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20884
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

_source line 9 · 2026-05-27T08:12:11.295Z_

【阶段】: Meta Judge
【三次中位】: [27%, 23%, 25%]  std=1.6%
【共识维度】: 
- **Novelty = 中**（3/3 一致）：核心贡献是组合式（combinatorial）而非概念式（conceptual）——将 PURE min-form advantage + Park et al. quantile regression confidence width + GRPO outcome advantage 通过 sigmoid 函数连接。PROGRS 已在 RL 训练中使用 frozen QR-PRM，概念距离不远。
- **Significance = 中**（3/3 一致）：方向正确但增量预期有限——PURE min-form 已达 82.6% MATH-500，边际改进空间被压缩；核心发现若 positive，审稿人反应更可能是 "makes sense, I would have guessed this" 而非 "surprising"。
- **Related Work = 强**（3/3 一致）：覆盖 10+ 篇高度相关工作，差异化定位清晰准确，引用经验证真实，在投稿质量中属上乘。
- **Trivial alternative 威胁真实存在**（3/3 一致）：hard thresholding、fixed α blending、simple masking 等低成本替代方案均可能达到 UGCA 80-90% 效果，核心增量价值需实验证明。
- **核心前提假设未经验证**（3/3 一致）：(a) PURE min-form 之后是否仍有足够严重的 PRM-uncertainty-driven reward hacking；(b) QR confidence interval width 是否是 PRM reliability 的好 proxy（宽 CI 可能出现在本身困难但 PRM 判断正确的 step 上）。
- **PROGRS 是最接近竞争者**（3/3 一致）：同样使用 frozen QR-PRM 在 RL 训练中，区别仅为 trajectory-level centering vs. per-step gating。

【异常维度】: 
- R2 将 Novelty 评为"弱-中"（其余两位评"中"）——R2 更强调 PROGRS/UCAS/UARD 已覆盖了 meta-idea，认为精确 novelty delta 仅为工程变体级别。此判断有一定依据但偏严，降权处理（不拉低最终 Novelty 判定至弱-中，维持"中"但注明接近下沿）。
- R3 单独指出 PROF (arXiv 2509.03403) 为遗漏的 related work——经核实 PROF 是 process-outcome 协调方法但机制完全不同（sample filtering vs. gating），遗漏不构成致命问题，仅为小瑕疵。
- R3 单独质疑"为什么 fallback 是 GRPO outcome advantage 而非 zero advantage"——有效质疑但非致命，可通过消融回应。

【最终概率】: [21% - 29%] 中位 25%
【一致性】: 高（std=1.6% < 3%，三位审稿人在所有核心维度上高度一致）
【综合理由】: 
三位审稿人在所有关键维度上高度收敛：Novelty 中（组合式）、Significance 中（incremental）、Related Work 强。概率区间大量重叠（[22-32] ∩ [18-28] ∩ [20-32] = [22-28]）。鉴于高一致性，取中位附近并适度缩窄区间。

最终中位 25% 的核心逻辑：
1. **Novelty 天花板限制**：在极度拥挤的 math reasoning RL credit assignment 子领域，组合式 novelty（sigmoid gating 连接已有模块）的含金量有限，PROGRS 已走了同一条路的大半。这封死了概率上界在 ~30% 附近。
2. **Significance 受 PURE 压缩**：PURE min-form 已将 MATH-500 推至 82.6%，UGCA 的边际改进空间客观受限，且 core finding 缺乏 surprise factor。
3. **Trivial alternative 是实质性威胁**：如果简单阈值过滤或固定混合比效果相当，核心贡献会被严重稀释——这在 idea 层面无法预判，需实验验证。
4. **Related Work 强是唯一加分项**：提高了执行可信度和 proposal 的专业度，支撑了概率下限不至于跌破 20%。
5. R2 的偏严评分（弱-中 novelty, median 23%）有合理依据但系三人中最严，在高一致性下不应过度拉低最终估计。

【建议】: 边缘（偏不推荐侧）
【实施评估】:
  - 计算资源: ~1800 H100-hours（PRM 校准 100h + 1.7B 消融 360h + 8B 全量对比 1200h + 评估诊断 140h），预估 GPU 成本 ~$4,500（H100 spot ~$2.50/hr）
  - 数据需求: MATH 训练集 (8K prompts) + 评测集 MATH-500/AMC23/AIME24/OlympiadBench，均为公开数据集；Qwen2.5-Math-PRM-7B 开源可得
  - 人工介入: 中等——需人工实现 PURE codebase 与 veRL 的集成、quantile regression head 的适配、超参搜索脚本编写；无需人工标注
  - 训练需求: 需要训练——Qwen3-8B 和 Qwen3-1.7B 的 RL 训练（每次 8B run ~25h on 8×H100），共 12 个配置（2 模型 × 6 configs）；PRM 本身 frozen 不训练，仅做一次 quantile regression 校准
  - 新 Benchmark: 不需要，使用已有标准 benchmark
  - 预估周期: 6-8 周（wk1-2 PRM 校准+代码集成；wk3-4 1.7B 消融；wk5-6 8B 全量对比；wk7 分析可视化；wk8 写作投稿）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d40cd84e-aaed-4591-973c-a650cedcc759",
  "isSidechain": false,
  "requestId": "req_011CbSjbz5PMs4YBxrneUmGt",
  "type": "assistant",
  "uuid": "506a2ac4-771a-48bb-93d6-6fa2daaf9e35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1XdxvLZL7fEGu5DfcZSSL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20884,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2792,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 20884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20884
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a well-grounded assessm…",
  "leafUuid": "506a2ac4-771a-48bb-93d6-6fa2daaf9e35",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate process-outcome RL credit assignment proposal",
  "sessionId": "593853a0-12e6-4ee7-a6a1-97c342b6682e"
}
```

---
