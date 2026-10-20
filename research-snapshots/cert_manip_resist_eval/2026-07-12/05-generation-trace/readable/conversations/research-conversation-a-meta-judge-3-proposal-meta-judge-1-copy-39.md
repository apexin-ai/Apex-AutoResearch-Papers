# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/6a2d2860-92a0-450a-8f98-c341ca3d3a32.jsonl`
- **Structured JSON:** [`5af1d13792442be6f68d.json`](../../sessions/5a/5af1d13792442be6f68d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:17:36.960Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:17:36.960Z",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n**核心竞争论文（perception-stage rewards for geometric reasoning）：**\n\n- [GeoDPO / GeoPerceive](https://arxiv.org/abs/2602.22703) (arXiv 2026): 最直接竞品。用 learned NL-to-DSL translator 计算 DSL-level reward scores 做 RL，在 in-domain perception 上 +26.5%。但 translator 本身是 neural 的，可能 hallucinate scores。FPR 的目标是用 formal verification 替代这个 neural translator。\n- [Perception-R1](https://arxiv.org/abs/2506.07218) (arXiv 2025): 用 judge LLM 评估视觉感知一致性，仅 1,442 样本达到 SOTA。但 judge 是 neural 的，缺乏 formal grounding。\n- [SymHPR](https://arxiv.org/abs/2512.03126) (arXiv 2025): 用 symbolic auto-encoder 提供 hierarchical per-primitive rewards（point-on-line, line-on-shape consistency），98.2% MSE reduction。**关键区别**：使用 rule-based F1/L2 metric 而非 formal deduction engine，无法检测语义级几何矛盾。这是 FPR 与 SymHPR 的主要差异化点。\n- [EVPV](https://arxiv.org/abs/2603.16253) (arXiv 2026): 提取 structured visual constraints，用 constraint matching 计算 reliability-gating signal 校准 PRM。用 constraint matching 而非 formal geometric verification。\n- [Perceval](https://arxiv.org/abs/2604.24583) (arXiv 2026, April): Perception-centric PRM，支持 token-level error grounding，逐条对比 image-related claims 与 visual evidence。无 formal geometric engine。\n\n**Formal verification for reasoning（非 perception）：**\n\n- [SGVR / GeoGoal](https://arxiv.org/abs/2601.05073) (arXiv 2026): Formal verification 生成 sub-goal rewards，用于 reasoning steps，+9.7%。明确仅用于下游推理，不涉及 perception。\n- [InternGeometry](https://arxiv.org/abs/2512.10534) (arXiv 2025): 用 DDAR-class symbolic engine 在 RL 循环中做 geometry proof，仅用于推理/证明步骤。\n- [FoVer](https://arxiv.org/abs/2505.15960) (ACL 2026 Findings): 用 Z3/Isabelle 合成 step-level PRM training data，展示跨任务泛化，但未应用于 geometric perception。\n\n**2026 年 5 月爆发的 perception reward 论文（proposal 未覆盖的重要并发工作）：**\n\n- [\"Bad Seeing or Bad Thinking?\"](https://arxiv.org/abs/2605.14054) (arXiv 2026.05): 提出 RL 框架，通过 modality credit assignment 分离 perception 和 reasoning rewards。直接竞争方向。\n- [PDCR](https://arxiv.org/abs/2605.13467) (arXiv 2026.05, KAIST/UIUC/MSRA): Perception-Decomposed Confidence Reward，解决 vision step 信号被 textual step 淹没的问题。\n- [\"From Seeing to Thinking\"](https://arxiv.org/abs/2605.20177) (arXiv 2026.05): 系统研究 perception-reasoning decoupling，three-stage training，8B 模型 SOTA。\n- [\"One RL to See Them All\" (V-Triune)](https://arxiv.org/abs/2505.18129) (arXiv 2025.05): 统一 perception + reasoning RL 框架，Sample-Level Reward Routing。\n- [GeoPQA](https://arxiv.org/abs/2509.17437) (EMNLP 2025): 两阶段 RL——先 perception 再 reasoning，几何推理 +9.7%。**Proposal 未引用此论文，但它是这一方向的直接先驱。**\n\n- **调研总结**: 2025 下半年至 2026 年上半年，\"perception-stage reward for VLM\" 已成为一个非常拥挤的赛道（至少 10+ 篇论文）。现有工作使用 neural judges（Perception-R1）、learned translators（GeoDPO）、rule-based metrics（SymHPR）或 constraint matching（EVPV）做 perception reward，而 formal deduction engines 目前仅用于 reasoning steps（SGVR、InternGeometry、FoVer）。Proposal 所声称的 \"formal geometric deduction for perception-stage rewards\" 这一交叉点，据调研确实尚未被占据。但这一赛道的高拥挤度意味着审稿人对 novelty 的要求将非常高。\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。** \n\nFormalGeo7K 提供了每道题的完整 formal annotations（ground truth geometric facts）。最直接的 trivial baseline 是：让 VLM 输出 structured geometric facts，然后与 ground truth annotations 做 **简单的 per-fact F1 matching**（类似 SymHPR 的做法），就已经能提供 (1) per-fact 的 dense reward，(2) 诊断出具体哪个 fact 错了，(3) 实现 targeted re-perception。\n\nFPR 相对于这个 trivial baseline 的 **增量价值** 在于：formal constraint propagation 能检测 **在没有 ground truth 的情况下** 的内部不一致性（e.g., \"angle ABC=90° 与 A 在以 BC 为直径的圆上矛盾\"）。但这引出两个问题：\n1. **训练时有 ground truth**——如果训练集有 annotations，简单 matching 已经足够提供 dense per-fact reward；formal verification 的增量在训练时可能有限。\n2. **测试时无 ground truth**——formal verification 的真正价值在于 test-time self-consistency checking。但 proposal 对此的讨论不够深入：constraint propagation 只能检测 *不一致*，不能检测 *一致但全部错误* 的 perception。\n\n增量价值确实存在（尤其是 test-time 场景和 out-of-distribution 泛化），但 proposal 需要非常清晰地论证为何 formal verification 优于 simple matching，否则审稿人会直接用这个 trivial alternative 来挑战核心贡献。\n\n【前提假设检验】:\n\n核心逻辑链中有 **两个关键的未验证假设**：\n\n1. **\"VLM 的 perception 错误经常表现为 semantically inconsistent geometric facts\"**——这是 formal constraint propagation 相对于 simple matching 产生增量价值的前提。但实际上，VLM 的 perception 错误很可能是\"一致但错误\"的（e.g., 一致地把 60° 看成 45°），而非\"angle ABC=90° 与 A 在圆上矛盾\"这种 semantically inconsistent 的模式。如果大多数 perception 错误是\"一致性内的\"，则 formal verification 的额外价值有限。**Proposal 没有提供任何实证来支撑这个假设。**\n\n2. **\"Perception-to-formal translation 的质量足以支撑有意义的 formal verification\"**——让一个正在训练的 VLM（Qwen3-VL-8B）用 FormalGeo 的 Geometric Construction Language 输出结构化 facts，这个翻译本身的准确度会影响下游验证的信噪比。如果 VLM 早期输出的 formal language 就是语法错误百出的（无法被 solver 解析），则 formal verification 信号会退化为 \"is the output parseable\" 这种粗粒度信号。Proposal 没有讨论 cold-start 问题或翻译质量的 bootstrap 策略。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \"将 formal geometric deduction engine 应用于 perception-stage RL rewards\" 这个交叉点确实空白，调研确认无现有工作完全覆盖。但 novelty 的性质是 **组合式的**（\"把已有方法 A 用于已有场景 B\"），而非概念性突破。SymHPR 已经做了 per-primitive structured perception rewards（只是用 rule-based 而非 formal deduction），SGVR 已经做了 formal verification rewards（只是用于 reasoning 而非 perception），EVPV 已经做了 structured constraint checking for perception（只是 matching 而非 deduction）。FPR 本质是这三者的自然交汇点——审稿人可能认为这是一个 \"obvious next step\" 而非 \"surprising insight\"。此外，2026 年 5 月爆发的大量 perception reward 论文（\"Bad Seeing or Bad Thinking\", PDCR, \"From Seeing to Thinking\"）进一步压缩了 novelty 空间。\n\n2. **Significance: 中** — Perception bottleneck 确实是一个被广泛认可的重要问题（SVE-Math 的 70% 错误率，GeoPQA 的实证）。但 proposal 的 scope 较窄——仅针对 geometric perception，而非一般性的 visual perception。Formal verification 的 insight（\"把 formal tools 从 reasoning 扩展到 perception\"）如果成立有一定的范式启示意义，但 geometric domain 之外的推广路径不清晰（非几何的 visual perception 没有现成的 formal solver）。此外，赛道极度拥挤，即使结果 positive，如果增量幅度不够大（对比 GeoDPO 的 +26.5%），significance 会被质疑。\n\n3. **Related Work: 中偏强** — Proposal 对核心竞争文献的覆盖和差异化定位做得不错（GeoDPO、Perception-R1、SGVR、SymHPR、EVPV、InternGeometry、FoVer 均有引用和清晰对比）。但存在明显遗漏：**GeoPQA**（EMNLP 2025，两阶段 perception-then-reasoning RL 的直接先驱）未被引用；2026 年 5 月的并发工作群（\"Bad Seeing or Bad Thinking\", PDCR, \"From Seeing to Thinking\", Perceval, V-Triune）虽属并发，但如果投稿前不纳入讨论，审稿人可能会指出缺失。差异化叙事清晰（\"第一个将 formal deduction 用于 perception-stage rewards\"），但需要更好地解释为何 formal deduction > simpler structured approaches（vs. SymHPR, EVPV）。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \nNovelty 维度是主要限制因素：虽然\"formal deduction for perception rewards\"这个交叉点确实空白，但 novelty 本质是组合式的——分别来自 formal verification（SGVR/FoVer 已有）和 perception-stage rewards（SymHPR/EVPV/Perception-R1 已有），FPR 是二者的自然交汇。审稿人可能视其为 \"next obvious step\" 而非 \"surprising insight\"。赛道的高拥挤度（2025-2026 至少 10+ 篇 perception reward 相关论文）进一步抬高了 novelty bar。Trivial alternative 威胁（simple per-fact F1 matching with ground truth）如果在实验中不被充分回应，可能成为致命弱点。Significance 受限于 geometric-specific scope 和增量价值的不确定性。Related work 覆盖尚可但有遗漏。综合来看，idea 方向正确、gap 真实存在，但核心贡献的 \"惊喜度\" 不足以冲击更高区间。\n\n【主要风险】: \n1. **Trivial Alternative 威胁**：审稿人可能直接问 \"和简单的 per-fact ground-truth matching 相比，formal constraint propagation 到底带来了多少增量？\"——如果实验中这个 ablation 的 delta 很小，论文的核心贡献就站不住。\n2. **组合式 novelty 在拥挤赛道中的生存空间**：SGVR（formal verification for reasoning）+ SymHPR（structured perception rewards）的自然组合，在一个 2026 年爆发了大量 perception reward 论文的赛道中，可能被审稿人认为是 incremental 的、缺乏 conceptual depth。\n```\n\nSources:\n- [GeoDPO (arXiv 2602.22703)](https://arxiv.org/abs/2602.22703)\n- [Perception-R1 (arXiv 2506.07218)](https://arxiv.org/abs/2506.07218)\n- [SGVR (arXiv 2601.05073)](https://arxiv.org/abs/2601.05073)\n- [SymHPR (arXiv 2512.03126)](https://arxiv.org/abs/2512.03126)\n- [EVPV (arXiv 2603.16253)](https://arxiv.org/abs/2603.16253)\n- [InternGeometry (arXiv 2512.10534)](https://arxiv.org/abs/2512.10534)\n- [FoVer (arXiv 2505.15960)](https://arxiv.org/abs/2505.15960)\n- [Perceval (arXiv 2604.24583)](https://arxiv.org/abs/2604.24583)\n- [Bad Seeing or Bad Thinking? (arXiv 2605.14054)](https://arxiv.org/abs/2605.14054)\n- [PDCR (arXiv 2605.13467)](https://arxiv.org/abs/2605.13467)\n- [From Seeing to Thinking (arXiv 2605.20177)](https://arxiv.org/abs/2605.20177)\n- [One RL to See Them All (arXiv 2505.18129)](https://arxiv.org/abs/2505.18129)\n- [GeoPQA (arXiv 2509.17437)](https://arxiv.org/abs/2509.17437)\n- [AlphaGeometry2 DDAR engine](https://github.com/google-deepmind/alphageometry2)\n- [FormalGeo (arXiv 2310.18021)](https://arxiv.org/abs/2310.18021)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [GeoDPO] (arXiv 2602.22703, Feb 2026): 最直接的竞争工作。使用 learned NL-to-DSL translator 计算 DSL 级别的 perception reward，GRPO/DPO 训练 VLM。在 in-domain geometric perception 上 +26.5%，downstream reasoning +39%。核心区别：translator 是 learned 的（可 hallucinate），非 formal verification。\n- [Perception-R1] (arXiv 2506.07218, Jun 2025): 使用 judge LLM 评估视觉感知一致性作为 reward。仅用 1,442 样本达到 SOTA。核心区别：neural judge，无 formal grounding。\n- [SGVR/GeoGoal] (arXiv 2601.05073, Jan 2026): 用 formal verification data engine 生成 sub-goal reward，but **仅用于 reasoning steps（downstream）**，不涉及 perception stage。+9.7% geometric reasoning。这是距离 proposal 最近的\"上游\"工作。\n- [SymHPR] (arXiv 2512.03126, Dec 2025): 针对 perception stage 的 structured hierarchical reward（point-on-line, line-on-shape），但使用 rule-based F1/L2 metrics，**不是 formal deduction engine**。98.2% MSE reduction in diagram reconstruction。这是距离 proposal 最近的\"功能\"竞争者。\n- [EVPV] (arXiv 2603.16253, Mar 2026): 分离 visual grounding error 与 reasoning error，提取 structured visual constraints 做 reliability gating，但使用 constraint matching 而非 formal geometric verification。\n- [FoVer] (arXiv 2505.15960, ACL 2026 Findings): 证明 formal verification tools (Z3, Isabelle) 可以 synthesize step-level PRM 训练数据且有跨任务泛化能力。但尚未应用于 geometric perception。\n- [InternGeometry] (arXiv 2512.10534, Dec 2025): 使用 DDAR-class symbolic engine 在 RL loop 中做 geometry proof/reasoning，解 44/50 IMO 题。但 DDAR 仅用于 reasoning/proof steps，不用于 visual perception。\n- [CogFlow] (arXiv 2601.01874, ICLR 2026): 三阶段框架 perception⇒internalization⇒reasoning，设计 Synergistic Visual Rewards 提升 perception，但不使用 formal deduction engine。\n- [FormalGeo/FormalGeo7K] (arXiv 2310.18021, 2024): 88 geometric predicates + 196 theorems，6,981 问题。DDAR2 用 C++ 实现有 300x 加速。这是 proposal 依赖的核心基础设施。\n\n- 调研总结: 几何感知 RL reward 领域正快速发展，2025-2026 涌现大量工作，但形成了明确的两条线——(1) perception-stage rewards 依赖 learned judges / rule-based metrics (GeoDPO, Perception-R1, SymHPR)；(2) formal verification 仅用于 reasoning-stage rewards (SGVR, InternGeometry, FoVer)。**两条线尚未交汇**。Proposal 定位在这个交汇点上，gap 确实存在。\n\n【Trivial Alternative 检验】:\n最直接的 trivial alternative 是：在 GeoDPO 的 DSL translator 输出上加一层 rule-based consistency checks（如检查角度之和、共线性、圆的性质等），而不需要完整的 formal deduction engine + constraint propagation。\n\n增量价值在于：\n(1) Formal deduction engine 能捕获 **跨定理的语义矛盾**（如 \"angle ABC=90° 与 A 在以 BC 为直径的圆上矛盾\"），这需要定理链推理，简单 rule-based checks 做不到。\n(2) Constraint propagation 能提供 **per-fact 诊断信号**，指出具体哪条感知事实出错，而非整体打分。\n\n但这个增量价值的实际幅度存疑——在实践中，多少 perception error 属于需要跨定理推理才能检测到的\"语义矛盾\"？如果大多数 perception error 是简单的点/线/角识别错误（如读错角度数值、漏检一条线），那 rule-based F1 metrics（SymHPR 方式）可能就足够了。Proposal **没有提供 error taxonomy 或 pilot study 来证明 formal deduction 的必要性**。这是一个实质性弱点。\n\n【前提假设检验】:\n核心 claim 的逻辑链条是：\nVLM 提取几何事实 → FormalGeo solver 做 constraint propagation → 检测矛盾 → 生成 per-fact diagnostic reward → 用于 GRPO 训练\n\n关键未验证假设：\n\n1. **Perception-to-formal translator 的可靠性**: Proposal 要求 VLM 直接输出 FormalGeo 的 Geometric Construction Language 格式。但这本身就是一个 perception + structured output 问题。如果 VLM 连几何事实都提取不准（proposal 自己引用了 GPT-4o 70% 错误率），那它输出 formal language 的可靠性如何保证？这是一个**鸡生蛋蛋生鸡**的问题——你用 formal verification 来改善 perception，但 formal verification 的输入本身就依赖 perception。Proposal 没有充分讨论这个 bootstrapping 难题。\n\n2. **FormalGeo solver 对 \"不完整/含噪\" 输入的鲁棒性**: FormalGeo 设计时假设输入是**完整、正确的 formal specification**。当输入是 VLM 的 noisy、potentially incomplete perception 时，solver 能否有意义地进行 constraint propagation，还是会直接 crash / 给出 trivial \"everything inconsistent\" 结果？\n\n3. **Per-fact diagnostic reward 在 GRPO 中的可用性**: GRPO 通常需要 scalar reward for a complete trajectory。将 per-fact diagnosis 转化为有效的 GRPO reward 需要 reward aggregation 设计。Proposal 假设 \"dense per-fact rewards\" 可以直接使用，但实际的 reward shaping 是非 trivial 的。\n\n4. **DDAR 从 proof steps 到 perception checking 的适配**: DDAR 设计用于从已知几何条件推导新定理/证明步骤。将其用于\"检查一组 perceived facts 的内部一致性\"是一个不同的使用模式。这个适配是否 straightforward，proposal 没有讨论。\n\n【3 维度打分】:\n\n1. Novelty: 中 — \n   理由：Proposal 正确识别了一个真实的 gap：formal verification 已用于 reasoning stage (SGVR, InternGeometry)，perception rewards 已存在但依赖 learned judges (GeoDPO, Perception-R1) 或 rule-based metrics (SymHPR)，两者的交汇点确实空白。然而，这本质上是一个 **\"A 用于 X，B 用于 Y → 把 A 用于 Y\" 的组合式创新**。给定 SGVR 已经展示 formal verification 在 geometric RL 中有效，GeoDPO 已经展示 perception-stage RL rewards 有效，将两者结合是一个自然的、可预期的下一步，而非反直觉的洞察。Per-fact diagnostic reward 和 targeted re-perception 是有意义的功能贡献，但概念层面的 novelty delta 有限。SymHPR 已经在做 hierarchical per-primitive reward for perception——虽然用的不是 formal deduction engine，但思路方向非常接近。\n\n2. Significance: 中 — \n   理由：研究问题本身重要——geometric perception bottleneck 确实是该领域的核心瓶颈（SVE-Math 的 70% 错误率、CogFlow 的 ICLR 2026 接收都印证了问题的重要性）。如果 formal verification 确实能在 perception stage 提供比 learned judges 更好的 reward signal，这将是一个有价值的贡献。但 significance 受限于两点：(a) 适用范围局限于有 formal specification 的几何问题（FormalGeo7K 仅 ~7K 问题），难以推广到更广泛的视觉数学推理；(b) 如果改进主要来自 reward signal quality 的边际提升（而非 paradigm shift），实际影响力有限。\n\n3. Related Work: 强 — \n   理由：Related work coverage 非常全面且准确。对 GeoDPO、Perception-R1、SGVR、SymHPR、EVPV、FoVer、InternGeometry、CogFlow、GeoSketch 等近期工作的描述与我调研结果一致。每篇工作的差异化定位清晰（是 learned vs. formal，是 perception vs. reasoning），convincingly 展示了 gap 的存在。对 SymHPR 的区分（rule-based F1 vs. formal deduction）尤其准确。这是 proposal 最强的维度。\n\n【概率估计】: [23% - 33%] 中位 28%\n\n【估计理由】: \nRelated Work 维度强，表明作者对领域有深刻理解且 gap 确实存在。但 Novelty 是中等——核心创新是组合式的（把 formal verification 从 reasoning stage 搬到 perception stage），缺乏反直觉的洞察；如果结果 positive，审稿人更可能说 \"makes sense, expected this would help\" 而非 \"surprising\"。Significance 也是中等——problem 重要但 contribution 的推广性受限于 formal geometry 的 domain scope。**上界主要被 Novelty 限制**：在 AAAI 审稿人看来，\"obvious bridge\" 类的组合创新通常需要非常强的实验结果来弥补概念新颖性的不足，而目前只是 proposal 阶段无法保证实验强度。另外，前提假设中 perception-to-formal translator 的 bootstrapping 问题若在 rebuttal 中被审稿人抓住，会很难回应。\n\n【主要风险】:\n1. **\"Obvious bridge\" 质疑**: 审稿人很可能指出这是 SGVR (formal verification for reasoning) + GeoDPO (perception-stage RL rewards) 的自然组合，要求更强的 conceptual contribution 或 surprising findings。\n2. **Bootstrapping 循环论证**: Formal verification 依赖 VLM 准确输出 formal language，而 VLM 的准确性正是要通过 formal verification reward 来提升的——这个循环依赖在 proposal 中未被充分论证，审稿人可能视之为 fundamental flaw。\n```\n\nSources:\n- [GeoDPO - arXiv 2602.22703](https://arxiv.org/abs/2602.22703)\n- [Perception-R1 - arXiv 2506.07218](https://arxiv.org/abs/2506.07218)\n- [SGVR - arXiv 2601.05073](https://arxiv.org/abs/2601.05073)\n- [SymHPR - arXiv 2512.03126](https://arxiv.org/abs/2512.03126)\n- [EVPV - arXiv 2603.16253](https://arxiv.org/abs/2603.16253)\n- [FoVer - arXiv 2505.15960](https://arxiv.org/abs/2505.15960)\n- [InternGeometry - arXiv 2512.10534](https://arxiv.org/abs/2512.10534)\n- [CogFlow - arXiv 2601.01874](https://arxiv.org/abs/2601.01874)\n- [FormalGeo - arXiv 2310.18021](https://arxiv.org/abs/2310.18021)\n- [AlphaGeometry2 - arXiv 2502.03544](https://arxiv.org/abs/2502.03544)\n- [FormalGeo Project Site](https://formalgeo.github.io/)\n- [AlphaGeometry2 GitHub (DDAR)](https://github.com/google-deepmind/alphageometry2)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nI now have comprehensive research results. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [GeoDPO] \"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning\" (arXiv:2602.22703, Feb 2026):\n   最直接的竞争工作。使用 learned NL-to-DSL translator 计算 DSL-level scores 作为 RL 奖励，在 in-domain perception +26.5%，downstream reasoning +39%。核心差异：GeoDPO 用 learned translator，本 proposal 用 formal solver。但 GeoDPO 已经证明 structured perception reward 在这个任务上有效，因此 FPR 需要证明 formal verification 相比 learned translator 的 marginal gain。\n\n2. [Perception-R1] \"Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward\" (arXiv:2506.07218, 2025):\n   用 LLM judge 评估 visual perception 一致性作为 reward，仅 1,442 样本即达 SOTA。证明 perception reward 的有效性，但 judge 无 formal grounding。本 proposal 正确识别了这个局限。\n\n3. [SGVR/GeoGoal] \"Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward\" (arXiv:2601.05073, Jan 2026):\n   用 formal verification data engine 生成 sub-goal rewards，geometric reasoning +9.7%。但仅用于 reasoning stage，不涉及 perception。FPR 的核心 novelty claim（将 formal verification 从 reasoning 延伸到 perception）依赖于与 SGVR 的对比。\n\n4. [SymHPR] \"Hierarchical Process Reward Models are Symbolic Vision Learners\" (arXiv:2512.03126, Dec 2025):\n   最接近的 concurrent work。用 symbolic auto-encoder 做 hierarchical per-primitive rewards（point-on-line, line-on-shape consistency），perception +13%。但用 rule-based F1/L2 metric 而非 formal deduction engine。FPR 声称能检测 semantic geometric contradictions 是超越 SymHPR 的点。\n\n5. [EVPV] \"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models\" (arXiv:2603.16253, Mar 2026):\n   分离 visual grounding errors 和 reasoning errors，用 constraint matching 计算 reliability-gating signal。方向高度相关但使用 constraint matching 而非 formal geometric verification。\n\n6. ⚠️ [Bad Seeing or Bad Thinking?] (arXiv:2605.14054, May 2026) — **proposal 未引用**:\n   刚发表 2 周。直接分解 perception vs. reasoning credit assignment，用 RL 框架显式 reward perception fidelity。核心问题与 FPR 高度重叠，虽不使用 formal verification，但直接瞄准同一个 gap。\n\n7. ⚠️ [PDCR] \"Perception-Decomposed Confidence Reward\" (arXiv:2605.13467, May 2026) — **proposal 未引用**:\n   分解 perception 和 reasoning 的 reward signal，解决 mixture-induced signal degradation 问题。另一个 May 2026 的直接竞争者。\n\n8. ⚠️ [From Seeing to Thinking] (arXiv:2605.20177, May 2026) — **proposal 未引用**:\n   系统研究 perception 和 reasoning 在 post-training 中的 interplay，发现 visual perception is more effectively learned via RL than caption-based SFT，且需要 staged training。直接支持 perception-stage RL 的价值，但不使用 formal verification。\n\n9. [FoVer] (arXiv:2505.15960, ACL 2026 Findings):\n   用 Z3/Isabelle 合成 PRM 训练数据，展示 formal verification → PRM 的 cross-task generalization。证明 formal verification tools 可以用于 reward/verification，但未应用到 geometric perception。\n\n10. [InternGeometry] (arXiv:2512.10534, Dec 2025):\n    使用 DDAR-class engine (Newclid) 在 RL loop 中做 geometry reasoning/proof，但仅用于 reasoning steps，不涉及 perception。\n\n- **调研总结**: 2025-2026 年 geometric perception + RL 领域极其活跃。\"Perception-stage reward\" 是明确的研究热点，多篇 May 2026 论文同时瞄准 perception-reasoning credit decomposition。Formal verification 用于 reasoning-stage reward 已被 SGVR、FoVer、InternGeometry 等充分验证。但 formal verification 用于 **perception-stage** reward 确实是一个未被填补的空白。FPR 处于两个已有方向（formal verification for reasoning + RL reward for perception）的交叉点——novelty 来自组合，而非全新 paradigm。\n\n【Trivial Alternative 检验】:\n\n存在实质性的 trivial alternative 威胁：\n\n1. **GeoDPO 的 learned translator 已经能够提供 structured perception reward** 且达到了 +26.5% 的 in-domain 增益。FPR 用 formal solver 替换 learned translator 作为 judge，但 learned translator 本身更灵活、更容易部署、且不需要 FormalGeo format 的严格输出。FPR 需要论证 formal verification 相比 learned DSL scoring 的 marginal gain 值得额外的系统复杂度。\n\n2. **Perception-R1 用简单的 LLM judge 仅用 1,442 样本即达 SOTA**。这说明 perception reward 的有效性可能更多取决于 reward signal 的 existence 而非 reward signal 的 formal rigor。如果一个 $0 成本的 LLM judge 就能工作，投入大量工程去集成 FormalGeo + DDAR 的增量价值需要强有力的论证。\n\n3. **FPR 的真正增量价值**在于 diagnostic capability（per-fact contradiction detection → targeted re-perception）。这是 learned judges 无法提供的。如果实验设计能突出这一点（不仅仅是 overall accuracy，而是 diagnostic precision、re-perception 效率），增量价值可以成立。但如果最终评估只看 accuracy on GeoQA/Geometry3K，这个增量可能不显著。\n\n**结论**：存在 trivial alternative 威胁，但 diagnostic capability 是可辩护的增量价值点——前提是实验设计能充分展示它。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有 **三个关键未验证假设**：\n\n1. **⚠️ 最关键：Internal consistency ≠ Perception correctness**。FPR 的 formal solver 执行 constraint propagation 检查 extracted facts 的内部一致性。但一组 geometrically self-consistent 的 facts 不意味着它们 match 实际 diagram。例如：VLM 将一个三角形的所有角系统性地误差 10°，但新的角度值恰好满足内部约束（三角形角和 = 180°），formal checker 不会报错。Proposal 暗示 formal verification = perception verification，但实际上 formal solver 只能检测 **self-contradictions**，不能检测 **与 ground truth diagram 的偏差**。这是一个根本性的逻辑缺口。\n\n   - 缓解因素：(a) 多数 perception errors 确实会产生内部矛盾（不太可能所有 errors 恰好 self-consistent）；(b) FormalGeo7K 有 ground truth formal annotations，可以作为 reference 进行比较。但如果使用 ground truth comparison，那本质上就是 structured matching（与 GeoDPO 类似），\"formal verification\" 的 claim 就变弱了。\n\n2. **Perception-to-formal translation bottleneck 的 chicken-and-egg 问题**。FPR 要求 VLM 输出 FormalGeo Geometric Construction Language 格式的 structured facts。但能可靠输出这种格式的 VLM 已经在很大程度上\"解决\"了 perception 问题。如果 VLM 的 formal output 本身就充满错误，formal checker 收到的是 noisy input，其 diagnostic signal 的可靠性大打折扣。Proposal 没有讨论这个 bootstrapping 问题——第一轮训练时 VLM 的 formal output 质量如何？\n\n3. **DDAR/FormalGeo 的 coverage 和 latency 假设**。Proposal 提到 FormalGeo constraint checking throughput ~50 problems/sec on CPU，但 RL 训练中每个 step 都需要 reward computation。GRPO 的 batch size 通常需要 thousands of reward evaluations per step。50 problems/sec 在 RL loop 中是否足够快？Proposal 提到可能需要 \"batched verification or C++ DDAR backend\"，但这本身是一个非平凡的工程假设。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   FPR 处于两个已有方向的交叉点：formal verification for reasoning（SGVR, FoVer, InternGeometry 已充分验证）和 RL reward for perception（GeoDPO, Perception-R1, SymHPR, EVPV 等已大量探索）。将 formal deduction engine 应用到 perception stage 确实是未被填补的组合空白，proposal 对此的识别是准确的。Diagnostic capability（per-fact contradiction detection → targeted re-perception）是一个有意义的 novelty contribution。\n   \n   但这本质上是一个 **组合创新**（combination novelty）而非 **范式创新**：把 A（已有）用到 B（已有但 A 没用过的场景）。审稿人对组合创新的标准会更高——需要论证为什么这个组合非平凡、为什么简单的 learned approach 不够。此外，May 2026 三篇未引用的论文（\"Bad Seeing or Bad Thinking?\", PDCR, \"From Seeing to Thinking\"）表明 perception-stage reward 的研究空间正在快速被填充，虽然它们不使用 formal verification，但进一步削弱了 novelty perception。\n\n2. **Significance: 中** — \n   研究问题（geometric perception bottleneck）是 well-documented 且重要的（SVE-Math 的 70% error rate）。\"From Seeing to Thinking\" 进一步确认 perception 需要 specialized RL training。但 FPR 的 approach 是 **domain-specific to geometry**——formal geometric constraint checking 无法推广到一般的 visual perception tasks（如 chart understanding, scene description, spatial reasoning）。这限制了 significance 的 scope。与 Perception-R1（general visual perception reward）和 PDCR（general perception-reasoning decomposition）相比，FPR 的适用范围窄得多。\n   \n   此外，核心发现如果 positive——\"formal geometric constraints as rewards improve geometric perception\"——审稿人可能的反应是 \"this makes sense\"（logical extension）而非 \"surprising\"。把 formal verification（在 reasoning 上已被证明有效）用到 perception（另一个 stage），结果确实有效，这不是一个反直觉的发现。\n\n3. **Related Work: 中偏强** — \n   Proposal 对 2025-early 2026 的 landscape 覆盖较好：GeoDPO, Perception-R1, SGVR, SymHPR, EVPV, FoVer, InternGeometry, GeoSketch 等核心工作均被引用，差异化定位清晰（每个 prior work 做了什么、缺什么）。ACL 2026 survey 也被引用。\n   \n   但存在 **显著的 coverage gap**：May 2026 三篇高度相关的论文未被覆盖——\"Bad Seeing or Bad Thinking?\" (2605.14054), PDCR (2605.13467), \"From Seeing to Thinking\" (2605.20177)。这些论文直接瞄准 perception-reasoning credit decomposition，是最近且最直接的竞争者。此外，Vision-SR1 (2508.19652) 和 PEARL (2511.18437) 也未被提及。考虑到这些是 May 2026 的论文，submission 之前应该能发现。GCA (2511.22659, Geometrically-Constrained Agent) 使用 VLM 翻译查询为 formal constraints 的 paradigm 也高度相关但未引用。\n\n【概率估计】: [20% - 30%] 中位 24%\n\n【估计理由】: \nIdea 的核心是一个 **组合创新**——将已被验证的 formal verification 从 reasoning stage 延伸到 perception stage。这个组合空白确实存在（调研确认无直接竞争者做到了这一点），但它更多是一个 \"natural next step\" 而非 \"surprising insight\"。三个维度中，Novelty 受限于组合性质（非范式级创新），Significance 受限于 geometry-specific scope 和 \"I would have guessed this\" 的预期性。最严重的 idea 层面问题是 **internal consistency ≠ perception correctness 的逻辑缺口**——这不是实验能补救的，它质疑 formal verification 作为 perception reward 的 fundamental validity。如果这个缺口在 rebuttal 中被审稿人追问，defense 难度较大。上界被 novelty 和 significance 的双重 \"中\" 评级限制在 ~30%；下界被 \"gap 确实存在 + diagnostic capability 有价值\" 支撑在 ~20%。\n\n【主要风险】:\n1. **Internal consistency ≠ perception correctness 的逻辑缺口**: 审稿人会追问 \"formal solver 只能检测自相矛盾，无法检测与 ground truth diagram 的偏差——你们的 reward 到底在 reward 什么？\" 如果 reward 本质上退化为 ground truth matching，那和 GeoDPO 的 structured scoring 差异不大，novelty claim 会坍塌。\n2. **Trivial alternative 威胁**: Perception-R1 用简单 LLM judge + 1,442 样本即达 SOTA，GeoDPO 用 learned translator 达 +26.5%。审稿人会问 \"为什么需要 FormalGeo + DDAR 的重型 infrastructure？marginal gain 是否值得？\" 如果 FPR 的最终数字只和这些方法 comparable 或 marginally better，story 很难成立。\n```\n\nSources:\n- [GeoDPO - arXiv:2602.22703](https://arxiv.org/abs/2602.22703)\n- [Perception-R1 - arXiv:2506.07218](https://arxiv.org/abs/2506.07218)\n- [SGVR - arXiv:2601.05073](https://arxiv.org/abs/2601.05073)\n- [SymHPR - arXiv:2512.03126](https://arxiv.org/abs/2512.03126)\n- [EVPV - arXiv:2603.16253](https://arxiv.org/abs/2603.16253)\n- [FormalGeo - arXiv:2310.18021](https://arxiv.org/abs/2310.18021)\n- [FoVer - arXiv:2505.15960](https://arxiv.org/abs/2505.15960)\n- [InternGeometry - arXiv:2512.10534](https://arxiv.org/abs/2512.10534)\n- [Bad Seeing or Bad Thinking? - arXiv:2605.14054](https://arxiv.org/abs/2605.14054)\n- [PDCR - arXiv:2605.13467](https://arxiv.org/abs/2605.13467)\n- [From Seeing to Thinking - arXiv:2605.20177](https://arxiv.org/abs/2605.20177)\n- [AlphaGeometry2 GitHub](https://github.com/google-deepmind/alphageometry2)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Formal Geometric Constraints as Verifiable Perception Rewards\n\n## Core Problem\n\nHow can we provide formally verifiable, diagnostic reward signals for the visual perception stage of multimodal geometric reasoning, moving beyond learned neural judges that can be gamed or miss subtle geometric inconsistencies?\n\n## Research Opportunity\n\nCurrent RL approaches for visual math perception (GeoDPO, Perception-R1, PRCO) all rely on learned judges — either DSL-score translators or LLM consistency checkers — which lack formal guarantees and cannot diagnose WHICH specific perception is wrong. Meanwhile, formal verification methods (Safe/Lean 4, SGVR/GeoGoal) have proven powerful but remain confined to text-based reasoning steps, never applied to the perception stage. AlphaGeometry2's DDAR engine and FormalGeo7K now make it feasible to perform symbolic geometric constraint checking at scale, providing a bridge that didn't previously exist.\n\n## Research Landscape\n\nThe perception bottleneck in visual geometric reasoning is well-documented: GPT-4o exhibits a 70% error rate on geometric primitive grounding (SVE-Math, arXiv:2501.06430). GeoDPO (arXiv:2602.22703) uses a learned NL-to-DSL translator to compute DSL-level reward scores for RL training, achieving +26.5% on in-domain geometric perception, but the translator itself can hallucinate scores. Perception-R1 (arXiv:2506.07218) uses a judge LLM for visual perception rewards achieving SOTA with minimal data, but the neural judge lacks formal grounding. SGVR (arXiv:2601.05073) uses a formal verification engine to generate sub-goal rewards for geometric reasoning (+9.7%), but only for downstream reasoning steps, not perception. GeoSketch (arXiv:2509.22460) implements auto-correction by comparing generated-vs-original diagrams via MLLM, but acknowledges it 'does not assess the correctness or validity of intermediate steps.' SymHPR (arXiv:2512.03126) is the closest concurrent work targeting perception-stage structured rewards: it uses a symbolic auto-encoder with hierarchical per-primitive rewards (point-on-line, line-on-shape consistency) achieving 98.2% MSE reduction in diagram reconstruction, but employs rule-based F1/L2 metric comparison rather than a formal deduction engine or constraint propagation — it cannot detect semantic geometric contradictions (e.g., an angle value inconsistent with a circle theorem). EVPV (arXiv:2603.16253) separates visual grounding errors from reasoning errors in process reward models by extracting structured visual constraints and computing a reliability-gating signal, but uses constraint matching rather than formal geometric verification. InternGeometry (arXiv:2512.10534) uses a DDAR-class symbolic engine in an RL loop for geometry but only for reasoning/proof steps, not visual perception. FoVer (arXiv:2505.15960, ACL 2026 Findings) demonstrates that formal verification tools (Z3, Isabelle) can synthesize step-level PRM training data with cross-task generalization, but has not been applied to geometric perception. The ACL 2026 geometry survey (arXiv:2507.11936) identifies 'formal language representations' and automated verification as critical open challenges. No existing work bridges formal geometric deduction engines to perception-stage RL rewards — the key novel contribution would be using symbolic constraint propagation not just to score but to DIAGNOSE specific perception errors (e.g., 'angle ABC=90° contradicts A being on circle with diameter BC'), enabling targeted re-perception at test time and dense per-fact reward signals at training time.\n\n## Proposed Approach\n\nWe propose FormalPerceptReward (FPR), which constructs a formally verifiable reward pipeline for visual geometric perception by coupling a perception-to-formal translator with FormalGeo's symbolic solver and AlphaGeometry2's DDAR engine. A VLM (Qwen3-VL-8B, currently the strongest open-source VLM at its scale with 85.8% MathVista for the 235B variant) is prompted to output structured geometric facts from a diagram in FormalGeo's Geometric Construction Language; the symbolic solver then performs constraint propagation to check internal consistency, flagging specific contradictions (e.g., 'perceived angle ABC=90 degrees is inconsistent with A lying on circle with diameter BC') as per-fact diagnostic signals. These dense formal-verification rewards replace learned neural judges in GRPO training on FormalGeo7K's ~7K annotated problems augmented with Geometry3K diagrams, following the lightweight training paradigm demonstrated by Perception-R1 (SOTA from only 1,442 samples on 16x A800 GPUs). At test time, the diagnostic feedback loop enables targeted re-perception: the model re-examines only the specific geometric facts flagged as inconsistent, rather than re-processing the entire diagram, analogous to how SGVR's skeleton-rate metric provides sub-goal granularity but now applied at the perception stage.\n\n## Detailed Description\n\nWe introduce FormalPerceptReward (FPR), the first framework to apply formal geometric deduction engines as verifiable reward signals for the visual perception stage of multimodal geometric reasoning. While existing RL approaches for geometric perception rely on learned neural judges — GeoDPO's DSL translator, Perception-R1's LLM judge, SymHPR's rule-based F1 metrics — that lack formal guarantees, and formal verification methods (SGVR, Safe, FoVer) remain confined to downstream reasoning steps, FPR bridges this gap. Given a VLM's extracted geometric facts from a diagram, FormalGeo's symbolic solver and AlphaGeometry2's DDAR engine perform constraint propagation to identify specific contradictions, producing per-fact diagnostic reward signals. These dense, formally-grounded rewards enable GRPO training on FormalGeo7K (~7K annotated problems) with Qwen3-VL-8B as the base model, replacing opaque neural judges with transparent symbolic verification. At test time, diagnostic feedback enables targeted re-perception of specific erroneous facts rather than full-diagram re-processing. Concurrent work search (May 2026) confirms no existing paper combines formal deduction engines with perception-stage RL rewards. We target improvements over GeoDPO's +26.5% in-domain perception gain and SGVR's +9.7% reasoning gain, evaluating on GeoQA, Geometry3K, and PGPS9K benchmarks.\n\n## Key References\n\n- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026, 2602.22703)\n- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025, 2506.07218)\n- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (arXiv 2026, 2601.05073)\n- Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs [SVE-Math] (arXiv 2025, 2501.06430)\n- Solving Olympiad Geometry without Human Demonstrations [AlphaGeometry] (Nature 2024)\n- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (Symmetry 2024, arXiv 2310.18021)\n- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026, arXiv 2601.01874)\n- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025, 2512.03126)\n- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026, 2603.16253)\n- Efficient PRM Training Data Synthesis via Formal Verification [FoVer] (ACL 2026 Findings, arXiv 2505.15960)\n- GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning with Auxiliary Line Construction and Affine Transformation (arXiv 2025, 2509.22460)\n- A Survey of Deep Learning for Geometry Problem Solving (ACL 2026 Main, arXiv 2507.11936)\n- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (arXiv 2025, 2506.04592)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 2500–3000 (16x A800-80G: ~6 GRPO training runs × 20h each + ablations + evaluation), timeline: 5 months (M1: perception-to-formal translator + FormalGeo/DDAR integration; M2–3: GRPO training experiments + reward design iteration; M4: comprehensive evaluation + ablations on GeoQA/Geometry3K/PGPS9K; M5: paper writing), estimated_gpu_cost: $5,000–6,000 (at ~$2/GPU-hr for A800 cloud instances)\n- **human_in_loop**: gpu_hours: 2000–2500 (Claude accelerates translator code + reward shaping, fewer wasted runs), timeline: 3.5–4 months (M1: pipeline + initial experiments with Claude-assisted code generation; M2–3: GRPO training + hyperparameter search; M3.5–4: evaluation + paper drafting), claude_api_cost: $300–500 (code generation for FormalGeo integration, reward function design, experiment analysis, paper drafting), estimated_gpu_cost: $4,000–5,000\n- **auto_research**: gpu_hours: 3000–4000 (more exploratory runs for reward variants, automated ablations), timeline: 2.5–3 months (parallel experiment scheduling, automated evaluation pipelines), claude_api_cost: $1,200–2,000 (extensive code generation, automated experiment orchestration, result analysis, full paper writing), estimated_gpu_cost: $6,000–8,000, speed_bottleneck: RL training wall-clock time: each GRPO run takes ~16–20 hours on 16x A800 GPUs regardless of automation; FormalGeo constraint checking throughput (~50 problems/sec on CPU) may require batched verification or C++ DDAR backend for RL-loop latency\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T08:17:36.963Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:17:36.963Z",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T08:17:37.009Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

**核心竞争论文（perception-stage rewards for geometric reasoning）：**

- [GeoDPO / GeoPerceive](https://arxiv.org/abs/2602.22703) (arXiv 2026): 最直接竞品。用 learned NL-to-DSL translator 计算 DSL-level reward scores 做 RL，在 in-domain perception 上 +26.5%。但 translator 本身是 neural 的，可能 hallucinate scores。FPR 的目标是用 formal verification 替代这个 neural translator。
- [Perception-R1](https://arxiv.org/abs/2506.07218) (arXiv 2025): 用 judge LLM 评估视觉感知一致性，仅 1,442 样本达到 SOTA。但 judge 是 neural 的，缺乏 formal grounding。
- [SymHPR](https://arxiv.org/abs/2512.03126) (arXiv 2025): 用 symbolic auto-encoder 提供 hierarchical per-primitive rewards（point-on-line, line-on-shape consistency），98.2% MSE reduction。**关键区别**：使用 rule-based F1/L2 metric 而非 formal deduction engine，无法检测语义级几何矛盾。这是 FPR 与 SymHPR 的主要差异化点。
- [EVPV](https://arxiv.org/abs/2603.16253) (arXiv 2026): 提取 structured visual constraints，用 constraint matching 计算 reliability-gating signal 校准 PRM。用 constraint matching 而非 formal geometric verification。
- [Perceval](https://arxiv.org/abs/2604.24583) (arXiv 2026, April): Perception-centric PRM，支持 token-level error grounding，逐条对比 image-related claims 与 visual evidence。无 formal geometric engine。

**Formal verification for reasoning（非 perception）：**

- [SGVR / GeoGoal](https://arxiv.org/abs/2601.05073) (arXiv 2026): Formal verification 生成 sub-goal rewards，用于 reasoning steps，+9.7%。明确仅用于下游推理，不涉及 perception。
- [InternGeometry](https://arxiv.org/abs/2512.10534) (arXiv 2025): 用 DDAR-class symbolic engine 在 RL 循环中做 geometry proof，仅用于推理/证明步骤。
- [FoVer](https://arxiv.org/abs/2505.15960) (ACL 2026 Findings): 用 Z3/Isabelle 合成 step-level PRM training data，展示跨任务泛化，但未应用于 geometric perception。

**2026 年 5 月爆发的 perception reward 论文（proposal 未覆盖的重要并发工作）：**

- ["Bad Seeing or Bad Thinking?"](https://arxiv.org/abs/2605.14054) (arXiv 2026.05): 提出 RL 框架，通过 modality credit assignment 分离 perception 和 reasoning rewards。直接竞争方向。
- [PDCR](https://arxiv.org/abs/2605.13467) (arXiv 2026.05, KAIST/UIUC/MSRA): Perception-Decomposed Confidence Reward，解决 vision step 信号被 textual step 淹没的问题。
- ["From Seeing to Thinking"](https://arxiv.org/abs/2605.20177) (arXiv 2026.05): 系统研究 perception-reasoning decoupling，three-stage training，8B 模型 SOTA。
- ["One RL to See Them All" (V-Triune)](https://arxiv.org/abs/2505.18129) (arXiv 2025.05): 统一 perception + reasoning RL 框架，Sample-Level Reward Routing。
- [GeoPQA](https://arxiv.org/abs/2509.17437) (EMNLP 2025): 两阶段 RL——先 perception 再 reasoning，几何推理 +9.7%。**Proposal 未引用此论文，但它是这一方向的直接先驱。**

- **调研总结**: 2025 下半年至 2026 年上半年，"perception-stage reward for VLM" 已成为一个非常拥挤的赛道（至少 10+ 篇论文）。现有工作使用 neural judges（Perception-R1）、learned translators（GeoDPO）、rule-based metrics（SymHPR）或 constraint matching（EVPV）做 perception reward，而 formal deduction engines 目前仅用于 reasoning steps（SGVR、InternGeometry、FoVer）。Proposal 所声称的 "formal geometric deduction for perception-stage rewards" 这一交叉点，据调研确实尚未被占据。但这一赛道的高拥挤度意味着审稿人对 novelty 的要求将非常高。

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 

FormalGeo7K 提供了每道题的完整 formal annotations（ground truth geometric facts）。最直接的 trivial baseline 是：让 VLM 输出 structured geometric facts，然后与 ground truth annotations 做 **简单的 per-fact F1 matching**（类似 SymHPR 的做法），就已经能提供 (1) per-fact 的 dense reward，(2) 诊断出具体哪个 fact 错了，(3) 实现 targeted re-perception。

FPR 相对于这个 trivial baseline 的 **增量价值** 在于：formal constraint propagation 能检测 **在没有 ground truth 的情况下** 的内部不一致性（e.g., "angle ABC=90° 与 A 在以 BC 为直径的圆上矛盾"）。但这引出两个问题：
1. **训练时有 ground truth**——如果训练集有 annotations，简单 matching 已经足够提供 dense per-fact reward；formal verification 的增量在训练时可能有限。
2. **测试时无 ground truth**——formal verification 的真正价值在于 test-time self-consistency checking。但 proposal 对此的讨论不够深入：constraint propagation 只能检测 *不一致*，不能检测 *一致但全部错误* 的 perception。

增量价值确实存在（尤其是 test-time 场景和 out-of-distribution 泛化），但 proposal 需要非常清晰地论证为何 formal verification 优于 simple matching，否则审稿人会直接用这个 trivial alternative 来挑战核心贡献。

【前提假设检验】:

核心逻辑链中有 **两个关键的未验证假设**：

1. **"VLM 的 perception 错误经常表现为 semantically inconsistent geometric facts"**——这是 formal constraint propagation 相对于 simple matching 产生增量价值的前提。但实际上，VLM 的 perception 错误很可能是"一致但错误"的（e.g., 一致地把 60° 看成 45°），而非"angle ABC=90° 与 A 在圆上矛盾"这种 semantically inconsistent 的模式。如果大多数 perception 错误是"一致性内的"，则 formal verification 的额外价值有限。**Proposal 没有提供任何实证来支撑这个假设。**

2. **"Perception-to-formal translation 的质量足以支撑有意义的 formal verification"**——让一个正在训练的 VLM（Qwen3-VL-8B）用 FormalGeo 的 Geometric Construction Language 输出结构化 facts，这个翻译本身的准确度会影响下游验证的信噪比。如果 VLM 早期输出的 formal language 就是语法错误百出的（无法被 solver 解析），则 formal verification 信号会退化为 "is the output parseable" 这种粗粒度信号。Proposal 没有讨论 cold-start 问题或翻译质量的 bootstrap 策略。

【3 维度打分】:

1. **Novelty: 中** — "将 formal geometric deduction engine 应用于 perception-stage RL rewards" 这个交叉点确实空白，调研确认无现有工作完全覆盖。但 novelty 的性质是 **组合式的**（"把已有方法 A 用于已有场景 B"），而非概念性突破。SymHPR 已经做了 per-primitive structured perception rewards（只是用 rule-based 而非 formal deduction），SGVR 已经做了 formal verification rewards（只是用于 reasoning 而非 perception），EVPV 已经做了 structured constraint checking for perception（只是 matching 而非 deduction）。FPR 本质是这三者的自然交汇点——审稿人可能认为这是一个 "obvious next step" 而非 "surprising insight"。此外，2026 年 5 月爆发的大量 perception reward 论文（"Bad Seeing or Bad Thinking", PDCR, "From Seeing to Thinking"）进一步压缩了 novelty 空间。

2. **Significance: 中** — Perception bottleneck 确实是一个被广泛认可的重要问题（SVE-Math 的 70% 错误率，GeoPQA 的实证）。但 proposal 的 scope 较窄——仅针对 geometric perception，而非一般性的 visual perception。Formal verification 的 insight（"把 formal tools 从 reasoning 扩展到 perception"）如果成立有一定的范式启示意义，但 geometric domain 之外的推广路径不清晰（非几何的 visual perception 没有现成的 formal solver）。此外，赛道极度拥挤，即使结果 positive，如果增量幅度不够大（对比 GeoDPO 的 +26.5%），significance 会被质疑。

3. **Related Work: 中偏强** — Proposal 对核心竞争文献的覆盖和差异化定位做得不错（GeoDPO、Perception-R1、SGVR、SymHPR、EVPV、InternGeometry、FoVer 均有引用和清晰对比）。但存在明显遗漏：**GeoPQA**（EMNLP 2025，两阶段 perception-then-reasoning RL 的直接先驱）未被引用；2026 年 5 月的并发工作群（"Bad Seeing or Bad Thinking", PDCR, "From Seeing to Thinking", Perceval, V-Triune）虽属并发，但如果投稿前不纳入讨论，审稿人可能会指出缺失。差异化叙事清晰（"第一个将 formal deduction 用于 perception-stage rewards"），但需要更好地解释为何 formal deduction > simpler structured approaches（vs. SymHPR, EVPV）。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Novelty 维度是主要限制因素：虽然"formal deduction for perception rewards"这个交叉点确实空白，但 novelty 本质是组合式的——分别来自 formal verification（SGVR/FoVer 已有）和 perception-stage rewards（SymHPR/EVPV/Perception-R1 已有），FPR 是二者的自然交汇。审稿人可能视其为 "next obvious step" 而非 "surprising insight"。赛道的高拥挤度（2025-2026 至少 10+ 篇 perception reward 相关论文）进一步抬高了 novelty bar。Trivial alternative 威胁（simple per-fact F1 matching with ground truth）如果在实验中不被充分回应，可能成为致命弱点。Significance 受限于 geometric-specific scope 和增量价值的不确定性。Related work 覆盖尚可但有遗漏。综合来看，idea 方向正确、gap 真实存在，但核心贡献的 "惊喜度" 不足以冲击更高区间。

【主要风险】: 
1. **Trivial Alternative 威胁**：审稿人可能直接问 "和简单的 per-fact ground-truth matching 相比，formal constraint propagation 到底带来了多少增量？"——如果实验中这个 ablation 的 delta 很小，论文的核心贡献就站不住。
2. **组合式 novelty 在拥挤赛道中的生存空间**：SGVR（formal verification for reasoning）+ SymHPR（structured perception rewards）的自然组合，在一个 2026 年爆发了大量 perception reward 论文的赛道中，可能被审稿人认为是 incremental 的、缺乏 conceptual depth。
```

Sources:
- [GeoDPO (arXiv 2602.22703)](https://arxiv.org/abs/2602.22703)
- [Perception-R1 (arXiv 2506.07218)](https://arxiv.org/abs/2506.07218)
- [SGVR (arXiv 2601.05073)](https://arxiv.org/abs/2601.05073)
- [SymHPR (arXiv 2512.03126)](https://arxiv.org/abs/2512.03126)
- [EVPV (arXiv 2603.16253)](https://arxiv.org/abs/2603.16253)
- [InternGeometry (arXiv 2512.10534)](https://arxiv.org/abs/2512.10534)
- [FoVer (arXiv 2505.15960)](https://arxiv.org/abs/2505.15960)
- [Perceval (arXiv 2604.24583)](https://arxiv.org/abs/2604.24583)
- [Bad Seeing or Bad Thinking? (arXiv 2605.14054)](https://arxiv.org/abs/2605.14054)
- [PDCR (arXiv 2605.13467)](https://arxiv.org/abs/2605.13467)
- [From Seeing to Thinking (arXiv 2605.20177)](https://arxiv.org/abs/2605.20177)
- [One RL to See Them All (arXiv 2505.18129)](https://arxiv.org/abs/2505.18129)
- [GeoPQA (arXiv 2509.17437)](https://arxiv.org/abs/2509.17437)
- [AlphaGeometry2 DDAR engine](https://github.com/google-deepmind/alphageometry2)
- [FormalGeo (arXiv 2310.18021)](https://arxiv.org/abs/2310.18021)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:
- [GeoDPO] (arXiv 2602.22703, Feb 2026): 最直接的竞争工作。使用 learned NL-to-DSL translator 计算 DSL 级别的 perception reward，GRPO/DPO 训练 VLM。在 in-domain geometric perception 上 +26.5%，downstream reasoning +39%。核心区别：translator 是 learned 的（可 hallucinate），非 formal verification。
- [Perception-R1] (arXiv 2506.07218, Jun 2025): 使用 judge LLM 评估视觉感知一致性作为 reward。仅用 1,442 样本达到 SOTA。核心区别：neural judge，无 formal grounding。
- [SGVR/GeoGoal] (arXiv 2601.05073, Jan 2026): 用 formal verification data engine 生成 sub-goal reward，but **仅用于 reasoning steps（downstream）**，不涉及 perception stage。+9.7% geometric reasoning。这是距离 proposal 最近的"上游"工作。
- [SymHPR] (arXiv 2512.03126, Dec 2025): 针对 perception stage 的 structured hierarchical reward（point-on-line, line-on-shape），但使用 rule-based F1/L2 metrics，**不是 formal deduction engine**。98.2% MSE reduction in diagram reconstruction。这是距离 proposal 最近的"功能"竞争者。
- [EVPV] (arXiv 2603.16253, Mar 2026): 分离 visual grounding error 与 reasoning error，提取 structured visual constraints 做 reliability gating，但使用 constraint matching 而非 formal geometric verification。
- [FoVer] (arXiv 2505.15960, ACL 2026 Findings): 证明 formal verification tools (Z3, Isabelle) 可以 synthesize step-level PRM 训练数据且有跨任务泛化能力。但尚未应用于 geometric perception。
- [InternGeometry] (arXiv 2512.10534, Dec 2025): 使用 DDAR-class symbolic engine 在 RL loop 中做 geometry proof/reasoning，解 44/50 IMO 题。但 DDAR 仅用于 reasoning/proof steps，不用于 visual perception。
- [CogFlow] (arXiv 2601.01874, ICLR 2026): 三阶段框架 perception⇒internalization⇒reasoning，设计 Synergistic Visual Rewards 提升 perception，但不使用 formal deduction engine。
- [FormalGeo/FormalGeo7K] (arXiv 2310.18021, 2024): 88 geometric predicates + 196 theorems，6,981 问题。DDAR2 用 C++ 实现有 300x 加速。这是 proposal 依赖的核心基础设施。

- 调研总结: 几何感知 RL reward 领域正快速发展，2025-2026 涌现大量工作，但形成了明确的两条线——(1) perception-stage rewards 依赖 learned judges / rule-based metrics (GeoDPO, Perception-R1, SymHPR)；(2) formal verification 仅用于 reasoning-stage rewards (SGVR, InternGeometry, FoVer)。**两条线尚未交汇**。Proposal 定位在这个交汇点上，gap 确实存在。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是：在 GeoDPO 的 DSL translator 输出上加一层 rule-based consistency checks（如检查角度之和、共线性、圆的性质等），而不需要完整的 formal deduction engine + constraint propagation。

增量价值在于：
(1) Formal deduction engine 能捕获 **跨定理的语义矛盾**（如 "angle ABC=90° 与 A 在以 BC 为直径的圆上矛盾"），这需要定理链推理，简单 rule-based checks 做不到。
(2) Constraint propagation 能提供 **per-fact 诊断信号**，指出具体哪条感知事实出错，而非整体打分。

但这个增量价值的实际幅度存疑——在实践中，多少 perception error 属于需要跨定理推理才能检测到的"语义矛盾"？如果大多数 perception error 是简单的点/线/角识别错误（如读错角度数值、漏检一条线），那 rule-based F1 metrics（SymHPR 方式）可能就足够了。Proposal **没有提供 error taxonomy 或 pilot study 来证明 formal deduction 的必要性**。这是一个实质性弱点。

【前提假设检验】:
核心 claim 的逻辑链条是：
VLM 提取几何事实 → FormalGeo solver 做 constraint propagation → 检测矛盾 → 生成 per-fact diagnostic reward → 用于 GRPO 训练

关键未验证假设：

1. **Perception-to-formal translator 的可靠性**: Proposal 要求 VLM 直接输出 FormalGeo 的 Geometric Construction Language 格式。但这本身就是一个 perception + structured output 问题。如果 VLM 连几何事实都提取不准（proposal 自己引用了 GPT-4o 70% 错误率），那它输出 formal language 的可靠性如何保证？这是一个**鸡生蛋蛋生鸡**的问题——你用 formal verification 来改善 perception，但 formal verification 的输入本身就依赖 perception。Proposal 没有充分讨论这个 bootstrapping 难题。

2. **FormalGeo solver 对 "不完整/含噪" 输入的鲁棒性**: FormalGeo 设计时假设输入是**完整、正确的 formal specification**。当输入是 VLM 的 noisy、potentially incomplete perception 时，solver 能否有意义地进行 constraint propagation，还是会直接 crash / 给出 trivial "everything inconsistent" 结果？

3. **Per-fact diagnostic reward 在 GRPO 中的可用性**: GRPO 通常需要 scalar reward for a complete trajectory。将 per-fact diagnosis 转化为有效的 GRPO reward 需要 reward aggregation 设计。Proposal 假设 "dense per-fact rewards" 可以直接使用，但实际的 reward shaping 是非 trivial 的。

4. **DDAR 从 proof steps 到 perception checking 的适配**: DDAR 设计用于从已知几何条件推导新定理/证明步骤。将其用于"检查一组 perceived facts 的内部一致性"是一个不同的使用模式。这个适配是否 straightforward，proposal 没有讨论。

【3 维度打分】:

1. Novelty: 中 — 
   理由：Proposal 正确识别了一个真实的 gap：formal verification 已用于 reasoning stage (SGVR, InternGeometry)，perception rewards 已存在但依赖 learned judges (GeoDPO, Perception-R1) 或 rule-based metrics (SymHPR)，两者的交汇点确实空白。然而，这本质上是一个 **"A 用于 X，B 用于 Y → 把 A 用于 Y" 的组合式创新**。给定 SGVR 已经展示 formal verification 在 geometric RL 中有效，GeoDPO 已经展示 perception-stage RL rewards 有效，将两者结合是一个自然的、可预期的下一步，而非反直觉的洞察。Per-fact diagnostic reward 和 targeted re-perception 是有意义的功能贡献，但概念层面的 novelty delta 有限。SymHPR 已经在做 hierarchical per-primitive reward for perception——虽然用的不是 formal deduction engine，但思路方向非常接近。

2. Significance: 中 — 
   理由：研究问题本身重要——geometric perception bottleneck 确实是该领域的核心瓶颈（SVE-Math 的 70% 错误率、CogFlow 的 ICLR 2026 接收都印证了问题的重要性）。如果 formal verification 确实能在 perception stage 提供比 learned judges 更好的 reward signal，这将是一个有价值的贡献。但 significance 受限于两点：(a) 适用范围局限于有 formal specification 的几何问题（FormalGeo7K 仅 ~7K 问题），难以推广到更广泛的视觉数学推理；(b) 如果改进主要来自 reward signal quality 的边际提升（而非 paradigm shift），实际影响力有限。

3. Related Work: 强 — 
   理由：Related work coverage 非常全面且准确。对 GeoDPO、Perception-R1、SGVR、SymHPR、EVPV、FoVer、InternGeometry、CogFlow、GeoSketch 等近期工作的描述与我调研结果一致。每篇工作的差异化定位清晰（是 learned vs. formal，是 perception vs. reasoning），convincingly 展示了 gap 的存在。对 SymHPR 的区分（rule-based F1 vs. formal deduction）尤其准确。这是 proposal 最强的维度。

【概率估计】: [23% - 33%] 中位 28%

【估计理由】: 
Related Work 维度强，表明作者对领域有深刻理解且 gap 确实存在。但 Novelty 是中等——核心创新是组合式的（把 formal verification 从 reasoning stage 搬到 perception stage），缺乏反直觉的洞察；如果结果 positive，审稿人更可能说 "makes sense, expected this would help" 而非 "surprising"。Significance 也是中等——problem 重要但 contribution 的推广性受限于 formal geometry 的 domain scope。**上界主要被 Novelty 限制**：在 AAAI 审稿人看来，"obvious bridge" 类的组合创新通常需要非常强的实验结果来弥补概念新颖性的不足，而目前只是 proposal 阶段无法保证实验强度。另外，前提假设中 perception-to-formal translator 的 bootstrapping 问题若在 rebuttal 中被审稿人抓住，会很难回应。

【主要风险】:
1. **"Obvious bridge" 质疑**: 审稿人很可能指出这是 SGVR (formal verification for reasoning) + GeoDPO (perception-stage RL rewards) 的自然组合，要求更强的 conceptual contribution 或 surprising findings。
2. **Bootstrapping 循环论证**: Formal verification 依赖 VLM 准确输出 formal language，而 VLM 的准确性正是要通过 formal verification reward 来提升的——这个循环依赖在 proposal 中未被充分论证，审稿人可能视之为 fundamental flaw。
```

Sources:
- [GeoDPO - arXiv 2602.22703](https://arxiv.org/abs/2602.22703)
- [Perception-R1 - arXiv 2506.07218](https://arxiv.org/abs/2506.07218)
- [SGVR - arXiv 2601.05073](https://arxiv.org/abs/2601.05073)
- [SymHPR - arXiv 2512.03126](https://arxiv.org/abs/2512.03126)
- [EVPV - arXiv 2603.16253](https://arxiv.org/abs/2603.16253)
- [FoVer - arXiv 2505.15960](https://arxiv.org/abs/2505.15960)
- [InternGeometry - arXiv 2512.10534](https://arxiv.org/abs/2512.10534)
- [CogFlow - arXiv 2601.01874](https://arxiv.org/abs/2601.01874)
- [FormalGeo - arXiv 2310.18021](https://arxiv.org/abs/2310.18021)
- [AlphaGeometry2 - arXiv 2502.03544](https://arxiv.org/abs/2502.03544)
- [FormalGeo Project Site](https://formalgeo.github.io/)
- [AlphaGeometry2 GitHub (DDAR)](https://github.com/google-deepmind/alphageometry2)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
I now have comprehensive research results. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. [GeoDPO] "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning" (arXiv:2602.22703, Feb 2026):
   最直接的竞争工作。使用 learned NL-to-DSL translator 计算 DSL-level scores 作为 RL 奖励，在 in-domain perception +26.5%，downstream reasoning +39%。核心差异：GeoDPO 用 learned translator，本 proposal 用 formal solver。但 GeoDPO 已经证明 structured perception reward 在这个任务上有效，因此 FPR 需要证明 formal verification 相比 learned translator 的 marginal gain。

2. [Perception-R1] "Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward" (arXiv:2506.07218, 2025):
   用 LLM judge 评估 visual perception 一致性作为 reward，仅 1,442 样本即达 SOTA。证明 perception reward 的有效性，但 judge 无 formal grounding。本 proposal 正确识别了这个局限。

3. [SGVR/GeoGoal] "Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward" (arXiv:2601.05073, Jan 2026):
   用 formal verification data engine 生成 sub-goal rewards，geometric reasoning +9.7%。但仅用于 reasoning stage，不涉及 perception。FPR 的核心 novelty claim（将 formal verification 从 reasoning 延伸到 perception）依赖于与 SGVR 的对比。

4. [SymHPR] "Hierarchical Process Reward Models are Symbolic Vision Learners" (arXiv:2512.03126, Dec 2025):
   最接近的 concurrent work。用 symbolic auto-encoder 做 hierarchical per-primitive rewards（point-on-line, line-on-shape consistency），perception +13%。但用 rule-based F1/L2 metric 而非 formal deduction engine。FPR 声称能检测 semantic geometric contradictions 是超越 SymHPR 的点。

5. [EVPV] "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models" (arXiv:2603.16253, Mar 2026):
   分离 visual grounding errors 和 reasoning errors，用 constraint matching 计算 reliability-gating signal。方向高度相关但使用 constraint matching 而非 formal geometric verification。

6. ⚠️ [Bad Seeing or Bad Thinking?] (arXiv:2605.14054, May 2026) — **proposal 未引用**:
   刚发表 2 周。直接分解 perception vs. reasoning credit assignment，用 RL 框架显式 reward perception fidelity。核心问题与 FPR 高度重叠，虽不使用 formal verification，但直接瞄准同一个 gap。

7. ⚠️ [PDCR] "Perception-Decomposed Confidence Reward" (arXiv:2605.13467, May 2026) — **proposal 未引用**:
   分解 perception 和 reasoning 的 reward signal，解决 mixture-induced signal degradation 问题。另一个 May 2026 的直接竞争者。

8. ⚠️ [From Seeing to Thinking] (arXiv:2605.20177, May 2026) — **proposal 未引用**:
   系统研究 perception 和 reasoning 在 post-training 中的 interplay，发现 visual perception is more effectively learned via RL than caption-based SFT，且需要 staged training。直接支持 perception-stage RL 的价值，但不使用 formal verification。

9. [FoVer] (arXiv:2505.15960, ACL 2026 Findings):
   用 Z3/Isabelle 合成 PRM 训练数据，展示 formal verification → PRM 的 cross-task generalization。证明 formal verification tools 可以用于 reward/verification，但未应用到 geometric perception。

10. [InternGeometry] (arXiv:2512.10534, Dec 2025):
    使用 DDAR-class engine (Newclid) 在 RL loop 中做 geometry reasoning/proof，但仅用于 reasoning steps，不涉及 perception。

- **调研总结**: 2025-2026 年 geometric perception + RL 领域极其活跃。"Perception-stage reward" 是明确的研究热点，多篇 May 2026 论文同时瞄准 perception-reasoning credit decomposition。Formal verification 用于 reasoning-stage reward 已被 SGVR、FoVer、InternGeometry 等充分验证。但 formal verification 用于 **perception-stage** reward 确实是一个未被填补的空白。FPR 处于两个已有方向（formal verification for reasoning + RL reward for perception）的交叉点——novelty 来自组合，而非全新 paradigm。

【Trivial Alternative 检验】:

存在实质性的 trivial alternative 威胁：

1. **GeoDPO 的 learned translator 已经能够提供 structured perception reward** 且达到了 +26.5% 的 in-domain 增益。FPR 用 formal solver 替换 learned translator 作为 judge，但 learned translator 本身更灵活、更容易部署、且不需要 FormalGeo format 的严格输出。FPR 需要论证 formal verification 相比 learned DSL scoring 的 marginal gain 值得额外的系统复杂度。

2. **Perception-R1 用简单的 LLM judge 仅用 1,442 样本即达 SOTA**。这说明 perception reward 的有效性可能更多取决于 reward signal 的 existence 而非 reward signal 的 formal rigor。如果一个 $0 成本的 LLM judge 就能工作，投入大量工程去集成 FormalGeo + DDAR 的增量价值需要强有力的论证。

3. **FPR 的真正增量价值**在于 diagnostic capability（per-fact contradiction detection → targeted re-perception）。这是 learned judges 无法提供的。如果实验设计能突出这一点（不仅仅是 overall accuracy，而是 diagnostic precision、re-perception 效率），增量价值可以成立。但如果最终评估只看 accuracy on GeoQA/Geometry3K，这个增量可能不显著。

**结论**：存在 trivial alternative 威胁，但 diagnostic capability 是可辩护的增量价值点——前提是实验设计能充分展示它。

【前提假设检验】:

核心 claim 的逻辑链中有 **三个关键未验证假设**：

1. **⚠️ 最关键：Internal consistency ≠ Perception correctness**。FPR 的 formal solver 执行 constraint propagation 检查 extracted facts 的内部一致性。但一组 geometrically self-consistent 的 facts 不意味着它们 match 实际 diagram。例如：VLM 将一个三角形的所有角系统性地误差 10°，但新的角度值恰好满足内部约束（三角形角和 = 180°），formal checker 不会报错。Proposal 暗示 formal verification = perception verification，但实际上 formal solver 只能检测 **self-contradictions**，不能检测 **与 ground truth diagram 的偏差**。这是一个根本性的逻辑缺口。

   - 缓解因素：(a) 多数 perception errors 确实会产生内部矛盾（不太可能所有 errors 恰好 self-consistent）；(b) FormalGeo7K 有 ground truth formal annotations，可以作为 reference 进行比较。但如果使用 ground truth comparison，那本质上就是 structured matching（与 GeoDPO 类似），"formal verification" 的 claim 就变弱了。

2. **Perception-to-formal translation bottleneck 的 chicken-and-egg 问题**。FPR 要求 VLM 输出 FormalGeo Geometric Construction Language 格式的 structured facts。但能可靠输出这种格式的 VLM 已经在很大程度上"解决"了 perception 问题。如果 VLM 的 formal output 本身就充满错误，formal checker 收到的是 noisy input，其 diagnostic signal 的可靠性大打折扣。Proposal 没有讨论这个 bootstrapping 问题——第一轮训练时 VLM 的 formal output 质量如何？

3. **DDAR/FormalGeo 的 coverage 和 latency 假设**。Proposal 提到 FormalGeo constraint checking throughput ~50 problems/sec on CPU，但 RL 训练中每个 step 都需要 reward computation。GRPO 的 batch size 通常需要 thousands of reward evaluations per step。50 problems/sec 在 RL loop 中是否足够快？Proposal 提到可能需要 "batched verification or C++ DDAR backend"，但这本身是一个非平凡的工程假设。

【3 维度打分】:

1. **Novelty: 中** — 
   FPR 处于两个已有方向的交叉点：formal verification for reasoning（SGVR, FoVer, InternGeometry 已充分验证）和 RL reward for perception（GeoDPO, Perception-R1, SymHPR, EVPV 等已大量探索）。将 formal deduction engine 应用到 perception stage 确实是未被填补的组合空白，proposal 对此的识别是准确的。Diagnostic capability（per-fact contradiction detection → targeted re-perception）是一个有意义的 novelty contribution。
   
   但这本质上是一个 **组合创新**（combination novelty）而非 **范式创新**：把 A（已有）用到 B（已有但 A 没用过的场景）。审稿人对组合创新的标准会更高——需要论证为什么这个组合非平凡、为什么简单的 learned approach 不够。此外，May 2026 三篇未引用的论文（"Bad Seeing or Bad Thinking?", PDCR, "From Seeing to Thinking"）表明 perception-stage reward 的研究空间正在快速被填充，虽然它们不使用 formal verification，但进一步削弱了 novelty perception。

2. **Significance: 中** — 
   研究问题（geometric perception bottleneck）是 well-documented 且重要的（SVE-Math 的 70% error rate）。"From Seeing to Thinking" 进一步确认 perception 需要 specialized RL training。但 FPR 的 approach 是 **domain-specific to geometry**——formal geometric constraint checking 无法推广到一般的 visual perception tasks（如 chart understanding, scene description, spatial reasoning）。这限制了 significance 的 scope。与 Perception-R1（general visual perception reward）和 PDCR（general perception-reasoning decomposition）相比，FPR 的适用范围窄得多。
   
   此外，核心发现如果 positive——"formal geometric constraints as rewards improve geometric perception"——审稿人可能的反应是 "this makes sense"（logical extension）而非 "surprising"。把 formal verification（在 reasoning 上已被证明有效）用到 perception（另一个 stage），结果确实有效，这不是一个反直觉的发现。

3. **Related Work: 中偏强** — 
   Proposal 对 2025-early 2026 的 landscape 覆盖较好：GeoDPO, Perception-R1, SGVR, SymHPR, EVPV, FoVer, InternGeometry, GeoSketch 等核心工作均被引用，差异化定位清晰（每个 prior work 做了什么、缺什么）。ACL 2026 survey 也被引用。
   
   但存在 **显著的 coverage gap**：May 2026 三篇高度相关的论文未被覆盖——"Bad Seeing or Bad Thinking?" (2605.14054), PDCR (2605.13467), "From Seeing to Thinking" (2605.20177)。这些论文直接瞄准 perception-reasoning credit decomposition，是最近且最直接的竞争者。此外，Vision-SR1 (2508.19652) 和 PEARL (2511.18437) 也未被提及。考虑到这些是 May 2026 的论文，submission 之前应该能发现。GCA (2511.22659, Geometrically-Constrained Agent) 使用 VLM 翻译查询为 formal constraints 的 paradigm 也高度相关但未引用。

【概率估计】: [20% - 30%] 中位 24%

【估计理由】: 
Idea 的核心是一个 **组合创新**——将已被验证的 formal verification 从 reasoning stage 延伸到 perception stage。这个组合空白确实存在（调研确认无直接竞争者做到了这一点），但它更多是一个 "natural next step" 而非 "surprising insight"。三个维度中，Novelty 受限于组合性质（非范式级创新），Significance 受限于 geometry-specific scope 和 "I would have guessed this" 的预期性。最严重的 idea 层面问题是 **internal consistency ≠ perception correctness 的逻辑缺口**——这不是实验能补救的，它质疑 formal verification 作为 perception reward 的 fundamental validity。如果这个缺口在 rebuttal 中被审稿人追问，defense 难度较大。上界被 novelty 和 significance 的双重 "中" 评级限制在 ~30%；下界被 "gap 确实存在 + diagnostic capability 有价值" 支撑在 ~20%。

【主要风险】:
1. **Internal consistency ≠ perception correctness 的逻辑缺口**: 审稿人会追问 "formal solver 只能检测自相矛盾，无法检测与 ground truth diagram 的偏差——你们的 reward 到底在 reward 什么？" 如果 reward 本质上退化为 ground truth matching，那和 GeoDPO 的 structured scoring 差异不大，novelty claim 会坍塌。
2. **Trivial alternative 威胁**: Perception-R1 用简单 LLM judge + 1,442 样本即达 SOTA，GeoDPO 用 learned translator 达 +26.5%。审稿人会问 "为什么需要 FormalGeo + DDAR 的重型 infrastructure？marginal gain 是否值得？" 如果 FPR 的最终数字只和这些方法 comparable 或 marginally better，story 很难成立。
```

Sources:
- [GeoDPO - arXiv:2602.22703](https://arxiv.org/abs/2602.22703)
- [Perception-R1 - arXiv:2506.07218](https://arxiv.org/abs/2506.07218)
- [SGVR - arXiv:2601.05073](https://arxiv.org/abs/2601.05073)
- [SymHPR - arXiv:2512.03126](https://arxiv.org/abs/2512.03126)
- [EVPV - arXiv:2603.16253](https://arxiv.org/abs/2603.16253)
- [FormalGeo - arXiv:2310.18021](https://arxiv.org/abs/2310.18021)
- [FoVer - arXiv:2505.15960](https://arxiv.org/abs/2505.15960)
- [InternGeometry - arXiv:2512.10534](https://arxiv.org/abs/2512.10534)
- [Bad Seeing or Bad Thinking? - arXiv:2605.14054](https://arxiv.org/abs/2605.14054)
- [PDCR - arXiv:2605.13467](https://arxiv.org/abs/2605.13467)
- [From Seeing to Thinking - arXiv:2605.20177](https://arxiv.org/abs/2605.20177)
- [AlphaGeometry2 GitHub](https://github.com/google-deepmind/alphageometry2)


【原始 proposal（允许参考但不是主要依据）】:
# Formal Geometric Constraints as Verifiable Perception Rewards

## Core Problem

How can we provide formally verifiable, diagnostic reward signals for the visual perception stage of multimodal geometric reasoning, moving beyond learned neural judges that can be gamed or miss subtle geometric inconsistencies?

## Research Opportunity

Current RL approaches for visual math perception (GeoDPO, Perception-R1, PRCO) all rely on learned judges — either DSL-score translators or LLM consistency checkers — which lack formal guarantees and cannot diagnose WHICH specific perception is wrong. Meanwhile, formal verification methods (Safe/Lean 4, SGVR/GeoGoal) have proven powerful but remain confined to text-based reasoning steps, never applied to the perception stage. AlphaGeometry2's DDAR engine and FormalGeo7K now make it feasible to perform symbolic geometric constraint checking at scale, providing a bridge that didn't previously exist.

## Research Landscape

The perception bottleneck in visual geometric reasoning is well-documented: GPT-4o exhibits a 70% error rate on geometric primitive grounding (SVE-Math, arXiv:2501.06430). GeoDPO (arXiv:2602.22703) uses a learned NL-to-DSL translator to compute DSL-level reward scores for RL training, achieving +26.5% on in-domain geometric perception, but the translator itself can hallucinate scores. Perception-R1 (arXiv:2506.07218) uses a judge LLM for visual perception rewards achieving SOTA with minimal data, but the neural judge lacks formal grounding. SGVR (arXiv:2601.05073) uses a formal verification engine to generate sub-goal rewards for geometric reasoning (+9.7%), but only for downstream reasoning steps, not perception. GeoSketch (arXiv:2509.22460) implements auto-correction by comparing generated-vs-original diagrams via MLLM, but acknowledges it 'does not assess the correctness or validity of intermediate steps.' SymHPR (arXiv:2512.03126) is the closest concurrent work targeting perception-stage structured rewards: it uses a symbolic auto-encoder with hierarchical per-primitive rewards (point-on-line, line-on-shape consistency) achieving 98.2% MSE reduction in diagram reconstruction, but employs rule-based F1/L2 metric comparison rather than a formal deduction engine or constraint propagation — it cannot detect semantic geometric contradictions (e.g., an angle value inconsistent with a circle theorem). EVPV (arXiv:2603.16253) separates visual grounding errors from reasoning errors in process reward models by extracting structured visual constraints and computing a reliability-gating signal, but uses constraint matching rather than formal geometric verification. InternGeometry (arXiv:2512.10534) uses a DDAR-class symbolic engine in an RL loop for geometry but only for reasoning/proof steps, not visual perception. FoVer (arXiv:2505.15960, ACL 2026 Findings) demonstrates that formal verification tools (Z3, Isabelle) can synthesize step-level PRM training data with cross-task generalization, but has not been applied to geometric perception. The ACL 2026 geometry survey (arXiv:2507.11936) identifies 'formal language representations' and automated verification as critical open challenges. No existing work bridges formal geometric deduction engines to perception-stage RL rewards — the key novel contribution would be using symbolic constraint propagation not just to score but to DIAGNOSE specific perception errors (e.g., 'angle ABC=90° contradicts A being on circle with diameter BC'), enabling targeted re-perception at test time and dense per-fact reward signals at training time.

## Proposed Approach

We propose FormalPerceptReward (FPR), which constructs a formally verifiable reward pipeline for visual geometric perception by coupling a perception-to-formal translator with FormalGeo's symbolic solver and AlphaGeometry2's DDAR engine. A VLM (Qwen3-VL-8B, currently the strongest open-source VLM at its scale with 85.8% MathVista for the 235B variant) is prompted to output structured geometric facts from a diagram in FormalGeo's Geometric Construction Language; the symbolic solver then performs constraint propagation to check internal consistency, flagging specific contradictions (e.g., 'perceived angle ABC=90 degrees is inconsistent with A lying on circle with diameter BC') as per-fact diagnostic signals. These dense formal-verification rewards replace learned neural judges in GRPO training on FormalGeo7K's ~7K annotated problems augmented with Geometry3K diagrams, following the lightweight training paradigm demonstrated by Perception-R1 (SOTA from only 1,442 samples on 16x A800 GPUs). At test time, the diagnostic feedback loop enables targeted re-perception: the model re-examines only the specific geometric facts flagged as inconsistent, rather than re-processing the entire diagram, analogous to how SGVR's skeleton-rate metric provides sub-goal granularity but now applied at the perception stage.

## Detailed Description

We introduce FormalPerceptReward (FPR), the first framework to apply formal geometric deduction engines as verifiable reward signals for the visual perception stage of multimodal geometric reasoning. While existing RL approaches for geometric perception rely on learned neural judges — GeoDPO's DSL translator, Perception-R1's LLM judge, SymHPR's rule-based F1 metrics — that lack formal guarantees, and formal verification methods (SGVR, Safe, FoVer) remain confined to downstream reasoning steps, FPR bridges this gap. Given a VLM's extracted geometric facts from a diagram, FormalGeo's symbolic solver and AlphaGeometry2's DDAR engine perform constraint propagation to identify specific contradictions, producing per-fact diagnostic reward signals. These dense, formally-grounded rewards enable GRPO training on FormalGeo7K (~7K annotated problems) with Qwen3-VL-8B as the base model, replacing opaque neural judges with transparent symbolic verification. At test time, diagnostic feedback enables targeted re-perception of specific erroneous facts rather than full-diagram re-processing. Concurrent work search (May 2026) confirms no existing paper combines formal deduction engines with perception-stage RL rewards. We target improvements over GeoDPO's +26.5% in-domain perception gain and SGVR's +9.7% reasoning gain, evaluating on GeoQA, Geometry3K, and PGPS9K benchmarks.

## Key References

- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026, 2602.22703)
- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025, 2506.07218)
- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (arXiv 2026, 2601.05073)
- Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs [SVE-Math] (arXiv 2025, 2501.06430)
- Solving Olympiad Geometry without Human Demonstrations [AlphaGeometry] (Nature 2024)
- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (Symmetry 2024, arXiv 2310.18021)
- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026, arXiv 2601.01874)
- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025, 2512.03126)
- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026, 2603.16253)
- Efficient PRM Training Data Synthesis via Formal Verification [FoVer] (ACL 2026 Findings, arXiv 2505.15960)
- GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning with Auxiliary Line Construction and Affine Transformation (arXiv 2025, 2509.22460)
- A Survey of Deep Learning for Geometry Problem Solving (ACL 2026 Main, arXiv 2507.11936)
- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (arXiv 2025, 2506.04592)

## Resource Estimate

- **manual**: gpu_hours: 2500–3000 (16x A800-80G: ~6 GRPO training runs × 20h each + ablations + evaluation), timeline: 5 months (M1: perception-to-formal translator + FormalGeo/DDAR integration; M2–3: GRPO training experiments + reward design iteration; M4: comprehensive evaluation + ablations on GeoQA/Geometry3K/PGPS9K; M5: paper writing), estimated_gpu_cost: $5,000–6,000 (at ~$2/GPU-hr for A800 cloud instances)
- **human_in_loop**: gpu_hours: 2000–2500 (Claude accelerates translator code + reward shaping, fewer wasted runs), timeline: 3.5–4 months (M1: pipeline + initial experiments with Claude-assisted code generation; M2–3: GRPO training + hyperparameter search; M3.5–4: evaluation + paper drafting), claude_api_cost: $300–500 (code generation for FormalGeo integration, reward function design, experiment analysis, paper drafting), estimated_gpu_cost: $4,000–5,000
- **auto_research**: gpu_hours: 3000–4000 (more exploratory runs for reward variants, automated ablations), timeline: 2.5–3 months (parallel experiment scheduling, automated evaluation pipelines), claude_api_cost: $1,200–2,000 (extensive code generation, automated experiment orchestration, result analysis, full paper writing), estimated_gpu_cost: $6,000–8,000, speed_bottleneck: RL training wall-clock time: each GRPO run takes ~16–20 hours on 16x A800 GPUs regardless of automation; FormalGeo constraint checking throughput (~50 problems/sec on CPU) may require batched verification or C++ DDAR backend for RL-loop latency


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bb509db1-1f87-4c50-9dfe-ff663a262831",
  "type": "user",
  "uuid": "c1b5891a-26bf-46ff-878b-1c7903c1ef1f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:17:37.008Z_

```json
{
  "parentUuid": "c1b5891a-26bf-46ff-878b-1c7903c1ef1f",
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
  "uuid": "9cd3c605-d964-472d-babe-52fe2d465b08",
  "timestamp": "2026-05-27T08:17:37.008Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:17:37.008Z_

```json
{
  "parentUuid": "9cd3c605-d964-472d-babe-52fe2d465b08",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e233d9d2-c39d-4956-a994-17d392c0010a",
  "timestamp": "2026-05-27T08:17:37.008Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to provide a thorough evaluatio…",
  "leafUuid": "e233d9d2-c39d-4956-a994-17d392c0010a",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate formal geometric verification for perception rewards",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:18:17.437Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews of this proposal and synthesize them as the Meta Judge.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 中偏强
- Probability: [22% - 33%] 中位 27%

**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [23% - 33%] 中位 28%


**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 中偏强
- Probability: [20% - 30%] 中位 24%

Now I'm calculating the aggregate statistics across all three reviewers. The median probabilities are 27%, 28%, and 24%, which gives me a mean of 26.3% and a median of 27%. I'm also computing the standard deviation to understand the spread in their assessments.

The standard deviation comes out to roughly 1.7%, which indicates very high consistency across reviewers—well below the 3% threshold. Looking at where they align, there's strong consensus that the novelty is incremental rather than paradigm-shifting, the significance is limited by its geometry-specific scope, and there's a genuine gap in formal verification for perception-stage rewards. All three also flag the same core vulnerability: simpler alternatives like direct matching or learned judges could potentially achieve similar results. There's also agreement on the bootstrapping problem—how to ensure the perception model accurately translates to formal specifications—and that internal consistency doesn't guarantee the model actually captures what we care about.

The reviewers converge on the crowded landscape of perception reward work and characterize this as a natural but somewhat obvious next step. They also note that recent papers from May 2026 aren't covered, though R3 emphasizes this more strongly. Related work is generally solid across the board, though R2 rates it slightly higher than the others. The outliers are R3's notably lower acceptance probability, which hinges on treating the consistency-versus-correctness gap as more fundamental, and R1's specific call-out of a missing GeoPQA reference that the others don't mention.

Looking at the implementation side, the proposal outlines concrete resource requirements—around 2500-3000 GPU hours on 16 A800s, with FormalGeo's constraint checking running at roughly 50 problems per second on CPU. The timeline stretches across 3.5 to 5 months depending on the approach chosen, and R3 flags potential latency issues with DDAR in the reinforcement learning loop. Now I need to synthesize these reviewer assessments into a Meta Judge output, keeping in mind that the standard deviation of about 1.7% indicates high consistency, so I should anchor near the median and tighten the range.

The three ranges cluster tightly—R1 at 22-33%, R2 at 23-33%, R3 at 20-30%—with medians hovering around 24-28%. Given this strong agreement, I'll narrow toward the center around 26%, settling on [21%-30%] as the final interval.

This reflects the clear consensus: a combination innovation with real but limited novelty and scope. R3's critique about internal consistency not guaranteeing correctness resonates with R1's concerns too, so I'm adjusting slightly downward to account for that shared skepticism.

Now for the recommendation: with a median of 26%, this falls below the 36% threshold, putting it in "不推荐" territory. All three reviewers flagged fundamental issues—the trivial alternative, the combination nature, the bootstrapping problem—so the median being firmly in the 20s points toward rejection rather than borderline. The idea isn't fatally flawed, but it needs substantial strengthening to meet the bar. I'll recommend "不推荐" with concrete guidance on what would need to change.

For the implementation assessment, I'm looking at the computational requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e233d9d2-c39d-4956-a994-17d392c0010a",
  "isSidechain": false,
  "requestId": "req_011CbSk6kHECC44ffy8EWFUT",
  "type": "assistant",
  "uuid": "0cc2e9e8-cbf9-4e82-8508-b0ddb5948b80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeBHaFpxLBq4admKkipWKT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21941,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21941,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3457,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21941
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

_source line 9 · 2026-05-27T08:18:53.418Z_

【阶段】: Meta Judge
【三次中位】: [27%, 28%, 24%]  std=1.7%
【共识维度】:
- **Novelty = 中**（3/3 一致）：组合式创新（formal verification from reasoning + perception-stage rewards），"natural next step" / "obvious bridge"，非范式级突破
- **Significance = 中**（3/3 一致）：问题重要但 scope 局限于几何领域，推广路径不清晰；结果即使 positive 也属 "expected" 而非 "surprising"
- **Related Work = 中偏强至强**（3/3 方向一致）：核心文献覆盖全面，差异化定位清晰，但 May 2026 并发论文群有缺漏
- **Trivial Alternative 威胁**（3/3 一致）：simple per-fact matching / learned translator / LLM judge 已能提供 perception reward，formal verification 的增量价值待证
- **Bootstrapping 问题**（2/3：R2、R3 深入分析）：perception-to-formal translation 质量依赖 VLM 感知能力，而后者正是要被训练的对象——循环依赖
- **Internal consistency ≠ perception correctness**（2/3：R1 提及、R3 作为核心论点）：formal solver 只检测自相矛盾，无法检测"一致但全错"的 perception
- **赛道拥挤**（3/3 一致）：2025-2026 至少 10+ 篇 perception reward 论文，novelty 空间被持续压缩
- **Gap 确实存在**（3/3 一致）：formal deduction engine 用于 perception-stage rewards 的交叉点确实未被占据

【异常维度】:
- R2 给 Related Work = 强（其余两位为中偏强）——略偏乐观，但方向一致，不构成实质分歧
- R1 单独指出 GeoPQA (EMNLP 2025) 缺引——合理补充，但非致命遗漏
- R3 给出最低中位 24%，主要源于将 "internal consistency ≠ correctness" 定位为 fundamental flaw——R1 也提及此点但未将其升级为致命级，属程度差异而非方向分歧

【最终概率】: [21% - 30%] 中位 26%
【一致性】: 高（std=1.7% < 3%）
【综合理由】:
三位审稿人在所有核心维度上达成高度一致：Novelty 中、Significance 中、Related Work 中偏强。概率中位集中在 24-28% 的窄带内（std 仅 1.7%），表明三方对这个 proposal 的判断非常收敛。

**概率上限受 Novelty 硬约束**：三位审稿人一致认为核心创新是组合式的——SGVR（formal verification for reasoning）+ GeoDPO/SymHPR（structured perception rewards）的自然交汇。在 2025-2026 perception reward 论文爆发期，这种 "obvious bridge" 很难被视为足够的 conceptual contribution。上界不超过 30%。

**概率下限由 gap 真实性支撑**：三位均确认 formal deduction engine 用于 perception-stage rewards 的空白确实存在，diagnostic capability（per-fact contradiction detection → targeted re-perception）是有意义的功能贡献。下界约 21%。

**处理异常**：R3 的 24% 偏低源于对 "internal consistency ≠ correctness" 的致命级定位。R1 也提及此点但给出 27%，表明多数审稿人认为这是一个 serious concern 但非 fundamental invalidation（因为多数 perception errors 确实会产生内部矛盾，且训练时有 ground truth 可参照）。最终中位 26% 在 R3 和 R1/R2 之间取折中，略偏严格。

**核心瓶颈诊断**：proposal 的天花板由 idea 质量（组合式 novelty + 中等 significance）决定，非实验设计可突破。即使实验做到最好（formal verification 大幅优于 trivial baselines），审稿人仍可能认为 conceptual depth 不足。这是 AAAI 顶会对组合创新的结构性挑战。

【建议】: 边缘偏下 / 不推荐（中位 26% < 36% 阈值；idea 层面天花板有限，但方向非致命，存在提升空间）
【实施评估】:
  - 计算资源: 16× A800-80G GPU，2500-3000 GPU 小时（6+ 次 GRPO 训练 × 16-20h/次 + 消融 + 评估），预估 GPU 云成本 $5,000-6,000
  - 数据需求: FormalGeo7K（~7K 标注几何题）、Geometry3K、GeoQA、PGPS9K——均为公开数据集，无需额外采集
  - 人工介入: FormalGeo/DDAR 集成工程开发（非平凡）、reward shaping 设计与调参、perception-to-formal translator 的 prompt 工程；无需人工标注
  - 训练需求: 需要模型训练——Qwen3-VL-8B 基座模型的 GRPO 强化学习训练，每次训练 16-20h on 16× A800
  - 新 Benchmark: 不需要（使用现有 benchmark）
  - 预估周期: 3.5-5 个月（M1: perception-to-formal translator + FormalGeo/DDAR 集成；M2-3: GRPO 训练实验；M4: 评估与消融；M5: 论文撰写）。关键瓶颈：FormalGeo 约束检查吞吐量（~50 problems/sec on CPU）在 RL loop 中可能不足，需 C++ DDAR 后端或批处理验证方案

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc2e9e8-cbf9-4e82-8508-b0ddb5948b80",
  "isSidechain": false,
  "requestId": "req_011CbSk6kHECC44ffy8EWFUT",
  "type": "assistant",
  "uuid": "477d88d9-bc57-4c67-a36e-f209220c17b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeBHaFpxLBq4admKkipWKT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21941,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21941,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3457,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21941
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to provide a thorough evaluatio…",
  "leafUuid": "477d88d9-bc57-4c67-a36e-f209220c17b6",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate formal geometric verification for perception rewards",
  "sessionId": "6a2d2860-92a0-450a-8f98-c341ca3d3a32"
}
```

---
