# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f40b30a0-1c09-4565-9038-2bbcf4fca429.jsonl`
- **Structured JSON:** [`642f09e872c69fdcebb2.json`](../../sessions/64/642f09e872c69fdcebb2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:30:36.197Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:30:36.197Z",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nBased on my research, I now have enough context to provide a comprehensive evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [ViDoRe V3] (arXiv:2601.08620, 2026): 定义了检索+定位的联合评测标准，3,099个人工标注查询，当前最佳模型grounding F1仅0.089 vs 人类0.602。这个巨大差距直接支撑了proposal的研究动机。\n- [Nemotron ColEmbed V2] (arXiv:2602.03992, 2026): ViDoRe V3 SOTA，63.42 nDCG@10，基于Qwen3-VL-8B+双向注意力+hard negative mining。是page-level retrieval的直接竞争对手。\n- [MetaEmbed] (ICLR 2026 Oral, arXiv:2509.18095): Matryoshka Multi-Vector Retrieval，沿token数量维度嵌套。Proposal正确区分了自己在\"空间语义粒度\"维度的嵌套。\n- [MURE] (arXiv:2603.13349, 2026): 分辨率级别Matryoshka表示学习(RMRL)，输入侧嵌套。Proposal正确定位其差异化：输出侧空间语义层次嵌套。\n- [Multi-Granularity Framework] (arXiv:2505.01457, 2025): 3模型pipeline达到MMDocIR 65.56，明确留下端到端统一作为open question。直接验证了proposal要解决的问题。\n- [AGREE] (SIGIR 2026, arXiv:2511.13415): 注意力代理监督，改善page-level nDCG但无bounding box输出。Proposal的直接前驱，从proxy supervision升级到direct box regression。\n- [Hydra] (arXiv:2603.28554, 2026): 单模型检索+生成，LoRA切换，但两任务独立无共享loss。Proposal强调joint training的互强化假说与之形成对比。\n- [ReAlign] (SIGIR 2026, arXiv:2604.07419): VLM推理识别区域→文本描述→KL散度对齐。间接空间监督，proposal用直接box regression区分。\n- [PixSearch] (arXiv:2601.19060, 2026): 端到端LMM统一区域感知与检索增强推理，但属于RAG范式(生成时动态检索)，非独立检索范式；使用pixel-level分割而非bounding box。\n- [Localization Heads] (CVPR 2025 Highlight, arXiv:2503.06287): 冻结VLM中~3个注意力头即可实现竞争性定位（自然图像），核心假设的间接证据来源。\n- [Snappy] (arXiv:2512.02660, 2025): 无训练patch-to-region相关性传播，BBox-DocVQA上59.7% IoU@0.5。是grounding的training-free下界。\n\n- 调研总结: Visual Document Retrieval是2025-2026年的高活跃赛道，多模型pipeline已证明多粒度检索的价值但留下端到端统一作为明确的open question。空间定位（grounding）刚被ViDoRe V3正式纳入评测，当前模型与人类的巨大差距(0.089 vs 0.602 F1)标志着这是一个刚打开的研究窗口。Proposal精准定位在这个窗口上，且与现有工作(AGREE, ReAlign, PixSearch, Hydra)有清晰的差异化。\n\n【整体印象】: 作为审稿人，第一反应是**倾向 weak accept**。这是一篇在活跃领域中精准定位了genuine research gap的proposal，展现了对领域的深刻理解。研究假说清晰且可证伪，实验设计非常完备（6个ablation直接测试每个设计决策）。主要犹豫在于：(1) 核心贡献可能被视为\"已有组件的工程整合\"而非\"根本性新洞见\"；(2) 系统复杂度高，成功依赖多个组件协同工作。但整体来说，这是一篇above-average的投稿。\n\n【核心贡献】: \n1. **端到端多粒度检索+空间定位的统一**: 将3模型pipeline压缩为单模型，同时新增直接bounding box输出能力——这是文档检索领域目前不存在的能力组合。\n2. **Retrieval-Grounding Synergy假说**: 提出检索loss和定位loss通过共享空间语义表征互相增强的具体机制，有可证伪的ablation设计(#3)。\n3. **Spatially-Typed Matryoshka嵌套**: 在MetaEmbed（token维度）和MURE（分辨率维度）之外提出第三个正交嵌套轴（空间语义粒度），支持测试时粒度控制。\n\n贡献价值评估：如果synergy假说成立（joint training > separate training），这将为检索+定位联合学习提供有价值的empirical evidence。pipeline压缩本身具有明确的工程价值。但如果synergy不成立，论文退化为一篇系统集成论文，价值显著降低。\n\n【方法合理性】: \n方法总体合理，各组件有充分的先验支持：\n- 双向注意力LoRA: Nemotron ColEmbed V2已验证其对检索的有效性\n- 自回归定位头: Localization Heads (CVPR 2025)证明VLM patch嵌入包含空间信息；但该结论仅在自然图像上验证，文档图像需要独立验证（proposal已意识到并设计了DocLayNet评测）\n- Late interaction: ColPali/ColQwen2已验证的范式\n- Matryoshka训练: MetaEmbed已验证的框架\n\n**更简单的替代方案**: \n- 是否可以用Snappy的无训练方法（patch-to-region propagation）代替learned localization head？如果能达到类似效果，150M参数的额外decoder就不必要。Proposal应在ablation中包含Snappy-style baseline。\n- 是否可以直接用AGREE的注意力代理方法指导region proposal，而非训练独立的localization head？\n\n这些替代方案的存在不构成致命问题，但审稿人很可能会提出。Ablation #1（learned vs external parser vs fixed grid）部分回答了这个问题，但缺少与Snappy-style无训练方法的直接对比。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — ViDoRe V3的grounding gap (0.089 vs 0.602 F1)和Multi-Granularity Framework明确留下的open question提供了强有力的问题动机。这是一个在benchmark层面被明确量化的痛点，具有清晰的应用价值（RAG pipeline的context cropping需要精确定位）。问题的时效性极强，研究窗口刚刚打开。\n\n  2. 方法与创新: 【中偏强】 — 各组件单独来看并非全新（late interaction、box regression、Matryoshka训练均有先例），创新在于\"组合方式\"和\"joint training假说\"。与AGREE相比是从proxy → direct supervision的合理升级；与Hydra相比是从independent modes → joint loss的明确进步；与Multi-Granularity Framework相比是从multi-model → single-model的架构简化。Spatially-Typed Matryoshka是一个有趣的新概念但实质可能只是embedding加type tag。核心novelty高度依赖synergy假说是否成立。参考MetaEmbed(ICLR 2026 Oral)在token维度的Matryoshka创新深度，GroundVDR在空间语义维度的扩展是合理但可能被视为incremental。\n\n  3. 实验设计: 【强】 — 这是proposal最突出的优势。4类baseline覆盖所有竞争方向（page-level、region-level、grounding、unified）；6个ablation逐一测试每个设计决策，特别是ablation #3直接验证核心假说（3 seeds + paired significance test）；多benchmark覆盖（ViDoRe V1/V2/V3 + MMDocIR + BBox-DocVQA）；效率报告包含per-component latency breakdown和compute-normalized comparison。独立的localization head评测（DocLayNet mAP）验证核心假设。grounding target设定合理（0.2 F1 = 2.2× current SOTA作为minimum viable）。相比领域标准（Nemotron ColEmbed V2只报告nDCG，无ablation breakdown），这个实验设计远超average。\n\n  4. 可行性: 【中偏强】 — 480 H100-hours是学术实验室2-3周可完成的规模，合理可行。训练数据来源明确（DocLayNet公开80K + MMDocIR公开173K）。但风险点在于：(a) 自回归localization head在文档图像上的表现未知；(b) joint training可能需要大量超参调试（两个loss的权重平衡、梯度冲突等），实际时间可能超预估；(c) 只使用2 seeds进行主实验的统计显著性可能不够。\n\n  5. 写作与呈现: 【强】 — Proposal逻辑极其清晰：problem → hypothesis → landscape → differentiation → approach → evaluation。每个设计决策都有明确的motivation和对应的validation计划。与竞争工作的区分非常精确（如MURE输入侧 vs GroundVDR输出侧、Hydra独立模式 vs GroundVDR联合训练、ReAlign文本桥接 vs GroundVDR直接回归）。R-CNN → Faster R-CNN的类比既准确又有说服力。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】: \n- 上行因素：研究问题timing极佳（ViDoRe V3刚开放grounding赛道）；实验设计质量在领域内属于top tier；与所有竞争工作有清晰差异化；假说可证伪性强（审稿人欣赏这一点）。\n- 下行因素：创新可能被视为\"known components的新组合\"而非fundamental insight；系统复杂度高意味着实验结果可能不如预期clean；2025-2026该领域竞争极其激烈（每月有新SOTA），投稿时可能已有更新的工作出现；如果synergy假说不成立（ablation #3显示marginal gains），论文核心story塌缩。\n- AAAI 2026接收率约20-23%。这篇proposal整体质量明显高于average submission，但在一个拥挤的赛道上面临\"是否足够novel\"的审稿人分歧风险。预计会获得1个positive review（appreciate thorough design）和1-2个borderline review（question novelty depth），概率分布在acceptance threshold附近。\n\n【主要风险】: \n1. **Synergy假说不成立**: 如果ablation #3显示joint training相比separate training仅有marginal improvement（<1 nDCG point），核心贡献从\"scientific insight\"降级为\"engineering integration\"，审稿人会质疑\"为什么不直接用pipeline\"。\n2. **Novelty perception**: 在MURE、Hydra、ColParse、ReAlign等concurrent work密集的环境下，审稿人可能认为这是\"yet another system paper in VDR\"，尤其是如果Spatially-Typed Matryoshka被视为trivial extension（加type tag）。\n\n【实施评估】:\n  - 计算资源: ~480 H100-hours total（含ablation和multi-seed），学术实验室4-8 GPU集群可在2-3周完成。合理且可复现。\n  - 数据需求: DocLayNet (80K pages, 公开) + MMDocIR (173K bootstrapped + 1,685 expert annotations, 公开) + ViDoRe V3 (3,099 queries, 公开评测集)。全部公开可获取，无数据壁垒。\n  - 人工介入: 无需额外人工标注（利用现有public datasets）。但如果MMDocIR的bootstrapped annotations质量不足，可能需要少量人工清洗。\n  - 训练需求: 两阶段训练（Phase 1: localization head预训练 30h; Phase 2: joint fine-tuning 150h）。需要实现autoregressive localization head与VLM backbone的梯度连接，有一定工程复杂度。\n  - 新 Benchmark: 不需要构建新benchmark。使用现有ViDoRe V1/V2/V3 + MMDocIR + BBox-DocVQA。\n  - 预估周期: 实现+训练+ablation约6-8周（含调试时间）。如果joint training梯度平衡困难，可能延长至10-12周。写作2-3周。总计约2.5-3.5个月。\n```\n\nSources:\n- [ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2601.08620)\n- [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models](https://arxiv.org/abs/2602.03992)\n- [MetaEmbed: Scaling Multimodal Retrieval at Test-Time (ICLR 2026 Oral)](https://arxiv.org/abs/2509.18095)\n- [MURE: Hierarchical Multi-Resolution Encoding for VDR](https://arxiv.org/abs/2603.13349)\n- [Multi-Granularity Retrieval Framework for Visually-Rich Documents](https://arxiv.org/abs/2505.01457)\n- [AGREE: Attention Grounded Enhancement for Visual Document Retrieval (SIGIR 2026)](https://arxiv.org/abs/2511.13415)\n- [Hydra: Unifying Document Retrieval and Generation](https://arxiv.org/abs/2603.28554)\n- [ReAlign: Reasoning-Guided Fine-Grained Alignment (SIGIR 2026)](https://arxiv.org/abs/2604.07419)\n- [PixSearch: Pixel-Grounded Retrieval for Knowledgeable LMMs](https://arxiv.org/abs/2601.19060)\n- [Localization Heads in VLMs (CVPR 2025)](https://arxiv.org/abs/2503.06287)\n- [Snappy: Spatially-Grounded Document Retrieval](https://arxiv.org/abs/2512.02660)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- Nemotron ColEmbed V2 (arXiv 2026, arXiv:2602.03992): 当前 ViDoRe V3 榜首，nDCG@10=63.42，基于 Qwen3-VL-8B + 双向注意力 + hard negative mining。GroundVDR 使用相同 backbone（Qwen3-VL-8B），页面级检索需与之直接竞争。\n- MetaEmbed (ICLR 2026 Oral, arXiv:2509.18095): Meta/Facebook 工作，Matryoshka Multi-Vector Retrieval，沿 token 数量维度做嵌套。GroundVDR 提出沿空间-语义粒度维度的第三种正交嵌套轴——这是对 Matryoshka 范式的真正扩展，有明确区分度。\n- Multi-Granularity Framework (arXiv:2505.01457): 多粒度检索 SOTA (MMDocIR 65.56)，但需要 ColQwen2 + GME + Qwen2.5-VL + OCR 四组件流水线。该工作明确将\"端到端统一\"列为 open question——正是 GroundVDR 要回答的问题。\n- MURE (arXiv:2603.13349): 输入侧分辨率 Matryoshka (RMRL)，与 GroundVDR 输出侧空间-语义 Matryoshka 正交互补。MURE 无学习式 region proposal 或 bbox 预测。\n- Hydra (arXiv:2603.28554): 单模型统一检索+生成（LoRA 开关），但两任务是独立模式，无共享 loss 或协同训练。GroundVDR 的联合训练 + 协同假设提供了清晰区分。\n- AGREE (SIGIR 2026, arXiv:2511.13415): 注意力作为代理空间信号，页面级 nDCG 提升 12.82%，但不产生 bounding box。GroundVDR 从代理注意力监督升级为直接 box 回归监督。\n- Snappy (arXiv:2512.02660): 训练免费的空间定位，IoU@0.5=59.7% (BBox-DocVQA)。作为定位下界 baseline，GroundVDR 应大幅超越。\n- ReAlign (SIGIR 2026, arXiv:2604.07419): 使用 VLM 推理生成文本描述作为空间监督信号，是间接的文本桥接方法。GroundVDR 的直接 box 回归保留精确坐标且端到端可优化——区分明确。\n- PixSearch (arXiv:2601.19060): 统一区域感知与检索增强推理，但属于 RAG 范式（动态触发检索），产生像素级分割掩码而非 bbox，无层级多粒度嵌入结构。与 GroundVDR 的独立检索范式有根本区别。\n- Localization Heads (CVPR 2025 Highlight, arXiv:2503.06287): 仅需 ~3 个注意力头即可在自然图像上实现竞争力定位——为 GroundVDR 的核心假设（VLM patch embedding 含充足空间信息）提供间接证据，但文档图像与自然图像差异显著。\n- RegionRAG (AAAI 2026): 学习查询-patch 对齐但依赖手动阈值的 BFS 启发式 patch 分组。GroundVDR 的学习式 localization head 是更原则性的替代。\n- ColParse (arXiv:2603.01666): 布局感知子图像检索，95% 存储缩减，但依赖外部解析器无法联合优化。\n\n- 调研总结: 视觉文档检索领域在 2025-2026 年极其活跃，页面级检索已趋成熟（Nemotron ColEmbed V2, MetaEmbed），但**多粒度检索+空间定位的端到端统一**仍是公认的 open problem。现有工作要么是多模型流水线（Multi-Granularity Framework），要么只解决部分问题（AGREE 无 bbox, Hydra 无定位, MURE 无 region proposal）。GroundVDR 精准地占据了这一空白，且与所有现有工作的区分度清晰可辩。\n\n【整体印象】:\n作为审稿人，我的第一反应是 **lean accept / weak accept**。这是一份在竞争激烈的热门领域中展现出深度研究功底的 proposal：\n1. 问题定义精准，直击领域公认的 open problem（多模型流水线 vs. 端到端统一）；\n2. 文献定位极其详尽，对每个竞争工作的差异化分析准确到位；\n3. 核心假设（检索-定位协同效应）清晰可测试，有 detection 领域（R-CNN → Faster R-CNN）的成熟类比支撑；\n4. 实验设计非常完备，6 个 ablation 精准对应每个设计选择。\n\n主要顾虑在于：(a) 核心假设（VLM patch embedding 对文档 layout 的定位能力）是否成立仍是实验风险；(b) 同时在页面级、区域级、元素级三个粒度都做到竞争力水平的野心很大；(c) 定位目标（0.2 F1）虽然是 SOTA 的 2.2×，但绝对值仍然偏低。\n\n【核心贡献】:\n1. **Spatially-Typed Matryoshka Multi-Vector Embeddings**: 在 MetaEmbed 的 token 数量嵌套和 MURE 的分辨率嵌套之外，引入空间-语义粒度作为第三个正交嵌套维度——这是对 Matryoshka 检索范式的实质性概念扩展，且可推广到其他层级空间检索场景。\n2. **检索-定位联合训练的协同效应假设**: 将 detection 领域的经典洞见（端到端 joint training 优于分阶段 pipeline）迁移到 VDR 领域，提出可测试的具体假设。\n3. **端到端多粒度检索 + 空间定位统一模型**: 将 3-model pipeline 压缩为单一模型，同时新增定位能力——实用价值明确。\n\n这些贡献对领域有**中到高价值**。如果协同假设被实验验证，这将成为该子领域的 foundational 工作；即使协同效应不显著，Spatially-Typed Matryoshka 和端到端统一本身也是有价值的贡献。\n\n【方法合理性】:\n方法整体合理，设计选择有据可循：\n- 基于 Qwen3-VL-8B + 双向注意力与 SOTA (Nemotron ColEmbed V2) 使用相同 backbone，确保公平比较。\n- 自回归 localization head (~150M) 附加在 VLM patch embedding 上——灵感来自 Localization Heads (CVPR 2025) 的发现，但通过可学习参数（6 层 transformer decoder）替代 training-free probing，是合理的升级。\n- DocLayNet 预训练 + MMDocIR 联合微调的两阶段训练策略与领域标准实践一致。\n- L1 + GIoU 联合损失是目标检测领域的标准选择。\n\n**更简单的替代方案**: 一个关键问题是——能否用 AGREE 风格的注意力代理 + 后处理 bbox 提取达到类似效果，而无需引入 150M 的 localization head？Proposal 通过 ablation #1（用外部解析器或固定网格替换 localization head）部分回答了这个问题，但审稿人可能还会要求一个\"注意力热力图 → bbox\"的更轻量 baseline。另外，Snappy 已在训练免费条件下达到 59.7% IoU@0.5 on BBox-DocVQA，GroundVDR 需要证明学习式方法的增量收益足以 justify 额外的模型复杂度和训练成本。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — 多粒度 VDR + 空间定位的端到端统一是领域公认的 open problem（Multi-Granularity Framework 论文明确列为 open question），ViDoRe V3 grounding 评估中 model F1=0.089 vs. human F1=0.602 的巨大差距量化了需求。问题定义精准且有实际应用价值（RAG context cropping）。\n\n  2. 方法与创新: 【强-】 — Spatially-Typed Matryoshka 是对 MetaEmbed (ICLR 2026 Oral) 的实质性概念扩展，不是简单的 incremental work。检索-定位协同假设有 R-CNN→Faster R-CNN 的成熟类比支撑。与所有竞争工作的区分度清晰：vs. AGREE（直接 bbox vs. 代理注意力）、vs. Hydra（联合训练 vs. 独立模式）、vs. MURE（输出侧 vs. 输入侧 Matryoshka）、vs. PixSearch（独立检索 vs. RAG 范式）、vs. ReAlign（直接坐标 vs. 文本桥接）。减分项：整体是已有技术的精巧组合（late interaction + localization head + Matryoshka + type tags），每个组件单独看不算全新，创新主要在于组合方式和协同假设。\n\n  3. 实验设计: 【强】 — 这是该 proposal 最突出的维度。4 类 baseline 覆盖页面级、区域级、定位、统一模型；6 个 ablation 精准对应每个设计选择（localization head、Matryoshka nesting、联合损失协同、type tags、layer selection、truncation Pareto curve）。特别赞赏：ablation #3 用 3 seed + paired significance test 直接检验核心协同假设；独立 localization head 评估（DocLayNet COCO mAP）验证核心假设；ViDoRe V3 grounding 标签仅用于 zero-shot 评估（避免数据泄露）；compute-normalized comparison。相比该领域很多只做 nDCG 对比的论文，这套实验设计的严谨度显著高于平均水平。\n\n  4. 可行性: 【中+】 — 计算预算 ~480 H100-hours 对学术实验室可行（小型 GPU 集群 2-3 周）。DocLayNet 和 MMDocIR 均为公开数据集。主要风险：(a) VLM patch embedding 对文档 layout 的定位能力是核心假设但未经验证——Localization Heads (CVPR 2025) 仅在自然图像上验证，文档的高度结构化布局可能更有利也可能引入新挑战；(b) 同时在三个粒度达到竞争力水平需要精心的 loss balancing 和训练策略；(c) 自回归 localization head 的推理延迟可能影响端到端效率优势。但 proposal 对这些风险有清醒认识，并设计了相应的验证实验（独立 localization head 评估、效率 breakdown 报告）。\n\n  5. 写作与呈现: 【强】 — 逻辑链清晰：问题（pipeline 冗余 + 缺少定位）→ 假设（检索-定位协同）→ 方法（统一架构）→ 验证（精准 ablation）。文献定位极其详尽，对 10+ 竞争工作逐一做了差异化分析。技术描述精确（架构细节、训练策略、loss 设计均有具体参数）。唯一小问题：proposal 篇幅较长，实际论文需要大幅压缩，如何在 8 页内呈现如此丰富的内容是一个写作挑战。\n\n【概率估计】: [33% - 47%] 中位 40%\n\n【估计理由】:\n上调因素：(1) 占据了领域公认的 open problem（端到端多粒度 + 定位统一），且该 problem 刚被 ViDoRe V3 和 Multi-Granularity Framework 的 2025-2026 论文正式提出/量化，timing 非常好；(2) Spatially-Typed Matryoshka 概念是对 ICLR 2026 Oral 工作的实质扩展，创新度足够；(3) 实验设计的完备度在该领域中属于上乘——6 个 ablation 的设计显示出对方法论的深刻理解；(4) 与竞争工作的区分度非常清晰，positioning 几乎无可挑剔；(5) 计算预算合理，不需要超大规模资源。\n\n下调因素：(1) 核心假设（VLM patch embedding → 文档 layout detection 质量）尚未验证，如果 localization head 在文档上表现不佳，整个方法基础动摇；(2) 同时追求三个粒度的竞争力有过度野心风险——如果页面级 nDCG 不及 Nemotron ColEmbed V2、区域级不及 Multi-Granularity Framework、定位 F1 仅 0.2，审稿人可能认为\"什么都做但都不够好\"；(3) 方法是多个已有技术的精巧组合，审稿人可能质疑 technical depth；(4) 领域竞争非常激烈，2025-2026 年有大量并发工作，提交时可能面临更多新 SOTA。\n\n综合看，这是一份准备充分、定位精准的 proposal，如果实验结果验证了协同假设（尤其是 ablation #3 显示统计显著的联合训练收益），有较好的中稿机会。40% 中位反映了\"方向正确、设计扎实、但实验结果未知且领域竞争激烈\"的综合判断。\n\n【主要风险】:\n1. **核心假设失败风险**: VLM patch embedding 在文档图像上的 layout detection 质量可能不足以支撑有效的 region proposal——如果 localization head 的 mAP 显著低于 HybriDLA (83.5%)，则下游的区域级检索和定位质量都会受影响，导致联合训练的收益无法体现。\n2. **\"样样通但样样不精\"风险**: 在页面级检索上可能不敌专注页面级的 Nemotron ColEmbed V2，在区域级检索上可能不敌 3-model pipeline，定位 F1 目标 0.2 的绝对值偏低——审稿人可能认为统一模型在每个维度都 compromise 了质量，总体贡献不够有说服力。\n\n【实施评估】:\n  - 计算资源: ~480 H100-hours 总计（Phase 1: 30h, Phase 2: 150h, Ablations: 100h, Multi-seed: 200h）。对有小型 GPU 集群的学术实验室可行，约 2-3 周完成。\n  - 数据需求: DocLayNet (~80K layout-annotated pages, 公开), MMDocIR (173K bootstrapped + 1,685 expert annotations, 公开), ViDoRe V1/V2/V3 (公开评测集), BBox-DocVQA (公开)。所有数据集均为公开可获取，无数据获取瓶颈。\n  - 人工介入: 低。无需人工标注——利用已有公开标注数据集。实验设计和调参需要研究者投入。\n  - 训练需求: 两阶段训练——Phase 1 (localization head 预训练) 和 Phase 2 (LoRA backbone + 联合微调)。需要实现自回归 localization head、spatially-typed Matryoshka embedding、联合 loss。工程复杂度中等偏高。\n  - 新 Benchmark: 不需要。完全基于已有公开 benchmark (ViDoRe V1/V2/V3, MMDocIR, BBox-DocVQA, DocLayNet)。\n  - 预估周期: 实现 + 训练 + 实验 + 论文撰写约 2.5-3.5 个月。其中模型实现 ~3 周，训练 + ablation ~3 周，分析 + 撰写 ~3-4 周。\n```\n\nSources:\n- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449)\n- [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models](https://arxiv.org/abs/2602.03992)\n- [MetaEmbed: Scaling Multimodal Retrieval at Test-Time (ICLR 2026 Oral)](https://arxiv.org/abs/2509.18095)\n- [MetaEmbed GitHub - Facebook Research](https://github.com/facebookresearch/MetaEmbed)\n- [A Multi-Granularity Retrieval Framework for Visually-Rich Documents](https://arxiv.org/abs/2505.01457)\n- [MMDocIR: Benchmarking Multi-Modal Retrieval for Long Documents](https://mmdocrag.github.io/MMDocIR/)\n- [MURE: Hierarchical Multi-Resolution Encoding for VDR](https://arxiv.org/abs/2603.13349)\n- [Hydra: Unifying Document Retrieval and Generation](https://arxiv.org/abs/2603.28554)\n- [AGREE: Attention Grounded Enhancement for Visual Document Retrieval](https://arxiv.org/abs/2511.13415)\n- [Snappy: Spatially-Grounded Document Retrieval](https://arxiv.org/abs/2512.02660)\n- [ReAlign: Reasoning-Guided Fine-Grained Alignment (SIGIR 2026)](https://arxiv.org/abs/2604.07419)\n- [PixSearch: Pixel-Grounded Retrieval](https://arxiv.org/abs/2601.19060)\n- [Localization Heads in Vision-Language Models (CVPR 2025 Highlight)](https://arxiv.org/abs/2503.06287)\n- [ViDoRe Benchmark V2](https://arxiv.org/pdf/2505.17166)\n- [ViDoRe Benchmarks for Visual Retrieval](https://www.emergentmind.com/topics/vidore-benchmarks)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have comprehensive research to make a well-informed assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992) (arXiv 2026): 当前 ViDoRe V3 SOTA，8B 模型 nDCG@10 = 63.42。使用 Qwen3-VL-8B + 双向注意力 + 硬负样本挖掘。GroundVDR 使用相同的 backbone 和双向注意力策略，验证了技术路线的合理性，但也意味着 page-level 性能上限可能被 Nemotron 卡住。\n- [MetaEmbed](https://arxiv.org/abs/2509.18095) (ICLR 2026 Oral): 提出 Matryoshka Multi-Vector Retrieval (MMR)，沿 token 数量维度做嵌套。GroundVDR 声称在第三个正交轴（空间-语义粒度）上扩展 Matryoshka 框架，这是一个清晰且有实质性的差异化。\n- [Multi-Granularity Framework](https://arxiv.org/html/2505.01457v2) (arXiv 2025): MMDocIR 上达 65.56 nDCG，但需要 ColQwen2 + GME + Qwen2.5-VL + OCR 四个组件。明确将端到端统一作为 open question 留出——这正是 GroundVDR 试图填补的空白。\n- [AGREE](https://arxiv.org/abs/2511.13415) (SIGIR 2026): 用 MLLM 注意力作为代理空间监督信号，改善页面级 nDCG 但不产生边界框。GroundVDR 从代理注意力升级到直接框回归，差异明确。\n- [Snappy](https://arxiv.org/abs/2512.02660) (arXiv 2025): 推理时无训练的空间定位，ColQwen3-4B 达 IoU@0.5 = 59.7%。作为 training-free lower bound，GroundVDR 的 learned 方案理应显著超越。\n- [MURE](https://arxiv.org/abs/2603.13349) (arXiv 2026): 输入侧多分辨率 Matryoshka（RMRL），无学习到的 region proposal 或框预测。GroundVDR 的输出侧空间-语义粒度嵌套是正交且互补的方向。\n- [Hydra](https://arxiv.org/abs/2603.28554) (arXiv 2026): LoRA 开关统一检索和生成，两个任务独立模式无共享损失。GroundVDR 的联合训练共享损失设计有实质区别。\n- [ReAlign](https://arxiv.org/abs/2604.07419) (SIGIR 2026): 用 VLM 推理生成文本描述作为间接空间监督，通过 KL 散度对齐检索器。GroundVDR 的直接框回归保留精确坐标、可端到端优化，差异清晰。\n- [ColParse](https://arxiv.org/abs/2603.01666) (arXiv 2026): 依赖外部 parser 的 layout-informed 子图像检索，95% 存储压缩但无法联合优化。\n- [PixSearch](https://arxiv.org/abs/2601.19060) (arXiv 2026): RAG 范式下的 pixel-level 分割 + 检索触发，与 GroundVDR 的离线索引 + 在线查询的独立检索范式不同。\n- [Localization Heads](https://arxiv.org/abs/2503.06287) (CVPR 2025 Highlight): 证明 VLM 中 ~3 个注意力头即可实现竞争性定位，但仅在自然图像上验证。GroundVDR 的核心假设之一是该能力可迁移到文档图像——这是一个需要验证的经验性问题。\n- [ViDoRe V3](https://arxiv.org/abs/2601.08620) (arXiv 2026): 3,099 条人工标注查询，包含边界框定位评估。最佳模型 F1 仅 0.089 vs 人类 0.602，量化了巨大的 grounding gap。\n- [MMDocIR](https://arxiv.org/abs/2501.08828) (EMNLP 2025): 1,685 专家标注 + 173K 引导标注，页面级 + 布局级双任务。GroundVDR 拟用其训练集做联合微调。\n\n- 调研总结: 视觉文档检索领域在 2025-2026 极度活跃，page-level 检索已趋于成熟（Nemotron 63.42 nDCG@10），但 sub-page 多粒度检索仍依赖多模型流水线，空间定位（grounding）几乎是未开发的蓝海（0.089 vs 0.602 F1 gap）。GroundVDR 精准定位了\"联合检索+定位的端到端单模型\"这一明确空白，是当前竞争格局中尚无直接竞品的位置。\n\n【整体印象】:\n作为审稿人，第一反应是**倾向 weak accept / borderline accept**。这是一篇极其精心准备的 proposal：\n1. 问题定义清晰且有量化证据支撑（28.5pp 检索 gap，0.089 vs 0.602 grounding F1 gap）\n2. 文献综述异常全面，逐一与 10+ 竞品对比并明确差异化\n3. 方法设计有清晰的结构性洞察（detection 领域 multi-stage → end-to-end 的类比）\n4. 实验方案极其完备，6 个 ablation 直接对应 6 个设计决策\n5. 计算预算合理透明\n\n但核心风险在于：(a) synergy hypothesis 可能不成立或效果有限；(b) 文档图像上 localization head 的性能是未验证的核心假设；(c) 方法组合性较强（backbone + localization head + type tags + Matryoshka nesting + joint loss），审稿人可能质疑工程堆叠 vs. 原理性创新。\n\n【核心贡献】:\n1. **首个端到端联合检索+空间定位的单一 VDR 模型**：将当前 3-model pipeline 压缩为单模型，同时新增 grounding 能力——这是文献中明确的空白。\n2. **Spatially-Typed Matryoshka Multi-Vector Embeddings**：在 MetaEmbed 的 token-count 维度和 MURE 的 input-resolution 维度之外，引入第三个正交嵌套轴（page → region → element 的空间-语义粒度层级）。概念新颖，且有 test-time granularity control 的实用价值。\n3. **Retrieval-Grounding Synergy Hypothesis 的系统验证**：通过 ablation #3 直接检验联合训练 vs. 分别训练的增益——这是一个有科学意义的实验。\n\n价值评估：如果 synergy hypothesis 得到验证且性能提升显著，这将是该领域一个重要的方法论贡献。即使 synergy 较弱，单模型统一多粒度检索+定位本身也有工程和应用价值。\n\n【方法合理性】:\n方法整体合理，各组件有独立的先行工作支撑：\n- Qwen3-VL-8B + 双向注意力 + LoRA：跟随 Nemotron ColEmbed V2 的成功配方\n- 自回归 localization head：受 Localization Heads (CVPR 2025) 启发，但从自然图像迁移到文档是未验证的假设\n- Late-interaction contrastive loss + box regression loss (L1 + GIoU)：两个损失项各自是标准做法\n- Spatially-Typed Matryoshka：是 MetaEmbed MMR 的自然扩展\n\n**潜在的更简单替代方案**：\n1. 直接用外部高质量 parser（如 HybriDLA, AAAI 2026, 83.5% mAP）+ 现有 retriever（如 Nemotron/MetaEmbed），以更少工作量构建多粒度检索。但 proposal 正确指出这无法联合优化且有 error cascading。\n2. AGREE 式注意力代理监督 + Snappy 式推理时定位。但 proposal 合理论证了学习式定位应优于这些启发式方法。\n\n方法中值得关注的设计风险：\n- 自回归 localization head（150M params, 6-layer transformer decoder）在推理时增加延迟——proposal 承诺报告延迟 breakdown，但审稿人可能要求与外部 parser 做延迟对比\n- Type tag 路由机制的实际效果可能有限——如果 late interaction 已自然学习到粒度区分，显式 type tag 可能是冗余信号\n\n【5 维度打分】:\n\n1. 研究问题: 【强】\n   — 问题有精确量化支撑：ViDoRe V3 grounding gap (0.089 vs 0.602 F1) 和 MMDocIR page-vs-layout gap (28.5pp) 都是已发表 benchmark 上的真实数字。Multi-Granularity Framework 明确将端到端统一留为 open question。这不是人造的问题，而是领域的真实痛点，且影响下游 RAG 系统的 context 质量。\n\n2. 方法与创新: 【中偏强】\n   — 与 MetaEmbed (ICLR 2026 Oral) 对比：MetaEmbed 沿 token 数量嵌套，GroundVDR 沿空间-语义粒度嵌套——第三轴扩展概念新颖但本质上是架构组合创新。\n   — 与 AGREE (SIGIR 2026) 对比：从代理注意力监督升级到直接框回归——技术路径明确且合理，但\"升级\"而非\"范式变革\"。\n   — 与 Hydra (arXiv 2026) 对比：从独立模式到联合训练——差异清晰但需要实验验证 synergy 的实际增益幅度。\n   — 与 Localization Heads (CVPR 2025) 对比：从自然图像扩展到文档图像——方向合理但迁移假设需验证。\n   — 总体：方法是\"正确方向上的自然下一步\"而非\"意料之外的创新\"，创新来自组件的新颖组合和新的嵌套轴。对于 AAAI，这在 novelty 门槛之上但不算突出。\n\n3. 实验设计: 【强】\n   — Baselines 覆盖 4 大类（page-level/sub-page/grounding/unified），包括所有主要竞品\n   — 6 个 ablation 逐一验证 6 个设计决策，ablation #3（synergy hypothesis）设计 3-seed + paired significance test，方法论严谨\n   — 独立 localization head 评估（DocLayNet 上 COCO-style mAP）直接验证核心假设\n   — 多 benchmark（ViDoRe V1/V2/V3, MMDocIR, BBox-DocVQA）+ 效率指标 + compute-normalized 对比\n   — Grounding targets 有量化目标（0.2 F1 minimum, 0.3+ stretch）和 per-modality breakdown\n   — 这个实验设计本身是 proposal 的重要加分项，即使方法创新属于\"组合式\"，完备的实验方案能有效弥补\n\n4. 可行性: 【中偏强】\n   — 480 H100-hours 合理，且有清晰的 per-phase 分解（30 + 150 + 100 + 200）\n   — 训练数据来源明确：DocLayNet (80K, 公开), MMDocIR (173K, 公开)\n   — 风险点：(a) localization head 在文档上可能需要大量调参才能达到满意的 mAP；(b) 联合训练两个异质损失（contrastive + regression）的平衡可能需要大量超参搜索，proposal 未详述损失权重策略；(c) 自回归 localization head 的推理延迟可能影响实际部署，审稿人可能要求延迟分析\n   — 2-3 周完成有前提——需要 GPU 集群能持续分配且无排队，实际可能需要 4-6 周\n\n5. 写作与呈现: 【强】\n   — 逻辑链条清晰：问题量化 → 假设陈述 → 类比论证（R-CNN → Faster R-CNN）→ 方法设计 → 实验验证\n   — 文献定位异常精准，逐一与 10+ 竞品明确差异化，Critical distinction 标注到位\n   — 核心假设（VLM patch embeddings 对文档布局的适用性）被明确标注为\"需验证的经验性问题\"——诚实且专业\n   — 方法描述有清晰的 4-step inference pipeline，便于理解\n   — 不足：部分细节过度压缩（如 type tag 的具体实现、损失权重策略、多粒度索引的具体数据结构），但对 proposal 阶段已足够\n\n【概率估计】: [30% - 45%] 中位 37%\n\n【估计理由】:\n**上行因素（推向 45%）**：\n- 研究问题有强量化支撑，领域公认的空白\n- 实验设计极其完备，堪称 proposal 级别的标杆\n- 写作和定位质量高，审稿人不太会因理解困难而给低分\n- 如果 synergy hypothesis 被验证（即使 modest gain），叙事完整度很高\n- Grounding 是 VDR 领域的新兴热点，timing 好\n\n**下行因素（推向 30%）**：\n- 方法创新属于\"组件组合\"类型，可能被审稿人视为 engineering contribution\n- Synergy hypothesis 可能不成立或增益微弱（<2pp），则论文核心叙事动摇\n- 领域竞争极度激烈（MURE, ColParse, AGREE, ReAlign, Hydra 都是同期竞品），AAAI 该方向投稿密度可能很高\n- 文档图像 localization head 是未验证的核心假设，失败概率非零\n- 系统复杂度高（多个新组件叠加），审稿人可能要求逐一证明每个组件的必要性——6 个 ablation 可以应对但篇幅压力大\n\n**中位 37% 的逻辑**：这是一篇方向正确、准备充分、问题真实的 solid 投稿。它不是那种\"一看就会 accept\"的突破性工作，但也远不是弱稿。在 AAAI 2026 的竞争强度下，高质量的实验执行和 synergy hypothesis 的验证结果将是决定因素。如果实验结果 deliver（synergy 增益 ≥ 3pp + grounding F1 ≥ 0.25），概率可上移至 40-45%；如果实验结果 underwhelming，概率下移至 28-32%。\n\n【主要风险】:\n1. **Synergy hypothesis 验证失败**：如果 ablation #3 显示联合训练与分别训练无显著差异（或差异 <1pp），论文的核心叙事（\"retrieval-grounding synergy\"）将严重受损。此时论文退化为\"一个工程上集成了多功能的系统\"，novelty 主要靠 Spatially-Typed Matryoshka 概念支撑，对 AAAI 可能不够。\n2. **方法被质疑为 engineering stacking**：backbone + localization head + type tags + Matryoshka + joint loss 的组合可能让审稿人质疑\"每增加一个组件带来了多少性能提升？总提升中有多少来自工程优化而非方法论创新？\"——虽然 6 个 ablation 设计了应对方案，但如果个别组件贡献微弱，会削弱整体说服力。\n\n【实施评估】:\n  - 计算资源: ~480 H100-hours，需要小型 GPU 集群（4-8 块 H100）。对 well-funded 学术实验室可行，对资源有限的团队有压力。Multi-seed 实验（200 H100-hours）是大头，可适当削减。\n  - 数据需求: DocLayNet (80K, 公开 COCO 格式) + MMDocIR (173K bootstrapped + 1,685 expert, 公开 HuggingFace) + ViDoRe V3 (3,099 queries, 公开)。所有数据公开可用，无数据瓶颈。\n  - 人工介入: 中等。需要大量超参搜索（联合损失权重平衡、localization head 架构调参、Matryoshka 嵌套策略）。Layout 标注使用现有数据集，无需新标注。\n  - 训练需求: 两阶段训练（Phase 1 预训练 localization head, Phase 2 联合微调 LoRA + localization head）。需要实现自定义的 autoregressive localization head 和 spatially-typed Matryoshka embedding pooling。工程量较大但无需从零训练 foundation model。\n  - 新 Benchmark: 不需要。完全使用现有 benchmark（ViDoRe V1/V2/V3, MMDocIR, BBox-DocVQA, DocLayNet）。\n  - 预估周期: 实现 + 调参 + 实验 + 论文写作：约 3-4 个月。其中代码实现 ~3-4 周，实验运行 ~3-4 周（考虑排队和调参），论文撰写 ~2-3 周。\n```\n\n---\n\nSources:\n- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992)\n- [MetaEmbed (ICLR 2026 Oral)](https://arxiv.org/abs/2509.18095)\n- [Multi-Granularity Retrieval Framework](https://arxiv.org/html/2505.01457v2)\n- [AGREE (SIGIR 2026)](https://arxiv.org/abs/2511.13415)\n- [Snappy](https://arxiv.org/abs/2512.02660)\n- [MURE](https://arxiv.org/abs/2603.13349)\n- [Hydra](https://arxiv.org/abs/2603.28554)\n- [ReAlign (SIGIR 2026)](https://arxiv.org/abs/2604.07419)\n- [ColParse](https://arxiv.org/abs/2603.01666)\n- [PixSearch](https://arxiv.org/abs/2601.19060)\n- [Localization Heads (CVPR 2025 Highlight)](https://arxiv.org/abs/2503.06287)\n- [ViDoRe V3](https://arxiv.org/abs/2601.08620)\n- [MMDocIR](https://arxiv.org/abs/2501.08828)\n- [ColPali (ECIR 2025)](https://arxiv.org/abs/2407.01449)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Learned Spatial Grounding for Multi-Granularity Visual Document Retrieval\n\n## Core Problem\n\nCurrent visual document retrieval (VDR) models operate at page granularity or require multi-model pipelines with external layout parsers to access element-level content. The SOTA multi-granularity pipeline (Multi-Granularity Framework, arXiv:2505.01457) requires three separate large models (ColQwen2 + GME + Qwen2.5-VL) plus OCR — incurring 3× memory, pipeline latency, and error cascading (OCR errors → layout errors → retrieval errors). No single model jointly learns to retrieve at page, region, and element granularities while producing spatially grounded evidence bounding boxes. The 28.5pp page-vs-layout retrieval gap on MMDocIR (arXiv 2025) and the 0.089 vs. 0.602 model-vs-human grounding F1 on ViDoRe V3 (arXiv 2026) quantify this deficiency.\n\n## Research Hypothesis\n\n**Retrieval-Grounding Synergy**: Joint training of contrastive retrieval and bounding-box regression in a single VLM produces mutually reinforcing learning signals — grounding loss preserves spatial position information in the embedding space, directly benefiting region- and element-level retrieval, while retrieval loss provides semantic discriminability that improves grounding precision. This mirrors the well-established synergy in object detection: the transition from multi-stage pipelines (R-CNN: separate feature extraction → proposal → classification) to end-to-end joint training (Faster R-CNN/YOLO) consistently improved both localization and classification, precisely because the two tasks share spatial-semantic representations. GroundVDR applies the same structural insight to VDR — jointly learning where (grounding) and what (retrieval) through shared spatial-semantic embeddings.\n\nIndirect evidence: AGREE (SIGIR 2026, arXiv:2511.13415) showed that even proxy attention-based spatial signals improve page-level nDCG by 12.82%. GroundVDR elevates this from proxy attention supervision to direct box regression supervision, which should yield stronger spatial encoding and produce actionable bounding boxes.\n\n## Research Landscape\n\n**Page-level VDR.** Nemotron ColEmbed V2 (arXiv 2026) leads ViDoRe V3 at 63.42 nDCG@10 using bidirectional attention and hard negative mining on Qwen3-VL-8B. ColPali (ECIR 2025) established the vision-language late-interaction retrieval paradigm. MetaEmbed (ICLR 2026 Oral, arXiv:2509.18095) introduced Matryoshka Multi-Vector Retrieval (MMR) with learnable Meta Tokens, nesting along the token-count dimension for coarse-to-fine retrieval; 3B achieves 60.3% nDCG@5 on ViDoRe V2.\n\n**Sub-page / region-level retrieval.** The Multi-Granularity Framework (arXiv:2505.01457) achieves 65.56 on MMDocIR but requires three separate large models plus OCR, explicitly leaving end-to-end unification as an open question. RegionRAG (AAAI 2026) learns query-patch alignment but relies on BFS heuristic with manual threshold for patch grouping. ColParse (arXiv 2026, arXiv:2603.01666) achieves 95% storage reduction via layout-informed sub-images but depends on an external parser that cannot be jointly optimized. MURE (arXiv 2026, arXiv:2603.13349) introduces Resolution-level Matryoshka Representation Learning (RMRL), nesting embeddings across input resolutions (multi-resolution sampling). **Critical distinction**: MURE's Matryoshka operates on the input side (resolution hierarchy), while GroundVDR's operates on the output side (spatial-semantic granularity hierarchy: page → region → element). MURE performs no learned region proposals or bounding-box prediction.\n\n**Unified multi-task VDR.** Hydra (arXiv 2026, arXiv:2603.28554) unifies retrieval and generation in a single VLM via LoRA toggle — enabling LoRA yields ColBERT-style embeddings, disabling it recovers generation with byte-identical outputs. However, Hydra's two tasks are independent modes (no shared loss, no mutual reinforcement), whereas GroundVDR's retrieval and grounding are jointly trained with a shared loss, hypothesizing explicit synergy.\n\n**Spatial grounding in retrieval.** AGREE (SIGIR 2026, arXiv:2511.13415) uses MLLM attention as proxy supervision, improving page-level nDCG but producing no bounding boxes. Snappy (arXiv 2025, arXiv:2512.02660) achieves 59.7% IoU@0.5 on BBox-DocVQA purely at inference time with no learned optimization. ReAlign (SIGIR 2026, arXiv:2604.07419) uses VLM reasoning to identify query-relevant regions, then generates textual descriptions as supervision to align retriever rankings via KL divergence — a text-bridged indirect spatial supervision approach. GroundVDR differs fundamentally: direct box regression preserves precise spatial coordinates (vs. ReAlign's lossy text compression), is end-to-end optimizable (vs. ReAlign's frozen VLM teacher), and produces bounding boxes directly usable for downstream RAG context cropping. PixSearch (arXiv 2026, arXiv:2601.19060) combines retrieval with region-level grounding but differs in three ways: (1) retrieval is generation-time dynamic triggering (retrieval-augmented generation paradigm) vs. GroundVDR's offline indexing + online query (standalone retrieval paradigm); (2) grounding produces pixel-level segmentation masks vs. bounding boxes (less natural for rectangular document layouts); (3) no hierarchical multi-granularity embedding structure with test-time granularity control. On ViDoRe V3's grounding evaluation, the best model achieves only 0.089 F1 vs. 0.602 human F1. Localization Heads (CVPR 2025 Highlight, arXiv:2503.06287) show that ~3 attention heads in VLMs suffice for competitive grounding on natural images without fine-tuning.\n\n**Key gap.** No existing work jointly learns retrieval and spatial grounding with direct bounding-box supervision in a single end-to-end model. The detection and retrieval communities have independently developed the necessary components but never unified them.\n\n## Proposed Approach\n\nWe propose **GroundVDR**, a single vision-language model that jointly performs multi-granularity document retrieval and spatial grounding end-to-end, compressing the current 3-model pipeline into one model while adding grounding capabilities that no existing single model provides.\n\n**Architecture.** Built on Qwen3-VL-8B with bidirectional attention (LoRA r=64 on backbone). An autoregressive localization head (6-layer transformer decoder, ~150M parameters, fully trained) is attached to VLM patch embeddings to predict region bounding boxes as coordinate token sequences, replacing external parsers.\n\n**Core assumption (to be validated):** VLM patch embeddings contain sufficient spatial and semantic information for high-quality document region proposals. While Localization Heads (CVPR 2025) demonstrated this for natural images, document layouts differ structurally. We hypothesize that documents' highly structured, grid-like layouts are actually more amenable to patch-level spatial reasoning than cluttered natural scenes — but this is an empirical question central to the paper, addressed by independent evaluation of the localization head on DocLayNet.\n\n**Spatially-Typed Matryoshka Multi-Vector Embeddings.** MetaEmbed nests along the token-count dimension; MURE nests along the input-resolution dimension. GroundVDR introduces a third, orthogonal nesting axis: **spatial-semantic granularity**. Each embedding vector carries a learned type tag encoding its position in the document's spatial hierarchy (page / region-type / element-type). During late interaction, type tags enable heterogeneous matching — a region-level query preferentially interacts with region-typed embeddings, while a page-level query aggregates across all types. This extends the Matryoshka framework from a precision-efficiency tradeoff to a spatial-semantic granularity tradeoff with test-time control. The extension is not limited to VDR — any retrieval scenario with hierarchical spatial structure (e.g., map retrieval, medical imaging) could benefit, though this paper focuses on document retrieval.\n\n**Inference Pipeline (4 steps):**\n1. Document page → backbone bidirectional encoding → patch embeddings\n2. Patch embeddings → localization head (autoregressive decoding) → region bounding boxes\n3. Region boxes → crop & pool patch embeddings → region-level and element-level spatially-typed Matryoshka embeddings; page-level embedding aggregated from all patches\n4. Multi-granularity index: page/region/element embeddings indexed separately; query-time granularity selection via type-tag routing\n\n**Joint Loss.** Late-interaction contrastive retrieval loss + bounding-box regression loss (L1 + GIoU), with gradient flowing from both losses through the shared backbone. The synergy hypothesis predicts that joint training outperforms separate training of either task — tested directly in ablation #3.\n\n**Training Data Strategy.**\n- Phase 1: Localization head pre-training on DocLayNet (KDD 2022, ~80K layout-annotated pages, 11 classes, COCO format) for general document layout detection (~30 H100-hours).\n- Phase 2: Joint fine-tuning on MMDocIR's 173K bootstrapped layout annotations + 1,685 expert annotations for retrieval + grounding alignment (~150 H100-hours). Grounding-capable layers selected using Localization Heads' probing protocol.\n- Grounding evaluation: ViDoRe V3's 3,099 human-verified queries used exclusively for zero-shot evaluation (no training on ViDoRe V3 grounding labels to prevent data leakage).\n\n## Experimental Design\n\n**Baselines (4 categories):**\n- Page-level retrieval: Nemotron ColEmbed V2 (8B), MetaEmbed (3B/7B), ColPali/ColQwen2, BM25+OCR\n- Sub-page/region-level retrieval: MURE, ColParse, RegionRAG, Multi-Granularity Framework (pipeline upper bound)\n- Grounding: Snappy (training-free lower bound, reproduced on ViDoRe V3), AGREE (attention-proxy baseline)\n- Unified single-model: Hydra (retrieval+generation, no grounding → grounding column marked N/A)\n\n**Benchmarks and Metrics:**\n- ViDoRe V1/V2/V3: nDCG@{5,10} for retrieval; IoU@{0.25, 0.5, 0.7}, mean IoU, Dice/F1 for grounding (V3 only)\n- MMDocIR: page-level nDCG@{5,10} and layout-level nDCG@{5,10} reported separately\n- BBox-DocVQA: IoU@{0.25, 0.5, 0.7} for grounding (supplementary, aligns with Snappy's primary benchmark)\n- Efficiency: storage cost (embeddings per page × dimension, bytes per page), per-page encoding latency (ms) with breakdown (backbone / localization head / pooling+indexing), training cost (GPU-hours per phase)\n- Compute-normalized comparison: training FLOPs (or GPU-hours) vs. performance for all methods\n\n**Grounding targets:** 0.2 F1 as minimum viable (2.2× current SOTA 0.089), 0.3+ F1 as stretch target. Per-modality breakdown (text 60.4% / image 18.8% / table 16.7%) to analyze where grounding gains concentrate.\n\n**Ablation Studies (6 experiments):**\n1. Replace learned localization head with external parser (HybriDLA) or fixed grid → quantify learned vs. external proposals on retrieval quality\n2. Remove Matryoshka nesting → flat multi-vector → quantify hierarchical nesting contribution per granularity level\n3. Remove joint loss → train retrieval-only and grounding-only variants separately → **directly test the synergy hypothesis** (3 seeds, paired significance test)\n4. Remove spatial type tags → uniform embedding type → quantify type-aware heterogeneous interaction value\n5. Layer selection: vary which backbone layers feed the localization head → validate probing protocol for document images\n6. Matryoshka truncation tradeoff: performance at page-only / page+region / page+region+element embedding levels → Pareto curve (storage vs. nDCG), compared against MetaEmbed group-size tradeoff and MURE resolution tradeoff\n\n**Independent Localization Head Evaluation:** Report COCO-style mAP@{0.5, 0.5:0.95, 0.75} on DocLayNet test set, compared against HybriDLA (83.5% mAP, AAAI 2026) and other layout detection baselines. This directly validates the core assumption about VLM patch embeddings for document layout analysis.\n\n**Compute Budget:**\n- Phase 1 (localization head pre-training, DocLayNet 80K): ~30 H100-hours\n- Phase 2 (backbone LoRA + joint fine-tuning, MMDocIR 173K): ~150 H100-hours\n- Ablation experiments (6 ablations, ~30-50% of main training each): ~100 H100-hours\n- Multi-seed: 2 seeds for main results, 3 seeds for ablation #3 → additional ~200 H100-hours\n- **Total: ~480 H100-hours**, reproducible by academic labs with a small GPU cluster over 2-3 weeks\n\n## Key References\n\n- Nemotron ColEmbed V2 (arXiv 2026)\n- ColPali: Efficient Document Retrieval with Vision Language Models (ECIR 2025)\n- MMDocIR: Multi-Modal Document Information Retrieval (arXiv 2025)\n- ViDoRe V3: Visual Document Retrieval Benchmark with Grounding (arXiv 2026)\n- MetaEmbed: Matryoshka Multi-Vector Retrieval (ICLR 2026 Oral, arXiv:2509.18095)\n- HybriDLA: Hybrid Diffusion-Autoregressive Document Layout Analysis (AAAI 2026)\n- RegionRAG: Region-Level RAG for Visual Document Understanding (AAAI 2026)\n- AGREE: Attention-Grounded Retriever Enhancement (SIGIR 2026, arXiv:2511.13415)\n- Snappy: Spatially-Grounded Document Retrieval (arXiv 2025, arXiv:2512.02660)\n- Localization Heads in Vision-Language Models (CVPR 2025 Highlight, arXiv:2503.06287)\n- MURE: Hierarchical Multi-Resolution Encoding for VDR (arXiv 2026, arXiv:2603.13349)\n- Hydra: Unifying Document Retrieval and Generation (arXiv 2026, arXiv:2603.28554)\n- ColParse: Layout-Informed Sub-Image Retrieval (arXiv 2026, arXiv:2603.01666)\n- Multi-Granularity Retrieval Framework (arXiv 2025, arXiv:2505.01457)\n- PixSearch: Pixel-Grounded Retrieval (arXiv 2026, arXiv:2601.19060)\n- ReAlign: Reasoning-Guided Fine-Grained Alignment (SIGIR 2026, arXiv:2604.07419)\n- DocLayNet: Document Layout Analysis Dataset (KDD 2022)"
}
````

