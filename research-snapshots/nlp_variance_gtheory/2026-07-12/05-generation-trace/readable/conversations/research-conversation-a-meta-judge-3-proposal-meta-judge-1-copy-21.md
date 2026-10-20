# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/a6809ca4-ba1b-4ddb-94f2-39ad79891e71.jsonl`
- **Structured JSON:** [`c13b54f9c7d59ad0f5b4.json`](../../sessions/c1/c13b54f9c7d59ad0f5b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:12:16.456Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:12:16.456Z",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 【致命性前置问题：venue mismatch】\nCoRL 2026 (Conference on Robot Learning) 的 scope 明确限定在 robotics + machine learning 交叉领域。\n其 Call for Papers 原文声明：\"Submissions without a robotics focus will be returned without review.\"\n本 proposal 研究的是多语言 LLM 中的跨语言知识传导性 (cross-lingual knowledge conductivity)，\n与机器人学没有任何关联。投稿 CoRL 会被直接 desk reject。\n本 proposal 的合理目标会议是 ACL / EMNLP / NAACL / EACL 等 NLP 主会。\n\n以下评审基于 \"假设投稿至合适的 NLP 主会 (如 ACL/EMNLP)\" 进行，以便提供有意义的反馈。\n\n【领域调研】:\n- CLiKA (Gao et al., NAACL 2024, arXiv:2404.04659): 建立了跨语言知识对齐的三层框架\n  (Performance / Consistency / Conductivity)，发现现有多语言预训练和指令微调均未实质\n  改善 conductivity (XRR < 0.01)。本 proposal 直接针对此 gap。论文真实存在，描述准确。\n\n- CCL-XCoT (EMNLP Findings 2025, arXiv:2507.14239): 句/段粒度对比持续预训练，在 \n  Gemma-7B/LLaMA-3.1-8B 上将跨语言幻觉率降低最多 62%。论文真实存在，描述准确。\n  本 proposal 的直接 baseline。\n\n- Liu & Niehues (ACL 2025, arXiv:2502.14830): 中间层句子级对比对齐用于跨语言迁移，\n  发现 layer 16/32 的跨语言检索对齐最强。论文真实存在，描述准确。\n  本 proposal 声称在 granularity（entity vs. sentence）和目标（conductivity vs. task \n  transfer）上差异化，成立。\n\n- KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564): 在 XLM-R（encoder）上\n  用 entity masking + relation masking + passage relation prediction 进行多粒度知识锚定\n  CPT，生物医学域零样本跨语言 NER/RE 提升 ~20 F1。论文真实存在，描述准确。\n  本 proposal 声称是将此范式从 encoder + masking 扩展到 decoder + contrastive。\n\n- Entity-level alignment in cross-lingual consistency (Liu, Wang et al., arXiv:2510.10280): \n  证明 entity alignment 与跨语言一致性 Pearson r > 0.7，>99% 一致事实成功 entity \n  alignment；SubInj 方法在推理时获得 +14-32% recall、+17-44% consistency。\n  论文真实存在。**关键：此论文已展示 inference-time entity alignment intervention \n  有显著效果，构成本 proposal 的 trivial alternative 威胁。**\n\n- FactNet (arXiv:2602.03417, Feb 2026): 1.7B entity-grounded atomic facts，覆盖 316 \n  Wikipedia editions，grounding precision 92.1%。论文真实存在，描述准确。\n\n- Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646): 知识编辑探针证明 script \n  similarity 主导跨语言表示共享 (~37.6% same-script CKR vs. <10-20% cross-script)。\n  论文真实存在。\n\n- Bandarkar et al. (arXiv:2603.17070, March 2026): script match 是知识迁移失败的主要\n  预测因子 (~13% gap)；entity priming 不成比例地改善跨脚本问题。论文真实存在，\n  描述准确。\n\n- TransliCo (ACL 2024, arXiv:2401.06620): 在 Glot500-m encoder 上用 5% 数据做 \n  transliteration contrastive learning 产出 Furina，改善跨脚本零样本迁移。\n  论文真实存在。encoder-only，句子级，无 entity grounding。\n\n- DaMuEL (arXiv:2306.09288, 2023): 53 语言 12.3B tokens QID-linked entity \n  annotations。论文真实存在，描述准确。\n\n- 调研总结: 跨语言事实一致性是一个活跃领域。CCL-XCoT（句子级对比 CPT）和 Liu & \n  Niehues（中间层句子级对比）代表当前 SOTA 方法论；CLiKA 确立了 conductivity gap；\n  entity alignment 与 consistency 的高相关性已被实证。本 proposal 位于这些工作的\n  自然交汇点——从 sentence-level 下沉到 entity-level 的对比对齐。这一步在逻辑上\n  连贯，但在 novelty 层面更接近\"组合型创新\"（recombination）而非\"概念型突破\"。\n\n【Trivial Alternative 检验】:\n存在显著的 trivial alternative 威胁：\n\n1. **Inference-time entity intervention (SubInj)**: Liu, Wang et al. (arXiv:2510.10280) \n   已证明在推理时注入英语实体名称即可获得 +14-32% recall 和 +17-44% consistency \n   提升，且无需任何训练。EACA 需要 ~1100-1600 H100-hours 的训练成本才能实现\n   training-time 的 entity alignment——如果 EACA 的增量收益相对于 SubInj 不显著，\n   整个方法的 cost-effectiveness 会被严重质疑。\n\n2. **LEIA-style entity augmentation (无 contrastive loss)**: 本 proposal 自己将 LEIA \n   列为 ablation baseline。如果仅在 CPT 中插入 [ENT]...[/ENT] 标记（不加 contrastive \n   loss）就能获得大部分收益，那么对比损失的增量价值存疑。\n\n3. **EACA 相对于 CCL-XCoT 的增量**: CCL-XCoT 已经在句子粒度实现 62% 幻觉率降低。\n   EACA 声称 entity-level 更好，但这个 claim 尚未有任何实证，而 CCL-XCoT 已有\n   实验结果。如果 entity-level 的边际改进不大（比如从 62% 到 68%），付出的工程\n   复杂度（entity preprocessing pipeline、QID grounding、type-aware negatives 等）\n   难以 justify。\n\n增量价值的成立条件：EACA 必须显著优于 (a) SubInj inference-time intervention、\n(b) LEIA-style entity augmentation without contrastive loss、(c) CCL-XCoT \nsentence-level contrastive。三重门槛，每一个都不轻松。\n\n【前提假设检验】:\n核心 claim 的逻辑链中有以下未经验证的关键假设：\n\n1. **\"相关性 → 因果性\" 跳跃**: entity alignment 与 consistency 的 r > 0.7 相关性\n   是 observational evidence。Proposal 隐含假设 \"改善 entity alignment 会 cause \n   consistency improvement\"，但这可能是共同因果（例如训练数据覆盖度同时影响两者）。\n   **目前没有因果干预实验证明 training-time entity alignment improvement → \n   consistency improvement 的因果链。**\n\n2. **\"Entity-level 粒度优于 sentence-level\" 的假设缺乏直接实证**: CLiKA 证明了\n   sentence/document-level methods 不 work，但 \"因此 entity-level 会 work\" 是\n   逻辑跳跃。失败可能不仅仅是粒度问题——也可能是对比损失本身不够、数据量不够、\n   或者 decoder LLM 的 representation geometry 就不适合通过对比学习改变。\n\n3. **Decoder LLM 上 entity-level contrastive loss 的可行性假设**: KBioXLM 在 \n   encoder (XLM-R) 上有效不意味着 decoder LLM 上同样有效。Decoder LLM 的表示\n   空间是 autoregressive 的，causal attention 意味着 entity span 的表示只能看到\n   左侧上下文——这与 encoder 的双向上下文截然不同。mean-pooling 一个只有左侧\n   上下文的 entity span 是否能产生有意义的 entity representation？这是一个非平凡\n   假设，Entity Lens 的发现（decoder LLMs develop entity-specific mechanisms）\n   提供了部分支撑，但不足以完全消除疑虑。\n\n4. **FactNet 覆盖的均匀性假设**: Proposal 承认 FactNet 有 \"significant coverage \n   skew\"，但整个方法依赖于低资源语言有足够的 entity-fact pairs 来构建对比训练。\n   如果 Tier 3 语言的实体覆盖极低（如 Khmer 可能只有 5K-25K pairs），对比学习\n   的有效性会打折。\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心贡献是将 entity-level 粒度引入跨语言对比 CPT for decoder LLMs。但这更像是\n   已有组件的重新组合，而非新概念：\n   - Entity-level alignment in multilingual pretraining: KBioXLM (EMNLP Findings 2023) \n     已做过，只是在 encoder + masking 上\n   - Contrastive CPT for cross-lingual consistency: CCL-XCoT (EMNLP Findings 2025) \n     已做过，只是在 sentence-level\n   - Middle-layer contrastive alignment: Liu & Niehues (ACL 2025) 已做过\n   - Script barrier + transliteration: TransliCo (ACL 2024) 已做过\n   - Entity boundary markers: LEIA (ACL Findings 2024) 已做过\n   \n   EACA 的 novelty delta 是 \"在 decoder LLM 的中间层对 entity span 做 InfoNCE \n   contrastive CPT，用 FactNet QIDs 构建对比对\"。这是一个具体的 engineering \n   组合，但审稿人可能会认为这是 \"obvious next step given the existing literature\"\n   —— 一旦知道 entity alignment 是 bottleneck（2510.10280）+ 中间层对比有效\n   （Liu & Niehues）+ 对比 CPT 有效（CCL-XCoT），entity-level 对比 CPT at \n   middle layers 几乎是不需要 insight 就能提出的方案。\n   \n   Proposal 列出的 \"6 key novelties\" 中多数是工程选择（frequency weighting、\n   gradient monitoring、script-aware evaluation）而非概念创新。\n\n2. **Significance: 中** — \n   研究问题本身重要：CLiKA 揭示的 conductivity gap (XRR < 0.01) 是一个真实且\n   有影响力的问题（NAACL 2024）。跨语言知识一致性对多语言 LLM 的实际部署至关\n   重要。但几个因素限制了 significance 的上界：\n   - 如果 positive result，审稿人的反应更可能是 \"makes sense, entity-level should \n     help\" 而不是 \"surprising\"——因为 entity alignment 作为 bottleneck 已经被\n     2510.10280 充分论证过了\n   - 方法的可推广性受限于 FactNet + DaMuEL 数据的可用性——对于没有足够 Wikipedia \n     覆盖和 Wikidata QID 链接的语言（真正的低资源语言），这个方法不直接适用\n   - 如果 negative result（entity-level 没有比 sentence-level 好多少），贡献变为\n     一个 negative finding，其发表价值取决于 analysis quality\n\n3. **Related Work: 强** — \n   这是本 proposal 的最强维度。Related work 覆盖极其全面：\n   - 直接竞争工作（CCL-XCoT、Liu & Niehues、KBioXLM）均被详细讨论，差异化清晰\n   - Script barrier 文献（Ifergan et al.、Bandarkar et al.、TransliCo）覆盖充分\n   - 所引论文经调研均真实存在，描述基本准确\n   - FactNet、DaMuEL、LEIA 等基础设施型工作引用合理\n   - 差异化定位（5 axes vs. Liu & Niehues、4 dimensions vs. KBioXLM）表述清晰\n   唯一潜在遗漏：可能需要更多讨论 inference-time entity intervention（SubInj 等）\n   作为 trivial baseline 的对比 positioning。\n\n【概率估计】: [15% - 25%] 中位 20%\n（注：此概率基于投稿 NLP 主会如 ACL/EMNLP。投稿 CoRL 的概率为 ~0%，会被 desk reject。）\n\n【估计理由】: \n从 3 维度到概率的推理：\n- Related Work 很强，意味着作者对领域有深入理解，这是基础保障\n- Significance 中等，问题重要但预期发现不 surprising\n- Novelty 弱-中，是限制上界的关键因素——组合型创新 + \"obvious next step\" 风险高\n\nNovelty 是限制上界的主要维度。对于 ACL/EMNLP 主会，审稿人会问：\n\"KBioXLM + CCL-XCoT + Liu & Niehues 三篇已有论文的自然结合，这里面的 intellectual \ncontribution 是什么？\"如果答案仅是 \"我们第一个在 decoder LLM 上做 entity-level \ncontrastive CPT\"，这是 execution novelty 而非 conceptual novelty，对 top venue \n来说偏弱。\n\n同时，trivial alternative 威胁（SubInj 推理时介入 vs. 昂贵的对比 CPT）进一步\n压低了评估——审稿人有很自然的 pushback 角度。\n\n如果实验能证明 EACA 显著优于 SubInj 且优于 CCL-XCoT，概率可以上升到 ~30%。\n但那是实验层面的事，入口阶段只评 idea 本身。\n\n【主要风险】:\n1. **\"Obvious next step\" 质疑**: 核心贡献是已有方法的粒度迁移（sentence→entity）+ \n   场景迁移（encoder→decoder），审稿人可能认为 intellectual contribution 不足以\n   支撑 top venue 主会论文。Proposal 自身列出的 \"6 key novelties\" 反而暴露了这个\n   问题——需要列 6 个 novelties 通常意味着没有一个足够强的单一贡献。\n\n2. **Trivial alternative 未被充分 address**: SubInj (arXiv:2510.10280) 已在推理时\n   以零训练成本实现 entity-level alignment 的显著提升。Proposal 如果不能在 framing \n   中明确论证为什么 training-time alignment 相对于 inference-time intervention 有\n   不可替代的优势（beyond \"training-time is more elegant\"），审稿人会认为 EACA \n   是一个过度工程化的解决方案。\n```\n\nSources:\n- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)\n- [CLiKA - arXiv](https://arxiv.org/html/2404.04659)\n- [CCL-XCoT - EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.93/)\n- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)\n- [Liu & Niehues - arXiv](https://arxiv.org/abs/2502.14830)\n- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)\n- [Entity-Level Alignment in Cross-lingual Consistency](https://arxiv.org/pdf/2510.10280)\n- [FactNet - arXiv 2026](https://arxiv.org/abs/2602.03417)\n- [Ifergan et al. - NAACL Findings 2025](https://www.semanticscholar.org/paper/Beneath-the-Surface-of-Consistency:-Exploring-in-Ifergan-Choshen/54a2e0dad730c1a955c66f3568a3fa0dca400225)\n- [Bandarkar et al. - arXiv 2603.17070](https://arxiv.org/abs/2603.17070)\n- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)\n- [DaMuEL - arXiv](https://arxiv.org/abs/2306.09288)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make my assessment. Let me compile the analysis.\n\n---\n\n```\n【阶段】: Triage\n```\n\n## ⚠️ 重大前置问题：投稿 venue 严重不匹配\n\n**CoRL（Conference on Robot Learning）是机器人学习会议**，其 Call for Papers 明确要求论文聚焦于\"core robotics problem\"，鼓励 real-robot experiments 或 sim-to-real transfer 证据。本 proposal 是一篇纯粹的多语言 NLP 工作（cross-lingual knowledge conductivity via entity contrastive alignment），与机器人学习**完全无关**。投到 CoRL 会被 desk reject。\n\n**应投稿的正确 venue**：ACL / EMNLP / NAACL / EACL 主会或 Findings，或 COLM / ICLR。以下评估基于投稿到 NLP/CL 顶会（如 ACL/EMNLP）的假设进行。\n\n---\n\n```\n【领域调研】:\n```\n\n- **[CLiKA] Gao et al. (NAACL 2024, arXiv:2404.04659)**: 定义了 cross-lingual knowledge conductivity 的 XRR 指标，发现现有多语言预训练和指令微调均无法实质性提升 conductivity（XRR < 0.01）。**这是 EACA 立项的根基，论文确实存在且描述准确。CLiKA 仅提出诊断，未提出解决方案——这为 EACA 留出了空间。**\n\n- **[CCL-XCoT] Zheng et al. (EMNLP Findings 2025)**: 在 Gemma-7B/LLaMA-3.1-8B 上用 sentence-to-paragraph 级别的 InfoNCE + NTP joint CPT，减少 hallucination 62%。**是 EACA 的主要 baseline——EACA 的核心 claim 是 entity-level 比 sentence/paragraph-level 更有效。CCL-XCoT 确实存在。**\n\n- **[Liu & Niehues] (ACL 2025, arXiv:2502.14830)**: 在 LLaMA-3-8B middle layer（layer 16）做 sentence-level contrastive alignment 用于 task-specific fine-tuning，证明中间层是跨语言对齐的最佳位置。**EACA 借用了其 middle-layer 的发现但改为 entity-level。确实存在。**\n\n- **[Ifergan et al.] (NAACL Findings 2025, arXiv:2408.10646)**: 通过 knowledge editing 探测发现 script similarity 是 representation sharing 的主导因素（same-script CKR ~37.6% vs cross-script <10-20%）。**确实存在，描述准确。**\n\n- **[Bandarkar et al.] (arXiv:2603.17070, March 2026)**: 发现 script match 是知识迁移失败的主要预测因子（~13% gap），但 entity priming 实验表明提供源语言 entity names 能不成比例地提升 cross-script 问题准确率。**确实存在，且\"entity priming disproportionately helps cross-script\"的描述准确——这是 EACA entity-level alignment 最重要的实证动机之一。**\n\n- **[FactNet] (arXiv:2602.03417, Feb 2026)**: 1.7B entity-grounded atomic facts，316 Wikipedia editions，92.1% grounding precision。**确实存在，是 EACA 的核心数据基础设施。**\n\n- **[KBioXLM] Geng et al. (EMNLP Findings 2023, arXiv:2311.11564)**: 在 XLM-R encoder 上用 entity masking + relation masking + passage relation prediction 做生物医学领域多语言 CPT，cross-lingual zero-shot +20 F1。**确实存在。EACA 的定位是将此范式从 encoder/masking/specialized-domain 扩展到 decoder/contrastive/general-domain。**\n\n- **[TransliCo] (ACL 2024, arXiv:2401.06620)**: 在 Glot500-m encoder 上用 transliteration contrastive learning 仅用 5% 数据桥接 script barrier。**确实存在，但仅作用于 encoder。EACA 将 transliteration augmentation 作为跨脚本辅助策略。**\n\n- **[arXiv:2510.10280] Liu, Wang et al.**: Entity alignment 与 crosslingual consistency 的 Pearson r > 0.7 相关性，>99% 一致性 facts 有成功的 entity alignment。**确实存在。这是 EACA\"entity 是瓶颈\"claim 的最关键实证依据。**\n\n- **调研未发现的直接竞争者**：搜索\"entity-level contrastive pretraining decoder LLM\"和\"entity-anchored contrastive alignment\"等关键词，**未找到已有工作直接在 decoder-only LLM 上做 entity-level InfoNCE contrastive CPT for cross-lingual factual conductivity**。最接近的是 KBioXLM（encoder + masking）、CCL-XCoT（decoder + sentence-level contrastive）、EntityCS（encoder + code-switching）、LEIA（decoder + entity augmentation without contrastive）。EACA 的组合确实是新的。\n\n- **调研总结**：Cross-lingual factual consistency 是一个活跃且重要的研究方向。CLiKA 提出了诊断但无解。CCL-XCoT 和 Liu & Niehues 验证了 contrastive CPT 的有效性但停留在 sentence-level。实证工作（arXiv:2510.10280, Bandarkar et al.）强烈暗示 entity-level 是真正的瓶颈。EACA 处于这些工作的自然交汇点，填补了\"entity-level contrastive CPT on decoder LLMs\"这一具体空缺。\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在 partial trivial alternatives，但 EACA 的增量价值可以论证。**\n\n1. **LEIA-style entity augmentation (无 contrastive loss)**：LEIA 已经通过在 CPT 中插入 entity markers 来提升跨语言迁移。一个 reviewer 会问：\"只用 LEIA-style augmentation + standard CPT，不加 contrastive loss，是否已经足够？\" Proposal 已将此作为 ablation（好的），但如果 LEIA 本身就能在 CLiKA 的 XRR 上取得大部分收益，EACA 的 contrastive loss 增量就会缩小。\n\n2. **SubInj / SubSub (arXiv:2510.10280) 推理时干预**：这些方法在推理时注入英文 entity name 就能获得 +14-32% recall 和 +17-44% consistency gains。一个 reviewer 会问：\"如果推理时 entity priming 就够了，为什么要付训练时 contrastive alignment 的代价？\" Proposal 提到了这一点但回答相对薄弱——\"训练时对齐 vs 推理时干预是互补的\"需要实证支持。\n\n3. **CCL-XCoT 的 entity-grounded 简单变体**：一个 reviewer 可能想到：在 CCL-XCoT 的 sentence-level contrastive loss 中，不用 entity-level，而是简单地在 batch 构建时确保 positive pairs 包含相同 entity mentions，这可能用更低成本实现大部分收益。\n\n**增量价值**：EACA 的增量在于 (a) 直接在 entity representation space 做对齐（vs 间接通过 sentence-level），(b) FactNet 提供的结构化 entity-fact grounding（vs 依赖 parallel text），(c) frequency weighting 针对 low-resource entities。这些增量是真实的，但需要实验验证其 marginal value 是否显著。\n\n---\n\n```\n【前提假设检验】:\n```\n\n**核心逻辑链**：Entity alignment 是 crosslingual consistency 的瓶颈 → Entity-level contrastive loss 能改善 entity alignment → 改善 entity alignment 能改善 XRR conductivity → 这比 sentence-level contrastive 更有效。\n\n**检验各环节**：\n\n1. ✅ \"Entity alignment 是瓶颈\"——有实证支撑（arXiv:2510.10280 的 r > 0.7 相关性；Bandarkar entity priming 实验）。**但注意**：相关性 ≠ 因果性。entity alignment 好的 facts 一致性高，不代表强制 entity alignment 就能带来一致性提升。这是一个关键的逻辑跳跃。\n\n2. ⚠️ \"Entity-level InfoNCE contrastive loss 能有效改善 decoder LLM 的 entity representation alignment\"——**这是未经验证的核心假设**。在 encoder 上有效（KBioXLM）不代表在 decoder-only 上有效。Decoder-only 模型的 hidden states 是 causal/left-to-right 的，mean-pooling over entity span 是否能得到有意义的 entity representation 尚无定论。Entity Lens (BlackboxNLP 2025) 提供了一些间接支撑，但那是分析性工作，不是训练时干预的证据。\n\n3. ⚠️ \"Contrastive loss 在 entity-level 比 sentence-level 更有效\"——这是中心假设，**完全没有先验实证**。理论动机（\"entity 是 factual knowledge 的自然单元\"）是 plausible 但不是 evidence。一个 reviewer 可以 argue：\"sentence-level contrastive 已经隐含了 entity alignment（因为 parallel sentences 中相同 entities 自然出现），而且提供了更丰富的上下文信号。\"\n\n4. ⚠️ \"Joint NTP + entity contrastive 不会严重冲突\"——Proposal 设计了 gradient monitoring + PCGrad fallback，但前提假设是 NTP 和 entity contrastive 在 middle layers 的 gradient 足够兼容。Veitsman et al. (arXiv 2026) 发现 sentence-level contrastive alignment 在 token-level tasks 上失败——类似的 granularity mismatch 可能出现在 entity-level contrastive + token-level NTP 之间。\n\n---\n\n```\n【3 维度打分】:\n```\n\n**1. Novelty: 中（偏强）**\n\n理由：\n- **真实的组合新颖性**：调研确认没有现有工作直接在 decoder-only LLM 上做 entity-level InfoNCE contrastive CPT for cross-lingual factual conductivity。最近的 CCL-XCoT 是 sentence-level，KBioXLM 是 encoder + masking + biomedical domain，LEIA 无 contrastive loss，EntityCS 是 encoder + code-switching。EACA 的组合点确实是空白。\n- **但**：这是一个\"自然延伸\"而非\"conceptual surprise\"。当 CLiKA 发现 conductivity gap、arXiv:2510.10280 发现 entity alignment 是瓶颈、CCL-XCoT 验证了 contrastive CPT 有效时，\"把 contrastive CPT 从 sentence-level 下沉到 entity-level\"是一个**高度可预测的下一步**。一个熟悉该领域的 reviewer 看到这个 idea 可能会说 \"this is the obvious next thing to try\" 而非 \"surprising\"。\n- Novelty 的真实增量主要来自 FactNet QID-grounded contrastive pairs（vs parallel text）和 script-aware transliteration augmentation 的集成。但 transliteration augmentation 本身来自 TransliCo (ACL 2024)，frequency weighting 来自 Liu et al. (EMNLP 2025)，gradient monitoring 来自 PCGrad/GradNorm——都是已有 technique 的搬运。\n- **总结**：组合是新的，空白是真的，但 conceptual novelty 有限——更像是\"missing experiment\"而非\"missing insight\"。\n\n**2. Significance: 中**\n\n理由：\n- **问题重要性高**：Cross-lingual knowledge conductivity 是多语言 LLM 的核心挑战。CLiKA (NAACL 2024) 的发现——现有方法都无法实质性提升 conductivity——使这个问题非常值得研究。\n- **如果 positive，impact 是真实的**：如果 EACA 确实能在 XRR 上取得 significant improvement（而非仅仅 BMLAMA 上的 marginal gains），这对多语言 LLM 领域有明确贡献。\n- **但 scope 受限**：(a) 方法依赖 FactNet + DaMuEL 这些特定资源，泛化性有限；(b) 仅在 7-8B 模型上验证；(c) 如果 entity-level contrastive 只在 same-script pairs 有效（Ifergan et al. 的证据暗示这很可能），实际价值会大打折扣——cross-script 才是真正的 hard case。\n- **\"I would have guessed this\" 风险**：如果结果是\"entity-level contrastive > sentence-level contrastive for entity-centric tasks\"，这 **完全符合直觉**。审稿人可能会说 \"of course, finer-grained alignment at the entity level helps for entity-level evaluation.\" 这不 surprising。\n\n**3. Related Work: 强**\n\n理由：\n- Related work 覆盖极其全面：核心的 CLiKA、CCL-XCoT、Liu & Niehues、KBioXLM、arXiv:2510.10280 全部引用且描述准确。\n- Script barrier 维度（Ifergan et al., Bandarkar et al., TransliCo）的覆盖是一个亮点，说明作者对领域有深入理解。\n- 差异化定位清晰：与 CCL-XCoT 的 5 轴差异、与 KBioXLM 的 4 维度扩展都有具体论述。\n- FactNet (Feb 2026)、Bandarkar et al. (March 2026) 等非常新的论文都被引用，说明 related work 的时效性好。\n- 唯一轻微不足：缺少对 mLUKE (ACL 2022) 和 LUKE 系列在 entity representation 方面的更深入讨论，以及与 code-switching pretraining (PreAlign, CrossIC-PT) 的更系统对比。但这属于小问题。\n\n---\n\n```\n【概率估计】: [25% - 38%] 中位 30%\n```\n\n```\n【估计理由】:\n```\n\n三维度综合来看：\n- **Related Work（强）** 保证了论文的基本学术规范和定位不会被 reject 因为 \"missing important work\"。\n- **Significance（中）** 说明问题值得做，但 scope 和 impact 的天花板不够高——依赖特定资源、same-script 可能吃到大部分收益、cross-script 提升不确定。\n- **Novelty（中偏强）** 是主要限制上界的因素。核心 idea 是一个\"自然的下一步\"（natural next step），在该领域活跃研究者眼中可预测。这使得论文更接近\"solid engineering contribution\"而非\"surprising insight\"。如果核心结果 positive，审稿人可能的反应是 \"this confirms what we expected\" 而非 \"this changes how I think about the problem.\"\n\n概率主要被 Novelty 的 \"predictable next step\" 性质限制在 35% 以下。如果实验做得非常好（strong ablations, clear entity-vs-sentence separation, cross-script gains），可以推到 35-38%；如果 cross-script 提升有限或 entity-level vs sentence-level 的增量不显著，概率跌到 25% 以下。\n\n```\n【主要风险】:\n```\n\n1. **\"Predictable Extension\" 质疑**：审稿人可能认为这是 CCL-XCoT + entity markers 的直接组合，conceptual contribution 不足以支撑顶会主会。Related work 做得越全面，反而越容易暴露\"这只是现有工作的自然推论\"——一个 reviewer 可以说 \"the authors themselves show that all the ingredients already exist; the paper's contribution is just putting them together.\"\n\n2. **Entity-level vs Sentence-level 的 marginal gain 可能不显著**：如果 sentence-level contrastive 已经隐含地做了 entity alignment（因为 parallel sentences 中相同 entity 的 representations 被拉近），entity-level 的额外收益可能很小。特别是在 same-script 语言对上，sentence-level 可能已经足够好了。这会使 core claim 变成 marginal empirical finding 而非 significant methodological advance。\n\nSources:\n- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)\n- [CCL-XCoT - EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.93/)\n- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)\n- [Ifergan et al. - NAACL Findings 2025](https://aclanthology.org/2025.findings-naacl.475/)\n- [Bandarkar et al. - arXiv:2603.17070](https://arxiv.org/abs/2603.17070)\n- [FactNet - arXiv:2602.03417](https://arxiv.org/abs/2602.03417)\n- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)\n- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)\n- [Entity-Level Alignment - arXiv:2510.10280](https://arxiv.org/abs/2510.10280)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct my evaluation. Let me compile the analysis.\n\n---\n\n```\n【阶段】: Triage\n\n============================================================\n⚠️ 严重警告：venue 完全不匹配 ⚠️\n============================================================\n\n本 proposal 研究的是多语言 LLM 的 cross-lingual knowledge conductivity，\n属于 NLP/Computational Linguistics 领域。\n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确指出：\n\"Submissions without a robotics focus will be returned without review.\"\nCoRL 接受的主题包括：robot perception、manipulation、locomotion、\nsim-to-real transfer、imitation learning for robotics 等。\n\n本 proposal 与 robotics 零关联，投稿 CoRL 会被 desk reject。\n如果目标是 NLP 会议（ACL/EMNLP/NAACL），以下评估按 NLP 领域标准给出。\n如果确实要投 CoRL，概率为 ~0%，无需进一步评估。\n\n以下按 NLP/CL 领域会议标准评估 idea 质量。\n============================================================\n\n【领域调研】:\n\n1. CLiKA (Gao et al., NAACL 2024, arXiv:2404.04659):\n   定义了 cross-lingual knowledge conductivity 及 XRR 指标，发现现有多语言预训练和指令微调均无法实质性提升 conductivity（XRR < 0.01）。这是本 proposal 的核心问题来源。论文真实存在，描述准确。\n\n2. CCL-XCoT (Zheng et al., EMNLP Findings 2025, arXiv:2507.14239):\n   在句/段级别用 InfoNCE 对比学习进行 continued pretraining，配合 XCoT 指令微调，减少跨语言幻觉达 62%。本 proposal 的直接 baseline，描述准确。注意：CCL-XCoT 的 arXiv 日期为 2025 年 7 月，而 proposal 中声称其为 EMNLP 2025 Findings——需验证时间线是否一致（EMNLP 2025 于 2025 年底举行，7 月 arXiv 合理）。\n\n3. Liu & Niehues (ACL 2025, arXiv:2502.14830):\n   中间层（layer 16/32）句级对比对齐用于 task-specific fine-tuning，在 slot filling (+1.5 F1) 和 MT (+1.5 BLEU) 上取得改进。本 proposal 的方法论前辈，描述准确。\n\n4. KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564):\n   在 XLM-R 上用实体掩码、关系掩码、段落关系预测进行生物医学跨语言对齐，+20 F1。本 proposal 的实体级对齐先例，但限于 encoder + 生物医学域。描述准确。\n\n5. FactNet (arXiv:2602.03417, Feb 2026):\n   1.7B 实体锚定原子事实，316 个 Wikipedia 版本，92.1% grounding precision。真实存在，描述准确。\n\n6. Bandarkar et al. (arXiv:2603.17070, Mar 2026):\n   确认 script match 是跨语言知识迁移失败的主要预测因子（~13% gap），entity priming 实验证明实体映射是跨脚本瓶颈。真实存在，描述准确。\n\n7. Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646):\n   用 knowledge editing 探针发现 script similarity 主导跨语言表征共享（same-script CKR ~37.6% vs. cross-script <10-20%）。真实存在，描述准确。\n\n8. DCO (arXiv:2603.04678, Mar 2026):\n   DPO-inspired post-hoc consistency optimization。本 proposal 提到其为互补方法。真实存在。\n\n9. AlignX (EMNLP 2025):\n   多语言 continual pretraining 对齐表征 + 指令微调，扩展到 51 种语言。与本 proposal 有重叠但粒度不同（AlignX 为通用表征对齐，非实体级）。\n\n10. Entity-Level Alignment (Liu, Wang et al., arXiv:2510.10280):\n    发现 entity alignment 与 cross-lingual consistency 的 Pearson r > 0.7，SubInj 方法在推理时就能达到 +14-32% recall 和 +17-44% consistency gains。真实存在，描述准确——但这恰恰构成了本 proposal 的 trivial alternative 威胁。\n\n- 调研总结: \n  跨语言知识一致性/传导性是 2024-2026 年的活跃研究方向，已有工作沿两条线展开：(a) 句/段级对比 CPT (CCL-XCoT, Liu & Niehues)，(b) 推理时干预 (SubInj, entity priming)。实体级对比对齐在 decoder LLM 上的 CPT 尚无直接先例（KBioXLM 仅限 encoder + 生物医学），本 proposal 定位在此空白处。但该空白是否代表\"真正未被探索的机会\"还是\"已有的组合但尚未有人做因为改进可能有限\"，存在不确定性。\n\n\n【Trivial Alternative 检验】:\n\n存在两个严肃的 trivial alternative 威胁：\n\n(1) **推理时 SubInj/Entity Priming**：arXiv:2510.10280 的 SubInj 方法仅在推理时注入英语实体名称，就获得了 +14-32% recall 和 +17-44% consistency gains，且零训练成本。Bandarkar et al. 的 entity priming 实验同样表明推理时提供实体名就能显著改善跨脚本迁移。EACA 需要 ~1100-1600 H100 hours 的训练成本，如果最终效果与推理时干预相当，增量价值极低。Proposal 未直接与 SubInj 进行比较或论证为何训练时对齐优于推理时干预。\n\n(2) **LEIA + 简单 entity code-switching**：LEIA 已经证明在 decoder LLM CPT 中插入英语实体名可以改善跨语言迁移。如果 EACA 的核心优势主要来自实体边界标注（[ENT]/[/ENT]），而非对比损失本身，那么 LEIA 风格的简单 augmentation 可能已经捕获了大部分收益。\n\n增量价值论证：Proposal 的 implicit 论点是\"训练时对齐 > 推理时干预\"因为它改变了模型的内部表征而非仅仅在表面层面提供线索。这有一定道理，但未被论证——是一个需要实验验证的假设，而非已知事实。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链：\n\"句级对齐不够 → 实体才是事实知识的基本单位 → 实体级对比对齐能改善 conductivity\"\n\n未经验证的关键假设：\n\n(1) **相关 ≠ 因果**：entity alignment 与 consistency 的 r > 0.7 相关性是观察性的。高 entity alignment 可能是 consistency 的结果而非原因——可能是因为模型在某些语言对上整体表征更好，因此 entity alignment 和 consistency 同时高。强制对齐 entity 表征是否能因果性地改善 consistency，是一个未经验证的跳跃。\n\n(2) **对比损失在 decoder LLM 隐藏状态上的有效性**：在 encoder 模型上，对比学习有大量成功先例（SimCLR, CLIP, E5 等）。但 decoder LLM 的隐藏状态具有不同特性——它们是自回归的、位置敏感的。Mean-pooling entity span 在 decoder 中间层是否能产生足够好的实体表征用于对比学习，是一个未经检验的假设。Liu & Niehues 在句级别展示了可行性，但实体级别 span 更短（通常 1-5 tokens），信号可能更弱。\n\n(3) **NTP 和实体对比损失的兼容性**：NTP 优化语言特定的 token 分布，对比损失拉近跨语言实体表征。这两个目标可能在 decoder LLM 中存在根本性冲突。Proposal 设计了 PCGrad/GradNorm 作为缓解措施，但如果冲突是根本性的（而非工程可调的），这些机制无法真正解决问题。\n\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   \n   理由：实体级对比对齐在 decoder LLM CPT 上的应用确实没有直接先例——这是真实的 novelty。KBioXLM (EMNLP Findings 2023) 做了实体级对齐但在 encoder 上用 masking 目标；CCL-XCoT (EMNLP Findings 2025) 做了对比 CPT 但在句/段级别；Liu & Niehues (ACL 2025) 做了中间层对比对齐但在句级别。EACA 在\"粒度 × 模型架构 × 训练范式\"三维矩阵中占据了一个空位。\n\n   但 novelty 的性质是**组合性的**而非**概念性的**——它将已有的组件（InfoNCE、entity span、middle-layer extraction、decoder LLM CPT）以新组合拼装在一起，每个组件都有明确先例。核心 insight \"entity-level alignment should help entity-level consistency\" 虽然在技术执行上是新的，但在概念上是相当直觉的。审稿人可能会认为这是 \"the obvious next thing to try\" 而非 \"a surprising new insight\"。\n\n   此外，方法的 novelty 声称中有些水分：proposal 列出了 6 条 novelty，但其中 (3) frequency-aware weighting、(4) gradient conflict monitoring、(5) transliteration augmentation、(6) script-stratified evaluation 均为工程细节或评估规范，不构成独立的 novelty 贡献。真正的核心 novelty 只有 (1) entity-level contrastive anchoring 和 (2) structured knowledge grounding via QIDs。\n\n2. Significance: 【中偏强】\n   \n   理由：研究问题本身重要且被明确界定。CLiKA (NAACL 2024) 令人信服地证明了 conductivity gap 的存在，且至今无有效解决方案。如果 EACA 的核心发现是 positive 的（实体级 > 句级），这对多语言 LLM 社区有实质指导意义——它会建立一个新的 CPT 范式。\n\n   但 significance 受限于两个因素：\n   - 如果结果仅限于 same-script pairs 有效而 cross-script 改善有限（这是 proposal 自己承认的风险），那么实际影响的语言覆盖范围会大打折扣。\n   - 推理时方法（SubInj）已经取得了实质性的 consistency gains，如果 EACA 的额外训练成本仅换来边际改善，则实际意义存疑。\n   \n   问题的重要性不等于解决方案的重要性。问题是 strong 的，但这个特定解决方案是否足够有力仍需验证。\n\n3. Related Work: 【强】\n   \n   理由：这是整个 proposal 最突出的部分。Related work 覆盖面极广且定位精确：\n   - 方法论维度：CCL-XCoT（句/段级对比 CPT）、Liu & Niehues（句级中间层对比对齐）、KBioXLM（encoder 实体级 masking 对齐）——每个都有清晰的差异化论述\n   - 问题维度：CLiKA（conductivity gap）、arXiv:2510.10280（entity alignment 与 consistency 的相关性）\n   - 脚本维度：Ifergan et al. (NAACL Findings 2025)、Bandarkar et al. (arXiv:2603.17070)、TransliCo (ACL 2024)\n   - 数据/资源维度：FactNet、DaMuEL、mReFinED\n   \n   所有引用的论文经调研确认真实存在，描述基本准确。positioning 对每个 baseline 都给出了多维度的区分。\n   \n   唯一的轻微不足是：对 SubInj (arXiv:2510.10280) 作为推理时替代方案的论述不够充分——它被作为 \"motivation\" 引用（entity alignment 很重要），但未被作为 \"trivial alternative\" 正面对比。\n\n\n【概率估计】: [25% - 35%] 中位 28%\n（注意：此概率基于投稿 ACL/EMNLP/NAACL 等 NLP 主会估计。\n 投稿 CoRL 2026 的概率为 ~0%——venue 完全不匹配，会被 desk reject。）\n\n【估计理由】:\n- Novelty 为\"中\"：核心 idea 有真实的组合新颖性，但概念上是直觉的\"the obvious next step\"，缺少 surprising 的 insight。这限制了上界——即使实验完美执行，审稿人可能写 \"well-executed but the idea is incremental\"。\n- Significance 为\"中偏强\"：问题重要且被领域认可，但推理时 trivial alternative (SubInj) 的存在削弱了训练时方案的增量价值论证。\n- Related Work 为\"强\"：这是一个 plus，但不能弥补 idea 内核的 novelty 上限。\n- 概率上界被 Novelty 限制在 ~35%：如果核心实验全部 positive，审稿人大概率评价为 \"solid empirical contribution, somewhat expected result\"，可能获得一个 borderline accept。但如果有审稿人认为 SubInj 已经足够，或者认为从 correlation 到 causation 的跳跃不成立，则可能被拉到 reject。\n\n【主要风险】:\n1. **Trivial Alternative 风险**：SubInj 等推理时实体干预方法零训练成本即可获得显著 consistency gains (+17-44%)。如果 EACA 的额外 ~1100 H100 hours 训练仅换来边际改善（例如在 SubInj 基础上仅额外 +5%），审稿人会质疑其实际价值。Proposal 未提供\"训练时对齐优于推理时干预\"的先验论证。\n2. **相关-因果跳跃风险**：整个 proposal 的逻辑基础建立在\"entity alignment 与 consistency 高度相关 → 因此强制 entity alignment 能改善 consistency\"。但这一因果方向未被建立。如果 entity alignment 是高 consistency 的伴随现象而非原因，那么 EACA 的核心前提不成立。\n```\n\nSources:\n- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)\n- [CLiKA - arXiv](https://arxiv.org/abs/2404.04659)\n- [CCL-XCoT - arXiv](https://arxiv.org/abs/2507.14239)\n- [CCL-XCoT - EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.93.pdf)\n- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)\n- [Liu & Niehues - arXiv](https://arxiv.org/abs/2502.14830)\n- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)\n- [FactNet - arXiv](https://arxiv.org/abs/2602.03417)\n- [Bandarkar et al. - arXiv](https://arxiv.org/abs/2603.17070)\n- [DCO - arXiv](https://arxiv.org/abs/2603.04678)\n- [Entity-Level Alignment - arXiv](https://arxiv.org/pdf/2510.10280)\n- [AlignX - EMNLP 2025](https://arxiv.org/html/2509.24338)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Entity-Anchored Contrastive Alignment for Cross-Lingual Knowledge Conductivity\n\n## Description\nEACA is a continued pretraining method that introduces InfoNCE contrastive loss on entity-span hidden states alongside standard next-token prediction, targeting entity-level cross-lingual knowledge conductivity — a capability that CLiKA (NAACL 2024) established is not substantially improved by existing multilingual pretraining or instruction tuning (XRR < 0.01). Unlike CCL-XCoT (sentence/paragraph-level contrastive CPT) and Liu & Niehues (ACL 2025, sentence-level middle-layer contrastive fine-tuning), EACA anchors contrastive pairs to Wikidata QIDs using FactNet's 1.7B entity-grounded atomic facts, operating at the entity level — the granularity empirically shown to be the bottleneck for cross-lingual consistency (entity alignment correlates at r > 0.7 with consistency, arXiv:2510.10280). This extends KBioXLM's (EMNLP Findings 2023) precedent of multi-granularity entity alignment in multilingual pretraining from encoder-based masking objectives in a specialized domain to explicit contrastive alignment in decoder-only LLMs for general-domain conductivity. Entity spans are marked with LEIA-style [ENT]/[/ENT] tokens using DaMuEL (12.3B QID-annotated tokens across 53 languages) as the primary annotation source for 10 of 13 target languages, supplemented by a Wikipedia wikilinks-to-QID extraction pipeline for the 3 uncovered Tier 3 languages (SW/YO/KM) and mReFinED entity linking for non-hyperlinked mention gap-filling, with 1.5-2 weeks budgeted for preprocessing. Representations are extracted via mean-pooling at middle layers (~layer 16, validated via Phase 0 sweep). The proposal explicitly addresses the script barrier identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070): script similarity dominates representation sharing (~37.6% same-script CKR vs. <10-20% cross-script), but entity priming disproportionately helps cross-script transfer, motivating entity-level alignment as targeting the right bottleneck. Cross-script QID pairs receive transliteration-augmented entity markers (e.g., [ENT]北京 (Beijing)[/ENT]), inspired by TransliCo (ACL 2024), with mandatory script-grouped evaluation (same-script vs. cross-script gains). Stratified batch construction uses 128-256 entities per batch with class-aware false-negative masking, type-aware hard negatives (~50% same-type entities via Wikidata P31 properties, following Robinson et al. ICLR 2021), and asymmetric positive sets for entities with uneven language coverage (K_min = 3 languages per QID). Joint optimization (L_NTP + λ·L_contrastive, λ=0.1 with warmup) includes gradient conflict monitoring: cosine similarity between NTP and contrastive gradients is tracked every 100 steps, with PCGrad (Yu et al., NeurIPS 2020) activated if conflicts exceed 30% of steps, and GradNorm (Chen et al., ICML 2018) for dynamic λ adjustment if gradient magnitudes diverge beyond 10:1. Inverse-frequency weighting prioritizes low-resource entity-facts. Catastrophic forgetting is mitigated through LoRA (rank 64) on middle layers (10-22), 15% general-domain replay, and cosine LR scheduling. A tiered language selection spans 13 languages across ~7 scripts: Tier 1 (EN/ZH/JA/DE), Tier 2 (AR/HI/TR/ID/VI/TH), Tier 3 (SW/YO/KM), with mandatory Phase 0 FactNet coverage audit and contingency replacements. Phase 0 pilot (500M tokens, 5 languages spanning ≥3 scripts, ~130 H100 hours) includes baselines against sentence-level contrastive (CCL-XCoT), middle-layer sentence contrastive (Liu & Niehues), masking-based entity alignment (KBioXLM-style adaptation), LEIA augmentation, and standard CPT, plus layer sweep, gradient analysis, and script-grouped evaluation. Six key novelties: (1) entity-level contrastive anchoring vs. sentence-level, (2) structured knowledge grounding via FactNet QIDs vs. parallel text, (3) frequency-aware weighting, (4) joint NTP+contrastive optimization with gradient conflict monitoring at entity level during CPT, (5) script-aware transliteration augmentation for cross-script entity alignment, (6) direct targeting of CLiKA's conductivity gap with script-stratified evaluation.\n\n## Core Problem\nCan entity-level contrastive alignment — anchored to Wikidata QIDs and grounded in FactNet's structured atomic facts — improve cross-lingual knowledge conductivity (as defined by CLiKA's XRR metric, Gao et al. NAACL 2024) more effectively than sentence/paragraph-level contrastive continued pretraining (e.g., CCL-XCoT) or sentence-level middle-layer alignment (Liu & Niehues, ACL 2025)? CLiKA established that neither multilingual pretraining nor instruction tuning substantially improves conductivity, with XRR scores below 0.01 for most non-English languages. EACA hypothesizes that this conductivity barrier persists because prior methods align at sentence/document granularity — conflating entity-specific factual knowledge with syntactic and discourse-level variation — whereas factual knowledge is inherently structured around entities (subject-property-object triples). A critical complication, identified by Ifergan et al. (NAACL Findings 2025) and Bandarkar et al. (arXiv:2603.17070), is that script similarity is the dominant factor in cross-lingual representation sharing: high behavioral consistency does not imply shared internal representation for cross-script language pairs, and script match — not language family — is the primary predictor of knowledge transfer failure. Crucially, however, Bandarkar et al.'s entity priming experiment shows that providing source-language entity names disproportionately improves cross-script transfer, directly implicating entity-level mapping failure as the mechanism behind the script barrier. This suggests that entity-level contrastive alignment targets the right bottleneck, but that cross-script entity alignment requires additional support (e.g., transliteration augmentation) beyond what same-script entity alignment needs. EACA therefore addresses a two-level problem: (1) entity-level alignment as the fundamental unit of factual knowledge transfer, and (2) script-aware strategies to bridge the representation gap across writing systems.\n\n## Opportunity\nCCL-XCoT (EMNLP 2025 Findings) demonstrates that contrastive continued pretraining reduces cross-lingual hallucination by up to 62% but operates at sentence/paragraph granularity with parallel text. Liu & Niehues (ACL 2025) show that middle-layer contrastive alignment (layer 16 of 32 in LLaMA-3-8B) significantly improves cross-lingual transfer for downstream tasks, but again at sentence-level granularity and for task-specific fine-tuning rather than factual consistency. CLiKA (NAACL 2024) reveals a critical gap: existing multilingual pretraining and instruction tuning improve surface-level consistency but fail to improve knowledge conductivity (XRR < 0.01), suggesting that fundamentally different alignment granularity is needed. Meanwhile, FactNet (arXiv:2602.03417, Feb 2026) provides 1.7B entity-grounded atomic facts across 316 Wikipedia editions with Wikidata QID linking — enabling entity-level contrastive pairs grounded in structured knowledge. Entity Lens (BlackboxNLP 2025) confirms that decoder LLMs develop entity-specific internal mechanisms to represent multi-token entities. Liu et al. (EMNLP 2025 Findings) show that cross-lingual transfer is frequency-driven, with low-frequency facts benefiting most. Critically, recent evidence from entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) demonstrates that cross-lingual factual consistency correlates strongly with entity alignment (Pearson r > 0.7), with over 99% of consistent facts exhibiting successful entity alignment — providing direct empirical motivation for entity-level rather than sentence-level contrastive objectives. Marco et al. ('Unveiling LLMs', arXiv:2404.03623) further establish that factual knowledge about subject entities concentrates in middle layers (L5-L21 for LLaMA-2-7B). KBioXLM (EMNLP Findings 2023) provides an important precedent: it demonstrated that multi-granularity knowledge alignment (entity masking, relation masking, passage relation prediction) during continued pretraining of XLM-R yields +20 F1 points on cross-lingual zero-shot biomedical tasks, establishing entity-anchored alignment as effective — but using masking-based reconstruction on encoders rather than contrastive loss on decoder LLMs, and targeting downstream task transfer rather than factual conductivity. Ifergan et al. (NAACL Findings 2025) reveal a deeper challenge: using knowledge editing as a probe for representation sharing, they find script similarity is the dominant factor (same-script CKR ~37.6% in Mistral; cross-script <10-20%), and that behavioral consistency diverges sharply from representation sharing for cross-script pairs. Bandarkar et al. (arXiv:2603.17070, March 2026) confirm this with regression analysis showing script match as the primary predictor after controlling for model capability and question difficulty (~13% accuracy gap), but critically, their entity priming experiment shows that providing source-language entity names disproportionately improves cross-script questions — directly implicating entity mapping as the bottleneck. TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers using only 5% of training data on encoders. DaMuEL (2023) provides 12.3B tokens with QID-linked entity annotations across 53 languages, enabling efficient preprocessing for 10 of EACA's 13 target languages. The opportunity is to combine these insights — entity-level anchoring + structured knowledge grounding + middle-layer extraction + inverse-frequency weighting + script-aware strategies — into a contrastive CPT method that targets the specific granularity (entities), representation layer (middle), data regime (low-frequency facts), and script barriers where current methods demonstrably fall short.\n\n## Related Work / Landscape\nThe cross-lingual factual consistency landscape spans several complementary approaches. CCL-XCoT (EMNLP 2025 Findings) is the primary baseline, employing InfoNCE symmetric contrastive loss during continued pretraining with a sentence-to-paragraph curriculum on Gemma-7B and LLaMA-3.1-8B using LoRA on layers 9-19/11-22, reducing hallucination by 62%, but operating at sentence/paragraph granularity without entity grounding or frequency weighting. Liu & Niehues (ACL 2025) represent the closest methodological precedent for contrastive alignment: they apply contrastive loss on mean-pooled sentence representations at middle layers (specifically layer 16 of 32 for LLaMA-3-8B-Instruct) during task-specific fine-tuning with LoRA (rank 8), demonstrating +1.5 F1 on slot filling and +1.5 BLEU on MT across 35 languages — however, they use sentence-level alignment with alternating (not joint) task/alignment training, target downstream task transfer rather than factual consistency, use parallel text rather than structured knowledge, and include no frequency weighting. EACA differentiates from Liu & Niehues on five axes: (1) entity-level rather than sentence-level granularity, (2) continued pretraining for factual consistency rather than task-specific fine-tuning, (3) FactNet-grounded contrastive pairs rather than parallel text, (4) joint NTP+contrastive objective rather than alternating training, and (5) inverse-frequency weighting for underrepresented facts. KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564) is an important precedent for multi-granularity entity-anchored alignment in multilingual pretraining. It performs continued pretraining on XLM-R using three alignment objectives grounded in UMLS biomedical knowledge: entity masking (code-switching entity mentions across EN-CN and predicting masked entity tokens via MLM cross-entropy), relation masking (masking relation tokens in subject-predicate-object triples), and passage relation prediction (3-way classification on aligned EN-CN Wikipedia passages). KBioXLM achieves +20 F1 points on cross-lingual zero-shot biomedical NER/RE. EACA extends this paradigm along four dimensions: (a) decoder-only LLMs vs. encoder (XLM-R), requiring contrastive loss on hidden states rather than masking-based reconstruction, since decoder LLMs lack bidirectional context for effective mask prediction; (b) general domain vs. biomedical, using FactNet's 1.7B facts across 316 editions vs. UMLS's specialized ontology; (c) explicit contrastive alignment (InfoNCE) vs. implicit alignment through masking, directly optimizing cross-lingual entity representation similarity rather than relying on the prediction bottleneck; (d) conductivity metric (CLiKA's XRR) vs. downstream task transfer, targeting the specific capability that prior methods fail to improve. CLiKA (Gao et al., NAACL 2024) provides the diagnostic framework: they define knowledge conductivity as the Cross-Retrieval Ratio (XRR) — retrieving knowledge learned in one language using another — and find that neither multilingual pretraining nor instruction tuning substantially improves XRR (scores < 0.01 for most non-English languages), with no concrete solutions proposed. The entity-level alignment analysis (Liu, Wang et al., arXiv:2510.10280) provides strong empirical support: cross-lingual consistency correlates with entity alignment at r > 0.7, and their SubInj method yields +14-32% recall and +17-44% consistency gains, but only at inference time; EACA aims to achieve this alignment at training time. On the script barrier dimension, Ifergan et al. ('Beneath the Surface of Consistency', NAACL Findings 2025, arXiv:2408.10646) demonstrate via knowledge editing probes on 7 decoder LLMs (7B scale) that script similarity is the dominant factor in cross-lingual knowledge representation sharing (CKR): same-script Latin pairs show ~37.6% average CKR in Mistral, while cross-script pairs show <10-20% transfer; crucially, they find that high behavioral consistency (CKC) does not imply shared representation for cross-script pairs, with E[NCL] consistently exceeding E[NTL]. Even targeted language extension pretraining achieves only marginal cross-script CKR improvement. Bandarkar et al. ('Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts', arXiv:2603.17070, March 2026) confirm via regression analysis on ECLeKTic and MultiLoKo that script match — not language family — is the primary predictor of knowledge transfer failure (~13% accuracy gap), but their entity priming experiment reveals that providing source-language entity names disproportionately improves cross-script questions, directly implicating entity mapping as the cross-script bottleneck. TransliCo (Liu et al., ACL 2024, arXiv:2401.06620) addresses script barriers through transliteration contrastive modeling (TCM), fine-tuning Glot500-m on 5% of data with Latin transliterations as contrastive targets, producing Furina which outperforms Glot500-m on cross-script zero-shot transfer — but operates on encoders at sentence level without entity grounding. Transliteration-based post-training alignment (Moosa et al., EMNLP Findings 2024, arXiv:2406.19759) achieves up to 50% improvement on cross-script English-centric transfer with even larger gains for non-English sources. EACA incorporates this insight by adding transliteration-augmented entity contrastive pairs for cross-script language combinations as a complementary mechanism. NeighXLM (EMNLP 2025 Findings) introduces neighbor-augmented contrastive pretraining for low-resource languages without parallel data, but targets general cross-lingual transfer rather than entity-specific factual consistency. PreAlign (EMNLP 2024) uses code-switching pretraining with word-level alignment but lacks entity anchoring. CrossIC-PT (EMNLP 2025) interleaves bilingual Wikipedia content without entity-level grounding. LEIA (ACL Findings 2024) inserts English entity names with [translate]/[/translate] markers during continued pretraining of decoder LLMs, improving cross-lingual transfer but without contrastive loss or frequency weighting. EntityCS (EMNLP Findings 2022) performs entity-centric code switching with Wikidata but is limited to encoder-only models. Entity Lens (BlackboxNLP 2025) reveals that decoder LLMs develop entity-specific mechanisms to represent and manipulate multi-token entities via task vectors. The middle-layer factual knowledge claim is supported by Liu & Niehues (ACL 2025) showing layer 16 of 32 has strongest cross-lingual retrieval alignment, and Marco et al. (arXiv:2404.03623) demonstrating via dynamic knowledge graphs that middle layers (L5-L21) encode comprehensive factual knowledge while late layers show 90%+ degradation. ELO (arXiv:2601.03648, Jan 2026) demonstrates efficient layer-specific optimization with 6.46x speedup from selective middle-layer updates. FactNet (arXiv:2602.03417) provides 1.7B entity-grounded facts across 316 Wikipedia editions with significant coverage skew. CLM-Bench (arXiv:2601.17397) shows edit vectors are nearly orthogonal across languages, further motivating entity-level alignment. DCO (arXiv:2603.04678, March 2026) proposes DPO-inspired post-hoc consistency optimization, complementary to pretraining-time methods. Veitsman et al. (arXiv:2603.18863, March 2026) find that sentence-level contrastive alignment fails for token-level tasks in XLM-R encoders, supporting entity-level approaches for entity-centric tasks. Cultural knowledge asymmetry research (ACL 2025) confirms that frequency drives cross-lingual transferability.\n\n## Approach\nEACA adds an InfoNCE contrastive loss on entity-span hidden states to the standard next-token prediction (NTP) objective during continued pretraining. The method comprises five integrated components: entity preprocessing, entity-level contrastive alignment, script-aware augmentation, stratified batch construction, and joint optimization with gradient monitoring.\n\n**1. Entity Preprocessing Pipeline.** Entity boundary annotation uses a two-stage pipeline. Stage 1 (primary): DaMuEL (2023), which provides 12.3B QID-annotated tokens across 53 languages (CC BY-SA), is used directly for the 10 target languages it covers (EN/ZH/JA/DE/AR/HI/TR/ID/VI/TH). DaMuEL provides start/end token indices per entity mention with Wikidata QID links, extracted from Wikipedia wikilinks and expanded via lemmatization and alias matching (~17% recall gain over raw wikilinks). Stage 2 (Tier 3 gap-filling): For the 3 Tier 3 languages not covered by DaMuEL (SW/YO/KM), a lightweight Wikipedia wikilinks extraction pipeline resolves hyperlinks to QIDs via Wikidata sitelinks (~50-60% mention coverage). mReFinED (EMNLP Findings 2023), which is 44-60x faster than comparable entity linkers, is applied as a second pass on high-resource languages to annotate non-hyperlinked entity mentions where higher recall is needed. Entity boundaries are marked with LEIA-style [ENT]/[/ENT] tokens around linked mentions. Preprocessing budget: 1.5-2 weeks engineering time, ~2-4 GPU-days on A100 for mReFinED gap-filling, ~24-48 CPU-hours for wikilinks extraction across Tier 3 languages. This pipeline is on the critical path and must complete before Phase 0.\n\n**2. Entity-Level Contrastive Alignment.** Entity representations are extracted via mean-pooling over hidden states within the [ENT]...[/ENT] span at a designated middle layer (defaulting to layer 16 for 32-layer models based on Liu & Niehues' ACL 2025 finding and Marco et al.'s analysis; validated via Phase 0 sweep over layers 12-20), with loss propagation blocked on boundary markers themselves. Contrastive pairs are constructed per QID from FactNet: positive pairs consist of atomic fact descriptions for the same QID across languages, while negatives come from different QIDs within the same batch (detailed in Component 4). Inverse-frequency weighting assigns higher contrastive loss weight to facts with lower cross-lingual FactNet coverage, directly targeting low-resource facts where CLiKA's conductivity analysis shows the largest gap.\n\nTheoretical motivation for entity-level granularity: Three converging lines of evidence support entity-level over sentence-level contrastive alignment for factual consistency: (1) Entity alignment analysis (arXiv:2510.10280) demonstrates Pearson r > 0.7 between entity alignment and cross-lingual consistency, with >99% of consistent facts showing successful entity alignment — establishing entities as the bottleneck for consistency; (2) CLM-Bench's finding that cross-lingual edit vectors are nearly orthogonal implies that factual knowledge editing, which operates at entity-level (subject-property-object triples), requires entity-aligned representations rather than sentence-aligned ones; (3) CLiKA's failure result — that sentence/document-level pretraining and instruction tuning do not improve conductivity — suggests that coarser-grained alignment conflates entity-specific factual knowledge with syntactic and discourse-level variation, diluting the alignment signal.\n\n**3. Script Barrier Mitigation.** EACA's 13 target languages span ~7 scripts (Latin: EN/DE/TR/ID/VI/SW/YO; CJK: ZH/JA; Arabic: AR; Devanagari: HI; Thai: TH; Khmer: KM). Ifergan et al. (NAACL Findings 2025) demonstrate that cross-lingual representation sharing (CKR) clusters strongly by script family (~37.6% same-script CKR vs. <10-20% cross-script in Mistral-7B), and Bandarkar et al. (arXiv:2603.17070) confirm script match as the primary predictor of transfer failure (~13% gap). This poses a genuine risk that entity-level contrastive alignment may primarily improve same-script entity alignment while showing limited gains for cross-script pairs. However, two findings provide grounds for cautious optimism: (a) Bandarkar et al.'s entity priming experiment shows source-language entity names disproportionately improve cross-script transfer, implicating entity mapping — not script-level representation — as the cross-script bottleneck for factual knowledge; (b) TransliCo (ACL 2024) demonstrates that transliteration-based contrastive learning bridges script barriers on encoders using only 5% of training data. EACA therefore incorporates a script-aware augmentation strategy: for cross-script QID pairs (e.g., EN-ZH, EN-AR, EN-HI, EN-TH, EN-KM), entity mentions in non-Latin scripts are supplemented with Latin transliterations appended within the [ENT] boundary (e.g., [ENT]北京 (Beijing)[/ENT]), providing a lexical bridge for the contrastive objective. This is tested as an ablation (EACA vs. EACA+translit) to isolate the contribution of transliteration augmentation beyond entity-level alignment. The evaluation plan includes mandatory script-grouped analysis: same-script entity alignment gains (Latin-Latin, CJK-CJK) vs. cross-script gains (Latin-CJK, Latin-Arabic, Latin-Devanagari, etc.), reporting both entity cosine similarity and downstream factual consistency metrics separately for each script-pair category. If Phase 0 reveals that cross-script entity alignment gains are <50% of same-script gains despite transliteration augmentation, this will be explicitly reported as a limitation and the analysis will quantify what fraction of EACA's overall conductivity improvement comes from same-script vs. cross-script alignment.\n\n**4. Stratified Batch Construction with Type-Aware Hard Negatives.** Effective contrastive learning is highly sensitive to negative quality (Robinson et al., ICLR 2021). EACA uses stratified mini-batching: each batch contains K_batch = 128-256 unique QIDs, with all available language instances per QID forming the positive set (asymmetric positive sets accommodate QIDs present in only 2-3 languages without dropping them). Minimum language coverage per QID is K_min = 3 languages; QIDs with fewer than 3 language instances are filtered during preprocessing. Class-Aware Masking (CAM) ensures that all instances of the same QID are excluded from the InfoNCE denominator, preventing false-negative contamination. For hard negative mining, type-aware stratification ensures ~50% of in-batch negatives share the anchor entity's Wikidata type (e.g., Q5/human, Q515/city, Q4830453/organization) — forcing the model to discriminate on fine-grained entity identity rather than coarse type. This is implemented via Wikidata instance-of (P31) properties, grouping entities into 8-10 macro-types for sampling. The remaining ~50% are random negatives for diversity. Batch composition is balanced across script families to ensure cross-script contrastive signals appear in every batch. The InfoNCE loss for entity e with QID q is: L_entity(q) = -log[exp(sim(h_q^i, h_q^j)/τ) / (exp(sim(h_q^i, h_q^j)/τ) + Σ_{k≠q} exp(sim(h_q^i, h_k)/τ))], where h_q^i, h_q^j are entity representations from different languages for the same QID, and h_k are representations from different QIDs, with τ = 0.07 as the temperature (tuned in Phase 0 over {0.05, 0.07, 0.1}).\n\n**5. Joint Optimization with Gradient Monitoring.** The joint objective is L_total = L_NTP + λ * L_entity_contrastive, with λ initialized at 0.1 (following guidance from headless LM work showing λ ∈ [0.01, 0.1] is appropriate for contrastive + generation joint training during CPT). A potential tension exists: NTP learns language-specific token distributions while contrastive loss pulls entity representations together across languages. Unlike Liu & Niehues' alternating approach, EACA uses joint optimization to ensure entity alignment co-adapts with the language modeling objective — but addresses gradient conflict risk through three mechanisms: (a) Phase 0 gradient analysis: cosine similarity between ∇L_NTP and ∇L_entity_contrastive is computed every 100 steps on the shared LoRA parameters. If gradient cosine similarity is negative for >30% of monitored steps, PCGrad projection (Yu et al., NeurIPS 2020) is applied — projecting the contrastive gradient onto the normal plane of the NTP gradient to eliminate destructive interference. (b) GradNorm (Chen et al., ICML 2018) is implemented as an optional dynamic λ adjustment mechanism: if the gradient magnitude ratio between the two losses drifts beyond 10:1, GradNorm normalizes to equalize learning rates. (c) λ warmup: contrastive loss weight ramps linearly from 0 to λ_target over the first 10% of training steps, allowing NTP to stabilize before contrastive pressure is introduced. Phase 0 reports gradient conflict frequency, cosine similarity distribution, and whether PCGrad/GradNorm activation was required — this informs the full training configuration. If gradient conflicts are severe (>50% of steps) even with PCGrad, the fallback is alternating optimization (NTP steps → contrastive steps per batch) following Liu & Niehues' validated approach.\n\nCatastrophic forgetting is mitigated through three mechanisms: (a) LoRA (rank 64) applied to middle layers only (layers 10-22), following CCL-XCoT's selective layer approach and ELO's findings that first/last layers are critical for general capabilities; (b) 15% general-domain English replay data mixed into training batches; (c) cosine learning rate schedule with linear warmup (peak LR 2e-5). Language selection follows a tiered strategy: Tier 1 comprises 4 anchor languages (EN/ZH/JA/DE, >1M entity-fact pairs), Tier 2 includes 6 mid-resource languages (AR/HI/TR/ID/VI/TH, 100K-1M pairs), and Tier 3 covers 3 low-resource languages (SW/YO/KM). Tier 3 viability assessment based on Wikipedia article counts (SW: ~117K, YO: ~37K, KM: ~12K) and FactNet's 0.36 low-resource yield rate estimates approximately 50K-200K entity-fact pairs for Swahili, 15K-60K for Yoruba, and 5K-25K for Khmer. None of the Tier 3 languages are covered by DaMuEL, so all three rely on the Wikipedia wikilinks extraction pipeline (Stage 2 above). A mandatory FactNet coverage audit in Phase 0 will report exact entity-fact pair counts for all 13 languages; minimum viable threshold is set at 10K entity-fact pairs per language (sufficient for contrastive batching at size 128-256 with adequate negative diversity). If any Tier 3 language falls below threshold, contingency replacements include Bengali (BN, ~157K Wikipedia articles), Tagalog (TL, ~115K articles), or Hausa (HA, ~8K articles but stronger NLP benchmark coverage). Languages below 25K pairs receive LEIA-style English entity augmentation to supplement contrastive pairs.\n\nPhase 0 pilot uses 500M tokens across 5 languages (3 Tier-1 + 2 Tier-2, selected to span at least 3 scripts for script barrier analysis) for approximately 130 H100 hours, with baselines including: (a) CCL-XCoT-style sentence-level contrastive CPT, (b) Liu & Niehues-style middle-layer sentence-level contrastive alignment (the closest methodological comparison, testing entity-level vs. sentence-level at the same middle layer), (c) LEIA-style entity augmentation without contrastive loss, (d) standard CPT, and (e) KBioXLM-style entity masking adaptation (masking [ENT]-bounded tokens and predicting via NTP, without contrastive loss — testing contrastive vs. masking-based entity alignment on decoders). Phase 0 additionally includes: a layer sweep (layers 12, 14, 16, 18, 20) to empirically determine optimal entity extraction depth; gradient conflict analysis (cosine similarity monitoring, PCGrad activation rate); and script-grouped entity alignment analysis (same-script vs. cross-script gains). Go/no-go criteria require entity cosine similarity improvement of at least 0.05, BMLAMA-53 consistency improvement of at least 2 points, no TyDiQA degradation beyond 1 point, AND gradient conflict rate below 50% (with or without PCGrad). Full training processes 1.5-2.5B tokens on LLaMA-3.1-8B (primary) and Gemma-7B (secondary, for CCL-XCoT comparability) across all 13 languages. A complementary EACA+DCO experiment tests whether pretraining-time and post-hoc consistency methods yield cumulative gains. Evaluation covers BMLAMA-53, TyDiQA-GoldP, X-CODAH, LiveCLKTBench, and CLiKA's XRR metric (to directly measure conductivity improvement), plus entity representation cosine similarity analysis. All metrics are reported with script-grouped breakdowns (same-script pairs, cross-script pairs, overall) as a mandatory analysis dimension. Ablations cover: entity-level vs. sentence-level contrastive (the central hypothesis), contrastive vs. masking-based entity alignment (EACA vs. KBioXLM-style adaptation), EACA vs. EACA+transliteration augmentation (script barrier mitigation), frequency weighting on/off, type-aware vs. random negatives, number of languages, layer selection, joint vs. alternating training, gradient conflict mitigation (none vs. PCGrad vs. GradNorm), contrastive pair construction (FactNet-grounded vs. parallel-text-based), and K_min language threshold (2 vs. 3 vs. 5).\n\n## Inspiration\nCCL-XCoT contrastive CPT framework (EMNLP 2025 Findings) + Liu & Niehues middle-layer contrastive alignment (ACL 2025) + FactNet entity-grounded facts (arXiv:2602.03417) + LEIA entity boundary markers (ACL 2024) + CLiKA conductivity diagnostic (NAACL 2024) + Entity-level alignment in crosslingual consistency (arXiv:2510.10280) + Entity Lens entity-specific mechanisms (BlackboxNLP 2025) + Marco et al. middle-layer factual knowledge (arXiv:2404.03623) + ELO selective layer optimization (arXiv:2601.03648) + Liu et al. frequency-driven transfer (EMNLP 2025) + CLM-Bench orthogonal edit vectors (arXiv:2601.17397) + cultural knowledge asymmetry frequency hypothesis (ACL 2025) + Ifergan et al. script-CKR dominance (NAACL Findings 2025) + Bandarkar et al. script barrier in reasoning models (arXiv:2603.17070) + TransliCo transliteration-contrastive script bridging (ACL 2024) + KBioXLM multi-granularity entity alignment (EMNLP Findings 2023) + DaMuEL QID-annotated corpus (2023) + Robinson et al. hard negative mining (ICLR 2021) + PCGrad gradient surgery (NeurIPS 2020) + GradNorm dynamic loss weighting (ICML 2018)\n\n## Key References\n- CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer Method for Mitigating Hallucination Generation (EMNLP Findings 2025)\n- Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs [Liu & Niehues] (ACL 2025, arXiv:2502.14830)\n- Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly [CLiKA] (NAACL 2024, arXiv:2404.04659)\n- On the Entity-Level Alignment in Crosslingual Consistency [Liu, Wang et al.] (arXiv:2510.10280)\n- FactNet: A Billion-Scale Knowledge Graph for Multilingual Factual Grounding (arXiv 2026)\n- LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation (ACL Findings 2024)\n- On the Representations of Entities in Auto-regressive Large Language Models [Entity Lens] (BlackboxNLP 2025, arXiv:2510.09421)\n- Unveiling LLMs: The Evolution of Latent Representations in a Dynamic Knowledge Graph [Marco et al.] (arXiv:2404.03623)\n- Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs [Ifergan et al.] (NAACL Findings 2025, arXiv:2408.10646)\n- Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts [Bandarkar et al.] (arXiv:2603.17070, March 2026)\n- TransliCo: A Contrastive Learning Framework to Address the Script Barrier in Multilingual Pretrained Language Models (ACL 2024, arXiv:2401.06620)\n- Breaking the Script Barrier in Multilingual Pre-Trained Language Models with Transliteration-Based Post-Training Alignment [Moosa et al.] (EMNLP Findings 2024, arXiv:2406.19759)\n- KBioXLM: A Knowledge-anchored Biomedical Multilingual Pretrained Language Model [Geng et al.] (EMNLP Findings 2023, arXiv:2311.11564)\n- DaMuEL: A Large Multilingual Dataset for Entity Linking (arXiv:2306.09288, 2023)\n- Contrastive Learning with Hard Negative Samples [Robinson et al.] (ICLR 2021)\n- Gradient Surgery for Multi-Task Learning [PCGrad, Yu et al.] (NeurIPS 2020)\n- GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks [Chen et al.] (ICML 2018)\n- mReFinED: An Efficient End-to-End Multilingual Entity Linking Model (EMNLP Findings 2023)\n- NeighXLM: Enhancing Cross-Lingual Transfer in Low-Resource Languages via Neighbor-Augmented Contrastive Pretraining (EMNLP Findings 2025)\n- mLUKE: The Power of Entity Representations in Multilingual Pretrained Language Models (ACL 2022)\n- ELO: Efficient Layer-Specific Optimization for Continual Pretraining of Multilingual LLMs (arXiv 2026)\n- Tracing Multilingual Factual Knowledge Acquisition in Pretraining (EMNLP Findings 2025)\n- PreAlign: Boosting Cross-Lingual Transfer by Early Establishment of Multilingual Alignment (EMNLP 2024)\n- Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training [CrossIC-PT] (EMNLP 2025)\n- Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025)\n- EntityCS: Improving Zero-Shot Cross-lingual Transfer with Entity-Centric Code Switching (EMNLP Findings 2022)\n- Optimizing Language Models for Crosslingual Knowledge Consistency [DCO] (arXiv 2026)\n- Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models [BMLAMA] (EMNLP 2023)\n- LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs (arXiv 2025)\n- Why Better Cross-Lingual Alignment Fails for Better Cross-Lingual Transfer: Case of Encoders [Veitsman et al.] (arXiv 2026)\n- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026)\n- DoLa: Decoding by Contrasting Layers Improves Factuality and Faithfulness of Large Language Models (ICLR 2024)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '1100-1550 H100 (Preprocessing: ~10-15 GPU-days A100 for mReFinED; Phase 0: ~130 including layer sweep + gradient analysis; Full training: ~800-1100; Evaluation: ~70; Ablations: ~90-165 including script/masking/gradient ablations)', 'timeline': '4.5-5.5 months (includes 1.5-2 weeks preprocessing pipeline)', 'estimated_gpu_cost': '$2,200-3,100 (at ~$2/H100-hr spot)'}\n- **human_in_loop**: {'gpu_hours': '900-1250 H100', 'timeline': '3.5-4.5 months', 'claude_api_cost': '$300-450 (FactNet coverage audit, DaMuEL integration, preprocessing pipeline, gradient analysis visualization, evaluation analysis, paper drafting)', 'estimated_gpu_cost': '$1,800-2,500'}\n- **auto_research**: {'gpu_hours': '1100-1600 H100', 'timeline': '3-4 months', 'claude_api_cost': '$600-950 (full pipeline automation: DaMuEL integration + mReFinED gap-filling + Tier 3 wikilinks pipeline + FactNet coverage audit + Tier 3 viability check, entity marker insertion, layer sweep, gradient analysis, hyperparameter sweep, script-grouped analysis, ablation analysis, paper writing)', 'estimated_gpu_cost': '$2,200-3,200', 'speed_bottleneck': 'Preprocessing pipeline (1.5-2 weeks) is on critical path before Phase 0; Phase 0 pilot (2-3 weeks including layer sweep, gradient analysis, and script-grouped evaluation) must complete before full training; full training wallclock ~30-50 hours per run on 8xH100; sequential dependency: preprocessing → FactNet audit gates Tier 3 language selection → pilot go/no-go gates full training'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T21:12:16.459Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:12:16.459Z",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T21:12:16.470Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

⚠️ 【致命性前置问题：venue mismatch】
CoRL 2026 (Conference on Robot Learning) 的 scope 明确限定在 robotics + machine learning 交叉领域。
其 Call for Papers 原文声明："Submissions without a robotics focus will be returned without review."
本 proposal 研究的是多语言 LLM 中的跨语言知识传导性 (cross-lingual knowledge conductivity)，
与机器人学没有任何关联。投稿 CoRL 会被直接 desk reject。
本 proposal 的合理目标会议是 ACL / EMNLP / NAACL / EACL 等 NLP 主会。

以下评审基于 "假设投稿至合适的 NLP 主会 (如 ACL/EMNLP)" 进行，以便提供有意义的反馈。

【领域调研】:
- CLiKA (Gao et al., NAACL 2024, arXiv:2404.04659): 建立了跨语言知识对齐的三层框架
  (Performance / Consistency / Conductivity)，发现现有多语言预训练和指令微调均未实质
  改善 conductivity (XRR < 0.01)。本 proposal 直接针对此 gap。论文真实存在，描述准确。

- CCL-XCoT (EMNLP Findings 2025, arXiv:2507.14239): 句/段粒度对比持续预训练，在 
  Gemma-7B/LLaMA-3.1-8B 上将跨语言幻觉率降低最多 62%。论文真实存在，描述准确。
  本 proposal 的直接 baseline。

- Liu & Niehues (ACL 2025, arXiv:2502.14830): 中间层句子级对比对齐用于跨语言迁移，
  发现 layer 16/32 的跨语言检索对齐最强。论文真实存在，描述准确。
  本 proposal 声称在 granularity（entity vs. sentence）和目标（conductivity vs. task 
  transfer）上差异化，成立。

- KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564): 在 XLM-R（encoder）上
  用 entity masking + relation masking + passage relation prediction 进行多粒度知识锚定
  CPT，生物医学域零样本跨语言 NER/RE 提升 ~20 F1。论文真实存在，描述准确。
  本 proposal 声称是将此范式从 encoder + masking 扩展到 decoder + contrastive。

