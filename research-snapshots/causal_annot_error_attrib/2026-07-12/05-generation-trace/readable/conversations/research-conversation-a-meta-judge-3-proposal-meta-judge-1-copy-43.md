# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/02b12412-4617-4da9-95ab-ccadfdb02d76.jsonl`
- **Structured JSON:** [`8cdca521f1157e739ddd.json`](../../sessions/8c/8cdca521f1157e739ddd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:53:36.404Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:53:36.404Z",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct the evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [JuICE: Taming Knowledge Conflicts in Language Models](https://arxiv.org/abs/2503.10996) (ICML 2025 Spotlight): 最直接的上游工作。发现注意力头存在 superposition（同一 head 同时促进 memory 和 context），提出双次推理头级干预，在11个数据集上达 SOTA。但仅限头级别，无 FFN/copy suppression 分析——正是 CORe 扩展的方向。\n- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221) (arXiv Feb 2026): 发现 flip 现象（正确答案在中层出现后被深层 FFN 抑制），用加性校正进行干预。FFN 级别，无电路级诊断。CORe Phase 2 的 flip 统一假设直接基于此。\n- [ParamMute](https://arxiv.org/abs/2502.15543) (NeurIPS 2025): 定位中-深层 FFN 为不忠实生成的关键，提出 FFN 抑制框架。单组件干预，无因果电路分析。\n- [SpARE: SAE-Based Representation Engineering](https://arxiv.org/abs/2410.15999) (NAACL 2025 Oral): 用预训练 SAE 特征在单层进行推理时干预，+10% EM。单层单点。\n- [CD-T: Contextual Decomposition for Transformers](https://arxiv.org/abs/2407.00886) (ICLR 2025): 电路发现方法，运行时间从小时降至秒级，97% ROC AUC。CORe Phase 1 的核心工具之一。\n- [PEAP: Position-aware Edge Attribution Patching](https://aclanthology.org/2025.acl-long.141/) (ACL 2025): 位置感知电路发现，比非位置方法边数少数个数量级。CORe Phase 1 的另一核心工具。\n- [Competition of Mechanisms](https://arxiv.org/abs/2402.11655) (ACL 2024) + [Generalizability Study](https://arxiv.org/abs/2506.22977) (arXiv 2025): 事实回忆 vs. 上下文复制的竞争。关键发现：Llama 3.1 8B 中头的特化显著减弱→override 电路在大模型中更分布式，支持 CORe 的多点干预动机。\n- [Simulated Adoption](https://arxiv.org/abs/2602.04918) (arXiv Feb 2026): 冲突解决通过正交干扰（几何旋转而非幅度抑制）。CORe Phase 2 几何统一的三个独立观察之一。\n- [How Transformers Reject Wrong Answers](https://arxiv.org/abs/2603.13259) (arXiv Mar 2026): 旋转动力学，1.6B 参数相变。另一个独立几何观察。\n- [Context Copying Modulation: Entropy Neurons](https://arxiv.org/abs/2509.10663) (EMNLP 2025 Findings): 熵神经元抑制上下文复制（<2‰ FFN 神经元但影响显著）。CORe 第三干预点（copy suppression inhibition）的机制基础。\n- [CLEAR: Probing Latent Knowledge Conflict](https://arxiv.org/abs/2510.12460) (arXiv Oct 2025): 三阶段干预但基于 probing（非因果），需微调，仅调制注意力。CORe 的最直接多阶段竞争者。\n- [CoCoA: Confidence- and Context-Aware Adaptive Decoding](https://aclanthology.org/2025.emnlp-main.1116/) (EMNLP 2025): 对比解码 SOTA，但在解码层操作，无内部机制理解。\n\n- **调研总结**: RAG 知识冲突干预领域正处于从\"单组件启发式干预\"向\"机制级理解\"的范式转换期。JuICE/CoRect/ParamMute/SpARE 各自识别了不同组件的贡献但彼此独立；Competition of Mechanisms 的泛化研究表明大模型中 override 机制更分布式。CORe 的定位——用因果电路追踪统一这些分散发现并进行协同多点干预——填补了一个真实存在的空白，但核心假设（补偿动力学）尚无直接前序证据。\n\n【整体印象】:\n作为审稿人，第一反应是：这是一份学术素养极高、问题定义精准、实验设计专业的 proposal。作者对领域文献的掌握深度超过了大多数投稿——不仅知道每个方法做了什么，还能精确定位它们的局限性并解释为什么这些局限性会导致性能瓶颈。补偿动力学假设具有理论吸引力，且在神经科学（neural circuit compensation）中有丰富类比。我会倾向于给 weak accept，但有保留意见：scope 过大（本质上是三篇论文合一）、核心假设尚属推测、以及 CD-T+PEAP 在 8B 规模 RAG 长上下文中的可扩展性存在不确定性。\n\n【核心贡献】:\n三层核心贡献：\n1. **方法论贡献**：首次将因果电路追踪（CD-T + PEAP）应用于 RAG override 机制，产出位置感知的 override 电路图——这本身就是对领域理解的实质推进。\n2. **理论贡献**：补偿动力学假设和 flip 现象的几何统一——如果成立，这将为单点干预瓶颈提供首个因果解释。\n3. **工程贡献**：几何感知协同三点推理时干预（FFN + 注意力 + copy suppression），无需训练，单次前向传播。\n\n这些贡献对领域的价值显著——从\"哪个组件重要\"的零散认知推进到\"组件如何协同构成 override 电路\"的系统理解。但价值高度依赖于补偿动力学假设是否成立。\n\n【方法合理性】:\n方法整体合理但复杂度高。具体评估：\n\n**合理之处：**\n- CD-T（粗筛）→ PEAP（精细位置感知边归因）的两阶段管线利用了两者的互补优势，有理论支撑。\n- 三点干预覆盖了文献中已识别的三类关键组件（FFN override layers/retrieval heads/entropy neurons），逻辑完整。\n- 几何感知校准（旋转主导→投影；幅度主导→缩放；混合→混合）基于三个独立的几何发现，有证据支持。\n- 纳入 Naive Stack baseline 是关键设计，直接检验\"电路指导的协同是否优于朴素组合\"。\n\n**潜在替代方案的威胁：**\n- 是否可以仅用 PEAP 做电路发现而跳过 CD-T？PEAP 本身已经能产出位置感知电路，CD-T 的粗筛步骤是否真正必要需要验证。\n- CoRect 的 logit contrast 方法本质上已经在做\"定位哪些层抑制了正确答案\"，CORe 的因果电路追踪是否能提供显著超越 CoRect 的定位精度？\n- 几何感知校准增加了显著复杂度——如果一个简单的固定强度三点干预就能超过单点方法，那几何感知部分的边际贡献可能不大。\n\n**方法风险：**\n- CD-T 在原论文中主要在小规模模型/任务上验证，8B 模型 + RAG 长上下文是显著的规模跳跃。\n- 三组件 × 多强度参数的校准空间很大，存在过拟合到特定数据集的风险。\n\n【5 维度打分】:\n\n1. **研究问题: 强** — 问题定义精准且有实际价值。\"为什么单点干预总是 plateau\"是该领域的核心困惑，补偿动力学假设提供了一个可证伪的解释。Competition of Mechanisms 的泛化研究（arXiv:2506.22977）证实大模型中 override 机制更分布式，进一步支持了多点协同干预的必要性。无论假设成立与否，结果都有信息量（proposal 正确指出了这一点）。\n\n2. **方法与创新: 中偏强** — 组合 CD-T + PEAP 进行 RAG 电路发现是新颖的应用创新，三点协同干预在该领域确实首创。但各组件（CD-T、PEAP、entropy neuron ablation）均为已有工具的组合应用而非方法论发明。与 CLEAR（arXiv:2510.12460）相比，CORe 在因果性（causal vs. probing）和组件覆盖度（三组件 vs. 仅注意力）上有清晰优势，但 CLEAR 的端到端可操作性可能更好。几何统一假设（连接 Simulated Adoption + Marín 2026 + Promote-Suppress-Iterate）是最具原创性的理论贡献，但也是最投机的。\n\n3. **实验设计: 强** — 这是 proposal 最突出的维度。3 架构 × 4 数据集 × 7+ baseline（含 Naive Stack 这一关键对照）× 7 ablation 配置 × 跨数据集迁移性测试 × 无冲突对照 × 统计显著性检验——实验矩阵的完备度超过了大多数同领域已发表论文。特别值得肯定：(a) Naive Stack baseline 直接检验核心 claim；(b) 电路迁移性测试关乎实用性；(c) 推理效率对比考虑了摊销成本。相比 JuICE（ICML 2025）和 ParamMute（NeurIPS 2025）的实验设计，CORe 的实验方案更全面。唯一缺失：没有提及 human evaluation 或 case study 分析（虽然对 QA 任务非必需但可加分）。\n\n4. **可行性: 中** — 这是主要短板之一。(a) **Scope 过大**：三个阶段（电路发现 → 几何特征化 + 补偿动力学测试 → 协同干预）中每一个都足以独立成文，在一篇论文中完成全部且都做到 solid 的概率不高。(b) **CD-T 规模化风险**：尽管 proposal 提到了 pilot study 和 HAGD 回退方案，但 8B 模型 + 长 RAG 上下文的电路发现在实践中可能遇到未预见的困难。(c) **校准复杂度**：3 组件 × 3-5 强度 × 3 几何模式 = 大量超参数组合，需要精心调优。(d) **积极面**：回退方案设计周全（CD-T 失败→HAGD；flip 不普遍→仅用 Phase 1 归因分数；分数融合退化→纯管线），表明作者对风险有清醒认识。\n\n5. **写作与呈现: 强** — Proposal 的逻辑结构清晰，从问题（单点干预 plateau）→ 假设（补偿动力学）→ 方法（三阶段管线）→ 评估的叙事链条完整有力。对每个相关工作的定位精准且公允（不贬低前人工作，而是准确指出局限）。Gap statement 有说服力。技术描述具体到可复现程度（如 flip 事件的操作性定义、CD-T 候选分数的归一化方式）。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n**上推因素（→42%）：** 研究问题精准、实验设计极其完备（特别是 Naive Stack baseline 和 ablation 矩阵）、文献综述深度罕见、写作质量高、填补的空白真实存在。如果补偿动力学假设成立且电路发现方法在 8B 模型上可行，这篇论文的贡献将非常显著。\n\n**下拉因素（→28%）：** (1) Scope 是最大风险——三个阶段的工作量和不确定性叠加，审稿人可能认为\"做了很多但每个部分都不够深入\"；(2) 核心假设（补偿动力学）完全推测性，无前序 LLM 实验证据（仅有神经科学类比），一旦不成立，叙事的说服力显著下降（虽然 Phase 1 电路发现和 Phase 3 干预仍有独立价值）；(3) CD-T+PEAP 在 8B 规模 RAG 任务上的验证真空——pilot study 可能发现不可逾越的障碍；(4) 方法本质是已有工具（CD-T、PEAP、entropy neuron ablation、JuICE 式头干预、ParamMute 式 FFN 抑制）的系统整合，审稿人可能质疑\"方法论新颖性在哪里\"。\n\n**中位 35% 的定位依据：** 这份 proposal 在问题定义和实验设计上属于领域上游水平，显著优于平均投稿。但 scope 过大 + 核心假设投机性 + 方法为组合创新而非原创方法 三者叠加，使其处于 borderline accept 的区间。在 AAAI 的审稿流程中，这类 proposal 的命运高度依赖于审稿人分配——遇到重视 mechanistic interpretability 和实验设计的审稿人可能获得 accept，遇到看重方法论原创性的审稿人则可能被拒。\n\n【主要风险】:\n1. **Scope 过载导致审稿人质疑深度**：三阶段管线中任一阶段的实验如果做得不够深入（例如 Phase 2 几何统一仅是初步观察而非严格验证），整体论文会被视为\"广而不深\"。审稿人可能建议\"拆成两篇论文\"——这在顶会中是常见的 reject 理由。\n2. **补偿动力学假设不成立或效应很弱**：如果单路径 ablation 后其他路径的补偿效应在统计上不显著，核心叙事（\"协同干预之所以有效是因为需要同时阻断补偿通路\"）将缺乏支撑。此时 CORe 退化为\"用更好的方法选择干预目标\"，其相对于 JuICE/CoRect 的优势将大幅缩小。\n\n【实施评估】:\n  - **计算资源**: 高。需对 3 个 8B 模型分别运行 CD-T + PEAP 电路发现（CD-T 声称高效但未在 8B+长上下文验证），加上 7 ablation × 4 数据集 × 3 模型 × 3 运行的评估矩阵。估计需 4-8 块 A100 80G，总 GPU 时数约 200-500 小时。\n  - **数据需求**: 中低。使用已有公开数据集（NQ-swap、ConFiQA、CoFaithfulQA、MemoTrap），无需构建新数据。\n  - **人工介入**: 中。电路图的解读和验证、干预强度的初始校准、flip 事件的质量检查可能需要研究者手动参与。\n  - **训练需求**: 无模型训练。纯推理时干预 + 一次性电路发现。\n  - **新 Benchmark**: 不需要。\n  - **预估周期**: 3-5 个月。Phase 1（电路发现 + pilot study）~6-8 周；Phase 2（几何特征化 + 补偿动力学测试）~4-6 周；Phase 3（干预实现 + 全矩阵评估）~4-6 周；写作 ~3-4 周。如果 CD-T 遇到规模化问题需要切换到 HAGD，额外 2-3 周。\n```\n\nSources:\n- [JuICE: Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)\n- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification (arXiv 2026)](https://arxiv.org/abs/2602.08221)\n- [ParamMute: Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://arxiv.org/abs/2502.15543)\n- [SpARE: SAE-Based Representation Engineering (NAACL 2025)](https://arxiv.org/abs/2410.15999)\n- [CD-T: Efficient Automated Circuit Discovery (ICLR 2025)](https://arxiv.org/abs/2407.00886)\n- [PEAP: Position-aware Automatic Circuit Discovery (ACL 2025)](https://aclanthology.org/2025.acl-long.141/)\n- [Competition of Mechanisms (ACL 2024)](https://arxiv.org/abs/2402.11655)\n- [On the Generalizability of Competition of Mechanisms (arXiv 2025)](https://arxiv.org/abs/2506.22977)\n- [Simulated Adoption (arXiv 2026)](https://arxiv.org/abs/2602.04918)\n- [How Transformers Reject Wrong Answers (arXiv 2026)](https://arxiv.org/abs/2603.13259)\n- [Context Copying Modulation: Entropy Neurons (EMNLP 2025)](https://arxiv.org/abs/2509.10663)\n- [CLEAR: Probing Latent Knowledge Conflict (arXiv 2025)](https://arxiv.org/abs/2510.12460)\n- [JuICE GitHub Repository](https://github.com/GaotangLi/JUICE)\n- [ParamMute GitHub Repository](https://github.com/OpenBMB/ParamMute)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [JuICE / Taming Knowledge Conflicts in Language Models](https://arxiv.org/abs/2503.10996) (ICML 2025 Spotlight): 发现注意力头的\"superposition\"现象（同一头同时促进记忆和上下文），提出dual-run头级干预，11数据集SOTA。CORe的最直接基线之一，CORe需在此基础上证明多组件协调干预的增量价值。\n- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221) (arXiv Feb 2026): 记录了flip phenomenon（正确答案在中间层出现后被深层FFN抑制），提出对比logit方法做hidden state矫正。CORe Phase 2a的geometric unification直接建立在此发现之上，但CORe声称提供因果解释而非相关性检测。\n- [SpARE / SAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.264/) (NAACL 2025 Oral): 用SAE特征做steering，+10% EM，但目标选择基于单层互信息排名。CORe声称通过因果归因提供更principled的目标选择。\n- [ParamMute: Suppressing Knowledge-Critical FFNs](https://arxiv.org/abs/2502.15543) (NeurIPS 2025): 识别中深层FFN（70%-90%相对深度）为不忠实生成的关键，通过抑制这些FFN提升忠实度。单组件类型干预，CORe的直接对比对象。\n- [Simulated Adoption: Decoupling Magnitude and Direction](https://arxiv.org/abs/2602.04918) (arXiv Feb 2026): 发现冲突解决通过正交干扰（几何旋转而非幅度抑制）实现，跨Llama-3.1-8B/Qwen-3-4B/GLM-4-9B验证。CORe Phase 2a的geometric unification的关键输入之一。\n- [Context Copying Modulation / Entropy Neurons](https://aclanthology.org/2025.findings-emnlp.1116/) (EMNLP 2025 Findings): 发现entropy neurons（<0.2% FFN神经元）在最后transformer层抑制上下文复制。CORe第三干预点（copy suppression inhibition）的机制基础。\n- [CLEAR: Probing Latent Knowledge Conflict](https://arxiv.org/abs/2510.12460) (arXiv Oct 2025): 三阶段干预（知识分解→探针定位→注意力调制），但基于probing相关性（非因果）、需微调、仅调制注意力。CORe区分自身的重要对比点。\n- [CD-T / Efficient Automated Circuit Discovery](https://arxiv.org/pdf/2407.00886) (ICLR 2025): 基于Contextual Decomposition的电路发现方法，声称transformer-agnostic可扩展性。CORe Phase 1的核心工具之一。\n- [Competition of Mechanisms](https://arxiv.org/abs/2506.22977) (ACL 2024 + arXiv 2025 generalization study): 追踪factual recall vs. in-context copying的竞争，发现Llama 3.1 8B中头专门化减弱，暗示override circuits在大模型中更分布式。直接支持CORe的分布式电路假说。\n\n- **调研总结**: RAG知识冲突领域正处于从\"单组件启发式干预\"向\"机制理解驱动的系统干预\"转型的节点。JuICE、SpARE、ParamMute等单组件方法各自取得了显著进展但都有天花板。几何理解（旋转vs.幅度）正在独立涌现但尚未统一。CORe的定位——因果电路追踪+几何统一+多点协调干预——准确地占据了一个尚无人填充的空白，时机恰好。\n\n【整体印象】:\n作为审稿人，我的第一反应是\"这是一份精心构建的、野心很大的proposal\"。研究问题切中要害——为什么单点干预会plateau？——这是领域内practitioners普遍感受到但尚无人系统性回答的问题。compensatory dynamics假说优雅且可测试，\"无论结果如何都有价值\"的双向设计体现了科学诚实性。文献综述异常全面，清晰地建立了gap。\n\n倾向：**Weak Accept**。问题好、方法有理、实验设计扎实，但scope过于宏大是最大隐患——在一篇论文中同时做电路发现、几何统一、三点干预，任何一个phase出问题都可能导致整体叙事断裂。如果执行良好、结果positive，这是一篇strong paper；但执行风险不容忽视。\n\n【核心贡献】:\n1. **Compensatory dynamics假说及其实证验证**: 首次提出并检验RAG override circuit中的补偿动力学，为单点干预plateau提供因果解释。这是最核心的科学贡献。\n2. **位置感知因果电路追踪应用于RAG**: 将CD-T/PEAP pipeline应用于RAG context-parametric冲突场景，产出可解释的circuit graph。\n3. **几何统一**: 将flip phenomenon、旋转抑制、多阶段promote-suppress动力学统一为一个框架（如果成功）。\n4. **Geometry-aware coordinated 3-point intervention**: 基于电路和几何诊断的多点推理时干预，配合naive stack baseline直接检验协调的价值。\n\n核心贡献对领域的价值：**中到高**。如果compensatory dynamics被验证，这改变了领域对\"为什么干预失败\"的理解，具有paradigm-shifting潜力。即使只是部分验证，位置感知电路追踪和predictive diagnostics也有独立价值。\n\n【方法合理性】:\n方法整体合理，逻辑链条清晰（电路发现→几何刻画→干预设计）。几个关键点：\n\n1. **CD-T + PEAP pipeline**: 这两个工具各自在ICLR 2025和ACL 2025发表，有独立验证。但它们从未在RAG场景下组合使用，组合后的效果未知。CD-T在8B模型上的可扩展性是实际风险，pilot study的设计是明智的，HAGD fallback也合理。\n2. **Compensatory dynamics测试**: 方法设计合理——ablate一种pathway，测量其他pathway的override贡献是否增加。这是标准的因果检验范式。\n3. **Geometry-aware calibration**: rotation-dominant → project out; magnitude-dominant → scale; mixed → hybrid。逻辑清晰，但per-instance的几何类型判断可能引入额外复杂性和噪声。\n4. **更简单的替代方案？** Naive stack baseline直接回答了这个问题。如果naive stack已经很好，那么circuit-guided coordination的额外价值会被质疑。但这也正是proposal设计的优点——它主动设置了这个检验。\n\n主要方法论风险：Phase 2a的geometric unification涉及三个独立发现（CoRect的flip、Simulated Adoption的旋转、Marín的球面旋转），它们可能不收敛为一个统一机制，特别是在不同架构上。\n\n【5 维度打分】:\n  1. 研究问题: **强** — \"为什么单点干预plateau\"是领域内公认的开放问题，JuICE/SpARE/ParamMute/CoRect各自SOTA但各有天花板，compensatory dynamics假说提供了一个可测试的因果解释。双向假设设计（存在/不存在compensatory dynamics都有科学价值）进一步增强了研究问题的robustness。研究问题同时服务于理解（为什么）和工程（怎么办），兼具科学价值和应用价值。\n  \n  2. 方法与创新: **中偏强** — CD-T（ICLR 2025）+ PEAP（ACL 2025）的组合在RAG场景的应用是新颖的，geometry-aware calibration有创新性。但核心工具都是已有方法的组合应用，创新更多在\"组合方式\"而非\"基础方法\"层面。与JuICE（发现superposition现象）、SpARE（SAE特征应用于steering）、ParamMute（识别关键FFN层）相比，CORe的方法创新更偏\"系统集成\"。审稿人可能会质疑：这是一个新方法还是已有方法的pipeline？需要通过compensatory dynamics的实证发现来证明组合不是简单拼接。\n  \n  3. 实验设计: **强** — 这是proposal最亮的部分之一。7配置ablation matrix直接检验核心假设；naive stack baseline是关键设计，主动回答\"为什么不简单叠加\"；3模型×4数据集覆盖全面；no-conflict control防止过度干预；circuit transferability测试实用价值高；inference efficiency对比（单pass hooks vs. 双run方法）体现工程关注。统计严格性（3 runs + paired bootstrap）也到位。缺一个adversarial analysis——如果模型在circuit discovery时看到的冲突模式与test时不同怎么办？\n  \n  4. 可行性: **中** — 这是最大的风险维度。三个phase中每个都有不小的执行风险：(1) CD-T在8B模型上的runtime/memory未知，pilot study是必要但结果可能不乐观；(2) geometric unification可能在不同架构上表现不一致；(3) 三点干预的参数空间（3-5强度值×3组件×7配置×3模型×4数据集）实验量巨大。proposal的contingency planning（HAGD fallback、flip不普遍时的退化方案）体现了成熟思考，但整体scope对于一个conference paper来说偏大。成功执行可能需要2-3个月的密集实验期。\n  \n  5. 写作与呈现: **强** — Proposal的文献综述异常全面，每篇相关工作都有精确的定位和差异化分析。Gap identification清晰有力。研究问题的framing（compensatory dynamics）具有很强的narrative coherence。Contingency planning的透明性增强了可信度。术语使用准确。唯一不足：方法描述部分信息密度很高，实际论文需要更多空间展开。\n\n【概率估计】: [30% - 42%] 中位 35%\n\n【估计理由】:\n**上行因素** (推向42%+):\n- 研究问题精准切中领域痛点，novelty claim在调研后确认成立——截至2026年5月无已发表工作组合因果电路追踪+多点RAG干预\n- 实验设计非常完备，naive stack baseline的设置是审稿人最想看到的关键对照\n- 文献综述的深度和精确度超出大多数submissions，体现了对领域的深刻理解\n- compensatory dynamics如果被验证，贡献级别可达Best Paper候选\n\n**下行因素** (推向30%以下):\n- Scope过大：三个phase中任何一个出问题（CD-T不可扩展、geometric unification不收敛、compensatory dynamics不存在），整个narrative就要重构\n- 方法创新更偏\"系统集成\"，审稿人可能认为这是engineering contribution而非scientific contribution\n- 如果compensatory dynamics不存在（这完全可能），paper虽仍有价值但narrative力度大幅下降\n- 如果naive stack已经工作得很好，circuit-guided coordination的额外价值可能不够显著\n\n**中位判断** (35%):\n这是一篇\"高风险高回报\"的投稿。研究问题好、设计扎实、gap真实存在。如果结果positive（compensatory dynamics存在 + 协调干预显著优于naive stack + 几何统一成功），这是40%+的strong accept候选。但如果任一核心假设不成立或execution不到位，可能落入\"ambitious but inconclusive\"的reject区间。35%的中位反映了：好的问题+好的设计 vs. 高执行风险+过大scope的权衡。\n\n【主要风险】:\n1. **Scope过大导致执行不完整**: 三个phase的完整执行（3模型×4数据集×7 ablation配置 + 几何分析 + 电路发现）工作量极大，deadline压力下很可能某些phase不够深入，导致审稿人认为\"每个方面都浅尝辄止\"。如果只能完整做好一部分，建议优先Phase 1 + compensatory dynamics test + 3-point intervention，geometric unification可作为supporting analysis而非主要贡献。\n2. **核心假设（compensatory dynamics）可能不成立**: 如果ablate一种pathway后其他pathway的override贡献并不增加，那么\"为什么单点干预plateau\"的问题回到原点。paper的\"value regardless of outcome\"framing能部分缓解，但审稿人可能认为negative result的价值不足以支撑一个AAAI oral/poster。\n\n【实施评估】:\n  - 计算资源: **高**。CD-T在8B模型上的decomposition + PEAP的forward/backward pass + 3模型×4数据集×7 ablation配置的完整实验矩阵。估计需要4-8× A100 80GB持续运行。Pilot study至关重要，可能需要1-2周GPU时间仅用于可行性验证。\n  - 数据需求: **中低**。NQ-swap、ConFiQA、MemoTrap、CoFaithfulQA均为已有公开数据集，无需构建新数据集。但可能需要自建部分conflict prompts用于circuit discovery phase的精细控制。\n  - 人工介入: **低至中**。电路图的解读和geometric analysis需要专家判断，但整体pipeline高度自动化。Intervention strength calibration可能需要一定手动调参。\n  - 训练需求: **无**。全部干预在推理时通过forward hooks实现，不需要模型训练或微调。这是CORe相对CLEAR的重要优势。\n  - 新 Benchmark: **无需**。使用已有benchmark组合。CoFaithfulQA（ParamMute引入）已可用。\n  - 预估周期: **3-4个月**（含pilot study 2-3周 + Phase 1电路发现 3-4周 + Phase 2几何分析和compensatory dynamics测试 3-4周 + Phase 3干预实现和完整实验 4-5周 + 论文写作 3-4周）。如果精简scope（例如减少模型数量或简化geometric unification），可压缩至2.5-3个月。\n```\n\n---\n\nSources:\n- [Taming Knowledge Conflicts in Language Models (JuICE) - ICML 2025](https://arxiv.org/abs/2503.10996)\n- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221)\n- [SpARE: Steering Knowledge Selection via SAE-Based Representation Engineering - NAACL 2025](https://aclanthology.org/2025.naacl-long.264/)\n- [ParamMute: Suppressing Knowledge-Critical FFNs for Faithful RAG - NeurIPS 2025](https://arxiv.org/abs/2502.15543)\n- [Simulated Adoption: Decoupling Magnitude and Direction in LLM Conflict Resolution](https://arxiv.org/abs/2602.04918)\n- [Context Copying Modulation: The Role of Entropy Neurons - EMNLP 2025 Findings](https://aclanthology.org/2025.findings-emnlp.1116/)\n- [CLEAR: Probing Latent Knowledge Conflict for Faithful RAG](https://arxiv.org/abs/2510.12460)\n- [CD-T: Efficient Automated Circuit Discovery via Contextual Decomposition](https://arxiv.org/pdf/2407.00886)\n- [JuICE GitHub Repository](https://github.com/GaotangLi/JUICE)\n- [ParamMute GitHub Repository](https://github.com/OpenBMB/ParamMute)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [JuICE: Taming Knowledge Conflicts in Language Models](https://arxiv.org/abs/2503.10996) (ICML 2025 Spotlight): 发现注意力头的 superposition 现象（同一头同时促进 memory 和 context），提出 dual-run 头级干预，11 个数据集上取得 SOTA。是本 proposal 最直接的 baseline 和动机来源——JuICE 仅做头级干预，未涉及 FFN 或 copy suppression。\n- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221) (arXiv Feb 2026): 发现 flip 现象（正确答案在中间层出现后被深层 FFN 抑制），通过 logit 对比进行 additive rectification。仅干预 FFN 层，无电路级诊断。CORe 的 Phase 2 直接试图解释 flip 的几何机制。\n- [ParamMute: Suppressing Knowledge-Critical FFNs](https://arxiv.org/abs/2502.15543) (NeurIPS 2025): 识别 70%-90% 相对深度的 FFN 层为不忠实生成的关键层，通过抑制实现 faithfulness 提升。单组件干预，统计识别。CORe 的 FFN 干预点与之重叠但采用因果归因而非统计方法。\n- [SpARE: SAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.264/) (NAACL 2025 Oral): 利用 SAE 特征进行 steering，仅选择单一中间层点的 0.05% SAE 激活，+10% EM。单点、单层干预。\n- [PEAP: Position-aware Automatic Circuit Discovery](https://aclanthology.org/2025.acl-long.141/) (ACL 2025): 引入 dataset schema 实现位置感知电路发现，比位置无关电路更小更精确。CORe Phase 1 的核心工具之一。\n- [CD-T: Efficient Automated Circuit Discovery via Contextual Decomposition](https://arxiv.org/abs/2407.00886) (ICLR 2025): 基于数学分解（非 activation patching）的电路发现，声称 transformer-agnostic 可扩展性。CORe Phase 1 的另一核心工具。\n- [Simulated Adoption](https://arxiv.org/abs/2602.04918) (arXiv Feb 2026): 发现知识冲突解决中的正交干扰机制——模型通过几何旋转而非幅度抑制来绕过正确答案。CORe Phase 2 试图将此发现与 CoRect flip 和 Marín 的旋转动力学统一。\n- [Context Copying Modulation](https://aclanthology.org/2025.findings-emnlp.1116/) (EMNLP 2025 Findings): 发现 entropy neurons（不到 0.2% 的 FFN 神经元）在最后 transformer 层中显著抑制 context copying。CORe 的第三干预点（copy suppression 抑制）直接基于此发现。\n- [Competition of Mechanisms](https://arxiv.org/abs/2305.14251) (ACL 2024) + [泛化研究](https://arxiv.org/abs/2506.22977): 追踪 factual recall vs. in-context copying 竞争，但泛化研究发现头部特化在大模型中显著减弱，暗示 override 电路更加分布式。\n- [MAT-STEER: Multi-Attribute Targeted Steering](https://arxiv.org/abs/2502.12446) (2025): 解决多属性 ITI 中的冲突问题，但针对属性控制而非知识冲突，且未采用电路级分析。\n- [CLEAR](https://arxiv.org/abs/2510.12460) (arXiv Oct 2025): 三阶段干预（pruning→probing→modulation），最接近 CORe 的多阶段范式，但使用 probing 相关性（非因果）、需要 fine-tuning、仅调制 attention。CORe 在因果性、推理时干预、多组件覆盖三方面有明确差异化。\n\n- 调研总结: RAG 知识冲突是 2024-2026 年的高热度研究方向，已有大量单组件干预方法（JuICE/CoRect/SpARE/ParamMute/IRCAN）和几何机制分析（Simulated Adoption/旋转动力学）。然而，现有工作普遍局限于单一组件类型的干预，且未建立因果电路级理解来解释为何单点干预遇到瓶颈。CORe 占据了一个真实且清晰的研究空位：因果电路追踪 + 几何统一 + 协调多点干预。这个空位既不是臆造的，也尚未被已有工作填补。\n\n【整体印象】:\n作为审稿人，第一反应是 \"这是一个准备充分、问题意识清晰、实验设计严谨的 proposal\"。作者对领域现状的理解深度令人印象深刻——从 JuICE 的 superposition 到 CoRect 的 flip 现象，从 Simulated Adoption 的正交干扰到 entropy neurons 的 copy suppression，每一个相关发现都被精准地编织进叙事链。核心假设（补偿动力学导致单点干预瓶颈）具有可证伪性，且无论结果如何都有科学价值。\n\n然而，这个 proposal 的野心也是其最大风险。三个 Phase 实质上是三篇独立论文的工作量压缩进一篇：(1) RAG override 电路的因果发现，(2) 几何机制的统一解释，(3) 协调多点干预方法。如果执行到位，这将是一篇非常有影响力的论文；但如果任何一个 Phase 的结果不如预期，整个叙事链可能断裂。\n\n倾向：**Borderline accept / weak accept**。问题重要、方法有依据、实验设计出色，但执行风险高且可能被批评为\"组合现有工具的工程工作\"。\n\n【核心贡献】:\n1. **首个 RAG override 电路的因果图谱**（Phase 1）：将 CD-T 和 PEAP 这两个通用电路发现工具应用于 RAG 知识冲突场景，产出位置感知的因果电路归因——这本身就是一个有价值的 artifact，即使后续干预效果平平。\n2. **补偿动力学的实证验证**（Phase 2b）：直接测试\"单点干预失败是否因为其他路径补偿\"这一假设，为理解现有方法瓶颈提供因果解释。\n3. **几何统一框架**（Phase 2a）：将 flip 现象、正交干扰、旋转抑制三个独立发现统一到 RAG override 的几何解释中。\n4. **协调 3 点推理时干预**（Phase 3）：基于电路级理解的 FFN + attention head + copy suppression 同时干预，配以几何感知的校准策略。\n\n核心贡献对领域的价值：**高**。如果补偿动力学假设成立，这将改变该领域对干预方法设计的思维范式——从\"找到最重要的单一组件\"转向\"理解分布式电路并协调干预\"。即使假设不成立，因果电路图谱和几何分析本身也是有价值的科学发现。\n\n【方法合理性】:\n方法整体上是合理的，但存在若干需要审慎评估的点：\n\n**合理之处：**\n- CD-T → PEAP 的 pipeline 设计有据可循：CD-T 做粗筛（数学分解，计算高效），PEAP 做精细化（位置感知边归因）。两者互补而非冗余。\n- 几何感知校准（rotation-dominant → project out; magnitude-dominant → scale）在 Simulated Adoption 和 Marín 2026 的发现基础上逻辑自洽。\n- 单 pass forward hooks 实现干预，避免了 JuICE 的 dual-run 开销，实际部署更友好。\n- Naive Stack baseline 的设置是方法论上的亮点——直接检验 \"电路指导是否优于朴素组合\"。\n\n**需要质疑之处：**\n- CD-T 和 PEAP 都未在 RAG 知识冲突场景下验证过，它们最初是为更简单的任务设计的（如间接对象识别、主谓一致）。RAG 的三方交互（query → evidence → parametric override）是否超出这些工具的有效范围是未知的。\n- **更简单的替代方案**：审稿人可能会问——是否可以直接用 activation patching / causal tracing（à la Meng et al. 2022）配合 RAG 特定 prompt 来发现电路，而不需要 CD-T + PEAP 的复杂 pipeline？proposal 未充分论证为何更简单的因果追踪方法不够用。\n- Phase 2a 的几何统一是否真的需要？一个审稿人可能认为，Phase 1 的电路发现 + Phase 3 的协调干预已经足够构成一篇完整的贡献，Phase 2a 的几何统一增加了复杂度但可能不是必需的。\n- 三个干预点的\"协调\"具体如何实现？proposal 提到 \"geometry-aware calibration\"，但具体的优化目标函数或校准算法未明确描述——这留下了方法细节的空白。\n\n【5 维度打分】:\n\n1. 研究问题: **强** — \"为什么单点干预会遇到瓶颈\"是该领域一个真实且重要的问题。JuICE (ICML 2025 Spotlight)、CoRect、SpARE、ParamMute 各自独立取得了显著进展，但都局限于单一组件类型，且性能提升似乎开始饱和。提出\"补偿动力学\"假设为这一瓶颈提供了可证伪的因果解释，且 Competition of Mechanisms 泛化研究（arXiv:2506.22977）发现头部特化在大模型中减弱——间接支持了 override 电路更分布式的假设。问题定义清晰、有足够的前置证据支撑、且有明确的科学价值。\n\n2. 方法与创新: **中偏强** — 方法的创新性主要体现在：(a) 将 CD-T（ICLR 2025）和 PEAP（ACL 2025）组合应用于 RAG 知识冲突的电路发现——这是新的应用场景，但工具本身不是新的；(b) 协调 3 点干预的思路是新颖的——现有方法（JuICE 头级、ParamMute FFN级、entropy neuron 级）各自独立，无人尝试过基于电路理解的协调干预；(c) 几何统一框架连接了 Simulated Adoption、CoRect flip、Marín 旋转动力学三个独立发现。然而，核心方法论贡献更多是\"正确地组合现有工具\"而非\"发明新工具\"，这可能被部分审稿人视为工程组合而非方法论创新。与 CLEAR（arXiv:2510.12460）相比，CORe 在因果性和组件覆盖面上有明确优势，但 CLEAR 至少有（probing-based 的）实证结果。\n\n3. 实验设计: **强** — 这是 proposal 最出色的方面。(a) 3 个不同架构（Llama/Qwen/Gemma）确保跨模型泛化性；(b) 4 个覆盖不同冲突类型的数据集（entity substitution/multi-hop/faithfulness/memorization-trap）；(c) 7 个 baseline 包含各主要方法流派（头级 JuICE、FFN 级 CoRect/ParamMute、SAE 级 SpARE、解码级 CoCoA、神经元级 IRCAN），且关键地包含了 Naive Stack baseline——这直接测试核心 claim；(d) 7 配置的 ablation matrix（A/B/C/AB/AC/BC/ABC）完整覆盖所有组合；(e) no-conflict control 确保干预不损害正常生成；(f) circuit transferability 测试实际部署可行性；(g) predictive diagnostics 增加可解释性价值；(h) 统计严谨性（3 runs + paired bootstrap）。唯一缺失：未提及更大规模模型（70B+）的可扩展性评估，但对于 proposal 阶段这是合理的。\n\n4. 可行性: **中** — 存在显著的执行风险。(a) CD-T + PEAP pipeline 在 8B 模型上的计算可行性是真实的不确定性——proposal 承认了这一点并提出了 pilot study 和 HAGD fallback，这是负责任的；(b) 三个 Phase 的顺序依赖意味着 Phase 1 的延迟或失败会级联影响后续所有工作；(c) 3 模型 × 4 数据集 × 7+ baseline × 7 ablation 配置 = 大量实验，保守估计需要数百 GPU 小时；(d) Phase 2a 的几何统一可能需要大量的分析和可视化工作，难以预估时间；(e) 如果补偿动力学不存在，叙事需要显著调整。总体上，一个 3-4 人团队在 3-4 个月内完成是可能的，但紧张。\n\n5. 写作与呈现: **强** — Proposal 本身的写作质量极高。(a) 问题-现有方法局限-假设-方法-实验的逻辑链清晰完整；(b) 相关工作覆盖全面且时效性极强（引用到 2026 年 4 月的 arXiv 预印本）；(c) 与每一个相关工作的差异化都有明确阐述（特别是与 CLEAR 的三点差异）；(d) 每个 Phase 都有 contingency plan（HAGD fallback、flip 不普遍时的降级策略），显示成熟的研究规划；(e) \"value regardless of outcome\" 的框架是科学上诚实的。唯一的担忧是：将三个 Phase 的内容压缩进一篇 8 页论文可能导致方法细节不足。\n\n【概率估计】: [25% - 40%] 中位 33%\n\n【估计理由】:\n**上调因素（→40%）：** (1) 问题高度时效且重要——RAG 知识冲突是 2025-2026 年的热门方向，AAAI 审稿人大概率对此感兴趣；(2) 占据了一个真实且清晰的研究空位——没有现有工作结合因果电路追踪与多点协调干预；(3) 实验设计极其扎实——naive stack baseline、完整 ablation、跨模型/跨数据集评估、statistical rigor，几乎没有可攻击的实验设计漏洞；(4) 写作/叙事质量高，审稿人阅读体验好；(5) 有 fallback 方案应对各种不确定性。\n\n**下调因素（→25%）：** (1) **方法论创新的\"组合\"质疑**——核心工具（CD-T、PEAP、entropy neuron ablation、attention intervention）全部来自已有工作，CORe 的创新是\"正确地组合\"它们，部分审稿人可能认为这是 engineering contribution 而非 scientific contribution；(2) **执行风险极高**——三个顺序依赖的 Phase，任何一个结果不如预期都可能导致叙事断裂；(3) **补偿动力学假设可能不成立**——虽然 proposal 声称\"value regardless of outcome\"，但实际上如果核心假设被否定，论文的影响力和故事完整性会大打折扣；(4) **范围过广**——电路发现 + 几何统一 + 协调干预，对于一篇 8 页论文来说内容过于密集，可能导致每个部分都浅尝辄止；(5) **AAAI 2026 审稿周期压力**——proposal 引用了多篇 2026 年初的预印本，说明领域发展极快，在 proposal → 提交的窗口期内可能出现直接竞争的工作。\n\n**中位 33% 的依据：** 这是一个\"方向正确、设计精良但执行风险高\"的 proposal。在 AAAI 的双盲审稿中，它很可能收到 1-2 个正面评价（赞赏问题定义和实验设计）和 1 个负面评价（质疑方法创新性或范围过广），最终处于 borderline 区域。AC 的决定将取决于 rebuttal 中是否能提供初步实验证据（至少 Phase 1 的 pilot 结果）来回应执行风险的质疑。\n\n【主要风险】:\n1. **\"组合创新\"质疑**：审稿人可能认为 CORe 的核心贡献是将已有工具（CD-T、PEAP、entropy neurons、attention intervention）组合应用于 RAG 场景，而非提出根本性新方法。Rebuttal 需要强调：(a) 组合本身需要非平凡的协调信号（这正是 naive stack baseline 要验证的），(b) 电路图谱和补偿动力学发现是独立的科学贡献。\n2. **范围过广导致深度不足**：三个 Phase（电路发现 / 几何统一 / 协调干预）中任何一个都可以独立成文。压缩到一篇论文可能导致方法细节不足，审稿人难以判断技术可行性。建议考虑将 Phase 2a（几何统一）降级为辅助分析而非核心贡献，集中力量在\"电路发现 → 补偿动力学验证 → 协调干预\"的主线上。\n\n【实施评估】:\n  - 计算资源: 高。3 个 8B 模型 × 4 数据集 × (CD-T + PEAP pipeline + 7 baseline + 7 ablation) = 保守估计 500-1000 GPU 小时（A100 80GB）。Phase 1 电路发现是计算瓶颈。\n  - 数据需求: 中低。NQ-swap、ConFiQA、CoFaithfulQA、MemoTrap 均为公开数据集，无需新数据收集。\n  - 人工介入: 低。方法为全自动 pipeline，但电路图谱的解读和可视化需要研究者的分析判断。\n  - 训练需求: 无。所有干预都是推理时进行（forward hooks），不修改模型参数——这是一个显著优势。\n  - 新 Benchmark: 否。使用已有 benchmark。\n  - 预估周期: 3-4 个月。Phase 1 pilot study（2-3 周）→ Phase 1 full（3-4 周）→ Phase 2（3-4 周）→ Phase 3 + 全部实验（4-5 周）→ 写作（2-3 周）。团队规模 3-4 人时可适度并行化。\n```\n\nSources:\n- [JuICE: Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)\n- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification (arXiv 2026)](https://arxiv.org/abs/2602.08221)\n- [ParamMute: Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://arxiv.org/abs/2502.15543)\n- [SpARE: SAE-Based Representation Engineering (NAACL 2025)](https://aclanthology.org/2025.naacl-long.264/)\n- [PEAP: Position-aware Automatic Circuit Discovery (ACL 2025)](https://aclanthology.org/2025.acl-long.141/)\n- [CD-T: Efficient Automated Circuit Discovery via Contextual Decomposition (ICLR 2025)](https://arxiv.org/abs/2407.00886)\n- [Simulated Adoption: Decoupling Magnitude and Direction (arXiv 2026)](https://arxiv.org/abs/2602.04918)\n- [Context Copying Modulation: Entropy Neurons (EMNLP 2025 Findings)](https://aclanthology.org/2025.findings-emnlp.1116/)\n- [Competition of Mechanisms Generalization Study](https://arxiv.org/abs/2506.22977)\n- [JuICE GitHub Repository](https://github.com/GaotangLi/JUICE)\n- [ParamMute GitHub Repository](https://github.com/OpenBMB/ParamMute)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# CORe: Tracing and Repairing Override Circuits in RAG\n\n## Core Problem and Primary Research Question\n\nRAG-augmented LLMs systematically override retrieved evidence with parametric memory during knowledge conflicts. Existing interventions (SpARE, CoRect, JuICE, IRCAN) target single component types selected via statistical heuristics, yet consistently plateau in performance. We hypothesize this plateau stems from compensatory dynamics within a distributed override circuit: the override mechanism spans attention heads, FFN layers, and copy suppression components with redundant pathways, so repairing one node causes others to compensate and restore the parametric override.\n\n**Primary research question:** Does the RAG override circuit exhibit compensatory dynamics — and if so, does coordinated multi-point intervention that addresses all compensatory pathways simultaneously outperform both single-point methods and naive stacking of independent single-point interventions?\n\nThis question has value regardless of outcome: if compensatory dynamics exist, they provide the first causal explanation for single-point intervention plateaus and necessitate coordinated repair; if they do not, then single-point failures stem from wrong target selection, and causal circuit tracing still provides principled target identification that heuristic methods lack.\n\n**Why naive stacking is insufficient:** Simply combining existing methods (e.g., JuICE head amplification + ParamMute FFN suppression + entropy neuron ablation) without circuit-level understanding risks: (1) contradictory intervention directions at shared components (a head amplified by JuICE may belong to a pathway that ParamMute needs dampened); (2) uncontrolled interaction effects without principled strength calibration; (3) no diagnostic capability to determine which combination is appropriate per instance. Causal circuit tracing provides the coordinating signal that naive stacking lacks.\n\n## Research Landscape\n\n**Single-component heuristic interventions (current paradigm):**\nJuICE (ICML 2025 Spotlight) discovered attention head superposition (same head promotes both memory and context), invalidating clean head-type dichotomies (PH3, IRCAN), and proposed dual-run head-level intervention achieving SOTA on 11 datasets — but remains head-level with no FFN or copy suppression analysis. CoRect (arXiv Feb 2026, arXiv:2602.08221) documented the flip phenomenon (56% of conflict failures: correct answer appears mid-layer then gets suppressed by deep FFN layers) and intervenes with additive rectification, but without circuit-level diagnosis of why specific layers suppress. SpARE (NAACL 2025 Oral) uses SAE features for steering with +10% EM gains, selecting targets via mutual information ranking at a single mid-layer point. ParamMute (NeurIPS 2025, arXiv:2502.15543) identifies mid-to-deep FFN layers (70%-90% relative depth) as critical for unfaithful generation and suppresses them — single component type. IRCAN (NeurIPS 2024) reweights context-aware neurons but uses statistical identification. CoCoA (EMNLP 2025) advances contrastive decoding with confidence-aware token-level adjustment, outperforming CAD and AdaCAD by up to 9.2 points — but operates at decoding level without internal mechanism understanding.\n\n**Multi-stage approaches:**\nCLEAR (arXiv:2510.12460, Oct 2025) implements three-stage intervention: fine-grained knowledge pruning → latent-state probing to localize conflicts → conflict-aware attention modulation. However, CLEAR uses probing-based correlation (no causal guarantee — probing localizes where conflicts manifest, not what causes them), requires conflict-aware fine-tuning (modifying model parameters), and modulates only attention (single component type). CORe differs in three ways: (1) causal circuit attribution via CD-T/PEAP vs. probing correlation; (2) pure inference-time intervention vs. fine-tuning; (3) coordinated 3-component intervention (FFN + attention + copy suppression) vs. attention-only.\n\n**Mechanism-level understanding:**\nCompetition of Mechanisms (ACL 2024) traced factual recall (MLP) vs. in-context copying (induction heads) competition via logit inspection and attention modification. Its generalization study (arXiv:2506.22977) found head specialization weakens substantially in Llama 3.1 8B, suggesting override circuits are more distributed in larger models. CORe addresses the more complex RAG three-way interaction (query → evidence integration → parametric override) rather than binary competition, and designs intervention rather than just tracing. Context Copying Modulation (EMNLP 2025 Findings, arXiv:2509.10663) identified entropy neurons as key components suppressing context copying — providing a mechanistic basis for copy suppression that CORe's third intervention point will leverage, but studied in isolation without connecting to the broader override circuit. PhantomCircuit (EMNLP 2025, arXiv:2505.14406) applied circuit analysis to knowledge overshadowing between training data sources (inter-training-data conflicts, not RAG context-parametric conflicts).\n\n**Geometric understanding:**\nSimulated Adoption (arXiv Feb 2026, arXiv:2602.04918) showed conflict resolution operates via orthogonal interference — geometric rotation rather than magnitude suppression — across Llama-3.1-8B, Qwen-3-4B, and GLM-4-9B. How Transformers Reject Wrong Answers (arXiv Mar 2026, arXiv:2603.13259) independently found that transformers actively suppress correct answers through rotational dynamics on a representation hypersphere, with a phase transition at 1.6B parameters. Promote, Suppress, Iterate (EMNLP 2025) revealed multi-stage promote-then-suppress dynamics. The Override Gap (arXiv Apr 2026, arXiv:2604.23750) found magnitude-dominant failure in hypernetwork-based adaptation (Doc-to-LoRA) — a distinct paradigm from in-context RAG, but cautioning against universalizing geometric assumptions. These three independent geometric findings (Simulated Adoption, Marín 2026, Promote-Suppress-Iterate) have not been unified; CORe's Phase 2 aims to do so specifically in the RAG context.\n\n**Gap:** No existing work combines (1) position-aware causal circuit tracing of RAG override mechanisms, (2) a unified geometric account of why correct answers appear then vanish (connecting the flip phenomenon, rotational suppression, and multi-stage dynamics), and (3) coordinated multi-point inference-time intervention that addresses compensatory pathways. Additionally, no method provides predictive diagnostics — the ability to explain per-instance why a given single-point intervention fails.\n\n## Proposed Approach\n\n**Phase 1 — Circuit Discovery via CD-T → PEAP Pipeline.** Run CD-T on Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B with NQ-swap/ConFiQA/MemoTrap conflict prompts to identify candidate override components (coarse screen). Apply PEAP with query/passage/answer position schemas on the CD-T candidate set to produce position-aware edge attributions (fine-grained refinement). Reconcile both into a unified circuit graph via normalized causal effect scores: each component's score = weighted combination of CD-T decomposition contribution and PEAP gradient attribution, normalized to [0,1] per prompt. Fallback: if reconciliation degrades circuit quality metrics, revert to pure pipeline (CD-T candidates → PEAP edges) without score fusion. Scalability note: CD-T uses mathematical decomposition (not activation patching) and claims transformer-agnostic scalability; PEAP requires 2 forward + 1 backward pass per prompt-pair. A pilot study on 100 NQ-swap samples × Llama-3.1-8B will establish actual runtime and memory requirements before full-scale experiments. If CD-T proves impractical at 8B scale, HAGD (arXiv:2601.12879) offers O(n²log n) complexity as an alternative.\n\n**Phase 2 — Characterizing Override Geometry and Testing Compensatory Dynamics.**\nTwo sub-goals: (2a) Provide a unified geometric account of the flip phenomenon. Three independent observations suggest a coherent mechanism: CoRect's flip phenomenon (correct answer appears mid-layer then vanishes), Simulated Adoption's orthogonal interference (geometric rotation in conflict resolution), and Marín's rotational suppression (active rejection via rotation on hypersphere, arXiv:2603.13259). Testable unified hypothesis: deep FFN layers inject parametric direction vectors quasi-orthogonal to the context-aligned representation, implementing rotational suppression at the evidence-integration-to-override transition — the same geometric mechanism identified in simpler settings, but operating within RAG's multi-stage pipeline. Stage-wise ablation decomposes layer-wise residual stream updates at flip points into direction and magnitude components, testing whether ablating rotational vs. magnitude components selectively recovers the correct answer. The framework accommodates rotation-dominant, magnitude-dominant, or mixed outcomes.\n(2b) Test for compensatory dynamics: after Phase 1 identifies the circuit, selectively ablate individual pathway types (FFN override nodes only, retrieval heads only, copy suppression only) and measure whether remaining pathway types increase their override contribution to compensate. This directly tests the primary research question.\n\nFlip event operational definition (independent of CoRect's implementation): at layer L, the correct answer token's logit rank enters top-k; at layer L+Δ, it exits top-k. This captures the same phenomenon without dependency on CoRect's specific logit contrast methodology. Contingency: if flip events are not prevalent on certain models/architectures, Phase 3 intervention calibration falls back to Phase 1 circuit attribution scores alone (still principled, though without flip-specific geometry profiling).\n\n**Phase 3 — Geometry-Aware Coordinated 3-Point Intervention.** Inference-time intervention simultaneously addressing three override pathway components: (A) dampen parametric FFN re-promotion at identified override layers, (B) amplify retrieval head signals at evidence-integration positions, (C) inhibit copy suppression — informed by entropy neuron findings (Context Copying Modulation, EMNLP 2025 Findings, arXiv:2509.10663) — at output-proximal layers. Calibration is geometry-aware per Phase 2 profile: rotation-dominant → project out parametric direction; magnitude-dominant → scale activations; mixed → hybrid. All interventions implemented via single-pass forward hooks (no dual-run overhead).\n\n## Evaluation Design\n\n**Models:** Llama-3.1-8B, Qwen3-8B, Gemma-2-9B (3 architectures).\n\n**Datasets:** NQ-swap, ConFiQA, CoFaithfulQA, MemoTrap (entity substitution, multi-hop, faithfulness, memorization-trap conflict types).\n\n**Baselines:** JuICE (head-level SOTA), CoRect (FFN rectification), SpARE (SAE steering), ParamMute (FFN suppression), CoCoA (contrastive decoding SOTA, EMNLP 2025), IRCAN (neuron-level). Supplementary: Knowledgeable-R1 (ICLR 2026, RL-based), TCR (AAAI 2026, detection + soft-prompt). Additional critical baseline: **Naive Stack** (JuICE heads + ParamMute FFN suppression + entropy neuron ablation applied simultaneously without circuit guidance) — directly tests whether circuit-informed coordination adds value beyond independent method combination.\n\n**Metrics — Task Performance:** EM, token-level F1, memorization ratio (per ParamMute). **No-conflict control:** EM/F1 on standard (non-conflicting) RAG inputs + output perplexity, verifying intervention does not degrade normal generation quality. **Circuit Quality (Phase 1-2):** circuit faithfulness, completeness, sparsity (per CD-T/PEAP evaluation frameworks).\n\n**Ablation Matrix:**\n- Component isolation: (A) FFN dampening only, (B) retrieval head amplification only, (C) copy suppression inhibition only, (AB), (AC), (BC), (ABC = full CORe) — 7 configurations. Key test: does removing one component cause remaining components' effectiveness to degrade (evidence of compensatory dynamics)?\n- Intervention strategy: geometry-aware vs. magnitude-only calibration under same 3-point framework.\n- Sensitivity: 3-5 intervention strength values per component.\n- **Circuit transferability:** discover circuit on dataset A, apply intervention to datasets B/C/D without re-discovery — tests practical deployability.\n\n**Predictive Diagnostics Analysis:** For instances where baseline X fails but CORe succeeds, analyze which circuit pathways are active — demonstrating CORe's diagnostic capability beyond aggregate metric improvement.\n\n**Inference Efficiency:** (1) Per-sample cost: additional forward passes (CORe: 0, single-pass hooks; JuICE: 1 extra; CoRect: 1 extra; CoCoA: 1 extra), wall-clock time, peak GPU memory. (2) Amortized setup cost: GPU-hours for one-time circuit discovery per model (one-time; subsequent inference is hook-only).\n\n**Statistical Rigor:** Core comparisons (CORe vs. each primary baseline, full vs. ablated) report mean ± std over 3 runs with paired bootstrap significance tests.\n\n## Broader Significance\n\nBeyond RAG knowledge conflicts, the diagnose-then-intervene framework (position-aware circuit tracing → geometry characterization → coordinated multi-point repair) may generalize to other LLM internal conflict scenarios: instruction-following vs. safety guardrails, competing reasoning paths in multi-hop inference, cross-lingual knowledge interference. PhantomCircuit (EMNLP 2025, arXiv:2505.14406) has already demonstrated circuit-level analysis transfers across conflict types. We leave these extensions to future work.\n\n## Concurrent Work Check\n\nNo 2026 submission combines causal circuit tracing with multi-point RAG intervention. Closest: ParamMute (FFN-only, no circuit tracing), CLEAR (probing-based, requires fine-tuning, attention-only), ReDeEP (ICLR 2025, detection not repair), PhantomCircuit (training-data conflicts not RAG), Knowledgeable-R1 (ICLR 2026, RL-based not mechanistic), TCR (AAAI 2026, detection + soft-prompt, no mechanistic analysis).\n\n## Key References\n\n- Taming Knowledge Conflicts in Language Models [JuICE] (ICML 2025)\n- CoRect: Context-Aware Logit Contrast for Hidden State Rectification (arXiv 2026, arXiv:2602.08221)\n- Steering Knowledge Selection via SAE-Based Repr. Engineering [SpARE] (NAACL 2025)\n- Efficient Automated Circuit Discovery via Contextual Decomposition [CD-T] (ICLR 2025)\n- Position-aware Automatic Circuit Discovery [PEAP] (ACL 2025)\n- Simulated Adoption: Decoupling Magnitude and Direction in LLM Conflict Resolution (arXiv 2026, arXiv:2602.04918)\n- Resisting Contextual Interference in RAG [Knowledgeable-R1] (ICLR 2026)\n- Promote, Suppress, Iterate (EMNLP 2025)\n- ReDeEP: Detecting Hallucination in RAG via Mechanistic Interpretability (ICLR 2025)\n- ParamMute: Suppressing Knowledge-Critical FFNs for Faithful RAG (NeurIPS 2025, arXiv:2502.15543)\n- Competition of Mechanisms: Tracing How Language Models Handle Facts and Counterfactuals (ACL 2024) + On the Generalizability of Competition of Mechanisms (arXiv:2506.22977)\n- Context Copying Modulation: The Role of Entropy Neurons (EMNLP 2025 Findings, arXiv:2509.10663)\n- PhantomCircuit: Pierce the Mists of Knowledge Conflicts (EMNLP 2025, arXiv:2505.14406)\n- The Override Gap: Magnitude Account of Knowledge Conflict in Hypernetwork Adaptation (arXiv Apr 2026, arXiv:2604.23750)\n- Seeing through the Conflict (AAAI 2026)\n- How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing (arXiv Mar 2026, arXiv:2603.13259)\n- CLEAR: Probing Latent Knowledge Conflict for Faithful RAG (arXiv:2510.12460, Oct 2025)\n- CoCoA: Confidence- and Context-Aware Adaptive Decoding (EMNLP 2025)\n- IRCAN: Identifying and Reweighting Context-Aware Neurons (NeurIPS 2024)\n- HAGD: Hierarchical Attribution Graph Decomposition (arXiv:2601.12879)"
}
````

