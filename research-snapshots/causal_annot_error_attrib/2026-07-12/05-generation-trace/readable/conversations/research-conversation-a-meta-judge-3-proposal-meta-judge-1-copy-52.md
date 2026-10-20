# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/d5b3a5f8-6648-4b68-9731-b0731efe8e68.jsonl`
- **Structured JSON:** [`f89d82ab2e170ceb6b92.json`](../../sessions/f8/f89d82ab2e170ceb6b92.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:42:48.222Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:42:48.222Z",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a thorough, evidence-based evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [GenPRM (arXiv:2504.00891)] (AAAI 2026): 直接竞争者。7B generative PRM via CoT + code verification，在 ProcessBench 上超越 Qwen2.5-Math-PRM-72B。开源权重和代码，是 neural branch 的核心组件也是最强 neural baseline。\n- [FoVer (arXiv:2505.15960)] (ACL 2026): 直接竞争者/基础组件。Z3/Isabelle 生成 PRM 训练标签，在 12 个推理 benchmark 上泛化性强，但 proposal 正确指出其在 informal reasoning steps 上 overly-strict 的问题。\n- [VERGE (arXiv:2601.20055)] (arXiv 2026): 最直接的先驱。Rule-based semantic routing（logical claims → Z3, commonsense → LLM ensemble），18.7% uplift。论文明确指出 learned routing 是 open problem——proposal 的 novelty claim 在此成立。\n- [LogicReward (arXiv:2512.18196)] (ICLR 2026): 相关但定位不同。Isabelle step verification + RL training reward，8B 模型超 GPT-4o 11.6%。但它是 RL reward framework，不是 standalone PRM；其 \"try-formal-first\" 策略确实存在 proposal 所述的 false alarm 问题。\n- [ThinkPRM (arXiv:2504.16828)] (arXiv 2025): 强 baseline。仅用 PRM800K 1% 的 process labels 训练，在相同 token budget 下超 LLM-as-Judge 7.2%。其 token-budget-normalized 比较范式是本 proposal 需要满足的实验标准。\n- [R-PRM (arXiv:2503.21295)] (EMNLP 2025): +13.9 F1 on ProcessBench via three-stage pipeline (cold-start, DPO, inference scaling)。又一个强 neural baseline。\n- [RRM (arXiv:2510.07774)] (withdrawn ICLR 2026): 定义 miracle step taxonomy，RRM 减少 71% miracle steps via rubric rewards。Proposal 的 miracle step detection 概念直接来源于此，但 RRM 从未用 formal derivability——proposal 在此有差异化。\n- [Risk-Controlled Lean-as-Judge (arXiv:2605.28365)] (arXiv 2026): 关键参考。报告 7B autoformalizer 仅 43% faithfulness、28% coverage on MATH-500。这是对 proposal 有利也有弊的证据——说明了 honest reporting 的必要性，但也暴露了 formal branch 的有效覆盖率可能很低。\n- [Do LLMs Game Formalization? (arXiv:2604.19459)] (arXiv 2026): 识别 axiom fabrication 和 premise mistranslation 两种 unfaithfulness 模式。Proposal 正确引用此作为 roundtrip verification 的动机。\n- [PRMBench (arXiv:2501.03124)] (ACL 2025): 标准评测基准。6,216 problems, 83,456 step-level labels。SOTA (Gemini-2-Thinking) 68.8 vs human 83.8，差距仍大。\n- 调研总结: PRM 领域 2025-2026 极度活跃，formal/neural/hybrid 三条路线并行发展。VERGE 的 rule-based routing 和 LogicReward 的 try-and-fallback 已经验证了 hybrid 路线的价值，但 **learned context-dependent routing** 确实是一个明确的、被先驱工作显式指出的 open gap。Proposal 精准定位了这个缝隙。然而，autoformalization 的低 faithfulness (43%) 和低 coverage (28%) 对 formal branch 的实际价值构成根本性约束。\n\n【整体印象】:\n作为审稿人，第一反应是：这是一份 **异常成熟的 proposal**，文献梳理之细致、positioning 之精准、实验设计之完备在 proposal 阶段是罕见的。作者显然对 PRM 领域有深入理解，且诚实地面对了 autoformalization 的局限性（这是加分项）。\n\n但同时会有两个顾虑浮上来：\n1. **核心贡献的 \"系统集成\" 味道较重**——每个组件（Z3 验证、roundtrip verification、GenPRM neural scoring、LoRA router）都是已有的，创新主要在组装方式和 learned routing 上。这在 AAAI 审稿中可能被视为 incremental。\n2. **\"Conditional soundness\" 的实际覆盖率可能很低**——如果 7B autoformalizer 只有 28% coverage × 43% faithfulness ≈ 12% effective soundness coverage（即使用 72B 模型可能提升到 20-30%），审稿人会质疑：\"对 12-30% 的 steps 有 formal guarantee，对整体 PRM 性能提升有多大？\"\n\n倾向：**borderline**，在 weak accept 和 weak reject 之间。实验设计的完备性是显著加分项，但 novelty 和 practical impact 的疑虑需要强实验结果来弥补。\n\n【核心贡献】:\n1. **Learned context-dependent formalizability routing**——区别于 VERGE 的 rule-based 和 LogicReward 的 unlearned try-and-fallback，这是一个明确的 technical contribution，但量级偏轻（本质是一个分类器）。\n2. **Conditional sound miracle step detection**——概念上干净（formally verified subset 上 Z3 UNSAT = miracle step），但 practical coverage 受 autoformalization 瓶颈严重限制。\n3. **Three-layer pipeline 的系统设计**——完整的 routing + faithfulness gating + hybrid verification，带 asymmetric cost-aware threshold。\n\n对领域的价值：如果 learned routing 能显著优于 VERGE 和 try-and-fallback（>3-5% 提升），且 formal branch 在 miracle step detection 上有明显 precision 优势，这对 PRM 社区有 solid 的参考价值。但如果提升有限，贡献就偏薄。\n\n【方法合理性】:\n方法整体 **逻辑自洽且合理**。Three-layer pipeline 的设计有清晰的因果链：routing 解决 \"该不该送 formal\"，roundtrip verification 解决 \"formal translation 是否忠实\"，Z3/GenPRM 解决 \"步骤是否正确\"。Asymmetric cost-aware threshold 是合理的工程考量。\n\n**更简单的替代方案是否能达到类似效果？** 这是最大的方法论风险：\n- **Try-and-fallback baseline**（proposal 自己列为 Ablation #6）可能与 learned routing 差距不大。如果 Z3 返回 timeout/error 的速度足够快，fallback 的额外成本可能很低，learned routing 的优势就不明显。\n- **GenPRM majority voting at equivalent compute**（proposal 列为 compute-matched baseline）可能在整体 F1 上接近甚至超过 hybrid system，因为 formal branch 的低覆盖率限制了其贡献。\n- Proposal 设计了这两个关键 baseline，说明作者意识到了这些风险，这本身是加分项——但实验结果需要 beat 这些 baseline，否则 \"learned routing\" 的价值就不成立。\n\n【5 维度打分】:\n\n1. **研究问题**: 【中偏强】\n   理由：Learned formalizability routing 是一个真实的 open problem（VERGE 论文显式指出），问题动机清晰。但问题的 impact 受 autoformalization 瓶颈约束——即使 routing 完美，formal branch 的有效覆盖率也可能很低（Risk-Controlled Lean-as-Judge 报告 28% coverage, 43% faithfulness），这限制了整体方法在 end-to-end PRM 任务上的潜在提升空间。问题有研究价值，但不是 high-impact 级别。\n\n2. **方法与创新**: 【中】\n   理由：与 VERGE 的 rule-based routing 和 LogicReward 的 try-and-fallback 相比，learned context-dependent routing 是一个 clear next step，但 novelty 量级偏轻——核心创新归结为 \"用 Qwen3-8B LoRA 训练一个二分类器\"。每个组件（Z3 verification from FoVer, roundtrip verification from arXiv:2604.25031, GenPRM for neural branch, Platt scaling from ARES）都是已有工作。\"Conditional soundness\" 概念虽然干净，但更像是对已知事实的形式化表述而非新发现。与 GenPRM（generative CoT + code verification, AAAI 2026）、ThinkPRM（data-efficient + token-budget scaling）相比，本 proposal 的 methodological novelty 偏弱。\n\n3. **实验设计**: 【强】\n   理由：这是 proposal 最突出的亮点。(a) Benchmark 选择全面覆盖（ProcessBench F1/AUROC + PRMBench PRMScore + Best-of-N on MATH-500/AIME24 + OOD GPQA-Diamond + miracle step detection）。(b) Baseline 矩阵极为完整，包含 pure neural (GenPRM, ThinkPRM, R-PRM), pure formal (FoVer), hybrid (VERGE, naive hybrid), LLM-as-Judge (GPT-4o, QwQ-32B)，以及关键的 **compute-matched GenPRM majority voting**（遵循 ThinkPRM 的 token-budget-normalized paradigm）。(c) 7 项 ablation 设计周全，特别是 Ablation #6 (try-formal-first fallback) 直接测试 learned routing vs. unlearned fallback，Ablation #4 (oracle routing) 给出 performance ceiling。(d) Honest coverage reporting following Risk-Controlled methodology。(e) Router quality analysis 含 human-annotated oracle labels。这套实验方案如果执行到位，足以回答所有可能的审稿人质疑。\n\n4. **可行性**: 【中偏强】\n   理由：Compute budget 合理（training <1 day, evaluation <5 days on 8×H100）。主要组件都有开源实现（FoVer, GenPRM, Z3）。但以下风险值得注意：(a) Pipeline 涉及 5+ 个独立模块（Qwen3-8B router, Qwen2.5-Math-72B autoformalization, roundtrip verification, Z3 solver, GenPRM-7B），集成调试复杂度高。(b) Autoformalization 使用 Qwen2.5-Math-72B-Instruct，这是 dominant compute cost，且 72B 模型的推理成本在学术环境中不低。(c) Router training labels 的质量依赖 FoVer pipeline 的输出，label noise 可能影响 router 性能（proposal 有 Ablation #7 分析此问题，是好的）。(d) Miracle step 评测数据可能不公开（RRM 被 withdrawn），需要自建 human annotation（200-300 steps）。总体可行但有执行风险。\n\n5. **写作与呈现**: 【强】\n   理由：Proposal 的组织极为清晰——Problem → Opportunity → Insight → Contributions → Landscape → Approach → Evaluation，逻辑链完整。文献定位精准，每个竞争者的优劣势都有具体引用支撑。\"Conditional soundness\" 的概念表述很干净。Asymmetric cost analysis 有说服力。唯一的小瑕疵是 proposal 篇幅偏长，实际论文需要大幅压缩。\n\n【概率估计】: [28% - 40%] 中位 34%\n\n【估计理由】:\n**上界 (40%)**: 如果实验结果显示 (a) learned routing 显著优于 try-and-fallback 和 VERGE (>3% F1 on ProcessBench), (b) formal branch 在 miracle step detection 上有明显 precision 优势 (>10% precision lift), (c) compute-matched comparison 中 FormalRoute-PRM 胜出，且 (d) effective formal coverage 达到 25%+——那么\"learned routing + conditional soundness\"的双重贡献足够支撑一篇 solid 的 AAAI 投稿。实验设计的完备性本身就是显著加分项，论文质量会高于平均 submission。\n\n**下界 (28%)**: 如果 (a) try-and-fallback baseline 与 learned routing 差距很小 (<2%), (b) compute-matched GenPRM majority voting 整体性能接近或超过 FormalRoute-PRM, (c) effective formal coverage 只有 10-15%——审稿人会认为 \"用一个分类器做 routing\" 的 novelty 不足以支撑 top venue，尤其是与 GenPRM (AAAI 2026) 和 ThinkPRM 这些更 clean 的 contribution 相比。\n\n**中位 (34%)**: 最可能的情况是 learned routing 有一定优势但不显著，formal branch 在 miracle step precision 上有可测量的提升但 coverage 有限。论文的 contribution 会被认为 \"solid but somewhat incremental\"——well-executed engineering of a known direction（VERGE 已经指出了这个方向）。AAAI 审稿人对 \"系统集成\" 类工作的接受阈值相对较高，需要令人信服的实验结果来弥补 novelty 的不足。\n\n**关键不确定性**: 这个 proposal 的中稿概率异常依赖实验结果——如果 learned routing 和 conditional soundness 的实际收益超出预期，概率可以提升到 40%+；如果收益平平，会跌到 25% 左右。Proposal 本身的质量在同档竞争者中偏上，但 novelty 天花板限制了上限。\n\n【主要风险】:\n1. **\"Incremental integration\" 质疑**：每个组件（Z3, GenPRM, roundtrip verification, LoRA classifier）都是已有的，核心创新归结为训练一个路由分类器。如果 learned routing vs. try-and-fallback 的提升有限，审稿人很可能判定 novelty 不足。这是最可能的 reject 理由。\n2. **Formal branch 的 effective coverage 过低导致 practical impact 存疑**：基于 Risk-Controlled Lean-as-Judge 的数据（28% coverage, 43% faithfulness），即使用 72B autoformalizer，effective soundness coverage 可能仅 20-30%。审稿人会问：\"对 20% 的 steps 有 formal guarantee，对 end-to-end Best-of-N reranking 的提升到底有多少？这个 guarantee 值不值得 72B autoformalization 的额外 compute cost？\"\n\n【实施评估】:\n  - 计算资源: 单节点 8×H100，training <1 day, evaluation <5 days。主要开销在 Qwen2.5-Math-72B-Instruct autoformalization inference（约占 70% compute）。学术可行但不宽裕。\n  - 数据需求: FoVer 公开数据 (~80K labels) 用于 router training；ProcessBench, PRMBench, MATH-500, AIME24, GPQA-Diamond 均为公开 benchmark；miracle step annotation 需自建 200-300 例 (2-3 annotators)。\n  - 人工介入: (a) Router label audit: 200-300 examples human review; (b) Miracle step annotation: 200-300 steps, 2-3 annotators + Cohen's kappa; (c) Oracle formalizability labels: 100-200 examples. 总人工量中等。\n  - 训练需求: Qwen3-8B LoRA fine-tuning (~4-8 GPU-hours)，GenPRM-7B 和 Qwen2.5-Math-72B 使用现有权重无需额外训练。训练量很轻。\n  - 新 Benchmark: 不需要构建全新 benchmark，但需要自建 miracle step human annotation set (200-300 steps)。\n  - 预估周期: Pipeline 搭建 2-3 周 + Router training & tuning 1 周 + Full evaluation 2-3 周 + 论文写作 2-3 周 ≈ **7-10 周** (若顺利)。考虑到多模块集成调试可能遇到的问题，留 **10-12 周** 更保险。\n```\n\nSources:\n- [GenPRM: Scaling Test-Time Compute of PRMs via Generative Reasoning (AAAI 2026)](https://arxiv.org/abs/2504.00891)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055)\n- [LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision (ICLR 2026)](https://arxiv.org/abs/2512.18196)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025)](https://arxiv.org/abs/2503.21295)\n- [RRM: Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774)\n- [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](https://arxiv.org/abs/2605.28365)\n- [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/abs/2604.19459)\n- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)](https://arxiv.org/abs/2501.03124)\n- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)\n- [Awesome-Process-Reward-Models GitHub](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough field context to conduct a thorough evaluation. Let me compile the full assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960) (ACL 2026 Findings): 直接前置工作。用Z3/Isabelle生成PRM训练标签，ProcessBench上85.8 AUROC，但在非形式化步骤上存在documented overly-strict behavior。本proposal的formal branch和router训练标签直接依赖FoVer。\n- [GenPRM: Scaling Test-Time Compute of PRMs via Generative Reasoning](https://arxiv.org/abs/2504.00891) (AAAI 2026): 本proposal neural branch的核心组件。7B模型超越Qwen2.5-Math-PRM-72B，是当前最强neural PRM之一。被本proposal作为neural verifier使用。\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 最直接的竞争者/前驱工作。rule-based semantic routing（逻辑 vs. 常识claim）分派到Z3或neural ensemble，取得18.7% uplift。论文明确指出\"learned routing\"是open next step——本proposal正好填补这一空白。\n- [LogicReward](https://arxiv.org/abs/2512.18196) (ICLR 2026): Isabelle step verification + token-probability fallback，8B模型在逻辑推理上超GPT-4o 11.6%。是RL训练框架而非standalone PRM，其try-and-fallback策略正是本proposal要改进的routing机制。\n- [Curing Miracle Steps with Rubric Rewards (RRM)](https://arxiv.org/abs/2510.07774) (arXiv 2025, withdrawn ICLR 2026): 定义了miracle step分类法，通过rubric rewards减少71% miracle steps，但未使用formal derivability检测。本proposal将miracle step概念与formal verification结合。\n- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365) (arXiv 2026): 关键校准数据来源。7B autoformalizer在MATH-500上仅43% faithfulness、28% coverage。本proposal的honest coverage reporting methodology直接源于此工作。\n- [ThinkPRM](https://arxiv.org/abs/2504.16828) (arXiv 2025): 14B模型仅用8K process labels训练，建立了token-budget-normalized比较范式。本proposal的compute-matched comparison直接参考其方法论。\n- [R-PRM](https://arxiv.org/abs/2503.21295) (EMNLP 2025): ProcessBench上+13.9 F1，PRMBench上+8.5 F1，三阶段训练pipeline。重要baseline。\n- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459) (arXiv 2026): 识别axiom fabrication和premise mistranslation两种unfaithfulness模式，为roundtrip verification的必要性提供理论依据。\n- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031) (arXiv 2026): 本proposal Layer 2的方法论来源。\n\n- **调研总结**: PRM领域2025-2026处于快速发展期，formal PRM（FoVer）和neural PRM（GenPRM/ThinkPRM/R-PRM）各有明确优势和局限，hybrid系统（VERGE/LogicReward）已验证了formal+neural组合的价值但routing机制粗糙。本proposal定位于\"learned formalizability routing\"这一被VERGE明确标识为open problem的空白，时机准确，但面临核心贡献被视为\"工程组合\"的风险。搜索未发现任何已有的learned formalizability routing工作，novelty claim在当前文献中成立。\n\n【整体印象】:\n作为审稿人，我的第一反应是：这是一篇定位非常精准、文献综述极为扎实、实验设计异常完备的proposal，作者对领域的理解深度令人印象深刻。\"Conditional formal soundness\"的概念框架诚实且有智识吸引力——不回避autoformalization的局限性，反而将其显式建模。\n\n然而，我会有两个核心疑虑：(1) 核心贡献是否足够\"新\"——learned router + existing formal verifier + existing neural verifier的组合，每个组件都来自已有工作，novelty主要在于组合方式和router的学习；(2) formal soundness guarantee的实际覆盖率可能非常窄——如果autoformalization faithfulness仅43%、coverage仅28%，经过router + roundtrip verification双重过滤后，能获得formal guarantee的步骤可能仅占总步骤的10-15%，这使得\"sound miracle step detection\"的实际影响被大幅稀释。\n\n倾向：**weak accept / borderline**——方向正确、执行方案扎实，但需要实验证明learned routing显著优于简单的try-and-fallback baseline，且formal branch的实际覆盖率足以产生meaningful impact。\n\n【核心贡献】:\n核心贡献是**learned context-dependent formalizability routing**——一个经过训练的分类器，根据步骤及其前驱上下文预测该步骤是否可以被faithfully formalized，从而将其分派到formal（Z3）或neural（GenPRM）验证路径。配合roundtrip faithfulness verification，在正式验证的子集上提供sound miracle step detection。\n\n对领域的价值评估：\n- **填补真实空白**: VERGE明确标识learned routing为open problem，LogicReward的try-and-fallback策略有documented局限性。这不是一个人造的gap。\n- **conditional soundness framing**: 将形式化验证的保证与autoformalization的局限性显式关联，提供了一个intellectually honest的分析框架，这对后续hybrid PRM的设计有指导意义。\n- **但贡献的\"重量\"取决于实验结果**: 如果learned router相比try-and-fallback仅有marginal improvement，或formal branch的effective coverage过低，则贡献会显得单薄。\n\n【方法合理性】:\n方法总体合理，三层pipeline设计逻辑清晰：\n\n**合理之处:**\n1. Router → Roundtrip → Verification的层次设计，每层有明确功能和失败模式处理。\n2. Asymmetric cost-aware threshold是一个thoughtful设计选择，反映了对FoVer overly-strict behavior的正确理解。\n3. 使用Qwen3-8B作为router（轻量）+ Qwen2.5-Math-72B-Instruct作为autoformalizer（强力）的分工合理。\n\n**潜在问题:**\n1. **更简单的替代方案**: \"try-formal-first + neural fallback\"（ablation #6）是最直接的竞争方案。如果Z3 timeout足够快，这个trivial baseline可能接近learned routing的效果——因为autoformalization失败或Z3 timeout会自然地将non-formalizable步骤redirect到neural branch。Proposal已预见到这一点并设置了专门ablation，这很好，但如果实验中learned routing的优势不显著，整个工作的价值会被大幅削弱。\n2. **Router训练标签的noise**: FoVer Z3 labels + autoformalization success signals本身是noisy的（Risk-Controlled的43% faithfulness数据）。Router trained on noisy labels → router本身的precision/recall可能不理想。Ablation #7（label noise analysis）是正确的实验，但500-1000 human-cleaned examples可能不够。\n3. **Roundtrip verification的可靠性**: 依赖LLM进行back-translation + semantic equivalence check——这本身也是一个noisy过程，可能引入新的failure modes。\n\n**总结**: 方法合理但不算elegant——是对已有组件的工程化组合。没有看到更简单的替代方案能直接替代整个pipeline，但try-and-fallback是一个需要convincingly beat的baseline。\n\n【5 维度打分】:\n\n1. **研究问题: 中偏强** — Learned formalizability routing是VERGE明确标识的open problem，且formal-neural hybrid PRM是一个真实且活跃的研究方向。Miracle step detection具有practical importance（RRM的71%减少表明这是一个real problem）。扣分点：研究问题的\"规模\"相对较小——这是一个specific routing mechanism的改进，而非paradigm shift。\n\n2. **方法与创新: 中** — Novelty在于将formalizability prediction建模为learned classification problem，并引入conditional soundness framing。但每个组件（Z3 verification from FoVer, GenPRM for neural scoring, roundtrip verification from arXiv:2604.25031, miracle step concept from RRM）都直接来自已有工作，创新主要在于组合和routing mechanism。与VERGE（rule-based routing, 18.7% uplift）相比，learned routing是自然但incremental的改进。与LogicReward（try-and-fallback）相比，显式routing避免了false alarms——但这一优势需要实验量化。搜索结果确认无已有learned formalizability routing工作，novelty claim成立，但contribution weight取决于实验中learned vs. unlearned routing的delta。\n\n3. **实验设计: 强** — 这是本proposal最突出的优势。Baseline matrix非常全面（neural: GenPRM/ThinkPRM/R-PRM/Qwen2.5-Math-PRM-72B; formal: FoVer; hybrid: VERGE + Naive Hybrid; LLM-as-Judge: GPT-4o/QwQ-32B; compute-matched: GenPRM majority voting）。7项ablation设计精准，特别是ablation #6（try-formal-first baseline）和ablation #4（oracle routing ceiling）直接回答了最关键的问题。Compute fairness reporting（含autoformalization cost）和honest coverage reporting展示了methodological rigor。唯一不足：miracle step detection的benchmark不确定（RRM数据可能不公开），self-constructed set仅200-300 steps偏小。\n\n4. **可行性: 中偏强** — Compute budget realistic（单节点8×H100，训练<1天，评估<5天）。所有组件都有公开实现（FoVer开源、GenPRM有open weights）。主要风险：(a) Qwen2.5-Math-72B-Instruct的autoformalization推理成本是dominant cost，可能限制实验throughput；(b) router训练标签的构建需要大量autoformalization预处理；(c) roundtrip verification的semantic equivalence checking可能需要额外调优。总体而言，方案在学术团队的资源范围内可执行。\n\n5. **写作与呈现: 强** — Proposal结构清晰，论证有力。Research landscape部分对每个prior work的定位精准，关键差异点清晰标注。\"Key Insight\"部分对conditional soundness的推导逻辑严密。Contributions的表述不over-claim——\"first PRM offering formal soundness guarantees for any subset\"的措辞恰当。对局限性的处理（autoformalization faithfulness问题、coverage limitations）诚实且前置。唯一不足：pipeline的复杂性可能在实际论文中需要更好的可视化/figure设计来辅助理解。\n\n【概率估计】: [28% - 40%] 中位 34%\n\n【估计理由】:\n**上行因素 (→40%)**:\n- 填补VERGE明确标识的open problem，时机精准\n- 实验设计异常完备，显示了高度的methodological awareness\n- PRM是2025-2026热门方向，AAAI对此类工作有需求\n- Conditional soundness framing在intellectually honest的同时具有新颖性\n- 如果learned routing显著beat try-and-fallback，且formal branch effective coverage达到20%+，论文将非常convincing\n\n**下行因素 (→28%)**:\n- 核心贡献可能被视为existing components的工程组合，novelty depth不足\n- Formal soundness的effective coverage可能过窄（~10-15%），稀释实际impact\n- AAAI 2026竞争激烈，同领域（PRM/verification）可能有多篇投稿\n- 如果learned routing vs. try-and-fallback的margin较小，核心卖点不成立\n\n**中位34%的推理**: 这是一篇well-positioned、technically sound、experimentally thorough的proposal，处于\"有实质贡献但缺乏突出亮点\"到\"整体扎实\"的交界区间。最终命运很大程度取决于两个关键实验结果：(1) learned routing vs. try-and-fallback的performance gap，(2) formal branch的effective soundness coverage。在结果未知的情况下，给予略高于baseline acceptance rate的估计。\n\n【主要风险】:\n1. **Learned routing可能无法显著超越try-and-fallback**: 如果Z3 timeout足够快（millisecond级，proposal中也提到），try-formal-first策略可以自然地将non-formalizable步骤redirect到neural branch，使得learned router的added value marginal。这将直接瓦解contribution #2（learned routing的三个优势）。\n2. **Formal branch的effective soundness coverage过低**: 经过router过滤 → autoformalization → roundtrip verification三层筛选后，获得formal guarantee的步骤可能仅占总步骤的极小比例（<15%），使得\"sound miracle step detection\"更像一个theoretical contribution而非practical improvement——reviewers可能质疑\"为了验证15%的步骤值得引入这么复杂的pipeline吗？\"\n\n【实施评估】:\n  - 计算资源: 单节点8×H100，合理。Dominant cost是Qwen2.5-Math-72B-Instruct的autoformalization推理，估计约3-4天（假设30-50%步骤进入formal branch，跨多个benchmark）\n  - 数据需求: FoVer-80K公开数据用于router训练；ProcessBench、PRMBench、MATH-500、AIME24、GPQA-Diamond均为公开benchmark；需自建200-300步human-annotated miracle step数据集\n  - 人工介入: (a) 200-300步miracle step标注（2-3名标注员+Cohen's kappa），约2-3人天；(b) 200-300条router训练标签人工审核，约1-2人天；(c) 100-200条oracle formalizability标注，约1人天。总计约5-8人天。\n  - 训练需求: Qwen3-8B LoRA fine-tuning（4-8 GPU-hours），轻量级。无需训练GenPRM或autoformalization模型（使用现有权重）。\n  - 新 Benchmark: 不需要构建新benchmark。需要自建小规模miracle step标注集（200-300步）作为补充评估，但非full benchmark。\n  - 预估周期: Router训练1天 + Pipeline集成与调试3-5天 + 全量评估5天 + 消融实验5-7天 + 人工标注与分析3-5天 + 论文写作2-3周 = **总计约6-8周**（单人）或**4-5周**（2-3人团队）\n```\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)\n- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)\n- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)\n- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)\n- [PRMBench: Fine-grained PRM Benchmark](https://arxiv.org/abs/2501.03124)\n- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459)\n- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960) (ACL 2026): 直接前序工作。使用 Z3/Isabelle 合成 PRM 训练标签，ProcessBench 上 85.8 AUROC。文档化了在非形式化推理步骤上的\"过于严格\"行为——这正是本 proposal 试图解决的问题。提供公开代码和数据集。\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 最直接竞争者。规则化语义路由（逻辑 vs. 常识 claim type）到 Z3 或 LLM ensemble，18.7% 性能提升。路由是静态的、基于 claim type 的、非学习的。论文明确指出 learned routing 是开放的下一步——本 proposal 正是回应这一 gap。\n- [LogicReward](https://arxiv.org/abs/2512.18196) (ICLR 2026): Isabelle step verification + token-probability fallback。8B 模型超越 GPT-4o 11.6%。但其\"先尝试形式化、失败则回退\"策略无法区分\"步骤本质上不可形式化\"与\"自动形式化在可形式化步骤上失败\"——正是 proposal 所批评的缺陷。\n- [GenPRM](https://arxiv.org/abs/2504.00891) (AAAI 2026): 生成式 PRM，7B 超越 Qwen2.5-Math-PRM-72B。开源权重。本 proposal 将其用作 neural branch 的 backbone。\n- [ThinkPRM](https://arxiv.org/abs/2504.16828) (arXiv 2025): 14B 模型仅用 8K 过程标签即超越 100× 数据训练的判别式 PRM。建立了 token-budget-normalized 比较范式——proposal 引用此范式做 compute fairness 分析。\n- [R-PRM](https://arxiv.org/abs/2503.21295) (EMNLP 2025): ProcessBench +13.9 F1，PRMBench +8.5 F1，三阶段训练。本 proposal 将其列为 baseline。\n- [RRM: Curing Miracle Steps](https://arxiv.org/abs/2510.07774) (arXiv 2025, withdrawn from ICLR 2026): 定义 miracle step 分类法，通过 rubric rewards 减少 71% miracle steps。未测试形式化可推导性——proposal 的 miracle detection 贡献直接建立在此基础之上。\n- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365) (arXiv 2026): 7B autoformalizer 仅 43% faithfulness、28% coverage。该论文提供了量化 autoformalization 局限的校准数据和 honest coverage reporting 方法论——proposal 的\"条件性形式化保证\"直接受此启发。\n- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031) (arXiv 2026): Roundtrip verification 将 formal equivalence 从 45-61% 提升到 83-85%。本 proposal 的 Layer 2 直接采用此方法。\n- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459) (arXiv 2026): 识别出 axiom fabrication 和 premise mistranslation 两种 unfaithfulness 模式。为 proposal 的 roundtrip verification 层提供了理论动机。\n- [FIRMA](https://aclanthology.org/2025.mathnlp-main.5/) (MathNLP 2025): 复杂度感知路由做 formal-informal 翻译。Proposal 正确指出其目标函数（翻译质量）与 formalizability routing for verification 根本不同。\n- [PRoSFI](https://arxiv.org/abs/2603.29500) (arXiv 2026): 结构化形式中间体用于 prover verification，偏向 generation side。\n\n- **调研总结**: PRM 领域正处于从纯判别式向生成式/混合式快速演进的阶段。形式化验证（FoVer, VERGE, LogicReward）已被证明有效但受限于覆盖率和过度严格问题。\"学习化路由\"是 VERGE 明确指出的开放问题，目前确实没有工作实现了 learned context-dependent formalizability routing。但 autoformalization 的低可靠性（43% faithfulness）构成了系统性瓶颈。Proposal 在这一 landscape 中定位清晰，但其条件性保证的实际覆盖范围可能受限。\n\n【整体印象】:\n如果我是审稿人，第一反应是：这是一篇 **定位精准、技术叙事清晰、实验设计异常完备** 的 proposal。作者对领域的掌握非常深入，VERGE 的 static routing → learned routing 的 gap 真实存在且被原论文明确指出。三层 pipeline（routing → roundtrip verification → formal/neural dispatch）逻辑自洽，honest coverage reporting 的设计哲学也令人欣赏。\n\n然而，我的倾向会是 **borderline（偏向 weak accept / borderline reject）**。原因如下：\n1. 核心贡献——learned formalizability routing——在技术上是一个相对直接的二分类器（Qwen3-8B LoRA fine-tuned on FoVer labels），novelty 天花板有限。\n2. 受制于 autoformalization 的低可靠性（43% faithfulness, 28% coverage），formal branch 的\"effective soundness coverage\"可能仅覆盖 10-20% 的步骤，条件性保证的实际影响力存疑。\n3. 如果 ablation 6（try-formal-first + neural fallback）表现接近 learned router，整个贡献基础将被削弱。\n\n【核心贡献】:\n1. **Conditional sound miracle detection**: 在 router 判定为 formalizable 且 roundtrip verification 通过的步骤子集上，Z3 predecessor-derivability 检查提供有保证的 miracle step 检测。这是第一个对推理步骤子集提供形式化正确性保证的 PRM。\n2. **Learned context-dependent formalizability routing**: 不同于 VERGE 的静态 claim type routing 和 LogicReward 的 try-and-fallback，使用 Qwen3-8B 预测依赖前驱链上下文的 formalizability。\n3. **Asymmetric cost-aware routing threshold**: 显式建模路由错误的不对称代价。\n\n**贡献价值评估**: 贡献 1 在理论上有吸引力，但受 autoformalization 瓶颈限制，实际覆盖范围可能很窄。贡献 2 是核心 novelty，但二分类器的技术复杂度有限。贡献 3 更像是工程设计选择而非独立贡献。整体来看，这是一个 **方向正确、gap 清晰、但 novelty 量级中等** 的贡献。\n\n【方法合理性】:\n方法整体合理，三层 pipeline 的 cascading 设计逻辑自洽。但需关注以下问题：\n\n1. **更简单的替代方案**: Ablation 6（try-formal-first + neural fallback，即 LogicReward 的策略）是一个非常自然的 trivial baseline。如果 Z3 编译失败即回退到 neural，无需训练 router，只需付出额外的 Z3 尝试开销（millisecond-scale）。Proposal 虽然将其列为 ablation，但未提供任何初步证据表明 learned routing 显著优于此简单策略。这是最大的方法论风险——如果 learned routing 的优势不显著，论文的核心贡献将大打折扣。\n\n2. **Router 训练数据的 circularity**: Router 在 FoVer Z3 verification labels 上训练，但这些 labels 编码的是当前 autoformalization 工具的能力边界，而非步骤的内在 formalizability。换工具后 labels 需要重新生成，router 需要重新训练。这削弱了\"学习 formalizability\"的叙事。\n\n3. **Roundtrip verification 的额外开销**: Layer 2 需要 72B 模型做 autoformalization + back-translation + semantic equivalence check，计算代价不低。在 effective coverage 可能只有 10-20% 的情况下，cost-effectiveness 值得质疑。\n\n4. **神经分支缺乏创新**: Neural branch 直接使用 GenPRM-7B + Platt scaling，没有任何修改。这意味着对于大部分（~80-90%）步骤，系统退化为标准 GenPRM。\n\n【5 维度打分】:\n\n  1. **研究问题: 强** — \n     形式化-only PRM 过于严格 vs. 神经-only PRM 无形式化保证的 gap 在 FoVer、VERGE、LogicReward 的文献中都有明确记载。\"Learned formalizability routing\" 是 VERGE 论文明确指出的 open next step。Miracle step 的形式化检测连接了 RRM 的分类法和 FoVer 的验证能力，是一个有理论价值的组合。研究问题定义清晰，有充分的文献支撑。\n\n  2. **方法与创新: 中** — \n     三层 pipeline 设计合理，但核心 novelty（learned routing classifier）在技术上是标准的 LoRA fine-tuning + binary classification。与 VERGE 相比，从 rule-based → learned 的跨越是真实的，但并非意料之外。与 FIRMA 的 complexity router 相比（虽然目标不同），learned routing 的概念并非全新。条件性形式化保证是好的理论贡献，但 honest coverage reporting 的方法论直接借自 Risk-Controlled Lean-as-Judge，原创成分有限。没有提出新的 autoformalization 方法或新的形式验证技术，主要贡献在于组合和系统设计。Asymmetric threshold 是标准的 cost-sensitive classification，不构成独立贡献。\n\n  3. **实验设计: 强** — \n     这是 proposal 最突出的亮点。7 个 ablation（formal-only, neural-only, random routing, oracle routing, threshold sweep, try-formal-first fallback, label noise analysis）非常全面，特别是 ablation 6 直接测试了最自然的 trivial alternative，ablation 4 给出了性能上限。Baseline 矩阵包括 pure neural (GenPRM, ThinkPRM, R-PRM), pure formal (FoVer), hybrid (VERGE, Naive Hybrid), LLM-as-Judge, compute-matched comparison，覆盖全面。Compute fairness 分析（包含 autoformalization 成本）和 honest coverage reporting 遵循了领域最佳实践（ThinkPRM 的 token-budget paradigm, Risk-Controlled 方法论）。Miracle step detection 的评估有 primary data source (RRM) + proxy (PRMBench) + self-constructed human annotation 的三级方案。唯一的小遗憾是没有对 OOD 场景（如 code reasoning, scientific reasoning beyond GPQA）做更多规划。\n\n  4. **可行性: 强** — \n     计算预算合理：Qwen3-8B LoRA 训练 4-8 H100 GPU-hours，全流程评估 <5 天 on 8×H100。所有核心组件（FoVer 代码、GenPRM 权重、Qwen 系列模型、Z3 solver）均已公开可用。最大的不确定性是 roundtrip verification 的实际通过率和 formal branch 的 effective coverage——但 proposal 已将这些作为实验指标来报告，而非作为必须成功的前提条件。\n\n  5. **写作与呈现: 强** — \n     Proposal 结构清晰、逻辑连贯。Research opportunity 的三条 converging gaps 叙事有说服力。对 autoformalization 局限性的诚实讨论（引用 Risk-Controlled 的具体数据）和对 conditional soundness 的明确界定显示了学术诚实。Related work 覆盖 14+ 篇论文并精确标注了与本工作的区别。技术细节（pipeline 三层、输出 confidence tier 分级）描述精确。一个改进点是：可以更早、更显著地讨论 \"learned routing vs. try-and-fallback 的预期优势\"，以预防最明显的审稿人质疑。\n\n【概率估计】: [28% - 42%] 中位 34%\n\n【估计理由】:\n向上因素：\n- 研究问题定位精准，填补了 VERGE 明确指出的 learned routing gap（+）\n- 实验设计异常完备，ablation 设计直接回应最自然的质疑（+）\n- 对 autoformalization 局限性的诚实处理遵循领域最佳实践（+）\n- 计算预算合理，可行性高（+）\n- 领域热度高，PRM 是当前 reasoning 研究的焦点（+）\n\n向下因素：\n- 核心 novelty（learned binary classifier for routing）技术复杂度有限，可能被视为\"incremental over VERGE\"（-）\n- Formal branch 的 effective soundness coverage 可能仅 10-20%，实际影响力有限（-）\n- 如果 ablation 6（try-formal-first fallback）表现接近 learned router，核心贡献将被严重质疑（-）\n- Neural branch 对大部分步骤直接退化为 GenPRM，系统的实际增量价值可能有限（-）\n- 没有初步实验结果支撑 learned routing 优于 try-and-fallback 的假设（-）\n\n综合判断：这是一篇 solid 但 novelty 中等的工作。在 AAAI 的激烈竞争中，方向正确 + 实验完备但 novelty 不够突出的论文通常处于 borderline 区间。中位 34% 反映了\"质量高于平均投稿但不足以进入上半区\"的定位。\n\n【主要风险】:\n1. **Ablation 6 风险（致命）**: Try-formal-first + neural fallback 是零训练成本的 trivial alternative。如果其性能接近 learned router（差距 <2-3% F1），审稿人将直接判定 learned routing 没有足够的价值，论文的核心贡献不成立。这是最大的单点风险。\n2. **Effective coverage 过低风险（严重）**: 如果 formal branch 最终只覆盖 10-15% 的步骤且这些步骤本身错误率低（形式化步骤通常较简单、错误率较低），那么\"conditional sound miracle detection\" 在最需要检测 miracle steps 的困难步骤上恰恰无能为力——审稿人会质疑条件性保证的实际价值。\n\n【实施评估】:\n  - 计算资源: 单节点 8×H100，训练 <1 天，评估 <5 天。主要成本在 Qwen2.5-Math-72B-Instruct 的 autoformalization 推理（dominant cost）。学术实验室可行。\n  - 数据需求: FoVer ~80K 标签（已公开），ProcessBench/PRMBench（已公开），MATH-500/AIME24（已公开），人工标注 200-300 步骤用于 miracle step 评估 + 100-200 formalizability oracle labels + 200-300 router label noise audit。总人工标注量约 500-800 个样本。\n  - 人工介入: 中等。需要 2-3 名标注员进行 miracle step 标注、formalizability oracle 标注、router label audit，并计算 inter-annotator agreement (Cohen's kappa)。\n  - 训练需求: Qwen3-8B LoRA fine-tuning（轻量）。不需要从头训练大模型。GenPRM-7B 使用预训练权重，不需要额外训练。\n  - 新 Benchmark: 不需要构建全新 benchmark。使用已有 ProcessBench, PRMBench, MATH-500, AIME24, GPQA-Diamond。自建 miracle step 标注集 (200-300 steps) 规模较小。\n  - 预估周期: 6-10 周。Router 训练 1-2 周（含数据准备），Pipeline 集成 1-2 周，全面评估 2-3 周，人工标注并行进行 2-3 周，写作 2 周。AAAI 2026 deadline 前可完成。\n```\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)\n- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)\n- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)\n- [RRM: Curing Miracle Steps](https://arxiv.org/abs/2510.07774)\n- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365)\n- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031)\n- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459)\n- [FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment](https://aclanthology.org/2025.mathnlp-main.5/)\n- [PRoSFI: Structured Formal Intermediaries](https://arxiv.org/abs/2603.29500)\n- [PRMBench: Fine-grained PRM Benchmark](https://prmbench.github.io/)\n- [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Formally-Routed Process Reward Models for Sound Miracle Step Detection\n\n## Core Problem\n\nNo existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) provide high precision but suffer documented overly-strict behavior on informal steps. Neural-only PRMs (GenPRM, ThinkPRM, R-PRM, ARES) provide broad coverage but no formal derivability guarantees. Hybrid systems use either hand-crafted routing (VERGE) or unlearned try-and-fallback (LogicReward). The critical gap: a learned, context-dependent formalizability router that dispatches each step to the appropriate verifier—with roundtrip-verified formal checking providing sound miracle step detection on formalizable steps while neural verification covers the rest.\n\n## Research Opportunity\n\nThree converging gaps create a unique opening:\n\n(1) VERGE (arXiv:2601.20055) demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses rule-based routing over static claim types (logical vs. commonsense)—context-free and not learned. The paper explicitly identifies learned routing as the open next step.\n\n(2) LogicReward (ICLR 2026, arXiv:2512.18196) implements Isabelle step verification with token-probability fallback—a \"try-formal-first\" strategy. This cannot distinguish \"step is intrinsically non-formalizable\" from \"autoformalization failed on a formalizable step,\" producing systematic false alarms on non-formalizable steps (the same overly-strict behavior documented in FoVer).\n\n(3) RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, but never tested formal derivability from predecessors. FoVer's public codebase (arXiv:2505.15960), GenPRM's open weights (arXiv:2504.00891), and Risk-Controlled Lean-as-Judge (arXiv:2605.28365) with its honest quantification of autoformalization limits (43% faithfulness, 28% coverage for 7B autoformalizer on MATH-500) provide infrastructure and calibration data for a hybrid system at academic compute budgets.\n\n## Key Insight: Conditional Formal Soundness for Miracle Detection\n\nA miracle step is an unjustified logical leap—step S_i that does not follow from predecessors {S_1,...,S_{i-1}}. When a step is faithfully formalized and submitted to Z3 for predecessor-derivability checking, miracle steps produce Z3 UNSAT (not derivable). This is near-definitional: on the faithfully-formalized subset, miracle step detection reduces to Z3 derivability failure.\n\nThe critical qualifier is \"faithfully formalized.\" Autoformalization is unreliable: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) reports only 43% faithfulness, and Do LLMs Game Formalization? (arXiv:2604.19459) identifies two unfaithfulness modes—axiom fabrication and premise mistranslation—that evade compilation-based detection. Therefore, the soundness guarantee is conditional: it holds only for steps that pass both formalizability routing AND roundtrip verification of autoformalization faithfulness (arXiv:2604.25031).\n\nFormalRoute-PRM makes this conditionality explicit and operationalizable through a three-layer pipeline: learned formalizability routing → roundtrip faithfulness verification → formal or neural verification.\n\n## Contributions\n\n1. **Conditional sound miracle detection.** On steps that the router identifies as formalizable AND that pass roundtrip faithfulness verification, Z3 predecessor-derivability checking provides guaranteed miracle step detection. This is the first PRM offering formal soundness guarantees for any subset of reasoning steps, with honest coverage reporting following Risk-Controlled methodology.\n\n2. **Learned context-dependent formalizability routing.** Unlike VERGE's static claim-type routing (context-free) and LogicReward's unlearned try-and-fallback, our Qwen3-8B router predicts formalizability conditioned on the full predecessor chain {S_1,...,S_{i-1}}. Context-dependent formalizability prediction is a non-trivial learning problem because a step's formalizability depends on: (a) the formal context established by predecessors (which definitions and variables are already formalized), (b) the autoformalization tool's capability boundary for this step type, and (c) the step's position in the proof (early declarative steps are more formalizable than later heuristic steps). Rule-based approaches cannot capture these context dependencies. Compared to try-and-fallback, learned routing provides three advantages: (i) avoids systematic false alarms from formal verification on non-formalizable steps (FoVer's documented overly-strict behavior), (ii) produces per-step verification confidence signals distinguishing formally guaranteed vs. neurally estimated scores, and (iii) distinguishes intrinsic step formalizability from extrinsic autoformalization capability.\n\n3. **Asymmetric cost-aware routing threshold.** Router errors have asymmetric costs: routing non-formalizable steps to Z3 produces false alarms (overly strict); routing formalizable steps to neural verification risks missing miracle steps. The router threshold is optimized to favor recall (prefer sending to Z3), with explicit cost-asymmetry analysis. This design is informed by FoVer's documented overly-strict behavior and Risk-Controlled Lean-as-Judge's faithfulness quantification.\n\n## Research Landscape\n\n**Formal-only PRMs.** FoVer (ACL 2026, arXiv:2505.15960) achieves 85.8 AUROC on ProcessBench via Z3/Isabelle-verified training labels, but produces overly-strict scores on informal reasoning steps. PRoSFI (arXiv:2603.29500) generates structured formal intermediaries for prover verification on the generation side.\n\n**Neural PRMs.** GenPRM (AAAI 2026, arXiv:2504.00891): 7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification. ThinkPRM (arXiv:2504.16828): 14B trained on only 8K process labels outperforms discriminative PRMs trained on 100× more data; establishes token-budget-normalized comparison paradigm (+7.2% over LLM-as-Judge at same budget). R-PRM (EMNLP 2025, arXiv:2503.21295): +13.9 F1 on ProcessBench and +8.5 F1 on PRMBench via three-stage cold-start, DPO, inference-time scaling. ARES (2025): 72.1% Macro-F1 on PRMBench via autoregressive entailment, entirely dependent on LLM calibration.\n\n**Hybrid systems.** VERGE (arXiv:2601.20055): rule-based semantic routing (logical vs. commonsense claim types) to Z3 or LLM ensemble, 18.7% uplift—routing is static, context-free, not learned. LogicReward (ICLR 2026, arXiv:2512.18196): Isabelle step verification with token-probability fallback; 8B model surpasses GPT-4o by 11.6% on logical reasoning but is an RL training framework, not a standalone PRM. FIRMA (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5): bidirectional formal-informal mathematical language alignment with a complexity router—but this routes for translation quality, not verification correctness; the target function and training signal are fundamentally different from formalizability routing for verification.\n\n**Miracle step detection.** RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, without formal derivability checking.\n\n**Autoformalization limits.** Risk-Controlled Lean-as-Judge (arXiv:2605.28365): 43% faithfulness, 28% coverage for 7B autoformalizer. Do LLMs Game Formalization? (arXiv:2604.19459): identifies axiom fabrication and premise mistranslation as unfaithfulness modes evading compilation checks. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031): provides roundtrip verification methodology for detecting unfaithful formalizations.\n\n## Proposed Approach\n\n**Three-layer pipeline:**\n\n**Layer 1: Formalizability Router.** Qwen3-8B classifier trained on FoVer Z3 verification labels + autoformalization success signals. Labels defined as: formalizable = Z3 compilation success AND roundtrip semantic verification pass; non-formalizable = autoformalization failure OR roundtrip failure OR Z3 timeout. Input: step S_i + predecessor context {S_1,...,S_{i-1}}. Output: formalizability probability. Threshold set via asymmetric cost-aware optimization favoring recall.\n\n**Layer 2: Roundtrip Faithfulness Verification.** Steps routed to formal branch undergo autoformalization (via Qwen2.5-Math-72B-Instruct) → roundtrip verification (arXiv:2604.25031): back-translate the formal statement to natural language and check semantic equivalence with the original step. Steps failing roundtrip verification are redirected to neural branch. This layer gates the soundness guarantee.\n\n**Layer 3: Verification.**\n- Formal branch (roundtrip-verified): Z3 predecessor-derivability checking. Z3 UNSAT → miracle step detected (sound). Z3 SAT → step verified with formal guarantee.\n- Neural branch (non-formalizable or roundtrip-failed): GenPRM-7B scoring with ARES-style calibrated entailment (Platt scaling on held-out validation set). Best-effort verification without formal guarantees.\n\n**Output.** Per-step score with verification confidence tier: (a) roundtrip-verified + Z3-verified (highest confidence), (b) roundtrip-failed but router-formalizable (medium—formal attempt inconclusive), (c) router-non-formalizable + neurally scored (neural confidence), (d) router uncertain (lowest confidence).\n\n## Evaluation Design\n\n**Benchmarks and metrics.**\n- ProcessBench: F1 (aligned with GenPRM, R-PRM) + AUROC (aligned with FoVer)\n- PRMBench (ACL 2025, arXiv:2501.03124): PRMScore + error-type breakdown\n- Best-of-N reranking: MATH-500, AIME24 using Qwen2.5-Math-7B-Instruct as generator; report Pass@1, majority voting, PRM reranking (N=8,16,64)\n- OOD generalization: GPQA-Diamond (scientific reasoning, following ThinkPRM)\n- Miracle step detection: precision/recall/F1 on (a) RRM miracle taxonomy annotations (Yuan et al., 2025) if publicly available, (b) PRMBench error-type categories as primary proxy if RRM data unavailable, (c) self-constructed human-annotated set (200–300 steps, 2–3 annotators, inter-annotator agreement via Cohen's kappa)\n\n**Baseline matrix.**\n- Pure neural: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B\n- Pure formal: FoVer-7B\n- Hybrid: VERGE (hand-crafted routing), Naive Hybrid (FoVer Z3 try-and-fallback to GenPRM, no learned router)\n- LLM-as-Judge: GPT-4o, QwQ-32B\n- Compute-matched: GenPRM majority voting under equivalent total token budget (including autoformalization cost)\n- LogicReward (ICLR 2026): conceptual comparison on method design; quantitative comparison where applicable with methodology differences noted (RL framework vs. standalone PRM)\n\n**Ablation studies.**\n1. Formal-only: all steps → Z3 (low coverage penalty)\n2. Neural-only: all steps → GenPRM (miracle step leakage)\n3. Random routing: 50/50 formal/neural (isolates routing from ensemble)\n4. Oracle routing: ground-truth formalizability labels (performance ceiling)\n5. Router threshold sweep: coverage-accuracy trade-off across formalizability thresholds, visualizing asymmetric cost impact\n6. Try-formal-first + neural fallback: no router, attempt Z3 on all steps, fallback on failure (trivial alternative baseline—directly tests whether learned routing outperforms unlearned try-and-fallback)\n7. Router label noise analysis: compare router trained on noisy auto-labels vs. router trained on human-cleaned labels (500–1000 examples); report label precision via human audit of 200–300 \"non-formalizable\" training labels\n\n**Compute fairness.** Report per-step average inference time and total FLOPs for all systems, explicitly including autoformalization cost (Qwen2.5-Math-72B-Instruct inference) in FormalRoute-PRM's compute. Plot accuracy vs. compute Pareto curve. Compute-matched GenPRM majority voting as explicit comparison following ThinkPRM's token-budget-normalized paradigm.\n\n**Router analysis.** Classification accuracy, precision, recall on in-domain (formal reasoning) and out-of-domain (general math, GPQA-Diamond) splits. Few-shot domain adaptation ablation with ProcessBench/PRMBench samples. Oracle formalizability labels (human-annotated, 100–200 examples) to quantify router quality ceiling. Formalizability positive rate, formal branch coverage, roundtrip verification pass rate per benchmark.\n\n**Honest coverage reporting.** Following Risk-Controlled Lean-as-Judge (arXiv:2605.28365) methodology: report autoformalization coverage, roundtrip faithfulness rate, formal branch activation rate, and effective soundness coverage (= steps receiving formal guarantee / total steps) per benchmark.\n\n## Compute Budget\n\n- Router training: Qwen3-8B LoRA fine-tuning on ~80K FoVer-derived labels, ≈4–8 GPU-hours on single H100\n- Autoformalization: Qwen2.5-Math-72B-Instruct inference for formalizable steps (est. 30–50% of total); dominant compute cost\n- Z3 solving: millisecond-scale per formula, negligible\n- GenPRM-7B inference: standard 7B inference for neural branch steps\n- Roundtrip verification: one additional LLM call per formal-branch step for back-translation + semantic equivalence check\n- Total: training <1 day, full evaluation pipeline <5 days on single-node 8×H100 (dominated by autoformalization inference)\n\n## Key References\n\n- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026, arXiv:2505.15960)\n- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026, arXiv:2504.00891)\n- LogicReward: Step-Wise Logical Supervision (ICLR 2026, arXiv:2512.18196)\n- VERGE: Formal Refinement and Guidance Engine (arXiv 2026, arXiv:2601.20055)\n- Curing Miracle Steps with Rubric Rewards (arXiv 2025, arXiv:2510.07774)\n- Risk-Controlled Lean-as-Judge (arXiv 2026, arXiv:2605.28365)\n- ARES: Autoregressive Entailment Scoring (2025)\n- ThinkPRM: Process Reward Models That Think (arXiv:2504.16828)\n- R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, arXiv:2503.21295)\n- PRMBench: Fine-grained PRM Benchmark (ACL 2025, arXiv:2501.03124)\n- PRoSFI: Structured Formal Intermediaries (arXiv:2603.29500)\n- Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031)\n- FIRMA: Formal-Informal Mathematical Language Alignment (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5)\n- Do LLMs Game Formalization? (arXiv:2604.19459)"
}
````

