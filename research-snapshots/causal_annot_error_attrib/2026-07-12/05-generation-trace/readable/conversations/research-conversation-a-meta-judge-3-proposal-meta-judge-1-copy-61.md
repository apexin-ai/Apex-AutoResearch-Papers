# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/3b60e073-7297-4ac8-a7e7-fc2e804856dd.jsonl`
- **Structured JSON:** [`9eb09acdc41bd0e27581.json`](../../sessions/9e/9eb09acdc41bd0e27581.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:29:35.647Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:29:35.647Z",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to evaluate this proposal. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv Mar 2026, Robin Young): 本 proposal 的理论基础。纯理论论文，推导出 alignment tax 的椭圆 Pareto 前沿由 safety-capability 子空间间的主角 α 参数化。作者明确承认框架在大扰动下失效（\"the KL is not quadratic, the representation geometry shifts\"），且无任何实证验证。\n- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026, CERT-Lab): 引入 MSO (Mode Subspace Overlap) 量化 safety-capability 纠缠度。关键发现：safety 子空间与 useful update 子空间高度重叠，无法线性分离。仅在 Llama 2/3.2, Qwen 2.5 (1B–7B) 的 chat 设定下验证。\n- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (Mar 2026, Plaut): 在 agentic DPO 中观察到近线性 Pareto 前沿 (R²=0.77, slope −0.83)。仅用 β∈{0.05, 0.1} 两个值，8B–14B dense 模型，无表征分析，无几何解释。\n- [RASA: Routing-Aware Safety Alignment for MoE](https://arxiv.org/abs/2602.04448) (Feb 2026): 发现 MoE 全参数安全微调会产生 routing dominance artifacts（恢复原始 routing 后 harmlessness 下降 0.38–0.46），证明安全通过 routing shortcuts 而非 expert repair 实现。\n- [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026): 将 safety gradients 投影到 capability null space，假设子空间可分离——正是 MSO 论文反驳的假设。\n- [OGPSA](https://arxiv.org/html/2602.07892v1) (Feb 2026): 类似正交梯度投影方法，同样假设子空间可分离。\n- 调研总结: 该领域形成了\"理论框架(Young) + 纠缠测量(MSO) + agentic观察(Plaut) + MoE安全(RASA/SAFEx)\"四条平行线，且确认**无现有工作**将这四条线桥接——proposal 定位的 gap 是真实存在的。\n\n【Trivial Alternative 检验】:\n最直接的 trivial alternative：直接对 Plaut 的工作进行扩展——用更多 β 值做 DPO sweep，拟合曲线区分线性/椭圆，不需要任何表征几何分析。这能回答\"前沿形状是什么\"但无法回答\"为什么是这个形状\"。本 proposal 的增量价值核心在 **dual-estimation test**（α_repr vs α_frontier 是否一致）——这是对几何理论的因果验证，而非单纯的曲线拟合。这确实不可被 trivial baseline 替代。但需注意：如果 dual-estimation 结果是\"一致\"，审稿人可能认为这只是 confirmation（\"the theory works as predicted\"），surprise 有限。\n\n【前提假设检验】:\n1. **线性表征假设在 agentic 设定下仍近似成立**：整个框架依赖于 safety/capability 可以用线性子空间表征。原理论作者明确指出框架在大扰动下失效。Agentic 设定涉及多步推理、工具调用，非线性度显然更高——该假设未经验证且可能在 agent 设定下恰好最不成立。\n2. **LoRA-DPO β sweep 能产生足够的前沿变异**：12 个 β 值是否足以用 WAIC 区分椭圆 vs 线性？椭圆退化为直线的判别需要高曲率区域的精确采样，但高 β 区域训练可能不稳定。\n3. **Tool-call decision point 的 activation 捕捉相关几何**：假设在工具调用前的 token position 提取的 activation 就是 safety/capability trade-off 发生的\"正确位置\"——这是方法论假设，无先验支持。\n4. **Dense 和 MoE 的 LoRA matched-parameter 对比是 \"apples-to-apples\"**：MoE 的 LoRA 作用于 22B active parameters vs dense 的 32B 全参数，matched trainable params 不等于 matched effective capacity。\n\n【3 维度打分】:\n1. Novelty: 中 — Gap 是真实存在的（调研确认无现有工作同时覆盖 entanglement-aware + architecture-controlled + agentic geometry）。Dual-estimation test 是方法论上的真实创新。但核心贡献性质是\"用已有方法(MSO, principal angles)在新设定(agents, MoE)验证已有理论(Young 2603.00047)\"——是 empirical validation + extension，非 new theory 或 new method。类比：如果 Young 的理论是 Newton's law，本文是\"在水中验证牛顿定律也成立\"——有价值但 novelty 天花板有限。\n\n2. Significance: 中 — 如果结果 positive（α_repr ≈ α_frontier，theory works），实际意义是\"可以从表征测量预测 alignment tax 严重程度，无需跑完整 DPO sweep\"——这是有实用价值的。MoE vs dense 对比也 timely。但 proposal 明确排除了 intervention（不做 entanglement-adapted NSPO/OGPSA），所以贡献停留在 descriptive/diagnostic 层面，不直接改变 alignment 实践。如果结果 negative（theory fails in agents），贡献是 negative result——对 ICLR 可以接受但影响力更低。\n\n3. Related Work: 强 — 覆盖极为全面（~30篇），定位清晰，四条平行线的汇聚叙事 compelling。每篇引用的论文经验证均真实存在且描述准确。唯一潜在遗漏：multi-objective alignment 的 HoE (Hierarchical Experts) 工作与 MoE alignment 相关但未提及。\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \n- Novelty 是\"中\"而非\"强\"：核心是 empirical validation of an existing framework in new settings。审稿人看到 positive results 时最可能的反应是\"nice confirmation, the theory works as expected\"而非 \"surprising\"。这直接限制了上界（不进入 35%+ 区间）。\n- Significance 是\"中\"：pure measurement paper without intervention，停留在 diagnostic。\n- Related Work 是\"强\"：叙事清晰，gap 真实，这撑起了下界（不低于 25%）。\n- MoE routing 分析有潜力产生 surprise（如发现 routing-mediated fragility 的具体几何机制），但这恰是最不确定的部分。\n- 上界主要受限于 Novelty 维度：contributes a validation, not a new paradigm。\n\n【主要风险】:\n1. **\"Confirmation without surprise\" 风险**：如果 dual-estimation 一致、agents 确实有更高 MSO 和更小 α，审稿人可能评价为\"verifies what theory already predicted\"——incremental validation 而非 new insight。核心问题：验证别人的理论在新设定下成立，这个贡献量级是否够一篇 top venue paper？\n2. **线性表征假设在 agentic 设定下可能恰好失效**：如果 agent 的多步推理使 safety/capability 表征本质上非线性，则整个框架的前提崩塌。这不仅是 negative result，而是 undermines the entire methodology——dual-estimation 失败不是因为\"theory wrong\"而是\"measurement tool inappropriate\"，难以得出清晰结论。\n```\n\nSources:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)\n- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185)\n- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229)\n- [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448)\n- [Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization](https://arxiv.org/abs/2512.11391)\n- [OGPSA: Safety Alignment as Continual Learning](https://arxiv.org/html/2602.07892v1)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【重要前置说明 — 投稿会议匹配度】:\n本 proposal 的目标会议为 ICLR 2027 / AAAI 2027 / ICML 2027（proposal 原文明确列出）。\n然而用户要求评估的是 **CoRL 2026**（Conference on Robot Learning）。\nCoRL 的 scope 聚焦于 robot learning、manipulation、locomotion、sim-to-real transfer、robot perception 等，\n与本 proposal 的主题（LLM alignment tax 的几何结构、safety-capability 表征子空间纠缠度量）**完全不匹配**。\n本 proposal 在 CoRL 属于 **scope 外 desk reject**，中稿概率接近 0%。\n\n以下评估基于该 idea 在其**合理目标会议**（ICLR / ICML / NeurIPS 等 AI/ML 主会）的质量，\n以便后续流程判断是否值得立项。同时在最终概率估计中给出 CoRL 的独立评估。\n\n======================================================================\n\n【领域调研】:\n\n1. [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026):\n   本 proposal 的理论骨架来源。该文在线性表征假设下证明了\n   safety-capability tradeoff 的 Pareto 前沿为椭圆，参数化\n   于 safety/capability 子空间的 principal angle α。纯理论工作，\n   作者自己承认\"大扰动下 KL 非二次、表征几何会漂移\"，\n   无任何实证验证。\n\n2. [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026):\n   引入 Mode Subspace Overlap (MSO) 度量 safety/capability 子空间\n   的纠缠程度。在 Llama 2/3.2、Qwen 2.5（1B–7B）上实验，\n   仅 chat setting。证明 safety 子空间与 useful update 子空间\n   高度重叠——子空间分离假设不成立。\n\n3. [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025):\n   在 Llama 3 8B 上发现多维正交 safety 方向——主 refusal 方向\n   + 可解释的次级方向（假设叙事、角色扮演等）。仅 chat，单模型。\n\n4. [Safety Training Persists Through Helpfulness Optimization](https://arxiv.org/abs/2603.02229) (Plaut, Mar 2026):\n   在 agentic DPO 中观察到近线性 Pareto 前沿（R²=0.77, slope −0.83），\n   模型为 Llama 3.1 8B / Qwen 2.5 7B / Phi 4 14B，仅用 β∈{0.05, 0.1}，\n   无表征分析、无 MoE。**关键数据点**，但分辨率不足以区分\n   low-angle ellipse vs. true line。\n\n5. [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026):\n   将 safety 梯度投影到 capability 协方差矩阵的零空间，\n   实现 safety 不降低 capability 的 SOTA。**假设子空间可分离**\n   ——恰好是 MSO 论文所推翻的假设。\n\n6. [OGPSA](https://arxiv.org/abs/2602.07892) (Feb 2026):\n   类似思路，正交梯度投影。同样假设可分离。\n\n7. [RASA](https://arxiv.org/abs/2602.04448) (Feb 2026):\n   识别 safety-critical experts，证明全参 MoE fine-tune\n   通过 routing shortcuts 达到\"安全\"但恢复原始 routing 后\n   safety 崩溃（Δ ∈ [−0.38, −0.46]）。\n\n8. [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621) (Feb 2026):\n   引入 RoSais score，mask 5 routers → ASR 增加 4× 至 0.79。\n   MoE safety 高度依赖少数 routing pathway。\n\n9. 调研总结:\n   该领域目前处于\"理论框架刚出、实证验证空白、MoE 安全\n   独立发展但未连接几何理论\"的阶段。Proposal 瞄准的桥接\n   方向（entanglement-aware geometry × MoE × agentic）确实\n   没有现有工作覆盖。但这是一个 **measurement/validation study**\n   而非 method paper，其价值取决于度量结果能否产生超出\n   直觉预期的洞见。\n\n\n【Trivial Alternative 检验】:\n\n存在更简单的替代路径：\n(a) 直接在 Plaut 的设置上增加 β sweep 密度（从 2 → 12+）并做\n    ellipse vs. line 的 model comparison，即可回答\"agentic 前沿\n    是否为低角度椭圆\"——不需要 MSO、不需要 α_repr、不需要\n    MoE comparison。这是一个 ~200 GPU-hr 的实验。\n(b) 类似地，直接在 chat vs. agent 上测 MSO 差异（延伸 ICLR 2026\n    论文到 agent setting）也是一个独立且更轻量的贡献。\n\nProposal 的增量价值在于 **dual-estimation test**（α_repr ≈ α_frontier）\n—— 这是唯一不能被 trivial decomposition 替代的部分，因为它\n同时需要表征分析和前沿拟合。但审稿人可能会问：这个 agreement\n如果成立，说明什么？如果不成立，又说明什么？前者是 \"theory works\nas expected\"（not surprising），后者是 \"theory breaks under\nentanglement\"（interesting but negative）。核心发现的 upside\n并不高。\n\n\n【前提假设检验】:\n\n核心逻辑链中有以下未验证假设：\n\n1. **线性表征假设在 agent 激活上仍然成立**。原理论框架基于\n   线性表征假设（safety/capability 编码在线性子空间）。\n   在 chat 单轮设置下这个假设有一定实证基础，但在多步\n   agentic trajectory 中，激活的提取点（\"tool-call decision\n   points\"）是否仍满足线性可分离性，完全未知。如果不满足，\n   整个 principal angle 测量和椭圆拟合都失去意义。\n\n2. **LoRA-DPO β sweep 能产生有意义的 Pareto 前沿**。仅通过\n   β 值变化来 trace 前沿，隐含假设 β 是 safety-capability\n   tradeoff 的唯一/主要控制变量。但 DPO 前沿的形状可能\n   更多受 data composition、LoRA rank、learning rate schedule\n   影响而非 β。Plaut 的 R²=0.77 本身就说明有 23% 的方差\n   未被解释。\n\n3. **Active-parameter matching = 公平比较**。Proposal 声称\n   通过匹配 trainable parameter count 来隔离架构效应，但\n   dense 32B 和 MoE 22B-active/235B-total 的计算图、梯度流、\n   representation capacity 根本不同。匹配 LoRA rank 只能\n   控制一个维度。\n\n4. **12 个数据点足以用 WAIC 区分三个模型**。虽然 proposal\n   选择了 Bayesian 方法而非频率检验，但 12 个 β 点 fit 2-参数\n   椭圆 vs. 2-参数线性 vs. 分段线性，自由度非常有限。\n   α_frontier 的估计不确定性可能很大，以至于 dual-estimation\n   test 不具有判别力。\n\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   理由：桥接方向（entanglement geometry × agentic × MoE）\n   确实目前无人做过——调研确认不存在直接竞争工作。但 novelty\n   的本质是\"将已有工具 A（MSO/principal angles）应用到新设置 B\n   （agents + MoE）并验证已有理论 C（椭圆前沿）是否成立\"。\n   这是 **methodological extension** 而非 **conceptual innovation**。\n   MSO 来自 [Safety Subspaces](https://arxiv.org/abs/2505.14185)，\n   椭圆理论来自 [Geometry of Alignment Tax](https://arxiv.org/abs/2603.00047)，\n   MoE routing 分析框架来自 [RASA](https://arxiv.org/abs/2602.04448) /\n   [Sparse Models Sparse Safety](https://arxiv.org/abs/2602.08621)。\n   Proposal 的原创方法论贡献仅限于 dual-estimation test 的\n   设计——这是 clever 但不 deep。与 ICLR 2026 的 MSO 论文相比，\n   novelty delta 主要在 setting extension 而非 insight depth。\n\n2. Significance: 【中偏弱】\n   理由：\n   - 正面：alignment tax 是重要问题；理解其几何结构有实际价值\n     （指导 NSPO/OGPSA 等方法的改进）；MoE 已成为 frontier\n     model 的主流架构，理解其 safety 机制有现实意义。\n   - 负面：这是一个 **纯度量论文**，proposal 自己明确排除了\n     intervention phase。度量论文的 significance 取决于度量结果\n     的 surprise factor。但核心预测（agent 比 chat 纠缠更高、\n     线性前沿是低角度椭圆的退化、MoE routing 引入脆弱性）\n     **全部是直觉上\"I would have guessed this\"的方向**。即使\n     结果完美 positive，审稿人的反应更可能是\"nice confirmation\"\n     而非\"surprising insight\"。\n   - 此外，proposal 无法回答 \"so what\"——得到了 α_repr ≈ α_frontier，\n     然后呢？能指导什么实际决策？Proposal 最后提到\"predicting\n     alignment tax severity from representation measurements alone\"，\n     但这需要 α_repr → downstream safety metric 的 predictive\n     regression 在多个模型上有强泛化性，12 个数据点难以证明。\n\n3. Related Work: 【强】\n   理由：文献覆盖非常全面。调研确认所有引用的关键论文\n   （[2603.00047](https://arxiv.org/abs/2603.00047),\n   [2505.14185](https://arxiv.org/abs/2505.14185),\n   [2502.09674](https://arxiv.org/abs/2502.09674),\n   [2603.02229](https://arxiv.org/abs/2603.02229),\n   [2512.11391](https://arxiv.org/abs/2512.11391),\n   [2602.04448](https://arxiv.org/abs/2602.04448),\n   [2602.08621](https://arxiv.org/abs/2602.08621)）\n   均真实存在且描述准确。差异化定位清晰——明确说明了\n   每篇先前工作覆盖了什么、缺失了什么。这是 proposal 最强的\n   维度。\n\n\n【概率估计】:\n\n对合理目标会议（ICLR / ICML / NeurIPS）:\n  [18% - 28%] 中位 22%\n\n对 CoRL 2026:\n  [0% - 3%] 中位 1%（scope 完全不匹配，desk reject）\n\n【估计理由】:\nIdea 内核是\"将已有度量工具在新设置上做验证性实验\"。\n方向正确、文献扎实、execution plan 详尽，这些保证了下限不会太低。\n但 **Significance 维度限制了上界**：核心发现即使完全 positive，\n审稿人大概率认为是 \"confirmatory measurement, not surprising\"。\nNovelty 是 methodological extension 而非 conceptual leap，\ndual-estimation test 有巧思但不足以将整个工作提升到 strong accept。\n一个纯度量论文需要 surprising result 来中顶会——而这个 proposal\n的所有预测方向都太符合直觉。\n\n此外，CoRL 2026 是 robot learning 会议（manipulation, locomotion,\nsim-to-real, robot perception），本 proposal 的 LLM alignment\nsafety 主题完全不在其 scope 内，投稿几乎必然 desk reject。\n\n【主要风险】:\n1. **\"Confirmatory, not insightful\" 质疑**：审稿人最可能的 reject\n   理由是——如果 entanglement 高则前沿近线性，这正是理论的\n   直接推论，验证它成立不构成 surprising contribution；验证它\n   不成立则理论 breaks 但 proposal 没有提供替代框架。\n2. **Scope overload 风险**：2×2 design × 12 β × MoE ablations ×\n   Bayesian model comparison × routing analysis × MSO × multi-dimensional\n   decomposition × principal angles —— 单篇论文难以深入每个维度，\n   极可能被审稿人批评为\"a mile wide and an inch deep\"。\n```\n\nSources:\n- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)\n- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185)\n- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674)\n- [Safety Training Persists Through Helpfulness Optimization](https://arxiv.org/abs/2603.02229)\n- [NSPO: Null-Space Constrained Policy Optimization](https://arxiv.org/abs/2512.11391)\n- [OGPSA: Safety Alignment as Continual Learning](https://arxiv.org/abs/2602.07892)\n- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448)\n- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\n\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings\n\n## Description\nThe alignment tax has been formalized geometrically with elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces. But empirically, these subspaces are highly entangled (ICLR 2026), MoE architectures route safety through sparse expert dynamics, and in agentic settings Plaut (2603.02229) already observes a near-linear frontier (R²=0.77) without geometric explanation. We hypothesize a unifying account: high safety-capability entanglement in agents yields small α, degenerating the ellipse toward linearity — and MoE routing introduces architectural modulation absent in dense models. We conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agents. Using a 2×2 design — {Qwen3-32B, Gemma 4 31B} (dense) × {Qwen3-235B-A22B, Llama-4-Maverick} (MoE) in {chat, agent} — we measure entanglement via MSO, multi-dimensional safety decomposition, and principal angles (yielding α_repr). For MoE models, we add per-expert subspace analysis, routing distribution divergence, and router safety importance scoring. We sweep 12 LoRA-DPO β values per condition with matched trainable parameters across architectures (plus MoE-specific ablations), using Bayesian model comparison (WAIC) to distinguish elliptic, linear, and piecewise-linear frontiers, extracting α_frontier. The dual-estimation test — whether α_repr agrees with α_frontier — provides the first empirical validation of the geometric alignment tax framework. Expected: (1) higher MSO in agents vs. chat; (2) α_repr ≈ α_frontier with both smaller in agents (explaining Plaut's near-linear frontier as a low-angle ellipse); (3) MoE routing-mediated safety fragility absent in dense models; (4) the geometric framework becoming actionable for predicting alignment tax severity from representation measurements alone.\n\n## Core Problem\nThe alignment tax — the safety-capability tradeoff — has been formalized geometrically under the linear representation hypothesis, yielding elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces. However, three empirical challenges prevent direct application: (1) Safety Subspaces are Not Linearly Distinct (ICLR 2026) shows safety and capability subspaces are highly entangled, with Mode Subspace Overlap (MSO) strongest between useful and safety-specific updates; (2) frontier open-weight models are predominantly Mixture-of-Experts architectures where safety is governed by sparse expert routing dynamics (RASA, SAFEx, Sparse Models Sparse Safety), not global activation subspaces; (3) in agentic tool-use settings, both challenges intensify — text safety does not transfer to tool-call safety (Mind the GAP), and the safe controller mapping has inherently higher Lipschitz complexity (Why Does Agentic Safety Fail to Generalize). Critically, Plaut (2603.02229) already measured an approximately linear Pareto frontier (R²=0.77, slope −0.83) in agentic DPO on 8B–14B models — but with only two β values, no representation analysis, and no MoE comparison, providing an empirical observation without geometric explanation. The theoretical framework predicts that when the principal angle α is small (i.e., when safety and capability subspaces are highly entangled), the elliptic frontier degenerates toward linearity. The field thus has a frontier shape observation that awaits geometric explanation, entanglement measurements that have not been tested in agents or MoE models, and a theoretical bridge between entanglement degree and frontier geometry that has never been validated empirically.\n\n## Opportunity\nFour independent lines of work create a convergence point whose bridge is missing. The Geometry of the Alignment Tax (Mar 2026) provides the formal apparatus — principal angles, elliptic Pareto frontiers, tax rate decomposition — but assumes linear separability, static representations, and dense architectures, with the author explicitly noting the framework fails 'for large perturbations, the KL is not quadratic, the representation geometry shifts.' Safety Subspaces are Not Linearly Distinct (ICLR 2026) proves the separability assumption fails empirically by quantifying safety-capability entanglement via MSO, but only studies chat settings on models up to 7B. The Hidden Dimensions of LLM Alignment (ICML 2025) reveals multi-dimensional orthogonal safety directions with interpretable secondary features, but likewise only in chat on Llama 3 8B. Plaut (Mar 2026) discovers a near-linear Pareto frontier in agentic DPO, which the geometric theory predicts should occur when α is small — but Plaut used only 8B–14B dense models with 2 β values and provided no representation analysis to verify this geometric explanation. Meanwhile, the MoE safety literature (RASA, SAFEx, Sparse Models Sparse Safety, Geometric Routing) establishes that safety operates through routing dynamics — safety-critical experts, routing distribution divergence, expert silencing vulnerabilities — but none connects to the alignment tax geometry. And the null-space projection literature (NSPO at ICLR 2026, OGPSA) mitigates the alignment tax by projecting safety gradients into capability null spaces, but assumes those subspaces are separable — precisely the assumption MSO disproves. The missing bridge connects: (a) entanglement-aware geometric measurement to the theoretical framework, (b) architecture-aware analysis to capture how MoE routing mediates the tax differently from dense models, and (c) agentic empirics to verify whether high entanglement geometrically explains the near-linear frontier Plaut observed.\n\n## Landscape\nThe Geometry of the Alignment Tax (arXiv 2603.00047, Mar 2026) proves the Pareto frontier is an ellipse ΔS = ΔC cos α + sin α √(B² − ΔC²) parameterized by the principal angle α, but the paper is purely theoretical with no empirical validation, and acknowledges the framework fails under large perturbations or nonlinear encoding. Safety Subspaces are Not Linearly Distinct (arXiv 2505.14185, ICLR 2026) introduces MSO quantifying safety-capability entanglement; strongest overlap is between useful and safety updates on Llama 2/3.2 and Qwen 2.5 (1B–7B) — chat only. The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025) reveals multi-dimensional orthogonal safety directions with a dominant refusal direction plus interpretable secondary features — chat only, Llama 3 8B. Safety Training Persists Through Helpfulness Optimization (arXiv 2603.02229, Mar 2026, Plaut) finds an approximately linear Pareto frontier (R²=0.77, slope −0.83) across 180 DPO training configurations on Llama 3.1 8B, Qwen 2.5 7B, and Phi 4 14B using ToolEmu (144 tasks); uses only β ∈ {0.05, 0.1}, no representation analysis, no MoE models — the frontier shape is observed but not geometrically explained. NSPO (arXiv 2512.11391, ICLR 2026) projects safety gradients into the null space of the capability covariance matrix KK⊤, achieving SOTA safety without capability degradation on Llama3-8B and Qwen2.5-7B — but assumes separable subspaces. OGPSA (arXiv 2602.07892, Feb 2026) similarly projects safety gradients onto the orthogonal complement of a capability subspace, improving the safety-utility Pareto frontier. Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696) shows safety regions are dataset-dependent with low IoU across safety datasets, complementing the entanglement finding. The Geometry of Alignment Collapse (arXiv 2602.15799) shows alignment concentrates in low-dimensional subspaces with sharp curvature, creating brittle structure where second-order gradient effects systematically steer into alignment-sensitive regions. ShaPO (arXiv 2602.07340) enforces geometry-aware preference optimization via selective geometry control over alignment-critical parameter subspace, demonstrating token-level and reward-level geometric stabilization. Sparse Crosscoders (arXiv 2603.05805) provides crosscoder-based methods for comparing MoE and dense model representations, finding MoEs learn fewer but more specific features than dense models at matched active parameters. The Autonomy Tax (Mar 2026) shows 99% timeout rates from agent safety training. Mind the GAP (arXiv 2602.16943, Feb 2026) demonstrates text-tool safety divergence across 17,420 datapoints. Why Does Agentic Safety Fail to Generalize (arXiv 2605.06992, May 2026) proves the safe controller has higher Lipschitz constant than task execution. RASA (arXiv 2602.04448, Feb 2026) identifies safety-critical experts via Adversarial Activation Discrepancy and shows full-parameter MoE safety fine-tuning creates routing dominance artifacts — when original routing is restored in fully fine-tuned models, harmlessness collapses by Δ ∈ [−0.38, −0.46], proving safety was achieved through routing shortcuts not genuine expert repair. SAFEx shows disabling 12 of 6,144 experts drops refusal rate 22%. Sparse Models Sparse Safety (arXiv 2602.08621, Feb 2026) introduces RoSais scores: masking 5 routers increases ASR 4× to 0.79. Geometric Routing (arXiv 2604.14434, Apr 2026) demonstrates monosemantic experts with frequency-to-syntax gradient. Grassmannian MoE (arXiv 2602.17798, Feb 2026) provides subspace-manifold routing. Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026) characterizes theoretical tradeoff limits. The Verifier Tax (Mar 2026) and Steering Externalities (Feb 2026) provide further agentic alignment tax evidence. When Safety Geometry Collapses (arXiv 2605.02914, May 2026) demonstrates safety geometry destruction in guard models. The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026) confirms sharp safety degradation in tool-enabled agents. ATBench (arXiv 2604.02022, Apr 2026) provides paired safe/unsafe trajectory construction methodology via planner-based synthesis with 1,000 trajectories across 1,954 tools. No existing work measures alignment tax geometry under entanglement-aware metrics in agentic settings, provides geometric explanation for the observed near-linear frontier in agents, or compares dense vs. MoE alignment tax structure.\n\n## Approach\nWe conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agentic tool-use settings, using a 2×2 factorial design: {dense, MoE} × {chat, agent}. The study has three phases producing three core contributions: entanglement measurement, MoE routing analysis, and geometrically-explained Pareto frontier mapping.\n\n**Model Selection (2 dense + 2 MoE, matched on active parameters):**\n- Dense: Qwen3-32B (32.8B active, Qwen3 family), Gemma 4 31B (31B, Apache 2.0)\n- MoE: Qwen3-235B-A22B (22B active / 235B total, Qwen3 family), Llama-4-Maverick (17B active / 400B total)\nThe Qwen3 dense/MoE pair enables within-family comparison isolating routing effects.\n\n**Phase 1: Entanglement Geometry Measurement (wk 1–5)**\n\n*Trajectory Construction (addressing methodological specification):*\nFor agent settings, we construct paired safe/unsafe trajectories using two complementary sources: (i) OpenAgentSafety's 350+ executable tasks with rule-based safety evaluators across 8 risk categories — we run each model to generate trajectories, then classify via the framework's evaluators; (ii) ATBench's planner-based paired trajectory synthesis methodology, which generates matched safe/unsafe trajectory pairs sharing identical task setups with controlled risk injection points (avg. 9 turns, 1,954 tools). For capability subspace extraction, we use tau2-bench policy-adherence tasks, extracting activations from successful vs. failed completions. Activations are extracted at tool-call decision points — the token positions immediately preceding tool-call generation — following the step-specific extraction methodology from LLM Reasoning as Trajectories (2604.05655), which demonstrated that activations at decision boundaries form linearly separable, step-specific subspaces. For chat baseline, we use AdvBench/BeaverTails prompts matching the original MSO paper's methodology.\n\n*Entanglement Metrics:*\n(a) Mode Subspace Overlap (MSO): following Safety Subspaces are Not Linearly Distinct, we compute MSO between safety and capability update subspaces via SVD overlap matrices. We test whether MSO is higher in agent vs. chat settings, as predicted by the higher Lipschitz complexity of safe agentic control.\n(b) Multi-dimensional safety decomposition: following Hidden Dimensions, we identify the dominant refusal direction and orthogonal secondary directions, testing whether agent settings activate additional safety dimensions absent in chat (e.g., tool-execution safety, multi-step consequence reasoning).\n(c) Principal angles via SVD on cross-covariance matrices: critically reinterpreted as coupling strength rather than separability indicators. Small angles indicate strong entanglement. We compute α_repr (representation-derived principal angle) as the first output of this analysis, which will later be compared to α_frontier (the angle estimated from Pareto frontier fitting).\n\n**Phase 2: Architecture-Aware MoE Routing Analysis (wk 4–7, overlapping)**\nFor MoE models, we decompose analysis into three levels:\n(a) Shared attention layers: analogous to dense-model analysis, providing a controlled comparison point.\n(b) Per-expert FFN subspaces: extract safety/capability subspaces within individual expert networks, identifying safety-critical experts via Adversarial Activation Discrepancy (following RASA's methodology) between safe/unsafe trajectories. We apply Sparse Crosscoders (2603.05805) to compare feature organization between MoE and dense models, testing whether MoE's 'fewer but more specific features' pattern extends to safety representations.\n(c) Router weight space: compute routing distribution divergence (KL divergence of expert selection probabilities) between safe/unsafe inputs in chat vs. agent contexts. Test whether routing divergence is smaller in agent settings (indicating safety routing is more fragile under tool-use). Apply RoSais-style router safety importance scoring to identify which layers' routing is most safety-critical.\n\n**Phase 3: Pareto Frontier Mapping with Geometric Explanation (wk 6–11)**\n\n*Addressing the confounded comparison:* We use a two-tier design:\n- Primary comparison ('apples-to-apples'): LoRA-DPO applied to all layers for BOTH dense and MoE models, with LoRA rank adjusted to match total trainable parameter count across architectures. This isolates architectural effects from training protocol effects.\n- MoE-specific ablation: For MoE models only, we additionally run (i) shared-attention-only LoRA and (ii) active-expert-only LoRA (HELLoRA-style, targeting top-k activated experts). This tests whether MoE-specific training protocols change frontier shape, decomposing the total architecture effect into routing-mediated vs. representation-mediated components.\n\n*Statistical approach (addressing power concerns):* We sweep 12 LoRA-DPO β values per model/setting combination (β ∈ {0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0}, with increased resolution in the high-gradient region identified in preliminary coarse sweeps). Rather than frequentist goodness-of-fit tests (which lack power at n=12), we use Bayesian model comparison via WAIC to compare three frontier models: (i) elliptic (2 free parameters: α, B), (ii) linear (2 parameters: slope, intercept), (iii) piecewise-linear (allowing discrete expert-switching thresholds in MoE). From the elliptic fit, we extract α_frontier.\n\n*Core hypothesis connecting Phases 1 and 3:* The key prediction is that α_repr (measured from representation geometry in Phase 1) and α_frontier (estimated from Pareto frontier shape in Phase 3) should agree if the geometric theory holds under entanglement. This dual-estimation approach provides the first empirical validation of the alignment tax geometry framework. We further hypothesize:\n(i) Both α_repr and α_frontier are smaller in agent vs. chat settings (reflecting higher entanglement), providing geometric explanation for Plaut's approximately linear frontier — the ellipse degenerates toward a line as α → 0. Plaut's models (8B–14B) with 2 β values lacked both the representation analysis to verify this and sufficient sweep resolution to distinguish a low-angle ellipse from a line.\n(ii) MoE models show different frontier shapes than dense models due to routing-mediated safety — the all-layer LoRA comparison isolates this, while the ablations reveal whether routing-respecting training protocols improve or worsen the tax.\n(iii) Regression of geometric measurements (MSO, α_repr, effective rank, routing divergence for MoE) against α_frontier and downstream safety metrics establishes whether entanglement geometry is predictive of alignment tax severity — making the geometric framework empirically actionable.\n\n**Scope note:** We deliberately exclude an intervention phase (entanglement-adapted OGPSA or NSPO) that was in an earlier version of this proposal. That line of work — adapting null-space projection methods for entangled subspaces — is a full study in its own right and would dilute the measurement contributions. We instead focus on rigorous measurement and geometric explanation, providing the empirical foundation that any future intervention (OGPSA, NSPO, or ShaPO-style geometry-aware optimization) would need.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,600 (4×H100 for dense models, 8×H100 for MoE: Phase 1 activation extraction 4 models × 2 settings × ~25 hr = 200 hr; Phase 2 MoE routing analysis 2 models × 60 hr = 120 hr; Phase 3 primary Pareto sweep 4 models × 2 settings × 12 β × ~5 hr = 480 hr; Phase 3 MoE ablation 2 models × 2 settings × 8 β × ~5 hr = 160 hr; agent evaluation on tau2-bench + OpenAgentSafety + ATBench = 200 hr; infrastructure debugging + reruns = 440 hr buffer)', 'timeline': '14 weeks (wk 1–2 infrastructure + trajectory generation; wk 2–5 entanglement geometry extraction; wk 4–7 MoE routing analysis; wk 6–11 Pareto sweeps + ablations; wk 12–14 analysis, regression, writing)', 'estimated_gpu_cost': '$4,800 at ~$3.00/GPU-hr average (mix of spot at $1.67–$2.50/hr for H100 SXM and on-demand for debugging)'}, 'human_in_loop': {'gpu_hours': '1,450 (Claude-assisted probe code, MSO computation scripts, routing analysis, and Bayesian model comparison saves ~150 hr of manual iteration)', 'timeline': '12 weeks', 'claude_api_cost': '$700 (Sonnet 4.6 at $3/$15 per M tokens: ~35M input + 10M output tokens for MSO/principal-angle implementation, routing analysis scripts, WAIC computation, analysis notebooks)', 'estimated_gpu_cost': '$4,350 at ~$3.00/GPU-hr average'}, 'auto_research': {'gpu_hours': '1,450', 'timeline': '8 weeks', 'claude_api_cost': '$2,800 (Opus 4.7 at $5/$25 per M tokens: ~130M input + 40M output for autonomous sweep management, routing analysis, MSO computation, Bayesian model comparison, result interpretation, draft writing)', 'estimated_gpu_cost': '$4,350 at ~$3.00/GPU-hr average', 'speed_bottleneck': 'Sequential LoRA-DPO fine-tuning within each Pareto sweep (each run ~5 GPU-hr on 4–8×H100; β values can be parallelized across cluster but limited by GPU allocation); MoE routing analysis requires loading full 235B/400B models'}}\n\n## Inspired By\nField guide Section 4.1 (pass@1 vs. production gap) + the convergent pattern: (a) the formal alignment tax geometry needs entanglement-robust metrics for empirical validation, (b) Plaut's near-linear agentic frontier needs geometric explanation (our framework predicts: high entanglement → small α → near-linear ellipse), (c) the MoE safety routing literature needs geometric formalization, and (d) null-space projection methods (NSPO, OGPSA) need entanglement-aware adaptation. These four bridges converge in one study.\n\n## Target Venues\n- ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026 — primary target, 14-week execution + 4-week buffer from May 19 start)\n- AAAI 2027 (abstract Jul 26, full paper Aug 2, 2026 — stretch target for dense-model-only subset if Phase 1+3 dense results are strong by week 10)\n- ICML 2027 (estimated Jan 29, 2027 — fallback with complete results including all MoE ablations)\n\n## Key References\n- What Is the Geometry of the Alignment Tax? (arXiv 2603.00047, Mar 2026)\n- Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study (arXiv 2505.14185, ICLR 2026)\n- The Hidden Dimensions of LLM Alignment (arXiv 2502.09674, ICML 2025)\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv 2603.02229, Mar 2026, Plaut)\n- Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization [NSPO] (arXiv 2512.11391, ICLR 2026)\n- Safety Alignment as Continual Learning via Orthogonal Gradient Projection [OGPSA] (arXiv 2602.07892, Feb 2026)\n- The Autonomy Tax: Defense Training Breaks LLM Agents (arXiv 2026)\n- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety (arXiv 2602.16943, Feb 2026)\n- Why Does Agentic Safety Fail to Generalize Across Tasks? (arXiv 2605.06992, May 2026)\n- RASA: Routing-Aware Safety Alignment for MoE Models (arXiv 2602.04448, Feb 2026)\n- SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs (arXiv 2506.17368)\n- Sparse Models, Sparse Safety (arXiv 2602.08621, Feb 2026)\n- Geometric Routing Enables Causal Expert Control in MoE (arXiv 2604.14434, Apr 2026)\n- Grassmannian MoE (arXiv 2602.17798, Feb 2026)\n- Sparse Crosscoders for diffing MoEs and Dense models (arXiv 2603.05805, Mar 2026)\n- Can LLM Safety Be Ensured by Constraining Parameter Regions? (arXiv 2602.17696, Feb 2026)\n- The Geometry of Alignment Collapse (arXiv 2602.15799, Feb 2026)\n- ShaPO: Selective Geometry Control for Safety Alignment (arXiv 2602.07340, Feb 2026)\n- Fundamental Safety-Capability Trade-offs (arXiv 2503.20807, PNAS Nexus 2026)\n- Steering Externalities (arXiv 2026)\n- The Verifier Tax (arXiv 2026)\n- When Safety Geometry Collapses (arXiv 2605.02914, May 2026)\n- The Causal Impact of Tool Affordance (arXiv 2603.20320, Mar 2026)\n- OpenAgentSafety (ICLR 2026)\n- ATBench (arXiv 2604.02022, Apr 2026)\n- Multi-Agent Security Tax (arXiv 2025)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:29:35.651Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:29:35.651Z",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:29:35.666Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv Mar 2026, Robin Young): 本 proposal 的理论基础。纯理论论文，推导出 alignment tax 的椭圆 Pareto 前沿由 safety-capability 子空间间的主角 α 参数化。作者明确承认框架在大扰动下失效（"the KL is not quadratic, the representation geometry shifts"），且无任何实证验证。
- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026, CERT-Lab): 引入 MSO (Mode Subspace Overlap) 量化 safety-capability 纠缠度。关键发现：safety 子空间与 useful update 子空间高度重叠，无法线性分离。仅在 Llama 2/3.2, Qwen 2.5 (1B–7B) 的 chat 设定下验证。
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229) (Mar 2026, Plaut): 在 agentic DPO 中观察到近线性 Pareto 前沿 (R²=0.77, slope −0.83)。仅用 β∈{0.05, 0.1} 两个值，8B–14B dense 模型，无表征分析，无几何解释。
- [RASA: Routing-Aware Safety Alignment for MoE](https://arxiv.org/abs/2602.04448) (Feb 2026): 发现 MoE 全参数安全微调会产生 routing dominance artifacts（恢复原始 routing 后 harmlessness 下降 0.38–0.46），证明安全通过 routing shortcuts 而非 expert repair 实现。
- [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026): 将 safety gradients 投影到 capability null space，假设子空间可分离——正是 MSO 论文反驳的假设。
- [OGPSA](https://arxiv.org/html/2602.07892v1) (Feb 2026): 类似正交梯度投影方法，同样假设子空间可分离。
- 调研总结: 该领域形成了"理论框架(Young) + 纠缠测量(MSO) + agentic观察(Plaut) + MoE安全(RASA/SAFEx)"四条平行线，且确认**无现有工作**将这四条线桥接——proposal 定位的 gap 是真实存在的。

【Trivial Alternative 检验】:
最直接的 trivial alternative：直接对 Plaut 的工作进行扩展——用更多 β 值做 DPO sweep，拟合曲线区分线性/椭圆，不需要任何表征几何分析。这能回答"前沿形状是什么"但无法回答"为什么是这个形状"。本 proposal 的增量价值核心在 **dual-estimation test**（α_repr vs α_frontier 是否一致）——这是对几何理论的因果验证，而非单纯的曲线拟合。这确实不可被 trivial baseline 替代。但需注意：如果 dual-estimation 结果是"一致"，审稿人可能认为这只是 confirmation（"the theory works as predicted"），surprise 有限。

【前提假设检验】:
1. **线性表征假设在 agentic 设定下仍近似成立**：整个框架依赖于 safety/capability 可以用线性子空间表征。原理论作者明确指出框架在大扰动下失效。Agentic 设定涉及多步推理、工具调用，非线性度显然更高——该假设未经验证且可能在 agent 设定下恰好最不成立。
2. **LoRA-DPO β sweep 能产生足够的前沿变异**：12 个 β 值是否足以用 WAIC 区分椭圆 vs 线性？椭圆退化为直线的判别需要高曲率区域的精确采样，但高 β 区域训练可能不稳定。
3. **Tool-call decision point 的 activation 捕捉相关几何**：假设在工具调用前的 token position 提取的 activation 就是 safety/capability trade-off 发生的"正确位置"——这是方法论假设，无先验支持。
4. **Dense 和 MoE 的 LoRA matched-parameter 对比是 "apples-to-apples"**：MoE 的 LoRA 作用于 22B active parameters vs dense 的 32B 全参数，matched trainable params 不等于 matched effective capacity。

【3 维度打分】:
1. Novelty: 中 — Gap 是真实存在的（调研确认无现有工作同时覆盖 entanglement-aware + architecture-controlled + agentic geometry）。Dual-estimation test 是方法论上的真实创新。但核心贡献性质是"用已有方法(MSO, principal angles)在新设定(agents, MoE)验证已有理论(Young 2603.00047)"——是 empirical validation + extension，非 new theory 或 new method。类比：如果 Young 的理论是 Newton's law，本文是"在水中验证牛顿定律也成立"——有价值但 novelty 天花板有限。

2. Significance: 中 — 如果结果 positive（α_repr ≈ α_frontier，theory works），实际意义是"可以从表征测量预测 alignment tax 严重程度，无需跑完整 DPO sweep"——这是有实用价值的。MoE vs dense 对比也 timely。但 proposal 明确排除了 intervention（不做 entanglement-adapted NSPO/OGPSA），所以贡献停留在 descriptive/diagnostic 层面，不直接改变 alignment 实践。如果结果 negative（theory fails in agents），贡献是 negative result——对 ICLR 可以接受但影响力更低。

3. Related Work: 强 — 覆盖极为全面（~30篇），定位清晰，四条平行线的汇聚叙事 compelling。每篇引用的论文经验证均真实存在且描述准确。唯一潜在遗漏：multi-objective alignment 的 HoE (Hierarchical Experts) 工作与 MoE alignment 相关但未提及。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
- Novelty 是"中"而非"强"：核心是 empirical validation of an existing framework in new settings。审稿人看到 positive results 时最可能的反应是"nice confirmation, the theory works as expected"而非 "surprising"。这直接限制了上界（不进入 35%+ 区间）。
- Significance 是"中"：pure measurement paper without intervention，停留在 diagnostic。
- Related Work 是"强"：叙事清晰，gap 真实，这撑起了下界（不低于 25%）。
- MoE routing 分析有潜力产生 surprise（如发现 routing-mediated fragility 的具体几何机制），但这恰是最不确定的部分。
- 上界主要受限于 Novelty 维度：contributes a validation, not a new paradigm。

【主要风险】:
1. **"Confirmation without surprise" 风险**：如果 dual-estimation 一致、agents 确实有更高 MSO 和更小 α，审稿人可能评价为"verifies what theory already predicted"——incremental validation 而非 new insight。核心问题：验证别人的理论在新设定下成立，这个贡献量级是否够一篇 top venue paper？
2. **线性表征假设在 agentic 设定下可能恰好失效**：如果 agent 的多步推理使 safety/capability 表征本质上非线性，则整个框架的前提崩塌。这不仅是 negative result，而是 undermines the entire methodology——dual-estimation 失败不是因为"theory wrong"而是"measurement tool inappropriate"，难以得出清晰结论。
```

Sources:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)
- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185)
- [Safety Training Persists Through Helpfulness Optimization in LLM Agents](https://arxiv.org/abs/2603.02229)
- [RASA: Routing-Aware Safety Alignment for MoE Models](https://arxiv.org/abs/2602.04448)
- [Mitigating the Safety Alignment Tax with Null-Space Constrained Policy Optimization](https://arxiv.org/abs/2512.11391)
- [OGPSA: Safety Alignment as Continual Learning](https://arxiv.org/html/2602.07892v1)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【重要前置说明 — 投稿会议匹配度】:
本 proposal 的目标会议为 ICLR 2027 / AAAI 2027 / ICML 2027（proposal 原文明确列出）。
然而用户要求评估的是 **CoRL 2026**（Conference on Robot Learning）。
CoRL 的 scope 聚焦于 robot learning、manipulation、locomotion、sim-to-real transfer、robot perception 等，
与本 proposal 的主题（LLM alignment tax 的几何结构、safety-capability 表征子空间纠缠度量）**完全不匹配**。
本 proposal 在 CoRL 属于 **scope 外 desk reject**，中稿概率接近 0%。

以下评估基于该 idea 在其**合理目标会议**（ICLR / ICML / NeurIPS 等 AI/ML 主会）的质量，
以便后续流程判断是否值得立项。同时在最终概率估计中给出 CoRL 的独立评估。

======================================================================

【领域调研】:

1. [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047) (arXiv, Mar 2026):
   本 proposal 的理论骨架来源。该文在线性表征假设下证明了
   safety-capability tradeoff 的 Pareto 前沿为椭圆，参数化
   于 safety/capability 子空间的 principal angle α。纯理论工作，
   作者自己承认"大扰动下 KL 非二次、表征几何会漂移"，
   无任何实证验证。

2. [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185) (ICLR 2026):
   引入 Mode Subspace Overlap (MSO) 度量 safety/capability 子空间
   的纠缠程度。在 Llama 2/3.2、Qwen 2.5（1B–7B）上实验，
   仅 chat setting。证明 safety 子空间与 useful update 子空间
   高度重叠——子空间分离假设不成立。

3. [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (ICML 2025):
   在 Llama 3 8B 上发现多维正交 safety 方向——主 refusal 方向
   + 可解释的次级方向（假设叙事、角色扮演等）。仅 chat，单模型。

4. [Safety Training Persists Through Helpfulness Optimization](https://arxiv.org/abs/2603.02229) (Plaut, Mar 2026):
   在 agentic DPO 中观察到近线性 Pareto 前沿（R²=0.77, slope −0.83），
   模型为 Llama 3.1 8B / Qwen 2.5 7B / Phi 4 14B，仅用 β∈{0.05, 0.1}，
   无表征分析、无 MoE。**关键数据点**，但分辨率不足以区分
   low-angle ellipse vs. true line。

5. [NSPO](https://arxiv.org/abs/2512.11391) (ICLR 2026):
   将 safety 梯度投影到 capability 协方差矩阵的零空间，
   实现 safety 不降低 capability 的 SOTA。**假设子空间可分离**
   ——恰好是 MSO 论文所推翻的假设。

6. [OGPSA](https://arxiv.org/abs/2602.07892) (Feb 2026):
   类似思路，正交梯度投影。同样假设可分离。

7. [RASA](https://arxiv.org/abs/2602.04448) (Feb 2026):
   识别 safety-critical experts，证明全参 MoE fine-tune
   通过 routing shortcuts 达到"安全"但恢复原始 routing 后
   safety 崩溃（Δ ∈ [−0.38, −0.46]）。

8. [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621) (Feb 2026):
   引入 RoSais score，mask 5 routers → ASR 增加 4× 至 0.79。
   MoE safety 高度依赖少数 routing pathway。

9. 调研总结:
   该领域目前处于"理论框架刚出、实证验证空白、MoE 安全
   独立发展但未连接几何理论"的阶段。Proposal 瞄准的桥接
   方向（entanglement-aware geometry × MoE × agentic）确实
   没有现有工作覆盖。但这是一个 **measurement/validation study**
   而非 method paper，其价值取决于度量结果能否产生超出
   直觉预期的洞见。


【Trivial Alternative 检验】:

存在更简单的替代路径：
(a) 直接在 Plaut 的设置上增加 β sweep 密度（从 2 → 12+）并做
    ellipse vs. line 的 model comparison，即可回答"agentic 前沿
    是否为低角度椭圆"——不需要 MSO、不需要 α_repr、不需要
    MoE comparison。这是一个 ~200 GPU-hr 的实验。
(b) 类似地，直接在 chat vs. agent 上测 MSO 差异（延伸 ICLR 2026
    论文到 agent setting）也是一个独立且更轻量的贡献。

Proposal 的增量价值在于 **dual-estimation test**（α_repr ≈ α_frontier）
—— 这是唯一不能被 trivial decomposition 替代的部分，因为它
同时需要表征分析和前沿拟合。但审稿人可能会问：这个 agreement
如果成立，说明什么？如果不成立，又说明什么？前者是 "theory works
as expected"（not surprising），后者是 "theory breaks under
entanglement"（interesting but negative）。核心发现的 upside
并不高。


【前提假设检验】:

核心逻辑链中有以下未验证假设：

1. **线性表征假设在 agent 激活上仍然成立**。原理论框架基于
   线性表征假设（safety/capability 编码在线性子空间）。
   在 chat 单轮设置下这个假设有一定实证基础，但在多步
   agentic trajectory 中，激活的提取点（"tool-call decision
   points"）是否仍满足线性可分离性，完全未知。如果不满足，
   整个 principal angle 测量和椭圆拟合都失去意义。

2. **LoRA-DPO β sweep 能产生有意义的 Pareto 前沿**。仅通过
   β 值变化来 trace 前沿，隐含假设 β 是 safety-capability
   tradeoff 的唯一/主要控制变量。但 DPO 前沿的形状可能
   更多受 data composition、LoRA rank、learning rate schedule
   影响而非 β。Plaut 的 R²=0.77 本身就说明有 23% 的方差
   未被解释。

3. **Active-parameter matching = 公平比较**。Proposal 声称
   通过匹配 trainable parameter count 来隔离架构效应，但
   dense 32B 和 MoE 22B-active/235B-total 的计算图、梯度流、
   representation capacity 根本不同。匹配 LoRA rank 只能
   控制一个维度。

4. **12 个数据点足以用 WAIC 区分三个模型**。虽然 proposal
   选择了 Bayesian 方法而非频率检验，但 12 个 β 点 fit 2-参数
   椭圆 vs. 2-参数线性 vs. 分段线性，自由度非常有限。
   α_frontier 的估计不确定性可能很大，以至于 dual-estimation
   test 不具有判别力。


【3 维度打分】:

1. Novelty: 【中】
   理由：桥接方向（entanglement geometry × agentic × MoE）
   确实目前无人做过——调研确认不存在直接竞争工作。但 novelty
   的本质是"将已有工具 A（MSO/principal angles）应用到新设置 B
   （agents + MoE）并验证已有理论 C（椭圆前沿）是否成立"。
   这是 **methodological extension** 而非 **conceptual innovation**。
   MSO 来自 [Safety Subspaces](https://arxiv.org/abs/2505.14185)，
   椭圆理论来自 [Geometry of Alignment Tax](https://arxiv.org/abs/2603.00047)，
   MoE routing 分析框架来自 [RASA](https://arxiv.org/abs/2602.04448) /
   [Sparse Models Sparse Safety](https://arxiv.org/abs/2602.08621)。
   Proposal 的原创方法论贡献仅限于 dual-estimation test 的
   设计——这是 clever 但不 deep。与 ICLR 2026 的 MSO 论文相比，
   novelty delta 主要在 setting extension 而非 insight depth。

2. Significance: 【中偏弱】
   理由：
   - 正面：alignment tax 是重要问题；理解其几何结构有实际价值
     （指导 NSPO/OGPSA 等方法的改进）；MoE 已成为 frontier
     model 的主流架构，理解其 safety 机制有现实意义。
   - 负面：这是一个 **纯度量论文**，proposal 自己明确排除了
     intervention phase。度量论文的 significance 取决于度量结果
     的 surprise factor。但核心预测（agent 比 chat 纠缠更高、
     线性前沿是低角度椭圆的退化、MoE routing 引入脆弱性）
     **全部是直觉上"I would have guessed this"的方向**。即使
     结果完美 positive，审稿人的反应更可能是"nice confirmation"
     而非"surprising insight"。
   - 此外，proposal 无法回答 "so what"——得到了 α_repr ≈ α_frontier，
     然后呢？能指导什么实际决策？Proposal 最后提到"predicting
     alignment tax severity from representation measurements alone"，
     但这需要 α_repr → downstream safety metric 的 predictive
     regression 在多个模型上有强泛化性，12 个数据点难以证明。

3. Related Work: 【强】
   理由：文献覆盖非常全面。调研确认所有引用的关键论文
   （[2603.00047](https://arxiv.org/abs/2603.00047),
   [2505.14185](https://arxiv.org/abs/2505.14185),
   [2502.09674](https://arxiv.org/abs/2502.09674),
   [2603.02229](https://arxiv.org/abs/2603.02229),
   [2512.11391](https://arxiv.org/abs/2512.11391),
   [2602.04448](https://arxiv.org/abs/2602.04448),
   [2602.08621](https://arxiv.org/abs/2602.08621)）
   均真实存在且描述准确。差异化定位清晰——明确说明了
   每篇先前工作覆盖了什么、缺失了什么。这是 proposal 最强的
   维度。


【概率估计】:

对合理目标会议（ICLR / ICML / NeurIPS）:
  [18% - 28%] 中位 22%

对 CoRL 2026:
  [0% - 3%] 中位 1%（scope 完全不匹配，desk reject）

【估计理由】:
Idea 内核是"将已有度量工具在新设置上做验证性实验"。
方向正确、文献扎实、execution plan 详尽，这些保证了下限不会太低。
但 **Significance 维度限制了上界**：核心发现即使完全 positive，
审稿人大概率认为是 "confirmatory measurement, not surprising"。
Novelty 是 methodological extension 而非 conceptual leap，
dual-estimation test 有巧思但不足以将整个工作提升到 strong accept。
一个纯度量论文需要 surprising result 来中顶会——而这个 proposal
的所有预测方向都太符合直觉。

此外，CoRL 2026 是 robot learning 会议（manipulation, locomotion,
sim-to-real, robot perception），本 proposal 的 LLM alignment
safety 主题完全不在其 scope 内，投稿几乎必然 desk reject。

【主要风险】:
1. **"Confirmatory, not insightful" 质疑**：审稿人最可能的 reject
   理由是——如果 entanglement 高则前沿近线性，这正是理论的
   直接推论，验证它成立不构成 surprising contribution；验证它
   不成立则理论 breaks 但 proposal 没有提供替代框架。
2. **Scope overload 风险**：2×2 design × 12 β × MoE ablations ×
   Bayesian model comparison × routing analysis × MSO × multi-dimensional
   decomposition × principal angles —— 单篇论文难以深入每个维度，
   极可能被审稿人批评为"a mile wide and an inch deep"。
```

Sources:
- [What Is the Geometry of the Alignment Tax?](https://arxiv.org/abs/2603.00047)
- [Safety Subspaces are Not Linearly Distinct](https://arxiv.org/abs/2505.14185)
- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674)
- [Safety Training Persists Through Helpfulness Optimization](https://arxiv.org/abs/2603.02229)
- [NSPO: Null-Space Constrained Policy Optimization](https://arxiv.org/abs/2512.11391)
- [OGPSA: Safety Alignment as Continual Learning](https://arxiv.org/abs/2602.07892)
- [RASA: Routing-Aware Safety Alignment](https://arxiv.org/abs/2602.04448)
- [Sparse Models, Sparse Safety](https://arxiv.org/abs/2602.08621)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━



【原始 proposal（允许参考但不是主要依据）】:
# Entanglement Geometry of the Alignment Tax Across Dense and MoE Architectures in Agentic Tool-Use Settings

## Description
The alignment tax has been formalized geometrically with elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces. But empirically, these subspaces are highly entangled (ICLR 2026), MoE architectures route safety through sparse expert dynamics, and in agentic settings Plaut (2603.02229) already observes a near-linear frontier (R²=0.77) without geometric explanation. We hypothesize a unifying account: high safety-capability entanglement in agents yields small α, degenerating the ellipse toward linearity — and MoE routing introduces architectural modulation absent in dense models. We conduct the first entanglement-aware, architecture-controlled measurement of alignment tax geometry in agents. Using a 2×2 design — {Qwen3-32B, Gemma 4 31B} (dense) × {Qwen3-235B-A22B, Llama-4-Maverick} (MoE) in {chat, agent} — we measure entanglement via MSO, multi-dimensional safety decomposition, and principal angles (yielding α_repr). For MoE models, we add per-expert subspace analysis, routing distribution divergence, and router safety importance scoring. We sweep 12 LoRA-DPO β values per condition with matched trainable parameters across architectures (plus MoE-specific ablations), using Bayesian model comparison (WAIC) to distinguish elliptic, linear, and piecewise-linear frontiers, extracting α_frontier. The dual-estimation test — whether α_repr agrees with α_frontier — provides the first empirical validation of the geometric alignment tax framework. Expected: (1) higher MSO in agents vs. chat; (2) α_repr ≈ α_frontier with both smaller in agents (explaining Plaut's near-linear frontier as a low-angle ellipse); (3) MoE routing-mediated safety fragility absent in dense models; (4) the geometric framework becoming actionable for predicting alignment tax severity from representation measurements alone.

## Core Problem
The alignment tax — the safety-capability tradeoff — has been formalized geometrically under the linear representation hypothesis, yielding elliptic Pareto frontiers parameterized by the principal angle α between safety and capability subspaces. However, three empirical challenges prevent direct application: (1) Safety Subspaces are Not Linearly Distinct (ICLR 2026) shows safety and capability subspaces are highly entangled, with Mode Subspace Overlap (MSO) strongest between useful and safety-specific updates; (2) frontier open-weight models are predominantly Mixture-of-Experts architectures where safety is governed by sparse expert routing dynamics (RASA, SAFEx, Sparse Models Sparse Safety), not global activation subspaces; (3) in agentic tool-use settings, both challenges intensify — text safety does not transfer to tool-call safety (Mind the GAP), and the safe controller mapping has inherently higher Lipschitz complexity (Why Does Agentic Safety Fail to Generalize). Critically, Plaut (2603.02229) already measured an approximately linear Pareto frontier (R²=0.77, slope −0.83) in agentic DPO on 8B–14B models — but with only two β values, no representation analysis, and no MoE comparison, providing an empirical observation without geometric explanation. The theoretical framework predicts that when the principal angle α is small (i.e., when safety and capability subspaces are highly entangled), the elliptic frontier degenerates toward linearity. The field thus has a frontier shape observation that awaits geometric explanation, entanglement measurements that have not been tested in agents or MoE models, and a theoretical bridge between entanglement degree and frontier geometry that has never been validated empirically.

## Opportunity
Four independent lines of work create a convergence point whose bridge is missing. The Geometry of the Alignment Tax (Mar 2026) provides the formal apparatus — principal angles, elliptic Pareto frontiers, tax rate decomposition — but assumes linear separability, static representations, and dense architectures, with the author explicitly noting the framework fails 'for large perturbations, the KL is not quadratic, the representation geometry shifts.' Safety Subspaces are Not Linearly Distinct (ICLR 2026) proves the separability assumption fails empirically by quantifying safety-capability entanglement via MSO, but only studies chat settings on models up to 7B. The Hidden Dimensions of LLM Alignment (ICML 2025) reveals multi-dimensional orthogonal safety directions with interpretable secondary features, but likewise only in chat on Llama 3 8B. Plaut (Mar 2026) discovers a near-linear Pareto frontier in agentic DPO, which the geometric theory predicts should occur when α is small — but Plaut used only 8B–14B dense models with 2 β values and provided no representation analysis to verify this geometric explanation. Meanwhile, the MoE safety literature (RASA, SAFEx, Sparse Models Sparse Safety, Geometric Routing) establishes that safety operates through routing dynamics — safety-critical experts, routing distribution divergence, expert silencing vulnerabilities — but none connects to the alignment tax geometry. And the null-space projection literature (NSPO at ICLR 2026, OGPSA) mitigates the alignment tax by projecting safety gradients into capability null spaces, but assumes those subspaces are separable — precisely the assumption MSO disproves. The missing bridge connects: (a) entanglement-aware geometric measurement to the theoretical framework, (b) architecture-aware analysis to capture how MoE routing mediates the tax differently from dense models, and (c) agentic empirics to verify whether high entanglement geometrically explains the near-linear frontier Plaut observed.

## Landscape
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

## Resource Estimate
{'manual': {'gpu_hours': '1,600 (4×H100 for dense models, 8×H100 for MoE: Phase 1 activation extraction 4 models × 2 settings × ~25 hr = 200 hr; Phase 2 MoE routing analysis 2 models × 60 hr = 120 hr; Phase 3 primary Pareto sweep 4 models × 2 settings × 12 β × ~5 hr = 480 hr; Phase 3 MoE ablation 2 models × 2 settings × 8 β × ~5 hr = 160 hr; agent evaluation on tau2-bench + OpenAgentSafety + ATBench = 200 hr; infrastructure debugging + reruns = 440 hr buffer)', 'timeline': '14 weeks (wk 1–2 infrastructure + trajectory generation; wk 2–5 entanglement geometry extraction; wk 4–7 MoE routing analysis; wk 6–11 Pareto sweeps + ablations; wk 12–14 analysis, regression, writing)', 'estimated_gpu_cost': '$4,800 at ~$3.00/GPU-hr average (mix of spot at $1.67–$2.50/hr for H100 SXM and on-demand for debugging)'}, 'human_in_loop': {'gpu_hours': '1,450 (Claude-assisted probe code, MSO computation scripts, routing analysis, and Bayesian model comparison saves ~150 hr of manual iteration)', 'timeline': '12 weeks', 'claude_api_cost': '$700 (Sonnet 4.6 at $3/$15 per M tokens: ~35M input + 10M output tokens for MSO/principal-angle implementation, routing analysis scripts, WAIC computation, analysis notebooks)', 'estimated_gpu_cost': '$4,350 at ~$3.00/GPU-hr average'}, 'auto_research': {'gpu_hours': '1,450', 'timeline': '8 weeks', 'claude_api_cost': '$2,800 (Opus 4.7 at $5/$25 per M tokens: ~130M input + 40M output for autonomous sweep management, routing analysis, MSO computation, Bayesian model comparison, result interpretation, draft writing)', 'estimated_gpu_cost': '$4,350 at ~$3.00/GPU-hr average', 'speed_bottleneck': 'Sequential LoRA-DPO fine-tuning within each Pareto sweep (each run ~5 GPU-hr on 4–8×H100; β values can be parallelized across cluster but limited by GPU allocation); MoE routing analysis requires loading full 235B/400B models'}}

## Inspired By
Field guide Section 4.1 (pass@1 vs. production gap) + the convergent pattern: (a) the formal alignment tax geometry needs entanglement-robust metrics for empirical validation, (b) Plaut's near-linear agentic frontier needs geometric explanation (our framework predicts: high entanglement → small α → near-linear ellipse), (c) the MoE safety routing literature needs geometric formalization, and (d) null-space projection methods (NSPO, OGPSA) need entanglement-aware adaptation. These four bridges converge in one study.

## Target Venues
- ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026 — primary target, 14-week execution + 4-week buffer from May 19 start)
- AAAI 2027 (abstract Jul 26, full paper Aug 2, 2026 — stretch target for dense-model-only subset if Phase 1+3 dense results are strong by week 10)
- ICML 2027 (estimated Jan 29, 2027 — fallback with complete results including all MoE ablations)

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


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "237c86d5-752b-4dfa-9b8f-2d70139f3bd9",
  "type": "user",
  "uuid": "5567f802-55eb-4c04-8d73-543bb2d45bc6",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:29:35.664Z_

```json
{
  "parentUuid": "5567f802-55eb-4c04-8d73-543bb2d45bc6",
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
  "uuid": "87eebfb7-c655-4603-9435-dd8f97cc21a4",
  "timestamp": "2026-05-20T03:29:35.664Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:29:35.664Z_

```json
{
  "parentUuid": "87eebfb7-c655-4603-9435-dd8f97cc21a4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fc1f0a84-4788-4449-ac32-b7e173fca948",
  "timestamp": "2026-05-20T03:29:35.664Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to evaluate this proposal. L…",
  "leafUuid": "fc1f0a84-4788-4449-ac32-b7e173fca948",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Measure alignment tax geometry in agentic MoE models",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:30:05.652Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully.

First, let me note that I only see **two** reviewer assessments, not three. Reviewer 3's section is empty - there's no content after "审稿人 3（独立评审）". Let me work with what I have.

Wait, the user says "3 位审稿人" but Reviewer 3 is blank. I need to address this. Let me proceed with the two available reviews and note the missing third.

Actually, looking more carefully, the user instruction says "综合以下 3 位审稿人对同一 proposal 的独立评估" but Reviewer 3 is empty. I should note this and work with what's available.


Looking at the two available reviews, Reviewer 1 rates the novelty and significance as moderate with strong related work coverage, estimating a 30% acceptance probability, while flagging concerns about confirmation bias and linear representation assumptions. Reviewer 2 is more critical, also rating novelty and significance as moderate to weak, with a 22% probability for reasonable venues but only 1% for CoRL, citing confirmatory findings as a key weakness.

Both reviewers converge on the core issue: the work reads as methodological extension rather than conceptual breakthrough, with strong related work grounding but insufficient novelty to surprise. The 8-point gap between their probability estimates reflects Reviewer 2's additional concern about scope mismatch with CoRL specifically. With Reviewer 3 missing, I'm working with limited data, but the mean probability sits around 26% with notable variance depending on venue fit.

The critical insight from Reviewer 2 is that this proposal fundamentally misaligns with CoRL's scope—it's about LLM alignment safety geometry, not robot learning. That scope mismatch would likely trigger a desk reject, making the acceptance probability essentially zero for this specific venue, regardless of the paper's merit for other conferences like ICLR or ICML. I'm calculating the standard deviation with just these two reviewer assessments—around 5.7% for reasonable venues—which puts us in the moderate agreement range, so I should be more cautious and widen my confidence intervals. For CoRL specifically, both reviewers implicitly agree it's a desk reject since R1 didn't even consider it viable for that venue. Now I'll write up the final assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc1f0a84-4788-4449-ac32-b7e173fca948",
  "isSidechain": false,
  "requestId": "req_011CbD7USXeaCYj3PHPQ8HEq",
  "type": "assistant",
  "uuid": "1bb12965-20de-4434-94f3-0b679252f108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCNeVNZ21TKtewZLFL9Tz3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14617,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3667,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14617
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

_source line 9 · 2026-05-20T03:31:06.933Z_

【阶段】: Meta Judge

**⚠️ 前置说明：审稿人 3 评审内容为空**，实际仅收到 2 份有效评审（R1、R2）。以下综合基于 2 份评审，样本量不足 3 份时我按规则偏严处理。

**⚠️ 关键 Scope 问题：用户要求评估 CoRL 2026 中稿潜力，但 proposal 原文明确列出的目标会议为 ICLR 2027 / AAAI 2027 / ICML 2027。R2 明确指出 CoRL（Conference on Robot Learning）聚焦 robot learning / manipulation / locomotion / sim-to-real，本 proposal 的 LLM alignment tax 几何主题完全不在 scope 内，属于 desk reject。以下给出两组评估：CoRL 2026（实际投稿目标）+ 合理目标会议（ICLR/ICML/NeurIPS）。**

---

【三次中位】: [30%, 22%, N/A（R3 缺失）] std=5.7%（仅 2 个有效值）

【共识维度】（2/2 人同时提到）:
- **Novelty = 中**：两位审稿人高度一致——核心贡献是"将已有度量工具（MSO, principal angles）在新设定（agents, MoE）上验证已有理论（Young 椭圆前沿）"，属 methodological extension 而非 conceptual innovation。Dual-estimation test 有巧思但不足以提升整体 novelty 到"强"。
- **Related Work = 强**：两位均确认文献覆盖极为全面，所有引用真实存在且描述准确，差异化定位清晰。
- **"Confirmation without surprise" 核心风险**：两位均指出——如果结果 positive（α_repr ≈ α_frontier），审稿人最可能的反应是"nice confirmation, the theory works as predicted"，surprise factor 低；如果 negative，proposal 未提供替代框架。
- **线性表征假设在 agentic 设定下可能失效**：两位均指出该前提未经验证，且 agentic 多步推理场景的非线性度更高，恰好可能是假设最不成立之处。
- **12 个 β 数据点统计功效存疑**：两位均质疑 12 点是否足以用 WAIC 区分椭圆 vs 线性，α_frontier 估计不确定性可能很大。
- **Dense vs MoE matched-parameter 对比不公平**：两位均指出匹配 trainable parameter count 不等于匹配 effective capacity。
- **纯度量论文无 intervention**：两位均注意到 proposal 明确排除 intervention phase，贡献停留在 descriptive/diagnostic 层面。

【异常维度】（仅 1 人提到）:
- **Significance "中偏弱" vs "中"**：R2 比 R1 更严，认为核心预测方向全部符合直觉（"I would have guessed this"），而 R1 认为 MoE routing 分析有潜在 surprise。差异不大，偏严取"中偏弱"。
- **"Scope overload / a mile wide and an inch deep" 风险**（仅 R2）：2×2 design × 12β × MoE ablations × Bayesian comparison × routing analysis × MSO × multi-dimensional decomposition × principal angles——单篇论文可能每个维度都做不深。这个观察合理，不作为 outlier 降权，纳入综合评估。
- **CoRL scope mismatch**（仅 R2 显式指出）：但这是客观事实而非主观判断，R1 虽未显式提及但其评估隐含针对 ML 主会而非 CoRL，实质上两位均未按 CoRL 标准评估。此点权重最高。

【最终概率】:

**对 CoRL 2026（用户指定目标）：**
[0% - 3%] 中位 1%

**对合理目标会议（ICLR 2027 / ICML 2027 / NeurIPS 2027）：**
[18% - 28%] 中位 23%

【一致性】: 中（std ≈ 5.7%，且仅 2 份有效评审，按规则偏严）

【综合理由】:

**CoRL 评估**：LLM alignment tax 的表征几何分析与 CoRL 的 robot learning scope 完全不匹配。即使 proposal 质量极高，也面临 desk reject。R2 的 1% 估计合理——唯一非零概率来源是极小概率的 scope 误判（如 CoRL 2026 开设 LLM safety for robotics special track，但无证据表明此事）。

**合理会议评估逻辑**：
1. **概率上限由 Novelty 和 Significance 共同决定**。两位一致判 Novelty = 中，Significance 在中与中偏弱之间。这意味着即使实验执行完美，概率上限约 30-35%。一个"验证已有理论在新设定下成立"的工作，在 ICLR/ICML 的接收标准下，需要验证结果本身产生 surprising insight 才能突破这个天花板——而两位审稿人都认为核心预测方向太符合直觉。
2. **概率下限由实验设计的合理性决定**。实验设计详尽但有多个未解的方法论风险（线性假设、12 点统计功效、matched-parameter 公平性）。这些是可补救但需要额外工作的问题，下限不低于 18%（文献质量和 gap 真实性撑住）。
3. **偏严处理**：仅 2 份评审，R1 中位 30% vs R2 中位 22%，按规则偏向更严格方。取 23% 而非 26%（算术中位），反映：(a) R2 的 scope overload 风险是合理的额外降分点；(b) Significance "中偏弱" 比 "中" 更准确（纯度量论文 + 所有预测符合直觉）。

【建议】:

**对 CoRL 2026：KILL**（scope 完全不匹配，不建议投稿）

**对合理目标会议：边缘偏下 / 不推荐（中位 23%，低于 36% 阈值）**。idea 方向真实、文献扎实，但贡献性质（验证性度量，无 intervention，预测方向符合直觉）在顶会标准下 significance 不足。若要提升至可投稿水平，需要在 idea 层面增加 surprise factor 或加入 intervention 贡献。

【实施评估】:
- **计算资源**: ~1,450-1,600 GPU-hr（H100），需 4×H100（dense）到 8×H100（MoE 235B/400B 模型），估算 GPU 成本 $4,350-$4,800。MoE 模型需加载完整 235B/400B 参数，对显存要求高（至少 8×H100 80GB）。
- **数据需求**: OpenAgentSafety（350+ 可执行任务，公开）、ATBench（1,954 tools + 1,000 trajectories，公开）、tau2-bench（公开）、AdvBench/BeaverTails（公开）。数据全部公开可得，无获取瓶颈。
- **人工介入**: 中等。需要人工设计 trajectory extraction pipeline、调试 MSO/principal angle 计算代码、解读 Bayesian model comparison 结果。Proposal 估算可用 Claude API 辅助节省 ~150 hr 手工迭代（$700-$2,800 API 成本取决于自动化程度）。
- **训练需求**: 是——需对 4 个模型 × 2 个设定 × 12 个 β 值进行 LoRA-DPO 微调（共 96 次训练 run），加上 MoE ablation 额外 ~32 次 run。每次 run ~5 GPU-hr。这是主要计算瓶颈。
- **新 Benchmark**: 不需要构建新 benchmark。使用现有公开 benchmark 组合（OpenAgentSafety + ATBench + tau2-bench + AdvBench/BeaverTails）。
- **预估周期**: 12-14 周（从启动到可投稿），瓶颈在 Phase 3 的 sequential LoRA-DPO sweep（可通过 GPU 集群并行化 β 值缓解）。ICLR 2027 deadline（Sep 2026）需从 5 月中旬立即启动，时间紧张但可行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bb12965-20de-4434-94f3-0b679252f108",
  "isSidechain": false,
  "requestId": "req_011CbD7USXeaCYj3PHPQ8HEq",
  "type": "assistant",
  "uuid": "2a7e994a-81bc-4587-99f8-4602547c3549",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCNeVNZ21TKtewZLFL9Tz3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14617,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3667,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14617
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to evaluate this proposal. L…",
  "leafUuid": "2a7e994a-81bc-4587-99f8-4602547c3549",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Measure alignment tax geometry in agentic MoE models",
  "sessionId": "3b60e073-7297-4ac8-a7e7-fc2e804856dd"
}
```

---
