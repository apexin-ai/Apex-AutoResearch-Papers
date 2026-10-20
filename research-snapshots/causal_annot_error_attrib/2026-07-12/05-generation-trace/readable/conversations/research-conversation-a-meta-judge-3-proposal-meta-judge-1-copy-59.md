# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/a4f86aec-3b40-48f1-8258-c157820c89af.jsonl`
- **Structured JSON:** [`133eb054e6abac8ead40.json`](../../sessions/13/133eb054e6abac8ead40.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:43:57.372Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:43:57.372Z",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient literature context. Let me compile the comprehensive evaluation.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026): 本 proposal 的核心理论基础。纯理论工作，证明 Pareto 前沿是由 principal angle α 参数化的椭圆，但无任何实验验证，作者自述在大扰动下失效。该框架是全新且未经验证的——这既是机会也是风险。\n- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026): 本 proposal 的另一核心支柱。引入 MSO 度量参数空间中安全-能力子空间的纠缠。仅在 chat 场景、1B-7B 模型上验证。Proposal 正确地指出 MSO（参数空间）与 α（激活空间）之间从未建立联系。\n- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025): 揭示安全方向在激活空间中是多维正交的，有主导拒绝方向和可解释的次级方向。仅 Llama 3 8B chat 场景。Proposal 拟将此扩展到 agent 和 MoE。\n- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (arXiv, Mar 2026, Plaut): 发现 agentic DPO 的近线性 Pareto 前沿（R²=0.77）。仅用 2 个 β 值、8B-14B dense 模型、无表征分析、无 MoE。Proposal 的核心动机之一是几何地解释这一观察。\n- [NSPO: Null-Space Constrained Policy Optimization](https://arxiv.org/abs/2512.11391) (ICLR 2026): 将安全梯度投影到能力空间的零空间。假设子空间可分离——若 MSO 与 α 不对应，此方法的理论基础存疑。Proposal 的 C1 对此有直接意义。\n- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448) (arXiv, Feb 2026): 识别安全关键专家，证明 MoE 安全通过路由动态实现。Proposal 的 C3（MoE 压力测试）直接建立在此发现之上。\n- [AQI: Alignment Quality Index](https://aclanthology.org/2025.emnlp-main.145/) (EMNLP 2025): 用聚类散度度量潜在几何来诊断对齐质量。与本 proposal 相关但不同——AQI 用标量聚类指标，proposal 用 principal angles 参数化前沿形状。\n- [OGPSA: Safety Alignment via Orthogonal Gradient Projection](https://arxiv.org/abs/2602.07892) (Feb 2026): 另一个假设子空间可分离的参数空间方法。\n- [SAFEx](https://arxiv.org/abs/2506.17368), [Sparse Models Sparse Safety](https://arxiv.org/abs/2602.08621): 证明 MoE 中少量专家承载安全功能（禁用 12/6144 专家降低拒绝率 22%），进一步支持 MoE 安全是路由介导的论点。\n\n- **调研总结**: 对齐税的几何理论（2603.00047）是 2026 年初的全新理论框架，尚无实证验证。MSO、principal angles、MoE routing safety 三条研究线独立发展，确实没有工作尝试连接它们。Proposal 识别出了一个**真实的**、**未被填补的**交叉点。但该交叉点主要是\"测量/诊断\"性质——用现有工具在新设定下测量——而非提出新方法。\n\n【整体印象】:\n作为审稿人，我的第一反应是：这是一份在文献综述和实验设计上**异常详尽**的 proposal，展示了对领域的深度理解和严谨的方法论规划。它正确识别了一个真实的研究空白——参数空间纠缠度量（MSO）与激活空间几何（principal angle α）之间从未建立对应关系，几何框架也从未在 MoE 或 agentic 设定下被验证。\n\n然而，我的核心犹豫是：**这本质上是一项纯测量/表征研究**，核心操作是将已有的分析工具（MSO、SVD、DPO sweep）应用到新的组合设定中。三个贡献（C1 跨空间桥梁、C2 诊断双估计、C3 MoE 压力测试）中，方法论创新有限，主要价值在于\"首次在这些条件下测量\"。此外，proposal **严重过载**——三个独立贡献各需大量实验，压入一篇论文中每个都可能处理不够深入。\n\n我会倾向给一个 **borderline / weak reject**，除非实验结果揭示出显著出乎意料的发现。\n\n【核心贡献】:\n1. **C1（跨空间度量桥梁）**: 首次建立 MSO（参数空间纠缠）与 α_repr（激活空间几何）的层级对应关系。这是最具原创性的贡献，对判断参数空间干预（NSPO, OGPSA）与激活空间诊断是否操作在兼容基础上有直接意义。但其价值高度依赖于发现的性质——若二者强相关，解释力有限（可能由共因混淆）；若不相关，也难以区分是根本不兼容还是测量方法差异所致。\n2. **C2（诊断双估计测试）**: 比较 α_repr 与 α_frontier，配合 2×2 预注册结果拓扑。实验设计理念优秀（确保任何结果都可解释），但本质上是在测试一个全新且未验证的理论框架——验证或否证一个 March 2026 的纯理论论文的实践价值取决于该理论的影响力。\n3. **C3（MoE 压力测试）**: 测试连续子空间几何假设是否适用于路由介导的 MoE 安全。方向合理，但预期结果（MoE 中几何框架失效）较为可预见。\n\n对领域的价值：**中等**。如果该几何框架成为后续工作的重要基础，这项实证验证就很有价值。但该框架本身尚未被社区广泛采纳，测量性工作的即时影响力有限。\n\n【方法合理性】:\n方法总体合理，但有若干关切：\n\n1. **跨空间对应（C1）的方法论脆弱性**：用混合效应模型在 ~80-100 个层级数据点上拟合 MSO 与 α_repr 的对应关系，但两者可能因共同的混淆因素（如层深度效应）而产生虚假相关。仅有相关性不足以证明\"可兼容的基础\"。\n2. **前沿形状判别**：Proposal 自身承认若 α < 10°，PSIS-LOO 可能无法区分椭圆与线性模型。鉴于高纠缠（MSO 文献强烈暗示）的预期，大多数条件可能确实产生小 α，使 C2 的核心判别变得不可行。\n3. **参数匹配问题**：Dense（32.8B）vs. MoE（22B active）的比较存在固有混淆，FLOP 归一化分析只能部分缓解。\n4. **更简单的替代方案**：C1 可以不依赖 DPO sweep，直接在 base/aligned/harmful 模型上提取两个空间的度量进行对比，大幅减少实验复杂度。C3 的核心发现（MoE 中几何框架失效）可能通过更简单的案例研究就能得出。\n\n**是否有更简单的方案？** 是的。该 proposal 将过多维度压入一个实验中。一个更聚焦的版本可以：(a) 只做 C1（跨空间桥梁）在多个模型上，或 (b) 只做 C3（MoE 压力测试）配合前沿映射。当前方案试图同时推进三个前沿，每个都可能因实验页面限制而变得单薄。\n\n【5 维度打分】:\n  1. 研究问题: **中偏强** — 识别出的研究空白是真实的：参数空间与激活空间安全度量的断裂、几何框架在 MoE/agent 下的适用性，均为该领域尚未回答的有意义问题。但这些问题的\"紧迫性\"和\"影响力\"有限——解答它们主要服务于理论完备性，对实践（如改进安全对齐方法）的直接启示不明确。Plaut 的线性前沿缺乏几何解释是一个好切入点。\n  \n  2. 方法与创新: **中偏弱** — 三个贡献均是将已有分析工具（MSO、SVD principal angles、DPO sweep、Bayesian 模型比较）应用于新组合。方法论本身无创新——MSO 直接沿用 ICLR 2026 论文，principal angles 是标准线性代数，前沿拟合用标准贝叶斯方法。预注册结果拓扑是一个亮点（受 [Hidden Dimensions, ICML 2025] 的多维分析启发但走了不同方向），但不构成方法论贡献。与 AQI (EMNLP 2025) 相比，AQI 至少提出了新的组合度量（XBI, CHI, DBI, DI 的整合），而本 proposal 的\"桥梁\"主要是在两个已有度量之间跑相关。\n  \n  3. 实验设计: **强** — 这是 proposal 最大的亮点。2×2 因子设计干净；16 β 值密集扫描（相比 Plaut 的 2 个β）充分覆盖参数空间；优先级分层（Tier 1/2/3）现实且合理；灵敏度消融（子空间秩 K、数据源、token 位置）全面；统计方法（PSIS-LOO、WAIC、mixed-effects）严谨；预注册结果拓扑确保任何结果都可解释；MoE 消融（shared-attention-only、active-expert-only LoRA）针对性强。后备方案（Maverick 降级、小 α 重新定义贡献）体现务实性。这是一份**远超平均投稿**的实验设计。\n  \n  4. 可行性: **中** — 3,500-5,000 GPU-hours、$10,500-$15,000 不算天文数字但也不小。主要风险点：(a) 400B Maverick 的 DPO 训练可行性存疑（proposal 有后备方案）；(b) 16 周时间线紧张——Phase 1-3 有重叠但 wk 1-2 的 infra validation 可能出意外；(c) 三个评估框架（OpenAgentSafety、ATBench、tau2-bench）加 AdvBench 的整合工程量大；(d) 结果可能因多种原因模糊不清（小 α、高噪声、不同度量的不一致）。Tier 制度和后备方案是加分项。\n  \n  5. 写作与呈现: **中** — Proposal 本身写得信息密度极高、文献覆盖全面、逻辑链条完整。但**过度工程化**是突出问题——proposal 读起来像是在试图覆盖所有可能的质疑（token 位置消融、数据源消融、参数匹配消融、FLOP 归一化、两种统计方法、后备方案...），反而模糊了核心叙事。一个好论文需要一个清晰的 take-home message——\"我们发现了 X，这改变了你对 Y 的理解\"——而这份 proposal 的 take-home message 分散在三个 contributions 中。8 页正文可能装不下。\n\n【概率估计】: [20% - 35%] 中位 27%\n\n【估计理由】: \n**上拉因素**: (1) 识别出真实的研究空白，问题有意义；(2) 实验设计极为详尽，远超同类工作的方法论严谨性，这本身是显著加分项；(3) 预注册结果拓扑框架在方法论上值得肯定；(4) 领域高度时效性——2026年初的多篇核心论文刚出，连接它们有自然的新鲜感；(5) 对 Plaut 线性前沿的几何解释如果成立，是有吸引力的发现。\n\n**下拉因素**: (1) **纯测量/表征研究，无方法论创新**——这在顶会评审中通常被视为\"nice characterization but limited contribution\"，除非发现非常意外；(2) **严重过载**——三个独立贡献挤入一篇论文，每个可能处理单薄，8 页正文难以充分展开；(3) **多项预期发现较为平凡**——高纠缠环境下几何框架在 MoE 中失效、agent 比 chat 纠缠更高——这些是多数研究者的默认预期，确认它们的价值有限；(4) **C1 跨空间桥梁的因果推断力弱**——层级相关可能由混淆因素驱动；(5) **所验证的理论框架（2603.00047）本身太新且影响力未知**——如果该框架最终未被社区采纳，验证工作的价值随之缩水。\n\n中位估计 27%，落在\"整体合格、有实质贡献，但缺乏突出亮点\"的区间。若实验产出出乎意料的发现（如 MSO 与 α 强烈不对应，或 MoE 中几何框架意外成立），概率可升至 35%+。若发现平凡且叙事不聚焦，概率可能跌至 20% 以下。\n\n【主要风险】:\n1. **\"So what?\" 问题**: 审稿人可能认为这是一项勤勉但缺乏 actionable insight 的表征研究——\"你确认了几何框架在 MoE 中不适用，那然后呢？\" 缺少干预阶段（proposal 明确排除了）意味着没有展示这些测量如何转化为更好的对齐方法。\n2. **叙事分散/过载**: 三个独立贡献（跨空间桥梁 + 诊断双估计 + MoE 压力测试）难以在 8 页内讲一个统一的、有力的故事。审稿人可能觉得每个贡献都只触及表面，建议拆分为多篇论文。\n\n【实施评估】:\n  - 计算资源: 3,500-5,000 GPU-hours (H100)，$10,500-$15,000，属于中高规模实证研究\n  - 数据需求: 使用已有数据集（OpenAgentSafety, ATBench, AdvBench, BeaverTails, tau2-bench），无需构建新数据集\n  - 人工介入: 较低——主要是工程和分析自动化，无需人工标注\n  - 训练需求: 128 个 LoRA-DPO 训练 run（Tier 1+2），最多 192 个（含 Tier 3）+ MoE 消融，每次 ~5 hr on 4-8×H100\n  - 新 Benchmark: 否——使用已有 benchmark\n  - 预估周期: 16 周（proposal 自述），但考虑 infra 调试和意外情况，实际可能 18-20 周\n```\n\nSources:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)\n- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185)\n- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674)\n- [Safety Training Persists Through Helpfulness Optimization](https://arxiv.org/abs/2603.02229)\n- [NSPO: Null-Space Constrained Policy Optimization](https://arxiv.org/abs/2512.11391)\n- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448)\n- [AQI: Alignment Quality Index](https://aclanthology.org/2025.emnlp-main.145/)\n- [OGPSA: Safety Alignment via Orthogonal Gradient Projection](https://arxiv.org/abs/2602.07892)\n- [SAFEx: MoE Vulnerabilities](https://arxiv.org/abs/2506.17368)\n- [Sparse Models Sparse Safety](https://arxiv.org/abs/2602.08621)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [What Is the Geometry of the Alignment Tax? (arXiv 2603.00047)](https://arxiv.org/abs/2603.00047) (Mar 2026): The theoretical backbone of this proposal. Proves Pareto frontier is an ellipse parameterized by principal angle α. Purely theoretical — no empirical validation. Explicitly acknowledges failure under large perturbations / nonlinear encoding. This proposal's C2 directly attempts to empirically validate and stress-test this framework.\n- [Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185)](https://arxiv.org/abs/2505.14185) (ICLR 2026): Introduces MSO (parameter-space entanglement metric). Tested only on ≤7B models, chat-only setting. This proposal's C1 attempts to bridge MSO to activation-space principal angles — a gap this paper leaves entirely open.\n- [The Hidden Dimensions of LLM Alignment (arXiv 2502.09674)](https://arxiv.org/abs/2502.09674) (ICML 2025): Multi-dimensional orthogonal safety directions in activation space, but only on Llama 3 8B in chat. No connection to parameter-space metrics or MoE architectures.\n- [Safety Training Persists Through Helpfulness Optimization — Plaut (arXiv 2603.02229)](https://arxiv.org/abs/2603.02229) (Mar 2026): Finds near-linear Pareto frontier (R²=0.77) in agentic DPO. Only 2 β values, ≤14B dense models, no representation analysis, no geometric explanation. This proposal aims to explain this observation geometrically.\n- [NSPO (arXiv 2512.11391)](https://arxiv.org/abs/2512.11391) (ICLR 2026): Projects safety gradients into null space of capability covariance — parameter-space intervention assuming separable subspaces. If MSO–α_repr don't correspond, NSPO's foundational assumption is challenged.\n- [RASA (arXiv 2602.04448)](https://arxiv.org/abs/2602.04448) (Feb 2026): Identifies safety-critical experts via routing analysis in MoE. Directly motivates C3 — safety in MoE is routing-mediated, making continuous-subspace geometry potentially inapplicable.\n- [AQI (arXiv 2506.13901)](https://arxiv.org/abs/2506.13901) (EMNLP 2025): Uses latent geometry (cluster divergence) to diagnose alignment quality. Related but methodologically distinct — cluster metrics vs. principal angles. No cross-space, MoE, or agent analysis.\n- 调研总结: The proposal sits at a genuine convergence point where 4+ independent research threads (geometric alignment tax theory, parameter-space entanglement, MoE routing safety, agentic safety divergence) have left clear bridging gaps. **No existing work connects parameter-space MSO to activation-space principal angles, measures alignment geometry under entanglement in agentic settings, or tests the geometric framework on MoE architectures.** The novelty claim is well-supported.\n\n【整体印象】:\n作为审稿人，我的第一反应是：这是一份极其深思熟虑、文献调研无可挑剔的 proposal，识别了一个真实且重要的理论空白。但随之而来的直觉反应是——**这篇论文试图在一篇 paper 里做太多事情**。三个 contribution（C1 跨空间桥梁、C2 诊断性双估计检验、C3 MoE 压力测试），4个模型 × 2个设置 × 16个 β 值 = 128+ 次 DPO 训练，加上 MoE 三层分解、多种 ablation、Bayesian 模型比较……这不是一篇 8 页论文能装下的。\n\n更根本的是：**这是一篇纯测量/表征论文，没有提出任何干预方法**。proposal 明确声明 \"We exclude intervention phases\"。这意味着它的 contribution 完全依赖于测量本身的价值。虽然好的测量论文确实存在（例如 MSO 论文本身就是），但在这种情况下，花费 3,500-5,000 GPU-hours 做一个表征研究，审稿人会问 \"so what?\" — 这些测量结果能指导什么具体行动？\n\n我的倾向是 **borderline reject / weak accept**，取决于执行质量和写作清晰度。\n\n【核心贡献】:\n核心贡献是三方面的：\n1. **C1（最有价值）**: 首次建立 parameter-space MSO 与 activation-space α_repr 的跨空间对应关系。这是一个真实的测量学空白——如果这两个度量不对应，那么 NSPO/OGPSA 等 parameter-space 干预方法和 activation-space 诊断工具实际上在分析不同的结构，对 alignment 干预设计有直接影响。\n2. **C2（方法论创新）**: Pre-registered outcome topology 是一个聪明的设计选择——无论结果如何，论文都有信息价值。但这更像是一个好的实验设计原则，不是独立的 contribution。\n3. **C3（及时性强）**: MoE 架构已成为 frontier model 的主流，测试几何框架在 routing-mediated safety 下的适用性是重要的。\n\n总体而言，C1 对领域有中等偏高价值——如果执行得好，它能回答 \"parameter-space 和 activation-space 的 alignment 分析是否看的是同一个东西\" 这个关键问题。但价值是条件性的：如果答案是 \"它们大致对应\"，那信息增量有限；如果不对应，信息量更大但需要后续工作来利用这个发现。\n\n【方法合理性】:\n方法论整体合理但有几个关键问题：\n\n1. **Layer-wise mixed-effects model 的统计有效性**：用层级数据点（~80-100 个）来弥补条件级分析（n=8）的统计力不足，但层间数据有强自相关性（相邻层的 MSO 和 α_repr 高度相关），违反了混合效应模型的独立性假设。如果不做适当的空间自相关校正，p 值可能严重膨胀。\n\n2. **Elliptic vs. Linear 判别**：这是 C2 的核心，但如果 α 确实很小（如 <10°），椭圆和直线在统计上几乎不可区分。proposal 承认了这一点并设计了 \"small-α fallback\"，但 fallback 的 contribution 明显弱于原始假设——\"证明 α 确实很小\" 基本等于确认已有的猜测。\n\n3. **Dense-MoE 对比的 confound**: 即使在 Qwen3 family 内，dense (32.8B) vs. MoE (22B active) 的 active parameter count 差异很大。FLOP-normalized 分析能部分缓解，但不能完全消除架构差异以外的 confound。\n\n4. **更简单的替代方案**：C1 的跨空间对应可以在更小规模（2-3 模型 × 8 β 值）上先验证，然后再扩展。目前的设计把验证性分析和大规模系统性测量混在一起，不够高效。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】— 跨空间度量对应、MoE 几何框架适用性、agentic 设置下的 alignment geometry 都是真实且重要的开放问题。四条独立研究线的汇聚点识别得很准确，文献覆盖几乎堪称详尽。Plaut 的近线性 frontier 缺乏几何解释、NSPO/OGPSA 假设 parameter-space 和 activation-space 可互换但缺乏验证——这些都是经得起推敲的 research gap。\n\n2. 方法与创新: 【中】— 跨空间桥梁（C1）在概念上新颖，但方法本身是对现有工具（MSO、principal angle SVD）的组合应用，不涉及新的数学工具或算法。Pre-registered outcome topology（C2）是好的实验设计但不是方法创新。与 [AQI (EMNLP 2025)](https://arxiv.org/abs/2506.13901) 相比，本文在方法层面的创新更多体现在\"桥接\"而非\"发明\"。与 [Hidden Dimensions (ICML 2025)](https://arxiv.org/abs/2502.09674) 相比，本文的 activation-space 分析本质上是扩展而非突破。核心方法论担忧是层级混合效应模型在处理自相关数据时的统计有效性。\n\n3. 实验设计: 【强】— 这是 proposal 最突出的亮点。2×2 factorial design 合理，16-point β sweep 远超 Plaut 的 2 β 值，Bayesian model comparison (PSIS-LOO + WAIC) 比简单的 curve fitting 严谨得多。敏感性 ablation（数据源、token 位置、subspace rank K）覆盖全面。Priority tier 系统和 Maverick fallback 显示了实际执行智慧。与 [Plaut (arXiv 2603.02229)](https://arxiv.org/abs/2603.02229) 的实验规模（2 β, 3 models, no representation analysis）相比，这是量级提升。与 [MSO 论文 (ICLR 2026)](https://arxiv.org/abs/2505.14185) 的 ≤7B chat-only 范围相比，本文在 scale 和 coverage 上有实质性扩展。唯一的短板是有效样本量：8 个条件对 meta-analytic agreement testing 来说偏少，层级混合效应模型是否能真正解决这个问题存疑。\n\n4. 可行性: 【中】— 3,500-5,000 GPU-hours、$10,500-$15,000 GPU cost 是可负担的（对有资源的实验室而言），但 16 周的时间线在 128+ DPO 训练、大规模 activation 提取、MoE 三层分解等工作面前非常紧张。Maverick (400B total) 的 DPO 训练可能在实际操作中比预期更难——reference offloading for 400B 参数的 MoE 在 8×H100 上的可行性存在不确定性。如果 Tier 3 被迫降级到 Qwen3-30B-A3B (3.3B active)，与 dense 模型 (32B) 的 active parameter 差距扩大到 ~10x，可比性进一步削弱。写作方面，把三个 contribution + 完整的实验结果 + 所有 ablation 压缩到 8 页正文 + appendix 是一个极大的挑战。\n\n5. 写作与呈现: 【中】— proposal 的文献覆盖和逻辑链条是其强项，但也恰恰暴露了潜在的写作问题：当前 proposal 已经极其密集，术语堆叠严重（MSO、α_repr、α_frontier、PSIS-LOO、WAIC、RoSais、FLOP-normalized、HELLoRA-style 等），如果论文也是这种密度，审稿人可能在理解核心贡献之前就失去耐心。标题 \"Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings\" 有 15 个词，试图把所有关键词塞进去，反而模糊了焦点。\n\n【概率估计】: [20% - 35%] 中位 27%\n\n【估计理由】:\n推理过程：\n\n**向上推的因素（+）**：\n- 研究问题真实且重要，文献空白验证充分（+）\n- 实验设计在方法论上非常严谨，远超该领域同类工作（+）\n- Pre-registered outcome topology 确保论文在任何结果下都有贡献（+）\n- 话题极度 timely——alignment tax、MoE safety、agentic safety 都是 2026 热点（+）\n- 跨空间桥梁（C1）对 alignment intervention 设计有实际意义（+）\n\n**向下拉的因素（−）**：\n- **纯测量论文没有干预方法**：在 EMNLP 这样的会议上，\"we measured X and found Y\" 的贡献往往被认为不如 \"we found problem X and solved it with method Y\"。三个 contribution 都是测量/诊断性质的，缺乏 actionable output（−−）\n- **范围过大**：三个 contribution 每一个都可以是独立论文的核心。把它们全塞进一篇 8 页论文，每个都难以充分展开（−−）\n- **统计力担忧**：核心 claim（C2 的 α_repr–α_frontier 一致性/分歧）在有效样本量 n=8 的条件下，即使用层级混合效应模型补救，也面临自相关数据的统计有效性质疑（−）\n- **Elliptic vs. Linear 判别的固有困难**：如果 α 确实很小，小样本下的 Bayesian 模型比较可能得出不确定结论，核心 story 变成 \"α 的上界估计\"，contribution 明显减弱（−）\n- **写作挑战极大**：proposal 的密度和复杂度暗示最终论文可能难以让不在这个精确交叉领域的审稿人快速理解（−）\n- **执行风险**：MoE 训练复杂度、400B 模型的 reference offloading、16 周 timeline 对应的工作量——实际执行中任何一个环节出问题都可能导致需要显著缩减范围（−）\n\n综合判断：这是一个识别能力极强的研究者写的 proposal，问题发现精准、实验设计严谨，但在 \"做什么\" 的选择上过于贪心，\"贡献什么\" 的层面偏向测量而非解决问题。在 EMNLP 2026 的竞争环境中，这种 profile 的论文通常落在 borderline 区域——如果执行完美、写作精炼、结果清晰，有望进入 25-35% 的 accept 区间；如果任何一个方面出问题，容易滑入 20-25% 的 reject 区间。中位估计 27%。\n\n【主要风险】:\n1. **\"纯测量无干预\" 的 contribution 定位**：审稿人可能认为 3,500-5,000 GPU-hours 的纯表征研究缺乏足够的 actionable insight。如果结果是 \"MSO 和 α_repr 大致对应\"，信息增量有限；如果不对应，没有后续解决方案，贡献感不足。在 EMNLP 的竞争环境中，measurement-only paper 需要极高的执行质量和结果的 surprising 程度才能获得 accept。\n2. **范围膨胀导致的深度不足**：三个 contribution 在 8 页内可能每个都只能浅尝辄止。特别是 C3（MoE 压力测试）涉及三层分解（shared attention、per-expert FFN、router weights），如果不能充分展开，会被视为 \"incomplete analysis\"。审稿人可能建议 \"拆成 2-3 篇更聚焦的论文\"。\n\n【实施评估】:\n  - 计算资源: 3,500–5,000 GPU-hr (4–8×H100)，$10,500–$15,000。对中等规模实验室可行，但不轻松。\n  - 数据需求: 依赖已有 benchmark（OpenAgentSafety、ATBench、AdvBench、BeaverTails、tau2-bench）。无需自建数据集，降低了风险。\n  - 人工介入: 相对低——主要是 pipeline 搭建和结果分析。Claude-assisted 自动化降低了人工成本。\n  - 训练需求: 大量 LoRA-DPO 训练（128+ runs），含 MoE 模型的 QLoRA 训练。MoE 训练（尤其 400B Maverick）的工程复杂度是主要风险点。\n  - 新 Benchmark: 不需要。完全使用已有 benchmark。\n  - 预估周期: 16 周（紧张但理论上可行）。实际可能需要 18-20 周，考虑到 MoE 训练的工程调试和可能的 Tier 3 降级。\n```\n\nSources:\n- [What Is the Geometry of the Alignment Tax? (arXiv 2603.00047)](https://arxiv.org/abs/2603.00047)\n- [Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185)](https://arxiv.org/abs/2505.14185)\n- [The Hidden Dimensions of LLM Alignment (arXiv 2502.09674)](https://arxiv.org/abs/2502.09674)\n- [Safety Training Persists Through Helpfulness Optimization — Plaut (arXiv 2603.02229)](https://arxiv.org/abs/2603.02229)\n- [NSPO (arXiv 2512.11391)](https://arxiv.org/abs/2512.11391)\n- [RASA (arXiv 2602.04448)](https://arxiv.org/abs/2602.04448)\n- [AQI (arXiv 2506.13901)](https://arxiv.org/abs/2506.13901)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to evaluate this proposal. Let me compile my assessment.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026): The theoretical foundation this proposal builds on. Purely theoretical — proves Pareto frontier is an ellipse parameterized by principal angle α. Explicitly notes limitations under large perturbations and nonlinear encoding. No empirical validation exists yet, which is the gap this proposal targets.\n- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026): Introduces MSO in parameter space; shows safety-capability subspaces are highly entangled on Llama 2/3.2 and Qwen 2.5 (1B–7B), chat only. Core tool for this proposal's C1 contribution. Confirmed real and accurately described.\n- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025): Multi-dimensional orthogonal safety directions in activation space on Llama 3 8B. Chat only. Provides the activation-space methodology for principal angle extraction. Accurately cited.\n- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (Plaut, Mar 2026): Observes near-linear Pareto frontier (R²=0.77) in agentic DPO on 8B–14B dense models with only 2 β values. No representation analysis, no MoE. This is the key empirical observation the proposal aims to geometrically explain.\n- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448) (Feb 2026): Shows safety in MoE is routing-mediated; full-parameter fine-tuning creates routing shortcuts. Restoring original routing collapses harmlessness by Δ∈[−0.38, −0.46]. Key evidence for C3.\n- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621) (Feb 2026): RoSais scores show masking 5 routers increases ASR 4× to 0.79. Further evidence that MoE safety is structurally different from dense safety.\n- [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026): Null-space projection method that assumes separable subspaces. This proposal argues if MSO and α_repr don't correspond, NSPO-like methods and activation-space diagnostics may be analyzing different structures.\n- [The Viscosity of Logic](https://arxiv.org/abs/2601.17260) (Jan 2026): Phase transitions in DPO β sweeps on 7B models. Motivates the dense β sampling design. Architecture-specific responses found (sharp in Mistral, smooth in Qwen).\n- [AQI](https://aclanthology.org/2025.emnlp-main.145/) (EMNLP 2025): Uses cluster divergence metrics on safe/unsafe activations for alignment diagnosis without generation. Most directly related prior work using representation geometry for alignment quality. Differs in using cluster quality (scalar) vs. principal angles (structural).\n- 调研总结: The gap identification is legitimate — no prior work connects parameter-space MSO to activation-space principal angles, tests the geometric framework on MoE architectures, or provides geometric explanation for Plaut's near-linear agentic frontier. However, this is an extremely crowded and fast-moving area (20+ papers in 3 months), and the proposal's contribution is fundamentally characterization/measurement rather than a new method or intervention.\n\n【整体印象】:\n如果我是审稿人，第一反应是：这是一份极其 well-researched 的 proposal，文献调研几乎无可挑剔，实验设计也非常严谨（pre-registered outcome topology、Bayesian model comparison、分层优先级）。但随之而来的第二反应是：这到底在贡献什么？三个 contributions 加在一起构成的是一个大型 empirical characterization study，但缺乏 actionable 的方法论输出——不提出新的 alignment 方法、不提出新的优化算法、不构建新的 benchmark。它的核心是\"测量并桥接两个已有的度量系统\"，这在 significance 上面临挑战。\n\n我会倾向于 **borderline reject**，理由是：(1) 核心贡献是诊断/测量性质的，缺乏直接的 actionable impact；(2) 过度铺展三个贡献导致每个都不够深入；(3) 部分结论可能无论结果如何都是\"意料之中\"的（MSO和α要么相关——说明它们测量相似结构，要么不相关——说明它们测量不同结构，两个结论都不够 surprising）。\n\n【核心贡献】:\n核心贡献是建立 parameter-space (MSO) 和 activation-space (principal angle α) 两个独立度量系统之间的 cross-space correspondence，并在 agentic + MoE 设置下测试几何理论框架的适用性。这本质上是一个 metrological/diagnostic 贡献——回答\"我们已有的两套工具是否在测量同一个底层现象？\"以及\"理论框架在更复杂的架构和设置下是否成立？\"\n\n对领域的价值：中等。如果发现 MSO 和 α_repr 高度对应，这为 parameter-space 干预方法（NSPO、OGPSA）和 activation-space 诊断方法提供了统一的理论基础，有实际意义。如果发现不对应，则警告社区不要混用两种范式。但无论哪种结果，直接影响偏间接——不会立即改变任何人的训练/对齐流程。\n\nMoE 作为几何框架的 stress test（C3）可能是最有趣的贡献，因为它直接关系到前沿模型（大多是 MoE 架构）的 alignment 实践。但这也是资源消耗最大、最可能出现技术障碍的部分。\n\n【方法合理性】:\n方法设计本身是合理且严谨的。2×2 factorial design、16-point β sweep、Bayesian model comparison（PSIS-LOO + WAIC）、pre-registered outcome topology——这些都是方法论上的良好实践。\n\n然而，存在几个合理性质疑：\n\n1. **Cross-space correspondence 的 layer-wise mixed-effects 分析**：用 ~80-100 个 (MSO_layer, α_repr_layer) 数据点做 mixed-effects model，每个 model-setting 条件只有 ~10-15 个 layers——这有严重的 pseudoreplication 风险。层与层之间高度非独立（特别是相邻层），mixed-effects model 的 random intercept 不足以解决这个问题。\n\n2. **α_repr vs. α_frontier 的比较**：α_repr 来自 Phase 1（representation analysis），α_frontier 来自 Phase 3（elliptic fit to Pareto frontier）。但 α_frontier 的估计依赖于 elliptic model 的拟合优度——如果大多数条件下 elliptic 和 linear model 不可区分（小 α scenario），α_frontier 的 uncertainty 会很大，使得 dual-estimation test 失去 power。\n\n3. **更简单的替代方案**：直接对比 dense vs. MoE 模型在相同 DPO 设置下的 Pareto frontier 形状，配合 representation probing，可能用 1/3 的资源达到 80% 的 insight。Cross-space bridge 和 diagnostic dual-estimation 增加了大量复杂性，但边际信息增益不确定。\n\n4. **Dense vs. MoE 的 confounding**：即使 Qwen3 family 内部比较，32B dense vs. 22B active MoE 在 active parameter count 上差 50%。FLOP-normalized analysis 帮助但不能完全消除 confound。\n\n【5 维度打分】:\n\n1. 研究问题: **中** — 问题是真实存在的：parameter-space 和 activation-space 的度量确实从未被连接，MoE 安全的几何理解确实缺失，Plaut 的近线性 frontier 确实缺乏解释。但这些更像是\"测量空白\"而非\"理解瓶颈\"——填补它们不会直接解决任何 alignment 的实际问题。对比同类工作：AQI (EMNLP 2025) 被接收是因为它提出了一个可直接使用的诊断工具；NSPO (ICLR 2026) 被接收是因为它提出了一个有效的优化方法。本 proposal 的输出更接近\"characterization report\"，在顶会中的价值定位不够清晰。\n\n2. 方法与创新: **中** — 方法论设计严谨（Bayesian model comparison、pre-registered outcomes、mixed-effects analysis），但创新主要在于\"将已有工具组合应用于新设置\"，而非提出新的分析工具或方法。Cross-space correspondence 是 MSO (ICLR 2026) + principal angles (arXiv 2603.00047) 的直接组合；MoE routing analysis 基本沿用 RASA (arXiv 2602.04448) 和 RoSais (arXiv 2602.08621) 的方法。Pre-registered outcome topology 是一个亮点，但更多是\"好的实验实践\"而非\"方法创新\"。\n\n3. 实验设计: **强** — 这是 proposal 最突出的优势。16-point β sweep（远超 Plaut 的 2 点）、2×2 factorial design（覆盖 dense/MoE × chat/agent）、Bayesian model comparison 而非 p-value hacking、多种 evaluation benchmarks（tau2-bench, OpenAgentSafety, ATBench, AdvBench）、sensitivity ablations（rank K, data source, token position）、power simulation before data collection、tiered priority system with fallback plans。这是顶会级别的实验设计。如果执行到位，实验部分本身没有明显漏洞。\n\n4. 可行性: **中偏弱** — 3,500-5,000 GPU-hours / $10,500-15,000 是一笔不小的开支。16 周时间线紧张但可行。最大风险点：(a) Maverick (400B total) 的 DPO 训练可能因内存问题不可行——proposal 承认了这一点并有 fallback，但 fallback 到 Qwen3-30B-A3B (3.3B active) 会大幅改变实验 narrative（从\"前沿规模 MoE\"变成\"小规模 MoE\"）；(b) 在 30B+ 模型上进行 128 runs (4 models × 2 settings × 16 β) 的 DPO 训练，加上 representation extraction 和 evaluation，需要非常高效的工程实践；(c) 多个 benchmark 的集成（tau2-bench, OpenAgentSafety, ATBench）增加了工程复杂度。对于一个不是大型实验室的团队来说，这个规模可能过于雄心勃勃。\n\n5. 写作与呈现: **中偏强** — Proposal 的文献覆盖极其全面（30+ 篇相关工作，每篇都精确定位与本工作的关系），逻辑结构清晰（Core Problem → Opportunity → Landscape → Approach → Resource）。但存在两个写作问题：(a) **过度密集**——信息密度太高，审稿人需要花大量精力理解三个 contributions 之间的关系和每个的具体内容，可能导致 reviewer fatigue；(b) **narrative 不够聚焦**——试图同时服务四个 narrative（cross-space bridge, geometric explanation of linearity, MoE stress test, probing-based prediction），核心 story 不够突出。\n\n【概率估计】: [18% - 32%] 中位 25%\n\n【估计理由】:\n**向上因素**：(1) Gap 是真实的，文献调研无懈可击，没有直接竞争的 concurrent work；(2) 实验设计非常严谨，方法论上挑不出大问题；(3) Pre-registered outcome topology 是审稿人喜欢的实验设计范式；(4) 如果 C3（MoE stress test）得出强结论（如 MoE 几何完全不同于 dense），这对前沿 alignment 实践有实际指导意义。\n\n**向下因素**：(1) **核心身份问题**——这是 characterization/measurement paper，不提出新方法或工具，在 top venue 的 impact bar 上处于劣势，审稿人可能评价为 \"interesting but incremental\"；(2) **三个 contributions 的聚焦度不足**——每个 contribution 独立来看都是\"测量 X 和 Y 是否对应\"或\"在新设置下验证已有框架\"，没有任何一个强到可以单独撑起一篇顶会；(3) **可预测性风险**——部分结论无论结果如何都不够 surprising（如果 MSO 和 α 对应：expected since both capture safety-capability geometry；如果不对应：trivially expected since they're in different spaces）；(4) **资源可行性**——如果 Maverick 不可行且 fallback 到小规模 MoE，C3 的 narrative 弱化严重；(5) **小 α scenario**——如果大多数条件下 α < 10°，C2 的 elliptic-vs-linear discrimination 可能 inconclusive，fallback 到 \"quantifying upper bound\" 虽然 informative 但不够 exciting。\n\n中位 25% 的定位理由：实验设计扎实将其拉到合格线以上，但 characterization paper 的身份和 significance 不足将其压在\"需要运气\"的区间。一个友好的审稿人组可能给 borderline accept，但大概率会有至少一个审稿人质疑 \"so what?\"。\n\n【主要风险】:\n1. **\"So what?\" 风险**：审稿人质疑——\"你测量了 MSO 和 α 的对应关系，发现它们对应/不对应，然后呢？这如何改变我们做 alignment 的方式？\"缺乏从诊断到行动的闭环（proposal 明确排除了 intervention phase），这在顶会中是常见的 reject 理由。\n2. **Scope 过大导致执行不完整**：128 runs DPO + representation extraction + multi-benchmark evaluation + MoE routing analysis，如果任何环节出现技术困难（Maverick 不可行、某个 benchmark 集成有 bug、某些 β 值训练不稳定），整个 2×2 design 的完整性就会受损，paper 会变成\"我们做了一部分实验，结论是 preliminary\"。\n\n【实施评估】:\n  - 计算资源: 3,500-5,000 GPU-hours (4-8×H100)，$10,500-15,000。属于中等偏大规模实验，需要稳定的 GPU 集群访问或充足的 cloud budget。\n  - 数据需求: 主要依赖已有 benchmark（OpenAgentSafety, ATBench, AdvBench, tau2-bench, BeaverTails）。不需要构建新数据集，但需要集成多个异构 benchmark 的 evaluation pipeline，工程量不小。\n  - 人工介入: 中等。probe code、evaluation pipeline 搭建需要扎实的工程能力。统计分析（Bayesian model comparison, mixed-effects modeling）需要统计学专业知识。\n  - 训练需求: 是，需要对 4 个 30B+ 模型进行 LoRA-DPO 训练，每个模型 16 个 β 值 × 2 个 setting。MoE 模型的 DPO 训练可能需要 reference model offloading 等特殊处理。\n  - 新 Benchmark: 否，不需要构建新 benchmark。\n  - 预估周期: 16 周（proposal 自估），考虑到工程调试和不可预见问题，20 周更现实。\n```\n\nSources:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)\n- [Safety Subspaces are Not Linearly Distinct (ICLR 2026)](https://arxiv.org/abs/2505.14185)\n- [The Hidden Dimensions of LLM Alignment (ICML 2025)](https://arxiv.org/abs/2502.09674)\n- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229)\n- [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448)\n- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621)\n- [NSPO (ICLR 2026)](https://arxiv.org/abs/2512.11391)\n- [The Viscosity of Logic](https://arxiv.org/abs/2601.17260)\n- [AQI (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.145/)\n- [The Geometry of Alignment Collapse](https://arxiv.org/abs/2602.15799)\n- [OGPSA](https://arxiv.org/abs/2602.07892)\n- [SAFEx](https://arxiv.org/abs/2506.17368)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings\n\n## Description\n\nThe alignment tax has been formalized geometrically with elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces (arXiv 2603.00047). But empirically, these subspaces are highly entangled (MSO, ICLR 2026), MoE architectures route safety through sparse expert dynamics, and in agentic settings Plaut (arXiv 2603.02229) observes a near-linear frontier (R²=0.77) without geometric explanation. We hypothesize: high entanglement yields small α, degenerating the ellipse toward linearity, while MoE routing introduces discrete dynamics that violate the framework's continuous-subspace assumptions. We produce three contributions. (C1) The first empirical bridge between two independent metric systems — MSO (parameter-space entanglement, ICLR 2026) and principal angle α (activation-space geometry) — establishing their cross-space correspondence via layer-wise mixed-effects analysis; this determines whether parameter-space interventions (NSPO arXiv 2512.11391, OGPSA arXiv 2602.07892) and activation-space diagnostics operate on compatible foundations, and provides initial evidence for probing-based alignment tax prediction without full DPO sweeps. (C2) A diagnostic dual-estimation test with pre-registered outcome topology: α_repr–α_frontier agreement validates geometric theory under entanglement, while systematic divergence quantifies the linear representation hypothesis's failure boundary; a 2×2 outcome matrix ({dense,MoE} × {chat,agent}) pre-registers interpretations for every divergence pattern, making the paper informative under any result. (C3) MoE as a stress test of continuous-subspace geometry: if safety is routing-mediated (RASA, arXiv 2602.04448), activation-space α may fail to capture MoE safety structure, and α_repr–α_frontier divergence should be larger in MoE than dense models. Using a 2×2 design — {Qwen3-32B, Gemma 4 31B} (dense) × {Qwen3-235B-A22B, Llama-4-Maverick} (MoE) in {chat, agent} — we sweep 16 LoRA-DPO β values per condition with Bayesian model comparison (PSIS-LOO + WAIC) and meta-analytic agreement testing. Expected: (1) higher MSO in agents vs. chat; (2) α_repr ≈ α_frontier in dense models, both smaller in agents (explaining Plaut's frontier as a low-angle ellipse); (3) larger α_repr–α_frontier divergence in MoE than dense, quantifying routing-mediated geometry violation; (4) layer-wise MSO–α_repr correspondence establishing whether parameter-space and activation-space analyses are compatible paradigms.\n\n## Core Problem\n\nThe alignment tax has been formalized geometrically under the linear representation hypothesis, yielding elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces (arXiv 2603.00047). Three empirical challenges prevent direct application. (1) Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) shows safety and capability subspaces are highly entangled, with MSO strongest between useful and safety-specific updates — but MSO operates in parameter space (SVD of weight difference matrices) while α operates in activation space (cross-covariance of activation vectors). These two metric systems have never been connected, creating a measurement schism: the alignment community simultaneously uses parameter-space interventions (null-space gradient projection) and activation-space diagnostics (probing, geometric theory) without knowing if they analyze the same underlying structure. (2) Frontier models are predominantly MoE architectures where safety is governed by sparse expert routing (RASA arXiv 2602.04448, SAFEx arXiv 2506.17368, Sparse Models Sparse Safety arXiv 2602.08621), not global activation subspaces — making the continuous-subspace geometric framework's applicability non-trivial. (3) In agentic tool-use settings, both challenges intensify: text safety does not transfer to tool-call safety (Mind the GAP, arXiv 2602.16943), and the safe controller mapping has inherently higher Lipschitz complexity (Why Does Agentic Safety Fail to Generalize, arXiv 2605.06992). Plaut (arXiv 2603.02229) measured an approximately linear Pareto frontier (R²=0.77, slope −0.83) in agentic DPO on 8B–14B models — but with only two β values, no representation analysis, and no MoE comparison. The geometric framework's author explicitly notes it fails \"for large perturbations, the KL is not quadratic, the representation geometry shifts\" — but this failure boundary has never been quantified.\n\n## Opportunity\n\nFour independent lines of work create a convergence point whose bridges are missing. The Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) provides the formal apparatus — principal angles, elliptic Pareto frontiers, tax rate decomposition — but assumes linear separability, static representations, and dense architectures. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) proves the separability assumption fails via MSO in parameter space, but only in chat on models up to 7B — and operates in a different mathematical space than the geometric theory. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions in activation space, but only in chat on Llama 3 8B. Plaut (arXiv 2603.02229, Mar 2026) discovers a near-linear agentic Pareto frontier, which the geometric theory predicts when α is small — but used only 8B–14B dense models with 2 β values and no representation analysis. The MoE safety literature (RASA arXiv 2602.04448, SAFEx arXiv 2506.17368, Sparse Models Sparse Safety arXiv 2602.08621) establishes that safety operates through routing dynamics — safety-critical experts, routing distribution divergence, expert silencing — meaning MoE safety is fundamentally routing-mediated and may not be capturable by continuous activation-space geometry. This makes MoE a stress test of the geometric framework's foundations. The null-space projection literature (NSPO arXiv 2512.11391, ICLR 2026; OGPSA arXiv 2602.07892) mitigates the tax by projecting safety gradients into capability null spaces — but in parameter space, assuming separable subspaces. If MSO and α_repr do not correspond, then parameter-space interventions and activation-space theory may be analyzing different structures, with direct consequences for intervention design. LoRA rank=1 achieves optimal reasoning-safety tradeoff (arXiv 2507.17075), suggesting safety alignment is intrinsically low-rank and representation probing may suffice to capture relevant structure. AQI (arXiv 2506.13901, EMNLP 2025) demonstrates that latent geometry — cluster divergence metrics applied to safe/unsafe activations — can diagnose alignment quality without generation, validating the general approach of representation-based alignment diagnosis; our work differs by using principal angles (geometric structure parameterizing the Pareto frontier) rather than cluster quality metrics (scalar diagnostic), and by connecting to cross-space correspondence, architecture-specific analysis, and frontier shape prediction.\n\n## Landscape\n\nThe Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) proves the Pareto frontier is an ellipse ΔS = ΔC cos α + sin α √(B² − ΔC²) parameterized by the principal angle α, but is purely theoretical with no empirical validation and acknowledges failure under large perturbations or nonlinear encoding. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) introduces MSO quantifying safety-capability entanglement via SVD overlap matrices; strongest overlap is between useful and safety updates on Llama 2/3.2 and Qwen 2.5 (1B–7B) — chat only, parameter space only, with layer-specific analysis at 70-85 percentile depth. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions with a dominant refusal direction plus interpretable secondary features — chat only, Llama 3 8B, activation space. Safety Training Persists Through Helpfulness Optimization (arXiv 2603.02229, Mar 2026, Plaut) finds an approximately linear Pareto frontier (R²=0.77, slope −0.83) across 180 DPO configurations on Llama 3.1 8B, Qwen 2.5 7B, and Phi 4 14B using ToolEmu (144 tasks); uses only β ∈ {0.05, 0.1}, no representation analysis, no MoE — frontier shape observed but not geometrically explained. The Viscosity of Logic (arXiv 2601.17260, Jan 2026) sweeps DPO β on Mistral-7B and identifies phase transitions at discrete β values near 10⁻², demonstrating that systematic β sweeping reveals nonlinear regime transitions, motivating dense sampling in high-gradient regions. LoRA is All You Need for Safety Alignment of Reasoning LLMs (arXiv 2507.17075) finds rank=1 LoRA achieves optimal reasoning-safety tradeoff, suggesting safety alignment is intrinsically low-rank. AQI (arXiv 2506.13901, EMNLP 2025) uses latent geometry — Xie-Beni, Calinski-Harabasz, Davies-Bouldin, Dunn indices on safe/unsafe activation clusters — to diagnose alignment quality without generation; differs from our approach in using cluster divergence (scalar quality indicator) vs. principal angles (geometric structure parameterizing Pareto frontier shape), and does not address agent/MoE settings or cross-space correspondence. NSPO (arXiv 2512.11391, ICLR 2026) projects safety gradients into the null space of the capability covariance matrix KK⊤ — but assumes separable subspaces. OGPSA (arXiv 2602.07892, Feb 2026) similarly projects safety gradients onto the orthogonal complement of a capability subspace. Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696) shows safety regions are dataset-dependent with low IoU. The Geometry of Alignment Collapse (arXiv 2602.15799) shows alignment concentrates in low-dimensional subspaces with sharp curvature. ShaPO (arXiv 2602.07340) enforces geometry-aware preference optimization via selective geometry control. Sparse Crosscoders (arXiv 2603.05805) provides methods for comparing MoE and dense model representations at small scale, finding MoEs learn fewer but more specific features. The Autonomy Tax (Mar 2026) shows 99% timeout rates from agent safety training. Mind the GAP (arXiv 2602.16943, Feb 2026) demonstrates text-tool safety divergence across 17,420 datapoints. Why Does Agentic Safety Fail to Generalize (arXiv 2605.06992, May 2026) proves the safe controller has higher Lipschitz constant than task execution. RASA (arXiv 2602.04448, Feb 2026) identifies safety-critical experts via Adversarial Activation Discrepancy and shows full-parameter MoE safety fine-tuning creates routing shortcuts — restoring original routing collapses harmlessness by Δ ∈ [−0.38, −0.46]. SAFEx (arXiv 2506.17368) shows disabling 12 of 6,144 experts drops refusal rate 22%. Sparse Models Sparse Safety (arXiv 2602.08621, Feb 2026) introduces RoSais scores: masking 5 routers increases ASR 4× to 0.79. Geometric Routing (arXiv 2604.14434, Apr 2026) demonstrates monosemantic experts with frequency-to-syntax gradient. Grassmannian MoE (arXiv 2602.17798, Feb 2026) provides subspace-manifold routing. Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026) characterizes theoretical tradeoff limits. The Verifier Tax (Mar 2026) and Steering Externalities (Feb 2026) provide further agentic alignment tax evidence. When Safety Geometry Collapses (arXiv 2605.02914, May 2026) demonstrates safety geometry destruction in guard models. The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026) confirms sharp safety degradation in tool-enabled agents. ATBench (arXiv 2604.02022, Apr 2026) provides paired safe/unsafe trajectory construction with 1,000 trajectories across 1,954 tools. OpenAgentSafety (ICLR 2026) provides 350+ executable tasks with rule-based evaluators. Multi-Agent Security Tax (arXiv 2025) documents safety costs in multi-agent settings. No existing work connects parameter-space MSO to activation-space principal angles, measures alignment tax geometry under entanglement-aware metrics in agentic settings, provides geometric explanation for the observed near-linear frontier in agents, or tests the geometric framework's applicability to MoE routing-mediated safety.\n\n## Approach\n\nWe conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agentic tool-use settings, using a 2×2 factorial design: {dense, MoE} × {chat, agent}. Three core contributions: (C1) cross-space metric bridge with metrological implications, (C2) diagnostic dual-estimation test with pre-registered outcome topology, (C3) MoE stress test of geometric framework.\n\n**Model Selection (2 dense + 2 MoE):**\n- Dense: Qwen3-32B (32.8B active, Qwen3 family), Gemma 4 31B (31B, Apache 2.0)\n- MoE: Qwen3-235B-A22B (22B active / 235B total, Qwen3 family), Llama-4-Maverick (17B active / 400B total)\n\nThe Qwen3 dense/MoE pair enables within-family comparison (same training data, tokenizer) — this is the primary apples-to-apples comparison. The cross-family pair (Gemma/Maverick) provides generalizability signal. Active parameter counts differ between dense and MoE (32.8B vs. 22B for Qwen3; 31B vs. 17B cross-family); addressed via FLOP-normalized analysis. Maverick contingency: if DPO memory requirements prove prohibitive (400B total requires reference offloading for DPO), fallback to Qwen3-30B-A3B (30B total / 3.3B active, Qwen3 family), which provides an MoE sparsity gradient (22B vs. 3.3B active) within the same model family.\n\n**Priority tiers:** Tier 1 (must-have): Qwen3-32B + Qwen3-235B-A22B × 2 settings × 16 β = 64 runs. Tier 2 (high-priority): Gemma 4 31B × 2 settings × 16 β = 32 runs. Tier 3 (contingent on resources): Maverick (or fallback) × 2 settings × 16 β = 32 runs.\n\n**Phase 1: Entanglement Geometry & Cross-Space Metric Bridge (wk 1–6)**\n\n*Infrastructure Validation (wk 1–2):* End-to-end pipeline verification on 1–2 β values per model: confirm QLoRA/LoRA-DPO training, activation extraction, evaluation pipeline (tau2-bench, OpenAgentSafety, ATBench, AdvBench). For Maverick, validate reference offloading feasibility; if infeasible, trigger fallback to Qwen3-30B-A3B.\n\n*Trajectory Construction:*\nAgent settings: paired safe/unsafe trajectories from (i) OpenAgentSafety's (ICLR 2026) 350+ executable tasks with rule-based safety evaluators across 8 risk categories; (ii) ATBench's (arXiv 2604.02022) planner-based paired trajectory synthesis with 1,000 trajectories across 1,954 tools. Capability subspace: tau2-bench policy-adherence tasks, activations from successful vs. failed completions. Activations extracted at tool-call decision points following LLM Reasoning as Trajectories (arXiv 2604.05655). Chat baseline: AdvBench/BeaverTails prompts matching the original MSO paper's methodology.\n\n*Entanglement Metrics:*\n(a) Mode Subspace Overlap (MSO): following Safety Subspaces are Not Linearly Distinct (ICLR 2026), computed via SVD overlap matrices. Sensitivity ablation over subspace rank K ∈ {5, 10, 20, 50, 100}.\n(b) Multi-dimensional safety decomposition: following Hidden Dimensions (ICML 2025), identifying dominant refusal direction and orthogonal secondary directions.\n(c) Principal angles via SVD on cross-covariance matrices of activation vectors, yielding α_repr. Spectrum of first 10 principal angles reported (not just leading angle). Layer-wise profiles computed per layer.\n\n*Cross-Space Correspondence (C1) with Metrological Implications:*\nWe test the empirical relationship between MSO (parameter space) and α_repr (activation space) at layer-wise granularity: for each model × setting condition, compute both MSO and α_repr at each layer in the middle-third depth range (~10–15 layers per model), yielding ~80–100 (MSO_layer, α_repr_layer) data points total. Analyze via linear mixed-effects model with MSO_layer as predictor, α_repr_layer as response, and random intercept per model-setting condition. This resolves the statistical power limitation of condition-level analysis (n=8) while respecting the nested structure. The correspondence is non-trivial: weight-space overlap may manifest as activation-space masking, amplification, or rank change without angle reduction. Results determine whether parameter-space interventions (NSPO, OGPSA) and activation-space diagnostics operate on compatible foundations — if MSO and α_repr do not correspond, these two analysis paradigms are not interchangeable, directly impacting alignment intervention design.\n\n*Probing-Based Prediction (C1 application):*\nRegression of condition-level representation measurements (MSO, α_repr, effective rank, routing divergence for MoE) against α_frontier and downstream safety metrics. If predictive, this provides initial evidence that alignment tax severity can be estimated from representation probing (~25 GPU-hr per model) without full DPO sweeps (~80+ GPU-hr per model), addressing the open question posed by the Geometry of the Alignment Tax author.\n\n*Trajectory Construction Sensitivity Ablation:*\n(i) Data source ablation: MSO and α_repr from OpenAgentSafety-only vs. ATBench-only vs. combined. (ii) Token position ablation: extraction at (a) tool-call decision points (default), (b) last token of each agent step, (c) mean-pooling over all step tokens.\n\n**Phase 2: Architecture-Aware MoE Routing Analysis (wk 4–7, overlapping)**\nFor MoE models, three-level decomposition:\n(a) Shared attention layers: analogous to dense-model analysis, providing controlled comparison.\n(b) Per-expert FFN subspaces: safety-critical experts identified via Adversarial Activation Discrepancy (RASA, arXiv 2602.04448). Per-expert α_repr and MSO computed to test whether safety is concentrated in specific experts or distributed.\n(c) Router weight space: routing distribution divergence (KL) between safe/unsafe inputs; RoSais-style router safety importance scoring (Sparse Models Sparse Safety, arXiv 2602.08621).\n\nSupplementary/exploratory: Sparse Crosscoders (arXiv 2603.05805) for feature organization comparison, contingent on scaling feasibility at 30B+ scale (original validation at 5-layer models only). Core MoE conclusions do not depend on crosscoder results.\n\n**Phase 3: Pareto Frontier Mapping & Diagnostic Dual-Estimation Test (wk 6–12)**\n\n*Evaluation Axes:*\n- Safety axis: OpenAgentSafety safety score (agent); AdvBench refusal rate + BeaverTails safety score (chat). Cross-setting control: all agent-trained models also evaluated on AdvBench (shared safety metric across settings).\n- Capability axis: tau2-bench task success rate + OpenAgentSafety task completion rate (agent); MMLU (5-shot) + GSM8K (8-shot) (chat). Pareto frontiers reported per capability metric to verify shape robustness.\n- Within-setting comparison (same evaluation protocol, varying architecture/model) is the primary analysis. Cross-setting comparison (agent vs. chat α) is secondary/suggestive, with metric-induced confounds explicitly discussed.\n\n*Training Protocol:*\n- Primary: LoRA-DPO on all layers, LoRA rank matched on total trainable parameters across architectures.\n- Secondary matching: per-token active trainable parameters (MoE LoRA rank increased to compensate for expert sparsity), testing whether matching strategy affects frontier shape conclusions.\n- MoE-specific ablation: (i) shared-attention-only LoRA, (ii) active-expert-only LoRA (HELLoRA-style). These ablations also serve to address the parameter-matching confound by isolating which model components drive frontier shape.\n- FLOP-normalized analysis: per-model training/inference FLOPs reported; FLOP-normalized Pareto frontiers provided alongside parameter-matched frontiers.\n\n*β Sweep:*\n16 LoRA-DPO β values per model/setting (β ∈ {0.003, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0}), with increased density in the high-gradient region. If pre-study power simulation indicates n=16 insufficient for α < 15° discrimination, increase to 24 β points for Tier 1 models (offset by reducing Tier 3 scope). Phase transitions at discrete β values (The Viscosity of Logic, arXiv 2601.17260) motivate the dense sampling.\n\n*Statistical Approach:*\nBayesian model comparison using PSIS-LOO (Vehtari, Gelman & Gabry, 2017; preferred for small-sample robustness) and WAIC for three frontier models: (i) elliptic (α, B), (ii) linear (slope, intercept), (iii) piecewise-linear. Report ΔELPD ± SE(ΔELPD); if |ΔELPD| < SE, honestly reported as inconclusive. Pre-study power simulation: synthetic frontiers at α ∈ {5°, 10°, 15°, 20°, 45°} with realistic noise, testing PSIS-LOO discrimination at n=16 and n=24. Leave-one-out sensitivity: checking whether removing any single β point changes model ranking. Supplementary: local curvature analysis (second-order finite differences along the frontier) to detect deviation from linearity even when global shape discrimination is inconclusive.\n\n*Small-α Fallback:* If most conditions yield α < 10° and PSIS-LOO is inconclusive for elliptic vs. linear, C2's contribution reframes as \"quantifying α's upper bound\" — empirically demonstrating that entanglement is sufficient to collapse the frontier to near-linearity (α < X° with 95% credible interval), which itself validates the geometric theory's prediction that high entanglement linearizes the tax.\n\n*Diagnostic Dual-Estimation Test (C2) with Outcome Topology:*\nα_repr (Phase 1) vs. α_frontier (elliptic fit) compared via random-effects meta-analysis: compute (α_repr − α_frontier) for each of the 8 conditions (with uncertainty from bootstrap for α_repr and posterior for α_frontier), fit random-effects model testing whether the population mean difference deviates from 0. This replaces arbitrary counting thresholds with a formal statistical test of systematic divergence.\n\nPre-registered outcome topology — the 2×2 structure ({dense, MoE} × {chat, agent}) yields four interpretive patterns:\n- Dense agree + MoE diverge → routing violates continuous-subspace assumption (C3 confirmed); activation-space geometry remains valid for dense models but breaks for MoE\n- Chat agree + agent diverge → agentic complexity exceeds linear representation assumption; standard geometric framework applies in chat but not in tool-use settings\n- Both diverge → geometric framework fundamentally inadequate under real entanglement levels; the linear representation hypothesis is a poor approximation for safety-capability geometry\n- Both agree → framework is surprisingly robust despite entanglement; principal angle theory extends beyond its stated assumptions\n\nEach pattern has distinct consequences for alignment intervention design (parameter-space projection vs. routing-aware methods vs. setting-specific approaches), ensuring the paper produces actionable findings regardless of outcome.\n\n**Scope note:** We exclude intervention phases (entanglement-adapted OGPSA or NSPO). We focus on rigorous measurement and geometric explanation.\n\n## Resource Estimate\n\n**GPU hours (distinguishing wall-clock from GPU-hours):**\n- Infrastructure validation (wk 1–2): ~100 GPU-hr (1–2 β × 4 models × 2 settings, quick runs)\n- Phase 1 activation extraction: 4 models × 2 settings × ~25 hr on 4–8×H100 ≈ 400–600 GPU-hr\n- Phase 2 MoE routing analysis: 2 models × 60 hr on 8×H100 ≈ 960 GPU-hr\n- Phase 3 Tier 1 sweep (Qwen3 pair): 2 models × 2 settings × 16 β × ~5 hr on 4×H100 (dense) / 4–8×H100 (MoE QLoRA) ≈ 640–1,280 GPU-hr\n- Phase 3 Tier 2 sweep (Gemma): 1 model × 2 settings × 16 β × ~5 hr on 4×H100 ≈ 640 GPU-hr\n- Phase 3 Tier 3 sweep (Maverick/fallback): 1 model × 2 settings × 16 β × ~5 hr on 8×H100 (with ref offloading) ≈ 1,280 GPU-hr\n- Phase 3 MoE ablation: 2 models × 2 settings × 8 β × ~5 hr on 4–8×H100 ≈ 640–1,280 GPU-hr\n- Agent evaluation (tau2-bench + OpenAgentSafety + ATBench + AdvBench bridging): ~300 GPU-hr\n- Buffer (debugging, reruns, power-contingent β expansion): ~500 GPU-hr\n\n**Total: ~3,500–5,000 GPU-hr** (lower bound = QLoRA feasible + Tier 3 deferred; upper bound = 8×H100 for all MoE + full Tier 3).\n**Timeline:** 16 weeks (wk 1–2 infrastructure validation + trajectory generation + power simulation; wk 2–6 entanglement geometry extraction; wk 4–7 MoE routing analysis; wk 6–12 Pareto sweeps + ablations; wk 13–14 analysis + regression; wk 15–16 writing).\n**Estimated GPU cost:** $10,500–$15,000 at ~$3.00/GPU-hr average.\n**Human-in-loop variant:** Claude-assisted probe code and analysis; API cost ~$700 (Sonnet 4.6). **Auto-research variant:** Opus 4.7; API cost ~$2,800; timeline compressible to ~11 weeks.\n\n## Inspired By\n\nField guide Section 4.1 (pass@1 vs. production gap) + the convergent pattern: (a) the formal alignment tax geometry needs entanglement-robust metrics for empirical validation, (b) Plaut's near-linear agentic frontier needs geometric explanation (our framework predicts: high entanglement → small α → near-linear ellipse), (c) the MoE safety routing literature needs geometric formalization, and (d) null-space projection methods (NSPO, OGPSA) need entanglement-aware adaptation. These four bridges converge in one study.\n\n## Target Venues\n\n- ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026 — primary target, 16-week execution from May 19 start)\n- AAAI 2027 (abstract Jul 26, full paper Aug 2, 2026 — stretch target for dense-model-only subset if Tier 1 results strong by week 10)\n- ICML 2027 (estimated Jan 29, 2027 — fallback with complete results including all tiers)\n\n## Key References\n\n- What Is the Geometry of the Alignment Tax? (arXiv 2603.00047, Mar 2026)\n- Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study (arXiv 2505.14185, ICLR 2026)\n- The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025)\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv 2603.02229, Mar 2026, Plaut)\n- The Viscosity of Logic: Phase Transitions in DPO (arXiv 2601.17260, Jan 2026)\n- LoRA is All You Need for Safety Alignment of Reasoning LLMs (arXiv 2507.17075)\n- Alignment Quality Index (arXiv 2506.13901, EMNLP 2025)\n- Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization [NSPO] (arXiv 2512.11391, ICLR 2026)\n- Safety Alignment as Continual Learning via Orthogonal Gradient Projection [OGPSA] (arXiv 2602.07892, Feb 2026)\n- The Autonomy Tax: Defense Training Breaks LLM Agents (arXiv 2026)\n- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety (arXiv 2602.16943, Feb 2026)\n- Why Does Agentic Safety Fail to Generalize Across Tasks? (arXiv 2605.06992, May 2026)\n- RASA: Routing-Aware Safety Alignment for MoE Models (arXiv 2602.04448, Feb 2026)\n- SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs (arXiv 2506.17368)\n- Sparse Models, Sparse Safety (arXiv 2602.08621, Feb 2026)\n- Geometric Routing Enables Causal Expert Control in MoE (arXiv 2604.14434, Apr 2026)\n- Grassmannian MoE (arXiv 2602.17798, Feb 2026)\n- Sparse Crosscoders for diffing MoEs and Dense models (arXiv 2603.05805, Mar 2026)\n- Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696, Feb 2026)\n- The Geometry of Alignment Collapse (arXiv 2602.15799, Feb 2026)\n- ShaPO: Selective Geometry Control for Safety Alignment (arXiv 2602.07340, Feb 2026)\n- Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026)\n- Steering Externalities (arXiv 2026)\n- The Verifier Tax (arXiv 2026)\n- When Safety Geometry Collapses (arXiv 2605.02914, May 2026)\n- The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026)\n- OpenAgentSafety (ICLR 2026)\n- ATBench (arXiv 2604.02022, Apr 2026)\n- Multi-Agent Security Tax (arXiv 2025)\n- LLM Reasoning as Trajectories (arXiv 2604.05655)\n- Vehtari, Gelman & Gabry (2017), Practical Bayesian Model Evaluation Using LOO-CV and WAIC, Statistics and Computing 27(5)"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:43:57.376Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:43:57.376Z",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T04:43:57.389Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient literature context. Let me compile the comprehensive evaluation.

```
【阶段】: Triage

【领域调研】:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026): 本 proposal 的核心理论基础。纯理论工作，证明 Pareto 前沿是由 principal angle α 参数化的椭圆，但无任何实验验证，作者自述在大扰动下失效。该框架是全新且未经验证的——这既是机会也是风险。
- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026): 本 proposal 的另一核心支柱。引入 MSO 度量参数空间中安全-能力子空间的纠缠。仅在 chat 场景、1B-7B 模型上验证。Proposal 正确地指出 MSO（参数空间）与 α（激活空间）之间从未建立联系。
- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025): 揭示安全方向在激活空间中是多维正交的，有主导拒绝方向和可解释的次级方向。仅 Llama 3 8B chat 场景。Proposal 拟将此扩展到 agent 和 MoE。
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (arXiv, Mar 2026, Plaut): 发现 agentic DPO 的近线性 Pareto 前沿（R²=0.77）。仅用 2 个 β 值、8B-14B dense 模型、无表征分析、无 MoE。Proposal 的核心动机之一是几何地解释这一观察。
- [NSPO: Null-Space Constrained Policy Optimization](https://arxiv.org/abs/2512.11391) (ICLR 2026): 将安全梯度投影到能力空间的零空间。假设子空间可分离——若 MSO 与 α 不对应，此方法的理论基础存疑。Proposal 的 C1 对此有直接意义。
- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448) (arXiv, Feb 2026): 识别安全关键专家，证明 MoE 安全通过路由动态实现。Proposal 的 C3（MoE 压力测试）直接建立在此发现之上。
- [AQI: Alignment Quality Index](https://aclanthology.org/2025.emnlp-main.145/) (EMNLP 2025): 用聚类散度度量潜在几何来诊断对齐质量。与本 proposal 相关但不同——AQI 用标量聚类指标，proposal 用 principal angles 参数化前沿形状。
- [OGPSA: Safety Alignment via Orthogonal Gradient Projection](https://arxiv.org/abs/2602.07892) (Feb 2026): 另一个假设子空间可分离的参数空间方法。
- [SAFEx](https://arxiv.org/abs/2506.17368), [Sparse Models Sparse Safety](https://arxiv.org/abs/2602.08621): 证明 MoE 中少量专家承载安全功能（禁用 12/6144 专家降低拒绝率 22%），进一步支持 MoE 安全是路由介导的论点。

- **调研总结**: 对齐税的几何理论（2603.00047）是 2026 年初的全新理论框架，尚无实证验证。MSO、principal angles、MoE routing safety 三条研究线独立发展，确实没有工作尝试连接它们。Proposal 识别出了一个**真实的**、**未被填补的**交叉点。但该交叉点主要是"测量/诊断"性质——用现有工具在新设定下测量——而非提出新方法。

【整体印象】:
作为审稿人，我的第一反应是：这是一份在文献综述和实验设计上**异常详尽**的 proposal，展示了对领域的深度理解和严谨的方法论规划。它正确识别了一个真实的研究空白——参数空间纠缠度量（MSO）与激活空间几何（principal angle α）之间从未建立对应关系，几何框架也从未在 MoE 或 agentic 设定下被验证。

然而，我的核心犹豫是：**这本质上是一项纯测量/表征研究**，核心操作是将已有的分析工具（MSO、SVD、DPO sweep）应用到新的组合设定中。三个贡献（C1 跨空间桥梁、C2 诊断双估计、C3 MoE 压力测试）中，方法论创新有限，主要价值在于"首次在这些条件下测量"。此外，proposal **严重过载**——三个独立贡献各需大量实验，压入一篇论文中每个都可能处理不够深入。

我会倾向给一个 **borderline / weak reject**，除非实验结果揭示出显著出乎意料的发现。

【核心贡献】:
1. **C1（跨空间度量桥梁）**: 首次建立 MSO（参数空间纠缠）与 α_repr（激活空间几何）的层级对应关系。这是最具原创性的贡献，对判断参数空间干预（NSPO, OGPSA）与激活空间诊断是否操作在兼容基础上有直接意义。但其价值高度依赖于发现的性质——若二者强相关，解释力有限（可能由共因混淆）；若不相关，也难以区分是根本不兼容还是测量方法差异所致。
2. **C2（诊断双估计测试）**: 比较 α_repr 与 α_frontier，配合 2×2 预注册结果拓扑。实验设计理念优秀（确保任何结果都可解释），但本质上是在测试一个全新且未验证的理论框架——验证或否证一个 March 2026 的纯理论论文的实践价值取决于该理论的影响力。
3. **C3（MoE 压力测试）**: 测试连续子空间几何假设是否适用于路由介导的 MoE 安全。方向合理，但预期结果（MoE 中几何框架失效）较为可预见。

对领域的价值：**中等**。如果该几何框架成为后续工作的重要基础，这项实证验证就很有价值。但该框架本身尚未被社区广泛采纳，测量性工作的即时影响力有限。

【方法合理性】:
方法总体合理，但有若干关切：

1. **跨空间对应（C1）的方法论脆弱性**：用混合效应模型在 ~80-100 个层级数据点上拟合 MSO 与 α_repr 的对应关系，但两者可能因共同的混淆因素（如层深度效应）而产生虚假相关。仅有相关性不足以证明"可兼容的基础"。
2. **前沿形状判别**：Proposal 自身承认若 α < 10°，PSIS-LOO 可能无法区分椭圆与线性模型。鉴于高纠缠（MSO 文献强烈暗示）的预期，大多数条件可能确实产生小 α，使 C2 的核心判别变得不可行。
3. **参数匹配问题**：Dense（32.8B）vs. MoE（22B active）的比较存在固有混淆，FLOP 归一化分析只能部分缓解。
4. **更简单的替代方案**：C1 可以不依赖 DPO sweep，直接在 base/aligned/harmful 模型上提取两个空间的度量进行对比，大幅减少实验复杂度。C3 的核心发现（MoE 中几何框架失效）可能通过更简单的案例研究就能得出。

**是否有更简单的方案？** 是的。该 proposal 将过多维度压入一个实验中。一个更聚焦的版本可以：(a) 只做 C1（跨空间桥梁）在多个模型上，或 (b) 只做 C3（MoE 压力测试）配合前沿映射。当前方案试图同时推进三个前沿，每个都可能因实验页面限制而变得单薄。

【5 维度打分】:
  1. 研究问题: **中偏强** — 识别出的研究空白是真实的：参数空间与激活空间安全度量的断裂、几何框架在 MoE/agent 下的适用性，均为该领域尚未回答的有意义问题。但这些问题的"紧迫性"和"影响力"有限——解答它们主要服务于理论完备性，对实践（如改进安全对齐方法）的直接启示不明确。Plaut 的线性前沿缺乏几何解释是一个好切入点。
  
  2. 方法与创新: **中偏弱** — 三个贡献均是将已有分析工具（MSO、SVD principal angles、DPO sweep、Bayesian 模型比较）应用于新组合。方法论本身无创新——MSO 直接沿用 ICLR 2026 论文，principal angles 是标准线性代数，前沿拟合用标准贝叶斯方法。预注册结果拓扑是一个亮点（受 [Hidden Dimensions, ICML 2025] 的多维分析启发但走了不同方向），但不构成方法论贡献。与 AQI (EMNLP 2025) 相比，AQI 至少提出了新的组合度量（XBI, CHI, DBI, DI 的整合），而本 proposal 的"桥梁"主要是在两个已有度量之间跑相关。
  
  3. 实验设计: **强** — 这是 proposal 最大的亮点。2×2 因子设计干净；16 β 值密集扫描（相比 Plaut 的 2 个β）充分覆盖参数空间；优先级分层（Tier 1/2/3）现实且合理；灵敏度消融（子空间秩 K、数据源、token 位置）全面；统计方法（PSIS-LOO、WAIC、mixed-effects）严谨；预注册结果拓扑确保任何结果都可解释；MoE 消融（shared-attention-only、active-expert-only LoRA）针对性强。后备方案（Maverick 降级、小 α 重新定义贡献）体现务实性。这是一份**远超平均投稿**的实验设计。
  
  4. 可行性: **中** — 3,500-5,000 GPU-hours、$10,500-$15,000 不算天文数字但也不小。主要风险点：(a) 400B Maverick 的 DPO 训练可行性存疑（proposal 有后备方案）；(b) 16 周时间线紧张——Phase 1-3 有重叠但 wk 1-2 的 infra validation 可能出意外；(c) 三个评估框架（OpenAgentSafety、ATBench、tau2-bench）加 AdvBench 的整合工程量大；(d) 结果可能因多种原因模糊不清（小 α、高噪声、不同度量的不一致）。Tier 制度和后备方案是加分项。
  
  5. 写作与呈现: **中** — Proposal 本身写得信息密度极高、文献覆盖全面、逻辑链条完整。但**过度工程化**是突出问题——proposal 读起来像是在试图覆盖所有可能的质疑（token 位置消融、数据源消融、参数匹配消融、FLOP 归一化、两种统计方法、后备方案...），反而模糊了核心叙事。一个好论文需要一个清晰的 take-home message——"我们发现了 X，这改变了你对 Y 的理解"——而这份 proposal 的 take-home message 分散在三个 contributions 中。8 页正文可能装不下。

【概率估计】: [20% - 35%] 中位 27%

【估计理由】: 
**上拉因素**: (1) 识别出真实的研究空白，问题有意义；(2) 实验设计极为详尽，远超同类工作的方法论严谨性，这本身是显著加分项；(3) 预注册结果拓扑框架在方法论上值得肯定；(4) 领域高度时效性——2026年初的多篇核心论文刚出，连接它们有自然的新鲜感；(5) 对 Plaut 线性前沿的几何解释如果成立，是有吸引力的发现。

**下拉因素**: (1) **纯测量/表征研究，无方法论创新**——这在顶会评审中通常被视为"nice characterization but limited contribution"，除非发现非常意外；(2) **严重过载**——三个独立贡献挤入一篇论文，每个可能处理单薄，8 页正文难以充分展开；(3) **多项预期发现较为平凡**——高纠缠环境下几何框架在 MoE 中失效、agent 比 chat 纠缠更高——这些是多数研究者的默认预期，确认它们的价值有限；(4) **C1 跨空间桥梁的因果推断力弱**——层级相关可能由混淆因素驱动；(5) **所验证的理论框架（2603.00047）本身太新且影响力未知**——如果该框架最终未被社区采纳，验证工作的价值随之缩水。

中位估计 27%，落在"整体合格、有实质贡献，但缺乏突出亮点"的区间。若实验产出出乎意料的发现（如 MSO 与 α 强烈不对应，或 MoE 中几何框架意外成立），概率可升至 35%+。若发现平凡且叙事不聚焦，概率可能跌至 20% 以下。

【主要风险】:
1. **"So what?" 问题**: 审稿人可能认为这是一项勤勉但缺乏 actionable insight 的表征研究——"你确认了几何框架在 MoE 中不适用，那然后呢？" 缺少干预阶段（proposal 明确排除了）意味着没有展示这些测量如何转化为更好的对齐方法。
2. **叙事分散/过载**: 三个独立贡献（跨空间桥梁 + 诊断双估计 + MoE 压力测试）难以在 8 页内讲一个统一的、有力的故事。审稿人可能觉得每个贡献都只触及表面，建议拆分为多篇论文。

【实施评估】:
  - 计算资源: 3,500-5,000 GPU-hours (H100)，$10,500-$15,000，属于中高规模实证研究
  - 数据需求: 使用已有数据集（OpenAgentSafety, ATBench, AdvBench, BeaverTails, tau2-bench），无需构建新数据集
  - 人工介入: 较低——主要是工程和分析自动化，无需人工标注
  - 训练需求: 128 个 LoRA-DPO 训练 run（Tier 1+2），最多 192 个（含 Tier 3）+ MoE 消融，每次 ~5 hr on 4-8×H100
  - 新 Benchmark: 否——使用已有 benchmark
  - 预估周期: 16 周（proposal 自述），但考虑 infra 调试和意外情况，实际可能 18-20 周
```

Sources:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)
- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185)
- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674)
- [Safety Training Persists Through Helpfulness Optimization](https://arxiv.org/abs/2603.02229)
- [NSPO: Null-Space Constrained Policy Optimization](https://arxiv.org/abs/2512.11391)
- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448)
- [AQI: Alignment Quality Index](https://aclanthology.org/2025.emnlp-main.145/)
- [OGPSA: Safety Alignment via Orthogonal Gradient Projection](https://arxiv.org/abs/2602.07892)
- [SAFEx: MoE Vulnerabilities](https://arxiv.org/abs/2506.17368)
- [Sparse Models Sparse Safety](https://arxiv.org/abs/2602.08621)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [What Is the Geometry of the Alignment Tax? (arXiv 2603.00047)](https://arxiv.org/abs/2603.00047) (Mar 2026): The theoretical backbone of this proposal. Proves Pareto frontier is an ellipse parameterized by principal angle α. Purely theoretical — no empirical validation. Explicitly acknowledges failure under large perturbations / nonlinear encoding. This proposal's C2 directly attempts to empirically validate and stress-test this framework.
- [Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185)](https://arxiv.org/abs/2505.14185) (ICLR 2026): Introduces MSO (parameter-space entanglement metric). Tested only on ≤7B models, chat-only setting. This proposal's C1 attempts to bridge MSO to activation-space principal angles — a gap this paper leaves entirely open.
- [The Hidden Dimensions of LLM Alignment (arXiv 2502.09674)](https://arxiv.org/abs/2502.09674) (ICML 2025): Multi-dimensional orthogonal safety directions in activation space, but only on Llama 3 8B in chat. No connection to parameter-space metrics or MoE architectures.
- [Safety Training Persists Through Helpfulness Optimization — Plaut (arXiv 2603.02229)](https://arxiv.org/abs/2603.02229) (Mar 2026): Finds near-linear Pareto frontier (R²=0.77) in agentic DPO. Only 2 β values, ≤14B dense models, no representation analysis, no geometric explanation. This proposal aims to explain this observation geometrically.
- [NSPO (arXiv 2512.11391)](https://arxiv.org/abs/2512.11391) (ICLR 2026): Projects safety gradients into null space of capability covariance — parameter-space intervention assuming separable subspaces. If MSO–α_repr don't correspond, NSPO's foundational assumption is challenged.
- [RASA (arXiv 2602.04448)](https://arxiv.org/abs/2602.04448) (Feb 2026): Identifies safety-critical experts via routing analysis in MoE. Directly motivates C3 — safety in MoE is routing-mediated, making continuous-subspace geometry potentially inapplicable.
- [AQI (arXiv 2506.13901)](https://arxiv.org/abs/2506.13901) (EMNLP 2025): Uses latent geometry (cluster divergence) to diagnose alignment quality. Related but methodologically distinct — cluster metrics vs. principal angles. No cross-space, MoE, or agent analysis.
- 调研总结: The proposal sits at a genuine convergence point where 4+ independent research threads (geometric alignment tax theory, parameter-space entanglement, MoE routing safety, agentic safety divergence) have left clear bridging gaps. **No existing work connects parameter-space MSO to activation-space principal angles, measures alignment geometry under entanglement in agentic settings, or tests the geometric framework on MoE architectures.** The novelty claim is well-supported.

【整体印象】:
作为审稿人，我的第一反应是：这是一份极其深思熟虑、文献调研无可挑剔的 proposal，识别了一个真实且重要的理论空白。但随之而来的直觉反应是——**这篇论文试图在一篇 paper 里做太多事情**。三个 contribution（C1 跨空间桥梁、C2 诊断性双估计检验、C3 MoE 压力测试），4个模型 × 2个设置 × 16个 β 值 = 128+ 次 DPO 训练，加上 MoE 三层分解、多种 ablation、Bayesian 模型比较……这不是一篇 8 页论文能装下的。

更根本的是：**这是一篇纯测量/表征论文，没有提出任何干预方法**。proposal 明确声明 "We exclude intervention phases"。这意味着它的 contribution 完全依赖于测量本身的价值。虽然好的测量论文确实存在（例如 MSO 论文本身就是），但在这种情况下，花费 3,500-5,000 GPU-hours 做一个表征研究，审稿人会问 "so what?" — 这些测量结果能指导什么具体行动？

我的倾向是 **borderline reject / weak accept**，取决于执行质量和写作清晰度。

【核心贡献】:
核心贡献是三方面的：
1. **C1（最有价值）**: 首次建立 parameter-space MSO 与 activation-space α_repr 的跨空间对应关系。这是一个真实的测量学空白——如果这两个度量不对应，那么 NSPO/OGPSA 等 parameter-space 干预方法和 activation-space 诊断工具实际上在分析不同的结构，对 alignment 干预设计有直接影响。
2. **C2（方法论创新）**: Pre-registered outcome topology 是一个聪明的设计选择——无论结果如何，论文都有信息价值。但这更像是一个好的实验设计原则，不是独立的 contribution。
3. **C3（及时性强）**: MoE 架构已成为 frontier model 的主流，测试几何框架在 routing-mediated safety 下的适用性是重要的。

总体而言，C1 对领域有中等偏高价值——如果执行得好，它能回答 "parameter-space 和 activation-space 的 alignment 分析是否看的是同一个东西" 这个关键问题。但价值是条件性的：如果答案是 "它们大致对应"，那信息增量有限；如果不对应，信息量更大但需要后续工作来利用这个发现。

【方法合理性】:
方法论整体合理但有几个关键问题：

1. **Layer-wise mixed-effects model 的统计有效性**：用层级数据点（~80-100 个）来弥补条件级分析（n=8）的统计力不足，但层间数据有强自相关性（相邻层的 MSO 和 α_repr 高度相关），违反了混合效应模型的独立性假设。如果不做适当的空间自相关校正，p 值可能严重膨胀。

2. **Elliptic vs. Linear 判别**：这是 C2 的核心，但如果 α 确实很小（如 <10°），椭圆和直线在统计上几乎不可区分。proposal 承认了这一点并设计了 "small-α fallback"，但 fallback 的 contribution 明显弱于原始假设——"证明 α 确实很小" 基本等于确认已有的猜测。

3. **Dense-MoE 对比的 confound**: 即使在 Qwen3 family 内，dense (32.8B) vs. MoE (22B active) 的 active parameter count 差异很大。FLOP-normalized 分析能部分缓解，但不能完全消除架构差异以外的 confound。

4. **更简单的替代方案**：C1 的跨空间对应可以在更小规模（2-3 模型 × 8 β 值）上先验证，然后再扩展。目前的设计把验证性分析和大规模系统性测量混在一起，不够高效。

【5 维度打分】:

1. 研究问题: 【强】— 跨空间度量对应、MoE 几何框架适用性、agentic 设置下的 alignment geometry 都是真实且重要的开放问题。四条独立研究线的汇聚点识别得很准确，文献覆盖几乎堪称详尽。Plaut 的近线性 frontier 缺乏几何解释、NSPO/OGPSA 假设 parameter-space 和 activation-space 可互换但缺乏验证——这些都是经得起推敲的 research gap。

2. 方法与创新: 【中】— 跨空间桥梁（C1）在概念上新颖，但方法本身是对现有工具（MSO、principal angle SVD）的组合应用，不涉及新的数学工具或算法。Pre-registered outcome topology（C2）是好的实验设计但不是方法创新。与 [AQI (EMNLP 2025)](https://arxiv.org/abs/2506.13901) 相比，本文在方法层面的创新更多体现在"桥接"而非"发明"。与 [Hidden Dimensions (ICML 2025)](https://arxiv.org/abs/2502.09674) 相比，本文的 activation-space 分析本质上是扩展而非突破。核心方法论担忧是层级混合效应模型在处理自相关数据时的统计有效性。

3. 实验设计: 【强】— 这是 proposal 最突出的亮点。2×2 factorial design 合理，16-point β sweep 远超 Plaut 的 2 β 值，Bayesian model comparison (PSIS-LOO + WAIC) 比简单的 curve fitting 严谨得多。敏感性 ablation（数据源、token 位置、subspace rank K）覆盖全面。Priority tier 系统和 Maverick fallback 显示了实际执行智慧。与 [Plaut (arXiv 2603.02229)](https://arxiv.org/abs/2603.02229) 的实验规模（2 β, 3 models, no representation analysis）相比，这是量级提升。与 [MSO 论文 (ICLR 2026)](https://arxiv.org/abs/2505.14185) 的 ≤7B chat-only 范围相比，本文在 scale 和 coverage 上有实质性扩展。唯一的短板是有效样本量：8 个条件对 meta-analytic agreement testing 来说偏少，层级混合效应模型是否能真正解决这个问题存疑。

4. 可行性: 【中】— 3,500-5,000 GPU-hours、$10,500-$15,000 GPU cost 是可负担的（对有资源的实验室而言），但 16 周的时间线在 128+ DPO 训练、大规模 activation 提取、MoE 三层分解等工作面前非常紧张。Maverick (400B total) 的 DPO 训练可能在实际操作中比预期更难——reference offloading for 400B 参数的 MoE 在 8×H100 上的可行性存在不确定性。如果 Tier 3 被迫降级到 Qwen3-30B-A3B (3.3B active)，与 dense 模型 (32B) 的 active parameter 差距扩大到 ~10x，可比性进一步削弱。写作方面，把三个 contribution + 完整的实验结果 + 所有 ablation 压缩到 8 页正文 + appendix 是一个极大的挑战。

5. 写作与呈现: 【中】— proposal 的文献覆盖和逻辑链条是其强项，但也恰恰暴露了潜在的写作问题：当前 proposal 已经极其密集，术语堆叠严重（MSO、α_repr、α_frontier、PSIS-LOO、WAIC、RoSais、FLOP-normalized、HELLoRA-style 等），如果论文也是这种密度，审稿人可能在理解核心贡献之前就失去耐心。标题 "Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings" 有 15 个词，试图把所有关键词塞进去，反而模糊了焦点。

【概率估计】: [20% - 35%] 中位 27%

【估计理由】:
推理过程：

**向上推的因素（+）**：
- 研究问题真实且重要，文献空白验证充分（+）
- 实验设计在方法论上非常严谨，远超该领域同类工作（+）
- Pre-registered outcome topology 确保论文在任何结果下都有贡献（+）
- 话题极度 timely——alignment tax、MoE safety、agentic safety 都是 2026 热点（+）
- 跨空间桥梁（C1）对 alignment intervention 设计有实际意义（+）

**向下拉的因素（−）**：
- **纯测量论文没有干预方法**：在 EMNLP 这样的会议上，"we measured X and found Y" 的贡献往往被认为不如 "we found problem X and solved it with method Y"。三个 contribution 都是测量/诊断性质的，缺乏 actionable output（−−）
- **范围过大**：三个 contribution 每一个都可以是独立论文的核心。把它们全塞进一篇 8 页论文，每个都难以充分展开（−−）
- **统计力担忧**：核心 claim（C2 的 α_repr–α_frontier 一致性/分歧）在有效样本量 n=8 的条件下，即使用层级混合效应模型补救，也面临自相关数据的统计有效性质疑（−）
- **Elliptic vs. Linear 判别的固有困难**：如果 α 确实很小，小样本下的 Bayesian 模型比较可能得出不确定结论，核心 story 变成 "α 的上界估计"，contribution 明显减弱（−）
- **写作挑战极大**：proposal 的密度和复杂度暗示最终论文可能难以让不在这个精确交叉领域的审稿人快速理解（−）
- **执行风险**：MoE 训练复杂度、400B 模型的 reference offloading、16 周 timeline 对应的工作量——实际执行中任何一个环节出问题都可能导致需要显著缩减范围（−）

综合判断：这是一个识别能力极强的研究者写的 proposal，问题发现精准、实验设计严谨，但在 "做什么" 的选择上过于贪心，"贡献什么" 的层面偏向测量而非解决问题。在 EMNLP 2026 的竞争环境中，这种 profile 的论文通常落在 borderline 区域——如果执行完美、写作精炼、结果清晰，有望进入 25-35% 的 accept 区间；如果任何一个方面出问题，容易滑入 20-25% 的 reject 区间。中位估计 27%。

【主要风险】:
1. **"纯测量无干预" 的 contribution 定位**：审稿人可能认为 3,500-5,000 GPU-hours 的纯表征研究缺乏足够的 actionable insight。如果结果是 "MSO 和 α_repr 大致对应"，信息增量有限；如果不对应，没有后续解决方案，贡献感不足。在 EMNLP 的竞争环境中，measurement-only paper 需要极高的执行质量和结果的 surprising 程度才能获得 accept。
2. **范围膨胀导致的深度不足**：三个 contribution 在 8 页内可能每个都只能浅尝辄止。特别是 C3（MoE 压力测试）涉及三层分解（shared attention、per-expert FFN、router weights），如果不能充分展开，会被视为 "incomplete analysis"。审稿人可能建议 "拆成 2-3 篇更聚焦的论文"。

【实施评估】:
  - 计算资源: 3,500–5,000 GPU-hr (4–8×H100)，$10,500–$15,000。对中等规模实验室可行，但不轻松。
  - 数据需求: 依赖已有 benchmark（OpenAgentSafety、ATBench、AdvBench、BeaverTails、tau2-bench）。无需自建数据集，降低了风险。
  - 人工介入: 相对低——主要是 pipeline 搭建和结果分析。Claude-assisted 自动化降低了人工成本。
  - 训练需求: 大量 LoRA-DPO 训练（128+ runs），含 MoE 模型的 QLoRA 训练。MoE 训练（尤其 400B Maverick）的工程复杂度是主要风险点。
  - 新 Benchmark: 不需要。完全使用已有 benchmark。
  - 预估周期: 16 周（紧张但理论上可行）。实际可能需要 18-20 周，考虑到 MoE 训练的工程调试和可能的 Tier 3 降级。
```

Sources:
- [What Is the Geometry of the Alignment Tax? (arXiv 2603.00047)](https://arxiv.org/abs/2603.00047)
- [Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185)](https://arxiv.org/abs/2505.14185)
- [The Hidden Dimensions of LLM Alignment (arXiv 2502.09674)](https://arxiv.org/abs/2502.09674)
- [Safety Training Persists Through Helpfulness Optimization — Plaut (arXiv 2603.02229)](https://arxiv.org/abs/2603.02229)
- [NSPO (arXiv 2512.11391)](https://arxiv.org/abs/2512.11391)
- [RASA (arXiv 2602.04448)](https://arxiv.org/abs/2602.04448)
- [AQI (arXiv 2506.13901)](https://arxiv.org/abs/2506.13901)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

```
【阶段】: Triage

【领域调研】:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026): The theoretical foundation this proposal builds on. Purely theoretical — proves Pareto frontier is an ellipse parameterized by principal angle α. Explicitly notes limitations under large perturbations and nonlinear encoding. No empirical validation exists yet, which is the gap this proposal targets.
- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026): Introduces MSO in parameter space; shows safety-capability subspaces are highly entangled on Llama 2/3.2 and Qwen 2.5 (1B–7B), chat only. Core tool for this proposal's C1 contribution. Confirmed real and accurately described.
- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025): Multi-dimensional orthogonal safety directions in activation space on Llama 3 8B. Chat only. Provides the activation-space methodology for principal angle extraction. Accurately cited.
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (Plaut, Mar 2026): Observes near-linear Pareto frontier (R²=0.77) in agentic DPO on 8B–14B dense models with only 2 β values. No representation analysis, no MoE. This is the key empirical observation the proposal aims to geometrically explain.
- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448) (Feb 2026): Shows safety in MoE is routing-mediated; full-parameter fine-tuning creates routing shortcuts. Restoring original routing collapses harmlessness by Δ∈[−0.38, −0.46]. Key evidence for C3.
- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621) (Feb 2026): RoSais scores show masking 5 routers increases ASR 4× to 0.79. Further evidence that MoE safety is structurally different from dense safety.
- [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026): Null-space projection method that assumes separable subspaces. This proposal argues if MSO and α_repr don't correspond, NSPO-like methods and activation-space diagnostics may be analyzing different structures.
- [The Viscosity of Logic](https://arxiv.org/abs/2601.17260) (Jan 2026): Phase transitions in DPO β sweeps on 7B models. Motivates the dense β sampling design. Architecture-specific responses found (sharp in Mistral, smooth in Qwen).
- [AQI](https://aclanthology.org/2025.emnlp-main.145/) (EMNLP 2025): Uses cluster divergence metrics on safe/unsafe activations for alignment diagnosis without generation. Most directly related prior work using representation geometry for alignment quality. Differs in using cluster quality (scalar) vs. principal angles (structural).
- 调研总结: The gap identification is legitimate — no prior work connects parameter-space MSO to activation-space principal angles, tests the geometric framework on MoE architectures, or provides geometric explanation for Plaut's near-linear agentic frontier. However, this is an extremely crowded and fast-moving area (20+ papers in 3 months), and the proposal's contribution is fundamentally characterization/measurement rather than a new method or intervention.

【整体印象】:
如果我是审稿人，第一反应是：这是一份极其 well-researched 的 proposal，文献调研几乎无可挑剔，实验设计也非常严谨（pre-registered outcome topology、Bayesian model comparison、分层优先级）。但随之而来的第二反应是：这到底在贡献什么？三个 contributions 加在一起构成的是一个大型 empirical characterization study，但缺乏 actionable 的方法论输出——不提出新的 alignment 方法、不提出新的优化算法、不构建新的 benchmark。它的核心是"测量并桥接两个已有的度量系统"，这在 significance 上面临挑战。

我会倾向于 **borderline reject**，理由是：(1) 核心贡献是诊断/测量性质的，缺乏直接的 actionable impact；(2) 过度铺展三个贡献导致每个都不够深入；(3) 部分结论可能无论结果如何都是"意料之中"的（MSO和α要么相关——说明它们测量相似结构，要么不相关——说明它们测量不同结构，两个结论都不够 surprising）。

【核心贡献】:
核心贡献是建立 parameter-space (MSO) 和 activation-space (principal angle α) 两个独立度量系统之间的 cross-space correspondence，并在 agentic + MoE 设置下测试几何理论框架的适用性。这本质上是一个 metrological/diagnostic 贡献——回答"我们已有的两套工具是否在测量同一个底层现象？"以及"理论框架在更复杂的架构和设置下是否成立？"

对领域的价值：中等。如果发现 MSO 和 α_repr 高度对应，这为 parameter-space 干预方法（NSPO、OGPSA）和 activation-space 诊断方法提供了统一的理论基础，有实际意义。如果发现不对应，则警告社区不要混用两种范式。但无论哪种结果，直接影响偏间接——不会立即改变任何人的训练/对齐流程。

MoE 作为几何框架的 stress test（C3）可能是最有趣的贡献，因为它直接关系到前沿模型（大多是 MoE 架构）的 alignment 实践。但这也是资源消耗最大、最可能出现技术障碍的部分。

【方法合理性】:
方法设计本身是合理且严谨的。2×2 factorial design、16-point β sweep、Bayesian model comparison（PSIS-LOO + WAIC）、pre-registered outcome topology——这些都是方法论上的良好实践。

然而，存在几个合理性质疑：

1. **Cross-space correspondence 的 layer-wise mixed-effects 分析**：用 ~80-100 个 (MSO_layer, α_repr_layer) 数据点做 mixed-effects model，每个 model-setting 条件只有 ~10-15 个 layers——这有严重的 pseudoreplication 风险。层与层之间高度非独立（特别是相邻层），mixed-effects model 的 random intercept 不足以解决这个问题。

2. **α_repr vs. α_frontier 的比较**：α_repr 来自 Phase 1（representation analysis），α_frontier 来自 Phase 3（elliptic fit to Pareto frontier）。但 α_frontier 的估计依赖于 elliptic model 的拟合优度——如果大多数条件下 elliptic 和 linear model 不可区分（小 α scenario），α_frontier 的 uncertainty 会很大，使得 dual-estimation test 失去 power。

3. **更简单的替代方案**：直接对比 dense vs. MoE 模型在相同 DPO 设置下的 Pareto frontier 形状，配合 representation probing，可能用 1/3 的资源达到 80% 的 insight。Cross-space bridge 和 diagnostic dual-estimation 增加了大量复杂性，但边际信息增益不确定。

4. **Dense vs. MoE 的 confounding**：即使 Qwen3 family 内部比较，32B dense vs. 22B active MoE 在 active parameter count 上差 50%。FLOP-normalized analysis 帮助但不能完全消除 confound。

【5 维度打分】:

1. 研究问题: **中** — 问题是真实存在的：parameter-space 和 activation-space 的度量确实从未被连接，MoE 安全的几何理解确实缺失，Plaut 的近线性 frontier 确实缺乏解释。但这些更像是"测量空白"而非"理解瓶颈"——填补它们不会直接解决任何 alignment 的实际问题。对比同类工作：AQI (EMNLP 2025) 被接收是因为它提出了一个可直接使用的诊断工具；NSPO (ICLR 2026) 被接收是因为它提出了一个有效的优化方法。本 proposal 的输出更接近"characterization report"，在顶会中的价值定位不够清晰。

2. 方法与创新: **中** — 方法论设计严谨（Bayesian model comparison、pre-registered outcomes、mixed-effects analysis），但创新主要在于"将已有工具组合应用于新设置"，而非提出新的分析工具或方法。Cross-space correspondence 是 MSO (ICLR 2026) + principal angles (arXiv 2603.00047) 的直接组合；MoE routing analysis 基本沿用 RASA (arXiv 2602.04448) 和 RoSais (arXiv 2602.08621) 的方法。Pre-registered outcome topology 是一个亮点，但更多是"好的实验实践"而非"方法创新"。

3. 实验设计: **强** — 这是 proposal 最突出的优势。16-point β sweep（远超 Plaut 的 2 点）、2×2 factorial design（覆盖 dense/MoE × chat/agent）、Bayesian model comparison 而非 p-value hacking、多种 evaluation benchmarks（tau2-bench, OpenAgentSafety, ATBench, AdvBench）、sensitivity ablations（rank K, data source, token position）、power simulation before data collection、tiered priority system with fallback plans。这是顶会级别的实验设计。如果执行到位，实验部分本身没有明显漏洞。

4. 可行性: **中偏弱** — 3,500-5,000 GPU-hours / $10,500-15,000 是一笔不小的开支。16 周时间线紧张但可行。最大风险点：(a) Maverick (400B total) 的 DPO 训练可能因内存问题不可行——proposal 承认了这一点并有 fallback，但 fallback 到 Qwen3-30B-A3B (3.3B active) 会大幅改变实验 narrative（从"前沿规模 MoE"变成"小规模 MoE"）；(b) 在 30B+ 模型上进行 128 runs (4 models × 2 settings × 16 β) 的 DPO 训练，加上 representation extraction 和 evaluation，需要非常高效的工程实践；(c) 多个 benchmark 的集成（tau2-bench, OpenAgentSafety, ATBench）增加了工程复杂度。对于一个不是大型实验室的团队来说，这个规模可能过于雄心勃勃。

5. 写作与呈现: **中偏强** — Proposal 的文献覆盖极其全面（30+ 篇相关工作，每篇都精确定位与本工作的关系），逻辑结构清晰（Core Problem → Opportunity → Landscape → Approach → Resource）。但存在两个写作问题：(a) **过度密集**——信息密度太高，审稿人需要花大量精力理解三个 contributions 之间的关系和每个的具体内容，可能导致 reviewer fatigue；(b) **narrative 不够聚焦**——试图同时服务四个 narrative（cross-space bridge, geometric explanation of linearity, MoE stress test, probing-based prediction），核心 story 不够突出。

【概率估计】: [18% - 32%] 中位 25%

【估计理由】:
**向上因素**：(1) Gap 是真实的，文献调研无懈可击，没有直接竞争的 concurrent work；(2) 实验设计非常严谨，方法论上挑不出大问题；(3) Pre-registered outcome topology 是审稿人喜欢的实验设计范式；(4) 如果 C3（MoE stress test）得出强结论（如 MoE 几何完全不同于 dense），这对前沿 alignment 实践有实际指导意义。

**向下因素**：(1) **核心身份问题**——这是 characterization/measurement paper，不提出新方法或工具，在 top venue 的 impact bar 上处于劣势，审稿人可能评价为 "interesting but incremental"；(2) **三个 contributions 的聚焦度不足**——每个 contribution 独立来看都是"测量 X 和 Y 是否对应"或"在新设置下验证已有框架"，没有任何一个强到可以单独撑起一篇顶会；(3) **可预测性风险**——部分结论无论结果如何都不够 surprising（如果 MSO 和 α 对应：expected since both capture safety-capability geometry；如果不对应：trivially expected since they're in different spaces）；(4) **资源可行性**——如果 Maverick 不可行且 fallback 到小规模 MoE，C3 的 narrative 弱化严重；(5) **小 α scenario**——如果大多数条件下 α < 10°，C2 的 elliptic-vs-linear discrimination 可能 inconclusive，fallback 到 "quantifying upper bound" 虽然 informative 但不够 exciting。

中位 25% 的定位理由：实验设计扎实将其拉到合格线以上，但 characterization paper 的身份和 significance 不足将其压在"需要运气"的区间。一个友好的审稿人组可能给 borderline accept，但大概率会有至少一个审稿人质疑 "so what?"。

【主要风险】:
1. **"So what?" 风险**：审稿人质疑——"你测量了 MSO 和 α 的对应关系，发现它们对应/不对应，然后呢？这如何改变我们做 alignment 的方式？"缺乏从诊断到行动的闭环（proposal 明确排除了 intervention phase），这在顶会中是常见的 reject 理由。
2. **Scope 过大导致执行不完整**：128 runs DPO + representation extraction + multi-benchmark evaluation + MoE routing analysis，如果任何环节出现技术困难（Maverick 不可行、某个 benchmark 集成有 bug、某些 β 值训练不稳定），整个 2×2 design 的完整性就会受损，paper 会变成"我们做了一部分实验，结论是 preliminary"。

【实施评估】:
  - 计算资源: 3,500-5,000 GPU-hours (4-8×H100)，$10,500-15,000。属于中等偏大规模实验，需要稳定的 GPU 集群访问或充足的 cloud budget。
  - 数据需求: 主要依赖已有 benchmark（OpenAgentSafety, ATBench, AdvBench, tau2-bench, BeaverTails）。不需要构建新数据集，但需要集成多个异构 benchmark 的 evaluation pipeline，工程量不小。
  - 人工介入: 中等。probe code、evaluation pipeline 搭建需要扎实的工程能力。统计分析（Bayesian model comparison, mixed-effects modeling）需要统计学专业知识。
  - 训练需求: 是，需要对 4 个 30B+ 模型进行 LoRA-DPO 训练，每个模型 16 个 β 值 × 2 个 setting。MoE 模型的 DPO 训练可能需要 reference model offloading 等特殊处理。
  - 新 Benchmark: 否，不需要构建新 benchmark。
  - 预估周期: 16 周（proposal 自估），考虑到工程调试和不可预见问题，20 周更现实。
```

Sources:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)
- [Safety Subspaces are Not Linearly Distinct (ICLR 2026)](https://arxiv.org/abs/2505.14185)
- [The Hidden Dimensions of LLM Alignment (ICML 2025)](https://arxiv.org/abs/2502.09674)
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229)
- [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448)
- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621)
- [NSPO (ICLR 2026)](https://arxiv.org/abs/2512.11391)
- [The Viscosity of Logic](https://arxiv.org/abs/2601.17260)
- [AQI (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.145/)
- [The Geometry of Alignment Collapse](https://arxiv.org/abs/2602.15799)
- [OGPSA](https://arxiv.org/abs/2602.07892)
- [SAFEx](https://arxiv.org/abs/2506.17368)


【原始 proposal（允许参考但不是主要依据）】:
# Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings

## Description

The alignment tax has been formalized geometrically with elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces (arXiv 2603.00047). But empirically, these subspaces are highly entangled (MSO, ICLR 2026), MoE architectures route safety through sparse expert dynamics, and in agentic settings Plaut (arXiv 2603.02229) observes a near-linear frontier (R²=0.77) without geometric explanation. We hypothesize: high entanglement yields small α, degenerating the ellipse toward linearity, while MoE routing introduces discrete dynamics that violate the framework's continuous-subspace assumptions. We produce three contributions. (C1) The first empirical bridge between two independent metric systems — MSO (parameter-space entanglement, ICLR 2026) and principal angle α (activation-space geometry) — establishing their cross-space correspondence via layer-wise mixed-effects analysis; this determines whether parameter-space interventions (NSPO arXiv 2512.11391, OGPSA arXiv 2602.07892) and activation-space diagnostics operate on compatible foundations, and provides initial evidence for probing-based alignment tax prediction without full DPO sweeps. (C2) A diagnostic dual-estimation test with pre-registered outcome topology: α_repr–α_frontier agreement validates geometric theory under entanglement, while systematic divergence quantifies the linear representation hypothesis's failure boundary; a 2×2 outcome matrix ({dense,MoE} × {chat,agent}) pre-registers interpretations for every divergence pattern, making the paper informative under any result. (C3) MoE as a stress test of continuous-subspace geometry: if safety is routing-mediated (RASA, arXiv 2602.04448), activation-space α may fail to capture MoE safety structure, and α_repr–α_frontier divergence should be larger in MoE than dense models. Using a 2×2 design — {Qwen3-32B, Gemma 4 31B} (dense) × {Qwen3-235B-A22B, Llama-4-Maverick} (MoE) in {chat, agent} — we sweep 16 LoRA-DPO β values per condition with Bayesian model comparison (PSIS-LOO + WAIC) and meta-analytic agreement testing. Expected: (1) higher MSO in agents vs. chat; (2) α_repr ≈ α_frontier in dense models, both smaller in agents (explaining Plaut's frontier as a low-angle ellipse); (3) larger α_repr–α_frontier divergence in MoE than dense, quantifying routing-mediated geometry violation; (4) layer-wise MSO–α_repr correspondence establishing whether parameter-space and activation-space analyses are compatible paradigms.

## Core Problem

The alignment tax has been formalized geometrically under the linear representation hypothesis, yielding elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces (arXiv 2603.00047). Three empirical challenges prevent direct application. (1) Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) shows safety and capability subspaces are highly entangled, with MSO strongest between useful and safety-specific updates — but MSO operates in parameter space (SVD of weight difference matrices) while α operates in activation space (cross-covariance of activation vectors). These two metric systems have never been connected, creating a measurement schism: the alignment community simultaneously uses parameter-space interventions (null-space gradient projection) and activation-space diagnostics (probing, geometric theory) without knowing if they analyze the same underlying structure. (2) Frontier models are predominantly MoE architectures where safety is governed by sparse expert routing (RASA arXiv 2602.04448, SAFEx arXiv 2506.17368, Sparse Models Sparse Safety arXiv 2602.08621), not global activation subspaces — making the continuous-subspace geometric framework's applicability non-trivial. (3) In agentic tool-use settings, both challenges intensify: text safety does not transfer to tool-call safety (Mind the GAP, arXiv 2602.16943), and the safe controller mapping has inherently higher Lipschitz complexity (Why Does Agentic Safety Fail to Generalize, arXiv 2605.06992). Plaut (arXiv 2603.02229) measured an approximately linear Pareto frontier (R²=0.77, slope −0.83) in agentic DPO on 8B–14B models — but with only two β values, no representation analysis, and no MoE comparison. The geometric framework's author explicitly notes it fails "for large perturbations, the KL is not quadratic, the representation geometry shifts" — but this failure boundary has never been quantified.

## Opportunity

Four independent lines of work create a convergence point whose bridges are missing. The Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) provides the formal apparatus — principal angles, elliptic Pareto frontiers, tax rate decomposition — but assumes linear separability, static representations, and dense architectures. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) proves the separability assumption fails via MSO in parameter space, but only in chat on models up to 7B — and operates in a different mathematical space than the geometric theory. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions in activation space, but only in chat on Llama 3 8B. Plaut (arXiv 2603.02229, Mar 2026) discovers a near-linear agentic Pareto frontier, which the geometric theory predicts when α is small — but used only 8B–14B dense models with 2 β values and no representation analysis. The MoE safety literature (RASA arXiv 2602.04448, SAFEx arXiv 2506.17368, Sparse Models Sparse Safety arXiv 2602.08621) establishes that safety operates through routing dynamics — safety-critical experts, routing distribution divergence, expert silencing — meaning MoE safety is fundamentally routing-mediated and may not be capturable by continuous activation-space geometry. This makes MoE a stress test of the geometric framework's foundations. The null-space projection literature (NSPO arXiv 2512.11391, ICLR 2026; OGPSA arXiv 2602.07892) mitigates the tax by projecting safety gradients into capability null spaces — but in parameter space, assuming separable subspaces. If MSO and α_repr do not correspond, then parameter-space interventions and activation-space theory may be analyzing different structures, with direct consequences for intervention design. LoRA rank=1 achieves optimal reasoning-safety tradeoff (arXiv 2507.17075), suggesting safety alignment is intrinsically low-rank and representation probing may suffice to capture relevant structure. AQI (arXiv 2506.13901, EMNLP 2025) demonstrates that latent geometry — cluster divergence metrics applied to safe/unsafe activations — can diagnose alignment quality without generation, validating the general approach of representation-based alignment diagnosis; our work differs by using principal angles (geometric structure parameterizing the Pareto frontier) rather than cluster quality metrics (scalar diagnostic), and by connecting to cross-space correspondence, architecture-specific analysis, and frontier shape prediction.

## Landscape

The Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) proves the Pareto frontier is an ellipse ΔS = ΔC cos α + sin α √(B² − ΔC²) parameterized by the principal angle α, but is purely theoretical with no empirical validation and acknowledges failure under large perturbations or nonlinear encoding. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) introduces MSO quantifying safety-capability entanglement via SVD overlap matrices; strongest overlap is between useful and safety updates on Llama 2/3.2 and Qwen 2.5 (1B–7B) — chat only, parameter space only, with layer-specific analysis at 70-85 percentile depth. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions with a dominant refusal direction plus interpretable secondary features — chat only, Llama 3 8B, activation space. Safety Training Persists Through Helpfulness Optimization (arXiv 2603.02229, Mar 2026, Plaut) finds an approximately linear Pareto frontier (R²=0.77, slope −0.83) across 180 DPO configurations on Llama 3.1 8B, Qwen 2.5 7B, and Phi 4 14B using ToolEmu (144 tasks); uses only β ∈ {0.05, 0.1}, no representation analysis, no MoE — frontier shape observed but not geometrically explained. The Viscosity of Logic (arXiv 2601.17260, Jan 2026) sweeps DPO β on Mistral-7B and identifies phase transitions at discrete β values near 10⁻², demonstrating that systematic β sweeping reveals nonlinear regime transitions, motivating dense sampling in high-gradient regions. LoRA is All You Need for Safety Alignment of Reasoning LLMs (arXiv 2507.17075) finds rank=1 LoRA achieves optimal reasoning-safety tradeoff, suggesting safety alignment is intrinsically low-rank. AQI (arXiv 2506.13901, EMNLP 2025) uses latent geometry — Xie-Beni, Calinski-Harabasz, Davies-Bouldin, Dunn indices on safe/unsafe activation clusters — to diagnose alignment quality without generation; differs from our approach in using cluster divergence (scalar quality indicator) vs. principal angles (geometric structure parameterizing Pareto frontier shape), and does not address agent/MoE settings or cross-space correspondence. NSPO (arXiv 2512.11391, ICLR 2026) projects safety gradients into the null space of the capability covariance matrix KK⊤ — but assumes separable subspaces. OGPSA (arXiv 2602.07892, Feb 2026) similarly projects safety gradients onto the orthogonal complement of a capability subspace. Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696) shows safety regions are dataset-dependent with low IoU. The Geometry of Alignment Collapse (arXiv 2602.15799) shows alignment concentrates in low-dimensional subspaces with sharp curvature. ShaPO (arXiv 2602.07340) enforces geometry-aware preference optimization via selective geometry control. Sparse Crosscoders (arXiv 2603.05805) provides methods for comparing MoE and dense model representations at small scale, finding MoEs learn fewer but more specific features. The Autonomy Tax (Mar 2026) shows 99% timeout rates from agent safety training. Mind the GAP (arXiv 2602.16943, Feb 2026) demonstrates text-tool safety divergence across 17,420 datapoints. Why Does Agentic Safety Fail to Generalize (arXiv 2605.06992, May 2026) proves the safe controller has higher Lipschitz constant than task execution. RASA (arXiv 2602.04448, Feb 2026) identifies safety-critical experts via Adversarial Activation Discrepancy and shows full-parameter MoE safety fine-tuning creates routing shortcuts — restoring original routing collapses harmlessness by Δ ∈ [−0.38, −0.46]. SAFEx (arXiv 2506.17368) shows disabling 12 of 6,144 experts drops refusal rate 22%. Sparse Models Sparse Safety (arXiv 2602.08621, Feb 2026) introduces RoSais scores: masking 5 routers increases ASR 4× to 0.79. Geometric Routing (arXiv 2604.14434, Apr 2026) demonstrates monosemantic experts with frequency-to-syntax gradient. Grassmannian MoE (arXiv 2602.17798, Feb 2026) provides subspace-manifold routing. Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026) characterizes theoretical tradeoff limits. The Verifier Tax (Mar 2026) and Steering Externalities (Feb 2026) provide further agentic alignment tax evidence. When Safety Geometry Collapses (arXiv 2605.02914, May 2026) demonstrates safety geometry destruction in guard models. The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026) confirms sharp safety degradation in tool-enabled agents. ATBench (arXiv 2604.02022, Apr 2026) provides paired safe/unsafe trajectory construction with 1,000 trajectories across 1,954 tools. OpenAgentSafety (ICLR 2026) provides 350+ executable tasks with rule-based evaluators. Multi-Agent Security Tax (arXiv 2025) documents safety costs in multi-agent settings. No existing work connects parameter-space MSO to activation-space principal angles, measures alignment tax geometry under entanglement-aware metrics in agentic settings, provides geometric explanation for the observed near-linear frontier in agents, or tests the geometric framework's applicability to MoE routing-mediated safety.

## Approach

We conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agentic tool-use settings, using a 2×2 factorial design: {dense, MoE} × {chat, agent}. Three core contributions: (C1) cross-space metric bridge with metrological implications, (C2) diagnostic dual-estimation test with pre-registered outcome topology, (C3) MoE stress test of geometric framework.

**Model Selection (2 dense + 2 MoE):**
- Dense: Qwen3-32B (32.8B active, Qwen3 family), Gemma 4 31B (31B, Apache 2.0)
- MoE: Qwen3-235B-A22B (22B active / 235B total, Qwen3 family), Llama-4-Maverick (17B active / 400B total)

The Qwen3 dense/MoE pair enables within-family comparison (same training data, tokenizer) — this is the primary apples-to-apples comparison. The cross-family pair (Gemma/Maverick) provides generalizability signal. Active parameter counts differ between dense and MoE (32.8B vs. 22B for Qwen3; 31B vs. 17B cross-family); addressed via FLOP-normalized analysis. Maverick contingency: if DPO memory requirements prove prohibitive (400B total requires reference offloading for DPO), fallback to Qwen3-30B-A3B (30B total / 3.3B active, Qwen3 family), which provides an MoE sparsity gradient (22B vs. 3.3B active) within the same model family.

**Priority tiers:** Tier 1 (must-have): Qwen3-32B + Qwen3-235B-A22B × 2 settings × 16 β = 64 runs. Tier 2 (high-priority): Gemma 4 31B × 2 settings × 16 β = 32 runs. Tier 3 (contingent on resources): Maverick (or fallback) × 2 settings × 16 β = 32 runs.

**Phase 1: Entanglement Geometry & Cross-Space Metric Bridge (wk 1–6)**

*Infrastructure Validation (wk 1–2):* End-to-end pipeline verification on 1–2 β values per model: confirm QLoRA/LoRA-DPO training, activation extraction, evaluation pipeline (tau2-bench, OpenAgentSafety, ATBench, AdvBench). For Maverick, validate reference offloading feasibility; if infeasible, trigger fallback to Qwen3-30B-A3B.

*Trajectory Construction:*
Agent settings: paired safe/unsafe trajectories from (i) OpenAgentSafety's (ICLR 2026) 350+ executable tasks with rule-based safety evaluators across 8 risk categories; (ii) ATBench's (arXiv 2604.02022) planner-based paired trajectory synthesis with 1,000 trajectories across 1,954 tools. Capability subspace: tau2-bench policy-adherence tasks, activations from successful vs. failed completions. Activations extracted at tool-call decision points following LLM Reasoning as Trajectories (arXiv 2604.05655). Chat baseline: AdvBench/BeaverTails prompts matching the original MSO paper's methodology.

*Entanglement Metrics:*
(a) Mode Subspace Overlap (MSO): following Safety Subspaces are Not Linearly Distinct (ICLR 2026), computed via SVD overlap matrices. Sensitivity ablation over subspace rank K ∈ {5, 10, 20, 50, 100}.
(b) Multi-dimensional safety decomposition: following Hidden Dimensions (ICML 2025), identifying dominant refusal direction and orthogonal secondary directions.
(c) Principal angles via SVD on cross-covariance matrices of activation vectors, yielding α_repr. Spectrum of first 10 principal angles reported (not just leading angle). Layer-wise profiles computed per layer.

*Cross-Space Correspondence (C1) with Metrological Implications:*
We test the empirical relationship between MSO (parameter space) and α_repr (activation space) at layer-wise granularity: for each model × setting condition, compute both MSO and α_repr at each layer in the middle-third depth range (~10–15 layers per model), yielding ~80–100 (MSO_layer, α_repr_layer) data points total. Analyze via linear mixed-effects model with MSO_layer as predictor, α_repr_layer as response, and random intercept per model-setting condition. This resolves the statistical power limitation of condition-level analysis (n=8) while respecting the nested structure. The correspondence is non-trivial: weight-space overlap may manifest as activation-space masking, amplification, or rank change without angle reduction. Results determine whether parameter-space interventions (NSPO, OGPSA) and activation-space diagnostics operate on compatible foundations — if MSO and α_repr do not correspond, these two analysis paradigms are not interchangeable, directly impacting alignment intervention design.

*Probing-Based Prediction (C1 application):*
Regression of condition-level representation measurements (MSO, α_repr, effective rank, routing divergence for MoE) against α_frontier and downstream safety metrics. If predictive, this provides initial evidence that alignment tax severity can be estimated from representation probing (~25 GPU-hr per model) without full DPO sweeps (~80+ GPU-hr per model), addressing the open question posed by the Geometry of the Alignment Tax author.

*Trajectory Construction Sensitivity Ablation:*
(i) Data source ablation: MSO and α_repr from OpenAgentSafety-only vs. ATBench-only vs. combined. (ii) Token position ablation: extraction at (a) tool-call decision points (default), (b) last token of each agent step, (c) mean-pooling over all step tokens.

**Phase 2: Architecture-Aware MoE Routing Analysis (wk 4–7, overlapping)**
For MoE models, three-level decomposition:
(a) Shared attention layers: analogous to dense-model analysis, providing controlled comparison.
(b) Per-expert FFN subspaces: safety-critical experts identified via Adversarial Activation Discrepancy (RASA, arXiv 2602.04448). Per-expert α_repr and MSO computed to test whether safety is concentrated in specific experts or distributed.
(c) Router weight space: routing distribution divergence (KL) between safe/unsafe inputs; RoSais-style router safety importance scoring (Sparse Models Sparse Safety, arXiv 2602.08621).

Supplementary/exploratory: Sparse Crosscoders (arXiv 2603.05805) for feature organization comparison, contingent on scaling feasibility at 30B+ scale (original validation at 5-layer models only). Core MoE conclusions do not depend on crosscoder results.

**Phase 3: Pareto Frontier Mapping & Diagnostic Dual-Estimation Test (wk 6–12)**

*Evaluation Axes:*
- Safety axis: OpenAgentSafety safety score (agent); AdvBench refusal rate + BeaverTails safety score (chat). Cross-setting control: all agent-trained models also evaluated on AdvBench (shared safety metric across settings).
- Capability axis: tau2-bench task success rate + OpenAgentSafety task completion rate (agent); MMLU (5-shot) + GSM8K (8-shot) (chat). Pareto frontiers reported per capability metric to verify shape robustness.
- Within-setting comparison (same evaluation protocol, varying architecture/model) is the primary analysis. Cross-setting comparison (agent vs. chat α) is secondary/suggestive, with metric-induced confounds explicitly discussed.

*Training Protocol:*
- Primary: LoRA-DPO on all layers, LoRA rank matched on total trainable parameters across architectures.
- Secondary matching: per-token active trainable parameters (MoE LoRA rank increased to compensate for expert sparsity), testing whether matching strategy affects frontier shape conclusions.
- MoE-specific ablation: (i) shared-attention-only LoRA, (ii) active-expert-only LoRA (HELLoRA-style). These ablations also serve to address the parameter-matching confound by isolating which model components drive frontier shape.
- FLOP-normalized analysis: per-model training/inference FLOPs reported; FLOP-normalized Pareto frontiers provided alongside parameter-matched frontiers.

*β Sweep:*
16 LoRA-DPO β values per model/setting (β ∈ {0.003, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.15, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0}), with increased density in the high-gradient region. If pre-study power simulation indicates n=16 insufficient for α < 15° discrimination, increase to 24 β points for Tier 1 models (offset by reducing Tier 3 scope). Phase transitions at discrete β values (The Viscosity of Logic, arXiv 2601.17260) motivate the dense sampling.

*Statistical Approach:*
Bayesian model comparison using PSIS-LOO (Vehtari, Gelman & Gabry, 2017; preferred for small-sample robustness) and WAIC for three frontier models: (i) elliptic (α, B), (ii) linear (slope, intercept), (iii) piecewise-linear. Report ΔELPD ± SE(ΔELPD); if |ΔELPD| < SE, honestly reported as inconclusive. Pre-study power simulation: synthetic frontiers at α ∈ {5°, 10°, 15°, 20°, 45°} with realistic noise, testing PSIS-LOO discrimination at n=16 and n=24. Leave-one-out sensitivity: checking whether removing any single β point changes model ranking. Supplementary: local curvature analysis (second-order finite differences along the frontier) to detect deviation from linearity even when global shape discrimination is inconclusive.

*Small-α Fallback:* If most conditions yield α < 10° and PSIS-LOO is inconclusive for elliptic vs. linear, C2's contribution reframes as "quantifying α's upper bound" — empirically demonstrating that entanglement is sufficient to collapse the frontier to near-linearity (α < X° with 95% credible interval), which itself validates the geometric theory's prediction that high entanglement linearizes the tax.

*Diagnostic Dual-Estimation Test (C2) with Outcome Topology:*
α_repr (Phase 1) vs. α_frontier (elliptic fit) compared via random-effects meta-analysis: compute (α_repr − α_frontier) for each of the 8 conditions (with uncertainty from bootstrap for α_repr and posterior for α_frontier), fit random-effects model testing whether the population mean difference deviates from 0. This replaces arbitrary counting thresholds with a formal statistical test of systematic divergence.

Pre-registered outcome topology — the 2×2 structure ({dense, MoE} × {chat, agent}) yields four interpretive patterns:
- Dense agree + MoE diverge → routing violates continuous-subspace assumption (C3 confirmed); activation-space geometry remains valid for dense models but breaks for MoE
- Chat agree + agent diverge → agentic complexity exceeds linear representation assumption; standard geometric framework applies in chat but not in tool-use settings
- Both diverge → geometric framework fundamentally inadequate under real entanglement levels; the linear representation hypothesis is a poor approximation for safety-capability geometry
- Both agree → framework is surprisingly robust despite entanglement; principal angle theory extends beyond its stated assumptions

Each pattern has distinct consequences for alignment intervention design (parameter-space projection vs. routing-aware methods vs. setting-specific approaches), ensuring the paper produces actionable findings regardless of outcome.

**Scope note:** We exclude intervention phases (entanglement-adapted OGPSA or NSPO). We focus on rigorous measurement and geometric explanation.

## Resource Estimate

**GPU hours (distinguishing wall-clock from GPU-hours):**
- Infrastructure validation (wk 1–2): ~100 GPU-hr (1–2 β × 4 models × 2 settings, quick runs)
- Phase 1 activation extraction: 4 models × 2 settings × ~25 hr on 4–8×H100 ≈ 400–600 GPU-hr
- Phase 2 MoE routing analysis: 2 models × 60 hr on 8×H100 ≈ 960 GPU-hr
- Phase 3 Tier 1 sweep (Qwen3 pair): 2 models × 2 settings × 16 β × ~5 hr on 4×H100 (dense) / 4–8×H100 (MoE QLoRA) ≈ 640–1,280 GPU-hr
- Phase 3 Tier 2 sweep (Gemma): 1 model × 2 settings × 16 β × ~5 hr on 4×H100 ≈ 640 GPU-hr
- Phase 3 Tier 3 sweep (Maverick/fallback): 1 model × 2 settings × 16 β × ~5 hr on 8×H100 (with ref offloading) ≈ 1,280 GPU-hr
- Phase 3 MoE ablation: 2 models × 2 settings × 8 β × ~5 hr on 4–8×H100 ≈ 640–1,280 GPU-hr
- Agent evaluation (tau2-bench + OpenAgentSafety + ATBench + AdvBench bridging): ~300 GPU-hr
- Buffer (debugging, reruns, power-contingent β expansion): ~500 GPU-hr

**Total: ~3,500–5,000 GPU-hr** (lower bound = QLoRA feasible + Tier 3 deferred; upper bound = 8×H100 for all MoE + full Tier 3).
**Timeline:** 16 weeks (wk 1–2 infrastructure validation + trajectory generation + power simulation; wk 2–6 entanglement geometry extraction; wk 4–7 MoE routing analysis; wk 6–12 Pareto sweeps + ablations; wk 13–14 analysis + regression; wk 15–16 writing).
**Estimated GPU cost:** $10,500–$15,000 at ~$3.00/GPU-hr average.
**Human-in-loop variant:** Claude-assisted probe code and analysis; API cost ~$700 (Sonnet 4.6). **Auto-research variant:** Opus 4.7; API cost ~$2,800; timeline compressible to ~11 weeks.

## Inspired By

Field guide Section 4.1 (pass@1 vs. production gap) + the convergent pattern: (a) the formal alignment tax geometry needs entanglement-robust metrics for empirical validation, (b) Plaut's near-linear agentic frontier needs geometric explanation (our framework predicts: high entanglement → small α → near-linear ellipse), (c) the MoE safety routing literature needs geometric formalization, and (d) null-space projection methods (NSPO, OGPSA) need entanglement-aware adaptation. These four bridges converge in one study.

## Target Venues

- ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026 — primary target, 16-week execution from May 19 start)
- AAAI 2027 (abstract Jul 26, full paper Aug 2, 2026 — stretch target for dense-model-only subset if Tier 1 results strong by week 10)
- ICML 2027 (estimated Jan 29, 2027 — fallback with complete results including all tiers)

## Key References

- What Is the Geometry of the Alignment Tax? (arXiv 2603.00047, Mar 2026)
- Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study (arXiv 2505.14185, ICLR 2026)
- The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025)
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv 2603.02229, Mar 2026, Plaut)
- The Viscosity of Logic: Phase Transitions in DPO (arXiv 2601.17260, Jan 2026)
- LoRA is All You Need for Safety Alignment of Reasoning LLMs (arXiv 2507.17075)
- Alignment Quality Index (arXiv 2506.13901, EMNLP 2025)
- Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization [NSPO] (arXiv 2512.11391, ICLR 2026)
- Safety Alignment as Continual Learning via Orthogonal Gradient Projection [OGPSA] (arXiv 2602.07892, Feb 2026)
- The Autonomy Tax: Defense Training Breaks LLM Agents (arXiv 2026)
- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety (arXiv 2602.16943, Feb 2026)
- Why Does Agentic Safety Fail to Generalize Across Tasks? (arXiv 2605.06992, May 2026)
- RASA: Routing-Aware Safety Alignment for MoE Models (arXiv 2602.04448, Feb 2026)
- SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs (arXiv 2506.17368)
- Sparse Models, Sparse Safety (arXiv 2602.08621, Feb 2026)
- Geometric Routing Enables Causal Expert Control in MoE (arXiv 2604.14434, Apr 2026)
- Grassmannian MoE (arXiv 2602.17798, Feb 2026)
- Sparse Crosscoders for diffing MoEs and Dense models (arXiv 2603.05805, Mar 2026)
- Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696, Feb 2026)
- The Geometry of Alignment Collapse (arXiv 2602.15799, Feb 2026)
- ShaPO: Selective Geometry Control for Safety Alignment (arXiv 2602.07340, Feb 2026)
- Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026)
- Steering Externalities (arXiv 2026)
- The Verifier Tax (arXiv 2026)
- When Safety Geometry Collapses (arXiv 2605.02914, May 2026)
- The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026)
- OpenAgentSafety (ICLR 2026)
- ATBench (arXiv 2604.02022, Apr 2026)
- Multi-Agent Security Tax (arXiv 2025)
- LLM Reasoning as Trajectories (arXiv 2604.05655)
- Vehtari, Gelman & Gabry (2017), Practical Bayesian Model Evaluation Using LOO-CV and WAIC, Statistics and Computing 27(5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9031589a-9f46-4afc-a580-a063bd553602",
  "type": "user",
  "uuid": "e2128f4c-42b1-4814-8bee-d69d98fecffe",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:43:57.387Z_

```json
{
  "parentUuid": "e2128f4c-42b1-4814-8bee-d69d98fecffe",
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
  "uuid": "6d60ff14-2a71-4495-81d2-c845a3e3f5f7",
  "timestamp": "2026-05-20T04:43:57.387Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:43:57.387Z_

```json
{
  "parentUuid": "6d60ff14-2a71-4495-81d2-c845a3e3f5f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d078353a-f2a6-41b3-a245-64b4afd361ff",
  "timestamp": "2026-05-20T04:43:57.387Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient literature context. Let me compile the c…",
  "leafUuid": "d078353a-f2a6-41b3-a245-64b4afd361ff",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize three independent peer reviews of LLM alignment research proposal",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:44:29.591Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them according to the Meta Judge format.

First, let me extract the key data points:

**Reviewer 1:**
- Probability: [20% - 35%] 中位 27%
- Research Question: 中偏强
- Method & Innovation: 中偏弱
- Experimental Design: 强
- Feasibility: 中
- Writing: 中

**Reviewer 2:**
- Probability: [20% - 35%] 中位 27%


- Research Question: 强
- Method & Innovation: 中
- Experimental Design: 强
- Feasibility: 中
- Writing: 中偏强

**Reviewer 3:**
- Probability: [18% - 32%] 中位 25%
- Research Question: 中
- Method & Innovation: 中
- Experimental Design: 强
- Feasibility: 中偏弱
- Writing: 中偏强

Now I'm calculating the aggregate probability by taking the three midpoints of 27%, 27%, and 25%, which gives me a mean of 26.3% with a standard deviation calculation in progress. The consistency is remarkably tight across all reviewers. Looking at where they align, the experimental design gets universal praise, while method and innovation are consistently flagged as weak—specifically the lack of methodological novelty beyond measurement, the overly broad scope, and the unresolved "so what?" question. Feasibility also draws uniform concern, and there's agreement that the small-α scenario creates a confounding issue with the dense-MoE analysis.

Where they diverge slightly: R2 is notably more optimistic about the research question itself, rating it strong while R1 and R3 are more moderate. R3 leans slightly more pessimistic on feasibility than the other two. But these are minor variations against the backdrop of strong consensus on the core weaknesses.

Now I'm ready to synthesize this into the meta-judge assessment.

Given the high consistency across reviewers (standard deviation around 0.94%), I should anchor to the median rather than spread the interval wide. Two reviewers landed on 27%, one on 25%, so the consensus probability sits right around 26%. The three of them are remarkably aligned on what matters most—they all recognize the solid experimental design and genuine research gap, but they're equally concerned about the paper being purely measurement-focused, the scope creep, and the limited methodological innovation. With this level of agreement and applying the "偏严" principle, I'll set the final range at [19%-33%] with a median of 26%. The next thinking is empty, so I'll output nothing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d078353a-f2a6-41b3-a245-64b4afd361ff",
  "isSidechain": false,
  "requestId": "req_011CbDD9LMVV3hF4CUgpZ22X",
  "type": "assistant",
  "uuid": "6f162285-5b5b-460c-b52f-7efadf506ccc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkDJSmDQfp2nUXLw2tAMpo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25043,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25043,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3712,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 25043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25043
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

_source line 9 · 2026-05-20T04:45:30.213Z_

【阶段】: Meta Judge
【三次中位】: [27%, 27%, 25%]  std=0.9%
【共识维度】:
- **实验设计: 强**（3/3 一致）— 所有审稿人均将实验设计列为 proposal 最突出的优势：16-point β sweep、2×2 factorial design、Bayesian model comparison、pre-registered outcome topology、tiered priority system、sensitivity ablations
- **方法与创新: 中/中偏弱**（3/3 一致）— 所有审稿人均认为方法论无创新，核心操作是将已有分析工具（MSO、SVD principal angles、DPO sweep）组合应用于新设定，"桥接"而非"发明"
- **"纯测量/表征研究，缺乏 actionable output": 致命级风险**（3/3 一致）— 所有审稿人均将"So what?"问题列为首要或次要风险。Proposal 明确排除 intervention phase，3,500-5,000 GPU-hr 的纯表征研究缺乏从诊断到行动的闭环
- **范围过载: 强下拉因素**（3/3 一致）— 三个独立贡献（C1 跨空间桥梁 + C2 诊断双估计 + C3 MoE 压力测试）挤入一篇 8 页论文，每个可能处理单薄，审稿人可能建议拆分
- **研究空白真实性: 确认**（3/3 一致）— 所有审稿人均确认 parameter-space MSO 与 activation-space α 从未被连接，MoE 几何框架未被测试，gap 是真实的
- **小 α scenario 削弱 C2: 中等风险**（3/3 一致）— 高纠缠环境下多数条件可能产生 α < 10°，使 elliptic vs. linear 判别不可行，核心 contribution 退化为 upper bound 估计
- **Dense-MoE confounding: 中等方法论缺陷**（3/3 一致）— active parameter count 差异（32.8B vs. 22B）引入固有混淆，FLOP 归一化只能部分缓解
- **Layer-wise mixed-effects pseudoreplication: 统计有效性质疑**（2/3 明确标注，R2+R3）— 相邻层数据高度自相关，违反独立性假设，p 值可能严重膨胀
- **可行性: 中**（3/3 一致）— 16 周 timeline 紧张，Maverick 400B DPO 可行性存疑，fallback 会削弱 narrative

【异常维度】:
- **研究问题评级分歧**：R2 给"强"，R1 给"中偏强"，R3 给"中"——R2 在这一维度偏宽松。但 R2 的"强"评语中也承认了 actionable impact 有限，实际判断与 R1/R3 差异不大，仅措辞不同。降权 R2 的"强"评级，取"中偏强"作为共识。
- **The Viscosity of Logic 引用**：仅 R2 和 R3 提及（R1 未提及），但此为支撑性文献而非评价维度分歧，不影响判断。

【最终概率】: [19% - 33%] 中位 26%
【一致性】: 高（std=0.9%，三份评审在核心判决、风险识别、概率区间上高度收敛）
【综合理由】:

三份评审呈现罕见的高一致性：核心判决完全收敛，概率区间几乎重叠。综合逻辑如下：

1. **概率上限由 idea 质量决定（~33%）**：方法与创新被一致评为"中"或"中偏弱"——纯测量/表征论文在顶会的 contribution bar 上天然受限。即使实验执行完美、结果出人意料，"没有提出新方法/新工具/新算法"这一事实将概率上限锁定在 ~33%。三位审稿人给出的上界分别是 35%、35%、32%，取最严格的 32% 附近上调 1% 至 33%（考虑实验设计的突出优势可能打动个别审稿人）。

2. **概率下限由实验完备性和可行性决定（~19%）**：实验设计被一致评为"强"，这是 proposal 的核心防线——确保论文不会因方法论漏洞而被直接 reject。但 pseudoreplication 风险（2/3 审稿人标注）、小 α 判别困难（3/3）、Dense-MoE confounding（3/3）构成统计方法论的攻击面，可能将概率从合格线拉向 20% 以下。三位审稿人给出的下界分别是 20%、20%、18%，取 19%。

3. **中位取 26% 而非 27%**：虽然 R1 和 R2 中位均为 27%，但基于"宁缺毋滥"原则，R3 的 25% 应适当加权。此外，三份评审均未发现任何被低估的亮点（没有任何维度被某位审稿人评为被其他人忽略的强项），说明 27% 已经充分反映了正面因素。下调 1% 至 26%。

4. **"So what?"是核心击穿风险**：这不是边缘问题——3/3 审稿人将其列为首要或次要风险。一篇花费 3,500-5,000 GPU-hr 的纯表征研究，如果结果不出人意料（而多个预期结果确实可预见——如 "MoE 中几何框架失效"、"agent 比 chat 纠缠更高"），contribution 感会被严重压缩。Pre-registered outcome topology 是好的设计保险，但不能替代 surprising findings 对 accept decision 的推动力。

5. **范围过载是结构性问题**：三个贡献中任何一个都可以独立成文。压缩到 8 页不仅是写作挑战，更根本地影响了每个贡献的深度和说服力。审稿人可能建议"拆成 2-3 篇更聚焦的论文"——这在顶会中是常见的 borderline reject 理由。

【建议】: 边缘（Borderline — 需要显著修改才有竞争力，核心问题是 contribution 定位和范围控制）
【实施评估】:
  - 计算资源: 3,500-5,000 GPU-hours（4-8×H100），$10,500-$15,000。属于中高规模实证研究，需要稳定的 GPU 集群或充足的 cloud budget。对中等规模实验室可行但不轻松。
  - 数据需求: 完全依赖已有公开 benchmark（OpenAgentSafety, ATBench, AdvBench, BeaverTails, tau2-bench），无需自建数据集。但需要集成多个异构 benchmark 的 evaluation pipeline，工程量中等。
  - 人工介入: 较低。主要是 pipeline 搭建、工程调试和统计分析。统计分析（Bayesian model comparison, mixed-effects modeling）需要统计学专业知识。Claude-assisted 自动化可降低部分成本。
  - 训练需求: 大量 LoRA-DPO 训练（128-192 runs），含 MoE 模型的 QLoRA 训练。每次约 5 hr on 4-8×H100。Maverick 400B 的 DPO 训练可行性存在显著不确定性（reference offloading 工程挑战）。
  - 新 Benchmark: 否，完全使用已有 benchmark。
  - 预估周期: 16 周（proposal 自估），实际更可能 18-20 周，考虑到 MoE 训练的工程调试、多 benchmark 集成、以及可能的 Tier 3 降级调整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f162285-5b5b-460c-b52f-7efadf506ccc",
  "isSidechain": false,
  "requestId": "req_011CbDD9LMVV3hF4CUgpZ22X",
  "type": "assistant",
  "uuid": "b58c4a3e-18c8-4fdd-8255-96eaddb5bf93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkDJSmDQfp2nUXLw2tAMpo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25043,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25043,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3712,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 25043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25043
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient literature context. Let me compile the c…",
  "leafUuid": "b58c4a3e-18c8-4fdd-8255-96eaddb5bf93",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize three independent peer reviews of LLM alignment research proposal",
  "sessionId": "a4f86aec-3b40-48f1-8258-c157820c89af"
}
```

---