---

### Runtime record

_source line 2 · 2026-05-29T06:42:48.226Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:42:48.226Z",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-29T06:42:48.243Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make a thorough, evidence-based evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [GenPRM (arXiv:2504.00891)] (AAAI 2026): 直接竞争者。7B generative PRM via CoT + code verification，在 ProcessBench 上超越 Qwen2.5-Math-PRM-72B。开源权重和代码，是 neural branch 的核心组件也是最强 neural baseline。
- [FoVer (arXiv:2505.15960)] (ACL 2026): 直接竞争者/基础组件。Z3/Isabelle 生成 PRM 训练标签，在 12 个推理 benchmark 上泛化性强，但 proposal 正确指出其在 informal reasoning steps 上 overly-strict 的问题。
- [VERGE (arXiv:2601.20055)] (arXiv 2026): 最直接的先驱。Rule-based semantic routing（logical claims → Z3, commonsense → LLM ensemble），18.7% uplift。论文明确指出 learned routing 是 open problem——proposal 的 novelty claim 在此成立。
- [LogicReward (arXiv:2512.18196)] (ICLR 2026): 相关但定位不同。Isabelle step verification + RL training reward，8B 模型超 GPT-4o 11.6%。但它是 RL reward framework，不是 standalone PRM；其 "try-formal-first" 策略确实存在 proposal 所述的 false alarm 问题。
- [ThinkPRM (arXiv:2504.16828)] (arXiv 2025): 强 baseline。仅用 PRM800K 1% 的 process labels 训练，在相同 token budget 下超 LLM-as-Judge 7.2%。其 token-budget-normalized 比较范式是本 proposal 需要满足的实验标准。
- [R-PRM (arXiv:2503.21295)] (EMNLP 2025): +13.9 F1 on ProcessBench via three-stage pipeline (cold-start, DPO, inference scaling)。又一个强 neural baseline。
- [RRM (arXiv:2510.07774)] (withdrawn ICLR 2026): 定义 miracle step taxonomy，RRM 减少 71% miracle steps via rubric rewards。Proposal 的 miracle step detection 概念直接来源于此，但 RRM 从未用 formal derivability——proposal 在此有差异化。
- [Risk-Controlled Lean-as-Judge (arXiv:2605.28365)] (arXiv 2026): 关键参考。报告 7B autoformalizer 仅 43% faithfulness、28% coverage on MATH-500。这是对 proposal 有利也有弊的证据——说明了 honest reporting 的必要性，但也暴露了 formal branch 的有效覆盖率可能很低。
- [Do LLMs Game Formalization? (arXiv:2604.19459)] (arXiv 2026): 识别 axiom fabrication 和 premise mistranslation 两种 unfaithfulness 模式。Proposal 正确引用此作为 roundtrip verification 的动机。
- [PRMBench (arXiv:2501.03124)] (ACL 2025): 标准评测基准。6,216 problems, 83,456 step-level labels。SOTA (Gemini-2-Thinking) 68.8 vs human 83.8，差距仍大。
- 调研总结: PRM 领域 2025-2026 极度活跃，formal/neural/hybrid 三条路线并行发展。VERGE 的 rule-based routing 和 LogicReward 的 try-and-fallback 已经验证了 hybrid 路线的价值，但 **learned context-dependent routing** 确实是一个明确的、被先驱工作显式指出的 open gap。Proposal 精准定位了这个缝隙。然而，autoformalization 的低 faithfulness (43%) 和低 coverage (28%) 对 formal branch 的实际价值构成根本性约束。

