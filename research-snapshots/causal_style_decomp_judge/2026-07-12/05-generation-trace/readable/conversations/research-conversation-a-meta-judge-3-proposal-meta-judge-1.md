# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/946f8a36-ca3e-4ca9-aae2-ae39a65089ff.jsonl`
- **Structured JSON:** [`ee7b1e8d3ec9b2049537.json`](../../sessions/ee/ee7b1e8d3ec9b2049537.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:58:27.335Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:58:27.335Z",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- \"Variation in Verification\" (arXiv 2509.17995, ICLR 2026): 直接奠基论文。揭示了验证器在不同问题难度/生成器能力下的异构可靠性（TPR/TNR随难度变化），为JOVA的difficulty-conditioned routing提供了核心empirical motivation。JOVA可视为对该发现的operational化。\n- Strategic Scaling Bandit (Zuo et al., arXiv 2506.12721): 最接近的adaptive-K工作。用UCB bandit自适应调整K，MATH-500上+11.1%。但固定verifier类型不变。JOVA在此基础上增加了d维度的联合优化，差异化清晰。\n- Montgomery et al. Budget-aware Verification (arXiv 2510.14913): 最接近的hybrid verification工作。证明discriminative+generative hybrid在固定budget下surpass纯generative达15.3%（AIME25）。但采用per-dataset uniform策略，无per-instance difficulty conditioning。JOVA的per-instance routing是明确的增量贡献。\n- AVA: Anytime Verified Agents (OpenReview 2026): 最接近的multi-dimensional allocation工作。动态分配compute across search/sampling/verification，用calibrated uncertainty + early exit cascades。与JOVA的关键差异：uncertainty-driven vs difficulty-driven，continuous allocation vs discrete (K,d) menu。两者在机制层面有实质差异，但reviewer可能质疑difficulty和uncertainty的相关性。\n- GenPRM (arXiv 2504.00891, AAAI 2026): 当前verification SOTA，1.5B GenPRM超GPT-4o。但仍是单一fixed verifier，不做adaptive routing。JOVA将其作为verifier hierarchy最高层，定位合理。\n- DiffAdapt (ICLR 2026): 难度自适应推理长度（非verification type选择），token reduction 62%。与JOVA正交但共享difficulty-adaptive思路，说明difficulty conditioning是当前热点。\n- DTR (arXiv 2602.13517): JOVA依赖的difficulty signal。r=0.683 average accuracy correlation，但仅在≥30B模型上验证。≤14B模型上的有效性是JOVA的关键风险点。\n- LiLaVe (arXiv 2504.16760): JOVA最底层verifier（Latent-ORM）。几乎零开销的hidden-state verification，与大型LLM verifier comparable。可行性已验证。\n- MAV: Multi-Agent Verification (arXiv 2502.20379): ensemble所有verifiers vs JOVA的per-instance selection/routing。在budget-constrained场景下，routing比ensemble更合理。差异化论证充分。\n- FlexiVe/SDV (arXiv 2505.11966): binary fast/slow verification via GRPO。JOVA推广至4-tier hierarchy，是明确的generalization。\n- CPO (arXiv 2604.14853): constrained policy optimization for reasoning strategy selection，12.8% relative improvement under matched budget。方法论上与JOVA互补（CPO优化reasoning策略，JOVA优化verification策略）。\n\n- 调研总结: Test-time compute的adaptive allocation是2025-2026年的核心热点，但现有工作均沿单一维度优化（K、verification granularity、binary type、reasoning length、model routing）。JOVA提出的(K,d)联合优化在文献中确实没有直接先例，gap identification成立。但该领域进展极快，竞争激烈，JOVA需要在empirical gains上给出convincing evidence才能脱颖而出。\n\n【整体印象】: \n作为审稿人，第一反应是\"这是一篇非常well-prepared的proposal\"。文献覆盖广泛且精准（引用了~25篇高度相关工作并逐一区分），问题formulation清晰（(K,d)联合优化under shared budget），实验设计极其详尽（8个baselines、6个ablation、8个budget levels、多benchmark多模型）。Simpson's Paradox类比很巧妙，composition gap的分析框架有理论深度。\n\n然而，核心concern是这本质上是一个routing/scheduling problem over existing components——没有提出新的verification方法，没有训练新模型，创新在于\"如何组合已有工具\"。一个tough reviewer可能将其定性为\"systems/engineering contribution\"而非\"scientific contribution\"。另一个关键风险是Grid-Search-(K,d)-per-bucket这个strong trivial baseline：如果简单的per-difficulty-bin lookup table就能capture大部分joint optimization gain，JOVA的learned routing的marginal value会很小。\n\n总体倾向：borderline，偏向weak accept方向。如果empirical results显示composition gap显著（>3%）且JOVA大幅超越grid-search baseline，可以push到accept。\n\n【核心贡献】: \n1. 识别并formalize了(K,d)联合优化问题——在shared compute budget下，generation数量与verification类型的耦合关系。这一formulation本身有价值。\n2. 提出composition gap概念——independent optimization of K and d vs joint optimization的accuracy差距在medium-difficulty regime最大。这是一个可验证的structural prediction。\n3. Difficulty-conditioned routing over a verifier hierarchy——从latent-ORM到GenRM的4-tier hierarchy，per-instance选择最优(K,d)组合。\n4. 极其完备的实验方案——从Phase 0 pilot到完整ablation，包含了几乎所有可能被reviewer要求的分析。\n\n贡献的核心价值：中等偏上。(K,d)联合优化的gap确实存在且被系统性忽视，但贡献本质是\"更好的组合策略\"而非\"新方法\"。如果composition gap empirically显著，价值会上升；如果marginal，价值有限。\n\n【方法合理性】: \n方法在技术上是合理的。DTR→difficulty estimation→(K,d) routing是自然的pipeline。UCB bandit refinement有理论基础。4-tier verifier hierarchy的cost structure是realistic的（latent-ORM ~2% of c_g, GenRM ~76× of c_g）。\n\n**更简单的替代方案风险**：Grid-Search-(K,d)-per-bucket（per difficulty tercile的static lookup）是一个非常强的trivial baseline。Proposal承认了这一点并给出了三个反驳论证（continuous difficulty, domain-specific factors, distribution shift），但这些论证偏理论化，需要empirical验证。如果grid-search baseline在MATH-500上只差1-2%，continuous routing的复杂性难以justify。\n\nDTR dependency是另一个concern——DTR在≤14B模型上未验证，fallback signals（logit entropy, SC agreement）可能显著弱于DTR。如果fallback signal只有r~0.4-0.5，routing quality会大幅下降。不过proposal设计了Phase 0来explicitly验证这一点，并设定了r≥0.6的proceed threshold，这是负责任的设计。\n\n方法本身没有致命缺陷，但其有效性高度依赖于：(1) difficulty signal的质量，(2) composition gap的实际大小，(3) grid-search baseline的competitiveness。\n\n【5 维度打分】:\n  1. 研究问题: [强] — (K,d)联合优化的gap在文献中确实系统性未被addressed。Variation in Verification (ICLR 2026)揭示了heterogeneous reliability，Montgomery et al.证明了hybrid verification的价值，Strategic Scaling bandit证明了adaptive K的价值，但没有work将这些dimension joint起来。问题重要性和timeliness都很好。唯一的minor concern是这个问题是否\"足够大\"——如果composition gap只有1-2%，研究问题的significance就打折扣。\n  \n  2. 方法与创新: [中] — 方法在技术上合理，(K,d) formulation清晰，UCB+DTR pipeline自然。但创新主要在formulation和组合层面，没有新的verification method、新的training paradigm或新的theoretical result。与Strategic Scaling bandit (Zuo et al.)相比，增量是加了d维度；与Montgomery et al.相比，增量是per-instance conditioning。每个增量都合理但不transformative。Grid-search baseline的潜在competitiveness进一步压缩了novelty空间。AVA (OpenReview 2026)在multi-dimensional allocation上也做了类似的工作，虽然机制不同，但narrative上有overlap。\n  \n  3. 实验设计: [强] — 这可能是proposal最突出的优势。8个compute-matched baselines（覆盖了所有主要competing approaches），6个ablation configurations（完整分离K/d/router各component的贡献），8个log-spaced budget levels，多benchmark（MATH-500/AIME25/GPQA），多model scale（8B/14B/32B，optional 671B），Phase 0 pilot验证核心假设，bootstrap CI + multi-seed。特别值得肯定的：(a) composition gap的direct measurement（JOVA-full vs max(Fix-d-best, Fix-K-best)），(b) tier dropout分析（验证4-tier vs 2/3-tier的marginal value），(c) router robustness分析（simulated routing error），(d) grid-search baseline的explicit inclusion。这套实验设计在AAAI投稿中属于top-tier水平。\n  \n  4. 可行性: [中] — 总compute ~350-550 A100-hours，对academic lab是可承受的。所有components（DTR, LiLaVe, open-source PRMs, GenRM via self-verification）都有现成实现或straightforward复现。主要风险：(a) DTR在≤14B模型上可能失效（mitigated by Phase 0 + fallback signals），(b) verifier hierarchy可能non-monotonic（mitigated by Phase 0验证 + 声明hierarchy是hypothesis not assumption），(c) AIME25只有30题，statistical power有限（mitigated by ≥10 seeds，但仍然marginal）。时间线合理（target AAAI 2027 = Jul 28 deadline），但如果Phase 0结果不理想需要pivot，时间会紧。\n  \n  5. 写作与呈现: [强] — Proposal结构清晰，逻辑链完整：motivation（heterogeneous reliability + cost coupling）→ structural insight（composition gap in medium difficulty）→ method（JOVA）→ experiments。文献review非常thorough且有differentiation。Simpson's Paradox类比增强了可读性。Honest limitation acknowledgment（DTR仅验证在≥30B，hierarchy是hypothesis不是assumption）增加了可信度。技术细节（cost model C(K,d) = K·(c_g + c_v(d))，FLOPs calibration，pilot overhead inclusion in cost model）体现了严谨性。\n\n【概率估计】: [25% - 38%] 中位 32%\n\n【估计理由】: \n这是一篇preparation质量远高于average AAAI submission的proposal——literature coverage、experimental design、problem framing都是professional级别的。研究问题genuine且timely，gap identification成立。实验设计的completeness本身是significant加分项。\n\n然而，以下因素压制了概率上限：\n(1) **Novelty concern**：核心贡献是routing/scheduling over existing components，没有new method或new model。一个tough reviewer（尤其是方法论导向的）可能给\"limited novelty\"。在AAAI这种large venue，novelty bar比workshop高但比ICML/NeurIPS稍低，这有一定buffer。\n(2) **Empirical risk**：composition gap的实际大小未知。如果grid-search per-bucket baseline已经capture了80%+的joint optimization gain，JOVA的learned routing marginal value变小，paper的story会被削弱。\n(3) **领域拥挤**：Test-time compute allocation是2025-2026最热门的方向之一，AVA、CPO、Strategic Scaling等多个concurrent work在抢占类似的narrative space。reviewer可能因为\"yet another adaptive allocation paper\"而打低分。\n(4) **执行依赖**：DTR在target model scale上的有效性、verifier hierarchy的实际shape都是unknowns。Phase 0设计虽好，但如果结果不理想，pivot成本高。\n\n综合来看，32%中位数反映了\"solid preparation + clear gap + strong experiment design\"vs \"novelty concern + empirical uncertainty + crowded field\"的balance。如果empirical results strong（composition gap >3%, JOVA大幅超越grid-search），可以push到40%+区间。\n\n【主要风险】: \n1. **Composition gap可能很小**：如果independently optimizing K and d只比jointly优化差1-2%，整篇论文的核心contribution被undermined。Grid-search per-bucket baseline可能surprisingly competitive，让learned routing的marginal value不足以justify complexity。这是最可能导致reject的风险。\n2. **Novelty perceived as incremental**：Reviewer可能认为\"routing over existing verifiers conditioned on difficulty\"是一个engineering contribution而非scientific contribution，尤其在concurrent work（AVA、CPO、Strategic Scaling）已经占据了adaptive allocation narrative的背景下。即使gap identification正确，\"just putting existing pieces together\"的perception可能导致borderline reject。\n\n【实施评估】:\n  - 计算资源: ~350-550 A100-hours，对有GPU集群access的academic lab可行。Phase 0 pilot (~50h)可快速验证核心假设，降低sunk cost风险。\n  - 数据需求: 使用公开benchmark（MATH-500, AIME25, GPQA-Diamond），无custom数据集需求。所有verifier模型均为open-source（InternLM2-7B-Reward, Skywork-o1-Open-PRM等）。\n  - 人工介入: 无human annotation需求。需要moderate engineering effort搭建multi-verifier pipeline、DTR extraction、UCB bandit training。\n  - 训练需求: 极少。LiLaVe需训练XGBoost（trivial）。UCB bandit需在validation split上pre-train（lightweight）。无LLM fine-tuning。\n  - 新 Benchmark: 不需要。使用现有established benchmarks。\n  - 预估周期: Phase 0 (1-2周) + Phase 1 (2-3周) + Phase 2 (2-3周) + Phase 3 (1-2周) + 写作 (2-3周) ≈ 8-13周。对AAAI 2027 (Jul 28 deadline) timeline充裕。\n```\n\nSources:\n- [Variation in Verification (arXiv 2509.17995)](https://arxiv.org/abs/2509.17995)\n- [Strategic Scaling of Test-Time Compute: A Bandit Learning Approach (arXiv 2506.12721)](https://arxiv.org/abs/2506.12721)\n- [Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913)](https://arxiv.org/abs/2510.14913)\n- [AVA: Anytime Verified Agents (OpenReview 2026)](https://openreview.net/forum?id=JMDCMf7mlF)\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models (AAAI 2026)](https://github.com/RyanLiu112/GenPRM)\n- [DiffAdapt: Difficulty-Adaptive Reasoning (ICLR 2026)](https://arxiv.org/pdf/2510.19669)\n- [Think Deep, Not Just Long: DTR via Deep-Thinking Tokens (arXiv 2602.13517)](https://arxiv.org/abs/2602.13517)\n- [LiLaVe: Lightweight Latent Verifiers (arXiv 2504.16760)](https://arxiv.org/abs/2504.16760)\n- [Multi-Agent Verification: BoN-MAV (arXiv 2502.20379)](https://arxiv.org/pdf/2502.20379)\n- [FlexiVe/SDV (arXiv 2505.11966)](https://arxiv.org/pdf/2505.11966)\n- [Adaptive TTC via Constrained Policy Optimization (arXiv 2604.14853)](https://arxiv.org/abs/2604.14853)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough information to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [When To Solve, When To Verify (Singhi et al.)](https://arxiv.org/abs/2504.01005) (COLM 2025): 建立了 SC vs GenRM 的聚合 scaling law，发现在大多数实际 budget 下 SC 优于 GenRM。本 proposal 的核心出发点——认为这一聚合结论掩盖了 difficulty-heterogeneous 的结构——直接建立在此工作之上，是合理的理论推进。\n- [Variation in Verification](https://arxiv.org/abs/2509.17995) (ICLR 2026): 实证展示了不同验证方法在不同难度下的异质可靠性（TPR/TNR 差异），为本 proposal 的 difficulty-conditioned routing 提供了直接经验支持。proposal 正确引用并基于此构建。\n- [Strategic Scaling Bandit (Zuo et al.)](https://arxiv.org/abs/2506.12721): 用 UCB bandit 自适应调整 K，在 MATH-500 上获得 11.1% 提升，但假设固定 verifier。是本 proposal 的关键 baseline，JOVA 在其基础上增加了 d 维度。\n- [VG-Search (Chen et al.)](https://arxiv.org/abs/2505.11730): 统一 beam search 和 BoN 的连续粒度参数，减少 52% FLOPs，但不在验证类型间选择。是重要 baseline。\n- [GenPRM](https://arxiv.org/abs/2504.00891) (AAAI 2026): 当前验证 SOTA，1.5B GenPRM 超越 GPT-4o 的 BoN 选择。proposal 将其作为最高成本 tier 纳入，合理。\n- [Budget-aware Verification (Montgomery et al.)](https://arxiv.org/abs/2510.14913): 混合 discriminative+generative 验证在 AIME25 上超过纯 generative 15.3%，但采用 uniform per-dataset 策略。是最接近的竞争工作之一，JOVA 的差异化在于 per-instance difficulty conditioning。\n- [Multi-Agent Verification (MAV)](https://arxiv.org/abs/2502.20379): 通过投票组合多个异构 verifier。MAV 是 ensemble（全用），JOVA 是 routing（选一个）。在 budget 受限时 routing 比 ensemble 更合理。\n- [LiLaVe](https://arxiv.org/abs/2504.16760): 基于隐状态的近零成本验证，XGBoost 浅层模型。proposal 将其作为最低成本 tier。\n- [DTR / Think@n](https://arxiv.org/abs/2602.13517): 基于深度思考 token 比率的难度信号，r=0.828 准确度相关。proposal 以此为核心路由信号，但诚实承认仅在 ≥30B 模型上验证过。\n- [AVA (Anytime Verified Agents)](https://openreview.net/forum?id=JMDCMf7mlF) (OpenReview 2026): 动态分配 compute 于 search/sampling/verification，基于 uncertainty 的 cascade。与 JOVA 并行但方法论不同（uncertainty vs difficulty, cascade vs routing）。\n- [CPO](https://arxiv.org/abs/2604.14853): 使用约束策略优化的自适应推理策略选择，12.8% 相对提升。在 adaptive reasoning 方向上的竞争工作。\n- [FlexiVe/SDV](https://arxiv.org/abs/2505.11966): 快/慢二元验证，通过 GRPO 门控。JOVA 扩展到 4-tier 层级。\n- [Route to Reason (RTR)](https://arxiv.org/abs/2505.19435): 学习压缩表示以联合选择模型和推理策略。路由思路相近但在模型层面而非验证类型层面。\n\n- 调研总结: 2025-2026 年 test-time compute 的自适应分配是极热门方向，但现有工作均在单一维度优化（K、粒度、二元类型、推理长度、模型路由）或无选择地组合所有 verifier。在 (K, d) 二维联合优化 + difficulty-conditioned routing 这一特定组合上，proposal 确实占据了一个未被填充的 niche，但该 niche 的实际增量价值需实验验证。\n\n【整体印象】:\n作为审稿人，我的第一印象是这是一篇 **well-motivated, carefully positioned** 的系统性工作。proposal 展示了对领域的深入理解，文献综述极为全面（覆盖 20+ 篇高度相关工作），定位清晰。核心 insight（difficulty-dependent composition gap 使得联合优化 K 和 d 优于独立优化）在理论上合理且直觉上有吸引力。Simpson's Paradox 的类比恰当。\n\n然而，我会倾向于 **borderline accept / weak accept**，主要顾虑在于：\n1. **增量性风险**：核心贡献本质上是将两个已知维度（adaptive K + adaptive verifier type）组合起来，并用 difficulty 做路由。组合本身的创新度有限，价值取决于 composition gap 的实际大小。\n2. **DTR 信号在小模型上的不确定性**：DTR 仅在 ≥30B 模型上验证，而主要实验模型是 14B 和 8B，这是一个实质性风险。proposal 准备了 fallback 方案，但如果 DTR 不 work 且 fallback 信号也弱，整个系统的核心假设就会动摇。\n3. **实验 burden 极高**：8 baseline × 8 budget levels × 多个 benchmark × 多个 ablation，工作量巨大但每个对比的增量可能较小。\n\n【核心贡献】:\n核心贡献是 JOVA 框架——一个 difficulty-conditioned (K, d) 联合分配系统，在给定 compute budget 下通过路由到最优验证类型并同时调整候选数量来最大化准确率。具体包括：\n1. **理论层面**：揭示 difficulty-dependent composition gap 结构，即联合优化 (K,d) 相对于独立优化的增益在中等难度区间最大\n2. **系统层面**：基于 DTR 的轻量路由器 + UCB bandit refinement 的实际可部署方案\n3. **实验层面**：首次在 4-tier verifier hierarchy 下系统性地量化 (K,d) 联合优化的增量\n\n对领域的价值：中等偏上。如果 composition gap 确实显著（比如在中等难度问题上 ≥3-5% 准确率提升），这对 LLM serving 部署有实际意义。但如果 gap 很小（<2%），则贡献会被认为过于 incremental。\n\n【方法合理性】:\n方法整体合理，各组件有文献支撑：\n- DTR 作为 difficulty signal 有实证基础（r=0.828），但需要在目标模型规模上重新验证\n- UCB bandit refinement 是标准的在线优化方法，有理论保证\n- 4-tier verifier hierarchy 的设计合理，涵盖了从近零成本到高成本的完整光谱\n- Phase 0 pilot 设计（先验证假设再全面实验）是负责任的做法\n\n**更简单的替代方案问题**：Grid-Search-(K,d)-per-bucket 是一个强 trivial baseline。proposal 已经意识到这一点并将其纳入 baseline 6，同时论证了连续 difficulty、domain-specific factors 和 distribution shift 使得 learned routing 优于 static lookup。这个论证合理但需要实验验证——如果 Grid-Search 与 JOVA-full 差距很小（<1%），审稿人可能会质疑系统复杂性是否值得。\n\n【5 维度打分】:\n\n1. 研究问题: [强] — 在 test-time compute 这个 AAAI 高度关注的热点方向上，(K,d) 联合优化是一个自然但未被探索的问题。difficulty-dependent composition gap 的概念有理论吸引力，Simpson's Paradox 类比增强了 motivation。问题的实际部署价值（heterogeneous verifier routing）也有实际意义。\n\n2. 方法与创新: [中] — 方法合理但创新度有限。核心是将 adaptive K (Strategic Scaling Bandit, arXiv 2506.12721) 和 adaptive verifier type (Montgomery et al., arXiv 2510.14913; FlexiVe, arXiv 2505.11966) 两个已知维度组合，用 DTR (arXiv 2602.13517) 做路由信号。各组件都有先例，组合本身的技术贡献较为 incremental。与 AVA (OpenReview 2026) 的差异化（difficulty vs uncertainty, routing vs cascade）清晰但需要实验证明 difficulty-driven routing 的优越性。UCB bandit 是标准方法，不构成独立贡献。\n\n3. 实验设计: [强] — 这是 proposal 的最大亮点。8 个 compute-matched baseline（涵盖所有关键竞争工作），6 个 ablation configuration（系统性分离各组件贡献），8 个 log-spaced budget level，bootstrap 95% CI，多 seed 重复，per-difficulty-bin 分析，tier dropout 分析，router robustness 分析，composition gap 直接量化。Phase 0 pilot 验证核心假设的设计非常审慎。实验方案的完备性远超该方向的平均水平（对比 Montgomery et al. 仅使用 uniform per-dataset 策略，FlexiVe 仅有 binary hierarchy）。\n\n4. 可行性: [中] — 350-550 A100-hours 对学术实验室可行但不轻松。主要风险：(a) DTR 在 ≤14B 模型上可能不 work，虽有 fallback 但增加了不确定性；(b) 4-tier verifier hierarchy 需要部署和校准多个不同模型（LiLaVe XGBoost、InternLM2-7B-Reward、Skywork-PRM-7B、generator self-verification），工程复杂度高；(c) GenRM 成本 ~76× c_g 意味着高 budget 实验消耗巨大。但 proposal 的分阶段设计（Phase 0 先验证可行性）降低了沉没成本风险。\n\n5. 写作与呈现: [强] — proposal 写作极为清晰，逻辑严密。Problem formulation（C(K,d) = K·(c_g + c_v(d))）简洁有力。Simpson's Paradox 类比直觉化了核心 insight。文献定位精准（对每个 related work 明确指出了差异化维度）。诚实地承认了 DTR 的局限性。Phase 0 / Phase 1-3 的分阶段叙述增强了可执行感。verifier specification 表格和 ablation 表格增强了可读性。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n- **加分项**：(1) 研究问题 well-motivated，处于 AAAI 热点方向（test-time compute scaling）；(2) 实验设计极为完备，远超同方向多数工作；(3) 写作和定位清晰，文献综述全面；(4) 有实际部署价值（heterogeneous verifier serving）；(5) Phase 0 pilot 设计降低了风险。\n- **减分项**：(1) 方法创新度有限——本质是两个已知维度的组合 + 已知路由信号，审稿人可能认为 \"engineering contribution > scientific contribution\"；(2) composition gap 的实际大小未知——如果在中等难度区间仅有 1-2% 提升，贡献会被认为 trivial；(3) DTR 在目标模型规模上的有效性未验证，是系统核心假设的风险点；(4) 该方向竞争极为激烈（2025-2026 年有大量工作），差异化窗口正在关闭；(5) Grid-Search-per-bucket baseline 可能表现接近 JOVA-full，削弱 learned routing 的必要性。\n- **综合判断**：这是一篇 solid 的投稿，研究问题有价值、方法合理、实验设计出色。但在 AAAI 这样的顶会，方法创新度是核心评判维度，而本工作的组合性质可能让部分审稿人倾向 borderline reject。如果实验结果显示 composition gap 显著且 Grid-Search baseline 被明确击败，概率会上移到 38-42%；如果 gap 小或 DTR fallback 效果差，概率会下移到 28-32%。中位取 35%，反映\"整体扎实但缺少 breakthrough-level novelty\"的定位。\n\n【主要风险】:\n1. **Composition gap 过小**：如果联合优化 (K,d) 相比独立优化各维度的最佳值仅带来 <2% 的准确率提升，审稿人会认为系统复杂性不值得，方法贡献 incremental。这是最可能导致被拒的原因——\"interesting idea but marginal empirical gains\"。\n2. **DTR 信号在 ≤14B 模型上失效 + Grid-Search baseline 表现接近**：如果 DTR 在目标规模不 work，退化为 SC agreement 或 logit entropy 等弱信号，同时 Grid-Search-per-bucket 这个 trivial baseline 达到接近 JOVA-full 的效果，那么整个 learned routing 的必要性会被根本性质疑——\"a static lookup table suffices\"。\n\n【实施评估】:\n  - 计算资源: 350-550 A100-hours（中等规模，学术实验室可行但需要充足的 GPU 资源）\n  - 数据需求: 使用现有公开 benchmark（MATH-500, AIME25, GPQA-Diamond），无需构建新数据集\n  - 人工介入: 中等——需要部署和校准 4 种不同的 verifier（LiLaVe XGBoost 训练、InternLM2-7B-Reward 部署、Skywork-PRM 部署、GenRM prompt 设计），工程量不小\n  - 训练需求: 轻量——LiLaVe XGBoost 训练（分钟级）、UCB bandit 预训练（validation split 上，小时级）；不涉及大模型训练/微调\n  - 新 Benchmark: 不需要——完全基于现有 benchmark\n  - 预估周期: 约 8-12 周（Phase 0: 1-2 周, Phase 1: 2-3 周, Phase 2: 2-3 周, Phase 3: 2-3 周, 论文撰写: 2-3 周），但并行度有限（Phase 依赖前序结果），且 debug 和 unexpected failures 可能延长周期\n```\n\nSources:\n- [When To Solve, When To Verify (Singhi et al., COLM 2025)](https://arxiv.org/abs/2504.01005)\n- [Variation in Verification (ICLR 2026)](https://arxiv.org/abs/2509.17995)\n- [Strategic Scaling Bandit (Zuo et al.)](https://arxiv.org/abs/2506.12721)\n- [VG-Search (Chen et al.)](https://arxiv.org/abs/2505.11730)\n- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)\n- [Budget-aware Verification (Montgomery et al.)](https://arxiv.org/abs/2510.14913)\n- [Multi-Agent Verification (MAV)](https://arxiv.org/abs/2502.20379)\n- [LiLaVe](https://arxiv.org/abs/2504.16760)\n- [DTR / Think@n](https://arxiv.org/abs/2602.13517)\n- [AVA (Anytime Verified Agents)](https://openreview.net/forum?id=JMDCMf7mlF)\n- [CPO (Constrained Policy Optimization)](https://arxiv.org/abs/2604.14853)\n- [FlexiVe/SDV](https://arxiv.org/abs/2505.11966)\n- [Route to Reason (RTR)](https://arxiv.org/abs/2505.19435)\n- [Adaptive Test-Time Compute Allocation](https://www.emergentmind.com/topics/adaptive-test-time-compute-allocation)\n- [Putting the Value Back in RL](https://arxiv.org/abs/2505.04842)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile the final evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Singhi et al., \"When To Solve, When To Verify\", arXiv 2504.01005] (COLM 2025): 建立了 SC vs GenRM 的聚合 scaling law，结论为\"SC在大多数实际预算下优于GenRM\"。Proposal 正确指出这一结论是 difficulty-averaged 的，存在 Simpson's Paradox 式盲区。这是 JOVA 的核心出发点。\n- [Zhou et al., \"Variation in Verification\", arXiv 2509.17995] (ICLR 2026): 系统分析验证动态，确认 TPR 受 problem difficulty 主导、TNR 受 generator capability 主导。为 JOVA 的核心前提（不同验证器在不同难度上表现异质）提供了直接实证基础。\n- [Zuo et al., \"Strategic Scaling via Bandit\", arXiv 2506.12721] (2025): UCB 自适应 K 分配，MATH-500 提升 11.10%。但固定了 verifier 类型，未考虑 verification cost heterogeneity。JOVA 的直接上游工作。\n- [Chen et al., \"VG-Search\", arXiv 2505.11730] (2025): 引入连续 granularity 参数统一 beam search 和 BoN，52% FLOPs 降低。但不在 verifier 类型间选择。\n- [Montgomery et al., \"Budget-aware Verification\", arXiv 2510.14913] (2025): 证明 hybrid disc+gen 验证在 AIME25 上比纯 generative 提升 15.3%。但采用 uniform per-dataset 策略，不做 per-instance routing。JOVA 的关键对比工作。\n- [AVA, \"Anytime Verified Agents\", OpenReview 2026]: 多维度动态分配 (search/sampling/verification)，用 uncertainty 驱动 cascade + early exit。与 JOVA 的核心区别在于 signal (uncertainty vs difficulty) 和 mechanism (cascade vs type switching)。最接近的竞争者。\n- [DTR, arXiv 2602.13517] (2026): Deep-Thinking Ratio 作为难度信号，论文报告 r=0.683 平均正相关（注：proposal 中声称 r=0.828，与原文有出入）。仅在≥30B模型上验证。\n- [GenPRM, arXiv 2504.00891] (AAAI 2026): 7B GenPRM 超越 Qwen2.5-Math-PRM-72B，建立当前验证 SOTA。作为 JOVA 的高成本验证层。\n- [FlexiVe/SDV, arXiv 2505.11966] (2025): Fast/slow 二元验证 via GRPO，限于二元层级。\n- [CPO, arXiv 2604.14853] (2026): 约束策略优化做推理策略选择，12.8% 相对提升。方法论上与 JOVA 互补。\n- 调研总结: Test-time compute 的自适应分配是 2025-2026 的研究热点，但现有工作各自优化单一变量（K, granularity, binary type, reasoning length）。联合优化 (K, d) 跨多类验证器的工作确实是一个空白，proposal 准确识别了这个 gap。但该领域竞争激烈，AVA 和 Montgomery et al. 已经触及了多验证器组合的边缘。\n\n【整体印象】: \n这是一篇研究问题清晰、文献调研扎实、实验设计全面的 proposal。如果我是审稿人，第一反应是\"这个人对领域非常了解，问题定位准确\"。但随之而来的疑虑是：(1) 核心贡献——联合优化 (K, d) 相对于独立优化的增益（即 \"composition gap\"）——其实际幅度未知，如果只有 1-2% 的提升，论文的价值会大打折扣；(2) 系统涉及 DTR + UCB + 4层验证器层级，复杂度较高，reviewers 会追问\"Grid-Search per-bucket 是否已足够好\"。整体倾向 borderline accept，但取决于实验结果是否能证明 composition gap 的实质性存在。\n\n【核心贡献】: \nJOVA 的核心贡献是将 test-time compute 分配从 \"单变量优化\"（adaptive K 或 adaptive verifier type）提升到 \"联合优化\"（adaptive K × adaptive d），并通过 difficulty-conditioned routing 实现这一联合决策。附带贡献包括：(1) \"composition gap\" 概念的形式化及其难度依赖结构的理论预测；(2) Simpson's Paradox 视角重新解读 Singhi et al. 的结论。这个贡献方向正确且有实际价值（多验证器部署场景），但贡献的实际大小取决于实验中 composition gap 的幅度。如果 composition gap 在 medium-difficulty regime 显著（>3-5%），贡献扎实；如果小（<2%），则偏增量。\n\n【方法合理性】: \n方法整体合理，各组件都有文献支撑。但存在几个需要审视的点：\n1. **Grid-Search per-bucket 作为 trivial alternative**: Proposal 自己承认了这一点并列为 baseline 6，这很好。但如果 JOVA-full 对 Grid-Search 的提升不大，reviewers 会质疑 DTR+UCB 的必要性。\n2. **DTR 在小模型上的有效性**: DTR 仅在≥30B模型上验证（原文 r=0.683，非 proposal 声称的 r=0.828），而主要实验用 14B 和 8B 模型。Fallback signals (logit entropy, SC agreement) 的有效性是未验证的假设。Phase 0 设计了验证步骤，这很审慎。\n3. **验证器层级的假设**: 4层 cost-precision 单调递增是作为假设提出的（Phase 0 验证），这是合理的。但如果实际上 PRM 和 Disc-ORM 的差异不大，4层退化为2-3层，系统的价值会降低。\n4. **没有更简单的替代方案？** 一个更简单的方案是：用 SC agreement 作为 confidence proxy，high-confidence 直接用 majority voting，low-confidence 才用 GenRM（类似 FlexiVe 的思路但更灵活）。这比 JOVA 的 4层 DTR+UCB 简单得多。Proposal 需要在实验中清楚地展示完整系统相对于这种简化方案的优势。\n\n【5 维度打分】:\n  1. 研究问题: [强] — 问题定位精准，填补了明确的 gap（现有工作各优化单一变量，无联合 K×d 优化）。Simpson's Paradox 视角新颖且有解释力。实际部署场景（多验证器 serving）赋予实用价值。问题有足够的深度（composition gap 的难度依赖结构）而非单纯工程拼接。\n  \n  2. 方法与创新: [中] — 方法合理但创新程度中等。核心是将已有组件（DTR difficulty estimation, UCB bandit from Zuo et al., 多类型 verifier from Montgomery et al./MAV）在一个新的联合框架下组合。联合优化框架本身是自然的延伸而非根本性新方法。与 AVA（多维分配 + uncertainty cascade）的差异化需要更清晰的实验论证。Grid-Search per-bucket 作为 trivial alternative 的存在压缩了方法的创新空间。\n  \n  3. 实验设计: [强] — 这是 proposal 的突出亮点。8个 compute-matched baselines 覆盖了所有相关工作（Singhi, Zuo, Chen, SDV, Montgomery, GenPRM, Grid-Search, Static BoN），且包含了 compute-matched 的严谨要求（FLOPs primary, wall-clock supplementary）。6组 ablation 系统地隔离了每个组件的贡献。Phase 0 pilot 设计审慎（DTR 验证、层级验证、LiLaVe profiling）。8个 budget levels 的 Pareto curve、bootstrap CI、≥10 seeds for AIME25 均达到了领域最佳实践。Tier dropout 实验和 router robustness 分析显示了对潜在质疑的预见性。唯一小不足：缺少 domain transfer 的系统实验（仅 optional LiveCodeBench）。\n  \n  4. 可行性: [强] — 350-550 A100-hours 完全可行，所有组件（DTR, LiLaVe, 开源 ORM/PRM, GenRM self-verification）都有现成实现或简单复现路径。分4阶段推进，Phase 0 设有明确的 go/no-go 条件（r≥0.6）。DTR 在小模型上的不确定性通过 fallback signals 缓解。模型选择（DeepSeek-R1-Distill-14B, Qwen3-8B）实际且有代表性。\n  \n  5. 写作与呈现: [强] — 文献调研极其全面（25+ 篇相关工作，精确的差异化分析）。问题动机清晰（Simpson's Paradox framing），技术框架结构化（C(K,d) formulation, composition gap 预测）。主动暴露局限性（DTR 仅验证于大模型、层级非假设而是待验证假设）显示出学术诚实。唯一改进空间：核心创新的凝练表述可以更 punchy——当前较多篇幅在定位和文献对比上，核心 insight 的表达力可以加强。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】: \n这篇 proposal 在研究问题定位和实验设计方面表现出色，文献调研的深度和广度在同类 proposal 中属于上乘。35% 的中位估计基于以下推理：\n\n**正面因素 (推向上界):**\n- 问题 gap 真实存在且定位精准，Simpson's Paradox 视角有吸引力\n- 实验设计非常全面，baselines/ablations 的覆盖度在 proposal 阶段就已经超过很多最终提交的论文\n- 实际部署价值明确（多验证器 routing policy）\n- Phase 0 pilot 设计和 go/no-go 条件显示执行能力\n\n**负面因素 (推向下界):**\n- 核心创新偏向\"组合 + 联合优化\"而非根本性新方法，novelty bar 可能被部分 reviewers 质疑\n- Composition gap 的实际幅度未知——这是最大的不确定性。如果 gap 很小，paper 的核心 narrative 将难以成立\n- 领域竞争极其激烈（2025-2026 有大量 test-time compute scaling 工作），窗口期紧迫\n- DTR 在 ≤14B 模型上的有效性是核心前提但尚未验证（proposal 中引用的 r=0.828 与原文的 r=0.683 有出入，需要谨慎）\n\n整体属于 solid borderline 投稿：方向对、执行力可见、实验充分，但核心 novelty 的突破性有限，且核心 claim 的实证支撑存在不确定性。\n\n【主要风险】: \n1. **Composition gap 幅度不足**: 如果联合优化 (K,d) 相对于独立优化的增益很小（<2%），或者 Grid-Search per-bucket 这个 trivial baseline 已经 capture 了大部分增益，那么核心贡献将被视为 incremental，几乎必然被 reject。\n2. **DTR 在小模型上失效**: 主要实验模型为 14B 和 8B，但 DTR 仅在 ≥30B 模型上验证。如果 DTR 和所有 fallback signals 在目标模型上 correlation 都低于 r=0.6（Phase 0 门槛），整个 routing 机制的基础会瓦解，需要大幅重构方法。\n\n【实施评估】:\n  - 计算资源: ~350-550 A100-hours，中等规模，对有 GPU 集群的实验室完全可行\n  - 数据需求: MATH-500, AIME25, GPQA-Diamond 均为公开 benchmark，无数据获取障碍\n  - 人工介入: 低。系统自动化程度高，主要人工工作在 Phase 0 pilot 的分析决策和实验结果解读\n  - 训练需求: 极低。LiLaVe 需要训练 XGBoost（trivial），UCB bandit 需在验证集预训练（轻量）。核心方法不需要 fine-tuning 任何 LLM\n  - 新 Benchmark: 不需要。使用现有 benchmark\n  - 预估周期: ~8-12 周（Phase 0: 1-2周, Phase 1: 2-3周, Phase 2: 3-4周, Phase 3: 2-3周），与 AAAI 2027 Jul 28 截稿时间兼容\n```\n\nSources:\n- [When To Solve, When To Verify (Singhi et al., COLM 2025)](https://arxiv.org/abs/2504.01005)\n- [Variation in Verification (ICLR 2026)](https://arxiv.org/abs/2509.17995)\n- [Strategic Scaling via Bandit (Zuo et al.)](https://arxiv.org/abs/2506.12721)\n- [VG-Search (Chen et al.)](https://arxiv.org/abs/2505.11730)\n- [Budget-aware Verification (Montgomery et al.)](https://arxiv.org/abs/2510.14913)\n- [AVA: Anytime Verified Agents](https://openreview.net/forum?id=JMDCMf7mlF)\n- [DTR: Deep-Thinking Tokens](https://arxiv.org/abs/2602.13517)\n- [GenPRM](https://arxiv.org/abs/2504.00891)\n- [LiLaVe: Lightweight Latent Verifiers](https://arxiv.org/abs/2504.16760)\n- [FlexiVe/SDV](https://arxiv.org/abs/2505.11966)\n- [CPO: Constrained Policy Optimization](https://arxiv.org/abs/2604.14853)\n- [Multi-Agent Verification (MAV)](https://arxiv.org/abs/2502.20379)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Difficulty-Adaptive Joint Generation-Verification Compute Allocation for LLM Reasoning\n\n## Core Problem and Motivation\n\nDifferent verification methods exhibit heterogeneous reliability profiles across problem difficulty levels: lightweight verifiers may achieve adequate TNR on easy problems, while GenRM achieves substantially higher TPR on hard problems (Variation in Verification, ICLR 2026, arXiv 2509.17995). This heterogeneity means selecting a single verification type is structurally suboptimal regardless of compute budget.\n\nThe current aggregate consensus — \"self-consistency beats GenRM under most practical budgets\" (Singhi et al., COLM 2025, arXiv 2504.01005) — masks this difficulty-heterogeneous value structure, analogous to Simpson's Paradox: the aggregate trend (SC > GenRM) may reverse in difficulty strata where GenRM's higher TPR on hard problems dominates. JOVA reveals and exploits this blind spot by enabling per-instance verification type selection conditioned on difficulty.\n\nSimultaneously, under a shared inference budget, K (candidate count) and d (verification type) are coupled through C(K,d) = K·(c_g + c_v(d)), where c_v spans ~2% (latent-ORM) to ~76× (GenRM) of c_g. We ask: how should a system jointly select (K, d) per-instance to maximize accuracy, exploiting both the reliability mismatch and the cost structure?\n\n**Structural insight: K-d interaction is maximally non-decomposable in the medium-difficulty regime.** For easy problems, optimal (K, d) ≈ (high K, low d) — both K-only and d-only optimization independently converge here. For hard problems, optimal (K, d) ≈ (low K, high d) — again independently recoverable. But for medium-difficulty problems, the iso-compute Pareto tradeoff is sharpest: switching from PRM to GenRM requires reducing K from ~16 to ~3, and whether this trade improves accuracy depends on the verifier's difficulty-specific TPR/TNR. Under a simplified analytical model where verifier d at difficulty h has TPR(d,h) and TNR(d,h), and K candidates each have correctness probability p(h), the expected BoN accuracy is a function of K, d, and h. When p(h) is extreme (easy/hard), optimal (K,d) is insensitive to boundary perturbations; when p(h) is moderate, small TPR/TNR shifts cause discontinuous jumps in optimal (K,d). This composition gap — the accuracy loss from independently optimizing K and d vs. jointly — is predicted to peak in the medium-difficulty regime. The experiments will quantify this.\n\n**Practical relevance.** When serving infrastructure deploys multiple verifiers (latent-ORM near-free, disc-ORM moderate cost, GenRM expensive), JOVA provides a principled routing policy to maximize accuracy within a fixed serving budget — answering the deployment question \"given these verifiers, how do I use them optimally per query?\"\n\n## Research Landscape\n\n**Generation-verification tradeoff foundations.** Singhi et al. (COLM 2025, arXiv 2504.01005) established aggregate scaling laws showing SC beats GenRM under most practical budgets, but this is difficulty-averaged. Rethinking Reward Models (arXiv 2510.00492) characterizes verifier effectiveness across domains with uniform strategies. Trust but Verify (arXiv 2508.16665) provides a verification taxonomy (discriminative/generative, process/outcome, prompt-based/fine-tuned).\n\n**Adaptive K (fixed verifier).** Strategic Scaling bandit (Zuo et al., arXiv 2506.12721) achieves up to 11.10% improvement on MATH-500 via UCB-adaptive K, but assumes a fixed reward oracle and ignores verification cost. AdaBoN (arXiv 2505.12050) adapts K for alignment, not verification selection.\n\n**Adaptive verification (fixed K or type).** VG-Search (Chen et al., arXiv 2505.11730) introduces a continuous granularity parameter unifying beam search and BoN with 52% FLOPs reduction but does not select between verification types. FlexiVe/SDV (arXiv 2505.11966) introduces fast/slow binary verification gated by consensus via GRPO, limited to binary hierarchy. Budget-aware Verification (Montgomery et al., arXiv 2510.14913) demonstrates hybrid discriminative+generative verification surpasses pure generative by up to 15.3% on AIME25 under fixed compute, but applies uniform per-dataset strategy. GenPRM (arXiv 2504.00891, AAAI 2026) trains generative PRMs with CoT reasoning + code verification; 1.5B GenPRM surpasses GPT-4o in BoN selection, 7B surpasses Qwen2.5-Math-PRM-72B — establishing the current verification SOTA but using a single fixed verifier type. \"Putting the Value Back in RL\" (arXiv 2505.04842) jointly trains reasoner and verifier with dynamic compute via confidence thresholds — a unified-model alternative to JOVA's modular approach.\n\n**Heterogeneous verifier combination.** Multi-Agent Verification (MAV, arXiv 2502.20379) scales test-time compute by combining multiple heterogeneous Aspect Verifiers via voting (BoN-MAV). MAV **combines** all available verifiers simultaneously (ensemble); JOVA **routes** to a single optimal verifier per instance (selection). MAV does not consider per-instance difficulty conditioning or compute budget constraints — under budget constraints, running all verifiers is infeasible, making difficulty-conditioned routing the appropriate strategy.\n\n**Adaptive reasoning length (orthogonal axis).** DiffAdapt (ICLR 2026) adapts reasoning length per instance. CODA (arXiv 2603.08659) formalizes difficulty-aware allocation as utility maximization over reasoning length. CPO (arXiv 2604.14853) uses constrained optimization with Lagrangian dual for reasoning strategy selection (12.8% relative improvement). LATTS (arXiv 2509.20368) performs step-level adaptive scaling via verifier acceptance criteria.\n\n**Adaptive routing (model-level).** ODAR (arXiv 2602.23681) uses active-inference-based difficulty estimation to route between fast/slow agents (82% cost savings), routing between models rather than verification types.\n\n**Multi-dimensional budget allocation.** AVA (Anytime Verified Agents, OpenReview 2026) dynamically allocates compute across search, sampling, and verification using calibrated uncertainty and selective verification cascades with early exits. JOVA differs in three dimensions: (1) Signal — difficulty (intrinsic problem property via DTR) vs. uncertainty (model-problem interaction); (2) Space — discrete (K, d) menu with bilinear cost vs. continuous search/sampling/verification allocation; (3) Mechanism — cross-type switching (latent-ORM → GenRM with distinct TPR/TNR) vs. early exit within a single verification pipeline.\n\n**Difficulty signals and lightweight verifiers.** DTR (arXiv 2602.13517) provides a difficulty signal with r=0.828 average accuracy correlation (validated on GPT-OSS-120B, DeepSeek-R1-70B, Qwen3-30B-Thinking across AIME 24/25, HMMT 25, GPQA-diamond; not yet validated on distilled ≤14B models). LiLaVe (arXiv 2504.16760) enables near-free hidden-state-based verification. TrajSelector (arXiv 2510.16449) uses hidden states for process-level scoring via a 0.6B verifier, exceeding majority voting by 4.61%.\n\n**Gap.** All existing work optimizes a single variable (K, granularity, binary type, reasoning length, or model routing), or combines all verifiers without selection (MAV). AVA allocates multi-dimensionally but uses uncertainty-driven cascades, not difficulty-driven type switching. No work jointly optimizes (K, d) over a verifier type hierarchy under a shared budget with a continuous difficulty signal, nor reveals the difficulty-dependent composition gap structure.\n\n## Proposed Approach: JOVA\n\n**Formulation.** Per-instance allocation over a discrete (K, d) menu under C(K,d) = K·(c_g + c_v(d)) ≤ B.\n\n**Verifier type hierarchy.** We treat the four-tier ordering (latent-ORM < disc-ORM < PRM < GenRM in cost and expected precision) as an empirical hypothesis to be validated in Phase 0, not an assumption. If the actual reliability structure is non-monotonic (e.g., PRM outperforms GenRM on certain problem types), the (K, d) menu is reorganized accordingly.\n\n**Difficulty routing.** DTR-based router estimates difficulty from short prefix hidden states. Honest limitation: DTR primarily captures reasoning effort intensity; domain-specific factors (algebraic vs. geometric vs. combinatorial) and generator confidence may additionally influence optimal verification type. DTR provides a strong but not exhaustive routing signal; multi-signal routing is a natural future extension.\n\n**Fallback difficulty signals.** DTR has been validated only on ≥30B models. For ≤14B distilled models, we include fallbacks: (a) generator logit entropy (zero-overhead, extracted during generation), (b) two-stage SC agreement rate (fixed K_0=4 pilot samples to estimate difficulty, then allocate remaining budget B − K_0·c_g adaptively; cost model explicitly includes pilot overhead: C_total = K_0·c_g + K·(c_g + c_v(d))). Phase 0 selects the best signal for the target model scale.\n\n**Online refinement.** UCB bandit refines (K, d) via correctness feedback. Protocol: bandit pre-trained on held-out validation split, then frozen for test evaluation. For small benchmarks (AIME25), transfer policy learned on MATH-500 validation split.\n\n**Why learned routing exceeds static lookup.** Grid-Search-(K,d)-per-bucket (exhaustive search per difficulty tercile on validation data) is a strong trivial alternative. JOVA's advantages: (a) difficulty is continuous — discrete bins lose boundary information; (b) optimal (K, d) depends on domain-specific factors beyond scalar difficulty; (c) UCB adapts to distribution shift across benchmarks.\n\n## Experimental Design\n\n**Phase 0 (pilot, ~50 A100-hours).** (a) DTR correlation on DeepSeek-R1-Distill-14B and Qwen3-8B using MATH-500; compare DTR vs. SC agreement rate vs. logit entropy vs. prompt perplexity; proceed if best signal achieves r ≥ 0.6. (b) Validate verifier hierarchy: measure TPR/TNR of each verifier tier per difficulty bin; test whether ordering is monotonic. (c) Profile LiLaVe hidden state extraction overhead.\n\n**Benchmarks.** MATH-500 (primary per-difficulty analysis), AIME25 (aggregate + qualitative case study; ≥10 seeds due to n=30), GPQA-Diamond (aggregate). Optional: LiveCodeBench for cross-domain generalization.\n\n**Models.** Primary: DeepSeek-R1-Distill-Qwen-14B, Qwen3-8B. Extended: DeepSeek-R1-Distill-Qwen-32B. Supplementary: DeepSeek-R1 full (671B MoE) if resources permit.\n\n**Verifier specification:**\n\n| Tier | Implementation | Params | Approx. Cost |\n|---|---|---|---|\n| Latent-ORM | LiLaVe: XGBoost on hidden states (arXiv 2504.16760) | ~0 (reuses forward pass) | ~2% of c_g |\n| Disc-ORM | InternLM2-7B-Reward (or comparable open-source outcome RM) | 7B | ~50% of c_g |\n| PRM | Skywork-o1-Open-PRM-Qwen-2.5-7B, step-level scoring (note: robustness limitations per arXiv 2603.06621; Phase 0 validates on target generations) | 7B | ~60% of c_g |\n| GenRM | Generator self-verification via CoT | same as generator | ~76× of c_g |\n\nDisc-ORM and PRM intentionally use different model families to ensure the hierarchy captures genuine type diversity rather than scoring-granularity-within-one-model artifacts. FLOPs cost table calibrated per model-verifier pair; distinguishes prefill vs decode.\n\n**Baselines (compute-matched via FLOPs as primary metric; wall-clock as supplementary):**\n1. Static Best-of-N with each single verifier type (4 configs)\n2. Self-Consistency (majority voting)\n3. Strategic Scaling bandit (Zuo et al., arXiv 2506.12721) — adaptive K + fixed best verifier\n4. VG-Search (Chen et al., arXiv 2505.11730) — adaptive granularity, uniform type\n5. FlexiVe/SDV (arXiv 2505.11966) — fast/slow binary verification\n6. Grid-Search-(K,d)-per-bucket — static lookup per difficulty tercile\n7. Montgomery et al. hybrid disc+gen verification (arXiv 2510.14913) — uniform per-dataset\n8. GenPRM-7B BoN (arXiv 2504.00891, AAAI 2026) — fixed GenPRM verifier + best K\n\n**Ablations:**\n\n| Configuration | K | d | Router | Purpose |\n|---|---|---|---|---|\n| JOVA-full | adaptive | adaptive | DTR+UCB | Complete system |\n| Fix-d-best | adaptive | fixed best d | DTR+UCB | Isolate d-selection gain |\n| Fix-K-best | fixed best K | adaptive | DTR+UCB | Isolate K-selection gain |\n| DTR-only | DTR preset | DTR preset | DTR only | Isolate UCB refinement gain |\n| UCB-only | UCB learned | UCB learned | UCB only | Isolate DTR initialization gain |\n| Oracle-router | adaptive | adaptive | Oracle | Performance upper bound |\n\nAdditional analyses: (a) difficulty signal comparison (DTR vs SC-agreement vs logit entropy vs perplexity); (b) tier dropout: 2-tier (Latent-ORM + GenRM only) vs 3-tier (drop Disc-ORM or PRM) vs 4-tier (full) — quantifies marginal contribution of intermediate tiers; (c) binning sensitivity (2/3/5-bin vs continuous mapping); (d) router robustness (10%/20%/30% simulated routing error); (e) per-difficulty-bin (K,d) allocation distribution (MATH-500 only); (f) composition gap measurement: compare JOVA-full accuracy vs max(Fix-d-best, Fix-K-best), stratified by difficulty, to directly quantify the joint optimization benefit per regime.\n\n**Evaluation protocol:**\n- 8 budget levels at log-spacing: 1×, 2×, 4×, 8×, 16×, 32×, 64×, 128× of pass@1 cost\n- Accuracy-vs-FLOPs Pareto curves (primary) + accuracy-vs-wall-clock (supplementary, measured on single A100-80G, batch size 1)\n- Bootstrap 95% CI; ≥5 seeds (MATH-500, GPQA), ≥10 seeds (AIME25)\n- Gains reported in two tiers: (a) vs static BoN, (b) vs best adaptive-K-only baseline\n\n**Compute estimate (~350-550 A100-hours total):**\n- Phase 0 (pilot): ~50 hours\n- Phase 1 (core): MATH-500 + 14B + main ablations + Grid-Search baseline (~120 hours)\n- Phase 2 (extension): AIME25 + GPQA + Qwen3-8B + all baselines (~180 hours)\n- Phase 3 (analysis): difficulty breakdown, tier dropout, router robustness, Pareto curves, binning sensitivity, 32B model (~100 hours)\n\nPrimary target: AAAI 2027 (Jul 28).\n\n## Key References\n\n- When To Solve, When To Verify (Singhi et al., COLM 2025, arXiv 2504.01005)\n- Strategic Scaling of Test-Time Compute: A Bandit Approach (Zuo et al., arXiv 2506.12721)\n- VG-Search: Rethinking Optimal Verification Granularity (Chen et al., arXiv 2505.11730)\n- FlexiVe/SDV: Flexible Generative Verifier (arXiv 2505.11966)\n- Variation in Verification (ICLR 2026, arXiv 2509.17995)\n- Think Deep, Not Just Long: DTR via Deep-Thinking Tokens (arXiv 2602.13517)\n- Lightweight Latent Verifiers for Meta-Generation: LiLaVe (arXiv 2504.16760)\n- TrajSelector: Latent Representations for Best-of-N (arXiv 2510.16449)\n- Rethinking Reward Models for Multi-Domain Scaling (arXiv 2510.00492)\n- Budget-aware Test-time Scaling via Discriminative Verification (Montgomery et al., arXiv 2510.14913)\n- DiffAdapt: Difficulty-Adaptive Reasoning (ICLR 2026)\n- CODA: Difficulty-Aware Compute Allocation (arXiv 2603.08659)\n- ODAR: Principled Adaptive Routing via Active Inference (arXiv 2602.23681)\n- Adaptive TTC via Constrained Policy Optimization (arXiv 2604.14853)\n- LATTS: Locally Adaptive Test-Time Scaling (arXiv 2509.20368)\n- AdaBoN: Adaptive Best-of-N (arXiv 2505.12050)\n- AVA: Anytime Verified Agents (OpenReview 2026)\n- Putting the Value Back in RL: Unifying Reasoners With Verifiers (arXiv 2505.04842)\n- Trust but Verify! Survey on Verification Design (arXiv 2508.16665)\n- Multi-Agent Verification: BoN-MAV (arXiv 2502.20379)\n- GenPRM: Generative Process Reward Model (arXiv 2504.00891, AAAI 2026)\n- Reward Under Attack: PRM Robustness (arXiv 2603.06621)"
}
````

