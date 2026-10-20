# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/fa1834d3-1275-4512-9fde-4129d908f30c.jsonl`
- **Structured JSON:** [`cb04aca2233383553e86.json`](../../sessions/cb/cb04aca2233383553e86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:31:08.618Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:31:08.618Z",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\n现在我已经完成了充分的领域调研，可以进行系统评估了。\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [arXiv:2604.22271] \"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals\" (2026.04):\n   — 直接竞争者。该论文从决策神经科学的\"二阶模型\"出发，研究 LLM 内部的评价性信号如何驱动错误检测与自我修正，发现 LLM 缓存了一个独立于 log-prob 的评价性表征，能预测哪些错误模型可以修正。这与本 proposal 的核心 claim（用内部表征预测 correctability）高度重叠。\n\n2. [arXiv:2601.00828] \"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis\" (2025.12):\n   — 直接前驱。该论文将 self-correction 分解为 error detection / localization / correction 三个子能力，提出 Error Depth Hypothesis：强模型犯的错误更\"深\"、更抗修正。这在概念层面与 \"correctability\" 作为预测目标高度一致——\"浅错误=可修正，深错误=不可修正\"。\n\n3. [arXiv:2602.09924] \"LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations\" (2026.02):\n   — 密切相关。该论文训练 linear probe on pre-generation activations 预测模型是否会答对，并展示 probe-guided routing 可在减少 40% 计算成本的同时匹配高计算精度。方法论上（probe → gating）与本 proposal 的框架非常接近，区别仅在目标（correctness vs. correctability）。\n\n4. [arXiv:2604.13386] \"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\" (2026.04):\n   — 本 proposal 直接引用的方法来源。该论文证明多层 ensemble probe 在 deception detection 上大幅优于单层 probe（+78% AUROC on Harm-Pressure Knowledge）。本 proposal 的\"Phase 0 pilot\"本质是测试此技术是否 transfer 到 correctability 任务。\n\n5. [arXiv:2604.19974] \"Are LLM Uncertainty and Correctness Encoded by the Same Features?\" (2026.04):\n   — 本 proposal 引用的 SAE 分析基础。该论文区分了 pure uncertainty / pure incorrectness / confounded features 三类特征，发现 68% 的 pure incorrectness features 在因果干预下是 inert 的。本 proposal 拟将此分析框架延伸到 correctability。\n\n6. [arXiv:2602.08159] \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\" (2026.02):\n   — 本 proposal 引用的几何分析基础。该论文在 9 个模型上发现 correctness 信号占据 3-8 维、线性可分、非线性分类器无额外提升。本 proposal 拟测试 correctability（二阶属性）是否也具有类似结构。\n\n7. [arXiv:2510.04128] \"Internal states before wait modulate reasoning patterns\" (2025.10):\n   — 本 proposal 引用的 Wait-token 机制分析。使用 crosscoder 定位影响 wait token 概率的特征集。\n\n8. [arXiv:2602.08948] \"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute\" (2026.02):\n   — 本 proposal 的主要对比系统。CoRefine 使用 output-level confidence 做三路路由（HALT/RETHINK/ALTERNATIVE），211K 参数 Conv1D controller，精度 92.6%。\n\n- 调研总结: 2025-2026 年间，LLM 自我修正的 probe-based gating、内部表征对 correctness/uncertainty 的编码、以及 self-correction 的分解分析已成为非常拥挤的研究方向。本 proposal 的每一个技术组件（multi-layer ensemble probe、SAE feature decomposition、representational geometry analysis、probe-gated routing）均已在近期独立论文中被提出和验证。Proposal 的差异化定位在于将预测目标从 \"correctness\" 切换为 \"correctability\"，但这一概念与 Error Depth Hypothesis 和内部 confidence 信号的工作存在显著重叠。\n\n\n【Trivial Alternative 检验】:\n存在多个成本更低的 trivial alternatives：\n\n(1) **直接用 correctness probe 做代理**：既然已经有成熟的 correctness linear probe（AUROC ~0.87，见 LLM Reasoning as Trajectories），可以简单地\"检测错误 → 一律尝试修正\"，省去 correctability 预测这一步。Proposal 的增量价值取决于\"可修正\"vs.\"不可修正\"的区分能否提供超过 correctness probe 的显著收益——但这本身是一个 empirical claim，且 Error Depth Hypothesis 已经暗示更强的模型犯的错更少但更难修正，意味着 correctability prediction 可能本身就很难（大多数错误要么都可修正，要么都不可修正）。\n\n(2) **CoRefine 的 confidence-based routing**：CoRefine 使用 output-level confidence 做 routing，精度达 92.6%，且只需 211K 参数。本 proposal 使用 hidden-state probe 做 routing 的增量收益需要超过这个强 baseline，但 hidden-state probe 的额外复杂度（multi-layer extraction, SAE feature selection）是否值得，是一个未回答的问题。\n\n(3) **简单的 logit entropy / verbalized confidence**：多篇论文已表明 logit-based uncertainty 和 verbalized confidence 在某些场景下已经是有效的 proxy。\n\n增量价值在于：如果 correctability 确实是一个与 correctness 不同的、可预测的内部属性，且其预测能带来超越 confidence-based routing 的 gating 收益。但这是一个层层叠加的条件假设，每层都有 fail 的风险。\n\n\n【前提假设检验】:\n核心 claim 的逻辑链存在多个未验证的前提假设：\n\n(1) **\"Correctability 是模型内部表征中一个可检测的、与 correctness 不同的独立属性\"** —— 这是最关键的假设，完全没有理论或实证支撑。已有证据反而不利：arXiv:2604.19974 发现 68% 的 pure incorrectness features 是 causally inert 的。如果 correctness 的一阶属性都在内部表征中缺乏 causal footprint，一个依赖于 correctness 的二阶属性（correctability = \"wrong AND fixable\"）为什么会有更强的可检测信号？没有理论解释。\n\n(2) **\"Multi-layer ensemble 从 deception detection transfer 到 correctability\"** —— Deception 是一个有意的、二元的行为（模型\"知道\"正确答案但选择输出错误答案），内部表征的几何结构可能与 correctability（模型不知道正确答案但可能通过 reasoning 找到）完全不同。Transfer 假设缺乏理论支撑。\n\n(3) **\"三路 gating 优于二路 gating\"** —— 添加 abstain 选项的前提是 correctability probe 能可靠区分\"可修正\"和\"不可修正\"的错误。如果 probe 精度不够，三路 gating 反而可能比二路更差（多了一个错误分类的维度）。\n\n(4) **Prior work 的 0.614 AUROC 意味着 \"insufficient but improvable\"** —— 这假设了信号存在但 extraction 方法不够好。但另一种解释是：信号本身就很弱（correctability 可能不是一个被模型内部清晰编码的属性），再好的 probe 也不会提升太多。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱** — \n   核心概念 \"correctability as a prediction target\" 与 Error Depth Hypothesis (arXiv:2601.00828) 在概念上高度重叠（浅错误=可修正，深错误=不可修正）；arXiv:2604.22271 已经从内部 confidence 信号角度研究了 LLM 的错误检测和修正预测；arXiv:2602.09924 已经展示了 probe-guided routing 框架。本 proposal 的方法论组件——multi-layer ensemble probe、SAE feature decomposition、representational geometry analysis——全部来自 2025-2026 年的独立论文（分别是 arXiv:2604.13386、arXiv:2604.19974、arXiv:2602.08159），组合应用到一个新目标上。这更接近于\"工程集成\"而非\"科学发现\"。剔除 surface differences 后，novelty delta 有限：将预测目标从 correctness 切换为 correctability，但 correctability 这个概念本身已被相关工作以不同名称（error depth, correction success prediction）实质性地探索。\n\n2. **Significance: 中** — \n   研究问题本身重要：LLM self-correction 的 overcorrection 问题是真实的 pain point（多篇 survey 和 benchmark 论文确认），selective correction 有实际应用价值。但本 proposal 的预期影响受限于：(a) 如果 correctability 不可靠预测（前提假设未验证），贡献退化为一个\"negative result + representational geometry analysis\"，这虽然 publishable 但影响有限；(b) 即使 positive，主要是一个工程改进（从 confidence-based routing 到 probe-based routing 的 incremental gain），不太可能改变领域的研究范式。如果核心实验结果 positive，审稿人的反应更可能是 \"reasonable extension, I would have guessed this could work\" 而非 \"surprising\"。\n\n3. **Related Work: 强** — \n   Proposal 对近期相关工作的覆盖非常全面：明确引用了 Error Depth Hypothesis (arXiv:2601.00828)、multi-layer ensemble probing (arXiv:2604.13386)、SAE feature dissociation (arXiv:2604.19974)、Confidence Manifold (arXiv:2602.08159)、Wait-token mechanisms (arXiv:2510.04128)、CoRefine (arXiv:2602.08948)。与 CoRefine 的差异化定位清晰（signal source, abstention capability, correctability specificity）。唯一的遗漏是 arXiv:2604.22271（2026.04），这篇直接研究 internal confidence signals 对 error detection and correction 的预测作用，是最直接的竞争者，proposal 未引用。此外 arXiv:2602.09924 也未被引用但在方法论上高度相关。\n\n\n【概率估计】: [12% - 22%] 中位 17%\n\n【估计理由】: \nNovelty 维度是主要瓶颈。核心贡献——correctability 作为独立预测目标——在概念上已被 Error Depth Hypothesis 和 internal confidence signals 工作实质性地触及；方法论上是对 5-6 篇近期论文技术组件的组合应用，缺乏独立的方法论创新。Significance 受限于\"条件性贡献\"结构：只有当多个未验证的前提假设同时成立时才能产生有意义的 positive result。Related Work 的良好覆盖提供了一定的下限保护，但不足以弥补 novelty 的不足。\n\n此外需要严重注意：**本 proposal 投稿 CoRL（Conference on Robot Learning）存在根本性的 venue mismatch——proposal 内容完全是 NLP interpretability / self-correction，不包含任何 robotics 相关内容**。如果确实投 CoRL，中稿概率接近 0%。上述 12-22% 的估计是假设投稿到 ACL/EMNLP/NeurIPS 等适配 venue 的情况。\n\n【主要风险】:\n1. **核心 novelty 不足**: \"Correctability as a prediction target\" 与 Error Depth Hypothesis (arXiv:2601.00828) 和 Internal Confidence Signals (arXiv:2604.22271) 在概念上重叠过多，审稿人可能认为这只是已有工作的 rebranding + 工程组合，而非独立的科学贡献。\n\n2. **核心前提假设脆弱**: Correctability 作为模型内部表征中一个可检测的独立属性，这一假设缺乏理论支撑，且已有证据（68% pure incorrectness features 是 causally inert）暗示二阶属性的信号可能更弱。如果 probe AUROC 无法显著超过 0.614 baseline，proposal 的退路（representational geometry analysis）虽然 publishable，但价值和 novelty 都很有限。\n```\n\n---\n\nSources:\n- [How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals](https://arxiv.org/html/2604.22271v1)\n- [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis](https://arxiv.org/abs/2601.00828)\n- [LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations](https://arxiv.org/abs/2602.09924)\n- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)\n- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)\n- [The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models](https://arxiv.org/html/2602.08159v1)\n- [Internal states before wait modulate reasoning patterns](https://arxiv.org/abs/2510.04128)\n- [CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute](https://arxiv.org/abs/2602.08948)\n- [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/)\n- [Can Linear Probes Measure LLM Uncertainty?](https://arxiv.org/html/2510.04108)\n- [Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation](https://arxiv.org/html/2603.05881v1)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have a comprehensive picture of the field. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. arXiv:2604.22271 — \"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals\" (Google DeepMind, April 2026):\n   **最直接的竞争工作。** 该论文已经证明 LLM 在 post-answer token 处缓存了一个内部 confidence representation，该信号不仅能检测错误，还能预测哪些错误可以被自我纠正。Proposal 中提到的 \"0.614 AUROC at PANL with single-layer linear probe\" 极可能来源于此。这意味着 proposal 的核心 claim——\"内部表征可以预测 correctability\"——已被 DeepMind 团队部分建立。\n\n2. arXiv:2604.13386 — \"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\" (April 2026):\n   Proposal 的核心技术手段（multi-layer ensemble stacking）直接来源于此。该论文在 deception detection 上展示了 multi-layer ensembling 将 AUROC 提升最高 78%。Proposal 明确标注要测试此技术是否迁移到 correctability——这是合理的，但属于\"已知技术的新应用\"而非方法创新。\n\n3. arXiv:2604.19974 — \"Are LLM Uncertainty and Correctness Encoded by the Same Features?\" (April 2026):\n   通过 SAE 发现 uncertainty 和 correctness 由不同 feature populations 编码。68% 的 pure incorrectness features 是因果惰性的。Proposal 利用这一发现做 SAE-guided feature selection，瞄准 confounded feature intersection。这是合理的技术利用，但 proposal 对其的使用仍是推测性的（\"correctability 是否依赖于 confounded features\"）。\n\n4. arXiv:2602.08948 — CoRefine (February 2026):\n   Confidence-guided self-refinement，使用 211k 参数的 Conv1D controller 实现三路决策（HALT/RETHINK/ALTERNATIVE）。Proposal 明确与之对比，声称区别在于：(a) 使用 hidden-state probes 而非 output-level confidence，(b) 真正的 abstention，(c) correctability-aware。这些区别是实质性的，但增量性质明显。\n\n5. arXiv:2602.08159 — \"The Confidence Manifold\" (February 2026):\n   已建立 correctness 在 transformer 表征中呈低维线性可分结构（3-8 维，AUC 0.80-0.97）。Proposal 要测试 correctability 是否也具有类似几何结构——这是对已有发现的自然延伸。\n\n6. arXiv:2512.20578 — Gnosis (December 2025):\n   轻量级 self-awareness mechanism，~5M 参数，双流（hidden states + attention patterns）预测 correctness。与 proposal 在技术路径上高度重叠（都是 probe hidden states to predict properties of model outputs）。\n\n7. arXiv:2601.00828 — \"Decomposing LLM Self-Correction: Error Depth Hypothesis\" (January 2026):\n   提出 stronger models make deeper errors that resist self-correction。为 proposal 的 correctability 概念提供了行为层面的动机。\n\n8. arXiv:2506.10406 — PAG (June 2025):\n   Policy as Generative Verifier，selective revision only when self-verification detects error。Proposal 将其作为 baseline 之一。\n\n- **调研总结**: 这个领域在 2025-2026 年极其活跃。\"correctness probing\" 已经成熟（AUC 0.80-0.97），内部信号预测 error self-correctability 已被 DeepMind 团队初步建立（2604.22271），confidence-based routing 已有 CoRefine 等方案。Proposal 处于\"已有发现的工程优化 + 概念细化\"的位置——将多种已有技术组合以提升 correctability probe 质量，并将 correctability 形式化为独立于 correctness 的预测目标。\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。** \n\n1. **Correctness probe + 简单阈值 gating**: 既然 correctness probes 已经能达到 0.80-0.97 AUC（The Confidence Manifold, 2602.08159），一个明显的 trivial baseline 是：用现成的 correctness probe 做 gating（\"错了就尝试纠正，对了就保留\"），而不需要专门预测\"错误是否可纠正\"。Proposal 的增量价值在于区分\"可纠正的错误\"和\"不可纠正的错误\"以避免无效的纠正尝试——但这个增量有多大取决于\"不可纠正错误\"在总错误中的占比以及无效纠正的实际损害。如果大多数错误要么容易纠正要么模型本来就不会尝试纠正，那 correctability-aware gating 的边际收益可能很小。\n\n2. **CoRefine-style confidence routing**: CoRefine 用 output-level confidence 做三路 routing，已经达到 92.6% 的 halt precision。Proposal 声称用 hidden-state probes 更好，但需要证明这个\"更好\"是 substantial 而非 marginal。\n\n增量价值的最终判断取决于实验结果——但从 idea 层面看，trivial alternative 是真实存在的威胁。\n\n【前提假设检验】:\n\n1. **核心假设：\"Correctability 是一个可在表征层面独立于 correctness 被探测到的属性\"** — 这是整个 proposal 的立足点，但完全未经验证。Correctability 是 correctness 的\"二阶属性\"（不仅要错，还要错误可被修复），它可能不会在表征空间中以独立于 correctness 的方式编码。如果 correctability 的信号完全嵌套在 correctness 信号中（即只是 correctness probe 的低置信区域），那整个 correctability-specific probing 的努力就没有增量价值。\n\n2. **迁移假设：\"multi-layer ensembling 从 deception detection 迁移到 correctability prediction\"** — Deception 涉及模型\"知道真相但说谎\"的信号，这在层间有一致的方向性旋转（论文 2604.13386 的几何解释）。Correctability 的信号可能完全不同——它不是一个\"方向\"而是一个关于模型知识边界的属性。迁移性不能想当然。\n\n3. **暗含假设：\"SAE confounded features 与 correctability 有特殊关联\"** — 2604.19974 发现 confounded features（同时编码 uncertainty 和 correctness 的特征）与 pure features 有功能差异，但没有任何证据表明这些 confounded features 编码了 correctability 信息。这一步推理是 proposal 自己的推测。\n\n【3 维度打分】:\n\n1. **Novelty: 弱** — \n   - 核心 claim \"内部表征可预测 correctability\" 已被 arXiv:2604.22271 (DeepMind) 部分建立，该论文已展示 PANL 处的内部 confidence signal 能预测哪些错误可被纠正。Proposal 的增量是\"提升 probe 质量\"（0.614 → 更高），但方法全部来自已有技术的组合（multi-layer ensembling from 2604.13386 + SAE features from 2604.19974 + attention entropy + multi-token features）。\n   - \"Correctability 作为独立于 correctness 的预测目标\"这一概念化有一定新意，但它是 correctness probing 领域的自然延伸，审稿人不太可能认为这是一个 surprising framing。\n   - Representational geometry comparison（correctability vs correctness 的几何结构对比）是最新颖的分析角度，但它更像是 2602.08159 (Confidence Manifold) 的 follow-up analysis。\n   - 综合来看，novelty 主要体现在\"已有技术的新组合 + 已有分析框架的新应用目标\"。\n\n2. **Significance: 中** — \n   - \"哪些错误可以被自我纠正\"是一个有实际价值的问题，对 LLM deployment 有直接影响。\n   - 但如果 core finding 是 positive（probes work well），审稿人可能会说 \"I would have guessed this\"——考虑到 correctness probes 已经 0.80-0.97 AUC，correctability 作为其 refinement 能被探测到并不令人意外。\n   - 如果 core finding 是 negative（probes don't improve much），贡献主要是 negative result + representational analysis，影响力有限。\n   - 三路 gating with abstention 有实用价值，但是 engineering contribution 而非 scientific insight。\n   - Error Depth Hypothesis (2601.00828) 已经提供了为什么不同错误有不同 correctability 的行为层面解释——proposal 的贡献是将其推进到表征层面，这有价值但不是 paradigm-shifting。\n\n3. **Related Work: 强** — \n   - 对领域内最新工作的覆盖非常全面，包括 2026 年 4 月的最新论文。\n   - 与 CoRefine 的差异化定位是明确且实质的（signal source, abstention, correctability specificity）。\n   - 正确引用了 multi-layer ensembling、SAE functional dissociation、Wait token mechanisms 等关键前期工作。\n   - 唯一的遗漏可能是 Gnosis (arXiv:2512.20578)——一个同样用 hidden states + attention patterns 预测 correctness 的系统，与 proposal 的技术路径高度重叠，应被讨论。\n\n【概率估计】: [15% - 25%] 中位 20%\n\n【估计理由】: \nNovelty 是限制上界的主要因素。核心 claim 已被 2604.22271 部分覆盖，技术手段是已有方法的组合，concept framing 是自然延伸而非 surprising insight。Significance 中等——问题有价值但结果无论正负都难以达到\"surprising\"的门槛。Related Work 的强覆盖提供了一定的下限保障。综合来看，这是一篇方向正确、技术到位、但缺乏让审稿人写 \"I didn't expect this\" 的核心发现的 proposal——在顶会中属于 borderline reject 到 weak reject 区间。\n\n【主要风险】: \n1. **Novelty 被 arXiv:2604.22271 实质性削弱**: DeepMind 的工作已经建立了\"内部 confidence 信号预测 correctability\"的基本结论。Proposal 的改进（更好的 probe）可能被审稿人视为 incremental engineering optimization 而非 new scientific insight。\n2. **Trivial alternative 难以击败**: 如果简单的 correctness probe + threshold gating 已经能捕获大部分 correctability 信号（因为 correctability 可能高度相关于 low-confidence errors），那么整套 ECP 方案的增量收益可能不够显著以证明其复杂性。\n```\n\nSources:\n- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)\n- [Linear Probe Accuracy Scales with Model Size (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)\n- [Are LLM Uncertainty and Correctness Encoded by the Same Features? (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)\n- [CoRefine: Confidence-Guided Self-Refinement (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)\n- [The Confidence Manifold (arXiv:2602.08159)](https://arxiv.org/html/2602.08159v1)\n- [Can LLMs Predict Their Own Failures? Gnosis (arXiv:2512.20578)](https://arxiv.org/abs/2512.20578)\n- [Decomposing LLM Self-Correction: Error Depth Hypothesis (arXiv:2601.00828)](https://arxiv.org/abs/2601.00828)\n- [Internal states before wait modulate reasoning patterns (arXiv:2510.04128)](https://arxiv.org/abs/2510.04128)\n- [PAG: Multi-Turn Reinforced LLM Self-Correction (arXiv:2506.10406)](https://arxiv.org/abs/2506.10406)\n- [LLM Reasoning as Trajectories (arXiv:2604.05655)](https://arxiv.org/pdf/2604.05655)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\" (arXiv:2602.08159, 2026):\n   最直接的竞争性工作。已证明 correctness 在 transformer hidden states 中是低维(3-8维)、线性可分的，linear probes 达到 0.80-0.97 AUC，远超 output-based 方法(0.44-0.64 AUC)。这意味着 correctness probing 已经是一个成熟的技术——本 proposal 的 correctability probing 需要证明自己在 correctness probing 之上有增量价值。\n\n2. \"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders\" (arXiv:2604.19974, 2026):\n   本 proposal 直接依赖的基础工作。已发现 uncertainty 和 correctness 由不同 feature populations 编码（pure uncertainty features, pure incorrectness features, confounded features），且 68% 的 pure incorrectness features 是 causally inert。本 proposal 拟将此框架扩展到 correctability，但这个扩展的增量价值需要论证。\n\n3. \"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\" (arXiv:2604.13386, 2026):\n   本 proposal 拟迁移的技术来源。已证明 multi-layer ensemble 在 deception detection 上相比 single-layer 可提升 AUROC 达 78%。本 proposal 的核心技术贡献之一（multi-layer ensembling for correctability）本质上是该技术的直接应用。\n\n4. \"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute\" (arXiv:2602.08948, 2026):\n   最直接的系统级竞争者。已实现三路路由(HALT/RETHINK/ALTERNATIVE)，用 211K 参数 Conv1D controller 在 confidence features 上做决策，halting precision 达 92.6%。本 proposal 需要证明 hidden-state probe 比 output-level confidence 更优。\n\n5. \"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis\" (arXiv:2601.00828, 2025):\n   提出 Error Depth Hypothesis——更强的模型犯更少但更深的错误，深错误抗拒自我修正。这为 correctability 的异质性提供了经验证据，但也暗示了一个 trivial baseline：correctability ≈ f(error depth)，而 error depth 可能通过 correctness probe confidence 近似估计。\n\n6. \"Internal states before wait modulate reasoning patterns\" (arXiv:2510.04128, 2025):\n   分析了 Wait token 前的 hidden states 如何影响后续推理模式。本 proposal 拟利用这些 pre-Wait features，但该论文已做了大量 crosscoder 分析，留给 proposal 的新贡献空间有限。\n\n7. \"LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations\" (arXiv:2602.09924, 2026, ICLR 2026 LIT Workshop):\n   用 pre-generation activations 上的 linear probes 预测 task success。证明了 LLM 内部编码了 model-specific 的难度信号。但该工作预测的是\"是否会答对\"（correctness），而非\"答错了能否修正\"（correctability），这是本 proposal 声称的关键区分。\n\n8. \"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals\" (arXiv:2604.22271, 2026):\n   直接相关但 proposal 未引用。研究 LLM 内部 confidence signals 在 error detection 和 self-correction 中的角色，声称 confidence signals 可以 predict which errors the model can correct。这与本 proposal 的核心 claim 高度重叠。\n\n- 调研总结: LLM 内部表征对 correctness 的编码已被充分研究(linear probes 达 0.80-0.97 AUC)，uncertainty 与 correctness 的 feature dissociation 已被 SAE 分析揭示，confidence-based routing 已有成熟方案(CoRefine)。本 proposal 处于这些工作的交叉地带，试图将 probing 目标从 correctness 推进到 correctability，但这个概念距离上的推进在技术上是否对应一个genuinely distinct internal signal 尚不清楚。同时，arXiv:2604.22271 已在非常接近的方向上开展工作，对 novelty 构成实质威胁。\n\n\n【Trivial Alternative 检验】:\n\n**存在明确的 trivial alternative 威胁。** \n\n最直接的替代方案：将已有的 correctness probe (0.80-0.97 AUC, arXiv:2602.08159) 与 uncertainty probe 简单组合——如果模型 (1) 被探测为\"大概率错误\"且 (2) 具有高 uncertainty，则尝试修正；如果 (1) 大概率错误但 (2) 低 uncertainty（即\"自信地犯错\"），则 abstain。这种组合不需要引入\"correctability\"作为独立的预测目标，只需要现成的 correctness + uncertainty probes 的逻辑运算。\n\n第二个替代方案：CoRefine 的 confidence-based controller 已经在 output-level features 上实现了三路路由且 halting precision 达 92.6%。本 proposal 需要证明 hidden-state probes 提供的增量超过 output-level confidence features，而 arXiv:2602.08159 虽然显示 internal probes > output-based methods 在 correctness detection 上，但这不等同于在 routing/gating 任务上也成立。\n\n**增量价值的关键条件**：本 proposal 的增量价值完全取决于一个未经验证的假设——\"correctability 是一个在模型内部有独立表征的信号，不可还原为 correctness + uncertainty 的组合\"。如果这个假设不成立，整个 elaborate probe 构建就是过度工程化。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的关键假设：\n\n1. **\"Correctability 是一个内部编码的独立属性\"假设**（最关键）：\n   一个错误是否可自修正，可能并非模型在生成错误答案时已经\"知道\"的信息，而是取决于修正过程中的 stochastic factors（采样温度、prompt 形式、解码策略等）。如果 correctability 不是模型 hidden state 中的确定性属性，而是修正过程的涌现结果，那么从 pre-correction hidden state 去预测它在原理上就存在 ceiling。Error Depth Hypothesis (arXiv:2601.00828) 暗示 correctability 与 error depth 相关，但 error depth 本身可能不完全由 hidden state 编码。\n\n2. **\"Multi-layer ensembling 从 deception 迁移到 correctability\"假设**：\n   Deception detection 的信号结构（deception direction 跨层缓慢旋转）可能与 correctability 的信号结构有本质不同。Deception 涉及模型\"知道真答案但选择说谎\"，信号清晰；correctability 涉及\"模型不确定是否能找到正确答案\"，信号可能更模糊、更分散。直接迁移的合理性需要论证。\n\n3. **\"PANL + last-answer-token + reasoning tokens 的 multi-token 组合能提升 probe 性能\"假设**：\n   arXiv:2602.08159 已证明 correctness signal 只需 3-8 维就能捕获，暗示信号结构简单。添加更多 token positions 和 feature types 可能导致过拟合而非性能提升。proposal 缺少对这一 over-parameterization 风险的讨论。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   \"Correctability 作为独立预测目标\"这一概念确实新颖，但增量有限。技术层面几乎全部借用自近期工作：multi-layer ensembling 直接来自 arXiv:2604.13386，SAE feature decomposition 框架来自 arXiv:2604.19974，representational geometry 分析来自 arXiv:2602.08159。更关键的是，arXiv:2604.22271 已经在研究 \"internal confidence signals predict which errors the model can correct\"——与本 proposal 的核心 claim 高度重叠。剥离 surface differences 后，本 proposal 的核心新增量是 (a) 将 correctability 形式化为独立预测目标，(b) 与 correctness 做 representational geometry 对比。(a) 是一个好的 framing 但不是 deep insight；(b) 是一个有意思的实验但结论可能是 \"correctability 的表征结构与 correctness 类似\"——这在审稿人看来属于 \"I would have guessed this\"。\n\n2. **Significance: 中** — \n   \"哪些错误值得修正、哪些应该 abstain\"在实际部署中确实重要。如果 probe-gated correction 能可靠工作，对 test-time compute allocation 有实际价值。但问题的重要性被两个因素削弱：(a) CoRefine 等 output-level 方案已经在实用层面解决了类似问题（92.6% halting precision），hidden-state probe 的增量收益可能不足以 justify 额外的复杂性；(b) 随着 reasoning models 和 extended thinking 的快速发展，self-correction 本身的范式可能正在被超越——模型可能会通过更好的 initial reasoning 而非 post-hoc correction 来提升准确率。\n\n3. **Related Work: 中** — \n   对 CoRefine、Error Depth Hypothesis、SAE dissociation、Wait token 机制等的引用是准确和相关的。但缺失了一些直接竞争的工作：arXiv:2604.22271 (\"How LLMs Detect and Correct Their Own Errors\") 研究的方向与本 proposal 高度重叠但未被引用；arXiv:2512.20578 (\"Can LLMs Predict Their Own Failures?\") 和 arXiv:2510.16062 (CorrectBench) 也是应该讨论的工作。与 CoRefine 的差异化定位虽然有尝试（hidden-state vs. output-level, genuine abstention），但论证深度不足——proposal 未能解释为什么 hidden-state probe 在 gating 任务上比 output-level confidence 更优的理论原因。\n\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】: \nNovelty 是主要限制维度。核心概念（correctability as distinct target）有新颖性但增量有限——剥离借用的技术后，真正新的 insight 薄弱，且 arXiv:2604.22271 已在高度重叠的方向上工作。Significance 受限于 CoRefine 等 output-level 方案已提供了实用的替代方案。最关键的风险是 Trivial Alternative 威胁：correctness probe + uncertainty probe 的简单组合可能达到接近的 gating 效果，使得 correctability 作为独立信号的 value proposition 不成立。proposal 的\"kitchen-sink\"风格（堆叠多层 ensemble、multi-token features、attention entropy、SAE features、crosscoder analysis 等）反映了对核心 idea 深度的不自信，审稿人可能会批评 contribution 不够 focused。dual-outcome 保底策略（\"even if probe AUROC plateaus\"）虽然务实，但从 idea 评估角度看是一个负面信号——proposal 自身暗示了核心 result 可能为 negative。\n\n【主要风险】: \n1. **Correctability 不是独立信号风险**：如果 correctability ≈ correctness + uncertainty 的组合，核心 contribution 瓦解，trivial baseline (correctness probe + uncertainty threshold) 即可 replicate 主要效果\n2. **与 arXiv:2604.22271 的重叠风险**：该工作已研究 internal confidence signals 如何 predict which errors the model can correct，如果在 submission 前该工作被进一步发展或被顶会接收，本 proposal 的 novelty claim 将受到严重质疑\n```\n\nSources:\n- [The Confidence Manifold (arXiv:2602.08159)](https://arxiv.org/pdf/2602.08159)\n- [SAE Functional Dissociation (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)\n- [Multi-Layer Ensemble Probing (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)\n- [CoRefine (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)\n- [Error Depth Hypothesis (arXiv:2601.00828)](https://arxiv.org/abs/2601.00828)\n- [Wait Token Mechanisms (arXiv:2510.04128)](https://arxiv.org/abs/2510.04128)\n- [LLMs Encode Their Failures (arXiv:2602.09924)](https://arxiv.org/abs/2602.09924)\n- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)\n- [Can LLMs Predict Their Own Failures? (arXiv:2512.20578)](https://arxiv.org/abs/2512.20578)\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/html/2507.02778v1)\n- [CorrectBench (arXiv:2510.16062)](https://arxiv.org/abs/2510.16062)\n- [Reflective Confidence (arXiv:2512.18605)](https://arxiv.org/pdf/2512.18605)\n- [PAG (arXiv:2506.10406)](https://arxiv.org/pdf/2506.10406)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:31:08.622Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:31:08.622Z",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:31:08.649Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
现在我已经完成了充分的领域调研，可以进行系统评估了。

---

```
【阶段】: Triage

【领域调研】:

1. [arXiv:2604.22271] "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals" (2026.04):
   — 直接竞争者。该论文从决策神经科学的"二阶模型"出发，研究 LLM 内部的评价性信号如何驱动错误检测与自我修正，发现 LLM 缓存了一个独立于 log-prob 的评价性表征，能预测哪些错误模型可以修正。这与本 proposal 的核心 claim（用内部表征预测 correctability）高度重叠。

2. [arXiv:2601.00828] "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis" (2025.12):
   — 直接前驱。该论文将 self-correction 分解为 error detection / localization / correction 三个子能力，提出 Error Depth Hypothesis：强模型犯的错误更"深"、更抗修正。这在概念层面与 "correctability" 作为预测目标高度一致——"浅错误=可修正，深错误=不可修正"。

3. [arXiv:2602.09924] "LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations" (2026.02):
   — 密切相关。该论文训练 linear probe on pre-generation activations 预测模型是否会答对，并展示 probe-guided routing 可在减少 40% 计算成本的同时匹配高计算精度。方法论上（probe → gating）与本 proposal 的框架非常接近，区别仅在目标（correctness vs. correctability）。

4. [arXiv:2604.13386] "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (2026.04):
   — 本 proposal 直接引用的方法来源。该论文证明多层 ensemble probe 在 deception detection 上大幅优于单层 probe（+78% AUROC on Harm-Pressure Knowledge）。本 proposal 的"Phase 0 pilot"本质是测试此技术是否 transfer 到 correctability 任务。

5. [arXiv:2604.19974] "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (2026.04):
   — 本 proposal 引用的 SAE 分析基础。该论文区分了 pure uncertainty / pure incorrectness / confounded features 三类特征，发现 68% 的 pure incorrectness features 在因果干预下是 inert 的。本 proposal 拟将此分析框架延伸到 correctability。

6. [arXiv:2602.08159] "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models" (2026.02):
   — 本 proposal 引用的几何分析基础。该论文在 9 个模型上发现 correctness 信号占据 3-8 维、线性可分、非线性分类器无额外提升。本 proposal 拟测试 correctability（二阶属性）是否也具有类似结构。

7. [arXiv:2510.04128] "Internal states before wait modulate reasoning patterns" (2025.10):
   — 本 proposal 引用的 Wait-token 机制分析。使用 crosscoder 定位影响 wait token 概率的特征集。

8. [arXiv:2602.08948] "CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute" (2026.02):
   — 本 proposal 的主要对比系统。CoRefine 使用 output-level confidence 做三路路由（HALT/RETHINK/ALTERNATIVE），211K 参数 Conv1D controller，精度 92.6%。

- 调研总结: 2025-2026 年间，LLM 自我修正的 probe-based gating、内部表征对 correctness/uncertainty 的编码、以及 self-correction 的分解分析已成为非常拥挤的研究方向。本 proposal 的每一个技术组件（multi-layer ensemble probe、SAE feature decomposition、representational geometry analysis、probe-gated routing）均已在近期独立论文中被提出和验证。Proposal 的差异化定位在于将预测目标从 "correctness" 切换为 "correctability"，但这一概念与 Error Depth Hypothesis 和内部 confidence 信号的工作存在显著重叠。


【Trivial Alternative 检验】:
存在多个成本更低的 trivial alternatives：

(1) **直接用 correctness probe 做代理**：既然已经有成熟的 correctness linear probe（AUROC ~0.87，见 LLM Reasoning as Trajectories），可以简单地"检测错误 → 一律尝试修正"，省去 correctability 预测这一步。Proposal 的增量价值取决于"可修正"vs."不可修正"的区分能否提供超过 correctness probe 的显著收益——但这本身是一个 empirical claim，且 Error Depth Hypothesis 已经暗示更强的模型犯的错更少但更难修正，意味着 correctability prediction 可能本身就很难（大多数错误要么都可修正，要么都不可修正）。

(2) **CoRefine 的 confidence-based routing**：CoRefine 使用 output-level confidence 做 routing，精度达 92.6%，且只需 211K 参数。本 proposal 使用 hidden-state probe 做 routing 的增量收益需要超过这个强 baseline，但 hidden-state probe 的额外复杂度（multi-layer extraction, SAE feature selection）是否值得，是一个未回答的问题。

(3) **简单的 logit entropy / verbalized confidence**：多篇论文已表明 logit-based uncertainty 和 verbalized confidence 在某些场景下已经是有效的 proxy。

增量价值在于：如果 correctability 确实是一个与 correctness 不同的、可预测的内部属性，且其预测能带来超越 confidence-based routing 的 gating 收益。但这是一个层层叠加的条件假设，每层都有 fail 的风险。


【前提假设检验】:
核心 claim 的逻辑链存在多个未验证的前提假设：

(1) **"Correctability 是模型内部表征中一个可检测的、与 correctness 不同的独立属性"** —— 这是最关键的假设，完全没有理论或实证支撑。已有证据反而不利：arXiv:2604.19974 发现 68% 的 pure incorrectness features 是 causally inert 的。如果 correctness 的一阶属性都在内部表征中缺乏 causal footprint，一个依赖于 correctness 的二阶属性（correctability = "wrong AND fixable"）为什么会有更强的可检测信号？没有理论解释。

(2) **"Multi-layer ensemble 从 deception detection transfer 到 correctability"** —— Deception 是一个有意的、二元的行为（模型"知道"正确答案但选择输出错误答案），内部表征的几何结构可能与 correctability（模型不知道正确答案但可能通过 reasoning 找到）完全不同。Transfer 假设缺乏理论支撑。

(3) **"三路 gating 优于二路 gating"** —— 添加 abstain 选项的前提是 correctability probe 能可靠区分"可修正"和"不可修正"的错误。如果 probe 精度不够，三路 gating 反而可能比二路更差（多了一个错误分类的维度）。

(4) **Prior work 的 0.614 AUROC 意味着 "insufficient but improvable"** —— 这假设了信号存在但 extraction 方法不够好。但另一种解释是：信号本身就很弱（correctability 可能不是一个被模型内部清晰编码的属性），再好的 probe 也不会提升太多。


【3 维度打分】:

1. **Novelty: 弱** — 
   核心概念 "correctability as a prediction target" 与 Error Depth Hypothesis (arXiv:2601.00828) 在概念上高度重叠（浅错误=可修正，深错误=不可修正）；arXiv:2604.22271 已经从内部 confidence 信号角度研究了 LLM 的错误检测和修正预测；arXiv:2602.09924 已经展示了 probe-guided routing 框架。本 proposal 的方法论组件——multi-layer ensemble probe、SAE feature decomposition、representational geometry analysis——全部来自 2025-2026 年的独立论文（分别是 arXiv:2604.13386、arXiv:2604.19974、arXiv:2602.08159），组合应用到一个新目标上。这更接近于"工程集成"而非"科学发现"。剔除 surface differences 后，novelty delta 有限：将预测目标从 correctness 切换为 correctability，但 correctability 这个概念本身已被相关工作以不同名称（error depth, correction success prediction）实质性地探索。

2. **Significance: 中** — 
   研究问题本身重要：LLM self-correction 的 overcorrection 问题是真实的 pain point（多篇 survey 和 benchmark 论文确认），selective correction 有实际应用价值。但本 proposal 的预期影响受限于：(a) 如果 correctability 不可靠预测（前提假设未验证），贡献退化为一个"negative result + representational geometry analysis"，这虽然 publishable 但影响有限；(b) 即使 positive，主要是一个工程改进（从 confidence-based routing 到 probe-based routing 的 incremental gain），不太可能改变领域的研究范式。如果核心实验结果 positive，审稿人的反应更可能是 "reasonable extension, I would have guessed this could work" 而非 "surprising"。

3. **Related Work: 强** — 
   Proposal 对近期相关工作的覆盖非常全面：明确引用了 Error Depth Hypothesis (arXiv:2601.00828)、multi-layer ensemble probing (arXiv:2604.13386)、SAE feature dissociation (arXiv:2604.19974)、Confidence Manifold (arXiv:2602.08159)、Wait-token mechanisms (arXiv:2510.04128)、CoRefine (arXiv:2602.08948)。与 CoRefine 的差异化定位清晰（signal source, abstention capability, correctability specificity）。唯一的遗漏是 arXiv:2604.22271（2026.04），这篇直接研究 internal confidence signals 对 error detection and correction 的预测作用，是最直接的竞争者，proposal 未引用。此外 arXiv:2602.09924 也未被引用但在方法论上高度相关。


【概率估计】: [12% - 22%] 中位 17%

【估计理由】: 
Novelty 维度是主要瓶颈。核心贡献——correctability 作为独立预测目标——在概念上已被 Error Depth Hypothesis 和 internal confidence signals 工作实质性地触及；方法论上是对 5-6 篇近期论文技术组件的组合应用，缺乏独立的方法论创新。Significance 受限于"条件性贡献"结构：只有当多个未验证的前提假设同时成立时才能产生有意义的 positive result。Related Work 的良好覆盖提供了一定的下限保护，但不足以弥补 novelty 的不足。

此外需要严重注意：**本 proposal 投稿 CoRL（Conference on Robot Learning）存在根本性的 venue mismatch——proposal 内容完全是 NLP interpretability / self-correction，不包含任何 robotics 相关内容**。如果确实投 CoRL，中稿概率接近 0%。上述 12-22% 的估计是假设投稿到 ACL/EMNLP/NeurIPS 等适配 venue 的情况。

【主要风险】:
1. **核心 novelty 不足**: "Correctability as a prediction target" 与 Error Depth Hypothesis (arXiv:2601.00828) 和 Internal Confidence Signals (arXiv:2604.22271) 在概念上重叠过多，审稿人可能认为这只是已有工作的 rebranding + 工程组合，而非独立的科学贡献。

2. **核心前提假设脆弱**: Correctability 作为模型内部表征中一个可检测的独立属性，这一假设缺乏理论支撑，且已有证据（68% pure incorrectness features 是 causally inert）暗示二阶属性的信号可能更弱。如果 probe AUROC 无法显著超过 0.614 baseline，proposal 的退路（representational geometry analysis）虽然 publishable，但价值和 novelty 都很有限。
```

---

Sources:
- [How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals](https://arxiv.org/html/2604.22271v1)
- [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis](https://arxiv.org/abs/2601.00828)
- [LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations](https://arxiv.org/abs/2602.09924)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)
- [The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models](https://arxiv.org/html/2602.08159v1)
- [Internal states before wait modulate reasoning patterns](https://arxiv.org/abs/2510.04128)
- [CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute](https://arxiv.org/abs/2602.08948)
- [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/)
- [Can Linear Probes Measure LLM Uncertainty?](https://arxiv.org/html/2510.04108)
- [Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation](https://arxiv.org/html/2603.05881v1)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have a comprehensive picture of the field. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. arXiv:2604.22271 — "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals" (Google DeepMind, April 2026):
   **最直接的竞争工作。** 该论文已经证明 LLM 在 post-answer token 处缓存了一个内部 confidence representation，该信号不仅能检测错误，还能预测哪些错误可以被自我纠正。Proposal 中提到的 "0.614 AUROC at PANL with single-layer linear probe" 极可能来源于此。这意味着 proposal 的核心 claim——"内部表征可以预测 correctability"——已被 DeepMind 团队部分建立。

2. arXiv:2604.13386 — "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (April 2026):
   Proposal 的核心技术手段（multi-layer ensemble stacking）直接来源于此。该论文在 deception detection 上展示了 multi-layer ensembling 将 AUROC 提升最高 78%。Proposal 明确标注要测试此技术是否迁移到 correctability——这是合理的，但属于"已知技术的新应用"而非方法创新。

3. arXiv:2604.19974 — "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (April 2026):
   通过 SAE 发现 uncertainty 和 correctness 由不同 feature populations 编码。68% 的 pure incorrectness features 是因果惰性的。Proposal 利用这一发现做 SAE-guided feature selection，瞄准 confounded feature intersection。这是合理的技术利用，但 proposal 对其的使用仍是推测性的（"correctability 是否依赖于 confounded features"）。

4. arXiv:2602.08948 — CoRefine (February 2026):
   Confidence-guided self-refinement，使用 211k 参数的 Conv1D controller 实现三路决策（HALT/RETHINK/ALTERNATIVE）。Proposal 明确与之对比，声称区别在于：(a) 使用 hidden-state probes 而非 output-level confidence，(b) 真正的 abstention，(c) correctability-aware。这些区别是实质性的，但增量性质明显。

5. arXiv:2602.08159 — "The Confidence Manifold" (February 2026):
   已建立 correctness 在 transformer 表征中呈低维线性可分结构（3-8 维，AUC 0.80-0.97）。Proposal 要测试 correctability 是否也具有类似几何结构——这是对已有发现的自然延伸。

6. arXiv:2512.20578 — Gnosis (December 2025):
   轻量级 self-awareness mechanism，~5M 参数，双流（hidden states + attention patterns）预测 correctness。与 proposal 在技术路径上高度重叠（都是 probe hidden states to predict properties of model outputs）。

7. arXiv:2601.00828 — "Decomposing LLM Self-Correction: Error Depth Hypothesis" (January 2026):
   提出 stronger models make deeper errors that resist self-correction。为 proposal 的 correctability 概念提供了行为层面的动机。

8. arXiv:2506.10406 — PAG (June 2025):
   Policy as Generative Verifier，selective revision only when self-verification detects error。Proposal 将其作为 baseline 之一。

- **调研总结**: 这个领域在 2025-2026 年极其活跃。"correctness probing" 已经成熟（AUC 0.80-0.97），内部信号预测 error self-correctability 已被 DeepMind 团队初步建立（2604.22271），confidence-based routing 已有 CoRefine 等方案。Proposal 处于"已有发现的工程优化 + 概念细化"的位置——将多种已有技术组合以提升 correctability probe 质量，并将 correctability 形式化为独立于 correctness 的预测目标。

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 

1. **Correctness probe + 简单阈值 gating**: 既然 correctness probes 已经能达到 0.80-0.97 AUC（The Confidence Manifold, 2602.08159），一个明显的 trivial baseline 是：用现成的 correctness probe 做 gating（"错了就尝试纠正，对了就保留"），而不需要专门预测"错误是否可纠正"。Proposal 的增量价值在于区分"可纠正的错误"和"不可纠正的错误"以避免无效的纠正尝试——但这个增量有多大取决于"不可纠正错误"在总错误中的占比以及无效纠正的实际损害。如果大多数错误要么容易纠正要么模型本来就不会尝试纠正，那 correctability-aware gating 的边际收益可能很小。

2. **CoRefine-style confidence routing**: CoRefine 用 output-level confidence 做三路 routing，已经达到 92.6% 的 halt precision。Proposal 声称用 hidden-state probes 更好，但需要证明这个"更好"是 substantial 而非 marginal。

增量价值的最终判断取决于实验结果——但从 idea 层面看，trivial alternative 是真实存在的威胁。

【前提假设检验】:

1. **核心假设："Correctability 是一个可在表征层面独立于 correctness 被探测到的属性"** — 这是整个 proposal 的立足点，但完全未经验证。Correctability 是 correctness 的"二阶属性"（不仅要错，还要错误可被修复），它可能不会在表征空间中以独立于 correctness 的方式编码。如果 correctability 的信号完全嵌套在 correctness 信号中（即只是 correctness probe 的低置信区域），那整个 correctability-specific probing 的努力就没有增量价值。

2. **迁移假设："multi-layer ensembling 从 deception detection 迁移到 correctability prediction"** — Deception 涉及模型"知道真相但说谎"的信号，这在层间有一致的方向性旋转（论文 2604.13386 的几何解释）。Correctability 的信号可能完全不同——它不是一个"方向"而是一个关于模型知识边界的属性。迁移性不能想当然。

3. **暗含假设："SAE confounded features 与 correctability 有特殊关联"** — 2604.19974 发现 confounded features（同时编码 uncertainty 和 correctness 的特征）与 pure features 有功能差异，但没有任何证据表明这些 confounded features 编码了 correctability 信息。这一步推理是 proposal 自己的推测。

【3 维度打分】:

1. **Novelty: 弱** — 
   - 核心 claim "内部表征可预测 correctability" 已被 arXiv:2604.22271 (DeepMind) 部分建立，该论文已展示 PANL 处的内部 confidence signal 能预测哪些错误可被纠正。Proposal 的增量是"提升 probe 质量"（0.614 → 更高），但方法全部来自已有技术的组合（multi-layer ensembling from 2604.13386 + SAE features from 2604.19974 + attention entropy + multi-token features）。
   - "Correctability 作为独立于 correctness 的预测目标"这一概念化有一定新意，但它是 correctness probing 领域的自然延伸，审稿人不太可能认为这是一个 surprising framing。
   - Representational geometry comparison（correctability vs correctness 的几何结构对比）是最新颖的分析角度，但它更像是 2602.08159 (Confidence Manifold) 的 follow-up analysis。
   - 综合来看，novelty 主要体现在"已有技术的新组合 + 已有分析框架的新应用目标"。

2. **Significance: 中** — 
   - "哪些错误可以被自我纠正"是一个有实际价值的问题，对 LLM deployment 有直接影响。
   - 但如果 core finding 是 positive（probes work well），审稿人可能会说 "I would have guessed this"——考虑到 correctness probes 已经 0.80-0.97 AUC，correctability 作为其 refinement 能被探测到并不令人意外。
   - 如果 core finding 是 negative（probes don't improve much），贡献主要是 negative result + representational analysis，影响力有限。
   - 三路 gating with abstention 有实用价值，但是 engineering contribution 而非 scientific insight。
   - Error Depth Hypothesis (2601.00828) 已经提供了为什么不同错误有不同 correctability 的行为层面解释——proposal 的贡献是将其推进到表征层面，这有价值但不是 paradigm-shifting。

3. **Related Work: 强** — 
   - 对领域内最新工作的覆盖非常全面，包括 2026 年 4 月的最新论文。
   - 与 CoRefine 的差异化定位是明确且实质的（signal source, abstention, correctability specificity）。
   - 正确引用了 multi-layer ensembling、SAE functional dissociation、Wait token mechanisms 等关键前期工作。
   - 唯一的遗漏可能是 Gnosis (arXiv:2512.20578)——一个同样用 hidden states + attention patterns 预测 correctness 的系统，与 proposal 的技术路径高度重叠，应被讨论。

【概率估计】: [15% - 25%] 中位 20%

【估计理由】: 
Novelty 是限制上界的主要因素。核心 claim 已被 2604.22271 部分覆盖，技术手段是已有方法的组合，concept framing 是自然延伸而非 surprising insight。Significance 中等——问题有价值但结果无论正负都难以达到"surprising"的门槛。Related Work 的强覆盖提供了一定的下限保障。综合来看，这是一篇方向正确、技术到位、但缺乏让审稿人写 "I didn't expect this" 的核心发现的 proposal——在顶会中属于 borderline reject 到 weak reject 区间。

【主要风险】: 
1. **Novelty 被 arXiv:2604.22271 实质性削弱**: DeepMind 的工作已经建立了"内部 confidence 信号预测 correctability"的基本结论。Proposal 的改进（更好的 probe）可能被审稿人视为 incremental engineering optimization 而非 new scientific insight。
2. **Trivial alternative 难以击败**: 如果简单的 correctness probe + threshold gating 已经能捕获大部分 correctability 信号（因为 correctability 可能高度相关于 low-confidence errors），那么整套 ECP 方案的增量收益可能不够显著以证明其复杂性。
```

Sources:
- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)
- [Linear Probe Accuracy Scales with Model Size (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features? (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)
- [CoRefine: Confidence-Guided Self-Refinement (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)
- [The Confidence Manifold (arXiv:2602.08159)](https://arxiv.org/html/2602.08159v1)
- [Can LLMs Predict Their Own Failures? Gnosis (arXiv:2512.20578)](https://arxiv.org/abs/2512.20578)
- [Decomposing LLM Self-Correction: Error Depth Hypothesis (arXiv:2601.00828)](https://arxiv.org/abs/2601.00828)
- [Internal states before wait modulate reasoning patterns (arXiv:2510.04128)](https://arxiv.org/abs/2510.04128)
- [PAG: Multi-Turn Reinforced LLM Self-Correction (arXiv:2506.10406)](https://arxiv.org/abs/2506.10406)
- [LLM Reasoning as Trajectories (arXiv:2604.05655)](https://arxiv.org/pdf/2604.05655)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models" (arXiv:2602.08159, 2026):
   最直接的竞争性工作。已证明 correctness 在 transformer hidden states 中是低维(3-8维)、线性可分的，linear probes 达到 0.80-0.97 AUC，远超 output-based 方法(0.44-0.64 AUC)。这意味着 correctness probing 已经是一个成熟的技术——本 proposal 的 correctability probing 需要证明自己在 correctness probing 之上有增量价值。

2. "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders" (arXiv:2604.19974, 2026):
   本 proposal 直接依赖的基础工作。已发现 uncertainty 和 correctness 由不同 feature populations 编码（pure uncertainty features, pure incorrectness features, confounded features），且 68% 的 pure incorrectness features 是 causally inert。本 proposal 拟将此框架扩展到 correctability，但这个扩展的增量价值需要论证。

3. "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (arXiv:2604.13386, 2026):
   本 proposal 拟迁移的技术来源。已证明 multi-layer ensemble 在 deception detection 上相比 single-layer 可提升 AUROC 达 78%。本 proposal 的核心技术贡献之一（multi-layer ensembling for correctability）本质上是该技术的直接应用。

4. "CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute" (arXiv:2602.08948, 2026):
   最直接的系统级竞争者。已实现三路路由(HALT/RETHINK/ALTERNATIVE)，用 211K 参数 Conv1D controller 在 confidence features 上做决策，halting precision 达 92.6%。本 proposal 需要证明 hidden-state probe 比 output-level confidence 更优。

5. "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis" (arXiv:2601.00828, 2025):
   提出 Error Depth Hypothesis——更强的模型犯更少但更深的错误，深错误抗拒自我修正。这为 correctability 的异质性提供了经验证据，但也暗示了一个 trivial baseline：correctability ≈ f(error depth)，而 error depth 可能通过 correctness probe confidence 近似估计。

6. "Internal states before wait modulate reasoning patterns" (arXiv:2510.04128, 2025):
   分析了 Wait token 前的 hidden states 如何影响后续推理模式。本 proposal 拟利用这些 pre-Wait features，但该论文已做了大量 crosscoder 分析，留给 proposal 的新贡献空间有限。

7. "LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations" (arXiv:2602.09924, 2026, ICLR 2026 LIT Workshop):
   用 pre-generation activations 上的 linear probes 预测 task success。证明了 LLM 内部编码了 model-specific 的难度信号。但该工作预测的是"是否会答对"（correctness），而非"答错了能否修正"（correctability），这是本 proposal 声称的关键区分。

8. "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals" (arXiv:2604.22271, 2026):
   直接相关但 proposal 未引用。研究 LLM 内部 confidence signals 在 error detection 和 self-correction 中的角色，声称 confidence signals 可以 predict which errors the model can correct。这与本 proposal 的核心 claim 高度重叠。

- 调研总结: LLM 内部表征对 correctness 的编码已被充分研究(linear probes 达 0.80-0.97 AUC)，uncertainty 与 correctness 的 feature dissociation 已被 SAE 分析揭示，confidence-based routing 已有成熟方案(CoRefine)。本 proposal 处于这些工作的交叉地带，试图将 probing 目标从 correctness 推进到 correctability，但这个概念距离上的推进在技术上是否对应一个genuinely distinct internal signal 尚不清楚。同时，arXiv:2604.22271 已在非常接近的方向上开展工作，对 novelty 构成实质威胁。


【Trivial Alternative 检验】:

**存在明确的 trivial alternative 威胁。** 

最直接的替代方案：将已有的 correctness probe (0.80-0.97 AUC, arXiv:2602.08159) 与 uncertainty probe 简单组合——如果模型 (1) 被探测为"大概率错误"且 (2) 具有高 uncertainty，则尝试修正；如果 (1) 大概率错误但 (2) 低 uncertainty（即"自信地犯错"），则 abstain。这种组合不需要引入"correctability"作为独立的预测目标，只需要现成的 correctness + uncertainty probes 的逻辑运算。

第二个替代方案：CoRefine 的 confidence-based controller 已经在 output-level features 上实现了三路路由且 halting precision 达 92.6%。本 proposal 需要证明 hidden-state probes 提供的增量超过 output-level confidence features，而 arXiv:2602.08159 虽然显示 internal probes > output-based methods 在 correctness detection 上，但这不等同于在 routing/gating 任务上也成立。

**增量价值的关键条件**：本 proposal 的增量价值完全取决于一个未经验证的假设——"correctability 是一个在模型内部有独立表征的信号，不可还原为 correctness + uncertainty 的组合"。如果这个假设不成立，整个 elaborate probe 构建就是过度工程化。


【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的关键假设：

1. **"Correctability 是一个内部编码的独立属性"假设**（最关键）：
   一个错误是否可自修正，可能并非模型在生成错误答案时已经"知道"的信息，而是取决于修正过程中的 stochastic factors（采样温度、prompt 形式、解码策略等）。如果 correctability 不是模型 hidden state 中的确定性属性，而是修正过程的涌现结果，那么从 pre-correction hidden state 去预测它在原理上就存在 ceiling。Error Depth Hypothesis (arXiv:2601.00828) 暗示 correctability 与 error depth 相关，但 error depth 本身可能不完全由 hidden state 编码。

2. **"Multi-layer ensembling 从 deception 迁移到 correctability"假设**：
   Deception detection 的信号结构（deception direction 跨层缓慢旋转）可能与 correctability 的信号结构有本质不同。Deception 涉及模型"知道真答案但选择说谎"，信号清晰；correctability 涉及"模型不确定是否能找到正确答案"，信号可能更模糊、更分散。直接迁移的合理性需要论证。

3. **"PANL + last-answer-token + reasoning tokens 的 multi-token 组合能提升 probe 性能"假设**：
   arXiv:2602.08159 已证明 correctness signal 只需 3-8 维就能捕获，暗示信号结构简单。添加更多 token positions 和 feature types 可能导致过拟合而非性能提升。proposal 缺少对这一 over-parameterization 风险的讨论。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   "Correctability 作为独立预测目标"这一概念确实新颖，但增量有限。技术层面几乎全部借用自近期工作：multi-layer ensembling 直接来自 arXiv:2604.13386，SAE feature decomposition 框架来自 arXiv:2604.19974，representational geometry 分析来自 arXiv:2602.08159。更关键的是，arXiv:2604.22271 已经在研究 "internal confidence signals predict which errors the model can correct"——与本 proposal 的核心 claim 高度重叠。剥离 surface differences 后，本 proposal 的核心新增量是 (a) 将 correctability 形式化为独立预测目标，(b) 与 correctness 做 representational geometry 对比。(a) 是一个好的 framing 但不是 deep insight；(b) 是一个有意思的实验但结论可能是 "correctability 的表征结构与 correctness 类似"——这在审稿人看来属于 "I would have guessed this"。

2. **Significance: 中** — 
   "哪些错误值得修正、哪些应该 abstain"在实际部署中确实重要。如果 probe-gated correction 能可靠工作，对 test-time compute allocation 有实际价值。但问题的重要性被两个因素削弱：(a) CoRefine 等 output-level 方案已经在实用层面解决了类似问题（92.6% halting precision），hidden-state probe 的增量收益可能不足以 justify 额外的复杂性；(b) 随着 reasoning models 和 extended thinking 的快速发展，self-correction 本身的范式可能正在被超越——模型可能会通过更好的 initial reasoning 而非 post-hoc correction 来提升准确率。

3. **Related Work: 中** — 
   对 CoRefine、Error Depth Hypothesis、SAE dissociation、Wait token 机制等的引用是准确和相关的。但缺失了一些直接竞争的工作：arXiv:2604.22271 ("How LLMs Detect and Correct Their Own Errors") 研究的方向与本 proposal 高度重叠但未被引用；arXiv:2512.20578 ("Can LLMs Predict Their Own Failures?") 和 arXiv:2510.16062 (CorrectBench) 也是应该讨论的工作。与 CoRefine 的差异化定位虽然有尝试（hidden-state vs. output-level, genuine abstention），但论证深度不足——proposal 未能解释为什么 hidden-state probe 在 gating 任务上比 output-level confidence 更优的理论原因。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】: 
Novelty 是主要限制维度。核心概念（correctability as distinct target）有新颖性但增量有限——剥离借用的技术后，真正新的 insight 薄弱，且 arXiv:2604.22271 已在高度重叠的方向上工作。Significance 受限于 CoRefine 等 output-level 方案已提供了实用的替代方案。最关键的风险是 Trivial Alternative 威胁：correctness probe + uncertainty probe 的简单组合可能达到接近的 gating 效果，使得 correctability 作为独立信号的 value proposition 不成立。proposal 的"kitchen-sink"风格（堆叠多层 ensemble、multi-token features、attention entropy、SAE features、crosscoder analysis 等）反映了对核心 idea 深度的不自信，审稿人可能会批评 contribution 不够 focused。dual-outcome 保底策略（"even if probe AUROC plateaus"）虽然务实，但从 idea 评估角度看是一个负面信号——proposal 自身暗示了核心 result 可能为 negative。

【主要风险】: 
1. **Correctability 不是独立信号风险**：如果 correctability ≈ correctness + uncertainty 的组合，核心 contribution 瓦解，trivial baseline (correctness probe + uncertainty threshold) 即可 replicate 主要效果
2. **与 arXiv:2604.22271 的重叠风险**：该工作已研究 internal confidence signals 如何 predict which errors the model can correct，如果在 submission 前该工作被进一步发展或被顶会接收，本 proposal 的 novelty claim 将受到严重质疑
```

Sources:
- [The Confidence Manifold (arXiv:2602.08159)](https://arxiv.org/pdf/2602.08159)
- [SAE Functional Dissociation (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)
- [Multi-Layer Ensemble Probing (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)
- [CoRefine (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)
- [Error Depth Hypothesis (arXiv:2601.00828)](https://arxiv.org/abs/2601.00828)
- [Wait Token Mechanisms (arXiv:2510.04128)](https://arxiv.org/abs/2510.04128)
- [LLMs Encode Their Failures (arXiv:2602.09924)](https://arxiv.org/abs/2602.09924)
- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)
- [Can LLMs Predict Their Own Failures? (arXiv:2512.20578)](https://arxiv.org/abs/2512.20578)
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/html/2507.02778v1)
- [CorrectBench (arXiv:2510.16062)](https://arxiv.org/abs/2510.16062)
- [Reflective Confidence (arXiv:2512.18605)](https://arxiv.org/pdf/2512.18605)
- [PAG (arXiv:2506.10406)](https://arxiv.org/pdf/2506.10406)


【原始 proposal（允许参考但不是主要依据）】:
# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction

## Description
We investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1eb6d7ae-ab0b-4bcd-83f0-6c5fe8a2b8be",
  "type": "user",
  "uuid": "d3f6ff9f-cf7b-426e-9582-2a1cb5993820",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:31:08.643Z_

```json
{
  "parentUuid": "d3f6ff9f-cf7b-426e-9582-2a1cb5993820",
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
  "uuid": "11cd0cc1-cbca-461c-a17e-aaf2d6816bd3",
  "timestamp": "2026-05-20T03:31:08.643Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:31:08.643Z_

```json
{
  "parentUuid": "11cd0cc1-cbca-461c-a17e-aaf2d6816bd3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fb480903-5dec-4097-8ada-a7a573765bfb",
  "timestamp": "2026-05-20T03:31:08.643Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

````json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ 现在我已经完成了充分的领域调研，可以进行系统评估了。  ---  ``` 【阶段】: Triage  【领域调研】:  1.…",
  "leafUuid": "fb480903-5dec-4097-8ada-a7a573765bfb",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c"
}
````

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction for selective self-correction",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:31:49.606Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as the Meta Judge.

First, let me extract the key data:

**Reviewer 1**: [12% - 22%] 中位 17%
- Novelty: 弱
- Significance: 中
- Related Work: 强

**Reviewer 2**: [15% - 25%] 中位 20%
- Novelty: 弱


- Significance: 中
- Related Work: 强

**Reviewer 3**: [18% - 28%] 中位 22%
- Novelty: 弱-中
- Significance: 中
- Related Work: 中

The three midpoints cluster tightly around 17%, 20%, and 22% with a mean of 19.67% and median of 20%, showing strong consistency across reviewers. All three agree that novelty is weak, significance is moderate, and related work coverage is strong to moderate—with consensus emerging that this paper has limited novelty but adequate treatment of existing literature. The reviewers all flag that a trivial alternative—using a correctness probe with a simple threshold, or CoRefine's existing confidence-based routing—could achieve similar results, undermining the novelty. They're also skeptical about the core assumption that "correctability" is a detectable internal property independent of the model's actual behavior, especially given that 68% of the features appear causally inert. The related work section is mostly solid across reviewers, though all note the missing citation of arXiv:2604.22271, and R2 and R3 point out gaps around Gnosis.

Beyond the consensus issues, R1 raises a critical venue mismatch—this is an NLP interpretability paper being submitted to a robotics conference, which is a fundamental problem the other reviewers didn't catch. R3 adds that the approach feels like a "kitchen-sink" design lacking confidence in the core idea, and flags two additional risks: reasoning models with extended thinking might be making post-hoc correction obsolete, and adding more token positions could lead to overfitting given the low-dimensional correctness signals.

Now I'm realizing the venue issue is even more critical than I initially thought. R1 correctly identified that submitting to CoRL (Conference on Robot Learning) is a fatal mismatch for a paper entirely about LLM self-correction and internal representations. The 12-22% estimate R1 gave assumes submission to an appropriate venue like ACL or EMNLP, but the user explicitly specified CoRL 2026 as the target. This completely changes the evaluation—the paper isn't just weak for its venue, it's in the wrong venue entirely.

I should report this objectively: if the submission is genuinely going to CoRL, the acceptance probability would be near zero, not 12-22%. Let me also recalculate the standard deviation across the three estimates to properly quantify the uncertainty. The values are 17, 20, and 22 percent, which gives a standard deviation of about 2 percent, indicating relatively tight agreement among reviewers despite the venue mismatch issue.

Now I'm assessing the feasibility of the proposed work. The project involves running inference on multiple large language models, training lightweight probes, and analyzing sparse autoencoders across three standard datasets. While the datasets are publicly available, the computational requirements are substantial—particularly the inference runs across different model sizes. This is definitely implementable but would require meaningful compute resources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb480903-5dec-4097-8ada-a7a573765bfb",
  "isSidechain": false,
  "requestId": "req_011CbD7bJCXsAuQZkbU8GGzU",
  "type": "assistant",
  "uuid": "e2c93a9d-9d2d-463d-826d-ee544a31365a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyMjPECR8AKFgwa4RkJmXP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14567,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3773,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3773,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14567
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

_source line 9 · 2026-05-20T03:32:36.957Z_

【阶段】: Meta Judge
【三次中位】: [17%, 20%, 22%]  std=2.05%
【共识维度】:
- **Novelty = 弱**（3/3）：核心 claim "内部表征预测 correctability" 已被 arXiv:2604.22271 部分建立；技术组件全部借用自 2025-2026 近期独立论文（multi-layer ensembling from 2604.13386, SAE from 2604.19974, geometry from 2602.08159）；概念与 Error Depth Hypothesis (2601.00828) 实质重叠
- **Significance = 中**（3/3）：问题本身有实际价值（selective self-correction 避免 overcorrection），但正面结果 "I would have guessed this"，负面结果贡献有限；CoRefine 92.6% halting precision 已提供实用替代方案
- **Trivial Alternative 威胁真实存在**（3/3）：correctness probe + 简单阈值 gating 是最直接的 trivial baseline；CoRefine 的 output-level confidence routing 是第二个；R3 额外提出 correctness + uncertainty probe 逻辑组合
- **核心前提假设脆弱**（3/3）："correctability 是模型内部独立编码的可检测属性"这一最关键假设无理论或实证支撑；68% pure incorrectness features causally inert 的已有发现反而暗示二阶属性信号可能更弱
- **arXiv:2604.22271 未被引用**（3/3）：三位审稿人均独立发现这一最直接竞争工作未被 proposal 引用，构成 Related Work 遗漏
【异常维度】:
- **Venue mismatch**（仅 R1）：R1 指出 proposal 内容为纯 NLP interpretability / self-correction，投稿 CoRL（Conference on Robot Learning）存在根本性领域不匹配。R2、R3 未提及 venue 问题，其概率估计隐含假设投稿 NLP/ML 适配 venue
- **"Kitchen-sink" 批评**（仅 R3）：R3 认为堆叠过多技术组件反映对核心 idea 深度的不自信
- **Paradigm shift 风险**（仅 R3）：reasoning models / extended thinking 可能正在超越 post-hoc correction 范式
- **Over-parameterization 风险**（仅 R3）：correctness 信号仅需 3-8 维，添加更多 token positions 可能导致过拟合
【最终概率】: [13% - 24%] 中位 19%
【一致性】: 高
【综合理由】:

三位审稿人的评估高度收敛（std=2.05%，远低于 3% 阈值），在 Novelty、Significance、Trivial Alternative、核心前提假设等关键维度上形成了强共识。处理逻辑如下：

1. **共识处理**：Novelty=弱 是三方一致结论且论证充分——arXiv:2604.22271 对核心 claim 的先行覆盖、技术组件全部借用、概念与 Error Depth Hypothesis 重叠——这构成了概率天花板的刚性约束。Significance=中 同样三方一致。这两个维度共同将 idea 质量天花板锁定在约 25%。

2. **异常处理**：
   - **Venue mismatch（R1）**：虽然只有 R1 提出，但这是一个客观事实性判断（proposal 无任何 robotics 内容 → CoRL 不匹配），不应因为仅 1 人提到就降权。**如果确实投稿 CoRL，这是致命缺陷，概率趋近 0%。** 以下最终概率估计基于投稿适配 venue（ACL/EMNLP/NeurIPS/ICML）的假设。
   - **Kitchen-sink 批评（R3）**：虽只有 R3 明确使用此措辞，但 R1 和 R2 对"已有技术组合应用"的描述实质上传达了类似信号，因此适度采纳。
   - **Paradigm shift 风险（R3）**：有一定道理但属于长期趋势判断，对 submission cycle 内的评审影响有限，降权处理。

3. **收敛后校准**：高一致性情况下取中位附近。三份中位分别为 17%/20%/22%，中位的中位为 20%。考虑到共识中的严重负面信号（trivial alternative 威胁 + 核心前提脆弱 + 最直接竞争者未引用），在中位基础上小幅下调至 19%。区间因高一致性略微收窄至 [13%-24%]。

4. **Related Work 特殊说明**：R1 和 R2 给出"强"，R3 给出"中"。分歧原因是 R3 对差异化论证深度有更高要求。综合判定为"中-强"——覆盖面好但有 1 个关键竞争者遗漏（2604.22271），且与 CoRefine 的差异化论证缺乏理论深度。

**⚠️ 致命 venue 问题**：若确实投稿 CoRL 2026，概率估计应修正为 **[0% - 3%] 中位 1%**——proposal 不含任何 robotics / embodied AI / robot learning 内容，desk reject 风险极高。上述 [13%-24%] 中位 19% 仅适用于 NLP/ML 适配 venue。

【建议】: 不推荐（如投 CoRL 则 KILL）
【实施评估】:
  - 计算资源: 中等。需要在 3 个模型（Gemma-3-27B, Qwen-2.5-7B, Mistral-Small-3.2-24B）上提取 hidden states 并训练 linear probes。推理提取阶段需要约 2-4 张 A100 GPU（27B 模型需要多卡），probe 训练本身计算量很小。SAE 分析和 crosscoder 分析需要额外计算但量级可控。总体 GPU 时约 500-1000 A100-hours。
  - 数据需求: 低。TriviaQA、MMLU、GSM8K 均为公开数据集，可直接获取。需要自行构建 correctability 标注（对每个错误答案运行 self-correction 并标记成功/失败），这增加推理成本但不需要外部数据采购。
  - 人工介入: 低-中。correctability 标注基本可自动化（模型跑 self-correction → 自动比对正确答案）。少量 case study / error analysis 可能需要人工审查。
  - 训练需求: 轻量。仅训练 linear probes 和 ensemble stacking（非大模型训练），训练时间可忽略（分钟级）。不涉及大模型微调。
  - 新 Benchmark: 不需要构建全新 benchmark。需要在现有 benchmark 上生成 correctability 标注数据，这是数据处理而非 benchmark 构建。
  - 预估周期: 2-3 个月。Phase 0 pilot（multi-layer ensembling 迁移测试）约 2-3 周；主实验（probe 训练 + gating 评估 + 几何分析 + SAE 分析）约 4-6 周；写作约 3-4 周。假设资源到位，从启动到可投稿约 10-12 周。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2c93a9d-9d2d-463d-826d-ee544a31365a",
  "isSidechain": false,
  "requestId": "req_011CbD7bJCXsAuQZkbU8GGzU",
  "type": "assistant",
  "uuid": "32688c0d-3275-41dd-99a5-fa3a29b10e18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyMjPECR8AKFgwa4RkJmXP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14567,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3773,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3773,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14567
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

````json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ 现在我已经完成了充分的领域调研，可以进行系统评估了。  ---  ``` 【阶段】: Triage  【领域调研】:  1.…",
  "leafUuid": "32688c0d-3275-41dd-99a5-fa3a29b10e18",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c"
}
````

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction for selective self-correction",
  "sessionId": "fa1834d3-1275-4512-9fde-4129d908f30c"
}
```

---