【整体印象】:
作为审稿人，第一反应是：这是一份 **异常成熟的 proposal**，文献梳理之细致、positioning 之精准、实验设计之完备在 proposal 阶段是罕见的。作者显然对 PRM 领域有深入理解，且诚实地面对了 autoformalization 的局限性（这是加分项）。

但同时会有两个顾虑浮上来：
1. **核心贡献的 "系统集成" 味道较重**——每个组件（Z3 验证、roundtrip verification、GenPRM neural scoring、LoRA router）都是已有的，创新主要在组装方式和 learned routing 上。这在 AAAI 审稿中可能被视为 incremental。
2. **"Conditional soundness" 的实际覆盖率可能很低**——如果 7B autoformalizer 只有 28% coverage × 43% faithfulness ≈ 12% effective soundness coverage（即使用 72B 模型可能提升到 20-30%），审稿人会质疑："对 12-30% 的 steps 有 formal guarantee，对整体 PRM 性能提升有多大？"

倾向：**borderline**，在 weak accept 和 weak reject 之间。实验设计的完备性是显著加分项，但 novelty 和 practical impact 的疑虑需要强实验结果来弥补。

【核心贡献】:
1. **Learned context-dependent formalizability routing**——区别于 VERGE 的 rule-based 和 LogicReward 的 unlearned try-and-fallback，这是一个明确的 technical contribution，但量级偏轻（本质是一个分类器）。
2. **Conditional sound miracle step detection**——概念上干净（formally verified subset 上 Z3 UNSAT = miracle step），但 practical coverage 受 autoformalization 瓶颈严重限制。
3. **Three-layer pipeline 的系统设计**——完整的 routing + faithfulness gating + hybrid verification，带 asymmetric cost-aware threshold。