- Entity-level alignment in cross-lingual consistency (Liu, Wang et al., arXiv:2510.10280): 
  证明 entity alignment 与跨语言一致性 Pearson r > 0.7，>99% 一致事实成功 entity 
  alignment；SubInj 方法在推理时获得 +14-32% recall、+17-44% consistency。
  论文真实存在。**关键：此论文已展示 inference-time entity alignment intervention 
  有显著效果，构成本 proposal 的 trivial alternative 威胁。**

- FactNet (arXiv:2602.03417, Feb 2026): 1.7B entity-grounded atomic facts，覆盖 316 
  Wikipedia editions，grounding precision 92.1%。论文真实存在，描述准确。

- Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646): 知识编辑探针证明 script 
  similarity 主导跨语言表示共享 (~37.6% same-script CKR vs. <10-20% cross-script)。
  论文真实存在。

- Bandarkar et al. (arXiv:2603.17070, March 2026): script match 是知识迁移失败的主要
  预测因子 (~13% gap)；entity priming 不成比例地改善跨脚本问题。论文真实存在，
  描述准确。

- TransliCo (ACL 2024, arXiv:2401.06620): 在 Glot500-m encoder 上用 5% 数据做 
  transliteration contrastive learning 产出 Furina，改善跨脚本零样本迁移。
  论文真实存在。encoder-only，句子级，无 entity grounding。

