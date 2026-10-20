# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/47dbb15e-7978-4708-be71-94230b7e7bf5.jsonl`
- **Structured JSON:** [`d37ccd9e715c132902b1.json`](../../sessions/d3/d37ccd9e715c132902b1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:59:26.910Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:59:26.910Z",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- CLiKA: \"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly\" (NAACL 2024, arXiv:2404.04659): 定义了 Cross-Retrieval Ratio (XRR) 度量 conductivity，发现所有测试 LLM 的 XRR < 0.01，多语言预训练和指令微调均无法实质性提升 conductivity。这是 proposal 的核心动机，已验证为真实存在的论文和发现。\n- CCL-XCoT (EMNLP Findings 2025, arXiv:2507.14239): 句子/段落粒度的对比学习 CPT，在 Gemma-7B 和 LLaMA-3.1-8B 上将跨语言幻觉降低 62%。使用课程化对比学习 + NTP，是最直接的句子级 baseline。该论文真实存在，但发表时间需注意——arXiv 为 2025 年 7 月，作为 EMNLP 2025 Findings 发表。\n- Liu & Niehues (ACL 2025, arXiv:2502.14830): 中间层（layer 16/32）句子级对比对齐，用于任务特定微调，在 slot filling 上 +1.5 F1，MT 上 +1.5 BLEU。验证了中间层是跨语言对齐的最佳位置，但仅在句子粒度和下游任务迁移。真实论文，ACL 2025 已发表。\n- \"On the Entity-Level Alignment in Crosslingual Consistency\" (arXiv:2510.10280): 发现实体对齐与跨语言一致性的 Pearson r > 0.7，>99% 一致的事实展示成功的实体对齐。提出 SubInj 方法（推理时插入英文实体名）获得 +14-32% recall 和 +17-44% 一致性提升。**关键竞争者**：此推理时方法已经取得了显著效果。\n- KBioXLM (EMNLP Findings 2023, arXiv:2311.11564): 在 XLM-R（encoder）上使用多粒度知识对齐（实体掩码、关系掩码、段落关系预测）进行 CPT，在跨语言零样本生物医学任务上 +20 F1。真实论文，但限于 encoder + 生物医学领域。\n- FactNet (arXiv:2602.03417, Feb 2026): 1.7B 实体锚定原子事实，316 个 Wikipedia 版本，Wikidata QID 链接，92.1% 精度。已在 arXiv 发布，GitHub 存在。是 EACA 的核心数据资源。\n- TransliCo (ACL 2024, arXiv:2401.06620): 在 encoder (Glot500-m) 上使用音译对比学习，5% 数据即可桥接脚本障碍。ACL 2024 真实论文。\n- DaMuEL (arXiv:2306.09288, 2023): 12.3B QID 标注 tokens，53 语言。真实数据集，CC BY-SA 许可。\n- Bandarkar et al. (arXiv:2603.17070, March 2026): 确认 script match 是知识迁移的主要预测因子（~13% gap），关键的 entity priming 实验显示提供源语言实体名可不成比例地改善跨脚本迁移。真实 arXiv 论文。\n- Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646): 通过知识编辑探针发现 script similarity 主导跨语言知识表征共享（同脚本 CKR ~37.6% vs. 跨脚本 <10-20%）。真实论文。\n- LEIA (ACL Findings 2024, arXiv:2402.11485): 在 decoder LLM CPT 中插入英文实体名（[translate]/[/translate] 标记），无对比损失，改善跨语言迁移。**关键 trivial alternative 候选者**。\n- EntityCS (EMNLP Findings 2022): 实体级代码切换，但限于 encoder。\n- Entity Lens (BlackboxNLP 2025, arXiv:2510.09421): decoder LLM 发展出实体特定机制来表征多 token 实体。\n\n- **调研总结**: 跨语言事实一致性领域正处于快速发展期。CLiKA 揭示的 conductivity gap（XRR < 0.01）是一个公认的未解决问题。现有方法沿两条路线发展：(1) 句子/段落级对比 CPT（CCL-XCoT, Liu & Niehues），在下游任务和幻觉上有效但未解决实体级 conductivity；(2) 推理时实体增强（SubInj, LEIA 式方法），有效但不改变模型内部表征。EACA 提出的\"实体级对比 CPT\"位于两条路线的交汇点，但这个交汇点目前确实没有被已有工作直接占据。\n\n【Trivial Alternative 检验】:\n存在两个需要认真对待的 trivial alternative：\n\n1. **SubInj（推理时实体增强）**：arXiv:2510.10280 的 SubInj 方法仅在推理时将英文实体名注入提示，就获得 +14-32% recall 和 +17-44% 一致性提升。这是零训练成本的方法。EACA 需要 1100-1600 H100 小时和 4-5 个月工程时间——如果最终效果与 SubInj 相当或仅小幅优于 SubInj，成本效益比极差。EACA 的增量价值论述是：训练时对齐改变模型内部表征，应该比推理时 prompt engineering 更根本、更泛化（不依赖于特定 prompt 格式）。这个论述逻辑上成立，但需要实验验证。\n\n2. **LEIA + CCL-XCoT 组合**：LEIA 已经在 CPT 中使用实体标记增强，CCL-XCoT 已经在 CPT 中使用对比学习。一个直接的 baseline 是将 LEIA 的实体标记与 CCL-XCoT 的句子级对比损失简单组合。如果这个简单组合已经能获得大部分收益，EACA 的\"实体级对比对齐\"的边际贡献就会被压缩。Proposal 意识到了 LEIA 作为 baseline 的存在（Phase 0 包含了 LEIA augmentation baseline），但没有明确讨论 \"LEIA + 句子级对比\" 这个组合 baseline 的威胁。\n\n**增量价值判断**：EACA 的真正增量在于将对比信号从句子级降到实体级并用结构化知识（FactNet QID）锚定正样本对。理论动机有据（r > 0.7 相关性，CLiKA 的 failure result），但这个增量是否大到足以 justify 系统复杂度，是实验需要回答的核心问题。Trivial alternative 威胁等级：**中等偏高**。\n\n【前提假设检验】:\n核心 claim 的逻辑链条：\n1. ✅ CLiKA 表明现有方法无法提升 conductivity（XRR < 0.01）→ **有实证支持**\n2. ✅ 实体对齐与跨语言一致性强相关（r > 0.7）→ **有实证支持**（arXiv:2510.10280）\n3. ⚠️ **\"句子级对比之所以不改善 conductivity，是因为粒度太粗，conflating entity-specific knowledge with syntactic variation\"** → **这是未经验证的假设**。CLiKA 测试的是标准多语言预训练和指令微调，CCL-XCoT 的句子级对比确实降低了幻觉 62%，但其对 CLiKA 的 XRR 指标的影响未知。Proposal 假设句子级对比无法改善 XRR，但这并未被实验验证——CCL-XCoT 论文没有报告 XRR 指标。\n4. ⚠️ **\"实体级对比对齐可以改善模型内部表征，而非仅仅是推理时效果\"** → **合理但未验证**。SubInj 的成功表明实体对齐是瓶颈，但 SubInj 是推理时的，EACA 假设训练时对比学习可以将这种对齐内化到模型表征中。虽然这在理论上合理（对比学习改变表征空间是有先例的），但在 decoder LLM 的 CPT 阶段使用实体级 InfoNCE 是否能有效改变中间层表征，以及是否比 NTP 自然学习的表征更好，并无先例。\n5. ⚠️ **\"在 decoder LLM 上的实体级对比损失不会严重干扰自回归语言建模能力\"** → 这是一个工程假设，有 CCL-XCoT 的句子级先例支持，但实体级对比（每个 batch 128-256 个 QID 的正/负样本对）的梯度动态与句子级可能不同。Proposal 通过 PCGrad 和 GradNorm 设计了缓解机制，但这本身就暗示了风险。\n\n**最关键的未验证假设**：第 3 点——\"句子级对比之所以失败是因为粒度问题\"。如果句子级对比实际上也能改善 XRR（只是没人测过），那 EACA 的核心动机就被削弱。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   EACA 的核心贡献是将对比 CPT 的粒度从句子级降至实体级，并用结构化知识图谱（FactNet QID）锚定对比对。这个组合在已有工作中确实不存在：CCL-XCoT 是句子级对比 CPT（EMNLP 2025 Findings），Liu & Niehues 是句子级中间层对比微调（ACL 2025），KBioXLM 是 encoder 上的实体掩码（EMNLP 2023 Findings），LEIA 是实体增强 CPT 无对比损失（ACL 2024 Findings），TransliCo 是 encoder 上的音译对比（ACL 2024）。EACA 位于这些工作的交叉点，这个特定的组合点确实是空白的。然而，novelty 主要来自\"组合\"而非\"新概念\"——每个组件（实体标记、对比损失、中间层提取、知识图谱锚定、音译增强、梯度冲突监控）都有明确的来源。对于审稿人来说，问题在于这是\"principled synthesis\"还是\"incremental combination\"——这很大程度上取决于实验结果是否显著超越各组件的简单组合。此外，arXiv:2510.10280 已经建立了\"实体对齐 → 一致性\"的强相关性，使得 EACA 的方向几乎是\"显而易见的下一步\"，降低了 surprise factor。\n\n2. **Significance: 中偏强** — \n   研究问题（跨语言知识 conductivity）是领域内公认的重要问题。CLiKA (NAACL 2024) 明确表明所有现有方法在 XRR 指标上几乎为零，这是一个 well-documented failure。如果 EACA 能够实质性提升 XRR（即便是从 <0.01 提升到 0.05-0.1），这将是一个有影响力的结果，因为它回答了一个目前无解的问题。此外，脚本障碍问题（Ifergan et al. NAACL 2025; Bandarkar et al. 2026）是多语言 NLP 的持久挑战，EACA 对此的针对性处理（音译增强 + 脚本分组评估）增加了实用价值。但 significance 受限于：(a) 实际应用场景——conductivity 改善对终端用户的实际影响尚不清楚；(b) 仅在 8B 模型上验证，scaling behavior 未知；(c) 如果效果仅在 same-script 上显著而 cross-script 改善有限（考虑到脚本障碍的严重性），影响力会打折。\n\n3. **Related Work: 强** — \n   这是 proposal 最强的维度。覆盖范围极为全面：从诊断框架（CLiKA）、对比 CPT（CCL-XCoT）、中间层对齐（Liu & Niehues）、实体级先例（KBioXLM、LEIA、EntityCS）、实体表征分析（Entity Lens、Marco et al.）、脚本障碍（Ifergan et al.、Bandarkar et al.、TransliCo）到数据资源（FactNet、DaMuEL），几乎无遗漏。差异化定位清晰——对 CCL-XCoT 有 5 轴差异分析，对 Liu & Niehues 有详细的粒度/目标/数据比较，对 KBioXLM 有 4 维度扩展论述。所有我能搜到的关键引用都被准确引用和描述。唯一的轻微不足是未讨论\"LEIA + 句子级对比\"这个组合 baseline 的威胁。\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \nNovelty 为中是主要限制因素。idea 的核心洞见（\"实体级对齐是 conductivity 的瓶颈，应该用实体级对比学习来解决\"）是被现有证据（r > 0.7 相关性）高度预测的\"下一步\"，而不是反直觉的发现。审稿人很可能会说\"the motivation is sound, but the contribution is primarily the engineering effort of putting known pieces together\"。Significance 中偏强——问题确实重要且 well-documented，但受制于 trivial alternative 威胁（SubInj 推理时已获得显著效果）。Related Work 强——但相关工作的完备性不能提升 idea 本身的 novelty 天花板。概率上界（35%）需要实验结果显著超越所有 trivial alternatives + 在 cross-script 上也有明显效果；下界（25%）对应审稿人认定为 incremental combination 的情况。注意：如果目标会议确实是 CoRL（Conference on Robot Learning），此 proposal 完全 off-topic，概率接近 0%——此处按 NLP/CL 顶会估计。\n\n【主要风险】: \n1. **\"Principled engineering\" vs. \"new idea\" 的审稿认知风险**：每个组件都有明确来源，核心假设（实体级 > 句子级）几乎是 arXiv:2510.10280 相关性结果的直接推论。审稿人可能认为这是\"well-executed combination\"而非\"novel contribution\"，在 novelty 维度给出 borderline reject。\n2. **Trivial alternative 的实验失败风险**：如果 SubInj（零训练成本的推理时方法）或 \"LEIA + CCL-XCoT\" 简单组合在 XRR 指标上与 EACA 效果相当，则 EACA 的 1100+ H100 小时投入和复杂 pipeline 难以 justify。这不是 idea 本身的缺陷，但它意味着 idea 的成功高度依赖于实验 delta 的大小。\n```\n\nSources:\n- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)\n- [CCL-XCoT - EMNLP Findings 2025](https://arxiv.org/abs/2507.14239)\n- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)\n- [Entity-Level Alignment in Crosslingual Consistency](https://arxiv.org/abs/2510.10280)\n- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)\n- [FactNet - arXiv 2026](https://arxiv.org/abs/2602.03417)\n- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)\n- [DaMuEL](https://arxiv.org/abs/2306.09288)\n- [Bandarkar et al. - Script Barrier](https://arxiv.org/abs/2603.17070)\n- [LEIA - ACL Findings 2024](https://aclanthology.org/2024.findings-acl.419/)\n- [Ifergan et al. - NAACL Findings 2025](https://arxiv.org/abs/2408.10646)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research material. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. CLiKA (Gao et al., NAACL 2024, arXiv:2404.04659):\n   定义了 cross-lingual knowledge conductivity 的 XRR 指标，发现即使经过多语言预训练和指令微调，XRR < 0.01，conductivity 几乎未被改善。这是本 proposal 所针对的核心 gap，论文真实存在，描述准确。\n\n2. CCL-XCoT (EMNLP 2025 Findings, arXiv:2507.14239):\n   句子/段落级对比学习 CPT，在 Gemma-7B 和 LLaMA-3.1-8B 上将跨语言幻觉减少最多 62%。是本 proposal 的主要 baseline。论文真实，描述准确。\n\n3. Liu & Niehues (ACL 2025, arXiv:2502.14830):\n   在 LLaMA-3-8B 的 layer 16 进行句子级中间层对比对齐，slot filling +1.5 F1，MT +1.5 BLEU。论文真实，描述准确。注意：该工作目标是 task-specific fine-tuning 的跨语言迁移，而非 factual conductivity。\n\n4. On the Entity-Level Alignment in Crosslingual Consistency (Liu, Wang et al., arXiv:2510.10280, Oct 2025):\n   发现 entity alignment 与 cross-lingual consistency 的 Pearson r > 0.7，>99% 的一致事实展现成功的实体对齐。**关键**：提出 SubInj 方法——在推理时注入英语实体翻译——即可获得 +14-32% recall 和 +17-44% consistency 提升，无需任何训练修改。论文真实。\n\n5. FactNet (arXiv:2602.03417, Feb 2026):\n   1.7B 实体锚定原子事实，覆盖 316 个 Wikipedia 版本，grounding precision 92.1%。论文真实，描述准确。\n\n6. Bandarkar et al. (arXiv:2603.17070, Mar 2026):\n   script match 是知识迁移失败的首要预测因素（~13% accuracy gap），entity priming 不成比例地改善跨脚本迁移。论文真实，描述准确。\n\n7. Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646):\n   same-script CKR ~37.6% vs. cross-script <10-20%。论文真实，描述准确。\n\n8. KBioXLM (EMNLP Findings 2023, arXiv:2311.11564):\n   在 XLM-R encoder 上用 masking-based 多粒度实体对齐，生物医学领域 +10+ F1。论文真实，描述准确。\n\n9. DCO (arXiv:2603.04678, Mar 2026):\n   DPO-inspired 后训练一致性优化方法，在 26 种语言上显著提升跨语言一致性。这是一种后处理方法，与 EACA 的预训练时方法互补。论文真实。\n\n10. TransliCo (ACL 2024, arXiv:2401.06620):\n    音译对比学习框架，仅用 5% 数据在 encoder 模型上桥接脚本障碍。论文真实。\n\n- **调研总结**: Cross-lingual factual consistency/conductivity 是一个活跃但尚未解决的研究方向。CLiKA 建立了诊断框架并揭示了 gap，CCL-XCoT 在句子级取得了进展，Liu et al. (arXiv:2510.10280) 从分析角度证明了实体对齐的重要性，DCO 提供了后训练解决方案。**尚无已发表工作将 entity-level contrastive alignment 应用于 decoder-only LLM 的 CPT 以专门解决 conductivity**——但这是因为 (a) 这是现有技术的自然组合，(b) SubInj 等推理时方法已经部分填补了这个 gap 且成本极低。EACA 处于\"自然下一步\"的位置：方向合理但不出人意料。\n\n\n【Trivial Alternative 检验】:\n\n**存在严重的 trivial alternative 威胁。**\n\n最直接的竞争者是 **SubInj/SubSub**（arXiv:2510.10280）：仅在推理时将英语实体名注入 prompt，即可获得 +14-32% recall 和 +17-44% consistency 提升，**零训练成本**。EACA 需要 1100-1600 H100-hours 的训练来达成一个在推理时就能部分实现的目标。\n\nEACA 的增量价值论点是：\n1. 推理时方法每次推理都需要实体链接 + 注入，增加延迟；训练时对齐是\"一劳永逸\"的\n2. 推理时方法依赖外部实体链接器的可用性和准确性\n3. 训练时对齐可能改变模型内部表征，从而在 SubInj 无法覆盖的场景（如开放生成、长文本推理）中也起作用\n\n但这些增量价值论点 *尚未被验证*。审稿人几乎一定会问：\"为什么不直接用 SubInj？如果 EACA 的提升与 SubInj 可比甚至不如，这 1000+ GPU-hours 的投入是否正当？\" Proposal 需要一个 **EACA vs. SubInj** 的直接对比（或 EACA + SubInj 是否叠加），目前缺失。\n\n此外，**LEIA + NTP-only CPT**（用 FactNet 数据做标准 CPT，只加 [ENT] 标记但不加对比 loss）也是一个需要排除的 trivial baseline。proposal 的 Phase 0 包含 LEIA-style baseline，这是好的，但如果 LEIA+CPT 就能拿到大部分 gain，entity-level contrastive 的增量就存疑。\n\n\n【前提假设检验】:\n\n核心逻辑链：\n```\nentity alignment 与 consistency 相关 (r>0.7)\n→ entity-level 对比 loss 可以改善 entity alignment\n→ 改善的 entity alignment 可以提升 conductivity (XRR)\n→ 效果优于句子级对比\n```\n\n**第一环节（相关性）**：实证支撑最强（arXiv:2510.10280），但**相关不等于因果**。r > 0.7 的相关性可能是因为\"容易对齐的实体碰巧也是容易迁移的知识\"，而非\"对齐实体就能产生迁移\"。SubInj 的成功提供了部分因果证据（干预实体名 → consistency 提升），但那是推理时干预，不能直接推导到训练时 hidden state 对比对齐也有同样效果。\n\n**第二环节（对比 loss 改善对齐）**：这是最薄弱的假设。在 encoder 模型上，这已被广泛验证。但在 **decoder-only LLM** 上，mean-pooling entity span 的 hidden states 作为对比学习 target 是否有效，存在合理怀疑：\n- Decoder 的 hidden states 是 causal/autoregressive 的，entity span 内的 token 只看到自己及之前的 context，span 内部信息不对称\n- Veitsman et al.（arXiv:2603.18863，proposal 自己引用）发现 sentence-level contrastive alignment 在 encoder 上对 token-level 任务无效——entity-level contrastive 在 decoder 上对 entity-specific 任务是否也有类似问题？\n- Entity Lens 的发现（decoder LLM 有 entity-specific 机制）是描述性的，不保证对比 loss 可以有效干预这些机制\n\n**第三环节（entity-level 优于 sentence-level）**：合理推测但无直接证据。CCL-XCoT 的句子级方法已经减少 62% 幻觉——如果 entity-level 只在此基础上带来边际提升，novelty story 就变弱了。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** —\n   核心贡献是\"将对比学习的粒度从句子级下移到实体级，并用 FactNet QID 作为锚点\"。这是 CCL-XCoT（句子级对比 CPT）+ KBioXLM（实体级对齐，但 encoder + masking）+ FactNet（数据源）+ TransliCo（脚本桥接）的自然组合。每个单独组件都有明确的先例：\n   - 对比 CPT：CCL-XCoT (EMNLP 2025)\n   - 中间层对比对齐：Liu & Niehues (ACL 2025)\n   - 实体级对齐在多语言模型中的应用：KBioXLM (EMNLP 2023)、LEIA (ACL 2024)、EntityCS (EMNLP 2022)\n   - QID 锚定实体标注：DaMuEL (2023)\n   - 脚本障碍的音译桥接：TransliCo (ACL 2024)\n\n   Proposal 的 \"六大 novelty\" 中的大部分是工程集成而非概念创新。真正新的是将这些成分 **同时组合并应用于 conductivity 这一特定目标**，但这更像是\"补全拼图的最后一块\"而非\"发现新拼图\"。如果结果 positive，多数了解该领域的审稿人会说 \"I would have guessed that entity-level would help — the interesting question is by how much\"，而非 \"this is surprising\"。\n\n2. **Significance: 中** —\n   研究问题（CLiKA 揭示的 conductivity gap）是真实且重要的。如果 EACA 有效，它填补了一个有价值的空白——从\"诊断 gap\"到\"提供解决方案\"。但 significance 被两个因素限制：(a) SubInj 等推理时方法已经提供了一个低成本的部分解决方案，削弱了训练时方法的紧迫性；(b) conductivity (XRR) 是一个相对小众的指标，它与下游任务性能的关系在 CLiKA 自身论文中也未被充分建立。对更广泛 NLP/CL 社区的影响力取决于 conductivity 改善是否转化为下游可见的收益（e.g., BMLAMA, TyDiQA）。\n\n3. **Related Work: 强** —\n   这是 proposal 最强的维度。文献覆盖极其全面（30+ 篇高度相关论文），每篇的定位和差异化描述都准确。关键论文（CLiKA、CCL-XCoT、Liu & Niehues、KBioXLM、Bandarkar、Ifergan、FactNet、TransliCo）全部真实存在且描述准确。调研中未发现任何被遗漏的直接竞争者。唯一的小遗漏是未讨论 SubInj 作为 trivial alternative 的竞争地位（proposal 引用了 arXiv:2510.10280 但主要作为支持证据而非竞争方法）。\n\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】:\n- Related Work 覆盖是强项，确保 proposal 不会因文献遗漏被拒\n- 问题真实、gap 明确（CLiKA 的 conductivity 空白），给出了合理的切入角度\n- 但 Novelty 是关键上界限制：核心贡献是现有技术的自然组合（entity-level contrastive = CCL-XCoT 的粒度下移 + KBioXLM 的思路迁移到 decoder），审稿人很可能认为这是\"预期中的下一步\"而非\"令人惊喜的发现\"\n- Trivial Alternative 威胁（SubInj 零训练成本获得可比效果）进一步压低了 idea 的增量价值感知\n- 核心逻辑链中\"decoder LLM 上 entity span mean-pooling + contrastive loss → 有效改善内部实体表征\"这一环节缺乏理论或实证支撑，是未验证的假设\n- 即使实验完美执行，如果核心发现是 \"entity-level beats sentence-level by X points\"，审稿人的反应更可能是 \"reasonable, I expected this\" 而非 \"surprising\"\n- 概率范围上界 28% 假设实验能展现出令人印象深刻的跨脚本 gains（目前是最未知的部分）；下界 18% 反映了若 entity-level 与 sentence-level 差异不够显著时的 trivial alternative 风险\n\n【主要风险】:\n1. **Trivial Alternative 致命质疑**：SubInj（推理时实体注入，零训练成本）可能达到与 EACA 可比的 consistency 提升，审稿人会质疑 1000+ GPU-hours 训练的正当性。如果 proposal 无法在实验中展示 EACA 在 SubInj 无法覆盖的场景下的独特优势（如开放生成、无 entity linker 的场景），增量价值论点无法成立。\n2. **\"I would have guessed this\" 风险**：核心 claim（entity-level 优于 sentence-level）是一个合理假设的实证验证，而非反直觉发现。如果实验结果只是确认了\"entity 粒度在 entity-centric 任务上比 sentence 粒度更好\"，审稿人可能认为 contribution 不足以支撑主会论文。\n```\n\n**补充说明**: 本 proposal 标注投稿 CoRL 2026（Conference on Robot Learning），但内容完全是 NLP/多语言 LLM 的 cross-lingual knowledge alignment 工作，与机器人学习无关。如果确实投稿 CoRL，会因主题不匹配被直接 desk reject。上述概率估计假设投稿至合适的 NLP 顶会（ACL/EMNLP/NAACL）。\n\nSources:\n- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)\n- [CLiKA - arXiv](https://arxiv.org/abs/2404.04659)\n- [CCL-XCoT - EMNLP 2025 Findings](https://aclanthology.org/2025.findings-emnlp.93/)\n- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)\n- [Entity-Level Alignment - arXiv:2510.10280](https://arxiv.org/abs/2510.10280)\n- [FactNet - arXiv:2602.03417](https://arxiv.org/abs/2602.03417)\n- [Bandarkar et al. - arXiv:2603.17070](https://arxiv.org/abs/2603.17070)\n- [Ifergan et al. - arXiv:2408.10646](https://arxiv.org/abs/2408.10646)\n- [KBioXLM - EMNLP 2023](https://aclanthology.org/2023.findings-emnlp.751/)\n- [DCO - arXiv:2603.04678](https://arxiv.org/abs/2603.04678)\n- [TransliCo - arXiv:2401.06620](https://arxiv.org/abs/2401.06620)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\n调研完毕。现在我已经掌握了足够的信息来进行客观评估。以下是我的入口评审报告：\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：venue mismatch】\n本 proposal 是一篇纯粹的多语言 NLP / cross-lingual representation learning 论文。\nCoRL 2026 (Conference on Robot Learning) 的 call for papers 明确要求：\n\"Submissions should focus on a core robotics problem and demonstrate \nthe relevance of proposed models, algorithms, datasets, and benchmarks \nto robotics.\"\n涵盖的 topic 包括 robot perception, manipulation, locomotion, imitation \nlearning, reinforcement learning for physical robots, sim-to-real transfer 等。\n\n本 proposal 与机器人学习没有任何关联——没有机器人实验、没有 embodied 场景、\n没有 sim-to-real、没有 physical interaction。投稿 CoRL 将面临 desk rejection。\n\n建议投稿 ACL / EMNLP / NAACL / COLM 等 NLP 主会。\n以下 idea 质量评估基于 NLP venue 标准进行（如投 CoRL，概率直接为 ~0%）。\n\n【领域调研】:\n- CLiKA (Gao et al., NAACL 2024, arXiv:2404.04659): \n  定义 knowledge conductivity 和 XRR metric，发现现有多语言预训练和\n  instruction tuning 均未能实质提升 XRR (< 0.01)。本 proposal 的核心\n  motivation 直接来源于此。论文真实存在，描述准确。\n\n- CCL-XCoT (EMNLP Findings 2025, arXiv:2507.14239): \n  句/段落级 contrastive CPT + XCoT prompting，降低跨语言幻觉 62%。\n  本 proposal 的主要 baseline。论文真实存在，描述准确。\n\n- Liu & Niehues (ACL 2025, arXiv:2502.14830): \n  middle-layer (layer 16/32) sentence-level contrastive alignment，\n  用于 task-specific fine-tuning 而非 factual consistency。\n  本 proposal 的方法论最近参照物。论文真实，描述准确。\n\n- KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564): \n  在 encoder (XLM-R) 上用 entity masking + relation masking 做\n  biomedical 跨语言 CPT，+20 F1。本 proposal 声称的 \"encoder → decoder, \n  masking → contrastive, biomedical → general\" 扩展确实存在真实 gap。\n\n- FactNet (arXiv:2602.03417, Feb 2026): \n  1.7B entity-grounded atomic facts，316 Wikipedia editions，92.1% \n  grounding precision。真实存在。为本 proposal 提供实体级对比对。\n\n- 实体级对齐与一致性 (Liu, Wang et al., arXiv:2510.10280): \n  Pearson r > 0.7 entity alignment vs. cross-lingual consistency。\n  真实存在，为 \"entity is the bottleneck\" 论点提供关键实证。\n\n- Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646): \n  script similarity 主导 CKR (~37.6% same-script vs. <10-20% cross-script)。\n  真实存在，描述准确。\n\n- Bandarkar et al. (arXiv:2603.17070, March 2026): \n  script match 是 knowledge transfer failure 的首要预测因子；entity priming \n  不成比例地帮助 cross-script transfer。真实存在，描述准确。关键的 entity \n  priming 实验确实支持 \"entity mapping is the bottleneck\" 论点。\n\n- TransliCo (Liu et al., ACL 2024, arXiv:2401.06620): \n  transliteration contrastive learning on Glot500-m encoder, 5% data, \n  cross-script transfer 提升。真实存在。\n\n- 调研总结: \n  Cross-lingual factual consistency/conductivity 是一个活跃且重要的研究方向。\n  当前工作分为三条线：(1) sentence/paragraph-level contrastive CPT (CCL-XCoT)；\n  (2) middle-layer sentence-level alignment (Liu & Niehues)；(3) entity-level \n  alignment 但限于 encoder + masking (KBioXLM) 或 inference-time intervention \n  (SubInj)。Proposal 定位在 \"entity-level × contrastive × decoder-only × \n  general-domain CPT\" 这个尚未被占据的交叉位置。这个 gap 是真实的，但也相当\n  可预测——是 2×2 matrix 中待填的格子。\n\n【Trivial Alternative 检验】:\n存在多个成本更低的替代方案，构成实质威胁：\n\n1. **LEIA-style entity augmentation (无 contrastive loss)**：\n   仅在 CPT 中插入 [ENT]entity_name[/ENT] 标记，不加对比学习。\n   proposal 自己将此列为 baseline，但如果 LEIA-style 已能达到大部分效果，\n   则 contrastive loss 的增量价值存疑。\n\n2. **SubInj inference-time intervention (arXiv:2510.10280)**：\n   在推理时注入 English entity cue，无需任何训练即可获得 +14-32% recall \n   和 +17-44% consistency。这是一个零训练成本的 alternative。\n   如果 EACA 需要 1100+ H100 hours 训练才能达到类似效果，\n   cost-effectiveness argument 会被严重质疑。\n\n3. **Code-switching at entity level**：\n   EntityCS (EMNLP Findings 2022) 已在 encoder 上做过 entity-level \n   code-switching。在 decoder 上直接复现这一策略 (无 contrastive loss) \n   可能是更简单的 baseline。\n\n增量价值需要 EACA 在实验中明确胜过这三个 alternative，特别是 SubInj \n(inference-time, 零训练成本)。这是 proposal 最大的 trivial alternative 威胁。\n\n【前提假设检验】:\n核心逻辑链: \"entity alignment correlates with consistency (r>0.7) \n→ entity alignment IS the bottleneck → contrastive training on entity \nrepresentations CAN fix this bottleneck → fixing it WILL improve conductivity\"\n\n未验证假设 (从前到后):\n\n1. **相关 ≠ 因果**: r > 0.7 correlation 不等于 entity alignment 是 \n   consistency 的 causal driver。可能二者都是某个更深层因素（如语言间词汇\n   重叠、训练数据分布）的结果。proposal 将此相关性直接作为因果论据使用。\n\n2. **contrastive loss 能否有效移动 entity representations**: \n   在 decoder-only LLM 中，entity span 的 hidden states 受 autoregressive \n   attention mask 影响（只能看到左侧上下文）。mean-pooling 这些 states \n   是否能产生足够 informative 的 entity representation 用于 contrastive \n   alignment 是未经验证的。encoder (KBioXLM) 中有效不等于 decoder 中有效。\n\n3. **CLiKA 的 conductivity gap 是否可通过 CPT 解决**: \n   CLiKA 发现 \"neither multilingual pretraining nor instruction tuning \n   substantially improves conductivity\"。如果标准 CPT 就不行，为什么 \n   entity-level contrastive CPT 就行？这个假设的逻辑跳跃在于：CLiKA 测试的 \n   CPT 不是 entity-level 的——但这并不能排除 conductivity gap 是更根本性的\n   architectural limitation（如 tokenizer-level script segregation）。\n\n4. **FactNet 覆盖足以支撑有效对比训练**: \n   特别对 Tier 3 语言 (SW/YO/KM)，估计仅 5K-60K entity-fact pairs。\n   以 128-256 entities/batch 的 batch size，negative diversity 是否足够？\n\n【3 维度打分】:\n\n1. Novelty: 中 — \n   核心 novelty 是将 entity-level contrastive alignment 从 encoder/masking \n   范式 (KBioXLM) 和 sentence-level contrastive CPT (CCL-XCoT, Liu & Niehues) \n   的交叉空白处填补，应用于 decoder-only LLM 的 general-domain conductivity。\n   这个 gap 确实存在（调研确认无直接竞争工作），但属于 \"2×2 matrix gap-filling\"\n   ——方向可预测，审稿人不太可能感到 surprised。声称的 \"6 novelties\" 中，\n   频率加权、gradient conflict monitoring、type-aware negatives 等都是\n   engineering decisions 而非概念创新。真正的 novelty delta 集中在一个点：\n   entity-level granularity for factual conductivity contrastive CPT。\n   这一个点是 solid 的，但 thin。\n\n2. Significance: 中偏强 — \n   Cross-lingual knowledge conductivity 是一个重要且未解决的问题 \n   (CLiKA XRR < 0.01 确认了这一点)。如果 EACA 能显著提升 XRR，\n   对多语言 NLP 领域有实质影响。但 significance 受制于两个因素：\n   (a) 如果 SubInj 这样的 inference-time method 已经能达到类似效果，\n   则 training-time intervention 的实际价值降低；\n   (b) 如果最终改进仅限于 same-script pairs (Ifergan et al. 的证据\n   暗示 cross-script 可能很难)，则 generalizability 受限。\n   问题本身重要，但 EACA 作为解决方案的 significance 取决于实验结果。\n\n3. Related Work: 强 — \n   Related work 覆盖异常全面。所有关键引用 (CLiKA, CCL-XCoT, \n   Liu & Niehues, KBioXLM, FactNet, Ifergan et al., Bandarkar et al., \n   TransliCo) 均经调研确认真实存在且描述准确。差异化定位清晰：\n   vs. CCL-XCoT (entity vs. sentence granularity), \n   vs. Liu & Niehues (CPT vs. task-specific, entity vs. sentence), \n   vs. KBioXLM (decoder vs. encoder, contrastive vs. masking, general vs. bio)。\n   一个小缺陷：未充分讨论 SubInj (inference-time) 作为 trivial alternative \n   的威胁，只提到它 \"only at inference time\" 但未正面论证为什么 training-time \n   intervention 优于 inference-time。\n\n【概率估计】: [22% - 32%] 中位 27%\n（注意：此为投稿 NLP 主会 (ACL/EMNLP) 的估计。投稿 CoRL 概率约 0-2%。）\n\n【估计理由】: \nNovelty 维度限制了上界。核心 idea \"entity-level > sentence-level for \ncontrastive CPT\" 是一个合理但可预测的假设——如果实验 positive，多数审稿人\n会说 \"makes sense given the evidence\" 而非 \"surprising\"。这将概率上限\n卡在 ~35% 以下。Related Work 的出色覆盖提供了稳固的下限 (~22%)。\nSignificance 处于中偏强，但受 trivial alternative (SubInj) 威胁。\n实验设计非常详尽（Phase 0 pilot, 多 ablation, gradient monitoring），\n这在后续执行中可以提升下限，但不改变 idea 上限。\n\n综合来看：这是一篇 well-motivated, well-positioned 的 \"填空式\" 工作。\ndirection 完全站得住脚，不会因 idea 问题被直接拒绝，但核心发现不太可能\n让审稿人写 \"surprising\"。中位 27% 反映了 \"solid but not exciting\" 的定位。\n\n【主要风险】:\n1. **Trivial Alternative 威胁 (SubInj)**：inference-time entity priming \n   零训练成本可达类似效果，审稿人会问 \"why pay 1100 GPU-hours for what \n   you can get with a prompt trick?\" 如果实验无法证明 training-time \n   alignment 在 XRR 上显著优于 inference-time intervention，这将是最\n   可能的拒稿理由。\n\n2. **Correlation ≠ Causation 质疑**：核心 motivation 依赖 entity alignment \n   与 consistency 的 r > 0.7 相关性，但审稿人可能质疑这是否反映因果关系。\n   如果 entity contrastive alignment 在实验中仅带来 marginal improvement \n   (如 XRR 从 0.01 到 0.03)，这一质疑将成为致命弱点。\n```\n\n---\n\n**补充说明（venue mismatch）**：\n\n这个 proposal 的领域调研、motivation chain、related work positioning 都做得非常扎实。但 **CoRL 是机器人学习会议**，接收的论文必须 \"focus on a core robotics problem\"，主题包括 manipulation, locomotion, perception, sim-to-real transfer 等。本 proposal 是纯粹的多语言 NLP 工作，与 robotics 无任何交集。\n\n**强烈建议**将目标 venue 更换为 ACL 2026 / EMNLP 2026 / NAACL 2026 / COLM 2026 等 NLP 主会，上述 27% 的概率估计即基于 NLP venue 标准。\n\nSources:\n- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)\n- [CCL-XCoT - EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.93/)\n- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)\n- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)\n- [FactNet - arXiv 2026](https://arxiv.org/abs/2602.03417)\n- [Entity-Level Alignment - arXiv 2510.10280](https://arxiv.org/html/2510.10280)\n- [Ifergan et al. - NAACL Findings 2025](https://aclanthology.org/2025.findings-naacl.475/)\n- [Bandarkar et al. - arXiv 2603.17070](https://arxiv.org/abs/2603.17070)\n- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity\n\n## Description\nEACA is a continued pretraining method that introduces InfoNCE contrastive loss on entity-span hidden states alongside standard next-token prediction, targeting entity-level cross-lingual knowledge conductivity — a capability that CLiKA (NAACL 2024) established is not substantially improved by existing multilingual pretraining or instruction tuning (XRR < 0.01). Unlike CCL-XCoT (sentence/paragraph-level contrastive CPT) and Liu & Niehues (ACL 2025, sentence-level middle-layer contrastive fine-tuning), EACA anchors contrastive pairs to Wikidata QIDs using FactNet's 1.7B entity-grounded atomic facts, operating at the entity level — the granularity empirically shown to be the bottleneck for cross-lingual consistency (entity alignment correlates at r > 0.7 with consistency, arXiv:2510.10280). This extends KBioXLM's (EMNLP Findings 2023) precedent of multi-granularity entity alignment in multilingual pretraining from encoder-based masking objectives in a specialized domain to explicit contrastive alignment in decoder-only LLMs for general-domain conductivity. Entity spans are marked with LEIA-style [ENT]/[/ENT] tokens using DaMuEL (12.3B QID-annotated tokens across 53 languages) as the primary annotation source for 10 of 13 target languages, supplemented by a Wikipedia wikilinks-to-QID extraction pipeline for the 3 uncovered Tier 3 languages (SW/YO/KM) and mReFinED entity linking for non-hyperlinked mention gap-filling, with 1.5-2 weeks budgeted for preprocessing. Representations are extracted via mean-pooling at middle layers (~layer 16, validated via Phase 0 sweep). The proposal explicitly addresses the script barrier identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070): script similarity dominates representation sharing (~37.6% same-script CKR vs. <10-20% cross-script), but entity priming disproportionately helps cross-script transfer, motivating entity-level alignment as targeting the right bottleneck. Cross-script QID pairs receive transliteration-augmented entity markers (e.g., [ENT]北京 (Beijing)[/ENT]), inspired by TransliCo (ACL 2024), with mandatory script-grouped evaluation (same-script vs. cross-script gains). Stratified batch construction uses 128-256 entities per batch with class-aware false-negative masking, type-aware hard negatives (~50% same-type entities via Wikidata P31 properties, following Robinson et al. ICLR 2021), and asymmetric positive sets for entities with uneven language coverage (K_min = 3 languages per QID). Joint optimization (L_NTP + λ·L_contrastive, λ=0.1 with warmup) includes gradient conflict monitoring: cosine similarity between NTP and contrastive gradients is tracked every 100 steps, with PCGrad (Yu et al., NeurIPS 2020) activated if conflicts exceed 30% of steps, and GradNorm (Chen et al., ICML 2018) for dynamic λ adjustment if gradient magnitudes diverge beyond 10:1. Inverse-frequency weighting prioritizes low-resource entity-facts. Catastrophic forgetting is mitigated through LoRA (rank 64) on middle layers (10-22), 15% general-domain replay, and cosine LR scheduling. A tiered language selection spans 13 languages across ~7 scripts: Tier 1 (EN/ZH/JA/DE), Tier 2 (AR/HI/TR/ID/VI/TH), Tier 3 (SW/YO/KM), with mandatory Phase 0 FactNet coverage audit and contingency replacements. Phase 0 pilot (500M tokens, 5 languages spanning ≥3 scripts, ~130 H100 hours) includes baselines against sentence-level contrastive (CCL-XCoT), middle-layer sentence contrastive (Liu & Niehues), masking-based entity alignment (KBioXLM-style adaptation), LEIA augmentation, and standard CPT, plus layer sweep, gradient analysis, and script-grouped evaluation. Six key novelties: (1) entity-level contrastive anchoring vs. sentence-level, (2) structured knowledge grounding via FactNet QIDs vs. parallel text, (3) frequency-aware weighting, (4) joint NTP+contrastive optimization with gradient conflict monitoring at entity level during CPT, (5) script-aware transliteration augmentation for cross-script entity alignment, (6) direct targeting of CLiKA's conductivity gap with script-stratified evaluation.\n\n## Core Problem\nCan entity-level contrastive alignment — anchored to Wikidata QIDs and grounded in FactNet's structured atomic facts — improve cross-lingual knowledge conductivity (as defined by CLiKA's XRR metric, Gao et al. NAACL 2024) more effectively than sentence/paragraph-level contrastive continued pretraining (e.g., CCL-XCoT) or sentence-level middle-layer alignment (Liu & Niehues, ACL 2025)? CLiKA established that neither multilingual pretraining nor instruction tuning substantially improves conductivity, with XRR scores below 0.01 for most non-English languages. EACA hypothesizes that this conductivity barrier persists because prior methods align at sentence/document granularity — conflating entity-specific factual knowledge with syntactic and discourse-level variation — whereas factual knowledge is inherently structured around entities (subject-property-object triples). A critical complication, identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070), is that script similarity is the dominant factor in cross-lingual representation sharing: high behavioral consistency does not imply shared internal representation for cross-script language pairs, and script match — not language family — is the primary predictor of knowledge transfer failure. Crucially, however, Bandarkar et al.'s entity priming experiment shows that providing source-language entity names disproportionately improves cross-script transfer, directly implicating entity-level mapping failure as the mechanism behind the script barrier. This suggests that entity-level contrastive alignment targets the right bottleneck, but that cross-script entity alignment requires additional support (e.g., transliteration augmentation) beyond what same-script entity alignment needs. EACA therefore addresses a two-level problem: (1) entity-level alignment as the fundamental unit of factual knowledge transfer, and (2) script-aware strategies to bridge the representation gap across writing systems.\n\n## Opportunity\nCCL-XCoT (EMNLP 2025 Findings) demonstrates that contrastive continued pretraining reduces cross-lingual hallucination by up to 62% but operates at sentence/paragraph granularity with parallel text. Liu & Niehues (ACL 2025) show that middle-layer contrastive alignment (layer 16 of 32 in LLaMA-3-8B) significantly improves cross-lingual transfer for downstream tasks, but again at sentence-level granularity and for task-specific fine-tuning rather than factual consistency. CLiKA (NAACL 2024) reveals a critical gap: existing multilingual pretraining and instruction tuning improve surface-level consistency but fail to improve knowledge conductivity (XRR < 0.01), suggesting that fundamentally different alignment granularity is needed. Meanwhile, FactNet (arXiv:2602.03417, Feb 2026) provides 1.7B entity-grounded atomic facts across 316 Wikipedia editions with Wikidata QID linking — enabling entity-level contrastive pairs grounded in structured knowledge. Entity Lens (BlackboxNLP 2025) confirms that decoder LLMs develop entity-specific internal mechanisms to represent multi-token entities. Liu et al. (EMNLP 2025 Findings) show that cross-lingual transfer is frequency-driven, with low-frequency facts benefiting most. Critically, recent evidence from entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) demonstrates that cross-lingual factual consistency correlates strongly with entity alignment (Pearson r > 0.7), with over 99% of consistent facts exhibiting successful entity alignment — providing direct empirical motivation for entity-level rather than sentence-level contrastive objectives. Marco et al. ('Unveiling LLMs', arXiv:2404.03623) further establish that factual knowledge about subject entities concentrates in middle layers (L5-L21 for LLaMA-2-7B). KBioXLM (EMNLP Findings 2023) provides an important precedent: it demonstrated that multi-granularity knowledge alignment (entity masking, relation masking, passage relation prediction) during continued pretraining of XLM-R yields +20 F1 points on cross-lingual zero-shot biomedical tasks, establishing entity-anchored alignment as effective — but using masking-based reconstruction on encoders rather than contrastive loss on decoder LLMs, and targeting downstream task transfer rather than factual conductivity. Ifergan et al. (NAACL Findings 2025) reveal a deeper challenge: using knowledge editing as a probe for representation sharing, they find script similarity is the dominant factor (same-script CKR ~37.6% in Mistral; cross-script <10-20%), and that behavioral consistency diverges sharply from representation sharing for cross-script pairs. Bandarkar et al. (arXiv:2603.17070, March 2026) confirm this with regression analysis showing script match as the primary predictor after controlling for model capability and question difficulty (~13% accuracy gap), but critically, their entity priming experiment shows that providing source-language entity names disproportionately improves cross-script questions — directly implicating entity mapping as the bottleneck. TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers using only 5% of training data on encoders. DaMuEL (2023) provides 12.3B tokens with QID-linked entity annotations across 53 languages, enabling efficient preprocessing for 10 of EACA's 13 target languages. The opportunity is to combine these insights — entity-level anchoring + structured knowledge grounding + middle-layer extraction + inverse-frequency weighting + script-aware strategies — into a contrastive CPT method that targets the specific granularity (entities), representation layer (middle), data regime (low-frequency facts), and script barriers where current methods demonstrably fall short.\n\n## Related Work / Landscape\nThe cross-lingual factual consistency landscape spans several complementary approaches. CCL-XCoT (EMNLP 2025 Findings) is the primary baseline, employing InfoNCE symmetric contrastive loss during continued pretraining with a sentence-to-paragraph curriculum on Gemma-7B and LLaMA-3.1-8B using LoRA on layers 9-19/11-22, reducing hallucination by 62%, but operating at sentence/paragraph granularity without entity grounding or frequency weighting. Liu & Niehues (ACL 2025) represent the closest methodological precedent for contrastive alignment: they apply contrastive loss on mean-pooled sentence representations at middle layers (specifically layer 16 of 32 for LLaMA-3-8B-Instruct) during task-specific fine-tuning with LoRA (rank 8), demonstrating +1.5 F1 on slot filling and +1.5 BLEU on MT across 35 languages — however, they use sentence-level alignment with alternating (not joint) task/alignment training, target downstream task transfer rather than factual consistency, use parallel text rather than structured knowledge, and include no frequency weighting. EACA differentiates from Liu & Niehues on five axes: (1) entity-level rather than sentence-level granularity, (2) continued pretraining for factual consistency rather than task-specific fine-tuning, (3) FactNet-grounded contrastive pairs rather than parallel text, (4) joint NTP+contrastive objective rather than alternating training, and (5) inverse-frequency weighting for underrepresented facts. KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564) is an important precedent for multi-granularity entity-anchored alignment in multilingual pretraining. It performs continued pretraining on XLM-R using three alignment objectives grounded in UMLS biomedical knowledge: entity masking (code-switching entity mentions across EN-CN and predicting masked entity tokens via MLM cross-entropy), relation masking (masking relation tokens in subject-predicate-object triples), and passage relation prediction (3-way classification on aligned EN-CN Wikipedia passages). KBioXLM achieves +20 F1 points on cross-lingual zero-shot biomedical NER/RE. EACA extends this paradigm along four dimensions: (a) decoder-only LLMs vs. encoder (XLM-R), requiring contrastive loss on hidden states rather than masking-based reconstruction, since decoder LLMs lack bidirectional context for effective mask prediction; (b) general domain vs. biomedical, using FactNet's 1.7B facts across 316 editions vs. UMLS's specialized ontology; (c) explicit contrastive alignment (InfoNCE) vs. implicit alignment through masking, directly optimizing cross-lingual entity representation similarity rather than relying on the prediction bottleneck; (d) conductivity metric (CLiKA's XRR) vs. downstream task transfer, targeting the specific capability that prior methods fail to improve. CLiKA (Gao et al., NAACL 2024) provides the diagnostic framework: they define knowledge conductivity as the Cross-Retrieval Ratio (XRR) — retrieving knowledge learned in one language using another — and find that neither multilingual pretraining nor instruction tuning substantially improves XRR (scores < 0.01 for most non-English languages), with no concrete solutions proposed. The entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) provides strong empirical support: cross-lingual consistency correlates with entity alignment at r > 0.7, and their SubInj method yields +14-32% recall and +17-44% consistency gains, but only at inference time; EACA aims to achieve this alignment at training time. On the script barrier dimension, Ifergan et al. ('Beneath the Surface of Consistency', NAACL Findings 2025, arXiv:2408.10646) demonstrate via knowledge editing probes on 7 decoder LLMs (7B scale) that script similarity is the dominant factor in cross-lingual knowledge representation sharing (CKR): same-script Latin pairs show ~37.6% average CKR in Mistral, while cross-script pairs show <10-20% transfer; crucially, they find that high behavioral consistency (CKC) does not imply shared representation for cross-script pairs, with E[NCL] consistently exceeding E[NTL]. Even targeted language extension pretraining achieves only marginal cross-script CKR improvement. Bandarkar et al. ('Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts', arXiv:2603.17070, March 2026) confirm via regression analysis on ECLeKTic and MultiLoKo that script match — not language family — is the primary predictor of knowledge transfer failure (~13% accuracy gap), but their entity priming experiment reveals that providing source-language entity names disproportionately improves cross-script questions, directly implicating entity mapping as the cross-script bottleneck. TransliCo (Liu et al., ACL 2024, arXiv:2401.06620) addresses script barriers through transliteration contrastive modeling (TCM), fine-tuning Glot500-m on 5% of data with Latin transliterations as contrastive targets, producing Furina which outperforms Glot500-m on cross-script zero-shot transfer — but operates on encoders at sentence level without entity grounding. Transliteration-based post-training alignment (Moosa et al., EMNLP Findings 2024, arXiv:2406.19759) achieves up to 50% improvement on cross-script English-centric transfer with even larger gains for non-English sources. EACA incorporates this insight by adding transliteration-augmented entity contrastive pairs for cross-script language combinations as a complementary mechanism. NeighXLM (EMNLP 2025 Findings) introduces neighbor-augmented contrastive pretraining for low-resource languages without parallel data, but targets general cross-lingual transfer rather than entity-specific factual consistency. PreAlign (EMNLP 2024) uses code-switching pretraining with word-level alignment but lacks entity anchoring. CrossIC-PT (EMNLP 2025) interleaves bilingual Wikipedia content without entity-level grounding. LEIA (ACL Findings 2024) inserts English entity names with [translate]/[/translate] markers during continued pretraining of decoder LLMs, improving cross-lingual transfer but without contrastive loss or frequency weighting. EntityCS (EMNLP Findings 2022) performs entity-centric code switching with Wikidata but is limited to encoder-only models. Entity Lens (BlackboxNLP 2025) reveals that decoder LLMs develop entity-specific mechanisms to represent and manipulate multi-token entities via task vectors. The middle-layer factual knowledge claim is supported by Liu & Niehues (ACL 2025) showing layer 16 of 32 has strongest cross-lingual retrieval alignment, and Marco et al. (arXiv:2404.03623) demonstrating via dynamic knowledge graphs that middle layers (L5-L21) encode comprehensive factual knowledge while late layers show 90%+ degradation. ELO (arXiv:2601.03648, Jan 2026) demonstrates efficient layer-specific optimization with 6.46x speedup from selective middle-layer updates. FactNet (arXiv:2602.03417) provides 1.7B entity-grounded facts across 316 Wikipedia editions with significant coverage skew. CLM-Bench (arXiv:2601.17397) shows edit vectors are nearly orthogonal across languages, further motivating entity-level alignment. DCO (arXiv:2603.04678, March 2026) proposes DPO-inspired post-hoc consistency optimization, complementary to pretraining-time methods. Veitsman et al. (arXiv:2603.18863, March 2026) find that sentence-level contrastive alignment fails for token-level tasks in XLM-R encoders, supporting entity-level approaches for entity-centric tasks. Cultural knowledge asymmetry research (ACL 2025) confirms that frequency drives cross-lingual transferability.\n\n## Approach\nEACA adds an InfoNCE contrastive loss on entity-span hidden states to the standard next-token prediction (NTP) objective during continued pretraining. The method comprises five integrated components: entity preprocessing, entity-level contrastive alignment, script-aware augmentation, stratified batch construction, and joint optimization with gradient monitoring.\n\n**1. Entity Preprocessing Pipeline.** Entity boundary annotation uses a two-stage pipeline. Stage 1 (primary): DaMuEL (2023), which provides 12.3B QID-annotated tokens across 53 languages (CC BY-SA), is used directly for the 10 target languages it covers (EN/ZH/JA/DE/AR/HI/TR/ID/VI/TH). DaMuEL provides start/end token indices per entity mention with Wikidata QID links, extracted from Wikipedia wikilinks and expanded via lemmatization and alias matching (~17% recall gain over raw wikilinks). Stage 2 (Tier 3 gap-filling): For the 3 Tier 3 languages not covered by DaMuEL (SW/YO/KM), a lightweight Wikipedia wikilinks extraction pipeline resolves hyperlinks to QIDs via Wikidata sitelinks (~50-60% mention coverage). mReFinED (EMNLP Findings 2023), which is 44-60x faster than comparable entity linkers, is applied as a second pass on high-resource languages to annotate non-hyperlinked entity mentions where higher recall is needed. Entity boundaries are marked with LEIA-style [ENT]/[/ENT] tokens around linked mentions. Preprocessing budget: 1.5-2 weeks engineering time, ~2-4 GPU-days on A100 for mReFinED gap-filling, ~24-48 CPU-hours for wikilinks extraction across Tier 3 languages. This pipeline is on the critical path and must complete before Phase 0.\n\n**2. Entity-Level Contrastive Alignment.** Entity representations are extracted via mean-pooling over hidden states within the [ENT]...[/ENT] span at a designated middle layer (defaulting to layer 16 for 32-layer models based on Liu & Niehues' ACL 2025 finding and Marco et al.'s analysis; validated via Phase 0 sweep over layers 12-20), with loss propagation blocked on boundary markers themselves. Contrastive pairs are constructed per QID from FactNet: positive pairs consist of atomic fact descriptions for the same QID across languages, while negatives come from different QIDs within the same batch (detailed in Component 4). Inverse-frequency weighting assigns higher contrastive loss weight to facts with lower cross-lingual FactNet coverage, directly targeting low-resource facts where CLiKA's conductivity analysis shows the largest gap.\n\nTheoretical motivation for entity-level granularity: Three converging lines of evidence support entity-level over sentence-level contrastive alignment for factual consistency: (1) Entity alignment analysis (arXiv:2510.10280) demonstrates Pearson r > 0.7 between entity alignment and cross-lingual consistency, with >99% of consistent facts showing successful entity alignment — establishing entities as the bottleneck for consistency; (2) CLM-Bench's finding that cross-lingual edit vectors are nearly orthogonal implies that factual knowledge editing, which operates at entity-level (subject-property-object triples), requires entity-aligned representations rather than sentence-aligned ones; (3) CLiKA's failure result — that sentence/document-level pretraining and instruction tuning do not improve conductivity — suggests that coarser-grained alignment conflates entity-specific factual knowledge with syntactic and discourse-level variation, diluting the alignment signal.\n\n**3. Script Barrier Mitigation.** EACA's 13 target languages span ~7 scripts (Latin: EN/DE/TR/ID/VI/SW/YO; CJK: ZH/JA; Arabic: AR; Devanagari: HI; Thai: TH; Khmer: KM). Ifergan et al. (NAACL Findings 2025) demonstrate that cross-lingual representation sharing (CKR) clusters strongly by script family (~37.6% same-script CKR vs. <10-20% cross-script in Mistral-7B), and Bandarkar et al. (arXiv:2603.17070) confirm script match as the primary predictor of transfer failure (~13% gap). This poses a genuine risk that entity-level contrastive alignment may primarily improve same-script entity alignment while showing limited gains for cross-script pairs. However, two findings provide grounds for cautious optimism: (a) Bandarkar et al.'s entity priming experiment shows source-language entity names disproportionately improve cross-script transfer, implicating entity mapping — not script-level representation — as the cross-script bottleneck for factual knowledge; (b) TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers on encoders using only 5% of training data. EACA therefore incorporates a script-aware augmentation strategy: for cross-script QID pairs (e.g., EN-ZH, EN-AR, EN-HI, EN-TH, EN-KM), entity mentions in non-Latin scripts are supplemented with Latin transliterations appended within the [ENT] boundary (e.g., [ENT]北京 (Beijing)[/ENT]), providing a lexical bridge for the contrastive objective. This is tested as an ablation (EACA vs. EACA+translit) to isolate the contribution of transliteration augmentation beyond entity-level alignment. The evaluation plan includes mandatory script-grouped analysis: same-script entity alignment gains (Latin-Latin, CJK-CJK) vs. cross-script gains (Latin-CJK, Latin-Arabic, Latin-Devanagari, etc.), reporting both entity cosine similarity and downstream factual consistency metrics separately for each script-pair category. If Phase 0 reveals that cross-script entity alignment gains are <50% of same-script gains despite transliteration augmentation, this will be explicitly reported as a limitation and the analysis will quantify what fraction of EACA's overall conductivity improvement comes from same-script vs. cross-script alignment.\n\n**4. Stratified Batch Construction with Type-Aware Hard Negatives.** Effective contrastive learning is highly sensitive to negative quality (Robinson et al., ICLR 2021). EACA uses stratified mini-batching: each batch contains K_batch = 128-256 unique QIDs, with all available language instances per QID forming the positive set (asymmetric positive sets accommodate QIDs present in only 2-3 languages without dropping them). Minimum language coverage per QID is K_min = 3 languages; QIDs with fewer than 3 language instances are filtered during preprocessing. Class-Aware Masking (CAM) ensures that all instances of the same QID are excluded from the InfoNCE denominator, preventing false-negative contamination. For hard negative mining, type-aware stratification ensures ~50% of in-batch negatives share the anchor entity's Wikidata type (e.g., Q5/human, Q515/city, Q4830453/organization) — forcing the model to discriminate on fine-grained entity identity rather than coarse type. This is implemented via Wikidata instance-of (P31) properties, grouping entities into 8-10 macro-types for sampling. The remaining ~50% are random negatives for diversity. Batch composition is balanced across script families to ensure cross-script contrastive signals appear in every batch. The InfoNCE loss for entity e with QID q is: L_entity(q) = -log[exp(sim(h_q^i, h_q^j)/τ) / (exp(sim(h_q^i, h_q^j)/τ) + Σ_{k≠q} exp(sim(h_q^i, h_k)/τ))], where h_q^i, h_q^j are entity representations from different languages for the same QID, and h_k are representations from different QIDs, with τ = 0.07 as the temperature (tuned in Phase 0 over {0.05, 0.07, 0.1}).\n\n**5. Joint Optimization with Gradient Monitoring.** The joint objective is L_total = L_NTP + λ * L_entity_contrastive, with λ initialized at 0.1 (following guidance from headless LM work showing λ ∈ [0.01, 0.1] is appropriate for contrastive + generation joint training during CPT). A potential tension exists: NTP learns language-specific token distributions while contrastive loss pulls entity representations together across languages. Unlike Liu & Niehues' alternating approach, EACA uses joint optimization to ensure entity alignment co-adapts with the language modeling objective — but addresses gradient conflict risk through three mechanisms: (a) Phase 0 gradient analysis: cosine similarity between ∇L_NTP and ∇L_entity_contrastive is computed every 100 steps on the shared LoRA parameters. If gradient cosine similarity is negative for >30% of monitored steps, PCGrad projection (Yu et al., NeurIPS 2020) is applied — projecting the contrastive gradient onto the normal plane of the NTP gradient to eliminate destructive interference. (b) GradNorm (Chen et al., ICML 2018) is implemented as an optional dynamic λ adjustment mechanism: if the gradient magnitude ratio between the two losses drifts beyond 10:1, GradNorm normalizes to equalize learning rates. (c) λ warmup: contrastive loss weight ramps linearly from 0 to λ_target over the first 10% of training steps, allowing NTP to stabilize before contrastive pressure is introduced. Phase 0 reports gradient conflict frequency, cosine similarity distribution, and whether PCGrad/GradNorm activation was required — this informs the full training configuration. If gradient conflicts are severe (>50% of steps) even with PCGrad, the fallback is alternating optimization (NTP steps → contrastive steps per batch) following Liu & Niehues' validated approach.\n\nCatastrophic forgetting is mitigated through three mechanisms: (a) LoRA (rank 64) applied to middle layers only (layers 10-22), following CCL-XCoT's selective layer approach and ELO's findings that first/last layers are critical for general capabilities; (b) 15% general-domain English replay data mixed into training batches; (c) cosine learning rate schedule with linear warmup (peak LR 2e-5). Language selection follows a tiered strategy: Tier 1 comprises 4 anchor languages (EN/ZH/JA/DE, >1M entity-fact pairs), Tier 2 includes 6 mid-resource languages (AR/HI/TR/ID/VI/TH, 100K-1M pairs), and Tier 3 covers 3 low-resource languages (SW/YO/KM). Tier 3 viability assessment based on Wikipedia article counts (SW: ~117K, YO: ~37K, KM: ~12K) and FactNet's 0.36 low-resource yield rate estimates approximately 50K-200K entity-fact pairs for Swahili, 15K-60K for Yoruba, and 5K-25K for Khmer. None of the Tier 3 languages are covered by DaMuEL, so all three rely on the Wikipedia wikilinks extraction pipeline (Stage 2 above). A mandatory FactNet coverage audit in Phase 0 will report exact entity-fact pair counts for all 13 languages; minimum viable threshold is set at 10K entity-fact pairs per language (sufficient for contrastive batching at size 128-256 with adequate negative diversity). If any Tier 3 language falls below threshold, contingency replacements include Bengali (BN, ~157K Wikipedia articles), Tagalog (TL, ~115K articles), or Hausa (HA, ~8K articles but stronger NLP benchmark coverage). Languages below 25K pairs receive LEIA-style English entity augmentation to supplement contrastive pairs.\n\nPhase 0 pilot uses 500M tokens across 5 languages (3 Tier-1 + 2 Tier-2, selected to span at least 3 scripts for script barrier analysis) for approximately 130 H100 hours, with baselines including: (a) CCL-XCoT-style sentence-level contrastive CPT, (b) Liu & Niehues-style middle-layer sentence-level contrastive alignment (the closest methodological comparison, testing entity-level vs. sentence-level at the same middle layer), (c) LEIA-style entity augmentation without contrastive loss, (d) standard CPT, and (e) KBioXLM-style entity masking adaptation (masking [ENT]-bounded tokens and predicting via NTP, without contrastive loss — testing contrastive vs. masking-based entity alignment on decoders). Phase 0 additionally includes: a layer sweep (layers 12, 14, 16, 18, 20) to empirically determine optimal entity extraction depth; gradient conflict analysis (cosine similarity monitoring, PCGrad activation rate); and script-grouped entity alignment analysis (same-script vs. cross-script gains). Go/no-go criteria require entity cosine similarity improvement of at least 0.05, BMLAMA-53 consistency improvement of at least 2 points, no TyDiQA degradation beyond 1 point, AND gradient conflict rate below 50% (with or without PCGrad). Full training processes 1.5-2.5B tokens on LLaMA-3.1-8B (primary) and Gemma-7B (secondary, for CCL-XCoT comparability) across all 13 languages. A complementary EACA+DCO experiment tests whether pretraining-time and post-hoc consistency methods yield cumulative gains. Evaluation covers BMLAMA-53, TyDiQA-GoldP, X-CODAH, LiveCLKTBench, and CLiKA's XRR metric (to directly measure conductivity improvement), plus entity representation cosine similarity analysis. All metrics are reported with script-grouped breakdowns (same-script pairs, cross-script pairs, overall) as a mandatory analysis dimension. Ablations cover: entity-level vs. sentence-level contrastive (the central hypothesis), contrastive vs. masking-based entity alignment (EACA vs. KBioXLM-style adaptation), EACA vs. EACA+transliteration augmentation (script barrier mitigation), frequency weighting on/off, type-aware vs. random negatives, number of languages, layer selection, joint vs. alternating training, gradient conflict mitigation (none vs. PCGrad vs. GradNorm), contrastive pair construction (FactNet-grounded vs. parallel-text-based), and K_min language threshold (2 vs. 3 vs. 5).\n\n## Inspiration\nCCL-XCoT contrastive CPT framework (EMNLP 2025 Findings) + Liu & Niehues middle-layer contrastive alignment (ACL 2025) + FactNet entity-grounded facts (arXiv:2602.03417) + LEIA entity boundary markers (ACL 2024) + CLiKA conductivity diagnostic (NAACL 2024) + Entity-level alignment in crosslingual consistency (arXiv:2510.10280) + Entity Lens entity-specific mechanisms (BlackboxNLP 2025) + Marco et al. middle-layer factual knowledge (arXiv:2404.03623) + ELO selective layer optimization (arXiv:2601.03648) + Liu et al. frequency-driven transfer (EMNLP 2025) + CLM-Bench orthogonal edit vectors (arXiv:2601.17397) + cultural knowledge asymmetry frequency hypothesis (ACL 2025) + Ifergan et al. script-CKR dominance (NAACL Findings 2025) + Bandarkar et al. script barrier in reasoning models (arXiv:2603.17070) + TransliCo transliteration-contrastive script bridging (ACL 2024) + KBioXLM multi-granularity entity alignment (EMNLP Findings 2023) + DaMuEL QID-annotated corpus (2023) + Robinson et al. hard negative mining (ICLR 2021) + PCGrad gradient surgery (NeurIPS 2020) + GradNorm dynamic loss weighting (ICML 2018)\n\n## Key References\n- CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation (EMNLP Findings 2025)\n- Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs [Liu & Niehues] (ACL 2025, arXiv:2502.14830)\n- Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly [CLiKA] (NAACL 2024, arXiv:2404.04659)\n- On the Entity-Level Alignment in Crosslingual Consistency [Liu, Wang et al.] (arXiv:2510.10280)\n- FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding (arXiv 2026)\n- LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation (ACL Findings 2024)\n- On the Representations of Entities in Auto-regressive Large Language Models [Entity Lens] (BlackboxNLP 2025, arXiv:2510.09421)\n- Unveiling LLMs: The Evolution of Latent Representations in a Dynamic Knowledge Graph [Marco et al.] (arXiv:2404.03623)\n- Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs [Ifergan et al.] (NAACL Findings 2025, arXiv:2408.10646)\n- Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts [Bandarkar et al.] (arXiv:2603.17070, March 2026)\n- TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models (ACL 2024, arXiv:2401.06620)\n- Breaking the Script Barrier in Multilingual Pre-Trained Language Models with Transliteration-Based Post-Training Alignment [Moosa et al.] (EMNLP Findings 2024, arXiv:2406.19759)\n- KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model [Geng et al.] (EMNLP Findings 2023, arXiv:2311.11564)\n- DaMuEL: A Large Multilingual Dataset for Entity Linking (arXiv:2306.09288, 2023)\n- Contrastive Learning with Hard Negative Samples [Robinson et al.] (ICLR 2021)\n- Gradient Surgery for Multi-Task Learning [PCGrad, Yu et al.] (NeurIPS 2020)\n- GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks [Chen et al.] (ICML 2018)\n- mReFinED: An Efficient End-to-End Multilingual Entity Linking Model (EMNLP Findings 2023)\n- NeighXLM: Enhancing Cross-Lingual Transfer in Low-Resource Languages via Neighbor-Augmented Contrastive Pretraining (EMNLP Findings 2025)\n- mLUKE: The Power of Entity Representations in Multilingual Pretrained Language Models (ACL 2022)\n- ELO: Efficient Layer-Specific Optimization for Continual Pretraining of Multilingual LLMs (arXiv 2026)\n- Tracing Multilingual Factual Knowledge Acquisition in Pretraining (EMNLP Findings 2025)\n- PreAlign: Boosting Cross-Lingual Transfer by Early Establishment of Multilingual Alignment (EMNLP 2024)\n- Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training [CrossIC-PT] (EMNLP 2025)\n- Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025)\n- EntityCS: Improving Zero-Shot Cross-lingual Transfer with Entity-Centric Code Switching (EMNLP Findings 2022)\n- Optimizing Language Models for Crosslingual Knowledge Consistency [DCO] (arXiv 2026)\n- Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models [BMLAMA] (EMNLP 2023)\n- LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs (arXiv 2025)\n- Why Better Cross-Lingual Alignment Fails for Better Cross-Lingual Transfer: Case of Encoders [Veitsman et al.] (arXiv 2026)\n- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026)\n- DoLa: Decoding by Contrasting Layers Improves Factuality and Faithfulness of Large Language Models (ICLR 2024)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '1100-1550 H100 (Preprocessing: ~10-15 GPU-days A100 for mReFinED; Phase 0: ~130 including layer sweep + gradient analysis; Full training: ~800-1100; Evaluation: ~70; Ablations: ~90-165 including script/masking/gradient ablations)', 'timeline': '4.5-5.5 months (includes 1.5-2 weeks preprocessing pipeline)', 'estimated_gpu_cost': '$2,200-3,100 (at ~$2/H100-hr spot)'}\n- **human_in_loop**: {'gpu_hours': '900-1250 H100', 'timeline': '3.5-4.5 months', 'claude_api_cost': '$300-450 (FactNet coverage audit, DaMuEL integration, preprocessing pipeline, gradient analysis visualization, evaluation analysis, paper drafting)', 'estimated_gpu_cost': '$1,800-2,500'}\n- **auto_research**: {'gpu_hours': '1100-1600 H100', 'timeline': '3-4 months', 'claude_api_cost': '$600-950 (full pipeline automation: DaMuEL integration + mReFinED gap-filling + Tier 3 wikilinks pipeline + FactNet coverage audit + Tier 3 viability check, entity marker insertion, layer sweep, gradient analysis, hyperparameter sweep, script-grouped analysis, ablation analysis, paper writing)', 'estimated_gpu_cost': '$2,200-3,200', 'speed_bottleneck': 'Preprocessing pipeline (1.5-2 weeks) is on critical path before Phase 0; Phase 0 pilot (2-3 weeks including layer sweep, gradient analysis, and script-grouped evaluation) must complete before full training; full training wallclock ~30-50 hours per run on 8xH100; sequential dependency: preprocessing → FactNet audit gates Tier 3 language selection → pilot go/no-go gates full training'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T18:59:26.912Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:59:26.912Z",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T18:59:26.923Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- CLiKA: "Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly" (NAACL 2024, arXiv:2404.04659): 定义了 Cross-Retrieval Ratio (XRR) 度量 conductivity，发现所有测试 LLM 的 XRR < 0.01，多语言预训练和指令微调均无法实质性提升 conductivity。这是 proposal 的核心动机，已验证为真实存在的论文和发现。
- CCL-XCoT (EMNLP Findings 2025, arXiv:2507.14239): 句子/段落粒度的对比学习 CPT，在 Gemma-7B 和 LLaMA-3.1-8B 上将跨语言幻觉降低 62%。使用课程化对比学习 + NTP，是最直接的句子级 baseline。该论文真实存在，但发表时间需注意——arXiv 为 2025 年 7 月，作为 EMNLP 2025 Findings 发表。
- Liu & Niehues (ACL 2025, arXiv:2502.14830): 中间层（layer 16/32）句子级对比对齐，用于任务特定微调，在 slot filling 上 +1.5 F1，MT 上 +1.5 BLEU。验证了中间层是跨语言对齐的最佳位置，但仅在句子粒度和下游任务迁移。真实论文，ACL 2025 已发表。
- "On the Entity-Level Alignment in Crosslingual Consistency" (arXiv:2510.10280): 发现实体对齐与跨语言一致性的 Pearson r > 0.7，>99% 一致的事实展示成功的实体对齐。提出 SubInj 方法（推理时插入英文实体名）获得 +14-32% recall 和 +17-44% 一致性提升。**关键竞争者**：此推理时方法已经取得了显著效果。
- KBioXLM (EMNLP Findings 2023, arXiv:2311.11564): 在 XLM-R（encoder）上使用多粒度知识对齐（实体掩码、关系掩码、段落关系预测）进行 CPT，在跨语言零样本生物医学任务上 +20 F1。真实论文，但限于 encoder + 生物医学领域。
- FactNet (arXiv:2602.03417, Feb 2026): 1.7B 实体锚定原子事实，316 个 Wikipedia 版本，Wikidata QID 链接，92.1% 精度。已在 arXiv 发布，GitHub 存在。是 EACA 的核心数据资源。
- TransliCo (ACL 2024, arXiv:2401.06620): 在 encoder (Glot500-m) 上使用音译对比学习，5% 数据即可桥接脚本障碍。ACL 2024 真实论文。
- DaMuEL (arXiv:2306.09288, 2023): 12.3B QID 标注 tokens，53 语言。真实数据集，CC BY-SA 许可。
- Bandarkar et al. (arXiv:2603.17070, March 2026): 确认 script match 是知识迁移的主要预测因子（~13% gap），关键的 entity priming 实验显示提供源语言实体名可不成比例地改善跨脚本迁移。真实 arXiv 论文。
- Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646): 通过知识编辑探针发现 script similarity 主导跨语言知识表征共享（同脚本 CKR ~37.6% vs. 跨脚本 <10-20%）。真实论文。
- LEIA (ACL Findings 2024, arXiv:2402.11485): 在 decoder LLM CPT 中插入英文实体名（[translate]/[/translate] 标记），无对比损失，改善跨语言迁移。**关键 trivial alternative 候选者**。
- EntityCS (EMNLP Findings 2022): 实体级代码切换，但限于 encoder。
- Entity Lens (BlackboxNLP 2025, arXiv:2510.09421): decoder LLM 发展出实体特定机制来表征多 token 实体。