---

### Runtime record

_source line 2 · 2026-05-29T06:58:27.341Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:58:27.341Z",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-29T06:58:27.362Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- "Variation in Verification" (arXiv 2509.17995, ICLR 2026): 直接奠基论文。揭示了验证器在不同问题难度/生成器能力下的异构可靠性（TPR/TNR随难度变化），为JOVA的difficulty-conditioned routing提供了核心empirical motivation。JOVA可视为对该发现的operational化。
- Strategic Scaling Bandit (Zuo et al., arXiv 2506.12721): 最接近的adaptive-K工作。用UCB bandit自适应调整K，MATH-500上+11.1%。但固定verifier类型不变。JOVA在此基础上增加了d维度的联合优化，差异化清晰。
- Montgomery et al. Budget-aware Verification (arXiv 2510.14913): 最接近的hybrid verification工作。证明discriminative+generative hybrid在固定budget下surpass纯generative达15.3%（AIME25）。但采用per-dataset uniform策略，无per-instance difficulty conditioning。JOVA的per-instance routing是明确的增量贡献。
- AVA: Anytime Verified Agents (OpenReview 2026): 最接近的multi-dimensional allocation工作。动态分配compute across search/sampling/verification，用calibrated uncertainty + early exit cascades。与JOVA的关键差异：uncertainty-driven vs difficulty-driven，continuous allocation vs discrete (K,d) menu。两者在机制层面有实质差异，但reviewer可能质疑difficulty和uncertainty的相关性。
- GenPRM (arXiv 2504.00891, AAAI 2026): 当前verification SOTA，1.5B GenPRM超GPT-4o。但仍是单一fixed verifier，不做adaptive routing。JOVA将其作为verifier hierarchy最高层，定位合理。
- DiffAdapt (ICLR 2026): 难度自适应推理长度（非verification type选择），token reduction 62%。与JOVA正交但共享difficulty-adaptive思路，说明difficulty conditioning是当前热点。
- DTR (arXiv 2602.13517): JOVA依赖的difficulty signal。r=0.683 average accuracy correlation，但仅在≥30B模型上验证。≤14B模型上的有效性是JOVA的关键风险点。
- LiLaVe (arXiv 2504.16760): JOVA最底层verifier（Latent-ORM）。几乎零开销的hidden-state verification，与大型LLM verifier comparable。可行性已验证。
- MAV: Multi-Agent Verification (arXiv 2502.20379): ensemble所有verifiers vs JOVA的per-instance selection/routing。在budget-constrained场景下，routing比ensemble更合理。差异化论证充分。
- FlexiVe/SDV (arXiv 2505.11966): binary fast/slow verification via GRPO。JOVA推广至4-tier hierarchy，是明确的generalization。
- CPO (arXiv 2604.14853): constrained policy optimization for reasoning strategy selection，12.8% relative improvement under matched budget。方法论上与JOVA互补（CPO优化reasoning策略，JOVA优化verification策略）。

