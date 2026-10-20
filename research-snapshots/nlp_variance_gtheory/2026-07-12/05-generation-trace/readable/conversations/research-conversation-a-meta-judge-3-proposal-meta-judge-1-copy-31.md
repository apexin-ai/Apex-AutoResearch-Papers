# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/70128e95-59eb-4945-b0d3-37d8856228c9.jsonl`
- **Structured JSON:** [`f9a6b3e4884dcfb3afb4.json`](../../sessions/f9/f9a6b3e4884dcfb3afb4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:46:49.262Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:46:49.262Z",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct my assessment. Let me compile the triage evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Yuan et al., arXiv 2605.09502] (May 2026): \"Hidden Error Awareness: The Signal Is Diagnostic, Not Causal.\" 线性 probe 在 correctness 上达到 0.95 AUROC，但四种 causal intervention（activation steering、probe-guided best-of-N、self-correction、activation patching）全部失败。这是本 proposal 的核心动机来源——\"diagnostic-not-causal gap\"概念直接源自此文。论文已确认存在，描述准确。\n- [Cox et al., arXiv 2603.01437] (Mar 2026): \"Decoding Answers Before CoT.\" Pre-CoT probes 在 instruction-tuned 模型上达到 >0.9 AUC，steering flip rate >50%；但在 reasoning model (GPT-OSS-20B) 上 steering 失败。与 Yuan et al. 互相独立地确认了 diagnostic-causal gap。描述准确。\n- [Chrabąszcz et al., arXiv 2605.18549] (May 2026): \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics.\" 提取 60+ signal-processing features（volatility, trend, steady-state 等），max-pooling 达到 91-97% AUROC，比 static probes 提高 17pp。这是 probe trajectory 方向最接近的 concurrent work。关键差异：**没有 causal contribution 组件**、没有 gap metric、没有 calibration、没有 phenomenon taxonomy。描述准确。\n- [Wang, arXiv 2604.15726] (Apr 2026): \"LLM Reasoning Is Latent, Not the Chain of Thought.\" 形式化了 H1（latent-mediated）/ H2（CoT-mediated）/ H0（serial compute）三个竞争假说。本 proposal 声称 ICG 框架可以在每个 token position 区分 H1 vs H2。论文已确认存在。\n- [Ballon et al., arXiv 2601.23163] (Jan 2026): \"Probing the Trajectories of Reasoning Traces.\" Truncation-reinjection 协议，在 decile intervals 测量 accuracy 变化，三个 control conditions 验证 sequential content matters。这是 C(t) 的方法论基础。论文已确认，描述准确。\n- [Gjølbye et al., arXiv 2605.15454] (May 2026): \"Reasoning Models Don't Just Think Longer, They Move Differently.\" 研究 hidden-state trajectory geometry，发现 difficulty 与 trajectory geometry 的 coupling 在 length correction 后仍然存在，但 domain-specific（code: ρ⊥=+0.41, math: +0.05）。描述准确。\n- [CMI framework, arXiv 2602.03994] (Feb 2026): Layerwise causal audit，只在 ~50 examples 上测试，无 temporal resolution。确认存在。\n- [Kudo et al., EACL 2026]: Per-position probes + activation patching on synthetic arithmetic. 确认 CoT faithful for arithmetic but synthetic setting. 确认存在。\n- 未发现任何已发表工作提出 \"Information-Contribution Gap\" 或等价的 probe trajectory + causal contribution temporal dual-estimator framework。proposal 声称的 \"no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline\" 在我的调研范围内成立。\n\n- 调研总结: CoT faithfulness 领域在 2025-2026 年经历了爆发式增长。Probe-based 诊断（Yuan, Cox, David, Zhang, Esakkiraja, Chrabąszcz）和 causal contribution 测量（Ballon, Ye/NLDD, Zhao/TTS, CMI）两条线已经各自成熟，但确实没有人将两者 temporally 结合。本 proposal 定位在两条线的交汇处，gap 是真实的。然而，这个交汇点是一个 \"obvious next step\"——领域内任何关注这两条线的人都能看到这个方向。\n\n【Trivial Alternative 检验】:\n存在若干更简单的替代方案：\n\n(1) **单点 gap 而非 temporal trajectory**: 只比较 pre-CoT probe accuracy 与 final answer accuracy 的差值作为 faithfulness proxy。不需要 temporal resolution，不需要 C(t) 的多种估计方法。这能捕获最核心的 \"model knows but doesn't use\" 信号。增量价值：temporal trajectory 提供的 phenomenon fingerprinting 是唯一辩护，但 phenomenon fingerprinting 本身是未经验证的假说。\n\n(2) **只用 Chrabąszcz et al. 的 probe trajectory + accuracy-based heuristic**: 对比 probe trajectory shape 与最终正确/错误，不需要 causal contribution estimation。如果只是区分 \"faithful\" vs \"unfaithful\"，probe trajectory alone 可能就够了。增量价值：加入 C(t) 维度理论上能区分 \"model knows and uses CoT\" 和 \"model knows but CoT is decorative\"，但这一区分能否被 probe trajectory shape alone 近似捕获是开放问题。\n\n(3) **直接用 Ballon et al. 的 truncation accuracy curve + pre-CoT probe accuracy**: 不需要构建完整的 G*(t) 框架，只需两个测量取差值。\n\n**增量价值的关键辩护**在于 phenomenon taxonomy 的可区分性——如果 G*(t) 确实能 fingerprint 不同的 unfaithfulness 模式，这比上述 trivial alternatives 有质的提升。但如果 phenomenon 不可区分（Phase 0b 失败），框架退化为一个 characterization tool，其增量价值相对 trivial alternatives 变得微薄。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中存在以下未经验证的假设：\n\n(1) **P*(t) 和 C(t) 的可减性（commensurability）**：这是最严重的未检验假设。P*(t) 是 calibrated AUROC（分类器性能指标，[0,1]），C(t) 由三种方法估计：prefix truncation 给出 accuracy change、paraphrase perturbation 给出 stability score、NLDD 给出 logit degradation。这三者的 scale、分布特性完全不同，也都与 AUROC 不在同一度量空间。G*(t) = P*(t) − C(t) 的减法在数学上是什么含义？proposal 完全没有讨论如何将这些异质测量统一到同一 scale。如果 gap 的数值意义不明确，整个 phenomenon fingerprinting 就缺乏坚实基础。\n\n(2) **Phenomenon 离散可分假设**：proposal 假设 pre-CoT encoding、genuine reasoning、post-hoc rationalization 是离散类别，且在 G*(t) 空间中形成可区分的 clusters。但实际上，单个 reasoning trace 可能同时包含多种模式（前半段 genuine reasoning，后半段 post-hoc rationalization），且不同模式之间可能是连续谱而非离散类别。Phase 0b 的 d > 0.5 threshold 设定也相对宽松（effect size 0.5 在心理学中只是 medium effect）。\n\n(3) **Probe calibration 的充分性**：null-probe calibration（P*(t) = P(t) − P_null(t)）假设 inflation 是 additive 的。但 Chun et al. 的 MCT 工作已经表明 probe accuracy 与 geometric separability 的关系是非线性的——probe accuracy 可以在 geometric separability 消失后保持高位。简单减法可能无法正确 calibrate。\n\n(4) **Post-hoc rationalization 的 \"widening gap\" 预测**：proposal 预测 post-hoc rationalization 表现为 \"G*(t) starts moderate, rises during CoT\"，但同时引用 David 的数据显示 P*(t) 在 t=4 后稳定在 ~0.80。如果 P*(t) 稳定而 C(t) flat，gap 是常数而非 widening。要 widening 需要 C(t) 下降，但 post-hoc rationalization 中 C(t) 没有理由下降。这个具体预测的逻辑链有缺陷。\n\n【3 维度打分】:\n  1. Novelty: 【中】 — 核心 idea \"将 probe trajectory 和 causal contribution 联合 track 为 temporal dual-estimator gap\" 在技术层面是新的——调研确认 Chrabąszcz et al. 只有 probe side，Ballon et al. 只有 causal side，CMI 无 temporal resolution。然而，这属于 \"synthesis novelty\"：每个组件（temporal probing, causal contribution estimation, calibration）都已存在，组合方式是领域发展的 obvious next step。The conceptual insight \"the gap IS the phenomenon\" 已经隐含在 Yuan et al. 和 Cox et al. 的讨论中——本 proposal 的贡献是 formalize 和 operationalize，而非 discover。Phenomenon taxonomy 的 fingerprinting 如果成功会增加 novelty，但这是未验证的假说。此外，commensurability 问题（P*(t) 和 C(t) 的 scale 不一致）使得 \"gap\" 的 formalization 本身并不如表面看起来那么 clean。\n\n  2. Significance: 【中-强】 — 研究问题本身——CoT faithfulness 的 temporal dynamics——是 NLP/AI safety 领域的核心问题之一，2025-2026 年有大量关注。如果 framework 成功，它将提供：(a) instance-level faithfulness diagnostic（实用价值），(b) 对不同 unfaithfulness 模式的分类学（理论贡献），(c) 对 \"when does CoT add value\" 的实证回答（practical guidance）。Difficulty conditioning 部分有独立价值。然而，如果 Phase 0b 显示 phenomenon 不可区分，论文的 impact 大幅下降，退化为 \"we measured G*(t) and it varies\"——这在一个已有大量 characterization 工作（David, Zhang, Esakkiraja, Chrabąszcz）的领域中增量有限。\n\n  3. Related Work: 【强】 — 这是本 proposal 最强的维度。覆盖了 30+ 篇 2024-2026 年的相关工作，包括所有主要方向（probe-based measurement, causal intervention, temporal dynamics, trajectory geometry, calibration, faithfulness taxonomy）。与最接近的 concurrent work（Chrabąszcz et al.）的差异化定位清晰且有说服力。引用的关键论文经调研确认真实存在且描述准确。对 CMI, Kudo et al., TTS 等 probe+intervention 组合工作的定位合理。唯一的小瑕疵：对 Hewitt & Liang (2019) 和 Voita & Titov (2020) 的 calibration 文献引用是准确的，但 null-probe calibration 方案本身在技术层面存在可质疑性（如前述 additive assumption）。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \nNovelty 是限制上界的主要因素。核心 idea 是一个 well-executed synthesis，但不是一个 surprising insight。如果审稿人问 \"if the core finding is positive, would I be surprised?\"，答案大概率是 \"No, I would have guessed that pre-CoT encoding shows high gap while genuine reasoning shows converging gap\"——这些预测本身是直觉性的。Significance 将上界推高（重要问题 + 实用价值），Related Work 的 thoroughness 提供了坚实的 positioning 基础。但 commensurability 问题（P*(t) 和 C(t) 的 scale 不一致）是一个可能让审稿人直接质疑 framework soundness 的技术漏洞。Phenomenon separability 假说增加了 upside potential（如果成功，novelty 升至中-强），但也增加了 downside risk（如果失败，论文核心 narrative 被削弱）。综合来看，这是一篇 \"solid framework/analysis paper\"，在 EMNLP 的 interpretability/analysis track 有竞争力但并非突出。\n\n【主要风险】: \n1. **Commensurability 缺陷**: G*(t) = P*(t) − C(t) 将不同度量空间的量相减，审稿人几乎必然会质疑这一形式化的数学意义。如果无法令人信服地解释 AUROC − (accuracy change / stability / logit degradation) 的含义，framework 的核心 formalization 就站不住脚。这是 idea 层面的风险，不仅仅是实验设计问题。\n2. **\"Obvious next step\" 的 novelty 挑战**: 在一个 Chrabąszcz et al. 已做 probe trajectory、Ballon et al. 已做 causal trajectory、Yuan et al. 已指出 diagnostic-not-causal gap 的领域，将三者组合是自然推论。审稿人可能认为 novelty 在于 execution 而非 idea，而 execution 层面的 novelty（calibration, Phase 0b pilot, difficulty conditioning）可能不足以撑起一篇顶会论文的 contribution bar。\n```\n\nSources:\n- [Yuan et al. - Hidden Error Awareness](https://arxiv.org/abs/2605.09502)\n- [Cox et al. - Decoding Answers Before CoT](https://arxiv.org/abs/2603.01437)\n- [Chrabąszcz et al. - Probe Trajectories](https://arxiv.org/abs/2605.18549)\n- [Wang - LLM Reasoning Is Latent](https://arxiv.org/abs/2604.15726)\n- [Ballon et al. - Probing Trajectories of Reasoning Traces](https://arxiv.org/abs/2601.23163)\n- [Gjølbye et al. - Reasoning Models Move Differently](https://arxiv.org/abs/2605.15454)\n- [CMI Framework - Bypassing the Rationale](https://arxiv.org/abs/2602.03994)\n- [FaithCoT-Bench - ICLR 2026](https://arxiv.org/abs/2510.04040)\n- [Ye et al. - Mechanistic Evidence for Faithfulness Decay](https://arxiv.org/abs/2602.11201)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct my evaluation. Let me compile my thorough analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Yuan et al., \"Hidden Error Awareness: The Signal Is Diagnostic, Not Causal\"](https://arxiv.org/abs/2605.09502) (arXiv, May 2026): 核心动机论文。证明线性 probe 可检测推理正确性 (0.95 AUROC)，但四种干预策略全部失败。本 proposal 的 ICG 框架本质上是将此发现从\"obstacle\"重新框架为\"phenomenon\"——这既是最大的 novelty claim，也是最大的风险点。\n- [Chrabąszcz et al., \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\"](https://arxiv.org/abs/2605.18549) (arXiv, May 2026): 最直接的竞争工作。已实现 probe trajectory 时序追踪 + 60+ signal-processing 特征提取，在 4 个推理模型上达到 91-97% AUROC。Proposal 正确识别了它缺少 causal contribution 维度，但这也意味着 Chrabąszcz 的工作已经覆盖了 ICG 框架中 P*(t) 这一半的工作。\n- [Cox et al., \"Decoding Answers Before Chain-of-Thought\"](https://arxiv.org/abs/2603.01437) (arXiv, Mar 2026): 证明 pre-CoT probes 可达 >0.9 AUC，且 steering 在 instruction-tuned 模型上有效但在 reasoning 模型上失败。与 Yuan et al. 独立印证 diagnostic-causal gap。\n- [Ballon et al., \"Probing the Trajectories of Reasoning Traces\"](https://arxiv.org/abs/2601.23163) (arXiv, Jan 2026): 提出 truncation-reinjection 协议作为行为层面的 C(t) 测量，proposal 直接借用该方法。\n- [Wang, \"LLM Reasoning Is Latent, Not the Chain of Thought\"](https://arxiv.org/abs/2604.15726) (arXiv, Apr 2026): 提出 H1/H2/H0 理论框架，proposal 声称 ICG 可实证区分 H1 vs H2。\n- [Gjølbye et al., \"Reasoning Models Don't Just Think Longer, They Move Differently\"](https://arxiv.org/abs/2605.15454) (arXiv, May 2026): 隐状态轨迹几何与难度耦合，domain-specific 强度差异。Proposal 引用其 length correction 方法和 domain-specific 发现。\n- [Kudo et al., \"LLMs Faithfully and Iteratively Compute Answers During CoT\"](https://aclanthology.org/2026.findings-eacl.59/) (EACL Findings 2026): 在合成算术任务上结合 per-position probes + activation patching，是最接近的 probe+causal 先行工作，但限于合成任务。\n- [CMI/Sathyanarayanan et al., \"When Chains of Thought Don't Matter\"](https://arxiv.org/abs/2602.03994) (arXiv 2026): 层级 activation patching 框架，仅 ~50 个样本，但同样结合了 probe + causal intervention。\n\n- **调研总结**: CoT faithfulness 是 2025-2026 年的\"热区\"——probe 方面（Chrabąszcz, David, Zhang, Yuan, Esakkiraja）和 causal intervention 方面（Ballon, Ye, Zhao）已各自成熟，但的确没有一个框架同时在时间轴上追踪两者的 divergence。理论框架（Wang H1/H2）也刚建立但缺乏实证操作化。Proposal 定位在这两个方向的交汇点，有真实的空白，但该空白的\"宽度\"需要仔细评估——Kudo (EACL 2026) 和 CMI 已经做了 probe+causal 组合（虽然规模小/任务受限），真正的 novelty delta 在于 \"full-timeline temporal tracking\" + \"phenomenon taxonomy\" + \"calibration\"。\n\n【Trivial Alternative 检验】:\n有一个值得担忧的 trivial alternative：**直接将 Chrabąszcz 的 probe trajectory 方法与 Ballon 的 truncation-reinjection C(t) 方法做简单拼接**（在同一模型、同一数据集上分别运行两个已有方法，然后画出它们的差值），而不需要 ICG 框架中大量的形式化、calibration machinery、和 phenomenon taxonomy。审稿人很可能会问：\"为什么不直接用这两篇论文的方法各跑一遍、把曲线叠在一起看？你的 null-probe calibration 和 MCT validation 带来的增量价值是什么？\"\n\nProposal 的增量价值在于：(1) null-probe calibration 去除 probe inflation（有理论基础，Hewitt & Liang 2019），(2) 将 gap 操作化为 instance-level diagnostic score (TIF)，(3) 现象分类学——将不同 G*(t) 形状映射到命名的 faithfulness failure mode。其中 (1) 是方法论上的实质贡献但并非 novel concept，(2) 是工程化包装，(3) 的实际可行性尚未验证（Phase 0b 就是为了验证这个）。总体而言，trivial alternative 威胁是中等的——有增量价值，但需要 Phase 0b 的正面结果来证明该增量价值是 substantive 而非 cosmetic。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有三个关键的未验证假设：\n\n1. **\"P*(t) 和 C(t) 可以在同一尺度上有意义地相减\"假设**。P*(t) 是 null-calibrated 的 AUROC（无量纲概率度量），C(t) 是行为层面的准确率变化（或 NLDD score）。两者度量空间不同，直接相减得到的 G*(t) 在数学上的意义并不清晰。Proposal 没有充分论证这两个量的 commensurability——这是一个相当根本的方法论假设。\n\n2. **\"不同 faithfulness phenomena 会产生可区分的 G*(t) temporal fingerprints\"假设**。Proposal 的 phenomenon signature predictions（pre-CoT encoding → \"large constant gap\"，genuine reasoning → \"converging gap\"，post-hoc rationalization → \"widening gap\"）是基于跨研究、跨模型、跨数据集的 probe 数据拼接出来的\"semi-synthetic\"预测。在同一个模型、同一个数据集上，这些轨迹形状是否能可靠区分，完全是 open question。Proposal 自己也承认这一点（Phase 0b），但如果 Phase 0b 失败（d < 0.3），剩下的\"characterization paper\"的贡献会大幅缩水。\n\n3. **\"correctness probe 是更好的 probe target\"假设**。Proposal 给出了三个论证（broader applicability, grounding in diagnostic-not-causal finding, more direct faithfulness interpretation），但 correctness probe 和 answer-content probe 测量的是不同东西——correctness probe 只编码 meta-cognitive \"对/错\" 信号，这比 answer-content 更间接地与 \"reasoning faithfulness\" 相关。当 G*(t) >> 0 时，其解释是 \"模型知道自己对/错但 CoT 没反映\"，但这并不直接等于 \"CoT is unfaithful\"——一个 faithful 的 CoT 也可能不编码 meta-cognitive self-monitoring。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 核心 novelty 是 \"同一时间轴上追踪 probe-estimated information availability 与 causal contribution 的 divergence\"。这确实是一个在现有文献中没有被完整实现的组合。但需要注意：(a) Kudo et al. (EACL 2026) 和 CMI (2602.03994) 已经做了 probe+causal 的组合（虽然规模小）；(b) Chrabąszcz et al. 已经做了 probe trajectory 的大规模实现；(c) Ballon et al. 已经做了 behavioral C(t) 曲线。ICG 的核心 novelty 是\"把这些拼在一起 + calibration + phenomenon taxonomy\"，这是一个 integration novelty 而非 conceptual breakthrough。Wang (2604.15726) 提供了理论框架，ICG 提供了实证操作化——这有价值，但 \"the gap IS the phenomenon\" 这个 reframing 在读过 Yuan et al. 和 Cox et al. 之后并不算 surprising，更像是一个 natural next step。\n\n2. **Significance: 中偏强** — 研究问题本身是高度重要的：CoT faithfulness 是当前 AI safety 和 interpretability 的核心问题，理解 \"what models know but don't use\" 对模型监控和对齐有直接 implications。如果 ICG 框架确实能产生可区分的 phenomenon fingerprints，它会成为一个广泛使用的诊断工具。实用性高（difficulty-conditioned gap 可以回答 \"when does CoT add value\"）。但 significance 受限于两个因素：(a) 框架的实用性高度依赖 Phase 0b 的正面结果——如果 phenomena 不可区分，它退化为\"又一个 characterization study\"；(b) 该领域已经非常拥挤（2025-2026 年有 30+ 篇高度相关的论文），incremental contribution 的感知风险较高。\n\n3. **Related Work: 强** — Proposal 对已有工作的覆盖异常全面（30+ 篇引用，多数是 2025-2026 年的最新工作）。差异化定位清晰：明确指出 Chrabąszcz et al. 缺少 causal dimension，Ballon et al. 缺少 probe-side measurement，Kudo et al. 限于合成任务，CMI 限于小样本。对竞争工作的分析诚实且准确（经调研验证，引用的论文真实存在且描述基本准确）。唯一的小问题是 \"unique in combining all five\" 的 claim 可能被审稿人视为 integration 而非 innovation。\n\n【概率估计】: [22% - 35%] 中位 28%\n\n【估计理由】: \n- Novelty 是 integration novelty（组合已有方法 + calibration + taxonomy），而非 conceptual breakthrough。审稿人读完 proposal 后的反应更可能是 \"this is a natural next step that someone should do\" 而不是 \"I wouldn't have thought of this\"。这将上界限制在 ~35%。\n- Significance 是真实的——研究问题重要、实用性强——但高度 contingent on Phase 0b 结果。如果 phenomena 不可区分，核心贡献大幅缩水。\n- Related work coverage 非常强，是 proposal 的主要优势。\n- P*(t) 和 C(t) 的 commensurability 问题是一个 methodological concern，如果审稿人深究可能是 weakness。\n- 领域拥挤度极高（2025-2026 热区），审稿人对 \"又一个 CoT faithfulness 框架\" 的容忍度较低。\n- 综合而言，这是一个方向正确、执行计划详尽、related work coverage 极强的 proposal，但核心 idea 的 novelty 和 surprise factor 处于 \"natural next step\" 级别。中位 28% 反映了 solid integration work 在拥挤领域的典型接收概率。\n\n【主要风险】:\n1. **\"Integration, not innovation\" 质疑**: 审稿人可能认为 ICG 框架是将 Chrabąszcz 的 probe trajectories + Ballon 的 truncation-reinjection + Hewitt & Liang 的 probe calibration 做 straightforward 组合，核心 insight（\"the gap IS the phenomenon\"）是 Yuan et al. 和 Cox et al. 之后的 obvious reframing，novelty delta 不足以支撑一篇顶会论文。\n2. **P*(t) 和 C(t) 的 commensurability 问题**: 这两个量度量空间不同（calibrated AUROC vs. behavioral accuracy change），直接相减缺乏严格的理论 justification。如果审稿人质疑 G*(t) 的数学意义，整个框架的 interpretive power 会被动摇。\n```\n\nSources:\n- [Yuan et al., \"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal\"](https://arxiv.org/abs/2605.09502)\n- [Chrabąszcz et al., \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\"](https://arxiv.org/abs/2605.18549)\n- [Cox et al., \"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\"](https://arxiv.org/abs/2603.01437)\n- [Ballon et al., \"Probing the Trajectories of Reasoning Traces in Large Language Models\"](https://arxiv.org/abs/2601.23163)\n- [Wang, \"LLM Reasoning Is Latent, Not the Chain of Thought\"](https://arxiv.org/abs/2604.15726)\n- [Gjølbye et al., \"Reasoning Models Don't Just Think Longer, They Move Differently\"](https://arxiv.org/abs/2605.15454)\n- [Kudo et al., \"LLMs Faithfully and Iteratively Compute Answers During CoT\" (EACL Findings 2026)](https://aclanthology.org/2026.findings-eacl.59/)\n- [Sathyanarayanan et al., \"When Chains of Thought Don't Matter: Causal Bypass / CMI\"](https://arxiv.org/abs/2602.03994)\n- [FaithCoT-Bench (ICLR 2026)](https://openreview.net/forum?id=lN3yKqqzF1)\n- [Project Ariadne: Structural Causal Framework for Auditing Faithfulness](https://arxiv.org/abs/2601.02314)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient context to provide a thorough evaluation. Let me synthesize all findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **Chrabąszcz et al. (arXiv 2605.18549, May 2026)**: \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics.\" 最直接的竞争工作。在 4 个推理模型上追踪 probe trajectory，提取 60+ 信号处理特征（volatility, trend, steady-state, boundary transients, autocorrelation），max-pooling 达到 91-97% AUROC。关键差异：完全没有 causal contribution 组件，没有 gap metric，没有 calibration。这同时验证了 proposal 的 P*(t) 方向，也说明 probe trajectory 本身已不新鲜。\n\n2. **Yuan et al. (arXiv 2605.09502, May 2026)**: \"Hidden Error Awareness: The Signal Is Diagnostic, Not Causal.\" 在 Qwen/Llama/Phi 三个家族（1.5B-72B）上证明四种干预策略全部失败：activation steering (+4% at best)、probe-guided best-of-N (matches random)、self-correction (hurts −3%)、activation patching (destroys coherence)。核心引用验证：correctness probe 达 0.95 AUROC，first-step 0.79。这是 proposal 的基础性动机论文，描述准确。\n\n3. **Cox et al. (arXiv 2603.01437, March 2026)**: \"Decoding Answers Before Chain-of-Thought.\" answer-content probes 在 instruction-tuned models 上达 >0.9 AUC 且 steering 能 flip >50%，但在 reasoning model GPT-OSS-20B 上 flip rate negligible。验证了 proposal 对 diagnostic-causal gap 在 reasoning models 上的描述。\n\n4. **Wang (arXiv 2604.15726, April 2026)**: \"LLM Reasoning Is Latent, Not the Chain of Thought.\" 形式化 H1 (latent-mediated) / H2 (CoT-mediated) / H0 (serial compute) 三假设。是一篇 position paper，提出了理论框架但没有提供实证方法论。Proposal 声称其 ICG 框架可操作化 Wang 的 H1/H2 区分——这个定位是合理的。\n\n5. **Ballon et al. (arXiv 2601.23163, January 2026)**: \"Probing the Trajectories of Reasoning Traces.\" truncation-reinjection protocol，在 Qwen3/gpt-oss 上展示单调递增的 accuracy curves，三种控制条件（random/swapped/shuffled tokens）验证 sequential content matters。这是 proposal C(t) 组件的直接前驱，但原论文明确声明不做 faithfulness-to-internal-computations 分析。\n\n6. **Gjølbye et al. (arXiv 2605.15454, May 2026)**: \"Reasoning Models Move Differently.\" 在 length correction 后 difficulty 仍与 trajectory geometry 系统性耦合（Codeforces ρ⊥=+0.41，MATH +0.05），domain-specific。为 proposal 的 difficulty conditioning 提供直接支撑。\n\n7. **Ye et al. (arXiv 2602.11201, February 2026)**: \"Mechanistic Evidence for Faithfulness Decay.\" NLDD metric，发现 Reasoning Horizon 在 70-85% chain length。是 proposal 三种 C(t) estimator 之一的来源。\n\n8. **CMI Framework (arXiv 2602.03994)**: layerwise activation patching，在 ~50 examples 上计算 CoT Mediation Index。规模太小，缺乏 temporal resolution，但概念上是 probe+intervention 的先驱。\n\n9. **Kudo et al. (EACL 2026, arXiv 2412.01113)**: per-position probes + sliding-window activation patching on synthetic arithmetic，发现 CoT IS faithful for arithmetic。但限于 synthetic setting。\n\n10. **Zhao et al. (arXiv 2510.24941)**: True Thinking Score (TTS)，per-step causal contribution，发现仅 2.3% AIME steps 有 TTS≥0.7。提供 step-level causal data 但无 probe-side measurement。\n\n- **调研总结**: CoT faithfulness 是 2025-2026 最拥挤的 NLP 研究方向之一。Probe 端（Chrabąszcz, Yuan, David, Zhang, Esakkiraja, Cox）和 causal 端（Ballon, Ye, Zhao, CMI）已各自成熟。将两者在时间维度上统一成 gap metric 的想法是 natural next step——没有人做过，但也不出人意料。Wang 的理论框架提供了\"为什么要这样做\"的理论支点，但 proposal 的技术贡献主要是 engineering synthesis，不是 conceptual breakthrough。该领域 6 个月内出了 40+ 篇相关论文，竞争极其激烈。\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。** 一个简化版本可以：(1) 在 t=0（CoT 开始前）测量 probe accuracy P(0)，在 CoT 结束后测量 final answer accuracy A_final；(2) 计算 Δ = A_final − P(0) 作为 CoT 的 causal uplift 的粗略度量。如果 P(0) 已经很高但 A_final 没有显著提升，这就已经捕捉到了\"知道但不用\"的核心信号。按 difficulty quintile 分层做这个 static 分析（easy vs. hard），就能得到 proposal 最主要的 expected finding（easy→decorative, hard→load-bearing），而完全不需要 full temporal resolution、三种 C(t) estimator、null-probe calibration、MCT validation 等重型机制。\n\n**增量价值在于时间分辨率和 phenomenon taxonomy**：如果不同 faithfulness 模式确实在 G*(t) 的 *temporal shape* 上可区分（Phase 0b 的核心赌注），那么 full temporal framework 提供的信息量超越 static baseline。但这个增量价值 heavily 依赖于 Phase 0b 的成功——如果 trajectory shapes 不可区分（d < 0.5），框架就退化为一个更昂贵的方式来重现 static analysis 已能给出的结论。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的关键假设：\n\n1. **P*(t) 和 C(t) 的可比性假设（致命级）**：P*(t) 是 probe AUROC（[0.5, 1.0] 区间），C(t) 是 causal contribution（可通过 prefix truncation 的 accuracy change 度量，也是概率量）。这两个量的量纲、尺度、噪声特性完全不同。G*(t) = P*(t) − C(t) 是否有清晰的 interpretable meaning？Probe AUROC 衡量的是\"是否能从 hidden states 分类出 correctness\"，causal contribution 衡量的是\"CoT 文本是否影响最终 answer\"。两者的 reduction 不一定是对同一个 latent variable 的两个 view。Proposal 隐含假设它们在同一语义空间上，但这未经证明。\n\n2. **Phenomenon trajectory-shape 可区分性假设（核心赌注）**：Proposal 声称 pre-CoT encoding、genuine reasoning、post-hoc rationalization 产生不同的 G*(t) 曲线形状。这个预测基于跨研究拼接的 semi-synthetic data（不同模型、不同数据集、不同度量），而非同一实验条件下的真实观察。Proposal 诚实地承认了这一点并设计了 Phase 0b 来验证，但如果 Phase 0b 失败，论文的核心贡献就塌缩为\"我们度量了 gap，gap 存在，但没有诊断力\"。\n\n3. **Null-probe calibration 充分性假设（中等级）**：P*(t) = P(t) − P_null(t) 只消除了 *uniform* correlative inflation。Chun et al. (2602.20338) 展示了 MCT geometric separability 在 CoT 中 transiently peaks 然后 probe accuracy 仍保持高位——说明 inflation 是 *non-uniform* 的。Proposal 提到了 MCT concordance check，但如果 non-uniform inflation 严重，P*(t) 本身的可靠性就成问题，进而 G*(t) 的 interpretability 也受损。\n\n4. **Correctness probe 作为 faithfulness proxy 的有效性假设（中等级）**：\"模型知道自己对不对但 CoT 没有反映这个 awareness\" ≠ \"CoT 不 faithful\"。一个模型可以在 CoT 中进行 faithful 的推理但不显式输出 meta-cognitive self-monitoring——这时 correctness probe gap 高但 CoT 仍然 faithful。Proposal 需要论证为什么 correctness awareness gap 是 faithfulness 的 necessary/sufficient condition，但这个论证目前是 implicit 的。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 核心贡献是将 probe trajectory（Chrabąszcz et al. 已做）和 causal contribution measurement（Ballon, Ye, Zhao 已做）在时间维度上组合成 gap metric。这是一个 *natural synthesis*，不是 *surprising insight*。没有人做过这个 exact combination（确认：我的调研未发现完全相同的框架），所以有 genuine novelty delta。但 delta 的性质更接近 \"engineering combination\" 而非 \"conceptual breakthrough\"。将 diagnostic-causal gap 从障碍重新定义为现象本身，framing 上有巧思，但如果一位审稿人已经熟悉 Yuan et al. + Ballon et al.，这个 reframing 不会让他们说 \"surprising\"。Probe calibration (Hewitt & Liang 2019) 和 MCT validation (Chun et al. 2022) 都是已有技术的应用。Phenomenon taxonomy 是 speculative 的——只有在 Phase 0b 验证后才构成真正的 novelty。\n\n2. **Significance: 中偏强** — 研究问题本身非常重要：理解 CoT 的因果角色是 AI safety 和 interpretability 的核心问题。如果 ICG 框架能成功分类 faithfulness phenomena 并提供 instance-level diagnostic，这对该领域有显著推动作用。但 expected findings 中最稳健的部分（easy→decorative, hard→genuine）已被 David, Li et al., ICLR Workshop 独立建立——ICG 框架提供更精细的度量但不改变核心结论。真正的 significance uplift 取决于 phenomenon classification 是否成功，这是不确定的。该方向对 inference-time compute allocation 和 safety monitoring 有清晰的 practical implications。\n\n3. **Related Work: 强** — 引用覆盖范围异常全面，包括 40+ 篇论文，且对每篇的描述与我调研核实的结果一致（Yuan et al. 的四种干预失败、Cox et al. 的 steering 在 reasoning model 上失败、Chrabąszcz et al. 的 60+ 特征、Ballon et al. 的三种控制条件）。对最直接竞争工作（Chrabąszcz et al.）的差异化定位清晰且准确。唯一的 minor gap：对 \"Robust Answers, Fragile Logic\" (2505.17406) 和 \"Answer-Conditioned Probing\" 等探讨 correctness probe interpretability 的工作覆盖不足——这些工作直接关系到前提假设检验第 4 点。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \n- Novelty 是 \"中\"：核心是 existing tools 的 temporal combination，reframing 有巧思但不 surprising。这将上界限制在 ~35% 以下——一个 \"natural synthesis\" 类工作在顶会中的 typical range。\n- Significance 是 \"中偏强\"：研究问题重要，但最 robust 的 expected finding (difficulty conditioning) 已被先前工作建立，限制了 surprise value。这进一步将中位数拉低到 30% 以下。\n- Related Work 是 \"强\"：这是加分项，但 related work 的全面性属于 execution quality，不改变 idea 的 intrinsic novelty ceiling。\n- P*(t) 和 C(t) 的可比性问题是一个 conceptual weakness，如果审稿人 push back on the interpretability of G*(t)，论文的整个 framework 都会受损。\n- 该领域竞争激烈（6 个月 40+ 篇），被抢发或被视为 incremental 的风险实质性存在。\n- Novelty 维度是限制上界的关键因素。\n\n【主要风险】:\n1. **\"Natural next step\" 而非 \"surprising insight\"**: 一位熟悉 Chrabąszcz + Yuan + Ballon 的审稿人可能会说 \"combining probe trajectories with causal measurement is the obvious thing to do — where is the surprising finding?\" 如果 Phase 0b 的 phenomenon classification 不成功，论文就只剩下 \"我们度量了 gap，gap 存在\"——这在当前文献密度下不足以支撑顶会论文。\n2. **G*(t) = P*(t) − C(t) 的 interpretability 问题**: Probe AUROC 和 causal contribution 是不同性质的量。审稿人可能质疑：这个差值的物理意义是什么？为什么两个度量在不同 scale 上的 raw difference 比单独分析两条曲线更有信息量？如果 proposal 不能说服审稿人这个 gap metric 比 \"separately plotting P*(t) and C(t) and visually comparing\" 有实质性的额外价值，核心 claim 就显得 thin。\n```\n\nSources:\n- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)\n- [Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al.)](https://arxiv.org/abs/2605.09502)\n- [Decoding Answers Before Chain-of-Thought (Cox et al.)](https://arxiv.org/abs/2603.01437)\n- [LLM Reasoning Is Latent, Not the Chain of Thought (Wang)](https://arxiv.org/abs/2604.15726)\n- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)\n- [Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al.)](https://arxiv.org/abs/2605.15454)\n- [Mechanistic Evidence for Faithfulness Decay (Ye et al.)](https://arxiv.org/abs/2602.11201)\n- [Bypassing the Rationale: Causal Auditing / CMI (Sathyanarayanan et al.)](https://arxiv.org/abs/2602.03994)\n- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)\n- [Why Models Know But Don't Say (Young)](https://arxiv.org/abs/2603.26410)\n- [Lie to Me (2603.22582)](https://arxiv.org/abs/2603.22582)\n- [Emergent Manifold Separability / MCT (Chun et al.)](https://arxiv.org/abs/2602.20338)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWe propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.\n\nThe framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness (explicitly targeting right/wrong prediction — justified over answer-content probes by broader applicability beyond binary tasks, grounding in the diagnostic-not-causal finding which is about correctness, and more direct faithfulness interpretation — with supplementary answer-content analysis on binary/MC subsets), and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions validating sequential content matters, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\nPositioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes across 4 reasoning models — our framework adds the entire causal contribution dimension, the calibrated gap metric, null-probe calibration with MCT geometric validation, phenomenon taxonomy, and task-difficulty conditioning. Their probe-trajectory methodology validates our P*(t) direction; we extend it to the dual-estimator gap that no existing framework provides.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) constructs real G*(t) curves from the SAME model and dataset and tests whether at least 2 phenomena produce distinguishable trajectories (effect size d > 0.5) before committing to the full classification pipeline — addressing the concern that semi-synthetic simulation from cross-study measurements overestimates real-data accuracy. The semi-synthetic simulation is retained as hypothesis generation producing testable predictions, not as evidence.\n\nTask-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits, the ICLR 2026 Workshop finding, and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific (weaker on MATH) — reveals the decorative→load-bearing transition with practical guidance on when chain-of-thought adds genuine value, applying length correction (residualizing on log(N)) to avoid generation-length confounds.\n\nThe paper focuses on four core contributions: (a) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. to demonstrate the value of the causal contribution dimension; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real data; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) probe-target analysis contrasting correctness vs. answer-content gaps. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs) as the primary bottleneck.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — with linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find that steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four distinct intervention strategies (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B parameters and report that ALL fail: 'RL training does not close the diagnostic–causal gap.' This diagnostic-causal gap — the divergence between what information is available in a model's hidden states and what information the chain-of-thought reasoning text causally contributes — is NOT a methodological obstacle to overcome; it IS the central phenomenon. Critically, the literature conflates two distinct probe targets: answer-content probes (Cox et al.: predicting the specific answer on binary tasks, models ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: predicting right/wrong on models up to 72B; Zhang et al.: per-chunk correctness on 7B-70B). This distinction matters because the gap's interpretation differs: answer-content gaps mean 'the model has already decided but CoT doesn't derive the answer,' while correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.' Meanwhile, the temporal dynamics of this gap are now empirically grounded: David (2511.14773) shows probe accuracy stabilizes at 0.84 AUC by token 4, remaining ~0.8 through token 100, with task-difficulty conditioning revealing easy (0.84) vs. hard (0.76) signatures. Zhang et al. (2504.05419) report chunk-level probe trajectories rising from 65% at 10% of reasoning to 79% at 100% on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with a characteristic dip at 5-10% of reasoning followed by recovery. Chrabąszcz et al. (2605.18549) demonstrate that temporal probe trajectories with 60+ signal-processing features achieve up to 17pp improvement over static probes, showing that trajectory dynamics capture information invisible to single-timepoint measurements. These temporal profiles suggest that different modes of CoT unfaithfulness — pre-CoT encoding, post-hoc rationalization, reasoning theater, myopic planning, thinking-answer gap — produce distinguishable temporal divergence signatures. Yet no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline: Chrabąszcz et al. provide the closest probe-trajectory methodology but lack any causal contribution component, gap metric, probe calibration, or phenomenon taxonomy; Ballon et al. (2601.23163) provide behavioral causal curves via truncation-reinjection but lack hidden-state measurement; the CMI framework provides layerwise causal audit on ~50 examples but no temporal resolution; Zhao et al.'s True Thinking Score provides per-step causal contribution but no probe-side measurement. The gap between diagnostic information availability and causal contribution IS the phenomenon of interest, not an obstacle.\n\n## Opportunity\nThe field has independently produced the measurement tools needed for a unified temporal framework, but these tools remain siloed. The opportunity is fourfold:\n\n(1) **Temporal gap measurement.** Despite rapid accumulation of probe measurements (David: 0.84 at t=4; Zhang: 0.82-0.91 on chunks; Yuan: 0.95 overall, 0.787 first-step; Esakkiraja: >90% pre-generation; Chrabąszcz et al.: 91-97% AUROC with max-pooling on trajectories), no work tracks the full-timeline divergence between probe-estimated information availability and intervention-estimated causal contribution. Chrabąszcz et al. (2605.18549) come closest on the probe side — extracting 60+ signal-processing features from probe trajectories across 4 reasoning models and 4 datasets, achieving up to 17pp improvement over static probes on GSM8K — but they target outcome prediction (correctness, harmfulness) rather than the faithfulness gap, and provide no causal contribution measurement. Their work validates that temporal probe trajectories capture dynamics invisible to static probes (confirming our P*(t) direction); our framework extends this via the dual-estimator gap G*(t) = P*(t) − C(t) that requires the additional causal contribution dimension, null-probe calibration, and phenomenon mapping. On the causal side, Ballon et al. (2601.23163) provide behavioral C(t) curves via truncation-reinjection at decile intervals on Qwen3/gpt-oss across GPQA-Diamond and MMLU-Pro — showing monotonic accuracy increase from 30.8-42.3% to 49.0-73.1% with control conditions validating that sequential content (not just context length) matters — but lack hidden-state measurement. The gap between these two measurement traditions IS the framework's niche.\n\n(2) **Phenomenon unification with honest scoping.** The CoT faithfulness literature treats each failure mode as separate: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al. 2603.01437; Esakkiraja et al. 2604.01202), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103), thinking-answer gap. We propose that 2-3 of these are confidently distinguishable via trajectory-shape signatures in the information-contribution gap G*(t), with 4-5 as a stretch goal requiring additional features. The honest scoping — validated through an empirical pilot on real data before committing to full classification — is itself a contribution to a field prone to over-claiming.\n\n(3) **Task-difficulty conditioning.** The ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration show easy→decorative, hard→faithful. David's easy/hard splits (0.84 vs. 0.76 at t=32) provide probe-level evidence. Gjølbye et al. (2605.15454) demonstrate that difficulty is systematically coupled to hidden-state trajectory geometry even after length correction (ρ⊥ = +0.41 for reasoning models vs. −0.06 for baselines on competitive programming), with domain-specific strength. A difficulty-conditioned gap framework can answer the practical question: at what difficulty level does CoT transition from decorative to load-bearing?\n\n(4) **Probe target clarification.** The field has not confronted the distinction between answer-content probes (Cox et al.: binary tasks, ≤9B) and correctness probes (Yuan et al.: up to 72B). A framework that explicitly measures correctness awareness gap — and contrasts it with answer-content gap on applicable tasks — provides the first principled treatment of what 'knowing but not using' means.\n\nTwo prior works have combined probing with causal interventions: Kudo et al. (EACL 2026) on synthetic arithmetic, and the CMI framework (2602.03994) on ~50 examples. Wang (2604.15726) formalizes the need via competing hypotheses (H1: latent-mediated, H2: CoT-mediated, H0: serial compute) and proposes compute-audited designs — our ICG framework provides an empirical methodology to distinguish H1 from H2 at each token position. Neither Kudo et al. nor CMI provides: (a) full temporal-position coverage on natural benchmarks, (b) mapping to named faithfulness phenomena, (c) a standalone instance-level diagnostic, (d) systematic multi-model comparison, (e) robustness validation — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) an empirical pilot validating phenomenon separability on real data.\n\n## Landscape\n**Probe-based temporal measurement (foundational for our P*(t) component).** Chrabąszcz et al. (2605.18549) is the closest concurrent work: they introduce probe trajectories — tracking concept probability at each generated token — and extract 60+ signal-processing features (volatility, trend, steady-state, temporal segmentation, boundary transients, autocorrelation) via 3-layer MLP probes with Multi-Instance Learning meta-probe across layers. Key results: max-pooling achieves 91-97% AUROC on harmfulness detection (vs. 33-61% for average-pooling, demonstrating average/last-token pooling collapses to near-random); up to 17pp improvement over static probes on GSM8K mathematical error prediction across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours total). Critical differentiators from our framework: (a) NO causal contribution component — they measure only probe accuracy trajectories, not whether CoT causally contributes; (b) NO gap metric — just trajectory vs. static comparison for outcome prediction; (c) NO null-probe calibration or MCT geometric validation — their 3-layer MLP probes are uncalibrated; (d) NO phenomenon taxonomy — they separate correct/incorrect or safe/harmful, not faithfulness modes; (e) NO task-difficulty conditioning. Their 60+ feature extraction methodology is complementary and could enhance our trajectory-shape classification. David (2511.14773) trains per-position probes on reasoning models, finding 0.84 AUC at t=4, stable ~0.8 through t≈100, with easy/hard splits of 0.84 vs. 0.76 at t=32 on Qwen3-8B. Zhang et al. (2504.05419) probe R1-Distill models (7B/32B/70B) for correctness at each reasoning chunk, achieving 0.82-0.91 AUROC on GSM8K/MATH/AIME, with a rising trajectory from 65% at 10% chunk to 79% at 100%, enabling 24% token reduction via early-exit. Yuan et al. (2605.09502) report 0.95 AUROC on Qwen-3B, 0.852 on DeepSeek-R1-7B, 0.787 from first-step hidden states alone, and a concealment gap of 0.197 AUROC between hidden-state (0.787) and text-surface (0.590) classifiers — using correctness probes (right/wrong), not answer-content probes. Esakkiraja et al. (2604.01202) find >90% AUROC pre-generation on Qwen3-4B and GLM-Z1-9B, with a characteristic dip at 5-10% of reasoning and recovery to near-100% by think_end. Cox et al. (2603.01437) use answer-content probes (predicting specific answer A/B on binary tasks: Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) achieving >0.9 AUC on instruction-tuned Gemma-2 (2B, 9B) and Qwen-2.5 (1.5B, 3B, 7B) models, with causal validation via steering (>50% flip rates) — but 'the answer flip rate is negligible against the orthogonal baseline' on the reasoning model GPT-OSS-20B. Additional probing work: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop, probing F1 90-100%, steering 46% recovery).\n\n**The diagnostic-not-causal evidence (motivating our framework).** Yuan et al. (2605.09502) is the decisive study: four interventions — activation steering (at most +4%), probe-guided best-of-N (matches random), self-correction (hurts accuracy −3%), activation patching (destroys coherence at α=0.5) — all fail. Tested on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. Key quote: 'The error signal is a diagnostic readout—a summary statistic of computation quality—not a causal component that can be edited.' Cox et al. (2603.01437) independently confirm: steering fails on reasoning models despite high probe accuracy. This establishes that probe accuracy ≠ causal potency on reasoning models, which is the foundational observation our framework exploits.\n\n**Behavioral trajectory probing (foundational for our C(t) component).** Ballon et al. (2601.23163) introduce the truncation-reinjection protocol: generate full reasoning traces on Qwen3-4B/8B/14B and gpt-oss-20B/120B, truncate at decile intervals (10-100%), reinject with early-stopping suffix, measure answer-choice probability distributions. Key results: accuracy increases monotonically from 30.8-42.3% (no reasoning) to 49.0-73.1% (full trace) on GPQA-Diamond; decision commitment tracks similarly. Three control conditions validate causal content: random tokens (+2.1-4.3%), swapped traces (+3.2-8.7%), and shuffled tokens (+0.3-10.8%) all substantially underperform intact truncated traces (+18.1-33.1%), confirming sequential content — not just context length — drives gains. Stronger models rescue weak-model errors at 43-68% rate with free continuation vs. 28-51% anchoring in base mode. Explicitly disclaims faithfulness-to-internal-computations analysis, making it a direct precursor to our prefix-truncation C(t) estimator. Zhao et al. (2510.24941) introduce the True Thinking Score (TTS), measuring per-step causal contribution via numerical perturbation and ATE computation on DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7. Ye et al. (2602.11201) introduce NLDD, finding a Reasoning Horizon at 70-85% of chain length on 3 models across synthetic tasks. Basu & Chakraborty (2603.22816) propose a decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026) provides another causal measurement approach.\n\n**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize. The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, DialoGPT on StrategyQA (20), TruthfulQA (10), GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors operating on small samples or synthetic tasks.\n\n**Latent-reasoning theory.** Wang (2604.15726) formalizes three competing hypotheses about LLM reasoning: H1 (reasoning is primarily mediated by latent-state trajectories), H2 (reasoning is primarily mediated by explicit surface CoT), H0 (most reasoning gains are better explained by generic serial compute). Proposes compute-audited designs with six experimental arms (baseline, surface manipulation, surface control, latent intervention, latent control, compute-only expansion) and evidence tiers (probe-only = suggestive, compute-matched causal = strongest). Our ICG framework operationalizes Wang's H1/H2 distinction: when G*(t) >> 0, hidden states encode correctness awareness that CoT doesn't contribute (H1-consistent); when G*(t) ≈ 0, CoT is mediating (H2-consistent).\n\n**Temporal hidden-state dynamics (concurrent complementary work).** Gjølbye et al. (2605.15454) study hidden-state trajectory geometry across 11 models (6 reasoning: R1-Distill-Qwen-7B/14B/32B, R1-Distill-Llama-8B, QwQ-32B, Phi-4-Reasoning; 5 instruction-tuned baselines) on competitive programming (500 Codeforces), math (500 MATH), and Boolean SAT (500 SATBench). After length correction (residualizing directness/curvature on log(N)), difficulty remains systematically coupled to trajectory geometry: reasoning models show ρ⊥^D = +0.41 on Codeforces vs. −0.06 for baselines (raw correlations reverse from −0.73 to +0.41), with weaker effects in math (+0.05 vs. −0.07) and non-specific effects in SAT (+0.27 vs. +0.23). Critically, prompt-stage linear probes do NOT mirror these geometric effects — reasoning dynamics manifest during generation, not at input. Their length correction methodology and domain-specificity finding are relevant for our temporal analysis and difficulty conditioning. Furuya & Tanimura (2605.01853) introduce StALT, a training-free trajectory statistic separating correct from incorrect reasoning trajectories. Herrmann et al. (2605.09159) study 'internal polylogue' dynamics: persona vectors tracked temporally across MMLU-Pro in four open-weight models. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, tracking concept-direction alignment per step on Qwen 3-4B; find easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals, achieving 14-70% token savings on R1-Distill/Phi-4/Qwen3.\n\n**Probe calibration and inflation (methodological foundation).** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity. Ravichander et al. (2020) demonstrate properties recoverable even when unused. Voita & Titov (2020) show MDL-based probing reveals accuracy doesn't substantially favor pretrained over random. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning: geometric separability peaks transiently as a 'geometric pulse' while probe accuracy remains high afterward — direct evidence that probe accuracy overestimates information availability. We address this via null-probe calibration: P*(t) = P(t) − P_null(t).\n\n**Trajectory-shape analysis (supporting our shape-based classification).** Entropy trajectory paper (2603.18940): monotonicity predicts reliability regardless of absolute levels (+5.8pp). RQA analysis (2602.06266): temporal features outperform aggregates 36.94% vs. 28.97%. Microsoft trajectory geometry (2604.05655): 0.852 AUC from shape features vs. 0.649 baseline. This literature validates trajectory shapes as diagnostic features.\n\n**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence. Task-difficulty moderation: ICLR 2026 Workshop and Li et al. (2510.22362).\n\n**Reasoning-model internal dynamics.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill.\n\n**Benchmarks, surveys, pathology diagnostics.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Liu et al. (2602.13904): text-level metrics for rationalization/encoded/internalized reasoning. Reasoning Theater (2603.05488). Young (2603.26410). 'Lie to Me' (2603.22582). Various early-exit methods: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT.\n\n**What remains open.** No extant framework provides: (1) a full-timeline information-contribution gap curve pairing calibrated probe trajectories with causal contribution estimation — Chrabąszcz et al.'s probe trajectories are the closest but lack the entire C(t) dimension, gap metric, and calibration; (2) an empirically-validated phenomenon trajectory-shape taxonomy grounded in real within-model, within-dataset G*(t) curves rather than cross-study semi-synthetic assembly; (3) an instance-level diagnostic score derived from the temporal gap; (4) difficulty-conditioned gap analysis with domain-specific nuance (following Gjølbye et al.'s finding of domain-dependent coupling strength); or (5) a principled treatment of the probe-target distinction (correctness vs. answer-content) and its implications for gap interpretation. The calibrated temporal ICG framework is unique in combining all five.\n\n## Approach\nWe propose the Information-Contribution Gap (ICG) framework: a calibrated, temporally-resolved diagnostic that measures the divergence between information available in hidden states and information that causally contributes to model outputs, tracked across the full chain-of-thought generation trajectory.\n\n**Formal Framework.** Define two time-varying quantities at each token position t during CoT generation:\n\n(i) *Calibrated Information Availability* P*(t): Cross-validated AUROC of a linear probe on layer-l hidden states at position t, calibrated via null-probe normalization (P*(t) = P(t) − P_null(t), following Hewitt & Liang 2019 selectivity, where P_null is trained on shuffled labels). **Probe target: correctness (right/wrong).** We choose correctness over answer-content for three reasons: (a) broader applicability — correctness probes generalize beyond binary/MC tasks (Cox et al.'s answer-content probes are limited to binary A/B on 4 tasks), while correctness probes (Yuan et al.) work across model families up to 72B; (b) the 'diagnostic not causal' finding that motivates the entire framework is specifically about correctness probes (Yuan et al.'s four-intervention failure on correctness probes); (c) correctness gaps are more directly interpretable for faithfulness — G*(t) >> 0 means 'the model's hidden states encode awareness that its answer is right/wrong, but its CoT does not causally reflect this self-monitoring.' On binary/MC task subsets, we additionally train answer-content probes to test whether the 'what answer' gap differs from the 'whether correct' gap — a supplementary analysis testing whether pre-CoT encoding operates on content or meta-cognition. This measures excess correctness awareness above correlative features. We probe at layers L/4, L/2, 3L/4, L to capture layer-wise dynamics. MCT geometric validation (Chun et al. 2602.20338) on 500 examples confirms whether calibrated probe signal reflects geometrically organized information rather than mere retrievability. Note: Chrabąszcz et al. (2605.18549) demonstrate that probe trajectories with 60+ signal-processing features substantially outperform static probes (up to 17pp on GSM8K). We adopt their insight that temporal dynamics are essential, while adding null-probe calibration (which they lack) and extending to the dual-estimator gap. Where applicable, we incorporate their feature categories (volatility, trend, steady-state, boundary transients) as additional trajectory descriptors for phenomenon classification in Phase 3.\n\n(ii) *Causal Contribution* C(t): The causal contribution of CoT up to position t, estimated via three complementary methods: (a) prefix-truncation ablation — measuring P(correct | CoT[:t]) vs. P(correct | full CoT), following Ballon et al.'s (2601.23163) truncation-reinjection protocol with their three control conditions (random tokens, swapped traces, shuffled tokens) to validate that C(t) measures genuine sequential content contribution rather than context-length effects (their finding: shuffled tokens retain +0.3-10.8% vs. intact +18.1-33.1%); (b) paraphrase perturbation — replacing CoT segments with meaning-preserving paraphrases and measuring answer stability; (c) NLDD-based influence scoring (Ye et al. 2602.11201) — measuring how corruption at position t degrades the answer distribution. Using multiple C(t) estimators provides robustness against single-method artifacts, following Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive.\n\n**The Information-Contribution Gap.** G*(t) = P*(t) − C(t). This gap is the primary diagnostic signal:\n- G*(t) ≈ 0: Correctness awareness and causal contribution are aligned (necessary for faithfulness)\n- G*(t) >> 0: The model encodes correctness awareness it does not causally use in its CoT (diagnostic excess — the model 'knows but doesn't use')\n- G*(t) < 0: The CoT contributes to correctness beyond what hidden states encode at that point (information assembled during reasoning)\n\nBecause P*(t) is null-probe-calibrated, uniform correlative inflation is removed. C(t) is not subject to probe inflation as it measures behavioral change under intervention. The gap G*(t) is interpretable as 'calibrated correctness awareness the model has but doesn't channel through its CoT at position t.' Following Wang's (2604.15726) H1/H2 framework: G*(t) >> 0 is H1-consistent (latent-mediated reasoning), G*(t) ≈ 0 is H2-consistent (CoT-mediated reasoning).\n\n**Phenomenon Signature Predictions (2-3 confident, 4-5 stretch).** We ground predictions in real probe data but adopt honest scoping informed by the concern that cross-study heterogeneity may overestimate separability:\n\n*Primary targets (HIGH confidence, validated in Phase 0b pilot):*\n(i) *Pre-CoT encoding*: G*(t) starts high and stays high. Grounded in: David's 0.84 AUC at t=4, Esakkiraja's >90% pre-generation AUROC, Cox's >0.9 pre-CoT AUC. P*(0) > 0.5 (after calibration), C(t) rises slowly. Shape: large constant gap.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. Grounded in: Zhang et al.'s 65%→79% chunk trajectory, Li et al.'s finding that hard→faithful, Ballon et al.'s monotonic accuracy increase with reasoning length. P*(t) rises gradually, C(t) tracks P*(t). Shape: co-rising curves, small/decreasing gap.\n(iii) *Post-hoc rationalization*: G*(t) starts moderate, rises during CoT. P*(t) stable (David: ~0.80 from t=4 through t=100), C(t) remains flat despite token generation. Shape: widening gap.\n\n*Stretch targets (MODERATE confidence, require additional features):*\n(iv) *Steganographic encoding*: G*(t) dip-and-recovery. Potentially consistent with Esakkiraja's dip at 5-10%. May require multi-layer analysis to separate from noise.\n(v) *Reasoning Theater*: EMPIRICAL QUESTION. Under non-uniform inflation, may overlap with pre-CoT encoding or post-hoc rationalization. Additional features — layer-wise P*(t) distribution, C(t) variance under paraphrase perturbation, Chrabąszcz-style signal features (autocorrelation, boundary transients, dwell-time run-lengths) — may enable separation. Whether Theater is cleanly separable is reported honestly with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** We construct semi-synthetic G*(t) curves grounded in real published data to generate testable predictions about trajectory-shape separability — but we do NOT treat this as evidence of real-data separability (published measurements come from different models, datasets, and setups, introducing heterogeneity that does not match within-dataset variance). Instead, the simulation identifies: (a) which trajectory features are most discriminative in principle, (b) what minimum effect sizes real-data classification needs to achieve, (c) where non-uniform inflation causes theoretical overlap between phenomena. I_probe(t) profiles drawn from published measurements (David, Zhang, Esakkiraja, Yuan), C(t) profiles modeled from NLDD (Ye et al.) and TTS (Zhao et al.) data, non-uniform inflation calibrated against Chun et al.'s MCT finding. The real validation comes from Phase 0b.\n\n**Phase 0a: Gap Characterization (Weeks 1-2.5).** Three objectives on 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct empirical P*(t) and C(t) curves at token-level resolution\n(ii) Validate null-probe calibration: P_null(t) shows high accuracy (inflation exists) but P*(t) shows meaningful variance (calibration reveals structure)\n(iii) Characterize causal potency: following Cox et al.'s protocol, measure answer flip rates via probe-direction steering on reasoning vs. instruction-tuned models\n\nExpected outcome (base case): Causal potency is low on reasoning models, confirming the diagnostic-not-causal property and validating the ICG framework's interpretive power. If causal potency is unexpectedly high, this is an exciting upgrade. Either outcome is scientifically valuable.\n\n**Phase 0b: Empirical Pilot for Phenomenon Separability (Weeks 2.5-4).** This phase validates that trajectory-shape classification is feasible on real data before committing to the full pipeline. On the SAME model (R1-Distill-Qwen-7B) and datasets (GSM8K + MATH-500, 1000 examples), construct real G*(t) curves and test whether at least 2 phenomena produce distinguishable trajectories. Protocol: (i) partition examples by difficulty quintile and model behavior (easy-correct with high P*(0) → pre-CoT encoding candidates; hard-correct with rising P*(t) tracking C(t) → genuine reasoning candidates; incorrect with stable P*(t) and flat C(t) → post-hoc rationalization candidates); (ii) compute full G*(t) for each partition; (iii) test effect size d > 0.5 on at least 2 trajectory features between partitions. Apply Gjølbye et al.'s (2605.15454) length correction (residualizing trajectory features on log(N)) to ensure differences are not conflated with generation-length effects. Success criterion: d > 0.5 between at least 2 partitions on 2+ features. If d < 0.3 across all features, downscope to a characterization paper (gap exists and varies with difficulty, but trajectory shapes are not cleanly phenotypic) — still a strong contribution given no prior full-timeline G*(t) measurement exists.\n\n**Phase 1: Full ICG Construction (Weeks 4-9).** Conditional on Phase 0b showing separability (d > 0.5). Extend to 4 models (add QwQ-32B or R1-Distill-32B) × 4 benchmarks (add GPQA-Diamond or AIME). Full calibrated P*(t) with null-probe normalization + MCT concordance check on 500 examples. Three C(t) estimators with Ballon et al.-style controls (random, swap, shuffle baselines). Cross-reference with TTS (Zhao et al.) at step boundaries. Bootstrap confidence intervals on G*(t).\n\n**Phase 2: Task-Difficulty Conditioning (Weeks 7-11).** Partition each benchmark into difficulty quintiles (using model accuracy as proxy). Measure G*(t) per quintile. Hypothesis grounded in David's easy/hard data, Li et al.'s finding, and Gjølbye et al.'s difficulty-geometry coupling: easy problems show large persistent gap (decorative CoT), hard problems show converging gap (load-bearing CoT). Following Gjølbye et al., apply length correction and report domain-specific effects — expecting stronger effects on math/code benchmarks than MMLU, given their finding of ρ⊥ = +0.41 on Codeforces vs. +0.05 on MATH. The transition point — where G*(t) shifts from decorative to genuine — provides practical guidance on when CoT adds value.\n\n**Phase 3: Phenomenon Classification and Robustness (Weeks 9-14).** Apply trajectory-shape classification to real data. Target: 2-3 cleanly separable phenomena, with 4-5 reported honestly including overlap. Incorporate Chrabąszcz et al.'s feature categories (volatility, trend, boundary transients, autocorrelation) alongside our gap-specific features (initial G* value, G* slope, convergence rate, dC/dt locality). Six robustness ablations following Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection (single best vs. multi-layer); (c) C(t) estimator agreement (prefix vs. paraphrase vs. NLDD); (d) gap normalization method; (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content on binary/MC subsets). Report sensitivity ranges across all dimensions.\n\n**TIF Score.** Temporal Information-contribution Faithfulness score: normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s text-level metrics.\n\n**Paper Focus (Tightened).** Core contributions: (1) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al.'s probe trajectories — demonstrating the value added by the causal contribution dimension and gap metric; (2) Phase 0b empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real within-model, within-dataset data; (3) task-difficulty conditioning revealing the decorative→load-bearing transition with domain-specific strength following Gjølbye et al.'s nuance. Supporting: robustness ablations (6 dimensions); TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness probe comparison; semi-synthetic simulation as hypothesis generation.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT cross-reference. Gjølbye-style length correction on all temporal analyses.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~830 H100-hours (Phase 0a characterization: 80 hrs [3 models × 3 datasets, probe training + prefix ablation + steering tests]; Phase 0b empirical pilot: 30 hrs [1 model × 2 datasets, full G*(t) construction + partition analysis + length correction]; Phase 1 full ICG: 120 hrs [4 models × 4 benchmarks, multi-layer probes + 3 C(t) estimators]; Phase 2 difficulty conditioning: 50 hrs; Phase 3 phenomenon classification + robustness ablations: 50 hrs; NLDD on 32B model: 250 hrs [primary bottleneck — up to 20 perturbation positions × 5K examples × forward passes]; NLDD on 7B/14B models: 100 hrs; MCT geometric validation: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic simulation: 50 hrs [mostly CPU, some GPU for validation])', 'timeline': '15-17 weeks (2 researchers: 4 weeks Phase 0a+0b characterization + pilot; 5 weeks Phase 1 full ICG; 4 weeks Phases 2-3 in parallel with NLDD; 2-3 weeks writing + ablations)', 'estimated_gpu_cost': '$2,500 at ~$3/H100-hour (cloud spot pricing)', 'storage': '3-5 TB (4 layers per model, fp16); reducible to ~1.5 TB via PCA'}, 'human_in_loop': {'gpu_hours': '~830 H100-hours', 'timeline': '13 weeks (1 researcher + Claude for experiment design and analysis)', 'claude_api_cost': '$350', 'estimated_gpu_cost': '$2,500'}, 'auto_research': {'gpu_hours': '~830 H100-hours', 'timeline': '11 weeks', 'claude_api_cost': '$700', 'estimated_gpu_cost': '$2,500', 'speed_bottleneck': 'NLDD on 32B (~250 H100-hours, ~30% of total compute) is the primary bottleneck. Each NLDD evaluation requires corrupting reasoning at multiple positions and measuring logit degradation — O(T × N) forward passes where T≈20 perturbation positions and N≈5K examples. For 32B models, this cannot be easily parallelized beyond 8-GPU data parallelism. Secondary: 671B subset (8×H100, ~50 hrs); MCT geometric validation (~50 hrs). Phase 0b pilot (30 hrs) provides early go/no-go signal before committing full Phase 1-3 compute.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s finding that answer-content probe steering fails on reasoning models despite high accuracy; (b) Yuan et al.'s systematic demonstration that four interventions all fail on correctness probes, establishing 'diagnostic not causal'; (c) the temporal probe dynamics now empirically characterized by David (0.84 AUC at t=4, stable ~0.8), Zhang et al. (chunk-level rising trajectory), Esakkiraja et al. (pre-generation >90% with dip-recovery), and Chrabąszcz et al. (60+ trajectory features capturing dynamics invisible to static probes, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection protocol demonstrating monotonic behavioral C(t) curves with rigorous controls (sequential content +18.1-33.1% vs. shuffled +0.3-10.8%) — all pointing to the same insight: the gap between diagnostic information availability and causal contribution IS the phenomenon of interest. Additionally inspired by: Wang's (2604.15726) formalization of H1/H2/H0 hypotheses providing the theoretical scaffold for what our framework empirically measures; Gjølbye et al.'s (2605.15454) finding that difficulty-geometry coupling is domain-specific and requires length correction; Herrmann et al.'s concurrent temporal persona-vector dynamics; and the trajectory-shape literature showing shapes can distinguish phenomena regardless of absolute-value calibration.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)\n- ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces in Large Language Models (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent, Not the Chain of Thought (Wang, arXiv 2604.15726)\n- Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- Can Aha Moments Be Fake? True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Do LLMs Experience an Internal Polylogue? (Herrmann et al., arXiv 2605.09159)\n- LLMs Faithfully and Iteratively Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- When Chains of Thought Don't Matter: Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- Spatiotemporal Hidden-State Dynamics / StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Mapping Faithful Reasoning / Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- Emergent Manifold Separability / MCT (Chun et al., arXiv 2602.20338)\n- Tracing the Traces: Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940)\n- Is My Model Mind Blurting? RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability via Information Theory (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics with MI (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination via Transport Geometry (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE: Perfect Linear Concept Erasure (Belrose et al., NeurIPS 2023, arXiv 2306.03819)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:46:49.264Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:46:49.264Z",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:46:49.276Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct my assessment. Let me compile the triage evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Yuan et al., arXiv 2605.09502] (May 2026): "Hidden Error Awareness: The Signal Is Diagnostic, Not Causal." 线性 probe 在 correctness 上达到 0.95 AUROC，但四种 causal intervention（activation steering、probe-guided best-of-N、self-correction、activation patching）全部失败。这是本 proposal 的核心动机来源——"diagnostic-not-causal gap"概念直接源自此文。论文已确认存在，描述准确。
- [Cox et al., arXiv 2603.01437] (Mar 2026): "Decoding Answers Before CoT." Pre-CoT probes 在 instruction-tuned 模型上达到 >0.9 AUC，steering flip rate >50%；但在 reasoning model (GPT-OSS-20B) 上 steering 失败。与 Yuan et al. 互相独立地确认了 diagnostic-causal gap。描述准确。
- [Chrabąszcz et al., arXiv 2605.18549] (May 2026): "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics." 提取 60+ signal-processing features（volatility, trend, steady-state 等），max-pooling 达到 91-97% AUROC，比 static probes 提高 17pp。这是 probe trajectory 方向最接近的 concurrent work。关键差异：**没有 causal contribution 组件**、没有 gap metric、没有 calibration、没有 phenomenon taxonomy。描述准确。
- [Wang, arXiv 2604.15726] (Apr 2026): "LLM Reasoning Is Latent, Not the Chain of Thought." 形式化了 H1（latent-mediated）/ H2（CoT-mediated）/ H0（serial compute）三个竞争假说。本 proposal 声称 ICG 框架可以在每个 token position 区分 H1 vs H2。论文已确认存在。
- [Ballon et al., arXiv 2601.23163] (Jan 2026): "Probing the Trajectories of Reasoning Traces." Truncation-reinjection 协议，在 decile intervals 测量 accuracy 变化，三个 control conditions 验证 sequential content matters。这是 C(t) 的方法论基础。论文已确认，描述准确。
- [Gjølbye et al., arXiv 2605.15454] (May 2026): "Reasoning Models Don't Just Think Longer, They Move Differently." 研究 hidden-state trajectory geometry，发现 difficulty 与 trajectory geometry 的 coupling 在 length correction 后仍然存在，但 domain-specific（code: ρ⊥=+0.41, math: +0.05）。描述准确。
- [CMI framework, arXiv 2602.03994] (Feb 2026): Layerwise causal audit，只在 ~50 examples 上测试，无 temporal resolution。确认存在。
- [Kudo et al., EACL 2026]: Per-position probes + activation patching on synthetic arithmetic. 确认 CoT faithful for arithmetic but synthetic setting. 确认存在。
- 未发现任何已发表工作提出 "Information-Contribution Gap" 或等价的 probe trajectory + causal contribution temporal dual-estimator framework。proposal 声称的 "no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline" 在我的调研范围内成立。

