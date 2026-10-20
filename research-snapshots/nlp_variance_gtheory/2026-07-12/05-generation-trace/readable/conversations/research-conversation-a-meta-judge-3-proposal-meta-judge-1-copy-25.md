# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/11600e8d-eafb-49e2-9de6-aebb2f3dd81a.jsonl`
- **Structured JSON:** [`2ffeedc06a1b824658c2.json`](../../sessions/2f/2ffeedc06a1b824658c2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:39:34.144Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:39:34.144Z",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a thorough assessment. Let me compile the evaluation.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [SOS-Bench] (arXiv:2409.15268): 直接动机论文，证明 style features 在 LLM judge 打分中 dominate substance。CSD 以此为核心 motivation 之一，且将其作为评测 benchmark。\n- [CASSE] (arXiv:2601.10809): 识别 12 种 cross-correlated style features，核心发现 style features 高度纠缠。CSD 的 α legitimacy-aware correction 直接回应 CASSE 关于 \"style removal has side effects\" 的发现。\n- [Preference Leakage] (ICLR 2026, arXiv:2502.01534): 证明 judge style bias 向下游 RLHF/DPO 传播。为 CSD 提供了 broader impact 论证——debiasing judges 有 cascading benefits。已被 ICLR 2026 接收，验证了该问题的重要性。\n- [RATE] (ICML 2025, arXiv:2410.11348): CSD 最直接的技术竞争者。RATE 用 double-rewrite protocol 处理 imperfect counterfactuals，但需 ~25x inference cost 且不产生 corrected scores。CSD 用 DML 替代 double-rewrite，降至 7x 且产生可用的 debiased scores。RATE 已发表在 ICML 2025。\n- [LC-AlpacaEval] (ICLR 2025, arXiv:2404.04475): 最广泛使用的 observational debiasing 方法，但仅处理 length 单一维度，且无法区分 causal vs. spurious associations。CSD 在多维度+因果识别上形成差异化。\n- [Post-hoc Reward Calibration] (ICLR 2025, arXiv:2409.17407): 扩展 locally weighted regression 至 33 reward models，但同样是 observational，受 confounding 限制。\n- [FairJudge] (arXiv:2602.06625): Training-based debiasing (SFT→DPO→GRPO)，需 white-box access，无法用于 proprietary models。CSD 在 black-box 适用性上有明确优势。\n- [Soumik] (arXiv:2604.23178): 系统评估 9 种 prompt-based debiasing 策略，best strategy 仅 +7-11pp improvement。作为 prompt engineering baseline 被 CSD 纳入对比。\n- [RBD] (NeurIPS 2025, arXiv:2505.17100): Reasoning-based bias detection，prompt-level 操作，不 disentangle 具体 style dimensions。\n- [BBE] (arXiv:2603.05485): DP-inspired Gaussian noise injection，有 formal bias bounds 但 destroys signal。\n- [CoLD] (arXiv:2507.15698): Counterfactual length debiasing for PRM，但限于 training-time、single-dimension (length)、white-box。\n- [CROME] (arXiv:2604.13833): Causal data augmentation for reward models，white-box training-time方法。\n- [Causal Rubrics] (ICML 2025, arXiv:2506.16507): Causal + neutral augmentations 训练 robust reward models，RewardBench 提升 5.4%，但需 training access。\n- [Counterfactual Style Measurement] (arXiv:2512.19908): LLM-generated counterfactual rewrites + Bradley-Terry 量化 rhetorical style effects (250K+ counterfactuals on ICLR papers)，但 quantifies without correcting。CSD 可视为其自然延伸——从 measurement 到 correction。\n- [CMBE] (AAAI 2027, arXiv:2505.16522): Multi-bias causal effect estimation and elimination，但需 white-box access。\n- [DML + Text Embeddings] (arXiv:2601.01511): 2025 年工作将 DML 与 text embeddings 结合做 causal deconfounding，验证了 DML 在 NLP 场景的适用性，但未应用于 judge debiasing。\n\n- 调研总结: LLM-as-Judge style bias 是 2025-2026 年活跃的研究热点，已有大量工作从不同角度（training-based、observational regression、prompt engineering、perturbation、causal intervention）进行 debiasing。然而，现有因果方法（RATE、CoLD、CROME、Causal Rubrics）要么需要 white-box access，要么仅做 explainability 而不产生 corrected scores，要么限于单一维度。CSD 填补了一个明确的 gap：black-box、multi-dimensional、causal debiasing with legitimacy awareness。该 gap 是真实存在的，proposal 对相关工作的定位准确。\n\n【整体印象】: 如果我是审稿人，第一反应是\"这是一篇 well-crafted、研究定位非常精准的 proposal\"。作者对领域的掌握令人印象深刻——相关工作极为全面，几乎涵盖了 2024-2026 年该方向的所有重要论文，且每篇工作的局限性分析准确到位。研究 gap 的识别是合理且有说服力的：black-box + multi-dimensional + causal 的交叉点确实是空白。方法设计有清晰的理论基础（DML），实验方案非常完备。我的倾向是 weak accept to borderline accept——这是一篇 solid work，但核心 novelty 主要在于\"已有组件的巧妙组合\"而非根本性的方法创新，最终评判取决于实验结果是否能 convincingly 展示 DML 层相对于 naive paired difference 的增量价值。\n\n【核心贡献】: \n1. 核心贡献是 dual-layer causal identification (counterfactual intervention + DML) 用于 black-box judge debiasing——这是一个有价值的方法论贡献，将计量经济学的 DML 框架首次系统应用于 LLM judge debiasing。\n2. Legitimacy-aware α parameter 是一个有意义的概念贡献——此前所有 debiasing 方法隐含假设 style effect 应被完全消除，而 CSD 首次区分了 bias vs. legitimate signal。\n3. ISE metric 作为标准化的 causal bias 诊断指标有社区工具价值。\n贡献的整体价值：中等偏上。问题重要且解决方案合理，但核心方法是 existing techniques 的组合应用（counterfactual generation 来自 RATE/counterfactual style measurement 传统，DML 来自计量经济学，correction formula 是 standard regression adjustment），创新性在组合而非组件。\n\n【方法合理性】: \n方法整体合理，几个关键判断：\n1. **DML 作为 robustness layer 的动机充分**：RATE (ICML 2025) 已经证明 imperfect counterfactuals 会引入 substantial bias，CSD 用 DML 而非 double-rewrite 来解决这个问题，理论上有 doubly-robust guarantee，且成本更低（7x vs 25x），这是合理的 alternative approach。\n2. **Content preservation gates (BERTScore ≥ 0.92 + NLI ≥ 0.95) 的设计合理但有风险**：这些阈值是否足以捕捉 subtle content leakage 是一个 open question。proposal 通过 DML nuisance absorption 和 human counterfactual quality audit 来 mitigate 这个风险，设计上是周全的。\n3. **三轴设计的局限性已被正确识别**：formality/verbosity/formatting 确实是文献中 documented 的主要 style dimensions，但 CASSE 识别了 12 个维度。3 轴 coverage 可能不够，但 proposal 包含了 coverage ablation。\n4. **替代方案考量**：一个更简单的替代方案是 \"Multi-Reg\"（proposal 中已包含为 baseline），即直接用自动化 style feature extractors 做多维回归。CSD 与 Multi-Reg 的关键差异在于 causal identification——CSD 通过 counterfactual intervention 实现 do-calculus identification，而 Multi-Reg 只做 observational regression。如果实验中 CSD 显著优于 Multi-Reg，就能证明 causal identification 的增量价值。这个 baseline 设计是聪明的。\n5. **Style_d 的操作化问题**：proposal 中 DML 公式使用 Style_d 作为 scalar treatment variable，但未明确说明如何从 counterfactual pairs 量化 Style_d。是二元变量（原始 vs 改写）还是连续变量？这需要在方法部分进一步澄清。\n\n【5 维度打分】:\n  1. 研究问题: 强 — LLM judge style bias 是经过 SOS-Bench、CASSE、Preference Leakage、Soumik 等多篇重要论文充分 documented 的真实问题，且 Preference Leakage (ICLR 2026) 证明其 downstream impact 远超评估本身。Black-box 设定切合实际需求（GPT-4o、Claude 等主流 judges 均为 proprietary）。问题的 timeliness 和 significance 都很强。\n  \n  2. 方法与创新: 中 — 方法设计合理且有理论基础，但核心创新是 existing techniques 的组合应用：counterfactual generation（来自 RATE/arXiv:2512.19908 传统）、DML（Chernozhukov et al. 2018，计量经济学标准方法）、post-hoc score correction（类似 LC-AlpacaEval 的 regression adjustment 范式）。Legitimacy-aware α 是一个有意义的增量贡献但并非 transformative insight。与 RATE 的差异化（DML vs double-rewrite）是 principled 的，但本质上是同一问题的两种 valid approaches。DML 在 NLP 文本场景的适用性已有先例（arXiv:2601.01511），不算全新的 cross-pollination。如果实验能 convincingly 展示 dual-layer design 的增量价值（尤其 CSD vs RATE-corrected 和 CSD vs Multi-Reg），可提升至 \"中强\"。\n  \n  3. 实验设计: 强 — 这是 proposal 最突出的优点。5 judges × 5 benchmarks × 8 baselines 的覆盖面在同类工作中属于顶级。8 个 baselines 设计极为周到：涵盖 no debiasing、observational regression (LC-AlpacaEval, Multi-Reg)、perturbation (BBE)、prompt engineering (Soumik)、causal (RATE-corrected)、training-based (FairJudge)、budget control (7-Call Majority Vote)。特别值得称赞的是：(a) RATE-corrected baseline 使用 RATE 的 causal estimates + CSD correction formula，实现了最公平的 causal identification 策略对比；(b) 7-Call Majority Vote 控制了 inference budget fairness；(c) Multi-Reg 作为 observational alternative 可以直接检验 causal identification 的增量价值。9 个 ablations 覆盖了所有关键 design choices。Human evaluation 设计（stratified sampling by divergence, counterfactual quality audit）遵循了领域最佳实践。统计分析（paired bootstrap, Fisher r-to-z, DML standard errors）严谨。\n  \n  4. 可行性: 中强 — 核心技术组件都有现成实现：DML 有 DoubleML 库，counterfactual generation 可用标准 LLM prompting，BERTScore 和 NLI 是现成工具。主要可行性风险：(a) 5 judges × 5 benchmarks × 7 calls/response 的 inference cost 较高（尤其 proprietary API 费用），但对于研究项目可控；(b) counterfactual quality 是否在所有 domain 上都足够好是 empirical question；(c) Human evaluation (200 responses × 3 annotators + 100-150 counterfactual audit pairs) 需要一定人力投入但规模合理。总体可行性高。\n  \n  5. 写作与呈现: 强 — Proposal 结构清晰、逻辑连贯。问题定义→gap 识别→方法设计→实验方案的叙述线非常流畅。相关工作的组织方式（按方法类型分类，每类列出代表作+关键局限性）便于审稿人快速理解 landscape。技术细节（DML 公式、content preservation gates、cost analysis）给出了充分信息而不冗余。唯一的小瑕疵是 Style_d 的操作化定义不够明确。\n\n【概率估计】: [33% - 43%] 中位 38%\n\n【估计理由】: \n该 proposal 在研究问题的重要性和 timeliness（强）、实验设计的完备性（强）、写作质量（强）三个维度表现突出，这些是 EMNLP 审稿中的重要考量因素。方法与创新维度（中）是主要短板——核心方法是 DML + counterfactual generation 的组合应用，novelty 主要在组合方式而非方法本身。然而，\"组合创新\"在 EMNLP 也有中稿先例，关键在于实验能否证明这种组合产生了超越各组件的增量价值。该 proposal 的实验设计（特别是 Multi-Reg baseline 和 RATE-corrected baseline）恰好能回答这个问题，是一个很好的 self-validation 机制。\n\n中位估计 38% 反映了以下判断：(a) 如果实验结果 strong（CSD 显著优于所有 baselines，DML > naive paired difference，α 展示 domain-specific 价值），有望获得 accept；(b) 如果实验结果 marginal（CSD 仅略优于 Multi-Reg 或 RATE-corrected），可能落入 borderline reject 区间；(c) 审稿人对 \"novelty mainly in combination\" 的容忍度有不确定性。上界 43% 反映了该方向在 EMNLP 的高 relevance 和实验设计的出色品质；下界 33% 反映了 novelty 不足和实验结果不确定性的下行风险。\n\n【主要风险】: \n1. **Novelty 被质疑为 incremental**: 审稿人可能认为 \"DML (established econometrics tool) + counterfactual generation (established NLP technique) + regression correction (standard)\" 的组合创新度不足以构成 top venue contribution，特别是 DML 已被应用于 NLP text deconfounding（arXiv:2601.01511）。应对策略：强调 dual-layer causal identification 的独特设计逻辑（counterfactual for first-stage identification, DML for robustness against imperfect counterfactuals），并确保实验清晰展示 DML 层的增量价值。\n2. **Counterfactual quality 不足导致整个 pipeline 失效**: 如果 content preservation gates 无法有效阻止 content leakage，DML 的 nuisance absorption 可能也不够（因为 leakage 可能是 systematic 的而非 random noise）。Manipulation check 和 human counterfactual quality audit 是关键——如果 audit 结果显示 human-automated gate agreement 低（如 Cohen's κ < 0.5），审稿人可能质疑整个方法的有效性。\n\n【实施评估】:\n  - 计算资源: 中等偏高。每个 response 需 7 judge calls (1 original + 6 counterfactuals) + rewriter calls + BERTScore/NLI evaluation。5 judges × 5 benchmarks 全矩阵约需数千美元 API 费用（proprietary judges），加上 open-weight judges (Qwen3-32B, Llama-4-Maverick) 需 ≥ 2×A100 GPU。DML 训练 (GBT with 5-fold cross-fitting) 计算开销很小。\n  - 数据需求: 低。所有 5 个 benchmarks 均为公开数据集，无需额外数据收集。\n  - 人工介入: 中等。Human evaluation 需要 200 responses × 3 annotators + 100-150 counterfactual audit pairs × annotators，约 800-1000 人工标注任务。需要制定 annotation guidelines 和 anchor examples，但规模可控。\n  - 训练需求: 低。CSD 本身是 post-hoc inference-time method，无需模型训练。DML 的 nuisance function 使用 GBT，训练开销极小。FairJudge baseline 需要对 open-weight judges 做 SFT→DPO→GRPO 训练（可复用原论文代码/权重）。\n  - 新 Benchmark: 否。使用 5 个现有 benchmarks。\n  - 预估周期: 10-14 周。分解：(1) Counterfactual generation pipeline 搭建 + 验证：2-3 周；(2) DML 实现 + 单 judge 单 benchmark 验证：1-2 周；(3) 全矩阵实验 (5×5×8 baselines)：3-4 周；(4) Ablations (9 组)：2-3 周；(5) Human evaluation + analysis：2-3 周；(6) 论文撰写：2-3 周（可与后期实验并行）。\n```\n\nSources:\n- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)\n- [Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)\n- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/pdf/2602.06625)\n- [Length-Controlled AlpacaEval](https://arxiv.org/html/2404.04475v2)\n- [Post-hoc Reward Calibration](https://arxiv.org/abs/2409.17407)\n- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/pdf/2603.05485)\n- [CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models](https://arxiv.org/abs/2507.15698)\n- [CROME: Robust Reward Modeling via Causal Decomposition](https://arxiv.org/html/2604.13833)\n- [Causal Rubrics: Robust Reward Modeling](https://arxiv.org/pdf/2506.16507)\n- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/html/2512.19908v1)\n- [Beyond Reward Hacking: Causal Rewards for LLM Alignment](https://arxiv.org/pdf/2501.09620)\n- [Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings and DML](https://arxiv.org/pdf/2601.01511)\n- [RBD: Any LLM Can Be a Reliable Judge](https://openreview.net/forum?id=sLNz60fJFF)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have a comprehensive understanding of the research landscape. Let me synthesize everything into my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348) (ICML 2025): 最直接的方法论竞争者。RATE 用 double-rewrite 协议解决 imperfect counterfactual 问题，提供因果可解释性但不输出修正分数，且 ~25x 推理开销。CSD 以 DML 替代 double-rewrite，7x 开销且输出修正分数——这是一个有意义的差异化。\n- [Preference Leakage](https://arxiv.org/abs/2502.01534) (ICLR 2026): 实证证明 style bias 在 LLM-as-a-judge 中会通过 RLHF/DPO 管道向下游传播，为 CSD 的 motivation 提供了强有力的支撑——debiasing judges 有 cascading benefits。\n- [Judging the Judges (Soumik)](https://arxiv.org/abs/2604.23178) (arXiv 2026.04): 量化 style bias 为 0.76–0.92，远超 position bias（≤0.04）。评测 9 种 prompt 策略，最佳仅 +7.2–11.2pp。为 CSD 提供了 empirical ceiling 参照——如果 CSD 能超越这个 ceiling，说服力很强。\n- [FairJudge](https://arxiv.org/abs/2602.06625) (arXiv 2026.02): SFT→DPO→GRPO 训练范式，但需白盒访问。CSD 的黑盒定位与其形成互补，实验中作为 open-weight-only baseline 是合理的。\n- [RBD](https://arxiv.org/abs/2505.17100) (NeurIPS 2025): Plug-in reasoning-based bias detector，+18.5% accuracy。在 prompt 层面操作，不分解具体 style 维度。CSD 的 per-axis 分解和因果估计提供了更细粒度的理解。\n- [Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475) (ICLR 2025) & [Post-hoc Reward Calibration](https://arxiv.org/abs/2409.17407) (ICLR 2025): 观察性回归方法，单维度（length），低成本。CSD 的多维因果方法是对这类方法的自然升级，但需要证明额外计算开销值得。\n- [Robust Reward Modeling via Causal Rubrics (CROME)](https://arxiv.org/abs/2506.16507) (ICML 2025): 因果增广训练 reward model，+5.4% RewardBench accuracy。需白盒训练。\n- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/abs/2512.19908) (arXiv 2025.12): 用 LLM 反事实重写 + Bradley-Terry 量化修辞风格效应，方法论上与 CSD 的反事实生成高度相关，但只量化不修正。CSD 可被视为将该方法扩展到 debiasing。\n- [Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings](https://arxiv.org/abs/2601.01511) (arXiv 2026.01): DML + text embeddings 用于因果推断，验证了 DML 在 NLP 场景中的适用性。\n\n- **调研总结**: LLM-as-a-Judge 的 style bias 是一个高度活跃的研究领域，2025–2026 年产出了大量相关工作。现有方法要么需要白盒访问（FairJudge、CROME、CoLD），要么局限于单维度观察性回归（LC-AlpacaEval），要么停留在 prompt 工程（RBD、Soumik），要么只提供可解释性但不修正分数（RATE）。CSD 提出的\"黑盒 + 多维因果 + 分数修正\"的组合确实填补了一个真实的方法论空白，novelty claim 基本成立。\n\n【整体印象】:\n如果我是审稿人，第一反应是：这是一篇思考深入、准备充分的 proposal。作者对领域现状有全面的了解，gap 的定位精准——black-box + multi-dimensional + causal + score correction 的组合确实没有被现有工作覆盖。方法设计有明确的理论动机（DML 的 doubly-robust 性质解决 imperfect counterfactual 问题），实验方案异常详尽。我的倾向是 **weak accept / borderline accept**——方向对、方法合理、实验设计扎实，但需要关注几个关键风险点能否在执行中妥善处理。\n\n【核心贡献】:\n核心贡献是提出了一个 dual-layer causal identification framework（counterfactual intervention + DML）用于黑盒 LLM judge 的多维 style debiasing。这个贡献的价值体现在三个层面：\n1. **方法论贡献**：将因果推断中的 DML 框架与 NLP counterfactual generation 结合，提供了比观察性回归更有理论保证的 debiasing 方案。\n2. **实用贡献**：黑盒适用性意味着可以直接应用于 GPT-4o、Claude 等商业 API，这是白盒方法无法做到的。\n3. **概念贡献**：legitimacy-aware α 参数引入了\"style 影响中哪些是 bias、哪些是 signal\"的区分，这是一个真实且被忽视的问题——CASSE 已经指出 style removal 有 unintended side effects。\n\n对领域的价值：中等偏高。Style bias 是 LLM 评估中的实际痛点，CSD 提供了一个有原则的解决方案。ISE metric 如果被社区采纳，有潜力成为标准化的 bias 报告工具。\n\n【方法合理性】:\n方法整体合理，有几个值得审视的点：\n\n**合理之处**：\n- DML 用于吸收 imperfect counterfactual 带来的残差内容泄露，这个动机清晰且有理论支撑。相比 RATE 的 double-rewrite（~25x），DML 是一个更经济的替代方案。\n- Content preservation gates（BERTScore + NLI）+ DML 的 dual-layer 设计确实比单独使用任何一层更 robust。\n- 3 个 style axis 的选择有文献支持（SOS-Bench, CASSE）。\n\n**需要审视的点**：\n1. **DML 理论保证的适用性**：Chernozhukov et al. (2018) 的 DML 假设 i.i.d. 数据。CSD 的数据是 paired（original + 6 counterfactuals），数据点之间存在依赖关系。√n-consistency 和 doubly-robust 性质是否在这种 paired 数据结构下仍然成立，需要更严格的论证。这是审稿人很可能追问的点。\n2. **更简单的替代方案**：Multi-Reg（多维观察性回归）是一个非常强的 baseline。如果 Multi-Reg 已经能捕获大部分 style 效应，CSD 的 7x 额外开销是否值得？这需要实验来回答。\n3. **α calibration 的 leave-one-benchmark-out 方法**有 overfitting 风险，尤其在只有 5 个 benchmarks 的情况下。\n\n**总体判断**：方法设计有明确的理论动机和实践价值，但几个理论细节需要在论文中谨慎处理。没有致命缺陷。\n\n【5 维度打分】:\n  1. 研究问题: 【强】— Style bias 在 LLM judges 中是一个被广泛验证的严重问题（Soumik 量化为 0.76–0.92），且 Preference Leakage (ICLR 2026) 证明了其下游传播效应。Black-box multi-dimensional causal debiasing 是一个真实的未解决 gap，研究价值明确。\n\n  2. 方法与创新: 【中偏强】— 将 DML 与 counterfactual intervention 结合用于黑盒 judge debiasing 是新颖的，填补了 RATE（只解释不修正，25x 开销）和 LC-AlpacaEval（观察性，单维度）之间的空白。Legitimacy-aware α 是一个概念创新。但核心组件（counterfactual rewriting、DML、style 分解）各自都不新——novelty 在于组合而非基础方法论突破。RATE (ICML 2025) 和 Counterfactual Style Measurement (arXiv 2512.19908) 已经建立了 counterfactual rewriting 用于 style 效应估计的范式，CSD 的增量贡献在于 DML 层和 score correction。\n\n  3. 实验设计: 【强】— 这是 proposal 最突出的部分。5 judges × 5 benchmarks × 8 baselines 的矩阵覆盖非常全面。Baselines 选择精当：包含了 compute-normalized 对照（7-Call Majority Vote）、同-causal-family 对照（RATE-corrected）、最佳 observational 对照（Multi-Reg）、最佳 prompt 对照（Soumik）。9 项 ablations 涵盖了所有关键假设。Human evaluation 设计遵循最佳实践（stratified sampling、counterfactual quality audit、inter-annotator agreement）。统计分析（bootstrap、Fisher r-to-z、DML standard errors）完备。与 LC-AlpacaEval (ICLR 2025) 和 RATE (ICML 2025) 的实验设计标准相比，本 proposal 达标甚至超标。\n\n  4. 可行性: 【中】— 方案技术上可行，但有几个执行风险：(a) 高质量 counterfactual generation 是整个方法的基础，BERTScore ≥ 0.92 + NLI ≥ 0.95 的 gate 能否真正保证 content preservation 有待验证；(b) 5 judges × 5 benchmarks × 8 baselines 的实验矩阵规模很大，API 调用成本不低（尤其 GPT-4o 和 Claude Sonnet 4）；(c) DML 的 5-fold cross-fitting 在较小 benchmarks（如 MT-Bench ~80 instances）上可能面临 statistical power 问题，proposal 已承认这一点；(d) 200 responses 的人工评估需要标注资源。整体可行但需要充足的计算和人力预算。\n\n  5. 写作与呈现: 【强】— Proposal 逻辑清晰，从 problem → gap → method → experiment 的叙事链完整。Related work 的分类（training-based, observational, perturbation-based, reasoning-based, statistical, prompt-engineering, white-box causal）系统且全面。方法动机的论证（为什么需要 DML on top of counterfactual intervention）有说服力。公式表达简洁准确。唯一小瑕疵是篇幅偏长，正式论文需要精简。\n\n【概率估计】: [32% - 48%] 中位 40%\n\n【估计理由】:\n推理过程如下：\n\n**上行因素**（推高概率的因素）：\n- 研究问题精准命中当前热点，且有 Preference Leakage (ICLR 2026) 等工作支撑其重要性\n- Gap 定位清晰且确实存在——黑盒多维因果 debiasing 目前无人做\n- 实验设计异常完备，8 baselines + 9 ablations + human eval + statistical analysis，远超平均 proposal 的实验规划\n- 方法有理论动机且与 RATE 的方法论差异清晰\n- Legitimacy-aware α 是一个真正的概念贡献\n\n**下行因素**（压低概率的因素）：\n- Novelty 主要在组合而非基础创新——counterfactual rewriting、DML、style 分解各自都是已有技术\n- 7x 推理开销 vs. Multi-Reg 的 1x，如果性能提升不够显著，cost-effectiveness 会被质疑\n- DML 在 paired/dependent 数据上的理论保证需要更严格论证\n- 3 axis 的覆盖率可能不足——如果 axis coverage ablation 显示 3 axes 只解释了 <50% 的 style variance，整个方法的效用会打折\n- 竞争激烈：RBD (NeurIPS 2025)、FairJudge、Soumik 等同期工作很多，审稿人可能已经 review fatigue\n\n**总体判断**：这是一篇 \"solid but not exceptional\" 的 proposal。方向正确、方法合理、实验充分，属于 \"above average submission\" 但不是 \"must accept\"。在 EMNLP 2026 的竞争中，预计处于 borderline 区域，最终结果很大程度取决于实验执行质量和审稿人匹配。\n\n【主要风险】:\n1. **Marginal empirical gains over simpler baselines**: 如果 CSD 相比 Multi-Reg（1x cost）的提升不够显著（例如 <2-3pp accuracy），审稿人会质疑 7x 开销的合理性。这是最大的风险——方法再有理论美感，如果\"贵了 7 倍但只好了一点\"，说服力大减。\n2. **DML 理论保证在 paired data 下的适用性**: Chernozhukov et al. (2018) 的标准 DML 理论假设 i.i.d. 观测。CSD 的 counterfactual pairs 引入了观测间的依赖结构。如果审稿人要求严格证明 √n-consistency 在此设定下仍成立，而论文没有给出令人满意的回答，这会成为一个 methodological weakness。\n\n【实施评估】:\n  - 计算资源: 中高。5 judges 中包含 GPT-4o、Claude Sonnet 4、Gemini 2.5 Pro 三个商业 API，每个 response 需要 7 次 judge call + counterfactual generation call。估算 5 benchmarks × ~1000 instances × 7 calls × 5 judges ≈ 175K API calls（仅 main experiments），加上 ablations 和 baselines 可能达到 300K+。API 费用预估 $2,000–$5,000。\n  - 数据需求: 低。所有 5 个 benchmarks 均为公开数据集。\n  - 人工介入: 中。200 responses × 3 annotators 的质量评估 + 100–150 counterfactual pairs × annotators 的质量审计。需要招募和管理标注团队，确保 Krippendorff's α ≥ 0.6。\n  - 训练需求: 低。CSD 本身不需要训练。DML 的 nuisance function 用 gradient-boosted trees，训练量可忽略。Qwen3-32B 作为 rewriter 需要推理能力但不需要微调。FairJudge baseline 需要训练但可使用作者释出的模型。\n  - 新 Benchmark: 无。使用现有 benchmarks。ISE metric 是新提出的诊断指标但不需要新数据。\n  - 预估周期: 2.5–4 个月。Counterfactual generation + validation (2–3 weeks), main experiments (2–3 weeks, 受 API rate limit 影响), ablations (2–3 weeks), human evaluation (3–4 weeks including annotation setup), analysis + writing (3–4 weeks)。若资源充足，并行化可压缩至 2.5 个月。\n```\n\nSources:\n- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)\n- [Judging the Judges (Soumik)](https://arxiv.org/abs/2604.23178)\n- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/abs/2602.06625)\n- [RBD: Any Large Language Model Can Be a Reliable Judge](https://arxiv.org/abs/2505.17100)\n- [Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475)\n- [Post-hoc Reward Calibration](https://arxiv.org/abs/2409.17407)\n- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507)\n- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/abs/2512.19908)\n- [Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings](https://arxiv.org/abs/2601.01511)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile my assessment.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [SOS-Bench / Style Outweighs Substance] (arXiv:2409.15268): 直接动机论文，证明surface-level style features在LLM judge评分中主导substance。CSD的核心问题设置直接源于此发现。\n- [CASSE] (arXiv:2601.10809): 识别12个交叉关联的style features，核心发现是style features高度entangled而非正交。CSD的3-axis设计需回应此发现，proposal中已纳入coverage分析和相关性检验作为ablation。\n- [Preference Leakage] (ICLR 2026, arXiv:2502.01534): 证明style bias通过judge→reward model→policy model的pipeline传播。为CSD提供了beyond evaluation的更广泛动机。\n- [Soumik / Judging the Judges] (arXiv:2604.23178): 量化style bias 0.76-0.92远超position bias ≤0.04，评估9种prompt策略，最佳仅+7-11pp。确认prompt-based方法ceiling较低。\n- [RATE] (ICML 2025, arXiv:2410.11348): 最直接的方法论竞争者。使用double-rewrite协议处理imperfect counterfactuals，但25x成本且不产生corrected scores。CSD用DML替代double-rewrite，7x成本且产生可用的debiased scores——这是清晰的差异化。\n- [LC-AlpacaEval] (ICLR 2025, arXiv:2404.04475): 通过logistic regression debias length效应，将AlpacaEval与Chat Arena的相关性从0.93提升至0.98。方法简单有效但限于单维度、observational。CSD在方法论上是其multi-dimensional causal generalization。\n- [FairJudge] (arXiv:2602.06625): SFT→DPO→GRPO三阶段训练debiased judge。需white-box access，无法用于proprietary models。与CSD互补而非竞争。\n- [Causal Rubrics / CROME] (ICML 2025, arXiv:2506.16507): 用causal augmentations训练robust reward models，RewardBench +5.4%。训练时white-box方法，与CSD的black-box post-hoc定位不同。\n- [BBE / Bias-Bounded Evaluation] (arXiv:2603.05485): DP-inspired noise injection提供formal bias bounds，但destruction of signal alongside bias。CSD的targeted intervention approach更精细。\n- [RBD] (NeurIPS 2025, arXiv:2505.17100): Prompt-level reasoning-based bias detection +18.5%准确率。不disentangle具体style维度，与CSD互补。\n- [Counterfactual LLM-based Style Measurement] (arXiv:2512.19908): 证明LLM-generated counterfactuals + Bradley-Terry可量化rhetorical style effects，250K+ counterfactuals on 8,485 ICLR papers。验证了counterfactual rewriting在style measurement中的可行性，但不做correction。\n- [Causal Inference-Time Intervention for Reward Models] (arXiv:2604.27495): 在neuron level做Bradley-Terry reward model的causal decomposition。White-box方法，不适用于proprietary judge APIs。\n- [CoLD] (arXiv:2507.15698): Counterfactual reasoning for length debiasing of process reward models。训练时、单维度、white-box限制。\n- [Reading Between the Lines] (arXiv:2601.01511): Neural Network-Enhanced DML framework leveraging text embeddings for causal identification。证明DML+text embeddings在NLP因果推断中的可行性，但未应用于LLM judge debiasing。\n\n- **调研总结**: LLM judge style bias是2025-2026年高度活跃的研究方向，已有大量工作从不同角度攻击这一问题。但现有方法明确分为两类：(1) white-box causal方法（Causal Rubrics, CoLD, Causal Inference-Time Intervention）效果好但无法用于proprietary judges；(2) black-box方法要么是observational/prompt-based（LC-AlpacaEval, RBD, Soumik）缺乏causal rigor，要么只做explainability不做correction（RATE）。CSD填补的\"black-box + multi-dimensional + causal + post-hoc correction\"这一交叉空位确实存在，且不是trivial extension——将DML引入counterfactual intervention框架需要非平凡的方法论设计。\n\n【整体印象】: \n作为审稿人，这是一份让人印象深刻的proposal。第一反应是倾向于weak accept。原因：(1) 问题动机极其清晰，有大量实证文献支撑style bias的严重性；(2) 方法定位精准——\"black-box + causal + multi-dimensional + post-hoc\"是一个真实且有价值的空位；(3) 将DML框架与counterfactual intervention结合的dual-layer设计是一个有技术深度的贡献，不是简单拼凑；(4) 实验设计的完备程度远超一般proposal（5 judges × 5 benchmarks × 8 baselines × 9 ablations + human eval + counterfactual quality audit），这显示了对审稿过程的深入理解；(5) legitimacy-aware α correction是一个genuine conceptual advance。\n\n主要的审稿顾虑集中在：(a) DML的partially linear model假设在LLM judge scoring这种高度非线性场景下是否成立；(b) 3个style axis是否足以cover主要的style variation（尽管已有ablation计划）；(c) 实际debiasing gains相对于simpler baselines（如Multi-Reg）的边际提升是否足够显著以justify 7x的inference cost。\n\n【核心贡献】: \n核心贡献是提出了第一个适用于black-box LLM judges的multi-dimensional causal debiasing框架。具体而言：\n1. **Dual-layer causal identification**（counterfactual intervention + DML）是方法论上的主要创新。相比RATE的double-rewrite（25x成本），CSD用DML nuisance absorption（7x成本）解决imperfect counterfactual问题，并提供了formal semiparametric efficiency guarantees。\n2. **Legitimacy-aware correction**（α parameter）是概念上的贡献——不是所有style influence都是bias，区分bias vs. legitimate signal是prior work普遍忽略的问题。\n3. **ISE metric** 作为standardized causal bias diagnostic有一定社区价值。\n\n这些贡献对领域价值较高：LLM-as-judge是当前评估基础设施的核心组件，其bias直接影响RLHF/DPO pipeline。一个principled、practical的debiasing方法有广泛的应用价值。\n\n【方法合理性】: \n方法整体合理，但有几个需要注意的点：\n\n**合理之处**：\n- Counterfactual intervention是估计causal effects的gold standard approach。用LLM rewrite生成counterfactuals已被RATE和arXiv:2512.19908验证可行。\n- DML作为second layer处理imperfect counterfactuals是合理的——这比RATE的double-rewrite在理论上更优雅（有formal guarantees），在成本上更优（7x vs 25x）。\n- Content preservation gates（BERTScore ≥ 0.92 + NLI ≥ 0.95）是标准做法。\n- 3-axis选择（formality, verbosity, formatting）有SOS-Bench和CASSE的实证支持。\n\n**潜在问题**：\n- DML假设Score = β_d · Style_d + g(Content, Style_{-d}) + ε，这是partially linear model。如果style effect是非线性的（例如moderate formality最优，过高或过低都有penalty），线性β_d可能miss真实的effect structure。Proposal未讨论非线性extension。\n- Rewriter confounding的处理虽然提到了independence principle（当judge = Qwen3-32B时换用Llama rewriter），但更微妙的问题是：不同rewriter可能引入不同的rewrite artifacts，这些artifacts本身可能被judge系统性偏好。Cross-rewriter consistency ablation可以部分检测但不能完全解决。\n- α calibration用leave-one-benchmark-out cross-validation，但只有5个benchmarks，cross-validation的variance可能很高。\n\n**更简单的替代方案**：\n- Multi-Reg（多维observational regression）是最直接的简单替代。CSD需要convincingly demonstrate DML+counterfactual的边际贡献超过Multi-Reg。Proposal将Multi-Reg列为baseline，这是正确的。关键实验结果将决定方法的说服力。\n- 如果Multi-Reg与CSD差距不大，审稿人可能质疑7x inference cost的必要性。\n\n【5 维度打分】:\n\n1. **研究问题**: 强 — Style bias在LLM judges中的严重性已被多篇高质量论文（SOS-Bench, CASSE, Preference Leakage, Soumik）充分证实，且该bias通过RLHF/DPO pipeline级联传播（Preference Leakage, ICLR 2026）。Black-box debiasing的需求在proprietary model主导评估实践的现状下尤为迫切。问题的重要性和研究价值毫无疑问。\n\n2. **方法与创新**: 中偏强 — 将DML引入LLM judge debiasing是一个novel combination。Dual-layer设计（counterfactual + DML）相比RATE的double-rewrite是一个有技术实质的替代方案，不是trivial variation。Legitimacy-aware α是概念上的genuinely new idea。但DML本身是成熟工具（Chernozhukov 2018），counterfactual rewriting也已有先例（RATE, arXiv:2512.19908），核心创新是\"组合+应用\"而非fundamental methodological advance。另外，partially linear model假设是一个理论层面的limitation。相比Causal Rubrics (ICML 2025)的causal augmentation approach和RATE (ICML 2025)的double-rewrite，CSD的创新度是comparable的。\n\n3. **实验设计**: 强 — 这是proposal最突出的优势之一。5 judges × 5 benchmarks的coverage远超领域内多数工作。8个baselines涵盖了所有主要方法类型（observational, perturbation, prompt, training, causal），且包含了compute-normalized comparison（7-Call Majority Vote）和method-normalized comparison（RATE-corrected）。9个ablations系统地覆盖了方法中每个关键design choice。Human evaluation protocol（stratified sampling + counterfactual quality audit）设计合理，Krippendorff's α target和bootstrap CI显示了统计学素养。DML robustness checks（nuisance estimator comparison, effective sample size, statistical power discussion）是审稿人常关注的技术细节。这个实验设计如果fully executed，将是非常convincing的。\n\n4. **可行性**: 中 — 方案原则上可以执行，但有显著的资源和工程挑战：\n   - 5 judges × 5 benchmarks × 7 calls/response的inference cost相当高。GPT-4o和Claude Sonnet 4的API成本不容忽视（粗估数万美元级别API调用费）。\n   - 生成高质量counterfactuals需要大量rewrite + quality gate filtering + retries，pipeline工程量大。\n   - Human evaluation 200 responses × 3 annotators + 100-150 counterfactual pairs需要相当的标注资源。\n   - 5-fold cross-fitting DML for each style axis × each judge × each benchmark的计算量也需考虑。\n   - α calibration的leave-one-benchmark-out在只有5个benchmarks时统计可靠性有限。\n   整体可行但需要充足的预算和工程能力。\n\n5. **写作与呈现**: 强 — Proposal结构清晰，逻辑链完整：Problem→Gap→Method→Experiments。每个design choice都有明确的rationale（如为什么用DML而不是simple paired differences，为什么选3个axes，为什么需要cross-rewriter consistency check）。对prior work的定位准确且公平（不strawman任何baseline）。Related work覆盖全面，包括最新的2026年论文。方法表述数学上精确。Acknowledged limitations诚实。整体呈现出对领域和审稿流程的深刻理解。\n\n【概率估计】: [33% - 48%] 中位 40%\n\n【估计理由】: \n这是一份高于平均水平的proposal，具备扎实的研究问题、合理的方法设计和出色的实验规划。\n\n**向上推动的因素**：\n- 研究问题高度timely且important（LLM judge bias + alignment pipeline影响）\n- Gap identification准确且convincing——真正的black-box causal debiasing空位\n- 实验设计的completeness在同类投稿中属于top tier\n- Legitimacy-aware correction是一个genuine conceptual advance\n- ISE作为standardized metric有community adoption potential\n- 写作quality和scholarly rigor高\n\n**向下拉动的因素**：\n- 核心方法论创新是\"组合+应用\"（DML + counterfactual），非fundamental advance。审稿人可能认为技术contribution深度不足\n- Partially linear model假设可能oversimplify style-score关系，审稿人可能challenge\n- 如果Multi-Reg baseline表现接近CSD，整个方法的value proposition（7x cost for how much gain?）会被严重质疑\n- α calibration在5个benchmarks上的statistical reliability是一个实际风险\n- 3-axis coverage的完备性虽有ablation，但如果coverage很低（如仅解释30%的style variance），整个方法的practical value会打折扣\n- 这是一个proposal，最终结果的强弱（DML vs Multi-Reg的margin, coverage fraction等）将决定上下限\n\n**综合判断**：EMNLP 2026近年录取率约22-25%。此proposal在研究问题和实验设计上显著高于average submission，方法创新度属于solid但非outstanding。如果实验结果如预期（DML显著优于observational baselines, 3-axis coverage合理, human eval confirms debiasing quality），估计在weak accept/borderline区间，中位约40%。若实验结果不如预期（如DML与Multi-Reg差异不显著），概率会降至25-30%。\n\n【主要风险】: \n1. **DML vs. simpler baselines的边际收益不显著**：如果Multi-Reg（多维observational regression，0额外cost）的debiasing效果接近CSD（7x cost），审稿人会质疑整个causal identification的必要性。这是最可能导致rejection的单一风险——\"interesting framework but the simpler baseline works just as well\"。\n2. **3-axis coverage不足**：如果formality + verbosity + formatting仅解释了judge score variance中较小的fraction（如<40%），残余的unexplained style bias会显著削弱方法的practical value，审稿人可能认为\"partial solution to a large problem\" insufficient for acceptance。\n\n【实施评估】:\n  - 计算资源: 高。5个proprietary judge API × 7 calls/response × 5 benchmarks = 大量API调用。粗估：假设每个benchmark平均500-1000 instances，总共约5 × 7 × 5 × 750 ≈ 131,250次judge API调用（不含rewrite calls和retries）。GPT-4o和Claude的cost估计在$5K-$15K范围。rewriter（Qwen3-32B）可用开源部署降低成本。\n  - 数据需求: 中。5个benchmarks均为publicly available（SOS-Bench, RewardBench, RewardBench 2, MT-Bench, Arena-Hard-Auto）。不需要构建新数据集，但需要大规模生成counterfactuals并进行quality filtering。\n  - 人工介入: 中。Human evaluation需要200 responses × 3 annotators + 100-150 counterfactual quality audit pairs × annotators。估计需要600-1000个human annotation units。需要设计详细的annotation rubric和training annotators。\n  - 训练需求: 低。CSD本身是post-hoc方法，不需要训练LLM。DML的nuisance function（gradient-boosted trees）训练量极小。FairJudge baseline需要复现其训练，但该工作如有released model可直接使用。\n  - 新 Benchmark: 无。完全使用existing benchmarks。\n  - 预估周期: 3-4个月。Breakdown：Pipeline工程+counterfactual生成（3-4周）→ API judge调用+data collection（2-3周，可能受rate limits影响）→ DML estimation+analysis（1-2周）→ Human evaluation recruitment+execution（3-4周）→ Ablations+additional experiments（2-3周）→ Writing（3-4周）。如果一人全职约4个月；2-3人团队约2.5-3个月。\n```\n\nSources:\n- [SOS-Bench: Style Outweighs Substance](https://arxiv.org/pdf/2409.15268)\n- [Judging the Judges: Systematic Evaluation of Bias Mitigation](https://arxiv.org/abs/2604.23178)\n- [RATE: Causal Explainability of Reward Models](https://arxiv.org/abs/2410.11348)\n- [Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475)\n- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/abs/2602.06625)\n- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507)\n- [CROME: Robust Reward Modeling via Causal Data Augmentation](https://arxiv.org/html/2604.13833)\n- [Preference Leakage: A Contamination Problem](https://arxiv.org/pdf/2502.01534)\n- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/html/2512.19908v1)\n- [Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/html/2604.27495)\n- [A Survey on LLM-as-a-Judge](https://arxiv.org/html/2411.15594v6)\n- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/pdf/2603.05485)\n- [RBD: Debiasing with a Reasoning-based Bias Detector](https://openreview.net/forum?id=sLNz60fJFF)\n- [Reading Between the Lines: DML with Text Embeddings](https://arxiv.org/pdf/2601.01511)\n- [Evaluating Scoring Bias in LLM-as-a-Judge](https://arxiv.org/html/2506.22316v1)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n## Causal Style Decomposition for Debiasing Black-Box LLM Judges\n\n### 1. Problem and Motivation\n\nLLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic style biases. SOS-Bench (arXiv:2409.15268) demonstrates that surface-level style features dominate substance in judge scoring. CASSE (arXiv:2601.10809) identifies 12 cross-correlated style features inducing evaluation side effects, with the core finding that style features are deeply entangled rather than orthogonal. Preference Leakage (ICLR 2026, arXiv:2502.01534) shows style-driven contamination propagates through training pipelines—from judge preferences to reward models to policy models. Soumik (arXiv:2604.23178) quantifies style bias at 0.76–0.92 across 5 judges, far exceeding position bias (≤0.04). Earlier work on LLM evaluation bias (NAACL 2024) and RubricBench (arXiv:2603.01562) further document how surface features mislead judges, revealing a 27% accuracy gap between model-generated and human rubrics on hard samples with misleading surface bias.\n\nCrucially, this is not merely an evaluation problem. Preference Leakage (ICLR 2026) demonstrates that style bias in judges propagates downstream: biased preference labels enter RLHF/DPO training data, contaminating reward models and ultimately policy models. Debiasing judges at the evaluation stage therefore has cascading benefits for the entire LLM alignment pipeline.\n\nExisting debiasing approaches each have fundamental limitations:\n\n- **Training-based**: FairJudge (arXiv:2602.06625) uses SFT→DPO→GRPO to retrain judges, requiring white-box access and per-judge retraining, inapplicable to proprietary models.\n- **Observational regression**: Length-Controlled AlpacaEval (ICLR 2025, arXiv:2404.04475) regresses out length effects at zero cost; Post-hoc Reward Calibration (ICLR 2025, arXiv:2409.17407) extends this via locally weighted regression across 33 reward models. Both handle only a single dimension and rely on observational associations that conflate genuine quality correlates with spurious confounding.\n- **Perturbation-based**: Bias-Bounded Evaluation (BBE, arXiv:2603.05485) injects DP-inspired Gaussian noise for formal bias bounds but destroys signal alongside bias; RATE (ICML 2025, arXiv:2410.11348) uses a double-rewrite protocol for causal explainability of reward models, providing the key insight that single-rewrite counterfactuals are imperfect and introduce substantial bias, but requires ~25x inference overhead and does not produce corrected scores.\n- **Reasoning-based**: RBD (NeurIPS 2025, arXiv:2505.17100) is a plug-in module that detects biased evaluations and guides self-correction via structured reasoning (+18.5% accuracy), but operates at the prompt level without disentangling specific style dimensions.\n- **Statistical**: PRECISE (AAAI 2026, arXiv:2601.18777) extends prediction-powered inference to combine human annotations with LLM judgments for debiased ranking estimation, but requires human labels and does not identify which style dimensions drive bias.\n- **Prompt-engineering**: Soumik (arXiv:2604.23178) evaluates 9 prompt-based strategies; the best (\"combined budget\") achieves +7.2 to +11.2pp on select model-strategy pairs.\n\nA parallel line of causal approaches targets reward model debiasing, all requiring white-box access or training-time intervention: Causally Motivated Inference-Time Intervention (arXiv:2604.27495) decomposes Bradley-Terry reward models via total effect / controlled direct effect and intervenes at the neuron level. CROME (arXiv:2604.13833) uses causal data augmentation to suppress prompt-independent shortcuts. Causal Rubrics (arXiv:2506.16507, ICML 2025) employs causal augmentations (pairs isolating causal attribute changes) and neutral augmentations (tie-labeled pairs varying spurious attributes) to train robust reward models, improving RewardBench accuracy by up to 5.4%. CoLD (arXiv:2507.15698) applies counterfactual reasoning and causal graph analysis for length debiasing of process reward models, but is limited to training-time, single-dimension (length), and white-box settings. Causal Reward Modeling (CRM; ICLR 2027, arXiv:2501.09620) enforces counterfactual invariance in reward predictions. CMBE (AAAI 2027, arXiv:2505.16522) proposes simultaneous multi-bias causal effect estimation and elimination.\n\nSeparately, counterfactual LLM-based style measurement (arXiv:2512.19908) demonstrates that LLM-generated counterfactual rewrites combined with Bradley-Terry aggregation can robustly quantify rhetorical style effects at scale (>250K counterfactuals on 8,485 ICLR papers)—but quantifies style without correcting for it.\n\nFoundational work on causal effects of linguistic properties (Pryzant et al., NAACL 2021) established methods for estimating causal effects of text attributes using distant supervision and pre-trained language models, providing the methodological precedent for CSD's approach.\n\n**The open gap**: No existing method provides principled, multi-dimensional causal debiasing for black-box LLM judges while preserving legitimate style-quality associations. White-box causal methods (Causal Rubrics, CoLD, arXiv:2604.27495) cannot be applied to proprietary judge APIs. Black-box methods remain limited to observational regression (LC-AlpacaEval) or prompt engineering (RBD, Soumik). CSD fills this gap by bridging two independently developing literatures: (1) the NLP evaluation community's empirical documentation of style biases with ad-hoc fixes, and (2) the causal inference / econometrics community's principled frameworks (Double Machine Learning; Chernozhukov et al. 2018) that have not yet been systematically applied to black-box LLM judge debiasing.\n\n### 2. Core Contributions\n\n1. **Causal Style Decomposition (CSD) framework**: A black-box, post-hoc method that decomposes LLM judge scores into content-driven and style-driven components via targeted counterfactual interventions along three style axes, using a dual-layer causal identification strategy: counterfactual intervention for first-stage identification, DML (Chernozhukov et al. 2018) for second-stage robustness against imperfect counterfactuals.\n\n2. **Legitimacy-aware correction**: Unlike all prior debiasing methods that implicitly assume style effects should be fully removed, CSD introduces a domain-conditional α parameter distinguishing domain-invariant style bias from domain-specific legitimate style-quality associations—addressing CASSE's (arXiv:2601.10809) finding that style removal has unintended side effects. This is a conceptual advance: the question is not just \"how much style bias exists\" but \"which portion of style influence is bias vs. signal.\"\n\n3. **Interventional Style Effect (ISE) metric**: A standardized, causal diagnostic for per-axis judge bias auditing. Unlike observational bias scores (e.g., Soumik's style bias metric of 0.76–0.92), ISE measures interventional causal sensitivity, enabling principled cross-judge comparison (\"GPT-4o's formality ISE is 2.3× Claude's\"), cross-domain analysis, and version-tracking of judge bias. ISE has potential as a community-standard bias reporting metric analogous to FID for image generation.\n\n4. **Empirical validation** across 5 judges × 5 benchmarks with 8 baselines, comprehensive ablations, compute-normalized comparisons, counterfactual quality auditing, and human evaluation.\n\n### 3. Method\n\n#### 3.1 Counterfactual Style Generation\n\nFor each response $r$, generate 6 counterfactuals by intervening on 3 style axes in 2 directions each:\n- **Formality**: formal ↔ informal tone (preserving content)\n- **Verbosity**: concise ↔ verbose (preserving information content)\n- **Formatting**: heavy markdown/structure ↔ plain text\n\nRewriter: Qwen3-32B (default). When the target judge is Qwen3-32B, use an independent rewriter (Llama-3.3-70B) to prevent rewriter-evaluator confounding, following the independence principle in RATE (ICML 2025, arXiv:2410.11348).\n\n**Content preservation gates**: Counterfactuals must pass BERTScore ≥ 0.92 AND NLI entailment score ≥ 0.95 relative to the original. Failing samples are re-generated (up to 3 retries) or excluded.\n\n**Three-axis design rationale**: Formality, verbosity, and formatting capture the dominant style variation documented in SOS-Bench (arXiv:2409.15268) and CASSE (arXiv:2601.10809). We treat their approximate independence as an empirical hypothesis to be verified (via correlation analysis of ISE estimates across axes), not an a priori assumption—important given CASSE's finding of style feature entanglement. Coverage analysis (fraction of total style variance these 3 axes explain) is included as an ablation. The framework extends to additional axes at linear cost.\n\n#### 3.2 Dual-Layer Causal Identification via DML\n\n**Why DML on top of counterfactual intervention?** A natural question is: given paired data (original + 6 counterfactuals), why not simply compute mean paired score differences as ATE estimates? The answer is that content preservation gates (BERTScore ≥ 0.92, NLI ≥ 0.95) are imperfect—residual content leakage inevitably passes through. RATE (ICML 2025, arXiv:2410.11348) demonstrated that imperfect counterfactuals introduce substantial bias in causal estimates, solving this via a double-rewrite protocol (rewriting the rewrite to cancel rewrite-induced bias). CSD takes an alternative approach with stronger theoretical guarantees:\n\n- **First layer (counterfactual intervention)**: Provides approximate do-calculus identification by actively manipulating style while holding content approximately fixed.\n- **Second layer (DML)**: The nuisance function $g(Content, Style_{-d})$ captures and partials out residual content variation that leaked through imperfect gates, providing doubly-robust, $\\sqrt{n}$-consistent estimation even if either the treatment or outcome model is misspecified.\n\nThis dual-layer design means CSD is robust to the imperfect-counterfactual problem that RATE solves via double-rewrite, but at ~7x inference cost (vs. RATE's ~25x) and with formal semiparametric efficiency guarantees.\n\nFor each style axis $d \\in \\{formality, verbosity, formatting\\}$, estimate the causal effect $\\beta_d$:\n\n$$Score = \\beta_d \\cdot Style_d + g(Content, Style_{-d}) + \\epsilon$$\n\nwhere $g(\\cdot)$ is estimated via gradient-boosted trees with 5-fold cross-fitting per Chernozhukov et al. (2018). Building on the causal identification logic of Pryzant et al. (NAACL 2021), this framework estimates the direct causal effect of each style dimension on judge scores while controlling for content quality and other style axes.\n\n#### 3.3 Legitimacy-Aware Correction\n\n$$Score_{debiased} = Score_{original} - \\sum_{d} (1 - \\alpha_d) \\cdot \\hat{\\beta}_d \\cdot (Style_d - Style_{ref})$$\n\nwhere $\\alpha_d \\in [0,1]$ is domain-conditional. $\\alpha_d = 0$: full debiasing; $\\alpha_d = 1$: no debiasing.\n\n**α calibration protocol**: Leave-one-benchmark-out cross-validation. Sensitivity analysis reports performance across α ∈ {0.0, 0.1, ..., 1.0}.\n\n#### 3.4 Format Adaptation\n\nCSD adapts to different evaluation formats: (a) **Pointwise** (MT-Bench): debias each response's score independently; (b) **Pairwise** (Arena-Hard-Auto, SOS-Bench): debias both chosen and rejected responses, then re-rank; (c) **Multi-choice** (RewardBench, RewardBench 2): debias each candidate's score independently, then select the highest-scoring candidate. Inference cost scales with the number of candidates per instance.\n\n#### 3.5 Inference Cost\n\nCSD requires 7 judge calls per response (1 original + 6 counterfactuals), ~7x overhead. This compares favorably to RATE's ~25x, while providing actionable score correction rather than only explainability.\n\n### 4. Experimental Design\n\n#### 4.1 Judges (5)\n\nGPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Qwen3-32B, Llama-4-Maverick. Covers 4 provider families and both proprietary and open-weight models.\n\n#### 4.2 Benchmarks (5)\n\n- **SOS-Bench** (arXiv:2409.15268): Style-substance separation evaluation\n- **RewardBench**: Standard reward model evaluation\n- **RewardBench 2** (arXiv:2506.01937): Updated with factuality and precise instruction following domains\n- **MT-Bench**: Multi-turn dialogue quality\n- **Arena-Hard-Auto**: Challenging single-turn evaluation\n\n#### 4.3 Baselines (8)\n\n| Baseline | Type | Extra cost | Applicability |\n|---|---|---|---|\n| Raw Judge | No debiasing | 1x | All judges |\n| LC-AlpacaEval (ICLR 2025, arXiv:2404.04475) | Single-dim observational regression | 1x | All judges |\n| Multi-Reg | Multi-dim observational regression | 1x | All judges |\n| BBE (arXiv:2603.05485) | DP noise injection | 1x | All judges |\n| Prompt-Debiasing (Soumik, arXiv:2604.23178) | Combined budget prompt strategy | 1x | All judges |\n| RATE-corrected (ICML 2025, arXiv:2410.11348) | Double-rewrite causal estimation + CSD-style correction | ~25x | All judges |\n| FairJudge (arXiv:2602.06625) | Training-based (SFT→DPO→GRPO) | 1x post-train | Open-weight only |\n| 7-Call Majority Vote | Same-budget sampling | 7x | All judges |\n\nMulti-Reg uses automated style feature extractors (markdown density, word count, Flesch-Kincaid readability) as covariates for multivariate regression—the most direct observational alternative to CSD. RATE-corrected applies RATE's double-rewrite causal estimates with CSD's correction formula, enabling direct comparison of the two causal identification strategies at different compute budgets. 7-Call Majority Vote controls for inference budget fairness. Results tables clearly distinguish all-judge-applicable baselines from open-weight-only methods (FairJudge) to avoid misleading comparison.\n\n#### 4.4 Metrics\n\n- **Primary**: Pairwise accuracy, Spearman/Kendall-τ correlation with ground-truth quality\n- **Diagnostic**: ISE per axis per judge (causal bias magnitude)\n- **Efficiency**: Accuracy-per-judge-call curve (1x, 3x, 5x, 7x, 25x budget)\n\n#### 4.5 Ablations\n\n1. **Decomposition method**: Linear regression vs. DML vs. nonparametric kernel estimation for β\n2. **Per-axis importance**: Single-axis (3 runs) + pairwise combinations (3 runs) + full 3-axis\n3. **Content preservation thresholds**: BERTScore ∈ {0.85, 0.88, 0.90, 0.92, 0.95} × NLI ∈ {0.90, 0.93, 0.95, 0.97}\n4. **Cross-rewriter consistency**: ISE and accuracy using Qwen3-32B vs. Llama-3.3-70B vs. Claude as rewriter\n5. **Axis coverage**: Variance decomposition—fraction of judge score variance explained by 3 axes vs. residual\n6. **α sensitivity**: Full grid α ∈ [0,1], per-domain performance landscape\n7. **ISE-based cross-judge comparison**: ISE estimates across judges and domains\n8. **Manipulation check**: Per-axis style metric effect sizes (Cohen's d) on automated proxies—formality → Flesch-Kincaid / formality classifier; verbosity → word count ratio; formatting → markdown element density. Validates that counterfactual interventions produce sufficient style variation for reliable ISE estimation.\n9. **DML robustness check** (supplementary): Nuisance estimator comparison (GBT vs. Random Forest vs. Lasso), per-cell effective sample size, and DML standard error analysis. Discussion of statistical power for smaller benchmarks (e.g., MT-Bench ~80 multi-turn dialogues).\n\n#### 4.6 Human Evaluation\n\n**Quality evaluation (200 responses)**: Stratified by divergence between CSD and raw judge rankings—sampled from top-20% (high divergence), middle 40%, and bottom 40% by divergence magnitude. 3 annotators per response, 5-point Likert scale evaluating content quality and presentation quality independently. Inter-annotator agreement target: Krippendorff's α ≥ 0.6, reported with bootstrap 95% CI. Annotation rubric includes operationalized definitions and anchor examples, following RubricBench (arXiv:2603.01562) best practices.\n\n**Counterfactual quality audit (100–150 pairs)**: ~50 per style axis, annotators judge: (1) whether target axis was successfully changed (binary), (2) whether non-target axes were unintentionally changed (Likert 1–5), (3) whether content semantics were preserved (Likert 1–5). Report Cohen's κ between automated gates (BERTScore + NLI) and human judgment, plus false positive/negative rates of the automated gates. This validates CSD's core assumption of content-preserving style intervention and addresses CASSE's (arXiv:2601.10809) entanglement concern.\n\n#### 4.7 Statistical Analysis\n\n- Pairwise accuracy differences: paired bootstrap test (10,000 resamples), 95% CIs\n- Correlation differences: Fisher r-to-z transformation for Spearman, bootstrap CIs for Kendall-τ\n- DML coefficients: asymptotic standard errors and p-values per Chernozhukov et al. (2018)\n- All main results include 95% confidence intervals\n\n### 5. Expected Outcome and Broader Impact\n\nCSD is expected to demonstrate that dual-layer causal identification (counterfactual intervention + DML) provides debiasing gains beyond observational regression (LC-AlpacaEval, Multi-Reg), perturbation methods (BBE), and prompt engineering (Soumik), particularly in domains where style-content confounding is strong. Comparison with RATE-corrected will isolate the efficiency advantage (7x vs. 25x) and compare robustness to imperfect counterfactuals (DML nuisance absorption vs. double-rewrite cancellation). The legitimacy-aware α mechanism is expected to show selective debiasing outperforms both full debiasing and no debiasing.\n\n**Broader impact on alignment pipelines**: Beyond evaluation, CSD can serve as a data quality intervention in RLHF/DPO pipelines. Preference Leakage (ICLR 2026, arXiv:2502.01534) demonstrated that style-biased judge labels contaminate reward models and downstream policies. Applying CSD to debias preference labels before they enter training could break this contamination chain at its source. While validating this downstream effect is beyond the scope of the current experiments, the framework is directly applicable to preference data curation, and we discuss this as a concrete direction for future work.\n\n**Acknowledged limitations**: (1) 3-axis coverage may miss residual style bias from uncovered dimensions; (2) counterfactual quality depends on rewriter capability; (3) 7x inference cost may be prohibitive for large-scale deployment, though axis-selective application reduces cost."
}
````

