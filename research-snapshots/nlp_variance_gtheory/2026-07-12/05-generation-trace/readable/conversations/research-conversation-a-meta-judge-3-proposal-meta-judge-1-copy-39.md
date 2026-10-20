# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/6031105c-bfba-4bc3-9066-7ca7e8d22711.jsonl`
- **Structured JSON:** [`0eed36776f04a9bf6e8e.json`](../../sessions/0e/0eed36776f04a9bf6e8e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T21:00:53.367Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T21:00:53.367Z",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a thorough assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- FoVer (arXiv 2505.15960, ACL 2026 Findings): 使用 Z3/Isabelle 进行形式化验证来合成 PRM 训练数据（FoVer-80K），一次性生成，非迭代，不追踪技能或多样性。验证了形式化工具可以为 math reasoning 提供可靠的 step-level 标签。\n- R-Diverse (arXiv 2602.13103, Feb 2026): 提出 Skill-Aware Measurement (SAM)，用 LLM 生成的 solver 程序和代码嵌入来衡量技能多样性，解决 self-play 训练中的\"多样性幻觉\"（Local + Surface Diversity Illusion）。在 10 个 benchmark 上持续优于 prior self-play 方法。技能衡量基于 LLM 嵌入，非形式化验证。\n- NSRSA (arXiv 2603.21558, Mar 2026): 将 SymPy 验证集成到迭代 self-training 中，过滤约 34% 答案正确但推理有缺陷的解（\"lucky guesses\"）。关注验证过滤，不做技能提取或多样性度量。在 Qwen3-4B 上验证，规模较小。\n- Noisy Data is Destructive (arXiv 2603.16140, Mar 2026, Zhu & Kang): 证明 RLVR 中 8-10% 的标注噪声导致严重性能下降，现有 RLVR 算法（包括改进版 GRPO）无法补偿噪声。强调高质量数据的不可替代性。\n- Spurious Rewards Paradox (arXiv 2601.11061, Jan 2026): 用 Path Patching/Logit Lens 等方法发现 RLVR 中的 Anchor-Adapter circuit（中间层 L18-20 + 后层 L21+），即使随机/虚假奖励也能激活记忆捷径。这是 reward-level 的机制性发现，而非 curriculum-level 的问题。\n- Prism (arXiv 2603.13309, Mar 2026): 基于嵌入的语义分区 + ZPD 门控，防止 self-evolving 系统的 curriculum collapse。在 AMC 上比 R-Zero 高 +3.98。方法简单，无需形式化验证即实现强效果。\n- ARISE (arXiv 2603.16060, Mar 2026): 层级 RL 框架，从成功 trace 中用 LLM 摘要生成技能库，集成到 GRPO 训练中。在 OlympiadBench 上持续优于 GRPO-family baseline。技能基于 LLM 摘要，无形式化保证。\n- PSV-Verus (arXiv 2512.18160, Dec 2025): 形式化验证驱动的 self-play 用于代码生成（Rust/Verus），pass@1 提升 9.6×。但在代码领域，非 math reasoning。\n- MATH-VF (arXiv 2505.20869, May 2025): 用 Z3+SymPy 进行 step-level 数学推理验证，在 MATH500 和 ProcessBench 上评估。Training-free 评估器，未集成到训练循环中。\n- RLVεR (arXiv 2601.04411, Jan 2026): 从理论角度建模 RLVR 中噪声奖励的影响，补充 Zhu & Kang 的实证发现。\n- 调研总结: 数学推理 self-improvement 在 2026 年上半年是高度活跃的研究方向，三条技术线索——形式化验证（FoVer/NSRSA/MATH-VF）、多样性度量（R-Diverse/Prism）、技能库演化（ARISE）——已各自独立成熟。本 proposal 位于这三条线的交汇点，填补了\"形式化验证 + 技能多样性 + 迭代训练\"的组合空缺。这个空缺是真实的，但也是显而易见的——任何同时阅读过 FoVer 和 R-Diverse 的研究者都会想到这个组合。\n\n【Trivial Alternative 检验】:\n存在多个成本更低的替代方案可能达到类似效果：\n\n1. **NSRSA + R-Diverse SAM 直接组合**: 在 NSRSA 的 SymPy 验证过滤基础上，直接叠加 R-Diverse 的 SAM 多样性指标进行 curriculum 选择。无需构建完整的形式化技能提取管线，即可同时获得\"验证过滤去噪\"和\"技能多样性选择\"两个好处。这个组合的工程成本远低于本 proposal，但可能达到 80-90% 的效果。\n\n2. **FoVer 验证 + Prism 嵌入多样性**: 用 FoVer 的形式化验证做 step-level 过滤（去噪），然后用 Prism 的嵌入语义分区做多样性选择。Prism 已经在 AMC 上展示了 +3.98 的提升，且不需要预定义技能分类体系。\n\n3. **ARISE 的 LLM 技能库 + SymPy 过滤**: ARISE 已经展示了 LLM 摘要技能库在 OlympiadBench 上优于 GRPO-family 的结果。在其基础上加入 SymPy 过滤即可获得验证保证。\n\n本 proposal 的增量价值在于：用形式化 AST 模式匹配提取的技能标签理论上比 LLM 嵌入或摘要更准确和无噪声。但这个增量价值有两个问题：(a) NL→formal 的翻译步骤本身会引入噪声，\"无噪声\"的承诺在实际执行中打折扣；(b) 多样性度量的噪声是否是绑定约束（binding constraint）？Zhu & Kang 的工作证明 reward 噪声是致命的，但 diversity metric 的噪声对最终性能的影响没有被独立验证过。\n\n【前提假设检验】:\n核心逻辑链中有以下未经验证的假设：\n\n1. **\"形式化技能标签是无噪声的\"（最关键）**: Proposal 声称通过 Z3/SymPy 验证 + AST 模式匹配可以获得\"provably-correct, noise-free skill labels\"。但这忽略了关键的前置步骤——将 LLM 生成的自然语言推理步骤翻译成 Z3/SymPy 形式化表达式。这个翻译步骤本身依赖 LLM（或规则系统），必然引入噪声和覆盖率问题。FoVer 和 MATH-VF 的论文中都有大量推理步骤无法被成功形式化的情况。\"noise-free\"只在 Z3/SymPy 验证环节成立，整个管线看下来并不是 noise-free 的。\n\n2. **\"技能空间覆盖可以同时防止课程崩塌、噪声积累和记忆捷径三种失败模式\"**: 这是 proposal 最核心的 claim，但逻辑链条在\"记忆捷径\"环节断裂。Spurious Rewards Paradox 论文明确表明，记忆捷径是在 reward 信号层面通过 Anchor-Adapter circuit 被激活的，这是一个模型内部机制问题，不是 curriculum 组成问题。更好的课程多样性可能缓解但无法\"防止\"记忆捷径——因为 GRPO 的 reward signal 结构并未被本 proposal 改变。\n\n3. **\"40-60 个预定义技能 + 确定性模式匹配可以覆盖竞赛数学空间\"**: 竞赛数学（AIME、OlympiadBench）的核心难度在于技能的创造性组合和跨领域迁移，而非单一技能的应用。预定义的 40-60 个技能分类体系 + 刚性模式匹配可能对标准 MATH 500 有效，但对竞赛级别问题的覆盖率是存疑的。\n\n4. **\"多样性度量的噪声是当前 self-improvement 的绑定约束\"**: Proposal 的立论基础是 R-Diverse 的 SAM 因为使用 LLM 嵌入而有噪声，而形式化方法可以消除这个噪声。但没有实证表明 SAM 的噪声是限制 self-improvement 性能的 bottleneck。可能其他因素（reward 设计、问题难度分布、训练动态）才是真正的瓶颈。\n\n【3 维度打分】:\n1. Novelty: 弱-中 — 核心贡献是将 FoVer/MATH-VF 的形式化验证、R-Diverse/ARISE 的技能多样性度量、GRPO-based 迭代训练三个已有组件组合在一起。每个组件都来自 2025-2026 年的近期工作，组合本身是设计空间中的一个显而易见的空位——任何同时阅读过 FoVer（ACL 2026）和 R-Diverse（Feb 2026）的研究者都会想到\"为什么不用形式化验证来替代 SAM 中的 LLM 嵌入？\"具体的技术贡献（AST 模式匹配提取技能标签、子模优化选择课程）是工程实现层面的，而非概念性创新。与 NSRSA（已经做了 SymPy + 迭代训练）和 ARISE（已经做了技能库 + RL 训练）相比，剩余的 novelty delta 较薄。如果 positive result 出来，审稿人更可能说\"this is a natural combination\"而非\"this is surprising\"。\n\n2. Significance: 中 — 研究问题本身（math self-improvement 的失败模式）是重要的，2026 年多篇高影响力论文都在研究这个方向。但本 proposal 的影响范围受限于：(a) 只适用于可形式化的数学领域，不推广到 general reasoning；(b) 依赖预定义技能分类体系，难以适应新出现的问题类型；(c) 如果形式化翻译覆盖率有限（如只覆盖代数和算术），那么 skill coverage 度量本身就是有偏的。相比之下，Prism 的嵌入方法和 ARISE 的 LLM 技能摘要虽然有噪声，但覆盖面更广、适应性更强。\n\n3. Related Work: 强 — Proposal 对 2025-2026 年的相关工作覆盖全面且准确。FoVer、R-Diverse、NSRSA、ARISE、Prism、PSV-Verus、MATH-VF、噪声/记忆化论文都被正确引用和定位。差异化定位（\"没有工作同时做形式化验证 + 技能多样性 + 迭代训练\"）是真实的。所有引用的论文经调研验证真实存在且描述准确。唯一的小缺陷是未引用 Prismatic Synthesis（关于嵌入多样性未必保证模型提升的反面证据）和 RLVεR（噪声奖励的理论分析）。\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】: \nRelated Work 维度是强的，说明作者对领域有深入理解，positioning 清晰。但 Novelty 是限制上界的核心维度——这是一个\"显而易见的组合\"型工作，将三个已有技术组件拼接在一起，审稿人很可能认为 incremental。Significance 受限于形式化方法的覆盖率和推广性问题。\n\n核心 claim \"形式化验证提供无噪声技能标签从而同时解决三种失败模式\"在逻辑上有断裂——特别是\"记忆捷径\"环节的因果链不成立（这是 reward-level 现象，不是 curriculum-level 现象），以及\"无噪声\"承诺被 NL→formal 翻译步骤所削弱。如果审稿人抓住这两点，paper 会在 soundness 和 novelty 上同时被质疑。\n\n22% 中位意味着：方向不致命，gap 是真实的，但 idea 内核偏薄，更像是工程贡献而非概念性突破。如果实验展示出显著优于 R-Diverse 和 NSRSA 的结果（> 3-5% on AIME），执行质量可以部分弥补 novelty 不足，将概率推到上界附近；但如果提升有限（1-2%），审稿人会认为不值得引入如此复杂的管线。\n\n【主要风险】: \n1. **\"显而易见的组合\"（Obvious Combination）**: 审稿人最可能的批评——FoVer + R-Diverse + GRPO 的三方组合是 design space 中的自然填充，缺乏 surprising insight。核心问题不是\"这个组合 work 不 work\"，而是\"你告诉了我们什么关于 formal verification 在 self-improvement 中作用的新知识？\"\n2. **\"无噪声\"承诺与实际管线矛盾**: NL→formal 翻译步骤的覆盖率和准确率是整个系统的瓶颈，但 proposal 对此几乎未做讨论。审稿人会追问：如果只有 50-60% 的推理步骤能被成功形式化，那 \"noise-free skill labels\" 的 claim 是否名不副实？这种 partial coverage 是否反而引入了新的 bias？\n```\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103)\n- [Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2603.16140)\n- [Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs](https://arxiv.org/abs/2601.11061)\n- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning](https://arxiv.org/abs/2603.16060)\n- [Prism: Preventing Curriculum Collapse in Self-Evolving Reasoning Systems](https://arxiv.org/pdf/2603.13309)\n- [PSV-Verus: Propose, Solve, Verify: Self-Play Through Formal Verification](https://arxiv.org/abs/2512.18160)\n- [MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving](https://arxiv.org/abs/2505.20869)\n- [Rate or Fate? RLVεR: Reinforcement Learning with Verifiable Noisy Rewards](https://arxiv.org/abs/2601.04411)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient context for a thorough evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. FoVer (arXiv 2505.15960, ACL 2026 Findings): 使用 Z3/Isabelle 对 formal reasoning tasks 进行 step-level 验证，生成 PRM 训练数据。关键局限：one-shot 生成，不追踪 skill，不参与迭代训练循环。Proposal 准确描述了其能力与局限。\n\n2. R-Diverse (arXiv 2602.13103, Feb 2026): 提出 Skill-Aware Measurement (SAM) 解决 self-play 中的 \"diversity illusion\"，使用 LLM-generated solver programs + code embeddings 衡量 skill 多样性。在 10 个 benchmark 上维持 5 轮迭代的持续增长。关键局限：SAM 依赖 LLM 生成的代码嵌入，本质上是有噪声的。Proposal 对此定位准确。\n\n3. \"Noisy Data is Destructive to RLVR\" (arXiv 2603.16140, Mar 2026): 严格证明了真正有噪声的标注在 RLVR 中导致 8-10% 的性能下降，且现有 RLVR 算法改进（包括 GRPO 变体）无法补偿噪声影响。这是 proposal 的核心动机之一，论文真实存在且描述准确。\n\n4. NSRSA (arXiv 2603.21558, Mar 2026): 在迭代 self-training 中集成 SymPy 进行 step-level 验证，过滤约 34% \"碰巧答对但推理有误\"的解。关键局限：只做了正确性过滤，没有 skill 追踪或多样性优化。这是 proposal 声称要超越的关键 baseline。\n\n5. ARISE (arXiv 2603.16060, Mar 2026): 层级 RL 框架，skill library 与 policy 共同进化。在 OlympiadBench 等 benchmark 上持续优于 GRPO 族方法。关键局限：skill 由 LLM 总结生成，无形式化保证。\n\n6. Prism / Preventing Curriculum Collapse (arXiv 2603.13309, Mar 2026): 使用 embedding-based semantic diversity 进行课程选择，在 AMC 上比 R-Zero 高 +3.98。关键局限：基于嵌入而非形式化方法，受限于 embedding 质量。\n\n7. MATH-VF (arXiv 2505.20869, May 2025): Z3+SymPy 的 step-level 验证器，在 MATH500 和 ProcessBench 上验证推理步骤。关键局限：one-shot evaluator，未集成到迭代训练中。\n\n8. Spurious Rewards Paradox (arXiv 2601.11061, Jan 2026): 用 Path Patching 和 Neural ODE 揭示了 RLVR 中的 Anchor-Adapter 记忆捷径电路（L18-20 层 Functional Anchor + L21+ 层 Structural Adapter）。论文真实存在，描述准确。\n\n9. PSV-Verus (arXiv 2512.18160, Dec 2025): 在代码生成领域实现 formal-verification-driven self-play，9.6x pass@1 提升，但不在 math reasoning 领域。\n\n- 调研总结: Math self-improvement 在 2026 上半年极其活跃，形式化验证（FoVer, NSRSA, MATH-VF）和多样性感知训练（R-Diverse, Prism, ARISE）各自发展成熟但尚未交叉融合。Proposal 准确定位在这个交叉空白点上——\"formally-verified skill extraction + iterative diversity-aware training\"确实没有直接竞争者，但各组件的成熟度意味着这一组合是自然可预见的下一步。\n\n\n【Trivial Alternative 检验】:\n\n存在两个成本更低的替代方案构成威胁：\n\n(1) **NSRSA + R-Diverse 的直接拼接**：用 NSRSA 的 SymPy 过滤保证步骤正确性，同时用 R-Diverse 的 SAM 进行 skill-aware 课程选择。这不需要构建新的 formal skill extractor，只需工程层面的集成。Proposal 的增量价值在于：SAM 的 skill 度量本身有噪声（基于 LLM code embeddings），而 VSC 的 skill labels 是确定性的、provably correct 的——但这个增量价值依赖于\"SAM 的噪声在实际训练中是否真正造成问题\"这个未经验证的假设。\n\n(2) **FoVer 验证 + 简单覆盖启发式**：用 FoVer 的验证管线保证正确性，加上对问题类型的简单分桶（如按数学子领域/难度）做覆盖，而不需要构建细粒度的 40-60 skill taxonomy。如果粗粒度覆盖已经足够防止 curriculum collapse，那么精细 skill taxonomy 的边际收益可能很小。\n\nProposal 的真正增量价值在于：(a) 将\"验证正确性\"和\"提取 skill labels\"统一在同一形式化管线中，减少系统复杂度；(b) 声称可以同时解决三个失败模式。但审稿人可能会质疑：三个失败模式中，noise sensitivity 主要被 formal verification 解决（NSRSA 已证明），curriculum collapse 主要被 diversity-aware selection 解决（R-Diverse/Prism 已证明），memorization shortcuts 的解决机制最不清楚——step-level skill verification 如何直接阻止 Anchor-Adapter 电路的激活？\n\n\n【前提假设检验】:\n\n核心逻辑链中存在以下未经验证的假设：\n\n1. **NL→Formal 翻译的可靠性假设**（最关键）：Proposal 假设可以将 LLM 生成的自然语言推理步骤可靠地翻译成 Z3/SymPy 形式化表达。FoVer 在 formal reasoning tasks 上工作良好，但 LLM 生成的 CoT 推理是非结构化的自然语言，翻译失败率可能很高。Proposal 承认这是 \"long-tail failure mode\"（在 Resource Estimate 中提及），但未量化或提出缓解方案。如果大量推理步骤无法被形式化，skill coverage 信号会系统性偏向可形式化的简单步骤，反而引入新的偏差。\n\n2. **Skill Taxonomy 充分性假设**：预定义 40-60 个 skill 的 taxonomy 假设了数学推理技能可以被离散化且穷举。但竞赛数学（AIME/OlympiadBench）常涉及 creative problem-solving（如构造辅助函数、类比推理），这些难以被预定义 taxonomy 覆盖。如果高难度问题的关键 skill 不在 taxonomy 中，skill coverage 会错误地认为这些问题\"没有新 skill 贡献\"。\n\n3. **Skill Coverage = Reasoning Diversity 假设**：Proposal 假设最大化 skill-space coverage 等同于最大化推理多样性。但同一 skill（如\"inequality chaining\"）可以有截然不同的难度和应用场景，仅追踪 skill 出现频率可能遗漏 skill 深度/组合复杂度这个维度。\n\n4. **Memorization抑制假设**（最弱）：Proposal 声称 step-level skill verification 可以阻止 memorization shortcuts，但 Spurious Rewards Paradox 论文揭示的 Anchor-Adapter 机制在 middle-to-late layers 中通过 reward signal 激活——这是一个训练动态问题，不是数据质量问题。即使训练数据经过完美的 skill 验证，如果 reward signal 本身存在 spurious patterns，Anchor-Adapter 电路仍然可能被激活。Proposal 在这一点上的论证链最弱。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — Proposal 的核心贡献是将已有的形式化验证（FoVer/MATH-VF 的 Z3+SymPy）与已有的 skill-aware diversity（R-Diverse 的 SAM 思路）进行组合，并放入已有的迭代训练框架（GRPO/verl）中。这是一个\"自然组合\"（natural combination）——任何同时读过 FoVer 和 R-Diverse 的研究者都可能想到\"用 formal verification 替代 LLM embeddings 来提取 skill labels\"。具体的技术细节（AST pattern matching → skill taxonomy, submodular coverage optimization）有一定工程创新但不构成概念性突破。与 NSRSA（已经做了 SymPy + iterative training）的差异主要在于加了 skill taxonomy 和 coverage objective——这是增量性的，而非范式性的。Prism 论文（Mar 2026）已经在做基于语义空间的 coverage 优化，VSC 本质上是将 embedding space 替换为 formal skill space——是信号来源的替换而非方法论的革新。\n\n2. **Significance: 中** — 研究问题本身非常重要且时效性强：math self-improvement 是 2026 最活跃的方向之一，三个 failure modes（noise, collapse, memorization）都有独立的高影响力论文佐证。如果 VSC 的实验结果显著优于 R-Diverse 和 NSRSA，将对该领域有实质贡献。但 significance 受限于两个因素：(a) 形式化验证的覆盖率——只有可被 Z3/SymPy 形式化的数学问题才能受益，高阶数学（如拓扑、分析）可能超出覆盖范围；(b) 贡献类型偏向工程集成而非科学洞见——\"formal verification gives cleaner signals\"是一个不令人惊讶的结论。如果实验结果为正，审稿人更可能写\"this makes sense and is a nice contribution\"而非\"this is surprising and changes how I think about the problem\"。\n\n3. **Related Work: 强** — 这是 proposal 最突出的维度。对 10+ 篇近期高度相关工作的覆盖非常全面且准确（经调研验证：FoVer、R-Diverse、NSRSA、ARISE、Prism、MATH-VF、Spurious Rewards Paradox、\"Noisy Data is Destructive\" 等论文均真实存在，描述准确）。差异化定位清晰：每篇相关工作都被明确归类为\"verified but not iterative/skill-aware\"、\"skill-aware but not verified\"、\"iterative but not diversity-aware\"等，VSC 的定位在交叉空白点上。唯一的轻微不足是对 \"Preventing Curriculum Collapse in Self-Evolving Reasoning Systems\"（arXiv 2603.13309）这篇直接相关工作的遗漏。\n\n\n【概率估计】: [22% - 32%] 中位 27%\n\n【估计理由】: \nRelated Work 维度强（准确、全面、定位清晰），说明作者对领域有深入理解。Significance 中等——问题确实重要且时效性强，但贡献类型偏工程集成。Novelty 中偏弱是限制上界的核心因素——\"formally-verified skill labels 替代 noisy LLM-based skill labels\"是一个自然、可预见的组合，缺乏概念性突破。在一个审稿人同时熟悉 FoVer 和 R-Diverse 的审稿 pool 中（AAAI 的数学推理领域审稿人很可能如此），\"这不就是把 FoVer 的验证管线接到 R-Diverse 的 diversity objective 上吗？\"是一个很自然的质疑。此外，前提假设检验中发现的 NL→Formal 翻译可靠性问题和 memorization 抑制机制的论证薄弱进一步削弱了 idea 的逻辑完整性。概率上界被 novelty 限制在 ~32%；下界 22% 来自\"如果实验结果足够强且 ablation 充分，execution quality 可以部分弥补 novelty 不足\"。\n\n【主要风险】:\n1. **\"Natural Combination\" 质疑**：审稿人直接指出这是 FoVer + R-Diverse 的工程拼接，概念性贡献不足以支撑主会论文（这是最可能的拒稿理由）。\n2. **Memorization 抑制机制论证不足**：Proposal 声称同时解决三个 failure modes，但对 memorization shortcuts 的抑制机制缺乏令人信服的解释——Anchor-Adapter 电路是训练动态问题，而非数据质量问题，step-level skill verification 不直接作用于 reward signal 的 spurious patterns。审稿人可能会指出这是对 Spurious Rewards Paradox 的误读或过度推广。\n```\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103)\n- [Noisy Data is Destructive to RLVR](https://arxiv.org/abs/2603.16140)\n- [NSRSA: Stabilizing Iterative Self-Training via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [ARISE: Agent Reasoning with Intrinsic Skill Evolution](https://arxiv.org/abs/2603.16060)\n- [Preventing Curriculum Collapse in Self-Evolving Reasoning Systems](https://arxiv.org/abs/2603.13309)\n- [Spurious Rewards Paradox](https://arxiv.org/abs/2601.11061)\n- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to produce a thorough evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **FoVer (arXiv 2505.15960, ACL 2026 Findings)**: 使用 Z3/Isabelle 对形式化推理任务进行步级错误标注，生成 PRM 训练数据。核心是 one-shot 数据合成，不涉及迭代训练，也不提取 skill 标签或追踪 skill 多样性。与本 proposal 的关系：提供了 formal verification → step-level labels 的技术基础，但缺少 skill extraction 和 iterative integration 两个关键环节。\n\n2. **R-Diverse (arXiv 2602.13103, Feb 2026)**: 识别了 self-play 训练中的 \"diversity illusion\"（表面多样但底层 skill 重复），提出 Skill-Aware Measurement (SAM) 通过 LLM 生成的 solver 程序和代码嵌入来衡量 skill 多样性，在 10 个 benchmark 上持续优于先前 self-play 方法。与本 proposal 最直接竞争：SAM 用 LLM 嵌入衡量 skill 多样性，proposal 用 formal AST 衡量——proposal 的增量贡献就在于把 SAM 的 noisy embedding 替换为 verified skill labels。\n\n3. **NSRSA (arXiv 2603.21558, Mar 2026)**: 在迭代 self-training 中嵌入 SymPy 步级验证，过滤掉约 34% 答案正确但推理有误的 solution。在 GSM8K 上 5 轮迭代达到 91.0%。与本 proposal 的关系：已经做了 \"SymPy verification + iterative training\"，但不做 skill extraction 也不做 diversity-based curriculum selection——proposal 在此之上加了 skill labeling + coverage maximization。\n\n4. **ARISE (arXiv 2603.16060, Mar 2026)**: 层次化 RL 框架，维护 tiered skill library，通过 LLM 对成功 trace 进行结构化摘要来生成 skill。在 OlympiadBench 上持续优于 GRPO-family baselines。与本 proposal 关系：同样关注 skill-based learning，但 ARISE 的 skill 来自 LLM summarization（无形式化保证），proposal 的 skill 来自 formal AST pattern matching。\n\n5. **Skill1 (arXiv 2605.06130, May 2026)**: 统一框架同时训练 skill selection、utilization 和 distillation。在 ALFWorld 和 WebShop 上表现优于 prior skill-based 和 RL baselines。与本 proposal 关系：方向相近但领域不同（agent tasks vs. math reasoning）；proposal 未引用此工作，属于遗漏。\n\n6. **Noisy Data is Destructive (arXiv 2603.16140, Mar 2026)**: 证明真正有噪声的 annotation 导致 RLVR 训练 8-10% 性能下降，现有 RLVR 算法无法补偿数据质量问题。与本 proposal 关系：提供了 \"noise hurts\" 的实证基础，是 proposal 动机的关键支撑之一。\n\n7. **Spurious Rewards Paradox (arXiv 2601.11061, Jan 2026)**: 机制层面揭示 RLVR 中的 Anchor-Adapter 电路——middle layers 的 Functional Anchor 触发记忆化 solution 检索，late layers 的 Structural Adapter 适配。与本 proposal 关系：proposal 声称 skill-diverse training 可以防止此记忆化机制，但这一论证链并不直接。\n\n8. **MATH-VF (arXiv 2505.20869, May 2025)**: Z3+SymPy 步级验证框架，使用 SimpleMath 形式语言，在 MATH500 和 ProcessBench 上测试。One-shot evaluator，不集成到训练中。与本 proposal 关系：提供了 NL→formal→verification 的具体技术路径。\n\n9. **Prismatic Synthesis / Prism-Math (arXiv 2505.20161)**: 基于梯度空间多样性（G-Vendi metric）生成语义多样的合成数学数据，PrismMath-7B 在 6/7 challenging benchmarks 上优于 R1-Distill-Qwen-7B。与本 proposal 关系：另一种 diversity-aware data selection 方法，作为潜在 baseline。\n\n- **调研总结**: 数学推理 self-improvement 领域在 2026 年上半年极为活跃，形成了三条并行技术路线：(a) 形式化验证用于数据质量/PRM (FoVer, NSRSA, MATH-VF)，(b) skill/diversity-aware curriculum selection (R-Diverse, ARISE, Prismatic Synthesis)，(c) 噪声与记忆化的机制理解 (Noisy Data, Spurious Rewards)。本 proposal 位于 (a) 和 (b) 的交叉处，试图用 formal verification 来提供 skill diversity signal。这个交叉点确实尚无直接先例工作，但组件层面的创新有限——核心 delta 是\"用 formal AST pattern matching 替代 LLM embedding 来获取 skill labels\"。\n\n【Trivial Alternative 检验】:\n\n**存在可比的更简单方案。** \n最直接的 trivial alternative 是：NSRSA 的 SymPy 验证（已有 iterative training 集成）+ 对 SymPy 表达式做简单聚类/heuristic 分类来近似 skill labels + 基于聚类的 diversity sampling。这避免了构建完整的 formal skill extraction pipeline（Z3 AST pattern matching、40-60 skill taxonomy 的手工定义），成本大幅降低。\n\nProposal 的增量价值在于：(1) skill labels 是 \"provably correct\" 的而非 heuristic 近似；(2) 预定义的 skill taxonomy 比聚类更可解释。但问题在于：NL→formal translation 本身是 LLM-based 的、有噪声的。所以\"noise-free skill labels\"的 claim 成立的前提是 NL→formal 的翻译是完美的——而 FoVer 和 MATH-VF 的实验都表明这一步有非trivial 的失败率。最终系统的噪声并未消除，只是从 reward/embedding 层面转移到了 formalization 层面。\n\n**增量价值评估**：如果 NL→formal 翻译准确率足够高（>90%），则 formal skill labels 确实优于 embedding-based skill measurement（消除了 embedding 空间的模糊性）。但这个条件本身是一个未经验证的强假设。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链存在以下未经验证的假设：\n\n1. **\"NL→formal translation 足够准确以实现 noise-free skill labels\"** — 这是最关键的假设。MATH-VF 使用了专门设计的 SimpleMath 语言来降低翻译难度，且仅在 MATH500 上测试（相对简单的问题）。对于 AIME/OlympiadBench 级别的复杂问题，NL reasoning step 到 Z3/SymPy formal expression 的翻译成功率可能大幅下降。如果翻译失败率 >20%，则 skill coverage 统计本身就是有偏的，submodular optimization 在有偏信号上运行未必优于 embedding-based 方法。\n\n2. **\"40-60 个预定义 skill 能充分覆盖数学推理的技能空间\"** — 数学推理的 skill 粒度问题是开放的。太粗（如 \"algebra\"）失去区分力；太细（如 \"factoring quadratics with leading coefficient > 1\"）导致 long-tail skills 稀疏。MathCAMPS 和 STEPS 提供了框架，但将其映射到 formal AST patterns 的具体可行性未经验证。\n\n3. **\"Skill-diverse training data 能防止 memorization shortcuts\"** — 这是最薄弱的环节。Spurious Rewards Paradox 揭示的 Anchor-Adapter 电路是由 reward signal 激活的，与训练数据的 skill composition 关系不直接。一个模型完全可以在 skill-diverse 的 curriculum 上对每个 skill 类别内的问题进行记忆化。Proposal 没有提供机制层面的论证解释 skill diversity 如何抑制 Anchor-Adapter 电路的激活。\n\n4. **\"Submodular coverage maximization 是 curriculum selection 的正确形式化\"** — 假设 skill coverage 具有 diminishing returns（submodularity），但实际 skill 间可能存在 prerequisite 关系或协同效应，简单的 coverage 目标可能忽略 skill 组合的重要性。\n\n【3 维度打分】:\n\n1. **Novelty: 弱至中** — 核心贡献是将 FoVer/MATH-VF 的 formal verification 与 R-Diverse 的 skill-aware diversity 相结合，应用于 GRPO-based iterative training。这是一个 **组合创新 (combination novelty)**：每个组件（formal verification for math steps、skill-aware diversity measurement、iterative RL training）都有成熟的先例工作。proposal 准确识别了这些工作之间的 gap，但填补方式是自然的、可预期的——\"既然 formal verification 能验证 steps，那何不用它来提取 skill labels？\"这不构成 surprising insight。与 NSRSA 相比，增量是加了 skill extraction + coverage optimization；与 R-Diverse 相比，增量是把 LLM embedding 换成 formal AST。审稿人很可能会认为这是 \"a natural extension\" 而非 \"a novel contribution\"。此外，Skill1 (May 2026) 和 ARISE (Mar 2026) 都在做 skill-based RL，进一步压缩了 novelty space。\n\n2. **Significance: 中** — 研究问题本身重要且时效性强：math reasoning self-improvement 是 2026 年最热的方向之一，noise、curriculum collapse、memorization 是真实且被广泛认可的问题。如果方法有效，对社区有实际价值。但核心发现的 surprise 程度有限——如果实验结果 positive（formal skill coverage > embedding-based diversity），审稿人大概率会说 \"this makes sense, formal labels should be cleaner than embeddings\"，而不是 \"this is surprising\"。此外，方法的 generalizability 受限于 Z3/SymPy 可处理的数学领域（代数、约束推理），对几何、组合、数论的覆盖存疑。\n\n3. **Related Work: 强** — Proposal 对领域格局的梳理相当全面和准确。关键竞争工作（FoVer、R-Diverse、NSRSA、ARISE、SAGE、Noisy Data、Spurious Rewards Paradox、MATH-VF、PSV-Verus）均被准确引用和定位。差异化分析清晰：每个 related work 缺少什么，proposal 如何填补。唯一遗漏是 Skill1 (May 2026)，这是一个很新的工作，对 skill-based RL 的研究有直接相关性。但整体 related work 覆盖在该领域的 proposal 中属于上乘。\n\n【概率估计】: [20% - 32%] 中位 25%\n\n【估计理由】: \n- Related Work 强（覆盖全面、定位清晰），但这只确保 proposal 不会因 \"missing key references\" 被拒，不直接提升 acceptance。\n- Novelty 弱至中是主要限制因素：核心贡献是对已有组件的自然组合，缺乏 surprising insight。AAAI 审稿人对 \"combination of existing techniques\" 类论文的 novelty bar 通常较高。如果三个审稿人中有两个认为 \"this is an engineering contribution, not a research contribution\"，则大概率被拒。\n- Significance 中等：问题重要但方法不够深刻。formal skill labels 替代 embedding-based labels 的改进可能在实验中体现为 marginal gains，不足以让审稿人信服这是一个质的飞跃。\n- \"Noise-free\" claim 的前提假设（NL→formal 翻译完美）在逻辑上有漏洞，审稿人很容易抓住这一点质疑整个 framework 的理论基础。\n- **上界限制因素**：Novelty。即使实验完美执行，idea 本身的 \"natural combination\" 性质限制了上界在 ~32%。\n\n【主要风险】: \n1. **Novelty 不足被判为 engineering contribution**：三个组件分别是已有工作的直接扩展，审稿人可能要求展示 combination 产生的 emergent insight 或 surprising finding，而非仅仅 \"formal labels > embedding labels\" 的预期结果。\n2. **\"Noise-free\" claim 被攻破**：NL→formal translation 本身引入噪声这一事实直接瓦解了 proposal 的核心叙事（\"formal verification eliminates verification noise\"）。审稿人只需指出 \"you moved the noise, you didn't eliminate it\" 即可质疑整个 framework 的理论动机。\n```\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103)\n- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning](https://arxiv.org/abs/2603.16060)\n- [Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://arxiv.org/abs/2605.06130)\n- [Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2603.16140)\n- [Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs](https://arxiv.org/abs/2601.11061)\n- [MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving](https://arxiv.org/abs/2505.20869)\n- [Prismatic Synthesis: Gradient-based Data Diversification Boosts Generalization in LLM Reasoning](https://arxiv.org/abs/2505.20161)\n- [FoVer GitHub Repository](https://github.com/psunlpgroup/FoVer)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Formally-Verified Skill Coverage for Robust Math Self-Improvement\n\n## Core Problem\n\nSelf-improvement loops for math reasoning fail via three interacting modes—noise sensitivity, curriculum collapse, and memorization shortcuts—all rooted in the inability to reliably measure genuine reasoning skill diversity in the generated training curriculum. Can formally-verified step-level skill decomposition provide a noise-free diversity signal that prevents all three failure modes simultaneously?\n\n## Research Opportunity\n\nRecent work has independently established that (a) formal tools can verify reasoning steps with provable correctness (FOVER, Safe), (b) skill-level diversity measurement outperforms surface metrics in self-play (R-Diverse's SAM), and (c) even small verification noise catastrophically degrades RLVR training (Zhu & Kang 2026). Yet no work combines these insights: R-Diverse's SAM uses LLM-generated code embeddings (inherently noisy), while FOVER's formal verification is one-shot and doesn't track skills or diversity. The missing piece is using formal verification tools (SymPy for algebraic operations, Z3 for constraint reasoning) to extract provably-correct skill labels from each verified reasoning step, then using skill-space coverage as the diversity objective in the self-improvement loop. This is now feasible because the self-improvement infrastructure (GRPO/DAPO), formal verification tools, and skill taxonomy frameworks (MathCAMPS, STEPS) are all mature and open-source.\n\n## Research Landscape\n\nSelf-improvement for math reasoning is a fast-moving area as of mid-2026. SAGE (Mar 2026) uses multi-agent co-evolution with a Critic for quality control but no formal verification. Prism (Mar 2026) prevents curriculum collapse via embedding-based semantic diversity (+3.98 on AMC), while R-Diverse (Feb 2026) addresses the 'diversity illusion' via Skill-Aware Measurement using LLM-generated solver programs and code embeddings. On the verification side, FOVER (ACL 2026) uses Z3/Isabelle for one-shot PRM data generation, NSRSA (Mar 2026) integrates basic SymPy checking into self-training (filtering ~34% of correct-answer solutions that have flawed reasoning), and PSV-Verus (Dec 2025) demonstrates formal-verification-driven self-play for code generation (9.6x pass@1 improvement) but in the code domain, not math reasoning. The 'Noisy Data is Destructive' paper (Mar 2026) shows current RLVR algorithms cannot compensate for noise (8-10% degradation), while the Spurious Rewards Paradox (Jan 2026) mechanistically identified how even random rewards activate memorization via an Anchor-Adapter circuit in middle-to-late layers. ARISE (Mar 2026) introduces hierarchical RL with a skill library evolved from successful traces, consistently outperforming GRPO-family baselines on OlympiadBench, but relies on LLM-summarized skills without formal guarantees. MATH-VF (May 2025) demonstrates Z3+SymPy step-level verification on MATH500 and ProcessBench but as a one-shot evaluator, not integrated into iterative training. No existing work combines formally-verified skill extraction with iterative diversity-aware self-improvement: the closest are R-Diverse (learned skills, not verified), FOVER (verified, not iterative or skill-aware), and ARISE (skill-aware, not formally verified).\n\n## Proposed Approach\n\nBuild a formal skill extractor pipeline that translates each LLM-generated reasoning step into Z3/SymPy formal expressions (extending FoVer's verification methodology and MATH-VF's step-level Z3+SymPy integration) and maps the verified formal operations to a predefined skill taxonomy (~40-60 skills such as quadratic factoring, modular arithmetic, inequality chaining, combinatorial counting) via deterministic pattern matching on the formal AST representation—yielding provably-correct, noise-free skill labels per step. Integrate this extractor into an iterative GRPO-based self-improvement loop (using the verl framework with Qwen3-8B or DeepSeek-R1-0528-Qwen3-8B as base) where curriculum selection at each of 5 training iterations maximizes a skill-space coverage objective over the verified skill distribution rather than relying on surface-level or embedding-based diversity metrics. Specifically, at each iteration, generate candidate problems, produce and formally verify solutions, extract skill coverage vectors, then select training batches that maximize marginal skill-space coverage using a submodular optimization procedure. Evaluate against R-Diverse's SAM-based selection, NSRSA's SymPy-only filtering, and vanilla GRPO baselines on MATH-500, AIME 2024/2025, AMC, and OlympiadBench, measuring both final accuracy and skill coverage breadth across iterations to demonstrate that formally-verified skill diversity prevents curriculum collapse, noise accumulation, and memorization shortcuts simultaneously.\n\n## Detailed Description\n\nWe propose Verified Skill Coverage (VSC), a self-improvement framework that uses formally-verified skill decomposition to provide a noise-free diversity signal for math reasoning training curricula. The key insight is that formal verification tools (Z3 for satisfiability and constraint reasoning, SymPy for algebraic operations) can not only verify reasoning step correctness—as in FoVer and NSRSA—but also extract provably-correct skill labels from each verified step through deterministic pattern matching on formal AST representations. We build an iterative GRPO-based training loop where curriculum selection maximizes coverage over this verified skill space, replacing noisy LLM-based diversity metrics (as in R-Diverse's SAM) with exact formal signals. This simultaneously addresses all three documented failure modes of math self-improvement: noise sensitivity (formal verification eliminates the verification noise that Zhu & Kang 2026 showed catastrophically degrades RLVR by 8-10%), curriculum collapse (skill-space coverage prevents the diversity illusion identified by R-Diverse), and memorization shortcuts (step-level skill verification ensures genuine reasoning rather than the Anchor-Adapter circuit exploitation documented in the Spurious Rewards Paradox). Using Qwen3-8B as the base model with the verl framework across 5 self-improvement iterations, we target improvements on MATH-500, AIME 2024/2025, and OlympiadBench while demonstrating sustained skill coverage breadth that existing methods fail to maintain.\n\n## Key References\n\n- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)\n- R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training (arXiv 2602.13103, 2026)\n- Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards (arXiv 2603.16140, 2026)\n- Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs (arXiv 2601.11061, 2026)\n- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2603.21558, 2026)\n- SAGE: Multi-Agent Self-Evolution for LLM Reasoning (arXiv 2603.15255, 2026)\n- ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning (arXiv 2603.16060, 2026)\n- Safe: Enhancing Mathematical Reasoning in LLMs via Retrospective Step-aware Formal Verification (ACL 2025)\n- Propose, Solve, Verify: Self-Play Through Formal Verification [PSV-Verus] (arXiv 2512.18160, 2025)\n- MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2505.20869, 2025)\n- DIVE: Diversified Iterative Self-Improvement (arXiv 2501.00747, 2025)\n- DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models [GRPO] (arXiv 2402.03300, 2024)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 2500 H100-hours (5 self-improvement iterations × ~350 GPU-hrs generation + ~150 GPU-hrs GRPO training per iteration, plus baselines/ablations at ~50% overhead), timeline: 3.5-4 months (2 weeks skill extractor development, 6 weeks main experiments, 2 weeks ablations, 2 weeks paper writing), estimated_gpu_cost: $6,250 (at $2.50/hr H100 spot pricing)\n- **human_in_loop**: gpu_hours: 2000 H100-hours (AI-assisted hyperparameter search and experiment design reduces wasted runs by ~20%), timeline: 2.5-3 months (AI accelerates skill taxonomy design, code scaffolding, and paper drafting), claude_api_cost: $400-600 (Sonnet 4.6 for code generation, experiment design, and paper drafting at ~150M tokens), estimated_gpu_cost: $5,000\n- **auto_research**: gpu_hours: 2200 H100-hours (slightly more than human-in-loop due to exploration overhead in automated ablation sweeps), timeline: 5-6 weeks (parallelized experiment execution, automated evaluation pipelines), claude_api_cost: $800-1200 (heavier API usage for autonomous code generation, debugging Z3/SymPy edge cases, and iterative paper revision), estimated_gpu_cost: $5,500, speed_bottleneck: Formal verification pipeline debugging—Z3/SymPy translation from natural language reasoning steps has long-tail failure modes requiring human judgment on taxonomy boundary cases; also vLLM throughput for 800K+ solution generations per iteration\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T21:00:53.370Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T21:00:53.370Z",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T21:00:53.404Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make a thorough assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- FoVer (arXiv 2505.15960, ACL 2026 Findings): 使用 Z3/Isabelle 进行形式化验证来合成 PRM 训练数据（FoVer-80K），一次性生成，非迭代，不追踪技能或多样性。验证了形式化工具可以为 math reasoning 提供可靠的 step-level 标签。
- R-Diverse (arXiv 2602.13103, Feb 2026): 提出 Skill-Aware Measurement (SAM)，用 LLM 生成的 solver 程序和代码嵌入来衡量技能多样性，解决 self-play 训练中的"多样性幻觉"（Local + Surface Diversity Illusion）。在 10 个 benchmark 上持续优于 prior self-play 方法。技能衡量基于 LLM 嵌入，非形式化验证。
- NSRSA (arXiv 2603.21558, Mar 2026): 将 SymPy 验证集成到迭代 self-training 中，过滤约 34% 答案正确但推理有缺陷的解（"lucky guesses"）。关注验证过滤，不做技能提取或多样性度量。在 Qwen3-4B 上验证，规模较小。
- Noisy Data is Destructive (arXiv 2603.16140, Mar 2026, Zhu & Kang): 证明 RLVR 中 8-10% 的标注噪声导致严重性能下降，现有 RLVR 算法（包括改进版 GRPO）无法补偿噪声。强调高质量数据的不可替代性。
- Spurious Rewards Paradox (arXiv 2601.11061, Jan 2026): 用 Path Patching/Logit Lens 等方法发现 RLVR 中的 Anchor-Adapter circuit（中间层 L18-20 + 后层 L21+），即使随机/虚假奖励也能激活记忆捷径。这是 reward-level 的机制性发现，而非 curriculum-level 的问题。
- Prism (arXiv 2603.13309, Mar 2026): 基于嵌入的语义分区 + ZPD 门控，防止 self-evolving 系统的 curriculum collapse。在 AMC 上比 R-Zero 高 +3.98。方法简单，无需形式化验证即实现强效果。
- ARISE (arXiv 2603.16060, Mar 2026): 层级 RL 框架，从成功 trace 中用 LLM 摘要生成技能库，集成到 GRPO 训练中。在 OlympiadBench 上持续优于 GRPO-family baseline。技能基于 LLM 摘要，无形式化保证。
- PSV-Verus (arXiv 2512.18160, Dec 2025): 形式化验证驱动的 self-play 用于代码生成（Rust/Verus），pass@1 提升 9.6×。但在代码领域，非 math reasoning。
- MATH-VF (arXiv 2505.20869, May 2025): 用 Z3+SymPy 进行 step-level 数学推理验证，在 MATH500 和 ProcessBench 上评估。Training-free 评估器，未集成到训练循环中。
- RLVεR (arXiv 2601.04411, Jan 2026): 从理论角度建模 RLVR 中噪声奖励的影响，补充 Zhu & Kang 的实证发现。
- 调研总结: 数学推理 self-improvement 在 2026 年上半年是高度活跃的研究方向，三条技术线索——形式化验证（FoVer/NSRSA/MATH-VF）、多样性度量（R-Diverse/Prism）、技能库演化（ARISE）——已各自独立成熟。本 proposal 位于这三条线的交汇点，填补了"形式化验证 + 技能多样性 + 迭代训练"的组合空缺。这个空缺是真实的，但也是显而易见的——任何同时阅读过 FoVer 和 R-Diverse 的研究者都会想到这个组合。

【Trivial Alternative 检验】:
存在多个成本更低的替代方案可能达到类似效果：

1. **NSRSA + R-Diverse SAM 直接组合**: 在 NSRSA 的 SymPy 验证过滤基础上，直接叠加 R-Diverse 的 SAM 多样性指标进行 curriculum 选择。无需构建完整的形式化技能提取管线，即可同时获得"验证过滤去噪"和"技能多样性选择"两个好处。这个组合的工程成本远低于本 proposal，但可能达到 80-90% 的效果。

2. **FoVer 验证 + Prism 嵌入多样性**: 用 FoVer 的形式化验证做 step-level 过滤（去噪），然后用 Prism 的嵌入语义分区做多样性选择。Prism 已经在 AMC 上展示了 +3.98 的提升，且不需要预定义技能分类体系。

3. **ARISE 的 LLM 技能库 + SymPy 过滤**: ARISE 已经展示了 LLM 摘要技能库在 OlympiadBench 上优于 GRPO-family 的结果。在其基础上加入 SymPy 过滤即可获得验证保证。

本 proposal 的增量价值在于：用形式化 AST 模式匹配提取的技能标签理论上比 LLM 嵌入或摘要更准确和无噪声。但这个增量价值有两个问题：(a) NL→formal 的翻译步骤本身会引入噪声，"无噪声"的承诺在实际执行中打折扣；(b) 多样性度量的噪声是否是绑定约束（binding constraint）？Zhu & Kang 的工作证明 reward 噪声是致命的，但 diversity metric 的噪声对最终性能的影响没有被独立验证过。

【前提假设检验】:
核心逻辑链中有以下未经验证的假设：

1. **"形式化技能标签是无噪声的"（最关键）**: Proposal 声称通过 Z3/SymPy 验证 + AST 模式匹配可以获得"provably-correct, noise-free skill labels"。但这忽略了关键的前置步骤——将 LLM 生成的自然语言推理步骤翻译成 Z3/SymPy 形式化表达式。这个翻译步骤本身依赖 LLM（或规则系统），必然引入噪声和覆盖率问题。FoVer 和 MATH-VF 的论文中都有大量推理步骤无法被成功形式化的情况。"noise-free"只在 Z3/SymPy 验证环节成立，整个管线看下来并不是 noise-free 的。

2. **"技能空间覆盖可以同时防止课程崩塌、噪声积累和记忆捷径三种失败模式"**: 这是 proposal 最核心的 claim，但逻辑链条在"记忆捷径"环节断裂。Spurious Rewards Paradox 论文明确表明，记忆捷径是在 reward 信号层面通过 Anchor-Adapter circuit 被激活的，这是一个模型内部机制问题，不是 curriculum 组成问题。更好的课程多样性可能缓解但无法"防止"记忆捷径——因为 GRPO 的 reward signal 结构并未被本 proposal 改变。

3. **"40-60 个预定义技能 + 确定性模式匹配可以覆盖竞赛数学空间"**: 竞赛数学（AIME、OlympiadBench）的核心难度在于技能的创造性组合和跨领域迁移，而非单一技能的应用。预定义的 40-60 个技能分类体系 + 刚性模式匹配可能对标准 MATH 500 有效，但对竞赛级别问题的覆盖率是存疑的。

4. **"多样性度量的噪声是当前 self-improvement 的绑定约束"**: Proposal 的立论基础是 R-Diverse 的 SAM 因为使用 LLM 嵌入而有噪声，而形式化方法可以消除这个噪声。但没有实证表明 SAM 的噪声是限制 self-improvement 性能的 bottleneck。可能其他因素（reward 设计、问题难度分布、训练动态）才是真正的瓶颈。

【3 维度打分】:
1. Novelty: 弱-中 — 核心贡献是将 FoVer/MATH-VF 的形式化验证、R-Diverse/ARISE 的技能多样性度量、GRPO-based 迭代训练三个已有组件组合在一起。每个组件都来自 2025-2026 年的近期工作，组合本身是设计空间中的一个显而易见的空位——任何同时阅读过 FoVer（ACL 2026）和 R-Diverse（Feb 2026）的研究者都会想到"为什么不用形式化验证来替代 SAM 中的 LLM 嵌入？"具体的技术贡献（AST 模式匹配提取技能标签、子模优化选择课程）是工程实现层面的，而非概念性创新。与 NSRSA（已经做了 SymPy + 迭代训练）和 ARISE（已经做了技能库 + RL 训练）相比，剩余的 novelty delta 较薄。如果 positive result 出来，审稿人更可能说"this is a natural combination"而非"this is surprising"。

2. Significance: 中 — 研究问题本身（math self-improvement 的失败模式）是重要的，2026 年多篇高影响力论文都在研究这个方向。但本 proposal 的影响范围受限于：(a) 只适用于可形式化的数学领域，不推广到 general reasoning；(b) 依赖预定义技能分类体系，难以适应新出现的问题类型；(c) 如果形式化翻译覆盖率有限（如只覆盖代数和算术），那么 skill coverage 度量本身就是有偏的。相比之下，Prism 的嵌入方法和 ARISE 的 LLM 技能摘要虽然有噪声，但覆盖面更广、适应性更强。

3. Related Work: 强 — Proposal 对 2025-2026 年的相关工作覆盖全面且准确。FoVer、R-Diverse、NSRSA、ARISE、Prism、PSV-Verus、MATH-VF、噪声/记忆化论文都被正确引用和定位。差异化定位（"没有工作同时做形式化验证 + 技能多样性 + 迭代训练"）是真实的。所有引用的论文经调研验证真实存在且描述准确。唯一的小缺陷是未引用 Prismatic Synthesis（关于嵌入多样性未必保证模型提升的反面证据）和 RLVεR（噪声奖励的理论分析）。

【概率估计】: [18% - 28%] 中位 22%

【估计理由】: 
Related Work 维度是强的，说明作者对领域有深入理解，positioning 清晰。但 Novelty 是限制上界的核心维度——这是一个"显而易见的组合"型工作，将三个已有技术组件拼接在一起，审稿人很可能认为 incremental。Significance 受限于形式化方法的覆盖率和推广性问题。

核心 claim "形式化验证提供无噪声技能标签从而同时解决三种失败模式"在逻辑上有断裂——特别是"记忆捷径"环节的因果链不成立（这是 reward-level 现象，不是 curriculum-level 现象），以及"无噪声"承诺被 NL→formal 翻译步骤所削弱。如果审稿人抓住这两点，paper 会在 soundness 和 novelty 上同时被质疑。

22% 中位意味着：方向不致命，gap 是真实的，但 idea 内核偏薄，更像是工程贡献而非概念性突破。如果实验展示出显著优于 R-Diverse 和 NSRSA 的结果（> 3-5% on AIME），执行质量可以部分弥补 novelty 不足，将概率推到上界附近；但如果提升有限（1-2%），审稿人会认为不值得引入如此复杂的管线。

【主要风险】: 
1. **"显而易见的组合"（Obvious Combination）**: 审稿人最可能的批评——FoVer + R-Diverse + GRPO 的三方组合是 design space 中的自然填充，缺乏 surprising insight。核心问题不是"这个组合 work 不 work"，而是"你告诉了我们什么关于 formal verification 在 self-improvement 中作用的新知识？"
2. **"无噪声"承诺与实际管线矛盾**: NL→formal 翻译步骤的覆盖率和准确率是整个系统的瓶颈，但 proposal 对此几乎未做讨论。审稿人会追问：如果只有 50-60% 的推理步骤能被成功形式化，那 "noise-free skill labels" 的 claim 是否名不副实？这种 partial coverage 是否反而引入了新的 bias？
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103)
- [Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2603.16140)
- [Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs](https://arxiv.org/abs/2601.11061)
- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning](https://arxiv.org/abs/2603.16060)
- [Prism: Preventing Curriculum Collapse in Self-Evolving Reasoning Systems](https://arxiv.org/pdf/2603.13309)
- [PSV-Verus: Propose, Solve, Verify: Self-Play Through Formal Verification](https://arxiv.org/abs/2512.18160)
- [MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving](https://arxiv.org/abs/2505.20869)
- [Rate or Fate? RLVεR: Reinforcement Learning with Verifiable Noisy Rewards](https://arxiv.org/abs/2601.04411)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient context for a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

1. FoVer (arXiv 2505.15960, ACL 2026 Findings): 使用 Z3/Isabelle 对 formal reasoning tasks 进行 step-level 验证，生成 PRM 训练数据。关键局限：one-shot 生成，不追踪 skill，不参与迭代训练循环。Proposal 准确描述了其能力与局限。

2. R-Diverse (arXiv 2602.13103, Feb 2026): 提出 Skill-Aware Measurement (SAM) 解决 self-play 中的 "diversity illusion"，使用 LLM-generated solver programs + code embeddings 衡量 skill 多样性。在 10 个 benchmark 上维持 5 轮迭代的持续增长。关键局限：SAM 依赖 LLM 生成的代码嵌入，本质上是有噪声的。Proposal 对此定位准确。

3. "Noisy Data is Destructive to RLVR" (arXiv 2603.16140, Mar 2026): 严格证明了真正有噪声的标注在 RLVR 中导致 8-10% 的性能下降，且现有 RLVR 算法改进（包括 GRPO 变体）无法补偿噪声影响。这是 proposal 的核心动机之一，论文真实存在且描述准确。

4. NSRSA (arXiv 2603.21558, Mar 2026): 在迭代 self-training 中集成 SymPy 进行 step-level 验证，过滤约 34% "碰巧答对但推理有误"的解。关键局限：只做了正确性过滤，没有 skill 追踪或多样性优化。这是 proposal 声称要超越的关键 baseline。

5. ARISE (arXiv 2603.16060, Mar 2026): 层级 RL 框架，skill library 与 policy 共同进化。在 OlympiadBench 等 benchmark 上持续优于 GRPO 族方法。关键局限：skill 由 LLM 总结生成，无形式化保证。

6. Prism / Preventing Curriculum Collapse (arXiv 2603.13309, Mar 2026): 使用 embedding-based semantic diversity 进行课程选择，在 AMC 上比 R-Zero 高 +3.98。关键局限：基于嵌入而非形式化方法，受限于 embedding 质量。

7. MATH-VF (arXiv 2505.20869, May 2025): Z3+SymPy 的 step-level 验证器，在 MATH500 和 ProcessBench 上验证推理步骤。关键局限：one-shot evaluator，未集成到迭代训练中。

8. Spurious Rewards Paradox (arXiv 2601.11061, Jan 2026): 用 Path Patching 和 Neural ODE 揭示了 RLVR 中的 Anchor-Adapter 记忆捷径电路（L18-20 层 Functional Anchor + L21+ 层 Structural Adapter）。论文真实存在，描述准确。

9. PSV-Verus (arXiv 2512.18160, Dec 2025): 在代码生成领域实现 formal-verification-driven self-play，9.6x pass@1 提升，但不在 math reasoning 领域。

- 调研总结: Math self-improvement 在 2026 上半年极其活跃，形式化验证（FoVer, NSRSA, MATH-VF）和多样性感知训练（R-Diverse, Prism, ARISE）各自发展成熟但尚未交叉融合。Proposal 准确定位在这个交叉空白点上——"formally-verified skill extraction + iterative diversity-aware training"确实没有直接竞争者，但各组件的成熟度意味着这一组合是自然可预见的下一步。


【Trivial Alternative 检验】:

存在两个成本更低的替代方案构成威胁：

(1) **NSRSA + R-Diverse 的直接拼接**：用 NSRSA 的 SymPy 过滤保证步骤正确性，同时用 R-Diverse 的 SAM 进行 skill-aware 课程选择。这不需要构建新的 formal skill extractor，只需工程层面的集成。Proposal 的增量价值在于：SAM 的 skill 度量本身有噪声（基于 LLM code embeddings），而 VSC 的 skill labels 是确定性的、provably correct 的——但这个增量价值依赖于"SAM 的噪声在实际训练中是否真正造成问题"这个未经验证的假设。

(2) **FoVer 验证 + 简单覆盖启发式**：用 FoVer 的验证管线保证正确性，加上对问题类型的简单分桶（如按数学子领域/难度）做覆盖，而不需要构建细粒度的 40-60 skill taxonomy。如果粗粒度覆盖已经足够防止 curriculum collapse，那么精细 skill taxonomy 的边际收益可能很小。

Proposal 的真正增量价值在于：(a) 将"验证正确性"和"提取 skill labels"统一在同一形式化管线中，减少系统复杂度；(b) 声称可以同时解决三个失败模式。但审稿人可能会质疑：三个失败模式中，noise sensitivity 主要被 formal verification 解决（NSRSA 已证明），curriculum collapse 主要被 diversity-aware selection 解决（R-Diverse/Prism 已证明），memorization shortcuts 的解决机制最不清楚——step-level skill verification 如何直接阻止 Anchor-Adapter 电路的激活？


【前提假设检验】:

核心逻辑链中存在以下未经验证的假设：

1. **NL→Formal 翻译的可靠性假设**（最关键）：Proposal 假设可以将 LLM 生成的自然语言推理步骤可靠地翻译成 Z3/SymPy 形式化表达。FoVer 在 formal reasoning tasks 上工作良好，但 LLM 生成的 CoT 推理是非结构化的自然语言，翻译失败率可能很高。Proposal 承认这是 "long-tail failure mode"（在 Resource Estimate 中提及），但未量化或提出缓解方案。如果大量推理步骤无法被形式化，skill coverage 信号会系统性偏向可形式化的简单步骤，反而引入新的偏差。

2. **Skill Taxonomy 充分性假设**：预定义 40-60 个 skill 的 taxonomy 假设了数学推理技能可以被离散化且穷举。但竞赛数学（AIME/OlympiadBench）常涉及 creative problem-solving（如构造辅助函数、类比推理），这些难以被预定义 taxonomy 覆盖。如果高难度问题的关键 skill 不在 taxonomy 中，skill coverage 会错误地认为这些问题"没有新 skill 贡献"。

3. **Skill Coverage = Reasoning Diversity 假设**：Proposal 假设最大化 skill-space coverage 等同于最大化推理多样性。但同一 skill（如"inequality chaining"）可以有截然不同的难度和应用场景，仅追踪 skill 出现频率可能遗漏 skill 深度/组合复杂度这个维度。

4. **Memorization抑制假设**（最弱）：Proposal 声称 step-level skill verification 可以阻止 memorization shortcuts，但 Spurious Rewards Paradox 论文揭示的 Anchor-Adapter 机制在 middle-to-late layers 中通过 reward signal 激活——这是一个训练动态问题，不是数据质量问题。即使训练数据经过完美的 skill 验证，如果 reward signal 本身存在 spurious patterns，Anchor-Adapter 电路仍然可能被激活。Proposal 在这一点上的论证链最弱。


【3 维度打分】:

1. **Novelty: 中偏弱** — Proposal 的核心贡献是将已有的形式化验证（FoVer/MATH-VF 的 Z3+SymPy）与已有的 skill-aware diversity（R-Diverse 的 SAM 思路）进行组合，并放入已有的迭代训练框架（GRPO/verl）中。这是一个"自然组合"（natural combination）——任何同时读过 FoVer 和 R-Diverse 的研究者都可能想到"用 formal verification 替代 LLM embeddings 来提取 skill labels"。具体的技术细节（AST pattern matching → skill taxonomy, submodular coverage optimization）有一定工程创新但不构成概念性突破。与 NSRSA（已经做了 SymPy + iterative training）的差异主要在于加了 skill taxonomy 和 coverage objective——这是增量性的，而非范式性的。Prism 论文（Mar 2026）已经在做基于语义空间的 coverage 优化，VSC 本质上是将 embedding space 替换为 formal skill space——是信号来源的替换而非方法论的革新。

2. **Significance: 中** — 研究问题本身非常重要且时效性强：math self-improvement 是 2026 最活跃的方向之一，三个 failure modes（noise, collapse, memorization）都有独立的高影响力论文佐证。如果 VSC 的实验结果显著优于 R-Diverse 和 NSRSA，将对该领域有实质贡献。但 significance 受限于两个因素：(a) 形式化验证的覆盖率——只有可被 Z3/SymPy 形式化的数学问题才能受益，高阶数学（如拓扑、分析）可能超出覆盖范围；(b) 贡献类型偏向工程集成而非科学洞见——"formal verification gives cleaner signals"是一个不令人惊讶的结论。如果实验结果为正，审稿人更可能写"this makes sense and is a nice contribution"而非"this is surprising and changes how I think about the problem"。

3. **Related Work: 强** — 这是 proposal 最突出的维度。对 10+ 篇近期高度相关工作的覆盖非常全面且准确（经调研验证：FoVer、R-Diverse、NSRSA、ARISE、Prism、MATH-VF、Spurious Rewards Paradox、"Noisy Data is Destructive" 等论文均真实存在，描述准确）。差异化定位清晰：每篇相关工作都被明确归类为"verified but not iterative/skill-aware"、"skill-aware but not verified"、"iterative but not diversity-aware"等，VSC 的定位在交叉空白点上。唯一的轻微不足是对 "Preventing Curriculum Collapse in Self-Evolving Reasoning Systems"（arXiv 2603.13309）这篇直接相关工作的遗漏。


【概率估计】: [22% - 32%] 中位 27%

【估计理由】: 
Related Work 维度强（准确、全面、定位清晰），说明作者对领域有深入理解。Significance 中等——问题确实重要且时效性强，但贡献类型偏工程集成。Novelty 中偏弱是限制上界的核心因素——"formally-verified skill labels 替代 noisy LLM-based skill labels"是一个自然、可预见的组合，缺乏概念性突破。在一个审稿人同时熟悉 FoVer 和 R-Diverse 的审稿 pool 中（AAAI 的数学推理领域审稿人很可能如此），"这不就是把 FoVer 的验证管线接到 R-Diverse 的 diversity objective 上吗？"是一个很自然的质疑。此外，前提假设检验中发现的 NL→Formal 翻译可靠性问题和 memorization 抑制机制的论证薄弱进一步削弱了 idea 的逻辑完整性。概率上界被 novelty 限制在 ~32%；下界 22% 来自"如果实验结果足够强且 ablation 充分，execution quality 可以部分弥补 novelty 不足"。

【主要风险】:
1. **"Natural Combination" 质疑**：审稿人直接指出这是 FoVer + R-Diverse 的工程拼接，概念性贡献不足以支撑主会论文（这是最可能的拒稿理由）。
2. **Memorization 抑制机制论证不足**：Proposal 声称同时解决三个 failure modes，但对 memorization shortcuts 的抑制机制缺乏令人信服的解释——Anchor-Adapter 电路是训练动态问题，而非数据质量问题，step-level skill verification 不直接作用于 reward signal 的 spurious patterns。审稿人可能会指出这是对 Spurious Rewards Paradox 的误读或过度推广。
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103)
- [Noisy Data is Destructive to RLVR](https://arxiv.org/abs/2603.16140)
- [NSRSA: Stabilizing Iterative Self-Training via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [ARISE: Agent Reasoning with Intrinsic Skill Evolution](https://arxiv.org/abs/2603.16060)
- [Preventing Curriculum Collapse in Self-Evolving Reasoning Systems](https://arxiv.org/abs/2603.13309)
- [Spurious Rewards Paradox](https://arxiv.org/abs/2601.11061)
- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to produce a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **FoVer (arXiv 2505.15960, ACL 2026 Findings)**: 使用 Z3/Isabelle 对形式化推理任务进行步级错误标注，生成 PRM 训练数据。核心是 one-shot 数据合成，不涉及迭代训练，也不提取 skill 标签或追踪 skill 多样性。与本 proposal 的关系：提供了 formal verification → step-level labels 的技术基础，但缺少 skill extraction 和 iterative integration 两个关键环节。

2. **R-Diverse (arXiv 2602.13103, Feb 2026)**: 识别了 self-play 训练中的 "diversity illusion"（表面多样但底层 skill 重复），提出 Skill-Aware Measurement (SAM) 通过 LLM 生成的 solver 程序和代码嵌入来衡量 skill 多样性，在 10 个 benchmark 上持续优于先前 self-play 方法。与本 proposal 最直接竞争：SAM 用 LLM 嵌入衡量 skill 多样性，proposal 用 formal AST 衡量——proposal 的增量贡献就在于把 SAM 的 noisy embedding 替换为 verified skill labels。

3. **NSRSA (arXiv 2603.21558, Mar 2026)**: 在迭代 self-training 中嵌入 SymPy 步级验证，过滤掉约 34% 答案正确但推理有误的 solution。在 GSM8K 上 5 轮迭代达到 91.0%。与本 proposal 的关系：已经做了 "SymPy verification + iterative training"，但不做 skill extraction 也不做 diversity-based curriculum selection——proposal 在此之上加了 skill labeling + coverage maximization。

4. **ARISE (arXiv 2603.16060, Mar 2026)**: 层次化 RL 框架，维护 tiered skill library，通过 LLM 对成功 trace 进行结构化摘要来生成 skill。在 OlympiadBench 上持续优于 GRPO-family baselines。与本 proposal 关系：同样关注 skill-based learning，但 ARISE 的 skill 来自 LLM summarization（无形式化保证），proposal 的 skill 来自 formal AST pattern matching。

5. **Skill1 (arXiv 2605.06130, May 2026)**: 统一框架同时训练 skill selection、utilization 和 distillation。在 ALFWorld 和 WebShop 上表现优于 prior skill-based 和 RL baselines。与本 proposal 关系：方向相近但领域不同（agent tasks vs. math reasoning）；proposal 未引用此工作，属于遗漏。

6. **Noisy Data is Destructive (arXiv 2603.16140, Mar 2026)**: 证明真正有噪声的 annotation 导致 RLVR 训练 8-10% 性能下降，现有 RLVR 算法无法补偿数据质量问题。与本 proposal 关系：提供了 "noise hurts" 的实证基础，是 proposal 动机的关键支撑之一。

7. **Spurious Rewards Paradox (arXiv 2601.11061, Jan 2026)**: 机制层面揭示 RLVR 中的 Anchor-Adapter 电路——middle layers 的 Functional Anchor 触发记忆化 solution 检索，late layers 的 Structural Adapter 适配。与本 proposal 关系：proposal 声称 skill-diverse training 可以防止此记忆化机制，但这一论证链并不直接。

8. **MATH-VF (arXiv 2505.20869, May 2025)**: Z3+SymPy 步级验证框架，使用 SimpleMath 形式语言，在 MATH500 和 ProcessBench 上测试。One-shot evaluator，不集成到训练中。与本 proposal 关系：提供了 NL→formal→verification 的具体技术路径。

9. **Prismatic Synthesis / Prism-Math (arXiv 2505.20161)**: 基于梯度空间多样性（G-Vendi metric）生成语义多样的合成数学数据，PrismMath-7B 在 6/7 challenging benchmarks 上优于 R1-Distill-Qwen-7B。与本 proposal 关系：另一种 diversity-aware data selection 方法，作为潜在 baseline。

- **调研总结**: 数学推理 self-improvement 领域在 2026 年上半年极为活跃，形成了三条并行技术路线：(a) 形式化验证用于数据质量/PRM (FoVer, NSRSA, MATH-VF)，(b) skill/diversity-aware curriculum selection (R-Diverse, ARISE, Prismatic Synthesis)，(c) 噪声与记忆化的机制理解 (Noisy Data, Spurious Rewards)。本 proposal 位于 (a) 和 (b) 的交叉处，试图用 formal verification 来提供 skill diversity signal。这个交叉点确实尚无直接先例工作，但组件层面的创新有限——核心 delta 是"用 formal AST pattern matching 替代 LLM embedding 来获取 skill labels"。

【Trivial Alternative 检验】:

**存在可比的更简单方案。** 
最直接的 trivial alternative 是：NSRSA 的 SymPy 验证（已有 iterative training 集成）+ 对 SymPy 表达式做简单聚类/heuristic 分类来近似 skill labels + 基于聚类的 diversity sampling。这避免了构建完整的 formal skill extraction pipeline（Z3 AST pattern matching、40-60 skill taxonomy 的手工定义），成本大幅降低。

Proposal 的增量价值在于：(1) skill labels 是 "provably correct" 的而非 heuristic 近似；(2) 预定义的 skill taxonomy 比聚类更可解释。但问题在于：NL→formal translation 本身是 LLM-based 的、有噪声的。所以"noise-free skill labels"的 claim 成立的前提是 NL→formal 的翻译是完美的——而 FoVer 和 MATH-VF 的实验都表明这一步有非trivial 的失败率。最终系统的噪声并未消除，只是从 reward/embedding 层面转移到了 formalization 层面。

**增量价值评估**：如果 NL→formal 翻译准确率足够高（>90%），则 formal skill labels 确实优于 embedding-based skill measurement（消除了 embedding 空间的模糊性）。但这个条件本身是一个未经验证的强假设。

【前提假设检验】:

核心 claim 的逻辑链存在以下未经验证的假设：

1. **"NL→formal translation 足够准确以实现 noise-free skill labels"** — 这是最关键的假设。MATH-VF 使用了专门设计的 SimpleMath 语言来降低翻译难度，且仅在 MATH500 上测试（相对简单的问题）。对于 AIME/OlympiadBench 级别的复杂问题，NL reasoning step 到 Z3/SymPy formal expression 的翻译成功率可能大幅下降。如果翻译失败率 >20%，则 skill coverage 统计本身就是有偏的，submodular optimization 在有偏信号上运行未必优于 embedding-based 方法。

2. **"40-60 个预定义 skill 能充分覆盖数学推理的技能空间"** — 数学推理的 skill 粒度问题是开放的。太粗（如 "algebra"）失去区分力；太细（如 "factoring quadratics with leading coefficient > 1"）导致 long-tail skills 稀疏。MathCAMPS 和 STEPS 提供了框架，但将其映射到 formal AST patterns 的具体可行性未经验证。

3. **"Skill-diverse training data 能防止 memorization shortcuts"** — 这是最薄弱的环节。Spurious Rewards Paradox 揭示的 Anchor-Adapter 电路是由 reward signal 激活的，与训练数据的 skill composition 关系不直接。一个模型完全可以在 skill-diverse 的 curriculum 上对每个 skill 类别内的问题进行记忆化。Proposal 没有提供机制层面的论证解释 skill diversity 如何抑制 Anchor-Adapter 电路的激活。

4. **"Submodular coverage maximization 是 curriculum selection 的正确形式化"** — 假设 skill coverage 具有 diminishing returns（submodularity），但实际 skill 间可能存在 prerequisite 关系或协同效应，简单的 coverage 目标可能忽略 skill 组合的重要性。

【3 维度打分】:

1. **Novelty: 弱至中** — 核心贡献是将 FoVer/MATH-VF 的 formal verification 与 R-Diverse 的 skill-aware diversity 相结合，应用于 GRPO-based iterative training。这是一个 **组合创新 (combination novelty)**：每个组件（formal verification for math steps、skill-aware diversity measurement、iterative RL training）都有成熟的先例工作。proposal 准确识别了这些工作之间的 gap，但填补方式是自然的、可预期的——"既然 formal verification 能验证 steps，那何不用它来提取 skill labels？"这不构成 surprising insight。与 NSRSA 相比，增量是加了 skill extraction + coverage optimization；与 R-Diverse 相比，增量是把 LLM embedding 换成 formal AST。审稿人很可能会认为这是 "a natural extension" 而非 "a novel contribution"。此外，Skill1 (May 2026) 和 ARISE (Mar 2026) 都在做 skill-based RL，进一步压缩了 novelty space。

2. **Significance: 中** — 研究问题本身重要且时效性强：math reasoning self-improvement 是 2026 年最热的方向之一，noise、curriculum collapse、memorization 是真实且被广泛认可的问题。如果方法有效，对社区有实际价值。但核心发现的 surprise 程度有限——如果实验结果 positive（formal skill coverage > embedding-based diversity），审稿人大概率会说 "this makes sense, formal labels should be cleaner than embeddings"，而不是 "this is surprising"。此外，方法的 generalizability 受限于 Z3/SymPy 可处理的数学领域（代数、约束推理），对几何、组合、数论的覆盖存疑。

3. **Related Work: 强** — Proposal 对领域格局的梳理相当全面和准确。关键竞争工作（FoVer、R-Diverse、NSRSA、ARISE、SAGE、Noisy Data、Spurious Rewards Paradox、MATH-VF、PSV-Verus）均被准确引用和定位。差异化分析清晰：每个 related work 缺少什么，proposal 如何填补。唯一遗漏是 Skill1 (May 2026)，这是一个很新的工作，对 skill-based RL 的研究有直接相关性。但整体 related work 覆盖在该领域的 proposal 中属于上乘。

【概率估计】: [20% - 32%] 中位 25%

【估计理由】: 
- Related Work 强（覆盖全面、定位清晰），但这只确保 proposal 不会因 "missing key references" 被拒，不直接提升 acceptance。
- Novelty 弱至中是主要限制因素：核心贡献是对已有组件的自然组合，缺乏 surprising insight。AAAI 审稿人对 "combination of existing techniques" 类论文的 novelty bar 通常较高。如果三个审稿人中有两个认为 "this is an engineering contribution, not a research contribution"，则大概率被拒。
- Significance 中等：问题重要但方法不够深刻。formal skill labels 替代 embedding-based labels 的改进可能在实验中体现为 marginal gains，不足以让审稿人信服这是一个质的飞跃。
- "Noise-free" claim 的前提假设（NL→formal 翻译完美）在逻辑上有漏洞，审稿人很容易抓住这一点质疑整个 framework 的理论基础。
- **上界限制因素**：Novelty。即使实验完美执行，idea 本身的 "natural combination" 性质限制了上界在 ~32%。

【主要风险】: 
1. **Novelty 不足被判为 engineering contribution**：三个组件分别是已有工作的直接扩展，审稿人可能要求展示 combination 产生的 emergent insight 或 surprising finding，而非仅仅 "formal labels > embedding labels" 的预期结果。
2. **"Noise-free" claim 被攻破**：NL→formal translation 本身引入噪声这一事实直接瓦解了 proposal 的核心叙事（"formal verification eliminates verification noise"）。审稿人只需指出 "you moved the noise, you didn't eliminate it" 即可质疑整个 framework 的理论动机。
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://arxiv.org/abs/2602.13103)
- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning](https://arxiv.org/abs/2603.16060)
- [Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://arxiv.org/abs/2605.06130)
- [Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2603.16140)
- [Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs](https://arxiv.org/abs/2601.11061)
- [MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving](https://arxiv.org/abs/2505.20869)
- [Prismatic Synthesis: Gradient-based Data Diversification Boosts Generalization in LLM Reasoning](https://arxiv.org/abs/2505.20161)
- [FoVer GitHub Repository](https://github.com/psunlpgroup/FoVer)


【原始 proposal（允许参考但不是主要依据）】:
# Formally-Verified Skill Coverage for Robust Math Self-Improvement

## Core Problem

Self-improvement loops for math reasoning fail via three interacting modes—noise sensitivity, curriculum collapse, and memorization shortcuts—all rooted in the inability to reliably measure genuine reasoning skill diversity in the generated training curriculum. Can formally-verified step-level skill decomposition provide a noise-free diversity signal that prevents all three failure modes simultaneously?

## Research Opportunity

Recent work has independently established that (a) formal tools can verify reasoning steps with provable correctness (FOVER, Safe), (b) skill-level diversity measurement outperforms surface metrics in self-play (R-Diverse's SAM), and (c) even small verification noise catastrophically degrades RLVR training (Zhu & Kang 2026). Yet no work combines these insights: R-Diverse's SAM uses LLM-generated code embeddings (inherently noisy), while FOVER's formal verification is one-shot and doesn't track skills or diversity. The missing piece is using formal verification tools (SymPy for algebraic operations, Z3 for constraint reasoning) to extract provably-correct skill labels from each verified reasoning step, then using skill-space coverage as the diversity objective in the self-improvement loop. This is now feasible because the self-improvement infrastructure (GRPO/DAPO), formal verification tools, and skill taxonomy frameworks (MathCAMPS, STEPS) are all mature and open-source.

## Research Landscape

Self-improvement for math reasoning is a fast-moving area as of mid-2026. SAGE (Mar 2026) uses multi-agent co-evolution with a Critic for quality control but no formal verification. Prism (Mar 2026) prevents curriculum collapse via embedding-based semantic diversity (+3.98 on AMC), while R-Diverse (Feb 2026) addresses the 'diversity illusion' via Skill-Aware Measurement using LLM-generated solver programs and code embeddings. On the verification side, FOVER (ACL 2026) uses Z3/Isabelle for one-shot PRM data generation, NSRSA (Mar 2026) integrates basic SymPy checking into self-training (filtering ~34% of correct-answer solutions that have flawed reasoning), and PSV-Verus (Dec 2025) demonstrates formal-verification-driven self-play for code generation (9.6x pass@1 improvement) but in the code domain, not math reasoning. The 'Noisy Data is Destructive' paper (Mar 2026) shows current RLVR algorithms cannot compensate for noise (8-10% degradation), while the Spurious Rewards Paradox (Jan 2026) mechanistically identified how even random rewards activate memorization via an Anchor-Adapter circuit in middle-to-late layers. ARISE (Mar 2026) introduces hierarchical RL with a skill library evolved from successful traces, consistently outperforming GRPO-family baselines on OlympiadBench, but relies on LLM-summarized skills without formal guarantees. MATH-VF (May 2025) demonstrates Z3+SymPy step-level verification on MATH500 and ProcessBench but as a one-shot evaluator, not integrated into iterative training. No existing work combines formally-verified skill extraction with iterative diversity-aware self-improvement: the closest are R-Diverse (learned skills, not verified), FOVER (verified, not iterative or skill-aware), and ARISE (skill-aware, not formally verified).

## Proposed Approach

Build a formal skill extractor pipeline that translates each LLM-generated reasoning step into Z3/SymPy formal expressions (extending FoVer's verification methodology and MATH-VF's step-level Z3+SymPy integration) and maps the verified formal operations to a predefined skill taxonomy (~40-60 skills such as quadratic factoring, modular arithmetic, inequality chaining, combinatorial counting) via deterministic pattern matching on the formal AST representation—yielding provably-correct, noise-free skill labels per step. Integrate this extractor into an iterative GRPO-based self-improvement loop (using the verl framework with Qwen3-8B or DeepSeek-R1-0528-Qwen3-8B as base) where curriculum selection at each of 5 training iterations maximizes a skill-space coverage objective over the verified skill distribution rather than relying on surface-level or embedding-based diversity metrics. Specifically, at each iteration, generate candidate problems, produce and formally verify solutions, extract skill coverage vectors, then select training batches that maximize marginal skill-space coverage using a submodular optimization procedure. Evaluate against R-Diverse's SAM-based selection, NSRSA's SymPy-only filtering, and vanilla GRPO baselines on MATH-500, AIME 2024/2025, AMC, and OlympiadBench, measuring both final accuracy and skill coverage breadth across iterations to demonstrate that formally-verified skill diversity prevents curriculum collapse, noise accumulation, and memorization shortcuts simultaneously.

## Detailed Description

We propose Verified Skill Coverage (VSC), a self-improvement framework that uses formally-verified skill decomposition to provide a noise-free diversity signal for math reasoning training curricula. The key insight is that formal verification tools (Z3 for satisfiability and constraint reasoning, SymPy for algebraic operations) can not only verify reasoning step correctness—as in FoVer and NSRSA—but also extract provably-correct skill labels from each verified step through deterministic pattern matching on formal AST representations. We build an iterative GRPO-based training loop where curriculum selection maximizes coverage over this verified skill space, replacing noisy LLM-based diversity metrics (as in R-Diverse's SAM) with exact formal signals. This simultaneously addresses all three documented failure modes of math self-improvement: noise sensitivity (formal verification eliminates the verification noise that Zhu & Kang 2026 showed catastrophically degrades RLVR by 8-10%), curriculum collapse (skill-space coverage prevents the diversity illusion identified by R-Diverse), and memorization shortcuts (step-level skill verification ensures genuine reasoning rather than the Anchor-Adapter circuit exploitation documented in the Spurious Rewards Paradox). Using Qwen3-8B as the base model with the verl framework across 5 self-improvement iterations, we target improvements on MATH-500, AIME 2024/2025, and OlympiadBench while demonstrating sustained skill coverage breadth that existing methods fail to maintain.

## Key References

- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)
- R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training (arXiv 2602.13103, 2026)
- Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards (arXiv 2603.16140, 2026)
- Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs (arXiv 2601.11061, 2026)
- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2603.21558, 2026)
- SAGE: Multi-Agent Self-Evolution for LLM Reasoning (arXiv 2603.15255, 2026)
- ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning (arXiv 2603.16060, 2026)
- Safe: Enhancing Mathematical Reasoning in LLMs via Retrospective Step-aware Formal Verification (ACL 2025)
- Propose, Solve, Verify: Self-Play Through Formal Verification [PSV-Verus] (arXiv 2512.18160, 2025)
- MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2505.20869, 2025)
- DIVE: Diversified Iterative Self-Improvement (arXiv 2501.00747, 2025)
- DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models [GRPO] (arXiv 2402.03300, 2024)

## Resource Estimate

- **manual**: gpu_hours: 2500 H100-hours (5 self-improvement iterations × ~350 GPU-hrs generation + ~150 GPU-hrs GRPO training per iteration, plus baselines/ablations at ~50% overhead), timeline: 3.5-4 months (2 weeks skill extractor development, 6 weeks main experiments, 2 weeks ablations, 2 weeks paper writing), estimated_gpu_cost: $6,250 (at $2.50/hr H100 spot pricing)
- **human_in_loop**: gpu_hours: 2000 H100-hours (AI-assisted hyperparameter search and experiment design reduces wasted runs by ~20%), timeline: 2.5-3 months (AI accelerates skill taxonomy design, code scaffolding, and paper drafting), claude_api_cost: $400-600 (Sonnet 4.6 for code generation, experiment design, and paper drafting at ~150M tokens), estimated_gpu_cost: $5,000
- **auto_research**: gpu_hours: 2200 H100-hours (slightly more than human-in-loop due to exploration overhead in automated ablation sweeps), timeline: 5-6 weeks (parallelized experiment execution, automated evaluation pipelines), claude_api_cost: $800-1200 (heavier API usage for autonomous code generation, debugging Z3/SymPy edge cases, and iterative paper revision), estimated_gpu_cost: $5,500, speed_bottleneck: Formal verification pipeline debugging—Z3/SymPy translation from natural language reasoning steps has long-tail failure modes requiring human judgment on taxonomy boundary cases; also vLLM throughput for 800K+ solution generations per iteration


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "66a41d26-56e7-4675-b2bb-16b862e7997f",
  "type": "user",
  "uuid": "83dc278f-938b-46c3-8ad3-7f7f052ab1f1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T21:00:53.403Z_

```json
{
  "parentUuid": "83dc278f-938b-46c3-8ad3-7f7f052ab1f1",
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
  "uuid": "2ccf111e-7f45-49a3-b7d0-7cbb604259f3",
  "timestamp": "2026-05-27T21:00:53.403Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T21:00:53.403Z_

```json
{
  "parentUuid": "2ccf111e-7f45-49a3-b7d0-7cbb604259f3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a56344ab-9f35-4a9f-baad-aa7daab56d17",
  "timestamp": "2026-05-27T21:00:53.403Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a thorough assessment.…",
  "leafUuid": "a56344ab-9f35-4a9f-baad-aa7daab56d17",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate formally-verified skill coverage for math reasoning",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711"
}
```

---

### Assistant

_source line 8 · 2026-05-27T21:01:19.462Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewer assessments and synthesize them as Meta Judge.

First, let me extract the key numbers:
- Reviewer 1: [18% - 28%] 中位 22%
- Reviewer 2: [22% - 32%] 中位 27%
- Reviewer 3: [20% - 32%] 中位 25%

Median values: 22%, 27%, 25%
Mean of medians: (22+27+25)/3 = 24.67%
Median of medians: 25%


Standard deviation of medians is about 2.05%, which indicates strong consistency across reviewers since it's well below 3%.

Now I'm looking at where the reviewers converge and where they diverge. All three reviewers characterize novelty similarly — ranging from weak to medium — suggesting this is a natural combination rather than a breakthrough innovation.

Beyond novelty, there's striking alignment on several critical vulnerabilities: the noise introduced by translating natural language to formal specifications, the fact that the Anchor-Adapter circuit operates at the reward level rather than the curriculum level, the risk that this is an obvious combination, and the threat that a cheaper alternative using NSRSA plus R-Diverse could achieve similar results. They also all raise concerns about the 40-60 skill taxonomy coverage and note the contradiction in claiming "noise-free" results when the translation process itself introduces noise.

A few references came up in only one or two reviews—RLVεR, Skill1, and Prismatic Synthesis—though Prism appeared across multiple reviewers as a notable omission. Looking at the implementation timeline and resource estimates, the three reviewers' median projections cluster tightly around 22-27% with very low variance, suggesting they're reading the feasibility similarly.

Since all three flagged the same core weaknesses—the novelty concerns, the contradiction around noise-free assumptions, and the memorization claims—the consensus is quite strong despite the individual variations. I'll settle on a range of 20-30% with a median around 24-25%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a56344ab-9f35-4a9f-baad-aa7daab56d17",
  "isSidechain": false,
  "requestId": "req_011CbTkJanpGR4o48tdwXdZD",
  "type": "assistant",
  "uuid": "78b5f21f-ade7-480a-8bb8-1d75c81a6582",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jp6hXVAUaemiDH2mtNFj8u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22559,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2933,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 22559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22559
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

_source line 9 · 2026-05-27T21:02:11.311Z_

【阶段】: Meta Judge
【三次中位】: [22%, 27%, 25%]  std=2.1%
【共识维度】:
- **Novelty = 弱至中**（3/3 一致）：三位审稿人均独立判定核心贡献为"自然组合"（natural/obvious combination），将 FoVer 的形式化验证 + R-Diverse 的 skill-aware diversity + GRPO 迭代训练拼接，缺乏 surprising insight。R1 用"显而易见的空位"，R2 用"自然可预见的下一步"，R3 用"不构成 surprising insight"——措辞不同但判决完全一致。**信号极强。**
- **Significance = 中**（3/3 一致）：问题本身重要且时效性强（2026 上半年最活跃方向之一），但贡献偏工程集成而非科学洞见。三人均指出"如果结果 positive，审稿人会说 makes sense 而非 surprising"。覆盖范围受限于可形式化的数学领域，不推广到 general reasoning。
- **Related Work = 强**（3/3 一致）：覆盖全面准确，差异化定位清晰，所有关键引用经调研验证真实存在。这是 proposal 最突出的维度。
- **"Noise-free" claim 前提假设致命矛盾**（3/3 一致）：NL→formal 翻译步骤本身依赖 LLM，必然引入噪声和覆盖率损失。"noise-free" 只在 Z3/SymPy 验证环节成立，整体管线并非 noise-free。R3 精准总结为"you moved the noise, you didn't eliminate it"。**这是审稿人最容易攻破的点。**
- **Memorization 抑制论证链断裂**（3/3 一致）：Spurious Rewards Paradox 揭示的 Anchor-Adapter 电路是 reward-level 训练动态问题，非 curriculum 组成问题。Skill-diverse training data 无法直接阻止该电路激活。Proposal 声称同时解决三个失败模式，但第三个（memorization）的因果链不成立。
- **Trivial Alternative 威胁真实**（3/3 一致）：NSRSA + R-Diverse SAM 的直接拼接是成本远更低的替代方案，可能达到 80-90% 的效果。Proposal 的增量价值（formal AST skill labels vs. LLM embedding）依赖于"多样性度量噪声是 binding constraint"这一未经验证的假设。
- **40-60 Skill Taxonomy 充分性存疑**（3/3 一致）：竞赛数学的核心难度在于创造性组合和跨领域迁移，预定义刚性 taxonomy 对 AIME/OlympiadBench 级别问题覆盖率存疑。

【异常维度】:
- R3 独自指出遗漏 Skill1 (arXiv 2605.06130, May 2026)——该工作在 agent tasks 而非 math reasoning 领域，相关性有限，降权处理
- R1 独自指出遗漏 RLVεR (arXiv 2601.04411)——理论补充性工作，非致命遗漏
- R3 独自提出 Prismatic Synthesis / Prism-Math (arXiv 2505.20161) 作为额外 baseline 考量——有参考价值但非核心

【最终概率】: [20% - 29%] 中位 24%
【一致性】: 高（std=2.1% < 3%）
【综合理由】:
三位审稿人在所有关键维度上高度一致（std=2.1%），这在独立评审中是极强的收敛信号，说明 proposal 的优缺点都是清晰、稳定可观测的，非主观分歧。

**概率上限受 Novelty 硬约束在 ~29%**：三人一致判定"自然组合"型工作，即使实验执行完美也难以突破。AAAI 对"组合已有技术"类论文的 novelty bar 高于 workshop/findings，审稿人极可能要求展示 emergent insight 而非仅"formal > embedding"的预期结果。

**概率下限 20% 来自三个支撑因素**：(1) Related Work 强保证不会因遗漏关键引用被拒；(2) 问题本身确实重要且时效性强；(3) 如果实验结果显著（>3-5% on AIME），execution quality 可以部分弥补 novelty 不足。

**中位从三人中位的算术均值（24.7%）向下微调至 24%**，原因：三人共识的两个逻辑硬伤（"noise-free" 名不副实 + memorization 因果链断裂）在实际审稿中大概率被同时指出，叠加效应使 soundness 分数受损。高一致性场景下取中位附近但偏严。

**关键判断**：该 proposal 的根本问题不是"做不做得出来"，而是"做出来了审稿人会不会认为这是一篇 research contribution 还是 engineering contribution"。三位审稿人在这一点上的判断完全一致——偏向后者。

【建议】: 不推荐（中位 24% < 36% 阈值，三方高度一致判定 novelty 不足，核心 claim 逻辑链存在两处被共识确认的断裂）

【实施评估】:
  - 计算资源: 2000-2500 H100-hours（5 轮迭代 × ~500 GPU-hrs/轮 + baselines/ablations），预估 GPU 成本 $5,000-$6,250（H100 spot pricing）
  - 数据需求: MATH-500、AIME 2024/2025、AMC、OlympiadBench（均为公开 benchmark）；需自建 skill taxonomy mapping（40-60 skills），依赖 MathCAMPS/STEPS 框架
  - 人工介入: skill taxonomy 的设计和边界定义需要数学领域专家参与；Z3/SymPy 翻译的 long-tail failure modes 需人工判断；预估 2-3 周专家工作量
  - 训练需求: 需要训练——Qwen3-8B 或 DeepSeek-R1-0528-Qwen3-8B 为 base model，5 轮 GRPO 迭代训练（verl 框架），每轮约 150 GPU-hrs 训练 + 350 GPU-hrs 生成
  - 新 Benchmark: 不需要构建全新 benchmark，但需要构建 formal skill extractor pipeline（Z3/SymPy AST pattern matching → skill labels），这是核心工程工作量
  - 预估周期: 2.5-4 个月（2 周 skill extractor 开发，6 周主实验，2 周 ablations，2 周写作）；瓶颈在 formal verification pipeline debugging（NL→formal 翻译的 long-tail failure modes）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78b5f21f-ade7-480a-8bb8-1d75c81a6582",
  "isSidechain": false,
  "requestId": "req_011CbTkJanpGR4o48tdwXdZD",
  "type": "assistant",
  "uuid": "aa9e7e7f-5dea-4a07-ad91-01439fcbd2a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jp6hXVAUaemiDH2mtNFj8u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22559,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2933,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 22559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22559
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a thorough assessment.…",
  "leafUuid": "aa9e7e7f-5dea-4a07-ad91-01439fcbd2a0",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate formally-verified skill coverage for math reasoning",
  "sessionId": "6031105c-bfba-4bc3-9066-7ca7e8d22711"
}
```

---