- DaMuEL (arXiv:2306.09288, 2023): 53 语言 12.3B tokens QID-linked entity 
  annotations。论文真实存在，描述准确。

- 调研总结: 跨语言事实一致性是一个活跃领域。CCL-XCoT（句子级对比 CPT）和 Liu & 
  Niehues（中间层句子级对比）代表当前 SOTA 方法论；CLiKA 确立了 conductivity gap；
  entity alignment 与 consistency 的高相关性已被实证。本 proposal 位于这些工作的
  自然交汇点——从 sentence-level 下沉到 entity-level 的对比对齐。这一步在逻辑上
  连贯，但在 novelty 层面更接近"组合型创新"（recombination）而非"概念型突破"。

【Trivial Alternative 检验】:
存在显著的 trivial alternative 威胁：

1. **Inference-time entity intervention (SubInj)**: Liu, Wang et al. (arXiv:2510.10280) 
   已证明在推理时注入英语实体名称即可获得 +14-32% recall 和 +17-44% consistency 
   提升，且无需任何训练。EACA 需要 ~1100-1600 H100-hours 的训练成本才能实现
   training-time 的 entity alignment——如果 EACA 的增量收益相对于 SubInj 不显著，
   整个方法的 cost-effectiveness 会被严重质疑。

2. **LEIA-style entity augmentation (无 contrastive loss)**: 本 proposal 自己将 LEIA 
   列为 ablation baseline。如果仅在 CPT 中插入 [ENT]...[/ENT] 标记（不加 contrastive 
   loss）就能获得大部分收益，那么对比损失的增量价值存疑。