- 调研总结: Test-time compute的adaptive allocation是2025-2026年的核心热点，但现有工作均沿单一维度优化（K、verification granularity、binary type、reasoning length、model routing）。JOVA提出的(K,d)联合优化在文献中确实没有直接先例，gap identification成立。但该领域进展极快，竞争激烈，JOVA需要在empirical gains上给出convincing evidence才能脱颖而出。

【整体印象】: 
作为审稿人，第一反应是"这是一篇非常well-prepared的proposal"。文献覆盖广泛且精准（引用了~25篇高度相关工作并逐一区分），问题formulation清晰（(K,d)联合优化under shared budget），实验设计极其详尽（8个baselines、6个ablation、8个budget levels、多benchmark多模型）。Simpson's Paradox类比很巧妙，composition gap的分析框架有理论深度。

然而，核心concern是这本质上是一个routing/scheduling problem over existing components——没有提出新的verification方法，没有训练新模型，创新在于"如何组合已有工具"。一个tough reviewer可能将其定性为"systems/engineering contribution"而非"scientific contribution"。另一个关键风险是Grid-Search-(K,d)-per-bucket这个strong trivial baseline：如果简单的per-difficulty-bin lookup table就能capture大部分joint optimization gain，JOVA的learned routing的marginal value会很小。

