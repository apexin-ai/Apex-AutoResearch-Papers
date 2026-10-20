# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/9fb15aa1-ebee-4088-ae10-62bbd1cf90d5.jsonl`
- **Structured JSON:** [`eafa4e1be64fe3b2ffa6.json`](../../sessions/ea/eafa4e1be64fe3b2ffa6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:30:36.096Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:30:36.096Z",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have comprehensive research coverage. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- JuICE / \"Taming Knowledge Conflicts in Language Models\" (ICML 2025 Spotlight): 当前 RAG knowledge conflict 领域的 SOTA。发现 attention head 的 superposition 现象（同时参与 memory 和 context），提出 dual-run 干预。在 11 个数据集/6 个模型上达到最优。CirRAG 正确地将此作为 head-level 方法的局限性依据，论证 circuit-level 分析的必要性。\n- CoRect (arXiv 2602.08221, 2026): FFN 层级干预，通过 logit contrast 识别参数偏置层并修正 hidden states。关键发现：56.4% 的冲突案例存在 mid-layer 正确答案抑制（flip phenomenon）。CirRAG 将此作为电路验证的 ground-truth 轨迹——claim 成立。\n- SpARE (NAACL 2025 Oral): 基于 SAE 的表示工程，+10% EM，+15% 超过 contrastive decoding。单一机制（feature editing）干预。\n- ParamMute (NeurIPS 2025): FFN 抑制 + 知识偏好校准。引入 CoFaithfulQA benchmark。+6.17% faithfulness on LLaMA3-8B。\n- Basu et al. (arXiv 2502.08059, COLM 2025): 最直接的竞争工作。提取两个独立的 behavior-conditioned circuits（Context-Faithfulness 和 Memory-Faithfulness），通过 attention upweighting 实现 92% context override。核心局限：两个独立快照无法捕捉竞争动态。CirRAG 对此的差异化论述——\"arbiter structures\"只在两种信号同时活跃时才出现——在逻辑上成立且具有原创性。\n- CD-T (ICLR 2025): 秒级电路发现，97% ROC AUC。但仅在 GPT-2 规模上验证。这是 CirRAG 最大的可行性风险来源。\n- HAGD (arXiv 2601.12879, 2026): 层次化稀疏电路提取，支持 Llama-7B–70B。O(n² log n) 复杂度。报告 15-20% \"reconstruction dark matter\"。CirRAG 正确引用此作为电路稀疏性风险的依据。\n- Simulated Adoption (arXiv 2602.04918, 2026): 发现 override 机制是角度位移（orthogonal interference），而非幅度变化。在 Qwen-3-4B, Llama-3.1-8B, GLM-4-9B 上验证。\n- \"How Transformers Reject Wrong Answers\" (arXiv 2603.13259, 2026): 独立确认 rotational dynamics，在 1.5B-13B 模型上发现 correct/incorrect paths 通过旋转分离。\n- \"Retrieval Heads are Dynamic\" (arXiv 2602.11162, 2026): 发现检索头在不同生成时间步间动态变化，Jaccard 相似度低。直接挑战 head-level 方法的稳定性假设。\n- IRCAN (NeurIPS 2024), CAD (NAACL 2024), DoLa (ICLR 2024): 更早期的单机制方法，CirRAG 正确地将其作为 baseline 层级。\n\n- 调研总结: RAG knowledge conflict 的机制性理解正处于快速发展期，2025-2026 年密集涌现了大量从不同角度揭示冲突机制的工作（head superposition、FFN 抑制、rotational dynamics、检索头动态性）。然而，目前没有任何工作尝试将这些碎片化发现统一到一个端到端的因果电路中，更没有基于电路拓扑进行协调式多点干预。CirRAG 精准地占据了这个空白位置，且其 novelty claim 经调研验证成立。\n\n【整体印象】:\n作为审稿人，我的第一反应是**倾向 accept**，但带有保留意见。这是一篇对领域现状有极其深刻理解的 proposal，准确识别了多项 2025-2026 年最新发现之间的结构性联系，并提出了一个逻辑自洽、有清晰差异化的研究方向。\"arbiter structures\" 的预测是真正的原创概念，而非对已有工作的渐进组合。实验设计的完备性——分层 baseline、7 变体消融、intervention cardinality curve、fixed vs adaptive、discovery method sensitivity——表明作者对该领域的实验标准有成熟理解。主要保留意见在于：(1) 电路发现方法在 1-3B 甚至 8B 模型上的可行性尚未被充分验证（CD-T 仅在 GPT-2 上验证），(2) 系统复杂度较高（三重干预 + 自适应路由），实际能否协调工作存在执行风险。\n\n【核心贡献】:\n三层贡献结构清晰且层层递进：\n1. **C1（科学发现）**: 首个统一的 \"conflict resolution circuit\"——不是分别提取两种行为模式的电路，而是追踪竞争过程本身。\"Arbiter structures\" 的预测是关键差异化：这些结构在行为条件分析中结构性不可见，只有在统一建模时才能发现。这是对 Basu et al. 工作的实质性推进，而非渐进改良。\n2. **C2（方法）**: CirRAG 的协调式多点干预。\"Why not pipeline combination\" 一节出色地论证了为什么简单堆叠 JuICE + CoRect + rotational insight 不等价于 circuit-guided intervention（interference、suboptimal loci、instance-varying routing 三个论点均成立）。\n3. **C3（机制性贡献）**: \"Circuit topology as invariant\" 假说——将正确的分析单元从个体组件提升到电路拓扑——如果得到验证，将统一解释 head superposition 和 retrieval head dynamism 两个看似独立的现象。\n\n核心贡献对领域的价值：**高**。这不仅是又一个 RAG faithfulness 方法，而是试图建立该子领域的统一框架。即使 C2 的性能提升有限，C1 和 C3 本身也具有独立的科学价值。\n\n【方法合理性】:\n方法的逻辑链条（电路发现 → 验证 → 拓扑引导干预）是合理的。但存在以下需要审视的点：\n\n1. **更简单的替代方案问题**: 一个自然的质疑是\"为什么不直接在 Basu et al. 的两个电路基础上进行干预，而要重新发现统一电路？\" Proposal 对此的回应（arbiter structures 不可见于行为条件分析）在逻辑上成立，但需要实验验证。如果最终 arbiter structures 贡献的增量很小，那么统一电路发现的额外成本就不值得。\n\n2. **Rotational correction 的可操作性**: 三篇旋转动力学论文都停留在分析层面。将角度位移转化为干预手段的具体操作（rotation magnitude γ 的确定、旋转方向的选择）在 proposal 中未充分展开。这是方法中最模糊的部分。\n\n3. **Instance-adaptive routing**: 用轻量级 activation probe 确定电路子路径是合理的想法，但训练该 probe 需要标注数据（哪些实例激活了哪条子路径），这增加了方法复杂度。\n\n整体而言，方法架构合理，各组件有充分的文献支撑。风险主要在执行层面而非设计层面。\n\n【5 维度打分】:\n\n  1. 研究问题: 【强】 — 问题重要且时机恰当。RAG faithfulness 是当前 LLM 应用的核心挑战之一。五个独立研究方向（CD-T、head superposition、FFN suppression、rotational dynamics、retrieval head dynamism）的汇聚为统一框架提供了罕见的窗口期。研究问题的表述——\"What is the complete causal circuit governing RAG evidence override, and can circuit-topology-guided multi-point interventions outperform heuristic single-mechanism steering?\"——精确、可验证、有科学意义。此外，论文指出的更广泛影响（knowledge editing、instruction following under conflicts）增加了潜在研究价值。\n\n  2. 方法与创新: 【强】 — 与 Basu et al. (COLM 2025) 的差异化清晰且实质性：统一电路 vs 两个独立电路快照，\"arbiter structures\" 的预测是原创概念。与 JuICE (ICML 2025) 的差异化同样清晰：circuit topology 作为分析单元 vs 个体 attention heads。Rotational correction 作为三项旋转动力学发现的首次操作化（arXiv 2602.04918, 2603.13259, 2602.11169）是有说服力的 first-mover contribution。\"Why not pipeline combination\" 一节有效地回应了\"简单堆叠\"的质疑。轻微扣分因素：rotational correction 的具体实现细节不够充分。\n\n  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点之一。分层 baseline 设计（contrastive → neuron → mechanistic → CirRAG）完整覆盖了领域的方法谱系。Baseline 选择与当前 SOTA 完全对齐（JuICE、CoRect、ParamMute、SpARE、IRCAN、CAD、DoLa、Basu et al.）。消融设计极为全面：7 个组件变体、intervention cardinality curve（k=1,3,5,10,all）、fixed vs adaptive、strength sensitivity grid、circuit granularity、discovery method sensitivity。数据集覆盖了多种冲突类型（substitution、multi-dimensional、realistic、coherent）。Compute fairness（Pareto curve）和统计严谨性（seeds、bootstrap test）的承诺表明作者了解当前的实验标准。这套实验设计如果执行到位，足以支撑一篇顶会论文。\n\n  4. 可行性: 【中】 — 这是 proposal 的主要弱点。(a) CD-T 仅在 GPT-2 规模上验证；1-3B 模型上的电路发现是否可行存在不确定性。Proposal 的 staged scaling strategy 和 HAGD/HAP fallback 是合理的风险缓解措施，但不消除风险。(b) 系统包含三种不同类型的干预（edge amplification、FFN dampening、rotational correction）+ instance-adaptive routing，每个组件都有超参数（α、β、γ），交互效应可能难以管理。(c) 85% EM degradation threshold 作为 \"intervention-ready\" 标准是合理的，但如果电路分布性太高未达标，论文的核心故事（C2）将被削弱。好的方面是：proposal 对这些风险的认知和应对策略是成熟的，有清晰的 fallback plan（contribution pivots to C1+C3）。计算资源需求在合理范围内——主要实验在 1-3B 模型上完成，8B 为扩展实验。\n\n  5. 写作与呈现: 【强】 — Proposal 的组织结构清晰、逻辑链条紧密。从 problem → contributions → research opportunity → landscape → approach → experiments 的叙事流畅。文献引用精确且恰当，没有虚假引用或夸大他人工作的不足。\"Research Opportunity\" 一节将五个独立进展编织成统一叙事的能力突出。\"Circuit Sparsity Assumption\" 一节的诚实和科学严谨性是加分项。风险声明和 fallback plan 的透明度令人印象深刻。唯一的改进建议：rotational correction 的操作细节可以更具体。\n\n【概率估计】: [30% - 47%] 中位 38%\n\n【估计理由】:\n向上因素：(1) Novelty claim 经调研验证完全成立——无人做过统一冲突解决电路+拓扑引导多点干预，(2) \"arbiter structures\" 是原创性强的科学预测，(3) 实验设计在当前 AAAI/NeurIPS/ICML 投稿中属于上乘水平——baseline 层次分明、消融穷尽、统计严谨，(4) 研究时机极佳（5+ 独立发现的汇聚），(5) 三层贡献中任意两层成功即可支撑一篇好论文。\n向下因素：(1) 电路发现的可扩展性是实质性执行风险——CD-T 从 GPT-2 到 1-3B 的跨越并非 trivial，(2) 系统复杂度高——三重干预+自适应路由的工程和调参负担大，(3) \"arbiter structures\" 如果不存在或效果微弱，C1 的核心差异化将被削弱，(4) Rotational correction 的操作化细节不足可能被审稿人追问，(5) 仅使用 base models，与 RAG 实际应用场景（instruct models）存在 gap。\n中位 38% 反映了：这是一篇方向正确、创新清晰、实验设计优秀的 proposal，但其核心承诺（统一电路发现、arbiter structures、coordinated intervention 的优越性）需要实验证据支撑，执行风险使其处于 borderline accept 区间。\n\n【主要风险】:\n1. **电路发现可扩展性失败**: 如果 CD-T 在 1-3B 模型上无法产出足够稀疏/忠实的电路（EM degradation < 85% 阈值），论文的核心方法贡献 (C2) 将退化为有限的 case study。虽然有 HAGD fallback，但切换发现方法可能影响下游干预的精度和一致性。\n2. **Arbiter structures 不存在或贡献微弱**: 如果统一电路与 Basu et al. 两个独立电路的并集差异极小，那么 C1 的核心 novelty——\"arbiter structures only visible in unified analysis\"——将被根本性否定，论文退化为\"用 circuit 信息指导 intervention placement\"，与 Basu et al. 的 circuit steering 差异化减弱。\n\n【实施评估】:\n  - 计算资源: 中等。核心实验在 1-3B 模型上（单 GPU 可完成），8B 扩展实验需多卡或 A100。Circuit discovery 的一次性成本取决于方法（CD-T 秒级但可能需多次迭代，HAGD 更重）。Baseline 复现需额外计算。估计总需求：2-4× A100 GPU，数周时间。\n  - 数据需求: 低。所有数据集均为已有公开 benchmark（ConflictQA、NQ-Swap、MemoTrap、ConFiQA、CoFaithfulQA），无需新数据收集。\n  - 人工介入: 低-中。电路分析结果的解读和 arbiter structure 识别可能需要人工判断。Intervention 超参数（α、β、γ）的调节需要实验迭代。\n  - 训练需求: 低。CirRAG 是 training-free 的推理时干预方法。Instance-adaptive routing 的 activation probe 需要少量训练，但数据来自电路分析的副产品。\n  - 新 Benchmark: 否。使用已有 benchmark，无需构建新 benchmark。\n  - 预估周期: 10-14 周。Stage 1（电路发现 + 调试）3-4 周，Stage 2（验证 + arbiter 分析）2-3 周，Stage 3（CirRAG 设计 + 调参 + 消融）3-4 周，写作 2-3 周。8B 扩展实验可能额外需要 2-3 周。\n```\n\nSources:\n- [JuICE - Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)\n- [CoRect - Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221)\n- [SpARE - SAE-Based Representation Engineering (NAACL 2025)](https://aclanthology.org/2025.naacl-long.264/)\n- [ParamMute - Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://arxiv.org/html/2502.15543)\n- [Basu et al. - Mechanistic Circuits for Extractive QA (COLM 2025)](https://arxiv.org/abs/2502.08059)\n- [CD-T - Efficient Automated Circuit Discovery (ICLR 2025)](https://arxiv.org/abs/2407.00886)\n- [HAGD - Hierarchical Sparse Circuit Extraction](https://arxiv.org/abs/2601.12879)\n- [Simulated Adoption - Decoupling Magnitude and Direction](https://arxiv.org/abs/2602.04918)\n- [How Transformers Reject Wrong Answers - Rotational Dynamics](https://arxiv.org/abs/2603.13259)\n- [Retrieval Heads are Dynamic](https://arxiv.org/abs/2602.11162)\n- [ReDeEP - Detecting Hallucination via Mechanistic Interpretability (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf)\n- [Where Knowledge Collides - Mechanistic Study of Knowledge Conflict](https://arxiv.org/pdf/2601.09445)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile my comprehensive evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [JuICE: Taming Knowledge Conflicts in Language Models](https://arxiv.org/abs/2503.10996) (ICML 2025 Spotlight): 发现注意力头在 context 和 memory 功能上存在 superposition，提出 dual-run test-time intervention。在 11 个数据集、6 个模型架构上达到 SOTA。是本 proposal 最直接的 head-level baseline，CirRAG 需要证明 circuit-level 分析能超越 head-level heuristic。\n\n- [ParamMute: Suppressing Knowledge-Critical FFNs for Faithful RAG](https://arxiv.org/abs/2502.15543) (NeurIPS 2025): 识别中深层 FFN 对不忠实生成的不成比例激活，通过抑制这些 FFN 提高忠实度 +6.17%/+54.63%。是 FFN-level 单机制方法的代表。\n\n- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221) (arXiv 2026): 通过 logit 对比定位 parametric bias 层并做 hidden state 修正。发现 56.4% 的冲突案例存在中层 correct-answer suppression（\"flip phenomenon\"）。提供了本 proposal 关键的 validation trajectory。\n\n- [SpARE: Steering Knowledge Selection via SAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.264/) (NAACL 2025 Oral): 利用 SAE 特征编辑内部激活，+10% EM / +15% over contrastive decoding。SAE feature-level 方法代表。\n\n- [CD-T: Efficient Automated Circuit Discovery using Contextual Decomposition](https://arxiv.org/abs/2407.00886) (ICLR 2025): 秒级 circuit 发现，支持 position-level 精度，97% ROC AUC。但验证规模主要在 GPT-2 级别，向 1-3B+ 扩展存在不确定性。\n\n- [Basu et al.: On Mechanistic Circuits for Extractive QA](https://arxiv.org/abs/2502.08059) (COLM 2025): 提取两个独立 circuits（Context-Faithfulness / Memory-Faithfulness），通过 CMA 方法。核心局限性正如 proposal 所述——两个独立快照无法捕捉竞争动态。\n\n- [Retrieval Heads are Dynamic](https://arxiv.org/abs/2602.11162) (arXiv 2026): 证明 retrieval heads 在不同生成步骤间动态变化，Jaccard similarity 低于静态识别，直接挑战 head-level 方法的稳定性假设。\n\n- [How Transformers Reject Wrong Answers: Rotational Dynamics](https://arxiv.org/abs/2603.13259) (arXiv 2026): 证实 factual constraint processing 通过旋转（方向性位移）而非缩放实现，在 1.5B-13B 模型上验证。为本 proposal 的 rotational correction 组件提供理论基础。\n\n- [HAGD: Hierarchical Sparse Circuit Extraction](https://arxiv.org/abs/2601.12879) (arXiv 2026): 将 circuit 发现复杂度降至 O(n² log n)，在 Llama-7B 到 70B 上验证。报告 15-20% \"reconstruction dark matter\"，对 proposal 的 circuit sparsity 假设构成挑战，也是重要的 fallback 方法。\n\n- [IRCAN: Identifying and Reweighting Context-Aware Neurons](https://openreview.net/) (NeurIPS 2024): 通过 integrated gradients 识别 context-aware neurons 并 reweight。Neuron-level 方法代表。\n\n- [Mechanistic Interpretability for LLM Alignment](https://arxiv.org/abs/2602.11180) (arXiv 2026): 综述 circuit discovery 应用于 alignment，涵盖 multi-token activation patching，表明领域正从分析走向干预，但 coordinated multi-point intervention 仍属前沿。\n\n- 调研总结: RAG 知识冲突领域极其活跃（2024-2026 年有 7+ 篇顶会论文），但现有方法均为单机制启发式干预（head-level / FFN-level / feature-level），**尚无工作从端到端因果电路角度进行统一分析和协调多点干预**。Proposal 所识别的 gap 是真实且重要的。竞争激烈但差异化清晰。\n\n【整体印象】:\n\n作为审稿人，我的第一反应是 **lean accept with reservations**。这是一份异常成熟的 proposal：研究问题定义精准，文献综述几乎穷尽了 2024-2026 年的所有相关工作，方法论框架有清晰的理论动机，实验设计的完备程度（baselines 分层、ablation 7 变体、统计严谨性）远超大多数投稿。核心的 novelty claim——unified conflict resolution circuit + circuit-topology-guided multi-point intervention——经调研确认是真实的学术空白。\n\n主要顾虑在于：(1) 项目极其宏大（circuit discovery + validation + intervention method + topology invariance hypothesis），单篇论文可能无法充分展开；(2) 关键技术依赖（CD-T scaling、circuit sparsity）存在实质性风险；(3) 若 arbiter structures 不存在或 circuit 过于分散，C1 的核心预测会落空。\n\n但 proposal 对这些风险有诚实的承认和备选方案（circuit sparsity threshold、discovery method fallback、contribution pivot strategy），这显示出研究成熟度。\n\n【核心贡献】:\n\n三层贡献结构，递进合理：\n\n1. **C1 (Scientific Discovery)**: 首个统一的 conflict resolution circuit，特别是 \"arbiter structures\" 的预测——仅在 context 和 parametric signals 同时活跃时才出现的节点/边。这是对 Basu et al. (COLM 2025) 两个独立 circuit 方法的直接超越，科学价值明确。\n\n2. **C2 (Method)**: CirRAG 的三组件协调干预（edge amplification + FFN dampening + rotational correction）。Rotational correction 组件是将三篇独立的 rotational dynamics 分析工作（arXiv 2602.04918, 2603.13259, 2602.11169）首次转化为可操作的干预手段，这一点确实 novel。\n\n3. **C3 (MI Contribution)**: \"circuit topology as invariant\" 假说——解释 retrieval heads 为何动态变化（头是 circuit role 的可互换实例化）以及为何 superposition 出现（同一头可在不同 context 下填充不同 circuit 位置）。若验证成功，这将为 mechanistic interpretability 领域提供重要的统一解释框架。\n\n**领域价值评估**: C1 和 C3 若能验证，对 mechanistic interpretability 社区有较高价值；C2 若能在实验中超越 JuICE 和 ParamMute，对 RAG 应用社区有直接实用价值。三个贡献互相支撑但也互相依赖——这既是优势也是风险。\n\n【方法合理性】:\n\n**合理性**: 整体方法论框架是合理的。从 circuit discovery → validation → intervention 的三阶段流程逻辑清晰。利用 CD-T 的 contextual decomposition 将 context tokens 定义为 \"relevant partition\" 来追踪 evidence propagation 是自然的适配。Staged scaling strategy（1-3B core → 8B hierarchical decomposition → fallback methods）务实。\n\n**替代方案分析**: Proposal 自己在 \"Why not pipeline combination?\" 部分很好地论证了为什么简单堆叠 JuICE + CoRect + rotational insight 不行——因为缺少 circuit topology 信息会导致 interference、suboptimal loci、和 instance-varying routing 问题。这是有说服力的论证。\n\n**潜在问题**:\n- **Rotational correction 的实际操作化**: 三篇 rotational dynamics 论文都是分析性工作；将 angular displacement findings 转化为具体的 \"rotational correction at copy-suppression bottlenecks\" 需要定义：(a) 旋转方向如何确定？(b) 旋转幅度如何校准？(c) 在高维空间中的旋转是否能 generalize across instances？Proposal 在这一关键细节上较为模糊。\n- **Instance-adaptive routing**: \"a lightweight activation probe determines which circuit sub-path the current instance activates\" ——这个 probe 的训练数据从哪来？准确率预期如何？若 probe 不准确，adaptive 可能不如 fixed。Proposal 安排了 fixed-vs-adaptive ablation，但没有详述 probe 设计。\n- **Arbiter structure 的可验证性**: 比较 unified circuit 与 two separate circuits 的 union，找到存在于 unified 但不存在于两个独立 circuit 中的节点。但这可能只是因为两种 circuit extraction 方法的噪声/不完整性，而非真正的 \"arbiter structures\"。需要更强的 causal evidence（如 ablate 这些 nodes 后 conflict resolution behavior 发生定性变化）。\n\n【5 维度打分】:\n\n1. **研究问题**: 【强】 \n   — 问题重要且时机恰当。RAG faithfulness 是 LLM 应用的核心挑战，现有方法（JuICE ICML'25, ParamMute NeurIPS'25, SpARE NAACL'25, CoRect arXiv'26）均为单机制启发式干预，缺乏端到端因果理解。五项 2025-2026 年的独立进展（CD-T, rotational dynamics ×3, dynamic retrieval heads）恰好为 circuit-level 分析提供了工具和理论基础。\"Unified conflict resolution circuit\" 的研究问题是自然的下一步。\n\n2. **方法与创新**: 【强】 \n   — 核心 novelty 经调研确认成立：(a) 无现有工作追踪完整的 RAG evidence override 因果电路（Basu et al. COLM'25 最接近但只有两个独立电路）；(b) 无现有工作做 circuit-topology-guided multi-point intervention；(c) rotational correction 作为干预手段是首创（三篇 2026 分析论文均停留在发现层面）。方法的 \"principled-ness\"——由 circuit topology 指导干预位置而非 heuristic——是对现有方法的本质提升。扣分点：rotational correction 的操作化细节不足，instance-adaptive probe 设计模糊。\n\n3. **实验设计**: 【强】 \n   — 这是本 proposal 最突出的优势之一。Baselines 分 4 层（contrastive decoding → neuron/representation → mechanistic intervention → CirRAG），涵盖了 2024-2026 年几乎所有 SOTA 方法。Ablation 设计 7 变体 + intervention cardinality curve + fixed-vs-adaptive + strength sensitivity grid + circuit granularity + discovery method sensitivity，非常完备。评测指标覆盖 faithfulness、side-effect、efficiency 三个维度，并承诺 paired bootstrap test 和 N=3 seeds。Compute fairness（offline/online 分离 + Pareto 曲线）也是好做法。数据集选择（ConflictQA, NQ-Swap, MemoTrap, ConFiQA, CoFaithfulQA, JuICE coherent partition）覆盖了 substitution/multi-dimensional/realistic/coherent 四种冲突类型。\n\n4. **可行性**: 【中】 \n   — 最主要的风险源：(a) CD-T 向 1-3B 扩展缺乏先例验证，虽有 HAGD 作为 fallback，但不同 discovery 方法产生的 circuit 可能质量差异大，影响下游 intervention；(b) circuit sparsity 假设——HAGD 报告 15-20% dark matter，若冲突解决行为高度分布式，CirRAG intervention 效果会受限（proposal 设了 85% EM threshold，但这是否足够保守？）；(c) 整体工程复杂度很高（circuit discovery + validation + 3 组件 intervention + instance-adaptive probe），对团队执行力要求极高；(d) 1-3B 模型上的结果可能难以令审稿人信服（主流关注 7-8B+），但 proposal 对此有 scaling plan。Proposal 对风险的自我认知是优秀的（circuit sparsity acknowledgment, contribution pivot strategy），但风险本身是实质性的。\n\n5. **写作与呈现**: 【强】 \n   — Proposal 逻辑极其清晰：从 problem → gap → opportunity → contributions → approach → experiments，每一步都有充分论证。文献综述几乎无遗漏，且对每篇 related work 都精确描述了其 limitation 以及与本工作的关系。\"Why not pipeline combination?\" 段是优秀的 preemptive defense。Staged scaling strategy 和 circuit sparsity acknowledgment 显示出科研成熟度。唯一的担忧是内容量巨大——三个 contributions + 三阶段 approach + 六个 ablation studies，在 AAAI 8 页主体限制内可能需要非常精炼的写作。\n\n【概率估计】: [33% - 48%] 中位 40%\n\n【估计理由】:\n\n**上界 (48%) 对应的情景**: Circuit discovery 在 1-3B scale 成功并产生清晰、稀疏的 conflict resolution circuit；arbiter structures 被发现并通过 causal ablation 验证；CirRAG 在主要 benchmark 上超越 JuICE 和 ParamMute 达到 statistically significant margins；topology invariance 假说得到初步验证。在这一情景下，论文具有三个互相支撑的强贡献（scientific discovery + method + MI insight），实验全面且结果亮眼，会是一篇非常有竞争力的投稿。\n\n**下界 (33%) 对应的情景**: Circuit 发现面临 scaling 挑战，需要使用 fallback method；circuit 较为分散（85% 阈值勉强达到或未达到），CirRAG 在某些 benchmark 上未能显著超越 JuICE（JuICE 作为 ICML Spotlight 有很高的 bar）；arbiter structures 的证据不够决定性。但即便如此，circuit discovery 本身（C1）和 topology invariance 假说（C3）仍有科学贡献价值，实验设计的完备性也会获得认可。\n\n**中位 40% 的判断依据**: (1) 研究问题和 novelty claim 经调研确认是真实且重要的；(2) 实验设计的完备程度在 proposal 阶段已远超平均水平；(3) 但核心技术依赖存在实质性不确定性（scaling, sparsity），且项目极其宏大，执行风险不可忽视；(4) 竞争领域——JuICE (ICML Spotlight), ParamMute (NeurIPS) 已经设了很高的 bar，新方法需要令人信服的实证优势。AAAI 接受率约 20-25%，40% 意味着这篇投稿显著高于平均质量，但仍存在相当的被拒风险。\n\n【主要风险】:\n1. **Circuit sparsity 假设不成立**: 如果 RAG evidence override 行为在 LLM 中高度分布式（HAGD 的 dark matter 证据指向此方向），circuit-guided intervention 将无法提供比 heuristic methods 有意义的改进。此时 C2 (CirRAG method) 的价值大幅缩水，论文需要靠 C1 和 C3 支撑，但纯分析性工作在应用导向的 reviewer 那里可能评价不高。\n2. **JuICE baseline 难以超越**: JuICE 是 ICML 2025 Spotlight，在 11 个数据集、6 个模型架构上达到 SOTA，且方法简洁（test-time attention intervention, no training）。CirRAG 需要证明 circuit-guided approach 的额外复杂度（offline circuit discovery, instance-adaptive probe）换来了显著的性能提升。若改进幅度小或不一致，reviewer 会质疑 complexity-performance tradeoff。\n\n【实施评估】:\n  - 计算资源: **中高需求**。Circuit discovery（CD-T 或 HAGD）在 1-3B 模型上可能需要数十 GPU-hours，在 8B 模型上需求更大（HAGD 在 Llama-70B 上的成本未明确）。CirRAG intervention 评估涉及 8+ baselines × 6+ 数据集 × 3 seeds × 多个 ablation 变体。估计需 4-8× A100/H100 GPU 持续使用 4-8 周。\n  - 数据需求: **低**。所有数据集（ConflictQA, NQ-Swap, MemoTrap, ConFiQA, CoFaithfulQA）均为已有公开数据集，无需新数据收集。JuICE 的 coherent conflict partition 也已公开。\n  - 人工介入: **中**。Circuit interpretation 和 arbiter structure identification 可能需要 manual inspection 来验证 automated discovery 的结果。Rotational correction 的具体参数化可能需要实验迭代。\n  - 训练需求: **低-中**。CirRAG 本身是 training-free intervention。Instance-adaptive probe 需要少量训练（但规模小）。Circuit discovery 是 inference-time forward pass，不涉及模型训练。\n  - 新 Benchmark: **否**。使用已有 benchmarks，不需要构建新 benchmark。\n  - 预估周期: **3-5 个月**。Stage 1 (circuit discovery + scaling): 4-6 周；Stage 2 (validation): 2-3 周；Stage 3 (CirRAG design + tuning): 3-4 周；实验 + ablation: 4-6 周；写作: 2-3 周。关键路径在 Stage 1 的 scaling 是否顺利。\n```\n\nSources:\n- [JuICE: Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)\n- [ParamMute: Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://arxiv.org/abs/2502.15543)\n- [CoRect: Context-Aware Logit Contrast (arXiv 2026)](https://arxiv.org/abs/2602.08221)\n- [SpARE: SAE-Based Representation Engineering (NAACL 2025)](https://aclanthology.org/2025.naacl-long.264/)\n- [CD-T: Efficient Automated Circuit Discovery (ICLR 2025)](https://arxiv.org/abs/2407.00886)\n- [Basu et al.: Mechanistic Circuits for Extractive QA (COLM 2025)](https://arxiv.org/abs/2502.08059)\n- [Retrieval Heads are Dynamic (arXiv 2026)](https://arxiv.org/abs/2602.11162)\n- [How Transformers Reject Wrong Answers: Rotational Dynamics (arXiv 2026)](https://arxiv.org/abs/2603.13259)\n- [HAGD: Hierarchical Sparse Circuit Extraction (arXiv 2026)](https://arxiv.org/abs/2601.12879)\n- [IRCAN: Identifying and Reweighting Context-Aware Neurons (NeurIPS 2024)](https://openreview.net/)\n- [Mechanistic Interpretability for LLM Alignment (arXiv 2026)](https://arxiv.org/abs/2602.11180)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have comprehensive context on the field. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- JuICE / \"Taming Knowledge Conflicts in Language Models\" (ICML 2025 Spotlight): 当前 SOTA，跨 11 数据集/6 模型架构。发现 attention head 存在 context-memory superposition，采用 dual-run 方式干预。是 CirRAG 最强的 baseline——CirRAG 必须在这个基础上展示统计显著的增益才有说服力。\n- Basu et al. \"On Mechanistic Circuits for Extractive QA\" (COLM 2025, arXiv 2502.08059): 提取 context-faithfulness 和 memory-faithfulness 两条独立 circuit，并用 ATTNATTRIB 实现数据归因和 steering。CirRAG 提出的\"unified conflict circuit\"和\"arbiter structures\"直接针对该工作的 two-circuit 局限。\n- CoRect (arXiv 2602.08221, 2026): 通过 logit contrast 定位 FFN parametric suppression 层并在推理时修正 hidden state。报告了 56.4% 的 mid-layer flip phenomenon——CirRAG 将其作为 circuit 验证的 ground truth。\n- ParamMute (NeurIPS 2025): 抑制 knowledge-critical FFN，在 LLaMA3-8B 上提升 6.17% faithfulness。引入了 CoFaithfulQA benchmark。\n- SpARE (NAACL 2025 Oral): 基于 SAE 的 representation engineering，+10% EM，+15% 超越 contrastive decoding 方法。\n- CD-T (ICLR 2025): 秒级 circuit discovery，97% ROC AUC，但**仅在 GPT-2 级别验证过**。这是 CirRAG 面临的关键 scaling 瓶颈。\n- HAGD (arXiv 2601.12879, 2026): 支持 Llama-7B 到 70B 的 hierarchical circuit extraction，但有 15-20% \"reconstruction dark matter\"且**不建模 attention circuit**——而 CirRAG 核心依赖 attention 分析。\n- \"Retrieval Heads are Dynamic\" (arXiv 2602.11162, 2026): 发现 retrieval heads 跨 timestep 动态变化（Jaccard 0.18-0.46），挑战了 head-level 方法的稳定性假设，为 CirRAG 的 topology-level 分析提供动机。\n- \"How Transformers Reject Wrong Answers\" (arXiv 2603.13259, 2026): 确认 correct/incorrect paths 通过 rotation 而非 rescaling 分离，1.6B 参数出现 phase transition。\n- ReDeEP (ICLR 2025): 首个将 mechanistic interpretability 用于 RAG hallucination 检测的工作，但聚焦检测而非干预。\n\n- 调研总结: RAG faithfulness 的机制干预已进入\"百花齐放\"阶段——2024-2026 涌现了大量各攻一个机制的方法（head/FFN/SAE/decoding），但尚无工作尝试端到端的 causal circuit 发现和基于 topology 的 coordinated multi-point intervention。CirRAG 瞄准的缝隙真实存在，但竞争极为激烈（JuICE ICML Spotlight 是硬标杆），且 circuit discovery 的 scaling 是领域级难题。\n\n【整体印象】:\n作为审稿人，我的第一反应是：这是一份 research maturity 极高的 proposal。对领域的理解深度、对 related work 的精准定位、对 contribution 的差异化表述、以及实验设计的完备性，都明显高于平均水平。\n\n核心叙事——\"五条独立研究线索在 2025-2026 汇聚，创造了一个 unified circuit 分析的窗口\"——构建得很有说服力。三个贡献 (C1 科学发现, C2 方法, C3 机制可解释性假设) 互相支撑，形成一个有内在一致性的研究议程。\n\n但我会倾向 **weak accept / borderline**，原因是：(1) scope 极为宏大，单篇论文能否同时交付 circuit discovery + multi-point intervention + topology invariance hypothesis 的充分实证？(2) 核心方法依赖 CD-T 的 scaling，而 CD-T 尚未在 >GPT-2 规模验证，fallback 方案 (HAGD) 不建模 attention——这不是小风险；(3) 竞争对手 JuICE 已经在 11 数据集 6 模型上 SOTA，CirRAG 的增量收益可能有限。\n\n【核心贡献】:\n1. **C1 (Unified Conflict Resolution Circuit)**: 首次追踪 RAG evidence override 的完整 causal circuit，并预测 \"arbiter structures\" 的存在——这是 Basu et al. 的 two-circuit 方法论上无法发现的结构。如果验证成功，这是一个真正的科学发现。\n2. **C2 (CirRAG Method)**: 基于 circuit topology 的 coordinated multi-point intervention，将 rotational dynamics 的分析洞察首次转化为干预手段。\n3. **C3 (Topology Invariance Hypothesis)**: 提出 circuit functional topology 是底层计算不变量，为 retrieval head dynamism 和 superposition 提供统一解释。\n\n贡献价值：如果 C1 的 arbiter structures 被验证，这对 mechanistic interpretability 领域有显著影响。C2 的实用价值取决于是否能显著超越 JuICE。C3 是一个有深度的假设，但验证难度高。总体而言，这是一个\"high risk, high reward\"的研究议程。\n\n【方法合理性】:\n方法的总体逻辑合理：先发现 circuit → 用 topology 指导干预位点 → 多点协调干预。这比 heuristic single-mechanism 方法在理论上更有吸引力。\n\n**关键质疑**:\n1. **更简单的替代方案**: 为什么不直接组合 JuICE (head) + CoRect (FFN) + SpARE (SAE feature) 的干预，用简单的 grid search 找最优组合？proposal 的 \"Why not pipeline combination?\" 一节给出了三个论点 (interference, suboptimal loci, instance-varying routing)，但这些论点是假设性的——在没有实验数据的情况下，一个 well-tuned pipeline combination 可能就够了。建议在实验中加入这个 baseline。\n2. **Rotational correction 的具体操作**: proposal 提到\"apply angular corrections at copy-suppression bottlenecks\"，但具体参数化方式不够明确。rotation 在高维空间中有很多可能的操作方式（Givens rotation? projection? subspace alignment?），这需要更详细的说明。\n3. **Instance-adaptive routing 的 overhead**: 一个 lightweight activation probe 能否在不引入显著延迟的情况下准确判断 circuit sub-path？这需要仔细的 latency 分析。\n\n【5 维度打分】:\n\n  1. 研究问题: 【强】 — RAG evidence override 是 LLM 部署的核心痛点之一。现有方法各攻一点、缺乏 unified understanding 的问题被清晰识别。五条研究线索的汇聚论述有说服力。研究问题既有实用价值 (improving RAG faithfulness) 又有科学价值 (understanding conflict resolution mechanisms)。\n\n  2. 方法与创新: 【中偏强】 — 创新点真实存在：(a) unified circuit 相对于 Basu et al. 的 two-circuit 是一个有意义的推进；(b) rotational correction 作为首个 intervention operationalization 有独特性；(c) multi-point coordinated intervention 的理念合理。但 novelty 的实质性取决于 arbiter structures 是否真的存在、是否与 Basu union of circuits 有显著差异。方法的核心依赖 (CD-T scaling) 引入了不确定性。相比 JuICE (ICML 2025 Spotlight) 的简洁优雅（just run twice），CirRAG 的复杂度显著更高，能否带来 proportional 的性能增益是关键问题。\n\n  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点之一。四类数据集覆盖 substitution/multi-dimensional/realistic/coherent conflicts。Baselines 按机制复杂度分四层，涵盖了所有重要工作。Ablation 设计极为完备（7 component variants, intervention cardinality curve, fixed vs adaptive, strength sensitivity, circuit granularity, discovery method sensitivity）。Compute fairness 的 accuracy-vs-latency Pareto curve 和 offline/online 成本分离也是加分项。统计严格性 (3 seeds + paired bootstrap) 达标。**唯一缺失**: 缺少一个 \"naive pipeline combination\" baseline（JuICE + CoRect + rotational insight 的简单组合）来直接验证 circuit-guided 定位的增量价值。\n\n  4. 可行性: 【中】 — 这是最大的风险维度。(a) CD-T 仅在 GPT-2 验证过，proposal 的核心实验需要 1-3B 甚至 8B 模型——scaling gap 显著。fallback 方案 HAGD 不建模 attention circuit，对本工作是硬伤。(b) Circuit sparsity assumption 如果不成立，C2 的价值大幅缩水。proposal 的 85% EM degradation threshold 和 \"pivot to C1+C3\" fallback 是成熟的风险管理，但这意味着 paper 的核心卖点可能无法兑现。(c) 三个 contributions 的 scope 对单篇论文来说过于宏大——circuit discovery、intervention method、topology invariance hypothesis 每一个都足以独立成文。(d) 预估周期可能偏紧。\n\n  5. 写作与呈现: 【强】 — Proposal 的叙事结构清晰、逻辑严密。\"Research Opportunity\" 节的五线汇聚论述特别出色。对 related work 的定位精准，每个 contribution 相对于 prior work 的差异化都说得很清楚。风险的坦诚披露和 fallback plan 增加了可信度。唯一可改进的是 rotational correction 的技术细节需要更具体。\n\n【概率估计】: [30% - 44%] 中位 37%\n\n【估计理由】:\n优势面：研究问题重要且 timely (强)、文献定位极为精准、实验设计在 proposal 阶段已接近顶会论文水平、三个 contribution 有内在一致性且各自有 novelty claim。这些特质使其显著高于平均投稿质量。\n\n劣势面：(1) **执行风险高**——CD-T scaling 是 uncharted territory，如果 circuit discovery 在 1-3B 模型上不 work 或过于 distributed，整个方法链条断裂；(2) **强竞争**——JuICE 已在 ICML 2025 以 Spotlight 发表且方法更简洁，CirRAG 需要展示明显且一致的增益；(3) **scope 过大**——三个 contribution 可能导致每个都不够深入，reviewer 可能质疑\"是 circuit discovery paper 还是 intervention paper 还是 interpretability paper\"；(4) **circuit sparsity assumption 未验证**——如果 conflict resolution 是 distributed computation，核心方法不成立。\n\n中位 37% 反映：这是一篇 direction 正确、craftsmanship 出色、但执行风险显著的投稿。如果实验结果支撑叙事（arbiter structures 被发现、CirRAG 统计显著超越 JuICE），可以冲击 strong accept (概率上界 44%）。如果 circuit discovery scaling 遇阻或性能增益 marginal，可能落入 borderline reject (概率下界 30%)。\n\n【主要风险】:\n1. **Circuit Discovery Scaling 瓶颈**: CD-T 仅在 GPT-2 (~117M) 验证过，proposal 需要在 1-3B 甚至 8B 模型上工作。Fallback 方案 HAGD 不建模 attention circuit——而 attention 是 RAG conflict resolution 的核心组件（JuICE 已证明）。如果两者都无法在目标规模上提供 fine-grained 且 faithful 的 circuit，整个方法基础崩塌。\n2. **增量收益 vs 方法复杂度**: JuICE 方法极其简洁 (\"just run twice\") 已达 SOTA，CirRAG 引入了 circuit discovery (offline GPU-hours) + activation probe (online latency) + 3-component coordinated intervention 的复杂 pipeline。如果最终性能增益仅在 1-3% EM 的统计噪声范围内，reviewer 会质疑 complexity-benefit tradeoff。\n\n【实施评估】:\n  - 计算资源: **高**。Circuit discovery 阶段需要大量 GPU 时间——CD-T 在 GPT-2 上秒级，但 1-3B 模型可能需要小时级（具体 scaling behavior 未知）。8B 模型的 hierarchical decomposition 可能需要 A100 80GB×4+ 数天。CirRAG 训练/调参（α, β, γ grid search）额外需要中等计算。总计估计需要 A100 80GB × 4-8 卡，2-4 周 dedicated compute。\n  - 数据需求: **中低**。所有数据集 (ConflictQA, NQ-Swap, MemoTrap, ConFiQA, CoFaithfulQA) 已公开可用。无需构建新数据集。JuICE 的 coherent conflict partition 需确认是否随代码公开。\n  - 人工介入: **中**。Circuit 分析和验证需要大量人工判断——识别 arbiter structures、解读 circuit topology、设计 rotational correction 的参数化方案。这不是一个全自动 pipeline。\n  - 训练需求: **低至中**。主要方法是 inference-time intervention，无需训练模型本身。但 activation probe (instance-adaptive routing) 需要小规模训练/calibration。\n  - 新 Benchmark: **否**。使用已有 benchmark。\n  - 预估周期: **4-6 个月**（紧凑）。Stage 1 (circuit discovery + scaling): 6-8 周；Stage 2 (validation): 3-4 周；Stage 3 (CirRAG intervention + ablation): 4-6 周；写作: 3-4 周。考虑到 circuit discovery scaling 的不确定性，建议预留 buffer，总计 5-7 个月更现实。对于 AAAI 2026 投稿（假设 2026 年 8 月 DDL），时间紧但可行。\n```\n\nSources:\n- [JuICE - Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)\n- [Basu et al. - On Mechanistic Circuits for Extractive QA (COLM 2025)](https://arxiv.org/abs/2502.08059)\n- [CoRect - Context-Aware Logit Contrast (arXiv 2026)](https://arxiv.org/abs/2602.08221)\n- [ParamMute - Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://openreview.net/forum?id=CyUq9D99vE)\n- [SpARE - SAE-Based Representation Engineering (NAACL 2025)](https://aclanthology.org/2025.naacl-long.264/)\n- [CD-T - Efficient Automated Circuit Discovery (ICLR 2025)](https://arxiv.org/abs/2407.00886)\n- [HAGD - Hierarchical Sparse Circuit Extraction (arXiv 2026)](https://arxiv.org/abs/2601.12879)\n- [Retrieval Heads are Dynamic (arXiv 2026)](https://arxiv.org/abs/2602.11162)\n- [How Transformers Reject Wrong Answers - Rotational Dynamics (arXiv 2026)](https://arxiv.org/abs/2603.13259)\n- [ReDeEP - Detecting Hallucination via Mechanistic Interpretability (ICLR 2025)](https://arxiv.org/abs/2410.11414)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# CirRAG: Circuit-Guided Multi-Point Repair of RAG Evidence Override\n\n## Core Problem\n\nWhen retrieved evidence conflicts with parametric memory, LLMs override context-derived answers through a specific circuit pathology. Existing interventions each target a single mechanism via heuristics: JuICE (ICML 2025) operates at head-level, CoRect (arXiv 2602.08221) patches FFN layers, SpARE (NAACL 2025) edits SAE features, ParamMute (NeurIPS 2025) suppresses FFNs, and IRCAN (NeurIPS 2024) reweights context-aware neurons. No existing work has traced the end-to-end causal circuit governing RAG evidence override or exploited circuit topology for coordinated multi-point intervention.\n\nBeyond RAG faithfulness, the conflict resolution circuit we seek to discover has broader implications: it may govern how LLMs arbitrate between competing signals in knowledge editing (why some edits get \"overwritten\") and instruction-following under prompt conflicts.\n\n**Research question**: What is the complete causal circuit governing RAG evidence override, and can circuit-topology-guided multi-point interventions outperform heuristic single-mechanism steering?\n\n## Contributions\n\n**C1 (Scientific Discovery)**: The first unified \"conflict resolution circuit\" mapping how context signals and parametric signals compete within the same forward pass. Unlike Basu et al. (arXiv 2502.08059), who extract two independent behavior-conditioned circuits (one Context-Faithfulness, one Memory-Faithfulness circuit via separate causal mediation analyses), we trace a single circuit capturing the competition process itself. We predict the existence of **arbiter structures**—edges and nodes that appear only when both signals are simultaneously active and that determine which signal wins. These arbiter structures are structurally invisible to behavior-conditioned analyses (which see only one behavioral mode at a time) and represent the irreducible contribution of unified circuit modeling.\n\n**C2 (Method)**: CirRAG, a coordinated multi-point intervention guided by circuit topology that simultaneously: (1) amplifies context-propagating edges, (2) dampens parametric FFN reassertion at circuit-pinpointed layers, and (3) applies rotational corrections at copy-suppression bottlenecks. The rotational correction component is the **first operationalization** of the converging rotational dynamics findings—three independent 2026 studies (arXiv 2602.04918, 2603.13259, 2602.11169) have discovered that override operates via angular displacement, but all remain at the analysis level; CirRAG is the first to convert this insight into an intervention, with circuit topology providing the precise locations for application.\n\n**C3 (Mechanistic Interpretability Contribution)**: Testing the \"circuit topology as invariant\" hypothesis. Retrieval heads change dynamically across generation timesteps (arXiv 2602.11162), and attention heads operate in superposition across memory and context functions (JuICE, ICML 2025). We hypothesize that circuit functional topology—connectivity patterns, bottleneck locations, information flow direction—is the stable computational structure underlying these surface-level dynamics. If confirmed, this provides the first unified mechanistic explanation for both phenomena: heads are interchangeable instantiations of circuit roles, and superposition arises because the same head can fill different circuit positions across contexts. This reframes the correct unit of mechanistic analysis from individual components to circuit topology.\n\n## Research Opportunity\n\nFive converging 2025–2026 advances create a unique opening:\n\n1. **CD-T (ICLR 2025)** enables seconds-scale circuit discovery with positional granularity. Defining context tokens as the \"relevant\" partition traces how retrieved evidence propagates and where it gets overridden. CD-T has been validated on GPT-2 scale; we propose a staged scaling strategy (see Approach).\n\n2. **CoRect's flip phenomenon** (arXiv 2602.08221): 56.4% of conflict cases show mid-layer correct-answer suppression—a ground-truth validation trajectory the discovered circuit must reproduce.\n\n3. **JuICE (ICML 2025)** proves attention heads operate in superposition, ruling out clean head-type separation and demanding circuit-level analysis.\n\n4. **Converging rotational dynamics evidence**: Simulated Adoption (arXiv 2602.04918) discovers angular displacement as the override mechanism; independently confirmed by \"How Transformers Reject Wrong Answers\" (arXiv 2603.13259, correct/incorrect paths diverge via rotation with active suppression, 1.5B–13B models) and \"Disentangling Direction and Magnitude\" (arXiv 2602.11169, angular perturbations cause 42.9× more damage than magnitude perturbations in Pythia). This triple convergence provides robust theoretical grounding for directional intervention.\n\n5. **Dynamic retrieval heads** (arXiv 2602.11162): Retrieval heads vary across timesteps with low Jaccard similarity to static identifications, challenging head-level methods and motivating circuit-level analysis where topology—not individual heads—is the invariant.\n\n## Research Landscape\n\n**Most directly comparable**: Basu et al. (arXiv 2502.08059) extract two separate behavior-conditioned circuits on Llama-3-8B (92% context override via attention upweighting). Core limitation: two independent snapshots cannot capture the competition dynamics—specifically, they cannot reveal arbiter structures that only emerge when both context and parametric signals are simultaneously active.\n\n**Single-mechanism SOTA** (each heuristic-targeted):\n- JuICE (ICML 2025 Spotlight): head-level dual-run, +SOTA across 11 datasets/6 models, but vulnerable to retrieval head dynamism\n- SpARE (NAACL 2025): SAE feature editing by mutual information, +10% EM\n- CoRect (arXiv 2602.08221): FFN patching by logit contrast, 72.95% avg QA accuracy on Qwen2.5-7B\n- ParamMute (NeurIPS 2025): FFN suppression, +6.17% faithfulness on LLaMA3-8B\n- IRCAN (NeurIPS 2024): context-aware neuron reweighting via integrated gradients\n- CAD (NAACL 2024): contrastive decoding amplifying context-vs-no-context difference\n- DoLa (ICLR 2024): early-vs-late layer logit contrast for factuality\n\nFACTUM (ECIR 2026) measures attention–FFN pathway alignment for hallucination detection. \"Promote, Suppress, Iterate\" (EMNLP 2025) and \"Where Knowledge Collides\" (arXiv 2601.09445) provide mechanistic analyses of knowledge retrieval dynamics. Certified Circuits (arXiv 2602.22968) offers stability guarantees for circuit discovery, reinforcing the importance of topology-level analysis.\n\n**Why not pipeline combination?** Stacking JuICE + CoRect + rotational insight without circuit discovery faces three problems: (a) **Interference**: amplifying attention heads while dampening FFN layers at heuristic positions may cancel each other, since which heads feed which FFNs in the conflict pathway is unknown without circuit analysis; (b) **Suboptimal loci**: circuit analysis identifies bottleneck nodes where small perturbations have maximal effect, rather than heuristic layer ranges; (c) **Instance-varying routing**: different conflict instances may activate different circuit sub-paths, requiring topology-informed intervention placement.\n\n## Proposed Approach\n\n### Circuit Sparsity Assumption\n\nThis work assumes the conflict resolution circuit is sufficiently sparse to guide precise intervention. We explicitly acknowledge the risk that the behavior may be highly distributed—HAGD (arXiv 2601.12879) reports 15–20% \"reconstruction dark matter\" in extracted circuits. We address this by: (1) reporting circuit faithfulness score (EM degradation upon circuit ablation), with a minimum 85% EM degradation threshold for the circuit to qualify as \"intervention-ready\"; (2) if faithfulness is below threshold, the contribution pivots to C1 (circuit discovery) and C3 (invariant hypothesis) with C2 (intervention) presented as limited by circuit distributedness. This defines the applicability boundary of circuit-guided intervention.\n\n### Stage 1: Circuit Discovery with Staged Scaling\n\nApply CD-T (ICLR 2025) to RAG conflict inputs (context tokens = relevant partition) to trace the full causal graph: retrieval heads → parametric FFN reassertion → copy suppression → output.\n\n**Scaling strategy**: (1) Core experiments on Llama-3.2-1B or Qwen2.5-1.5B—full circuit discovery, validation, and CirRAG evaluation at this scale constitute the primary contribution; (2) Hierarchical decomposition for 8B models—layer-level coarse circuit first, then head-level refinement within candidate layers; (3) If CD-T is computationally infeasible at 8B, fall back to HAGD (arXiv 2601.12879, validated on Llama-7B–70B) or HAP (arXiv 2510.03282, NeurIPS 2025). A circuit discovery method sensitivity ablation (CD-T vs fallback) on the 1–3B model quantifies the impact of discovery method on downstream intervention.\n\n**Target models**: One 1–3B model (core), Qwen3-8B and Llama-3.1-8B (scaling), with a third architecture (Mistral-7B or Gemma-2-9B) recommended if compute permits. All models are base (non-instruct) variants.\n\n### Stage 2: Circuit Validation\n\n1. **Flip reproduction**: In circuit mid-layers (L/3 to 2L/3), context-answer logit rank must exhibit V-shaped suppression-then-recovery in ≥40% of conflict cases (reference: CoRect reports 56.4% on Qwen2.5-7B; 40% is a conservative cross-architecture lower bound, to be calibrated via pilot on 1–3B model).\n2. **Causal necessity**: Ablating circuit subgraphs must produce ≥15% EM degradation on conflict datasets.\n3. **Arbiter structure identification**: Compare the unified conflict circuit against the union of separately extracted context-faithful and memory-faithful circuits (following Basu et al.'s methodology). Arbiter nodes/edges are those present in the unified circuit but absent from both individual circuits—their existence validates C1's core prediction.\n4. **Topology invariance test**: Across different generation timesteps where active retrieval heads shift (per arXiv 2602.11162), verify that circuit functional topology (connectivity, bottleneck locations) remains stable via graph-edit-distance or isomorphism metrics.\n\n### Stage 3: CirRAG Intervention Design\n\nCirRAG applies coordinated multi-point intervention informed by circuit topology:\n1. **Edge amplification**: strengthen context-propagating edges in the conflict resolution circuit\n2. **FFN dampening**: reduce parametric reassertion at circuit-pinpointed FFN layers\n3. **Rotational correction**: apply angular corrections at copy-suppression bottlenecks, grounded in converging rotational dynamics evidence (arXiv 2602.04918, 2603.13259, 2602.11169)\n\n**Intervention mode**: The circuit topology is discovered offline (one-time cost). At inference, a lightweight activation probe determines which circuit sub-path the current instance activates, selecting the corresponding intervention points. A fixed-vs-adaptive ablation quantifies the benefit of instance-adaptive placement over static intervention at the globally most-important nodes.\n\n## Experimental Design\n\n### Datasets\n- **Substitution conflicts**: ConflictQA, NQ-Swap, MemoTrap\n- **Multi-dimensional faithfulness**: ConFiQA (QA + multi-hop reasoning + multi-conflict)\n- **Realistic conflict**: CoFaithfulQA (6 open-domain QA sources, per ParamMute protocol)\n- **Coherent conflicts**: JuICE's coherent conflict partition\n\n### Baselines (layered by mechanism complexity)\n- **Layer 1 — Contrastive decoding**: CAD (NAACL 2024), DoLa (ICLR 2024)\n- **Layer 2 — Neuron/representation engineering**: IRCAN (NeurIPS 2024), SpARE (NAACL 2025)\n- **Layer 3 — Mechanistic intervention**: JuICE (ICML 2025), CoRect (arXiv 2602.08221), ParamMute (NeurIPS 2025), Basu et al. circuit steering (arXiv 2502.08059)\n- **Layer 4**: CirRAG (ours)\n\n### Metrics\n- **Primary**: Exact Match (EM) / Accuracy, F1\n- **Faithfulness**: Context Faithfulness Rate, ConR/MemR (per ParamMute protocol)\n- **Side-effect**: EM on non-conflict data (normal-performance degradation), perplexity\n- **Efficiency**: Inference latency (ms/query), memory overhead (MB), offline circuit discovery cost (GPU-hours). All measured on same GPU, batch size=1, BF16 precision\n- **Statistical rigor**: Mean ± std over N=3 random seeds; paired bootstrap test for significance of improvements over baselines\n\n### Ablation Studies\n- **Component isolation** (7 variants): Full CirRAG; remove each single component; remove each pair\n- **Intervention cardinality**: Intervene at top-k most important circuit nodes (k=1,3,5,10,all) → k-vs-EM curve demonstrating multi-point value and diminishing-returns boundary\n- **Fixed vs adaptive**: Static global intervention points vs instance-adaptive routing\n- **Intervention strength sensitivity**: Grid over amplification α, dampening β, rotation magnitude γ\n- **Circuit granularity**: Layer-level vs head-level vs position-level circuit\n- **Circuit discovery method**: CD-T vs HAGD vs attribution patching (on 1–3B model)\n\n### Compute Fairness\nReport offline (one-time) and online (per-query) costs separately. Present accuracy-vs-latency Pareto curve with all baselines under identical hardware configuration.\n\n## Key References\n\n- Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition [CD-T] (ICLR 2025)\n- Taming Knowledge Conflicts in Language Models [JuICE] (ICML 2025 Spotlight)\n- Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering [SpARE] (NAACL 2025)\n- ParamMute: Suppressing Knowledge-Critical FFNs for Faithful RAG (NeurIPS 2025)\n- Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries (EMNLP 2025)\n- CoRect: Context-Aware Logit Contrast for Hidden State Rectification (arXiv 2602.08221, 2026)\n- Simulated Adoption: Decoupling Magnitude and Direction in LLM In-Context Conflict Resolution (arXiv 2602.04918, 2026)\n- FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG (ECIR 2026)\n- On Mechanistic Circuits for Extractive Question-Answering [Basu et al.] (arXiv 2502.08059, 2025)\n- Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict (arXiv 2601.09445, 2026)\n- Retrieval Heads are Dynamic (arXiv 2602.11162, 2026)\n- How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing (arXiv 2603.13259, 2026)\n- Disentangling Direction and Magnitude in Transformer Representations (arXiv 2602.11169, 2026)\n- Hierarchical Sparse Circuit Extraction [HAGD] (arXiv 2601.12879, 2026)\n- Certified Circuits: Stability Guarantees for Mechanistic Circuits (arXiv 2602.22968, 2026)\n- Trusting Your Evidence: Hallucinate Less with Context-Aware Decoding [CAD] (NAACL 2024)\n- DoLa: Decoding by Contrasting Layers Improves Factuality (ICLR 2024)\n- IRCAN: Mitigating Knowledge Conflicts via Identifying and Reweighting Context-Aware Neurons (NeurIPS 2024)\n- Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework [HAP] (arXiv 2510.03282, NeurIPS 2025)"
}
````