3. **EACA 相对于 CCL-XCoT 的增量**: CCL-XCoT 已经在句子粒度实现 62% 幻觉率降低。
   EACA 声称 entity-level 更好，但这个 claim 尚未有任何实证，而 CCL-XCoT 已有
   实验结果。如果 entity-level 的边际改进不大（比如从 62% 到 68%），付出的工程
   复杂度（entity preprocessing pipeline、QID grounding、type-aware negatives 等）
   难以 justify。

增量价值的成立条件：EACA 必须显著优于 (a) SubInj inference-time intervention、
(b) LEIA-style entity augmentation without contrastive loss、(c) CCL-XCoT 
sentence-level contrastive。三重门槛，每一个都不轻松。

【前提假设检验】:
核心 claim 的逻辑链中有以下未经验证的关键假设：

1. **"相关性 → 因果性" 跳跃**: entity alignment 与 consistency 的 r > 0.7 相关性
   是 observational evidence。Proposal 隐含假设 "改善 entity alignment 会 cause 
   consistency improvement"，但这可能是共同因果（例如训练数据覆盖度同时影响两者）。
   **目前没有因果干预实验证明 training-time entity alignment improvement → 
   consistency improvement 的因果链。**

2. **"Entity-level 粒度优于 sentence-level" 的假设缺乏直接实证**: CLiKA 证明了
   sentence/document-level methods 不 work，但 "因此 entity-level 会 work" 是
   逻辑跳跃。失败可能不仅仅是粒度问题——也可能是对比损失本身不够、数据量不够、
   或者 decoder LLM 的 representation geometry 就不适合通过对比学习改变。