对领域的价值：如果 learned routing 能显著优于 VERGE 和 try-and-fallback（>3-5% 提升），且 formal branch 在 miracle step detection 上有明显 precision 优势，这对 PRM 社区有 solid 的参考价值。但如果提升有限，贡献就偏薄。

【方法合理性】:
方法整体 **逻辑自洽且合理**。Three-layer pipeline 的设计有清晰的因果链：routing 解决 "该不该送 formal"，roundtrip verification 解决 "formal translation 是否忠实"，Z3/GenPRM 解决 "步骤是否正确"。Asymmetric cost-aware threshold 是合理的工程考量。

**更简单的替代方案是否能达到类似效果？** 这是最大的方法论风险：
- **Try-and-fallback baseline**（proposal 自己列为 Ablation #6）可能与 learned routing 差距不大。如果 Z3 返回 timeout/error 的速度足够快，fallback 的额外成本可能很低，learned routing 的优势就不明显。
- **GenPRM majority voting at equivalent compute**（proposal 列为 compute-matched baseline）可能在整体 F1 上接近甚至超过 hybrid system，因为 formal branch 的低覆盖率限制了其贡献。
- Proposal 设计了这两个关键 baseline，说明作者意识到了这些风险，这本身是加分项——但实验结果需要 beat 这些 baseline，否则 "learned routing" 的价值就不成立。