- 调研总结: CoT faithfulness 领域在 2025-2026 年经历了爆发式增长。Probe-based 诊断（Yuan, Cox, David, Zhang, Esakkiraja, Chrabąszcz）和 causal contribution 测量（Ballon, Ye/NLDD, Zhao/TTS, CMI）两条线已经各自成熟，但确实没有人将两者 temporally 结合。本 proposal 定位在两条线的交汇处，gap 是真实的。然而，这个交汇点是一个 "obvious next step"——领域内任何关注这两条线的人都能看到这个方向。

【Trivial Alternative 检验】:
存在若干更简单的替代方案：

(1) **单点 gap 而非 temporal trajectory**: 只比较 pre-CoT probe accuracy 与 final answer accuracy 的差值作为 faithfulness proxy。不需要 temporal resolution，不需要 C(t) 的多种估计方法。这能捕获最核心的 "model knows but doesn't use" 信号。增量价值：temporal trajectory 提供的 phenomenon fingerprinting 是唯一辩护，但 phenomenon fingerprinting 本身是未经验证的假说。

(2) **只用 Chrabąszcz et al. 的 probe trajectory + accuracy-based heuristic**: 对比 probe trajectory shape 与最终正确/错误，不需要 causal contribution estimation。如果只是区分 "faithful" vs "unfaithful"，probe trajectory alone 可能就够了。增量价值：加入 C(t) 维度理论上能区分 "model knows and uses CoT" 和 "model knows but CoT is decorative"，但这一区分能否被 probe trajectory shape alone 近似捕获是开放问题。