3. **Decoder LLM 上 entity-level contrastive loss 的可行性假设**: KBioXLM 在 
   encoder (XLM-R) 上有效不意味着 decoder LLM 上同样有效。Decoder LLM 的表示
   空间是 autoregressive 的，causal attention 意味着 entity span 的表示只能看到
   左侧上下文——这与 encoder 的双向上下文截然不同。mean-pooling 一个只有左侧
   上下文的 entity span 是否能产生有意义的 entity representation？这是一个非平凡
   假设，Entity Lens 的发现（decoder LLMs develop entity-specific mechanisms）
   提供了部分支撑，但不足以完全消除疑虑。

4. **FactNet 覆盖的均匀性假设**: Proposal 承认 FactNet 有 "significant coverage 
   skew"，但整个方法依赖于低资源语言有足够的 entity-fact pairs 来构建对比训练。
   如果 Tier 3 语言的实体覆盖极低（如 Khmer 可能只有 5K-25K pairs），对比学习
   的有效性会打折。

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是将 entity-level 粒度引入跨语言对比 CPT for decoder LLMs。但这更像是
   已有组件的重新组合，而非新概念：
   - Entity-level alignment in multilingual pretraining: KBioXLM (EMNLP Findings 2023) 
     已做过，只是在 encoder + masking 上
   - Contrastive CPT for cross-lingual consistency: CCL-XCoT (EMNLP Findings 2025) 
     已做过，只是在 sentence-level
   - Middle-layer contrastive alignment: Liu & Niehues (ACL 2025) 已做过
   - Script barrier + transliteration: TransliCo (ACL 2024) 已做过
   - Entity boundary markers: LEIA (ACL Findings 2024) 已做过
   
   EACA 的 novelty delta 是 "在 decoder LLM 的中间层对 entity span 做 InfoNCE 
   contrastive CPT，用 FactNet QIDs 构建对比对"。这是一个具体的 engineering 
   组合，但审稿人可能会认为这是 "obvious next step given the existing literature"
   —— 一旦知道 entity alignment 是 bottleneck（2510.10280）+ 中间层对比有效
   （Liu & Niehues）+ 对比 CPT 有效（CCL-XCoT），entity-level 对比 CPT at 
   middle layers 几乎是不需要 insight 就能提出的方案。
   
   Proposal 列出的 "6 key novelties" 中多数是工程选择（frequency weighting、
   gradient monitoring、script-aware evaluation）而非概念创新。