总体倾向：borderline，偏向weak accept方向。如果empirical results显示composition gap显著（>3%）且JOVA大幅超越grid-search baseline，可以push到accept。

【核心贡献】: 
1. 识别并formalize了(K,d)联合优化问题——在shared compute budget下，generation数量与verification类型的耦合关系。这一formulation本身有价值。
2. 提出composition gap概念——independent optimization of K and d vs joint optimization的accuracy差距在medium-difficulty regime最大。这是一个可验证的structural prediction。
3. Difficulty-conditioned routing over a verifier hierarchy——从latent-ORM到GenRM的4-tier hierarchy，per-instance选择最优(K,d)组合。
4. 极其完备的实验方案——从Phase 0 pilot到完整ablation，包含了几乎所有可能被reviewer要求的分析。

贡献的核心价值：中等偏上。(K,d)联合优化的gap确实存在且被系统性忽视，但贡献本质是"更好的组合策略"而非"新方法"。如果composition gap empirically显著，价值会上升；如果marginal，价值有限。

【方法合理性】: 
方法在技术上是合理的。DTR→difficulty estimation→(K,d) routing是自然的pipeline。UCB bandit refinement有理论基础。4-tier verifier hierarchy的cost structure是realistic的（latent-ORM ~2% of c_g, GenRM ~76× of c_g）。