---

### Runtime record

_source line 2 · 2026-05-30T07:30:36.100Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:30:36.100Z",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-30T07:30:36.113Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have comprehensive research coverage. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- JuICE / "Taming Knowledge Conflicts in Language Models" (ICML 2025 Spotlight): 当前 RAG knowledge conflict 领域的 SOTA。发现 attention head 的 superposition 现象（同时参与 memory 和 context），提出 dual-run 干预。在 11 个数据集/6 个模型上达到最优。CirRAG 正确地将此作为 head-level 方法的局限性依据，论证 circuit-level 分析的必要性。
- CoRect (arXiv 2602.08221, 2026): FFN 层级干预，通过 logit contrast 识别参数偏置层并修正 hidden states。关键发现：56.4% 的冲突案例存在 mid-layer 正确答案抑制（flip phenomenon）。CirRAG 将此作为电路验证的 ground-truth 轨迹——claim 成立。
- SpARE (NAACL 2025 Oral): 基于 SAE 的表示工程，+10% EM，+15% 超过 contrastive decoding。单一机制（feature editing）干预。
- ParamMute (NeurIPS 2025): FFN 抑制 + 知识偏好校准。引入 CoFaithfulQA benchmark。+6.17% faithfulness on LLaMA3-8B。
- Basu et al. (arXiv 2502.08059, COLM 2025): 最直接的竞争工作。提取两个独立的 behavior-conditioned circuits（Context-Faithfulness 和 Memory-Faithfulness），通过 attention upweighting 实现 92% context override。核心局限：两个独立快照无法捕捉竞争动态。CirRAG 对此的差异化论述——"arbiter structures"只在两种信号同时活跃时才出现——在逻辑上成立且具有原创性。
- CD-T (ICLR 2025): 秒级电路发现，97% ROC AUC。但仅在 GPT-2 规模上验证。这是 CirRAG 最大的可行性风险来源。
- HAGD (arXiv 2601.12879, 2026): 层次化稀疏电路提取，支持 Llama-7B–70B。O(n² log n) 复杂度。报告 15-20% "reconstruction dark matter"。CirRAG 正确引用此作为电路稀疏性风险的依据。
- Simulated Adoption (arXiv 2602.04918, 2026): 发现 override 机制是角度位移（orthogonal interference），而非幅度变化。在 Qwen-3-4B, Llama-3.1-8B, GLM-4-9B 上验证。
- "How Transformers Reject Wrong Answers" (arXiv 2603.13259, 2026): 独立确认 rotational dynamics，在 1.5B-13B 模型上发现 correct/incorrect paths 通过旋转分离。
- "Retrieval Heads are Dynamic" (arXiv 2602.11162, 2026): 发现检索头在不同生成时间步间动态变化，Jaccard 相似度低。直接挑战 head-level 方法的稳定性假设。
- IRCAN (NeurIPS 2024), CAD (NAACL 2024), DoLa (ICLR 2024): 更早期的单机制方法，CirRAG 正确地将其作为 baseline 层级。