---

### Runtime record

_source line 2 · 2026-05-30T07:53:36.407Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:53:36.407Z",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-30T07:53:36.445Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct the evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [JuICE: Taming Knowledge Conflicts in Language Models](https://arxiv.org/abs/2503.10996) (ICML 2025 Spotlight): 最直接的上游工作。发现注意力头存在 superposition（同一 head 同时促进 memory 和 context），提出双次推理头级干预，在11个数据集上达 SOTA。但仅限头级别，无 FFN/copy suppression 分析——正是 CORe 扩展的方向。
- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221) (arXiv Feb 2026): 发现 flip 现象（正确答案在中层出现后被深层 FFN 抑制），用加性校正进行干预。FFN 级别，无电路级诊断。CORe Phase 2 的 flip 统一假设直接基于此。
- [ParamMute](https://arxiv.org/abs/2502.15543) (NeurIPS 2025): 定位中-深层 FFN 为不忠实生成的关键，提出 FFN 抑制框架。单组件干预，无因果电路分析。
- [SpARE: SAE-Based Representation Engineering](https://arxiv.org/abs/2410.15999) (NAACL 2025 Oral): 用预训练 SAE 特征在单层进行推理时干预，+10% EM。单层单点。
- [CD-T: Contextual Decomposition for Transformers](https://arxiv.org/abs/2407.00886) (ICLR 2025): 电路发现方法，运行时间从小时降至秒级，97% ROC AUC。CORe Phase 1 的核心工具之一。
- [PEAP: Position-aware Edge Attribution Patching](https://aclanthology.org/2025.acl-long.141/) (ACL 2025): 位置感知电路发现，比非位置方法边数少数个数量级。CORe Phase 1 的另一核心工具。
- [Competition of Mechanisms](https://arxiv.org/abs/2402.11655) (ACL 2024) + [Generalizability Study](https://arxiv.org/abs/2506.22977) (arXiv 2025): 事实回忆 vs. 上下文复制的竞争。关键发现：Llama 3.1 8B 中头的特化显著减弱→override 电路在大模型中更分布式，支持 CORe 的多点干预动机。
- [Simulated Adoption](https://arxiv.org/abs/2602.04918) (arXiv Feb 2026): 冲突解决通过正交干扰（几何旋转而非幅度抑制）。CORe Phase 2 几何统一的三个独立观察之一。
- [How Transformers Reject Wrong Answers](https://arxiv.org/abs/2603.13259) (arXiv Mar 2026): 旋转动力学，1.6B 参数相变。另一个独立几何观察。
- [Context Copying Modulation: Entropy Neurons](https://arxiv.org/abs/2509.10663) (EMNLP 2025 Findings): 熵神经元抑制上下文复制（<2‰ FFN 神经元但影响显著）。CORe 第三干预点（copy suppression inhibition）的机制基础。
- [CLEAR: Probing Latent Knowledge Conflict](https://arxiv.org/abs/2510.12460) (arXiv Oct 2025): 三阶段干预但基于 probing（非因果），需微调，仅调制注意力。CORe 的最直接多阶段竞争者。
- [CoCoA: Confidence- and Context-Aware Adaptive Decoding](https://aclanthology.org/2025.emnlp-main.1116/) (EMNLP 2025): 对比解码 SOTA，但在解码层操作，无内部机制理解。

- **调研总结**: RAG 知识冲突干预领域正处于从"单组件启发式干预"向"机制级理解"的范式转换期。JuICE/CoRect/ParamMute/SpARE 各自识别了不同组件的贡献但彼此独立；Competition of Mechanisms 的泛化研究表明大模型中 override 机制更分布式。CORe 的定位——用因果电路追踪统一这些分散发现并进行协同多点干预——填补了一个真实存在的空白，但核心假设（补偿动力学）尚无直接前序证据。

【整体印象】:
作为审稿人，第一反应是：这是一份学术素养极高、问题定义精准、实验设计专业的 proposal。作者对领域文献的掌握深度超过了大多数投稿——不仅知道每个方法做了什么，还能精确定位它们的局限性并解释为什么这些局限性会导致性能瓶颈。补偿动力学假设具有理论吸引力，且在神经科学（neural circuit compensation）中有丰富类比。我会倾向于给 weak accept，但有保留意见：scope 过大（本质上是三篇论文合一）、核心假设尚属推测、以及 CD-T+PEAP 在 8B 规模 RAG 长上下文中的可扩展性存在不确定性。

【核心贡献】:
三层核心贡献：
1. **方法论贡献**：首次将因果电路追踪（CD-T + PEAP）应用于 RAG override 机制，产出位置感知的 override 电路图——这本身就是对领域理解的实质推进。
2. **理论贡献**：补偿动力学假设和 flip 现象的几何统一——如果成立，这将为单点干预瓶颈提供首个因果解释。
3. **工程贡献**：几何感知协同三点推理时干预（FFN + 注意力 + copy suppression），无需训练，单次前向传播。

这些贡献对领域的价值显著——从"哪个组件重要"的零散认知推进到"组件如何协同构成 override 电路"的系统理解。但价值高度依赖于补偿动力学假设是否成立。

【方法合理性】:
方法整体合理但复杂度高。具体评估：

**合理之处：**
- CD-T（粗筛）→ PEAP（精细位置感知边归因）的两阶段管线利用了两者的互补优势，有理论支撑。
- 三点干预覆盖了文献中已识别的三类关键组件（FFN override layers/retrieval heads/entropy neurons），逻辑完整。
- 几何感知校准（旋转主导→投影；幅度主导→缩放；混合→混合）基于三个独立的几何发现，有证据支持。
- 纳入 Naive Stack baseline 是关键设计，直接检验"电路指导的协同是否优于朴素组合"。

**潜在替代方案的威胁：**
- 是否可以仅用 PEAP 做电路发现而跳过 CD-T？PEAP 本身已经能产出位置感知电路，CD-T 的粗筛步骤是否真正必要需要验证。
- CoRect 的 logit contrast 方法本质上已经在做"定位哪些层抑制了正确答案"，CORe 的因果电路追踪是否能提供显著超越 CoRect 的定位精度？
- 几何感知校准增加了显著复杂度——如果一个简单的固定强度三点干预就能超过单点方法，那几何感知部分的边际贡献可能不大。

**方法风险：**
- CD-T 在原论文中主要在小规模模型/任务上验证，8B 模型 + RAG 长上下文是显著的规模跳跃。
- 三组件 × 多强度参数的校准空间很大，存在过拟合到特定数据集的风险。

【5 维度打分】:

1. **研究问题: 强** — 问题定义精准且有实际价值。"为什么单点干预总是 plateau"是该领域的核心困惑，补偿动力学假设提供了一个可证伪的解释。Competition of Mechanisms 的泛化研究（arXiv:2506.22977）证实大模型中 override 机制更分布式，进一步支持了多点协同干预的必要性。无论假设成立与否，结果都有信息量（proposal 正确指出了这一点）。

2. **方法与创新: 中偏强** — 组合 CD-T + PEAP 进行 RAG 电路发现是新颖的应用创新，三点协同干预在该领域确实首创。但各组件（CD-T、PEAP、entropy neuron ablation）均为已有工具的组合应用而非方法论发明。与 CLEAR（arXiv:2510.12460）相比，CORe 在因果性（causal vs. probing）和组件覆盖度（三组件 vs. 仅注意力）上有清晰优势，但 CLEAR 的端到端可操作性可能更好。几何统一假设（连接 Simulated Adoption + Marín 2026 + Promote-Suppress-Iterate）是最具原创性的理论贡献，但也是最投机的。

3. **实验设计: 强** — 这是 proposal 最突出的维度。3 架构 × 4 数据集 × 7+ baseline（含 Naive Stack 这一关键对照）× 7 ablation 配置 × 跨数据集迁移性测试 × 无冲突对照 × 统计显著性检验——实验矩阵的完备度超过了大多数同领域已发表论文。特别值得肯定：(a) Naive Stack baseline 直接检验核心 claim；(b) 电路迁移性测试关乎实用性；(c) 推理效率对比考虑了摊销成本。相比 JuICE（ICML 2025）和 ParamMute（NeurIPS 2025）的实验设计，CORe 的实验方案更全面。唯一缺失：没有提及 human evaluation 或 case study 分析（虽然对 QA 任务非必需但可加分）。

4. **可行性: 中** — 这是主要短板之一。(a) **Scope 过大**：三个阶段（电路发现 → 几何特征化 + 补偿动力学测试 → 协同干预）中每一个都足以独立成文，在一篇论文中完成全部且都做到 solid 的概率不高。(b) **CD-T 规模化风险**：尽管 proposal 提到了 pilot study 和 HAGD 回退方案，但 8B 模型 + 长 RAG 上下文的电路发现在实践中可能遇到未预见的困难。(c) **校准复杂度**：3 组件 × 3-5 强度 × 3 几何模式 = 大量超参数组合，需要精心调优。(d) **积极面**：回退方案设计周全（CD-T 失败→HAGD；flip 不普遍→仅用 Phase 1 归因分数；分数融合退化→纯管线），表明作者对风险有清醒认识。

5. **写作与呈现: 强** — Proposal 的逻辑结构清晰，从问题（单点干预 plateau）→ 假设（补偿动力学）→ 方法（三阶段管线）→ 评估的叙事链条完整有力。对每个相关工作的定位精准且公允（不贬低前人工作，而是准确指出局限）。Gap statement 有说服力。技术描述具体到可复现程度（如 flip 事件的操作性定义、CD-T 候选分数的归一化方式）。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
**上推因素（→42%）：** 研究问题精准、实验设计极其完备（特别是 Naive Stack baseline 和 ablation 矩阵）、文献综述深度罕见、写作质量高、填补的空白真实存在。如果补偿动力学假设成立且电路发现方法在 8B 模型上可行，这篇论文的贡献将非常显著。

**下拉因素（→28%）：** (1) Scope 是最大风险——三个阶段的工作量和不确定性叠加，审稿人可能认为"做了很多但每个部分都不够深入"；(2) 核心假设（补偿动力学）完全推测性，无前序 LLM 实验证据（仅有神经科学类比），一旦不成立，叙事的说服力显著下降（虽然 Phase 1 电路发现和 Phase 3 干预仍有独立价值）；(3) CD-T+PEAP 在 8B 规模 RAG 任务上的验证真空——pilot study 可能发现不可逾越的障碍；(4) 方法本质是已有工具（CD-T、PEAP、entropy neuron ablation、JuICE 式头干预、ParamMute 式 FFN 抑制）的系统整合，审稿人可能质疑"方法论新颖性在哪里"。

**中位 35% 的定位依据：** 这份 proposal 在问题定义和实验设计上属于领域上游水平，显著优于平均投稿。但 scope 过大 + 核心假设投机性 + 方法为组合创新而非原创方法 三者叠加，使其处于 borderline accept 的区间。在 AAAI 的审稿流程中，这类 proposal 的命运高度依赖于审稿人分配——遇到重视 mechanistic interpretability 和实验设计的审稿人可能获得 accept，遇到看重方法论原创性的审稿人则可能被拒。

【主要风险】:
1. **Scope 过载导致审稿人质疑深度**：三阶段管线中任一阶段的实验如果做得不够深入（例如 Phase 2 几何统一仅是初步观察而非严格验证），整体论文会被视为"广而不深"。审稿人可能建议"拆成两篇论文"——这在顶会中是常见的 reject 理由。
2. **补偿动力学假设不成立或效应很弱**：如果单路径 ablation 后其他路径的补偿效应在统计上不显著，核心叙事（"协同干预之所以有效是因为需要同时阻断补偿通路"）将缺乏支撑。此时 CORe 退化为"用更好的方法选择干预目标"，其相对于 JuICE/CoRect 的优势将大幅缩小。

【实施评估】:
  - **计算资源**: 高。需对 3 个 8B 模型分别运行 CD-T + PEAP 电路发现（CD-T 声称高效但未在 8B+长上下文验证），加上 7 ablation × 4 数据集 × 3 模型 × 3 运行的评估矩阵。估计需 4-8 块 A100 80G，总 GPU 时数约 200-500 小时。
  - **数据需求**: 中低。使用已有公开数据集（NQ-swap、ConFiQA、CoFaithfulQA、MemoTrap），无需构建新数据。
  - **人工介入**: 中。电路图的解读和验证、干预强度的初始校准、flip 事件的质量检查可能需要研究者手动参与。
  - **训练需求**: 无模型训练。纯推理时干预 + 一次性电路发现。
  - **新 Benchmark**: 不需要。
  - **预估周期**: 3-5 个月。Phase 1（电路发现 + pilot study）~6-8 周；Phase 2（几何特征化 + 补偿动力学测试）~4-6 周；Phase 3（干预实现 + 全矩阵评估）~4-6 周；写作 ~3-4 周。如果 CD-T 遇到规模化问题需要切换到 HAGD，额外 2-3 周。
```

Sources:
- [JuICE: Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)
- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification (arXiv 2026)](https://arxiv.org/abs/2602.08221)
- [ParamMute: Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://arxiv.org/abs/2502.15543)
- [SpARE: SAE-Based Representation Engineering (NAACL 2025)](https://arxiv.org/abs/2410.15999)
- [CD-T: Efficient Automated Circuit Discovery (ICLR 2025)](https://arxiv.org/abs/2407.00886)
- [PEAP: Position-aware Automatic Circuit Discovery (ACL 2025)](https://aclanthology.org/2025.acl-long.141/)
- [Competition of Mechanisms (ACL 2024)](https://arxiv.org/abs/2402.11655)
- [On the Generalizability of Competition of Mechanisms (arXiv 2025)](https://arxiv.org/abs/2506.22977)
- [Simulated Adoption (arXiv 2026)](https://arxiv.org/abs/2602.04918)
- [How Transformers Reject Wrong Answers (arXiv 2026)](https://arxiv.org/abs/2603.13259)
- [Context Copying Modulation: Entropy Neurons (EMNLP 2025)](https://arxiv.org/abs/2509.10663)
- [CLEAR: Probing Latent Knowledge Conflict (arXiv 2025)](https://arxiv.org/abs/2510.12460)
- [JuICE GitHub Repository](https://github.com/GaotangLi/JUICE)
- [ParamMute GitHub Repository](https://github.com/OpenBMB/ParamMute)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:
- [JuICE / Taming Knowledge Conflicts in Language Models](https://arxiv.org/abs/2503.10996) (ICML 2025 Spotlight): 发现注意力头的"superposition"现象（同一头同时促进记忆和上下文），提出dual-run头级干预，11数据集SOTA。CORe的最直接基线之一，CORe需在此基础上证明多组件协调干预的增量价值。
- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221) (arXiv Feb 2026): 记录了flip phenomenon（正确答案在中间层出现后被深层FFN抑制），提出对比logit方法做hidden state矫正。CORe Phase 2a的geometric unification直接建立在此发现之上，但CORe声称提供因果解释而非相关性检测。
- [SpARE / SAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.264/) (NAACL 2025 Oral): 用SAE特征做steering，+10% EM，但目标选择基于单层互信息排名。CORe声称通过因果归因提供更principled的目标选择。
- [ParamMute: Suppressing Knowledge-Critical FFNs](https://arxiv.org/abs/2502.15543) (NeurIPS 2025): 识别中深层FFN（70%-90%相对深度）为不忠实生成的关键，通过抑制这些FFN提升忠实度。单组件类型干预，CORe的直接对比对象。
- [Simulated Adoption: Decoupling Magnitude and Direction](https://arxiv.org/abs/2602.04918) (arXiv Feb 2026): 发现冲突解决通过正交干扰（几何旋转而非幅度抑制）实现，跨Llama-3.1-8B/Qwen-3-4B/GLM-4-9B验证。CORe Phase 2a的geometric unification的关键输入之一。
- [Context Copying Modulation / Entropy Neurons](https://aclanthology.org/2025.findings-emnlp.1116/) (EMNLP 2025 Findings): 发现entropy neurons（<0.2% FFN神经元）在最后transformer层抑制上下文复制。CORe第三干预点（copy suppression inhibition）的机制基础。
- [CLEAR: Probing Latent Knowledge Conflict](https://arxiv.org/abs/2510.12460) (arXiv Oct 2025): 三阶段干预（知识分解→探针定位→注意力调制），但基于probing相关性（非因果）、需微调、仅调制注意力。CORe区分自身的重要对比点。
- [CD-T / Efficient Automated Circuit Discovery](https://arxiv.org/pdf/2407.00886) (ICLR 2025): 基于Contextual Decomposition的电路发现方法，声称transformer-agnostic可扩展性。CORe Phase 1的核心工具之一。
- [Competition of Mechanisms](https://arxiv.org/abs/2506.22977) (ACL 2024 + arXiv 2025 generalization study): 追踪factual recall vs. in-context copying的竞争，发现Llama 3.1 8B中头专门化减弱，暗示override circuits在大模型中更分布式。直接支持CORe的分布式电路假说。

- **调研总结**: RAG知识冲突领域正处于从"单组件启发式干预"向"机制理解驱动的系统干预"转型的节点。JuICE、SpARE、ParamMute等单组件方法各自取得了显著进展但都有天花板。几何理解（旋转vs.幅度）正在独立涌现但尚未统一。CORe的定位——因果电路追踪+几何统一+多点协调干预——准确地占据了一个尚无人填充的空白，时机恰好。

【整体印象】:
作为审稿人，我的第一反应是"这是一份精心构建的、野心很大的proposal"。研究问题切中要害——为什么单点干预会plateau？——这是领域内practitioners普遍感受到但尚无人系统性回答的问题。compensatory dynamics假说优雅且可测试，"无论结果如何都有价值"的双向设计体现了科学诚实性。文献综述异常全面，清晰地建立了gap。

倾向：**Weak Accept**。问题好、方法有理、实验设计扎实，但scope过于宏大是最大隐患——在一篇论文中同时做电路发现、几何统一、三点干预，任何一个phase出问题都可能导致整体叙事断裂。如果执行良好、结果positive，这是一篇strong paper；但执行风险不容忽视。

【核心贡献】:
1. **Compensatory dynamics假说及其实证验证**: 首次提出并检验RAG override circuit中的补偿动力学，为单点干预plateau提供因果解释。这是最核心的科学贡献。
2. **位置感知因果电路追踪应用于RAG**: 将CD-T/PEAP pipeline应用于RAG context-parametric冲突场景，产出可解释的circuit graph。
3. **几何统一**: 将flip phenomenon、旋转抑制、多阶段promote-suppress动力学统一为一个框架（如果成功）。
4. **Geometry-aware coordinated 3-point intervention**: 基于电路和几何诊断的多点推理时干预，配合naive stack baseline直接检验协调的价值。

核心贡献对领域的价值：**中到高**。如果compensatory dynamics被验证，这改变了领域对"为什么干预失败"的理解，具有paradigm-shifting潜力。即使只是部分验证，位置感知电路追踪和predictive diagnostics也有独立价值。

【方法合理性】:
方法整体合理，逻辑链条清晰（电路发现→几何刻画→干预设计）。几个关键点：

1. **CD-T + PEAP pipeline**: 这两个工具各自在ICLR 2025和ACL 2025发表，有独立验证。但它们从未在RAG场景下组合使用，组合后的效果未知。CD-T在8B模型上的可扩展性是实际风险，pilot study的设计是明智的，HAGD fallback也合理。
2. **Compensatory dynamics测试**: 方法设计合理——ablate一种pathway，测量其他pathway的override贡献是否增加。这是标准的因果检验范式。
3. **Geometry-aware calibration**: rotation-dominant → project out; magnitude-dominant → scale; mixed → hybrid。逻辑清晰，但per-instance的几何类型判断可能引入额外复杂性和噪声。
4. **更简单的替代方案？** Naive stack baseline直接回答了这个问题。如果naive stack已经很好，那么circuit-guided coordination的额外价值会被质疑。但这也正是proposal设计的优点——它主动设置了这个检验。

主要方法论风险：Phase 2a的geometric unification涉及三个独立发现（CoRect的flip、Simulated Adoption的旋转、Marín的球面旋转），它们可能不收敛为一个统一机制，特别是在不同架构上。

【5 维度打分】:
  1. 研究问题: **强** — "为什么单点干预plateau"是领域内公认的开放问题，JuICE/SpARE/ParamMute/CoRect各自SOTA但各有天花板，compensatory dynamics假说提供了一个可测试的因果解释。双向假设设计（存在/不存在compensatory dynamics都有科学价值）进一步增强了研究问题的robustness。研究问题同时服务于理解（为什么）和工程（怎么办），兼具科学价值和应用价值。
  
  2. 方法与创新: **中偏强** — CD-T（ICLR 2025）+ PEAP（ACL 2025）的组合在RAG场景的应用是新颖的，geometry-aware calibration有创新性。但核心工具都是已有方法的组合应用，创新更多在"组合方式"而非"基础方法"层面。与JuICE（发现superposition现象）、SpARE（SAE特征应用于steering）、ParamMute（识别关键FFN层）相比，CORe的方法创新更偏"系统集成"。审稿人可能会质疑：这是一个新方法还是已有方法的pipeline？需要通过compensatory dynamics的实证发现来证明组合不是简单拼接。
  
  3. 实验设计: **强** — 这是proposal最亮的部分之一。7配置ablation matrix直接检验核心假设；naive stack baseline是关键设计，主动回答"为什么不简单叠加"；3模型×4数据集覆盖全面；no-conflict control防止过度干预；circuit transferability测试实用价值高；inference efficiency对比（单pass hooks vs. 双run方法）体现工程关注。统计严格性（3 runs + paired bootstrap）也到位。缺一个adversarial analysis——如果模型在circuit discovery时看到的冲突模式与test时不同怎么办？
  
  4. 可行性: **中** — 这是最大的风险维度。三个phase中每个都有不小的执行风险：(1) CD-T在8B模型上的runtime/memory未知，pilot study是必要但结果可能不乐观；(2) geometric unification可能在不同架构上表现不一致；(3) 三点干预的参数空间（3-5强度值×3组件×7配置×3模型×4数据集）实验量巨大。proposal的contingency planning（HAGD fallback、flip不普遍时的退化方案）体现了成熟思考，但整体scope对于一个conference paper来说偏大。成功执行可能需要2-3个月的密集实验期。
  
  5. 写作与呈现: **强** — Proposal的文献综述异常全面，每篇相关工作都有精确的定位和差异化分析。Gap identification清晰有力。研究问题的framing（compensatory dynamics）具有很强的narrative coherence。Contingency planning的透明性增强了可信度。术语使用准确。唯一不足：方法描述部分信息密度很高，实际论文需要更多空间展开。

【概率估计】: [30% - 42%] 中位 35%

【估计理由】:
**上行因素** (推向42%+):
- 研究问题精准切中领域痛点，novelty claim在调研后确认成立——截至2026年5月无已发表工作组合因果电路追踪+多点RAG干预
- 实验设计非常完备，naive stack baseline的设置是审稿人最想看到的关键对照
- 文献综述的深度和精确度超出大多数submissions，体现了对领域的深刻理解
- compensatory dynamics如果被验证，贡献级别可达Best Paper候选

**下行因素** (推向30%以下):
- Scope过大：三个phase中任何一个出问题（CD-T不可扩展、geometric unification不收敛、compensatory dynamics不存在），整个narrative就要重构
- 方法创新更偏"系统集成"，审稿人可能认为这是engineering contribution而非scientific contribution
- 如果compensatory dynamics不存在（这完全可能），paper虽仍有价值但narrative力度大幅下降
- 如果naive stack已经工作得很好，circuit-guided coordination的额外价值可能不够显著

**中位判断** (35%):
这是一篇"高风险高回报"的投稿。研究问题好、设计扎实、gap真实存在。如果结果positive（compensatory dynamics存在 + 协调干预显著优于naive stack + 几何统一成功），这是40%+的strong accept候选。但如果任一核心假设不成立或execution不到位，可能落入"ambitious but inconclusive"的reject区间。35%的中位反映了：好的问题+好的设计 vs. 高执行风险+过大scope的权衡。

【主要风险】:
1. **Scope过大导致执行不完整**: 三个phase的完整执行（3模型×4数据集×7 ablation配置 + 几何分析 + 电路发现）工作量极大，deadline压力下很可能某些phase不够深入，导致审稿人认为"每个方面都浅尝辄止"。如果只能完整做好一部分，建议优先Phase 1 + compensatory dynamics test + 3-point intervention，geometric unification可作为supporting analysis而非主要贡献。
2. **核心假设（compensatory dynamics）可能不成立**: 如果ablate一种pathway后其他pathway的override贡献并不增加，那么"为什么单点干预plateau"的问题回到原点。paper的"value regardless of outcome"framing能部分缓解，但审稿人可能认为negative result的价值不足以支撑一个AAAI oral/poster。

【实施评估】:
  - 计算资源: **高**。CD-T在8B模型上的decomposition + PEAP的forward/backward pass + 3模型×4数据集×7 ablation配置的完整实验矩阵。估计需要4-8× A100 80GB持续运行。Pilot study至关重要，可能需要1-2周GPU时间仅用于可行性验证。
  - 数据需求: **中低**。NQ-swap、ConFiQA、MemoTrap、CoFaithfulQA均为已有公开数据集，无需构建新数据集。但可能需要自建部分conflict prompts用于circuit discovery phase的精细控制。
  - 人工介入: **低至中**。电路图的解读和geometric analysis需要专家判断，但整体pipeline高度自动化。Intervention strength calibration可能需要一定手动调参。
  - 训练需求: **无**。全部干预在推理时通过forward hooks实现，不需要模型训练或微调。这是CORe相对CLEAR的重要优势。
  - 新 Benchmark: **无需**。使用已有benchmark组合。CoFaithfulQA（ParamMute引入）已可用。
  - 预估周期: **3-4个月**（含pilot study 2-3周 + Phase 1电路发现 3-4周 + Phase 2几何分析和compensatory dynamics测试 3-4周 + Phase 3干预实现和完整实验 4-5周 + 论文写作 3-4周）。如果精简scope（例如减少模型数量或简化geometric unification），可压缩至2.5-3个月。
```

---

Sources:
- [Taming Knowledge Conflicts in Language Models (JuICE) - ICML 2025](https://arxiv.org/abs/2503.10996)
- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221)
- [SpARE: Steering Knowledge Selection via SAE-Based Representation Engineering - NAACL 2025](https://aclanthology.org/2025.naacl-long.264/)
- [ParamMute: Suppressing Knowledge-Critical FFNs for Faithful RAG - NeurIPS 2025](https://arxiv.org/abs/2502.15543)
- [Simulated Adoption: Decoupling Magnitude and Direction in LLM Conflict Resolution](https://arxiv.org/abs/2602.04918)
- [Context Copying Modulation: The Role of Entropy Neurons - EMNLP 2025 Findings](https://aclanthology.org/2025.findings-emnlp.1116/)
- [CLEAR: Probing Latent Knowledge Conflict for Faithful RAG](https://arxiv.org/abs/2510.12460)
- [CD-T: Efficient Automated Circuit Discovery via Contextual Decomposition](https://arxiv.org/pdf/2407.00886)
- [JuICE GitHub Repository](https://github.com/GaotangLi/JUICE)
- [ParamMute GitHub Repository](https://github.com/OpenBMB/ParamMute)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [JuICE: Taming Knowledge Conflicts in Language Models](https://arxiv.org/abs/2503.10996) (ICML 2025 Spotlight): 发现注意力头的 superposition 现象（同一头同时促进 memory 和 context），提出 dual-run 头级干预，11 个数据集上取得 SOTA。是本 proposal 最直接的 baseline 和动机来源——JuICE 仅做头级干预，未涉及 FFN 或 copy suppression。
- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification](https://arxiv.org/abs/2602.08221) (arXiv Feb 2026): 发现 flip 现象（正确答案在中间层出现后被深层 FFN 抑制），通过 logit 对比进行 additive rectification。仅干预 FFN 层，无电路级诊断。CORe 的 Phase 2 直接试图解释 flip 的几何机制。
- [ParamMute: Suppressing Knowledge-Critical FFNs](https://arxiv.org/abs/2502.15543) (NeurIPS 2025): 识别 70%-90% 相对深度的 FFN 层为不忠实生成的关键层，通过抑制实现 faithfulness 提升。单组件干预，统计识别。CORe 的 FFN 干预点与之重叠但采用因果归因而非统计方法。
- [SpARE: SAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.264/) (NAACL 2025 Oral): 利用 SAE 特征进行 steering，仅选择单一中间层点的 0.05% SAE 激活，+10% EM。单点、单层干预。
- [PEAP: Position-aware Automatic Circuit Discovery](https://aclanthology.org/2025.acl-long.141/) (ACL 2025): 引入 dataset schema 实现位置感知电路发现，比位置无关电路更小更精确。CORe Phase 1 的核心工具之一。
- [CD-T: Efficient Automated Circuit Discovery via Contextual Decomposition](https://arxiv.org/abs/2407.00886) (ICLR 2025): 基于数学分解（非 activation patching）的电路发现，声称 transformer-agnostic 可扩展性。CORe Phase 1 的另一核心工具。
- [Simulated Adoption](https://arxiv.org/abs/2602.04918) (arXiv Feb 2026): 发现知识冲突解决中的正交干扰机制——模型通过几何旋转而非幅度抑制来绕过正确答案。CORe Phase 2 试图将此发现与 CoRect flip 和 Marín 的旋转动力学统一。
- [Context Copying Modulation](https://aclanthology.org/2025.findings-emnlp.1116/) (EMNLP 2025 Findings): 发现 entropy neurons（不到 0.2% 的 FFN 神经元）在最后 transformer 层中显著抑制 context copying。CORe 的第三干预点（copy suppression 抑制）直接基于此发现。
- [Competition of Mechanisms](https://arxiv.org/abs/2305.14251) (ACL 2024) + [泛化研究](https://arxiv.org/abs/2506.22977): 追踪 factual recall vs. in-context copying 竞争，但泛化研究发现头部特化在大模型中显著减弱，暗示 override 电路更加分布式。
- [MAT-STEER: Multi-Attribute Targeted Steering](https://arxiv.org/abs/2502.12446) (2025): 解决多属性 ITI 中的冲突问题，但针对属性控制而非知识冲突，且未采用电路级分析。
- [CLEAR](https://arxiv.org/abs/2510.12460) (arXiv Oct 2025): 三阶段干预（pruning→probing→modulation），最接近 CORe 的多阶段范式，但使用 probing 相关性（非因果）、需要 fine-tuning、仅调制 attention。CORe 在因果性、推理时干预、多组件覆盖三方面有明确差异化。

- 调研总结: RAG 知识冲突是 2024-2026 年的高热度研究方向，已有大量单组件干预方法（JuICE/CoRect/SpARE/ParamMute/IRCAN）和几何机制分析（Simulated Adoption/旋转动力学）。然而，现有工作普遍局限于单一组件类型的干预，且未建立因果电路级理解来解释为何单点干预遇到瓶颈。CORe 占据了一个真实且清晰的研究空位：因果电路追踪 + 几何统一 + 协调多点干预。这个空位既不是臆造的，也尚未被已有工作填补。

【整体印象】:
作为审稿人，第一反应是 "这是一个准备充分、问题意识清晰、实验设计严谨的 proposal"。作者对领域现状的理解深度令人印象深刻——从 JuICE 的 superposition 到 CoRect 的 flip 现象，从 Simulated Adoption 的正交干扰到 entropy neurons 的 copy suppression，每一个相关发现都被精准地编织进叙事链。核心假设（补偿动力学导致单点干预瓶颈）具有可证伪性，且无论结果如何都有科学价值。

然而，这个 proposal 的野心也是其最大风险。三个 Phase 实质上是三篇独立论文的工作量压缩进一篇：(1) RAG override 电路的因果发现，(2) 几何机制的统一解释，(3) 协调多点干预方法。如果执行到位，这将是一篇非常有影响力的论文；但如果任何一个 Phase 的结果不如预期，整个叙事链可能断裂。

倾向：**Borderline accept / weak accept**。问题重要、方法有依据、实验设计出色，但执行风险高且可能被批评为"组合现有工具的工程工作"。

【核心贡献】:
1. **首个 RAG override 电路的因果图谱**（Phase 1）：将 CD-T 和 PEAP 这两个通用电路发现工具应用于 RAG 知识冲突场景，产出位置感知的因果电路归因——这本身就是一个有价值的 artifact，即使后续干预效果平平。
2. **补偿动力学的实证验证**（Phase 2b）：直接测试"单点干预失败是否因为其他路径补偿"这一假设，为理解现有方法瓶颈提供因果解释。
3. **几何统一框架**（Phase 2a）：将 flip 现象、正交干扰、旋转抑制三个独立发现统一到 RAG override 的几何解释中。
4. **协调 3 点推理时干预**（Phase 3）：基于电路级理解的 FFN + attention head + copy suppression 同时干预，配以几何感知的校准策略。

核心贡献对领域的价值：**高**。如果补偿动力学假设成立，这将改变该领域对干预方法设计的思维范式——从"找到最重要的单一组件"转向"理解分布式电路并协调干预"。即使假设不成立，因果电路图谱和几何分析本身也是有价值的科学发现。

【方法合理性】:
方法整体上是合理的，但存在若干需要审慎评估的点：

**合理之处：**
- CD-T → PEAP 的 pipeline 设计有据可循：CD-T 做粗筛（数学分解，计算高效），PEAP 做精细化（位置感知边归因）。两者互补而非冗余。
- 几何感知校准（rotation-dominant → project out; magnitude-dominant → scale）在 Simulated Adoption 和 Marín 2026 的发现基础上逻辑自洽。
- 单 pass forward hooks 实现干预，避免了 JuICE 的 dual-run 开销，实际部署更友好。
- Naive Stack baseline 的设置是方法论上的亮点——直接检验 "电路指导是否优于朴素组合"。

**需要质疑之处：**
- CD-T 和 PEAP 都未在 RAG 知识冲突场景下验证过，它们最初是为更简单的任务设计的（如间接对象识别、主谓一致）。RAG 的三方交互（query → evidence → parametric override）是否超出这些工具的有效范围是未知的。
- **更简单的替代方案**：审稿人可能会问——是否可以直接用 activation patching / causal tracing（à la Meng et al. 2022）配合 RAG 特定 prompt 来发现电路，而不需要 CD-T + PEAP 的复杂 pipeline？proposal 未充分论证为何更简单的因果追踪方法不够用。
- Phase 2a 的几何统一是否真的需要？一个审稿人可能认为，Phase 1 的电路发现 + Phase 3 的协调干预已经足够构成一篇完整的贡献，Phase 2a 的几何统一增加了复杂度但可能不是必需的。
- 三个干预点的"协调"具体如何实现？proposal 提到 "geometry-aware calibration"，但具体的优化目标函数或校准算法未明确描述——这留下了方法细节的空白。

【5 维度打分】:

1. 研究问题: **强** — "为什么单点干预会遇到瓶颈"是该领域一个真实且重要的问题。JuICE (ICML 2025 Spotlight)、CoRect、SpARE、ParamMute 各自独立取得了显著进展，但都局限于单一组件类型，且性能提升似乎开始饱和。提出"补偿动力学"假设为这一瓶颈提供了可证伪的因果解释，且 Competition of Mechanisms 泛化研究（arXiv:2506.22977）发现头部特化在大模型中减弱——间接支持了 override 电路更分布式的假设。问题定义清晰、有足够的前置证据支撑、且有明确的科学价值。

2. 方法与创新: **中偏强** — 方法的创新性主要体现在：(a) 将 CD-T（ICLR 2025）和 PEAP（ACL 2025）组合应用于 RAG 知识冲突的电路发现——这是新的应用场景，但工具本身不是新的；(b) 协调 3 点干预的思路是新颖的——现有方法（JuICE 头级、ParamMute FFN级、entropy neuron 级）各自独立，无人尝试过基于电路理解的协调干预；(c) 几何统一框架连接了 Simulated Adoption、CoRect flip、Marín 旋转动力学三个独立发现。然而，核心方法论贡献更多是"正确地组合现有工具"而非"发明新工具"，这可能被部分审稿人视为工程组合而非方法论创新。与 CLEAR（arXiv:2510.12460）相比，CORe 在因果性和组件覆盖面上有明确优势，但 CLEAR 至少有（probing-based 的）实证结果。

3. 实验设计: **强** — 这是 proposal 最出色的方面。(a) 3 个不同架构（Llama/Qwen/Gemma）确保跨模型泛化性；(b) 4 个覆盖不同冲突类型的数据集（entity substitution/multi-hop/faithfulness/memorization-trap）；(c) 7 个 baseline 包含各主要方法流派（头级 JuICE、FFN 级 CoRect/ParamMute、SAE 级 SpARE、解码级 CoCoA、神经元级 IRCAN），且关键地包含了 Naive Stack baseline——这直接测试核心 claim；(d) 7 配置的 ablation matrix（A/B/C/AB/AC/BC/ABC）完整覆盖所有组合；(e) no-conflict control 确保干预不损害正常生成；(f) circuit transferability 测试实际部署可行性；(g) predictive diagnostics 增加可解释性价值；(h) 统计严谨性（3 runs + paired bootstrap）。唯一缺失：未提及更大规模模型（70B+）的可扩展性评估，但对于 proposal 阶段这是合理的。

4. 可行性: **中** — 存在显著的执行风险。(a) CD-T + PEAP pipeline 在 8B 模型上的计算可行性是真实的不确定性——proposal 承认了这一点并提出了 pilot study 和 HAGD fallback，这是负责任的；(b) 三个 Phase 的顺序依赖意味着 Phase 1 的延迟或失败会级联影响后续所有工作；(c) 3 模型 × 4 数据集 × 7+ baseline × 7 ablation 配置 = 大量实验，保守估计需要数百 GPU 小时；(d) Phase 2a 的几何统一可能需要大量的分析和可视化工作，难以预估时间；(e) 如果补偿动力学不存在，叙事需要显著调整。总体上，一个 3-4 人团队在 3-4 个月内完成是可能的，但紧张。

5. 写作与呈现: **强** — Proposal 本身的写作质量极高。(a) 问题-现有方法局限-假设-方法-实验的逻辑链清晰完整；(b) 相关工作覆盖全面且时效性极强（引用到 2026 年 4 月的 arXiv 预印本）；(c) 与每一个相关工作的差异化都有明确阐述（特别是与 CLEAR 的三点差异）；(d) 每个 Phase 都有 contingency plan（HAGD fallback、flip 不普遍时的降级策略），显示成熟的研究规划；(e) "value regardless of outcome" 的框架是科学上诚实的。唯一的担忧是：将三个 Phase 的内容压缩进一篇 8 页论文可能导致方法细节不足。

【概率估计】: [25% - 40%] 中位 33%

【估计理由】:
**上调因素（→40%）：** (1) 问题高度时效且重要——RAG 知识冲突是 2025-2026 年的热门方向，AAAI 审稿人大概率对此感兴趣；(2) 占据了一个真实且清晰的研究空位——没有现有工作结合因果电路追踪与多点协调干预；(3) 实验设计极其扎实——naive stack baseline、完整 ablation、跨模型/跨数据集评估、statistical rigor，几乎没有可攻击的实验设计漏洞；(4) 写作/叙事质量高，审稿人阅读体验好；(5) 有 fallback 方案应对各种不确定性。

**下调因素（→25%）：** (1) **方法论创新的"组合"质疑**——核心工具（CD-T、PEAP、entropy neuron ablation、attention intervention）全部来自已有工作，CORe 的创新是"正确地组合"它们，部分审稿人可能认为这是 engineering contribution 而非 scientific contribution；(2) **执行风险极高**——三个顺序依赖的 Phase，任何一个结果不如预期都可能导致叙事断裂；(3) **补偿动力学假设可能不成立**——虽然 proposal 声称"value regardless of outcome"，但实际上如果核心假设被否定，论文的影响力和故事完整性会大打折扣；(4) **范围过广**——电路发现 + 几何统一 + 协调干预，对于一篇 8 页论文来说内容过于密集，可能导致每个部分都浅尝辄止；(5) **AAAI 2026 审稿周期压力**——proposal 引用了多篇 2026 年初的预印本，说明领域发展极快，在 proposal → 提交的窗口期内可能出现直接竞争的工作。

**中位 33% 的依据：** 这是一个"方向正确、设计精良但执行风险高"的 proposal。在 AAAI 的双盲审稿中，它很可能收到 1-2 个正面评价（赞赏问题定义和实验设计）和 1 个负面评价（质疑方法创新性或范围过广），最终处于 borderline 区域。AC 的决定将取决于 rebuttal 中是否能提供初步实验证据（至少 Phase 1 的 pilot 结果）来回应执行风险的质疑。

【主要风险】:
1. **"组合创新"质疑**：审稿人可能认为 CORe 的核心贡献是将已有工具（CD-T、PEAP、entropy neurons、attention intervention）组合应用于 RAG 场景，而非提出根本性新方法。Rebuttal 需要强调：(a) 组合本身需要非平凡的协调信号（这正是 naive stack baseline 要验证的），(b) 电路图谱和补偿动力学发现是独立的科学贡献。
2. **范围过广导致深度不足**：三个 Phase（电路发现 / 几何统一 / 协调干预）中任何一个都可以独立成文。压缩到一篇论文可能导致方法细节不足，审稿人难以判断技术可行性。建议考虑将 Phase 2a（几何统一）降级为辅助分析而非核心贡献，集中力量在"电路发现 → 补偿动力学验证 → 协调干预"的主线上。

【实施评估】:
  - 计算资源: 高。3 个 8B 模型 × 4 数据集 × (CD-T + PEAP pipeline + 7 baseline + 7 ablation) = 保守估计 500-1000 GPU 小时（A100 80GB）。Phase 1 电路发现是计算瓶颈。
  - 数据需求: 中低。NQ-swap、ConFiQA、CoFaithfulQA、MemoTrap 均为公开数据集，无需新数据收集。
  - 人工介入: 低。方法为全自动 pipeline，但电路图谱的解读和可视化需要研究者的分析判断。
  - 训练需求: 无。所有干预都是推理时进行（forward hooks），不修改模型参数——这是一个显著优势。
  - 新 Benchmark: 否。使用已有 benchmark。
  - 预估周期: 3-4 个月。Phase 1 pilot study（2-3 周）→ Phase 1 full（3-4 周）→ Phase 2（3-4 周）→ Phase 3 + 全部实验（4-5 周）→ 写作（2-3 周）。团队规模 3-4 人时可适度并行化。
```

Sources:
- [JuICE: Taming Knowledge Conflicts in Language Models (ICML 2025)](https://arxiv.org/abs/2503.10996)
- [CoRect: Context-Aware Logit Contrast for Hidden State Rectification (arXiv 2026)](https://arxiv.org/abs/2602.08221)
- [ParamMute: Suppressing Knowledge-Critical FFNs (NeurIPS 2025)](https://arxiv.org/abs/2502.15543)
- [SpARE: SAE-Based Representation Engineering (NAACL 2025)](https://aclanthology.org/2025.naacl-long.264/)
- [PEAP: Position-aware Automatic Circuit Discovery (ACL 2025)](https://aclanthology.org/2025.acl-long.141/)
- [CD-T: Efficient Automated Circuit Discovery via Contextual Decomposition (ICLR 2025)](https://arxiv.org/abs/2407.00886)
- [Simulated Adoption: Decoupling Magnitude and Direction (arXiv 2026)](https://arxiv.org/abs/2602.04918)
- [Context Copying Modulation: Entropy Neurons (EMNLP 2025 Findings)](https://aclanthology.org/2025.findings-emnlp.1116/)
- [Competition of Mechanisms Generalization Study](https://arxiv.org/abs/2506.22977)
- [JuICE GitHub Repository](https://github.com/GaotangLi/JUICE)
- [ParamMute GitHub Repository](https://github.com/OpenBMB/ParamMute)


【原始 proposal（允许参考但不是主要依据）】:
# CORe: Tracing and Repairing Override Circuits in RAG

## Core Problem and Primary Research Question

RAG-augmented LLMs systematically override retrieved evidence with parametric memory during knowledge conflicts. Existing interventions (SpARE, CoRect, JuICE, IRCAN) target single component types selected via statistical heuristics, yet consistently plateau in performance. We hypothesize this plateau stems from compensatory dynamics within a distributed override circuit: the override mechanism spans attention heads, FFN layers, and copy suppression components with redundant pathways, so repairing one node causes others to compensate and restore the parametric override.

**Primary research question:** Does the RAG override circuit exhibit compensatory dynamics — and if so, does coordinated multi-point intervention that addresses all compensatory pathways simultaneously outperform both single-point methods and naive stacking of independent single-point interventions?

This question has value regardless of outcome: if compensatory dynamics exist, they provide the first causal explanation for single-point intervention plateaus and necessitate coordinated repair; if they do not, then single-point failures stem from wrong target selection, and causal circuit tracing still provides principled target identification that heuristic methods lack.

**Why naive stacking is insufficient:** Simply combining existing methods (e.g., JuICE head amplification + ParamMute FFN suppression + entropy neuron ablation) without circuit-level understanding risks: (1) contradictory intervention directions at shared components (a head amplified by JuICE may belong to a pathway that ParamMute needs dampened); (2) uncontrolled interaction effects without principled strength calibration; (3) no diagnostic capability to determine which combination is appropriate per instance. Causal circuit tracing provides the coordinating signal that naive stacking lacks.

## Research Landscape

**Single-component heuristic interventions (current paradigm):**
JuICE (ICML 2025 Spotlight) discovered attention head superposition (same head promotes both memory and context), invalidating clean head-type dichotomies (PH3, IRCAN), and proposed dual-run head-level intervention achieving SOTA on 11 datasets — but remains head-level with no FFN or copy suppression analysis. CoRect (arXiv Feb 2026, arXiv:2602.08221) documented the flip phenomenon (56% of conflict failures: correct answer appears mid-layer then gets suppressed by deep FFN layers) and intervenes with additive rectification, but without circuit-level diagnosis of why specific layers suppress. SpARE (NAACL 2025 Oral) uses SAE features for steering with +10% EM gains, selecting targets via mutual information ranking at a single mid-layer point. ParamMute (NeurIPS 2025, arXiv:2502.15543) identifies mid-to-deep FFN layers (70%-90% relative depth) as critical for unfaithful generation and suppresses them — single component type. IRCAN (NeurIPS 2024) reweights context-aware neurons but uses statistical identification. CoCoA (EMNLP 2025) advances contrastive decoding with confidence-aware token-level adjustment, outperforming CAD and AdaCAD by up to 9.2 points — but operates at decoding level without internal mechanism understanding.

**Multi-stage approaches:**
CLEAR (arXiv:2510.12460, Oct 2025) implements three-stage intervention: fine-grained knowledge pruning → latent-state probing to localize conflicts → conflict-aware attention modulation. However, CLEAR uses probing-based correlation (no causal guarantee — probing localizes where conflicts manifest, not what causes them), requires conflict-aware fine-tuning (modifying model parameters), and modulates only attention (single component type). CORe differs in three ways: (1) causal circuit attribution via CD-T/PEAP vs. probing correlation; (2) pure inference-time intervention vs. fine-tuning; (3) coordinated 3-component intervention (FFN + attention + copy suppression) vs. attention-only.

**Mechanism-level understanding:**
Competition of Mechanisms (ACL 2024) traced factual recall (MLP) vs. in-context copying (induction heads) competition via logit inspection and attention modification. Its generalization study (arXiv:2506.22977) found head specialization weakens substantially in Llama 3.1 8B, suggesting override circuits are more distributed in larger models. CORe addresses the more complex RAG three-way interaction (query → evidence integration → parametric override) rather than binary competition, and designs intervention rather than just tracing. Context Copying Modulation (EMNLP 2025 Findings, arXiv:2509.10663) identified entropy neurons as key components suppressing context copying — providing a mechanistic basis for copy suppression that CORe's third intervention point will leverage, but studied in isolation without connecting to the broader override circuit. PhantomCircuit (EMNLP 2025, arXiv:2505.14406) applied circuit analysis to knowledge overshadowing between training data sources (inter-training-data conflicts, not RAG context-parametric conflicts).

**Geometric understanding:**
Simulated Adoption (arXiv Feb 2026, arXiv:2602.04918) showed conflict resolution operates via orthogonal interference — geometric rotation rather than magnitude suppression — across Llama-3.1-8B, Qwen-3-4B, and GLM-4-9B. How Transformers Reject Wrong Answers (arXiv Mar 2026, arXiv:2603.13259) independently found that transformers actively suppress correct answers through rotational dynamics on a representation hypersphere, with a phase transition at 1.6B parameters. Promote, Suppress, Iterate (EMNLP 2025) revealed multi-stage promote-then-suppress dynamics. The Override Gap (arXiv Apr 2026, arXiv:2604.23750) found magnitude-dominant failure in hypernetwork-based adaptation (Doc-to-LoRA) — a distinct paradigm from in-context RAG, but cautioning against universalizing geometric assumptions. These three independent geometric findings (Simulated Adoption, Marín 2026, Promote-Suppress-Iterate) have not been unified; CORe's Phase 2 aims to do so specifically in the RAG context.

**Gap:** No existing work combines (1) position-aware causal circuit tracing of RAG override mechanisms, (2) a unified geometric account of why correct answers appear then vanish (connecting the flip phenomenon, rotational suppression, and multi-stage dynamics), and (3) coordinated multi-point inference-time intervention that addresses compensatory pathways. Additionally, no method provides predictive diagnostics — the ability to explain per-instance why a given single-point intervention fails.

## Proposed Approach

**Phase 1 — Circuit Discovery via CD-T → PEAP Pipeline.** Run CD-T on Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B with NQ-swap/ConFiQA/MemoTrap conflict prompts to identify candidate override components (coarse screen). Apply PEAP with query/passage/answer position schemas on the CD-T candidate set to produce position-aware edge attributions (fine-grained refinement). Reconcile both into a unified circuit graph via normalized causal effect scores: each component's score = weighted combination of CD-T decomposition contribution and PEAP gradient attribution, normalized to [0,1] per prompt. Fallback: if reconciliation degrades circuit quality metrics, revert to pure pipeline (CD-T candidates → PEAP edges) without score fusion. Scalability note: CD-T uses mathematical decomposition (not activation patching) and claims transformer-agnostic scalability; PEAP requires 2 forward + 1 backward pass per prompt-pair. A pilot study on 100 NQ-swap samples × Llama-3.1-8B will establish actual runtime and memory requirements before full-scale experiments. If CD-T proves impractical at 8B scale, HAGD (arXiv:2601.12879) offers O(n²log n) complexity as an alternative.

**Phase 2 — Characterizing Override Geometry and Testing Compensatory Dynamics.**
Two sub-goals: (2a) Provide a unified geometric account of the flip phenomenon. Three independent observations suggest a coherent mechanism: CoRect's flip phenomenon (correct answer appears mid-layer then vanishes), Simulated Adoption's orthogonal interference (geometric rotation in conflict resolution), and Marín's rotational suppression (active rejection via rotation on hypersphere, arXiv:2603.13259). Testable unified hypothesis: deep FFN layers inject parametric direction vectors quasi-orthogonal to the context-aligned representation, implementing rotational suppression at the evidence-integration-to-override transition — the same geometric mechanism identified in simpler settings, but operating within RAG's multi-stage pipeline. Stage-wise ablation decomposes layer-wise residual stream updates at flip points into direction and magnitude components, testing whether ablating rotational vs. magnitude components selectively recovers the correct answer. The framework accommodates rotation-dominant, magnitude-dominant, or mixed outcomes.
(2b) Test for compensatory dynamics: after Phase 1 identifies the circuit, selectively ablate individual pathway types (FFN override nodes only, retrieval heads only, copy suppression only) and measure whether remaining pathway types increase their override contribution to compensate. This directly tests the primary research question.

Flip event operational definition (independent of CoRect's implementation): at layer L, the correct answer token's logit rank enters top-k; at layer L+Δ, it exits top-k. This captures the same phenomenon without dependency on CoRect's specific logit contrast methodology. Contingency: if flip events are not prevalent on certain models/architectures, Phase 3 intervention calibration falls back to Phase 1 circuit attribution scores alone (still principled, though without flip-specific geometry profiling).

**Phase 3 — Geometry-Aware Coordinated 3-Point Intervention.** Inference-time intervention simultaneously addressing three override pathway components: (A) dampen parametric FFN re-promotion at identified override layers, (B) amplify retrieval head signals at evidence-integration positions, (C) inhibit copy suppression — informed by entropy neuron findings (Context Copying Modulation, EMNLP 2025 Findings, arXiv:2509.10663) — at output-proximal layers. Calibration is geometry-aware per Phase 2 profile: rotation-dominant → project out parametric direction; magnitude-dominant → scale activations; mixed → hybrid. All interventions implemented via single-pass forward hooks (no dual-run overhead).

## Evaluation Design

**Models:** Llama-3.1-8B, Qwen3-8B, Gemma-2-9B (3 architectures).

**Datasets:** NQ-swap, ConFiQA, CoFaithfulQA, MemoTrap (entity substitution, multi-hop, faithfulness, memorization-trap conflict types).

**Baselines:** JuICE (head-level SOTA), CoRect (FFN rectification), SpARE (SAE steering), ParamMute (FFN suppression), CoCoA (contrastive decoding SOTA, EMNLP 2025), IRCAN (neuron-level). Supplementary: Knowledgeable-R1 (ICLR 2026, RL-based), TCR (AAAI 2026, detection + soft-prompt). Additional critical baseline: **Naive Stack** (JuICE heads + ParamMute FFN suppression + entropy neuron ablation applied simultaneously without circuit guidance) — directly tests whether circuit-informed coordination adds value beyond independent method combination.

**Metrics — Task Performance:** EM, token-level F1, memorization ratio (per ParamMute). **No-conflict control:** EM/F1 on standard (non-conflicting) RAG inputs + output perplexity, verifying intervention does not degrade normal generation quality. **Circuit Quality (Phase 1-2):** circuit faithfulness, completeness, sparsity (per CD-T/PEAP evaluation frameworks).

**Ablation Matrix:**
- Component isolation: (A) FFN dampening only, (B) retrieval head amplification only, (C) copy suppression inhibition only, (AB), (AC), (BC), (ABC = full CORe) — 7 configurations. Key test: does removing one component cause remaining components' effectiveness to degrade (evidence of compensatory dynamics)?
- Intervention strategy: geometry-aware vs. magnitude-only calibration under same 3-point framework.
- Sensitivity: 3-5 intervention strength values per component.
- **Circuit transferability:** discover circuit on dataset A, apply intervention to datasets B/C/D without re-discovery — tests practical deployability.

**Predictive Diagnostics Analysis:** For instances where baseline X fails but CORe succeeds, analyze which circuit pathways are active — demonstrating CORe's diagnostic capability beyond aggregate metric improvement.

**Inference Efficiency:** (1) Per-sample cost: additional forward passes (CORe: 0, single-pass hooks; JuICE: 1 extra; CoRect: 1 extra; CoCoA: 1 extra), wall-clock time, peak GPU memory. (2) Amortized setup cost: GPU-hours for one-time circuit discovery per model (one-time; subsequent inference is hook-only).

**Statistical Rigor:** Core comparisons (CORe vs. each primary baseline, full vs. ablated) report mean ± std over 3 runs with paired bootstrap significance tests.

## Broader Significance

Beyond RAG knowledge conflicts, the diagnose-then-intervene framework (position-aware circuit tracing → geometry characterization → coordinated multi-point repair) may generalize to other LLM internal conflict scenarios: instruction-following vs. safety guardrails, competing reasoning paths in multi-hop inference, cross-lingual knowledge interference. PhantomCircuit (EMNLP 2025, arXiv:2505.14406) has already demonstrated circuit-level analysis transfers across conflict types. We leave these extensions to future work.

## Concurrent Work Check

No 2026 submission combines causal circuit tracing with multi-point RAG intervention. Closest: ParamMute (FFN-only, no circuit tracing), CLEAR (probing-based, requires fine-tuning, attention-only), ReDeEP (ICLR 2025, detection not repair), PhantomCircuit (training-data conflicts not RAG), Knowledgeable-R1 (ICLR 2026, RL-based not mechanistic), TCR (AAAI 2026, detection + soft-prompt, no mechanistic analysis).

## Key References

- Taming Knowledge Conflicts in Language Models [JuICE] (ICML 2025)
- CoRect: Context-Aware Logit Contrast for Hidden State Rectification (arXiv 2026, arXiv:2602.08221)
- Steering Knowledge Selection via SAE-Based Repr. Engineering [SpARE] (NAACL 2025)
- Efficient Automated Circuit Discovery via Contextual Decomposition [CD-T] (ICLR 2025)
- Position-aware Automatic Circuit Discovery [PEAP] (ACL 2025)
- Simulated Adoption: Decoupling Magnitude and Direction in LLM Conflict Resolution (arXiv 2026, arXiv:2602.04918)
- Resisting Contextual Interference in RAG [Knowledgeable-R1] (ICLR 2026)
- Promote, Suppress, Iterate (EMNLP 2025)
- ReDeEP: Detecting Hallucination in RAG via Mechanistic Interpretability (ICLR 2025)
- ParamMute: Suppressing Knowledge-Critical FFNs for Faithful RAG (NeurIPS 2025, arXiv:2502.15543)
- Competition of Mechanisms: Tracing How Language Models Handle Facts and Counterfactuals (ACL 2024) + On the Generalizability of Competition of Mechanisms (arXiv:2506.22977)
- Context Copying Modulation: The Role of Entropy Neurons (EMNLP 2025 Findings, arXiv:2509.10663)
- PhantomCircuit: Pierce the Mists of Knowledge Conflicts (EMNLP 2025, arXiv:2505.14406)
- The Override Gap: Magnitude Account of Knowledge Conflict in Hypernetwork Adaptation (arXiv Apr 2026, arXiv:2604.23750)
- Seeing through the Conflict (AAAI 2026)
- How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing (arXiv Mar 2026, arXiv:2603.13259)
- CLEAR: Probing Latent Knowledge Conflict for Faithful RAG (arXiv:2510.12460, Oct 2025)
- CoCoA: Confidence- and Context-Aware Adaptive Decoding (EMNLP 2025)
- IRCAN: Identifying and Reweighting Context-Aware Neurons (NeurIPS 2024)
- HAGD: Hierarchical Attribution Graph Decomposition (arXiv:2601.12879)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "dd9a0bcb-1df5-4fd7-945a-424fd3ded77a",
  "type": "user",
  "uuid": "70f2d776-6337-4dbb-a53a-15052a2e029e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:53:36.443Z_

```json
{
  "parentUuid": "70f2d776-6337-4dbb-a53a-15052a2e029e",
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
  "uuid": "e8169a7c-1d4a-4bc6-96ca-d8038222d6d4",
  "timestamp": "2026-05-30T07:53:36.443Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:53:36.443Z_

```json
{
  "parentUuid": "e8169a7c-1d4a-4bc6-96ca-d8038222d6d4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2857604f-823b-4e10-bc32-fd4e4ea26b8a",
  "timestamp": "2026-05-30T07:53:36.443Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct the evaluation. L…",
  "leafUuid": "2857604f-823b-4e10-bc32-fd4e4ea26b8a",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified RAG override circuit tracing and coordinated repair",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76"
}
```

---

### Assistant

_source line 8 · 2026-05-30T07:54:08.195Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

First, let me extract the key numbers and assessments:

**Reviewer 1:** [28% - 42%] 中位 35%
**Reviewer 2:** [30% - 42%] 中位 35%
**Reviewer 3:** [25% - 40%] 中位 33%

Three medians: 35%, 35%, 33%
Mean of medians: 34.3%
Median of medians: 35%


Standard deviation of medians is about 0.94%, which indicates high consistency across reviewers.

Now I'm working through the rubric dimensions. For 研究问题, all three reviewers rated it as 强, so that's a unanimous 3.

Moving through the rest: 方法与创新 shows consistent 中偏强 ratings across all reviewers, 实验设计 is unanimously 强, 可行性 is uniformly 中, and 写作与呈现 is also unanimously 强. The consensus is remarkably strong across every dimension.

Looking at the risk points that multiple reviewers flagged: the scope being too broad and trying to combine three papers into one, questions about whether the compensation dynamics hypothesis actually holds, concerns that this is more of a combination of existing methods rather than a novel approach, scalability worries for CD-T at the 8B model size, and potential convergence issues with geometric unification. There are also some individual concerns—one reviewer wants human evaluation and case studies, another questions why simpler causal tracing wouldn't suffice, and there's a note about potential competing work emerging during the AAAI review cycle.

Given how tightly the three reviewers align on these assessments—the standard deviation is less than 1%, and they're all identifying the same core risks—I should anchor to the median values. The probability estimates cluster around 33-35%, all within a couple percentage points of each other. With this level of consensus, I'll narrow the interval to [28% - 40%] with a median estimate of 34%.

This approach respects the principle of being slightly conservative while reflecting the strong agreement across all dimensions. Now I need to synthesize the implementation assessments—the reviewers are aligned that computational resources are high (ranging from 200-1000 GPU hours depending on the setup) and data requirements are moderate across the board.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2857604f-823b-4e10-bc32-fd4e4ea26b8a",
  "isSidechain": false,
  "requestId": "req_011CbYPhHq4joNEVNMxSvXQT",
  "type": "assistant",
  "uuid": "3708ea83-d7da-40e9-9281-ff0bd8dc251d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QBe5gojpQjb1GTqqU9piSB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22105,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3242,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 22105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22105
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

_source line 9 · 2026-05-30T07:54:54.815Z_

【阶段】: Meta Judge
【三次中位】: [35%, 35%, 33%]  std=0.94%
【共识维度】:
- 研究问题: **强**（3/3 一致）— 三位审稿人均认为"为什么单点干预 plateau"是领域真实且重要的开放问题，补偿动力学假设可证伪且双向有价值
- 方法与创新: **中偏强**（3/3 一致）— 三位均指出核心工具（CD-T、PEAP、entropy neuron ablation）来自已有工作，创新在"组合方式"而非"基础方法"；同时均承认该组合在 RAG 场景首创且非平凡
- 实验设计: **强**（3/3 一致）— 三位均高度评价 Naive Stack baseline、7 配置 ablation、3 模型 × 4 数据集矩阵、统计严谨性；均认为这是 proposal 最突出的维度
- 可行性: **中**（3/3 一致）— 三位均指出 scope 过大（三篇论文合一）、CD-T 8B 规模化风险、Phase 间顺序依赖的级联风险；均认可 contingency planning 的成熟度
- 写作与呈现: **强**（3/3 一致）— 三位均赞赏文献覆盖深度、叙事逻辑链、差异化分析的精准性
- **核心风险共识**（3/3 均提到）：(1) scope 过大可能导致"广而不深"；(2) 补偿动力学假设可能不成立；(3) "组合创新 vs. 原创方法"的审稿人质疑；(4) CD-T 在 8B 模型上的可扩展性未验证
- **次要风险共识**（2/3 提到）：几何统一可能在不同架构上不收敛（R2、R3）

【异常维度】:
- R1 独有：缺少 human evaluation / case study 分析（对 QA 任务非必需，降权处理）
- R3 独有：未论证为何更简单的 causal tracing（如 Meng et al. 2022 式 activation patching）不够用（有一定道理但非致命，保留作为补救方向）
- R3 独有：AAAI 审稿窗口内可能出现直接竞争工作（属不可控外部风险，不影响 proposal 本身质量评估）

【最终概率】: [29% - 40%] 中位 34%
【一致性】: 高（std=0.94%，三位审稿人在全部 5 个 rubric 维度和核心风险识别上完全一致）
【综合理由】:
三位审稿人展现了罕见的高度一致性——不仅概率估计紧密聚拢（33%-35%），而且在所有 5 个 rubric 维度的判定上完全相同（强-中偏强-强-中-强），且独立识别出了相同的 4 个核心风险。这种一致性使得综合判断具有高置信度。

最终中位取 34%（略低于三位的算术均值 34.3%），遵循"宁缺毋滥"原则做微幅下调。理由：R3 给出的 33% 虽然偏低但其额外关切（未论证简单 causal tracing 为何不够用）具有一定合理性，值得在综合时给予权重。

区间缩窄至 [29%-40%]（相比三位的联合区间 [25%-42%]）：高一致性支持收窄，下界从 25% 上调至 29% 是因为 R3 的 25% 下界过于悲观（其下调主要基于"AAAI 审稿周期内可能出现竞争"这一外部不可控因素），上界从 42% 下调至 40% 遵循"不比最宽松更宽松"原则（R3 上界即 40%）。

**定位总结**：这是一份"问题好、设计精良、执行风险高"的 borderline proposal。34% 的中位反映了：idea 质量（研究问题强 + 方法中偏强）设定了约 38-40% 的天花板，而可行性风险（scope 过大 + 核心假设推测性 + 规模化不确定性）将实际概率从天花板拉低约 5-6 个百分点。如果执行完美且补偿动力学假设成立，可触及 40%；如果任一核心假设失败或 scope 导致深度不足，将跌至 29% 附近。

【建议】: 边缘（中位 34% 处于 borderline 区域，值得进入迭代优化流程尝试提升）
【实施评估】:
  - 计算资源: 高。3 个 8B 模型的 CD-T + PEAP 电路发现 + 3×4×7+ 的完整实验矩阵。三位审稿人估计 200-1000 GPU 小时（A100 80GB），取保守估计 400-800 GPU 小时，需 4-8 卡持续运行。Phase 1 电路发现是计算瓶颈，pilot study（100 样本 × 单模型）需 1-2 周 GPU 时间做可行性验证。
  - 数据需求: 中低。NQ-swap、ConFiQA、CoFaithfulQA、MemoTrap 均为公开数据集，无需新数据收集或标注。
  - 人工介入: 低至中。Pipeline 高度自动化，但电路图谱解读、几何分析的可视化判断、干预强度初始校准需要研究者专家判断。
  - 训练需求: 无。所有干预通过推理时 forward hooks 实现，不修改模型参数——这是相对 CLEAR 等需要 fine-tuning 的方法的显著优势。
  - 新 Benchmark: 不需要。使用已有公开 benchmark 组合。
  - 预估周期: 3-4 个月（三位审稿人一致）。Phase 1 pilot + 全量电路发现（5-7 周）→ Phase 2 几何分析 + 补偿动力学测试（3-4 周）→ Phase 3 干预实现 + 完整实验矩阵（4-5 周）→ 写作（2-4 周）。3-4 人团队可适度并行化。如精简 scope（如减少模型数或将几何统一降为辅助分析），可压缩至 2.5-3 个月。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3708ea83-d7da-40e9-9281-ff0bd8dc251d",
  "isSidechain": false,
  "requestId": "req_011CbYPhHq4joNEVNMxSvXQT",
  "type": "assistant",
  "uuid": "a40ddb5e-7557-4caa-8c32-2825030c010c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QBe5gojpQjb1GTqqU9piSB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22105,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3242,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 22105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22105
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct the evaluation. L…",
  "leafUuid": "a40ddb5e-7557-4caa-8c32-2825030c010c",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified RAG override circuit tracing and coordinated repair",
  "sessionId": "02b12412-4617-4da9-95ab-ccadfdb02d76"
}
```

---
