# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/34e9fd05-f4e1-48a0-9d1d-3b7276296e03.jsonl`
- **Structured JSON:** [`3eab7bf38487ddfea843.json`](../../sessions/3e/3eab7bf38487ddfea843.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:21:33.304Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:21:33.304Z",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide my evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" (arXiv:2603.06621, 2026):\n  最直接的竞争工作。提出三层诊断框架 (gradient attacks, RL-induced hacking, BoN overopt) 量化 PRM hackability。发现 AIME 上 PRM reward >0.9 但 ground-truth accuracy <4%，43% reward gains 来自 stylistic shortcuts。本 proposal 的实验框架（gradient attacks + RL-induced + BoN）几乎完全与此工作重叠，只是加了\"calibration\"这个变量。\n\n- Ackermann et al., \"Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards\" (arXiv:2602.18037, 2026):\n  Proposal 明确引用并声称要扩展的工作。证明 reward accuracy 与 loss landscape flatness 相关，提出 gradient regularization 作为防御。Proposal 声称将其 outcome-level gradient norm 分析扩展到 step-level Hessian spectral analysis，这是增量性扩展。\n\n- \"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\" (arXiv:2604.04648, 2026):\n  Proposal 中的 \"Caution\" baseline。使用 prediction error 驱动的 pessimism 来缓解 BoN 中的 reward hacking。已在理论 (linear setting) 和实验上证明 pessimism 有效。Proposal 的 CGSP 与此高度相似，区别在于 CGSP 用 calibration quality 来调制 pessimism 程度。\n\n- \"Learning a Pessimistic Reward Model in RLHF\" / PET (arXiv:2505.20556, 2025):\n  Proposal 中的另一个 baseline。使用 global pessimism（adversarially fine-tuned reward model）防御 reward hacking，不依赖 KL regularization。Proposal 声称 CGSP 优于 PET 的点在于\"step-level + calibration-grounded + adaptive\"，但 PET 的 global pessimism 已经相当有效。\n\n- \"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport\" (arXiv:2605.06785, May 2026):\n  **Proposal 未引用但高度相关的最新工作**。使用 conditional OT 对 PRM 进行 calibration，产生任意 quantile level 的 confidence bounds。在 MATH-500 和 AIME 上验证。该工作直接做了\"PRM calibration\"，虽然应用场景是 inference-time scaling 而非 reward hacking defense，但方法论和 PRM calibration 的技术手段高度重叠。\n\n- APRM: \"Adversarial Training for Process Reward Models\" (arXiv:2511.22888, 2025):\n  Proposal 中的 baseline。通过对抗训练增强 PRM 鲁棒性，+5.3pp OOD improvement。\n\n- \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" (arXiv:2506.09338):\n  直接研究 PRM 的 uncertainty calibration，发现 SOTA PRM 严重 miscalibrated，提出 quantile regression calibration。\n\n- PURE / \"Stop Summation: Min-Form Credit Assignment\" (arXiv:2504.15275, 2025):\n  通过改变 credit assignment 形式（sum → min）缓解 reward hacking，不需要改变 reward model 本身。\n\n- 调研总结: PRM hackability 和 PRM calibration 分别是 2025-2026 的活跃研究方向，已有大量工作分别攻克。本 proposal 试图\"bridge\"二者，但该桥接的核心洞察（calibration → robustness）在直觉上是显然的，且近期已有工作从不同角度部分覆盖了这一连接（如 Distributional PRM 做 calibration for better scaling, Caution 做 uncertainty-driven pessimism）。该领域竞争激烈，proposal 的 novelty delta 被快速压缩。\n\n\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁：\n\n1. **直接 post-hoc calibration + 现有 pessimism 方法**：Proposal 自己的实验设计中已经包含了 temperature scaling / Platt scaling 等 post-hoc 方法。如果 calibration 真的是关键因素，那么简单地对现有 PRM 做 temperature scaling 再搭配已有的 pessimism 方法（如 Caution 或 ensemble-min）就应该能获得大部分收益。CGSP 相对于这种简单组合的增量价值需要仔细论证，但 proposal 没有将\"calibrated PRM + existing defense\"作为 baseline。\n\n2. **Min-form credit assignment (PURE)**：完全不需要改动 reward model，仅改变 RL 中的 credit assignment 就能缓解 reward hacking。如果 PURE 的效果已经足够好，那么在 reward model 层面做复杂的 calibration-gated defense 是否 over-engineering？\n\n3. **CGSP 公式本身的简单性**：r̃_t = μ_t − α·σ_t/√c_t 本质上是 LCB (Lower Confidence Bound)，这是 bandit/RL 文献中极为经典的思路。区别仅在于用 calibration quality c_t 做分母——这算不算一个\"新方法\"，还是仅仅是 LCB 的一个 trivially different instantiation？\n\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的假设：\n\n1. **\"Calibration quality 是 hackability 的主要因果驱动因素\"**——这是整篇论文的核心 claim，但目前仅有相关性证据（proposal 自己也是先做 correlation study 再做 causal isolation）。然而，hackability 可能主要由 representation quality、training data distribution、model capacity 等因素决定，calibration 可能只是其中一个弱相关因素。如果 48 个配置的相关性实验结果显示 r < 0.29（即统计不显著），整篇论文的 story 将崩塌。\n\n2. **\"Per-step σ_t 是可靠的 uncertainty signal\"**——PRM 通常用 binary labels 训练（correct/incorrect step），其输出的 sigmoid probability 不一定携带有意义的 aleatoric/epistemic uncertainty 信息。仅仅通过 post-hoc calibration 不能将一个确定性模型变成一个有良好 uncertainty quantification 的模型。\n\n3. **\"Calibration Drift Detector 可在 RL 训练中实时计算 ECE\"**——ECE 的计算需要 ground-truth labels。在 RL 训练的 rollouts 中，如何获取 step-level ground truth？如果依赖 verifiable final answers (如 MATH)，那只有 outcome-level signal，无法计算 step-level ECE。这是一个实际可行性上的逻辑漏洞。\n\n4. **\"Post-hoc calibration provably preserves model representations\"**——Temperature scaling 确实不改变 representations，但 isotonic regression 和 conformal prediction 的\"representation preservation\"属性需要更仔细的论证。CKA verification 是一种弱验证。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心 idea（calibration → robustness）在直觉上是显然的：一个输出 well-calibrated probabilities 的 reward model 自然更难被 exploit，因为它的 scores 更准确地反映 true quality。\"Reward Under Attack\"(2603.06621) 已经建立了 PRM hackability 的系统分析框架；\"Caution\"(2604.04648) 已经在用 uncertainty-driven pessimism 防御 reward hacking；\"Distributional PRM\"(2605.06785) 已经在做 PRM calibration。本 proposal 的贡献主要是将这些已有 thread 做 systematic combination + 加上 causal framing，但组合本身缺乏 conceptual surprise。CGSP 公式 r̃_t = μ_t − α·σ_t/√c_t 是 LCB 的一个 straightforward variant。Step-level Hessian analysis 是 Ackermann et al. 的增量扩展。\n\n2. **Significance: 中** — \n   研究问题（PRM 为什么被 hack、如何防御）是 2025-2026 LLM reasoning 领域的核心问题之一，重要性不可否认。但本 proposal 的预期贡献是一个\"连接两个已有 thread\"的 bridge paper。如果核心实验结果是 positive（calibration 确实与 hackability 强相关），审稿人的反应大概率是\"makes sense, I would have guessed this\"而不是\"surprising\"。CGSP 作为防御方法，需要与已有的 5+ 种 defense 竞争 (Caution, PET, APRM, gradient regularization, PURE)，在拥挤的 solution space 中脱颖而出的难度很高。\n\n3. **Related Work: 中** — \n   Proposal 对主要 baseline (Caution, PET, APRM, gradient regularization) 的定位是清晰的，并准确描述了它们的局限性。但有一个重要遗漏：2026 年 5 月刚出的 \"Distributional Process Reward Models\"(arXiv:2605.06785) 直接做 PRM calibration 并在 MATH-500/AIME 上验证，与本 proposal 的方法论高度重叠。此外，PURE (min-form credit assignment) 作为一种完全不同思路的 defense 也应被讨论。\"Know What You Don't Know: Uncertainty Calibration of PRMs\" 直接研究 PRM uncertainty calibration，也需要被引用和比较。\n\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】: \n三个维度中 Novelty 是最大的限制因素。核心洞察（calibration helps robustness）缺乏 conceptual surprise，CGSP 是已有 pessimism 方法的 straightforward calibration-weighted variant，step-level Hessian 是 Ackermann et al. 的增量扩展。Significance 因研究问题的重要性而不低，但预期 finding 的 surprise level 不足以达到 35%+ 区间。领域竞争异常激烈（6 个月内至少 5 篇高度相关工作），novelty delta 被持续压缩。Proposal 形式上非常完善（48 configurations、causal isolation、4 contributions），但形式完善度不等于 idea 质量。按 rubric，这属于\"idea 方向站得住脚但内核薄弱\"到\"有实质内核但不 surprising\"的过渡区间。\n\n另需注意：**如果投稿目标确实是 CoRL (Conference on Robot Learning)，则存在严重的 venue mismatch 问题**——本 proposal 全部内容围绕 LLM 数学推理 (MATH-500, AIME, GRPO)，与 robotics 无任何关联，大概率会因 out-of-scope 被直接拒稿。若投稿目标是 NeurIPS/ICML/ICLR 等 ML 主会，则上述概率估计适用。\n\n【主要风险】: \n1. **Core insight 缺乏 surprise**：\"Well-calibrated reward model is harder to hack\" 在直觉上几乎是 tautological（calibration 意味着 scores 更准确 → 更准确的 scores 自然更难被 exploit）。审稿人可能质疑这一发现的 intellectual contribution 不足以支撑一篇顶会论文。\n2. **Solution space 拥挤，增量价值模糊**：CGSP 需要证明相对于\"简单 calibrate PRM + 已有 defense (如 Caution)\"的组合有显著优势，而 proposal 未将这一 trivial combination 作为 baseline，留下明显的审稿攻击面。\n```\n\nSources:\n- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)\n- [Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards](https://arxiv.org/abs/2602.18037)\n- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)\n- [Learning a Pessimistic Reward Model in RLHF (PET)](https://arxiv.org/abs/2505.20556)\n- [Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)\n- [Adversarial Training for Process Reward Models (APRM)](https://arxiv.org/abs/2511.22888)\n- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)\n- [Stop Summation: Min-Form Credit Assignment (PURE)](https://arxiv.org/abs/2504.15275)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\n现在我有了充分的调研基础，可以进行客观评估了。\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" (arXiv 2603.06621, March 2026):\n   - 与本 proposal 关系：**最直接的竞品**。该工作已经建立了三级诊断框架（静态扰动、梯度攻击、RL 诱导 hacking），在 AIME 上发现策略获得 >0.9 PRM reward 但真实准确率 <4%，43% 的 reward 增益归因于风格捷径。与 proposal 的 Contribution 1（correlation study across gradient attacks, RL-induced hacking, BoN overoptimization）高度重叠。\n\n2. \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" (NeurIPS 2025, arXiv 2506.09338):\n   - 与本 proposal 关系：**PRM 校准的开创性工作**。已证明 SOTA PRMs 严重 miscalibrated（过高估计部分推理步骤通向正确答案的概率），并提出基于分位数回归的校准方案。这是 proposal 校准维度的直接前置工作。\n\n3. \"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport\" (arXiv 2605.06785, May 2026):\n   - 最新 PRM 校准工作，使用条件最优传输学习完整的单调条件分位数函数，在 Brier score、ECE、weighted quantile loss 上显著优于未校准 PRM 和分位数回归。说明 PRM 校准领域正在快速进展。\n\n4. \"Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards\" — Ackermann et al. (arXiv 2602.18037, February 2026):\n   - proposal 明确引用并声称扩展此工作。原工作建立了 reward model 准确性与收敛点平坦度的理论联系，提出梯度正则化偏向平坦区域。Proposal 的 Contribution 3（step-level Hessian 分析）是对此的 step-level 推广。\n\n5. \"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\" (arXiv 2604.04648, April 2026):\n   - 已在 BoN 场景中使用悲观主义防御 reward hacking：训练 error model，用 prediction error 降低非典型响应的 reward 估计。Proposal 的 CGSP 与此共享\"pessimism-based defense\"的核心理念，差异在于 CGSP 是 step-level 且以校准质量为门控。\n\n6. \"Learning a Pessimistic Reward Model in RLHF\" — PET (arXiv 2505.20556, May 2025):\n   - 全局悲观 reward fine-tuning，证明在悲观 reward model 上优化策略可以防止 reward hacking 而无需 KL 正则化。Proposal 将 PET 列为 baseline，声称 CGSP 的优势在于 step-level + calibration-adaptive。\n\n7. \"Adversarial Training for Process Reward Models\" — APRM (arXiv 2511.22888, November 2025, ICLR 2026 submission):\n   - 通过生成器-判别器对抗训练提升 PRM 鲁棒性，+3.4pp 准确率提升。已列为 proposal baseline。\n\n8. \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning\" (arXiv 2504.15275, April 2025):\n   - 提出将 PRM 的求和式 credit assignment 替换为 min-form，直接缓解 reward hacking。这是一个 **简单而有效的替代方案**，proposal 未提及。\n\n- **调研总结**: PRM 校准和 PRM hackability 各自已有成熟且快速进展的研究线——前者从 NeurIPS 2025 的分位数回归到 2026 年的 OT 方法，后者从 APRM 到 Reward Under Attack 的系统性诊断。但将两者**因果连接**并转化为防御机制的工作目前尚未出现。Proposal 处于两条研究线的交汇点，该位置有价值但核心发现的\"惊喜度\"是关键问题。\n\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。**\n\n(a) **Ensemble-min + 温度缩放**：在 ensemble PRM 上取 min reward（已有 baseline），再对每个成员做简单的 temperature scaling（成本极低），可能达到 CGSP 大部分效果。CGSP 的公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是一个 calibration-weighted lower confidence bound (LCB)。LCB 是 offline RL 中的标准技术，将其应用于 PRM step reward 是自然组合而非根本创新。\n\n(b) **Min-form credit assignment**（arXiv 2504.15275）直接从 credit assignment 角度缓解 reward hacking，不需要校准步骤，实现更简单。如果 min-form 已经大幅缓解 hacking，那么校准层面的额外改进的增量价值可能有限。\n\n(c) **Caution**（arXiv 2604.04648）使用 prediction error 作为 uncertainty proxy 做悲观调整，不需要显式校准。CGSP 相对 Caution 的增量在于\"step-level + calibration-grounded\"，但这个 delta 是否足够大需要实证回答。\n\n**增量价值分析**: CGSP 的独特价值在于它将 pessimism 的强度与**校准质量的在线监测**耦合——如果校准在 policy drift 下退化，pessimism 自动增强。这是对 static pessimism 方法的真实改进，但它的增量是**工程层面的适应性**而非**概念层面的突破**。\n\n\n【前提假设检验】:\n\n核心 claim \"PRM 校准质量因果性地决定 reward hacking 抗性\" 的逻辑链中有以下未经验证的环节：\n\n1. **\"校准是独立于表征质量的可分离因素\"假设**: Proposal 试图通过 post-hoc calibration（temperature scaling 等）来隔离校准的因果效应，声称这些方法\"provably preserve model representations\"。这在技术上成立（post-hoc 校准不改变特征空间），但问题是：**如果 post-hoc 校准改善了 hackability resistance，这可能只是因为它改善了 reward 的单调性/排序质量**（而非\"校准\"本身）。ECE 的改善可能只是一个 side effect，真正起作用的是 reward ranking 的改善。Proposal 没有控制这个混淆因素。\n\n2. **\"校准在 RL policy drift 下保持有效\"假设**: Post-hoc 校准（temperature scaling, Platt scaling）是在固定数据分布上拟合的。RL 训练中 policy 会快速 drift，导致 PRM 的输入分布变化。Proposal 提到了 Calibration Drift Detector 来监测这一问题，但这个 detector 本身依赖 ECE 估计——在有限 rollout 样本上的 ECE 估计噪声很大，可能无法及时捕捉 drift。这是一个未经验证的工程假设。\n\n3. **\"校准质量可以在 48 个配置上稳定测量并建立因果关系\"假设**: 48 个配置（8 PRMs × 6 calibration methods）的相关性研究声称 sufficient statistical power to detect r≥0.29。但 PRM 之间不是独立样本——同一 base model 的不同校准方法是高度相关的，实际有效样本量远小于 48。这会严重削弱统计推断的可靠性。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中（偏弱）**\n   - 将\"PRM 校准\"和\"PRM hackability\"两条线连接的想法有一定价值，但核心发现的方向是高度可预测的：**更好校准的 reward model 更难被 hack，这是大多数研究者的 default intuition**。如果结果是 positive，审稿人很可能说 \"I would have guessed this\"。\n   - \"Reward Under Attack\"（2603.06621）已覆盖了大部分 hackability 分析框架（gradient attacks, RL-induced hacking on AIME, BoN overoptimization），proposal 的 Contribution 1 与之高度重叠。\n   - CGSP 公式是标准 LCB + calibration weighting，是已有技术的自然组合。与 Caution（2604.04648）和 PET（2505.20556）的差异主要在工程细节（step-level, calibration-gated）而非概念框架。\n   - Step-level Hessian 分析是 Ackermann et al. 的直接扩展，增量清晰但有限。\n   - **唯一真正新颖的贡献是因果隔离实验设计**（post-hoc vs. fine-tuning calibration），但这更像是一个好的实验方法论，而非新的 idea 内核。\n\n2. **Significance: 中**\n   - Reward hacking 是 LLM RL 训练的核心问题，方向重要。\n   - 但该领域在 2025-2026 年极度拥挤——梯度正则化（Ackermann）、对抗训练（APRM）、悲观 reward（PET, Caution）、因果 reward modeling（CausalRM, RRM）、min-form credit assignment 等多条技术路线同时推进。\n   - 即使 CGSP 有效，它在实际部署中需要：(a) 多个 PRM 或校准方法来估计 σ_t；(b) 持续的在线 ECE 监测。这增加了显著的工程复杂度，可能限制实际采用。\n   - 结果的可推广性存疑：在 MATH-500 和 AIME 上的数学推理结果能否推广到代码生成、开放域对话等其他场景？\n\n3. **Related Work: 弱**\n   - Proposal 提到了 APRM、Caution、PET、Ackermann 等，有基本覆盖。\n   - 但**关键缺失**：\n     - \"Reward Under Attack\"（2603.06621, March 2026）——最直接的竞品，做了几乎相同的 PRM hackability 分析，未被提及或充分区分。\n     - \"Know What You Don't Know\"（NeurIPS 2025）——PRM 校准的标志性工作，proposal 声称 \"first\" 连接校准与 hackability 但未充分承认 PRM 校准方面的现有工作。\n     - \"Distributional Process Reward Models\"（May 2026）——最新 PRM 校准方法，proposal 的 6 种校准方法是否包含此类最新方法？\n     - Min-form credit assignment（arXiv 2504.15275）——一个更简单的 reward hacking 缓解方案，作为 trivial alternative 应被讨论。\n     - RRM（ICLR 2025）——robust reward model training 的代表工作。\n   - 差异化定位不够清晰：proposal 声称 \"first causally rigorous study\"，但没有充分论证为什么已有的 correlation evidence（如 Reward Under Attack 中隐含的）不足以支持同样的结论。\n\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】:\n核心 idea 的\"惊喜度\"不足是主要限制因素——\"校准好的 reward model 更难被 hack\"这一核心发现即使有严格的因果证据支持，也属于 confirmatory research 而非 discovery。Novelty 维度（弱-中）严重限制了上界。Significance 受制于领域过度拥挤和 CGSP 的工程复杂度。Related work 覆盖有明显漏洞，特别是未处理 \"Reward Under Attack\" 这个最直接竞品。Proposal 的形式非常完善（48 配置的 power analysis, CKA verification, Hessian analysis, Calibration Drift Detector），但这是执行层面的完备性，不改变 idea 内核偏弱的基本判断。若将会议定位为 top ML venue（ICML/NeurIPS/ICLR），22% 是合理的中位估计；若针对 CoRL（机器人学习），由于主题不匹配（LLM 数学推理而非机器人），概率会更低。\n\n【主要风险】:\n1. **\"I would have guessed this\" 风险**: 核心 causal finding 的方向高度可预测。审稿人可能认为 \"calibration improves robustness\" 是一个 tautological observation（校准本质上就是让模型输出更准确的置信度，而 hacking 本质上就是利用不准确的置信度），缺乏真正的 intellectual surprise。\n2. **竞品重叠风险**: \"Reward Under Attack\"（March 2026）已建立了系统性的 PRM hackability 分析框架且时间更早，proposal 的 hackability analysis 部分可能被视为 concurrent/redundant。如果该论文在投稿时已被接收，proposal 需要更强的差异化论证。\n```\n\nSources:\n- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)\n- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)\n- [Distributional Process Reward Models via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)\n- [Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)\n- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)\n- [Learning a Pessimistic Reward Model in RLHF (PET)](https://arxiv.org/abs/2505.20556)\n- [Adversarial Training for Process Reward Models (APRM)](https://arxiv.org/abs/2511.22888)\n- [Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)\n- [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://openreview.net/forum?id=88AS5MQnmC)\n- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\n调研完成，现在我已经有足够的信息来进行评估。让我整合所有发现。\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" (NeurIPS 2025, arXiv 2506.09338):\n   - 与本 proposal 关系：**极为直接的前驱工作**。已经证明 PRM 存在严重的校准不良问题（倾向高估部分推理步骤导向正确答案的成功概率），提出了基于分位数回归的校准方法，并展示校准后的 PRM 可实现 instance-adaptive scaling (IAS)，在数学推理 benchmark 上减少推理开销同时维持准确率。\n   - 关键发现：PRM 校准是可行的且对下游任务有实际影响；但该工作聚焦于推理效率，**未探讨校准与 hackability 的关系**。\n\n2. \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" (arXiv 2603.06621, March 2026):\n   - 与本 proposal 关系：**最直接的竞争工作**。提出了三层诊断框架（静态扰动分析、梯度对抗优化、RL-induced hacking），在 AIME 上展示 PRM 训练的 policy 获得近乎完美的 PRM reward 但 ground-truth accuracy 停滞。发现当前 PRM 本质上是 fluency detector 而非 reasoning verifier。\n   - 关键发现：PRM hackability 已经被系统性地分析过，本 proposal 的 hackability 分析部分（贡献 1、2）与该工作高度重叠。\n\n3. \"Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards\" (arXiv 2602.18037, Feb 2026):\n   - 与本 proposal 关系：即 proposal 引用的 \"Ackermann et al.\"。建立了 reward accuracy 与 loss landscape flatness 的理论联系，提出梯度正则化使训练偏向更平坦区域。\n   - 关键发现：reward accuracy 与梯度范数经验性相关。本 proposal 的 Hessian 谱分析（贡献 3）声称将此扩展到 step-level multi-reward 几何。\n\n4. \"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\" (arXiv 2604.04648, April 2026):\n   - 与本 proposal 关系：proposal 明确将 Caution 列为 baseline。Caution 将 prediction error 作为分布外不确定性信号来降低 reward 估计。\n   - 关键发现：概念上与 CGSP 相似（都是 uncertainty-based pessimism），但 Caution 使用预测误差而非校准质量作为不确定性来源。\n\n5. \"Learning a Pessimistic Reward Model in RLHF\" (PET, arXiv 2505.20556):\n   - 与本 proposal 关系：proposal 明确将 PET 列为 baseline。PET 在 offline RLHF 中学习悲观 reward model，在 BoN sampling 中有效缓解 reward hacking。\n   - 关键发现：全局悲观策略在 25% label noise 下提升 true reward 达 75%。\n\n6. \"Probabilistic Uncertain Reward Model (PURM)\" (arXiv 2503.22480, March 2025):\n   - 与本 proposal 关系：**proposal 未提及但高度相关**。PURM 将标量 reward 泛化为高斯分布，在高不确定性区域施加惩罚以防止过优化。这在概念上与 CGSP 的 r̃_t = μ_t − α·σ_t/√c_t 非常接近——区别仅在 CGSP 多了一个校准质量权重 c_t。\n   - 关键发现：uncertainty-penalized reward 的范式已经存在，CGSP 的增量在于引入 calibration quality 作为额外调制因子。\n\n7. \"APRM: Adversarial Training for Process Reward Models\" (arXiv 2511.22888):\n   - 与本 proposal 关系：proposal 将其列为 baseline。通过对抗训练提升 PRM 鲁棒性。\n\n8. \"C²GSPG: Confidence-calibrated Group Sequence Policy Gradient\" (arXiv 2509.23129):\n   - 与本 proposal 关系：使用归一化序列概率定义模型置信度并施加交叉熵正则化进行校准，在 RL 训练中整合校准信息。概念上与本 proposal 的\"将校准信息融入 RL 训练\"思路部分重叠。\n\n- **调研总结**：PRM 校准和 PRM hackability 是 2025-2026 年的两个活跃研究方向，但已有大量独立工作分别深入探讨了两者。本 proposal 试图成为\"桥接\"二者的第一项因果研究，但 (a) hackability 诊断部分已被 \"Reward Under Attack\" 大幅覆盖；(b) calibration 部分已被 NeurIPS 2025 的 \"Know What You Don't Know\" 系统探索；(c) uncertainty-penalized reward 范式已被 PURM、Caution、PET 等多种方法覆盖。本 proposal 的真正增量在于\"因果隔离\"实验设计和 calibration quality 作为 adaptive 调制因子，但该增量相对于已有工作来说较薄。\n\n\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁：\n\n1. **PURM (uncertainty-penalized reward) + 简单温度缩放**：CGSP 的公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是 uncertainty-penalized reward 加上一个 calibration quality 权重。如果简单地对 PRM 做 temperature scaling（使其校准良好，即 c_t ≈ 1），然后使用标准的 μ − α·σ 悲观策略，效果可能接近 CGSP。CGSP 相对于此的增量价值在于 **自适应地基于 calibration quality 调节悲观程度**——但这个增量是否实质性地优于固定悲观系数 + 良好校准，需要实证验证。\n\n2. **Ensemble-min（已是 baseline）**：多个 PRM 取最小值本身就是一种不需要显式校准的悲观策略。如果 ensemble-min 已经表现良好，CGSP 的额外复杂性是否 justified 存疑。\n\n3. **对于因果分析部分**：如果研究者只是想知道\"校准是否影响 hackability\"，最直接的方法是：对同一个 PRM 分别做 post-hoc calibration 和不做，然后跑 RL training 比较 reward-accuracy alignment。这不需要 48 个配置和复杂的 CKA 验证。更大的实验矩阵提供了统计功效，但核心 insight 可能从更简单的设计中就能获得。\n\n**增量价值判断**：CGSP 的增量价值（相对于 \"已校准的 PRM + 标准 uncertainty penalization\"）取决于 c_t 这个校准质量因子在实践中是否提供了有意义的额外信号。如果 post-hoc calibration 通常都能把 PRM 校准到相当好的水平（即 c_t 变化不大），那么 CGSP 退化为标准的 uncertainty penalization。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中，以下环节是未经验证的假设：\n\n1. **\"校准质量因果决定 reward hacking resistance\"**：这是最核心的假设。但有一个强混淆因素：更好的 PRM（更好的表示、更好的训练数据）可能同时具有更好的校准和更强的 hacking resistance，而两者之间并非因果关系，而是共同果（common effect of model quality）。Post-hoc calibration 实验设计试图解决这个问题——如果 post-hoc calibration（不改变表示）就能降低 hackability，则支持因果 claim。但这里有微妙之处：**post-hoc calibration 改变了 reward 的绝对数值分布，这本身就可能改变 RL 训练的优化动态**，而不一定是通过\"校准\"这个机制。例如，temperature scaling 拉平了 reward distribution，这可能降低了 RL 的有效 reward signal 强度，从而\"偶然地\"减少了 overoptimization——这不是校准在起作用，而是 reward signal 衰减在起作用。\n\n2. **\"step-level flatness 在 trajectory 上 compound\"**：这个假设缺乏理论支撑。在什么意义上 compound？乘性的？加性的？如果每步的 Hessian 特征值独立，trajectory-level 的 landscape 几何不一定是局部几何的简单聚合。这个 claim 需要明确的数学形式化，目前是 hand-waving。\n\n3. **\"ECE 是校准质量的有效度量，且可在 current-policy rollouts 上实时计算\"**：ECE 本身有已知缺陷（bin 依赖、对类别不平衡敏感）。在 RL 训练过程中，policy 不断变化，rollout distribution 也在变化。在非平稳分布上计算 ECE 并将其作为 drift detector 是否可靠，是一个未经验证的假设。\n\n4. **隐含假设：σ_t（不确定性）在校准后是可信的**：CGSP 公式中 σ_t 被用作\"校准后的不确定性\"，但如果 PRM 本身是确定性模型，σ_t 从何而来？如果来自 ensemble，那与 ensemble-min 方法的区别进一步模糊。如果来自单个模型的输出分布，其是否是 epistemic uncertainty 的可靠估计也存疑。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   本 proposal 的核心叙事是\"桥接 PRM 校准和 PRM hackability 两条成熟研究线\"，提供因果证据和基于此的防御。但：\n   - \"Reward Under Attack\" (2603.06621) 已经系统分析了 PRM hackability，包括梯度攻击、RL-induced hacking、三层诊断框架，覆盖了 proposal 贡献 1 和部分贡献 2 的空间。\n   - \"Know What You Don't Know\" (NeurIPS 2025) 已经研究了 PRM 校准并展示其对下游任务的影响。\n   - PURM (2503.22480) 已经实现了 uncertainty-penalized reward，CGSP 相对于它的增量仅是 calibration quality weighting factor c_t。\n   - Caution (2604.04648) 和 PET (2505.20556) 已经从不同角度实现了 uncertainty-based pessimism。\n   - 因果隔离实验设计（post-hoc calibration 对比 fine-tuning）是相对新颖的方法论贡献，但这是实验设计层面的 novelty，不是概念层面的突破。\n   - Hessian 谱分析扩展 Ackermann et al. 到 step-level 是合理的延伸，但属于技术增量而非新范式。\n   \n   **总结**：组合性 novelty 存在但各组件已被充分探索，核心增量（c_t 因子 + 因果隔离设计）较薄。\n\n2. **Significance: 中** — \n   \"PRM 的什么结构性质决定其 hackability？\" 是一个有价值的研究问题，理解因果机制有助于指导更好的 PRM 训练和防御设计。然而：\n   - 核心发现若为 positive（\"校准更好的 PRM 更难 hack\"），审稿人很可能反应是 **\"I would have guessed this\"**——更准确的 reward signal 自然更难被利用，这在直觉上是 expected 的。\n   - 如果发现是 negative 或 nuanced（校准不影响 hackability，或只在特定条件下影响），反而更有价值，但 proposal 的叙事和 CGSP 设计都预设了 positive 结果。\n   - CGSP 作为防御方法进入了一个已经拥挤的空间（Caution、PET、PURM、ensemble-min、gradient regularization），其实际影响力取决于是否显著优于这些方法。\n   - 对领域的推广性有限：findings 主要适用于 math reasoning 上的 PRM，对更广泛的 RLHF/reward hacking 问题的推广需要额外论证。\n\n3. **Related Work: 弱** — \n   - **PURM (2503.22480) 未被提及**，这是一个关键遗漏——PURM 的 uncertainty-penalized Gaussian reward 在概念上与 CGSP 高度相似。\n   - \"Know What You Don't Know\" (NeurIPS 2025) 虽然可能在 proposal 的完整版本中被引用，但从描述来看未充分讨论其作为直接前驱的定位。\n   - \"Reward Under Attack\" (2603.06621) 的三层诊断框架与 proposal 的贡献 1（hackability 分析）高度重叠，proposal 需要更清楚地说明增量。\n   - C²GSPG (2509.23129) 的 confidence-calibrated policy gradient 思路与本 proposal 部分重叠但未讨论。\n   - Proposal 声称 \"first causally rigorous study connecting PRM calibration to exploitability\"，但 causal reward modeling 的相关工作（如 \"Beyond Reward Hacking: Causal Rewards for LLM Alignment\", 2501.09620）也在探索 causal 框架下的 reward robustness，未被讨论。\n\n\n【概率估计】: [15% - 28%] 中位 20%\n\n【估计理由】: \n三个维度综合来看：Novelty 处于弱-中之间，核心增量（c_t 调制 + 因果隔离设计）相对于已有工作（PURM、Caution、PET、\"Reward Under Attack\"、\"Know What You Don't Know\"）较薄；Significance 为中，研究问题有价值但核心发现若 positive 不够 surprising（\"更好校准 → 更难 hack\" 是直觉预期）；Related Work 为弱，存在关键遗漏（PURM、C²GSPG）且与 \"Reward Under Attack\" 的 overlap 定位不清。**上界主要受限于 Novelty**——在 PRM 校准、hackability 分析、uncertainty-based pessimism 三个子领域都已有充分的近期工作的情况下，本 proposal 的组合性 novelty 可能不足以说服审稿人。下界受限于 Related Work 遗漏可能招致审稿人质疑 \"awareness of concurrent work\"。\n\n【主要风险】: \n1. **Novelty 被质疑**：审稿人熟悉 PURM + \"Reward Under Attack\" + \"Know What You Don't Know\" 后，可能认为 CGSP 只是已有 uncertainty-penalized reward 的微小变体（多了一个 c_t），而因果分析部分与 \"Reward Under Attack\" 的诊断框架高度重叠。\n2. **核心 claim 的 \"So what?\" 风险**：如果因果分析证实\"校准好 → 更难 hack\"，审稿人可能认为这是 expected finding（better reward signal → harder to exploit），缺乏 surprising insight，从而质疑研究的知识贡献。\n```\n\nSources:\n- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)\n- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)\n- [Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards](https://arxiv.org/abs/2602.18037)\n- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)\n- [Learning a Pessimistic Reward Model in RLHF (PET)](https://arxiv.org/abs/2505.20556)\n- [Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/pdf/2503.22480)\n- [APRM: Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)\n- [C²GSPG: Confidence-calibrated Group Sequence Policy Gradient](https://arxiv.org/abs/2509.23129)\n- [Beyond Reward Hacking: Causal Rewards for LLM Alignment](https://arxiv.org/abs/2501.09620)\n- [A Survey of Process Reward Models](https://arxiv.org/html/2510.08049v3)\n- [Reward Hacking in the Era of Large Models](https://arxiv.org/html/2604.13602v1)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:21:33.307Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:21:33.307Z",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:21:33.318Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide my evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

- "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (arXiv:2603.06621, 2026):
  最直接的竞争工作。提出三层诊断框架 (gradient attacks, RL-induced hacking, BoN overopt) 量化 PRM hackability。发现 AIME 上 PRM reward >0.9 但 ground-truth accuracy <4%，43% reward gains 来自 stylistic shortcuts。本 proposal 的实验框架（gradient attacks + RL-induced + BoN）几乎完全与此工作重叠，只是加了"calibration"这个变量。

- Ackermann et al., "Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards" (arXiv:2602.18037, 2026):
  Proposal 明确引用并声称要扩展的工作。证明 reward accuracy 与 loss landscape flatness 相关，提出 gradient regularization 作为防御。Proposal 声称将其 outcome-level gradient norm 分析扩展到 step-level Hessian spectral analysis，这是增量性扩展。

- "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism" (arXiv:2604.04648, 2026):
  Proposal 中的 "Caution" baseline。使用 prediction error 驱动的 pessimism 来缓解 BoN 中的 reward hacking。已在理论 (linear setting) 和实验上证明 pessimism 有效。Proposal 的 CGSP 与此高度相似，区别在于 CGSP 用 calibration quality 来调制 pessimism 程度。

- "Learning a Pessimistic Reward Model in RLHF" / PET (arXiv:2505.20556, 2025):
  Proposal 中的另一个 baseline。使用 global pessimism（adversarially fine-tuned reward model）防御 reward hacking，不依赖 KL regularization。Proposal 声称 CGSP 优于 PET 的点在于"step-level + calibration-grounded + adaptive"，但 PET 的 global pessimism 已经相当有效。

- "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport" (arXiv:2605.06785, May 2026):
  **Proposal 未引用但高度相关的最新工作**。使用 conditional OT 对 PRM 进行 calibration，产生任意 quantile level 的 confidence bounds。在 MATH-500 和 AIME 上验证。该工作直接做了"PRM calibration"，虽然应用场景是 inference-time scaling 而非 reward hacking defense，但方法论和 PRM calibration 的技术手段高度重叠。

- APRM: "Adversarial Training for Process Reward Models" (arXiv:2511.22888, 2025):
  Proposal 中的 baseline。通过对抗训练增强 PRM 鲁棒性，+5.3pp OOD improvement。

- "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (arXiv:2506.09338):
  直接研究 PRM 的 uncertainty calibration，发现 SOTA PRM 严重 miscalibrated，提出 quantile regression calibration。

- PURE / "Stop Summation: Min-Form Credit Assignment" (arXiv:2504.15275, 2025):
  通过改变 credit assignment 形式（sum → min）缓解 reward hacking，不需要改变 reward model 本身。

- 调研总结: PRM hackability 和 PRM calibration 分别是 2025-2026 的活跃研究方向，已有大量工作分别攻克。本 proposal 试图"bridge"二者，但该桥接的核心洞察（calibration → robustness）在直觉上是显然的，且近期已有工作从不同角度部分覆盖了这一连接（如 Distributional PRM 做 calibration for better scaling, Caution 做 uncertainty-driven pessimism）。该领域竞争激烈，proposal 的 novelty delta 被快速压缩。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. **直接 post-hoc calibration + 现有 pessimism 方法**：Proposal 自己的实验设计中已经包含了 temperature scaling / Platt scaling 等 post-hoc 方法。如果 calibration 真的是关键因素，那么简单地对现有 PRM 做 temperature scaling 再搭配已有的 pessimism 方法（如 Caution 或 ensemble-min）就应该能获得大部分收益。CGSP 相对于这种简单组合的增量价值需要仔细论证，但 proposal 没有将"calibrated PRM + existing defense"作为 baseline。

2. **Min-form credit assignment (PURE)**：完全不需要改动 reward model，仅改变 RL 中的 credit assignment 就能缓解 reward hacking。如果 PURE 的效果已经足够好，那么在 reward model 层面做复杂的 calibration-gated defense 是否 over-engineering？

3. **CGSP 公式本身的简单性**：r̃_t = μ_t − α·σ_t/√c_t 本质上是 LCB (Lower Confidence Bound)，这是 bandit/RL 文献中极为经典的思路。区别仅在于用 calibration quality c_t 做分母——这算不算一个"新方法"，还是仅仅是 LCB 的一个 trivially different instantiation？


【前提假设检验】:

核心逻辑链中有以下未经验证的假设：

1. **"Calibration quality 是 hackability 的主要因果驱动因素"**——这是整篇论文的核心 claim，但目前仅有相关性证据（proposal 自己也是先做 correlation study 再做 causal isolation）。然而，hackability 可能主要由 representation quality、training data distribution、model capacity 等因素决定，calibration 可能只是其中一个弱相关因素。如果 48 个配置的相关性实验结果显示 r < 0.29（即统计不显著），整篇论文的 story 将崩塌。

2. **"Per-step σ_t 是可靠的 uncertainty signal"**——PRM 通常用 binary labels 训练（correct/incorrect step），其输出的 sigmoid probability 不一定携带有意义的 aleatoric/epistemic uncertainty 信息。仅仅通过 post-hoc calibration 不能将一个确定性模型变成一个有良好 uncertainty quantification 的模型。

3. **"Calibration Drift Detector 可在 RL 训练中实时计算 ECE"**——ECE 的计算需要 ground-truth labels。在 RL 训练的 rollouts 中，如何获取 step-level ground truth？如果依赖 verifiable final answers (如 MATH)，那只有 outcome-level signal，无法计算 step-level ECE。这是一个实际可行性上的逻辑漏洞。

4. **"Post-hoc calibration provably preserves model representations"**——Temperature scaling 确实不改变 representations，但 isotonic regression 和 conformal prediction 的"representation preservation"属性需要更仔细的论证。CKA verification 是一种弱验证。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心 idea（calibration → robustness）在直觉上是显然的：一个输出 well-calibrated probabilities 的 reward model 自然更难被 exploit，因为它的 scores 更准确地反映 true quality。"Reward Under Attack"(2603.06621) 已经建立了 PRM hackability 的系统分析框架；"Caution"(2604.04648) 已经在用 uncertainty-driven pessimism 防御 reward hacking；"Distributional PRM"(2605.06785) 已经在做 PRM calibration。本 proposal 的贡献主要是将这些已有 thread 做 systematic combination + 加上 causal framing，但组合本身缺乏 conceptual surprise。CGSP 公式 r̃_t = μ_t − α·σ_t/√c_t 是 LCB 的一个 straightforward variant。Step-level Hessian analysis 是 Ackermann et al. 的增量扩展。

2. **Significance: 中** — 
   研究问题（PRM 为什么被 hack、如何防御）是 2025-2026 LLM reasoning 领域的核心问题之一，重要性不可否认。但本 proposal 的预期贡献是一个"连接两个已有 thread"的 bridge paper。如果核心实验结果是 positive（calibration 确实与 hackability 强相关），审稿人的反应大概率是"makes sense, I would have guessed this"而不是"surprising"。CGSP 作为防御方法，需要与已有的 5+ 种 defense 竞争 (Caution, PET, APRM, gradient regularization, PURE)，在拥挤的 solution space 中脱颖而出的难度很高。

3. **Related Work: 中** — 
   Proposal 对主要 baseline (Caution, PET, APRM, gradient regularization) 的定位是清晰的，并准确描述了它们的局限性。但有一个重要遗漏：2026 年 5 月刚出的 "Distributional Process Reward Models"(arXiv:2605.06785) 直接做 PRM calibration 并在 MATH-500/AIME 上验证，与本 proposal 的方法论高度重叠。此外，PURE (min-form credit assignment) 作为一种完全不同思路的 defense 也应被讨论。"Know What You Don't Know: Uncertainty Calibration of PRMs" 直接研究 PRM uncertainty calibration，也需要被引用和比较。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】: 
三个维度中 Novelty 是最大的限制因素。核心洞察（calibration helps robustness）缺乏 conceptual surprise，CGSP 是已有 pessimism 方法的 straightforward calibration-weighted variant，step-level Hessian 是 Ackermann et al. 的增量扩展。Significance 因研究问题的重要性而不低，但预期 finding 的 surprise level 不足以达到 35%+ 区间。领域竞争异常激烈（6 个月内至少 5 篇高度相关工作），novelty delta 被持续压缩。Proposal 形式上非常完善（48 configurations、causal isolation、4 contributions），但形式完善度不等于 idea 质量。按 rubric，这属于"idea 方向站得住脚但内核薄弱"到"有实质内核但不 surprising"的过渡区间。

另需注意：**如果投稿目标确实是 CoRL (Conference on Robot Learning)，则存在严重的 venue mismatch 问题**——本 proposal 全部内容围绕 LLM 数学推理 (MATH-500, AIME, GRPO)，与 robotics 无任何关联，大概率会因 out-of-scope 被直接拒稿。若投稿目标是 NeurIPS/ICML/ICLR 等 ML 主会，则上述概率估计适用。

【主要风险】: 
1. **Core insight 缺乏 surprise**："Well-calibrated reward model is harder to hack" 在直觉上几乎是 tautological（calibration 意味着 scores 更准确 → 更准确的 scores 自然更难被 exploit）。审稿人可能质疑这一发现的 intellectual contribution 不足以支撑一篇顶会论文。
2. **Solution space 拥挤，增量价值模糊**：CGSP 需要证明相对于"简单 calibrate PRM + 已有 defense (如 Caution)"的组合有显著优势，而 proposal 未将这一 trivial combination 作为 baseline，留下明显的审稿攻击面。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)
- [Learning a Pessimistic Reward Model in RLHF (PET)](https://arxiv.org/abs/2505.20556)
- [Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)
- [Adversarial Training for Process Reward Models (APRM)](https://arxiv.org/abs/2511.22888)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Stop Summation: Min-Form Credit Assignment (PURE)](https://arxiv.org/abs/2504.15275)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
现在我有了充分的调研基础，可以进行客观评估了。

---

```
【阶段】: Triage

【领域调研】:

1. "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (arXiv 2603.06621, March 2026):
   - 与本 proposal 关系：**最直接的竞品**。该工作已经建立了三级诊断框架（静态扰动、梯度攻击、RL 诱导 hacking），在 AIME 上发现策略获得 >0.9 PRM reward 但真实准确率 <4%，43% 的 reward 增益归因于风格捷径。与 proposal 的 Contribution 1（correlation study across gradient attacks, RL-induced hacking, BoN overoptimization）高度重叠。

2. "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (NeurIPS 2025, arXiv 2506.09338):
   - 与本 proposal 关系：**PRM 校准的开创性工作**。已证明 SOTA PRMs 严重 miscalibrated（过高估计部分推理步骤通向正确答案的概率），并提出基于分位数回归的校准方案。这是 proposal 校准维度的直接前置工作。

3. "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport" (arXiv 2605.06785, May 2026):
   - 最新 PRM 校准工作，使用条件最优传输学习完整的单调条件分位数函数，在 Brier score、ECE、weighted quantile loss 上显著优于未校准 PRM 和分位数回归。说明 PRM 校准领域正在快速进展。

4. "Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards" — Ackermann et al. (arXiv 2602.18037, February 2026):
   - proposal 明确引用并声称扩展此工作。原工作建立了 reward model 准确性与收敛点平坦度的理论联系，提出梯度正则化偏向平坦区域。Proposal 的 Contribution 3（step-level Hessian 分析）是对此的 step-level 推广。

5. "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism" (arXiv 2604.04648, April 2026):
   - 已在 BoN 场景中使用悲观主义防御 reward hacking：训练 error model，用 prediction error 降低非典型响应的 reward 估计。Proposal 的 CGSP 与此共享"pessimism-based defense"的核心理念，差异在于 CGSP 是 step-level 且以校准质量为门控。

6. "Learning a Pessimistic Reward Model in RLHF" — PET (arXiv 2505.20556, May 2025):
   - 全局悲观 reward fine-tuning，证明在悲观 reward model 上优化策略可以防止 reward hacking 而无需 KL 正则化。Proposal 将 PET 列为 baseline，声称 CGSP 的优势在于 step-level + calibration-adaptive。

7. "Adversarial Training for Process Reward Models" — APRM (arXiv 2511.22888, November 2025, ICLR 2026 submission):
   - 通过生成器-判别器对抗训练提升 PRM 鲁棒性，+3.4pp 准确率提升。已列为 proposal baseline。

8. "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning" (arXiv 2504.15275, April 2025):
   - 提出将 PRM 的求和式 credit assignment 替换为 min-form，直接缓解 reward hacking。这是一个 **简单而有效的替代方案**，proposal 未提及。

- **调研总结**: PRM 校准和 PRM hackability 各自已有成熟且快速进展的研究线——前者从 NeurIPS 2025 的分位数回归到 2026 年的 OT 方法，后者从 APRM 到 Reward Under Attack 的系统性诊断。但将两者**因果连接**并转化为防御机制的工作目前尚未出现。Proposal 处于两条研究线的交汇点，该位置有价值但核心发现的"惊喜度"是关键问题。


【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

(a) **Ensemble-min + 温度缩放**：在 ensemble PRM 上取 min reward（已有 baseline），再对每个成员做简单的 temperature scaling（成本极低），可能达到 CGSP 大部分效果。CGSP 的公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是一个 calibration-weighted lower confidence bound (LCB)。LCB 是 offline RL 中的标准技术，将其应用于 PRM step reward 是自然组合而非根本创新。

(b) **Min-form credit assignment**（arXiv 2504.15275）直接从 credit assignment 角度缓解 reward hacking，不需要校准步骤，实现更简单。如果 min-form 已经大幅缓解 hacking，那么校准层面的额外改进的增量价值可能有限。

(c) **Caution**（arXiv 2604.04648）使用 prediction error 作为 uncertainty proxy 做悲观调整，不需要显式校准。CGSP 相对 Caution 的增量在于"step-level + calibration-grounded"，但这个 delta 是否足够大需要实证回答。

**增量价值分析**: CGSP 的独特价值在于它将 pessimism 的强度与**校准质量的在线监测**耦合——如果校准在 policy drift 下退化，pessimism 自动增强。这是对 static pessimism 方法的真实改进，但它的增量是**工程层面的适应性**而非**概念层面的突破**。


【前提假设检验】:

核心 claim "PRM 校准质量因果性地决定 reward hacking 抗性" 的逻辑链中有以下未经验证的环节：

1. **"校准是独立于表征质量的可分离因素"假设**: Proposal 试图通过 post-hoc calibration（temperature scaling 等）来隔离校准的因果效应，声称这些方法"provably preserve model representations"。这在技术上成立（post-hoc 校准不改变特征空间），但问题是：**如果 post-hoc 校准改善了 hackability resistance，这可能只是因为它改善了 reward 的单调性/排序质量**（而非"校准"本身）。ECE 的改善可能只是一个 side effect，真正起作用的是 reward ranking 的改善。Proposal 没有控制这个混淆因素。

2. **"校准在 RL policy drift 下保持有效"假设**: Post-hoc 校准（temperature scaling, Platt scaling）是在固定数据分布上拟合的。RL 训练中 policy 会快速 drift，导致 PRM 的输入分布变化。Proposal 提到了 Calibration Drift Detector 来监测这一问题，但这个 detector 本身依赖 ECE 估计——在有限 rollout 样本上的 ECE 估计噪声很大，可能无法及时捕捉 drift。这是一个未经验证的工程假设。

3. **"校准质量可以在 48 个配置上稳定测量并建立因果关系"假设**: 48 个配置（8 PRMs × 6 calibration methods）的相关性研究声称 sufficient statistical power to detect r≥0.29。但 PRM 之间不是独立样本——同一 base model 的不同校准方法是高度相关的，实际有效样本量远小于 48。这会严重削弱统计推断的可靠性。


【3 维度打分】:

1. **Novelty: 弱-中（偏弱）**
   - 将"PRM 校准"和"PRM hackability"两条线连接的想法有一定价值，但核心发现的方向是高度可预测的：**更好校准的 reward model 更难被 hack，这是大多数研究者的 default intuition**。如果结果是 positive，审稿人很可能说 "I would have guessed this"。
   - "Reward Under Attack"（2603.06621）已覆盖了大部分 hackability 分析框架（gradient attacks, RL-induced hacking on AIME, BoN overoptimization），proposal 的 Contribution 1 与之高度重叠。
   - CGSP 公式是标准 LCB + calibration weighting，是已有技术的自然组合。与 Caution（2604.04648）和 PET（2505.20556）的差异主要在工程细节（step-level, calibration-gated）而非概念框架。
   - Step-level Hessian 分析是 Ackermann et al. 的直接扩展，增量清晰但有限。
   - **唯一真正新颖的贡献是因果隔离实验设计**（post-hoc vs. fine-tuning calibration），但这更像是一个好的实验方法论，而非新的 idea 内核。

2. **Significance: 中**
   - Reward hacking 是 LLM RL 训练的核心问题，方向重要。
   - 但该领域在 2025-2026 年极度拥挤——梯度正则化（Ackermann）、对抗训练（APRM）、悲观 reward（PET, Caution）、因果 reward modeling（CausalRM, RRM）、min-form credit assignment 等多条技术路线同时推进。
   - 即使 CGSP 有效，它在实际部署中需要：(a) 多个 PRM 或校准方法来估计 σ_t；(b) 持续的在线 ECE 监测。这增加了显著的工程复杂度，可能限制实际采用。
   - 结果的可推广性存疑：在 MATH-500 和 AIME 上的数学推理结果能否推广到代码生成、开放域对话等其他场景？

3. **Related Work: 弱**
   - Proposal 提到了 APRM、Caution、PET、Ackermann 等，有基本覆盖。
   - 但**关键缺失**：
     - "Reward Under Attack"（2603.06621, March 2026）——最直接的竞品，做了几乎相同的 PRM hackability 分析，未被提及或充分区分。
     - "Know What You Don't Know"（NeurIPS 2025）——PRM 校准的标志性工作，proposal 声称 "first" 连接校准与 hackability 但未充分承认 PRM 校准方面的现有工作。
     - "Distributional Process Reward Models"（May 2026）——最新 PRM 校准方法，proposal 的 6 种校准方法是否包含此类最新方法？
     - Min-form credit assignment（arXiv 2504.15275）——一个更简单的 reward hacking 缓解方案，作为 trivial alternative 应被讨论。
     - RRM（ICLR 2025）——robust reward model training 的代表工作。
   - 差异化定位不够清晰：proposal 声称 "first causally rigorous study"，但没有充分论证为什么已有的 correlation evidence（如 Reward Under Attack 中隐含的）不足以支持同样的结论。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
核心 idea 的"惊喜度"不足是主要限制因素——"校准好的 reward model 更难被 hack"这一核心发现即使有严格的因果证据支持，也属于 confirmatory research 而非 discovery。Novelty 维度（弱-中）严重限制了上界。Significance 受制于领域过度拥挤和 CGSP 的工程复杂度。Related work 覆盖有明显漏洞，特别是未处理 "Reward Under Attack" 这个最直接竞品。Proposal 的形式非常完善（48 配置的 power analysis, CKA verification, Hessian analysis, Calibration Drift Detector），但这是执行层面的完备性，不改变 idea 内核偏弱的基本判断。若将会议定位为 top ML venue（ICML/NeurIPS/ICLR），22% 是合理的中位估计；若针对 CoRL（机器人学习），由于主题不匹配（LLM 数学推理而非机器人），概率会更低。

【主要风险】:
1. **"I would have guessed this" 风险**: 核心 causal finding 的方向高度可预测。审稿人可能认为 "calibration improves robustness" 是一个 tautological observation（校准本质上就是让模型输出更准确的置信度，而 hacking 本质上就是利用不准确的置信度），缺乏真正的 intellectual surprise。
2. **竞品重叠风险**: "Reward Under Attack"（March 2026）已建立了系统性的 PRM hackability 分析框架且时间更早，proposal 的 hackability analysis 部分可能被视为 concurrent/redundant。如果该论文在投稿时已被接收，proposal 需要更强的差异化论证。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)
- [Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)
- [Learning a Pessimistic Reward Model in RLHF (PET)](https://arxiv.org/abs/2505.20556)
- [Adversarial Training for Process Reward Models (APRM)](https://arxiv.org/abs/2511.22888)
- [Stop Summation: Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)
- [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://openreview.net/forum?id=88AS5MQnmC)
- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
调研完成，现在我已经有足够的信息来进行评估。让我整合所有发现。

---

```
【阶段】: Triage

【领域调研】:

1. "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (NeurIPS 2025, arXiv 2506.09338):
   - 与本 proposal 关系：**极为直接的前驱工作**。已经证明 PRM 存在严重的校准不良问题（倾向高估部分推理步骤导向正确答案的成功概率），提出了基于分位数回归的校准方法，并展示校准后的 PRM 可实现 instance-adaptive scaling (IAS)，在数学推理 benchmark 上减少推理开销同时维持准确率。
   - 关键发现：PRM 校准是可行的且对下游任务有实际影响；但该工作聚焦于推理效率，**未探讨校准与 hackability 的关系**。

2. "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (arXiv 2603.06621, March 2026):
   - 与本 proposal 关系：**最直接的竞争工作**。提出了三层诊断框架（静态扰动分析、梯度对抗优化、RL-induced hacking），在 AIME 上展示 PRM 训练的 policy 获得近乎完美的 PRM reward 但 ground-truth accuracy 停滞。发现当前 PRM 本质上是 fluency detector 而非 reasoning verifier。
   - 关键发现：PRM hackability 已经被系统性地分析过，本 proposal 的 hackability 分析部分（贡献 1、2）与该工作高度重叠。

3. "Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards" (arXiv 2602.18037, Feb 2026):
   - 与本 proposal 关系：即 proposal 引用的 "Ackermann et al."。建立了 reward accuracy 与 loss landscape flatness 的理论联系，提出梯度正则化使训练偏向更平坦区域。
   - 关键发现：reward accuracy 与梯度范数经验性相关。本 proposal 的 Hessian 谱分析（贡献 3）声称将此扩展到 step-level multi-reward 几何。

4. "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism" (arXiv 2604.04648, April 2026):
   - 与本 proposal 关系：proposal 明确将 Caution 列为 baseline。Caution 将 prediction error 作为分布外不确定性信号来降低 reward 估计。
   - 关键发现：概念上与 CGSP 相似（都是 uncertainty-based pessimism），但 Caution 使用预测误差而非校准质量作为不确定性来源。

5. "Learning a Pessimistic Reward Model in RLHF" (PET, arXiv 2505.20556):
   - 与本 proposal 关系：proposal 明确将 PET 列为 baseline。PET 在 offline RLHF 中学习悲观 reward model，在 BoN sampling 中有效缓解 reward hacking。
   - 关键发现：全局悲观策略在 25% label noise 下提升 true reward 达 75%。

6. "Probabilistic Uncertain Reward Model (PURM)" (arXiv 2503.22480, March 2025):
   - 与本 proposal 关系：**proposal 未提及但高度相关**。PURM 将标量 reward 泛化为高斯分布，在高不确定性区域施加惩罚以防止过优化。这在概念上与 CGSP 的 r̃_t = μ_t − α·σ_t/√c_t 非常接近——区别仅在 CGSP 多了一个校准质量权重 c_t。
   - 关键发现：uncertainty-penalized reward 的范式已经存在，CGSP 的增量在于引入 calibration quality 作为额外调制因子。

7. "APRM: Adversarial Training for Process Reward Models" (arXiv 2511.22888):
   - 与本 proposal 关系：proposal 将其列为 baseline。通过对抗训练提升 PRM 鲁棒性。

8. "C²GSPG: Confidence-calibrated Group Sequence Policy Gradient" (arXiv 2509.23129):
   - 与本 proposal 关系：使用归一化序列概率定义模型置信度并施加交叉熵正则化进行校准，在 RL 训练中整合校准信息。概念上与本 proposal 的"将校准信息融入 RL 训练"思路部分重叠。

- **调研总结**：PRM 校准和 PRM hackability 是 2025-2026 年的两个活跃研究方向，但已有大量独立工作分别深入探讨了两者。本 proposal 试图成为"桥接"二者的第一项因果研究，但 (a) hackability 诊断部分已被 "Reward Under Attack" 大幅覆盖；(b) calibration 部分已被 NeurIPS 2025 的 "Know What You Don't Know" 系统探索；(c) uncertainty-penalized reward 范式已被 PURM、Caution、PET 等多种方法覆盖。本 proposal 的真正增量在于"因果隔离"实验设计和 calibration quality 作为 adaptive 调制因子，但该增量相对于已有工作来说较薄。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. **PURM (uncertainty-penalized reward) + 简单温度缩放**：CGSP 的公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是 uncertainty-penalized reward 加上一个 calibration quality 权重。如果简单地对 PRM 做 temperature scaling（使其校准良好，即 c_t ≈ 1），然后使用标准的 μ − α·σ 悲观策略，效果可能接近 CGSP。CGSP 相对于此的增量价值在于 **自适应地基于 calibration quality 调节悲观程度**——但这个增量是否实质性地优于固定悲观系数 + 良好校准，需要实证验证。

2. **Ensemble-min（已是 baseline）**：多个 PRM 取最小值本身就是一种不需要显式校准的悲观策略。如果 ensemble-min 已经表现良好，CGSP 的额外复杂性是否 justified 存疑。

3. **对于因果分析部分**：如果研究者只是想知道"校准是否影响 hackability"，最直接的方法是：对同一个 PRM 分别做 post-hoc calibration 和不做，然后跑 RL training 比较 reward-accuracy alignment。这不需要 48 个配置和复杂的 CKA 验证。更大的实验矩阵提供了统计功效，但核心 insight 可能从更简单的设计中就能获得。

**增量价值判断**：CGSP 的增量价值（相对于 "已校准的 PRM + 标准 uncertainty penalization"）取决于 c_t 这个校准质量因子在实践中是否提供了有意义的额外信号。如果 post-hoc calibration 通常都能把 PRM 校准到相当好的水平（即 c_t 变化不大），那么 CGSP 退化为标准的 uncertainty penalization。


【前提假设检验】:

核心 claim 的逻辑链条中，以下环节是未经验证的假设：

1. **"校准质量因果决定 reward hacking resistance"**：这是最核心的假设。但有一个强混淆因素：更好的 PRM（更好的表示、更好的训练数据）可能同时具有更好的校准和更强的 hacking resistance，而两者之间并非因果关系，而是共同果（common effect of model quality）。Post-hoc calibration 实验设计试图解决这个问题——如果 post-hoc calibration（不改变表示）就能降低 hackability，则支持因果 claim。但这里有微妙之处：**post-hoc calibration 改变了 reward 的绝对数值分布，这本身就可能改变 RL 训练的优化动态**，而不一定是通过"校准"这个机制。例如，temperature scaling 拉平了 reward distribution，这可能降低了 RL 的有效 reward signal 强度，从而"偶然地"减少了 overoptimization——这不是校准在起作用，而是 reward signal 衰减在起作用。

2. **"step-level flatness 在 trajectory 上 compound"**：这个假设缺乏理论支撑。在什么意义上 compound？乘性的？加性的？如果每步的 Hessian 特征值独立，trajectory-level 的 landscape 几何不一定是局部几何的简单聚合。这个 claim 需要明确的数学形式化，目前是 hand-waving。

3. **"ECE 是校准质量的有效度量，且可在 current-policy rollouts 上实时计算"**：ECE 本身有已知缺陷（bin 依赖、对类别不平衡敏感）。在 RL 训练过程中，policy 不断变化，rollout distribution 也在变化。在非平稳分布上计算 ECE 并将其作为 drift detector 是否可靠，是一个未经验证的假设。

4. **隐含假设：σ_t（不确定性）在校准后是可信的**：CGSP 公式中 σ_t 被用作"校准后的不确定性"，但如果 PRM 本身是确定性模型，σ_t 从何而来？如果来自 ensemble，那与 ensemble-min 方法的区别进一步模糊。如果来自单个模型的输出分布，其是否是 epistemic uncertainty 的可靠估计也存疑。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   本 proposal 的核心叙事是"桥接 PRM 校准和 PRM hackability 两条成熟研究线"，提供因果证据和基于此的防御。但：
   - "Reward Under Attack" (2603.06621) 已经系统分析了 PRM hackability，包括梯度攻击、RL-induced hacking、三层诊断框架，覆盖了 proposal 贡献 1 和部分贡献 2 的空间。
   - "Know What You Don't Know" (NeurIPS 2025) 已经研究了 PRM 校准并展示其对下游任务的影响。
   - PURM (2503.22480) 已经实现了 uncertainty-penalized reward，CGSP 相对于它的增量仅是 calibration quality weighting factor c_t。
   - Caution (2604.04648) 和 PET (2505.20556) 已经从不同角度实现了 uncertainty-based pessimism。
   - 因果隔离实验设计（post-hoc calibration 对比 fine-tuning）是相对新颖的方法论贡献，但这是实验设计层面的 novelty，不是概念层面的突破。
   - Hessian 谱分析扩展 Ackermann et al. 到 step-level 是合理的延伸，但属于技术增量而非新范式。
   
   **总结**：组合性 novelty 存在但各组件已被充分探索，核心增量（c_t 因子 + 因果隔离设计）较薄。

2. **Significance: 中** — 
   "PRM 的什么结构性质决定其 hackability？" 是一个有价值的研究问题，理解因果机制有助于指导更好的 PRM 训练和防御设计。然而：
   - 核心发现若为 positive（"校准更好的 PRM 更难 hack"），审稿人很可能反应是 **"I would have guessed this"**——更准确的 reward signal 自然更难被利用，这在直觉上是 expected 的。
   - 如果发现是 negative 或 nuanced（校准不影响 hackability，或只在特定条件下影响），反而更有价值，但 proposal 的叙事和 CGSP 设计都预设了 positive 结果。
   - CGSP 作为防御方法进入了一个已经拥挤的空间（Caution、PET、PURM、ensemble-min、gradient regularization），其实际影响力取决于是否显著优于这些方法。
   - 对领域的推广性有限：findings 主要适用于 math reasoning 上的 PRM，对更广泛的 RLHF/reward hacking 问题的推广需要额外论证。

3. **Related Work: 弱** — 
   - **PURM (2503.22480) 未被提及**，这是一个关键遗漏——PURM 的 uncertainty-penalized Gaussian reward 在概念上与 CGSP 高度相似。
   - "Know What You Don't Know" (NeurIPS 2025) 虽然可能在 proposal 的完整版本中被引用，但从描述来看未充分讨论其作为直接前驱的定位。
   - "Reward Under Attack" (2603.06621) 的三层诊断框架与 proposal 的贡献 1（hackability 分析）高度重叠，proposal 需要更清楚地说明增量。
   - C²GSPG (2509.23129) 的 confidence-calibrated policy gradient 思路与本 proposal 部分重叠但未讨论。
   - Proposal 声称 "first causally rigorous study connecting PRM calibration to exploitability"，但 causal reward modeling 的相关工作（如 "Beyond Reward Hacking: Causal Rewards for LLM Alignment", 2501.09620）也在探索 causal 框架下的 reward robustness，未被讨论。


【概率估计】: [15% - 28%] 中位 20%

【估计理由】: 
三个维度综合来看：Novelty 处于弱-中之间，核心增量（c_t 调制 + 因果隔离设计）相对于已有工作（PURM、Caution、PET、"Reward Under Attack"、"Know What You Don't Know"）较薄；Significance 为中，研究问题有价值但核心发现若 positive 不够 surprising（"更好校准 → 更难 hack" 是直觉预期）；Related Work 为弱，存在关键遗漏（PURM、C²GSPG）且与 "Reward Under Attack" 的 overlap 定位不清。**上界主要受限于 Novelty**——在 PRM 校准、hackability 分析、uncertainty-based pessimism 三个子领域都已有充分的近期工作的情况下，本 proposal 的组合性 novelty 可能不足以说服审稿人。下界受限于 Related Work 遗漏可能招致审稿人质疑 "awareness of concurrent work"。

【主要风险】: 
1. **Novelty 被质疑**：审稿人熟悉 PURM + "Reward Under Attack" + "Know What You Don't Know" 后，可能认为 CGSP 只是已有 uncertainty-penalized reward 的微小变体（多了一个 c_t），而因果分析部分与 "Reward Under Attack" 的诊断框架高度重叠。
2. **核心 claim 的 "So what?" 风险**：如果因果分析证实"校准好 → 更难 hack"，审稿人可能认为这是 expected finding（better reward signal → harder to exploit），缺乏 surprising insight，从而质疑研究的知识贡献。
```

Sources:
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)
- [Learning a Pessimistic Reward Model in RLHF (PET)](https://arxiv.org/abs/2505.20556)
- [Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/pdf/2503.22480)
- [APRM: Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)
- [C²GSPG: Confidence-calibrated Group Sequence Policy Gradient](https://arxiv.org/abs/2509.23129)
- [Beyond Reward Hacking: Causal Rewards for LLM Alignment](https://arxiv.org/abs/2501.09620)
- [A Survey of Process Reward Models](https://arxiv.org/html/2510.08049v3)
- [Reward Hacking in the Era of Large Models](https://arxiv.org/html/2604.13602v1)


【原始 proposal（允许参考但不是主要依据）】:
# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense

## Description
We present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2818e794-6606-4304-ad1e-44e9b7b8e4b3",
  "type": "user",
  "uuid": "ac2c0de1-01c2-48c9-81f6-b40c8abe4ee9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:21:33.317Z_

```json
{
  "parentUuid": "ac2c0de1-01c2-48c9-81f6-b40c8abe4ee9",
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
  "uuid": "8fcdf6c7-f702-4b18-92ba-040847382f21",
  "timestamp": "2026-05-20T03:21:33.317Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:21:33.317Z_

```json
{
  "parentUuid": "8fcdf6c7-f702-4b18-92ba-040847382f21",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "64800364-02f2-4403-9cf3-875e05a0f02d",
  "timestamp": "2026-05-20T03:21:33.317Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide my evaluation. Le…",
  "leafUuid": "64800364-02f2-4403-9cf3-875e05a0f02d",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking defenses",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:22:05.372Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully and produce a Meta Judge output.

First, let me extract the key data points:

**Reviewer 1:**
- Probability: [18% - 28%] 中位 22%
- Novelty: 弱-中
- Significance: 中
- Related Work: 中
- Key concerns: Core insight lacks surprise, solution space crowded, CGSP is LCB variant, venue mismatch (CoRL)


**Reviewer 2:**
- Probability: [18% - 28%] 中位 22%
- Novelty: 弱-中（偏弱）
- Significance: 中
- Related Work: 弱
- Key concerns: "I would have guessed this" risk, Reward Under Attack overlap, missing PURM/C²GSPG references

**Reviewer 3:**
- Probability: [15% - 28%] 中位 20%
- Novelty: 弱-中
- Significance: 中
- Related Work: 弱
- Key concerns: PURM highly similar to CG

All three reviewers converge on weak-to-moderate novelty with moderate significance, though they identify different specific gaps—Reviewer 2 flags missing related work citations while Reviewer 3 points to substantial overlap with existing methods.

Computing the acceptance probabilities across reviewers gives me a median of 22% with remarkably tight consistency (standard deviation under 1%), suggesting strong agreement despite their different concerns. The core issues they all identify are thin incremental novelty, lack of surprising insights, and potential confounders in the causal claims being made.

Where they converge most is on the specific technical overlaps: the hackability analysis mirrors "Reward Under Attack," the step-level Hessian feels like a straightforward extension of Ackermann's work, and the solution space is already crowded. They also agree on several missing references that should strengthen the work—particularly "Know What You Don't Know" and the distributional PRM paper. The causal isolation contribution stands out as the most novel piece, but it's methodological rather than conceptually new, and there's concern that post-hoc calibration might be confounding the reward signal effects. One reviewer also flags a venue mismatch with CoRL.

The anomalies are scattered: only R1 mentions the Related Work section as adequate while the others find it weak, only R3 calls out a couple of specific missing papers, and only R2 raises a statistical independence question about the 48 configurations. Given how tightly the reviewers cluster otherwise—the standard deviation is around 1%—I should anchor on the median assessment and tighten the interval.

What really stands out is that all three converge on novelty being the core problem. They describe the central insight as tautological or highly derivative, which is the binding constraint here.

The strictest reviewer lands at 20%, while the other two are at 22%, so the median sits at 22%. With this level of consistency, I'll go with that.

Now looking at what the paper actually requires: they're running 48 different PRM configurations across multiple attack types, training GRPO on AIME, and using best-of-N sampling on MATH-500, which demands substantial compute resources. The data comes from public sources, there's real training involved with both GRPO and PRM fine-tuning, but no new benchmark is introduced. The timeline is considerable given the scale of configurations and the causal isolation work needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64800364-02f2-4403-9cf3-875e05a0f02d",
  "isSidechain": false,
  "requestId": "req_011CbD6rtJByZrLvBUFi5YAK",
  "type": "assistant",
  "uuid": "d5f35159-9e3a-4726-86c3-ea2565d417f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeqvPreypk43GuZ9gFrVjZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15408,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3327,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 15408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15408
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

_source line 9 · 2026-05-20T03:22:53.530Z_

【阶段】: Meta Judge
【三次中位】: [22%, 22%, 20%]  std=0.9%
【共识维度】:
- **Novelty 弱-中**（3/3 一致）：核心洞察"校准好的 PRM 更难被 hack"在直觉上近乎 tautological，缺乏 conceptual surprise。CGSP 是 LCB/uncertainty-penalized reward 的 straightforward variant。
- **Significance 中**（3/3 一致）：研究问题本身重要（PRM hackability 是 LLM RL 核心问题），但预期发现方向高度可预测（"I would have guessed this" 风险），且 solution space 极度拥挤（Caution, PET, PURM, APRM, gradient regularization, PURE 等 6+ 种已有 defense）。
- **"Reward Under Attack"(2603.06621) 高度重叠**（3/3 一致）：该工作已建立三层诊断框架覆盖 gradient attacks / RL-induced hacking / BoN overoptimization，与 proposal 的贡献 1 和部分贡献 2 空间重叠严重。
- **Step-level Hessian 是 Ackermann et al. 的增量扩展**（3/3 一致）：技术增量清晰但有限，非新范式。
- **Related Work 存在关键遗漏**（3/3 一致）：PURM(2503.22480)、"Know What You Don't Know"(NeurIPS 2025) 讨论不足、Distributional PRM(2605.06785) 未引用。其中 PURM 与 CGSP 概念高度相似（均为 uncertainty-penalized reward，CGSP 仅多一个 c_t 因子）。
- **Trivial alternative 威胁显著**（3/3 一致）：温度缩放 + 已有 pessimism 方法（Caution/ensemble-min）可能获得 CGSP 大部分收益；min-form credit assignment (PURE) 提供更简单的替代路径。
- **因果隔离实验设计存在混淆风险**（2/3，R2+R3）：post-hoc calibration 改变 reward 绝对数值分布，可能通过 reward signal 衰减而非"校准"本身降低 overoptimization，proposal 未控制此混淆因素。
- **因果隔离是最具新颖性的方法论贡献**（2/3，R1+R3）：但属于实验设计层面，非概念突破。

【异常维度】:
- Related Work 评为"中"（仅 R1，R2/R3 均评"弱"）→ R1 偏宽松，降权，采信 R2/R3 的"弱"判定
- C²GSPG(2509.23129) 和 "Beyond Reward Hacking: Causal Rewards"(2501.09620) 作为遗漏引用（仅 R3）→ 相关性较 PURM 弱，不构成关键遗漏
- 48 配置统计功效问题（PRM 间非独立，有效样本量远小于 48）（仅 R2）→ 合理质疑但属技术细节，不影响整体判定
- CoRL venue mismatch（仅 R1 明确指出）→ 这是事实性观察而非主观判断，应予以保留和强调

【最终概率】: [16% - 26%] 中位 21%
【一致性】: 高（std=0.9%，远低于 3% 阈值）
【综合理由】:
三位审稿人的判断高度一致，核心共识极为清晰：**Novelty 是绑定约束**。"更好校准的 reward model 更难被 hack" 这一核心 claim 在直觉上近乎 self-evident，即使用因果实验设计严格论证，也属于 confirmatory research 而非 discovery。CGSP 方法的增量价值被 PURM（已有 uncertainty-penalized reward）和 Caution（已有 uncertainty-based pessimism）大幅压缩，仅剩 c_t 调制因子这一点差异化。Hackability 分析部分与 "Reward Under Attack" 重叠严重。Related Work 存在多个关键遗漏（PURM 最为致命——它在概念上与 CGSP 仅一步之遥）。

中位取 21%（略低于三人中位 22%），因为：(1) Related Work 维度在 R2/R3 的"弱"评定下比 R1 的"中"更准确，应向严格方向微调；(2) 三人均未充分加权 PURM 对 CGSP novelty 的压缩效应——PURM 的存在使 CGSP 的"新方法"地位进一步削弱。区间略向下调整至 [16%-26%]，下界 16% 反映 Related Work 遗漏可能在评审中被放大的风险。

**特别标注**：若投稿目标确实是 CoRL（Conference on Robot Learning），则因严重的 venue mismatch（全部内容为 LLM 数学推理，与 robotics 无任何关联），概率应降至 5% 以下，属于直接 desk reject 风险。上述 21% 的估计仅适用于 ML 主会（NeurIPS/ICML/ICLR）。

【建议】: 不推荐
【实施评估】:
  - 计算资源: 48 个 PRM 配置的校准实验 + 多种攻击评估（gradient attacks, BoN, RL-induced hacking）+ GRPO 训练（AIME）需要大量 GPU 算力。估计需 8×A100 级别集群，总计算量约 2000-4000 GPU-hours（含 8 个 PRM 的 6 种校准方法 × 3 种攻击场景 + CGSP 的 GRPO 训练 + 5 个 baseline 对比）。Hessian 谱分析对大型 PRM 计算成本较高。
  - 数据需求: MATH-500 和 AIME 数据集均公开可得，无数据障碍。8 个 PRM 需要获取预训练 checkpoint（部分可能需自行训练）。
  - 人工介入: 需要手工分析 hackability case studies（stylistic shortcuts 等质性分析）；48 配置的实验管理和调参需要较高的工程投入。
  - 训练需求: 需要 PRM fine-tuning（6 种校准方法中的 fine-tuning-based 方法）+ GRPO RL 训练（AIME 场景）+ CGSP 及 5 个 baseline 的完整 RL 训练。模型规模取决于选用的 PRM（7B-70B 级别），训练总量显著。
  - 新 Benchmark: 不需要构建新 benchmark，使用现有 MATH-500 和 AIME。
  - 预估周期: 约 3-4 个月（含实验设计 2 周 + 48 配置实验 4-6 周 + 因果隔离实验 2-3 周 + CGSP 训练与评估 3-4 周 + 论文撰写 3-4 周）。关键瓶颈是 48 配置实验矩阵的计算吞吐量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5f35159-9e3a-4726-86c3-ea2565d417f2",
  "isSidechain": false,
  "requestId": "req_011CbD6rtJByZrLvBUFi5YAK",
  "type": "assistant",
  "uuid": "00798529-b1cd-4cf1-a8a6-3d15a7be8f90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeqvPreypk43GuZ9gFrVjZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15408,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3327,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 15408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15408
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide my evaluation. Le…",
  "leafUuid": "00798529-b1cd-4cf1-a8a6-3d15a7be8f90",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking defenses",
  "sessionId": "34e9fd05-f4e1-48a0-9d1d-3b7276296e03"
}
```

---