【5 维度打分】:

1. **研究问题**: 【中偏强】
   理由：Learned formalizability routing 是一个真实的 open problem（VERGE 论文显式指出），问题动机清晰。但问题的 impact 受 autoformalization 瓶颈约束——即使 routing 完美，formal branch 的有效覆盖率也可能很低（Risk-Controlled Lean-as-Judge 报告 28% coverage, 43% faithfulness），这限制了整体方法在 end-to-end PRM 任务上的潜在提升空间。问题有研究价值，但不是 high-impact 级别。

2. **方法与创新**: 【中】
   理由：与 VERGE 的 rule-based routing 和 LogicReward 的 try-and-fallback 相比，learned context-dependent routing 是一个 clear next step，但 novelty 量级偏轻——核心创新归结为 "用 Qwen3-8B LoRA 训练一个二分类器"。每个组件（Z3 verification from FoVer, roundtrip verification from arXiv:2604.25031, GenPRM for neural branch, Platt scaling from ARES）都是已有工作。"Conditional soundness" 概念虽然干净，但更像是对已知事实的形式化表述而非新发现。与 GenPRM（generative CoT + code verification, AAAI 2026）、ThinkPRM（data-efficient + token-budget scaling）相比，本 proposal 的 methodological novelty 偏弱。

3. **实验设计**: 【强】
   理由：这是 proposal 最突出的亮点。(a) Benchmark 选择全面覆盖（ProcessBench F1/AUROC + PRMBench PRMScore + Best-of-N on MATH-500/AIME24 + OOD GPQA-Diamond + miracle step detection）。(b) Baseline 矩阵极为完整，包含 pure neural (GenPRM, ThinkPRM, R-PRM), pure formal (FoVer), hybrid (VERGE, naive hybrid), LLM-as-Judge (GPT-4o, QwQ-32B)，以及关键的 **compute-matched GenPRM majority voting**（遵循 ThinkPRM 的 token-budget-normalized paradigm）。(c) 7 项 ablation 设计周全，特别是 Ablation #6 (try-formal-first fallback) 直接测试 learned routing vs. unlearned fallback，Ablation #4 (oracle routing) 给出 performance ceiling。(d) Honest coverage reporting following Risk-Controlled methodology。(e) Router quality analysis 含 human-annotated oracle labels。这套实验方案如果执行到位，足以回答所有可能的审稿人质疑。

4. **可行性**: 【中偏强】
   理由：Compute budget 合理（training <1 day, evaluation <5 days on 8×H100）。主要组件都有开源实现（FoVer, GenPRM, Z3）。但以下风险值得注意：(a) Pipeline 涉及 5+ 个独立模块（Qwen3-8B router, Qwen2.5-Math-72B autoformalization, roundtrip verification, Z3 solver, GenPRM-7B），集成调试复杂度高。(b) Autoformalization 使用 Qwen2.5-Math-72B-Instruct，这是 dominant compute cost，且 72B 模型的推理成本在学术环境中不低。(c) Router training labels 的质量依赖 FoVer pipeline 的输出，label noise 可能影响 router 性能（proposal 有 Ablation #7 分析此问题，是好的）。(d) Miracle step 评测数据可能不公开（RRM 被 withdrawn），需要自建 human annotation（200-300 steps）。总体可行但有执行风险。

5. **写作与呈现**: 【强】
   理由：Proposal 的组织极为清晰——Problem → Opportunity → Insight → Contributions → Landscape → Approach → Evaluation，逻辑链完整。文献定位精准，每个竞争者的优劣势都有具体引用支撑。"Conditional soundness" 的概念表述很干净。Asymmetric cost analysis 有说服力。唯一的小瑕疵是 proposal 篇幅偏长，实际论文需要大幅压缩。

【概率估计】: [28% - 40%] 中位 34%

【估计理由】:
**上界 (40%)**: 如果实验结果显示 (a) learned routing 显著优于 try-and-fallback 和 VERGE (>3% F1 on ProcessBench), (b) formal branch 在 miracle step detection 上有明显 precision 优势 (>10% precision lift), (c) compute-matched comparison 中 FormalRoute-PRM 胜出，且 (d) effective formal coverage 达到 25%+——那么"learned routing + conditional soundness"的双重贡献足够支撑一篇 solid 的 AAAI 投稿。实验设计的完备性本身就是显著加分项，论文质量会高于平均 submission。

**下界 (28%)**: 如果 (a) try-and-fallback baseline 与 learned routing 差距很小 (<2%), (b) compute-matched GenPRM majority voting 整体性能接近或超过 FormalRoute-PRM, (c) effective formal coverage 只有 10-15%——审稿人会认为 "用一个分类器做 routing" 的 novelty 不足以支撑 top venue，尤其是与 GenPRM (AAAI 2026) 和 ThinkPRM 这些更 clean 的 contribution 相比。

**中位 (34%)**: 最可能的情况是 learned routing 有一定优势但不显著，formal branch 在 miracle step precision 上有可测量的提升但 coverage 有限。论文的 contribution 会被认为 "solid but somewhat incremental"——well-executed engineering of a known direction（VERGE 已经指出了这个方向）。AAAI 审稿人对 "系统集成" 类工作的接受阈值相对较高，需要令人信服的实验结果来弥补 novelty 的不足。

**关键不确定性**: 这个 proposal 的中稿概率异常依赖实验结果——如果 learned routing 和 conditional soundness 的实际收益超出预期，概率可以提升到 40%+；如果收益平平，会跌到 25% 左右。Proposal 本身的质量在同档竞争者中偏上，但 novelty 天花板限制了上限。

【主要风险】:
1. **"Incremental integration" 质疑**：每个组件（Z3, GenPRM, roundtrip verification, LoRA classifier）都是已有的，核心创新归结为训练一个路由分类器。如果 learned routing vs. try-and-fallback 的提升有限，审稿人很可能判定 novelty 不足。这是最可能的 reject 理由。
2. **Formal branch 的 effective coverage 过低导致 practical impact 存疑**：基于 Risk-Controlled Lean-as-Judge 的数据（28% coverage, 43% faithfulness），即使用 72B autoformalizer，effective soundness coverage 可能仅 20-30%。审稿人会问："对 20% 的 steps 有 formal guarantee，对 end-to-end Best-of-N reranking 的提升到底有多少？这个 guarantee 值不值得 72B autoformalization 的额外 compute cost？"

【实施评估】:
  - 计算资源: 单节点 8×H100，training <1 day, evaluation <5 days。主要开销在 Qwen2.5-Math-72B-Instruct autoformalization inference（约占 70% compute）。学术可行但不宽裕。
  - 数据需求: FoVer 公开数据 (~80K labels) 用于 router training；ProcessBench, PRMBench, MATH-500, AIME24, GPQA-Diamond 均为公开 benchmark；miracle step annotation 需自建 200-300 例 (2-3 annotators)。
  - 人工介入: (a) Router label audit: 200-300 examples human review; (b) Miracle step annotation: 200-300 steps, 2-3 annotators + Cohen's kappa; (c) Oracle formalizability labels: 100-200 examples. 总人工量中等。
  - 训练需求: Qwen3-8B LoRA fine-tuning (~4-8 GPU-hours)，GenPRM-7B 和 Qwen2.5-Math-72B 使用现有权重无需额外训练。训练量很轻。
  - 新 Benchmark: 不需要构建全新 benchmark，但需要自建 miracle step human annotation set (200-300 steps)。
  - 预估周期: Pipeline 搭建 2-3 周 + Router training & tuning 1 周 + Full evaluation 2-3 周 + 论文写作 2-3 周 ≈ **7-10 周** (若顺利)。考虑到多模块集成调试可能遇到的问题，留 **10-12 周** 更保险。
```

Sources:
- [GenPRM: Scaling Test-Time Compute of PRMs via Generative Reasoning (AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055)
- [LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision (ICLR 2026)](https://arxiv.org/abs/2512.18196)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025)](https://arxiv.org/abs/2503.21295)
- [RRM: Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](https://arxiv.org/abs/2605.28365)
- [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/abs/2604.19459)
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)](https://arxiv.org/abs/2501.03124)
- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)
- [Awesome-Process-Reward-Models GitHub](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough field context to conduct a thorough evaluation. Let me compile the full assessment.

---

```
【阶段】: Triage