---

### Runtime record

_source line 2 · 2026-05-20T05:39:34.147Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:39:34.147Z",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T05:39:34.158Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make a thorough assessment. Let me compile the evaluation.

```
【阶段】: Triage

【领域调研】:
- [SOS-Bench] (arXiv:2409.15268): 直接动机论文，证明 style features 在 LLM judge 打分中 dominate substance。CSD 以此为核心 motivation 之一，且将其作为评测 benchmark。
- [CASSE] (arXiv:2601.10809): 识别 12 种 cross-correlated style features，核心发现 style features 高度纠缠。CSD 的 α legitimacy-aware correction 直接回应 CASSE 关于 "style removal has side effects" 的发现。
- [Preference Leakage] (ICLR 2026, arXiv:2502.01534): 证明 judge style bias 向下游 RLHF/DPO 传播。为 CSD 提供了 broader impact 论证——debiasing judges 有 cascading benefits。已被 ICLR 2026 接收，验证了该问题的重要性。
- [RATE] (ICML 2025, arXiv:2410.11348): CSD 最直接的技术竞争者。RATE 用 double-rewrite protocol 处理 imperfect counterfactuals，但需 ~25x inference cost 且不产生 corrected scores。CSD 用 DML 替代 double-rewrite，降至 7x 且产生可用的 debiased scores。RATE 已发表在 ICML 2025。
- [LC-AlpacaEval] (ICLR 2025, arXiv:2404.04475): 最广泛使用的 observational debiasing 方法，但仅处理 length 单一维度，且无法区分 causal vs. spurious associations。CSD 在多维度+因果识别上形成差异化。
- [Post-hoc Reward Calibration] (ICLR 2025, arXiv:2409.17407): 扩展 locally weighted regression 至 33 reward models，但同样是 observational，受 confounding 限制。
- [FairJudge] (arXiv:2602.06625): Training-based debiasing (SFT→DPO→GRPO)，需 white-box access，无法用于 proprietary models。CSD 在 black-box 适用性上有明确优势。
- [Soumik] (arXiv:2604.23178): 系统评估 9 种 prompt-based debiasing 策略，best strategy 仅 +7-11pp improvement。作为 prompt engineering baseline 被 CSD 纳入对比。
- [RBD] (NeurIPS 2025, arXiv:2505.17100): Reasoning-based bias detection，prompt-level 操作，不 disentangle 具体 style dimensions。
- [BBE] (arXiv:2603.05485): DP-inspired Gaussian noise injection，有 formal bias bounds 但 destroys signal。
- [CoLD] (arXiv:2507.15698): Counterfactual length debiasing for PRM，但限于 training-time、single-dimension (length)、white-box。
- [CROME] (arXiv:2604.13833): Causal data augmentation for reward models，white-box training-time方法。
- [Causal Rubrics] (ICML 2025, arXiv:2506.16507): Causal + neutral augmentations 训练 robust reward models，RewardBench 提升 5.4%，但需 training access。
- [Counterfactual Style Measurement] (arXiv:2512.19908): LLM-generated counterfactual rewrites + Bradley-Terry 量化 rhetorical style effects (250K+ counterfactuals on ICLR papers)，但 quantifies without correcting。CSD 可视为其自然延伸——从 measurement 到 correction。
- [CMBE] (AAAI 2027, arXiv:2505.16522): Multi-bias causal effect estimation and elimination，但需 white-box access。
- [DML + Text Embeddings] (arXiv:2601.01511): 2025 年工作将 DML 与 text embeddings 结合做 causal deconfounding，验证了 DML 在 NLP 场景的适用性，但未应用于 judge debiasing。

- 调研总结: LLM-as-Judge style bias 是 2025-2026 年活跃的研究热点，已有大量工作从不同角度（training-based、observational regression、prompt engineering、perturbation、causal intervention）进行 debiasing。然而，现有因果方法（RATE、CoLD、CROME、Causal Rubrics）要么需要 white-box access，要么仅做 explainability 而不产生 corrected scores，要么限于单一维度。CSD 填补了一个明确的 gap：black-box、multi-dimensional、causal debiasing with legitimacy awareness。该 gap 是真实存在的，proposal 对相关工作的定位准确。

【整体印象】: 如果我是审稿人，第一反应是"这是一篇 well-crafted、研究定位非常精准的 proposal"。作者对领域的掌握令人印象深刻——相关工作极为全面，几乎涵盖了 2024-2026 年该方向的所有重要论文，且每篇工作的局限性分析准确到位。研究 gap 的识别是合理且有说服力的：black-box + multi-dimensional + causal 的交叉点确实是空白。方法设计有清晰的理论基础（DML），实验方案非常完备。我的倾向是 weak accept to borderline accept——这是一篇 solid work，但核心 novelty 主要在于"已有组件的巧妙组合"而非根本性的方法创新，最终评判取决于实验结果是否能 convincingly 展示 DML 层相对于 naive paired difference 的增量价值。

【核心贡献】: 
1. 核心贡献是 dual-layer causal identification (counterfactual intervention + DML) 用于 black-box judge debiasing——这是一个有价值的方法论贡献，将计量经济学的 DML 框架首次系统应用于 LLM judge debiasing。
2. Legitimacy-aware α parameter 是一个有意义的概念贡献——此前所有 debiasing 方法隐含假设 style effect 应被完全消除，而 CSD 首次区分了 bias vs. legitimate signal。
3. ISE metric 作为标准化的 causal bias 诊断指标有社区工具价值。
贡献的整体价值：中等偏上。问题重要且解决方案合理，但核心方法是 existing techniques 的组合应用（counterfactual generation 来自 RATE/counterfactual style measurement 传统，DML 来自计量经济学，correction formula 是 standard regression adjustment），创新性在组合而非组件。

【方法合理性】: 
方法整体合理，几个关键判断：
1. **DML 作为 robustness layer 的动机充分**：RATE (ICML 2025) 已经证明 imperfect counterfactuals 会引入 substantial bias，CSD 用 DML 而非 double-rewrite 来解决这个问题，理论上有 doubly-robust guarantee，且成本更低（7x vs 25x），这是合理的 alternative approach。
2. **Content preservation gates (BERTScore ≥ 0.92 + NLI ≥ 0.95) 的设计合理但有风险**：这些阈值是否足以捕捉 subtle content leakage 是一个 open question。proposal 通过 DML nuisance absorption 和 human counterfactual quality audit 来 mitigate 这个风险，设计上是周全的。
3. **三轴设计的局限性已被正确识别**：formality/verbosity/formatting 确实是文献中 documented 的主要 style dimensions，但 CASSE 识别了 12 个维度。3 轴 coverage 可能不够，但 proposal 包含了 coverage ablation。
4. **替代方案考量**：一个更简单的替代方案是 "Multi-Reg"（proposal 中已包含为 baseline），即直接用自动化 style feature extractors 做多维回归。CSD 与 Multi-Reg 的关键差异在于 causal identification——CSD 通过 counterfactual intervention 实现 do-calculus identification，而 Multi-Reg 只做 observational regression。如果实验中 CSD 显著优于 Multi-Reg，就能证明 causal identification 的增量价值。这个 baseline 设计是聪明的。
5. **Style_d 的操作化问题**：proposal 中 DML 公式使用 Style_d 作为 scalar treatment variable，但未明确说明如何从 counterfactual pairs 量化 Style_d。是二元变量（原始 vs 改写）还是连续变量？这需要在方法部分进一步澄清。

【5 维度打分】:
  1. 研究问题: 强 — LLM judge style bias 是经过 SOS-Bench、CASSE、Preference Leakage、Soumik 等多篇重要论文充分 documented 的真实问题，且 Preference Leakage (ICLR 2026) 证明其 downstream impact 远超评估本身。Black-box 设定切合实际需求（GPT-4o、Claude 等主流 judges 均为 proprietary）。问题的 timeliness 和 significance 都很强。
  
  2. 方法与创新: 中 — 方法设计合理且有理论基础，但核心创新是 existing techniques 的组合应用：counterfactual generation（来自 RATE/arXiv:2512.19908 传统）、DML（Chernozhukov et al. 2018，计量经济学标准方法）、post-hoc score correction（类似 LC-AlpacaEval 的 regression adjustment 范式）。Legitimacy-aware α 是一个有意义的增量贡献但并非 transformative insight。与 RATE 的差异化（DML vs double-rewrite）是 principled 的，但本质上是同一问题的两种 valid approaches。DML 在 NLP 文本场景的适用性已有先例（arXiv:2601.01511），不算全新的 cross-pollination。如果实验能 convincingly 展示 dual-layer design 的增量价值（尤其 CSD vs RATE-corrected 和 CSD vs Multi-Reg），可提升至 "中强"。
  
  3. 实验设计: 强 — 这是 proposal 最突出的优点。5 judges × 5 benchmarks × 8 baselines 的覆盖面在同类工作中属于顶级。8 个 baselines 设计极为周到：涵盖 no debiasing、observational regression (LC-AlpacaEval, Multi-Reg)、perturbation (BBE)、prompt engineering (Soumik)、causal (RATE-corrected)、training-based (FairJudge)、budget control (7-Call Majority Vote)。特别值得称赞的是：(a) RATE-corrected baseline 使用 RATE 的 causal estimates + CSD correction formula，实现了最公平的 causal identification 策略对比；(b) 7-Call Majority Vote 控制了 inference budget fairness；(c) Multi-Reg 作为 observational alternative 可以直接检验 causal identification 的增量价值。9 个 ablations 覆盖了所有关键 design choices。Human evaluation 设计（stratified sampling by divergence, counterfactual quality audit）遵循了领域最佳实践。统计分析（paired bootstrap, Fisher r-to-z, DML standard errors）严谨。
  
  4. 可行性: 中强 — 核心技术组件都有现成实现：DML 有 DoubleML 库，counterfactual generation 可用标准 LLM prompting，BERTScore 和 NLI 是现成工具。主要可行性风险：(a) 5 judges × 5 benchmarks × 7 calls/response 的 inference cost 较高（尤其 proprietary API 费用），但对于研究项目可控；(b) counterfactual quality 是否在所有 domain 上都足够好是 empirical question；(c) Human evaluation (200 responses × 3 annotators + 100-150 counterfactual audit pairs) 需要一定人力投入但规模合理。总体可行性高。
  
  5. 写作与呈现: 强 — Proposal 结构清晰、逻辑连贯。问题定义→gap 识别→方法设计→实验方案的叙述线非常流畅。相关工作的组织方式（按方法类型分类，每类列出代表作+关键局限性）便于审稿人快速理解 landscape。技术细节（DML 公式、content preservation gates、cost analysis）给出了充分信息而不冗余。唯一的小瑕疵是 Style_d 的操作化定义不够明确。

【概率估计】: [33% - 43%] 中位 38%

【估计理由】: 
该 proposal 在研究问题的重要性和 timeliness（强）、实验设计的完备性（强）、写作质量（强）三个维度表现突出，这些是 EMNLP 审稿中的重要考量因素。方法与创新维度（中）是主要短板——核心方法是 DML + counterfactual generation 的组合应用，novelty 主要在组合方式而非方法本身。然而，"组合创新"在 EMNLP 也有中稿先例，关键在于实验能否证明这种组合产生了超越各组件的增量价值。该 proposal 的实验设计（特别是 Multi-Reg baseline 和 RATE-corrected baseline）恰好能回答这个问题，是一个很好的 self-validation 机制。

中位估计 38% 反映了以下判断：(a) 如果实验结果 strong（CSD 显著优于所有 baselines，DML > naive paired difference，α 展示 domain-specific 价值），有望获得 accept；(b) 如果实验结果 marginal（CSD 仅略优于 Multi-Reg 或 RATE-corrected），可能落入 borderline reject 区间；(c) 审稿人对 "novelty mainly in combination" 的容忍度有不确定性。上界 43% 反映了该方向在 EMNLP 的高 relevance 和实验设计的出色品质；下界 33% 反映了 novelty 不足和实验结果不确定性的下行风险。

【主要风险】: 
1. **Novelty 被质疑为 incremental**: 审稿人可能认为 "DML (established econometrics tool) + counterfactual generation (established NLP technique) + regression correction (standard)" 的组合创新度不足以构成 top venue contribution，特别是 DML 已被应用于 NLP text deconfounding（arXiv:2601.01511）。应对策略：强调 dual-layer causal identification 的独特设计逻辑（counterfactual for first-stage identification, DML for robustness against imperfect counterfactuals），并确保实验清晰展示 DML 层的增量价值。
2. **Counterfactual quality 不足导致整个 pipeline 失效**: 如果 content preservation gates 无法有效阻止 content leakage，DML 的 nuisance absorption 可能也不够（因为 leakage 可能是 systematic 的而非 random noise）。Manipulation check 和 human counterfactual quality audit 是关键——如果 audit 结果显示 human-automated gate agreement 低（如 Cohen's κ < 0.5），审稿人可能质疑整个方法的有效性。

【实施评估】:
  - 计算资源: 中等偏高。每个 response 需 7 judge calls (1 original + 6 counterfactuals) + rewriter calls + BERTScore/NLI evaluation。5 judges × 5 benchmarks 全矩阵约需数千美元 API 费用（proprietary judges），加上 open-weight judges (Qwen3-32B, Llama-4-Maverick) 需 ≥ 2×A100 GPU。DML 训练 (GBT with 5-fold cross-fitting) 计算开销很小。
  - 数据需求: 低。所有 5 个 benchmarks 均为公开数据集，无需额外数据收集。
  - 人工介入: 中等。Human evaluation 需要 200 responses × 3 annotators + 100-150 counterfactual audit pairs × annotators，约 800-1000 人工标注任务。需要制定 annotation guidelines 和 anchor examples，但规模可控。
  - 训练需求: 低。CSD 本身是 post-hoc inference-time method，无需模型训练。DML 的 nuisance function 使用 GBT，训练开销极小。FairJudge baseline 需要对 open-weight judges 做 SFT→DPO→GRPO 训练（可复用原论文代码/权重）。
  - 新 Benchmark: 否。使用 5 个现有 benchmarks。
  - 预估周期: 10-14 周。分解：(1) Counterfactual generation pipeline 搭建 + 验证：2-3 周；(2) DML 实现 + 单 judge 单 benchmark 验证：1-2 周；(3) 全矩阵实验 (5×5×8 baselines)：3-4 周；(4) Ablations (9 组)：2-3 周；(5) Human evaluation + analysis：2-3 周；(6) 论文撰写：2-3 周（可与后期实验并行）。
```

