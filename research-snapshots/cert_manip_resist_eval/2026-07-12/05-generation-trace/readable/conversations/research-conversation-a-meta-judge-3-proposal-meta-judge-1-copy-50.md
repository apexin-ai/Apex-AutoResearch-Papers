# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/95dfc2f8-6a20-467b-b476-7547688888e8.jsonl`
- **Structured JSON:** [`aad72e99f9b050fb56fc.json`](../../sessions/aa/aad72e99f9b050fb56fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:03:51.356Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:03:51.356Z",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a well-informed evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [Align Once, Benefit Multilingually (MLC loss)] (ICLR 2026, arXiv:2602.16660):\n   最直接的前驱工作。使用 SVD 分解多语言安全表示矩阵，通过 σ_1 dominance 的 collinearity loss 对齐单一 safety refusal direction。本 proposal 的核心数学框架（SVD → σ_1 dominance → 可微 loss）直接源自此工作，扩展方向是从\"1个safety concept\"到\"K个factual knowledge\"。\n\n2. [DCO: Optimizing Language Models for Crosslingual Knowledge Consistency] (arXiv 2603.04678, 投稿 ICML 2026):\n   DPO-inspired 的 behavioral-level 跨语言一致性优化，不需要 gold labels，在 9 个模型上取得 +2.7 到 +13.8 RankC。与本 proposal 互补但也构成竞争——DCO 的 behavioral gains 显著高于本 proposal 预期的 +2-4%。\n\n3. [DALI: Can you map it to English?] (EACL 2026, arXiv:2504.09378):\n   通过 activation patching 在 Llama 3.1 8B 上提供因果证据：中间层对齐质量因果决定跨语言性能。为本 proposal 的中间层干预点提供了理论支撑，但 DALI 本身已提供 instance-level alignment metric，与 C_k 在分析层面存在功能重叠。\n\n4. [Paths Not Taken] (EMNLP 2025, arXiv:2505.20546):\n   识别 Llama-3.2-3B 中的 English-centric factual recall pipeline，两个 vector intervention 产生 +19.04pp 平均改善。推理时干预，behavioral impact 远超本 proposal 的训练时方法预期效果。\n\n5. [AlignX] (EMNLP 2025, arXiv:2509.24338):\n   两阶段 representation-level 框架，在 layer 16 用对比学习对齐多语言表示。无 per-fact metric，但已覆盖 representation alignment 的训练范式。\n\n6. [SubInj: On the Entity-Level Alignment in Crosslingual Consistency] (arXiv 2025, arXiv:2510.10280):\n   12个模型、17种语言上的 entity-level 对齐分析，training-free SubInj 取得 +4.1-31.6% recall。训练不需要的推理时方法，效果显著。\n\n7. [CLM-Bench] (arXiv 2026, arXiv:2601.17397):\n   揭示 MEMIT 编辑向量跨语言近似正交（30.93% cross-lingual transfer）。为本 proposal 的几何分析提供了直接 motivation。\n\n8. [Why Better Cross-Lingual Alignment Fails] (arXiv 2026, arXiv:2603.18863):\n   反面证据——在 XLM-R encoder 上，alignment 和 downstream task 目标是正交的。虽然限于 encoder + 结构任务，但对\"几何对齐→行为改善\"的因果链提出质疑。\n\n9. [The Geometry of Multilingual Language Model Representations] (EMNLP 2022, arXiv:2205.10964):\n   较早的工作已使用 SVD 分析多语言表示空间的几何结构，识别 language subspaces。表明 SVD 分析多语言表示并非全新方法论。\n\n10. [A Joint Matrix Factorization Analysis of Multilingual Representations] (2023, arXiv:2310.15513):\n    使用 PARAFAC2 矩阵分解同时分析多语言表示，与本 proposal 的矩阵分解分析路线存在方法论重叠。\n\n- 调研总结：跨语言知识一致性是 2025-2026 年 NLP 的活跃研究方向，现有方法沿 behavioral (DCO)、representation (AlignX)、entity-level (SubInj)、inference-time intervention (Paths Not Taken) 四条路线推进。MLC (ICLR 2026) 已经在 safety 领域建立了 SVD collinearity 的范式。本 proposal 试图将 MLC 的 SVD collinearity 方法从 safety (1个方向) 推广到 per-fact knowledge (K个方向)，核心增量在于 per-fact 诊断工具和 inter-fact orthogonality。\n\n\n【Trivial Alternative 检验】:\n\n存在多个更简单的替代方案：\n\n(1) **Per-fact 平均 pairwise cosine similarity**：对每个 fact 的 L 种语言表示计算平均 pairwise cosine，同样能得到一个连续的 per-fact 对齐度量。SVD 的 σ_1 dominance 在数学上等价于对 Gram 矩阵第一特征值占比的度量，与平均 cosine 高度相关。Proposal 确实将 per-fact cosine 作为 ablation baseline，但问题是：如果 cosine loss 的 behavioral 效果与 MFC 相当（这是很可能的结果），那 SVD 的额外复杂度是否值得？\n\n(2) **AlignX-style per-fact contrastive loss**：直接将 AlignX 的对比学习从 general alignment 适配到 per-fact level。这也是 proposal 的 ablation 之一。\n\n增量价值的核心辩护在于：SVD 提供的不只是一个标量（cosine 也能给），而是 (a) 主方向向量 u_1 用于可视化/机制分析，(b) 残差奇异值用于 per-language deviation 诊断，(c) 跨 fact 的 Gram 矩阵分析。但这些增量主要是 **分析工具层面的**——它们提供更丰富的诊断信息，但是否产生更好的训练效果是存疑的。如果 ablation 结果显示 MFC 和 cosine loss 的 behavioral 效果接近，那 SVD 框架的价值将主要局限于分析贡献，而分析贡献单独可能不够支撑一篇 top venue 论文。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的关键假设：\n\n(1) **\"per-fact collinearity improvement → behavioral improvement\"**：这是最关键的假设。DALI 提供了中间层对齐→NLU 性能的因果证据，但 DALI 测试的是 NLU 任务（Belebele, XStoryCloze, XCOPA），不是 factual recall。\"How Do Multilingual Models Remember?\" 明确指出 factual recall 有两个阶段：中间层的 language-independent subject enrichment + 后层的 language-dependent object extraction。MFC 只优化中间层 subject enrichment 的几何结构，但如果瓶颈主要在 late-layer object extraction（Paths Not Taken 的发现支持这一点——翻译向量在 layer 21 的干预产生最大效果），那中间层的几何改善可能只解决一半问题，behavioral gains 就会受限。这解释了 proposal 自承的 modest behavioral targets (+2-4%)。\n\n(2) **\"per-fact SVD decomposition 在训练中是稳定的\"**：虽然有 Robust Differentiable SVD (CVPR 2021) 的技术支撑，但 per-fact SVD 的计算/梯度在 mini-batch 训练中的实际表现（特别是当 L 种语言不全在同一 batch 中时）是未经验证的。这更偏 feasibility，但它影响 claim 的可验证性。\n\n(3) **\"inter-fact orthogonality 是有益的\"**：proposal 假设不同 fact 的主方向应该正交。但如果相关的 facts（如同一 relation type）自然地共享方向，强制正交可能反而有害。这个假设缺乏理论支撑。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** —— \n   核心创新是将 MLC (ICLR 2026) 的 SVD collinearity 方法从单一 safety concept 推广到 per-fact knowledge。数学框架（SVD → σ_1 dominance → softmax-style loss）直接复用 MLC。推广的方向是自然且可预测的——从\"1个方向\"到\"K个方向\"加 orthogonality regularization 是一个 standard extension。Per-fact 诊断工具（language deviation profiles）有分析新意，但 SVD 分析多语言表示在方法论上已有先例（EMNLP 2022 的 Geometry of Multilingual LM Representations；2023 的 Joint Matrix Factorization Analysis）。与 DALI 的分析功能存在部分重叠——DALI 已提供 instance-level alignment metric，虽然用的是 discriminative similarity 而非 directional decomposition，但解决的是类似的\"per-instance 诊断\"需求。如果 MLC 已在 ICLR 2026 发表，审稿人很可能会问\"这相对于 MLC 的 novelty 到底在哪\"——答案是 per-fact 粒度和 orthogonality，但这可能被视为 incremental。\n\n2. **Significance: 中** —— \n   跨语言知识一致性是一个重要且活跃的研究问题，有真实的应用价值。Proposal 定位的分析 gap（没有 per-fact 几何度量工具）是真实存在的。但问题在于：(a) 预期的 behavioral impact 是 modest 的（+2-4% Bi-ZsRE），proposal 自己承认 DCO、SubInj、Paths Not Taken 的 behavioral gains 都更大；(b) 分析工具的价值取决于它能否产生 actionable insights——如果发现 \"cross-script facts have lower C_k\" 这类结论，审稿人可能会说 \"I would have guessed this\"（Beneath the Surface 已经展示了 script similarity 主导 representation sharing）；(c) editability 改善（CLM-Bench +8-15pt from 30.93%）如果实现会有意义，但这在 Extensions 中，不是 core。Proposal 的定位为 \"analysis + training method\"（类比 Beneath the Surface, DALI），但 Beneath the Surface 和 DALI 都揭示了 surprising findings，而本 proposal 的预期发现是否会 surprising 存疑。\n\n3. **Related Work: 强** —— \n   这是 proposal 最强的维度。相关工作覆盖极为全面，横跨 behavioral (DCO, CALM, CM-Align)、representation (AlignX, Middle-Layer RA)、entity-level (SubInj)、inference-time (Paths Not Taken)、mechanistic (DALI, How Do Multilingual Models Remember?, Lost in Multilinguality)、editing (X-KDE, CLM-Bench, LangEdit) 和 counter-evidence (arXiv:2603.18863, CLAS) 等多个维度。差异化定位清晰——proposal 准确地指出每个现有方法不提供 per-fact geometric characterization 这一 gap。对 counter-evidence 的处理也很诚实（承认 arXiv:2603.18863 的 alignment-task orthogonality 发现，给出合理但非铁证的辩护）。所有被引论文经搜索确认真实存在且描述基本准确。\n\n\n【概率估计】: [20% - 32%] 中位 25%\n\n【估计理由】: \n三维度综合推理：Related Work 强——不会因 related work 覆盖不足被拒，但 related work 好只防守下限不提升上限。Novelty 中偏弱是主要瓶颈——MLC→MFC 的推广路径过于自然，审稿人大概率会指出 \"this is a straightforward extension of MLC (ICLR 2026) to per-fact setting\"，而这正是区分 25% 和 35%+ 的关键：核心发现如果 positive（C_k 能刻画 per-fact 对齐、MFC loss 有效），审稿人的反应更可能是 \"makes sense, but I would have expected this to work\" 而不是 \"surprising\"。Significance 中——问题重要但预期 behavioral impact modest，分析贡献需要通过 surprising findings 来提升价值，而目前看不到哪个预期发现会是 surprising 的。上界被 Novelty 限制在 ~32%；下界被 Related Work 的全面性和分析 gap 的真实性托住在 ~20%。\n\n【主要风险】:\n1. **\"Incremental over MLC\" 风险**：最可能的拒稿理由。MLC (ICLR 2026) 已建立 SVD collinearity 的范式，本 proposal 的 per-fact 推广可能被视为 engineering extension 而非 conceptual contribution。如果 8-config ablation 中 per-fact cosine loss 效果与 MFC 接近，该风险将被放大为致命。\n2. **Analysis-only 价值不足风险**：如果 behavioral gains modest（如 proposal 自预期的 +2-4%），论文价值将主要依赖分析贡献。但分析贡献要求产出 surprising 的 findings（如发现某类 fact 意外地已经 well-aligned，或 orthogonality regularization 意外有害），而不仅仅是确认已有假说（如 \"cross-script facts have lower C_k\"）。如果分析结论都在预期之内，审稿人可能认为 per-fact SVD 只是一个 expensive way to confirm what we already know。\n```\n\nSources:\n- [Align Once, Benefit Multilingually (MLC loss) - ICLR 2026](https://arxiv.org/abs/2602.16660)\n- [DCO: Optimizing Language Models for Crosslingual Knowledge Consistency](https://arxiv.org/abs/2603.04678)\n- [DALI: Can you map it to English? - EACL 2026](https://arxiv.org/abs/2504.09378)\n- [Paths Not Taken - EMNLP 2025](https://arxiv.org/abs/2505.20546)\n- [AlignX - EMNLP 2025](https://arxiv.org/abs/2509.24338)\n- [SubInj: On the Entity-Level Alignment in Crosslingual Consistency](https://arxiv.org/abs/2510.10280)\n- [CLM-Bench](https://arxiv.org/abs/2601.17397)\n- [Why Better Cross-Lingual Alignment Fails](https://arxiv.org/abs/2603.18863)\n- [The Geometry of Multilingual Language Model Representations](https://arxiv.org/abs/2205.10964)\n- [A Joint Matrix Factorization Analysis of Multilingual Representations](https://arxiv.org/abs/2310.15513)\n- [Beneath the Surface of Consistency - NAACL 2025](https://arxiv.org/abs/2408.10646)\n- [X-KDE: Edit Once, Update Everywhere - ACL 2025](https://arxiv.org/abs/2502.14645)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough information to produce a thorough assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n```\n\n## ⚠️ 致命性前置问题：会议选择\n\n**在评估 idea 质量之前，必须先指出一个致命问题：CoRL (Conference on Robot Learning) 是机器人学习会议。** 根据 CoRL 2026 官方 Call for Papers：\"Submissions without a robotics focus will be returned without review.\" 该 proposal 关于跨语言知识表征的 SVD 几何分析，属于纯 NLP/多语言 LLM 研究，与机器人学习完全无关。**投稿 CoRL 会被直接 desk reject，中稿概率为 0%。**\n\n该 proposal 的合适会议应为 ACL、EMNLP、NAACL、ICLR、NeurIPS 等 NLP/ML 主会。以下评估基于假设投稿至合适的 NLP 主会（如 ACL/EMNLP 2026）来给出 idea 质量判断。\n\n---\n\n```\n【领域调研】:\n```\n\n**1. MLC Loss (ICLR 2026, arXiv:2602.16660)**：该 proposal 最直接的\"前驱\"工作。MLC loss 使用 SVD 分解多语言表征矩阵的共线性来对齐安全方向（单一 refusal direction），将 Swahili 安全得分从 6.11% 提升至 92.78%。**关键区别**：MLC 针对单一安全方向，本 proposal 将其扩展到 per-fact 级别的数千个知识方向。这是核心 novelty claim 的基础，但也是最需要审视的——从\"一个方向\"到\"数千个方向\"的扩展是否面临根本性困难。\n\n**2. DCO (ICML 2026, arXiv:2603.04678)**：DPO-inspired 的跨语言一致性优化，无需 gold label，在 9 个模型上获得 +2.7 到 +13.8 RankC。行为级别方法，不涉及表征几何分析。\n\n**3. AlignX (EMNLP 2025, arXiv:2509.24338)**：Layer 16 的对比学习对齐多语言表征。通用语义对齐，不提供 per-fact 指标。是本 proposal 最直接的表征级别竞争者。\n\n**4. SubInj (arXiv 2025, arXiv:2510.10280)**：12 个 decoder 模型上，通过注入英语 subject 翻译实现 +4.1-31.6% recall，训练免费、推理时干预。极其简单的方法获得了很大的效果提升。\n\n**5. Paths Not Taken (EMNLP 2025, arXiv:2505.20546)**：识别了 Llama-3.2-3B 中英语中心的事实检索流水线，两个向量干预获得 +19.04pp 平均提升，最低性能语言 +35%。推理时干预，效果显著。\n\n**6. DALI (EACL 2026, arXiv:2504.09378)**：Activation patching 因果证据证明中层对齐质量因果性地决定跨语言性能。24 种语言，3 个 NLU 任务。为中层干预提供了因果支持。\n\n**7. CLM-Bench (arXiv 2026, arXiv:2601.17397)**：中英文化知识编辑基准，发现编辑向量跨语言近乎正交，MEMIT 跨语言迁移率仅 30.93%。\n\n**8. Why Better Cross-Lingual Alignment Fails (arXiv 2026, arXiv:2603.18863)**：在 XLM-R 编码器上发现对齐和下游任务目标基本正交（cosine -0.10 to +0.18），显式对齐经常无法改善下游性能。**这是本 proposal 的潜在反面证据**——虽然作者限定于编码器和结构任务，但此发现对\"改善几何对齐→改善行为\"这一逻辑链构成质疑。\n\n**9. CLAS (arXiv 2026, arXiv:2601.16390)**：发现有效迁移通过功能分化（cluster separation）而非严格对齐实现。与本 proposal 强制对齐的方向存在张力。\n\n**10. Beneath the Surface of Consistency (NAACL 2025, arXiv:2408.10646)**：脚本相似性主导表征共享（同脚本 SR: 40-60%，跨脚本: 10-20%）。\n\n**调研总结**：跨语言知识一致性是 2024-2026 的活跃研究领域，已形成清晰的分层竞争格局——行为级（DCO/CALM）、表征级（AlignX）、实体级（SubInj）、推理时干预（Paths Not Taken）。MLC loss 已将 SVD 共线性用于安全对齐。**本 proposal 的核心定位是将 SVD 共线性从\"单方向安全对齐\"扩展到\"per-fact 知识对齐\"，同时提供分析框架。** 这是一个合理但增量的扩展，而非概念性突破。\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在显著的 trivial alternative 威胁。**\n\n1. **Per-fact 余弦相似度**：对于 L 种语言中每个 fact 的表征向量，计算所有语言对的 pairwise cosine similarity 的均值/方差，即可得到一个 per-fact 对齐质量指标。这比 SVD 计算量更低，解释性也不差。Proposal 自身将其列为 ablation baseline，这说明作者也意识到了这个威胁。\n\n2. **Per-fact CKA**：同样可以衡量跨语言表征的相似性，无需 SVD 分解。\n\n3. **Per-fact contrastive loss（AlignX 风格）**：直接在 per-fact 级别应用 AlignX 的对比学习，计算成本更低，不需要 SVD 的梯度反传（robust SVD backward 本身是一个工程挑战）。\n\n**增量价值在哪？** 本 proposal 的 SVD 框架相对于 trivial alternatives 的真正增量在于：(a) C_k 是一个单一标量指标，而 pairwise cosine 产生 L(L-1)/2 个值需要聚合；(b) u_1 提供一个可解释的\"共识方向\"；(c) 残差奇异值给出语言偏差 profile。但这些增量主要是**分析便利性**而非**本质能力差异**。如果 8-config ablation 发现 cosine loss 在行为指标上与 MFC 无显著差异，整个工作的价值将大幅缩水。\n\n---\n\n```\n【前提假设检验】:\n```\n\n核心 claim 的逻辑链存在多个未经验证的假设：\n\n1. **「每个 fact 应该有一个 dominant direction」假设**（最关键）：MLC loss 对安全对齐有效，是因为 refusal 本质上是单一方向的（pairwise agreement 0.97）。但事实性知识（如 \"巴黎是法国的首都\"）是否也在表征空间中形成单一主方向？这是一个**强假设**。每个 fact 可能需要多维表征（subject、relation、object 分别编码），不同语言可能共享 subject 编码但 object 编码不同（正如 \"How Do Multilingual Models Remember?\" 所揭示的两阶段机制）。如果 fact 表征本质上不是一维共线的，强制 C_k → 1.0 可能是有害的。\n\n2. **「几何对齐改善 → 行为改善」假设**：arXiv:2603.18863 明确发现在编码器上对齐与下游任务目标正交。虽然 DALI 提供了中层对齐的因果证据，但 DALI 测量的是 discriminative similarity（实例级别的匹配/不匹配区分能力），与 SVD 共线性是不同的数学量。**DALI 的因果证据不能直接迁移为 SVD 共线性的因果证据。**\n\n3. **「中层是正确的干预点」假设**：多项工作（Lost in Multilinguality, DALI, Paths Not Taken）汇聚支持中层的重要性，但 \"How Do Multilingual Models Remember?\" 明确指出 object extraction 发生在后期层且是语言相关的。MFC 只在中层施加约束，可能无法解决后期层的瓶颈。作者也承认这一点，但将其视为\"互补\"——然而如果主要瓶颈在后期层（如 SubInj 和 Paths Not Taken 的结果所暗示），中层几何改善的行为收益可能确实很小（作者自己的目标也只是 +2-4%）。\n\n4. **「inter-fact 正交性是可维持的」假设**：当 K 个 fact 的数量增长到数千级别时，d 维空间中 K 个方向不可能全部正交（K >> d 时）。正交性正则化在大规模下可能导致数值问题或与共线性目标冲突。\n\n---\n\n```\n【3 维度打分】:\n```\n\n**1. Novelty: 中偏弱 — 理由：**\n\n- 核心数学工具（SVD 分解多语言表征矩阵 → sigma_1 dominance ratio → differentiable loss）已在 MLC loss (ICLR 2026) 中被提出和验证，只不过用于安全对齐（单方向）。本 proposal 将其扩展到 per-fact 级别。这是一个**domain transfer + granularity extension**，而非全新方法论。\n- Per-fact 分析的\"框架\"（C_k 指标、u_1 方向、偏差 profile）在数学上是 SVD 的标准输出，包装为\"分析框架\"有一定贡献，但核心操作是直接的。\n- 与 AlignX 的区别主要在粒度（per-fact vs. general representation）和工具（SVD vs. contrastive），但如果 per-fact contrastive 效果相当，SVD 的 novelty 就被稀释。\n- **加分点**：将分析框架与训练目标统一（\"measure what you optimize\"）这一设计理念确实比纯分析或纯训练更完整。\n- **综合**：有增量 novelty，但不构成\"surprising\"级别的贡献。审稿人可能评价为\"straightforward extension of MLC to per-fact level\"。\n\n**2. Significance: 中 — 理由：**\n\n- 研究问题本身（跨语言知识的 per-fact 几何编码）是一个真实且有趣的问题。理解 LLM 如何在表征空间中编码跨语言事实，对多语言 AI 的可靠性有实际意义。\n- 然而，**实际影响力受限于行为收益的天花板**。作者自身的目标只有 +2-4% Bi-ZsRE，而 SubInj（训练免费）已达 +4.1-31.6%，DCO 达 +2.7-13.8 RankC，Paths Not Taken 达 +19.04pp。一个需要训练的方法如果行为收益低于推理时免费干预，其实际价值存疑。\n- 分析框架的 significance 取决于它是否能揭示**非平凡的发现**（如特定 fact 类型或脚本组合的几何特征）。如果分析结论只是\"跨脚本 C_k < 同脚本 C_k\"（已被 Beneath the Surface 预测），则分析贡献也不够 surprising。\n- **作为 editability 改善路径的潜力**（CLM-Bench 30.93% → target 39-46%）是一个有趣的应用场景，但效果存疑。\n\n**3. Related Work: 强 — 理由：**\n\n- 这是本 proposal 最突出的优点。Related work 覆盖极为全面，跨越行为级（DCO/CALM/CM-Align）、表征级（AlignX/Middle-Layer）、实体级（SubInj）、推理时干预（Paths Not Taken）、因果分析（DALI）、知识编辑（X-KDE/CLM-Bench/LangEdit）、机制分析（How Do MLMs Remember/Lost in Multilinguality）等所有相关维度。\n- 差异化定位清晰：proposal 明确说明了与每个竞争者在哪个维度上不同（行为 vs. 几何、通用 vs. per-fact、推理时 vs. 训练时）。\n- 关键引用经调研验证均真实存在且描述基本准确（MLC, DCO, AlignX, SubInj, DALI, Paths Not Taken, CLM-Bench 等）。\n- 反面证据也被包含（arXiv:2603.18863, CLAS 的 cluster separation），说明作者对领域有深入理解。\n- **唯一不足**：部分论文的会议归属需要核实（如 DCO 标注为 ICML 2026，但当前仅为 arXiv preprint，ICML 2026 录用结果可能尚未公布）。\n\n---\n\n```\n【概率估计】: [18% - 28%] 中位 22%\n```\n\n```\n【估计理由】:\n```\n\n**从 3 维度到概率的推理：**\n\n- **Novelty（中偏弱）限制了上界。** 核心方法是 MLC loss 的 per-fact 扩展，数学工具（SVD）是标准的，审稿人很可能会写 \"This is a straightforward extension of [MLC, ICLR 2026] from safety to factual knowledge. The per-fact SVD analysis, while useful, is the standard output of SVD applied to a different matrix.\" 这使得上界被限制在 ~30% 以下。\n- **Significance（中）提供了一定支撑但不够强。** 研究问题合理，但行为收益目标（+2-4%）远低于竞争方法，且作者采用了防守性定位（\"分析为主，行为为辅\"）。审稿人可能会质疑：如果行为收益不显著，为什么要用 550 A100-hours 训练模型而不是直接做纯分析？\n- **Related Work（强）提供了下界保障。** 优秀的文献覆盖和差异化定位至少说明作者对领域有深入理解，论文的学术严谨性有保障，不太可能因为\"忽略了关键相关工作\"被拒。\n\n**概率区间解释：**\n- 下界 18%：如果 ablation 发现 cosine/contrastive loss 与 MFC 无显著差异，且分析未产生 surprising 发现，审稿人将给出 \"limited novelty, incremental contribution\"。\n- 上界 28%：如果 per-fact 分析揭示了非平凡的几何现象（如特定 fact 类别的几何特征与行为强相关），且 MFC 在 editability 上展现出独特价值，可能获得部分审稿人的认可。\n- 中位 22%：最可能的情况是 novelty 被认为增量但 related work 和实验严谨性得到认可，在 borderline 区域被一位审稿人支持、一到两位审稿人质疑 novelty 和 significance。\n\n```\n【主要风险】:\n```\n\n1. **\"MLC 的直接扩展\"批评**：最大的 idea 层面风险。MLC (ICLR 2026) 已经建立了 SVD 共线性 + differentiable loss 的完整方法论框架，本 proposal 在方法论上的唯一区别是\"从一个方向扩展到多个方向 + 加了正交性正则\"。审稿人极可能将此视为 incremental extension 而非独立贡献。如果作者无法论证 per-fact 扩展引入了 MLC 未面对的根本性新挑战（如大规模正交性维护、fact 表征的多维性），这一批评将难以反驳。\n\n2. **Trivial alternative 的行为等效性**：如果 8-config ablation 显示 per-fact cosine similarity loss 在行为指标上与 MFC loss 无统计显著差异，则 SVD 框架的训练价值被直接否定。虽然分析框架仍有价值，但一篇\"分析框架 + 训练 loss，其中训练 loss 不优于 cosine baseline\"的论文很难说服审稿人给 accept。\n\n---\n\nSources:\n- [Align Once, Benefit Multilingually (MLC Loss, ICLR 2026)](https://arxiv.org/abs/2602.16660)\n- [DCO: Optimizing Language Models for Crosslingual Knowledge Consistency](https://arxiv.org/abs/2603.04678)\n- [AlignX: Advancing Multilingual LLMs with Multilingual Representation Alignment (EMNLP 2025)](https://arxiv.org/abs/2509.24338)\n- [On the Entity-Level Alignment in Crosslingual Consistency (SubInj)](https://arxiv.org/abs/2510.10280)\n- [Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline (EMNLP 2025)](https://arxiv.org/abs/2505.20546)\n- [Can you map it to English? (DALI, EACL 2026)](https://arxiv.org/abs/2504.09378)\n- [CLM-Bench: Benchmarking Cross-lingual Misalignment in Knowledge Editing](https://arxiv.org/abs/2601.17397)\n- [Why Better Cross-Lingual Alignment Fails for Better Cross-Lingual Transfer](https://arxiv.org/abs/2603.18863)\n- [Cross-Lingual Activation Steering (CLAS)](https://arxiv.org/abs/2601.16390)\n- [Beneath the Surface of Consistency (NAACL 2025)](https://arxiv.org/abs/2408.10646)\n- [X-KDE: Edit Once, Update Everywhere (ACL 2025)](https://arxiv.org/abs/2502.14645)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to complete the assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n```\n\n## ⚠️ 致命前置问题：会议-论文主题完全不匹配\n\n在进入 idea 质量评估之前，必须首先指出一个 **致命的投稿问题**：\n\n**CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求**：\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\" 以及 \"**Submissions without a robotics focus will be returned without review.**\"\n\n本 proposal 完全是关于多语言 LLM 中跨语言知识表征的几何分析与训练目标，**与机器人学没有任何关系**。在 CoRL 投稿 = **desk reject**，概率趋近 0%。\n\n本 proposal 适合的会议是 **ACL、EMNLP、NAACL、COLM** 等 NLP/CL 主会，或 **ICLR、NeurIPS、ICML** 等 ML 主会。以下评估基于将本 proposal 投稿至 NLP/CL 顶会（如 ACL/EMNLP）的假设进行。\n\n---\n\n```\n【领域调研】:\n```\n\n- **MLC loss — \"Align Once, Benefit Multilingually\"** ([arXiv:2602.16660](https://arxiv.org/abs/2602.16660), ICLR 2026): 本 proposal 最直接的前驱工作。对**单一安全拒绝方向**使用 SVD collinearity loss，实现跨语言安全对齐 (DPO+MLC: avg safety 0.50→0.94，Swahili 6.11%→92.78%)。本 proposal 的核心就是将此思路从\"单一安全方向\"扩展到\"K 个事实方向\"。\n\n- **DCO — \"Optimizing Language Models for Crosslingual Knowledge Consistency\"** ([arXiv:2603.04678](https://arxiv.org/abs/2603.04678), ICML 2026 under review): DPO-inspired 的 behavioral-level consistency 方法，无需 gold labels，+2.7-13.8 RankC across 9 models。在 response ranking 层面操作，不涉及 representation geometry。\n\n- **AlignX** ([arXiv:2509.24338](https://arxiv.org/abs/2509.24338), EMNLP 2025): Layer 16 contrastive learning 做通用多语言表征对齐。不提供 per-fact metric，目标是一般语义对齐而非事实方向性结构。\n\n- **DALI — \"Can you map it to English?\"** ([arXiv:2504.09378](https://arxiv.org/abs/2504.09378), **COLM 2025，非 proposal 中标注的 EACL 2026**): 提出 instance-level DALI 指标，activation patching 证明 middle-layer alignment 因果地决定跨语言正确性。但针对 NLU 任务（Belebele, XStoryCloze, XCOPA），非 factual knowledge。\n\n- **SubInj — \"On the Entity-Level Alignment\"** ([arXiv:2510.10280](https://arxiv.org/abs/2510.10280), arXiv 2025): 证明 >99% 跨语言一致的事实需要实体对齐成功；SubInj 通过注入英语主语翻译实现 +4.1-31.6% recall。training-free，inference-time fix。\n\n- **\"Paths Not Taken\"** ([arXiv:2505.20546](https://arxiv.org/abs/2505.20546), [EMNLP 2025](https://aclanthology.org/2025.emnlp-main.762/)): 揭示 English-centric pipeline（middle layers 做英语主导的事实检索，late layers 做翻译）。两个 vector interventions 实现 +19.04pp 平均 recall。\n\n- **CLM-Bench** ([arXiv:2601.17397](https://arxiv.org/abs/2601.17397), arXiv 2026): 中英文 knowledge editing benchmark，MEMIT 跨语言 transfer 仅 30.93%，编辑向量跨语言近乎正交。\n\n- **\"How Do Multilingual Models Remember?\"** ([arXiv:2410.14387](https://arxiv.org/abs/2410.14387), ACL 2025 Findings): subject enrichment 在 middle layers 是 language-independent，object extraction 在 late layers 是 language-dependent。\n\n- **\"Beneath the Surface of Consistency\"** ([arXiv:2408.10646](https://arxiv.org/abs/2408.10646), NAACL 2025): script similarity 主导表征共享 (same-script SR: 40-60%, cross-script: 10-20%)。\n\n- **\"Layerwise Recall and the Geometry of Interwoven Knowledge in LLMs\"** ([arXiv:2502.10871](https://arxiv.org/abs/2502.10871), 2025): 研究 LLM 中 multi-associated attributes 的 layerwise geometry，发现 intermediate layers 通过 overlapping spaces 编码知识，包含 3D spiral 结构等分析。是 representation geometry 分析方向的近期工作。\n\n- **\"Geometric Deviation as an Unsupervised Pre-Generation Reliability Signal\"** ([arXiv:2605.03196](https://arxiv.org/abs/2605.03196), May 2026): 使用 hidden state 的 geometric deviation 做 pre-generation reliability 判断。表明 representation geometry 分析正在成为活跃方向。\n\n- **调研总结**: 跨语言一致性是 2024-2026 的活跃领域，已有 behavioral-level (DCO)、entity-level (SubInj)、inference-time (Paths Not Taken)、general representation-level (AlignX) 的解决方案。MLC loss (ICLR 2026) 开创了 SVD collinearity 用于多语言对齐的先河，但仅用于单一安全方向。**Per-fact SVD analysis of knowledge representations 确实是一个未被填补的 gap**，但该 gap 在概念上是 MLC loss 向 knowledge domain 的自然扩展。\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在明确的 trivial alternative 威胁。**\n\n1. **Per-fact 平均 pairwise cosine similarity**：对每个 fact 的 L 个语言表征计算两两 cosine similarity 的均值，即可获得一个 per-fact alignment 度量。这是 O(L²) 对 vs SVD 的 O(d·L²) 复杂度，更简单、更直观。Proposal 将此纳入了 ablation (Component 2 中 per-fact cosine baseline)，但 **核心问题是：如果 cosine-based metric 与 C_k 高度相关，且 cosine loss 能达到类似的 behavioral/geometric 效果，那整个 SVD framework 的增量价值就是有限的**。Proposal 声称 SVD 提供更丰富的信息（deviation profiles、dominant direction），但这些额外信息的实际价值是 empirical question，尚无先验理由认为它们一定比简单 cosine 好。\n\n2. **CKA (Centered Kernel Alignment)**：也被纳入 ablation，同样是现成的、well-understood 的 representation similarity metric。\n\n3. **AlignX-style per-fact contrastive loss**：将 AlignX 的 contrastive learning 从通用对齐适配到 per-fact 级别，也是一个 straightforward baseline。\n\n**增量价值声明**：Proposal 的核心增量是 (a) C_k 提供的 continuous scalar metric 和 (b) u_1 dominant direction 的可解释性/可视化能力。但这些更多是 **engineering convenience**（更漂亮的度量、更好的可视化）而非 **fundamental capability difference**。如果 ablation 显示 cosine/CKA 在行为指标上与 MFC 相当，审稿人可能会质疑 SVD framework 的必要性。\n\n---\n\n```\n【前提假设检验】:\n```\n\n核心 claim 的逻辑链中有 **三个关键未验证假设**：\n\n1. **\"Middle-layer per-fact collinearity improvement → behavioral factual recall improvement\"（因果传导假设）**：Proposal 引用 DALI 的 causal evidence，但 DALI 证明的是 NLU 任务（Belebele 阅读理解等）上 middle-layer alignment → correctness 的因果关系，**不是 factual knowledge recall 上的因果关系**。\"How Do Multilingual Models Remember?\" 明确指出 object extraction 在 late layers 且 language-dependent——这意味着即使 middle-layer collinearity 完美，late-layer extraction 仍然可能是瓶颈。Proposal 承认了这一点但将其视为\"complementary\"而非\"limiting factor\"，这是一个乐观假设。\n\n2. **\"SVD dominance ratio C_k 是比 cosine similarity 更好的 per-fact alignment 度量\"（度量优越性假设）**：没有理论或实证理由支持 σ₁/Σσⱼ 一定比 avg pairwise cosine 更能捕捉 cross-lingual alignment quality。两者在高 collinearity 时都趋近 1，在低 collinearity 时都趋近某个下界。SVD 的额外信息（deviation profiles）是否能转化为 actionable insights 完全是 empirical 的。\n\n3. **\"Per-fact orthogonality regularization 是必要的\"（collapse 假设）**：假设没有 orthogonality loss，MFC 会导致 fact direction collapse（所有 u_1^(k) 指向同一方向）。但在 d >> K 的高维空间中（d ~ 4096, K ~ 数千），random directions 本身就近乎正交。这个 regularization 的必要性需要实证验证。\n\n---\n\n```\n【3 维度打分】:\n```\n\n**1. Novelty: 中（偏弱）**\n\n理由：\n- **本质是 MLC loss (ICLR 2026) 的领域迁移**：从安全对齐的单一方向扩展到知识表征的 K 个方向。数学工具完全相同（SVD decomposition + softmax over singular values），应用场景从 safety → knowledge 是自然扩展。\n- **Per-fact analysis framework 本身是 genuinely new gap**：基于调研，确实没有现有工作提供 per-fact 级别的跨语言对齐度量。这是真实的 novelty delta。\n- **但 novelty 的\"深度\"有限**：核心创新是\"将 SVD 应用到 per-fact representation matrix\"——这是一个 application-level 的创新，而非 method-level 的创新。SVD 是标准工具，per-fact stacking 是直接的数据组织方式，softmax-over-singular-values 的 loss 是 MLC 已有的。\n- 参考：MLC loss ([arXiv:2602.16660](https://arxiv.org/abs/2602.16660)) 已经做了 SVD collinearity；AlignX ([arXiv:2509.24338](https://arxiv.org/abs/2509.24338)) 已经做了 layer-specific representation alignment。本 proposal 的 novelty 是这两者的\"交叉点\"——在 AlignX 的 per-fact 粒度上使用 MLC 的 SVD 工具。\n\n**2. Significance: 中**\n\n理由：\n- **跨语言事实一致性是重要问题**：被 DCO、SubInj、Paths Not Taken 等大量近期工作证实。\n- **但 expected behavioral gains 诚实地标注为 modest (+2-4% Bi-ZsRE)**：这意味着即使一切如预期，对实际应用的 impact 有限。DCO (+2.7-13.8 RankC)、SubInj (+4.1-31.6% recall)、Paths Not Taken (+19.04pp) 都提供了更大的 behavioral gains。\n- **Analysis-first positioning 的风险**：如果 C_k 与 behavioral metrics 高度相关（expected），那分析框架是 \"nice to have\"；如果相关性弱（possible），那分析框架的价值就存疑。Proposal 的 dual-outcome 设计（\"If MFC produces higher C_k but similar behavioral gains, that STILL validates the analysis framework\"）是 reasonable 的学术态度，但审稿人可能认为 \"a metric that doesn't predict behavior is not very useful\"。\n- **Editability angle (CLM-Bench +8-15pt) 是潜在的 significance amplifier**：如果 MFC 预训练能显著提升 MEMIT 跨语言 transfer（从 30.93% baseline），这会是一个 compelling result。但这被放在 Extensions 而非 Core。\n\n**3. Related Work: 强**\n\n理由：\n- **覆盖极其全面**：30+ 篇 reference，涵盖 behavioral (DCO, CALM, CM-Align)、entity-level (SubInj)、inference-time (Paths Not Taken)、representation-level (AlignX, Middle-Layer Repr. Alignment)、mechanistic (DALI, \"How Do Multilingual Models Remember?\", Lost in Multilinguality)、editing (X-KDE, CLM-Bench, LangEdit) 等全部相关分支。\n- **差异化定位清晰**：明确说明每个竞争方法在 behavioral/entity/representation/geometric 层面的位置，以及本工作填补的 \"per-fact geometric characterization\" gap。\n- **有一个事实错误**：DALI 论文 \"Can you map it to English?\" 发表于 **COLM 2025**（根据我的调研），而非 proposal 中标注的 \"EACL 2026\"。这是一个需要修正的引用错误。\n- **Counter-evidence 的处理 fair but optimistic**：[arXiv:2603.18863](https://arxiv.org/abs/2603.18863) 关于 alignment-task orthogonality 的 counter-evidence 被正确引用，但 \"specific to encoders and structural tasks\" 的 dismiss 可能过于轻松。\n\n---\n\n```\n【概率估计】: [20% - 32%] 中位 25%\n```\n\n（注：此概率基于投稿至 **ACL/EMNLP 等 NLP 主会** 的假设。若投稿 CoRL 2026，概率为 ~0%，因为 desk reject。）\n\n```\n【估计理由】:\n```\n\n本 proposal 填补了一个 genuine gap（per-fact geometric characterization），有扎实的理论动机（MLC→knowledge 的迁移、DALI/Paths Not Taken 的 causal evidence），related work 覆盖在本次调研中确认为极其全面。这些让它避免了 15% 以下的\"方向不成立\"区间。\n\n然而，**Novelty 维度限制了上界**：核心创新本质是 MLC loss (ICLR 2026) 的领域扩展 + per-fact stacking，数学工具无新意。如果 ICLR 2026 已经发表了 SVD collinearity for multilingual alignment，那审稿人自然会问 \"what's fundamentally new beyond applying MLC to knowledge?\"。同时，**Trivial Alternative 威胁真实存在**——per-fact cosine similarity 可能在 ablation 中表现相当，从而削弱 SVD framework 的必要性。\n\n此外，proposal 诚实承认 behavioral gains modest (+2-4%)，将 primary contribution 定位为 analytical。Analysis papers 在 NLP 主会可以发表（参考 \"Beneath the Surface\"、DALI），但需要 analysis 本身揭示 **surprising findings**。\"有些 fact 比其他 fact 更好地跨语言对齐\"、\"same-script 比 cross-script 更对齐\" 这些预期发现不太可能让审稿人感到 surprising。\n\n```\n【主要风险】:\n```\n\n1. **\"MLC-for-knowledge\" 被视为 incremental extension**：审稿人可能认为 MLC loss (ICLR 2026) 已经解决了 SVD collinearity 的核心方法论问题，本 proposal 仅是换了 application domain。如果 ICLR reviewer 已经在 MLC 的 related work 中讨论过 \"potential extension to factual knowledge\"，本 proposal 的 novelty 会进一步打折。\n\n2. **Cosine ablation 的 outcome risk**：如果 per-fact cosine similarity loss 在 behavioral + geometric 两个维度上都与 MFC loss 表现相当，那整个 SVD framework 的价值叙事将崩塌。Proposal 的 dual-outcome framing（\"C_k higher even if behavioral similar → still validates\"）是审稿人可能不买账的防守性论述。\n\n---\n\nSources:\n- [MLC Loss - Align Once, Benefit Multilingually (ICLR 2026)](https://arxiv.org/abs/2602.16660)\n- [DCO - Optimizing Language Models for Crosslingual Knowledge Consistency](https://arxiv.org/abs/2603.04678)\n- [AlignX - EMNLP 2025](https://arxiv.org/abs/2509.24338)\n- [DALI - Can you map it to English? (COLM 2025)](https://arxiv.org/abs/2504.09378)\n- [SubInj - Entity-Level Alignment](https://arxiv.org/abs/2510.10280)\n- [Paths Not Taken (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.762/)\n- [CLM-Bench](https://arxiv.org/abs/2601.17397)\n- [How Do Multilingual Models Remember? (ACL 2025 Findings)](https://arxiv.org/abs/2410.14387)\n- [Beneath the Surface of Consistency (NAACL 2025)](https://arxiv.org/abs/2408.10646)\n- [Layerwise Recall and the Geometry of Interwoven Knowledge](https://arxiv.org/abs/2502.10871)\n- [Geometric Deviation as Reliability Signal](https://arxiv.org/abs/2605.03196)\n- [Why Better Cross-Lingual Alignment Fails](https://arxiv.org/abs/2603.18863)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Multilingual Factual Consistency Evaluation](https://www.emergentmind.com/topics/multilingual-factual-consistency-evaluation)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Per-Fact Cross-Lingual Knowledge Geometry: An SVD Analysis Framework and Collinearity Training Objective\n\n## Description\nWe propose a per-fact geometric analysis framework and collinearity training objective (MFC loss) for cross-lingual knowledge representations. The PRIMARY contribution is analytical: SVD decomposition of per-fact multilingual representation matrices yields three novel tools — (1) a sigma_1 dominance ratio (C_k) providing a continuous, interpretable per-fact collinearity metric that no existing method offers, (2) dominant fact direction vectors enabling visualization and mechanistic analysis, and (3) language deviation profiles identifying which languages/scripts diverge for specific facts. The SECONDARY contribution is MFC training loss — the natural differentiable counterpart — with inter-fact orthogonality regularization. While DCO (+2.7-13.8 RankC), SubInj (+4.1-31.6% recall), Paths Not Taken (+19.04pp avg), and AlignX all improve consistency, none provides per-fact geometric characterization. Two recent findings provide strong mechanistic support: DALI (EACL 2026) demonstrates via activation patching that middle-layer alignment CAUSALLY determines cross-lingual correctness (13.05% Δ DALI); Paths Not Taken (EMNLP 2025) identifies the English-centric pipeline with +35% recall via layer-specific vector interventions. The core paper evaluates MFC against per-fact contrastive, cosine, and CKA alternatives (±orthogonality) on Qwen3-8B and Llama-3.1-8B using Bi-ZsRE/MzsRE. Extensions: DCO/SubInj combinations, CLM-Bench three-tier editability (targeting 39-46% from 30.93%), script stratification. Targets: +2-4% Bi-ZsRE behavioral; C_k ~0.5→~0.75 geometric; +8-15pt editability. Positioned as 'geometric analysis + training method' comparable to Beneath the Surface or DALI, but with an actionable training objective.\n\n## Core Problem\nSafety alignment transfers universally across languages via a single refusal direction (pairwise agreement 0.97 with MLC loss), and recent DPO-based methods (DCO, CALM, CM-Align) achieve strong behavioral consistency by aligning response-level preferences across languages. However, these preference-based approaches operate at the response ranking level — they ensure the model gives the SAME answer across languages but do not control HOW individual facts are geometrically encoded in representation space. Meanwhile, factual knowledge remains trapped in language-specific subspaces (CLM-Bench: 30.93% cross-lingual transfer for MEMIT on Llama3-8B), with edit vectors nearly orthogonal across languages. Representation-level alignment methods exist — AlignX (EMNLP 2025) applies instruction contrastive learning at layer 16 to align general multilingual representations — but target general semantic proximity, not per-fact directional structure. A critical complication from mechanistic analysis: 'How Do Multilingual Models Remember?' (ACL 2025 Findings) demonstrates that factual recall has two distinct phases — subject enrichment in middle layers is language-independent, but object extraction in later layers is language-dependent. 'Paths Not Taken' (EMNLP 2025) further validates this via an English-centric pipeline analysis on Llama-3.2-3B: middle layers (10-21) perform English-dominant factual retrieval, while late layers (21-27) handle language-specific translation, with two targeted vector interventions yielding +19.04pp average non-English recall improvement. 'Can you map it to English?' (EACL 2026) provides CAUSAL evidence via activation patching on Llama 3.1 8B across 24 languages: incorrect non-English predictions are associated with lower representation alignment with English in middle layers (13.05% Δ in DALI scores on Belebele), and can be FIXED by patching English activations at middle layers — directly demonstrating that middle-layer alignment quality causally determines cross-lingual factual performance. Additionally, 'Beneath the Surface of Consistency' (NAACL 2025) shows script similarity dominates representation sharing (same-script SR: 40-60%, cross-script SR: 10-20%), and CLAS (arXiv 2026) finds that performance gains correlate with language cluster separation rather than strict alignment. Yet Lost in Multilinguality (ACL 2025) shows knowledge IS language-independent in middle layers. A further complication from entity-level analysis: 'On the Entity-Level Alignment in Crosslingual Consistency' (arXiv 2025) demonstrates that >99% of cross-lingually consistent facts involve successful entity alignment in highly multilingual models like Gemma and Qwen, with SubInj achieving +4.1-31.6% recall and +9.2-43.9% consistency gains across 12 decoder models simply by injecting English subject translations at inference time. This reveals a two-level bottleneck: (1) entity identification — the model must correctly map language-specific entity references to the shared conceptual space (addressed by SubInj at the input level), and (2) fact encoding geometry — even when entities are correctly identified, the resulting fact representations may lack cross-lingual directional alignment. Despite converging evidence that middle-layer geometry matters for cross-lingual knowledge, NO existing work provides tools to MEASURE per-fact directional alignment quality or to ENFORCE it at the individual fact level during training. This is both an analytical gap (we cannot characterize how well any given fact is cross-lingually encoded) and a training gap (we cannot directly optimize per-fact geometric structure).\n\n## Opportunity\nThe competitive landscape for cross-lingual consistency spans three levels: DPO-based behavioral methods (DCO, CALM), representation-level alignment methods (AlignX, Middle-Layer Representation Alignment), entity-level input interventions (SubInj), and inference-time vector interventions (Paths Not Taken). However, a critical analytical and training gap remains: per-fact geometric characterization and control of cross-lingual knowledge representations.\n\nThe PRIMARY opportunity is analytical: no existing method provides quantifiable, per-fact measures of cross-lingual alignment quality. AlignX uses contrastive loss that encourages general proximity but produces no interpretable per-fact metric. DCO measures behavioral rank consistency but cannot diagnose WHERE in representation space alignment fails for specific facts. SubInj and Paths Not Taken provide inference-time fixes but no framework for understanding which facts are well-aligned and which are not. DALI (EACL 2026) provides instance-level alignment metrics but for NLU tasks, not factual knowledge specifically, and uses discriminative similarity rather than directional decomposition.\n\nSVD-based per-fact analysis fills this gap with a principled geometric framework: for each fact, decompose the multilingual representation matrix via SVD to obtain (1) a sigma_1 dominance ratio quantifying collinearity quality (1.0 = perfect alignment, 1/min(d,L) = uniform spread), (2) a dominant left singular vector u_1 representing the cross-lingual fact direction, and (3) residual singular values characterizing language-specific deviations. This enables three novel capabilities: (a) per-fact alignment DIAGNOSIS — identifying which facts, language pairs, and script combinations have poor cross-lingual geometry; (b) per-fact alignment TRAINING — the sigma_1 dominance ratio is differentiable (via robust SVD backward pass) and directly usable as a training objective; (c) inter-fact ORTHOGONALITY analysis — the Gram matrix of dominant directions across K facts reveals whether the model maintains distinguishable fact encodings or collapses them. The training objective (MFC loss) is the natural counterpart to the analysis framework — it optimizes exactly the metric that the framework measures.\n\nThree converging findings create the technical foundation: (1) CLM-Bench shows fact-specific edit vectors are orthogonal across languages — a geometric problem visible only through geometric analysis; (2) Lost in Multilinguality, 'How Do Multilingual Models Remember?', and 'Paths Not Taken' jointly establish that middle layers encode language-independent factual structure — providing the intervention point; (3) DALI's causal evidence (activation patching at middle layers fixes incorrect predictions) demonstrates that middle-layer alignment quality CAUSALLY determines downstream factual performance — validating that geometric improvement at this level translates to behavioral gains.\n\n## Related Work / Landscape\nDPO/Preference-based consistency methods (behavioral level): DCO (ICML 2026, arXiv:2603.04678) uses DPO-inspired cross-lingual likelihood ratios requiring no gold labels, achieving +2.7 to +13.8 RankC across 9 models (3B-14B): Qwen3-8B, Qwen3-14B (+2.7 label-free, +4.4 with gold), Qwen2.5-7B, Qwen2.5-14B (+13.1), Aya-Expanse-8B (+3.1), Llama3.1-8B (+13.8), Llama3.2-3B, Gemma3-4B, Gemma3-12B (+10.2). CALM (arXiv:2501.18457) uses cross-lingual self-alignment via majority voting + DPO. CM-Align (arXiv:2509.08541) constructs consistency-based multilingual preference pairs for DPO. Implicit Cross-Lingual Rewarding (ACL 2025, arXiv:2503.04647) transfers English DPO rewards cross-lingually. Batch-wise alignment (EMNLP 2025 Industry, arXiv:2509.23659) achieves +23.9% non-English accuracy. ALL optimize response-level ranking consistency but do not control or measure per-fact representation geometry.\n\nEntity-level input interventions: SubInj (arXiv 2025, arXiv:2510.10280) on 12 decoder models (LLaMA 1B/3B/8B, Qwen 1.7B/4B/8B, Gemma 1B/4B/12B, OLMo 1B/7B/13B), 17 languages, 8 scripts: >99% of consistent facts require entity alignment; SubInj achieves +4.1-31.6% recall (Gemma-12B: +4.1%, LLaMA-8B: +7.2%, Qwen-8B: +6.3%, OLMo-13B: +31.6%) and +9.2-43.9% consistency (training-free, inference-time). Largest gains in English-dominant models (OLMo) and non-Latin scripts.\n\nInference-time vector interventions: 'Paths Not Taken' (EMNLP 2025, arXiv:2505.20546) identifies the English-centric factual recall pipeline in Llama-3.2-3B across 6 languages (EN, ZH, JA, KO, FR, ES): middle layers (10-21) for English-dominant retrieval, late layers (21-27) for translation. Two vector interventions — translation difference vector at layer 21 (conversion: 39.56%→67.74%) and recall task vector at layer 3 (scale 2x) — yield +35% for lowest-performing language, +19.04pp average. Key distinction: inference-time FIXES via predetermined vectors; MFC provides training-time geometric FRAMEWORK.\n\nCausal evidence for middle-layer alignment: DALI (EACL 2026, arXiv:2504.09378) on Llama 3.1 8B, 24 languages, 3 NLU tasks (Belebele, XStoryCloze, XCOPA): incorrect predictions have 13.05% lower DALI on Belebele; activation patching with English activations at middle layers FIXES incorrect predictions — CAUSAL evidence. Effect strongest for retrieval-based tasks, matching MFC's target.\n\nRepresentation-level alignment: AlignX (EMNLP 2025, arXiv:2509.24338) — contrastive learning at layer 16, general alignment, no per-fact metric. Middle-Layer Representation Alignment (ACL 2025, arXiv:2502.14830) — contrastive at middle layers for slot filling/MT. MLC loss (ICLR 2026, arXiv:2602.16660) — SVD collinearity for single safety direction (Swahili: 6.11%→92.78%). No existing work applies SVD to per-fact knowledge.\n\nCounter-evidence: arXiv:2603.18863 — alignment-task orthogonality in XLM-R encoders for POS/classification (cosine -0.10 to +0.18). Specific to encoders and structural tasks; DALI's causal evidence and Paths Not Taken's pipeline analysis demonstrate alignment-recall ARE causally linked in decoder LLMs for factual tasks. CLAS (arXiv:2601.16390) — cluster separation benefits on XNLI/XQuAD. Beneath the Surface (NAACL 2025, arXiv:2408.10646) — script dominates sharing (same-script SR: 40-60%, cross-script: 10-20%).\n\nKnowledge editing: X-KDE (ACL 2025, arXiv:2502.14645) 91.04% Bi-ZsRE (Llama2-7b-chat), 87.10% (Qwen2.5-7B). LU-LAFNs (COLING 2025) 74.91%. LangEdit (ACL 2025, arXiv:2506.10800) null-space constraints. CLM-Bench (arXiv:2601.17397) MEMIT 30.93% cross-lingual transfer.\n\nMechanistic analysis: 'How Do Multilingual Models Remember?' (ACL 2025 Findings, arXiv:2410.14387) — subject enrichment LANGUAGE-INDEPENDENT (middle layers), object extraction LANGUAGE-DEPENDENT (late layers). Lost in Multilinguality (ACL 2025, arXiv:2504.04264) — middle-layer language independence, linear shortcut (+4.6-8.4). SVD stability: Robust Differentiable SVD (CVPR 2021, arXiv:2104.03821), Moore-Penrose SVD (arXiv:2411.14141).\n\n## Approach\nWe propose a per-fact geometric analysis framework and collinearity training objective for cross-lingual knowledge representations. The PRIMARY contribution is the SVD-based per-fact analysis framework — providing quantifiable, interpretable measures of cross-lingual fact alignment quality that no existing method offers. The SECONDARY contribution is MFC loss — the natural training counterpart that optimizes exactly the metric the framework measures. This positions the work as a 'geometric analysis + targeted training method' contribution, where behavioral gains are one validation signal among several.\n\nWe structure the work around a lean CORE (Components 1-2) and EXTENSIONS (Components 3-5).\n\n=== CORE PAPER ===\n\nComponent 1: Per-Fact Geometric Analysis Framework. For each factual triple (s, r, o), we construct a multilingual representation matrix Z_k ∈ R^{d×L} by stacking L2-normalized hidden states from L language prompts at target middle layers (l* ~ layer 16 for 32-layer models, convergently identified by Lost in Multilinguality, AlignX, Middle-Layer Representation Alignment, and causally validated by DALI's activation patching and Paths Not Taken's pipeline analysis). We apply SVD: Z_k = U_k Σ_k V_k^T. This yields three interpretable quantities per fact:\n\n(a) Sigma_1 dominance ratio: C_k = σ_1/Σ_j σ_j ∈ [1/min(d,L), 1.0]. Continuous scalar metric of per-fact collinearity quality. C_k = 1.0 means all L languages encode fact k along exactly the same direction; C_k ≈ 1/L means uniform spread. No analogous per-fact metric exists.\n\n(b) Dominant fact direction: u_1^(k) ∈ R^d — the left singular vector capturing the cross-lingual consensus direction for fact k. Enables visualization, cross-script comparison, and mechanistic analysis.\n\n(c) Language deviation profile: residual σ_2, σ_3, ... and corresponding right singular vectors in V_k reveal which languages deviate most from consensus. Enables per-language, per-fact diagnosis.\n\nNovel geometric analyses: (i) C_k distribution across K facts; (ii) C_k stratified by script type (testing Beneath the Surface prediction); (iii) C_k by model (Qwen3-8B vs. Llama-3.1-8B); (iv) C_k vs. behavioral consistency correlation.\n\nComponent 2: MFC Loss with Inter-Fact Orthogonality. The σ_1 dominance ratio is differentiable via robust SVD (CVPR 2021, Taylor expansion backward pass, ε=1e-6).\n\nPer-fact loss: L_cons^(k) = -log[exp(σ_1/τ) / Σ_j exp(σ_j/τ)].\nMFC loss: L_MFC = (1/K) Σ_k L_cons^(k).\nOrthogonality: G_K[i,j] = (u_1^(i))^T u_1^(j); L_ortho = ‖G_K - I_K‖²_F.\nTotal: L_total = L_task + λ_MFC·L_MFC + λ_ortho·L_ortho (integrated into LoRA + X-KDE's XE-IT).\n\nCore ablation — the paper's central empirical question: Does SVD-based directional enforcement produce measurably different geometric AND behavioral outcomes vs. simpler alternatives? Compare: (a) MFC; (b) per-fact contrastive loss (AlignX-style); (c) per-fact cosine similarity; (d) per-fact CKA; each ±orthogonality (8 configs). Measured via BOTH C_k (geometric) AND Bi-ZsRE/MzsRE (behavioral). If MFC produces higher C_k but similar behavioral gains, that STILL validates the analysis framework.\n\n=== EXTENSIONS ===\n\nComponent 3 (Ext A): Script-Aware Curriculum — same-script first (SR: 40-60%), then cross-script (10-20%).\n\nComponent 4 (Ext B): Pipeline Combinations — MFC alone; MFC+DCO; MFC+SubInj; MFC+DCO+SubInj. Tests stacking across distinct bottlenecks.\n\nComponent 5 (Ext C): CLM-Bench Three-Tier — (a) MEMIT editability on MFC-trained models (primary, from 30.93% baseline); (b) edit vector geometric analysis; (c) direct recall.\n\nAddressing Complexity-to-Impact. We directly acknowledge behavioral gains from MFC alone are modest relative to simpler methods (DCO: +2.7-13.8 RankC; SubInj: +4.1-31.6% recall; Paths Not Taken: +19.04pp; batch-wise: +23.9%). The primary contributions are: (a) ANALYTICAL — per-fact collinearity framework providing geometric insight no existing method offers; (b) MECHANISTIC — fact direction vectors enabling visualization/analysis of cross-lingual knowledge encoding, complementing Paths Not Taken and DALI from different angles; (c) EDITABILITY — MFC pre-training improving MEMIT cross-lingual transfer; (d) BEHAVIORAL — complementary gains with DCO/SubInj. Positioned as 'representation analysis + training method' — comparable to Beneath the Surface (analysis of sharing) or DALI (instance-level alignment metric), but with an actionable training objective.\n\nAddressing Object Extraction Bottleneck. MFC targets middle-layer subject enrichment. DALI's causal evidence validates that middle-layer improvement translates to behavioral gains. Paths Not Taken operationalizes the extraction fix (translation vector at layer 21: 39.56%→67.74%). These are complementary.\n\nAddressing Entity Alignment. SubInj: +4.1-31.6% recall via entity identification. MFC addresses post-identification geometric alignment. SubInj's 'necessary but not sufficient' finding motivates MFC.\n\nEvaluation.\n\nCore (2 models × 2 benchmarks + geometric analysis): Qwen3-8B, Llama-3.1-8B on Bi-ZsRE, MzsRE. 8-config ablation. Baselines: X-KDE (reproduced), LU-LAFNs, AlignX (fact-adapted).\n\nExtensions: DCO/SubInj combos (6 configs), CLM-Bench three-tier, CLiKA, BabelEdits, script-stratified analysis (es-pt, ru-uk, en-de, en-zh, en-ar), RankC.\n\nTargets: +2-4% Bi-ZsRE; C_k: ~0.5 baseline → ~0.75; script: +4-6% same-script, +1-3% cross-script; CLM-Bench editability: +8-15 points from 30.93%.\n\n## Inspiration\nCross-domain transfer (safety→knowledge) + MLC loss (ICLR 2026) + Middle-layer language-independence (Lost in Multilinguality; How Do Multilingual Models Remember?; Paths Not Taken) + Causal evidence for middle-layer alignment (DALI, EACL 2026) + Per-fact geometric analysis gap in ALL existing methods + Entity alignment prerequisite (SubInj) + Null-space orthogonality (LangEdit) + Script-dependent sharing (Beneath the Surface) + Orthogonality regularization (NeurIPS 2024)\n\n## Key References\n- Optimizing Language Models for Crosslingual Knowledge Consistency [DCO] (ICML 2026, arXiv:2603.04678)\n- Align Once, Benefit Multilingually [MLC] (ICLR 2026, arXiv:2602.16660)\n- AlignX (EMNLP 2025, arXiv:2509.24338)\n- On the Entity-Level Alignment in Crosslingual Consistency [SubInj] (arXiv 2025, arXiv:2510.10280)\n- Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline (EMNLP 2025, arXiv:2505.20546)\n- Can you map it to English? [DALI] (EACL 2026, arXiv:2504.09378)\n- How Do Multilingual Language Models Remember Facts? (ACL 2025 Findings, arXiv:2410.14387)\n- Beneath the Surface of Consistency (NAACL 2025 Findings, arXiv:2408.10646)\n- Why Better Cross-Lingual Alignment Fails (arXiv 2026, arXiv:2603.18863)\n- CLAS (arXiv 2026, arXiv:2601.16390)\n- LangEdit (ACL 2025 Findings, arXiv:2506.10800)\n- Lost in Multilinguality (ACL 2025, arXiv:2504.04264)\n- Middle-Layer Representation Alignment (ACL 2025, arXiv:2502.14830)\n- CLM-Bench (arXiv 2026, arXiv:2601.17397)\n- X-KDE (ACL 2025 Findings, arXiv:2502.14645)\n- LU-LAFNs (COLING 2025, arXiv:2406.16416)\n- CALM (arXiv 2025, arXiv:2501.18457)\n- CM-Align (arXiv 2025, arXiv:2509.08541)\n- Implicit Cross-Lingual Rewarding (ACL 2025 Findings, arXiv:2503.04647)\n- Batch-wise alignment (EMNLP 2025 Industry, arXiv:2509.23659)\n- CLiKA (NAACL 2024, arXiv:2404.04659)\n- Refusal Direction is Universal (arXiv 2025, arXiv:2505.17306)\n- MEMLA (arXiv 2024, arXiv:2406.11566)\n- BabelEdits (ACL 2025 Findings)\n- Robust Differentiable SVD (CVPR 2021, arXiv:2104.03821)\n- Moore-Penrose SVD (arXiv 2024, arXiv:2411.14141)\n- Orthogonality Regularization (NeurIPS 2024, arXiv:2411.00392)\n- Cross-Lingual Consistency of Factual Knowledge (EMNLP 2023)\n- Editing Across Languages Survey (EMNLP 2025)\n- MEMIT (ICLR 2023, arXiv:2210.07229)\n- Surgical Steering (arXiv 2025, arXiv:2510.26024)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '550 A100-hours (X-KDE repro ~40h, SVD analysis ~30h, LoRA ~25h/run × 10 core configs, eval ~80h, extensions ~120h)', 'timeline': '10 weeks total: Core 7 weeks (2w setup/repro/framework, 3w core experiments, 2w writing); Extensions +3 weeks', 'estimated_gpu_cost': '$825'}\n- **human_in_loop**: {'gpu_hours': '430 A100-hours', 'timeline': '8 weeks total: Core 6 weeks (1.5w setup, 2.5w experiments, 2w writing); Extensions +2 weeks', 'claude_api_cost': '$320', 'estimated_gpu_cost': '$645'}\n- **auto_research**: {'gpu_hours': '550 A100-hours', 'timeline': '6 weeks total: Core 4.5 weeks; Extensions +1.5 weeks', 'claude_api_cost': '$720', 'estimated_gpu_cost': '$825', 'speed_bottleneck': 'GPU for concurrent ablation; sequential: X-KDE repro → geometric analysis → MFC training → ablation'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T21:03:51.359Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:03:51.359Z",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T21:03:51.374Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make a well-informed evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. [Align Once, Benefit Multilingually (MLC loss)] (ICLR 2026, arXiv:2602.16660):
   最直接的前驱工作。使用 SVD 分解多语言安全表示矩阵，通过 σ_1 dominance 的 collinearity loss 对齐单一 safety refusal direction。本 proposal 的核心数学框架（SVD → σ_1 dominance → 可微 loss）直接源自此工作，扩展方向是从"1个safety concept"到"K个factual knowledge"。

2. [DCO: Optimizing Language Models for Crosslingual Knowledge Consistency] (arXiv 2603.04678, 投稿 ICML 2026):
   DPO-inspired 的 behavioral-level 跨语言一致性优化，不需要 gold labels，在 9 个模型上取得 +2.7 到 +13.8 RankC。与本 proposal 互补但也构成竞争——DCO 的 behavioral gains 显著高于本 proposal 预期的 +2-4%。

3. [DALI: Can you map it to English?] (EACL 2026, arXiv:2504.09378):
   通过 activation patching 在 Llama 3.1 8B 上提供因果证据：中间层对齐质量因果决定跨语言性能。为本 proposal 的中间层干预点提供了理论支撑，但 DALI 本身已提供 instance-level alignment metric，与 C_k 在分析层面存在功能重叠。

4. [Paths Not Taken] (EMNLP 2025, arXiv:2505.20546):
   识别 Llama-3.2-3B 中的 English-centric factual recall pipeline，两个 vector intervention 产生 +19.04pp 平均改善。推理时干预，behavioral impact 远超本 proposal 的训练时方法预期效果。

5. [AlignX] (EMNLP 2025, arXiv:2509.24338):
   两阶段 representation-level 框架，在 layer 16 用对比学习对齐多语言表示。无 per-fact metric，但已覆盖 representation alignment 的训练范式。

6. [SubInj: On the Entity-Level Alignment in Crosslingual Consistency] (arXiv 2025, arXiv:2510.10280):
   12个模型、17种语言上的 entity-level 对齐分析，training-free SubInj 取得 +4.1-31.6% recall。训练不需要的推理时方法，效果显著。

7. [CLM-Bench] (arXiv 2026, arXiv:2601.17397):
   揭示 MEMIT 编辑向量跨语言近似正交（30.93% cross-lingual transfer）。为本 proposal 的几何分析提供了直接 motivation。

8. [Why Better Cross-Lingual Alignment Fails] (arXiv 2026, arXiv:2603.18863):
   反面证据——在 XLM-R encoder 上，alignment 和 downstream task 目标是正交的。虽然限于 encoder + 结构任务，但对"几何对齐→行为改善"的因果链提出质疑。

9. [The Geometry of Multilingual Language Model Representations] (EMNLP 2022, arXiv:2205.10964):
   较早的工作已使用 SVD 分析多语言表示空间的几何结构，识别 language subspaces。表明 SVD 分析多语言表示并非全新方法论。

10. [A Joint Matrix Factorization Analysis of Multilingual Representations] (2023, arXiv:2310.15513):
    使用 PARAFAC2 矩阵分解同时分析多语言表示，与本 proposal 的矩阵分解分析路线存在方法论重叠。

- 调研总结：跨语言知识一致性是 2025-2026 年 NLP 的活跃研究方向，现有方法沿 behavioral (DCO)、representation (AlignX)、entity-level (SubInj)、inference-time intervention (Paths Not Taken) 四条路线推进。MLC (ICLR 2026) 已经在 safety 领域建立了 SVD collinearity 的范式。本 proposal 试图将 MLC 的 SVD collinearity 方法从 safety (1个方向) 推广到 per-fact knowledge (K个方向)，核心增量在于 per-fact 诊断工具和 inter-fact orthogonality。


【Trivial Alternative 检验】:

存在多个更简单的替代方案：

(1) **Per-fact 平均 pairwise cosine similarity**：对每个 fact 的 L 种语言表示计算平均 pairwise cosine，同样能得到一个连续的 per-fact 对齐度量。SVD 的 σ_1 dominance 在数学上等价于对 Gram 矩阵第一特征值占比的度量，与平均 cosine 高度相关。Proposal 确实将 per-fact cosine 作为 ablation baseline，但问题是：如果 cosine loss 的 behavioral 效果与 MFC 相当（这是很可能的结果），那 SVD 的额外复杂度是否值得？

(2) **AlignX-style per-fact contrastive loss**：直接将 AlignX 的对比学习从 general alignment 适配到 per-fact level。这也是 proposal 的 ablation 之一。

增量价值的核心辩护在于：SVD 提供的不只是一个标量（cosine 也能给），而是 (a) 主方向向量 u_1 用于可视化/机制分析，(b) 残差奇异值用于 per-language deviation 诊断，(c) 跨 fact 的 Gram 矩阵分析。但这些增量主要是 **分析工具层面的**——它们提供更丰富的诊断信息，但是否产生更好的训练效果是存疑的。如果 ablation 结果显示 MFC 和 cosine loss 的 behavioral 效果接近，那 SVD 框架的价值将主要局限于分析贡献，而分析贡献单独可能不够支撑一篇 top venue 论文。


【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的关键假设：

(1) **"per-fact collinearity improvement → behavioral improvement"**：这是最关键的假设。DALI 提供了中间层对齐→NLU 性能的因果证据，但 DALI 测试的是 NLU 任务（Belebele, XStoryCloze, XCOPA），不是 factual recall。"How Do Multilingual Models Remember?" 明确指出 factual recall 有两个阶段：中间层的 language-independent subject enrichment + 后层的 language-dependent object extraction。MFC 只优化中间层 subject enrichment 的几何结构，但如果瓶颈主要在 late-layer object extraction（Paths Not Taken 的发现支持这一点——翻译向量在 layer 21 的干预产生最大效果），那中间层的几何改善可能只解决一半问题，behavioral gains 就会受限。这解释了 proposal 自承的 modest behavioral targets (+2-4%)。

(2) **"per-fact SVD decomposition 在训练中是稳定的"**：虽然有 Robust Differentiable SVD (CVPR 2021) 的技术支撑，但 per-fact SVD 的计算/梯度在 mini-batch 训练中的实际表现（特别是当 L 种语言不全在同一 batch 中时）是未经验证的。这更偏 feasibility，但它影响 claim 的可验证性。

(3) **"inter-fact orthogonality 是有益的"**：proposal 假设不同 fact 的主方向应该正交。但如果相关的 facts（如同一 relation type）自然地共享方向，强制正交可能反而有害。这个假设缺乏理论支撑。


【3 维度打分】:

1. **Novelty: 中偏弱** —— 
   核心创新是将 MLC (ICLR 2026) 的 SVD collinearity 方法从单一 safety concept 推广到 per-fact knowledge。数学框架（SVD → σ_1 dominance → softmax-style loss）直接复用 MLC。推广的方向是自然且可预测的——从"1个方向"到"K个方向"加 orthogonality regularization 是一个 standard extension。Per-fact 诊断工具（language deviation profiles）有分析新意，但 SVD 分析多语言表示在方法论上已有先例（EMNLP 2022 的 Geometry of Multilingual LM Representations；2023 的 Joint Matrix Factorization Analysis）。与 DALI 的分析功能存在部分重叠——DALI 已提供 instance-level alignment metric，虽然用的是 discriminative similarity 而非 directional decomposition，但解决的是类似的"per-instance 诊断"需求。如果 MLC 已在 ICLR 2026 发表，审稿人很可能会问"这相对于 MLC 的 novelty 到底在哪"——答案是 per-fact 粒度和 orthogonality，但这可能被视为 incremental。

2. **Significance: 中** —— 
   跨语言知识一致性是一个重要且活跃的研究问题，有真实的应用价值。Proposal 定位的分析 gap（没有 per-fact 几何度量工具）是真实存在的。但问题在于：(a) 预期的 behavioral impact 是 modest 的（+2-4% Bi-ZsRE），proposal 自己承认 DCO、SubInj、Paths Not Taken 的 behavioral gains 都更大；(b) 分析工具的价值取决于它能否产生 actionable insights——如果发现 "cross-script facts have lower C_k" 这类结论，审稿人可能会说 "I would have guessed this"（Beneath the Surface 已经展示了 script similarity 主导 representation sharing）；(c) editability 改善（CLM-Bench +8-15pt from 30.93%）如果实现会有意义，但这在 Extensions 中，不是 core。Proposal 的定位为 "analysis + training method"（类比 Beneath the Surface, DALI），但 Beneath the Surface 和 DALI 都揭示了 surprising findings，而本 proposal 的预期发现是否会 surprising 存疑。

3. **Related Work: 强** —— 
   这是 proposal 最强的维度。相关工作覆盖极为全面，横跨 behavioral (DCO, CALM, CM-Align)、representation (AlignX, Middle-Layer RA)、entity-level (SubInj)、inference-time (Paths Not Taken)、mechanistic (DALI, How Do Multilingual Models Remember?, Lost in Multilinguality)、editing (X-KDE, CLM-Bench, LangEdit) 和 counter-evidence (arXiv:2603.18863, CLAS) 等多个维度。差异化定位清晰——proposal 准确地指出每个现有方法不提供 per-fact geometric characterization 这一 gap。对 counter-evidence 的处理也很诚实（承认 arXiv:2603.18863 的 alignment-task orthogonality 发现，给出合理但非铁证的辩护）。所有被引论文经搜索确认真实存在且描述基本准确。


【概率估计】: [20% - 32%] 中位 25%

【估计理由】: 
三维度综合推理：Related Work 强——不会因 related work 覆盖不足被拒，但 related work 好只防守下限不提升上限。Novelty 中偏弱是主要瓶颈——MLC→MFC 的推广路径过于自然，审稿人大概率会指出 "this is a straightforward extension of MLC (ICLR 2026) to per-fact setting"，而这正是区分 25% 和 35%+ 的关键：核心发现如果 positive（C_k 能刻画 per-fact 对齐、MFC loss 有效），审稿人的反应更可能是 "makes sense, but I would have expected this to work" 而不是 "surprising"。Significance 中——问题重要但预期 behavioral impact modest，分析贡献需要通过 surprising findings 来提升价值，而目前看不到哪个预期发现会是 surprising 的。上界被 Novelty 限制在 ~32%；下界被 Related Work 的全面性和分析 gap 的真实性托住在 ~20%。

【主要风险】:
1. **"Incremental over MLC" 风险**：最可能的拒稿理由。MLC (ICLR 2026) 已建立 SVD collinearity 的范式，本 proposal 的 per-fact 推广可能被视为 engineering extension 而非 conceptual contribution。如果 8-config ablation 中 per-fact cosine loss 效果与 MFC 接近，该风险将被放大为致命。
2. **Analysis-only 价值不足风险**：如果 behavioral gains modest（如 proposal 自预期的 +2-4%），论文价值将主要依赖分析贡献。但分析贡献要求产出 surprising 的 findings（如发现某类 fact 意外地已经 well-aligned，或 orthogonality regularization 意外有害），而不仅仅是确认已有假说（如 "cross-script facts have lower C_k"）。如果分析结论都在预期之内，审稿人可能认为 per-fact SVD 只是一个 expensive way to confirm what we already know。
```

Sources:
- [Align Once, Benefit Multilingually (MLC loss) - ICLR 2026](https://arxiv.org/abs/2602.16660)
- [DCO: Optimizing Language Models for Crosslingual Knowledge Consistency](https://arxiv.org/abs/2603.04678)
- [DALI: Can you map it to English? - EACL 2026](https://arxiv.org/abs/2504.09378)
- [Paths Not Taken - EMNLP 2025](https://arxiv.org/abs/2505.20546)
- [AlignX - EMNLP 2025](https://arxiv.org/abs/2509.24338)
- [SubInj: On the Entity-Level Alignment in Crosslingual Consistency](https://arxiv.org/abs/2510.10280)
- [CLM-Bench](https://arxiv.org/abs/2601.17397)
- [Why Better Cross-Lingual Alignment Fails](https://arxiv.org/abs/2603.18863)
- [The Geometry of Multilingual Language Model Representations](https://arxiv.org/abs/2205.10964)
- [A Joint Matrix Factorization Analysis of Multilingual Representations](https://arxiv.org/abs/2310.15513)
- [Beneath the Surface of Consistency - NAACL 2025](https://arxiv.org/abs/2408.10646)
- [X-KDE: Edit Once, Update Everywhere - ACL 2025](https://arxiv.org/abs/2502.14645)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough information to produce a thorough assessment. Let me compile my findings.

---

```
【阶段】: Triage
```

## ⚠️ 致命性前置问题：会议选择

**在评估 idea 质量之前，必须先指出一个致命问题：CoRL (Conference on Robot Learning) 是机器人学习会议。** 根据 CoRL 2026 官方 Call for Papers："Submissions without a robotics focus will be returned without review." 该 proposal 关于跨语言知识表征的 SVD 几何分析，属于纯 NLP/多语言 LLM 研究，与机器人学习完全无关。**投稿 CoRL 会被直接 desk reject，中稿概率为 0%。**

该 proposal 的合适会议应为 ACL、EMNLP、NAACL、ICLR、NeurIPS 等 NLP/ML 主会。以下评估基于假设投稿至合适的 NLP 主会（如 ACL/EMNLP 2026）来给出 idea 质量判断。

---

```
【领域调研】:
```

**1. MLC Loss (ICLR 2026, arXiv:2602.16660)**：该 proposal 最直接的"前驱"工作。MLC loss 使用 SVD 分解多语言表征矩阵的共线性来对齐安全方向（单一 refusal direction），将 Swahili 安全得分从 6.11% 提升至 92.78%。**关键区别**：MLC 针对单一安全方向，本 proposal 将其扩展到 per-fact 级别的数千个知识方向。这是核心 novelty claim 的基础，但也是最需要审视的——从"一个方向"到"数千个方向"的扩展是否面临根本性困难。

**2. DCO (ICML 2026, arXiv:2603.04678)**：DPO-inspired 的跨语言一致性优化，无需 gold label，在 9 个模型上获得 +2.7 到 +13.8 RankC。行为级别方法，不涉及表征几何分析。

**3. AlignX (EMNLP 2025, arXiv:2509.24338)**：Layer 16 的对比学习对齐多语言表征。通用语义对齐，不提供 per-fact 指标。是本 proposal 最直接的表征级别竞争者。

**4. SubInj (arXiv 2025, arXiv:2510.10280)**：12 个 decoder 模型上，通过注入英语 subject 翻译实现 +4.1-31.6% recall，训练免费、推理时干预。极其简单的方法获得了很大的效果提升。

**5. Paths Not Taken (EMNLP 2025, arXiv:2505.20546)**：识别了 Llama-3.2-3B 中英语中心的事实检索流水线，两个向量干预获得 +19.04pp 平均提升，最低性能语言 +35%。推理时干预，效果显著。

**6. DALI (EACL 2026, arXiv:2504.09378)**：Activation patching 因果证据证明中层对齐质量因果性地决定跨语言性能。24 种语言，3 个 NLU 任务。为中层干预提供了因果支持。

**7. CLM-Bench (arXiv 2026, arXiv:2601.17397)**：中英文化知识编辑基准，发现编辑向量跨语言近乎正交，MEMIT 跨语言迁移率仅 30.93%。

**8. Why Better Cross-Lingual Alignment Fails (arXiv 2026, arXiv:2603.18863)**：在 XLM-R 编码器上发现对齐和下游任务目标基本正交（cosine -0.10 to +0.18），显式对齐经常无法改善下游性能。**这是本 proposal 的潜在反面证据**——虽然作者限定于编码器和结构任务，但此发现对"改善几何对齐→改善行为"这一逻辑链构成质疑。

**9. CLAS (arXiv 2026, arXiv:2601.16390)**：发现有效迁移通过功能分化（cluster separation）而非严格对齐实现。与本 proposal 强制对齐的方向存在张力。

**10. Beneath the Surface of Consistency (NAACL 2025, arXiv:2408.10646)**：脚本相似性主导表征共享（同脚本 SR: 40-60%，跨脚本: 10-20%）。

**调研总结**：跨语言知识一致性是 2024-2026 的活跃研究领域，已形成清晰的分层竞争格局——行为级（DCO/CALM）、表征级（AlignX）、实体级（SubInj）、推理时干预（Paths Not Taken）。MLC loss 已将 SVD 共线性用于安全对齐。**本 proposal 的核心定位是将 SVD 共线性从"单方向安全对齐"扩展到"per-fact 知识对齐"，同时提供分析框架。** 这是一个合理但增量的扩展，而非概念性突破。

---

```
【Trivial Alternative 检验】:
```

**存在显著的 trivial alternative 威胁。**

1. **Per-fact 余弦相似度**：对于 L 种语言中每个 fact 的表征向量，计算所有语言对的 pairwise cosine similarity 的均值/方差，即可得到一个 per-fact 对齐质量指标。这比 SVD 计算量更低，解释性也不差。Proposal 自身将其列为 ablation baseline，这说明作者也意识到了这个威胁。

2. **Per-fact CKA**：同样可以衡量跨语言表征的相似性，无需 SVD 分解。

3. **Per-fact contrastive loss（AlignX 风格）**：直接在 per-fact 级别应用 AlignX 的对比学习，计算成本更低，不需要 SVD 的梯度反传（robust SVD backward 本身是一个工程挑战）。

**增量价值在哪？** 本 proposal 的 SVD 框架相对于 trivial alternatives 的真正增量在于：(a) C_k 是一个单一标量指标，而 pairwise cosine 产生 L(L-1)/2 个值需要聚合；(b) u_1 提供一个可解释的"共识方向"；(c) 残差奇异值给出语言偏差 profile。但这些增量主要是**分析便利性**而非**本质能力差异**。如果 8-config ablation 发现 cosine loss 在行为指标上与 MFC 无显著差异，整个工作的价值将大幅缩水。

---

```
【前提假设检验】:
```

核心 claim 的逻辑链存在多个未经验证的假设：

1. **「每个 fact 应该有一个 dominant direction」假设**（最关键）：MLC loss 对安全对齐有效，是因为 refusal 本质上是单一方向的（pairwise agreement 0.97）。但事实性知识（如 "巴黎是法国的首都"）是否也在表征空间中形成单一主方向？这是一个**强假设**。每个 fact 可能需要多维表征（subject、relation、object 分别编码），不同语言可能共享 subject 编码但 object 编码不同（正如 "How Do Multilingual Models Remember?" 所揭示的两阶段机制）。如果 fact 表征本质上不是一维共线的，强制 C_k → 1.0 可能是有害的。

2. **「几何对齐改善 → 行为改善」假设**：arXiv:2603.18863 明确发现在编码器上对齐与下游任务目标正交。虽然 DALI 提供了中层对齐的因果证据，但 DALI 测量的是 discriminative similarity（实例级别的匹配/不匹配区分能力），与 SVD 共线性是不同的数学量。**DALI 的因果证据不能直接迁移为 SVD 共线性的因果证据。**

3. **「中层是正确的干预点」假设**：多项工作（Lost in Multilinguality, DALI, Paths Not Taken）汇聚支持中层的重要性，但 "How Do Multilingual Models Remember?" 明确指出 object extraction 发生在后期层且是语言相关的。MFC 只在中层施加约束，可能无法解决后期层的瓶颈。作者也承认这一点，但将其视为"互补"——然而如果主要瓶颈在后期层（如 SubInj 和 Paths Not Taken 的结果所暗示），中层几何改善的行为收益可能确实很小（作者自己的目标也只是 +2-4%）。

4. **「inter-fact 正交性是可维持的」假设**：当 K 个 fact 的数量增长到数千级别时，d 维空间中 K 个方向不可能全部正交（K >> d 时）。正交性正则化在大规模下可能导致数值问题或与共线性目标冲突。

---

```
【3 维度打分】:
```

**1. Novelty: 中偏弱 — 理由：**

- 核心数学工具（SVD 分解多语言表征矩阵 → sigma_1 dominance ratio → differentiable loss）已在 MLC loss (ICLR 2026) 中被提出和验证，只不过用于安全对齐（单方向）。本 proposal 将其扩展到 per-fact 级别。这是一个**domain transfer + granularity extension**，而非全新方法论。
- Per-fact 分析的"框架"（C_k 指标、u_1 方向、偏差 profile）在数学上是 SVD 的标准输出，包装为"分析框架"有一定贡献，但核心操作是直接的。
- 与 AlignX 的区别主要在粒度（per-fact vs. general representation）和工具（SVD vs. contrastive），但如果 per-fact contrastive 效果相当，SVD 的 novelty 就被稀释。
- **加分点**：将分析框架与训练目标统一（"measure what you optimize"）这一设计理念确实比纯分析或纯训练更完整。
- **综合**：有增量 novelty，但不构成"surprising"级别的贡献。审稿人可能评价为"straightforward extension of MLC to per-fact level"。

**2. Significance: 中 — 理由：**

- 研究问题本身（跨语言知识的 per-fact 几何编码）是一个真实且有趣的问题。理解 LLM 如何在表征空间中编码跨语言事实，对多语言 AI 的可靠性有实际意义。
- 然而，**实际影响力受限于行为收益的天花板**。作者自身的目标只有 +2-4% Bi-ZsRE，而 SubInj（训练免费）已达 +4.1-31.6%，DCO 达 +2.7-13.8 RankC，Paths Not Taken 达 +19.04pp。一个需要训练的方法如果行为收益低于推理时免费干预，其实际价值存疑。
- 分析框架的 significance 取决于它是否能揭示**非平凡的发现**（如特定 fact 类型或脚本组合的几何特征）。如果分析结论只是"跨脚本 C_k < 同脚本 C_k"（已被 Beneath the Surface 预测），则分析贡献也不够 surprising。
- **作为 editability 改善路径的潜力**（CLM-Bench 30.93% → target 39-46%）是一个有趣的应用场景，但效果存疑。

**3. Related Work: 强 — 理由：**

- 这是本 proposal 最突出的优点。Related work 覆盖极为全面，跨越行为级（DCO/CALM/CM-Align）、表征级（AlignX/Middle-Layer）、实体级（SubInj）、推理时干预（Paths Not Taken）、因果分析（DALI）、知识编辑（X-KDE/CLM-Bench/LangEdit）、机制分析（How Do MLMs Remember/Lost in Multilinguality）等所有相关维度。
- 差异化定位清晰：proposal 明确说明了与每个竞争者在哪个维度上不同（行为 vs. 几何、通用 vs. per-fact、推理时 vs. 训练时）。
- 关键引用经调研验证均真实存在且描述基本准确（MLC, DCO, AlignX, SubInj, DALI, Paths Not Taken, CLM-Bench 等）。
- 反面证据也被包含（arXiv:2603.18863, CLAS 的 cluster separation），说明作者对领域有深入理解。
- **唯一不足**：部分论文的会议归属需要核实（如 DCO 标注为 ICML 2026，但当前仅为 arXiv preprint，ICML 2026 录用结果可能尚未公布）。

---

```
【概率估计】: [18% - 28%] 中位 22%
```

```
【估计理由】:
```

**从 3 维度到概率的推理：**

- **Novelty（中偏弱）限制了上界。** 核心方法是 MLC loss 的 per-fact 扩展，数学工具（SVD）是标准的，审稿人很可能会写 "This is a straightforward extension of [MLC, ICLR 2026] from safety to factual knowledge. The per-fact SVD analysis, while useful, is the standard output of SVD applied to a different matrix." 这使得上界被限制在 ~30% 以下。
- **Significance（中）提供了一定支撑但不够强。** 研究问题合理，但行为收益目标（+2-4%）远低于竞争方法，且作者采用了防守性定位（"分析为主，行为为辅"）。审稿人可能会质疑：如果行为收益不显著，为什么要用 550 A100-hours 训练模型而不是直接做纯分析？
- **Related Work（强）提供了下界保障。** 优秀的文献覆盖和差异化定位至少说明作者对领域有深入理解，论文的学术严谨性有保障，不太可能因为"忽略了关键相关工作"被拒。

**概率区间解释：**
- 下界 18%：如果 ablation 发现 cosine/contrastive loss 与 MFC 无显著差异，且分析未产生 surprising 发现，审稿人将给出 "limited novelty, incremental contribution"。
- 上界 28%：如果 per-fact 分析揭示了非平凡的几何现象（如特定 fact 类别的几何特征与行为强相关），且 MFC 在 editability 上展现出独特价值，可能获得部分审稿人的认可。
- 中位 22%：最可能的情况是 novelty 被认为增量但 related work 和实验严谨性得到认可，在 borderline 区域被一位审稿人支持、一到两位审稿人质疑 novelty 和 significance。

```
【主要风险】:
```

1. **"MLC 的直接扩展"批评**：最大的 idea 层面风险。MLC (ICLR 2026) 已经建立了 SVD 共线性 + differentiable loss 的完整方法论框架，本 proposal 在方法论上的唯一区别是"从一个方向扩展到多个方向 + 加了正交性正则"。审稿人极可能将此视为 incremental extension 而非独立贡献。如果作者无法论证 per-fact 扩展引入了 MLC 未面对的根本性新挑战（如大规模正交性维护、fact 表征的多维性），这一批评将难以反驳。

2. **Trivial alternative 的行为等效性**：如果 8-config ablation 显示 per-fact cosine similarity loss 在行为指标上与 MFC loss 无统计显著差异，则 SVD 框架的训练价值被直接否定。虽然分析框架仍有价值，但一篇"分析框架 + 训练 loss，其中训练 loss 不优于 cosine baseline"的论文很难说服审稿人给 accept。

---

Sources:
- [Align Once, Benefit Multilingually (MLC Loss, ICLR 2026)](https://arxiv.org/abs/2602.16660)
- [DCO: Optimizing Language Models for Crosslingual Knowledge Consistency](https://arxiv.org/abs/2603.04678)
- [AlignX: Advancing Multilingual LLMs with Multilingual Representation Alignment (EMNLP 2025)](https://arxiv.org/abs/2509.24338)
- [On the Entity-Level Alignment in Crosslingual Consistency (SubInj)](https://arxiv.org/abs/2510.10280)
- [Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline (EMNLP 2025)](https://arxiv.org/abs/2505.20546)
- [Can you map it to English? (DALI, EACL 2026)](https://arxiv.org/abs/2504.09378)
- [CLM-Bench: Benchmarking Cross-lingual Misalignment in Knowledge Editing](https://arxiv.org/abs/2601.17397)
- [Why Better Cross-Lingual Alignment Fails for Better Cross-Lingual Transfer](https://arxiv.org/abs/2603.18863)
- [Cross-Lingual Activation Steering (CLAS)](https://arxiv.org/abs/2601.16390)
- [Beneath the Surface of Consistency (NAACL 2025)](https://arxiv.org/abs/2408.10646)
- [X-KDE: Edit Once, Update Everywhere (ACL 2025)](https://arxiv.org/abs/2502.14645)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to complete the assessment. Let me compile my findings.

---

```
【阶段】: Triage
```

## ⚠️ 致命前置问题：会议-论文主题完全不匹配

在进入 idea 质量评估之前，必须首先指出一个 **致命的投稿问题**：

**CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求**："Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics" 以及 "**Submissions without a robotics focus will be returned without review.**"

本 proposal 完全是关于多语言 LLM 中跨语言知识表征的几何分析与训练目标，**与机器人学没有任何关系**。在 CoRL 投稿 = **desk reject**，概率趋近 0%。

本 proposal 适合的会议是 **ACL、EMNLP、NAACL、COLM** 等 NLP/CL 主会，或 **ICLR、NeurIPS、ICML** 等 ML 主会。以下评估基于将本 proposal 投稿至 NLP/CL 顶会（如 ACL/EMNLP）的假设进行。

---

```
【领域调研】:
```

- **MLC loss — "Align Once, Benefit Multilingually"** ([arXiv:2602.16660](https://arxiv.org/abs/2602.16660), ICLR 2026): 本 proposal 最直接的前驱工作。对**单一安全拒绝方向**使用 SVD collinearity loss，实现跨语言安全对齐 (DPO+MLC: avg safety 0.50→0.94，Swahili 6.11%→92.78%)。本 proposal 的核心就是将此思路从"单一安全方向"扩展到"K 个事实方向"。

- **DCO — "Optimizing Language Models for Crosslingual Knowledge Consistency"** ([arXiv:2603.04678](https://arxiv.org/abs/2603.04678), ICML 2026 under review): DPO-inspired 的 behavioral-level consistency 方法，无需 gold labels，+2.7-13.8 RankC across 9 models。在 response ranking 层面操作，不涉及 representation geometry。

- **AlignX** ([arXiv:2509.24338](https://arxiv.org/abs/2509.24338), EMNLP 2025): Layer 16 contrastive learning 做通用多语言表征对齐。不提供 per-fact metric，目标是一般语义对齐而非事实方向性结构。

- **DALI — "Can you map it to English?"** ([arXiv:2504.09378](https://arxiv.org/abs/2504.09378), **COLM 2025，非 proposal 中标注的 EACL 2026**): 提出 instance-level DALI 指标，activation patching 证明 middle-layer alignment 因果地决定跨语言正确性。但针对 NLU 任务（Belebele, XStoryCloze, XCOPA），非 factual knowledge。

- **SubInj — "On the Entity-Level Alignment"** ([arXiv:2510.10280](https://arxiv.org/abs/2510.10280), arXiv 2025): 证明 >99% 跨语言一致的事实需要实体对齐成功；SubInj 通过注入英语主语翻译实现 +4.1-31.6% recall。training-free，inference-time fix。

- **"Paths Not Taken"** ([arXiv:2505.20546](https://arxiv.org/abs/2505.20546), [EMNLP 2025](https://aclanthology.org/2025.emnlp-main.762/)): 揭示 English-centric pipeline（middle layers 做英语主导的事实检索，late layers 做翻译）。两个 vector interventions 实现 +19.04pp 平均 recall。

- **CLM-Bench** ([arXiv:2601.17397](https://arxiv.org/abs/2601.17397), arXiv 2026): 中英文 knowledge editing benchmark，MEMIT 跨语言 transfer 仅 30.93%，编辑向量跨语言近乎正交。

- **"How Do Multilingual Models Remember?"** ([arXiv:2410.14387](https://arxiv.org/abs/2410.14387), ACL 2025 Findings): subject enrichment 在 middle layers 是 language-independent，object extraction 在 late layers 是 language-dependent。

- **"Beneath the Surface of Consistency"** ([arXiv:2408.10646](https://arxiv.org/abs/2408.10646), NAACL 2025): script similarity 主导表征共享 (same-script SR: 40-60%, cross-script: 10-20%)。

- **"Layerwise Recall and the Geometry of Interwoven Knowledge in LLMs"** ([arXiv:2502.10871](https://arxiv.org/abs/2502.10871), 2025): 研究 LLM 中 multi-associated attributes 的 layerwise geometry，发现 intermediate layers 通过 overlapping spaces 编码知识，包含 3D spiral 结构等分析。是 representation geometry 分析方向的近期工作。

- **"Geometric Deviation as an Unsupervised Pre-Generation Reliability Signal"** ([arXiv:2605.03196](https://arxiv.org/abs/2605.03196), May 2026): 使用 hidden state 的 geometric deviation 做 pre-generation reliability 判断。表明 representation geometry 分析正在成为活跃方向。

- **调研总结**: 跨语言一致性是 2024-2026 的活跃领域，已有 behavioral-level (DCO)、entity-level (SubInj)、inference-time (Paths Not Taken)、general representation-level (AlignX) 的解决方案。MLC loss (ICLR 2026) 开创了 SVD collinearity 用于多语言对齐的先河，但仅用于单一安全方向。**Per-fact SVD analysis of knowledge representations 确实是一个未被填补的 gap**，但该 gap 在概念上是 MLC loss 向 knowledge domain 的自然扩展。

---

```
【Trivial Alternative 检验】:
```

**存在明确的 trivial alternative 威胁。**

1. **Per-fact 平均 pairwise cosine similarity**：对每个 fact 的 L 个语言表征计算两两 cosine similarity 的均值，即可获得一个 per-fact alignment 度量。这是 O(L²) 对 vs SVD 的 O(d·L²) 复杂度，更简单、更直观。Proposal 将此纳入了 ablation (Component 2 中 per-fact cosine baseline)，但 **核心问题是：如果 cosine-based metric 与 C_k 高度相关，且 cosine loss 能达到类似的 behavioral/geometric 效果，那整个 SVD framework 的增量价值就是有限的**。Proposal 声称 SVD 提供更丰富的信息（deviation profiles、dominant direction），但这些额外信息的实际价值是 empirical question，尚无先验理由认为它们一定比简单 cosine 好。

2. **CKA (Centered Kernel Alignment)**：也被纳入 ablation，同样是现成的、well-understood 的 representation similarity metric。

3. **AlignX-style per-fact contrastive loss**：将 AlignX 的 contrastive learning 从通用对齐适配到 per-fact 级别，也是一个 straightforward baseline。

**增量价值声明**：Proposal 的核心增量是 (a) C_k 提供的 continuous scalar metric 和 (b) u_1 dominant direction 的可解释性/可视化能力。但这些更多是 **engineering convenience**（更漂亮的度量、更好的可视化）而非 **fundamental capability difference**。如果 ablation 显示 cosine/CKA 在行为指标上与 MFC 相当，审稿人可能会质疑 SVD framework 的必要性。

---

```
【前提假设检验】:
```

核心 claim 的逻辑链中有 **三个关键未验证假设**：

1. **"Middle-layer per-fact collinearity improvement → behavioral factual recall improvement"（因果传导假设）**：Proposal 引用 DALI 的 causal evidence，但 DALI 证明的是 NLU 任务（Belebele 阅读理解等）上 middle-layer alignment → correctness 的因果关系，**不是 factual knowledge recall 上的因果关系**。"How Do Multilingual Models Remember?" 明确指出 object extraction 在 late layers 且 language-dependent——这意味着即使 middle-layer collinearity 完美，late-layer extraction 仍然可能是瓶颈。Proposal 承认了这一点但将其视为"complementary"而非"limiting factor"，这是一个乐观假设。

2. **"SVD dominance ratio C_k 是比 cosine similarity 更好的 per-fact alignment 度量"（度量优越性假设）**：没有理论或实证理由支持 σ₁/Σσⱼ 一定比 avg pairwise cosine 更能捕捉 cross-lingual alignment quality。两者在高 collinearity 时都趋近 1，在低 collinearity 时都趋近某个下界。SVD 的额外信息（deviation profiles）是否能转化为 actionable insights 完全是 empirical 的。

3. **"Per-fact orthogonality regularization 是必要的"（collapse 假设）**：假设没有 orthogonality loss，MFC 会导致 fact direction collapse（所有 u_1^(k) 指向同一方向）。但在 d >> K 的高维空间中（d ~ 4096, K ~ 数千），random directions 本身就近乎正交。这个 regularization 的必要性需要实证验证。

---

```
【3 维度打分】:
```

**1. Novelty: 中（偏弱）**

理由：
- **本质是 MLC loss (ICLR 2026) 的领域迁移**：从安全对齐的单一方向扩展到知识表征的 K 个方向。数学工具完全相同（SVD decomposition + softmax over singular values），应用场景从 safety → knowledge 是自然扩展。
- **Per-fact analysis framework 本身是 genuinely new gap**：基于调研，确实没有现有工作提供 per-fact 级别的跨语言对齐度量。这是真实的 novelty delta。
- **但 novelty 的"深度"有限**：核心创新是"将 SVD 应用到 per-fact representation matrix"——这是一个 application-level 的创新，而非 method-level 的创新。SVD 是标准工具，per-fact stacking 是直接的数据组织方式，softmax-over-singular-values 的 loss 是 MLC 已有的。
- 参考：MLC loss ([arXiv:2602.16660](https://arxiv.org/abs/2602.16660)) 已经做了 SVD collinearity；AlignX ([arXiv:2509.24338](https://arxiv.org/abs/2509.24338)) 已经做了 layer-specific representation alignment。本 proposal 的 novelty 是这两者的"交叉点"——在 AlignX 的 per-fact 粒度上使用 MLC 的 SVD 工具。

**2. Significance: 中**

理由：
- **跨语言事实一致性是重要问题**：被 DCO、SubInj、Paths Not Taken 等大量近期工作证实。
- **但 expected behavioral gains 诚实地标注为 modest (+2-4% Bi-ZsRE)**：这意味着即使一切如预期，对实际应用的 impact 有限。DCO (+2.7-13.8 RankC)、SubInj (+4.1-31.6% recall)、Paths Not Taken (+19.04pp) 都提供了更大的 behavioral gains。
- **Analysis-first positioning 的风险**：如果 C_k 与 behavioral metrics 高度相关（expected），那分析框架是 "nice to have"；如果相关性弱（possible），那分析框架的价值就存疑。Proposal 的 dual-outcome 设计（"If MFC produces higher C_k but similar behavioral gains, that STILL validates the analysis framework"）是 reasonable 的学术态度，但审稿人可能认为 "a metric that doesn't predict behavior is not very useful"。
- **Editability angle (CLM-Bench +8-15pt) 是潜在的 significance amplifier**：如果 MFC 预训练能显著提升 MEMIT 跨语言 transfer（从 30.93% baseline），这会是一个 compelling result。但这被放在 Extensions 而非 Core。

**3. Related Work: 强**

理由：
- **覆盖极其全面**：30+ 篇 reference，涵盖 behavioral (DCO, CALM, CM-Align)、entity-level (SubInj)、inference-time (Paths Not Taken)、representation-level (AlignX, Middle-Layer Repr. Alignment)、mechanistic (DALI, "How Do Multilingual Models Remember?", Lost in Multilinguality)、editing (X-KDE, CLM-Bench, LangEdit) 等全部相关分支。
- **差异化定位清晰**：明确说明每个竞争方法在 behavioral/entity/representation/geometric 层面的位置，以及本工作填补的 "per-fact geometric characterization" gap。
- **有一个事实错误**：DALI 论文 "Can you map it to English?" 发表于 **COLM 2025**（根据我的调研），而非 proposal 中标注的 "EACL 2026"。这是一个需要修正的引用错误。
- **Counter-evidence 的处理 fair but optimistic**：[arXiv:2603.18863](https://arxiv.org/abs/2603.18863) 关于 alignment-task orthogonality 的 counter-evidence 被正确引用，但 "specific to encoders and structural tasks" 的 dismiss 可能过于轻松。

---

```
【概率估计】: [20% - 32%] 中位 25%
```

（注：此概率基于投稿至 **ACL/EMNLP 等 NLP 主会** 的假设。若投稿 CoRL 2026，概率为 ~0%，因为 desk reject。）

```
【估计理由】:
```

本 proposal 填补了一个 genuine gap（per-fact geometric characterization），有扎实的理论动机（MLC→knowledge 的迁移、DALI/Paths Not Taken 的 causal evidence），related work 覆盖在本次调研中确认为极其全面。这些让它避免了 15% 以下的"方向不成立"区间。

然而，**Novelty 维度限制了上界**：核心创新本质是 MLC loss (ICLR 2026) 的领域扩展 + per-fact stacking，数学工具无新意。如果 ICLR 2026 已经发表了 SVD collinearity for multilingual alignment，那审稿人自然会问 "what's fundamentally new beyond applying MLC to knowledge?"。同时，**Trivial Alternative 威胁真实存在**——per-fact cosine similarity 可能在 ablation 中表现相当，从而削弱 SVD framework 的必要性。

此外，proposal 诚实承认 behavioral gains modest (+2-4%)，将 primary contribution 定位为 analytical。Analysis papers 在 NLP 主会可以发表（参考 "Beneath the Surface"、DALI），但需要 analysis 本身揭示 **surprising findings**。"有些 fact 比其他 fact 更好地跨语言对齐"、"same-script 比 cross-script 更对齐" 这些预期发现不太可能让审稿人感到 surprising。

```
【主要风险】:
```

1. **"MLC-for-knowledge" 被视为 incremental extension**：审稿人可能认为 MLC loss (ICLR 2026) 已经解决了 SVD collinearity 的核心方法论问题，本 proposal 仅是换了 application domain。如果 ICLR reviewer 已经在 MLC 的 related work 中讨论过 "potential extension to factual knowledge"，本 proposal 的 novelty 会进一步打折。

2. **Cosine ablation 的 outcome risk**：如果 per-fact cosine similarity loss 在 behavioral + geometric 两个维度上都与 MFC loss 表现相当，那整个 SVD framework 的价值叙事将崩塌。Proposal 的 dual-outcome framing（"C_k higher even if behavioral similar → still validates"）是审稿人可能不买账的防守性论述。

---

Sources:
- [MLC Loss - Align Once, Benefit Multilingually (ICLR 2026)](https://arxiv.org/abs/2602.16660)
- [DCO - Optimizing Language Models for Crosslingual Knowledge Consistency](https://arxiv.org/abs/2603.04678)
- [AlignX - EMNLP 2025](https://arxiv.org/abs/2509.24338)
- [DALI - Can you map it to English? (COLM 2025)](https://arxiv.org/abs/2504.09378)
- [SubInj - Entity-Level Alignment](https://arxiv.org/abs/2510.10280)
- [Paths Not Taken (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.762/)
- [CLM-Bench](https://arxiv.org/abs/2601.17397)
- [How Do Multilingual Models Remember? (ACL 2025 Findings)](https://arxiv.org/abs/2410.14387)
- [Beneath the Surface of Consistency (NAACL 2025)](https://arxiv.org/abs/2408.10646)
- [Layerwise Recall and the Geometry of Interwoven Knowledge](https://arxiv.org/abs/2502.10871)
- [Geometric Deviation as Reliability Signal](https://arxiv.org/abs/2605.03196)
- [Why Better Cross-Lingual Alignment Fails](https://arxiv.org/abs/2603.18863)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Multilingual Factual Consistency Evaluation](https://www.emergentmind.com/topics/multilingual-factual-consistency-evaluation)


【原始 proposal（允许参考但不是主要依据）】:
# Per-Fact Cross-Lingual Knowledge Geometry: An SVD Analysis Framework and Collinearity Training Objective

## Description
We propose a per-fact geometric analysis framework and collinearity training objective (MFC loss) for cross-lingual knowledge representations. The PRIMARY contribution is analytical: SVD decomposition of per-fact multilingual representation matrices yields three novel tools — (1) a sigma_1 dominance ratio (C_k) providing a continuous, interpretable per-fact collinearity metric that no existing method offers, (2) dominant fact direction vectors enabling visualization and mechanistic analysis, and (3) language deviation profiles identifying which languages/scripts diverge for specific facts. The SECONDARY contribution is MFC training loss — the natural differentiable counterpart — with inter-fact orthogonality regularization. While DCO (+2.7-13.8 RankC), SubInj (+4.1-31.6% recall), Paths Not Taken (+19.04pp avg), and AlignX all improve consistency, none provides per-fact geometric characterization. Two recent findings provide strong mechanistic support: DALI (EACL 2026) demonstrates via activation patching that middle-layer alignment CAUSALLY determines cross-lingual correctness (13.05% Δ DALI); Paths Not Taken (EMNLP 2025) identifies the English-centric pipeline with +35% recall via layer-specific vector interventions. The core paper evaluates MFC against per-fact contrastive, cosine, and CKA alternatives (±orthogonality) on Qwen3-8B and Llama-3.1-8B using Bi-ZsRE/MzsRE. Extensions: DCO/SubInj combinations, CLM-Bench three-tier editability (targeting 39-46% from 30.93%), script stratification. Targets: +2-4% Bi-ZsRE behavioral; C_k ~0.5→~0.75 geometric; +8-15pt editability. Positioned as 'geometric analysis + training method' comparable to Beneath the Surface or DALI, but with an actionable training objective.

## Core Problem
Safety alignment transfers universally across languages via a single refusal direction (pairwise agreement 0.97 with MLC loss), and recent DPO-based methods (DCO, CALM, CM-Align) achieve strong behavioral consistency by aligning response-level preferences across languages. However, these preference-based approaches operate at the response ranking level — they ensure the model gives the SAME answer across languages but do not control HOW individual facts are geometrically encoded in representation space. Meanwhile, factual knowledge remains trapped in language-specific subspaces (CLM-Bench: 30.93% cross-lingual transfer for MEMIT on Llama3-8B), with edit vectors nearly orthogonal across languages. Representation-level alignment methods exist — AlignX (EMNLP 2025) applies instruction contrastive learning at layer 16 to align general multilingual representations — but target general semantic proximity, not per-fact directional structure. A critical complication from mechanistic analysis: 'How Do Multilingual Models Remember?' (ACL 2025 Findings) demonstrates that factual recall has two distinct phases — subject enrichment in middle layers is language-independent, but object extraction in later layers is language-dependent. 'Paths Not Taken' (EMNLP 2025) further validates this via an English-centric pipeline analysis on Llama-3.2-3B: middle layers (10-21) perform English-dominant factual retrieval, while late layers (21-27) handle language-specific translation, with two targeted vector interventions yielding +19.04pp average non-English recall improvement. 'Can you map it to English?' (EACL 2026) provides CAUSAL evidence via activation patching on Llama 3.1 8B across 24 languages: incorrect non-English predictions are associated with lower representation alignment with English in middle layers (13.05% Δ in DALI scores on Belebele), and can be FIXED by patching English activations at middle layers — directly demonstrating that middle-layer alignment quality causally determines cross-lingual factual performance. Additionally, 'Beneath the Surface of Consistency' (NAACL 2025) shows script similarity dominates representation sharing (same-script SR: 40-60%, cross-script SR: 10-20%), and CLAS (arXiv 2026) finds that performance gains correlate with language cluster separation rather than strict alignment. Yet Lost in Multilinguality (ACL 2025) shows knowledge IS language-independent in middle layers. A further complication from entity-level analysis: 'On the Entity-Level Alignment in Crosslingual Consistency' (arXiv 2025) demonstrates that >99% of cross-lingually consistent facts involve successful entity alignment in highly multilingual models like Gemma and Qwen, with SubInj achieving +4.1-31.6% recall and +9.2-43.9% consistency gains across 12 decoder models simply by injecting English subject translations at inference time. This reveals a two-level bottleneck: (1) entity identification — the model must correctly map language-specific entity references to the shared conceptual space (addressed by SubInj at the input level), and (2) fact encoding geometry — even when entities are correctly identified, the resulting fact representations may lack cross-lingual directional alignment. Despite converging evidence that middle-layer geometry matters for cross-lingual knowledge, NO existing work provides tools to MEASURE per-fact directional alignment quality or to ENFORCE it at the individual fact level during training. This is both an analytical gap (we cannot characterize how well any given fact is cross-lingually encoded) and a training gap (we cannot directly optimize per-fact geometric structure).

## Opportunity
The competitive landscape for cross-lingual consistency spans three levels: DPO-based behavioral methods (DCO, CALM), representation-level alignment methods (AlignX, Middle-Layer Representation Alignment), entity-level input interventions (SubInj), and inference-time vector interventions (Paths Not Taken). However, a critical analytical and training gap remains: per-fact geometric characterization and control of cross-lingual knowledge representations.

The PRIMARY opportunity is analytical: no existing method provides quantifiable, per-fact measures of cross-lingual alignment quality. AlignX uses contrastive loss that encourages general proximity but produces no interpretable per-fact metric. DCO measures behavioral rank consistency but cannot diagnose WHERE in representation space alignment fails for specific facts. SubInj and Paths Not Taken provide inference-time fixes but no framework for understanding which facts are well-aligned and which are not. DALI (EACL 2026) provides instance-level alignment metrics but for NLU tasks, not factual knowledge specifically, and uses discriminative similarity rather than directional decomposition.

SVD-based per-fact analysis fills this gap with a principled geometric framework: for each fact, decompose the multilingual representation matrix via SVD to obtain (1) a sigma_1 dominance ratio quantifying collinearity quality (1.0 = perfect alignment, 1/min(d,L) = uniform spread), (2) a dominant left singular vector u_1 representing the cross-lingual fact direction, and (3) residual singular values characterizing language-specific deviations. This enables three novel capabilities: (a) per-fact alignment DIAGNOSIS — identifying which facts, language pairs, and script combinations have poor cross-lingual geometry; (b) per-fact alignment TRAINING — the sigma_1 dominance ratio is differentiable (via robust SVD backward pass) and directly usable as a training objective; (c) inter-fact ORTHOGONALITY analysis — the Gram matrix of dominant directions across K facts reveals whether the model maintains distinguishable fact encodings or collapses them. The training objective (MFC loss) is the natural counterpart to the analysis framework — it optimizes exactly the metric that the framework measures.

Three converging findings create the technical foundation: (1) CLM-Bench shows fact-specific edit vectors are orthogonal across languages — a geometric problem visible only through geometric analysis; (2) Lost in Multilinguality, 'How Do Multilingual Models Remember?', and 'Paths Not Taken' jointly establish that middle layers encode language-independent factual structure — providing the intervention point; (3) DALI's causal evidence (activation patching at middle layers fixes incorrect predictions) demonstrates that middle-layer alignment quality CAUSALLY determines downstream factual performance — validating that geometric improvement at this level translates to behavioral gains.

## Related Work / Landscape
DPO/Preference-based consistency methods (behavioral level): DCO (ICML 2026, arXiv:2603.04678) uses DPO-inspired cross-lingual likelihood ratios requiring no gold labels, achieving +2.7 to +13.8 RankC across 9 models (3B-14B): Qwen3-8B, Qwen3-14B (+2.7 label-free, +4.4 with gold), Qwen2.5-7B, Qwen2.5-14B (+13.1), Aya-Expanse-8B (+3.1), Llama3.1-8B (+13.8), Llama3.2-3B, Gemma3-4B, Gemma3-12B (+10.2). CALM (arXiv:2501.18457) uses cross-lingual self-alignment via majority voting + DPO. CM-Align (arXiv:2509.08541) constructs consistency-based multilingual preference pairs for DPO. Implicit Cross-Lingual Rewarding (ACL 2025, arXiv:2503.04647) transfers English DPO rewards cross-lingually. Batch-wise alignment (EMNLP 2025 Industry, arXiv:2509.23659) achieves +23.9% non-English accuracy. ALL optimize response-level ranking consistency but do not control or measure per-fact representation geometry.

Entity-level input interventions: SubInj (arXiv 2025, arXiv:2510.10280) on 12 decoder models (LLaMA 1B/3B/8B, Qwen 1.7B/4B/8B, Gemma 1B/4B/12B, OLMo 1B/7B/13B), 17 languages, 8 scripts: >99% of consistent facts require entity alignment; SubInj achieves +4.1-31.6% recall (Gemma-12B: +4.1%, LLaMA-8B: +7.2%, Qwen-8B: +6.3%, OLMo-13B: +31.6%) and +9.2-43.9% consistency (training-free, inference-time). Largest gains in English-dominant models (OLMo) and non-Latin scripts.

Inference-time vector interventions: 'Paths Not Taken' (EMNLP 2025, arXiv:2505.20546) identifies the English-centric factual recall pipeline in Llama-3.2-3B across 6 languages (EN, ZH, JA, KO, FR, ES): middle layers (10-21) for English-dominant retrieval, late layers (21-27) for translation. Two vector interventions — translation difference vector at layer 21 (conversion: 39.56%→67.74%) and recall task vector at layer 3 (scale 2x) — yield +35% for lowest-performing language, +19.04pp average. Key distinction: inference-time FIXES via predetermined vectors; MFC provides training-time geometric FRAMEWORK.

Causal evidence for middle-layer alignment: DALI (EACL 2026, arXiv:2504.09378) on Llama 3.1 8B, 24 languages, 3 NLU tasks (Belebele, XStoryCloze, XCOPA): incorrect predictions have 13.05% lower DALI on Belebele; activation patching with English activations at middle layers FIXES incorrect predictions — CAUSAL evidence. Effect strongest for retrieval-based tasks, matching MFC's target.

Representation-level alignment: AlignX (EMNLP 2025, arXiv:2509.24338) — contrastive learning at layer 16, general alignment, no per-fact metric. Middle-Layer Representation Alignment (ACL 2025, arXiv:2502.14830) — contrastive at middle layers for slot filling/MT. MLC loss (ICLR 2026, arXiv:2602.16660) — SVD collinearity for single safety direction (Swahili: 6.11%→92.78%). No existing work applies SVD to per-fact knowledge.

Counter-evidence: arXiv:2603.18863 — alignment-task orthogonality in XLM-R encoders for POS/classification (cosine -0.10 to +0.18). Specific to encoders and structural tasks; DALI's causal evidence and Paths Not Taken's pipeline analysis demonstrate alignment-recall ARE causally linked in decoder LLMs for factual tasks. CLAS (arXiv:2601.16390) — cluster separation benefits on XNLI/XQuAD. Beneath the Surface (NAACL 2025, arXiv:2408.10646) — script dominates sharing (same-script SR: 40-60%, cross-script: 10-20%).

Knowledge editing: X-KDE (ACL 2025, arXiv:2502.14645) 91.04% Bi-ZsRE (Llama2-7b-chat), 87.10% (Qwen2.5-7B). LU-LAFNs (COLING 2025) 74.91%. LangEdit (ACL 2025, arXiv:2506.10800) null-space constraints. CLM-Bench (arXiv:2601.17397) MEMIT 30.93% cross-lingual transfer.

Mechanistic analysis: 'How Do Multilingual Models Remember?' (ACL 2025 Findings, arXiv:2410.14387) — subject enrichment LANGUAGE-INDEPENDENT (middle layers), object extraction LANGUAGE-DEPENDENT (late layers). Lost in Multilinguality (ACL 2025, arXiv:2504.04264) — middle-layer language independence, linear shortcut (+4.6-8.4). SVD stability: Robust Differentiable SVD (CVPR 2021, arXiv:2104.03821), Moore-Penrose SVD (arXiv:2411.14141).

## Approach
We propose a per-fact geometric analysis framework and collinearity training objective for cross-lingual knowledge representations. The PRIMARY contribution is the SVD-based per-fact analysis framework — providing quantifiable, interpretable measures of cross-lingual fact alignment quality that no existing method offers. The SECONDARY contribution is MFC loss — the natural training counterpart that optimizes exactly the metric the framework measures. This positions the work as a 'geometric analysis + targeted training method' contribution, where behavioral gains are one validation signal among several.

We structure the work around a lean CORE (Components 1-2) and EXTENSIONS (Components 3-5).

=== CORE PAPER ===

Component 1: Per-Fact Geometric Analysis Framework. For each factual triple (s, r, o), we construct a multilingual representation matrix Z_k ∈ R^{d×L} by stacking L2-normalized hidden states from L language prompts at target middle layers (l* ~ layer 16 for 32-layer models, convergently identified by Lost in Multilinguality, AlignX, Middle-Layer Representation Alignment, and causally validated by DALI's activation patching and Paths Not Taken's pipeline analysis). We apply SVD: Z_k = U_k Σ_k V_k^T. This yields three interpretable quantities per fact:

(a) Sigma_1 dominance ratio: C_k = σ_1/Σ_j σ_j ∈ [1/min(d,L), 1.0]. Continuous scalar metric of per-fact collinearity quality. C_k = 1.0 means all L languages encode fact k along exactly the same direction; C_k ≈ 1/L means uniform spread. No analogous per-fact metric exists.

(b) Dominant fact direction: u_1^(k) ∈ R^d — the left singular vector capturing the cross-lingual consensus direction for fact k. Enables visualization, cross-script comparison, and mechanistic analysis.

(c) Language deviation profile: residual σ_2, σ_3, ... and corresponding right singular vectors in V_k reveal which languages deviate most from consensus. Enables per-language, per-fact diagnosis.

Novel geometric analyses: (i) C_k distribution across K facts; (ii) C_k stratified by script type (testing Beneath the Surface prediction); (iii) C_k by model (Qwen3-8B vs. Llama-3.1-8B); (iv) C_k vs. behavioral consistency correlation.

Component 2: MFC Loss with Inter-Fact Orthogonality. The σ_1 dominance ratio is differentiable via robust SVD (CVPR 2021, Taylor expansion backward pass, ε=1e-6).

Per-fact loss: L_cons^(k) = -log[exp(σ_1/τ) / Σ_j exp(σ_j/τ)].
MFC loss: L_MFC = (1/K) Σ_k L_cons^(k).
Orthogonality: G_K[i,j] = (u_1^(i))^T u_1^(j); L_ortho = ‖G_K - I_K‖²_F.
Total: L_total = L_task + λ_MFC·L_MFC + λ_ortho·L_ortho (integrated into LoRA + X-KDE's XE-IT).

Core ablation — the paper's central empirical question: Does SVD-based directional enforcement produce measurably different geometric AND behavioral outcomes vs. simpler alternatives? Compare: (a) MFC; (b) per-fact contrastive loss (AlignX-style); (c) per-fact cosine similarity; (d) per-fact CKA; each ±orthogonality (8 configs). Measured via BOTH C_k (geometric) AND Bi-ZsRE/MzsRE (behavioral). If MFC produces higher C_k but similar behavioral gains, that STILL validates the analysis framework.

=== EXTENSIONS ===

Component 3 (Ext A): Script-Aware Curriculum — same-script first (SR: 40-60%), then cross-script (10-20%).

Component 4 (Ext B): Pipeline Combinations — MFC alone; MFC+DCO; MFC+SubInj; MFC+DCO+SubInj. Tests stacking across distinct bottlenecks.

Component 5 (Ext C): CLM-Bench Three-Tier — (a) MEMIT editability on MFC-trained models (primary, from 30.93% baseline); (b) edit vector geometric analysis; (c) direct recall.

Addressing Complexity-to-Impact. We directly acknowledge behavioral gains from MFC alone are modest relative to simpler methods (DCO: +2.7-13.8 RankC; SubInj: +4.1-31.6% recall; Paths Not Taken: +19.04pp; batch-wise: +23.9%). The primary contributions are: (a) ANALYTICAL — per-fact collinearity framework providing geometric insight no existing method offers; (b) MECHANISTIC — fact direction vectors enabling visualization/analysis of cross-lingual knowledge encoding, complementing Paths Not Taken and DALI from different angles; (c) EDITABILITY — MFC pre-training improving MEMIT cross-lingual transfer; (d) BEHAVIORAL — complementary gains with DCO/SubInj. Positioned as 'representation analysis + training method' — comparable to Beneath the Surface (analysis of sharing) or DALI (instance-level alignment metric), but with an actionable training objective.

Addressing Object Extraction Bottleneck. MFC targets middle-layer subject enrichment. DALI's causal evidence validates that middle-layer improvement translates to behavioral gains. Paths Not Taken operationalizes the extraction fix (translation vector at layer 21: 39.56%→67.74%). These are complementary.

Addressing Entity Alignment. SubInj: +4.1-31.6% recall via entity identification. MFC addresses post-identification geometric alignment. SubInj's 'necessary but not sufficient' finding motivates MFC.

Evaluation.

Core (2 models × 2 benchmarks + geometric analysis): Qwen3-8B, Llama-3.1-8B on Bi-ZsRE, MzsRE. 8-config ablation. Baselines: X-KDE (reproduced), LU-LAFNs, AlignX (fact-adapted).

Extensions: DCO/SubInj combos (6 configs), CLM-Bench three-tier, CLiKA, BabelEdits, script-stratified analysis (es-pt, ru-uk, en-de, en-zh, en-ar), RankC.

Targets: +2-4% Bi-ZsRE; C_k: ~0.5 baseline → ~0.75; script: +4-6% same-script, +1-3% cross-script; CLM-Bench editability: +8-15 points from 30.93%.

## Inspiration
Cross-domain transfer (safety→knowledge) + MLC loss (ICLR 2026) + Middle-layer language-independence (Lost in Multilinguality; How Do Multilingual Models Remember?; Paths Not Taken) + Causal evidence for middle-layer alignment (DALI, EACL 2026) + Per-fact geometric analysis gap in ALL existing methods + Entity alignment prerequisite (SubInj) + Null-space orthogonality (LangEdit) + Script-dependent sharing (Beneath the Surface) + Orthogonality regularization (NeurIPS 2024)

## Key References
- Optimizing Language Models for Crosslingual Knowledge Consistency [DCO] (ICML 2026, arXiv:2603.04678)
- Align Once, Benefit Multilingually [MLC] (ICLR 2026, arXiv:2602.16660)
- AlignX (EMNLP 2025, arXiv:2509.24338)
- On the Entity-Level Alignment in Crosslingual Consistency [SubInj] (arXiv 2025, arXiv:2510.10280)
- Paths Not Taken: Understanding and Mending the Multilingual Factual Recall Pipeline (EMNLP 2025, arXiv:2505.20546)
- Can you map it to English? [DALI] (EACL 2026, arXiv:2504.09378)
- How Do Multilingual Language Models Remember Facts? (ACL 2025 Findings, arXiv:2410.14387)
- Beneath the Surface of Consistency (NAACL 2025 Findings, arXiv:2408.10646)
- Why Better Cross-Lingual Alignment Fails (arXiv 2026, arXiv:2603.18863)
- CLAS (arXiv 2026, arXiv:2601.16390)
- LangEdit (ACL 2025 Findings, arXiv:2506.10800)
- Lost in Multilinguality (ACL 2025, arXiv:2504.04264)
- Middle-Layer Representation Alignment (ACL 2025, arXiv:2502.14830)
- CLM-Bench (arXiv 2026, arXiv:2601.17397)
- X-KDE (ACL 2025 Findings, arXiv:2502.14645)
- LU-LAFNs (COLING 2025, arXiv:2406.16416)
- CALM (arXiv 2025, arXiv:2501.18457)
- CM-Align (arXiv 2025, arXiv:2509.08541)
- Implicit Cross-Lingual Rewarding (ACL 2025 Findings, arXiv:2503.04647)
- Batch-wise alignment (EMNLP 2025 Industry, arXiv:2509.23659)
- CLiKA (NAACL 2024, arXiv:2404.04659)
- Refusal Direction is Universal (arXiv 2025, arXiv:2505.17306)
- MEMLA (arXiv 2024, arXiv:2406.11566)
- BabelEdits (ACL 2025 Findings)
- Robust Differentiable SVD (CVPR 2021, arXiv:2104.03821)
- Moore-Penrose SVD (arXiv 2024, arXiv:2411.14141)
- Orthogonality Regularization (NeurIPS 2024, arXiv:2411.00392)
- Cross-Lingual Consistency of Factual Knowledge (EMNLP 2023)
- Editing Across Languages Survey (EMNLP 2025)
- MEMIT (ICLR 2023, arXiv:2210.07229)
- Surgical Steering (arXiv 2025, arXiv:2510.26024)

## Resource Estimate
- **manual**: {'gpu_hours': '550 A100-hours (X-KDE repro ~40h, SVD analysis ~30h, LoRA ~25h/run × 10 core configs, eval ~80h, extensions ~120h)', 'timeline': '10 weeks total: Core 7 weeks (2w setup/repro/framework, 3w core experiments, 2w writing); Extensions +3 weeks', 'estimated_gpu_cost': '$825'}
- **human_in_loop**: {'gpu_hours': '430 A100-hours', 'timeline': '8 weeks total: Core 6 weeks (1.5w setup, 2.5w experiments, 2w writing); Extensions +2 weeks', 'claude_api_cost': '$320', 'estimated_gpu_cost': '$645'}
- **auto_research**: {'gpu_hours': '550 A100-hours', 'timeline': '6 weeks total: Core 4.5 weeks; Extensions +1.5 weeks', 'claude_api_cost': '$720', 'estimated_gpu_cost': '$825', 'speed_bottleneck': 'GPU for concurrent ablation; sequential: X-KDE repro → geometric analysis → MFC training → ablation'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a57a4f30-b6fe-46ee-9b7c-0f96223b895c",
  "type": "user",
  "uuid": "b3f90c1f-8ec3-4d86-9b5c-146684da361e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:03:51.371Z_

```json
{
  "parentUuid": "b3f90c1f-8ec3-4d86-9b5c-146684da361e",
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
  "uuid": "bc3aa76d-3a3c-43ec-af29-15ff9802eda4",
  "timestamp": "2026-05-19T21:03:51.371Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:03:51.371Z_

```json
{
  "parentUuid": "bc3aa76d-3a3c-43ec-af29-15ff9802eda4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0efc5575-bb90-4762-8c01-a7a494f9d25c",
  "timestamp": "2026-05-19T21:03:51.371Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a well-informed evaluat…",
  "leafUuid": "0efc5575-bb90-4762-8c01-a7a494f9d25c",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate multilingual knowledge representation geometry proposal",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:04:23.917Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

Let me first extract the key data points:

**Reviewer 1:**
- Novelty: 中偏弱
- Significance: 中
- Related Work: 强
- Probability: [20% - 32%] 中位 25%

**Reviewer 2:**
- Novelty: 中偏弱
- Significance: 中
- Related Work: 强
- Also flagged: CoRL desk reject (fatal venue mismatch)
- Probability (assuming NLP venue): [18% - 28%] 中位 22%


- Novelty: 中（偏弱）
- Significance: 中
- Related Work: 强
- Also flagged: CoRL desk reject (fatal venue mismatch)
- Probability (assuming NLP venue): [20% - 32%] 中位 25%

Now I'm calculating the consensus across all three reviewers. The median probabilities are 25%, 22%, and 25%, which gives me a mean of 24% with a standard deviation of about 1.41% — remarkably tight agreement despite the venue mismatch concerns flagged by two reviewers.

Looking at where the reviewers align, there's strong consensus that novelty is limited since this is essentially extending MLC to a new domain rather than introducing fundamental innovation, significance is moderate with only modest performance improvements, and the related work coverage is comprehensive across the board.

The critical vulnerabilities all three identified are the risk that a simple per-fact cosine similarity baseline could match MFC's performance, making the SVD framework's contribution questionable, plus the core concern that this feels incremental over MLC. They also all note that the middle-layer improvements might be overshadowed by bottlenecks in later processing stages, and both R2 and R3 see a venue mismatch with CoRL as a fatal issue. Finally, the analysis will only be compelling if it surfaces unexpected patterns beyond the obvious cross-script versus same-script comparison.

A few points stood out from individual reviewers: R3 caught a venue discrepancy in the proposal itself, R2 went deeper into CLAS cluster separation tensions, and R3 cited a couple of related works on geometric knowledge and reliability signals that the others didn't emphasize. All three referenced the same resource budget of 550 A100-hours and $825 in GPU costs.

Looking at the probability estimates, the three medians cluster tightly around 22–25% with minimal variance, suggesting strong agreement on the rejection likelihood.  The lower bounds converge around 20% and upper bounds around 30–32%, so I'm settling on a final range of 19–30% with a median of 24%, leaning slightly conservative given the consistent pattern across reviewers.

The venue mismatch flagged by two reviewers for CoRL is a critical issue that needs to be highlighted as a potential desk-reject problem. Beyond that, I should evaluate what implementation work the proposal actually requires based on the feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0efc5575-bb90-4762-8c01-a7a494f9d25c",
  "isSidechain": false,
  "requestId": "req_011CbCc4Nm8aePoWWZYKa8S3",
  "type": "assistant",
  "uuid": "8a161754-020c-4dd5-a8c9-1835907ac028",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CpxVPj349zwiXDxaSGSxz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23150,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3255,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 23150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23150
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

_source line 9 · 2026-05-19T21:05:07.305Z_

【阶段】: Meta Judge
【三次中位】: [25%, 22%, 25%]  std=1.4%
【共识维度】: 
- **Novelty: 中偏弱**（3/3 一致）— 核心方法是 MLC (ICLR 2026) 的 SVD collinearity 从 safety 单方向到 per-fact K 方向的领域扩展，数学工具无新意，属 straightforward extension
- **Significance: 中**（3/3 一致）— 问题重要但预期 behavioral gains modest (+2-4%)，远低于 SubInj (+4.1-31.6%)、Paths Not Taken (+19.04pp)、DCO (+2.7-13.8 RankC) 等竞争方法
- **Related Work: 强**（3/3 一致）— 覆盖全面，差异化定位清晰，引用经验证真实准确，包含 counter-evidence
- **Trivial Alternative 威胁真实存在**（3/3 一致）— per-fact cosine similarity 是最直接的 trivial alternative，若 ablation 显示 cosine loss ≈ MFC loss 在 behavioral 维度无显著差异，SVD 框架的训练价值被直接否定
- **"Incremental over MLC" 是首要拒稿风险**（3/3 一致）— 审稿人极可能写 "straightforward extension of MLC to per-fact level"
- **中间层干预点瓶颈**（3/3 一致）— late-layer object extraction 可能是真正瓶颈，中间层几何改善的 behavioral 收益天花板低
- **分析贡献需要 surprising findings**（3/3 一致）— 若分析结论仅为 "cross-script C_k < same-script C_k" 等已有预测，分析价值不足以支撑 top venue
- **CoRL 投稿 = desk reject**（2/3 明确标注）— CoRL 要求 robotics focus，本 proposal 是纯 NLP/多语言 LLM 研究，完全不匹配

【异常维度】: 
- R3 指出 DALI 论文发表于 COLM 2025 而非 proposal 标注的 EACL 2026（仅 R3 提出，属事实性纠正，值得采纳）
- R3 额外识别了 "Layerwise Recall and the Geometry of Interwoven Knowledge" (arXiv:2502.10871) 和 "Geometric Deviation as Reliability Signal" (arXiv:2605.03196) 两篇相关工作（仅 R3 提出，信号较弱，但表明 representation geometry 方向正变得拥挤）
- R2 对 DCO 会议归属提出质疑（标注为 ICML 2026 但可能仅为 arXiv preprint）（仅 R2 提出，属引用准确性问题）

【最终概率】: [19% - 30%] 中位 24%
【一致性】: 高（std=1.4%，三位审稿人在所有 rubric 维度的判决完全一致）

【综合理由】: 
三位审稿人在全部三个 rubric 维度上达成罕见的完全一致：Novelty 中偏弱、Significance 中、Related Work 强。核心问题高度收敛于同一诊断——MLC (ICLR 2026) 已建立 SVD collinearity 的完整方法论，本 proposal 的 per-fact 推广在概念深度上不足以构成独立贡献。三位同时识别 trivial alternative（cosine loss）为最大实验风险，同时识别 late-layer bottleneck 为理论瓶颈。

鉴于高一致性，取中位附近缩窄区间：中位从三份的 22%-25% 范围取 24%（略偏保守侧，遵循宁缺毋滥原则）。上界从 32%/28%/32% 缩窄至 30%（排除最宽松的 32%）。下界从 20%/18%/20% 取 19%（接近中位下界但略向严格方向偏移）。

**CoRL 投稿问题单独说明**：若坚持投 CoRL 2026，概率趋近 0%（desk reject）。以上 24% 估计基于投稿至 ACL/EMNLP/NAACL 等 NLP 主会的假设。这是一个必须在投稿前解决的致命前置问题。

**概率天花板分析**：Novelty 中偏弱 + Significance 中 → idea 质量天花板约 30-32%。即使实验完美执行、ablation 结果理想（MFC > cosine），审稿人仍大概率在 novelty 上给出 borderline-reject 评价。Related Work 强只防守下限（不会因遗漏被拒），不提升上限。

【建议】: 不推荐（中位 24% < 36% 阈值，且 idea 层面天花板有限——Novelty 中偏弱在三份评审中完全收敛，优化空间主要在 framing 而非 substance）

【实施评估】:
- **计算资源**: 550 A100-hours（含 X-KDE 复现 ~40h、SVD 分析 ~30h、LoRA 训练 ~25h/config × 10 核心配置、评测 ~80h、扩展实验 ~120h），预估 GPU 成本 ~$825。中等规模，对有 A100 集群访问的学术实验室可行
- **数据需求**: Bi-ZsRE、MzsRE（公开可得）、CLM-Bench（公开可得）、BabelEdits（公开可得）。无需私有数据或人工标注新数据集。数据需求是该 proposal 的优势——完全基于现有公开 benchmark
- **人工介入**: 无需人工标注。需要研究人员进行实验分析解读（C_k 分布、deviation profile 可视化），但这是标准学术工作量
- **训练需求**: 需要 LoRA fine-tuning Qwen3-8B 和 Llama-3.1-8B（两个 8B 参数模型）。每个配置约 25 A100-hours。核心 8-config ablation + baseline 复现，总训练量可控
- **新 Benchmark**: 不需要构建新 benchmark。C_k 指标本身是新的分析工具而非 benchmark，CLM-Bench 等使用现有 benchmark
- **预估周期**: 10 周（Core 7 周 + Extensions 3 周）。若有 AI 辅助可压缩至 6 周。瓶颈在 GPU 资源的并发能力——sequential 执行路径为 X-KDE 复现 → 几何分析 → MFC 训练 → ablation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a161754-020c-4dd5-a8c9-1835907ac028",
  "isSidechain": false,
  "requestId": "req_011CbCc4Nm8aePoWWZYKa8S3",
  "type": "assistant",
  "uuid": "075e1e5f-247a-49ce-8b3f-548608a9e154",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011CpxVPj349zwiXDxaSGSxz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23150,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3255,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 23150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23150
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a well-informed evaluat…",
  "leafUuid": "075e1e5f-247a-49ce-8b3f-548608a9e154",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate multilingual knowledge representation geometry proposal",
  "sessionId": "95dfc2f8-6a20-467b-b476-7547688888e8"
}
```

---