---

### Runtime record

_source line 2 · 2026-05-30T07:30:36.201Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:30:36.201Z",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-30T07:30:36.216Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Based on my research, I now have enough context to provide a comprehensive evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:
- [ViDoRe V3] (arXiv:2601.08620, 2026): 定义了检索+定位的联合评测标准，3,099个人工标注查询，当前最佳模型grounding F1仅0.089 vs 人类0.602。这个巨大差距直接支撑了proposal的研究动机。
- [Nemotron ColEmbed V2] (arXiv:2602.03992, 2026): ViDoRe V3 SOTA，63.42 nDCG@10，基于Qwen3-VL-8B+双向注意力+hard negative mining。是page-level retrieval的直接竞争对手。
- [MetaEmbed] (ICLR 2026 Oral, arXiv:2509.18095): Matryoshka Multi-Vector Retrieval，沿token数量维度嵌套。Proposal正确区分了自己在"空间语义粒度"维度的嵌套。
- [MURE] (arXiv:2603.13349, 2026): 分辨率级别Matryoshka表示学习(RMRL)，输入侧嵌套。Proposal正确定位其差异化：输出侧空间语义层次嵌套。
- [Multi-Granularity Framework] (arXiv:2505.01457, 2025): 3模型pipeline达到MMDocIR 65.56，明确留下端到端统一作为open question。直接验证了proposal要解决的问题。
- [AGREE] (SIGIR 2026, arXiv:2511.13415): 注意力代理监督，改善page-level nDCG但无bounding box输出。Proposal的直接前驱，从proxy supervision升级到direct box regression。
- [Hydra] (arXiv:2603.28554, 2026): 单模型检索+生成，LoRA切换，但两任务独立无共享loss。Proposal强调joint training的互强化假说与之形成对比。
- [ReAlign] (SIGIR 2026, arXiv:2604.07419): VLM推理识别区域→文本描述→KL散度对齐。间接空间监督，proposal用直接box regression区分。
- [PixSearch] (arXiv:2601.19060, 2026): 端到端LMM统一区域感知与检索增强推理，但属于RAG范式(生成时动态检索)，非独立检索范式；使用pixel-level分割而非bounding box。
- [Localization Heads] (CVPR 2025 Highlight, arXiv:2503.06287): 冻结VLM中~3个注意力头即可实现竞争性定位（自然图像），核心假设的间接证据来源。
- [Snappy] (arXiv:2512.02660, 2025): 无训练patch-to-region相关性传播，BBox-DocVQA上59.7% IoU@0.5。是grounding的training-free下界。