(3) **直接用 Ballon et al. 的 truncation accuracy curve + pre-CoT probe accuracy**: 不需要构建完整的 G*(t) 框架，只需两个测量取差值。

**增量价值的关键辩护**在于 phenomenon taxonomy 的可区分性——如果 G*(t) 确实能 fingerprint 不同的 unfaithfulness 模式，这比上述 trivial alternatives 有质的提升。但如果 phenomenon 不可区分（Phase 0b 失败），框架退化为一个 characterization tool，其增量价值相对 trivial alternatives 变得微薄。

【前提假设检验】:
核心 claim 的逻辑链条中存在以下未经验证的假设：

(1) **P*(t) 和 C(t) 的可减性（commensurability）**：这是最严重的未检验假设。P*(t) 是 calibrated AUROC（分类器性能指标，[0,1]），C(t) 由三种方法估计：prefix truncation 给出 accuracy change、paraphrase perturbation 给出 stability score、NLDD 给出 logit degradation。这三者的 scale、分布特性完全不同，也都与 AUROC 不在同一度量空间。G*(t) = P*(t) − C(t) 的减法在数学上是什么含义？proposal 完全没有讨论如何将这些异质测量统一到同一 scale。如果 gap 的数值意义不明确，整个 phenomenon fingerprinting 就缺乏坚实基础。