- **调研总结**: 跨语言事实一致性领域正处于快速发展期。CLiKA 揭示的 conductivity gap（XRR < 0.01）是一个公认的未解决问题。现有方法沿两条路线发展：(1) 句子/段落级对比 CPT（CCL-XCoT, Liu & Niehues），在下游任务和幻觉上有效但未解决实体级 conductivity；(2) 推理时实体增强（SubInj, LEIA 式方法），有效但不改变模型内部表征。EACA 提出的"实体级对比 CPT"位于两条路线的交汇点，但这个交汇点目前确实没有被已有工作直接占据。

【Trivial Alternative 检验】:
存在两个需要认真对待的 trivial alternative：

1. **SubInj（推理时实体增强）**：arXiv:2510.10280 的 SubInj 方法仅在推理时将英文实体名注入提示，就获得 +14-32% recall 和 +17-44% 一致性提升。这是零训练成本的方法。EACA 需要 1100-1600 H100 小时和 4-5 个月工程时间——如果最终效果与 SubInj 相当或仅小幅优于 SubInj，成本效益比极差。EACA 的增量价值论述是：训练时对齐改变模型内部表征，应该比推理时 prompt engineering 更根本、更泛化（不依赖于特定 prompt 格式）。这个论述逻辑上成立，但需要实验验证。