- 调研总结: Visual Document Retrieval是2025-2026年的高活跃赛道，多模型pipeline已证明多粒度检索的价值但留下端到端统一作为明确的open question。空间定位（grounding）刚被ViDoRe V3正式纳入评测，当前模型与人类的巨大差距(0.089 vs 0.602 F1)标志着这是一个刚打开的研究窗口。Proposal精准定位在这个窗口上，且与现有工作(AGREE, ReAlign, PixSearch, Hydra)有清晰的差异化。

【整体印象】: 作为审稿人，第一反应是**倾向 weak accept**。这是一篇在活跃领域中精准定位了genuine research gap的proposal，展现了对领域的深刻理解。研究假说清晰且可证伪，实验设计非常完备（6个ablation直接测试每个设计决策）。主要犹豫在于：(1) 核心贡献可能被视为"已有组件的工程整合"而非"根本性新洞见"；(2) 系统复杂度高，成功依赖多个组件协同工作。但整体来说，这是一篇above-average的投稿。

【核心贡献】: 
1. **端到端多粒度检索+空间定位的统一**: 将3模型pipeline压缩为单模型，同时新增直接bounding box输出能力——这是文档检索领域目前不存在的能力组合。
2. **Retrieval-Grounding Synergy假说**: 提出检索loss和定位loss通过共享空间语义表征互相增强的具体机制，有可证伪的ablation设计(#3)。
3. **Spatially-Typed Matryoshka嵌套**: 在MetaEmbed（token维度）和MURE（分辨率维度）之外提出第三个正交嵌套轴（空间语义粒度），支持测试时粒度控制。

贡献价值评估：如果synergy假说成立（joint training > separate training），这将为检索+定位联合学习提供有价值的empirical evidence。pipeline压缩本身具有明确的工程价值。但如果synergy不成立，论文退化为一篇系统集成论文，价值显著降低。

【方法合理性】: 
方法总体合理，各组件有充分的先验支持：
- 双向注意力LoRA: Nemotron ColEmbed V2已验证其对检索的有效性
- 自回归定位头: Localization Heads (CVPR 2025)证明VLM patch嵌入包含空间信息；但该结论仅在自然图像上验证，文档图像需要独立验证（proposal已意识到并设计了DocLayNet评测）
- Late interaction: ColPali/ColQwen2已验证的范式
- Matryoshka训练: MetaEmbed已验证的框架

**更简单的替代方案**: 
- 是否可以用Snappy的无训练方法（patch-to-region propagation）代替learned localization head？如果能达到类似效果，150M参数的额外decoder就不必要。Proposal应在ablation中包含Snappy-style baseline。
- 是否可以直接用AGREE的注意力代理方法指导region proposal，而非训练独立的localization head？

这些替代方案的存在不构成致命问题，但审稿人很可能会提出。Ablation #1（learned vs external parser vs fixed grid）部分回答了这个问题，但缺少与Snappy-style无训练方法的直接对比。

【5 维度打分】:
  1. 研究问题: 【强】 — ViDoRe V3的grounding gap (0.089 vs 0.602 F1)和Multi-Granularity Framework明确留下的open question提供了强有力的问题动机。这是一个在benchmark层面被明确量化的痛点，具有清晰的应用价值（RAG pipeline的context cropping需要精确定位）。问题的时效性极强，研究窗口刚刚打开。

  2. 方法与创新: 【中偏强】 — 各组件单独来看并非全新（late interaction、box regression、Matryoshka训练均有先例），创新在于"组合方式"和"joint training假说"。与AGREE相比是从proxy → direct supervision的合理升级；与Hydra相比是从independent modes → joint loss的明确进步；与Multi-Granularity Framework相比是从multi-model → single-model的架构简化。Spatially-Typed Matryoshka是一个有趣的新概念但实质可能只是embedding加type tag。核心novelty高度依赖synergy假说是否成立。参考MetaEmbed(ICLR 2026 Oral)在token维度的Matryoshka创新深度，GroundVDR在空间语义维度的扩展是合理但可能被视为incremental。

  3. 实验设计: 【强】 — 这是proposal最突出的优势。4类baseline覆盖所有竞争方向（page-level、region-level、grounding、unified）；6个ablation逐一测试每个设计决策，特别是ablation #3直接验证核心假说（3 seeds + paired significance test）；多benchmark覆盖（ViDoRe V1/V2/V3 + MMDocIR + BBox-DocVQA）；效率报告包含per-component latency breakdown和compute-normalized comparison。独立的localization head评测（DocLayNet mAP）验证核心假设。grounding target设定合理（0.2 F1 = 2.2× current SOTA作为minimum viable）。相比领域标准（Nemotron ColEmbed V2只报告nDCG，无ablation breakdown），这个实验设计远超average。

  4. 可行性: 【中偏强】 — 480 H100-hours是学术实验室2-3周可完成的规模，合理可行。训练数据来源明确（DocLayNet公开80K + MMDocIR公开173K）。但风险点在于：(a) 自回归localization head在文档图像上的表现未知；(b) joint training可能需要大量超参调试（两个loss的权重平衡、梯度冲突等），实际时间可能超预估；(c) 只使用2 seeds进行主实验的统计显著性可能不够。

  5. 写作与呈现: 【强】 — Proposal逻辑极其清晰：problem → hypothesis → landscape → differentiation → approach → evaluation。每个设计决策都有明确的motivation和对应的validation计划。与竞争工作的区分非常精确（如MURE输入侧 vs GroundVDR输出侧、Hydra独立模式 vs GroundVDR联合训练、ReAlign文本桥接 vs GroundVDR直接回归）。R-CNN → Faster R-CNN的类比既准确又有说服力。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】: 
- 上行因素：研究问题timing极佳（ViDoRe V3刚开放grounding赛道）；实验设计质量在领域内属于top tier；与所有竞争工作有清晰差异化；假说可证伪性强（审稿人欣赏这一点）。
- 下行因素：创新可能被视为"known components的新组合"而非fundamental insight；系统复杂度高意味着实验结果可能不如预期clean；2025-2026该领域竞争极其激烈（每月有新SOTA），投稿时可能已有更新的工作出现；如果synergy假说不成立（ablation #3显示marginal gains），论文核心story塌缩。
- AAAI 2026接收率约20-23%。这篇proposal整体质量明显高于average submission，但在一个拥挤的赛道上面临"是否足够novel"的审稿人分歧风险。预计会获得1个positive review（appreciate thorough design）和1-2个borderline review（question novelty depth），概率分布在acceptance threshold附近。

【主要风险】: 
1. **Synergy假说不成立**: 如果ablation #3显示joint training相比separate training仅有marginal improvement（<1 nDCG point），核心贡献从"scientific insight"降级为"engineering integration"，审稿人会质疑"为什么不直接用pipeline"。
2. **Novelty perception**: 在MURE、Hydra、ColParse、ReAlign等concurrent work密集的环境下，审稿人可能认为这是"yet another system paper in VDR"，尤其是如果Spatially-Typed Matryoshka被视为trivial extension（加type tag）。

【实施评估】:
  - 计算资源: ~480 H100-hours total（含ablation和multi-seed），学术实验室4-8 GPU集群可在2-3周完成。合理且可复现。
  - 数据需求: DocLayNet (80K pages, 公开) + MMDocIR (173K bootstrapped + 1,685 expert annotations, 公开) + ViDoRe V3 (3,099 queries, 公开评测集)。全部公开可获取，无数据壁垒。
  - 人工介入: 无需额外人工标注（利用现有public datasets）。但如果MMDocIR的bootstrapped annotations质量不足，可能需要少量人工清洗。
  - 训练需求: 两阶段训练（Phase 1: localization head预训练 30h; Phase 2: joint fine-tuning 150h）。需要实现autoregressive localization head与VLM backbone的梯度连接，有一定工程复杂度。
  - 新 Benchmark: 不需要构建新benchmark。使用现有ViDoRe V1/V2/V3 + MMDocIR + BBox-DocVQA。
  - 预估周期: 实现+训练+ablation约6-8周（含调试时间）。如果joint training梯度平衡困难，可能延长至10-12周。写作2-3周。总计约2.5-3.5个月。
```

Sources:
- [ViDoRe V3: A Comprehensive Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2601.08620)
- [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models](https://arxiv.org/abs/2602.03992)
- [MetaEmbed: Scaling Multimodal Retrieval at Test-Time (ICLR 2026 Oral)](https://arxiv.org/abs/2509.18095)
- [MURE: Hierarchical Multi-Resolution Encoding for VDR](https://arxiv.org/abs/2603.13349)
- [Multi-Granularity Retrieval Framework for Visually-Rich Documents](https://arxiv.org/abs/2505.01457)
- [AGREE: Attention Grounded Enhancement for Visual Document Retrieval (SIGIR 2026)](https://arxiv.org/abs/2511.13415)
- [Hydra: Unifying Document Retrieval and Generation](https://arxiv.org/abs/2603.28554)
- [ReAlign: Reasoning-Guided Fine-Grained Alignment (SIGIR 2026)](https://arxiv.org/abs/2604.07419)
- [PixSearch: Pixel-Grounded Retrieval for Knowledgeable LMMs](https://arxiv.org/abs/2601.19060)
- [Localization Heads in VLMs (CVPR 2025)](https://arxiv.org/abs/2503.06287)
- [Snappy: Spatially-Grounded Document Retrieval](https://arxiv.org/abs/2512.02660)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- Nemotron ColEmbed V2 (arXiv 2026, arXiv:2602.03992): 当前 ViDoRe V3 榜首，nDCG@10=63.42，基于 Qwen3-VL-8B + 双向注意力 + hard negative mining。GroundVDR 使用相同 backbone（Qwen3-VL-8B），页面级检索需与之直接竞争。
- MetaEmbed (ICLR 2026 Oral, arXiv:2509.18095): Meta/Facebook 工作，Matryoshka Multi-Vector Retrieval，沿 token 数量维度做嵌套。GroundVDR 提出沿空间-语义粒度维度的第三种正交嵌套轴——这是对 Matryoshka 范式的真正扩展，有明确区分度。
- Multi-Granularity Framework (arXiv:2505.01457): 多粒度检索 SOTA (MMDocIR 65.56)，但需要 ColQwen2 + GME + Qwen2.5-VL + OCR 四组件流水线。该工作明确将"端到端统一"列为 open question——正是 GroundVDR 要回答的问题。
- MURE (arXiv:2603.13349): 输入侧分辨率 Matryoshka (RMRL)，与 GroundVDR 输出侧空间-语义 Matryoshka 正交互补。MURE 无学习式 region proposal 或 bbox 预测。
- Hydra (arXiv:2603.28554): 单模型统一检索+生成（LoRA 开关），但两任务是独立模式，无共享 loss 或协同训练。GroundVDR 的联合训练 + 协同假设提供了清晰区分。
- AGREE (SIGIR 2026, arXiv:2511.13415): 注意力作为代理空间信号，页面级 nDCG 提升 12.82%，但不产生 bounding box。GroundVDR 从代理注意力监督升级为直接 box 回归监督。
- Snappy (arXiv:2512.02660): 训练免费的空间定位，IoU@0.5=59.7% (BBox-DocVQA)。作为定位下界 baseline，GroundVDR 应大幅超越。
- ReAlign (SIGIR 2026, arXiv:2604.07419): 使用 VLM 推理生成文本描述作为空间监督信号，是间接的文本桥接方法。GroundVDR 的直接 box 回归保留精确坐标且端到端可优化——区分明确。
- PixSearch (arXiv:2601.19060): 统一区域感知与检索增强推理，但属于 RAG 范式（动态触发检索），产生像素级分割掩码而非 bbox，无层级多粒度嵌入结构。与 GroundVDR 的独立检索范式有根本区别。
- Localization Heads (CVPR 2025 Highlight, arXiv:2503.06287): 仅需 ~3 个注意力头即可在自然图像上实现竞争力定位——为 GroundVDR 的核心假设（VLM patch embedding 含充足空间信息）提供间接证据，但文档图像与自然图像差异显著。
- RegionRAG (AAAI 2026): 学习查询-patch 对齐但依赖手动阈值的 BFS 启发式 patch 分组。GroundVDR 的学习式 localization head 是更原则性的替代。
- ColParse (arXiv:2603.01666): 布局感知子图像检索，95% 存储缩减，但依赖外部解析器无法联合优化。

- 调研总结: 视觉文档检索领域在 2025-2026 年极其活跃，页面级检索已趋成熟（Nemotron ColEmbed V2, MetaEmbed），但**多粒度检索+空间定位的端到端统一**仍是公认的 open problem。现有工作要么是多模型流水线（Multi-Granularity Framework），要么只解决部分问题（AGREE 无 bbox, Hydra 无定位, MURE 无 region proposal）。GroundVDR 精准地占据了这一空白，且与所有现有工作的区分度清晰可辩。

【整体印象】:
作为审稿人，我的第一反应是 **lean accept / weak accept**。这是一份在竞争激烈的热门领域中展现出深度研究功底的 proposal：
1. 问题定义精准，直击领域公认的 open problem（多模型流水线 vs. 端到端统一）；
2. 文献定位极其详尽，对每个竞争工作的差异化分析准确到位；
3. 核心假设（检索-定位协同效应）清晰可测试，有 detection 领域（R-CNN → Faster R-CNN）的成熟类比支撑；
4. 实验设计非常完备，6 个 ablation 精准对应每个设计选择。

主要顾虑在于：(a) 核心假设（VLM patch embedding 对文档 layout 的定位能力）是否成立仍是实验风险；(b) 同时在页面级、区域级、元素级三个粒度都做到竞争力水平的野心很大；(c) 定位目标（0.2 F1）虽然是 SOTA 的 2.2×，但绝对值仍然偏低。

【核心贡献】:
1. **Spatially-Typed Matryoshka Multi-Vector Embeddings**: 在 MetaEmbed 的 token 数量嵌套和 MURE 的分辨率嵌套之外，引入空间-语义粒度作为第三个正交嵌套维度——这是对 Matryoshka 检索范式的实质性概念扩展，且可推广到其他层级空间检索场景。
2. **检索-定位联合训练的协同效应假设**: 将 detection 领域的经典洞见（端到端 joint training 优于分阶段 pipeline）迁移到 VDR 领域，提出可测试的具体假设。
3. **端到端多粒度检索 + 空间定位统一模型**: 将 3-model pipeline 压缩为单一模型，同时新增定位能力——实用价值明确。

这些贡献对领域有**中到高价值**。如果协同假设被实验验证，这将成为该子领域的 foundational 工作；即使协同效应不显著，Spatially-Typed Matryoshka 和端到端统一本身也是有价值的贡献。

【方法合理性】:
方法整体合理，设计选择有据可循：
- 基于 Qwen3-VL-8B + 双向注意力与 SOTA (Nemotron ColEmbed V2) 使用相同 backbone，确保公平比较。
- 自回归 localization head (~150M) 附加在 VLM patch embedding 上——灵感来自 Localization Heads (CVPR 2025) 的发现，但通过可学习参数（6 层 transformer decoder）替代 training-free probing，是合理的升级。
- DocLayNet 预训练 + MMDocIR 联合微调的两阶段训练策略与领域标准实践一致。
- L1 + GIoU 联合损失是目标检测领域的标准选择。

**更简单的替代方案**: 一个关键问题是——能否用 AGREE 风格的注意力代理 + 后处理 bbox 提取达到类似效果，而无需引入 150M 的 localization head？Proposal 通过 ablation #1（用外部解析器或固定网格替换 localization head）部分回答了这个问题，但审稿人可能还会要求一个"注意力热力图 → bbox"的更轻量 baseline。另外，Snappy 已在训练免费条件下达到 59.7% IoU@0.5 on BBox-DocVQA，GroundVDR 需要证明学习式方法的增量收益足以 justify 额外的模型复杂度和训练成本。

【5 维度打分】:
  1. 研究问题: 【强】 — 多粒度 VDR + 空间定位的端到端统一是领域公认的 open problem（Multi-Granularity Framework 论文明确列为 open question），ViDoRe V3 grounding 评估中 model F1=0.089 vs. human F1=0.602 的巨大差距量化了需求。问题定义精准且有实际应用价值（RAG context cropping）。

  2. 方法与创新: 【强-】 — Spatially-Typed Matryoshka 是对 MetaEmbed (ICLR 2026 Oral) 的实质性概念扩展，不是简单的 incremental work。检索-定位协同假设有 R-CNN→Faster R-CNN 的成熟类比支撑。与所有竞争工作的区分度清晰：vs. AGREE（直接 bbox vs. 代理注意力）、vs. Hydra（联合训练 vs. 独立模式）、vs. MURE（输出侧 vs. 输入侧 Matryoshka）、vs. PixSearch（独立检索 vs. RAG 范式）、vs. ReAlign（直接坐标 vs. 文本桥接）。减分项：整体是已有技术的精巧组合（late interaction + localization head + Matryoshka + type tags），每个组件单独看不算全新，创新主要在于组合方式和协同假设。

  3. 实验设计: 【强】 — 这是该 proposal 最突出的维度。4 类 baseline 覆盖页面级、区域级、定位、统一模型；6 个 ablation 精准对应每个设计选择（localization head、Matryoshka nesting、联合损失协同、type tags、layer selection、truncation Pareto curve）。特别赞赏：ablation #3 用 3 seed + paired significance test 直接检验核心协同假设；独立 localization head 评估（DocLayNet COCO mAP）验证核心假设；ViDoRe V3 grounding 标签仅用于 zero-shot 评估（避免数据泄露）；compute-normalized comparison。相比该领域很多只做 nDCG 对比的论文，这套实验设计的严谨度显著高于平均水平。

  4. 可行性: 【中+】 — 计算预算 ~480 H100-hours 对学术实验室可行（小型 GPU 集群 2-3 周）。DocLayNet 和 MMDocIR 均为公开数据集。主要风险：(a) VLM patch embedding 对文档 layout 的定位能力是核心假设但未经验证——Localization Heads (CVPR 2025) 仅在自然图像上验证，文档的高度结构化布局可能更有利也可能引入新挑战；(b) 同时在三个粒度达到竞争力水平需要精心的 loss balancing 和训练策略；(c) 自回归 localization head 的推理延迟可能影响端到端效率优势。但 proposal 对这些风险有清醒认识，并设计了相应的验证实验（独立 localization head 评估、效率 breakdown 报告）。

  5. 写作与呈现: 【强】 — 逻辑链清晰：问题（pipeline 冗余 + 缺少定位）→ 假设（检索-定位协同）→ 方法（统一架构）→ 验证（精准 ablation）。文献定位极其详尽，对 10+ 竞争工作逐一做了差异化分析。技术描述精确（架构细节、训练策略、loss 设计均有具体参数）。唯一小问题：proposal 篇幅较长，实际论文需要大幅压缩，如何在 8 页内呈现如此丰富的内容是一个写作挑战。

【概率估计】: [33% - 47%] 中位 40%

【估计理由】:
上调因素：(1) 占据了领域公认的 open problem（端到端多粒度 + 定位统一），且该 problem 刚被 ViDoRe V3 和 Multi-Granularity Framework 的 2025-2026 论文正式提出/量化，timing 非常好；(2) Spatially-Typed Matryoshka 概念是对 ICLR 2026 Oral 工作的实质扩展，创新度足够；(3) 实验设计的完备度在该领域中属于上乘——6 个 ablation 的设计显示出对方法论的深刻理解；(4) 与竞争工作的区分度非常清晰，positioning 几乎无可挑剔；(5) 计算预算合理，不需要超大规模资源。

下调因素：(1) 核心假设（VLM patch embedding → 文档 layout detection 质量）尚未验证，如果 localization head 在文档上表现不佳，整个方法基础动摇；(2) 同时追求三个粒度的竞争力有过度野心风险——如果页面级 nDCG 不及 Nemotron ColEmbed V2、区域级不及 Multi-Granularity Framework、定位 F1 仅 0.2，审稿人可能认为"什么都做但都不够好"；(3) 方法是多个已有技术的精巧组合，审稿人可能质疑 technical depth；(4) 领域竞争非常激烈，2025-2026 年有大量并发工作，提交时可能面临更多新 SOTA。

综合看，这是一份准备充分、定位精准的 proposal，如果实验结果验证了协同假设（尤其是 ablation #3 显示统计显著的联合训练收益），有较好的中稿机会。40% 中位反映了"方向正确、设计扎实、但实验结果未知且领域竞争激烈"的综合判断。

【主要风险】:
1. **核心假设失败风险**: VLM patch embedding 在文档图像上的 layout detection 质量可能不足以支撑有效的 region proposal——如果 localization head 的 mAP 显著低于 HybriDLA (83.5%)，则下游的区域级检索和定位质量都会受影响，导致联合训练的收益无法体现。
2. **"样样通但样样不精"风险**: 在页面级检索上可能不敌专注页面级的 Nemotron ColEmbed V2，在区域级检索上可能不敌 3-model pipeline，定位 F1 目标 0.2 的绝对值偏低——审稿人可能认为统一模型在每个维度都 compromise 了质量，总体贡献不够有说服力。

【实施评估】:
  - 计算资源: ~480 H100-hours 总计（Phase 1: 30h, Phase 2: 150h, Ablations: 100h, Multi-seed: 200h）。对有小型 GPU 集群的学术实验室可行，约 2-3 周完成。
  - 数据需求: DocLayNet (~80K layout-annotated pages, 公开), MMDocIR (173K bootstrapped + 1,685 expert annotations, 公开), ViDoRe V1/V2/V3 (公开评测集), BBox-DocVQA (公开)。所有数据集均为公开可获取，无数据获取瓶颈。
  - 人工介入: 低。无需人工标注——利用已有公开标注数据集。实验设计和调参需要研究者投入。
  - 训练需求: 两阶段训练——Phase 1 (localization head 预训练) 和 Phase 2 (LoRA backbone + 联合微调)。需要实现自回归 localization head、spatially-typed Matryoshka embedding、联合 loss。工程复杂度中等偏高。
  - 新 Benchmark: 不需要。完全基于已有公开 benchmark (ViDoRe V1/V2/V3, MMDocIR, BBox-DocVQA, DocLayNet)。
  - 预估周期: 实现 + 训练 + 实验 + 论文撰写约 2.5-3.5 个月。其中模型实现 ~3 周，训练 + ablation ~3 周，分析 + 撰写 ~3-4 周。
```

Sources:
- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449)
- [Nemotron ColEmbed V2: Top-Performing Late Interaction Embedding Models](https://arxiv.org/abs/2602.03992)
- [MetaEmbed: Scaling Multimodal Retrieval at Test-Time (ICLR 2026 Oral)](https://arxiv.org/abs/2509.18095)
- [MetaEmbed GitHub - Facebook Research](https://github.com/facebookresearch/MetaEmbed)
- [A Multi-Granularity Retrieval Framework for Visually-Rich Documents](https://arxiv.org/abs/2505.01457)
- [MMDocIR: Benchmarking Multi-Modal Retrieval for Long Documents](https://mmdocrag.github.io/MMDocIR/)
- [MURE: Hierarchical Multi-Resolution Encoding for VDR](https://arxiv.org/abs/2603.13349)
- [Hydra: Unifying Document Retrieval and Generation](https://arxiv.org/abs/2603.28554)
- [AGREE: Attention Grounded Enhancement for Visual Document Retrieval](https://arxiv.org/abs/2511.13415)
- [Snappy: Spatially-Grounded Document Retrieval](https://arxiv.org/abs/2512.02660)
- [ReAlign: Reasoning-Guided Fine-Grained Alignment (SIGIR 2026)](https://arxiv.org/abs/2604.07419)
- [PixSearch: Pixel-Grounded Retrieval](https://arxiv.org/abs/2601.19060)
- [Localization Heads in Vision-Language Models (CVPR 2025 Highlight)](https://arxiv.org/abs/2503.06287)
- [ViDoRe Benchmark V2](https://arxiv.org/pdf/2505.17166)
- [ViDoRe Benchmarks for Visual Retrieval](https://www.emergentmind.com/topics/vidore-benchmarks)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have comprehensive research to make a well-informed assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992) (arXiv 2026): 当前 ViDoRe V3 SOTA，8B 模型 nDCG@10 = 63.42。使用 Qwen3-VL-8B + 双向注意力 + 硬负样本挖掘。GroundVDR 使用相同的 backbone 和双向注意力策略，验证了技术路线的合理性，但也意味着 page-level 性能上限可能被 Nemotron 卡住。
- [MetaEmbed](https://arxiv.org/abs/2509.18095) (ICLR 2026 Oral): 提出 Matryoshka Multi-Vector Retrieval (MMR)，沿 token 数量维度做嵌套。GroundVDR 声称在第三个正交轴（空间-语义粒度）上扩展 Matryoshka 框架，这是一个清晰且有实质性的差异化。
- [Multi-Granularity Framework](https://arxiv.org/html/2505.01457v2) (arXiv 2025): MMDocIR 上达 65.56 nDCG，但需要 ColQwen2 + GME + Qwen2.5-VL + OCR 四个组件。明确将端到端统一作为 open question 留出——这正是 GroundVDR 试图填补的空白。
- [AGREE](https://arxiv.org/abs/2511.13415) (SIGIR 2026): 用 MLLM 注意力作为代理空间监督信号，改善页面级 nDCG 但不产生边界框。GroundVDR 从代理注意力升级到直接框回归，差异明确。
- [Snappy](https://arxiv.org/abs/2512.02660) (arXiv 2025): 推理时无训练的空间定位，ColQwen3-4B 达 IoU@0.5 = 59.7%。作为 training-free lower bound，GroundVDR 的 learned 方案理应显著超越。
- [MURE](https://arxiv.org/abs/2603.13349) (arXiv 2026): 输入侧多分辨率 Matryoshka（RMRL），无学习到的 region proposal 或框预测。GroundVDR 的输出侧空间-语义粒度嵌套是正交且互补的方向。
- [Hydra](https://arxiv.org/abs/2603.28554) (arXiv 2026): LoRA 开关统一检索和生成，两个任务独立模式无共享损失。GroundVDR 的联合训练共享损失设计有实质区别。
- [ReAlign](https://arxiv.org/abs/2604.07419) (SIGIR 2026): 用 VLM 推理生成文本描述作为间接空间监督，通过 KL 散度对齐检索器。GroundVDR 的直接框回归保留精确坐标、可端到端优化，差异清晰。
- [ColParse](https://arxiv.org/abs/2603.01666) (arXiv 2026): 依赖外部 parser 的 layout-informed 子图像检索，95% 存储压缩但无法联合优化。
- [PixSearch](https://arxiv.org/abs/2601.19060) (arXiv 2026): RAG 范式下的 pixel-level 分割 + 检索触发，与 GroundVDR 的离线索引 + 在线查询的独立检索范式不同。
- [Localization Heads](https://arxiv.org/abs/2503.06287) (CVPR 2025 Highlight): 证明 VLM 中 ~3 个注意力头即可实现竞争性定位，但仅在自然图像上验证。GroundVDR 的核心假设之一是该能力可迁移到文档图像——这是一个需要验证的经验性问题。
- [ViDoRe V3](https://arxiv.org/abs/2601.08620) (arXiv 2026): 3,099 条人工标注查询，包含边界框定位评估。最佳模型 F1 仅 0.089 vs 人类 0.602，量化了巨大的 grounding gap。
- [MMDocIR](https://arxiv.org/abs/2501.08828) (EMNLP 2025): 1,685 专家标注 + 173K 引导标注，页面级 + 布局级双任务。GroundVDR 拟用其训练集做联合微调。

- 调研总结: 视觉文档检索领域在 2025-2026 极度活跃，page-level 检索已趋于成熟（Nemotron 63.42 nDCG@10），但 sub-page 多粒度检索仍依赖多模型流水线，空间定位（grounding）几乎是未开发的蓝海（0.089 vs 0.602 F1 gap）。GroundVDR 精准定位了"联合检索+定位的端到端单模型"这一明确空白，是当前竞争格局中尚无直接竞品的位置。

【整体印象】:
作为审稿人，第一反应是**倾向 weak accept / borderline accept**。这是一篇极其精心准备的 proposal：
1. 问题定义清晰且有量化证据支撑（28.5pp 检索 gap，0.089 vs 0.602 grounding F1 gap）
2. 文献综述异常全面，逐一与 10+ 竞品对比并明确差异化
3. 方法设计有清晰的结构性洞察（detection 领域 multi-stage → end-to-end 的类比）
4. 实验方案极其完备，6 个 ablation 直接对应 6 个设计决策
5. 计算预算合理透明

但核心风险在于：(a) synergy hypothesis 可能不成立或效果有限；(b) 文档图像上 localization head 的性能是未验证的核心假设；(c) 方法组合性较强（backbone + localization head + type tags + Matryoshka nesting + joint loss），审稿人可能质疑工程堆叠 vs. 原理性创新。

【核心贡献】:
1. **首个端到端联合检索+空间定位的单一 VDR 模型**：将当前 3-model pipeline 压缩为单模型，同时新增 grounding 能力——这是文献中明确的空白。
2. **Spatially-Typed Matryoshka Multi-Vector Embeddings**：在 MetaEmbed 的 token-count 维度和 MURE 的 input-resolution 维度之外，引入第三个正交嵌套轴（page → region → element 的空间-语义粒度层级）。概念新颖，且有 test-time granularity control 的实用价值。
3. **Retrieval-Grounding Synergy Hypothesis 的系统验证**：通过 ablation #3 直接检验联合训练 vs. 分别训练的增益——这是一个有科学意义的实验。

价值评估：如果 synergy hypothesis 得到验证且性能提升显著，这将是该领域一个重要的方法论贡献。即使 synergy 较弱，单模型统一多粒度检索+定位本身也有工程和应用价值。

【方法合理性】:
方法整体合理，各组件有独立的先行工作支撑：
- Qwen3-VL-8B + 双向注意力 + LoRA：跟随 Nemotron ColEmbed V2 的成功配方
- 自回归 localization head：受 Localization Heads (CVPR 2025) 启发，但从自然图像迁移到文档是未验证的假设
- Late-interaction contrastive loss + box regression loss (L1 + GIoU)：两个损失项各自是标准做法
- Spatially-Typed Matryoshka：是 MetaEmbed MMR 的自然扩展

**潜在的更简单替代方案**：
1. 直接用外部高质量 parser（如 HybriDLA, AAAI 2026, 83.5% mAP）+ 现有 retriever（如 Nemotron/MetaEmbed），以更少工作量构建多粒度检索。但 proposal 正确指出这无法联合优化且有 error cascading。
2. AGREE 式注意力代理监督 + Snappy 式推理时定位。但 proposal 合理论证了学习式定位应优于这些启发式方法。

方法中值得关注的设计风险：
- 自回归 localization head（150M params, 6-layer transformer decoder）在推理时增加延迟——proposal 承诺报告延迟 breakdown，但审稿人可能要求与外部 parser 做延迟对比
- Type tag 路由机制的实际效果可能有限——如果 late interaction 已自然学习到粒度区分，显式 type tag 可能是冗余信号

【5 维度打分】:

1. 研究问题: 【强】
   — 问题有精确量化支撑：ViDoRe V3 grounding gap (0.089 vs 0.602 F1) 和 MMDocIR page-vs-layout gap (28.5pp) 都是已发表 benchmark 上的真实数字。Multi-Granularity Framework 明确将端到端统一留为 open question。这不是人造的问题，而是领域的真实痛点，且影响下游 RAG 系统的 context 质量。

2. 方法与创新: 【中偏强】
   — 与 MetaEmbed (ICLR 2026 Oral) 对比：MetaEmbed 沿 token 数量嵌套，GroundVDR 沿空间-语义粒度嵌套——第三轴扩展概念新颖但本质上是架构组合创新。
   — 与 AGREE (SIGIR 2026) 对比：从代理注意力监督升级到直接框回归——技术路径明确且合理，但"升级"而非"范式变革"。
   — 与 Hydra (arXiv 2026) 对比：从独立模式到联合训练——差异清晰但需要实验验证 synergy 的实际增益幅度。
   — 与 Localization Heads (CVPR 2025) 对比：从自然图像扩展到文档图像——方向合理但迁移假设需验证。
   — 总体：方法是"正确方向上的自然下一步"而非"意料之外的创新"，创新来自组件的新颖组合和新的嵌套轴。对于 AAAI，这在 novelty 门槛之上但不算突出。

3. 实验设计: 【强】
   — Baselines 覆盖 4 大类（page-level/sub-page/grounding/unified），包括所有主要竞品
   — 6 个 ablation 逐一验证 6 个设计决策，ablation #3（synergy hypothesis）设计 3-seed + paired significance test，方法论严谨
   — 独立 localization head 评估（DocLayNet 上 COCO-style mAP）直接验证核心假设
   — 多 benchmark（ViDoRe V1/V2/V3, MMDocIR, BBox-DocVQA）+ 效率指标 + compute-normalized 对比
   — Grounding targets 有量化目标（0.2 F1 minimum, 0.3+ stretch）和 per-modality breakdown
   — 这个实验设计本身是 proposal 的重要加分项，即使方法创新属于"组合式"，完备的实验方案能有效弥补

4. 可行性: 【中偏强】
   — 480 H100-hours 合理，且有清晰的 per-phase 分解（30 + 150 + 100 + 200）
   — 训练数据来源明确：DocLayNet (80K, 公开), MMDocIR (173K, 公开)
   — 风险点：(a) localization head 在文档上可能需要大量调参才能达到满意的 mAP；(b) 联合训练两个异质损失（contrastive + regression）的平衡可能需要大量超参搜索，proposal 未详述损失权重策略；(c) 自回归 localization head 的推理延迟可能影响实际部署，审稿人可能要求延迟分析
   — 2-3 周完成有前提——需要 GPU 集群能持续分配且无排队，实际可能需要 4-6 周

5. 写作与呈现: 【强】
   — 逻辑链条清晰：问题量化 → 假设陈述 → 类比论证（R-CNN → Faster R-CNN）→ 方法设计 → 实验验证
   — 文献定位异常精准，逐一与 10+ 竞品明确差异化，Critical distinction 标注到位
   — 核心假设（VLM patch embeddings 对文档布局的适用性）被明确标注为"需验证的经验性问题"——诚实且专业
   — 方法描述有清晰的 4-step inference pipeline，便于理解
   — 不足：部分细节过度压缩（如 type tag 的具体实现、损失权重策略、多粒度索引的具体数据结构），但对 proposal 阶段已足够

【概率估计】: [30% - 45%] 中位 37%

【估计理由】:
**上行因素（推向 45%）**：
- 研究问题有强量化支撑，领域公认的空白
- 实验设计极其完备，堪称 proposal 级别的标杆
- 写作和定位质量高，审稿人不太会因理解困难而给低分
- 如果 synergy hypothesis 被验证（即使 modest gain），叙事完整度很高
- Grounding 是 VDR 领域的新兴热点，timing 好

**下行因素（推向 30%）**：
- 方法创新属于"组件组合"类型，可能被审稿人视为 engineering contribution
- Synergy hypothesis 可能不成立或增益微弱（<2pp），则论文核心叙事动摇
- 领域竞争极度激烈（MURE, ColParse, AGREE, ReAlign, Hydra 都是同期竞品），AAAI 该方向投稿密度可能很高
- 文档图像 localization head 是未验证的核心假设，失败概率非零
- 系统复杂度高（多个新组件叠加），审稿人可能要求逐一证明每个组件的必要性——6 个 ablation 可以应对但篇幅压力大

**中位 37% 的逻辑**：这是一篇方向正确、准备充分、问题真实的 solid 投稿。它不是那种"一看就会 accept"的突破性工作，但也远不是弱稿。在 AAAI 2026 的竞争强度下，高质量的实验执行和 synergy hypothesis 的验证结果将是决定因素。如果实验结果 deliver（synergy 增益 ≥ 3pp + grounding F1 ≥ 0.25），概率可上移至 40-45%；如果实验结果 underwhelming，概率下移至 28-32%。

【主要风险】:
1. **Synergy hypothesis 验证失败**：如果 ablation #3 显示联合训练与分别训练无显著差异（或差异 <1pp），论文的核心叙事（"retrieval-grounding synergy"）将严重受损。此时论文退化为"一个工程上集成了多功能的系统"，novelty 主要靠 Spatially-Typed Matryoshka 概念支撑，对 AAAI 可能不够。
2. **方法被质疑为 engineering stacking**：backbone + localization head + type tags + Matryoshka + joint loss 的组合可能让审稿人质疑"每增加一个组件带来了多少性能提升？总提升中有多少来自工程优化而非方法论创新？"——虽然 6 个 ablation 设计了应对方案，但如果个别组件贡献微弱，会削弱整体说服力。

【实施评估】:
  - 计算资源: ~480 H100-hours，需要小型 GPU 集群（4-8 块 H100）。对 well-funded 学术实验室可行，对资源有限的团队有压力。Multi-seed 实验（200 H100-hours）是大头，可适当削减。
  - 数据需求: DocLayNet (80K, 公开 COCO 格式) + MMDocIR (173K bootstrapped + 1,685 expert, 公开 HuggingFace) + ViDoRe V3 (3,099 queries, 公开)。所有数据公开可用，无数据瓶颈。
  - 人工介入: 中等。需要大量超参搜索（联合损失权重平衡、localization head 架构调参、Matryoshka 嵌套策略）。Layout 标注使用现有数据集，无需新标注。
  - 训练需求: 两阶段训练（Phase 1 预训练 localization head, Phase 2 联合微调 LoRA + localization head）。需要实现自定义的 autoregressive localization head 和 spatially-typed Matryoshka embedding pooling。工程量较大但无需从零训练 foundation model。
  - 新 Benchmark: 不需要。完全使用现有 benchmark（ViDoRe V1/V2/V3, MMDocIR, BBox-DocVQA, DocLayNet）。
  - 预估周期: 实现 + 调参 + 实验 + 论文写作：约 3-4 个月。其中代码实现 ~3-4 周，实验运行 ~3-4 周（考虑排队和调参），论文撰写 ~2-3 周。
```

---

Sources:
- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992)
- [MetaEmbed (ICLR 2026 Oral)](https://arxiv.org/abs/2509.18095)
- [Multi-Granularity Retrieval Framework](https://arxiv.org/html/2505.01457v2)
- [AGREE (SIGIR 2026)](https://arxiv.org/abs/2511.13415)
- [Snappy](https://arxiv.org/abs/2512.02660)
- [MURE](https://arxiv.org/abs/2603.13349)
- [Hydra](https://arxiv.org/abs/2603.28554)
- [ReAlign (SIGIR 2026)](https://arxiv.org/abs/2604.07419)
- [ColParse](https://arxiv.org/abs/2603.01666)
- [PixSearch](https://arxiv.org/abs/2601.19060)
- [Localization Heads (CVPR 2025 Highlight)](https://arxiv.org/abs/2503.06287)
- [ViDoRe V3](https://arxiv.org/abs/2601.08620)
- [MMDocIR](https://arxiv.org/abs/2501.08828)
- [ColPali (ECIR 2025)](https://arxiv.org/abs/2407.01449)


【原始 proposal（允许参考但不是主要依据）】:
# Learned Spatial Grounding for Multi-Granularity Visual Document Retrieval

## Core Problem

Current visual document retrieval (VDR) models operate at page granularity or require multi-model pipelines with external layout parsers to access element-level content. The SOTA multi-granularity pipeline (Multi-Granularity Framework, arXiv:2505.01457) requires three separate large models (ColQwen2 + GME + Qwen2.5-VL) plus OCR — incurring 3× memory, pipeline latency, and error cascading (OCR errors → layout errors → retrieval errors). No single model jointly learns to retrieve at page, region, and element granularities while producing spatially grounded evidence bounding boxes. The 28.5pp page-vs-layout retrieval gap on MMDocIR (arXiv 2025) and the 0.089 vs. 0.602 model-vs-human grounding F1 on ViDoRe V3 (arXiv 2026) quantify this deficiency.

## Research Hypothesis

**Retrieval-Grounding Synergy**: Joint training of contrastive retrieval and bounding-box regression in a single VLM produces mutually reinforcing learning signals — grounding loss preserves spatial position information in the embedding space, directly benefiting region- and element-level retrieval, while retrieval loss provides semantic discriminability that improves grounding precision. This mirrors the well-established synergy in object detection: the transition from multi-stage pipelines (R-CNN: separate feature extraction → proposal → classification) to end-to-end joint training (Faster R-CNN/YOLO) consistently improved both localization and classification, precisely because the two tasks share spatial-semantic representations. GroundVDR applies the same structural insight to VDR — jointly learning where (grounding) and what (retrieval) through shared spatial-semantic embeddings.

Indirect evidence: AGREE (SIGIR 2026, arXiv:2511.13415) showed that even proxy attention-based spatial signals improve page-level nDCG by 12.82%. GroundVDR elevates this from proxy attention supervision to direct box regression supervision, which should yield stronger spatial encoding and produce actionable bounding boxes.

## Research Landscape

**Page-level VDR.** Nemotron ColEmbed V2 (arXiv 2026) leads ViDoRe V3 at 63.42 nDCG@10 using bidirectional attention and hard negative mining on Qwen3-VL-8B. ColPali (ECIR 2025) established the vision-language late-interaction retrieval paradigm. MetaEmbed (ICLR 2026 Oral, arXiv:2509.18095) introduced Matryoshka Multi-Vector Retrieval (MMR) with learnable Meta Tokens, nesting along the token-count dimension for coarse-to-fine retrieval; 3B achieves 60.3% nDCG@5 on ViDoRe V2.

**Sub-page / region-level retrieval.** The Multi-Granularity Framework (arXiv:2505.01457) achieves 65.56 on MMDocIR but requires three separate large models plus OCR, explicitly leaving end-to-end unification as an open question. RegionRAG (AAAI 2026) learns query-patch alignment but relies on BFS heuristic with manual threshold for patch grouping. ColParse (arXiv 2026, arXiv:2603.01666) achieves 95% storage reduction via layout-informed sub-images but depends on an external parser that cannot be jointly optimized. MURE (arXiv 2026, arXiv:2603.13349) introduces Resolution-level Matryoshka Representation Learning (RMRL), nesting embeddings across input resolutions (multi-resolution sampling). **Critical distinction**: MURE's Matryoshka operates on the input side (resolution hierarchy), while GroundVDR's operates on the output side (spatial-semantic granularity hierarchy: page → region → element). MURE performs no learned region proposals or bounding-box prediction.

**Unified multi-task VDR.** Hydra (arXiv 2026, arXiv:2603.28554) unifies retrieval and generation in a single VLM via LoRA toggle — enabling LoRA yields ColBERT-style embeddings, disabling it recovers generation with byte-identical outputs. However, Hydra's two tasks are independent modes (no shared loss, no mutual reinforcement), whereas GroundVDR's retrieval and grounding are jointly trained with a shared loss, hypothesizing explicit synergy.

**Spatial grounding in retrieval.** AGREE (SIGIR 2026, arXiv:2511.13415) uses MLLM attention as proxy supervision, improving page-level nDCG but producing no bounding boxes. Snappy (arXiv 2025, arXiv:2512.02660) achieves 59.7% IoU@0.5 on BBox-DocVQA purely at inference time with no learned optimization. ReAlign (SIGIR 2026, arXiv:2604.07419) uses VLM reasoning to identify query-relevant regions, then generates textual descriptions as supervision to align retriever rankings via KL divergence — a text-bridged indirect spatial supervision approach. GroundVDR differs fundamentally: direct box regression preserves precise spatial coordinates (vs. ReAlign's lossy text compression), is end-to-end optimizable (vs. ReAlign's frozen VLM teacher), and produces bounding boxes directly usable for downstream RAG context cropping. PixSearch (arXiv 2026, arXiv:2601.19060) combines retrieval with region-level grounding but differs in three ways: (1) retrieval is generation-time dynamic triggering (retrieval-augmented generation paradigm) vs. GroundVDR's offline indexing + online query (standalone retrieval paradigm); (2) grounding produces pixel-level segmentation masks vs. bounding boxes (less natural for rectangular document layouts); (3) no hierarchical multi-granularity embedding structure with test-time granularity control. On ViDoRe V3's grounding evaluation, the best model achieves only 0.089 F1 vs. 0.602 human F1. Localization Heads (CVPR 2025 Highlight, arXiv:2503.06287) show that ~3 attention heads in VLMs suffice for competitive grounding on natural images without fine-tuning.

**Key gap.** No existing work jointly learns retrieval and spatial grounding with direct bounding-box supervision in a single end-to-end model. The detection and retrieval communities have independently developed the necessary components but never unified them.

## Proposed Approach

We propose **GroundVDR**, a single vision-language model that jointly performs multi-granularity document retrieval and spatial grounding end-to-end, compressing the current 3-model pipeline into one model while adding grounding capabilities that no existing single model provides.

**Architecture.** Built on Qwen3-VL-8B with bidirectional attention (LoRA r=64 on backbone). An autoregressive localization head (6-layer transformer decoder, ~150M parameters, fully trained) is attached to VLM patch embeddings to predict region bounding boxes as coordinate token sequences, replacing external parsers.

**Core assumption (to be validated):** VLM patch embeddings contain sufficient spatial and semantic information for high-quality document region proposals. While Localization Heads (CVPR 2025) demonstrated this for natural images, document layouts differ structurally. We hypothesize that documents' highly structured, grid-like layouts are actually more amenable to patch-level spatial reasoning than cluttered natural scenes — but this is an empirical question central to the paper, addressed by independent evaluation of the localization head on DocLayNet.

**Spatially-Typed Matryoshka Multi-Vector Embeddings.** MetaEmbed nests along the token-count dimension; MURE nests along the input-resolution dimension. GroundVDR introduces a third, orthogonal nesting axis: **spatial-semantic granularity**. Each embedding vector carries a learned type tag encoding its position in the document's spatial hierarchy (page / region-type / element-type). During late interaction, type tags enable heterogeneous matching — a region-level query preferentially interacts with region-typed embeddings, while a page-level query aggregates across all types. This extends the Matryoshka framework from a precision-efficiency tradeoff to a spatial-semantic granularity tradeoff with test-time control. The extension is not limited to VDR — any retrieval scenario with hierarchical spatial structure (e.g., map retrieval, medical imaging) could benefit, though this paper focuses on document retrieval.

**Inference Pipeline (4 steps):**
1. Document page → backbone bidirectional encoding → patch embeddings
2. Patch embeddings → localization head (autoregressive decoding) → region bounding boxes
3. Region boxes → crop & pool patch embeddings → region-level and element-level spatially-typed Matryoshka embeddings; page-level embedding aggregated from all patches
4. Multi-granularity index: page/region/element embeddings indexed separately; query-time granularity selection via type-tag routing

**Joint Loss.** Late-interaction contrastive retrieval loss + bounding-box regression loss (L1 + GIoU), with gradient flowing from both losses through the shared backbone. The synergy hypothesis predicts that joint training outperforms separate training of either task — tested directly in ablation #3.

**Training Data Strategy.**
- Phase 1: Localization head pre-training on DocLayNet (KDD 2022, ~80K layout-annotated pages, 11 classes, COCO format) for general document layout detection (~30 H100-hours).
- Phase 2: Joint fine-tuning on MMDocIR's 173K bootstrapped layout annotations + 1,685 expert annotations for retrieval + grounding alignment (~150 H100-hours). Grounding-capable layers selected using Localization Heads' probing protocol.
- Grounding evaluation: ViDoRe V3's 3,099 human-verified queries used exclusively for zero-shot evaluation (no training on ViDoRe V3 grounding labels to prevent data leakage).

## Experimental Design

**Baselines (4 categories):**
- Page-level retrieval: Nemotron ColEmbed V2 (8B), MetaEmbed (3B/7B), ColPali/ColQwen2, BM25+OCR
- Sub-page/region-level retrieval: MURE, ColParse, RegionRAG, Multi-Granularity Framework (pipeline upper bound)
- Grounding: Snappy (training-free lower bound, reproduced on ViDoRe V3), AGREE (attention-proxy baseline)
- Unified single-model: Hydra (retrieval+generation, no grounding → grounding column marked N/A)

**Benchmarks and Metrics:**
- ViDoRe V1/V2/V3: nDCG@{5,10} for retrieval; IoU@{0.25, 0.5, 0.7}, mean IoU, Dice/F1 for grounding (V3 only)
- MMDocIR: page-level nDCG@{5,10} and layout-level nDCG@{5,10} reported separately
- BBox-DocVQA: IoU@{0.25, 0.5, 0.7} for grounding (supplementary, aligns with Snappy's primary benchmark)
- Efficiency: storage cost (embeddings per page × dimension, bytes per page), per-page encoding latency (ms) with breakdown (backbone / localization head / pooling+indexing), training cost (GPU-hours per phase)
- Compute-normalized comparison: training FLOPs (or GPU-hours) vs. performance for all methods

**Grounding targets:** 0.2 F1 as minimum viable (2.2× current SOTA 0.089), 0.3+ F1 as stretch target. Per-modality breakdown (text 60.4% / image 18.8% / table 16.7%) to analyze where grounding gains concentrate.

**Ablation Studies (6 experiments):**
1. Replace learned localization head with external parser (HybriDLA) or fixed grid → quantify learned vs. external proposals on retrieval quality
2. Remove Matryoshka nesting → flat multi-vector → quantify hierarchical nesting contribution per granularity level
3. Remove joint loss → train retrieval-only and grounding-only variants separately → **directly test the synergy hypothesis** (3 seeds, paired significance test)
4. Remove spatial type tags → uniform embedding type → quantify type-aware heterogeneous interaction value
5. Layer selection: vary which backbone layers feed the localization head → validate probing protocol for document images
6. Matryoshka truncation tradeoff: performance at page-only / page+region / page+region+element embedding levels → Pareto curve (storage vs. nDCG), compared against MetaEmbed group-size tradeoff and MURE resolution tradeoff

**Independent Localization Head Evaluation:** Report COCO-style mAP@{0.5, 0.5:0.95, 0.75} on DocLayNet test set, compared against HybriDLA (83.5% mAP, AAAI 2026) and other layout detection baselines. This directly validates the core assumption about VLM patch embeddings for document layout analysis.

**Compute Budget:**
- Phase 1 (localization head pre-training, DocLayNet 80K): ~30 H100-hours
- Phase 2 (backbone LoRA + joint fine-tuning, MMDocIR 173K): ~150 H100-hours
- Ablation experiments (6 ablations, ~30-50% of main training each): ~100 H100-hours
- Multi-seed: 2 seeds for main results, 3 seeds for ablation #3 → additional ~200 H100-hours
- **Total: ~480 H100-hours**, reproducible by academic labs with a small GPU cluster over 2-3 weeks

## Key References

- Nemotron ColEmbed V2 (arXiv 2026)
- ColPali: Efficient Document Retrieval with Vision Language Models (ECIR 2025)
- MMDocIR: Multi-Modal Document Information Retrieval (arXiv 2025)
- ViDoRe V3: Visual Document Retrieval Benchmark with Grounding (arXiv 2026)
- MetaEmbed: Matryoshka Multi-Vector Retrieval (ICLR 2026 Oral, arXiv:2509.18095)
- HybriDLA: Hybrid Diffusion-Autoregressive Document Layout Analysis (AAAI 2026)
- RegionRAG: Region-Level RAG for Visual Document Understanding (AAAI 2026)
- AGREE: Attention-Grounded Retriever Enhancement (SIGIR 2026, arXiv:2511.13415)
- Snappy: Spatially-Grounded Document Retrieval (arXiv 2025, arXiv:2512.02660)
- Localization Heads in Vision-Language Models (CVPR 2025 Highlight, arXiv:2503.06287)
- MURE: Hierarchical Multi-Resolution Encoding for VDR (arXiv 2026, arXiv:2603.13349)
- Hydra: Unifying Document Retrieval and Generation (arXiv 2026, arXiv:2603.28554)
- ColParse: Layout-Informed Sub-Image Retrieval (arXiv 2026, arXiv:2603.01666)
- Multi-Granularity Retrieval Framework (arXiv 2025, arXiv:2505.01457)
- PixSearch: Pixel-Grounded Retrieval (arXiv 2026, arXiv:2601.19060)
- ReAlign: Reasoning-Guided Fine-Grained Alignment (SIGIR 2026, arXiv:2604.07419)
- DocLayNet: Document Layout Analysis Dataset (KDD 2022)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a83bfb82-a3d0-4b55-be5f-a59104964e8a",
  "type": "user",
  "uuid": "20267659-fbf9-441f-9573-4257ea97d260",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:30:36.214Z_

```json
{
  "parentUuid": "20267659-fbf9-441f-9573-4257ea97d260",
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
  "uuid": "8dfb4641-778a-4d10-8c05-c3e7c554cbbd",
  "timestamp": "2026-05-30T07:30:36.214Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:30:36.214Z_

```json
{
  "parentUuid": "8dfb4641-778a-4d10-8c05-c3e7c554cbbd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8d8e5eba-dcf6-4cfd-9251-1c30f66e6f69",
  "timestamp": "2026-05-30T07:30:36.214Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Based on my research, I now have enough context to provide a c…",
  "leafUuid": "8d8e5eba-dcf6-4cfd-9251-1c30f66e6f69",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "End-to-end multi-granularity document retrieval with spatial grounding",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429"
}
```

---

### Assistant

_source line 8 · 2026-05-30T07:31:04.398Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Probability: [28% - 42%] 中位 35%
- Research Problem: 强
- Method & Innovation: 中偏强
- Experimental Design: 强
- Feasibility: 中偏强
- Writing: 强
- Overall impression: weak accept

**Reviewer 2:**
- Probability: [33% - 47%] 中位 40%
- Research Problem: 强


- Method & Innovation: 强-
- Experimental Design: 强
- Feasibility: 中+
- Writing: 强
- Overall impression: lean accept / weak accept

**Reviewer 3:**
- Probability: [30% - 45%] 中位 37%
- Research Problem: 强
- Method & Innovation: 中偏强
- Experimental Design: 强
- Feasibility: 中偏强
- Writing: 强
- Overall impression: weak accept / borderline accept

Now I'm looking at the three median probabilities—35%, 40%, and 37%—which average to 37.3% with a median of 37%. The standard deviation is relatively small, suggesting the reviewers are fairly aligned in their assessment.

Looking at where the reviewers agree, the research problem, experimental design, and writing quality all received strong ratings across the board. The method and innovation dimension shows some variation, with two reviewers rating it as moderately strong while one rated it slightly lower.

The critical consensus risks that emerged from all three reviewers are the potential failure of the synergy hypothesis, concerns about whether the engineering combination constitutes genuine novelty, the unverified assumption about using VLM patch embeddings for document layout detection, and the intensity of the competitive landscape. System complexity also appears as a concern, explicitly flagged by two reviewers and implicitly by the third.

R2 stands out as having a slightly different perspective compared to the other two reviewers.

Looking at the probability ranges across all three reviewers, the standard deviation is quite tight at about 2.05%, which indicates strong agreement. Given this high consistency, I can confidently narrow the estimate around the median of these overlapping ranges rather than maintaining a wide interval.

The most generous reviewer (R2) sets an upper bound at 47% with a median of 40%, so my final estimate shouldn't exceed those values. Balancing the three ranges and applying the principle that the combined estimate shouldn't be more generous than any individual reviewer, I'm settling on a median of 37% with bounds around 30-31% on the lower end and 43-44% on the upper end.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d8e5eba-dcf6-4cfd-9251-1c30f66e6f69",
  "isSidechain": false,
  "requestId": "req_011CbYMwYifgaKg5Len4A3VY",
  "type": "assistant",
  "uuid": "7dd65e39-0ff9-4556-810e-342b614a4a58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEy11NccMKcHwYihJsr7Nw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20971,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3756,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20971
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

_source line 9 · 2026-05-30T07:32:05.589Z_

【阶段】: Meta Judge
【三次中位】: [35%, 40%, 37%]  std=2.1%
【共识维度】:
- 研究问题: 强（3/3 一致）— ViDoRe V3 grounding gap (0.089 vs 0.602 F1) 和 Multi-Granularity Framework 明确留出的 open question 提供强有力的问题动机，领域公认空白
- 实验设计: 强（3/3 一致）— 6 个 ablation 逐一对应设计决策、ablation #3 用 3-seed paired significance test 验证核心假说、4 类 baseline 覆盖全部竞争方向、compute-normalized comparison，三位审稿人均认为这是 proposal 最突出的加分项
- 写作与呈现: 强（3/3 一致）— 逻辑链清晰，文献定位精准详尽，与 10+ 竞品逐一差异化分析到位
- 方法与创新: 中偏强（3/3 实质一致，R1/R3 标 "中偏强"，R2 标 "强-"，语义等价）— Spatially-Typed Matryoshka 是对 MetaEmbed 的实质概念扩展，与所有竞品差异化清晰；但整体属于已有技术的精巧组合，创新主要在组合方式和 synergy 假说
- 可行性: 中偏强（3/3 实质一致，R1/R3 标 "中偏强"，R2 标 "中+"）— 480 H100-hours 合理可行，公开数据集无瓶颈；但联合训练调参复杂度、localization head 在文档图像上的表现为未验证风险
- **核心风险共识（3/3 均提及）**:
  - Synergy hypothesis 不成立或增益微弱 → 论文退化为工程集成
  - 方法被质疑为 "engineering stacking" / "known components 的新组合"
  - VLM patch embedding 对文档 layout 的定位能力为未验证核心假设
  - 领域竞争极其激烈，同期大量并发工作
【异常维度】:
- R1 明确要求添加 Snappy-style training-free baseline 到 ablation 中（R2/R3 提及 Snappy 但未强烈要求加入 ablation）— 合理但非关键遗漏，现有 ablation #1 部分覆盖
- R2 对 fallback 价值评估更乐观（"即使 synergy 不显著，Spatially-Typed Matryoshka 和端到端统一本身也有价值"）— 属于 R2 偏乐观的判断倾向，但有一定道理
- R2 提到 "注意力热力图 → bbox 的更轻量 baseline" 需求 — 合理的审稿人潜在质疑，但非 proposal 级别的致命遗漏
【最终概率】: [30% - 43%] 中位 37%
【一致性】: 高（std=2.1% < 3%）
【综合理由】:

三位审稿人在所有 5 个 rubric 维度上达成高度一致，概率估计 std 仅 2.1%，属于罕见的高收敛。核心判断完全对齐：**研究问题定义精准、实验设计完备是最大优势；方法创新属于组合型而非范式突破是主要天花板**。

取中位 37% 而非简单平均 37.3% 的逻辑：
1. R2（40%）是三份中最宽松的，其乐观源于对 Spatially-Typed Matryoshka 概念价值的更高评估（标 "强-"）。但 R1 和 R3 均标 "中偏强"，2:1 的共识应当优先，因此不上调至 R2 水平。
2. R1（35%）的下行判断中 "系统复杂度高意味着实验结果可能不如预期 clean" 和 "领域竞争激烈，投稿时可能有更新 SOTA" 是合理的保守考量，但 R2/R3 未将其作为显著下行因素，说明 R1 可能略微过度惩罚。
3. 37% 恰好在三位中位的几何中心，且略偏向 R1/R3 更保守的判断（遵循 "宁缺毋滥" 原则）。

上界定为 43%（低于 R2 的 47%）：即使实验结果全部 deliver（synergy ≥ 3pp、grounding F1 ≥ 0.25），方法创新的组合性质仍然限制上限，三位审稿人对此判断一致。下界定为 30%（取 R1 的 28% 和 R2 的 33% 之间的保守值）：如果 synergy 假说不成立，论文仍有 Spatially-Typed Matryoshka 概念和端到端统一的工程价值支撑，不至于跌破 30%。

**关键判断**：这是一篇方向正确、准备极其充分、问题真实且量化清晰的 solid 投稿。概率天花板被方法创新的 "组合性" 本质锁定——Synergy hypothesis 的验证结果是决定最终命运的关键变量。如果 synergy 增益显著（≥3pp），概率上移至 40-43%；如果不显著（<1pp），概率下移至 30-33%。

【建议】: 边缘（中位 37% 在 AAAI 接收率 ~20-23% 的竞争环境下属于 above-average 投稿，但需要实验结果 deliver 才能跨过 acceptance threshold。建议进入迭代优化，主攻 idea 层面的 novelty 锐化和实验层面的风险缓解。）

【实施评估】:
  - 计算资源: ~480 H100-hours 总计（Phase 1: 30h localization head 预训练, Phase 2: 150h 联合微调, Ablations: 100h, Multi-seed: 200h）。4-8 块 H100 集群可在 2-3 周完成训练部分。对 well-funded 学术实验室完全可行，资源受限团队有一定压力但非不可达。三位审稿人对此判断一致。
  - 数据需求: DocLayNet (~80K layout-annotated pages, 公开 COCO 格式) + MMDocIR (173K bootstrapped + 1,685 expert annotations, 公开 HuggingFace) + ViDoRe V1/V2/V3 (公开评测集) + BBox-DocVQA (公开)。全部公开可获取，无数据壁垒。三位审稿人完全一致。
  - 人工介入: 低到中等。无需新增人工标注（全部使用现有公开数据集），但联合损失权重平衡、localization head 架构调参、Matryoshka 嵌套策略等需要研究者投入较多超参搜索时间。R3 特别指出 "loss 权重策略未详述"，需在实施时重点关注。
  - 训练需求: 两阶段训练。Phase 1 在 DocLayNet 预训练 localization head（~30 H100-hours）；Phase 2 在 MMDocIR 联合微调 LoRA backbone + localization head（~150 H100-hours）。需要实现自定义组件：自回归 localization head（6 层 transformer decoder, ~150M 参数）、spatially-typed Matryoshka embedding pooling、联合 loss 梯度连接。工程复杂度中等偏高，但不需要从零预训练 foundation model。
  - 新 Benchmark: 不需要。完全基于现有公开 benchmark（ViDoRe V1/V2/V3, MMDocIR, BBox-DocVQA, DocLayNet），这是显著的可行性优势。
  - 预估周期: 综合三位审稿人评估，约 3-4 个月从启动到可投稿。其中代码实现 ~3-4 周（含自回归 localization head、spatially-typed Matryoshka、联合 loss 等核心模块），训练 + 调参 + ablation ~3-4 周（考虑 GPU 排队和超参搜索），分析 + 论文撰写 ~2-3 周。如果联合训练梯度平衡困难（R1 特别提醒此风险），可能延长至 4-5 个月。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dd65e39-0ff9-4556-810e-342b614a4a58",
  "isSidechain": false,
  "requestId": "req_011CbYMwYifgaKg5Len4A3VY",
  "type": "assistant",
  "uuid": "bed3b01a-e419-4f4e-998e-c224d9c462a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEy11NccMKcHwYihJsr7Nw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20971,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3756,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20971
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Based on my research, I now have enough context to provide a c…",
  "leafUuid": "bed3b01a-e419-4f4e-998e-c224d9c462a3",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "End-to-end multi-granularity document retrieval with spatial grounding",
  "sessionId": "f40b30a0-1c09-4565-9038-2bbcf4fca429"
}
```

---