2. **Significance: 中** — 
   研究问题本身重要：CLiKA 揭示的 conductivity gap (XRR < 0.01) 是一个真实且
   有影响力的问题（NAACL 2024）。跨语言知识一致性对多语言 LLM 的实际部署至关
   重要。但几个因素限制了 significance 的上界：
   - 如果 positive result，审稿人的反应更可能是 "makes sense, entity-level should 
     help" 而不是 "surprising"——因为 entity alignment 作为 bottleneck 已经被
     2510.10280 充分论证过了
   - 方法的可推广性受限于 FactNet + DaMuEL 数据的可用性——对于没有足够 Wikipedia 
     覆盖和 Wikidata QID 链接的语言（真正的低资源语言），这个方法不直接适用
   - 如果 negative result（entity-level 没有比 sentence-level 好多少），贡献变为
     一个 negative finding，其发表价值取决于 analysis quality

3. **Related Work: 强** — 
   这是本 proposal 的最强维度。Related work 覆盖极其全面：
   - 直接竞争工作（CCL-XCoT、Liu & Niehues、KBioXLM）均被详细讨论，差异化清晰
   - Script barrier 文献（Ifergan et al.、Bandarkar et al.、TransliCo）覆盖充分
   - 所引论文经调研均真实存在，描述基本准确
   - FactNet、DaMuEL、LEIA 等基础设施型工作引用合理
   - 差异化定位（5 axes vs. Liu & Niehues、4 dimensions vs. KBioXLM）表述清晰
   唯一潜在遗漏：可能需要更多讨论 inference-time entity intervention（SubInj 等）
   作为 trivial baseline 的对比 positioning。

【概率估计】: [15% - 25%] 中位 20%
（注：此概率基于投稿 NLP 主会如 ACL/EMNLP。投稿 CoRL 的概率为 ~0%，会被 desk reject。）

【估计理由】: 
从 3 维度到概率的推理：
- Related Work 很强，意味着作者对领域有深入理解，这是基础保障
- Significance 中等，问题重要但预期发现不 surprising
- Novelty 弱-中，是限制上界的关键因素——组合型创新 + "obvious next step" 风险高

Novelty 是限制上界的主要维度。对于 ACL/EMNLP 主会，审稿人会问：
"KBioXLM + CCL-XCoT + Liu & Niehues 三篇已有论文的自然结合，这里面的 intellectual 
contribution 是什么？"如果答案仅是 "我们第一个在 decoder LLM 上做 entity-level 
contrastive CPT"，这是 execution novelty 而非 conceptual novelty，对 top venue 
来说偏弱。

同时，trivial alternative 威胁（SubInj 推理时介入 vs. 昂贵的对比 CPT）进一步
压低了评估——审稿人有很自然的 pushback 角度。

如果实验能证明 EACA 显著优于 SubInj 且优于 CCL-XCoT，概率可以上升到 ~30%。
但那是实验层面的事，入口阶段只评 idea 本身。

【主要风险】:
1. **"Obvious next step" 质疑**: 核心贡献是已有方法的粒度迁移（sentence→entity）+ 
   场景迁移（encoder→decoder），审稿人可能认为 intellectual contribution 不足以
   支撑 top venue 主会论文。Proposal 自身列出的 "6 key novelties" 反而暴露了这个
   问题——需要列 6 个 novelties 通常意味着没有一个足够强的单一贡献。

2. **Trivial alternative 未被充分 address**: SubInj (arXiv:2510.10280) 已在推理时
   以零训练成本实现 entity-level alignment 的显著提升。Proposal 如果不能在 framing 
   中明确论证为什么 training-time alignment 相对于 inference-time intervention 有
   不可替代的优势（beyond "training-time is more elegant"），审稿人会认为 EACA 
   是一个过度工程化的解决方案。
```

Sources:
- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)
- [CLiKA - arXiv](https://arxiv.org/html/2404.04659)
- [CCL-XCoT - EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.93/)
- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)
- [Liu & Niehues - arXiv](https://arxiv.org/abs/2502.14830)
- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)
- [Entity-Level Alignment in Cross-lingual Consistency](https://arxiv.org/pdf/2510.10280)
- [FactNet - arXiv 2026](https://arxiv.org/abs/2602.03417)
- [Ifergan et al. - NAACL Findings 2025](https://www.semanticscholar.org/paper/Beneath-the-Surface-of-Consistency:-Exploring-in-Ifergan-Choshen/54a2e0dad730c1a955c66f3568a3fa0dca400225)
- [Bandarkar et al. - arXiv 2603.17070](https://arxiv.org/abs/2603.17070)
- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)
- [DaMuEL - arXiv](https://arxiv.org/abs/2306.09288)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make my assessment. Let me compile the analysis.

---

```
【阶段】: Triage
```

## ⚠️ 重大前置问题：投稿 venue 严重不匹配

**CoRL（Conference on Robot Learning）是机器人学习会议**，其 Call for Papers 明确要求论文聚焦于"core robotics problem"，鼓励 real-robot experiments 或 sim-to-real transfer 证据。本 proposal 是一篇纯粹的多语言 NLP 工作（cross-lingual knowledge conductivity via entity contrastive alignment），与机器人学习**完全无关**。投到 CoRL 会被 desk reject。

**应投稿的正确 venue**：ACL / EMNLP / NAACL / EACL 主会或 Findings，或 COLM / ICLR。以下评估基于投稿到 NLP/CL 顶会（如 ACL/EMNLP）的假设进行。

---

```
【领域调研】:
```

- **[CLiKA] Gao et al. (NAACL 2024, arXiv:2404.04659)**: 定义了 cross-lingual knowledge conductivity 的 XRR 指标，发现现有多语言预训练和指令微调均无法实质性提升 conductivity（XRR < 0.01）。**这是 EACA 立项的根基，论文确实存在且描述准确。CLiKA 仅提出诊断，未提出解决方案——这为 EACA 留出了空间。**

- **[CCL-XCoT] Zheng et al. (EMNLP Findings 2025)**: 在 Gemma-7B/LLaMA-3.1-8B 上用 sentence-to-paragraph 级别的 InfoNCE + NTP joint CPT，减少 hallucination 62%。**是 EACA 的主要 baseline——EACA 的核心 claim 是 entity-level 比 sentence/paragraph-level 更有效。CCL-XCoT 确实存在。**

- **[Liu & Niehues] (ACL 2025, arXiv:2502.14830)**: 在 LLaMA-3-8B middle layer（layer 16）做 sentence-level contrastive alignment 用于 task-specific fine-tuning，证明中间层是跨语言对齐的最佳位置。**EACA 借用了其 middle-layer 的发现但改为 entity-level。确实存在。**

- **[Ifergan et al.] (NAACL Findings 2025, arXiv:2408.10646)**: 通过 knowledge editing 探测发现 script similarity 是 representation sharing 的主导因素（same-script CKR ~37.6% vs cross-script <10-20%）。**确实存在，描述准确。**

- **[Bandarkar et al.] (arXiv:2603.17070, March 2026)**: 发现 script match 是知识迁移失败的主要预测因子（~13% gap），但 entity priming 实验表明提供源语言 entity names 能不成比例地提升 cross-script 问题准确率。**确实存在，且"entity priming disproportionately helps cross-script"的描述准确——这是 EACA entity-level alignment 最重要的实证动机之一。**

- **[FactNet] (arXiv:2602.03417, Feb 2026)**: 1.7B entity-grounded atomic facts，316 Wikipedia editions，92.1% grounding precision。**确实存在，是 EACA 的核心数据基础设施。**

- **[KBioXLM] Geng et al. (EMNLP Findings 2023, arXiv:2311.11564)**: 在 XLM-R encoder 上用 entity masking + relation masking + passage relation prediction 做生物医学领域多语言 CPT，cross-lingual zero-shot +20 F1。**确实存在。EACA 的定位是将此范式从 encoder/masking/specialized-domain 扩展到 decoder/contrastive/general-domain。**

- **[TransliCo] (ACL 2024, arXiv:2401.06620)**: 在 Glot500-m encoder 上用 transliteration contrastive learning 仅用 5% 数据桥接 script barrier。**确实存在，但仅作用于 encoder。EACA 将 transliteration augmentation 作为跨脚本辅助策略。**

- **[arXiv:2510.10280] Liu, Wang et al.**: Entity alignment 与 crosslingual consistency 的 Pearson r > 0.7 相关性，>99% 一致性 facts 有成功的 entity alignment。**确实存在。这是 EACA"entity 是瓶颈"claim 的最关键实证依据。**

- **调研未发现的直接竞争者**：搜索"entity-level contrastive pretraining decoder LLM"和"entity-anchored contrastive alignment"等关键词，**未找到已有工作直接在 decoder-only LLM 上做 entity-level InfoNCE contrastive CPT for cross-lingual factual conductivity**。最接近的是 KBioXLM（encoder + masking）、CCL-XCoT（decoder + sentence-level contrastive）、EntityCS（encoder + code-switching）、LEIA（decoder + entity augmentation without contrastive）。EACA 的组合确实是新的。

- **调研总结**：Cross-lingual factual consistency 是一个活跃且重要的研究方向。CLiKA 提出了诊断但无解。CCL-XCoT 和 Liu & Niehues 验证了 contrastive CPT 的有效性但停留在 sentence-level。实证工作（arXiv:2510.10280, Bandarkar et al.）强烈暗示 entity-level 是真正的瓶颈。EACA 处于这些工作的自然交汇点，填补了"entity-level contrastive CPT on decoder LLMs"这一具体空缺。

---

```
【Trivial Alternative 检验】:
```

**存在 partial trivial alternatives，但 EACA 的增量价值可以论证。**

1. **LEIA-style entity augmentation (无 contrastive loss)**：LEIA 已经通过在 CPT 中插入 entity markers 来提升跨语言迁移。一个 reviewer 会问："只用 LEIA-style augmentation + standard CPT，不加 contrastive loss，是否已经足够？" Proposal 已将此作为 ablation（好的），但如果 LEIA 本身就能在 CLiKA 的 XRR 上取得大部分收益，EACA 的 contrastive loss 增量就会缩小。

2. **SubInj / SubSub (arXiv:2510.10280) 推理时干预**：这些方法在推理时注入英文 entity name 就能获得 +14-32% recall 和 +17-44% consistency gains。一个 reviewer 会问："如果推理时 entity priming 就够了，为什么要付训练时 contrastive alignment 的代价？" Proposal 提到了这一点但回答相对薄弱——"训练时对齐 vs 推理时干预是互补的"需要实证支持。

3. **CCL-XCoT 的 entity-grounded 简单变体**：一个 reviewer 可能想到：在 CCL-XCoT 的 sentence-level contrastive loss 中，不用 entity-level，而是简单地在 batch 构建时确保 positive pairs 包含相同 entity mentions，这可能用更低成本实现大部分收益。

**增量价值**：EACA 的增量在于 (a) 直接在 entity representation space 做对齐（vs 间接通过 sentence-level），(b) FactNet 提供的结构化 entity-fact grounding（vs 依赖 parallel text），(c) frequency weighting 针对 low-resource entities。这些增量是真实的，但需要实验验证其 marginal value 是否显著。

---

```
【前提假设检验】:
```

**核心逻辑链**：Entity alignment 是 crosslingual consistency 的瓶颈 → Entity-level contrastive loss 能改善 entity alignment → 改善 entity alignment 能改善 XRR conductivity → 这比 sentence-level contrastive 更有效。

**检验各环节**：

1. ✅ "Entity alignment 是瓶颈"——有实证支撑（arXiv:2510.10280 的 r > 0.7 相关性；Bandarkar entity priming 实验）。**但注意**：相关性 ≠ 因果性。entity alignment 好的 facts 一致性高，不代表强制 entity alignment 就能带来一致性提升。这是一个关键的逻辑跳跃。

2. ⚠️ "Entity-level InfoNCE contrastive loss 能有效改善 decoder LLM 的 entity representation alignment"——**这是未经验证的核心假设**。在 encoder 上有效（KBioXLM）不代表在 decoder-only 上有效。Decoder-only 模型的 hidden states 是 causal/left-to-right 的，mean-pooling over entity span 是否能得到有意义的 entity representation 尚无定论。Entity Lens (BlackboxNLP 2025) 提供了一些间接支撑，但那是分析性工作，不是训练时干预的证据。

3. ⚠️ "Contrastive loss 在 entity-level 比 sentence-level 更有效"——这是中心假设，**完全没有先验实证**。理论动机（"entity 是 factual knowledge 的自然单元"）是 plausible 但不是 evidence。一个 reviewer 可以 argue："sentence-level contrastive 已经隐含了 entity alignment（因为 parallel sentences 中相同 entities 自然出现），而且提供了更丰富的上下文信号。"

4. ⚠️ "Joint NTP + entity contrastive 不会严重冲突"——Proposal 设计了 gradient monitoring + PCGrad fallback，但前提假设是 NTP 和 entity contrastive 在 middle layers 的 gradient 足够兼容。Veitsman et al. (arXiv 2026) 发现 sentence-level contrastive alignment 在 token-level tasks 上失败——类似的 granularity mismatch 可能出现在 entity-level contrastive + token-level NTP 之间。

---

```
【3 维度打分】:
```

**1. Novelty: 中（偏强）**

理由：
- **真实的组合新颖性**：调研确认没有现有工作直接在 decoder-only LLM 上做 entity-level InfoNCE contrastive CPT for cross-lingual factual conductivity。最近的 CCL-XCoT 是 sentence-level，KBioXLM 是 encoder + masking + biomedical domain，LEIA 无 contrastive loss，EntityCS 是 encoder + code-switching。EACA 的组合点确实是空白。
- **但**：这是一个"自然延伸"而非"conceptual surprise"。当 CLiKA 发现 conductivity gap、arXiv:2510.10280 发现 entity alignment 是瓶颈、CCL-XCoT 验证了 contrastive CPT 有效时，"把 contrastive CPT 从 sentence-level 下沉到 entity-level"是一个**高度可预测的下一步**。一个熟悉该领域的 reviewer 看到这个 idea 可能会说 "this is the obvious next thing to try" 而非 "surprising"。
- Novelty 的真实增量主要来自 FactNet QID-grounded contrastive pairs（vs parallel text）和 script-aware transliteration augmentation 的集成。但 transliteration augmentation 本身来自 TransliCo (ACL 2024)，frequency weighting 来自 Liu et al. (EMNLP 2025)，gradient monitoring 来自 PCGrad/GradNorm——都是已有 technique 的搬运。
- **总结**：组合是新的，空白是真的，但 conceptual novelty 有限——更像是"missing experiment"而非"missing insight"。

**2. Significance: 中**

理由：
- **问题重要性高**：Cross-lingual knowledge conductivity 是多语言 LLM 的核心挑战。CLiKA (NAACL 2024) 的发现——现有方法都无法实质性提升 conductivity——使这个问题非常值得研究。
- **如果 positive，impact 是真实的**：如果 EACA 确实能在 XRR 上取得 significant improvement（而非仅仅 BMLAMA 上的 marginal gains），这对多语言 LLM 领域有明确贡献。
- **但 scope 受限**：(a) 方法依赖 FactNet + DaMuEL 这些特定资源，泛化性有限；(b) 仅在 7-8B 模型上验证；(c) 如果 entity-level contrastive 只在 same-script pairs 有效（Ifergan et al. 的证据暗示这很可能），实际价值会大打折扣——cross-script 才是真正的 hard case。
- **"I would have guessed this" 风险**：如果结果是"entity-level contrastive > sentence-level contrastive for entity-centric tasks"，这 **完全符合直觉**。审稿人可能会说 "of course, finer-grained alignment at the entity level helps for entity-level evaluation." 这不 surprising。

**3. Related Work: 强**

理由：
- Related work 覆盖极其全面：核心的 CLiKA、CCL-XCoT、Liu & Niehues、KBioXLM、arXiv:2510.10280 全部引用且描述准确。
- Script barrier 维度（Ifergan et al., Bandarkar et al., TransliCo）的覆盖是一个亮点，说明作者对领域有深入理解。
- 差异化定位清晰：与 CCL-XCoT 的 5 轴差异、与 KBioXLM 的 4 维度扩展都有具体论述。
- FactNet (Feb 2026)、Bandarkar et al. (March 2026) 等非常新的论文都被引用，说明 related work 的时效性好。
- 唯一轻微不足：缺少对 mLUKE (ACL 2022) 和 LUKE 系列在 entity representation 方面的更深入讨论，以及与 code-switching pretraining (PreAlign, CrossIC-PT) 的更系统对比。但这属于小问题。

---

```
【概率估计】: [25% - 38%] 中位 30%
```

```
【估计理由】:
```

三维度综合来看：
- **Related Work（强）** 保证了论文的基本学术规范和定位不会被 reject 因为 "missing important work"。
- **Significance（中）** 说明问题值得做，但 scope 和 impact 的天花板不够高——依赖特定资源、same-script 可能吃到大部分收益、cross-script 提升不确定。
- **Novelty（中偏强）** 是主要限制上界的因素。核心 idea 是一个"自然的下一步"（natural next step），在该领域活跃研究者眼中可预测。这使得论文更接近"solid engineering contribution"而非"surprising insight"。如果核心结果 positive，审稿人可能的反应是 "this confirms what we expected" 而非 "this changes how I think about the problem."

概率主要被 Novelty 的 "predictable next step" 性质限制在 35% 以下。如果实验做得非常好（strong ablations, clear entity-vs-sentence separation, cross-script gains），可以推到 35-38%；如果 cross-script 提升有限或 entity-level vs sentence-level 的增量不显著，概率跌到 25% 以下。

```
【主要风险】:
```

1. **"Predictable Extension" 质疑**：审稿人可能认为这是 CCL-XCoT + entity markers 的直接组合，conceptual contribution 不足以支撑顶会主会。Related work 做得越全面，反而越容易暴露"这只是现有工作的自然推论"——一个 reviewer 可以说 "the authors themselves show that all the ingredients already exist; the paper's contribution is just putting them together."

2. **Entity-level vs Sentence-level 的 marginal gain 可能不显著**：如果 sentence-level contrastive 已经隐含地做了 entity alignment（因为 parallel sentences 中相同 entity 的 representations 被拉近），entity-level 的额外收益可能很小。特别是在 same-script 语言对上，sentence-level 可能已经足够好了。这会使 core claim 变成 marginal empirical finding 而非 significant methodological advance。

Sources:
- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)
- [CCL-XCoT - EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.93/)
- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)
- [Ifergan et al. - NAACL Findings 2025](https://aclanthology.org/2025.findings-naacl.475/)
- [Bandarkar et al. - arXiv:2603.17070](https://arxiv.org/abs/2603.17070)
- [FactNet - arXiv:2602.03417](https://arxiv.org/abs/2602.03417)
- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)
- [TransliCo - ACL 2024](https://aclanthology.org/2024.acl-long.136/)
- [Entity-Level Alignment - arXiv:2510.10280](https://arxiv.org/abs/2510.10280)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct my evaluation. Let me compile the analysis.

---

```
【阶段】: Triage

