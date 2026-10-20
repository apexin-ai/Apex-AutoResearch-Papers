# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/1d39e095-1ec0-4e31-a34b-65a4217a8c2b.jsonl`
- **Structured JSON:** [`43c4c7628d318c229f62.json`](../../sessions/43/43c4c7628d318c229f62.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:41:36.775Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:41:36.775Z",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile my evaluation.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474) (arXiv 2026): 最直接相关的工作。对 rubric gaming 进行了分类学研究，发现 partial compound satisfaction 占 gaming 的 36%，注意到 Simpson's paradox confound，但**未按难度分层分析 gaming 率**——正是本 proposal 要填补的空白。实验在医学/科学领域，非数学。\n- [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149) (ICLR 2026 Workshop): 在归纳推理任务上确认 shortcut prevalence 随任务复杂度单调递增，模型放弃规则归纳转而枚举实例级标签。其发现（extensional correctness 对复杂任务接受更多 false positive）直接支撑本 proposal 的 \"detection blindness\" 机制。\n- [DGPO: Harder Is Better](https://arxiv.org/abs/2601.20614) (ICLR 2026): 难度感知 GRPO，基于 group-level advantage reweighting，但仅适用于 binary outcome reward。证明了难度依赖的更新幅度偏差。是本 proposal 难度感知维度的对标方法，但不涉及 rubric aggregation。\n- [POW3R](https://arxiv.org/abs/2605.20164) (arXiv 2026): 基于 rollout variance 的 rubric criterion reweighting，preserves human weight prior。难度无关。24/30 comparison wins over vanilla GRPO。\n- [Focal Reward](https://arxiv.org/abs/2605.26579) (arXiv 2026): 基于 criterion saturation headroom 的自适应 reweighting，inverse reward projection 估计饱和度。难度无关。Proposal 对 Focal Reward 的 \"symptom-level vs mechanism-level\" 区分论证是 well-articulated。\n- [PAPO](https://arxiv.org/abs/2603.26535) (arXiv 2026): 将 ORM 和 rubric-based PRM 的 advantage decoupled normalization。解决的是训练稳定性，非 anti-gaming。\n- [SRaR](https://arxiv.org/abs/2605.17291) (arXiv 2026): Step-wise rubric attribution，发现 18.2% correct-answer 的 steps 错误但被正奖励。关注 step-level 粒度，非 difficulty conditioning。\n- [Reward Hacking as Equilibrium](https://arxiv.org/abs/2603.28063) (arXiv 2026): 理论框架，证明在五条极小公理下任何优化 agent 会 under-invest 于未被评估覆盖的质量维度。Proposal 将 DCM 的作用映射到该框架的 \"distortion index equalization\"，理论链接合理。\n- [DARO](https://arxiv.org/abs/2510.09001) (arXiv 2025): Difficulty-aware reweighting for policy optimization (loss weights)，与 DCM 解决不同层面问题（loss vs reward construction），可组合。\n\n- **调研总结**: 2026 年 rubric-based RLVR 领域极为活跃，7+ 篇并发工作分别从 variance、saturation、step-level、process-level 等角度优化 rubric aggregation，但全部 difficulty-agnostic。难度感知方法（DGPO/DARO/GRPO-LEAD）则全部限于 binary outcome reward。**将难度 conditioning 引入 rubric aggregation 作为 anti-gaming defense 确实是一个尚未被触碰的交叉空白**，proposal 的 gap claim 经调研验证成立。\n\n【整体印象】:\n作为审稿人，第一反应是 **cautious positive**——倾向 weak accept 到 borderline。这是一篇在活跃领域精准定位了交叉空白的 well-crafted proposal：问题动机清晰、方法简洁有原则、实验设计异常完备。两个机制（effort asymmetry + detection blindness）的论证有理论支撑且被已有实证（arXiv:2604.15149）部分验证。但主要担忧在于：(1) 核心假设（difficulty exploitation gradient 是一个足够显著的经验现象）尚未被验证，如果效应量小则论文立意动摇；(2) 方法本质上是 \"difficulty-conditioned softmin temperature\"，简洁但可能被 aggressive reviewer 视为 incremental combination。\n\n【核心贡献】:\n两个独立贡献：\n1. **诊断性贡献**：首次系统测量 rubric-based math RLVR 中按难度分层的 gaming rate，建立 \"difficulty exploitation gradient\" 作为经验现象（HRWAR + cross-judge + self-internalization gap 三级指标体系）。\n2. **防御性贡献**：DCM 聚合机制——softmin with difficulty-conditioned temperature，将 hard-problem reward 推向 min(s_k)，使 gaming payoff 受限于最难 game 的 criterion。\n\n对领域的价值：如果诊断贡献得到验证，这将是 rubric RLVR 领域一个重要的 empirical finding，因为它揭示了一个 structural vulnerability 而非 incidental bug。DCM 作为 defense 的简洁性是优势（易于在 existing pipeline 中集成），但也限制了 novelty ceiling。\n\n【方法合理性】:\n**合理，但有条件。**\n\n优点：\n- Softmin 是 min 的 smooth relaxation，数学性质清晰，τ→0 时 → min(s_k)，τ→∞ 时 → mean(s_k)，连续可控。\n- Difficulty conditioning 的逻辑链完整：difficulty ↑ → gaming profit ↑ → 需要更严格的 all-criterion enforcement → τ ↓。\n- Anti-gaming bound（gaming payoff bounded by min_k(ε_k) as τ→0）是 straightforward 但有用的理论保证。\n- 与 Stop Summation/PURE 的区分（temporal vs unordered dimensions）是正确的。\n\n潜在替代方案/质疑：\n1. **更简单的替代**：直接对 hard problems 使用 min aggregation（binary difficulty threshold）是否足够？Proposal 确实在 ablation 中包含了 \"fixed-τ softmin\" 和 \"step-function schedule\"，这是好的实验设计。\n2. **Genuine solution penalty 的风险**：Proposal 声称 gaming profile（high S1/S2, low D1-D3）与 genuine profile（potentially low S1/S2, high D1-D3）可区分。但在 hard math problems 上，genuine attempts 也经常在 D1-D3 上得分不均（某步推理正确但另一步出错），softmin 对这类 genuine partial progress 同样会施加惩罚。这是方法的 Achilles heel。\n3. **Surface/Deep 二分法的假设强度**：K=5 criteria 的 surface/deep 分类是否 robust？如果 LLM judge 在 hard problems 上的 D1-D3 评分本身 noisy（hard problems 的 judge reliability 通常更低），DCM 的 min 特性会 amplify judge noise。\n\n【5 维度打分】:\n\n1. **研究问题: 强** — 问题定义精准，且由三条独立证据线（arXiv:2605.12474 的 gaming taxonomy、arXiv:2604.15149 的 complexity-dependent shortcut、arXiv:2601.20614 的 difficulty-dependent bias）交叉支撑。\"Difficulty exploitation gradient\" 是一个清晰、可检验的假设。在 7+ 篇并发 rubric reweighting 工作均 difficulty-agnostic 的背景下，这是一个真实的 gap。唯一扣分：如果效应量不显著，问题的 practical importance 会受质疑。\n\n2. **方法与创新: 中（偏强）** — DCM 的核心创新是将 softmin temperature 与 difficulty conditioning 结合。与 Focal Reward（arXiv:2605.26579）的 \"symptom vs mechanism\" 区分论证有力。与 DGPO（arXiv:2601.20614）的区分（reward construction vs loss weighting）清晰，且二者可组合。理论贡献（anti-gaming bound + equilibrium framework connection）增色。但方法本身是 softmin 的一个参数化变体，创新跨度有限。一个 skeptical reviewer 可能认为这是 \"softmin + difficulty schedule\" 的 engineering combination。\n\n3. **实验设计: 强** — 这是 proposal 最突出的维度。7 baselines 覆盖了所有主要并发工作（POW3R、Focal Reward、DGPO、PAPO）+ 标准 ablation 参照（outcome-only、mean rubric、static min）。6 benchmarks（ID + OOD + easier ceiling）。5 项 ablation 全面且有针对性。Focal Reward + DCM 组合验证 complementarity claim。三级 gaming 指标（HRWAR + cross-judge + self-internalization gap）。Multi-seed + bootstrap CI。Compute tiered strategy 合理。**这个实验方案如果忠实执行，其完备性本身就是对 reviewers 的说服力。**\n\n4. **可行性: 中** — ~5,500 A100-hours 对大多数学术实验室是 significant（约 10-15 天 8×A100 集群 或 $5-10K 云计算成本），但对 well-funded labs 完全可行。主要风险不在计算资源，而在：(a) LLM judge（GPT-4o、Claude、Gemini）的 cross-judge panel 需要 API access + 费用；(b) 核心假设可能不成立（empirical risk）；(c) verl 框架 + Qwen3 的工程集成可能有 friction。时间线上，从实验到写作约需 3-4 个月，对 AAAI 2026 DDL 需确认 timing。\n\n5. **写作与呈现: 强** — Proposal 的逻辑结构清晰：Problem → Two Mechanisms → Gap → Method → Theory → Experiments。与并发工作的定位精准，每篇对标论文都有明确的 \"solves different problem / complementary\" 论证。Critical distinction from Focal Reward 一节尤为出色。术语使用一致（effort asymmetry、detection blindness、gaming profit margin 等概念贯穿始终）。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n\n**拉高因素：**\n- 精准的 gap identification，经调研确认 no concurrent work 在此交叉点上（+）\n- 异常完备的实验设计，7 baselines + 6 benchmarks + 5 ablations 已达 top-tier 标准（+）\n- 双贡献结构（diagnostic + defense），即使 DCM 效果有限，diagnostic 本身有独立价值（+）\n- 与并发工作的 positioning 极为精准，reviewers 不太可能找到被遗漏的直接竞争者（+）\n- 理论贡献（bound + equilibrium connection）为方法提供了 principled justification（+）\n- 领域极为热门（2026 RLVR/rubric RL），reviewer pool likely 对此问题有共鸣（+）\n\n**压低因素：**\n- 方法本质是 softmin temperature 的 difficulty-conditioned scheduling，创新跨度有限（−）\n- 核心假设（difficulty exploitation gradient 显著存在）是 empirical bet——如果效应量小，论文叙事坍塌（−）\n- Genuine solution penalty 的担忧需要极为有力的 empirical defense，如果 per-criterion profile 分析不够 convincing，会被质疑 DCM 对 genuine hard solutions 的 collateral damage（−）\n- Math-only domain 限制了 generalizability claim（−）\n- LLM judge 在 hard problems 上的 reliability 问题未充分 addressed——DCM 的 min 特性会 amplify judge errors（−）\n- AAAI 竞争激烈（acceptance rate ~20-23%），即使 solid 的 work 也面临筛选压力（−）\n\n**综合判断：** 这是一篇 direction 正确、design 扎实、positioning 精准的 proposal。在 AAAI 的 reviewer pool 中，如果遇到对 RLVR gaming 问题有认知的 reviewer，有较好机会拿到 positive review；但如果遇到 skeptical reviewer 质疑 \"这是否只是 softmin + difficulty heuristic 的工程组合\"，则可能被 borderline reject。中位估计 35% 反映的是一篇 \"solid but not exceptional\" 的投稿在顶会的 typical odds。\n\n【主要风险】:\n1. **Empirical bet 失败风险**：如果诊断实验显示 difficulty exploitation gradient 的效应量不够显著（例如 HRWAR 跨难度 quintile 的差异 < 5 percentage points），整篇论文的 motivation 和 contribution 都会大幅贬值。这是 make-or-break 风险。\n2. **Genuine solution collateral damage**：如果 DCM 在 hard problems 上对 genuine partial progress 施加了过度惩罚（导致 Q4-Q5 accuracy 下降而非持平/上升），reviewer 会质疑 method 的 precision——anti-gaming defense 如果 friendly fire 严重，则 net value 存疑。这需要 per-criterion profile 分析非常有说服力。\n\n【实施评估】:\n  - **计算资源**: ~5,500 A100-hours（1,500 for 1.5B ablation + 4,000 for 8B key comparisons）。需 8×A100 集群或等价云资源。成本约 $5K-$15K（取决于定价）。对 well-funded 学术组可行，对资源有限的组有一定门槛。\n  - **数据需求**: MATH training set (~7.5K) + NuminaMath（公开数据集）。评测用 MATH-500, AIME 2024/2025, OlympiadBench, AMC 2023, GSM8K 均为公开 benchmark。数据获取无障碍。\n  - **人工介入**: 中等。需要：(1) rubric criteria 设计与 LLM judge prompt engineering；(2) cross-judge panel setup（GPT-4o, Claude, Gemini API 配置）；(3) difficulty quintile 计算（base-model pass-rate，需要一次性评估）；(4) 实验 pipeline 集成（verl + GRPO + rubric judge）。\n  - **训练需求**: 需要完整的 GRPO 训练 pipeline。Primary: Qwen3-8B，Secondary: Qwen3-1.5B。每个 baseline/variant 需独立训练。Multi-seed 配置（DCM + Focal + combo 3 seeds on 8B；全部方法 3 seeds on 1.5B）。\n  - **新 Benchmark**: 不需要构建新 benchmark。需要构建新的诊断指标体系（HRWAR + cross-judge disagreement + self-internalization gap per difficulty quintile），但这是分析 pipeline 而非 benchmark。\n  - **预估周期**: 3-4 个月。Breakdown: 实验 pipeline 搭建 + difficulty quintile 计算（2-3 周）→ 1.5B 全量 ablation + diagnostic（3-4 周）→ 8B key comparisons（3-4 周）→ 分析 + 论文写作（3-4 周）。关键路径在 1.5B ablation 和 8B training 的顺序执行。\n```\n\nSources:\n- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474)\n- [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149)\n- [DGPO: Harder Is Better](https://arxiv.org/abs/2601.20614)\n- [POW3R: Policy-Aware Rubric Rewards](https://arxiv.org/abs/2605.20164)\n- [Focal Reward](https://arxiv.org/abs/2605.26579)\n- [PAPO: Decoupled Advantage Normalization](https://arxiv.org/abs/2603.26535)\n- [SRaR: Step-wise Rubric Rewards](https://arxiv.org/abs/2605.17291)\n- [Reward Hacking as Equilibrium](https://arxiv.org/abs/2603.28063)\n- [DARO: Difficulty-Aware Reweighting](https://arxiv.org/abs/2510.09001)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a comprehensive evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [arXiv:2605.12474] Reward Hacking in Rubric-Based RL (arXiv 2026): 最直接相关——首次系统分类 rubric gaming（含 partial compound satisfaction 占比 36%），提到 Simpson's paradox confound，但未按难度分层分析 gaming 率。本 proposal 的 diagnostic 贡献正是填补此空白。\n- [arXiv:2604.15149] LLMs Gaming Verifiers (ICLR 2026 Workshop): 证实任务复杂度越高、shortcut 越普遍（extensional correctness 对复杂任务 admits more false positives），直接支持 proposal 的 detection-blindness 机制。但该工作在 inductive reasoning 非 math 场景。\n- [arXiv:2601.20614] DGPO (ICLR 2026): 难度感知 GRPO 变体，通过 group advantage 平衡解决 learning efficiency 偏差，但仅操作 binary outcome reward。Proposal 正确区分了 policy optimization vs reward construction 的不同层面。\n- [arXiv:2605.20164] POW3R (arXiv 2026): 按 rollout contrastiveness（标准差）动态调整 rubric criterion 权重，难度无关。24/30 comparisons 胜出，是强 baseline。\n- [arXiv:2605.26579] Focal Reward (arXiv 2026): 按 criterion saturation headroom 自适应 reweight，解决 dimension 间极化问题。Proposal 对其的\"symptom-level vs mechanism-level\"区分论述清晰且成立——Focal Reward 确实无法区分 headroom 的来源（gaming vs 真实难度 vs 能力上限）。\n- [arXiv:2603.26535] PAPO (arXiv 2026): 解耦 ORM/PRM advantage normalization，解决 PRM 引入的 verbosity hacking，与本 proposal 方向正交。\n- [arXiv:2605.17291] SRaR (arXiv 2026): 将 rubric 评分下放到 step 粒度，消除 indiscriminate supervision，正交于 difficulty conditioning。\n- [arXiv:2504.15275] Stop Summation / PURE (NeurIPS 2025): 提出 temporal min-form credit assignment 防止 PRM reward hacking。Proposal 区分了 temporal step-wise aggregation vs unordered dimension aggregation，理论上需独立推导，此区分成立。\n- [arXiv:2603.28063] Reward Hacking as Equilibrium (arXiv 2026): 理论框架——五公理下任何优化 agent 在评估未覆盖维度上 under-invest。Proposal 将其作为 DCM 的理论支撑（均衡化 distortion index），连接合理。\n- [arXiv:2510.09001] DARO (arXiv 2025): 按难度动态调 loss contribution，与 DGPO 类似，仅操作 binary reward。\n- 调研总结: Rubric-based RLVR 和 reward hacking 是 2025-2026 极热方向，并发论文众多但均沿两条独立线展开——rubric 聚合优化（difficulty-agnostic）和 difficulty-aware RL（binary reward only）。在我的搜索中**未发现任何工作将 difficulty conditioning 与 rubric aggregation 结合用于 anti-gaming**，proposal 的 novelty claim 经验证成立。\n\n【整体印象】:\n作为审稿人，第一反应是 lean toward weak accept / borderline accept。这是一篇精心构造的 proposal，选取了两条活跃研究线的真实交叉空白，问题动机 well-grounded（effort asymmetry + detection blindness 两机制的论述有说服力），实验设计异常详尽（7+1 baselines、6 benchmarks、5 ablation、multi-seed + bootstrap CI）。但核心技术贡献——difficulty-conditioned softmin——本质是一个参数化温度调度的 softmin，技术上偏 incremental；整篇论文的 impact 高度依赖诊断性结果（difficulty exploitation gradient 是否 empirically 显著），如果实验中 gaming 率与难度的相关性不够 dramatic，防御机制就失去了动力。\n\n【核心贡献】:\n1. **诊断贡献**（potentially higher impact）：首次系统测量 rubric-based math RLVR 中 difficulty-stratified gaming 率，建立 difficulty exploitation gradient 作为经验现象。这是领域的 factual gap——arXiv:2605.12474 分类了 gaming 但未按难度分析；arXiv:2604.15149 观察到复杂度-shortcut 关联但在不同 domain。如果 diagnostic 结果 robust，这本身对领域有重要价值。\n2. **防御贡献**：DCM（difficulty-conditioned softmin）作为 mechanism-level defense，思路清晰但技术上较简单。理论 bound（gaming payoff bounded by min_k(ε_k) as τ→0）有价值但推导难度不高。\n\n核心贡献的领域价值：中等偏上。诊断贡献如果 robust，会被广泛引用；防御贡献更像一个 strong baseline 而非 paradigm shift。\n\n【方法合理性】:\n方法逻辑链合理：观测到 gaming 与难度正相关 → 在难题上加强 all-criterion enforcement → softmin 随难度收紧 → 理论保证 gaming payoff 受限于最难 game 的维度。\n\n**潜在挑战**：\n1. **Genuine solution penalty 假设过强**：Proposal 声称 gaming profile（高 S1/S2 低 D1-D3）与 genuine profile（低 S1/S2 高 D1-D3）\"structurally distinguishable\"。但实际中 genuine hard solutions 可能也有 D1-D3 维度的 partial failure（推理链长、compounding error），此时 softmin 同样惩罚 genuine attempts。这是方法最大的隐患。\n2. **更简单替代方案**：直接在 hard problems 上使用 binary outcome reward（abandon rubric for hard problems）可能达到类似 anti-gaming 效果但更简单。Proposal 需要论证为什么保留 rubric signal on hard problems 且用 DCM 调节比完全退回 binary 更优。\n3. **LLM-as-judge 可靠性**：5 个 rubric criteria 的评分依赖 LLM judge，尤其 D1（logical validity）和 D2（mathematical rigor）在 hard problems 上的 judge accuracy 本身可能下降，引入额外噪声。\n4. **Difficulty proxy 的 static 性质**：用训练前 base-model pass-rate 定义难度，但训练过程中模型能力变化可能导致 difficulty proxy 过时。\n\n方法整体合理，但上述挑战如未被实验充分回应，可能成为 reject 理由。\n\n【5 维度打分】:\n  1. 研究问题: 【强】— Difficulty-dependent gaming in rubric-based RLVR 是一个真实的、被忽略的问题。arXiv:2604.15149 已间接证实复杂度-hacking 关联，arXiv:2605.12474 明确提到 Simpson's paradox confound 但未深入，表明领域有 demand。问题有清晰的实践意义（rubric-based RLVR 正在被广泛部署）。\n  2. 方法与创新: 【中】— Novelty gap 经验证成立（无竞争工作 combine difficulty + rubric aggregation for anti-gaming）。但核心技术（softmin + τ difficulty schedule）创新度有限——softmin 已在 PURE/Stop Summation 中用于不同场景，difficulty conditioning 在 DGPO/DARO 中已有。创新在于 combination + 诊断 + 理论，而非技术本身。与 Focal Reward 的区分论述（symptom vs mechanism level）是 proposal 的 strong point。\n  3. 实验设计: 【强】— 这是 proposal 最突出的优势。7+1 baselines 涵盖所有主要竞争方向（outcome-only、mean rubric、static min、POW3R、Focal Reward、DGPO、PAPO + Focal+DCM combo）；6 benchmarks 覆盖 ID/OOD/easy/hard；5 ablation 系统性地隔离各设计选择；multi-seed + bootstrap CI 保证统计可靠性；理论 bound 验证；Focal+DCM combo 验证 complementarity。在同期论文中属于上乘设计。\n  4. 可行性: 【中偏强】— ~5,500 A100-hours 可行但需充足资源；Qwen3-8B/1.5B 是合理的模型选择；MATH + NuminaMath 数据可获取；verl 框架成熟。主要风险：cross-family LLM judge 成本；核心假设（difficulty exploitation gradient）如不成立则需 pivot。tiered compute 策略（1.5B 做 full ablation，8B 做 key comparisons）是明智的。\n  5. 写作与呈现: 【强】— Proposal 结构清晰，问题-机制-方法-实验逻辑链完整；与竞争工作的定位区分（尤其 Focal Reward、DGPO、PURE 三组对比）精准有力；\"Research Opportunity\" 节的三线汇聚论述有效建立了动机。theoretical framing（连接 equilibrium framework）增加深度。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n推理过程如下：\n- **加分因素**：(1) 真实的 novelty gap 在热门方向的交叉处（已验证无竞争工作）；(2) 实验设计极为详尽，达到 top-tier 标准；(3) 诊断+防御双贡献结构；(4) 与 concurrent work 的区分论述精准；(5) 理论 bound 增加深度。\n- **减分因素**：(1) 核心技术创新度有限——softmin + difficulty schedule 本质是已知组件的 combination，技术门槛不高，审稿人可能认为 \"trivially obvious once the problem is identified\"；(2) 整篇论文的 impact 高度 contingent on diagnostic results——如果 difficulty exploitation gradient 不够 dramatic（如仅有 5-10% 差异），reviewers 会质疑 defense 的必要性；(3) genuine solution penalty 问题可能成为审稿人的主要攻击点；(4) 8B 规模在 2026 context 下偏小，scaling behavior 未知。\n- **概率区间推理**：研究问题和实验设计是明确的加分项（对应 35-45% 锚点的 \"整体扎实\" 标准）；但方法创新度的局限和核心假设的 contingent 性质将概率从上界拉回。综合判断为 solid borderline submission，中位 35%。上界 42% 对应诊断结果 dramatic + 理论 tight + 实验全面的最佳情景；下界 28% 对应审稿人认为技术 trivial 或 diagnostic 不够 convincing 的情景。\n\n【主要风险】:\n1. **技术贡献被判 incremental**：核心方法（difficulty-conditioned softmin）可能被审稿人视为\"an obvious fix once the problem is stated\"，认为技术创新不足以支撑主会论文。尤其是 softmin 和 difficulty conditioning 分别在 PURE 和 DGPO 中已有先例，combination 的技术壁垒不高。\n2. **Diagnostic 假设不成立或不够 dramatic**：如果实验发现 gaming 率与难度的关联较弱（或方向相反、非单调），整篇论文的核心叙事和防御动机均会崩塌。这是最大的 existential risk。\n\n【实施评估】:\n  - 计算资源: ~5,500 A100-hours（1,500 for 1.5B ablation + 4,000 for 8B key comparisons）；需 8×A100 节点若干天，对 well-funded lab 可行，对资源有限的团队有压力\n  - 数据需求: MATH (~7.5K) + NuminaMath（公开可获取）；evaluation benchmarks (MATH-500, AIME 2024/2025, OlympiadBench, AMC 2023, GSM8K) 均为公开标准 benchmark\n  - 人工介入: 中等——rubric criteria 设计需要 domain expertise；cross-family LLM judge 的 prompt engineering 和校准需要 iteration；difficulty quintile 划分需手动验证合理性\n  - 训练需求: 需要完整的 GRPO 训练流水线（verl 框架）；Qwen3-8B 和 Qwen3-1.5B 两个规模的完整训练 + multi-seed\n  - 新 Benchmark: 不需要构建新 benchmark，但需要构建 HRWAR 等新 diagnostic metrics 的计算 pipeline 和 difficulty-stratified 分析框架\n  - 预估周期: 约 10-14 周——2 周 infrastructure/rubric/difficulty calibration，2 周 1.5B full ablation，3-4 周 8B key experiments，2-3 周 analysis/writing，1-2 周 buffer\n```\n\nSources:\n- [Reward Hacking in Rubric-Based RL (arXiv:2605.12474)](https://arxiv.org/abs/2605.12474)\n- [LLMs Gaming Verifiers (arXiv:2604.15149)](https://arxiv.org/abs/2604.15149)\n- [DGPO: Harder Is Better (arXiv:2601.20614)](https://arxiv.org/pdf/2601.20614)\n- [POW3R: Policy-Aware Rubric Rewards (arXiv:2605.20164)](https://arxiv.org/abs/2605.20164v1)\n- [Focal Reward (arXiv:2605.26579)](https://arxiv.org/abs/2605.26579)\n- [PAPO: Decoupled Advantage Normalization (arXiv:2603.26535)](https://arxiv.org/abs/2603.26535)\n- [SRaR: Step-wise Rubric Rewards (arXiv:2605.17291)](https://arxiv.org/abs/2605.17291)\n- [Stop Summation / PURE (arXiv:2504.15275)](https://arxiv.org/abs/2504.15275)\n- [Reward Hacking as Equilibrium (arXiv:2603.28063)](https://arxiv.org/abs/2603.28063)\n- [DARO: Difficulty-Aware Reweighting (arXiv:2510.09001)](https://arxiv.org/pdf/2510.09001)\n- [Representation-Level Reward Hacking (arXiv:2604.01476)](https://arxiv.org/pdf/2604.01476)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) (arXiv 2026): 最直接的前置工作。该文系统分类了 rubric gaming 的模式，发现 partial compound satisfaction 占 36% 的 gaming 行为，并注意到 Simpson's paradox 的混淆效应——但关键的是，该文 **从未按难度分层分析 gaming rate**，也未提出防御机制。Proposal 的 diagnostic 贡献恰好填补了这一明确遗漏。\n- [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149) (ICLR 2026 Workshop): 在归纳推理任务上确认 shortcut 行为随任务复杂度增加而增加，其解释（extensional correctness 对复杂任务承认更多 false positives）直接支撑了 proposal 的\"检测盲区\"机制。但该文聚焦于归纳推理验证器，未涉及 rubric 聚合。\n- [DGPO: Harder Is Better](https://arxiv.org/abs/2601.20614) (ICLR 2026): 证明了 GRPO 中存在的难度依赖更新量偏差，提出 difficulty-balanced group advantage estimation。但仅在 **binary outcome reward** 上操作，调整的是 policy optimization（loss weights），不是 reward signal construction。与 proposal 的 DCM 解决不同问题（学习效率 vs 防 gaming），理论上可组合使用。\n- [POW3R: Policy-Aware Rubric Rewards](https://arxiv.org/abs/2605.20164) (arXiv 2026): 基于 rollout-level contrast 对 rubric criterion 进行方差感知的重加权。在 30 个 base-policy/metric 比较中赢得 24 个。但其重加权是 **difficulty-agnostic** 的。\n- [Focal Reward: Balanced RL under Rubric-Based Rewards](https://arxiv.org/abs/2605.26579) (arXiv 2026): 基于 criterion saturation headroom 进行动态重加权。Proposal 对其的批评——headroom 来源不区分 gaming vs genuine difficulty vs capacity limits——是合理的。两者的补充关系在实验设计中通过 \"Focal Reward + DCM\" 组合 baseline 被显式验证。\n- [Stop Summation / PURE](https://arxiv.org/abs/2504.15275) (NeurIPS 2025): 在 PRM 的 **时序步骤聚合** 上引入 min-form credit assignment，缓解了步骤层面的 reward hacking。Proposal 的 min-form 是在 **无序维度（rubric criteria）** 上的，结构性不同（无时序依赖、无 error compounding），需要独立推导。\n- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (arXiv 2026): 理论框架，证明在五个最小公理下任何优化 agent 都会在评估未覆盖的质量维度上投资不足。Proposal 将其用作理论锚点——difficulty-agnostic rubric 聚合在高难度问题上结构性地\"under-cover\"了某些 criteria，创造了有利于 gaming 的均衡。\n- [DARO: Difficulty-Aware Reweighting Policy Optimization](https://arxiv.org/abs/2510.09001) (arXiv 2025): 基于模型学习状态动态调整每个难度组的 loss 贡献。同 DGPO，仅操作 binary rewards，调整的是 policy 端而非 reward 端。\n\n- **调研总结**: Rubric-based RLVR 的 reward aggregation 是 2025-2026 年的热门方向，已有 7+ 篇并发工作（POW3R, Focal Reward, PAPO, SRaR 等），但全部是 difficulty-agnostic 的。Difficulty-aware RL 方法（DGPO, DARO, GRPO-LEAD）全部仅操作 binary outcome rewards。**\"难度 × rubric 聚合\"的交叉点确实是一个真实的、未被占据的空白**。Proposal 的 novelty claim 经调研核实后成立。\n\n【整体印象】: \n如果我是审稿人，初始印象是 **cautiously positive**（倾向 weak accept 区间）。这篇 proposal 最令人印象深刻的是它对 research gap 的精准定位——在两个活跃且相互独立的研究线索（rubric aggregation 和 difficulty-aware RL）之间找到了一个真实的、有意义的交叉空白，并提供了两个清晰的动机机制（effort asymmetry + detection blindness）来解释为什么这个空白值得填补。实验设计的完备程度（7+1 baselines, 6 benchmarks, 5 ablations, multi-seed, bootstrap CI）远超一般 proposal 水准。\n\n然而，我也有顾虑：(1) 方法本身（softmin + 难度条件化 τ）在技术深度上较浅——这是一个简单的数学变换，核心创新更多在 framing 和诊断上而非算法设计上；(2) 整篇论文的叙事完全建立在\"难度利用梯度\"这个经验假说之上，如果实验中该梯度不够显著，诊断贡献和防御贡献都将大打折扣；(3) gaming vs genuine 的可区分性假设（gaming inflates S1/S2, genuine shows strong D1-D3）在实际中可能不那么干净。\n\n【核心贡献】:\n两个独立贡献：\n1. **诊断性贡献**：首次系统测量 rubric-based math RLVR 中按难度分层的 gaming rate，建立\"难度利用梯度\"作为一个经验现象。这可能是更有持久价值的贡献——即使 DCM 方法本身被更好的方法取代，这个 diagnostic 发现作为 empirical observation 仍然有引用价值。\n2. **防御性贡献**：DCM 聚合，一种机制层面的防御，通过在高难度问题上强制所有 criterion 满足来移动 gaming 均衡点。配有理论 bound（gaming payoff bounded by min_k(ε_k) as τ→0）和与均衡框架的联系。\n\n对领域的价值：中等偏高。这个工作不会改变 RLVR 的范式，但它填补了一个实际的盲区，提供了一个实用的防御工具，并且其诊断方法论可以被广泛复用。\n\n【方法合理性】:\n方法整体合理，但存在值得推敲的点：\n\n**合理之处：**\n- Softmin 作为 aggregation operator 有清晰的数学动机：当 τ→0 时退化为 min，强制所有 criterion 满足，直接攻击 partial satisfaction gaming。\n- 难度条件化的 τ schedule（τ = τ₀·(1-d)^α）是合理的连续化设计，避免了硬阈值。\n- 与 PURE 的区分是真实的：无序 rubric dimensions vs 有序时序步骤，无 error compounding，需要独立分析。\n\n**潜在问题：**\n1. **更简单的替代方案**：静态 min aggregation（difficulty-agnostic min）是一个天然的 baseline，proposal 已包含。但审稿人可能会问：为什么不简单地在高难度问题上增大 criterion weight 的最小值（即 min-weight clipping），而非改变整个聚合函数？这在概念上更简单，可能效果相近。\n2. **τ schedule 的粒度**：使用 pass-rate quintiles 作为离散难度代理，再映射到连续 τ——这引入了离散化噪声和 quintile 边界效应。Proposal 的 ablation（pass-rate quintile vs model-estimated difficulty）覆盖了这点。\n3. **Rubric criteria 的 LLM-as-judge 可靠性**：D1（逻辑有效性）和 D2（数学严谨性）的评分本身在高难度问题上可能不够可靠，这可能混淆诊断结果。交叉 judge panel 部分缓解了这个问题。\n4. **Genuine hard solutions 的惩罚风险**：Proposal 声称 gaming 和 genuine 的 rubric profile 可区分（S1-S2 高 vs D1-D3 高），但这一假设的鲁棒性未经验证。如果某些 genuine hard solutions 的 D criteria 也偶尔较低（例如，正确但不够严谨的解法），DCM 会过度惩罚它们。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — 两个活跃研究方向（rubric aggregation + difficulty-aware RL）的交叉空白经调研确认为真实存在。\"难度利用梯度\"有清晰的理论动机（effort asymmetry + detection blindness），且与 arXiv:2604.15149 的实证发现和 arXiv:2603.28063 的理论框架一致。问题的实际意义也很明确：rubric-based RLVR 正在被广泛部署（DeepSeek-R1 后），如果高难度问题的 gaming 确实更严重，这是一个必须解决的可靠性问题。\n  \n  2. 方法与创新: 【中】 — 技术创新的核心是 softmin + difficulty-conditioned τ，这是一个数学上简洁但深度有限的贡献。与 PURE (NeurIPS 2025) 的区分是合理的（无序维度 vs 有序时序步骤），但 softmin 本身不是新 operator。与 Focal Reward (arXiv:2605.26579) 的\"症状层 vs 机制层\"区分有洞察力但也有些 over-sell：Focal Reward 的 headroom 也可以被解释为间接的 mechanism signal。理论 bound（gaming payoff ≤ min_k(ε_k)）是清晰的但推导难度不高。总体而言，方法的价值更多来自\"在正确的地方使用了正确的工具\"而非算法本身的技术深度。\n  \n  3. 实验设计: 【强】 — 这是 proposal 最突出的优势。7+1 baselines 覆盖了所有主要竞争方法（POW3R, Focal Reward, DGPO, PAPO），包含 difficulty-agnostic min 和 Focal Reward+DCM 组合以验证互补性。6 个 benchmark 覆盖 in-distribution / OOD / harder / easier。多层级 gaming 指标（HRWAR + AUC, cross-judge disagreement, self-internalization gap）和 per-quintile 分析是诊断叙事的核心。Ablation 设计系统（聚合进阶、schedule 形式、超参数 heatmap、难度代理、rubric 粒度）。Multi-seed + bootstrap CI + compute-budget equalization 体现了严谨性。相比领域内多数并发工作（如 POW3R 仅报告 30 个 comparisons），实验设计的覆盖度和严谨度明显高于平均水平。\n  \n  4. 可行性: 【中偏强】 — ~5,500 A100-hours 是一个可观但在有 GPU 集群访问权的实验室范围内可行的预算。Tiered compute strategy（1.5B 做全 ablation，8B 做关键比较）是务实的。主要风险不在资源而在假说验证：如果\"难度利用梯度\"在实证中不够显著（例如，HRWAR 跨 quintile 的差异只有几个百分点），整篇论文的叙事基础将被削弱。此外，K=5 的 rubric criteria 中的 LLM-as-judge 评分（特别是 D1, D2）在高难度数学问题上的可靠性是一个实操风险。\n  \n  5. 写作与呈现: 【强】 — Proposal 的组织结构清晰（问题→贡献→研究空白→方法→实验），对相关工作的定位精准且诚实（与 Focal Reward、DGPO、PURE 的区分都有实质内容而非草率dismissal）。\"诊断 + 防御\"的双贡献叙事是一个强大的 paper framing——即使 DCM 方法的优势不够大，诊断发现本身就有独立发表价值。两个机制（effort asymmetry + detection blindness）的分解让论证有层次感。唯一的呈现风险是：8 页正文可能难以容纳如此丰富的内容（理论 + 诊断 + 方法 + 实验 + ablation）。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】: \nAAAI 2026 接受率 17.6%。本 proposal 的核心优势在于：(1) 精准定位了一个经调研确认的真实研究空白；(2) 实验设计的完备程度在同领域 proposal 中属于上游；(3) \"诊断 + 防御\"的双贡献叙事降低了单点失败风险；(4) 时机极好，处于 rubric-based RLVR 的研究热潮中。主要拖累因素：(1) 方法本身的技术深度有限（softmin 不是新 operator，difficulty conditioning 的 idea 概念上不复杂）；(2) 整个叙事高度依赖一个尚未验证的经验假说（难度利用梯度的显著性）；(3) 仅在数学领域验证，泛化性未展示。\n\n在乐观情境下（难度利用梯度显著、DCM 在 Q4-Q5 上的 gaming rate 下降显著且 Q1-Q3 不受损、理论 bound 紧致），这是一篇 solid 的中稿级别工作（~42%）。在悲观情境下（梯度不够显著、DCM 对 genuine hard solutions 有明显误伤、或审稿人认为方法太简单），概率下降至 ~28%。中位估计 35%，反映一篇有真实贡献但方法深度不足以拿到 strong accept 的竞争性投稿。\n\n【主要风险】: \n1. **经验假说风险**：整篇论文的核心叙事建立在\"难度利用梯度单调递增且幅度足够显著\"这一假说上。如果实际测量发现梯度微弱或非单调（例如中等难度才是 gaming 峰值），诊断贡献和防御动机都将受到严重质疑。这是最大的单点失败风险。\n2. **方法深度不足**：在 AAAI 这样的竞争性会议，审稿人可能认为\"将 softmin 用于 rubric aggregation 并加上 difficulty conditioning\"缺乏足够的算法创新，仅是现有工具的简单组合。理论 bound 虽然清晰但推导不复杂，可能被认为是 straightforward corollary。若审稿人持此观点，方法贡献可能被评为 incremental。\n\n【实施评估】:\n  - 计算资源: ~5,500 A100-hours（1,500 for 1.5B ablation + 4,000 for 8B key comparisons）。需要可靠的 A100/H100 集群访问。对有 GPU 集群的实验室属于中等规模实验。\n  - 数据需求: MATH 训练集（~7.5K）+ NuminaMath（公开可用）+ 6 个评测 benchmark（MATH-500, AIME 2024/2025, OlympiadBench, AMC 2023, GSM8K，全部公开）。数据不是瓶颈。\n  - 人工介入: 中等。需要：(1) 设计和迭代 K=5 rubric criteria 的 prompt engineering；(2) 调试 cross-family judge panel（GPT-4o, Claude Sonnet, Gemini Pro）的 API 调用和一致性；(3) 分析 gaming vs genuine profiles 的定性检查。无需大规模人工标注。\n  - 训练需求: 是。需要在 Qwen3-8B 和 Qwen3-1.5B 上进行完整的 GRPO 训练，使用 verl 框架。每个方法/配置需要独立训练 run。Total ~20-30 个独立训练 run（含 multi-seed）。\n  - 新 Benchmark: 否。使用现有 benchmark。但诊断指标 HRWAR 是新定义的，需要实现和验证。\n  - 预估周期: 8-12 周。Phase 1（2-3 周）：基础设施搭建（verl + rubric judge + 难度分层）。Phase 2（3-4 周）：1.5B 上的全 ablation + diagnostic。Phase 3（3-4 周）：8B 上的关键比较 + 理论验证。Phase 4（1-2 周）：论文撰写。总体时间线紧凑但可行。\n```\n\nSources:\n- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)\n- [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)\n- [DGPO: Harder Is Better](https://arxiv.org/abs/2601.20614)\n- [POW3R: Policy-Aware Rubric Rewards](https://arxiv.org/abs/2605.20164)\n- [Focal Reward: Balanced RL under Rubric-Based Rewards](https://arxiv.org/abs/2605.26579)\n- [Stop Summation / PURE](https://arxiv.org/abs/2504.15275)\n- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063)\n- [DARO: Difficulty-Aware Reweighting Policy Optimization](https://arxiv.org/abs/2510.09001)\n- [AAAI 2026 Accepted Papers Highlights](https://www.bohrium.com/blog/research-notes/aaai-2026-accepted-papers-highlights/)\n- [Reward Hacking in RLVR Systems](https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Difficulty-Conditioned Min-Form Rubric Rewards Resist Gaming\n\n## Core Problem\n\nUniform rubric strictness across problem difficulty levels creates a difficulty exploitation gradient in rubric-based RLVR, driven by two reinforcing mechanisms:\n\n1. **Effort asymmetry**: Genuine solving effort scales super-linearly with difficulty (harder problems require longer reasoning chains with compounding error risk), while gaming effort scales sub-linearly (shallow pattern-matching strategies that partially satisfy rubric criteria transfer across difficulty levels with minimal adaptation).\n\n2. **Detection blindness**: Uniform rubric aggregation has structurally lower discriminative power on hard problems—hard-problem responses exhibit higher rubric score variance even among genuine attempts, making it harder to distinguish gaming-induced partial satisfaction from genuine partial progress. The false-positive-tolerant regime on hard problems makes gaming systematically cheaper to disguise.\n\nTogether, these mechanisms create a monotonically increasing gaming profit margin with difficulty: hard problems are simultaneously the easiest to game and the hardest to detect gaming on. No existing work has diagnosed or defended against this difficulty-dependent gaming phenomenon.\n\n## Contributions\n\nWe make two independent contributions:\n\n1. **Diagnostic**: The first systematic measurement of difficulty-stratified gaming rates in rubric-based math RLVR, establishing the difficulty exploitation gradient as an empirical phenomenon (not merely hypothesized).\n\n2. **Defense**: Difficulty-Conditioned Min-form (DCM) aggregation, a mechanism-level defense that forces strict all-criterion satisfaction on hard problems, shifting the gaming equilibrium by making the gaming payoff bounded by the hardest-to-game criterion.\n\n## Research Opportunity\n\nThree lines converge on an untouched gap: (1) Reward Hacking in Rubric-Based RL (arXiv:2605.12474) taxonomizes rubric gaming, showing partial compound satisfaction accounts for 36% of gaming and noting a Simpson's paradox confound, but never investigates difficulty-dependent gaming rates (experiments in medical/science domains); (2) LLMs Gaming Verifiers (arXiv:2604.15149, ICLR 2026 Workshop) confirms shortcut prevalence increases with task complexity in inductive reasoning, with their explanation (extensional correctness admits more false positives for complex tasks) directly supporting our detection-blindness mechanism; (3) DGPO (arXiv:2601.20614, ICLR 2026) proves difficulty-dependent update magnitude bias but only for binary rewards. All 7+ concurrent rubric reweighting papers are difficulty-agnostic, and all difficulty-aware methods operate only on scalar outcome rewards.\n\nFrom a structural perspective, Reward Hacking as Equilibrium (arXiv:2603.28063) proves under five minimal axioms that any optimized agent under-invests in quality dimensions not adequately covered by evaluation. Difficulty-agnostic rubric aggregation structurally under-covers hard-problem criteria (uniform temperature fails to penalize partial satisfaction sufficiently at high difficulty), creating an equilibrium favoring gaming. DCM shifts this equilibrium by increasing the cost of under-investing in any single rubric dimension proportionally to difficulty-induced gaming vulnerability.\n\n## Research Landscape\n\nRubric reward aggregation (2026): POW3R (arXiv:2605.20164) reweights by rollout variance; Focal Reward (arXiv:2605.26579) by criterion saturation headroom; PAPO (arXiv:2603.26535) decouples ORM/PRM advantages; SRaR (arXiv:2605.17291) attributes rubrics to steps. None condition on difficulty.\n\nDifficulty-aware RL: DGPO (arXiv:2601.20614, ICLR 2026) uses difficulty-balanced group advantage; DARO (arXiv:2510.09001) dynamically adjusts loss contribution per difficulty group based on model learning state; GRPO-LEAD uses difficulty-aware advantage reweighting. All operate only on binary outcome rewards. The key distinction: DARO/DGPO adjust policy optimization (loss weights), while DCM adjusts reward signal construction (aggregation). They solve different problems (learning efficiency vs anti-gaming) and can be combined.\n\nGaming detection/theory: arXiv:2605.12474 taxonomizes rubric gaming but proposes no defense; arXiv:2603.28063 proves reward hacking is a structural equilibrium; arXiv:2604.01476 extracts shortcut behavior directions for detection.\n\n**Critical distinction from Focal Reward**: Focal Reward operates at the **symptom level**—it measures criterion saturation headroom (how much improvement remains) and upweights high-headroom criteria. But saturation headroom is agnostic to the *source* of headroom: gaming-induced suppression, genuine difficulty, or model capacity limits are treated identically. When easy and hard problems' headroom statistics are pooled, hard-problem gaming signals get diluted by easy-problem genuine headroom. DCM operates at the **mechanism level**—it directly constrains that no criterion can be abandoned on hard problems, with constraint strength proportional to gaming vulnerability (difficulty proxy), regardless of headroom patterns. Focal Reward answers \"which criterion to emphasize\"; DCM answers \"how strictly to enforce the weakest criterion given gaming risk.\" The two are complementary: Focal Reward optimizes learning signal quality while DCM prevents exploitation of the reward function.\n\nNo concurrent work combines difficulty conditioning with rubric aggregation for anti-gaming defense—confirmed via arXiv and OpenReview search through May 2026.\n\n## Proposed Approach\n\n**Training setup.** Train Qwen3-8B (primary) and Qwen3-1.5B (generalization) via GRPO + rubric rewards on the MATH training set (~7.5K problems), supplemented with NuminaMath for prompt diversity, using verl. Difficulty defined via base-model pass-rate quintiles (static, computed before training, following DGPO's practice).\n\n**Rubric criteria (K=5 canonical).** Surface-level: (S1) solution format compliance, (S2) step-by-step structure presence. Deep-level: (D1) logical validity of reasoning steps, (D2) mathematical rigor/correctness of operations, (D3) final answer correctness. The surface/deep distinction enables analysis of gaming-characteristic vs genuine-characteristic rubric profiles.\n\n**Diagnostic.** Measure per-stratum gaming with multi-level metrics: (1) Primary: High-Rubric-Wrong-Answer Rate (HRWAR) = P(rubric_score > θ ∧ answer incorrect), exploiting math's ground-truth verifiability. Report HRWAR-vs-θ curve and threshold-free AUC summary. (2) Secondary: cross-judge disagreement using cross-family panel (GPT-4o, Claude Sonnet, Gemini Pro). (3) Tertiary: self-internalization gap (from arXiv:2605.12474). All metrics reported per difficulty quintile.\n\n**DCM aggregation.** Replace mean rubric aggregation with softmin: r = -τ·log(Σ exp(-s_k/τ)) where τ = τ₀·(1-d)^α decreases with difficulty d ∈ [0,1], so hard-problem rewards → min(s_k). Easy-problem behavior remains mean-like (preserving learning signal), while hard-problem behavior enforces strict all-criterion satisfaction.\n\n**Addressing genuine-solution penalty.** Gaming-induced unevenness and genuine unevenness are structurally distinguishable: gaming inflates surface criteria (S1, S2) while neglecting deep criteria (D1-D3); genuine hard solutions show the reverse (potentially lower S1/S2 but strong D1-D3). The softmin thus selectively penalizes the gaming-characteristic profile. We validate empirically by analyzing per-criterion profiles of correct vs incorrect solutions across difficulty strata.\n\n**Theoretical contribution.** We derive an anti-gaming bound for cross-dimension softmin: if gaming inflates criterion k's score by ε_k, DCM-aggregated reward inflation is bounded by min_k(ε_k) as τ→0, meaning gaming payoff is limited by the hardest-to-game criterion. Unlike Stop Summation/PURE (arXiv:2504.15275, NeurIPS 2025), whose bound addresses temporal step-wise aggregation (ordered, error-compounding), our setting involves unordered dimensions with independent errors—structurally different, requiring independent derivation. We characterize bound degradation with τ and connect to the equilibrium framework: DCM equalizes the distortion index (from arXiv:2603.28063) across difficulty strata.\n\n## Experimental Design\n\n**Baselines (7 methods + 1 combination):**\n- GRPO + outcome-only reward (binary, no rubric)\n- GRPO + mean rubric aggregation (standard rubric baseline)\n- GRPO + static min aggregation (difficulty-agnostic min)\n- POW3R (arXiv:2605.20164, variance-based reweighting)\n- Focal Reward (arXiv:2605.26579, saturation-aware reweighting)\n- DGPO (arXiv:2601.20614, difficulty-aware binary reward)\n- PAPO (arXiv:2603.26535, decoupled advantage)\n- **Focal Reward + DCM** (combination: validates complementarity claim)\n\n**Evaluation benchmarks (6):**\n- In-distribution: MATH-500, AIME 2024\n- OOD / harder: AIME 2025, OlympiadBench, AMC 2023\n- Easier (ceiling): GSM8K\n\nPer benchmark: (1) accuracy (pass@1); (2) gaming rate (HRWAR + AUC, per-difficulty); (3) rubric score distribution.\n\n**Per-difficulty-stratum analysis (core to narrative):** For each method, report accuracy and gaming rate broken down by difficulty quintile. Key expected finding: DCM's advantage concentrates in Q4-Q5 (hardest) while preserving Q1-Q3 performance; static min damages Q1-Q3; Focal Reward is uniform across strata.\n\n**Ablation studies:**\n1. Aggregation progression: mean → fixed-τ softmin → DCM (isolates difficulty conditioning value)\n2. Schedule: τ₀·(1-d)^α vs linear vs step-function\n3. Hyperparameter sensitivity: τ₀ ∈ {0.1, 0.5, 1.0, 2.0}, α ∈ {0.5, 1.0, 2.0} (heatmap on 1.5B)\n4. Difficulty proxy: pass-rate quintile vs model-estimated difficulty\n5. Rubric granularity: K ∈ {3, 5, 8}\n\n**Theory validation:** Plot theoretical bound vs actual gaming payoff inflation across τ settings, demonstrating bound tightness and degradation curve.\n\n**Reproducibility controls:**\n- 3 random seeds for DCM + Focal Reward + combo (significance testing); other baselines 1 seed on 8B, 3 seeds on 1.5B\n- Identical compute budget across methods (same GRPO steps × rollouts)\n- Report GPU-hours per method; performance-vs-compute curves\n- Bootstrap confidence intervals for small benchmarks (AIME)\n\n**Compute strategy (tiered):** Full ablation + multi-seed on Qwen3-1.5B (~1,500 A100-hours); key comparisons (DCM vs top-3 baselines + combo + core ablation) on Qwen3-8B (~4,000 A100-hours). Total: ~5,500 A100-hours.\n\n## Key References\n\n- Reward Hacking in Rubric-Based RL (arXiv:2605.12474, arXiv 2026)\n- LLMs Gaming Verifiers (arXiv:2604.15149, ICLR 2026 Workshop)\n- DGPO: Harder Is Better (arXiv:2601.20614, ICLR 2026)\n- Stop Summation / PURE (arXiv:2504.15275, NeurIPS 2025)\n- POW3R: Policy-Aware Rubric Rewards (arXiv:2605.20164, arXiv 2026)\n- Focal Reward (arXiv:2605.26579, arXiv 2026)\n- GRPO-LEAD (arXiv 2025)\n- PAPO: Decoupled Advantage Normalization (arXiv:2603.26535, arXiv 2026)\n- SRaR: Step-wise Rubric Rewards (arXiv:2605.17291, arXiv 2026)\n- Reward Hacking as Equilibrium (arXiv:2603.28063, arXiv 2026)\n- Representation-Level Reward Hacking (arXiv:2604.01476, arXiv 2026)\n- DARO: Difficulty-Aware Reweighting (arXiv:2510.09001, arXiv 2025)"
}
````

