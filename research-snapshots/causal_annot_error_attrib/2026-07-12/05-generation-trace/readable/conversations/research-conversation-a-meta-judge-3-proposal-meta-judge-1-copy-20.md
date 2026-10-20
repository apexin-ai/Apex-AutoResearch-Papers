# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/1c0cfc61-25c1-4170-bfb9-ac84c7674771.jsonl`
- **Structured JSON:** [`97fdc2480398321ad318.json`](../../sessions/97/97fdc2480398321ad318.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T20:51:32.944Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T20:51:32.944Z",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make an informed assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【重大前置问题 — 投稿目标与 Proposal 内容严重不匹配】\n\nCoRL 2026 (Conference on Robot Learning, Austin, TX, Nov 10–12, 2026) 的 Call for Papers 明确要求：\n• \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n• \"Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\"\n\n本 Proposal 研究的是 LLM alignment tax 的几何结构、safety-capability subspace 的 entanglement、MoE 路由对安全性的影响，使用的 benchmark (ToolEmu, OpenAgentSafety, ATBench, tau2-bench) 全部是 LLM 软件工具调用场景，与机器人学习没有任何关系。该 Proposal 不涉及任何 robotic manipulation、navigation、locomotion、sim-to-real transfer、embodied AI 等 CoRL 核心主题。\n\n⚠️ 这构成了 desk rejection 级别的致命问题。该 Proposal 适合的会议是 NeurIPS / ICML / ICLR / AAAI（AI safety track）或 ACL / EMNLP（如果有 safety alignment 相关 track），绝非 CoRL。\n\n以下评估将同时给出：(A) 针对 CoRL 的概率，(B) 假设投稿到适配会议（NeurIPS/ICML/ICLR 级别 ML 会议）的 idea 质量评估。\n\n\n【领域调研】:\n\n1. [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026):\n   提出 alignment tax 的几何理论框架——在线性表示假设下，safety-capability 的 Pareto frontier 是由 principal angle α 参数化的椭圆。纯理论工作，作者自己承认\"对大扰动、非线性编码，框架不成立\"。本 Proposal 的核心理论基础。\n\n2. [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026):\n   引入 MSO (Mode Subspace Overlap) 量化 safety-capability subspace 的 entanglement。发现 safety 与 general learning 高度纠缠，在 Llama 2/3.2 和 Qwen 2.5 (1B–7B) 上验证，仅限 chat 场景。本 Proposal 的第二核心依据。\n\n3. [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (Plaut, Mar 2026):\n   在 agentic DPO 中发现近线性 Pareto frontier (R²=0.77, slope −0.83)，使用 Llama 3.1 8B / Qwen 2.5 7B / Phi 4 14B，仅 2 个 β 值，无表示分析，无 MoE 对比。本 Proposal 试图为其提供几何解释。\n\n4. [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448) (Feb 2026):\n   识别 MoE 中 safety-critical experts，发现全参数微调产生 routing 捷径——恢复原始 routing 后 harmlessness 大幅下降。本 Proposal 的 MoE 分析基础之一。\n\n5. [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621) (Feb 2026):\n   引入 RoSais 分数，mask 5 个 router 可使 ASR 提高 4 倍至 0.79，揭示 MoE 安全的脆弱性。\n\n6. [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026):\n   将 safety gradient 投影到 capability null space，实现 SOTA safety 而不损失 capability。假设 subspace 可分——恰好是 MSO 论文证伪的假设。\n\n7. [OGPSA](https://arxiv.org/abs/2602.07892) (Feb 2026):\n   类似思路，将 safety gradient 投影到 capability subspace 的正交补上。\n\n- **调研总结**: 2026 年上半年，alignment tax 的几何理论、safety subspace entanglement、MoE safety routing、agentic safety 四条线已各自成型但相互独立。本 Proposal 试图做\"桥梁\"——在 agentic + MoE 条件下用 entanglement-aware 方法实证验证几何理论。这个 positioning 是清晰的，但本质上是一个 measurement/validation study（测量 + 验证已有理论），而非提出新理论或新方法。\n\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。**\n\n核心 claim 是\"高 entanglement → 小 α → 近线性 frontier，这解释了 Plaut 的观察\"。一个成本更低的替代方案是：\n(1) 直接在 Plaut 的设置上增加 β sweep 点数（从 2 增加到 12），拟合椭圆 vs 线性，提取 α_frontier——这不需要 MoE、不需要 entanglement 测量，大约是本 Proposal GPU 开销的 1/5；\n(2) 在同样的模型上跑 MSO 分析——这在原始 MSO 论文的框架内可以直接完成，不需要新方法论。\n\n本 Proposal 的增量价值在于：\n- 2×2 factorial design（dense × MoE × chat × agent）的系统性\n- Dual-estimation test（α_repr vs α_frontier 的一致性）\n- MoE routing-specific 分析\n\n但这些增量价值更多是**实验设计的系统性**而非**idea 的概念创新**。如果 trivial baseline（扩展 Plaut + 扩展 MSO 论文到更大模型）就能得到 80% 的 insight，剩下 20% 的边际贡献是否足以支撑一篇顶会？这是核心问题。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中，以下环节是\"想当然\"的：\n\n1. **线性表示假设在 agentic 场景下成立**：几何理论的作者自己承认框架在大扰动下失效。Agentic tool-use 涉及多步决策、工具调用，其表示空间的非线性程度远高于 chat。如果线性假设不成立，α_repr 和 α_frontier 的 dual-estimation test 的逻辑前提就崩塌了。\n   \n2. **MSO 在 agentic 场景下可被有意义地计算**：MSO 原始论文在 chat setting 的 1B–7B 模型上验证。在 agentic 场景中，safety subspace 的定义本身就更模糊（tool-call safety vs. text safety），提取 activation 的\"决策点\"选择（tool-call 前一 token）是否能准确捕获 safety subspace 是未经验证的假设。\n\n3. **Entanglement → 小 α 的因果方向**：Proposal 假设高 entanglement 导致小 principal angle，但这两者可能只是同一现象的不同度量，而非因果关系。如果 MSO 和 α 本质上是同一信息的不同表达，那\"dual-estimation test\"就变成了 tautology 而非 validation。\n\n4. **Dense vs MoE 在 matched active parameters 下可公平比较**：MoE 的 routing 机制意味着不同 token 激活不同的 expert subsets，这使得\"subspace\"的定义在 MoE 和 dense 之间本质不同。matched active parameters 不等于 matched representation capacity。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心贡献是将已有理论框架（2603.00047 的几何理论）、已有度量方法（ICLR 2026 的 MSO）、已有经验观察（Plaut 的近线性 frontier）组合在新场景（agentic + MoE）中进行实证验证。没有提出新的理论工具、新的度量方法或新的算法。\"Dual-estimation test\"（α_repr vs α_frontier）有一定方法论新颖性，但本质上是对已有理论的验证实验设计，而非概念创新。Proposal 自己也承认排除了 intervention phase——这意味着即使测量结论全部成立，也没有 actionable 的新方法产出。\n   \n   与最相关工作的差异：相对于 2603.00047（理论无实证）+ 2505.14185（chat 无 agentic）+ Plaut（无表示分析无 MoE），增量是\"在更大范围内做更系统的测量\"。这是一种 extension novelty，不是 conceptual novelty。\n\n2. **Significance: 中** — \n   如果 dual-estimation test 成功验证（α_repr ≈ α_frontier），这为几何理论框架提供了第一个实证支撑，有一定价值。但核心预测（高 entanglement → 近线性 frontier）是理论的直接推论，审稿人大概率会说 \"I would have guessed this\"。MoE 分析如果发现质性不同的 frontier 形状，会更有 surprise value，但这是 dual-outcome 设计中的\"乐观场景\"。\n   \n   作为一个 measurement study，其影响力取决于：(a) 是否有后续工作会基于这些测量结果开发新方法，(b) 社区是否真的需要这种验证。考虑到 NSPO 和 OGPSA 已经在\"假设 subspace 可分\"的前提下取得了 SOTA 结果，实证证明\"其实不可分\"的价值可能被\"但方法照样 work\"所削弱。\n\n3. **Related Work: 强** — \n   覆盖极其全面，引用了 25+ 篇高度相关的 2025–2026 工作，定位清晰。文献调研是这个 Proposal 最强的维度。每条研究线的总结准确，gap 的识别合理。搜索验证了所引论文均真实存在且描述准确（2603.00047, 2505.14185, 2603.02229, 2512.11391, 2602.04448, 2602.08621 等均可查证）。\n\n\n【概率估计】:\n\n(A) **CoRL 2026: 0-2%，中位 1%**\n   — 投稿目标与 Proposal 内容完全不匹配，极大概率 desk rejection。\n\n(B) **假设投稿到适配会议（NeurIPS/ICML/ICLR AI Safety track）: 15-25%，中位 20%**\n\n【估计理由】:\nIdea 内核是一个系统性 measurement study，将已有理论、已有度量、已有经验观察组合在新场景中验证。Related Work 覆盖强，实验设计系统（但这是执行层面的优势，不影响 idea 上限评估）。Novelty 是限制上界的核心瓶颈——缺乏概念创新，核心预测不够 surprising（\"高 entanglement 导致近线性 frontier\"是理论的直接推论）。存在显著 trivial alternative 威胁（扩展 Plaut + 扩展 MSO 即可获得大部分 insight）。前提假设中线性表示假设在 agentic 场景下是否成立是一个未解决的根本问题，如果不成立则整个框架的基础动摇。\n\n【主要风险】:\n1. **Venue mismatch (致命)**: CoRL 是机器人学习会议，本 Proposal 与机器人学无关，几乎确定 desk rejection。\n2. **Novelty 不足 (idea 层面)**: 即使在适配会议，\"在新场景中系统性验证已有理论\"的 contribution level 可能被审稿人认为是 incremental extension，而非独立的 conceptual contribution。核心发现若 positive，审稿人反应更可能是 \"confirms what the theory predicted\" 而非 \"surprising\"。\n```\n\n---\n\n**总结建议**：\n\n这个 Proposal 的**文献调研和实验设计**做得非常扎实，但有两个根本性问题：\n\n1. **投稿目标错误**：必须更换到 NeurIPS / ICML / ICLR 等 ML 安全相关会议。投 CoRL 几乎不可能中稿。\n\n2. **Idea 内核是 measurement/validation study，缺乏概念创新**：如果作者能增加 intervention component（例如 entanglement-aware 的 NSPO/OGPSA 改进方法，并证明其优于原始方法），novelty 和 significance 都会显著提升。当前 Proposal 明确排除了这一部分，这限制了其贡献的天花板。\n\nSources:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)\n- [Safety Subspaces are Not Linearly Distinct (ICLR 2026)](https://arxiv.org/abs/2505.14185)\n- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229)\n- [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448)\n- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621)\n- [NSPO (ICLR 2026)](https://arxiv.org/abs/2512.11391)\n- [OGPSA](https://arxiv.org/abs/2602.07892)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\n\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide my assessment. Let me compile the analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：会议 Scope 不匹配】\n\n在进入 idea 质量评估之前，必须首先指出一个**致命的venue选择问题**：\n\nCoRL 2026 (Conference on Robot Learning) 的 Call for Papers 明确声明：\n\"submissions without a robotics focus will be returned without review\"\n\n本 proposal 的全部内容是 LLM 对齐税的几何理论在 dense/MoE 架构上的实证验证——\n涉及 alignment tax geometry、safety-capability subspace entanglement、LoRA-DPO β sweeps——\n**没有任何机器人学习内容**。没有机器人实验、没有 sim-to-real、没有机器人控制/感知/操作。\n所谓\"agentic tool-use\"是指 LLM 调用软件工具（ToolEmu、tau2-bench），不是机器人工具操作。\n\n**这篇论文提交 CoRL 会被 desk reject。** 这不是 idea 质量问题，而是根本性的 scope mismatch。\n\n合适的目标会议：NeurIPS 2026、ICLR 2027、ICML 2026（如果 deadline 未过）。\n\n以下评估假设投稿至一个 scope 合适的 ML/AI Safety 顶会（如 NeurIPS 2026），对 idea 质量本身进行客观打分。\n\n---\n\n【领域调研】:\n\n1. [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026):\n   纯理论工作，证明 alignment tax 的 Pareto frontier 是由 safety/capability subspace 间 principal angle α 参数化的椭圆。作者自己承认框架在 \"large perturbations\" 下失效（KL 不是二次的，representation geometry 会 shift）。**没有任何实证验证**。本 proposal 的核心目标之一是提供首个实证验证——这个 gap 是真实的。\n\n2. [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026):\n   引入 MSO 度量 safety-capability entanglement，发现 useful 和 safety updates 的 subspace 高度重叠。但仅在 chat setting 上测试（Llama 2/3.2, Qwen 2.5, 1B-7B）。本 proposal 正确识别了需要将其扩展到 agentic setting 和更大模型的 gap。\n\n3. [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (arXiv, Mar 2026, Plaut):\n   在 agentic DPO 设置下观察到近线性 Pareto frontier（R²=0.77, slope -0.83）。但仅用 2 个 β 值，无 representation analysis，无 MoE 对比。本 proposal 正确识别了这个观察缺乏几何解释的 gap。\n\n4. [RASA: Routing-Aware Safety Alignment for MoE](https://arxiv.org/abs/2602.04448) (Feb 2026):\n   识别 safety-critical experts，发现 full-parameter MoE safety fine-tuning 创建 routing shortcuts——恢复原始 routing 后 harmlessness 崩溃 Δ ∈ [-0.38, -0.46]。与本 proposal 的 MoE routing analysis 直接相关但不竞争——RASA 是 intervention，本 proposal 是 measurement。\n\n5. [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025):\n   发现多维正交 safety directions——dominant refusal direction + interpretable secondary features。仅在 chat setting, Llama 3 8B 上验证。\n\n6. [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026) & [OGPSA](https://arxiv.org/abs/2602.07892) (Feb 2026):\n   两种 null-space projection 方法都假设 safety/capability subspaces 可分——恰好是 MSO 论文证伪的假设。本 proposal 正确指出了这个矛盾。\n\n7. 直接竞争工作搜索结果：**未发现**已有工作在 entanglement-aware metrics 下测量 agentic settings 的 alignment tax geometry，也未发现 dense vs. MoE alignment tax 结构对比。\n\n- **调研总结**: 领域中存在四条独立研究线——(a) alignment tax 的几何理论（纯理论，无验证），(b) safety subspace entanglement（仅 chat），(c) agentic Pareto frontier 观察（无几何解释），(d) MoE safety routing（无 alignment tax geometry 联系）。本 proposal 的\"桥接\"定位在文献中确实是空白的。但这个空白的性质更多是\"自然延伸的实证补全\"，而非\"意外的概念突破\"。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。**\n\n最直接的简化替代方案：在 Plaut 的实验基础上，仅需 (1) 增加 β 值数量（如 12 个），(2) 在同一模型上跑 MSO + principal angle 计算，(3) 拟合椭圆 vs. 线性模型并提取 α_frontier。这个方案大约占本 proposal 贡献的 60-70%，但工程成本不到 1/4。\n\n本 proposal 的增量价值在于：\n- 2×2 factorial design（dense × MoE × chat × agent）——MoE routing 分析是 trivial alternative 无法覆盖的\n- Dual-estimation test（α_repr vs α_frontier 一致性）——这是方法论上的贡献\n- Per-expert subspace analysis 和 routing divergence 分析\n\n但核心发现的 *惊喜度* 是否因为增加了这些维度而本质提升？如果最终发现 \"agents 确实 entanglement 更高、α 更小、frontier 更线性\"——这正是理论的直接预测，审稿人会说 \"I would have guessed this\"。MoE 部分的发现可能更有惊喜度（routing 如何调制 tax 形状是未知的），但这取决于实验结果。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有多个未经验证的环节：\n\n1. **MSO → principal angle α 的映射关系是假设的**。MSO 测量的是 SVD 产生的 top-K singular vectors 之间的 overlap，而 α 是 safety/capability subspaces 之间的 principal angle。这两者相关但不等价——proposal 同时计算两者并期望一致，但没有理论保证 MSO 高 ↔ α 小。这个映射本身需要验证而非假设。\n\n2. **\"高 Lipschitz complexity → 高 MSO\" 是推测**。proposal 引用 \"Why Does Agentic Safety Fail to Generalize\" 的 Lipschitz 论证来预测 agents 有更高 entanglement，但 Lipschitz complexity 作用于函数空间，MSO 作用于 weight/activation subspace——两者之间的联系是直觉性的，不是严格推导。\n\n3. **线性表示假设本身**。整个框架依赖于 safety 和 capability 可以被编码为线性方向——但 geometric theory 论文的作者自己承认框架在 large perturbations 下失效。在 MoE 架构中，routing 的非线性特性可能从根本上违反这个假设。\n\n4. **12 个 β 值的统计功效**。proposal 选择 Bayesian model comparison (WAIC) 来避免频率主义检验在 n=12 时的低功效。但 WAIC 在仅 12 个数据点上区分 2-参数椭圆模型 vs. 2-参数线性模型的能力存疑——尤其当两者在低 α 时形状非常接近时（这恰好是 proposal 预测的情况）。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   \"桥接\"确实在文献中不存在（搜索未发现直接竞争工作），这是真实的。但桥接的性质是 **\"将已有工具（MSO、principal angles、LoRA-DPO sweeps）应用到新 setting（agentic + MoE）\"**——这是方法论组合创新，而非概念创新。Dual-estimation test（α_repr vs α_frontier）是最有方法论新意的点，但其成功取决于一个未经验证的假设（两个 α 应该一致）。与之对比，MSO 论文提出了新度量，geometric theory 论文推导了新理论——本 proposal 的 novelty delta 在于 empirical validation + architectural extension，这在 ML 顶会属于 solid but not surprising 级别。\n\n2. **Significance: 中** — \n   研究问题是重要的——理解 alignment tax 的几何结构、MoE 如何调制 safety、agentic settings 的特殊性——这些都是社区关心的话题。但本 proposal 是 **measurement study**，不产出新方法或新理论。如果所有预测被验证（agents MSO 更高、α 更小、frontier 更线性），这 validates 已有理论——有价值，但影响力有限，因为结果方向是可预测的。如果 α_repr ≠ α_frontier（理论不成立），那是 negative result，更难发表但可能更有科学价值。MoE routing 对 tax geometry 的影响是唯一可能产生 \"surprising\" 发现的方向——但 proposal 在这里的预测最弱（\"MoE shows different frontier shapes\" 太模糊）。\n\n3. **Related Work: 强** — \n   这是 proposal 最强的维度。Related work 的覆盖面极广（20+ 篇），包括了 geometric theory、subspace entanglement、agentic safety、MoE safety、null-space projection 等所有相关线索。差异化定位清晰——\"四条线的桥接\"。对每篇关键论文的局限性分析（chat only、no representation analysis、assumes separability）是准确的。唯一的小瑕疵：部分引用（如 \"The Autonomy Tax\"、\"Steering Externalities\"、\"The Verifier Tax\"）没有给出完整的 arXiv ID，可能需要验证。\n\n---\n\n【概率估计】: [20% - 32%] 中位 25%（假设投稿至 scope 合适的顶会如 NeurIPS 2026）\n\n若投稿 CoRL 2026: [0% - 2%] 中位 0%（desk reject，scope 完全不匹配）\n\n【估计理由】: \n对于 NeurIPS 等合适 venue：idea 的 \"桥接\" 定位是真实存在的文献空白，Related Work 覆盖全面且定位清晰，这些是加分项。但限制上界的核心因素是 **Novelty 和 Significance 的天花板**：(1) 核心贡献是 measurement/empirical validation，不是新方法或新理论；(2) 最可能的结果（agents 更 entangled, α 更小, frontier 更线性）是理论的直接预测，审稿人会说 \"I would have guessed this\"；(3) trivial alternative 威胁真实存在——简化版实验能获取大部分核心发现。这些因素将 idea 质量锚定在 25-35% 区间的低端。Related Work 的强势略做补偿，但无法弥补核心 novelty/significance 的中等水平。\n\n对于 CoRL：完全没有机器人学习内容，会被 desk reject，概率实质为 0。\n\n【主要风险】:\n1. **\"I would have guessed this\" 风险**：核心预测（agents → 高 entanglement → 小 α → 线性 frontier）是已有理论的直接推论。如果实验完美验证了这个预测，审稿人可能认为 contribution 是 \"running the experiment\" 而非 \"surprising insight\"——这是 measurement study 面临的经典困境。\n2. **统计不可区分风险**：proposal 预测 agent setting 下 α 很小、frontier 接近线性——但在 α 很小时，椭圆和线性模型在 12 个数据点上可能统计不可区分（WAIC 无法有效区分两个几乎相同形状的模型），从而使得 dual-estimation test 的核心方法论贡献失去说服力。\n```\n\n---\n\n**补充说明（不属于正式评分格式）**：\n\n关于 **CoRL 投稿**，我必须明确提醒：CoRL 2026 的 [Call for Papers](https://www.corl.org/contributions/call-for-papers) 明确要求提交必须有 robotics focus，否则 \"returned without review\"。本 proposal 100% 是 LLM alignment/safety 的 representation geometry 研究，没有任何机器人实验或机器人学习内容。建议将目标会议改为 **NeurIPS 2026**（deadline 通常在 5 月底）或 **ICLR 2027**。上述概率评估均基于投稿至 scope 合适的 ML/AI 顶会。\n\nSources:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)\n- [Safety Subspaces are Not Linearly Distinct (ICLR 2026)](https://arxiv.org/abs/2505.14185)\n- [Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut)](https://arxiv.org/abs/2603.02229)\n- [RASA: Routing-Aware Safety Alignment for MoE](https://arxiv.org/abs/2602.04448)\n- [The Hidden Dimensions of LLM Alignment (ICML 2025)](https://arxiv.org/abs/2502.09674)\n- [NSPO (ICLR 2026)](https://arxiv.org/abs/2512.11391)\n- [OGPSA](https://arxiv.org/abs/2602.07892)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings\n\n## Description\nThe alignment tax has been formalized geometrically with elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces. But empirically, these subspaces are highly entangled (ICLR 2026), MoE architectures route safety through sparse expert dynamics, and in agentic settings Plaut (2603.02229) already observes a near-linear frontier (R²=0.77) without geometric explanation. We hypothesize a unifying account: high safety-capability entanglement in agents yields small α, degenerating the ellipse toward linearity — and MoE routing introduces architectural modulation absent in dense models. We conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agents. Using a 2×2 design — {Qwen3-32B, Gemma 4 31B} (dense) × {Qwen3-235B-A22B, Llama-4-Maverick} (MoE) in {chat, agent} — we measure entanglement via MSO, multi-dimensional safety decomposition, and principal angles (yielding α_repr). For MoE models, we add per-expert subspace analysis, routing distribution divergence, and router safety importance scoring. We sweep 12 LoRA-DPO β values per condition with matched trainable parameters across architectures (plus MoE-specific ablations), using Bayesian model comparison (WAIC) to distinguish elliptic, linear, and piecewise-linear frontiers, extracting α_frontier. The dual-estimation test — whether α_repr agrees with α_frontier — provides the first empirical validation of the geometric alignment tax framework. Expected: (1) higher MSO in agents vs. chat; (2) α_repr ≈ α_frontier with both smaller in agents (explaining Plaut's near-linear frontier as a low-angle ellipse); (3) MoE routing-mediated safety fragility absent in dense models; (4) the geometric framework becoming actionable for predicting alignment tax severity from representation measurements alone.\n\n## Core Problem\nThe alignment tax — the safety-capability tradeoff — has been formalized geometrically under the linear representation hypothesis, yielding elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces. However, three empirical challenges prevent direct application: (1) Safety Subspaces are Not Linearly Distinct (ICLR 2026) shows safety and capability subspaces are highly entangled, with Mode Subspace Overlap (MSO) strongest between useful and safety-specific updates; (2) frontier open-weight models are predominantly Mixture-of-Experts architectures where safety is governed by sparse expert routing dynamics (RASA, SAFEx, Sparse Models Sparse Safety), not global activation subspaces; (3) in agentic tool-use settings, both challenges intensify — text safety does not transfer to tool-call safety (Mind the GAP), and the safe controller mapping has inherently higher Lipschitz complexity (Why Does Agentic Safety Fail to Generalize). Critically, Plaut (2603.02229) already measured an approximately linear Pareto frontier (R²=0.77, slope −0.83) in agentic DPO on 8B–14B models — but with only two β values, no representation analysis, and no MoE comparison, providing an empirical observation without geometric explanation. The theoretical framework predicts that when the principal angle α is small (i.e., when safety and capability subspaces are highly entangled), the elliptic frontier degenerates toward linearity. The field thus has a frontier shape observation that awaits geometric explanation, entanglement measurements that have not been tested in agents or MoE models, and a theoretical bridge between entanglement degree and frontier geometry that has never been validated empirically.\n\n## Opportunity\nFour independent lines of work create a convergence point whose bridge is missing. The Geometry of the Alignment Tax (Mar 2026) provides the formal apparatus — principal angles, elliptic Pareto frontiers, tax rate decomposition — but assumes linear separability, static representations, and dense architectures, with the author explicitly noting the framework fails 'for large perturbations, the KL is not quadratic, the representation geometry shifts.' Safety Subspaces are Not Linearly Distinct (ICLR 2026) proves the separability assumption fails empirically by quantifying safety-capability entanglement via MSO, but only studies chat settings on models up to 7B. The Hidden Dimensions of LLM Alignment (ICML 2025) reveals multi-dimensional orthogonal safety directions with interpretable secondary features, but likewise only in chat on Llama 3 8B. Plaut (Mar 2026) discovers a near-linear Pareto frontier in agentic DPO, which the geometric theory predicts should occur when α is small — but Plaut used only 8B–14B dense models with 2 β values and provided no representation analysis to verify this geometric explanation. Meanwhile, the MoE safety literature (RASA, SAFEx, Sparse Models Sparse Safety, Geometric Routing) establishes that safety operates through routing dynamics — safety-critical experts, routing distribution divergence, expert silencing vulnerabilities — but none connects to the alignment tax geometry. And the null-space projection literature (NSPO at ICLR 2026, OGPSA) mitigates the alignment tax by projecting safety gradients into capability null spaces, but assumes those subspaces are separable — precisely the assumption MSO disproves. The missing bridge connects: (a) entanglement-aware geometric measurement to the theoretical framework, (b) architecture-aware analysis to capture how MoE routing mediates the tax differently from dense models, and (c) agentic empirics to verify whether high entanglement geometrically explains the near-linear frontier Plaut observed.\n\n## Related Work / Landscape\nThe Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) proves the Pareto frontier is an ellipse ΔS = ΔC cos α + sin α √(B² − ΔC²) parameterized by the principal angle α, but the paper is purely theoretical with no empirical validation, and acknowledges the framework fails under large perturbations or nonlinear encoding. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) introduces MSO quantifying safety-capability entanglement; strongest overlap is between useful and safety updates on Llama 2/3.2 and Qwen 2.5 (1B–7B) — chat only. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions with a dominant refusal direction plus interpretable secondary features — chat only, Llama 3 8B. Safety Training Persists Through Helpfulness Optimization (arXiv 2603.02229, Mar 2026, Plaut) finds an approximately linear Pareto frontier (R²=0.77, slope −0.83) across 180 DPO training configurations on Llama 3.1 8B, Qwen 2.5 7B, and Phi 4 14B using ToolEmu (144 tasks); uses only β ∈ {0.05, 0.1}, no representation analysis, no MoE models — the frontier shape is observed but not geometrically explained. NSPO (arXiv 2512.11391, ICLR 2026) projects safety gradients into the null space of the capability covariance matrix KK⊤, achieving SOTA safety without capability degradation on Llama3-8B and Qwen2.5-7B — but assumes separable subspaces. OGPSA (arXiv 2602.07892, Feb 2026) similarly projects safety gradients onto the orthogonal complement of a capability subspace, improving the safety-utility Pareto frontier. Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696) shows safety regions are dataset-dependent with low IoU across safety datasets, complementing the entanglement finding. The Geometry of Alignment Collapse (arXiv 2602.15799) shows alignment concentrates in low-dimensional subspaces with sharp curvature, creating brittle structure where second-order gradient effects systematically steer into alignment-sensitive regions. ShaPO (arXiv 2602.07340) enforces geometry-aware preference optimization via selective geometry control over alignment-critical parameter subspace, demonstrating token-level and reward-level geometric stabilization. Sparse Crosscoders (arXiv 2603.05805) provides crosscoder-based methods for comparing MoE and dense model representations, finding MoEs learn fewer but more specific features than dense models at matched active parameters. The Autonomy Tax (Mar 2026) shows 99% timeout rates from agent safety training. Mind the GAP (arXiv 2602.16943, Feb 2026) demonstrates text-tool safety divergence across 17,420 datapoints. Why Does Agentic Safety Fail to Generalize (arXiv 2605.06992, May 2026) proves the safe controller has higher Lipschitz constant than task execution. RASA (arXiv 2602.04448, Feb 2026) identifies safety-critical experts via Adversarial Activation Discrepancy and shows full-parameter MoE safety fine-tuning creates routing dominance artifacts — when original routing is restored in fully fine-tuned models, harmlessness collapses by Δ ∈ [−0.38, −0.46], proving safety was achieved through routing shortcuts not genuine expert repair. SAFEx shows disabling 12 of 6,144 experts drops refusal rate 22%. Sparse Models Sparse Safety (arXiv 2602.08621, Feb 2026) introduces RoSais scores: masking 5 routers increases ASR 4× to 0.79. Geometric Routing (arXiv 2604.14434, Apr 2026) demonstrates monosemantic experts with frequency-to-syntax gradient. Grassmannian MoE (arXiv 2602.17798, Feb 2026) provides subspace-manifold routing. Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026) characterizes theoretical tradeoff limits. The Verifier Tax (Mar 2026) and Steering Externalities (Feb 2026) provide further agentic alignment tax evidence. When Safety Geometry Collapses (arXiv 2605.02914, May 2026) demonstrates safety geometry destruction in guard models. The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026) confirms sharp safety degradation in tool-enabled agents. ATBench (arXiv 2604.02022, Apr 2026) provides paired safe/unsafe trajectory construction methodology via planner-based synthesis with 1,000 trajectories across 1,954 tools. No existing work measures alignment tax geometry under entanglement-aware metrics in agentic settings, provides geometric explanation for the observed near-linear frontier in agents, or compares dense vs. MoE alignment tax structure.\n\n## Approach\nWe conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agentic tool-use settings, using a 2×2 factorial design: {dense, MoE} × {chat, agent}. The study has three phases producing three core contributions: entanglement measurement, MoE routing analysis, and geometrically-explained Pareto frontier mapping.\n\n**Model Selection (2 dense + 2 MoE, matched on active parameters):**\n- Dense: Qwen3-32B (32.8B active, Qwen3 family), Gemma 4 31B (31B, Apache 2.0)\n- MoE: Qwen3-235B-A22B (22B active / 235B total, Qwen3 family), Llama-4-Maverick (17B active / 400B total)\nThe Qwen3 dense/MoE pair enables within-family comparison isolating routing effects.\n\n**Phase 1: Entanglement Geometry Measurement (wk 1–5)**\n\n*Trajectory Construction (addressing methodological specification):*\nFor agent settings, we construct paired safe/unsafe trajectories using two complementary sources: (i) OpenAgentSafety's 350+ executable tasks with rule-based safety evaluators across 8 risk categories — we run each model to generate trajectories, then classify via the framework's evaluators; (ii) ATBench's planner-based paired trajectory synthesis methodology, which generates matched safe/unsafe trajectory pairs sharing identical task setups with controlled risk injection points (avg. 9 turns, 1,954 tools). For capability subspace extraction, we use tau2-bench policy-adherence tasks, extracting activations from successful vs. failed completions. Activations are extracted at tool-call decision points — the token positions immediately preceding tool-call generation — following the step-specific extraction methodology from LLM Reasoning as Trajectories (2604.05655), which demonstrated that activations at decision boundaries form linearly separable, step-specific subspaces. For chat baseline, we use AdvBench/BeaverTails prompts matching the original MSO paper's methodology.\n\n*Entanglement Metrics:*\n(a) Mode Subspace Overlap (MSO): following Safety Subspaces are Not Linearly Distinct, we compute MSO between safety and capability update subspaces via SVD overlap matrices. We test whether MSO is higher in agent vs. chat settings, as predicted by the higher Lipschitz complexity of safe agentic control.\n(b) Multi-dimensional safety decomposition: following Hidden Dimensions, we identify the dominant refusal direction and orthogonal secondary directions, testing whether agent settings activate additional safety dimensions absent in chat (e.g., tool-execution safety, multi-step consequence reasoning).\n(c) Principal angles via SVD on cross-covariance matrices: critically reinterpreted as coupling strength rather than separability indicators. Small angles indicate strong entanglement. We compute α_repr (representation-derived principal angle) as the first output of this analysis, which will later be compared to α_frontier (the angle estimated from Pareto frontier fitting).\n\n**Phase 2: Architecture-Aware MoE Routing Analysis (wk 4–7, overlapping)**\nFor MoE models, we decompose analysis into three levels:\n(a) Shared attention layers: analogous to dense-model analysis, providing a controlled comparison point.\n(b) Per-expert FFN subspaces: extract safety/capability subspaces within individual expert networks, identifying safety-critical experts via Adversarial Activation Discrepancy (following RASA's methodology) between safe/unsafe trajectories. We apply Sparse Crosscoders (2603.05805) to compare feature organization between MoE and dense models, testing whether MoE's 'fewer but more specific features' pattern extends to safety representations.\n(c) Router weight space: compute routing distribution divergence (KL divergence of expert selection probabilities) between safe/unsafe inputs in chat vs. agent contexts. Test whether routing divergence is smaller in agent settings (indicating safety routing is more fragile under tool-use). Apply RoSais-style router safety importance scoring to identify which layers' routing is most safety-critical.\n\n**Phase 3: Pareto Frontier Mapping with Geometric Explanation (wk 6–11)**\n\n*Addressing the confounded comparison:* We use a two-tier design:\n- Primary comparison ('apples-to-apples'): LoRA-DPO applied to all layers for BOTH dense and MoE models, with LoRA rank adjusted to match total trainable parameter count across architectures. This isolates architectural effects from training protocol effects.\n- MoE-specific ablation: For MoE models only, we additionally run (i) shared-attention-only LoRA and (ii) active-expert-only LoRA (HELLoRA-style, targeting top-k activated experts). This tests whether MoE-specific training protocols change frontier shape, decomposing the total architecture effect into routing-mediated vs. representation-mediated components.\n\n*Statistical approach (addressing power concerns):* We sweep 12 LoRA-DPO β values per model/setting combination (β ∈ {0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0}, with increased resolution in the high-gradient region identified in preliminary coarse sweeps). Rather than frequentist goodness-of-fit tests (which lack power at n=12), we use Bayesian model comparison via WAIC to compare three frontier models: (i) elliptic (2 free parameters: α, B), (ii) linear (2 parameters: slope, intercept), (iii) piecewise-linear (allowing discrete expert-switching thresholds in MoE). From the elliptic fit, we extract α_frontier.\n\n*Core hypothesis connecting Phases 1 and 3:* The key prediction is that α_repr (measured from representation geometry in Phase 1) and α_frontier (estimated from Pareto frontier shape in Phase 3) should agree if the geometric theory holds under entanglement. This dual-estimation approach provides the first empirical validation of the alignment tax geometry framework. We further hypothesize:\n(i) Both α_repr and α_frontier are smaller in agent vs. chat settings (reflecting higher entanglement), providing geometric explanation for Plaut's approximately linear frontier — the ellipse degenerates toward a line as α → 0. Plaut's models (8B–14B) with 2 β values lacked both the representation analysis to verify this and sufficient sweep resolution to distinguish a low-angle ellipse from a line.\n(ii) MoE models show different frontier shapes than dense models due to routing-mediated safety — the all-layer LoRA comparison isolates this, while the ablations reveal whether routing-respecting training protocols improve or worsen the tax.\n(iii) Regression of geometric measurements (MSO, α_repr, effective rank, routing divergence for MoE) against α_frontier and downstream safety metrics establishes whether entanglement geometry is predictive of alignment tax severity — making the geometric framework empirically actionable.\n\n**Scope note:** We deliberately exclude an intervention phase (entanglement-adapted OGPSA or NSPO) that was in an earlier version of this proposal. That line of work — adapting null-space projection methods for entangled subspaces — is a full study in its own right and would dilute the measurement contributions. We instead focus on rigorous measurement and geometric explanation, providing the empirical foundation that any future intervention (OGPSA, NSPO, or ShaPO-style geometry-aware optimization) would need.\n\n## Inspiration\nField guide Section 4.1 (pass@1 vs. production gap) + the convergent pattern: (a) the formal alignment tax geometry needs entanglement-robust metrics for empirical validation, (b) Plaut's near-linear agentic frontier needs geometric explanation (our framework predicts: high entanglement → small α → near-linear ellipse), (c) the MoE safety routing literature needs geometric formalization, and (d) null-space projection methods (NSPO, OGPSA) need entanglement-aware adaptation. These four bridges converge in one study.\n\n## Key References\n- What Is the Geometry of the Alignment Tax? (arXiv 2603.00047, Mar 2026)\n- Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study (arXiv 2505.14185, ICLR 2026)\n- The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025)\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv 2603.02229, Mar 2026, Plaut)\n- Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization [NSPO] (arXiv 2512.11391, ICLR 2026)\n- Safety Alignment as Continual Learning via Orthogonal Gradient Projection [OGPSA] (arXiv 2602.07892, Feb 2026)\n- The Autonomy Tax: Defense Training Breaks LLM Agents (arXiv 2026)\n- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety (arXiv 2602.16943, Feb 2026)\n- Why Does Agentic Safety Fail to Generalize Across Tasks? (arXiv 2605.06992, May 2026)\n- RASA: Routing-Aware Safety Alignment for MoE Models (arXiv 2602.04448, Feb 2026)\n- SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs (arXiv 2506.17368)\n- Sparse Models, Sparse Safety (arXiv 2602.08621, Feb 2026)\n- Geometric Routing Enables Causal Expert Control in MoE (arXiv 2604.14434, Apr 2026)\n- Grassmannian MoE (arXiv 2602.17798, Feb 2026)\n- Sparse Crosscoders for diffing MoEs and Dense models (arXiv 2603.05805, Mar 2026)\n- Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696, Feb 2026)\n- The Geometry of Alignment Collapse (arXiv 2602.15799, Feb 2026)\n- ShaPO: Selective Geometry Control for Safety Alignment (arXiv 2602.07340, Feb 2026)\n- Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026)\n- Steering Externalities (arXiv 2026)\n- The Verifier Tax (arXiv 2026)\n- When Safety Geometry Collapses (arXiv 2605.02914, May 2026)\n- The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026)\n- OpenAgentSafety (ICLR 2026)\n- ATBench (arXiv 2604.02022, Apr 2026)\n- Multi-Agent Security Tax (arXiv 2025)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '1,600 (4×H100 for dense models, 8×H100 for MoE: Phase 1 activation extraction 4 models × 2 settings × ~25 hr = 200 hr; Phase 2 MoE routing analysis 2 models × 60 hr = 120 hr; Phase 3 primary Pareto sweep 4 models × 2 settings × 12 β × ~5 hr = 480 hr; Phase 3 MoE ablation 2 models × 2 settings × 8 β × ~5 hr = 160 hr; agent evaluation on tau2-bench + OpenAgentSafety + ATBench = 200 hr; infrastructure debugging + reruns = 440 hr buffer)', 'timeline': '14 weeks (wk 1–2 infrastructure + trajectory generation; wk 2–5 entanglement geometry extraction; wk 4–7 MoE routing analysis; wk 6–11 Pareto sweeps + ablations; wk 12–14 analysis, regression, writing)', 'estimated_gpu_cost': '$4,800 at ~$3.00/GPU-hr average (mix of spot at $1.67–$2.50/hr for H100 SXM and on-demand for debugging)'}\n- **human_in_loop**: {'gpu_hours': '1,450 (Claude-assisted probe code, MSO computation scripts, routing analysis, and Bayesian model comparison saves ~150 hr of manual iteration)', 'timeline': '12 weeks', 'claude_api_cost': '$700 (Sonnet 4.6 at $3/$15 per M tokens: ~35M input + 10M output tokens for MSO/principal-angle implementation, routing analysis scripts, WAIC computation, analysis notebooks)', 'estimated_gpu_cost': '$4,350 at ~$3.00/GPU-hr average'}\n- **auto_research**: {'gpu_hours': '1,450', 'timeline': '8 weeks', 'claude_api_cost': '$2,800 (Opus 4.7 at $5/$25 per M tokens: ~130M input + 40M output for autonomous sweep management, routing analysis, MSO computation, Bayesian model comparison, result interpretation, draft writing)', 'estimated_gpu_cost': '$4,350 at ~$3.00/GPU-hr average', 'speed_bottleneck': 'Sequential LoRA-DPO fine-tuning within each Pareto sweep (each run ~5 GPU-hr on 4–8×H100; β values can be parallelized across cluster but limited by GPU allocation); MoE routing analysis requires loading full 235B/400B models'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T20:51:32.947Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T20:51:32.947Z",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T20:51:32.961Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make an informed assessment. Let me compile my findings.

---

```
【阶段】: Triage

【重大前置问题 — 投稿目标与 Proposal 内容严重不匹配】

CoRL 2026 (Conference on Robot Learning, Austin, TX, Nov 10–12, 2026) 的 Call for Papers 明确要求：
• "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
• "Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."

本 Proposal 研究的是 LLM alignment tax 的几何结构、safety-capability subspace 的 entanglement、MoE 路由对安全性的影响，使用的 benchmark (ToolEmu, OpenAgentSafety, ATBench, tau2-bench) 全部是 LLM 软件工具调用场景，与机器人学习没有任何关系。该 Proposal 不涉及任何 robotic manipulation、navigation、locomotion、sim-to-real transfer、embodied AI 等 CoRL 核心主题。

⚠️ 这构成了 desk rejection 级别的致命问题。该 Proposal 适合的会议是 NeurIPS / ICML / ICLR / AAAI（AI safety track）或 ACL / EMNLP（如果有 safety alignment 相关 track），绝非 CoRL。

以下评估将同时给出：(A) 针对 CoRL 的概率，(B) 假设投稿到适配会议（NeurIPS/ICML/ICLR 级别 ML 会议）的 idea 质量评估。


【领域调研】:

1. [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026):
   提出 alignment tax 的几何理论框架——在线性表示假设下，safety-capability 的 Pareto frontier 是由 principal angle α 参数化的椭圆。纯理论工作，作者自己承认"对大扰动、非线性编码，框架不成立"。本 Proposal 的核心理论基础。

2. [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026):
   引入 MSO (Mode Subspace Overlap) 量化 safety-capability subspace 的 entanglement。发现 safety 与 general learning 高度纠缠，在 Llama 2/3.2 和 Qwen 2.5 (1B–7B) 上验证，仅限 chat 场景。本 Proposal 的第二核心依据。

3. [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (Plaut, Mar 2026):
   在 agentic DPO 中发现近线性 Pareto frontier (R²=0.77, slope −0.83)，使用 Llama 3.1 8B / Qwen 2.5 7B / Phi 4 14B，仅 2 个 β 值，无表示分析，无 MoE 对比。本 Proposal 试图为其提供几何解释。

4. [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448) (Feb 2026):
   识别 MoE 中 safety-critical experts，发现全参数微调产生 routing 捷径——恢复原始 routing 后 harmlessness 大幅下降。本 Proposal 的 MoE 分析基础之一。

5. [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621) (Feb 2026):
   引入 RoSais 分数，mask 5 个 router 可使 ASR 提高 4 倍至 0.79，揭示 MoE 安全的脆弱性。

6. [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026):
   将 safety gradient 投影到 capability null space，实现 SOTA safety 而不损失 capability。假设 subspace 可分——恰好是 MSO 论文证伪的假设。

7. [OGPSA](https://arxiv.org/abs/2602.07892) (Feb 2026):
   类似思路，将 safety gradient 投影到 capability subspace 的正交补上。

- **调研总结**: 2026 年上半年，alignment tax 的几何理论、safety subspace entanglement、MoE safety routing、agentic safety 四条线已各自成型但相互独立。本 Proposal 试图做"桥梁"——在 agentic + MoE 条件下用 entanglement-aware 方法实证验证几何理论。这个 positioning 是清晰的，但本质上是一个 measurement/validation study（测量 + 验证已有理论），而非提出新理论或新方法。


【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

核心 claim 是"高 entanglement → 小 α → 近线性 frontier，这解释了 Plaut 的观察"。一个成本更低的替代方案是：
(1) 直接在 Plaut 的设置上增加 β sweep 点数（从 2 增加到 12），拟合椭圆 vs 线性，提取 α_frontier——这不需要 MoE、不需要 entanglement 测量，大约是本 Proposal GPU 开销的 1/5；
(2) 在同样的模型上跑 MSO 分析——这在原始 MSO 论文的框架内可以直接完成，不需要新方法论。

本 Proposal 的增量价值在于：
- 2×2 factorial design（dense × MoE × chat × agent）的系统性
- Dual-estimation test（α_repr vs α_frontier 的一致性）
- MoE routing-specific 分析

但这些增量价值更多是**实验设计的系统性**而非**idea 的概念创新**。如果 trivial baseline（扩展 Plaut + 扩展 MSO 论文到更大模型）就能得到 80% 的 insight，剩下 20% 的边际贡献是否足以支撑一篇顶会？这是核心问题。


【前提假设检验】:

核心 claim 的逻辑链条中，以下环节是"想当然"的：

1. **线性表示假设在 agentic 场景下成立**：几何理论的作者自己承认框架在大扰动下失效。Agentic tool-use 涉及多步决策、工具调用，其表示空间的非线性程度远高于 chat。如果线性假设不成立，α_repr 和 α_frontier 的 dual-estimation test 的逻辑前提就崩塌了。
   
2. **MSO 在 agentic 场景下可被有意义地计算**：MSO 原始论文在 chat setting 的 1B–7B 模型上验证。在 agentic 场景中，safety subspace 的定义本身就更模糊（tool-call safety vs. text safety），提取 activation 的"决策点"选择（tool-call 前一 token）是否能准确捕获 safety subspace 是未经验证的假设。

3. **Entanglement → 小 α 的因果方向**：Proposal 假设高 entanglement 导致小 principal angle，但这两者可能只是同一现象的不同度量，而非因果关系。如果 MSO 和 α 本质上是同一信息的不同表达，那"dual-estimation test"就变成了 tautology 而非 validation。

4. **Dense vs MoE 在 matched active parameters 下可公平比较**：MoE 的 routing 机制意味着不同 token 激活不同的 expert subsets，这使得"subspace"的定义在 MoE 和 dense 之间本质不同。matched active parameters 不等于 matched representation capacity。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是将已有理论框架（2603.00047 的几何理论）、已有度量方法（ICLR 2026 的 MSO）、已有经验观察（Plaut 的近线性 frontier）组合在新场景（agentic + MoE）中进行实证验证。没有提出新的理论工具、新的度量方法或新的算法。"Dual-estimation test"（α_repr vs α_frontier）有一定方法论新颖性，但本质上是对已有理论的验证实验设计，而非概念创新。Proposal 自己也承认排除了 intervention phase——这意味着即使测量结论全部成立，也没有 actionable 的新方法产出。
   
   与最相关工作的差异：相对于 2603.00047（理论无实证）+ 2505.14185（chat 无 agentic）+ Plaut（无表示分析无 MoE），增量是"在更大范围内做更系统的测量"。这是一种 extension novelty，不是 conceptual novelty。

2. **Significance: 中** — 
   如果 dual-estimation test 成功验证（α_repr ≈ α_frontier），这为几何理论框架提供了第一个实证支撑，有一定价值。但核心预测（高 entanglement → 近线性 frontier）是理论的直接推论，审稿人大概率会说 "I would have guessed this"。MoE 分析如果发现质性不同的 frontier 形状，会更有 surprise value，但这是 dual-outcome 设计中的"乐观场景"。
   
   作为一个 measurement study，其影响力取决于：(a) 是否有后续工作会基于这些测量结果开发新方法，(b) 社区是否真的需要这种验证。考虑到 NSPO 和 OGPSA 已经在"假设 subspace 可分"的前提下取得了 SOTA 结果，实证证明"其实不可分"的价值可能被"但方法照样 work"所削弱。

3. **Related Work: 强** — 
   覆盖极其全面，引用了 25+ 篇高度相关的 2025–2026 工作，定位清晰。文献调研是这个 Proposal 最强的维度。每条研究线的总结准确，gap 的识别合理。搜索验证了所引论文均真实存在且描述准确（2603.00047, 2505.14185, 2603.02229, 2512.11391, 2602.04448, 2602.08621 等均可查证）。


【概率估计】:

(A) **CoRL 2026: 0-2%，中位 1%**
   — 投稿目标与 Proposal 内容完全不匹配，极大概率 desk rejection。

(B) **假设投稿到适配会议（NeurIPS/ICML/ICLR AI Safety track）: 15-25%，中位 20%**

【估计理由】:
Idea 内核是一个系统性 measurement study，将已有理论、已有度量、已有经验观察组合在新场景中验证。Related Work 覆盖强，实验设计系统（但这是执行层面的优势，不影响 idea 上限评估）。Novelty 是限制上界的核心瓶颈——缺乏概念创新，核心预测不够 surprising（"高 entanglement 导致近线性 frontier"是理论的直接推论）。存在显著 trivial alternative 威胁（扩展 Plaut + 扩展 MSO 即可获得大部分 insight）。前提假设中线性表示假设在 agentic 场景下是否成立是一个未解决的根本问题，如果不成立则整个框架的基础动摇。

【主要风险】:
1. **Venue mismatch (致命)**: CoRL 是机器人学习会议，本 Proposal 与机器人学无关，几乎确定 desk rejection。
2. **Novelty 不足 (idea 层面)**: 即使在适配会议，"在新场景中系统性验证已有理论"的 contribution level 可能被审稿人认为是 incremental extension，而非独立的 conceptual contribution。核心发现若 positive，审稿人反应更可能是 "confirms what the theory predicted" 而非 "surprising"。
```

---

**总结建议**：

这个 Proposal 的**文献调研和实验设计**做得非常扎实，但有两个根本性问题：

1. **投稿目标错误**：必须更换到 NeurIPS / ICML / ICLR 等 ML 安全相关会议。投 CoRL 几乎不可能中稿。

2. **Idea 内核是 measurement/validation study，缺乏概念创新**：如果作者能增加 intervention component（例如 entanglement-aware 的 NSPO/OGPSA 改进方法，并证明其优于原始方法），novelty 和 significance 都会显著提升。当前 Proposal 明确排除了这一部分，这限制了其贡献的天花板。

Sources:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)
- [Safety Subspaces are Not Linearly Distinct (ICLR 2026)](https://arxiv.org/abs/2505.14185)
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229)
- [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448)
- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621)
- [NSPO (ICLR 2026)](https://arxiv.org/abs/2512.11391)
- [OGPSA](https://arxiv.org/abs/2602.07892)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━


━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to provide my assessment. Let me compile the analysis.

---

```
【阶段】: Triage

【⚠️ 致命前置问题：会议 Scope 不匹配】

在进入 idea 质量评估之前，必须首先指出一个**致命的venue选择问题**：

CoRL 2026 (Conference on Robot Learning) 的 Call for Papers 明确声明：
"submissions without a robotics focus will be returned without review"

本 proposal 的全部内容是 LLM 对齐税的几何理论在 dense/MoE 架构上的实证验证——
涉及 alignment tax geometry、safety-capability subspace entanglement、LoRA-DPO β sweeps——
**没有任何机器人学习内容**。没有机器人实验、没有 sim-to-real、没有机器人控制/感知/操作。
所谓"agentic tool-use"是指 LLM 调用软件工具（ToolEmu、tau2-bench），不是机器人工具操作。

**这篇论文提交 CoRL 会被 desk reject。** 这不是 idea 质量问题，而是根本性的 scope mismatch。

合适的目标会议：NeurIPS 2026、ICLR 2027、ICML 2026（如果 deadline 未过）。

以下评估假设投稿至一个 scope 合适的 ML/AI Safety 顶会（如 NeurIPS 2026），对 idea 质量本身进行客观打分。

---

【领域调研】:

1. [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026):
   纯理论工作，证明 alignment tax 的 Pareto frontier 是由 safety/capability subspace 间 principal angle α 参数化的椭圆。作者自己承认框架在 "large perturbations" 下失效（KL 不是二次的，representation geometry 会 shift）。**没有任何实证验证**。本 proposal 的核心目标之一是提供首个实证验证——这个 gap 是真实的。

2. [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026):
   引入 MSO 度量 safety-capability entanglement，发现 useful 和 safety updates 的 subspace 高度重叠。但仅在 chat setting 上测试（Llama 2/3.2, Qwen 2.5, 1B-7B）。本 proposal 正确识别了需要将其扩展到 agentic setting 和更大模型的 gap。

3. [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (arXiv, Mar 2026, Plaut):
   在 agentic DPO 设置下观察到近线性 Pareto frontier（R²=0.77, slope -0.83）。但仅用 2 个 β 值，无 representation analysis，无 MoE 对比。本 proposal 正确识别了这个观察缺乏几何解释的 gap。

4. [RASA: Routing-Aware Safety Alignment for MoE](https://arxiv.org/abs/2602.04448) (Feb 2026):
   识别 safety-critical experts，发现 full-parameter MoE safety fine-tuning 创建 routing shortcuts——恢复原始 routing 后 harmlessness 崩溃 Δ ∈ [-0.38, -0.46]。与本 proposal 的 MoE routing analysis 直接相关但不竞争——RASA 是 intervention，本 proposal 是 measurement。

5. [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025):
   发现多维正交 safety directions——dominant refusal direction + interpretable secondary features。仅在 chat setting, Llama 3 8B 上验证。

6. [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026) & [OGPSA](https://arxiv.org/abs/2602.07892) (Feb 2026):
   两种 null-space projection 方法都假设 safety/capability subspaces 可分——恰好是 MSO 论文证伪的假设。本 proposal 正确指出了这个矛盾。

7. 直接竞争工作搜索结果：**未发现**已有工作在 entanglement-aware metrics 下测量 agentic settings 的 alignment tax geometry，也未发现 dense vs. MoE alignment tax 结构对比。

- **调研总结**: 领域中存在四条独立研究线——(a) alignment tax 的几何理论（纯理论，无验证），(b) safety subspace entanglement（仅 chat），(c) agentic Pareto frontier 观察（无几何解释），(d) MoE safety routing（无 alignment tax geometry 联系）。本 proposal 的"桥接"定位在文献中确实是空白的。但这个空白的性质更多是"自然延伸的实证补全"，而非"意外的概念突破"。

---

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

最直接的简化替代方案：在 Plaut 的实验基础上，仅需 (1) 增加 β 值数量（如 12 个），(2) 在同一模型上跑 MSO + principal angle 计算，(3) 拟合椭圆 vs. 线性模型并提取 α_frontier。这个方案大约占本 proposal 贡献的 60-70%，但工程成本不到 1/4。

本 proposal 的增量价值在于：
- 2×2 factorial design（dense × MoE × chat × agent）——MoE routing 分析是 trivial alternative 无法覆盖的
- Dual-estimation test（α_repr vs α_frontier 一致性）——这是方法论上的贡献
- Per-expert subspace analysis 和 routing divergence 分析

但核心发现的 *惊喜度* 是否因为增加了这些维度而本质提升？如果最终发现 "agents 确实 entanglement 更高、α 更小、frontier 更线性"——这正是理论的直接预测，审稿人会说 "I would have guessed this"。MoE 部分的发现可能更有惊喜度（routing 如何调制 tax 形状是未知的），但这取决于实验结果。

---

【前提假设检验】:

核心 claim 的逻辑链条中有多个未经验证的环节：

1. **MSO → principal angle α 的映射关系是假设的**。MSO 测量的是 SVD 产生的 top-K singular vectors 之间的 overlap，而 α 是 safety/capability subspaces 之间的 principal angle。这两者相关但不等价——proposal 同时计算两者并期望一致，但没有理论保证 MSO 高 ↔ α 小。这个映射本身需要验证而非假设。

2. **"高 Lipschitz complexity → 高 MSO" 是推测**。proposal 引用 "Why Does Agentic Safety Fail to Generalize" 的 Lipschitz 论证来预测 agents 有更高 entanglement，但 Lipschitz complexity 作用于函数空间，MSO 作用于 weight/activation subspace——两者之间的联系是直觉性的，不是严格推导。

3. **线性表示假设本身**。整个框架依赖于 safety 和 capability 可以被编码为线性方向——但 geometric theory 论文的作者自己承认框架在 large perturbations 下失效。在 MoE 架构中，routing 的非线性特性可能从根本上违反这个假设。

4. **12 个 β 值的统计功效**。proposal 选择 Bayesian model comparison (WAIC) 来避免频率主义检验在 n=12 时的低功效。但 WAIC 在仅 12 个数据点上区分 2-参数椭圆模型 vs. 2-参数线性模型的能力存疑——尤其当两者在低 α 时形状非常接近时（这恰好是 proposal 预测的情况）。

---

【3 维度打分】:

1. **Novelty: 中** — 
   "桥接"确实在文献中不存在（搜索未发现直接竞争工作），这是真实的。但桥接的性质是 **"将已有工具（MSO、principal angles、LoRA-DPO sweeps）应用到新 setting（agentic + MoE）"**——这是方法论组合创新，而非概念创新。Dual-estimation test（α_repr vs α_frontier）是最有方法论新意的点，但其成功取决于一个未经验证的假设（两个 α 应该一致）。与之对比，MSO 论文提出了新度量，geometric theory 论文推导了新理论——本 proposal 的 novelty delta 在于 empirical validation + architectural extension，这在 ML 顶会属于 solid but not surprising 级别。

2. **Significance: 中** — 
   研究问题是重要的——理解 alignment tax 的几何结构、MoE 如何调制 safety、agentic settings 的特殊性——这些都是社区关心的话题。但本 proposal 是 **measurement study**，不产出新方法或新理论。如果所有预测被验证（agents MSO 更高、α 更小、frontier 更线性），这 validates 已有理论——有价值，但影响力有限，因为结果方向是可预测的。如果 α_repr ≠ α_frontier（理论不成立），那是 negative result，更难发表但可能更有科学价值。MoE routing 对 tax geometry 的影响是唯一可能产生 "surprising" 发现的方向——但 proposal 在这里的预测最弱（"MoE shows different frontier shapes" 太模糊）。

3. **Related Work: 强** — 
   这是 proposal 最强的维度。Related work 的覆盖面极广（20+ 篇），包括了 geometric theory、subspace entanglement、agentic safety、MoE safety、null-space projection 等所有相关线索。差异化定位清晰——"四条线的桥接"。对每篇关键论文的局限性分析（chat only、no representation analysis、assumes separability）是准确的。唯一的小瑕疵：部分引用（如 "The Autonomy Tax"、"Steering Externalities"、"The Verifier Tax"）没有给出完整的 arXiv ID，可能需要验证。

---

【概率估计】: [20% - 32%] 中位 25%（假设投稿至 scope 合适的顶会如 NeurIPS 2026）

若投稿 CoRL 2026: [0% - 2%] 中位 0%（desk reject，scope 完全不匹配）

【估计理由】: 
对于 NeurIPS 等合适 venue：idea 的 "桥接" 定位是真实存在的文献空白，Related Work 覆盖全面且定位清晰，这些是加分项。但限制上界的核心因素是 **Novelty 和 Significance 的天花板**：(1) 核心贡献是 measurement/empirical validation，不是新方法或新理论；(2) 最可能的结果（agents 更 entangled, α 更小, frontier 更线性）是理论的直接预测，审稿人会说 "I would have guessed this"；(3) trivial alternative 威胁真实存在——简化版实验能获取大部分核心发现。这些因素将 idea 质量锚定在 25-35% 区间的低端。Related Work 的强势略做补偿，但无法弥补核心 novelty/significance 的中等水平。

对于 CoRL：完全没有机器人学习内容，会被 desk reject，概率实质为 0。

【主要风险】:
1. **"I would have guessed this" 风险**：核心预测（agents → 高 entanglement → 小 α → 线性 frontier）是已有理论的直接推论。如果实验完美验证了这个预测，审稿人可能认为 contribution 是 "running the experiment" 而非 "surprising insight"——这是 measurement study 面临的经典困境。
2. **统计不可区分风险**：proposal 预测 agent setting 下 α 很小、frontier 接近线性——但在 α 很小时，椭圆和线性模型在 12 个数据点上可能统计不可区分（WAIC 无法有效区分两个几乎相同形状的模型），从而使得 dual-estimation test 的核心方法论贡献失去说服力。
```

---

**补充说明（不属于正式评分格式）**：

关于 **CoRL 投稿**，我必须明确提醒：CoRL 2026 的 [Call for Papers](https://www.corl.org/contributions/call-for-papers) 明确要求提交必须有 robotics focus，否则 "returned without review"。本 proposal 100% 是 LLM alignment/safety 的 representation geometry 研究，没有任何机器人实验或机器人学习内容。建议将目标会议改为 **NeurIPS 2026**（deadline 通常在 5 月底）或 **ICLR 2027**。上述概率评估均基于投稿至 scope 合适的 ML/AI 顶会。

Sources:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)
- [Safety Subspaces are Not Linearly Distinct (ICLR 2026)](https://arxiv.org/abs/2505.14185)
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut)](https://arxiv.org/abs/2603.02229)
- [RASA: Routing-Aware Safety Alignment for MoE](https://arxiv.org/abs/2602.04448)
- [The Hidden Dimensions of LLM Alignment (ICML 2025)](https://arxiv.org/abs/2502.09674)
- [NSPO (ICLR 2026)](https://arxiv.org/abs/2512.11391)
- [OGPSA](https://arxiv.org/abs/2602.07892)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings

## Description
The alignment tax has been formalized geometrically with elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces. But empirically, these subspaces are highly entangled (ICLR 2026), MoE architectures route safety through sparse expert dynamics, and in agentic settings Plaut (2603.02229) already observes a near-linear frontier (R²=0.77) without geometric explanation. We hypothesize a unifying account: high safety-capability entanglement in agents yields small α, degenerating the ellipse toward linearity — and MoE routing introduces architectural modulation absent in dense models. We conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agents. Using a 2×2 design — {Qwen3-32B, Gemma 4 31B} (dense) × {Qwen3-235B-A22B, Llama-4-Maverick} (MoE) in {chat, agent} — we measure entanglement via MSO, multi-dimensional safety decomposition, and principal angles (yielding α_repr). For MoE models, we add per-expert subspace analysis, routing distribution divergence, and router safety importance scoring. We sweep 12 LoRA-DPO β values per condition with matched trainable parameters across architectures (plus MoE-specific ablations), using Bayesian model comparison (WAIC) to distinguish elliptic, linear, and piecewise-linear frontiers, extracting α_frontier. The dual-estimation test — whether α_repr agrees with α_frontier — provides the first empirical validation of the geometric alignment tax framework. Expected: (1) higher MSO in agents vs. chat; (2) α_repr ≈ α_frontier with both smaller in agents (explaining Plaut's near-linear frontier as a low-angle ellipse); (3) MoE routing-mediated safety fragility absent in dense models; (4) the geometric framework becoming actionable for predicting alignment tax severity from representation measurements alone.

## Core Problem
The alignment tax — the safety-capability tradeoff — has been formalized geometrically under the linear representation hypothesis, yielding elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces. However, three empirical challenges prevent direct application: (1) Safety Subspaces are Not Linearly Distinct (ICLR 2026) shows safety and capability subspaces are highly entangled, with Mode Subspace Overlap (MSO) strongest between useful and safety-specific updates; (2) frontier open-weight models are predominantly Mixture-of-Experts architectures where safety is governed by sparse expert routing dynamics (RASA, SAFEx, Sparse Models Sparse Safety), not global activation subspaces; (3) in agentic tool-use settings, both challenges intensify — text safety does not transfer to tool-call safety (Mind the GAP), and the safe controller mapping has inherently higher Lipschitz complexity (Why Does Agentic Safety Fail to Generalize). Critically, Plaut (2603.02229) already measured an approximately linear Pareto frontier (R²=0.77, slope −0.83) in agentic DPO on 8B–14B models — but with only two β values, no representation analysis, and no MoE comparison, providing an empirical observation without geometric explanation. The theoretical framework predicts that when the principal angle α is small (i.e., when safety and capability subspaces are highly entangled), the elliptic frontier degenerates toward linearity. The field thus has a frontier shape observation that awaits geometric explanation, entanglement measurements that have not been tested in agents or MoE models, and a theoretical bridge between entanglement degree and frontier geometry that has never been validated empirically.

## Opportunity
Four independent lines of work create a convergence point whose bridge is missing. The Geometry of the Alignment Tax (Mar 2026) provides the formal apparatus — principal angles, elliptic Pareto frontiers, tax rate decomposition — but assumes linear separability, static representations, and dense architectures, with the author explicitly noting the framework fails 'for large perturbations, the KL is not quadratic, the representation geometry shifts.' Safety Subspaces are Not Linearly Distinct (ICLR 2026) proves the separability assumption fails empirically by quantifying safety-capability entanglement via MSO, but only studies chat settings on models up to 7B. The Hidden Dimensions of LLM Alignment (ICML 2025) reveals multi-dimensional orthogonal safety directions with interpretable secondary features, but likewise only in chat on Llama 3 8B. Plaut (Mar 2026) discovers a near-linear Pareto frontier in agentic DPO, which the geometric theory predicts should occur when α is small — but Plaut used only 8B–14B dense models with 2 β values and provided no representation analysis to verify this geometric explanation. Meanwhile, the MoE safety literature (RASA, SAFEx, Sparse Models Sparse Safety, Geometric Routing) establishes that safety operates through routing dynamics — safety-critical experts, routing distribution divergence, expert silencing vulnerabilities — but none connects to the alignment tax geometry. And the null-space projection literature (NSPO at ICLR 2026, OGPSA) mitigates the alignment tax by projecting safety gradients into capability null spaces, but assumes those subspaces are separable — precisely the assumption MSO disproves. The missing bridge connects: (a) entanglement-aware geometric measurement to the theoretical framework, (b) architecture-aware analysis to capture how MoE routing mediates the tax differently from dense models, and (c) agentic empirics to verify whether high entanglement geometrically explains the near-linear frontier Plaut observed.

## Related Work / Landscape
The Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) proves the Pareto frontier is an ellipse ΔS = ΔC cos α + sin α √(B² − ΔC²) parameterized by the principal angle α, but the paper is purely theoretical with no empirical validation, and acknowledges the framework fails under large perturbations or nonlinear encoding. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) introduces MSO quantifying safety-capability entanglement; strongest overlap is between useful and safety updates on Llama 2/3.2 and Qwen 2.5 (1B–7B) — chat only. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions with a dominant refusal direction plus interpretable secondary features — chat only, Llama 3 8B. Safety Training Persists Through Helpfulness Optimization (arXiv 2603.02229, Mar 2026, Plaut) finds an approximately linear Pareto frontier (R²=0.77, slope −0.83) across 180 DPO training configurations on Llama 3.1 8B, Qwen 2.5 7B, and Phi 4 14B using ToolEmu (144 tasks); uses only β ∈ {0.05, 0.1}, no representation analysis, no MoE models — the frontier shape is observed but not geometrically explained. NSPO (arXiv 2512.11391, ICLR 2026) projects safety gradients into the null space of the capability covariance matrix KK⊤, achieving SOTA safety without capability degradation on Llama3-8B and Qwen2.5-7B — but assumes separable subspaces. OGPSA (arXiv 2602.07892, Feb 2026) similarly projects safety gradients onto the orthogonal complement of a capability subspace, improving the safety-utility Pareto frontier. Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696) shows safety regions are dataset-dependent with low IoU across safety datasets, complementing the entanglement finding. The Geometry of Alignment Collapse (arXiv 2602.15799) shows alignment concentrates in low-dimensional subspaces with sharp curvature, creating brittle structure where second-order gradient effects systematically steer into alignment-sensitive regions. ShaPO (arXiv 2602.07340) enforces geometry-aware preference optimization via selective geometry control over alignment-critical parameter subspace, demonstrating token-level and reward-level geometric stabilization. Sparse Crosscoders (arXiv 2603.05805) provides crosscoder-based methods for comparing MoE and dense model representations, finding MoEs learn fewer but more specific features than dense models at matched active parameters. The Autonomy Tax (Mar 2026) shows 99% timeout rates from agent safety training. Mind the GAP (arXiv 2602.16943, Feb 2026) demonstrates text-tool safety divergence across 17,420 datapoints. Why Does Agentic Safety Fail to Generalize (arXiv 2605.06992, May 2026) proves the safe controller has higher Lipschitz constant than task execution. RASA (arXiv 2602.04448, Feb 2026) identifies safety-critical experts via Adversarial Activation Discrepancy and shows full-parameter MoE safety fine-tuning creates routing dominance artifacts — when original routing is restored in fully fine-tuned models, harmlessness collapses by Δ ∈ [−0.38, −0.46], proving safety was achieved through routing shortcuts not genuine expert repair. SAFEx shows disabling 12 of 6,144 experts drops refusal rate 22%. Sparse Models Sparse Safety (arXiv 2602.08621, Feb 2026) introduces RoSais scores: masking 5 routers increases ASR 4× to 0.79. Geometric Routing (arXiv 2604.14434, Apr 2026) demonstrates monosemantic experts with frequency-to-syntax gradient. Grassmannian MoE (arXiv 2602.17798, Feb 2026) provides subspace-manifold routing. Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026) characterizes theoretical tradeoff limits. The Verifier Tax (Mar 2026) and Steering Externalities (Feb 2026) provide further agentic alignment tax evidence. When Safety Geometry Collapses (arXiv 2605.02914, May 2026) demonstrates safety geometry destruction in guard models. The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026) confirms sharp safety degradation in tool-enabled agents. ATBench (arXiv 2604.02022, Apr 2026) provides paired safe/unsafe trajectory construction methodology via planner-based synthesis with 1,000 trajectories across 1,954 tools. No existing work measures alignment tax geometry under entanglement-aware metrics in agentic settings, provides geometric explanation for the observed near-linear frontier in agents, or compares dense vs. MoE alignment tax structure.

## Approach
We conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agentic tool-use settings, using a 2×2 factorial design: {dense, MoE} × {chat, agent}. The study has three phases producing three core contributions: entanglement measurement, MoE routing analysis, and geometrically-explained Pareto frontier mapping.

**Model Selection (2 dense + 2 MoE, matched on active parameters):**
- Dense: Qwen3-32B (32.8B active, Qwen3 family), Gemma 4 31B (31B, Apache 2.0)
- MoE: Qwen3-235B-A22B (22B active / 235B total, Qwen3 family), Llama-4-Maverick (17B active / 400B total)
The Qwen3 dense/MoE pair enables within-family comparison isolating routing effects.

**Phase 1: Entanglement Geometry Measurement (wk 1–5)**

*Trajectory Construction (addressing methodological specification):*
For agent settings, we construct paired safe/unsafe trajectories using two complementary sources: (i) OpenAgentSafety's 350+ executable tasks with rule-based safety evaluators across 8 risk categories — we run each model to generate trajectories, then classify via the framework's evaluators; (ii) ATBench's planner-based paired trajectory synthesis methodology, which generates matched safe/unsafe trajectory pairs sharing identical task setups with controlled risk injection points (avg. 9 turns, 1,954 tools). For capability subspace extraction, we use tau2-bench policy-adherence tasks, extracting activations from successful vs. failed completions. Activations are extracted at tool-call decision points — the token positions immediately preceding tool-call generation — following the step-specific extraction methodology from LLM Reasoning as Trajectories (2604.05655), which demonstrated that activations at decision boundaries form linearly separable, step-specific subspaces. For chat baseline, we use AdvBench/BeaverTails prompts matching the original MSO paper's methodology.

*Entanglement Metrics:*
(a) Mode Subspace Overlap (MSO): following Safety Subspaces are Not Linearly Distinct, we compute MSO between safety and capability update subspaces via SVD overlap matrices. We test whether MSO is higher in agent vs. chat settings, as predicted by the higher Lipschitz complexity of safe agentic control.
(b) Multi-dimensional safety decomposition: following Hidden Dimensions, we identify the dominant refusal direction and orthogonal secondary directions, testing whether agent settings activate additional safety dimensions absent in chat (e.g., tool-execution safety, multi-step consequence reasoning).
(c) Principal angles via SVD on cross-covariance matrices: critically reinterpreted as coupling strength rather than separability indicators. Small angles indicate strong entanglement. We compute α_repr (representation-derived principal angle) as the first output of this analysis, which will later be compared to α_frontier (the angle estimated from Pareto frontier fitting).

**Phase 2: Architecture-Aware MoE Routing Analysis (wk 4–7, overlapping)**
For MoE models, we decompose analysis into three levels:
(a) Shared attention layers: analogous to dense-model analysis, providing a controlled comparison point.
(b) Per-expert FFN subspaces: extract safety/capability subspaces within individual expert networks, identifying safety-critical experts via Adversarial Activation Discrepancy (following RASA's methodology) between safe/unsafe trajectories. We apply Sparse Crosscoders (2603.05805) to compare feature organization between MoE and dense models, testing whether MoE's 'fewer but more specific features' pattern extends to safety representations.
(c) Router weight space: compute routing distribution divergence (KL divergence of expert selection probabilities) between safe/unsafe inputs in chat vs. agent contexts. Test whether routing divergence is smaller in agent settings (indicating safety routing is more fragile under tool-use). Apply RoSais-style router safety importance scoring to identify which layers' routing is most safety-critical.

**Phase 3: Pareto Frontier Mapping with Geometric Explanation (wk 6–11)**

*Addressing the confounded comparison:* We use a two-tier design:
- Primary comparison ('apples-to-apples'): LoRA-DPO applied to all layers for BOTH dense and MoE models, with LoRA rank adjusted to match total trainable parameter count across architectures. This isolates architectural effects from training protocol effects.
- MoE-specific ablation: For MoE models only, we additionally run (i) shared-attention-only LoRA and (ii) active-expert-only LoRA (HELLoRA-style, targeting top-k activated experts). This tests whether MoE-specific training protocols change frontier shape, decomposing the total architecture effect into routing-mediated vs. representation-mediated components.

*Statistical approach (addressing power concerns):* We sweep 12 LoRA-DPO β values per model/setting combination (β ∈ {0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0}, with increased resolution in the high-gradient region identified in preliminary coarse sweeps). Rather than frequentist goodness-of-fit tests (which lack power at n=12), we use Bayesian model comparison via WAIC to compare three frontier models: (i) elliptic (2 free parameters: α, B), (ii) linear (2 parameters: slope, intercept), (iii) piecewise-linear (allowing discrete expert-switching thresholds in MoE). From the elliptic fit, we extract α_frontier.

*Core hypothesis connecting Phases 1 and 3:* The key prediction is that α_repr (measured from representation geometry in Phase 1) and α_frontier (estimated from Pareto frontier shape in Phase 3) should agree if the geometric theory holds under entanglement. This dual-estimation approach provides the first empirical validation of the alignment tax geometry framework. We further hypothesize:
(i) Both α_repr and α_frontier are smaller in agent vs. chat settings (reflecting higher entanglement), providing geometric explanation for Plaut's approximately linear frontier — the ellipse degenerates toward a line as α → 0. Plaut's models (8B–14B) with 2 β values lacked both the representation analysis to verify this and sufficient sweep resolution to distinguish a low-angle ellipse from a line.
(ii) MoE models show different frontier shapes than dense models due to routing-mediated safety — the all-layer LoRA comparison isolates this, while the ablations reveal whether routing-respecting training protocols improve or worsen the tax.
(iii) Regression of geometric measurements (MSO, α_repr, effective rank, routing divergence for MoE) against α_frontier and downstream safety metrics establishes whether entanglement geometry is predictive of alignment tax severity — making the geometric framework empirically actionable.

**Scope note:** We deliberately exclude an intervention phase (entanglement-adapted OGPSA or NSPO) that was in an earlier version of this proposal. That line of work — adapting null-space projection methods for entangled subspaces — is a full study in its own right and would dilute the measurement contributions. We instead focus on rigorous measurement and geometric explanation, providing the empirical foundation that any future intervention (OGPSA, NSPO, or ShaPO-style geometry-aware optimization) would need.

## Inspiration
Field guide Section 4.1 (pass@1 vs. production gap) + the convergent pattern: (a) the formal alignment tax geometry needs entanglement-robust metrics for empirical validation, (b) Plaut's near-linear agentic frontier needs geometric explanation (our framework predicts: high entanglement → small α → near-linear ellipse), (c) the MoE safety routing literature needs geometric formalization, and (d) null-space projection methods (NSPO, OGPSA) need entanglement-aware adaptation. These four bridges converge in one study.

## Key References
- What Is the Geometry of the Alignment Tax? (arXiv 2603.00047, Mar 2026)
- Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study (arXiv 2505.14185, ICLR 2026)
- The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025)
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv 2603.02229, Mar 2026, Plaut)
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

## Resource Estimate
- **manual**: {'gpu_hours': '1,600 (4×H100 for dense models, 8×H100 for MoE: Phase 1 activation extraction 4 models × 2 settings × ~25 hr = 200 hr; Phase 2 MoE routing analysis 2 models × 60 hr = 120 hr; Phase 3 primary Pareto sweep 4 models × 2 settings × 12 β × ~5 hr = 480 hr; Phase 3 MoE ablation 2 models × 2 settings × 8 β × ~5 hr = 160 hr; agent evaluation on tau2-bench + OpenAgentSafety + ATBench = 200 hr; infrastructure debugging + reruns = 440 hr buffer)', 'timeline': '14 weeks (wk 1–2 infrastructure + trajectory generation; wk 2–5 entanglement geometry extraction; wk 4–7 MoE routing analysis; wk 6–11 Pareto sweeps + ablations; wk 12–14 analysis, regression, writing)', 'estimated_gpu_cost': '$4,800 at ~$3.00/GPU-hr average (mix of spot at $1.67–$2.50/hr for H100 SXM and on-demand for debugging)'}
- **human_in_loop**: {'gpu_hours': '1,450 (Claude-assisted probe code, MSO computation scripts, routing analysis, and Bayesian model comparison saves ~150 hr of manual iteration)', 'timeline': '12 weeks', 'claude_api_cost': '$700 (Sonnet 4.6 at $3/$15 per M tokens: ~35M input + 10M output tokens for MSO/principal-angle implementation, routing analysis scripts, WAIC computation, analysis notebooks)', 'estimated_gpu_cost': '$4,350 at ~$3.00/GPU-hr average'}
- **auto_research**: {'gpu_hours': '1,450', 'timeline': '8 weeks', 'claude_api_cost': '$2,800 (Opus 4.7 at $5/$25 per M tokens: ~130M input + 40M output for autonomous sweep management, routing analysis, MSO computation, Bayesian model comparison, result interpretation, draft writing)', 'estimated_gpu_cost': '$4,350 at ~$3.00/GPU-hr average', 'speed_bottleneck': 'Sequential LoRA-DPO fine-tuning within each Pareto sweep (each run ~5 GPU-hr on 4–8×H100; β values can be parallelized across cluster but limited by GPU allocation); MoE routing analysis requires loading full 235B/400B models'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0f7ab747-0884-4312-9108-b6da9125a67a",
  "type": "user",
  "uuid": "e0fc4757-ff61-4d76-b8ee-51a312985246",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T20:51:32.959Z_

```json
{
  "parentUuid": "e0fc4757-ff61-4d76-b8ee-51a312985246",
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
  "uuid": "72c16234-4cbb-408c-b521-a63bc784191b",
  "timestamp": "2026-05-19T20:51:32.959Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T20:51:32.959Z_

```json
{
  "parentUuid": "72c16234-4cbb-408c-b521-a63bc784191b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "27e39294-b817-4828-935d-683f8ca3fb05",
  "timestamp": "2026-05-19T20:51:32.959Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make an informed assessme…",
  "leafUuid": "27e39294-b817-4828-935d-683f8ca3fb05",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge assessment of LLM alignment tax geometry proposal",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771"
}
```

---

### Assistant

_source line 8 · 2026-05-19T20:52:01.150Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully.

I notice that only Reviewer 1 and Reviewer 3 provided their evaluations. Reviewer 2's section is empty. Let me work with what I have.

Wait, looking again:
- 审稿人 1: Full evaluation provided
- 审稿人 2: Empty (no content between the headers)
- 审稿人 3: Full evaluation provided

So I only have 2 out of 3 reviewers. I need to address this. Let me proceed with what I have.

Actually, the user asked me to synthesize 3 reviewers' evaluations. 

Reviewer 2 is missing, so I'm working with just the two available reviews. Reviewer 1 rates the novelty as weak-to-medium with medium significance, flags a fatal venue mismatch, and estimates only 1% median probability for CoRL but 20% for top-tier venues, citing concerns about the measurement study's lack of conceptual innovation and questionable assumptions about linearity in agentic systems. Reviewer 3 assesses novelty as medium and is starting to evaluate significance, but the assessment cuts off there.

Both reviewers converge on the same critical problem: this paper doesn't fit CoRL's scope and would face a desk reject, though they see stronger potential at venues like NeurIPS with acceptance probabilities around 20-25%. The core issues are the venue mismatch, medium novelty, and medium significance across the board. agree
4. **Related Work: strong** - both agree
5. **Measurement study nature** - both identify this as the core limitation
6. **Trivial alternative threat** - both identify this
7. **"I would have guessed this" risk** - both mention
8. **Assumption validity concerns** - both raise linearity assumption issues

Differences:
- R1 is slightly more negative on novelty (weak-medium vs medium)
- R3 has a slightly higher upper bound (32% vs 25%)
- R3 specifically raises the statistical power concern about WAIC at n=12 with similar shapes

Since I only have 2 of 3 reviewers, I need to note this limitation. The two available reviews are highly convergent.

Looking at the medians of 20% and 25%, that gives me a mean around 22.5% with a standard deviation of about 3.5% — medium consistency overall. With only two reviewers providing signals, I should lean toward being more conservative in my assessment.

I notice R2 is missing entirely, which I need to flag since the instructions asked for three independent evaluations. This reduces my confidence somewhat, so I'll work with what I have from the two available reviews and adjust accordingly.

For CoRL specifically, both reviewers are aligned at essentially 0-1% — a desk reject verdict that's unanimous and decisive. On the question of appropriate venue, the two medians of 20% and 25% suggest this work might find a home elsewhere, though the limited sample size means I should be cautious about over-interpreting this signal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27e39294-b817-4828-935d-683f8ca3fb05",
  "isSidechain": false,
  "requestId": "req_011CbCb7wkj2KFiA3h26N5tv",
  "type": "assistant",
  "uuid": "96b9974b-44c0-4811-860e-50efca3331d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5Lin77z56BWvuxVfHNiFP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21105,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3996,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3996,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 21105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21105
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

_source line 9 · 2026-05-19T20:53:08.768Z_

【阶段】: Meta Judge

【⚠️ 前置说明】: 审稿人 2 未提交评审内容（空白），仅有审稿人 1 和审稿人 3 的完整评审可用。以下综合基于 2 份独立评审，信号量不足 3 份时偏保守处理。

【三次中位】: [20%, ——, 25%] (仅 2 份有效) std=3.5%（两点估计）

【共识维度】（2/2 审稿人同时提到）:
- **Venue Mismatch: 致命** — 两位审稿人均独立判定 proposal 与 CoRL 2026 scope 完全不匹配（LLM alignment geometry vs. robot learning），一致认定 desk rejection。引用了相同的 CoRL CFP 原文（"submissions without a robotics focus will be returned without review"）。**最高置信共识。**
- **Novelty: 弱-中 / 中** — 两位均判定核心贡献是 measurement/empirical validation study，缺乏概念创新。R1 给"弱-中"，R3 给"中"，分歧在一个半档内。两位均指出"将已有工具应用到新 setting"属于 extension novelty 而非 conceptual novelty。
- **Significance: 中** — 完全一致。两位均指出核心预测方向可预测（"I would have guessed this"），measurement study 的 impact 天花板有限。
- **Related Work: 强** — 完全一致。两位均认为这是 proposal 最强维度，文献覆盖极其全面（20-25+ 篇相关工作），差异化定位清晰。
- **Trivial Alternative 威胁: 显著** — 两位均独立构造了相同的简化替代方案（扩展 Plaut β sweep + 直接跑 MSO），且均估计该简化方案能获取 60-80% 的核心 insight。
- **前提假设风险: 多个** — 两位均质疑：(1) 线性表示假设在 agentic 场景下的有效性；(2) MSO 与 principal angle α 之间映射的非平凡性；(3) dense vs. MoE 匹配比较的公平性。R3 额外提出 WAIC 在 n=12 时的统计功效问题。

【异常维度】（仅 1 人提到）:
- R1 独有：明确提出"MSO 和 α 可能是同一现象的不同度量"→ dual-estimation test 可能是 tautology。这是一个严重质疑，但仅 R1 提出，降权但保留为风险项。
- R3 独有：WAIC 在 n=12 + 低 α（椭圆≈线性）时统计不可区分的风险 → dual-estimation test 方法论贡献的核心说服力可能丧失。这是对实验设计关键环节的精准打击，虽仅 1 人提，但技术论证充分，不应降权。
- R1 独有：将 novelty 判为"弱-中"而非"中"，理由是"排除 intervention phase 意味着无 actionable 方法产出"。R3 虽也注意到但给了"中"。差异 ≤ 半档，不构成重大分歧。

【最终概率】:
- **CoRL 2026（原定投稿目标）**: [0% - 2%] 中位 0%
- **适配会议（NeurIPS/ICML/ICLR AI Safety track）**: [16% - 27%] 中位 21%

【一致性】: 高（两位审稿人在所有核心维度的判决方向完全一致，概率估计 std=3.5%，Novelty 分歧仅半档）

【综合理由】:

**1. CoRL 概率（0%）**：两位审稿人的判决完全一致且论据确凿——proposal 研究的是 LLM alignment tax geometry，使用的全部是软件工具调用 benchmark（ToolEmu, tau2-bench, OpenAgentSafety, ATBench），没有任何机器人实验、sim-to-real、embodied AI 内容。CoRL CFP 明确声明无 robotics focus 的稿件"returned without review"。这是一个 **desk rejection 级别的致命 scope mismatch**，无法通过修改 proposal 内容来补救（除非彻底重构为 robotics 方向，但那将是完全不同的工作）。

**2. 适配会议概率（中位 21%）的推导**：

*Novelty 天花板*：两位一致认定核心贡献是"在新 setting 中用已有工具做系统性测量"，属 extension novelty。R1 给弱-中，R3 给中。综合取中偏严 → **弱-中到中**。Dual-estimation test 有一定方法论新意，但 R1 的 tautology 质疑和 R3 的统计功效质疑均指向该贡献的脆弱性。Novelty 弱-中到中 → 概率上界约 30%。

*Significance 约束*：两位一致给"中"。Measurement study 的 impact 取决于结果是否 surprising，但两位均指出核心预测方向可预测。中 significance → 不额外降低但也不提升 Novelty 设定的天花板。

*Related Work 加分*：两位一致给"强"。这是实打实的加分项——审稿人不太会在 related work 维度给负面意见，减少了一个被攻击面。

*Trivial Alternative 减分*：两位独立构造了相同的简化替代，这意味着审稿人 very likely 也会构造出来。这对 novelty 是严重压力 → 在中位附近偏下。

*前提假设风险*：多个核心假设未验证（线性表示假设、MSO-α 映射、统计功效），如果审稿人深入追问，defense 困难。

*仅有 2 份评审的保守调整*：缺少第三份独立信号，无法确认是否存在两位均遗漏的维度。按"宁缺毋滥"原则，综合中位从两份的算术均值 22.5% 向下微调至 21%。

*最终区间*：取 R1 下界 15% 和 R3 上界 32% 作为参考，因一致性高可缩窄 → [16% - 27%]，中位 21%。

【建议】: 不推荐（投 CoRL）/ 边缘偏下（投适配会议，需重大修改）

**具体建议**：
1. **必须更换投稿目标**。CoRL 完全不可行。NeurIPS 2026（deadline 通常 5 月底）或 ICLR 2027 是合理选择。
2. **如继续推进（投适配会议）**，两位审稿人的共识指向同一个核心改进方向：**增加 intervention component**。当前 proposal 明确排除了 entanglement-aware NSPO/OGPSA 改进，这限制了 novelty 和 significance 的天花板。如果能加入"基于 entanglement 测量结果，设计 entanglement-aware 的 null-space projection 方法并证明其优于 vanilla NSPO/OGPSA"，将从 measurement study 升级为 measurement + method，概率估计可上移 8-12 个百分点。
3. **统计功效问题需在实验前解决**：R3 指出的 WAIC 在 n=12 + 低 α 时不可区分的风险是实验设计的硬伤。应考虑增加 β sweep 点数（至少 20 个）或引入补充统计方法。

【实施评估】:
- **计算资源**: 约 1,450-1,600 GPU-hr（H100），需 4×H100 用于 dense 模型、8×H100 用于 MoE 模型（235B/400B 全模型加载）。预估 GPU 费用 $4,350-$4,800。MoE 模型的显存需求是主要瓶颈（Qwen3-235B 和 Llama-4-Maverick 需 8×H100 80GB）。
- **数据需求**: 依赖 4 个公开 benchmark（ToolEmu、OpenAgentSafety、ATBench、tau2-bench）及标准 safety 评测集（AdvBench、BeaverTails）。均为公开可得数据集，无数据获取障碍。
- **人工介入**: 中等。需要人工设计 MSO 计算 pipeline、routing analysis 脚本、Bayesian model comparison 框架。Trajectory 分类依赖 OpenAgentSafety 的自动评估器，人工标注需求较低。但实验调试和结果解读需要对 representation geometry 有深入理解的研究者。
- **训练需求**: 需要训练。每个模型 × 每个 setting × 12 个 β 值 = 96 次 LoRA-DPO fine-tuning run（主实验），加 MoE 消融约 32 次。单次 LoRA-DPO 约 5 GPU-hr。不需要从头预训练，但 fine-tuning 总量可观。
- **新 Benchmark**: 不需要构建新 benchmark。使用现有公开 benchmark 组合。
- **预估周期**: 12-14 周（约 3-3.5 个月）。关键路径：wk 1-2 基础设施 → wk 2-5 entanglement 测量 → wk 4-7 MoE routing 分析 → wk 6-11 Pareto sweep → wk 12-14 分析写作。Phase 2 和 Phase 3 有部分重叠。如增加 intervention component（建议项），需额外 4-6 周。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96b9974b-44c0-4811-860e-50efca3331d0",
  "isSidechain": false,
  "requestId": "req_011CbCb7wkj2KFiA3h26N5tv",
  "type": "assistant",
  "uuid": "51a1b153-7c82-4601-aa86-6b68cafea097",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5Lin77z56BWvuxVfHNiFP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21105,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3996,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3996,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 21105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21105
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make an informed assessme…",
  "leafUuid": "51a1b153-7c82-4601-aa86-6b68cafea097",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge assessment of LLM alignment tax geometry proposal",
  "sessionId": "1c0cfc61-25c1-4170-bfb9-ac84c7674771"
}
```

---