【领域调研】:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960) (ACL 2026 Findings): 直接前置工作。用Z3/Isabelle生成PRM训练标签，ProcessBench上85.8 AUROC，但在非形式化步骤上存在documented overly-strict behavior。本proposal的formal branch和router训练标签直接依赖FoVer。
- [GenPRM: Scaling Test-Time Compute of PRMs via Generative Reasoning](https://arxiv.org/abs/2504.00891) (AAAI 2026): 本proposal neural branch的核心组件。7B模型超越Qwen2.5-Math-PRM-72B，是当前最强neural PRM之一。被本proposal作为neural verifier使用。
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 最直接的竞争者/前驱工作。rule-based semantic routing（逻辑 vs. 常识claim）分派到Z3或neural ensemble，取得18.7% uplift。论文明确指出"learned routing"是open next step——本proposal正好填补这一空白。
- [LogicReward](https://arxiv.org/abs/2512.18196) (ICLR 2026): Isabelle step verification + token-probability fallback，8B模型在逻辑推理上超GPT-4o 11.6%。是RL训练框架而非standalone PRM，其try-and-fallback策略正是本proposal要改进的routing机制。
- [Curing Miracle Steps with Rubric Rewards (RRM)](https://arxiv.org/abs/2510.07774) (arXiv 2025, withdrawn ICLR 2026): 定义了miracle step分类法，通过rubric rewards减少71% miracle steps，但未使用formal derivability检测。本proposal将miracle step概念与formal verification结合。
- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365) (arXiv 2026): 关键校准数据来源。7B autoformalizer在MATH-500上仅43% faithfulness、28% coverage。本proposal的honest coverage reporting methodology直接源于此工作。
- [ThinkPRM](https://arxiv.org/abs/2504.16828) (arXiv 2025): 14B模型仅用8K process labels训练，建立了token-budget-normalized比较范式。本proposal的compute-matched comparison直接参考其方法论。
- [R-PRM](https://arxiv.org/abs/2503.21295) (EMNLP 2025): ProcessBench上+13.9 F1，PRMBench上+8.5 F1，三阶段训练pipeline。重要baseline。
- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459) (arXiv 2026): 识别axiom fabrication和premise mistranslation两种unfaithfulness模式，为roundtrip verification的必要性提供理论依据。
- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031) (arXiv 2026): 本proposal Layer 2的方法论来源。

- **调研总结**: PRM领域2025-2026处于快速发展期，formal PRM（FoVer）和neural PRM（GenPRM/ThinkPRM/R-PRM）各有明确优势和局限，hybrid系统（VERGE/LogicReward）已验证了formal+neural组合的价值但routing机制粗糙。本proposal定位于"learned formalizability routing"这一被VERGE明确标识为open problem的空白，时机准确，但面临核心贡献被视为"工程组合"的风险。搜索未发现任何已有的learned formalizability routing工作，novelty claim在当前文献中成立。

【整体印象】:
作为审稿人，我的第一反应是：这是一篇定位非常精准、文献综述极为扎实、实验设计异常完备的proposal，作者对领域的理解深度令人印象深刻。"Conditional formal soundness"的概念框架诚实且有智识吸引力——不回避autoformalization的局限性，反而将其显式建模。

然而，我会有两个核心疑虑：(1) 核心贡献是否足够"新"——learned router + existing formal verifier + existing neural verifier的组合，每个组件都来自已有工作，novelty主要在于组合方式和router的学习；(2) formal soundness guarantee的实际覆盖率可能非常窄——如果autoformalization faithfulness仅43%、coverage仅28%，经过router + roundtrip verification双重过滤后，能获得formal guarantee的步骤可能仅占总步骤的10-15%，这使得"sound miracle step detection"的实际影响被大幅稀释。

倾向：**weak accept / borderline**——方向正确、执行方案扎实，但需要实验证明learned routing显著优于简单的try-and-fallback baseline，且formal branch的实际覆盖率足以产生meaningful impact。

【核心贡献】:
核心贡献是**learned context-dependent formalizability routing**——一个经过训练的分类器，根据步骤及其前驱上下文预测该步骤是否可以被faithfully formalized，从而将其分派到formal（Z3）或neural（GenPRM）验证路径。配合roundtrip faithfulness verification，在正式验证的子集上提供sound miracle step detection。

对领域的价值评估：
- **填补真实空白**: VERGE明确标识learned routing为open problem，LogicReward的try-and-fallback策略有documented局限性。这不是一个人造的gap。
- **conditional soundness framing**: 将形式化验证的保证与autoformalization的局限性显式关联，提供了一个intellectually honest的分析框架，这对后续hybrid PRM的设计有指导意义。
- **但贡献的"重量"取决于实验结果**: 如果learned router相比try-and-fallback仅有marginal improvement，或formal branch的effective coverage过低，则贡献会显得单薄。

【方法合理性】:
方法总体合理，三层pipeline设计逻辑清晰：

**合理之处:**
1. Router → Roundtrip → Verification的层次设计，每层有明确功能和失败模式处理。
2. Asymmetric cost-aware threshold是一个thoughtful设计选择，反映了对FoVer overly-strict behavior的正确理解。
3. 使用Qwen3-8B作为router（轻量）+ Qwen2.5-Math-72B-Instruct作为autoformalizer（强力）的分工合理。

**潜在问题:**
1. **更简单的替代方案**: "try-formal-first + neural fallback"（ablation #6）是最直接的竞争方案。如果Z3 timeout足够快，这个trivial baseline可能接近learned routing的效果——因为autoformalization失败或Z3 timeout会自然地将non-formalizable步骤redirect到neural branch。Proposal已预见到这一点并设置了专门ablation，这很好，但如果实验中learned routing的优势不显著，整个工作的价值会被大幅削弱。
2. **Router训练标签的noise**: FoVer Z3 labels + autoformalization success signals本身是noisy的（Risk-Controlled的43% faithfulness数据）。Router trained on noisy labels → router本身的precision/recall可能不理想。Ablation #7（label noise analysis）是正确的实验，但500-1000 human-cleaned examples可能不够。
3. **Roundtrip verification的可靠性**: 依赖LLM进行back-translation + semantic equivalence check——这本身也是一个noisy过程，可能引入新的failure modes。

**总结**: 方法合理但不算elegant——是对已有组件的工程化组合。没有看到更简单的替代方案能直接替代整个pipeline，但try-and-fallback是一个需要convincingly beat的baseline。

【5 维度打分】:

1. **研究问题: 中偏强** — Learned formalizability routing是VERGE明确标识的open problem，且formal-neural hybrid PRM是一个真实且活跃的研究方向。Miracle step detection具有practical importance（RRM的71%减少表明这是一个real problem）。扣分点：研究问题的"规模"相对较小——这是一个specific routing mechanism的改进，而非paradigm shift。

2. **方法与创新: 中** — Novelty在于将formalizability prediction建模为learned classification problem，并引入conditional soundness framing。但每个组件（Z3 verification from FoVer, GenPRM for neural scoring, roundtrip verification from arXiv:2604.25031, miracle step concept from RRM）都直接来自已有工作，创新主要在于组合和routing mechanism。与VERGE（rule-based routing, 18.7% uplift）相比，learned routing是自然但incremental的改进。与LogicReward（try-and-fallback）相比，显式routing避免了false alarms——但这一优势需要实验量化。搜索结果确认无已有learned formalizability routing工作，novelty claim成立，但contribution weight取决于实验中learned vs. unlearned routing的delta。

3. **实验设计: 强** — 这是本proposal最突出的优势。Baseline matrix非常全面（neural: GenPRM/ThinkPRM/R-PRM/Qwen2.5-Math-PRM-72B; formal: FoVer; hybrid: VERGE + Naive Hybrid; LLM-as-Judge: GPT-4o/QwQ-32B; compute-matched: GenPRM majority voting）。7项ablation设计精准，特别是ablation #6（try-formal-first baseline）和ablation #4（oracle routing ceiling）直接回答了最关键的问题。Compute fairness reporting（含autoformalization cost）和honest coverage reporting展示了methodological rigor。唯一不足：miracle step detection的benchmark不确定（RRM数据可能不公开），self-constructed set仅200-300 steps偏小。

4. **可行性: 中偏强** — Compute budget realistic（单节点8×H100，训练<1天，评估<5天）。所有组件都有公开实现（FoVer开源、GenPRM有open weights）。主要风险：(a) Qwen2.5-Math-72B-Instruct的autoformalization推理成本是dominant cost，可能限制实验throughput；(b) router训练标签的构建需要大量autoformalization预处理；(c) roundtrip verification的semantic equivalence checking可能需要额外调优。总体而言，方案在学术团队的资源范围内可执行。

5. **写作与呈现: 强** — Proposal结构清晰，论证有力。Research landscape部分对每个prior work的定位精准，关键差异点清晰标注。"Key Insight"部分对conditional soundness的推导逻辑严密。Contributions的表述不over-claim——"first PRM offering formal soundness guarantees for any subset"的措辞恰当。对局限性的处理（autoformalization faithfulness问题、coverage limitations）诚实且前置。唯一不足：pipeline的复杂性可能在实际论文中需要更好的可视化/figure设计来辅助理解。

【概率估计】: [28% - 40%] 中位 34%

【估计理由】:
**上行因素 (→40%)**:
- 填补VERGE明确标识的open problem，时机精准
- 实验设计异常完备，显示了高度的methodological awareness
- PRM是2025-2026热门方向，AAAI对此类工作有需求
- Conditional soundness framing在intellectually honest的同时具有新颖性
- 如果learned routing显著beat try-and-fallback，且formal branch effective coverage达到20%+，论文将非常convincing

**下行因素 (→28%)**:
- 核心贡献可能被视为existing components的工程组合，novelty depth不足
- Formal soundness的effective coverage可能过窄（~10-15%），稀释实际impact
- AAAI 2026竞争激烈，同领域（PRM/verification）可能有多篇投稿
- 如果learned routing vs. try-and-fallback的margin较小，核心卖点不成立

**中位34%的推理**: 这是一篇well-positioned、technically sound、experimentally thorough的proposal，处于"有实质贡献但缺乏突出亮点"到"整体扎实"的交界区间。最终命运很大程度取决于两个关键实验结果：(1) learned routing vs. try-and-fallback的performance gap，(2) formal branch的effective soundness coverage。在结果未知的情况下，给予略高于baseline acceptance rate的估计。

【主要风险】:
1. **Learned routing可能无法显著超越try-and-fallback**: 如果Z3 timeout足够快（millisecond级，proposal中也提到），try-formal-first策略可以自然地将non-formalizable步骤redirect到neural branch，使得learned router的added value marginal。这将直接瓦解contribution #2（learned routing的三个优势）。
2. **Formal branch的effective soundness coverage过低**: 经过router过滤 → autoformalization → roundtrip verification三层筛选后，获得formal guarantee的步骤可能仅占总步骤的极小比例（<15%），使得"sound miracle step detection"更像一个theoretical contribution而非practical improvement——reviewers可能质疑"为了验证15%的步骤值得引入这么复杂的pipeline吗？"

【实施评估】:
  - 计算资源: 单节点8×H100，合理。Dominant cost是Qwen2.5-Math-72B-Instruct的autoformalization推理，估计约3-4天（假设30-50%步骤进入formal branch，跨多个benchmark）
  - 数据需求: FoVer-80K公开数据用于router训练；ProcessBench、PRMBench、MATH-500、AIME24、GPQA-Diamond均为公开benchmark；需自建200-300步human-annotated miracle step数据集
  - 人工介入: (a) 200-300步miracle step标注（2-3名标注员+Cohen's kappa），约2-3人天；(b) 200-300条router训练标签人工审核，约1-2人天；(c) 100-200条oracle formalizability标注，约1人天。总计约5-8人天。
  - 训练需求: Qwen3-8B LoRA fine-tuning（4-8 GPU-hours），轻量级。无需训练GenPRM或autoformalization模型（使用现有权重）。
  - 新 Benchmark: 不需要构建新benchmark。需要自建小规模miracle step标注集（200-300步）作为补充评估，但非full benchmark。
  - 预估周期: Router训练1天 + Pipeline集成与调试3-5天 + 全量评估5天 + 消融实验5-7天 + 人工标注与分析3-5天 + 论文写作2-3周 = **总计约6-8周**（单人）或**4-5周**（2-3人团队）
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)
- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [PRMBench: Fine-grained PRM Benchmark](https://arxiv.org/abs/2501.03124)
- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459)
- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960) (ACL 2026): 直接前序工作。使用 Z3/Isabelle 合成 PRM 训练标签，ProcessBench 上 85.8 AUROC。文档化了在非形式化推理步骤上的"过于严格"行为——这正是本 proposal 试图解决的问题。提供公开代码和数据集。
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 最直接竞争者。规则化语义路由（逻辑 vs. 常识 claim type）到 Z3 或 LLM ensemble，18.7% 性能提升。路由是静态的、基于 claim type 的、非学习的。论文明确指出 learned routing 是开放的下一步——本 proposal 正是回应这一 gap。
- [LogicReward](https://arxiv.org/abs/2512.18196) (ICLR 2026): Isabelle step verification + token-probability fallback。8B 模型超越 GPT-4o 11.6%。但其"先尝试形式化、失败则回退"策略无法区分"步骤本质上不可形式化"与"自动形式化在可形式化步骤上失败"——正是 proposal 所批评的缺陷。
- [GenPRM](https://arxiv.org/abs/2504.00891) (AAAI 2026): 生成式 PRM，7B 超越 Qwen2.5-Math-PRM-72B。开源权重。本 proposal 将其用作 neural branch 的 backbone。
- [ThinkPRM](https://arxiv.org/abs/2504.16828) (arXiv 2025): 14B 模型仅用 8K 过程标签即超越 100× 数据训练的判别式 PRM。建立了 token-budget-normalized 比较范式——proposal 引用此范式做 compute fairness 分析。
- [R-PRM](https://arxiv.org/abs/2503.21295) (EMNLP 2025): ProcessBench +13.9 F1，PRMBench +8.5 F1，三阶段训练。本 proposal 将其列为 baseline。
- [RRM: Curing Miracle Steps](https://arxiv.org/abs/2510.07774) (arXiv 2025, withdrawn from ICLR 2026): 定义 miracle step 分类法，通过 rubric rewards 减少 71% miracle steps。未测试形式化可推导性——proposal 的 miracle detection 贡献直接建立在此基础之上。
- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365) (arXiv 2026): 7B autoformalizer 仅 43% faithfulness、28% coverage。该论文提供了量化 autoformalization 局限的校准数据和 honest coverage reporting 方法论——proposal 的"条件性形式化保证"直接受此启发。
- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031) (arXiv 2026): Roundtrip verification 将 formal equivalence 从 45-61% 提升到 83-85%。本 proposal 的 Layer 2 直接采用此方法。
- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459) (arXiv 2026): 识别出 axiom fabrication 和 premise mistranslation 两种 unfaithfulness 模式。为 proposal 的 roundtrip verification 层提供了理论动机。
- [FIRMA](https://aclanthology.org/2025.mathnlp-main.5/) (MathNLP 2025): 复杂度感知路由做 formal-informal 翻译。Proposal 正确指出其目标函数（翻译质量）与 formalizability routing for verification 根本不同。
- [PRoSFI](https://arxiv.org/abs/2603.29500) (arXiv 2026): 结构化形式中间体用于 prover verification，偏向 generation side。

- **调研总结**: PRM 领域正处于从纯判别式向生成式/混合式快速演进的阶段。形式化验证（FoVer, VERGE, LogicReward）已被证明有效但受限于覆盖率和过度严格问题。"学习化路由"是 VERGE 明确指出的开放问题，目前确实没有工作实现了 learned context-dependent formalizability routing。但 autoformalization 的低可靠性（43% faithfulness）构成了系统性瓶颈。Proposal 在这一 landscape 中定位清晰，但其条件性保证的实际覆盖范围可能受限。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇 **定位精准、技术叙事清晰、实验设计异常完备** 的 proposal。作者对领域的掌握非常深入，VERGE 的 static routing → learned routing 的 gap 真实存在且被原论文明确指出。三层 pipeline（routing → roundtrip verification → formal/neural dispatch）逻辑自洽，honest coverage reporting 的设计哲学也令人欣赏。

然而，我的倾向会是 **borderline（偏向 weak accept / borderline reject）**。原因如下：
1. 核心贡献——learned formalizability routing——在技术上是一个相对直接的二分类器（Qwen3-8B LoRA fine-tuned on FoVer labels），novelty 天花板有限。
2. 受制于 autoformalization 的低可靠性（43% faithfulness, 28% coverage），formal branch 的"effective soundness coverage"可能仅覆盖 10-20% 的步骤，条件性保证的实际影响力存疑。
3. 如果 ablation 6（try-formal-first + neural fallback）表现接近 learned router，整个贡献基础将被削弱。

【核心贡献】:
1. **Conditional sound miracle detection**: 在 router 判定为 formalizable 且 roundtrip verification 通过的步骤子集上，Z3 predecessor-derivability 检查提供有保证的 miracle step 检测。这是第一个对推理步骤子集提供形式化正确性保证的 PRM。
2. **Learned context-dependent formalizability routing**: 不同于 VERGE 的静态 claim type routing 和 LogicReward 的 try-and-fallback，使用 Qwen3-8B 预测依赖前驱链上下文的 formalizability。
3. **Asymmetric cost-aware routing threshold**: 显式建模路由错误的不对称代价。

**贡献价值评估**: 贡献 1 在理论上有吸引力，但受 autoformalization 瓶颈限制，实际覆盖范围可能很窄。贡献 2 是核心 novelty，但二分类器的技术复杂度有限。贡献 3 更像是工程设计选择而非独立贡献。整体来看，这是一个 **方向正确、gap 清晰、但 novelty 量级中等** 的贡献。

【方法合理性】:
方法整体合理，三层 pipeline 的 cascading 设计逻辑自洽。但需关注以下问题：

1. **更简单的替代方案**: Ablation 6（try-formal-first + neural fallback，即 LogicReward 的策略）是一个非常自然的 trivial baseline。如果 Z3 编译失败即回退到 neural，无需训练 router，只需付出额外的 Z3 尝试开销（millisecond-scale）。Proposal 虽然将其列为 ablation，但未提供任何初步证据表明 learned routing 显著优于此简单策略。这是最大的方法论风险——如果 learned routing 的优势不显著，论文的核心贡献将大打折扣。

2. **Router 训练数据的 circularity**: Router 在 FoVer Z3 verification labels 上训练，但这些 labels 编码的是当前 autoformalization 工具的能力边界，而非步骤的内在 formalizability。换工具后 labels 需要重新生成，router 需要重新训练。这削弱了"学习 formalizability"的叙事。

3. **Roundtrip verification 的额外开销**: Layer 2 需要 72B 模型做 autoformalization + back-translation + semantic equivalence check，计算代价不低。在 effective coverage 可能只有 10-20% 的情况下，cost-effectiveness 值得质疑。

4. **神经分支缺乏创新**: Neural branch 直接使用 GenPRM-7B + Platt scaling，没有任何修改。这意味着对于大部分（~80-90%）步骤，系统退化为标准 GenPRM。

【5 维度打分】:

  1. **研究问题: 强** — 
     形式化-only PRM 过于严格 vs. 神经-only PRM 无形式化保证的 gap 在 FoVer、VERGE、LogicReward 的文献中都有明确记载。"Learned formalizability routing" 是 VERGE 论文明确指出的 open next step。Miracle step 的形式化检测连接了 RRM 的分类法和 FoVer 的验证能力，是一个有理论价值的组合。研究问题定义清晰，有充分的文献支撑。

  2. **方法与创新: 中** — 
     三层 pipeline 设计合理，但核心 novelty（learned routing classifier）在技术上是标准的 LoRA fine-tuning + binary classification。与 VERGE 相比，从 rule-based → learned 的跨越是真实的，但并非意料之外。与 FIRMA 的 complexity router 相比（虽然目标不同），learned routing 的概念并非全新。条件性形式化保证是好的理论贡献，但 honest coverage reporting 的方法论直接借自 Risk-Controlled Lean-as-Judge，原创成分有限。没有提出新的 autoformalization 方法或新的形式验证技术，主要贡献在于组合和系统设计。Asymmetric threshold 是标准的 cost-sensitive classification，不构成独立贡献。

  3. **实验设计: 强** — 
     这是 proposal 最突出的亮点。7 个 ablation（formal-only, neural-only, random routing, oracle routing, threshold sweep, try-formal-first fallback, label noise analysis）非常全面，特别是 ablation 6 直接测试了最自然的 trivial alternative，ablation 4 给出了性能上限。Baseline 矩阵包括 pure neural (GenPRM, ThinkPRM, R-PRM), pure formal (FoVer), hybrid (VERGE, Naive Hybrid), LLM-as-Judge, compute-matched comparison，覆盖全面。Compute fairness 分析（包含 autoformalization 成本）和 honest coverage reporting 遵循了领域最佳实践（ThinkPRM 的 token-budget paradigm, Risk-Controlled 方法论）。Miracle step detection 的评估有 primary data source (RRM) + proxy (PRMBench) + self-constructed human annotation 的三级方案。唯一的小遗憾是没有对 OOD 场景（如 code reasoning, scientific reasoning beyond GPQA）做更多规划。

  4. **可行性: 强** — 
     计算预算合理：Qwen3-8B LoRA 训练 4-8 H100 GPU-hours，全流程评估 <5 天 on 8×H100。所有核心组件（FoVer 代码、GenPRM 权重、Qwen 系列模型、Z3 solver）均已公开可用。最大的不确定性是 roundtrip verification 的实际通过率和 formal branch 的 effective coverage——但 proposal 已将这些作为实验指标来报告，而非作为必须成功的前提条件。

  5. **写作与呈现: 强** — 
     Proposal 结构清晰、逻辑连贯。Research opportunity 的三条 converging gaps 叙事有说服力。对 autoformalization 局限性的诚实讨论（引用 Risk-Controlled 的具体数据）和对 conditional soundness 的明确界定显示了学术诚实。Related work 覆盖 14+ 篇论文并精确标注了与本工作的区别。技术细节（pipeline 三层、输出 confidence tier 分级）描述精确。一个改进点是：可以更早、更显著地讨论 "learned routing vs. try-and-fallback 的预期优势"，以预防最明显的审稿人质疑。

【概率估计】: [28% - 42%] 中位 34%

【估计理由】:
向上因素：
- 研究问题定位精准，填补了 VERGE 明确指出的 learned routing gap（+）
- 实验设计异常完备，ablation 设计直接回应最自然的质疑（+）
- 对 autoformalization 局限性的诚实处理遵循领域最佳实践（+）
- 计算预算合理，可行性高（+）
- 领域热度高，PRM 是当前 reasoning 研究的焦点（+）

向下因素：
- 核心 novelty（learned binary classifier for routing）技术复杂度有限，可能被视为"incremental over VERGE"（-）
- Formal branch 的 effective soundness coverage 可能仅 10-20%，实际影响力有限（-）
- 如果 ablation 6（try-formal-first fallback）表现接近 learned router，核心贡献将被严重质疑（-）
- Neural branch 对大部分步骤直接退化为 GenPRM，系统的实际增量价值可能有限（-）
- 没有初步实验结果支撑 learned routing 优于 try-and-fallback 的假设（-）

综合判断：这是一篇 solid 但 novelty 中等的工作。在 AAAI 的激烈竞争中，方向正确 + 实验完备但 novelty 不够突出的论文通常处于 borderline 区间。中位 34% 反映了"质量高于平均投稿但不足以进入上半区"的定位。

【主要风险】:
1. **Ablation 6 风险（致命）**: Try-formal-first + neural fallback 是零训练成本的 trivial alternative。如果其性能接近 learned router（差距 <2-3% F1），审稿人将直接判定 learned routing 没有足够的价值，论文的核心贡献不成立。这是最大的单点风险。
2. **Effective coverage 过低风险（严重）**: 如果 formal branch 最终只覆盖 10-15% 的步骤且这些步骤本身错误率低（形式化步骤通常较简单、错误率较低），那么"conditional sound miracle detection" 在最需要检测 miracle steps 的困难步骤上恰恰无能为力——审稿人会质疑条件性保证的实际价值。

【实施评估】:
  - 计算资源: 单节点 8×H100，训练 <1 天，评估 <5 天。主要成本在 Qwen2.5-Math-72B-Instruct 的 autoformalization 推理（dominant cost）。学术实验室可行。
  - 数据需求: FoVer ~80K 标签（已公开），ProcessBench/PRMBench（已公开），MATH-500/AIME24（已公开），人工标注 200-300 步骤用于 miracle step 评估 + 100-200 formalizability oracle labels + 200-300 router label noise audit。总人工标注量约 500-800 个样本。
  - 人工介入: 中等。需要 2-3 名标注员进行 miracle step 标注、formalizability oracle 标注、router label audit，并计算 inter-annotator agreement (Cohen's kappa)。
  - 训练需求: Qwen3-8B LoRA fine-tuning（轻量）。不需要从头训练大模型。GenPRM-7B 使用预训练权重，不需要额外训练。
  - 新 Benchmark: 不需要构建全新 benchmark。使用已有 ProcessBench, PRMBench, MATH-500, AIME24, GPQA-Diamond。自建 miracle step 标注集 (200-300 steps) 规模较小。
  - 预估周期: 6-10 周。Router 训练 1-2 周（含数据准备），Pipeline 集成 1-2 周，全面评估 2-3 周，人工标注并行进行 2-3 周，写作 2 周。AAAI 2026 deadline 前可完成。
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)
- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [RRM: Curing Miracle Steps](https://arxiv.org/abs/2510.07774)
- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365)
- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031)
- [Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459)
- [FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment](https://aclanthology.org/2025.mathnlp-main.5/)
- [PRoSFI: Structured Formal Intermediaries](https://arxiv.org/abs/2603.29500)
- [PRMBench: Fine-grained PRM Benchmark](https://prmbench.github.io/)
- [Awesome Process Reward Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)


【原始 proposal（允许参考但不是主要依据）】:
# Formally-Routed Process Reward Models for Sound Miracle Step Detection

## Core Problem

No existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) provide high precision but suffer documented overly-strict behavior on informal steps. Neural-only PRMs (GenPRM, ThinkPRM, R-PRM, ARES) provide broad coverage but no formal derivability guarantees. Hybrid systems use either hand-crafted routing (VERGE) or unlearned try-and-fallback (LogicReward). The critical gap: a learned, context-dependent formalizability router that dispatches each step to the appropriate verifier—with roundtrip-verified formal checking providing sound miracle step detection on formalizable steps while neural verification covers the rest.

## Research Opportunity

Three converging gaps create a unique opening:

(1) VERGE (arXiv:2601.20055) demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses rule-based routing over static claim types (logical vs. commonsense)—context-free and not learned. The paper explicitly identifies learned routing as the open next step.

(2) LogicReward (ICLR 2026, arXiv:2512.18196) implements Isabelle step verification with token-probability fallback—a "try-formal-first" strategy. This cannot distinguish "step is intrinsically non-formalizable" from "autoformalization failed on a formalizable step," producing systematic false alarms on non-formalizable steps (the same overly-strict behavior documented in FoVer).

(3) RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, but never tested formal derivability from predecessors. FoVer's public codebase (arXiv:2505.15960), GenPRM's open weights (arXiv:2504.00891), and Risk-Controlled Lean-as-Judge (arXiv:2605.28365) with its honest quantification of autoformalization limits (43% faithfulness, 28% coverage for 7B autoformalizer on MATH-500) provide infrastructure and calibration data for a hybrid system at academic compute budgets.

## Key Insight: Conditional Formal Soundness for Miracle Detection

A miracle step is an unjustified logical leap—step S_i that does not follow from predecessors {S_1,...,S_{i-1}}. When a step is faithfully formalized and submitted to Z3 for predecessor-derivability checking, miracle steps produce Z3 UNSAT (not derivable). This is near-definitional: on the faithfully-formalized subset, miracle step detection reduces to Z3 derivability failure.

The critical qualifier is "faithfully formalized." Autoformalization is unreliable: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) reports only 43% faithfulness, and Do LLMs Game Formalization? (arXiv:2604.19459) identifies two unfaithfulness modes—axiom fabrication and premise mistranslation—that evade compilation-based detection. Therefore, the soundness guarantee is conditional: it holds only for steps that pass both formalizability routing AND roundtrip verification of autoformalization faithfulness (arXiv:2604.25031).

FormalRoute-PRM makes this conditionality explicit and operationalizable through a three-layer pipeline: learned formalizability routing → roundtrip faithfulness verification → formal or neural verification.

## Contributions

1. **Conditional sound miracle detection.** On steps that the router identifies as formalizable AND that pass roundtrip faithfulness verification, Z3 predecessor-derivability checking provides guaranteed miracle step detection. This is the first PRM offering formal soundness guarantees for any subset of reasoning steps, with honest coverage reporting following Risk-Controlled methodology.

2. **Learned context-dependent formalizability routing.** Unlike VERGE's static claim-type routing (context-free) and LogicReward's unlearned try-and-fallback, our Qwen3-8B router predicts formalizability conditioned on the full predecessor chain {S_1,...,S_{i-1}}. Context-dependent formalizability prediction is a non-trivial learning problem because a step's formalizability depends on: (a) the formal context established by predecessors (which definitions and variables are already formalized), (b) the autoformalization tool's capability boundary for this step type, and (c) the step's position in the proof (early declarative steps are more formalizable than later heuristic steps). Rule-based approaches cannot capture these context dependencies. Compared to try-and-fallback, learned routing provides three advantages: (i) avoids systematic false alarms from formal verification on non-formalizable steps (FoVer's documented overly-strict behavior), (ii) produces per-step verification confidence signals distinguishing formally guaranteed vs. neurally estimated scores, and (iii) distinguishes intrinsic step formalizability from extrinsic autoformalization capability.

3. **Asymmetric cost-aware routing threshold.** Router errors have asymmetric costs: routing non-formalizable steps to Z3 produces false alarms (overly strict); routing formalizable steps to neural verification risks missing miracle steps. The router threshold is optimized to favor recall (prefer sending to Z3), with explicit cost-asymmetry analysis. This design is informed by FoVer's documented overly-strict behavior and Risk-Controlled Lean-as-Judge's faithfulness quantification.

## Research Landscape

**Formal-only PRMs.** FoVer (ACL 2026, arXiv:2505.15960) achieves 85.8 AUROC on ProcessBench via Z3/Isabelle-verified training labels, but produces overly-strict scores on informal reasoning steps. PRoSFI (arXiv:2603.29500) generates structured formal intermediaries for prover verification on the generation side.

**Neural PRMs.** GenPRM (AAAI 2026, arXiv:2504.00891): 7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification. ThinkPRM (arXiv:2504.16828): 14B trained on only 8K process labels outperforms discriminative PRMs trained on 100× more data; establishes token-budget-normalized comparison paradigm (+7.2% over LLM-as-Judge at same budget). R-PRM (EMNLP 2025, arXiv:2503.21295): +13.9 F1 on ProcessBench and +8.5 F1 on PRMBench via three-stage cold-start, DPO, inference-time scaling. ARES (2025): 72.1% Macro-F1 on PRMBench via autoregressive entailment, entirely dependent on LLM calibration.

**Hybrid systems.** VERGE (arXiv:2601.20055): rule-based semantic routing (logical vs. commonsense claim types) to Z3 or LLM ensemble, 18.7% uplift—routing is static, context-free, not learned. LogicReward (ICLR 2026, arXiv:2512.18196): Isabelle step verification with token-probability fallback; 8B model surpasses GPT-4o by 11.6% on logical reasoning but is an RL training framework, not a standalone PRM. FIRMA (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5): bidirectional formal-informal mathematical language alignment with a complexity router—but this routes for translation quality, not verification correctness; the target function and training signal are fundamentally different from formalizability routing for verification.

**Miracle step detection.** RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, without formal derivability checking.

**Autoformalization limits.** Risk-Controlled Lean-as-Judge (arXiv:2605.28365): 43% faithfulness, 28% coverage for 7B autoformalizer. Do LLMs Game Formalization? (arXiv:2604.19459): identifies axiom fabrication and premise mistranslation as unfaithfulness modes evading compilation checks. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031): provides roundtrip verification methodology for detecting unfaithful formalizations.

## Proposed Approach

**Three-layer pipeline:**

**Layer 1: Formalizability Router.** Qwen3-8B classifier trained on FoVer Z3 verification labels + autoformalization success signals. Labels defined as: formalizable = Z3 compilation success AND roundtrip semantic verification pass; non-formalizable = autoformalization failure OR roundtrip failure OR Z3 timeout. Input: step S_i + predecessor context {S_1,...,S_{i-1}}. Output: formalizability probability. Threshold set via asymmetric cost-aware optimization favoring recall.

**Layer 2: Roundtrip Faithfulness Verification.** Steps routed to formal branch undergo autoformalization (via Qwen2.5-Math-72B-Instruct) → roundtrip verification (arXiv:2604.25031): back-translate the formal statement to natural language and check semantic equivalence with the original step. Steps failing roundtrip verification are redirected to neural branch. This layer gates the soundness guarantee.

**Layer 3: Verification.**
- Formal branch (roundtrip-verified): Z3 predecessor-derivability checking. Z3 UNSAT → miracle step detected (sound). Z3 SAT → step verified with formal guarantee.
- Neural branch (non-formalizable or roundtrip-failed): GenPRM-7B scoring with ARES-style calibrated entailment (Platt scaling on held-out validation set). Best-effort verification without formal guarantees.

**Output.** Per-step score with verification confidence tier: (a) roundtrip-verified + Z3-verified (highest confidence), (b) roundtrip-failed but router-formalizable (medium—formal attempt inconclusive), (c) router-non-formalizable + neurally scored (neural confidence), (d) router uncertain (lowest confidence).

## Evaluation Design

**Benchmarks and metrics.**
- ProcessBench: F1 (aligned with GenPRM, R-PRM) + AUROC (aligned with FoVer)
- PRMBench (ACL 2025, arXiv:2501.03124): PRMScore + error-type breakdown
- Best-of-N reranking: MATH-500, AIME24 using Qwen2.5-Math-7B-Instruct as generator; report Pass@1, majority voting, PRM reranking (N=8,16,64)
- OOD generalization: GPQA-Diamond (scientific reasoning, following ThinkPRM)
- Miracle step detection: precision/recall/F1 on (a) RRM miracle taxonomy annotations (Yuan et al., 2025) if publicly available, (b) PRMBench error-type categories as primary proxy if RRM data unavailable, (c) self-constructed human-annotated set (200–300 steps, 2–3 annotators, inter-annotator agreement via Cohen's kappa)

**Baseline matrix.**
- Pure neural: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B
- Pure formal: FoVer-7B
- Hybrid: VERGE (hand-crafted routing), Naive Hybrid (FoVer Z3 try-and-fallback to GenPRM, no learned router)
- LLM-as-Judge: GPT-4o, QwQ-32B
- Compute-matched: GenPRM majority voting under equivalent total token budget (including autoformalization cost)
- LogicReward (ICLR 2026): conceptual comparison on method design; quantitative comparison where applicable with methodology differences noted (RL framework vs. standalone PRM)

**Ablation studies.**
1. Formal-only: all steps → Z3 (low coverage penalty)
2. Neural-only: all steps → GenPRM (miracle step leakage)
3. Random routing: 50/50 formal/neural (isolates routing from ensemble)
4. Oracle routing: ground-truth formalizability labels (performance ceiling)
5. Router threshold sweep: coverage-accuracy trade-off across formalizability thresholds, visualizing asymmetric cost impact
6. Try-formal-first + neural fallback: no router, attempt Z3 on all steps, fallback on failure (trivial alternative baseline—directly tests whether learned routing outperforms unlearned try-and-fallback)
7. Router label noise analysis: compare router trained on noisy auto-labels vs. router trained on human-cleaned labels (500–1000 examples); report label precision via human audit of 200–300 "non-formalizable" training labels

**Compute fairness.** Report per-step average inference time and total FLOPs for all systems, explicitly including autoformalization cost (Qwen2.5-Math-72B-Instruct inference) in FormalRoute-PRM's compute. Plot accuracy vs. compute Pareto curve. Compute-matched GenPRM majority voting as explicit comparison following ThinkPRM's token-budget-normalized paradigm.

**Router analysis.** Classification accuracy, precision, recall on in-domain (formal reasoning) and out-of-domain (general math, GPQA-Diamond) splits. Few-shot domain adaptation ablation with ProcessBench/PRMBench samples. Oracle formalizability labels (human-annotated, 100–200 examples) to quantify router quality ceiling. Formalizability positive rate, formal branch coverage, roundtrip verification pass rate per benchmark.

**Honest coverage reporting.** Following Risk-Controlled Lean-as-Judge (arXiv:2605.28365) methodology: report autoformalization coverage, roundtrip faithfulness rate, formal branch activation rate, and effective soundness coverage (= steps receiving formal guarantee / total steps) per benchmark.

## Compute Budget

- Router training: Qwen3-8B LoRA fine-tuning on ~80K FoVer-derived labels, ≈4–8 GPU-hours on single H100
- Autoformalization: Qwen2.5-Math-72B-Instruct inference for formalizable steps (est. 30–50% of total); dominant compute cost
- Z3 solving: millisecond-scale per formula, negligible
- GenPRM-7B inference: standard 7B inference for neural branch steps
- Roundtrip verification: one additional LLM call per formal-branch step for back-translation + semantic equivalence check
- Total: training <1 day, full evaluation pipeline <5 days on single-node 8×H100 (dominated by autoformalization inference)

## Key References

- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026, arXiv:2505.15960)
- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026, arXiv:2504.00891)
- LogicReward: Step-Wise Logical Supervision (ICLR 2026, arXiv:2512.18196)
- VERGE: Formal Refinement and Guidance Engine (arXiv 2026, arXiv:2601.20055)
- Curing Miracle Steps with Rubric Rewards (arXiv 2025, arXiv:2510.07774)
- Risk-Controlled Lean-as-Judge (arXiv 2026, arXiv:2605.28365)
- ARES: Autoregressive Entailment Scoring (2025)
- ThinkPRM: Process Reward Models That Think (arXiv:2504.16828)
- R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, arXiv:2503.21295)
- PRMBench: Fine-grained PRM Benchmark (ACL 2025, arXiv:2501.03124)
- PRoSFI: Structured Formal Intermediaries (arXiv:2603.29500)
- Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031)
- FIRMA: Formal-Informal Mathematical Language Alignment (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5)
- Do LLMs Game Formalization? (arXiv:2604.19459)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9d92336b-4b67-4495-b11c-d78567b3bd4f",
  "type": "user",
  "uuid": "60df7b25-128c-4356-b302-e8b5c727f0d8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:42:48.241Z_

