# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/83657097-a827-4c8b-b603-51ef6353df36.jsonl`
- **Structured JSON:** [`340728c5e3090d1bf6ae.json`](../../sessions/34/340728c5e3090d1bf6ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:56:05.709Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:56:05.709Z",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. Self-Correction Bench (arXiv:2507.02778, submitted ICLR 2026): 确立了 LLM 自纠错盲区概念，14 个非推理模型平均 64.5% 盲区率，\"Wait\" trick 降低 89.3%——但仅在 GSM8K/PRM800K 数学任务上、以 problem-level 粒度进行测量。论文确认存在，描述准确。\n\n2. CURE (arXiv:2604.12046, Apr 2026): 在 biography generation 上实现 39.9% claim-level accuracy 提升，通过 &lt;think>→&lt;decompose>→&lt;answer> 协议进行 claim-level 校准。**需要多阶段微调 (SFT+DPO+GRPO)**，仅做 calibrated abstention 不做 correction。与 proposal 共享任务域但方法论完全不同。确认存在，描述准确。\n\n3. Selective Abstraction / SA (arXiv:2602.11908, Feb 2026): 将 response 分解为 atomic claims，用 confidence-based abstraction 替换 uncertain claims，AURC 提升最高 27.73%。仅做 abstraction 不做 correction。确认存在，描述准确。\n\n4. CAG (arXiv:2605.01749, May 2026): Exploration-Commitment Decoupling，VeriScore 67.79%→79.80%。需要微调，suppresses 而非 corrects unreliable claims。确认存在，描述准确。\n\n5. DeepMind PANL correctability (arXiv:2604.22271, Apr 2026, Kumaran et al.): 发现 post-answer newline token 处的 residual-stream activations 可以预测 correction success (AUROC=0.614)，而 behavioral confidence 仅 0.524。需要 white-box access，仅在 TriviaQA/MNLI problem-level 上测试。确认存在，描述准确。\n\n6. \"Knowing but Not Correcting\" (arXiv:2605.05957, May 2026): 发现 correction suppression——模型在 isolation 中能纠正错误但在 task context 中抑制纠正（19-90% suppression rates across 8 models）。Hidden-state similarity >0.99 表明模型内部识别了错误但选择 comply。确认存在，描述准确。\n\n7. CyberCorrect (arXiv:2605.17305, May 2026): 三模态 error detector (self-consistency 0.4 + verbalized confidence 0.35 + logic-chain verification 0.25)，在 reasoning tasks 上 79.8% accuracy，41% reduction in over-correction。需要 reasoning chains，在 problem-level 上操作。确认存在，描述准确。\n\n8. Functional Dissociation (arXiv:2604.19974, Apr 2026): SAE 分析表明 uncertainty 和 correctness 由不同 feature populations 编码；suppress uncertainty features 导致 accuracy 下降最高 10.21%，而 suppress incorrectness features 几乎无影响。确认存在，描述准确。\n\n9. FactSelfCheck (arXiv:2503.17229, 2025): Fact-level black-box hallucination detection，KG-style triple representation，35.5% vs 10.6% factual improvement for fact-level vs sentence-level。确认存在，描述准确。\n\n10. ConFix (arXiv:2411.13343, 2024): Fact-level confidence calibration + self-correction，high-confidence facts bootstrap correction of low-confidence facts。确认存在，描述准确。\n\n11. FactCorrector + VELI5 (arXiv:2601.11232, Jan 2026): Graph-inspired correction pipeline + 17,522 instance benchmark with injected errors. 67.4% correction of incorrect atoms with structured feedback + external knowledge. 确认存在，描述准确。\n\n12. CSS (arXiv:2604.17487), CLC (arXiv:2502.19110), VeriFY (arXiv:2602.02018), I-CALM (arXiv:2604.03904): 均为 claim-level confidence/calibration-based abstention 方法，无一尝试 correction。\n\n- **调研总结**: 这个领域在 2025-2026 经历了爆发式增长，两个方向并行发展但未交汇：(A) self-correction blind spot 研究停留在 math/reasoning + problem-level 粒度；(B) claim-level factuality 处理已形成拥挤的 confidence-based abstention 赛道（6+ papers），但无一尝试 correctability-based correction routing。Proposal 精准定位在这两个方向的交叉空白处——将 blind spot 分析下沉到 fact-level 粒度、将 correctability（而非 confidence）作为 routing signal。领域文献引用高度准确，未发现 misrepresentation。\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative 是：**直接用 confidence threshold 做 correction routing**——即把 SA/CURE 的 confidence signal 原封不动地用来决定 \"纠正 vs. 放弃\"，而非 proposal 所提出的 correctability classifier。\n\n这个 trivial alternative 的威胁程度：**中等但可控**。Proposal 显式引用了三条独立证据来论证 confidence ≠ correctability：(1) DeepMind PANL 结果 behavioral confidence AUROC 仅 0.524 vs. internal AUROC 0.614；(2) Functional Dissociation 证明 uncertainty 和 correctness 由不同 feature populations 编码；(3) 6+ papers 实现了强 calibration 但无法 enable correction。Proposal 还将 confidence-threshold correction 作为 explicit baseline (h)。如果实验证实 confidence-threshold correction 已经接近 correctability classifier 的效果，那 novelty 确实受损——但 proposal 的 pre-registered 设计已经预见了这一风险，且即使 classifier 表现平庸，correctability-confidence dissociation 本身作为 empirical finding 仍有价值。\n\n第二个 trivial alternative：\"Wait\" trick 直接迁移到 factual claims 上就行了。Proposal 将此作为核心假设来测试而非假定不行，设计了专门的 ablation。如果 \"Wait\" 在 factual claims 上同样有效（>50% blind spot reduction），proposal 承认这是重要的 simplifying finding 并 reframe 贡献。这种 dual-outcome 设计是合理的。\n\n**增量价值所在**：即使两个 trivial alternatives 都部分有效，proposal 仍提供：(a) 首个 fact-level 粒度的 blind spot 系统测量（目前零篇论文做过这个）；(b) claim-type-stratified 盲区分析；(c) correctability vs. confidence 的 empirical dissociation 在 factual domain 的首次验证。这些 benchmark 和 characterization 贡献不受 trivial alternative 影响。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链：\n\n**假设 1：Math 领域的 blind spot 现象能推广到 knowledge-intensive generation**\n- 支撑度：中等。Correction suppression (arXiv:2605.05957) 已在 factual domain 发现 19-90% suppression rates，间接支持 blind spot 在 factual domain 存在。但 blind spot 的 **heterogeneity across claim types** 尚无直接证据——这确实是 proposal 要测试的核心假设，而非预设结论。合理。\n\n**假设 2：\"Wait\" trick 对 factual claims 效果显著弱于 math**\n- 支撑度：中等偏强。Self-Correction Bench 的 training-data analysis 表明 correction markers 集中在 reasoning datasets（中位 30-170/response）但在 non-reasoning text 中几乎不存在（95th percentile = 1），这为 \"Wait\" 在非推理领域失效提供了间接证据。Correction suppression 的机制也在更深层（hidden-state level）而非 activation failure。但这仍是 hypothesis 而非 established fact，proposal 正确地将其设计为可测试的。\n\n**假设 3：Black-box behavioral features 能 outperform confidence baseline 预测 correctability**\n- 支撑度：较弱，这是最大风险点。DeepMind 的结果表明 white-box internal representations 可以预测 correctability (AUROC=0.614)，但 behavioral confidence 仅 0.524。Proposal 认为加入 claim type + specificity + detection-correction gap 等 features 可以弥补 black-box 的劣势——但没有先验证据表明这些 features 对 correctability 有预测力。CyberCorrect 的三模态 detector 在 reasoning tasks 上有效，但其 logic-chain verification component 不适用于 factual claims。Proposal 的 pre-registered AUROC>0.58 阈值设置合理（参照 DeepMind 的 0.614 和 confidence baseline 的 0.524），但 classifier 性能仍是最大的不确定性。\n\n**假设 4：Correctability 和 confidence 在 factual domain 是 empirically dissociable 的**\n- 支撑度：较强。Functional Dissociation 已在 SAE level 证明了这一点；DeepMind PANL 结果在 behavioral level 也支持。但这些都不是在 long-form factual generation 的 atomic claim level 上验证的——proposal 要做的正是这个 gap 的 empirical 填充。\n\n**最薄弱环节**：假设 3——black-box correctability classifier 能否达到有意义的 AUROC。如果 classifier 仅达到 0.53-0.55（接近 confidence baseline），则 SFC pipeline 的 practical value 大幅缩水。不过 proposal 已设计了 graceful degradation path：即使 classifier 表现平庸，benchmark + blind spot characterization + \"Wait\" ablation + dissociation analysis 仍有独立贡献。\n\n【3 维度打分】:\n\n1. **Novelty: 中偏强** — \n   Proposal 定位了一个真实的、可验证的空白交叉点：self-correction blind spot 研究 (Self-Correction Bench, Error Depth Hypothesis) 停留在 math/problem-level；claim-level factuality 处理已拥挤但全部走 confidence-based abstention 路线 (SA, CSS, CLC, CURE, CAG, VeriFY = 6+ papers)；correctability prediction 只有 white-box (DeepMind PANL) 和 reasoning-only (CyberCorrect) 方案。**将 blind spot 分析下沉到 atomic claim level + correctability-based routing 在 factual domain 的首次探索** 这个组合确实是 unoccupied 的。\n\n   降分因素：这是一个 **\"自然延伸\" 型 novelty** 而非 **\"反直觉发现\" 型 novelty**。核心 idea 可以概括为 \"把 self-correction blind spot 的分析从 problem-level math 搬到 claim-level facts，然后用 correctability 替代 confidence 做 routing\"——方向正确但不令人 surprised。审稿人可能会说 \"interesting gap, obvious to fill\"。与之对比，Functional Dissociation 或 Correction Suppression 的发现本身具有更强的 surprise factor。\n\n2. **Significance: 中偏强** — \n   研究问题的重要性很高：LLM 在 knowledge-intensive generation 中的 factual accuracy 是部署的核心瓶颈；6+ papers 在同一问题上发力但都走了 abstention 路线说明需求真实。如果 blind spot 确实在 claim types 间存在 heterogeneity，且 correctability ≠ confidence 在 factual domain 得到验证，这对整个 claim-level factuality handling 领域的方向有指导意义。\n\n   降分因素：SFC pipeline 本身的 practical impact 取决于 classifier 性能，如果 AUROC 仅略高于 confidence baseline，downstream improvement 可能有限。不过 benchmark 和 characterization 的独立价值不受此影响。\n\n3. **Related Work: 强** — \n   这是该 proposal 最突出的优势之一。引用的 25+ 篇论文全部经核实存在且描述准确。领域格局的梳理极其系统：清晰区分了 (a) blind spot literature (math/problem-level), (b) fact-level hallucination literature, (c) correctability prediction (white-box/reasoning-only), (d) selective claim-level handling (confidence-based abstention) 四条线索，并在交叉点定位自己。差异化定位非常清晰——\"ALL 6+ papers use confidence, NONE attempt correctability-based correction\"。这种 exhaustive 且 accurate 的 landscape mapping 在 proposal 阶段是少见的。\n\n   唯一微弱不足：对 CorrectBench (arXiv:2510.16062) 的引用缺失——这是另一个系统评估 self-correction 的 benchmark，虽然也集中在 reasoning tasks 但应提及以显示更完整的 awareness。\n\n【概率估计】: 28% - 38%，中位 33%\n\n【估计理由】: \n- **Novelty (中偏强)** 和 **Significance (中偏强)** 共同支撑了 30%+ 的基础概率。Gap 是真实的、定位精准、related work 梳理极强。\n- **向上受限的主要因素**：核心 novelty 是 \"natural extension\" 型而非 \"surprising insight\" 型。审稿人很可能认为 \"当然 blind spot 在 factual claims 上也存在，当然 correctability ≠ confidence\"——核心发现如果 positive，部分审稿人会说 \"I would have guessed this\"。这限制了上界在 38% 而非更高。\n- **向上支撑因素**：(1) 精准的空白定位和系统的 landscape coverage 在 rebuttal 中很有价值；(2) dual-outcome 设计和 pre-registered thresholds 显示方法论成熟度；(3) 如果 \"Wait\" ablation 产生 surprising 结果（无论正面还是负面），可以显著提升 narrative impact。\n- **向下风险**：如果 classifier AUROC 仅 0.53-0.55 且 \"Wait\" 在 factual domain 意外有效（>50% reduction），proposal 的核心 SFC 贡献会被大幅削弱，此时需要靠 benchmark + characterization 支撑——作为 resource paper / analysis paper 的概率可能降至 25% 左右。\n\n【主要风险】:\n1. **\"Natural extension\" novelty ceiling**：核心贡献被审稿人视为 \"obvious gap to fill\" 而非 \"surprising finding\"——blind spot 从 math 到 facts 的迁移、correctability ≠ confidence 的论证，方向上都不令人意外，只是没人做过。这可能导致 \"incremental\" 的评价。\n2. **Correctability classifier 的 black-box 性能天花板**：如果 claim-type + specificity 等 features 对 correctability 的预测力有限（AUROC 接近 confidence baseline 的 0.524），则 SFC 的 practical value 和 \"correctability ≠ confidence\" 的论证力度都会受损，proposal 的 Phase 3-4 贡献会大幅缩水。\n```\n\nSources:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)\n- [CURE: Think Through Uncertainty (arXiv:2604.12046)](https://arxiv.org/abs/2604.12046)\n- [Selective Abstraction (arXiv:2602.11908)](https://arxiv.org/abs/2602.11908)\n- [CAG: Calibration-Aware Generation (arXiv:2605.01749)](https://arxiv.org/abs/2605.01749)\n- [DeepMind PANL: How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)\n- [Knowing but Not Correcting (arXiv:2605.05957)](https://arxiv.org/html/2605.05957v1)\n- [CyberCorrect (arXiv:2605.17305)](https://arxiv.org/abs/2605.17305)\n- [Functional Dissociation via SAEs (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)\n- [FactSelfCheck (arXiv:2503.17229)](https://arxiv.org/abs/2503.17229)\n- [FactCorrector + VELI5 (arXiv:2601.11232)](https://arxiv.org/abs/2601.11232)\n- [CSS (arXiv:2604.17487)](https://arxiv.org/html/2604.17487)\n- [ConFix (arXiv:2411.13343)](https://arxiv.org/pdf/2411.13343)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have a comprehensive picture of the literature. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Self-Correction Bench, arXiv:2507.02778] (submitted ICLR 2026): 定义了 self-correction blind spot 概念，14 个非推理模型平均 64.5% blind spot rate（GSM8K/PRM800K）。'Wait' trick 减少 blind spot 89.3%。关键限制：仅在 math 任务、problem-level 粒度。这是本 proposal 的直接上游工作和出发点。\n- [CURE, arXiv:2604.12046] (Apr 2026): Claim-level calibration for biography generation，&lt;think>→&lt;decompose>→&lt;answer> protocol，39.9% claim-level accuracy improvement。需要 SFT+DPO+GRPO 多阶段微调。关键：仅做 calibrated abstention，不尝试 correction。与本 proposal 在任务域（biography generation）高度重叠但范式不同。\n- [Selective Abstraction (SA), arXiv:2602.11908] (Feb 2026): Atom-wise 分解 + confidence-based abstraction，在 FActScore/LongFact 上 AURC 提升最高 27.73%。只做 abstraction，不做 correction。是本 proposal 的直接 baseline。\n- [CAG, arXiv:2605.01749] (May 2026): Exploration-Commitment Decoupling，VeriScore 67.79%→79.80%。同样只做 suppression 不做 correction。需要微调（CASS+CAPD）。\n- [DeepMind PANL, arXiv:2604.22271] (Apr 2026): White-box PANL probes 预测 correction success AUROC=0.614，behavioral confidence 仅 0.524。仅在 TriviaQA/MNLI problem-level 上测试 Gemma 3 27B 和 Qwen 2.5 7B。是 correctability prediction 的直接竞争/上游工作。\n- [CyberCorrect, arXiv:2605.17305] (May 2026): Tri-modal error detector (self-consistency 0.4 + verbalized confidence 0.35 + logic-chain verification 0.25)，type-directed correction，79.8% accuracy。仅在 reasoning tasks 上测试，logic-chain feature 不适用于 factual claims。\n- [Functional Dissociation, arXiv:2604.19974] (Apr 2026): SAE 分析表明 uncertainty 和 correctness 由 functionally distinct feature populations 编码。suppressing uncertainty features 导致 accuracy 下降最高 10.21%，suppressing incorrectness features 几乎无变化。为\"confidence ≠ correctability\"提供了 mechanistic evidence。\n- [Knowing but Not Correcting, arXiv:2605.05957] (May 2026): Correction suppression 现象——模型单独面对 false claim 时能纠正，但嵌入 task context 后 suppress correction（19-90% suppression rate）。Hidden-state similarity >0.99 证明模型 internally registers error。\n- [ConFix, arXiv:2411.13343] (2024): Fact-level confidence calibration + self-correction，高置信度 facts bootstrap 低置信度 facts 的 correction。这是一个重要的 trivial alternative 威胁——已经在做 fact-level self-correction，虽然用的是 confidence 而非 correctability。\n- [FactCorrector + VELI5, arXiv:2601.11232] (Jan 2026): Graph-inspired correction pipeline + 17,522 instances benchmark，67.4% atom correction rate。但依赖外部知识检索。\n- [FactSelfCheck, arXiv:2503.17229] (2025): Fact-level hallucination detection，35.5% vs 10.6% factual improvement 对比 sentence-level。\n- [CSS, arXiv:2604.17487] (Apr 2026): Claim-level specificity control，back off overcommitted claims。\n- [CLC, arXiv:2502.19110] (Feb 2026): Conformal linguistic calibration，conformal guarantees on claim factuality。\n\n- **调研总结**: Self-correction blind spot 研究目前被限制在 math/reasoning 的 problem-level 粒度。与此同时，fact-level claim handling 领域在 2026 年 2-5 月爆发式增长（SA, CSS, CLC, CURE, CAG 等 6+ 篇论文），但全部采用 confidence/calibration 作为 routing signal，响应方式为 abstention/suppression/hedging，无一尝试基于 correctability 的 correction routing。Proposal 精确定位在这两条线的交叉点——fact-level granularity × correctability-based correction——这个交叉点确实 unoccupied。但该定位的价值高度依赖于\"correctability ≠ confidence\"这个区分在 fact-level 实践中的真实效应大小。\n\n\n【Trivial Alternative 检验】:\n\n存在两个需要认真对待的 trivial alternatives：\n\n1. **ConFix + naive self-correction**: ConFix 已经在做 fact-level self-correction，使用 confidence-based bootstrapping。如果在本 proposal 的 benchmark 上直接跑 ConFix，能达到 SFC 效果的 80%+，那 correctability classifier 的增量价值就很有限。Proposal 确实将 ConFix-style bootstrapping 纳入了 SFC 的 correction 子模块，但没有直接 head-to-head 对比 ConFix 的 confidence routing vs. correctability routing 的边际差异。\n\n2. **'Wait' trick 直接应用到 factual claims**: Proposal 包含了 'Wait' ablation（Phase 2），这是正确的。但如果 'Wait' 在 factual claims 上也有 30-50% 的 blind spot reduction（即使不如 math 的 89.3%），那 'Wait' + naive self-correction 可能就是 \"good enough\" 的 trivial baseline。Proposal 的核心价值取决于 'Wait' ablation 的负面结果。\n\n**增量价值在哪**: 如果上述两个 trivial alternatives 都不够好（'Wait' 对 facts 无效 + confidence 和 correctability 的 gap 在 fact-level 足够大），那 correctability-guided routing 确实是一个有意义的新方向。但这个增量价值是 **conditional on empirical results** 的——这不是一个无论实验结果如何都有清晰增量的 idea。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的关键假设：\n\n1. **\"Factual errors stem from knowledge gaps, not activation failures\"——这个二分法过于简化**。并非所有 factual errors 都是 knowledge gaps。很多 hallucinations（尤其是 entity confusion、date off-by-one）可能也是 activation/retrieval failures，'Wait' 可能对这些同样有效。Proposal 将 math errors = activation failures vs. factual errors = knowledge gaps 作为一个核心前提，但实际的 error taxonomy 可能远比这复杂。如果相当比例的 factual errors 也是 activation failures，整个故事的 motivation 就被削弱了。\n\n2. **\"Behavioral features 能足够好地捕捉 correctability\"——来自 DeepMind 结果的证据其实是 negative 的**。DeepMind 发现 behavioral confidence 只有 AUROC 0.524（接近随机），而 white-box features 才有 0.614。Proposal 认为加入 claim type + specificity + detection-correction gap 能显著提升，但没有先验证据支持这一点。如果最终只达到 0.55-0.58，SFC 的实际效用会非常有限。\n\n3. **\"Error Depth Hypothesis 从 math 迁移到 factual claims\"——类比推理，未经验证**。Math 中的 error depth（calculation vs. logic vs. setup）和 factual claim types（entity, temporal, numerical, relational）是完全不同的 taxonomy。Error Depth 发现的是 model capability 相关的 depth gradient，factual claim types 之间是否存在类似的 difficulty gradient 是一个 open question。\n\n4. **\"Correction suppression 会 compound blind spot\"——外推**。arXiv:2605.05957 的实验设置（isolated false claim vs. task-embedded false claim）和本 proposal 的设置（model 纠正自己生成的 output 中的 errors）是不同的。能否直接外推需要验证。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Proposal 精确定位在 fact-level × blind spot × correctability 这个 unoccupied intersection，这一点是成立的。调研证实：Self-Correction Bench 仅覆盖 math/problem-level；SA/CURE/CAG 等 6+ 篇只做 confidence-based abstention，不做 correctability-based correction；DeepMind PANL 仅在 problem-level + white-box。然而，novelty 主要来自 **extension**（将已知概念推广到新粒度和新域）而非 **discovery**（发现新机制或反直觉现象）。核心预测——blind spot 在 factual claims 上存在且比 math 更严重，'Wait' 对 facts 效果减弱，不同 claim types 有不同 blind spot rates——大多数研究者会猜到这些方向。Correctability classifier 的构建借鉴了 CyberCorrect 的 feature 设计思路（self-consistency + confidence + type），主要替换了 logic-chain feature 为 claim-specific features，属于 adaptation 而非 innovation。最有 novelty 的贡献是 'Wait' ablation 在 factual domain 的系统性测试，以及 correctability-confidence dissociation 的 claim-level 量化——但这些更像是 \"good to know\" 而非 \"surprising\"。\n\n2. **Significance: 中偏强** — \n   研究问题本身是重要的。Self-correction 是 LLM 部署的核心能力，理解其在 knowledge-intensive generation 中的 fine-grained limitations 对实际应用有直接影响。6+ 篇论文在 2026 年 2-5 月密集出现在 claim-level handling 空间，证明了这个方向的热度和社区关注度。如果 benchmark 和 blind spot characterization 做得好，将为后续研究提供基础设施价值（类似 FActScore 对 factual evaluation 的贡献）。但 significance 被两点限制：(a) SFC pipeline 的实际改进幅度可能有限（correctability classifier 的 ceiling 不高），使得下游应用价值不确定；(b) 如果核心发现是\"blind spot 在 facts 上更严重，'Wait' 不好使\"，这是 confirmatory 而非 transformative。\n\n3. **Related Work: 强** — \n   这是 proposal 最突出的优势。覆盖了 5 条独立研究线（blind spot literature, fact-level hallucination, correctability prediction, selective claim handling, mechanistic evidence），引用了 30+ 篇论文，包括 2026 年 5 月的最新工作（CAG, CyberCorrect, Knowing but Not Correcting）。差异化定位清晰：与 SA/CURE/CAG 的区别（correctability vs. confidence, correction vs. abstention）、与 DeepMind PANL 的区别（black-box vs. white-box, claim-level vs. problem-level）、与 CyberCorrect 的区别（factual claims vs. reasoning, claim-level vs. step-level）都论述得非常到位。调研证实所有引用论文真实存在且描述准确。唯一微小问题：过于详尽的 related work 使得 proposal 读起来像一篇 survey，但这在入口评估中不是减分项。\n\n\n【概率估计】: [25% - 35%] 中位 29%\n\n【估计理由】: \nNovelty 处于\"中\"水平——gap 真实存在但 core findings 的预期方向是 intuitive 的（审稿人大概率会说 \"I would have guessed this\"），这是限制上界的主要因素。Significance 中偏强，因为研究问题重要、领域热度高、benchmark 有基础设施价值，这拉高了下界。Related Work 强，positioning 清晰无遗漏，但 related work 的完善度属于执行质量，不改变 idea 上限。\n\n从 rubric 锚点看：idea 有实质内核（真实的 novelty delta），方向正确，但核心发现如果 positive，审稿人更可能说 \"good systematic study, confirms what I expected\" 而非 \"surprising\"——这把它锚定在 25-35% 区间。中位取 29% 而非 30%+ 是因为 trivial alternative 威胁（ConFix 和 'Wait' ablation）增加了 idea 被质疑为 incremental 的风险。\n\n**限制上界的维度**: Novelty。Extension-type novelty（将已知概念推广到新域/粒度）在 top venues 通常不如 discovery-type novelty（发现新机制/反直觉现象）有竞争力，除非 extension 的过程中产生了 unexpected findings。\n\n【主要风险】: \n1. **\"Expected findings\" 风险**: 三个核心预测（blind spot 在 facts 上存在/更严重、'Wait' 对 facts 无效、claim types 间 heterogeneous）都是大多数研究者会预期的方向。如果实验结果完全 confirm expectations，审稿人可能评价为 \"well-executed but unsurprising\"，这是 EMNLP 最常见的 borderline reject 理由之一。除非实验过程中发现某个 truly unexpected pattern（例如某种 factual claim type 的 blind spot 反而低于 math，或 'Wait' 在某些 claim types 上出奇有效），整篇论文缺乏 \"aha moment\"。\n2. **Correctability classifier ceiling 过低的风险**: DeepMind 已经证明 behavioral signals 对 correctability 的预测力很弱（AUROC 0.524）。Proposal 的 classifier 加入了 claim type 和 specificity features，但如果最终 AUROC 只在 0.55-0.58 范围，SFC 相对于 confidence-threshold correction 的优势将非常边际，使得 Phase 3+4（classifier + SFC pipeline）的贡献变得 marginal，论文的贡献缩水为一个 benchmark paper。\n```\n\nSources:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)\n- [CURE (arXiv:2604.12046)](https://arxiv.org/abs/2604.12046)\n- [Selective Abstraction (arXiv:2602.11908)](https://arxiv.org/abs/2602.11908)\n- [CAG (arXiv:2605.01749)](https://arxiv.org/abs/2605.01749)\n- [DeepMind PANL (arXiv:2604.22271)](https://arxiv.org/abs/2604.22271)\n- [CyberCorrect (arXiv:2605.17305)](https://arxiv.org/abs/2605.17305)\n- [Functional Dissociation (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)\n- [Knowing but Not Correcting (arXiv:2605.05957)](https://arxiv.org/html/2605.05957v1)\n- [ConFix (arXiv:2411.13343)](https://arxiv.org/abs/2411.13343)\n- [FactCorrector + VELI5 (arXiv:2601.11232)](https://arxiv.org/abs/2601.11232)\n- [FactSelfCheck (arXiv:2503.17229)](https://arxiv.org/abs/2503.17229)\n- [CSS (arXiv:2604.17487)](https://arxiv.org/abs/2604.17487)\n- [CLC (arXiv:2502.19110)](https://arxiv.org/abs/2502.19110)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to evaluate this proposal. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- Self-Correction Bench (arXiv:2507.02778, submitted ICLR 2026): 确认存在。在GSM8K/PRM800K上测量14个非推理模型，64.5%平均blind spot率，'Wait'减少89.3%。但仅测试数学任务、问题级粒度。Proposal对该论文的描述准确。\n- CURE (arXiv:2604.12046, Apr 2026): 确认存在。通过&lt;think>→&lt;decompose>→&lt;answer>协议在biography generation上实现39.9%声明级准确率提升，通过SFT+DPO+GRPO多阶段微调实现校准弃权。确认使用置信度/校准作为路由信号，从不尝试纠正。描述准确。\n- Selective Abstraction (arXiv:2602.11908, Feb 2026): 确认存在。原子级声明分解+不确定声明用更模糊版本替换。描述准确。\n- DeepMind PANL论文 (arXiv:2604.22271, Apr 2026): 确认存在。Kumaran等人展示PANL残差流激活的线性探针预测纠正成功(AUROC=0.614)，行为置信度仅0.524。需要白盒访问。描述准确。\n- Functional Dissociation (arXiv:2604.19974, Apr 2026): 确认存在。通过稀疏自编码器在Llama-3.1-8B和Gemma-2-9B上证明不确定性和正确性由功能上不同的特征群编码。描述准确。\n- CyberCorrect (arXiv:2605.17305, May 2026): 确认存在。三模态错误检测器(自一致性+口头置信度+逻辑链验证)，基于控制论框架。操作在推理任务上。描述准确。\n- CAG (arXiv:2605.01749, May 2026): 确认存在。Exploration-Commitment Decoupling，VeriScore 67.79%→79.80%。需微调，抑制而非纠正不可靠声明。描述准确。\n- FactSelfCheck (arXiv:2503.17229, Mar 2025): 确认存在。事实级黑盒幻觉检测，知识图谱三元组表示。描述准确。\n- \"Knowing but Not Correcting\" (arXiv:2605.05957): **未能通过搜索验证**。多次搜索均未找到该论文。可能是非常近期发布尚未被索引，也可能arXiv ID有误。该论文被用作\"纠正抑制\"现象的关键论据之一。\n- 未找到直接竞争工作：搜索\"fact-level correctability prediction\"和\"correctability-based claim routing\"未找到任何已发表的、在原子声明级别做correctability预测并用于路由的工作。这支持了proposal所声称的gap确实存在。\n\n调研总结: 该领域在2026年初经历了快速发展——选择性声明级处理(SA, CSS, CLC, CURE, CAG)已成为拥挤赛道，但所有工作均使用置信度/校准作为路由信号，通过弃权/抽象化应对不确定性。Self-correction blind spot文献仅覆盖数学任务。Proposal定位在\"原子声明级correctability预测+纠正路由\"这个交叉空间，该空间确实未被占据。\n\n【Trivial Alternative 检验】:\n最直接的trivial alternative是：**直接使用SA/CURE的置信度信号，但将低置信度声明路由到纠正（而非弃权）**——即\"confidence-threshold selective correction\"。Proposal自己在Phase 4中将此作为baseline (g)纳入了，这显示了作者的自我意识。但问题在于：如果这个trivial baseline表现与SFC相当，那么整个correctability classifier的价值就会被大幅削弱。Proposal的增量价值完全取决于correctability ≠ confidence这个gap在实践中有多大。DeepMind论文显示PANL内部表征(0.614) vs 行为置信度(0.524)之间有gap，但这是白盒vs黑盒的差距，而proposal的分类器同样使用黑盒行为信号——为什么黑盒行为特征的组合(自一致性+口头置信度+声明类型+特异性)能显著超越单纯的行为置信度？这是proposal中最脆弱的环节。\n\n第二个trivial alternative：**对所有声明统一执行naive self-correction**。如果模型对大部分能纠正的声明确实能纠正，对不能纠正的声明纠正后质量不显著下降（\"destructive correction\"率较低），那么选择性路由的价值就有限。Proposal也包含了这个baseline (b)，但并未论证destructive correction在实践中有多严重。\n\n总体而言：trivial alternative威胁是真实存在的，proposal的增量价值高度依赖correctability-confidence dissociation在原子事实声明层面的实际大小。\n\n【前提假设检验】:\n1. **核心假设：\"correctability ≠ confidence\"在原子事实声明级别成立且gap足够大以支撑有意义的路由优势**。支撑证据来自两个不同层面的工作——DeepMind的白盒内部表征研究(在TriviaQA/MNLI的问题级别)和Functional Dissociation的SAE研究(在token级别)——但这些发现能否迁移到长文本中的原子事实声明粒度是未经验证的。这是整个proposal成败的关键假设。\n\n2. **假设：\"Wait\"技巧对事实声明效果显著弱于对数学问题\"**。这个假设的逻辑链是：数学错误=激活失败→'Wait'有效；事实错误=知识缺口→'Wait'无效。这个论证是合理的，但也是直觉性的。如果'Wait'对事实声明同样有效（>50%），proposal坦言这是\"important simplifying finding\"，但这会让correctability classifier和SFC的贡献大幅缩水。\n\n3. **假设：\"声明类型异质性\"存在且有意义**。Error Depth Hypothesis在数学中发现错误类型预测可纠正性，但从数学错误类型(计算/设置/逻辑)到事实声明类型(实体/时间/数值/关系)的类比是否成立未经验证。\n\n4. **假设：黑盒行为特征组合能够捕捉足够的correctability信号**。DeepMind论文恰恰显示行为置信度(0.524)远不如内部表征(0.614)，这反而暗示黑盒方法可能存在天花板效应。Proposal预注册的>0.58阈值虽然诚实但也承认了这一天花板。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Proposal确实识别了一个未被占据的交叉空间：在原子声明级别测量fact-level blind spot + correctability预测 + 纠正路由。搜索确认在SA/CSS/CLC/CURE/CAG/VeriFY等6+篇论文中，没有工作尝试correctability-based correction routing。这个gap是真实的。\n   \n   但novelty的性质需要审视。这本质上是\"将已有概念(blind spot测量)应用于新粒度(原子声明)和新领域(知识密集型任务)\"——这是**组合式novelty**而非**概念性novelty**。每个组件——FActScore式分解、self-correction测量、行为特征分类器、选择性路由——都有明确的先行工作。'Wait'转移性测试是一个clean的ablation但更像是sanity check而非创新贡献。Correctability classifier的特征集(自一致性、口头置信度、声明类型、特异性)中，前两个直接来自SelfCheckGPT和CyberCorrect，后两个是SA/CSS启发的。真正新的只有\"detection-correction gap\"这一个特征和将这些特征用于correctability而非confidence预测的framing。\n   \n   对于EMNLP而言，组合式novelty如果能产生新的发现是可以接受的，但审稿人可能会认为这是\"obvious next step\"——在Self-Correction Bench + SA/CURE之后，将blind spot分析扩展到原子事实声明是自然的延伸。\n\n2. **Significance: 中** — \n   研究问题本身是重要的：理解模型何时能/不能自我纠正事实性错误，对于构建可靠的LLM系统有直接实际价值。6+篇论文都走置信度弃权路线而无人走correctability纠正路线，填补这个空白有意义。\n   \n   但significance受限于两个因素：(a) 如果核心发现是positive（事实声明blind spot高于数学、异质性存在、'Wait'对事实无效），审稿人很可能说\"I would have guessed this\"——知识缺口导致的错误比激活失败更难纠正，这是大多数研究者的先验直觉。(b) correctability classifier的实际影响取决于AUROC能达到多高。在预注册的\"positive\"阈值仅>0.58的情况下，SFC相对于trivial confidence-threshold baseline的实际优势可能很小。\n   \n   最有意义的贡献可能不是下游应用(SFC)，而是benchmark本身和characterization findings——如果blind spot率、claim-type异质性模式、'Wait'转移性等提供了社区目前缺乏的定量理解。但这更接近\"measurement paper\"的贡献形态。\n\n3. **Related Work: 强** — \n   这是proposal最突出的维度。对领域的覆盖异常全面：Self-Correction Bench、Error Depth、Confidence vs Critique、FactSelfCheck、ConFix、FactCorrector、DeepMind PANL、CyberCorrect、Functional Dissociation、SA、CSS、CLC、CURE、CAG、VeriFY、I-CALM、AtomEval等全部被准确引用和定位。差异化论述清晰且有说服力——\"所有现有工作使用置信度/校准，无人做correctability\"这个定位经过调研确认是准确的。\n   \n   唯一瑕疵是arXiv:2605.05957(\"Knowing but Not Correcting\")未能通过搜索验证，该论文被用作\"correction suppression\"现象的关键论据。如果这篇论文不存在或被不准确描述，会削弱一个支柱性论点（但不是致命的，因为proposal的核心论证不完全依赖于它）。\n\n【概率估计】: [23% - 32%] 中位 27%\n\n【估计理由】: \nNovelty评为\"中\"是限制上界的主要因素。Proposal的核心贡献是\"将blind spot分析从数学/问题级扩展到事实/原子声明级\"——这是一个legitimate但组合性质的novelty，审稿人可能视为\"obvious next step after Self-Correction Bench + SA/CURE\"。预期核心发现（事实声明比数学更难自我纠正、'Wait'效果减弱、异质性存在）大概率会被审稿人判断为\"I would have guessed this\"，将概率压在35%以下。\n\nSignificance评为\"中\"进一步约束了估计：correctability classifier的预注册阈值(>0.58)诚实但也暴露了天花板问题，SFC的实际增量价值高度依赖correctability-confidence gap在实践中的大小——这是一个未经验证的假设。\n\nRelated Work评为\"强\"提供了下限支撑：即使idea不够surprising，出色的文献覆盖和清晰的定位会让审稿人认可论文的学术严谨性，不太会被拒为\"insufficiently novel\"到15%以下。\n\n综合而言，这是一篇方向正确、gap真实、但核心发现可能confirmatory而非surprising的measurement+分析论文。在EMNLP这样高标准的venue，27%的中位概率反映了\"solid but not exciting\"的定位。\n\n【主要风险】: \n1. **\"Obvious extension\"风险**: 审稿人可能认为\"在原子声明级别重复Self-Correction Bench的分析\"是自然延伸而非独立贡献，特别是当预期结果大多符合直觉时（事实错误比数学错误更难纠正）。这会直接打击novelty评分。\n2. **Correctability classifier天花板风险**: 如果黑盒行为特征无法显著超越简单置信度阈值baseline（DeepMind论文已暗示行为信号的天花板），则proposal最核心的技术贡献(correctability ≠ confidence的实践价值)将被架空，SFC的优势也将不明显。\n```\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Fact-Level Self-Correction Blind Spot in Knowledge-Intensive Generation: Benchmark, Analysis, and Correctability-Guided Selective Correction\n\n## Description\nWe propose FactBlind, the first benchmark and analysis framework for measuring the self-correction blind spot at fact-level granularity in knowledge-intensive generation. While the blind spot phenomenon has been characterized for mathematical reasoning at problem level (64.5% average failure rate on GSM8K/PRM800K), and the 'Wait' trick reduces this by 89.3% through an activation mechanism, no work has examined whether these patterns hold for atomic factual claims in long-form text — where errors often stem from genuine knowledge gaps rather than activation failures that prompt tricks can resolve. The recent discovery of correction suppression (19–90% suppression rates when false claims are embedded in task contexts) further suggests the problem in knowledge-intensive generation operates through mechanisms distinct from math. Meanwhile, the selective claim-level handling space has become remarkably crowded — SA, CSS, CLC, CURE (39.9% claim-level accuracy on biography generation), and CAG (VeriScore 67.79%→79.80%) all use confidence/calibration for abstention — while the correctability-based correction paradigm remains entirely unexplored, despite mechanistic evidence that uncertainty and correctness are encoded by functionally distinct feature populations (Functional Dissociation, arXiv:2604.19974). We decompose LLM-generated biographies, QA responses, and report summaries into atomic claims and measure per-claim blind spot rates across 8 models, using both controlled error injection (entity, temporal, numerical, relational) and naturally occurring hallucinations from FActScore-annotated data, with a dedicated 'Wait' ablation testing whether activation-based interventions transfer from math to factual claims. Our central hypothesis — that the blind spot is heterogeneous across claim types and resistant to simple activation prompts — is tested rather than assumed; if 'Wait' proves effective for factual claims, we report this as an important simplifying finding. We then train a black-box behavioral correctability classifier using self-consistency, verbal confidence, claim type, and specificity features, with pre-registered AUROC thresholds (>0.58 positive, >0.63 strong) anchored against DeepMind's white-box baseline (0.614) and behavioral confidence baseline (0.524). Even modest classifier performance reveals the correctability-confidence dissociation, which is itself an important finding given 6+ papers implicitly assume confidence suffices for claim-level routing. Finally, we build Selective Fact Correction (SFC) as a downstream application: claims predicted as correctable undergo ConFix-style bootstrapping while blind-spot claims are flagged for abstention, compared against no-correction, naive self-correction, SA, CURE reference results, confidence-threshold correction, and 'Wait'-augmented self-correction baselines. Unlike SA/CSS/CLC/CURE/CAG which exclusively abstract or suppress, SFC can recover factual accuracy for correctable claims while avoiding destructive correction for uncorrectable ones.\n\n## Core Problem\nSelf-correction research has characterized the blind spot phenomenon exclusively on mathematical reasoning tasks at problem-level granularity (Self-Correction Bench, 64.5% average blind spot rate across 14 models on GSM8K/PRM800K), and the 'Wait' prompt trick reduces this blind spot by 89.3% — but crucially, this works because math errors are activation failures, not knowledge deficiencies. Yet knowledge-intensive generation (biographies, open-domain QA, report writing) produces outputs containing dozens of heterogeneous atomic claims — entities, temporal facts, numerical values, relations — where errors often stem from genuine knowledge gaps that no activation trick can resolve. Meanwhile, a rapidly growing body of work on selective claim-level handling (Selective Abstraction, CSS, Conformal Linguistic Calibration, CURE, CAG — now 6+ papers) addresses uncertain claims through calibration, abstraction, or hedging, but none attempt to predict whether the model can actually *correct* a specific factual error — a fundamentally different question from whether the claim is uncertain or poorly calibrated, as demonstrated by recent evidence that uncertainty and correctness are encoded by distinct internal feature populations (Functional Dissociation, arXiv:2604.19974). Does the self-correction blind spot manifest differently at fact-level granularity in knowledge-intensive tasks, is it heterogeneous across claim types, can simple activation prompts ('Wait') compensate, and can behavioral correctability estimation enable more effective correction routing than either uniform correction or confidence-based abstraction?\n\n## Opportunity\nFive converging lines of work create a clear gap. First, the blind spot literature (Self-Correction Bench arXiv:2507.02778, submitted to ICLR 2026; Error Depth Hypothesis arXiv:2601.00828; Confidence v.s. Critique arXiv:2412.19513) has established that LLMs struggle to correct their own errors, with stronger models making fewer but 'deeper' errors that resist correction — but all measurement is at problem level on math tasks, and the 'Wait' trick's 89.3% blind spot reduction specifically exploits an activation mechanism that may not generalize to factual knowledge errors. Critically, 'Knowing but Not Correcting' (arXiv:2605.05957) discovers correction suppression — models reliably correct false claims in isolation but suppress correction when embedded in task contexts (19–90% suppression rates across 8 models) — demonstrating a complementary blind-spot phenomenon for factual claims that suggests the problem may be even worse in knowledge-intensive generation contexts where task framing is inherent. Second, the fact-level hallucination literature (FactSelfCheck arXiv:2503.17229, 35.5% vs 10.6% factual improvement for fact-level vs sentence-level; ConFix arXiv:2411.13343; FactCorrector arXiv:2601.11232 with the VELI5 benchmark) has demonstrated that fine-grained claim-level analysis dramatically outperforms coarser approaches — but neither studies whether models can correct their OWN factual errors claim-by-claim. Third, DeepMind's recent work (arXiv:2604.22271) shows that internal PANL representations can predict which errors a model can correct (AUROC=0.614 on TriviaQA), and CyberCorrect (arXiv:2605.17305) uses a tri-modal detector combining self-consistency, verbalized confidence, and logic-chain verification for type-directed correction — but both operate at problem level on reasoning/QA tasks, not at atomic-claim level within long-form outputs; CyberCorrect requires reasoning chains and DeepMind requires white-box model access. Moreover, a Functional Dissociation study (arXiv:2604.19974) demonstrates via sparse autoencoders that uncertainty and correctness are encoded by distinct feature populations — suppressing uncertainty features degrades accuracy by up to 10.21% while suppressing incorrectness features produces near-zero change — providing mechanistic evidence that confidence-based routing is fundamentally insufficient for correctability prediction. Fourth, the selective claim-level handling space has become remarkably crowded: Selective Abstraction (arXiv:2602.11908) decomposes responses into atomic claims and replaces uncertain ones with less-specific abstractions (up to 27.73% AURC improvement on FActScore), CSS (arXiv:2604.17487) backs off overcommitted claims, Conformal Linguistic Calibration (arXiv:2502.19110) provides conformal guarantees on claim factuality, CURE (arXiv:2604.12046) teaches models to reason about uncertainty at claim level via a structured &lt;think>→&lt;decompose>→&lt;answer> protocol achieving 39.9% claim-level accuracy improvement on biography generation through calibration and abstention, and CAG (arXiv:2605.01749) decouples exploration from commitment to improve VeriScore from 67.79% to 79.80% — but ALL of these (now 6+ papers) use confidence or calibration as their routing signal and respond to uncertainty through abstraction, suppression, or hedging, NEVER attempting correction. The intersection — measuring the blind spot at fact-level granularity, testing whether activation-based interventions generalize from math to factual claims, predicting correctability (not just confidence) using black-box behavioral signals, and routing claims to correction vs. abstention based on predicted correction success — is unoccupied.\n\n## Landscape\nThe self-correction blind spot was first quantified by Self-Correction Bench (arXiv:2507.02778, submitted to ICLR 2026), which found 64.5% average failure-to-self-correct across 14 non-reasoning models — but tested only on math tasks (GSM8K, PRM800K, SCLI5) and operates at problem level. Notably, the bench found that appending a minimal 'Wait' prompt reduces the blind spot by 89.3%, and the authors attribute this to correction markers acting as conditioning tokens that shift probability distributions toward self-evaluation sequences — an activation mechanism supported by training-data analysis showing correction markers are concentrated in reasoning datasets (median 30–170 per response) but nearly absent from non-reasoning datasets (95th percentile = 1 marker). This suggests 'Wait' works because math errors are activation failures, not knowledge deficiencies; for factual claims where the model genuinely lacks correct information, activation alone cannot compensate (we test this hypothesis with a 'Wait' ablation in Phase 2). We treat Self-Correction Bench as a useful reference point rather than a definitive field-wide statistic, noting the TACL survey 'When Can LLMs Actually Correct Their Own Mistakes?' (arXiv:2406.01297) provides broader context for when self-correction succeeds or fails. The Error Depth Hypothesis (arXiv:2601.00828) shows that error TYPE predicts correctability in math — stronger models make deeper (setup/logic) errors that resist correction while weaker models make shallower (calculation) errors that are more fixable — suggesting claim-type stratification is a promising direction, though this was only tested on GSM8K with 3 models. Confidence v.s. Critique (arXiv:2412.19513, ACL 2025) decomposes self-correction into confidence and critique capabilities with probabilistic metrics, but operates at problem level.\n\nA newly discovered complementary phenomenon is correction suppression (arXiv:2605.05957): models reliably reject false claims in isolation but comply with those same claims when embedded in task-oriented requests, with suppression rates of 19–90% across 8 models. Mechanistically, the model internally registers the error (hidden-state similarity >0.99) but task context diverts attention, with 'output intent crystallizing toward compliance at middle layers.' This suggests that in knowledge-intensive generation — where task framing is inherent — the blind spot may be compounded by contextual suppression, and that 'Wait'-style activation interventions may be insufficient because the suppression mechanism operates at a deeper level than simple activation failure.\n\nOn the fact-level side: FactSelfCheck (arXiv:2503.17229) achieves 35.5% factual improvement via fact-level hallucination detection using knowledge-graph-style triple representation. ConFix (arXiv:2411.13343) demonstrates that high-confidence facts can bootstrap correction of low-confidence facts within the same response without external knowledge. FactCorrector (arXiv:2601.11232) introduces the VELI5 benchmark (17,522 instances with injected factual errors and ground-truth corrections) and a graph-inspired correction pipeline — but relies on external knowledge retrieval via search APIs, achieving 67.4% correction of incorrect atoms with structured feedback. Atomic Calibration (Zhang et al., ACL 2025 KnowFM, arXiv:2410.13246) shows that LLMs exhibit poorer calibration at the atomic level during long-form generation than at response level, providing direct motivation for claim-level analysis.\n\nOn correctability prediction: DeepMind's work (arXiv:2604.22271) trains linear probes on post-answer newline (PANL) residual-stream activations that predict correction success (AUROC=0.614), while verbal confidence (0.524) and log-probability (0.531) baselines fail — but requires white-box access and operates at problem level on TriviaQA/MNLI with only Gemma 3 27B and Qwen 2.5 7B. CyberCorrect (arXiv:2605.17305) uses a tri-modal error detector combining self-consistency (weight 0.4), verbalized confidence (0.35), and logic-chain verification (0.25) for type-directed correction on reasoning tasks, achieving 79.8% accuracy with 41% reduction in over-correction — but its logic-chain verification feature requires reasoning chains not present in factual claims, and it operates at reasoning-step level on CyberCorrect-Bench (440 tasks across math/logic/commonsense). Independently, 'Are LLM Uncertainty and Correctness Encoded by the Same Features?' (arXiv:2604.19974) provides mechanistic evidence via sparse autoencoders on Llama-3.1-8B and Gemma-2-9B that uncertainty and correctness are encoded by functionally distinct feature populations: pure uncertainty features are essential for accuracy (suppression causes up to -10.21% accuracy), while pure incorrectness features are statistically significant but functionally inert (suppression yields mean -0.03% change). This directly supports our thesis that confidence-based routing (which tracks uncertainty features) cannot substitute for correctability prediction (which must track correctness-related features). Our behavioral correctability classifier adopts similar self-consistency and confidence signals to CyberCorrect but replaces logic-chain verification with claim-type and specificity features appropriate for factual claims, and critically predicts SELF-CORRECTION success at atomic granularity rather than routing pre-identified errors.\n\nThe selective claim-level handling space has become remarkably crowded but addresses a DIFFERENT question from ours. Selective Abstraction (SA; Goren et al., arXiv:2602.11908) decomposes long-form responses into atomic claims, estimates per-claim confidence via verbalized confidence scoring, generates progressively less-specific abstraction sequences, and selects the most specific abstraction satisfying a confidence threshold — achieving up to 27.73% AURC improvement on FActScore across 6 models. Crucially, SA never attempts correction: it exclusively replaces uncertain claims with vaguer versions. CSS (arXiv:2604.17487) similarly backs off overcommitted claims rather than correcting them. Conformal Linguistic Calibration (CLC; Jiang et al., arXiv:2502.19110) provides conformal guarantees on factual accuracy through nested answer-set prediction and progressive claim vaguening — tested on SimpleQA, Natural Questions, and FActScore — but requires fine-tuning (SFT/DPO/ORPO) and also does not attempt correction. CURE (arXiv:2604.12046) operates on the SAME task domain as our work (biography generation, FactBench) and at claim-level granularity: it introduces a Claim-Aware Reasoning Protocol that structures outputs into atomic claims paired with explicit confidence estimates via a &lt;think>→&lt;decompose>→&lt;answer> pipeline, achieving 39.9% claim-level accuracy improvement on Biography and 16.0% AUROC increase on FactBench — but requires multi-stage fine-tuning (SFT + DPO calibration + GRPO factuality optimization on 3–4K prompts) and responds exclusively through calibrated abstention, never attempting correction. CAG (arXiv:2605.01749) proposes an Exploration-Commitment Decoupling paradigm where calibrated reliability estimates filter unreliable reasoning steps before commitment, improving VeriScore from 67.79% to 79.80% across five benchmarks (AlpacaFact, Biography, FactBench, Factory, FAVA) — but also requires fine-tuning (CASS + CAPD stages) and suppresses rather than corrects unreliable claims. VeriFY (arXiv:2602.02018) teaches factual self-verification with abstention through structured verification traces at training time, reducing hallucination by 9.7–53.3% — but requires fine-tuning and operates at response level. I-CALM (arXiv:2604.03904) shows prompt-based abstention can shift error-prone cases to abstention without retraining. Know When You're Wrong (arXiv:2603.06604) aligns confidence with correctness for error detection (AUROC 0.806→0.879 with SFT).\n\nThe key distinction: ALL of the above selective-handling methods (now 6+ papers: SA, CSS, CLC, CURE, CAG, VeriFY) use CONFIDENCE or CALIBRATION as their routing signal and respond to uncertainty through ABSTRACTION, SUPPRESSION, or HEDGING. None ask the question central to our work: 'Can this model correct this specific factual error in its own output?' A model may be confidently wrong about a claim (SA/CURE wouldn't touch it) but still able to correct it when prompted; conversely, a model may flag uncertainty about a claim but be unable to produce a correct replacement. Correctability and confidence are related but mechanistically distinct signals — as demonstrated both by DeepMind's finding that behavioral confidence fails to predict correction success (AUROC=0.524 vs. 0.614 for internal representations) and by the Functional Dissociation study showing distinct neural feature populations — and the gap between them, measured at fact level, is our primary object of study.\n\nConcurrent work: AtomEval (arXiv:2604.07967, April 2026) introduces SROM-atom decomposition for adversarial fact verification. CURE (arXiv:2604.12046) and CAG (arXiv:2605.01749) are the closest concurrent works, sharing our task domain and claim-level granularity — but both pursue the confidence-based calibration/abstention paradigm rather than correctability-based correction, making them complementary rather than competing approaches.\n\n## Approach\nWe build FactBlind, a benchmark and analysis framework for measuring the self-correction blind spot at fact-level granularity in knowledge-intensive generation. The primary contributions are (1) the benchmark and blind spot analysis and (2) the behavioral correctability classifier; the selective correction pipeline is a downstream application demonstrating the practical value of correctability estimation, positioned as a secondary contribution given the now-crowded selective-handling design space.\n\n**Phase 1: Benchmark Construction (3 weeks).** (a) Injected-error track: Generate long-form responses (biographies, open-domain QA, report summaries) from 8 models, decompose into atomic claims using FActScore-style decomposition, then inject controlled factual errors stratified by type — entity swaps (replacing named entities), temporal shifts (date/year perturbations), numerical perturbations (magnitude changes), and relation inversions (swapping subject-object or predicate). We draw methodology inspiration from VELI5 (arXiv:2601.11232) but target intrinsic self-correction measurement rather than external-knowledge correction. We additionally stratify error injection by specificity level (informed by SA's finding that specificity affects reliability) to test whether more specific claims are harder to self-correct. (b) Natural-error track: Evaluate on unmodified LLM-generated biographies using existing FActScore annotations and SAFE/LongFact datasets, where naturally occurring hallucinations serve as ecological ground truth. This dual-track design directly addresses the threat that injected errors may behave differently from natural hallucinations.\n\n**Phase 2: Blind Spot Measurement (3 weeks).** For each atomic claim (both injected and natural errors), measure whether the model can (a) detect the error when presented as external input (external detection), (b) detect it in its own output (self-detection), and (c) correct it in its own output (self-correction). This yields a claim-type-stratified blind spot matrix: BS(model, claim_type) = 1 − P(self-correct | error) / P(external-correct | error). We test 8 models: DeepSeek-V4-Pro, Qwen3.5-27B, Qwen3.5-122B-A10B, Llama-4-Maverick, Llama-3.3-70B-Instruct, Qwen3-32B, Mistral-Small-24B-Instruct, and DeepSeek-V3. The central testable hypothesis is that the blind spot is heterogeneous across claim types — e.g., entity errors may be more detectable/correctable than temporal or relational errors, mirroring the Error Depth Hypothesis's finding that error type predicts correctability in math. A secondary analysis examines whether correction suppression effects (arXiv:2605.05957) manifest in our setting: we compare blind spot rates for claims embedded in full generated responses (task context) vs. claims presented in isolation, testing whether task-oriented framing compounds the blind spot.\n\n**'Wait' Ablation (within Phase 2).** We explicitly test whether Self-Correction Bench's 'Wait' trick transfers to factual claims. For each model, we compare blind spot rates with and without the 'Wait' prompt appended during self-correction. Our hypothesis is that 'Wait' will show substantially diminished effectiveness for factual claims compared to its 89.3% reduction on math, because: (i) factual errors in knowledge-intensive generation often stem from genuine knowledge gaps (entity confusion, outdated temporal facts, relation misattribution) rather than the activation failures that 'Wait' addresses — the model lacks the correct information, not the motivation to correct; (ii) Self-Correction Bench's training-data analysis shows correction markers are concentrated in reasoning datasets (median 30–170 per response) but nearly absent from non-reasoning text (95th percentile = 1), suggesting 'Wait' may lack the conditioning effect for factual correction sequences; (iii) correction suppression (arXiv:2605.05957) demonstrates that even when models possess the knowledge, task context diverts attention at a deeper mechanistic level than simple activation failure — hidden-state similarity >0.99 indicates the model registers the error but suppresses correction. If 'Wait' proves effective for factual claims (>50% blind spot reduction), this would be an important positive finding that simplifies the problem — we would report it prominently and reframe the correctability classifier as addressing the remaining residual blind spot.\n\n**Phase 3: Behavioral Correctability Classifier (2 weeks).** Train a lightweight classifier that predicts, for each atomic claim in a new response, whether self-correction will succeed or fail. Unlike the PANL-based approach (arXiv:2604.22271) which requires white-box access to residual-stream activations, and unlike CyberCorrect (arXiv:2605.17305) whose tri-modal detector uses logic-chain verification suited only to reasoning tasks, our classifier uses black-box behavioral features appropriate for factual claims in long-form text: (i) multi-sample self-consistency score (SelfCheckGPT-style), (ii) verbal confidence when asked to rate claim certainty, (iii) claim type (entity/temporal/numerical/relational), (iv) claim specificity (more specific claims may be harder to correct, informed by SA/CSS findings), (v) detection-correction gap (whether the model flags the claim as uncertain but fails to correct it — measuring the gap between the blind-spot-as-detection-failure and blind-spot-as-correction-failure). The classifier explicitly targets CORRECTABILITY, not confidence — a distinction supported by three independent findings: DeepMind's result that behavioral confidence signals (AUROC=0.524) fail to predict correction success even when internal representations succeed (AUROC=0.614); the Functional Dissociation study (arXiv:2604.19974) showing uncertainty and correctness are encoded by distinct feature populations in Llama-3.1-8B and Gemma-2-9B; and the existence of 6+ papers (SA, CSS, CLC, CURE, CAG, VeriFY) that achieve strong calibration without enabling correction.\n\n**Pre-registered AUROC expectations.** We anchor expectations against known baselines: DeepMind's white-box PANL probes achieve AUROC=0.614 for correction prediction, while their behavioral confidence baseline achieves only 0.524. Black-box hallucination DETECTION (a strictly easier task than correctability prediction) achieves AUROC 0.75–0.82 with self-consistency methods (SelfCheckGPT). We pre-register: AUROC > 0.58 constitutes a positive result, demonstrating that claim-type and specificity features add meaningful signal beyond confidence alone for correctability prediction (significantly beating the 0.524 behavioral confidence baseline). AUROC > 0.63 constitutes a strong result, approaching DeepMind's white-box performance (0.614) without requiring model internals. If AUROC falls in the 0.55–0.58 range, the classifier contribution is acknowledged as modest, but the correctability-confidence dissociation analysis (comparing classifier features' predictive power for correctability vs. confidence) remains an important finding — demonstrating that even when correctability is hard to predict, it is not the same signal as confidence. If the heterogeneous-blind-spot hypothesis does not hold (i.e., the blind spot is roughly uniform across claim types), the classifier reduces to a uniform threshold policy — in this case, the benchmark itself, the natural-vs-injected comparison, the 'Wait' ablation results, and the characterization of confidence-vs-correctability dissociation remain the primary contributions, and we report the negative result as informative for the field.\n\n**Phase 4: Correctability-Guided Selective Fact Correction (2 weeks).** Implement SFC, which routes each claim through the correctability classifier. The key distinction from existing selective-handling approaches: SA (arXiv:2602.11908), CSS (arXiv:2604.17487), CLC (arXiv:2502.19110), CURE (arXiv:2604.12046), and CAG (arXiv:2605.01749) all use CONFIDENCE or CALIBRATION as the routing signal and respond to uncertainty through ABSTRACTION, SUPPRESSION, or HEDGING. SFC uses CORRECTABILITY as the routing signal and responds differently based on predicted correction success: claims predicted as correctable undergo ConFix-style intra-response confidence bootstrapping (attempting actual factual correction); claims in the predicted blind spot are flagged for abstention (marked as uncertain) or left unchanged to avoid destructive correction. This means SFC can handle cases that SA/CURE miss (confidently wrong but correctable claims) and avoids cases where SA over-abstracts (uncertain but actually correct claims that SA would unnecessarily vaguify). Compare against: (a) no correction baseline, (b) full naive self-correction (ask model to correct everything), (c) Selective Abstraction (SA) — confidence-based abstraction baseline operating on the same atomic claims, (d) CURE reference comparison — using CURE's published results on Biography/FactBench as reference points for the calibration-with-fine-tuning paradigm (noting CURE requires multi-stage fine-tuning while SFC is inference-time), (e) FactCorrector-style external-knowledge correction as an oracle upper bound, (f) random selective correction, (g) confidence-threshold selective correction (applying SA's confidence signal but with correction instead of abstraction, to isolate the correctability vs. confidence distinction), (h) 'Wait'-augmented self-correction (applying the 'Wait' trick globally, to isolate whether activation-based intervention subsumes our approach). Evaluate using FActScore and SAFE metrics, plus an information-retention metric (following SA's information-theoretic measure) to ensure SFC preserves more content than abstraction-only approaches.\n\n## Resource Estimate\n{'manual': {'gpu_hours': \"750-1100 (inference-only: 8 models × 3 datasets × multi-sample generation + correction passes; natural-error track adds ~20% overhead for multi-sample consistency; SA baseline replication adds ~10%; 'Wait' ablation adds ~15%; on 4×A100 node)\", 'timeline': \"13-16 weeks (3 weeks benchmark construction including natural-error track, 3 weeks blind spot measurement including suppression analysis and 'Wait' ablation, 2 weeks correctability classifier, 2 weeks SFC pipeline + SA/CURE baseline comparison, 3-4 weeks writing and ablations)\", 'estimated_gpu_cost': '$1125-$1650 at ~$1.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': \"550-850 (Claude handles decomposition, error injection templates, multi-sample generation orchestration, SA baseline replication, 'Wait' ablation orchestration, and result analysis; human steers experiment design and interprets blind spot patterns)\", 'timeline': \"9-12 weeks (2.5 weeks benchmark with Claude-assisted decomposition + natural-error curation, 2.5 weeks measurement including 'Wait' ablation, 1.5 weeks classifier, 1.5 weeks SFC + baselines, 2-3 weeks writing)\", 'claude_api_cost': '$500-$800 (atomic decomposition of ~12K responses × ~10 claims each via Sonnet 4.6; error injection generation; correctability annotation; paper drafting)', 'estimated_gpu_cost': '$825-$1275'}, 'auto_research': {'gpu_hours': \"450-700 (automated sweep over models, claim types, 'Wait' ablation, and ablations)\", 'timeline': \"7-9 weeks (2 weeks benchmark auto-construction + natural-error curation, 2 weeks parallel blind spot sweeps + 'Wait' ablation, 1.5 weeks classifier training + SFC + SA baseline, 1.5-2 weeks writing)\", 'claude_api_cost': '$900-$1400 (heavier API use for automated claim decomposition, error injection, multi-sample consistency scoring, experiment orchestration, and iterative analysis)', 'estimated_gpu_cost': '$675-$1050', 'speed_bottleneck': \"Sequential model inference for blind spot measurement — each model must generate, then attempt correction (with and without 'Wait'), for thousands of claims; parallelizable across models but not within a single model's correction chain. Natural-error track requires multi-sample generation for consistency scoring.\"}}\n\n## Inspired By\nCombination of blind spot phenomenon (Self-Correction Bench) + the 'Wait' trick's 89.3% blind spot reduction on math raising the question of whether activation-based interventions transfer to factual knowledge tasks + Error Depth Hypothesis (error type predicts correctability in math) + correction suppression discovery (arXiv:2605.05957, showing task context suppresses factual correction 19-90%, which may compound the blind spot in knowledge-intensive generation) + fact-level confidence calibration (ConFix) + FactSelfCheck granularity results + DeepMind PANL correctability prediction (showing the signal exists but hasn't been studied at fact level or with black-box methods) + CyberCorrect's tri-modal detector features (self-consistency + confidence + error type for correction routing, but only on reasoning tasks) + Selective Abstraction's demonstration that atom-wise handling works at scale on FActScore (but abstracts rather than corrects) + CURE's claim-level calibration on biography generation (arXiv:2604.12046, achieving 39.9% accuracy improvement but never attempting correction) + CAG's exploration-commitment decoupling (arXiv:2605.01749, improving VeriScore but suppressing rather than correcting) + Functional Dissociation finding that uncertainty and correctness are encoded by distinct feature populations (arXiv:2604.19974); TACL survey finding that self-correction conditions are poorly understood outside reasoning tasks; the observation that FactCorrector achieves 67.4% atom correction WITH external knowledge but no one has measured intrinsic self-correction rates at atom level; Atomic Calibration's finding that LLMs show poorer calibration at atomic level in long-form generation; the emerging pattern that 6+ papers now pursue confidence-based claim-level abstention while zero papers pursue correctability-based claim-level correction.\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026 — tight but feasible with auto_research timeline)\n- EACL 2027 via ARR (submission: August 3, 2026; commitment: October 11, 2026)\n- ICLR 2027 (expected submission: ~September-October 2026, dates TBA)\n- NAACL 2027 via ARR (submission: ~October 2026; commitment: ~October 16, 2026)\n- TACL (rolling monthly deadlines, any month 2026)\n\n## Key References\n- FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (Min et al., EMNLP 2023)\n- SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models (Manakul et al., EMNLP 2023)\n- Chain-of-Verification Reduces Hallucination in Large Language Models (Dhuliawala et al., arXiv 2023)\n- Long-form Factuality in Large Language Models — SAFE (Wei et al., arXiv 2024, arXiv:2403.18802)\n- Atomic Self-Consistency for Better Long Form Generations (Agrawal et al., EMNLP 2024)\n- Fact-Level Confidence Calibration and Self-Correction — ConFix (arXiv:2411.13343, 2024)\n- Atomic Calibration of LLMs in Long-Form Generations (Zhang et al., ACL 2025 KnowFM / AACL-IJCNLP 2025, arXiv:2410.13246)\n- Confidence v.s. Critique: A Decomposition of Self-Correction Capability for LLMs (Yang et al., ACL 2025, arXiv:2412.19513)\n- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models (submitted to ICLR 2026, arXiv:2507.02778)\n- FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs (arXiv:2503.17229, 2025)\n- The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input (arXiv:2501.03200, 2025)\n- Know Your Limits: A Survey of Abstention in Large Language Models (arXiv 2025)\n- Enhancing LLM Reliability via Explicit Knowledge Boundary Modeling (arXiv 2025)\n- When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs (Kamoi et al., TACL 2025, arXiv:2406.01297)\n- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis (arXiv:2601.00828, Jan 2026)\n- FactCorrector: A Graph-Inspired Approach to Long-Form Factuality Correction + VELI5 Benchmark (arXiv:2601.11232, Jan 2026)\n- Conformal Linguistic Calibration: Trading-off between Factuality and Specificity (Jiang et al., arXiv:2502.19110, Feb 2026)\n- When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (Goren et al., arXiv:2602.11908, Feb 2026)\n- VeriFY: Learning Factual Self-Verification for Hallucination Reduction (arXiv:2602.02018, Feb 2026)\n- Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv:2603.06604, Mar 2026)\n- Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration — CURE (arXiv:2604.12046, Apr 2026)\n- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (Kumaran et al., DeepMind, arXiv:2604.22271, Apr 2026)\n- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, Apr 2026)\n- I-CALM: Incentivizing Confidence-Aware Abstention for LLM Hallucination Mitigation (arXiv:2604.03904, Apr 2026)\n- Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control — CSS (arXiv:2604.17487, Apr 2026)\n- AtomEval: SROM-atom Decomposition for Adversarial Fact Verification (arXiv:2604.07967, Apr 2026)\n- Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality — CAG (arXiv:2605.01749, May 2026)\n- Knowing but Not Correcting: Routine Task Requests Suppress Factual Correction in LLMs (Chen et al., arXiv:2605.05957, May 2026)\n- CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models (Wu et al., arXiv:2605.17305, May 2026)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T05:56:05.715Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:56:05.715Z",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T05:56:05.747Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. Self-Correction Bench (arXiv:2507.02778, submitted ICLR 2026): 确立了 LLM 自纠错盲区概念，14 个非推理模型平均 64.5% 盲区率，"Wait" trick 降低 89.3%——但仅在 GSM8K/PRM800K 数学任务上、以 problem-level 粒度进行测量。论文确认存在，描述准确。

2. CURE (arXiv:2604.12046, Apr 2026): 在 biography generation 上实现 39.9% claim-level accuracy 提升，通过 &lt;think>→&lt;decompose>→&lt;answer> 协议进行 claim-level 校准。**需要多阶段微调 (SFT+DPO+GRPO)**，仅做 calibrated abstention 不做 correction。与 proposal 共享任务域但方法论完全不同。确认存在，描述准确。

3. Selective Abstraction / SA (arXiv:2602.11908, Feb 2026): 将 response 分解为 atomic claims，用 confidence-based abstraction 替换 uncertain claims，AURC 提升最高 27.73%。仅做 abstraction 不做 correction。确认存在，描述准确。

4. CAG (arXiv:2605.01749, May 2026): Exploration-Commitment Decoupling，VeriScore 67.79%→79.80%。需要微调，suppresses 而非 corrects unreliable claims。确认存在，描述准确。

5. DeepMind PANL correctability (arXiv:2604.22271, Apr 2026, Kumaran et al.): 发现 post-answer newline token 处的 residual-stream activations 可以预测 correction success (AUROC=0.614)，而 behavioral confidence 仅 0.524。需要 white-box access，仅在 TriviaQA/MNLI problem-level 上测试。确认存在，描述准确。

6. "Knowing but Not Correcting" (arXiv:2605.05957, May 2026): 发现 correction suppression——模型在 isolation 中能纠正错误但在 task context 中抑制纠正（19-90% suppression rates across 8 models）。Hidden-state similarity >0.99 表明模型内部识别了错误但选择 comply。确认存在，描述准确。

7. CyberCorrect (arXiv:2605.17305, May 2026): 三模态 error detector (self-consistency 0.4 + verbalized confidence 0.35 + logic-chain verification 0.25)，在 reasoning tasks 上 79.8% accuracy，41% reduction in over-correction。需要 reasoning chains，在 problem-level 上操作。确认存在，描述准确。

8. Functional Dissociation (arXiv:2604.19974, Apr 2026): SAE 分析表明 uncertainty 和 correctness 由不同 feature populations 编码；suppress uncertainty features 导致 accuracy 下降最高 10.21%，而 suppress incorrectness features 几乎无影响。确认存在，描述准确。

9. FactSelfCheck (arXiv:2503.17229, 2025): Fact-level black-box hallucination detection，KG-style triple representation，35.5% vs 10.6% factual improvement for fact-level vs sentence-level。确认存在，描述准确。

10. ConFix (arXiv:2411.13343, 2024): Fact-level confidence calibration + self-correction，high-confidence facts bootstrap correction of low-confidence facts。确认存在，描述准确。

11. FactCorrector + VELI5 (arXiv:2601.11232, Jan 2026): Graph-inspired correction pipeline + 17,522 instance benchmark with injected errors. 67.4% correction of incorrect atoms with structured feedback + external knowledge. 确认存在，描述准确。

12. CSS (arXiv:2604.17487), CLC (arXiv:2502.19110), VeriFY (arXiv:2602.02018), I-CALM (arXiv:2604.03904): 均为 claim-level confidence/calibration-based abstention 方法，无一尝试 correction。

- **调研总结**: 这个领域在 2025-2026 经历了爆发式增长，两个方向并行发展但未交汇：(A) self-correction blind spot 研究停留在 math/reasoning + problem-level 粒度；(B) claim-level factuality 处理已形成拥挤的 confidence-based abstention 赛道（6+ papers），但无一尝试 correctability-based correction routing。Proposal 精准定位在这两个方向的交叉空白处——将 blind spot 分析下沉到 fact-level 粒度、将 correctability（而非 confidence）作为 routing signal。领域文献引用高度准确，未发现 misrepresentation。

【Trivial Alternative 检验】:

最直接的 trivial alternative 是：**直接用 confidence threshold 做 correction routing**——即把 SA/CURE 的 confidence signal 原封不动地用来决定 "纠正 vs. 放弃"，而非 proposal 所提出的 correctability classifier。

这个 trivial alternative 的威胁程度：**中等但可控**。Proposal 显式引用了三条独立证据来论证 confidence ≠ correctability：(1) DeepMind PANL 结果 behavioral confidence AUROC 仅 0.524 vs. internal AUROC 0.614；(2) Functional Dissociation 证明 uncertainty 和 correctness 由不同 feature populations 编码；(3) 6+ papers 实现了强 calibration 但无法 enable correction。Proposal 还将 confidence-threshold correction 作为 explicit baseline (h)。如果实验证实 confidence-threshold correction 已经接近 correctability classifier 的效果，那 novelty 确实受损——但 proposal 的 pre-registered 设计已经预见了这一风险，且即使 classifier 表现平庸，correctability-confidence dissociation 本身作为 empirical finding 仍有价值。

第二个 trivial alternative："Wait" trick 直接迁移到 factual claims 上就行了。Proposal 将此作为核心假设来测试而非假定不行，设计了专门的 ablation。如果 "Wait" 在 factual claims 上同样有效（>50% blind spot reduction），proposal 承认这是重要的 simplifying finding 并 reframe 贡献。这种 dual-outcome 设计是合理的。

**增量价值所在**：即使两个 trivial alternatives 都部分有效，proposal 仍提供：(a) 首个 fact-level 粒度的 blind spot 系统测量（目前零篇论文做过这个）；(b) claim-type-stratified 盲区分析；(c) correctability vs. confidence 的 empirical dissociation 在 factual domain 的首次验证。这些 benchmark 和 characterization 贡献不受 trivial alternative 影响。

【前提假设检验】:

核心 claim 的逻辑链：

**假设 1：Math 领域的 blind spot 现象能推广到 knowledge-intensive generation**
- 支撑度：中等。Correction suppression (arXiv:2605.05957) 已在 factual domain 发现 19-90% suppression rates，间接支持 blind spot 在 factual domain 存在。但 blind spot 的 **heterogeneity across claim types** 尚无直接证据——这确实是 proposal 要测试的核心假设，而非预设结论。合理。

**假设 2："Wait" trick 对 factual claims 效果显著弱于 math**
- 支撑度：中等偏强。Self-Correction Bench 的 training-data analysis 表明 correction markers 集中在 reasoning datasets（中位 30-170/response）但在 non-reasoning text 中几乎不存在（95th percentile = 1），这为 "Wait" 在非推理领域失效提供了间接证据。Correction suppression 的机制也在更深层（hidden-state level）而非 activation failure。但这仍是 hypothesis 而非 established fact，proposal 正确地将其设计为可测试的。

**假设 3：Black-box behavioral features 能 outperform confidence baseline 预测 correctability**
- 支撑度：较弱，这是最大风险点。DeepMind 的结果表明 white-box internal representations 可以预测 correctability (AUROC=0.614)，但 behavioral confidence 仅 0.524。Proposal 认为加入 claim type + specificity + detection-correction gap 等 features 可以弥补 black-box 的劣势——但没有先验证据表明这些 features 对 correctability 有预测力。CyberCorrect 的三模态 detector 在 reasoning tasks 上有效，但其 logic-chain verification component 不适用于 factual claims。Proposal 的 pre-registered AUROC>0.58 阈值设置合理（参照 DeepMind 的 0.614 和 confidence baseline 的 0.524），但 classifier 性能仍是最大的不确定性。

**假设 4：Correctability 和 confidence 在 factual domain 是 empirically dissociable 的**
- 支撑度：较强。Functional Dissociation 已在 SAE level 证明了这一点；DeepMind PANL 结果在 behavioral level 也支持。但这些都不是在 long-form factual generation 的 atomic claim level 上验证的——proposal 要做的正是这个 gap 的 empirical 填充。

**最薄弱环节**：假设 3——black-box correctability classifier 能否达到有意义的 AUROC。如果 classifier 仅达到 0.53-0.55（接近 confidence baseline），则 SFC pipeline 的 practical value 大幅缩水。不过 proposal 已设计了 graceful degradation path：即使 classifier 表现平庸，benchmark + blind spot characterization + "Wait" ablation + dissociation analysis 仍有独立贡献。

【3 维度打分】:

1. **Novelty: 中偏强** — 
   Proposal 定位了一个真实的、可验证的空白交叉点：self-correction blind spot 研究 (Self-Correction Bench, Error Depth Hypothesis) 停留在 math/problem-level；claim-level factuality 处理已拥挤但全部走 confidence-based abstention 路线 (SA, CSS, CLC, CURE, CAG, VeriFY = 6+ papers)；correctability prediction 只有 white-box (DeepMind PANL) 和 reasoning-only (CyberCorrect) 方案。**将 blind spot 分析下沉到 atomic claim level + correctability-based routing 在 factual domain 的首次探索** 这个组合确实是 unoccupied 的。

   降分因素：这是一个 **"自然延伸" 型 novelty** 而非 **"反直觉发现" 型 novelty**。核心 idea 可以概括为 "把 self-correction blind spot 的分析从 problem-level math 搬到 claim-level facts，然后用 correctability 替代 confidence 做 routing"——方向正确但不令人 surprised。审稿人可能会说 "interesting gap, obvious to fill"。与之对比，Functional Dissociation 或 Correction Suppression 的发现本身具有更强的 surprise factor。

2. **Significance: 中偏强** — 
   研究问题的重要性很高：LLM 在 knowledge-intensive generation 中的 factual accuracy 是部署的核心瓶颈；6+ papers 在同一问题上发力但都走了 abstention 路线说明需求真实。如果 blind spot 确实在 claim types 间存在 heterogeneity，且 correctability ≠ confidence 在 factual domain 得到验证，这对整个 claim-level factuality handling 领域的方向有指导意义。

   降分因素：SFC pipeline 本身的 practical impact 取决于 classifier 性能，如果 AUROC 仅略高于 confidence baseline，downstream improvement 可能有限。不过 benchmark 和 characterization 的独立价值不受此影响。

3. **Related Work: 强** — 
   这是该 proposal 最突出的优势之一。引用的 25+ 篇论文全部经核实存在且描述准确。领域格局的梳理极其系统：清晰区分了 (a) blind spot literature (math/problem-level), (b) fact-level hallucination literature, (c) correctability prediction (white-box/reasoning-only), (d) selective claim-level handling (confidence-based abstention) 四条线索，并在交叉点定位自己。差异化定位非常清晰——"ALL 6+ papers use confidence, NONE attempt correctability-based correction"。这种 exhaustive 且 accurate 的 landscape mapping 在 proposal 阶段是少见的。

   唯一微弱不足：对 CorrectBench (arXiv:2510.16062) 的引用缺失——这是另一个系统评估 self-correction 的 benchmark，虽然也集中在 reasoning tasks 但应提及以显示更完整的 awareness。

【概率估计】: 28% - 38%，中位 33%

【估计理由】: 
- **Novelty (中偏强)** 和 **Significance (中偏强)** 共同支撑了 30%+ 的基础概率。Gap 是真实的、定位精准、related work 梳理极强。
- **向上受限的主要因素**：核心 novelty 是 "natural extension" 型而非 "surprising insight" 型。审稿人很可能认为 "当然 blind spot 在 factual claims 上也存在，当然 correctability ≠ confidence"——核心发现如果 positive，部分审稿人会说 "I would have guessed this"。这限制了上界在 38% 而非更高。
- **向上支撑因素**：(1) 精准的空白定位和系统的 landscape coverage 在 rebuttal 中很有价值；(2) dual-outcome 设计和 pre-registered thresholds 显示方法论成熟度；(3) 如果 "Wait" ablation 产生 surprising 结果（无论正面还是负面），可以显著提升 narrative impact。
- **向下风险**：如果 classifier AUROC 仅 0.53-0.55 且 "Wait" 在 factual domain 意外有效（>50% reduction），proposal 的核心 SFC 贡献会被大幅削弱，此时需要靠 benchmark + characterization 支撑——作为 resource paper / analysis paper 的概率可能降至 25% 左右。

【主要风险】:
1. **"Natural extension" novelty ceiling**：核心贡献被审稿人视为 "obvious gap to fill" 而非 "surprising finding"——blind spot 从 math 到 facts 的迁移、correctability ≠ confidence 的论证，方向上都不令人意外，只是没人做过。这可能导致 "incremental" 的评价。
2. **Correctability classifier 的 black-box 性能天花板**：如果 claim-type + specificity 等 features 对 correctability 的预测力有限（AUROC 接近 confidence baseline 的 0.524），则 SFC 的 practical value 和 "correctability ≠ confidence" 的论证力度都会受损，proposal 的 Phase 3-4 贡献会大幅缩水。
```

Sources:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)
- [CURE: Think Through Uncertainty (arXiv:2604.12046)](https://arxiv.org/abs/2604.12046)
- [Selective Abstraction (arXiv:2602.11908)](https://arxiv.org/abs/2602.11908)
- [CAG: Calibration-Aware Generation (arXiv:2605.01749)](https://arxiv.org/abs/2605.01749)
- [DeepMind PANL: How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)
- [Knowing but Not Correcting (arXiv:2605.05957)](https://arxiv.org/html/2605.05957v1)
- [CyberCorrect (arXiv:2605.17305)](https://arxiv.org/abs/2605.17305)
- [Functional Dissociation via SAEs (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)
- [FactSelfCheck (arXiv:2503.17229)](https://arxiv.org/abs/2503.17229)
- [FactCorrector + VELI5 (arXiv:2601.11232)](https://arxiv.org/abs/2601.11232)
- [CSS (arXiv:2604.17487)](https://arxiv.org/html/2604.17487)
- [ConFix (arXiv:2411.13343)](https://arxiv.org/pdf/2411.13343)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have a comprehensive picture of the literature. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Self-Correction Bench, arXiv:2507.02778] (submitted ICLR 2026): 定义了 self-correction blind spot 概念，14 个非推理模型平均 64.5% blind spot rate（GSM8K/PRM800K）。'Wait' trick 减少 blind spot 89.3%。关键限制：仅在 math 任务、problem-level 粒度。这是本 proposal 的直接上游工作和出发点。
- [CURE, arXiv:2604.12046] (Apr 2026): Claim-level calibration for biography generation，&lt;think>→&lt;decompose>→&lt;answer> protocol，39.9% claim-level accuracy improvement。需要 SFT+DPO+GRPO 多阶段微调。关键：仅做 calibrated abstention，不尝试 correction。与本 proposal 在任务域（biography generation）高度重叠但范式不同。
- [Selective Abstraction (SA), arXiv:2602.11908] (Feb 2026): Atom-wise 分解 + confidence-based abstraction，在 FActScore/LongFact 上 AURC 提升最高 27.73%。只做 abstraction，不做 correction。是本 proposal 的直接 baseline。
- [CAG, arXiv:2605.01749] (May 2026): Exploration-Commitment Decoupling，VeriScore 67.79%→79.80%。同样只做 suppression 不做 correction。需要微调（CASS+CAPD）。
- [DeepMind PANL, arXiv:2604.22271] (Apr 2026): White-box PANL probes 预测 correction success AUROC=0.614，behavioral confidence 仅 0.524。仅在 TriviaQA/MNLI problem-level 上测试 Gemma 3 27B 和 Qwen 2.5 7B。是 correctability prediction 的直接竞争/上游工作。
- [CyberCorrect, arXiv:2605.17305] (May 2026): Tri-modal error detector (self-consistency 0.4 + verbalized confidence 0.35 + logic-chain verification 0.25)，type-directed correction，79.8% accuracy。仅在 reasoning tasks 上测试，logic-chain feature 不适用于 factual claims。
- [Functional Dissociation, arXiv:2604.19974] (Apr 2026): SAE 分析表明 uncertainty 和 correctness 由 functionally distinct feature populations 编码。suppressing uncertainty features 导致 accuracy 下降最高 10.21%，suppressing incorrectness features 几乎无变化。为"confidence ≠ correctability"提供了 mechanistic evidence。
- [Knowing but Not Correcting, arXiv:2605.05957] (May 2026): Correction suppression 现象——模型单独面对 false claim 时能纠正，但嵌入 task context 后 suppress correction（19-90% suppression rate）。Hidden-state similarity >0.99 证明模型 internally registers error。
- [ConFix, arXiv:2411.13343] (2024): Fact-level confidence calibration + self-correction，高置信度 facts bootstrap 低置信度 facts 的 correction。这是一个重要的 trivial alternative 威胁——已经在做 fact-level self-correction，虽然用的是 confidence 而非 correctability。
- [FactCorrector + VELI5, arXiv:2601.11232] (Jan 2026): Graph-inspired correction pipeline + 17,522 instances benchmark，67.4% atom correction rate。但依赖外部知识检索。
- [FactSelfCheck, arXiv:2503.17229] (2025): Fact-level hallucination detection，35.5% vs 10.6% factual improvement 对比 sentence-level。
- [CSS, arXiv:2604.17487] (Apr 2026): Claim-level specificity control，back off overcommitted claims。
- [CLC, arXiv:2502.19110] (Feb 2026): Conformal linguistic calibration，conformal guarantees on claim factuality。

- **调研总结**: Self-correction blind spot 研究目前被限制在 math/reasoning 的 problem-level 粒度。与此同时，fact-level claim handling 领域在 2026 年 2-5 月爆发式增长（SA, CSS, CLC, CURE, CAG 等 6+ 篇论文），但全部采用 confidence/calibration 作为 routing signal，响应方式为 abstention/suppression/hedging，无一尝试基于 correctability 的 correction routing。Proposal 精确定位在这两条线的交叉点——fact-level granularity × correctability-based correction——这个交叉点确实 unoccupied。但该定位的价值高度依赖于"correctability ≠ confidence"这个区分在 fact-level 实践中的真实效应大小。


【Trivial Alternative 检验】:

存在两个需要认真对待的 trivial alternatives：

1. **ConFix + naive self-correction**: ConFix 已经在做 fact-level self-correction，使用 confidence-based bootstrapping。如果在本 proposal 的 benchmark 上直接跑 ConFix，能达到 SFC 效果的 80%+，那 correctability classifier 的增量价值就很有限。Proposal 确实将 ConFix-style bootstrapping 纳入了 SFC 的 correction 子模块，但没有直接 head-to-head 对比 ConFix 的 confidence routing vs. correctability routing 的边际差异。

2. **'Wait' trick 直接应用到 factual claims**: Proposal 包含了 'Wait' ablation（Phase 2），这是正确的。但如果 'Wait' 在 factual claims 上也有 30-50% 的 blind spot reduction（即使不如 math 的 89.3%），那 'Wait' + naive self-correction 可能就是 "good enough" 的 trivial baseline。Proposal 的核心价值取决于 'Wait' ablation 的负面结果。

**增量价值在哪**: 如果上述两个 trivial alternatives 都不够好（'Wait' 对 facts 无效 + confidence 和 correctability 的 gap 在 fact-level 足够大），那 correctability-guided routing 确实是一个有意义的新方向。但这个增量价值是 **conditional on empirical results** 的——这不是一个无论实验结果如何都有清晰增量的 idea。


【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的关键假设：

1. **"Factual errors stem from knowledge gaps, not activation failures"——这个二分法过于简化**。并非所有 factual errors 都是 knowledge gaps。很多 hallucinations（尤其是 entity confusion、date off-by-one）可能也是 activation/retrieval failures，'Wait' 可能对这些同样有效。Proposal 将 math errors = activation failures vs. factual errors = knowledge gaps 作为一个核心前提，但实际的 error taxonomy 可能远比这复杂。如果相当比例的 factual errors 也是 activation failures，整个故事的 motivation 就被削弱了。

2. **"Behavioral features 能足够好地捕捉 correctability"——来自 DeepMind 结果的证据其实是 negative 的**。DeepMind 发现 behavioral confidence 只有 AUROC 0.524（接近随机），而 white-box features 才有 0.614。Proposal 认为加入 claim type + specificity + detection-correction gap 能显著提升，但没有先验证据支持这一点。如果最终只达到 0.55-0.58，SFC 的实际效用会非常有限。

3. **"Error Depth Hypothesis 从 math 迁移到 factual claims"——类比推理，未经验证**。Math 中的 error depth（calculation vs. logic vs. setup）和 factual claim types（entity, temporal, numerical, relational）是完全不同的 taxonomy。Error Depth 发现的是 model capability 相关的 depth gradient，factual claim types 之间是否存在类似的 difficulty gradient 是一个 open question。

4. **"Correction suppression 会 compound blind spot"——外推**。arXiv:2605.05957 的实验设置（isolated false claim vs. task-embedded false claim）和本 proposal 的设置（model 纠正自己生成的 output 中的 errors）是不同的。能否直接外推需要验证。


【3 维度打分】:

1. **Novelty: 中** — 
   Proposal 精确定位在 fact-level × blind spot × correctability 这个 unoccupied intersection，这一点是成立的。调研证实：Self-Correction Bench 仅覆盖 math/problem-level；SA/CURE/CAG 等 6+ 篇只做 confidence-based abstention，不做 correctability-based correction；DeepMind PANL 仅在 problem-level + white-box。然而，novelty 主要来自 **extension**（将已知概念推广到新粒度和新域）而非 **discovery**（发现新机制或反直觉现象）。核心预测——blind spot 在 factual claims 上存在且比 math 更严重，'Wait' 对 facts 效果减弱，不同 claim types 有不同 blind spot rates——大多数研究者会猜到这些方向。Correctability classifier 的构建借鉴了 CyberCorrect 的 feature 设计思路（self-consistency + confidence + type），主要替换了 logic-chain feature 为 claim-specific features，属于 adaptation 而非 innovation。最有 novelty 的贡献是 'Wait' ablation 在 factual domain 的系统性测试，以及 correctability-confidence dissociation 的 claim-level 量化——但这些更像是 "good to know" 而非 "surprising"。

2. **Significance: 中偏强** — 
   研究问题本身是重要的。Self-correction 是 LLM 部署的核心能力，理解其在 knowledge-intensive generation 中的 fine-grained limitations 对实际应用有直接影响。6+ 篇论文在 2026 年 2-5 月密集出现在 claim-level handling 空间，证明了这个方向的热度和社区关注度。如果 benchmark 和 blind spot characterization 做得好，将为后续研究提供基础设施价值（类似 FActScore 对 factual evaluation 的贡献）。但 significance 被两点限制：(a) SFC pipeline 的实际改进幅度可能有限（correctability classifier 的 ceiling 不高），使得下游应用价值不确定；(b) 如果核心发现是"blind spot 在 facts 上更严重，'Wait' 不好使"，这是 confirmatory 而非 transformative。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。覆盖了 5 条独立研究线（blind spot literature, fact-level hallucination, correctability prediction, selective claim handling, mechanistic evidence），引用了 30+ 篇论文，包括 2026 年 5 月的最新工作（CAG, CyberCorrect, Knowing but Not Correcting）。差异化定位清晰：与 SA/CURE/CAG 的区别（correctability vs. confidence, correction vs. abstention）、与 DeepMind PANL 的区别（black-box vs. white-box, claim-level vs. problem-level）、与 CyberCorrect 的区别（factual claims vs. reasoning, claim-level vs. step-level）都论述得非常到位。调研证实所有引用论文真实存在且描述准确。唯一微小问题：过于详尽的 related work 使得 proposal 读起来像一篇 survey，但这在入口评估中不是减分项。


【概率估计】: [25% - 35%] 中位 29%

【估计理由】: 
Novelty 处于"中"水平——gap 真实存在但 core findings 的预期方向是 intuitive 的（审稿人大概率会说 "I would have guessed this"），这是限制上界的主要因素。Significance 中偏强，因为研究问题重要、领域热度高、benchmark 有基础设施价值，这拉高了下界。Related Work 强，positioning 清晰无遗漏，但 related work 的完善度属于执行质量，不改变 idea 上限。

从 rubric 锚点看：idea 有实质内核（真实的 novelty delta），方向正确，但核心发现如果 positive，审稿人更可能说 "good systematic study, confirms what I expected" 而非 "surprising"——这把它锚定在 25-35% 区间。中位取 29% 而非 30%+ 是因为 trivial alternative 威胁（ConFix 和 'Wait' ablation）增加了 idea 被质疑为 incremental 的风险。

**限制上界的维度**: Novelty。Extension-type novelty（将已知概念推广到新域/粒度）在 top venues 通常不如 discovery-type novelty（发现新机制/反直觉现象）有竞争力，除非 extension 的过程中产生了 unexpected findings。

【主要风险】: 
1. **"Expected findings" 风险**: 三个核心预测（blind spot 在 facts 上存在/更严重、'Wait' 对 facts 无效、claim types 间 heterogeneous）都是大多数研究者会预期的方向。如果实验结果完全 confirm expectations，审稿人可能评价为 "well-executed but unsurprising"，这是 EMNLP 最常见的 borderline reject 理由之一。除非实验过程中发现某个 truly unexpected pattern（例如某种 factual claim type 的 blind spot 反而低于 math，或 'Wait' 在某些 claim types 上出奇有效），整篇论文缺乏 "aha moment"。
2. **Correctability classifier ceiling 过低的风险**: DeepMind 已经证明 behavioral signals 对 correctability 的预测力很弱（AUROC 0.524）。Proposal 的 classifier 加入了 claim type 和 specificity features，但如果最终 AUROC 只在 0.55-0.58 范围，SFC 相对于 confidence-threshold correction 的优势将非常边际，使得 Phase 3+4（classifier + SFC pipeline）的贡献变得 marginal，论文的贡献缩水为一个 benchmark paper。
```

Sources:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)
- [CURE (arXiv:2604.12046)](https://arxiv.org/abs/2604.12046)
- [Selective Abstraction (arXiv:2602.11908)](https://arxiv.org/abs/2602.11908)
- [CAG (arXiv:2605.01749)](https://arxiv.org/abs/2605.01749)
- [DeepMind PANL (arXiv:2604.22271)](https://arxiv.org/abs/2604.22271)
- [CyberCorrect (arXiv:2605.17305)](https://arxiv.org/abs/2605.17305)
- [Functional Dissociation (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)
- [Knowing but Not Correcting (arXiv:2605.05957)](https://arxiv.org/html/2605.05957v1)
- [ConFix (arXiv:2411.13343)](https://arxiv.org/abs/2411.13343)
- [FactCorrector + VELI5 (arXiv:2601.11232)](https://arxiv.org/abs/2601.11232)
- [FactSelfCheck (arXiv:2503.17229)](https://arxiv.org/abs/2503.17229)
- [CSS (arXiv:2604.17487)](https://arxiv.org/abs/2604.17487)
- [CLC (arXiv:2502.19110)](https://arxiv.org/abs/2502.19110)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- Self-Correction Bench (arXiv:2507.02778, submitted ICLR 2026): 确认存在。在GSM8K/PRM800K上测量14个非推理模型，64.5%平均blind spot率，'Wait'减少89.3%。但仅测试数学任务、问题级粒度。Proposal对该论文的描述准确。
- CURE (arXiv:2604.12046, Apr 2026): 确认存在。通过&lt;think>→&lt;decompose>→&lt;answer>协议在biography generation上实现39.9%声明级准确率提升，通过SFT+DPO+GRPO多阶段微调实现校准弃权。确认使用置信度/校准作为路由信号，从不尝试纠正。描述准确。
- Selective Abstraction (arXiv:2602.11908, Feb 2026): 确认存在。原子级声明分解+不确定声明用更模糊版本替换。描述准确。
- DeepMind PANL论文 (arXiv:2604.22271, Apr 2026): 确认存在。Kumaran等人展示PANL残差流激活的线性探针预测纠正成功(AUROC=0.614)，行为置信度仅0.524。需要白盒访问。描述准确。
- Functional Dissociation (arXiv:2604.19974, Apr 2026): 确认存在。通过稀疏自编码器在Llama-3.1-8B和Gemma-2-9B上证明不确定性和正确性由功能上不同的特征群编码。描述准确。
- CyberCorrect (arXiv:2605.17305, May 2026): 确认存在。三模态错误检测器(自一致性+口头置信度+逻辑链验证)，基于控制论框架。操作在推理任务上。描述准确。
- CAG (arXiv:2605.01749, May 2026): 确认存在。Exploration-Commitment Decoupling，VeriScore 67.79%→79.80%。需微调，抑制而非纠正不可靠声明。描述准确。
- FactSelfCheck (arXiv:2503.17229, Mar 2025): 确认存在。事实级黑盒幻觉检测，知识图谱三元组表示。描述准确。
- "Knowing but Not Correcting" (arXiv:2605.05957): **未能通过搜索验证**。多次搜索均未找到该论文。可能是非常近期发布尚未被索引，也可能arXiv ID有误。该论文被用作"纠正抑制"现象的关键论据之一。
- 未找到直接竞争工作：搜索"fact-level correctability prediction"和"correctability-based claim routing"未找到任何已发表的、在原子声明级别做correctability预测并用于路由的工作。这支持了proposal所声称的gap确实存在。

调研总结: 该领域在2026年初经历了快速发展——选择性声明级处理(SA, CSS, CLC, CURE, CAG)已成为拥挤赛道，但所有工作均使用置信度/校准作为路由信号，通过弃权/抽象化应对不确定性。Self-correction blind spot文献仅覆盖数学任务。Proposal定位在"原子声明级correctability预测+纠正路由"这个交叉空间，该空间确实未被占据。

【Trivial Alternative 检验】:
最直接的trivial alternative是：**直接使用SA/CURE的置信度信号，但将低置信度声明路由到纠正（而非弃权）**——即"confidence-threshold selective correction"。Proposal自己在Phase 4中将此作为baseline (g)纳入了，这显示了作者的自我意识。但问题在于：如果这个trivial baseline表现与SFC相当，那么整个correctability classifier的价值就会被大幅削弱。Proposal的增量价值完全取决于correctability ≠ confidence这个gap在实践中有多大。DeepMind论文显示PANL内部表征(0.614) vs 行为置信度(0.524)之间有gap，但这是白盒vs黑盒的差距，而proposal的分类器同样使用黑盒行为信号——为什么黑盒行为特征的组合(自一致性+口头置信度+声明类型+特异性)能显著超越单纯的行为置信度？这是proposal中最脆弱的环节。

第二个trivial alternative：**对所有声明统一执行naive self-correction**。如果模型对大部分能纠正的声明确实能纠正，对不能纠正的声明纠正后质量不显著下降（"destructive correction"率较低），那么选择性路由的价值就有限。Proposal也包含了这个baseline (b)，但并未论证destructive correction在实践中有多严重。

总体而言：trivial alternative威胁是真实存在的，proposal的增量价值高度依赖correctability-confidence dissociation在原子事实声明层面的实际大小。

【前提假设检验】:
1. **核心假设："correctability ≠ confidence"在原子事实声明级别成立且gap足够大以支撑有意义的路由优势**。支撑证据来自两个不同层面的工作——DeepMind的白盒内部表征研究(在TriviaQA/MNLI的问题级别)和Functional Dissociation的SAE研究(在token级别)——但这些发现能否迁移到长文本中的原子事实声明粒度是未经验证的。这是整个proposal成败的关键假设。

2. **假设："Wait"技巧对事实声明效果显著弱于对数学问题"**。这个假设的逻辑链是：数学错误=激活失败→'Wait'有效；事实错误=知识缺口→'Wait'无效。这个论证是合理的，但也是直觉性的。如果'Wait'对事实声明同样有效（>50%），proposal坦言这是"important simplifying finding"，但这会让correctability classifier和SFC的贡献大幅缩水。

3. **假设："声明类型异质性"存在且有意义**。Error Depth Hypothesis在数学中发现错误类型预测可纠正性，但从数学错误类型(计算/设置/逻辑)到事实声明类型(实体/时间/数值/关系)的类比是否成立未经验证。

4. **假设：黑盒行为特征组合能够捕捉足够的correctability信号**。DeepMind论文恰恰显示行为置信度(0.524)远不如内部表征(0.614)，这反而暗示黑盒方法可能存在天花板效应。Proposal预注册的>0.58阈值虽然诚实但也承认了这一天花板。

【3 维度打分】:

1. **Novelty: 中** — 
   Proposal确实识别了一个未被占据的交叉空间：在原子声明级别测量fact-level blind spot + correctability预测 + 纠正路由。搜索确认在SA/CSS/CLC/CURE/CAG/VeriFY等6+篇论文中，没有工作尝试correctability-based correction routing。这个gap是真实的。
   
   但novelty的性质需要审视。这本质上是"将已有概念(blind spot测量)应用于新粒度(原子声明)和新领域(知识密集型任务)"——这是**组合式novelty**而非**概念性novelty**。每个组件——FActScore式分解、self-correction测量、行为特征分类器、选择性路由——都有明确的先行工作。'Wait'转移性测试是一个clean的ablation但更像是sanity check而非创新贡献。Correctability classifier的特征集(自一致性、口头置信度、声明类型、特异性)中，前两个直接来自SelfCheckGPT和CyberCorrect，后两个是SA/CSS启发的。真正新的只有"detection-correction gap"这一个特征和将这些特征用于correctability而非confidence预测的framing。
   
   对于EMNLP而言，组合式novelty如果能产生新的发现是可以接受的，但审稿人可能会认为这是"obvious next step"——在Self-Correction Bench + SA/CURE之后，将blind spot分析扩展到原子事实声明是自然的延伸。

2. **Significance: 中** — 
   研究问题本身是重要的：理解模型何时能/不能自我纠正事实性错误，对于构建可靠的LLM系统有直接实际价值。6+篇论文都走置信度弃权路线而无人走correctability纠正路线，填补这个空白有意义。
   
   但significance受限于两个因素：(a) 如果核心发现是positive（事实声明blind spot高于数学、异质性存在、'Wait'对事实无效），审稿人很可能说"I would have guessed this"——知识缺口导致的错误比激活失败更难纠正，这是大多数研究者的先验直觉。(b) correctability classifier的实际影响取决于AUROC能达到多高。在预注册的"positive"阈值仅>0.58的情况下，SFC相对于trivial confidence-threshold baseline的实际优势可能很小。
   
   最有意义的贡献可能不是下游应用(SFC)，而是benchmark本身和characterization findings——如果blind spot率、claim-type异质性模式、'Wait'转移性等提供了社区目前缺乏的定量理解。但这更接近"measurement paper"的贡献形态。

3. **Related Work: 强** — 
   这是proposal最突出的维度。对领域的覆盖异常全面：Self-Correction Bench、Error Depth、Confidence vs Critique、FactSelfCheck、ConFix、FactCorrector、DeepMind PANL、CyberCorrect、Functional Dissociation、SA、CSS、CLC、CURE、CAG、VeriFY、I-CALM、AtomEval等全部被准确引用和定位。差异化论述清晰且有说服力——"所有现有工作使用置信度/校准，无人做correctability"这个定位经过调研确认是准确的。
   
   唯一瑕疵是arXiv:2605.05957("Knowing but Not Correcting")未能通过搜索验证，该论文被用作"correction suppression"现象的关键论据。如果这篇论文不存在或被不准确描述，会削弱一个支柱性论点（但不是致命的，因为proposal的核心论证不完全依赖于它）。

【概率估计】: [23% - 32%] 中位 27%

【估计理由】: 
Novelty评为"中"是限制上界的主要因素。Proposal的核心贡献是"将blind spot分析从数学/问题级扩展到事实/原子声明级"——这是一个legitimate但组合性质的novelty，审稿人可能视为"obvious next step after Self-Correction Bench + SA/CURE"。预期核心发现（事实声明比数学更难自我纠正、'Wait'效果减弱、异质性存在）大概率会被审稿人判断为"I would have guessed this"，将概率压在35%以下。

Significance评为"中"进一步约束了估计：correctability classifier的预注册阈值(>0.58)诚实但也暴露了天花板问题，SFC的实际增量价值高度依赖correctability-confidence gap在实践中的大小——这是一个未经验证的假设。

Related Work评为"强"提供了下限支撑：即使idea不够surprising，出色的文献覆盖和清晰的定位会让审稿人认可论文的学术严谨性，不太会被拒为"insufficiently novel"到15%以下。

综合而言，这是一篇方向正确、gap真实、但核心发现可能confirmatory而非surprising的measurement+分析论文。在EMNLP这样高标准的venue，27%的中位概率反映了"solid but not exciting"的定位。

【主要风险】: 
1. **"Obvious extension"风险**: 审稿人可能认为"在原子声明级别重复Self-Correction Bench的分析"是自然延伸而非独立贡献，特别是当预期结果大多符合直觉时（事实错误比数学错误更难纠正）。这会直接打击novelty评分。
2. **Correctability classifier天花板风险**: 如果黑盒行为特征无法显著超越简单置信度阈值baseline（DeepMind论文已暗示行为信号的天花板），则proposal最核心的技术贡献(correctability ≠ confidence的实践价值)将被架空，SFC的优势也将不明显。
```


【原始 proposal（允许参考但不是主要依据）】:
# Fact-Level Self-Correction Blind Spot in Knowledge-Intensive Generation: Benchmark, Analysis, and Correctability-Guided Selective Correction

## Description
We propose FactBlind, the first benchmark and analysis framework for measuring the self-correction blind spot at fact-level granularity in knowledge-intensive generation. While the blind spot phenomenon has been characterized for mathematical reasoning at problem level (64.5% average failure rate on GSM8K/PRM800K), and the 'Wait' trick reduces this by 89.3% through an activation mechanism, no work has examined whether these patterns hold for atomic factual claims in long-form text — where errors often stem from genuine knowledge gaps rather than activation failures that prompt tricks can resolve. The recent discovery of correction suppression (19–90% suppression rates when false claims are embedded in task contexts) further suggests the problem in knowledge-intensive generation operates through mechanisms distinct from math. Meanwhile, the selective claim-level handling space has become remarkably crowded — SA, CSS, CLC, CURE (39.9% claim-level accuracy on biography generation), and CAG (VeriScore 67.79%→79.80%) all use confidence/calibration for abstention — while the correctability-based correction paradigm remains entirely unexplored, despite mechanistic evidence that uncertainty and correctness are encoded by functionally distinct feature populations (Functional Dissociation, arXiv:2604.19974). We decompose LLM-generated biographies, QA responses, and report summaries into atomic claims and measure per-claim blind spot rates across 8 models, using both controlled error injection (entity, temporal, numerical, relational) and naturally occurring hallucinations from FActScore-annotated data, with a dedicated 'Wait' ablation testing whether activation-based interventions transfer from math to factual claims. Our central hypothesis — that the blind spot is heterogeneous across claim types and resistant to simple activation prompts — is tested rather than assumed; if 'Wait' proves effective for factual claims, we report this as an important simplifying finding. We then train a black-box behavioral correctability classifier using self-consistency, verbal confidence, claim type, and specificity features, with pre-registered AUROC thresholds (>0.58 positive, >0.63 strong) anchored against DeepMind's white-box baseline (0.614) and behavioral confidence baseline (0.524). Even modest classifier performance reveals the correctability-confidence dissociation, which is itself an important finding given 6+ papers implicitly assume confidence suffices for claim-level routing. Finally, we build Selective Fact Correction (SFC) as a downstream application: claims predicted as correctable undergo ConFix-style bootstrapping while blind-spot claims are flagged for abstention, compared against no-correction, naive self-correction, SA, CURE reference results, confidence-threshold correction, and 'Wait'-augmented self-correction baselines. Unlike SA/CSS/CLC/CURE/CAG which exclusively abstract or suppress, SFC can recover factual accuracy for correctable claims while avoiding destructive correction for uncorrectable ones.

## Core Problem
Self-correction research has characterized the blind spot phenomenon exclusively on mathematical reasoning tasks at problem-level granularity (Self-Correction Bench, 64.5% average blind spot rate across 14 models on GSM8K/PRM800K), and the 'Wait' prompt trick reduces this blind spot by 89.3% — but crucially, this works because math errors are activation failures, not knowledge deficiencies. Yet knowledge-intensive generation (biographies, open-domain QA, report writing) produces outputs containing dozens of heterogeneous atomic claims — entities, temporal facts, numerical values, relations — where errors often stem from genuine knowledge gaps that no activation trick can resolve. Meanwhile, a rapidly growing body of work on selective claim-level handling (Selective Abstraction, CSS, Conformal Linguistic Calibration, CURE, CAG — now 6+ papers) addresses uncertain claims through calibration, abstraction, or hedging, but none attempt to predict whether the model can actually *correct* a specific factual error — a fundamentally different question from whether the claim is uncertain or poorly calibrated, as demonstrated by recent evidence that uncertainty and correctness are encoded by distinct internal feature populations (Functional Dissociation, arXiv:2604.19974). Does the self-correction blind spot manifest differently at fact-level granularity in knowledge-intensive tasks, is it heterogeneous across claim types, can simple activation prompts ('Wait') compensate, and can behavioral correctability estimation enable more effective correction routing than either uniform correction or confidence-based abstraction?

## Opportunity
Five converging lines of work create a clear gap. First, the blind spot literature (Self-Correction Bench arXiv:2507.02778, submitted to ICLR 2026; Error Depth Hypothesis arXiv:2601.00828; Confidence v.s. Critique arXiv:2412.19513) has established that LLMs struggle to correct their own errors, with stronger models making fewer but 'deeper' errors that resist correction — but all measurement is at problem level on math tasks, and the 'Wait' trick's 89.3% blind spot reduction specifically exploits an activation mechanism that may not generalize to factual knowledge errors. Critically, 'Knowing but Not Correcting' (arXiv:2605.05957) discovers correction suppression — models reliably correct false claims in isolation but suppress correction when embedded in task contexts (19–90% suppression rates across 8 models) — demonstrating a complementary blind-spot phenomenon for factual claims that suggests the problem may be even worse in knowledge-intensive generation contexts where task framing is inherent. Second, the fact-level hallucination literature (FactSelfCheck arXiv:2503.17229, 35.5% vs 10.6% factual improvement for fact-level vs sentence-level; ConFix arXiv:2411.13343; FactCorrector arXiv:2601.11232 with the VELI5 benchmark) has demonstrated that fine-grained claim-level analysis dramatically outperforms coarser approaches — but neither studies whether models can correct their OWN factual errors claim-by-claim. Third, DeepMind's recent work (arXiv:2604.22271) shows that internal PANL representations can predict which errors a model can correct (AUROC=0.614 on TriviaQA), and CyberCorrect (arXiv:2605.17305) uses a tri-modal detector combining self-consistency, verbalized confidence, and logic-chain verification for type-directed correction — but both operate at problem level on reasoning/QA tasks, not at atomic-claim level within long-form outputs; CyberCorrect requires reasoning chains and DeepMind requires white-box model access. Moreover, a Functional Dissociation study (arXiv:2604.19974) demonstrates via sparse autoencoders that uncertainty and correctness are encoded by distinct feature populations — suppressing uncertainty features degrades accuracy by up to 10.21% while suppressing incorrectness features produces near-zero change — providing mechanistic evidence that confidence-based routing is fundamentally insufficient for correctability prediction. Fourth, the selective claim-level handling space has become remarkably crowded: Selective Abstraction (arXiv:2602.11908) decomposes responses into atomic claims and replaces uncertain ones with less-specific abstractions (up to 27.73% AURC improvement on FActScore), CSS (arXiv:2604.17487) backs off overcommitted claims, Conformal Linguistic Calibration (arXiv:2502.19110) provides conformal guarantees on claim factuality, CURE (arXiv:2604.12046) teaches models to reason about uncertainty at claim level via a structured &lt;think>→&lt;decompose>→&lt;answer> protocol achieving 39.9% claim-level accuracy improvement on biography generation through calibration and abstention, and CAG (arXiv:2605.01749) decouples exploration from commitment to improve VeriScore from 67.79% to 79.80% — but ALL of these (now 6+ papers) use confidence or calibration as their routing signal and respond to uncertainty through abstraction, suppression, or hedging, NEVER attempting correction. The intersection — measuring the blind spot at fact-level granularity, testing whether activation-based interventions generalize from math to factual claims, predicting correctability (not just confidence) using black-box behavioral signals, and routing claims to correction vs. abstention based on predicted correction success — is unoccupied.

## Landscape
The self-correction blind spot was first quantified by Self-Correction Bench (arXiv:2507.02778, submitted to ICLR 2026), which found 64.5% average failure-to-self-correct across 14 non-reasoning models — but tested only on math tasks (GSM8K, PRM800K, SCLI5) and operates at problem level. Notably, the bench found that appending a minimal 'Wait' prompt reduces the blind spot by 89.3%, and the authors attribute this to correction markers acting as conditioning tokens that shift probability distributions toward self-evaluation sequences — an activation mechanism supported by training-data analysis showing correction markers are concentrated in reasoning datasets (median 30–170 per response) but nearly absent from non-reasoning datasets (95th percentile = 1 marker). This suggests 'Wait' works because math errors are activation failures, not knowledge deficiencies; for factual claims where the model genuinely lacks correct information, activation alone cannot compensate (we test this hypothesis with a 'Wait' ablation in Phase 2). We treat Self-Correction Bench as a useful reference point rather than a definitive field-wide statistic, noting the TACL survey 'When Can LLMs Actually Correct Their Own Mistakes?' (arXiv:2406.01297) provides broader context for when self-correction succeeds or fails. The Error Depth Hypothesis (arXiv:2601.00828) shows that error TYPE predicts correctability in math — stronger models make deeper (setup/logic) errors that resist correction while weaker models make shallower (calculation) errors that are more fixable — suggesting claim-type stratification is a promising direction, though this was only tested on GSM8K with 3 models. Confidence v.s. Critique (arXiv:2412.19513, ACL 2025) decomposes self-correction into confidence and critique capabilities with probabilistic metrics, but operates at problem level.

A newly discovered complementary phenomenon is correction suppression (arXiv:2605.05957): models reliably reject false claims in isolation but comply with those same claims when embedded in task-oriented requests, with suppression rates of 19–90% across 8 models. Mechanistically, the model internally registers the error (hidden-state similarity >0.99) but task context diverts attention, with 'output intent crystallizing toward compliance at middle layers.' This suggests that in knowledge-intensive generation — where task framing is inherent — the blind spot may be compounded by contextual suppression, and that 'Wait'-style activation interventions may be insufficient because the suppression mechanism operates at a deeper level than simple activation failure.

On the fact-level side: FactSelfCheck (arXiv:2503.17229) achieves 35.5% factual improvement via fact-level hallucination detection using knowledge-graph-style triple representation. ConFix (arXiv:2411.13343) demonstrates that high-confidence facts can bootstrap correction of low-confidence facts within the same response without external knowledge. FactCorrector (arXiv:2601.11232) introduces the VELI5 benchmark (17,522 instances with injected factual errors and ground-truth corrections) and a graph-inspired correction pipeline — but relies on external knowledge retrieval via search APIs, achieving 67.4% correction of incorrect atoms with structured feedback. Atomic Calibration (Zhang et al., ACL 2025 KnowFM, arXiv:2410.13246) shows that LLMs exhibit poorer calibration at the atomic level during long-form generation than at response level, providing direct motivation for claim-level analysis.

On correctability prediction: DeepMind's work (arXiv:2604.22271) trains linear probes on post-answer newline (PANL) residual-stream activations that predict correction success (AUROC=0.614), while verbal confidence (0.524) and log-probability (0.531) baselines fail — but requires white-box access and operates at problem level on TriviaQA/MNLI with only Gemma 3 27B and Qwen 2.5 7B. CyberCorrect (arXiv:2605.17305) uses a tri-modal error detector combining self-consistency (weight 0.4), verbalized confidence (0.35), and logic-chain verification (0.25) for type-directed correction on reasoning tasks, achieving 79.8% accuracy with 41% reduction in over-correction — but its logic-chain verification feature requires reasoning chains not present in factual claims, and it operates at reasoning-step level on CyberCorrect-Bench (440 tasks across math/logic/commonsense). Independently, 'Are LLM Uncertainty and Correctness Encoded by the Same Features?' (arXiv:2604.19974) provides mechanistic evidence via sparse autoencoders on Llama-3.1-8B and Gemma-2-9B that uncertainty and correctness are encoded by functionally distinct feature populations: pure uncertainty features are essential for accuracy (suppression causes up to -10.21% accuracy), while pure incorrectness features are statistically significant but functionally inert (suppression yields mean -0.03% change). This directly supports our thesis that confidence-based routing (which tracks uncertainty features) cannot substitute for correctability prediction (which must track correctness-related features). Our behavioral correctability classifier adopts similar self-consistency and confidence signals to CyberCorrect but replaces logic-chain verification with claim-type and specificity features appropriate for factual claims, and critically predicts SELF-CORRECTION success at atomic granularity rather than routing pre-identified errors.

The selective claim-level handling space has become remarkably crowded but addresses a DIFFERENT question from ours. Selective Abstraction (SA; Goren et al., arXiv:2602.11908) decomposes long-form responses into atomic claims, estimates per-claim confidence via verbalized confidence scoring, generates progressively less-specific abstraction sequences, and selects the most specific abstraction satisfying a confidence threshold — achieving up to 27.73% AURC improvement on FActScore across 6 models. Crucially, SA never attempts correction: it exclusively replaces uncertain claims with vaguer versions. CSS (arXiv:2604.17487) similarly backs off overcommitted claims rather than correcting them. Conformal Linguistic Calibration (CLC; Jiang et al., arXiv:2502.19110) provides conformal guarantees on factual accuracy through nested answer-set prediction and progressive claim vaguening — tested on SimpleQA, Natural Questions, and FActScore — but requires fine-tuning (SFT/DPO/ORPO) and also does not attempt correction. CURE (arXiv:2604.12046) operates on the SAME task domain as our work (biography generation, FactBench) and at claim-level granularity: it introduces a Claim-Aware Reasoning Protocol that structures outputs into atomic claims paired with explicit confidence estimates via a &lt;think>→&lt;decompose>→&lt;answer> pipeline, achieving 39.9% claim-level accuracy improvement on Biography and 16.0% AUROC increase on FactBench — but requires multi-stage fine-tuning (SFT + DPO calibration + GRPO factuality optimization on 3–4K prompts) and responds exclusively through calibrated abstention, never attempting correction. CAG (arXiv:2605.01749) proposes an Exploration-Commitment Decoupling paradigm where calibrated reliability estimates filter unreliable reasoning steps before commitment, improving VeriScore from 67.79% to 79.80% across five benchmarks (AlpacaFact, Biography, FactBench, Factory, FAVA) — but also requires fine-tuning (CASS + CAPD stages) and suppresses rather than corrects unreliable claims. VeriFY (arXiv:2602.02018) teaches factual self-verification with abstention through structured verification traces at training time, reducing hallucination by 9.7–53.3% — but requires fine-tuning and operates at response level. I-CALM (arXiv:2604.03904) shows prompt-based abstention can shift error-prone cases to abstention without retraining. Know When You're Wrong (arXiv:2603.06604) aligns confidence with correctness for error detection (AUROC 0.806→0.879 with SFT).

The key distinction: ALL of the above selective-handling methods (now 6+ papers: SA, CSS, CLC, CURE, CAG, VeriFY) use CONFIDENCE or CALIBRATION as their routing signal and respond to uncertainty through ABSTRACTION, SUPPRESSION, or HEDGING. None ask the question central to our work: 'Can this model correct this specific factual error in its own output?' A model may be confidently wrong about a claim (SA/CURE wouldn't touch it) but still able to correct it when prompted; conversely, a model may flag uncertainty about a claim but be unable to produce a correct replacement. Correctability and confidence are related but mechanistically distinct signals — as demonstrated both by DeepMind's finding that behavioral confidence fails to predict correction success (AUROC=0.524 vs. 0.614 for internal representations) and by the Functional Dissociation study showing distinct neural feature populations — and the gap between them, measured at fact level, is our primary object of study.

Concurrent work: AtomEval (arXiv:2604.07967, April 2026) introduces SROM-atom decomposition for adversarial fact verification. CURE (arXiv:2604.12046) and CAG (arXiv:2605.01749) are the closest concurrent works, sharing our task domain and claim-level granularity — but both pursue the confidence-based calibration/abstention paradigm rather than correctability-based correction, making them complementary rather than competing approaches.

## Approach
We build FactBlind, a benchmark and analysis framework for measuring the self-correction blind spot at fact-level granularity in knowledge-intensive generation. The primary contributions are (1) the benchmark and blind spot analysis and (2) the behavioral correctability classifier; the selective correction pipeline is a downstream application demonstrating the practical value of correctability estimation, positioned as a secondary contribution given the now-crowded selective-handling design space.

**Phase 1: Benchmark Construction (3 weeks).** (a) Injected-error track: Generate long-form responses (biographies, open-domain QA, report summaries) from 8 models, decompose into atomic claims using FActScore-style decomposition, then inject controlled factual errors stratified by type — entity swaps (replacing named entities), temporal shifts (date/year perturbations), numerical perturbations (magnitude changes), and relation inversions (swapping subject-object or predicate). We draw methodology inspiration from VELI5 (arXiv:2601.11232) but target intrinsic self-correction measurement rather than external-knowledge correction. We additionally stratify error injection by specificity level (informed by SA's finding that specificity affects reliability) to test whether more specific claims are harder to self-correct. (b) Natural-error track: Evaluate on unmodified LLM-generated biographies using existing FActScore annotations and SAFE/LongFact datasets, where naturally occurring hallucinations serve as ecological ground truth. This dual-track design directly addresses the threat that injected errors may behave differently from natural hallucinations.

**Phase 2: Blind Spot Measurement (3 weeks).** For each atomic claim (both injected and natural errors), measure whether the model can (a) detect the error when presented as external input (external detection), (b) detect it in its own output (self-detection), and (c) correct it in its own output (self-correction). This yields a claim-type-stratified blind spot matrix: BS(model, claim_type) = 1 − P(self-correct | error) / P(external-correct | error). We test 8 models: DeepSeek-V4-Pro, Qwen3.5-27B, Qwen3.5-122B-A10B, Llama-4-Maverick, Llama-3.3-70B-Instruct, Qwen3-32B, Mistral-Small-24B-Instruct, and DeepSeek-V3. The central testable hypothesis is that the blind spot is heterogeneous across claim types — e.g., entity errors may be more detectable/correctable than temporal or relational errors, mirroring the Error Depth Hypothesis's finding that error type predicts correctability in math. A secondary analysis examines whether correction suppression effects (arXiv:2605.05957) manifest in our setting: we compare blind spot rates for claims embedded in full generated responses (task context) vs. claims presented in isolation, testing whether task-oriented framing compounds the blind spot.

**'Wait' Ablation (within Phase 2).** We explicitly test whether Self-Correction Bench's 'Wait' trick transfers to factual claims. For each model, we compare blind spot rates with and without the 'Wait' prompt appended during self-correction. Our hypothesis is that 'Wait' will show substantially diminished effectiveness for factual claims compared to its 89.3% reduction on math, because: (i) factual errors in knowledge-intensive generation often stem from genuine knowledge gaps (entity confusion, outdated temporal facts, relation misattribution) rather than the activation failures that 'Wait' addresses — the model lacks the correct information, not the motivation to correct; (ii) Self-Correction Bench's training-data analysis shows correction markers are concentrated in reasoning datasets (median 30–170 per response) but nearly absent from non-reasoning text (95th percentile = 1), suggesting 'Wait' may lack the conditioning effect for factual correction sequences; (iii) correction suppression (arXiv:2605.05957) demonstrates that even when models possess the knowledge, task context diverts attention at a deeper mechanistic level than simple activation failure — hidden-state similarity >0.99 indicates the model registers the error but suppresses correction. If 'Wait' proves effective for factual claims (>50% blind spot reduction), this would be an important positive finding that simplifies the problem — we would report it prominently and reframe the correctability classifier as addressing the remaining residual blind spot.

**Phase 3: Behavioral Correctability Classifier (2 weeks).** Train a lightweight classifier that predicts, for each atomic claim in a new response, whether self-correction will succeed or fail. Unlike the PANL-based approach (arXiv:2604.22271) which requires white-box access to residual-stream activations, and unlike CyberCorrect (arXiv:2605.17305) whose tri-modal detector uses logic-chain verification suited only to reasoning tasks, our classifier uses black-box behavioral features appropriate for factual claims in long-form text: (i) multi-sample self-consistency score (SelfCheckGPT-style), (ii) verbal confidence when asked to rate claim certainty, (iii) claim type (entity/temporal/numerical/relational), (iv) claim specificity (more specific claims may be harder to correct, informed by SA/CSS findings), (v) detection-correction gap (whether the model flags the claim as uncertain but fails to correct it — measuring the gap between the blind-spot-as-detection-failure and blind-spot-as-correction-failure). The classifier explicitly targets CORRECTABILITY, not confidence — a distinction supported by three independent findings: DeepMind's result that behavioral confidence signals (AUROC=0.524) fail to predict correction success even when internal representations succeed (AUROC=0.614); the Functional Dissociation study (arXiv:2604.19974) showing uncertainty and correctness are encoded by distinct feature populations in Llama-3.1-8B and Gemma-2-9B; and the existence of 6+ papers (SA, CSS, CLC, CURE, CAG, VeriFY) that achieve strong calibration without enabling correction.

**Pre-registered AUROC expectations.** We anchor expectations against known baselines: DeepMind's white-box PANL probes achieve AUROC=0.614 for correction prediction, while their behavioral confidence baseline achieves only 0.524. Black-box hallucination DETECTION (a strictly easier task than correctability prediction) achieves AUROC 0.75–0.82 with self-consistency methods (SelfCheckGPT). We pre-register: AUROC > 0.58 constitutes a positive result, demonstrating that claim-type and specificity features add meaningful signal beyond confidence alone for correctability prediction (significantly beating the 0.524 behavioral confidence baseline). AUROC > 0.63 constitutes a strong result, approaching DeepMind's white-box performance (0.614) without requiring model internals. If AUROC falls in the 0.55–0.58 range, the classifier contribution is acknowledged as modest, but the correctability-confidence dissociation analysis (comparing classifier features' predictive power for correctability vs. confidence) remains an important finding — demonstrating that even when correctability is hard to predict, it is not the same signal as confidence. If the heterogeneous-blind-spot hypothesis does not hold (i.e., the blind spot is roughly uniform across claim types), the classifier reduces to a uniform threshold policy — in this case, the benchmark itself, the natural-vs-injected comparison, the 'Wait' ablation results, and the characterization of confidence-vs-correctability dissociation remain the primary contributions, and we report the negative result as informative for the field.

**Phase 4: Correctability-Guided Selective Fact Correction (2 weeks).** Implement SFC, which routes each claim through the correctability classifier. The key distinction from existing selective-handling approaches: SA (arXiv:2602.11908), CSS (arXiv:2604.17487), CLC (arXiv:2502.19110), CURE (arXiv:2604.12046), and CAG (arXiv:2605.01749) all use CONFIDENCE or CALIBRATION as the routing signal and respond to uncertainty through ABSTRACTION, SUPPRESSION, or HEDGING. SFC uses CORRECTABILITY as the routing signal and responds differently based on predicted correction success: claims predicted as correctable undergo ConFix-style intra-response confidence bootstrapping (attempting actual factual correction); claims in the predicted blind spot are flagged for abstention (marked as uncertain) or left unchanged to avoid destructive correction. This means SFC can handle cases that SA/CURE miss (confidently wrong but correctable claims) and avoids cases where SA over-abstracts (uncertain but actually correct claims that SA would unnecessarily vaguify). Compare against: (a) no correction baseline, (b) full naive self-correction (ask model to correct everything), (c) Selective Abstraction (SA) — confidence-based abstraction baseline operating on the same atomic claims, (d) CURE reference comparison — using CURE's published results on Biography/FactBench as reference points for the calibration-with-fine-tuning paradigm (noting CURE requires multi-stage fine-tuning while SFC is inference-time), (e) FactCorrector-style external-knowledge correction as an oracle upper bound, (f) random selective correction, (g) confidence-threshold selective correction (applying SA's confidence signal but with correction instead of abstraction, to isolate the correctability vs. confidence distinction), (h) 'Wait'-augmented self-correction (applying the 'Wait' trick globally, to isolate whether activation-based intervention subsumes our approach). Evaluate using FActScore and SAFE metrics, plus an information-retention metric (following SA's information-theoretic measure) to ensure SFC preserves more content than abstraction-only approaches.

## Resource Estimate
{'manual': {'gpu_hours': "750-1100 (inference-only: 8 models × 3 datasets × multi-sample generation + correction passes; natural-error track adds ~20% overhead for multi-sample consistency; SA baseline replication adds ~10%; 'Wait' ablation adds ~15%; on 4×A100 node)", 'timeline': "13-16 weeks (3 weeks benchmark construction including natural-error track, 3 weeks blind spot measurement including suppression analysis and 'Wait' ablation, 2 weeks correctability classifier, 2 weeks SFC pipeline + SA/CURE baseline comparison, 3-4 weeks writing and ablations)", 'estimated_gpu_cost': '$1125-$1650 at ~$1.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': "550-850 (Claude handles decomposition, error injection templates, multi-sample generation orchestration, SA baseline replication, 'Wait' ablation orchestration, and result analysis; human steers experiment design and interprets blind spot patterns)", 'timeline': "9-12 weeks (2.5 weeks benchmark with Claude-assisted decomposition + natural-error curation, 2.5 weeks measurement including 'Wait' ablation, 1.5 weeks classifier, 1.5 weeks SFC + baselines, 2-3 weeks writing)", 'claude_api_cost': '$500-$800 (atomic decomposition of ~12K responses × ~10 claims each via Sonnet 4.6; error injection generation; correctability annotation; paper drafting)', 'estimated_gpu_cost': '$825-$1275'}, 'auto_research': {'gpu_hours': "450-700 (automated sweep over models, claim types, 'Wait' ablation, and ablations)", 'timeline': "7-9 weeks (2 weeks benchmark auto-construction + natural-error curation, 2 weeks parallel blind spot sweeps + 'Wait' ablation, 1.5 weeks classifier training + SFC + SA baseline, 1.5-2 weeks writing)", 'claude_api_cost': '$900-$1400 (heavier API use for automated claim decomposition, error injection, multi-sample consistency scoring, experiment orchestration, and iterative analysis)', 'estimated_gpu_cost': '$675-$1050', 'speed_bottleneck': "Sequential model inference for blind spot measurement — each model must generate, then attempt correction (with and without 'Wait'), for thousands of claims; parallelizable across models but not within a single model's correction chain. Natural-error track requires multi-sample generation for consistency scoring."}}

## Inspired By
Combination of blind spot phenomenon (Self-Correction Bench) + the 'Wait' trick's 89.3% blind spot reduction on math raising the question of whether activation-based interventions transfer to factual knowledge tasks + Error Depth Hypothesis (error type predicts correctability in math) + correction suppression discovery (arXiv:2605.05957, showing task context suppresses factual correction 19-90%, which may compound the blind spot in knowledge-intensive generation) + fact-level confidence calibration (ConFix) + FactSelfCheck granularity results + DeepMind PANL correctability prediction (showing the signal exists but hasn't been studied at fact level or with black-box methods) + CyberCorrect's tri-modal detector features (self-consistency + confidence + error type for correction routing, but only on reasoning tasks) + Selective Abstraction's demonstration that atom-wise handling works at scale on FActScore (but abstracts rather than corrects) + CURE's claim-level calibration on biography generation (arXiv:2604.12046, achieving 39.9% accuracy improvement but never attempting correction) + CAG's exploration-commitment decoupling (arXiv:2605.01749, improving VeriScore but suppressing rather than correcting) + Functional Dissociation finding that uncertainty and correctness are encoded by distinct feature populations (arXiv:2604.19974); TACL survey finding that self-correction conditions are poorly understood outside reasoning tasks; the observation that FactCorrector achieves 67.4% atom correction WITH external knowledge but no one has measured intrinsic self-correction rates at atom level; Atomic Calibration's finding that LLMs show poorer calibration at atomic level in long-form generation; the emerging pattern that 6+ papers now pursue confidence-based claim-level abstention while zero papers pursue correctability-based claim-level correction.

## Target Venues
- AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026 — tight but feasible with auto_research timeline)
- EACL 2027 via ARR (submission: August 3, 2026; commitment: October 11, 2026)
- ICLR 2027 (expected submission: ~September-October 2026, dates TBA)
- NAACL 2027 via ARR (submission: ~October 2026; commitment: ~October 16, 2026)
- TACL (rolling monthly deadlines, any month 2026)

## Key References
- FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (Min et al., EMNLP 2023)
- SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models (Manakul et al., EMNLP 2023)
- Chain-of-Verification Reduces Hallucination in Large Language Models (Dhuliawala et al., arXiv 2023)
- Long-form Factuality in Large Language Models — SAFE (Wei et al., arXiv 2024, arXiv:2403.18802)
- Atomic Self-Consistency for Better Long Form Generations (Agrawal et al., EMNLP 2024)
- Fact-Level Confidence Calibration and Self-Correction — ConFix (arXiv:2411.13343, 2024)
- Atomic Calibration of LLMs in Long-Form Generations (Zhang et al., ACL 2025 KnowFM / AACL-IJCNLP 2025, arXiv:2410.13246)
- Confidence v.s. Critique: A Decomposition of Self-Correction Capability for LLMs (Yang et al., ACL 2025, arXiv:2412.19513)
- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models (submitted to ICLR 2026, arXiv:2507.02778)
- FactSelfCheck: Fact-Level Black-Box Hallucination Detection for LLMs (arXiv:2503.17229, 2025)
- The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input (arXiv:2501.03200, 2025)
- Know Your Limits: A Survey of Abstention in Large Language Models (arXiv 2025)
- Enhancing LLM Reliability via Explicit Knowledge Boundary Modeling (arXiv 2025)
- When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs (Kamoi et al., TACL 2025, arXiv:2406.01297)
- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis (arXiv:2601.00828, Jan 2026)
- FactCorrector: A Graph-Inspired Approach to Long-Form Factuality Correction + VELI5 Benchmark (arXiv:2601.11232, Jan 2026)
- Conformal Linguistic Calibration: Trading-off between Factuality and Specificity (Jiang et al., arXiv:2502.19110, Feb 2026)
- When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (Goren et al., arXiv:2602.11908, Feb 2026)
- VeriFY: Learning Factual Self-Verification for Hallucination Reduction (arXiv:2602.02018, Feb 2026)
- Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv:2603.06604, Mar 2026)
- Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration — CURE (arXiv:2604.12046, Apr 2026)
- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (Kumaran et al., DeepMind, arXiv:2604.22271, Apr 2026)
- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, Apr 2026)
- I-CALM: Incentivizing Confidence-Aware Abstention for LLM Hallucination Mitigation (arXiv:2604.03904, Apr 2026)
- Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control — CSS (arXiv:2604.17487, Apr 2026)
- AtomEval: SROM-atom Decomposition for Adversarial Fact Verification (arXiv:2604.07967, Apr 2026)
- Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality — CAG (arXiv:2605.01749, May 2026)
- Knowing but Not Correcting: Routine Task Requests Suppress Factual Correction in LLMs (Chen et al., arXiv:2605.05957, May 2026)
- CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models (Wu et al., arXiv:2605.17305, May 2026)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3b5ac6f6-4b46-4a0a-8c9d-b0a076b73731",
  "type": "user",
  "uuid": "3333c2f4-3225-431a-be06-35758abc1466",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:56:05.744Z_

```json
{
  "parentUuid": "3333c2f4-3225-431a-be06-35758abc1466",
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
  "uuid": "00083f1f-e6e8-4a16-ba37-5fe781b4ca37",
  "timestamp": "2026-05-20T05:56:05.744Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:56:05.744Z_

```json
{
  "parentUuid": "00083f1f-e6e8-4a16-ba37-5fe781b4ca37",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "48ca1c31-74bb-467a-b4a1-83304672dde7",
  "timestamp": "2026-05-20T05:56:05.744Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36",
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
  "leafUuid": "48ca1c31-74bb-467a-b4a1-83304672dde7",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate fact-level self-correction blind spot proposal",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:56:43.706Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three reviewer assessments and synthesize them into a Meta Judge evaluation.

Let me first extract the key data points:

**Reviewer 1:**
- Novelty: 中偏强 (Medium-Strong)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability: [28% - 38%] 中位 33%
- Main risks: "Natural extension" novelty ceiling; Correctability classifier black-box performance ceiling


**Reviewer 2:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability: [25% - 35%] 中位 29%
- Main risks: "Expected findings" risk; Correctability classifier ceiling too low

**Reviewer 3:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [23% - 32%] 中位 27%
- Main risks: "Obvious extension" risk; Correctability classifier ceiling

Now I'm calculating the aggregate statistics from the three probability estimates. The median comes to 29%, with a mean around 29.67% and a standard deviation of approximately 2.49%, showing fairly tight clustering around the central estimate. Now I'm classifying the overall consistency as medium since the sample standard deviation sits right at the boundary. Looking at where the reviewers align, novelty shows medium consensus with one reviewer leaning slightly stronger, related work has full agreement, and significance clusters around medium-to-strong with one dissenting voice. Across all three reviewers, I'm noticing they consistently flag the same core concerns: the work reads as a natural extension rather than a novel contribution, the correctability classifier has inherent limitations, and there are trivial alternative approaches they all mention.

The weakest points emerge as expected confirmatory findings and the behavioral features hypothesis, which all three reviewers identify as problematic. Some critiques are unique—one reviewer references a missing benchmark paper, another couldn't verify a citation while the other two confirmed it, and one reviewer makes the sharpest observation about oversimplifying the distinction between math errors and factual errors. With three midpoint estimates clustering tightly between 27-33% and that narrow standard deviation, I'm working toward a final assessment.

The median sits at 29%, and given this medium consistency level, I should weight the stricter estimates more heavily. The consensus on novelty being medium rather than medium-strong, plus the agreement on strong related work, guides my calibration. For significance, there's a 2-1 split favoring medium-strong, so I'm settling on a range of 28-29% as my final estimate.

Now I'm examining the implementation feasibility—the compute requirements are modest at 450-1100 GPU hours on A100s since this is inference-only work, and the datasets plus models are all publicly available. The human effort is moderate, mainly in experiment design and interpretation, though there's some uncertainty around the classifier's performance ceiling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48ca1c31-74bb-467a-b4a1-83304672dde7",
  "isSidechain": false,
  "requestId": "req_011CbDJePsTtvcE7hMQQfHqZ",
  "type": "assistant",
  "uuid": "9b07689d-64a8-4965-a77a-0c2432cb2af3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132TeMtEgHDV6U5ttvZJc8X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23812,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3854,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 23812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23812
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

_source line 9 · 2026-05-20T05:57:35.584Z_

【阶段】: Meta Judge
【三次中位】: [33%, 29%, 27%]  std=3.1%
【共识维度】:
- **Novelty = 中**（R2、R3 均判"中"；R1 判"中偏强"为 outlier 偏高）：三人均指出核心贡献属于 "extension/combination" 型 novelty——将已有概念（blind spot 测量、correctability prediction）推广到新粒度（atomic claim）和新域（knowledge-intensive generation），而非发现新机制或反直觉现象。三人均认为预期核心发现方向符合研究者先验直觉（"I would have guessed this"）。**这是压低概率上界的主要共识因素。**
- **Related Work = 强**（三人一致）：文献覆盖极其全面（25-30+ 篇，含 2026 年 5 月最新工作），差异化定位清晰准确，所有引用经核实真实存在且描述准确。三人均认为这是 proposal 最突出的优势。
- **Significance = 中偏强**（R1、R2 判"中偏强"；R3 判"中"为 outlier 偏低）：研究问题重要性得到认可（6+ 篇并发论文证明赛道热度），benchmark 有基础设施价值，但 SFC pipeline 的 practical impact 高度依赖 classifier 性能。
- **Correctability classifier 黑盒天花板**（三人一致风险点）：DeepMind 已证明 behavioral confidence AUROC 仅 0.524，proposal 加入 claim type + specificity 等特征能否显著提升是核心不确定性。三人均认为如果 AUROC 仅 0.55-0.58，Phase 3-4 贡献大幅缩水。
- **Trivial alternative 威胁**（三人一致）：confidence-threshold correction 和 "Wait" 直接迁移均被识别为真实威胁。Proposal 已将两者纳入 baseline/ablation，但增量价值 conditional on empirical results。
- **"Expected findings" 风险**（三人一致）：核心预测（blind spot 在 facts 上存在/更严重、"Wait" 效果减弱、claim type 异质性）均为研究者会预期的方向，缺乏 "aha moment"。

【异常维度】:
- R1 指出缺少 CorrectBench (arXiv:2510.16062) 引用——仅 R1 提及，降权处理（不影响总体判断，但可作为完善建议）
- R3 未能搜索验证 arXiv:2605.05957——但 R1 和 R2 均确认该论文存在且描述准确，判定 R3 搜索失败为假阴性，不影响评估
- R2 对 "math errors = activation failures vs. factual errors = knowledge gaps" 二分法的批评最为尖锐——R1/R3 也注意到但措辞温和；R2 的批评有道理但 proposal 将此设计为可测试假设而非预设前提，威胁可控

【最终概率】: [24% - 34%] 中位 29%
【一致性】: 中（std=3.1%，刚超过 3% 阈值；三人 rubric 判决高度一致但数值略有分散）
【综合理由】:

三位审稿人在核心判断上高度一致：这是一个 **gap 真实、定位精准、执行设计成熟，但核心 novelty 属于 "natural extension" 而非 "surprising discovery" 的 proposal**。

**概率上界受限于 Novelty（中）**：三人共识认为将 blind spot 从 math/problem-level 推广到 fact/claim-level 是 "obvious next step"，预期核心发现方向符合直觉。R1 给出的"中偏强"是三人中最宽松的判断，但其理由（"精准空白定位"和"dual-outcome 设计"）更多反映执行质量而非 idea 本身的 surprise factor。综合后 Novelty 锚定在"中"，这将概率天花板限制在 ~35%。

**概率下界由 Related Work（强）和 Significance（中偏强）支撑**：出色的文献覆盖和清晰定位确保论文不会被判为 "insufficiently novel" 到 20% 以下；研究问题的实际重要性和 benchmark 基础设施价值提供额外支撑。

**中位取 29% 而非更高的理由**：(1) 三人一致识别的 classifier 天花板风险——如果 Phase 3-4 贡献缩水，论文退化为 benchmark/measurement paper，在 EMNLP 竞争力进一步下降；(2) trivial alternative 威胁真实——如果 confidence-threshold correction 或 "Wait" ablation 结果削弱了 correctability routing 的增量价值，核心 narrative 受损；(3) "expected findings" 风险——confirmatory 结果在顶会中的竞争力弱于 surprising 发现。

**未采纳 R1 的较高估计（33%）**：R1 的 Novelty 判断"中偏强"与 R2/R3 的"中"形成 1:2 分歧，按"宁缺毋滥"原则偏向更严格判断。R1 强调的 "dual-outcome 设计" 和 "pre-registered thresholds" 确实是方法论亮点，但属于执行质量而非 idea 质量加分，不改变 novelty 天花板。

【建议】: 边缘（中位 29% 处于 borderline 区域，有通过迭代优化提升至 36%+ 的可能性，但需要 idea 层面的强化而非仅靠实验完善）

【实施评估】:
- **计算资源**: 450-1100 GPU-hours（A100），以推理为主（8 模型 × 3 数据集 × 多轮 generation + correction + Wait ablation + multi-sample consistency），无大规模训练需求。预估 GPU 成本 $675-$1650（A100 spot pricing）。4×A100 节点可在合理时间内完成。资源门槛**中低**。
- **数据需求**: FActScore 已标注数据、SAFE/LongFact 数据集（均公开可得）；自建注入错误数据集需要 FActScore-style 原子分解（可用 API 自动化）。数据门槛**低**。
- **人工介入**: 实验设计与 blind spot pattern 解读需要研究者判断；原子分解和错误注入可高度自动化（Claude API）；benchmark 质量控制需要抽样人工审核。人工介入量**中等**。
- **训练需求**: 仅需训练轻量级 correctability classifier（logistic regression / 小型 MLP），无 LLM 微调。训练门槛**极低**。
- **新 Benchmark**: 是——FactBlind benchmark 是核心贡献之一，包含注入错误轨道和自然错误轨道，需要系统构建和质量验证。
- **预估周期**: 7-16 周（取决于自动化程度），auto_research 模式下 7-9 周可完成实验，加写作约 9-12 周。若目标 EMNLP 2026 主会（ARR 提交截止通常在 6-8 月），时间可行但偏紧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b07689d-64a8-4965-a77a-0c2432cb2af3",
  "isSidechain": false,
  "requestId": "req_011CbDJePsTtvcE7hMQQfHqZ",
  "type": "assistant",
  "uuid": "9a2d28ec-4a9b-4372-989d-6673f948ca34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132TeMtEgHDV6U5ttvZJc8X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23812,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3854,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3854,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 23812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23812
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
  "leafUuid": "9a2d28ec-4a9b-4372-989d-6673f948ca34",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate fact-level self-correction blind spot proposal",
  "sessionId": "83657097-a827-4c8b-b603-51ef6353df36"
}
```

---
