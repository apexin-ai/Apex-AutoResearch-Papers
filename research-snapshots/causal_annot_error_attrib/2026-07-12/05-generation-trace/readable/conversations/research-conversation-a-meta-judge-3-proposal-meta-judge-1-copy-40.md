# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/0d9dc1d8-a93d-4f65-9e25-a8684efdf74c.jsonl`
- **Structured JSON:** [`e0062849a71992e144bf.json`](../../sessions/e0/e0062849a71992e144bf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:47:14.308Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:47:14.308Z",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to produce the evaluation. Let me synthesize my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Wan et al., \"Mitigating Conversational Inertia in Multi-Turn Agents\"](https://arxiv.org/abs/2602.03664) (ICML 2026): 本 proposal 的核心依赖。提出 diagonal attention 与 CPL 干预，但仅在 agentic task performance 上验证，从未评估 safety 效果。Aggregate-level 分析，无 per-head decomposition。代码未公开。\n- [Li et al., \"DETAM\"](https://arxiv.org/abs/2504.13562) (ACL 2025 Findings): 推理时 attention reallocation 防御，ASR 46%→1.2%，建立了 attention 再分配→safety 提升的因果证据。但限于 single-turn，需 runtime 识别 intent tokens。\n- [Park et al., \"ASGuard\"](https://arxiv.org/abs/2509.25843) (ICLR 2026): 训练时 circuit-targeted head scaling，ASR 42%→8%，识别 Layer 13 的 4 个 vulnerable heads。但针对特定可定位的攻击电路，非 discourse-level 动态。\n- [Zhou et al., \"On the Role of Attention Heads in LLM Safety\"](https://arxiv.org/abs/2410.13708) (ICLR 2025): 单个 safety head 消融即可使 harmful queries 应答增加 16×，safety head 分布高度模型依赖。本 proposal 的 Phase 0.5 cross-validation 依据之一。\n- [Dongre et al., \"When Attention Closes\"](https://arxiv.org/abs/2605.12922) (arXiv 2026.05): 提出 GAR 度量 multi-turn attention 衰减，发现 architecture-dependent failure modes。非常新的工作（2026年5月），与本 proposal 互补。\n- [Yang et al., \"MT-AgentRisk / ToolShield\"](https://unsafer-in-many-turns.github.io/) (arXiv 2026): 365-task multi-turn safety benchmark + inference-time defense（ASR 降低 ~30%）。本 proposal 的主要评测平台。\n- [Lu et al., \"X-Boundary\"](https://arxiv.org/abs/2502.09990) (EMNLP 2025): Representation-level boundaries，ASR 58.5%→16.5%。本 proposal 的直接 baseline 之一。\n- [Guo et al., \"MTSA\"](https://arxiv.org/abs/2505.17147) (ACL 2025): RL-based multi-turn alignment，ASR 74.5%→23.5%。另一个重要 baseline。\n- **调研中未发现直接竞争工作**：没有任何已发表或 arXiv 工作测试过\"untargeted discourse training → safety improvement via attention reallocation\"这一路径。per-head diagonal attention decomposition 和 attention capacity flow mapping 确实是未被做过的。\n\n- 调研总结: multi-turn safety 是一个快速增长的领域，2025-2026年涌现了大量攻击、防御和机理分析工作，但均在\"直接用 safety 数据训练\"或\"推理时干预\"范式内。本 proposal 提出的\"untargeted discourse training 间接改善 safety\"路径确实是一个未被探索的空白，核心 novelty claim 成立。\n\n【整体印象】:\n作为审稿人，我的第一反应是：这是一个极其雄心勃勃、文献调研深入、实验设计严谨的 proposal，核心研究问题（untargeted discourse 训练能否通过 attention reallocation 因果性地改善 multi-turn safety）是真正新颖的。然而，我也会立即产生两个担忧：(1) scope 过于庞大——5+ phases、8 conditions、4 种 head identification 方法、3-level hypothesis 框架、多个 benchmark，这对一篇论文来说可能过度；(2) 核心假设高度投机性——没有任何初步证据表明 CPL 会影响 safety，整个 5-phase 研究建立在一个未验证的 bridge hypothesis 之上。总体倾向：**borderline**，如果执行良好且结果清晰，有可能 accept；但执行风险高，呈现不当则很容易 reject。\n\n【核心贡献】:\n1. **首个因果性测试**：untargeted discourse training (CPL) 是否通过 attention reallocation 机制改善 multi-turn safety——这是一个干净、未被探索的研究问题。\n2. **方法论贡献**：per-head diagonal attention decomposition（首次）、attention capacity flow mapping（首次）、四方法 safety head 对比——这些无论主假设结果如何都有独立价值。\n3. **Paradigm-controlled comparison**：CPL vs. XGuard-DPO（同一 DPO 框架、不同数据源）实现训练范式与数据来源的解耦，实验设计巧妙。\n\n贡献价值评估：如果主假设成立（CPL 确实通过 attention reallocation 改善 safety），这将是一个高影响力发现，连接了 discourse quality 和 safety 两个独立的研究方向。即使主假设不成立，方法论贡献仍有中等价值。但单靠方法论贡献（per-head decomposition 等）撑不起一篇 top venue 论文——需要有实质性的正面或负面发现。\n\n【方法合理性】:\n方法整体合理，有几个亮点和隐患：\n\n**亮点：**\n- Manipulation check 设计：先验证 CPL 是否降低了 diagonal attention，再解释 safety 效果——这是标准的因果推断方法论，很多 ML 论文忽略这一步。\n- Double dissociation 设计：CPL (discourse data + DPO) vs. XGuard-DPO (safety data + DPO) 可以分离数据源和训练范式的效果。\n- 多种控制条件（Random-Preference LoRA, Reversed-CPL）排除 trivial 解释。\n\n**隐患：**\n- **CPL 复现是最大风险**：代码未公开，需要复现 dual-rollout preference pair construction pipeline on AgentGym。如果复现的 CPL 效果不好，整个研究的因果推断基础就不牢固。\n- **Three-level framework 的可证伪性存疑**：Level 1/2/3 覆盖了所有可能的结果——高重叠是 Level 1，中等是 Level 2，低重叠是 Level 3——这使得假设几乎不可能被否证。一个好的因果假设应该有明确的否定条件。\n- **更简单的替代方案**：是否可以直接在 CPL 前后对比 DETAM 的 Focus Loss 指标，而不需要如此复杂的多 phase 设计？很多 phase 的贡献可以被更简洁的实验替代。\n- **Preference pair 分布差异**：CPL 和 XGuard-DPO 的 preference margin 分布不同是 proposal 自己承认的 limitation，但这直接影响 double dissociation 的解释力。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】— \"untargeted discourse training 能否因果性地改善 multi-turn safety\" 是一个干净、新颖、有价值的研究问题。它连接了两个独立发展的研究线（discourse quality / safety alignment），且有明确的实际意义（如果成立，意味着可以通过改善对话质量间接提高安全性，无需昂贵的 safety-specific 数据标注）。调研确认该问题未被任何已有工作回答。\n\n2. 方法与创新: 【中偏强】— 核心创新点（将 CPL 应用于 safety 评估 + per-head decomposition + capacity flow mapping）是真正新颖的，调研中未发现直接竞争工作。实验设计中的 manipulation check、paradigm-controlled comparison、double dissociation 体现了强方法论素养。但 Three-level framework 的可证伪性不足，且 CPL 本身不是本工作的贡献（是 Wan et al. 的方法），本工作更多是在\"应用+分析\"层面。与 DETAM（推理时）、ASGuard（训练时 targeted）、X-Boundary（representation level）相比，本工作的方法论 delta 主要在分析框架而非新算法。\n\n3. 实验设计: 【强】— 这是本 proposal 最突出的优点之一。8 个实验条件（含控制组）、paradigm-matched comparison、manipulation check、turn-count dose-response、多 benchmark（MT-AgentRisk + OpenAgentSafety + MultiBreak 子集）、over-refusal 评测、capability preservation（MMLU + MT-Bench）、hyperparameter sensitivity、multiple evaluation protocols（GPT-4o judge + rule-based + inter-method agreement）。与领域内已有工作相比（DETAM 仅 single-turn benchmark、ASGuard 4 个模型但 single-turn、X-Boundary 无 dose-response），本 proposal 的实验设计显著更全面。样本量和统计功效分析也到位。Null-result 策略有 9 个独立贡献点，比大多数 proposal 考虑得周到。\n\n4. 可行性: 【中】— 资源需求合理（~1000-1200 A100-hours，$1500-1800），timeline 有缓冲。但存在关键风险：(a) CPL 复现依赖未公开代码和 AgentGym 环境搭建；(b) 16-18 周的 timeline 意味着如果目标是 EMNLP 2026（通常 deadline 在 2026 年 6 月左右），时间上不可行——proposal 本身目标是 ICLR 2027（2026年9月）；(c) 整体 scope 极大，5 个 phase 中任何一个延迟都会级联影响后续；(d) \"联系 Wan et al. 获取 checkpoint\" 是不确定性极高的依赖。\n\n5. 写作与呈现: 【中偏弱】— Proposal 本身信息密度极高、文献引用详尽，体现了深入的领域理解。但同时也暴露了呈现风险：(a) 过度堆砌——一个 proposal 引用了 40+ 篇论文，几乎每一句都有 citation，这在实际论文中会让审稿人疲劳；(b) 核心 story 被埋没在大量细节中——\"untargeted discourse training → safety via attention reallocation\" 这个简洁的核心叙事被 five-phase design、three-level framework、quadruple-method triangulation 等复杂设计淹没；(c) 8 页 EMNLP 论文中很难容纳如此多的内容，必须大幅精简；(d) 某些术语（如\"quadruple triangulation\"、\"attention capacity competition hypothesis\"）增加了不必要的认知负担。\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】:\n- **上行因素 (→38%)**：核心 novelty 真正成立（调研确认无竞争工作）；研究问题重要且 timely；实验设计严谨程度超过领域平均水平；即使负面结果也有方法论贡献。如果执行良好、写作精炼、结果清晰，有实力进入 borderline accept 区间。\n- **下行因素 (→25%)**：核心假设高度投机、无初步证据支撑，审稿人可能认为这是 \"fishing expedition\"；scope 过大导致论文展开不充分或审稿人无法 follow；CPL 复现失败的实际可能性；three-level framework 的不可证伪性可能被审稿人视为方法论弱点；presentation 过于复杂的风险。\n- **中位推理 (30%)**：在 EMNLP 2026 的安全 / 可解释性 track 中，这个 novelty 水平和实验设计深度属于\"above average submission but with significant execution risk\"。领域内已有大量 multi-turn safety 工作（X-Boundary、MTSA、MUSE-D 等），竞争激烈。如果实验结果干净（CPL 确实降低 inertia 且改善 safety），则 30% 偏上界；如果实验结果混杂（CPL 降低 inertia 但 safety 改善不显著，或改善可归因于 DPO 训练本身），则 30% 偏下界。\n\n【主要风险】:\n1. **核心假设落空 + 方法论贡献不足以独立支撑**：如果 CPL 未能有效降低 safety 任务上的 diagonal attention，或降低后 safety 无显著改善，剩下的 per-head decomposition 和 capacity flow mapping 虽有新颖性，但在独立性和影响力上可能不足以支撑一篇 top venue 论文——审稿人可能评价为 \"interesting analysis but no actionable insight\"。\n2. **Scope 过大导致论文不聚焦**：5+ phases、8 conditions、4 种 head identification 方法、3-level framework 在 8 页正文中难以清晰展开。审稿人极可能抱怨 \"too many moving parts\"、\"hard to follow the main contribution\"，甚至怀疑作者是否真的能在有限篇幅内充分呈现所有实验结果和分析。\n\n【实施评估】:\n  - 计算资源: ~980-1200 A100-hours（约 $1500-1800），对于有 GPU 集群访问的研究组是合理的，但对于个人研究者可能偏高。\n  - 数据需求: 主要依赖公开 benchmark（MT-AgentRisk 365 tasks、OpenAgentSafety 356 tasks、MultiBreak 10,389 prompts）和公开模型（Qwen3-8B、Llama 3.1-8B），数据获取无障碍。CPL 训练需要 AgentGym 环境构建 preference pairs。\n  - 人工介入: GPT-4o 评审需要 API 调用成本；AgentGym 环境搭建可能需要较多调试；quadruple-method head analysis 需要实现 4 种不同的 head identification 方法。整体人工介入程度中等偏高。\n  - 训练需求: 需要训练 CPL（LoRA rank-16 DPO）、XGuard-SFT（两个配置）、XGuard-DPO、两个控制 LoRA，共 ~6 个 LoRA 模型 × 2 base models = ~12 次训练。不需要从头预训练。\n  - 新 Benchmark: 不需要构建新 benchmark，但需要构造 extended-turn variants（100 tasks × 5 turn-counts），这属于数据增强而非新 benchmark。\n  - 预估周期: 16-18 周（含 1 周 buffer）。对于 EMNLP 2026（若 deadline ~2026年6月），时间不足；proposal 自身定位 ICLR 2027（2026年9月 deadline），timeline 勉强可行但紧张。\n```\n\nSources:\n- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026)](https://arxiv.org/abs/2602.03664)\n- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)\n- [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026)](https://arxiv.org/abs/2509.25843)\n- [On the Role of Attention Heads in LLM Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)\n- [When Attention Closes (Dongre et al., arXiv 2026)](https://arxiv.org/abs/2605.12922)\n- [MT-AgentRisk / ToolShield](https://unsafer-in-many-turns.github.io/)\n- [X-Boundary (Lu et al., EMNLP 2025)](https://arxiv.org/abs/2502.09990)\n- [MTSA (Guo et al., ACL 2025)](https://arxiv.org/abs/2505.17147)\n- [Awesome Attention Heads Survey](https://github.com/IAAR-Shanghai/Awesome-Attention-Heads)\n- [Multi-Turn Jailbreak Attacks Topic](https://www.emergentmind.com/topics/multi-turn-jailbreak-attacks)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient field context. Let me compile the comprehensive evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Wan et al., \"Mitigating Conversational Inertia in Multi-Turn Agents\", arXiv:2602.03664] (ICML 2026): 提出 conversational inertia 概念和 CPL 干预，但仅在 agentic performance 上评估，从未涉及 safety，且 diagonal attention 仅有 aggregate-level 刻画。确认 proposal 关于\"CPL 未评估 safety\"及\"无 per-head decomposition\"的 novelty claim 成立。\n- [Li et al., \"DETAM\", arXiv:2504.13562] (ACL 2025 Findings): 通过 inference-time attention reallocation（修改 causal mask）实现 ASR 46%→1.2%。确认其为 single-turn only，需 runtime intent token identification。Proposal 对其局限性的分析准确。\n- [Park et al., \"ASGuard\", arXiv:2509.25843] (ICLR 2026): 通过 circuit-level channel-wise scaling 修改 safety-vulnerable heads，ASR 42%→8%。确认其针对特定 attack types 的 localizable circuits，proposal 对其\"efficacy hinges on localizable circuits\"的论断准确。\n- [Dongre et al., \"When Attention Closes\", arXiv:2605.12922] (2026): 提出 GAR 指标，发现 architecture-dependent failure modes。非常新的工作（2026年5月），proposal 对其整合合理。\n- [Johnson & Huo, arXiv:2602.14370] (2026): 从物理学角度形式化 attention competition tipping points。理论框架但缺乏 NLP 社区的实证验证，proposal 试图提供这种验证。\n- [CAST, arXiv:2601.04262] (2026): Head-level conflict map 用于 safety-utility 冲突诊断。与 proposal 的 quadruple-method 头识别比较相关。\n- [X-Boundary, arXiv:2502.09990] (EMNLP 2025): Representation-level 边界，ASR 58.5%→16.5%。作为 proposal 的 baseline 之一。\n- [MTSA, arXiv:2505.17147] (ACL 2025): RL-based multi-turn alignment，ASR 74.5%→23.5%。代表 safety-labeled data 训练路线。\n- [Huang et al., arXiv:2508.19697] (2025): 提出 AHD 将 safety 分布到更多头。与 proposal 的 competition hypothesis 形成有趣对话。\n- [Alignment Pretraining, arXiv:2601.10160] (2026): 展示 pretraining discourse 内容因果影响 alignment（misalignment 45%→9%）。为 discourse→safety pathway 提供独立证据，但通过 data content 而非 attention mechanics。\n- 调研总结: 多轮安全退化的 attention 机制解释（DETAM/ASGuard/ASJA）和多轮安全防御（X-Boundary/MTSA/MUSE-D）已有成熟工作，但\"untargeted discourse intervention → safety via attention reallocation\"这条因果链确实无人验证。per-head diagonal attention decomposition 和 capacity flow mapping 确为方法论空白。Proposal 在这个交叉点上有真实的 novelty 空间。\n\n【整体印象】:\n作为审稿人，第一反应是：这是一个研究品味很好、文献功底极深的 proposal，研究问题genuinely interesting（untargeted discourse training 是否通过 attention reallocation 因果地影响 safety），方法论贡献（per-head decomposition、capacity flow mapping）有独立价值。但这个 proposal 的最大问题是 **scope 严重超载**——五个主相位（0, 0.5, 1, 2, 3, 4）加上 2.5 和二级评估，8 个实验条件，4 种 head identification 方法，2 个模型，3+ 个 benchmark，hyperparameter sensitivity sweep……这更像一个 2 年的 research program 而非一篇论文。我会倾向给 **borderline**（weak accept / weak reject），取决于最终呈现能否聚焦。\n\n【核心贡献】:\n1. **因果检验**：首次测试 untargeted discourse intervention（CPL）是否通过 attention reallocation 因果地改善多轮安全——这是一个有价值的实验问题，因为它桥接了 discourse dynamics 和 safety mechanisms 两个原本分离的文献。\n2. **方法论贡献**：per-head diagonal attention decomposition（Wan et al. 仅有 aggregate）；attention capacity flow mapping（DETAM/ASGuard/AISA 都未追踪释放的 attention 流向何处）；quadruple-method safety head comparison。这些无论 safety 结果如何都有价值。\n3. **范式控制的 double dissociation 设计**：CPL vs. XGuard-DPO 对比在相同训练范式下隔离数据来源的效应，实验设计巧妙。\n\n贡献价值：如果执行到位且结果明确，对领域有中等偏上的价值——它不会改变 safety 研究的基本范式，但会为 attention-based safety 理解增加重要的 mechanistic 证据，并提供有用的方法论工具。\n\n【方法合理性】:\n方法的核心逻辑是合理的：如果 diagonal attention（inertia）与 safety attention 在 softmax zero-sum 约束下竞争，那么减少 inertia 应当释放 attention 给 safety tokens。CPL 作为干预是合理选择，因为它是唯一已验证的训练级 inertia reduction 方法。\n\n但有几个值得质疑的点：\n1. **因果归因的挑战**：即使 CPL 同时减少 inertia 和改善 safety，因果链可能不是 \"inertia↓ → safety attention↑ → safety↑\"，而是 DPO 训练的其他效应（如更好的 instruction following、更短的回复等）同时影响两者。Paradigm-matched XGuard-DPO 控制有帮助但不完全解决——因为 CPL 和 XGuard-DPO 的 preference data 分布不同（proposal 也承认了这一点）。\n2. **三层竞争假设的可证伪性**：Level 1/2/3 的框架覆盖了几乎所有可能的竞争模式——如果 head overlap 高是 Level 1，中等是 Level 2，低是 Level 3。这种全覆盖框架很难被 falsify，削弱了假设的锐利度。\n3. **是否有更简单的替代方案**：直接在 CPL 的 DPO 训练中加入少量 safety preference pairs（mixed training）来测试 discourse + safety 的交互效应，可能比五阶段实验更高效地回答核心问题。不过 proposal 的设计确实提供了更丰富的 mechanistic 理解。\n\n【5 维度打分】:\n\n1. 研究问题: [强] — 多轮安全退化的 attention 机制是 2025-2026 的热门方向（DETAM, ASGuard, ASJA, Deng et al. 等大量相关工作），\"untargeted discourse intervention 是否因果影响 safety\"是一个自然但尚未被测试的问题。问题定位精准，抓住了 discourse dynamics 和 safety mechanisms 文献的交叉空白。\n\n2. 方法与创新: [中偏强] — Per-head diagonal attention decomposition 确实是 Wan et al. 未做的有价值扩展；capacity flow mapping 填补了 DETAM/ASGuard/AISA 的方法空白；paradigm-matched DPO comparison 设计巧妙。但核心 novelty（用 CPL 测 safety）更像是\"obvious next step\"而非深层创新——Wan et al. 提出 CPL 后，自然有人会测其 safety 效应。三层竞争假设虽有理论价值但 unfalsifiable 设计削弱了 contribution。与 Alignment Pretraining (arXiv:2601.10160) 的 discourse→alignment 因果路径相比，proposal 的路径（post-training attention mechanics）是互补但更窄。\n\n3. 实验设计: [强] — 这是 proposal 最突出的优势。8 个实验条件涵盖了几乎所有合理对照（random LoRA, reversed-CPL, parameter-matched SFT, paradigm-matched DPO, representation-level baseline, inference-time baseline, combination test）。Manipulation check 设计（先验证 CPL 确实减少 inertia 再解读 safety）是方法论上的亮点。Dose-response 测试 tipping point 预测、per-turn ASR 分析、over-refusal 评估（OpenAgentSafety + OR-Bench）都很周全。与 MTSA（ASR 74.5%→23.5%）、X-Boundary（ASR 58.5%→16.5%）、ASGuard（ASR 42%→8%）等已发表工作的 baseline 标准相比，proposal 的实验设计达标甚至超标。但 scope 过大是双刃剑——执行风险高。\n\n4. 可行性: [中偏弱] — 主要风险：(a) CPL 代码未发布，reproduction 是整个研究的前提，Phase 0 失败则全盘皆输；(b) 16-18 周完成这个规模的实验在资源受限条件下非常紧张；(c) ~1000-1200 A100-hours 的 GPU 预算对于 8 conditions × 2 models + 大量分析是偏紧的估计；(d) AgentGym 环境的 dual-rollout pipeline 可能不稳定；(e) EMNLP 2026 的 ARR 提交截止日为 2026 年 5 月 25 日（距今仅 5 天），即使后续 ARR cycle 可 commit 到 EMNLP 2026，该 proposal 的 16-18 周时间线意味着最早 9-10 月完成，无法赶上 EMNLP 2026（但这是物流问题，不影响学术质量评估）。Go/no-go milestones 和 fallback paths 设计合理，但 fallback（\"pivot to correlational-only study\"）会大幅削弱 contribution。\n\n5. 写作与呈现: [中] — 文献综述极其详尽，体现了深厚的学术功底。但 proposal 过于冗长密集，核心叙事线被大量细节淹没。一个审稿人读完后可能的反应是\"这里有很多好想法，但我不确定这篇论文到底要讲什么核心故事\"。需要显著精简，提炼出 1-2 个核心贡献作为主线，其余作为 supplementary。三层竞争假设的呈现方式也过于框架化，给人\"理论先行\"的感觉。\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】:\n研究问题有真实的 novelty 空间（强），实验设计非常完备（强），方法论贡献有独立价值。这些因素将概率推向 30%+。但以下因素将概率拉低：(1) scope 严重超载——这个规模的实验计划如果不大幅精简，成稿后很可能不聚焦，审稿人会抱怨\"tries to do too much\"；(2) 核心 novelty 的\"obvious next step\"感——在 Wan et al. 之后测 CPL 的 safety 效应是自然的延伸而非深层创新；(3) 可行性风险——CPL 复现是前提条件，失败则 pivoting 后贡献大打折扣；(4) 三层竞争假设的 unfalsifiability 问题会被 mechanistic interpretability 方向的审稿人质疑；(5) 因果归因的挑战——即使所有实验都跑通，CPL 的多重效应使得\"inertia reduction → safety improvement\"的因果链难以 clean 地建立。中位估计 30% 反映了\"方向正确、设计出色但执行和聚焦风险显著\"的判断。如果作者能将论文聚焦到 Phase 0.5 + Phase 1 + Phase 2 的核心实验（per-head decomposition + correlational + interventional），精简到 8 页主体 + appendix，概率可提升至 35-40%。\n\n【主要风险】:\n1. **Scope 过大导致论文不聚焦**：五阶段实验 + 四种 head identification 方法 + 三层竞争假设 + 多个 benchmark，审稿人极有可能给出\"ambitious but unfocused\"的评价，这是 EMNLP/ACL 类会议 reject 的常见原因。\n2. **CPL 复现失败或因果归因不清晰**：整个研究建立在 CPL 成功复现的前提上（代码未发布），且即使 CPL 同时减少 inertia 和改善 safety，paradigm-matched 控制也无法完全排除 DPO 训练的其他混淆效应，审稿人可能认为因果证据不够 conclusive。\n\n【实施评估】:\n  - 计算资源: ~1000-1200 A100-hours（$1500-1800），对学术实验室偏重但可行；主要瓶颈在 8 conditions × 2 models 的组合爆炸和多阶段 attention 分析\n  - 数据需求: MT-AgentRisk (365 tasks, 公开), OpenAgentSafety (356 tasks, 公开), MultiBreak (10,389 prompts, 公开), XGuard-Train (HuggingFace 公开), OR-Bench (公开)。CPL 的 preference pair 构建需要 AgentGym 环境 + dual-rollout pipeline（高技术风险）\n  - 人工介入: 中等——CPL 复现需手动调试 AgentGym pipeline；extended-turn variant 构建需半手动设计；GPT-4o judge 需 API 成本和 prompt 工程\n  - 训练需求: 需训练 ~8 个 LoRA 模型（CPL ×2 models, XGuard-SFT rank-8/16 ×2, XGuard-DPO ×2, Random-LoRA ×2, Reversed-CPL ×2）+ hyperparameter sweep ~16 个额外模型\n  - 新 Benchmark: 无需构建全新 benchmark，但 extended-turn variants（0/2/4/6/8 prepended turns × 100 tasks）需要半自动构建\n  - 预估周期: 16-18 周（proposal 自估），实际更可能 20-24 周，考虑到 CPL 复现风险和 Phase 0 的 serial dependency\n```\n\nSources:\n- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026)](https://arxiv.org/abs/2602.03664)\n- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)\n- [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026)](https://arxiv.org/abs/2509.25843)\n- [When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction (Dongre et al., 2026)](https://arxiv.org/abs/2605.12922)\n- [Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, 2026)](https://arxiv.org/abs/2602.14370)\n- [X-Boundary: Establishing Exact Safety Boundary (Lu et al., EMNLP 2025)](https://arxiv.org/abs/2502.09990)\n- [MTSA: Multi-turn Safety Alignment (Guo et al., ACL 2025)](https://arxiv.org/abs/2505.17147)\n- [Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., 2025)](https://arxiv.org/abs/2508.19697)\n- [Safety-Utility Conflicts Are Not Global: CAST (2026)](https://arxiv.org/abs/2601.04262)\n- [Alignment Pretraining (Tice et al., 2026)](https://arxiv.org/abs/2601.10160)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [On the Role of Attention Heads in LLM Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)\n- [Unsafer in Many Turns: MT-AgentRisk (Yang et al., 2026)](https://arxiv.org/abs/2602.13379)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient field context. Let me compile my comprehensive evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Wan et al., \"Mitigating Conversational Inertia in Multi-Turn Agents\" (ICML 2026, arXiv:2602.03664)]: 本 proposal 的核心基础工作。提出 diagonal attention（conversational inertia）现象和 CPL 干预方法。仅在 agentic performance 上验证，未涉及 safety。Aggregate-level 注意力分析，未做 per-head decomposition。代码未公开。\n- [Li et al., \"DETAM\" (ACL 2025 Findings, arXiv:2504.13562)]: 单轮 inference-time attention reallocation 防御，ASR 46%→1.2%。证明 attention redistribution 因果性改善安全性，但依赖运行时 intent token 识别，无法扩展到 multi-turn。\n- [Park et al., \"ASGuard\" (ICLR 2026, arXiv:2509.25843)]: Training-time circuit-targeted head scaling，ASR 42%→8%。识别 Layer-13 关键 heads。但仅针对特定可定位的攻击类型（如 tense-changing），不处理渐进式 discourse erosion。\n- [Zhou et al., \"On the Role of Attention Heads in LLM Safety\" (ICLR 2025, arXiv:2410.13708)]: Ships score 评估 head 安全贡献，发现安全头集中在少量 heads。为 Phase 0.5 head overlap 分析提供基础方法。\n- [Huang et al., \"Safety Alignment Should Be Made More Than Just A Few Attention Heads\" (arXiv:2508.19697)]: 提出 AHD 分布安全能力到更多 heads，与本 proposal 的 competition hypothesis 形成有趣张力。\n- [Deng et al., \"The Struggle Between Continuation and Refusal\" (arXiv:2603.08234)]: 识别 safety heads (L25-27) vs. continuation heads (~L13) 的竞争，与 ASGuard 的 L13 vulnerable heads 吻合。直接支持 competition mechanism。\n- [Lu et al., \"X-Boundary\" (EMNLP 2025, arXiv:2502.09990)]: Representation-level boundary 防御，ASR 58-76%→16-25%，over-refusal 减少~20%。作为 Level 3 (representation-level) baseline。\n- [Guo et al., \"MTSA\" (ACL 2025, arXiv:2505.17147)]: Multi-turn RL safety alignment，ASR 74.5%→23.5%，peak attack at round 5。直接竞争者但使用 safety-labeled 数据。\n- [COLM 2025, \"X-Teaming/XGuard-Train\" (arXiv:2504.13203)]: Multi-turn safety SFT baseline，up to 48.3% vulnerability reduction。\n- [MUSE-D (EMNLP 2025, arXiv:2509.14651)]: Turn-level DPO，24% ASR reduction。直接 multi-turn DPO baseline。\n- [Yang et al., \"MT-AgentRisk/ToolShield\" (arXiv:2602.13379)]: 365-task benchmark + inference-time 防御（~30% ASR reduction）。Proposal 的主要评测平台。开源可用。\n- [Dongre et al., \"When Attention Closes\" (arXiv:2605.12922)]: GAR 指标衡量 goal-token attention degradation，发现 architecture-dependent failure modes。补充性指标。\n- [CAST (arXiv:2601.04262)]: Head-level conflict map，发现 utility degradation 集中在少量 high-conflict heads。为 quadruple-method triangulation 提供第四种方法。\n- [Tice et al., \"Alignment Pretraining\" (arXiv:2601.10160)]: Discourse-level pretraining data 因果影响 alignment (misalignment 45%→9%)。独立证据支持 discourse→safety pathway 存在性。\n- [Johnson & Huo (arXiv:2602.14370)]: Attention competition tipping point 理论框架。为 dose-response 实验设计提供理论依据。\n\n- 调研总结: Multi-turn safety 是 2025-2026 快速增长的研究方向，已有多种防御方法（XGuard、MUSE-D、X-Boundary、MTSA、ToolShield），但均直接使用 safety-labeled 数据。Attention mechanism 在 safety 中的角色已被充分研究（DETAM、ASGuard、Zhou、AISA），但\"discourse-level 非安全干预能否因果性改善 safety\"这一假设确实 **未被测试过**。Per-head diagonal attention decomposition 和 attention capacity flow mapping 在文献中确实不存在。Proposal 精准定位了一个真实且重要的研究空白。\n\n【整体印象】: \n作为审稿人，我的第一反应是\"研究问题有真正的 novelty，实验设计令人印象深刻地严谨，但整体范围极度膨胀\"。这篇 proposal 的核心洞察——untargeted discourse training 是否能因果性改善 multi-turn safety——是一个优美、测试价值高的假设。将 CPL 的 inertia reduction 与 DETAM/ASGuard 的 attention reallocation 框架联系起来，逻辑链清晰且有理论支撑。\n\n然而，proposal 试图将至少 2-3 篇论文的工作量压缩到一项研究中：per-head decomposition + capacity flow mapping + quadruple-method head comparison + paradigm-controlled comparison + dose-response analysis + double dissociation + autonomy tax audit + mechanistic verification + OpenAgentSafety secondary evaluation。这种 scope inflation 是 EMNLP 审稿中**最常见的拒稿理由之一**。一篇试图做所有事情的论文，往往每件事都做不够深。\n\n我会倾向于 **borderline accept / weak reject**，取决于最终论文是否能有效聚焦。\n\n【核心贡献】:\n1. **假设检验贡献**（最高价值）: 首次测试 discourse-level 训练干预（CPL）是否因果性改善 multi-turn safety，连接了 discourse quality 和 safety 两个独立研究社区。如果正面结果成立，这揭示了 safety 的一种全新改善路径（不需要 safety-labeled 数据）。\n2. **方法论贡献**（中高价值）: Per-head diagonal attention decomposition 和 attention capacity flow mapping 是真实的 first，前者填补了 Wan et al. 仅报告 aggregate-level 的空白，后者回答了所有 attention-reallocation safety 工作都隐含假设但未验证的问题。\n3. **分析贡献**（中等价值）: Quadruple-method safety head identification comparison 有独立价值，但更像是 engineering contribution 而非 conceptual breakthrough。\n4. 对领域的价值：如果正面结果成立，impact 较高——表明 safety 不需要仅靠 safety 数据来改善，discourse quality 训练是一条互补路径。如果负面结果，价值中等——首次排除了一个重要假设 + 方法论贡献。\n\n【方法合理性】:\n方法整体合理，但存在几个关键脆弱点：\n\n**合理之处：**\n- CPL 作为干预手段选择得当：它是 parameter-efficient (0.4% params)、well-characterized 的方法，其 attention 效应已被原文档记录。\n- Paradigm-controlled comparison (XGuard-DPO) 设计精巧，通过将 XGuard safety 数据转换为 CPL 相同的 DPO 格式，有效控制了训练范式这一混杂因素。\n- Manipulation check 先验证 CPL 是否真的减少了 inertia，再解释 safety 效果——这是好的因果推断实践。\n\n**脆弱之处：**\n1. **Softmax zero-sum ≠ causal competition**: Proposal 反复强调 softmax 的 zero-sum 约束保证 capacity release，但 zero-sum 只意味着总概率恒定，并不意味着从 diagonal 释放的 attention 会流向 safety tokens。Capacity flow mapping 正是为了解决这个问题，但如果结果显示 released capacity 分散到 formatting/task tokens 而非 safety tokens，整个 competition hypothesis 就不成立了。这是一个合法的实验设计，但审稿人会质疑 \"hypothesis 失败\" 的情况下论文的贡献是否足够。\n2. **CPL reproduction risk**: 代码未公开，dual-rollout preference pair construction 在 AgentGym 上的复现存在不确定性。Proposal 设了 fallback paths，但如果 CPL 复现不精确，所有下游分析的效力都会受损。\n3. **XGuard-DPO paradigm matching 的局限性**: Proposal 坦承 preference margin distributions 会不同，但这恰好是一个核心混杂因素——DPO 的效果对 preference margin 极度敏感（Park et al., arXiv:2403.19159 已证明）。\"Double dissociation\" claim 因此显著减弱。\n4. **更简单的替代方案**: 一个 reviewer 可能会问——是否可以直接测试 DETAM 在 multi-turn setting 中的效果（比如 turn-level DETAM），而不需要引入 CPL？如果 turn-level DETAM 有效，那 CPL 的 value proposition 就更窄了。Proposal 提到了 DETAM 在 multi-turn 中 intent token 定位的困难，但并未实验性地验证这个困难。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】— \"Untargeted discourse training 能否因果性改善 multi-turn safety\" 是一个高度原创、有理论和实践价值的问题。文献调研确认这一假设未被测试（所有现有 multi-turn safety defense 都使用 safety-labeled 数据），与 Alignment Pretraining (Tice et al., arXiv:2601.10160) 的发现形成互补但独立的证据线。Multi-turn safety erosion 本身是 well-documented 的现实问题（MT-AgentRisk: 16% ASR increase），且现有解法的 attention-mechanism 基础已被 DETAM、ASGuard、Zhou et al. 等充分建立，使得这一 causal question 有坚实的研究基础。\n\n2. 方法与创新: 【中】— 核心方法创新在于 per-head diagonal attention decomposition 和 capacity flow mapping，这两者在文献中确实不存在（Wan et al. 仅报告 aggregate; DETAM/ASGuard/AISA 均不追踪 capacity 流向）。然而，**核心实验本质上是 \"take existing method (CPL) and evaluate on new task (safety)\"**，这是 application-level novelty 而非 fundamental methodological innovation。Three-level competition hierarchy 虽然有组织价值，但更像是对已知现象（head-level safety: Zhou et al.; layer-level: Deng et al.; representation-level: X-Boundary）的框架化重述，而非真正的理论贡献。Paradigm-controlled comparison (XGuard-DPO) 设计精巧但受 preference margin confound 限制（Park et al., arXiv:2403.19159）。\n\n3. 实验设计: 【强】— 这是 proposal 最大的亮点。8 个实验条件（CPL + 2 controls + 3 XGuard variants + X-Boundary + ToolShield + combination）涵盖了几乎所有合理的 baseline。Manipulation check 先验证机制再解释效果，是一流的因果推断设计。Dose-response 测试 tipping point 预测，sample size justification (365 tasks × 8 conditions 提供 >5800 observations)，GPT-4o judge with position-swap protocol + rule-based secondary evaluator + Cohen's kappa 报告——这些都显著超过了该领域的平均实验标准。与同类工作相比：MUSE-D 仅用单一 DPO baseline；X-Boundary 未做 paradigm-controlled comparison；MTSA 未做 attention-level mechanistic analysis。Null-result framing strategy 也值得称赞。**但 scope 过大是双刃剑——设计完美但执行不完整的实验 vs. 范围适中但执行彻底的实验，审稿人几乎总是偏好后者。**\n\n4. 可行性: 【中】— 资源需求合理（~1000-1200 A100-hours，~$1500-1800，8B 模型），16-18 周时间线虽紧凑但不不切实际。主要风险：(a) CPL 代码未公开，复现需要 contact authors + reproduce dual-rollout pipeline，这可能消耗大量时间；(b) AgentGym 环境稳定性；(c) Quadruple-method pipeline 的工程复杂度；(d) 8 个条件 × 2 模型 × 多个评测集的实验矩阵管理。Go/no-go milestones 设计合理，但 fallback 到 \"correlational-only study\" 或 \"DETAM in multi-turn settings\" 实质上是完全不同的论文。最大的可行性风险是 **scope 导致的执行质量下降**——即使每个组件都可行，同时高质量完成所有组件在 16 周内是极具挑战的。\n\n5. 写作与呈现: 【中偏弱】— Proposal 展示了对领域的深入理解和极强的综合能力，literature review 堪称典范。但当前写作存在严重的 **信息过载** 问题：大量首字母缩写（CPL、DETAM、ASGuard、AISA、CAST、GAR、SRI、AHD）、过度的交叉引用、嵌套式论证使得核心 message 被淹没。一个清晰的 3 句话 elevator pitch 应该是：\"Multi-turn safety erosion 可能由 attention inertia 驱动 → CPL 减少 inertia → 如果 CPL 也改善 safety，则证明了一条不需要 safety 数据的新路径。\" 但这个简洁信息需要在大量技术细节中费力提取。审稿人在 3-5 分钟快速浏览时可能无法抓住核心贡献。此外，Target Venues 写的是 ICLR 2027 / AAAI 2027 而非 EMNLP 2026，这是细节但反映了 framing 的不聚焦。\n\n【概率估计】: [22% - 36%] 中位 28%\n\n【估计理由】: \n研究问题的 novelty 是真实的——这是一个未被测试的重要假设，且实验设计远超该领域平均水平，这两点将 proposal 提升到 \"有竞争力\" 的范围。然而，三个因素显著压低了概率：\n\n(1) **Scope inflation 是最大的单一风险**。当前 proposal 包含至少 3 篇论文的内容（Paper A: per-head diagonal decomposition + capacity flow mapping; Paper B: CPL→safety causal test with paradigm controls; Paper C: quadruple-method head comparison + mechanistic analysis）。EMNLP 审稿人对 \"试图做太多\" 的论文非常敏感——不是因为内容不好，而是因为每个部分都无法做到足够深入。如果最终论文不能有效聚焦到 1-2 个核心贡献，rejection 概率显著上升。\n\n(2) **核心贡献的 perceived novelty 可能被低估**。\"Take CPL and test on safety\" 在技术上是 application-level transfer，审稿人可能将其视为 \"applying existing method to new domain\" 而非 fundamental contribution，即使 causal framing 提升了其价值。\n\n(3) **结果不确定性高**。如果 CPL 的 safety improvement 效果不显著（与直接 safety training 方法如 MTSA、X-Boundary 相比），论文需要依赖 null-result + methodological contributions 来立足，这在顶会中更难被接受。如果 capacity flow 分散而非定向到 safety tokens，三级竞争假设被削弱。\n\n正面因素：research question 的 novelty 真实存在，experimental rigor 远超平均水平（manipulation check + paradigm control + dose-response 在该领域非常少见），multi-turn safety 是 EMNLP 社区高度关注的方向，standalone methodological contributions (per-head decomposition, capacity flow) 提供了 fallback value。\n\n综合判断：如果论文有效聚焦（砍掉 Phase 2.5 hyperparameter sensitivity、简化 Phase 4 mechanistic verification、将 quadruple-method comparison 移入 appendix）且 CPL 产生有意义的 safety improvement，概率可提升到 35-40%。按当前 scope 执行，概率在 22-28% 范围。\n\n【主要风险】:\n1. **Scope inflation → 每个贡献都不够深**：当前 proposal 是 5 phases + 8 conditions + quadruple triangulation + dose-response + mechanistic verification + secondary evaluation + autonomy tax audit。即使全部执行完毕，在 8 页正文中无法做到每个部分都有足够深度。审稿人最可能的 criticism 是 \"the paper tries to do too much and each contribution feels shallow\"。\n2. **CPL safety improvement 效果可能不显著或不如直接 safety training methods**：如果 CPL 的 ASR reduction 显著弱于 XGuard-DPO / X-Boundary / MTSA（后者直接使用 safety 数据），审稿人会质疑 \"为什么不直接用 safety 数据训练？\" 虽然 causal mechanism insight 有独立价值，但 \"method 不 work well\" + \"但我们理解了为什么\" 在顶会中是高风险策略。\n\n【实施评估】:\n  - 计算资源: ~980-1200 A100-hours (~$1500-1800)，对学术实验室合理；8B 模型规模不需要极端资源，但 8 条件 × 2 模型的实验矩阵管理需要良好的工程基础设施\n  - 数据需求: MT-AgentRisk (365 tasks, 公开)、OpenAgentSafety (公开)、MultiBreak (公开)、XGuard-Train (HuggingFace 公开)、CPL preference pairs (需复现 dual-rollout pipeline on AgentGym)、OR-Bench (公开)\n  - 人工介入: 中等——CPL 复现需要与原作者沟通获取 checkpoints、AgentGym 环境调试、extended-turn variant 构造（100 tasks × 5 turn counts）需要人工验证质量\n  - 训练需求: 需要训练——CPL DPO (2 models)、XGuard-SFT rank-8 和 rank-16 (2 models each)、XGuard-DPO (2 models)、Random-Preference LoRA (2 models)、Reversed-CPL (2 models)、hyperparameter sweeps；总计约 14-16 次训练运行 + sweeps\n  - 新 Benchmark: 不需要构建全新 benchmark，但需要构造 extended-turn variants（在 MT-AgentRisk 基础上 prepend benign turns）和将 XGuard 数据转换为 DPO 格式\n  - 预估周期: 16-18 周（含 1 周 buffer），但如果 CPL 复现遇到困难可能延伸到 20+ 周；关键路径：CPL 复现 → Phase 0.5 head overlap → Phase 2 interventional\n```\n\nSources:\n- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., 2026)](https://arxiv.org/abs/2602.03664)\n- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025)](https://arxiv.org/abs/2504.13562)\n- [ASGuard: Activation-Scaling Guard (Park et al., ICLR 2026)](https://arxiv.org/abs/2509.25843)\n- [On the Role of Attention Heads in LLM Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)\n- [When Attention Closes (Dongre et al., 2026)](https://arxiv.org/abs/2605.12922)\n- [CAST: Safety-Utility Conflicts Are Not Global (2026)](https://arxiv.org/abs/2601.04262)\n- [Unsafer in Many Turns / MT-AgentRisk / ToolShield (2026)](https://arxiv.org/abs/2602.13379)\n- [X-Boundary (Lu et al., EMNLP 2025)](https://arxiv.org/abs/2502.09990)\n- [Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., 2025)](https://arxiv.org/abs/2508.19697)\n- [The Struggle Between Continuation and Refusal (Deng et al., 2026)](https://arxiv.org/abs/2603.08234)\n- [Alignment Pretraining (Tice et al., 2026)](https://arxiv.org/abs/2601.10160)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Conversational Inertia as a Causal Pathway to Multi-Turn Safety Erosion: Testing the Attention Capacity Competition Hypothesis\n\n## Description\nThis project conducts the first controlled interventional study testing whether conversational inertia — diagonal attention to previous outputs (Wan et al., ICML 2026) — constitutes an independent causal mechanism of progressive multi-turn safety erosion, distinct from and orthogonal to mechanisms addressed by DETAM (single-turn attention reallocation, ASR 46%→1.2%; Li et al., ACL 2025 Findings) and ASGuard (circuit-specific vulnerability targeting; Park et al., ICLR 2026). We propose that reducing inertia through untargeted discourse training (CPL) achieves broad attention reallocation addressing progressive multi-turn erosion that targeted approaches structurally cannot: DETAM's intent-token localization is ill-defined in multi-turn crescendo attacks where intent is distributed across turns; ASGuard's efficacy hinges on localizable circuits absent in cumulative discourse erosion. The study makes two novel methodological contributions beyond safety evaluation: (1) the first per-head decomposition of diagonal attention (Wan et al. explicitly averages all heads), and (2) the first attention capacity flow mapping — tracking where attention capacity released by inertia reduction actually flows (toward safety tokens, task tokens, or dispersed), a question no prior attention-reallocation safety work (DETAM, ASGuard, AISA) has addressed. Phase 0.5 measures overlap with safety-critical heads using quadruple triangulation (Ships score, DETAM sensitivity, AISA spatiotemporal analysis, CAST conflict map from arXiv:2601.04262), cross-validated against four published head sets (Zhou et al., Depth Charge, ASGuard, CAST). We integrate the Goal Accessibility Ratio (GAR; Dongre et al., arXiv:2605.12922) as a complementary metric — if diagonal attention rises while GAR falls, two independent measures converge on the same competition mechanism. The five-phase causal design includes: a manipulation check verifying CPL reduces inertia on safety benchmarks before interpreting safety effects; paradigm-controlled comparison (XGuard-DPO: safety data in CPL's exact DPO format) enabling detection of a potential double dissociation between attention-reallocation and direct-safety training pathways; turn-count dose-response testing Johnson & Huo's (arXiv:2602.14370) tipping point predictions; ToolShield direct comparison and CPL+ToolShield combination testing orthogonality of training-time and inference-time defenses; and X-Boundary (EMNLP 2025) as a direct representation-level baseline. If CPL reproduces DETAM-like attention redistribution and ASGuard-targeted head modification despite having no safety training signal, this reveals shared attentional infrastructure between discourse quality and safety — consistent with independent evidence from Alignment Pretraining (arXiv:2601.10160) that discourse-level data properties causally influence alignment through a different pathway (pretraining content vs. post-training attention mechanics). The per-head decomposition, capacity flow mapping, quadruple-method head comparison, and mechanistic analysis constitute standalone contributions regardless of safety results.\n\n## Core Problem\nMulti-turn agent interactions exhibit systematic safety degradation (16% higher attack success rates), and while recent work has identified attention-level mechanisms — attention dispersion on safety keywords (ASJA, AAAI 2025), competition between safety and continuation heads (Deng et al., arXiv:2603.08234), and attention reallocation as a defense (DETAM, ACL 2025 Findings) — and developed multi-turn safety defenses (MUSE-D turn-level DPO, EMNLP 2025; XGuard-Train SFT, COLM 2025; X-Boundary representation boundaries, EMNLP 2025; MTSA RL-based alignment, ACL 2025), and training-time attention head interventions for specific vulnerability types (ASGuard circuit-targeted scaling, ICLR 2026), these studies are either attack-oriented, single-turn, operate at inference time, target specific localizable vulnerabilities, or train directly on safety-labeled data without testing whether discourse-level mechanisms causally drive safety erosion. Critically, DETAM demonstrates that simply reallocating attention from attack tokens toward safety-relevant tokens at inference time reduces ASR from 46% to 1.2% on LLaMA-2, providing the strongest existing evidence that attention redistribution causally improves safety. Yet DETAM requires explicit identification of 'intent tokens' at runtime and operates only in single-turn settings — in multi-turn crescendo attacks where malicious intent is progressively distributed across turns, the notion of localizable 'intent tokens' breaks down fundamentally. ASGuard demonstrates that training-time modification of safety-relevant heads is feasible via circuit-targeted scaling vectors, but its efficacy 'hinges on localizable causal circuits' for specific attack types — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits. Concurrently, \"When Attention Closes\" (Dongre et al., arXiv:2605.12922) demonstrates that multi-turn attention degradation produces architecture-dependent failure modes — some models preserve goal-conditioned behavior through residual streams even at vanishing direct attention, others fail despite decodable residual goal information — suggesting that the pathway from attention loss to behavioral failure is not uniform and requires measurement at multiple levels. Furthermore, the competition hypothesis contains a critical hidden assumption: that attention capacity released by reducing diagonal inertia is captured by safety-relevant tokens rather than by other competing patterns. Softmax's zero-sum constraint guarantees capacity release but not its direction — no work has explicitly tracked where released capacity flows, despite this being fundamental to all attention-reallocation safety claims (DETAM, ASGuard, AISA). The only characterization of diagonal attention (Wan et al., ICML 2026) reports aggregate-level patterns averaged across all heads; no per-head decomposition exists, leaving the head-level competition question empirically open.\n\n## Opportunity\nSeven independent research threads have converged to make a controlled causal study newly feasible: (1) Conversational Inertia (Wan et al., ICML 2026, arXiv:2602.03664) identifies diagonal attention where the i-th token attends to the i-th previous output position and provides Context Preference Learning (CPL) as a parameter-efficient intervention (0.4% params, LoRA rank-16 DPO with beta=0.01), validated on Qwen3-8B and Llama 3.1-8B-Instruct across eight agentic environments but never evaluated for safety — crucially, the diagonal attention pattern is characterized only at the aggregate level (averaged across all heads), so the per-head distribution remains unknown; (2) DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) provides direct causal evidence that attention reallocation toward safety-relevant tokens improves safety — reducing ASR by 97%+ without weight modification — but requires runtime intent token identification and is single-turn only; (3) ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) demonstrates that training-time modification of safety-relevant attention heads is feasible via circuit-targeted channel-wise scaling vectors — crucially identifying 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30), exactly where Deng et al. find continuation heads — but targets specific localizable vulnerability circuits rather than discourse-level dynamics; (4) Multi-turn safety erosion is now well-benchmarked via MT-AgentRisk (365 tasks, 5 tools, avg 3.19 turns) with ToolShield as a defense baseline, supplemented by OpenAgentSafety (ICLR 2026, arXiv:2507.06134; 356 real-tool tasks) and MultiBreak (arXiv:2605.01687; 10,389 multi-turn adversarial prompts); (5) Multi-turn safety training has mature baselines: XGuard-Train SFT (COLM 2025, arXiv:2504.13203; up to 48.3% vulnerability reduction), MUSE-D turn-level DPO (EMNLP 2025, arXiv:2509.14651), X-Boundary representation-level boundaries (EMNLP 2025, arXiv:2502.09990; ASR reduction to 16-25%), and MTSA RL with future rewards (ACL 2025, arXiv:2505.17147; ASR 74.5% to 23.5%) — but all train directly on safety-labeled data; (6) AISA (Song et al., arXiv:2602.13547) provides spatiotemporal safety head localization via large-scale linear probing — K=16 heads achieving 0.92 detection accuracy — enabling methodological triangulation; (7) \"When Attention Closes\" (Dongre et al., arXiv:2605.12922) introduces the Goal Accessibility Ratio (GAR) measuring attention from generated tokens to goal-defining tokens across turns, demonstrating architecture-dependent failure modes that inform the multi-level competition hypothesis. Additionally, CAST (arXiv:2601.04262) provides a fourth complementary head identification method via head-level conflict maps, and Alignment Pretraining (Tice et al., arXiv:2601.10160) provides independent evidence that discourse-level data properties causally influence alignment — reducing misalignment from 45% to 9% via pretraining content curation — supporting the broader principle that untargeted discourse properties can affect safety through indirect pathways. This seven-thread convergence, combined with Johnson & Huo's (arXiv:2602.14370) formalization of attention competition tipping points, motivates a three-level attention capacity competition hypothesis testable through a novel Phase 0.5 head overlap analysis.\n\n## Landscape\n**Attention reallocation defenses:** DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) identifies attention heads sensitive to jailbreaks by computing attention score differences (threshold alpha: 0.1 for LLaMA-2, 0.03 for Vicuna), modifies the causal mask by multiplying at intent token positions by beta=5.0, reducing average ASR from 46.0% to 1.2% on LLaMA-2-7b-chat and from 81.8% to 4.0% on Vicuna-13b-v1.5. Cross-model transferability: sensitive heads from LLaMA-2 transferred to Meta-LLaMA-3 achieve 4% ASR vs. 96% vanilla. Three fundamental limitations for multi-turn agent settings: (a) requires runtime identification of 'intent tokens' — in crescendo attacks (Russinovich et al., USENIX Security 2025, arXiv:2404.01833) where intent is distributed across turns, token-level localization is ill-defined; (b) single-turn only, cannot address cumulative attention shift that Johnson & Huo's tipping point theory predicts; (c) per-turn computational overhead. Our study tests whether CPL achieves DETAM-like redistribution persistently through training. **Training-time attention head intervention:** ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) uses EAP-IG to identify causally linked heads, trains channel-wise activation scaling vectors (s_j ∈ R^{d_head}, H'_{l,j} = H_{l,j} ⊙ s_j) on identified heads with preventative fine-tuning. Reduces ASR from 42% to 8% on Llama-3.1-8B and 51% to 8% on Qwen2.5-7B, achieving Pareto-optimal safety-utility balance. Identifies 11 vulnerable heads including 4 at Layer 13 (L13H8, L13H18, L13H25, L13H30) — exactly where Deng et al. find continuation heads. Key differences: (a) targets localizable circuits; (b) fixes known attack types one at a time; (c) single-turn only. **Head-level conflict diagnosis:** CAST (arXiv:2601.04262) proposes Conflict-Aware Sparse Tuning, constructing head-level conflict maps by synthesizing optimization conflict and functional sensitivity. Key finding: utility degradation concentrates in a small subset of \"high-conflict\" heads. CAST's conflict map provides a fourth independent method for identifying safety-relevant heads, complementary to Ships score, DETAM sensitivity, and AISA probing. **Multi-turn attention degradation:** \"When Attention Closes\" (Dongre et al., arXiv:2605.12922) introduces GAR measuring attention from generated tokens to goal-defining tokens. Key finding: architecture-dependent failure modes — some models preserve goal-conditioned behavior at vanishing attention through residual streams, others fail despite decodable residual goal information, encoding layers varying from 2 to 27. GAR measures the same degradation phenomenon as diagonal inertia from a complementary angle, and the architecture-dependent failure modes inform the Level 2/3 distinction. **Safety head localization methods:** AISA (Song et al., arXiv:2602.13547) localizes safety-critical heads via spatiotemporal analysis — large-scale linear probing across 15 positions per layer, top-K=16 heads achieving 0.92 detection accuracy. Safety heads cluster in middle layers in standard models but shift toward higher layers in strongly safety-aligned models. **Safety head distribution:** Huang et al. (arXiv:2508.19697) propose Attention Head-level Dropout (AHD) to distribute safety capabilities across more heads, arguing that concentration in few heads is itself a vulnerability. This creates a productive tension with the competition hypothesis: if AHD distributes safety across more heads, does capacity competition become weaker or stronger? We argue stronger — softmax zero-sum operates within each head independently, so distributed safety heads increase the surface area over which capacity competition operates. If CPL's effect weakens on AHD-treated models, this would confirm head-level competition as the mechanism. **Attack-side mechanisms:** Du et al. (ASJA, AAAI 2025) show successful multi-turn jailbreaks correlate with attention dispersion away from safety keywords (p=4.38e-07). Deng et al. (arXiv:2603.08234) identify competing safety (layers 25-27) and continuation (~Layer 13) heads. Depth Charge (Wu et al., arXiv:2603.05772) introduces SAHA, 82-91% ASR, layer-specific concentrations (layer 7 for Llama 3.1-8B, head 31 universally important). Attention Eclipse (Zaree et al., arXiv:2502.15334) achieves 91.2% ASR by manipulating attention focus. **Attention competition theory:** Johnson & Huo (arXiv:2602.14370) formalize dot-product competition creating tipping points (n*) — cumulative inertia pushes past a threshold single-turn defenses cannot prevent. **Discourse-alignment causal pathway:** Alignment Pretraining (Tice et al., arXiv:2601.10160) demonstrates that discourse-level properties of pretraining data causally influence alignment (misalignment 45%→9%), establishing a precedent that untargeted discourse properties can affect safety — though through data content rather than attention mechanics. Our work tests the complementary pathway: post-training attention structure modification. **Multi-turn safety benchmarking:** Yang et al. (arXiv 2026) document 16% average ASR increase on MT-AgentRisk and propose ToolShield (~30% ASR reduction). OpenAgentSafety (ICLR 2026, arXiv:2507.06134) provides 356 multi-turn, multi-user tasks with real tools including benign-intent tasks useful for over-refusal evaluation. Li et al. (STAR, arXiv:2603.15684) show monotonic drift from refusal representations. MultiBreak (arXiv:2605.01687) provides 10,389 multi-turn adversarial prompts across diverse attack types. **Multi-turn safety defenses:** X-Teaming (COLM 2025, arXiv:2504.13203) introduces XGuard-Train (30K multi-turn safety dataset). SFT with LoRA rank-8, lr=1e-4, 3 epochs achieves up to 48.3% vulnerability reduction. MUSE-D (EMNLP 2025, arXiv:2509.14651) applies turn-level DPO achieving 24% ASR reduction. X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990) reduces ASR from 58.5-76.0% to 16.0-25.0% while reducing over-refusal by ~20%. MTSA (Guo et al., ACL 2025, arXiv:2505.17147) reduces ASR from 74.5% to 23.5%, peak attack at round 5. Agent Safety Alignment (Sha et al., arXiv:2507.08270) proposes unified sandboxed RL. STREAM (arXiv:2506.00668) reduces ASR by 51.2% via safety reasoning. TurnGate (arXiv:2605.05630) introduces turn-level harm detection. STREAM and TurnGate operate at inference time and are complementary to training-time interventions. **Discourse dynamics:** Wan et al. (ICML 2026, arXiv:2602.03664; also OpenReview #UubLs3lUfk, published in PMLR 306, Seoul, July 6-11) identify conversational inertia and propose CPL. Diagonal attention characterized only at aggregate level. Code not released. **Safety attention head mechanisms:** Zhou et al. (ICLR 2025, arXiv:2410.13708) show the most critical head in Llama-2-7B-Chat is Head (2, 26). Wei et al. (arXiv:2408.17003) identify safety layers at layers 9-14. The refusal direction (Arditi et al., arXiv:2406.11717) is strongest around layer 15. **Safety persistence:** Plaut (arXiv:2603.02229) shows LoRA safety DPO persists with 90-94% retention, Pareto frontier R-squared=0.77. **DPO length bias:** Park et al. (arXiv:2403.19159) and Meng et al. (arXiv:2409.06411) document hidden length dependence. **Gap:** Despite convergent progress on attention reallocation (DETAM), targeted head intervention (ASGuard), safety defenses (XGuard-Train, MUSE-D, X-Boundary, MTSA), head localization (Zhou et al., AISA, Depth Charge, CAST), attention degradation (GAR), competition theory (Johnson & Huo), discourse-alignment pathways (Alignment Pretraining), and discourse dynamics (conversational inertia), no work has: (a) tested whether training-time discourse intervention achieves broad DETAM-like attention reallocation and causally reduces multi-turn safety erosion; (b) provided per-head decomposition of diagonal attention; (c) tracked where attention capacity released by reallocation actually flows; (d) compared discourse-targeted vs. safety-targeted training under paradigm-matched conditions (DPO vs. DPO); or (e) controlled for DPO response-length confounds in discourse-safety evaluations.\n\n## Approach\nWe run a five-phase causal study on MT-AgentRisk (primary) and OpenAgentSafety (secondary) benchmarks using Qwen3-8B and Llama 3.1-8B-Instruct, organized around the 'attention capacity competition hypothesis.'\n\n**Why Training-Time Discourse Intervention?** DETAM achieves 97%+ ASR reduction in single-turn settings — but requires identifying 'intent tokens' at runtime. In multi-turn crescendo attacks where intent is distributed across 3-10 turns (MTSA finds peak attack at round 5), no single token set constitutes 'the intent.' ASGuard's Limitations notes 'efficacy hinges on localizable causal circuits.' Multi-turn inertia erosion is progressive, not localizable. CPL reduces cumulative inertia that dilutes safety attention — addressing the root cause (per-turn accumulation) that Johnson & Huo's tipping point theory predicts pushes past n*.\n\n**The Attention Capacity Competition Hypothesis (Three-Level Framework):** Diagonal attention competes with safety-keyword attention at three levels, and different architectures may exhibit different mixtures of these levels (informed by Dongre et al.'s architecture-dependent failure modes, arXiv:2605.12922): **Level 1 (Head-level, strong form):** Diagonal and safety attention share heads; softmax zero-sum directly displaces safety attention. Even if safety capabilities are distributed across many heads (per Huang et al., arXiv:2508.19697), softmax competition operates independently within each head, so distribution increases the surface area for competition rather than eliminating it. **Level 2 (Layer-level, medium form):** Different heads within shared layers; competition through residual stream — supported by Deng et al.'s Layer 13 continuation vs. Layer 25-27 safety antagonism, corroborated by ASGuard's 4 Layer-13 vulnerable heads, and by \"When Attention Closes\" finding that some architectures preserve goal information via residual streams. **Level 3 (Representation-level, weak form):** Competition through accumulated representation drift, validated by X-Boundary's success (ASR 58.5% to 16.5%). Phase 0.5 determines the relative contribution of each level per architecture — not which single level applies, but the mixture. If Qwen3-8B shows Level 1 while Llama 3.1-8B shows Level 2, this architecture-dependent competition pattern is itself a finding.\n\n**Phase 0 — CPL Acquisition/Reproduction + Baseline Preparation (weeks 1-3):** Contact Wan et al. for CPL checkpoints immediately (ICML 2026 camera-ready due May 2026; authors likely have checkpoints). Simultaneously reproduce CPL using TRL DPOTrainer + PEFT: LoRA rank-16, alpha-16, 0.4% params, DPO with beta=0.01, sigmoid loss, 2 epochs, lr=5e-7, AdamW, 1000 preference pairs per environment. Main reproduction risk: dual-rollout preference pair construction pipeline on AgentGym. Estimated: ~40 A100-hours per model. In parallel, prepare baselines: (a) XGuard-Train SFT rank-8 (published config: lr=1e-4, 3 epochs); (b) XGuard-Train SFT rank-16 (CPL-matched params); (c) **XGuard-DPO rank-16** — convert XGuard-Train safety data to DPO preference format (rejected responses generated via base model greedy decoding on harmful prompts, following standard DPO safety practice), train with CPL-identical DPO config (rank-16, beta=0.01, 2 epochs, lr=5e-7); report preference margin distributions for both CPL and XGuard-DPO pairs, with distributional differences acknowledged as inherent limitation of paradigm matching; (d) **X-Boundary** — reproduce using open-source code (GitHub: AI45Lab/X-Boundary); (e) **ToolShield** — deploy as direct inference-time baseline using open-source code (GitHub: CHATS-lab/ToolShield). Construct extended-turn variants: prepend {0, 2, 4, 6, 8} benign tool-use turns to 100 representative MT-AgentRisk tasks (stratified by risk category) for turn-count dose-response analysis.\n\n**Granular Go/No-Go Milestones:** Week 1.5: AgentGym >=3/8 environments operational. Week 2.5: dual-rollout pipeline producing valid preference pairs with measurable attention differential. Week 3: DPO training converged + base model matches Wan et al. within 1.5 SEM on >=2 environments (relaxed from 1 SEM as Plan B; approximate CPL sufficient for causal inference). 1 week buffer reserved for debugging. **Fallback paths:** (a) environment failure: proceed with 2-3 most reliable; (b) inertia differential failure: pivot to correlational-only study (Phases 1 and 4); (c) training failure: debug + 1 week → if still failing by week 4, pivot to 'DETAM in multi-turn settings.'\n\n**Phase 0.5 — Head Overlap Test and Per-Head Diagonal Attention Decomposition (weeks 3-5, ~30 A100-hours):** First per-head decomposition of diagonal attention and prerequisite test for the competition hypothesis. Using both base models on 50 MT-AgentRisk tasks. **Core tier (must complete, weeks 3-4.5):** (a) Per-head diagonal attention decomposition using Wan et al.'s metric (attention between current output position i and previous assistant output position i ±5 tokens) — the first such decomposition. (b) Ships score (Zhou et al., ICLR 2025) via KL divergence after head ablation. (c) DETAM sensitivity metric. (d) Overlap analysis: Jaccard index between top-k diagonal and top-k safety heads (k=5,10,20,50) with permutation tests on ~1024 heads per model; bootstrap CIs on per-head diagonal attention scores to confirm estimation stability from 50 tasks. Cross-validate against published localizations: Zhou et al.'s Head (2,26); Depth Charge's layer-specific data (layer 7 for Llama 3.1-8B); ASGuard's EAP-IG heads (11 heads including 4 at Layer 13). **Enhancement tier (best-effort, weeks 4.5-5, parallel with early Phase 1):** (e) AISA spatiotemporal probing (K=16); (f) CAST conflict map. If enhancement methods incomplete by week 5, proceed with triple-method results; enhancement results integrated retroactively. **Level determination:** Level 1 (>30% head overlap) → per-head softmax; Level 2 (same layers, <30% overlap) → residual stream, Layer 13 nexus; Level 3 (<10%) → representation-level. Report per-architecture level mixture rather than single determination.\n\n**Phase 1 — Correlational with Attention Capacity Analysis (weeks 5-8):** Measure diagonal attention (per-head), GAR (Dongre et al., arXiv:2605.12922), AND safety-keyword attention at each turn on 365 MT-AgentRisk tasks and extended-turn variants. **Attention capacity flow mapping:** When diagonal attention varies across turns or conditions, track where capacity flows using attention mass metric — for each token category (safety-relevant tokens identified via DETAM's intent token method + ASJA's safety keyword extraction, task tokens including tool names and parameters, formatting tokens, previous-context tokens), compute proportion of total attention allocated by high-diagonal heads (from Phase 0.5). This maps whether inertia reduction benefits safety tokens specifically or disperses broadly — fundamental to all attention-reallocation safety claims yet never measured. Fit mixed-effects models with turn position as fixed effect (linear and quadratic terms), task as random intercept, controlling for response token count. Test whether per-turn diagonal attention increase predicts safety attention decrease at same or next turn. (Note: Granger causality inappropriate for avg 3.19 turns — turn-position regression is statistically appropriate for these short sequences.)\n\n**Phase 2 — Interventional with Confound Controls (weeks 8-12):** **Manipulation check (prerequisite):** Verify CPL reduces diagonal attention on MT-AgentRisk tasks (per-head and aggregate) before interpreting safety effects. If CPL fails to reduce inertia, safety results cannot adjudicate competition hypothesis. **Eight conditions:** (a) CPL (rank-16 DPO, discourse data); (b) Random-Preference LoRA; (c) Reversed-CPL; (d) XGuard-Train SFT (rank-8, published config); (e) XGuard-Train SFT (rank-16, parameter-matched); (f) XGuard-DPO (rank-16, paradigm-matched); (g) X-Boundary (representation-level); (h) **ToolShield** (inference-time, direct comparison). Plus **CPL + ToolShield combination** to test orthogonality of training-time and inference-time defenses — additional benefit from combination would demonstrate complementary mechanisms. Plus Response-Length Analysis across all conditions. **Evaluation protocol:** Primary: GPT-4o judge with 5-point safety scale and position-swap protocol (each sample judged twice with swapped condition order; report position consistency rate). Secondary: rule-based evaluator following ToolShield's keyword matching + refusal pattern detection pipeline. Report inter-method agreement (Cohen's kappa). **Attack type coverage:** MT-AgentRisk crescendo-style (primary) + MultiBreak subset covering diverse types (attention-shifting, many-turn). **Turn-count dose-response:** 100 extended-turn tasks × {0,2,4,6,8} prepended turns — if tipping point hypothesis holds, CPL benefit is largest at high turn counts. **Per-turn safety analysis:** ASR at each turn position across conditions; CPL should show concentrated improvement in later turns. **Double dissociation potential:** The CPL vs. XGuard-DPO comparison is designed to detect whether two independent pathways to safety improvement exist — if CPL reduces inertia + improves safety while XGuard-DPO improves safety without reducing inertia, this constitutes a double dissociation between attention-reallocation and direct-safety-training mechanisms. Compare against published MUSE-D and MTSA results (indirect, with evaluation condition differences explicitly noted). **Sample size justification:** 365 tasks × 8 conditions × 2 models provides >5800 observations; published effect sizes (X-Boundary ASR Δ~35pp, MTSA Δ~51pp) indicate 365 tasks/condition detects effects >10pp at power >0.95.\n\n**Phase 2.5 — Hyperparameter Sensitivity (weeks 10-11, ~90 A100-hours):** On Llama 3.1-8B-Instruct (primary): (a) Data scaling: {250, 500, 1000, 2000} preference pairs; (b) LoRA rank: {4, 8, 16, 32}; (c) DPO beta: {0.001, 0.01, 0.05, 0.1}. On Qwen3-8B (cross-model spot-check): top-2 most sensitive axes from Llama sweep × 3 values each (~20 A100-hours), verifying sensitivity patterns are qualitatively consistent across architectures.\n\n**Phase 3 — Autonomy Tax Audit (weeks 10-12, parallel):** Step-1 completion rate, cascade failure rate, end-to-end success. **Over-refusal evaluation:** (a) OpenAgentSafety benign-intent task subset (most relevant for multi-turn agent setting); (b) OR-Bench supplementary evaluation (large-scale benign-but-sensitive queries); (c) AgentGym agentic performance change (indirect over-refusal indicator). **General capability preservation:** MMLU (knowledge) and MT-Bench (dialogue quality). Report safety-competence Pareto frontier extending Plaut's (arXiv:2603.02229) analysis. Compare frontier position with X-Boundary's ~20% over-refusal reduction, ASGuard's Pareto-optimal balance, and XGuard-SFT's published results.\n\n**Phase 4 — Mechanistic Verification (weeks 11-15):** (a) SRI signal framework for step-wise refusal dynamics; (b) Head-level analysis extending Deng et al.'s safety-continuation head identification to multi-turn, calibrated by Phase 0.5; (c) **DETAM-informed analysis:** If CPL shifts attention in same heads/direction as DETAM targets → 'implicit DETAM' through discourse training; (d) **ASGuard-informed analysis:** If CPL affects ASGuard's Layer-13 heads despite not targeting them → untargeted discourse training modifies same heads as targeted circuit surgery; (e) **Shared infrastructure hypothesis:** If (c) and (d) both positive, combined with CAST overlap from Phase 0.5 and Alignment Pretraining's independent evidence of discourse→alignment causality (arXiv:2601.10160), this constitutes convergent evidence that discourse quality and safety share attentional infrastructure — an insight with broad implications beyond this specific study; (f) Level-appropriate analysis: Level 2 → residual stream composition; Level 3 → representation trajectory per X-Boundary's framework.\n\n**Secondary Evaluation — OpenAgentSafety (weeks 13-15):** Top-3 conditions (CPL, best XGuard variant, X-Boundary) and base model on OpenAgentSafety subset for ecological validity.\n\n**Null-Result Framing Strategy:** (1) First per-head decomposition of diagonal attention and overlap with safety heads; (2) First attention capacity flow mapping — tracking where released attention goes (novel regardless of safety results and applicable to all attention-reallocation safety methods); (3) First quadruple-method safety head identification comparison (Ships + DETAM sensitivity + AISA + CAST), cross-validated against four published head sets; (4) Architecture-dependent competition level mixture analysis; (5) First paradigm-controlled comparison (XGuard-DPO) isolating data source from training paradigm; (6) First multi-turn extension of DETAM's Focus Loss analysis; (7) Empirical test of untargeted vs. targeted head modification; (8) Turn-count dose-response testing tipping point predictions; (9) Capacity flow direction analysis. If CPL reduces inertia but not safety → competition hypothesis weakened (standalone finding). If CPL fails to reduce inertia on safety tasks → experiment cannot adjudicate (needs stronger intervention).\n\n**Extended-Turn Variant Validity (Limitation):** Acknowledged with mitigations: OpenAgentSafety for ecological validity, attention pattern validation, conservative amplification framing. Dose-response design ({0,2,4,6,8} turns) tests monotonicity consistent with tipping point predictions.\n\nAll primary experiments use MT-AgentRisk (365 tasks), ToolShield codebase (GitHub: CHATS-lab/ToolShield), XGuard-Train (HuggingFace: marslabucla/XGuard-Train), X-Boundary (GitHub: AI45Lab/X-Boundary), and the CPL training recipe from Wan et al. (ICML 2026).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '980-1200 A100-hours (CPL reproduction 2 models ~80h, XGuard-SFT rank-8 + rank-16 training 2 models ~60h, XGuard-DPO rank-16 2 models ~40h, X-Boundary reproduction 2 models ~40h, 2 control LoRAs 2 models ~80h, Phase 0.5 head overlap core+enhancement ~35h, MT-AgentRisk evaluation 8 conditions × 2 models + ToolShield combo ~320h, extended-turn dose-response 100 tasks × 5 turn-counts × key conditions ~80h, MultiBreak subset ~40h, OpenAgentSafety top-3 conditions ~60h, SRI signal analysis ~30h, attention analysis including per-head diagonal + GAR + capacity flow mapping + DETAM/ASGuard-informed ~110h, hyperparameter sensitivity Llama full + Qwen spot-check ~90h, general capability MMLU + MT-Bench ~25h, over-refusal OR-Bench ~10h)', 'timeline': '16-18 weeks (3 weeks Phase 0 + go/no-go, 2 weeks Phase 0.5, 3 weeks Phase 1, 4 weeks Phase 2 + Phase 2.5 + Phase 3 parallel, 4 weeks Phase 4 + OpenAgentSafety, 3 weeks writing; 1 week buffer for CPL debugging)', 'estimated_gpu_cost': '$1470-1800 at $1.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': '980-1200 A100-hours', 'timeline': '14-16 weeks (Claude accelerates CPL reproduction, quadruple-method pipeline, capacity flow analysis, statistical modeling)', 'claude_api_cost': '$450-600', 'estimated_gpu_cost': '$1470-1800 at $1.50/A100-hr spot pricing'}, 'auto_research': {'gpu_hours': '1200-1500 A100-hours (additional automated sweeps, full OpenAgentSafety, extended ablation, comprehensive analysis)', 'timeline': '10-12 weeks (parallelized execution)', 'claude_api_cost': '$750-1000', 'estimated_gpu_cost': '$1800-2250 at $1.50/A100-hr spot pricing', 'speed_bottleneck': 'Sequential multi-turn generation; 16 model configurations (2 models × 8 conditions); Phase 0.5 serial dependency; quadruple-method analysis'}}\n\n## Inspired By\nField guide Section 4 (cascading failures, production gap) + Section 5.2 (error propagation). Key insight: DETAM's inference-time attention reallocation (ASR 46%→1.2%) establishes that redirecting attention improves safety — does implicit redirection via discourse training also work? ASGuard's training-time head modification for specific vulnerabilities raises: can untargeted training achieve the same for progressive erosion? The three-level competition hierarchy reflects Wan et al.'s aggregate-only characterization and safety heads spanning L2, L9-14, L25-27, while continuation heads at Layer 13 overlap with ASGuard's vulnerable heads. Johnson & Huo's (2026) tipping points provide theoretical framework. Dongre et al.'s architecture-dependent failure modes (arXiv:2605.12922) motivate per-architecture level mixture analysis. CAST's conflict map (arXiv:2601.04262) enables testing whether safety-utility, safety-inertia, and safety-discourse conflicts converge on shared heads. Alignment Pretraining's (arXiv:2601.10160) demonstration that discourse-level data properties causally affect alignment through pretraining content provides independent evidence for discourse→safety pathways, complementing our post-training attention mechanics pathway. The observation that no prior work tracks where released attention capacity actually flows (DETAM, ASGuard, AISA all measure safety attention improvement but not capacity source) motivated capacity flow mapping as a core methodological contribution.\n\n## Target Venues\n- ICLR 2027 (abstract September 19 2026, full paper September 24 2026 [estimated] — primary target, comfortable timeline with Phase 0.5 extension)\n- AAAI 2027 (abstract July 21 2026, full paper July 28 2026 — stretch target, feasible only if CPL checkpoints obtained early and Phase 0.5 shows Level 1/2 overlap)\n\n## Key References\n- DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings, arXiv:2504.13562)\n- ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026, arXiv:2509.25843)\n- AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks (Song et al., arXiv:2602.13547, Feb 2026)\n- Multi-Turn Jailbreaking Large Language Models via Attention Shifting (ASJA, AAAI 2025)\n- Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026, arXiv:2602.03664)\n- Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents (Yang et al., arXiv 2026)\n- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents (COLM 2025, arXiv:2504.13203)\n- MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety (EMNLP 2025, arXiv:2509.14651)\n- X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability (Lu et al., EMNLP 2025, arXiv:2502.09990)\n- MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming (Guo et al., ACL 2025, arXiv:2505.17147)\n- Agent Safety Alignment via Reinforcement Learning (Sha et al., arXiv:2507.08270)\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut, arXiv:2603.02229, March 2026)\n- The Struggle Between Continuation and Refusal (Deng et al., arXiv:2603.08234, Mar 2026)\n- The Autonomy Tax: Defense Training Breaks LLM Agents (Li & Zhao, arXiv:2603.19423, Mar 2026)\n- On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025, arXiv:2410.13708)\n- Depth Charge: Jailbreak Large Language Models from Deep Safety Attention Heads (Wu et al., arXiv:2603.05772, Mar 2026)\n- Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., arXiv:2508.19697, 2025)\n- Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, arXiv:2602.14370, Feb 2026)\n- Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment (Zaree et al., arXiv:2502.15334, Feb 2025)\n- Safety Layers in Aligned Large Language Models (Wei et al., arXiv:2408.17003, 2024)\n- Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., arXiv:2406.11717, 2024)\n- State-Dependent Safety Failures in Multi-Turn Language Model Interaction (STAR, arXiv:2603.15684, Mar 2026)\n- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026, arXiv:2507.06134)\n- One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue (TurnGate, arXiv:2605.05630, May 2026)\n- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv:2605.01687, May 2026)\n- STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (arXiv:2506.00668, May 2025)\n- When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction (Dongre et al., arXiv:2605.12922, May 2026)\n- Safety-Utility Conflicts Are Not Global: Surgical Alignment via Head-Level Diagnosis (CAST, arXiv:2601.04262, Jan 2026)\n- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (Tice et al., arXiv:2601.10160, Jan 2026)\n- Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions (arXiv 2026)\n- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2026)\n- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv 2025)\n- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction (arXiv 2026)\n- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv 2026)\n- Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction (arXiv 2026)\n- Asking Forever: Universal Activations Behind Turn Amplification (arXiv:2602.17778, Feb 2026)\n- Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models (arXiv:2602.02600, Feb 2026)\n- Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection (arXiv:2604.28129, Apr 2026)\n- Many-Turn Jailbreaking (arXiv:2508.06755, Aug 2025)\n- Disentangling Length from Quality in Direct Preference Optimization (Park et al., arXiv:2403.19159, 2024)\n- Length Desensitization in Direct Preference Optimization (Meng et al., arXiv:2409.06411, 2024)\n- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., USENIX Security 2025, arXiv:2404.01833)"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:47:14.312Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:47:14.312Z",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T04:47:14.327Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to produce the evaluation. Let me synthesize my findings.

---

```
【阶段】: Triage

【领域调研】:
- [Wan et al., "Mitigating Conversational Inertia in Multi-Turn Agents"](https://arxiv.org/abs/2602.03664) (ICML 2026): 本 proposal 的核心依赖。提出 diagonal attention 与 CPL 干预，但仅在 agentic task performance 上验证，从未评估 safety 效果。Aggregate-level 分析，无 per-head decomposition。代码未公开。
- [Li et al., "DETAM"](https://arxiv.org/abs/2504.13562) (ACL 2025 Findings): 推理时 attention reallocation 防御，ASR 46%→1.2%，建立了 attention 再分配→safety 提升的因果证据。但限于 single-turn，需 runtime 识别 intent tokens。
- [Park et al., "ASGuard"](https://arxiv.org/abs/2509.25843) (ICLR 2026): 训练时 circuit-targeted head scaling，ASR 42%→8%，识别 Layer 13 的 4 个 vulnerable heads。但针对特定可定位的攻击电路，非 discourse-level 动态。
- [Zhou et al., "On the Role of Attention Heads in LLM Safety"](https://arxiv.org/abs/2410.13708) (ICLR 2025): 单个 safety head 消融即可使 harmful queries 应答增加 16×，safety head 分布高度模型依赖。本 proposal 的 Phase 0.5 cross-validation 依据之一。
- [Dongre et al., "When Attention Closes"](https://arxiv.org/abs/2605.12922) (arXiv 2026.05): 提出 GAR 度量 multi-turn attention 衰减，发现 architecture-dependent failure modes。非常新的工作（2026年5月），与本 proposal 互补。
- [Yang et al., "MT-AgentRisk / ToolShield"](https://unsafer-in-many-turns.github.io/) (arXiv 2026): 365-task multi-turn safety benchmark + inference-time defense（ASR 降低 ~30%）。本 proposal 的主要评测平台。
- [Lu et al., "X-Boundary"](https://arxiv.org/abs/2502.09990) (EMNLP 2025): Representation-level boundaries，ASR 58.5%→16.5%。本 proposal 的直接 baseline 之一。
- [Guo et al., "MTSA"](https://arxiv.org/abs/2505.17147) (ACL 2025): RL-based multi-turn alignment，ASR 74.5%→23.5%。另一个重要 baseline。
- **调研中未发现直接竞争工作**：没有任何已发表或 arXiv 工作测试过"untargeted discourse training → safety improvement via attention reallocation"这一路径。per-head diagonal attention decomposition 和 attention capacity flow mapping 确实是未被做过的。

- 调研总结: multi-turn safety 是一个快速增长的领域，2025-2026年涌现了大量攻击、防御和机理分析工作，但均在"直接用 safety 数据训练"或"推理时干预"范式内。本 proposal 提出的"untargeted discourse training 间接改善 safety"路径确实是一个未被探索的空白，核心 novelty claim 成立。

【整体印象】:
作为审稿人，我的第一反应是：这是一个极其雄心勃勃、文献调研深入、实验设计严谨的 proposal，核心研究问题（untargeted discourse 训练能否通过 attention reallocation 因果性地改善 multi-turn safety）是真正新颖的。然而，我也会立即产生两个担忧：(1) scope 过于庞大——5+ phases、8 conditions、4 种 head identification 方法、3-level hypothesis 框架、多个 benchmark，这对一篇论文来说可能过度；(2) 核心假设高度投机性——没有任何初步证据表明 CPL 会影响 safety，整个 5-phase 研究建立在一个未验证的 bridge hypothesis 之上。总体倾向：**borderline**，如果执行良好且结果清晰，有可能 accept；但执行风险高，呈现不当则很容易 reject。

【核心贡献】:
1. **首个因果性测试**：untargeted discourse training (CPL) 是否通过 attention reallocation 机制改善 multi-turn safety——这是一个干净、未被探索的研究问题。
2. **方法论贡献**：per-head diagonal attention decomposition（首次）、attention capacity flow mapping（首次）、四方法 safety head 对比——这些无论主假设结果如何都有独立价值。
3. **Paradigm-controlled comparison**：CPL vs. XGuard-DPO（同一 DPO 框架、不同数据源）实现训练范式与数据来源的解耦，实验设计巧妙。

贡献价值评估：如果主假设成立（CPL 确实通过 attention reallocation 改善 safety），这将是一个高影响力发现，连接了 discourse quality 和 safety 两个独立的研究方向。即使主假设不成立，方法论贡献仍有中等价值。但单靠方法论贡献（per-head decomposition 等）撑不起一篇 top venue 论文——需要有实质性的正面或负面发现。

【方法合理性】:
方法整体合理，有几个亮点和隐患：

**亮点：**
- Manipulation check 设计：先验证 CPL 是否降低了 diagonal attention，再解释 safety 效果——这是标准的因果推断方法论，很多 ML 论文忽略这一步。
- Double dissociation 设计：CPL (discourse data + DPO) vs. XGuard-DPO (safety data + DPO) 可以分离数据源和训练范式的效果。
- 多种控制条件（Random-Preference LoRA, Reversed-CPL）排除 trivial 解释。

**隐患：**
- **CPL 复现是最大风险**：代码未公开，需要复现 dual-rollout preference pair construction pipeline on AgentGym。如果复现的 CPL 效果不好，整个研究的因果推断基础就不牢固。
- **Three-level framework 的可证伪性存疑**：Level 1/2/3 覆盖了所有可能的结果——高重叠是 Level 1，中等是 Level 2，低重叠是 Level 3——这使得假设几乎不可能被否证。一个好的因果假设应该有明确的否定条件。
- **更简单的替代方案**：是否可以直接在 CPL 前后对比 DETAM 的 Focus Loss 指标，而不需要如此复杂的多 phase 设计？很多 phase 的贡献可以被更简洁的实验替代。
- **Preference pair 分布差异**：CPL 和 XGuard-DPO 的 preference margin 分布不同是 proposal 自己承认的 limitation，但这直接影响 double dissociation 的解释力。

【5 维度打分】:

1. 研究问题: 【强】— "untargeted discourse training 能否因果性地改善 multi-turn safety" 是一个干净、新颖、有价值的研究问题。它连接了两个独立发展的研究线（discourse quality / safety alignment），且有明确的实际意义（如果成立，意味着可以通过改善对话质量间接提高安全性，无需昂贵的 safety-specific 数据标注）。调研确认该问题未被任何已有工作回答。

2. 方法与创新: 【中偏强】— 核心创新点（将 CPL 应用于 safety 评估 + per-head decomposition + capacity flow mapping）是真正新颖的，调研中未发现直接竞争工作。实验设计中的 manipulation check、paradigm-controlled comparison、double dissociation 体现了强方法论素养。但 Three-level framework 的可证伪性不足，且 CPL 本身不是本工作的贡献（是 Wan et al. 的方法），本工作更多是在"应用+分析"层面。与 DETAM（推理时）、ASGuard（训练时 targeted）、X-Boundary（representation level）相比，本工作的方法论 delta 主要在分析框架而非新算法。

3. 实验设计: 【强】— 这是本 proposal 最突出的优点之一。8 个实验条件（含控制组）、paradigm-matched comparison、manipulation check、turn-count dose-response、多 benchmark（MT-AgentRisk + OpenAgentSafety + MultiBreak 子集）、over-refusal 评测、capability preservation（MMLU + MT-Bench）、hyperparameter sensitivity、multiple evaluation protocols（GPT-4o judge + rule-based + inter-method agreement）。与领域内已有工作相比（DETAM 仅 single-turn benchmark、ASGuard 4 个模型但 single-turn、X-Boundary 无 dose-response），本 proposal 的实验设计显著更全面。样本量和统计功效分析也到位。Null-result 策略有 9 个独立贡献点，比大多数 proposal 考虑得周到。

4. 可行性: 【中】— 资源需求合理（~1000-1200 A100-hours，$1500-1800），timeline 有缓冲。但存在关键风险：(a) CPL 复现依赖未公开代码和 AgentGym 环境搭建；(b) 16-18 周的 timeline 意味着如果目标是 EMNLP 2026（通常 deadline 在 2026 年 6 月左右），时间上不可行——proposal 本身目标是 ICLR 2027（2026年9月）；(c) 整体 scope 极大，5 个 phase 中任何一个延迟都会级联影响后续；(d) "联系 Wan et al. 获取 checkpoint" 是不确定性极高的依赖。

5. 写作与呈现: 【中偏弱】— Proposal 本身信息密度极高、文献引用详尽，体现了深入的领域理解。但同时也暴露了呈现风险：(a) 过度堆砌——一个 proposal 引用了 40+ 篇论文，几乎每一句都有 citation，这在实际论文中会让审稿人疲劳；(b) 核心 story 被埋没在大量细节中——"untargeted discourse training → safety via attention reallocation" 这个简洁的核心叙事被 five-phase design、three-level framework、quadruple-method triangulation 等复杂设计淹没；(c) 8 页 EMNLP 论文中很难容纳如此多的内容，必须大幅精简；(d) 某些术语（如"quadruple triangulation"、"attention capacity competition hypothesis"）增加了不必要的认知负担。

【概率估计】: [25% - 38%] 中位 30%

【估计理由】:
- **上行因素 (→38%)**：核心 novelty 真正成立（调研确认无竞争工作）；研究问题重要且 timely；实验设计严谨程度超过领域平均水平；即使负面结果也有方法论贡献。如果执行良好、写作精炼、结果清晰，有实力进入 borderline accept 区间。
- **下行因素 (→25%)**：核心假设高度投机、无初步证据支撑，审稿人可能认为这是 "fishing expedition"；scope 过大导致论文展开不充分或审稿人无法 follow；CPL 复现失败的实际可能性；three-level framework 的不可证伪性可能被审稿人视为方法论弱点；presentation 过于复杂的风险。
- **中位推理 (30%)**：在 EMNLP 2026 的安全 / 可解释性 track 中，这个 novelty 水平和实验设计深度属于"above average submission but with significant execution risk"。领域内已有大量 multi-turn safety 工作（X-Boundary、MTSA、MUSE-D 等），竞争激烈。如果实验结果干净（CPL 确实降低 inertia 且改善 safety），则 30% 偏上界；如果实验结果混杂（CPL 降低 inertia 但 safety 改善不显著，或改善可归因于 DPO 训练本身），则 30% 偏下界。

【主要风险】:
1. **核心假设落空 + 方法论贡献不足以独立支撑**：如果 CPL 未能有效降低 safety 任务上的 diagonal attention，或降低后 safety 无显著改善，剩下的 per-head decomposition 和 capacity flow mapping 虽有新颖性，但在独立性和影响力上可能不足以支撑一篇 top venue 论文——审稿人可能评价为 "interesting analysis but no actionable insight"。
2. **Scope 过大导致论文不聚焦**：5+ phases、8 conditions、4 种 head identification 方法、3-level framework 在 8 页正文中难以清晰展开。审稿人极可能抱怨 "too many moving parts"、"hard to follow the main contribution"，甚至怀疑作者是否真的能在有限篇幅内充分呈现所有实验结果和分析。

【实施评估】:
  - 计算资源: ~980-1200 A100-hours（约 $1500-1800），对于有 GPU 集群访问的研究组是合理的，但对于个人研究者可能偏高。
  - 数据需求: 主要依赖公开 benchmark（MT-AgentRisk 365 tasks、OpenAgentSafety 356 tasks、MultiBreak 10,389 prompts）和公开模型（Qwen3-8B、Llama 3.1-8B），数据获取无障碍。CPL 训练需要 AgentGym 环境构建 preference pairs。
  - 人工介入: GPT-4o 评审需要 API 调用成本；AgentGym 环境搭建可能需要较多调试；quadruple-method head analysis 需要实现 4 种不同的 head identification 方法。整体人工介入程度中等偏高。
  - 训练需求: 需要训练 CPL（LoRA rank-16 DPO）、XGuard-SFT（两个配置）、XGuard-DPO、两个控制 LoRA，共 ~6 个 LoRA 模型 × 2 base models = ~12 次训练。不需要从头预训练。
  - 新 Benchmark: 不需要构建新 benchmark，但需要构造 extended-turn variants（100 tasks × 5 turn-counts），这属于数据增强而非新 benchmark。
  - 预估周期: 16-18 周（含 1 周 buffer）。对于 EMNLP 2026（若 deadline ~2026年6月），时间不足；proposal 自身定位 ICLR 2027（2026年9月 deadline），timeline 勉强可行但紧张。
```

Sources:
- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026)](https://arxiv.org/abs/2602.03664)
- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)
- [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026)](https://arxiv.org/abs/2509.25843)
- [On the Role of Attention Heads in LLM Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)
- [When Attention Closes (Dongre et al., arXiv 2026)](https://arxiv.org/abs/2605.12922)
- [MT-AgentRisk / ToolShield](https://unsafer-in-many-turns.github.io/)
- [X-Boundary (Lu et al., EMNLP 2025)](https://arxiv.org/abs/2502.09990)
- [MTSA (Guo et al., ACL 2025)](https://arxiv.org/abs/2505.17147)
- [Awesome Attention Heads Survey](https://github.com/IAAR-Shanghai/Awesome-Attention-Heads)
- [Multi-Turn Jailbreak Attacks Topic](https://www.emergentmind.com/topics/multi-turn-jailbreak-attacks)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient field context. Let me compile the comprehensive evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Wan et al., "Mitigating Conversational Inertia in Multi-Turn Agents", arXiv:2602.03664] (ICML 2026): 提出 conversational inertia 概念和 CPL 干预，但仅在 agentic performance 上评估，从未涉及 safety，且 diagonal attention 仅有 aggregate-level 刻画。确认 proposal 关于"CPL 未评估 safety"及"无 per-head decomposition"的 novelty claim 成立。
- [Li et al., "DETAM", arXiv:2504.13562] (ACL 2025 Findings): 通过 inference-time attention reallocation（修改 causal mask）实现 ASR 46%→1.2%。确认其为 single-turn only，需 runtime intent token identification。Proposal 对其局限性的分析准确。
- [Park et al., "ASGuard", arXiv:2509.25843] (ICLR 2026): 通过 circuit-level channel-wise scaling 修改 safety-vulnerable heads，ASR 42%→8%。确认其针对特定 attack types 的 localizable circuits，proposal 对其"efficacy hinges on localizable circuits"的论断准确。
- [Dongre et al., "When Attention Closes", arXiv:2605.12922] (2026): 提出 GAR 指标，发现 architecture-dependent failure modes。非常新的工作（2026年5月），proposal 对其整合合理。
- [Johnson & Huo, arXiv:2602.14370] (2026): 从物理学角度形式化 attention competition tipping points。理论框架但缺乏 NLP 社区的实证验证，proposal 试图提供这种验证。
- [CAST, arXiv:2601.04262] (2026): Head-level conflict map 用于 safety-utility 冲突诊断。与 proposal 的 quadruple-method 头识别比较相关。
- [X-Boundary, arXiv:2502.09990] (EMNLP 2025): Representation-level 边界，ASR 58.5%→16.5%。作为 proposal 的 baseline 之一。
- [MTSA, arXiv:2505.17147] (ACL 2025): RL-based multi-turn alignment，ASR 74.5%→23.5%。代表 safety-labeled data 训练路线。
- [Huang et al., arXiv:2508.19697] (2025): 提出 AHD 将 safety 分布到更多头。与 proposal 的 competition hypothesis 形成有趣对话。
- [Alignment Pretraining, arXiv:2601.10160] (2026): 展示 pretraining discourse 内容因果影响 alignment（misalignment 45%→9%）。为 discourse→safety pathway 提供独立证据，但通过 data content 而非 attention mechanics。
- 调研总结: 多轮安全退化的 attention 机制解释（DETAM/ASGuard/ASJA）和多轮安全防御（X-Boundary/MTSA/MUSE-D）已有成熟工作，但"untargeted discourse intervention → safety via attention reallocation"这条因果链确实无人验证。per-head diagonal attention decomposition 和 capacity flow mapping 确为方法论空白。Proposal 在这个交叉点上有真实的 novelty 空间。

【整体印象】:
作为审稿人，第一反应是：这是一个研究品味很好、文献功底极深的 proposal，研究问题genuinely interesting（untargeted discourse training 是否通过 attention reallocation 因果地影响 safety），方法论贡献（per-head decomposition、capacity flow mapping）有独立价值。但这个 proposal 的最大问题是 **scope 严重超载**——五个主相位（0, 0.5, 1, 2, 3, 4）加上 2.5 和二级评估，8 个实验条件，4 种 head identification 方法，2 个模型，3+ 个 benchmark，hyperparameter sensitivity sweep……这更像一个 2 年的 research program 而非一篇论文。我会倾向给 **borderline**（weak accept / weak reject），取决于最终呈现能否聚焦。

【核心贡献】:
1. **因果检验**：首次测试 untargeted discourse intervention（CPL）是否通过 attention reallocation 因果地改善多轮安全——这是一个有价值的实验问题，因为它桥接了 discourse dynamics 和 safety mechanisms 两个原本分离的文献。
2. **方法论贡献**：per-head diagonal attention decomposition（Wan et al. 仅有 aggregate）；attention capacity flow mapping（DETAM/ASGuard/AISA 都未追踪释放的 attention 流向何处）；quadruple-method safety head comparison。这些无论 safety 结果如何都有价值。
3. **范式控制的 double dissociation 设计**：CPL vs. XGuard-DPO 对比在相同训练范式下隔离数据来源的效应，实验设计巧妙。

贡献价值：如果执行到位且结果明确，对领域有中等偏上的价值——它不会改变 safety 研究的基本范式，但会为 attention-based safety 理解增加重要的 mechanistic 证据，并提供有用的方法论工具。

【方法合理性】:
方法的核心逻辑是合理的：如果 diagonal attention（inertia）与 safety attention 在 softmax zero-sum 约束下竞争，那么减少 inertia 应当释放 attention 给 safety tokens。CPL 作为干预是合理选择，因为它是唯一已验证的训练级 inertia reduction 方法。

但有几个值得质疑的点：
1. **因果归因的挑战**：即使 CPL 同时减少 inertia 和改善 safety，因果链可能不是 "inertia↓ → safety attention↑ → safety↑"，而是 DPO 训练的其他效应（如更好的 instruction following、更短的回复等）同时影响两者。Paradigm-matched XGuard-DPO 控制有帮助但不完全解决——因为 CPL 和 XGuard-DPO 的 preference data 分布不同（proposal 也承认了这一点）。
2. **三层竞争假设的可证伪性**：Level 1/2/3 的框架覆盖了几乎所有可能的竞争模式——如果 head overlap 高是 Level 1，中等是 Level 2，低是 Level 3。这种全覆盖框架很难被 falsify，削弱了假设的锐利度。
3. **是否有更简单的替代方案**：直接在 CPL 的 DPO 训练中加入少量 safety preference pairs（mixed training）来测试 discourse + safety 的交互效应，可能比五阶段实验更高效地回答核心问题。不过 proposal 的设计确实提供了更丰富的 mechanistic 理解。

【5 维度打分】:

1. 研究问题: [强] — 多轮安全退化的 attention 机制是 2025-2026 的热门方向（DETAM, ASGuard, ASJA, Deng et al. 等大量相关工作），"untargeted discourse intervention 是否因果影响 safety"是一个自然但尚未被测试的问题。问题定位精准，抓住了 discourse dynamics 和 safety mechanisms 文献的交叉空白。

2. 方法与创新: [中偏强] — Per-head diagonal attention decomposition 确实是 Wan et al. 未做的有价值扩展；capacity flow mapping 填补了 DETAM/ASGuard/AISA 的方法空白；paradigm-matched DPO comparison 设计巧妙。但核心 novelty（用 CPL 测 safety）更像是"obvious next step"而非深层创新——Wan et al. 提出 CPL 后，自然有人会测其 safety 效应。三层竞争假设虽有理论价值但 unfalsifiable 设计削弱了 contribution。与 Alignment Pretraining (arXiv:2601.10160) 的 discourse→alignment 因果路径相比，proposal 的路径（post-training attention mechanics）是互补但更窄。

3. 实验设计: [强] — 这是 proposal 最突出的优势。8 个实验条件涵盖了几乎所有合理对照（random LoRA, reversed-CPL, parameter-matched SFT, paradigm-matched DPO, representation-level baseline, inference-time baseline, combination test）。Manipulation check 设计（先验证 CPL 确实减少 inertia 再解读 safety）是方法论上的亮点。Dose-response 测试 tipping point 预测、per-turn ASR 分析、over-refusal 评估（OpenAgentSafety + OR-Bench）都很周全。与 MTSA（ASR 74.5%→23.5%）、X-Boundary（ASR 58.5%→16.5%）、ASGuard（ASR 42%→8%）等已发表工作的 baseline 标准相比，proposal 的实验设计达标甚至超标。但 scope 过大是双刃剑——执行风险高。

4. 可行性: [中偏弱] — 主要风险：(a) CPL 代码未发布，reproduction 是整个研究的前提，Phase 0 失败则全盘皆输；(b) 16-18 周完成这个规模的实验在资源受限条件下非常紧张；(c) ~1000-1200 A100-hours 的 GPU 预算对于 8 conditions × 2 models + 大量分析是偏紧的估计；(d) AgentGym 环境的 dual-rollout pipeline 可能不稳定；(e) EMNLP 2026 的 ARR 提交截止日为 2026 年 5 月 25 日（距今仅 5 天），即使后续 ARR cycle 可 commit 到 EMNLP 2026，该 proposal 的 16-18 周时间线意味着最早 9-10 月完成，无法赶上 EMNLP 2026（但这是物流问题，不影响学术质量评估）。Go/no-go milestones 和 fallback paths 设计合理，但 fallback（"pivot to correlational-only study"）会大幅削弱 contribution。

5. 写作与呈现: [中] — 文献综述极其详尽，体现了深厚的学术功底。但 proposal 过于冗长密集，核心叙事线被大量细节淹没。一个审稿人读完后可能的反应是"这里有很多好想法，但我不确定这篇论文到底要讲什么核心故事"。需要显著精简，提炼出 1-2 个核心贡献作为主线，其余作为 supplementary。三层竞争假设的呈现方式也过于框架化，给人"理论先行"的感觉。

【概率估计】: [25% - 38%] 中位 30%

【估计理由】:
研究问题有真实的 novelty 空间（强），实验设计非常完备（强），方法论贡献有独立价值。这些因素将概率推向 30%+。但以下因素将概率拉低：(1) scope 严重超载——这个规模的实验计划如果不大幅精简，成稿后很可能不聚焦，审稿人会抱怨"tries to do too much"；(2) 核心 novelty 的"obvious next step"感——在 Wan et al. 之后测 CPL 的 safety 效应是自然的延伸而非深层创新；(3) 可行性风险——CPL 复现是前提条件，失败则 pivoting 后贡献大打折扣；(4) 三层竞争假设的 unfalsifiability 问题会被 mechanistic interpretability 方向的审稿人质疑；(5) 因果归因的挑战——即使所有实验都跑通，CPL 的多重效应使得"inertia reduction → safety improvement"的因果链难以 clean 地建立。中位估计 30% 反映了"方向正确、设计出色但执行和聚焦风险显著"的判断。如果作者能将论文聚焦到 Phase 0.5 + Phase 1 + Phase 2 的核心实验（per-head decomposition + correlational + interventional），精简到 8 页主体 + appendix，概率可提升至 35-40%。

【主要风险】:
1. **Scope 过大导致论文不聚焦**：五阶段实验 + 四种 head identification 方法 + 三层竞争假设 + 多个 benchmark，审稿人极有可能给出"ambitious but unfocused"的评价，这是 EMNLP/ACL 类会议 reject 的常见原因。
2. **CPL 复现失败或因果归因不清晰**：整个研究建立在 CPL 成功复现的前提上（代码未发布），且即使 CPL 同时减少 inertia 和改善 safety，paradigm-matched 控制也无法完全排除 DPO 训练的其他混淆效应，审稿人可能认为因果证据不够 conclusive。

【实施评估】:
  - 计算资源: ~1000-1200 A100-hours（$1500-1800），对学术实验室偏重但可行；主要瓶颈在 8 conditions × 2 models 的组合爆炸和多阶段 attention 分析
  - 数据需求: MT-AgentRisk (365 tasks, 公开), OpenAgentSafety (356 tasks, 公开), MultiBreak (10,389 prompts, 公开), XGuard-Train (HuggingFace 公开), OR-Bench (公开)。CPL 的 preference pair 构建需要 AgentGym 环境 + dual-rollout pipeline（高技术风险）
  - 人工介入: 中等——CPL 复现需手动调试 AgentGym pipeline；extended-turn variant 构建需半手动设计；GPT-4o judge 需 API 成本和 prompt 工程
  - 训练需求: 需训练 ~8 个 LoRA 模型（CPL ×2 models, XGuard-SFT rank-8/16 ×2, XGuard-DPO ×2, Random-LoRA ×2, Reversed-CPL ×2）+ hyperparameter sweep ~16 个额外模型
  - 新 Benchmark: 无需构建全新 benchmark，但 extended-turn variants（0/2/4/6/8 prepended turns × 100 tasks）需要半自动构建
  - 预估周期: 16-18 周（proposal 自估），实际更可能 20-24 周，考虑到 CPL 复现风险和 Phase 0 的 serial dependency
```

Sources:
- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026)](https://arxiv.org/abs/2602.03664)
- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)
- [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026)](https://arxiv.org/abs/2509.25843)
- [When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction (Dongre et al., 2026)](https://arxiv.org/abs/2605.12922)
- [Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, 2026)](https://arxiv.org/abs/2602.14370)
- [X-Boundary: Establishing Exact Safety Boundary (Lu et al., EMNLP 2025)](https://arxiv.org/abs/2502.09990)
- [MTSA: Multi-turn Safety Alignment (Guo et al., ACL 2025)](https://arxiv.org/abs/2505.17147)
- [Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., 2025)](https://arxiv.org/abs/2508.19697)
- [Safety-Utility Conflicts Are Not Global: CAST (2026)](https://arxiv.org/abs/2601.04262)
- [Alignment Pretraining (Tice et al., 2026)](https://arxiv.org/abs/2601.10160)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [On the Role of Attention Heads in LLM Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)
- [Unsafer in Many Turns: MT-AgentRisk (Yang et al., 2026)](https://arxiv.org/abs/2602.13379)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient field context. Let me compile my comprehensive evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Wan et al., "Mitigating Conversational Inertia in Multi-Turn Agents" (ICML 2026, arXiv:2602.03664)]: 本 proposal 的核心基础工作。提出 diagonal attention（conversational inertia）现象和 CPL 干预方法。仅在 agentic performance 上验证，未涉及 safety。Aggregate-level 注意力分析，未做 per-head decomposition。代码未公开。
- [Li et al., "DETAM" (ACL 2025 Findings, arXiv:2504.13562)]: 单轮 inference-time attention reallocation 防御，ASR 46%→1.2%。证明 attention redistribution 因果性改善安全性，但依赖运行时 intent token 识别，无法扩展到 multi-turn。
- [Park et al., "ASGuard" (ICLR 2026, arXiv:2509.25843)]: Training-time circuit-targeted head scaling，ASR 42%→8%。识别 Layer-13 关键 heads。但仅针对特定可定位的攻击类型（如 tense-changing），不处理渐进式 discourse erosion。
- [Zhou et al., "On the Role of Attention Heads in LLM Safety" (ICLR 2025, arXiv:2410.13708)]: Ships score 评估 head 安全贡献，发现安全头集中在少量 heads。为 Phase 0.5 head overlap 分析提供基础方法。
- [Huang et al., "Safety Alignment Should Be Made More Than Just A Few Attention Heads" (arXiv:2508.19697)]: 提出 AHD 分布安全能力到更多 heads，与本 proposal 的 competition hypothesis 形成有趣张力。
- [Deng et al., "The Struggle Between Continuation and Refusal" (arXiv:2603.08234)]: 识别 safety heads (L25-27) vs. continuation heads (~L13) 的竞争，与 ASGuard 的 L13 vulnerable heads 吻合。直接支持 competition mechanism。
- [Lu et al., "X-Boundary" (EMNLP 2025, arXiv:2502.09990)]: Representation-level boundary 防御，ASR 58-76%→16-25%，over-refusal 减少~20%。作为 Level 3 (representation-level) baseline。
- [Guo et al., "MTSA" (ACL 2025, arXiv:2505.17147)]: Multi-turn RL safety alignment，ASR 74.5%→23.5%，peak attack at round 5。直接竞争者但使用 safety-labeled 数据。
- [COLM 2025, "X-Teaming/XGuard-Train" (arXiv:2504.13203)]: Multi-turn safety SFT baseline，up to 48.3% vulnerability reduction。
- [MUSE-D (EMNLP 2025, arXiv:2509.14651)]: Turn-level DPO，24% ASR reduction。直接 multi-turn DPO baseline。
- [Yang et al., "MT-AgentRisk/ToolShield" (arXiv:2602.13379)]: 365-task benchmark + inference-time 防御（~30% ASR reduction）。Proposal 的主要评测平台。开源可用。
- [Dongre et al., "When Attention Closes" (arXiv:2605.12922)]: GAR 指标衡量 goal-token attention degradation，发现 architecture-dependent failure modes。补充性指标。
- [CAST (arXiv:2601.04262)]: Head-level conflict map，发现 utility degradation 集中在少量 high-conflict heads。为 quadruple-method triangulation 提供第四种方法。
- [Tice et al., "Alignment Pretraining" (arXiv:2601.10160)]: Discourse-level pretraining data 因果影响 alignment (misalignment 45%→9%)。独立证据支持 discourse→safety pathway 存在性。
- [Johnson & Huo (arXiv:2602.14370)]: Attention competition tipping point 理论框架。为 dose-response 实验设计提供理论依据。

- 调研总结: Multi-turn safety 是 2025-2026 快速增长的研究方向，已有多种防御方法（XGuard、MUSE-D、X-Boundary、MTSA、ToolShield），但均直接使用 safety-labeled 数据。Attention mechanism 在 safety 中的角色已被充分研究（DETAM、ASGuard、Zhou、AISA），但"discourse-level 非安全干预能否因果性改善 safety"这一假设确实 **未被测试过**。Per-head diagonal attention decomposition 和 attention capacity flow mapping 在文献中确实不存在。Proposal 精准定位了一个真实且重要的研究空白。

【整体印象】: 
作为审稿人，我的第一反应是"研究问题有真正的 novelty，实验设计令人印象深刻地严谨，但整体范围极度膨胀"。这篇 proposal 的核心洞察——untargeted discourse training 是否能因果性改善 multi-turn safety——是一个优美、测试价值高的假设。将 CPL 的 inertia reduction 与 DETAM/ASGuard 的 attention reallocation 框架联系起来，逻辑链清晰且有理论支撑。

然而，proposal 试图将至少 2-3 篇论文的工作量压缩到一项研究中：per-head decomposition + capacity flow mapping + quadruple-method head comparison + paradigm-controlled comparison + dose-response analysis + double dissociation + autonomy tax audit + mechanistic verification + OpenAgentSafety secondary evaluation。这种 scope inflation 是 EMNLP 审稿中**最常见的拒稿理由之一**。一篇试图做所有事情的论文，往往每件事都做不够深。

我会倾向于 **borderline accept / weak reject**，取决于最终论文是否能有效聚焦。

【核心贡献】:
1. **假设检验贡献**（最高价值）: 首次测试 discourse-level 训练干预（CPL）是否因果性改善 multi-turn safety，连接了 discourse quality 和 safety 两个独立研究社区。如果正面结果成立，这揭示了 safety 的一种全新改善路径（不需要 safety-labeled 数据）。
2. **方法论贡献**（中高价值）: Per-head diagonal attention decomposition 和 attention capacity flow mapping 是真实的 first，前者填补了 Wan et al. 仅报告 aggregate-level 的空白，后者回答了所有 attention-reallocation safety 工作都隐含假设但未验证的问题。
3. **分析贡献**（中等价值）: Quadruple-method safety head identification comparison 有独立价值，但更像是 engineering contribution 而非 conceptual breakthrough。
4. 对领域的价值：如果正面结果成立，impact 较高——表明 safety 不需要仅靠 safety 数据来改善，discourse quality 训练是一条互补路径。如果负面结果，价值中等——首次排除了一个重要假设 + 方法论贡献。

【方法合理性】:
方法整体合理，但存在几个关键脆弱点：

**合理之处：**
- CPL 作为干预手段选择得当：它是 parameter-efficient (0.4% params)、well-characterized 的方法，其 attention 效应已被原文档记录。
- Paradigm-controlled comparison (XGuard-DPO) 设计精巧，通过将 XGuard safety 数据转换为 CPL 相同的 DPO 格式，有效控制了训练范式这一混杂因素。
- Manipulation check 先验证 CPL 是否真的减少了 inertia，再解释 safety 效果——这是好的因果推断实践。

**脆弱之处：**
1. **Softmax zero-sum ≠ causal competition**: Proposal 反复强调 softmax 的 zero-sum 约束保证 capacity release，但 zero-sum 只意味着总概率恒定，并不意味着从 diagonal 释放的 attention 会流向 safety tokens。Capacity flow mapping 正是为了解决这个问题，但如果结果显示 released capacity 分散到 formatting/task tokens 而非 safety tokens，整个 competition hypothesis 就不成立了。这是一个合法的实验设计，但审稿人会质疑 "hypothesis 失败" 的情况下论文的贡献是否足够。
2. **CPL reproduction risk**: 代码未公开，dual-rollout preference pair construction 在 AgentGym 上的复现存在不确定性。Proposal 设了 fallback paths，但如果 CPL 复现不精确，所有下游分析的效力都会受损。
3. **XGuard-DPO paradigm matching 的局限性**: Proposal 坦承 preference margin distributions 会不同，但这恰好是一个核心混杂因素——DPO 的效果对 preference margin 极度敏感（Park et al., arXiv:2403.19159 已证明）。"Double dissociation" claim 因此显著减弱。
4. **更简单的替代方案**: 一个 reviewer 可能会问——是否可以直接测试 DETAM 在 multi-turn setting 中的效果（比如 turn-level DETAM），而不需要引入 CPL？如果 turn-level DETAM 有效，那 CPL 的 value proposition 就更窄了。Proposal 提到了 DETAM 在 multi-turn 中 intent token 定位的困难，但并未实验性地验证这个困难。

【5 维度打分】:

1. 研究问题: 【强】— "Untargeted discourse training 能否因果性改善 multi-turn safety" 是一个高度原创、有理论和实践价值的问题。文献调研确认这一假设未被测试（所有现有 multi-turn safety defense 都使用 safety-labeled 数据），与 Alignment Pretraining (Tice et al., arXiv:2601.10160) 的发现形成互补但独立的证据线。Multi-turn safety erosion 本身是 well-documented 的现实问题（MT-AgentRisk: 16% ASR increase），且现有解法的 attention-mechanism 基础已被 DETAM、ASGuard、Zhou et al. 等充分建立，使得这一 causal question 有坚实的研究基础。

2. 方法与创新: 【中】— 核心方法创新在于 per-head diagonal attention decomposition 和 capacity flow mapping，这两者在文献中确实不存在（Wan et al. 仅报告 aggregate; DETAM/ASGuard/AISA 均不追踪 capacity 流向）。然而，**核心实验本质上是 "take existing method (CPL) and evaluate on new task (safety)"**，这是 application-level novelty 而非 fundamental methodological innovation。Three-level competition hierarchy 虽然有组织价值，但更像是对已知现象（head-level safety: Zhou et al.; layer-level: Deng et al.; representation-level: X-Boundary）的框架化重述，而非真正的理论贡献。Paradigm-controlled comparison (XGuard-DPO) 设计精巧但受 preference margin confound 限制（Park et al., arXiv:2403.19159）。

3. 实验设计: 【强】— 这是 proposal 最大的亮点。8 个实验条件（CPL + 2 controls + 3 XGuard variants + X-Boundary + ToolShield + combination）涵盖了几乎所有合理的 baseline。Manipulation check 先验证机制再解释效果，是一流的因果推断设计。Dose-response 测试 tipping point 预测，sample size justification (365 tasks × 8 conditions 提供 >5800 observations)，GPT-4o judge with position-swap protocol + rule-based secondary evaluator + Cohen's kappa 报告——这些都显著超过了该领域的平均实验标准。与同类工作相比：MUSE-D 仅用单一 DPO baseline；X-Boundary 未做 paradigm-controlled comparison；MTSA 未做 attention-level mechanistic analysis。Null-result framing strategy 也值得称赞。**但 scope 过大是双刃剑——设计完美但执行不完整的实验 vs. 范围适中但执行彻底的实验，审稿人几乎总是偏好后者。**

4. 可行性: 【中】— 资源需求合理（~1000-1200 A100-hours，~$1500-1800，8B 模型），16-18 周时间线虽紧凑但不不切实际。主要风险：(a) CPL 代码未公开，复现需要 contact authors + reproduce dual-rollout pipeline，这可能消耗大量时间；(b) AgentGym 环境稳定性；(c) Quadruple-method pipeline 的工程复杂度；(d) 8 个条件 × 2 模型 × 多个评测集的实验矩阵管理。Go/no-go milestones 设计合理，但 fallback 到 "correlational-only study" 或 "DETAM in multi-turn settings" 实质上是完全不同的论文。最大的可行性风险是 **scope 导致的执行质量下降**——即使每个组件都可行，同时高质量完成所有组件在 16 周内是极具挑战的。

5. 写作与呈现: 【中偏弱】— Proposal 展示了对领域的深入理解和极强的综合能力，literature review 堪称典范。但当前写作存在严重的 **信息过载** 问题：大量首字母缩写（CPL、DETAM、ASGuard、AISA、CAST、GAR、SRI、AHD）、过度的交叉引用、嵌套式论证使得核心 message 被淹没。一个清晰的 3 句话 elevator pitch 应该是："Multi-turn safety erosion 可能由 attention inertia 驱动 → CPL 减少 inertia → 如果 CPL 也改善 safety，则证明了一条不需要 safety 数据的新路径。" 但这个简洁信息需要在大量技术细节中费力提取。审稿人在 3-5 分钟快速浏览时可能无法抓住核心贡献。此外，Target Venues 写的是 ICLR 2027 / AAAI 2027 而非 EMNLP 2026，这是细节但反映了 framing 的不聚焦。

【概率估计】: [22% - 36%] 中位 28%

【估计理由】: 
研究问题的 novelty 是真实的——这是一个未被测试的重要假设，且实验设计远超该领域平均水平，这两点将 proposal 提升到 "有竞争力" 的范围。然而，三个因素显著压低了概率：

(1) **Scope inflation 是最大的单一风险**。当前 proposal 包含至少 3 篇论文的内容（Paper A: per-head diagonal decomposition + capacity flow mapping; Paper B: CPL→safety causal test with paradigm controls; Paper C: quadruple-method head comparison + mechanistic analysis）。EMNLP 审稿人对 "试图做太多" 的论文非常敏感——不是因为内容不好，而是因为每个部分都无法做到足够深入。如果最终论文不能有效聚焦到 1-2 个核心贡献，rejection 概率显著上升。

(2) **核心贡献的 perceived novelty 可能被低估**。"Take CPL and test on safety" 在技术上是 application-level transfer，审稿人可能将其视为 "applying existing method to new domain" 而非 fundamental contribution，即使 causal framing 提升了其价值。

(3) **结果不确定性高**。如果 CPL 的 safety improvement 效果不显著（与直接 safety training 方法如 MTSA、X-Boundary 相比），论文需要依赖 null-result + methodological contributions 来立足，这在顶会中更难被接受。如果 capacity flow 分散而非定向到 safety tokens，三级竞争假设被削弱。

正面因素：research question 的 novelty 真实存在，experimental rigor 远超平均水平（manipulation check + paradigm control + dose-response 在该领域非常少见），multi-turn safety 是 EMNLP 社区高度关注的方向，standalone methodological contributions (per-head decomposition, capacity flow) 提供了 fallback value。

综合判断：如果论文有效聚焦（砍掉 Phase 2.5 hyperparameter sensitivity、简化 Phase 4 mechanistic verification、将 quadruple-method comparison 移入 appendix）且 CPL 产生有意义的 safety improvement，概率可提升到 35-40%。按当前 scope 执行，概率在 22-28% 范围。

【主要风险】:
1. **Scope inflation → 每个贡献都不够深**：当前 proposal 是 5 phases + 8 conditions + quadruple triangulation + dose-response + mechanistic verification + secondary evaluation + autonomy tax audit。即使全部执行完毕，在 8 页正文中无法做到每个部分都有足够深度。审稿人最可能的 criticism 是 "the paper tries to do too much and each contribution feels shallow"。
2. **CPL safety improvement 效果可能不显著或不如直接 safety training methods**：如果 CPL 的 ASR reduction 显著弱于 XGuard-DPO / X-Boundary / MTSA（后者直接使用 safety 数据），审稿人会质疑 "为什么不直接用 safety 数据训练？" 虽然 causal mechanism insight 有独立价值，但 "method 不 work well" + "但我们理解了为什么" 在顶会中是高风险策略。

【实施评估】:
  - 计算资源: ~980-1200 A100-hours (~$1500-1800)，对学术实验室合理；8B 模型规模不需要极端资源，但 8 条件 × 2 模型的实验矩阵管理需要良好的工程基础设施
  - 数据需求: MT-AgentRisk (365 tasks, 公开)、OpenAgentSafety (公开)、MultiBreak (公开)、XGuard-Train (HuggingFace 公开)、CPL preference pairs (需复现 dual-rollout pipeline on AgentGym)、OR-Bench (公开)
  - 人工介入: 中等——CPL 复现需要与原作者沟通获取 checkpoints、AgentGym 环境调试、extended-turn variant 构造（100 tasks × 5 turn counts）需要人工验证质量
  - 训练需求: 需要训练——CPL DPO (2 models)、XGuard-SFT rank-8 和 rank-16 (2 models each)、XGuard-DPO (2 models)、Random-Preference LoRA (2 models)、Reversed-CPL (2 models)、hyperparameter sweeps；总计约 14-16 次训练运行 + sweeps
  - 新 Benchmark: 不需要构建全新 benchmark，但需要构造 extended-turn variants（在 MT-AgentRisk 基础上 prepend benign turns）和将 XGuard 数据转换为 DPO 格式
  - 预估周期: 16-18 周（含 1 周 buffer），但如果 CPL 复现遇到困难可能延伸到 20+ 周；关键路径：CPL 复现 → Phase 0.5 head overlap → Phase 2 interventional
```

Sources:
- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., 2026)](https://arxiv.org/abs/2602.03664)
- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025)](https://arxiv.org/abs/2504.13562)
- [ASGuard: Activation-Scaling Guard (Park et al., ICLR 2026)](https://arxiv.org/abs/2509.25843)
- [On the Role of Attention Heads in LLM Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)
- [When Attention Closes (Dongre et al., 2026)](https://arxiv.org/abs/2605.12922)
- [CAST: Safety-Utility Conflicts Are Not Global (2026)](https://arxiv.org/abs/2601.04262)
- [Unsafer in Many Turns / MT-AgentRisk / ToolShield (2026)](https://arxiv.org/abs/2602.13379)
- [X-Boundary (Lu et al., EMNLP 2025)](https://arxiv.org/abs/2502.09990)
- [Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., 2025)](https://arxiv.org/abs/2508.19697)
- [The Struggle Between Continuation and Refusal (Deng et al., 2026)](https://arxiv.org/abs/2603.08234)
- [Alignment Pretraining (Tice et al., 2026)](https://arxiv.org/abs/2601.10160)


【原始 proposal（允许参考但不是主要依据）】:
# Conversational Inertia as a Causal Pathway to Multi-Turn Safety Erosion: Testing the Attention Capacity Competition Hypothesis

## Description
This project conducts the first controlled interventional study testing whether conversational inertia — diagonal attention to previous outputs (Wan et al., ICML 2026) — constitutes an independent causal mechanism of progressive multi-turn safety erosion, distinct from and orthogonal to mechanisms addressed by DETAM (single-turn attention reallocation, ASR 46%→1.2%; Li et al., ACL 2025 Findings) and ASGuard (circuit-specific vulnerability targeting; Park et al., ICLR 2026). We propose that reducing inertia through untargeted discourse training (CPL) achieves broad attention reallocation addressing progressive multi-turn erosion that targeted approaches structurally cannot: DETAM's intent-token localization is ill-defined in multi-turn crescendo attacks where intent is distributed across turns; ASGuard's efficacy hinges on localizable circuits absent in cumulative discourse erosion. The study makes two novel methodological contributions beyond safety evaluation: (1) the first per-head decomposition of diagonal attention (Wan et al. explicitly averages all heads), and (2) the first attention capacity flow mapping — tracking where attention capacity released by inertia reduction actually flows (toward safety tokens, task tokens, or dispersed), a question no prior attention-reallocation safety work (DETAM, ASGuard, AISA) has addressed. Phase 0.5 measures overlap with safety-critical heads using quadruple triangulation (Ships score, DETAM sensitivity, AISA spatiotemporal analysis, CAST conflict map from arXiv:2601.04262), cross-validated against four published head sets (Zhou et al., Depth Charge, ASGuard, CAST). We integrate the Goal Accessibility Ratio (GAR; Dongre et al., arXiv:2605.12922) as a complementary metric — if diagonal attention rises while GAR falls, two independent measures converge on the same competition mechanism. The five-phase causal design includes: a manipulation check verifying CPL reduces inertia on safety benchmarks before interpreting safety effects; paradigm-controlled comparison (XGuard-DPO: safety data in CPL's exact DPO format) enabling detection of a potential double dissociation between attention-reallocation and direct-safety training pathways; turn-count dose-response testing Johnson & Huo's (arXiv:2602.14370) tipping point predictions; ToolShield direct comparison and CPL+ToolShield combination testing orthogonality of training-time and inference-time defenses; and X-Boundary (EMNLP 2025) as a direct representation-level baseline. If CPL reproduces DETAM-like attention redistribution and ASGuard-targeted head modification despite having no safety training signal, this reveals shared attentional infrastructure between discourse quality and safety — consistent with independent evidence from Alignment Pretraining (arXiv:2601.10160) that discourse-level data properties causally influence alignment through a different pathway (pretraining content vs. post-training attention mechanics). The per-head decomposition, capacity flow mapping, quadruple-method head comparison, and mechanistic analysis constitute standalone contributions regardless of safety results.

## Core Problem
Multi-turn agent interactions exhibit systematic safety degradation (16% higher attack success rates), and while recent work has identified attention-level mechanisms — attention dispersion on safety keywords (ASJA, AAAI 2025), competition between safety and continuation heads (Deng et al., arXiv:2603.08234), and attention reallocation as a defense (DETAM, ACL 2025 Findings) — and developed multi-turn safety defenses (MUSE-D turn-level DPO, EMNLP 2025; XGuard-Train SFT, COLM 2025; X-Boundary representation boundaries, EMNLP 2025; MTSA RL-based alignment, ACL 2025), and training-time attention head interventions for specific vulnerability types (ASGuard circuit-targeted scaling, ICLR 2026), these studies are either attack-oriented, single-turn, operate at inference time, target specific localizable vulnerabilities, or train directly on safety-labeled data without testing whether discourse-level mechanisms causally drive safety erosion. Critically, DETAM demonstrates that simply reallocating attention from attack tokens toward safety-relevant tokens at inference time reduces ASR from 46% to 1.2% on LLaMA-2, providing the strongest existing evidence that attention redistribution causally improves safety. Yet DETAM requires explicit identification of 'intent tokens' at runtime and operates only in single-turn settings — in multi-turn crescendo attacks where malicious intent is progressively distributed across turns, the notion of localizable 'intent tokens' breaks down fundamentally. ASGuard demonstrates that training-time modification of safety-relevant heads is feasible via circuit-targeted scaling vectors, but its efficacy 'hinges on localizable causal circuits' for specific attack types — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits. Concurrently, "When Attention Closes" (Dongre et al., arXiv:2605.12922) demonstrates that multi-turn attention degradation produces architecture-dependent failure modes — some models preserve goal-conditioned behavior through residual streams even at vanishing direct attention, others fail despite decodable residual goal information — suggesting that the pathway from attention loss to behavioral failure is not uniform and requires measurement at multiple levels. Furthermore, the competition hypothesis contains a critical hidden assumption: that attention capacity released by reducing diagonal inertia is captured by safety-relevant tokens rather than by other competing patterns. Softmax's zero-sum constraint guarantees capacity release but not its direction — no work has explicitly tracked where released capacity flows, despite this being fundamental to all attention-reallocation safety claims (DETAM, ASGuard, AISA). The only characterization of diagonal attention (Wan et al., ICML 2026) reports aggregate-level patterns averaged across all heads; no per-head decomposition exists, leaving the head-level competition question empirically open.

## Opportunity
Seven independent research threads have converged to make a controlled causal study newly feasible: (1) Conversational Inertia (Wan et al., ICML 2026, arXiv:2602.03664) identifies diagonal attention where the i-th token attends to the i-th previous output position and provides Context Preference Learning (CPL) as a parameter-efficient intervention (0.4% params, LoRA rank-16 DPO with beta=0.01), validated on Qwen3-8B and Llama 3.1-8B-Instruct across eight agentic environments but never evaluated for safety — crucially, the diagonal attention pattern is characterized only at the aggregate level (averaged across all heads), so the per-head distribution remains unknown; (2) DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) provides direct causal evidence that attention reallocation toward safety-relevant tokens improves safety — reducing ASR by 97%+ without weight modification — but requires runtime intent token identification and is single-turn only; (3) ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) demonstrates that training-time modification of safety-relevant attention heads is feasible via circuit-targeted channel-wise scaling vectors — crucially identifying 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30), exactly where Deng et al. find continuation heads — but targets specific localizable vulnerability circuits rather than discourse-level dynamics; (4) Multi-turn safety erosion is now well-benchmarked via MT-AgentRisk (365 tasks, 5 tools, avg 3.19 turns) with ToolShield as a defense baseline, supplemented by OpenAgentSafety (ICLR 2026, arXiv:2507.06134; 356 real-tool tasks) and MultiBreak (arXiv:2605.01687; 10,389 multi-turn adversarial prompts); (5) Multi-turn safety training has mature baselines: XGuard-Train SFT (COLM 2025, arXiv:2504.13203; up to 48.3% vulnerability reduction), MUSE-D turn-level DPO (EMNLP 2025, arXiv:2509.14651), X-Boundary representation-level boundaries (EMNLP 2025, arXiv:2502.09990; ASR reduction to 16-25%), and MTSA RL with future rewards (ACL 2025, arXiv:2505.17147; ASR 74.5% to 23.5%) — but all train directly on safety-labeled data; (6) AISA (Song et al., arXiv:2602.13547) provides spatiotemporal safety head localization via large-scale linear probing — K=16 heads achieving 0.92 detection accuracy — enabling methodological triangulation; (7) "When Attention Closes" (Dongre et al., arXiv:2605.12922) introduces the Goal Accessibility Ratio (GAR) measuring attention from generated tokens to goal-defining tokens across turns, demonstrating architecture-dependent failure modes that inform the multi-level competition hypothesis. Additionally, CAST (arXiv:2601.04262) provides a fourth complementary head identification method via head-level conflict maps, and Alignment Pretraining (Tice et al., arXiv:2601.10160) provides independent evidence that discourse-level data properties causally influence alignment — reducing misalignment from 45% to 9% via pretraining content curation — supporting the broader principle that untargeted discourse properties can affect safety through indirect pathways. This seven-thread convergence, combined with Johnson & Huo's (arXiv:2602.14370) formalization of attention competition tipping points, motivates a three-level attention capacity competition hypothesis testable through a novel Phase 0.5 head overlap analysis.

## Landscape
**Attention reallocation defenses:** DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) identifies attention heads sensitive to jailbreaks by computing attention score differences (threshold alpha: 0.1 for LLaMA-2, 0.03 for Vicuna), modifies the causal mask by multiplying at intent token positions by beta=5.0, reducing average ASR from 46.0% to 1.2% on LLaMA-2-7b-chat and from 81.8% to 4.0% on Vicuna-13b-v1.5. Cross-model transferability: sensitive heads from LLaMA-2 transferred to Meta-LLaMA-3 achieve 4% ASR vs. 96% vanilla. Three fundamental limitations for multi-turn agent settings: (a) requires runtime identification of 'intent tokens' — in crescendo attacks (Russinovich et al., USENIX Security 2025, arXiv:2404.01833) where intent is distributed across turns, token-level localization is ill-defined; (b) single-turn only, cannot address cumulative attention shift that Johnson & Huo's tipping point theory predicts; (c) per-turn computational overhead. Our study tests whether CPL achieves DETAM-like redistribution persistently through training. **Training-time attention head intervention:** ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) uses EAP-IG to identify causally linked heads, trains channel-wise activation scaling vectors (s_j ∈ R^{d_head}, H'_{l,j} = H_{l,j} ⊙ s_j) on identified heads with preventative fine-tuning. Reduces ASR from 42% to 8% on Llama-3.1-8B and 51% to 8% on Qwen2.5-7B, achieving Pareto-optimal safety-utility balance. Identifies 11 vulnerable heads including 4 at Layer 13 (L13H8, L13H18, L13H25, L13H30) — exactly where Deng et al. find continuation heads. Key differences: (a) targets localizable circuits; (b) fixes known attack types one at a time; (c) single-turn only. **Head-level conflict diagnosis:** CAST (arXiv:2601.04262) proposes Conflict-Aware Sparse Tuning, constructing head-level conflict maps by synthesizing optimization conflict and functional sensitivity. Key finding: utility degradation concentrates in a small subset of "high-conflict" heads. CAST's conflict map provides a fourth independent method for identifying safety-relevant heads, complementary to Ships score, DETAM sensitivity, and AISA probing. **Multi-turn attention degradation:** "When Attention Closes" (Dongre et al., arXiv:2605.12922) introduces GAR measuring attention from generated tokens to goal-defining tokens. Key finding: architecture-dependent failure modes — some models preserve goal-conditioned behavior at vanishing attention through residual streams, others fail despite decodable residual goal information, encoding layers varying from 2 to 27. GAR measures the same degradation phenomenon as diagonal inertia from a complementary angle, and the architecture-dependent failure modes inform the Level 2/3 distinction. **Safety head localization methods:** AISA (Song et al., arXiv:2602.13547) localizes safety-critical heads via spatiotemporal analysis — large-scale linear probing across 15 positions per layer, top-K=16 heads achieving 0.92 detection accuracy. Safety heads cluster in middle layers in standard models but shift toward higher layers in strongly safety-aligned models. **Safety head distribution:** Huang et al. (arXiv:2508.19697) propose Attention Head-level Dropout (AHD) to distribute safety capabilities across more heads, arguing that concentration in few heads is itself a vulnerability. This creates a productive tension with the competition hypothesis: if AHD distributes safety across more heads, does capacity competition become weaker or stronger? We argue stronger — softmax zero-sum operates within each head independently, so distributed safety heads increase the surface area over which capacity competition operates. If CPL's effect weakens on AHD-treated models, this would confirm head-level competition as the mechanism. **Attack-side mechanisms:** Du et al. (ASJA, AAAI 2025) show successful multi-turn jailbreaks correlate with attention dispersion away from safety keywords (p=4.38e-07). Deng et al. (arXiv:2603.08234) identify competing safety (layers 25-27) and continuation (~Layer 13) heads. Depth Charge (Wu et al., arXiv:2603.05772) introduces SAHA, 82-91% ASR, layer-specific concentrations (layer 7 for Llama 3.1-8B, head 31 universally important). Attention Eclipse (Zaree et al., arXiv:2502.15334) achieves 91.2% ASR by manipulating attention focus. **Attention competition theory:** Johnson & Huo (arXiv:2602.14370) formalize dot-product competition creating tipping points (n*) — cumulative inertia pushes past a threshold single-turn defenses cannot prevent. **Discourse-alignment causal pathway:** Alignment Pretraining (Tice et al., arXiv:2601.10160) demonstrates that discourse-level properties of pretraining data causally influence alignment (misalignment 45%→9%), establishing a precedent that untargeted discourse properties can affect safety — though through data content rather than attention mechanics. Our work tests the complementary pathway: post-training attention structure modification. **Multi-turn safety benchmarking:** Yang et al. (arXiv 2026) document 16% average ASR increase on MT-AgentRisk and propose ToolShield (~30% ASR reduction). OpenAgentSafety (ICLR 2026, arXiv:2507.06134) provides 356 multi-turn, multi-user tasks with real tools including benign-intent tasks useful for over-refusal evaluation. Li et al. (STAR, arXiv:2603.15684) show monotonic drift from refusal representations. MultiBreak (arXiv:2605.01687) provides 10,389 multi-turn adversarial prompts across diverse attack types. **Multi-turn safety defenses:** X-Teaming (COLM 2025, arXiv:2504.13203) introduces XGuard-Train (30K multi-turn safety dataset). SFT with LoRA rank-8, lr=1e-4, 3 epochs achieves up to 48.3% vulnerability reduction. MUSE-D (EMNLP 2025, arXiv:2509.14651) applies turn-level DPO achieving 24% ASR reduction. X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990) reduces ASR from 58.5-76.0% to 16.0-25.0% while reducing over-refusal by ~20%. MTSA (Guo et al., ACL 2025, arXiv:2505.17147) reduces ASR from 74.5% to 23.5%, peak attack at round 5. Agent Safety Alignment (Sha et al., arXiv:2507.08270) proposes unified sandboxed RL. STREAM (arXiv:2506.00668) reduces ASR by 51.2% via safety reasoning. TurnGate (arXiv:2605.05630) introduces turn-level harm detection. STREAM and TurnGate operate at inference time and are complementary to training-time interventions. **Discourse dynamics:** Wan et al. (ICML 2026, arXiv:2602.03664; also OpenReview #UubLs3lUfk, published in PMLR 306, Seoul, July 6-11) identify conversational inertia and propose CPL. Diagonal attention characterized only at aggregate level. Code not released. **Safety attention head mechanisms:** Zhou et al. (ICLR 2025, arXiv:2410.13708) show the most critical head in Llama-2-7B-Chat is Head (2, 26). Wei et al. (arXiv:2408.17003) identify safety layers at layers 9-14. The refusal direction (Arditi et al., arXiv:2406.11717) is strongest around layer 15. **Safety persistence:** Plaut (arXiv:2603.02229) shows LoRA safety DPO persists with 90-94% retention, Pareto frontier R-squared=0.77. **DPO length bias:** Park et al. (arXiv:2403.19159) and Meng et al. (arXiv:2409.06411) document hidden length dependence. **Gap:** Despite convergent progress on attention reallocation (DETAM), targeted head intervention (ASGuard), safety defenses (XGuard-Train, MUSE-D, X-Boundary, MTSA), head localization (Zhou et al., AISA, Depth Charge, CAST), attention degradation (GAR), competition theory (Johnson & Huo), discourse-alignment pathways (Alignment Pretraining), and discourse dynamics (conversational inertia), no work has: (a) tested whether training-time discourse intervention achieves broad DETAM-like attention reallocation and causally reduces multi-turn safety erosion; (b) provided per-head decomposition of diagonal attention; (c) tracked where attention capacity released by reallocation actually flows; (d) compared discourse-targeted vs. safety-targeted training under paradigm-matched conditions (DPO vs. DPO); or (e) controlled for DPO response-length confounds in discourse-safety evaluations.

## Approach
We run a five-phase causal study on MT-AgentRisk (primary) and OpenAgentSafety (secondary) benchmarks using Qwen3-8B and Llama 3.1-8B-Instruct, organized around the 'attention capacity competition hypothesis.'

**Why Training-Time Discourse Intervention?** DETAM achieves 97%+ ASR reduction in single-turn settings — but requires identifying 'intent tokens' at runtime. In multi-turn crescendo attacks where intent is distributed across 3-10 turns (MTSA finds peak attack at round 5), no single token set constitutes 'the intent.' ASGuard's Limitations notes 'efficacy hinges on localizable causal circuits.' Multi-turn inertia erosion is progressive, not localizable. CPL reduces cumulative inertia that dilutes safety attention — addressing the root cause (per-turn accumulation) that Johnson & Huo's tipping point theory predicts pushes past n*.

**The Attention Capacity Competition Hypothesis (Three-Level Framework):** Diagonal attention competes with safety-keyword attention at three levels, and different architectures may exhibit different mixtures of these levels (informed by Dongre et al.'s architecture-dependent failure modes, arXiv:2605.12922): **Level 1 (Head-level, strong form):** Diagonal and safety attention share heads; softmax zero-sum directly displaces safety attention. Even if safety capabilities are distributed across many heads (per Huang et al., arXiv:2508.19697), softmax competition operates independently within each head, so distribution increases the surface area for competition rather than eliminating it. **Level 2 (Layer-level, medium form):** Different heads within shared layers; competition through residual stream — supported by Deng et al.'s Layer 13 continuation vs. Layer 25-27 safety antagonism, corroborated by ASGuard's 4 Layer-13 vulnerable heads, and by "When Attention Closes" finding that some architectures preserve goal information via residual streams. **Level 3 (Representation-level, weak form):** Competition through accumulated representation drift, validated by X-Boundary's success (ASR 58.5% to 16.5%). Phase 0.5 determines the relative contribution of each level per architecture — not which single level applies, but the mixture. If Qwen3-8B shows Level 1 while Llama 3.1-8B shows Level 2, this architecture-dependent competition pattern is itself a finding.

**Phase 0 — CPL Acquisition/Reproduction + Baseline Preparation (weeks 1-3):** Contact Wan et al. for CPL checkpoints immediately (ICML 2026 camera-ready due May 2026; authors likely have checkpoints). Simultaneously reproduce CPL using TRL DPOTrainer + PEFT: LoRA rank-16, alpha-16, 0.4% params, DPO with beta=0.01, sigmoid loss, 2 epochs, lr=5e-7, AdamW, 1000 preference pairs per environment. Main reproduction risk: dual-rollout preference pair construction pipeline on AgentGym. Estimated: ~40 A100-hours per model. In parallel, prepare baselines: (a) XGuard-Train SFT rank-8 (published config: lr=1e-4, 3 epochs); (b) XGuard-Train SFT rank-16 (CPL-matched params); (c) **XGuard-DPO rank-16** — convert XGuard-Train safety data to DPO preference format (rejected responses generated via base model greedy decoding on harmful prompts, following standard DPO safety practice), train with CPL-identical DPO config (rank-16, beta=0.01, 2 epochs, lr=5e-7); report preference margin distributions for both CPL and XGuard-DPO pairs, with distributional differences acknowledged as inherent limitation of paradigm matching; (d) **X-Boundary** — reproduce using open-source code (GitHub: AI45Lab/X-Boundary); (e) **ToolShield** — deploy as direct inference-time baseline using open-source code (GitHub: CHATS-lab/ToolShield). Construct extended-turn variants: prepend {0, 2, 4, 6, 8} benign tool-use turns to 100 representative MT-AgentRisk tasks (stratified by risk category) for turn-count dose-response analysis.

**Granular Go/No-Go Milestones:** Week 1.5: AgentGym >=3/8 environments operational. Week 2.5: dual-rollout pipeline producing valid preference pairs with measurable attention differential. Week 3: DPO training converged + base model matches Wan et al. within 1.5 SEM on >=2 environments (relaxed from 1 SEM as Plan B; approximate CPL sufficient for causal inference). 1 week buffer reserved for debugging. **Fallback paths:** (a) environment failure: proceed with 2-3 most reliable; (b) inertia differential failure: pivot to correlational-only study (Phases 1 and 4); (c) training failure: debug + 1 week → if still failing by week 4, pivot to 'DETAM in multi-turn settings.'

**Phase 0.5 — Head Overlap Test and Per-Head Diagonal Attention Decomposition (weeks 3-5, ~30 A100-hours):** First per-head decomposition of diagonal attention and prerequisite test for the competition hypothesis. Using both base models on 50 MT-AgentRisk tasks. **Core tier (must complete, weeks 3-4.5):** (a) Per-head diagonal attention decomposition using Wan et al.'s metric (attention between current output position i and previous assistant output position i ±5 tokens) — the first such decomposition. (b) Ships score (Zhou et al., ICLR 2025) via KL divergence after head ablation. (c) DETAM sensitivity metric. (d) Overlap analysis: Jaccard index between top-k diagonal and top-k safety heads (k=5,10,20,50) with permutation tests on ~1024 heads per model; bootstrap CIs on per-head diagonal attention scores to confirm estimation stability from 50 tasks. Cross-validate against published localizations: Zhou et al.'s Head (2,26); Depth Charge's layer-specific data (layer 7 for Llama 3.1-8B); ASGuard's EAP-IG heads (11 heads including 4 at Layer 13). **Enhancement tier (best-effort, weeks 4.5-5, parallel with early Phase 1):** (e) AISA spatiotemporal probing (K=16); (f) CAST conflict map. If enhancement methods incomplete by week 5, proceed with triple-method results; enhancement results integrated retroactively. **Level determination:** Level 1 (>30% head overlap) → per-head softmax; Level 2 (same layers, <30% overlap) → residual stream, Layer 13 nexus; Level 3 (<10%) → representation-level. Report per-architecture level mixture rather than single determination.

**Phase 1 — Correlational with Attention Capacity Analysis (weeks 5-8):** Measure diagonal attention (per-head), GAR (Dongre et al., arXiv:2605.12922), AND safety-keyword attention at each turn on 365 MT-AgentRisk tasks and extended-turn variants. **Attention capacity flow mapping:** When diagonal attention varies across turns or conditions, track where capacity flows using attention mass metric — for each token category (safety-relevant tokens identified via DETAM's intent token method + ASJA's safety keyword extraction, task tokens including tool names and parameters, formatting tokens, previous-context tokens), compute proportion of total attention allocated by high-diagonal heads (from Phase 0.5). This maps whether inertia reduction benefits safety tokens specifically or disperses broadly — fundamental to all attention-reallocation safety claims yet never measured. Fit mixed-effects models with turn position as fixed effect (linear and quadratic terms), task as random intercept, controlling for response token count. Test whether per-turn diagonal attention increase predicts safety attention decrease at same or next turn. (Note: Granger causality inappropriate for avg 3.19 turns — turn-position regression is statistically appropriate for these short sequences.)

**Phase 2 — Interventional with Confound Controls (weeks 8-12):** **Manipulation check (prerequisite):** Verify CPL reduces diagonal attention on MT-AgentRisk tasks (per-head and aggregate) before interpreting safety effects. If CPL fails to reduce inertia, safety results cannot adjudicate competition hypothesis. **Eight conditions:** (a) CPL (rank-16 DPO, discourse data); (b) Random-Preference LoRA; (c) Reversed-CPL; (d) XGuard-Train SFT (rank-8, published config); (e) XGuard-Train SFT (rank-16, parameter-matched); (f) XGuard-DPO (rank-16, paradigm-matched); (g) X-Boundary (representation-level); (h) **ToolShield** (inference-time, direct comparison). Plus **CPL + ToolShield combination** to test orthogonality of training-time and inference-time defenses — additional benefit from combination would demonstrate complementary mechanisms. Plus Response-Length Analysis across all conditions. **Evaluation protocol:** Primary: GPT-4o judge with 5-point safety scale and position-swap protocol (each sample judged twice with swapped condition order; report position consistency rate). Secondary: rule-based evaluator following ToolShield's keyword matching + refusal pattern detection pipeline. Report inter-method agreement (Cohen's kappa). **Attack type coverage:** MT-AgentRisk crescendo-style (primary) + MultiBreak subset covering diverse types (attention-shifting, many-turn). **Turn-count dose-response:** 100 extended-turn tasks × {0,2,4,6,8} prepended turns — if tipping point hypothesis holds, CPL benefit is largest at high turn counts. **Per-turn safety analysis:** ASR at each turn position across conditions; CPL should show concentrated improvement in later turns. **Double dissociation potential:** The CPL vs. XGuard-DPO comparison is designed to detect whether two independent pathways to safety improvement exist — if CPL reduces inertia + improves safety while XGuard-DPO improves safety without reducing inertia, this constitutes a double dissociation between attention-reallocation and direct-safety-training mechanisms. Compare against published MUSE-D and MTSA results (indirect, with evaluation condition differences explicitly noted). **Sample size justification:** 365 tasks × 8 conditions × 2 models provides >5800 observations; published effect sizes (X-Boundary ASR Δ~35pp, MTSA Δ~51pp) indicate 365 tasks/condition detects effects >10pp at power >0.95.

**Phase 2.5 — Hyperparameter Sensitivity (weeks 10-11, ~90 A100-hours):** On Llama 3.1-8B-Instruct (primary): (a) Data scaling: {250, 500, 1000, 2000} preference pairs; (b) LoRA rank: {4, 8, 16, 32}; (c) DPO beta: {0.001, 0.01, 0.05, 0.1}. On Qwen3-8B (cross-model spot-check): top-2 most sensitive axes from Llama sweep × 3 values each (~20 A100-hours), verifying sensitivity patterns are qualitatively consistent across architectures.

**Phase 3 — Autonomy Tax Audit (weeks 10-12, parallel):** Step-1 completion rate, cascade failure rate, end-to-end success. **Over-refusal evaluation:** (a) OpenAgentSafety benign-intent task subset (most relevant for multi-turn agent setting); (b) OR-Bench supplementary evaluation (large-scale benign-but-sensitive queries); (c) AgentGym agentic performance change (indirect over-refusal indicator). **General capability preservation:** MMLU (knowledge) and MT-Bench (dialogue quality). Report safety-competence Pareto frontier extending Plaut's (arXiv:2603.02229) analysis. Compare frontier position with X-Boundary's ~20% over-refusal reduction, ASGuard's Pareto-optimal balance, and XGuard-SFT's published results.

**Phase 4 — Mechanistic Verification (weeks 11-15):** (a) SRI signal framework for step-wise refusal dynamics; (b) Head-level analysis extending Deng et al.'s safety-continuation head identification to multi-turn, calibrated by Phase 0.5; (c) **DETAM-informed analysis:** If CPL shifts attention in same heads/direction as DETAM targets → 'implicit DETAM' through discourse training; (d) **ASGuard-informed analysis:** If CPL affects ASGuard's Layer-13 heads despite not targeting them → untargeted discourse training modifies same heads as targeted circuit surgery; (e) **Shared infrastructure hypothesis:** If (c) and (d) both positive, combined with CAST overlap from Phase 0.5 and Alignment Pretraining's independent evidence of discourse→alignment causality (arXiv:2601.10160), this constitutes convergent evidence that discourse quality and safety share attentional infrastructure — an insight with broad implications beyond this specific study; (f) Level-appropriate analysis: Level 2 → residual stream composition; Level 3 → representation trajectory per X-Boundary's framework.

**Secondary Evaluation — OpenAgentSafety (weeks 13-15):** Top-3 conditions (CPL, best XGuard variant, X-Boundary) and base model on OpenAgentSafety subset for ecological validity.

**Null-Result Framing Strategy:** (1) First per-head decomposition of diagonal attention and overlap with safety heads; (2) First attention capacity flow mapping — tracking where released attention goes (novel regardless of safety results and applicable to all attention-reallocation safety methods); (3) First quadruple-method safety head identification comparison (Ships + DETAM sensitivity + AISA + CAST), cross-validated against four published head sets; (4) Architecture-dependent competition level mixture analysis; (5) First paradigm-controlled comparison (XGuard-DPO) isolating data source from training paradigm; (6) First multi-turn extension of DETAM's Focus Loss analysis; (7) Empirical test of untargeted vs. targeted head modification; (8) Turn-count dose-response testing tipping point predictions; (9) Capacity flow direction analysis. If CPL reduces inertia but not safety → competition hypothesis weakened (standalone finding). If CPL fails to reduce inertia on safety tasks → experiment cannot adjudicate (needs stronger intervention).

**Extended-Turn Variant Validity (Limitation):** Acknowledged with mitigations: OpenAgentSafety for ecological validity, attention pattern validation, conservative amplification framing. Dose-response design ({0,2,4,6,8} turns) tests monotonicity consistent with tipping point predictions.

All primary experiments use MT-AgentRisk (365 tasks), ToolShield codebase (GitHub: CHATS-lab/ToolShield), XGuard-Train (HuggingFace: marslabucla/XGuard-Train), X-Boundary (GitHub: AI45Lab/X-Boundary), and the CPL training recipe from Wan et al. (ICML 2026).

## Resource Estimate
{'manual': {'gpu_hours': '980-1200 A100-hours (CPL reproduction 2 models ~80h, XGuard-SFT rank-8 + rank-16 training 2 models ~60h, XGuard-DPO rank-16 2 models ~40h, X-Boundary reproduction 2 models ~40h, 2 control LoRAs 2 models ~80h, Phase 0.5 head overlap core+enhancement ~35h, MT-AgentRisk evaluation 8 conditions × 2 models + ToolShield combo ~320h, extended-turn dose-response 100 tasks × 5 turn-counts × key conditions ~80h, MultiBreak subset ~40h, OpenAgentSafety top-3 conditions ~60h, SRI signal analysis ~30h, attention analysis including per-head diagonal + GAR + capacity flow mapping + DETAM/ASGuard-informed ~110h, hyperparameter sensitivity Llama full + Qwen spot-check ~90h, general capability MMLU + MT-Bench ~25h, over-refusal OR-Bench ~10h)', 'timeline': '16-18 weeks (3 weeks Phase 0 + go/no-go, 2 weeks Phase 0.5, 3 weeks Phase 1, 4 weeks Phase 2 + Phase 2.5 + Phase 3 parallel, 4 weeks Phase 4 + OpenAgentSafety, 3 weeks writing; 1 week buffer for CPL debugging)', 'estimated_gpu_cost': '$1470-1800 at $1.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': '980-1200 A100-hours', 'timeline': '14-16 weeks (Claude accelerates CPL reproduction, quadruple-method pipeline, capacity flow analysis, statistical modeling)', 'claude_api_cost': '$450-600', 'estimated_gpu_cost': '$1470-1800 at $1.50/A100-hr spot pricing'}, 'auto_research': {'gpu_hours': '1200-1500 A100-hours (additional automated sweeps, full OpenAgentSafety, extended ablation, comprehensive analysis)', 'timeline': '10-12 weeks (parallelized execution)', 'claude_api_cost': '$750-1000', 'estimated_gpu_cost': '$1800-2250 at $1.50/A100-hr spot pricing', 'speed_bottleneck': 'Sequential multi-turn generation; 16 model configurations (2 models × 8 conditions); Phase 0.5 serial dependency; quadruple-method analysis'}}

## Inspired By
Field guide Section 4 (cascading failures, production gap) + Section 5.2 (error propagation). Key insight: DETAM's inference-time attention reallocation (ASR 46%→1.2%) establishes that redirecting attention improves safety — does implicit redirection via discourse training also work? ASGuard's training-time head modification for specific vulnerabilities raises: can untargeted training achieve the same for progressive erosion? The three-level competition hierarchy reflects Wan et al.'s aggregate-only characterization and safety heads spanning L2, L9-14, L25-27, while continuation heads at Layer 13 overlap with ASGuard's vulnerable heads. Johnson & Huo's (2026) tipping points provide theoretical framework. Dongre et al.'s architecture-dependent failure modes (arXiv:2605.12922) motivate per-architecture level mixture analysis. CAST's conflict map (arXiv:2601.04262) enables testing whether safety-utility, safety-inertia, and safety-discourse conflicts converge on shared heads. Alignment Pretraining's (arXiv:2601.10160) demonstration that discourse-level data properties causally affect alignment through pretraining content provides independent evidence for discourse→safety pathways, complementing our post-training attention mechanics pathway. The observation that no prior work tracks where released attention capacity actually flows (DETAM, ASGuard, AISA all measure safety attention improvement but not capacity source) motivated capacity flow mapping as a core methodological contribution.

## Target Venues
- ICLR 2027 (abstract September 19 2026, full paper September 24 2026 [estimated] — primary target, comfortable timeline with Phase 0.5 extension)
- AAAI 2027 (abstract July 21 2026, full paper July 28 2026 — stretch target, feasible only if CPL checkpoints obtained early and Phase 0.5 shows Level 1/2 overlap)

## Key References
- DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings, arXiv:2504.13562)
- ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026, arXiv:2509.25843)
- AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks (Song et al., arXiv:2602.13547, Feb 2026)
- Multi-Turn Jailbreaking Large Language Models via Attention Shifting (ASJA, AAAI 2025)
- Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026, arXiv:2602.03664)
- Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents (Yang et al., arXiv 2026)
- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents (COLM 2025, arXiv:2504.13203)
- MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety (EMNLP 2025, arXiv:2509.14651)
- X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability (Lu et al., EMNLP 2025, arXiv:2502.09990)
- MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming (Guo et al., ACL 2025, arXiv:2505.17147)
- Agent Safety Alignment via Reinforcement Learning (Sha et al., arXiv:2507.08270)
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut, arXiv:2603.02229, March 2026)
- The Struggle Between Continuation and Refusal (Deng et al., arXiv:2603.08234, Mar 2026)
- The Autonomy Tax: Defense Training Breaks LLM Agents (Li & Zhao, arXiv:2603.19423, Mar 2026)
- On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025, arXiv:2410.13708)
- Depth Charge: Jailbreak Large Language Models from Deep Safety Attention Heads (Wu et al., arXiv:2603.05772, Mar 2026)
- Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., arXiv:2508.19697, 2025)
- Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, arXiv:2602.14370, Feb 2026)
- Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment (Zaree et al., arXiv:2502.15334, Feb 2025)
- Safety Layers in Aligned Large Language Models (Wei et al., arXiv:2408.17003, 2024)
- Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., arXiv:2406.11717, 2024)
- State-Dependent Safety Failures in Multi-Turn Language Model Interaction (STAR, arXiv:2603.15684, Mar 2026)
- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026, arXiv:2507.06134)
- One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue (TurnGate, arXiv:2605.05630, May 2026)
- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv:2605.01687, May 2026)
- STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (arXiv:2506.00668, May 2025)
- When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction (Dongre et al., arXiv:2605.12922, May 2026)
- Safety-Utility Conflicts Are Not Global: Surgical Alignment via Head-Level Diagnosis (CAST, arXiv:2601.04262, Jan 2026)
- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (Tice et al., arXiv:2601.10160, Jan 2026)
- Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions (arXiv 2026)
- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2026)
- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv 2025)
- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction (arXiv 2026)
- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv 2026)
- Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction (arXiv 2026)
- Asking Forever: Universal Activations Behind Turn Amplification (arXiv:2602.17778, Feb 2026)
- Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models (arXiv:2602.02600, Feb 2026)
- Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection (arXiv:2604.28129, Apr 2026)
- Many-Turn Jailbreaking (arXiv:2508.06755, Aug 2025)
- Disentangling Length from Quality in Direct Preference Optimization (Park et al., arXiv:2403.19159, 2024)
- Length Desensitization in Direct Preference Optimization (Meng et al., arXiv:2409.06411, 2024)
- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., USENIX Security 2025, arXiv:2404.01833)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "947835c9-77a6-459e-a47f-9335724081e6",
  "type": "user",
  "uuid": "c16430de-3483-440a-98c1-ba0c398e240d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:47:14.325Z_