- 调研总结: RAG knowledge conflict 的机制性理解正处于快速发展期，2025-2026 年密集涌现了大量从不同角度揭示冲突机制的工作（head superposition、FFN 抑制、rotational dynamics、检索头动态性）。然而，目前没有任何工作尝试将这些碎片化发现统一到一个端到端的因果电路中，更没有基于电路拓扑进行协调式多点干预。CirRAG 精准地占据了这个空白位置，且其 novelty claim 经调研验证成立。

【整体印象】:
作为审稿人，我的第一反应是**倾向 accept**，但带有保留意见。这是一篇对领域现状有极其深刻理解的 proposal，准确识别了多项 2025-2026 年最新发现之间的结构性联系，并提出了一个逻辑自洽、有清晰差异化的研究方向。"arbiter structures" 的预测是真正的原创概念，而非对已有工作的渐进组合。实验设计的完备性——分层 baseline、7 变体消融、intervention cardinality curve、fixed vs adaptive、discovery method sensitivity——表明作者对该领域的实验标准有成熟理解。主要保留意见在于：(1) 电路发现方法在 1-3B 甚至 8B 模型上的可行性尚未被充分验证（CD-T 仅在 GPT-2 上验证），(2) 系统复杂度较高（三重干预 + 自适应路由），实际能否协调工作存在执行风险。