============================================================
⚠️ 严重警告：venue 完全不匹配 ⚠️
============================================================

本 proposal 研究的是多语言 LLM 的 cross-lingual knowledge conductivity，
属于 NLP/Computational Linguistics 领域。

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确指出：
"Submissions without a robotics focus will be returned without review."
CoRL 接受的主题包括：robot perception、manipulation、locomotion、
sim-to-real transfer、imitation learning for robotics 等。

本 proposal 与 robotics 零关联，投稿 CoRL 会被 desk reject。
如果目标是 NLP 会议（ACL/EMNLP/NAACL），以下评估按 NLP 领域标准给出。
如果确实要投 CoRL，概率为 ~0%，无需进一步评估。

以下按 NLP/CL 领域会议标准评估 idea 质量。
============================================================

【领域调研】:

1. CLiKA (Gao et al., NAACL 2024, arXiv:2404.04659):
   定义了 cross-lingual knowledge conductivity 及 XRR 指标，发现现有多语言预训练和指令微调均无法实质性提升 conductivity（XRR < 0.01）。这是本 proposal 的核心问题来源。论文真实存在，描述准确。

2. CCL-XCoT (Zheng et al., EMNLP Findings 2025, arXiv:2507.14239):
   在句/段级别用 InfoNCE 对比学习进行 continued pretraining，配合 XCoT 指令微调，减少跨语言幻觉达 62%。本 proposal 的直接 baseline，描述准确。注意：CCL-XCoT 的 arXiv 日期为 2025 年 7 月，而 proposal 中声称其为 EMNLP 2025 Findings——需验证时间线是否一致（EMNLP 2025 于 2025 年底举行，7 月 arXiv 合理）。

3. Liu & Niehues (ACL 2025, arXiv:2502.14830):
   中间层（layer 16/32）句级对比对齐用于 task-specific fine-tuning，在 slot filling (+1.5 F1) 和 MT (+1.5 BLEU) 上取得改进。本 proposal 的方法论前辈，描述准确。

4. KBioXLM (Geng et al., EMNLP Findings 2023, arXiv:2311.11564):
   在 XLM-R 上用实体掩码、关系掩码、段落关系预测进行生物医学跨语言对齐，+20 F1。本 proposal 的实体级对齐先例，但限于 encoder + 生物医学域。描述准确。

5. FactNet (arXiv:2602.03417, Feb 2026):
   1.7B 实体锚定原子事实，316 个 Wikipedia 版本，92.1% grounding precision。真实存在，描述准确。

6. Bandarkar et al. (arXiv:2603.17070, Mar 2026):
   确认 script match 是跨语言知识迁移失败的主要预测因子（~13% gap），entity priming 实验证明实体映射是跨脚本瓶颈。真实存在，描述准确。

7. Ifergan et al. (NAACL Findings 2025, arXiv:2408.10646):
   用 knowledge editing 探针发现 script similarity 主导跨语言表征共享（same-script CKR ~37.6% vs. cross-script <10-20%）。真实存在，描述准确。

8. DCO (arXiv:2603.04678, Mar 2026):
   DPO-inspired post-hoc consistency optimization。本 proposal 提到其为互补方法。真实存在。

9. AlignX (EMNLP 2025):
   多语言 continual pretraining 对齐表征 + 指令微调，扩展到 51 种语言。与本 proposal 有重叠但粒度不同（AlignX 为通用表征对齐，非实体级）。

10. Entity-Level Alignment (Liu, Wang et al., arXiv:2510.10280):
    发现 entity alignment 与 cross-lingual consistency 的 Pearson r > 0.7，SubInj 方法在推理时就能达到 +14-32% recall 和 +17-44% consistency gains。真实存在，描述准确——但这恰恰构成了本 proposal 的 trivial alternative 威胁。

- 调研总结: 
  跨语言知识一致性/传导性是 2024-2026 年的活跃研究方向，已有工作沿两条线展开：(a) 句/段级对比 CPT (CCL-XCoT, Liu & Niehues)，(b) 推理时干预 (SubInj, entity priming)。实体级对比对齐在 decoder LLM 上的 CPT 尚无直接先例（KBioXLM 仅限 encoder + 生物医学），本 proposal 定位在此空白处。但该空白是否代表"真正未被探索的机会"还是"已有的组合但尚未有人做因为改进可能有限"，存在不确定性。


【Trivial Alternative 检验】:

存在两个严肃的 trivial alternative 威胁：

(1) **推理时 SubInj/Entity Priming**：arXiv:2510.10280 的 SubInj 方法仅在推理时注入英语实体名称，就获得了 +14-32% recall 和 +17-44% consistency gains，且零训练成本。Bandarkar et al. 的 entity priming 实验同样表明推理时提供实体名就能显著改善跨脚本迁移。EACA 需要 ~1100-1600 H100 hours 的训练成本，如果最终效果与推理时干预相当，增量价值极低。Proposal 未直接与 SubInj 进行比较或论证为何训练时对齐优于推理时干预。

(2) **LEIA + 简单 entity code-switching**：LEIA 已经证明在 decoder LLM CPT 中插入英语实体名可以改善跨语言迁移。如果 EACA 的核心优势主要来自实体边界标注（[ENT]/[/ENT]），而非对比损失本身，那么 LEIA 风格的简单 augmentation 可能已经捕获了大部分收益。

增量价值论证：Proposal 的 implicit 论点是"训练时对齐 > 推理时干预"因为它改变了模型的内部表征而非仅仅在表面层面提供线索。这有一定道理，但未被论证——是一个需要实验验证的假设，而非已知事实。


【前提假设检验】:

核心 claim 的逻辑链：
"句级对齐不够 → 实体才是事实知识的基本单位 → 实体级对比对齐能改善 conductivity"

未经验证的关键假设：

(1) **相关 ≠ 因果**：entity alignment 与 consistency 的 r > 0.7 相关性是观察性的。高 entity alignment 可能是 consistency 的结果而非原因——可能是因为模型在某些语言对上整体表征更好，因此 entity alignment 和 consistency 同时高。强制对齐 entity 表征是否能因果性地改善 consistency，是一个未经验证的跳跃。

(2) **对比损失在 decoder LLM 隐藏状态上的有效性**：在 encoder 模型上，对比学习有大量成功先例（SimCLR, CLIP, E5 等）。但 decoder LLM 的隐藏状态具有不同特性——它们是自回归的、位置敏感的。Mean-pooling entity span 在 decoder 中间层是否能产生足够好的实体表征用于对比学习，是一个未经检验的假设。Liu & Niehues 在句级别展示了可行性，但实体级别 span 更短（通常 1-5 tokens），信号可能更弱。

(3) **NTP 和实体对比损失的兼容性**：NTP 优化语言特定的 token 分布，对比损失拉近跨语言实体表征。这两个目标可能在 decoder LLM 中存在根本性冲突。Proposal 设计了 PCGrad/GradNorm 作为缓解措施，但如果冲突是根本性的（而非工程可调的），这些机制无法真正解决问题。


【3 维度打分】:

1. Novelty: 【中】
   
   理由：实体级对比对齐在 decoder LLM CPT 上的应用确实没有直接先例——这是真实的 novelty。KBioXLM (EMNLP Findings 2023) 做了实体级对齐但在 encoder 上用 masking 目标；CCL-XCoT (EMNLP Findings 2025) 做了对比 CPT 但在句/段级别；Liu & Niehues (ACL 2025) 做了中间层对比对齐但在句级别。EACA 在"粒度 × 模型架构 × 训练范式"三维矩阵中占据了一个空位。

   但 novelty 的性质是**组合性的**而非**概念性的**——它将已有的组件（InfoNCE、entity span、middle-layer extraction、decoder LLM CPT）以新组合拼装在一起，每个组件都有明确先例。核心 insight "entity-level alignment should help entity-level consistency" 虽然在技术执行上是新的，但在概念上是相当直觉的。审稿人可能会认为这是 "the obvious next thing to try" 而非 "a surprising new insight"。

   此外，方法的 novelty 声称中有些水分：proposal 列出了 6 条 novelty，但其中 (3) frequency-aware weighting、(4) gradient conflict monitoring、(5) transliteration augmentation、(6) script-stratified evaluation 均为工程细节或评估规范，不构成独立的 novelty 贡献。真正的核心 novelty 只有 (1) entity-level contrastive anchoring 和 (2) structured knowledge grounding via QIDs。