Sources:
- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)
- [Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies](https://arxiv.org/abs/2604.23178)
- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/pdf/2602.06625)
- [Length-Controlled AlpacaEval](https://arxiv.org/html/2404.04475v2)
- [Post-hoc Reward Calibration](https://arxiv.org/abs/2409.17407)
- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/pdf/2603.05485)
- [CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models](https://arxiv.org/abs/2507.15698)
- [CROME: Robust Reward Modeling via Causal Decomposition](https://arxiv.org/html/2604.13833)
- [Causal Rubrics: Robust Reward Modeling](https://arxiv.org/pdf/2506.16507)
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/html/2512.19908v1)
- [Beyond Reward Hacking: Causal Rewards for LLM Alignment](https://arxiv.org/pdf/2501.09620)
- [Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings and DML](https://arxiv.org/pdf/2601.01511)
- [RBD: Any LLM Can Be a Reliable Judge](https://openreview.net/forum?id=sLNz60fJFF)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have a comprehensive understanding of the research landscape. Let me synthesize everything into my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348) (ICML 2025): 最直接的方法论竞争者。RATE 用 double-rewrite 协议解决 imperfect counterfactual 问题，提供因果可解释性但不输出修正分数，且 ~25x 推理开销。CSD 以 DML 替代 double-rewrite，7x 开销且输出修正分数——这是一个有意义的差异化。
- [Preference Leakage](https://arxiv.org/abs/2502.01534) (ICLR 2026): 实证证明 style bias 在 LLM-as-a-judge 中会通过 RLHF/DPO 管道向下游传播，为 CSD 的 motivation 提供了强有力的支撑——debiasing judges 有 cascading benefits。
- [Judging the Judges (Soumik)](https://arxiv.org/abs/2604.23178) (arXiv 2026.04): 量化 style bias 为 0.76–0.92，远超 position bias（≤0.04）。评测 9 种 prompt 策略，最佳仅 +7.2–11.2pp。为 CSD 提供了 empirical ceiling 参照——如果 CSD 能超越这个 ceiling，说服力很强。
- [FairJudge](https://arxiv.org/abs/2602.06625) (arXiv 2026.02): SFT→DPO→GRPO 训练范式，但需白盒访问。CSD 的黑盒定位与其形成互补，实验中作为 open-weight-only baseline 是合理的。
- [RBD](https://arxiv.org/abs/2505.17100) (NeurIPS 2025): Plug-in reasoning-based bias detector，+18.5% accuracy。在 prompt 层面操作，不分解具体 style 维度。CSD 的 per-axis 分解和因果估计提供了更细粒度的理解。
- [Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475) (ICLR 2025) & [Post-hoc Reward Calibration](https://arxiv.org/abs/2409.17407) (ICLR 2025): 观察性回归方法，单维度（length），低成本。CSD 的多维因果方法是对这类方法的自然升级，但需要证明额外计算开销值得。
- [Robust Reward Modeling via Causal Rubrics (CROME)](https://arxiv.org/abs/2506.16507) (ICML 2025): 因果增广训练 reward model，+5.4% RewardBench accuracy。需白盒训练。
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/abs/2512.19908) (arXiv 2025.12): 用 LLM 反事实重写 + Bradley-Terry 量化修辞风格效应，方法论上与 CSD 的反事实生成高度相关，但只量化不修正。CSD 可被视为将该方法扩展到 debiasing。
- [Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings](https://arxiv.org/abs/2601.01511) (arXiv 2026.01): DML + text embeddings 用于因果推断，验证了 DML 在 NLP 场景中的适用性。

- **调研总结**: LLM-as-a-Judge 的 style bias 是一个高度活跃的研究领域，2025–2026 年产出了大量相关工作。现有方法要么需要白盒访问（FairJudge、CROME、CoLD），要么局限于单维度观察性回归（LC-AlpacaEval），要么停留在 prompt 工程（RBD、Soumik），要么只提供可解释性但不修正分数（RATE）。CSD 提出的"黑盒 + 多维因果 + 分数修正"的组合确实填补了一个真实的方法论空白，novelty claim 基本成立。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇思考深入、准备充分的 proposal。作者对领域现状有全面的了解，gap 的定位精准——black-box + multi-dimensional + causal + score correction 的组合确实没有被现有工作覆盖。方法设计有明确的理论动机（DML 的 doubly-robust 性质解决 imperfect counterfactual 问题），实验方案异常详尽。我的倾向是 **weak accept / borderline accept**——方向对、方法合理、实验设计扎实，但需要关注几个关键风险点能否在执行中妥善处理。

【核心贡献】:
核心贡献是提出了一个 dual-layer causal identification framework（counterfactual intervention + DML）用于黑盒 LLM judge 的多维 style debiasing。这个贡献的价值体现在三个层面：
1. **方法论贡献**：将因果推断中的 DML 框架与 NLP counterfactual generation 结合，提供了比观察性回归更有理论保证的 debiasing 方案。
2. **实用贡献**：黑盒适用性意味着可以直接应用于 GPT-4o、Claude 等商业 API，这是白盒方法无法做到的。
3. **概念贡献**：legitimacy-aware α 参数引入了"style 影响中哪些是 bias、哪些是 signal"的区分，这是一个真实且被忽视的问题——CASSE 已经指出 style removal 有 unintended side effects。

对领域的价值：中等偏高。Style bias 是 LLM 评估中的实际痛点，CSD 提供了一个有原则的解决方案。ISE metric 如果被社区采纳，有潜力成为标准化的 bias 报告工具。

【方法合理性】:
方法整体合理，有几个值得审视的点：

**合理之处**：
- DML 用于吸收 imperfect counterfactual 带来的残差内容泄露，这个动机清晰且有理论支撑。相比 RATE 的 double-rewrite（~25x），DML 是一个更经济的替代方案。
- Content preservation gates（BERTScore + NLI）+ DML 的 dual-layer 设计确实比单独使用任何一层更 robust。
- 3 个 style axis 的选择有文献支持（SOS-Bench, CASSE）。

**需要审视的点**：
1. **DML 理论保证的适用性**：Chernozhukov et al. (2018) 的 DML 假设 i.i.d. 数据。CSD 的数据是 paired（original + 6 counterfactuals），数据点之间存在依赖关系。√n-consistency 和 doubly-robust 性质是否在这种 paired 数据结构下仍然成立，需要更严格的论证。这是审稿人很可能追问的点。
2. **更简单的替代方案**：Multi-Reg（多维观察性回归）是一个非常强的 baseline。如果 Multi-Reg 已经能捕获大部分 style 效应，CSD 的 7x 额外开销是否值得？这需要实验来回答。
3. **α calibration 的 leave-one-benchmark-out 方法**有 overfitting 风险，尤其在只有 5 个 benchmarks 的情况下。

**总体判断**：方法设计有明确的理论动机和实践价值，但几个理论细节需要在论文中谨慎处理。没有致命缺陷。

【5 维度打分】:
  1. 研究问题: 【强】— Style bias 在 LLM judges 中是一个被广泛验证的严重问题（Soumik 量化为 0.76–0.92），且 Preference Leakage (ICLR 2026) 证明了其下游传播效应。Black-box multi-dimensional causal debiasing 是一个真实的未解决 gap，研究价值明确。

  2. 方法与创新: 【中偏强】— 将 DML 与 counterfactual intervention 结合用于黑盒 judge debiasing 是新颖的，填补了 RATE（只解释不修正，25x 开销）和 LC-AlpacaEval（观察性，单维度）之间的空白。Legitimacy-aware α 是一个概念创新。但核心组件（counterfactual rewriting、DML、style 分解）各自都不新——novelty 在于组合而非基础方法论突破。RATE (ICML 2025) 和 Counterfactual Style Measurement (arXiv 2512.19908) 已经建立了 counterfactual rewriting 用于 style 效应估计的范式，CSD 的增量贡献在于 DML 层和 score correction。

  3. 实验设计: 【强】— 这是 proposal 最突出的部分。5 judges × 5 benchmarks × 8 baselines 的矩阵覆盖非常全面。Baselines 选择精当：包含了 compute-normalized 对照（7-Call Majority Vote）、同-causal-family 对照（RATE-corrected）、最佳 observational 对照（Multi-Reg）、最佳 prompt 对照（Soumik）。9 项 ablations 涵盖了所有关键假设。Human evaluation 设计遵循最佳实践（stratified sampling、counterfactual quality audit、inter-annotator agreement）。统计分析（bootstrap、Fisher r-to-z、DML standard errors）完备。与 LC-AlpacaEval (ICLR 2025) 和 RATE (ICML 2025) 的实验设计标准相比，本 proposal 达标甚至超标。

  4. 可行性: 【中】— 方案技术上可行，但有几个执行风险：(a) 高质量 counterfactual generation 是整个方法的基础，BERTScore ≥ 0.92 + NLI ≥ 0.95 的 gate 能否真正保证 content preservation 有待验证；(b) 5 judges × 5 benchmarks × 8 baselines 的实验矩阵规模很大，API 调用成本不低（尤其 GPT-4o 和 Claude Sonnet 4）；(c) DML 的 5-fold cross-fitting 在较小 benchmarks（如 MT-Bench ~80 instances）上可能面临 statistical power 问题，proposal 已承认这一点；(d) 200 responses 的人工评估需要标注资源。整体可行但需要充足的计算和人力预算。

  5. 写作与呈现: 【强】— Proposal 逻辑清晰，从 problem → gap → method → experiment 的叙事链完整。Related work 的分类（training-based, observational, perturbation-based, reasoning-based, statistical, prompt-engineering, white-box causal）系统且全面。方法动机的论证（为什么需要 DML on top of counterfactual intervention）有说服力。公式表达简洁准确。唯一小瑕疵是篇幅偏长，正式论文需要精简。

【概率估计】: [32% - 48%] 中位 40%

【估计理由】:
推理过程如下：

**上行因素**（推高概率的因素）：
- 研究问题精准命中当前热点，且有 Preference Leakage (ICLR 2026) 等工作支撑其重要性
- Gap 定位清晰且确实存在——黑盒多维因果 debiasing 目前无人做
- 实验设计异常完备，8 baselines + 9 ablations + human eval + statistical analysis，远超平均 proposal 的实验规划
- 方法有理论动机且与 RATE 的方法论差异清晰
- Legitimacy-aware α 是一个真正的概念贡献

**下行因素**（压低概率的因素）：
- Novelty 主要在组合而非基础创新——counterfactual rewriting、DML、style 分解各自都是已有技术
- 7x 推理开销 vs. Multi-Reg 的 1x，如果性能提升不够显著，cost-effectiveness 会被质疑
- DML 在 paired/dependent 数据上的理论保证需要更严格论证
- 3 axis 的覆盖率可能不足——如果 axis coverage ablation 显示 3 axes 只解释了 <50% 的 style variance，整个方法的效用会打折
- 竞争激烈：RBD (NeurIPS 2025)、FairJudge、Soumik 等同期工作很多，审稿人可能已经 review fatigue

**总体判断**：这是一篇 "solid but not exceptional" 的 proposal。方向正确、方法合理、实验充分，属于 "above average submission" 但不是 "must accept"。在 EMNLP 2026 的竞争中，预计处于 borderline 区域，最终结果很大程度取决于实验执行质量和审稿人匹配。

【主要风险】:
1. **Marginal empirical gains over simpler baselines**: 如果 CSD 相比 Multi-Reg（1x cost）的提升不够显著（例如 <2-3pp accuracy），审稿人会质疑 7x 开销的合理性。这是最大的风险——方法再有理论美感，如果"贵了 7 倍但只好了一点"，说服力大减。
2. **DML 理论保证在 paired data 下的适用性**: Chernozhukov et al. (2018) 的标准 DML 理论假设 i.i.d. 观测。CSD 的 counterfactual pairs 引入了观测间的依赖结构。如果审稿人要求严格证明 √n-consistency 在此设定下仍成立，而论文没有给出令人满意的回答，这会成为一个 methodological weakness。

【实施评估】:
  - 计算资源: 中高。5 judges 中包含 GPT-4o、Claude Sonnet 4、Gemini 2.5 Pro 三个商业 API，每个 response 需要 7 次 judge call + counterfactual generation call。估算 5 benchmarks × ~1000 instances × 7 calls × 5 judges ≈ 175K API calls（仅 main experiments），加上 ablations 和 baselines 可能达到 300K+。API 费用预估 $2,000–$5,000。
  - 数据需求: 低。所有 5 个 benchmarks 均为公开数据集。
  - 人工介入: 中。200 responses × 3 annotators 的质量评估 + 100–150 counterfactual pairs × annotators 的质量审计。需要招募和管理标注团队，确保 Krippendorff's α ≥ 0.6。
  - 训练需求: 低。CSD 本身不需要训练。DML 的 nuisance function 用 gradient-boosted trees，训练量可忽略。Qwen3-32B 作为 rewriter 需要推理能力但不需要微调。FairJudge baseline 需要训练但可使用作者释出的模型。
  - 新 Benchmark: 无。使用现有 benchmarks。ISE metric 是新提出的诊断指标但不需要新数据。
  - 预估周期: 2.5–4 个月。Counterfactual generation + validation (2–3 weeks), main experiments (2–3 weeks, 受 API rate limit 影响), ablations (2–3 weeks), human evaluation (3–4 weeks including annotation setup), analysis + writing (3–4 weeks)。若资源充足，并行化可压缩至 2.5 个月。
```

Sources:
- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals](https://arxiv.org/abs/2410.11348)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://arxiv.org/abs/2502.01534)
- [Judging the Judges (Soumik)](https://arxiv.org/abs/2604.23178)
- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/abs/2602.06625)
- [RBD: Any Large Language Model Can Be a Reliable Judge](https://arxiv.org/abs/2505.17100)
- [Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475)
- [Post-hoc Reward Calibration](https://arxiv.org/abs/2409.17407)
- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507)
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/abs/2512.19908)
- [Reading Between the Lines: Deconfounding Causal Estimates using Text Embeddings](https://arxiv.org/abs/2601.01511)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

```
【阶段】: Triage

【领域调研】:
- [SOS-Bench / Style Outweighs Substance] (arXiv:2409.15268): 直接动机论文，证明surface-level style features在LLM judge评分中主导substance。CSD的核心问题设置直接源于此发现。
- [CASSE] (arXiv:2601.10809): 识别12个交叉关联的style features，核心发现是style features高度entangled而非正交。CSD的3-axis设计需回应此发现，proposal中已纳入coverage分析和相关性检验作为ablation。
- [Preference Leakage] (ICLR 2026, arXiv:2502.01534): 证明style bias通过judge→reward model→policy model的pipeline传播。为CSD提供了beyond evaluation的更广泛动机。
- [Soumik / Judging the Judges] (arXiv:2604.23178): 量化style bias 0.76-0.92远超position bias ≤0.04，评估9种prompt策略，最佳仅+7-11pp。确认prompt-based方法ceiling较低。
- [RATE] (ICML 2025, arXiv:2410.11348): 最直接的方法论竞争者。使用double-rewrite协议处理imperfect counterfactuals，但25x成本且不产生corrected scores。CSD用DML替代double-rewrite，7x成本且产生可用的debiased scores——这是清晰的差异化。
- [LC-AlpacaEval] (ICLR 2025, arXiv:2404.04475): 通过logistic regression debias length效应，将AlpacaEval与Chat Arena的相关性从0.93提升至0.98。方法简单有效但限于单维度、observational。CSD在方法论上是其multi-dimensional causal generalization。
- [FairJudge] (arXiv:2602.06625): SFT→DPO→GRPO三阶段训练debiased judge。需white-box access，无法用于proprietary models。与CSD互补而非竞争。
- [Causal Rubrics / CROME] (ICML 2025, arXiv:2506.16507): 用causal augmentations训练robust reward models，RewardBench +5.4%。训练时white-box方法，与CSD的black-box post-hoc定位不同。
- [BBE / Bias-Bounded Evaluation] (arXiv:2603.05485): DP-inspired noise injection提供formal bias bounds，但destruction of signal alongside bias。CSD的targeted intervention approach更精细。
- [RBD] (NeurIPS 2025, arXiv:2505.17100): Prompt-level reasoning-based bias detection +18.5%准确率。不disentangle具体style维度，与CSD互补。
- [Counterfactual LLM-based Style Measurement] (arXiv:2512.19908): 证明LLM-generated counterfactuals + Bradley-Terry可量化rhetorical style effects，250K+ counterfactuals on 8,485 ICLR papers。验证了counterfactual rewriting在style measurement中的可行性，但不做correction。
- [Causal Inference-Time Intervention for Reward Models] (arXiv:2604.27495): 在neuron level做Bradley-Terry reward model的causal decomposition。White-box方法，不适用于proprietary judge APIs。
- [CoLD] (arXiv:2507.15698): Counterfactual reasoning for length debiasing of process reward models。训练时、单维度、white-box限制。
- [Reading Between the Lines] (arXiv:2601.01511): Neural Network-Enhanced DML framework leveraging text embeddings for causal identification。证明DML+text embeddings在NLP因果推断中的可行性，但未应用于LLM judge debiasing。

- **调研总结**: LLM judge style bias是2025-2026年高度活跃的研究方向，已有大量工作从不同角度攻击这一问题。但现有方法明确分为两类：(1) white-box causal方法（Causal Rubrics, CoLD, Causal Inference-Time Intervention）效果好但无法用于proprietary judges；(2) black-box方法要么是observational/prompt-based（LC-AlpacaEval, RBD, Soumik）缺乏causal rigor，要么只做explainability不做correction（RATE）。CSD填补的"black-box + multi-dimensional + causal + post-hoc correction"这一交叉空位确实存在，且不是trivial extension——将DML引入counterfactual intervention框架需要非平凡的方法论设计。

【整体印象】: 
作为审稿人，这是一份让人印象深刻的proposal。第一反应是倾向于weak accept。原因：(1) 问题动机极其清晰，有大量实证文献支撑style bias的严重性；(2) 方法定位精准——"black-box + causal + multi-dimensional + post-hoc"是一个真实且有价值的空位；(3) 将DML框架与counterfactual intervention结合的dual-layer设计是一个有技术深度的贡献，不是简单拼凑；(4) 实验设计的完备程度远超一般proposal（5 judges × 5 benchmarks × 8 baselines × 9 ablations + human eval + counterfactual quality audit），这显示了对审稿过程的深入理解；(5) legitimacy-aware α correction是一个genuine conceptual advance。

主要的审稿顾虑集中在：(a) DML的partially linear model假设在LLM judge scoring这种高度非线性场景下是否成立；(b) 3个style axis是否足以cover主要的style variation（尽管已有ablation计划）；(c) 实际debiasing gains相对于simpler baselines（如Multi-Reg）的边际提升是否足够显著以justify 7x的inference cost。

【核心贡献】: 
核心贡献是提出了第一个适用于black-box LLM judges的multi-dimensional causal debiasing框架。具体而言：
1. **Dual-layer causal identification**（counterfactual intervention + DML）是方法论上的主要创新。相比RATE的double-rewrite（25x成本），CSD用DML nuisance absorption（7x成本）解决imperfect counterfactual问题，并提供了formal semiparametric efficiency guarantees。
2. **Legitimacy-aware correction**（α parameter）是概念上的贡献——不是所有style influence都是bias，区分bias vs. legitimate signal是prior work普遍忽略的问题。
3. **ISE metric** 作为standardized causal bias diagnostic有一定社区价值。

这些贡献对领域价值较高：LLM-as-judge是当前评估基础设施的核心组件，其bias直接影响RLHF/DPO pipeline。一个principled、practical的debiasing方法有广泛的应用价值。

【方法合理性】: 
方法整体合理，但有几个需要注意的点：

**合理之处**：
- Counterfactual intervention是估计causal effects的gold standard approach。用LLM rewrite生成counterfactuals已被RATE和arXiv:2512.19908验证可行。
- DML作为second layer处理imperfect counterfactuals是合理的——这比RATE的double-rewrite在理论上更优雅（有formal guarantees），在成本上更优（7x vs 25x）。
- Content preservation gates（BERTScore ≥ 0.92 + NLI ≥ 0.95）是标准做法。
- 3-axis选择（formality, verbosity, formatting）有SOS-Bench和CASSE的实证支持。

**潜在问题**：
- DML假设Score = β_d · Style_d + g(Content, Style_{-d}) + ε，这是partially linear model。如果style effect是非线性的（例如moderate formality最优，过高或过低都有penalty），线性β_d可能miss真实的effect structure。Proposal未讨论非线性extension。
- Rewriter confounding的处理虽然提到了independence principle（当judge = Qwen3-32B时换用Llama rewriter），但更微妙的问题是：不同rewriter可能引入不同的rewrite artifacts，这些artifacts本身可能被judge系统性偏好。Cross-rewriter consistency ablation可以部分检测但不能完全解决。
- α calibration用leave-one-benchmark-out cross-validation，但只有5个benchmarks，cross-validation的variance可能很高。

**更简单的替代方案**：
- Multi-Reg（多维observational regression）是最直接的简单替代。CSD需要convincingly demonstrate DML+counterfactual的边际贡献超过Multi-Reg。Proposal将Multi-Reg列为baseline，这是正确的。关键实验结果将决定方法的说服力。
- 如果Multi-Reg与CSD差距不大，审稿人可能质疑7x inference cost的必要性。

【5 维度打分】:

1. **研究问题**: 强 — Style bias在LLM judges中的严重性已被多篇高质量论文（SOS-Bench, CASSE, Preference Leakage, Soumik）充分证实，且该bias通过RLHF/DPO pipeline级联传播（Preference Leakage, ICLR 2026）。Black-box debiasing的需求在proprietary model主导评估实践的现状下尤为迫切。问题的重要性和研究价值毫无疑问。

2. **方法与创新**: 中偏强 — 将DML引入LLM judge debiasing是一个novel combination。Dual-layer设计（counterfactual + DML）相比RATE的double-rewrite是一个有技术实质的替代方案，不是trivial variation。Legitimacy-aware α是概念上的genuinely new idea。但DML本身是成熟工具（Chernozhukov 2018），counterfactual rewriting也已有先例（RATE, arXiv:2512.19908），核心创新是"组合+应用"而非fundamental methodological advance。另外，partially linear model假设是一个理论层面的limitation。相比Causal Rubrics (ICML 2025)的causal augmentation approach和RATE (ICML 2025)的double-rewrite，CSD的创新度是comparable的。

3. **实验设计**: 强 — 这是proposal最突出的优势之一。5 judges × 5 benchmarks的coverage远超领域内多数工作。8个baselines涵盖了所有主要方法类型（observational, perturbation, prompt, training, causal），且包含了compute-normalized comparison（7-Call Majority Vote）和method-normalized comparison（RATE-corrected）。9个ablations系统地覆盖了方法中每个关键design choice。Human evaluation protocol（stratified sampling + counterfactual quality audit）设计合理，Krippendorff's α target和bootstrap CI显示了统计学素养。DML robustness checks（nuisance estimator comparison, effective sample size, statistical power discussion）是审稿人常关注的技术细节。这个实验设计如果fully executed，将是非常convincing的。

4. **可行性**: 中 — 方案原则上可以执行，但有显著的资源和工程挑战：
   - 5 judges × 5 benchmarks × 7 calls/response的inference cost相当高。GPT-4o和Claude Sonnet 4的API成本不容忽视（粗估数万美元级别API调用费）。
   - 生成高质量counterfactuals需要大量rewrite + quality gate filtering + retries，pipeline工程量大。
   - Human evaluation 200 responses × 3 annotators + 100-150 counterfactual pairs需要相当的标注资源。
   - 5-fold cross-fitting DML for each style axis × each judge × each benchmark的计算量也需考虑。
   - α calibration的leave-one-benchmark-out在只有5个benchmarks时统计可靠性有限。
   整体可行但需要充足的预算和工程能力。

5. **写作与呈现**: 强 — Proposal结构清晰，逻辑链完整：Problem→Gap→Method→Experiments。每个design choice都有明确的rationale（如为什么用DML而不是simple paired differences，为什么选3个axes，为什么需要cross-rewriter consistency check）。对prior work的定位准确且公平（不strawman任何baseline）。Related work覆盖全面，包括最新的2026年论文。方法表述数学上精确。Acknowledged limitations诚实。整体呈现出对领域和审稿流程的深刻理解。

【概率估计】: [33% - 48%] 中位 40%

【估计理由】: 
这是一份高于平均水平的proposal，具备扎实的研究问题、合理的方法设计和出色的实验规划。

**向上推动的因素**：
- 研究问题高度timely且important（LLM judge bias + alignment pipeline影响）
- Gap identification准确且convincing——真正的black-box causal debiasing空位
- 实验设计的completeness在同类投稿中属于top tier
- Legitimacy-aware correction是一个genuine conceptual advance
- ISE作为standardized metric有community adoption potential
- 写作quality和scholarly rigor高

**向下拉动的因素**：
- 核心方法论创新是"组合+应用"（DML + counterfactual），非fundamental advance。审稿人可能认为技术contribution深度不足
- Partially linear model假设可能oversimplify style-score关系，审稿人可能challenge
- 如果Multi-Reg baseline表现接近CSD，整个方法的value proposition（7x cost for how much gain?）会被严重质疑
- α calibration在5个benchmarks上的statistical reliability是一个实际风险
- 3-axis coverage的完备性虽有ablation，但如果coverage很低（如仅解释30%的style variance），整个方法的practical value会打折扣
- 这是一个proposal，最终结果的强弱（DML vs Multi-Reg的margin, coverage fraction等）将决定上下限

**综合判断**：EMNLP 2026近年录取率约22-25%。此proposal在研究问题和实验设计上显著高于average submission，方法创新度属于solid但非outstanding。如果实验结果如预期（DML显著优于observational baselines, 3-axis coverage合理, human eval confirms debiasing quality），估计在weak accept/borderline区间，中位约40%。若实验结果不如预期（如DML与Multi-Reg差异不显著），概率会降至25-30%。

【主要风险】: 
1. **DML vs. simpler baselines的边际收益不显著**：如果Multi-Reg（多维observational regression，0额外cost）的debiasing效果接近CSD（7x cost），审稿人会质疑整个causal identification的必要性。这是最可能导致rejection的单一风险——"interesting framework but the simpler baseline works just as well"。
2. **3-axis coverage不足**：如果formality + verbosity + formatting仅解释了judge score variance中较小的fraction（如<40%），残余的unexplained style bias会显著削弱方法的practical value，审稿人可能认为"partial solution to a large problem" insufficient for acceptance。

【实施评估】:
  - 计算资源: 高。5个proprietary judge API × 7 calls/response × 5 benchmarks = 大量API调用。粗估：假设每个benchmark平均500-1000 instances，总共约5 × 7 × 5 × 750 ≈ 131,250次judge API调用（不含rewrite calls和retries）。GPT-4o和Claude的cost估计在$5K-$15K范围。rewriter（Qwen3-32B）可用开源部署降低成本。
  - 数据需求: 中。5个benchmarks均为publicly available（SOS-Bench, RewardBench, RewardBench 2, MT-Bench, Arena-Hard-Auto）。不需要构建新数据集，但需要大规模生成counterfactuals并进行quality filtering。
  - 人工介入: 中。Human evaluation需要200 responses × 3 annotators + 100-150 counterfactual quality audit pairs × annotators。估计需要600-1000个human annotation units。需要设计详细的annotation rubric和training annotators。
  - 训练需求: 低。CSD本身是post-hoc方法，不需要训练LLM。DML的nuisance function（gradient-boosted trees）训练量极小。FairJudge baseline需要复现其训练，但该工作如有released model可直接使用。
  - 新 Benchmark: 无。完全使用existing benchmarks。
  - 预估周期: 3-4个月。Breakdown：Pipeline工程+counterfactual生成（3-4周）→ API judge调用+data collection（2-3周，可能受rate limits影响）→ DML estimation+analysis（1-2周）→ Human evaluation recruitment+execution（3-4周）→ Ablations+additional experiments（2-3周）→ Writing（3-4周）。如果一人全职约4个月；2-3人团队约2.5-3个月。
```

Sources:
- [SOS-Bench: Style Outweighs Substance](https://arxiv.org/pdf/2409.15268)
- [Judging the Judges: Systematic Evaluation of Bias Mitigation](https://arxiv.org/abs/2604.23178)
- [RATE: Causal Explainability of Reward Models](https://arxiv.org/abs/2410.11348)
- [Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475)
- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/abs/2602.06625)
- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507)
- [CROME: Robust Reward Modeling via Causal Data Augmentation](https://arxiv.org/html/2604.13833)
- [Preference Leakage: A Contamination Problem](https://arxiv.org/pdf/2502.01534)
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://arxiv.org/html/2512.19908v1)
- [Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/html/2604.27495)
- [A Survey on LLM-as-a-Judge](https://arxiv.org/html/2411.15594v6)
- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation](https://arxiv.org/pdf/2603.05485)
- [RBD: Debiasing with a Reasoning-based Bias Detector](https://openreview.net/forum?id=sLNz60fJFF)
- [Reading Between the Lines: DML with Text Embeddings](https://arxiv.org/pdf/2601.01511)
- [Evaluating Scoring Bias in LLM-as-a-Judge](https://arxiv.org/html/2506.22316v1)


【原始 proposal（允许参考但不是主要依据）】:
## Causal Style Decomposition for Debiasing Black-Box LLM Judges

### 1. Problem and Motivation

LLM-as-a-Judge pipelines are increasingly used for automated evaluation, but suffer from systematic style biases. SOS-Bench (arXiv:2409.15268) demonstrates that surface-level style features dominate substance in judge scoring. CASSE (arXiv:2601.10809) identifies 12 cross-correlated style features inducing evaluation side effects, with the core finding that style features are deeply entangled rather than orthogonal. Preference Leakage (ICLR 2026, arXiv:2502.01534) shows style-driven contamination propagates through training pipelines—from judge preferences to reward models to policy models. Soumik (arXiv:2604.23178) quantifies style bias at 0.76–0.92 across 5 judges, far exceeding position bias (≤0.04). Earlier work on LLM evaluation bias (NAACL 2024) and RubricBench (arXiv:2603.01562) further document how surface features mislead judges, revealing a 27% accuracy gap between model-generated and human rubrics on hard samples with misleading surface bias.

Crucially, this is not merely an evaluation problem. Preference Leakage (ICLR 2026) demonstrates that style bias in judges propagates downstream: biased preference labels enter RLHF/DPO training data, contaminating reward models and ultimately policy models. Debiasing judges at the evaluation stage therefore has cascading benefits for the entire LLM alignment pipeline.

Existing debiasing approaches each have fundamental limitations:

- **Training-based**: FairJudge (arXiv:2602.06625) uses SFT→DPO→GRPO to retrain judges, requiring white-box access and per-judge retraining, inapplicable to proprietary models.
- **Observational regression**: Length-Controlled AlpacaEval (ICLR 2025, arXiv:2404.04475) regresses out length effects at zero cost; Post-hoc Reward Calibration (ICLR 2025, arXiv:2409.17407) extends this via locally weighted regression across 33 reward models. Both handle only a single dimension and rely on observational associations that conflate genuine quality correlates with spurious confounding.
- **Perturbation-based**: Bias-Bounded Evaluation (BBE, arXiv:2603.05485) injects DP-inspired Gaussian noise for formal bias bounds but destroys signal alongside bias; RATE (ICML 2025, arXiv:2410.11348) uses a double-rewrite protocol for causal explainability of reward models, providing the key insight that single-rewrite counterfactuals are imperfect and introduce substantial bias, but requires ~25x inference overhead and does not produce corrected scores.
- **Reasoning-based**: RBD (NeurIPS 2025, arXiv:2505.17100) is a plug-in module that detects biased evaluations and guides self-correction via structured reasoning (+18.5% accuracy), but operates at the prompt level without disentangling specific style dimensions.
- **Statistical**: PRECISE (AAAI 2026, arXiv:2601.18777) extends prediction-powered inference to combine human annotations with LLM judgments for debiased ranking estimation, but requires human labels and does not identify which style dimensions drive bias.
- **Prompt-engineering**: Soumik (arXiv:2604.23178) evaluates 9 prompt-based strategies; the best ("combined budget") achieves +7.2 to +11.2pp on select model-strategy pairs.

A parallel line of causal approaches targets reward model debiasing, all requiring white-box access or training-time intervention: Causally Motivated Inference-Time Intervention (arXiv:2604.27495) decomposes Bradley-Terry reward models via total effect / controlled direct effect and intervenes at the neuron level. CROME (arXiv:2604.13833) uses causal data augmentation to suppress prompt-independent shortcuts. Causal Rubrics (arXiv:2506.16507, ICML 2025) employs causal augmentations (pairs isolating causal attribute changes) and neutral augmentations (tie-labeled pairs varying spurious attributes) to train robust reward models, improving RewardBench accuracy by up to 5.4%. CoLD (arXiv:2507.15698) applies counterfactual reasoning and causal graph analysis for length debiasing of process reward models, but is limited to training-time, single-dimension (length), and white-box settings. Causal Reward Modeling (CRM; ICLR 2027, arXiv:2501.09620) enforces counterfactual invariance in reward predictions. CMBE (AAAI 2027, arXiv:2505.16522) proposes simultaneous multi-bias causal effect estimation and elimination.

Separately, counterfactual LLM-based style measurement (arXiv:2512.19908) demonstrates that LLM-generated counterfactual rewrites combined with Bradley-Terry aggregation can robustly quantify rhetorical style effects at scale (>250K counterfactuals on 8,485 ICLR papers)—but quantifies style without correcting for it.

Foundational work on causal effects of linguistic properties (Pryzant et al., NAACL 2021) established methods for estimating causal effects of text attributes using distant supervision and pre-trained language models, providing the methodological precedent for CSD's approach.

**The open gap**: No existing method provides principled, multi-dimensional causal debiasing for black-box LLM judges while preserving legitimate style-quality associations. White-box causal methods (Causal Rubrics, CoLD, arXiv:2604.27495) cannot be applied to proprietary judge APIs. Black-box methods remain limited to observational regression (LC-AlpacaEval) or prompt engineering (RBD, Soumik). CSD fills this gap by bridging two independently developing literatures: (1) the NLP evaluation community's empirical documentation of style biases with ad-hoc fixes, and (2) the causal inference / econometrics community's principled frameworks (Double Machine Learning; Chernozhukov et al. 2018) that have not yet been systematically applied to black-box LLM judge debiasing.

### 2. Core Contributions

1. **Causal Style Decomposition (CSD) framework**: A black-box, post-hoc method that decomposes LLM judge scores into content-driven and style-driven components via targeted counterfactual interventions along three style axes, using a dual-layer causal identification strategy: counterfactual intervention for first-stage identification, DML (Chernozhukov et al. 2018) for second-stage robustness against imperfect counterfactuals.

2. **Legitimacy-aware correction**: Unlike all prior debiasing methods that implicitly assume style effects should be fully removed, CSD introduces a domain-conditional α parameter distinguishing domain-invariant style bias from domain-specific legitimate style-quality associations—addressing CASSE's (arXiv:2601.10809) finding that style removal has unintended side effects. This is a conceptual advance: the question is not just "how much style bias exists" but "which portion of style influence is bias vs. signal."

3. **Interventional Style Effect (ISE) metric**: A standardized, causal diagnostic for per-axis judge bias auditing. Unlike observational bias scores (e.g., Soumik's style bias metric of 0.76–0.92), ISE measures interventional causal sensitivity, enabling principled cross-judge comparison ("GPT-4o's formality ISE is 2.3× Claude's"), cross-domain analysis, and version-tracking of judge bias. ISE has potential as a community-standard bias reporting metric analogous to FID for image generation.

4. **Empirical validation** across 5 judges × 5 benchmarks with 8 baselines, comprehensive ablations, compute-normalized comparisons, counterfactual quality auditing, and human evaluation.

### 3. Method

#### 3.1 Counterfactual Style Generation

For each response $r$, generate 6 counterfactuals by intervening on 3 style axes in 2 directions each:
- **Formality**: formal ↔ informal tone (preserving content)
- **Verbosity**: concise ↔ verbose (preserving information content)
- **Formatting**: heavy markdown/structure ↔ plain text

Rewriter: Qwen3-32B (default). When the target judge is Qwen3-32B, use an independent rewriter (Llama-3.3-70B) to prevent rewriter-evaluator confounding, following the independence principle in RATE (ICML 2025, arXiv:2410.11348).

**Content preservation gates**: Counterfactuals must pass BERTScore ≥ 0.92 AND NLI entailment score ≥ 0.95 relative to the original. Failing samples are re-generated (up to 3 retries) or excluded.

**Three-axis design rationale**: Formality, verbosity, and formatting capture the dominant style variation documented in SOS-Bench (arXiv:2409.15268) and CASSE (arXiv:2601.10809). We treat their approximate independence as an empirical hypothesis to be verified (via correlation analysis of ISE estimates across axes), not an a priori assumption—important given CASSE's finding of style feature entanglement. Coverage analysis (fraction of total style variance these 3 axes explain) is included as an ablation. The framework extends to additional axes at linear cost.

#### 3.2 Dual-Layer Causal Identification via DML

**Why DML on top of counterfactual intervention?** A natural question is: given paired data (original + 6 counterfactuals), why not simply compute mean paired score differences as ATE estimates? The answer is that content preservation gates (BERTScore ≥ 0.92, NLI ≥ 0.95) are imperfect—residual content leakage inevitably passes through. RATE (ICML 2025, arXiv:2410.11348) demonstrated that imperfect counterfactuals introduce substantial bias in causal estimates, solving this via a double-rewrite protocol (rewriting the rewrite to cancel rewrite-induced bias). CSD takes an alternative approach with stronger theoretical guarantees:

- **First layer (counterfactual intervention)**: Provides approximate do-calculus identification by actively manipulating style while holding content approximately fixed.
- **Second layer (DML)**: The nuisance function $g(Content, Style_{-d})$ captures and partials out residual content variation that leaked through imperfect gates, providing doubly-robust, $\sqrt{n}$-consistent estimation even if either the treatment or outcome model is misspecified.

This dual-layer design means CSD is robust to the imperfect-counterfactual problem that RATE solves via double-rewrite, but at ~7x inference cost (vs. RATE's ~25x) and with formal semiparametric efficiency guarantees.

For each style axis $d \in \{formality, verbosity, formatting\}$, estimate the causal effect $\beta_d$:

$$Score = \beta_d \cdot Style_d + g(Content, Style_{-d}) + \epsilon$$

where $g(\cdot)$ is estimated via gradient-boosted trees with 5-fold cross-fitting per Chernozhukov et al. (2018). Building on the causal identification logic of Pryzant et al. (NAACL 2021), this framework estimates the direct causal effect of each style dimension on judge scores while controlling for content quality and other style axes.

#### 3.3 Legitimacy-Aware Correction

$$Score_{debiased} = Score_{original} - \sum_{d} (1 - \alpha_d) \cdot \hat{\beta}_d \cdot (Style_d - Style_{ref})$$

where $\alpha_d \in [0,1]$ is domain-conditional. $\alpha_d = 0$: full debiasing; $\alpha_d = 1$: no debiasing.

**α calibration protocol**: Leave-one-benchmark-out cross-validation. Sensitivity analysis reports performance across α ∈ {0.0, 0.1, ..., 1.0}.

#### 3.4 Format Adaptation

CSD adapts to different evaluation formats: (a) **Pointwise** (MT-Bench): debias each response's score independently; (b) **Pairwise** (Arena-Hard-Auto, SOS-Bench): debias both chosen and rejected responses, then re-rank; (c) **Multi-choice** (RewardBench, RewardBench 2): debias each candidate's score independently, then select the highest-scoring candidate. Inference cost scales with the number of candidates per instance.

#### 3.5 Inference Cost

CSD requires 7 judge calls per response (1 original + 6 counterfactuals), ~7x overhead. This compares favorably to RATE's ~25x, while providing actionable score correction rather than only explainability.

### 4. Experimental Design

#### 4.1 Judges (5)

GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Qwen3-32B, Llama-4-Maverick. Covers 4 provider families and both proprietary and open-weight models.

#### 4.2 Benchmarks (5)

- **SOS-Bench** (arXiv:2409.15268): Style-substance separation evaluation
- **RewardBench**: Standard reward model evaluation
- **RewardBench 2** (arXiv:2506.01937): Updated with factuality and precise instruction following domains
- **MT-Bench**: Multi-turn dialogue quality
- **Arena-Hard-Auto**: Challenging single-turn evaluation

#### 4.3 Baselines (8)

| Baseline | Type | Extra cost | Applicability |
|---|---|---|---|
| Raw Judge | No debiasing | 1x | All judges |
| LC-AlpacaEval (ICLR 2025, arXiv:2404.04475) | Single-dim observational regression | 1x | All judges |
| Multi-Reg | Multi-dim observational regression | 1x | All judges |
| BBE (arXiv:2603.05485) | DP noise injection | 1x | All judges |
| Prompt-Debiasing (Soumik, arXiv:2604.23178) | Combined budget prompt strategy | 1x | All judges |
| RATE-corrected (ICML 2025, arXiv:2410.11348) | Double-rewrite causal estimation + CSD-style correction | ~25x | All judges |
| FairJudge (arXiv:2602.06625) | Training-based (SFT→DPO→GRPO) | 1x post-train | Open-weight only |
| 7-Call Majority Vote | Same-budget sampling | 7x | All judges |

Multi-Reg uses automated style feature extractors (markdown density, word count, Flesch-Kincaid readability) as covariates for multivariate regression—the most direct observational alternative to CSD. RATE-corrected applies RATE's double-rewrite causal estimates with CSD's correction formula, enabling direct comparison of the two causal identification strategies at different compute budgets. 7-Call Majority Vote controls for inference budget fairness. Results tables clearly distinguish all-judge-applicable baselines from open-weight-only methods (FairJudge) to avoid misleading comparison.

#### 4.4 Metrics

- **Primary**: Pairwise accuracy, Spearman/Kendall-τ correlation with ground-truth quality
- **Diagnostic**: ISE per axis per judge (causal bias magnitude)
- **Efficiency**: Accuracy-per-judge-call curve (1x, 3x, 5x, 7x, 25x budget)

#### 4.5 Ablations

1. **Decomposition method**: Linear regression vs. DML vs. nonparametric kernel estimation for β
2. **Per-axis importance**: Single-axis (3 runs) + pairwise combinations (3 runs) + full 3-axis
3. **Content preservation thresholds**: BERTScore ∈ {0.85, 0.88, 0.90, 0.92, 0.95} × NLI ∈ {0.90, 0.93, 0.95, 0.97}
4. **Cross-rewriter consistency**: ISE and accuracy using Qwen3-32B vs. Llama-3.3-70B vs. Claude as rewriter
5. **Axis coverage**: Variance decomposition—fraction of judge score variance explained by 3 axes vs. residual
6. **α sensitivity**: Full grid α ∈ [0,1], per-domain performance landscape
7. **ISE-based cross-judge comparison**: ISE estimates across judges and domains
8. **Manipulation check**: Per-axis style metric effect sizes (Cohen's d) on automated proxies—formality → Flesch-Kincaid / formality classifier; verbosity → word count ratio; formatting → markdown element density. Validates that counterfactual interventions produce sufficient style variation for reliable ISE estimation.
9. **DML robustness check** (supplementary): Nuisance estimator comparison (GBT vs. Random Forest vs. Lasso), per-cell effective sample size, and DML standard error analysis. Discussion of statistical power for smaller benchmarks (e.g., MT-Bench ~80 multi-turn dialogues).

#### 4.6 Human Evaluation

**Quality evaluation (200 responses)**: Stratified by divergence between CSD and raw judge rankings—sampled from top-20% (high divergence), middle 40%, and bottom 40% by divergence magnitude. 3 annotators per response, 5-point Likert scale evaluating content quality and presentation quality independently. Inter-annotator agreement target: Krippendorff's α ≥ 0.6, reported with bootstrap 95% CI. Annotation rubric includes operationalized definitions and anchor examples, following RubricBench (arXiv:2603.01562) best practices.

**Counterfactual quality audit (100–150 pairs)**: ~50 per style axis, annotators judge: (1) whether target axis was successfully changed (binary), (2) whether non-target axes were unintentionally changed (Likert 1–5), (3) whether content semantics were preserved (Likert 1–5). Report Cohen's κ between automated gates (BERTScore + NLI) and human judgment, plus false positive/negative rates of the automated gates. This validates CSD's core assumption of content-preserving style intervention and addresses CASSE's (arXiv:2601.10809) entanglement concern.

#### 4.7 Statistical Analysis

- Pairwise accuracy differences: paired bootstrap test (10,000 resamples), 95% CIs
- Correlation differences: Fisher r-to-z transformation for Spearman, bootstrap CIs for Kendall-τ
- DML coefficients: asymptotic standard errors and p-values per Chernozhukov et al. (2018)
- All main results include 95% confidence intervals

### 5. Expected Outcome and Broader Impact

CSD is expected to demonstrate that dual-layer causal identification (counterfactual intervention + DML) provides debiasing gains beyond observational regression (LC-AlpacaEval, Multi-Reg), perturbation methods (BBE), and prompt engineering (Soumik), particularly in domains where style-content confounding is strong. Comparison with RATE-corrected will isolate the efficiency advantage (7x vs. 25x) and compare robustness to imperfect counterfactuals (DML nuisance absorption vs. double-rewrite cancellation). The legitimacy-aware α mechanism is expected to show selective debiasing outperforms both full debiasing and no debiasing.

**Broader impact on alignment pipelines**: Beyond evaluation, CSD can serve as a data quality intervention in RLHF/DPO pipelines. Preference Leakage (ICLR 2026, arXiv:2502.01534) demonstrated that style-biased judge labels contaminate reward models and downstream policies. Applying CSD to debias preference labels before they enter training could break this contamination chain at its source. While validating this downstream effect is beyond the scope of the current experiments, the framework is directly applicable to preference data curation, and we discuss this as a concrete direction for future work.

**Acknowledged limitations**: (1) 3-axis coverage may miss residual style bias from uncovered dimensions; (2) counterfactual quality depends on rewriter capability; (3) 7x inference cost may be prohibitive for large-scale deployment, though axis-selective application reduces cost.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "02023088-acce-4a14-b1c8-996788e1a61f",
  "type": "user",
  "uuid": "142dea6e-23ef-426d-b0a0-393123b025d5",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:39:34.156Z_

```json
{
  "parentUuid": "142dea6e-23ef-426d-b0a0-393123b025d5",
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
  "uuid": "5271ad80-3137-4004-8b20-5af238f39a94",
  "timestamp": "2026-05-20T05:39:34.156Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:39:34.156Z_

```json
{
  "parentUuid": "5271ad80-3137-4004-8b20-5af238f39a94",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "88ae7232-8d49-4078-a2f0-452b0aabcef0",
  "timestamp": "2026-05-20T05:39:34.156Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a",
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
  "leafUuid": "88ae7232-8d49-4078-a2f0-452b0aabcef0",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Debias LLM judges using causal style decomposition",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:40:14.544Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully to produce a Meta Judge synthesis.

First, let me extract the key numbers and dimensions:

**Reviewer 1**: [33% - 43%] 中位 38%
**Reviewer 2**: [32% - 48%] 中位 40%
**Reviewer 3**: [33% - 48%] 中位 40%

Three midpoints: 38%, 40%, 40%
Mean: 39.3%
Median: 40%
Std: ~1.15% → Very high consistency


Now I'm looking at how the reviewers rated each dimension across the rubric. The research question and experimental design show strong consensus across all three reviewers, while the methodology and feasibility assessments are slightly more varied, with some reviewers rating them as moderately strong versus moderate. Writing and presentation are consistently rated as strong.

The key risks that emerged from all three reviewers center on the novelty being primarily a combination of existing approaches rather than a fundamental breakthrough, the marginal performance improvements between the proposed CSD method and multi-regression baselines, insufficient coverage across the three axes being evaluated, and incomplete theoretical guarantees for the DML approach. The standard deviation works out to about 0.94%, which is extremely tight — all three reviewers converged on scores in the 38-40% range. Given this high consistency, I should take the median and use a narrower interval for my final assessment.

The reviewers are aligned on the core judgment: this is a well-executed proposal with strong motivation and experimental rigor, but the novelty lies in the combination of existing techniques rather than fundamental innovation. The main uncertainty is whether the empirical results will actually justify the 7x computational cost.

Now looking at the implementation complexity assessments, the reviewers rate it as medium-high to high across the board. — consensus on significant compute needs
- Data: All say low — public datasets
- Human: All say 中 — ~600-1000 annotation units
- Training: All say low — post-hoc method
- New benchmark: All say no
- Timeline: R1 says 10-14 weeks, R2 says 2.5-4 months, R3 says 3-4 months — generally 2.5-4 months

The three reviewers show remarkably tight agreement with medians at 38%, 40%, and 40%, so I should narrow my interval around 39-40% rather than spreading wider. The most generous bound is 48% and most conservative is 32%, but given the high consistency and the principle of being conservative, I'll settle on [34% - 44%] with a median of 39%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88ae7232-8d49-4078-a2f0-452b0aabcef0",
  "isSidechain": false,
  "requestId": "req_011CbDHPJUjUZakfPKLtyuxB",
  "type": "assistant",
  "uuid": "995ff516-f044-4eba-977b-e4b9b07d6cd8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LihfSpMnwXi3JyWaPPPqx6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22765,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3892,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 22765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22765
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

_source line 9 · 2026-05-20T05:41:12.022Z_

【阶段】: Meta Judge
【三次中位】: [38%, 40%, 40%]  std=0.9%
【共识维度】:
- **研究问题: 强**（3/3）— 三位审稿人一致认为 LLM judge style bias 是经过 SOS-Bench、CASSE、Preference Leakage (ICLR 2026)、Soumik 等大量文献充分 documented 的真实且重要问题，black-box 设定切合实际需求。
- **方法与创新: 中/中偏强**（3/3）— 三位均认为核心创新在于"已有组件的组合应用"（counterfactual generation + DML + regression correction），而非 fundamental methodological advance。R1 判中，R2/R3 判中偏强，差异在于对 legitimacy-aware α 概念贡献和 dual-layer 设计技术深度的权重不同，但三人对 novelty 天花板的判断高度一致。
- **实验设计: 强**（3/3）— 三位一致认为 5 judges × 5 benchmarks × 8 baselines × 9 ablations + human eval 的设计在同类工作中属于顶级水平，特别称赞 Multi-Reg baseline（检验 causal identification 增量价值）、RATE-corrected（同 causal 策略对比）、7-Call Majority Vote（compute-normalized 对照）的设计。
- **写作与呈现: 强**（3/3）— 三位一致评价高。
- **可行性: 中**（2/3 判中，R1 判中强）— R2/R3 更关注 API 成本和标注资源的执行风险。
- **CSD vs Multi-Reg 边际收益风险**（3/3）— 三位均将此列为最大单一风险：如果 7x 成本的 CSD 相对 1x 成本的 Multi-Reg 提升不显著，整个方法的 value proposition 将被严重质疑。
- **3-axis coverage 不足风险**（3/3）— 三位均指出 CASSE 识别了 12 维度，3 轴可能覆盖不足。
- **7x 推理成本的 cost-effectiveness 质疑**（3/3）— 与 Multi-Reg 风险直接关联。

【异常维度】:
- R1 单独提出 Style_d 操作化定义不明确（scalar vs. binary），R2/R3 未提及 → 降权，但确实是方法描述的小瑕疵，建议论文中澄清
- R3 更强调 partially linear model 假设可能 oversimplify 非线性 style-score 关系（R2 轻微提及但未作为主要风险）→ 部分降权，但作为理论层面 limitation 值得在论文中 acknowledge
- R1 的可行性评分（中强）高于 R2/R3（中）→ R1 可能对资源需求估计偏乐观

【最终概率】: [33% - 44%] 中位 39%
【一致性】: 高（std=0.9%，远低于 3% 阈值；rubric 判决无严重冲突，仅在方法创新度的细分程度上有微小分歧）
【综合理由】:
三位审稿人的评估高度一致（std=0.9%），这在独立评审中极为罕见，说明 proposal 的优劣势都非常明显且容易识别：

**上行共识**：研究问题的 timeliness 和 importance 毫无争议（强×3）；实验设计的 completeness 远超 average submission（强×3）；writing quality 高（强×3）。这些因素共同构成了 solid acceptance case 的基础——这不是一篇会被轻易 desk reject 的论文。

**下行共识**：novelty 的天花板在"组合创新"而非"基础突破"（3/3 一致判断），这直接限制了概率上限。三位均认为 CSD vs Multi-Reg 的实验结果是 make-or-break 的关键——这是一个纯粹的 empirical uncertainty，在 proposal 阶段无法消除。

**区间收窄逻辑**：由于一致性极高，我将区间从三人的并集 [32%-48%] 收窄至 [33%-44%]。下界 33% 反映 novelty 天花板和 Multi-Reg 可能 tie 的下行风险；上界 44% 反映如果实验 convincing（DML 显著优于 Multi-Reg + 3-axis 覆盖合理 + α 展示跨域价值），在 EMNLP 的高 relevance 加持下有望 weak accept。中位从 40% 微调至 39%，体现"宁缺毋滥"原则——proposal 阶段的 empirical uncertainty 应偏保守估计。

**关键判断**：这是一篇典型的 "borderline but leaning positive" proposal。方向正确、方法合理、实验设计出色，但 novelty 的 incremental nature 和 empirical results 的不确定性使其落在 weak accept / borderline reject 的分水岭上。最终结果高度取决于：(1) CSD vs Multi-Reg 的边际提升幅度，(2) 3-axis coverage 的实际覆盖率，(3) 审稿人对"组合创新"的容忍度。

【建议】: 边缘（Borderline — 建议进入迭代优化，有提升空间但需关注 novelty framing 和 key risk mitigation）

【实施评估】:
  - 计算资源: 中高。5 proprietary/open-weight judges × 5 benchmarks × 7 calls/response，主实验约 130K-175K judge API 调用，加 ablations 和 baselines 达 300K+。API 费用预估 $3K-$10K（取决于 rate 和用量）。Open-weight judges（Qwen3-32B, Llama-4-Maverick）需 ≥ 2×A100 推理。Rewriter（Qwen3-32B）同样需要 GPU 推理资源。DML 训练（GBT with 5-fold cross-fitting）计算开销可忽略。
  - 数据需求: 低。5 个 benchmarks 均为公开数据集（SOS-Bench, RewardBench, RewardBench 2, MT-Bench, Arena-Hard-Auto），无需额外数据收集。需大规模生成 counterfactuals 并做 quality filtering。
  - 人工介入: 中。200 responses × 3 annotators 质量评估 + 100-150 counterfactual pairs × annotators 质量审计，总计约 800-1000 人工标注单元。需制定 annotation guidelines、anchor examples、annotator training。Krippendorff's α ≥ 0.6 目标需要一定质控投入。
  - 训练需求: 低。CSD 本身是 post-hoc inference-time 方法，无需模型训练。DML nuisance function（GBT）训练量极小。FairJudge baseline 如有 released model 可直接使用，否则需复现训练。
  - 新 Benchmark: 无。完全使用现有 benchmarks。ISE 是新提出的诊断指标但不需要新数据。
  - 预估周期: 10-16 周（2.5-4 个月）。分解：Pipeline 工程 + counterfactual 生成验证（2-3 周）→ DML 实现 + 单 cell 验证（1-2 周）→ 全矩阵实验 + baselines（2-3 周，受 API rate limit 影响）→ Ablations（2-3 周）→ Human evaluation（3-4 周含标注准备）→ 论文撰写（3-4 周，可与后期实验并行）。2-3 人团队可压缩至 2.5 个月。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "995ff516-f044-4eba-977b-e4b9b07d6cd8",
  "isSidechain": false,
  "requestId": "req_011CbDHPJUjUZakfPKLtyuxB",
  "type": "assistant",
  "uuid": "afb54efd-10be-4051-b2a7-77c7e92ce06f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LihfSpMnwXi3JyWaPPPqx6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22765,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3892,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 22765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22765
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
  "leafUuid": "afb54efd-10be-4051-b2a7-77c7e92ce06f",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Debias LLM judges using causal style decomposition",
  "sessionId": "11600e8d-eafb-49e2-9de6-aebb2f3dd81a"
}
```

---