**更简单的替代方案风险**：Grid-Search-(K,d)-per-bucket（per difficulty tercile的static lookup）是一个非常强的trivial baseline。Proposal承认了这一点并给出了三个反驳论证（continuous difficulty, domain-specific factors, distribution shift），但这些论证偏理论化，需要empirical验证。如果grid-search baseline在MATH-500上只差1-2%，continuous routing的复杂性难以justify。

DTR dependency是另一个concern——DTR在≤14B模型上未验证，fallback signals（logit entropy, SC agreement）可能显著弱于DTR。如果fallback signal只有r~0.4-0.5，routing quality会大幅下降。不过proposal设计了Phase 0来explicitly验证这一点，并设定了r≥0.6的proceed threshold，这是负责任的设计。

方法本身没有致命缺陷，但其有效性高度依赖于：(1) difficulty signal的质量，(2) composition gap的实际大小，(3) grid-search baseline的competitiveness。

【5 维度打分】:
  1. 研究问题: [强] — (K,d)联合优化的gap在文献中确实系统性未被addressed。Variation in Verification (ICLR 2026)揭示了heterogeneous reliability，Montgomery et al.证明了hybrid verification的价值，Strategic Scaling bandit证明了adaptive K的价值，但没有work将这些dimension joint起来。问题重要性和timeliness都很好。唯一的minor concern是这个问题是否"足够大"——如果composition gap只有1-2%，研究问题的significance就打折扣。
  
  2. 方法与创新: [中] — 方法在技术上合理，(K,d) formulation清晰，UCB+DTR pipeline自然。但创新主要在formulation和组合层面，没有新的verification method、新的training paradigm或新的theoretical result。与Strategic Scaling bandit (Zuo et al.)相比，增量是加了d维度；与Montgomery et al.相比，增量是per-instance conditioning。每个增量都合理但不transformative。Grid-search baseline的潜在competitiveness进一步压缩了novelty空间。AVA (OpenReview 2026)在multi-dimensional allocation上也做了类似的工作，虽然机制不同，但narrative上有overlap。
  
  3. 实验设计: [强] — 这可能是proposal最突出的优势。8个compute-matched baselines（覆盖了所有主要competing approaches），6个ablation configurations（完整分离K/d/router各component的贡献），8个log-spaced budget levels，多benchmark（MATH-500/AIME25/GPQA），多model scale（8B/14B/32B，optional 671B），Phase 0 pilot验证核心假设，bootstrap CI + multi-seed。特别值得肯定的：(a) composition gap的direct measurement（JOVA-full vs max(Fix-d-best, Fix-K-best)），(b) tier dropout分析（验证4-tier vs 2/3-tier的marginal value），(c) router robustness分析（simulated routing error），(d) grid-search baseline的explicit inclusion。这套实验设计在AAAI投稿中属于top-tier水平。
  
  4. 可行性: [中] — 总compute ~350-550 A100-hours，对academic lab是可承受的。所有components（DTR, LiLaVe, open-source PRMs, GenRM via self-verification）都有现成实现或straightforward复现。主要风险：(a) DTR在≤14B模型上可能失效（mitigated by Phase 0 + fallback signals），(b) verifier hierarchy可能non-monotonic（mitigated by Phase 0验证 + 声明hierarchy是hypothesis not assumption），(c) AIME25只有30题，statistical power有限（mitigated by ≥10 seeds，但仍然marginal）。时间线合理（target AAAI 2027 = Jul 28 deadline），但如果Phase 0结果不理想需要pivot，时间会紧。
  
  5. 写作与呈现: [强] — Proposal结构清晰，逻辑链完整：motivation（heterogeneous reliability + cost coupling）→ structural insight（composition gap in medium difficulty）→ method（JOVA）→ experiments。文献review非常thorough且有differentiation。Simpson's Paradox类比增强了可读性。Honest limitation acknowledgment（DTR仅验证在≥30B，hierarchy是hypothesis不是assumption）增加了可信度。技术细节（cost model C(K,d) = K·(c_g + c_v(d))，FLOPs calibration，pilot overhead inclusion in cost model）体现了严谨性。

【概率估计】: [25% - 38%] 中位 32%

【估计理由】: 
这是一篇preparation质量远高于average AAAI submission的proposal——literature coverage、experimental design、problem framing都是professional级别的。研究问题genuine且timely，gap identification成立。实验设计的completeness本身是significant加分项。

然而，以下因素压制了概率上限：
(1) **Novelty concern**：核心贡献是routing/scheduling over existing components，没有new method或new model。一个tough reviewer（尤其是方法论导向的）可能给"limited novelty"。在AAAI这种large venue，novelty bar比workshop高但比ICML/NeurIPS稍低，这有一定buffer。
(2) **Empirical risk**：composition gap的实际大小未知。如果grid-search per-bucket baseline已经capture了80%+的joint optimization gain，JOVA的learned routing marginal value变小，paper的story会被削弱。
(3) **领域拥挤**：Test-time compute allocation是2025-2026最热门的方向之一，AVA、CPO、Strategic Scaling等多个concurrent work在抢占类似的narrative space。reviewer可能因为"yet another adaptive allocation paper"而打低分。
(4) **执行依赖**：DTR在target model scale上的有效性、verifier hierarchy的实际shape都是unknowns。Phase 0设计虽好，但如果结果不理想，pivot成本高。

综合来看，32%中位数反映了"solid preparation + clear gap + strong experiment design"vs "novelty concern + empirical uncertainty + crowded field"的balance。如果empirical results strong（composition gap >3%, JOVA大幅超越grid-search），可以push到40%+区间。

【主要风险】: 
1. **Composition gap可能很小**：如果independently optimizing K and d只比jointly优化差1-2%，整篇论文的核心contribution被undermined。Grid-search per-bucket baseline可能surprisingly competitive，让learned routing的marginal value不足以justify complexity。这是最可能导致reject的风险。
2. **Novelty perceived as incremental**：Reviewer可能认为"routing over existing verifiers conditioned on difficulty"是一个engineering contribution而非scientific contribution，尤其在concurrent work（AVA、CPO、Strategic Scaling）已经占据了adaptive allocation narrative的背景下。即使gap identification正确，"just putting existing pieces together"的perception可能导致borderline reject。

【实施评估】:
  - 计算资源: ~350-550 A100-hours，对有GPU集群access的academic lab可行。Phase 0 pilot (~50h)可快速验证核心假设，降低sunk cost风险。
  - 数据需求: 使用公开benchmark（MATH-500, AIME25, GPQA-Diamond），无custom数据集需求。所有verifier模型均为open-source（InternLM2-7B-Reward, Skywork-o1-Open-PRM等）。
  - 人工介入: 无human annotation需求。需要moderate engineering effort搭建multi-verifier pipeline、DTR extraction、UCB bandit training。
  - 训练需求: 极少。LiLaVe需训练XGBoost（trivial）。UCB bandit需在validation split上pre-train（lightweight）。无LLM fine-tuning。
  - 新 Benchmark: 不需要。使用现有established benchmarks。
  - 预估周期: Phase 0 (1-2周) + Phase 1 (2-3周) + Phase 2 (2-3周) + Phase 3 (1-2周) + 写作 (2-3周) ≈ 8-13周。对AAAI 2027 (Jul 28 deadline) timeline充裕。