【核心贡献】:
三层贡献结构清晰且层层递进：
1. **C1（科学发现）**: 首个统一的 "conflict resolution circuit"——不是分别提取两种行为模式的电路，而是追踪竞争过程本身。"Arbiter structures" 的预测是关键差异化：这些结构在行为条件分析中结构性不可见，只有在统一建模时才能发现。这是对 Basu et al. 工作的实质性推进，而非渐进改良。
2. **C2（方法）**: CirRAG 的协调式多点干预。"Why not pipeline combination" 一节出色地论证了为什么简单堆叠 JuICE + CoRect + rotational insight 不等价于 circuit-guided intervention（interference、suboptimal loci、instance-varying routing 三个论点均成立）。
3. **C3（机制性贡献）**: "Circuit topology as invariant" 假说——将正确的分析单元从个体组件提升到电路拓扑——如果得到验证，将统一解释 head superposition 和 retrieval head dynamism 两个看似独立的现象。

核心贡献对领域的价值：**高**。这不仅是又一个 RAG faithfulness 方法，而是试图建立该子领域的统一框架。即使 C2 的性能提升有限，C1 和 C3 本身也具有独立的科学价值。

【方法合理性】:
方法的逻辑链条（电路发现 → 验证 → 拓扑引导干预）是合理的。但存在以下需要审视的点：