2. **LEIA + CCL-XCoT 组合**：LEIA 已经在 CPT 中使用实体标记增强，CCL-XCoT 已经在 CPT 中使用对比学习。一个直接的 baseline 是将 LEIA 的实体标记与 CCL-XCoT 的句子级对比损失简单组合。如果这个简单组合已经能获得大部分收益，EACA 的"实体级对比对齐"的边际贡献就会被压缩。Proposal 意识到了 LEIA 作为 baseline 的存在（Phase 0 包含了 LEIA augmentation baseline），但没有明确讨论 "LEIA + 句子级对比" 这个组合 baseline 的威胁。

**增量价值判断**：EACA 的真正增量在于将对比信号从句子级降到实体级并用结构化知识（FactNet QID）锚定正样本对。理论动机有据（r > 0.7 相关性，CLiKA 的 failure result），但这个增量是否大到足以 justify 系统复杂度，是实验需要回答的核心问题。Trivial alternative 威胁等级：**中等偏高**。

【前提假设检验】:
核心 claim 的逻辑链条：
1. ✅ CLiKA 表明现有方法无法提升 conductivity（XRR < 0.01）→ **有实证支持**
2. ✅ 实体对齐与跨语言一致性强相关（r > 0.7）→ **有实证支持**（arXiv:2510.10280）
3. ⚠️ **"句子级对比之所以不改善 conductivity，是因为粒度太粗，conflating entity-specific knowledge with syntactic variation"** → **这是未经验证的假设**。CLiKA 测试的是标准多语言预训练和指令微调，CCL-XCoT 的句子级对比确实降低了幻觉 62%，但其对 CLiKA 的 XRR 指标的影响未知。Proposal 假设句子级对比无法改善 XRR，但这并未被实验验证——CCL-XCoT 论文没有报告 XRR 指标。
4. ⚠️ **"实体级对比对齐可以改善模型内部表征，而非仅仅是推理时效果"** → **合理但未验证**。SubInj 的成功表明实体对齐是瓶颈，但 SubInj 是推理时的，EACA 假设训练时对比学习可以将这种对齐内化到模型表征中。虽然这在理论上合理（对比学习改变表征空间是有先例的），但在 decoder LLM 的 CPT 阶段使用实体级 InfoNCE 是否能有效改变中间层表征，以及是否比 NTP 自然学习的表征更好，并无先例。
5. ⚠️ **"在 decoder LLM 上的实体级对比损失不会严重干扰自回归语言建模能力"** → 这是一个工程假设，有 CCL-XCoT 的句子级先例支持，但实体级对比（每个 batch 128-256 个 QID 的正/负样本对）的梯度动态与句子级可能不同。Proposal 通过 PCGrad 和 GradNorm 设计了缓解机制，但这本身就暗示了风险。