```

Sources:
- [Variation in Verification (arXiv 2509.17995)](https://arxiv.org/abs/2509.17995)
- [Strategic Scaling of Test-Time Compute: A Bandit Learning Approach (arXiv 2506.12721)](https://arxiv.org/abs/2506.12721)
- [Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913)](https://arxiv.org/abs/2510.14913)
- [AVA: Anytime Verified Agents (OpenReview 2026)](https://openreview.net/forum?id=JMDCMf7mlF)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models (AAAI 2026)](https://github.com/RyanLiu112/GenPRM)
- [DiffAdapt: Difficulty-Adaptive Reasoning (ICLR 2026)](https://arxiv.org/pdf/2510.19669)
- [Think Deep, Not Just Long: DTR via Deep-Thinking Tokens (arXiv 2602.13517)](https://arxiv.org/abs/2602.13517)
- [LiLaVe: Lightweight Latent Verifiers (arXiv 2504.16760)](https://arxiv.org/abs/2504.16760)
- [Multi-Agent Verification: BoN-MAV (arXiv 2502.20379)](https://arxiv.org/pdf/2502.20379)
- [FlexiVe/SDV (arXiv 2505.11966)](https://arxiv.org/pdf/2505.11966)
- [Adaptive TTC via Constrained Policy Optimization (arXiv 2604.14853)](https://arxiv.org/abs/2604.14853)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough information to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [When To Solve, When To Verify (Singhi et al.)](https://arxiv.org/abs/2504.01005) (COLM 2025): 建立了 SC vs GenRM 的聚合 scaling law，发现在大多数实际 budget 下 SC 优于 GenRM。本 proposal 的核心出发点——认为这一聚合结论掩盖了 difficulty-heterogeneous 的结构——直接建立在此工作之上，是合理的理论推进。
- [Variation in Verification](https://arxiv.org/abs/2509.17995) (ICLR 2026): 实证展示了不同验证方法在不同难度下的异质可靠性（TPR/TNR 差异），为本 proposal 的 difficulty-conditioned routing 提供了直接经验支持。proposal 正确引用并基于此构建。
- [Strategic Scaling Bandit (Zuo et al.)](https://arxiv.org/abs/2506.12721): 用 UCB bandit 自适应调整 K，在 MATH-500 上获得 11.1% 提升，但假设固定 verifier。是本 proposal 的关键 baseline，JOVA 在其基础上增加了 d 维度。
- [VG-Search (Chen et al.)](https://arxiv.org/abs/2505.11730): 统一 beam search 和 BoN 的连续粒度参数，减少 52% FLOPs，但不在验证类型间选择。是重要 baseline。
- [GenPRM](https://arxiv.org/abs/2504.00891) (AAAI 2026): 当前验证 SOTA，1.5B GenPRM 超越 GPT-4o 的 BoN 选择。proposal 将其作为最高成本 tier 纳入，合理。
- [Budget-aware Verification (Montgomery et al.)](https://arxiv.org/abs/2510.14913): 混合 discriminative+generative 验证在 AIME25 上超过纯 generative 15.3%，但采用 uniform per-dataset 策略。是最接近的竞争工作之一，JOVA 的差异化在于 per-instance difficulty conditioning。
- [Multi-Agent Verification (MAV)](https://arxiv.org/abs/2502.20379): 通过投票组合多个异构 verifier。MAV 是 ensemble（全用），JOVA 是 routing（选一个）。在 budget 受限时 routing 比 ensemble 更合理。
- [LiLaVe](https://arxiv.org/abs/2504.16760): 基于隐状态的近零成本验证，XGBoost 浅层模型。proposal 将其作为最低成本 tier。
- [DTR / Think@n](https://arxiv.org/abs/2602.13517): 基于深度思考 token 比率的难度信号，r=0.828 准确度相关。proposal 以此为核心路由信号，但诚实承认仅在 ≥30B 模型上验证过。
- [AVA (Anytime Verified Agents)](https://openreview.net/forum?id=JMDCMf7mlF) (OpenReview 2026): 动态分配 compute 于 search/sampling/verification，基于 uncertainty 的 cascade。与 JOVA 并行但方法论不同（uncertainty vs difficulty, cascade vs routing）。
- [CPO](https://arxiv.org/abs/2604.14853): 使用约束策略优化的自适应推理策略选择，12.8% 相对提升。在 adaptive reasoning 方向上的竞争工作。
- [FlexiVe/SDV](https://arxiv.org/abs/2505.11966): 快/慢二元验证，通过 GRPO 门控。JOVA 扩展到 4-tier 层级。
- [Route to Reason (RTR)](https://arxiv.org/abs/2505.19435): 学习压缩表示以联合选择模型和推理策略。路由思路相近但在模型层面而非验证类型层面。

- 调研总结: 2025-2026 年 test-time compute 的自适应分配是极热门方向，但现有工作均在单一维度优化（K、粒度、二元类型、推理长度、模型路由）或无选择地组合所有 verifier。在 (K, d) 二维联合优化 + difficulty-conditioned routing 这一特定组合上，proposal 确实占据了一个未被填充的 niche，但该 niche 的实际增量价值需实验验证。

【整体印象】:
作为审稿人，我的第一印象是这是一篇 **well-motivated, carefully positioned** 的系统性工作。proposal 展示了对领域的深入理解，文献综述极为全面（覆盖 20+ 篇高度相关工作），定位清晰。核心 insight（difficulty-dependent composition gap 使得联合优化 K 和 d 优于独立优化）在理论上合理且直觉上有吸引力。Simpson's Paradox 的类比恰当。

然而，我会倾向于 **borderline accept / weak accept**，主要顾虑在于：
1. **增量性风险**：核心贡献本质上是将两个已知维度（adaptive K + adaptive verifier type）组合起来，并用 difficulty 做路由。组合本身的创新度有限，价值取决于 composition gap 的实际大小。
2. **DTR 信号在小模型上的不确定性**：DTR 仅在 ≥30B 模型上验证，而主要实验模型是 14B 和 8B，这是一个实质性风险。proposal 准备了 fallback 方案，但如果 DTR 不 work 且 fallback 信号也弱，整个系统的核心假设就会动摇。
3. **实验 burden 极高**：8 baseline × 8 budget levels × 多个 benchmark × 多个 ablation，工作量巨大但每个对比的增量可能较小。

【核心贡献】:
核心贡献是 JOVA 框架——一个 difficulty-conditioned (K, d) 联合分配系统，在给定 compute budget 下通过路由到最优验证类型并同时调整候选数量来最大化准确率。具体包括：
1. **理论层面**：揭示 difficulty-dependent composition gap 结构，即联合优化 (K,d) 相对于独立优化的增益在中等难度区间最大
2. **系统层面**：基于 DTR 的轻量路由器 + UCB bandit refinement 的实际可部署方案
3. **实验层面**：首次在 4-tier verifier hierarchy 下系统性地量化 (K,d) 联合优化的增量

对领域的价值：中等偏上。如果 composition gap 确实显著（比如在中等难度问题上 ≥3-5% 准确率提升），这对 LLM serving 部署有实际意义。但如果 gap 很小（<2%），则贡献会被认为过于 incremental。

【方法合理性】:
方法整体合理，各组件有文献支撑：
- DTR 作为 difficulty signal 有实证基础（r=0.828），但需要在目标模型规模上重新验证
- UCB bandit refinement 是标准的在线优化方法，有理论保证
- 4-tier verifier hierarchy 的设计合理，涵盖了从近零成本到高成本的完整光谱
- Phase 0 pilot 设计（先验证假设再全面实验）是负责任的做法

**更简单的替代方案问题**：Grid-Search-(K,d)-per-bucket 是一个强 trivial baseline。proposal 已经意识到这一点并将其纳入 baseline 6，同时论证了连续 difficulty、domain-specific factors 和 distribution shift 使得 learned routing 优于 static lookup。这个论证合理但需要实验验证——如果 Grid-Search 与 JOVA-full 差距很小（<1%），审稿人可能会质疑系统复杂性是否值得。

【5 维度打分】:

1. 研究问题: [强] — 在 test-time compute 这个 AAAI 高度关注的热点方向上，(K,d) 联合优化是一个自然但未被探索的问题。difficulty-dependent composition gap 的概念有理论吸引力，Simpson's Paradox 类比增强了 motivation。问题的实际部署价值（heterogeneous verifier routing）也有实际意义。

2. 方法与创新: [中] — 方法合理但创新度有限。核心是将 adaptive K (Strategic Scaling Bandit, arXiv 2506.12721) 和 adaptive verifier type (Montgomery et al., arXiv 2510.14913; FlexiVe, arXiv 2505.11966) 两个已知维度组合，用 DTR (arXiv 2602.13517) 做路由信号。各组件都有先例，组合本身的技术贡献较为 incremental。与 AVA (OpenReview 2026) 的差异化（difficulty vs uncertainty, routing vs cascade）清晰但需要实验证明 difficulty-driven routing 的优越性。UCB bandit 是标准方法，不构成独立贡献。

3. 实验设计: [强] — 这是 proposal 的最大亮点。8 个 compute-matched baseline（涵盖所有关键竞争工作），6 个 ablation configuration（系统性分离各组件贡献），8 个 log-spaced budget level，bootstrap 95% CI，多 seed 重复，per-difficulty-bin 分析，tier dropout 分析，router robustness 分析，composition gap 直接量化。Phase 0 pilot 验证核心假设的设计非常审慎。实验方案的完备性远超该方向的平均水平（对比 Montgomery et al. 仅使用 uniform per-dataset 策略，FlexiVe 仅有 binary hierarchy）。

4. 可行性: [中] — 350-550 A100-hours 对学术实验室可行但不轻松。主要风险：(a) DTR 在 ≤14B 模型上可能不 work，虽有 fallback 但增加了不确定性；(b) 4-tier verifier hierarchy 需要部署和校准多个不同模型（LiLaVe XGBoost、InternLM2-7B-Reward、Skywork-PRM-7B、generator self-verification），工程复杂度高；(c) GenRM 成本 ~76× c_g 意味着高 budget 实验消耗巨大。但 proposal 的分阶段设计（Phase 0 先验证可行性）降低了沉没成本风险。

5. 写作与呈现: [强] — proposal 写作极为清晰，逻辑严密。Problem formulation（C(K,d) = K·(c_g + c_v(d))）简洁有力。Simpson's Paradox 类比直觉化了核心 insight。文献定位精准（对每个 related work 明确指出了差异化维度）。诚实地承认了 DTR 的局限性。Phase 0 / Phase 1-3 的分阶段叙述增强了可执行感。verifier specification 表格和 ablation 表格增强了可读性。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
- **加分项**：(1) 研究问题 well-motivated，处于 AAAI 热点方向（test-time compute scaling）；(2) 实验设计极为完备，远超同方向多数工作；(3) 写作和定位清晰，文献综述全面；(4) 有实际部署价值（heterogeneous verifier serving）；(5) Phase 0 pilot 设计降低了风险。
- **减分项**：(1) 方法创新度有限——本质是两个已知维度的组合 + 已知路由信号，审稿人可能认为 "engineering contribution > scientific contribution"；(2) composition gap 的实际大小未知——如果在中等难度区间仅有 1-2% 提升，贡献会被认为 trivial；(3) DTR 在目标模型规模上的有效性未验证，是系统核心假设的风险点；(4) 该方向竞争极为激烈（2025-2026 年有大量工作），差异化窗口正在关闭；(5) Grid-Search-per-bucket baseline 可能表现接近 JOVA-full，削弱 learned routing 的必要性。
- **综合判断**：这是一篇 solid 的投稿，研究问题有价值、方法合理、实验设计出色。但在 AAAI 这样的顶会，方法创新度是核心评判维度，而本工作的组合性质可能让部分审稿人倾向 borderline reject。如果实验结果显示 composition gap 显著且 Grid-Search baseline 被明确击败，概率会上移到 38-42%；如果 gap 小或 DTR fallback 效果差，概率会下移到 28-32%。中位取 35%，反映"整体扎实但缺少 breakthrough-level novelty"的定位。

【主要风险】:
1. **Composition gap 过小**：如果联合优化 (K,d) 相比独立优化各维度的最佳值仅带来 <2% 的准确率提升，审稿人会认为系统复杂性不值得，方法贡献 incremental。这是最可能导致被拒的原因——"interesting idea but marginal empirical gains"。
2. **DTR 信号在 ≤14B 模型上失效 + Grid-Search baseline 表现接近**：如果 DTR 在目标规模不 work，退化为 SC agreement 或 logit entropy 等弱信号，同时 Grid-Search-per-bucket 这个 trivial baseline 达到接近 JOVA-full 的效果，那么整个 learned routing 的必要性会被根本性质疑——"a static lookup table suffices"。

【实施评估】:
  - 计算资源: 350-550 A100-hours（中等规模，学术实验室可行但需要充足的 GPU 资源）
  - 数据需求: 使用现有公开 benchmark（MATH-500, AIME25, GPQA-Diamond），无需构建新数据集
  - 人工介入: 中等——需要部署和校准 4 种不同的 verifier（LiLaVe XGBoost 训练、InternLM2-7B-Reward 部署、Skywork-PRM 部署、GenRM prompt 设计），工程量不小
  - 训练需求: 轻量——LiLaVe XGBoost 训练（分钟级）、UCB bandit 预训练（validation split 上，小时级）；不涉及大模型训练/微调
  - 新 Benchmark: 不需要——完全基于现有 benchmark
  - 预估周期: 约 8-12 周（Phase 0: 1-2 周, Phase 1: 2-3 周, Phase 2: 2-3 周, Phase 3: 2-3 周, 论文撰写: 2-3 周），但并行度有限（Phase 依赖前序结果），且 debug 和 unexpected failures 可能延长周期
```

