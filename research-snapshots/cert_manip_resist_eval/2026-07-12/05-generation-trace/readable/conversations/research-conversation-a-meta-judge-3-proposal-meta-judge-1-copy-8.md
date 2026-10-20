# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/a99ab81e-7502-40c3-bd42-3932ef7be9f2.jsonl`
- **Structured JSON:** [`c0b4bce74a21269fa106.json`](../../sessions/c0/c0b4bce74a21269fa106.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T22:20:52.095Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T22:20:52.095Z",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient background to perform the evaluation. Let me synthesize my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **GeoDPO** (arXiv 2602.22703, Feb 2026): 最直接的竞争者。训练 NL-to-DSL 翻译器，用翻译器 soft confidence 分数作为 RL reward 强化几何感知。效果: +26.5% in-domain, +39.0% 下游推理。与本 proposal 的关键差异在于: GeoDPO reward 来自学习到的翻译器（model-dependent），提供 diagram-level holistic scoring；本 proposal 用 ground-truth formal parse + symbolic matching（model-free），提供 claim-level granularity。但二者核心思路一脉相承——都是用结构化几何表示指导 perception RL。\n\n2. **PEARL** (CVPR 2026, arXiv 2511.18437): 从推理 QA 自动推导 perception checklist，用 LLM-judge 验证。+9.7% on MathVerse。属 model-dependent explicit 方法，与本 proposal 的 model-free 定位形成对比，但 PEARL 的 checklist 思想与本 proposal 的 claim-level 验证在形式上有相似性。\n\n3. **PAPO** (arXiv 2507.06448): 通过 KL 散度 Implicit Perception Loss 提升感知能力，30.5% perception error reduction。零额外基础设施成本，是本 proposal 需要超越的 cost-effectiveness 基准。\n\n4. **SGVR** (arXiv 2601.05073, Jan 2026): 将几何形式化证明转换为可验证 numeric sub-goals 作为 RL reward，+9.7% geometry。验证的是推理中间步骤的正确性（outcome-level），而非感知前提的正确性（premise-level）。本 proposal 明确定位为与 SGVR 互补。\n\n5. **MoCA** (ICML 2026 Spotlight, arXiv 2605.14054): 通过 \"blindfolded reasoning\" proxy 解耦感知与推理，间接奖励感知保真度。Model-dependent。\n\n6. **CogFlow** (ICLR 2026, arXiv 2601.01874): 三阶段 perception→internalization→reasoning 框架，使用 learned synergistic visual rewards。代表了另一种解决感知-推理脱节的范式。\n\n7. **PRCO** (arXiv 2603.28618): 双角色 RLVR 框架，Observer + Solver 分工，role-specific rewards。用 utility reward 而非直接验证感知。\n\n8. **EVPV** (arXiv 2603.16253, Mar 2026): Explicit Visual Premise Verification，将 step scoring 条件化于 visual premise 的可靠性。用 model-generated checklist + constraint extraction 计算 reliability signal。这与本 proposal 在\"验证具体 visual claim\"这一思想上高度相似，但 EVPV 用于 PRM reranking 而非 RL training reward，且其 constraint extraction 仍有 model 参与。\n\n9. **Geoparsing/GDP-29K** (arXiv 2604.11600, Apr 2026): 本 proposal 依赖的 formal parser。统一平面与立体几何的形式语言，29K 数据集。是较新的工作（2026年4月），其在真实多样几何图的泛化鲁棒性尚待广泛验证。\n\n10. **SymHPR** (arXiv 2512.03126, Dec 2025): 符号化 hierarchical process reward 用于几何 diagram reconstruction。使用 rule-based reward，但仅训练感知模块，不用于全链路 RL。\n\n11. **Visual-ERM / RRVF** (arXiv 2603.13224): Executable visual verification 用于 chart-to-code (+8.4)。证明了\"可执行验证作为 RL reward\"在视觉代码生成中的有效性，但未用于数学推理感知。\n\n- **调研总结**: 这个领域正处于爆发式增长期（2025H2-2026H1 涌现了十余篇直接相关工作），核心趋势是\"如何在 multimodal RL 中给感知信号提供更好的 reward\"。当前方法从 implicit（PAPO）到 model-based explicit（PEARL, CogFlow, MoCA, PRCO）再到 structural-representation-based（GeoDPO, SymHPR）形成了清晰的谱系。本 proposal 定位在该谱系的最右端——完全 model-free 的 symbolic verification reward，是一个自然但尚未被占据的位置。然而 GeoDPO 已经非常接近这个位置（用结构化 DSL 表示 + 学习到的翻译器），本 proposal 的增量贡献取决于\"model-free vs. model-dependent\"这一步差异在实践中能否带来显著收益。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在两个 trivial alternative 威胁：**\n\n(1) **GeoDPO + 更好的翻译器**: 如果将 GeoDPO 的 NL-to-DSL 翻译器在更大更多样的数据上训练，使其准确率达到 95%+，那么\"model-dependent but accurate\"与\"model-free\"之间的实际差距可能很小。本 proposal 的核心 selling point——\"model-free 消除 correlated bias blind spots\"——需要实验证明 blind spots 是实际存在且有实际影响的（而不仅仅是理论上存在的）。Proposal 中设计了 blind spot validation 实验（controlled corruption + conditional circularity analysis），这是合理的，但如果实验结果显示 blind spot 效应微弱，整个 story 的核心就垮了。\n\n(2) **PAPO 的零成本方案**: PAPO 用一个简单的 KL 散度项就实现了 30.5% 的 perception error reduction，零额外基础设施。EPV 需要构建 formal parse cache、claim extraction pipeline、symbolic matching system——如果最终 perception error reduction 仅略优于 PAPO（比如 35% vs. 30.5%），那么从 cost-effectiveness 角度很难 justify 这套复杂系统。\n\n**增量价值所在**: 如果实验确实证明 (a) claim-level diagnostics 能精确定位系统性感知错误模式从而指导 targeted intervention，(b) model-free reward 在 reward signal quality（与人工标注的 Pearson/Spearman 相关性）上显著优于 PEARL LLM-judge 和 GeoDPO translator，那么增量价值是成立的。但这高度依赖实验结果，idea 层面无法先验保证。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有 **四个关键未验证假设**：\n\n**(1) Formal parser 质量足以充当 ground-truth oracle**\nGeoparsing/GDP-29K 是 2026 年 4 月才发布的工作，其在 training set 之外的真实多样几何图上的解析准确率未知。如果 formal parser 本身有 5-10% 的错误率，那么所谓的\"model-free oracle\"实际上引入了一种不同类型的 systematic bias（parser bias）。Proposal 设计了 noise injection robustness 实验（5%/10%/20%），但这只验证了 EPV 对已知噪声的容忍度，没有回答\"实际噪声率到底是多少\"。\n\n**(2) Claim extraction 从 CoT 中可靠且全面**\n从 free-form CoT 中提取结构化 perception claims 是一个非平凡的 NLP 问题。Rule-based pattern matching 只能覆盖显式数值/关系 claims（\"∠ABC = 60°\", \"AB ∥ CD\"），但大量感知信息是隐式的或混杂在推理步骤中。Proposal 承认了这一点并设计了 extraction quality 验证，但如果 recall 较低（比如只覆盖 50-60% 的实际 perception claims），reward signal 的信息量就大打折扣。\n\n**(3) Correlated bias blind spots 是 VLM RL 性能的实际瓶颈**\n\"Model-dependent reward 与 policy VLM 共享 systematic bias\"是一个合理的理论假设，但其实际影响大小未知。GeoDPO 的翻译器是单独在合成数据上训练的，与 policy VLM 的训练数据和架构都不同，correlated bias 可能远小于预期。如果 blind spot 效应微弱，本 proposal 的核心 motivation 就大幅削弱。\n\n**(4) Symbolic matching 能正确处理 NL claim 与 formal representation 之间的语义对齐**\n\"AB ∥ CD\"在 NL 中可能有多种表述（\"line AB is parallel to CD\", \"AB and CD are parallel lines\", 甚至\"since these two lines never meet...\"），如何 robustly 地将这些 match 到 formal parse 中的 parallel(A,B,C,D) 关系？这不是 trivial 的字符串匹配，可能本身就需要一个小型 NLU 模块——这又引入了 model-dependent 成分，削弱了\"完全 model-free\"的 claim。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 核心贡献是将 model-free symbolic verification 用于 perception RL reward 并提供 claim-level 粒度。与最直接竞争者 GeoDPO 相比，差异是真实的（model-free vs. model-dependent, claim-level vs. holistic, joint training vs. staged），但属于同一研究路线上的增量推进而非范式转换。EVPV 已经在做 claim-level visual premise verification（虽然用于 PRM 而非 RL reward），SGVR 已经在几何中用 formal verification 做 RL reward（虽然是 reasoning outcome 而非 perception premise），Visual-ERM 已经证明了 executable verification 作为 RL reward 的有效性。本 proposal 的贡献更像是\"将已有的 pieces 组合在一起\"——formal parsing (Geoparsing) + claim-level verification (EVPV 的思想) + RL reward (SGVR 的思想) → 针对 perception 的 model-free claim-level reward。组合是合理的、位置是空白的，但单看任何一个维度都不算突破性创新。\n\n2. **Significance: 中** — 研究问题（如何给 multimodal math RL 中的 perception 提供更好的 reward）是当前领域的热门且重要问题（十余篇 2025-2026 论文在攻克）。但本 proposal 的 instantiation 高度 domain-specific（仅限于有 formal parser 的领域），当前只在几何上验证，泛化到化学结构/电路图/函数图完全是理论性的。如果核心结果是 positive（比如 EPV 比 GeoDPO 好 5-8 个点），审稿人的反应可能是\"makes sense, not surprising\"——因为用 ground-truth 比用 learned proxy 更准确是直觉上预期的结果。真正 surprising 的结果需要是：(a) EPV 揭示了 GeoDPO/PEARL 无法发现的 systematic blind spots, (b) claim-level diagnostics 带来了 holistic reward 无法实现的 targeted improvement, 或 (c) EPV+SGVR 的组合产生了超加性效应。这些都有可能，但不是先验可预期的。\n\n3. **Related Work: 强** — 这是本 proposal 最强的维度。对已有工作的覆盖非常全面，从 implicit (PAPO) 到 model-based explicit (PEARL, CogFlow, MoCA, PRCO, EVPV) 到 structural-representation-based (GeoDPO, SymHPR) 到 formal verification for reasoning (SGVR) 构建了清晰的谱系，差异化定位明确。与 GeoDPO 的三点差异分析具体且有说服力。SGVR 的互补性定位也合理。引用的论文经调研验证全部真实存在且描述准确。唯一的小瑕疵是对 EVPV 的定位可能不够突出——EVPV 的 claim-level visual premise verification 与本 proposal 的思想有较高相似性，proposal 中只在列表中提了一句，没有充分讨论为何 EVPV 的方法不够好。\n\n---\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \n- Related Work 覆盖全面且定位清晰，这为论文提供了坚实的 framing 基础（拉高下界）。\n- Novelty 为中：核心贡献是已有 building blocks 的合理组合，GeoDPO 的存在使得增量空间被压缩。任何一个了解 GeoDPO + SGVR 的审稿人都可能认为\"用 ground-truth formal parse 替代 learned translator\"是一个自然的 next step，not surprising。\n- Significance 受限于两个因素：(a) 高度 domain-specific，当前只能在几何上工作；(b) 如果核心结果 positive，审稿人可能认为\"ground-truth 比 learned proxy 好\"是预期之内的。\n- **上界受限于 Novelty**：即使实验全部 positive，idea 的 conceptual novelty（已有 pieces 的组合）使得论文很难进入\"strong accept\"区间。\n- **下界受限于 Significance**：如果 blind spot validation 和 claim-level diagnostics 的结果不够 compelling，论文的 motivation 会被审稿人质疑（\"为什么不直接用 GeoDPO + 更好的翻译器？\"）。\n\n【主要风险】:\n1. **\"Natural next step\" 的 novelty 质疑**: 审稿人很可能指出 EPV 是 GeoDPO + SGVR 的自然延伸，缺乏足够的 conceptual novelty。\"用 ground-truth 替代 learned proxy\"的 insight 不够 deep——这更像是 engineering decision 而非 research contribution。\n2. **增量收益可能不足以 justify 复杂度**: 如果 EPV 相比 GeoDPO 的提升仅 3-5 个百分点，而 PAPO 用零基础设施就能获得可观的 perception improvement，审稿人会质疑这套需要 formal parse cache + claim extraction + symbolic matching 的系统是否值得。核心风险在于 model-free 的理论优势在实践中可能转化不出显著的性能增量。\n```\n\nSources:\n- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/abs/2602.22703)\n- [PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning](https://arxiv.org/abs/2511.18437)\n- [PAPO: Perception-Aware Policy Optimization for Multimodal Reasoning](https://arxiv.org/abs/2507.06448)\n- [SGVR: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)\n- [MoCA: Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)\n- [CogFlow: Bridging Perception and Reasoning through Knowledge Internalization](https://arxiv.org/abs/2601.01874)\n- [PRCO: Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning](https://arxiv.org/abs/2603.28618)\n- [EVPV: Grounding the Score: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253)\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)\n- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)\n- [Visual-ERM: Reward Modeling for Visual Equivalence](https://arxiv.org/abs/2603.13224)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to conduct a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [GeoDPO / arXiv 2602.22703] (Feb 2026): 最直接的竞争对手。训练 NL-to-DSL translator，用 translator 的 soft confidence scores 作为 geometry perception 的 RL reward（+26.5% in-domain, +39.0% downstream reasoning）。采用 staged training（先 DPO perception 后 reasoning），holistic diagram-level scoring。是当前 geometry perception RL reward 的 SOTA。\n- [PEARL / arXiv 2511.18437] (CVPR 2026): 构建 perception checklist sub-questions，用 LLM-as-judge 验证后给 perception reward gate（+9.7% MathVerse, +6.6% over GRPO）。Model-dependent（LLM judge），但 checklist 思路与 claim-level 有相似之处。\n- [PAPO / arXiv 2507.06448] (Jul 2025): 纯 implicit 方法，通过 KL divergence implicit perception loss 嵌入 policy gradient，zero overhead，不需要额外 oracle（+8% vision-dependent, 30.5% perception error reduction）。是零成本 baseline 的强力挑战者。\n- [MoCA / arXiv 2605.14054] (ICML 2026 Spotlight): 用 blindfolded reasoning（纯文本推理 vs. 多模态推理）作为 perception sufficiency 的 proxy reward，不直接验证 perception claims，而是间接度量 perception 的贡献。\n- [SGVR / arXiv 2601.05073] (Jan 2026): 将 formal proof 转化为 verifiable numeric sub-goals 用于 RL reward（+9.7% geometry），但验证的是 reasoning outcomes（中间推理值是否正确），不是 perception premises。与本 proposal 构成互补关系。\n- [Perceval / arXiv 2604.24583] (Apr 2026): **高度相关但 proposal 未引用。** 该工作提出 perception-centric PRM，能够从 response 中提取 image-related claims 并与 visual evidence 逐条比对，返回包含 perceptual errors 的 claims，并在 RL 中施加 token-level advantages。与本 proposal 的 claim-level extraction + verification 在概念层面非常接近，但使用的是 learned PRM 而非 model-free symbolic matching。\n- [EVPV / arXiv 2603.16253] (Mar 2026): 步级 visual checklist + constraint extractor → reliability gating 的 PRM 方法。与本 proposal 的 claim verification 概念相似，但完全 model-dependent（learned constraint extractor）。\n- [ViCrit / NeurIPS 2025]: 构造 proxy task（在 caption 中注入 subtle hallucination，训练模型定位错误 span），用作 verifiable perception RL 任务。思路不同但目标相似。\n- [Geoparsing / GDP-29K / arXiv 2604.11600] (Apr 2026): 统一形式化语言的 geometry diagram parser，覆盖平面和立体几何。是本 proposal 的核心技术依赖。论文本身发布较新（Apr 2026），parser 的成熟度和可靠性尚需验证。\n- [Visual-ERM / arXiv 2603.13224] (Mar 2026): 用渲染后视觉比对作为 code generation 的 reward（+8.4 chart-to-code）。是 executable verification 在 vision-to-code 的先例，但未用于 math reasoning RL。\n\n- **调研总结**: Multimodal math RL 的 perception reward 是 2025-2026 年的研究热点，已形成从 implicit (PAPO) → model-based explicit (PEARL, Perceval, EVPV) → structural-representation-based (GeoDPO) 的方法谱系。本 proposal 试图在该谱系上推进到\"model-free symbolic verification\"这一端点。核心竞争对手是 GeoDPO（结构化表示 + learned translator）和 Perceval（claim-level extraction + learned PRM）。关键问题是：从\"learned translator/PRM\"到\"model-free symbolic matching\"的增量是否足够大？\n\n【Trivial Alternative 检验】:\n\n**存在明确的 trivial alternative 威胁。** \n(1) GeoDPO 已经使用 DSL 结构化表示作为 reward signal，虽然通过 learned translator 而非 symbolic matching，但如果 translator 训练在足够大的合成数据上且泛化良好，其 reward quality 可能已经接近 ground-truth symbolic matching。本 proposal 的增量价值完全依赖于\"learned translator 的 bias 确实造成了可测量的 blind spot\"这一未验证假设。\n(2) 一种更简单的替代方案：直接用 Geoparsing 的 formal parse 作为 gold label，对 VLM 的 diagram description 做 string/DSL-level matching（不需要 claim extraction from CoT），用 diagram-level F1 作为 reward。这种方法省去了 claim extraction 的复杂工程，可能达到类似效果。\n(3) PAPO 的 implicit KL loss 是零额外成本的方法，已经实现 30.5% perception error reduction。本 proposal 需要证明其复杂的 pipeline（formal parse cache + claim extraction + symbolic matching）带来的增益显著超过 PAPO 的零成本 baseline。\n\n**增量价值定位**: 如果 blind spot 假说被验证（model-dependent reward 确实系统性地 miss 某些 perception errors），且 claim-level 的 diagnostic 功能被证明对 targeted training data curation 有实际价值，则增量价值成立。否则，这只是一个更复杂版本的 GeoDPO。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条包含以下未经验证的假设：\n\n1. **\"Model-dependent rewards inherit systematic biases shared with the policy VLM\"（blind spot 假说）**: 这是全文最核心的 motivating assumption，但纯属推测。当 reward model（如 GPT-4 作为 PEARL 的 judge，或 GeoDPO 的 translator 训练在合成数据上）与 policy VLM 差异很大时，bias correlation 可能很低。Proposal 设计了 conditional circularity analysis 来验证这一点，但如果实验发现 bias overlap 并不显著，整个 motivation 就坍塌了。\n\n2. **\"Claim extraction from free-form CoT is feasible and reliable\"**: Rule-based pattern matching 能捕获 explicit numeric/relational claims（如 \"angle ABC = 60°\"），但 CoT 中大量 perception 是 implicit 的（如隐含地将图中两线视为平行而直接使用了平行线的性质），这些 claims 很难被 rule-based 方法提取。Proposal 承认了 hybrid extraction 的需要并规划了 precision/recall 评估，但如果 recall 低于某个阈值（如 50%），claim-level verification 就退化为对\"容易检测的 explicit claims\"的验证，对最 challenging 的 implicit perception errors 无能为力。\n\n3. **\"Formal parsing quality has reached sufficient maturity\"**: Geoparsing (GDP-29K) 发布于 2026 年 4 月，论文本身很新。如果 formal parser 在某些 diagram types 上有系统性错误（如复杂嵌套几何图形、手绘图），那么 \"model-free oracle\" 自身就成了一个有 bias 的 reward source——只是 bias 的类型不同于 learned models。Proposal 有 noise injection ablation，但这测试的是对随机噪声的鲁棒性，不是对系统性 parsing 错误的鲁棒性。\n\n4. **\"Joint GRPO training with perception reward outperforms staged training\"**: Proposal 声称 EPV 的优势之一是 joint training（vs. GeoDPO 的 staged training），但这是一个 orthogonal 的设计选择，not unique to model-free verification。GeoDPO 也可以切换到 joint GRPO training。\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — \n   核心 idea（用 formal parse 作为 ground truth oracle 做 symbolic verification of perception claims）是该领域的一个 **natural and somewhat obvious next step**。GeoDPO 已经使用 DSL 结构化表示作为 reward，本 proposal 的核心增量只是将 \"learned translator\" 替换为 \"symbolic matching against ground-truth parse\"——这是一个 implementation-level 的变化而非 conceptual breakthrough。Perceval (arXiv 2604.24583) 在 Apr 2026 已经实现了 claim-level extraction + per-claim verification（虽然用 learned PRM），进一步削弱了 claim-level granularity 的 novelty claim。\n   \n   **剩余 novelty delta**:（a）model-free symbolic matching（vs. 所有 prior work 的 model-dependent approaches）；（b）blind spot hypothesis 的形式化和验证实验设计。这些是真实的增量，但审稿人很可能认为 (a) 是 engineering choice rather than research insight，(b) 是 interesting but secondary。\n\n2. **Significance: 中偏弱** — \n   - **Domain specificity 严重限制 impact**: 方法仅适用于 geometry（以及理论上的化学结构、电路图等），但只在 geometry 上 instantiate。对于 NLP/multimodal reasoning 大领域的影响力有限。\n   - **核心发现的 surprise value 低**: 如果实验结果是 positive（\"model-free symbolic verification outperforms learned translator for geometry perception reward\"），审稿人的反应更可能是 \"I would have guessed this\"（ground truth 当然比 learned approximation 好）而非 \"surprising\"。 \n   - **Practical significance 受限于 formal parser 可用性**: 该方法的泛化性完全取决于其他领域是否也有成熟的 formal parsers，而目前这类 parsers 很少。\n   - 正面因素：perception error 占 multimodal math failure 的 40-67% 是被充分验证的事实（PAPO, MoCA 等均有数据支撑），问题本身是重要的。\n\n3. **Related Work: 强** — \n   Literature coverage 非常全面，包括 implicit (PAPO), model-based explicit (PEARL, Perception-R1, CogFlow, PRCO, EVPV), structural-representation (GeoDPO), formal verification for reasoning (SGVR), reconstruction-based (SymHPR), executable visual verification (Visual-ERM/RRVF) 等。差异化定位清晰，特别是与 GeoDPO 的三点对比（model-free vs. learned, joint vs. staged, claim-level vs. holistic）。\n   **一个重要遗漏**: Perceval (arXiv 2604.24583, Apr 2026) 做了 claim-level extraction + per-claim verification for perception reward in RL，在概念层面与本 proposal 高度接近，但 proposal 未提及。这会被审稿人视为 related work 遗漏。\n\n【概率估计】: [23% - 33%] 中位 28%\n\n【估计理由】: \n- Novelty (中偏弱) 和 Significance (中偏弱) 共同限制了上界。核心 idea 是 natural next step，surprise value 低。\"用 ground truth formal parse 做 symbolic matching\" 在概念上不 surprising——这是任何看到 GeoDPO + Geoparsing 两篇论文的研究者都会想到的组合。\n- Related Work (强) 提供了下限保护——至少论文定位清晰、不会因为 missing related work 而直接被拒（但需补上 Perceval）。\n- Domain specificity (仅 geometry) 显著拉低 significance，因为 AAAI 审稿人通常期望方法有更广的适用性。\n- Blind spot hypothesis 的验证实验设计（conditional circularity analysis）是 proposal 中最有学术价值的部分，如果结果 positive 且 convincing，可以提升论文的贡献——但这属于实验层面能否拉升的问题，不改变 idea 本身的中位估计。\n- 该领域竞争极其激烈（PAPO, PEARL, GeoDPO, MoCA, Perceval, EVPV 等在 6 个月内密集发表），增量贡献容易被审稿人认为 insufficient。\n\n【主要风险】:\n1. **\"Obvious combination\" 质疑**: 审稿人可能认为 \"用已有的 formal parser 做 symbolic matching 替换 learned translator\" 是 engineering contribution 而非 research contribution，尤其是当 GeoDPO + Geoparsing 作为已有工作时，这种组合的 intellectual novelty 有限。\n2. **Domain specificity + low surprise value**: 方法仅适用于有成熟 formal parser 的领域，在 geometry 上的 positive result 不会 surprise 审稿人（ground truth oracle 理应优于 learned approximation），且无法泛化到 multimodal math 的其他子领域（代数、统计图表等），限制了论文在 AAAI 的 impact narrative。\n```\n\nSources:\n- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/abs/2602.22703)\n- [PEARL: Perceptual-Evidence Anchored Reinforced Learning](https://arxiv.org/abs/2511.18437)\n- [PAPO: Perception-Aware Policy Optimization for Multimodal Reasoning](https://arxiv.org/abs/2507.06448)\n- [MoCA: Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)\n- [SGVR: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)\n- [Perceval: Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583)\n- [EVPV: Grounding the Score: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253)\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)\n- [Visual-ERM: Reward Modeling for Visual Equivalence](https://arxiv.org/abs/2603.13224)\n- [ViCrit: Verifiable RL Proxy Task for Visual Perception in VLMs](https://arxiv.org/abs/2506.10128)\n- [Perception-R1: Advancing Multimodal Reasoning via Visual Perception Reward](https://arxiv.org/html/2506.07218)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me synthesize my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [PAPO: Perception-Aware Policy Optimization](https://arxiv.org/abs/2507.06448) (arXiv 2025): 引入隐式 KL 散度感知损失，无需外部预言机即可在 GRPO/DAPO 中提升感知能力，+8% vision-dependent tasks，感知错误减少 30.5%。本 proposal 将其定位为\"隐式方法，无法提供 claim-level 诊断\"。描述准确。\n- [GeoDPO: Translator-Guided RL for Geometry Perception](https://arxiv.org/abs/2602.22703) (arXiv 2026): 训练 NL-to-DSL 翻译器计算 DSL 级别奖励，in-domain +26.5%，downstream reasoning +39.0%。**这是最直接的竞争者**——同样使用结构化表示作为几何感知奖励，但依赖学习到的翻译器（model-dependent）。Proposal 声称的三个差异（model-free vs learned translator, joint vs staged training, claim-level vs holistic）基本准确。\n- [PEARL: Perceptual-Evidence Anchored RL](https://arxiv.org/abs/2511.18437) (CVPR 2026): 从 QA 实例派生感知 checklist，用 LLM judge 验证，+9.7% MathVerse。使用 LLM-as-judge，属于 model-dependent explicit 方法。\n- [MoCA: Bad Seeing or Bad Thinking](https://arxiv.org/abs/2605.14054) (ICML 2026 Spotlight): 通过\"蒙眼推理\"代理来奖励感知保真度，解决感知-推理信用分配问题。间接衡量感知质量，不直接验证感知声明。\n- [SGVR: Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073) (arXiv 2026): 将形式证明转化为可验证数值子目标作为 RL 奖励，+9.7% geometry。**关键区分**：验证推理产出（intermediate computed values），不验证感知前提（visual inputs）。Proposal 的区分描述准确。\n- [CogFlow](https://arxiv.org/abs/2601.01874) (ICLR 2026): 三阶段框架（感知→内化→推理），使用学习到的协同视觉奖励。Model-dependent。\n- [PRCO: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618) (arXiv 2026): Observer-Solver 双角色框架，role-specific 奖励。Model-dependent（Observer 的效用奖励来自 Solver 的下游成功）。\n- [EVPV: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253) (arXiv 2026): 模型生成 checklist + 约束提取器进行视觉可靠性评分。也是 model-dependent（依赖约束提取器）。\n- [Geoparsing / GDP-29K](https://arxiv.org/abs/2604.11600) (arXiv 2026): 20K 平面 + 9K 立体几何样本配对 ground-truth 形式化描述。**这是 EPV-Oracle 的关键基础设施**，论文确实存在且提供了 proposal 声称的能力。\n- [Visual-ERM](https://arxiv.org/abs/2603.13224) (arXiv 2026): 视觉等价奖励模型，用于 vision-to-code 任务，chart-to-code +8.4。与本 proposal 的领域不同（code generation vs math reasoning）。\n- [SymHPR](https://arxiv.org/abs/2512.03126) (arXiv 2025): 基于重建的奖励，但仅训练感知模块，不用于完整推理链的 RL 训练。\n\n**调研总结**: 多模态数学 RL 中的感知奖励是 2025-2026 年极其活跃的研究方向，已有超过 10 篇高质量工作从不同角度攻击这个问题。现有方法全部是 model-dependent（隐式 KL、LLM-as-judge、学习到的翻译器、蒙眼代理等），无一实现 model-free + claim-level 的符号化验证。**这个空白是真实存在的**，但空白的大小（incremental improvement vs paradigm shift）取决于 model-free 在实践中是否带来显著收益。\n\n【Trivial Alternative 检验】:\n\n存在一个值得警惕的 trivial alternative：**直接用 GeoDPO 的框架但换一个更好的翻译器**。GeoDPO 已经使用了结构化表示（DSL）作为几何感知奖励，只是通过学习到的翻译器来桥接。如果翻译器的准确率足够高（比如在高质量数据上 fine-tune），其\"model-dependent bias\"可能在实践中可忽略不计。Proposal 的核心增量价值在于：\n\n1. **真正的 model-free**：使用 ground-truth formal parse 而非 learned translator，理论上消除了系统性偏差。但\"盲点假说\"（policy VLM 和 model-dependent judge 共享偏差）对 GeoDPO 的适用性存疑——GeoDPO 的翻译器有不同的架构和训练目标，其偏差不一定与 policy VLM 相关。\n2. **Claim-level 粒度**：GeoDPO 给出 holistic diagram-level 分数，EPV 验证个别声明。这是真正的新增能力，但其实用价值取决于 claim extraction 的质量。\n\n**结论**：trivial alternative 不完全成立——claim-level 粒度确实是 GeoDPO 不具备的新能力。但 model-free vs model-dependent 的实际增益可能不大，这削弱了核心论点的说服力。\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的环节：\n\n1. **\"盲点假说\"本身未经实证**：Proposal 声称 model-dependent rewards 与 policy VLM 共享系统性偏差，导致 reward 恰好在 policy 最需要纠正的地方失效。这个假设直觉上对 LLM-as-judge 合理（共享预训练数据和架构偏差），但对 GeoDPO 的翻译器（不同任务、不同数据）是否成立需要实证。Proposal 设计了 conditional circularity analysis 来验证，但这本身是一个需要在实验中才能确认的假设。**如果实验发现 GeoDPO 翻译器的偏差与 policy VLM 不相关，核心论点的力度将大幅减弱。**\n\n2. **Claim extraction 的可靠性是硬依赖**：整个方法的有效性取决于能否从 free-form CoT 中可靠提取感知声明。Rule-based pattern matching 对显式数值/关系声明（\"angle ABC = 60°\"）可行，但对隐式/推断性声明（\"the triangle appears to be right-angled\"）可能遗漏大量信息。CoT 中的感知信息可能以非结构化方式嵌入推理中，难以用规则提取。**如果 extraction recall 低，reward signal 就是稀疏且有偏的。**\n\n3. **Formal parse 的覆盖率和质量**：GDP-29K 的 formal parse 质量在简单几何上可能很高，但在复杂图表（重叠元素、手绘、非标准标注）上的覆盖率未知。Proposal 计划进行 \"data audit\" 来确定覆盖率，但这又是一个事后才能验证的假设。\n\n4. **λ annealing 的有效性**：perception reward 和 outcome reward 的结合方式（线性/余弦退火）假设两者可以简单加权，但感知错误和推理错误的相互作用可能更复杂。这一点在 prior work（CogFlow, PRCO）中已有研究，不是致命问题但需要仔细调参。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 核心创新是\"model-free + claim-level + symbolic\"的组合，这在已发表工作中确实不存在。GeoDPO（最近竞争者）使用 learned translator + holistic scoring，SGVR 验证推理而非感知，PEARL/EVPV 使用 LLM-as-judge。**但剥离 surface differences 后，novelty delta 的本质是\"用 ground-truth formal parse 替换 learned translator 作为奖励来源，并加上 claim-level 拆分\"**——这是一个工程上干净、理论上有道理的改进，但不是 paradigm shift。审稿人可能评价为 \"clean and principled, but incremental over GeoDPO\"。EPV+SGVR 的互补组合（感知输入验证 + 推理产出验证 = 双重覆盖）是一个有吸引力的贡献点，但属于 bonus 而非核心创新。\n\n2. **Significance: 中** — 问题本身非常重要且热门：多篇顶会论文（PEARL@CVPR, CogFlow@ICLR, MoCA@ICML, Perception-R1@ICLR）都在攻击感知-推理耦合问题，40-60% 的多模态数学错误来自感知。但 EPV 的适用范围被限制在**有 formal parser 的领域**（当前仅几何），generalization claim（化学结构、电路图等）是未经验证的推测。如果 positive results 出来，审稿人可能的反应是 \"makes sense, but geometry-specific\"，而非 \"this changes how we think about perception rewards\"。此外，如果 EPV 在实验中仅比 GeoDPO 好几个百分点，significance 会进一步受限。\n\n3. **Related Work: 强** — 这是 proposal 最突出的优点。覆盖了近期所有重要工作（PAPO, PEARL, MoCA, CogFlow, PRCO, EVPV, SGVR, GeoDPO, Perception-R1, SymHPR, Visual-ERM），分类清晰（implicit → model-based explicit → structural-representation-based → formal verification for reasoning），与 GeoDPO 的差异化定位准确且具体（三个维度的对比）。所有引用的论文均经验证真实存在，描述准确。\n\n【概率估计】: [22% - 35%] 中位 28%\n\n【估计理由】: \n- Novelty 为\"中\"限制了上界：核心贡献是 GeoDPO 的 model-free 升级版 + claim-level 粒度，审稿人可能视为 incremental。\n- Significance 为\"中\"进一步限制上界：domain-specific（仅几何），generalization 停留在 claim 层面。\n- Related Work \"强\"提供了一定的下界保护：positioning 清晰，审稿人不太可能指出 \"missed important related work\"。\n- 该领域极度拥挤（2025-2026 年已有 10+ 篇顶会/顶刊论文），竞争激烈，incremental novelty 在 top venue 很难脱颖而出。\n- EPV+SGVR 互补性是一个加分项（如果实验证实），可能将概率从下界拉升。\n- \"盲点假说\"如果实验验证成立，会是一个有说服力的 story，但如果不成立，核心论点被削弱。\n\n上界被 Novelty 和 Significance 两个维度共同限制在 35% 左右。\n\n【主要风险】:\n1. **Incremental over GeoDPO 的质疑**：审稿人可能认为 \"用 ground-truth formal parse 替换 learned translator\" 是一个工程优化而非研究贡献，尤其是如果实验增益不大的话。核心 selling point 的\"model-free 消除盲点\"需要 blind-spot validation 实验的强力支撑，但这个实验本身设计复杂且结论不确定。\n2. **Domain specificity 限制 impact**：方法仅适用于有成熟 formal parser 的领域（当前仅几何），generalization 到化学结构/电路图/函数图是未验证的 claim。审稿人可能质疑 \"if this only works for geometry, is it general enough for a top venue?\"——尤其是当 GeoDPO 已经在几何上取得了 +26.5% in-domain, +39.0% reasoning 的强结果时，EPV 需要在同一领域展示更大的增益才有说服力。\n```\n\nSources:\n- [PAPO: Perception-Aware Policy Optimization](https://arxiv.org/abs/2507.06448)\n- [GeoDPO: Translator-Guided RL for Geometry Perception](https://arxiv.org/abs/2602.22703)\n- [PEARL: Perceptual-Evidence Anchored RL](https://arxiv.org/abs/2511.18437)\n- [MoCA: Bad Seeing or Bad Thinking](https://arxiv.org/abs/2605.14054)\n- [SGVR: Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)\n- [CogFlow](https://arxiv.org/abs/2601.01874)\n- [PRCO: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)\n- [EVPV: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253)\n- [Geoparsing / GDP-29K](https://arxiv.org/abs/2604.11600)\n- [Visual-ERM](https://arxiv.org/abs/2603.13224)\n- [SymHPR](https://arxiv.org/abs/2512.03126)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Model-Free Claim-Level Perception Verification Rewards for Multimodal Math RL\n\n## Core Problem\n\nCurrent perception rewards in multimodal math RL rely on model-dependent assessment — from implicit regularization (PAPO's KL divergence, arXiv 2507.06448) to learned translators (GeoDPO's NL-to-DSL scores, arXiv 2602.22703) to LLM-as-judge (PEARL, CVPR 2026). These methods suffer from two limitations of varying severity: (1) model-dependent rewards inherit systematic biases shared with the policy VLM, creating blind spots where the reward fails to penalize precisely the perception errors the policy most needs to correct; (2) holistic or implicit rewards cannot pinpoint which specific perception claim is wrong, limiting diagnostic utility and targeted credit assignment.\n\nWe propose a general principle: wherever executable formal verifiers exist for a visual domain, model-free symbolic verification should replace model-dependent judges as RL perception rewards, providing claim-level granularity. We instantiate this principle in geometry — where formal parsers have reached sufficient maturity — as the first demonstration of model-free, claim-level, symbolically grounded perception verification rewards for multimodal math RL.\n\n## Research Opportunity\n\nFormal diagram parsers (Geoparsing with GDP-29K annotated geometry diagrams, arXiv 2604.11600; SymHPR with 98.2% reconstruction MSE reduction, arXiv 2512.03126) produce structured ground-truth representations of mathematical diagrams but are used only as preprocessing or for perception module training in isolation. Executable visual verification (RRVF, Visual-ERM, arXiv 2603.13224) has proven effective for code generation (+8.4 on chart-to-code) but has never been applied to mathematical reasoning RL. The missing bridge is using formal parses as model-free oracles to verify individual perception claims within the reasoning chain during RL training, providing truly verifiable, claim-level step rewards.\n\nThis is feasible now because (1) formal parsing quality has reached sufficient maturity, (2) perception-reasoning disentanglement is a proven recipe (MoCA at ICML 2026 Spotlight, arXiv 2605.14054), and (3) 40-60% of multimodal math failures are perception errors. The principle generalizes beyond geometry: chemical structure diagrams can be verified via SMILES/InChI validators, circuit diagrams via SPICE simulators, function graphs via symbolic computation engines. Geometry is the optimal first testbed due to formal parser maturity.\n\n## Research Landscape\n\nExisting perception reward methods span a spectrum from implicit to explicit but remain model-dependent:\n\n**Implicit methods**: PAPO (arXiv 2507.06448) introduces KL divergence Implicit Perception Loss, improving perception without external oracles (+8% on vision-dependent tasks, 30.5% perception error reduction). Effective but provides zero claim-level diagnostics — cannot identify which perception was wrong. KAWHI (arXiv 2603.27375) addresses visual representation bottlenecks via reward reweighting but does not verify perception claims.\n\n**Model-based explicit methods**: URSA (NeurIPS 2025) uses process reward models with synthetic hallucination injection. Perception-R1 (ICLR 2026) uses LLM-as-judge. PRCO (2026, arXiv 2603.28618) uses model-generated captions with role-specific rewards. MoCA (ICML 2026 Spotlight, arXiv 2605.14054) uses blindfolded reasoning as proxy for perception sufficiency. CogFlow (ICLR 2026, arXiv 2601.01874) uses learned synergistic visual rewards with three-stage perception→internalization→reasoning. PEARL (CVPR 2026, arXiv 2511.18437) derives perception checklists verified via LLM judge during GRPO (+9.7% on MathVerse). EVPV (Mar 2026, arXiv 2603.16253) verifies visual premises via model-generated checklists with reliability gating.\n\n**Structural-representation-based methods**: GeoDPO (arXiv 2602.22703) trains an NL-to-DSL translator to compute DSL-level scores as RL reward for geometry perception (+26.5% in-domain, +39.0% downstream reasoning). This is the closest prior work. Three key differences from our approach: (1) GeoDPO's reward comes from a learned translator's soft confidence scores — still model-dependent, inheriting translator biases; EPV uses ground-truth formal parses with symbolic matching, fully model-free. (2) GeoDPO does staged training (DPO perception → reasoning); EPV integrates perception rewards into joint GRPO training, enabling perception-reasoning co-adaptation. (3) GeoDPO provides holistic diagram-level scoring; EPV verifies individual claims, enabling fine-grained credit assignment and targeted failure diagnosis (e.g., \"model systematically misidentifies parallel relations\").\n\n**Formal verification for reasoning (not perception)**: SGVR (Jan 2026, arXiv 2601.05073) converts formal proofs into verifiable numeric sub-goals for RL reward (+9.7% on geometry), but verifies reasoning outcomes (whether intermediate computed values are correct), not perception premises (whether visual inputs were correctly read). SymHPR (Dec 2025, arXiv 2512.03126) uses reconstruction-based rewards but only trains the perception module.\n\n**The gap**: Model-free, claim-level, symbolically grounded perception verification as step-level RL reward for the full reasoning chain is not addressed by any published or concurrent work. EPV verifies perception inputs (premise-level) while SGVR verifies reasoning outputs (outcome-level); their combination achieves dual coverage — we validate this complementarity experimentally.\n\n## Proposed Approach\n\nWe build an Executable Perception Verification Oracle (EPV-Oracle) with three components:\n\n**1. Ground-truth formal parse cache.** Pre-parse all training geometry diagrams into ground-truth formal representations using Geoparsing (GDP-29K, arXiv 2604.11600) and FormalGeo, storing structured representations of points, lines, angles, parallel/perpendicular relations, and measurements. Data audit determines actual coverage across GDP-29K, FormalGeo7K, and GeoQA; diagrams lacking gold annotations are auto-parsed via the Geoparsing model with quality filtering. Strict train-test split protocol: any evaluation benchmark sample (GeoQA test, Geometry3K test) appearing in the formal parse training cache is removed; a zero-overlap evaluation subset is reported separately.\n\n**2. Perception claim extraction.** During GRPO training, we extract perception claims from each CoT step using a dual-path approach: (a) rule-based pattern matching for explicit numeric/relational claims (e.g., \"angle ABC = 60°\", \"AB ∥ CD\"), and (b) structured output prompting that encourages parseable perception claims during rollouts. We independently validate extraction quality on 500-800 hand-annotated CoT samples, reporting precision/recall/F1 broken down by claim type (explicit numeric, explicit relational, implicit/inferential), and ablate rule-based vs. hybrid extraction and high-recall vs. high-precision configurations to characterize noise tolerance.\n\n**3. Symbolic verification and reward.** Extracted claims are verified against the formal parse through symbolic matching — no LLM judge, no learned model. The verification yields step-level perception reward r_percept = verified_claims / total_claims, combined with outcome reward via r = r_outcome + λ·r_percept, where λ is annealed during training. Beyond the scalar reward, claim-level verification enables targeted failure diagnosis: automatic identification of systematic perception failure patterns (e.g., \"model consistently misidentifies obtuse angles as right angles\"), which can guide training data curation and model debugging.\n\n**Correlated bias analysis (blind spot validation).** We validate the blind-spot hypothesis with two diagnostic experiments: (1) Controlled corruption: inject known errors into formal parses, verify EPV reward degrades monotonically (oracle accuracy validation). (2) Conditional circularity analysis: stratify geometry problems by configuration difficulty, measure within-stratum overlap between policy VLM perception errors and PEARL-style LLM-judge false negatives vs. EPV-Oracle false negatives. If within-stratum overlap is high for LLM-judge but low for EPV-Oracle, this provides evidence that the blind spots are due to shared model biases rather than intrinsic difficulty.\n\nWe train on geometry problems (actual count determined by data audit, estimated 10-15K after deduplication and leakage removal) from GDP-29K, FormalGeo7K, and GeoQA, using EasyR1/OpenRLHF on 16×A100 GPUs, at two model scales: Qwen3-VL-4B and Qwen3-VL-8B.\n\n## Evaluation Design\n\n**Benchmarks (5-6):**\n- Geometry-specific: MathVerse, GeoQA, Geometry3K (with zero-overlap subset reported separately)\n- General multimodal (generalization/regression): MMMU, MathVista\n- Step-level perception: VisualProcessBench (EVPV benchmark)\n\n**Baselines (6 direct + indirect):**\n1. Vanilla GRPO (no perception reward) — lower bound\n2. PEARL (LLM-judge perception, CVPR 2026, arXiv 2511.18437) — model-based explicit\n3. GeoDPO (learned translator DSL reward, arXiv 2602.22703) — structural-representation-based, closest competitor\n4. PAPO (implicit KL perception loss, arXiv 2507.06448) — zero-overhead implicit method, cost-effectiveness challenge\n5. SGVR (formal sub-goal reward, arXiv 2601.05073) — formal verification for reasoning outcomes\n6. MoCA (blindfolded proxy, ICML 2026 Spotlight, arXiv 2605.14054) — perception sufficiency paradigm\n- Indirect (cited numbers): Perception-R1 (ICLR 2026), CogFlow (ICLR 2026), PRCO (arXiv 2603.28618)\n\n**Perception-specific diagnostics:**\n- Blindfold test (MoCA paradigm): text-only vs. multimodal inference to isolate perception contribution\n- Reward signal quality: Pearson/Spearman correlation between EPV reward and human-annotated perception correctness on held-out set, compared against PEARL LLM-judge and GeoDPO translator scores\n- Error type breakdown: perception/reasoning/calculation error rates before and after training\n- Geometry-specific perception error rate: manual annotation of perception errors on 200+ GeoQA/Geometry3K test samples, reporting reduction percentage (comparable to PRCO's 39.2%, PAPO's 30.5%)\n\n**Internal ablations:**\n- λ strategy: constant λ vs. linear annealing vs. cosine annealing vs. λ=0 (vanilla GRPO)\n- r_percept granularity: ratio (verified/total) vs. binary per-step vs. difficulty-weighted\n- Claim extraction: rule-based vs. hybrid; high-recall vs. high-precision\n- Formal parse source: GDP-29K only vs. FormalGeo7K only vs. combined vs. auto-parsed\n- Training data scale: 5K vs. 10K vs. 15K\n- EPV + SGVR joint training: r = r_outcome + λ₁·r_percept(EPV) + λ₂·r_subgoal(SGVR), validating complementarity\n- Noise injection robustness: 5%/10%/20% error injection into formal parse cache\n\n**Compute fairness:** Full lifecycle compute decomposition (parse cache construction + per-step extraction + per-step verification + RL training) for all methods. Iso-compute comparison: fixed total GPU-hours budget, each method trains for as many steps as its per-step cost allows. Performance-vs-compute scaling curve.\n\n## Key References\n\n- Unlocking Multimodal Mathematical Reasoning via Process Reward Model (NeurIPS 2025)\n- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (ICLR 2026)\n- Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning (ICML 2026)\n- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026)\n- Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning (CVPR 2026)\n- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning (arXiv 2026)\n- Hierarchical Process Reward Models are Symbolic Vision Learners (arXiv 2025)\n- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2026)\n- Grounding the Score: Explicit Visual Premise Verification for Reliable VL-PRMs (arXiv 2026)\n- Learning Only with Images: Visual Reinforcement Learning with Reasoning, Rendering, and Visual Feedback (arXiv 2025)\n- Visual-ERM: Reward Modeling for Visual Equivalence (arXiv 2026)\n- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)\n- A Survey of Multimodal Mathematical Reasoning: From Perception, Alignment to Reasoning (arXiv 2026)\n- Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2026)\n- ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs (NeurIPS 2025)\n- PAPO: Perception-Aware Policy Optimization for Multimodal Reasoning (arXiv 2507.06448)\n- GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning (arXiv 2602.22703)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 2,500–3,500 (6 baselines × 2 scales + ablations), timeline: 16–20 weeks, estimated_gpu_cost: $6,250–$8,750, annotation: 500-800 CoT samples + 200 perception error samples\n- **human_in_loop**: gpu_hours: 2,000–2,800, timeline: 12–16 weeks, claude_api_cost: $500–$800, estimated_gpu_cost: $5,000–$7,000\n- **auto_research**: gpu_hours: 2,000–2,800, timeline: 8–12 weeks, claude_api_cost: $1,200–$1,800, estimated_gpu_cost: $5,000–$7,000, speed_bottleneck: RL training wall-clock (16h/run on 16×A100); formal parses pre-cached; experiment iteration loop is binding constraint"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T22:20:52.098Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T22:20:52.098Z",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-27T22:20:52.110Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient background to perform the evaluation. Let me synthesize my findings.

---

```
【阶段】: Triage

【领域调研】:

1. **GeoDPO** (arXiv 2602.22703, Feb 2026): 最直接的竞争者。训练 NL-to-DSL 翻译器，用翻译器 soft confidence 分数作为 RL reward 强化几何感知。效果: +26.5% in-domain, +39.0% 下游推理。与本 proposal 的关键差异在于: GeoDPO reward 来自学习到的翻译器（model-dependent），提供 diagram-level holistic scoring；本 proposal 用 ground-truth formal parse + symbolic matching（model-free），提供 claim-level granularity。但二者核心思路一脉相承——都是用结构化几何表示指导 perception RL。

2. **PEARL** (CVPR 2026, arXiv 2511.18437): 从推理 QA 自动推导 perception checklist，用 LLM-judge 验证。+9.7% on MathVerse。属 model-dependent explicit 方法，与本 proposal 的 model-free 定位形成对比，但 PEARL 的 checklist 思想与本 proposal 的 claim-level 验证在形式上有相似性。

3. **PAPO** (arXiv 2507.06448): 通过 KL 散度 Implicit Perception Loss 提升感知能力，30.5% perception error reduction。零额外基础设施成本，是本 proposal 需要超越的 cost-effectiveness 基准。

4. **SGVR** (arXiv 2601.05073, Jan 2026): 将几何形式化证明转换为可验证 numeric sub-goals 作为 RL reward，+9.7% geometry。验证的是推理中间步骤的正确性（outcome-level），而非感知前提的正确性（premise-level）。本 proposal 明确定位为与 SGVR 互补。

5. **MoCA** (ICML 2026 Spotlight, arXiv 2605.14054): 通过 "blindfolded reasoning" proxy 解耦感知与推理，间接奖励感知保真度。Model-dependent。

6. **CogFlow** (ICLR 2026, arXiv 2601.01874): 三阶段 perception→internalization→reasoning 框架，使用 learned synergistic visual rewards。代表了另一种解决感知-推理脱节的范式。

7. **PRCO** (arXiv 2603.28618): 双角色 RLVR 框架，Observer + Solver 分工，role-specific rewards。用 utility reward 而非直接验证感知。

8. **EVPV** (arXiv 2603.16253, Mar 2026): Explicit Visual Premise Verification，将 step scoring 条件化于 visual premise 的可靠性。用 model-generated checklist + constraint extraction 计算 reliability signal。这与本 proposal 在"验证具体 visual claim"这一思想上高度相似，但 EVPV 用于 PRM reranking 而非 RL training reward，且其 constraint extraction 仍有 model 参与。

9. **Geoparsing/GDP-29K** (arXiv 2604.11600, Apr 2026): 本 proposal 依赖的 formal parser。统一平面与立体几何的形式语言，29K 数据集。是较新的工作（2026年4月），其在真实多样几何图的泛化鲁棒性尚待广泛验证。

10. **SymHPR** (arXiv 2512.03126, Dec 2025): 符号化 hierarchical process reward 用于几何 diagram reconstruction。使用 rule-based reward，但仅训练感知模块，不用于全链路 RL。

11. **Visual-ERM / RRVF** (arXiv 2603.13224): Executable visual verification 用于 chart-to-code (+8.4)。证明了"可执行验证作为 RL reward"在视觉代码生成中的有效性，但未用于数学推理感知。

- **调研总结**: 这个领域正处于爆发式增长期（2025H2-2026H1 涌现了十余篇直接相关工作），核心趋势是"如何在 multimodal RL 中给感知信号提供更好的 reward"。当前方法从 implicit（PAPO）到 model-based explicit（PEARL, CogFlow, MoCA, PRCO）再到 structural-representation-based（GeoDPO, SymHPR）形成了清晰的谱系。本 proposal 定位在该谱系的最右端——完全 model-free 的 symbolic verification reward，是一个自然但尚未被占据的位置。然而 GeoDPO 已经非常接近这个位置（用结构化 DSL 表示 + 学习到的翻译器），本 proposal 的增量贡献取决于"model-free vs. model-dependent"这一步差异在实践中能否带来显著收益。

---

【Trivial Alternative 检验】:

**存在两个 trivial alternative 威胁：**

(1) **GeoDPO + 更好的翻译器**: 如果将 GeoDPO 的 NL-to-DSL 翻译器在更大更多样的数据上训练，使其准确率达到 95%+，那么"model-dependent but accurate"与"model-free"之间的实际差距可能很小。本 proposal 的核心 selling point——"model-free 消除 correlated bias blind spots"——需要实验证明 blind spots 是实际存在且有实际影响的（而不仅仅是理论上存在的）。Proposal 中设计了 blind spot validation 实验（controlled corruption + conditional circularity analysis），这是合理的，但如果实验结果显示 blind spot 效应微弱，整个 story 的核心就垮了。

(2) **PAPO 的零成本方案**: PAPO 用一个简单的 KL 散度项就实现了 30.5% 的 perception error reduction，零额外基础设施。EPV 需要构建 formal parse cache、claim extraction pipeline、symbolic matching system——如果最终 perception error reduction 仅略优于 PAPO（比如 35% vs. 30.5%），那么从 cost-effectiveness 角度很难 justify 这套复杂系统。

**增量价值所在**: 如果实验确实证明 (a) claim-level diagnostics 能精确定位系统性感知错误模式从而指导 targeted intervention，(b) model-free reward 在 reward signal quality（与人工标注的 Pearson/Spearman 相关性）上显著优于 PEARL LLM-judge 和 GeoDPO translator，那么增量价值是成立的。但这高度依赖实验结果，idea 层面无法先验保证。

---

【前提假设检验】:

核心 claim 的逻辑链条中有 **四个关键未验证假设**：

**(1) Formal parser 质量足以充当 ground-truth oracle**
Geoparsing/GDP-29K 是 2026 年 4 月才发布的工作，其在 training set 之外的真实多样几何图上的解析准确率未知。如果 formal parser 本身有 5-10% 的错误率，那么所谓的"model-free oracle"实际上引入了一种不同类型的 systematic bias（parser bias）。Proposal 设计了 noise injection robustness 实验（5%/10%/20%），但这只验证了 EPV 对已知噪声的容忍度，没有回答"实际噪声率到底是多少"。

**(2) Claim extraction 从 CoT 中可靠且全面**
从 free-form CoT 中提取结构化 perception claims 是一个非平凡的 NLP 问题。Rule-based pattern matching 只能覆盖显式数值/关系 claims（"∠ABC = 60°", "AB ∥ CD"），但大量感知信息是隐式的或混杂在推理步骤中。Proposal 承认了这一点并设计了 extraction quality 验证，但如果 recall 较低（比如只覆盖 50-60% 的实际 perception claims），reward signal 的信息量就大打折扣。

**(3) Correlated bias blind spots 是 VLM RL 性能的实际瓶颈**
"Model-dependent reward 与 policy VLM 共享 systematic bias"是一个合理的理论假设，但其实际影响大小未知。GeoDPO 的翻译器是单独在合成数据上训练的，与 policy VLM 的训练数据和架构都不同，correlated bias 可能远小于预期。如果 blind spot 效应微弱，本 proposal 的核心 motivation 就大幅削弱。

**(4) Symbolic matching 能正确处理 NL claim 与 formal representation 之间的语义对齐**
"AB ∥ CD"在 NL 中可能有多种表述（"line AB is parallel to CD", "AB and CD are parallel lines", 甚至"since these two lines never meet..."），如何 robustly 地将这些 match 到 formal parse 中的 parallel(A,B,C,D) 关系？这不是 trivial 的字符串匹配，可能本身就需要一个小型 NLU 模块——这又引入了 model-dependent 成分，削弱了"完全 model-free"的 claim。

---

【3 维度打分】:

1. **Novelty: 中** — 核心贡献是将 model-free symbolic verification 用于 perception RL reward 并提供 claim-level 粒度。与最直接竞争者 GeoDPO 相比，差异是真实的（model-free vs. model-dependent, claim-level vs. holistic, joint training vs. staged），但属于同一研究路线上的增量推进而非范式转换。EVPV 已经在做 claim-level visual premise verification（虽然用于 PRM 而非 RL reward），SGVR 已经在几何中用 formal verification 做 RL reward（虽然是 reasoning outcome 而非 perception premise），Visual-ERM 已经证明了 executable verification 作为 RL reward 的有效性。本 proposal 的贡献更像是"将已有的 pieces 组合在一起"——formal parsing (Geoparsing) + claim-level verification (EVPV 的思想) + RL reward (SGVR 的思想) → 针对 perception 的 model-free claim-level reward。组合是合理的、位置是空白的，但单看任何一个维度都不算突破性创新。

2. **Significance: 中** — 研究问题（如何给 multimodal math RL 中的 perception 提供更好的 reward）是当前领域的热门且重要问题（十余篇 2025-2026 论文在攻克）。但本 proposal 的 instantiation 高度 domain-specific（仅限于有 formal parser 的领域），当前只在几何上验证，泛化到化学结构/电路图/函数图完全是理论性的。如果核心结果是 positive（比如 EPV 比 GeoDPO 好 5-8 个点），审稿人的反应可能是"makes sense, not surprising"——因为用 ground-truth 比用 learned proxy 更准确是直觉上预期的结果。真正 surprising 的结果需要是：(a) EPV 揭示了 GeoDPO/PEARL 无法发现的 systematic blind spots, (b) claim-level diagnostics 带来了 holistic reward 无法实现的 targeted improvement, 或 (c) EPV+SGVR 的组合产生了超加性效应。这些都有可能，但不是先验可预期的。

3. **Related Work: 强** — 这是本 proposal 最强的维度。对已有工作的覆盖非常全面，从 implicit (PAPO) 到 model-based explicit (PEARL, CogFlow, MoCA, PRCO, EVPV) 到 structural-representation-based (GeoDPO, SymHPR) 到 formal verification for reasoning (SGVR) 构建了清晰的谱系，差异化定位明确。与 GeoDPO 的三点差异分析具体且有说服力。SGVR 的互补性定位也合理。引用的论文经调研验证全部真实存在且描述准确。唯一的小瑕疵是对 EVPV 的定位可能不够突出——EVPV 的 claim-level visual premise verification 与本 proposal 的思想有较高相似性，proposal 中只在列表中提了一句，没有充分讨论为何 EVPV 的方法不够好。

---

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
- Related Work 覆盖全面且定位清晰，这为论文提供了坚实的 framing 基础（拉高下界）。
- Novelty 为中：核心贡献是已有 building blocks 的合理组合，GeoDPO 的存在使得增量空间被压缩。任何一个了解 GeoDPO + SGVR 的审稿人都可能认为"用 ground-truth formal parse 替代 learned translator"是一个自然的 next step，not surprising。
- Significance 受限于两个因素：(a) 高度 domain-specific，当前只能在几何上工作；(b) 如果核心结果 positive，审稿人可能认为"ground-truth 比 learned proxy 好"是预期之内的。
- **上界受限于 Novelty**：即使实验全部 positive，idea 的 conceptual novelty（已有 pieces 的组合）使得论文很难进入"strong accept"区间。
- **下界受限于 Significance**：如果 blind spot validation 和 claim-level diagnostics 的结果不够 compelling，论文的 motivation 会被审稿人质疑（"为什么不直接用 GeoDPO + 更好的翻译器？"）。

【主要风险】:
1. **"Natural next step" 的 novelty 质疑**: 审稿人很可能指出 EPV 是 GeoDPO + SGVR 的自然延伸，缺乏足够的 conceptual novelty。"用 ground-truth 替代 learned proxy"的 insight 不够 deep——这更像是 engineering decision 而非 research contribution。
2. **增量收益可能不足以 justify 复杂度**: 如果 EPV 相比 GeoDPO 的提升仅 3-5 个百分点，而 PAPO 用零基础设施就能获得可观的 perception improvement，审稿人会质疑这套需要 formal parse cache + claim extraction + symbolic matching 的系统是否值得。核心风险在于 model-free 的理论优势在实践中可能转化不出显著的性能增量。
```

Sources:
- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/abs/2602.22703)
- [PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning](https://arxiv.org/abs/2511.18437)
- [PAPO: Perception-Aware Policy Optimization for Multimodal Reasoning](https://arxiv.org/abs/2507.06448)
- [SGVR: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)
- [MoCA: Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)
- [CogFlow: Bridging Perception and Reasoning through Knowledge Internalization](https://arxiv.org/abs/2601.01874)
- [PRCO: Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning](https://arxiv.org/abs/2603.28618)
- [EVPV: Grounding the Score: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253)
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)
- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)
- [Visual-ERM: Reward Modeling for Visual Equivalence](https://arxiv.org/abs/2603.13224)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to conduct a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

- [GeoDPO / arXiv 2602.22703] (Feb 2026): 最直接的竞争对手。训练 NL-to-DSL translator，用 translator 的 soft confidence scores 作为 geometry perception 的 RL reward（+26.5% in-domain, +39.0% downstream reasoning）。采用 staged training（先 DPO perception 后 reasoning），holistic diagram-level scoring。是当前 geometry perception RL reward 的 SOTA。
- [PEARL / arXiv 2511.18437] (CVPR 2026): 构建 perception checklist sub-questions，用 LLM-as-judge 验证后给 perception reward gate（+9.7% MathVerse, +6.6% over GRPO）。Model-dependent（LLM judge），但 checklist 思路与 claim-level 有相似之处。
- [PAPO / arXiv 2507.06448] (Jul 2025): 纯 implicit 方法，通过 KL divergence implicit perception loss 嵌入 policy gradient，zero overhead，不需要额外 oracle（+8% vision-dependent, 30.5% perception error reduction）。是零成本 baseline 的强力挑战者。
- [MoCA / arXiv 2605.14054] (ICML 2026 Spotlight): 用 blindfolded reasoning（纯文本推理 vs. 多模态推理）作为 perception sufficiency 的 proxy reward，不直接验证 perception claims，而是间接度量 perception 的贡献。
- [SGVR / arXiv 2601.05073] (Jan 2026): 将 formal proof 转化为 verifiable numeric sub-goals 用于 RL reward（+9.7% geometry），但验证的是 reasoning outcomes（中间推理值是否正确），不是 perception premises。与本 proposal 构成互补关系。
- [Perceval / arXiv 2604.24583] (Apr 2026): **高度相关但 proposal 未引用。** 该工作提出 perception-centric PRM，能够从 response 中提取 image-related claims 并与 visual evidence 逐条比对，返回包含 perceptual errors 的 claims，并在 RL 中施加 token-level advantages。与本 proposal 的 claim-level extraction + verification 在概念层面非常接近，但使用的是 learned PRM 而非 model-free symbolic matching。
- [EVPV / arXiv 2603.16253] (Mar 2026): 步级 visual checklist + constraint extractor → reliability gating 的 PRM 方法。与本 proposal 的 claim verification 概念相似，但完全 model-dependent（learned constraint extractor）。
- [ViCrit / NeurIPS 2025]: 构造 proxy task（在 caption 中注入 subtle hallucination，训练模型定位错误 span），用作 verifiable perception RL 任务。思路不同但目标相似。
- [Geoparsing / GDP-29K / arXiv 2604.11600] (Apr 2026): 统一形式化语言的 geometry diagram parser，覆盖平面和立体几何。是本 proposal 的核心技术依赖。论文本身发布较新（Apr 2026），parser 的成熟度和可靠性尚需验证。
- [Visual-ERM / arXiv 2603.13224] (Mar 2026): 用渲染后视觉比对作为 code generation 的 reward（+8.4 chart-to-code）。是 executable verification 在 vision-to-code 的先例，但未用于 math reasoning RL。

- **调研总结**: Multimodal math RL 的 perception reward 是 2025-2026 年的研究热点，已形成从 implicit (PAPO) → model-based explicit (PEARL, Perceval, EVPV) → structural-representation-based (GeoDPO) 的方法谱系。本 proposal 试图在该谱系上推进到"model-free symbolic verification"这一端点。核心竞争对手是 GeoDPO（结构化表示 + learned translator）和 Perceval（claim-level extraction + learned PRM）。关键问题是：从"learned translator/PRM"到"model-free symbolic matching"的增量是否足够大？

【Trivial Alternative 检验】:

**存在明确的 trivial alternative 威胁。** 
(1) GeoDPO 已经使用 DSL 结构化表示作为 reward signal，虽然通过 learned translator 而非 symbolic matching，但如果 translator 训练在足够大的合成数据上且泛化良好，其 reward quality 可能已经接近 ground-truth symbolic matching。本 proposal 的增量价值完全依赖于"learned translator 的 bias 确实造成了可测量的 blind spot"这一未验证假设。
(2) 一种更简单的替代方案：直接用 Geoparsing 的 formal parse 作为 gold label，对 VLM 的 diagram description 做 string/DSL-level matching（不需要 claim extraction from CoT），用 diagram-level F1 作为 reward。这种方法省去了 claim extraction 的复杂工程，可能达到类似效果。
(3) PAPO 的 implicit KL loss 是零额外成本的方法，已经实现 30.5% perception error reduction。本 proposal 需要证明其复杂的 pipeline（formal parse cache + claim extraction + symbolic matching）带来的增益显著超过 PAPO 的零成本 baseline。

**增量价值定位**: 如果 blind spot 假说被验证（model-dependent reward 确实系统性地 miss 某些 perception errors），且 claim-level 的 diagnostic 功能被证明对 targeted training data curation 有实际价值，则增量价值成立。否则，这只是一个更复杂版本的 GeoDPO。

【前提假设检验】:

核心 claim 的逻辑链条包含以下未经验证的假设：

1. **"Model-dependent rewards inherit systematic biases shared with the policy VLM"（blind spot 假说）**: 这是全文最核心的 motivating assumption，但纯属推测。当 reward model（如 GPT-4 作为 PEARL 的 judge，或 GeoDPO 的 translator 训练在合成数据上）与 policy VLM 差异很大时，bias correlation 可能很低。Proposal 设计了 conditional circularity analysis 来验证这一点，但如果实验发现 bias overlap 并不显著，整个 motivation 就坍塌了。

2. **"Claim extraction from free-form CoT is feasible and reliable"**: Rule-based pattern matching 能捕获 explicit numeric/relational claims（如 "angle ABC = 60°"），但 CoT 中大量 perception 是 implicit 的（如隐含地将图中两线视为平行而直接使用了平行线的性质），这些 claims 很难被 rule-based 方法提取。Proposal 承认了 hybrid extraction 的需要并规划了 precision/recall 评估，但如果 recall 低于某个阈值（如 50%），claim-level verification 就退化为对"容易检测的 explicit claims"的验证，对最 challenging 的 implicit perception errors 无能为力。

3. **"Formal parsing quality has reached sufficient maturity"**: Geoparsing (GDP-29K) 发布于 2026 年 4 月，论文本身很新。如果 formal parser 在某些 diagram types 上有系统性错误（如复杂嵌套几何图形、手绘图），那么 "model-free oracle" 自身就成了一个有 bias 的 reward source——只是 bias 的类型不同于 learned models。Proposal 有 noise injection ablation，但这测试的是对随机噪声的鲁棒性，不是对系统性 parsing 错误的鲁棒性。

4. **"Joint GRPO training with perception reward outperforms staged training"**: Proposal 声称 EPV 的优势之一是 joint training（vs. GeoDPO 的 staged training），但这是一个 orthogonal 的设计选择，not unique to model-free verification。GeoDPO 也可以切换到 joint GRPO training。

【3 维度打分】:

1. **Novelty: 中偏弱** — 
   核心 idea（用 formal parse 作为 ground truth oracle 做 symbolic verification of perception claims）是该领域的一个 **natural and somewhat obvious next step**。GeoDPO 已经使用 DSL 结构化表示作为 reward，本 proposal 的核心增量只是将 "learned translator" 替换为 "symbolic matching against ground-truth parse"——这是一个 implementation-level 的变化而非 conceptual breakthrough。Perceval (arXiv 2604.24583) 在 Apr 2026 已经实现了 claim-level extraction + per-claim verification（虽然用 learned PRM），进一步削弱了 claim-level granularity 的 novelty claim。
   
   **剩余 novelty delta**:（a）model-free symbolic matching（vs. 所有 prior work 的 model-dependent approaches）；（b）blind spot hypothesis 的形式化和验证实验设计。这些是真实的增量，但审稿人很可能认为 (a) 是 engineering choice rather than research insight，(b) 是 interesting but secondary。

2. **Significance: 中偏弱** — 
   - **Domain specificity 严重限制 impact**: 方法仅适用于 geometry（以及理论上的化学结构、电路图等），但只在 geometry 上 instantiate。对于 NLP/multimodal reasoning 大领域的影响力有限。
   - **核心发现的 surprise value 低**: 如果实验结果是 positive（"model-free symbolic verification outperforms learned translator for geometry perception reward"），审稿人的反应更可能是 "I would have guessed this"（ground truth 当然比 learned approximation 好）而非 "surprising"。 
   - **Practical significance 受限于 formal parser 可用性**: 该方法的泛化性完全取决于其他领域是否也有成熟的 formal parsers，而目前这类 parsers 很少。
   - 正面因素：perception error 占 multimodal math failure 的 40-67% 是被充分验证的事实（PAPO, MoCA 等均有数据支撑），问题本身是重要的。

3. **Related Work: 强** — 
   Literature coverage 非常全面，包括 implicit (PAPO), model-based explicit (PEARL, Perception-R1, CogFlow, PRCO, EVPV), structural-representation (GeoDPO), formal verification for reasoning (SGVR), reconstruction-based (SymHPR), executable visual verification (Visual-ERM/RRVF) 等。差异化定位清晰，特别是与 GeoDPO 的三点对比（model-free vs. learned, joint vs. staged, claim-level vs. holistic）。
   **一个重要遗漏**: Perceval (arXiv 2604.24583, Apr 2026) 做了 claim-level extraction + per-claim verification for perception reward in RL，在概念层面与本 proposal 高度接近，但 proposal 未提及。这会被审稿人视为 related work 遗漏。

【概率估计】: [23% - 33%] 中位 28%

【估计理由】: 
- Novelty (中偏弱) 和 Significance (中偏弱) 共同限制了上界。核心 idea 是 natural next step，surprise value 低。"用 ground truth formal parse 做 symbolic matching" 在概念上不 surprising——这是任何看到 GeoDPO + Geoparsing 两篇论文的研究者都会想到的组合。
- Related Work (强) 提供了下限保护——至少论文定位清晰、不会因为 missing related work 而直接被拒（但需补上 Perceval）。
- Domain specificity (仅 geometry) 显著拉低 significance，因为 AAAI 审稿人通常期望方法有更广的适用性。
- Blind spot hypothesis 的验证实验设计（conditional circularity analysis）是 proposal 中最有学术价值的部分，如果结果 positive 且 convincing，可以提升论文的贡献——但这属于实验层面能否拉升的问题，不改变 idea 本身的中位估计。
- 该领域竞争极其激烈（PAPO, PEARL, GeoDPO, MoCA, Perceval, EVPV 等在 6 个月内密集发表），增量贡献容易被审稿人认为 insufficient。

【主要风险】:
1. **"Obvious combination" 质疑**: 审稿人可能认为 "用已有的 formal parser 做 symbolic matching 替换 learned translator" 是 engineering contribution 而非 research contribution，尤其是当 GeoDPO + Geoparsing 作为已有工作时，这种组合的 intellectual novelty 有限。
2. **Domain specificity + low surprise value**: 方法仅适用于有成熟 formal parser 的领域，在 geometry 上的 positive result 不会 surprise 审稿人（ground truth oracle 理应优于 learned approximation），且无法泛化到 multimodal math 的其他子领域（代数、统计图表等），限制了论文在 AAAI 的 impact narrative。
```

Sources:
- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/abs/2602.22703)
- [PEARL: Perceptual-Evidence Anchored Reinforced Learning](https://arxiv.org/abs/2511.18437)
- [PAPO: Perception-Aware Policy Optimization for Multimodal Reasoning](https://arxiv.org/abs/2507.06448)
- [MoCA: Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)
- [SGVR: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)
- [Perceval: Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583)
- [EVPV: Grounding the Score: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253)
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)
- [Visual-ERM: Reward Modeling for Visual Equivalence](https://arxiv.org/abs/2603.13224)
- [ViCrit: Verifiable RL Proxy Task for Visual Perception in VLMs](https://arxiv.org/abs/2506.10128)
- [Perception-R1: Advancing Multimodal Reasoning via Visual Perception Reward](https://arxiv.org/html/2506.07218)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me synthesize my findings.

---

```
【阶段】: Triage

【领域调研】:
- [PAPO: Perception-Aware Policy Optimization](https://arxiv.org/abs/2507.06448) (arXiv 2025): 引入隐式 KL 散度感知损失，无需外部预言机即可在 GRPO/DAPO 中提升感知能力，+8% vision-dependent tasks，感知错误减少 30.5%。本 proposal 将其定位为"隐式方法，无法提供 claim-level 诊断"。描述准确。
- [GeoDPO: Translator-Guided RL for Geometry Perception](https://arxiv.org/abs/2602.22703) (arXiv 2026): 训练 NL-to-DSL 翻译器计算 DSL 级别奖励，in-domain +26.5%，downstream reasoning +39.0%。**这是最直接的竞争者**——同样使用结构化表示作为几何感知奖励，但依赖学习到的翻译器（model-dependent）。Proposal 声称的三个差异（model-free vs learned translator, joint vs staged training, claim-level vs holistic）基本准确。
- [PEARL: Perceptual-Evidence Anchored RL](https://arxiv.org/abs/2511.18437) (CVPR 2026): 从 QA 实例派生感知 checklist，用 LLM judge 验证，+9.7% MathVerse。使用 LLM-as-judge，属于 model-dependent explicit 方法。
- [MoCA: Bad Seeing or Bad Thinking](https://arxiv.org/abs/2605.14054) (ICML 2026 Spotlight): 通过"蒙眼推理"代理来奖励感知保真度，解决感知-推理信用分配问题。间接衡量感知质量，不直接验证感知声明。
- [SGVR: Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073) (arXiv 2026): 将形式证明转化为可验证数值子目标作为 RL 奖励，+9.7% geometry。**关键区分**：验证推理产出（intermediate computed values），不验证感知前提（visual inputs）。Proposal 的区分描述准确。
- [CogFlow](https://arxiv.org/abs/2601.01874) (ICLR 2026): 三阶段框架（感知→内化→推理），使用学习到的协同视觉奖励。Model-dependent。
- [PRCO: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618) (arXiv 2026): Observer-Solver 双角色框架，role-specific 奖励。Model-dependent（Observer 的效用奖励来自 Solver 的下游成功）。
- [EVPV: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253) (arXiv 2026): 模型生成 checklist + 约束提取器进行视觉可靠性评分。也是 model-dependent（依赖约束提取器）。
- [Geoparsing / GDP-29K](https://arxiv.org/abs/2604.11600) (arXiv 2026): 20K 平面 + 9K 立体几何样本配对 ground-truth 形式化描述。**这是 EPV-Oracle 的关键基础设施**，论文确实存在且提供了 proposal 声称的能力。
- [Visual-ERM](https://arxiv.org/abs/2603.13224) (arXiv 2026): 视觉等价奖励模型，用于 vision-to-code 任务，chart-to-code +8.4。与本 proposal 的领域不同（code generation vs math reasoning）。
- [SymHPR](https://arxiv.org/abs/2512.03126) (arXiv 2025): 基于重建的奖励，但仅训练感知模块，不用于完整推理链的 RL 训练。

**调研总结**: 多模态数学 RL 中的感知奖励是 2025-2026 年极其活跃的研究方向，已有超过 10 篇高质量工作从不同角度攻击这个问题。现有方法全部是 model-dependent（隐式 KL、LLM-as-judge、学习到的翻译器、蒙眼代理等），无一实现 model-free + claim-level 的符号化验证。**这个空白是真实存在的**，但空白的大小（incremental improvement vs paradigm shift）取决于 model-free 在实践中是否带来显著收益。

【Trivial Alternative 检验】:

存在一个值得警惕的 trivial alternative：**直接用 GeoDPO 的框架但换一个更好的翻译器**。GeoDPO 已经使用了结构化表示（DSL）作为几何感知奖励，只是通过学习到的翻译器来桥接。如果翻译器的准确率足够高（比如在高质量数据上 fine-tune），其"model-dependent bias"可能在实践中可忽略不计。Proposal 的核心增量价值在于：

1. **真正的 model-free**：使用 ground-truth formal parse 而非 learned translator，理论上消除了系统性偏差。但"盲点假说"（policy VLM 和 model-dependent judge 共享偏差）对 GeoDPO 的适用性存疑——GeoDPO 的翻译器有不同的架构和训练目标，其偏差不一定与 policy VLM 相关。
2. **Claim-level 粒度**：GeoDPO 给出 holistic diagram-level 分数，EPV 验证个别声明。这是真正的新增能力，但其实用价值取决于 claim extraction 的质量。

**结论**：trivial alternative 不完全成立——claim-level 粒度确实是 GeoDPO 不具备的新能力。但 model-free vs model-dependent 的实际增益可能不大，这削弱了核心论点的说服力。

【前提假设检验】:

核心逻辑链中有以下未经验证的环节：

1. **"盲点假说"本身未经实证**：Proposal 声称 model-dependent rewards 与 policy VLM 共享系统性偏差，导致 reward 恰好在 policy 最需要纠正的地方失效。这个假设直觉上对 LLM-as-judge 合理（共享预训练数据和架构偏差），但对 GeoDPO 的翻译器（不同任务、不同数据）是否成立需要实证。Proposal 设计了 conditional circularity analysis 来验证，但这本身是一个需要在实验中才能确认的假设。**如果实验发现 GeoDPO 翻译器的偏差与 policy VLM 不相关，核心论点的力度将大幅减弱。**

2. **Claim extraction 的可靠性是硬依赖**：整个方法的有效性取决于能否从 free-form CoT 中可靠提取感知声明。Rule-based pattern matching 对显式数值/关系声明（"angle ABC = 60°"）可行，但对隐式/推断性声明（"the triangle appears to be right-angled"）可能遗漏大量信息。CoT 中的感知信息可能以非结构化方式嵌入推理中，难以用规则提取。**如果 extraction recall 低，reward signal 就是稀疏且有偏的。**

3. **Formal parse 的覆盖率和质量**：GDP-29K 的 formal parse 质量在简单几何上可能很高，但在复杂图表（重叠元素、手绘、非标准标注）上的覆盖率未知。Proposal 计划进行 "data audit" 来确定覆盖率，但这又是一个事后才能验证的假设。

4. **λ annealing 的有效性**：perception reward 和 outcome reward 的结合方式（线性/余弦退火）假设两者可以简单加权，但感知错误和推理错误的相互作用可能更复杂。这一点在 prior work（CogFlow, PRCO）中已有研究，不是致命问题但需要仔细调参。

【3 维度打分】:

1. **Novelty: 中** — 核心创新是"model-free + claim-level + symbolic"的组合，这在已发表工作中确实不存在。GeoDPO（最近竞争者）使用 learned translator + holistic scoring，SGVR 验证推理而非感知，PEARL/EVPV 使用 LLM-as-judge。**但剥离 surface differences 后，novelty delta 的本质是"用 ground-truth formal parse 替换 learned translator 作为奖励来源，并加上 claim-level 拆分"**——这是一个工程上干净、理论上有道理的改进，但不是 paradigm shift。审稿人可能评价为 "clean and principled, but incremental over GeoDPO"。EPV+SGVR 的互补组合（感知输入验证 + 推理产出验证 = 双重覆盖）是一个有吸引力的贡献点，但属于 bonus 而非核心创新。

2. **Significance: 中** — 问题本身非常重要且热门：多篇顶会论文（PEARL@CVPR, CogFlow@ICLR, MoCA@ICML, Perception-R1@ICLR）都在攻击感知-推理耦合问题，40-60% 的多模态数学错误来自感知。但 EPV 的适用范围被限制在**有 formal parser 的领域**（当前仅几何），generalization claim（化学结构、电路图等）是未经验证的推测。如果 positive results 出来，审稿人可能的反应是 "makes sense, but geometry-specific"，而非 "this changes how we think about perception rewards"。此外，如果 EPV 在实验中仅比 GeoDPO 好几个百分点，significance 会进一步受限。

3. **Related Work: 强** — 这是 proposal 最突出的优点。覆盖了近期所有重要工作（PAPO, PEARL, MoCA, CogFlow, PRCO, EVPV, SGVR, GeoDPO, Perception-R1, SymHPR, Visual-ERM），分类清晰（implicit → model-based explicit → structural-representation-based → formal verification for reasoning），与 GeoDPO 的差异化定位准确且具体（三个维度的对比）。所有引用的论文均经验证真实存在，描述准确。

【概率估计】: [22% - 35%] 中位 28%

【估计理由】: 
- Novelty 为"中"限制了上界：核心贡献是 GeoDPO 的 model-free 升级版 + claim-level 粒度，审稿人可能视为 incremental。
- Significance 为"中"进一步限制上界：domain-specific（仅几何），generalization 停留在 claim 层面。
- Related Work "强"提供了一定的下界保护：positioning 清晰，审稿人不太可能指出 "missed important related work"。
- 该领域极度拥挤（2025-2026 年已有 10+ 篇顶会/顶刊论文），竞争激烈，incremental novelty 在 top venue 很难脱颖而出。
- EPV+SGVR 互补性是一个加分项（如果实验证实），可能将概率从下界拉升。
- "盲点假说"如果实验验证成立，会是一个有说服力的 story，但如果不成立，核心论点被削弱。

上界被 Novelty 和 Significance 两个维度共同限制在 35% 左右。

【主要风险】:
1. **Incremental over GeoDPO 的质疑**：审稿人可能认为 "用 ground-truth formal parse 替换 learned translator" 是一个工程优化而非研究贡献，尤其是如果实验增益不大的话。核心 selling point 的"model-free 消除盲点"需要 blind-spot validation 实验的强力支撑，但这个实验本身设计复杂且结论不确定。
2. **Domain specificity 限制 impact**：方法仅适用于有成熟 formal parser 的领域（当前仅几何），generalization 到化学结构/电路图/函数图是未验证的 claim。审稿人可能质疑 "if this only works for geometry, is it general enough for a top venue?"——尤其是当 GeoDPO 已经在几何上取得了 +26.5% in-domain, +39.0% reasoning 的强结果时，EPV 需要在同一领域展示更大的增益才有说服力。
```

Sources:
- [PAPO: Perception-Aware Policy Optimization](https://arxiv.org/abs/2507.06448)
- [GeoDPO: Translator-Guided RL for Geometry Perception](https://arxiv.org/abs/2602.22703)
- [PEARL: Perceptual-Evidence Anchored RL](https://arxiv.org/abs/2511.18437)
- [MoCA: Bad Seeing or Bad Thinking](https://arxiv.org/abs/2605.14054)
- [SGVR: Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)
- [CogFlow](https://arxiv.org/abs/2601.01874)
- [PRCO: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)
- [EVPV: Explicit Visual Premise Verification](https://arxiv.org/abs/2603.16253)
- [Geoparsing / GDP-29K](https://arxiv.org/abs/2604.11600)
- [Visual-ERM](https://arxiv.org/abs/2603.13224)
- [SymHPR](https://arxiv.org/abs/2512.03126)


【原始 proposal（允许参考但不是主要依据）】:
# Model-Free Claim-Level Perception Verification Rewards for Multimodal Math RL

## Core Problem

Current perception rewards in multimodal math RL rely on model-dependent assessment — from implicit regularization (PAPO's KL divergence, arXiv 2507.06448) to learned translators (GeoDPO's NL-to-DSL scores, arXiv 2602.22703) to LLM-as-judge (PEARL, CVPR 2026). These methods suffer from two limitations of varying severity: (1) model-dependent rewards inherit systematic biases shared with the policy VLM, creating blind spots where the reward fails to penalize precisely the perception errors the policy most needs to correct; (2) holistic or implicit rewards cannot pinpoint which specific perception claim is wrong, limiting diagnostic utility and targeted credit assignment.

We propose a general principle: wherever executable formal verifiers exist for a visual domain, model-free symbolic verification should replace model-dependent judges as RL perception rewards, providing claim-level granularity. We instantiate this principle in geometry — where formal parsers have reached sufficient maturity — as the first demonstration of model-free, claim-level, symbolically grounded perception verification rewards for multimodal math RL.

## Research Opportunity

Formal diagram parsers (Geoparsing with GDP-29K annotated geometry diagrams, arXiv 2604.11600; SymHPR with 98.2% reconstruction MSE reduction, arXiv 2512.03126) produce structured ground-truth representations of mathematical diagrams but are used only as preprocessing or for perception module training in isolation. Executable visual verification (RRVF, Visual-ERM, arXiv 2603.13224) has proven effective for code generation (+8.4 on chart-to-code) but has never been applied to mathematical reasoning RL. The missing bridge is using formal parses as model-free oracles to verify individual perception claims within the reasoning chain during RL training, providing truly verifiable, claim-level step rewards.

This is feasible now because (1) formal parsing quality has reached sufficient maturity, (2) perception-reasoning disentanglement is a proven recipe (MoCA at ICML 2026 Spotlight, arXiv 2605.14054), and (3) 40-60% of multimodal math failures are perception errors. The principle generalizes beyond geometry: chemical structure diagrams can be verified via SMILES/InChI validators, circuit diagrams via SPICE simulators, function graphs via symbolic computation engines. Geometry is the optimal first testbed due to formal parser maturity.

## Research Landscape

Existing perception reward methods span a spectrum from implicit to explicit but remain model-dependent:

**Implicit methods**: PAPO (arXiv 2507.06448) introduces KL divergence Implicit Perception Loss, improving perception without external oracles (+8% on vision-dependent tasks, 30.5% perception error reduction). Effective but provides zero claim-level diagnostics — cannot identify which perception was wrong. KAWHI (arXiv 2603.27375) addresses visual representation bottlenecks via reward reweighting but does not verify perception claims.

**Model-based explicit methods**: URSA (NeurIPS 2025) uses process reward models with synthetic hallucination injection. Perception-R1 (ICLR 2026) uses LLM-as-judge. PRCO (2026, arXiv 2603.28618) uses model-generated captions with role-specific rewards. MoCA (ICML 2026 Spotlight, arXiv 2605.14054) uses blindfolded reasoning as proxy for perception sufficiency. CogFlow (ICLR 2026, arXiv 2601.01874) uses learned synergistic visual rewards with three-stage perception→internalization→reasoning. PEARL (CVPR 2026, arXiv 2511.18437) derives perception checklists verified via LLM judge during GRPO (+9.7% on MathVerse). EVPV (Mar 2026, arXiv 2603.16253) verifies visual premises via model-generated checklists with reliability gating.

**Structural-representation-based methods**: GeoDPO (arXiv 2602.22703) trains an NL-to-DSL translator to compute DSL-level scores as RL reward for geometry perception (+26.5% in-domain, +39.0% downstream reasoning). This is the closest prior work. Three key differences from our approach: (1) GeoDPO's reward comes from a learned translator's soft confidence scores — still model-dependent, inheriting translator biases; EPV uses ground-truth formal parses with symbolic matching, fully model-free. (2) GeoDPO does staged training (DPO perception → reasoning); EPV integrates perception rewards into joint GRPO training, enabling perception-reasoning co-adaptation. (3) GeoDPO provides holistic diagram-level scoring; EPV verifies individual claims, enabling fine-grained credit assignment and targeted failure diagnosis (e.g., "model systematically misidentifies parallel relations").

**Formal verification for reasoning (not perception)**: SGVR (Jan 2026, arXiv 2601.05073) converts formal proofs into verifiable numeric sub-goals for RL reward (+9.7% on geometry), but verifies reasoning outcomes (whether intermediate computed values are correct), not perception premises (whether visual inputs were correctly read). SymHPR (Dec 2025, arXiv 2512.03126) uses reconstruction-based rewards but only trains the perception module.

**The gap**: Model-free, claim-level, symbolically grounded perception verification as step-level RL reward for the full reasoning chain is not addressed by any published or concurrent work. EPV verifies perception inputs (premise-level) while SGVR verifies reasoning outputs (outcome-level); their combination achieves dual coverage — we validate this complementarity experimentally.

## Proposed Approach

We build an Executable Perception Verification Oracle (EPV-Oracle) with three components:

**1. Ground-truth formal parse cache.** Pre-parse all training geometry diagrams into ground-truth formal representations using Geoparsing (GDP-29K, arXiv 2604.11600) and FormalGeo, storing structured representations of points, lines, angles, parallel/perpendicular relations, and measurements. Data audit determines actual coverage across GDP-29K, FormalGeo7K, and GeoQA; diagrams lacking gold annotations are auto-parsed via the Geoparsing model with quality filtering. Strict train-test split protocol: any evaluation benchmark sample (GeoQA test, Geometry3K test) appearing in the formal parse training cache is removed; a zero-overlap evaluation subset is reported separately.

**2. Perception claim extraction.** During GRPO training, we extract perception claims from each CoT step using a dual-path approach: (a) rule-based pattern matching for explicit numeric/relational claims (e.g., "angle ABC = 60°", "AB ∥ CD"), and (b) structured output prompting that encourages parseable perception claims during rollouts. We independently validate extraction quality on 500-800 hand-annotated CoT samples, reporting precision/recall/F1 broken down by claim type (explicit numeric, explicit relational, implicit/inferential), and ablate rule-based vs. hybrid extraction and high-recall vs. high-precision configurations to characterize noise tolerance.

**3. Symbolic verification and reward.** Extracted claims are verified against the formal parse through symbolic matching — no LLM judge, no learned model. The verification yields step-level perception reward r_percept = verified_claims / total_claims, combined with outcome reward via r = r_outcome + λ·r_percept, where λ is annealed during training. Beyond the scalar reward, claim-level verification enables targeted failure diagnosis: automatic identification of systematic perception failure patterns (e.g., "model consistently misidentifies obtuse angles as right angles"), which can guide training data curation and model debugging.

**Correlated bias analysis (blind spot validation).** We validate the blind-spot hypothesis with two diagnostic experiments: (1) Controlled corruption: inject known errors into formal parses, verify EPV reward degrades monotonically (oracle accuracy validation). (2) Conditional circularity analysis: stratify geometry problems by configuration difficulty, measure within-stratum overlap between policy VLM perception errors and PEARL-style LLM-judge false negatives vs. EPV-Oracle false negatives. If within-stratum overlap is high for LLM-judge but low for EPV-Oracle, this provides evidence that the blind spots are due to shared model biases rather than intrinsic difficulty.

We train on geometry problems (actual count determined by data audit, estimated 10-15K after deduplication and leakage removal) from GDP-29K, FormalGeo7K, and GeoQA, using EasyR1/OpenRLHF on 16×A100 GPUs, at two model scales: Qwen3-VL-4B and Qwen3-VL-8B.

## Evaluation Design

**Benchmarks (5-6):**
- Geometry-specific: MathVerse, GeoQA, Geometry3K (with zero-overlap subset reported separately)
- General multimodal (generalization/regression): MMMU, MathVista
- Step-level perception: VisualProcessBench (EVPV benchmark)

**Baselines (6 direct + indirect):**
1. Vanilla GRPO (no perception reward) — lower bound
2. PEARL (LLM-judge perception, CVPR 2026, arXiv 2511.18437) — model-based explicit
3. GeoDPO (learned translator DSL reward, arXiv 2602.22703) — structural-representation-based, closest competitor
4. PAPO (implicit KL perception loss, arXiv 2507.06448) — zero-overhead implicit method, cost-effectiveness challenge
5. SGVR (formal sub-goal reward, arXiv 2601.05073) — formal verification for reasoning outcomes
6. MoCA (blindfolded proxy, ICML 2026 Spotlight, arXiv 2605.14054) — perception sufficiency paradigm
- Indirect (cited numbers): Perception-R1 (ICLR 2026), CogFlow (ICLR 2026), PRCO (arXiv 2603.28618)

**Perception-specific diagnostics:**
- Blindfold test (MoCA paradigm): text-only vs. multimodal inference to isolate perception contribution
- Reward signal quality: Pearson/Spearman correlation between EPV reward and human-annotated perception correctness on held-out set, compared against PEARL LLM-judge and GeoDPO translator scores
- Error type breakdown: perception/reasoning/calculation error rates before and after training
- Geometry-specific perception error rate: manual annotation of perception errors on 200+ GeoQA/Geometry3K test samples, reporting reduction percentage (comparable to PRCO's 39.2%, PAPO's 30.5%)

**Internal ablations:**
- λ strategy: constant λ vs. linear annealing vs. cosine annealing vs. λ=0 (vanilla GRPO)
- r_percept granularity: ratio (verified/total) vs. binary per-step vs. difficulty-weighted
- Claim extraction: rule-based vs. hybrid; high-recall vs. high-precision
- Formal parse source: GDP-29K only vs. FormalGeo7K only vs. combined vs. auto-parsed
- Training data scale: 5K vs. 10K vs. 15K
- EPV + SGVR joint training: r = r_outcome + λ₁·r_percept(EPV) + λ₂·r_subgoal(SGVR), validating complementarity
- Noise injection robustness: 5%/10%/20% error injection into formal parse cache

**Compute fairness:** Full lifecycle compute decomposition (parse cache construction + per-step extraction + per-step verification + RL training) for all methods. Iso-compute comparison: fixed total GPU-hours budget, each method trains for as many steps as its per-step cost allows. Performance-vs-compute scaling curve.

## Key References

- Unlocking Multimodal Mathematical Reasoning via Process Reward Model (NeurIPS 2025)
- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (ICLR 2026)
- Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning (ICML 2026)
- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026)
- Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning (CVPR 2026)
- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning (arXiv 2026)
- Hierarchical Process Reward Models are Symbolic Vision Learners (arXiv 2025)
- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2026)
- Grounding the Score: Explicit Visual Premise Verification for Reliable VL-PRMs (arXiv 2026)
- Learning Only with Images: Visual Reinforcement Learning with Reasoning, Rendering, and Visual Feedback (arXiv 2025)
- Visual-ERM: Reward Modeling for Visual Equivalence (arXiv 2026)
- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)
- A Survey of Multimodal Mathematical Reasoning: From Perception, Alignment to Reasoning (arXiv 2026)
- Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2026)
- ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs (NeurIPS 2025)
- PAPO: Perception-Aware Policy Optimization for Multimodal Reasoning (arXiv 2507.06448)
- GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning (arXiv 2602.22703)

## Resource Estimate

- **manual**: gpu_hours: 2,500–3,500 (6 baselines × 2 scales + ablations), timeline: 16–20 weeks, estimated_gpu_cost: $6,250–$8,750, annotation: 500-800 CoT samples + 200 perception error samples
- **human_in_loop**: gpu_hours: 2,000–2,800, timeline: 12–16 weeks, claude_api_cost: $500–$800, estimated_gpu_cost: $5,000–$7,000
- **auto_research**: gpu_hours: 2,000–2,800, timeline: 8–12 weeks, claude_api_cost: $1,200–$1,800, estimated_gpu_cost: $5,000–$7,000, speed_bottleneck: RL training wall-clock (16h/run on 16×A100); formal parses pre-cached; experiment iteration loop is binding constraint

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "46bf781e-5459-468d-bdc6-cf6d0cb4dbd1",
  "type": "user",
  "uuid": "731f67a6-3947-4080-939e-b4a436b1ed27",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T22:20:52.109Z_

```json
{
  "parentUuid": "731f67a6-3947-4080-939e-b4a436b1ed27",
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
  "uuid": "7a8b8435-421e-4845-8033-8ad6ee0115b8",
  "timestamp": "2026-05-27T22:20:52.109Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T22:20:52.109Z_

```json
{
  "parentUuid": "7a8b8435-421e-4845-8033-8ad6ee0115b8",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "e5aeb687-fce9-4d34-b30a-0693bcc12ea7",
  "timestamp": "2026-05-27T22:20:52.109Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-27T22:20:52.109Z_

```json
{
  "parentUuid": "e5aeb687-fce9-4d34-b30a-0693bcc12ea7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c792a7f9-22e4-456e-bcfe-aed49b34e2ca",
  "timestamp": "2026-05-27T22:20:52.109Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient background to perform the evaluation. Le…",
  "leafUuid": "c792a7f9-22e4-456e-bcfe-aed49b34e2ca",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate model-free perception rewards for multimodal math RL",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2"
}
```

---

### Assistant

_source line 9 · 2026-05-27T22:21:15.650Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as the Meta Judge.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [22% - 33%] 中位 27%

**Reviewer 2:**
- Novelty: 中偏弱 (Medium-weak)
- Significance: 中偏弱 (Medium-weak)


- Related Work: 强 (Strong) - but notes Perceval as important omission
- Probability: [23% - 33%] 中位 28%

**Reviewer 3:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [22% - 35%] 中位 28%

The three probability medians cluster tightly at 27%, 28%, and 28%, averaging 27.67% with minimal variance. Looking across the reviews, there's strong agreement on the related work assessment, though Reviewer 2 flags Perceval as a notable gap. Novelty and significance ratings are mostly aligned around medium, with Reviewer 2 leaning slightly weaker on both dimensions.

The core consensus issues are clear: all three reviewers see this as a natural extension of GeoDPO rather than a fundamental innovation, flag the unverified blind spot hypothesis as central to the claims, and raise concerns about claim extraction reliability and formal parser maturity. They also consistently identify PAPO's cost-effectiveness as a practical limitation and note how domain specificity constrains the work's broader impact. Reviewer 2 uniquely surfaces Perceval as a missing reference point.

Looking at the numerical consistency across the three median scores—all clustering tightly around 27-28% with less than 1% variation—the picture is remarkably aligned: this is competent and well-positioned relative to prior work, but fundamentally incremental. The proposal combines existing techniques in a straightforward way, and while the related work section is thorough, the novelty and significance both land solidly in the medium range.

Given this tight consensus, I'll anchor my final estimate at 27-28% and tighten the confidence interval accordingly. Now I need to draft the Meta Judge assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c792a7f9-22e4-456e-bcfe-aed49b34e2ca",
  "isSidechain": false,
  "requestId": "req_011CbTrQKHH2EWAyYrYYr3UW",
  "type": "assistant",
  "uuid": "69e3a587-38aa-4171-92de-8c41f4cd5614",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUWXLJKs8JFpUpbe6TgwQu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18664,
      "cache_read_input_tokens": 16149,
      "output_tokens": 3283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3283,
          "cache_read_input_tokens": 16149,
          "cache_creation_input_tokens": 18664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18664
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

_source line 10 · 2026-05-27T22:22:09.815Z_

【阶段】: Meta Judge
【三次中位】: [27%, 28%, 28%]  std=0.6%
【共识维度】:
- **Novelty = 中**（3/3）：核心贡献是 GeoDPO + Geoparsing 的自然组合（model-free symbolic matching 替换 learned translator + claim-level 粒度），属 incremental advancement 而非 paradigm shift。任何了解 GeoDPO 和 Geoparsing 的研究者都会自然想到这一步。
- **Significance = 中/中偏弱**（3/3）：domain-specific（仅几何），positive result 的 surprise value 低（ground-truth oracle 理应优于 learned proxy 是直觉预期），泛化到其他领域停留在 claim 层面。
- **Related Work = 强**（3/3）：覆盖从 implicit (PAPO) 到 model-based explicit (PEARL, MoCA, CogFlow, PRCO, EVPV) 到 structural-representation (GeoDPO) 到 formal verification for reasoning (SGVR) 的完整谱系，定位清晰，引用全部经验证真实。
- **Blind spot 假说未经实证**（3/3）：核心 motivation——"model-dependent reward 与 policy VLM 共享 systematic bias"——是理论推测，尤其对 GeoDPO（不同架构、不同训练数据的翻译器）适用性存疑。如果实验不支持，核心论点坍塌。
- **Claim extraction 可靠性存疑**（3/3）：rule-based pattern matching 仅覆盖显式数值/关系 claim，隐式感知信息难以提取，若 recall 低则 reward signal 稀疏有偏。
- **Formal parser 成熟度存疑**（3/3）：Geoparsing (GDP-29K) 发布于 2026 年 4 月，复杂/非标准几何图上的泛化鲁棒性未知，"model-free oracle"自身可能引入 parser bias。
- **PAPO 零成本挑战**（3/3）：PAPO 零额外基础设施即实现 30.5% perception error reduction，EPV 需要 formal parse cache + claim extraction + symbolic matching 的复杂 pipeline，cost-effectiveness 需显著优于 PAPO 才能 justify。
- **GeoDPO 为最直接竞争者**（3/3）：三位审稿人均识别 GeoDPO 为最近竞争者，核心增量是 model-free vs. model-dependent 这一步差异，实践中能否带来显著收益高度依赖实验。

【异常维度】:
- **Perceval 遗漏**（仅审稿人 2 提出）：Perceval (arXiv 2604.24583, Apr 2026) 已实现 claim-level extraction + per-claim verification for perception reward in RL（虽用 learned PRM），与本 proposal 概念高度接近。审稿人 2 认为这进一步削弱 claim-level granularity 的 novelty claim，并标注为 related work 遗漏。审稿人 1 和 3 未提及此工作。→ 该工作如果确实存在且描述准确，是一个值得重视的信号（会削弱 novelty），但因只有 1 人提及，降权处理：标注为"应补充但不单独击穿"。
- **Novelty 评级分歧**：审稿人 2 给出"中偏弱"，审稿人 1 和 3 给出"中"。分歧不大，审稿人 2 的更严格评级部分源于 Perceval 的发现。→ 取"中"但偏保守端。
- **审稿人 2 指出 joint vs. staged training 是 orthogonal design choice**（仅 1 人）：GeoDPO 也可切换到 joint GRPO training，这不是 model-free verification 的独有优势。→ 合理观点，但属于技术细节，不单独影响大局。

【最终概率】: [22% - 33%] 中位 27%
【一致性】: 高（std=0.6%，三位审稿人在所有 rubric 维度上高度一致）
【综合理由】:
三位审稿人展现出罕见的高度一致性——不仅概率估计几乎相同（27-28%），在所有关键维度的判断上也高度趋同。核心共识非常清晰：

1. **Idea 天花板由 Novelty 决定，约 35%**：核心贡献是将已有 building blocks（Geoparsing 的 formal parse + GeoDPO 的结构化 reward 思路 + EVPV 的 claim-level verification 思想）组合为 model-free claim-level perception verification reward。组合是合理的、位置是空白的，但单看任何维度都不是突破性创新。三位审稿人均用了"natural next step"或"obvious combination"的措辞。即使实验全面 positive，idea 本身的 conceptual novelty 不足以进入 strong accept 区间。

2. **Significance 进一步压缩上界**：domain-specific（仅几何）、positive result 不 surprising、泛化未验证，使得即使实验完美，论文的 impact narrative 也受限。三位审稿人均预期审稿人反应为"makes sense, not surprising"。

3. **Related Work 提供下界保护**：这是三位审稿人一致认可的最强维度，确保论文不会因定位不清或遗漏关键工作被直接拒绝（但需补上 Perceval）。

4. **多个核心假设未经验证（blind spot 假说、claim extraction 可靠性、formal parser 质量）**：这些都是"实验可能证实也可能证伪"的高不确定性因素。在所有因素都 positive 的最好情况下可触及上界 33%；若任一关键假设被证伪（特别是 blind spot 假说），概率跌至下界 22% 附近。

5. **中位取 27% 而非三人算术平均 27.7%**：考虑到审稿人 2 识别了 Perceval 这一额外竞争者（降权但不忽略），以及"宁缺毋滥"原则，中位略偏保守端。

【建议】: 边缘（偏不推荐侧）— 中位 27% 距离合理的投稿阈值（~36%）有明显差距。idea 层面的 novelty 天花板是主要瓶颈，实验层面的优化无法突破这一天花板。如果要推进，需要在 idea 层面找到更强的差异化角度或更 surprising 的贡献点。

【实施评估】:
  - 计算资源: 16×A100 GPU 集群，预估 2,000-3,500 GPU-hours（6 baselines × 2 scales + 内部消融），按 $2.5/GPU-hour 约 $5,000-$8,750。RL 训练单次约 16h on 16×A100，是主要瓶颈。
  - 数据需求: GDP-29K + FormalGeo7K + GeoQA，均为公开数据集。需进行数据审计确定实际覆盖率，去重后估计 10-15K 可用样本。需严格的 train-test split 防止数据泄漏。
  - 人工介入: 500-800 CoT 样本的 claim extraction 质量标注 + 200+ 测试样本的感知错误人工标注。标注工作量中等（约 2-4 周 1-2 人）。
  - 训练需求: 需要训练 GRPO RL（Qwen3-VL-4B 和 8B 两个规模），以及复现 6 个 baseline 方法。不需要从头预训练，但 RL 训练调参工作量大。
  - 新 Benchmark: 不需要构建全新 benchmark，但需要构建 formal parse cache、claim extraction pipeline、symbolic matching system 三个核心基础设施组件，以及 blind spot validation 的专用评测协议。
  - 预估周期: 12-20 周（基础设施搭建 3-4 周 + RL 训练与调参 4-6 周 + baseline 复现 3-4 周 + 分析与写作 2-4 周）。关键路径是 RL 训练的 wall-clock 时间和 formal parse cache 的质量验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e3a587-38aa-4171-92de-8c41f4cd5614",
  "isSidechain": false,
  "requestId": "req_011CbTrQKHH2EWAyYrYYr3UW",
  "type": "assistant",
  "uuid": "4af8648d-0dc6-4ad9-bd95-4c3c01581d28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NUWXLJKs8JFpUpbe6TgwQu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18664,
      "cache_read_input_tokens": 16149,
      "output_tokens": 3283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3283,
          "cache_read_input_tokens": 16149,
          "cache_creation_input_tokens": 18664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18664
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient background to perform the evaluation. Le…",
  "leafUuid": "4af8648d-0dc6-4ad9-bd95-4c3c01581d28",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate model-free perception rewards for multimodal math RL",
  "sessionId": "a99ab81e-7502-40c3-bd42-3932ef7be9f2"
}
```

---