2. Significance: 【中偏强】
   
   理由：研究问题本身重要且被明确界定。CLiKA (NAACL 2024) 令人信服地证明了 conductivity gap 的存在，且至今无有效解决方案。如果 EACA 的核心发现是 positive 的（实体级 > 句级），这对多语言 LLM 社区有实质指导意义——它会建立一个新的 CPT 范式。

   但 significance 受限于两个因素：
   - 如果结果仅限于 same-script pairs 有效而 cross-script 改善有限（这是 proposal 自己承认的风险），那么实际影响的语言覆盖范围会大打折扣。
   - 推理时方法（SubInj）已经取得了实质性的 consistency gains，如果 EACA 的额外训练成本仅换来边际改善，则实际意义存疑。
   
   问题的重要性不等于解决方案的重要性。问题是 strong 的，但这个特定解决方案是否足够有力仍需验证。

3. Related Work: 【强】
   
   理由：这是整个 proposal 最突出的部分。Related work 覆盖面极广且定位精确：
   - 方法论维度：CCL-XCoT（句/段级对比 CPT）、Liu & Niehues（句级中间层对比对齐）、KBioXLM（encoder 实体级 masking 对齐）——每个都有清晰的差异化论述
   - 问题维度：CLiKA（conductivity gap）、arXiv:2510.10280（entity alignment 与 consistency 的相关性）
   - 脚本维度：Ifergan et al. (NAACL Findings 2025)、Bandarkar et al. (arXiv:2603.17070)、TransliCo (ACL 2024)
   - 数据/资源维度：FactNet、DaMuEL、mReFinED
   
   所有引用的论文经调研确认真实存在，描述基本准确。positioning 对每个 baseline 都给出了多维度的区分。
   
   唯一的轻微不足是：对 SubInj (arXiv:2510.10280) 作为推理时替代方案的论述不够充分——它被作为 "motivation" 引用（entity alignment 很重要），但未被作为 "trivial alternative" 正面对比。


【概率估计】: [25% - 35%] 中位 28%
（注意：此概率基于投稿 ACL/EMNLP/NAACL 等 NLP 主会估计。
 投稿 CoRL 2026 的概率为 ~0%——venue 完全不匹配，会被 desk reject。）

【估计理由】:
- Novelty 为"中"：核心 idea 有真实的组合新颖性，但概念上是直觉的"the obvious next step"，缺少 surprising 的 insight。这限制了上界——即使实验完美执行，审稿人可能写 "well-executed but the idea is incremental"。
- Significance 为"中偏强"：问题重要且被领域认可，但推理时 trivial alternative (SubInj) 的存在削弱了训练时方案的增量价值论证。
- Related Work 为"强"：这是一个 plus，但不能弥补 idea 内核的 novelty 上限。
- 概率上界被 Novelty 限制在 ~35%：如果核心实验全部 positive，审稿人大概率评价为 "solid empirical contribution, somewhat expected result"，可能获得一个 borderline accept。但如果有审稿人认为 SubInj 已经足够，或者认为从 correlation 到 causation 的跳跃不成立，则可能被拉到 reject。

【主要风险】:
1. **Trivial Alternative 风险**：SubInj 等推理时实体干预方法零训练成本即可获得显著 consistency gains (+17-44%)。如果 EACA 的额外 ~1100 H100 hours 训练仅换来边际改善（例如在 SubInj 基础上仅额外 +5%），审稿人会质疑其实际价值。Proposal 未提供"训练时对齐优于推理时干预"的先验论证。
2. **相关-因果跳跃风险**：整个 proposal 的逻辑基础建立在"entity alignment 与 consistency 高度相关 → 因此强制 entity alignment 能改善 consistency"。但这一因果方向未被建立。如果 entity alignment 是高 consistency 的伴随现象而非原因，那么 EACA 的核心前提不成立。
```

Sources:
- [CLiKA - NAACL 2024](https://aclanthology.org/2024.naacl-long.339/)
- [CLiKA - arXiv](https://arxiv.org/abs/2404.04659)
- [CCL-XCoT - arXiv](https://arxiv.org/abs/2507.14239)
- [CCL-XCoT - EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.93.pdf)
- [Liu & Niehues - ACL 2025](https://aclanthology.org/2025.acl-long.778/)
- [Liu & Niehues - arXiv](https://arxiv.org/abs/2502.14830)
- [KBioXLM - EMNLP Findings 2023](https://aclanthology.org/2023.findings-emnlp.751/)
- [FactNet - arXiv](https://arxiv.org/abs/2602.03417)
- [Bandarkar et al. - arXiv](https://arxiv.org/abs/2603.17070)
- [DCO - arXiv](https://arxiv.org/abs/2603.04678)
- [Entity-Level Alignment - arXiv](https://arxiv.org/pdf/2510.10280)
- [AlignX - EMNLP 2025](https://arxiv.org/html/2509.24338)
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
  "promptId": "8b885680-cedc-4c1d-9767-a00ba644efb5",
  "type": "user",
  "uuid": "58477136-b4fd-434b-a345-009136d82ffd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:12:16.468Z_

```json
{
  "parentUuid": "58477136-b4fd-434b-a345-009136d82ffd",
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
  "uuid": "730b1d70-d523-4d79-865b-b45805cd593c",
  "timestamp": "2026-05-19T21:12:16.468Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:12:16.468Z_

```json
{
  "parentUuid": "730b1d70-d523-4d79-865b-b45805cd593c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "127a53ae-3fa9-4c5e-bc8f-0832acf3ed87",
  "timestamp": "2026-05-19T21:12:16.468Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71",
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
  "leafUuid": "127a53ae-3fa9-4c5e-bc8f-0832acf3ed87",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge synthesis of multilingual LLM entity alignment proposal",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:13:00.662Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully to produce a Meta Judge synthesis.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 弱-中 (Weak-Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [15% - 25%] 中位 20%
- Venue: CoRL mismatch (desk reject), evaluated for NLP venue
  
**Reviewer 2:**
- Novelty: 中偏强 (Medium-Strong)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [25% - 38%] 中位 30%
- Venue: CoRL mismatch (desk reject), evaluated for NLP venue

**Reviewer 3:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability: [25% - 35%] 中位 28%
- Venue: CoRL

Now I'm comparing the three assessments across novelty, significance, and venue fit. Reviewers 2 and 3 rate novelty slightly higher than Reviewer 1, while Reviewer 3 sees stronger significance than the others. All three agree on strong related work coverage, and the acceptance probabilities cluster around 20-30%, with Reviewer 2 being most optimistic.

The most striking consensus is that all three reviewers identify a fundamental venue mismatch—CoRL isn't the right fit for this work, with two explicitly recommending evaluation at an NLP venue instead. This is a desk reject. Related work is universally rated as strong across all reviewers. Novelty emerges as the critical bottleneck—all three reviewers characterize it as combinatorial recombination rather than a conceptual breakthrough, with consistent concerns about it being an obvious or predictable next step given existing literature. SubInj presents a serious threat as a trivial alternative requiring zero training versus roughly 1600 H100 hours. There's also universal skepticism about whether the causal direction between entity alignment and consistency is actually proven, and whether entity-level contrastive loss can work effectively on decoder-only models the way it does in encoder architectures. Significance lands at medium consensus across reviewers. LEIA-style augmentation without contrastive loss is flagged as another potential trivial baseline. The reviewers diverge somewhat on novelty ratings, with assessments ranging from weak-to-medium up to medium-to-strong. Given the "宁缺毋滥" principle favoring conservative assessments, I'm settling on "中" as the consensus view since the novelty is clearly combinatorial rather than conceptual. For the probability estimates, I'm widening the interval to account for the moderate consistency across raters and leaning toward the stricter end, landing on a range of 18-30% with a median of 25%. Let me reconsider the venue constraint—all three reviewers flag this as a desk reject at CoRL, which is a hard blocker since the proposal can't even be submitted there. For the NLP venue assessment, I'm settling on [18%-32%] with a median of 25%, leaning toward R1's stricter estimates while acknowledging the higher consensus from R2 and R3.

Now I'm looking at the implementation details across the reviews: the compute requirements are around 1100-1600 H100 hours, the data comes from public sources like FactNet and Wikipedia, there's preprocessing and analysis work needed, continued pretraining of 7-8B models, and no new benchmark development required.

The timeline spans 3-5.5 months, so I'm ready to compile the final assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "127a53ae-3fa9-4c5e-bc8f-0832acf3ed87",
  "isSidechain": false,
  "requestId": "req_011CbCchcF2bJEPkASm3HT9y",
  "type": "assistant",
  "uuid": "927f8237-953a-430a-8dc0-4cf883353e2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rffa5DdjLV2WNiv3vixvma",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26988,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4475,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 26988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26988
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

_source line 9 · 2026-05-19T21:13:58.532Z_

【阶段】: Meta Judge
【三次中位】: [20%, 28%, 30%]  std=4.3%
【共识维度】:
- **Venue Mismatch（致命）**: 3/3 审稿人一致判定 CoRL 2026 是完全错误的投稿目标，会被 desk reject。以下所有评估基于改投 NLP 主会（ACL/EMNLP/NAACL）。
- **Related Work（强）**: 3/3 一致评为"强"。覆盖全面、引用真实、差异化定位清晰，是 proposal 最突出的维度。
- **Novelty 为概率天花板的主限制因素**: 3/3 一致认为核心贡献是"组合型创新"（recombination）而非"概念型突破"。所有人独立使用了"obvious next step"/"predictable extension"的表述。
- **SubInj trivial alternative 威胁（强共识）**: 3/3 一致标记 SubInj（arXiv:2510.10280）的推理时零训练成本 entity intervention（+14-32% recall, +17-44% consistency）为最严重的 trivial alternative，EACA 需~1100-1600 H100-hours 训练，增量 cost-effectiveness 存疑。
- **相关≠因果逻辑跳跃**: 3/3 一致指出 entity alignment 与 consistency 的 r>0.7 相关性是观察性的，强制训练时 entity alignment → consistency improvement 的因果链未被建立。
- **Decoder LLM entity contrastive 可行性存疑**: 3/3 一致指出 encoder 上有效（KBioXLM）不代表 decoder-only 上有效，mean-pooling causal entity span 的有效性是未经验证的核心假设。
- **LEIA trivial baseline 威胁**: 3/3 一致标记如果 LEIA-style entity augmentation（无 contrastive loss）就能获得大部分收益，contrastive loss 的增量价值存疑。
- **Significance（中）**: R1=中, R2=中, R3=中偏强，共识落在"中"，问题重要但解决方案的增量价值受 trivial alternative 和 scope 限制。
- **"6 novelties 水分"问题**: R1 和 R3 明确指出列出的 6 条 novelty 中 (3)-(6) 是工程细节/评估规范，真正的核心 novelty 仅 (1)(2)。R2 虽未单独标记此点但在 novelty 分析中暗示了相同判断。
【异常维度】:
- **Novelty=弱-中（仅 R1）**: R1 给出的 novelty 评级最低（弱-中），R2（中偏强）和 R3（中）均更宽松。R1 的论证逻辑强（"需要列 6 个 novelties 通常意味着没有一个足够强的单一贡献"），但"弱"端可能过于严苛——调研确认该组合确实无直接先例。降权处理：取 R2/R3 的共识"中"作为稳健判定，但保留 R1 的"弱"端风险作为下界参考。
- **Significance=中偏强（仅 R3）**: R3 略高于其他两位。R3 论证合理（"如果 positive 会建立新 CPT 范式"），但 R1/R2 的共识"中"更稳健——因为"positive 的结果本身不 surprising"。降权处理：保持"中"。
- **NTP 与 contrastive loss 兼容性风险**: R3 单独强调了 NTP 和 entity contrastive loss 可能存在根本性冲突，引用了 Veitsman et al. 的发现。R1/R2 提到了 gradient conflict 但未上升到"根本性冲突"的高度。保留为需关注的风险点但不作为主判据。
【最终概率】: [18% - 32%] 中位 25%
【一致性】: 中（std=4.3%，在 3-7% 区间内；rubric 判决方向一致但 Novelty 评级存在一档分歧）
【综合理由】:

1. **Novelty 共识锁定天花板**: 三位审稿人对 novelty 的定性判断高度一致——组合型创新、predictable next step、缺乏 surprising insight。分歧仅在程度（弱-中 vs. 中 vs. 中偏强）。按"宁缺毋滥"原则，取"中"但附带"弱"端下行风险。Novelty=中 在 NLP 主会对应的概率天花板约 35%（需要实验极其亮眼才能触及）。

2. **Trivial alternative 三重门槛进一步压低**: 三位审稿人共识标记了三个 trivial alternative（SubInj > LEIA > CCL-XCoT），任何一个如果 EACA 无法显著超越，论文的增量价值就不成立。这不是一个简单的"实验能救"的问题——即使实验 positive，审稿人仍然有天然的 pushback 路径（"SubInj 零成本已经这么好了"）。这将有效天花板从 ~35% 压至 ~32%。

3. **因果逻辑缺口是结构性弱点**: 相关≠因果的逻辑跳跃是 proposal 核心论证链上的裂缝，三位审稿人一致指出。这不是实验设计能完全弥补的——即使实验 positive，审稿人仍可 argue "你在优化的可能不是真正的 causal bottleneck"。

4. **中位偏向严格端处理**: R1（20%）与 R2/R3（28%/30%）有 8-10 个百分点的差距。R1 的严格评估有充分论据支撑（novelty 弱-中 + trivial alternative 三重门槛），按"中一致偏严"原则，中位取 25%——在 R1 和 R2/R3 中位之间偏向 R1。

5. **Related Work 的"双刃剑"效应**: R1 精准指出一个悖论——related work 做得越全面，反而越暴露"all ingredients already exist; the paper just puts them together"。这是一个 meta-level 的风险，三位审稿人都隐含提到了。

6. **Venue 问题是前置致命项**: 即使 idea 本身有一定概率中稿 NLP 主会，投稿 CoRL 的概率为 ~0%。这是系统最需要优先反馈的信息。

【建议】: 边缘（改投 NLP 主会后，中位 25% 处于边缘区；需要在 Novelty framing 和 trivial alternative 论证上做实质性强化才可能推向 30%+。CoRL 投稿不推荐——会被 desk reject。）

【实施评估】:
  - 计算资源: 1100-1600 H100-hours（预处理 ~10-15 GPU-days A100，Phase 0 ~130 H100-hrs，全量训练 ~800-1100 H100-hrs，评估+消融 ~160-235 H100-hrs），估算 GPU 成本 $2,200-3,200（spot pricing ~$2/H100-hr）
  - 数据需求: FactNet（1.7B entity-grounded facts，公开 arXiv）、DaMuEL（12.3B QID-annotated tokens，CC BY-SA，公开）、Wikipedia wikilinks（公开）、mReFinED（公开）、BMLAMA-53/TyDiQA-GoldP/X-CODAH 等评测集（均公开）。Tier 3 语言（SW/YO/KM）的 FactNet 覆盖存在不确定性（5K-200K pairs），需 Phase 0 审计
  - 人工介入: 预处理 pipeline 工程搭建（1.5-2 周）、Phase 0 go/no-go 判断、gradient conflict 分析解读、script-grouped 评估分析。无需人工标注
  - 训练需求: 需要对 LLaMA-3.1-8B（主）和 Gemma-7B（辅）进行 continued pretraining，LoRA rank 64 on middle layers，1.5-2.5B tokens 全量训练。单次全量训练 wallclock ~30-50 hrs on 8×H100
  - 新 Benchmark: 不需要构建新 benchmark，使用现有 BMLAMA-53、TyDiQA-GoldP、X-CODAH、LiveCLKTBench、CLiKA XRR
  - 预估周期: 3.5-5.5 个月（preprocessing 1.5-2 周 → Phase 0 pilot 2-3 周 → 全量训练+评估+消融 6-10 周 → 分析+写作 3-4 周）。关键路径：preprocessing → FactNet audit → Phase 0 go/no-go → 全量训练，串行依赖

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "927f8237-953a-430a-8dc0-4cf883353e2c",
  "isSidechain": false,
  "requestId": "req_011CbCchcF2bJEPkASm3HT9y",
  "type": "assistant",
  "uuid": "bdb74fc9-1987-42b7-b527-86fdf67b3a1f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rffa5DdjLV2WNiv3vixvma",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26988,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4475,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 26988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26988
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
  "leafUuid": "bdb74fc9-1987-42b7-b527-86fdf67b3a1f",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge synthesis of multilingual LLM entity alignment proposal",
  "sessionId": "a6809ca4-ba1b-4ddb-94f2-39ad79891e71"
}
```

---