Sources:
- [When To Solve, When To Verify (Singhi et al., COLM 2025)](https://arxiv.org/abs/2504.01005)
- [Variation in Verification (ICLR 2026)](https://arxiv.org/abs/2509.17995)
- [Strategic Scaling Bandit (Zuo et al.)](https://arxiv.org/abs/2506.12721)
- [VG-Search (Chen et al.)](https://arxiv.org/abs/2505.11730)
- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [Budget-aware Verification (Montgomery et al.)](https://arxiv.org/abs/2510.14913)
- [Multi-Agent Verification (MAV)](https://arxiv.org/abs/2502.20379)
- [LiLaVe](https://arxiv.org/abs/2504.16760)
- [DTR / Think@n](https://arxiv.org/abs/2602.13517)
- [AVA (Anytime Verified Agents)](https://openreview.net/forum?id=JMDCMf7mlF)
- [CPO (Constrained Policy Optimization)](https://arxiv.org/abs/2604.14853)
- [FlexiVe/SDV](https://arxiv.org/abs/2505.11966)
- [Route to Reason (RTR)](https://arxiv.org/abs/2505.19435)
- [Adaptive Test-Time Compute Allocation](https://www.emergentmind.com/topics/adaptive-test-time-compute-allocation)
- [Putting the Value Back in RL](https://arxiv.org/abs/2505.04842)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile the final evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Singhi et al., "When To Solve, When To Verify", arXiv 2504.01005] (COLM 2025): 建立了 SC vs GenRM 的聚合 scaling law，结论为"SC在大多数实际预算下优于GenRM"。Proposal 正确指出这一结论是 difficulty-averaged 的，存在 Simpson's Paradox 式盲区。这是 JOVA 的核心出发点。
- [Zhou et al., "Variation in Verification", arXiv 2509.17995] (ICLR 2026): 系统分析验证动态，确认 TPR 受 problem difficulty 主导、TNR 受 generator capability 主导。为 JOVA 的核心前提（不同验证器在不同难度上表现异质）提供了直接实证基础。
- [Zuo et al., "Strategic Scaling via Bandit", arXiv 2506.12721] (2025): UCB 自适应 K 分配，MATH-500 提升 11.10%。但固定了 verifier 类型，未考虑 verification cost heterogeneity。JOVA 的直接上游工作。
- [Chen et al., "VG-Search", arXiv 2505.11730] (2025): 引入连续 granularity 参数统一 beam search 和 BoN，52% FLOPs 降低。但不在 verifier 类型间选择。
- [Montgomery et al., "Budget-aware Verification", arXiv 2510.14913] (2025): 证明 hybrid disc+gen 验证在 AIME25 上比纯 generative 提升 15.3%。但采用 uniform per-dataset 策略，不做 per-instance routing。JOVA 的关键对比工作。
- [AVA, "Anytime Verified Agents", OpenReview 2026]: 多维度动态分配 (search/sampling/verification)，用 uncertainty 驱动 cascade + early exit。与 JOVA 的核心区别在于 signal (uncertainty vs difficulty) 和 mechanism (cascade vs type switching)。最接近的竞争者。
- [DTR, arXiv 2602.13517] (2026): Deep-Thinking Ratio 作为难度信号，论文报告 r=0.683 平均正相关（注：proposal 中声称 r=0.828，与原文有出入）。仅在≥30B模型上验证。
- [GenPRM, arXiv 2504.00891] (AAAI 2026): 7B GenPRM 超越 Qwen2.5-Math-PRM-72B，建立当前验证 SOTA。作为 JOVA 的高成本验证层。
- [FlexiVe/SDV, arXiv 2505.11966] (2025): Fast/slow 二元验证 via GRPO，限于二元层级。
- [CPO, arXiv 2604.14853] (2026): 约束策略优化做推理策略选择，12.8% 相对提升。方法论上与 JOVA 互补。
- 调研总结: Test-time compute 的自适应分配是 2025-2026 的研究热点，但现有工作各自优化单一变量（K, granularity, binary type, reasoning length）。联合优化 (K, d) 跨多类验证器的工作确实是一个空白，proposal 准确识别了这个 gap。但该领域竞争激烈，AVA 和 Montgomery et al. 已经触及了多验证器组合的边缘。

【整体印象】: 
这是一篇研究问题清晰、文献调研扎实、实验设计全面的 proposal。如果我是审稿人，第一反应是"这个人对领域非常了解，问题定位准确"。但随之而来的疑虑是：(1) 核心贡献——联合优化 (K, d) 相对于独立优化的增益（即 "composition gap"）——其实际幅度未知，如果只有 1-2% 的提升，论文的价值会大打折扣；(2) 系统涉及 DTR + UCB + 4层验证器层级，复杂度较高，reviewers 会追问"Grid-Search per-bucket 是否已足够好"。整体倾向 borderline accept，但取决于实验结果是否能证明 composition gap 的实质性存在。

【核心贡献】: 
JOVA 的核心贡献是将 test-time compute 分配从 "单变量优化"（adaptive K 或 adaptive verifier type）提升到 "联合优化"（adaptive K × adaptive d），并通过 difficulty-conditioned routing 实现这一联合决策。附带贡献包括：(1) "composition gap" 概念的形式化及其难度依赖结构的理论预测；(2) Simpson's Paradox 视角重新解读 Singhi et al. 的结论。这个贡献方向正确且有实际价值（多验证器部署场景），但贡献的实际大小取决于实验中 composition gap 的幅度。如果 composition gap 在 medium-difficulty regime 显著（>3-5%），贡献扎实；如果小（<2%），则偏增量。

【方法合理性】: 
方法整体合理，各组件都有文献支撑。但存在几个需要审视的点：
1. **Grid-Search per-bucket 作为 trivial alternative**: Proposal 自己承认了这一点并列为 baseline 6，这很好。但如果 JOVA-full 对 Grid-Search 的提升不大，reviewers 会质疑 DTR+UCB 的必要性。
2. **DTR 在小模型上的有效性**: DTR 仅在≥30B模型上验证（原文 r=0.683，非 proposal 声称的 r=0.828），而主要实验用 14B 和 8B 模型。Fallback signals (logit entropy, SC agreement) 的有效性是未验证的假设。Phase 0 设计了验证步骤，这很审慎。
3. **验证器层级的假设**: 4层 cost-precision 单调递增是作为假设提出的（Phase 0 验证），这是合理的。但如果实际上 PRM 和 Disc-ORM 的差异不大，4层退化为2-3层，系统的价值会降低。
4. **没有更简单的替代方案？** 一个更简单的方案是：用 SC agreement 作为 confidence proxy，high-confidence 直接用 majority voting，low-confidence 才用 GenRM（类似 FlexiVe 的思路但更灵活）。这比 JOVA 的 4层 DTR+UCB 简单得多。Proposal 需要在实验中清楚地展示完整系统相对于这种简化方案的优势。

【5 维度打分】:
  1. 研究问题: [强] — 问题定位精准，填补了明确的 gap（现有工作各优化单一变量，无联合 K×d 优化）。Simpson's Paradox 视角新颖且有解释力。实际部署场景（多验证器 serving）赋予实用价值。问题有足够的深度（composition gap 的难度依赖结构）而非单纯工程拼接。
  
  2. 方法与创新: [中] — 方法合理但创新程度中等。核心是将已有组件（DTR difficulty estimation, UCB bandit from Zuo et al., 多类型 verifier from Montgomery et al./MAV）在一个新的联合框架下组合。联合优化框架本身是自然的延伸而非根本性新方法。与 AVA（多维分配 + uncertainty cascade）的差异化需要更清晰的实验论证。Grid-Search per-bucket 作为 trivial alternative 的存在压缩了方法的创新空间。
  
  3. 实验设计: [强] — 这是 proposal 的突出亮点。8个 compute-matched baselines 覆盖了所有相关工作（Singhi, Zuo, Chen, SDV, Montgomery, GenPRM, Grid-Search, Static BoN），且包含了 compute-matched 的严谨要求（FLOPs primary, wall-clock supplementary）。6组 ablation 系统地隔离了每个组件的贡献。Phase 0 pilot 设计审慎（DTR 验证、层级验证、LiLaVe profiling）。8个 budget levels 的 Pareto curve、bootstrap CI、≥10 seeds for AIME25 均达到了领域最佳实践。Tier dropout 实验和 router robustness 分析显示了对潜在质疑的预见性。唯一小不足：缺少 domain transfer 的系统实验（仅 optional LiveCodeBench）。
  
  4. 可行性: [强] — 350-550 A100-hours 完全可行，所有组件（DTR, LiLaVe, 开源 ORM/PRM, GenRM self-verification）都有现成实现或简单复现路径。分4阶段推进，Phase 0 设有明确的 go/no-go 条件（r≥0.6）。DTR 在小模型上的不确定性通过 fallback signals 缓解。模型选择（DeepSeek-R1-Distill-14B, Qwen3-8B）实际且有代表性。
  
  5. 写作与呈现: [强] — 文献调研极其全面（25+ 篇相关工作，精确的差异化分析）。问题动机清晰（Simpson's Paradox framing），技术框架结构化（C(K,d) formulation, composition gap 预测）。主动暴露局限性（DTR 仅验证于大模型、层级非假设而是待验证假设）显示出学术诚实。唯一改进空间：核心创新的凝练表述可以更 punchy——当前较多篇幅在定位和文献对比上，核心 insight 的表达力可以加强。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】: 
这篇 proposal 在研究问题定位和实验设计方面表现出色，文献调研的深度和广度在同类 proposal 中属于上乘。35% 的中位估计基于以下推理：

**正面因素 (推向上界):**
- 问题 gap 真实存在且定位精准，Simpson's Paradox 视角有吸引力
- 实验设计非常全面，baselines/ablations 的覆盖度在 proposal 阶段就已经超过很多最终提交的论文
- 实际部署价值明确（多验证器 routing policy）
- Phase 0 pilot 设计和 go/no-go 条件显示执行能力

**负面因素 (推向下界):**
- 核心创新偏向"组合 + 联合优化"而非根本性新方法，novelty bar 可能被部分 reviewers 质疑
- Composition gap 的实际幅度未知——这是最大的不确定性。如果 gap 很小，paper 的核心 narrative 将难以成立
- 领域竞争极其激烈（2025-2026 有大量 test-time compute scaling 工作），窗口期紧迫
- DTR 在 ≤14B 模型上的有效性是核心前提但尚未验证（proposal 中引用的 r=0.828 与原文的 r=0.683 有出入，需要谨慎）

整体属于 solid borderline 投稿：方向对、执行力可见、实验充分，但核心 novelty 的突破性有限，且核心 claim 的实证支撑存在不确定性。

【主要风险】: 
1. **Composition gap 幅度不足**: 如果联合优化 (K,d) 相对于独立优化的增益很小（<2%），或者 Grid-Search per-bucket 这个 trivial baseline 已经 capture 了大部分增益，那么核心贡献将被视为 incremental，几乎必然被 reject。
2. **DTR 在小模型上失效**: 主要实验模型为 14B 和 8B，但 DTR 仅在 ≥30B 模型上验证。如果 DTR 和所有 fallback signals 在目标模型上 correlation 都低于 r=0.6（Phase 0 门槛），整个 routing 机制的基础会瓦解，需要大幅重构方法。

【实施评估】:
  - 计算资源: ~350-550 A100-hours，中等规模，对有 GPU 集群的实验室完全可行
  - 数据需求: MATH-500, AIME25, GPQA-Diamond 均为公开 benchmark，无数据获取障碍
  - 人工介入: 低。系统自动化程度高，主要人工工作在 Phase 0 pilot 的分析决策和实验结果解读
  - 训练需求: 极低。LiLaVe 需要训练 XGBoost（trivial），UCB bandit 需在验证集预训练（轻量）。核心方法不需要 fine-tuning 任何 LLM
  - 新 Benchmark: 不需要。使用现有 benchmark
  - 预估周期: ~8-12 周（Phase 0: 1-2周, Phase 1: 2-3周, Phase 2: 3-4周, Phase 3: 2-3周），与 AAAI 2027 Jul 28 截稿时间兼容
```

Sources:
- [When To Solve, When To Verify (Singhi et al., COLM 2025)](https://arxiv.org/abs/2504.01005)
- [Variation in Verification (ICLR 2026)](https://arxiv.org/abs/2509.17995)
- [Strategic Scaling via Bandit (Zuo et al.)](https://arxiv.org/abs/2506.12721)
- [VG-Search (Chen et al.)](https://arxiv.org/abs/2505.11730)
- [Budget-aware Verification (Montgomery et al.)](https://arxiv.org/abs/2510.14913)
- [AVA: Anytime Verified Agents](https://openreview.net/forum?id=JMDCMf7mlF)
- [DTR: Deep-Thinking Tokens](https://arxiv.org/abs/2602.13517)
- [GenPRM](https://arxiv.org/abs/2504.00891)
- [LiLaVe: Lightweight Latent Verifiers](https://arxiv.org/abs/2504.16760)
- [FlexiVe/SDV](https://arxiv.org/abs/2505.11966)
- [CPO: Constrained Policy Optimization](https://arxiv.org/abs/2604.14853)
- [Multi-Agent Verification (MAV)](https://arxiv.org/abs/2502.20379)


【原始 proposal（允许参考但不是主要依据）】:
# Difficulty-Adaptive Joint Generation-Verification Compute Allocation for LLM Reasoning

## Core Problem and Motivation

Different verification methods exhibit heterogeneous reliability profiles across problem difficulty levels: lightweight verifiers may achieve adequate TNR on easy problems, while GenRM achieves substantially higher TPR on hard problems (Variation in Verification, ICLR 2026, arXiv 2509.17995). This heterogeneity means selecting a single verification type is structurally suboptimal regardless of compute budget.

The current aggregate consensus — "self-consistency beats GenRM under most practical budgets" (Singhi et al., COLM 2025, arXiv 2504.01005) — masks this difficulty-heterogeneous value structure, analogous to Simpson's Paradox: the aggregate trend (SC > GenRM) may reverse in difficulty strata where GenRM's higher TPR on hard problems dominates. JOVA reveals and exploits this blind spot by enabling per-instance verification type selection conditioned on difficulty.

Simultaneously, under a shared inference budget, K (candidate count) and d (verification type) are coupled through C(K,d) = K·(c_g + c_v(d)), where c_v spans ~2% (latent-ORM) to ~76× (GenRM) of c_g. We ask: how should a system jointly select (K, d) per-instance to maximize accuracy, exploiting both the reliability mismatch and the cost structure?

**Structural insight: K-d interaction is maximally non-decomposable in the medium-difficulty regime.** For easy problems, optimal (K, d) ≈ (high K, low d) — both K-only and d-only optimization independently converge here. For hard problems, optimal (K, d) ≈ (low K, high d) — again independently recoverable. But for medium-difficulty problems, the iso-compute Pareto tradeoff is sharpest: switching from PRM to GenRM requires reducing K from ~16 to ~3, and whether this trade improves accuracy depends on the verifier's difficulty-specific TPR/TNR. Under a simplified analytical model where verifier d at difficulty h has TPR(d,h) and TNR(d,h), and K candidates each have correctness probability p(h), the expected BoN accuracy is a function of K, d, and h. When p(h) is extreme (easy/hard), optimal (K,d) is insensitive to boundary perturbations; when p(h) is moderate, small TPR/TNR shifts cause discontinuous jumps in optimal (K,d). This composition gap — the accuracy loss from independently optimizing K and d vs. jointly — is predicted to peak in the medium-difficulty regime. The experiments will quantify this.

**Practical relevance.** When serving infrastructure deploys multiple verifiers (latent-ORM near-free, disc-ORM moderate cost, GenRM expensive), JOVA provides a principled routing policy to maximize accuracy within a fixed serving budget — answering the deployment question "given these verifiers, how do I use them optimally per query?"

## Research Landscape

**Generation-verification tradeoff foundations.** Singhi et al. (COLM 2025, arXiv 2504.01005) established aggregate scaling laws showing SC beats GenRM under most practical budgets, but this is difficulty-averaged. Rethinking Reward Models (arXiv 2510.00492) characterizes verifier effectiveness across domains with uniform strategies. Trust but Verify (arXiv 2508.16665) provides a verification taxonomy (discriminative/generative, process/outcome, prompt-based/fine-tuned).

**Adaptive K (fixed verifier).** Strategic Scaling bandit (Zuo et al., arXiv 2506.12721) achieves up to 11.10% improvement on MATH-500 via UCB-adaptive K, but assumes a fixed reward oracle and ignores verification cost. AdaBoN (arXiv 2505.12050) adapts K for alignment, not verification selection.

**Adaptive verification (fixed K or type).** VG-Search (Chen et al., arXiv 2505.11730) introduces a continuous granularity parameter unifying beam search and BoN with 52% FLOPs reduction but does not select between verification types. FlexiVe/SDV (arXiv 2505.11966) introduces fast/slow binary verification gated by consensus via GRPO, limited to binary hierarchy. Budget-aware Verification (Montgomery et al., arXiv 2510.14913) demonstrates hybrid discriminative+generative verification surpasses pure generative by up to 15.3% on AIME25 under fixed compute, but applies uniform per-dataset strategy. GenPRM (arXiv 2504.00891, AAAI 2026) trains generative PRMs with CoT reasoning + code verification; 1.5B GenPRM surpasses GPT-4o in BoN selection, 7B surpasses Qwen2.5-Math-PRM-72B — establishing the current verification SOTA but using a single fixed verifier type. "Putting the Value Back in RL" (arXiv 2505.04842) jointly trains reasoner and verifier with dynamic compute via confidence thresholds — a unified-model alternative to JOVA's modular approach.

**Heterogeneous verifier combination.** Multi-Agent Verification (MAV, arXiv 2502.20379) scales test-time compute by combining multiple heterogeneous Aspect Verifiers via voting (BoN-MAV). MAV **combines** all available verifiers simultaneously (ensemble); JOVA **routes** to a single optimal verifier per instance (selection). MAV does not consider per-instance difficulty conditioning or compute budget constraints — under budget constraints, running all verifiers is infeasible, making difficulty-conditioned routing the appropriate strategy.

**Adaptive reasoning length (orthogonal axis).** DiffAdapt (ICLR 2026) adapts reasoning length per instance. CODA (arXiv 2603.08659) formalizes difficulty-aware allocation as utility maximization over reasoning length. CPO (arXiv 2604.14853) uses constrained optimization with Lagrangian dual for reasoning strategy selection (12.8% relative improvement). LATTS (arXiv 2509.20368) performs step-level adaptive scaling via verifier acceptance criteria.

**Adaptive routing (model-level).** ODAR (arXiv 2602.23681) uses active-inference-based difficulty estimation to route between fast/slow agents (82% cost savings), routing between models rather than verification types.

**Multi-dimensional budget allocation.** AVA (Anytime Verified Agents, OpenReview 2026) dynamically allocates compute across search, sampling, and verification using calibrated uncertainty and selective verification cascades with early exits. JOVA differs in three dimensions: (1) Signal — difficulty (intrinsic problem property via DTR) vs. uncertainty (model-problem interaction); (2) Space — discrete (K, d) menu with bilinear cost vs. continuous search/sampling/verification allocation; (3) Mechanism — cross-type switching (latent-ORM → GenRM with distinct TPR/TNR) vs. early exit within a single verification pipeline.

**Difficulty signals and lightweight verifiers.** DTR (arXiv 2602.13517) provides a difficulty signal with r=0.828 average accuracy correlation (validated on GPT-OSS-120B, DeepSeek-R1-70B, Qwen3-30B-Thinking across AIME 24/25, HMMT 25, GPQA-diamond; not yet validated on distilled ≤14B models). LiLaVe (arXiv 2504.16760) enables near-free hidden-state-based verification. TrajSelector (arXiv 2510.16449) uses hidden states for process-level scoring via a 0.6B verifier, exceeding majority voting by 4.61%.

**Gap.** All existing work optimizes a single variable (K, granularity, binary type, reasoning length, or model routing), or combines all verifiers without selection (MAV). AVA allocates multi-dimensionally but uses uncertainty-driven cascades, not difficulty-driven type switching. No work jointly optimizes (K, d) over a verifier type hierarchy under a shared budget with a continuous difficulty signal, nor reveals the difficulty-dependent composition gap structure.

## Proposed Approach: JOVA

**Formulation.** Per-instance allocation over a discrete (K, d) menu under C(K,d) = K·(c_g + c_v(d)) ≤ B.

**Verifier type hierarchy.** We treat the four-tier ordering (latent-ORM < disc-ORM < PRM < GenRM in cost and expected precision) as an empirical hypothesis to be validated in Phase 0, not an assumption. If the actual reliability structure is non-monotonic (e.g., PRM outperforms GenRM on certain problem types), the (K, d) menu is reorganized accordingly.

**Difficulty routing.** DTR-based router estimates difficulty from short prefix hidden states. Honest limitation: DTR primarily captures reasoning effort intensity; domain-specific factors (algebraic vs. geometric vs. combinatorial) and generator confidence may additionally influence optimal verification type. DTR provides a strong but not exhaustive routing signal; multi-signal routing is a natural future extension.

**Fallback difficulty signals.** DTR has been validated only on ≥30B models. For ≤14B distilled models, we include fallbacks: (a) generator logit entropy (zero-overhead, extracted during generation), (b) two-stage SC agreement rate (fixed K_0=4 pilot samples to estimate difficulty, then allocate remaining budget B − K_0·c_g adaptively; cost model explicitly includes pilot overhead: C_total = K_0·c_g + K·(c_g + c_v(d))). Phase 0 selects the best signal for the target model scale.

**Online refinement.** UCB bandit refines (K, d) via correctness feedback. Protocol: bandit pre-trained on held-out validation split, then frozen for test evaluation. For small benchmarks (AIME25), transfer policy learned on MATH-500 validation split.

**Why learned routing exceeds static lookup.** Grid-Search-(K,d)-per-bucket (exhaustive search per difficulty tercile on validation data) is a strong trivial alternative. JOVA's advantages: (a) difficulty is continuous — discrete bins lose boundary information; (b) optimal (K, d) depends on domain-specific factors beyond scalar difficulty; (c) UCB adapts to distribution shift across benchmarks.

## Experimental Design

**Phase 0 (pilot, ~50 A100-hours).** (a) DTR correlation on DeepSeek-R1-Distill-14B and Qwen3-8B using MATH-500; compare DTR vs. SC agreement rate vs. logit entropy vs. prompt perplexity; proceed if best signal achieves r ≥ 0.6. (b) Validate verifier hierarchy: measure TPR/TNR of each verifier tier per difficulty bin; test whether ordering is monotonic. (c) Profile LiLaVe hidden state extraction overhead.

**Benchmarks.** MATH-500 (primary per-difficulty analysis), AIME25 (aggregate + qualitative case study; ≥10 seeds due to n=30), GPQA-Diamond (aggregate). Optional: LiveCodeBench for cross-domain generalization.

**Models.** Primary: DeepSeek-R1-Distill-Qwen-14B, Qwen3-8B. Extended: DeepSeek-R1-Distill-Qwen-32B. Supplementary: DeepSeek-R1 full (671B MoE) if resources permit.

**Verifier specification:**

| Tier | Implementation | Params | Approx. Cost |
|---|---|---|---|
| Latent-ORM | LiLaVe: XGBoost on hidden states (arXiv 2504.16760) | ~0 (reuses forward pass) | ~2% of c_g |
| Disc-ORM | InternLM2-7B-Reward (or comparable open-source outcome RM) | 7B | ~50% of c_g |
| PRM | Skywork-o1-Open-PRM-Qwen-2.5-7B, step-level scoring (note: robustness limitations per arXiv 2603.06621; Phase 0 validates on target generations) | 7B | ~60% of c_g |
| GenRM | Generator self-verification via CoT | same as generator | ~76× of c_g |

Disc-ORM and PRM intentionally use different model families to ensure the hierarchy captures genuine type diversity rather than scoring-granularity-within-one-model artifacts. FLOPs cost table calibrated per model-verifier pair; distinguishes prefill vs decode.

**Baselines (compute-matched via FLOPs as primary metric; wall-clock as supplementary):**
1. Static Best-of-N with each single verifier type (4 configs)
2. Self-Consistency (majority voting)
3. Strategic Scaling bandit (Zuo et al., arXiv 2506.12721) — adaptive K + fixed best verifier
4. VG-Search (Chen et al., arXiv 2505.11730) — adaptive granularity, uniform type
5. FlexiVe/SDV (arXiv 2505.11966) — fast/slow binary verification
6. Grid-Search-(K,d)-per-bucket — static lookup per difficulty tercile
7. Montgomery et al. hybrid disc+gen verification (arXiv 2510.14913) — uniform per-dataset
8. GenPRM-7B BoN (arXiv 2504.00891, AAAI 2026) — fixed GenPRM verifier + best K

**Ablations:**

| Configuration | K | d | Router | Purpose |
|---|---|---|---|---|
| JOVA-full | adaptive | adaptive | DTR+UCB | Complete system |
| Fix-d-best | adaptive | fixed best d | DTR+UCB | Isolate d-selection gain |
| Fix-K-best | fixed best K | adaptive | DTR+UCB | Isolate K-selection gain |
| DTR-only | DTR preset | DTR preset | DTR only | Isolate UCB refinement gain |
| UCB-only | UCB learned | UCB learned | UCB only | Isolate DTR initialization gain |
| Oracle-router | adaptive | adaptive | Oracle | Performance upper bound |

Additional analyses: (a) difficulty signal comparison (DTR vs SC-agreement vs logit entropy vs perplexity); (b) tier dropout: 2-tier (Latent-ORM + GenRM only) vs 3-tier (drop Disc-ORM or PRM) vs 4-tier (full) — quantifies marginal contribution of intermediate tiers; (c) binning sensitivity (2/3/5-bin vs continuous mapping); (d) router robustness (10%/20%/30% simulated routing error); (e) per-difficulty-bin (K,d) allocation distribution (MATH-500 only); (f) composition gap measurement: compare JOVA-full accuracy vs max(Fix-d-best, Fix-K-best), stratified by difficulty, to directly quantify the joint optimization benefit per regime.

**Evaluation protocol:**
- 8 budget levels at log-spacing: 1×, 2×, 4×, 8×, 16×, 32×, 64×, 128× of pass@1 cost
- Accuracy-vs-FLOPs Pareto curves (primary) + accuracy-vs-wall-clock (supplementary, measured on single A100-80G, batch size 1)
- Bootstrap 95% CI; ≥5 seeds (MATH-500, GPQA), ≥10 seeds (AIME25)
- Gains reported in two tiers: (a) vs static BoN, (b) vs best adaptive-K-only baseline

**Compute estimate (~350-550 A100-hours total):**
- Phase 0 (pilot): ~50 hours
- Phase 1 (core): MATH-500 + 14B + main ablations + Grid-Search baseline (~120 hours)
- Phase 2 (extension): AIME25 + GPQA + Qwen3-8B + all baselines (~180 hours)
- Phase 3 (analysis): difficulty breakdown, tier dropout, router robustness, Pareto curves, binning sensitivity, 32B model (~100 hours)

Primary target: AAAI 2027 (Jul 28).

## Key References

- When To Solve, When To Verify (Singhi et al., COLM 2025, arXiv 2504.01005)
- Strategic Scaling of Test-Time Compute: A Bandit Approach (Zuo et al., arXiv 2506.12721)
- VG-Search: Rethinking Optimal Verification Granularity (Chen et al., arXiv 2505.11730)
- FlexiVe/SDV: Flexible Generative Verifier (arXiv 2505.11966)
- Variation in Verification (ICLR 2026, arXiv 2509.17995)
- Think Deep, Not Just Long: DTR via Deep-Thinking Tokens (arXiv 2602.13517)
- Lightweight Latent Verifiers for Meta-Generation: LiLaVe (arXiv 2504.16760)
- TrajSelector: Latent Representations for Best-of-N (arXiv 2510.16449)
- Rethinking Reward Models for Multi-Domain Scaling (arXiv 2510.00492)
- Budget-aware Test-time Scaling via Discriminative Verification (Montgomery et al., arXiv 2510.14913)
- DiffAdapt: Difficulty-Adaptive Reasoning (ICLR 2026)
- CODA: Difficulty-Aware Compute Allocation (arXiv 2603.08659)
- ODAR: Principled Adaptive Routing via Active Inference (arXiv 2602.23681)
- Adaptive TTC via Constrained Policy Optimization (arXiv 2604.14853)
- LATTS: Locally Adaptive Test-Time Scaling (arXiv 2509.20368)
- AdaBoN: Adaptive Best-of-N (arXiv 2505.12050)
- AVA: Anytime Verified Agents (OpenReview 2026)
- Putting the Value Back in RL: Unifying Reasoners With Verifiers (arXiv 2505.04842)
- Trust but Verify! Survey on Verification Design (arXiv 2508.16665)
- Multi-Agent Verification: BoN-MAV (arXiv 2502.20379)
- GenPRM: Generative Process Reward Model (arXiv 2504.00891, AAAI 2026)
- Reward Under Attack: PRM Robustness (arXiv 2603.06621)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5a2307d2-0494-4905-917a-d5842e1b7427",
  "type": "user",
  "uuid": "fd576024-157f-451b-94a4-a9eb90527610",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:58:27.359Z_

```json
{
  "parentUuid": "fd576024-157f-451b-94a4-a9eb90527610",
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
  "uuid": "e0b91f4b-286f-4a7a-ab2b-6722f3587f75",
  "timestamp": "2026-05-29T06:58:27.359Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:58:27.359Z_

```json
{
  "parentUuid": "e0b91f4b-286f-4a7a-ab2b-6722f3587f75",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "55b281e0-43f5-4fd2-8a58-62e209e33c2f",
  "timestamp": "2026-05-29T06:58:27.359Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make a thorough evaluatio…",
  "leafUuid": "55b281e0-43f5-4fd2-8a58-62e209e33c2f",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint generation-verification compute allocation for LLM reasoning",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:59:02.189Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Probability: [25% - 38%] 中位 32%
- Rubric scores: 研究问题[强], 方法与创新[中], 实验设计[强], 可行性[中], 写作与呈现[强]
- Main risks: Composition gap可能很小; Novelty perceived as incremental
  
**Reviewer 2:**
- Probability: [28% - 42%] 中位 35%
- Rubric scores: 研究问题[强], 方法与创新[中], 实验设计[强], 可行性[中], 写作与呈现[强]
- Main risks: Composition gap过小; DTR信号在≤14B模型上失效 + Grid-Search baseline表现接近

**Reviewer 3:**
- Probability: [28% - 42%] 中位 35%
- Rubric scores: 研究问题[强], 方法与创新[中], 实验设计[强], 可行性[强], 写作与呈现[强]

Reviewers 2 and 3 converge on a higher probability estimate around 35%, while Reviewer 1 is slightly more conservative at 32%. There's strong consensus on the research question and experimental design, but consistent concerns about the novelty being incremental and potential limitations with smaller model scales. Looking at where the reviewers diverge, feasibility is the main outlier—R3 rates it as strong while R1 and R2 mark it as moderate. R3 also uniquely flags a discrepancy in the DTR correlation coefficients that the others didn't explicitly call out. But across implementation details, all three are remarkably aligned. Given how tight the overall consistency is, I should weight the median assessment.

The three ranges cluster closely: R1 at 25-38%, R2 and R3 both at 28-42%. The midpoints are 32%, 35%, and 35% respectively, so the median sits at 35%. Following the guidance for high consistency, I'll narrow the interval around this center point rather than spreading across the full range. That puts me at approximately 27-40% with a median of 34%. I'm double-checking my bounds against the constraint that I shouldn't exceed the most lenient reviewer's range—42% upper bound is fine since my 39% stays within that. The median of 35% suggests I should land near there, but given the consistent concerns all three reviewers raised about novelty and empirical validation, plus R1's particularly thoughtful critique of the framing, I'm settling on [27% - 39%] with a midpoint of 34% to reflect that slightly more conservative position.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55b281e0-43f5-4fd2-8a58-62e209e33c2f",
  "isSidechain": false,
  "requestId": "req_011CbWRgT87MWn7yx7Gogv1n",
  "type": "assistant",
  "uuid": "1f1d09af-3415-4217-9204-ff62e8dc1824",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SG213uYrMuXdbHJHT9mZS1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19949,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3167,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 19949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19949
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

_source line 9 · 2026-05-29T06:59:45.767Z_

【阶段】: Meta Judge
【三次中位】: [32%, 35%, 35%]  std=1.4%
【共识维度】:
- 研究问题: [强] — 3/3 一致。(K,d)联合优化的gap真实存在，Simpson's Paradox视角有吸引力，问题timely且有部署价值。高信号。
- 方法与创新: [中] — 3/3 一致。核心是已有组件（DTR + UCB + 多类型verifier）的组合与联合框架，无新verification method或新training paradigm。组合性质限制了novelty天花板。高信号。
- 实验设计: [强] — 3/3 一致。8 baselines、6 ablations、8 budget levels、Phase 0 pilot、bootstrap CI、多seed。覆盖度在proposal阶段远超同类工作。高信号。
- 写作与呈现: [强] — 3/3 一致。文献调研极其全面（25+篇精准差异化），逻辑链完整，主动暴露局限性显示学术诚实。高信号。
- 主要风险 — Composition gap可能很小: 3/3 一致认为这是最大的单一风险。如果联合优化增益<2%，论文核心narrative崩塌。
- 主要风险 — DTR在≤14B模型上未验证: 3/3 一致。Phase 0 mitigates但不消除。
- 主要风险 — Grid-Search per-bucket baseline竞争力: 3/3 一致。trivial baseline可能capture大部分增益。
- 主要风险 — Novelty perceived as incremental/engineering: 3/3 一致。"just putting existing pieces together"的perception风险。
- 可行性: [中] — 2/3（R1、R2给[中]，R3给[强]）。共识偏[中]，主要因工程复杂度和DTR不确定性。

【异常维度】:
- R3单独指出DTR r值不一致（proposal声称r=0.828 vs 原文r=0.683）——这是一个有价值的细节发现，但不改变整体判决方向，因为即使取r=0.683，Phase 0仍可验证其在目标模型上的有效性。
- R3可行性给[强]而其他两位给[中]——轻微分歧，偏向多数意见[中]。
- R1额外提到AVA的"difficulty vs uncertainty相关性"质疑——仅R1提及，降权处理。

【最终概率】: [27% - 39%] 中位 34%
【一致性】: 高（std=1.4%，远低于3%阈值）
【综合理由】:
三份评审在所有5个rubric维度上高度一致（研究问题[强]、方法[中]、实验[强]、写作[强]，可行性2:1偏[中]），且对核心风险的识别完全重叠（composition gap幅度、DTR小模型有效性、Grid-Search竞争力、novelty增量性）。这种高度收敛提供了强信号：

**概率上限受限于方法创新度[中]**。三位审稿人一致认为核心贡献是组合性质的——将adaptive K（Zuo et al.）+ adaptive verifier type（Montgomery et al./FlexiVe）通过DTR路由联合起来——没有提出新的verification method或理论突破。在AAAI顶会，方法创新度是核心评判维度之一。即使实验完美执行，方法[中]将概率天花板限制在~40%。

**概率下限由实验设计[强]和研究问题[强]托底**。实验方案的完备性、Phase 0的审慎设计、以及问题本身的真实性和timeliness确保了即使composition gap偏小，论文仍有borderline accept的可能。

**中位取34%而非三位中位数的中位35%的理由**：(1) 三位审稿人虽然给出不同数字但对novelty concern的论述力度一致偏强，R1明确使用了"systems/engineering contribution"的framing，这在AAAI实际评审中是一个常见的reject理由；(2) 领域拥挤度——2025-2026年test-time compute方向的concurrent work密度极高（AVA、CPO、Strategic Scaling、Montgomery等），差异化窗口在收窄；(3) R3发现的DTR r值不一致（0.828 vs 0.683）虽是小问题，但如果被reviewer发现会损害credibility。综合以上，在高一致的基础上微偏保守1个百分点。

区间缩窄至[27%-39%]（vs三份评审的并集[25%-42%]），因为高一致性降低了尾部不确定性。

【建议】: 边缘（Borderline，可进入迭代优化流程，重点强化novelty framing和差异化论证）

【实施评估】:
- 计算资源: ~350-550 A100-hours（三份评审完全一致），Phase 0 ~50h可快速验证核心假设降低sunk cost。对有GPU集群的学术实验室可行但非trivial。
- 数据需求: MATH-500、AIME25、GPQA-Diamond，均为公开benchmark，无数据获取障碍。
- 人工介入: 低至中等。需部署和校准4种verifier（LiLaVe XGBoost训练、InternLM2-7B-Reward部署、Skywork-PRM部署、GenRM prompt设计），工程量中等但无human annotation需求。
- 训练需求: 极低。LiLaVe XGBoost（分钟级）、UCB bandit预训练（小时级）。不涉及LLM fine-tuning。
- 新 Benchmark: 不需要，完全使用现有established benchmarks。
- 预估周期: ~8-13周（Phase 0: 1-2周 → Phase 1: 2-3周 → Phase 2: 2-3周 → Phase 3: 1-3周 → 写作: 2-3周）。与AAAI 2027 Jul 28 deadline兼容，但Phase间有串行依赖，debug/pivot空间有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f1d09af-3415-4217-9204-ff62e8dc1824",
  "isSidechain": false,
  "requestId": "req_011CbWRgT87MWn7yx7Gogv1n",
  "type": "assistant",
  "uuid": "26c0fd3a-628f-494c-b44b-9de442d47322",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SG213uYrMuXdbHJHT9mZS1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19949,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3167,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 19949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19949
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make a thorough evaluatio…",
  "leafUuid": "26c0fd3a-628f-494c-b44b-9de442d47322",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Joint generation-verification compute allocation for LLM reasoning",
  "sessionId": "946f8a36-ca3e-4ca9-aae2-ae39a65089ff"
}
```

---
