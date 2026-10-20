# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/900c5be3-d76c-4e50-a5c1-51b0987ca813.jsonl`
- **Structured JSON:** [`8baef686ce6284462adf.json`](../../sessions/8b/8baef686ce6284462adf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T19:20:40.414Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T19:20:40.414Z",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n==========================================================================\n⚠️ 关键前置问题：严重的投稿目标会议错位\n==========================================================================\n\n在进入 idea 质量评估之前，必须指出一个致命问题：\n本 proposal 关于 NLP/ML 领域的 Process Reward Model 机制可解释性，\n而 CoRL (Conference on Robot Learning) 的核心主题是机器人学习：\n仿真到真实迁移、机器人操纵/运动/导航/驾驶、机器人感知、\n机器人强化学习等。CoRL 2026 (Austin, TX, Nov 10-12) 的 Call for Papers\n明确要求 \"real-robot experiments or convincing evidence that simulation\nexperiments are transferable to real robots\"。\n\n本 proposal 与机器人学习领域零交集——无机器人实验、无机器人任务、\n无 embodied 组件。如果直接投稿 CoRL 2026 主会，大概率被 desk reject。\n\n适合的目标会议：ICML / NeurIPS / ICLR (ML track) 或 ACL / EMNLP (NLP track)。\n\n以下评估假设投稿目标为一个合适的 ML/NLP 顶会（如 NeurIPS 2026），\n以便下游 agent 能在正确语境下优化 proposal。\n\n==========================================================================\n\n【领域调研】:\n\n- [Basu et al., arXiv:2603.18353] (March 2026): \"Interpretability without \n  Actionability\" — 在临床分诊 LM 上测试四种机制可解释性干预方法\n  （含 SAE steering、activation patching），发现均无法有效纠正输出错误。\n  线性探针达 98.2% AUROC 但模型输出灵敏度仅 45.1%，存在 53pp 的\n  knowledge-action gap。已验证存在，是本 proposal 的核心对比点。\n\n- [SteerRM, arXiv:2603.12795] (March 2026): 北大团队提出首个\n  training-free SAE-based RM 去偏方法。使用预训练 LlamaScope SAE，\n  在 RM-Bench Hard split 上平均提升 7.3 points。发现 format-related\n  features 集中在浅层且跨模型迁移。已经实现了 feature-level 干预。\n\n- [CIRM / Shinoda et al., arXiv:2604.27495] (April 2026, ACL 2026): \n  NTT 团队提出 neuron-level 因果中介分析去偏，编辑 <2% neurons \n  即可匹配 70B RM 性能。已经实现了 neuron-level 干预。\n\n- [Orgad et al., arXiv:2605.11161] (ICML 2026 Position Paper): \n  提出可解释性应以 actionability 为评估标准，定义 concreteness \n  和 validation 两个维度。本 proposal 采用其评估框架但并非核心创新。\n\n- [Lee et al., arXiv:2605.05508] (May 2026): \n  提出可解释性作为严格评估的三个科学标准（可证伪性、可复现性、\n  预测性），提供互补诊断框架。\n\n- [Zhang et al., arXiv:2601.14004] (Jan 2026): \"Locate, Steer, Improve\" \n  综述，提供 actionable MI 的最全面分类法。本 proposal 实例化其 pipeline。\n\n- [CRA, arXiv:2508.04216] (2025): 在 PRM 激活上从头训练 SAE 用于\n  后门纠正，本 proposal 的 SAE 方法论直接沿用此工作。\n\n- [Arad et al., arXiv:2505.20063] (EMNLP 2025): 区分 output features\n  和 input features 可带来 2-3× 改进。本 proposal 采用其过滤方法。\n\n- 调研总结: 这个领域在 2026 年初极为活跃。PRM 去偏已有 feature-level\n  (SteerRM)、neuron-level (CIRM)、probe-level (One Bias After Another) \n  等多种粒度的独立工作。\"可解释性是否 actionable\"的辩论也有了正反两方\n  的 position papers。本 proposal 试图在已有拼图上做\"统一比较框架+\n  domain amenability 假说\"，但核心方法论组件均来自已有工作。\n\n\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁，分两个层面：\n\n(1) 对于 \"Domain Amenability Hypothesis\"：这个假说本质上在说\"当任务\n    有明确输出语义、受限输出结构、可验证 ground truth、可独立测试\n    specificity 时，机制干预更容易成功\"。这近乎同义反复——\"当你能\n    清晰定义成功、精确测量效果、独立检验副作用时，干预更可能被判定\n    为成功\"。一个更 trivial 的表述是：\"机制干预在更简单、更可度量的\n    任务上效果更好\"。审稿人很可能认为这不是一个需要实验验证的\n    hypothesis，而是一个 obvious observation。\n\n(2) 对于 PRM 去偏本身：fine-tuning on debiased data（proposal 自己\n    列为 baseline）可能以更低成本达到类似或更好效果。Factored CRL\n    (ICML 2026) 已经在训练时解决了这个问题。本 proposal 的增量价值\n    在于\"理解 why/when 干预 work\"，但如果假说本身是 trivial 的，\n    这个增量价值就大打折扣。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链有以下未经验证的环节：\n\n(1) N=2 归纳问题：整个 Domain Amenability Hypothesis 的\"验证\"建立在\n    两个数据点上——PRM（满足四条件，干预成功）vs. 临床 LM（不满足\n    四条件，干预失败）。但这两个域之间的差异远不止这四个条件（模型\n    架构、训练数据、任务类型、模型规模、领域知识等全部不同）。无法\n    排除混淆因素，无法证明是这四个条件而非其他因素导致了成功/失败\n    的差异。这不是\"验证假说\"，而是\"post-hoc rationalization\"。\n\n(2) 四个条件的选择缺乏理论基础：为什么是这四个条件而非其他？为什么\n    不是\"输出维度低\"、\"任务复杂度低\"、\"偏差是线性可分的\"等？\n    这四个条件看起来是从 PRM 的特征反推出来的（PRM 有什么特点 →\n    这些特点就是成功的条件），存在严重的 overfitting to the \n    observation 风险。\n\n(3) \"43% of reward gains from stylistic exploitation\" 这个数字来自\n    Tiwari et al.，但这是在特定 PRM 和特定攻击设置下的结果，\n    能否推广到本 proposal 使用的 Qwen2.5-Math-PRM 和 \n    Math-Shepherd-Mistral-7B-PRM 是未经验证的。\n\n(4) 对 Basu et al. 失败的归因：Basu et al. 的失败可能有多种原因\n    （SAE 质量差、steering 方向选择不当、临床任务本身更难等），\n    proposal 将其归因于\"domain 不满足四条件\"是一个未经验证的\n    归因。Basu et al. 自己的分析也指向了更具体的技术原因。\n\n\n【3 维度打分】:\n\n1. Novelty: 弱 — \n   核心贡献有两个层面：(a) Domain Amenability Hypothesis 和 \n   (b) multi-granularity comparison。\n   \n   对于 (a)：这个假说本身接近同义反复（见 Trivial Alternative 检验），\n   且仅基于 N=2 的 post-hoc 对比，缺乏理论推导。这不构成 strong \n   novelty。\n   \n   对于 (b)：这是一个 systematic empirical comparison，但比较的\n   对象——feature-level (SteerRM, 2603.12795)、neuron-level \n   (CIRM, 2604.27495)、circuit-level (activation patching) ——\n   均为已有方法的直接应用或微调。唯一的方法论增量是将 Arad et al.\n   的 output-score filtering 与 CRA 的 from-scratch SAE 结合，\n   但这是 straightforward engineering integration。\n   \n   与最相关工作的 delta：SteerRM 已做 feature-level；CIRM 已做\n   neuron-level；CRA 已做 PRM-specific SAE training。本 proposal\n   的核心 novelty 是\"把它们放在一起比较\"+ 一个薄弱的 framing 假说。\n   这更接近 survey + benchmark 而非 research contribution。\n\n2. Significance: 中 — \n   \"when do mechanistic interventions succeed\" 是 MI 社区当前的\n   核心问题之一，Basu et al. 和 Orgad et al. 分别从负面和正面\n   推动了这个讨论。这个问题的重要性毋庸置疑。\n   \n   但本 proposal 对这个问题的回答质量堪忧：N=2 的 domain 对比\n   不可能给出有说服力的答案。即使 PRM 干预成功，审稿人仍然无法\n   判断是因为 Domain Amenability Hypothesis 的四个条件还是其他\n   原因。结论的可推广性极低。\n   \n   PRM 去偏的实际应用价值存在，但 discriminative PRM 正在被\n   generative PRM (ThinkPRM, GenPRM) 替代，这削弱了 practical \n   significance。\n   \n   对领域的影响：如果结果 positive，贡献的是\"又一个 MI 干预成功\n   的 case study\"，但 SteerRM 和 CIRM 已经提供了类似证据。\n   如果结果 negative，那更有意思（但 proposal 的设计倾向于 \n   positive result）。\n\n3. Related Work: 强 — \n   Related work 覆盖极为全面，涵盖了 actionability debate 双方\n   (Basu et al., Orgad et al.)、所有主要 intervention 粒度\n   (SteerRM, CIRM, CRA, One Bias After Another)、评估框架\n   (Lee et al.)、分类法 (Zhang et al.)、电路分析工具 \n   (RelP, CLT-Forge)、self-repair (McGrath et al.) 等。\n   差异化定位也算清晰——\"统一比较框架\"的定位在文献中确实空白。\n   引用的论文经核实均真实存在且描述准确。\n\n\n【概率估计】: [15% - 25%] 中位 20%\n\n【估计理由】: \n投稿 CoRL 的话概率接近 0%（完全 off-topic，会被 desk reject）。\n\n即使投稿合适的 ML/NLP 顶会（NeurIPS/ICML/ACL），idea 质量也\n处于 15-25% 区间：\n\n- Novelty 是核心瓶颈。Domain Amenability Hypothesis 近乎同义反复\n  且 N=2 归纳不具说服力；multi-granularity comparison 是 \n  straightforward 的已有方法组合。审稿人大概率会评价为 \"well-executed\n  but incremental\"。\n\n- Significance 被两个因素削弱：(a) discriminative PRM 正被 generative \n  PRM 替代，降低了实际应用价值；(b) 对核心问题 \"when do MI interventions \n  succeed\" 的回答因 N=2 设计而不具说服力。\n\n- Related work 的强项不足以弥补 novelty 的弱项——在顶会审稿中，\n  idea 新颖性通常是决定性因素。\n\n- 形式完善度很高（详细的实验 plan、完整的 resource estimate、\n  双 outcome 设计），但这是执行层面的优势，不改变 idea 内核。\n\n上界 25% 受限于 Novelty 维度——即使实验完美执行，核心 claim \n的 intellectual contribution 仍然薄弱。\n\n【主要风险】: \n1. Domain Amenability Hypothesis 被审稿人判定为 tautological/obvious，\n   且 N=2 对比被认为不构成 hypothesis testing（这是最可能的拒稿理由）\n2. \"统一比较已有方法\"的定位被归类为 benchmark/survey paper 而非\n   research paper，不符合顶会主会对 novelty 的要求\n```\n\n**补充说明给下游 agent：**\n\n如果要进入迭代优化，我建议重点关注两个方向：\n1. **必须解决 venue 问题**——如果坚持投 CoRL，需要彻底重新设计 proposal 使其与机器人学习相关（例如：将机制可解释性应用于 robot reward models / robot policy learning），否则投稿无意义。\n2. **如果转投 NLP/ML 顶会**，核心问题是 Domain Amenability Hypothesis 太弱——需要要么 (a) 增加更多对比域使假说检验更有说服力，要么 (b) 放弃假说包装、转而强化 multi-granularity comparison 的方法论贡献和实用价值。\n\nSources:\n- [Interpretability without Actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)\n- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495)\n- [Position: Interpretability Can Be Actionable (Orgad et al.)](https://arxiv.org/abs/2605.11161)\n- [Rigorous Interpretation Is a Form of Evaluation (Lee et al.)](https://arxiv.org/abs/2605.05508)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 About](https://www.corl.org/about-corl)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：投稿目标 venue 严重不匹配】\n\n本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。CoRL 2026 的 Call for Papers 明确要求 submissions \"focus on a core robotics problem\" 并鼓励 \"real-robot experiments or convincing evidence that simulation experiments are transferable to real robots\"。其 topics 包括 robot manipulation、navigation、locomotion、driving 等。\n\n本 proposal 的内容是对 **数学推理领域的 Process Reward Models** 进行 mechanistic interpretability 分析与多粒度干预比较。全文无任何机器人相关内容。这不是\"scope 偏边缘\"的问题，而是**完全不在会议范围内**，大概率在 desk review 阶段即被拒。\n\n该 proposal 的自然投稿目标应为 NeurIPS、ICML、ICLR 或 ACL/EMNLP。以下评估将**假设投稿到合适的 ML/NLP venue**来评价 idea 质量本身，但最终概率估计会反映 CoRL 的实际接收可能性。\n\n---\n\n【领域调研】:\n\n- **Basu et al. \"Interpretability without Actionability\" (arXiv:2603.18353, March 2026)**: 在临床分诊 LM 上测试 4 种 mechanistic intervention（含 SAE steering、activation patching），发现 knowledge-action gap 持续存在——linear probes 可达 98.2% AUROC 但 output sensitivity 仅 45.1%，最好的 intervention 仅纠正 24% 的错误。这是本 proposal 的核心动机论文。确认真实存在，描述准确。\n\n- **SteerRM (arXiv:2603.12795, March 2026)**: 使用预训练 LlamaScope SAE 对 RM 进行 feature-level debiasing，RM-Bench Hard split 提升 7.3 分。限制：仅适用于有预训练 SAE 的架构，有效分析限于 layers 0-9。确认真实存在，描述准确。\n\n- **CIRM / Shinoda et al. (arXiv:2604.27495, ACL 2026)**: 使用 Spearman correlation 做 bias-specific neuron identification + causal mediation analysis，编辑 <2% neurons 在 general RMs 上达到 70B 级性能。确认真实存在，描述准确。\n\n- **CRA (arXiv:2508.04216, 2025)**: 从头在 PRM activations 上训练 SAE，通过 backdoor adjustment 修正 reward hacking。确认真实存在，proposal 的描述准确。\n\n- **Arad et al. \"SAEs Are Good for Steering\" (EMNLP 2025)**: 区分 input features vs. output features，output-score filtering 带来 2-3x steering 改善。确认真实存在，描述准确。\n\n- **Orgad et al. \"Interpretability Can Be Actionable\" (ICML 2026, position paper)**: 提出 concreteness × validation 双维评估框架。确认真实存在，描述准确。\n\n- **Lee et al. \"Rigorous Interpretation Is a Form of Evaluation\" (arXiv:2605.05508, May 2026)**: 提出 falsifiability / reproducibility / predictivity 三标准。确认真实存在，描述准确。\n\n- **Zhang et al. \"Locate, Steer, and Improve\" (arXiv:2601.14004, Jan 2026)**: 最全面的 actionable MI survey，分类 localization 和 intervention 方法。确认真实存在。\n\n- **Wang et al. \"Automatically Finding Reward Model Biases\" (arXiv:2602.15222, Feb 2026)**: 自动化 evolutionary bias discovery pipeline。确认真实存在，描述准确。\n\n- **\"One Bias After Another\" (arXiv:2603.03291, 2026)**: 使用 linear probes 做 mechanistic reward shaping。确认存在。\n\n- **调研未发现的关键空白**: 搜索 \"domain amenability\" + mechanistic interpretability 未找到任何现有工作使用过这一术语或框架。该 framing 确实是 proposal 自己的贡献。但也未找到任何工作系统比较 feature / neuron / circuit 三种粒度的 MI intervention 在同一 domain 上的效果。\n\n- **调研总结**: PRM debiasing 在 2025-2026 是一个快速增长的小领域，已有 feature-level (SteerRM)、neuron-level (CIRM)、probe-level (One Bias After Another)、SAE-from-scratch (CRA) 等独立工作。actionability debate (Basu vs. others) 是 2026 MI 社区的热点话题。但**目前没有工作将这些方法在统一框架下比较**，也**没有工作显式提出和测试\"什么 domain 条件下 MI intervention 更可能成功\"的假设**。\n\n---\n\n【Trivial Alternative 检验】:\n\n存在明确的 trivial alternative 威胁：\n\n1. **Fine-tuning on debiased data**: 如果目标是 PRM debiasing，最简单的方法是在去偏数据上微调 PRM。Proposal 虽然将此列为 baseline，但没有论证为什么 mechanistic approach 应当**根本上优于**这一方法。如果 fine-tuning 在所有 benchmark 上都能匹配或超过所有 mechanistic interventions，那整个 multi-granularity comparison 的实用价值就大打折扣——即使它仍有 scientific understanding 的价值。\n\n2. **Linear probes + simple editing**: \"One Bias After Another\" 已经用简单的 linear probes 做 mechanistic reward shaping。如果 linear probes 就够用，那 SAE + circuit tracing 的复杂 pipeline 的增量价值在哪？\n\n**增量价值定位**: Proposal 的真正价值不在\"PRM debiasing 的实用效果\"（这可能被 trivial alternatives 达到），而在**理解性问题**——\"WHEN 和 WHY 机制级别的 intervention 能成功\"。但这意味着 proposal 的核心贡献是 empirical understanding，不是 practical improvement，这在顶会的 novelty 评估中是一个较弱的位置。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有几个关键未验证假设：\n\n1. **Domain Amenability Hypothesis 的可证伪性极弱**: 用 N=1 正例（PRMs）和 N=1 反例（Basu et al. 的 clinical LMs）来\"测试\"一个 4-condition 假设，统计上几乎不可能得出有意义的结论。这更接近 post-hoc rationalization 而非 hypothesis testing。4 个条件（well-defined output semantics, constrained output structure, verifiable ground truth, independently testable specificity）是在已知 PRMs 的特性后定制的，存在严重的 overfitting-to-the-example 风险。\n\n2. **跨 domain 对比的 confound 太多**: PRMs vs. clinical LMs 的差异不仅仅是这 4 个条件——模型架构不同、训练数据不同、任务复杂度不同、研究者不同。将 intervention 成败归因于 domain conditions 而非其他 confounders 是一个很强的假设。\n\n3. **\"If interventions succeed, this provides positive evidence for the hypothesis\"**: 这是一个单向验证。如果 PRM interventions 成功，我们无法区分是因为\"domain amenability\"还是因为\"这些特定的 PRMs 恰好容易被 intervention\"。只有当 proposal 在多个满足/不满足各条件的 domain 上系统测试时，假设才有说服力。\n\n4. **43% stylistic exploitation 的普遍性**: Tiwari et al. 的发现是否在 Qwen2.5-Math-PRM 和 Math-Shepherd-Mistral 上同样成立？Proposal 假设了这一点但未验证。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   - 积极面: \"Domain Amenability Hypothesis\" 作为一个 framing 是新的（搜索确认无先例），将 feature/neuron/circuit 三粒度在统一框架下比较也是首次。结合 Orgad et al. + Lee et al. 的评估标准构建 granularity-by-criterion matrix 是有组织创新的。\n   - 限制面: 每个组成部分（SAE on PRMs → CRA 已做; feature-level debiasing → SteerRM 已做; neuron-level → CIRM 已做; circuit tracing → RelP/CLT 已有工具; output-score filtering → Arad et al. 已提出）都是现有方法的直接应用。核心 novelty 是 **comparison + framing**，不是 **method or discovery**。这在 ML 顶会中属于 \"solid empirical study\" 而非 \"conceptual breakthrough\"，novelty 评价通常会落在 \"moderate\" 区间。\n   - 关键参考: SteerRM (2603.12795) 已做 feature-level PRM debiasing; CIRM (2604.27495) 已做 neuron-level; CRA (2508.04216) 已训练 SAE on PRM activations。本 proposal 的 delta 是将这些放在一起比较。\n\n2. **Significance: 中** — \n   - 积极面: \"When do mechanistic interventions succeed?\" 是 MI 社区在 2026 的核心争论之一（Basu et al. vs. Orgad et al.），选题切中时代痛点。如果能给出清晰答案，对领域有真实推进价值。\n   - 限制面: (a) Domain Amenability Hypothesis 在本 proposal 中的测试强度不足（N=1 vs. N=1），即使实验全部成功，审稿人仍会质疑\"你证明了 PRM 上能 work，但这能 generalize 到你假设的 4 个条件吗？\" (b) 核心发现如果是 positive（\"interventions work on PRMs\"），审稿人很可能说 **\"I would have guessed this\"**——PRMs 有 scalar output、binary labels、verifiable math ground truth，当然比 open-ended clinical text 容易 intervene。反直觉的 finding 只有在 interventions 失败时才会出现，但 proposal 没有为此设计 narrative。(c) 对 NLP/CL 实践的直接影响有限——PRM debiasing 已有多种方法（含 fine-tuning），这里的贡献更偏 scientific understanding。\n\n3. **Related Work: 强** — \n   - 这是 proposal 最突出的维度。Related work 覆盖极为全面（经过调研验证，所有引用论文确认存在且描述准确）。差异化定位清晰——明确指出与 SteerRM（pretrained vs. from-scratch SAE）、CIRM（neuron-level vs. multi-granularity）、CRA（backdoor correction vs. debiasing）的区别。将 Orgad et al. 和 Lee et al. 的评估框架整合为 assessment criteria 也体现了良好的文献整合能力。\n   - 唯一小瑕疵: 缺少对 \"One Bias After Another\" 和 CRA 的更深入对比，以及对 generative PRM landscape（ThinkPRM, GenPRM）的讨论虽有提及但可以更好地论证\"为什么还要研究 discriminative PRMs\"。\n\n---\n\n【概率估计】: \n\n- **若投稿 CoRL 2026**: [0% - 3%] 中位 1%\n  - 理由: 完全不在会议 scope 内（零机器人内容），极大概率 desk reject。\n\n- **若投稿合适的 ML/NLP 顶会 (NeurIPS/ICML/ICLR)**: [18% - 30%] 中位 23%\n\n【估计理由】: \n（以下分析基于投稿到合适 venue 的假设）\n\nRelated Work 维度是强项，说明作者对领域理解深入。但 **Novelty 和 Significance 共同限制了上界**：\n\n- Novelty 受限于\"方法组合\"而非\"方法创新\"——每个组件都是现有工具的直接应用，核心 delta 是 comparison framework。ML 顶会对 empirical comparison papers 的 bar 很高，需要 comparison 本身产生 surprising insights 才能获得高 novelty 分。\n- Significance 受限于 Domain Amenability Hypothesis 的测试强度（N=1 vs. N=1）和核心发现的可预测性（\"PRMs 比 clinical LMs 更容易被 mechanistic intervention debiased\" 不 surprising）。\n- 概率未低于 18% 是因为：(a) 选题紧扣社区热点辩论，(b) related work 整合出色，(c) 如果实验中产生意外发现（如某粒度显著优于预期/某粒度完全失败），有可能提升到 \"surprising\" 的程度。\n\n**实际投稿 CoRL 的概率中位估计为 1%**，因为 venue mismatch 是根本性的。\n\n【主要风险】:\n1. **Venue 完全不匹配 CoRL**: 这是最直接的 rejection 原因——desk reject 概率极高。\n2. **核心假设的可证伪性不足**: Domain Amenability Hypothesis 用 N=1 正例 + N=1 反例（且反例来自他人论文）\"测试\"一个 4-condition 框架，审稿人会指出这不构成有效的假设检验，更像 post-hoc storytelling。即使转投合适 venue，这也是最可能触发 rejection 的 idea 层面弱点。\n```\n\n---\n\n**Sources:**\n- [Basu et al. - Interpretability without Actionability (arXiv:2603.18353)](https://arxiv.org/abs/2603.18353)\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795)](https://arxiv.org/abs/2603.12795)\n- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention (arXiv:2604.27495)](https://arxiv.org/abs/2604.27495)\n- [Orgad et al. - Interpretability Can Be Actionable (ICML 2026)](https://arxiv.org/abs/2605.11161)\n- [Lee et al. - Rigorous Interpretation Is a Form of Evaluation (arXiv:2605.05508)](https://arxiv.org/abs/2605.05508)\n- [CRA: Causal Reward Adjustment (arXiv:2508.04216)](https://arxiv.org/abs/2508.04216)\n- [Arad et al. - SAEs Are Good for Steering (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.519/)\n- [Wang et al. - Automatically Finding Reward Model Biases (arXiv:2602.15222)](https://arxiv.org/abs/2602.15222)\n- [Zhang et al. - Locate, Steer, and Improve (arXiv:2601.14004)](https://arxiv.org/abs/2601.14004)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct the evaluation. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n**关键发现：致命的 venue mismatch**\n\nCoRL (Conference on Robot Learning) 2026 明确要求论文 \"focus on a core robotics problem\"，鼓励 \"real-robot experiments or convincing evidence that simulation experiments are transferable to real robots\"。议题范围包括：robot foundation models, imitation learning for robotics, sim-to-real transfer, learned manipulation and locomotion 等。\n本 proposal 的内容是 NLP/MI 领域的 mechanistic interpretability for Process Reward Models（数学推理任务），与 robotics 零交集。这在 CoRL 属于 desk-reject 级别的 scope mismatch。\n\n以下是基于 idea 本身质量的调研（假设投稿至合适 venue 如 NeurIPS/ICML/ICLR）：\n\n- [Interpretability without Actionability] (arXiv:2603.18353, 2026): 本 proposal 的核心起点。Basu et al. 在 clinical triage LMs 上测试 4 种 MI 方法（含 SAE steering），发现 zero/negligible corrections，揭示 knowledge-action gap。本 proposal 试图用 PRM domain 作为对照来解释这一失败。\n- [SteerRM] (arXiv:2603.12795, 2026): 用 pretrained LlamaScope SAEs 做 RM debiasing，Hard-split +7.3 points。本 proposal 声称通过 from-scratch SAE + output-score filtering 改进此方法。\n- [CIRM] (arXiv:2604.27495, ACL 2026): Neuron-level causal mediation debiasing，edit <2% neurons 即匹配 70B 性能。本 proposal 将其作为 neuron-level baseline。\n- [Orgad et al.] (arXiv:2605.11161, ICML 2026): Position paper，提出 actionable interpretability 的 concreteness × validation 二维评估框架。本 proposal 采用其评估 criteria。\n- [Lee et al.] (arXiv:2605.05508, 2026): 主张 interpretability 作为 rigorous evaluation 需满足 falsifiability, reproducibility, predictivity。本 proposal 采用其 scientific rigor criteria。\n- [Tiwari et al.] (arXiv:2603.06621, 2026): 建立 PRM-BiasBench，发现 43% reward gains 来自 stylistic exploitation。本 proposal 的 PRM bias 问题来源。\n- [Zhang et al.] (arXiv:2601.14004, 2026): \"Locate, Steer, Improve\" survey，目前最全面的 actionable MI 分类体系。本 proposal 声称 instantiate 其 pipeline。\n- [One Bias After Another] (arXiv:2603.03291, 2026): Linear probes for mechanistic reward shaping，5 个 RMs。本 proposal 的 probe-level baseline。\n- [CRA] (arXiv:2508.04216, 2025): 在 PRM activations 上从头训练 SAE 做 backdoor correction。本 proposal 的 SAE 方法论直接来源。\n\n- 调研总结: 2025-2026 年，PRM debiasing 和 actionable MI 已成为高度活跃的研究领域。SteerRM (feature-level), CIRM (neuron-level), CRA (SAE from scratch), \"One Bias After Another\" (probe-level) 各自从不同粒度切入 PRM/RM debiasing。本 proposal 的核心定位是\"将现有方法整合到统一框架中比较\"——这是 empirical comparison/systematization 贡献，而非方法论突破。\n\n\n【Trivial Alternative 检验】:\n\n存在严重的 trivial alternative 威胁：\n\n1. **Domain Amenability Hypothesis 的检验**：Proposal 声称通过 PRM vs. clinical LM 的对比来 \"test\" 其假设，但这只是 N=2 的 domain 对比，且两个 domain 之间存在大量混杂因素（model architecture, training procedure, task formulation, data distribution, model scale 等均不同）。一个更简单的方式是：直接做 literature survey + meta-analysis，列出已有 MI intervention 的 success/failure cases，按 domain 属性分类——这无需任何 GPU，就能得出类似的（甚至更有说服力的）结论。\n\n2. **Multi-granularity comparison**：将 SteerRM、CIRM 等已有方法在相同 benchmark 上跑一遍并比较，本质上是 replication + comparison study。这有价值，但 novelty delta 有限——因为各方法的论文本身已经在相似 benchmark 上报告了结果（RM-Bench, ProcessBench 等）。\n\n3. **PRM debiasing 本身**：Fine-tuning on debiased data（proposal 自己列为 baseline）可能就是最简单有效的方案。如果 fine-tuning baseline 表现良好，整个 mechanistic intervention 的 comparative utility 就会被质疑。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链有多个未经验证的关键假设：\n\n1. **\"Domain properties 是 intervention success 的决定因素\" 这一假设缺乏控制**：Basu et al. 在 clinical LMs 上失败，但失败原因可能是 model-specific、task-specific 或 method-specific 的，而非 domain-specific 的。将两个完全不同实验的结果归因于 \"domain amenability\" 是一个 attribution leap，缺乏控制实验来排除混杂因素。真正的检验需要在同一模型、同一方法上切换 domain——这在实践中极难实现。\n\n2. **\"PRMs satisfy all four conditions\" 的论证是 post-hoc 且 circular**：作者先观察到 SteerRM/CIRM 在 PRM 上成功，然后提出 4 个 \"条件\"，然后论证 PRM 满足这 4 个条件。这不是 hypothesis testing，而是 post-hoc rationalization。\n\n3. **\"43% of reward gains from stylistic exploitation\" 是否意味着 fluency-reasoning 可分离**：这个数字来自 Tiwari et al. 的 adversarial optimization 实验，不一定意味着 PRM 内部有 clean 的 fluency vs. reasoning circuit separation。Polysemanticity 和 superposition 可能使分离比预期困难得多。\n\n4. **Self-repair 的假设 (H4) 是从非 PRM 文献外推的**：McGrath et al. 的 self-repair 研究是在 general LMs 上做的，直接外推到 discriminative PRMs 的 reward head 缺乏依据。\n\n\n【3 维度打分】:\n\n1. Novelty: 弱 — \n   核心贡献是 (a) Domain Amenability Hypothesis 和 (b) multi-granularity comparison。\n   \n   对于 (a)：这是一个 N=2 的 post-hoc domain 对比，且\"有 verifiable ground truth + constrained output 的 domain 更容易做 intervention\"接近常识。没有搜索到任何先前工作提出过完全相同的 formulation，但 Zhang et al. (2026) 的 survey 已经讨论了 \"success requires sparse and decomposable mechanisms\"——这本质上是相同洞察的不同表述。\n   \n   对于 (b)：SteerRM, CIRM, CRA, \"One Bias After Another\" 已分别在 feature/neuron/probe/SAE 粒度上做了 PRM/RM debiasing。本 proposal 的增量是\"放在一起比较\"——这是 empirical systematization，不是 methodological novelty。没有提出任何新的 intervention 方法、新的 analysis technique、或新的 model architecture。\n   \n   剔除 surface differences 后，真正的 novelty delta 是 \"unified comparison + domain amenability framing\"——这更像是 survey/benchmark paper 的贡献，而非 top venue main conference 的 idea 级别。\n\n2. Significance: 中 — \n   \"When do mechanistic interventions work?\" 是一个 timely 且 important 的问题，Basu et al. 和 Orgad et al. 的工作证明了这个问题的 urgency。PRM debiasing 也有实际应用价值（RLHF pipeline 的 robustness）。\n   \n   但问题在于：(a) 即使实验成功（PRMs 上 intervention 有效），审稿人很可能说 \"I would have guessed this\"——因为 PRM 的 constrained output + verifiable ground truth 本身就预示着 intervention 应该更容易成功；(b) 如果实验失败（PRMs 上也不行），那结论是 \"mechanistic interventions fundamentally limited\"——这虽然有价值但属于 negative result；(c) 对领域的推广性有限——从 N=2 domain 对比得出的 \"domain amenability\" 结论，审稿人很难被说服这是一个 general principle。\n\n3. Related Work: 强 — \n   Related work 覆盖非常全面，涵盖了 2025-2026 几乎所有相关工作：actionability debate (Basu et al., Orgad et al., Lee et al.), PRM bias (Tiwari et al., Wang et al.), intervention methods (SteerRM, CIRM, CRA, \"One Bias After Another\"), SAE methodology (Arad et al., CRA vs. SteerRM), circuit analysis (RelP, CLT-Forge), self-repair (McGrath et al.)。差异化定位也比较清晰。这是 proposal 最强的维度。\n\n\n【概率估计】: 0% - 3%，中位 1%\n\n【估计理由】: \n**致命问题是 venue mismatch。** CoRL 2026 明确要求 \"focus on a core robotics problem\"，本 proposal 关于 NLP mechanistic interpretability for math PRMs 的内容与 robotics 完全无关，极大概率 desk-reject。这一条直接将概率压到接近 0%。\n\n即使假设投到合适的 venue（NeurIPS/ICML/ICLR），idea 质量的概率估计约 20-28%（中位 ~24%）：\n- Novelty 弱是主要限制因素：核心贡献是 existing methods 的 comparison + post-hoc domain hypothesis，缺乏 methodological innovation\n- Significance 受限于 \"I would have guessed this\" 风险\n- 极好的 Related Work 覆盖提供了 floor support，但不能弥补 idea 内核的薄弱\n- 280 H100-hours 的投入产出比堪忧——花大量 compute 做 comparison study\n\n【主要风险】: \n1. **致命风险 — 完全的 venue mismatch**: CoRL 是 robotics 会议，本 proposal 是纯 NLP/MI 工作，desk-reject 概率极高。建议改投 NeurIPS 2026, ICML 2026, ICLR 2027, 或 EMNLP 2026。\n2. **Idea 层面风险 — Novelty 不足**: 核心贡献是 empirical comparison + post-hoc domain hypothesis，没有新方法/新 technique/新 insight。审稿人可能评价为 \"well-executed comparison study but limited novelty for main conference\"。Domain Amenability Hypothesis 的 N=2 对比 + 大量混杂因素使其作为 \"hypothesis test\" 的说服力很弱。\n```\n\nSources:\n- [Interpretability without Actionability (Basu et al., 2026)](https://arxiv.org/abs/2603.18353)\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)\n- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/html/2604.27495)\n- [Position: Interpretability Can Be Actionable (Orgad et al., ICML 2026)](https://arxiv.org/abs/2605.11161)\n- [Locate, Steer, and Improve Survey (Zhang et al., 2026)](https://arxiv.org/pdf/2601.14004)\n- [Reward Under Attack: PRM Hackability (Tiwari et al., 2026)](https://arxiv.org/abs/2603.06621)\n- [One Bias After Another (2026)](https://arxiv.org/pdf/2603.03291)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)\n- [ICML 2026 Poster: Interpretability Can Be Actionable](https://icml.cc/virtual/2026/poster/67043)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models\n\n## Description\nWhen do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.\n\n## Core Problem\nThe mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).\n\n## Opportunity\nThe interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.\n\n## Related Work / Landscape\nTHE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.\n\nACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.\n\nPRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.\n\nINTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.\n\nSPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.\n\nSAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.\n\nCIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.\n\nSELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.\n\nGENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.\n\n## Approach\nWe conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.\n\n**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**\n\n*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.\n\n*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.\n\n*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.\n\n**Phase 2: Multi-Method Causal Circuit Tracing.**\n\nTier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).\n\nTier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.\n\n**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.\n\nComponents are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.\n\n**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:\n\n(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.\n\n(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.\n\n**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:\n\n**Core granularities (all 3 PRMs × 3 core benchmarks):**\n(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);\n(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;\n(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.\n\n**Extension granularities (single most informative PRM × 3 core benchmarks):**\n(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;\n(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.\n\nWe benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.\n\n**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:\n\n*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?\n\n*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.\n\nThis produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.\n\n**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.\n\n**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.\n\n## Inspiration\nPrimary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing\n\n## Key References\n- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)\n- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)\n- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)\n- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)\n- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)\n- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)\n- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)\n- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)\n- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)\n- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)\n- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)\n- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)\n- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)\n- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)\n- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)\n- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)\n- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)\n- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)\n- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)\n- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)\n- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)\n- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)\n- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)\n- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)\n- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)\n- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}\n- **human_in_loop**: {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}\n- **auto_research**: {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T19:20:40.417Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T19:20:40.417Z",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T19:20:40.428Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

==========================================================================
⚠️ 关键前置问题：严重的投稿目标会议错位
==========================================================================

在进入 idea 质量评估之前，必须指出一个致命问题：
本 proposal 关于 NLP/ML 领域的 Process Reward Model 机制可解释性，
而 CoRL (Conference on Robot Learning) 的核心主题是机器人学习：
仿真到真实迁移、机器人操纵/运动/导航/驾驶、机器人感知、
机器人强化学习等。CoRL 2026 (Austin, TX, Nov 10-12) 的 Call for Papers
明确要求 "real-robot experiments or convincing evidence that simulation
experiments are transferable to real robots"。

本 proposal 与机器人学习领域零交集——无机器人实验、无机器人任务、
无 embodied 组件。如果直接投稿 CoRL 2026 主会，大概率被 desk reject。

适合的目标会议：ICML / NeurIPS / ICLR (ML track) 或 ACL / EMNLP (NLP track)。

以下评估假设投稿目标为一个合适的 ML/NLP 顶会（如 NeurIPS 2026），
以便下游 agent 能在正确语境下优化 proposal。

==========================================================================

【领域调研】:

- [Basu et al., arXiv:2603.18353] (March 2026): "Interpretability without 
  Actionability" — 在临床分诊 LM 上测试四种机制可解释性干预方法
  （含 SAE steering、activation patching），发现均无法有效纠正输出错误。
  线性探针达 98.2% AUROC 但模型输出灵敏度仅 45.1%，存在 53pp 的
  knowledge-action gap。已验证存在，是本 proposal 的核心对比点。

- [SteerRM, arXiv:2603.12795] (March 2026): 北大团队提出首个
  training-free SAE-based RM 去偏方法。使用预训练 LlamaScope SAE，
  在 RM-Bench Hard split 上平均提升 7.3 points。发现 format-related
  features 集中在浅层且跨模型迁移。已经实现了 feature-level 干预。

- [CIRM / Shinoda et al., arXiv:2604.27495] (April 2026, ACL 2026): 
  NTT 团队提出 neuron-level 因果中介分析去偏，编辑 <2% neurons 
  即可匹配 70B RM 性能。已经实现了 neuron-level 干预。

- [Orgad et al., arXiv:2605.11161] (ICML 2026 Position Paper): 
  提出可解释性应以 actionability 为评估标准，定义 concreteness 
  和 validation 两个维度。本 proposal 采用其评估框架但并非核心创新。

- [Lee et al., arXiv:2605.05508] (May 2026): 
  提出可解释性作为严格评估的三个科学标准（可证伪性、可复现性、
  预测性），提供互补诊断框架。

- [Zhang et al., arXiv:2601.14004] (Jan 2026): "Locate, Steer, Improve" 
  综述，提供 actionable MI 的最全面分类法。本 proposal 实例化其 pipeline。

- [CRA, arXiv:2508.04216] (2025): 在 PRM 激活上从头训练 SAE 用于
  后门纠正，本 proposal 的 SAE 方法论直接沿用此工作。

- [Arad et al., arXiv:2505.20063] (EMNLP 2025): 区分 output features
  和 input features 可带来 2-3× 改进。本 proposal 采用其过滤方法。

- 调研总结: 这个领域在 2026 年初极为活跃。PRM 去偏已有 feature-level
  (SteerRM)、neuron-level (CIRM)、probe-level (One Bias After Another) 
  等多种粒度的独立工作。"可解释性是否 actionable"的辩论也有了正反两方
  的 position papers。本 proposal 试图在已有拼图上做"统一比较框架+
  domain amenability 假说"，但核心方法论组件均来自已有工作。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁，分两个层面：

(1) 对于 "Domain Amenability Hypothesis"：这个假说本质上在说"当任务
    有明确输出语义、受限输出结构、可验证 ground truth、可独立测试
    specificity 时，机制干预更容易成功"。这近乎同义反复——"当你能
    清晰定义成功、精确测量效果、独立检验副作用时，干预更可能被判定
    为成功"。一个更 trivial 的表述是："机制干预在更简单、更可度量的
    任务上效果更好"。审稿人很可能认为这不是一个需要实验验证的
    hypothesis，而是一个 obvious observation。

(2) 对于 PRM 去偏本身：fine-tuning on debiased data（proposal 自己
    列为 baseline）可能以更低成本达到类似或更好效果。Factored CRL
    (ICML 2026) 已经在训练时解决了这个问题。本 proposal 的增量价值
    在于"理解 why/when 干预 work"，但如果假说本身是 trivial 的，
    这个增量价值就大打折扣。


【前提假设检验】:

核心 claim 的逻辑链有以下未经验证的环节：

(1) N=2 归纳问题：整个 Domain Amenability Hypothesis 的"验证"建立在
    两个数据点上——PRM（满足四条件，干预成功）vs. 临床 LM（不满足
    四条件，干预失败）。但这两个域之间的差异远不止这四个条件（模型
    架构、训练数据、任务类型、模型规模、领域知识等全部不同）。无法
    排除混淆因素，无法证明是这四个条件而非其他因素导致了成功/失败
    的差异。这不是"验证假说"，而是"post-hoc rationalization"。

(2) 四个条件的选择缺乏理论基础：为什么是这四个条件而非其他？为什么
    不是"输出维度低"、"任务复杂度低"、"偏差是线性可分的"等？
    这四个条件看起来是从 PRM 的特征反推出来的（PRM 有什么特点 →
    这些特点就是成功的条件），存在严重的 overfitting to the 
    observation 风险。

(3) "43% of reward gains from stylistic exploitation" 这个数字来自
    Tiwari et al.，但这是在特定 PRM 和特定攻击设置下的结果，
    能否推广到本 proposal 使用的 Qwen2.5-Math-PRM 和 
    Math-Shepherd-Mistral-7B-PRM 是未经验证的。

(4) 对 Basu et al. 失败的归因：Basu et al. 的失败可能有多种原因
    （SAE 质量差、steering 方向选择不当、临床任务本身更难等），
    proposal 将其归因于"domain 不满足四条件"是一个未经验证的
    归因。Basu et al. 自己的分析也指向了更具体的技术原因。


【3 维度打分】:

1. Novelty: 弱 — 
   核心贡献有两个层面：(a) Domain Amenability Hypothesis 和 
   (b) multi-granularity comparison。
   
   对于 (a)：这个假说本身接近同义反复（见 Trivial Alternative 检验），
   且仅基于 N=2 的 post-hoc 对比，缺乏理论推导。这不构成 strong 
   novelty。
   
   对于 (b)：这是一个 systematic empirical comparison，但比较的
   对象——feature-level (SteerRM, 2603.12795)、neuron-level 
   (CIRM, 2604.27495)、circuit-level (activation patching) ——
   均为已有方法的直接应用或微调。唯一的方法论增量是将 Arad et al.
   的 output-score filtering 与 CRA 的 from-scratch SAE 结合，
   但这是 straightforward engineering integration。
   
   与最相关工作的 delta：SteerRM 已做 feature-level；CIRM 已做
   neuron-level；CRA 已做 PRM-specific SAE training。本 proposal
   的核心 novelty 是"把它们放在一起比较"+ 一个薄弱的 framing 假说。
   这更接近 survey + benchmark 而非 research contribution。

2. Significance: 中 — 
   "when do mechanistic interventions succeed" 是 MI 社区当前的
   核心问题之一，Basu et al. 和 Orgad et al. 分别从负面和正面
   推动了这个讨论。这个问题的重要性毋庸置疑。
   
   但本 proposal 对这个问题的回答质量堪忧：N=2 的 domain 对比
   不可能给出有说服力的答案。即使 PRM 干预成功，审稿人仍然无法
   判断是因为 Domain Amenability Hypothesis 的四个条件还是其他
   原因。结论的可推广性极低。
   
   PRM 去偏的实际应用价值存在，但 discriminative PRM 正在被
   generative PRM (ThinkPRM, GenPRM) 替代，这削弱了 practical 
   significance。
   
   对领域的影响：如果结果 positive，贡献的是"又一个 MI 干预成功
   的 case study"，但 SteerRM 和 CIRM 已经提供了类似证据。
   如果结果 negative，那更有意思（但 proposal 的设计倾向于 
   positive result）。

3. Related Work: 强 — 
   Related work 覆盖极为全面，涵盖了 actionability debate 双方
   (Basu et al., Orgad et al.)、所有主要 intervention 粒度
   (SteerRM, CIRM, CRA, One Bias After Another)、评估框架
   (Lee et al.)、分类法 (Zhang et al.)、电路分析工具 
   (RelP, CLT-Forge)、self-repair (McGrath et al.) 等。
   差异化定位也算清晰——"统一比较框架"的定位在文献中确实空白。
   引用的论文经核实均真实存在且描述准确。


【概率估计】: [15% - 25%] 中位 20%

【估计理由】: 
投稿 CoRL 的话概率接近 0%（完全 off-topic，会被 desk reject）。

即使投稿合适的 ML/NLP 顶会（NeurIPS/ICML/ACL），idea 质量也
处于 15-25% 区间：

- Novelty 是核心瓶颈。Domain Amenability Hypothesis 近乎同义反复
  且 N=2 归纳不具说服力；multi-granularity comparison 是 
  straightforward 的已有方法组合。审稿人大概率会评价为 "well-executed
  but incremental"。

- Significance 被两个因素削弱：(a) discriminative PRM 正被 generative 
  PRM 替代，降低了实际应用价值；(b) 对核心问题 "when do MI interventions 
  succeed" 的回答因 N=2 设计而不具说服力。

- Related work 的强项不足以弥补 novelty 的弱项——在顶会审稿中，
  idea 新颖性通常是决定性因素。

- 形式完善度很高（详细的实验 plan、完整的 resource estimate、
  双 outcome 设计），但这是执行层面的优势，不改变 idea 内核。

上界 25% 受限于 Novelty 维度——即使实验完美执行，核心 claim 
的 intellectual contribution 仍然薄弱。

【主要风险】: 
1. Domain Amenability Hypothesis 被审稿人判定为 tautological/obvious，
   且 N=2 对比被认为不构成 hypothesis testing（这是最可能的拒稿理由）
2. "统一比较已有方法"的定位被归类为 benchmark/survey paper 而非
   research paper，不符合顶会主会对 novelty 的要求
```

**补充说明给下游 agent：**

如果要进入迭代优化，我建议重点关注两个方向：
1. **必须解决 venue 问题**——如果坚持投 CoRL，需要彻底重新设计 proposal 使其与机器人学习相关（例如：将机制可解释性应用于 robot reward models / robot policy learning），否则投稿无意义。
2. **如果转投 NLP/ML 顶会**，核心问题是 Domain Amenability Hypothesis 太弱——需要要么 (a) 增加更多对比域使假说检验更有说服力，要么 (b) 放弃假说包装、转而强化 multi-granularity comparison 的方法论贡献和实用价值。

Sources:
- [Interpretability without Actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)
- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495)
- [Position: Interpretability Can Be Actionable (Orgad et al.)](https://arxiv.org/abs/2605.11161)
- [Rigorous Interpretation Is a Form of Evaluation (Lee et al.)](https://arxiv.org/abs/2605.05508)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to provide my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【⚠️ 致命前置问题：投稿目标 venue 严重不匹配】

本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。CoRL 2026 的 Call for Papers 明确要求 submissions "focus on a core robotics problem" 并鼓励 "real-robot experiments or convincing evidence that simulation experiments are transferable to real robots"。其 topics 包括 robot manipulation、navigation、locomotion、driving 等。

本 proposal 的内容是对 **数学推理领域的 Process Reward Models** 进行 mechanistic interpretability 分析与多粒度干预比较。全文无任何机器人相关内容。这不是"scope 偏边缘"的问题，而是**完全不在会议范围内**，大概率在 desk review 阶段即被拒。

该 proposal 的自然投稿目标应为 NeurIPS、ICML、ICLR 或 ACL/EMNLP。以下评估将**假设投稿到合适的 ML/NLP venue**来评价 idea 质量本身，但最终概率估计会反映 CoRL 的实际接收可能性。

---

【领域调研】:

- **Basu et al. "Interpretability without Actionability" (arXiv:2603.18353, March 2026)**: 在临床分诊 LM 上测试 4 种 mechanistic intervention（含 SAE steering、activation patching），发现 knowledge-action gap 持续存在——linear probes 可达 98.2% AUROC 但 output sensitivity 仅 45.1%，最好的 intervention 仅纠正 24% 的错误。这是本 proposal 的核心动机论文。确认真实存在，描述准确。

- **SteerRM (arXiv:2603.12795, March 2026)**: 使用预训练 LlamaScope SAE 对 RM 进行 feature-level debiasing，RM-Bench Hard split 提升 7.3 分。限制：仅适用于有预训练 SAE 的架构，有效分析限于 layers 0-9。确认真实存在，描述准确。

- **CIRM / Shinoda et al. (arXiv:2604.27495, ACL 2026)**: 使用 Spearman correlation 做 bias-specific neuron identification + causal mediation analysis，编辑 <2% neurons 在 general RMs 上达到 70B 级性能。确认真实存在，描述准确。

- **CRA (arXiv:2508.04216, 2025)**: 从头在 PRM activations 上训练 SAE，通过 backdoor adjustment 修正 reward hacking。确认真实存在，proposal 的描述准确。

- **Arad et al. "SAEs Are Good for Steering" (EMNLP 2025)**: 区分 input features vs. output features，output-score filtering 带来 2-3x steering 改善。确认真实存在，描述准确。

- **Orgad et al. "Interpretability Can Be Actionable" (ICML 2026, position paper)**: 提出 concreteness × validation 双维评估框架。确认真实存在，描述准确。

- **Lee et al. "Rigorous Interpretation Is a Form of Evaluation" (arXiv:2605.05508, May 2026)**: 提出 falsifiability / reproducibility / predictivity 三标准。确认真实存在，描述准确。

- **Zhang et al. "Locate, Steer, and Improve" (arXiv:2601.14004, Jan 2026)**: 最全面的 actionable MI survey，分类 localization 和 intervention 方法。确认真实存在。

- **Wang et al. "Automatically Finding Reward Model Biases" (arXiv:2602.15222, Feb 2026)**: 自动化 evolutionary bias discovery pipeline。确认真实存在，描述准确。

- **"One Bias After Another" (arXiv:2603.03291, 2026)**: 使用 linear probes 做 mechanistic reward shaping。确认存在。

- **调研未发现的关键空白**: 搜索 "domain amenability" + mechanistic interpretability 未找到任何现有工作使用过这一术语或框架。该 framing 确实是 proposal 自己的贡献。但也未找到任何工作系统比较 feature / neuron / circuit 三种粒度的 MI intervention 在同一 domain 上的效果。

- **调研总结**: PRM debiasing 在 2025-2026 是一个快速增长的小领域，已有 feature-level (SteerRM)、neuron-level (CIRM)、probe-level (One Bias After Another)、SAE-from-scratch (CRA) 等独立工作。actionability debate (Basu vs. others) 是 2026 MI 社区的热点话题。但**目前没有工作将这些方法在统一框架下比较**，也**没有工作显式提出和测试"什么 domain 条件下 MI intervention 更可能成功"的假设**。

---

【Trivial Alternative 检验】:

存在明确的 trivial alternative 威胁：

1. **Fine-tuning on debiased data**: 如果目标是 PRM debiasing，最简单的方法是在去偏数据上微调 PRM。Proposal 虽然将此列为 baseline，但没有论证为什么 mechanistic approach 应当**根本上优于**这一方法。如果 fine-tuning 在所有 benchmark 上都能匹配或超过所有 mechanistic interventions，那整个 multi-granularity comparison 的实用价值就大打折扣——即使它仍有 scientific understanding 的价值。

2. **Linear probes + simple editing**: "One Bias After Another" 已经用简单的 linear probes 做 mechanistic reward shaping。如果 linear probes 就够用，那 SAE + circuit tracing 的复杂 pipeline 的增量价值在哪？

**增量价值定位**: Proposal 的真正价值不在"PRM debiasing 的实用效果"（这可能被 trivial alternatives 达到），而在**理解性问题**——"WHEN 和 WHY 机制级别的 intervention 能成功"。但这意味着 proposal 的核心贡献是 empirical understanding，不是 practical improvement，这在顶会的 novelty 评估中是一个较弱的位置。

---

【前提假设检验】:

核心 claim 的逻辑链中有几个关键未验证假设：

1. **Domain Amenability Hypothesis 的可证伪性极弱**: 用 N=1 正例（PRMs）和 N=1 反例（Basu et al. 的 clinical LMs）来"测试"一个 4-condition 假设，统计上几乎不可能得出有意义的结论。这更接近 post-hoc rationalization 而非 hypothesis testing。4 个条件（well-defined output semantics, constrained output structure, verifiable ground truth, independently testable specificity）是在已知 PRMs 的特性后定制的，存在严重的 overfitting-to-the-example 风险。

2. **跨 domain 对比的 confound 太多**: PRMs vs. clinical LMs 的差异不仅仅是这 4 个条件——模型架构不同、训练数据不同、任务复杂度不同、研究者不同。将 intervention 成败归因于 domain conditions 而非其他 confounders 是一个很强的假设。

3. **"If interventions succeed, this provides positive evidence for the hypothesis"**: 这是一个单向验证。如果 PRM interventions 成功，我们无法区分是因为"domain amenability"还是因为"这些特定的 PRMs 恰好容易被 intervention"。只有当 proposal 在多个满足/不满足各条件的 domain 上系统测试时，假设才有说服力。

4. **43% stylistic exploitation 的普遍性**: Tiwari et al. 的发现是否在 Qwen2.5-Math-PRM 和 Math-Shepherd-Mistral 上同样成立？Proposal 假设了这一点但未验证。

---

【3 维度打分】:

1. **Novelty: 中** — 
   - 积极面: "Domain Amenability Hypothesis" 作为一个 framing 是新的（搜索确认无先例），将 feature/neuron/circuit 三粒度在统一框架下比较也是首次。结合 Orgad et al. + Lee et al. 的评估标准构建 granularity-by-criterion matrix 是有组织创新的。
   - 限制面: 每个组成部分（SAE on PRMs → CRA 已做; feature-level debiasing → SteerRM 已做; neuron-level → CIRM 已做; circuit tracing → RelP/CLT 已有工具; output-score filtering → Arad et al. 已提出）都是现有方法的直接应用。核心 novelty 是 **comparison + framing**，不是 **method or discovery**。这在 ML 顶会中属于 "solid empirical study" 而非 "conceptual breakthrough"，novelty 评价通常会落在 "moderate" 区间。
   - 关键参考: SteerRM (2603.12795) 已做 feature-level PRM debiasing; CIRM (2604.27495) 已做 neuron-level; CRA (2508.04216) 已训练 SAE on PRM activations。本 proposal 的 delta 是将这些放在一起比较。

2. **Significance: 中** — 
   - 积极面: "When do mechanistic interventions succeed?" 是 MI 社区在 2026 的核心争论之一（Basu et al. vs. Orgad et al.），选题切中时代痛点。如果能给出清晰答案，对领域有真实推进价值。
   - 限制面: (a) Domain Amenability Hypothesis 在本 proposal 中的测试强度不足（N=1 vs. N=1），即使实验全部成功，审稿人仍会质疑"你证明了 PRM 上能 work，但这能 generalize 到你假设的 4 个条件吗？" (b) 核心发现如果是 positive（"interventions work on PRMs"），审稿人很可能说 **"I would have guessed this"**——PRMs 有 scalar output、binary labels、verifiable math ground truth，当然比 open-ended clinical text 容易 intervene。反直觉的 finding 只有在 interventions 失败时才会出现，但 proposal 没有为此设计 narrative。(c) 对 NLP/CL 实践的直接影响有限——PRM debiasing 已有多种方法（含 fine-tuning），这里的贡献更偏 scientific understanding。

3. **Related Work: 强** — 
   - 这是 proposal 最突出的维度。Related work 覆盖极为全面（经过调研验证，所有引用论文确认存在且描述准确）。差异化定位清晰——明确指出与 SteerRM（pretrained vs. from-scratch SAE）、CIRM（neuron-level vs. multi-granularity）、CRA（backdoor correction vs. debiasing）的区别。将 Orgad et al. 和 Lee et al. 的评估框架整合为 assessment criteria 也体现了良好的文献整合能力。
   - 唯一小瑕疵: 缺少对 "One Bias After Another" 和 CRA 的更深入对比，以及对 generative PRM landscape（ThinkPRM, GenPRM）的讨论虽有提及但可以更好地论证"为什么还要研究 discriminative PRMs"。

---

【概率估计】: 

- **若投稿 CoRL 2026**: [0% - 3%] 中位 1%
  - 理由: 完全不在会议 scope 内（零机器人内容），极大概率 desk reject。

- **若投稿合适的 ML/NLP 顶会 (NeurIPS/ICML/ICLR)**: [18% - 30%] 中位 23%

【估计理由】: 
（以下分析基于投稿到合适 venue 的假设）

Related Work 维度是强项，说明作者对领域理解深入。但 **Novelty 和 Significance 共同限制了上界**：

- Novelty 受限于"方法组合"而非"方法创新"——每个组件都是现有工具的直接应用，核心 delta 是 comparison framework。ML 顶会对 empirical comparison papers 的 bar 很高，需要 comparison 本身产生 surprising insights 才能获得高 novelty 分。
- Significance 受限于 Domain Amenability Hypothesis 的测试强度（N=1 vs. N=1）和核心发现的可预测性（"PRMs 比 clinical LMs 更容易被 mechanistic intervention debiased" 不 surprising）。
- 概率未低于 18% 是因为：(a) 选题紧扣社区热点辩论，(b) related work 整合出色，(c) 如果实验中产生意外发现（如某粒度显著优于预期/某粒度完全失败），有可能提升到 "surprising" 的程度。

**实际投稿 CoRL 的概率中位估计为 1%**，因为 venue mismatch 是根本性的。

【主要风险】:
1. **Venue 完全不匹配 CoRL**: 这是最直接的 rejection 原因——desk reject 概率极高。
2. **核心假设的可证伪性不足**: Domain Amenability Hypothesis 用 N=1 正例 + N=1 反例（且反例来自他人论文）"测试"一个 4-condition 框架，审稿人会指出这不构成有效的假设检验，更像 post-hoc storytelling。即使转投合适 venue，这也是最可能触发 rejection 的 idea 层面弱点。
```

---

**Sources:**
- [Basu et al. - Interpretability without Actionability (arXiv:2603.18353)](https://arxiv.org/abs/2603.18353)
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795)](https://arxiv.org/abs/2603.12795)
- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention (arXiv:2604.27495)](https://arxiv.org/abs/2604.27495)
- [Orgad et al. - Interpretability Can Be Actionable (ICML 2026)](https://arxiv.org/abs/2605.11161)
- [Lee et al. - Rigorous Interpretation Is a Form of Evaluation (arXiv:2605.05508)](https://arxiv.org/abs/2605.05508)
- [CRA: Causal Reward Adjustment (arXiv:2508.04216)](https://arxiv.org/abs/2508.04216)
- [Arad et al. - SAEs Are Good for Steering (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.519/)
- [Wang et al. - Automatically Finding Reward Model Biases (arXiv:2602.15222)](https://arxiv.org/abs/2602.15222)
- [Zhang et al. - Locate, Steer, and Improve (arXiv:2601.14004)](https://arxiv.org/abs/2601.14004)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct the evaluation. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:

**关键发现：致命的 venue mismatch**

CoRL (Conference on Robot Learning) 2026 明确要求论文 "focus on a core robotics problem"，鼓励 "real-robot experiments or convincing evidence that simulation experiments are transferable to real robots"。议题范围包括：robot foundation models, imitation learning for robotics, sim-to-real transfer, learned manipulation and locomotion 等。
本 proposal 的内容是 NLP/MI 领域的 mechanistic interpretability for Process Reward Models（数学推理任务），与 robotics 零交集。这在 CoRL 属于 desk-reject 级别的 scope mismatch。

以下是基于 idea 本身质量的调研（假设投稿至合适 venue 如 NeurIPS/ICML/ICLR）：

- [Interpretability without Actionability] (arXiv:2603.18353, 2026): 本 proposal 的核心起点。Basu et al. 在 clinical triage LMs 上测试 4 种 MI 方法（含 SAE steering），发现 zero/negligible corrections，揭示 knowledge-action gap。本 proposal 试图用 PRM domain 作为对照来解释这一失败。
- [SteerRM] (arXiv:2603.12795, 2026): 用 pretrained LlamaScope SAEs 做 RM debiasing，Hard-split +7.3 points。本 proposal 声称通过 from-scratch SAE + output-score filtering 改进此方法。
- [CIRM] (arXiv:2604.27495, ACL 2026): Neuron-level causal mediation debiasing，edit <2% neurons 即匹配 70B 性能。本 proposal 将其作为 neuron-level baseline。
- [Orgad et al.] (arXiv:2605.11161, ICML 2026): Position paper，提出 actionable interpretability 的 concreteness × validation 二维评估框架。本 proposal 采用其评估 criteria。
- [Lee et al.] (arXiv:2605.05508, 2026): 主张 interpretability 作为 rigorous evaluation 需满足 falsifiability, reproducibility, predictivity。本 proposal 采用其 scientific rigor criteria。
- [Tiwari et al.] (arXiv:2603.06621, 2026): 建立 PRM-BiasBench，发现 43% reward gains 来自 stylistic exploitation。本 proposal 的 PRM bias 问题来源。
- [Zhang et al.] (arXiv:2601.14004, 2026): "Locate, Steer, Improve" survey，目前最全面的 actionable MI 分类体系。本 proposal 声称 instantiate 其 pipeline。
- [One Bias After Another] (arXiv:2603.03291, 2026): Linear probes for mechanistic reward shaping，5 个 RMs。本 proposal 的 probe-level baseline。
- [CRA] (arXiv:2508.04216, 2025): 在 PRM activations 上从头训练 SAE 做 backdoor correction。本 proposal 的 SAE 方法论直接来源。

- 调研总结: 2025-2026 年，PRM debiasing 和 actionable MI 已成为高度活跃的研究领域。SteerRM (feature-level), CIRM (neuron-level), CRA (SAE from scratch), "One Bias After Another" (probe-level) 各自从不同粒度切入 PRM/RM debiasing。本 proposal 的核心定位是"将现有方法整合到统一框架中比较"——这是 empirical comparison/systematization 贡献，而非方法论突破。


【Trivial Alternative 检验】:

存在严重的 trivial alternative 威胁：

1. **Domain Amenability Hypothesis 的检验**：Proposal 声称通过 PRM vs. clinical LM 的对比来 "test" 其假设，但这只是 N=2 的 domain 对比，且两个 domain 之间存在大量混杂因素（model architecture, training procedure, task formulation, data distribution, model scale 等均不同）。一个更简单的方式是：直接做 literature survey + meta-analysis，列出已有 MI intervention 的 success/failure cases，按 domain 属性分类——这无需任何 GPU，就能得出类似的（甚至更有说服力的）结论。

2. **Multi-granularity comparison**：将 SteerRM、CIRM 等已有方法在相同 benchmark 上跑一遍并比较，本质上是 replication + comparison study。这有价值，但 novelty delta 有限——因为各方法的论文本身已经在相似 benchmark 上报告了结果（RM-Bench, ProcessBench 等）。

3. **PRM debiasing 本身**：Fine-tuning on debiased data（proposal 自己列为 baseline）可能就是最简单有效的方案。如果 fine-tuning baseline 表现良好，整个 mechanistic intervention 的 comparative utility 就会被质疑。


【前提假设检验】:

核心 claim 的逻辑链有多个未经验证的关键假设：

1. **"Domain properties 是 intervention success 的决定因素" 这一假设缺乏控制**：Basu et al. 在 clinical LMs 上失败，但失败原因可能是 model-specific、task-specific 或 method-specific 的，而非 domain-specific 的。将两个完全不同实验的结果归因于 "domain amenability" 是一个 attribution leap，缺乏控制实验来排除混杂因素。真正的检验需要在同一模型、同一方法上切换 domain——这在实践中极难实现。

2. **"PRMs satisfy all four conditions" 的论证是 post-hoc 且 circular**：作者先观察到 SteerRM/CIRM 在 PRM 上成功，然后提出 4 个 "条件"，然后论证 PRM 满足这 4 个条件。这不是 hypothesis testing，而是 post-hoc rationalization。

3. **"43% of reward gains from stylistic exploitation" 是否意味着 fluency-reasoning 可分离**：这个数字来自 Tiwari et al. 的 adversarial optimization 实验，不一定意味着 PRM 内部有 clean 的 fluency vs. reasoning circuit separation。Polysemanticity 和 superposition 可能使分离比预期困难得多。

4. **Self-repair 的假设 (H4) 是从非 PRM 文献外推的**：McGrath et al. 的 self-repair 研究是在 general LMs 上做的，直接外推到 discriminative PRMs 的 reward head 缺乏依据。


【3 维度打分】:

1. Novelty: 弱 — 
   核心贡献是 (a) Domain Amenability Hypothesis 和 (b) multi-granularity comparison。
   
   对于 (a)：这是一个 N=2 的 post-hoc domain 对比，且"有 verifiable ground truth + constrained output 的 domain 更容易做 intervention"接近常识。没有搜索到任何先前工作提出过完全相同的 formulation，但 Zhang et al. (2026) 的 survey 已经讨论了 "success requires sparse and decomposable mechanisms"——这本质上是相同洞察的不同表述。
   
   对于 (b)：SteerRM, CIRM, CRA, "One Bias After Another" 已分别在 feature/neuron/probe/SAE 粒度上做了 PRM/RM debiasing。本 proposal 的增量是"放在一起比较"——这是 empirical systematization，不是 methodological novelty。没有提出任何新的 intervention 方法、新的 analysis technique、或新的 model architecture。
   
   剔除 surface differences 后，真正的 novelty delta 是 "unified comparison + domain amenability framing"——这更像是 survey/benchmark paper 的贡献，而非 top venue main conference 的 idea 级别。

2. Significance: 中 — 
   "When do mechanistic interventions work?" 是一个 timely 且 important 的问题，Basu et al. 和 Orgad et al. 的工作证明了这个问题的 urgency。PRM debiasing 也有实际应用价值（RLHF pipeline 的 robustness）。
   
   但问题在于：(a) 即使实验成功（PRMs 上 intervention 有效），审稿人很可能说 "I would have guessed this"——因为 PRM 的 constrained output + verifiable ground truth 本身就预示着 intervention 应该更容易成功；(b) 如果实验失败（PRMs 上也不行），那结论是 "mechanistic interventions fundamentally limited"——这虽然有价值但属于 negative result；(c) 对领域的推广性有限——从 N=2 domain 对比得出的 "domain amenability" 结论，审稿人很难被说服这是一个 general principle。

3. Related Work: 强 — 
   Related work 覆盖非常全面，涵盖了 2025-2026 几乎所有相关工作：actionability debate (Basu et al., Orgad et al., Lee et al.), PRM bias (Tiwari et al., Wang et al.), intervention methods (SteerRM, CIRM, CRA, "One Bias After Another"), SAE methodology (Arad et al., CRA vs. SteerRM), circuit analysis (RelP, CLT-Forge), self-repair (McGrath et al.)。差异化定位也比较清晰。这是 proposal 最强的维度。


【概率估计】: 0% - 3%，中位 1%

【估计理由】: 
**致命问题是 venue mismatch。** CoRL 2026 明确要求 "focus on a core robotics problem"，本 proposal 关于 NLP mechanistic interpretability for math PRMs 的内容与 robotics 完全无关，极大概率 desk-reject。这一条直接将概率压到接近 0%。

即使假设投到合适的 venue（NeurIPS/ICML/ICLR），idea 质量的概率估计约 20-28%（中位 ~24%）：
- Novelty 弱是主要限制因素：核心贡献是 existing methods 的 comparison + post-hoc domain hypothesis，缺乏 methodological innovation
- Significance 受限于 "I would have guessed this" 风险
- 极好的 Related Work 覆盖提供了 floor support，但不能弥补 idea 内核的薄弱
- 280 H100-hours 的投入产出比堪忧——花大量 compute 做 comparison study

【主要风险】: 
1. **致命风险 — 完全的 venue mismatch**: CoRL 是 robotics 会议，本 proposal 是纯 NLP/MI 工作，desk-reject 概率极高。建议改投 NeurIPS 2026, ICML 2026, ICLR 2027, 或 EMNLP 2026。
2. **Idea 层面风险 — Novelty 不足**: 核心贡献是 empirical comparison + post-hoc domain hypothesis，没有新方法/新 technique/新 insight。审稿人可能评价为 "well-executed comparison study but limited novelty for main conference"。Domain Amenability Hypothesis 的 N=2 对比 + 大量混杂因素使其作为 "hypothesis test" 的说服力很弱。
```

Sources:
- [Interpretability without Actionability (Basu et al., 2026)](https://arxiv.org/abs/2603.18353)
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)
- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/html/2604.27495)
- [Position: Interpretability Can Be Actionable (Orgad et al., ICML 2026)](https://arxiv.org/abs/2605.11161)
- [Locate, Steer, and Improve Survey (Zhang et al., 2026)](https://arxiv.org/pdf/2601.14004)
- [Reward Under Attack: PRM Hackability (Tiwari et al., 2026)](https://arxiv.org/abs/2603.06621)
- [One Bias After Another (2026)](https://arxiv.org/pdf/2603.03291)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [ICML 2026 Poster: Interpretability Can Be Actionable](https://icml.cc/virtual/2026/poster/67043)


【原始 proposal（允许参考但不是主要依据）】:
# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models

## Description
When do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.

## Core Problem
The mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).

## Opportunity
The interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.

## Related Work / Landscape
THE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.

ACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.

PRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.

INTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.

SPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.

SAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.

CIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.

SELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.

GENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.

## Approach
We conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.

**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**

*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.

*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.

*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.

**Phase 2: Multi-Method Causal Circuit Tracing.**

Tier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).

Tier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.

**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.

Components are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.

**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:

(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.

(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.

**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:

**Core granularities (all 3 PRMs × 3 core benchmarks):**
(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);
(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;
(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.

**Extension granularities (single most informative PRM × 3 core benchmarks):**
(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;
(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.

We benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.

**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:

*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?

*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.

This produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.

**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.

**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.

## Inspiration
Primary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing

## Key References
- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)
- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)
- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)
- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)
- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)
- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)
- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)
- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)
- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)
- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)
- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)
- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)
- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)
- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)
- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)
- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)
- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)
- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)
- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)
- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)
- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)
- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)
- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)
- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)
- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)
- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)
- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)
- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)
- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)

## Resource Estimate
- **manual**: {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}
- **human_in_loop**: {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}
- **auto_research**: {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0af19dfd-447c-44b1-93a7-c5f2aa883574",
  "type": "user",
  "uuid": "5f0b5ed1-8247-43ed-8a1d-d763df0bbf70",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T19:20:40.426Z_

```json
{
  "parentUuid": "5f0b5ed1-8247-43ed-8a1d-d763df0bbf70",
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
  "uuid": "5eda5c78-2b2c-4300-beee-2267477dbd7c",
  "timestamp": "2026-05-19T19:20:40.426Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T19:20:40.426Z_

```json
{
  "parentUuid": "5eda5c78-2b2c-4300-beee-2267477dbd7c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "32f3e7a0-4d99-4d29-b383-a3b6f725f822",
  "timestamp": "2026-05-19T19:20:40.426Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make my assessment. Let m…",
  "leafUuid": "32f3e7a0-4d99-4d29-b383-a3b6f725f822",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate mechanistic interventions on process reward models",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813"
}
```

---

### Assistant

_source line 8 · 2026-05-19T19:21:10.806Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

Let me extract the key information from each reviewer:

**Reviewer 1:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability (CoRL): ~0% (desk reject)
- Probability (suitable venue): [15% - 25%] 中位 20%
- Key issues: venue mismatch, Domain Amenability Hypothesis is near-tautological, N=2 comparison, post-hoc rationalization, trivial alternative threat


**Reviewer 2:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability (CoRL): [0% - 3%] 中位 1%
- Probability (suitable venue): [18% - 30%] 中位 23%
- Key issues: venue mismatch, N=2 hypothesis testing weak, "I would have guessed this" risk, empirical comparison not methodological novelty

**Reviewer 3:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability (CoRL): 0%

–3% 中位 1%
- Probability (suitable venue): 20%–28% 中位 ~24%
- Key issues: venue mismatch, post-hoc rationalization, trivial alternative (fine-tuning), empirical systematization not methodological novelty

Now I'm aggregating the acceptance probabilities across reviewers. For CoRL, all three converge around 1%, while for a suitable venue like NeurIPS/ICML/ICLR, the medians cluster between 20–24%. Let me calculate the mean and standard deviation across these venue estimates to get a clearer picture of the consensus.

The suitable venue estimates show high consistency with a standard deviation under 2%, indicating strong agreement among reviewers. For CoRL specifically, all three reviewers independently identified the venue mismatch as a fatal flaw—this is overwhelming consensus. Now I'm identifying where reviewers agree and diverge on the core issues. Work is strong: ALL 3 (强)
5. Significance is medium: ALL 3 (中)
6. Trivial alternative threat (fine-tuning baseline): ALL 3
7. "I would have guessed this" risk: R2 and R3 explicitly, R1 implicitly (近同义反复)
8. Four conditions are post-hoc/overfitted: ALL 3

**Divergence points:**
- R1 rates Novelty as 弱, R2 rates it as 中, R3 rates it as 弱. So 2 out of 3 say 弱.
- R2 is slightly more generous on novelty, noting the "Domain Amenability Hypothesis" framing is genuinely new (confirmed by search). But R1 and R3 argue this doesn't constitute sufficient novelty.

All three reviewers converge on essentially 0-1% acceptance probability for CoRL 2026 specifically, which is the actual target venue. However, they also estimated chances for more suitable ML/NLP venues at around 20-24%, showing high consistency across reviewers. Since the question focuses on CoRL 2026 main conference, the consensus is a desk reject.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32f3e7a0-4d99-4d29-b383-a3b6f725f822",
  "isSidechain": false,
  "requestId": "req_011CbCUC1p6TVanuf2W6Xumg",
  "type": "assistant",
  "uuid": "c6268506-3d56-4b63-90fd-86ae401e9474",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ett8dfb2axdRs3xjEESRh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22198,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3969,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3969,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 22198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22198
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

_source line 9 · 2026-05-19T19:22:13.803Z_

【阶段】: Meta Judge
【三次中位】: [20%, 23%, 24%] std≈1.7%（注：此为三位审稿人假设投稿合适 ML/NLP venue 的概率；投稿 CoRL 的概率三人分别为 ~0%、1%、1%，std≈0.5%）

【共识维度】:
- **Venue Mismatch（致命）**: 3/3 审稿人独立判定——proposal 与 CoRL 2026（Conference on Robot Learning）完全无交集，零机器人内容，desk reject 概率极高。三人均独立查证了 CoRL CFP 并得出相同结论。**这是最高信号的共识。**
- **Novelty（弱-中）**: 3/3 审稿人认为核心贡献是"已有方法的 comparison + post-hoc domain framing"，缺乏方法论创新。R1 和 R3 判"弱"，R2 判"中"（2:1 偏弱）。
- **Domain Amenability Hypothesis 的科学效力（严重缺陷）**: 3/3 审稿人独立指出 N=2 domain 对比（PRM vs. clinical LM）无法构成有效假设检验，混杂因素过多，属于 post-hoc rationalization 而非 hypothesis testing。四条件的选择缺乏理论基础，存在 overfitting-to-the-observation 风险。
- **Significance（中）**: 3/3 审稿人认同"when do MI interventions succeed"是 timely 且 important 的问题，但对本 proposal 回答该问题的质量存疑。R2/R3 明确提出"I would have guessed this"风险。
- **Related Work（强）**: 3/3 审稿人一致认为 related work 覆盖极为全面、引用准确、差异化定位清晰，是 proposal 最强维度。
- **Trivial Alternative 威胁**: 3/3 审稿人均指出 fine-tuning on debiased data 可能以更低成本达到类似效果，削弱 mechanistic approach 的增量实用价值。
- **"I would have guessed this" 风险**: R2/R3 显式提出，R1 以"近同义反复"的表述暗示——PRM 有 scalar output + verifiable ground truth + constrained structure，intervention 更容易成功并不 surprising。

【异常维度】:
- R1 对"Domain Amenability Hypothesis 近乎同义反复"的措辞最激烈（"当你能清晰定义成功、精确测量效果时，干预更可能被判定为成功"），R2/R3 措辞更温和但实质判断一致。非 outlier，仅程度差异。
- R2 给 Novelty 判"中"而非"弱"，理由是"Domain Amenability Hypothesis 作为 framing 确实无先例"（经搜索确认）。这是唯一的评级分歧，但 R2 自己也承认核心 delta 是 "comparison + framing, not method or discovery"，实质与 R1/R3 差距不大。降权处理：Novelty 最终判定偏向"弱"。
- R1 提到 generative PRM（ThinkPRM, GenPRM）替代 discriminative PRM 对 practical significance 的削弱；R2/R3 提及但未强调。此点有一定信号但非决定性（discriminative PRM 仍在广泛部署）。

【最终概率】:
- **投稿 CoRL 2026（实际目标）**: [0% - 2%] 中位 1%
- **假设投稿合适 ML/NLP venue（NeurIPS/ICML/ICLR）**: [16% - 25%] 中位 21%

【一致性】: 高（三位审稿人在所有关键维度上高度一致，概率估计 std≈1.7%）

【综合理由】:

**1. CoRL 概率（中位 1%）**：三位审稿人对 venue mismatch 的判定完全一致且独立验证，这是无法通过任何 proposal 修改来弥补的致命问题（除非彻底重写为 robotics 方向）。Proposal 内容是纯 NLP/MI 工作，与 robot learning 零交集。CoRL CFP 明确要求 "focus on a core robotics problem"。Desk reject 几乎确定。

**2. 合适 venue 概率（中位 21%）**：三份评审高度一致（std≈1.7%），取中位附近略偏严。理由：
- **Novelty 是核心瓶颈**（2/3 判"弱"，1/3 判"中"）：核心贡献是已有方法的 comparison + 一个科学效力不足的 domain hypothesis。ML 顶会对 empirical comparison papers 的 novelty bar 很高，需要 comparison 本身产生 surprising insights——而本 proposal 最可能的结论"PRM 上 intervention 有效"并不 surprising。
- **Significance 受限于假设检验的强度**：N=2 的 domain 对比无法排除混杂因素，即使实验全部成功，审稿人仍无法判断是因为四条件还是其他原因。
- **Related Work 的强项提供了 floor support 但不能弥补 idea 内核的薄弱**——这是三位审稿人的共同判断。
- 上界 25% 而非更高，因为 Novelty 弱是硬性天花板——即使实验完美执行，核心 intellectual contribution 仍不足以突破 25%。
- 下界 16% 而非更低，因为选题确实紧扣社区热点辩论（actionability debate），且如果实验中出现意外发现可能有上升空间。

**3. 分歧处理**：R2 给 Novelty 判"中"是唯一分歧。但 R2 的理由（"framing 是新的"）与 R1/R3 的判定（"framing 新但科学效力弱"）并不矛盾——R2 自己也承认这是 "solid empirical study" 而非 "conceptual breakthrough"。因此 Novelty 最终裁定偏向"弱"，但不完全忽略 R2 的考量（反映在概率未跌破 16%）。

【建议】: 不推荐（投稿 CoRL 2026）/ 边缘偏不推荐（投稿合适 ML/NLP venue，需重大修改）

**具体建议**：
1. **必须更换投稿目标**。CoRL 2026 是 desk reject。建议 NeurIPS 2026、ICML 2026 或 EMNLP 2026。
2. **如果转投 ML/NLP venue**，核心问题是 Novelty——需要在迭代中重点强化 idea 层面，而非仅打磨实验设计。三位审稿人共同指向的可能提升路径：(a) 大幅增加对比 domain 数量以增强假设检验的说服力；(b) 放弃弱假说包装，转而强化 multi-granularity comparison 的方法论贡献（需要产出 surprising finding）；(c) 提出新的 intervention method 而非仅比较已有方法。

【实施评估】:
- **计算资源**: 280 H100-hours（约 $560），三位审稿人均未质疑此估算的合理性。R3 指出"280 H100-hours 的投入产出比堪忧——花大量 compute 做 comparison study"。整体计算需求中等偏高，但在可行范围内。
- **数据需求**: PRM-BiasBench、ProcessBench、RM-Bench（Hard split）、PRMBench、Socratic-PRMBench 均为公开数据集。Wang et al. 的 automated bias discovery pipeline 需要复现。模型方面 Qwen2.5-Math-PRM-7B、Math-Shepherd-Mistral-7B-PRM、Skywork-o1-Open-PRM-Qwen-2.5-1.5B 均公开可得。数据需求无障碍。
- **人工介入**: 中等。需要人工构建 contrastive pairs、审核 SAE feature 质量、验证 circuit taxonomy 的合理性。Wang et al. pipeline 的复现需要工程投入。
- **训练需求**: 需要从头训练 SAE（非 LLM 训练），计算量可控（~65 H100-hours for SAE training）。可能需要训练 CLT（35 H100-hours on 1.5B model）。不需要训练/微调 LLM。
- **新 Benchmark**: 不需要构建新 benchmark，使用现有公开 benchmark 组合。但 "granularity-by-criterion matrix" 评估框架是新的组织方式。
- **预估周期**: 10-12 周（从启动到可投稿）。关键瓶颈是 pilot SAE training → targeted layer selection 的顺序依赖，以及多粒度实验的并行调度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6268506-3d56-4b63-90fd-86ae401e9474",
  "isSidechain": false,
  "requestId": "req_011CbCUC1p6TVanuf2W6Xumg",
  "type": "assistant",
  "uuid": "67a74646-856f-49cf-afd6-8bae9379cb4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ett8dfb2axdRs3xjEESRh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22198,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3969,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3969,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 22198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22198
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make my assessment. Let m…",
  "leafUuid": "67a74646-856f-49cf-afd6-8bae9379cb4d",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate mechanistic interventions on process reward models",
  "sessionId": "900c5be3-d76c-4e50-a5c1-51b0987ca813"
}
```

---
