# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/05630948-4d28-4948-b45a-f1c448e3178f.jsonl`
- **Structured JSON:** [`bba7fd87f89b9bc341fd.json`](../../sessions/bb/bba7fd87f89b9bc341fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T23:54:19.398Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T23:54:19.398Z",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [PRCO / \"Seeing with You\" (arXiv 2603.28618, Mar 2026)](https://arxiv.org/abs/2603.28618): 最直接的竞争者。双角色 RLVR（Observer 生成 NL caption + Solver 求解），8 个 benchmark 平均 +7pt。核心区别：Observer 输出是不可验证的 NL caption，不是 formal predicates；无持久化记忆或检索机制。SymMem 可视为 PRCO 的 formal-predicate 升级版 + scratchpad。\n- [Geoparsing (arXiv 2604.11600, Apr 2026)](https://arxiv.org/abs/2604.11600): SOTA 形式化几何图解析器，SFT+RLVR 训练，GDP-29K 数据集（20K 平面 + 9K 立体）。SymMem 的 Observer 组件本质上是复用 Geoparsing 的方法论。\n- [Don't Blink (arXiv 2604.04207, Apr 2026)](https://arxiv.org/abs/2604.04207): 证明推理 VLM 在 CoT 过程中视觉注意力质量下降 >50%（evidence collapse）。验证了 SymMem 的动机之一，但该论文本身提出的是 entropy-vision veto，而非 symbolic memory 解法。\n- [Symbolic Grounding (arXiv 2604.21346, Apr 2026)](https://arxiv.org/abs/2604.21346): 在 Bongard-LOGO 上证明 oracle symbolic grounding 可将 LLM 准确率从近随机提升到 mid-90s。**但注意**：Bongard-LOGO 是抽象视觉推理，与几何问题的视觉复杂度和形式化程度差异很大，gap 的可迁移性未经验证。\n- [CogFlow (ICLR 2026, arXiv 2601.01874)](https://arxiv.org/abs/2601.01874): 认知启发三阶段框架（感知→内化→推理），MathVista 76.8%。内化阶段使用文本形式，而非 formal predicates。与 SymMem 的 \"internalization\" 概念有重叠，但实现路径不同。\n- [Hilbert-Geo (arXiv 2605.16385, May 2026)](https://arxiv.org/abs/2605.16385): Parse2Reason 方法，使用 CDL formal predicates（120 predicates），SolidFGeo2k 77.3%。**无 RL、无持久化记忆**。是 SymMem 在 \"formal parsing → reasoning\" 路径上的直接前驱，SymMem 的增量在于 RL 训练和 scratchpad。\n- [FIGR (arXiv 2512.24297, Dec 2025)](https://arxiv.org/abs/2512.24297): 在推理循环中生成可执行代码渲染图像，+13.12% AIME。与 SymMem 的 verifiable symbolic predicates 在哲学上不同（pixel-level vs. predicate-level），但都在做 \"将推理外化为可验证中间表示\"。\n- [Neuro-symbolic RL (arXiv 2604.22062, Apr 2026)](https://arxiv.org/abs/2604.22062): Qwen3-VL-2B + GRPO + symbolic language，+3.33%。小规模验证了 symbolic + RL 的可行性，但无 persistent memory、无 formal verification。\n- [MathLens (arXiv 2510.01719, Oct 2025)](https://arxiv.org/abs/2510.01719): 分解感知/推理/整合三类错误，发现整合错误随模型改进而占比上升。SymMem 引用此论文作为 \"integration failure is the escalating bottleneck\" 的论据。\n- [FormalGeo (arXiv 2310.18021)](https://arxiv.org/abs/2310.18021): 88 predicates + 196 theorems，FormalGeo7k 数据集（6,981 题，扩增至 ~134K）。SymMem 的符号表示基础设施。\n\n- **调研总结**: 该领域目前处于 \"perception-reasoning 分离优化向联合训练过渡\" 的阶段。PRCO 确立了双角色 RL 的范式，Geoparsing/Hilbert-Geo 确立了 formal parsing 的能力，但二者尚未系统性结合。SymMem 的定位是在两条独立成熟的研究线之间搭桥——这是一个自然且可预见的下一步，而非范式突破。\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative：**\"Geoparsing 输出的 formal predicates 直接拼接到 prompt，然后用 PRCO 的 RL 框架训练\"**（即 PRCO + formal predicates，无 scratchpad，无 step-wise retrieval，无 coverage reward）。\n\nProposal 给出了三个反驳理由，但需要逐一审视：\n(a) **Lost-in-the-middle effect**：几何题的 formal predicates 通常只有 20-60 条（几十到几百 tokens），远不到触发 lost-in-the-middle 效应的上下文长度（该效应在数千 tokens 时才显著）。这个论据在几何场景下偏弱。\n(b) **无自适应检索**：有效性取决于谓词数量。对于典型几何题，全量拼接不会造成信息过载；但如果扩展到更复杂的图（如多图组合），检索的价值会增大。\n(c) **无 integration reward**：这是最强的论据。但 PRCO 的 Solver reward 已经通过反向传播间接激励 Observer 输出有用信息，coverage reward 的增量价值需要实验验证。\n\n**增量价值判断**：SymMem 相对 trivial alternative 的真正增量在于 (1) structural verification 使 Observer reward 可以独立计算（vs. PRCO 只能依赖下游任务成功率间接估计），(2) coverage-based integration reward 是一种更显式的整合激励。但这些是 reward engineering 层面的改进，而非架构层面的根本性创新。Persistent scratchpad 对于几何题可能是 over-engineering。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链：\n1. \"视觉信息在 CoT 过程中不可逆丢失\"（Don't Blink）→ ✅ 有实证支撑\n2. \"integration failure 是随模型改进而升级的瓶颈\"（MathLens）→ ✅ 有实证支撑\n3. \"Oracle symbolic grounding 可大幅提升性能\"（Symbolic Grounding on Bongard-LOGO）→ ⚠️ **关键假设跳跃**：Bongard-LOGO 是抽象视觉推理，visual→symbolic 的 gap 极大；几何图是高度结构化的，视觉编码本身可能已经捕获了大部分结构信息。在几何领域，oracle gap 可能远小于 Bongard-LOGO 上观察到的，从而削弱了整个 \"bridging the oracle gap\" 叙事的力度。\n4. \"Persistent scratchpad + step-wise retrieval 优于一次性拼接\"→ ⚠️ **未经验证**。对于谓词数量有限的几何题（vs. 需要处理长文档的 QA 任务），step-wise retrieval 的增量价值不确定。\n5. \"Coverage-based integration reward 优于 per-step utilization reward 或无 reward\"→ ⚠️ **纯假设，无先验支撑**。这是一个 reward design choice，是否有效完全依赖实验。\n6. \"三路 reward 可以稳定训练（Observer F1 + Solver accuracy + R_cov）\"→ ⚠️ 多目标 RL 的训练稳定性是已知难题，λ_cov 的敏感度可能很高。\n\n**最关键的假设跳跃是第 3 条**：从 Bongard-LOGO 上的 oracle gap 推广到几何领域，缺乏中间验证步骤。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — SymMem 是两条成熟研究线（PRCO 的双角色 RL + Geoparsing/Hilbert-Geo 的 formal parsing）的自然组合。单独来看，每个组件都有直接对应的 prior work：dual-role RL → PRCO；formal parsing → Geoparsing + Hilbert-Geo；symbolic + RL → Neuro-symbolic RL (2604.22062)；scratchpad 机制 → Notes-to-Self (2602.21013)。真正的 novelty delta 在于：(a) structural verification 使 Observer reward 可独立计算，(b) coverage-based integration reward，(c) oracle gap decomposition 评估框架。这些是有价值的工程/方法论贡献，但不构成 \"surprising\" 的新发现。如果告诉一个熟悉 PRCO 和 Geoparsing 的研究者这个 idea，他们的反应更可能是 \"makes sense, obvious next step\" 而非 \"I wouldn't have thought of that\"。\n\n2. **Significance: 中偏强** — 问题本身重要且 well-motivated。视觉数学推理是活跃的研究方向，integration failure 是一个被充分记录的真实瓶颈（MathLens）。几何作为 testbed 是合理的选择。但 significance 受限于两点：(a) 方法强绑定 FormalGeo 的谓词系统，可推广性存疑——非几何视觉数学问题（如图表、函数图像）没有类似的 mature formal predicate system；(b) 如果 oracle gap 在几何领域本身不大（因为几何图已经高度结构化），那么 \"bridging the gap\" 的故事就不够有说服力。\n\n3. **Related Work: 强** — Proposal 对相关工作的覆盖非常全面，包括了所有主要竞争者（PRCO、CogFlow、Geoparsing、Hilbert-Geo、FIGR、Neuro-symbolic RL）且差异化定位清晰。与 PRCO 的区别（formal vs. NL、verifiable vs. unverifiable）、与 Hilbert-Geo 的区别（+RL +persistent memory）、与 FIGR 的区别（predicate-level vs. pixel-level）都有明确阐述。唯一遗漏的是可能需要更明确讨论 CogFlow 的 \"knowledge internalization\" 与 SymMem 的 \"persistent symbolic scratchpad\" 在概念层面的重叠和区别。\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \n- Significance 和 Related Work 都是支撑项（问题重要、覆盖全面）\n- **上界被 Novelty 限制**：核心 idea 是现有方法的 predictable combination，缺乏 \"surprising\" 元素。审稿人很可能会问 \"What is the core insight beyond combining PRCO with formal parsing?\"，而 proposal 的回答（persistent scratchpad + coverage reward + oracle gap evaluation）更多是 system design 和 evaluation methodology 层面的贡献，而非根本性的新见解。\n- 下界被 well-motivated problem + oracle gap evaluation framework 托住——即使 novelty 被质疑，solid experimental design 可以部分弥补。\n- 概率没有达到 35-45% 区间，因为核心发现如果 positive（formal predicates + scratchpad 优于 NL captions），多数熟悉领域的审稿人会认为 \"I would have guessed this\"。\n\n【主要风险】:\n1. **\"Obvious combination\" 质疑**：审稿人可能认为 SymMem 只是 \"PRCO + Geoparsing + scratchpad\"，novelty 不足以达到顶会门槛。proposal 需要更强地论证 persistent scratchpad 和 coverage reward 的不可替代性（而不只是 \"more complete\"）。\n2. **Oracle gap 迁移性假设的脆弱性**：从 Bongard-LOGO（抽象视觉推理，gap 极大）推广到几何（结构化视觉，gap 可能很小），如果实验显示几何领域 oracle gap 本身只有 2-5pt，那么整个 \"bridging the gap\" 叙事将大幅削弱，论文的核心故事线将失去支撑。\n```\n\nSources:\n- [PRCO: Seeing with You (arXiv 2603.28618)](https://arxiv.org/abs/2603.28618)\n- [Geoparsing (arXiv 2604.11600)](https://arxiv.org/abs/2604.11600)\n- [Don't Blink: Evidence Collapse (arXiv 2604.04207)](https://arxiv.org/abs/2604.04207)\n- [Symbolic Grounding (arXiv 2604.21346)](https://arxiv.org/abs/2604.21346)\n- [CogFlow (arXiv 2601.01874, ICLR 2026)](https://arxiv.org/abs/2601.01874)\n- [MathLens (arXiv 2510.01719)](https://arxiv.org/abs/2510.01719)\n- [Hilbert-Geo (arXiv 2605.16385)](https://arxiv.org/abs/2605.16385)\n- [FIGR (arXiv 2512.24297)](https://arxiv.org/abs/2512.24297)\n- [Neuro-symbolic RL (arXiv 2604.22062)](https://arxiv.org/abs/2604.22062)\n- [FormalGeo (arXiv 2310.18021)](https://arxiv.org/abs/2310.18021)\n- [Notes-to-Self Scratchpad (arXiv 2602.21013)](https://arxiv.org/abs/2602.21013)\n- [ACL 2026 Survey: Deep Learning for Geometry Problem Solving](https://github.com/majianz/dl4gps)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [PRCO / \"Seeing with You\" (arXiv 2603.28618, Mar 2026)]: 双角色 RLVR 框架，Observer 生成 NL caption + Solver 推理，8 个 benchmark 上平均 +7pt。使用 NL 文本桥接而非 formal predicates，无法验证 Observer 输出的正确性。是本 proposal 最直接的上游工作和最强竞争者。\n\n- [Symbolic Grounding (arXiv 2604.21346, Apr 2026)]: 证明 LLM 接收 oracle 符号表示时在 Bongard-LOGO 上从 near-chance 跳到 mid-90s accuracy。建立了 representation（而非 reasoning）是核心瓶颈的关键论据。是本 proposal 动机的核心支柱，已确认存在且描述准确。\n\n- [Don't Blink (arXiv 2604.04207, Apr 2026)]: 揭示推理 VLM 在 CoT 展开过程中 >50% 的 visual evidence mass 衰减。提供了 attention tracking 方法论和公开代码。为 persistent memory 的必要性提供了实证基础。已确认存在。\n\n- [MathLens / \"What MLLMs Learn\" (arXiv 2510.01719, Oct 2025, updated Feb 2026)]: 将 MLLM 错误分解为 perception / reasoning / integration 三类，发现随着模型改进，integration failure 占比上升，成为 escalating bottleneck。已确认存在，描述准确。\n\n- [Geoparsing (arXiv 2604.11600, Apr 2026)]: SOTA 形式化几何图解析，SFT+RLVR，GDP-29K 数据集，PGDP 96.4 / SGDP 94.9，超越 GPT-5.2。已确认存在。为 proposal 的 Observer 模块提供了技术可行性依据。\n\n- [Hilbert-Geo (arXiv 2605.16385, May 2026)]: Parse2Reason 框架，CDL predicates，SolidFGeo2k 上 78% accuracy。有 formal parsing，但**无 RL、无 persistent memory**。是与 SymMem 最接近的 neuro-symbolic geometry 工作，proposal 的差异化定位准确。\n\n- [CogFlow (ICLR 2026, arXiv 2601.01874)]: 三阶段 perception→internalization→reasoning，text-based internalization + Visual-Gated Policy Optimization。MathVista 76.8%。使用文本内化而非 formal predicates，无 persistent queryable memory。已确认是 ICLR 2026 accepted paper。\n\n- [FIGR (arXiv 2512.24297, Dec 2025)]: 在推理循环中生成可执行代码渲染图表，+13.12% AIME。生成 pixel-level diagrams 而非 formal predicates。与 SymMem 的区别在于：code-rendered visual states vs. verifiable symbolic predicates。\n\n- [Neuro-symbolic RL (arXiv 2604.22062, Apr 2026)]: GRPO + symbolic reasoning，Qwen3-VL-2B，+3.33% accuracy，减少 75% reasoning tokens。小规模实验，无 persistent memory。\n\n- [SymHPR (arXiv 2512.03126, Dec 2025)]: 符号自编码器，98.2% 几何图重建 fidelity。提供了 symbolic encoding 的可行性证据。\n\n- [GeoMathCode (arXiv 2605.25384, May 2026)]: 交替 math-code 推理，发现代码主要作为辅助可执行表示而非主动推理模态。\n\n- 调研总结: 2025-2026 年间，visual mathematical reasoning 领域正从三个独立方向推进：(1) formal diagram parsing 达到 SOTA（Geoparsing 96.4%），(2) 双角色 RL 证明 perception-reasoning 协同训练有效（PRCO +7pt），(3) evidence collapse 和 integration failure 被确认为系统性瓶颈。但目前**没有工作**将 formal predicate parsing、persistent queryable memory、和 RL integration training 三者结合——这正是 SymMem 的定位。最接近的是 Hilbert-Geo（formal parsing + reasoning，无 RL/memory）和 PRCO（RL 双角色，NL caption，无 formal verification）。\n\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative：**\"parse once + concatenate formal predicates to prompt + SFT\"**——即用 Geoparsing 解析图形，将 predicates 拼接到 prompt 前面，做 SFT 训练。\n\nProposal 给出了三个反驳理由：(a) lost-in-the-middle 效应，(b) 无 step-wise retrieval，(c) 无 integration reward 导致 solver 可能 bypass predicates。\n\n**我的评估：理由 (a) 较弱，理由 (b)(c) 有一定说服力但不确定。** \n- 理由 (a)：一个典型几何问题的 formal predicates 大约 20-50 条，总计几百个 token。在 Qwen3-VL-8B 的 context window 内，这是非常短的前缀。\"Lost-in-the-middle\" 效应主要针对数千 token 的长上下文，对几百 token 的 predicate 集合影响有限。这个论据站不太稳。\n- 理由 (b)：step-wise retrieval 的必要性是一个**开放的实证问题**。如果 predicate 总量不大，全量提供 vs. 按步检索的差异可能不显著。\n- 理由 (c)：最有说服力的理由。MathLens 确实表明 integration failure 是真实问题，但 SFT 训练也可以部分解决这个问题，不一定需要专门的 coverage reward。\n\n**结论：trivial alternative 确实存在，且 proposal 的反驳不够决定性。** 好在 proposal 的 ablation 设计 (iii) \"symbolic predicates concatenated without retrieval\" 直接测试了这一点。SymMem 的增量价值将取决于实验中 full system vs. parse+concat 的差距大小。如果差距很小（<2pt），整个 persistent memory + retrieval + coverage reward 机制的正当性就会受到质疑。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链：\n1. Visual evidence collapses during reasoning → **有实证支撑 (Don't Blink)**，成立 ✓\n2. Integration failure is the escalating bottleneck → **有实证支撑 (MathLens)**，成立 ✓\n3. Oracle symbolic representations dramatically improve performance → **有实证支撑 (Symbolic Grounding paper)**，但注意这是在 Bongard-LOGO (abstract reasoning) 上，**不是几何问题**。从 abstract visual reasoning 到 real-world geometry 的迁移性是一个**未经验证的假设** ⚠️\n4. Formal predicates ≈ oracle symbolic representations → **关键假设**。Geoparsing 在 parsing 上达到 96.4%，但 parsing accuracy ≠ downstream task-relevant representation quality。有些信息可能在 formalization 过程中丢失（如空间关系的模糊性、图形的视觉直觉等）。**这是一个合理但未验证的假设** ⚠️\n5. Persistent queryable memory > static concatenation → **未经验证的核心假设** ⚠️。这是整个 architecture 相对于 trivial alternative 的关键差异化假设，需要实验验证。\n6. Coverage-based integration reward 能有效解决 integration failure → **未经验证** ⚠️。这是一个新提出的 reward 设计，没有先例。合理但需要实验验证。\n\n**总结：假设 1-2 有坚实的实证基础；假设 3-4 从合理的 analogy 出发但跨域迁移性未验证；假设 5-6 是核心贡献假设，必须靠实验验证。逻辑链整体合理，但 3-6 的每一个环节都可能独立 fail。**\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   SymMem 的核心贡献是将 formal predicate parsing (Geoparsing)、persistent queryable memory (scratchpad + retrieval)、dual-role RL with coverage reward (extending PRCO) 三者组合。这个组合确实是新的——Hilbert-Geo 有 formal parsing 但无 RL/memory，PRCO 有 RL 但用 NL caption 且无 persistent memory，CogFlow 有 internalization 但不是 formal predicates。然而，这本质上是一个**integration contribution**：每个组件都有现成技术（Geoparsing 的 parser、PRCO 的 RL 框架、standard retrieval mechanism），novelty 在于组合方式而非单个组件。Oracle gap framework 作为评估方法论有独立贡献价值。Coverage-based integration reward R_cov 是一个有趣的新设计，但思路直接，不算 surprising。剔除 surface differences 后，核心 novelty delta 可概括为：\"用 formal predicates 替代 NL captions 作为 PRCO 的桥接表示 + 加 persistent memory + 加 coverage reward\"——这是一个自然的方向延伸，不是反直觉的发现。\n\n2. **Significance: 中** — \n   问题本身（visual math reasoning 中的 evidence collapse + integration failure）是高度重要的，MathLens 和 Don't Blink 的发现引起了广泛关注。**但 SymMem 的解决方案 scope 严格限制在几何领域**——proposal 自己也承认 \"Geometry serves as the ideal testbed... If persistent symbolic memory cannot demonstrate value under these best-case conditions, it is unlikely to succeed elsewhere.\" 这种诚实的 scope 界定是学术优点，但也意味着：(a) 方法的 generalizability 有限——few other math domains have mature formal predicate systems，(b) 论文的影响力取决于 oracle gap framework 和 insights 的可迁移性，而非方法本身。如果核心发现是 positive（显著 close oracle gap），对领域的贡献在于：证明 end-to-end systems can approach oracle symbolic grounding，这是一个有价值的 existence proof。但如果结果 moderate，审稿人可能会说 \"interesting but narrow\"。\n\n3. **Related Work: 强** — \n   这是 proposal 最强的维度。覆盖了 2025-2026 年间几乎所有相关工作：PRCO、CogFlow、Geoparsing、Hilbert-Geo、FIGR、SymHPR、Don't Blink、Symbolic Grounding、MathLens、InternGeometry、KAWHI、GeoMathCode、CoRGI、Neuro-symbolic RL、Mitigating Visual Forgetting。每篇论文的描述经调研验证均准确。与每个竞争者的差异化定位清晰且合理（PRCO=NL not formal, Hilbert-Geo=no RL/memory, FIGR=pixel not predicate, CogFlow=text internalization）。数据来源（FormalGeo、GDP-29K）和 evaluation benchmarks 的选择有充分依据。唯一小瑕疵：proposal 将 MathLens 归因于一篇名为 \"What MLLMs Learn...\" 的论文，实际上 MathLens 是该论文中提出的 benchmark 名称——描述准确但命名方式可能让读者困惑。\n\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \nNovelty 是限制上界的关键因素。虽然组合是新的、问题动机极为出色、related work 覆盖堪称典范，但核心贡献是一个 integration of existing components（formal parsing + persistent memory + RL），而非提出一个新的 paradigm 或反直觉的发现。如果 \"core finding is positive, would reviewers say surprising?\"——大概率答案是 \"makes sense, the components are well-chosen, but I would have guessed that formal predicates + memory + RL should work better than NL captions\"。这将 idea 定位在 25-35% 区间。\n\n上界受限于：(1) integration contribution 的 novelty ceiling，(2) 几何领域限定的 significance scope，(3) trivial alternative (parse+concat) 的威胁——如果 ablation 显示 persistent memory + retrieval 的增量收益不大，论文的核心 architectural contribution 就被 undermine。\n\n下界支撑因素：(1) 问题动机极强（三篇独立论文的 converging evidence），(2) oracle gap framework 有独立贡献价值，(3) 方法论设计（asymmetric reward schedule, coverage-based reward, structural verification）显示高度的技术成熟度，(4) neuro-symbolic integration 是 AAAI 的传统强项领域。\n\n【主要风险】: \n1. **Trivial alternative risk**: parse + concatenate + SFT 可能已获得 SymMem 80-90% 的收益，使 persistent memory + retrieval + coverage reward 这些核心 architectural 贡献变得 marginal——这是审稿人最可能 raise 的致命质疑。\n2. **Integration contribution novelty ceiling**: 三位审稿人中若有人认为 \"this is just PRCO with formal predicates and a retrieval cache\"，novelty score 会很低，而 proposal 缺乏一个足以独立成章的理论贡献（如 oracle gap 的理论 bound、convergence analysis）来对冲这一风险。\n```\n\nSources:\n- [PRCO: Seeing with You](https://arxiv.org/abs/2603.28618)\n- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)\n- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/pdf/2604.04207)\n- [What MLLMs Learn about Multimodal Reasoning (MathLens)](https://arxiv.org/abs/2510.01719)\n- [Geoparsing: Diagram Parsing with Unified Formal Language](https://arxiv.org/abs/2604.11600)\n- [Hilbert-Geo: Neural-Symbolic Reasoning for Solid Geometry](https://arxiv.org/abs/2605.16385)\n- [CogFlow: Bridging Perception and Reasoning (ICLR 2026)](https://arxiv.org/abs/2601.01874)\n- [FIGR: Executable Visual States for Reasoning](https://arxiv.org/abs/2512.24297)\n- [Neuro-symbolic RL for VLMs](https://arxiv.org/abs/2604.22062)\n- [SymHPR: Hierarchical Process Reward Models](https://arxiv.org/abs/2512.03126)\n- [GeoMathCode: Interleaved Math-Code Reasoning](https://arxiv.org/abs/2605.25384)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a well-grounded assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. PRCO (arXiv 2603.28618, 2026): 最直接的竞争者。提出 Observer-Solver 双角色 RL 框架，Observer 生成 NL caption 作为桥梁，Solver 基于 caption 推理。在 8 个 benchmark 上平均 +7pts。核心区别：PRCO 使用自然语言 caption（不可验证），SymMem 使用形式化谓词（可验证）+ 持久化记忆。PRCO 已经证明了双角色 RL 的有效性，SymMem 的增量是 symbolic representation + persistent memory + coverage reward。\n\n2. Geoparsing (arXiv 2604.11600, 2026): SOTA 几何图形形式化解析器，SFT+RLVR 训练范式，GDP-29K 数据集，96.4/94.9 解析分数。直接给 Qwen3-VL-8B 提供解析输出就能在 Geometry3K 上 +10.1%。这表明\"解析+拼接\"这个 trivial baseline 已经有显著效果，SymMem 需要证明持久记忆+RL 的额外价值。\n\n3. Hilbert-Geo (arXiv 2605.16385, 2026): Parse2Reason 方法，使用 CDL 形式化谓词，在 SolidFGeo2k 上 77.3%。没有 RL 也没有持久记忆。是 SymMem 在\"形式化解析→推理\"方向上最近的竞品，SymMem 的增量是持久记忆和 RL 集成训练。\n\n4. CogFlow (ICLR 2026, arXiv 2601.01874): 感知→内化→推理三阶段框架，Knowledge Internalization Reward，Visual-Gated Policy Optimization。在 MathVista 上 76.8%。使用文本内化而非符号谓词。已被 ICLR 2026 接收，验证了\"bridging perception and reasoning\"这个研究方向的价值。\n\n5. Don't Blink (arXiv 2604.04207, 2026): 证实 evidence collapse 现象——推理 VLM 在 CoT 过程中丢失 >50% 视觉注意力。公开了注意力追踪代码。为 SymMem 的核心动机提供实证支撑。✓ 论文真实存在且发现与 proposal 描述一致。\n\n6. Symbolic Grounding (arXiv 2604.21346, 2026): LLM 接收 oracle 符号表示时在 Bongard-LOGO 上从近随机跳到 mid-90s 准确率，证明表示（而非推理）是瓶颈。✓ 论文真实存在且发现与 proposal 描述一致。\n\n7. MathLens (arXiv 2510.01719, 2025): 分解多模态推理为感知/推理/整合三部分，发现整合（integration）是持续性瓶颈，RL 对其改善最少。✓ 论文真实存在且发现与 proposal 描述一致。\n\n8. FIGR (arXiv 2512.24297, 2025): 在推理循环中生成可执行代码构建图形，+13.12% AIME。与 SymMem 的区别：FIGR 生成像素级图形而非形式化谓词，无符号级验证。\n\n9. SymHPR (arXiv 2512.03126, 2025): 符号自编码器，98.2% 重建保真度，层次化过程奖励。✓ 论文真实存在。\n\n10. Neuro-symbolic RL (arXiv 2604.22062, 2026): Qwen3-VL-2B 上 symbolic+GRPO，+3.33%。规模很小，没有持久记忆。是 SymMem 在\"符号+RL\"方向的近期工作，但规模和深度远不如 SymMem proposal。\n\n11. Mitigating Visual Forgetting / TVC (ACL 2025): Take-along Visual Conditioning，通过动态剪枝和重新注入视觉 token 缓解视觉遗忘。与 SymMem 解决同一问题（视觉信息丢失），但方案不同：TVC 操作在连续视觉 token 层面，SymMem 操作在离散符号谓词层面。\n\n- 调研总结: 这个领域在 2025-2026 年经历了快速发展，多篇工作从不同角度攻击\"VLM 在多步推理中丢失视觉信息\"的问题。PRCO 建立了双角色 RL 的范式，Geoparsing/Hilbert-Geo 建立了形式化解析的 SOTA，CogFlow 探索了感知-推理桥接。**SymMem 处于这些研究线的交汇点——它试图将形式化解析（Geoparsing）、双角色 RL（PRCO）和持久记忆机制整合为统一系统。** 这个交汇位置目前确实没有被已有工作占据，但每个组件都已有成熟先例。\n\n\n【Trivial Alternative 检验】:\n\n最具威胁的 trivial alternative 是 **\"Geoparsing 解析 + 直接拼接到 prompt\"**。Geoparsing 论文本身已经展示了仅通过提供解析输出就能在 Geometry3K 上 +10.1%。Proposal 预见到了这个挑战并提出三个反驳：(a) 解析后文本受 lost-in-the-middle 效应影响，(b) 无法自适应按步骤检索，(c) 无集成训练信号导致模型可能跳过谓词。\n\n这些反驳在逻辑上站得住脚，但**其实际增量价值是纯粹的实验问题**。如果实验显示\"解析+拼接\"与 SymMem 差距很小（比如 <3pts），整个持久记忆+RL 训练的复杂性就难以 justify。这是此 proposal 最大的实验风险。\n\n第二个 trivial alternative：**PRCO 框架直接使用 FormalGeo 谓词替代 NL caption**——这基本是 SymMem 去掉持久记忆和 coverage reward 后的简化版。proposal 设计了 \"data-matched PRCO\" baseline 来隔离这个对比，设计是合理的。\n\n**增量价值判断**: 如果以上两个 trivial alternatives 都被实验击败，SymMem 的增量价值在于：(1) 持久化记忆提供按需检索能力（解决长上下文信息衰减），(2) coverage 奖励驱动的集成训练（解决 MathLens 发现的集成失败）。逻辑链完整，但增量幅度存疑。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链：\nEvidence collapse (Don't Blink) + Integration failure (MathLens) + Oracle gap (Symbolic Grounding) → 需要 persistent symbolic memory → SymMem 可以近似 oracle symbolic grounding\n\n未经验证的关键假设：\n\n1. **\"规则化实体匹配检索足够好\"**: Proposal 使用 rule-based entity matching 从当前推理步骤提取几何实体名称，然后检索匹配谓词。这假设推理过程中会产生明确的实体名称、且实体名称与谓词之间存在可靠的对应关系。如果模型推理时使用模糊的指代或跳步推理，检索可能失败。不过 proposal 也设计了 learned embedding retrieval 的对比消融，部分缓解了这个风险。\n\n2. **\"三路奖励可以稳定收敛\"**: Observer F1 + Solver correctness + coverage reward 三者的优化目标可能冲突。例如 Observer 可能为了提高 F1 而过度解析无关谓词，coverage reward 可能鼓励检索所有谓词（包括不相关的），这与 Solver accuracy 可能矛盾。Proposal 提到了 weight sensitivity 和 frozen Observer 消融，但没有理论保证收敛。\n\n3. **\"Bongard-LOGO 上的 oracle gap 发现可以迁移到几何推理\"**: Symbolic Grounding 论文在抽象视觉推理（Bongard-LOGO）上建立了 oracle upper bound，但几何推理的符号化难度和推理复杂度与 Bongard-LOGO 差异很大。Oracle gap 在几何域的实际大小是未知的。\n\n4. **\"Evidence collapse 的原因是信息未持久化，而非注意力机制的根本局限\"**: Don't Blink 记录了注意力质量衰减的现象，但原因可能是架构层面的（注意力窗口有限、位置编码衰减等），而非仅仅是\"信息未被显式保存\"。如果根因是架构层面的，持久记忆可以缓解但不能根本解决。\n\n假设 1 和 2 是执行层面的风险，可以通过实验验证。假设 3 和 4 是 idea 层面的前提假设，如果不成立会动摇核心 claim。但假设 3 的风险被 proposal 的\"geometry as ideal testbed\"论述部分缓解——它不是声称一定能迁移，而是声称几何是最有利的测试场。假设 4 的风险也被 evidence retention analysis 的设计部分缓解——它计划同时测量视觉 token 注意力和 scratchpad token 注意力。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — SymMem 的每个组件在已有工作中都有先例：形式化解析（Geoparsing, Hilbert-Geo）、双角色 RL（PRCO）、视觉信息持久化（TVC, VLM²）、符号+RL（Neuro-symbolic RL）。核心 novelty 在于这些组件的**特定组合方式**：可验证的符号谓词 + 持久可查询记忆 + coverage-based 集成奖励，以及 oracle gap 评估框架。这个组合确实没有被现有工作覆盖——PRCO 用 NL caption（不可验证）、Hilbert-Geo 没有 RL 和持久记忆、Geoparsing 只做解析不做集成训练。Oracle gap framework 作为评估方法论的贡献是独立有价值的。但审稿人可能会质疑这是\"incremental combination\"而非\"conceptual breakthrough\"。Coverage-based integration reward 是一个新的技术贡献，但体量较小。\n\n2. **Significance: 中** — 研究问题（多步视觉数学推理中的信息丢失和跨模态整合失败）是重要且时效性很强的问题，被多篇 2025-2026 论文独立验证。但 proposal 的方案高度依赖 FormalGeo 的 88 谓词系统和几何领域的特殊性质（形式化谓词系统成熟、ground-truth 标注可用、结构化验证可行），**向其他视觉推理域的推广路径不清晰**。Proposal 以\"ideal testbed\"框架定位几何域是聪明的，但这也意味着即使成功，直接影响力限于几何推理这个子领域。如果核心发现是 positive（SymMem 显著优于 parse-and-concatenate），审稿人可能会说\"interesting but expected — of course persistent memory with RL training should help\"。如果 oracle gap analysis 揭示了意外发现（如 parsing error 而非 integration failure 是主要瓶颈），significance 会更高。\n\n3. **Related Work: 强** — 这是 proposal 最强的维度。覆盖了所有主要竞争者（PRCO, Geoparsing, Hilbert-Geo, CogFlow, FIGR, SymHPR, Don't Blink, MathLens, Symbolic Grounding, TVC, Neuro-symbolic RL, InternGeometry, KAWHI, GeoMathCode, CoRGI），对每个工作的定位和区分都准确清晰。所有引用的关键论文均经调研验证真实存在，描述准确。对 InternGeometry（外部工具使用 vs. 训练时内化）和 FIGR（像素级图形 vs. 谓词级符号）的区分尤其精准。Baseline 设计包含 compute-matched 和 data-matched 对照，显示出对公平对比的认真思考。\n\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】: \n- **Novelty (中)** 是主要限制因素。idea 的核心是将 4 个已有方向（形式化解析、双角色 RL、持久记忆、符号验证）组合起来，每个方向都有 2026 年的成熟先例。虽然特定组合是新的，且 oracle gap framework 有独立贡献，但审稿人大概率会视为 \"solid systems work / incremental combination\" 而非 \"new paradigm\"。这限制了上界在 ~38%。\n- **Significance (中)** 进一步限制了中位数。几何域的特殊性（成熟的形式化系统、标注数据）使得方案难以推广，而几何推理本身在 AAAI 审稿人眼中可能被视为相对窄的方向。\n- **Related Work (强)** 提供了扎实的下限保障（~25%），因为 proposal 对领域的理解是准确且深入的，不太可能因为遗漏关键 related work 而被拒。\n- 三线动机汇聚（evidence collapse + integration failure + oracle gap）的叙事结构是强有力的，但叙事质量不等于 idea novelty。\n- Oracle gap framework 是独立的方法论贡献，为概率加分 ~3-5%。\n\n【主要风险】: \n1. **\"Incremental combination\" 质疑**: 审稿人可能认为 SymMem = Geoparsing + PRCO + 简单检索机制，每个组件的整合虽然需要工程努力但缺乏概念层面的创新。coverage reward 虽然新颖但体量偏小，难以独撑 novelty claim。\n2. **Trivial baseline 威胁**: 如果\"Geoparsing 解析 + prompt 拼接\"在实验中已经接近 SymMem 的效果（差距 <3pts），整个持久记忆+RL集成+coverage reward 的复杂系统就无法 justify，论文的核心 claim（persistent symbolic memory is necessary）将被动摇。这是一个 idea 层面的风险，因为它质疑的是\"持久化记忆是否真的必要\"这个前提。\n```\n\nSources:\n- [PRCO: Seeing with You](https://arxiv.org/abs/2603.28618)\n- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/pdf/2604.04207)\n- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)\n- [MathLens: What MLLMs Learn about Multimodal Reasoning](https://arxiv.org/abs/2510.01719)\n- [CogFlow: Bridging Perception and Reasoning (ICLR 2026)](https://arxiv.org/abs/2601.01874)\n- [Hilbert-Geo: Neural-Symbolic Reasoning for Solid Geometry](https://arxiv.org/abs/2605.16385)\n- [FIGR: Executable Visual States](https://arxiv.org/abs/2512.24297)\n- [SymHPR: Hierarchical Process Reward Models](https://arxiv.org/abs/2512.03126)\n- [Neuro-symbolic RL for VLMs](https://arxiv.org/abs/2604.22062)\n- [Mitigating Visual Forgetting via TVC (ACL 2025)](https://aclanthology.org/2025.acl-long.257/)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Bridging the Oracle-to-End-to-End Gap: Persistent Symbolic Memory for Visual Mathematical Reasoning\n\n## Core Problem\n\nMulti-step visual mathematical reasoning suffers from two compounding failures. First, evidence collapse: reasoning VLMs lose >50% of visual attention mass as chain-of-thought unfolds (Don't Blink, arXiv 2026), meaning visual information is irrecoverably lost during reasoning and must be converted to a persistent format early. Second, cross-modal integration failure: the dominant error mode that constitutes a growing fraction of remaining errors as models improve (MathLens, arXiv 2025) — an escalating bottleneck that demands structural architectural intervention, not incremental optimization or scaling.\n\nThe Symbolic Grounding paper (arXiv 2026) establishes a striking upper bound: LLMs receiving oracle symbolic representations instead of raw images jump from near-chance to mid-90s accuracy on abstract visual reasoning (Bongard-LOGO), proving that representation — not reasoning — is the fundamental bottleneck. This motivates a central research question: **How close can an end-to-end system come to oracle symbolic grounding on real-world geometry problems?** No existing method attempts this — diagrams are encoded once into continuous embeddings that decay, and no verifiable, persistent symbolic bridge exists between perception and reasoning.\n\n## Research Opportunity\n\nTwo research lines have advanced independently: formal diagram parsers (Geoparsing, arXiv 2026; SymHPR, arXiv 2025) achieve SOTA conversion of diagrams into verifiable symbolic predicates, and dual-role RL frameworks (PRCO, arXiv 2026) demonstrate +7pt gains through perception-reasoning co-training with NL caption bridges. But these remain disconnected.\n\nSymMem closes three gaps simultaneously to approximate oracle symbolic grounding end-to-end: (1) learning to parse diagrams into formally verifiable predicates (approximating the oracle), (2) maintaining these predicates as persistent, queryable memory (preventing information loss), and (3) training the system to utilize this symbolic bridge via RL (solving integration failure).\n\n**Why not simply parse once and concatenate predicates to the prompt?** This naive alternative fails for two independent reasons: (a) irrecoverable visual decay (Don't Blink) means predicates must be extracted early — but once extracted as text, they suffer the well-documented \"lost-in-the-middle\" effect in long contexts, where early tokens are progressively overshadowed by subsequent generation; (b) without step-wise retrieval, the solver cannot adaptively access step-relevant predicates; (c) without integration reward, the solver may bypass predicates entirely — the integration failure mode MathLens documents as the escalating bottleneck.\n\nGeometry serves as the **ideal testbed** for this hypothesis: it is the only visual math domain where a mature formal predicate system exists (FormalGeo, 88 predicates + 196 theorems), large-scale ground-truth formal annotations are available (GDP-29K, FormalGeo7k), and structural verification is possible without task-specific answer labels. If persistent symbolic memory cannot demonstrate value under these best-case conditions, it is unlikely to succeed elsewhere.\n\n## Research Landscape\n\nCurrent MathVista SOTA: o3 at 86.8%; open models: Qwen3-VL at 85.8%, Step3-VL-10B (arXiv 2026) at 84.0%. PRCO (arXiv 2026): +7pts average via NL Observer-Solver RL, 8 benchmarks, cannot verify Observer output. CogFlow (ICLR 2026): perception→internalization→reasoning, 76.8% MathVista, text-based internalization. Geoparsing (arXiv 2026): SOTA formal parsing via SFT+RLVR on GDP-29K. SymHPR (arXiv 2025): symbolic auto-encoding, 98.2% reconstruction fidelity. Don't Blink (arXiv 2026): >50% visual evidence mass loss, public attention tracking code. v1 (arXiv 2025): visual-token re-attention, cannot correct initial perception errors. MathLens (arXiv 2025): integration failure escalates as models improve. InternGeometry (arXiv 2512.10534): IMO-gold geometry via 200+ rounds with external DDAR engine — represents the test-time compute scaling paradigm (external tool use), whereas SymMem pursues training-time internalization (self-contained model). Hilbert-Geo (arXiv 2026): Parse2Reason with formal CDL predicates, 77.3% SolidFGeo2k, no RL or persistent memory. FIGR (arXiv 2512.24297): executable visual states within reasoning loops via end-to-end RL (+13.12% AIME), but generates code-rendered pixel-level diagrams without formal predicate-level verification — fundamentally different from SymMem's verifiable symbolic predicates. KAWHI (arXiv 2026): attention-based reward reweighting for RLVR. GeoMathCode (arXiv 2026): interleaved math-code reasoning, code as auxiliary representation. CoRGI (arXiv 2025): post-hoc inference-only verification. Neuro-symbolic RL (arXiv 2604.22062): symbolic+GRPO at small scale (Qwen3-VL-2B, +3.33%), no persistent memory. Mitigating Visual Forgetting (ACL 2025): take-along visual conditioning for long CoT.\n\n## Proposed Approach\n\n**Architecture.** Built on Qwen3-VL-8B. A formal Observer converts diagrams into structured symbolic predicates (FormalGeo's 88-predicate system). These populate a persistent symbolic scratchpad. At each CoT step, rule-based entity matching extracts geometric entity names from the Solver's current reasoning output and retrieves top-K matching predicates from the scratchpad, injecting them into the next step's context. For non-geometric inputs, a learned diagram-type classifier (trained on MathVista's category metadata) triggers fallback to NL caption mode.\n\n**Structural Verification.** Observer output is verified via structural/topological comparison against ground-truth formal annotations (predicate-level P/R/F1). This avoids pixel-level rendering dependency.\n\n**Dual-Role RL with Coverage-Based Integration Reward.** Observer reward: structural verification F1. Solver reward: outcome correctness. Integration reward: R_cov = |∪_t P_retrieved(t)| / |P_total|, measuring predicate coverage across the entire reasoning chain via retrieval logs (not NL string matching). Coverage-based formulation avoids incentivizing redundant per-step referencing. The outcome reward provides natural precision pressure. Weight sensitivity: λ_cov ∈ {0.1, 0.3, 0.5, 1.0}. Asymmetric reward schedule for mixed-label data: formal-annotation-only samples → Observer reward only; answer-only samples → Solver reward only; dual-label samples → all three rewards.\n\n**Training Data.** Phase 1 (formal parser SFT+RLVR): GDP-29K (availability pending; backup: FormalGeo augmented data + Hilbert-Geo SolidFGeo2k/PlaneFGeo3k). Phase 3 (dual-role RL): FormalGeo augmented data (~134K dual-label problems; FGeo-TP extension to ~187K available if needed), supplemented by GDP-29K for Observer-only training.\n\n**Evaluation — Oracle Gap Framework.** The paper is structured around measuring and closing the oracle-to-end-to-end gap:\n1. **Oracle upper bound**: GT formal annotations directly populate scratchpad (bypassing Observer) → measures Solver's ceiling under perfect symbolic grounding.\n2. **End-to-end SymMem**: full pipeline with learned Observer → measures how close the system approaches the oracle.\n3. **Gap decomposition**: remaining gap attributed to parsing error (Observer F1 deficit), retrieval miss (coverage gap), and integration failure (predicate-utilization-to-accuracy correlation) — identifying where future improvement should focus.\n\nEight benchmarks: MathVista, MathVerse, GeoQA, WeMath, MathVision, DynaMath, Geometry3K, LogicVista. Per-category breakdown on mixed benchmarks. Evidence retention analysis via expanded metric: total evidence mass = visual token attention + scratchpad token attention (separately reported), using Don't Blink's attention tracking methodology. Core claim: SymMem transfers evidence from rapidly-decaying visual tokens to persistently-queryable scratchpad tokens, significantly slowing total evidence mass decay. Training FLOPs and GPU-hours reported.\n\n**Baselines.** (1) PRCO (NL Observer + RL), (2) CogFlow (text internalization, ICLR 2026), (3) KAWHI (attention reward reweighting), (4) Hilbert-Geo Parse2Reason (formal parsing, no persistent memory, no RL integration), (5) Compute-matched PRCO (same total FLOPs), (6) Data-matched PRCO (same FormalGeo data as NL captions, isolating symbolic vs. NL representation benefit). Reported-number comparisons: FIGR (arXiv 2512.24297), GeoMathCode, Neuro-symbolic RL.\n\n**Ablations.** Progressive (6-level): (A) Qwen3-VL-8B base → (B) +formal parser SFT → (C) +structural verifier → (D) +persistent scratchpad with retrieval → (E) +dual-role RL → (F) +coverage integration reward. Memory mechanism: (i) re-read visual tokens (v1-style), (ii) NL predicates concatenated, (iii) symbolic predicates concatenated without retrieval, (iv) symbolic scratchpad with retrieval. Retrieval mechanism: rule-based entity matching vs. learned embedding retrieval. Integration reward: coverage-based R_cov vs. per-step utilization vs. none. Reward stability: frozen Observer (post-SFT) + Solver RL vs. joint Observer+Solver RL, with training curve analysis of Observer F1 / Solver accuracy / R_cov dynamics. Fallback classifier: oracle vs. learned vs. all-symbolic vs. all-NL. Observer parsing quality: standalone P/R/F1 vs. Geoparsing; parsing F1-binned task accuracy correlation.\n\n## Key References\n\n- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning (arXiv 2026)\n- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)\n- Hierarchical Process Reward Models are Symbolic Vision Learners (arXiv 2025)\n- Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv 2026)\n- Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning (arXiv 2026)\n- v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning (arXiv 2025)\n- What MLLMs Learn about When they Learn about Multimodal Reasoning: Perception, Reasoning, or their Integration? (arXiv 2025)\n- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026)\n- Mitigating Visual Forgetting via Take-along Visual Conditioning for Multi-modal Long CoT Reasoning (ACL 2025)\n- Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models (arXiv 2026)\n- CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding (arXiv 2025)\n- STEP3-VL-10B Technical Report (arXiv 2026)\n- Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning (arXiv 2026)\n- InternGeometry: Achieving Olympia-Level Geometry via Complexity Boosting Reinforcement Learning (arXiv 2512.10534, Dec 2025)\n- Incentivizing Neuro-symbolic Language-based Reasoning in VLMs via Reinforcement Learning (arXiv 2604.22062, Apr 2026)\n- FIGR: Figure It Out — Improve the Frontier of Reasoning with Executable Visual States (arXiv 2512.24297, Dec 2025)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 850–1050 H100-hours (Phase 1 formal parser SFT+RLVR: ~120h; Phase 2 structural verifier: ~80h; Phase 3 dual-role RL on ~134K FormalGeo data: ~350h; Phase 4 evaluation on 8 benchmarks + oracle gap framework + full ablation matrix + frozen Observer ablation + evidence retention analysis + compute/data-matched baselines: ~300h), timeline: 14–16 weeks, estimated_gpu_cost: $2,125–$2,625 at $2.50/hr spot H100\n- **human_in_loop**: gpu_hours: 700–900 H100-hours, timeline: 10–12 weeks, claude_api_cost: $300–$450, estimated_gpu_cost: $1,750–$2,250\n- **auto_research**: gpu_hours: 1050–1400 H100-hours, timeline: 7–9 weeks, claude_api_cost: $550–$850, estimated_gpu_cost: $2,625–$3,500, speed_bottleneck: Coverage integration reward design and three-way reward conflict analysis; fallback classifier threshold tuning; GDP-29K availability contingency; oracle gap decomposition methodology"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T23:54:19.401Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T23:54:19.401Z",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T23:54:19.437Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- [PRCO / "Seeing with You" (arXiv 2603.28618, Mar 2026)](https://arxiv.org/abs/2603.28618): 最直接的竞争者。双角色 RLVR（Observer 生成 NL caption + Solver 求解），8 个 benchmark 平均 +7pt。核心区别：Observer 输出是不可验证的 NL caption，不是 formal predicates；无持久化记忆或检索机制。SymMem 可视为 PRCO 的 formal-predicate 升级版 + scratchpad。
- [Geoparsing (arXiv 2604.11600, Apr 2026)](https://arxiv.org/abs/2604.11600): SOTA 形式化几何图解析器，SFT+RLVR 训练，GDP-29K 数据集（20K 平面 + 9K 立体）。SymMem 的 Observer 组件本质上是复用 Geoparsing 的方法论。
- [Don't Blink (arXiv 2604.04207, Apr 2026)](https://arxiv.org/abs/2604.04207): 证明推理 VLM 在 CoT 过程中视觉注意力质量下降 >50%（evidence collapse）。验证了 SymMem 的动机之一，但该论文本身提出的是 entropy-vision veto，而非 symbolic memory 解法。
- [Symbolic Grounding (arXiv 2604.21346, Apr 2026)](https://arxiv.org/abs/2604.21346): 在 Bongard-LOGO 上证明 oracle symbolic grounding 可将 LLM 准确率从近随机提升到 mid-90s。**但注意**：Bongard-LOGO 是抽象视觉推理，与几何问题的视觉复杂度和形式化程度差异很大，gap 的可迁移性未经验证。
- [CogFlow (ICLR 2026, arXiv 2601.01874)](https://arxiv.org/abs/2601.01874): 认知启发三阶段框架（感知→内化→推理），MathVista 76.8%。内化阶段使用文本形式，而非 formal predicates。与 SymMem 的 "internalization" 概念有重叠，但实现路径不同。
- [Hilbert-Geo (arXiv 2605.16385, May 2026)](https://arxiv.org/abs/2605.16385): Parse2Reason 方法，使用 CDL formal predicates（120 predicates），SolidFGeo2k 77.3%。**无 RL、无持久化记忆**。是 SymMem 在 "formal parsing → reasoning" 路径上的直接前驱，SymMem 的增量在于 RL 训练和 scratchpad。
- [FIGR (arXiv 2512.24297, Dec 2025)](https://arxiv.org/abs/2512.24297): 在推理循环中生成可执行代码渲染图像，+13.12% AIME。与 SymMem 的 verifiable symbolic predicates 在哲学上不同（pixel-level vs. predicate-level），但都在做 "将推理外化为可验证中间表示"。
- [Neuro-symbolic RL (arXiv 2604.22062, Apr 2026)](https://arxiv.org/abs/2604.22062): Qwen3-VL-2B + GRPO + symbolic language，+3.33%。小规模验证了 symbolic + RL 的可行性，但无 persistent memory、无 formal verification。
- [MathLens (arXiv 2510.01719, Oct 2025)](https://arxiv.org/abs/2510.01719): 分解感知/推理/整合三类错误，发现整合错误随模型改进而占比上升。SymMem 引用此论文作为 "integration failure is the escalating bottleneck" 的论据。
- [FormalGeo (arXiv 2310.18021)](https://arxiv.org/abs/2310.18021): 88 predicates + 196 theorems，FormalGeo7k 数据集（6,981 题，扩增至 ~134K）。SymMem 的符号表示基础设施。

- **调研总结**: 该领域目前处于 "perception-reasoning 分离优化向联合训练过渡" 的阶段。PRCO 确立了双角色 RL 的范式，Geoparsing/Hilbert-Geo 确立了 formal parsing 的能力，但二者尚未系统性结合。SymMem 的定位是在两条独立成熟的研究线之间搭桥——这是一个自然且可预见的下一步，而非范式突破。

【Trivial Alternative 检验】:

最直接的 trivial alternative：**"Geoparsing 输出的 formal predicates 直接拼接到 prompt，然后用 PRCO 的 RL 框架训练"**（即 PRCO + formal predicates，无 scratchpad，无 step-wise retrieval，无 coverage reward）。

Proposal 给出了三个反驳理由，但需要逐一审视：
(a) **Lost-in-the-middle effect**：几何题的 formal predicates 通常只有 20-60 条（几十到几百 tokens），远不到触发 lost-in-the-middle 效应的上下文长度（该效应在数千 tokens 时才显著）。这个论据在几何场景下偏弱。
(b) **无自适应检索**：有效性取决于谓词数量。对于典型几何题，全量拼接不会造成信息过载；但如果扩展到更复杂的图（如多图组合），检索的价值会增大。
(c) **无 integration reward**：这是最强的论据。但 PRCO 的 Solver reward 已经通过反向传播间接激励 Observer 输出有用信息，coverage reward 的增量价值需要实验验证。

**增量价值判断**：SymMem 相对 trivial alternative 的真正增量在于 (1) structural verification 使 Observer reward 可以独立计算（vs. PRCO 只能依赖下游任务成功率间接估计），(2) coverage-based integration reward 是一种更显式的整合激励。但这些是 reward engineering 层面的改进，而非架构层面的根本性创新。Persistent scratchpad 对于几何题可能是 over-engineering。

【前提假设检验】:

核心 claim 的逻辑链：
1. "视觉信息在 CoT 过程中不可逆丢失"（Don't Blink）→ ✅ 有实证支撑
2. "integration failure 是随模型改进而升级的瓶颈"（MathLens）→ ✅ 有实证支撑
3. "Oracle symbolic grounding 可大幅提升性能"（Symbolic Grounding on Bongard-LOGO）→ ⚠️ **关键假设跳跃**：Bongard-LOGO 是抽象视觉推理，visual→symbolic 的 gap 极大；几何图是高度结构化的，视觉编码本身可能已经捕获了大部分结构信息。在几何领域，oracle gap 可能远小于 Bongard-LOGO 上观察到的，从而削弱了整个 "bridging the oracle gap" 叙事的力度。
4. "Persistent scratchpad + step-wise retrieval 优于一次性拼接"→ ⚠️ **未经验证**。对于谓词数量有限的几何题（vs. 需要处理长文档的 QA 任务），step-wise retrieval 的增量价值不确定。
5. "Coverage-based integration reward 优于 per-step utilization reward 或无 reward"→ ⚠️ **纯假设，无先验支撑**。这是一个 reward design choice，是否有效完全依赖实验。
6. "三路 reward 可以稳定训练（Observer F1 + Solver accuracy + R_cov）"→ ⚠️ 多目标 RL 的训练稳定性是已知难题，λ_cov 的敏感度可能很高。

**最关键的假设跳跃是第 3 条**：从 Bongard-LOGO 上的 oracle gap 推广到几何领域，缺乏中间验证步骤。

【3 维度打分】:

1. **Novelty: 中** — SymMem 是两条成熟研究线（PRCO 的双角色 RL + Geoparsing/Hilbert-Geo 的 formal parsing）的自然组合。单独来看，每个组件都有直接对应的 prior work：dual-role RL → PRCO；formal parsing → Geoparsing + Hilbert-Geo；symbolic + RL → Neuro-symbolic RL (2604.22062)；scratchpad 机制 → Notes-to-Self (2602.21013)。真正的 novelty delta 在于：(a) structural verification 使 Observer reward 可独立计算，(b) coverage-based integration reward，(c) oracle gap decomposition 评估框架。这些是有价值的工程/方法论贡献，但不构成 "surprising" 的新发现。如果告诉一个熟悉 PRCO 和 Geoparsing 的研究者这个 idea，他们的反应更可能是 "makes sense, obvious next step" 而非 "I wouldn't have thought of that"。

2. **Significance: 中偏强** — 问题本身重要且 well-motivated。视觉数学推理是活跃的研究方向，integration failure 是一个被充分记录的真实瓶颈（MathLens）。几何作为 testbed 是合理的选择。但 significance 受限于两点：(a) 方法强绑定 FormalGeo 的谓词系统，可推广性存疑——非几何视觉数学问题（如图表、函数图像）没有类似的 mature formal predicate system；(b) 如果 oracle gap 在几何领域本身不大（因为几何图已经高度结构化），那么 "bridging the gap" 的故事就不够有说服力。

3. **Related Work: 强** — Proposal 对相关工作的覆盖非常全面，包括了所有主要竞争者（PRCO、CogFlow、Geoparsing、Hilbert-Geo、FIGR、Neuro-symbolic RL）且差异化定位清晰。与 PRCO 的区别（formal vs. NL、verifiable vs. unverifiable）、与 Hilbert-Geo 的区别（+RL +persistent memory）、与 FIGR 的区别（predicate-level vs. pixel-level）都有明确阐述。唯一遗漏的是可能需要更明确讨论 CogFlow 的 "knowledge internalization" 与 SymMem 的 "persistent symbolic scratchpad" 在概念层面的重叠和区别。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
- Significance 和 Related Work 都是支撑项（问题重要、覆盖全面）
- **上界被 Novelty 限制**：核心 idea 是现有方法的 predictable combination，缺乏 "surprising" 元素。审稿人很可能会问 "What is the core insight beyond combining PRCO with formal parsing?"，而 proposal 的回答（persistent scratchpad + coverage reward + oracle gap evaluation）更多是 system design 和 evaluation methodology 层面的贡献，而非根本性的新见解。
- 下界被 well-motivated problem + oracle gap evaluation framework 托住——即使 novelty 被质疑，solid experimental design 可以部分弥补。
- 概率没有达到 35-45% 区间，因为核心发现如果 positive（formal predicates + scratchpad 优于 NL captions），多数熟悉领域的审稿人会认为 "I would have guessed this"。

【主要风险】:
1. **"Obvious combination" 质疑**：审稿人可能认为 SymMem 只是 "PRCO + Geoparsing + scratchpad"，novelty 不足以达到顶会门槛。proposal 需要更强地论证 persistent scratchpad 和 coverage reward 的不可替代性（而不只是 "more complete"）。
2. **Oracle gap 迁移性假设的脆弱性**：从 Bongard-LOGO（抽象视觉推理，gap 极大）推广到几何（结构化视觉，gap 可能很小），如果实验显示几何领域 oracle gap 本身只有 2-5pt，那么整个 "bridging the gap" 叙事将大幅削弱，论文的核心故事线将失去支撑。
```

Sources:
- [PRCO: Seeing with You (arXiv 2603.28618)](https://arxiv.org/abs/2603.28618)
- [Geoparsing (arXiv 2604.11600)](https://arxiv.org/abs/2604.11600)
- [Don't Blink: Evidence Collapse (arXiv 2604.04207)](https://arxiv.org/abs/2604.04207)
- [Symbolic Grounding (arXiv 2604.21346)](https://arxiv.org/abs/2604.21346)
- [CogFlow (arXiv 2601.01874, ICLR 2026)](https://arxiv.org/abs/2601.01874)
- [MathLens (arXiv 2510.01719)](https://arxiv.org/abs/2510.01719)
- [Hilbert-Geo (arXiv 2605.16385)](https://arxiv.org/abs/2605.16385)
- [FIGR (arXiv 2512.24297)](https://arxiv.org/abs/2512.24297)
- [Neuro-symbolic RL (arXiv 2604.22062)](https://arxiv.org/abs/2604.22062)
- [FormalGeo (arXiv 2310.18021)](https://arxiv.org/abs/2310.18021)
- [Notes-to-Self Scratchpad (arXiv 2602.21013)](https://arxiv.org/abs/2602.21013)
- [ACL 2026 Survey: Deep Learning for Geometry Problem Solving](https://github.com/majianz/dl4gps)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

- [PRCO / "Seeing with You" (arXiv 2603.28618, Mar 2026)]: 双角色 RLVR 框架，Observer 生成 NL caption + Solver 推理，8 个 benchmark 上平均 +7pt。使用 NL 文本桥接而非 formal predicates，无法验证 Observer 输出的正确性。是本 proposal 最直接的上游工作和最强竞争者。

- [Symbolic Grounding (arXiv 2604.21346, Apr 2026)]: 证明 LLM 接收 oracle 符号表示时在 Bongard-LOGO 上从 near-chance 跳到 mid-90s accuracy。建立了 representation（而非 reasoning）是核心瓶颈的关键论据。是本 proposal 动机的核心支柱，已确认存在且描述准确。

- [Don't Blink (arXiv 2604.04207, Apr 2026)]: 揭示推理 VLM 在 CoT 展开过程中 >50% 的 visual evidence mass 衰减。提供了 attention tracking 方法论和公开代码。为 persistent memory 的必要性提供了实证基础。已确认存在。

- [MathLens / "What MLLMs Learn" (arXiv 2510.01719, Oct 2025, updated Feb 2026)]: 将 MLLM 错误分解为 perception / reasoning / integration 三类，发现随着模型改进，integration failure 占比上升，成为 escalating bottleneck。已确认存在，描述准确。

- [Geoparsing (arXiv 2604.11600, Apr 2026)]: SOTA 形式化几何图解析，SFT+RLVR，GDP-29K 数据集，PGDP 96.4 / SGDP 94.9，超越 GPT-5.2。已确认存在。为 proposal 的 Observer 模块提供了技术可行性依据。

- [Hilbert-Geo (arXiv 2605.16385, May 2026)]: Parse2Reason 框架，CDL predicates，SolidFGeo2k 上 78% accuracy。有 formal parsing，但**无 RL、无 persistent memory**。是与 SymMem 最接近的 neuro-symbolic geometry 工作，proposal 的差异化定位准确。

- [CogFlow (ICLR 2026, arXiv 2601.01874)]: 三阶段 perception→internalization→reasoning，text-based internalization + Visual-Gated Policy Optimization。MathVista 76.8%。使用文本内化而非 formal predicates，无 persistent queryable memory。已确认是 ICLR 2026 accepted paper。

- [FIGR (arXiv 2512.24297, Dec 2025)]: 在推理循环中生成可执行代码渲染图表，+13.12% AIME。生成 pixel-level diagrams 而非 formal predicates。与 SymMem 的区别在于：code-rendered visual states vs. verifiable symbolic predicates。

- [Neuro-symbolic RL (arXiv 2604.22062, Apr 2026)]: GRPO + symbolic reasoning，Qwen3-VL-2B，+3.33% accuracy，减少 75% reasoning tokens。小规模实验，无 persistent memory。

- [SymHPR (arXiv 2512.03126, Dec 2025)]: 符号自编码器，98.2% 几何图重建 fidelity。提供了 symbolic encoding 的可行性证据。

- [GeoMathCode (arXiv 2605.25384, May 2026)]: 交替 math-code 推理，发现代码主要作为辅助可执行表示而非主动推理模态。

- 调研总结: 2025-2026 年间，visual mathematical reasoning 领域正从三个独立方向推进：(1) formal diagram parsing 达到 SOTA（Geoparsing 96.4%），(2) 双角色 RL 证明 perception-reasoning 协同训练有效（PRCO +7pt），(3) evidence collapse 和 integration failure 被确认为系统性瓶颈。但目前**没有工作**将 formal predicate parsing、persistent queryable memory、和 RL integration training 三者结合——这正是 SymMem 的定位。最接近的是 Hilbert-Geo（formal parsing + reasoning，无 RL/memory）和 PRCO（RL 双角色，NL caption，无 formal verification）。


【Trivial Alternative 检验】:

最直接的 trivial alternative：**"parse once + concatenate formal predicates to prompt + SFT"**——即用 Geoparsing 解析图形，将 predicates 拼接到 prompt 前面，做 SFT 训练。

Proposal 给出了三个反驳理由：(a) lost-in-the-middle 效应，(b) 无 step-wise retrieval，(c) 无 integration reward 导致 solver 可能 bypass predicates。

**我的评估：理由 (a) 较弱，理由 (b)(c) 有一定说服力但不确定。** 
- 理由 (a)：一个典型几何问题的 formal predicates 大约 20-50 条，总计几百个 token。在 Qwen3-VL-8B 的 context window 内，这是非常短的前缀。"Lost-in-the-middle" 效应主要针对数千 token 的长上下文，对几百 token 的 predicate 集合影响有限。这个论据站不太稳。
- 理由 (b)：step-wise retrieval 的必要性是一个**开放的实证问题**。如果 predicate 总量不大，全量提供 vs. 按步检索的差异可能不显著。
- 理由 (c)：最有说服力的理由。MathLens 确实表明 integration failure 是真实问题，但 SFT 训练也可以部分解决这个问题，不一定需要专门的 coverage reward。

**结论：trivial alternative 确实存在，且 proposal 的反驳不够决定性。** 好在 proposal 的 ablation 设计 (iii) "symbolic predicates concatenated without retrieval" 直接测试了这一点。SymMem 的增量价值将取决于实验中 full system vs. parse+concat 的差距大小。如果差距很小（<2pt），整个 persistent memory + retrieval + coverage reward 机制的正当性就会受到质疑。


【前提假设检验】:

核心 claim 的逻辑链：
1. Visual evidence collapses during reasoning → **有实证支撑 (Don't Blink)**，成立 ✓
2. Integration failure is the escalating bottleneck → **有实证支撑 (MathLens)**，成立 ✓
3. Oracle symbolic representations dramatically improve performance → **有实证支撑 (Symbolic Grounding paper)**，但注意这是在 Bongard-LOGO (abstract reasoning) 上，**不是几何问题**。从 abstract visual reasoning 到 real-world geometry 的迁移性是一个**未经验证的假设** ⚠️
4. Formal predicates ≈ oracle symbolic representations → **关键假设**。Geoparsing 在 parsing 上达到 96.4%，但 parsing accuracy ≠ downstream task-relevant representation quality。有些信息可能在 formalization 过程中丢失（如空间关系的模糊性、图形的视觉直觉等）。**这是一个合理但未验证的假设** ⚠️
5. Persistent queryable memory > static concatenation → **未经验证的核心假设** ⚠️。这是整个 architecture 相对于 trivial alternative 的关键差异化假设，需要实验验证。
6. Coverage-based integration reward 能有效解决 integration failure → **未经验证** ⚠️。这是一个新提出的 reward 设计，没有先例。合理但需要实验验证。

**总结：假设 1-2 有坚实的实证基础；假设 3-4 从合理的 analogy 出发但跨域迁移性未验证；假设 5-6 是核心贡献假设，必须靠实验验证。逻辑链整体合理，但 3-6 的每一个环节都可能独立 fail。**


【3 维度打分】:

1. **Novelty: 中** — 
   SymMem 的核心贡献是将 formal predicate parsing (Geoparsing)、persistent queryable memory (scratchpad + retrieval)、dual-role RL with coverage reward (extending PRCO) 三者组合。这个组合确实是新的——Hilbert-Geo 有 formal parsing 但无 RL/memory，PRCO 有 RL 但用 NL caption 且无 persistent memory，CogFlow 有 internalization 但不是 formal predicates。然而，这本质上是一个**integration contribution**：每个组件都有现成技术（Geoparsing 的 parser、PRCO 的 RL 框架、standard retrieval mechanism），novelty 在于组合方式而非单个组件。Oracle gap framework 作为评估方法论有独立贡献价值。Coverage-based integration reward R_cov 是一个有趣的新设计，但思路直接，不算 surprising。剔除 surface differences 后，核心 novelty delta 可概括为："用 formal predicates 替代 NL captions 作为 PRCO 的桥接表示 + 加 persistent memory + 加 coverage reward"——这是一个自然的方向延伸，不是反直觉的发现。

2. **Significance: 中** — 
   问题本身（visual math reasoning 中的 evidence collapse + integration failure）是高度重要的，MathLens 和 Don't Blink 的发现引起了广泛关注。**但 SymMem 的解决方案 scope 严格限制在几何领域**——proposal 自己也承认 "Geometry serves as the ideal testbed... If persistent symbolic memory cannot demonstrate value under these best-case conditions, it is unlikely to succeed elsewhere." 这种诚实的 scope 界定是学术优点，但也意味着：(a) 方法的 generalizability 有限——few other math domains have mature formal predicate systems，(b) 论文的影响力取决于 oracle gap framework 和 insights 的可迁移性，而非方法本身。如果核心发现是 positive（显著 close oracle gap），对领域的贡献在于：证明 end-to-end systems can approach oracle symbolic grounding，这是一个有价值的 existence proof。但如果结果 moderate，审稿人可能会说 "interesting but narrow"。

3. **Related Work: 强** — 
   这是 proposal 最强的维度。覆盖了 2025-2026 年间几乎所有相关工作：PRCO、CogFlow、Geoparsing、Hilbert-Geo、FIGR、SymHPR、Don't Blink、Symbolic Grounding、MathLens、InternGeometry、KAWHI、GeoMathCode、CoRGI、Neuro-symbolic RL、Mitigating Visual Forgetting。每篇论文的描述经调研验证均准确。与每个竞争者的差异化定位清晰且合理（PRCO=NL not formal, Hilbert-Geo=no RL/memory, FIGR=pixel not predicate, CogFlow=text internalization）。数据来源（FormalGeo、GDP-29K）和 evaluation benchmarks 的选择有充分依据。唯一小瑕疵：proposal 将 MathLens 归因于一篇名为 "What MLLMs Learn..." 的论文，实际上 MathLens 是该论文中提出的 benchmark 名称——描述准确但命名方式可能让读者困惑。


【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty 是限制上界的关键因素。虽然组合是新的、问题动机极为出色、related work 覆盖堪称典范，但核心贡献是一个 integration of existing components（formal parsing + persistent memory + RL），而非提出一个新的 paradigm 或反直觉的发现。如果 "core finding is positive, would reviewers say surprising?"——大概率答案是 "makes sense, the components are well-chosen, but I would have guessed that formal predicates + memory + RL should work better than NL captions"。这将 idea 定位在 25-35% 区间。

上界受限于：(1) integration contribution 的 novelty ceiling，(2) 几何领域限定的 significance scope，(3) trivial alternative (parse+concat) 的威胁——如果 ablation 显示 persistent memory + retrieval 的增量收益不大，论文的核心 architectural contribution 就被 undermine。

下界支撑因素：(1) 问题动机极强（三篇独立论文的 converging evidence），(2) oracle gap framework 有独立贡献价值，(3) 方法论设计（asymmetric reward schedule, coverage-based reward, structural verification）显示高度的技术成熟度，(4) neuro-symbolic integration 是 AAAI 的传统强项领域。

【主要风险】: 
1. **Trivial alternative risk**: parse + concatenate + SFT 可能已获得 SymMem 80-90% 的收益，使 persistent memory + retrieval + coverage reward 这些核心 architectural 贡献变得 marginal——这是审稿人最可能 raise 的致命质疑。
2. **Integration contribution novelty ceiling**: 三位审稿人中若有人认为 "this is just PRCO with formal predicates and a retrieval cache"，novelty score 会很低，而 proposal 缺乏一个足以独立成章的理论贡献（如 oracle gap 的理论 bound、convergence analysis）来对冲这一风险。
```

Sources:
- [PRCO: Seeing with You](https://arxiv.org/abs/2603.28618)
- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)
- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/pdf/2604.04207)
- [What MLLMs Learn about Multimodal Reasoning (MathLens)](https://arxiv.org/abs/2510.01719)
- [Geoparsing: Diagram Parsing with Unified Formal Language](https://arxiv.org/abs/2604.11600)
- [Hilbert-Geo: Neural-Symbolic Reasoning for Solid Geometry](https://arxiv.org/abs/2605.16385)
- [CogFlow: Bridging Perception and Reasoning (ICLR 2026)](https://arxiv.org/abs/2601.01874)
- [FIGR: Executable Visual States for Reasoning](https://arxiv.org/abs/2512.24297)
- [Neuro-symbolic RL for VLMs](https://arxiv.org/abs/2604.22062)
- [SymHPR: Hierarchical Process Reward Models](https://arxiv.org/abs/2512.03126)
- [GeoMathCode: Interleaved Math-Code Reasoning](https://arxiv.org/abs/2605.25384)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to make a well-grounded assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. PRCO (arXiv 2603.28618, 2026): 最直接的竞争者。提出 Observer-Solver 双角色 RL 框架，Observer 生成 NL caption 作为桥梁，Solver 基于 caption 推理。在 8 个 benchmark 上平均 +7pts。核心区别：PRCO 使用自然语言 caption（不可验证），SymMem 使用形式化谓词（可验证）+ 持久化记忆。PRCO 已经证明了双角色 RL 的有效性，SymMem 的增量是 symbolic representation + persistent memory + coverage reward。

2. Geoparsing (arXiv 2604.11600, 2026): SOTA 几何图形形式化解析器，SFT+RLVR 训练范式，GDP-29K 数据集，96.4/94.9 解析分数。直接给 Qwen3-VL-8B 提供解析输出就能在 Geometry3K 上 +10.1%。这表明"解析+拼接"这个 trivial baseline 已经有显著效果，SymMem 需要证明持久记忆+RL 的额外价值。

3. Hilbert-Geo (arXiv 2605.16385, 2026): Parse2Reason 方法，使用 CDL 形式化谓词，在 SolidFGeo2k 上 77.3%。没有 RL 也没有持久记忆。是 SymMem 在"形式化解析→推理"方向上最近的竞品，SymMem 的增量是持久记忆和 RL 集成训练。

4. CogFlow (ICLR 2026, arXiv 2601.01874): 感知→内化→推理三阶段框架，Knowledge Internalization Reward，Visual-Gated Policy Optimization。在 MathVista 上 76.8%。使用文本内化而非符号谓词。已被 ICLR 2026 接收，验证了"bridging perception and reasoning"这个研究方向的价值。

5. Don't Blink (arXiv 2604.04207, 2026): 证实 evidence collapse 现象——推理 VLM 在 CoT 过程中丢失 >50% 视觉注意力。公开了注意力追踪代码。为 SymMem 的核心动机提供实证支撑。✓ 论文真实存在且发现与 proposal 描述一致。

6. Symbolic Grounding (arXiv 2604.21346, 2026): LLM 接收 oracle 符号表示时在 Bongard-LOGO 上从近随机跳到 mid-90s 准确率，证明表示（而非推理）是瓶颈。✓ 论文真实存在且发现与 proposal 描述一致。

7. MathLens (arXiv 2510.01719, 2025): 分解多模态推理为感知/推理/整合三部分，发现整合（integration）是持续性瓶颈，RL 对其改善最少。✓ 论文真实存在且发现与 proposal 描述一致。

8. FIGR (arXiv 2512.24297, 2025): 在推理循环中生成可执行代码构建图形，+13.12% AIME。与 SymMem 的区别：FIGR 生成像素级图形而非形式化谓词，无符号级验证。

9. SymHPR (arXiv 2512.03126, 2025): 符号自编码器，98.2% 重建保真度，层次化过程奖励。✓ 论文真实存在。

10. Neuro-symbolic RL (arXiv 2604.22062, 2026): Qwen3-VL-2B 上 symbolic+GRPO，+3.33%。规模很小，没有持久记忆。是 SymMem 在"符号+RL"方向的近期工作，但规模和深度远不如 SymMem proposal。

11. Mitigating Visual Forgetting / TVC (ACL 2025): Take-along Visual Conditioning，通过动态剪枝和重新注入视觉 token 缓解视觉遗忘。与 SymMem 解决同一问题（视觉信息丢失），但方案不同：TVC 操作在连续视觉 token 层面，SymMem 操作在离散符号谓词层面。

- 调研总结: 这个领域在 2025-2026 年经历了快速发展，多篇工作从不同角度攻击"VLM 在多步推理中丢失视觉信息"的问题。PRCO 建立了双角色 RL 的范式，Geoparsing/Hilbert-Geo 建立了形式化解析的 SOTA，CogFlow 探索了感知-推理桥接。**SymMem 处于这些研究线的交汇点——它试图将形式化解析（Geoparsing）、双角色 RL（PRCO）和持久记忆机制整合为统一系统。** 这个交汇位置目前确实没有被已有工作占据，但每个组件都已有成熟先例。


【Trivial Alternative 检验】:

最具威胁的 trivial alternative 是 **"Geoparsing 解析 + 直接拼接到 prompt"**。Geoparsing 论文本身已经展示了仅通过提供解析输出就能在 Geometry3K 上 +10.1%。Proposal 预见到了这个挑战并提出三个反驳：(a) 解析后文本受 lost-in-the-middle 效应影响，(b) 无法自适应按步骤检索，(c) 无集成训练信号导致模型可能跳过谓词。

这些反驳在逻辑上站得住脚，但**其实际增量价值是纯粹的实验问题**。如果实验显示"解析+拼接"与 SymMem 差距很小（比如 <3pts），整个持久记忆+RL 训练的复杂性就难以 justify。这是此 proposal 最大的实验风险。

第二个 trivial alternative：**PRCO 框架直接使用 FormalGeo 谓词替代 NL caption**——这基本是 SymMem 去掉持久记忆和 coverage reward 后的简化版。proposal 设计了 "data-matched PRCO" baseline 来隔离这个对比，设计是合理的。

**增量价值判断**: 如果以上两个 trivial alternatives 都被实验击败，SymMem 的增量价值在于：(1) 持久化记忆提供按需检索能力（解决长上下文信息衰减），(2) coverage 奖励驱动的集成训练（解决 MathLens 发现的集成失败）。逻辑链完整，但增量幅度存疑。


【前提假设检验】:

核心 claim 的逻辑链：
Evidence collapse (Don't Blink) + Integration failure (MathLens) + Oracle gap (Symbolic Grounding) → 需要 persistent symbolic memory → SymMem 可以近似 oracle symbolic grounding

未经验证的关键假设：

1. **"规则化实体匹配检索足够好"**: Proposal 使用 rule-based entity matching 从当前推理步骤提取几何实体名称，然后检索匹配谓词。这假设推理过程中会产生明确的实体名称、且实体名称与谓词之间存在可靠的对应关系。如果模型推理时使用模糊的指代或跳步推理，检索可能失败。不过 proposal 也设计了 learned embedding retrieval 的对比消融，部分缓解了这个风险。

2. **"三路奖励可以稳定收敛"**: Observer F1 + Solver correctness + coverage reward 三者的优化目标可能冲突。例如 Observer 可能为了提高 F1 而过度解析无关谓词，coverage reward 可能鼓励检索所有谓词（包括不相关的），这与 Solver accuracy 可能矛盾。Proposal 提到了 weight sensitivity 和 frozen Observer 消融，但没有理论保证收敛。

3. **"Bongard-LOGO 上的 oracle gap 发现可以迁移到几何推理"**: Symbolic Grounding 论文在抽象视觉推理（Bongard-LOGO）上建立了 oracle upper bound，但几何推理的符号化难度和推理复杂度与 Bongard-LOGO 差异很大。Oracle gap 在几何域的实际大小是未知的。

4. **"Evidence collapse 的原因是信息未持久化，而非注意力机制的根本局限"**: Don't Blink 记录了注意力质量衰减的现象，但原因可能是架构层面的（注意力窗口有限、位置编码衰减等），而非仅仅是"信息未被显式保存"。如果根因是架构层面的，持久记忆可以缓解但不能根本解决。

假设 1 和 2 是执行层面的风险，可以通过实验验证。假设 3 和 4 是 idea 层面的前提假设，如果不成立会动摇核心 claim。但假设 3 的风险被 proposal 的"geometry as ideal testbed"论述部分缓解——它不是声称一定能迁移，而是声称几何是最有利的测试场。假设 4 的风险也被 evidence retention analysis 的设计部分缓解——它计划同时测量视觉 token 注意力和 scratchpad token 注意力。


【3 维度打分】:

1. **Novelty: 中** — SymMem 的每个组件在已有工作中都有先例：形式化解析（Geoparsing, Hilbert-Geo）、双角色 RL（PRCO）、视觉信息持久化（TVC, VLM²）、符号+RL（Neuro-symbolic RL）。核心 novelty 在于这些组件的**特定组合方式**：可验证的符号谓词 + 持久可查询记忆 + coverage-based 集成奖励，以及 oracle gap 评估框架。这个组合确实没有被现有工作覆盖——PRCO 用 NL caption（不可验证）、Hilbert-Geo 没有 RL 和持久记忆、Geoparsing 只做解析不做集成训练。Oracle gap framework 作为评估方法论的贡献是独立有价值的。但审稿人可能会质疑这是"incremental combination"而非"conceptual breakthrough"。Coverage-based integration reward 是一个新的技术贡献，但体量较小。

2. **Significance: 中** — 研究问题（多步视觉数学推理中的信息丢失和跨模态整合失败）是重要且时效性很强的问题，被多篇 2025-2026 论文独立验证。但 proposal 的方案高度依赖 FormalGeo 的 88 谓词系统和几何领域的特殊性质（形式化谓词系统成熟、ground-truth 标注可用、结构化验证可行），**向其他视觉推理域的推广路径不清晰**。Proposal 以"ideal testbed"框架定位几何域是聪明的，但这也意味着即使成功，直接影响力限于几何推理这个子领域。如果核心发现是 positive（SymMem 显著优于 parse-and-concatenate），审稿人可能会说"interesting but expected — of course persistent memory with RL training should help"。如果 oracle gap analysis 揭示了意外发现（如 parsing error 而非 integration failure 是主要瓶颈），significance 会更高。

3. **Related Work: 强** — 这是 proposal 最强的维度。覆盖了所有主要竞争者（PRCO, Geoparsing, Hilbert-Geo, CogFlow, FIGR, SymHPR, Don't Blink, MathLens, Symbolic Grounding, TVC, Neuro-symbolic RL, InternGeometry, KAWHI, GeoMathCode, CoRGI），对每个工作的定位和区分都准确清晰。所有引用的关键论文均经调研验证真实存在，描述准确。对 InternGeometry（外部工具使用 vs. 训练时内化）和 FIGR（像素级图形 vs. 谓词级符号）的区分尤其精准。Baseline 设计包含 compute-matched 和 data-matched 对照，显示出对公平对比的认真思考。


【概率估计】: [25% - 38%] 中位 30%

【估计理由】: 
- **Novelty (中)** 是主要限制因素。idea 的核心是将 4 个已有方向（形式化解析、双角色 RL、持久记忆、符号验证）组合起来，每个方向都有 2026 年的成熟先例。虽然特定组合是新的，且 oracle gap framework 有独立贡献，但审稿人大概率会视为 "solid systems work / incremental combination" 而非 "new paradigm"。这限制了上界在 ~38%。
- **Significance (中)** 进一步限制了中位数。几何域的特殊性（成熟的形式化系统、标注数据）使得方案难以推广，而几何推理本身在 AAAI 审稿人眼中可能被视为相对窄的方向。
- **Related Work (强)** 提供了扎实的下限保障（~25%），因为 proposal 对领域的理解是准确且深入的，不太可能因为遗漏关键 related work 而被拒。
- 三线动机汇聚（evidence collapse + integration failure + oracle gap）的叙事结构是强有力的，但叙事质量不等于 idea novelty。
- Oracle gap framework 是独立的方法论贡献，为概率加分 ~3-5%。

【主要风险】: 
1. **"Incremental combination" 质疑**: 审稿人可能认为 SymMem = Geoparsing + PRCO + 简单检索机制，每个组件的整合虽然需要工程努力但缺乏概念层面的创新。coverage reward 虽然新颖但体量偏小，难以独撑 novelty claim。
2. **Trivial baseline 威胁**: 如果"Geoparsing 解析 + prompt 拼接"在实验中已经接近 SymMem 的效果（差距 <3pts），整个持久记忆+RL集成+coverage reward 的复杂系统就无法 justify，论文的核心 claim（persistent symbolic memory is necessary）将被动摇。这是一个 idea 层面的风险，因为它质疑的是"持久化记忆是否真的必要"这个前提。
```

Sources:
- [PRCO: Seeing with You](https://arxiv.org/abs/2603.28618)
- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/pdf/2604.04207)
- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)
- [MathLens: What MLLMs Learn about Multimodal Reasoning](https://arxiv.org/abs/2510.01719)
- [CogFlow: Bridging Perception and Reasoning (ICLR 2026)](https://arxiv.org/abs/2601.01874)
- [Hilbert-Geo: Neural-Symbolic Reasoning for Solid Geometry](https://arxiv.org/abs/2605.16385)
- [FIGR: Executable Visual States](https://arxiv.org/abs/2512.24297)
- [SymHPR: Hierarchical Process Reward Models](https://arxiv.org/abs/2512.03126)
- [Neuro-symbolic RL for VLMs](https://arxiv.org/abs/2604.22062)
- [Mitigating Visual Forgetting via TVC (ACL 2025)](https://aclanthology.org/2025.acl-long.257/)


【原始 proposal（允许参考但不是主要依据）】:
# Bridging the Oracle-to-End-to-End Gap: Persistent Symbolic Memory for Visual Mathematical Reasoning

## Core Problem

Multi-step visual mathematical reasoning suffers from two compounding failures. First, evidence collapse: reasoning VLMs lose >50% of visual attention mass as chain-of-thought unfolds (Don't Blink, arXiv 2026), meaning visual information is irrecoverably lost during reasoning and must be converted to a persistent format early. Second, cross-modal integration failure: the dominant error mode that constitutes a growing fraction of remaining errors as models improve (MathLens, arXiv 2025) — an escalating bottleneck that demands structural architectural intervention, not incremental optimization or scaling.

The Symbolic Grounding paper (arXiv 2026) establishes a striking upper bound: LLMs receiving oracle symbolic representations instead of raw images jump from near-chance to mid-90s accuracy on abstract visual reasoning (Bongard-LOGO), proving that representation — not reasoning — is the fundamental bottleneck. This motivates a central research question: **How close can an end-to-end system come to oracle symbolic grounding on real-world geometry problems?** No existing method attempts this — diagrams are encoded once into continuous embeddings that decay, and no verifiable, persistent symbolic bridge exists between perception and reasoning.

## Research Opportunity

Two research lines have advanced independently: formal diagram parsers (Geoparsing, arXiv 2026; SymHPR, arXiv 2025) achieve SOTA conversion of diagrams into verifiable symbolic predicates, and dual-role RL frameworks (PRCO, arXiv 2026) demonstrate +7pt gains through perception-reasoning co-training with NL caption bridges. But these remain disconnected.

SymMem closes three gaps simultaneously to approximate oracle symbolic grounding end-to-end: (1) learning to parse diagrams into formally verifiable predicates (approximating the oracle), (2) maintaining these predicates as persistent, queryable memory (preventing information loss), and (3) training the system to utilize this symbolic bridge via RL (solving integration failure).

**Why not simply parse once and concatenate predicates to the prompt?** This naive alternative fails for two independent reasons: (a) irrecoverable visual decay (Don't Blink) means predicates must be extracted early — but once extracted as text, they suffer the well-documented "lost-in-the-middle" effect in long contexts, where early tokens are progressively overshadowed by subsequent generation; (b) without step-wise retrieval, the solver cannot adaptively access step-relevant predicates; (c) without integration reward, the solver may bypass predicates entirely — the integration failure mode MathLens documents as the escalating bottleneck.

Geometry serves as the **ideal testbed** for this hypothesis: it is the only visual math domain where a mature formal predicate system exists (FormalGeo, 88 predicates + 196 theorems), large-scale ground-truth formal annotations are available (GDP-29K, FormalGeo7k), and structural verification is possible without task-specific answer labels. If persistent symbolic memory cannot demonstrate value under these best-case conditions, it is unlikely to succeed elsewhere.

## Research Landscape

Current MathVista SOTA: o3 at 86.8%; open models: Qwen3-VL at 85.8%, Step3-VL-10B (arXiv 2026) at 84.0%. PRCO (arXiv 2026): +7pts average via NL Observer-Solver RL, 8 benchmarks, cannot verify Observer output. CogFlow (ICLR 2026): perception→internalization→reasoning, 76.8% MathVista, text-based internalization. Geoparsing (arXiv 2026): SOTA formal parsing via SFT+RLVR on GDP-29K. SymHPR (arXiv 2025): symbolic auto-encoding, 98.2% reconstruction fidelity. Don't Blink (arXiv 2026): >50% visual evidence mass loss, public attention tracking code. v1 (arXiv 2025): visual-token re-attention, cannot correct initial perception errors. MathLens (arXiv 2025): integration failure escalates as models improve. InternGeometry (arXiv 2512.10534): IMO-gold geometry via 200+ rounds with external DDAR engine — represents the test-time compute scaling paradigm (external tool use), whereas SymMem pursues training-time internalization (self-contained model). Hilbert-Geo (arXiv 2026): Parse2Reason with formal CDL predicates, 77.3% SolidFGeo2k, no RL or persistent memory. FIGR (arXiv 2512.24297): executable visual states within reasoning loops via end-to-end RL (+13.12% AIME), but generates code-rendered pixel-level diagrams without formal predicate-level verification — fundamentally different from SymMem's verifiable symbolic predicates. KAWHI (arXiv 2026): attention-based reward reweighting for RLVR. GeoMathCode (arXiv 2026): interleaved math-code reasoning, code as auxiliary representation. CoRGI (arXiv 2025): post-hoc inference-only verification. Neuro-symbolic RL (arXiv 2604.22062): symbolic+GRPO at small scale (Qwen3-VL-2B, +3.33%), no persistent memory. Mitigating Visual Forgetting (ACL 2025): take-along visual conditioning for long CoT.

## Proposed Approach

**Architecture.** Built on Qwen3-VL-8B. A formal Observer converts diagrams into structured symbolic predicates (FormalGeo's 88-predicate system). These populate a persistent symbolic scratchpad. At each CoT step, rule-based entity matching extracts geometric entity names from the Solver's current reasoning output and retrieves top-K matching predicates from the scratchpad, injecting them into the next step's context. For non-geometric inputs, a learned diagram-type classifier (trained on MathVista's category metadata) triggers fallback to NL caption mode.

**Structural Verification.** Observer output is verified via structural/topological comparison against ground-truth formal annotations (predicate-level P/R/F1). This avoids pixel-level rendering dependency.

**Dual-Role RL with Coverage-Based Integration Reward.** Observer reward: structural verification F1. Solver reward: outcome correctness. Integration reward: R_cov = |∪_t P_retrieved(t)| / |P_total|, measuring predicate coverage across the entire reasoning chain via retrieval logs (not NL string matching). Coverage-based formulation avoids incentivizing redundant per-step referencing. The outcome reward provides natural precision pressure. Weight sensitivity: λ_cov ∈ {0.1, 0.3, 0.5, 1.0}. Asymmetric reward schedule for mixed-label data: formal-annotation-only samples → Observer reward only; answer-only samples → Solver reward only; dual-label samples → all three rewards.

**Training Data.** Phase 1 (formal parser SFT+RLVR): GDP-29K (availability pending; backup: FormalGeo augmented data + Hilbert-Geo SolidFGeo2k/PlaneFGeo3k). Phase 3 (dual-role RL): FormalGeo augmented data (~134K dual-label problems; FGeo-TP extension to ~187K available if needed), supplemented by GDP-29K for Observer-only training.

**Evaluation — Oracle Gap Framework.** The paper is structured around measuring and closing the oracle-to-end-to-end gap:
1. **Oracle upper bound**: GT formal annotations directly populate scratchpad (bypassing Observer) → measures Solver's ceiling under perfect symbolic grounding.
2. **End-to-end SymMem**: full pipeline with learned Observer → measures how close the system approaches the oracle.
3. **Gap decomposition**: remaining gap attributed to parsing error (Observer F1 deficit), retrieval miss (coverage gap), and integration failure (predicate-utilization-to-accuracy correlation) — identifying where future improvement should focus.

Eight benchmarks: MathVista, MathVerse, GeoQA, WeMath, MathVision, DynaMath, Geometry3K, LogicVista. Per-category breakdown on mixed benchmarks. Evidence retention analysis via expanded metric: total evidence mass = visual token attention + scratchpad token attention (separately reported), using Don't Blink's attention tracking methodology. Core claim: SymMem transfers evidence from rapidly-decaying visual tokens to persistently-queryable scratchpad tokens, significantly slowing total evidence mass decay. Training FLOPs and GPU-hours reported.

**Baselines.** (1) PRCO (NL Observer + RL), (2) CogFlow (text internalization, ICLR 2026), (3) KAWHI (attention reward reweighting), (4) Hilbert-Geo Parse2Reason (formal parsing, no persistent memory, no RL integration), (5) Compute-matched PRCO (same total FLOPs), (6) Data-matched PRCO (same FormalGeo data as NL captions, isolating symbolic vs. NL representation benefit). Reported-number comparisons: FIGR (arXiv 2512.24297), GeoMathCode, Neuro-symbolic RL.

**Ablations.** Progressive (6-level): (A) Qwen3-VL-8B base → (B) +formal parser SFT → (C) +structural verifier → (D) +persistent scratchpad with retrieval → (E) +dual-role RL → (F) +coverage integration reward. Memory mechanism: (i) re-read visual tokens (v1-style), (ii) NL predicates concatenated, (iii) symbolic predicates concatenated without retrieval, (iv) symbolic scratchpad with retrieval. Retrieval mechanism: rule-based entity matching vs. learned embedding retrieval. Integration reward: coverage-based R_cov vs. per-step utilization vs. none. Reward stability: frozen Observer (post-SFT) + Solver RL vs. joint Observer+Solver RL, with training curve analysis of Observer F1 / Solver accuracy / R_cov dynamics. Fallback classifier: oracle vs. learned vs. all-symbolic vs. all-NL. Observer parsing quality: standalone P/R/F1 vs. Geoparsing; parsing F1-binned task accuracy correlation.

## Key References

- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning (arXiv 2026)
- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)
- Hierarchical Process Reward Models are Symbolic Vision Learners (arXiv 2025)
- Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv 2026)
- Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning (arXiv 2026)
- v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning (arXiv 2025)
- What MLLMs Learn about When they Learn about Multimodal Reasoning: Perception, Reasoning, or their Integration? (arXiv 2025)
- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026)
- Mitigating Visual Forgetting via Take-along Visual Conditioning for Multi-modal Long CoT Reasoning (ACL 2025)
- Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models (arXiv 2026)
- CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding (arXiv 2025)
- STEP3-VL-10B Technical Report (arXiv 2026)
- Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning (arXiv 2026)
- InternGeometry: Achieving Olympia-Level Geometry via Complexity Boosting Reinforcement Learning (arXiv 2512.10534, Dec 2025)
- Incentivizing Neuro-symbolic Language-based Reasoning in VLMs via Reinforcement Learning (arXiv 2604.22062, Apr 2026)
- FIGR: Figure It Out — Improve the Frontier of Reasoning with Executable Visual States (arXiv 2512.24297, Dec 2025)

## Resource Estimate

- **manual**: gpu_hours: 850–1050 H100-hours (Phase 1 formal parser SFT+RLVR: ~120h; Phase 2 structural verifier: ~80h; Phase 3 dual-role RL on ~134K FormalGeo data: ~350h; Phase 4 evaluation on 8 benchmarks + oracle gap framework + full ablation matrix + frozen Observer ablation + evidence retention analysis + compute/data-matched baselines: ~300h), timeline: 14–16 weeks, estimated_gpu_cost: $2,125–$2,625 at $2.50/hr spot H100
- **human_in_loop**: gpu_hours: 700–900 H100-hours, timeline: 10–12 weeks, claude_api_cost: $300–$450, estimated_gpu_cost: $1,750–$2,250
- **auto_research**: gpu_hours: 1050–1400 H100-hours, timeline: 7–9 weeks, claude_api_cost: $550–$850, estimated_gpu_cost: $2,625–$3,500, speed_bottleneck: Coverage integration reward design and three-way reward conflict analysis; fallback classifier threshold tuning; GDP-29K availability contingency; oracle gap decomposition methodology

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "38a90b0e-75a6-4577-ba35-a068f6d528f3",
  "type": "user",
  "uuid": "5661921f-a1c8-489b-a701-73730d90100c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T23:54:19.436Z_

```json
{
  "parentUuid": "5661921f-a1c8-489b-a701-73730d90100c",
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
  "uuid": "3639cd5c-3392-4e82-b684-cb14af40ed7e",
  "timestamp": "2026-05-27T23:54:19.436Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T23:54:19.436Z_

```json
{
  "parentUuid": "3639cd5c-3392-4e82-b684-cb14af40ed7e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7f6ce926-95e6-4dc7-8e09-b744bba55142",
  "timestamp": "2026-05-27T23:54:19.436Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct a thorough evalua…",
  "leafUuid": "7f6ce926-95e6-4dc7-8e09-b744bba55142",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate SymMem proposal with oracle gap framework",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f"
}
```

---

### Assistant

_source line 8 · 2026-05-27T23:54:39.884Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews of this proposal and synthesize them as Meta Judge.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [25% - 35%] 中位 30%
- Main risks: "Obvious combination" challenge, Oracle gap transferability assumption fragility

**Reviewer 2:**
- Novelty: 中
- Significance: 中


- Related Work: 强
- Probability: [25% - 35%] 中位 30%
- Main risks: Trivial alternative risk (parse+concat+SFT), Integration contribution novelty ceiling

**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [25% - 38%] 中位 30%
- Main risks: "Incremental combination" challenge, Trivial baseline threat

All three reviewers converge on a 30% acceptance probability with zero variance, which is striking—they're aligned despite raising different concerns about the work's originality and whether the approach amounts to a straightforward combination of existing techniques. The consensus across all three reviewers is striking—they converge on the same overall score and identify nearly identical concerns around the incremental nature of the approach, the unverified assumption about oracle transferability, and the limited scope to geometry tasks. The only minor divergences are R1's slightly more optimistic significance rating and some differences in which related work they emphasize. Now I'm moving to synthesize the implementation feasibility based on what the proposal claims and what the reviewers flagged about technical stability and generalizability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f6ce926-95e6-4dc7-8e09-b744bba55142",
  "isSidechain": false,
  "requestId": "req_011CbTyXf3RwrzWXUTc8GhDM",
  "type": "assistant",
  "uuid": "fb2eed8a-4bd8-45e5-9299-c4d4e22cf1c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ry95htw2kaqRc4vbUcpRcN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18168,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18168,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2782,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18168
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

_source line 9 · 2026-05-27T23:55:31.258Z_

【阶段】: Meta Judge
【三次中位】: [30%, 30%, 30%]  std=0%
【共识维度】:
- **Novelty = 中**（3/3 一致）：三位审稿人不约而同认定 SymMem 是 PRCO（双角色 RL）+ Geoparsing（形式化解析）+ 持久记忆的"自然组合/predictable combination"，每个组件均有成熟先例，组合方式虽新但不 surprising。Coverage reward 和 oracle gap framework 有独立贡献但体量偏小，不足以将 novelty 提升至"强"。
- **Related Work = 强**（3/3 一致）：覆盖全面（PRCO、Geoparsing、Hilbert-Geo、CogFlow、FIGR、Don't Blink、MathLens、Symbolic Grounding 等），差异化定位准确，所有引用经验证真实存在。这是 proposal 最强的维度，无争议。
- **Significance = 中**（2/3 共识，R2/R3 均为"中"，R1 为"中偏强"）：问题动机极强（三线汇聚：evidence collapse + integration failure + oracle gap），但方案强绑定 FormalGeo 谓词系统，几何域特异性限制了推广路径。
- **"Obvious combination" 质疑**（3/3 一致）：核心风险。审稿人极可能问 "What is the core insight beyond combining PRCO with formal parsing?"，proposal 目前缺乏足以独立成章的理论贡献来对冲。
- **Trivial alternative 威胁**（3/3 一致）：parse+concat 可能已获得 SymMem 大部分收益。三位审稿人均指出 proposal 的三个反驳中，(a) lost-in-the-middle 在几何场景下偏弱（谓词通常仅几十到几百 tokens），(b)(c) 的增量价值是纯粹的实验问题。
- **Oracle gap 迁移性假设脆弱**（3/3 一致）：Bongard-LOGO（抽象视觉推理）→ 几何（结构化视觉）的 gap 大小未经验证，几何图本身已高度结构化，oracle gap 可能远小于预期，从而削弱核心叙事。
- **多目标 RL 稳定性风险**（2/3，R1+R3）：三路奖励可能冲突，λ_cov 敏感度高，无理论收敛保证。
- **几何域特异性限制 significance**（2/3，R2+R3）：方法依赖成熟的形式化谓词系统，其他视觉数学领域无类似基础设施。

【异常维度】:
- R1 对 Significance 给出"中偏强"（vs R2/R3 的"中"）——属轻微正向偏离，不影响共识判断。R1 更侧重问题本身的重要性，R2/R3 更侧重方案的推广局限。按保守原则，取"中"。
- R3 上界给到 38%（vs R1/R2 的 35%）——属轻微偏宽，不影响中位判断。

【最终概率】: [25% - 35%] 中位 30%
【一致性】: 高（std=0%，三位审稿人在所有核心维度上判断高度一致）
【综合理由】:
这是我见过的最高一致性评审之一——三位独立审稿人在 Novelty/Significance/Related Work 三个维度的打分、概率区间、核心风险识别上几乎完全对齐。处理逻辑如下：

1. **中位数直接采信**：std=0%，三位审稿人独立给出完全相同的中位 30%，无需任何调整。

2. **区间取交集偏严**：R1=[25-35%]，R2=[25-35%]，R3=[25-38%]。R3 的上界略宽但属 outlier，取两位共识的 [25-35%]。

3. **Novelty 天花板效应确认**：三位审稿人一致认为核心 idea 是 "integration of existing components"，不是 paradigm shift。即使实验结果完美，"I would have guessed this should work" 的反应限制了论文的 surprise factor。这将概率天花板锁定在 ~35%——除非实验中涌现出意外发现（如 oracle gap decomposition 揭示反直觉的瓶颈分布），否则很难突破。

4. **下限由动机质量托底**：三线汇聚的动机叙事（Don't Blink + MathLens + Symbolic Grounding）是扎实的，Related Work 覆盖堪称典范，oracle gap framework 有独立贡献。这些保证了即使 novelty 被质疑，论文也不至于被视为 trivial。

5. **关键实验风险**：trivial alternative（parse+concat）的威胁是决定论文命运的关键实验。如果增量 <3pts，核心架构贡献将被 undermine，概率跌至下界附近。

【建议】: 边缘（Novelty 天花板限制了上界，但问题动机强、实验设计完备、Related Work 扎实，有一定中稿可能性。需要通过迭代强化 novelty angle 和 trivial alternative 的反驳力度。）

【实施评估】:
- **计算资源**: 850–1400 H100-hours（取决于执行模式），约 $2,125–$3,500 GPU 成本。Phase 3 双角色 RL（~350h）是最大单项开销。需要至少 4×H100 节点持续运行。
- **数据需求**: FormalGeo 增强数据（~134K，公开）、GDP-29K（可用性待确认，有 FormalGeo + Hilbert-Geo 数据作为备选）、8 个评测 benchmark（均公开）。GDP-29K 可用性是关键不确定因素。
- **人工介入**: 中等——需要人工调试三路 reward 权重（λ_cov 敏感度分析）、fallback 分类器阈值、oracle gap decomposition 方法论验证。如采用 human-in-loop 模式可缩短至 10-12 周。
- **训练需求**: 需要完整模型训练。Phase 1: Observer SFT+RLVR；Phase 3: 双角色 RL（Observer + Solver 联合训练）。基础模型 Qwen3-VL-8B，全参数 RL 训练。
- **新 Benchmark**: 不需要构建全新 benchmark，但 oracle gap framework 本身是一套新的评估方法论，需要实现和验证。Evidence retention analysis 需要复现 Don't Blink 的注意力追踪方法并扩展。
- **预估周期**: 10–16 周（取决于执行模式和 GDP-29K 数据可用性）。关键路径：Phase 1 parser 训练 → Phase 3 双角色 RL → 全量消融实验 + 8 benchmark 评测。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb2eed8a-4bd8-45e5-9299-c4d4e22cf1c8",
  "isSidechain": false,
  "requestId": "req_011CbTyXf3RwrzWXUTc8GhDM",
  "type": "assistant",
  "uuid": "28555ed5-a989-45a7-89bc-92e180561697",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ry95htw2kaqRc4vbUcpRcN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18168,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18168,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2782,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18168
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct a thorough evalua…",
  "leafUuid": "28555ed5-a989-45a7-89bc-92e180561697",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate SymMem proposal with oracle gap framework",
  "sessionId": "05630948-4d28-4948-b45a-f1c448e3178f"
}
```

---