```json
{
  "parentUuid": "60df7b25-128c-4356-b302-e8b5c727f0d8",
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
  "uuid": "e0625422-cf59-4d3d-aade-9b05dc601ab1",
  "timestamp": "2026-05-29T06:42:48.241Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:42:48.241Z_

```json
{
  "parentUuid": "e0625422-cf59-4d3d-aade-9b05dc601ab1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "13d81cee-4b8b-43fd-b769-7d13e493fb30",
  "timestamp": "2026-05-29T06:42:48.241Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a thorough, evidence-ba…",
  "leafUuid": "13d81cee-4b8b-43fd-b769-7d13e493fb30",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate hybrid formal-neural PRM proposal",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:43:13.958Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews carefully to produce a Meta Judge synthesis.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Probability: [28% - 40%] 中位 34%
- Research Problem: 中偏强
- Method & Innovation: 中
- Experimental Design: 强
- Feasibility: 中偏强
- Writing: 强
- Main risks: Incremental integration, low effective coverage

**Reviewer 2:**
- Probability: [28% - 40%] 中位 34%


- Research Problem: 中偏强
- Method & Innovation: 中
- Experimental Design: 强
- Feasibility: 中偏强
- Writing: 强
- Main risks: Learned routing vs try-and-fallback, effective coverage too low

**Reviewer 3:**
- Probability: [28% - 42%] 中位 34%
- Research Problem: 强
- Method & Innovation: 中
- Experimental Design: 强
- Feasibility: 强
- Writing: 强
- Main risks: Ablation 6 risk, effective coverage too low

All three reviewers converged on a 34% median probability, with consistent assessments across most dimensions. The main divergence appears in Research Problem strength and Feasibility, where Reviewer 3 rates both higher, while the risk profiles show some variation in specific concerns though effective coverage emerges as a shared worry. The outliers are minor — R3 is slightly more generous on both Research Problem and Feasibility, and mentions a unique concern about router training data circularity that the others don't flag. With standard deviation near zero across all three reviewers' median scores of 34%, the consensus is remarkably tight, so I'll anchor to the median range of 28-40% and narrow slightly from there.

Now looking at the implementation assessment, there's strong alignment on the computational requirements — 8 H100s with training under a day and evaluation under five days, where the 72B autoformalization dominates costs. The data side needs roughly 80K public examples from FoVer plus standard benchmarks, supplemented by 200-300 human-annotated miracle steps. The human effort lands around 5-8 person-days for annotations, using lightweight LoRA fine-tuning. Timeline estimates cluster around 6-10 weeks depending on the reviewer, with some suggesting 4-5 weeks as an optimistic floor and 10-12 weeks as a safer buffer.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13d81cee-4b8b-43fd-b769-7d13e493fb30",
  "isSidechain": false,
  "requestId": "req_011CbWQVDsxWKMPp6czhe9HP",
  "type": "assistant",
  "uuid": "e9b386e4-4f04-4719-ab4a-0e2fa8c4e2bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZzxnAMPCZQ8uF8AizJmmv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20987,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3187,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20987
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

_source line 9 · 2026-05-29T06:43:59.936Z_

【阶段】: Meta Judge
【三次中位】: [34%, 34%, 34%]  std=0%
【共识维度】:
- **方法与创新 = 中**（3/3 一致）：核心 novelty 归结为 learned binary classifier (LoRA fine-tuned Qwen3-8B)，每个组件均来自已有工作（Z3 from FoVer, GenPRM for neural, roundtrip from arXiv:2604.25031, miracle step concept from RRM），创新主要在组合方式和 routing mechanism。三位审稿人均认为从 VERGE rule-based → learned 的跨越真实但量级有限。
- **实验设计 = 强**（3/3 一致）：7 项 ablation 设计（特别是 #6 try-formal-first fallback 和 #4 oracle routing ceiling）、全面的 baseline 矩阵、compute fairness 分析、honest coverage reporting 均被三位审稿人高度评价，一致认为这是 proposal 最突出的亮点。
- **写作与呈现 = 强**（3/3 一致）：文献定位精准、结构清晰、conditional soundness 表述干净、对局限性的诚实讨论。
- **致命风险 #1：Ablation 6 (try-and-fallback) 威胁**（3/3 一致）：如果 learned routing 与零训练成本的 try-formal-first + neural fallback 差距 <2-3% F1，核心贡献不成立。这是三位审稿人一致认定的最大单点风险。
- **致命风险 #2：Formal branch effective coverage 过低**（3/3 一致）：基于 Risk-Controlled Lean-as-Judge 数据（43% faithfulness, 28% coverage），经三层过滤后 effective soundness coverage 可能仅 10-20%，对 end-to-end 性能提升存疑。
- **研究问题 = 中偏强**（2/3，R1+R2）：VERGE 明确标识的 open problem，gap 真实，但 impact 受 autoformalization 瓶颈约束。
- **可行性 = 中偏强**（2/3，R1+R2）：计算预算合理，核心组件公开可用，但多模块集成调试复杂度和 72B autoformalization 推理成本构成执行风险。

【异常维度】:
- R3 将研究问题评为 **强**（R1/R2 为中偏强）：R3 更重视 VERGE 论文对 learned routing 的显式呼吁和 miracle step 检测的理论价值。但 R1/R2 的 "impact 受 autoformalization 瓶颈约束" 论点更有说服力，降权 R3 的上调。
- R3 将可行性评为 **强**（R1/R2 为中偏强）：R3 对多模块集成风险的评估偏乐观。R1 明确提到 "5+ 独立模块集成调试复杂度高"，更符合工程现实。
- R3 独有提出 **router 训练数据 circularity**（训练标签编码的是当前 autoformalization 工具的能力边界而非步骤的内在 formalizability）：这是一个有效的概念层面质疑，但并非致命——proposal 的 ablation #7 (label noise analysis) 部分回应了此问题。标记为次要风险。

【最终概率】: [28% - 40%] 中位 34%
【一致性】: 高（std=0%，三位审稿人概率中位完全一致，rubric 维度判决高度趋同）
【综合理由】:

三位审稿人展现出极为罕见的高度一致：概率中位均为 34%，下界均为 28%，上界仅 R3 微幅上调至 42%（R1/R2 均为 40%）。五个 rubric 维度中，方法与创新（中）、实验设计（强）、写作（强）三个维度 3/3 完全一致；研究问题和可行性仅 R3 各上调一档，但其上调理由不足以推翻 R1/R2 的共识。

**核心共识画像**：这是一篇"方向正确、定位精准、实验设计异常完备，但 novelty 天花板受限于核心贡献本质是已有组件的工程化组合"的 borderline 工作。概率高度依赖实验结果——learned routing vs. try-and-fallback 的 delta 和 formal branch effective coverage 是两个决定性变量。

**处理异常**：R3 在研究问题和可行性上的上调（各一档）被降权处理，因为 (a) R1/R2 的"autoformalization 瓶颈约束 impact"论点有具体数据支撑（43% faithfulness, 28% coverage），(b) R1 的"5+ 模块集成复杂度"更符合工程常识。R3 的 router circularity 质疑作为补充风险点纳入，但不影响概率估计。

**最终区间取法**：高一致性下取共识区间 [28%-40%]，中位保持 34%。未采纳 R3 的 42% 上界，因为在方法创新仅为"中"的前提下，即使实验结果理想，40% 是更合理的天花板。

【建议】: 边缘

【实施评估】:
  - 计算资源: 单节点 8×H100。训练 <1 天（Qwen3-8B LoRA fine-tuning, 4-8 GPU-hours）。全量评估 <5 天。Dominant cost 为 Qwen2.5-Math-72B-Instruct autoformalization 推理（约占总 compute 70%），这是主要的资源瓶颈。学术实验室可行但不宽裕。
  - 数据需求: FoVer ~80K 标签（公开可得）用于 router 训练；ProcessBench、PRMBench、MATH-500、AIME24、GPQA-Diamond 均为公开 benchmark。需自建 miracle step 人工标注集（200-300 steps）。
  - 人工介入: 中等。(a) Miracle step 标注 200-300 steps，2-3 名标注员 + Cohen's kappa，约 2-3 人天；(b) Router label noise audit 200-300 examples，约 1-2 人天；(c) Oracle formalizability labels 100-200 examples，约 1 人天。总计约 5-8 人天。
  - 训练需求: 仅 Qwen3-8B LoRA fine-tuning（轻量级）。GenPRM-7B 和 Qwen2.5-Math-72B-Instruct 使用现有预训练权重，无需额外训练。训练负担极轻。
  - 新 Benchmark: 不需要构建全新 benchmark。使用已有公开 benchmark。仅需自建小规模 miracle step 标注集（200-300 steps）作为补充评估。
  - 预估周期: Pipeline 搭建与集成调试 2-3 周 + Router 训练与调优 1 周 + 全量评估与消融实验 2-3 周 + 人工标注（可并行）2-3 周 + 论文写作 2-3 周 ≈ **7-10 周**（单人）或 **5-7 周**（2-3 人团队）。留 10-12 周更保险，考虑多模块集成可能遇到的工程问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9b386e4-4f04-4719-ab4a-0e2fa8c4e2bc",
  "isSidechain": false,
  "requestId": "req_011CbWQVDsxWKMPp6czhe9HP",
  "type": "assistant",
  "uuid": "7dd1340a-79aa-48a0-9407-c192bc0ce42e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZzxnAMPCZQ8uF8AizJmmv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20987,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3187,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20987
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a thorough, evidence-ba…",
  "leafUuid": "7dd1340a-79aa-48a0-9407-c192bc0ce42e",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate hybrid formal-neural PRM proposal",
  "sessionId": "d5b3a5f8-6648-4b68-9731-b0731efe8e68"
}
```

---