**最关键的未验证假设**：第 3 点——"句子级对比之所以失败是因为粒度问题"。如果句子级对比实际上也能改善 XRR（只是没人测过），那 EACA 的核心动机就被削弱。

【3 维度打分】:

1. **Novelty: 中** — 
   EACA 的核心贡献是将对比 CPT 的粒度从句子级降至实体级，并用结构化知识图谱（FactNet QID）锚定对比对。这个组合在已有工作中确实不存在：CCL-XCoT 是句子级对比 CPT（EMNLP 2025 Findings），Liu & Niehues 是句子级中间层对比微调（ACL 2025），KBioXLM 是 encoder 上的实体掩码（EMNLP 2023 Findings），LEIA 是实体增强 CPT 无对比损失（ACL 2024 Findings），TransliCo 是 encoder 上的音译对比（ACL 2024）。EACA 位于这些工作的交叉点，这个特定的组合点确实是空白的。然而，novelty 主要来自"组合"而非"新概念"——每个组件（实体标记、对比损失、中间层提取、知识图谱锚定、音译增强、梯度冲突监控）都有明确的来源。对于审稿人来说，问题在于这是"principled synthesis"还是"incremental combination"——这很大程度上取决于实验结果是否显著超越各组件的简单组合。此外，arXiv:2510.10280 已经建立了"实体对齐 → 一致性"的强相关性，使得 EACA 的方向几乎是"显而易见的下一步"，降低了 surprise factor。