1. **更简单的替代方案问题**: 一个自然的质疑是"为什么不直接在 Basu et al. 的两个电路基础上进行干预，而要重新发现统一电路？" Proposal 对此的回应（arbiter structures 不可见于行为条件分析）在逻辑上成立，但需要实验验证。如果最终 arbiter structures 贡献的增量很小，那么统一电路发现的额外成本就不值得。

2. **Rotational correction 的可操作性**: 三篇旋转动力学论文都停留在分析层面。将角度位移转化为干预手段的具体操作（rotation magnitude γ 的确定、旋转方向的选择）在 proposal 中未充分展开。这是方法中最模糊的部分。

3. **Instance-adaptive routing**: 用轻量级 activation probe 确定电路子路径是合理的想法，但训练该 probe 需要标注数据（哪些实例激活了哪条子路径），这增加了方法复杂度。

整体而言，方法架构合理，各组件有充分的文献支撑。风险主要在执行层面而非设计层面。

【5 维度打分】:

  1. 研究问题: 【强】 — 问题重要且时机恰当。RAG faithfulness 是当前 LLM 应用的核心挑战之一。五个独立研究方向（CD-T、head superposition、FFN suppression、rotational dynamics、retrieval head dynamism）的汇聚为统一框架提供了罕见的窗口期。研究问题的表述——"What is the complete causal circuit governing RAG evidence override, and can circuit-topology-guided multi-point interventions outperform heuristic single-mechanism steering?"——精确、可验证、有科学意义。此外，论文指出的更广泛影响（knowledge editing、instruction following under conflicts）增加了潜在研究价值。

  2. 方法与创新: 【强】 — 与 Basu et al. (COLM 2025) 的差异化清晰且实质性：统一电路 vs 两个独立电路快照，"arbiter structures" 的预测是原创概念。与 JuICE (ICML 2025) 的差异化同样清晰：circuit topology 作为分析单元 vs 个体 attention heads。Rotational correction 作为三项旋转动力学发现的首次操作化（arXiv 2602.04918, 2603.13259, 2602.11169）是有说服力的 first-mover contribution。"Why not pipeline combination" 一节有效地回应了"简单堆叠"的质疑。轻微扣分因素：rotational correction 的具体实现细节不够充分。

  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点之一。分层 baseline 设计（contrastive → neuron → mechanistic → CirRAG）完整覆盖了领域的方法谱系。Baseline 选择与当前 SOTA 完全对齐（JuICE、CoRect、ParamMute、SpARE、IRCAN、CAD、DoLa、Basu et al.）。消融设计极为全面：7 个组件变体、intervention cardinality curve（k=1,3,5,10,all）、fixed vs adaptive、strength sensitivity grid、circuit granularity、discovery method sensitivity。数据集覆盖了多种冲突类型（substitution、multi-dimensional、realistic、coherent）。Compute fairness（Pareto curve）和统计严谨性（seeds、bootstrap test）的承诺表明作者了解当前的实验标准。这套实验设计如果执行到位，足以支撑一篇顶会论文。

  4. 可行性: 【中】 — 这是 proposal 的主要弱点。(a) CD-T 仅在 GPT-2 规模上验证；1-3B 模型上的电路发现是否可行存在不确定性。Proposal 的 staged scaling strategy 和 HAGD/HAP fallback 是合理的风险缓解措施，但不消除风险。(b) 系统包含三种不同类型的干预（edge amplification、FFN dampening、rotational correction）+ instance-adaptive routing，每个组件都有超参数（α、β、γ），交互效应可能难以管理。(c) 85% EM degradation threshold 作为 "intervention-ready" 标准是合理的，但如果电路分布性太高未达标，论文的核心故事（C2）将被削弱。好的方面是：proposal 对这些风险的认知和应对策略是成熟的，有清晰的 fallback plan（contribution pivots to C1+C3）。计算资源需求在合理范围内——主要实验在 1-3B 模型上完成，8B 为扩展实验。

  5. 写作与呈现: 【强】 — Proposal 的组织结构清晰、逻辑链条紧密。从 problem → contributions → research opportunity → landscape → approach → experiments 的叙事流畅。文献引用精确且恰当，没有虚假引用或夸大他人工作的不足。"Research Opportunity" 一节将五个独立进展编织成统一叙事的能力突出。"Circuit Sparsity Assumption" 一节的诚实和科学严谨性是加分项。风险声明和 fallback plan 的透明度令人印象深刻。唯一的改进建议：rotational correction 的操作细节可以更具体。

【概率估计】: [30% - 47%] 中位 38%

【估计理由】:
向上因素：(1) Novelty claim 经调研验证完全成立——无人做过统一冲突解决电路+拓扑引导多点干预，(2) "arbiter structures" 是原创性强的科学预测，(3) 实验设计在当前 AAAI/NeurIPS/ICML 投稿中属于上乘水平——baseline 层次分明、消融穷尽、统计严谨，(4) 研究时机极佳（5+ 独立发现的汇聚），(5) 三层贡献中任意两层成功即可支撑一篇好论文。
向下因素：(1) 电路发现的可扩展性是实质性执行风险——CD-T 从 GPT-2 到 1-3B 的跨越并非 trivial，(2) 系统复杂度高——三重干预+自适应路由的工程和调参负担大，(3) "arbiter structures" 如果不存在或效果微弱，C1 的核心差异化将被削弱，(4) Rotational correction 的操作化细节不足可能被审稿人追问，(5) 仅使用 base models，与 RAG 实际应用场景（instruct models）存在 gap。
中位 38% 反映了：这是一篇方向正确、创新清晰、实验设计优秀的 proposal，但其核心承诺（统一电路发现、arbiter structures、coordinated intervention 的优越性）需要实验证据支撑，执行风险使其处于 borderline accept 区间。

【主要风险】:
1. **电路发现可扩展性失败**: 如果 CD-T 在 1-3B 模型上无法产出足够稀疏/忠实的电路（EM degradation < 85% 阈值），论文的核心方法贡献 (C2) 将退化为有限的 case study。虽然有 HAGD fallback，但切换发现方法可能影响下游干预的精度和一致性。
2. **Arbiter structures 不存在或贡献微弱**: 如果统一电路与 Basu et al. 两个独立电路的并集差异极小，那么 C1 的核心 novelty——"arbiter structures only visible in unified analysis"——将被根本性否定，论文退化为"用 circuit 信息指导 intervention placement"，与 Basu et al. 的 circuit steering 差异化减弱。

【实施评估】:
  - 计算资源: 中等。核心实验在 1-3B 模型上（单 GPU 可完成），8B 扩展实验需多卡或 A100。Circuit discovery 的一次性成本取决于方法（CD-T 秒级但可能需多次迭代，HAGD 更重）。Baseline 复现需额外计算。估计总需求：2-4× A100 GPU，数周时间。
  - 数据需求: 低。所有数据集均为已有公开 benchmark（ConflictQA、NQ-Swap、MemoTrap、ConFiQA、CoFaithfulQA），无需新数据收集。
  - 人工介入: 低-中。电路分析结果的解读和 arbiter structure 识别可能需要人工判断。Intervention 超参数（α、β、γ）的调节需要实验迭代。
  - 训练需求: 低。CirRAG 是 training-free 的推理时干预方法。Instance-adaptive routing 的 activation probe 需要少量训练，但数据来自电路分析的副产品。
  - 新 Benchmark: 否。使用已有 benchmark，无需构建新 benchmark。
  - 预估周期: 10-14 周。Stage 1（电路发现 + 调试）3-4 周，Stage 2（验证 + arbiter 分析）2-3 周，Stage 3（CirRAG 设计 + 调参 + 消融）3-4 周，写作 2-3 周。8B 扩展实验可能额外需要 2-3 周。
```

Sources:
- [JuICE - Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)
- [CoRect - Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221)
- [SpARE - SAE-Based Representation Engineering (NAACL 2025)](https://aclanthology.org/2025.naacl-long.264/)
- [ParamMute - Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://arxiv.org/html/2502.15543)
- [Basu et al. - Mechanistic Circuits for Extractive QA (COLM 2025)](https://arxiv.org/abs/2502.08059)
- [CD-T - Efficient Automated Circuit Discovery (ICLR 2025)](https://arxiv.org/abs/2407.00886)
- [HAGD - Hierarchical Sparse Circuit Extraction](https://arxiv.org/abs/2601.12879)
- [Simulated Adoption - Decoupling Magnitude and Direction](https://arxiv.org/abs/2602.04918)
- [How Transformers Reject Wrong Answers - Rotational Dynamics](https://arxiv.org/abs/2603.13259)
- [Retrieval Heads are Dynamic](https://arxiv.org/abs/2602.11162)
- [ReDeEP - Detecting Hallucination via Mechanistic Interpretability (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf)
- [Where Knowledge Collides - Mechanistic Study of Knowledge Conflict](https://arxiv.org/pdf/2601.09445)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile my comprehensive evaluation.

---

```
【阶段】: Triage

【领域调研】:

- [JuICE: Taming Knowledge Conflicts in Language Models](https://arxiv.org/abs/2503.10996) (ICML 2025 Spotlight): 发现注意力头在 context 和 memory 功能上存在 superposition，提出 dual-run test-time intervention。在 11 个数据集、6 个模型架构上达到 SOTA。是本 proposal 最直接的 head-level baseline，CirRAG 需要证明 circuit-level 分析能超越 head-level heuristic。

- [ParamMute: Suppressing Knowledge-Critical FFNs for Faithful RAG](https://arxiv.org/abs/2502.15543) (NeurIPS 2025): 识别中深层 FFN 对不忠实生成的不成比例激活，通过抑制这些 FFN 提高忠实度 +6.17%/+54.63%。是 FFN-level 单机制方法的代表。

- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221) (arXiv 2026): 通过 logit 对比定位 parametric bias 层并做 hidden state 修正。发现 56.4% 的冲突案例存在中层 correct-answer suppression（"flip phenomenon"）。提供了本 proposal 关键的 validation trajectory。

- [SpARE: Steering Knowledge Selection via SAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.264/) (NAACL 2025 Oral): 利用 SAE 特征编辑内部激活，+10% EM / +15% over contrastive decoding。SAE feature-level 方法代表。

- [CD-T: Efficient Automated Circuit Discovery using Contextual Decomposition](https://arxiv.org/abs/2407.00886) (ICLR 2025): 秒级 circuit 发现，支持 position-level 精度，97% ROC AUC。但验证规模主要在 GPT-2 级别，向 1-3B+ 扩展存在不确定性。

- [Basu et al.: On Mechanistic Circuits for Extractive QA](https://arxiv.org/abs/2502.08059) (COLM 2025): 提取两个独立 circuits（Context-Faithfulness / Memory-Faithfulness），通过 CMA 方法。核心局限性正如 proposal 所述——两个独立快照无法捕捉竞争动态。

- [Retrieval Heads are Dynamic](https://arxiv.org/abs/2602.11162) (arXiv 2026): 证明 retrieval heads 在不同生成步骤间动态变化，Jaccard similarity 低于静态识别，直接挑战 head-level 方法的稳定性假设。

- [How Transformers Reject Wrong Answers: Rotational Dynamics](https://arxiv.org/abs/2603.13259) (arXiv 2026): 证实 factual constraint processing 通过旋转（方向性位移）而非缩放实现，在 1.5B-13B 模型上验证。为本 proposal 的 rotational correction 组件提供理论基础。

- [HAGD: Hierarchical Sparse Circuit Extraction](https://arxiv.org/abs/2601.12879) (arXiv 2026): 将 circuit 发现复杂度降至 O(n² log n)，在 Llama-7B 到 70B 上验证。报告 15-20% "reconstruction dark matter"，对 proposal 的 circuit sparsity 假设构成挑战，也是重要的 fallback 方法。

- [IRCAN: Identifying and Reweighting Context-Aware Neurons](https://openreview.net/) (NeurIPS 2024): 通过 integrated gradients 识别 context-aware neurons 并 reweight。Neuron-level 方法代表。

- [Mechanistic Interpretability for LLM Alignment](https://arxiv.org/abs/2602.11180) (arXiv 2026): 综述 circuit discovery 应用于 alignment，涵盖 multi-token activation patching，表明领域正从分析走向干预，但 coordinated multi-point intervention 仍属前沿。

- 调研总结: RAG 知识冲突领域极其活跃（2024-2026 年有 7+ 篇顶会论文），但现有方法均为单机制启发式干预（head-level / FFN-level / feature-level），**尚无工作从端到端因果电路角度进行统一分析和协调多点干预**。Proposal 所识别的 gap 是真实且重要的。竞争激烈但差异化清晰。

【整体印象】:

作为审稿人，我的第一反应是 **lean accept with reservations**。这是一份异常成熟的 proposal：研究问题定义精准，文献综述几乎穷尽了 2024-2026 年的所有相关工作，方法论框架有清晰的理论动机，实验设计的完备程度（baselines 分层、ablation 7 变体、统计严谨性）远超大多数投稿。核心的 novelty claim——unified conflict resolution circuit + circuit-topology-guided multi-point intervention——经调研确认是真实的学术空白。

主要顾虑在于：(1) 项目极其宏大（circuit discovery + validation + intervention method + topology invariance hypothesis），单篇论文可能无法充分展开；(2) 关键技术依赖（CD-T scaling、circuit sparsity）存在实质性风险；(3) 若 arbiter structures 不存在或 circuit 过于分散，C1 的核心预测会落空。

但 proposal 对这些风险有诚实的承认和备选方案（circuit sparsity threshold、discovery method fallback、contribution pivot strategy），这显示出研究成熟度。

【核心贡献】:

三层贡献结构，递进合理：

1. **C1 (Scientific Discovery)**: 首个统一的 conflict resolution circuit，特别是 "arbiter structures" 的预测——仅在 context 和 parametric signals 同时活跃时才出现的节点/边。这是对 Basu et al. (COLM 2025) 两个独立 circuit 方法的直接超越，科学价值明确。

2. **C2 (Method)**: CirRAG 的三组件协调干预（edge amplification + FFN dampening + rotational correction）。Rotational correction 组件是将三篇独立的 rotational dynamics 分析工作（arXiv 2602.04918, 2603.13259, 2602.11169）首次转化为可操作的干预手段，这一点确实 novel。

3. **C3 (MI Contribution)**: "circuit topology as invariant" 假说——解释 retrieval heads 为何动态变化（头是 circuit role 的可互换实例化）以及为何 superposition 出现（同一头可在不同 context 下填充不同 circuit 位置）。若验证成功，这将为 mechanistic interpretability 领域提供重要的统一解释框架。

**领域价值评估**: C1 和 C3 若能验证，对 mechanistic interpretability 社区有较高价值；C2 若能在实验中超越 JuICE 和 ParamMute，对 RAG 应用社区有直接实用价值。三个贡献互相支撑但也互相依赖——这既是优势也是风险。

【方法合理性】:

**合理性**: 整体方法论框架是合理的。从 circuit discovery → validation → intervention 的三阶段流程逻辑清晰。利用 CD-T 的 contextual decomposition 将 context tokens 定义为 "relevant partition" 来追踪 evidence propagation 是自然的适配。Staged scaling strategy（1-3B core → 8B hierarchical decomposition → fallback methods）务实。

**替代方案分析**: Proposal 自己在 "Why not pipeline combination?" 部分很好地论证了为什么简单堆叠 JuICE + CoRect + rotational insight 不行——因为缺少 circuit topology 信息会导致 interference、suboptimal loci、和 instance-varying routing 问题。这是有说服力的论证。

**潜在问题**:
- **Rotational correction 的实际操作化**: 三篇 rotational dynamics 论文都是分析性工作；将 angular displacement findings 转化为具体的 "rotational correction at copy-suppression bottlenecks" 需要定义：(a) 旋转方向如何确定？(b) 旋转幅度如何校准？(c) 在高维空间中的旋转是否能 generalize across instances？Proposal 在这一关键细节上较为模糊。
- **Instance-adaptive routing**: "a lightweight activation probe determines which circuit sub-path the current instance activates" ——这个 probe 的训练数据从哪来？准确率预期如何？若 probe 不准确，adaptive 可能不如 fixed。Proposal 安排了 fixed-vs-adaptive ablation，但没有详述 probe 设计。
- **Arbiter structure 的可验证性**: 比较 unified circuit 与 two separate circuits 的 union，找到存在于 unified 但不存在于两个独立 circuit 中的节点。但这可能只是因为两种 circuit extraction 方法的噪声/不完整性，而非真正的 "arbiter structures"。需要更强的 causal evidence（如 ablate 这些 nodes 后 conflict resolution behavior 发生定性变化）。

【5 维度打分】:

1. **研究问题**: 【强】 
   — 问题重要且时机恰当。RAG faithfulness 是 LLM 应用的核心挑战，现有方法（JuICE ICML'25, ParamMute NeurIPS'25, SpARE NAACL'25, CoRect arXiv'26）均为单机制启发式干预，缺乏端到端因果理解。五项 2025-2026 年的独立进展（CD-T, rotational dynamics ×3, dynamic retrieval heads）恰好为 circuit-level 分析提供了工具和理论基础。"Unified conflict resolution circuit" 的研究问题是自然的下一步。

2. **方法与创新**: 【强】 
   — 核心 novelty 经调研确认成立：(a) 无现有工作追踪完整的 RAG evidence override 因果电路（Basu et al. COLM'25 最接近但只有两个独立电路）；(b) 无现有工作做 circuit-topology-guided multi-point intervention；(c) rotational correction 作为干预手段是首创（三篇 2026 分析论文均停留在发现层面）。方法的 "principled-ness"——由 circuit topology 指导干预位置而非 heuristic——是对现有方法的本质提升。扣分点：rotational correction 的操作化细节不足，instance-adaptive probe 设计模糊。

3. **实验设计**: 【强】 
   — 这是本 proposal 最突出的优势之一。Baselines 分 4 层（contrastive decoding → neuron/representation → mechanistic intervention → CirRAG），涵盖了 2024-2026 年几乎所有 SOTA 方法。Ablation 设计 7 变体 + intervention cardinality curve + fixed-vs-adaptive + strength sensitivity grid + circuit granularity + discovery method sensitivity，非常完备。评测指标覆盖 faithfulness、side-effect、efficiency 三个维度，并承诺 paired bootstrap test 和 N=3 seeds。Compute fairness（offline/online 分离 + Pareto 曲线）也是好做法。数据集选择（ConflictQA, NQ-Swap, MemoTrap, ConFiQA, CoFaithfulQA, JuICE coherent partition）覆盖了 substitution/multi-dimensional/realistic/coherent 四种冲突类型。

4. **可行性**: 【中】 
   — 最主要的风险源：(a) CD-T 向 1-3B 扩展缺乏先例验证，虽有 HAGD 作为 fallback，但不同 discovery 方法产生的 circuit 可能质量差异大，影响下游 intervention；(b) circuit sparsity 假设——HAGD 报告 15-20% dark matter，若冲突解决行为高度分布式，CirRAG intervention 效果会受限（proposal 设了 85% EM threshold，但这是否足够保守？）；(c) 整体工程复杂度很高（circuit discovery + validation + 3 组件 intervention + instance-adaptive probe），对团队执行力要求极高；(d) 1-3B 模型上的结果可能难以令审稿人信服（主流关注 7-8B+），但 proposal 对此有 scaling plan。Proposal 对风险的自我认知是优秀的（circuit sparsity acknowledgment, contribution pivot strategy），但风险本身是实质性的。

5. **写作与呈现**: 【强】 
   — Proposal 逻辑极其清晰：从 problem → gap → opportunity → contributions → approach → experiments，每一步都有充分论证。文献综述几乎无遗漏，且对每篇 related work 都精确描述了其 limitation 以及与本工作的关系。"Why not pipeline combination?" 段是优秀的 preemptive defense。Staged scaling strategy 和 circuit sparsity acknowledgment 显示出科研成熟度。唯一的担忧是内容量巨大——三个 contributions + 三阶段 approach + 六个 ablation studies，在 AAAI 8 页主体限制内可能需要非常精炼的写作。

【概率估计】: [33% - 48%] 中位 40%

【估计理由】:

**上界 (48%) 对应的情景**: Circuit discovery 在 1-3B scale 成功并产生清晰、稀疏的 conflict resolution circuit；arbiter structures 被发现并通过 causal ablation 验证；CirRAG 在主要 benchmark 上超越 JuICE 和 ParamMute 达到 statistically significant margins；topology invariance 假说得到初步验证。在这一情景下，论文具有三个互相支撑的强贡献（scientific discovery + method + MI insight），实验全面且结果亮眼，会是一篇非常有竞争力的投稿。

**下界 (33%) 对应的情景**: Circuit 发现面临 scaling 挑战，需要使用 fallback method；circuit 较为分散（85% 阈值勉强达到或未达到），CirRAG 在某些 benchmark 上未能显著超越 JuICE（JuICE 作为 ICML Spotlight 有很高的 bar）；arbiter structures 的证据不够决定性。但即便如此，circuit discovery 本身（C1）和 topology invariance 假说（C3）仍有科学贡献价值，实验设计的完备性也会获得认可。

**中位 40% 的判断依据**: (1) 研究问题和 novelty claim 经调研确认是真实且重要的；(2) 实验设计的完备程度在 proposal 阶段已远超平均水平；(3) 但核心技术依赖存在实质性不确定性（scaling, sparsity），且项目极其宏大，执行风险不可忽视；(4) 竞争领域——JuICE (ICML Spotlight), ParamMute (NeurIPS) 已经设了很高的 bar，新方法需要令人信服的实证优势。AAAI 接受率约 20-25%，40% 意味着这篇投稿显著高于平均质量，但仍存在相当的被拒风险。

【主要风险】:
1. **Circuit sparsity 假设不成立**: 如果 RAG evidence override 行为在 LLM 中高度分布式（HAGD 的 dark matter 证据指向此方向），circuit-guided intervention 将无法提供比 heuristic methods 有意义的改进。此时 C2 (CirRAG method) 的价值大幅缩水，论文需要靠 C1 和 C3 支撑，但纯分析性工作在应用导向的 reviewer 那里可能评价不高。
2. **JuICE baseline 难以超越**: JuICE 是 ICML 2025 Spotlight，在 11 个数据集、6 个模型架构上达到 SOTA，且方法简洁（test-time attention intervention, no training）。CirRAG 需要证明 circuit-guided approach 的额外复杂度（offline circuit discovery, instance-adaptive probe）换来了显著的性能提升。若改进幅度小或不一致，reviewer 会质疑 complexity-performance tradeoff。

【实施评估】:
  - 计算资源: **中高需求**。Circuit discovery（CD-T 或 HAGD）在 1-3B 模型上可能需要数十 GPU-hours，在 8B 模型上需求更大（HAGD 在 Llama-70B 上的成本未明确）。CirRAG intervention 评估涉及 8+ baselines × 6+ 数据集 × 3 seeds × 多个 ablation 变体。估计需 4-8× A100/H100 GPU 持续使用 4-8 周。
  - 数据需求: **低**。所有数据集（ConflictQA, NQ-Swap, MemoTrap, ConFiQA, CoFaithfulQA）均为已有公开数据集，无需新数据收集。JuICE 的 coherent conflict partition 也已公开。
  - 人工介入: **中**。Circuit interpretation 和 arbiter structure identification 可能需要 manual inspection 来验证 automated discovery 的结果。Rotational correction 的具体参数化可能需要实验迭代。
  - 训练需求: **低-中**。CirRAG 本身是 training-free intervention。Instance-adaptive probe 需要少量训练（但规模小）。Circuit discovery 是 inference-time forward pass，不涉及模型训练。
  - 新 Benchmark: **否**。使用已有 benchmarks，不需要构建新 benchmark。
  - 预估周期: **3-5 个月**。Stage 1 (circuit discovery + scaling): 4-6 周；Stage 2 (validation): 2-3 周；Stage 3 (CirRAG design + tuning): 3-4 周；实验 + ablation: 4-6 周；写作: 2-3 周。关键路径在 Stage 1 的 scaling 是否顺利。
```

Sources:
- [JuICE: Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)
- [ParamMute: Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://arxiv.org/abs/2502.15543)
- [CoRect: Context-Aware Logit Contrast (arXiv 2026)](https://arxiv.org/abs/2602.08221)
- [SpARE: SAE-Based Representation Engineering (NAACL 2025)](https://aclanthology.org/2025.naacl-long.264/)
- [CD-T: Efficient Automated Circuit Discovery (ICLR 2025)](https://arxiv.org/abs/2407.00886)
- [Basu et al.: Mechanistic Circuits for Extractive QA (COLM 2025)](https://arxiv.org/abs/2502.08059)
- [Retrieval Heads are Dynamic (arXiv 2026)](https://arxiv.org/abs/2602.11162)
- [How Transformers Reject Wrong Answers: Rotational Dynamics (arXiv 2026)](https://arxiv.org/abs/2603.13259)
- [HAGD: Hierarchical Sparse Circuit Extraction (arXiv 2026)](https://arxiv.org/abs/2601.12879)
- [IRCAN: Identifying and Reweighting Context-Aware Neurons (NeurIPS 2024)](https://openreview.net/)
- [Mechanistic Interpretability for LLM Alignment (arXiv 2026)](https://arxiv.org/abs/2602.11180)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have comprehensive context on the field. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- JuICE / "Taming Knowledge Conflicts in Language Models" (ICML 2025 Spotlight): 当前 SOTA，跨 11 数据集/6 模型架构。发现 attention head 存在 context-memory superposition，采用 dual-run 方式干预。是 CirRAG 最强的 baseline——CirRAG 必须在这个基础上展示统计显著的增益才有说服力。
- Basu et al. "On Mechanistic Circuits for Extractive QA" (COLM 2025, arXiv 2502.08059): 提取 context-faithfulness 和 memory-faithfulness 两条独立 circuit，并用 ATTNATTRIB 实现数据归因和 steering。CirRAG 提出的"unified conflict circuit"和"arbiter structures"直接针对该工作的 two-circuit 局限。
- CoRect (arXiv 2602.08221, 2026): 通过 logit contrast 定位 FFN parametric suppression 层并在推理时修正 hidden state。报告了 56.4% 的 mid-layer flip phenomenon——CirRAG 将其作为 circuit 验证的 ground truth。
- ParamMute (NeurIPS 2025): 抑制 knowledge-critical FFN，在 LLaMA3-8B 上提升 6.17% faithfulness。引入了 CoFaithfulQA benchmark。
- SpARE (NAACL 2025 Oral): 基于 SAE 的 representation engineering，+10% EM，+15% 超越 contrastive decoding 方法。
- CD-T (ICLR 2025): 秒级 circuit discovery，97% ROC AUC，但**仅在 GPT-2 级别验证过**。这是 CirRAG 面临的关键 scaling 瓶颈。
- HAGD (arXiv 2601.12879, 2026): 支持 Llama-7B 到 70B 的 hierarchical circuit extraction，但有 15-20% "reconstruction dark matter"且**不建模 attention circuit**——而 CirRAG 核心依赖 attention 分析。
- "Retrieval Heads are Dynamic" (arXiv 2602.11162, 2026): 发现 retrieval heads 跨 timestep 动态变化（Jaccard 0.18-0.46），挑战了 head-level 方法的稳定性假设，为 CirRAG 的 topology-level 分析提供动机。
- "How Transformers Reject Wrong Answers" (arXiv 2603.13259, 2026): 确认 correct/incorrect paths 通过 rotation 而非 rescaling 分离，1.6B 参数出现 phase transition。
- ReDeEP (ICLR 2025): 首个将 mechanistic interpretability 用于 RAG hallucination 检测的工作，但聚焦检测而非干预。

- 调研总结: RAG faithfulness 的机制干预已进入"百花齐放"阶段——2024-2026 涌现了大量各攻一个机制的方法（head/FFN/SAE/decoding），但尚无工作尝试端到端的 causal circuit 发现和基于 topology 的 coordinated multi-point intervention。CirRAG 瞄准的缝隙真实存在，但竞争极为激烈（JuICE ICML Spotlight 是硬标杆），且 circuit discovery 的 scaling 是领域级难题。

【整体印象】:
作为审稿人，我的第一反应是：这是一份 research maturity 极高的 proposal。对领域的理解深度、对 related work 的精准定位、对 contribution 的差异化表述、以及实验设计的完备性，都明显高于平均水平。

核心叙事——"五条独立研究线索在 2025-2026 汇聚，创造了一个 unified circuit 分析的窗口"——构建得很有说服力。三个贡献 (C1 科学发现, C2 方法, C3 机制可解释性假设) 互相支撑，形成一个有内在一致性的研究议程。

但我会倾向 **weak accept / borderline**，原因是：(1) scope 极为宏大，单篇论文能否同时交付 circuit discovery + multi-point intervention + topology invariance hypothesis 的充分实证？(2) 核心方法依赖 CD-T 的 scaling，而 CD-T 尚未在 >GPT-2 规模验证，fallback 方案 (HAGD) 不建模 attention——这不是小风险；(3) 竞争对手 JuICE 已经在 11 数据集 6 模型上 SOTA，CirRAG 的增量收益可能有限。

【核心贡献】:
1. **C1 (Unified Conflict Resolution Circuit)**: 首次追踪 RAG evidence override 的完整 causal circuit，并预测 "arbiter structures" 的存在——这是 Basu et al. 的 two-circuit 方法论上无法发现的结构。如果验证成功，这是一个真正的科学发现。
2. **C2 (CirRAG Method)**: 基于 circuit topology 的 coordinated multi-point intervention，将 rotational dynamics 的分析洞察首次转化为干预手段。
3. **C3 (Topology Invariance Hypothesis)**: 提出 circuit functional topology 是底层计算不变量，为 retrieval head dynamism 和 superposition 提供统一解释。

贡献价值：如果 C1 的 arbiter structures 被验证，这对 mechanistic interpretability 领域有显著影响。C2 的实用价值取决于是否能显著超越 JuICE。C3 是一个有深度的假设，但验证难度高。总体而言，这是一个"high risk, high reward"的研究议程。

【方法合理性】:
方法的总体逻辑合理：先发现 circuit → 用 topology 指导干预位点 → 多点协调干预。这比 heuristic single-mechanism 方法在理论上更有吸引力。

**关键质疑**:
1. **更简单的替代方案**: 为什么不直接组合 JuICE (head) + CoRect (FFN) + SpARE (SAE feature) 的干预，用简单的 grid search 找最优组合？proposal 的 "Why not pipeline combination?" 一节给出了三个论点 (interference, suboptimal loci, instance-varying routing)，但这些论点是假设性的——在没有实验数据的情况下，一个 well-tuned pipeline combination 可能就够了。建议在实验中加入这个 baseline。
2. **Rotational correction 的具体操作**: proposal 提到"apply angular corrections at copy-suppression bottlenecks"，但具体参数化方式不够明确。rotation 在高维空间中有很多可能的操作方式（Givens rotation? projection? subspace alignment?），这需要更详细的说明。
3. **Instance-adaptive routing 的 overhead**: 一个 lightweight activation probe 能否在不引入显著延迟的情况下准确判断 circuit sub-path？这需要仔细的 latency 分析。

【5 维度打分】:

  1. 研究问题: 【强】 — RAG evidence override 是 LLM 部署的核心痛点之一。现有方法各攻一点、缺乏 unified understanding 的问题被清晰识别。五条研究线索的汇聚论述有说服力。研究问题既有实用价值 (improving RAG faithfulness) 又有科学价值 (understanding conflict resolution mechanisms)。

  2. 方法与创新: 【中偏强】 — 创新点真实存在：(a) unified circuit 相对于 Basu et al. 的 two-circuit 是一个有意义的推进；(b) rotational correction 作为首个 intervention operationalization 有独特性；(c) multi-point coordinated intervention 的理念合理。但 novelty 的实质性取决于 arbiter structures 是否真的存在、是否与 Basu union of circuits 有显著差异。方法的核心依赖 (CD-T scaling) 引入了不确定性。相比 JuICE (ICML 2025 Spotlight) 的简洁优雅（just run twice），CirRAG 的复杂度显著更高，能否带来 proportional 的性能增益是关键问题。

  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点之一。四类数据集覆盖 substitution/multi-dimensional/realistic/coherent conflicts。Baselines 按机制复杂度分四层，涵盖了所有重要工作。Ablation 设计极为完备（7 component variants, intervention cardinality curve, fixed vs adaptive, strength sensitivity, circuit granularity, discovery method sensitivity）。Compute fairness 的 accuracy-vs-latency Pareto curve 和 offline/online 成本分离也是加分项。统计严格性 (3 seeds + paired bootstrap) 达标。**唯一缺失**: 缺少一个 "naive pipeline combination" baseline（JuICE + CoRect + rotational insight 的简单组合）来直接验证 circuit-guided 定位的增量价值。

  4. 可行性: 【中】 — 这是最大的风险维度。(a) CD-T 仅在 GPT-2 验证过，proposal 的核心实验需要 1-3B 甚至 8B 模型——scaling gap 显著。fallback 方案 HAGD 不建模 attention circuit，对本工作是硬伤。(b) Circuit sparsity assumption 如果不成立，C2 的价值大幅缩水。proposal 的 85% EM degradation threshold 和 "pivot to C1+C3" fallback 是成熟的风险管理，但这意味着 paper 的核心卖点可能无法兑现。(c) 三个 contributions 的 scope 对单篇论文来说过于宏大——circuit discovery、intervention method、topology invariance hypothesis 每一个都足以独立成文。(d) 预估周期可能偏紧。

  5. 写作与呈现: 【强】 — Proposal 的叙事结构清晰、逻辑严密。"Research Opportunity" 节的五线汇聚论述特别出色。对 related work 的定位精准，每个 contribution 相对于 prior work 的差异化都说得很清楚。风险的坦诚披露和 fallback plan 增加了可信度。唯一可改进的是 rotational correction 的技术细节需要更具体。

【概率估计】: [30% - 44%] 中位 37%

【估计理由】:
优势面：研究问题重要且 timely (强)、文献定位极为精准、实验设计在 proposal 阶段已接近顶会论文水平、三个 contribution 有内在一致性且各自有 novelty claim。这些特质使其显著高于平均投稿质量。

劣势面：(1) **执行风险高**——CD-T scaling 是 uncharted territory，如果 circuit discovery 在 1-3B 模型上不 work 或过于 distributed，整个方法链条断裂；(2) **强竞争**——JuICE 已在 ICML 2025 以 Spotlight 发表且方法更简洁，CirRAG 需要展示明显且一致的增益；(3) **scope 过大**——三个 contribution 可能导致每个都不够深入，reviewer 可能质疑"是 circuit discovery paper 还是 intervention paper 还是 interpretability paper"；(4) **circuit sparsity assumption 未验证**——如果 conflict resolution 是 distributed computation，核心方法不成立。

中位 37% 反映：这是一篇 direction 正确、craftsmanship 出色、但执行风险显著的投稿。如果实验结果支撑叙事（arbiter structures 被发现、CirRAG 统计显著超越 JuICE），可以冲击 strong accept (概率上界 44%）。如果 circuit discovery scaling 遇阻或性能增益 marginal，可能落入 borderline reject (概率下界 30%)。

【主要风险】:
1. **Circuit Discovery Scaling 瓶颈**: CD-T 仅在 GPT-2 (~117M) 验证过，proposal 需要在 1-3B 甚至 8B 模型上工作。Fallback 方案 HAGD 不建模 attention circuit——而 attention 是 RAG conflict resolution 的核心组件（JuICE 已证明）。如果两者都无法在目标规模上提供 fine-grained 且 faithful 的 circuit，整个方法基础崩塌。
2. **增量收益 vs 方法复杂度**: JuICE 方法极其简洁 ("just run twice") 已达 SOTA，CirRAG 引入了 circuit discovery (offline GPU-hours) + activation probe (online latency) + 3-component coordinated intervention 的复杂 pipeline。如果最终性能增益仅在 1-3% EM 的统计噪声范围内，reviewer 会质疑 complexity-benefit tradeoff。

【实施评估】:
  - 计算资源: **高**。Circuit discovery 阶段需要大量 GPU 时间——CD-T 在 GPT-2 上秒级，但 1-3B 模型可能需要小时级（具体 scaling behavior 未知）。8B 模型的 hierarchical decomposition 可能需要 A100 80GB×4+ 数天。CirRAG 训练/调参（α, β, γ grid search）额外需要中等计算。总计估计需要 A100 80GB × 4-8 卡，2-4 周 dedicated compute。
  - 数据需求: **中低**。所有数据集 (ConflictQA, NQ-Swap, MemoTrap, ConFiQA, CoFaithfulQA) 已公开可用。无需构建新数据集。JuICE 的 coherent conflict partition 需确认是否随代码公开。
  - 人工介入: **中**。Circuit 分析和验证需要大量人工判断——识别 arbiter structures、解读 circuit topology、设计 rotational correction 的参数化方案。这不是一个全自动 pipeline。
  - 训练需求: **低至中**。主要方法是 inference-time intervention，无需训练模型本身。但 activation probe (instance-adaptive routing) 需要小规模训练/calibration。
  - 新 Benchmark: **否**。使用已有 benchmark。
  - 预估周期: **4-6 个月**（紧凑）。Stage 1 (circuit discovery + scaling): 6-8 周；Stage 2 (validation): 3-4 周；Stage 3 (CirRAG intervention + ablation): 4-6 周；写作: 3-4 周。考虑到 circuit discovery scaling 的不确定性，建议预留 buffer，总计 5-7 个月更现实。对于 AAAI 2026 投稿（假设 2026 年 8 月 DDL），时间紧但可行。
```

Sources:
- [JuICE - Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)
- [Basu et al. - On Mechanistic Circuits for Extractive QA (COLM 2025)](https://arxiv.org/abs/2502.08059)
- [CoRect - Context-Aware Logit Contrast (arXiv 2026)](https://arxiv.org/abs/2602.08221)
- [ParamMute - Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://openreview.net/forum?id=CyUq9D99vE)
- [SpARE - SAE-Based Representation Engineering (NAACL 2025)](https://aclanthology.org/2025.naacl-long.264/)
- [CD-T - Efficient Automated Circuit Discovery (ICLR 2025)](https://arxiv.org/abs/2407.00886)
- [HAGD - Hierarchical Sparse Circuit Extraction (arXiv 2026)](https://arxiv.org/abs/2601.12879)
- [Retrieval Heads are Dynamic (arXiv 2026)](https://arxiv.org/abs/2602.11162)
- [How Transformers Reject Wrong Answers - Rotational Dynamics (arXiv 2026)](https://arxiv.org/abs/2603.13259)
- [ReDeEP - Detecting Hallucination via Mechanistic Interpretability (ICLR 2025)](https://arxiv.org/abs/2410.11414)


【原始 proposal（允许参考但不是主要依据）】:
# CirRAG: Circuit-Guided Multi-Point Repair of RAG Evidence Override

## Core Problem

When retrieved evidence conflicts with parametric memory, LLMs override context-derived answers through a specific circuit pathology. Existing interventions each target a single mechanism via heuristics: JuICE (ICML 2025) operates at head-level, CoRect (arXiv 2602.08221) patches FFN layers, SpARE (NAACL 2025) edits SAE features, ParamMute (NeurIPS 2025) suppresses FFNs, and IRCAN (NeurIPS 2024) reweights context-aware neurons. No existing work has traced the end-to-end causal circuit governing RAG evidence override or exploited circuit topology for coordinated multi-point intervention.

Beyond RAG faithfulness, the conflict resolution circuit we seek to discover has broader implications: it may govern how LLMs arbitrate between competing signals in knowledge editing (why some edits get "overwritten") and instruction-following under prompt conflicts.

**Research question**: What is the complete causal circuit governing RAG evidence override, and can circuit-topology-guided multi-point interventions outperform heuristic single-mechanism steering?

## Contributions

**C1 (Scientific Discovery)**: The first unified "conflict resolution circuit" mapping how context signals and parametric signals compete within the same forward pass. Unlike Basu et al. (arXiv 2502.08059), who extract two independent behavior-conditioned circuits (one Context-Faithfulness, one Memory-Faithfulness circuit via separate causal mediation analyses), we trace a single circuit capturing the competition process itself. We predict the existence of **arbiter structures**—edges and nodes that appear only when both signals are simultaneously active and that determine which signal wins. These arbiter structures are structurally invisible to behavior-conditioned analyses (which see only one behavioral mode at a time) and represent the irreducible contribution of unified circuit modeling.

**C2 (Method)**: CirRAG, a coordinated multi-point intervention guided by circuit topology that simultaneously: (1) amplifies context-propagating edges, (2) dampens parametric FFN reassertion at circuit-pinpointed layers, and (3) applies rotational corrections at copy-suppression bottlenecks. The rotational correction component is the **first operationalization** of the converging rotational dynamics findings—three independent 2026 studies (arXiv 2602.04918, 2603.13259, 2602.11169) have discovered that override operates via angular displacement, but all remain at the analysis level; CirRAG is the first to convert this insight into an intervention, with circuit topology providing the precise locations for application.

**C3 (Mechanistic Interpretability Contribution)**: Testing the "circuit topology as invariant" hypothesis. Retrieval heads change dynamically across generation timesteps (arXiv 2602.11162), and attention heads operate in superposition across memory and context functions (JuICE, ICML 2025). We hypothesize that circuit functional topology—connectivity patterns, bottleneck locations, information flow direction—is the stable computational structure underlying these surface-level dynamics. If confirmed, this provides the first unified mechanistic explanation for both phenomena: heads are interchangeable instantiations of circuit roles, and superposition arises because the same head can fill different circuit positions across contexts. This reframes the correct unit of mechanistic analysis from individual components to circuit topology.

## Research Opportunity

Five converging 2025–2026 advances create a unique opening:

1. **CD-T (ICLR 2025)** enables seconds-scale circuit discovery with positional granularity. Defining context tokens as the "relevant" partition traces how retrieved evidence propagates and where it gets overridden. CD-T has been validated on GPT-2 scale; we propose a staged scaling strategy (see Approach).

2. **CoRect's flip phenomenon** (arXiv 2602.08221): 56.4% of conflict cases show mid-layer correct-answer suppression—a ground-truth validation trajectory the discovered circuit must reproduce.

3. **JuICE (ICML 2025)** proves attention heads operate in superposition, ruling out clean head-type separation and demanding circuit-level analysis.

4. **Converging rotational dynamics evidence**: Simulated Adoption (arXiv 2602.04918) discovers angular displacement as the override mechanism; independently confirmed by "How Transformers Reject Wrong Answers" (arXiv 2603.13259, correct/incorrect paths diverge via rotation with active suppression, 1.5B–13B models) and "Disentangling Direction and Magnitude" (arXiv 2602.11169, angular perturbations cause 42.9× more damage than magnitude perturbations in Pythia). This triple convergence provides robust theoretical grounding for directional intervention.

5. **Dynamic retrieval heads** (arXiv 2602.11162): Retrieval heads vary across timesteps with low Jaccard similarity to static identifications, challenging head-level methods and motivating circuit-level analysis where topology—not individual heads—is the invariant.

## Research Landscape

**Most directly comparable**: Basu et al. (arXiv 2502.08059) extract two separate behavior-conditioned circuits on Llama-3-8B (92% context override via attention upweighting). Core limitation: two independent snapshots cannot capture the competition dynamics—specifically, they cannot reveal arbiter structures that only emerge when both context and parametric signals are simultaneously active.

**Single-mechanism SOTA** (each heuristic-targeted):
- JuICE (ICML 2025 Spotlight): head-level dual-run, +SOTA across 11 datasets/6 models, but vulnerable to retrieval head dynamism
- SpARE (NAACL 2025): SAE feature editing by mutual information, +10% EM
- CoRect (arXiv 2602.08221): FFN patching by logit contrast, 72.95% avg QA accuracy on Qwen2.5-7B
- ParamMute (NeurIPS 2025): FFN suppression, +6.17% faithfulness on LLaMA3-8B
- IRCAN (NeurIPS 2024): context-aware neuron reweighting via integrated gradients
- CAD (NAACL 2024): contrastive decoding amplifying context-vs-no-context difference
- DoLa (ICLR 2024): early-vs-late layer logit contrast for factuality

FACTUM (ECIR 2026) measures attention–FFN pathway alignment for hallucination detection. "Promote, Suppress, Iterate" (EMNLP 2025) and "Where Knowledge Collides" (arXiv 2601.09445) provide mechanistic analyses of knowledge retrieval dynamics. Certified Circuits (arXiv 2602.22968) offers stability guarantees for circuit discovery, reinforcing the importance of topology-level analysis.

**Why not pipeline combination?** Stacking JuICE + CoRect + rotational insight without circuit discovery faces three problems: (a) **Interference**: amplifying attention heads while dampening FFN layers at heuristic positions may cancel each other, since which heads feed which FFNs in the conflict pathway is unknown without circuit analysis; (b) **Suboptimal loci**: circuit analysis identifies bottleneck nodes where small perturbations have maximal effect, rather than heuristic layer ranges; (c) **Instance-varying routing**: different conflict instances may activate different circuit sub-paths, requiring topology-informed intervention placement.

## Proposed Approach

### Circuit Sparsity Assumption

This work assumes the conflict resolution circuit is sufficiently sparse to guide precise intervention. We explicitly acknowledge the risk that the behavior may be highly distributed—HAGD (arXiv 2601.12879) reports 15–20% "reconstruction dark matter" in extracted circuits. We address this by: (1) reporting circuit faithfulness score (EM degradation upon circuit ablation), with a minimum 85% EM degradation threshold for the circuit to qualify as "intervention-ready"; (2) if faithfulness is below threshold, the contribution pivots to C1 (circuit discovery) and C3 (invariant hypothesis) with C2 (intervention) presented as limited by circuit distributedness. This defines the applicability boundary of circuit-guided intervention.

### Stage 1: Circuit Discovery with Staged Scaling

Apply CD-T (ICLR 2025) to RAG conflict inputs (context tokens = relevant partition) to trace the full causal graph: retrieval heads → parametric FFN reassertion → copy suppression → output.

**Scaling strategy**: (1) Core experiments on Llama-3.2-1B or Qwen2.5-1.5B—full circuit discovery, validation, and CirRAG evaluation at this scale constitute the primary contribution; (2) Hierarchical decomposition for 8B models—layer-level coarse circuit first, then head-level refinement within candidate layers; (3) If CD-T is computationally infeasible at 8B, fall back to HAGD (arXiv 2601.12879, validated on Llama-7B–70B) or HAP (arXiv 2510.03282, NeurIPS 2025). A circuit discovery method sensitivity ablation (CD-T vs fallback) on the 1–3B model quantifies the impact of discovery method on downstream intervention.

**Target models**: One 1–3B model (core), Qwen3-8B and Llama-3.1-8B (scaling), with a third architecture (Mistral-7B or Gemma-2-9B) recommended if compute permits. All models are base (non-instruct) variants.

### Stage 2: Circuit Validation

1. **Flip reproduction**: In circuit mid-layers (L/3 to 2L/3), context-answer logit rank must exhibit V-shaped suppression-then-recovery in ≥40% of conflict cases (reference: CoRect reports 56.4% on Qwen2.5-7B; 40% is a conservative cross-architecture lower bound, to be calibrated via pilot on 1–3B model).
2. **Causal necessity**: Ablating circuit subgraphs must produce ≥15% EM degradation on conflict datasets.
3. **Arbiter structure identification**: Compare the unified conflict circuit against the union of separately extracted context-faithful and memory-faithful circuits (following Basu et al.'s methodology). Arbiter nodes/edges are those present in the unified circuit but absent from both individual circuits—their existence validates C1's core prediction.
4. **Topology invariance test**: Across different generation timesteps where active retrieval heads shift (per arXiv 2602.11162), verify that circuit functional topology (connectivity, bottleneck locations) remains stable via graph-edit-distance or isomorphism metrics.

### Stage 3: CirRAG Intervention Design

CirRAG applies coordinated multi-point intervention informed by circuit topology:
1. **Edge amplification**: strengthen context-propagating edges in the conflict resolution circuit
2. **FFN dampening**: reduce parametric reassertion at circuit-pinpointed FFN layers
3. **Rotational correction**: apply angular corrections at copy-suppression bottlenecks, grounded in converging rotational dynamics evidence (arXiv 2602.04918, 2603.13259, 2602.11169)

**Intervention mode**: The circuit topology is discovered offline (one-time cost). At inference, a lightweight activation probe determines which circuit sub-path the current instance activates, selecting the corresponding intervention points. A fixed-vs-adaptive ablation quantifies the benefit of instance-adaptive placement over static intervention at the globally most-important nodes.

## Experimental Design

### Datasets
- **Substitution conflicts**: ConflictQA, NQ-Swap, MemoTrap
- **Multi-dimensional faithfulness**: ConFiQA (QA + multi-hop reasoning + multi-conflict)
- **Realistic conflict**: CoFaithfulQA (6 open-domain QA sources, per ParamMute protocol)
- **Coherent conflicts**: JuICE's coherent conflict partition

### Baselines (layered by mechanism complexity)
- **Layer 1 — Contrastive decoding**: CAD (NAACL 2024), DoLa (ICLR 2024)
- **Layer 2 — Neuron/representation engineering**: IRCAN (NeurIPS 2024), SpARE (NAACL 2025)
- **Layer 3 — Mechanistic intervention**: JuICE (ICML 2025), CoRect (arXiv 2602.08221), ParamMute (NeurIPS 2025), Basu et al. circuit steering (arXiv 2502.08059)
- **Layer 4**: CirRAG (ours)

### Metrics
- **Primary**: Exact Match (EM) / Accuracy, F1
- **Faithfulness**: Context Faithfulness Rate, ConR/MemR (per ParamMute protocol)
- **Side-effect**: EM on non-conflict data (normal-performance degradation), perplexity
- **Efficiency**: Inference latency (ms/query), memory overhead (MB), offline circuit discovery cost (GPU-hours). All measured on same GPU, batch size=1, BF16 precision
- **Statistical rigor**: Mean ± std over N=3 random seeds; paired bootstrap test for significance of improvements over baselines

### Ablation Studies
- **Component isolation** (7 variants): Full CirRAG; remove each single component; remove each pair
- **Intervention cardinality**: Intervene at top-k most important circuit nodes (k=1,3,5,10,all) → k-vs-EM curve demonstrating multi-point value and diminishing-returns boundary
- **Fixed vs adaptive**: Static global intervention points vs instance-adaptive routing
- **Intervention strength sensitivity**: Grid over amplification α, dampening β, rotation magnitude γ
- **Circuit granularity**: Layer-level vs head-level vs position-level circuit
- **Circuit discovery method**: CD-T vs HAGD vs attribution patching (on 1–3B model)

### Compute Fairness
Report offline (one-time) and online (per-query) costs separately. Present accuracy-vs-latency Pareto curve with all baselines under identical hardware configuration.

## Key References

- Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition [CD-T] (ICLR 2025)
- Taming Knowledge Conflicts in Language Models [JuICE] (ICML 2025 Spotlight)
- Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering [SpARE] (NAACL 2025)
- ParamMute: Suppressing Knowledge-Critical FFNs for Faithful RAG (NeurIPS 2025)
- Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries (EMNLP 2025)
- CoRect: Context-Aware Logit Contrast for Hidden State Rectification (arXiv 2602.08221, 2026)
- Simulated Adoption: Decoupling Magnitude and Direction in LLM In-Context Conflict Resolution (arXiv 2602.04918, 2026)
- FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG (ECIR 2026)
- On Mechanistic Circuits for Extractive Question-Answering [Basu et al.] (arXiv 2502.08059, 2025)
- Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict (arXiv 2601.09445, 2026)
- Retrieval Heads are Dynamic (arXiv 2602.11162, 2026)
- How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing (arXiv 2603.13259, 2026)
- Disentangling Direction and Magnitude in Transformer Representations (arXiv 2602.11169, 2026)
- Hierarchical Sparse Circuit Extraction [HAGD] (arXiv 2601.12879, 2026)
- Certified Circuits: Stability Guarantees for Mechanistic Circuits (arXiv 2602.22968, 2026)
- Trusting Your Evidence: Hallucinate Less with Context-Aware Decoding [CAD] (NAACL 2024)
- DoLa: Decoding by Contrasting Layers Improves Factuality (ICLR 2024)
- IRCAN: Mitigating Knowledge Conflicts via Identifying and Reweighting Context-Aware Neurons (NeurIPS 2024)
- Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework [HAP] (arXiv 2510.03282, NeurIPS 2025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9f958496-6fda-48dd-bec7-37edada79dfc",
  "type": "user",
  "uuid": "67692e93-0506-44bd-8d64-d50a2546edab",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:30:36.111Z_

```json
{
  "parentUuid": "67692e93-0506-44bd-8d64-d50a2546edab",
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
  "uuid": "1479d39b-1bb4-40fc-90ce-84dd2fc8cc9c",
  "timestamp": "2026-05-30T07:30:36.111Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:30:36.111Z_

```json
{
  "parentUuid": "1479d39b-1bb4-40fc-90ce-84dd2fc8cc9c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b5d1ca19-4ea7-4762-9fa6-44d3aa4fab29",
  "timestamp": "2026-05-30T07:30:36.111Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive research coverage. Let me compile my…",
  "leafUuid": "b5d1ca19-4ea7-4762-9fa6-44d3aa4fab29",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Circuit-guided multi-point repair for RAG conflicts",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5"
}
```

---

### Assistant

_source line 8 · 2026-05-30T07:31:06.038Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' evaluations carefully to produce a Meta Judge synthesis.

**Reviewer 1**: [30% - 47%] 中位 38%
**Reviewer 2**: [33% - 48%] 中位 40%
**Reviewer 3**: [30% - 44%] 中位 37%

Three midpoints: 38%, 40%, 37%
Mean: 38.33%
Median: 38%
Std of midpoints: sqrt(((38-38.33)^2 + (40-38.33)^2 + (37-38.33)^2)/3) = sqrt((0.11 + 2.79 + 1.77)/3) = sqrt(1.56) ≈ 1.25%


The standard deviation is well under 3%, indicating strong agreement across reviewers.

Now I'm mapping out where the consensus lies across different dimensions. Research Question, Experimental Design, and Writing all show unanimous strong ratings. Method & Innovation leans toward strong with one reviewer being slightly more cautious. Feasibility is consistently rated as moderate across all three. I'm also noting which risks appear in multiple reviews to identify the main concerns.

The most critical consensus risks are the CD-T scaling challenge, circuit sparsity assumptions, whether arbiter structures actually exist, and insufficient details on rotational correction operationalization. There's also agreement that JuICE is a tough baseline to surpass, the scope might be overambitious, the instance-adaptive probe design needs clarification, and the overall system complexity is high. One reviewer raises a distinctive point about HAGD not modeling attention circuits—something the other two don't emphasize as strongly—and suggests adding a naive pipeline combination baseline as a control.

Now I'm calculating the consensus score range. The three reviewers' lower bounds cluster around 30-33%, upper bounds around 44-48%, and midpoints around 37-40%. Given how tightly these estimates align, I should anchor to the median values: 30% lower, 47% upper, 38% midpoint. The high consistency suggests I can narrow the interval confidently, and the "quality over quantity" principle combined with the most conservative reviewer's assessment points me slightly toward the lower end of this range.

My final assessment is 30-46% with a median of 38%. Now I need to synthesize the implementation assessment across all three reviews and prepare the output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5d1ca19-4ea7-4762-9fa6-44d3aa4fab29",
  "isSidechain": false,
  "requestId": "req_011CbYMwYJNAtXVxRtLw9EEH",
  "type": "assistant",
  "uuid": "d15d2baa-0e53-46cc-9ef3-7dc149d6e553",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPnPfHK1MgKCtTmtHpKCjo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21413,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2879,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 21413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21413
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

_source line 9 · 2026-05-30T07:31:57.842Z_

【阶段】: Meta Judge
【三次中位】: [38%, 40%, 37%]  std=1.25%
【共识维度】: 
- 研究问题: 强（3/3 一致）— RAG evidence override 问题重要且时机恰当，五条研究线索汇聚论述有说服力
- 方法与创新: 强（2/3 强，1/3 中偏强）— unified circuit vs Basu et al. two-circuit 的差异化真实成立；arbiter structures 是原创预测；rotational correction 的首次操作化有独特性
- 实验设计: 强（3/3 一致）— 四层 baseline、7 变体消融、cardinality curve、统计严谨性，proposal 阶段即达顶会水平
- 可行性: 中（3/3 一致）— CD-T scaling 是核心瓶颈（仅 GPT-2 验证过）；circuit sparsity 假设未验证；系统复杂度高
- 写作与呈现: 强（3/3 一致）— 叙事结构清晰、文献定位精准、风险披露诚实
- **共识风险点**（3/3 均提及）: ① CD-T 从 GPT-2 到 1-3B 的 scaling gap 是实质性执行风险；② arbiter structures 可能不存在或贡献微弱；③ rotational correction 操作化细节不足；④ instance-adaptive probe 设计模糊；⑤ JuICE (ICML Spotlight) 是极强 baseline，增量收益可能有限
- **共识风险点**（2/3 提及）: ⑥ 三个 contributions 的 scope 对单篇论文过于宏大（R2, R3）

【异常维度】: 
- R3 独有: HAGD 不建模 attention circuit，作为 fallback 存在硬伤（有效观点，但 R1/R2 未单独标记为高风险）
- R3 独有: 缺少 "naive pipeline combination" baseline（JuICE + CoRect + rotational 简单组合）— 合理建议但属实验细节层面
- R1 独有: 仅使用 base models 与实际 RAG 场景（instruct models）存在 gap — 有效但非致命

【最终概率】: [30% - 46%] 中位 38%
【一致性】: 高（std=1.25%，远低于 3% 阈值）
【综合理由】: 

三位审稿人在所有五个 rubric 维度上达到了罕见的高度一致：研究问题、实验设计、写作均为"强"，可行性均为"中"，方法创新 2 强 1 中偏强。概率估计极为收敛（37-40%，std 仅 1.25%），表明该 proposal 的质量信号明确、没有争议性的判断分歧。

**上行因素**（支撑 46% 上界）: Novelty claim 经三位审稿人独立调研均确认成立——unified conflict resolution circuit + arbiter structures + rotational correction 操作化在现有文献中确无先例。实验设计被一致认为是 proposal 最突出的亮点。三层贡献的内在一致性使得即使 C2 受限，C1+C3 仍有独立科学价值（fallback 策略成熟）。

**下行因素**（约束 30% 下界）: 三位审稿人一致指出的执行风险是真实且不可回避的——CD-T 的 scaling 跨度（GPT-2 → 1-3B）在领域内尚无先例，HAGD fallback 被 R3 正确指出不建模 attention（降权处理但保留参考）。JuICE 作为 ICML Spotlight 的简洁方法设立了极高的 bar，CirRAG 的额外复杂度需要换来显著的性能增益。Circuit sparsity 假设如不成立，C2 的价值大幅缩水。

**中位 38% 的校准逻辑**: 取三位审稿人中位的中位（38%），不做上调或下调。理由：(1) 高一致性意味着无需额外保守调整；(2) 该 proposal 的信号结构清晰——idea 层面约 40-45% 天花板（Novelty 强但 arbiter structures 未验证），执行风险将实际概率拉至 35-40% 区间；(3) 38% 反映"显著高于平均质量但存在实质性执行风险"的判断，与 AAAI ~20-25% 接受率相比，该 proposal 处于 borderline accept 区间。

【建议】: 边缘（偏积极）— idea 方向正确、craftsmanship 出色，值得推进实验验证；核心风险在执行而非立意，中稿概率取决于实验结果能否兑现 proposal 承诺

【实施评估】:
  - 计算资源: **中高**。三位审稿人估计趋同：核心实验（1-3B 模型）单卡可完成 circuit discovery + intervention 评估；8B 扩展需 A100 80GB × 4+。Circuit discovery 在 1-3B 上的时间成本取决于 CD-T scaling behavior（未知但关键）。Baseline 复现 + 消融实验 + 3 seeds 增加总量。综合估计：A100 80GB × 4-8 卡，持续 4-8 周（取 R1 偏乐观和 R3 偏保守的中间值）。
  - 数据需求: **低**（3/3 一致）。所有数据集（ConflictQA, NQ-Swap, MemoTrap, ConFiQA, CoFaithfulQA）均公开可用，无需新数据收集。JuICE coherent partition 需确认公开状态。
  - 人工介入: **中**（3/3 一致）。Circuit 分析结果解读、arbiter structure 识别、rotational correction 参数化方案设计均需人工判断，非全自动 pipeline。
  - 训练需求: **低**（3/3 一致）。CirRAG 是 training-free inference-time intervention。Instance-adaptive probe 需少量训练但规模小。无需训练或微调 LLM 本身。
  - 新 Benchmark: **否**（3/3 一致）。使用已有 benchmark，无需构建新评测数据集。
  - 预估周期: **3.5-5.5 个月**（取 R1 的 10-14 周和 R3 的 5-7 个月的加权中位）。关键路径在 Stage 1 的 circuit discovery scaling——若顺利则 3.5 个月可完成，若遇阻需 5+ 个月。对 AAAI 2026 投稿（假设 2026 年 8 月 DDL）时间紧凑但可行，建议尽早启动 Stage 1 以验证 CD-T scaling 可行性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d15d2baa-0e53-46cc-9ef3-7dc149d6e553",
  "isSidechain": false,
  "requestId": "req_011CbYMwYJNAtXVxRtLw9EEH",
  "type": "assistant",
  "uuid": "0491da04-be38-439f-b3ff-2c5dd8a0a616",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPnPfHK1MgKCtTmtHpKCjo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21413,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2879,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 21413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21413
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive research coverage. Let me compile my…",
  "leafUuid": "0491da04-be38-439f-b3ff-2c5dd8a0a616",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Circuit-guided multi-point repair for RAG conflicts",
  "sessionId": "9fb15aa1-ebee-4088-ae10-62bbd1cf90d5"
}
```

---