(2) **Phenomenon 离散可分假设**：proposal 假设 pre-CoT encoding、genuine reasoning、post-hoc rationalization 是离散类别，且在 G*(t) 空间中形成可区分的 clusters。但实际上，单个 reasoning trace 可能同时包含多种模式（前半段 genuine reasoning，后半段 post-hoc rationalization），且不同模式之间可能是连续谱而非离散类别。Phase 0b 的 d > 0.5 threshold 设定也相对宽松（effect size 0.5 在心理学中只是 medium effect）。

(3) **Probe calibration 的充分性**：null-probe calibration（P*(t) = P(t) − P_null(t)）假设 inflation 是 additive 的。但 Chun et al. 的 MCT 工作已经表明 probe accuracy 与 geometric separability 的关系是非线性的——probe accuracy 可以在 geometric separability 消失后保持高位。简单减法可能无法正确 calibrate。

(4) **Post-hoc rationalization 的 "widening gap" 预测**：proposal 预测 post-hoc rationalization 表现为 "G*(t) starts moderate, rises during CoT"，但同时引用 David 的数据显示 P*(t) 在 t=4 后稳定在 ~0.80。如果 P*(t) 稳定而 C(t) flat，gap 是常数而非 widening。要 widening 需要 C(t) 下降，但 post-hoc rationalization 中 C(t) 没有理由下降。这个具体预测的逻辑链有缺陷。