2. **Significance: 中偏强** — 
   研究问题（跨语言知识 conductivity）是领域内公认的重要问题。CLiKA (NAACL 2024) 明确表明所有现有方法在 XRR 指标上几乎为零，这是一个 well-documented failure。如果 EACA 能够实质性提升 XRR（即便是从 <0.01 提升到 0.05-0.1），这将是一个有影响力的结果，因为它回答了一个目前无解的问题。此外，脚本障碍问题（Ifergan et al. NAACL 2025; Bandarkar et al. 2026）是多语言 NLP 的持久挑战，EACA 对此的针对性处理（音译增强 + 脚本分组评估）增加了实用价值。但 significance 受限于：(a) 实际应用场景——conductivity 改善对终端用户的实际影响尚不清楚；(b) 仅在 8B 模型上验证，scaling behavior 未知；(c) 如果效果仅在 same-script 上显著而 cross-script 改善有限（考虑到脚本障碍的严重性），影响力会打折。

3. **Related Work: 强** — 
   这是 proposal 最强的维度。覆盖范围极为全面：从诊断框架（CLiKA）、对比 CPT（CCL-XCoT）、中间层对齐（Liu & Niehues）、实体级先例（KBioXLM、LEIA、EntityCS）、实体表征分析（Entity Lens、Marco et al.）、脚本障碍（Ifergan et al.、Bandarkar et al.、TransliCo）到数据资源（FactNet、DaMuEL），几乎无遗漏。差异化定位清晰——对 CCL-XCoT 有 5 轴差异分析，对 Liu & Niehues 有详细的粒度/目标/数据比较，对 KBioXLM 有 4 维度扩展论述。所有我能搜到的关键引用都被准确引用和描述。唯一的轻微不足是未讨论"LEIA + 句子级对比"这个组合 baseline 的威胁。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty 为中是主要限制因素。idea 的核心洞见（"实体级对齐是 conductivity 的瓶颈，应该用实体级对比学习来解决"）是被现有证据（r > 0.7 相关性）高度预测的"下一步"，而不是反直觉的发现。审稿人很可能会说"the motivation is sound, but the contribution is primarily the engineering effort of putting known pieces together"。Significance 中偏强——问题确实重要且 well-documented，但受制于 trivial alternative 威胁（SubInj 推理时已获得显著效果）。Related Work 强——但相关工作的完备性不能提升 idea 本身的 novelty 天花板。概率上界（35%）需要实验结果显著超越所有 trivial alternatives + 在 cross-script 上也有明显效果；下界（25%）对应审稿人认定为 incremental combination 的情况。注意：如果目标会议确实是 CoRL（Conference on Robot Learning），此 proposal 完全 off-topic，概率接近 0%——此处按 NLP/CL 顶会估计。

【主要风险】: 
1. **"Principled engineering" vs. "new idea" 的审稿认知风险**：每个组件都有明确来源，核心假设（实体级 > 句子级）几乎是 arXiv:2510.10280 相关性结果的直接推论。审稿人可能认为这是"well-executed combination"而非"novel contribution"，在 novelty 维度给出 borderline reject。
2. **Trivial alternative 的实验失败风险**：如果 SubInj（零训练成本的推理时方法）或 "LEIA + CCL-XCoT" 简单组合在 XRR 指标上与 EACA 效果相当，则 EACA 的 1100+ H100 小时投入和复杂 pipeline 难以 justify。这不是 idea 本身的缺陷，但它意味着 idea 的成功高度依赖于实验 delta 的大小。
```

Sources:
- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)
- [CCL-XCoT - EMNLP Findings 2025](https://arxiv.org/abs/2507.14239)
- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)
- [Entity-Level Alignment in Crosslingual Consistency](https://arxiv.org/abs/2510.10280)
- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)
- [FactNet - arXiv 2026](https://arxiv.org/abs/2602.03417)
- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)
- [DaMuEL](https://arxiv.org/abs/2306.09288)
- [Bandarkar et al. - Script Barrier](https://arxiv.org/abs/2603.17070)
- [LEIA - ACL Findings 2024](https://aclanthology.org/2024.findings-acl.419/)
- [Ifergan et al. - NAACL Findings 2025](https://arxiv.org/abs/2408.10646)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research material. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. CLiKA (Gao et al., NAACL 2024, arXiv:2404.04659):
   定义了 cross-lingual knowledge conductivity 的 XRR 指标，发现即使经过多语言预训练和指令微调，XRR < 0.01，conductivity 几乎未被改善。这是本 proposal 所针对的核心 gap，论文真实存在，描述准确。

2. CCL-XCoT (EMNLP 2025 Findings, arXiv:2507.14239):
   句子/段落级对比学习 CPT，在 Gemma-7B 和 LLaMA-3.1-8B 上将跨语言幻觉减少最多 62%。是本 proposal 的主要 baseline。论文真实，描述准确。

3. Liu & Niehues (ACL 2025, arXiv:2502.14830):
   在 LLaMA-3-8B 的 layer 16 进行句子级中间层对比对齐，slot filling +1.5 F1，MT +1.5 BLEU。论文真实，描述准确。注意：该工作目标是 task-specific fine-tuning 的跨语言迁移，而非 factual conductivity。

4. On the Entity-Level Alignment in Crosslingual Consistency (Liu, Wang et al., arXiv:2510.10280, Oct 2025):
   发现 entity alignment 与 cross-lingual consistency 的 Pearson r > 0.7，>99% 的一致事实展现成功的实体对齐。**关键**：提出 SubInj 方法——在推理时注入英语实体翻译——即可获得 +14-32% recall 和 +17-44% consistency 提升，无需任何训练修改。论文真实。

5. FactNet (arXiv:2602.03417, Feb 2026):
   1.7B 实体锚定原子事实，覆盖 316 个 Wikipedia 版本，grounding precision 92.1%。论文真实，描述准确。

6. Bandarkar et al. (arXiv:2603.17070, Mar 2026):
   script match 是知识迁移失败的首要预测因素（~13% accuracy gap），entity priming 不成比例地改善跨脚本迁移。论文真实，描述准确。

7. Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646):
   same-script CKR ~37.6% vs. cross-script <10-20%。论文真实，描述准确。

8. KBioXLM (EMNLP Findings 2023, arXiv:2311.11564):
   在 XLM-R encoder 上用 masking-based 多粒度实体对齐，生物医学领域 +10+ F1。论文真实，描述准确。

9. DCO (arXiv:2603.04678, Mar 2026):
   DPO-inspired 后训练一致性优化方法，在 26 种语言上显著提升跨语言一致性。这是一种后处理方法，与 EACA 的预训练时方法互补。论文真实。

10. TransliCo (ACL 2024, arXiv:2401.06620):
    音译对比学习框架，仅用 5% 数据在 encoder 模型上桥接脚本障碍。论文真实。

- **调研总结**: Cross-lingual factual consistency/conductivity 是一个活跃但尚未解决的研究方向。CLiKA 建立了诊断框架并揭示了 gap，CCL-XCoT 在句子级取得了进展，Liu et al. (arXiv:2510.10280) 从分析角度证明了实体对齐的重要性，DCO 提供了后训练解决方案。**尚无已发表工作将 entity-level contrastive alignment 应用于 decoder-only LLM 的 CPT 以专门解决 conductivity**——但这是因为 (a) 这是现有技术的自然组合，(b) SubInj 等推理时方法已经部分填补了这个 gap 且成本极低。EACA 处于"自然下一步"的位置：方向合理但不出人意料。


【Trivial Alternative 检验】:

**存在严重的 trivial alternative 威胁。**

最直接的竞争者是 **SubInj/SubSub**（arXiv:2510.10280）：仅在推理时将英语实体名注入 prompt，即可获得 +14-32% recall 和 +17-44% consistency 提升，**零训练成本**。EACA 需要 1100-1600 H100-hours 的训练来达成一个在推理时就能部分实现的目标。

EACA 的增量价值论点是：
1. 推理时方法每次推理都需要实体链接 + 注入，增加延迟；训练时对齐是"一劳永逸"的
2. 推理时方法依赖外部实体链接器的可用性和准确性
3. 训练时对齐可能改变模型内部表征，从而在 SubInj 无法覆盖的场景（如开放生成、长文本推理）中也起作用

但这些增量价值论点 *尚未被验证*。审稿人几乎一定会问："为什么不直接用 SubInj？如果 EACA 的提升与 SubInj 可比甚至不如，这 1000+ GPU-hours 的投入是否正当？" Proposal 需要一个 **EACA vs. SubInj** 的直接对比（或 EACA + SubInj 是否叠加），目前缺失。

此外，**LEIA + NTP-only CPT**（用 FactNet 数据做标准 CPT，只加 [ENT] 标记但不加对比 loss）也是一个需要排除的 trivial baseline。proposal 的 Phase 0 包含 LEIA-style baseline，这是好的，但如果 LEIA+CPT 就能拿到大部分 gain，entity-level contrastive 的增量就存疑。


【前提假设检验】:

核心逻辑链：
```
entity alignment 与 consistency 相关 (r>0.7)
→ entity-level 对比 loss 可以改善 entity alignment
→ 改善的 entity alignment 可以提升 conductivity (XRR)
→ 效果优于句子级对比
```

**第一环节（相关性）**：实证支撑最强（arXiv:2510.10280），但**相关不等于因果**。r > 0.7 的相关性可能是因为"容易对齐的实体碰巧也是容易迁移的知识"，而非"对齐实体就能产生迁移"。SubInj 的成功提供了部分因果证据（干预实体名 → consistency 提升），但那是推理时干预，不能直接推导到训练时 hidden state 对比对齐也有同样效果。

**第二环节（对比 loss 改善对齐）**：这是最薄弱的假设。在 encoder 模型上，这已被广泛验证。但在 **decoder-only LLM** 上，mean-pooling entity span 的 hidden states 作为对比学习 target 是否有效，存在合理怀疑：
- Decoder 的 hidden states 是 causal/autoregressive 的，entity span 内的 token 只看到自己及之前的 context，span 内部信息不对称
- Veitsman et al.（arXiv:2603.18863，proposal 自己引用）发现 sentence-level contrastive alignment 在 encoder 上对 token-level 任务无效——entity-level contrastive 在 decoder 上对 entity-specific 任务是否也有类似问题？
- Entity Lens 的发现（decoder LLM 有 entity-specific 机制）是描述性的，不保证对比 loss 可以有效干预这些机制

**第三环节（entity-level 优于 sentence-level）**：合理推测但无直接证据。CCL-XCoT 的句子级方法已经减少 62% 幻觉——如果 entity-level 只在此基础上带来边际提升，novelty story 就变弱了。


【3 维度打分】:

1. **Novelty: 中偏弱** —
   核心贡献是"将对比学习的粒度从句子级下移到实体级，并用 FactNet QID 作为锚点"。这是 CCL-XCoT（句子级对比 CPT）+ KBioXLM（实体级对齐，但 encoder + masking）+ FactNet（数据源）+ TransliCo（脚本桥接）的自然组合。每个单独组件都有明确的先例：
   - 对比 CPT：CCL-XCoT (EMNLP 2025)
   - 中间层对比对齐：Liu & Niehues (ACL 2025)
   - 实体级对齐在多语言模型中的应用：KBioXLM (EMNLP 2023)、LEIA (ACL 2024)、EntityCS (EMNLP 2022)
   - QID 锚定实体标注：DaMuEL (2023)
   - 脚本障碍的音译桥接：TransliCo (ACL 2024)

   Proposal 的 "六大 novelty" 中的大部分是工程集成而非概念创新。真正新的是将这些成分 **同时组合并应用于 conductivity 这一特定目标**，但这更像是"补全拼图的最后一块"而非"发现新拼图"。如果结果 positive，多数了解该领域的审稿人会说 "I would have guessed that entity-level would help — the interesting question is by how much"，而非 "this is surprising"。

2. **Significance: 中** —
   研究问题（CLiKA 揭示的 conductivity gap）是真实且重要的。如果 EACA 有效，它填补了一个有价值的空白——从"诊断 gap"到"提供解决方案"。但 significance 被两个因素限制：(a) SubInj 等推理时方法已经提供了一个低成本的部分解决方案，削弱了训练时方法的紧迫性；(b) conductivity (XRR) 是一个相对小众的指标，它与下游任务性能的关系在 CLiKA 自身论文中也未被充分建立。对更广泛 NLP/CL 社区的影响力取决于 conductivity 改善是否转化为下游可见的收益（e.g., BMLAMA, TyDiQA）。

3. **Related Work: 强** —
   这是 proposal 最强的维度。文献覆盖极其全面（30+ 篇高度相关论文），每篇的定位和差异化描述都准确。关键论文（CLiKA、CCL-XCoT、Liu & Niehues、KBioXLM、Bandarkar、Ifergan、FactNet、TransliCo）全部真实存在且描述准确。调研中未发现任何被遗漏的直接竞争者。唯一的小遗漏是未讨论 SubInj 作为 trivial alternative 的竞争地位（proposal 引用了 arXiv:2510.10280 但主要作为支持证据而非竞争方法）。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
- Related Work 覆盖是强项，确保 proposal 不会因文献遗漏被拒
- 问题真实、gap 明确（CLiKA 的 conductivity 空白），给出了合理的切入角度
- 但 Novelty 是关键上界限制：核心贡献是现有技术的自然组合（entity-level contrastive = CCL-XCoT 的粒度下移 + KBioXLM 的思路迁移到 decoder），审稿人很可能认为这是"预期中的下一步"而非"令人惊喜的发现"
- Trivial Alternative 威胁（SubInj 零训练成本获得可比效果）进一步压低了 idea 的增量价值感知
- 核心逻辑链中"decoder LLM 上 entity span mean-pooling + contrastive loss → 有效改善内部实体表征"这一环节缺乏理论或实证支撑，是未验证的假设
- 即使实验完美执行，如果核心发现是 "entity-level beats sentence-level by X points"，审稿人的反应更可能是 "reasonable, I expected this" 而非 "surprising"
- 概率范围上界 28% 假设实验能展现出令人印象深刻的跨脚本 gains（目前是最未知的部分）；下界 18% 反映了若 entity-level 与 sentence-level 差异不够显著时的 trivial alternative 风险

【主要风险】:
1. **Trivial Alternative 致命质疑**：SubInj（推理时实体注入，零训练成本）可能达到与 EACA 可比的 consistency 提升，审稿人会质疑 1000+ GPU-hours 训练的正当性。如果 proposal 无法在实验中展示 EACA 在 SubInj 无法覆盖的场景下的独特优势（如开放生成、无 entity linker 的场景），增量价值论点无法成立。
2. **"I would have guessed this" 风险**：核心 claim（entity-level 优于 sentence-level）是一个合理假设的实证验证，而非反直觉发现。如果实验结果只是确认了"entity 粒度在 entity-centric 任务上比 sentence 粒度更好"，审稿人可能认为 contribution 不足以支撑主会论文。
```

