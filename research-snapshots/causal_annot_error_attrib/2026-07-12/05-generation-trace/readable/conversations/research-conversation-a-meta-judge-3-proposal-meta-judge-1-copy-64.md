# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/39641383-8072-41e0-abe9-cd597001473b.jsonl`
- **Structured JSON:** [`d7de2b5ad87a984c94a7.json`](../../sessions/d7/d7de2b5ad87a984c94a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T19:03:19.152Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T19:03:19.152Z",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have enough information. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 【致命前置问题：投稿会议不匹配】\nCoRL (Conference on Robot Learning) 2026 官网明确声明：\n\"Submissions without a robotics focus will be returned without review.\"\n本 proposal 的内容（LLM 内部表征探针、自我纠错门控、SAE 特征分解）100% 是纯 NLP/ML 机制研究，\n与机器人学习完全无关。无论 idea 质量如何，投稿 CoRL 将被直接 desk reject，概率为 0%。\n适合的会议：NeurIPS / ICML / ICLR / ACL / EMNLP。\n以下评估基于假设投稿到合适的 ML/NLP 主会（如 NeurIPS 2026），以评价 idea 本身的质量。\n\n【领域调研】:\n- [arXiv:2604.22271] \"How LLMs Detect and Correct Their Own Errors\" (2026):\n  建立了 PANL (Post-Answer NewLine) correctability 信号的概念，单层线性探针在 own-generated errors 上达到 0.614 AUROC。\n  这是本 proposal 最直接的前序工作——本 proposal 本质上是在这篇论文的基础上做\"探针方法升级\"。\n\n- [arXiv:2604.13386] \"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\" (2026):\n  多层集成探针在欺骗检测上将 AUROC 从 0.510 提升到 0.910（+78%）。\n  但该结果特定于 deception detection，是否可迁移到 correctability 是未验证假设。\n\n- [arXiv:2604.19974] \"Are LLM Uncertainty and Correctness Encoded by the Same Features?\" (2026):\n  用 SAE 分解出 pure uncertainty / pure incorrectness / confounded 三类特征，发现 68% 的 pure incorrectness 特征因果无效。\n  proposal 将其引入 correctability 分析是合理的延伸，但属于\"应用已有框架到新场景\"。\n\n- [arXiv:2602.08948] \"CoRefine\" (2026):\n  已实现三路路由（halt/rethink/alternative），用 211K 参数 Conv1D 控制器在 output-level confidence 上运作，92.6% halt precision。\n  proposal 的核心差异化点是用 hidden-state 探针替代 output-level confidence + 加入 genuine abstention。\n\n- [arXiv:2512.20578] \"Gnosis\" (2025):\n  多信号融合在 correctness prediction 上达到 0.80–0.95 AUROC。\n  proposal 的多信号探针设计（多层+多 token+attention 熵）与 Gnosis 的方法论高度相似，只是目标从 correctness 切换到 correctability。\n\n- [arXiv:2504.05419] \"Reasoning Models Know When They're Right\" (2025):\n  用 hidden-state 探针做 early exit，AUROC 0.77–0.91（针对 correctness）。\n\n- [arXiv:2602.08159] \"The Confidence Manifold\" (2026):\n  correctness 仅需 3-8 维、25 个样本即可线性分离。Proposal 想测试 correctability 是否也有类似结构。\n\n- 调研总结: correctability prediction 作为一个 distinct target（区分于 correctness/error detection）是由 PANL 论文刚刚建立的概念（2026年4月）。\n  本 proposal 的定位是\"用更强的探针方法论提升 correctability AUROC + 将其用于三路门控\"。\n  核心方法论组件（多层集成、多 token、attention 熵、SAE 引导）均来自已有工作，proposal 的贡献主要在于\"组合 + 应用到新目标\"。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁：\n1. CoRefine 的 output-level confidence 已经实现了 92.6% halt precision 的三路路由。\n   Proposal 需要证明 hidden-state 探针比 output-level confidence 好多少——如果提升有限（如 2-3 个 AUROC 点），\n   那付出的额外复杂度（多层提取、SAE 训练、探针训练）是否值得？\n2. 简单的 confidence thresholding（如 Reflective Confidence 的 logprob 阈值方法）在 AIME 2025 上达到 83.3%。\n3. 核心问题：如果 correctability 作为一个内部信号本身就很弱（PANL 论文显示只有 0.614），\n   那更好的探针可能只是从 0.614 提升到 0.70-0.75——这个增量是否足以让 probe-gated correction 真正优于简单 confidence baseline？\n   Proposal 自己也承认 \"whether similar gains transfer... is an open empirical question\"。\n\n增量价值在于：如果能证明 hidden-state probes 确实能可靠区分 correctable vs. uncorrectable errors（而 output-level confidence 不能），\n这在理论上有意义。但这个 \"如果\" 本身就是最大的不确定性。\n\n【前提假设检验】:\n核心 claim 的逻辑链中有几个未验证的关键假设：\n\n1. **\"correctability 是可被探针捕获的信号\"假设**：PANL 论文的 0.614 AUROC 仅略高于随机（0.5）。\n   这可能意味着 correctability 根本就不是一个在 hidden states 中有强编码的属性——\n   也许模型内部根本没有\"我能纠正这个错误\"的稳定表征。\n   Proposal 假设 0.614 是因为探针方法太弱，但另一个同样合理的解释是：信号本身就很弱。\n\n2. **\"多层集成从 deception 迁移到 correctability\"假设**：deception detection 和 correctability 是根本不同的任务。\n   Deception 有明确的\"模型知道真相但选择说谎\"的编码模式；\n   correctability 则取决于模型的知识覆盖、推理路径可达性等更复杂的因素。\n   Proposal 用 Phase 0 测试这个假设是好的实验设计，但如果结果是 negative，\n   整个 Phase 1 的方法论基础就塌了。\n\n3. **\"confounded features 是 correctability 的有效基底\"假设**：\n   arXiv:2604.19974 的 confounded features 发现是关于 uncertainty × correctness 的关系，\n   而 correctability 是一个更高阶的概念（涉及纠错机制的可达性）。\n   从\"uncertainty-correctness confounded features\"到\"correctability prediction\"的跳跃缺乏理论支撑。\n\n4. **\"genuine abstention 优于 CoRefine 的 ALTERNATIVE\"假设**：\n   在实际应用中，\"尝试另一种方法\"（CoRefine 的 ALTERNATIVE）可能比\"直接放弃\"（abstention）更有价值。\n   Proposal 预设 abstention 是更好的策略，但这取决于具体应用场景。\n\n【3 维度打分】:\n\n1. Novelty: 弱-中 —\n   - 核心概念\"correctability as distinct from correctness\"已由 PANL 论文（2604.22271）建立\n   - 探针方法论的每个组件都是从已有工作借鉴：多层集成（2604.13386）、attention 熵（2602.13699）、SAE 引导（2604.19974）、多 token（PANL 论文自己的 causal analysis）\n   - 三路门控已由 CoRefine（2602.08948）实现，差异在于信号源（hidden-state vs. output-level）和 abstention\n   - 真正的 novelty delta 在于\"组合这些技术应用于 correctability + SAE 分解分析 correctability 的表征结构\"——这是一个有效但较薄的 novelty\n   - Phase 3b 的 representational geometry 分析如果做好可以是不错的贡献，但本质上仍然是\"将已有分析框架应用到新目标\"\n\n2. Significance: 中 —\n   - 研究问题本身有意义：理解哪些错误可以被自我纠正是 LLM 部署中的真实需求\n   - 但实际影响力受限于：(a) 如果信号本身就弱，实际可部署性很低；(b) 需要多层 hidden state 提取的方案在实际推理中成本很高；(c) 纯 confidence-based 方法已经相当有效\n   - Phase 3b 的表征分析可能有较好的科学贡献（理解 second-order properties 的编码方式），但其影响力取决于发现是否 surprising\n   - 如果核心发现是 \"correctability 需要更高维度/非线性边界\"，审稿人可能会说 \"I would have guessed this\"——因为更高阶的属性需要更复杂的表征是直觉上预期的\n\n3. Related Work: 强 —\n   - 相关工作覆盖非常全面，差异化定位清晰\n   - 与 CoRefine 的三重区分（信号源、abstention、correctability-aware）描述准确\n   - 对每篇引用工作的局限性分析到位（如 Gnosis 的 ablation 仅在 Qwen3-1.7B 上、多层集成的 deception-specific 性质）\n   - 唯一的小问题：对四篇 concurrent probe-gating 论文的总结有点快速，可以更深入地分析与本工作的区别\n\n【概率估计】: [15% - 30%] 中位 22%\n（注意：此概率是假设投稿到 NeurIPS/ICML 等合适会议。投稿 CoRL 的概率为 ~0%，会被 desk reject。）\n\n【估计理由】:\n- Novelty 维度限制了上界：核心是\"已有探针技术的组合应用于一个刚被提出的新目标\"，审稿人可能会评价为 incremental combination\n- Significance 处于中等：研究问题有价值，但核心发现（无论 positive 还是 negative）不太可能是 surprising。如果探针提升到 0.75 AUROC，审稿人可能说 \"expected improvement from better probing\"；如果 plateau 在 0.65，Phase 3b 的表征分析虽有趣但 impact 有限\n- Related Work 是该 proposal 最强的维度，但好的 related work 覆盖不能弥补 novelty 的不足\n- Proposal 过于 kitchen-sink：4 个 phase + 6 种探针变体 + 8 个 baseline + SAE 分析 + 表征几何 + error depth，试图在一篇论文中做太多事情，这本身可能被审稿人视为缺乏聚焦\n- \"Robust to negative results\" 设计虽然是好的学术实践，但也暗示作者自己对核心 claim 的信心不足\n\n【主要风险】:\n1. **信号天花板风险**：correctability 可能在 hidden states 中根本就没有强编码——0.614 AUROC 可能不是探针方法的问题，而是信号本身的问题。如果增强探针只能把 AUROC 提到 0.68-0.72，整个 gating 框架的实用价值存疑，论文会变成\"我们用了很多技术但提升有限\"的 negative result + 分析论文\n2. **Novelty 薄弱风险**：审稿人可能认为这是\"将一堆已有的探针改进技术套用到一个新定义的预测目标上\"——方法层面无新意，目标层面由 PANL 论文已经定义，组合本身不构成充分的 novelty\n\n⚠️ 再次强调：如果目标确实是 CoRL 2026，请立即更换投稿会议。这个 proposal 与 robot learning 完全无关，会被 desk reject。\n```\n\nSources:\n- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)\n- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)\n- [Are LLM Uncertainty and Correctness Encoded by the Same Features? (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)\n- [CoRefine: Confidence-Guided Self-Refinement (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Reasoning Models Know When They're Right (arXiv:2504.05419)](https://arxiv.org/html/2504.05419v1)\n- [Can LLMs Predict Their Own Failures? Gnosis (arXiv:2512.20578)](https://arxiv.org/pdf/2512.20578)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to evaluate this proposal. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n```\n\n## ⚠️ 关键前置问题：严重的会议选择错位\n\n在进入 idea 质量评估之前，必须先指出一个**致命的会议选择问题**：\n\n**CoRL (Conference on Robot Learning) 是机器人学习会议**，其 Call for Papers 明确要求论文聚焦于 \"core robotics problem\"，主题包括机器人感知、控制、操作、导航、运动等。本 proposal 完全关于 **LLM 内部表示的可纠正性探测与自纠错门控**，与机器人学习零关联。投稿 CoRL 极大概率会被 **desk reject**。\n\n合适的目标会议应为：**EMNLP 2026, ACL 2026, NeurIPS 2026, ICLR 2027, 或 COLM 2026**。\n\n以下评估基于 idea 本身的质量，假设投稿到合适的 NLP/ML 会议。\n\n---\n\n```\n【领域调研】:\n\n1. [How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals] (arXiv:2604.22271, 2026):\n   - 这是本 proposal 的直接前驱。建立 PANL (post-answer newline token) 信号，错误检测 AUROC 0.986 但可纠正性预测仅 0.614。\n   - 关系：proposal 的核心起点，试图改进 0.614 的基线。\n\n2. [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling] (arXiv:2604.13386, 2026):\n   - 多层集成在欺骗检测上将 AUROC 从 0.510 提升至 0.910 (+78%)。\n   - 关系：proposal 的核心技术借鉴源。但该工作针对的是欺骗检测，与可纠正性是截然不同的任务，迁移性是开放问题。\n\n3. [Are LLM Uncertainty and Correctness Encoded by the Same Features?] (arXiv:2604.19974, 2026):\n   - SAE 分解显示不确定性与正确性由功能性分离的特征群编码；68% 纯错误特征因果惰性；仅 102 个混合特征有效。\n   - 关系：proposal 的 SAE 引导探针设计和 Phase 3b 分析的理论基础。\n\n4. [Can LLMs Predict Their Own Failures? — Gnosis] (arXiv:2512.20578, 2025):\n   - 多信号融合（隐状态+注意力）实现正确性预测 AUROC 0.80-0.95，~5M 参数。\n   - 关系：proposal 的多信号探针设计与 Gnosis 在技术路线上高度相似，但 target 不同（正确性 vs 可纠正性）。\n\n5. [CoRefine: Confidence-Guided Self-Refinement] (arXiv:2602.08948, 2026):\n   - 基于输出层置信度的三路路由（halt/rethink/alternative），92.6% halt 精度，~190× token 缩减。\n   - 关系：最直接的系统级竞争者。proposal 的区分点在于使用隐状态探针而非输出置信度，以及\"可纠正性感知\"和真正的 abstention。\n\n6. [Reasoning Models Know When They're Right] (arXiv:2504.05419, 2025):\n   - 隐状态探针用于推理正确性验证和提前退出，AUROC 0.77-0.91。\n   - 关系：相邻工作，目标是正确性而非可纠正性。\n\n7. [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox] (arXiv:2601.00828, 2026):\n   - 弱模型纠错率是强模型的 1.6 倍；Error Depth Hypothesis。\n   - 关系：为\"哪些错误可纠正\"提供了分类框架，proposal 在 Phase 3b 中使用。\n\n8. [The Confidence Manifold] (arXiv:2602.08159, 2026):\n   - 正确性仅占 3-8 个维度，线性可分，25 个标注样本即够。\n   - 关系：proposal 质疑可纠正性（二阶属性）是否共享此低维结构。\n\n- 调研总结：LLM 自纠错是 2025-2026 的活跃领域，已有大量工作分别解决了(a)正确性预测（Gnosis, Confidence Manifold）、(b)探针门控（早退/abstention）、(c)置信度路由（CoRefine）、(d)SAE 特征分解。PANL 论文首次将\"可纠正性\"作为独立预测目标，但仅用最简探针。本 proposal 处于这些工作的交汇处，核心差异化在于将\"可纠正性\"（而非正确性）作为预测目标并结合多种已有技术。\n```\n\n```\n【Trivial Alternative 检验】:\n\n存在两个需要认真对待的 trivial alternative：\n\n(1) **直接用输出层置信度做门控**：CoRefine 已经用 211K 参数的 Conv1D 控制器在输出置信度上实现 92.6% 的 halt 精度。如果 proposal 的隐状态探针最终只能达到 AUROC 0.70-0.75，其相对于简单置信度路由的增量价值可能非常有限。Proposal 的反驳是\"置信度不区分可纠正与不可纠正错误\"，但这需要实验证明此区分在实践中确实带来显著收益。\n\n(2) **用已有的高性能正确性探针 + 经验纠错率估计**：Gnosis 在正确性预测上达到 0.80-0.95 AUROC。一个更简单的方案是：用正确性探针检测错误 → 对所有检测到的错误尝试纠正 → 用经验成功率事后评估。这跳过了\"预测可纠正性\"这一中间步骤。Proposal 的增量价值取决于可纠正性预测是否比\"检测错误后直接尝试纠正\"显著更好。\n\n增量价值评估：proposal 的真正增量在于 (a) 避免对不可纠正错误浪费计算、(b) 避免纠正正确答案导致的 overcorrection、(c) 在不可纠正错误上 abstain。这些都有实际价值，但需要探针 AUROC 足够高才能兑现。如果 AUROC 仅从 0.614 提升到 0.70，trivial alternatives 可能接近甚至等效。\n```\n\n```\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的环节：\n\n(1) **多层集成从欺骗检测到可纠正性预测的迁移性**：这是整个技术方案的基石假设。欺骗检测中信息跨层旋转的现象在可纠正性预测中是否成立完全未知。可纠正性是一个\"二阶属性\"——不仅需要编码\"模型错了\"，还需要编码\"模型有能力纠正\"。这种复合信号可能不像欺骗那样在层间有互补编码。Proposal 诚实地承认了这一点并设计了 Phase 0 pilot，这是好的，但如果 pilot 失败，主要技术贡献就大幅缩水。\n\n(2) **可纠正性在内部表示中有足够强的可提取信号**：0.614 AUROC 的基线非常弱。一个根本性的可能是：可纠正性天然就不在模型的内部表示中被强编码——因为模型在生成初始答案时并不需要\"知道自己的错误是否可修复\"，这个信息可能根本就没有被学习到。如果可纠正性的信号上限本身就很低（比如 AUROC 0.72），那么再精细的探针设计也无济于事。\n\n(3) **SAE 混合特征对可纠正性的特殊相关性**：arXiv:2604.19974 的发现是关于\"正确性\"和\"不确定性\"的，而非\"可纠正性\"。将该框架直接外推到可纠正性是一个类比推理，缺乏直接证据。可纠正性可能有完全不同的特征编码结构。\n\n(4) **三路门控的实际效用依赖于探针质量的假设阈值**：proposal 声称在\"某个 AUROC 阈值以上\"门控优于非门控纠正。但如果这个阈值高于探针能达到的水平，整个系统设计就失去了实际意义。\n```\n\n```\n【3 维度打分】:\n\n1. Novelty: 【中】\n   理由：核心创新在于将\"可纠正性\"（而非正确性）作为独立预测目标——这确实是 PANL 论文（arXiv:2604.22271）之后的自然延伸，且目前无人做过系统性的增强探针研究。然而，技术手段几乎全部借鉴自已有工作：多层集成来自 arXiv:2604.13386，多信号融合路线与 Gnosis (arXiv:2512.20578) 高度同构，注意力熵来自 arXiv:2602.13699，SAE 分解来自 arXiv:2604.19974，三路门控框架来自 CoRefine (arXiv:2602.08948)。本质上是\"将 5-6 种已有技术组合应用到一个新的预测目标上\"。Phase 3b 的表示几何分析（可纠正性 vs 正确性的维度/线性可分性对比）是较为新颖的子贡献，但并非文章的核心 claim。审稿人很可能认为这是 \"solid engineering + interesting target\" 而非 \"novel methodology\"。\n\n2. Significance: 【中】\n   理由：自纠错是 LLM 部署中的重要问题。区分\"可纠正\"与\"不可纠正\"错误有实际价值——避免浪费计算、避免 overcorrection、在不可修复时 abstain。然而，实际影响力受限于两点：(a) 如果探针 AUROC 仅达到 0.70-0.75（高于 0.614 基线但仍然中等），实际部署价值有限——CoRefine 用更简单的方法可能达到类似效果；(b) 即使探针 AUROC 达到 0.85+，核心发现也是\"多信号探针比单层探针好\"——这在正确性预测中已被 Gnosis 等多篇论文反复验证，迁移到可纠正性预测并不令人意外（\"I would have guessed this\"）。最有意义的潜在发现是 Phase 3b 中\"可纠正性作为二阶属性是否有不同的表示几何\"——如果答案是 yes，这对 LLM 内部表示的理解有贡献；但这被定位为\"即使主实验失败也能发的 fallback contribution\"，暗示作者自身也认为其独立份量有限。\n\n3. Related Work: 【强】\n   理由：这是本 proposal 最突出的优势。对 25+ 篇近期论文的覆盖极为详尽，包括 PANL (arXiv:2604.22271)、多层集成 (arXiv:2604.13386)、SAE 分解 (arXiv:2604.19974)、CoRefine (arXiv:2602.08948)、Gnosis (arXiv:2512.20578)、Reflective Confidence (arXiv:2512.18605)、Confidence Manifold (arXiv:2602.08159) 等。每篇论文都给出了具体数字和明确的差异化定位。与最直接竞争者 CoRefine 的三点区分（信号来源、abstention 能力、可纠正性感知）清晰合理。对四篇 concurrent probe-gating 论文的定位同样精确。经调研验证，引用论文真实存在，数字描述准确。\n```\n\n```\n【概率估计】: [20% - 32%] 中位 25%\n（注：此概率基于投稿至合适的 NLP/ML 会议如 EMNLP/NeurIPS。若投稿 CoRL，概率接近 0%——desk reject。）\n\n【估计理由】:\nRelated Work 维度是强项（充分的覆盖和差异化定位），但这只保证了形式完备，不决定中稿。\n\n概率上界受 Novelty 限制：核心技术路线是\"将已有探针技术组合应用到可纠正性这个新目标\"——这是 application novelty 而非 methodological novelty。如果多信号探针在可纠正性上也能 work（AUROC 显著提升），审稿人大概率会说 \"interesting result but unsurprising approach\"；如果 work 不了（AUROC 仅微幅提升），则主要贡献退化为 Phase 3b 的表示分析——一个 negative result + geometry analysis 的组合，份量不足以撑一篇顶会主会论文。\n\n概率下界受 Significance 支撑：可纠正性作为预测目标的独立价值确实存在，Phase 3b 的二阶属性表示分析有学术趣味，dual-outcome 设计保证了最低发表可能性。\n\n中位 25% 的核心判断：idea 方向正确，有真实的增量 novelty（可纠正性作为独立目标 + 表示几何对比），但核心发现若为正面结果（\"多信号探针确实提升了可纠正性预测\"），审稿人会说 \"I would have guessed this\"——因为正确性预测领域已经反复证明了多信号优于单信号。真正的 surprise 需要来自 Phase 3b（可纠正性有截然不同的表示结构），但这被定位为 secondary contribution。\n\n【主要风险】:\n1. **Trivial alternative 威胁**：CoRefine 用输出层置信度 + 211K 参数控制器已实现 92.6% halt 精度。如果 proposal 的隐状态探针无法大幅超越这一简单基线在实际任务指标上的表现，reviewers 会质疑\"为何不直接用 logprobs\"——尤其考虑到隐状态探针需要中间层提取，部署成本更高。\n2. **可纠正性信号天花板过低的根本性风险**：0.614 AUROC 的基线极弱，可能反映的不是探针设计的问题，而是可纠正性信号本身在内部表示中编码就很弱——模型在生成答案时不需要\"知道自己的错误是否可修复\"。如果信号天花板本身就在 0.72-0.75，那么无论多精细的探针都无法产生有实际意义的门控收益，而整篇论文的叙事结构就会崩塌。\n```\n\n---\n\n**附注 - 会议选择建议**：本 proposal 应投稿至 NLP/ML 会议。按匹配度排序：\n1. **EMNLP 2026**（最佳匹配——LLM 内部表示 + 自纠错是 EMNLP 核心主题）\n2. **NeurIPS 2026**（如果 Phase 3b 表示几何分析有强结果，偏 representation learning 方向）\n3. **ICLR 2027**（如果强调 probing methodology + representation analysis）\n4. **COLM 2026**（专注语言模型的新会议，高度相关）\n\nSources:\n- [How LLMs Detect and Correct Their Own Errors (PANL)](https://arxiv.org/html/2604.22271v1)\n- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)\n- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)\n- [Can LLMs Predict Their Own Failures? — Gnosis](https://arxiv.org/abs/2512.20578)\n- [CoRefine: Confidence-Guided Self-Refinement](https://arxiv.org/abs/2602.08948)\n- [Reasoning Models Know When They're Right: Probing Hidden States](https://arxiv.org/html/2504.05419v1)\n- [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox](https://arxiv.org/html/2601.00828)\n- [The Confidence Manifold](https://arxiv.org/abs/2602.08159)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\n调研完成。现在我有足够的信息进行客观评估。\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：投稿venue完全不匹配】\n\nCoRL (Conference on Robot Learning) 2026 明确声明：\"Submissions without a robotics focus \nwill be returned without review.\" 本 proposal 是一篇纯 NLP/mechanistic interpretability 论文\n（LLM 内部表征探测 + 自我纠错门控），与机器人学习完全无关。\n\n→ 投稿 CoRL 2026 的中稿概率：≈0%（desk reject，不进入审稿流程）。\n\n适合的venue：ACL、EMNLP、NeurIPS、ICML、ICLR 的 NLP/interpretability track。\n以下评估假设投稿至适当的 NLP/ML 主会（如 ACL/EMNLP 2026 或 NeurIPS 2026）。\n\n═══════════════════════════════════════════════════════════════\n\n【领域调研】:\n\n- arXiv:2604.22271 \"How LLMs Detect and Correct Their Own Errors\" (2026): \n  本 proposal 的直接前驱。已建立 PANL（post-answer newline）token 处的 correctability \n  信号，在 own-generated errors 上达到 0.614 AUROC。该论文已将 correctability 作为一个\n  distinct prediction target 从 error detection 中分离出来。proposal 的核心概念贡献\n  （correctability as a prediction target）在此论文中已被 operationalize。\n\n- arXiv:2604.13386 \"Linear Probe Accuracy Scales with Model Size and Benefits from \n  Multi-Layer Ensembling\" (2026): \n  proposal 的主要技术灵感来源。在 deception detection 上 multi-layer stacking 将 AUROC \n  从 0.510 提升至 0.910（+78%）。但该工作针对的是 deception，其 layer-wise encoding \n  特性与 correctability 可能有本质差异。\n\n- arXiv:2604.19974 \"Are LLM Uncertainty and Correctness Encoded by the Same Features?\" \n  (2026): \n  SAE 分解发现 uncertainty 和 correctness 由功能上不同的 feature population 编码。\n  proposal 将此框架 extend 至 correctability（二阶属性）。但原论文针对的是 correctness\n  （一阶属性），transferability 是未经验证的假设。\n\n- arXiv:2602.08948 \"CoRefine\" (2026): \n  已实现基于 output-level confidence 的三路由自修正，211K 参数控制器达到 92.6% halt \n  precision，~190× token reduction。proposal 声称的差异化（hidden-state vs. output \n  logprobs, 真正的 abstention, correctability-aware）是成立的，但 CoRefine 的实际效果\n  已经相当强，增量价值需要实验证明。\n\n- arXiv:2512.18605 \"Reflective Confidence\" (2025): \n  将低 confidence 信号转化为 reflection trigger，在 AIME 2025 上达 83.3%（vs. 70.0% \n  Self-Consistency）。使用 output-level logprobs，未建模 correctability。\n\n- arXiv:2602.08159 \"The Confidence Manifold\" (2026): \n  correctness 在 activation space 中占据 3-8 维，线性可分。proposal 计划测试 \n  correctability 是否共享此结构。这是 proposal 中最有潜在 insight 的部分。\n\n- arXiv:2512.20578 \"Gnosis\" (2025): \n  multi-signal fusion for correctness prediction, hidden-only 0.78-0.92 AUROC。\n  为 correctness 而非 correctability，但技术路线相似。\n\n- arXiv:2507.12379 / arXiv:2504.05419 / arXiv:2604.18419 / arXiv:2506.12217 (2025-2026): \n  四篇 concurrent probe-gating 论文分别探测 arithmetic errors、early exit、dynamic \n  abstention、self-reflection。均未针对 correctability，但方法论上高度相似。\n\n- 调研总结: 2025-2026年出现了一个快速增长的子领域——用 LLM 内部表征探测来辅助自修正\n  决策。PANL paper 已将 correctability 概念化，多篇 probe-gating 论文已从不同角度实现\n  了 probe→decision 的 pipeline。本 proposal 处于这个快速拥挤的 landscape 的自然延伸\n  位置——将多种已有技术（multi-layer ensembling, SAE feature analysis, probe-gating）\n  组合应用于 correctability 这个已被定义但未被充分探索的 target。\n\n\n【Trivial Alternative 检验】:\n\n存在多个 trivial/simpler alternatives：\n\n1. **直接在 PANL probe 上做 multi-layer 扩展**：只需在 PANL paper 的代码基础上训练\n   每层的 logistic regression 再 stack，无需任何新的 framework。这个 trivial baseline\n   就能回答 proposal 的核心问题（multi-layer ensembling 是否提升 correctability AUROC）。\n   Proposal 的 Phase 0 本质上就是这个 trivial experiment。\n\n2. **Output-level confidence thresholding**：CoRefine 已证明 output logprobs 可以做\n   有效的三路由，92.6% halt precision。如果 hidden-state probe 只比 logprobs 好 2-3 \n   个 AUROC 点，其工程复杂度的增量价值很难justify。\n\n3. **Wait baseline 的 overcorrection 测量**：只需在 correct answers 上跑一遍 Wait \n   baseline 即可，这是一个 weekend experiment，不需要整个 ECP framework。\n\n增量价值在于：如果 ECP 能将 correctability AUROC 从 0.614 显著提升（如 >0.80），且\nhidden-state probe 明确优于 output-level confidence，那么三路门控的实际效用才能被\njustify。但这是一个 empirical bet，而非 conceptual advance。\n\n\n【前提假设检验】:\n\n核心逻辑链中有 3 个未经验证的关键假设：\n\n1. **\"Correctability 信息充分编码在 internal representations 中\"** — PANL paper \n   仅达到 0.614 AUROC，这可能不是 probing 方法的问题，而是信息本身就不够。\n   Correctability 是一个 second-order property（不仅要\"错\"，还要\"能纠正\"），\n   模型可能根本没有在内部充分编码这个信息——因为它在训练中没有被优化来做这件事。\n   这是一个 information-theoretic ceiling 问题，不是 extraction 问题。\n\n2. **\"Multi-layer ensembling 从 deception detection 可迁移至 correctability\"** — \n   Deception 的 layer-wise encoding 有其独特性（模型\"知道\"真相但选择撒谎，不同层\n   编码 ground truth vs. deceptive output），而 correctability 涉及模型自身纠错\n   机制的能力判断，编码模式可能完全不同。Proposal 诚实地承认了这是 hypothesis，\n   但整个 Phase 1 的前提就建立在这个迁移上。\n\n3. **\"SAE confounded features 是 correctability probing 的有效 substrate\"** — \n   arXiv:2604.19974 的发现是关于 correctness（一阶属性），correctability 作为\n   二阶属性是否也集中在 confounded features 中完全是推测性的。如果 correctability\n   的信息分布模式与 correctness 不同，整个 SAE-guided approach 就失去了理论基础。\n\n\n【3 维度打分】:\n\n1. Novelty: 弱-中 (Weak-to-Medium)\n   \n   理由：Proposal 的 5 个 claimed contributions 逐一分析：\n   \n   (1) \"Operationalizing correctability as a prediction target\" — 已由 PANL paper \n   (arXiv:2604.22271) 完成。该论文明确将 correctability 从 error detection 中分离\n   并建立了 baseline probe。Proposal 是在此基础上的改进，不是概念首创。\n   \n   (2) \"Multi-layer ensembling transfer to correctability\" — 这是 arXiv:2604.13386 \n   的技术在新 domain 上的直接应用。方法本身无新意，novelty 仅在于\"试了一下看行不行\"。\n   \n   (3) \"Hidden-state probe-based gating with abstention\" — probe-gating 已有 4 篇 \n   concurrent papers (arXiv:2507.12379, 2504.05419, 2604.18419, 2506.12217)。\n   Abstention 是 arXiv:2604.18419 的核心贡献。Correctability-specificity 是新的\n   组合点，但不是新方法。\n   \n   (4) \"Representational geometry of correctability\" — 这是 proposal 中真正有潜力\n   的部分。将 Confidence Manifold (arXiv:2602.08159) 的方法论 extend 到 second-order \n   property 并与 SAE 分析结合，可能产生有意义的 insight（如发现 correctability 需要\n   更高维度/非线性边界）。但方法论本身是已有的，新意在于分析对象。\n   \n   (5) \"Threshold analysis\" — 这是标准的 engineering analysis，不构成 novelty。\n   \n   总结：每个 component 都是已有技术的 transfer/组合，conceptual novelty 有限。\n   最有新意的是 Phase 3b 的表征几何分析，但独立来看也是已有方法的 straightforward\n   extension。整体是\"组合创新\"而非\"概念创新\"。\n\n2. Significance: 中 (Medium)\n   \n   理由：Selective self-correction 是一个实际重要的问题，尤其在 LLM 部署场景中。\n   但关键的 \"surprising\" 检验失败了：\n   \n   - 如果 ECP 成功提升 AUROC（如 0.614→0.75+），审稿人反应大概率是 \"makes sense, \n     combining more features helps\" 而非 \"surprising\"。\n   - 如果 ECP 未能大幅提升，审稿人反应是 \"correctability may simply not be well-encoded, \n     as the authors themselves anticipated\"。\n   - 表征几何分析如果发现 correctability 需要更高维度，审稿人反应是 \"expected, given \n     it's a second-order property\"。\n   \n   无论结果如何，都难以产生 \"I didn't expect this\" 的反应。这限制了 significance 的\n   上限。此外，practical impact 取决于 probe AUROC 能否达到 actionable 水平（~0.80+），\n   这是高度不确定的。\n\n3. Related Work: 强 (Strong)\n   \n   理由：这是 proposal 最突出的优点。引用了 25+ 篇高度相关的论文，且对每篇的描述\n   经我调研验证后是准确的（PANL 的 0.614 AUROC、arXiv:2604.13386 的 0.510→0.910、\n   CoRefine 的 92.6% halt precision、arXiv:2604.19974 的 confounded features 等数据\n   均与原文一致）。与 CoRefine 的三重差异化（signal source、abstention、correctability-\n   awareness）定位清晰。与 4 篇 concurrent probe-gating papers 的差异化也合理。\n   对自身假设的不确定性有诚实的 hedge（如反复强调 multi-layer ensembling 的迁移是\n   hypothesis）。但需注意：thorough related work ≠ idea 本身有 novelty。\n\n\n【概率估计】: \n\n⚠️ 投稿 CoRL 2026：0-5%（desk reject，venue 完全不匹配）\n\n若投稿适当 NLP/ML venue（ACL/EMNLP/NeurIPS）：[18% - 28%] 中位 22%\n\n【估计理由】: \n\nIdea 的核心是\"把多种已有 probing 技术组合应用于 correctability 这个 adjacent target\"。\n这是一个方向正确、execution-heavy 但 conceptual contribution 偏薄的 proposal。\n\n- Novelty 弱-中 是主要限制因素：5 个 contributions 中没有一个是 conceptual breakthrough，\n  全部是 existing techniques 的 transfer/组合。最有 insight 潜力的 Phase 3b 表征几何\n  分析只是 proposal 的一个 sub-component 而非主线。\n  \n- Significance 中 限制了上限：无论正负结果都不太可能让审稿人 \"surprised\"。这使得\n  即使 execution 完美，也很难超过 30%。\n\n- Related Work 强 提供了下限保障：如果 execution 优秀，thoroughness 可以防止直接被拒。\n\n- Proposal 形式非常完善（dual-outcome design、8 baselines、Phase 0 pilot），但这\n  恰恰体现了 proposal 的特点：工程完备性补偿了 conceptual thinness。一个真正 novel \n  的 idea 不需要这么多 hedging。\n\n- 22% 中位概率对应 rubric 中 \"idea 方向站得住脚但内核薄弱\" 到 \"有实质内核但发现不\n  surprising\" 之间的位置。\n\n【主要风险】: \n\n1. **\"Incremental combination\" 批评**：审稿人最可能的拒稿理由是 \"this combines existing\n   probing methods (multi-layer ensembling, SAE features, attention entropy) and applies \n   them to a closely related target (correctability vs. correctness). Each component is \n   borrowed, and the combination lacks a unifying conceptual insight.\" 这不是 execution \n   能补救的——idea 层面的组合性 novelty 是结构性弱点。\n\n2. **Information ceiling 风险**：如果 correctability 确实没有在 LLM internal representations\n   中被充分编码（0.614 AUROC 可能就是接近 ceiling 而非 extraction 不足），那么无论\n   用多复杂的 probe，AUROC 都不会大幅提升。此时 proposal 的主线 (Phase 1-2) 全部\n   fail，只剩 Phase 3b 作为 negative-result contribution——但一个\"发现 correctability\n   不太可 probe\"的 negative result 的 impact 有限。\n```\n\n---\n\n**补充说明**：\n\n关于 venue 选择，我必须明确指出：**这篇 proposal 投稿 CoRL 2026 会被直接 desk reject**。CoRL 官网 Call for Papers 明确要求 \"submissions should focus on a core robotics problem\" 且 \"submissions without a robotics focus will be returned without review\"。本 proposal 是纯粹的 NLP/mechanistic interpretability 工作，与机器人学习无任何关联。\n\n如果要继续推进这个 idea，建议将目标 venue 调整为 **ACL 2026, EMNLP 2026, NeurIPS 2026, 或 ICLR 2027**（取决于 submission timeline）。在这些 venue 下，上述 18-28% 的概率估计才是有效的。\n\nSources:\n- [How LLMs Detect and Correct Their Own Errors (PANL paper)](https://arxiv.org/html/2604.22271v1)\n- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)\n- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)\n- [CoRefine: Confidence-Guided Self-Refinement](https://arxiv.org/abs/2602.08948)\n- [Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction](https://arxiv.org/abs/2512.18605)\n- [The Confidence Manifold](https://arxiv.org/pdf/2602.08159)\n- [Can LLMs Predict Their Own Failures? (Gnosis)](https://arxiv.org/pdf/2512.20578)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Probing for Arithmetic Errors in Language Models](https://arxiv.org/pdf/2507.12379)\n- [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox](https://arxiv.org/pdf/2601.00828)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n\n## Core Problem\nLLMs attempt correction on all detected errors equally, but ~64.5% of self-generated errors are uncorrectable. Recent work reveals a faint internal 'correctability' signal at the post-answer newline token (PANL), but it achieves only 0.614 AUROC on own-generated errors using a single-layer linear probe — barely actionable for reliable gating. Meanwhile, trivial interventions like appending 'Wait' reduce blind spots by 89.3% on known errors, but their overcorrection rate on correct answers is completely untested. Confidence-based controllers like CoRefine (arXiv:2602.08948) achieve efficient three-way routing (halt/rethink/explore-alternative) using output-level logprobs, but they do not distinguish between correctable and uncorrectable errors — treating all detected issues as potentially fixable. Critically, correctability is a second-order property — it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer — and recent SAE analysis (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations, with only rare 'confounded' features bridging both signals. It is unknown whether correctability — which inherently requires engaging both axes — shares the favorable geometric properties (low dimensionality, linear separability) that correctness exhibits, or whether it requires targeting the narrow confounded feature intersection. Can enhanced multi-signal probes substantially improve correctability prediction, what is the representational relationship between correctability, correctness, and uncertainty at the feature level, and under what conditions does probe-gated correction with genuine abstention outperform both ungated correction and simpler confidence-based alternatives?\n\n## Opportunity\nThree converging findings create a clear research opportunity: (1) The PANL paper (arXiv:2604.22271) establishes that correctability is partially encoded in internal representations, but their single-layer, single-token linear probe barely exceeds chance (0.614 AUROC) on own-generated errors — leaving substantial room for improvement. For correctness prediction on adjacent tasks, Gnosis-style multi-signal fusion (arXiv:2512.20578) achieves 0.78–0.92 AUROC on hidden states alone (with the lower end on MMLU-Pro; ablation on Qwen3-1.7B only) and 0.80–0.95 with attention fusion, while attention-head entropy probes (arXiv:2602.13699) achieve +0.06 AUROC absolute improvement in OOD settings (0.70→0.76 average, 8.5% relative vs. Lookback Lens). Multi-layer probe ensembling (arXiv:2604.13386) has dramatically improved deception detection AUROC (0.510→0.910 on Harm-Pressure Knowledge in Llama-70B), though whether similar gains transfer to correctability — a fundamentally different property — is an open empirical question that motivates our pilot experiment. (2) The 'Wait' baseline from Self-Correction Bench (arXiv:2507.02778) is powerful but fundamentally non-selective: it was tested only on known errors, never on correct answers, so its overcorrection cost is unknown. QwQ-32B naturally generates 'Wait' as its first correction token 37.7–76.8% of the time depending on benchmark (SCLI5 to PRM800K-SC), but this behavior varies widely across models and is near-zero for non-reasoning models. Recent mechanistic work shows that internal states before Wait tokens causally modulate distinct reasoning patterns — restarting, recalling, uncertainty expression, and double-checking (arXiv:2510.04128, EMNLP 2025 Findings) — and that Wait token probabilities correlate with reasoning correctness in ways that vary by training strategy (arXiv:2601.17421). These findings suggest Wait's effectiveness is not uniform but depends on which reasoning pattern it triggers, creating an opportunity for probe-selective application. Reflective Confidence (arXiv:2512.18605) demonstrates a related approach, transforming low-confidence output signals into reflection triggers rather than stopping, achieving 83.3% accuracy on AIME 2025 vs. 70.0% for Self-Consistency — but uses only output-level logprobs, not internal representations. (3) Existing gating approaches occupy adjacent niches but leave a clear gap. CoRefine (arXiv:2602.08948) implements three-way routing (halt/rethink/alternative) via a 211K-parameter Conv1D controller on output-level confidence, achieving 92.6% halt precision — but its decisions are confidence-based rather than correctability-aware, and its ALTERNATIVE option explores different approaches rather than genuinely abstaining when errors are likely unfixable. Four concurrent probe-gating papers address correctness, early exit, abstention, or reflection control — but none probe for correctability (whether a specific error is fixable), and none combine hidden-state probes with genuine abstention in a correctability-aware framework. Moreover, the SAE dissociation paper (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations — with 68% of pure incorrectness features being causally inert and only rare confounded features (102 out of 1,057 in Llama-3.1-8B) bridging both signals to achieve 0.79 AUROC with just 3 features. This finding directly challenges naive linear probing over broad activations and suggests correctability prediction may need to target the narrow confounded feature intersection, motivating our SAE-guided probe design and representational analysis.\n\n## Related Work / Landscape\nThe PANL paper (arXiv:2604.22271) establishes correctability prediction as a distinct task from error detection, achieving 0.986 AUROC for detection but only 0.614 for correctability on own-generated errors using single-layer logistic regression at one token position. This gap — high detectability but low correctability prediction — is the central technical challenge. Gnosis (arXiv:2512.20578) achieves 0.80–0.95 AUROC for correctness prediction by fusing final-layer hidden states with attention-map features via a ~5M-parameter architecture; notably, the hidden-state stream alone achieves 0.78–0.92 AUROC (with the lower end on MMLU-Pro; ablation only reported for Qwen3-1.7B), with attention fusion adding 0–3 points depending on the task. The multi-layer ensembling paper (arXiv:2604.13386) shows that logistic stacking across complementary layers can dramatically improve probe performance — achieving 0.510→0.910 AUROC on the hardest deception detection task (Harm-Pressure Knowledge, Llama-70B) — because informative directions rotate across layers and double-fault analysis reveals complementary error patterns between early and late layers. However, this result is specific to deception detection, which has different layer-wise encoding properties than correctness or correctability; whether analogous gains transfer is an empirical hypothesis we test via a Phase 0 pilot. For correctness prediction specifically, multi-signal approaches show more modest but consistent gains: attention-head entropy probes (arXiv:2602.13699) improve OOD AUROC by +0.06 absolute (0.70→0.76 average across 5 models, an 8.5% relative improvement over Lookback Lens), and perturbation-stability probes (arXiv:2505.21772) add +6 AUROC points via targeted adversarial perturbations to hidden states. SWIFT (arXiv:2505.12225) concatenates all-layer hidden states with learned gating weights to extract token-level quality signals.\n\nThe Self-Correction Bench (arXiv:2507.02778) documents the 64.5% blind spot and shows 'Wait' reduces it by 89.3%. QwQ-32B naturally generates 'Wait' as its first correction token at rates varying by benchmark (37.7% on SCLI5, 72.5% on GSM8K-SC, 76.8% on PRM800K-SC), but this behavior is model-specific — other reasoning models show different patterns and non-reasoning models rarely generate Wait spontaneously. The Wait baseline was never tested on correct answers, leaving the overcorrection cost unknown. Two recent papers provide mechanistic understanding of Wait tokens: arXiv:2510.04128 (EMNLP 2025 Findings) trains crosscoders on DeepSeek-R1-Distill-Llama-8B to identify features that promote or suppress Wait tokens, discovering causal features for distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) via activation steering at layer 15; arXiv:2601.17421 systematically analyzes Wait and other discourse tokens across model scales and training strategies, finding that Wait token probabilities correlate with reasoning correctness but that models exploit this signal only partially. Reflective Confidence (arXiv:2512.18605) proposes a related approach, transforming low-confidence output-level logprob signals into reflection triggers rather than early stopping, achieving 83.3% accuracy on AIME 2025 (vs. 70.0% Self-Consistency, K=32) on Qwen3-8B — demonstrating that selective confidence-gated correction can significantly outperform non-selective baselines, though it uses output-level signals rather than internal representations and does not model correctability.\n\nCoRefine (arXiv:2602.08948) is the closest existing system to our three-way gating, implementing halt/rethink/alternative decisions via a 211K-parameter Conv1D controller that consumes output-level confidence traces from the frozen LLM. It achieves 92.6% halt precision, averages 2.7 refinement steps per problem, and reduces tokens ~190× relative to 512-sample baselines on mathematical reasoning benchmarks. However, CoRefine differs from our proposal in three fundamental ways: (a) it uses output-level logprobs rather than hidden-state probes, missing the richer internal signal that PANL demonstrates exists; (b) its HALT decision accepts the current answer — it never genuinely abstains or flags for external intervention when errors are likely unfixable; (c) its routing is confidence-based, not correctability-aware — it cannot distinguish correctable from uncorrectable errors, treating all low-confidence outputs as potentially improvable. Four concurrent probe-gating papers occupy adjacent niches: arXiv:2507.12379 probes for arithmetic errors and selectively re-prompts (only 6–12% of detected errors actually get corrected); arXiv:2504.05419 uses probes for early exit from reasoning chains (AUROC 0.77–0.91 for correctness, not correctability); arXiv:2604.18419 trains value-function probes for dynamic mid-generation abstention; arXiv:2506.12217 uses activation steering to modulate self-reflection frequency. None of these probe for correctability specifically, and none combine hidden-state probes with genuine abstention in a correctability-aware framework.\n\nA critical finding for our probing approach comes from arXiv:2604.19974, which uses sparse autoencoders to decompose LLM representations into functionally distinct feature populations. In Llama-3.1-8B, they identify 700 pure uncertainty features, 255 pure incorrectness features, and only 102 confounded features encoding both signals. The key insight is a functional dissociation: 68% of pure incorrectness features are causally inert (mean accuracy delta of -0.03% when suppressed), while pure uncertainty features are essential for model performance, and only confounded features bridging both axes are causally effective for correctness prediction — with just 3 confounded features from layer 18 achieving 0.79 AUROC. This has direct implications for correctability probing: correctability is inherently a joint uncertainty+correctness concept (the model must be wrong AND the correction mechanism must be able to reach the right answer), so probes targeting broad activation spaces risk relying on functionally inert incorrectness features. This motivates our SAE-guided feature analysis in Phase 3b and suggests that the confounded feature intersection — not the full activation space — may be the effective substrate for correctability prediction, potentially explaining why the single-layer PANL probe achieves only 0.614 AUROC.\n\nThe Confidence Manifold (arXiv:2602.08159) shows correctness occupies only 3–8 dimensions in activation space and is linearly separable with as few as 25 labeled examples. However, correctability is a second-order property: it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer given the model's knowledge state and reasoning pathways. The Interpretability-without-Actionability paper (arXiv:2603.18353) provides indirect evidence that this second-order property may be harder to capture: even with 98.2% detection AUROC, activation steering corrected only 20–24% of errors (concept-bottleneck steering) or 0% (SAE feature steering), revealing a 53-percentage-point knowledge-action gap. This suggests correctability may occupy a different — possibly higher-dimensional or non-linear — representational subspace than correctness, and the SAE dissociation finding (arXiv:2604.19974) provides a mechanistic explanation: correctability may require engaging the narrow confounded feature population rather than the broader (but functionally inert) incorrectness features. The Truth-as-a-Trajectory framework (arXiv:2603.01326) proposes that cross-layer displacement vectors capture properties that static single-layer probes miss, potentially relevant to second-order properties like correctability. The Accuracy-Correction Paradox (arXiv:2601.00828) shows weaker models achieve 1.6× higher correction rates and proposes the Error Depth Hypothesis — that stronger models make fewer but deeper errors that resist self-correction — providing a taxonomy of error correctable characteristics. The information-theoretic analysis of correlated errors (Preprints.org 202601.0892) formalizes bounds on self-correction when generator and evaluator share failure modes, motivating external probe-based gating as a mechanism to break the correlation. LLMs also encode problem difficulty as a linearly decodable property (arXiv:2510.18147, ρ ≈ 0.88), suggesting that related meta-cognitive properties may be extractable, though correctability's second-order nature makes direct analogy uncertain.\n\n## Approach\nWe propose a four-phase study of correctability prediction and selective self-correction, including an explicit pilot to validate the multi-layer ensemble transfer hypothesis, SAE-guided feature analysis informed by the uncertainty-correctness dissociation (arXiv:2604.19974), and a contribution plan that is robust to negative results.\n\n**Phase 0: Pilot Feasibility Study.** Before committing to the full experimental pipeline, we run a targeted pilot on the PANL paper's existing correctability labels (Gemma-3-27B, TriviaQA subset). We train independent logistic regression probes at each of the ~42 layers, identify complementary layers via double-fault analysis (following arXiv:2604.13386's methodology), and build a 3–5 layer stacked ensemble. This pilot directly tests whether the multi-layer ensembling technique that improved deception detection AUROC by up to 78% transfers to correctability prediction. Success criterion: if the ensemble achieves ≥0.70 AUROC (meaningful improvement over the 0.614 single-layer baseline), we proceed to Phase 1. If the ensemble plateaus below 0.70, we shift emphasis to the representational geometry and SAE feature analysis (Phase 3b), which remains a publishable contribution. Estimated cost: ~15 H100-hours (single model, single dataset, multi-layer extraction only).\n\n**Phase 1: Enhanced Correctability Probes (ECP).** We move beyond the PANL paper's single-layer, single-token linear probe by developing multi-signal correctability probes. (a) Multi-layer ensemble: train independent logistic regression probes at each layer, select 3–5 complementary layers via double-fault analysis, combine via logistic stacking (following arXiv:2604.13386, but with the explicit caveat that this technique was validated on deception detection — our Phase 0 tests transfer to correctability). (b) Multi-token features: concatenate hidden states from the post-answer newline token (PANL), the last answer token (LAT), and the last 2 reasoning tokens — the PANL paper's own causal analysis shows LAT carries complementary information at different layers. (c) Attention-based features: extract per-head entropy statistics across semantic sections (question, reasoning, answer), following the methodology of arXiv:2602.13699 which achieves +0.06 AUROC absolute improvement over Lookback Lens in OOD correctness prediction. (d) Wait-token features: inspired by the crosscoder analysis of arXiv:2510.04128, extract hidden-state features at the position immediately preceding natural Wait tokens (when present), capturing the causal features that modulate reasoning patterns (restarting, recalling, uncertainty expression, double-checking). The insight from arXiv:2601.17421 that Wait token probabilities correlate with reasoning correctness suggests these features encode meta-cognitive state relevant to correctability. (e) SAE-guided feature selection: motivated by arXiv:2604.19974's finding that only confounded features (encoding both uncertainty and correctness) are causally effective while pure incorrectness features are functionally inert, we train SAEs on our target models and identify confounded features relevant to correctability. We then compare probes trained on (i) full activation spaces, (ii) SAE-reconstructed activations from confounded features only, and (iii) SAE-reconstructed activations excluding pure incorrectness features. This tests whether the narrow confounded feature intersection — rather than broad activations — is the effective substrate for correctability prediction, and whether filtering out causally inert features improves probe AUROC. (f) Non-linear probe ablation: compare linear probes, 2-layer MLPs (hidden dim 16/32), and SWIFT-style all-layer gated aggregation — motivated by the possibility that correctability, as a second-order property, may require non-linear boundaries even if correctness is linearly separable in 3–8 dimensions (arXiv:2602.08159). All probes are trained on on-policy correctability labels generated by running the model's actual self-correction pipeline (multiple correction attempts per error to get calibrated fixability scores), avoiding the distribution mismatch of synthetic error injection documented in SCoRe (arXiv:2409.12917).\n\n**Phase 2: Three-Way Gated Self-Correction.** Use the ECP to implement a three-way decision at inference time: (i) if the error detection probe indicates the answer is likely correct, retain the original answer; (ii) if the error is detected AND the correctability probe predicts high fixability (above a calibrated threshold), attempt correction — either prompting-based correction or probe-selective Wait insertion (applying Wait only when the probe detects both an error and high correctability, leveraging the mechanistic finding from arXiv:2510.04128 that Wait triggers different reasoning patterns depending on internal state); (iii) if the error is detected but correctability is predicted as low, abstain or flag for external intervention. This design is distinguished from CoRefine's (arXiv:2602.08948) three-way routing in three key ways: we use hidden-state probes rather than output-level confidence, our third option is genuine abstention (declining to answer) rather than exploring alternative approaches, and our gating is explicitly correctability-aware — routing based on predicted fixability rather than confidence level. Where CoRefine optimizes compute efficiency (achieving ~190× token reduction), our framework optimizes decision quality by preventing wasted correction attempts on unfixable errors and avoiding overcorrection of correct answers.\n\n**Phase 3: Comprehensive Evaluation.** Evaluate across three dense models where probing is well-understood: Gemma-3-27B (same as PANL paper, validates signal transfer), Qwen-2.5-7B-Instruct (same as PANL paper, smaller scale), and Mistral-Small-3.2-24B (different architecture family, tests generalization). Use three benchmarks (TriviaQA, MMLU, GSM8K) with 10K+ questions each. Compare gated correction against eight baselines: (1) no correction, (2) ungated prompting-based correction, (3) Wait-appended correction applied to all answers — measuring the previously-untested overcorrection rate, (4) Wait-appended correction applied only to probe-detected errors, (5) confidence-threshold gating using log-probabilities (following Reflective Confidence's approach, arXiv:2512.18605), (6) CoRefine-style output-confidence routing (arXiv:2602.08948) — retrained on our models/benchmarks for fair comparison, (7) PAG-style generative verification (arXiv:2506.10406), (8) oracle gating (upper bound). Conduct ablations on: probe architecture (linear vs. MLP vs. ensemble vs. SAE-guided), feature sources (PANL-only vs. multi-token vs. +attention vs. +Wait-features vs. +SAE-confounded), layer selection, cross-task transferability, and threshold sensitivity analysis showing at what AUROC level gating begins to outperform ungated correction.\n\n**Phase 3b: Representational Geometry and Feature Decomposition of Correctability (Robust to Negative Probe Results).** Regardless of probe performance, we conduct a dedicated analysis of the representational relationship between correctability, correctness, and uncertainty at the feature population level. (a) Subspace comparison: compute the principal components of correctness and correctability representations separately (following arXiv:2602.08159's methodology) and measure subspace alignment via principal angle analysis — testing whether correctability occupies the same 3–8 dimensional subspace as correctness or requires distinct dimensions. (b) Dimensionality analysis: determine how many dimensions encode correctability vs. correctness at each layer, and whether correctability requires higher dimensionality (consistent with its second-order nature). (c) Non-linearity characterization: compare linear vs. non-linear probe AUROC gaps for correctability vs. correctness — a larger gap for correctability would indicate it occupies a more complex geometric region. (d) SAE feature decomposition: train SAEs on our target models and decompose correctability-predictive features into pure uncertainty, pure incorrectness, and confounded populations (following arXiv:2604.19974's 2×2 framework). Test whether confounded features are disproportionately important for correctability prediction compared to correctness prediction — which would provide mechanistic evidence that correctability requires simultaneously engaging both uncertainty and correctness axes. Measure the causal efficacy of each population via suppression experiments: if suppressing pure incorrectness features has minimal effect on correctability prediction (paralleling the functional inertness finding for correctness), this confirms the narrow confounded intersection hypothesis and explains the representational ceiling for broad-activation linear probes. (e) Error depth analysis: using the Error Depth Hypothesis framework (arXiv:2601.00828), characterize what makes errors correctable vs. uncorrectable — surface-level errors (calculation mistakes, recall failures) vs. deep errors (fundamental misunderstanding, missing knowledge) — and test whether this taxonomy is reflected in representational distance and SAE feature activation patterns. (f) Cross-layer trajectory analysis: inspired by Truth-as-a-Trajectory (arXiv:2603.01326), examine whether correctability is better captured by cross-layer displacement vectors than by static single-layer activations, which would explain why single-layer probes struggle. This phase yields publishable insights regardless of whether the ECP achieves high AUROC, providing the first empirical characterization of how correctability is (or is not) represented in LLM internal states and the first application of the SAE uncertainty-correctness dissociation framework to a second-order property.\n\n## Inspiration\nThe gap between 0.614 AUROC (single-layer PANL probe) and the consistently higher performance of multi-signal probes on correctness prediction (Gnosis hidden-only: 0.78–0.92; attention entropy: +0.06 AUROC absolute in OOD) suggests correctability prediction has room for improvement with better probing methodology — though the magnitude of potential gains is uncertain given correctability's second-order nature. The dramatic improvement from multi-layer ensembling on deception detection (0.510→0.910; arXiv:2604.13386) demonstrates that multi-layer stacking can rescue failing single-layer probes, but transferability to correctability is a hypothesis to test, not a guaranteed outcome. The SAE dissociation finding (arXiv:2604.19974) — that only rare confounded features bridging uncertainty and correctness are causally effective — provides both a challenge and an opportunity: correctability probes may need to target this narrow feature intersection, but successfully doing so could yield more principled and interpretable predictions than broad-activation probing. The untested overcorrection cost of the 'Wait' baseline, combined with new mechanistic understanding of Wait tokens' causal role in triggering distinct reasoning patterns (arXiv:2510.04128, arXiv:2601.17421), creates a clear opportunity for probe-selective Wait application. CoRefine (arXiv:2602.08948) demonstrates the viability of learned three-way routing for self-correction but uses output-level confidence without correctability awareness or genuine abstention — leaving a well-defined gap for hidden-state probe-based gating that distinguishes correctable from uncorrectable errors. Key untried combination: multi-signal enhanced probes for correctability prediction informed by SAE feature analysis + three-way gating with genuine abstention + comparison against Wait and confidence-based controllers, with explicit analysis of what makes correctability representationally distinct from correctness at the feature population level.\n\n## Key References\n- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (arXiv:2604.22271, 2026) — establishes PANL correctability signal, 0.614 AUROC baseline\n- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in LLMs (arXiv:2507.02778, NeurIPS 2025 Workshop) — 64.5% blind spot, Wait baseline achieving 89.3% reduction; QwQ-32B generates Wait first-token at 37.7–76.8% depending on benchmark\n- Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386, 2026) — multi-layer stacking on deception detection: +29% on Insider Trading, +78% on Harm-Pressure Knowledge (0.510→0.910 in Llama-70B); transfer to correctability is a hypothesis we test\n- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits — Gnosis (arXiv:2512.20578, 2025) — multi-signal fusion for correctness prediction: hidden-only 0.78–0.92 AUROC (ablation on Qwen3-1.7B), fusion 0.80–0.95 AUROC\n- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, 2026) — SAE decomposition reveals functionally distinct feature populations: 68% of pure incorrectness features are causally inert; only rare confounded features (102/1,057 in Llama-3.1-8B) bridge uncertainty and correctness, achieving 0.79 AUROC with 3 features from layer 18; directly informs our probe design and Phase 3b analysis\n- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv:2602.08948, 2026) — three-way routing (halt/rethink/alternative) via 211K-parameter Conv1D controller on output-level confidence; 92.6% halt precision, ~190× token reduction; differs from our approach in signal source (output logprobs vs. hidden-state probes), decision type (no genuine abstention), and gating criterion (confidence vs. correctability)\n- Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction (arXiv:2512.18605, 2025) — transforms low-confidence output signals into reflection triggers; 83.3% on AIME 2025 vs. 70.0% Self-Consistency; uses output-level logprobs, no correctability modeling\n- Internal states before wait modulate reasoning patterns (arXiv:2510.04128, EMNLP 2025 Findings) — crosscoders identify causal features promoting/suppressing Wait tokens; distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) triggered by pre-Wait internal states\n- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421, Jan 2026) — Wait token probabilities correlate with reasoning correctness; models exploit Wait signals only partially; implications for token-level steering\n- Probing for Arithmetic Errors in Language Models (arXiv:2507.12379, 2025) — probe-guided selective re-prompting, 6–12% correction rate\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv:2504.05419, 2025) — probe-gated early exit, AUROC 0.77–0.91\n- Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning (arXiv:2604.18419, 2026) — value-function probes for abstention gating\n- From Emergence to Control: Probing and Modulating Self-Reflection in Language Models (arXiv:2506.12217, 2025) — self-reflection vector steering\n- The Confidence Manifold (arXiv:2602.08159, 2026) — correctness in 3–8 dimensions, 25-example sufficiency, linearly separable\n- Attention Head Entropy of LLMs Predicts Answer Correctness (arXiv:2602.13699, 2026) — per-head 2-Rényi entropy achieves OOD AUROC 0.76 average (+0.06 absolute, 8.5% relative improvement over Lookback Lens)\n- PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier (arXiv:2506.10406, 2025)\n- Understanding the Dark Side of LLMs' Intrinsic Self-Correction (ACL 2025) — overcorrection and cognitive biases\n- Interpretability without Actionability (arXiv:2603.18353, 2026) — knowledge-action gap: 98.2% detection AUROC but only 20–24% correction via steering, 53-point gap\n- Mining Intrinsic Rewards from LLM Hidden States — SWIFT (arXiv:2505.12225, 2025) — all-layer gated aggregation\n- Between the Layers Lies the Truth (arXiv:2603.22299, 2026) — cross-layer agreement features\n- Truth as a Trajectory (arXiv:2603.01326, 2026) — cross-layer displacement vectors capture properties missed by static single-layer probes\n- Training Language Models to Self-Correct via Reinforcement Learning — SCoRe (arXiv:2409.12917, 2024) — on-policy training data importance\n- Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)\n- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox (arXiv:2601.00828, 2026) — Error Depth Hypothesis: weaker models achieve 1.6× higher correction rates; deeper errors resist self-correction\n- No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes (arXiv:2509.10625, ICLR 2026 Workshop)\n- Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv:2505.21772, 2025) — +6 AUROC points via adversarial perturbation stability\n- LLMs Encode How Difficult Problems Are (arXiv:2510.18147, 2025) — difficulty linearly decodable (ρ ≈ 0.88); meta-cognitive properties extractable but correctability's second-order nature makes transfer uncertain\n- Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors (Preprints.org 202601.0892, Feb 2026) — formalizes bounds on self-correction with correlated generator-evaluator errors\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '220–280 H100-hours (Phase 0 pilot: ~15 hrs; inference for 3 models × ~30K questions × 3 passes [initial + Wait + correction] + multi-layer hidden state extraction across ~10 layers + attention feature extraction + Wait-feature extraction + SAE training and feature decomposition + probe training + representational geometry analysis + ablations)', 'timeline': '11–13 weeks (includes pilot, SAE analysis, full experiments, geometry analysis, paper writing)', 'estimated_gpu_cost': '$550–700 (at ~$2.50/H100-hr on cloud providers)'}\n- **human_in_loop**: {'gpu_hours': '220–280 H100-hours (same compute, faster iteration via AI-assisted code/analysis)', 'timeline': '8–10 weeks', 'claude_api_cost': '$150–210 (experiment orchestration, SAE analysis notebooks, geometry visualization, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$550–700'}\n- **auto_research**: {'gpu_hours': '300–360 H100-hours (overhead from automated probe architecture sweeps, SAE training and decomposition, threshold optimization, representational geometry grid, and broader ablation grid)', 'timeline': '2–3 weeks wall-clock', 'claude_api_cost': '$420–580 (full pipeline orchestration, code generation, debugging, SAE analysis, statistical analysis, visualization, paper drafting)', 'estimated_gpu_cost': '$750–900', 'speed_bottleneck': 'Sequential multi-layer hidden state extraction over ~90K forward passes (3 models × 30K questions); extraction requires full-precision activations at 5–10 layers per pass and cannot be batched as aggressively as standard inference; SAE training adds ~20–30 H100-hours per model'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T19:03:19.156Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T19:03:19.156Z",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T19:03:19.171Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have enough information. Let me compile my assessment.

---

```
【阶段】: Triage

⚠️ 【致命前置问题：投稿会议不匹配】
CoRL (Conference on Robot Learning) 2026 官网明确声明：
"Submissions without a robotics focus will be returned without review."
本 proposal 的内容（LLM 内部表征探针、自我纠错门控、SAE 特征分解）100% 是纯 NLP/ML 机制研究，
与机器人学习完全无关。无论 idea 质量如何，投稿 CoRL 将被直接 desk reject，概率为 0%。
适合的会议：NeurIPS / ICML / ICLR / ACL / EMNLP。
以下评估基于假设投稿到合适的 ML/NLP 主会（如 NeurIPS 2026），以评价 idea 本身的质量。

【领域调研】:
- [arXiv:2604.22271] "How LLMs Detect and Correct Their Own Errors" (2026):
  建立了 PANL (Post-Answer NewLine) correctability 信号的概念，单层线性探针在 own-generated errors 上达到 0.614 AUROC。
  这是本 proposal 最直接的前序工作——本 proposal 本质上是在这篇论文的基础上做"探针方法升级"。

- [arXiv:2604.13386] "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (2026):
  多层集成探针在欺骗检测上将 AUROC 从 0.510 提升到 0.910（+78%）。
  但该结果特定于 deception detection，是否可迁移到 correctability 是未验证假设。

- [arXiv:2604.19974] "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (2026):
  用 SAE 分解出 pure uncertainty / pure incorrectness / confounded 三类特征，发现 68% 的 pure incorrectness 特征因果无效。
  proposal 将其引入 correctability 分析是合理的延伸，但属于"应用已有框架到新场景"。

- [arXiv:2602.08948] "CoRefine" (2026):
  已实现三路路由（halt/rethink/alternative），用 211K 参数 Conv1D 控制器在 output-level confidence 上运作，92.6% halt precision。
  proposal 的核心差异化点是用 hidden-state 探针替代 output-level confidence + 加入 genuine abstention。

- [arXiv:2512.20578] "Gnosis" (2025):
  多信号融合在 correctness prediction 上达到 0.80–0.95 AUROC。
  proposal 的多信号探针设计（多层+多 token+attention 熵）与 Gnosis 的方法论高度相似，只是目标从 correctness 切换到 correctability。

- [arXiv:2504.05419] "Reasoning Models Know When They're Right" (2025):
  用 hidden-state 探针做 early exit，AUROC 0.77–0.91（针对 correctness）。

- [arXiv:2602.08159] "The Confidence Manifold" (2026):
  correctness 仅需 3-8 维、25 个样本即可线性分离。Proposal 想测试 correctability 是否也有类似结构。

- 调研总结: correctability prediction 作为一个 distinct target（区分于 correctness/error detection）是由 PANL 论文刚刚建立的概念（2026年4月）。
  本 proposal 的定位是"用更强的探针方法论提升 correctability AUROC + 将其用于三路门控"。
  核心方法论组件（多层集成、多 token、attention 熵、SAE 引导）均来自已有工作，proposal 的贡献主要在于"组合 + 应用到新目标"。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁：
1. CoRefine 的 output-level confidence 已经实现了 92.6% halt precision 的三路路由。
   Proposal 需要证明 hidden-state 探针比 output-level confidence 好多少——如果提升有限（如 2-3 个 AUROC 点），
   那付出的额外复杂度（多层提取、SAE 训练、探针训练）是否值得？
2. 简单的 confidence thresholding（如 Reflective Confidence 的 logprob 阈值方法）在 AIME 2025 上达到 83.3%。
3. 核心问题：如果 correctability 作为一个内部信号本身就很弱（PANL 论文显示只有 0.614），
   那更好的探针可能只是从 0.614 提升到 0.70-0.75——这个增量是否足以让 probe-gated correction 真正优于简单 confidence baseline？
   Proposal 自己也承认 "whether similar gains transfer... is an open empirical question"。

增量价值在于：如果能证明 hidden-state probes 确实能可靠区分 correctable vs. uncorrectable errors（而 output-level confidence 不能），
这在理论上有意义。但这个 "如果" 本身就是最大的不确定性。

【前提假设检验】:
核心 claim 的逻辑链中有几个未验证的关键假设：

1. **"correctability 是可被探针捕获的信号"假设**：PANL 论文的 0.614 AUROC 仅略高于随机（0.5）。
   这可能意味着 correctability 根本就不是一个在 hidden states 中有强编码的属性——
   也许模型内部根本没有"我能纠正这个错误"的稳定表征。
   Proposal 假设 0.614 是因为探针方法太弱，但另一个同样合理的解释是：信号本身就很弱。

2. **"多层集成从 deception 迁移到 correctability"假设**：deception detection 和 correctability 是根本不同的任务。
   Deception 有明确的"模型知道真相但选择说谎"的编码模式；
   correctability 则取决于模型的知识覆盖、推理路径可达性等更复杂的因素。
   Proposal 用 Phase 0 测试这个假设是好的实验设计，但如果结果是 negative，
   整个 Phase 1 的方法论基础就塌了。

3. **"confounded features 是 correctability 的有效基底"假设**：
   arXiv:2604.19974 的 confounded features 发现是关于 uncertainty × correctness 的关系，
   而 correctability 是一个更高阶的概念（涉及纠错机制的可达性）。
   从"uncertainty-correctness confounded features"到"correctability prediction"的跳跃缺乏理论支撑。

4. **"genuine abstention 优于 CoRefine 的 ALTERNATIVE"假设**：
   在实际应用中，"尝试另一种方法"（CoRefine 的 ALTERNATIVE）可能比"直接放弃"（abstention）更有价值。
   Proposal 预设 abstention 是更好的策略，但这取决于具体应用场景。

【3 维度打分】:

1. Novelty: 弱-中 —
   - 核心概念"correctability as distinct from correctness"已由 PANL 论文（2604.22271）建立
   - 探针方法论的每个组件都是从已有工作借鉴：多层集成（2604.13386）、attention 熵（2602.13699）、SAE 引导（2604.19974）、多 token（PANL 论文自己的 causal analysis）
   - 三路门控已由 CoRefine（2602.08948）实现，差异在于信号源（hidden-state vs. output-level）和 abstention
   - 真正的 novelty delta 在于"组合这些技术应用于 correctability + SAE 分解分析 correctability 的表征结构"——这是一个有效但较薄的 novelty
   - Phase 3b 的 representational geometry 分析如果做好可以是不错的贡献，但本质上仍然是"将已有分析框架应用到新目标"

2. Significance: 中 —
   - 研究问题本身有意义：理解哪些错误可以被自我纠正是 LLM 部署中的真实需求
   - 但实际影响力受限于：(a) 如果信号本身就弱，实际可部署性很低；(b) 需要多层 hidden state 提取的方案在实际推理中成本很高；(c) 纯 confidence-based 方法已经相当有效
   - Phase 3b 的表征分析可能有较好的科学贡献（理解 second-order properties 的编码方式），但其影响力取决于发现是否 surprising
   - 如果核心发现是 "correctability 需要更高维度/非线性边界"，审稿人可能会说 "I would have guessed this"——因为更高阶的属性需要更复杂的表征是直觉上预期的

3. Related Work: 强 —
   - 相关工作覆盖非常全面，差异化定位清晰
   - 与 CoRefine 的三重区分（信号源、abstention、correctability-aware）描述准确
   - 对每篇引用工作的局限性分析到位（如 Gnosis 的 ablation 仅在 Qwen3-1.7B 上、多层集成的 deception-specific 性质）
   - 唯一的小问题：对四篇 concurrent probe-gating 论文的总结有点快速，可以更深入地分析与本工作的区别

【概率估计】: [15% - 30%] 中位 22%
（注意：此概率是假设投稿到 NeurIPS/ICML 等合适会议。投稿 CoRL 的概率为 ~0%，会被 desk reject。）

【估计理由】:
- Novelty 维度限制了上界：核心是"已有探针技术的组合应用于一个刚被提出的新目标"，审稿人可能会评价为 incremental combination
- Significance 处于中等：研究问题有价值，但核心发现（无论 positive 还是 negative）不太可能是 surprising。如果探针提升到 0.75 AUROC，审稿人可能说 "expected improvement from better probing"；如果 plateau 在 0.65，Phase 3b 的表征分析虽有趣但 impact 有限
- Related Work 是该 proposal 最强的维度，但好的 related work 覆盖不能弥补 novelty 的不足
- Proposal 过于 kitchen-sink：4 个 phase + 6 种探针变体 + 8 个 baseline + SAE 分析 + 表征几何 + error depth，试图在一篇论文中做太多事情，这本身可能被审稿人视为缺乏聚焦
- "Robust to negative results" 设计虽然是好的学术实践，但也暗示作者自己对核心 claim 的信心不足

【主要风险】:
1. **信号天花板风险**：correctability 可能在 hidden states 中根本就没有强编码——0.614 AUROC 可能不是探针方法的问题，而是信号本身的问题。如果增强探针只能把 AUROC 提到 0.68-0.72，整个 gating 框架的实用价值存疑，论文会变成"我们用了很多技术但提升有限"的 negative result + 分析论文
2. **Novelty 薄弱风险**：审稿人可能认为这是"将一堆已有的探针改进技术套用到一个新定义的预测目标上"——方法层面无新意，目标层面由 PANL 论文已经定义，组合本身不构成充分的 novelty

⚠️ 再次强调：如果目标确实是 CoRL 2026，请立即更换投稿会议。这个 proposal 与 robot learning 完全无关，会被 desk reject。
```

Sources:
- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features? (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)
- [CoRefine: Confidence-Guided Self-Refinement (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Reasoning Models Know When They're Right (arXiv:2504.05419)](https://arxiv.org/html/2504.05419v1)
- [Can LLMs Predict Their Own Failures? Gnosis (arXiv:2512.20578)](https://arxiv.org/pdf/2512.20578)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage
```

## ⚠️ 关键前置问题：严重的会议选择错位

在进入 idea 质量评估之前，必须先指出一个**致命的会议选择问题**：

**CoRL (Conference on Robot Learning) 是机器人学习会议**，其 Call for Papers 明确要求论文聚焦于 "core robotics problem"，主题包括机器人感知、控制、操作、导航、运动等。本 proposal 完全关于 **LLM 内部表示的可纠正性探测与自纠错门控**，与机器人学习零关联。投稿 CoRL 极大概率会被 **desk reject**。

合适的目标会议应为：**EMNLP 2026, ACL 2026, NeurIPS 2026, ICLR 2027, 或 COLM 2026**。

以下评估基于 idea 本身的质量，假设投稿到合适的 NLP/ML 会议。

---

```
【领域调研】:

1. [How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals] (arXiv:2604.22271, 2026):
   - 这是本 proposal 的直接前驱。建立 PANL (post-answer newline token) 信号，错误检测 AUROC 0.986 但可纠正性预测仅 0.614。
   - 关系：proposal 的核心起点，试图改进 0.614 的基线。

2. [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling] (arXiv:2604.13386, 2026):
   - 多层集成在欺骗检测上将 AUROC 从 0.510 提升至 0.910 (+78%)。
   - 关系：proposal 的核心技术借鉴源。但该工作针对的是欺骗检测，与可纠正性是截然不同的任务，迁移性是开放问题。

3. [Are LLM Uncertainty and Correctness Encoded by the Same Features?] (arXiv:2604.19974, 2026):
   - SAE 分解显示不确定性与正确性由功能性分离的特征群编码；68% 纯错误特征因果惰性；仅 102 个混合特征有效。
   - 关系：proposal 的 SAE 引导探针设计和 Phase 3b 分析的理论基础。

4. [Can LLMs Predict Their Own Failures? — Gnosis] (arXiv:2512.20578, 2025):
   - 多信号融合（隐状态+注意力）实现正确性预测 AUROC 0.80-0.95，~5M 参数。
   - 关系：proposal 的多信号探针设计与 Gnosis 在技术路线上高度相似，但 target 不同（正确性 vs 可纠正性）。

5. [CoRefine: Confidence-Guided Self-Refinement] (arXiv:2602.08948, 2026):
   - 基于输出层置信度的三路路由（halt/rethink/alternative），92.6% halt 精度，~190× token 缩减。
   - 关系：最直接的系统级竞争者。proposal 的区分点在于使用隐状态探针而非输出置信度，以及"可纠正性感知"和真正的 abstention。

6. [Reasoning Models Know When They're Right] (arXiv:2504.05419, 2025):
   - 隐状态探针用于推理正确性验证和提前退出，AUROC 0.77-0.91。
   - 关系：相邻工作，目标是正确性而非可纠正性。

7. [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox] (arXiv:2601.00828, 2026):
   - 弱模型纠错率是强模型的 1.6 倍；Error Depth Hypothesis。
   - 关系：为"哪些错误可纠正"提供了分类框架，proposal 在 Phase 3b 中使用。

8. [The Confidence Manifold] (arXiv:2602.08159, 2026):
   - 正确性仅占 3-8 个维度，线性可分，25 个标注样本即够。
   - 关系：proposal 质疑可纠正性（二阶属性）是否共享此低维结构。

- 调研总结：LLM 自纠错是 2025-2026 的活跃领域，已有大量工作分别解决了(a)正确性预测（Gnosis, Confidence Manifold）、(b)探针门控（早退/abstention）、(c)置信度路由（CoRefine）、(d)SAE 特征分解。PANL 论文首次将"可纠正性"作为独立预测目标，但仅用最简探针。本 proposal 处于这些工作的交汇处，核心差异化在于将"可纠正性"（而非正确性）作为预测目标并结合多种已有技术。
```

```
【Trivial Alternative 检验】:

存在两个需要认真对待的 trivial alternative：

(1) **直接用输出层置信度做门控**：CoRefine 已经用 211K 参数的 Conv1D 控制器在输出置信度上实现 92.6% 的 halt 精度。如果 proposal 的隐状态探针最终只能达到 AUROC 0.70-0.75，其相对于简单置信度路由的增量价值可能非常有限。Proposal 的反驳是"置信度不区分可纠正与不可纠正错误"，但这需要实验证明此区分在实践中确实带来显著收益。

(2) **用已有的高性能正确性探针 + 经验纠错率估计**：Gnosis 在正确性预测上达到 0.80-0.95 AUROC。一个更简单的方案是：用正确性探针检测错误 → 对所有检测到的错误尝试纠正 → 用经验成功率事后评估。这跳过了"预测可纠正性"这一中间步骤。Proposal 的增量价值取决于可纠正性预测是否比"检测错误后直接尝试纠正"显著更好。

增量价值评估：proposal 的真正增量在于 (a) 避免对不可纠正错误浪费计算、(b) 避免纠正正确答案导致的 overcorrection、(c) 在不可纠正错误上 abstain。这些都有实际价值，但需要探针 AUROC 足够高才能兑现。如果 AUROC 仅从 0.614 提升到 0.70，trivial alternatives 可能接近甚至等效。
```

```
【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的环节：

(1) **多层集成从欺骗检测到可纠正性预测的迁移性**：这是整个技术方案的基石假设。欺骗检测中信息跨层旋转的现象在可纠正性预测中是否成立完全未知。可纠正性是一个"二阶属性"——不仅需要编码"模型错了"，还需要编码"模型有能力纠正"。这种复合信号可能不像欺骗那样在层间有互补编码。Proposal 诚实地承认了这一点并设计了 Phase 0 pilot，这是好的，但如果 pilot 失败，主要技术贡献就大幅缩水。

(2) **可纠正性在内部表示中有足够强的可提取信号**：0.614 AUROC 的基线非常弱。一个根本性的可能是：可纠正性天然就不在模型的内部表示中被强编码——因为模型在生成初始答案时并不需要"知道自己的错误是否可修复"，这个信息可能根本就没有被学习到。如果可纠正性的信号上限本身就很低（比如 AUROC 0.72），那么再精细的探针设计也无济于事。

(3) **SAE 混合特征对可纠正性的特殊相关性**：arXiv:2604.19974 的发现是关于"正确性"和"不确定性"的，而非"可纠正性"。将该框架直接外推到可纠正性是一个类比推理，缺乏直接证据。可纠正性可能有完全不同的特征编码结构。

(4) **三路门控的实际效用依赖于探针质量的假设阈值**：proposal 声称在"某个 AUROC 阈值以上"门控优于非门控纠正。但如果这个阈值高于探针能达到的水平，整个系统设计就失去了实际意义。
```

```
【3 维度打分】:

1. Novelty: 【中】
   理由：核心创新在于将"可纠正性"（而非正确性）作为独立预测目标——这确实是 PANL 论文（arXiv:2604.22271）之后的自然延伸，且目前无人做过系统性的增强探针研究。然而，技术手段几乎全部借鉴自已有工作：多层集成来自 arXiv:2604.13386，多信号融合路线与 Gnosis (arXiv:2512.20578) 高度同构，注意力熵来自 arXiv:2602.13699，SAE 分解来自 arXiv:2604.19974，三路门控框架来自 CoRefine (arXiv:2602.08948)。本质上是"将 5-6 种已有技术组合应用到一个新的预测目标上"。Phase 3b 的表示几何分析（可纠正性 vs 正确性的维度/线性可分性对比）是较为新颖的子贡献，但并非文章的核心 claim。审稿人很可能认为这是 "solid engineering + interesting target" 而非 "novel methodology"。

2. Significance: 【中】
   理由：自纠错是 LLM 部署中的重要问题。区分"可纠正"与"不可纠正"错误有实际价值——避免浪费计算、避免 overcorrection、在不可修复时 abstain。然而，实际影响力受限于两点：(a) 如果探针 AUROC 仅达到 0.70-0.75（高于 0.614 基线但仍然中等），实际部署价值有限——CoRefine 用更简单的方法可能达到类似效果；(b) 即使探针 AUROC 达到 0.85+，核心发现也是"多信号探针比单层探针好"——这在正确性预测中已被 Gnosis 等多篇论文反复验证，迁移到可纠正性预测并不令人意外（"I would have guessed this"）。最有意义的潜在发现是 Phase 3b 中"可纠正性作为二阶属性是否有不同的表示几何"——如果答案是 yes，这对 LLM 内部表示的理解有贡献；但这被定位为"即使主实验失败也能发的 fallback contribution"，暗示作者自身也认为其独立份量有限。

3. Related Work: 【强】
   理由：这是本 proposal 最突出的优势。对 25+ 篇近期论文的覆盖极为详尽，包括 PANL (arXiv:2604.22271)、多层集成 (arXiv:2604.13386)、SAE 分解 (arXiv:2604.19974)、CoRefine (arXiv:2602.08948)、Gnosis (arXiv:2512.20578)、Reflective Confidence (arXiv:2512.18605)、Confidence Manifold (arXiv:2602.08159) 等。每篇论文都给出了具体数字和明确的差异化定位。与最直接竞争者 CoRefine 的三点区分（信号来源、abstention 能力、可纠正性感知）清晰合理。对四篇 concurrent probe-gating 论文的定位同样精确。经调研验证，引用论文真实存在，数字描述准确。
```

```
【概率估计】: [20% - 32%] 中位 25%
（注：此概率基于投稿至合适的 NLP/ML 会议如 EMNLP/NeurIPS。若投稿 CoRL，概率接近 0%——desk reject。）

【估计理由】:
Related Work 维度是强项（充分的覆盖和差异化定位），但这只保证了形式完备，不决定中稿。

概率上界受 Novelty 限制：核心技术路线是"将已有探针技术组合应用到可纠正性这个新目标"——这是 application novelty 而非 methodological novelty。如果多信号探针在可纠正性上也能 work（AUROC 显著提升），审稿人大概率会说 "interesting result but unsurprising approach"；如果 work 不了（AUROC 仅微幅提升），则主要贡献退化为 Phase 3b 的表示分析——一个 negative result + geometry analysis 的组合，份量不足以撑一篇顶会主会论文。

概率下界受 Significance 支撑：可纠正性作为预测目标的独立价值确实存在，Phase 3b 的二阶属性表示分析有学术趣味，dual-outcome 设计保证了最低发表可能性。

中位 25% 的核心判断：idea 方向正确，有真实的增量 novelty（可纠正性作为独立目标 + 表示几何对比），但核心发现若为正面结果（"多信号探针确实提升了可纠正性预测"），审稿人会说 "I would have guessed this"——因为正确性预测领域已经反复证明了多信号优于单信号。真正的 surprise 需要来自 Phase 3b（可纠正性有截然不同的表示结构），但这被定位为 secondary contribution。

【主要风险】:
1. **Trivial alternative 威胁**：CoRefine 用输出层置信度 + 211K 参数控制器已实现 92.6% halt 精度。如果 proposal 的隐状态探针无法大幅超越这一简单基线在实际任务指标上的表现，reviewers 会质疑"为何不直接用 logprobs"——尤其考虑到隐状态探针需要中间层提取，部署成本更高。
2. **可纠正性信号天花板过低的根本性风险**：0.614 AUROC 的基线极弱，可能反映的不是探针设计的问题，而是可纠正性信号本身在内部表示中编码就很弱——模型在生成答案时不需要"知道自己的错误是否可修复"。如果信号天花板本身就在 0.72-0.75，那么无论多精细的探针都无法产生有实际意义的门控收益，而整篇论文的叙事结构就会崩塌。
```

---

**附注 - 会议选择建议**：本 proposal 应投稿至 NLP/ML 会议。按匹配度排序：
1. **EMNLP 2026**（最佳匹配——LLM 内部表示 + 自纠错是 EMNLP 核心主题）
2. **NeurIPS 2026**（如果 Phase 3b 表示几何分析有强结果，偏 representation learning 方向）
3. **ICLR 2027**（如果强调 probing methodology + representation analysis）
4. **COLM 2026**（专注语言模型的新会议，高度相关）

Sources:
- [How LLMs Detect and Correct Their Own Errors (PANL)](https://arxiv.org/html/2604.22271v1)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)
- [Can LLMs Predict Their Own Failures? — Gnosis](https://arxiv.org/abs/2512.20578)
- [CoRefine: Confidence-Guided Self-Refinement](https://arxiv.org/abs/2602.08948)
- [Reasoning Models Know When They're Right: Probing Hidden States](https://arxiv.org/html/2504.05419v1)
- [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox](https://arxiv.org/html/2601.00828)
- [The Confidence Manifold](https://arxiv.org/abs/2602.08159)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
调研完成。现在我有足够的信息进行客观评估。

---

```
【阶段】: Triage

【⚠️ 致命前置问题：投稿venue完全不匹配】

CoRL (Conference on Robot Learning) 2026 明确声明："Submissions without a robotics focus 
will be returned without review." 本 proposal 是一篇纯 NLP/mechanistic interpretability 论文
（LLM 内部表征探测 + 自我纠错门控），与机器人学习完全无关。

→ 投稿 CoRL 2026 的中稿概率：≈0%（desk reject，不进入审稿流程）。

适合的venue：ACL、EMNLP、NeurIPS、ICML、ICLR 的 NLP/interpretability track。
以下评估假设投稿至适当的 NLP/ML 主会（如 ACL/EMNLP 2026 或 NeurIPS 2026）。

═══════════════════════════════════════════════════════════════

【领域调研】:

- arXiv:2604.22271 "How LLMs Detect and Correct Their Own Errors" (2026): 
  本 proposal 的直接前驱。已建立 PANL（post-answer newline）token 处的 correctability 
  信号，在 own-generated errors 上达到 0.614 AUROC。该论文已将 correctability 作为一个
  distinct prediction target 从 error detection 中分离出来。proposal 的核心概念贡献
  （correctability as a prediction target）在此论文中已被 operationalize。

- arXiv:2604.13386 "Linear Probe Accuracy Scales with Model Size and Benefits from 
  Multi-Layer Ensembling" (2026): 
  proposal 的主要技术灵感来源。在 deception detection 上 multi-layer stacking 将 AUROC 
  从 0.510 提升至 0.910（+78%）。但该工作针对的是 deception，其 layer-wise encoding 
  特性与 correctability 可能有本质差异。

- arXiv:2604.19974 "Are LLM Uncertainty and Correctness Encoded by the Same Features?" 
  (2026): 
  SAE 分解发现 uncertainty 和 correctness 由功能上不同的 feature population 编码。
  proposal 将此框架 extend 至 correctability（二阶属性）。但原论文针对的是 correctness
  （一阶属性），transferability 是未经验证的假设。

- arXiv:2602.08948 "CoRefine" (2026): 
  已实现基于 output-level confidence 的三路由自修正，211K 参数控制器达到 92.6% halt 
  precision，~190× token reduction。proposal 声称的差异化（hidden-state vs. output 
  logprobs, 真正的 abstention, correctability-aware）是成立的，但 CoRefine 的实际效果
  已经相当强，增量价值需要实验证明。

- arXiv:2512.18605 "Reflective Confidence" (2025): 
  将低 confidence 信号转化为 reflection trigger，在 AIME 2025 上达 83.3%（vs. 70.0% 
  Self-Consistency）。使用 output-level logprobs，未建模 correctability。

- arXiv:2602.08159 "The Confidence Manifold" (2026): 
  correctness 在 activation space 中占据 3-8 维，线性可分。proposal 计划测试 
  correctability 是否共享此结构。这是 proposal 中最有潜在 insight 的部分。

- arXiv:2512.20578 "Gnosis" (2025): 
  multi-signal fusion for correctness prediction, hidden-only 0.78-0.92 AUROC。
  为 correctness 而非 correctability，但技术路线相似。

- arXiv:2507.12379 / arXiv:2504.05419 / arXiv:2604.18419 / arXiv:2506.12217 (2025-2026): 
  四篇 concurrent probe-gating 论文分别探测 arithmetic errors、early exit、dynamic 
  abstention、self-reflection。均未针对 correctability，但方法论上高度相似。

- 调研总结: 2025-2026年出现了一个快速增长的子领域——用 LLM 内部表征探测来辅助自修正
  决策。PANL paper 已将 correctability 概念化，多篇 probe-gating 论文已从不同角度实现
  了 probe→decision 的 pipeline。本 proposal 处于这个快速拥挤的 landscape 的自然延伸
  位置——将多种已有技术（multi-layer ensembling, SAE feature analysis, probe-gating）
  组合应用于 correctability 这个已被定义但未被充分探索的 target。


【Trivial Alternative 检验】:

存在多个 trivial/simpler alternatives：

1. **直接在 PANL probe 上做 multi-layer 扩展**：只需在 PANL paper 的代码基础上训练
   每层的 logistic regression 再 stack，无需任何新的 framework。这个 trivial baseline
   就能回答 proposal 的核心问题（multi-layer ensembling 是否提升 correctability AUROC）。
   Proposal 的 Phase 0 本质上就是这个 trivial experiment。

2. **Output-level confidence thresholding**：CoRefine 已证明 output logprobs 可以做
   有效的三路由，92.6% halt precision。如果 hidden-state probe 只比 logprobs 好 2-3 
   个 AUROC 点，其工程复杂度的增量价值很难justify。

3. **Wait baseline 的 overcorrection 测量**：只需在 correct answers 上跑一遍 Wait 
   baseline 即可，这是一个 weekend experiment，不需要整个 ECP framework。

增量价值在于：如果 ECP 能将 correctability AUROC 从 0.614 显著提升（如 >0.80），且
hidden-state probe 明确优于 output-level confidence，那么三路门控的实际效用才能被
justify。但这是一个 empirical bet，而非 conceptual advance。


【前提假设检验】:

核心逻辑链中有 3 个未经验证的关键假设：

1. **"Correctability 信息充分编码在 internal representations 中"** — PANL paper 
   仅达到 0.614 AUROC，这可能不是 probing 方法的问题，而是信息本身就不够。
   Correctability 是一个 second-order property（不仅要"错"，还要"能纠正"），
   模型可能根本没有在内部充分编码这个信息——因为它在训练中没有被优化来做这件事。
   这是一个 information-theoretic ceiling 问题，不是 extraction 问题。

2. **"Multi-layer ensembling 从 deception detection 可迁移至 correctability"** — 
   Deception 的 layer-wise encoding 有其独特性（模型"知道"真相但选择撒谎，不同层
   编码 ground truth vs. deceptive output），而 correctability 涉及模型自身纠错
   机制的能力判断，编码模式可能完全不同。Proposal 诚实地承认了这是 hypothesis，
   但整个 Phase 1 的前提就建立在这个迁移上。

3. **"SAE confounded features 是 correctability probing 的有效 substrate"** — 
   arXiv:2604.19974 的发现是关于 correctness（一阶属性），correctability 作为
   二阶属性是否也集中在 confounded features 中完全是推测性的。如果 correctability
   的信息分布模式与 correctness 不同，整个 SAE-guided approach 就失去了理论基础。


【3 维度打分】:

1. Novelty: 弱-中 (Weak-to-Medium)
   
   理由：Proposal 的 5 个 claimed contributions 逐一分析：
   
   (1) "Operationalizing correctability as a prediction target" — 已由 PANL paper 
   (arXiv:2604.22271) 完成。该论文明确将 correctability 从 error detection 中分离
   并建立了 baseline probe。Proposal 是在此基础上的改进，不是概念首创。
   
   (2) "Multi-layer ensembling transfer to correctability" — 这是 arXiv:2604.13386 
   的技术在新 domain 上的直接应用。方法本身无新意，novelty 仅在于"试了一下看行不行"。
   
   (3) "Hidden-state probe-based gating with abstention" — probe-gating 已有 4 篇 
   concurrent papers (arXiv:2507.12379, 2504.05419, 2604.18419, 2506.12217)。
   Abstention 是 arXiv:2604.18419 的核心贡献。Correctability-specificity 是新的
   组合点，但不是新方法。
   
   (4) "Representational geometry of correctability" — 这是 proposal 中真正有潜力
   的部分。将 Confidence Manifold (arXiv:2602.08159) 的方法论 extend 到 second-order 
   property 并与 SAE 分析结合，可能产生有意义的 insight（如发现 correctability 需要
   更高维度/非线性边界）。但方法论本身是已有的，新意在于分析对象。
   
   (5) "Threshold analysis" — 这是标准的 engineering analysis，不构成 novelty。
   
   总结：每个 component 都是已有技术的 transfer/组合，conceptual novelty 有限。
   最有新意的是 Phase 3b 的表征几何分析，但独立来看也是已有方法的 straightforward
   extension。整体是"组合创新"而非"概念创新"。

2. Significance: 中 (Medium)
   
   理由：Selective self-correction 是一个实际重要的问题，尤其在 LLM 部署场景中。
   但关键的 "surprising" 检验失败了：
   
   - 如果 ECP 成功提升 AUROC（如 0.614→0.75+），审稿人反应大概率是 "makes sense, 
     combining more features helps" 而非 "surprising"。
   - 如果 ECP 未能大幅提升，审稿人反应是 "correctability may simply not be well-encoded, 
     as the authors themselves anticipated"。
   - 表征几何分析如果发现 correctability 需要更高维度，审稿人反应是 "expected, given 
     it's a second-order property"。
   
   无论结果如何，都难以产生 "I didn't expect this" 的反应。这限制了 significance 的
   上限。此外，practical impact 取决于 probe AUROC 能否达到 actionable 水平（~0.80+），
   这是高度不确定的。

3. Related Work: 强 (Strong)
   
   理由：这是 proposal 最突出的优点。引用了 25+ 篇高度相关的论文，且对每篇的描述
   经我调研验证后是准确的（PANL 的 0.614 AUROC、arXiv:2604.13386 的 0.510→0.910、
   CoRefine 的 92.6% halt precision、arXiv:2604.19974 的 confounded features 等数据
   均与原文一致）。与 CoRefine 的三重差异化（signal source、abstention、correctability-
   awareness）定位清晰。与 4 篇 concurrent probe-gating papers 的差异化也合理。
   对自身假设的不确定性有诚实的 hedge（如反复强调 multi-layer ensembling 的迁移是
   hypothesis）。但需注意：thorough related work ≠ idea 本身有 novelty。


【概率估计】: 

⚠️ 投稿 CoRL 2026：0-5%（desk reject，venue 完全不匹配）

若投稿适当 NLP/ML venue（ACL/EMNLP/NeurIPS）：[18% - 28%] 中位 22%

【估计理由】: 

Idea 的核心是"把多种已有 probing 技术组合应用于 correctability 这个 adjacent target"。
这是一个方向正确、execution-heavy 但 conceptual contribution 偏薄的 proposal。

- Novelty 弱-中 是主要限制因素：5 个 contributions 中没有一个是 conceptual breakthrough，
  全部是 existing techniques 的 transfer/组合。最有 insight 潜力的 Phase 3b 表征几何
  分析只是 proposal 的一个 sub-component 而非主线。
  
- Significance 中 限制了上限：无论正负结果都不太可能让审稿人 "surprised"。这使得
  即使 execution 完美，也很难超过 30%。

- Related Work 强 提供了下限保障：如果 execution 优秀，thoroughness 可以防止直接被拒。

- Proposal 形式非常完善（dual-outcome design、8 baselines、Phase 0 pilot），但这
  恰恰体现了 proposal 的特点：工程完备性补偿了 conceptual thinness。一个真正 novel 
  的 idea 不需要这么多 hedging。

- 22% 中位概率对应 rubric 中 "idea 方向站得住脚但内核薄弱" 到 "有实质内核但发现不
  surprising" 之间的位置。

【主要风险】: 

1. **"Incremental combination" 批评**：审稿人最可能的拒稿理由是 "this combines existing
   probing methods (multi-layer ensembling, SAE features, attention entropy) and applies 
   them to a closely related target (correctability vs. correctness). Each component is 
   borrowed, and the combination lacks a unifying conceptual insight." 这不是 execution 
   能补救的——idea 层面的组合性 novelty 是结构性弱点。

2. **Information ceiling 风险**：如果 correctability 确实没有在 LLM internal representations
   中被充分编码（0.614 AUROC 可能就是接近 ceiling 而非 extraction 不足），那么无论
   用多复杂的 probe，AUROC 都不会大幅提升。此时 proposal 的主线 (Phase 1-2) 全部
   fail，只剩 Phase 3b 作为 negative-result contribution——但一个"发现 correctability
   不太可 probe"的 negative result 的 impact 有限。
```

---

**补充说明**：

关于 venue 选择，我必须明确指出：**这篇 proposal 投稿 CoRL 2026 会被直接 desk reject**。CoRL 官网 Call for Papers 明确要求 "submissions should focus on a core robotics problem" 且 "submissions without a robotics focus will be returned without review"。本 proposal 是纯粹的 NLP/mechanistic interpretability 工作，与机器人学习无任何关联。

如果要继续推进这个 idea，建议将目标 venue 调整为 **ACL 2026, EMNLP 2026, NeurIPS 2026, 或 ICLR 2027**（取决于 submission timeline）。在这些 venue 下，上述 18-28% 的概率估计才是有效的。

Sources:
- [How LLMs Detect and Correct Their Own Errors (PANL paper)](https://arxiv.org/html/2604.22271v1)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)
- [CoRefine: Confidence-Guided Self-Refinement](https://arxiv.org/abs/2602.08948)
- [Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction](https://arxiv.org/abs/2512.18605)
- [The Confidence Manifold](https://arxiv.org/pdf/2602.08159)
- [Can LLMs Predict Their Own Failures? (Gnosis)](https://arxiv.org/pdf/2512.20578)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Probing for Arithmetic Errors in Language Models](https://arxiv.org/pdf/2507.12379)
- [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox](https://arxiv.org/pdf/2601.00828)


【原始 proposal（允许参考但不是主要依据）】:
# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction

## Description
We investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.

## Core Problem
LLMs attempt correction on all detected errors equally, but ~64.5% of self-generated errors are uncorrectable. Recent work reveals a faint internal 'correctability' signal at the post-answer newline token (PANL), but it achieves only 0.614 AUROC on own-generated errors using a single-layer linear probe — barely actionable for reliable gating. Meanwhile, trivial interventions like appending 'Wait' reduce blind spots by 89.3% on known errors, but their overcorrection rate on correct answers is completely untested. Confidence-based controllers like CoRefine (arXiv:2602.08948) achieve efficient three-way routing (halt/rethink/explore-alternative) using output-level logprobs, but they do not distinguish between correctable and uncorrectable errors — treating all detected issues as potentially fixable. Critically, correctability is a second-order property — it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer — and recent SAE analysis (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations, with only rare 'confounded' features bridging both signals. It is unknown whether correctability — which inherently requires engaging both axes — shares the favorable geometric properties (low dimensionality, linear separability) that correctness exhibits, or whether it requires targeting the narrow confounded feature intersection. Can enhanced multi-signal probes substantially improve correctability prediction, what is the representational relationship between correctability, correctness, and uncertainty at the feature level, and under what conditions does probe-gated correction with genuine abstention outperform both ungated correction and simpler confidence-based alternatives?

## Opportunity
Three converging findings create a clear research opportunity: (1) The PANL paper (arXiv:2604.22271) establishes that correctability is partially encoded in internal representations, but their single-layer, single-token linear probe barely exceeds chance (0.614 AUROC) on own-generated errors — leaving substantial room for improvement. For correctness prediction on adjacent tasks, Gnosis-style multi-signal fusion (arXiv:2512.20578) achieves 0.78–0.92 AUROC on hidden states alone (with the lower end on MMLU-Pro; ablation on Qwen3-1.7B only) and 0.80–0.95 with attention fusion, while attention-head entropy probes (arXiv:2602.13699) achieve +0.06 AUROC absolute improvement in OOD settings (0.70→0.76 average, 8.5% relative vs. Lookback Lens). Multi-layer probe ensembling (arXiv:2604.13386) has dramatically improved deception detection AUROC (0.510→0.910 on Harm-Pressure Knowledge in Llama-70B), though whether similar gains transfer to correctability — a fundamentally different property — is an open empirical question that motivates our pilot experiment. (2) The 'Wait' baseline from Self-Correction Bench (arXiv:2507.02778) is powerful but fundamentally non-selective: it was tested only on known errors, never on correct answers, so its overcorrection cost is unknown. QwQ-32B naturally generates 'Wait' as its first correction token 37.7–76.8% of the time depending on benchmark (SCLI5 to PRM800K-SC), but this behavior varies widely across models and is near-zero for non-reasoning models. Recent mechanistic work shows that internal states before Wait tokens causally modulate distinct reasoning patterns — restarting, recalling, uncertainty expression, and double-checking (arXiv:2510.04128, EMNLP 2025 Findings) — and that Wait token probabilities correlate with reasoning correctness in ways that vary by training strategy (arXiv:2601.17421). These findings suggest Wait's effectiveness is not uniform but depends on which reasoning pattern it triggers, creating an opportunity for probe-selective application. Reflective Confidence (arXiv:2512.18605) demonstrates a related approach, transforming low-confidence output signals into reflection triggers rather than stopping, achieving 83.3% accuracy on AIME 2025 vs. 70.0% for Self-Consistency — but uses only output-level logprobs, not internal representations. (3) Existing gating approaches occupy adjacent niches but leave a clear gap. CoRefine (arXiv:2602.08948) implements three-way routing (halt/rethink/alternative) via a 211K-parameter Conv1D controller on output-level confidence, achieving 92.6% halt precision — but its decisions are confidence-based rather than correctability-aware, and its ALTERNATIVE option explores different approaches rather than genuinely abstaining when errors are likely unfixable. Four concurrent probe-gating papers address correctness, early exit, abstention, or reflection control — but none probe for correctability (whether a specific error is fixable), and none combine hidden-state probes with genuine abstention in a correctability-aware framework. Moreover, the SAE dissociation paper (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations — with 68% of pure incorrectness features being causally inert and only rare confounded features (102 out of 1,057 in Llama-3.1-8B) bridging both signals to achieve 0.79 AUROC with just 3 features. This finding directly challenges naive linear probing over broad activations and suggests correctability prediction may need to target the narrow confounded feature intersection, motivating our SAE-guided probe design and representational analysis.

## Related Work / Landscape
The PANL paper (arXiv:2604.22271) establishes correctability prediction as a distinct task from error detection, achieving 0.986 AUROC for detection but only 0.614 for correctability on own-generated errors using single-layer logistic regression at one token position. This gap — high detectability but low correctability prediction — is the central technical challenge. Gnosis (arXiv:2512.20578) achieves 0.80–0.95 AUROC for correctness prediction by fusing final-layer hidden states with attention-map features via a ~5M-parameter architecture; notably, the hidden-state stream alone achieves 0.78–0.92 AUROC (with the lower end on MMLU-Pro; ablation only reported for Qwen3-1.7B), with attention fusion adding 0–3 points depending on the task. The multi-layer ensembling paper (arXiv:2604.13386) shows that logistic stacking across complementary layers can dramatically improve probe performance — achieving 0.510→0.910 AUROC on the hardest deception detection task (Harm-Pressure Knowledge, Llama-70B) — because informative directions rotate across layers and double-fault analysis reveals complementary error patterns between early and late layers. However, this result is specific to deception detection, which has different layer-wise encoding properties than correctness or correctability; whether analogous gains transfer is an empirical hypothesis we test via a Phase 0 pilot. For correctness prediction specifically, multi-signal approaches show more modest but consistent gains: attention-head entropy probes (arXiv:2602.13699) improve OOD AUROC by +0.06 absolute (0.70→0.76 average across 5 models, an 8.5% relative improvement over Lookback Lens), and perturbation-stability probes (arXiv:2505.21772) add +6 AUROC points via targeted adversarial perturbations to hidden states. SWIFT (arXiv:2505.12225) concatenates all-layer hidden states with learned gating weights to extract token-level quality signals.

The Self-Correction Bench (arXiv:2507.02778) documents the 64.5% blind spot and shows 'Wait' reduces it by 89.3%. QwQ-32B naturally generates 'Wait' as its first correction token at rates varying by benchmark (37.7% on SCLI5, 72.5% on GSM8K-SC, 76.8% on PRM800K-SC), but this behavior is model-specific — other reasoning models show different patterns and non-reasoning models rarely generate Wait spontaneously. The Wait baseline was never tested on correct answers, leaving the overcorrection cost unknown. Two recent papers provide mechanistic understanding of Wait tokens: arXiv:2510.04128 (EMNLP 2025 Findings) trains crosscoders on DeepSeek-R1-Distill-Llama-8B to identify features that promote or suppress Wait tokens, discovering causal features for distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) via activation steering at layer 15; arXiv:2601.17421 systematically analyzes Wait and other discourse tokens across model scales and training strategies, finding that Wait token probabilities correlate with reasoning correctness but that models exploit this signal only partially. Reflective Confidence (arXiv:2512.18605) proposes a related approach, transforming low-confidence output-level logprob signals into reflection triggers rather than early stopping, achieving 83.3% accuracy on AIME 2025 (vs. 70.0% Self-Consistency, K=32) on Qwen3-8B — demonstrating that selective confidence-gated correction can significantly outperform non-selective baselines, though it uses output-level signals rather than internal representations and does not model correctability.

CoRefine (arXiv:2602.08948) is the closest existing system to our three-way gating, implementing halt/rethink/alternative decisions via a 211K-parameter Conv1D controller that consumes output-level confidence traces from the frozen LLM. It achieves 92.6% halt precision, averages 2.7 refinement steps per problem, and reduces tokens ~190× relative to 512-sample baselines on mathematical reasoning benchmarks. However, CoRefine differs from our proposal in three fundamental ways: (a) it uses output-level logprobs rather than hidden-state probes, missing the richer internal signal that PANL demonstrates exists; (b) its HALT decision accepts the current answer — it never genuinely abstains or flags for external intervention when errors are likely unfixable; (c) its routing is confidence-based, not correctability-aware — it cannot distinguish correctable from uncorrectable errors, treating all low-confidence outputs as potentially improvable. Four concurrent probe-gating papers occupy adjacent niches: arXiv:2507.12379 probes for arithmetic errors and selectively re-prompts (only 6–12% of detected errors actually get corrected); arXiv:2504.05419 uses probes for early exit from reasoning chains (AUROC 0.77–0.91 for correctness, not correctability); arXiv:2604.18419 trains value-function probes for dynamic mid-generation abstention; arXiv:2506.12217 uses activation steering to modulate self-reflection frequency. None of these probe for correctability specifically, and none combine hidden-state probes with genuine abstention in a correctability-aware framework.

A critical finding for our probing approach comes from arXiv:2604.19974, which uses sparse autoencoders to decompose LLM representations into functionally distinct feature populations. In Llama-3.1-8B, they identify 700 pure uncertainty features, 255 pure incorrectness features, and only 102 confounded features encoding both signals. The key insight is a functional dissociation: 68% of pure incorrectness features are causally inert (mean accuracy delta of -0.03% when suppressed), while pure uncertainty features are essential for model performance, and only confounded features bridging both axes are causally effective for correctness prediction — with just 3 confounded features from layer 18 achieving 0.79 AUROC. This has direct implications for correctability probing: correctability is inherently a joint uncertainty+correctness concept (the model must be wrong AND the correction mechanism must be able to reach the right answer), so probes targeting broad activation spaces risk relying on functionally inert incorrectness features. This motivates our SAE-guided feature analysis in Phase 3b and suggests that the confounded feature intersection — not the full activation space — may be the effective substrate for correctability prediction, potentially explaining why the single-layer PANL probe achieves only 0.614 AUROC.

The Confidence Manifold (arXiv:2602.08159) shows correctness occupies only 3–8 dimensions in activation space and is linearly separable with as few as 25 labeled examples. However, correctability is a second-order property: it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer given the model's knowledge state and reasoning pathways. The Interpretability-without-Actionability paper (arXiv:2603.18353) provides indirect evidence that this second-order property may be harder to capture: even with 98.2% detection AUROC, activation steering corrected only 20–24% of errors (concept-bottleneck steering) or 0% (SAE feature steering), revealing a 53-percentage-point knowledge-action gap. This suggests correctability may occupy a different — possibly higher-dimensional or non-linear — representational subspace than correctness, and the SAE dissociation finding (arXiv:2604.19974) provides a mechanistic explanation: correctability may require engaging the narrow confounded feature population rather than the broader (but functionally inert) incorrectness features. The Truth-as-a-Trajectory framework (arXiv:2603.01326) proposes that cross-layer displacement vectors capture properties that static single-layer probes miss, potentially relevant to second-order properties like correctability. The Accuracy-Correction Paradox (arXiv:2601.00828) shows weaker models achieve 1.6× higher correction rates and proposes the Error Depth Hypothesis — that stronger models make fewer but deeper errors that resist self-correction — providing a taxonomy of error correctable characteristics. The information-theoretic analysis of correlated errors (Preprints.org 202601.0892) formalizes bounds on self-correction when generator and evaluator share failure modes, motivating external probe-based gating as a mechanism to break the correlation. LLMs also encode problem difficulty as a linearly decodable property (arXiv:2510.18147, ρ ≈ 0.88), suggesting that related meta-cognitive properties may be extractable, though correctability's second-order nature makes direct analogy uncertain.

## Approach
We propose a four-phase study of correctability prediction and selective self-correction, including an explicit pilot to validate the multi-layer ensemble transfer hypothesis, SAE-guided feature analysis informed by the uncertainty-correctness dissociation (arXiv:2604.19974), and a contribution plan that is robust to negative results.

**Phase 0: Pilot Feasibility Study.** Before committing to the full experimental pipeline, we run a targeted pilot on the PANL paper's existing correctability labels (Gemma-3-27B, TriviaQA subset). We train independent logistic regression probes at each of the ~42 layers, identify complementary layers via double-fault analysis (following arXiv:2604.13386's methodology), and build a 3–5 layer stacked ensemble. This pilot directly tests whether the multi-layer ensembling technique that improved deception detection AUROC by up to 78% transfers to correctability prediction. Success criterion: if the ensemble achieves ≥0.70 AUROC (meaningful improvement over the 0.614 single-layer baseline), we proceed to Phase 1. If the ensemble plateaus below 0.70, we shift emphasis to the representational geometry and SAE feature analysis (Phase 3b), which remains a publishable contribution. Estimated cost: ~15 H100-hours (single model, single dataset, multi-layer extraction only).

**Phase 1: Enhanced Correctability Probes (ECP).** We move beyond the PANL paper's single-layer, single-token linear probe by developing multi-signal correctability probes. (a) Multi-layer ensemble: train independent logistic regression probes at each layer, select 3–5 complementary layers via double-fault analysis, combine via logistic stacking (following arXiv:2604.13386, but with the explicit caveat that this technique was validated on deception detection — our Phase 0 tests transfer to correctability). (b) Multi-token features: concatenate hidden states from the post-answer newline token (PANL), the last answer token (LAT), and the last 2 reasoning tokens — the PANL paper's own causal analysis shows LAT carries complementary information at different layers. (c) Attention-based features: extract per-head entropy statistics across semantic sections (question, reasoning, answer), following the methodology of arXiv:2602.13699 which achieves +0.06 AUROC absolute improvement over Lookback Lens in OOD correctness prediction. (d) Wait-token features: inspired by the crosscoder analysis of arXiv:2510.04128, extract hidden-state features at the position immediately preceding natural Wait tokens (when present), capturing the causal features that modulate reasoning patterns (restarting, recalling, uncertainty expression, double-checking). The insight from arXiv:2601.17421 that Wait token probabilities correlate with reasoning correctness suggests these features encode meta-cognitive state relevant to correctability. (e) SAE-guided feature selection: motivated by arXiv:2604.19974's finding that only confounded features (encoding both uncertainty and correctness) are causally effective while pure incorrectness features are functionally inert, we train SAEs on our target models and identify confounded features relevant to correctability. We then compare probes trained on (i) full activation spaces, (ii) SAE-reconstructed activations from confounded features only, and (iii) SAE-reconstructed activations excluding pure incorrectness features. This tests whether the narrow confounded feature intersection — rather than broad activations — is the effective substrate for correctability prediction, and whether filtering out causally inert features improves probe AUROC. (f) Non-linear probe ablation: compare linear probes, 2-layer MLPs (hidden dim 16/32), and SWIFT-style all-layer gated aggregation — motivated by the possibility that correctability, as a second-order property, may require non-linear boundaries even if correctness is linearly separable in 3–8 dimensions (arXiv:2602.08159). All probes are trained on on-policy correctability labels generated by running the model's actual self-correction pipeline (multiple correction attempts per error to get calibrated fixability scores), avoiding the distribution mismatch of synthetic error injection documented in SCoRe (arXiv:2409.12917).

**Phase 2: Three-Way Gated Self-Correction.** Use the ECP to implement a three-way decision at inference time: (i) if the error detection probe indicates the answer is likely correct, retain the original answer; (ii) if the error is detected AND the correctability probe predicts high fixability (above a calibrated threshold), attempt correction — either prompting-based correction or probe-selective Wait insertion (applying Wait only when the probe detects both an error and high correctability, leveraging the mechanistic finding from arXiv:2510.04128 that Wait triggers different reasoning patterns depending on internal state); (iii) if the error is detected but correctability is predicted as low, abstain or flag for external intervention. This design is distinguished from CoRefine's (arXiv:2602.08948) three-way routing in three key ways: we use hidden-state probes rather than output-level confidence, our third option is genuine abstention (declining to answer) rather than exploring alternative approaches, and our gating is explicitly correctability-aware — routing based on predicted fixability rather than confidence level. Where CoRefine optimizes compute efficiency (achieving ~190× token reduction), our framework optimizes decision quality by preventing wasted correction attempts on unfixable errors and avoiding overcorrection of correct answers.

**Phase 3: Comprehensive Evaluation.** Evaluate across three dense models where probing is well-understood: Gemma-3-27B (same as PANL paper, validates signal transfer), Qwen-2.5-7B-Instruct (same as PANL paper, smaller scale), and Mistral-Small-3.2-24B (different architecture family, tests generalization). Use three benchmarks (TriviaQA, MMLU, GSM8K) with 10K+ questions each. Compare gated correction against eight baselines: (1) no correction, (2) ungated prompting-based correction, (3) Wait-appended correction applied to all answers — measuring the previously-untested overcorrection rate, (4) Wait-appended correction applied only to probe-detected errors, (5) confidence-threshold gating using log-probabilities (following Reflective Confidence's approach, arXiv:2512.18605), (6) CoRefine-style output-confidence routing (arXiv:2602.08948) — retrained on our models/benchmarks for fair comparison, (7) PAG-style generative verification (arXiv:2506.10406), (8) oracle gating (upper bound). Conduct ablations on: probe architecture (linear vs. MLP vs. ensemble vs. SAE-guided), feature sources (PANL-only vs. multi-token vs. +attention vs. +Wait-features vs. +SAE-confounded), layer selection, cross-task transferability, and threshold sensitivity analysis showing at what AUROC level gating begins to outperform ungated correction.

**Phase 3b: Representational Geometry and Feature Decomposition of Correctability (Robust to Negative Probe Results).** Regardless of probe performance, we conduct a dedicated analysis of the representational relationship between correctability, correctness, and uncertainty at the feature population level. (a) Subspace comparison: compute the principal components of correctness and correctability representations separately (following arXiv:2602.08159's methodology) and measure subspace alignment via principal angle analysis — testing whether correctability occupies the same 3–8 dimensional subspace as correctness or requires distinct dimensions. (b) Dimensionality analysis: determine how many dimensions encode correctability vs. correctness at each layer, and whether correctability requires higher dimensionality (consistent with its second-order nature). (c) Non-linearity characterization: compare linear vs. non-linear probe AUROC gaps for correctability vs. correctness — a larger gap for correctability would indicate it occupies a more complex geometric region. (d) SAE feature decomposition: train SAEs on our target models and decompose correctability-predictive features into pure uncertainty, pure incorrectness, and confounded populations (following arXiv:2604.19974's 2×2 framework). Test whether confounded features are disproportionately important for correctability prediction compared to correctness prediction — which would provide mechanistic evidence that correctability requires simultaneously engaging both uncertainty and correctness axes. Measure the causal efficacy of each population via suppression experiments: if suppressing pure incorrectness features has minimal effect on correctability prediction (paralleling the functional inertness finding for correctness), this confirms the narrow confounded intersection hypothesis and explains the representational ceiling for broad-activation linear probes. (e) Error depth analysis: using the Error Depth Hypothesis framework (arXiv:2601.00828), characterize what makes errors correctable vs. uncorrectable — surface-level errors (calculation mistakes, recall failures) vs. deep errors (fundamental misunderstanding, missing knowledge) — and test whether this taxonomy is reflected in representational distance and SAE feature activation patterns. (f) Cross-layer trajectory analysis: inspired by Truth-as-a-Trajectory (arXiv:2603.01326), examine whether correctability is better captured by cross-layer displacement vectors than by static single-layer activations, which would explain why single-layer probes struggle. This phase yields publishable insights regardless of whether the ECP achieves high AUROC, providing the first empirical characterization of how correctability is (or is not) represented in LLM internal states and the first application of the SAE uncertainty-correctness dissociation framework to a second-order property.

## Inspiration
The gap between 0.614 AUROC (single-layer PANL probe) and the consistently higher performance of multi-signal probes on correctness prediction (Gnosis hidden-only: 0.78–0.92; attention entropy: +0.06 AUROC absolute in OOD) suggests correctability prediction has room for improvement with better probing methodology — though the magnitude of potential gains is uncertain given correctability's second-order nature. The dramatic improvement from multi-layer ensembling on deception detection (0.510→0.910; arXiv:2604.13386) demonstrates that multi-layer stacking can rescue failing single-layer probes, but transferability to correctability is a hypothesis to test, not a guaranteed outcome. The SAE dissociation finding (arXiv:2604.19974) — that only rare confounded features bridging uncertainty and correctness are causally effective — provides both a challenge and an opportunity: correctability probes may need to target this narrow feature intersection, but successfully doing so could yield more principled and interpretable predictions than broad-activation probing. The untested overcorrection cost of the 'Wait' baseline, combined with new mechanistic understanding of Wait tokens' causal role in triggering distinct reasoning patterns (arXiv:2510.04128, arXiv:2601.17421), creates a clear opportunity for probe-selective Wait application. CoRefine (arXiv:2602.08948) demonstrates the viability of learned three-way routing for self-correction but uses output-level confidence without correctability awareness or genuine abstention — leaving a well-defined gap for hidden-state probe-based gating that distinguishes correctable from uncorrectable errors. Key untried combination: multi-signal enhanced probes for correctability prediction informed by SAE feature analysis + three-way gating with genuine abstention + comparison against Wait and confidence-based controllers, with explicit analysis of what makes correctability representationally distinct from correctness at the feature population level.

## Key References
- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (arXiv:2604.22271, 2026) — establishes PANL correctability signal, 0.614 AUROC baseline
- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in LLMs (arXiv:2507.02778, NeurIPS 2025 Workshop) — 64.5% blind spot, Wait baseline achieving 89.3% reduction; QwQ-32B generates Wait first-token at 37.7–76.8% depending on benchmark
- Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386, 2026) — multi-layer stacking on deception detection: +29% on Insider Trading, +78% on Harm-Pressure Knowledge (0.510→0.910 in Llama-70B); transfer to correctability is a hypothesis we test
- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits — Gnosis (arXiv:2512.20578, 2025) — multi-signal fusion for correctness prediction: hidden-only 0.78–0.92 AUROC (ablation on Qwen3-1.7B), fusion 0.80–0.95 AUROC
- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, 2026) — SAE decomposition reveals functionally distinct feature populations: 68% of pure incorrectness features are causally inert; only rare confounded features (102/1,057 in Llama-3.1-8B) bridge uncertainty and correctness, achieving 0.79 AUROC with 3 features from layer 18; directly informs our probe design and Phase 3b analysis
- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv:2602.08948, 2026) — three-way routing (halt/rethink/alternative) via 211K-parameter Conv1D controller on output-level confidence; 92.6% halt precision, ~190× token reduction; differs from our approach in signal source (output logprobs vs. hidden-state probes), decision type (no genuine abstention), and gating criterion (confidence vs. correctability)
- Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction (arXiv:2512.18605, 2025) — transforms low-confidence output signals into reflection triggers; 83.3% on AIME 2025 vs. 70.0% Self-Consistency; uses output-level logprobs, no correctability modeling
- Internal states before wait modulate reasoning patterns (arXiv:2510.04128, EMNLP 2025 Findings) — crosscoders identify causal features promoting/suppressing Wait tokens; distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) triggered by pre-Wait internal states
- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421, Jan 2026) — Wait token probabilities correlate with reasoning correctness; models exploit Wait signals only partially; implications for token-level steering
- Probing for Arithmetic Errors in Language Models (arXiv:2507.12379, 2025) — probe-guided selective re-prompting, 6–12% correction rate
- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv:2504.05419, 2025) — probe-gated early exit, AUROC 0.77–0.91
- Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning (arXiv:2604.18419, 2026) — value-function probes for abstention gating
- From Emergence to Control: Probing and Modulating Self-Reflection in Language Models (arXiv:2506.12217, 2025) — self-reflection vector steering
- The Confidence Manifold (arXiv:2602.08159, 2026) — correctness in 3–8 dimensions, 25-example sufficiency, linearly separable
- Attention Head Entropy of LLMs Predicts Answer Correctness (arXiv:2602.13699, 2026) — per-head 2-Rényi entropy achieves OOD AUROC 0.76 average (+0.06 absolute, 8.5% relative improvement over Lookback Lens)
- PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier (arXiv:2506.10406, 2025)
- Understanding the Dark Side of LLMs' Intrinsic Self-Correction (ACL 2025) — overcorrection and cognitive biases
- Interpretability without Actionability (arXiv:2603.18353, 2026) — knowledge-action gap: 98.2% detection AUROC but only 20–24% correction via steering, 53-point gap
- Mining Intrinsic Rewards from LLM Hidden States — SWIFT (arXiv:2505.12225, 2025) — all-layer gated aggregation
- Between the Layers Lies the Truth (arXiv:2603.22299, 2026) — cross-layer agreement features
- Truth as a Trajectory (arXiv:2603.01326, 2026) — cross-layer displacement vectors capture properties missed by static single-layer probes
- Training Language Models to Self-Correct via Reinforcement Learning — SCoRe (arXiv:2409.12917, 2024) — on-policy training data importance
- Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)
- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox (arXiv:2601.00828, 2026) — Error Depth Hypothesis: weaker models achieve 1.6× higher correction rates; deeper errors resist self-correction
- No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes (arXiv:2509.10625, ICLR 2026 Workshop)
- Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv:2505.21772, 2025) — +6 AUROC points via adversarial perturbation stability
- LLMs Encode How Difficult Problems Are (arXiv:2510.18147, 2025) — difficulty linearly decodable (ρ ≈ 0.88); meta-cognitive properties extractable but correctability's second-order nature makes transfer uncertain
- Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors (Preprints.org 202601.0892, Feb 2026) — formalizes bounds on self-correction with correlated generator-evaluator errors

## Resource Estimate
- **manual**: {'gpu_hours': '220–280 H100-hours (Phase 0 pilot: ~15 hrs; inference for 3 models × ~30K questions × 3 passes [initial + Wait + correction] + multi-layer hidden state extraction across ~10 layers + attention feature extraction + Wait-feature extraction + SAE training and feature decomposition + probe training + representational geometry analysis + ablations)', 'timeline': '11–13 weeks (includes pilot, SAE analysis, full experiments, geometry analysis, paper writing)', 'estimated_gpu_cost': '$550–700 (at ~$2.50/H100-hr on cloud providers)'}
- **human_in_loop**: {'gpu_hours': '220–280 H100-hours (same compute, faster iteration via AI-assisted code/analysis)', 'timeline': '8–10 weeks', 'claude_api_cost': '$150–210 (experiment orchestration, SAE analysis notebooks, geometry visualization, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$550–700'}
- **auto_research**: {'gpu_hours': '300–360 H100-hours (overhead from automated probe architecture sweeps, SAE training and decomposition, threshold optimization, representational geometry grid, and broader ablation grid)', 'timeline': '2–3 weeks wall-clock', 'claude_api_cost': '$420–580 (full pipeline orchestration, code generation, debugging, SAE analysis, statistical analysis, visualization, paper drafting)', 'estimated_gpu_cost': '$750–900', 'speed_bottleneck': 'Sequential multi-layer hidden state extraction over ~90K forward passes (3 models × 30K questions); extraction requires full-precision activations at 5–10 layers per pass and cannot be batched as aggressively as standard inference; SAE training adds ~20–30 H100-hours per model'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ba70acf2-8331-4ff1-b157-db7c58674f4d",
  "type": "user",
  "uuid": "980d2b84-45d6-4367-9713-faf846151116",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T19:03:19.169Z_

```json
{
  "parentUuid": "980d2b84-45d6-4367-9713-faf846151116",
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
  "uuid": "4ba6823c-b062-4e8f-af63-c58ac59cdd55",
  "timestamp": "2026-05-19T19:03:19.169Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T19:03:19.169Z_

```json
{
  "parentUuid": "4ba6823c-b062-4e8f-af63-c58ac59cdd55",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ac386af4-befb-4e6c-9aa6-aad53aa4227e",
  "timestamp": "2026-05-19T19:03:19.169Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information. Let me compile my assessment.…",
  "leafUuid": "ac386af4-befb-4e6c-9aa6-aad53aa4227e",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b"
}
```

---

### Assistant

_source line 8 · 2026-05-19T19:03:51.166Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully and produce the Meta Judge output.

## Extracting Key Data

### Reviewer 1:
- Novelty: 弱-中 (Weak-Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [15% - 30%] 中位 22%
- Fatal issue: CoRL venue mismatch (desk reject)
- Key risks: Signal ceiling, Novelty thinness ("incremental combination")
- Trivial alternative: CoRefine output-level confidence already strong


### Reviewer 2:
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [20% - 32%] 中位 25%
- Fatal issue: CoRL venue mismatch (desk reject)
- Key risks: Trivial alternative threat, correctability signal ceiling
- Trivial alternative: Output-level confidence + correctness probe + empirical correction rate

### Reviewer 3:
- Novelty: 弱-中 (Weak-Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [18% - 28%] 中位 22%
- Fatal issue: CoRL venue mismatch (desk reject)
- Key risks: "Incremental combination" criticism, information ceiling

## Consensus Analysis

All three reviewers converge on a 22-25% acceptance probability with extremely tight agreement (std ≈ 1.41%), and they unanimously flag the CoRL venue mismatch as a fatal desk-reject issue. Beyond that, there's consensus that novelty sits at weak-to-medium, significance is medium, and related work coverage is strong. The core technical concerns align across reviewers: the 0.614 AUROC likely reflects an information ceiling rather than extraction inadequacy, the approach combines existing techniques without sufficient novelty, and Phase 3b emerges as the most novel component but remains insufficient standalone. All three also identify the proposal as overloaded with multiple compensatory mechanisms that mask thin core novelty. R1 emphasizes the "kitchen-sink" nature more explicitly, while R2 suggests COLM 2026 as an alternative venue, and R3 articulates the "genuine abstention" critique more precisely.

Given this high convergence and the principle of "宁缺毋滥," I'm settling on a median of 22% with a narrow band of [18% - 30%], though the actual ranges from individual reviewers span [15% - 30%] to [20% - ...].
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac386af4-befb-4e6c-9aa6-aad53aa4227e",
  "isSidechain": false,
  "requestId": "req_011CbCSsFzEjqqb4cb8XFMV8",
  "type": "assistant",
  "uuid": "ecf85a4d-b7e3-4252-8b97-e3bcc894090f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzJnsHtR1qcwTsJosYpZXR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24466,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3328,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 24466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24466
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

_source line 9 · 2026-05-19T19:04:44.901Z_

【阶段】: Meta Judge
【三次中位】: [22%, 25%, 22%]  std=1.4%
【共识维度】:
- **CoRL 会议选择（致命）**: 3/3 一致判定 CoRL 2026 投稿将被 desk reject（proposal 与机器人学习完全无关）。此为致命前置问题，但以下评估假设投稿至合适的 NLP/ML 会议。
- **Novelty（弱-中）**: 3/3 一致认为核心是"已有探针技术（多层集成、SAE 分解、注意力熵、多 token）组合应用于 correctability 这个新 target"——application novelty 而非 methodological novelty。R1/R3 明确评"弱-中"，R2 评"中"但理由中同样指出"每个 component 都是借鉴"。
- **Significance（中）**: 3/3 一致。核心论点：无论正面结果（多信号探针提升 AUROC）还是负面结果（correctability 信号天花板低），都不太可能产生 "I didn't expect this" 的审稿人反应。
- **Related Work（强）**: 3/3 一致。25+ 篇论文覆盖详尽，引用数据准确，差异化定位清晰。但 3/3 均指出 "thorough related work ≠ novelty"。
- **信号天花板风险**: 3/3 一致标记 0.614 AUROC 可能反映的是 correctability 在内部表征中编码本身就弱（information-theoretic ceiling），而非探针方法不够好。
- **Trivial alternative 威胁**: 3/3 一致指出 CoRefine 用 output-level confidence 已达 92.6% halt precision，hidden-state 探针的增量价值需要实验证明且可能有限。
- **多层集成迁移不确定性**: 3/3 一致指出从 deception detection 到 correctability 的迁移是未经验证的核心假设。
- **Phase 3b 是最有新意的部分但份量不足独撑论文**: 3/3 一致。被定位为 fallback contribution 本身暗示主线信心不足。
- **"Incremental combination" 是最可能的拒稿理由**: 3/3 一致。

【异常维度】:
- R1 单独强调 "proposal 过于 kitchen-sink（4 phase + 6 探针变体 + 8 baseline），缺乏聚焦"——R2/R3 隐含但未显式判定。此观点有一定道理但非致命，适度降权。
- R2 单独提出 COLM 2026 作为备选 venue——合理但非评估核心，不影响概率。
- R3 单独指出 arXiv:2604.18419 已做 abstention（R1/R2 未特别强调此点对 novelty 的削弱），具有一定信号价值但影响有限。

【最终概率】: [18% - 28%] 中位 22%
【一致性】: 高（std=1.4%，远低于 3% 阈值；三份评审在所有核心维度判决一致）

【综合理由】:

三份评审在所有核心维度上高度收敛，无需处理分歧。最终中位取 22%（与 R1/R3 中位一致，略偏保守于 R2 的 25%），理由如下：

1. **Novelty 是概率天花板的决定因素**。三位审稿人一致认为：correctability 概念已由 PANL 论文建立，五个技术组件均来自已有工作，proposal 的贡献本质是"组合 + 迁移到新 target"。R2 给出略高评分（"中"）是因为承认 correctability 作为独立 target 的 framing 有一定价值，但这不足以改变"组合创新"的基本判定。Novelty 弱-中 将概率上限锁定在约 30%。

2. **Significance 中 进一步限制上界**。三位审稿人一致指出核心发现（无论正负）都缺乏 surprise：正面结果是 "expected improvement from better probing"，负面结果是 "correctability may not be well-encoded, as anticipated"。这使得即使 execution 完美，也难以突破 28-30%。

3. **信号天花板风险是最大的结构性不确定性**。0.614 AUROC 可能不是探针方法的问题，而是信息本身的上限。如果 correctability 在内部表征中本就编码很弱，整个 Phase 1-2 的叙事结构崩塌，论文退化为 negative result + Phase 3b 分析——份量不足撑顶会主会。

4. **Related Work 强提供了概率下限**。详尽的文献覆盖和诚实的 hedging 确保了形式完备性，加上 dual-outcome 设计，防止了被直接拒绝的最坏情况。下限 18%。

5. **CoRL 投稿是致命错误**。三位审稿人一致判定 desk reject，概率 ≈0%。上述 22% 仅在投稿 NeurIPS/EMNLP/ICLR 等合适会议时有效。

【建议】: 不推荐（中位 22% < 36% 阈值；Novelty 弱-中是结构性限制，难以通过迭代优化补救到 36%+；会议选择致命错位需首先修正）

【实施评估】:
  - 计算资源: 220–360 H100-hours（取决于自动化程度），约 $550–900 GPU 云成本。三个模型（Gemma-3-27B、Qwen-2.5-7B、Mistral-Small-3.2-24B）× ~30K 问题 × 多轮推理 + 多层 hidden state 提取 + SAE 训练。瓶颈在 ~90K forward pass 的全精度多层激活提取，无法高度并行化。
  - 数据需求: TriviaQA / MMLU / GSM8K（均公开可得），需自行生成 on-policy correctability labels（模型对自身错误运行多轮纠错），标注成本包含在 GPU 推理时间中。
  - 人工介入: 中等——Phase 0 pilot 结果需人工判断是否继续；SAE 特征分解需人工解读语义；Phase 3b 表征几何分析需可视化和定性分析。无需外部人工标注。
  - 训练需求: 探针训练本身轻量（logistic regression / 小 MLP），但 SAE 训练较重（每模型约 20–30 H100-hours）。不涉及 LLM 本体训练或微调。
  - 新 Benchmark: 不需要构建全新 benchmark，使用现有评测集。需要自行构建 correctability labels 数据集（通过运行模型自纠错 pipeline 生成），但这是实验流程的一部分，非独立 benchmark 贡献。
  - 预估周期: 手动 11–13 周，AI 辅助 8–10 周，全自动化 2–3 周（墙钟时间）。从启动到可投稿约 2–3 个月。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecf85a4d-b7e3-4252-8b97-e3bcc894090f",
  "isSidechain": false,
  "requestId": "req_011CbCSsFzEjqqb4cb8XFMV8",
  "type": "assistant",
  "uuid": "792b2b0a-8eb3-4bc5-8b7a-ecd414848647",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzJnsHtR1qcwTsJosYpZXR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24466,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3328,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 24466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24466
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information. Let me compile my assessment.…",
  "leafUuid": "792b2b0a-8eb3-4bc5-8b7a-ecd414848647",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "39641383-8072-41e0-abe9-cd597001473b"
}
```

---