【3 维度打分】:
  1. Novelty: 【中】 — 核心 idea "将 probe trajectory 和 causal contribution 联合 track 为 temporal dual-estimator gap" 在技术层面是新的——调研确认 Chrabąszcz et al. 只有 probe side，Ballon et al. 只有 causal side，CMI 无 temporal resolution。然而，这属于 "synthesis novelty"：每个组件（temporal probing, causal contribution estimation, calibration）都已存在，组合方式是领域发展的 obvious next step。The conceptual insight "the gap IS the phenomenon" 已经隐含在 Yuan et al. 和 Cox et al. 的讨论中——本 proposal 的贡献是 formalize 和 operationalize，而非 discover。Phenomenon taxonomy 的 fingerprinting 如果成功会增加 novelty，但这是未验证的假说。此外，commensurability 问题（P*(t) 和 C(t) 的 scale 不一致）使得 "gap" 的 formalization 本身并不如表面看起来那么 clean。

  2. Significance: 【中-强】 — 研究问题本身——CoT faithfulness 的 temporal dynamics——是 NLP/AI safety 领域的核心问题之一，2025-2026 年有大量关注。如果 framework 成功，它将提供：(a) instance-level faithfulness diagnostic（实用价值），(b) 对不同 unfaithfulness 模式的分类学（理论贡献），(c) 对 "when does CoT add value" 的实证回答（practical guidance）。Difficulty conditioning 部分有独立价值。然而，如果 Phase 0b 显示 phenomenon 不可区分，论文的 impact 大幅下降，退化为 "we measured G*(t) and it varies"——这在一个已有大量 characterization 工作（David, Zhang, Esakkiraja, Chrabąszcz）的领域中增量有限。

  3. Related Work: 【强】 — 这是本 proposal 最强的维度。覆盖了 30+ 篇 2024-2026 年的相关工作，包括所有主要方向（probe-based measurement, causal intervention, temporal dynamics, trajectory geometry, calibration, faithfulness taxonomy）。与最接近的 concurrent work（Chrabąszcz et al.）的差异化定位清晰且有说服力。引用的关键论文经调研确认真实存在且描述准确。对 CMI, Kudo et al., TTS 等 probe+intervention 组合工作的定位合理。唯一的小瑕疵：对 Hewitt & Liang (2019) 和 Voita & Titov (2020) 的 calibration 文献引用是准确的，但 null-probe calibration 方案本身在技术层面存在可质疑性（如前述 additive assumption）。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Novelty 是限制上界的主要因素。核心 idea 是一个 well-executed synthesis，但不是一个 surprising insight。如果审稿人问 "if the core finding is positive, would I be surprised?"，答案大概率是 "No, I would have guessed that pre-CoT encoding shows high gap while genuine reasoning shows converging gap"——这些预测本身是直觉性的。Significance 将上界推高（重要问题 + 实用价值），Related Work 的 thoroughness 提供了坚实的 positioning 基础。但 commensurability 问题（P*(t) 和 C(t) 的 scale 不一致）是一个可能让审稿人直接质疑 framework soundness 的技术漏洞。Phenomenon separability 假说增加了 upside potential（如果成功，novelty 升至中-强），但也增加了 downside risk（如果失败，论文核心 narrative 被削弱）。综合来看，这是一篇 "solid framework/analysis paper"，在 EMNLP 的 interpretability/analysis track 有竞争力但并非突出。

【主要风险】: 
1. **Commensurability 缺陷**: G*(t) = P*(t) − C(t) 将不同度量空间的量相减，审稿人几乎必然会质疑这一形式化的数学意义。如果无法令人信服地解释 AUROC − (accuracy change / stability / logit degradation) 的含义，framework 的核心 formalization 就站不住脚。这是 idea 层面的风险，不仅仅是实验设计问题。
2. **"Obvious next step" 的 novelty 挑战**: 在一个 Chrabąszcz et al. 已做 probe trajectory、Ballon et al. 已做 causal trajectory、Yuan et al. 已指出 diagnostic-not-causal gap 的领域，将三者组合是自然推论。审稿人可能认为 novelty 在于 execution 而非 idea，而 execution 层面的 novelty（calibration, Phase 0b pilot, difficulty conditioning）可能不足以撑起一篇顶会论文的 contribution bar。
```

Sources:
- [Yuan et al. - Hidden Error Awareness](https://arxiv.org/abs/2605.09502)
- [Cox et al. - Decoding Answers Before CoT](https://arxiv.org/abs/2603.01437)
- [Chrabąszcz et al. - Probe Trajectories](https://arxiv.org/abs/2605.18549)
- [Wang - LLM Reasoning Is Latent](https://arxiv.org/abs/2604.15726)
- [Ballon et al. - Probing Trajectories of Reasoning Traces](https://arxiv.org/abs/2601.23163)
- [Gjølbye et al. - Reasoning Models Move Differently](https://arxiv.org/abs/2605.15454)
- [CMI Framework - Bypassing the Rationale](https://arxiv.org/abs/2602.03994)
- [FaithCoT-Bench - ICLR 2026](https://arxiv.org/abs/2510.04040)
- [Ye et al. - Mechanistic Evidence for Faithfulness Decay](https://arxiv.org/abs/2602.11201)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct my evaluation. Let me compile my thorough analysis.

---

```
【阶段】: Triage