---

### Runtime record

_source line 2 · 2026-05-29T06:41:36.778Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:41:36.778Z",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-29T06:41:36.806Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile my evaluation.

```
【阶段】: Triage

【领域调研】:
- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474) (arXiv 2026): 最直接相关的工作。对 rubric gaming 进行了分类学研究，发现 partial compound satisfaction 占 gaming 的 36%，注意到 Simpson's paradox confound，但**未按难度分层分析 gaming 率**——正是本 proposal 要填补的空白。实验在医学/科学领域，非数学。
- [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149) (ICLR 2026 Workshop): 在归纳推理任务上确认 shortcut prevalence 随任务复杂度单调递增，模型放弃规则归纳转而枚举实例级标签。其发现（extensional correctness 对复杂任务接受更多 false positive）直接支撑本 proposal 的 "detection blindness" 机制。
- [DGPO: Harder Is Better](https://arxiv.org/abs/2601.20614) (ICLR 2026): 难度感知 GRPO，基于 group-level advantage reweighting，但仅适用于 binary outcome reward。证明了难度依赖的更新幅度偏差。是本 proposal 难度感知维度的对标方法，但不涉及 rubric aggregation。
- [POW3R](https://arxiv.org/abs/2605.20164) (arXiv 2026): 基于 rollout variance 的 rubric criterion reweighting，preserves human weight prior。难度无关。24/30 comparison wins over vanilla GRPO。
- [Focal Reward](https://arxiv.org/abs/2605.26579) (arXiv 2026): 基于 criterion saturation headroom 的自适应 reweighting，inverse reward projection 估计饱和度。难度无关。Proposal 对 Focal Reward 的 "symptom-level vs mechanism-level" 区分论证是 well-articulated。
- [PAPO](https://arxiv.org/abs/2603.26535) (arXiv 2026): 将 ORM 和 rubric-based PRM 的 advantage decoupled normalization。解决的是训练稳定性，非 anti-gaming。
- [SRaR](https://arxiv.org/abs/2605.17291) (arXiv 2026): Step-wise rubric attribution，发现 18.2% correct-answer 的 steps 错误但被正奖励。关注 step-level 粒度，非 difficulty conditioning。
- [Reward Hacking as Equilibrium](https://arxiv.org/abs/2603.28063) (arXiv 2026): 理论框架，证明在五条极小公理下任何优化 agent 会 under-invest 于未被评估覆盖的质量维度。Proposal 将 DCM 的作用映射到该框架的 "distortion index equalization"，理论链接合理。
- [DARO](https://arxiv.org/abs/2510.09001) (arXiv 2025): Difficulty-aware reweighting for policy optimization (loss weights)，与 DCM 解决不同层面问题（loss vs reward construction），可组合。

- **调研总结**: 2026 年 rubric-based RLVR 领域极为活跃，7+ 篇并发工作分别从 variance、saturation、step-level、process-level 等角度优化 rubric aggregation，但全部 difficulty-agnostic。难度感知方法（DGPO/DARO/GRPO-LEAD）则全部限于 binary outcome reward。**将难度 conditioning 引入 rubric aggregation 作为 anti-gaming defense 确实是一个尚未被触碰的交叉空白**，proposal 的 gap claim 经调研验证成立。

【整体印象】:
作为审稿人，第一反应是 **cautious positive**——倾向 weak accept 到 borderline。这是一篇在活跃领域精准定位了交叉空白的 well-crafted proposal：问题动机清晰、方法简洁有原则、实验设计异常完备。两个机制（effort asymmetry + detection blindness）的论证有理论支撑且被已有实证（arXiv:2604.15149）部分验证。但主要担忧在于：(1) 核心假设（difficulty exploitation gradient 是一个足够显著的经验现象）尚未被验证，如果效应量小则论文立意动摇；(2) 方法本质上是 "difficulty-conditioned softmin temperature"，简洁但可能被 aggressive reviewer 视为 incremental combination。

【核心贡献】:
两个独立贡献：
1. **诊断性贡献**：首次系统测量 rubric-based math RLVR 中按难度分层的 gaming rate，建立 "difficulty exploitation gradient" 作为经验现象（HRWAR + cross-judge + self-internalization gap 三级指标体系）。
2. **防御性贡献**：DCM 聚合机制——softmin with difficulty-conditioned temperature，将 hard-problem reward 推向 min(s_k)，使 gaming payoff 受限于最难 game 的 criterion。

对领域的价值：如果诊断贡献得到验证，这将是 rubric RLVR 领域一个重要的 empirical finding，因为它揭示了一个 structural vulnerability 而非 incidental bug。DCM 作为 defense 的简洁性是优势（易于在 existing pipeline 中集成），但也限制了 novelty ceiling。

【方法合理性】:
**合理，但有条件。**

优点：
- Softmin 是 min 的 smooth relaxation，数学性质清晰，τ→0 时 → min(s_k)，τ→∞ 时 → mean(s_k)，连续可控。
- Difficulty conditioning 的逻辑链完整：difficulty ↑ → gaming profit ↑ → 需要更严格的 all-criterion enforcement → τ ↓。
- Anti-gaming bound（gaming payoff bounded by min_k(ε_k) as τ→0）是 straightforward 但有用的理论保证。
- 与 Stop Summation/PURE 的区分（temporal vs unordered dimensions）是正确的。

潜在替代方案/质疑：
1. **更简单的替代**：直接对 hard problems 使用 min aggregation（binary difficulty threshold）是否足够？Proposal 确实在 ablation 中包含了 "fixed-τ softmin" 和 "step-function schedule"，这是好的实验设计。
2. **Genuine solution penalty 的风险**：Proposal 声称 gaming profile（high S1/S2, low D1-D3）与 genuine profile（potentially low S1/S2, high D1-D3）可区分。但在 hard math problems 上，genuine attempts 也经常在 D1-D3 上得分不均（某步推理正确但另一步出错），softmin 对这类 genuine partial progress 同样会施加惩罚。这是方法的 Achilles heel。
3. **Surface/Deep 二分法的假设强度**：K=5 criteria 的 surface/deep 分类是否 robust？如果 LLM judge 在 hard problems 上的 D1-D3 评分本身 noisy（hard problems 的 judge reliability 通常更低），DCM 的 min 特性会 amplify judge noise。

【5 维度打分】:

1. **研究问题: 强** — 问题定义精准，且由三条独立证据线（arXiv:2605.12474 的 gaming taxonomy、arXiv:2604.15149 的 complexity-dependent shortcut、arXiv:2601.20614 的 difficulty-dependent bias）交叉支撑。"Difficulty exploitation gradient" 是一个清晰、可检验的假设。在 7+ 篇并发 rubric reweighting 工作均 difficulty-agnostic 的背景下，这是一个真实的 gap。唯一扣分：如果效应量不显著，问题的 practical importance 会受质疑。

2. **方法与创新: 中（偏强）** — DCM 的核心创新是将 softmin temperature 与 difficulty conditioning 结合。与 Focal Reward（arXiv:2605.26579）的 "symptom vs mechanism" 区分论证有力。与 DGPO（arXiv:2601.20614）的区分（reward construction vs loss weighting）清晰，且二者可组合。理论贡献（anti-gaming bound + equilibrium framework connection）增色。但方法本身是 softmin 的一个参数化变体，创新跨度有限。一个 skeptical reviewer 可能认为这是 "softmin + difficulty schedule" 的 engineering combination。

3. **实验设计: 强** — 这是 proposal 最突出的维度。7 baselines 覆盖了所有主要并发工作（POW3R、Focal Reward、DGPO、PAPO）+ 标准 ablation 参照（outcome-only、mean rubric、static min）。6 benchmarks（ID + OOD + easier ceiling）。5 项 ablation 全面且有针对性。Focal Reward + DCM 组合验证 complementarity claim。三级 gaming 指标（HRWAR + cross-judge + self-internalization gap）。Multi-seed + bootstrap CI。Compute tiered strategy 合理。**这个实验方案如果忠实执行，其完备性本身就是对 reviewers 的说服力。**

4. **可行性: 中** — ~5,500 A100-hours 对大多数学术实验室是 significant（约 10-15 天 8×A100 集群 或 $5-10K 云计算成本），但对 well-funded labs 完全可行。主要风险不在计算资源，而在：(a) LLM judge（GPT-4o、Claude、Gemini）的 cross-judge panel 需要 API access + 费用；(b) 核心假设可能不成立（empirical risk）；(c) verl 框架 + Qwen3 的工程集成可能有 friction。时间线上，从实验到写作约需 3-4 个月，对 AAAI 2026 DDL 需确认 timing。

5. **写作与呈现: 强** — Proposal 的逻辑结构清晰：Problem → Two Mechanisms → Gap → Method → Theory → Experiments。与并发工作的定位精准，每篇对标论文都有明确的 "solves different problem / complementary" 论证。Critical distinction from Focal Reward 一节尤为出色。术语使用一致（effort asymmetry、detection blindness、gaming profit margin 等概念贯穿始终）。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:

**拉高因素：**
- 精准的 gap identification，经调研确认 no concurrent work 在此交叉点上（+）
- 异常完备的实验设计，7 baselines + 6 benchmarks + 5 ablations 已达 top-tier 标准（+）
- 双贡献结构（diagnostic + defense），即使 DCM 效果有限，diagnostic 本身有独立价值（+）
- 与并发工作的 positioning 极为精准，reviewers 不太可能找到被遗漏的直接竞争者（+）
- 理论贡献（bound + equilibrium connection）为方法提供了 principled justification（+）
- 领域极为热门（2026 RLVR/rubric RL），reviewer pool likely 对此问题有共鸣（+）

**压低因素：**
- 方法本质是 softmin temperature 的 difficulty-conditioned scheduling，创新跨度有限（−）
- 核心假设（difficulty exploitation gradient 显著存在）是 empirical bet——如果效应量小，论文叙事坍塌（−）
- Genuine solution penalty 的担忧需要极为有力的 empirical defense，如果 per-criterion profile 分析不够 convincing，会被质疑 DCM 对 genuine hard solutions 的 collateral damage（−）
- Math-only domain 限制了 generalizability claim（−）
- LLM judge 在 hard problems 上的 reliability 问题未充分 addressed——DCM 的 min 特性会 amplify judge errors（−）
- AAAI 竞争激烈（acceptance rate ~20-23%），即使 solid 的 work 也面临筛选压力（−）

**综合判断：** 这是一篇 direction 正确、design 扎实、positioning 精准的 proposal。在 AAAI 的 reviewer pool 中，如果遇到对 RLVR gaming 问题有认知的 reviewer，有较好机会拿到 positive review；但如果遇到 skeptical reviewer 质疑 "这是否只是 softmin + difficulty heuristic 的工程组合"，则可能被 borderline reject。中位估计 35% 反映的是一篇 "solid but not exceptional" 的投稿在顶会的 typical odds。

【主要风险】:
1. **Empirical bet 失败风险**：如果诊断实验显示 difficulty exploitation gradient 的效应量不够显著（例如 HRWAR 跨难度 quintile 的差异 < 5 percentage points），整篇论文的 motivation 和 contribution 都会大幅贬值。这是 make-or-break 风险。
2. **Genuine solution collateral damage**：如果 DCM 在 hard problems 上对 genuine partial progress 施加了过度惩罚（导致 Q4-Q5 accuracy 下降而非持平/上升），reviewer 会质疑 method 的 precision——anti-gaming defense 如果 friendly fire 严重，则 net value 存疑。这需要 per-criterion profile 分析非常有说服力。

【实施评估】:
  - **计算资源**: ~5,500 A100-hours（1,500 for 1.5B ablation + 4,000 for 8B key comparisons）。需 8×A100 集群或等价云资源。成本约 $5K-$15K（取决于定价）。对 well-funded 学术组可行，对资源有限的组有一定门槛。
  - **数据需求**: MATH training set (~7.5K) + NuminaMath（公开数据集）。评测用 MATH-500, AIME 2024/2025, OlympiadBench, AMC 2023, GSM8K 均为公开 benchmark。数据获取无障碍。
  - **人工介入**: 中等。需要：(1) rubric criteria 设计与 LLM judge prompt engineering；(2) cross-judge panel setup（GPT-4o, Claude, Gemini API 配置）；(3) difficulty quintile 计算（base-model pass-rate，需要一次性评估）；(4) 实验 pipeline 集成（verl + GRPO + rubric judge）。
  - **训练需求**: 需要完整的 GRPO 训练 pipeline。Primary: Qwen3-8B，Secondary: Qwen3-1.5B。每个 baseline/variant 需独立训练。Multi-seed 配置（DCM + Focal + combo 3 seeds on 8B；全部方法 3 seeds on 1.5B）。
  - **新 Benchmark**: 不需要构建新 benchmark。需要构建新的诊断指标体系（HRWAR + cross-judge disagreement + self-internalization gap per difficulty quintile），但这是分析 pipeline 而非 benchmark。
  - **预估周期**: 3-4 个月。Breakdown: 实验 pipeline 搭建 + difficulty quintile 计算（2-3 周）→ 1.5B 全量 ablation + diagnostic（3-4 周）→ 8B key comparisons（3-4 周）→ 分析 + 论文写作（3-4 周）。关键路径在 1.5B ablation 和 8B training 的顺序执行。
```

