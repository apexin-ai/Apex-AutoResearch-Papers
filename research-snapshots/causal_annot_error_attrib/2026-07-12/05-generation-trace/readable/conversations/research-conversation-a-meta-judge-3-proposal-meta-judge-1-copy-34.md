# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/0a60b288-4ced-4f7c-beaf-00a80a176b11.jsonl`
- **Structured JSON:** [`1547188f09e536f5813d.json`](../../sessions/15/1547188f09e536f5813d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T01:54:30.161Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T01:54:30.161Z",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have enough information to make my assessment. Let me synthesize everything.\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】: \n存在严重的 trivial alternative 威胁。\n\n(1) **单 GRU + 特征拼接**：将三类信号在每步直接拼接（dim ~85-165），输入一个 GRU，末尾接分类头。如果三类信号确实互补，这种最简单的方法同样能隐式学到时变的特征重要性——不需要三个独立编码器 + 显式 gating MLP。Proposal 辩称 gating 提供\"可解释性\"，但 gradient attribution / SHAP / attention rollout 等 post-hoc 方法同样可以对单 GRU 做特征归因，代价远低于专门设计 gating 架构。因此 gating network 的增量价值很大程度局限于\"更直接的可解释性\"——这是一个 nice-to-have，但不构成核心方法论贡献。\n\n(2) **Multi-horizon loss 独立于 fusion 架构**：multi-horizon early-detection loss（在不同 observation fraction 上计算 BCE 加权和）是一个通用训练技巧，可以直接施加于任何已有单信号检测器（如 HALT、EigenTrack）。如果单信号 + multi-horizon loss 就已经大幅提升早期检测性能，那 fusion 的增量价值将更加微弱。这一分离性意味着 proposal 的两个\"Novel Component\"实际上是独立的，而非协同的。\n\n增量价值在哪：如果 fusion 的增量 AUROC gain 在统计上显著且实质性（>2-3 pp），且 temporal gate weights 揭示了**反直觉的**信号动态（而非 proposal 自身机制论证所预测的\"attention 先变化 → hidden states 中间 → log-probs 最后\"），则有增量价值。但 proposal 自己的理论论证恰恰预测了最可能出现的结果模式——这使得发现大概率是 confirmatory 而非 surprising。\n\n【前提假设检验】: \n核心 claim 的逻辑链条中有两个关键未验证假设：\n\n(1) **\"三类信号具有时间互补性\"（temporal complementarity）**：Proposal 的机制论证是——attention 做 routing (WHERE)，hidden states 做 computation (WHAT)，log-probs 做 confidence (HOW)，因为它们在 transformer pipeline 中的位置不同，所以应该在不同的生成阶段携带互补的幻觉信号。但这个论证混淆了**步内（intra-step）**和**步间（inter-step）**的时间尺度。在每个 decoding step 内，attention → FFN → output 确实是顺序的；但 TemporalFuse 的 GRU 跨越的是 generation steps（不同 token 的生成时刻），在这个时间尺度上，所有三类信号都是同一个自回归过程的产物，可能高度相关。Proposal 承认了这个风险（pilot 中 Pearson r > 0.95 → pivot），但没有提供任何先验证据支持互补性假设。它引用的 \"Hallucination as Trajectory Commitment\" 和 \"Shadows in the Attention\" 显示 hidden states 和 attention 有不同的时间 profile，但这些观察是在不同实验设置下得出的，直接外推到 TruthfulQA + Llama-3.1-8B 设置并不可靠。\n\n(2) **\"静态比较的分歧是因为忽略了时间动态\"**：Proposal 将 HALUPROBE（attention 最优）与 krogoldAI（FFN 最优）的分歧归因于\"static snapshots collapse temporal dynamics\"。但更 parsimonious 的解释是——不同的模型（Llama-2-7B vs Ministral-8B）、不同的数据集、不同的特征工程、不同的分类器导致了不同的结论。Temporal dynamics 作为解释是一个合理的假设，但被呈现得过于肯定，似乎是 proposal 设计的 motivation 而非客观分析的结论。如果真实原因是 model/dataset/feature 差异而非 temporal collapse，那么 TemporalFuse 的\"resolving the conflict\"叙事就不成立。\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — \n   核心方法论贡献（parallel GRU encoders + gating MLP + multi-horizon loss）在时间序列和多模态融合文献中是非常标准的架构。192→64→3 softmax gating 是教科书级 mixture-of-experts gate；multi-horizon loss 是 early time series classification 文献的直接搬用。Novelty 主要来自**应用领域的首次性**——第一个在 LLM 幻觉检测中做 temporal multi-signal fusion + early detection optimization。这种\"first to apply X to Y\"在 EMNLP 主会的 novelty 标准下通常不够强，除非应用本身揭示了领域特有的、非平凡的洞察。SpectralTrack 对 INSIDE/EigenScore 的扩展是工程改进而非概念突破。\"Temporal signal importance map\"是 gating 架构的自然副产品，不构成独立贡献。\n\n2. **Significance: 中** — \n   研究问题（实时幻觉检测中的多信号融合与早期检测）具有实际重要性，practitioners 确实面临\"选哪个信号\"和\"何时能可靠检测\"的问题。但存在两个 significance 限制：(a) 如果核心发现是 positive（fusion 优于 individual signals，early detection 可行），这对多数审稿人来说是符合预期的——\"更多信息 = 更好的检测\"是 common sense。审稿人更可能说 \"I would have guessed this\" 而非 \"surprising\"；(b) EMNLP short paper 版本只有 1 model × 1 benchmark × 1K examples，generalizability 存疑。Temporal gate weight 分析的发现空间窄：如果 pattern 符合机制论证的预测（attention 先 → hidden states 中 → log-probs 后），则 confirmatory 而非 insightful；如果 pattern 不符合预测，则需要更多模型/数据来确认不是 artifact。\n\n3. **Related Work: 强** — \n   覆盖面非常全面。涵盖了静态信号比较（HALUPROBE, Proxy Analyzers, krogoldAI, LLM-Check）、多信号融合（HaDeMiF, HaluNet, CHARM, ReDeEP）、单信号时序（EigenTrack, HALT, HSAD, ICR Probe）、基础工作（INSIDE/EigenScore）、流式检测（Streaming Hallucination Detection）、级联系统（HaluGate, HALL-OPT）、跨领域融合先例（MFGAN, DSAC）。差异化定位清晰：逐一与已有方法区分（static vs temporal, single vs multi-signal, complete vs early detection）。这是 proposal 最强的维度。唯一微小的遗漏是对\"early time series classification\"具体方法（如 TEASER, ECONOMY, CALIMERA 等）的引用不够具体，但这不影响整体评价。\n\n【概率估计】: [18% - 30%] 中位 23%\n（注：此估计针对 EMNLP 2026 主会 main track short paper；若含 Findings，上调至 [30% - 42%] 中位 35%）\n\n【估计理由】: \nRelated Work 维度强，但不影响中稿概率的上界——好的文献综述只是 table stakes。概率上界被 **Novelty** 限制：核心方法是标准时序融合架构在新领域的首次应用，EMNLP 主会审稿人对 \"first to apply X to Y\" 类贡献通常要求发现本身有 surprising insight，而本 proposal 的理论论证恰恰预测了最可能出现的实验结果模式，使得 \"surprising finding\" 的概率较低。概率下界被 **Significance** 和问题动机支撑——研究问题实际重要、gap identification 清晰、实验设计（如果执行好的话）覆盖了审稿人会期望的对比和消融。\n\n具体推理：EMNLP 2026 短论文接收率约 ~25%。本 proposal 在动机和文献方面高于平均水平，但 novelty 低于平均水平（标准方法 + 预期结果）。如果实验结果中 temporal gate weights 揭示了 genuinely unexpected patterns（如某信号在所有时间点都 dominant，或信号权重在 hallucination vs factual 之间呈现非单调切换），可以推至 30%；如果结果 confirmatory，更接近 18-20%。\n\n【主要风险】:\n1. **\"Standard method in new domain\" 批评**：三条 GRU + gating MLP 在方法论上缺乏新颖性，审稿人很可能指出这是 \"straightforward application of well-known temporal fusion techniques to a new problem\"，尤其在 EMNLP 主会对 novelty 要求较高的背景下。\n2. **核心发现大概率 confirmatory 而非 surprising**：proposal 自身的机制论证（attention=WHERE, hidden=WHAT, logprob=HOW 的流水线顺序导致时间互补性）如果被实验验证，审稿人会觉得\"如预期所料\"；如果没被验证，则 motivation 与结果不一致。这是一个 lose-lose framing——positive results 不 surprising，negative results 削弱 motivation。\n```\n\nSources:\n- [HaluNet: Multi-Granular Uncertainty Modeling for Efficient Hallucination Detection](https://arxiv.org/html/2512.24562)\n- [Neural Message-Passing on Attention Graphs for Hallucination Detection (CHARM)](https://arxiv.org/abs/2509.24770)\n- [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models (ICLR 2025)](https://openreview.net/forum?id=VwOYxPScxB)\n- [Hallucination Detection via Activations of Open-Weight Proxy Analyzers](https://arxiv.org/abs/2605.07209)\n- [EigenTrack: Spectral Activation Feature Tracking](https://arxiv.org/html/2509.15735v4)\n- [HSAD: LLM Hallucination Detection via FFT on Hidden Layer Temporal Signals](https://arxiv.org/html/2509.13154)\n- [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection (ICLR 2024)](https://arxiv.org/abs/2402.03744)\n- [Multivariate Time Series Early Classification Across Channel and Time Dimensions](https://arxiv.org/html/2306.14606)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me synthesize everything.\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】:\n存在多个 trivial alternative 威胁：\n\n(1) **简单拼接 + 静态分类器**: 将三种信号在每步提取后直接 concatenate，喂入一个 MLP 或 logistic regression，不需要 GRU 也不需要 gating network。Proposal 确实在 ablation 中提到了 equal-weight fusion baseline 和 static logistic regression，但这些是实验层面的对照——核心问题是：如果简单拼接已经 work，那整个 GRU + gating architecture 的 engineering overhead 换来的增量到底有多大？这一增量价值完全取决于\"temporal complementarity\"假设是否成立，而这个假设本身未经验证。\n\n(2) **直接用最好的单信号时序检测器**: HALT 的 GRU on log-probs 已经证明 5M 参数的 GRU 即可取得 strong results。如果一个信号就已经 dominant（HALUPROBE 和 Proxy Analyzers 都发现 attention dominant；krogoldAI 发现 FFN dominant），那 fusion 增量可能是 marginal 的。Proposal 自己的 pilot design 也承认 r > 0.95 时 fusion 没有价值。\n\n增量价值在于：如果 temporal complementarity 确实存在（不同信号在不同生成阶段 dominant），fusion 能实现 Pareto improvement 尤其在 early detection。但这正是未验证的前提。\n\n(3) **Early detection 的实际需求质疑**: LLM 生成速度通常在 30-80 tokens/sec，一个 100 token 的回复约 1-3 秒。\"在 25% observation 时就检测\"相比\"等完整回复\"在实际部署中可能只节省 1-2 秒延迟。这个 practical motivation 是否足够强，审稿人可能会质疑。\n\n【前提假设检验】:\n核心 claim 的逻辑链有以下未经验证的关键假设：\n\n(1) **Temporal complementarity 假设 [核心]**: \"不同信号在不同生成阶段携带互补信息\"——这是整篇论文的立论基础。Proposal 用 mechanistic interpretability 论证（WHERE/WHAT/HOW），并引用 Trajectory Commitment（44.3% 的 prompt 在第一个 token 就分叉）和 Shadows in the Attention（attention-locking 渐进出现）。但这两篇论文研究的是不同现象（residual stream trajectories vs. attention patterns），不等于证明\"三种信号在同一个 generation 中有不同的 temporal profile\"。这个从 mechanistic 论述到 empirical complementarity 的推理跳跃是想当然的。\n\n(2) **\"Fusion 不可能比最好单臂差\"的 asymmetry 论证**: 理论上成立（gate 可以学到给一个 arm 全部权重），但在 1K examples + 5-fold CV 的小数据量下，多参数模型（~100K total）过拟合的风险是真实的。更多参数 + 更少数据 = validation performance 可能反而下降。\n\n(3) **Static comparison 冲突源于 temporal collapsing**: Proposal 声称 HALUPROBE 和 krogoldAI 的冲突是因为都是\"static snapshot\"，但更可能的原因是模型差异（Llama-2 vs. Ministral-8B）、数据集差异、特征工程差异。将冲突归因于\"temporal vs static\"并以此作为 temporal fusion 的动机，逻辑链不够坚实。\n\n【3 维度打分】:\n1. Novelty: 【中】\n   — 核心贡献是将 multivariate time series anomaly detection 中成熟的 multi-signal temporal fusion（GRU encoder + gating network）迁移到 LLM hallucination detection 领域。这是一个真实但增量的 novelty——各组件全部来自已有工作：三种信号分别源自 SinkProbe / EigenScore / HALT；GRU encoder 是标准架构；gating MLP with softmax 是经典的 attention/gating 机制；multi-horizon loss 是 early TSC 的直接适配。\n   — CHARM (ICLR 2026) 已经将 attention + activation 信号融合（通过 GNN）；HaDeMiF (ICLR 2025) 已经融合 hidden states + prediction characteristics。TemporalFuse 的增量 delta 是 (a) temporal 而非 static fusion，(b) early-detection loss。这个 delta 真实存在但较窄。\n   — \"First temporal map of signal importance during hallucination onset\" 是一个有价值的 interpretability 贡献，但属于 analysis byproduct，不是方法论创新。\n   — 如果核心发现是 positive（fusion helps, especially early），审稿人的反应很可能是 \"makes sense, I would have guessed this\"，而不是 \"surprising\"。Temporal complementarity 是一个 intuitive hypothesis。\n\n2. Significance: 【中】\n   — 研究问题本身（如何融合多种内部信号做实时幻觉检测）是重要的，对实际部署 LLM guardrails 有实用价值。\n   — 但 EMNLP short paper 版本的 scope 严重限制了 significance：1 model (Llama-8B)、1 benchmark (TruthfulQA)、1K examples。TruthfulQA 已经是一个相对 \"dated\" 的 benchmark，且它的分布较窄（factoid questions）。\n   — Early detection 的 practical motivation 论证不充分（如上分析，实际延迟节省可能很小）。\n   — \"解决 static comparison 冲突\"的 framing 有吸引力，但如前分析，冲突的真实原因可能不是 temporal vs static，而是模型/数据差异。\n   — 如果 temporal complementarity 不成立（pilot 的 r > 0.95 场景），paper 退化为 negative result（\"我们试了 fusion 但信号冗余\"），这在 short paper format 中是可以发表的，但 impact 会大幅降低。\n\n3. Related Work: 【强】\n   — 覆盖极其全面，包含 40+ 篇近期工作，涵盖 static comparison (HALUPROBE, Proxy Analyzers, krogoldAI, LLM-Check)、foundational methods (INSIDE/EigenScore)、multi-signal fusion (HaDeMiF, HaluNet, CHARM, ReDeEP)、single-signal temporal (EigenTrack, HALT, HSAD)、streaming detection、cascaded systems、cross-modal fusion 等多个子领域。\n   — 差异化定位清晰：对每个已有方法都明确指出 TemporalFuse 的差异（temporal vs static, multi-signal vs single-signal, early detection vs full-response）。\n   — 对 CHARM 和 HaDeMiF 这两个最接近的竞争者的分析准确且公允。\n   — 唯一潜在风险：该领域进展极快（2026 年 4-5 月就有大量新工作），到 ARR review 结束时可能有新的 overlap。\n\n【概率估计】: [18% - 28%] 中位 23%\n\n【估计理由】:\nNovelty 维度是概率上界的主要限制因素。核心架构（GRU + gating network + multi-horizon loss）是已有技术的组合迁移，个体组件均无创新。对于 EMNLP main conference（非 Findings），即使是 short paper，审稿人也会问 \"what's the conceptual contribution beyond putting known pieces together?\" \nSignificance 维度受限于 (a) early detection 的 practical motivation 论证不充分，(b) short paper 的实验 scope 过窄（1 model / 1 benchmark），(c) 核心发现如果 positive 并不 surprising。\nRelated work 是唯一强项，但好的 related work 覆盖只能保底不能拉高。\n\n综合来看，这是一个方向正确、定位清晰、但内核偏 engineering combination 的 proposal。它更接近 \"25-35% 区间的下沿\"——有真实 novelty delta 但 delta 较窄，核心发现 unsurprising。考虑到 EMNLP main track 的竞争性和 short paper 的实验局限性，中位估计 23%。如果投 Findings track，概率可能提升到 30-35%。\n\n【主要风险】:\n1. **Novelty 不足以支撑 main conference**: 审稿人可能认为这是 \"well-executed engineering\" 而非 \"scientific contribution\"——将 time series domain 的 mature techniques 应用于 hallucination detection，各组件都是 off-the-shelf，无 conceptual surprise。CHARM (ICLR 2026) 和 HaDeMiF (ICLR 2025) 已经探索了 multi-signal fusion for hallucination detection，TemporalFuse 的增量 delta（temporal + early detection）可能被视为 marginal extension。\n2. **核心前提假设（temporal complementarity）未经验证且可能不成立**: 如果三种信号 temporally redundant，整个 paper 的核心 narrative 崩塌。即使 proposal 设计了 dual-outcome pivot，一篇说\"我们验证了信号冗余\"的 short paper 在 EMNLP main track 的吸引力远低于原始 framing。\n```\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】:\n\n存在两个威胁性较高的 trivial alternatives：\n\n(1) **Simple feature concatenation + single GRU**：将三种信号在每个 step 直接拼接，送入一个 GRU，不需要三个独立编码器和 gating network。这是标准的多模态融合 baseline，实现成本极低。Proposal 虽然包含 \"equal-weight fusion\" 作为 ablation，但更具威胁的是 \"concatenation baseline\"——让单一 GRU 自己学习信号间的交互，而不是强加 gating 结构。如果 concatenation baseline 性能接近 gating fusion，则 gating 的增量价值仅限于可解释性（gate weights 可视化），而可解释性单独撑不起核心贡献。\n\n(2) **Best single-signal temporal detector（如 HALT 或 SinkProbe + GRU）+ 简单 ensemble**：对三个独立 arm 做 logit-level averaging 或 max-pooling，无需任何 learned fusion。如果这种 trivial ensemble 接近 TemporalFuse 的性能，则 \"learned adaptive fusion\" 的价值被架空。\n\n**增量价值在哪？** 如果确实存在明显的 temporal complementarity（不同阶段不同信号占优），gating 会优于静态融合。但这恰恰是需要实验验证的核心假设，而不是可以先验保证的。Proposal 意识到了这一点（pilot decision rule），但这也意味着整篇论文的核心贡献押注在一个未经验证的假设上。\n\n【前提假设检验】:\n\n核心逻辑链中有三个未经验证的环节：\n\n(1) **\"静态比较的分歧源于忽视了时间动态\"——这是一个叙事性归因，非事实**。HALUPROBE 和 krogoldAI 的分歧可能来自：不同模型（Llama-2-7B vs. Ministral-8B）、不同数据集、不同分类器架构、不同特征工程。将分歧归因于\"collapse of temporal dynamics\"是 narrative convenience，而非 established fact。如果实验中 temporal gate weights 在不同阶段并不显著变化，这个叙事就会崩塌。\n\n(2) **\"Attention = WHERE, Hidden states = WHAT, Log-probs = HOW → 因此时间上互补\"——这是一个看似合理但未经验证的 mechanistic story**。仅仅因为三种信号在 transformer pipeline 中位于不同位置，不代表它们在 hallucination detection 任务中携带 temporally complementary 的信息。它们可能同时反映同一个底层事件（如 knowledge retrieval failure），只是以不同的 magnitude 呈现。Pipeline 位置的不同 ≠ temporal complementarity。\n\n(3) **\"Fusion cannot underperform the best individual signal\"——理论上成立但实践中不保证**。在 1K 样本、5-fold CV 的设定下，gating network（12.5K 参数）+ 三个 GRU（75K 参数）的总参数量可能导致 overfitting，使 fusion 实际 underperform 最佳单 arm。这在小数据多模态融合中是常见现象。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心贡献是将三种已知有效的 hallucination detection 信号通过 GRU + gating network 进行 temporal fusion，并加入 multi-horizon early-detection loss。逐项拆解：\n   - GRU 建模内部信号的时间序列：HALT、EigenTrack 已做（非新）\n   - 多信号融合做 hallucination detection：HaDeMiF (ICLR 2025)、HaluNet、CHARM (ICLR 2026) 已做（非新）\n   - Gated fusion networks：多模态学习中的标准技术（非新）\n   - Multi-horizon early-detection loss：从 early time series classification 领域迁移到 hallucination detection——这是最具新意的单点贡献，但本质是 methodology transfer 而非 methodology invention\n   - Temporal signal importance map 的可解释性分析：有一定新意，但依赖于 gate weights 实际展示出有意义的时间变化模式\n   \n   与最相关的 5 篇近期工作（CHARM、HaDeMiF、HALT、EigenTrack、SinkProbe）对比，剔除 surface differences 后，真正剩余的 novelty delta 是：\"temporal fusion during generation\"（vs. static fusion on complete response）+ \"multi-horizon loss\"。这是一个 legitimate 但 incremental 的组合创新。审稿人会认可方向的合理性，但不会认为这是一个 surprising 的 insight。\n\n2. **Significance: 中** — \n   研究问题本身重要且实际——real-time hallucination detection 是 LLM 部署中的真实需求，\"which signal, when?\"是一个有价值的科学问题。然而：\n   - 如果 fusion positive，审稿人的反应更可能是 \"I would have guessed this\"——组合多个互补信号的 learned fusion 理应优于任何单一信号，这是一个直觉上 expected 的结果\n   - 如果 fusion 的提升幅度很小（如 AUROC 提升 1-2 个点），论文的核心价值转移到 interpretability analysis 上，但 gate weight 的可视化能否达到 \"insight\" 级别的发现，事先不确定\n   - Short paper scope（1 model, 1 dataset）限制了 generalizability claim 的强度\n   - 实际部署中，多信号融合的额外 latency 和实现复杂度可能使 practitioners 倾向于简单使用最好的单一信号\n\n3. **Related Work: 强** — \n   文献覆盖非常全面，包括最新的 2026 年工作（SinkProbe、CHARM、Proxy Analyzers、SinkTrack 等）。差异化定位清晰——准确识别了 \"static fusion\" vs. \"temporal fusion\" 和 \"no early detection optimization\" 两个 gap。对 HaDeMiF、HaluNet、CHARM 的定位是准确的。唯一的小瑕疵是将 HALUPROBE vs. krogoldAI 的分歧过度归因于 temporal dynamics 而非 experimental confounds。\n\n【概率估计】: [20% - 32%] 中位 25%\n\n【估计理由】: \nNovelty 限制了上界。这是一个方向正确、文献覆盖充分的 proposal，但核心贡献是已有技术的组合创新（GRU temporal modeling + gated fusion + multi-horizon loss），而非一个 surprising insight。如果核心发现是 positive（fusion > single signal, especially early），审稿人更可能说 \"reasonable and expected\" 而非 \"surprising\"。Related Work 的强度和问题的实际重要性为概率提供了下界支撑（不太可能因为方向错误被拒），但 novelty 的 incremental 性质和 \"I would have guessed this\" 的风险限制了上界。作为 EMNLP main conference short paper，25% 是合理的中位估计——有机会，但需要实验结果足够 crisp 且 temporal signal importance map 展示出 genuinely surprising patterns 才有望突破上界。\n\n【主要风险】:\n1. **\"I would have guessed this\" 风险**：核心发现（多信号 learned fusion > 单信号）在审稿人看来可能是 expected result 而非 genuine insight，尤其当改进幅度较小时。论文的 novelty 将主要依赖 temporal signal importance map 的发现是否 surprising，这是一个不可控的风险。\n2. **Trivial baseline 威胁**：如果 simple concatenation（三种特征直接拼接送入单一 GRU）或 logit-level ensemble 性能接近 TemporalFuse，则 gating network 的增量贡献被挤压到仅剩可解释性，对于 main conference 而言可能不够。\n```\n\nSources:\n- [CHARM: Neural Message-Passing on Attention Graphs for Hallucination Detection](https://arxiv.org/abs/2509.24770)\n- [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models (ICLR 2025)](https://openreview.net/forum?id=VwOYxPScxB)\n- [SinkProbe: Attention Sinks as Internal Signals for Hallucination Detection](https://arxiv.org/abs/2604.10697)\n- [HALT: Hallucination Assessment via Log-probs as Time series](https://arxiv.org/abs/2602.02888)\n- [HSAD: LLM Hallucination Detection via FFT on Hidden Layer Temporal Signals](https://arxiv.org/abs/2509.13154)\n- [SinkTrack: Attention Sink based Context Anchoring (ICLR 2026)](https://arxiv.org/abs/2604.10027)\n- [LapEigvals: Hallucination Detection Using Spectral Features of Attention Maps (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1239.pdf)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# TemporalFuse: Adaptive Multi-Signal Temporal Fusion for Early Hallucination Detection via Learned Signal Dynamics\n\n**状态**: 待审阅  \n**级别**: top-tier  \n**创建时间**: 2026-05-15T16:22:26.445444+00:00\n\n## 描述\nTemporalFuse proposes the first adaptive multi-signal temporal fusion method for early hallucination detection during autoregressive LLM generation. Unlike prior detectors that each rely on a single internal signal type — attention sinks (SinkProbe), hidden-state spectral features (EigenTrack), or log-probabilities (HALT) — and unlike prior multi-signal approaches that fuse statically on complete responses (HaDeMiF fuses hidden states + prediction characteristics via D3T/MLP; HaluNet fuses embeddings + log-likelihoods + entropy via parallel branches; CHARM combines attention and activation features via GNN) — TemporalFuse trains three parallel GRU encoders on these signal streams and introduces a cross-signal gating network that learns time-varying weights over the signal streams at each generation step. The gating MLP (192→64→3 with softmax) produces interpretable per-step weights α_t indicating which signal the model relies on at each generation stage, providing the first temporal map of signal importance during hallucination onset. The method also introduces a multi-horizon early-detection loss that optimizes detection at multiple observation fractions simultaneously (L = Σ w_f·BCE at fractions {0.25, 0.5, 0.75, 1.0}), adapting early time series classification methodology to hallucination detection for the first time — explicitly training the model to detect hallucination from partial responses. The SpectralTrack arm extends the eigenvalue-based hallucination detection paradigm established by INSIDE/EigenScore (ICLR 2024) — which showed LLMs' internal states retain hallucination-detection power via eigenvalues of hidden-state covariance matrices — from sentence-level multi-generation analysis to per-step sliding-window tracking within a single generation. The architecture uses identical GRU encoders (~25K recurrent parameters each) with per-arm linear projections (raw dims ~50–120 / ~10–20 / ~25 → common d=32), ensuring the fusion improvement reflects genuine signal complementarity rather than architectural differences. This directly addresses the unresolved conflict between static signal comparisons: HALUPROBE and Proxy Analyzers find attention dominant, krogoldAI finds FFN/hidden states dominant — TemporalFuse shows how optimal reliance varies temporally, explaining why static snapshots disagree. The framework is grounded in mechanistic interpretability: attention heads route information (WHERE), hidden states accumulate computation (WHAT), log-probs reflect confidence (HOW) — since these pipeline stages process information sequentially, they should carry temporally complementary hallucination signatures, making learned fusion the principled default. For the EMNLP 2026 short paper (ARR May 25 — the only deadline eligible for EMNLP 2026 commitment on August 2; if missed, short paper targets August 3 ARR → EACL 2027): 1 model (Llama-3.1-8B), 1 benchmark (TruthfulQA), 1K examples, demonstrating fusion outperforms individual arms especially at partial observation, with interpretable temporal signal importance analysis. Entity-match onset annotation uses objective NER-based curation (spaCy en_core_web_lg, factoid question patterns). For AAAI 2027 full paper (abstract July 21, paper July 28): adds a fourth FFN activation arm (resolving krogoldAI conflict), 3 models, 3 benchmarks, CascadeProbe extension (using learned gate thresholds for compute-adaptive escalation), and DoLa intervention. All claims supported by 5-fold stratified CV with bootstrap 95% CIs and paired permutation tests. Explicit pilot decision rule: if per-step GRU logits across all arm pairs show Pearson r > 0.95 (temporal redundancy), the contribution focuses on why signals are redundant despite carrying different static information. Total compute: ≤230 H100-hours.\n\n## 核心问题\nReal-time hallucination detection during LLM generation requires monitoring internal signals, but practitioners face two unsolved problems. First, existing detectors each rely on a single signal type — attention patterns (SinkProbe, AUROC 0.89 on HaluEval-QA), hidden-state dynamics (EigenTrack, 0.82–0.94 AUROC; HSAD via FFT), or log-probabilities (HALT via GRU) — with no principled way to combine them. Static comparisons disagree on which signal is best: HALUPROBE (arXiv 2502.13490) and Proxy Analyzers (arXiv 2605.07209) both find attention-based features dominant (attention entropy + per-head source-document attention account for 88%+ of Random Forest importance in Proxy Analyzers), while krogoldAI's empirical study finds FFN activations (82.96% accuracy, 91.04% AUC) outperform attention (79.90%, 88.46% AUC), concluding attention 'added no value beyond what FFN activations already provided.' This conflict persists because all comparisons are static — they collapse temporal dynamics into single snapshots, ignoring that different signals may carry complementary information at different generation stages. Second, and more critically, no existing method optimizes for early detection — identifying hallucination from partial responses (e.g., after only 25% of tokens are generated). Current detectors are trained and evaluated on complete responses, yet real-time guardrails must act as early as possible. Early time series classification is well-established in other domains (MultiETSC, RL-based early classifiers) but has never been applied to hallucination detection during LLM generation. These two gaps — no multi-signal temporal fusion, no early-detection optimization — mean practitioners building real-time hallucination guardrails must choose a single signal type with no principled basis, deploy a detector that cannot be trusted until generation is nearly complete, and sacrifice either accuracy (single signal) or latency (waiting for full response).\n\n## 机遇 / Why Now\nFive independent research threads converge to make adaptive temporal fusion both possible and timely. (1) Signal validation: SinkProbe (arXiv 2604.10697) established attention sinks, EigenTrack (arXiv 2509.15735) validated hidden-state spectral features, and HALT (arXiv 2602.02888) proved log-probability time series — each independently effective for hallucination detection via temporal modeling, but never combined. The foundational basis for internal-state hallucination detection was established by INSIDE (ICLR 2024), which showed that LLMs' internal states retain hallucination-detection power via EigenScore, an eigenvalue-based metric on hidden-state covariance matrices. (2) Causal grounding: SinkTrack (ICLR 2026) demonstrated that modifying attention sinks causally affects hallucination; ReDeEP (ICLR 2025) showed Knowledge FFNs and Copying Heads carry mechanistically distinct hallucination information — establishing that different signal types carry independent, non-redundant information. (3) Temporal complementarity evidence: Hallucination as Trajectory Commitment (arXiv 2604.15400) showed residual-stream trajectories bifurcate at the first generated token in 44.3% of prompts, while Shadows in the Attention (arXiv 2505.16894) found attention-locking thresholds emerge gradually — suggesting attention and hidden-state signals have fundamentally different temporal profiles, creating an opportunity for fusion. (4) Cross-modal fusion precedent: Attention-based fusion of multiple temporal signal streams is well-established in multivariate time series anomaly detection (MFGAN, DSAC) and multi-modal monitoring, but has never been applied to LLM internal signals. (5) Early classification methodology: Prefix-based multi-horizon training for time series is mature (tslearn, MultiETSC), providing the methodological foundation for optimizing detection at partial observation.\n\nThe key insight: if different signals carry complementary information at different generation stages (attention sinks as routing indicators, hidden states as computation indicators, log-probs as confidence indicators), then a learned time-varying fusion should outperform any fixed single-signal detector, and optimizing for early detection should yield faster-acting guardrails. We test this with TemporalFuse — the first adaptive multi-signal temporal fusion method for hallucination detection during autoregressive generation. The fusion architecture is the primary methodological contribution; the analysis of learned signal weights provides the first temporal comparison of signal types as an interpretable byproduct.\n\n## 方法思路\nWe propose TemporalFuse, an adaptive temporal fusion method that learns time-varying weights over three internal signal streams — attention sinks, hidden-state spectral features, and log-probabilities — to detect hallucination during autoregressive generation, optimized for the earliest possible detection. The primary methodological contribution is the fusion architecture and early-detection training objective; the analysis of learned fusion weights provides the first temporal signal comparison as an interpretable byproduct.\n\n**Theoretical Motivation: Why Fusion Should Outperform Single Signals.** The three signal types occupy different positions in the transformer's computational pipeline: attention heads function as information routing (WHERE the model reads — Wu et al., ICLR 2025), hidden states represent accumulated computation (WHAT the model has computed — FFN key-value memories, Geva et al., EMNLP 2021), and log-probabilities reflect output confidence (HOW certain the model is). Because routing decisions causally precede the computation they gate, and both precede the output distribution, these signals should carry complementary information: a routing error may appear in attention features before the residual stream incorporates erroneous information, while confidence collapse in log-probs may be the most direct indicator of hallucination once it manifests. If the signals are temporally complementary (shifting at different times and rates), learned fusion can outperform any individual signal by attending to the most informative signal at each generation stage. If they are temporally redundant, fusion still cannot underperform the best individual signal (it can learn to assign all weight to one arm). This asymmetry makes fusion the principled default.\n\n**Architecture: Three-Arm Temporal Encoder + Cross-Signal Gating + Early-Detection Loss.**\n\nFor each generation, we extract three parallel feature streams at every decoding step t:\n\n*Arm 1 — SinkWatch (Attention Sinks):* Per-step features from top-K informative head-layer combinations (K=5–15) identified via SinkProbe's ℓ₁-regularized analysis: sink scores for top-k sink tokens (k=2–3), sink concentration, sink entropy, context-attention ratio, plus first-order temporal derivatives. Raw dim ~50–120.\n\n*Arm 2 — SpectralTrack (Hidden States):* Per-step spectral features from sliding-window covariance matrices of hidden-state activations: leading eigenvalues, spectral gaps, entropy, RMT statistics. This extends the eigenvalue-based hallucination detection paradigm established by INSIDE/EigenScore (ICLR 2024, Chen et al.) — which showed that eigenvalues of hidden-state covariance matrices capture hallucination-relevant semantic structure — from sentence-level multi-generation analysis to per-step sliding-window tracking within a single generation, matching EigenTrack's temporal design. Raw dim ~10–20.\n\n*Arm 3 — LogProbTrack (Log-Probabilities):* Per-step log-probability features: token log-prob, predictive entropy, top-k probability gap, rank. Matching HALT's design. Raw dim ~25.\n\nEach arm includes a per-arm learned linear projection to common dimension d=32, then feeds into an identical unidirectional GRU (hidden_dim=64, ~25K recurrent parameters). At each step t, the three GRU hidden states h_t^sink, h_t^spec, h_t^logp ∈ ℝ^64 represent modality-specific temporal summaries.\n\n**Cross-Signal Gating Network (Novel Component 1).** A learned gating network dynamically weights the three signal streams at each step:\n- Input: concatenation [h_t^sink; h_t^spec; h_t^logp] ∈ ℝ^192\n- Gating MLP: 192 → 64 (ReLU) → 3 (softmax) → gate weights α_t ∈ ℝ^3\n- Fused representation: z_t = Σ_i α_t^i · h_t^i ∈ ℝ^64\n- Detection score: ŷ_t = σ(w^T z_t + b)\n\nThe gate weights α_t are directly interpretable: α_t^sink = 0.6 at step 5 means the model assigns 60% importance to attention sink features at that generation stage. By plotting mean gate weights across steps for factual vs. hallucinated generations, we obtain the first temporal map of signal importance during hallucination — the comparison result emerges as an interpretable analysis of the method. Total gating parameters: ~12.5K (negligible vs. 75K total GRU parameters).\n\n**Multi-Horizon Early-Detection Loss (Novel Component 2).** Instead of training only on complete responses, we optimize detection at multiple observation fractions simultaneously:\n\nL = Σ_{f ∈ F} w_f · BCE(ŷ_{T·f}, y)\n\nwhere F = {0.25, 0.50, 0.75, 1.0} are observation fractions, ŷ_{T·f} is the detection score at step ⌊T·f⌋, y is the ground-truth label, and w_f = f (linear weighting — more lenient at early fractions, full weight at complete observation). This adapts early time series classification methodology (MultiETSC, RL-based early classifiers) to hallucination detection for the first time, explicitly training the model to produce informative predictions before generation is complete. The loss encourages the gating network to attend to whichever signal carries the earliest discriminative information.\n\n**Primary Analyses (EMNLP Short Paper).** (1) Fusion vs. individual arms: AUROC/AUPRC comparing TemporalFuse against each individual arm, testing whether fusion outperforms the best single signal. (2) Early-detection curves: AUROC at observation fractions {0.10, 0.25, 0.50, 0.75, 1.0} for TemporalFuse vs. individual arms, demonstrating the benefit of multi-horizon training. (3) Temporal signal importance map: mean gate weights α_t across steps for factual vs. hallucinated generations — the first visualization of how optimal signal reliance changes during hallucination onset. This directly answers 'which signal, when?' without framing it as a standalone comparison study. (4) Static-vs-temporal ranking: comparing signal rankings from our learned gate weights against HALUPROBE's and Proxy Analyzers' static findings. (5) Ablation: TemporalFuse with/without multi-horizon loss; TemporalFuse with/without gating (equal-weight fusion baseline); individual arms with temporal GRU vs. static logistic regression.\n\n**Statistical Rigor.** 5-fold stratified cross-validation, reporting mean ± std for all metrics. Bootstrap 95% CIs (1000 resamples) for pairwise comparisons. Paired permutation tests (10,000 permutations, p < 0.05). Cohen's d effect sizes.\n\n**Entity-Match Onset Annotation (for temporal signal importance analysis).** For the subset of TruthfulQA used in temporal gate-weight analysis, we apply objective NER-based curation: include questions where (a) the reference answer contains ≥1 named entity detected by spaCy NER (model en_core_web_lg), AND (b) the question matches factoid patterns (starts with 'Who', 'What is/was', 'Where is/was', 'When did/was', or contains 'name of'). Onset = first generated token matching a hallucinated entity (entity not in reference, detected by NER). We supplement with NLI sliding-window annotation (window size 10 tokens, entailment threshold 0.5 via DeBERTa-v3-large-MNLI). Report agreement rate between entity-match and NLI-window onset.\n\n**Pilot Design (First 48 hours).** 100 TruthfulQA examples on Llama-3.1-8B: extract all three feature streams, train TemporalFuse and individual arms. **Decision rule:** If all three signals are perfectly correlated temporally (Pearson r > 0.95 between per-step GRU logits across all arm pairs), fusion cannot help — pivot to analyzing why temporal dynamics are redundant despite carrying different static information. If signals show distinct temporal profiles (r < 0.85 for at least one pair), proceed with full experiments.\n\n**Dual-Target Venue Strategy:**\n\n*EMNLP 2026 (ARR May 25 — short paper, 4 pages):* 1 model (Llama-3.1-8B-Instruct), 1 benchmark (TruthfulQA), 1K examples. Focus: TemporalFuse method + early-detection curves + temporal signal importance map + ablations. Core claim: adaptive temporal fusion outperforms individual signals, especially at partial observation. May 25 is the only ARR submission deadline eligible for EMNLP 2026 commitment (August 2, 2026). There is no June ARR cycle — the 10-day timeline (May 15–25) is non-negotiable for EMNLP 2026. If May 25 is missed, the short paper targets the August 3 ARR cycle for commitment to EACL 2027 (commitment deadline October 11, 2026), while the full method paper proceeds to AAAI 2027 independently.\n\n*AAAI 2027 (full paper, 8 pages, abstract deadline July 21, paper deadline July 28):* 3 models (Llama-3.1-8B, Mistral-7B-v0.3, Llama-3.1-70B), 3 benchmarks (TruthfulQA, TriviaQA, HaluEval-QA), 2K examples per pair. **Fourth arm: FFN activations** (matching krogoldAI's feature design — mean-pooled FFN outputs from informative mid-layers) to directly resolve the conflicting static evidence. Full temporal characterization, complementarity analysis, CascadeProbe extension (using learned gate thresholds as escalation triggers for compute-adaptive detection), DoLa intervention when the fused probability exceeds threshold.\n\n**Baselines.** Single-signal temporal: individual GRU arms (SinkWatch, SpectralTrack, LogProbTrack). Static: SinkProbe, LapEigvals, TOHA. Prior temporal: EigenTrack, HALT. Online: MIND, DRIFT, PCNet. Multi-signal static: HaDeMiF-style fusion (hidden states + prediction characteristics, static), HaluNet-style parallel fusion (equal-weight concatenation of static features). Ablation: equal-weight temporal fusion (no gating), TemporalFuse without multi-horizon loss.\n\n**Evaluation Metrics.** Primary: AUROC and AUPRC with 95% bootstrap CIs. Secondary: early-detection AUROC at partial observation fractions, F1 at calibrated threshold, latency overhead (ms/token), gate weight entropy (measuring signal specialization), Cohen's d. For AAAI: hallucination rate reduction with DoLa intervention, compute-accuracy Pareto curves for CascadeProbe.\n\n## 研究现状\n**Static signal-type comparison for hallucination detection:** HALUPROBE (arXiv 2502.13490, Feb 2025) compares attention weights, hidden-state activations, and logits with static classifiers on Llama-2-7B and Vicuna-7B, finding attention-based lookback ratio achieves highest accuracy. Proxy Analyzers (arXiv 2605.07209, May 2026) finds per-head source-document attention and attention entropy account for 88%+ of Random Forest importance across 18 features and 7 analyzer architectures. However, krogoldAI (HuggingFace blog, Dec 2025) found FFN activations (91.04% AUC) outperform attention (88.46% AUC) using Ministral-8B on 145K examples — directly contradicting both. LLM-Check (NSF 2025) also finds hidden-state methods (SAPLMA) generally outperform logit-based and attention-based methods. All comparisons are static; none model temporal dynamics during generation. **TemporalFuse resolves this conflict by showing how optimal signal reliance varies across generation stages — a signal dominant statically may not be dominant at partial observation.**\n\n**Foundational internal-state detection:** INSIDE (ICLR 2024, Chen et al.) established the foundational principle that LLMs' internal states retain hallucination-detection power, introducing EigenScore — an eigenvalue-based metric on the covariance matrix of last-token middle-layer embeddings across multiple generations. EigenScore measures semantic consistency in the dense embedding space and achieved 80–84% AUROC across QA benchmarks. This directly informs SpectralTrack's feature design: while INSIDE operates at the sentence level across multiple generations, SpectralTrack extends eigenvalue-based features to per-step sliding-window analysis within a single generation, enabling temporal tracking.\n\n**Multi-signal fusion for hallucination detection:** HaDeMiF (ICLR 2025, Zhou et al.) fuses hidden states (via MLP) and prediction characteristics — confidence, uncertainty, consistency — (via Deep Dynamic Decision Tree) for hallucination detection and calibration, achieving effective detection with <2% parameter overhead. However, HaDeMiF operates on complete responses with static fusion of output-space characteristics and hidden states; it does not model temporal dynamics during generation, does not incorporate attention-based signals, and does not optimize for early detection. HaluNet (arXiv 2512.24562, Dec 2025) fuses semantic embeddings, log-likelihoods, and entropy via a multi-branch architecture — but uses parallel fusion on complete responses, not learned temporal fusion during generation. ReDeEP (ICLR 2025) combines Knowledge FFN scores and Copying Head attention for RAG hallucination detection — mechanistically principled but operates on single forward passes. CHARM (ICLR 2026) applies GNNs on graphs combining attention and activation features — static aggregation, no temporal modeling. UniFact (arXiv 2512.02772) benchmarks hidden-state and logit methods but does not fuse signals. **No prior work — including HaDeMiF, HaluNet, and CHARM — learns time-varying weights over multiple signal types during autoregressive generation or optimizes for early detection at partial observation.**\n\n**Single-signal temporal/trajectory detection:** EigenTrack (arXiv 2509.15735) tracks hidden-state spectral dynamics via GRU (0.82–0.94 AUROC). HALT (arXiv 2602.02888) treats log-probs as time series via bidirectional GRU. HSAD (arXiv 2509.13154) applies FFT to cross-layer hidden-state activations. Step-Level Hidden-State Transport Geometry (arXiv 2605.13772) uses BiLSTM on hidden-state geometric features. ICR Probe (ACL 2025) tracks cross-layer hidden-state evolution. **Each validates temporal modeling for one signal type; none combine multiple signals or optimize for early detection.**\n\n**Streaming and temporal hallucination detection during generation:** Streaming Hallucination Detection (arXiv 2601.02170, Lu et al.) also models hallucination as temporally evolving during generation, treating step-level hallucination judgments as local observations and introducing a cumulative prefix-level signal that tracks the global evolution of the reasoning state. However, it uses external NLI judges on chain-of-thought reasoning steps rather than fusing internal signal streams — a fundamentally different signal source (external model judgments vs. internal activations), different task domain (long CoT reasoning vs. factual QA generation), and different method (cumulative NLI scoring vs. learned multi-signal temporal fusion). TemporalFuse shares the temporal framing but addresses the complementary problem of fusing multiple internal signals for factual QA, without requiring external judges.\n\n**Cascaded/adaptive detection systems:** HaluGate (vLLM blog, Dec 2025) implements a three-stage cascade (Sentinel binary classifier → token-level detector → NLI explainer) achieving 72.2% query skip rate — but cascades at the query-type level using external signals, not across internal signal types. HALL-OPT (Nature Scientific Reports 2026) combines dual-stream attention detection with adaptive token pruning — but streams are parallel, not sequentially gated. Monitoring Decoding (ACL Findings 2025) gates expensive correction based on cheap monitoring — gates mitigation, not detection depth. Energy-efficient speculative decoding (arXiv 2508.12590) filters tokens for expensive verification using attention-weight statistics and uncertainty — the closest paradigm to our approach but applied to speculative decoding, not hallucination detection. **No prior work cascades across internal signal types (attention → hidden states → log-probs) with learned escalation for hallucination detection.**\n\n**Cross-modal temporal fusion in other domains:** Attention-based fusion of multiple temporal signal streams is well-established in multivariate time series anomaly detection (MFGAN, DSAC), video anomaly detection, and industrial monitoring. These provide architectural precedent for our cross-signal attention mechanism but have never been applied to LLM internal signals.\n\n**The open gaps:** (1) No method fuses multiple internal signal types with learned temporal weighting during generation — existing fusion is static (HaDeMiF, HaluNet, CHARM, ReDeEP) or external (HaluGate). (2) No method optimizes for early detection at partial observation fractions — all detectors are trained on complete responses. (3) No analysis shows how optimal signal reliance changes during generation — static comparisons collapse temporal dynamics. TemporalFuse addresses all three.\n\n## 目标 Venue\n- EMNLP 2026 (primary short-term target — ARR May 25, 2026, the only submission deadline eligible for EMNLP 2026 commitment on August 2, 2026; 4-page short paper focusing on TemporalFuse method, early-detection curves, and temporal signal importance analysis; Findings track acceptable; if missed, short paper targets August 3 ARR → EACL 2027 commitment October 11, 2026)\n- AAAI 2027 (primary long-term target — abstract deadline July 21, paper deadline July 28, 2026; full 8-page method paper with 4 signal arms including FFN, multi-model evaluation, CascadeProbe extension, intervention experiments)\n- ICLR 2027 (fallback — deadline expected ~October 2026; allows additional experiments if AAAI timeline requires descoping)\n\n## 关键参考\n- What are Models Thinking about? Understanding Large Language Model Hallucinations 'Psychology' through Model Inner State Analysis [HALUPROBE] (arXiv 2502.13490, Feb 2025)\n- Hallucination Detection via Activations of Open-Weight Proxy Analyzers [Proxy Analyzers] (arXiv 2605.07209, May 2026)\n- Towards Unification of Hallucination Detection and Fact Verification for Large Language Models [UniFact] (arXiv 2512.02772, Dec 2025)\n- Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models [SinkProbe] (arXiv 2604.10697, April 2026)\n- EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs (arXiv 2509.15735, 2025)\n- HALT: Hallucination Assessment via Log-probs as Time series (arXiv 2602.02888, Feb 2026)\n- Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models [MIND] (ACL Findings 2024, arXiv 2403.06448)\n- LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals [HSAD] (arXiv 2509.13154, Sep 2025)\n- HaluNet: Multi-Granular Uncertainty Modeling for Efficient Hallucination Detection in LLM Question Answering (arXiv 2512.24562, Dec 2025)\n- ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability (ICLR 2025, arXiv 2410.11414)\n- HaDeMiF: Hallucination Detection and Mitigation in Large Language Models (ICLR 2025, OpenReview VwOYxPScxB, arXiv 2601.09929)\n- INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection [EigenScore] (ICLR 2024, arXiv 2402.03744)\n- Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation (arXiv 2604.15400, April 2026)\n- Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models (arXiv 2604.13068, April 2026)\n- Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)\n- Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs (arXiv 2505.16894, May 2025)\n- HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders (arXiv 2604.16430, April 2026)\n- Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)\n- Uncertainty-Aware Attention Heads: Efficient Unsupervised Uncertainty Quantification for LLMs [RAUQ] (arXiv 2505.20045, May 2025)\n- Hallucination Detection in LLMs with Topological Divergence on Attention Graphs [TOHA] (ACL 2026, arXiv 2504.10063)\n- SinkTrack: Attention Sink based Context Anchoring for Large Language Models (ICLR 2026, arXiv 2604.10027)\n- FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG (arXiv 2601.05866, Jan 2026)\n- First Hallucination Tokens Are Different from Conditional Ones (arXiv 2507.20836, 2025)\n- Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)\n- ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs (ACL 2025, arXiv 2507.16488)\n- Real-Time Detection of Hallucinated Entities in Long-Form Generation (arXiv 2509.03531, 2025)\n- Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation (arXiv 2604.10098, April 2026)\n- Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNet/PC-LDCD] (arXiv 2605.05953, May 2026)\n- DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)\n- Hallucination Detection in LLMs Using Spectral Features of Attention Maps [LapEigvals] (EMNLP 2025, arXiv 2502.17598)\n- Neural Message-Passing on Attention Graphs for Hallucination Detection [CHARM] (ICLR 2026, arXiv 2509.24770)\n- Spectral Guardrails for Agents in the Wild: Detecting Tool Use Hallucinations via Attention Topology (arXiv 2602.08082, Feb 2026)\n- AggTruth: Contextual Hallucination Detection using Aggregated Attention Scores in LLMs (ICCS 2025, arXiv 2506.18628)\n- Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, Jan 2026)\n- Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (ACL Findings 2025, arXiv 2503.03106)\n- DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models (ICLR 2024)\n- Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention (arXiv 2602.18145, Feb 2026)\n- Mirage in the Eyes: Hallucination Attack on Multi-modal Large Language Models with Only Attention Sink (USENIX Security 2025, arXiv 2501.15269)\n- Retrieval Head Mechanistically Explains Long-Context Factuality (Wu et al., ICLR 2025)\n- Transformer Feed-Forward Layers Are Key-Value Memories (Geva et al., EMNLP 2021)\n- HaluGate: Token-Level Truth — Three-Stage Conditional Hallucination Detection Pipeline (vLLM Blog, Dec 2025)\n- HALL-OPT: Hallucination-Aware Learning and Latency Optimization Transformer for Real-Time Edge Intelligence (Nature Scientific Reports, 2026)\n- LLM-Check: Investigating Detection of Hallucinations in Large Language Models (NSF, 2025)\n- krogoldAI: LLM Hallucination Detection via Internal Representations (HuggingFace Blog, Dec 2025)\n- Energy-Efficient Speculative Decoding with Uncertainty-Awareness and Adaptive Token Filtering (arXiv 2508.12590, 2025)\n\n## 资源估算\n### auto_research\n- **claude_api_cost**: $320–530 (~3200–5300 turns).\n- **estimated_gpu_cost**: $575–690.\n- **gpu_hours**: ~230h H100 total.\n- **gpu_utilization**: High (~80%+).\n- **speed_bottleneck**: Bottlenecked by eager-mode attention extraction (~3–4× slower than standard inference). 1K examples × ~100 tokens ≈ 10–15h on single H100, parallelizable. The gating network and multi-horizon loss add negligible training overhead.\n- **team**: 0 (initial setup + final review only)\n- **timeline**: EMNLP: 7–8 days. AAAI: 3 additional weeks.\n\n### human_in_loop\n- **claude_api_cost**: $220–380 (~2200–3800 turns).\n- **estimated_gpu_cost**: $525–630.\n- **gpu_hours**: ~210h H100 total.\n- **gpu_utilization**: Moderate-high (~60–70%).\n- **risk_note**: Primary risk: signals may be temporally redundant (fusion ≈ best individual arm). Mitigation: (1) pilot correlation check in first 48 hours — if r > 0.95 across all pairs, shift focus to understanding why; (2) even if fusion margin is small, the early-detection curves and temporal signal importance maps are novel contributions independent of fusion magnitude; (3) the multi-horizon loss may still improve individual arms. Secondary risk: the 10-day EMNLP timeline is aggressive and non-negotiable — May 25 is the only ARR submission deadline for EMNLP 2026 commitment (August 2). There is no June ARR cycle; the next cycle after May 25 is August 3, which can only commit to EACL 2027 (October 11 commitment deadline). Mitigation: (1) short paper scope (1 model, 1 benchmark) is tractable in 10 days; (2) fusion architecture adds minimal implementation overhead (~200 lines on top of three arms); (3) if EMNLP is missed, the short paper targets August 3 ARR → EACL 2027, while the full method paper proceeds to AAAI 2027 (July 28 paper deadline) independently — both venue paths remain viable. Tertiary risk: entity-match onset annotation unreliable. Mitigation: NER-based curation criteria are objective and reproducible; NLI sliding-window supplement provides independent validation; TriviaQA added as primary onset benchmark in AAAI version.\n- **team**: 1 researcher, ~60min/day for EMNLP sprint, ~45min/day for AAAI\n- **timeline**: EMNLP: 10 days (May 15–25, non-negotiable for EMNLP 2026; fallback: August 3 ARR → EACL 2027). AAAI: 8 additional weeks.\n\n### manual\n- **estimated_gpu_cost**: $475–570\n- **gpu_hours**: ~190h H100 total. EMNLP short paper: ~52h (feature extraction for 3 arms × 1K examples on Llama-8B: ~20h; GRU + fusion training with 5-fold CV: ~10h; baselines including HaDeMiF-style and HALUPROBE-style: ~12h; curated subset annotation + analysis: ~6h; pilot: ~4h). AAAI full paper (incremental): ~138h additional (multi-model extraction: ~60h; 70B experiments: ~20h; 4th FFN arm: ~12h; CascadeProbe extension: ~8h; extended baselines + DoLa intervention: ~20h; additional CV + ablations: ~18h).\n- **gpu_utilization**: Moderate (~50–60%).\n- **team**: 1–2 researchers\n- **timeline**: EMNLP short paper: 10 days (May 15–25). This timeline is non-negotiable — May 25 is the only ARR deadline eligible for EMNLP 2026. If missed, the short paper shifts to the August 3 ARR cycle targeting EACL 2027. AAAI full paper: additional 8 weeks (May 25–July 21).\n\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T01:54:30.164Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T01:54:30.164Z",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T01:54:30.178Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have enough information to make my assessment. Let me synthesize everything.

---

```
【阶段】: Triage

【Trivial Alternative 检验】: 
存在严重的 trivial alternative 威胁。

(1) **单 GRU + 特征拼接**：将三类信号在每步直接拼接（dim ~85-165），输入一个 GRU，末尾接分类头。如果三类信号确实互补，这种最简单的方法同样能隐式学到时变的特征重要性——不需要三个独立编码器 + 显式 gating MLP。Proposal 辩称 gating 提供"可解释性"，但 gradient attribution / SHAP / attention rollout 等 post-hoc 方法同样可以对单 GRU 做特征归因，代价远低于专门设计 gating 架构。因此 gating network 的增量价值很大程度局限于"更直接的可解释性"——这是一个 nice-to-have，但不构成核心方法论贡献。

(2) **Multi-horizon loss 独立于 fusion 架构**：multi-horizon early-detection loss（在不同 observation fraction 上计算 BCE 加权和）是一个通用训练技巧，可以直接施加于任何已有单信号检测器（如 HALT、EigenTrack）。如果单信号 + multi-horizon loss 就已经大幅提升早期检测性能，那 fusion 的增量价值将更加微弱。这一分离性意味着 proposal 的两个"Novel Component"实际上是独立的，而非协同的。

增量价值在哪：如果 fusion 的增量 AUROC gain 在统计上显著且实质性（>2-3 pp），且 temporal gate weights 揭示了**反直觉的**信号动态（而非 proposal 自身机制论证所预测的"attention 先变化 → hidden states 中间 → log-probs 最后"），则有增量价值。但 proposal 自己的理论论证恰恰预测了最可能出现的结果模式——这使得发现大概率是 confirmatory 而非 surprising。

【前提假设检验】: 
核心 claim 的逻辑链条中有两个关键未验证假设：

(1) **"三类信号具有时间互补性"（temporal complementarity）**：Proposal 的机制论证是——attention 做 routing (WHERE)，hidden states 做 computation (WHAT)，log-probs 做 confidence (HOW)，因为它们在 transformer pipeline 中的位置不同，所以应该在不同的生成阶段携带互补的幻觉信号。但这个论证混淆了**步内（intra-step）**和**步间（inter-step）**的时间尺度。在每个 decoding step 内，attention → FFN → output 确实是顺序的；但 TemporalFuse 的 GRU 跨越的是 generation steps（不同 token 的生成时刻），在这个时间尺度上，所有三类信号都是同一个自回归过程的产物，可能高度相关。Proposal 承认了这个风险（pilot 中 Pearson r > 0.95 → pivot），但没有提供任何先验证据支持互补性假设。它引用的 "Hallucination as Trajectory Commitment" 和 "Shadows in the Attention" 显示 hidden states 和 attention 有不同的时间 profile，但这些观察是在不同实验设置下得出的，直接外推到 TruthfulQA + Llama-3.1-8B 设置并不可靠。

(2) **"静态比较的分歧是因为忽略了时间动态"**：Proposal 将 HALUPROBE（attention 最优）与 krogoldAI（FFN 最优）的分歧归因于"static snapshots collapse temporal dynamics"。但更 parsimonious 的解释是——不同的模型（Llama-2-7B vs Ministral-8B）、不同的数据集、不同的特征工程、不同的分类器导致了不同的结论。Temporal dynamics 作为解释是一个合理的假设，但被呈现得过于肯定，似乎是 proposal 设计的 motivation 而非客观分析的结论。如果真实原因是 model/dataset/feature 差异而非 temporal collapse，那么 TemporalFuse 的"resolving the conflict"叙事就不成立。

【3 维度打分】:

1. **Novelty: 中偏弱** — 
   核心方法论贡献（parallel GRU encoders + gating MLP + multi-horizon loss）在时间序列和多模态融合文献中是非常标准的架构。192→64→3 softmax gating 是教科书级 mixture-of-experts gate；multi-horizon loss 是 early time series classification 文献的直接搬用。Novelty 主要来自**应用领域的首次性**——第一个在 LLM 幻觉检测中做 temporal multi-signal fusion + early detection optimization。这种"first to apply X to Y"在 EMNLP 主会的 novelty 标准下通常不够强，除非应用本身揭示了领域特有的、非平凡的洞察。SpectralTrack 对 INSIDE/EigenScore 的扩展是工程改进而非概念突破。"Temporal signal importance map"是 gating 架构的自然副产品，不构成独立贡献。

2. **Significance: 中** — 
   研究问题（实时幻觉检测中的多信号融合与早期检测）具有实际重要性，practitioners 确实面临"选哪个信号"和"何时能可靠检测"的问题。但存在两个 significance 限制：(a) 如果核心发现是 positive（fusion 优于 individual signals，early detection 可行），这对多数审稿人来说是符合预期的——"更多信息 = 更好的检测"是 common sense。审稿人更可能说 "I would have guessed this" 而非 "surprising"；(b) EMNLP short paper 版本只有 1 model × 1 benchmark × 1K examples，generalizability 存疑。Temporal gate weight 分析的发现空间窄：如果 pattern 符合机制论证的预测（attention 先 → hidden states 中 → log-probs 后），则 confirmatory 而非 insightful；如果 pattern 不符合预测，则需要更多模型/数据来确认不是 artifact。

3. **Related Work: 强** — 
   覆盖面非常全面。涵盖了静态信号比较（HALUPROBE, Proxy Analyzers, krogoldAI, LLM-Check）、多信号融合（HaDeMiF, HaluNet, CHARM, ReDeEP）、单信号时序（EigenTrack, HALT, HSAD, ICR Probe）、基础工作（INSIDE/EigenScore）、流式检测（Streaming Hallucination Detection）、级联系统（HaluGate, HALL-OPT）、跨领域融合先例（MFGAN, DSAC）。差异化定位清晰：逐一与已有方法区分（static vs temporal, single vs multi-signal, complete vs early detection）。这是 proposal 最强的维度。唯一微小的遗漏是对"early time series classification"具体方法（如 TEASER, ECONOMY, CALIMERA 等）的引用不够具体，但这不影响整体评价。

【概率估计】: [18% - 30%] 中位 23%
（注：此估计针对 EMNLP 2026 主会 main track short paper；若含 Findings，上调至 [30% - 42%] 中位 35%）

【估计理由】: 
Related Work 维度强，但不影响中稿概率的上界——好的文献综述只是 table stakes。概率上界被 **Novelty** 限制：核心方法是标准时序融合架构在新领域的首次应用，EMNLP 主会审稿人对 "first to apply X to Y" 类贡献通常要求发现本身有 surprising insight，而本 proposal 的理论论证恰恰预测了最可能出现的实验结果模式，使得 "surprising finding" 的概率较低。概率下界被 **Significance** 和问题动机支撑——研究问题实际重要、gap identification 清晰、实验设计（如果执行好的话）覆盖了审稿人会期望的对比和消融。

具体推理：EMNLP 2026 短论文接收率约 ~25%。本 proposal 在动机和文献方面高于平均水平，但 novelty 低于平均水平（标准方法 + 预期结果）。如果实验结果中 temporal gate weights 揭示了 genuinely unexpected patterns（如某信号在所有时间点都 dominant，或信号权重在 hallucination vs factual 之间呈现非单调切换），可以推至 30%；如果结果 confirmatory，更接近 18-20%。

【主要风险】:
1. **"Standard method in new domain" 批评**：三条 GRU + gating MLP 在方法论上缺乏新颖性，审稿人很可能指出这是 "straightforward application of well-known temporal fusion techniques to a new problem"，尤其在 EMNLP 主会对 novelty 要求较高的背景下。
2. **核心发现大概率 confirmatory 而非 surprising**：proposal 自身的机制论证（attention=WHERE, hidden=WHAT, logprob=HOW 的流水线顺序导致时间互补性）如果被实验验证，审稿人会觉得"如预期所料"；如果没被验证，则 motivation 与结果不一致。这是一个 lose-lose framing——positive results 不 surprising，negative results 削弱 motivation。
```

Sources:
- [HaluNet: Multi-Granular Uncertainty Modeling for Efficient Hallucination Detection](https://arxiv.org/html/2512.24562)
- [Neural Message-Passing on Attention Graphs for Hallucination Detection (CHARM)](https://arxiv.org/abs/2509.24770)
- [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models (ICLR 2025)](https://openreview.net/forum?id=VwOYxPScxB)
- [Hallucination Detection via Activations of Open-Weight Proxy Analyzers](https://arxiv.org/abs/2605.07209)
- [EigenTrack: Spectral Activation Feature Tracking](https://arxiv.org/html/2509.15735v4)
- [HSAD: LLM Hallucination Detection via FFT on Hidden Layer Temporal Signals](https://arxiv.org/html/2509.13154)
- [INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection (ICLR 2024)](https://arxiv.org/abs/2402.03744)
- [Multivariate Time Series Early Classification Across Channel and Time Dimensions](https://arxiv.org/html/2306.14606)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me synthesize everything.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:
存在多个 trivial alternative 威胁：

(1) **简单拼接 + 静态分类器**: 将三种信号在每步提取后直接 concatenate，喂入一个 MLP 或 logistic regression，不需要 GRU 也不需要 gating network。Proposal 确实在 ablation 中提到了 equal-weight fusion baseline 和 static logistic regression，但这些是实验层面的对照——核心问题是：如果简单拼接已经 work，那整个 GRU + gating architecture 的 engineering overhead 换来的增量到底有多大？这一增量价值完全取决于"temporal complementarity"假设是否成立，而这个假设本身未经验证。

(2) **直接用最好的单信号时序检测器**: HALT 的 GRU on log-probs 已经证明 5M 参数的 GRU 即可取得 strong results。如果一个信号就已经 dominant（HALUPROBE 和 Proxy Analyzers 都发现 attention dominant；krogoldAI 发现 FFN dominant），那 fusion 增量可能是 marginal 的。Proposal 自己的 pilot design 也承认 r > 0.95 时 fusion 没有价值。

增量价值在于：如果 temporal complementarity 确实存在（不同信号在不同生成阶段 dominant），fusion 能实现 Pareto improvement 尤其在 early detection。但这正是未验证的前提。

(3) **Early detection 的实际需求质疑**: LLM 生成速度通常在 30-80 tokens/sec，一个 100 token 的回复约 1-3 秒。"在 25% observation 时就检测"相比"等完整回复"在实际部署中可能只节省 1-2 秒延迟。这个 practical motivation 是否足够强，审稿人可能会质疑。

【前提假设检验】:
核心 claim 的逻辑链有以下未经验证的关键假设：

(1) **Temporal complementarity 假设 [核心]**: "不同信号在不同生成阶段携带互补信息"——这是整篇论文的立论基础。Proposal 用 mechanistic interpretability 论证（WHERE/WHAT/HOW），并引用 Trajectory Commitment（44.3% 的 prompt 在第一个 token 就分叉）和 Shadows in the Attention（attention-locking 渐进出现）。但这两篇论文研究的是不同现象（residual stream trajectories vs. attention patterns），不等于证明"三种信号在同一个 generation 中有不同的 temporal profile"。这个从 mechanistic 论述到 empirical complementarity 的推理跳跃是想当然的。

(2) **"Fusion 不可能比最好单臂差"的 asymmetry 论证**: 理论上成立（gate 可以学到给一个 arm 全部权重），但在 1K examples + 5-fold CV 的小数据量下，多参数模型（~100K total）过拟合的风险是真实的。更多参数 + 更少数据 = validation performance 可能反而下降。

(3) **Static comparison 冲突源于 temporal collapsing**: Proposal 声称 HALUPROBE 和 krogoldAI 的冲突是因为都是"static snapshot"，但更可能的原因是模型差异（Llama-2 vs. Ministral-8B）、数据集差异、特征工程差异。将冲突归因于"temporal vs static"并以此作为 temporal fusion 的动机，逻辑链不够坚实。

【3 维度打分】:
1. Novelty: 【中】
   — 核心贡献是将 multivariate time series anomaly detection 中成熟的 multi-signal temporal fusion（GRU encoder + gating network）迁移到 LLM hallucination detection 领域。这是一个真实但增量的 novelty——各组件全部来自已有工作：三种信号分别源自 SinkProbe / EigenScore / HALT；GRU encoder 是标准架构；gating MLP with softmax 是经典的 attention/gating 机制；multi-horizon loss 是 early TSC 的直接适配。
   — CHARM (ICLR 2026) 已经将 attention + activation 信号融合（通过 GNN）；HaDeMiF (ICLR 2025) 已经融合 hidden states + prediction characteristics。TemporalFuse 的增量 delta 是 (a) temporal 而非 static fusion，(b) early-detection loss。这个 delta 真实存在但较窄。
   — "First temporal map of signal importance during hallucination onset" 是一个有价值的 interpretability 贡献，但属于 analysis byproduct，不是方法论创新。
   — 如果核心发现是 positive（fusion helps, especially early），审稿人的反应很可能是 "makes sense, I would have guessed this"，而不是 "surprising"。Temporal complementarity 是一个 intuitive hypothesis。

2. Significance: 【中】
   — 研究问题本身（如何融合多种内部信号做实时幻觉检测）是重要的，对实际部署 LLM guardrails 有实用价值。
   — 但 EMNLP short paper 版本的 scope 严重限制了 significance：1 model (Llama-8B)、1 benchmark (TruthfulQA)、1K examples。TruthfulQA 已经是一个相对 "dated" 的 benchmark，且它的分布较窄（factoid questions）。
   — Early detection 的 practical motivation 论证不充分（如上分析，实际延迟节省可能很小）。
   — "解决 static comparison 冲突"的 framing 有吸引力，但如前分析，冲突的真实原因可能不是 temporal vs static，而是模型/数据差异。
   — 如果 temporal complementarity 不成立（pilot 的 r > 0.95 场景），paper 退化为 negative result（"我们试了 fusion 但信号冗余"），这在 short paper format 中是可以发表的，但 impact 会大幅降低。

3. Related Work: 【强】
   — 覆盖极其全面，包含 40+ 篇近期工作，涵盖 static comparison (HALUPROBE, Proxy Analyzers, krogoldAI, LLM-Check)、foundational methods (INSIDE/EigenScore)、multi-signal fusion (HaDeMiF, HaluNet, CHARM, ReDeEP)、single-signal temporal (EigenTrack, HALT, HSAD)、streaming detection、cascaded systems、cross-modal fusion 等多个子领域。
   — 差异化定位清晰：对每个已有方法都明确指出 TemporalFuse 的差异（temporal vs static, multi-signal vs single-signal, early detection vs full-response）。
   — 对 CHARM 和 HaDeMiF 这两个最接近的竞争者的分析准确且公允。
   — 唯一潜在风险：该领域进展极快（2026 年 4-5 月就有大量新工作），到 ARR review 结束时可能有新的 overlap。

【概率估计】: [18% - 28%] 中位 23%

【估计理由】:
Novelty 维度是概率上界的主要限制因素。核心架构（GRU + gating network + multi-horizon loss）是已有技术的组合迁移，个体组件均无创新。对于 EMNLP main conference（非 Findings），即使是 short paper，审稿人也会问 "what's the conceptual contribution beyond putting known pieces together?" 
Significance 维度受限于 (a) early detection 的 practical motivation 论证不充分，(b) short paper 的实验 scope 过窄（1 model / 1 benchmark），(c) 核心发现如果 positive 并不 surprising。
Related work 是唯一强项，但好的 related work 覆盖只能保底不能拉高。

综合来看，这是一个方向正确、定位清晰、但内核偏 engineering combination 的 proposal。它更接近 "25-35% 区间的下沿"——有真实 novelty delta 但 delta 较窄，核心发现 unsurprising。考虑到 EMNLP main track 的竞争性和 short paper 的实验局限性，中位估计 23%。如果投 Findings track，概率可能提升到 30-35%。

【主要风险】:
1. **Novelty 不足以支撑 main conference**: 审稿人可能认为这是 "well-executed engineering" 而非 "scientific contribution"——将 time series domain 的 mature techniques 应用于 hallucination detection，各组件都是 off-the-shelf，无 conceptual surprise。CHARM (ICLR 2026) 和 HaDeMiF (ICLR 2025) 已经探索了 multi-signal fusion for hallucination detection，TemporalFuse 的增量 delta（temporal + early detection）可能被视为 marginal extension。
2. **核心前提假设（temporal complementarity）未经验证且可能不成立**: 如果三种信号 temporally redundant，整个 paper 的核心 narrative 崩塌。即使 proposal 设计了 dual-outcome pivot，一篇说"我们验证了信号冗余"的 short paper 在 EMNLP main track 的吸引力远低于原始 framing。
```

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:

存在两个威胁性较高的 trivial alternatives：

(1) **Simple feature concatenation + single GRU**：将三种信号在每个 step 直接拼接，送入一个 GRU，不需要三个独立编码器和 gating network。这是标准的多模态融合 baseline，实现成本极低。Proposal 虽然包含 "equal-weight fusion" 作为 ablation，但更具威胁的是 "concatenation baseline"——让单一 GRU 自己学习信号间的交互，而不是强加 gating 结构。如果 concatenation baseline 性能接近 gating fusion，则 gating 的增量价值仅限于可解释性（gate weights 可视化），而可解释性单独撑不起核心贡献。

(2) **Best single-signal temporal detector（如 HALT 或 SinkProbe + GRU）+ 简单 ensemble**：对三个独立 arm 做 logit-level averaging 或 max-pooling，无需任何 learned fusion。如果这种 trivial ensemble 接近 TemporalFuse 的性能，则 "learned adaptive fusion" 的价值被架空。

**增量价值在哪？** 如果确实存在明显的 temporal complementarity（不同阶段不同信号占优），gating 会优于静态融合。但这恰恰是需要实验验证的核心假设，而不是可以先验保证的。Proposal 意识到了这一点（pilot decision rule），但这也意味着整篇论文的核心贡献押注在一个未经验证的假设上。

【前提假设检验】:

核心逻辑链中有三个未经验证的环节：

(1) **"静态比较的分歧源于忽视了时间动态"——这是一个叙事性归因，非事实**。HALUPROBE 和 krogoldAI 的分歧可能来自：不同模型（Llama-2-7B vs. Ministral-8B）、不同数据集、不同分类器架构、不同特征工程。将分歧归因于"collapse of temporal dynamics"是 narrative convenience，而非 established fact。如果实验中 temporal gate weights 在不同阶段并不显著变化，这个叙事就会崩塌。

(2) **"Attention = WHERE, Hidden states = WHAT, Log-probs = HOW → 因此时间上互补"——这是一个看似合理但未经验证的 mechanistic story**。仅仅因为三种信号在 transformer pipeline 中位于不同位置，不代表它们在 hallucination detection 任务中携带 temporally complementary 的信息。它们可能同时反映同一个底层事件（如 knowledge retrieval failure），只是以不同的 magnitude 呈现。Pipeline 位置的不同 ≠ temporal complementarity。

(3) **"Fusion cannot underperform the best individual signal"——理论上成立但实践中不保证**。在 1K 样本、5-fold CV 的设定下，gating network（12.5K 参数）+ 三个 GRU（75K 参数）的总参数量可能导致 overfitting，使 fusion 实际 underperform 最佳单 arm。这在小数据多模态融合中是常见现象。

【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是将三种已知有效的 hallucination detection 信号通过 GRU + gating network 进行 temporal fusion，并加入 multi-horizon early-detection loss。逐项拆解：
   - GRU 建模内部信号的时间序列：HALT、EigenTrack 已做（非新）
   - 多信号融合做 hallucination detection：HaDeMiF (ICLR 2025)、HaluNet、CHARM (ICLR 2026) 已做（非新）
   - Gated fusion networks：多模态学习中的标准技术（非新）
   - Multi-horizon early-detection loss：从 early time series classification 领域迁移到 hallucination detection——这是最具新意的单点贡献，但本质是 methodology transfer 而非 methodology invention
   - Temporal signal importance map 的可解释性分析：有一定新意，但依赖于 gate weights 实际展示出有意义的时间变化模式
   
   与最相关的 5 篇近期工作（CHARM、HaDeMiF、HALT、EigenTrack、SinkProbe）对比，剔除 surface differences 后，真正剩余的 novelty delta 是："temporal fusion during generation"（vs. static fusion on complete response）+ "multi-horizon loss"。这是一个 legitimate 但 incremental 的组合创新。审稿人会认可方向的合理性，但不会认为这是一个 surprising 的 insight。

2. **Significance: 中** — 
   研究问题本身重要且实际——real-time hallucination detection 是 LLM 部署中的真实需求，"which signal, when?"是一个有价值的科学问题。然而：
   - 如果 fusion positive，审稿人的反应更可能是 "I would have guessed this"——组合多个互补信号的 learned fusion 理应优于任何单一信号，这是一个直觉上 expected 的结果
   - 如果 fusion 的提升幅度很小（如 AUROC 提升 1-2 个点），论文的核心价值转移到 interpretability analysis 上，但 gate weight 的可视化能否达到 "insight" 级别的发现，事先不确定
   - Short paper scope（1 model, 1 dataset）限制了 generalizability claim 的强度
   - 实际部署中，多信号融合的额外 latency 和实现复杂度可能使 practitioners 倾向于简单使用最好的单一信号

3. **Related Work: 强** — 
   文献覆盖非常全面，包括最新的 2026 年工作（SinkProbe、CHARM、Proxy Analyzers、SinkTrack 等）。差异化定位清晰——准确识别了 "static fusion" vs. "temporal fusion" 和 "no early detection optimization" 两个 gap。对 HaDeMiF、HaluNet、CHARM 的定位是准确的。唯一的小瑕疵是将 HALUPROBE vs. krogoldAI 的分歧过度归因于 temporal dynamics 而非 experimental confounds。

【概率估计】: [20% - 32%] 中位 25%

【估计理由】: 
Novelty 限制了上界。这是一个方向正确、文献覆盖充分的 proposal，但核心贡献是已有技术的组合创新（GRU temporal modeling + gated fusion + multi-horizon loss），而非一个 surprising insight。如果核心发现是 positive（fusion > single signal, especially early），审稿人更可能说 "reasonable and expected" 而非 "surprising"。Related Work 的强度和问题的实际重要性为概率提供了下界支撑（不太可能因为方向错误被拒），但 novelty 的 incremental 性质和 "I would have guessed this" 的风险限制了上界。作为 EMNLP main conference short paper，25% 是合理的中位估计——有机会，但需要实验结果足够 crisp 且 temporal signal importance map 展示出 genuinely surprising patterns 才有望突破上界。

【主要风险】:
1. **"I would have guessed this" 风险**：核心发现（多信号 learned fusion > 单信号）在审稿人看来可能是 expected result 而非 genuine insight，尤其当改进幅度较小时。论文的 novelty 将主要依赖 temporal signal importance map 的发现是否 surprising，这是一个不可控的风险。
2. **Trivial baseline 威胁**：如果 simple concatenation（三种特征直接拼接送入单一 GRU）或 logit-level ensemble 性能接近 TemporalFuse，则 gating network 的增量贡献被挤压到仅剩可解释性，对于 main conference 而言可能不够。
```

Sources:
- [CHARM: Neural Message-Passing on Attention Graphs for Hallucination Detection](https://arxiv.org/abs/2509.24770)
- [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models (ICLR 2025)](https://openreview.net/forum?id=VwOYxPScxB)
- [SinkProbe: Attention Sinks as Internal Signals for Hallucination Detection](https://arxiv.org/abs/2604.10697)
- [HALT: Hallucination Assessment via Log-probs as Time series](https://arxiv.org/abs/2602.02888)
- [HSAD: LLM Hallucination Detection via FFT on Hidden Layer Temporal Signals](https://arxiv.org/abs/2509.13154)
- [SinkTrack: Attention Sink based Context Anchoring (ICLR 2026)](https://arxiv.org/abs/2604.10027)
- [LapEigvals: Hallucination Detection Using Spectral Features of Attention Maps (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1239.pdf)


【原始 proposal（允许参考但不是主要依据）】:
# TemporalFuse: Adaptive Multi-Signal Temporal Fusion for Early Hallucination Detection via Learned Signal Dynamics

**状态**: 待审阅  
**级别**: top-tier  
**创建时间**: 2026-05-15T16:22:26.445444+00:00

## 描述
TemporalFuse proposes the first adaptive multi-signal temporal fusion method for early hallucination detection during autoregressive LLM generation. Unlike prior detectors that each rely on a single internal signal type — attention sinks (SinkProbe), hidden-state spectral features (EigenTrack), or log-probabilities (HALT) — and unlike prior multi-signal approaches that fuse statically on complete responses (HaDeMiF fuses hidden states + prediction characteristics via D3T/MLP; HaluNet fuses embeddings + log-likelihoods + entropy via parallel branches; CHARM combines attention and activation features via GNN) — TemporalFuse trains three parallel GRU encoders on these signal streams and introduces a cross-signal gating network that learns time-varying weights over the signal streams at each generation step. The gating MLP (192→64→3 with softmax) produces interpretable per-step weights α_t indicating which signal the model relies on at each generation stage, providing the first temporal map of signal importance during hallucination onset. The method also introduces a multi-horizon early-detection loss that optimizes detection at multiple observation fractions simultaneously (L = Σ w_f·BCE at fractions {0.25, 0.5, 0.75, 1.0}), adapting early time series classification methodology to hallucination detection for the first time — explicitly training the model to detect hallucination from partial responses. The SpectralTrack arm extends the eigenvalue-based hallucination detection paradigm established by INSIDE/EigenScore (ICLR 2024) — which showed LLMs' internal states retain hallucination-detection power via eigenvalues of hidden-state covariance matrices — from sentence-level multi-generation analysis to per-step sliding-window tracking within a single generation. The architecture uses identical GRU encoders (~25K recurrent parameters each) with per-arm linear projections (raw dims ~50–120 / ~10–20 / ~25 → common d=32), ensuring the fusion improvement reflects genuine signal complementarity rather than architectural differences. This directly addresses the unresolved conflict between static signal comparisons: HALUPROBE and Proxy Analyzers find attention dominant, krogoldAI finds FFN/hidden states dominant — TemporalFuse shows how optimal reliance varies temporally, explaining why static snapshots disagree. The framework is grounded in mechanistic interpretability: attention heads route information (WHERE), hidden states accumulate computation (WHAT), log-probs reflect confidence (HOW) — since these pipeline stages process information sequentially, they should carry temporally complementary hallucination signatures, making learned fusion the principled default. For the EMNLP 2026 short paper (ARR May 25 — the only deadline eligible for EMNLP 2026 commitment on August 2; if missed, short paper targets August 3 ARR → EACL 2027): 1 model (Llama-3.1-8B), 1 benchmark (TruthfulQA), 1K examples, demonstrating fusion outperforms individual arms especially at partial observation, with interpretable temporal signal importance analysis. Entity-match onset annotation uses objective NER-based curation (spaCy en_core_web_lg, factoid question patterns). For AAAI 2027 full paper (abstract July 21, paper July 28): adds a fourth FFN activation arm (resolving krogoldAI conflict), 3 models, 3 benchmarks, CascadeProbe extension (using learned gate thresholds for compute-adaptive escalation), and DoLa intervention. All claims supported by 5-fold stratified CV with bootstrap 95% CIs and paired permutation tests. Explicit pilot decision rule: if per-step GRU logits across all arm pairs show Pearson r > 0.95 (temporal redundancy), the contribution focuses on why signals are redundant despite carrying different static information. Total compute: ≤230 H100-hours.

## 核心问题
Real-time hallucination detection during LLM generation requires monitoring internal signals, but practitioners face two unsolved problems. First, existing detectors each rely on a single signal type — attention patterns (SinkProbe, AUROC 0.89 on HaluEval-QA), hidden-state dynamics (EigenTrack, 0.82–0.94 AUROC; HSAD via FFT), or log-probabilities (HALT via GRU) — with no principled way to combine them. Static comparisons disagree on which signal is best: HALUPROBE (arXiv 2502.13490) and Proxy Analyzers (arXiv 2605.07209) both find attention-based features dominant (attention entropy + per-head source-document attention account for 88%+ of Random Forest importance in Proxy Analyzers), while krogoldAI's empirical study finds FFN activations (82.96% accuracy, 91.04% AUC) outperform attention (79.90%, 88.46% AUC), concluding attention 'added no value beyond what FFN activations already provided.' This conflict persists because all comparisons are static — they collapse temporal dynamics into single snapshots, ignoring that different signals may carry complementary information at different generation stages. Second, and more critically, no existing method optimizes for early detection — identifying hallucination from partial responses (e.g., after only 25% of tokens are generated). Current detectors are trained and evaluated on complete responses, yet real-time guardrails must act as early as possible. Early time series classification is well-established in other domains (MultiETSC, RL-based early classifiers) but has never been applied to hallucination detection during LLM generation. These two gaps — no multi-signal temporal fusion, no early-detection optimization — mean practitioners building real-time hallucination guardrails must choose a single signal type with no principled basis, deploy a detector that cannot be trusted until generation is nearly complete, and sacrifice either accuracy (single signal) or latency (waiting for full response).

## 机遇 / Why Now
Five independent research threads converge to make adaptive temporal fusion both possible and timely. (1) Signal validation: SinkProbe (arXiv 2604.10697) established attention sinks, EigenTrack (arXiv 2509.15735) validated hidden-state spectral features, and HALT (arXiv 2602.02888) proved log-probability time series — each independently effective for hallucination detection via temporal modeling, but never combined. The foundational basis for internal-state hallucination detection was established by INSIDE (ICLR 2024), which showed that LLMs' internal states retain hallucination-detection power via EigenScore, an eigenvalue-based metric on hidden-state covariance matrices. (2) Causal grounding: SinkTrack (ICLR 2026) demonstrated that modifying attention sinks causally affects hallucination; ReDeEP (ICLR 2025) showed Knowledge FFNs and Copying Heads carry mechanistically distinct hallucination information — establishing that different signal types carry independent, non-redundant information. (3) Temporal complementarity evidence: Hallucination as Trajectory Commitment (arXiv 2604.15400) showed residual-stream trajectories bifurcate at the first generated token in 44.3% of prompts, while Shadows in the Attention (arXiv 2505.16894) found attention-locking thresholds emerge gradually — suggesting attention and hidden-state signals have fundamentally different temporal profiles, creating an opportunity for fusion. (4) Cross-modal fusion precedent: Attention-based fusion of multiple temporal signal streams is well-established in multivariate time series anomaly detection (MFGAN, DSAC) and multi-modal monitoring, but has never been applied to LLM internal signals. (5) Early classification methodology: Prefix-based multi-horizon training for time series is mature (tslearn, MultiETSC), providing the methodological foundation for optimizing detection at partial observation.

The key insight: if different signals carry complementary information at different generation stages (attention sinks as routing indicators, hidden states as computation indicators, log-probs as confidence indicators), then a learned time-varying fusion should outperform any fixed single-signal detector, and optimizing for early detection should yield faster-acting guardrails. We test this with TemporalFuse — the first adaptive multi-signal temporal fusion method for hallucination detection during autoregressive generation. The fusion architecture is the primary methodological contribution; the analysis of learned signal weights provides the first temporal comparison of signal types as an interpretable byproduct.

## 方法思路
We propose TemporalFuse, an adaptive temporal fusion method that learns time-varying weights over three internal signal streams — attention sinks, hidden-state spectral features, and log-probabilities — to detect hallucination during autoregressive generation, optimized for the earliest possible detection. The primary methodological contribution is the fusion architecture and early-detection training objective; the analysis of learned fusion weights provides the first temporal signal comparison as an interpretable byproduct.

**Theoretical Motivation: Why Fusion Should Outperform Single Signals.** The three signal types occupy different positions in the transformer's computational pipeline: attention heads function as information routing (WHERE the model reads — Wu et al., ICLR 2025), hidden states represent accumulated computation (WHAT the model has computed — FFN key-value memories, Geva et al., EMNLP 2021), and log-probabilities reflect output confidence (HOW certain the model is). Because routing decisions causally precede the computation they gate, and both precede the output distribution, these signals should carry complementary information: a routing error may appear in attention features before the residual stream incorporates erroneous information, while confidence collapse in log-probs may be the most direct indicator of hallucination once it manifests. If the signals are temporally complementary (shifting at different times and rates), learned fusion can outperform any individual signal by attending to the most informative signal at each generation stage. If they are temporally redundant, fusion still cannot underperform the best individual signal (it can learn to assign all weight to one arm). This asymmetry makes fusion the principled default.

**Architecture: Three-Arm Temporal Encoder + Cross-Signal Gating + Early-Detection Loss.**

For each generation, we extract three parallel feature streams at every decoding step t:

*Arm 1 — SinkWatch (Attention Sinks):* Per-step features from top-K informative head-layer combinations (K=5–15) identified via SinkProbe's ℓ₁-regularized analysis: sink scores for top-k sink tokens (k=2–3), sink concentration, sink entropy, context-attention ratio, plus first-order temporal derivatives. Raw dim ~50–120.

*Arm 2 — SpectralTrack (Hidden States):* Per-step spectral features from sliding-window covariance matrices of hidden-state activations: leading eigenvalues, spectral gaps, entropy, RMT statistics. This extends the eigenvalue-based hallucination detection paradigm established by INSIDE/EigenScore (ICLR 2024, Chen et al.) — which showed that eigenvalues of hidden-state covariance matrices capture hallucination-relevant semantic structure — from sentence-level multi-generation analysis to per-step sliding-window tracking within a single generation, matching EigenTrack's temporal design. Raw dim ~10–20.

*Arm 3 — LogProbTrack (Log-Probabilities):* Per-step log-probability features: token log-prob, predictive entropy, top-k probability gap, rank. Matching HALT's design. Raw dim ~25.

Each arm includes a per-arm learned linear projection to common dimension d=32, then feeds into an identical unidirectional GRU (hidden_dim=64, ~25K recurrent parameters). At each step t, the three GRU hidden states h_t^sink, h_t^spec, h_t^logp ∈ ℝ^64 represent modality-specific temporal summaries.

**Cross-Signal Gating Network (Novel Component 1).** A learned gating network dynamically weights the three signal streams at each step:
- Input: concatenation [h_t^sink; h_t^spec; h_t^logp] ∈ ℝ^192
- Gating MLP: 192 → 64 (ReLU) → 3 (softmax) → gate weights α_t ∈ ℝ^3
- Fused representation: z_t = Σ_i α_t^i · h_t^i ∈ ℝ^64
- Detection score: ŷ_t = σ(w^T z_t + b)

The gate weights α_t are directly interpretable: α_t^sink = 0.6 at step 5 means the model assigns 60% importance to attention sink features at that generation stage. By plotting mean gate weights across steps for factual vs. hallucinated generations, we obtain the first temporal map of signal importance during hallucination — the comparison result emerges as an interpretable analysis of the method. Total gating parameters: ~12.5K (negligible vs. 75K total GRU parameters).

**Multi-Horizon Early-Detection Loss (Novel Component 2).** Instead of training only on complete responses, we optimize detection at multiple observation fractions simultaneously:

L = Σ_{f ∈ F} w_f · BCE(ŷ_{T·f}, y)

where F = {0.25, 0.50, 0.75, 1.0} are observation fractions, ŷ_{T·f} is the detection score at step ⌊T·f⌋, y is the ground-truth label, and w_f = f (linear weighting — more lenient at early fractions, full weight at complete observation). This adapts early time series classification methodology (MultiETSC, RL-based early classifiers) to hallucination detection for the first time, explicitly training the model to produce informative predictions before generation is complete. The loss encourages the gating network to attend to whichever signal carries the earliest discriminative information.

**Primary Analyses (EMNLP Short Paper).** (1) Fusion vs. individual arms: AUROC/AUPRC comparing TemporalFuse against each individual arm, testing whether fusion outperforms the best single signal. (2) Early-detection curves: AUROC at observation fractions {0.10, 0.25, 0.50, 0.75, 1.0} for TemporalFuse vs. individual arms, demonstrating the benefit of multi-horizon training. (3) Temporal signal importance map: mean gate weights α_t across steps for factual vs. hallucinated generations — the first visualization of how optimal signal reliance changes during hallucination onset. This directly answers 'which signal, when?' without framing it as a standalone comparison study. (4) Static-vs-temporal ranking: comparing signal rankings from our learned gate weights against HALUPROBE's and Proxy Analyzers' static findings. (5) Ablation: TemporalFuse with/without multi-horizon loss; TemporalFuse with/without gating (equal-weight fusion baseline); individual arms with temporal GRU vs. static logistic regression.

**Statistical Rigor.** 5-fold stratified cross-validation, reporting mean ± std for all metrics. Bootstrap 95% CIs (1000 resamples) for pairwise comparisons. Paired permutation tests (10,000 permutations, p < 0.05). Cohen's d effect sizes.

**Entity-Match Onset Annotation (for temporal signal importance analysis).** For the subset of TruthfulQA used in temporal gate-weight analysis, we apply objective NER-based curation: include questions where (a) the reference answer contains ≥1 named entity detected by spaCy NER (model en_core_web_lg), AND (b) the question matches factoid patterns (starts with 'Who', 'What is/was', 'Where is/was', 'When did/was', or contains 'name of'). Onset = first generated token matching a hallucinated entity (entity not in reference, detected by NER). We supplement with NLI sliding-window annotation (window size 10 tokens, entailment threshold 0.5 via DeBERTa-v3-large-MNLI). Report agreement rate between entity-match and NLI-window onset.

**Pilot Design (First 48 hours).** 100 TruthfulQA examples on Llama-3.1-8B: extract all three feature streams, train TemporalFuse and individual arms. **Decision rule:** If all three signals are perfectly correlated temporally (Pearson r > 0.95 between per-step GRU logits across all arm pairs), fusion cannot help — pivot to analyzing why temporal dynamics are redundant despite carrying different static information. If signals show distinct temporal profiles (r < 0.85 for at least one pair), proceed with full experiments.

**Dual-Target Venue Strategy:**

*EMNLP 2026 (ARR May 25 — short paper, 4 pages):* 1 model (Llama-3.1-8B-Instruct), 1 benchmark (TruthfulQA), 1K examples. Focus: TemporalFuse method + early-detection curves + temporal signal importance map + ablations. Core claim: adaptive temporal fusion outperforms individual signals, especially at partial observation. May 25 is the only ARR submission deadline eligible for EMNLP 2026 commitment (August 2, 2026). There is no June ARR cycle — the 10-day timeline (May 15–25) is non-negotiable for EMNLP 2026. If May 25 is missed, the short paper targets the August 3 ARR cycle for commitment to EACL 2027 (commitment deadline October 11, 2026), while the full method paper proceeds to AAAI 2027 independently.

*AAAI 2027 (full paper, 8 pages, abstract deadline July 21, paper deadline July 28):* 3 models (Llama-3.1-8B, Mistral-7B-v0.3, Llama-3.1-70B), 3 benchmarks (TruthfulQA, TriviaQA, HaluEval-QA), 2K examples per pair. **Fourth arm: FFN activations** (matching krogoldAI's feature design — mean-pooled FFN outputs from informative mid-layers) to directly resolve the conflicting static evidence. Full temporal characterization, complementarity analysis, CascadeProbe extension (using learned gate thresholds as escalation triggers for compute-adaptive detection), DoLa intervention when the fused probability exceeds threshold.

**Baselines.** Single-signal temporal: individual GRU arms (SinkWatch, SpectralTrack, LogProbTrack). Static: SinkProbe, LapEigvals, TOHA. Prior temporal: EigenTrack, HALT. Online: MIND, DRIFT, PCNet. Multi-signal static: HaDeMiF-style fusion (hidden states + prediction characteristics, static), HaluNet-style parallel fusion (equal-weight concatenation of static features). Ablation: equal-weight temporal fusion (no gating), TemporalFuse without multi-horizon loss.

**Evaluation Metrics.** Primary: AUROC and AUPRC with 95% bootstrap CIs. Secondary: early-detection AUROC at partial observation fractions, F1 at calibrated threshold, latency overhead (ms/token), gate weight entropy (measuring signal specialization), Cohen's d. For AAAI: hallucination rate reduction with DoLa intervention, compute-accuracy Pareto curves for CascadeProbe.

## 研究现状
**Static signal-type comparison for hallucination detection:** HALUPROBE (arXiv 2502.13490, Feb 2025) compares attention weights, hidden-state activations, and logits with static classifiers on Llama-2-7B and Vicuna-7B, finding attention-based lookback ratio achieves highest accuracy. Proxy Analyzers (arXiv 2605.07209, May 2026) finds per-head source-document attention and attention entropy account for 88%+ of Random Forest importance across 18 features and 7 analyzer architectures. However, krogoldAI (HuggingFace blog, Dec 2025) found FFN activations (91.04% AUC) outperform attention (88.46% AUC) using Ministral-8B on 145K examples — directly contradicting both. LLM-Check (NSF 2025) also finds hidden-state methods (SAPLMA) generally outperform logit-based and attention-based methods. All comparisons are static; none model temporal dynamics during generation. **TemporalFuse resolves this conflict by showing how optimal signal reliance varies across generation stages — a signal dominant statically may not be dominant at partial observation.**

**Foundational internal-state detection:** INSIDE (ICLR 2024, Chen et al.) established the foundational principle that LLMs' internal states retain hallucination-detection power, introducing EigenScore — an eigenvalue-based metric on the covariance matrix of last-token middle-layer embeddings across multiple generations. EigenScore measures semantic consistency in the dense embedding space and achieved 80–84% AUROC across QA benchmarks. This directly informs SpectralTrack's feature design: while INSIDE operates at the sentence level across multiple generations, SpectralTrack extends eigenvalue-based features to per-step sliding-window analysis within a single generation, enabling temporal tracking.

**Multi-signal fusion for hallucination detection:** HaDeMiF (ICLR 2025, Zhou et al.) fuses hidden states (via MLP) and prediction characteristics — confidence, uncertainty, consistency — (via Deep Dynamic Decision Tree) for hallucination detection and calibration, achieving effective detection with <2% parameter overhead. However, HaDeMiF operates on complete responses with static fusion of output-space characteristics and hidden states; it does not model temporal dynamics during generation, does not incorporate attention-based signals, and does not optimize for early detection. HaluNet (arXiv 2512.24562, Dec 2025) fuses semantic embeddings, log-likelihoods, and entropy via a multi-branch architecture — but uses parallel fusion on complete responses, not learned temporal fusion during generation. ReDeEP (ICLR 2025) combines Knowledge FFN scores and Copying Head attention for RAG hallucination detection — mechanistically principled but operates on single forward passes. CHARM (ICLR 2026) applies GNNs on graphs combining attention and activation features — static aggregation, no temporal modeling. UniFact (arXiv 2512.02772) benchmarks hidden-state and logit methods but does not fuse signals. **No prior work — including HaDeMiF, HaluNet, and CHARM — learns time-varying weights over multiple signal types during autoregressive generation or optimizes for early detection at partial observation.**

**Single-signal temporal/trajectory detection:** EigenTrack (arXiv 2509.15735) tracks hidden-state spectral dynamics via GRU (0.82–0.94 AUROC). HALT (arXiv 2602.02888) treats log-probs as time series via bidirectional GRU. HSAD (arXiv 2509.13154) applies FFT to cross-layer hidden-state activations. Step-Level Hidden-State Transport Geometry (arXiv 2605.13772) uses BiLSTM on hidden-state geometric features. ICR Probe (ACL 2025) tracks cross-layer hidden-state evolution. **Each validates temporal modeling for one signal type; none combine multiple signals or optimize for early detection.**

**Streaming and temporal hallucination detection during generation:** Streaming Hallucination Detection (arXiv 2601.02170, Lu et al.) also models hallucination as temporally evolving during generation, treating step-level hallucination judgments as local observations and introducing a cumulative prefix-level signal that tracks the global evolution of the reasoning state. However, it uses external NLI judges on chain-of-thought reasoning steps rather than fusing internal signal streams — a fundamentally different signal source (external model judgments vs. internal activations), different task domain (long CoT reasoning vs. factual QA generation), and different method (cumulative NLI scoring vs. learned multi-signal temporal fusion). TemporalFuse shares the temporal framing but addresses the complementary problem of fusing multiple internal signals for factual QA, without requiring external judges.

**Cascaded/adaptive detection systems:** HaluGate (vLLM blog, Dec 2025) implements a three-stage cascade (Sentinel binary classifier → token-level detector → NLI explainer) achieving 72.2% query skip rate — but cascades at the query-type level using external signals, not across internal signal types. HALL-OPT (Nature Scientific Reports 2026) combines dual-stream attention detection with adaptive token pruning — but streams are parallel, not sequentially gated. Monitoring Decoding (ACL Findings 2025) gates expensive correction based on cheap monitoring — gates mitigation, not detection depth. Energy-efficient speculative decoding (arXiv 2508.12590) filters tokens for expensive verification using attention-weight statistics and uncertainty — the closest paradigm to our approach but applied to speculative decoding, not hallucination detection. **No prior work cascades across internal signal types (attention → hidden states → log-probs) with learned escalation for hallucination detection.**

**Cross-modal temporal fusion in other domains:** Attention-based fusion of multiple temporal signal streams is well-established in multivariate time series anomaly detection (MFGAN, DSAC), video anomaly detection, and industrial monitoring. These provide architectural precedent for our cross-signal attention mechanism but have never been applied to LLM internal signals.

**The open gaps:** (1) No method fuses multiple internal signal types with learned temporal weighting during generation — existing fusion is static (HaDeMiF, HaluNet, CHARM, ReDeEP) or external (HaluGate). (2) No method optimizes for early detection at partial observation fractions — all detectors are trained on complete responses. (3) No analysis shows how optimal signal reliance changes during generation — static comparisons collapse temporal dynamics. TemporalFuse addresses all three.

## 目标 Venue
- EMNLP 2026 (primary short-term target — ARR May 25, 2026, the only submission deadline eligible for EMNLP 2026 commitment on August 2, 2026; 4-page short paper focusing on TemporalFuse method, early-detection curves, and temporal signal importance analysis; Findings track acceptable; if missed, short paper targets August 3 ARR → EACL 2027 commitment October 11, 2026)
- AAAI 2027 (primary long-term target — abstract deadline July 21, paper deadline July 28, 2026; full 8-page method paper with 4 signal arms including FFN, multi-model evaluation, CascadeProbe extension, intervention experiments)
- ICLR 2027 (fallback — deadline expected ~October 2026; allows additional experiments if AAAI timeline requires descoping)

## 关键参考
- What are Models Thinking about? Understanding Large Language Model Hallucinations 'Psychology' through Model Inner State Analysis [HALUPROBE] (arXiv 2502.13490, Feb 2025)
- Hallucination Detection via Activations of Open-Weight Proxy Analyzers [Proxy Analyzers] (arXiv 2605.07209, May 2026)
- Towards Unification of Hallucination Detection and Fact Verification for Large Language Models [UniFact] (arXiv 2512.02772, Dec 2025)
- Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models [SinkProbe] (arXiv 2604.10697, April 2026)
- EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs (arXiv 2509.15735, 2025)
- HALT: Hallucination Assessment via Log-probs as Time series (arXiv 2602.02888, Feb 2026)
- Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models [MIND] (ACL Findings 2024, arXiv 2403.06448)
- LLM Hallucination Detection: A Fast Fourier Transform Method Based on Hidden Layer Temporal Signals [HSAD] (arXiv 2509.13154, Sep 2025)
- HaluNet: Multi-Granular Uncertainty Modeling for Efficient Hallucination Detection in LLM Question Answering (arXiv 2512.24562, Dec 2025)
- ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability (ICLR 2025, arXiv 2410.11414)
- HaDeMiF: Hallucination Detection and Mitigation in Large Language Models (ICLR 2025, OpenReview VwOYxPScxB, arXiv 2601.09929)
- INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection [EigenScore] (ICLR 2024, arXiv 2402.03744)
- Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation (arXiv 2604.15400, April 2026)
- Before the First Token: Scale-Dependent Emergence of Hallucination Signals in Autoregressive Language Models (arXiv 2604.13068, April 2026)
- Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)
- Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs (arXiv 2505.16894, May 2025)
- HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders (arXiv 2604.16430, April 2026)
- Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)
- Uncertainty-Aware Attention Heads: Efficient Unsupervised Uncertainty Quantification for LLMs [RAUQ] (arXiv 2505.20045, May 2025)
- Hallucination Detection in LLMs with Topological Divergence on Attention Graphs [TOHA] (ACL 2026, arXiv 2504.10063)
- SinkTrack: Attention Sink based Context Anchoring for Large Language Models (ICLR 2026, arXiv 2604.10027)
- FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG (arXiv 2601.05866, Jan 2026)
- First Hallucination Tokens Are Different from Conditional Ones (arXiv 2507.20836, 2025)
- Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)
- ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs (ACL 2025, arXiv 2507.16488)
- Real-Time Detection of Hallucinated Entities in Long-Form Generation (arXiv 2509.03531, 2025)
- Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation (arXiv 2604.10098, April 2026)
- Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNet/PC-LDCD] (arXiv 2605.05953, May 2026)
- DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)
- Hallucination Detection in LLMs Using Spectral Features of Attention Maps [LapEigvals] (EMNLP 2025, arXiv 2502.17598)
- Neural Message-Passing on Attention Graphs for Hallucination Detection [CHARM] (ICLR 2026, arXiv 2509.24770)
- Spectral Guardrails for Agents in the Wild: Detecting Tool Use Hallucinations via Attention Topology (arXiv 2602.08082, Feb 2026)
- AggTruth: Contextual Hallucination Detection using Aggregated Attention Scores in LLMs (ICCS 2025, arXiv 2506.18628)
- Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, Jan 2026)
- Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (ACL Findings 2025, arXiv 2503.03106)
- DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models (ICLR 2024)
- Detecting Contextual Hallucinations in Large Language Models with Frequency-Aware Attention (arXiv 2602.18145, Feb 2026)
- Mirage in the Eyes: Hallucination Attack on Multi-modal Large Language Models with Only Attention Sink (USENIX Security 2025, arXiv 2501.15269)
- Retrieval Head Mechanistically Explains Long-Context Factuality (Wu et al., ICLR 2025)
- Transformer Feed-Forward Layers Are Key-Value Memories (Geva et al., EMNLP 2021)
- HaluGate: Token-Level Truth — Three-Stage Conditional Hallucination Detection Pipeline (vLLM Blog, Dec 2025)
- HALL-OPT: Hallucination-Aware Learning and Latency Optimization Transformer for Real-Time Edge Intelligence (Nature Scientific Reports, 2026)
- LLM-Check: Investigating Detection of Hallucinations in Large Language Models (NSF, 2025)
- krogoldAI: LLM Hallucination Detection via Internal Representations (HuggingFace Blog, Dec 2025)
- Energy-Efficient Speculative Decoding with Uncertainty-Awareness and Adaptive Token Filtering (arXiv 2508.12590, 2025)

## 资源估算
### auto_research
- **claude_api_cost**: $320–530 (~3200–5300 turns).
- **estimated_gpu_cost**: $575–690.
- **gpu_hours**: ~230h H100 total.
- **gpu_utilization**: High (~80%+).
- **speed_bottleneck**: Bottlenecked by eager-mode attention extraction (~3–4× slower than standard inference). 1K examples × ~100 tokens ≈ 10–15h on single H100, parallelizable. The gating network and multi-horizon loss add negligible training overhead.
- **team**: 0 (initial setup + final review only)
- **timeline**: EMNLP: 7–8 days. AAAI: 3 additional weeks.

### human_in_loop
- **claude_api_cost**: $220–380 (~2200–3800 turns).
- **estimated_gpu_cost**: $525–630.
- **gpu_hours**: ~210h H100 total.
- **gpu_utilization**: Moderate-high (~60–70%).
- **risk_note**: Primary risk: signals may be temporally redundant (fusion ≈ best individual arm). Mitigation: (1) pilot correlation check in first 48 hours — if r > 0.95 across all pairs, shift focus to understanding why; (2) even if fusion margin is small, the early-detection curves and temporal signal importance maps are novel contributions independent of fusion magnitude; (3) the multi-horizon loss may still improve individual arms. Secondary risk: the 10-day EMNLP timeline is aggressive and non-negotiable — May 25 is the only ARR submission deadline for EMNLP 2026 commitment (August 2). There is no June ARR cycle; the next cycle after May 25 is August 3, which can only commit to EACL 2027 (October 11 commitment deadline). Mitigation: (1) short paper scope (1 model, 1 benchmark) is tractable in 10 days; (2) fusion architecture adds minimal implementation overhead (~200 lines on top of three arms); (3) if EMNLP is missed, the short paper targets August 3 ARR → EACL 2027, while the full method paper proceeds to AAAI 2027 (July 28 paper deadline) independently — both venue paths remain viable. Tertiary risk: entity-match onset annotation unreliable. Mitigation: NER-based curation criteria are objective and reproducible; NLI sliding-window supplement provides independent validation; TriviaQA added as primary onset benchmark in AAAI version.
- **team**: 1 researcher, ~60min/day for EMNLP sprint, ~45min/day for AAAI
- **timeline**: EMNLP: 10 days (May 15–25, non-negotiable for EMNLP 2026; fallback: August 3 ARR → EACL 2027). AAAI: 8 additional weeks.

### manual
- **estimated_gpu_cost**: $475–570
- **gpu_hours**: ~190h H100 total. EMNLP short paper: ~52h (feature extraction for 3 arms × 1K examples on Llama-8B: ~20h; GRU + fusion training with 5-fold CV: ~10h; baselines including HaDeMiF-style and HALUPROBE-style: ~12h; curated subset annotation + analysis: ~6h; pilot: ~4h). AAAI full paper (incremental): ~138h additional (multi-model extraction: ~60h; 70B experiments: ~20h; 4th FFN arm: ~12h; CascadeProbe extension: ~8h; extended baselines + DoLa intervention: ~20h; additional CV + ablations: ~18h).
- **gpu_utilization**: Moderate (~50–60%).
- **team**: 1–2 researchers
- **timeline**: EMNLP short paper: 10 days (May 15–25). This timeline is non-negotiable — May 25 is the only ARR deadline eligible for EMNLP 2026. If missed, the short paper shifts to the August 3 ARR cycle targeting EACL 2027. AAAI full paper: additional 8 weeks (May 25–July 21).



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4427c25e-867b-4627-9935-f8f996e85172",
  "type": "user",
  "uuid": "6e5cf138-66ea-4b9e-9656-7f33d9119863",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T01:54:30.176Z_

```json
{
  "parentUuid": "6e5cf138-66ea-4b9e-9656-7f33d9119863",
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
  "uuid": "9e220e22-47ca-4cdc-9864-0255efc98ff1",
  "timestamp": "2026-05-16T01:54:30.176Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T01:54:30.176Z_

```json
{
  "parentUuid": "9e220e22-47ca-4cdc-9864-0255efc98ff1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4941958a-7dd1-4db5-b8bc-04cfeb8a4bb8",
  "timestamp": "2026-05-16T01:54:30.176Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information to make my assessment. Let me sy…",
  "leafUuid": "4941958a-7dd1-4db5-b8bc-04cfeb8a4bb8",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge: Synthesize three hallucination detection reviews",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11"
}
```

---

### Assistant

_source line 8 · 2026-05-16T01:54:55.201Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them as the Meta Judge.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 中偏弱
- Significance: 中
- Related Work: 强
- Probability: [18% - 30%] 中位 23%

**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [18% - 28%] 中位 23%


**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [20% - 32%] 中位 25%

Looking at the three median probabilities of 23%, 23%, and 25%, the mean comes to about 23.67% with a median of 23% and very low standard deviation around 1.15%, indicating strong consistency across reviewers. Now I'm identifying where the reviewers align and where they diverge.

There's clear consensus across all three reviewers on several critical dimensions: novelty is uniformly incremental with no surprising insights, significance is consistently moderate, and related work coverage is strong. They all flag the same core vulnerabilities—a trivial baseline of simple concatenation with a single GRU poses a major threat, the temporal complementarity assumption remains unverified, and the attribution of results to temporal dynamics rather than model or data confounds feels like narrative convenience. All three also note that positive results would be largely expected and confirmatory, and they identify fusion overfitting as a risk given the small dataset of 1K samples. The multi-horizon loss being independent of the fusion mechanism is another point of concern raised.

A few points stand out as individual observations: Reviewer 1 rates novelty slightly lower than the others, Reviewer 2 uniquely questions whether the practical value of early detection—saving 1-2 seconds of latency—justifies the added complexity, and Reviewer 1 articulates a sharp "lose-lose" framing where positive results confirm expectations while negative results undermine the paper's motivation. What's striking is the numerical convergence—the three reviewers' overall scores cluster tightly around 23-25% with minimal variance, and their rubric assessments are nearly identical despite approaching from different angles. This level of agreement is genuinely rare.

The consensus is clear: novelty acts as the hard ceiling, the related work section is solid but can't compensate for the limited novelty, the core premise lacks validation, and the results would likely feel predictable. Given this consistency and the principle of not being more lenient than the most generous reviewer, I'll anchor the final score around 23% with a tight confidence band. Now I need to pull together the implementation assessment based on what the proposal estimates for resources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4941958a-7dd1-4db5-b8bc-04cfeb8a4bb8",
  "isSidechain": false,
  "requestId": "req_011Cb5QzCiy7ZUgrJt4rwLD5",
  "type": "assistant",
  "uuid": "668bef75-673b-42b3-a038-586a8b973ac7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8Pxyt8m3Y6Bt5sSf3hmrJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23698,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3254,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23698
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

_source line 9 · 2026-05-16T01:55:51.358Z_

【阶段】: Meta Judge
【三次中位】: [23%, 23%, 25%]  std=1.2%
【共识维度】:
- **Novelty = 中（3/3）**：三位审稿人一致认定核心架构（GRU encoder + gating MLP + multi-horizon loss）是已有成熟技术的组合迁移，非方法论创新。Reviewer 1 进一步细化为"中偏弱"，但本质判定一致：增量 delta 真实但狭窄，属于 "first to apply X to Y" 而非 conceptual breakthrough。
- **Significance = 中（3/3）**：研究问题实际重要，但三位均指出 (a) positive results 大概率 confirmatory（"I would have guessed this"），(b) short paper scope（1 model / 1 benchmark / 1K examples）严重限制 generalizability claim。
- **Related Work = 强（3/3）**：覆盖全面、差异化定位清晰，是 proposal 最强维度，但三位均明确"好的 related work 只是 table stakes，不拉高概率上界"。
- **Trivial alternative 威胁严重（3/3）**：三位不约而同指出"简单拼接 + 单 GRU"是最大威胁——如果该 baseline 性能接近 TemporalFuse，gating network 的增量贡献被挤压至仅剩可解释性。
- **核心前提（temporal complementarity）未经验证（3/3）**：三位均认为"三类信号具有时间互补性"是整篇论文的立论基础，但完全未经验证，且 mechanistic 论证（WHERE/WHAT/HOW）存在从步内到步间时间尺度的推理跳跃。
- **Static comparison 冲突归因有问题（3/3）**：三位均指出将 HALUPROBE vs. krogoldAI 分歧归因于"temporal collapse"是 narrative convenience，更 parsimonious 的解释是模型/数据/特征差异。
- **Positive results = confirmatory 风险（3/3）**：如果 fusion 确实优于单信号，审稿人反应更可能是"如预期"而非"surprising"。

【异常维度】:
- Reviewer 1 独有的"lose-lose framing"论述（positive 不 surprising，negative 削弱 motivation）——洞察敏锐，但其他两位未明确以此结构表述，降权处理（不影响最终概率，但作为风险备注保留）。
- Reviewer 2 独有的"early detection 实际延迟节省质疑"（LLM 生成 100 token 仅需 1-3 秒，25% observation 只节省 1-2 秒）——有道理但属于 practical deployment 层面的次要论点，降权处理。
- Reviewer 1 独有的"multi-horizon loss 独立于 fusion 架构"分离性论述——逻辑正确（两个 Novel Component 实际独立而非协同），但其他两位未展开讨论，降权处理（但对 novelty 评估有辅助参考价值）。
- Reviewer 2 独有的"过拟合风险"明确量化论述（100K total params vs. 1K examples）——Reviewer 3 也提及但不如 R2 详细，属于中等信号。

【最终概率】: [18% - 28%] 中位 23%
【一致性】: 高（std=1.2%，三份评审在 rubric 判决和概率区间上高度收敛）
【综合理由】:

三份评审展现出罕见的高度一致性：rubric 三维度判定完全相同（中/中/强），概率中位仅差 2 个百分点，核心风险识别几乎完全重叠。这使得综合判断的置信度很高。

**概率上界（28%）由 Novelty 决定**：三位一致认为核心架构是标准时序融合技术的领域迁移，CHARM (ICLR 2026) 和 HaDeMiF (ICLR 2025) 已在 hallucination detection 中探索多信号融合。TemporalFuse 的增量 delta（temporal 而非 static + early detection loss）真实但窄。如果实验中 temporal gate weights 揭示出 genuinely unexpected patterns，可触及 28%；但 proposal 自身的理论论证恰恰预测了最可能出现的 pattern，降低了 surprise 概率。

**概率下界（18%）由问题本身的实际重要性支撑**：研究方向正确、gap identification 清晰、实验设计覆盖了审稿人期望的对比和消融。不太可能因方向问题被 desk reject。但 trivial alternative 威胁和核心前提不成立的风险压低了下界。

**中位取 23%**：三位中位的简单中位恰好是 23%，且高一致性下无需做额外调整。这反映了"方向正确、执行可靠、但内核偏 engineering combination"的典型 profile——略低于 EMNLP short paper ~25% 的平均接收率，因为 novelty 低于平均水平抵消了 related work 高于平均水平的优势。

**处理异常**：Reviewer 1 的"中偏弱" Novelty 评级和"lose-lose framing"是三份中最严格的，但其概率中位（23%）与 R2 一致，说明即使 Novelty 评级略低也未导致概率大幅偏离——该异常不影响最终综合。Reviewer 3 略高的中位（25%）在高一致性下被视为正常波动，不做上调。

【建议】: 不推荐（EMNLP 2026 主会 main track）；边缘偏下（若接受 Findings track，估计可上调至 [28%-38%] 中位 33%）

【实施评估】:
- **计算资源**: EMNLP short paper 约 52h H100（特征提取 ~20h，GRU+fusion 训练含 5-fold CV ~10h，baselines ~12h，分析 ~6h，pilot ~4h）；AAAI full paper 额外 ~138h H100（主要瓶颈在 70B 模型推理和多模型特征提取）。总计 ≤230h H100，GPU 成本约 $475-690。Eager-mode attention 提取是速度瓶颈（~3-4× slower than standard inference）。
- **数据需求**: TruthfulQA（公开可得）1K examples（EMNLP）；AAAI 追加 TriviaQA、HaluEval-QA，均公开可得。无需私有数据。
- **人工介入**: Entity-match onset annotation 使用 spaCy NER 自动化（en_core_web_lg），NLI sliding-window 用 DeBERTa-v3-large-MNLI 补充。人工介入量低：1 researcher ~60min/day（EMNLP sprint 10 天），~45min/day（AAAI 8 周）。无需大规模人工标注。
- **训练需求**: 需要训练轻量级模型——三个 GRU encoder（各 ~25K params）+ gating MLP（~12.5K params），总计 ~100K 参数。训练数据仅 1K examples（EMNLP），5-fold CV。训练时间短（~10h H100 含 CV）。**不需要**训练或微调 LLM 本身（Llama-3.1-8B 仅用于推理提取特征）。
- **新 Benchmark**: 不需要构建全新 benchmark。使用现有 TruthfulQA，但需要自建 entity-match onset annotation pipeline（基于 spaCy NER + 规则匹配，工程量中等）。
- **预估周期**: EMNLP short paper: 10 天（May 15-25，时间线极其紧张且不可协商）；AAAI full paper: 额外 8 周。从启动到 EMNLP 可投稿的窗口仅 10 天，存在时间风险但 scope 可控（1 model / 1 benchmark / 1K examples + 轻量级模型训练）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "668bef75-673b-42b3-a038-586a8b973ac7",
  "isSidechain": false,
  "requestId": "req_011Cb5QzCiy7ZUgrJt4rwLD5",
  "type": "assistant",
  "uuid": "18a04be0-34a7-4765-9f6f-92817ab7a7af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8Pxyt8m3Y6Bt5sSf3hmrJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23698,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3254,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23698
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information to make my assessment. Let me sy…",
  "leafUuid": "18a04be0-34a7-4765-9f6f-92817ab7a7af",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge: Synthesize three hallucination detection reviews",
  "sessionId": "0a60b288-4ced-4f7c-beaf-00a80a176b11"
}
```

---
