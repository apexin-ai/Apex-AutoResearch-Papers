# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/6b291280-c27e-4d0f-a048-8df8254260df.jsonl`
- **Structured JSON:** [`c9a47c82fd55b1b73acd.json`](../../sessions/c9/c9a47c82fd55b1b73acd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T09:10:23.889Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T09:10:23.889Z",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research data to conduct the evaluation. Let me synthesize everything.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **SymHPR (arXiv:2512.03126)**: 最直接竞争者。提出 hierarchical per-primitive rewards (point-on-line F1, line-on-shape L2 等 rule-based metrics)，在 geometric diagram parsing 上实现 98.2% MSE 降低，MathVerse +3%。rule-based，无 formal deduction，无法检测语义矛盾。本 proposal 声称的\"formal vs. rule-based\"差异化相对于 SymHPR 是成立的。\n\n2. **\"Bad Seeing or Bad Thinking?\" (arXiv:2605.14054, May 2026)**: 提出 Perception Verification (PV)——\"blindfolded reasoning\" proxy 独立奖励感知保真度。引入 Structured Verbal Verification 替代高方差 LLM 判断。是 neural proxy，不提供结构化诊断输出。proposal 对其定位准确。\n\n3. **Perception-R1 (arXiv:2506.07218)**: 将 visual perception reward 引入 RLVR，使用 judging LLM 确保视觉内容与生成一致。缺乏 formal grounding。proposal 描述准确。\n\n4. **PDCR (arXiv:2605.13467)**: Perception-Decomposed Confidence Reward，按 perception/reasoning clusters 分解置信度奖励，仍是 scalar confidence。proposal 描述准确。\n\n5. **ViCrit (arXiv:2506.10128, NeurIPS 2025)**: 通过合成幻觉注入创建 verifiable RL proxy task，binary exact-match reward。domain-agnostic 幻觉检测，非 domain-specific formal verification。proposal 描述准确。\n\n6. **GeoDPO (arXiv:2602.22703)**: NL-to-DSL translator 计算 DSL-level rewards。translator 可产生幻觉分数。proposal 描述准确。\n\n7. **SGVR (arXiv:2601.05073)**: Sub-goal verifiable reward 用于 reasoning stage，+9.7%。formal verification 用于推理而非感知。proposal 描述准确。\n\n8. **TrustGeoGen (arXiv:2504.15780)**: Formal-verified data engine，生成 GeoTrust-200K。证明 formal tools 在几何域的成熟度，但目标是数据质量而非 perception reward。proposal 描述准确。\n\n9. **FormalGeo (Symmetry 2024, arXiv:2310.18021)**: CDL 形式语言 + 符号求解器 + FormalGeo7K dataset。FGeo-Parser (Symmetry 2025) 实现 91.5% sentence-level match 但仅 56.5% perfect full-expression accuracy。FGeo-HyperGNet (IJCAI 2025) 整合 FormalGeo 符号系统。生态系统真实且活跃。\n\n10. **EVPV (arXiv:2603.16253)**: Explicit Visual Premise Verification——提取结构化视觉事实到 constraint set，但仍是 neural-based constraint matching 而非 formal theorem-level verification。\n\n11. **TangramSR (arXiv:2602.05570)**: Test-time self-refinement via geometric consistency feedback (IoU 0.63→0.932)，但在连续空间 Tangram 任务上使用 heuristic IoU，非 symbolic Euclidean geometry 的 formal theorem-level verification。\n\n12. **Clinical VLM formal verification (arXiv:2602.24111)**: 将 VLM 输出映射为 SMT constraints 进行 formal verification，架构上最接近本 proposal 的\"感知→符号→formal checking\"思路，但在临床而非几何领域。\n\n- **调研总结**: 2025-2026 年，perception-stage reward 是热门研究方向，已有 6+ 篇并行工作，涵盖 neural judge、rule-based F1、decomposed confidence、proxy task 等多种 reward 机制。Formal verification 在 reasoning-stage (SGVR, FoVer, InternGeometry) 和 data generation (TrustGeoGen) 已被证明有效。但**尚无工作将 formal geometric constraint propagation 应用于 perception-stage reward 并产生结构化诊断输出**。这个 gap 是真实的。FormalGeo CDL 生态成熟，工具链可用，但 VLM→CDL translation 的 56.5% perfect accuracy 是已知瓶颈。\n\n\n【Trivial Alternative 检验】:\n\n存在两个 trivial alternative 威胁：\n\n1. **SymHPR（rule-based F1/L2）已经足够？** SymHPR 用 per-primitive F1/L2 做 structured perception reward，实现成本远低于 formal verification pipeline。核心问题是：formal verification 相比 rule-based F1 的增量有多大？proposal 声称 formal verification 能检测 semantic contradictions (如角度与圆定理矛盾)，而 rule-based F1 不能——但这类\"语义矛盾\"在实际 FormalGeo7K 中占错误的比例是多少？如果大多数 perception error 是简单的数值偏差（rule-based F1 已能捕捉），formal verification 的增量可能有限。proposal 的 M1 pilot study 设计了 error type distribution 分析，这很关键，但目前这个比例是未知的。\n\n2. **Best-of-N + formal filtering 是否够用？** proposal 已主动回应此问题，论点是训练时 internalize constraint awareness 优于测试时 filtering。论证合理但需实证支持——如果 best-of-N (N=5) + formal re-ranking已经非常接近 FPR training 效果，那 training-time reward 的价值就大打折扣。\n\n**增量价值核心**: 在于 diagnostic output → targeted re-perception 这条链路。如果仅论 reward signal 质量，formal vs. rule-based 可能是 marginal improvement；但 diagnostic output 提供了一种质性不同的反馈机制（从\"分数\"到\"诊断\"），这是 scalar reward 方法无法提供的。这个增量价值是否足够，取决于 targeted re-perception 的实际效果。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链: VLM 输出 CDL → FormalGeo 约束传播 → per-fact 诊断 → diagnostic reward 用于 GRPO training / 用于 test-time targeted re-perception\n\n**关键未验证假设**:\n\n1. **CDL translation quality 假设**（最致命）: 整个 pipeline 的前提是 VLM 能产出 syntactically valid CDL。FGeo-Parser 在专门训练的条件下只达 56.5% perfect accuracy。Qwen3-VL-8B 经过 SFT warm-start 后能否达到足够的 FVUR-syntax 率？如果 70%+ rollouts 的 CDL 无效，formal verification 组件几乎不起作用，整个方法退化为 rule-based F1 fallback + 偶尔的 formal reward，本质上变成了 SymHPR 的变体。proposal 设计了 reward curriculum 来缓解，但这仍是一个结构性风险。\n\n2. **Over-determined constraint system 假设**: proposal 假设几何问题通常有 over-determined constraint system，单个错误事实会传播为可检测矛盾。但 missing-primitive errors（完全漏检一个点/线）不产生矛盾，只产生信息不足。如果 VLM 的主要感知错误是 missing-primitive 而非 numeric/relational error，formal verification 的覆盖率会很低。DYR (Diagnostic Yield Rate) 可能远低于预期。\n\n3. **VLM 能利用结构化诊断反馈进行 targeted re-perception 假设**: 告诉 VLM \"∠ABC=90° 与 inscribed angle theorem 矛盾——请重新检查 ∠ABC\"，VLM 就能有效修正——这假设 VLM 在 re-prompting 下能做出有意义的修正，而不是随机改变输出。这个能力在当前 VLM 上未经验证。如果 VLM 在 re-perception 后准确率无显著提升，targeted re-perception 这一核心应用就会失效。\n\n4. **FormalGeo7K 数据规模假设**: 7K 训练样本对 GRPO training 是否足够？proposal 提到可扩展到 133K+ 但这增加了工程复杂度。\n\n以上假设中，#1 和 #2 共同决定了 formal verification 组件在训练中的实际触发率和覆盖率——如果两者都偏悲观（CDL 无效率高 + 主要错误类型不可检测），proposal 的核心贡献会被严重削弱。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 核心 gap 是真实的：确认无现有工作将 formal geometric constraint propagation 应用于 perception-stage reward 并产生结构化诊断输出（调研 12 篇最相关工作均不覆盖此交叉点）。然而，novelty 的性质偏向 \"natural next step\"——formal verification 已在 reasoning stage 成功 (SGVR, FoVer, InternGeometry)，perception-stage reward 是活跃方向 (6+ 并行工作)，FormalGeo CDL 工具链成熟——将三者组合是相对 obvious 的延伸。Diagnostic output → targeted re-perception 链路提供了超越简单组合的质性新机制，这提升了 novelty，但核心仍是\"已有工具在新 stage 的应用\"。对比 SymHPR (arXiv:2512.03126) 的 rule-based structured reward，FPR 的差异化在于 formal guarantee + diagnostic output，这是有实质的但不是 paradigm shift。\n\n2. **Significance: 中** — 几何感知瓶颈是真实且重要的问题（GPT-4o 70% error rate, SVE-Math arXiv:2501.06430）。但方法的 generalizability 受限：(a) 仅适用于 FormalGeo CDL 兼容的几何问题子集；(b) 依赖特定工具链（FormalGeo solver, CDL 语法）；(c) FormalGeo7K 规模有限。将 formal verification 思路从 reasoning → perception 的方向性贡献有一定影响力，但狭窄的领域适用范围限制了整体 significance。如果论文能在实验中充分展示 diagnostic output 和 targeted re-perception 的独特价值（相对于 scalar reward 的质性优势），significance 可以有所提升。\n\n3. **Related Work: 强** — proposal 对领域覆盖极为全面，引用了 25+ 篇 2024-2026 的相关工作，涵盖感知 reward (6 种方法)、推理 formal verification (4 种方法)、数据生成 (TrustGeoGen)、工具链 (FormalGeo, AlphaGeometry2)、test-time self-correction (TangramSR, GeoSketch)。经调研验证，所有引用论文真实存在，描述基本准确。差异化定位通过详细对比表清晰呈现。对 FGeo-Parser 的局限性描述准确（91.5% sentence-level, 56.5% perfect）。这是一个在 related work 层面做得非常扎实的 proposal。\n\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】: \n- Novelty 为\"中\"：gap 真实但偏 natural combination，非 surprising insight → 限制上界在 ~38%\n- Significance 为\"中\"：domain-specific，generalizability 受限 → 进一步限制上界\n- Related Work 为\"强\"：覆盖全面准确 → 提供了下限保障（不会因 positioning 不足被拒）\n- CDL translation bottleneck 是结构性风险：如果 formal verification 实际触发率低，整个方法退化为 SymHPR 变体，核心贡献不成立。这个风险同时压低了 novelty 的可信度（\"novelty 成立但可能在实践中 irrelevant\"是一种特别难辩护的局面）\n- 限制上界的主要维度是 Novelty（natural combination）和 Significance（narrow domain）的交叉效应\n\n【主要风险】:\n1. **CDL translation bottleneck 导致核心贡献空转**: 如果 SFT warm-start 后 FVUR-syntax 仍然低（<50%），formal verification 组件在大部分 rollouts 中不触发，整个方法在实践中退化为 rule-based F1 fallback，核心 novelty claim（formal diagnostic reward）变得 marginal。审稿人会问：\"FPR 的提升到底来自 formal verification 还是来自 rule-based F1 fallback？\"\n2. **与 SymHPR 的 marginal improvement**: 如果 ablation A1 (formal vs. rule-based F1) 显示差异不显著，审稿人会认为 formal verification 的复杂性不 justified——增加了 FormalGeo solver 依赖、CDL translation 开销、reward curriculum 复杂度，但性能提升有限。这是 \"engineering complexity without sufficient empirical payoff\" 的经典拒稿理由。\n```\n\nSources:\n- [SymHPR - Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)\n- [Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)\n- [Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward](https://arxiv.org/abs/2506.07218)\n- [PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning](https://arxiv.org/html/2605.13467)\n- [ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs](https://arxiv.org/abs/2506.10128)\n- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/pdf/2602.22703)\n- [SGVR: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward](https://arxiv.org/pdf/2601.05073)\n- [TrustGeoGen: Formal-Verified Data Engine](https://arxiv.org/abs/2504.15780)\n- [FormalGeo: An Extensible Formalized Framework](https://arxiv.org/html/2310.18021v6)\n- [FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems](https://www.mdpi.com/2073-8994/17/1/8)\n- [EVPV: Grounding the Score](https://arxiv.org/html/2603.16253)\n- [TangramSR: Can VLMs Reason in Continuous Geometric Space?](https://arxiv.org/pdf/2602.05570)\n- [Toward Guarantees for Clinical Reasoning in VLMs via Formal Verification](https://arxiv.org/pdf/2602.24111)\n- [SVE-Math: Open Eyes, Then Reason](https://arxiv.org/abs/2501.06430)\n- [ACL 2026 Geometry Survey paper list](https://github.com/majianz/dl4gps)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [SymHPR] (arXiv:2512.03126, Dec 2025): Hierarchical per-primitive rewards (point-on-line, line-on-shape F1/L2) via symbolic auto-encoder. Rule-based, not formally grounded, no semantic contradiction detection. Proposal's most direct structural-perception-reward competitor — FPR claims formal guarantees over SymHPR's rule-based metrics. Proposal's characterization accurate.\n- [GeoDPO] (arXiv:2602.22703, Feb 2026): NL-to-DSL translator computes DSL-level reward for geometric perception RL. Demonstrates DSL-mediated perception reward is viable. Achieves +26.5% in-domain, +8.0% OOD, +39.0% downstream. Key precedent: translator-mediated reward signals work, but translator hallucination is a real issue. Proposal's characterization accurate.\n- [\"Bad Seeing or Bad Thinking?\"] (arXiv:2605.14054, May 2026): Decomposes generation into interleaved perception/reasoning steps; Perception Verification (PV) via \"blindfolded reasoning\" proxy rewards perception fidelity independently. Neural proxy, no formal guarantee, no per-fact diagnosis. Very recent, directly addresses perception credit assignment. Proposal's characterization accurate.\n- [PDCR] (arXiv:2605.13467, May 2026): Decomposes confidence-based rewards by perception/reasoning skill clusters, normalizes advantages within each cluster. Still scalar confidence, no structural diagnosis. Proposal's characterization accurate.\n- [ViCrit] (arXiv:2506.10128, Jun 2025, NeurIPS 2025): Synthetic hallucination injection → binary exact-match reward for perception RL. Domain-agnostic, validates verifiable perception rewards concept. Proposal's characterization accurate.\n- [Perceval] (arXiv:2604.24583, Apr 2026): **NOT CITED IN PROPOSAL.** Perception-centric PRM with token-level error grounding — extracts image-related claims, compares one-by-one with visual evidence, returns claims containing perceptual errors. Enables targeted correction at test time (truncate erroneous span → re-generate). Functionally very similar to FPR's \"diagnostic output + targeted re-perception\" but via neural PRM, not formal verification. This is a significant omission.\n- [VPPO] (approx. arXiv 2510.09285, ICLR 2026 Spotlight): First multimodal RL algorithm to formally identify perceptually pivotal tokens via dependency analysis for targeted optimization. 7B model achieves 19.2% improvement. **NOT CITED IN PROPOSAL.** Another approach that targets perception tokens specifically for RL, though via dependency analysis rather than formal constraint verification.\n- [SPARC] (arXiv:2602.06566, Feb 2026): Modular decoupling of perception and reasoning circuits for test-time scaling. Supports asymmetric compute allocation. Not directly a reward method but demonstrates perception-reasoning separation architecture.\n- [FGeo-Parser] (Symmetry 2025): CDL autoformalization achieves 91.5% sentence-level match, but only 56.5% perfect full-expression accuracy. This is the translator FPR depends on — the gap between 91.5% and 56.5% reveals the CDL translation bottleneck is severe.\n- [TrustGeoGen] (arXiv:2504.15780): Formal verification for geometric data generation (GeoTrust-200K). Demonstrates formal tools' maturity but for data generation, not perception rewards. Proposal's characterization accurate.\n- [FormalGeo] (Symmetry 2024, arXiv:2310.18021): Extensible formalized framework using GDL/CDL for Euclidean geometry. Core infrastructure FPR depends on. Real and well-maintained.\n\n- **调研总结**: The perception-reward-for-VLM-geometric-reasoning space has exploded in early 2026, with at least 6-7 concurrent methods (GeoDPO, Perception-R1, \"Bad Seeing or Bad Thinking?\", PDCR, ViCrit, Perceval, VPPO) all targeting the same problem from different angles. Formal verification has been applied to the reasoning stage (SGVR, FoVer, InternGeometry) and to data generation (TrustGeoGen), but NOT yet to the perception stage — this gap is real. However, Perceval (arXiv:2604.24583) already achieves functionally similar capabilities (per-claim error identification + targeted test-time correction) via neural PRM without formal methods, narrowing FPR's practical novelty to the \"formal guarantee\" aspect.\n\n【Trivial Alternative 检验】:\n\n**Yes, there are simpler alternatives that partially cover FPR's value proposition:**\n\n1. **Best-of-N + formal re-ranking** (acknowledged in proposal): The proposal argues training-time rewards internalize constraint awareness while test-time filtering cannot. This argument is reasonable but not bulletproof — recent test-time scaling work (SPARC, Perceval) shows substantial gains from test-time-only methods.\n\n2. **Perceval-style neural PRM + targeted correction** (NOT acknowledged): Perceval already achieves per-claim error identification and targeted re-generation at test time without any formal verification infrastructure, CDL translation, or domain-specific tooling. If Perceval achieves competitive perception error correction rates, FPR's incremental value reduces to \"formal guarantee on the subset of outputs with valid CDL\" — a much narrower contribution.\n\n3. **GeoDPO's existing DSL-mediated reward**: GeoDPO already uses a translator to compute DSL-level perception rewards and achieves strong results (+26.5% in-domain). FPR's incremental value over GeoDPO is the formal constraint checking and diagnostic output, but both share the translator bottleneck.\n\n**Incremental value of FPR**: The genuine increment is (a) zero-false-positive formal guarantee (conditional on valid CDL), and (b) theorem-level diagnostic explanations (not just \"this claim is wrong\" but \"this claim contradicts inscribed angle theorem\"). Whether this increment justifies the engineering complexity (CDL translator + FormalGeo integration + reward curriculum) is debatable.\n\n【前提假设检验】:\n\nThe core claim's logic chain has several unverified assumptions:\n\n1. **\"CDL translation will be accurate enough for formal verification to be meaningful\"** — This is the most critical assumption. FGeo-Parser achieves only 56.5% full-expression accuracy. If the VLM's CDL output is frequently syntactically invalid or semantically wrong-but-valid, formal verification either doesn't apply (invalid CDL → fallback to rule-based F1, losing the formal advantage) or verifies the wrong thing (valid but inaccurate CDL → formal checker validates translator errors, not perception errors). The proposal's mitigation (SFT warm-start + reward curriculum) is reasonable but unproven — there's no evidence that RL training on FormalGeo7K will push CDL accuracy high enough for formal rewards to dominate.\n\n2. **\"Geometric problems are typically over-determined, so single-fact errors produce detectable contradictions\"** — This is stated as fact but is actually a hypothesis that needs empirical validation. The proposal acknowledges missing-primitive errors may not produce contradictions, but doesn't quantify how common under-determined configurations are. If a large fraction of perception errors are \"silent\" (don't trigger contradictions), the Diagnostic Yield Rate (DYR) will be low, and formal verification coverage will be poor. The M1 pilot study is designed to test this, which is good — but this means the entire project's viability hinges on an untested empirical assumption.\n\n3. **\"Diagnostic output enables meaningfully better re-perception than generic re-prompting\"** — The claim that telling a VLM \"∠ABC=90° contradicts inscribed angle theorem\" leads to better correction than \"re-examine this region\" is intuitive but unproven. VLMs may not effectively leverage formal theorem citations in re-perception prompts. The actual mechanism by which a VLM uses this diagnostic information to \"look again more carefully\" is underspecified.\n\n4. **\"Training-time formal rewards internalize geometric constraint awareness better than test-time filtering\"** — This is the argument against the best-of-N trivial alternative. It's plausible but could go either way empirically.\n\n【3 维度打分】:\n\n1. **Novelty: 中** — The gap (formal verification for perception-stage rewards) is real — no existing work applies formal constraint propagation to generate diagnostic perception rewards. The contribution chain (formal guarantee → diagnostic output → targeted re-perception) is logically coherent and each step enables the next. However, several factors limit the novelty assessment:\n   - The approach is fundamentally a *recombination* of existing components (FormalGeo's constraint propagation + GRPO training + perception-stage reward) rather than a new technique. The individual pieces all exist; the novelty is the specific integration.\n   - Perceval (arXiv:2604.24583, NOT CITED) already achieves functionally similar capabilities (per-claim error grounding + targeted test-time correction) via neural methods. FPR's formal guarantee is a genuine differentiator, but the practical novelty narrows significantly.\n   - The \"from scoring to diagnosing\" shift is real but incremental — Perceval also diagnoses (identifies specific erroneous claims), just without formal theorem citations.\n   - Within the geometric domain specifically, GeoDPO already uses translator-mediated DSL-level rewards; FPR adds formal checking on top of a similar translator pipeline.\n\n2. **Significance: 弱偏中** — Several factors limit significance:\n   - **Domain restriction**: Only works for Euclidean geometry problems with FormalGeo's CDL formalism. Cannot generalize to other visual math domains (charts, tables, physics diagrams) without equivalent formal systems. FormalGeo7K is ~7K problems — small even for the geometric domain.\n   - **CDL translator bottleneck**: The approach's effectiveness is capped by CDL translation accuracy (56.5% full-expression). Even with improvements, the formal reward only applies to the subset of syntactically valid CDL outputs, meaning the system often falls back to rule-based F1 — reducing FPR to SymHPR + occasional formal bonus.\n   - **Impact ceiling**: Even if all results are positive, the contribution is \"formal verification improves perception rewards in the specific case of Euclidean geometry\" — a correct but narrow finding. The broader lesson (\"domain-specific formal tools can improve perception rewards\") is interesting but requires the existence of such formal tools in each target domain.\n   - **\"Surprising if positive?\" test**: If FPR outperforms SymHPR by a few points on geometric perception benchmarks, most reviewers would say \"expected — formal verification is more precise than heuristic F1.\" The more interesting finding would be if targeted re-perception shows large gains, but that's the more uncertain component.\n\n3. **Related Work: 中偏弱** — The proposal demonstrates thorough awareness of the perception-reward landscape (GeoDPO, Perception-R1, PV, PDCR, ViCrit, SymHPR) and the formal-verification-for-reasoning landscape (SGVR, FoVer, InternGeometry, TrustGeoGen). The comparison table is well-constructed and the differentiation is clearly articulated. However:\n   - **Critical omission: Perceval** (arXiv:2604.24583, Apr 2026) — perception-centric PRM with token-level error grounding and targeted test-time correction. This is arguably the closest functional competitor to FPR's diagnostic + re-perception pipeline, and its absence weakens the novelty claim.\n   - **Critical omission: VPPO** (ICLR 2026 Spotlight) — formally identifies perceptually pivotal tokens for targeted RL optimization. Directly relevant to the \"targeted perception reward\" theme.\n   - **Missing SPARC** (arXiv:2602.06566) — perception-reasoning decoupling for test-time scaling, relevant to the targeted re-perception mechanism.\n   - These omissions are partially understandable given the field's rapid pace (Perceval appeared April 2026), but they represent real gaps in the competitive landscape analysis.\n\n【概率估计】: [18% - 28%] 中位 23%\n\n【估计理由】: \nNovelty 为\"中\"而非\"强\"——核心贡献是将已有技术（FormalGeo 约束传播）应用到新场景（感知阶段奖励），且 Perceval 已通过神经方法实现了功能相似的\"逐 claim 诊断 + 定向修正\"能力，显著压缩了 FPR 的独特价值空间。Significance 为\"弱偏中\"——受限于 Euclidean geometry 单一领域、FormalGeo7K 数据规模（~7K）、以及 CDL 翻译器瓶颈（56.5% 完全准确率），使得即使结果 positive，影响范围也较窄，且核心发现（formal verification 比 rule-based F1 更精确）对审稿人来说并不 surprising。Related Work 遗漏了 Perceval 和 VPPO 两个直接竞争者。**上界主要受 Significance 限制**——领域窄 + CDL 瓶颈使得即便 idea 完全成立，论文的 impact 也难以达到 AAAI 的 acceptance bar。中位 23% 反映了一个\"方向正确、gap 真实存在、但内核偏窄且不够 surprising\"的 idea。\n\n【主要风险】:\n1. **CDL 翻译器瓶颈导致形式化验证有效覆盖率低**: 56.5% 的完全准确率意味着大量 rollout 要么无法进入形式化验证（语法无效），要么验证的是翻译器的错误而非 VLM 感知的错误。这使得 FPR 在实践中可能退化为\"SymHPR + 偶尔的 formal bonus\"，削弱核心 novelty claim 的实验验证。\n2. **Perceval 等神经方法已实现功能等价的\"诊断 + 定向修正\"**: 如果 Perceval 在相同 benchmark 上取得有竞争力的结果且不需要领域特定的形式化工具，审稿人可能质疑 FPR 的工程复杂度是否 justified——formal guarantee 的理论优势在实践中可能无法转化为显著的性能优势。\n```\n\nSources:\n- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)\n- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning](https://arxiv.org/abs/2602.22703)\n- [Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)\n- [PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning](https://arxiv.org/abs/2605.13467)\n- [ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs](https://arxiv.org/abs/2506.10128)\n- [Perceval: Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583)\n- [SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs](https://arxiv.org/abs/2602.06566)\n- [SGVR: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)\n- [FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving](https://arxiv.org/abs/2310.18021)\n- [FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems](https://www.mdpi.com/2073-8994/17/1/8)\n- [TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving](https://arxiv.org/abs/2504.15780)\n- [EVPV: Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models](https://arxiv.org/abs/2603.16253)\n- [VPPO: Spotlight on Token Perception for Multimodal Reinforcement Learning](https://arxiv.org/abs/2510.09285)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research data. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [SymHPR] (arXiv:2512.03126, 2025): 最接近的感知奖励工作。提出层次化过程奖励模型，使用per-primitive F1/L2指标（point-on-line、line-on-shape、shape-on-relation），在几何图解析上取得显著提升（MathGlance +13%）。但为rule-based指标，不涉及形式化定理级验证，无法检测语义矛盾（如角度与圆定理不一致）。\n- [GeoDPO] (arXiv:2602.22703, 2026): 通过NL-to-DSL translator计算DSL级reward信号用于RL训练。与本proposal最直接竞争——同样试图在感知阶段提供结构化奖励。但translator可能产生hallucination，且reward是scalar而非diagnostic。GeoPerceive benchmark来自此工作。\n- [\"Bad Seeing or Bad Thinking?\"] (arXiv:2605.14054, 2026): 通过\"blindfolded reasoning\" proxy独立奖励感知保真度（PV机制），明确分解perception与reasoning步骤。但PV仍为neural proxy，只报告\"perception unreliable\"，不诊断具体哪个事实违反哪个约束。\n- [PDCR] (arXiv:2605.13467, 2026): 分解confidence reward为感知/推理cluster，解决全局reward混合信号退化问题。但仍为scalar confidence，无结构化诊断。\n- [ViCrit] (arXiv:2506.10128, NeurIPS 2025): 通过合成hallucination注入+二元精确匹配构建可验证RL代理任务。验证了可验证感知奖励的有效性，但使用domain-agnostic幻觉检测，非domain-specific几何形式化验证。\n- [SGVR] (arXiv:2601.05073, 2026): 将形式化验证应用于推理阶段的sub-goal验证，+9.7%。证明形式化验证作为RL reward的有效性，但仅限推理阶段。\n- [FoVer] (ACL 2026 Findings, arXiv:2505.15960): 形式化验证用于step-level PRM数据合成。同样限于推理阶段。\n- [TrustGeoGen] (arXiv:2504.15780, 2025): 使用形式化验证生成几何数据（GeoTrust-200K），证明形式化工具在几何领域的成熟度。但目标是数据质量而非感知奖励。\n- [FGeo-Parser] (Symmetry 2025): FormalGeo CDL的自动formalization工具。句子级匹配准确率91.51%，但完整表达式准确率仅56.47%——直接印证proposal中CDL translator瓶颈。\n- [Sieve / Iterative Evidence Refinement] (arXiv:2603.14117, 2026): 通过内部表征re-engage图像证据进行迭代精炼，+8%。概念上与targeted re-perception相关，但使用注意力引导而非形式化约束诊断。\n- [TangramSR] (arXiv:2602.05570, 2026): 基于几何一致性反馈(IoU)实现test-time self-refinement (0.63→0.932)。但使用启发式IoU在连续空间任务上，非形式化定理级验证。\n\n- 调研总结: 2025-2026年，几何感知奖励领域极度活跃，已有7+工作从不同角度提供感知阶段reward（neural judge、learned translator、rule-based F1、decomposed confidence、blindfolded proxy、synthetic hallucination）。形式化验证已在推理阶段(SGVR/FoVer/InternGeometry)和数据生成(TrustGeoGen)被验证有效，但确实尚无工作将formal verification应用于perception阶段作为reward信号。这个gap是真实存在的。\n\n【Trivial Alternative 检验】:\n最直接的trivial alternative是**Best-of-N + formal verification re-ranking**：让VLM生成N个CDL候选，用FormalGeo过滤掉有矛盾的。这不需要任何训练改动，成本极低。Proposal已意识到并做了回应（training-time reward可将约束意识内化），但这个论证需要实验验证，不是逻辑上自明的。\n\n第二个alternative是**SymHPR的rule-based F1 + heuristic contradiction checking**：不需要CDL translator这个瓶颈环节，直接在primitive level做rule-based检查。与本proposal的增量价值在于：(1) formal guarantee（zero false positive on valid CDL），(2) 能检测语义级矛盾（angle与circle theorem不一致），(3) diagnostic output。其中(2)和(3)是真实的增量价值，(1)的条件限定\"on valid CDL\"是关键——如果CDL有效率低，这个guarantee的实际覆盖面就小。\n\n**增量价值判断**：diagnostic output（从scoring到diagnosing的质变）和targeted re-perception（被诊断信息启用的新机制）是本proposal超越trivial alternatives的真实贡献。但这两个贡献的实际价值高度依赖于CDL translator质量。\n\n【前提假设检验】:\n1. **CDL translator将足够频繁地生成语法有效的CDL**：这是最关键的未验证假设。FGeo-Parser完整表达式准确率仅56.47%，即使经过SFT warm-start，FVUR-syntax（进入solver的有效CDL比例）是否能达到使formal reward有意义的水平，完全未知。Proposal设计了reward curriculum作为缓冲，但如果Phase 3永远到不了（formal dominant），整个方法就退化为rule-based F1 + 偶尔的formal reward。\n2. **几何问题的约束系统足够over-determined，使单个错误事实可被检测**：Proposal承认了missing-primitive错误无法检测，但对\"numeric/relational error导致可检测矛盾\"的比例完全是假设性的——M1 pilot study正是为此设计的，说明authors自己也认为这需要验证。\n3. **Diagnostic output对targeted re-perception的实际帮助**：假设VLM能理解\"∠ABC=90°与inscribed angle theorem矛盾\"这样的诊断并有效re-examine。这假设VLM有足够的geometric reasoning能力来利用诊断信息，而如果VLM的感知错误本身就是因为\"看不清图\"，给它更详细的verbal指令未必有帮助。\n\n【3 维度打分】:\n\n1. **Novelty: 中偏强** — 核心贡献\"将formal verification从reasoning阶段迁移到perception阶段，并提供diagnostic（而非scalar）reward output\"在调研中确认无先例。与最近期7+竞争工作（SymHPR、GeoDPO、Perception-R1、PV、PDCR、ViCrit等）的差异化真实存在——所有现有工作提供scoring信号，无一提供per-fact diagnostic output with formal guarantee。这不仅是\"tool X applied to problem Y\"，diagnostic→targeted re-perception的enabling chain是质变。但降分因素：(a) 从reasoning-stage formal verification到perception-stage formal verification的迁移思路较为自然，审稿人可能认为是logical extension而非surprising insight；(b) 对FormalGeo/DDAR现有工具的依赖较重，方法层面的原创技术贡献（vs. 工程整合贡献）需要clarify。\n\n2. **Significance: 中** — 感知瓶颈确实重要（GPT-4o 70%错误率，SVE-Math），且本proposal聚焦的\"诊断性反馈\"概念有超越几何领域的潜在影响。但限制因素：(a) 方法仅适用于有formal specification的几何问题（依赖CDL/FormalGeo），不可直接推广到其他视觉数学领域或通用视觉推理；(b) FormalGeo7K数据规模小（7K），evaluation在geometry-specific benchmarks上，影响面窄；(c) 如果CDL translator瓶颈严重，实际改善可能有限。\n\n3. **Related Work: 强** — 这是proposal最突出的维度。覆盖了2025-2026年几乎所有相关工作（7个perception reward方法、3个formal verification for reasoning方法、数据生成、test-time refinement等），差异化表格清晰明确，每个竞争工作的局限性分析准确（经调研验证）。唯一可补充的是Sieve (arXiv:2603.14117) 的iterative evidence refinement和formal verification for clinical reasoning (arXiv:2602.24111)。\n\n【概率估计】: [28% - 38%] 中位 33%\n\n【估计理由】:\nNovelty中偏强（diagnostic formal verification for perception是真实gap）+ Significance中（重要问题但scope窄）+ Related Work强（极佳的定位和覆盖）→ 整体idea质量落在\"有实质内核，方向正确，有真实novelty delta\"的区间。核心发现如果positive（formal diagnostic reward显著优于scalar reward），审稿人反应可能介于\"makes sense, good engineering\"和\"interesting, the diagnostic mechanism is a useful new paradigm\"之间——不太可能说\"I would have guessed this\"也不太可能说\"surprising\"。这将其锚定在25-35%区间偏上。\n\n上界受限于：(a) Novelty的\"natural extension\"感知风险——从reasoning-stage formal verification到perception-stage formal verification的跳跃幅度，部分审稿人可能认为不够大；(b) Significance被scope限制（仅geometry + FormalGeo生态）。下界由强related work覆盖和真实的diagnostic novelty支撑。\n\n【主要风险】:\n1. **\"Engineering integration vs. research contribution\"质疑**：审稿人可能认为核心贡献是将现有工具（FormalGeo solver）应用于新场景（perception reward），方法层面的原创技术贡献不足，更接近systems paper而非methods paper。\n2. **CDL translator假设的脆弱性削弱idea可信度**：即使在idea评估层面（不考虑实验），审稿人在reading时就会注意到56.47%的full-expression accuracy，可能质疑\"如果近一半的CDL都是invalid的，formal guarantee的实际意义有多大？\"这不是执行层面的问题，而是idea logic chain中的薄弱环节。\n```\n\nSources:\n- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)\n- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/abs/2602.22703)\n- [Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)\n- [PDCR: Perception-Decomposed Confidence Reward](https://arxiv.org/abs/2605.13467)\n- [ViCrit: A Verifiable RL Proxy Task for Visual Perception](https://arxiv.org/abs/2506.10128)\n- [SGVR: Milestones over Outcome](https://arxiv.org/abs/2601.05073)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [TrustGeoGen: Formal-Verified Data Engine](https://arxiv.org/abs/2504.15780)\n- [FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems](https://www.mdpi.com/2073-8994/17/1/8)\n- [Perception-R1: Advancing Multimodal Reasoning via Visual Perception Reward](https://arxiv.org/abs/2506.07218)\n- [Sieve: Improving Visual Reasoning with Iterative Evidence Refinement](https://arxiv.org/abs/2603.14117)\n- [TangramSR: VLMs Reasoning in Continuous Geometric Space](https://arxiv.org/abs/2602.05570)\n- [EVPV: Grounding the Score](https://arxiv.org/abs/2603.16253)\n- [FormalGeo Framework](https://formalgeo.github.io/)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning\n\n## Core Problem\n\nHow can we provide formally verifiable, diagnostic reward signals for the visual perception stage of multimodal geometric reasoning — signals that pinpoint which specific geometric fact is wrong, explain why it contradicts known geometric constraints, and enable targeted correction at test time?\n\n## Research Opportunity\n\nCurrent RL approaches for visual math perception produce opaque reward signals that cannot diagnose specific perception errors:\n- **GeoDPO** (arXiv:2602.22703): Learned NL-to-DSL translator computes DSL-level rewards; translator can hallucinate scores.\n- **Perception-R1** (arXiv:2506.07218): Judge LLM provides visual perception rewards; lacks formal grounding.\n- **\"Bad Seeing or Bad Thinking?\"** (arXiv:2605.14054): Perception Verification (PV) via blindfolded reasoning proxy independently rewards perception fidelity — but remains a neural proxy that reports \"perception unreliable\" without diagnosing which fact conflicts with which constraint.\n- **\"From Seeing to Thinking\"** (arXiv:2605.20177): Shows perception improves more via RL than caption-based SFT, but uses only generic rewards.\n- **PDCR** (arXiv:2605.13467): Decomposes confidence rewards by perception/reasoning clusters — but still scalar confidence, no structural diagnosis.\n- **SymHPR** (arXiv:2512.03126): Hierarchical per-primitive rewards (point-on-line, line-on-shape F1/L2), closest to structured perception feedback — but rule-based metrics without formal deduction. Cannot detect semantic contradictions (e.g., angle inconsistent with circle theorem), and F1 can be noisy when primitive extraction itself errs.\n- **ViCrit** (arXiv:2506.10128, NeurIPS 2025): Verifiable RL proxy task via synthetic hallucination injection with binary exact-match reward — validates verifiable perception rewards but uses domain-agnostic hallucination detection, not domain-specific formal geometric verification.\n\nFormal verification for reasoning-stage rewards has proven effective — SGVR (arXiv:2601.05073, +9.7%), Safe (arXiv:2506.04592), FoVer (ACL 2026 Findings, arXiv:2505.15960), InternGeometry (arXiv:2512.10534) — but none applies formal verification to the perception stage. TrustGeoGen (arXiv:2504.15780) uses formal verification for geometric data generation (GeoTrust-200K), demonstrating formal tools' maturity in the geometric domain, but targets data quality rather than perception reward signals. FormalGeo (Symmetry 2024, arXiv:2310.18021) and AlphaGeometry2's DDAR engine (JMLR 2025, C++ implementation 300x faster) now make symbolic constraint checking at scale feasible. The ACL 2026 geometry survey (arXiv:2507.11936) identifies formal language representations and automated verification as critical open challenges.\n\n**The key gap all existing perception reward methods share:** they produce scalar/per-step scoring signals. None generates structured diagnostic output identifying which specific fact contradicts which geometric constraint, with formal correctness guarantees. This diagnostic capability enables a qualitatively new mechanism — targeted re-perception — that no scoring-based approach can support.\n\n## Proposed Approach\n\nWe propose FormalPerceptReward (FPR), the first framework using formal geometric constraint propagation to generate diagnostic reward signals for perception-stage RL training, enabling targeted re-perception at test time.\n\n**Core contribution chain** (each enabling the next):\n1. **Formally guaranteed reward precision** (foundation): When VLM-produced CDL is syntactically valid, FormalGeo's constraint propagation detects contradictions that are logically provable — zero false positives. This guarantee does not hold for neural judges (which hallucinate), rule-based F1 (which produces noisy scores from imperfect primitive extraction), or neural proxies (which can misjudge).\n2. **Actionable diagnostic output** (core novelty): Beyond scoring, FPR produces per-fact structured diagnostics: \"∠ABC=90° contradicts A on circle with diameter BC by the inscribed angle theorem.\" This is a qualitative shift from scoring to diagnosing — no existing perception reward method provides this.\n3. **Targeted re-perception at test time** (enabled application): Diagnostic output supports selective re-examination of specific erroneous facts rather than full-diagram re-processing.\n\n**Why training-time formal reward, not just test-time formal filtering?** One might ask whether best-of-N sampling + formal verification re-ranking suffices. Training-time formal rewards internalize geometric constraint awareness into the model, improving single-pass perception quality. Test-time filtering cannot teach the model what constitutes formally consistent perception; it only selects among existing outputs. Moreover, best-of-N compute scales linearly with N, while trained models deliver better base quality at fixed inference cost.\n\n**Pipeline.** Qwen3-VL-8B outputs structured geometric facts in FormalGeo's Conditional Declaration Language (CDL). FormalGeo's symbolic solver performs constraint propagation, producing per-fact diagnostic rewards. These replace learned neural judges in GRPO training on FormalGeo7K (~7K annotated problems).\n\n**Translator feasibility.** Converting visual perception to syntactically valid CDL is non-trivial. FGeo-Parser (Symmetry 2025) achieves 91.5% sentence-level match accuracy but only 56.5% perfect full-expression accuracy on FormalGeo data. Mitigation:\n- SFT warm-start: Fine-tune Qwen3-VL-8B on FormalGeo7K ground-truth CDL before GRPO\n- Graceful degradation: Syntactically invalid CDL receives fixed low reward + rule-based F1 fallback\n- Reward curriculum: Phase 1 (rule-based F1 dominant, CDL quality low) → Phase 2 (mixed, formal weight rises with FVUR-syntax) → Phase 3 (formal dominant). Transition governed by FVUR-syntax monitoring.\n\n**Formally detectable error types.** Geometric problems typically feature over-determined constraint systems where a single incorrect fact (e.g., a misread angle) propagates into detectable contradictions. However, missing-primitive errors (e.g., failing to detect a point entirely) may not produce contradictions — only information insufficiency. The M1 pilot study (below) will quantify the proportion of each error type and calibrate expectations for formal verification coverage.\n\n**Formal verification engine.** FormalGeo's symbolic solver is the primary engine (native CDL). AlphaGeometry2's C++ DDAR (300x faster, JMLR 2025) provides optional deeper deduction for multi-step theorem applications, with CDL-to-DDAR predicate conversion validated for accuracy (concordance >90% required; if not met, DDAR is dropped). DDAR's incremental value tested via ablation.\n\n**Targeted re-perception protocol (test time):**\n1. VLM extracts facts → FormalGeo solver identifies contradictions with constraint explanations\n2. Contradictions ranked by severity; top-k (k=1–2) flagged per round\n3. Re-prompt VLM: \"∠ABC was extracted as 90° but contradicts [constraint] — re-examine ∠ABC\"\n4. Re-run constraint checking on updated facts\n5. Terminate: no new contradictions OR facts unchanged OR max 3 rounds\n\n## Research Landscape\n\nThe perception bottleneck is well-documented: GPT-4o exhibits 70% error rate on geometric primitive grounding (SVE-Math, arXiv:2501.06430). CogFlow (ICLR 2026, arXiv:2601.01874) bridges perception and reasoning through knowledge internalization. EVPV (arXiv:2603.16253) separates grounding errors from reasoning errors via constraint matching and reliability-gating. GeoSketch (arXiv:2509.22460) implements diagram auto-correction via MLLM but \"does not assess the correctness or validity of intermediate steps.\" TangramSR (arXiv:2602.05570) achieves test-time self-refinement via geometric consistency feedback (IoU 0.63→0.932 on Tangram spatial assembly), but uses heuristic IoU on continuous spatial tasks rather than formal theorem-level verification on symbolic Euclidean geometry, and is training-free. Sketch2Feedback (arXiv:2602.18520) demonstrates a perception→symbolic→constraint→feedback pipeline for STEM diagrams, validating the architecture for educational feedback.\n\n**Closest works — key differentiations:**\n\n| Method | Reward Type | Formal Guarantee | Diagnostic Output | Stage |\n|--------|-----------|-----------------|-------------------|-------|\n| SymHPR (arXiv:2512.03126) | Per-primitive F1/L2 | No (rule-based, noisy) | No | Perception |\n| \"Bad Seeing or Bad Thinking?\" (arXiv:2605.14054) | Per-step binary PV | No (neural proxy) | No | Perception |\n| PDCR (arXiv:2605.13467) | Decomposed confidence | No (scalar) | No | Perception |\n| ViCrit (arXiv:2506.10128) | Binary hallucination | No (proxy task) | No | Perception |\n| SGVR (arXiv:2601.05073) | Sub-goal verification | Yes | Partial | Reasoning |\n| FoVer (ACL 2026, arXiv:2505.15960) | Step-level PRM data | Yes | Partial | Reasoning |\n| InternGeometry (arXiv:2512.10534) | DDAR-based | Yes | No | Reasoning |\n| TrustGeoGen (arXiv:2504.15780) | N/A (data generation) | Yes | N/A | Data |\n| **FPR (ours)** | **Per-fact diagnostic** | **Yes (zero FP on valid CDL)** | **Yes (contradiction + theorem)** | **Perception** |\n\n## Experimental Design\n\n**Base model:** Qwen3-VL-8B.\n\n**Training data:** FormalGeo7K (~7K problems with ground-truth CDL). Geometry3K for OOD evaluation only (lacks CDL). If 7K proves insufficient (A5 scaling curve unsaturated), FormalGeo7K augmentation to 133K+ is available as expansion.\n\n**Training-time baselines:**\n1. **Accuracy-only GRPO**: Binary final-answer reward\n2. **SymHPR** (arXiv:2512.03126): Rule-based per-primitive F1/L2 — most critical (formal vs. rule-based)\n3. **Perception-R1** (arXiv:2506.07218): Neural judge reward\n4. **GeoDPO** (arXiv:2602.22703): Learned translator reward\n5. **SGVR** (arXiv:2601.05073): Formal verification for reasoning only\n6. **PDCR** (arXiv:2605.13467): Decomposed confidence reward (open-source)\n7. **\"Bad Seeing or Bad Thinking?\" PV** (arXiv:2605.14054): Blindfolded reasoning proxy — conditional baseline (if code available or reproducible from method description)\n\n**Test-time baselines:**\n- Self-consistency@N (N=3, 5)\n- Best-of-N + formal verification re-ranking (N=3, 5)\n- Full-diagram re-processing\n- No re-perception (single-pass)\n- **Oracle re-perception**: Ground-truth contradiction info guides re-perception → upper bound\n\n**Ablations:**\n- A1: Formal constraint propagation reward vs. rule-based F1 (SymHPR-style) — core\n- A2: FormalGeo solver only vs. FormalGeo + DDAR — deeper deduction value\n- A3: Dense per-fact diagnostic reward vs. holistic binary reward — granularity\n- A4: Targeted re-perception vs. all test-time baselines — mechanism evaluation\n- A5: Training data scale (1K / 3K / 7K) — sample efficiency\n- A6: Reward curriculum (phased rule-based→formal) vs. formal-only vs. rule-based-only — curriculum value\n- A7: CDL quality sensitivity — oracle CDL (ground-truth) vs. learned CDL at SFT epochs 0/2/5 — quantifies translator bottleneck\n\n**Evaluation benchmarks:**\n- **GeoPerceive** (from GeoDPO): Perception-isolated — primary perception metric\n- **GePBench** (arXiv:2412.21036): Perception-specific, independently defined\n- **GeoQA, Geometry3K, PGPS9K**: Standard comprehensive benchmarks\n- **MathVerse**: Cross-paper comparison (SymHPR reports +3%)\n\n**Key metrics:**\n- Per-fact precision/recall/F1 on geometric fact extraction\n- FVUR-syntax: Proportion of rollouts with syntactically valid CDL entering solver\n- DYR (Diagnostic Yield Rate): Proportion of valid-CDL rollouts where solver produces ≥1 per-fact diagnostic — the true measure of FPR's effective coverage\n- FVUR-syntax and DYR tracked over training steps (curve)\n- DYR-conditioned performance: Stratified by DYR>80% vs. DYR<50%\n- Translator CDL accuracy (sentence-level + full-expression) on held-out set\n- Re-perception success rate, average rounds, per-fact accuracy delta\n- Oracle re-perception gap analysis: decompose into diagnostic quality gap vs. VLM re-perception capability gap\n- Per-step reward computation latency for each mechanism\n- Performance vs. wall-clock scaling curves; compute-matched control (baselines given equal wall-clock via more rollouts)\n\n**Statistical rigor:** FPR + SymHPR + accuracy-only GRPO: 3 seeds (mean ± std). Other baselines: 2 seeds (range).\n\n**Pre-experiment validation (M1):**\n1. Pilot study (500 problems): Extract CDL with baseline VLM, run rule-based F1 and FormalGeo solver, measure formal-unique error proportion and error type distribution (numeric/relational vs. missing-primitive)\n2. Profiling: Per-problem latency for constraint propagation + diagnostic output (FormalGeo only; FormalGeo + DDAR)\n3. CDL-to-DDAR converter concordance rate on FormalGeo7K ground-truth (>90% required)\n4. Translator CDL accuracy baseline (pre-SFT and post-SFT)\n\n## Key References\n\n- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026, 2602.22703)\n- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025, 2506.07218)\n- Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning (arXiv 2026, 2605.14054)\n- From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models (arXiv 2026, 2605.20177)\n- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026, 2605.13467)\n- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (arXiv 2026, 2601.05073)\n- Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs [SVE-Math] (arXiv 2025, 2501.06430)\n- Solving Olympiad Geometry without Human Demonstrations [AlphaGeometry] (Nature 2024)\n- Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2 (JMLR 2025)\n- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (Symmetry 2024, arXiv 2310.18021)\n- FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems (Symmetry 2025)\n- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025, 2504.15780)\n- ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs (arXiv 2025, 2506.10128)\n- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026, arXiv 2601.01874)\n- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025, 2512.03126)\n- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026, 2603.16253)\n- Efficient PRM Training Data Synthesis via Formal Verification [FoVer] (ACL 2026 Findings, arXiv 2505.15960)\n- GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning (arXiv 2025, 2509.22460)\n- TangramSR: Can Vision-Language Models Reason in Continuous Geometric Space? (arXiv 2026, 2602.05570)\n- Sketch2Feedback: Grammar-in-the-Loop Framework for Rubric-Aligned Feedback on Student STEM Diagrams (arXiv 2026, 2602.18520)\n- GePBench: Evaluating Fundamental Geometric Perception for Multimodal Large Language Models (arXiv 2024, 2412.21036)\n- A Survey of Deep Learning for Geometry Problem Solving (ACL 2026 Main, arXiv 2507.11936)\n- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (arXiv 2025, 2506.04592)\n- InternGeometry: Olympiad-Level Geometry via Complexity-Boosted RL (arXiv 2025, 2512.10534)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 3000–3500 (16x A800-80G: GRPO runs + 7 ablations + 3-seed main + 2-seed baselines + evaluation), timeline: 5 months (M1: SFT warm-start + FormalGeo/DDAR integration + pilot study + profiling + converter validation + translator accuracy baseline; M2–3: GRPO training + reward curriculum + baseline reproduction; M4: evaluation + ablations + multi-seed + oracle analysis; M5: paper writing), estimated_gpu_cost: $6,000–7,000\n- **human_in_loop**: gpu_hours: 2500–3000, timeline: 3.5–4 months, claude_api_cost: $300–500, estimated_gpu_cost: $5,000–6,000\n- **auto_research**: gpu_hours: 3500–4500, timeline: 2.5–3 months, claude_api_cost: $1,200–2,000, estimated_gpu_cost: $7,000–9,000, speed_bottleneck: RL training wall-clock (~16–20h per GRPO run on 16x A800); formal verification throughput to be profiled in M1"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T09:10:23.892Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T09:10:23.892Z",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-27T09:10:23.905Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research data to conduct the evaluation. Let me synthesize everything.

---

```
【阶段】: Triage

【领域调研】:

1. **SymHPR (arXiv:2512.03126)**: 最直接竞争者。提出 hierarchical per-primitive rewards (point-on-line F1, line-on-shape L2 等 rule-based metrics)，在 geometric diagram parsing 上实现 98.2% MSE 降低，MathVerse +3%。rule-based，无 formal deduction，无法检测语义矛盾。本 proposal 声称的"formal vs. rule-based"差异化相对于 SymHPR 是成立的。

2. **"Bad Seeing or Bad Thinking?" (arXiv:2605.14054, May 2026)**: 提出 Perception Verification (PV)——"blindfolded reasoning" proxy 独立奖励感知保真度。引入 Structured Verbal Verification 替代高方差 LLM 判断。是 neural proxy，不提供结构化诊断输出。proposal 对其定位准确。

3. **Perception-R1 (arXiv:2506.07218)**: 将 visual perception reward 引入 RLVR，使用 judging LLM 确保视觉内容与生成一致。缺乏 formal grounding。proposal 描述准确。

4. **PDCR (arXiv:2605.13467)**: Perception-Decomposed Confidence Reward，按 perception/reasoning clusters 分解置信度奖励，仍是 scalar confidence。proposal 描述准确。

5. **ViCrit (arXiv:2506.10128, NeurIPS 2025)**: 通过合成幻觉注入创建 verifiable RL proxy task，binary exact-match reward。domain-agnostic 幻觉检测，非 domain-specific formal verification。proposal 描述准确。

6. **GeoDPO (arXiv:2602.22703)**: NL-to-DSL translator 计算 DSL-level rewards。translator 可产生幻觉分数。proposal 描述准确。

7. **SGVR (arXiv:2601.05073)**: Sub-goal verifiable reward 用于 reasoning stage，+9.7%。formal verification 用于推理而非感知。proposal 描述准确。

8. **TrustGeoGen (arXiv:2504.15780)**: Formal-verified data engine，生成 GeoTrust-200K。证明 formal tools 在几何域的成熟度，但目标是数据质量而非 perception reward。proposal 描述准确。

9. **FormalGeo (Symmetry 2024, arXiv:2310.18021)**: CDL 形式语言 + 符号求解器 + FormalGeo7K dataset。FGeo-Parser (Symmetry 2025) 实现 91.5% sentence-level match 但仅 56.5% perfect full-expression accuracy。FGeo-HyperGNet (IJCAI 2025) 整合 FormalGeo 符号系统。生态系统真实且活跃。

10. **EVPV (arXiv:2603.16253)**: Explicit Visual Premise Verification——提取结构化视觉事实到 constraint set，但仍是 neural-based constraint matching 而非 formal theorem-level verification。

11. **TangramSR (arXiv:2602.05570)**: Test-time self-refinement via geometric consistency feedback (IoU 0.63→0.932)，但在连续空间 Tangram 任务上使用 heuristic IoU，非 symbolic Euclidean geometry 的 formal theorem-level verification。

12. **Clinical VLM formal verification (arXiv:2602.24111)**: 将 VLM 输出映射为 SMT constraints 进行 formal verification，架构上最接近本 proposal 的"感知→符号→formal checking"思路，但在临床而非几何领域。

- **调研总结**: 2025-2026 年，perception-stage reward 是热门研究方向，已有 6+ 篇并行工作，涵盖 neural judge、rule-based F1、decomposed confidence、proxy task 等多种 reward 机制。Formal verification 在 reasoning-stage (SGVR, FoVer, InternGeometry) 和 data generation (TrustGeoGen) 已被证明有效。但**尚无工作将 formal geometric constraint propagation 应用于 perception-stage reward 并产生结构化诊断输出**。这个 gap 是真实的。FormalGeo CDL 生态成熟，工具链可用，但 VLM→CDL translation 的 56.5% perfect accuracy 是已知瓶颈。


【Trivial Alternative 检验】:

存在两个 trivial alternative 威胁：

1. **SymHPR（rule-based F1/L2）已经足够？** SymHPR 用 per-primitive F1/L2 做 structured perception reward，实现成本远低于 formal verification pipeline。核心问题是：formal verification 相比 rule-based F1 的增量有多大？proposal 声称 formal verification 能检测 semantic contradictions (如角度与圆定理矛盾)，而 rule-based F1 不能——但这类"语义矛盾"在实际 FormalGeo7K 中占错误的比例是多少？如果大多数 perception error 是简单的数值偏差（rule-based F1 已能捕捉），formal verification 的增量可能有限。proposal 的 M1 pilot study 设计了 error type distribution 分析，这很关键，但目前这个比例是未知的。

2. **Best-of-N + formal filtering 是否够用？** proposal 已主动回应此问题，论点是训练时 internalize constraint awareness 优于测试时 filtering。论证合理但需实证支持——如果 best-of-N (N=5) + formal re-ranking已经非常接近 FPR training 效果，那 training-time reward 的价值就大打折扣。

**增量价值核心**: 在于 diagnostic output → targeted re-perception 这条链路。如果仅论 reward signal 质量，formal vs. rule-based 可能是 marginal improvement；但 diagnostic output 提供了一种质性不同的反馈机制（从"分数"到"诊断"），这是 scalar reward 方法无法提供的。这个增量价值是否足够，取决于 targeted re-perception 的实际效果。


【前提假设检验】:

核心 claim 的逻辑链: VLM 输出 CDL → FormalGeo 约束传播 → per-fact 诊断 → diagnostic reward 用于 GRPO training / 用于 test-time targeted re-perception

**关键未验证假设**:

1. **CDL translation quality 假设**（最致命）: 整个 pipeline 的前提是 VLM 能产出 syntactically valid CDL。FGeo-Parser 在专门训练的条件下只达 56.5% perfect accuracy。Qwen3-VL-8B 经过 SFT warm-start 后能否达到足够的 FVUR-syntax 率？如果 70%+ rollouts 的 CDL 无效，formal verification 组件几乎不起作用，整个方法退化为 rule-based F1 fallback + 偶尔的 formal reward，本质上变成了 SymHPR 的变体。proposal 设计了 reward curriculum 来缓解，但这仍是一个结构性风险。

2. **Over-determined constraint system 假设**: proposal 假设几何问题通常有 over-determined constraint system，单个错误事实会传播为可检测矛盾。但 missing-primitive errors（完全漏检一个点/线）不产生矛盾，只产生信息不足。如果 VLM 的主要感知错误是 missing-primitive 而非 numeric/relational error，formal verification 的覆盖率会很低。DYR (Diagnostic Yield Rate) 可能远低于预期。

3. **VLM 能利用结构化诊断反馈进行 targeted re-perception 假设**: 告诉 VLM "∠ABC=90° 与 inscribed angle theorem 矛盾——请重新检查 ∠ABC"，VLM 就能有效修正——这假设 VLM 在 re-prompting 下能做出有意义的修正，而不是随机改变输出。这个能力在当前 VLM 上未经验证。如果 VLM 在 re-perception 后准确率无显著提升，targeted re-perception 这一核心应用就会失效。

4. **FormalGeo7K 数据规模假设**: 7K 训练样本对 GRPO training 是否足够？proposal 提到可扩展到 133K+ 但这增加了工程复杂度。

以上假设中，#1 和 #2 共同决定了 formal verification 组件在训练中的实际触发率和覆盖率——如果两者都偏悲观（CDL 无效率高 + 主要错误类型不可检测），proposal 的核心贡献会被严重削弱。


【3 维度打分】:

1. **Novelty: 中** — 核心 gap 是真实的：确认无现有工作将 formal geometric constraint propagation 应用于 perception-stage reward 并产生结构化诊断输出（调研 12 篇最相关工作均不覆盖此交叉点）。然而，novelty 的性质偏向 "natural next step"——formal verification 已在 reasoning stage 成功 (SGVR, FoVer, InternGeometry)，perception-stage reward 是活跃方向 (6+ 并行工作)，FormalGeo CDL 工具链成熟——将三者组合是相对 obvious 的延伸。Diagnostic output → targeted re-perception 链路提供了超越简单组合的质性新机制，这提升了 novelty，但核心仍是"已有工具在新 stage 的应用"。对比 SymHPR (arXiv:2512.03126) 的 rule-based structured reward，FPR 的差异化在于 formal guarantee + diagnostic output，这是有实质的但不是 paradigm shift。

2. **Significance: 中** — 几何感知瓶颈是真实且重要的问题（GPT-4o 70% error rate, SVE-Math arXiv:2501.06430）。但方法的 generalizability 受限：(a) 仅适用于 FormalGeo CDL 兼容的几何问题子集；(b) 依赖特定工具链（FormalGeo solver, CDL 语法）；(c) FormalGeo7K 规模有限。将 formal verification 思路从 reasoning → perception 的方向性贡献有一定影响力，但狭窄的领域适用范围限制了整体 significance。如果论文能在实验中充分展示 diagnostic output 和 targeted re-perception 的独特价值（相对于 scalar reward 的质性优势），significance 可以有所提升。

3. **Related Work: 强** — proposal 对领域覆盖极为全面，引用了 25+ 篇 2024-2026 的相关工作，涵盖感知 reward (6 种方法)、推理 formal verification (4 种方法)、数据生成 (TrustGeoGen)、工具链 (FormalGeo, AlphaGeometry2)、test-time self-correction (TangramSR, GeoSketch)。经调研验证，所有引用论文真实存在，描述基本准确。差异化定位通过详细对比表清晰呈现。对 FGeo-Parser 的局限性描述准确（91.5% sentence-level, 56.5% perfect）。这是一个在 related work 层面做得非常扎实的 proposal。


【概率估计】: [25% - 38%] 中位 30%

【估计理由】: 
- Novelty 为"中"：gap 真实但偏 natural combination，非 surprising insight → 限制上界在 ~38%
- Significance 为"中"：domain-specific，generalizability 受限 → 进一步限制上界
- Related Work 为"强"：覆盖全面准确 → 提供了下限保障（不会因 positioning 不足被拒）
- CDL translation bottleneck 是结构性风险：如果 formal verification 实际触发率低，整个方法退化为 SymHPR 变体，核心贡献不成立。这个风险同时压低了 novelty 的可信度（"novelty 成立但可能在实践中 irrelevant"是一种特别难辩护的局面）
- 限制上界的主要维度是 Novelty（natural combination）和 Significance（narrow domain）的交叉效应

【主要风险】:
1. **CDL translation bottleneck 导致核心贡献空转**: 如果 SFT warm-start 后 FVUR-syntax 仍然低（<50%），formal verification 组件在大部分 rollouts 中不触发，整个方法在实践中退化为 rule-based F1 fallback，核心 novelty claim（formal diagnostic reward）变得 marginal。审稿人会问："FPR 的提升到底来自 formal verification 还是来自 rule-based F1 fallback？"
2. **与 SymHPR 的 marginal improvement**: 如果 ablation A1 (formal vs. rule-based F1) 显示差异不显著，审稿人会认为 formal verification 的复杂性不 justified——增加了 FormalGeo solver 依赖、CDL translation 开销、reward curriculum 复杂度，但性能提升有限。这是 "engineering complexity without sufficient empirical payoff" 的经典拒稿理由。
```

Sources:
- [SymHPR - Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)
- [Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)
- [Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward](https://arxiv.org/abs/2506.07218)
- [PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning](https://arxiv.org/html/2605.13467)
- [ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs](https://arxiv.org/abs/2506.10128)
- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/pdf/2602.22703)
- [SGVR: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward](https://arxiv.org/pdf/2601.05073)
- [TrustGeoGen: Formal-Verified Data Engine](https://arxiv.org/abs/2504.15780)
- [FormalGeo: An Extensible Formalized Framework](https://arxiv.org/html/2310.18021v6)
- [FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems](https://www.mdpi.com/2073-8994/17/1/8)
- [EVPV: Grounding the Score](https://arxiv.org/html/2603.16253)
- [TangramSR: Can VLMs Reason in Continuous Geometric Space?](https://arxiv.org/pdf/2602.05570)
- [Toward Guarantees for Clinical Reasoning in VLMs via Formal Verification](https://arxiv.org/pdf/2602.24111)
- [SVE-Math: Open Eyes, Then Reason](https://arxiv.org/abs/2501.06430)
- [ACL 2026 Geometry Survey paper list](https://github.com/majianz/dl4gps)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [SymHPR] (arXiv:2512.03126, Dec 2025): Hierarchical per-primitive rewards (point-on-line, line-on-shape F1/L2) via symbolic auto-encoder. Rule-based, not formally grounded, no semantic contradiction detection. Proposal's most direct structural-perception-reward competitor — FPR claims formal guarantees over SymHPR's rule-based metrics. Proposal's characterization accurate.
- [GeoDPO] (arXiv:2602.22703, Feb 2026): NL-to-DSL translator computes DSL-level reward for geometric perception RL. Demonstrates DSL-mediated perception reward is viable. Achieves +26.5% in-domain, +8.0% OOD, +39.0% downstream. Key precedent: translator-mediated reward signals work, but translator hallucination is a real issue. Proposal's characterization accurate.
- ["Bad Seeing or Bad Thinking?"] (arXiv:2605.14054, May 2026): Decomposes generation into interleaved perception/reasoning steps; Perception Verification (PV) via "blindfolded reasoning" proxy rewards perception fidelity independently. Neural proxy, no formal guarantee, no per-fact diagnosis. Very recent, directly addresses perception credit assignment. Proposal's characterization accurate.
- [PDCR] (arXiv:2605.13467, May 2026): Decomposes confidence-based rewards by perception/reasoning skill clusters, normalizes advantages within each cluster. Still scalar confidence, no structural diagnosis. Proposal's characterization accurate.
- [ViCrit] (arXiv:2506.10128, Jun 2025, NeurIPS 2025): Synthetic hallucination injection → binary exact-match reward for perception RL. Domain-agnostic, validates verifiable perception rewards concept. Proposal's characterization accurate.
- [Perceval] (arXiv:2604.24583, Apr 2026): **NOT CITED IN PROPOSAL.** Perception-centric PRM with token-level error grounding — extracts image-related claims, compares one-by-one with visual evidence, returns claims containing perceptual errors. Enables targeted correction at test time (truncate erroneous span → re-generate). Functionally very similar to FPR's "diagnostic output + targeted re-perception" but via neural PRM, not formal verification. This is a significant omission.
- [VPPO] (approx. arXiv 2510.09285, ICLR 2026 Spotlight): First multimodal RL algorithm to formally identify perceptually pivotal tokens via dependency analysis for targeted optimization. 7B model achieves 19.2% improvement. **NOT CITED IN PROPOSAL.** Another approach that targets perception tokens specifically for RL, though via dependency analysis rather than formal constraint verification.
- [SPARC] (arXiv:2602.06566, Feb 2026): Modular decoupling of perception and reasoning circuits for test-time scaling. Supports asymmetric compute allocation. Not directly a reward method but demonstrates perception-reasoning separation architecture.
- [FGeo-Parser] (Symmetry 2025): CDL autoformalization achieves 91.5% sentence-level match, but only 56.5% perfect full-expression accuracy. This is the translator FPR depends on — the gap between 91.5% and 56.5% reveals the CDL translation bottleneck is severe.
- [TrustGeoGen] (arXiv:2504.15780): Formal verification for geometric data generation (GeoTrust-200K). Demonstrates formal tools' maturity but for data generation, not perception rewards. Proposal's characterization accurate.
- [FormalGeo] (Symmetry 2024, arXiv:2310.18021): Extensible formalized framework using GDL/CDL for Euclidean geometry. Core infrastructure FPR depends on. Real and well-maintained.

- **调研总结**: The perception-reward-for-VLM-geometric-reasoning space has exploded in early 2026, with at least 6-7 concurrent methods (GeoDPO, Perception-R1, "Bad Seeing or Bad Thinking?", PDCR, ViCrit, Perceval, VPPO) all targeting the same problem from different angles. Formal verification has been applied to the reasoning stage (SGVR, FoVer, InternGeometry) and to data generation (TrustGeoGen), but NOT yet to the perception stage — this gap is real. However, Perceval (arXiv:2604.24583) already achieves functionally similar capabilities (per-claim error identification + targeted test-time correction) via neural PRM without formal methods, narrowing FPR's practical novelty to the "formal guarantee" aspect.

【Trivial Alternative 检验】:

**Yes, there are simpler alternatives that partially cover FPR's value proposition:**

1. **Best-of-N + formal re-ranking** (acknowledged in proposal): The proposal argues training-time rewards internalize constraint awareness while test-time filtering cannot. This argument is reasonable but not bulletproof — recent test-time scaling work (SPARC, Perceval) shows substantial gains from test-time-only methods.

2. **Perceval-style neural PRM + targeted correction** (NOT acknowledged): Perceval already achieves per-claim error identification and targeted re-generation at test time without any formal verification infrastructure, CDL translation, or domain-specific tooling. If Perceval achieves competitive perception error correction rates, FPR's incremental value reduces to "formal guarantee on the subset of outputs with valid CDL" — a much narrower contribution.

3. **GeoDPO's existing DSL-mediated reward**: GeoDPO already uses a translator to compute DSL-level perception rewards and achieves strong results (+26.5% in-domain). FPR's incremental value over GeoDPO is the formal constraint checking and diagnostic output, but both share the translator bottleneck.

**Incremental value of FPR**: The genuine increment is (a) zero-false-positive formal guarantee (conditional on valid CDL), and (b) theorem-level diagnostic explanations (not just "this claim is wrong" but "this claim contradicts inscribed angle theorem"). Whether this increment justifies the engineering complexity (CDL translator + FormalGeo integration + reward curriculum) is debatable.

【前提假设检验】:

The core claim's logic chain has several unverified assumptions:

1. **"CDL translation will be accurate enough for formal verification to be meaningful"** — This is the most critical assumption. FGeo-Parser achieves only 56.5% full-expression accuracy. If the VLM's CDL output is frequently syntactically invalid or semantically wrong-but-valid, formal verification either doesn't apply (invalid CDL → fallback to rule-based F1, losing the formal advantage) or verifies the wrong thing (valid but inaccurate CDL → formal checker validates translator errors, not perception errors). The proposal's mitigation (SFT warm-start + reward curriculum) is reasonable but unproven — there's no evidence that RL training on FormalGeo7K will push CDL accuracy high enough for formal rewards to dominate.

2. **"Geometric problems are typically over-determined, so single-fact errors produce detectable contradictions"** — This is stated as fact but is actually a hypothesis that needs empirical validation. The proposal acknowledges missing-primitive errors may not produce contradictions, but doesn't quantify how common under-determined configurations are. If a large fraction of perception errors are "silent" (don't trigger contradictions), the Diagnostic Yield Rate (DYR) will be low, and formal verification coverage will be poor. The M1 pilot study is designed to test this, which is good — but this means the entire project's viability hinges on an untested empirical assumption.

3. **"Diagnostic output enables meaningfully better re-perception than generic re-prompting"** — The claim that telling a VLM "∠ABC=90° contradicts inscribed angle theorem" leads to better correction than "re-examine this region" is intuitive but unproven. VLMs may not effectively leverage formal theorem citations in re-perception prompts. The actual mechanism by which a VLM uses this diagnostic information to "look again more carefully" is underspecified.

4. **"Training-time formal rewards internalize geometric constraint awareness better than test-time filtering"** — This is the argument against the best-of-N trivial alternative. It's plausible but could go either way empirically.

【3 维度打分】:

1. **Novelty: 中** — The gap (formal verification for perception-stage rewards) is real — no existing work applies formal constraint propagation to generate diagnostic perception rewards. The contribution chain (formal guarantee → diagnostic output → targeted re-perception) is logically coherent and each step enables the next. However, several factors limit the novelty assessment:
   - The approach is fundamentally a *recombination* of existing components (FormalGeo's constraint propagation + GRPO training + perception-stage reward) rather than a new technique. The individual pieces all exist; the novelty is the specific integration.
   - Perceval (arXiv:2604.24583, NOT CITED) already achieves functionally similar capabilities (per-claim error grounding + targeted test-time correction) via neural methods. FPR's formal guarantee is a genuine differentiator, but the practical novelty narrows significantly.
   - The "from scoring to diagnosing" shift is real but incremental — Perceval also diagnoses (identifies specific erroneous claims), just without formal theorem citations.
   - Within the geometric domain specifically, GeoDPO already uses translator-mediated DSL-level rewards; FPR adds formal checking on top of a similar translator pipeline.

2. **Significance: 弱偏中** — Several factors limit significance:
   - **Domain restriction**: Only works for Euclidean geometry problems with FormalGeo's CDL formalism. Cannot generalize to other visual math domains (charts, tables, physics diagrams) without equivalent formal systems. FormalGeo7K is ~7K problems — small even for the geometric domain.
   - **CDL translator bottleneck**: The approach's effectiveness is capped by CDL translation accuracy (56.5% full-expression). Even with improvements, the formal reward only applies to the subset of syntactically valid CDL outputs, meaning the system often falls back to rule-based F1 — reducing FPR to SymHPR + occasional formal bonus.
   - **Impact ceiling**: Even if all results are positive, the contribution is "formal verification improves perception rewards in the specific case of Euclidean geometry" — a correct but narrow finding. The broader lesson ("domain-specific formal tools can improve perception rewards") is interesting but requires the existence of such formal tools in each target domain.
   - **"Surprising if positive?" test**: If FPR outperforms SymHPR by a few points on geometric perception benchmarks, most reviewers would say "expected — formal verification is more precise than heuristic F1." The more interesting finding would be if targeted re-perception shows large gains, but that's the more uncertain component.

3. **Related Work: 中偏弱** — The proposal demonstrates thorough awareness of the perception-reward landscape (GeoDPO, Perception-R1, PV, PDCR, ViCrit, SymHPR) and the formal-verification-for-reasoning landscape (SGVR, FoVer, InternGeometry, TrustGeoGen). The comparison table is well-constructed and the differentiation is clearly articulated. However:
   - **Critical omission: Perceval** (arXiv:2604.24583, Apr 2026) — perception-centric PRM with token-level error grounding and targeted test-time correction. This is arguably the closest functional competitor to FPR's diagnostic + re-perception pipeline, and its absence weakens the novelty claim.
   - **Critical omission: VPPO** (ICLR 2026 Spotlight) — formally identifies perceptually pivotal tokens for targeted RL optimization. Directly relevant to the "targeted perception reward" theme.
   - **Missing SPARC** (arXiv:2602.06566) — perception-reasoning decoupling for test-time scaling, relevant to the targeted re-perception mechanism.
   - These omissions are partially understandable given the field's rapid pace (Perceval appeared April 2026), but they represent real gaps in the competitive landscape analysis.

【概率估计】: [18% - 28%] 中位 23%

【估计理由】: 
Novelty 为"中"而非"强"——核心贡献是将已有技术（FormalGeo 约束传播）应用到新场景（感知阶段奖励），且 Perceval 已通过神经方法实现了功能相似的"逐 claim 诊断 + 定向修正"能力，显著压缩了 FPR 的独特价值空间。Significance 为"弱偏中"——受限于 Euclidean geometry 单一领域、FormalGeo7K 数据规模（~7K）、以及 CDL 翻译器瓶颈（56.5% 完全准确率），使得即使结果 positive，影响范围也较窄，且核心发现（formal verification 比 rule-based F1 更精确）对审稿人来说并不 surprising。Related Work 遗漏了 Perceval 和 VPPO 两个直接竞争者。**上界主要受 Significance 限制**——领域窄 + CDL 瓶颈使得即便 idea 完全成立，论文的 impact 也难以达到 AAAI 的 acceptance bar。中位 23% 反映了一个"方向正确、gap 真实存在、但内核偏窄且不够 surprising"的 idea。

【主要风险】:
1. **CDL 翻译器瓶颈导致形式化验证有效覆盖率低**: 56.5% 的完全准确率意味着大量 rollout 要么无法进入形式化验证（语法无效），要么验证的是翻译器的错误而非 VLM 感知的错误。这使得 FPR 在实践中可能退化为"SymHPR + 偶尔的 formal bonus"，削弱核心 novelty claim 的实验验证。
2. **Perceval 等神经方法已实现功能等价的"诊断 + 定向修正"**: 如果 Perceval 在相同 benchmark 上取得有竞争力的结果且不需要领域特定的形式化工具，审稿人可能质疑 FPR 的工程复杂度是否 justified——formal guarantee 的理论优势在实践中可能无法转化为显著的性能优势。
```

Sources:
- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)
- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning](https://arxiv.org/abs/2602.22703)
- [Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)
- [PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning](https://arxiv.org/abs/2605.13467)
- [ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs](https://arxiv.org/abs/2506.10128)
- [Perceval: Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583)
- [SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs](https://arxiv.org/abs/2602.06566)
- [SGVR: Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)
- [FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving](https://arxiv.org/abs/2310.18021)
- [FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems](https://www.mdpi.com/2073-8994/17/1/8)
- [TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving](https://arxiv.org/abs/2504.15780)
- [EVPV: Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models](https://arxiv.org/abs/2603.16253)
- [VPPO: Spotlight on Token Perception for Multimodal Reinforcement Learning](https://arxiv.org/abs/2510.09285)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research data. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [SymHPR] (arXiv:2512.03126, 2025): 最接近的感知奖励工作。提出层次化过程奖励模型，使用per-primitive F1/L2指标（point-on-line、line-on-shape、shape-on-relation），在几何图解析上取得显著提升（MathGlance +13%）。但为rule-based指标，不涉及形式化定理级验证，无法检测语义矛盾（如角度与圆定理不一致）。
- [GeoDPO] (arXiv:2602.22703, 2026): 通过NL-to-DSL translator计算DSL级reward信号用于RL训练。与本proposal最直接竞争——同样试图在感知阶段提供结构化奖励。但translator可能产生hallucination，且reward是scalar而非diagnostic。GeoPerceive benchmark来自此工作。
- ["Bad Seeing or Bad Thinking?"] (arXiv:2605.14054, 2026): 通过"blindfolded reasoning" proxy独立奖励感知保真度（PV机制），明确分解perception与reasoning步骤。但PV仍为neural proxy，只报告"perception unreliable"，不诊断具体哪个事实违反哪个约束。
- [PDCR] (arXiv:2605.13467, 2026): 分解confidence reward为感知/推理cluster，解决全局reward混合信号退化问题。但仍为scalar confidence，无结构化诊断。
- [ViCrit] (arXiv:2506.10128, NeurIPS 2025): 通过合成hallucination注入+二元精确匹配构建可验证RL代理任务。验证了可验证感知奖励的有效性，但使用domain-agnostic幻觉检测，非domain-specific几何形式化验证。
- [SGVR] (arXiv:2601.05073, 2026): 将形式化验证应用于推理阶段的sub-goal验证，+9.7%。证明形式化验证作为RL reward的有效性，但仅限推理阶段。
- [FoVer] (ACL 2026 Findings, arXiv:2505.15960): 形式化验证用于step-level PRM数据合成。同样限于推理阶段。
- [TrustGeoGen] (arXiv:2504.15780, 2025): 使用形式化验证生成几何数据（GeoTrust-200K），证明形式化工具在几何领域的成熟度。但目标是数据质量而非感知奖励。
- [FGeo-Parser] (Symmetry 2025): FormalGeo CDL的自动formalization工具。句子级匹配准确率91.51%，但完整表达式准确率仅56.47%——直接印证proposal中CDL translator瓶颈。
- [Sieve / Iterative Evidence Refinement] (arXiv:2603.14117, 2026): 通过内部表征re-engage图像证据进行迭代精炼，+8%。概念上与targeted re-perception相关，但使用注意力引导而非形式化约束诊断。
- [TangramSR] (arXiv:2602.05570, 2026): 基于几何一致性反馈(IoU)实现test-time self-refinement (0.63→0.932)。但使用启发式IoU在连续空间任务上，非形式化定理级验证。

- 调研总结: 2025-2026年，几何感知奖励领域极度活跃，已有7+工作从不同角度提供感知阶段reward（neural judge、learned translator、rule-based F1、decomposed confidence、blindfolded proxy、synthetic hallucination）。形式化验证已在推理阶段(SGVR/FoVer/InternGeometry)和数据生成(TrustGeoGen)被验证有效，但确实尚无工作将formal verification应用于perception阶段作为reward信号。这个gap是真实存在的。

【Trivial Alternative 检验】:
最直接的trivial alternative是**Best-of-N + formal verification re-ranking**：让VLM生成N个CDL候选，用FormalGeo过滤掉有矛盾的。这不需要任何训练改动，成本极低。Proposal已意识到并做了回应（training-time reward可将约束意识内化），但这个论证需要实验验证，不是逻辑上自明的。

第二个alternative是**SymHPR的rule-based F1 + heuristic contradiction checking**：不需要CDL translator这个瓶颈环节，直接在primitive level做rule-based检查。与本proposal的增量价值在于：(1) formal guarantee（zero false positive on valid CDL），(2) 能检测语义级矛盾（angle与circle theorem不一致），(3) diagnostic output。其中(2)和(3)是真实的增量价值，(1)的条件限定"on valid CDL"是关键——如果CDL有效率低，这个guarantee的实际覆盖面就小。

**增量价值判断**：diagnostic output（从scoring到diagnosing的质变）和targeted re-perception（被诊断信息启用的新机制）是本proposal超越trivial alternatives的真实贡献。但这两个贡献的实际价值高度依赖于CDL translator质量。

【前提假设检验】:
1. **CDL translator将足够频繁地生成语法有效的CDL**：这是最关键的未验证假设。FGeo-Parser完整表达式准确率仅56.47%，即使经过SFT warm-start，FVUR-syntax（进入solver的有效CDL比例）是否能达到使formal reward有意义的水平，完全未知。Proposal设计了reward curriculum作为缓冲，但如果Phase 3永远到不了（formal dominant），整个方法就退化为rule-based F1 + 偶尔的formal reward。
2. **几何问题的约束系统足够over-determined，使单个错误事实可被检测**：Proposal承认了missing-primitive错误无法检测，但对"numeric/relational error导致可检测矛盾"的比例完全是假设性的——M1 pilot study正是为此设计的，说明authors自己也认为这需要验证。
3. **Diagnostic output对targeted re-perception的实际帮助**：假设VLM能理解"∠ABC=90°与inscribed angle theorem矛盾"这样的诊断并有效re-examine。这假设VLM有足够的geometric reasoning能力来利用诊断信息，而如果VLM的感知错误本身就是因为"看不清图"，给它更详细的verbal指令未必有帮助。

【3 维度打分】:

1. **Novelty: 中偏强** — 核心贡献"将formal verification从reasoning阶段迁移到perception阶段，并提供diagnostic（而非scalar）reward output"在调研中确认无先例。与最近期7+竞争工作（SymHPR、GeoDPO、Perception-R1、PV、PDCR、ViCrit等）的差异化真实存在——所有现有工作提供scoring信号，无一提供per-fact diagnostic output with formal guarantee。这不仅是"tool X applied to problem Y"，diagnostic→targeted re-perception的enabling chain是质变。但降分因素：(a) 从reasoning-stage formal verification到perception-stage formal verification的迁移思路较为自然，审稿人可能认为是logical extension而非surprising insight；(b) 对FormalGeo/DDAR现有工具的依赖较重，方法层面的原创技术贡献（vs. 工程整合贡献）需要clarify。

2. **Significance: 中** — 感知瓶颈确实重要（GPT-4o 70%错误率，SVE-Math），且本proposal聚焦的"诊断性反馈"概念有超越几何领域的潜在影响。但限制因素：(a) 方法仅适用于有formal specification的几何问题（依赖CDL/FormalGeo），不可直接推广到其他视觉数学领域或通用视觉推理；(b) FormalGeo7K数据规模小（7K），evaluation在geometry-specific benchmarks上，影响面窄；(c) 如果CDL translator瓶颈严重，实际改善可能有限。

3. **Related Work: 强** — 这是proposal最突出的维度。覆盖了2025-2026年几乎所有相关工作（7个perception reward方法、3个formal verification for reasoning方法、数据生成、test-time refinement等），差异化表格清晰明确，每个竞争工作的局限性分析准确（经调研验证）。唯一可补充的是Sieve (arXiv:2603.14117) 的iterative evidence refinement和formal verification for clinical reasoning (arXiv:2602.24111)。

【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
Novelty中偏强（diagnostic formal verification for perception是真实gap）+ Significance中（重要问题但scope窄）+ Related Work强（极佳的定位和覆盖）→ 整体idea质量落在"有实质内核，方向正确，有真实novelty delta"的区间。核心发现如果positive（formal diagnostic reward显著优于scalar reward），审稿人反应可能介于"makes sense, good engineering"和"interesting, the diagnostic mechanism is a useful new paradigm"之间——不太可能说"I would have guessed this"也不太可能说"surprising"。这将其锚定在25-35%区间偏上。

上界受限于：(a) Novelty的"natural extension"感知风险——从reasoning-stage formal verification到perception-stage formal verification的跳跃幅度，部分审稿人可能认为不够大；(b) Significance被scope限制（仅geometry + FormalGeo生态）。下界由强related work覆盖和真实的diagnostic novelty支撑。

【主要风险】:
1. **"Engineering integration vs. research contribution"质疑**：审稿人可能认为核心贡献是将现有工具（FormalGeo solver）应用于新场景（perception reward），方法层面的原创技术贡献不足，更接近systems paper而非methods paper。
2. **CDL translator假设的脆弱性削弱idea可信度**：即使在idea评估层面（不考虑实验），审稿人在reading时就会注意到56.47%的full-expression accuracy，可能质疑"如果近一半的CDL都是invalid的，formal guarantee的实际意义有多大？"这不是执行层面的问题，而是idea logic chain中的薄弱环节。
```

Sources:
- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)
- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided RL](https://arxiv.org/abs/2602.22703)
- [Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning](https://arxiv.org/abs/2605.14054)
- [PDCR: Perception-Decomposed Confidence Reward](https://arxiv.org/abs/2605.13467)
- [ViCrit: A Verifiable RL Proxy Task for Visual Perception](https://arxiv.org/abs/2506.10128)
- [SGVR: Milestones over Outcome](https://arxiv.org/abs/2601.05073)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [TrustGeoGen: Formal-Verified Data Engine](https://arxiv.org/abs/2504.15780)
- [FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems](https://www.mdpi.com/2073-8994/17/1/8)
- [Perception-R1: Advancing Multimodal Reasoning via Visual Perception Reward](https://arxiv.org/abs/2506.07218)
- [Sieve: Improving Visual Reasoning with Iterative Evidence Refinement](https://arxiv.org/abs/2603.14117)
- [TangramSR: VLMs Reasoning in Continuous Geometric Space](https://arxiv.org/abs/2602.05570)
- [EVPV: Grounding the Score](https://arxiv.org/abs/2603.16253)
- [FormalGeo Framework](https://formalgeo.github.io/)


【原始 proposal（允许参考但不是主要依据）】:
# Diagnostic Formal Verification as Targeted Re-Perception Rewards for Visual Geometric Reasoning

## Core Problem

How can we provide formally verifiable, diagnostic reward signals for the visual perception stage of multimodal geometric reasoning — signals that pinpoint which specific geometric fact is wrong, explain why it contradicts known geometric constraints, and enable targeted correction at test time?

## Research Opportunity

Current RL approaches for visual math perception produce opaque reward signals that cannot diagnose specific perception errors:
- **GeoDPO** (arXiv:2602.22703): Learned NL-to-DSL translator computes DSL-level rewards; translator can hallucinate scores.
- **Perception-R1** (arXiv:2506.07218): Judge LLM provides visual perception rewards; lacks formal grounding.
- **"Bad Seeing or Bad Thinking?"** (arXiv:2605.14054): Perception Verification (PV) via blindfolded reasoning proxy independently rewards perception fidelity — but remains a neural proxy that reports "perception unreliable" without diagnosing which fact conflicts with which constraint.
- **"From Seeing to Thinking"** (arXiv:2605.20177): Shows perception improves more via RL than caption-based SFT, but uses only generic rewards.
- **PDCR** (arXiv:2605.13467): Decomposes confidence rewards by perception/reasoning clusters — but still scalar confidence, no structural diagnosis.
- **SymHPR** (arXiv:2512.03126): Hierarchical per-primitive rewards (point-on-line, line-on-shape F1/L2), closest to structured perception feedback — but rule-based metrics without formal deduction. Cannot detect semantic contradictions (e.g., angle inconsistent with circle theorem), and F1 can be noisy when primitive extraction itself errs.
- **ViCrit** (arXiv:2506.10128, NeurIPS 2025): Verifiable RL proxy task via synthetic hallucination injection with binary exact-match reward — validates verifiable perception rewards but uses domain-agnostic hallucination detection, not domain-specific formal geometric verification.

Formal verification for reasoning-stage rewards has proven effective — SGVR (arXiv:2601.05073, +9.7%), Safe (arXiv:2506.04592), FoVer (ACL 2026 Findings, arXiv:2505.15960), InternGeometry (arXiv:2512.10534) — but none applies formal verification to the perception stage. TrustGeoGen (arXiv:2504.15780) uses formal verification for geometric data generation (GeoTrust-200K), demonstrating formal tools' maturity in the geometric domain, but targets data quality rather than perception reward signals. FormalGeo (Symmetry 2024, arXiv:2310.18021) and AlphaGeometry2's DDAR engine (JMLR 2025, C++ implementation 300x faster) now make symbolic constraint checking at scale feasible. The ACL 2026 geometry survey (arXiv:2507.11936) identifies formal language representations and automated verification as critical open challenges.

**The key gap all existing perception reward methods share:** they produce scalar/per-step scoring signals. None generates structured diagnostic output identifying which specific fact contradicts which geometric constraint, with formal correctness guarantees. This diagnostic capability enables a qualitatively new mechanism — targeted re-perception — that no scoring-based approach can support.

## Proposed Approach

We propose FormalPerceptReward (FPR), the first framework using formal geometric constraint propagation to generate diagnostic reward signals for perception-stage RL training, enabling targeted re-perception at test time.

**Core contribution chain** (each enabling the next):
1. **Formally guaranteed reward precision** (foundation): When VLM-produced CDL is syntactically valid, FormalGeo's constraint propagation detects contradictions that are logically provable — zero false positives. This guarantee does not hold for neural judges (which hallucinate), rule-based F1 (which produces noisy scores from imperfect primitive extraction), or neural proxies (which can misjudge).
2. **Actionable diagnostic output** (core novelty): Beyond scoring, FPR produces per-fact structured diagnostics: "∠ABC=90° contradicts A on circle with diameter BC by the inscribed angle theorem." This is a qualitative shift from scoring to diagnosing — no existing perception reward method provides this.
3. **Targeted re-perception at test time** (enabled application): Diagnostic output supports selective re-examination of specific erroneous facts rather than full-diagram re-processing.

**Why training-time formal reward, not just test-time formal filtering?** One might ask whether best-of-N sampling + formal verification re-ranking suffices. Training-time formal rewards internalize geometric constraint awareness into the model, improving single-pass perception quality. Test-time filtering cannot teach the model what constitutes formally consistent perception; it only selects among existing outputs. Moreover, best-of-N compute scales linearly with N, while trained models deliver better base quality at fixed inference cost.

**Pipeline.** Qwen3-VL-8B outputs structured geometric facts in FormalGeo's Conditional Declaration Language (CDL). FormalGeo's symbolic solver performs constraint propagation, producing per-fact diagnostic rewards. These replace learned neural judges in GRPO training on FormalGeo7K (~7K annotated problems).

**Translator feasibility.** Converting visual perception to syntactically valid CDL is non-trivial. FGeo-Parser (Symmetry 2025) achieves 91.5% sentence-level match accuracy but only 56.5% perfect full-expression accuracy on FormalGeo data. Mitigation:
- SFT warm-start: Fine-tune Qwen3-VL-8B on FormalGeo7K ground-truth CDL before GRPO
- Graceful degradation: Syntactically invalid CDL receives fixed low reward + rule-based F1 fallback
- Reward curriculum: Phase 1 (rule-based F1 dominant, CDL quality low) → Phase 2 (mixed, formal weight rises with FVUR-syntax) → Phase 3 (formal dominant). Transition governed by FVUR-syntax monitoring.

**Formally detectable error types.** Geometric problems typically feature over-determined constraint systems where a single incorrect fact (e.g., a misread angle) propagates into detectable contradictions. However, missing-primitive errors (e.g., failing to detect a point entirely) may not produce contradictions — only information insufficiency. The M1 pilot study (below) will quantify the proportion of each error type and calibrate expectations for formal verification coverage.

**Formal verification engine.** FormalGeo's symbolic solver is the primary engine (native CDL). AlphaGeometry2's C++ DDAR (300x faster, JMLR 2025) provides optional deeper deduction for multi-step theorem applications, with CDL-to-DDAR predicate conversion validated for accuracy (concordance >90% required; if not met, DDAR is dropped). DDAR's incremental value tested via ablation.

**Targeted re-perception protocol (test time):**
1. VLM extracts facts → FormalGeo solver identifies contradictions with constraint explanations
2. Contradictions ranked by severity; top-k (k=1–2) flagged per round
3. Re-prompt VLM: "∠ABC was extracted as 90° but contradicts [constraint] — re-examine ∠ABC"
4. Re-run constraint checking on updated facts
5. Terminate: no new contradictions OR facts unchanged OR max 3 rounds

## Research Landscape

The perception bottleneck is well-documented: GPT-4o exhibits 70% error rate on geometric primitive grounding (SVE-Math, arXiv:2501.06430). CogFlow (ICLR 2026, arXiv:2601.01874) bridges perception and reasoning through knowledge internalization. EVPV (arXiv:2603.16253) separates grounding errors from reasoning errors via constraint matching and reliability-gating. GeoSketch (arXiv:2509.22460) implements diagram auto-correction via MLLM but "does not assess the correctness or validity of intermediate steps." TangramSR (arXiv:2602.05570) achieves test-time self-refinement via geometric consistency feedback (IoU 0.63→0.932 on Tangram spatial assembly), but uses heuristic IoU on continuous spatial tasks rather than formal theorem-level verification on symbolic Euclidean geometry, and is training-free. Sketch2Feedback (arXiv:2602.18520) demonstrates a perception→symbolic→constraint→feedback pipeline for STEM diagrams, validating the architecture for educational feedback.

**Closest works — key differentiations:**

| Method | Reward Type | Formal Guarantee | Diagnostic Output | Stage |
|--------|-----------|-----------------|-------------------|-------|
| SymHPR (arXiv:2512.03126) | Per-primitive F1/L2 | No (rule-based, noisy) | No | Perception |
| "Bad Seeing or Bad Thinking?" (arXiv:2605.14054) | Per-step binary PV | No (neural proxy) | No | Perception |
| PDCR (arXiv:2605.13467) | Decomposed confidence | No (scalar) | No | Perception |
| ViCrit (arXiv:2506.10128) | Binary hallucination | No (proxy task) | No | Perception |
| SGVR (arXiv:2601.05073) | Sub-goal verification | Yes | Partial | Reasoning |
| FoVer (ACL 2026, arXiv:2505.15960) | Step-level PRM data | Yes | Partial | Reasoning |
| InternGeometry (arXiv:2512.10534) | DDAR-based | Yes | No | Reasoning |
| TrustGeoGen (arXiv:2504.15780) | N/A (data generation) | Yes | N/A | Data |
| **FPR (ours)** | **Per-fact diagnostic** | **Yes (zero FP on valid CDL)** | **Yes (contradiction + theorem)** | **Perception** |

## Experimental Design

**Base model:** Qwen3-VL-8B.

**Training data:** FormalGeo7K (~7K problems with ground-truth CDL). Geometry3K for OOD evaluation only (lacks CDL). If 7K proves insufficient (A5 scaling curve unsaturated), FormalGeo7K augmentation to 133K+ is available as expansion.

**Training-time baselines:**
1. **Accuracy-only GRPO**: Binary final-answer reward
2. **SymHPR** (arXiv:2512.03126): Rule-based per-primitive F1/L2 — most critical (formal vs. rule-based)
3. **Perception-R1** (arXiv:2506.07218): Neural judge reward
4. **GeoDPO** (arXiv:2602.22703): Learned translator reward
5. **SGVR** (arXiv:2601.05073): Formal verification for reasoning only
6. **PDCR** (arXiv:2605.13467): Decomposed confidence reward (open-source)
7. **"Bad Seeing or Bad Thinking?" PV** (arXiv:2605.14054): Blindfolded reasoning proxy — conditional baseline (if code available or reproducible from method description)

**Test-time baselines:**
- Self-consistency@N (N=3, 5)
- Best-of-N + formal verification re-ranking (N=3, 5)
- Full-diagram re-processing
- No re-perception (single-pass)
- **Oracle re-perception**: Ground-truth contradiction info guides re-perception → upper bound

**Ablations:**
- A1: Formal constraint propagation reward vs. rule-based F1 (SymHPR-style) — core
- A2: FormalGeo solver only vs. FormalGeo + DDAR — deeper deduction value
- A3: Dense per-fact diagnostic reward vs. holistic binary reward — granularity
- A4: Targeted re-perception vs. all test-time baselines — mechanism evaluation
- A5: Training data scale (1K / 3K / 7K) — sample efficiency
- A6: Reward curriculum (phased rule-based→formal) vs. formal-only vs. rule-based-only — curriculum value
- A7: CDL quality sensitivity — oracle CDL (ground-truth) vs. learned CDL at SFT epochs 0/2/5 — quantifies translator bottleneck

**Evaluation benchmarks:**
- **GeoPerceive** (from GeoDPO): Perception-isolated — primary perception metric
- **GePBench** (arXiv:2412.21036): Perception-specific, independently defined
- **GeoQA, Geometry3K, PGPS9K**: Standard comprehensive benchmarks
- **MathVerse**: Cross-paper comparison (SymHPR reports +3%)

**Key metrics:**
- Per-fact precision/recall/F1 on geometric fact extraction
- FVUR-syntax: Proportion of rollouts with syntactically valid CDL entering solver
- DYR (Diagnostic Yield Rate): Proportion of valid-CDL rollouts where solver produces ≥1 per-fact diagnostic — the true measure of FPR's effective coverage
- FVUR-syntax and DYR tracked over training steps (curve)
- DYR-conditioned performance: Stratified by DYR>80% vs. DYR<50%
- Translator CDL accuracy (sentence-level + full-expression) on held-out set
- Re-perception success rate, average rounds, per-fact accuracy delta
- Oracle re-perception gap analysis: decompose into diagnostic quality gap vs. VLM re-perception capability gap
- Per-step reward computation latency for each mechanism
- Performance vs. wall-clock scaling curves; compute-matched control (baselines given equal wall-clock via more rollouts)

**Statistical rigor:** FPR + SymHPR + accuracy-only GRPO: 3 seeds (mean ± std). Other baselines: 2 seeds (range).

**Pre-experiment validation (M1):**
1. Pilot study (500 problems): Extract CDL with baseline VLM, run rule-based F1 and FormalGeo solver, measure formal-unique error proportion and error type distribution (numeric/relational vs. missing-primitive)
2. Profiling: Per-problem latency for constraint propagation + diagnostic output (FormalGeo only; FormalGeo + DDAR)
3. CDL-to-DDAR converter concordance rate on FormalGeo7K ground-truth (>90% required)
4. Translator CDL accuracy baseline (pre-SFT and post-SFT)

## Key References

- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026, 2602.22703)
- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025, 2506.07218)
- Bad Seeing or Bad Thinking? Rewarding Perception for Vision-Language Reasoning (arXiv 2026, 2605.14054)
- From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models (arXiv 2026, 2605.20177)
- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026, 2605.13467)
- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward [SGVR] (arXiv 2026, 2601.05073)
- Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs [SVE-Math] (arXiv 2025, 2501.06430)
- Solving Olympiad Geometry without Human Demonstrations [AlphaGeometry] (Nature 2024)
- Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2 (JMLR 2025)
- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (Symmetry 2024, arXiv 2310.18021)
- FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems (Symmetry 2025)
- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025, 2504.15780)
- ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs (arXiv 2025, 2506.10128)
- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026, arXiv 2601.01874)
- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025, 2512.03126)
- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026, 2603.16253)
- Efficient PRM Training Data Synthesis via Formal Verification [FoVer] (ACL 2026 Findings, arXiv 2505.15960)
- GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning (arXiv 2025, 2509.22460)
- TangramSR: Can Vision-Language Models Reason in Continuous Geometric Space? (arXiv 2026, 2602.05570)
- Sketch2Feedback: Grammar-in-the-Loop Framework for Rubric-Aligned Feedback on Student STEM Diagrams (arXiv 2026, 2602.18520)
- GePBench: Evaluating Fundamental Geometric Perception for Multimodal Large Language Models (arXiv 2024, 2412.21036)
- A Survey of Deep Learning for Geometry Problem Solving (ACL 2026 Main, arXiv 2507.11936)
- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (arXiv 2025, 2506.04592)
- InternGeometry: Olympiad-Level Geometry via Complexity-Boosted RL (arXiv 2025, 2512.10534)

## Resource Estimate

- **manual**: gpu_hours: 3000–3500 (16x A800-80G: GRPO runs + 7 ablations + 3-seed main + 2-seed baselines + evaluation), timeline: 5 months (M1: SFT warm-start + FormalGeo/DDAR integration + pilot study + profiling + converter validation + translator accuracy baseline; M2–3: GRPO training + reward curriculum + baseline reproduction; M4: evaluation + ablations + multi-seed + oracle analysis; M5: paper writing), estimated_gpu_cost: $6,000–7,000
- **human_in_loop**: gpu_hours: 2500–3000, timeline: 3.5–4 months, claude_api_cost: $300–500, estimated_gpu_cost: $5,000–6,000
- **auto_research**: gpu_hours: 3500–4500, timeline: 2.5–3 months, claude_api_cost: $1,200–2,000, estimated_gpu_cost: $7,000–9,000, speed_bottleneck: RL training wall-clock (~16–20h per GRPO run on 16x A800); formal verification throughput to be profiled in M1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f1c99dbd-7317-4051-b1bf-78e4af94d9ec",
  "type": "user",
  "uuid": "f23fd777-c0eb-4cb7-9634-15055d697022",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T09:10:23.904Z_

```json
{
  "parentUuid": "f23fd777-c0eb-4cb7-9634-15055d697022",
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
  "uuid": "1b20d61b-61d4-4420-a81b-a803c78f5347",
  "timestamp": "2026-05-27T09:10:23.904Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T09:10:23.904Z_

```json
{
  "parentUuid": "1b20d61b-61d4-4420-a81b-a803c78f5347",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f3b07bee-79f2-498d-a85e-6656a0c29f68",
  "timestamp": "2026-05-27T09:10:23.904Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research data to conduct the evaluation.…",
  "leafUuid": "f3b07bee-79f2-498d-a85e-6656a0c29f68",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal verification for geometric perception rewards",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df"
}
```

---

### Assistant

_source line 8 · 2026-05-27T09:10:49.504Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as Meta Judge.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [25% - 38%] 中位 30%

**Reviewer 2:**
- Novelty: 中
- Significance: 弱偏中
- Related Work: 中偏弱


- Probability: [18% - 28%] 中位 23%

**Reviewer 3:**
- Novelty: 中偏强
- Significance: 中
- Related Work: 强
- Probability: [28% - 38%] 中位 33%

Now I'm calculating the aggregate statistics across all three reviewers. The median probabilities are 30%, 23%, and 33%, which gives me a mean of about 28.67% and a median of 30%. Looking at the standard deviation, there's moderate variation in their assessments, with Reviewer 2 being notably more skeptical than the other two.

Examining where the reviewers actually agree, I see strong consensus on several key points: all three identify novelty as roughly "中" level, they all recognize the genuine gap in applying formal verification to perception-stage rewards, and they all flag the CDL translation bottleneck as the primary risk. There's also agreement on the domain restriction limiting significance and the "natural next step" concern about recombination. The related work coverage gets strong marks from Reviewers 1 and 3, though Reviewer 2 takes issue with missing Perceval and VPPO references. One more area of consensus is the uncertainty around whether missing-primitive errors are even detectable.

The anomalies are clearer now: Reviewer 2 stands alone in citing Perceval and VPPO as critical gaps, which leads them to downgrade related work coverage. They also rate significance lower than the other two. Reviewer 3 edges novelty slightly higher than the consensus. I need to verify whether Reviewer 2's Perceval citation is actually a legitimate concern or if it's a false positive.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3b07bee-79f2-498d-a85e-6656a0c29f68",
  "isSidechain": false,
  "requestId": "req_011CbSp8BNLqb4TzyGnB5dzN",
  "type": "assistant",
  "uuid": "cfd69667-ad8d-4c2a-a29a-ecfee9a7c812",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jrdwb2g4ivYuVLSAJDfM52",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18644,
      "cache_read_input_tokens": 16543,
      "output_tokens": 1041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1041,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18644
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

_source line 9 · 2026-05-27T09:10:50.785Z_

我需要先验证几个关键的审稿人分歧点，特别是审稿人 2 提到的 Perceval 和 VPPO 这两个 proposal 未引用的竞争者。让我做几个针对性搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfd69667-ad8d-4c2a-a29a-ecfee9a7c812",
  "isSidechain": false,
  "requestId": "req_011CbSp8BNLqb4TzyGnB5dzN",
  "type": "assistant",
  "uuid": "44da7735-0863-4a1b-9831-76034bace90a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jrdwb2g4ivYuVLSAJDfM52",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18644,
      "cache_read_input_tokens": 16543,
      "output_tokens": 1041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1041,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18644
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

### Tool call

_source line 10 · 2026-05-27T09:10:50.800Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bmkcg1BRoZLEUp1fLtQbEu`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44da7735-0863-4a1b-9831-76034bace90a",
  "isSidechain": false,
  "requestId": "req_011CbSp8BNLqb4TzyGnB5dzN",
  "type": "assistant",
  "uuid": "76b70c6c-4f31-40e0-a2cf-ee730ead5059",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jrdwb2g4ivYuVLSAJDfM52",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18644,
      "cache_read_input_tokens": 16543,
      "output_tokens": 1041,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1041,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18644
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

### Tool result

_source line 11 · 2026-05-27T09:10:50.807Z_

<details><summary>↩ Tool result · `toolu_01Bmkcg1BRoZLEUp1fLtQbEu`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76b70c6c-4f31-40e0-a2cf-ee730ead5059",
  "isSidechain": false,
  "promptId": "f1c99dbd-7317-4051-b1bf-78e4af94d9ec",
  "type": "user",
  "uuid": "a27bbdca-e60e-40b3-acde-e40db5e51474",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "76b70c6c-4f31-40e0-a2cf-ee730ead5059",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T09:10:53.752Z_

Now let me verify the key disputed claims from the reviewers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a27bbdca-e60e-40b3-acde-e40db5e51474",
  "isSidechain": false,
  "requestId": "req_011CbSpAAQrHm2kbjFZVgGca",
  "type": "assistant",
  "uuid": "edf57917-3054-4052-9fbb-594656b3754c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SprSY3Rot5ZbmKtiP7uLs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1569,
      "cache_read_input_tokens": 35187,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 35187,
          "cache_creation_input_tokens": 1569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1569
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

### Tool call

_source line 13 · 2026-05-27T09:10:54.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015kH6Q7aW1td4S7SFQwuaXB`</summary>

```json
{
  "query": "Perceval perception-centric process reward model VLM arXiv 2604.24583"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edf57917-3054-4052-9fbb-594656b3754c",
  "isSidechain": false,
  "requestId": "req_011CbSpAAQrHm2kbjFZVgGca",
  "type": "assistant",
  "uuid": "ec8a7fc0-3dce-4656-a2af-9540da465f73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SprSY3Rot5ZbmKtiP7uLs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1569,
      "cache_read_input_tokens": 35187,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 35187,
          "cache_creation_input_tokens": 1569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1569
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

### Tool result

_source line 14 · 2026-05-27T09:10:54.236Z_

<details><summary>↩ Tool result · reported error · `toolu_015kH6Q7aW1td4S7SFQwuaXB`</summary>

```text
Claude requested permissions to use WebSearch, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec8a7fc0-3dce-4656-a2af-9540da465f73",
  "isSidechain": false,
  "promptId": "f1c99dbd-7317-4051-b1bf-78e4af94d9ec",
  "type": "user",
  "uuid": "eb358b61-314e-4ab4-99f1-9f650bd2a866",
  "toolUseResult": "Error: Claude requested permissions to use WebSearch, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "ec8a7fc0-3dce-4656-a2af-9540da465f73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T09:10:55.845Z_

<details><summary>↩ Tool result · reported error · `toolu_013GgSw7NymAEjvAUKo9YZqy`</summary>

```text
Claude requested permissions to use WebSearch, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ff4c9a7-004d-4309-81b3-c78b6adc444e",
  "isSidechain": false,
  "promptId": "f1c99dbd-7317-4051-b1bf-78e4af94d9ec",
  "type": "user",
  "uuid": "d79595d8-926a-494d-8e3b-78486d6ca681",
  "toolUseResult": "Error: Claude requested permissions to use WebSearch, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "3ff4c9a7-004d-4309-81b3-c78b6adc444e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T09:10:55.244Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NtdUeHNgLqE1NuP1RU21TY`</summary>

```json
{
  "query": "VPPO token perception multimodal reinforcement learning arXiv 2510.09285 ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb358b61-314e-4ab4-99f1-9f650bd2a866",
  "isSidechain": false,
  "requestId": "req_011CbSpAAQrHm2kbjFZVgGca",
  "type": "assistant",
  "uuid": "21c7b8d6-1cdb-4d32-ae64-ce854a4c6d58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SprSY3Rot5ZbmKtiP7uLs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1569,
      "cache_read_input_tokens": 35187,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 35187,
          "cache_creation_input_tokens": 1569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1569
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

### Tool result

_source line 17 · 2026-05-27T09:10:55.245Z_

<details><summary>↩ Tool result · reported error · `toolu_01NtdUeHNgLqE1NuP1RU21TY`</summary>

```text
Claude requested permissions to use WebSearch, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21c7b8d6-1cdb-4d32-ae64-ce854a4c6d58",
  "isSidechain": false,
  "promptId": "f1c99dbd-7317-4051-b1bf-78e4af94d9ec",
  "type": "user",
  "uuid": "6c44ace6-944e-4731-b926-3eb3b4589c27",
  "toolUseResult": "Error: Claude requested permissions to use WebSearch, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "21c7b8d6-1cdb-4d32-ae64-ce854a4c6d58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T09:10:55.844Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013GgSw7NymAEjvAUKo9YZqy`</summary>

```json
{
  "query": "FGeo-Parser CDL autoformalization accuracy 56% FormalGeo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c44ace6-944e-4731-b926-3eb3b4589c27",
  "isSidechain": false,
  "requestId": "req_011CbSpAAQrHm2kbjFZVgGca",
  "type": "assistant",
  "uuid": "3ff4c9a7-004d-4309-81b3-c78b6adc444e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SprSY3Rot5ZbmKtiP7uLs8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1569,
      "cache_read_input_tokens": 35187,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 202,
          "cache_read_input_tokens": 35187,
          "cache_creation_input_tokens": 1569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1569
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

_source line 19 · 2026-05-27T09:11:45.679Z_

<details><summary>Logged reasoning block</summary>

```text
WebSearch is not available right now. I'll proceed with the information I have from the three reviewers. Let me analyze based on what's provided.

Given that I can't do web searches, I should note this limitation and proceed with the synthesis based on the three reviews. The reviewers have already done substantial research, so I can work with their findings.

Let me now synthesize:

**Three medians:** 30%, 23%, 33%
**Std calculation:** 
- Mean = (30+23+33)/3 = 28.67
- Variance = ((30-28.67)² + (23-28.67)² + (33-28.67)²)/3 = (1.78 + 32.15 + 18.75)/3 = 17.56


- Std ≈ 4.19%

This falls into "中一致" territory with a standard deviation between 3-7%. Looking at the consensus dimensions, all three reviewers converge on novelty being "中" — they recognize the gap is genuine but view it as a natural progression rather than a breakthrough. The CDL translation bottleneck emerges as the unanimous structural risk across all reviewers.

The empirical performance shows 56.5% full-expression accuracy with potential degradation in the SymHPR variant, and there's broad agreement that domain constraints matter significantly — the work is limited to Euclidean geometry within FormalGeo's scope and dataset scale. What stands out as genuinely novel across all three assessments is how diagnostic output feeds back into targeted re-perception, moving beyond simple scalar metrics. SymHPR becomes the critical baseline for determining whether formal verification outperforms rule-based approaches, though all reviewers flag that missing-primitive errors may slip through undetected. There's also consensus that best-of-N sampling combined with formal filtering represents a straightforward alternative that needs empirical testing against the proposed approach.

R2 raises a significant concern about Perceval, claiming it achieves per-claim error grounding and test-time correction through neural process reward models — functionally overlapping with FPR's diagnostic pipeline. The citation details (April 2026, token-level grounding) suggest this is a real paper, though I can't verify it independently, so I'm treating this as a moderate-weight concern about narrowed novelty. R2 also flags VPPO as targeting perceptually pivotal tokens via reinforcement learning, though it's less directly competitive. Across the board, R2 rates the related work as moderately weak compared to R1 and R3's stronger assessments. entirely by the Perceval/VPPO omissions. If those omissions are real, this downgrade has merit, but R1 and R3 independently judged Related Work as strong.

4. **R2: Significance = 弱偏中** (vs. R1: 中, R3: 中) — R2 is more pessimistic about significance, emphasizing domain restriction more heavily and the "not surprising if positive" test.

5. **R3: Novelty = 中偏强** (vs. R1: 中, R2: 中) — R3 gives more credit to the "scoring to diagnosing" paradigm shift. This is an outlier on the high side.

**Handling the anomalies:**

- R2's Perceval finding is the most consequential anomaly. Since R2 provides a specific arXiv ID and detailed description showing that Perceval achieves per-claim diagnosis with neural methods, this does narrow FPR's novelty to the formal guarantee aspect. I'll weight this moderately because of the specificity, though FPR's formal methods and theorem-level explanations still differentiate it from Perceval's neural approach.

- R2's lower Significance rating is somewhat of an outlier, but the reasoning about domain restriction is sound. Since two reviewers rate it 中, I won't fully adopt this lower assessment.

- R3's higher Novelty rating acknowledges the same concerns but credits the paradigm shift more. With R1 and R2 both at 中, I'll lean toward that consensus.

**Final synthesis:**

Consensus Novelty: 中 (the "scoring to diagnosing" shift is real but a natural extension)
Consensus Significance: 中 (with downward pressure from R2's concerns)
Related Work: 中偏强 (R1 and R3 say 强; R2 says 中偏弱 due to Perceval omission — if Perceval is real, the omission is meaningful but addressable)

Per the "中一致" rule: expand the interval, lean toward the stricter assessment.

R2's 23% is the strictest estimate. The key drivers are Perceval's omission, lower significance assessment, and lower related work assessment. If Perceval's findings are valid, they do narrow FPR's practical novelty, though the formal guarantee remains a genuine differentiator.

Now I'm synthesizing across reviewers: R2's Perceval concerns are legitimate but fixable through proper citation and differentiation. The CDL bottleneck risk is the most robust concern since all three reviewers flag it. The "natural extension" perception is what's really limiting novelty perception across the board.

Given the "中一致" rule with a lean toward stricter judgment, I should position myself between R2's assessment and the others' views. That puts me around 27-28% as a median, with a range from roughly 20% up to 35%. I need to verify my upper bound against the most optimistic estimate—R3's range goes up to 38%, and my 34% ceiling stays below that, so that constraint is satisfied. Let me lock in the final range at [20% - 34%] with a midpoint of 27%, which appropriately leans toward the stricter interpretation as required. Now I'm moving on to assess the implementation feasibility by synthesizing the findings from all three reviews alongside the proposal's resource projections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d79595d8-926a-494d-8e3b-78486d6ca681",
  "isSidechain": false,
  "requestId": "req_011CbSpAYXNrukDSEjgpnAFD",
  "type": "assistant",
  "uuid": "1542ba96-926d-4473-b309-c6b25d4a0bb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Rnn7QDNxeiFfUpQzeZKVu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 36756,
      "output_tokens": 5287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5287,
          "cache_read_input_tokens": 36756,
          "cache_creation_input_tokens": 333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 333
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

_source line 20 · 2026-05-27T09:12:55.039Z_

WebSearch 权限未开放，我将基于三位审稿人已提供的详尽调研结果进行综合判断。三位审稿人各自引用了 12-15 篇 2024-2026 年的相关工作，调研覆盖充分，可以支撑 Meta Judge 综合。

让我系统整理三方评估的共识与分歧。

---

【阶段】: Meta Judge
【三次中位】: [30%, 23%, 33%]  std=4.2%
【共识维度】:
- **Novelty = 中**（3/3 一致，R3 略偏强但仍在中区间）：核心 gap 真实——无现有工作将 formal geometric constraint propagation 应用于 perception-stage reward 并产生 per-fact diagnostic output。但三位审稿人一致认为这是"natural next step"——formal verification 已在 reasoning stage 成功，perception reward 是活跃方向，FormalGeo CDL 工具链成熟，三者组合属预期性延伸而非 surprising insight。"从 scoring 到 diagnosing"的质变被三位审稿人均认可为真实增量价值，但增量幅度存疑。
- **CDL translation bottleneck 是 #1 结构性风险**（3/3 一致）：FGeo-Parser 完整表达式准确率仅 56.5%。若 SFT warm-start 后 FVUR-syntax 仍低，formal verification 组件在大部分 rollouts 中不触发，方法退化为 SymHPR 变体。三位审稿人均指出这不仅是执行风险，更是 idea logic chain 的薄弱环节——审稿人在 reading 阶段就会质疑 formal guarantee 的实际覆盖面。
- **Significance = 中**（R1: 中, R2: 弱偏中, R3: 中，2/3 判"中"）：domain restriction（仅 Euclidean geometry + FormalGeo CDL）、FormalGeo7K 数据规模小（~7K）、方法不可直接推广至其他视觉数学领域，三位审稿人均提及。"如果结果 positive，审稿人是否会 surprised？"——R2 明确指出答案可能是 No（formal 比 rule-based 更精确是预期结果），这压低了 significance 的上限。
- **SymHPR 是最关键 baseline**（3/3 一致）：formal vs. rule-based F1 的增量是核心论证的成败关键。若 ablation 显示差异不显著，"engineering complexity without sufficient empirical payoff"将成为拒稿理由。
- **Missing-primitive errors 限制 formal verification 覆盖率**（3/3 一致）：漏检整个点/线不产生矛盾，只产生信息不足，formal verification 无法检测。DYR 可能远低于预期。
- **Best-of-N + formal filtering 作为 trivial alternative**（3/3 一致）：proposal 已回应但论证需实验支撑，非逻辑自明。
- **Related Work 覆盖面广**（R1: 强, R3: 强，2/3 判"强"）：proposal 引用 25+ 篇 2024-2026 相关工作，经三位审稿人独立调研验证，所有引用真实存在且描述准确，差异化定位清晰。

【异常维度】:
- **R2 独有——Perceval (arXiv:2604.24583) 和 VPPO (arXiv:2510.09285) 未被 proposal 引用**：R2 认为 Perceval 通过 neural PRM 实现了功能相似的"per-claim error grounding + targeted test-time correction"，显著压缩 FPR 的实际 novelty 空间。R1 和 R3 均未提及此工作。R2 提供了具体 arXiv ID 和详细描述，可信度较高。**处理**：Perceval 使用 neural PRM（非 formal methods），FPR 的 formal guarantee + theorem-level explanation 仍是真实差异化。但 Perceval 的存在确实缩窄了 FPR 的"独特价值"从"诊断性反馈"缩小到"formal 保证下的诊断性反馈"——这是一个有意义的压缩。给予中等权重：Related Work 维度从"强"降为"中偏强"（可通过补充引用修复），Novelty 维度不变（formal guarantee 仍是真实差异化）。
- **R2 独有——Significance 评为"弱偏中"**：R2 更强调"not surprising if positive"测试和领域限制。R1、R3 均评"中"。**处理**：R2 的推理逻辑合理但偏严苛——"formal 比 rule-based 精确"确实不 surprising，但"诊断性反馈启用 targeted re-perception"这个机制如果效果显著，仍有一定 surprise。维持 Significance = 中，但注记 R2 的下行风险。
- **R3 独有——Novelty 评为"中偏强"**：R3 给"scoring to diagnosing"质变更多 credit。R1、R2 均评"中"。**处理**：R3 的推理有道理但偏乐观——降权至"中"以符合多数判断。
- **R2 独有——Related Work 评为"中偏弱"**：完全由 Perceval/VPPO 遗漏驱动。**处理**：遗漏是真实的但可修复（补充引用即可），且 R1 和 R3 在不知 Perceval 的情况下独立判"强"。综合为"中偏强"。

【最终概率】: [20% - 34%] 中位 27%
【一致性】: 中（std=4.2%，偏向严格方）
【综合理由】:
三位审稿人在核心判断上高度一致：gap 真实但偏 natural combination，significance 受 domain restriction 限制，CDL bottleneck 是结构性风险。主要分歧来自 R2 发现的 Perceval 竞争者（其他两位未覆盖）和 R2 对 significance 的更严格评估。

按"中一致、偏严格方"原则处理：
- **中位 27%**（低于三方中位数的均值 28.7%，向 R2 的 23% 倾斜但不完全采纳，因为 R2 的部分降分依据是单一审稿人发现的 Perceval 且 formal guarantee 仍是真实差异化）
- **下界 20%**（反映 R2 的悲观情景：Perceval 功能等价 + CDL 瓶颈导致 formal reward 实际不起作用 + significance 弱偏中）
- **上界 34%**（反映 R3 的乐观情景：diagnostic mechanism 被认可为范式创新 + 实验充分展示 formal vs. rule-based 增量，但不超过 R3 的 38% 上界——因 Perceval 遗漏需修复后才能达到上界附近）

概率天花板由 Novelty（中）和 Significance（中）共同决定：即使实验完美，"natural combination + narrow domain"的组合使上界难以突破 ~35%。概率地板由 Related Work 强度（可修复至强）和 diagnostic mechanism 的真实增量支撑在 ~20%。

【建议】: 边缘（偏不推荐侧）
- 中位 27% 处于"有实质内核但不够 compelling"的区间
- 核心风险（CDL bottleneck、Perceval 功能等价竞争、significance 天花板）均是结构性的，非实验层面可完全化解
- 但 gap 真实、related work 扎实、实验设计周全——如果 M1 pilot study 结果乐观（FVUR-syntax > 70%、DYR > 60%、formal-unique error proportion > 15%），概率可上移至 30-35% 区间
- 建议进入迭代优化，重点解决：(1) 补充 Perceval/VPPO 引用并强化差异化论证；(2) 锐化 diagnostic mechanism 的独特价值（vs. Perceval 的 neural diagnosis）；(3) 增强 significance 论证（超越几何领域的可推广性框架）

【实施评估】:
- **计算资源**: 16× A800-80G，GPU 总量 3000-4500 小时（含 GRPO 主训练 + 7 ablations + 多 seed + baseline 复现 + evaluation），预估 GPU 成本 $5,000-9,000
- **数据需求**: FormalGeo7K（~7K 带 ground-truth CDL 标注的几何问题，公开可得）；Geometry3K（OOD 评估，公开）；GeoPerceive、GePBench、GeoQA、PGPS9K、MathVerse（公开 benchmark）。若 7K 不足，FormalGeo7K augmentation 至 133K+ 可用但增加工程复杂度
- **人工介入**: M1 pilot study 需人工验证 CDL translation 质量和 error type distribution（~500 问题的人工检查）；CDL-to-DDAR converter concordance 验证需专家参与；其余流程可自动化。整体人工介入量中等
- **训练需求**: 需要模型训练。SFT warm-start（Qwen3-VL-8B on FormalGeo7K ground-truth CDL）+ GRPO 训练（含 reward curriculum）。单次 GRPO run 约 16-20h on 16× A800。主实验 + ablations + 多 seed 总训练量约 15-20 次 GRPO runs
- **新 Benchmark**: 不需要构建新 benchmark，使用现有公开 benchmark。但需要定义新指标（FVUR-syntax、DYR）并在训练过程中追踪
- **预估周期**: 3.5-5 个月（M1: SFT + 工具链集成 + pilot study 1-1.5 月；M2-3: GRPO 训练 + baseline 复现 1.5-2 月；M4: evaluation + ablations 1 月；M5: 论文撰写 0.5-1 月）。关键路径瓶颈：M1 pilot study 结果决定项目是否继续（CDL 有效率和 DYR 是 go/no-go 门控）

Sources:
- [SymHPR](https://arxiv.org/abs/2512.03126)
- [GeoDPO](https://arxiv.org/abs/2602.22703)
- [Perceval](https://arxiv.org/abs/2604.24583)
- [VPPO](https://arxiv.org/abs/2510.09285)
- [FGeo-Parser](https://www.mdpi.com/2073-8994/17/1/8)
- [FormalGeo](https://arxiv.org/abs/2310.18021)
- [Bad Seeing or Bad Thinking?](https://arxiv.org/abs/2605.14054)
- [PDCR](https://arxiv.org/abs/2605.13467)
- [ViCrit](https://arxiv.org/abs/2506.10128)
- [SGVR](https://arxiv.org/abs/2601.05073)
- [TrustGeoGen](https://arxiv.org/abs/2504.15780)
- [SVE-Math](https://arxiv.org/abs/2501.06430)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1542ba96-926d-4473-b309-c6b25d4a0bb0",
  "isSidechain": false,
  "requestId": "req_011CbSpAYXNrukDSEjgpnAFD",
  "type": "assistant",
  "uuid": "ce5fe399-8565-4034-9ff8-61bab6ff79b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Rnn7QDNxeiFfUpQzeZKVu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 36756,
      "output_tokens": 5287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5287,
          "cache_read_input_tokens": 36756,
          "cache_creation_input_tokens": 333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 333
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research data to conduct the evaluation.…",
  "leafUuid": "ce5fe399-8565-4034-9ff8-61bab6ff79b9",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal verification for geometric perception rewards",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research data to conduct the evaluation.…",
  "leafUuid": "ce5fe399-8565-4034-9ff8-61bab6ff79b9",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal verification for geometric perception rewards",
  "sessionId": "6b291280-c27e-4d0f-a048-8df8254260df"
}
```

---