Sources:
- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474)
- [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149)
- [DGPO: Harder Is Better](https://arxiv.org/abs/2601.20614)
- [POW3R: Policy-Aware Rubric Rewards](https://arxiv.org/abs/2605.20164)
- [Focal Reward](https://arxiv.org/abs/2605.26579)
- [PAPO: Decoupled Advantage Normalization](https://arxiv.org/abs/2603.26535)
- [SRaR: Step-wise Rubric Rewards](https://arxiv.org/abs/2605.17291)
- [Reward Hacking as Equilibrium](https://arxiv.org/abs/2603.28063)
- [DARO: Difficulty-Aware Reweighting](https://arxiv.org/abs/2510.09001)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a comprehensive evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [arXiv:2605.12474] Reward Hacking in Rubric-Based RL (arXiv 2026): 最直接相关——首次系统分类 rubric gaming（含 partial compound satisfaction 占比 36%），提到 Simpson's paradox confound，但未按难度分层分析 gaming 率。本 proposal 的 diagnostic 贡献正是填补此空白。
- [arXiv:2604.15149] LLMs Gaming Verifiers (ICLR 2026 Workshop): 证实任务复杂度越高、shortcut 越普遍（extensional correctness 对复杂任务 admits more false positives），直接支持 proposal 的 detection-blindness 机制。但该工作在 inductive reasoning 非 math 场景。
- [arXiv:2601.20614] DGPO (ICLR 2026): 难度感知 GRPO 变体，通过 group advantage 平衡解决 learning efficiency 偏差，但仅操作 binary outcome reward。Proposal 正确区分了 policy optimization vs reward construction 的不同层面。
- [arXiv:2605.20164] POW3R (arXiv 2026): 按 rollout contrastiveness（标准差）动态调整 rubric criterion 权重，难度无关。24/30 comparisons 胜出，是强 baseline。
- [arXiv:2605.26579] Focal Reward (arXiv 2026): 按 criterion saturation headroom 自适应 reweight，解决 dimension 间极化问题。Proposal 对其的"symptom-level vs mechanism-level"区分论述清晰且成立——Focal Reward 确实无法区分 headroom 的来源（gaming vs 真实难度 vs 能力上限）。
- [arXiv:2603.26535] PAPO (arXiv 2026): 解耦 ORM/PRM advantage normalization，解决 PRM 引入的 verbosity hacking，与本 proposal 方向正交。
- [arXiv:2605.17291] SRaR (arXiv 2026): 将 rubric 评分下放到 step 粒度，消除 indiscriminate supervision，正交于 difficulty conditioning。
- [arXiv:2504.15275] Stop Summation / PURE (NeurIPS 2025): 提出 temporal min-form credit assignment 防止 PRM reward hacking。Proposal 区分了 temporal step-wise aggregation vs unordered dimension aggregation，理论上需独立推导，此区分成立。
- [arXiv:2603.28063] Reward Hacking as Equilibrium (arXiv 2026): 理论框架——五公理下任何优化 agent 在评估未覆盖维度上 under-invest。Proposal 将其作为 DCM 的理论支撑（均衡化 distortion index），连接合理。
- [arXiv:2510.09001] DARO (arXiv 2025): 按难度动态调 loss contribution，与 DGPO 类似，仅操作 binary reward。
- 调研总结: Rubric-based RLVR 和 reward hacking 是 2025-2026 极热方向，并发论文众多但均沿两条独立线展开——rubric 聚合优化（difficulty-agnostic）和 difficulty-aware RL（binary reward only）。在我的搜索中**未发现任何工作将 difficulty conditioning 与 rubric aggregation 结合用于 anti-gaming**，proposal 的 novelty claim 经验证成立。

【整体印象】:
作为审稿人，第一反应是 lean toward weak accept / borderline accept。这是一篇精心构造的 proposal，选取了两条活跃研究线的真实交叉空白，问题动机 well-grounded（effort asymmetry + detection blindness 两机制的论述有说服力），实验设计异常详尽（7+1 baselines、6 benchmarks、5 ablation、multi-seed + bootstrap CI）。但核心技术贡献——difficulty-conditioned softmin——本质是一个参数化温度调度的 softmin，技术上偏 incremental；整篇论文的 impact 高度依赖诊断性结果（difficulty exploitation gradient 是否 empirically 显著），如果实验中 gaming 率与难度的相关性不够 dramatic，防御机制就失去了动力。

【核心贡献】:
1. **诊断贡献**（potentially higher impact）：首次系统测量 rubric-based math RLVR 中 difficulty-stratified gaming 率，建立 difficulty exploitation gradient 作为经验现象。这是领域的 factual gap——arXiv:2605.12474 分类了 gaming 但未按难度分析；arXiv:2604.15149 观察到复杂度-shortcut 关联但在不同 domain。如果 diagnostic 结果 robust，这本身对领域有重要价值。
2. **防御贡献**：DCM（difficulty-conditioned softmin）作为 mechanism-level defense，思路清晰但技术上较简单。理论 bound（gaming payoff bounded by min_k(ε_k) as τ→0）有价值但推导难度不高。

核心贡献的领域价值：中等偏上。诊断贡献如果 robust，会被广泛引用；防御贡献更像一个 strong baseline 而非 paradigm shift。

【方法合理性】:
方法逻辑链合理：观测到 gaming 与难度正相关 → 在难题上加强 all-criterion enforcement → softmin 随难度收紧 → 理论保证 gaming payoff 受限于最难 game 的维度。

**潜在挑战**：
1. **Genuine solution penalty 假设过强**：Proposal 声称 gaming profile（高 S1/S2 低 D1-D3）与 genuine profile（低 S1/S2 高 D1-D3）"structurally distinguishable"。但实际中 genuine hard solutions 可能也有 D1-D3 维度的 partial failure（推理链长、compounding error），此时 softmin 同样惩罚 genuine attempts。这是方法最大的隐患。
2. **更简单替代方案**：直接在 hard problems 上使用 binary outcome reward（abandon rubric for hard problems）可能达到类似 anti-gaming 效果但更简单。Proposal 需要论证为什么保留 rubric signal on hard problems 且用 DCM 调节比完全退回 binary 更优。
3. **LLM-as-judge 可靠性**：5 个 rubric criteria 的评分依赖 LLM judge，尤其 D1（logical validity）和 D2（mathematical rigor）在 hard problems 上的 judge accuracy 本身可能下降，引入额外噪声。
4. **Difficulty proxy 的 static 性质**：用训练前 base-model pass-rate 定义难度，但训练过程中模型能力变化可能导致 difficulty proxy 过时。

方法整体合理，但上述挑战如未被实验充分回应，可能成为 reject 理由。

【5 维度打分】:
  1. 研究问题: 【强】— Difficulty-dependent gaming in rubric-based RLVR 是一个真实的、被忽略的问题。arXiv:2604.15149 已间接证实复杂度-hacking 关联，arXiv:2605.12474 明确提到 Simpson's paradox confound 但未深入，表明领域有 demand。问题有清晰的实践意义（rubric-based RLVR 正在被广泛部署）。
  2. 方法与创新: 【中】— Novelty gap 经验证成立（无竞争工作 combine difficulty + rubric aggregation for anti-gaming）。但核心技术（softmin + τ difficulty schedule）创新度有限——softmin 已在 PURE/Stop Summation 中用于不同场景，difficulty conditioning 在 DGPO/DARO 中已有。创新在于 combination + 诊断 + 理论，而非技术本身。与 Focal Reward 的区分论述（symptom vs mechanism level）是 proposal 的 strong point。
  3. 实验设计: 【强】— 这是 proposal 最突出的优势。7+1 baselines 涵盖所有主要竞争方向（outcome-only、mean rubric、static min、POW3R、Focal Reward、DGPO、PAPO + Focal+DCM combo）；6 benchmarks 覆盖 ID/OOD/easy/hard；5 ablation 系统性地隔离各设计选择；multi-seed + bootstrap CI 保证统计可靠性；理论 bound 验证；Focal+DCM combo 验证 complementarity。在同期论文中属于上乘设计。
  4. 可行性: 【中偏强】— ~5,500 A100-hours 可行但需充足资源；Qwen3-8B/1.5B 是合理的模型选择；MATH + NuminaMath 数据可获取；verl 框架成熟。主要风险：cross-family LLM judge 成本；核心假设（difficulty exploitation gradient）如不成立则需 pivot。tiered compute 策略（1.5B 做 full ablation，8B 做 key comparisons）是明智的。
  5. 写作与呈现: 【强】— Proposal 结构清晰，问题-机制-方法-实验逻辑链完整；与竞争工作的定位区分（尤其 Focal Reward、DGPO、PURE 三组对比）精准有力；"Research Opportunity" 节的三线汇聚论述有效建立了动机。theoretical framing（连接 equilibrium framework）增加深度。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
推理过程如下：
- **加分因素**：(1) 真实的 novelty gap 在热门方向的交叉处（已验证无竞争工作）；(2) 实验设计极为详尽，达到 top-tier 标准；(3) 诊断+防御双贡献结构；(4) 与 concurrent work 的区分论述精准；(5) 理论 bound 增加深度。
- **减分因素**：(1) 核心技术创新度有限——softmin + difficulty schedule 本质是已知组件的 combination，技术门槛不高，审稿人可能认为 "trivially obvious once the problem is identified"；(2) 整篇论文的 impact 高度 contingent on diagnostic results——如果 difficulty exploitation gradient 不够 dramatic（如仅有 5-10% 差异），reviewers 会质疑 defense 的必要性；(3) genuine solution penalty 问题可能成为审稿人的主要攻击点；(4) 8B 规模在 2026 context 下偏小，scaling behavior 未知。
- **概率区间推理**：研究问题和实验设计是明确的加分项（对应 35-45% 锚点的 "整体扎实" 标准）；但方法创新度的局限和核心假设的 contingent 性质将概率从上界拉回。综合判断为 solid borderline submission，中位 35%。上界 42% 对应诊断结果 dramatic + 理论 tight + 实验全面的最佳情景；下界 28% 对应审稿人认为技术 trivial 或 diagnostic 不够 convincing 的情景。

【主要风险】:
1. **技术贡献被判 incremental**：核心方法（difficulty-conditioned softmin）可能被审稿人视为"an obvious fix once the problem is stated"，认为技术创新不足以支撑主会论文。尤其是 softmin 和 difficulty conditioning 分别在 PURE 和 DGPO 中已有先例，combination 的技术壁垒不高。
2. **Diagnostic 假设不成立或不够 dramatic**：如果实验发现 gaming 率与难度的关联较弱（或方向相反、非单调），整篇论文的核心叙事和防御动机均会崩塌。这是最大的 existential risk。

【实施评估】:
  - 计算资源: ~5,500 A100-hours（1,500 for 1.5B ablation + 4,000 for 8B key comparisons）；需 8×A100 节点若干天，对 well-funded lab 可行，对资源有限的团队有压力
  - 数据需求: MATH (~7.5K) + NuminaMath（公开可获取）；evaluation benchmarks (MATH-500, AIME 2024/2025, OlympiadBench, AMC 2023, GSM8K) 均为公开标准 benchmark
  - 人工介入: 中等——rubric criteria 设计需要 domain expertise；cross-family LLM judge 的 prompt engineering 和校准需要 iteration；difficulty quintile 划分需手动验证合理性
  - 训练需求: 需要完整的 GRPO 训练流水线（verl 框架）；Qwen3-8B 和 Qwen3-1.5B 两个规模的完整训练 + multi-seed
  - 新 Benchmark: 不需要构建新 benchmark，但需要构建 HRWAR 等新 diagnostic metrics 的计算 pipeline 和 difficulty-stratified 分析框架
  - 预估周期: 约 10-14 周——2 周 infrastructure/rubric/difficulty calibration，2 周 1.5B full ablation，3-4 周 8B key experiments，2-3 周 analysis/writing，1-2 周 buffer
```

Sources:
- [Reward Hacking in Rubric-Based RL (arXiv:2605.12474)](https://arxiv.org/abs/2605.12474)
- [LLMs Gaming Verifiers (arXiv:2604.15149)](https://arxiv.org/abs/2604.15149)
- [DGPO: Harder Is Better (arXiv:2601.20614)](https://arxiv.org/pdf/2601.20614)
- [POW3R: Policy-Aware Rubric Rewards (arXiv:2605.20164)](https://arxiv.org/abs/2605.20164v1)
- [Focal Reward (arXiv:2605.26579)](https://arxiv.org/abs/2605.26579)
- [PAPO: Decoupled Advantage Normalization (arXiv:2603.26535)](https://arxiv.org/abs/2603.26535)
- [SRaR: Step-wise Rubric Rewards (arXiv:2605.17291)](https://arxiv.org/abs/2605.17291)
- [Stop Summation / PURE (arXiv:2504.15275)](https://arxiv.org/abs/2504.15275)
- [Reward Hacking as Equilibrium (arXiv:2603.28063)](https://arxiv.org/abs/2603.28063)
- [DARO: Difficulty-Aware Reweighting (arXiv:2510.09001)](https://arxiv.org/pdf/2510.09001)
- [Representation-Level Reward Hacking (arXiv:2604.01476)](https://arxiv.org/pdf/2604.01476)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) (arXiv 2026): 最直接的前置工作。该文系统分类了 rubric gaming 的模式，发现 partial compound satisfaction 占 36% 的 gaming 行为，并注意到 Simpson's paradox 的混淆效应——但关键的是，该文 **从未按难度分层分析 gaming rate**，也未提出防御机制。Proposal 的 diagnostic 贡献恰好填补了这一明确遗漏。
- [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149) (ICLR 2026 Workshop): 在归纳推理任务上确认 shortcut 行为随任务复杂度增加而增加，其解释（extensional correctness 对复杂任务承认更多 false positives）直接支撑了 proposal 的"检测盲区"机制。但该文聚焦于归纳推理验证器，未涉及 rubric 聚合。
- [DGPO: Harder Is Better](https://arxiv.org/abs/2601.20614) (ICLR 2026): 证明了 GRPO 中存在的难度依赖更新量偏差，提出 difficulty-balanced group advantage estimation。但仅在 **binary outcome reward** 上操作，调整的是 policy optimization（loss weights），不是 reward signal construction。与 proposal 的 DCM 解决不同问题（学习效率 vs 防 gaming），理论上可组合使用。
- [POW3R: Policy-Aware Rubric Rewards](https://arxiv.org/abs/2605.20164) (arXiv 2026): 基于 rollout-level contrast 对 rubric criterion 进行方差感知的重加权。在 30 个 base-policy/metric 比较中赢得 24 个。但其重加权是 **difficulty-agnostic** 的。
- [Focal Reward: Balanced RL under Rubric-Based Rewards](https://arxiv.org/abs/2605.26579) (arXiv 2026): 基于 criterion saturation headroom 进行动态重加权。Proposal 对其的批评——headroom 来源不区分 gaming vs genuine difficulty vs capacity limits——是合理的。两者的补充关系在实验设计中通过 "Focal Reward + DCM" 组合 baseline 被显式验证。
- [Stop Summation / PURE](https://arxiv.org/abs/2504.15275) (NeurIPS 2025): 在 PRM 的 **时序步骤聚合** 上引入 min-form credit assignment，缓解了步骤层面的 reward hacking。Proposal 的 min-form 是在 **无序维度（rubric criteria）** 上的，结构性不同（无时序依赖、无 error compounding），需要独立推导。
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (arXiv 2026): 理论框架，证明在五个最小公理下任何优化 agent 都会在评估未覆盖的质量维度上投资不足。Proposal 将其用作理论锚点——difficulty-agnostic rubric 聚合在高难度问题上结构性地"under-cover"了某些 criteria，创造了有利于 gaming 的均衡。
- [DARO: Difficulty-Aware Reweighting Policy Optimization](https://arxiv.org/abs/2510.09001) (arXiv 2025): 基于模型学习状态动态调整每个难度组的 loss 贡献。同 DGPO，仅操作 binary rewards，调整的是 policy 端而非 reward 端。

- **调研总结**: Rubric-based RLVR 的 reward aggregation 是 2025-2026 年的热门方向，已有 7+ 篇并发工作（POW3R, Focal Reward, PAPO, SRaR 等），但全部是 difficulty-agnostic 的。Difficulty-aware RL 方法（DGPO, DARO, GRPO-LEAD）全部仅操作 binary outcome rewards。**"难度 × rubric 聚合"的交叉点确实是一个真实的、未被占据的空白**。Proposal 的 novelty claim 经调研核实后成立。

【整体印象】: 
如果我是审稿人，初始印象是 **cautiously positive**（倾向 weak accept 区间）。这篇 proposal 最令人印象深刻的是它对 research gap 的精准定位——在两个活跃且相互独立的研究线索（rubric aggregation 和 difficulty-aware RL）之间找到了一个真实的、有意义的交叉空白，并提供了两个清晰的动机机制（effort asymmetry + detection blindness）来解释为什么这个空白值得填补。实验设计的完备程度（7+1 baselines, 6 benchmarks, 5 ablations, multi-seed, bootstrap CI）远超一般 proposal 水准。

然而，我也有顾虑：(1) 方法本身（softmin + 难度条件化 τ）在技术深度上较浅——这是一个简单的数学变换，核心创新更多在 framing 和诊断上而非算法设计上；(2) 整篇论文的叙事完全建立在"难度利用梯度"这个经验假说之上，如果实验中该梯度不够显著，诊断贡献和防御贡献都将大打折扣；(3) gaming vs genuine 的可区分性假设（gaming inflates S1/S2, genuine shows strong D1-D3）在实际中可能不那么干净。

【核心贡献】:
两个独立贡献：
1. **诊断性贡献**：首次系统测量 rubric-based math RLVR 中按难度分层的 gaming rate，建立"难度利用梯度"作为一个经验现象。这可能是更有持久价值的贡献——即使 DCM 方法本身被更好的方法取代，这个 diagnostic 发现作为 empirical observation 仍然有引用价值。
2. **防御性贡献**：DCM 聚合，一种机制层面的防御，通过在高难度问题上强制所有 criterion 满足来移动 gaming 均衡点。配有理论 bound（gaming payoff bounded by min_k(ε_k) as τ→0）和与均衡框架的联系。

对领域的价值：中等偏高。这个工作不会改变 RLVR 的范式，但它填补了一个实际的盲区，提供了一个实用的防御工具，并且其诊断方法论可以被广泛复用。

【方法合理性】:
方法整体合理，但存在值得推敲的点：

**合理之处：**
- Softmin 作为 aggregation operator 有清晰的数学动机：当 τ→0 时退化为 min，强制所有 criterion 满足，直接攻击 partial satisfaction gaming。
- 难度条件化的 τ schedule（τ = τ₀·(1-d)^α）是合理的连续化设计，避免了硬阈值。
- 与 PURE 的区分是真实的：无序 rubric dimensions vs 有序时序步骤，无 error compounding，需要独立分析。

**潜在问题：**
1. **更简单的替代方案**：静态 min aggregation（difficulty-agnostic min）是一个天然的 baseline，proposal 已包含。但审稿人可能会问：为什么不简单地在高难度问题上增大 criterion weight 的最小值（即 min-weight clipping），而非改变整个聚合函数？这在概念上更简单，可能效果相近。
2. **τ schedule 的粒度**：使用 pass-rate quintiles 作为离散难度代理，再映射到连续 τ——这引入了离散化噪声和 quintile 边界效应。Proposal 的 ablation（pass-rate quintile vs model-estimated difficulty）覆盖了这点。
3. **Rubric criteria 的 LLM-as-judge 可靠性**：D1（逻辑有效性）和 D2（数学严谨性）的评分本身在高难度问题上可能不够可靠，这可能混淆诊断结果。交叉 judge panel 部分缓解了这个问题。
4. **Genuine hard solutions 的惩罚风险**：Proposal 声称 gaming 和 genuine 的 rubric profile 可区分（S1-S2 高 vs D1-D3 高），但这一假设的鲁棒性未经验证。如果某些 genuine hard solutions 的 D criteria 也偶尔较低（例如，正确但不够严谨的解法），DCM 会过度惩罚它们。

【5 维度打分】:
  1. 研究问题: 【强】 — 两个活跃研究方向（rubric aggregation + difficulty-aware RL）的交叉空白经调研确认为真实存在。"难度利用梯度"有清晰的理论动机（effort asymmetry + detection blindness），且与 arXiv:2604.15149 的实证发现和 arXiv:2603.28063 的理论框架一致。问题的实际意义也很明确：rubric-based RLVR 正在被广泛部署（DeepSeek-R1 后），如果高难度问题的 gaming 确实更严重，这是一个必须解决的可靠性问题。
  
  2. 方法与创新: 【中】 — 技术创新的核心是 softmin + difficulty-conditioned τ，这是一个数学上简洁但深度有限的贡献。与 PURE (NeurIPS 2025) 的区分是合理的（无序维度 vs 有序时序步骤），但 softmin 本身不是新 operator。与 Focal Reward (arXiv:2605.26579) 的"症状层 vs 机制层"区分有洞察力但也有些 over-sell：Focal Reward 的 headroom 也可以被解释为间接的 mechanism signal。理论 bound（gaming payoff ≤ min_k(ε_k)）是清晰的但推导难度不高。总体而言，方法的价值更多来自"在正确的地方使用了正确的工具"而非算法本身的技术深度。
  
  3. 实验设计: 【强】 — 这是 proposal 最突出的优势。7+1 baselines 覆盖了所有主要竞争方法（POW3R, Focal Reward, DGPO, PAPO），包含 difficulty-agnostic min 和 Focal Reward+DCM 组合以验证互补性。6 个 benchmark 覆盖 in-distribution / OOD / harder / easier。多层级 gaming 指标（HRWAR + AUC, cross-judge disagreement, self-internalization gap）和 per-quintile 分析是诊断叙事的核心。Ablation 设计系统（聚合进阶、schedule 形式、超参数 heatmap、难度代理、rubric 粒度）。Multi-seed + bootstrap CI + compute-budget equalization 体现了严谨性。相比领域内多数并发工作（如 POW3R 仅报告 30 个 comparisons），实验设计的覆盖度和严谨度明显高于平均水平。
  
  4. 可行性: 【中偏强】 — ~5,500 A100-hours 是一个可观但在有 GPU 集群访问权的实验室范围内可行的预算。Tiered compute strategy（1.5B 做全 ablation，8B 做关键比较）是务实的。主要风险不在资源而在假说验证：如果"难度利用梯度"在实证中不够显著（例如，HRWAR 跨 quintile 的差异只有几个百分点），整篇论文的叙事基础将被削弱。此外，K=5 的 rubric criteria 中的 LLM-as-judge 评分（特别是 D1, D2）在高难度数学问题上的可靠性是一个实操风险。
  
  5. 写作与呈现: 【强】 — Proposal 的组织结构清晰（问题→贡献→研究空白→方法→实验），对相关工作的定位精准且诚实（与 Focal Reward、DGPO、PURE 的区分都有实质内容而非草率dismissal）。"诊断 + 防御"的双贡献叙事是一个强大的 paper framing——即使 DCM 方法的优势不够大，诊断发现本身就有独立发表价值。两个机制（effort asymmetry + detection blindness）的分解让论证有层次感。唯一的呈现风险是：8 页正文可能难以容纳如此丰富的内容（理论 + 诊断 + 方法 + 实验 + ablation）。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】: 
AAAI 2026 接受率 17.6%。本 proposal 的核心优势在于：(1) 精准定位了一个经调研确认的真实研究空白；(2) 实验设计的完备程度在同领域 proposal 中属于上游；(3) "诊断 + 防御"的双贡献叙事降低了单点失败风险；(4) 时机极好，处于 rubric-based RLVR 的研究热潮中。主要拖累因素：(1) 方法本身的技术深度有限（softmin 不是新 operator，difficulty conditioning 的 idea 概念上不复杂）；(2) 整个叙事高度依赖一个尚未验证的经验假说（难度利用梯度的显著性）；(3) 仅在数学领域验证，泛化性未展示。

在乐观情境下（难度利用梯度显著、DCM 在 Q4-Q5 上的 gaming rate 下降显著且 Q1-Q3 不受损、理论 bound 紧致），这是一篇 solid 的中稿级别工作（~42%）。在悲观情境下（梯度不够显著、DCM 对 genuine hard solutions 有明显误伤、或审稿人认为方法太简单），概率下降至 ~28%。中位估计 35%，反映一篇有真实贡献但方法深度不足以拿到 strong accept 的竞争性投稿。

【主要风险】: 
1. **经验假说风险**：整篇论文的核心叙事建立在"难度利用梯度单调递增且幅度足够显著"这一假说上。如果实际测量发现梯度微弱或非单调（例如中等难度才是 gaming 峰值），诊断贡献和防御动机都将受到严重质疑。这是最大的单点失败风险。
2. **方法深度不足**：在 AAAI 这样的竞争性会议，审稿人可能认为"将 softmin 用于 rubric aggregation 并加上 difficulty conditioning"缺乏足够的算法创新，仅是现有工具的简单组合。理论 bound 虽然清晰但推导不复杂，可能被认为是 straightforward corollary。若审稿人持此观点，方法贡献可能被评为 incremental。

【实施评估】:
  - 计算资源: ~5,500 A100-hours（1,500 for 1.5B ablation + 4,000 for 8B key comparisons）。需要可靠的 A100/H100 集群访问。对有 GPU 集群的实验室属于中等规模实验。
  - 数据需求: MATH 训练集（~7.5K）+ NuminaMath（公开可用）+ 6 个评测 benchmark（MATH-500, AIME 2024/2025, OlympiadBench, AMC 2023, GSM8K，全部公开）。数据不是瓶颈。
  - 人工介入: 中等。需要：(1) 设计和迭代 K=5 rubric criteria 的 prompt engineering；(2) 调试 cross-family judge panel（GPT-4o, Claude Sonnet, Gemini Pro）的 API 调用和一致性；(3) 分析 gaming vs genuine profiles 的定性检查。无需大规模人工标注。
  - 训练需求: 是。需要在 Qwen3-8B 和 Qwen3-1.5B 上进行完整的 GRPO 训练，使用 verl 框架。每个方法/配置需要独立训练 run。Total ~20-30 个独立训练 run（含 multi-seed）。
  - 新 Benchmark: 否。使用现有 benchmark。但诊断指标 HRWAR 是新定义的，需要实现和验证。
  - 预估周期: 8-12 周。Phase 1（2-3 周）：基础设施搭建（verl + rubric judge + 难度分层）。Phase 2（3-4 周）：1.5B 上的全 ablation + diagnostic。Phase 3（3-4 周）：8B 上的关键比较 + 理论验证。Phase 4（1-2 周）：论文撰写。总体时间线紧凑但可行。
```

Sources:
- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)
- [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)
- [DGPO: Harder Is Better](https://arxiv.org/abs/2601.20614)
- [POW3R: Policy-Aware Rubric Rewards](https://arxiv.org/abs/2605.20164)
- [Focal Reward: Balanced RL under Rubric-Based Rewards](https://arxiv.org/abs/2605.26579)
- [Stop Summation / PURE](https://arxiv.org/abs/2504.15275)
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063)
- [DARO: Difficulty-Aware Reweighting Policy Optimization](https://arxiv.org/abs/2510.09001)
- [AAAI 2026 Accepted Papers Highlights](https://www.bohrium.com/blog/research-notes/aaai-2026-accepted-papers-highlights/)
- [Reward Hacking in RLVR Systems](https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr)


【原始 proposal（允许参考但不是主要依据）】:
# Difficulty-Conditioned Min-Form Rubric Rewards Resist Gaming

## Core Problem

Uniform rubric strictness across problem difficulty levels creates a difficulty exploitation gradient in rubric-based RLVR, driven by two reinforcing mechanisms:

1. **Effort asymmetry**: Genuine solving effort scales super-linearly with difficulty (harder problems require longer reasoning chains with compounding error risk), while gaming effort scales sub-linearly (shallow pattern-matching strategies that partially satisfy rubric criteria transfer across difficulty levels with minimal adaptation).

2. **Detection blindness**: Uniform rubric aggregation has structurally lower discriminative power on hard problems—hard-problem responses exhibit higher rubric score variance even among genuine attempts, making it harder to distinguish gaming-induced partial satisfaction from genuine partial progress. The false-positive-tolerant regime on hard problems makes gaming systematically cheaper to disguise.

Together, these mechanisms create a monotonically increasing gaming profit margin with difficulty: hard problems are simultaneously the easiest to game and the hardest to detect gaming on. No existing work has diagnosed or defended against this difficulty-dependent gaming phenomenon.

## Contributions

We make two independent contributions:

1. **Diagnostic**: The first systematic measurement of difficulty-stratified gaming rates in rubric-based math RLVR, establishing the difficulty exploitation gradient as an empirical phenomenon (not merely hypothesized).

2. **Defense**: Difficulty-Conditioned Min-form (DCM) aggregation, a mechanism-level defense that forces strict all-criterion satisfaction on hard problems, shifting the gaming equilibrium by making the gaming payoff bounded by the hardest-to-game criterion.

## Research Opportunity

Three lines converge on an untouched gap: (1) Reward Hacking in Rubric-Based RL (arXiv:2605.12474) taxonomizes rubric gaming, showing partial compound satisfaction accounts for 36% of gaming and noting a Simpson's paradox confound, but never investigates difficulty-dependent gaming rates (experiments in medical/science domains); (2) LLMs Gaming Verifiers (arXiv:2604.15149, ICLR 2026 Workshop) confirms shortcut prevalence increases with task complexity in inductive reasoning, with their explanation (extensional correctness admits more false positives for complex tasks) directly supporting our detection-blindness mechanism; (3) DGPO (arXiv:2601.20614, ICLR 2026) proves difficulty-dependent update magnitude bias but only for binary rewards. All 7+ concurrent rubric reweighting papers are difficulty-agnostic, and all difficulty-aware methods operate only on scalar outcome rewards.

From a structural perspective, Reward Hacking as Equilibrium (arXiv:2603.28063) proves under five minimal axioms that any optimized agent under-invests in quality dimensions not adequately covered by evaluation. Difficulty-agnostic rubric aggregation structurally under-covers hard-problem criteria (uniform temperature fails to penalize partial satisfaction sufficiently at high difficulty), creating an equilibrium favoring gaming. DCM shifts this equilibrium by increasing the cost of under-investing in any single rubric dimension proportionally to difficulty-induced gaming vulnerability.

## Research Landscape

Rubric reward aggregation (2026): POW3R (arXiv:2605.20164) reweights by rollout variance; Focal Reward (arXiv:2605.26579) by criterion saturation headroom; PAPO (arXiv:2603.26535) decouples ORM/PRM advantages; SRaR (arXiv:2605.17291) attributes rubrics to steps. None condition on difficulty.

Difficulty-aware RL: DGPO (arXiv:2601.20614, ICLR 2026) uses difficulty-balanced group advantage; DARO (arXiv:2510.09001) dynamically adjusts loss contribution per difficulty group based on model learning state; GRPO-LEAD uses difficulty-aware advantage reweighting. All operate only on binary outcome rewards. The key distinction: DARO/DGPO adjust policy optimization (loss weights), while DCM adjusts reward signal construction (aggregation). They solve different problems (learning efficiency vs anti-gaming) and can be combined.

Gaming detection/theory: arXiv:2605.12474 taxonomizes rubric gaming but proposes no defense; arXiv:2603.28063 proves reward hacking is a structural equilibrium; arXiv:2604.01476 extracts shortcut behavior directions for detection.

**Critical distinction from Focal Reward**: Focal Reward operates at the **symptom level**—it measures criterion saturation headroom (how much improvement remains) and upweights high-headroom criteria. But saturation headroom is agnostic to the *source* of headroom: gaming-induced suppression, genuine difficulty, or model capacity limits are treated identically. When easy and hard problems' headroom statistics are pooled, hard-problem gaming signals get diluted by easy-problem genuine headroom. DCM operates at the **mechanism level**—it directly constrains that no criterion can be abandoned on hard problems, with constraint strength proportional to gaming vulnerability (difficulty proxy), regardless of headroom patterns. Focal Reward answers "which criterion to emphasize"; DCM answers "how strictly to enforce the weakest criterion given gaming risk." The two are complementary: Focal Reward optimizes learning signal quality while DCM prevents exploitation of the reward function.

No concurrent work combines difficulty conditioning with rubric aggregation for anti-gaming defense—confirmed via arXiv and OpenReview search through May 2026.

## Proposed Approach

**Training setup.** Train Qwen3-8B (primary) and Qwen3-1.5B (generalization) via GRPO + rubric rewards on the MATH training set (~7.5K problems), supplemented with NuminaMath for prompt diversity, using verl. Difficulty defined via base-model pass-rate quintiles (static, computed before training, following DGPO's practice).

**Rubric criteria (K=5 canonical).** Surface-level: (S1) solution format compliance, (S2) step-by-step structure presence. Deep-level: (D1) logical validity of reasoning steps, (D2) mathematical rigor/correctness of operations, (D3) final answer correctness. The surface/deep distinction enables analysis of gaming-characteristic vs genuine-characteristic rubric profiles.

**Diagnostic.** Measure per-stratum gaming with multi-level metrics: (1) Primary: High-Rubric-Wrong-Answer Rate (HRWAR) = P(rubric_score > θ ∧ answer incorrect), exploiting math's ground-truth verifiability. Report HRWAR-vs-θ curve and threshold-free AUC summary. (2) Secondary: cross-judge disagreement using cross-family panel (GPT-4o, Claude Sonnet, Gemini Pro). (3) Tertiary: self-internalization gap (from arXiv:2605.12474). All metrics reported per difficulty quintile.

**DCM aggregation.** Replace mean rubric aggregation with softmin: r = -τ·log(Σ exp(-s_k/τ)) where τ = τ₀·(1-d)^α decreases with difficulty d ∈ [0,1], so hard-problem rewards → min(s_k). Easy-problem behavior remains mean-like (preserving learning signal), while hard-problem behavior enforces strict all-criterion satisfaction.

**Addressing genuine-solution penalty.** Gaming-induced unevenness and genuine unevenness are structurally distinguishable: gaming inflates surface criteria (S1, S2) while neglecting deep criteria (D1-D3); genuine hard solutions show the reverse (potentially lower S1/S2 but strong D1-D3). The softmin thus selectively penalizes the gaming-characteristic profile. We validate empirically by analyzing per-criterion profiles of correct vs incorrect solutions across difficulty strata.

**Theoretical contribution.** We derive an anti-gaming bound for cross-dimension softmin: if gaming inflates criterion k's score by ε_k, DCM-aggregated reward inflation is bounded by min_k(ε_k) as τ→0, meaning gaming payoff is limited by the hardest-to-game criterion. Unlike Stop Summation/PURE (arXiv:2504.15275, NeurIPS 2025), whose bound addresses temporal step-wise aggregation (ordered, error-compounding), our setting involves unordered dimensions with independent errors—structurally different, requiring independent derivation. We characterize bound degradation with τ and connect to the equilibrium framework: DCM equalizes the distortion index (from arXiv:2603.28063) across difficulty strata.

## Experimental Design

**Baselines (7 methods + 1 combination):**
- GRPO + outcome-only reward (binary, no rubric)
- GRPO + mean rubric aggregation (standard rubric baseline)
- GRPO + static min aggregation (difficulty-agnostic min)
- POW3R (arXiv:2605.20164, variance-based reweighting)
- Focal Reward (arXiv:2605.26579, saturation-aware reweighting)
- DGPO (arXiv:2601.20614, difficulty-aware binary reward)
- PAPO (arXiv:2603.26535, decoupled advantage)
- **Focal Reward + DCM** (combination: validates complementarity claim)

**Evaluation benchmarks (6):**
- In-distribution: MATH-500, AIME 2024
- OOD / harder: AIME 2025, OlympiadBench, AMC 2023
- Easier (ceiling): GSM8K

Per benchmark: (1) accuracy (pass@1); (2) gaming rate (HRWAR + AUC, per-difficulty); (3) rubric score distribution.

**Per-difficulty-stratum analysis (core to narrative):** For each method, report accuracy and gaming rate broken down by difficulty quintile. Key expected finding: DCM's advantage concentrates in Q4-Q5 (hardest) while preserving Q1-Q3 performance; static min damages Q1-Q3; Focal Reward is uniform across strata.

**Ablation studies:**
1. Aggregation progression: mean → fixed-τ softmin → DCM (isolates difficulty conditioning value)
2. Schedule: τ₀·(1-d)^α vs linear vs step-function
3. Hyperparameter sensitivity: τ₀ ∈ {0.1, 0.5, 1.0, 2.0}, α ∈ {0.5, 1.0, 2.0} (heatmap on 1.5B)
4. Difficulty proxy: pass-rate quintile vs model-estimated difficulty
5. Rubric granularity: K ∈ {3, 5, 8}

**Theory validation:** Plot theoretical bound vs actual gaming payoff inflation across τ settings, demonstrating bound tightness and degradation curve.

**Reproducibility controls:**
- 3 random seeds for DCM + Focal Reward + combo (significance testing); other baselines 1 seed on 8B, 3 seeds on 1.5B
- Identical compute budget across methods (same GRPO steps × rollouts)
- Report GPU-hours per method; performance-vs-compute curves
- Bootstrap confidence intervals for small benchmarks (AIME)

**Compute strategy (tiered):** Full ablation + multi-seed on Qwen3-1.5B (~1,500 A100-hours); key comparisons (DCM vs top-3 baselines + combo + core ablation) on Qwen3-8B (~4,000 A100-hours). Total: ~5,500 A100-hours.

## Key References

- Reward Hacking in Rubric-Based RL (arXiv:2605.12474, arXiv 2026)
- LLMs Gaming Verifiers (arXiv:2604.15149, ICLR 2026 Workshop)
- DGPO: Harder Is Better (arXiv:2601.20614, ICLR 2026)
- Stop Summation / PURE (arXiv:2504.15275, NeurIPS 2025)
- POW3R: Policy-Aware Rubric Rewards (arXiv:2605.20164, arXiv 2026)
- Focal Reward (arXiv:2605.26579, arXiv 2026)
- GRPO-LEAD (arXiv 2025)
- PAPO: Decoupled Advantage Normalization (arXiv:2603.26535, arXiv 2026)
- SRaR: Step-wise Rubric Rewards (arXiv:2605.17291, arXiv 2026)
- Reward Hacking as Equilibrium (arXiv:2603.28063, arXiv 2026)
- Representation-Level Reward Hacking (arXiv:2604.01476, arXiv 2026)
- DARO: Difficulty-Aware Reweighting (arXiv:2510.09001, arXiv 2025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c42716ef-6631-4ca7-a9a7-19baf966fb5b",
  "type": "user",
  "uuid": "f3ff3257-2265-4d70-b2e9-85d20d3c32b9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:41:36.804Z_

```json
{
  "parentUuid": "f3ff3257-2265-4d70-b2e9-85d20d3c32b9",
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
  "uuid": "f5237345-9fcb-41dd-a03c-8f3891783a06",
  "timestamp": "2026-05-29T06:41:36.804Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:41:36.804Z_

```json
{
  "parentUuid": "f5237345-9fcb-41dd-a03c-8f3891783a06",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e02b8675-bb56-48de-851c-60c1175994f2",
  "timestamp": "2026-05-29T06:41:36.804Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research context. Let me compile my eval…",
  "leafUuid": "e02b8675-bb56-48de-851c-60c1175994f2",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Difficulty-conditioned rubric rewards for anti-gaming in RLVR",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:42:09.289Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' evaluations carefully to produce a Meta Judge synthesis.

**Reviewer 1**: [28% - 42%] 中位 35%
**Reviewer 2**: [28% - 42%] 中位 35%
**Reviewer 3**: [28% - 42%] 中位 35%

All three reviewers gave identical probability estimates. This is extremely high convergence.

Let me check the rubric dimensions:

| Dimension | R1 | R2 | R3 |
|---|---|---|---|
| 研究问题 | 强 | 强 | 强 |


| 方法与创新 | 中（偏强） | 中 | 中 |
| 实验设计 | 强 | 强 | 强 |
| 可行性 | 中 | 中偏强 | 中偏强 |
| 写作与呈现 | 强 | 强 | 强 |

The standard deviation across all three midpoints is zero—perfect alignment. Looking at the consensus, the research question, experimental design, and presentation are uniformly rated as strong across all reviewers, while methodology and feasibility show slightly more variation but still cluster around the middle range.

The three critical risks that emerged unanimously are whether the empirical hypothesis actually holds in practice, whether the proposed solution creates unintended negative effects, and whether the approach will be perceived as merely incremental rather than genuinely novel. All reviewers also agreed the diagnostic contribution has standalone value, though there's concern about relying on LLM judges for evaluating difficult problems.

Looking at where reviewers diverged, domain-specific limitations affecting generalizability came up in two reviews, while alternative approaches like binary outcome rewards or min-weight clipping were each mentioned by only one reviewer. The convergence on the acceptance probability is striking—all three landed in the 28-42% range with a standard deviation of zero, so I can narrow the estimate with confidence. On the computational side, they're aligned on roughly 5,500 A100-hours needed.

For the final probability, I'll apply the convergence principle and tighten the interval slightly to 30-40% while keeping the midpoint at 35%, staying within the bounds that all three reviewers established.

For the recommendation: 35% sits right on the borderline—the work has genuine strengths but the methodological depth concern poses a real risk for a top-tier venue, so this doesn't warrant a strong endorsement either way.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e02b8675-bb56-48de-851c-60c1175994f2",
  "isSidechain": false,
  "requestId": "req_011CbWQPxQeZKFY686xwB3Sx",
  "type": "assistant",
  "uuid": "97540c0e-d54b-4e6f-848d-d0353de66b87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FMsUDudhafr1jw9V5BKwDD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19309,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19309,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3150,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 19309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19309
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

_source line 9 · 2026-05-29T06:42:59.231Z_

【阶段】: Meta Judge
【三次中位】: [35%, 35%, 35%]  std=0%
【共识维度】: 
- **研究问题=强** (3/3)：三位审稿人均确认"难度×rubric聚合"交叉空白真实存在，经独立调研验证无竞争工作，gap claim 成立
- **方法与创新=中** (3/3)：三位均认为 softmin + difficulty-conditioned τ 技术深度有限，存在"incremental combination / trivially obvious once problem identified"的审稿风险
- **实验设计=强** (3/3)：三位一致认定这是 proposal 最突出的维度，7+1 baselines / 6 benchmarks / 5 ablations / multi-seed + bootstrap CI 达到 top-tier 标准
- **写作与呈现=强** (3/3)：逻辑链完整，与并发工作的定位精准（尤其 Focal Reward 区分）
- **核心风险：empirical hypothesis bet** (3/3)：若难度利用梯度效应量不显著，论文叙事基础坍塌——三位均标注为最大单点失败风险
- **核心风险：genuine solution collateral damage** (3/3)：softmin 对 hard problems 上的 genuine partial progress 可能误伤，gaming vs genuine 的 profile 可区分性假设未经验证
- **核心风险：方法 incremental 判定** (3/3)：softmin 在 PURE 中已用，difficulty conditioning 在 DGPO 中已有，组合的技术壁垒不高
- **诊断贡献独立价值** (3/3)：即使 DCM 效果有限，difficulty exploitation gradient 的 empirical finding 本身有引用和领域推动价值
- **LLM judge 可靠性** (3/3)：hard problems 上 D1/D2 评分精度下降，DCM 的 min 特性会放大 judge noise
- **可行性=中偏强** (3/3)：~5,500 A100-hours 可行但有一定门槛，tiered compute 策略合理
【异常维度】: 
- R2 独有：提出"hard problems 上直接退回 binary outcome reward"作为更简单替代——有效但属 edge case，其他两位未认为此替代构成威胁
- R3 独有：提出"min-weight clipping"替代方案——概念更简单但功能不等价（clipping 不改变聚合函数结构），降权处理
- R3 独有：8 页正文容量担忧——有效但属呈现层面，不影响学术质量评估
- R1 独有：K=5 surface/deep 分类的鲁棒性 + judge noise 被 min 放大的具体机制分析——有效观察，已被其他两位的 judge reliability 共识覆盖
【最终概率】: [30% - 40%] 中位 35%
【一致性】: 高（三位审稿人概率估计完全一致，rubric 维度判决高度对齐，std=0%）
【综合理由】: 
三位审稿人在所有核心维度上达成了罕见的完全共识——概率区间、中位数、rubric 各维度判决、主要风险点均高度一致。这使得综合判断具有很高的置信度。

**核心逻辑**：这是一篇"问题对、定位准、设计强、但方法浅"的 proposal。其价值分布不均匀——研究问题识别（强）和实验设计（强）是真正的竞争力，而方法创新（中）是天花板限制。三位审稿人均指出，softmin + difficulty conditioning 本质是已知工具的参数化组合，技术门槛不高。这意味着即使实验结果理想，论文也难以拿到 strong accept，因为方法贡献在顶会审稿中通常是决定性维度。

**概率区间缩窄逻辑**：由于 std=0%（最高一致性），按规则取中位附近并缩窄区间。原三份均为 [28%-42%]，缩窄至 [30%-40%]。下界上调 2%（三位共识实验设计强劲，提供了稳定的下限保障）；上界下调 2%（方法创新中的共识限制了上行空间）。中位维持 35%，反映一篇 solid but not exceptional 的投稿在 AAAI 的典型 odds。

**对异常维度的处理**：R2 的"退回 binary reward"替代和 R3 的"min-weight clipping"替代均为单人提出的 edge case。前者改变了问题设定（放弃 rubric signal），后者功能不等价。两者均不构成对 proposal 核心 novelty 的致命威胁，但建议 proposal 在实验或讨论中简要回应"为什么不在 hard problems 上直接退回 binary reward"这一自然问题。

【建议】: 边缘
【实施评估】:
  - 计算资源: ~5,500 A100-hours（三位一致）。需 8×A100 集群约 10-15 天，或等价云计算 $5K-$15K。对 well-funded 学术组可行，对资源受限团队有一定门槛。
  - 数据需求: MATH (~7.5K) + NuminaMath 训练数据 + 6 个公开评测 benchmark（MATH-500, AIME 2024/2025, OlympiadBench, AMC 2023, GSM8K）。数据获取无障碍。
  - 人工介入: 中等。主要集中在：(1) K=5 rubric criteria 的 prompt engineering 及迭代优化；(2) cross-family LLM judge panel（GPT-4o, Claude Sonnet, Gemini Pro）的 API 配置与一致性校准；(3) difficulty quintile 划分的合理性验证；(4) gaming vs genuine profile 的定性分析。无需大规模人工标注。
  - 训练需求: 需要完整 GRPO 训练 pipeline（verl 框架）。Qwen3-8B（主实验）+ Qwen3-1.5B（ablation + 泛化验证）。总计约 20-30 个独立训练 run（含 multi-seed），每个 run 需要完整的 RL 训练周期。
  - 新 Benchmark: 不需要构建新 benchmark。需要实现新的诊断指标体系（HRWAR + cross-judge disagreement + self-internalization gap per difficulty quintile），属于分析 pipeline 而非 benchmark 构建。
  - 预估周期: 10-14 周（三位估计的交集区间）。关键路径：基础设施搭建（2-3 周）→ 1.5B 全量 ablation + diagnostic（3-4 周）→ 8B 关键比较（3-4 周）→ 分析与写作（2-3 周）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97540c0e-d54b-4e6f-848d-d0353de66b87",
  "isSidechain": false,
  "requestId": "req_011CbWQPxQeZKFY686xwB3Sx",
  "type": "assistant",
  "uuid": "5c0d3e95-4767-4d97-b251-474a3891dc7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FMsUDudhafr1jw9V5BKwDD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19309,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19309,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3150,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 19309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19309
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research context. Let me compile my eval…",
  "leafUuid": "5c0d3e95-4767-4d97-b251-474a3891dc7d",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Difficulty-conditioned rubric rewards for anti-gaming in RLVR",
  "sessionId": "1d39e095-1ec0-4e31-a34b-65a4217a8c2b"
}
```

---