【领域调研】:
- [Yuan et al., "Hidden Error Awareness: The Signal Is Diagnostic, Not Causal"](https://arxiv.org/abs/2605.09502) (arXiv, May 2026): 核心动机论文。证明线性 probe 可检测推理正确性 (0.95 AUROC)，但四种干预策略全部失败。本 proposal 的 ICG 框架本质上是将此发现从"obstacle"重新框架为"phenomenon"——这既是最大的 novelty claim，也是最大的风险点。
- [Chrabąszcz et al., "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"](https://arxiv.org/abs/2605.18549) (arXiv, May 2026): 最直接的竞争工作。已实现 probe trajectory 时序追踪 + 60+ signal-processing 特征提取，在 4 个推理模型上达到 91-97% AUROC。Proposal 正确识别了它缺少 causal contribution 维度，但这也意味着 Chrabąszcz 的工作已经覆盖了 ICG 框架中 P*(t) 这一半的工作。
- [Cox et al., "Decoding Answers Before Chain-of-Thought"](https://arxiv.org/abs/2603.01437) (arXiv, Mar 2026): 证明 pre-CoT probes 可达 >0.9 AUC，且 steering 在 instruction-tuned 模型上有效但在 reasoning 模型上失败。与 Yuan et al. 独立印证 diagnostic-causal gap。
- [Ballon et al., "Probing the Trajectories of Reasoning Traces"](https://arxiv.org/abs/2601.23163) (arXiv, Jan 2026): 提出 truncation-reinjection 协议作为行为层面的 C(t) 测量，proposal 直接借用该方法。
- [Wang, "LLM Reasoning Is Latent, Not the Chain of Thought"](https://arxiv.org/abs/2604.15726) (arXiv, Apr 2026): 提出 H1/H2/H0 理论框架，proposal 声称 ICG 可实证区分 H1 vs H2。
- [Gjølbye et al., "Reasoning Models Don't Just Think Longer, They Move Differently"](https://arxiv.org/abs/2605.15454) (arXiv, May 2026): 隐状态轨迹几何与难度耦合，domain-specific 强度差异。Proposal 引用其 length correction 方法和 domain-specific 发现。
- [Kudo et al., "LLMs Faithfully and Iteratively Compute Answers During CoT"](https://aclanthology.org/2026.findings-eacl.59/) (EACL Findings 2026): 在合成算术任务上结合 per-position probes + activation patching，是最接近的 probe+causal 先行工作，但限于合成任务。
- [CMI/Sathyanarayanan et al., "When Chains of Thought Don't Matter"](https://arxiv.org/abs/2602.03994) (arXiv 2026): 层级 activation patching 框架，仅 ~50 个样本，但同样结合了 probe + causal intervention。

- **调研总结**: CoT faithfulness 是 2025-2026 年的"热区"——probe 方面（Chrabąszcz, David, Zhang, Yuan, Esakkiraja）和 causal intervention 方面（Ballon, Ye, Zhao）已各自成熟，但的确没有一个框架同时在时间轴上追踪两者的 divergence。理论框架（Wang H1/H2）也刚建立但缺乏实证操作化。Proposal 定位在这两个方向的交汇点，有真实的空白，但该空白的"宽度"需要仔细评估——Kudo (EACL 2026) 和 CMI 已经做了 probe+causal 组合（虽然规模小/任务受限），真正的 novelty delta 在于 "full-timeline temporal tracking" + "phenomenon taxonomy" + "calibration"。

【Trivial Alternative 检验】:
有一个值得担忧的 trivial alternative：**直接将 Chrabąszcz 的 probe trajectory 方法与 Ballon 的 truncation-reinjection C(t) 方法做简单拼接**（在同一模型、同一数据集上分别运行两个已有方法，然后画出它们的差值），而不需要 ICG 框架中大量的形式化、calibration machinery、和 phenomenon taxonomy。审稿人很可能会问："为什么不直接用这两篇论文的方法各跑一遍、把曲线叠在一起看？你的 null-probe calibration 和 MCT validation 带来的增量价值是什么？"

Proposal 的增量价值在于：(1) null-probe calibration 去除 probe inflation（有理论基础，Hewitt & Liang 2019），(2) 将 gap 操作化为 instance-level diagnostic score (TIF)，(3) 现象分类学——将不同 G*(t) 形状映射到命名的 faithfulness failure mode。其中 (1) 是方法论上的实质贡献但并非 novel concept，(2) 是工程化包装，(3) 的实际可行性尚未验证（Phase 0b 就是为了验证这个）。总体而言，trivial alternative 威胁是中等的——有增量价值，但需要 Phase 0b 的正面结果来证明该增量价值是 substantive 而非 cosmetic。

【前提假设检验】:
核心 claim 的逻辑链条中有三个关键的未验证假设：

1. **"P*(t) 和 C(t) 可以在同一尺度上有意义地相减"假设**。P*(t) 是 null-calibrated 的 AUROC（无量纲概率度量），C(t) 是行为层面的准确率变化（或 NLDD score）。两者度量空间不同，直接相减得到的 G*(t) 在数学上的意义并不清晰。Proposal 没有充分论证这两个量的 commensurability——这是一个相当根本的方法论假设。

2. **"不同 faithfulness phenomena 会产生可区分的 G*(t) temporal fingerprints"假设**。Proposal 的 phenomenon signature predictions（pre-CoT encoding → "large constant gap"，genuine reasoning → "converging gap"，post-hoc rationalization → "widening gap"）是基于跨研究、跨模型、跨数据集的 probe 数据拼接出来的"semi-synthetic"预测。在同一个模型、同一个数据集上，这些轨迹形状是否能可靠区分，完全是 open question。Proposal 自己也承认这一点（Phase 0b），但如果 Phase 0b 失败（d < 0.3），剩下的"characterization paper"的贡献会大幅缩水。

3. **"correctness probe 是更好的 probe target"假设**。Proposal 给出了三个论证（broader applicability, grounding in diagnostic-not-causal finding, more direct faithfulness interpretation），但 correctness probe 和 answer-content probe 测量的是不同东西——correctness probe 只编码 meta-cognitive "对/错" 信号，这比 answer-content 更间接地与 "reasoning faithfulness" 相关。当 G*(t) >> 0 时，其解释是 "模型知道自己对/错但 CoT 没反映"，但这并不直接等于 "CoT is unfaithful"——一个 faithful 的 CoT 也可能不编码 meta-cognitive self-monitoring。

【3 维度打分】:

1. **Novelty: 中** — 核心 novelty 是 "同一时间轴上追踪 probe-estimated information availability 与 causal contribution 的 divergence"。这确实是一个在现有文献中没有被完整实现的组合。但需要注意：(a) Kudo et al. (EACL 2026) 和 CMI (2602.03994) 已经做了 probe+causal 的组合（虽然规模小）；(b) Chrabąszcz et al. 已经做了 probe trajectory 的大规模实现；(c) Ballon et al. 已经做了 behavioral C(t) 曲线。ICG 的核心 novelty 是"把这些拼在一起 + calibration + phenomenon taxonomy"，这是一个 integration novelty 而非 conceptual breakthrough。Wang (2604.15726) 提供了理论框架，ICG 提供了实证操作化——这有价值，但 "the gap IS the phenomenon" 这个 reframing 在读过 Yuan et al. 和 Cox et al. 之后并不算 surprising，更像是一个 natural next step。

2. **Significance: 中偏强** — 研究问题本身是高度重要的：CoT faithfulness 是当前 AI safety 和 interpretability 的核心问题，理解 "what models know but don't use" 对模型监控和对齐有直接 implications。如果 ICG 框架确实能产生可区分的 phenomenon fingerprints，它会成为一个广泛使用的诊断工具。实用性高（difficulty-conditioned gap 可以回答 "when does CoT add value"）。但 significance 受限于两个因素：(a) 框架的实用性高度依赖 Phase 0b 的正面结果——如果 phenomena 不可区分，它退化为"又一个 characterization study"；(b) 该领域已经非常拥挤（2025-2026 年有 30+ 篇高度相关的论文），incremental contribution 的感知风险较高。

3. **Related Work: 强** — Proposal 对已有工作的覆盖异常全面（30+ 篇引用，多数是 2025-2026 年的最新工作）。差异化定位清晰：明确指出 Chrabąszcz et al. 缺少 causal dimension，Ballon et al. 缺少 probe-side measurement，Kudo et al. 限于合成任务，CMI 限于小样本。对竞争工作的分析诚实且准确（经调研验证，引用的论文真实存在且描述基本准确）。唯一的小问题是 "unique in combining all five" 的 claim 可能被审稿人视为 integration 而非 innovation。

【概率估计】: [22% - 35%] 中位 28%

【估计理由】: 
- Novelty 是 integration novelty（组合已有方法 + calibration + taxonomy），而非 conceptual breakthrough。审稿人读完 proposal 后的反应更可能是 "this is a natural next step that someone should do" 而不是 "I wouldn't have thought of this"。这将上界限制在 ~35%。
- Significance 是真实的——研究问题重要、实用性强——但高度 contingent on Phase 0b 结果。如果 phenomena 不可区分，核心贡献大幅缩水。
- Related work coverage 非常强，是 proposal 的主要优势。
- P*(t) 和 C(t) 的 commensurability 问题是一个 methodological concern，如果审稿人深究可能是 weakness。
- 领域拥挤度极高（2025-2026 热区），审稿人对 "又一个 CoT faithfulness 框架" 的容忍度较低。
- 综合而言，这是一个方向正确、执行计划详尽、related work coverage 极强的 proposal，但核心 idea 的 novelty 和 surprise factor 处于 "natural next step" 级别。中位 28% 反映了 solid integration work 在拥挤领域的典型接收概率。

【主要风险】:
1. **"Integration, not innovation" 质疑**: 审稿人可能认为 ICG 框架是将 Chrabąszcz 的 probe trajectories + Ballon 的 truncation-reinjection + Hewitt & Liang 的 probe calibration 做 straightforward 组合，核心 insight（"the gap IS the phenomenon"）是 Yuan et al. 和 Cox et al. 之后的 obvious reframing，novelty delta 不足以支撑一篇顶会论文。
2. **P*(t) 和 C(t) 的 commensurability 问题**: 这两个量度量空间不同（calibrated AUROC vs. behavioral accuracy change），直接相减缺乏严格的理论 justification。如果审稿人质疑 G*(t) 的数学意义，整个框架的 interpretive power 会被动摇。
```

Sources:
- [Yuan et al., "Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal"](https://arxiv.org/abs/2605.09502)
- [Chrabąszcz et al., "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"](https://arxiv.org/abs/2605.18549)
- [Cox et al., "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering"](https://arxiv.org/abs/2603.01437)
- [Ballon et al., "Probing the Trajectories of Reasoning Traces in Large Language Models"](https://arxiv.org/abs/2601.23163)
- [Wang, "LLM Reasoning Is Latent, Not the Chain of Thought"](https://arxiv.org/abs/2604.15726)
- [Gjølbye et al., "Reasoning Models Don't Just Think Longer, They Move Differently"](https://arxiv.org/abs/2605.15454)
- [Kudo et al., "LLMs Faithfully and Iteratively Compute Answers During CoT" (EACL Findings 2026)](https://aclanthology.org/2026.findings-eacl.59/)
- [Sathyanarayanan et al., "When Chains of Thought Don't Matter: Causal Bypass / CMI"](https://arxiv.org/abs/2602.03994)
- [FaithCoT-Bench (ICLR 2026)](https://openreview.net/forum?id=lN3yKqqzF1)
- [Project Ariadne: Structural Causal Framework for Auditing Faithfulness](https://arxiv.org/abs/2601.02314)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient context to provide a thorough evaluation. Let me synthesize all findings.

---

```
【阶段】: Triage

【领域调研】:

1. **Chrabąszcz et al. (arXiv 2605.18549, May 2026)**: "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics." 最直接的竞争工作。在 4 个推理模型上追踪 probe trajectory，提取 60+ 信号处理特征（volatility, trend, steady-state, boundary transients, autocorrelation），max-pooling 达到 91-97% AUROC。关键差异：完全没有 causal contribution 组件，没有 gap metric，没有 calibration。这同时验证了 proposal 的 P*(t) 方向，也说明 probe trajectory 本身已不新鲜。

2. **Yuan et al. (arXiv 2605.09502, May 2026)**: "Hidden Error Awareness: The Signal Is Diagnostic, Not Causal." 在 Qwen/Llama/Phi 三个家族（1.5B-72B）上证明四种干预策略全部失败：activation steering (+4% at best)、probe-guided best-of-N (matches random)、self-correction (hurts −3%)、activation patching (destroys coherence)。核心引用验证：correctness probe 达 0.95 AUROC，first-step 0.79。这是 proposal 的基础性动机论文，描述准确。

3. **Cox et al. (arXiv 2603.01437, March 2026)**: "Decoding Answers Before Chain-of-Thought." answer-content probes 在 instruction-tuned models 上达 >0.9 AUC 且 steering 能 flip >50%，但在 reasoning model GPT-OSS-20B 上 flip rate negligible。验证了 proposal 对 diagnostic-causal gap 在 reasoning models 上的描述。

4. **Wang (arXiv 2604.15726, April 2026)**: "LLM Reasoning Is Latent, Not the Chain of Thought." 形式化 H1 (latent-mediated) / H2 (CoT-mediated) / H0 (serial compute) 三假设。是一篇 position paper，提出了理论框架但没有提供实证方法论。Proposal 声称其 ICG 框架可操作化 Wang 的 H1/H2 区分——这个定位是合理的。

5. **Ballon et al. (arXiv 2601.23163, January 2026)**: "Probing the Trajectories of Reasoning Traces." truncation-reinjection protocol，在 Qwen3/gpt-oss 上展示单调递增的 accuracy curves，三种控制条件（random/swapped/shuffled tokens）验证 sequential content matters。这是 proposal C(t) 组件的直接前驱，但原论文明确声明不做 faithfulness-to-internal-computations 分析。

6. **Gjølbye et al. (arXiv 2605.15454, May 2026)**: "Reasoning Models Move Differently." 在 length correction 后 difficulty 仍与 trajectory geometry 系统性耦合（Codeforces ρ⊥=+0.41，MATH +0.05），domain-specific。为 proposal 的 difficulty conditioning 提供直接支撑。

7. **Ye et al. (arXiv 2602.11201, February 2026)**: "Mechanistic Evidence for Faithfulness Decay." NLDD metric，发现 Reasoning Horizon 在 70-85% chain length。是 proposal 三种 C(t) estimator 之一的来源。

8. **CMI Framework (arXiv 2602.03994)**: layerwise activation patching，在 ~50 examples 上计算 CoT Mediation Index。规模太小，缺乏 temporal resolution，但概念上是 probe+intervention 的先驱。

9. **Kudo et al. (EACL 2026, arXiv 2412.01113)**: per-position probes + sliding-window activation patching on synthetic arithmetic，发现 CoT IS faithful for arithmetic。但限于 synthetic setting。

10. **Zhao et al. (arXiv 2510.24941)**: True Thinking Score (TTS)，per-step causal contribution，发现仅 2.3% AIME steps 有 TTS≥0.7。提供 step-level causal data 但无 probe-side measurement。

- **调研总结**: CoT faithfulness 是 2025-2026 最拥挤的 NLP 研究方向之一。Probe 端（Chrabąszcz, Yuan, David, Zhang, Esakkiraja, Cox）和 causal 端（Ballon, Ye, Zhao, CMI）已各自成熟。将两者在时间维度上统一成 gap metric 的想法是 natural next step——没有人做过，但也不出人意料。Wang 的理论框架提供了"为什么要这样做"的理论支点，但 proposal 的技术贡献主要是 engineering synthesis，不是 conceptual breakthrough。该领域 6 个月内出了 40+ 篇相关论文，竞争极其激烈。

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 一个简化版本可以：(1) 在 t=0（CoT 开始前）测量 probe accuracy P(0)，在 CoT 结束后测量 final answer accuracy A_final；(2) 计算 Δ = A_final − P(0) 作为 CoT 的 causal uplift 的粗略度量。如果 P(0) 已经很高但 A_final 没有显著提升，这就已经捕捉到了"知道但不用"的核心信号。按 difficulty quintile 分层做这个 static 分析（easy vs. hard），就能得到 proposal 最主要的 expected finding（easy→decorative, hard→load-bearing），而完全不需要 full temporal resolution、三种 C(t) estimator、null-probe calibration、MCT validation 等重型机制。

**增量价值在于时间分辨率和 phenomenon taxonomy**：如果不同 faithfulness 模式确实在 G*(t) 的 *temporal shape* 上可区分（Phase 0b 的核心赌注），那么 full temporal framework 提供的信息量超越 static baseline。但这个增量价值 heavily 依赖于 Phase 0b 的成功——如果 trajectory shapes 不可区分（d < 0.5），框架就退化为一个更昂贵的方式来重现 static analysis 已能给出的结论。

【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的关键假设：

1. **P*(t) 和 C(t) 的可比性假设（致命级）**：P*(t) 是 probe AUROC（[0.5, 1.0] 区间），C(t) 是 causal contribution（可通过 prefix truncation 的 accuracy change 度量，也是概率量）。这两个量的量纲、尺度、噪声特性完全不同。G*(t) = P*(t) − C(t) 是否有清晰的 interpretable meaning？Probe AUROC 衡量的是"是否能从 hidden states 分类出 correctness"，causal contribution 衡量的是"CoT 文本是否影响最终 answer"。两者的 reduction 不一定是对同一个 latent variable 的两个 view。Proposal 隐含假设它们在同一语义空间上，但这未经证明。

2. **Phenomenon trajectory-shape 可区分性假设（核心赌注）**：Proposal 声称 pre-CoT encoding、genuine reasoning、post-hoc rationalization 产生不同的 G*(t) 曲线形状。这个预测基于跨研究拼接的 semi-synthetic data（不同模型、不同数据集、不同度量），而非同一实验条件下的真实观察。Proposal 诚实地承认了这一点并设计了 Phase 0b 来验证，但如果 Phase 0b 失败，论文的核心贡献就塌缩为"我们度量了 gap，gap 存在，但没有诊断力"。

3. **Null-probe calibration 充分性假设（中等级）**：P*(t) = P(t) − P_null(t) 只消除了 *uniform* correlative inflation。Chun et al. (2602.20338) 展示了 MCT geometric separability 在 CoT 中 transiently peaks 然后 probe accuracy 仍保持高位——说明 inflation 是 *non-uniform* 的。Proposal 提到了 MCT concordance check，但如果 non-uniform inflation 严重，P*(t) 本身的可靠性就成问题，进而 G*(t) 的 interpretability 也受损。

4. **Correctness probe 作为 faithfulness proxy 的有效性假设（中等级）**："模型知道自己对不对但 CoT 没有反映这个 awareness" ≠ "CoT 不 faithful"。一个模型可以在 CoT 中进行 faithful 的推理但不显式输出 meta-cognitive self-monitoring——这时 correctness probe gap 高但 CoT 仍然 faithful。Proposal 需要论证为什么 correctness awareness gap 是 faithfulness 的 necessary/sufficient condition，但这个论证目前是 implicit 的。

【3 维度打分】:

1. **Novelty: 中** — 核心贡献是将 probe trajectory（Chrabąszcz et al. 已做）和 causal contribution measurement（Ballon, Ye, Zhao 已做）在时间维度上组合成 gap metric。这是一个 *natural synthesis*，不是 *surprising insight*。没有人做过这个 exact combination（确认：我的调研未发现完全相同的框架），所以有 genuine novelty delta。但 delta 的性质更接近 "engineering combination" 而非 "conceptual breakthrough"。将 diagnostic-causal gap 从障碍重新定义为现象本身，framing 上有巧思，但如果一位审稿人已经熟悉 Yuan et al. + Ballon et al.，这个 reframing 不会让他们说 "surprising"。Probe calibration (Hewitt & Liang 2019) 和 MCT validation (Chun et al. 2022) 都是已有技术的应用。Phenomenon taxonomy 是 speculative 的——只有在 Phase 0b 验证后才构成真正的 novelty。

2. **Significance: 中偏强** — 研究问题本身非常重要：理解 CoT 的因果角色是 AI safety 和 interpretability 的核心问题。如果 ICG 框架能成功分类 faithfulness phenomena 并提供 instance-level diagnostic，这对该领域有显著推动作用。但 expected findings 中最稳健的部分（easy→decorative, hard→genuine）已被 David, Li et al., ICLR Workshop 独立建立——ICG 框架提供更精细的度量但不改变核心结论。真正的 significance uplift 取决于 phenomenon classification 是否成功，这是不确定的。该方向对 inference-time compute allocation 和 safety monitoring 有清晰的 practical implications。

3. **Related Work: 强** — 引用覆盖范围异常全面，包括 40+ 篇论文，且对每篇的描述与我调研核实的结果一致（Yuan et al. 的四种干预失败、Cox et al. 的 steering 在 reasoning model 上失败、Chrabąszcz et al. 的 60+ 特征、Ballon et al. 的三种控制条件）。对最直接竞争工作（Chrabąszcz et al.）的差异化定位清晰且准确。唯一的 minor gap：对 "Robust Answers, Fragile Logic" (2505.17406) 和 "Answer-Conditioned Probing" 等探讨 correctness probe interpretability 的工作覆盖不足——这些工作直接关系到前提假设检验第 4 点。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
- Novelty 是 "中"：核心是 existing tools 的 temporal combination，reframing 有巧思但不 surprising。这将上界限制在 ~35% 以下——一个 "natural synthesis" 类工作在顶会中的 typical range。
- Significance 是 "中偏强"：研究问题重要，但最 robust 的 expected finding (difficulty conditioning) 已被先前工作建立，限制了 surprise value。这进一步将中位数拉低到 30% 以下。
- Related Work 是 "强"：这是加分项，但 related work 的全面性属于 execution quality，不改变 idea 的 intrinsic novelty ceiling。
- P*(t) 和 C(t) 的可比性问题是一个 conceptual weakness，如果审稿人 push back on the interpretability of G*(t)，论文的整个 framework 都会受损。
- 该领域竞争激烈（6 个月 40+ 篇），被抢发或被视为 incremental 的风险实质性存在。
- Novelty 维度是限制上界的关键因素。

【主要风险】:
1. **"Natural next step" 而非 "surprising insight"**: 一位熟悉 Chrabąszcz + Yuan + Ballon 的审稿人可能会说 "combining probe trajectories with causal measurement is the obvious thing to do — where is the surprising finding?" 如果 Phase 0b 的 phenomenon classification 不成功，论文就只剩下 "我们度量了 gap，gap 存在"——这在当前文献密度下不足以支撑顶会论文。
2. **G*(t) = P*(t) − C(t) 的 interpretability 问题**: Probe AUROC 和 causal contribution 是不同性质的量。审稿人可能质疑：这个差值的物理意义是什么？为什么两个度量在不同 scale 上的 raw difference 比单独分析两条曲线更有信息量？如果 proposal 不能说服审稿人这个 gap metric 比 "separately plotting P*(t) and C(t) and visually comparing" 有实质性的额外价值，核心 claim 就显得 thin。
```

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al.)](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before Chain-of-Thought (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [LLM Reasoning Is Latent, Not the Chain of Thought (Wang)](https://arxiv.org/abs/2604.15726)
- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)
- [Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al.)](https://arxiv.org/abs/2605.15454)
- [Mechanistic Evidence for Faithfulness Decay (Ye et al.)](https://arxiv.org/abs/2602.11201)
- [Bypassing the Rationale: Causal Auditing / CMI (Sathyanarayanan et al.)](https://arxiv.org/abs/2602.03994)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [Why Models Know But Don't Say (Young)](https://arxiv.org/abs/2603.26410)
- [Lie to Me (2603.22582)](https://arxiv.org/abs/2603.22582)
- [Emergent Manifold Separability / MCT (Chun et al.)](https://arxiv.org/abs/2602.20338)


【原始 proposal（允许参考但不是主要依据）】:
# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness

## Description
We propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.

The framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness (explicitly targeting right/wrong prediction — justified over answer-content probes by broader applicability beyond binary tasks, grounding in the diagnostic-not-causal finding which is about correctness, and more direct faithfulness interpretation — with supplementary answer-content analysis on binary/MC subsets), and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions validating sequential content matters, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).

Positioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes across 4 reasoning models — our framework adds the entire causal contribution dimension, the calibrated gap metric, null-probe calibration with MCT geometric validation, phenomenon taxonomy, and task-difficulty conditioning. Their probe-trajectory methodology validates our P*(t) direction; we extend it to the dual-estimator gap that no existing framework provides.

We adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) constructs real G*(t) curves from the SAME model and dataset and tests whether at least 2 phenomena produce distinguishable trajectories (effect size d > 0.5) before committing to the full classification pipeline — addressing the concern that semi-synthetic simulation from cross-study measurements overestimates real-data accuracy. The semi-synthetic simulation is retained as hypothesis generation producing testable predictions, not as evidence.

Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits, the ICLR 2026 Workshop finding, and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific (weaker on MATH) — reveals the decorative→load-bearing transition with practical guidance on when chain-of-thought adds genuine value, applying length correction (residualizing on log(N)) to avoid generation-length confounds.

The paper focuses on four core contributions: (a) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. to demonstrate the value of the causal contribution dimension; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real data; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) probe-target analysis contrasting correctness vs. answer-content gaps. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs) as the primary bottleneck.

## Core Problem
A striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — with linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find that steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four distinct intervention strategies (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B parameters and report that ALL fail: 'RL training does not close the diagnostic–causal gap.' This diagnostic-causal gap — the divergence between what information is available in a model's hidden states and what information the chain-of-thought reasoning text causally contributes — is NOT a methodological obstacle to overcome; it IS the central phenomenon. Critically, the literature conflates two distinct probe targets: answer-content probes (Cox et al.: predicting the specific answer on binary tasks, models ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: predicting right/wrong on models up to 72B; Zhang et al.: per-chunk correctness on 7B-70B). This distinction matters because the gap's interpretation differs: answer-content gaps mean 'the model has already decided but CoT doesn't derive the answer,' while correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.' Meanwhile, the temporal dynamics of this gap are now empirically grounded: David (2511.14773) shows probe accuracy stabilizes at 0.84 AUC by token 4, remaining ~0.8 through token 100, with task-difficulty conditioning revealing easy (0.84) vs. hard (0.76) signatures. Zhang et al. (2504.05419) report chunk-level probe trajectories rising from 65% at 10% of reasoning to 79% at 100% on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with a characteristic dip at 5-10% of reasoning followed by recovery. Chrabąszcz et al. (2605.18549) demonstrate that temporal probe trajectories with 60+ signal-processing features achieve up to 17pp improvement over static probes, showing that trajectory dynamics capture information invisible to single-timepoint measurements. These temporal profiles suggest that different modes of CoT unfaithfulness — pre-CoT encoding, post-hoc rationalization, reasoning theater, myopic planning, thinking-answer gap — produce distinguishable temporal divergence signatures. Yet no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline: Chrabąszcz et al. provide the closest probe-trajectory methodology but lack any causal contribution component, gap metric, probe calibration, or phenomenon taxonomy; Ballon et al. (2601.23163) provide behavioral causal curves via truncation-reinjection but lack hidden-state measurement; the CMI framework provides layerwise causal audit on ~50 examples but no temporal resolution; Zhao et al.'s True Thinking Score provides per-step causal contribution but no probe-side measurement. The gap between diagnostic information availability and causal contribution IS the phenomenon of interest, not an obstacle.

## Opportunity
The field has independently produced the measurement tools needed for a unified temporal framework, but these tools remain siloed. The opportunity is fourfold:

(1) **Temporal gap measurement.** Despite rapid accumulation of probe measurements (David: 0.84 at t=4; Zhang: 0.82-0.91 on chunks; Yuan: 0.95 overall, 0.787 first-step; Esakkiraja: >90% pre-generation; Chrabąszcz et al.: 91-97% AUROC with max-pooling on trajectories), no work tracks the full-timeline divergence between probe-estimated information availability and intervention-estimated causal contribution. Chrabąszcz et al. (2605.18549) come closest on the probe side — extracting 60+ signal-processing features from probe trajectories across 4 reasoning models and 4 datasets, achieving up to 17pp improvement over static probes on GSM8K — but they target outcome prediction (correctness, harmfulness) rather than the faithfulness gap, and provide no causal contribution measurement. Their work validates that temporal probe trajectories capture dynamics invisible to static probes (confirming our P*(t) direction); our framework extends this via the dual-estimator gap G*(t) = P*(t) − C(t) that requires the additional causal contribution dimension, null-probe calibration, and phenomenon mapping. On the causal side, Ballon et al. (2601.23163) provide behavioral C(t) curves via truncation-reinjection at decile intervals on Qwen3/gpt-oss across GPQA-Diamond and MMLU-Pro — showing monotonic accuracy increase from 30.8-42.3% to 49.0-73.1% with control conditions validating that sequential content (not just context length) matters — but lack hidden-state measurement. The gap between these two measurement traditions IS the framework's niche.

(2) **Phenomenon unification with honest scoping.** The CoT faithfulness literature treats each failure mode as separate: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al. 2603.01437; Esakkiraja et al. 2604.01202), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103), thinking-answer gap. We propose that 2-3 of these are confidently distinguishable via trajectory-shape signatures in the information-contribution gap G*(t), with 4-5 as a stretch goal requiring additional features. The honest scoping — validated through an empirical pilot on real data before committing to full classification — is itself a contribution to a field prone to over-claiming.

(3) **Task-difficulty conditioning.** The ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration show easy→decorative, hard→faithful. David's easy/hard splits (0.84 vs. 0.76 at t=32) provide probe-level evidence. Gjølbye et al. (2605.15454) demonstrate that difficulty is systematically coupled to hidden-state trajectory geometry even after length correction (ρ⊥ = +0.41 for reasoning models vs. −0.06 for baselines on competitive programming), with domain-specific strength. A difficulty-conditioned gap framework can answer the practical question: at what difficulty level does CoT transition from decorative to load-bearing?

(4) **Probe target clarification.** The field has not confronted the distinction between answer-content probes (Cox et al.: binary tasks, ≤9B) and correctness probes (Yuan et al.: up to 72B). A framework that explicitly measures correctness awareness gap — and contrasts it with answer-content gap on applicable tasks — provides the first principled treatment of what 'knowing but not using' means.

Two prior works have combined probing with causal interventions: Kudo et al. (EACL 2026) on synthetic arithmetic, and the CMI framework (2602.03994) on ~50 examples. Wang (2604.15726) formalizes the need via competing hypotheses (H1: latent-mediated, H2: CoT-mediated, H0: serial compute) and proposes compute-audited designs — our ICG framework provides an empirical methodology to distinguish H1 from H2 at each token position. Neither Kudo et al. nor CMI provides: (a) full temporal-position coverage on natural benchmarks, (b) mapping to named faithfulness phenomena, (c) a standalone instance-level diagnostic, (d) systematic multi-model comparison, (e) robustness validation — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) an empirical pilot validating phenomenon separability on real data.

## Landscape
**Probe-based temporal measurement (foundational for our P*(t) component).** Chrabąszcz et al. (2605.18549) is the closest concurrent work: they introduce probe trajectories — tracking concept probability at each generated token — and extract 60+ signal-processing features (volatility, trend, steady-state, temporal segmentation, boundary transients, autocorrelation) via 3-layer MLP probes with Multi-Instance Learning meta-probe across layers. Key results: max-pooling achieves 91-97% AUROC on harmfulness detection (vs. 33-61% for average-pooling, demonstrating average/last-token pooling collapses to near-random); up to 17pp improvement over static probes on GSM8K mathematical error prediction across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours total). Critical differentiators from our framework: (a) NO causal contribution component — they measure only probe accuracy trajectories, not whether CoT causally contributes; (b) NO gap metric — just trajectory vs. static comparison for outcome prediction; (c) NO null-probe calibration or MCT geometric validation — their 3-layer MLP probes are uncalibrated; (d) NO phenomenon taxonomy — they separate correct/incorrect or safe/harmful, not faithfulness modes; (e) NO task-difficulty conditioning. Their 60+ feature extraction methodology is complementary and could enhance our trajectory-shape classification. David (2511.14773) trains per-position probes on reasoning models, finding 0.84 AUC at t=4, stable ~0.8 through t≈100, with easy/hard splits of 0.84 vs. 0.76 at t=32 on Qwen3-8B. Zhang et al. (2504.05419) probe R1-Distill models (7B/32B/70B) for correctness at each reasoning chunk, achieving 0.82-0.91 AUROC on GSM8K/MATH/AIME, with a rising trajectory from 65% at 10% chunk to 79% at 100%, enabling 24% token reduction via early-exit. Yuan et al. (2605.09502) report 0.95 AUROC on Qwen-3B, 0.852 on DeepSeek-R1-7B, 0.787 from first-step hidden states alone, and a concealment gap of 0.197 AUROC between hidden-state (0.787) and text-surface (0.590) classifiers — using correctness probes (right/wrong), not answer-content probes. Esakkiraja et al. (2604.01202) find >90% AUROC pre-generation on Qwen3-4B and GLM-Z1-9B, with a characteristic dip at 5-10% of reasoning and recovery to near-100% by think_end. Cox et al. (2603.01437) use answer-content probes (predicting specific answer A/B on binary tasks: Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) achieving >0.9 AUC on instruction-tuned Gemma-2 (2B, 9B) and Qwen-2.5 (1.5B, 3B, 7B) models, with causal validation via steering (>50% flip rates) — but 'the answer flip rate is negligible against the orthogonal baseline' on the reasoning model GPT-OSS-20B. Additional probing work: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop, probing F1 90-100%, steering 46% recovery).

**The diagnostic-not-causal evidence (motivating our framework).** Yuan et al. (2605.09502) is the decisive study: four interventions — activation steering (at most +4%), probe-guided best-of-N (matches random), self-correction (hurts accuracy −3%), activation patching (destroys coherence at α=0.5) — all fail. Tested on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. Key quote: 'The error signal is a diagnostic readout—a summary statistic of computation quality—not a causal component that can be edited.' Cox et al. (2603.01437) independently confirm: steering fails on reasoning models despite high probe accuracy. This establishes that probe accuracy ≠ causal potency on reasoning models, which is the foundational observation our framework exploits.

**Behavioral trajectory probing (foundational for our C(t) component).** Ballon et al. (2601.23163) introduce the truncation-reinjection protocol: generate full reasoning traces on Qwen3-4B/8B/14B and gpt-oss-20B/120B, truncate at decile intervals (10-100%), reinject with early-stopping suffix, measure answer-choice probability distributions. Key results: accuracy increases monotonically from 30.8-42.3% (no reasoning) to 49.0-73.1% (full trace) on GPQA-Diamond; decision commitment tracks similarly. Three control conditions validate causal content: random tokens (+2.1-4.3%), swapped traces (+3.2-8.7%), and shuffled tokens (+0.3-10.8%) all substantially underperform intact truncated traces (+18.1-33.1%), confirming sequential content — not just context length — drives gains. Stronger models rescue weak-model errors at 43-68% rate with free continuation vs. 28-51% anchoring in base mode. Explicitly disclaims faithfulness-to-internal-computations analysis, making it a direct precursor to our prefix-truncation C(t) estimator. Zhao et al. (2510.24941) introduce the True Thinking Score (TTS), measuring per-step causal contribution via numerical perturbation and ATE computation on DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7. Ye et al. (2602.11201) introduce NLDD, finding a Reasoning Horizon at 70-85% of chain length on 3 models across synthetic tasks. Basu & Chakraborty (2603.22816) propose a decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026) provides another causal measurement approach.

**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize. The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, DialoGPT on StrategyQA (20), TruthfulQA (10), GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors operating on small samples or synthetic tasks.

**Latent-reasoning theory.** Wang (2604.15726) formalizes three competing hypotheses about LLM reasoning: H1 (reasoning is primarily mediated by latent-state trajectories), H2 (reasoning is primarily mediated by explicit surface CoT), H0 (most reasoning gains are better explained by generic serial compute). Proposes compute-audited designs with six experimental arms (baseline, surface manipulation, surface control, latent intervention, latent control, compute-only expansion) and evidence tiers (probe-only = suggestive, compute-matched causal = strongest). Our ICG framework operationalizes Wang's H1/H2 distinction: when G*(t) >> 0, hidden states encode correctness awareness that CoT doesn't contribute (H1-consistent); when G*(t) ≈ 0, CoT is mediating (H2-consistent).

**Temporal hidden-state dynamics (concurrent complementary work).** Gjølbye et al. (2605.15454) study hidden-state trajectory geometry across 11 models (6 reasoning: R1-Distill-Qwen-7B/14B/32B, R1-Distill-Llama-8B, QwQ-32B, Phi-4-Reasoning; 5 instruction-tuned baselines) on competitive programming (500 Codeforces), math (500 MATH), and Boolean SAT (500 SATBench). After length correction (residualizing directness/curvature on log(N)), difficulty remains systematically coupled to trajectory geometry: reasoning models show ρ⊥^D = +0.41 on Codeforces vs. −0.06 for baselines (raw correlations reverse from −0.73 to +0.41), with weaker effects in math (+0.05 vs. −0.07) and non-specific effects in SAT (+0.27 vs. +0.23). Critically, prompt-stage linear probes do NOT mirror these geometric effects — reasoning dynamics manifest during generation, not at input. Their length correction methodology and domain-specificity finding are relevant for our temporal analysis and difficulty conditioning. Furuya & Tanimura (2605.01853) introduce StALT, a training-free trajectory statistic separating correct from incorrect reasoning trajectories. Herrmann et al. (2605.09159) study 'internal polylogue' dynamics: persona vectors tracked temporally across MMLU-Pro in four open-weight models. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, tracking concept-direction alignment per step on Qwen 3-4B; find easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals, achieving 14-70% token savings on R1-Distill/Phi-4/Qwen3.

**Probe calibration and inflation (methodological foundation).** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity. Ravichander et al. (2020) demonstrate properties recoverable even when unused. Voita & Titov (2020) show MDL-based probing reveals accuracy doesn't substantially favor pretrained over random. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning: geometric separability peaks transiently as a 'geometric pulse' while probe accuracy remains high afterward — direct evidence that probe accuracy overestimates information availability. We address this via null-probe calibration: P*(t) = P(t) − P_null(t).

**Trajectory-shape analysis (supporting our shape-based classification).** Entropy trajectory paper (2603.18940): monotonicity predicts reliability regardless of absolute levels (+5.8pp). RQA analysis (2602.06266): temporal features outperform aggregates 36.94% vs. 28.97%. Microsoft trajectory geometry (2604.05655): 0.852 AUC from shape features vs. 0.649 baseline. This literature validates trajectory shapes as diagnostic features.

**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence. Task-difficulty moderation: ICLR 2026 Workshop and Li et al. (2510.22362).

**Reasoning-model internal dynamics.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill.

**Benchmarks, surveys, pathology diagnostics.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Liu et al. (2602.13904): text-level metrics for rationalization/encoded/internalized reasoning. Reasoning Theater (2603.05488). Young (2603.26410). 'Lie to Me' (2603.22582). Various early-exit methods: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT.

**What remains open.** No extant framework provides: (1) a full-timeline information-contribution gap curve pairing calibrated probe trajectories with causal contribution estimation — Chrabąszcz et al.'s probe trajectories are the closest but lack the entire C(t) dimension, gap metric, and calibration; (2) an empirically-validated phenomenon trajectory-shape taxonomy grounded in real within-model, within-dataset G*(t) curves rather than cross-study semi-synthetic assembly; (3) an instance-level diagnostic score derived from the temporal gap; (4) difficulty-conditioned gap analysis with domain-specific nuance (following Gjølbye et al.'s finding of domain-dependent coupling strength); or (5) a principled treatment of the probe-target distinction (correctness vs. answer-content) and its implications for gap interpretation. The calibrated temporal ICG framework is unique in combining all five.

## Approach
We propose the Information-Contribution Gap (ICG) framework: a calibrated, temporally-resolved diagnostic that measures the divergence between information available in hidden states and information that causally contributes to model outputs, tracked across the full chain-of-thought generation trajectory.

**Formal Framework.** Define two time-varying quantities at each token position t during CoT generation:

(i) *Calibrated Information Availability* P*(t): Cross-validated AUROC of a linear probe on layer-l hidden states at position t, calibrated via null-probe normalization (P*(t) = P(t) − P_null(t), following Hewitt & Liang 2019 selectivity, where P_null is trained on shuffled labels). **Probe target: correctness (right/wrong).** We choose correctness over answer-content for three reasons: (a) broader applicability — correctness probes generalize beyond binary/MC tasks (Cox et al.'s answer-content probes are limited to binary A/B on 4 tasks), while correctness probes (Yuan et al.) work across model families up to 72B; (b) the 'diagnostic not causal' finding that motivates the entire framework is specifically about correctness probes (Yuan et al.'s four-intervention failure on correctness probes); (c) correctness gaps are more directly interpretable for faithfulness — G*(t) >> 0 means 'the model's hidden states encode awareness that its answer is right/wrong, but its CoT does not causally reflect this self-monitoring.' On binary/MC task subsets, we additionally train answer-content probes to test whether the 'what answer' gap differs from the 'whether correct' gap — a supplementary analysis testing whether pre-CoT encoding operates on content or meta-cognition. This measures excess correctness awareness above correlative features. We probe at layers L/4, L/2, 3L/4, L to capture layer-wise dynamics. MCT geometric validation (Chun et al. 2602.20338) on 500 examples confirms whether calibrated probe signal reflects geometrically organized information rather than mere retrievability. Note: Chrabąszcz et al. (2605.18549) demonstrate that probe trajectories with 60+ signal-processing features substantially outperform static probes (up to 17pp on GSM8K). We adopt their insight that temporal dynamics are essential, while adding null-probe calibration (which they lack) and extending to the dual-estimator gap. Where applicable, we incorporate their feature categories (volatility, trend, steady-state, boundary transients) as additional trajectory descriptors for phenomenon classification in Phase 3.

(ii) *Causal Contribution* C(t): The causal contribution of CoT up to position t, estimated via three complementary methods: (a) prefix-truncation ablation — measuring P(correct | CoT[:t]) vs. P(correct | full CoT), following Ballon et al.'s (2601.23163) truncation-reinjection protocol with their three control conditions (random tokens, swapped traces, shuffled tokens) to validate that C(t) measures genuine sequential content contribution rather than context-length effects (their finding: shuffled tokens retain +0.3-10.8% vs. intact +18.1-33.1%); (b) paraphrase perturbation — replacing CoT segments with meaning-preserving paraphrases and measuring answer stability; (c) NLDD-based influence scoring (Ye et al. 2602.11201) — measuring how corruption at position t degrades the answer distribution. Using multiple C(t) estimators provides robustness against single-method artifacts, following Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive.

**The Information-Contribution Gap.** G*(t) = P*(t) − C(t). This gap is the primary diagnostic signal:
- G*(t) ≈ 0: Correctness awareness and causal contribution are aligned (necessary for faithfulness)
- G*(t) >> 0: The model encodes correctness awareness it does not causally use in its CoT (diagnostic excess — the model 'knows but doesn't use')
- G*(t) < 0: The CoT contributes to correctness beyond what hidden states encode at that point (information assembled during reasoning)

Because P*(t) is null-probe-calibrated, uniform correlative inflation is removed. C(t) is not subject to probe inflation as it measures behavioral change under intervention. The gap G*(t) is interpretable as 'calibrated correctness awareness the model has but doesn't channel through its CoT at position t.' Following Wang's (2604.15726) H1/H2 framework: G*(t) >> 0 is H1-consistent (latent-mediated reasoning), G*(t) ≈ 0 is H2-consistent (CoT-mediated reasoning).

**Phenomenon Signature Predictions (2-3 confident, 4-5 stretch).** We ground predictions in real probe data but adopt honest scoping informed by the concern that cross-study heterogeneity may overestimate separability:

*Primary targets (HIGH confidence, validated in Phase 0b pilot):*
(i) *Pre-CoT encoding*: G*(t) starts high and stays high. Grounded in: David's 0.84 AUC at t=4, Esakkiraja's >90% pre-generation AUROC, Cox's >0.9 pre-CoT AUC. P*(0) > 0.5 (after calibration), C(t) rises slowly. Shape: large constant gap.
(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. Grounded in: Zhang et al.'s 65%→79% chunk trajectory, Li et al.'s finding that hard→faithful, Ballon et al.'s monotonic accuracy increase with reasoning length. P*(t) rises gradually, C(t) tracks P*(t). Shape: co-rising curves, small/decreasing gap.
(iii) *Post-hoc rationalization*: G*(t) starts moderate, rises during CoT. P*(t) stable (David: ~0.80 from t=4 through t=100), C(t) remains flat despite token generation. Shape: widening gap.

*Stretch targets (MODERATE confidence, require additional features):*
(iv) *Steganographic encoding*: G*(t) dip-and-recovery. Potentially consistent with Esakkiraja's dip at 5-10%. May require multi-layer analysis to separate from noise.
(v) *Reasoning Theater*: EMPIRICAL QUESTION. Under non-uniform inflation, may overlap with pre-CoT encoding or post-hoc rationalization. Additional features — layer-wise P*(t) distribution, C(t) variance under paraphrase perturbation, Chrabąszcz-style signal features (autocorrelation, boundary transients, dwell-time run-lengths) — may enable separation. Whether Theater is cleanly separable is reported honestly with confusion matrices.

**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** We construct semi-synthetic G*(t) curves grounded in real published data to generate testable predictions about trajectory-shape separability — but we do NOT treat this as evidence of real-data separability (published measurements come from different models, datasets, and setups, introducing heterogeneity that does not match within-dataset variance). Instead, the simulation identifies: (a) which trajectory features are most discriminative in principle, (b) what minimum effect sizes real-data classification needs to achieve, (c) where non-uniform inflation causes theoretical overlap between phenomena. I_probe(t) profiles drawn from published measurements (David, Zhang, Esakkiraja, Yuan), C(t) profiles modeled from NLDD (Ye et al.) and TTS (Zhao et al.) data, non-uniform inflation calibrated against Chun et al.'s MCT finding. The real validation comes from Phase 0b.

**Phase 0a: Gap Characterization (Weeks 1-2.5).** Three objectives on 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):
(i) Construct empirical P*(t) and C(t) curves at token-level resolution
(ii) Validate null-probe calibration: P_null(t) shows high accuracy (inflation exists) but P*(t) shows meaningful variance (calibration reveals structure)
(iii) Characterize causal potency: following Cox et al.'s protocol, measure answer flip rates via probe-direction steering on reasoning vs. instruction-tuned models

Expected outcome (base case): Causal potency is low on reasoning models, confirming the diagnostic-not-causal property and validating the ICG framework's interpretive power. If causal potency is unexpectedly high, this is an exciting upgrade. Either outcome is scientifically valuable.

**Phase 0b: Empirical Pilot for Phenomenon Separability (Weeks 2.5-4).** This phase validates that trajectory-shape classification is feasible on real data before committing to the full pipeline. On the SAME model (R1-Distill-Qwen-7B) and datasets (GSM8K + MATH-500, 1000 examples), construct real G*(t) curves and test whether at least 2 phenomena produce distinguishable trajectories. Protocol: (i) partition examples by difficulty quintile and model behavior (easy-correct with high P*(0) → pre-CoT encoding candidates; hard-correct with rising P*(t) tracking C(t) → genuine reasoning candidates; incorrect with stable P*(t) and flat C(t) → post-hoc rationalization candidates); (ii) compute full G*(t) for each partition; (iii) test effect size d > 0.5 on at least 2 trajectory features between partitions. Apply Gjølbye et al.'s (2605.15454) length correction (residualizing trajectory features on log(N)) to ensure differences are not conflated with generation-length effects. Success criterion: d > 0.5 between at least 2 partitions on 2+ features. If d < 0.3 across all features, downscope to a characterization paper (gap exists and varies with difficulty, but trajectory shapes are not cleanly phenotypic) — still a strong contribution given no prior full-timeline G*(t) measurement exists.

**Phase 1: Full ICG Construction (Weeks 4-9).** Conditional on Phase 0b showing separability (d > 0.5). Extend to 4 models (add QwQ-32B or R1-Distill-32B) × 4 benchmarks (add GPQA-Diamond or AIME). Full calibrated P*(t) with null-probe normalization + MCT concordance check on 500 examples. Three C(t) estimators with Ballon et al.-style controls (random, swap, shuffle baselines). Cross-reference with TTS (Zhao et al.) at step boundaries. Bootstrap confidence intervals on G*(t).

**Phase 2: Task-Difficulty Conditioning (Weeks 7-11).** Partition each benchmark into difficulty quintiles (using model accuracy as proxy). Measure G*(t) per quintile. Hypothesis grounded in David's easy/hard data, Li et al.'s finding, and Gjølbye et al.'s difficulty-geometry coupling: easy problems show large persistent gap (decorative CoT), hard problems show converging gap (load-bearing CoT). Following Gjølbye et al., apply length correction and report domain-specific effects — expecting stronger effects on math/code benchmarks than MMLU, given their finding of ρ⊥ = +0.41 on Codeforces vs. +0.05 on MATH. The transition point — where G*(t) shifts from decorative to genuine — provides practical guidance on when CoT adds value.

**Phase 3: Phenomenon Classification and Robustness (Weeks 9-14).** Apply trajectory-shape classification to real data. Target: 2-3 cleanly separable phenomena, with 4-5 reported honestly including overlap. Incorporate Chrabąszcz et al.'s feature categories (volatility, trend, boundary transients, autocorrelation) alongside our gap-specific features (initial G* value, G* slope, convergence rate, dC/dt locality). Six robustness ablations following Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection (single best vs. multi-layer); (c) C(t) estimator agreement (prefix vs. paraphrase vs. NLDD); (d) gap normalization method; (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content on binary/MC subsets). Report sensitivity ranges across all dimensions.

**TIF Score.** Temporal Information-contribution Faithfulness score: normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s text-level metrics.

**Paper Focus (Tightened).** Core contributions: (1) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al.'s probe trajectories — demonstrating the value added by the causal contribution dimension and gap metric; (2) Phase 0b empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real within-model, within-dataset data; (3) task-difficulty conditioning revealing the decorative→load-bearing transition with domain-specific strength following Gjølbye et al.'s nuance. Supporting: robustness ablations (6 dimensions); TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness probe comparison; semi-synthetic simulation as hypothesis generation.

**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT cross-reference. Gjølbye-style length correction on all temporal analyses.

## Resource Estimate
{'manual': {'gpu_hours': '~830 H100-hours (Phase 0a characterization: 80 hrs [3 models × 3 datasets, probe training + prefix ablation + steering tests]; Phase 0b empirical pilot: 30 hrs [1 model × 2 datasets, full G*(t) construction + partition analysis + length correction]; Phase 1 full ICG: 120 hrs [4 models × 4 benchmarks, multi-layer probes + 3 C(t) estimators]; Phase 2 difficulty conditioning: 50 hrs; Phase 3 phenomenon classification + robustness ablations: 50 hrs; NLDD on 32B model: 250 hrs [primary bottleneck — up to 20 perturbation positions × 5K examples × forward passes]; NLDD on 7B/14B models: 100 hrs; MCT geometric validation: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic simulation: 50 hrs [mostly CPU, some GPU for validation])', 'timeline': '15-17 weeks (2 researchers: 4 weeks Phase 0a+0b characterization + pilot; 5 weeks Phase 1 full ICG; 4 weeks Phases 2-3 in parallel with NLDD; 2-3 weeks writing + ablations)', 'estimated_gpu_cost': '$2,500 at ~$3/H100-hour (cloud spot pricing)', 'storage': '3-5 TB (4 layers per model, fp16); reducible to ~1.5 TB via PCA'}, 'human_in_loop': {'gpu_hours': '~830 H100-hours', 'timeline': '13 weeks (1 researcher + Claude for experiment design and analysis)', 'claude_api_cost': '$350', 'estimated_gpu_cost': '$2,500'}, 'auto_research': {'gpu_hours': '~830 H100-hours', 'timeline': '11 weeks', 'claude_api_cost': '$700', 'estimated_gpu_cost': '$2,500', 'speed_bottleneck': 'NLDD on 32B (~250 H100-hours, ~30% of total compute) is the primary bottleneck. Each NLDD evaluation requires corrupting reasoning at multiple positions and measuring logit degradation — O(T × N) forward passes where T≈20 perturbation positions and N≈5K examples. For 32B models, this cannot be easily parallelized beyond 8-GPU data parallelism. Secondary: 671B subset (8×H100, ~50 hrs); MCT geometric validation (~50 hrs). Phase 0b pilot (30 hrs) provides early go/no-go signal before committing full Phase 1-3 compute.'}}

## Inspired By
The convergence of five independent lines of evidence — (a) Cox et al.'s finding that answer-content probe steering fails on reasoning models despite high accuracy; (b) Yuan et al.'s systematic demonstration that four interventions all fail on correctness probes, establishing 'diagnostic not causal'; (c) the temporal probe dynamics now empirically characterized by David (0.84 AUC at t=4, stable ~0.8), Zhang et al. (chunk-level rising trajectory), Esakkiraja et al. (pre-generation >90% with dip-recovery), and Chrabąszcz et al. (60+ trajectory features capturing dynamics invisible to static probes, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection protocol demonstrating monotonic behavioral C(t) curves with rigorous controls (sequential content +18.1-33.1% vs. shuffled +0.3-10.8%) — all pointing to the same insight: the gap between diagnostic information availability and causal contribution IS the phenomenon of interest. Additionally inspired by: Wang's (2604.15726) formalization of H1/H2/H0 hypotheses providing the theoretical scaffold for what our framework empirically measures; Gjølbye et al.'s (2605.15454) finding that difficulty-geometry coupling is domain-specific and requires length correction; Herrmann et al.'s concurrent temporal persona-vector dynamics; and the trajectory-shape literature showing shapes can distinguish phenomena regardless of absolute-value calibration.

## Target Venues
- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)
- ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)

## Key References
- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al., arXiv 2605.18549)
- Probing the Trajectories of Reasoning Traces in Large Language Models (Ballon et al., arXiv 2601.23163)
- LLM Reasoning Is Latent, Not the Chain of Thought (Wang, arXiv 2604.15726)
- Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al., arXiv 2605.15454)
- Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502)
- Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437)
- Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773)
- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (Zhang et al., arXiv 2504.05419)
- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)
- Can Aha Moments Be Fake? True Thinking Score (Zhao et al., arXiv 2510.24941)
- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)
- Do LLMs Experience an Internal Polylogue? (Herrmann et al., arXiv 2605.09159)
- LLMs Faithfully and Iteratively Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)
- When Chains of Thought Don't Matter: Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)
- Spatiotemporal Hidden-State Dynamics / StALT (Furuya & Tanimura, arXiv 2605.01853)
- Mapping Faithful Reasoning / Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)
- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)
- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)
- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)
- Emergent Manifold Separability / MCT (Chun et al., arXiv 2602.20338)
- Tracing the Traces: Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)
- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)
- Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019)
- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)
- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)
- Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940)
- Is My Model Mind Blurting? RQA of Reasoning Dynamics (arXiv 2602.06266)
- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)
- Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128)
- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)
- Breaking the Chain (Somov et al., arXiv 2603.16475)
- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)
- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)
- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)
- Reasoning Theater (Boppana et al., arXiv 2603.05488)
- No Global Plan in CoT (Xu et al., arXiv 2602.02103)
- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)
- CoT Monitorability via Information Theory (Anwar et al., arXiv 2602.18297)
- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)
- Demystifying Reasoning Dynamics with MI (Qian et al., NeurIPS 2025, arXiv 2506.02867)
- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)
- Why Models Know But Don't Say (Young, arXiv 2603.26410)
- Lie to Me (arXiv 2603.22582)
- Step-Level Hallucination via Transport Geometry (Alvarez & Baheri, arXiv 2605.13772)
- From Reasoning to Answer (arXiv 2509.23676)
- SAE Reasoning Features (arXiv 2503.18878)
- FRIT (Swaroop et al., arXiv 2509.13334)
- Solution Hides in Hidden States (arXiv 2604.23351)
- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)
- LEACE: Perfect Linear Concept Erasure (Belrose et al., NeurIPS 2023, arXiv 2306.03819)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d09421d3-a550-4f1b-b37a-d865a30ff1fc",
  "type": "user",
  "uuid": "ada979c6-37ca-4d87-975a-b00aeb2c65b0",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:46:49.274Z_

```json
{
  "parentUuid": "ada979c6-37ca-4d87-975a-b00aeb2c65b0",
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
  "uuid": "0e204796-62f2-43fd-8c49-3ad31b3aafaf",
  "timestamp": "2026-05-20T03:46:49.274Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:46:49.274Z_

```json
{
  "parentUuid": "0e204796-62f2-43fd-8c49-3ad31b3aafaf",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4f8799c8-945b-4e78-8f77-1901370f7eb1",
  "timestamp": "2026-05-20T03:46:49.274Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct my assessment. Le…",
  "leafUuid": "4f8799c8-945b-4e78-8f77-1901370f7eb1",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta judge synthesis of three CoT faithfulness proposal reviews",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:47:27.305Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them as the Meta Judge.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 中
- Significance: 中-强
- Related Work: 强
- Probability: [22% - 33%] 中位 27%
- Key risks: Commensurability of P*(t) and C(t), "Obvious next step" novelty challenge


**Reviewer 2:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [22% - 35%] 中位 28%
- Key risks: "Integration, not innovation" challenge, P*(t) and C(t) commensurability
**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [22% - 33%] 中位 27%
- Key risks: "Natural next step" not "surprising insight", G*(t) interpretability

The three probability estimates cluster tightly around 27-28%, with all reviewers identifying similar concerns about whether this represents genuine innovation or a natural extension of existing work. The commensurability issues with P*(t) and C(t) appear consistently across reviewers as a technical risk. Looking at the anomalies, there are a few points that only individual reviewers flagged: Reviewer 1 caught a logical inconsistency in the widening gap prediction where stable P*(t) and flat C(t) should produce a constant rather than widening gap; Reviewer 2 implicitly raised gaps in related work coverage around answer-conditioned probing; and Reviewer 3 raised concerns about using correctness probes as a faithfulness proxy, questioning whether they actually measure meta-cognitive processes versus faithfulness itself.

Now I'm recalibrating which concerns actually appear across multiple reviewers—the non-uniform inflation issue shows up in both Reviewer 1 and 3's critiques, while the correctness probe validity concern appears most prominently in Reviewer 3 with some mention from Reviewer 2. Let me reorganize these findings to properly distinguish between what's truly anomalous versus what has broader support. fundamental methodological concern
5. Core idea is "natural next step" / "obvious combination"
6. Phase 0b is the make-or-break bet
7. Trivial alternative threat is moderate (mitigated by temporal resolution + taxonomy if Phase 0b succeeds)

**Moderate consensus (2/3):**
1. Non-uniform inflation concern (R1, R3)
2. Post-hoc rationalization prediction may have logical issues (R1 explicitly, arguably implicit in others)

**Only 1 reviewer:**
1. R1's specific logical flaw in "widening gap" prediction (P*(t) stable + C(t) flat = constant)
2. R3's emphasis on correctness probe ≠ faithfulness proxy concern

**Convergence assessment:**
The standard deviation of the median estimates is extremely tight at around 0.47%, indicating near-perfect alignment across all three reviewers. All three independently converged on a 22% lower bound, with upper bounds clustering at 33% or 35%. Given this extraordinarily high consensus, I'm taking the median range of [22% - 33%] with a central estimate of 27%, which feels appropriately confident without over-adjusting based on the agreement alone.

Now I'm looking at the implementation details the proposal outlines and what the reviewers flagged: approximately 830 H100-hours of compute, a 15-17 week timeline with two researchers, $2,500 in GPU costs, and the need for specific model variants like DeepSeek-R1-Distill and QwQ-32B across four evaluation benchmarks including GSM8K, MATH-500, MMLU, and GPQA-Diamond.

The key constraint is that NLDD on the 32B model becomes the bottleneck at around 250 hours, but the good news is this doesn't require new benchmark development or model training—just lightweight probe training—and human annotation is minimal since it leverages existing benchmarks with established answer keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f8799c8-945b-4e78-8f77-1901370f7eb1",
  "isSidechain": false,
  "requestId": "req_011CbD8ndezmTtp6biG8zH5T",
  "type": "assistant",
  "uuid": "e089e799-577e-4827-b770-a10e9372b9b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UXXmW7NxzKwXsCCBSKVKQq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 32150,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3736,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 32150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32150
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

_source line 9 · 2026-05-20T03:48:13.241Z_

【阶段】: Meta Judge
【三次中位】: [27%, 28%, 27%]  std=0.5%
【共识维度】:
- **Novelty = 中**（3/3）：核心 idea 是 probe trajectory + causal contribution 的 temporal combination，属于 integration/synthesis novelty 而非 conceptual breakthrough。"Natural next step" / "obvious combination" 判定一致
- **Significance = 中-强**（3/3）：研究问题重要（CoT faithfulness 是 AI safety 核心问题），但 expected finding 中最 robust 的部分（easy→decorative, hard→genuine）已被先行工作建立，真正的 significance uplift 高度依赖 Phase 0b 的 phenomenon separability 结果
- **Related Work = 强**（3/3）：30-40+ 篇引用覆盖全面，描述准确，差异化定位清晰（特别是对 Chrabąszcz et al. 的定位）
- **P\*(t) 与 C(t) 的 commensurability 是根本性方法论缺陷**（3/3）：AUROC 与 accuracy change / NLDD score 不在同一度量空间，G\*(t) = P\*(t) − C(t) 的减法缺乏数学 justification——这是三位审稿人一致判定的最核心技术风险
- **Phase 0b 是核心赌注**（3/3）：如果 phenomenon trajectory-shape 不可区分，论文退化为 "we measured the gap, it exists"，在极度拥挤的领域中增量贡献不足
- **Trivial alternative 威胁为中等**（3/3）：简化版（static pre-CoT probe vs. final accuracy + difficulty stratification）可捕获核心信号，增量价值完全取决于 temporal resolution + taxonomy 是否成功
- **领域极度拥挤**（3/3）：2025-2026 年 6 个月内 40+ 篇高度相关论文，被视为 incremental 的风险实质性存在

【异常维度】:
- R1 独有：post-hoc rationalization 的 "widening gap" 预测存在逻辑缺陷——如果 P\*(t) 在 t=4 后稳定在 ~0.80 且 C(t) flat，gap 应为常数而非 widening。这是一个具体且有效的技术观察，但属于单个 phenomenon prediction 的修正，不改变整体判定
- R3 独有：强调 correctness probe ≠ faithfulness proxy 的概念距离——模型可以进行 faithful reasoning 但不编码 meta-cognitive self-monitoring，此时 correctness gap 高但 CoT 仍 faithful。这是一个有见地的概念性挑战，但 R2 也在 trivial alternative 讨论中隐含涉及，降权处理合理

【最终概率】: [23% - 33%] 中位 27%
【一致性】: 高（std = 0.5%，三位审稿人在所有 rubric 维度上判定完全一致）
【综合理由】:
三位审稿人在所有核心维度上达成罕见的高度一致：Novelty=中、Significance=中-强、Related Work=强，概率中位仅差 1 个百分点（27%/28%/27%）。这种一致性表明评估是稳健的，不需要额外的保守调整。

概率上界（~33%）由 Novelty 天花板决定：核心 idea 是将两条已成熟研究线（probe trajectory + causal contribution）在时间维度上拼合，三位审稿人均判定这是 "natural next step" 而非 "surprising insight"。即使 Phase 0b 完全成功、实验执行完美，一个 integration novelty 在拥挤领域中的上界也难以突破 35%。

概率下界（~23%）由 Related Work 的强势和 Significance 的真实性托底：研究问题确实重要、文献覆盖确实全面、实验设计确实详尽。即使审稿人对 novelty 持怀疑态度，execution quality 会防止被直接 reject。

中位 27% 反映的核心矛盾：这是一篇"方向正确、执行详尽、positioning 精准的 synthesis 工作"，但在一个 6 个月出 40+ 篇论文的领域，synthesis novelty 的 acceptance bar 极高。Commensurability 问题作为三人共识的致命风险点，如果在论文中不解决，几乎必然被审稿人 flag——这将概率进一步锁定在中位 27% 附近而非向上突破。

异常维度（R1 的 widening gap 逻辑缺陷、R3 的 correctness-faithfulness 概念距离）虽然各自只有 1 人明确提出，但都是有效观察——它们不改变概率估计但增加了 proposal 需要修补的具体点。

【建议】: 边缘（可尝试优化，但 idea 的 novelty 天花板严格限制上界；如果 commensurability 问题能找到令人信服的技术解决方案 + Phase 0b 成功，有机会推至 30-35% 区间）

【实施评估】:
- **计算资源**: ~830 H100-hours，约 $2,500（云端 spot pricing）。NLDD on 32B 模型（~250 hrs）是主要瓶颈，受限于 O(T×N) forward passes 的串行性。671B 子集验证需要 8×H100。总体而言计算需求中等偏低，对拥有 A100/H100 集群访问权限的学术组完全可行
- **数据需求**: 全部使用公开 benchmark（GSM8K, MATH-500, MMLU, GPQA-Diamond/AIME）+ 公开模型（DeepSeek-R1-Distill 系列, QwQ-32B, Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct）。无需私有数据，数据可得性无风险
- **人工介入**: 极少。无需人工标注（benchmark 均有 ground truth），无需专家评审。主要人工工作在实验设计调优和结果分析。2 名研究者 + AI 辅助即可
- **训练需求**: 仅需训练线性 probe（轻量级，每个配置几分钟到几十分钟）。不需要 LLM 微调或预训练。probe 训练不是瓶颈
- **新 Benchmark**: 不需要。使用现有 benchmark + 现有 faithfulness benchmark（FaithCoT-Bench）进行 TIF 验证
- **预估周期**: 15-17 周（2 名研究者），可压缩至 11-13 周（with AI 辅助并行化）。Phase 0b 在第 2.5-4 周提供早期 go/no-go 信号，这是一个好的风险管理设计——如果 Phase 0b 失败（d < 0.3），可在第 4 周止损降级为 characterization paper，避免沉没成本

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e089e799-577e-4827-b770-a10e9372b9b0",
  "isSidechain": false,
  "requestId": "req_011CbD8ndezmTtp6biG8zH5T",
  "type": "assistant",
  "uuid": "a8c98e97-758e-4bfb-9702-cdce74c04a20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UXXmW7NxzKwXsCCBSKVKQq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 32150,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3736,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 32150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32150
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct my assessment. Le…",
  "leafUuid": "a8c98e97-758e-4bfb-9702-cdce74c04a20",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta judge synthesis of three CoT faithfulness proposal reviews",
  "sessionId": "70128e95-59eb-4945-b0d3-37d8856228c9"
}
```

---