**补充说明**: 本 proposal 标注投稿 CoRL 2026（Conference on Robot Learning），但内容完全是 NLP/多语言 LLM 的 cross-lingual knowledge alignment 工作，与机器人学习无关。如果确实投稿 CoRL，会因主题不匹配被直接 desk reject。上述概率估计假设投稿至合适的 NLP 顶会（ACL/EMNLP/NAACL）。

Sources:
- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)
- [CLiKA - arXiv](https://arxiv.org/abs/2404.04659)
- [CCL-XCoT - EMNLP 2025 Findings](https://aclanthology.org/2025.findings-emnlp.93/)
- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)
- [Entity-Level Alignment - arXiv:2510.10280](https://arxiv.org/abs/2510.10280)
- [FactNet - arXiv:2602.03417](https://arxiv.org/abs/2602.03417)
- [Bandarkar et al. - arXiv:2603.17070](https://arxiv.org/abs/2603.17070)
- [Ifergan et al. - arXiv:2408.10646](https://arxiv.org/abs/2408.10646)
- [KBioXLM - EMNLP 2023](https://aclanthology.org/2023.findings-emnlp.751/)
- [DCO - arXiv:2603.04678](https://arxiv.org/abs/2603.04678)
- [TransliCo - arXiv:2401.06620](https://arxiv.org/abs/2401.06620)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
调研完毕。现在我已经掌握了足够的信息来进行客观评估。以下是我的入口评审报告：

---

```
【阶段】: Triage

【⚠️ 致命前置问题：venue mismatch】
本 proposal 是一篇纯粹的多语言 NLP / cross-lingual representation learning 论文。
CoRL 2026 (Conference on Robot Learning) 的 call for papers 明确要求：
"Submissions should focus on a core robotics problem and demonstrate 
the relevance of proposed models, algorithms, datasets, and benchmarks 
to robotics."
涵盖的 topic 包括 robot perception, manipulation, locomotion, imitation 
learning, reinforcement learning for physical robots, sim-to-real transfer 等。

本 proposal 与机器人学习没有任何关联——没有机器人实验、没有 embodied 场景、
没有 sim-to-real、没有 physical interaction。投稿 CoRL 将面临 desk rejection。

建议投稿 ACL / EMNLP / NAACL / COLM 等 NLP 主会。
以下 idea 质量评估基于 NLP venue 标准进行（如投 CoRL，概率直接为 ~0%）。

【领域调研】:
- CLiKA (Gao et al., NAACL 2024, arXiv:2404.04659): 
  定义 knowledge conductivity 和 XRR metric，发现现有多语言预训练和
  instruction tuning 均未能实质提升 XRR (< 0.01)。本 proposal 的核心
  motivation 直接来源于此。论文真实存在，描述准确。

- CCL-XCoT (EMNLP Findings 2025, arXiv:2507.14239): 
  句/段落级 contrastive CPT + XCoT prompting，降低跨语言幻觉 62%。
  本 proposal 的主要 baseline。论文真实存在，描述准确。

- Liu & Niehues (ACL 2025, arXiv:2502.14830): 
  middle-layer (layer 16/32) sentence-level contrastive alignment，
  用于 task-specific fine-tuning 而非 factual consistency。
  本 proposal 的方法论最近参照物。论文真实，描述准确。

- KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564): 
  在 encoder (XLM-R) 上用 entity masking + relation masking 做
  biomedical 跨语言 CPT，+20 F1。本 proposal 声称的 "encoder → decoder, 
  masking → contrastive, biomedical → general" 扩展确实存在真实 gap。

- FactNet (arXiv:2602.03417, Feb 2026): 
  1.7B entity-grounded atomic facts，316 Wikipedia editions，92.1% 
  grounding precision。真实存在。为本 proposal 提供实体级对比对。

- 实体级对齐与一致性 (Liu, Wang et al., arXiv:2510.10280): 
  Pearson r > 0.7 entity alignment vs. cross-lingual consistency。
  真实存在，为 "entity is the bottleneck" 论点提供关键实证。

- Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646): 
  script similarity 主导 CKR (~37.6% same-script vs. <10-20% cross-script)。
  真实存在，描述准确。

- Bandarkar et al. (arXiv:2603.17070, March 2026): 
  script match 是 knowledge transfer failure 的首要预测因子；entity priming 
  不成比例地帮助 cross-script transfer。真实存在，描述准确。关键的 entity 
  priming 实验确实支持 "entity mapping is the bottleneck" 论点。

- TransliCo (Liu et al., ACL 2024, arXiv:2401.06620): 
  transliteration contrastive learning on Glot500-m encoder, 5% data, 
  cross-script transfer 提升。真实存在。

- 调研总结: 
  Cross-lingual factual consistency/conductivity 是一个活跃且重要的研究方向。
  当前工作分为三条线：(1) sentence/paragraph-level contrastive CPT (CCL-XCoT)；
  (2) middle-layer sentence-level alignment (Liu & Niehues)；(3) entity-level 
  alignment 但限于 encoder + masking (KBioXLM) 或 inference-time intervention 
  (SubInj)。Proposal 定位在 "entity-level × contrastive × decoder-only × 
  general-domain CPT" 这个尚未被占据的交叉位置。这个 gap 是真实的，但也相当
  可预测——是 2×2 matrix 中待填的格子。

【Trivial Alternative 检验】:
存在多个成本更低的替代方案，构成实质威胁：

1. **LEIA-style entity augmentation (无 contrastive loss)**：
   仅在 CPT 中插入 [ENT]entity_name[/ENT] 标记，不加对比学习。
   proposal 自己将此列为 baseline，但如果 LEIA-style 已能达到大部分效果，
   则 contrastive loss 的增量价值存疑。

2. **SubInj inference-time intervention (arXiv:2510.10280)**：
   在推理时注入 English entity cue，无需任何训练即可获得 +14-32% recall 
   和 +17-44% consistency。这是一个零训练成本的 alternative。
   如果 EACA 需要 1100+ H100 hours 训练才能达到类似效果，
   cost-effectiveness argument 会被严重质疑。

3. **Code-switching at entity level**：
   EntityCS (EMNLP Findings 2022) 已在 encoder 上做过 entity-level 
   code-switching。在 decoder 上直接复现这一策略 (无 contrastive loss) 
   可能是更简单的 baseline。

增量价值需要 EACA 在实验中明确胜过这三个 alternative，特别是 SubInj 
(inference-time, 零训练成本)。这是 proposal 最大的 trivial alternative 威胁。

【前提假设检验】:
核心逻辑链: "entity alignment correlates with consistency (r>0.7) 
→ entity alignment IS the bottleneck → contrastive training on entity 
representations CAN fix this bottleneck → fixing it WILL improve conductivity"

未验证假设 (从前到后):

1. **相关 ≠ 因果**: r > 0.7 correlation 不等于 entity alignment 是 
   consistency 的 causal driver。可能二者都是某个更深层因素（如语言间词汇
   重叠、训练数据分布）的结果。proposal 将此相关性直接作为因果论据使用。

2. **contrastive loss 能否有效移动 entity representations**: 
   在 decoder-only LLM 中，entity span 的 hidden states 受 autoregressive 
   attention mask 影响（只能看到左侧上下文）。mean-pooling 这些 states 
   是否能产生足够 informative 的 entity representation 用于 contrastive 
   alignment 是未经验证的。encoder (KBioXLM) 中有效不等于 decoder 中有效。

3. **CLiKA 的 conductivity gap 是否可通过 CPT 解决**: 
   CLiKA 发现 "neither multilingual pretraining nor instruction tuning 
   substantially improves conductivity"。如果标准 CPT 就不行，为什么 
   entity-level contrastive CPT 就行？这个假设的逻辑跳跃在于：CLiKA 测试的 
   CPT 不是 entity-level 的——但这并不能排除 conductivity gap 是更根本性的
   architectural limitation（如 tokenizer-level script segregation）。

4. **FactNet 覆盖足以支撑有效对比训练**: 
   特别对 Tier 3 语言 (SW/YO/KM)，估计仅 5K-60K entity-fact pairs。
   以 128-256 entities/batch 的 batch size，negative diversity 是否足够？

【3 维度打分】:

1. Novelty: 中 — 
   核心 novelty 是将 entity-level contrastive alignment 从 encoder/masking 
   范式 (KBioXLM) 和 sentence-level contrastive CPT (CCL-XCoT, Liu & Niehues) 
   的交叉空白处填补，应用于 decoder-only LLM 的 general-domain conductivity。
   这个 gap 确实存在（调研确认无直接竞争工作），但属于 "2×2 matrix gap-filling"
   ——方向可预测，审稿人不太可能感到 surprised。声称的 "6 novelties" 中，
   频率加权、gradient conflict monitoring、type-aware negatives 等都是
   engineering decisions 而非概念创新。真正的 novelty delta 集中在一个点：
   entity-level granularity for factual conductivity contrastive CPT。
   这一个点是 solid 的，但 thin。

2. Significance: 中偏强 — 
   Cross-lingual knowledge conductivity 是一个重要且未解决的问题 
   (CLiKA XRR < 0.01 确认了这一点)。如果 EACA 能显著提升 XRR，
   对多语言 NLP 领域有实质影响。但 significance 受制于两个因素：
   (a) 如果 SubInj 这样的 inference-time method 已经能达到类似效果，
   则 training-time intervention 的实际价值降低；
   (b) 如果最终改进仅限于 same-script pairs (Ifergan et al. 的证据
   暗示 cross-script 可能很难)，则 generalizability 受限。
   问题本身重要，但 EACA 作为解决方案的 significance 取决于实验结果。

3. Related Work: 强 — 
   Related work 覆盖异常全面。所有关键引用 (CLiKA, CCL-XCoT, 
   Liu & Niehues, KBioXLM, FactNet, Ifergan et al., Bandarkar et al., 
   TransliCo) 均经调研确认真实存在且描述准确。差异化定位清晰：
   vs. CCL-XCoT (entity vs. sentence granularity), 
   vs. Liu & Niehues (CPT vs. task-specific, entity vs. sentence), 
   vs. KBioXLM (decoder vs. encoder, contrastive vs. masking, general vs. bio)。
   一个小缺陷：未充分讨论 SubInj (inference-time) 作为 trivial alternative 
   的威胁，只提到它 "only at inference time" 但未正面论证为什么 training-time 
   intervention 优于 inference-time。

【概率估计】: [22% - 32%] 中位 27%
（注意：此为投稿 NLP 主会 (ACL/EMNLP) 的估计。投稿 CoRL 概率约 0-2%。）

【估计理由】: 
Novelty 维度限制了上界。核心 idea "entity-level > sentence-level for 
contrastive CPT" 是一个合理但可预测的假设——如果实验 positive，多数审稿人
会说 "makes sense given the evidence" 而非 "surprising"。这将概率上限
卡在 ~35% 以下。Related Work 的出色覆盖提供了稳固的下限 (~22%)。
Significance 处于中偏强，但受 trivial alternative (SubInj) 威胁。
实验设计非常详尽（Phase 0 pilot, 多 ablation, gradient monitoring），
这在后续执行中可以提升下限，但不改变 idea 上限。

综合来看：这是一篇 well-motivated, well-positioned 的 "填空式" 工作。
direction 完全站得住脚，不会因 idea 问题被直接拒绝，但核心发现不太可能
让审稿人写 "surprising"。中位 27% 反映了 "solid but not exciting" 的定位。

【主要风险】:
1. **Trivial Alternative 威胁 (SubInj)**：inference-time entity priming 
   零训练成本可达类似效果，审稿人会问 "why pay 1100 GPU-hours for what 
   you can get with a prompt trick?" 如果实验无法证明 training-time 
   alignment 在 XRR 上显著优于 inference-time intervention，这将是最
   可能的拒稿理由。

2. **Correlation ≠ Causation 质疑**：核心 motivation 依赖 entity alignment 
   与 consistency 的 r > 0.7 相关性，但审稿人可能质疑这是否反映因果关系。
   如果 entity contrastive alignment 在实验中仅带来 marginal improvement 
   (如 XRR 从 0.01 到 0.03)，这一质疑将成为致命弱点。
```

---

**补充说明（venue mismatch）**：

这个 proposal 的领域调研、motivation chain、related work positioning 都做得非常扎实。但 **CoRL 是机器人学习会议**，接收的论文必须 "focus on a core robotics problem"，主题包括 manipulation, locomotion, perception, sim-to-real transfer 等。本 proposal 是纯粹的多语言 NLP 工作，与 robotics 无任何交集。

**强烈建议**将目标 venue 更换为 ACL 2026 / EMNLP 2026 / NAACL 2026 / COLM 2026 等 NLP 主会，上述 27% 的概率估计即基于 NLP venue 标准。

Sources:
- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)
- [CCL-XCoT - EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.93/)
- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)
- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)
- [FactNet - arXiv 2026](https://arxiv.org/abs/2602.03417)
- [Entity-Level Alignment - arXiv 2510.10280](https://arxiv.org/html/2510.10280)
- [Ifergan et al. - NAACL Findings 2025](https://aclanthology.org/2025.findings-naacl.475/)
- [Bandarkar et al. - arXiv 2603.17070](https://arxiv.org/abs/2603.17070)
- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity

## Description
EACA is a continued pretraining method that introduces InfoNCE contrastive loss on entity-span hidden states alongside standard next-token prediction, targeting entity-level cross-lingual knowledge conductivity — a capability that CLiKA (NAACL 2024) established is not substantially improved by existing multilingual pretraining or instruction tuning (XRR < 0.01). Unlike CCL-XCoT (sentence/paragraph-level contrastive CPT) and Liu & Niehues (ACL 2025, sentence-level middle-layer contrastive fine-tuning), EACA anchors contrastive pairs to Wikidata QIDs using FactNet's 1.7B entity-grounded atomic facts, operating at the entity level — the granularity empirically shown to be the bottleneck for cross-lingual consistency (entity alignment correlates at r > 0.7 with consistency, arXiv:2510.10280). This extends KBioXLM's (EMNLP Findings 2023) precedent of multi-granularity entity alignment in multilingual pretraining from encoder-based masking objectives in a specialized domain to explicit contrastive alignment in decoder-only LLMs for general-domain conductivity. Entity spans are marked with LEIA-style [ENT]/[/ENT] tokens using DaMuEL (12.3B QID-annotated tokens across 53 languages) as the primary annotation source for 10 of 13 target languages, supplemented by a Wikipedia wikilinks-to-QID extraction pipeline for the 3 uncovered Tier 3 languages (SW/YO/KM) and mReFinED entity linking for non-hyperlinked mention gap-filling, with 1.5-2 weeks budgeted for preprocessing. Representations are extracted via mean-pooling at middle layers (~layer 16, validated via Phase 0 sweep). The proposal explicitly addresses the script barrier identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070): script similarity dominates representation sharing (~37.6% same-script CKR vs. <10-20% cross-script), but entity priming disproportionately helps cross-script transfer, motivating entity-level alignment as targeting the right bottleneck. Cross-script QID pairs receive transliteration-augmented entity markers (e.g., [ENT]北京 (Beijing)[/ENT]), inspired by TransliCo (ACL 2024), with mandatory script-grouped evaluation (same-script vs. cross-script gains). Stratified batch construction uses 128-256 entities per batch with class-aware false-negative masking, type-aware hard negatives (~50% same-type entities via Wikidata P31 properties, following Robinson et al. ICLR 2021), and asymmetric positive sets for entities with uneven language coverage (K_min = 3 languages per QID). Joint optimization (L_NTP + λ·L_contrastive, λ=0.1 with warmup) includes gradient conflict monitoring: cosine similarity between NTP and contrastive gradients is tracked every 100 steps, with PCGrad (Yu et al., NeurIPS 2020) activated if conflicts exceed 30% of steps, and GradNorm (Chen et al., ICML 2018) for dynamic λ adjustment if gradient magnitudes diverge beyond 10:1. Inverse-frequency weighting prioritizes low-resource entity-facts. Catastrophic forgetting is mitigated through LoRA (rank 64) on middle layers (10-22), 15% general-domain replay, and cosine LR scheduling. A tiered language selection spans 13 languages across ~7 scripts: Tier 1 (EN/ZH/JA/DE), Tier 2 (AR/HI/TR/ID/VI/TH), Tier 3 (SW/YO/KM), with mandatory Phase 0 FactNet coverage audit and contingency replacements. Phase 0 pilot (500M tokens, 5 languages spanning ≥3 scripts, ~130 H100 hours) includes baselines against sentence-level contrastive (CCL-XCoT), middle-layer sentence contrastive (Liu & Niehues), masking-based entity alignment (KBioXLM-style adaptation), LEIA augmentation, and standard CPT, plus layer sweep, gradient analysis, and script-grouped evaluation. Six key novelties: (1) entity-level contrastive anchoring vs. sentence-level, (2) structured knowledge grounding via FactNet QIDs vs. parallel text, (3) frequency-aware weighting, (4) joint NTP+contrastive optimization with gradient conflict monitoring at entity level during CPT, (5) script-aware transliteration augmentation for cross-script entity alignment, (6) direct targeting of CLiKA's conductivity gap with script-stratified evaluation.

## Core Problem
Can entity-level contrastive alignment — anchored to Wikidata QIDs and grounded in FactNet's structured atomic facts — improve cross-lingual knowledge conductivity (as defined by CLiKA's XRR metric, Gao et al. NAACL 2024) more effectively than sentence/paragraph-level contrastive continued pretraining (e.g., CCL-XCoT) or sentence-level middle-layer alignment (Liu & Niehues, ACL 2025)? CLiKA established that neither multilingual pretraining nor instruction tuning substantially improves conductivity, with XRR scores below 0.01 for most non-English languages. EACA hypothesizes that this conductivity barrier persists because prior methods align at sentence/document granularity — conflating entity-specific factual knowledge with syntactic and discourse-level variation — whereas factual knowledge is inherently structured around entities (subject-property-object triples). A critical complication, identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070), is that script similarity is the dominant factor in cross-lingual representation sharing: high behavioral consistency does not imply shared internal representation for cross-script language pairs, and script match — not language family — is the primary predictor of knowledge transfer failure. Crucially, however, Bandarkar et al.'s entity priming experiment shows that providing source-language entity names disproportionately improves cross-script transfer, directly implicating entity-level mapping failure as the mechanism behind the script barrier. This suggests that entity-level contrastive alignment targets the right bottleneck, but that cross-script entity alignment requires additional support (e.g., transliteration augmentation) beyond what same-script entity alignment needs. EACA therefore addresses a two-level problem: (1) entity-level alignment as the fundamental unit of factual knowledge transfer, and (2) script-aware strategies to bridge the representation gap across writing systems.

## Opportunity
CCL-XCoT (EMNLP 2025 Findings) demonstrates that contrastive continued pretraining reduces cross-lingual hallucination by up to 62% but operates at sentence/paragraph granularity with parallel text. Liu & Niehues (ACL 2025) show that middle-layer contrastive alignment (layer 16 of 32 in LLaMA-3-8B) significantly improves cross-lingual transfer for downstream tasks, but again at sentence-level granularity and for task-specific fine-tuning rather than factual consistency. CLiKA (NAACL 2024) reveals a critical gap: existing multilingual pretraining and instruction tuning improve surface-level consistency but fail to improve knowledge conductivity (XRR < 0.01), suggesting that fundamentally different alignment granularity is needed. Meanwhile, FactNet (arXiv:2602.03417, Feb 2026) provides 1.7B entity-grounded atomic facts across 316 Wikipedia editions with Wikidata QID linking — enabling entity-level contrastive pairs grounded in structured knowledge. Entity Lens (BlackboxNLP 2025) confirms that decoder LLMs develop entity-specific internal mechanisms to represent multi-token entities. Liu et al. (EMNLP 2025 Findings) show that cross-lingual transfer is frequency-driven, with low-frequency facts benefiting most. Critically, recent evidence from entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) demonstrates that cross-lingual factual consistency correlates strongly with entity alignment (Pearson r > 0.7), with over 99% of consistent facts exhibiting successful entity alignment — providing direct empirical motivation for entity-level rather than sentence-level contrastive objectives. Marco et al. ('Unveiling LLMs', arXiv:2404.03623) further establish that factual knowledge about subject entities concentrates in middle layers (L5-L21 for LLaMA-2-7B). KBioXLM (EMNLP Findings 2023) provides an important precedent: it demonstrated that multi-granularity knowledge alignment (entity masking, relation masking, passage relation prediction) during continued pretraining of XLM-R yields +20 F1 points on cross-lingual zero-shot biomedical tasks, establishing entity-anchored alignment as effective — but using masking-based reconstruction on encoders rather than contrastive loss on decoder LLMs, and targeting downstream task transfer rather than factual conductivity. Ifergan et al. (NAACL Findings 2025) reveal a deeper challenge: using knowledge editing as a probe for representation sharing, they find script similarity is the dominant factor (same-script CKR ~37.6% in Mistral; cross-script <10-20%), and that behavioral consistency diverges sharply from representation sharing for cross-script pairs. Bandarkar et al. (arXiv:2603.17070, March 2026) confirm this with regression analysis showing script match as the primary predictor after controlling for model capability and question difficulty (~13% accuracy gap), but critically, their entity priming experiment shows that providing source-language entity names disproportionately improves cross-script questions — directly implicating entity mapping as the bottleneck. TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers using only 5% of training data on encoders. DaMuEL (2023) provides 12.3B tokens with QID-linked entity annotations across 53 languages, enabling efficient preprocessing for 10 of EACA's 13 target languages. The opportunity is to combine these insights — entity-level anchoring + structured knowledge grounding + middle-layer extraction + inverse-frequency weighting + script-aware strategies — into a contrastive CPT method that targets the specific granularity (entities), representation layer (middle), data regime (low-frequency facts), and script barriers where current methods demonstrably fall short.

## Related Work / Landscape
The cross-lingual factual consistency landscape spans several complementary approaches. CCL-XCoT (EMNLP 2025 Findings) is the primary baseline, employing InfoNCE symmetric contrastive loss during continued pretraining with a sentence-to-paragraph curriculum on Gemma-7B and LLaMA-3.1-8B using LoRA on layers 9-19/11-22, reducing hallucination by 62%, but operating at sentence/paragraph granularity without entity grounding or frequency weighting. Liu & Niehues (ACL 2025) represent the closest methodological precedent for contrastive alignment: they apply contrastive loss on mean-pooled sentence representations at middle layers (specifically layer 16 of 32 for LLaMA-3-8B-Instruct) during task-specific fine-tuning with LoRA (rank 8), demonstrating +1.5 F1 on slot filling and +1.5 BLEU on MT across 35 languages — however, they use sentence-level alignment with alternating (not joint) task/alignment training, target downstream task transfer rather than factual consistency, use parallel text rather than structured knowledge, and include no frequency weighting. EACA differentiates from Liu & Niehues on five axes: (1) entity-level rather than sentence-level granularity, (2) continued pretraining for factual consistency rather than task-specific fine-tuning, (3) FactNet-grounded contrastive pairs rather than parallel text, (4) joint NTP+contrastive objective rather than alternating training, and (5) inverse-frequency weighting for underrepresented facts. KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564) is an important precedent for multi-granularity entity-anchored alignment in multilingual pretraining. It performs continued pretraining on XLM-R using three alignment objectives grounded in UMLS biomedical knowledge: entity masking (code-switching entity mentions across EN-CN and predicting masked entity tokens via MLM cross-entropy), relation masking (masking relation tokens in subject-predicate-object triples), and passage relation prediction (3-way classification on aligned EN-CN Wikipedia passages). KBioXLM achieves +20 F1 points on cross-lingual zero-shot biomedical NER/RE. EACA extends this paradigm along four dimensions: (a) decoder-only LLMs vs. encoder (XLM-R), requiring contrastive loss on hidden states rather than masking-based reconstruction, since decoder LLMs lack bidirectional context for effective mask prediction; (b) general domain vs. biomedical, using FactNet's 1.7B facts across 316 editions vs. UMLS's specialized ontology; (c) explicit contrastive alignment (InfoNCE) vs. implicit alignment through masking, directly optimizing cross-lingual entity representation similarity rather than relying on the prediction bottleneck; (d) conductivity metric (CLiKA's XRR) vs. downstream task transfer, targeting the specific capability that prior methods fail to improve. CLiKA (Gao et al., NAACL 2024) provides the diagnostic framework: they define knowledge conductivity as the Cross-Retrieval Ratio (XRR) — retrieving knowledge learned in one language using another — and find that neither multilingual pretraining nor instruction tuning substantially improves XRR (scores < 0.01 for most non-English languages), with no concrete solutions proposed. The entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) provides strong empirical support: cross-lingual consistency correlates with entity alignment at r > 0.7, and their SubInj method yields +14-32% recall and +17-44% consistency gains, but only at inference time; EACA aims to achieve this alignment at training time. On the script barrier dimension, Ifergan et al. ('Beneath the Surface of Consistency', NAACL Findings 2025, arXiv:2408.10646) demonstrate via knowledge editing probes on 7 decoder LLMs (7B scale) that script similarity is the dominant factor in cross-lingual knowledge representation sharing (CKR): same-script Latin pairs show ~37.6% average CKR in Mistral, while cross-script pairs show <10-20% transfer; crucially, they find that high behavioral consistency (CKC) does not imply shared representation for cross-script pairs, with E[NCL] consistently exceeding E[NTL]. Even targeted language extension pretraining achieves only marginal cross-script CKR improvement. Bandarkar et al. ('Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts', arXiv:2603.17070, March 2026) confirm via regression analysis on ECLeKTic and MultiLoKo that script match — not language family — is the primary predictor of knowledge transfer failure (~13% accuracy gap), but their entity priming experiment reveals that providing source-language entity names disproportionately improves cross-script questions, directly implicating entity mapping as the cross-script bottleneck. TransliCo (Liu et al., ACL 2024, arXiv:2401.06620) addresses script barriers through transliteration contrastive modeling (TCM), fine-tuning Glot500-m on 5% of data with Latin transliterations as contrastive targets, producing Furina which outperforms Glot500-m on cross-script zero-shot transfer — but operates on encoders at sentence level without entity grounding. Transliteration-based post-training alignment (Moosa et al., EMNLP Findings 2024, arXiv:2406.19759) achieves up to 50% improvement on cross-script English-centric transfer with even larger gains for non-English sources. EACA incorporates this insight by adding transliteration-augmented entity contrastive pairs for cross-script language combinations as a complementary mechanism. NeighXLM (EMNLP 2025 Findings) introduces neighbor-augmented contrastive pretraining for low-resource languages without parallel data, but targets general cross-lingual transfer rather than entity-specific factual consistency. PreAlign (EMNLP 2024) uses code-switching pretraining with word-level alignment but lacks entity anchoring. CrossIC-PT (EMNLP 2025) interleaves bilingual Wikipedia content without entity-level grounding. LEIA (ACL Findings 2024) inserts English entity names with [translate]/[/translate] markers during continued pretraining of decoder LLMs, improving cross-lingual transfer but without contrastive loss or frequency weighting. EntityCS (EMNLP Findings 2022) performs entity-centric code switching with Wikidata but is limited to encoder-only models. Entity Lens (BlackboxNLP 2025) reveals that decoder LLMs develop entity-specific mechanisms to represent and manipulate multi-token entities via task vectors. The middle-layer factual knowledge claim is supported by Liu & Niehues (ACL 2025) showing layer 16 of 32 has strongest cross-lingual retrieval alignment, and Marco et al. (arXiv:2404.03623) demonstrating via dynamic knowledge graphs that middle layers (L5-L21) encode comprehensive factual knowledge while late layers show 90%+ degradation. ELO (arXiv:2601.03648, Jan 2026) demonstrates efficient layer-specific optimization with 6.46x speedup from selective middle-layer updates. FactNet (arXiv:2602.03417) provides 1.7B entity-grounded facts across 316 Wikipedia editions with significant coverage skew. CLM-Bench (arXiv:2601.17397) shows edit vectors are nearly orthogonal across languages, further motivating entity-level alignment. DCO (arXiv:2603.04678, March 2026) proposes DPO-inspired post-hoc consistency optimization, complementary to pretraining-time methods. Veitsman et al. (arXiv:2603.18863, March 2026) find that sentence-level contrastive alignment fails for token-level tasks in XLM-R encoders, supporting entity-level approaches for entity-centric tasks. Cultural knowledge asymmetry research (ACL 2025) confirms that frequency drives cross-lingual transferability.

## Approach
EACA adds an InfoNCE contrastive loss on entity-span hidden states to the standard next-token prediction (NTP) objective during continued pretraining. The method comprises five integrated components: entity preprocessing, entity-level contrastive alignment, script-aware augmentation, stratified batch construction, and joint optimization with gradient monitoring.

**1. Entity Preprocessing Pipeline.** Entity boundary annotation uses a two-stage pipeline. Stage 1 (primary): DaMuEL (2023), which provides 12.3B QID-annotated tokens across 53 languages (CC BY-SA), is used directly for the 10 target languages it covers (EN/ZH/JA/DE/AR/HI/TR/ID/VI/TH). DaMuEL provides start/end token indices per entity mention with Wikidata QID links, extracted from Wikipedia wikilinks and expanded via lemmatization and alias matching (~17% recall gain over raw wikilinks). Stage 2 (Tier 3 gap-filling): For the 3 Tier 3 languages not covered by DaMuEL (SW/YO/KM), a lightweight Wikipedia wikilinks extraction pipeline resolves hyperlinks to QIDs via Wikidata sitelinks (~50-60% mention coverage). mReFinED (EMNLP Findings 2023), which is 44-60x faster than comparable entity linkers, is applied as a second pass on high-resource languages to annotate non-hyperlinked entity mentions where higher recall is needed. Entity boundaries are marked with LEIA-style [ENT]/[/ENT] tokens around linked mentions. Preprocessing budget: 1.5-2 weeks engineering time, ~2-4 GPU-days on A100 for mReFinED gap-filling, ~24-48 CPU-hours for wikilinks extraction across Tier 3 languages. This pipeline is on the critical path and must complete before Phase 0.

**2. Entity-Level Contrastive Alignment.** Entity representations are extracted via mean-pooling over hidden states within the [ENT]...[/ENT] span at a designated middle layer (defaulting to layer 16 for 32-layer models based on Liu & Niehues' ACL 2025 finding and Marco et al.'s analysis; validated via Phase 0 sweep over layers 12-20), with loss propagation blocked on boundary markers themselves. Contrastive pairs are constructed per QID from FactNet: positive pairs consist of atomic fact descriptions for the same QID across languages, while negatives come from different QIDs within the same batch (detailed in Component 4). Inverse-frequency weighting assigns higher contrastive loss weight to facts with lower cross-lingual FactNet coverage, directly targeting low-resource facts where CLiKA's conductivity analysis shows the largest gap.

Theoretical motivation for entity-level granularity: Three converging lines of evidence support entity-level over sentence-level contrastive alignment for factual consistency: (1) Entity alignment analysis (arXiv:2510.10280) demonstrates Pearson r > 0.7 between entity alignment and cross-lingual consistency, with >99% of consistent facts showing successful entity alignment — establishing entities as the bottleneck for consistency; (2) CLM-Bench's finding that cross-lingual edit vectors are nearly orthogonal implies that factual knowledge editing, which operates at entity-level (subject-property-object triples), requires entity-aligned representations rather than sentence-aligned ones; (3) CLiKA's failure result — that sentence/document-level pretraining and instruction tuning do not improve conductivity — suggests that coarser-grained alignment conflates entity-specific factual knowledge with syntactic and discourse-level variation, diluting the alignment signal.

**3. Script Barrier Mitigation.** EACA's 13 target languages span ~7 scripts (Latin: EN/DE/TR/ID/VI/SW/YO; CJK: ZH/JA; Arabic: AR; Devanagari: HI; Thai: TH; Khmer: KM). Ifergan et al. (NAACL Findings 2025) demonstrate that cross-lingual representation sharing (CKR) clusters strongly by script family (~37.6% same-script CKR vs. <10-20% cross-script in Mistral-7B), and Bandarkar et al. (arXiv:2603.17070) confirm script match as the primary predictor of transfer failure (~13% gap). This poses a genuine risk that entity-level contrastive alignment may primarily improve same-script entity alignment while showing limited gains for cross-script pairs. However, two findings provide grounds for cautious optimism: (a) Bandarkar et al.'s entity priming experiment shows source-language entity names disproportionately improve cross-script transfer, implicating entity mapping — not script-level representation — as the cross-script bottleneck for factual knowledge; (b) TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers on encoders using only 5% of training data. EACA therefore incorporates a script-aware augmentation strategy: for cross-script QID pairs (e.g., EN-ZH, EN-AR, EN-HI, EN-TH, EN-KM), entity mentions in non-Latin scripts are supplemented with Latin transliterations appended within the [ENT] boundary (e.g., [ENT]北京 (Beijing)[/ENT]), providing a lexical bridge for the contrastive objective. This is tested as an ablation (EACA vs. EACA+translit) to isolate the contribution of transliteration augmentation beyond entity-level alignment. The evaluation plan includes mandatory script-grouped analysis: same-script entity alignment gains (Latin-Latin, CJK-CJK) vs. cross-script gains (Latin-CJK, Latin-Arabic, Latin-Devanagari, etc.), reporting both entity cosine similarity and downstream factual consistency metrics separately for each script-pair category. If Phase 0 reveals that cross-script entity alignment gains are <50% of same-script gains despite transliteration augmentation, this will be explicitly reported as a limitation and the analysis will quantify what fraction of EACA's overall conductivity improvement comes from same-script vs. cross-script alignment.

**4. Stratified Batch Construction with Type-Aware Hard Negatives.** Effective contrastive learning is highly sensitive to negative quality (Robinson et al., ICLR 2021). EACA uses stratified mini-batching: each batch contains K_batch = 128-256 unique QIDs, with all available language instances per QID forming the positive set (asymmetric positive sets accommodate QIDs present in only 2-3 languages without dropping them). Minimum language coverage per QID is K_min = 3 languages; QIDs with fewer than 3 language instances are filtered during preprocessing. Class-Aware Masking (CAM) ensures that all instances of the same QID are excluded from the InfoNCE denominator, preventing false-negative contamination. For hard negative mining, type-aware stratification ensures ~50% of in-batch negatives share the anchor entity's Wikidata type (e.g., Q5/human, Q515/city, Q4830453/organization) — forcing the model to discriminate on fine-grained entity identity rather than coarse type. This is implemented via Wikidata instance-of (P31) properties, grouping entities into 8-10 macro-types for sampling. The remaining ~50% are random negatives for diversity. Batch composition is balanced across script families to ensure cross-script contrastive signals appear in every batch. The InfoNCE loss for entity e with QID q is: L_entity(q) = -log[exp(sim(h_q^i, h_q^j)/τ) / (exp(sim(h_q^i, h_q^j)/τ) + Σ_{k≠q} exp(sim(h_q^i, h_k)/τ))], where h_q^i, h_q^j are entity representations from different languages for the same QID, and h_k are representations from different QIDs, with τ = 0.07 as the temperature (tuned in Phase 0 over {0.05, 0.07, 0.1}).

**5. Joint Optimization with Gradient Monitoring.** The joint objective is L_total = L_NTP + λ * L_entity_contrastive, with λ initialized at 0.1 (following guidance from headless LM work showing λ ∈ [0.01, 0.1] is appropriate for contrastive + generation joint training during CPT). A potential tension exists: NTP learns language-specific token distributions while contrastive loss pulls entity representations together across languages. Unlike Liu & Niehues' alternating approach, EACA uses joint optimization to ensure entity alignment co-adapts with the language modeling objective — but addresses gradient conflict risk through three mechanisms: (a) Phase 0 gradient analysis: cosine similarity between ∇L_NTP and ∇L_entity_contrastive is computed every 100 steps on the shared LoRA parameters. If gradient cosine similarity is negative for >30% of monitored steps, PCGrad projection (Yu et al., NeurIPS 2020) is applied — projecting the contrastive gradient onto the normal plane of the NTP gradient to eliminate destructive interference. (b) GradNorm (Chen et al., ICML 2018) is implemented as an optional dynamic λ adjustment mechanism: if the gradient magnitude ratio between the two losses drifts beyond 10:1, GradNorm normalizes to equalize learning rates. (c) λ warmup: contrastive loss weight ramps linearly from 0 to λ_target over the first 10% of training steps, allowing NTP to stabilize before contrastive pressure is introduced. Phase 0 reports gradient conflict frequency, cosine similarity distribution, and whether PCGrad/GradNorm activation was required — this informs the full training configuration. If gradient conflicts are severe (>50% of steps) even with PCGrad, the fallback is alternating optimization (NTP steps → contrastive steps per batch) following Liu & Niehues' validated approach.

Catastrophic forgetting is mitigated through three mechanisms: (a) LoRA (rank 64) applied to middle layers only (layers 10-22), following CCL-XCoT's selective layer approach and ELO's findings that first/last layers are critical for general capabilities; (b) 15% general-domain English replay data mixed into training batches; (c) cosine learning rate schedule with linear warmup (peak LR 2e-5). Language selection follows a tiered strategy: Tier 1 comprises 4 anchor languages (EN/ZH/JA/DE, >1M entity-fact pairs), Tier 2 includes 6 mid-resource languages (AR/HI/TR/ID/VI/TH, 100K-1M pairs), and Tier 3 covers 3 low-resource languages (SW/YO/KM). Tier 3 viability assessment based on Wikipedia article counts (SW: ~117K, YO: ~37K, KM: ~12K) and FactNet's 0.36 low-resource yield rate estimates approximately 50K-200K entity-fact pairs for Swahili, 15K-60K for Yoruba, and 5K-25K for Khmer. None of the Tier 3 languages are covered by DaMuEL, so all three rely on the Wikipedia wikilinks extraction pipeline (Stage 2 above). A mandatory FactNet coverage audit in Phase 0 will report exact entity-fact pair counts for all 13 languages; minimum viable threshold is set at 10K entity-fact pairs per language (sufficient for contrastive batching at size 128-256 with adequate negative diversity). If any Tier 3 language falls below threshold, contingency replacements include Bengali (BN, ~157K Wikipedia articles), Tagalog (TL, ~115K articles), or Hausa (HA, ~8K articles but stronger NLP benchmark coverage). Languages below 25K pairs receive LEIA-style English entity augmentation to supplement contrastive pairs.

Phase 0 pilot uses 500M tokens across 5 languages (3 Tier-1 + 2 Tier-2, selected to span at least 3 scripts for script barrier analysis) for approximately 130 H100 hours, with baselines including: (a) CCL-XCoT-style sentence-level contrastive CPT, (b) Liu & Niehues-style middle-layer sentence-level contrastive alignment (the closest methodological comparison, testing entity-level vs. sentence-level at the same middle layer), (c) LEIA-style entity augmentation without contrastive loss, (d) standard CPT, and (e) KBioXLM-style entity masking adaptation (masking [ENT]-bounded tokens and predicting via NTP, without contrastive loss — testing contrastive vs. masking-based entity alignment on decoders). Phase 0 additionally includes: a layer sweep (layers 12, 14, 16, 18, 20) to empirically determine optimal entity extraction depth; gradient conflict analysis (cosine similarity monitoring, PCGrad activation rate); and script-grouped entity alignment analysis (same-script vs. cross-script gains). Go/no-go criteria require entity cosine similarity improvement of at least 0.05, BMLAMA-53 consistency improvement of at least 2 points, no TyDiQA degradation beyond 1 point, AND gradient conflict rate below 50% (with or without PCGrad). Full training processes 1.5-2.5B tokens on LLaMA-3.1-8B (primary) and Gemma-7B (secondary, for CCL-XCoT comparability) across all 13 languages. A complementary EACA+DCO experiment tests whether pretraining-time and post-hoc consistency methods yield cumulative gains. Evaluation covers BMLAMA-53, TyDiQA-GoldP, X-CODAH, LiveCLKTBench, and CLiKA's XRR metric (to directly measure conductivity improvement), plus entity representation cosine similarity analysis. All metrics are reported with script-grouped breakdowns (same-script pairs, cross-script pairs, overall) as a mandatory analysis dimension. Ablations cover: entity-level vs. sentence-level contrastive (the central hypothesis), contrastive vs. masking-based entity alignment (EACA vs. KBioXLM-style adaptation), EACA vs. EACA+transliteration augmentation (script barrier mitigation), frequency weighting on/off, type-aware vs. random negatives, number of languages, layer selection, joint vs. alternating training, gradient conflict mitigation (none vs. PCGrad vs. GradNorm), contrastive pair construction (FactNet-grounded vs. parallel-text-based), and K_min language threshold (2 vs. 3 vs. 5).

## Inspiration
CCL-XCoT contrastive CPT framework (EMNLP 2025 Findings) + Liu & Niehues middle-layer contrastive alignment (ACL 2025) + FactNet entity-grounded facts (arXiv:2602.03417) + LEIA entity boundary markers (ACL 2024) + CLiKA conductivity diagnostic (NAACL 2024) + Entity-level alignment in crosslingual consistency (arXiv:2510.10280) + Entity Lens entity-specific mechanisms (BlackboxNLP 2025) + Marco et al. middle-layer factual knowledge (arXiv:2404.03623) + ELO selective layer optimization (arXiv:2601.03648) + Liu et al. frequency-driven transfer (EMNLP 2025) + CLM-Bench orthogonal edit vectors (arXiv:2601.17397) + cultural knowledge asymmetry frequency hypothesis (ACL 2025) + Ifergan et al. script-CKR dominance (NAACL Findings 2025) + Bandarkar et al. script barrier in reasoning models (arXiv:2603.17070) + TransliCo transliteration-contrastive script bridging (ACL 2024) + KBioXLM multi-granularity entity alignment (EMNLP Findings 2023) + DaMuEL QID-annotated corpus (2023) + Robinson et al. hard negative mining (ICLR 2021) + PCGrad gradient surgery (NeurIPS 2020) + GradNorm dynamic loss weighting (ICML 2018)

## Key References
- CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation (EMNLP Findings 2025)
- Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs [Liu & Niehues] (ACL 2025, arXiv:2502.14830)
- Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly [CLiKA] (NAACL 2024, arXiv:2404.04659)
- On the Entity-Level Alignment in Crosslingual Consistency [Liu, Wang et al.] (arXiv:2510.10280)
- FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding (arXiv 2026)
- LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation (ACL Findings 2024)
- On the Representations of Entities in Auto-regressive Large Language Models [Entity Lens] (BlackboxNLP 2025, arXiv:2510.09421)
- Unveiling LLMs: The Evolution of Latent Representations in a Dynamic Knowledge Graph [Marco et al.] (arXiv:2404.03623)
- Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs [Ifergan et al.] (NAACL Findings 2025, arXiv:2408.10646)
- Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts [Bandarkar et al.] (arXiv:2603.17070, March 2026)
- TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models (ACL 2024, arXiv:2401.06620)
- Breaking the Script Barrier in Multilingual Pre-Trained Language Models with Transliteration-Based Post-Training Alignment [Moosa et al.] (EMNLP Findings 2024, arXiv:2406.19759)
- KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model [Geng et al.] (EMNLP Findings 2023, arXiv:2311.11564)
- DaMuEL: A Large Multilingual Dataset for Entity Linking (arXiv:2306.09288, 2023)
- Contrastive Learning with Hard Negative Samples [Robinson et al.] (ICLR 2021)
- Gradient Surgery for Multi-Task Learning [PCGrad, Yu et al.] (NeurIPS 2020)
- GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks [Chen et al.] (ICML 2018)
- mReFinED: An Efficient End-to-End Multilingual Entity Linking Model (EMNLP Findings 2023)
- NeighXLM: Enhancing Cross-Lingual Transfer in Low-Resource Languages via Neighbor-Augmented Contrastive Pretraining (EMNLP Findings 2025)
- mLUKE: The Power of Entity Representations in Multilingual Pretrained Language Models (ACL 2022)
- ELO: Efficient Layer-Specific Optimization for Continual Pretraining of Multilingual LLMs (arXiv 2026)
- Tracing Multilingual Factual Knowledge Acquisition in Pretraining (EMNLP Findings 2025)
- PreAlign: Boosting Cross-Lingual Transfer by Early Establishment of Multilingual Alignment (EMNLP 2024)
- Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training [CrossIC-PT] (EMNLP 2025)
- Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025)
- EntityCS: Improving Zero-Shot Cross-lingual Transfer with Entity-Centric Code Switching (EMNLP Findings 2022)
- Optimizing Language Models for Crosslingual Knowledge Consistency [DCO] (arXiv 2026)
- Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models [BMLAMA] (EMNLP 2023)
- LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs (arXiv 2025)
- Why Better Cross-Lingual Alignment Fails for Better Cross-Lingual Transfer: Case of Encoders [Veitsman et al.] (arXiv 2026)
- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026)
- DoLa: Decoding by Contrasting Layers Improves Factuality and Faithfulness of Large Language Models (ICLR 2024)

## Resource Estimate
- **manual**: {'gpu_hours': '1100-1550 H100 (Preprocessing: ~10-15 GPU-days A100 for mReFinED; Phase 0: ~130 including layer sweep + gradient analysis; Full training: ~800-1100; Evaluation: ~70; Ablations: ~90-165 including script/masking/gradient ablations)', 'timeline': '4.5-5.5 months (includes 1.5-2 weeks preprocessing pipeline)', 'estimated_gpu_cost': '$2,200-3,100 (at ~$2/H100-hr spot)'}
- **human_in_loop**: {'gpu_hours': '900-1250 H100', 'timeline': '3.5-4.5 months', 'claude_api_cost': '$300-450 (FactNet coverage audit, DaMuEL integration, preprocessing pipeline, gradient analysis visualization, evaluation analysis, paper drafting)', 'estimated_gpu_cost': '$1,800-2,500'}
- **auto_research**: {'gpu_hours': '1100-1600 H100', 'timeline': '3-4 months', 'claude_api_cost': '$600-950 (full pipeline automation: DaMuEL integration + mReFinED gap-filling + Tier 3 wikilinks pipeline + FactNet coverage audit + Tier 3 viability check, entity marker insertion, layer sweep, gradient analysis, hyperparameter sweep, script-grouped analysis, ablation analysis, paper writing)', 'estimated_gpu_cost': '$2,200-3,200', 'speed_bottleneck': 'Preprocessing pipeline (1.5-2 weeks) is on critical path before Phase 0; Phase 0 pilot (2-3 weeks including layer sweep, gradient analysis, and script-grouped evaluation) must complete before full training; full training wallclock ~30-50 hours per run on 8xH100; sequential dependency: preprocessing → FactNet audit gates Tier 3 language selection → pilot go/no-go gates full training'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f794c7c6-7681-4508-82fe-e26349823af5",
  "type": "user",
  "uuid": "2442b3f2-8566-41b2-b020-5d8682c9d103",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:59:26.922Z_

```json
{
  "parentUuid": "2442b3f2-8566-41b2-b020-5d8682c9d103",
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
  "uuid": "6f641e00-4c8b-4824-97ec-97c7d762eb86",
  "timestamp": "2026-05-19T18:59:26.922Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:59:26.922Z_

```json
{
  "parentUuid": "6f641e00-4c8b-4824-97ec-97c7d762eb86",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5b9f71b8-bbcd-4708-a48b-35cdcf08ee52",
  "timestamp": "2026-05-19T18:59:26.922Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make an informed assessment.…",
  "leafUuid": "5b9f71b8-bbcd-4708-a48b-35cdcf08ee52",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Entity-level contrastive alignment for cross-lingual knowledge",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5"
}
```

---

### Assistant

_source line 8 · 2026-05-19T19:00:03.698Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully and produce a Meta Judge synthesis.

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability: [25% - 35%] 中位 30%

**Reviewer 2:**
- Novelty: 中偏弱 (Medium-Weak)
- Significance: 中 (Medium)


- Related Work: 强 (Strong)
- Probability: [18% - 28%] 中位 22%

**Reviewer 3:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability: [22% - 32%] 中位 27%

All three reviewers flag the same critical issue: this work doesn't align with CoRL's scope, which would be fatal if submitted there. Their assessments assume an NLP venue instead. Computing the median probabilities across the three reviewers gives me 22%, 27%, and 30%, with the middle value at 27%.

The mean acceptance probability comes to 26.3% with a standard deviation of about 3.3%, indicating fairly tight agreement among reviewers. On the novelty front, there's clear consensus that the contribution is medium or below—all three rate it as such, suggesting the work combines existing techniques in a somewhat predictable way rather than introducing fundamentally new ideas.

The reviewers unanimously rate the related work section as strong. There's also broad agreement on significance, clustering around medium to medium-strong, with the caveat that the problem itself is real and important but the impact is limited by simpler alternatives. The most striking consensus emerges around the trivial alternative threat: all three reviewers identify inference-time entity injection as a serious vulnerability that undermines the approach's novelty. They consistently characterize the idea as a natural or predictable next step—filling an obvious gap in the 2×2 matrix of existing methods. Additionally, R2 and R3 both raise concerns about correlation versus causation. Looking at the unique concerns raised by individual reviewers — R2 flags DCO as a complementary method I haven't addressed, and R3 points out that FactNet's coverage for lower-tier languages might be too sparse to provide sufficient negative diversity. The consistency score of 3.3% puts this in medium agreement territory, so I'm applying the stricter threshold from R2's 22% assessment. This gives me a median of 27% when I account for the medium consistency and the bias toward the more conservative estimate.

Now I'm checking the implementation feasibility across all three reviews — they converge on similar resource requirements of around 1100-1600 H100 hours over 4-5 months, and they all note that existing benchmarks like BMLAMA-53 and TyDiQA can be reused without needing new evaluation infrastructure.

For the actual execution, the datasets are publicly available through FactNet and DaMuEL, though the approach does require training runs on 8B models with continued pretraining, plus some manual work on the preprocessing pipeline and entity annotation steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b9f71b8-bbcd-4708-a48b-35cdcf08ee52",
  "isSidechain": false,
  "requestId": "req_011CbCSa9153KzdcTRkM7oG1",
  "type": "assistant",
  "uuid": "c948a856-0591-4bdf-957d-f7f233fa8025",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kh1DoUSsxqULkTHoYPywsL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25864,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3634,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3634,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 25864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25864
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

_source line 9 · 2026-05-19T19:00:52.672Z_

【阶段】: Meta Judge
【三次中位】: [30%, 22%, 27%]  std=3.3%
【共识维度】:
- **Novelty = 中 或更低**（3/3）：核心贡献是已有技术的可预测组合（"2×2 matrix gap-filling"、"显而易见的下一步"、"natural combination"），每个组件（实体标记、对比损失、中间层提取、QID 锚定、音译增强）均有明确来源，真正的 novelty delta 集中在单一维度——"entity-level granularity for conductivity contrastive CPT"，solid but thin
- **Related Work = 强**（3/3）：文献覆盖极其全面，所有关键引用经调研确认真实且描述准确，差异化定位清晰
- **Significance = 中至中偏强**（3/3）：问题真实重要（CLiKA XRR < 0.01 的 conductivity gap），但受 trivial alternative 和效果不确定性制约
- **SubInj trivial alternative 威胁 = 严重**（3/3）：推理时零训练成本实体注入即获 +14-32% recall / +17-44% consistency，EACA 需 1100+ H100 小时训练——如果效果可比，成本效益论证崩塌
- **"I would have guessed this" 风险**（3/3）：核心 claim（entity-level > sentence-level）是合理假设的实证验证而非反直觉发现，审稿人更可能说"makes sense"而非"surprising"
- **Decoder mean-pooling 有效性存疑**（2/3，R2+R3 明确提出）：decoder-only LLM 的 causal attention mask 下，entity span mean-pooling 是否能产生足够 informative 的表征用于对比学习，是未经验证的关键假设
- **Correlation ≠ Causation**（2/3，R2+R3 明确，R1 隐含）：r > 0.7 相关性不等于因果，实体对齐可能是一致性的结果而非原因
- **Venue Mismatch = 致命**（3/3）：CoRL 是机器人学习会议，本 proposal 是纯 NLP 工作，投 CoRL 将 desk reject（概率 ~0%）

【异常维度】:
- R2 将 Novelty 评为"中偏弱"，比 R1/R3 的"中"更悲观——但其论证逻辑（"每个组件都有明确先例"）实际被 R1/R3 共享，差异更多在措辞力度而非实质判断上，故不作为 outlier 大幅降权
- R1 单独强调"LEIA + CCL-XCoT 组合 baseline"作为独立的 trivial alternative 威胁——R2/R3 未专门提出此组合，但逻辑合理，应纳入考量
- R3 单独提出 Tier 3 语言 FactNet 覆盖不足的具体数据质量风险（5K-60K pairs 的 negative diversity 问题）——属于实验细节，降权处理
- R2 单独引入 DCO（arXiv:2603.04678）作为互补后训练方法——proposal 本身已提到，非新增风险

【最终概率】: [20% - 30%] 中位 25%
【一致性】: 中（std=3.3%，rubric 判决方向一致但严格程度有差异）
【综合理由】:
三位审稿人在核心判断上高度趋同：这是一篇 well-motivated、well-positioned 的"填空式"工作，方向站得住脚但缺乏 surprise factor。概率上界由 Novelty 决定——三位均判定为"中"或更低，这意味着即使实验完美执行，概率也难以突破 35%。

中位取 25% 而非简单中位 27% 的理由：按"中一致偏严"原则，R2 的 22% 虽略偏悲观但其核心论证（每个组件均有先例、SubInj 零成本替代）被 R1/R3 完全认同。R1 的 30% 是三者中最宽松的，其 Significance 评为"中偏强"提供了上界支撑，但即便 R1 也承认 novelty 是"组合"而非"新概念"，且实验 delta 大小是决定性变量。综合后偏向 25%，区间 [20%-30%] 反映了：下界 20% 对应审稿人判定为 incremental combination + SubInj 效果可比的情况；上界 30% 对应实验展示出跨脚本的显著独特优势。

**Venue mismatch 特别说明**：以上概率基于投稿 NLP 主会（ACL/EMNLP/NAACL）。若实际投稿 CoRL 2026，概率为 ~0%（desk rejection）。这是三位审稿人的一致判断。

【建议】: 不推荐（中位 25% < 36% 阈值；Novelty 天花板过低，trivial alternative 威胁严重，但 idea 方向本身不是致命的——不构成 KILL，而是当前 framing 下中稿概率不足）

【实施评估】:
  - 计算资源: 1100-1600 H100 小时（含预处理 ~10-15 GPU-days A100、Phase 0 ~130 H100-hr、全量训练 ~800-1100 H100-hr、评估 ~70 H100-hr、消融 ~90-165 H100-hr），预估 GPU 成本 $2,200-3,200
  - 数据需求: FactNet（1.7B entity-grounded facts, arXiv:2602.03417）、DaMuEL（12.3B QID-annotated tokens, 53 languages, CC BY-SA）、Wikipedia wikilinks（Tier 3 语言）——核心数据公开可得，但 Tier 3 语言（SW/YO/KM）覆盖可能不足（估计 5K-60K entity-fact pairs），需 Phase 0 审计确认
  - 人工介入: 预处理 pipeline 搭建（1.5-2 周工程时间）、mReFinED 实体链接 gap-filling、Tier 3 语言 wikilinks 提取、Phase 0 go/no-go 决策、gradient 分析解读——中等人工参与度
  - 训练需求: 需要在 LLaMA-3.1-8B（主）和 Gemma-7B（辅）上进行 continued pretraining，1.5-2.5B tokens 全量训练，LoRA rank 64 on layers 10-22，单次训练 wallclock ~30-50 小时 on 8×H100
  - 新 Benchmark: 不需要构建新 benchmark（使用现有 BMLAMA-53、TyDiQA-GoldP、X-CODAH、LiveCLKTBench、CLiKA XRR），但需要搭建 entity-level cosine similarity 分析 + script-grouped evaluation 框架
  - 预估周期: 4-5.5 个月（预处理 1.5-2 周 → Phase 0 pilot 2-3 周 → 全量训练 4-6 周 → 评估+消融 2-3 周 → 论文写作 3-4 周），关键路径：预处理 → FactNet 审计 → Phase 0 go/no-go → 全量训练

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c948a856-0591-4bdf-957d-f7f233fa8025",
  "isSidechain": false,
  "requestId": "req_011CbCSa9153KzdcTRkM7oG1",
  "type": "assistant",
  "uuid": "0247d12d-3d13-4f29-992e-911c6375a93e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kh1DoUSsxqULkTHoYPywsL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25864,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3634,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3634,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 25864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25864
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make an informed assessment.…",
  "leafUuid": "0247d12d-3d13-4f29-992e-911c6375a93e",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Entity-level contrastive alignment for cross-lingual knowledge",
  "sessionId": "47dbb15e-7978-4708-be71-94230b7e7bf5"
}
```

---