```json
{
  "parentUuid": "c16430de-3483-440a-98c1-ba0c398e240d",
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
  "uuid": "8f7a48d0-3cf0-462b-83d9-fa187f80c2db",
  "timestamp": "2026-05-20T04:47:14.325Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:47:14.325Z_

```json
{
  "parentUuid": "8f7a48d0-3cf0-462b-83d9-fa187f80c2db",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5a3e80fd-b1bb-4841-b180-d30a7a817677",
  "timestamp": "2026-05-20T04:47:14.325Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to produce the evaluation. L…",
  "leafUuid": "5a3e80fd-b1bb-4841-b180-d30a7a817677",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Test discourse training pathway to multi-turn safety",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:47:42.573Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them according to my Meta Judge role.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- 研究问题: 强
- 方法与创新: 中偏强
- 实验设计: 强
- 可行性: 中
- 写作与呈现: 中偏弱
- 概率: [25% - 38%] 中位 30%


**Reviewer 2:**
- 研究问题: 强
- 方法与创新: 中偏强
- 实验设计: 强
- 可行性: 中偏弱
- 写作与呈现: 中
- 概率: [25% - 38%] 中位 30%
**Reviewer 3:**
- 研究问题: 强
- 方法与创新: 中
- 实验设计: 强
- 可行性: 中
- 写作与呈现: 中偏弱
- 概率: [22% - 36%] 中位 28%

All three reviewers agree on the strong research question and experimental design, with consistent probability estimates around 28-30%. The main variation appears in methodology assessment and feasibility concerns, with Reviewer 3 being slightly more conservative on the innovation aspect. Looking at where all three reviewers converge: scope inflation and reproducibility risks are universal concerns, the three-level framework has falsifiability issues that two reviewers explicitly flag, and everyone points to writing that needs tightening. There's broad agreement the work is application-level rather than fundamentally innovative, with moderate feasibility concerns and causal attribution challenges around preference margins that all reviewers identify. Looking at the three reviewer ranges and their midpoints clustering tightly around 29-30%, I should narrow the interval from any individual estimate given the high consistency. The instruction to take the median vicinity and compress the range suggests [25% - 35%] with a midpoint of 29% is the right balance.

Now I need to check the implementation assessment scores — they're similarly well-aligned across reviewers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a3e80fd-b1bb-4841-b180-d30a7a817677",
  "isSidechain": false,
  "requestId": "req_011CbDDPrTcvquagWg2M2uJi",
  "type": "assistant",
  "uuid": "f5df27a9-0683-4cbf-a528-9295a09249ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpA4ZvQF1NC3DSDsdF4haH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28721,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28721,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3210,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 28721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28721
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

_source line 9 · 2026-05-20T04:48:30.957Z_

【阶段】: Meta Judge
【三次中位】: [30%, 30%, 28%]  std=0.94%
【共识维度】: 
- 研究问题=强（3/3 一致）：untargeted discourse training → safety 的因果检验是真实空白，novelty claim 经调研确认成立
- 实验设计=强（3/3 一致）：8 条件 + manipulation check + paradigm-controlled comparison + dose-response + 多评测协议，显著超过领域平均水平
- Scope 过大=致命级风险（3/3 一致）：5+ phases、8 conditions、quadruple-method、three-level framework 在 8 页正文中难以充分展开，是最大的单一拒稿风险
- CPL 复现=高风险（3/3 一致）：代码未公开，dual-rollout pipeline 复现是整个研究的串行前提
- 方法与创新=中/中偏强（3/3 一致方向）：核心贡献是 application-level transfer（将 CPL 测试于 safety），非 fundamental methodological innovation；per-head decomposition 和 capacity flow mapping 有方法论价值但非 conceptual breakthrough
- 因果归因挑战（3/3 一致）：preference margin 分布差异削弱 double dissociation claim，DPO 的多重效应使因果链难以 clean 建立
- Three-level framework 不可证伪（2/3 明确提及，R3 隐含提及）：Level 1/2/3 覆盖所有可能结果，假设几乎无法被否定
- 写作/呈现=中偏弱（3/3 一致）：信息过载、核心叙事被技术细节淹没、8 页容量严重不足
- 可行性=中/中偏弱（3/3 一致方向）：资源合理但 scope 导致执行质量下降风险高，16-18 周 timeline 紧张

【异常维度】: 
- R2 单独提到"mixed training"（在 CPL DPO 中加入少量 safety pairs）作为更简单替代方案——合理但非共识
- R3 对方法与创新评分为"中"（R1/R2 为"中偏强"），更强调"obvious next step"感——属于程度差异而非方向分歧，略降权
- R2 提到 EMNLP 2026 ARR 具体截止日（5月25日）——纯物流信息，不影响学术质量判断

【最终概率】: [24% - 35%] 中位 29%
【一致性】: 高（std=0.94%，三位审稿人在所有核心维度上判断方向一致，概率估计高度收敛）
【综合理由】: 

三位审稿人独立达成高度一致的判断：研究问题有真实 novelty（untargeted discourse → safety 的因果路径确实无人验证），实验设计远超领域标准，但 scope 严重膨胀和核心方法的 application-level 性质构成双重瓶颈。

**概率上限（35%）受限于方法创新度**：三位审稿人均指出核心实验本质是"take existing method (CPL) and evaluate on new task (safety)"，per-head decomposition 和 capacity flow mapping 虽是 first，但属于 analytical tool 而非 algorithmic contribution。即使实验完美执行，方法创新天花板约束概率难以突破 35-38%。

**概率下限（24%）由执行风险决定**：scope inflation 是 3/3 审稿人标注的最大单一拒稿风险。当前 proposal 包含至少 2-3 篇论文的内容量，8 页正文无法做到每部分都有足够深度。叠加 CPL 复现的串行依赖和 three-level framework 的可证伪性质疑，下行压力显著。

**中位取 29%（较三人中位 30/30/28 略偏保守）**：高一致性下缩窄区间，但遵循"宁缺毋滥"原则微幅偏向更严格的 R3 判断。R3 对方法创新的更严格评估（"中"而非"中偏强"）具有合理性——"obvious next step" 的感知确实是审稿人的自然反应。

**关键条件性判断**：如果论文有效聚焦（砍掉 Phase 2.5、简化 Phase 4、将 quadruple-method 移入 appendix）且 CPL 产生有意义的 safety improvement，三位审稿人均认为概率可提升至 35-40%。这说明当前概率的主要压制因素是 scope 和 presentation，而非 idea 本身——优化空间存在。

【建议】: 边缘（有优化空间但需大幅精简 scope 和强化 novelty framing）

【实施评估】:
  - 计算资源: ~980-1200 A100-hours（$1470-1800 at spot pricing），对有集群访问的学术实验室合理；8 conditions × 2 models 的实验矩阵管理需要良好工程基础设施，个人研究者偏重
  - 数据需求: 公开数据集充足（MT-AgentRisk 365 tasks、OpenAgentSafety 356 tasks、MultiBreak 10,389 prompts、XGuard-Train on HuggingFace、OR-Bench），无获取障碍；关键瓶颈在 CPL preference pair 构建需要 AgentGym 环境 + dual-rollout pipeline（高技术风险）
  - 人工介入: 中等偏高——CPL 复现需联系原作者获取 checkpoints + 调试 AgentGym pipeline；extended-turn variant 构造需半手动设计和质量验证；GPT-4o judge 需 API 成本和 prompt 工程；quadruple-method head analysis 需实现 4 种独立的 head identification 方法
  - 训练需求: 需训练约 14-16 个 LoRA 模型（CPL ×2、XGuard-SFT rank-8/16 ×2 each、XGuard-DPO ×2、Random-LoRA ×2、Reversed-CPL ×2）+ hyperparameter sweep ~16 个额外配置；不需要从头预训练，模型规模为 8B
  - 新 Benchmark: 不需要构建全新 benchmark；需构造 extended-turn variants（100 tasks × 5 turn-counts）和将 XGuard 数据转换为 DPO 格式，属于数据增强
  - 预估周期: 名义 16-18 周，实际更可能 20-24 周（考虑 CPL 复现风险和 Phase 0 串行依赖）；关键路径为 CPL 复现 → Phase 0.5 → Phase 2 interventional；如果大幅精简 scope（砍掉 Phase 2.5 和简化 Phase 4），可压缩至 14-16 周实际执行

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5df27a9-0683-4cbf-a528-9295a09249ef",
  "isSidechain": false,
  "requestId": "req_011CbDDPrTcvquagWg2M2uJi",
  "type": "assistant",
  "uuid": "d957a75c-610d-4472-b2aa-cf61d1ed7769",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpA4ZvQF1NC3DSDsdF4haH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28721,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28721,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3210,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 28721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28721
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to produce the evaluation. L…",
  "leafUuid": "d957a75c-610d-4472-b2aa-cf61d1ed7769",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Test discourse training pathway to multi-turn safety",
  "sessionId": "0d9dc1d8-a93d-4f65-9e25-a8684efdf74c"
}
```

---
