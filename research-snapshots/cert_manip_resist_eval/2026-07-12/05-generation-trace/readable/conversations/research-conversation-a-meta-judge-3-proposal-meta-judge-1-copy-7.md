# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/b65d38de-e0ab-4717-bbf3-128111222818.jsonl`
- **Structured JSON:** [`b126933f7a78362e584d.json`](../../sessions/b1/b126933f7a78362e584d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:30:42.835Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:30:42.835Z",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 致命前置问题：Venue Mismatch ⚠️\n\n本 proposal 被要求评估投稿 CoRL 2026（Conference on Robot Learning）的中稿潜力。\n然而，CoRL 的 scope 明确要求论文 \"focus on a core robotics problem\"，涵盖\n机器人感知、控制、操控、运动、模仿学习、强化学习、sim-to-real 等方向。\n\n本 proposal 是一篇纯粹的统计方法论论文——将 conformal prediction 和\nprediction-powered inference 整合用于 LLM 文本抽取混杂因子下的因果推断。\n应用场景是临床笔记（MIMIC-IV）、社交媒体数据，完全不涉及机器人。\nProposal 自身列出的目标会议也是 AAAI 2027 / ARR→EACL 2027 / AISTATS 2027。\n\n结论：本 proposal 与 CoRL 2026 的 scope 完全不匹配，投 CoRL 主会的中稿概率\n实质为 0%（desk reject）。以下评估将基于 proposal 自身适合的会议\n（AAAI/AISTATS 级别 AI/统计方法论会议）进行 idea 质量评估，供后续流程参考。\n\n========================================================================\n\n【领域调研】:\n\n1. Zhang et al. \"Modular and Adaptive Conformal Prediction for Sequential \n   Models via Residual Decomposition\" (arXiv 2510.04406, Oct 2025):\n   — 本 proposal Track A 的核心理论基础。提出两阶段 pipeline 的残差分解框架，\n     用 FWER 控制校准各阶段参数。已验证存在，但原文处理的是供应链/股市等\n     非因果场景，未涉及加权可交换性或因果估计。\n\n2. Csillag et al. \"Extending Prediction-Powered Inference through Conformal \n   Prediction\" (arXiv 2510.16166, Oct 2025):\n   — 本 proposal Track B 的核心基础。将 PPI 与 conformal set-predictor 结合，\n     实现 Z-estimation 和 M-estimation 的有效推断。已验证存在。原文未涉及\n     因果效应估计。\n\n3. DoubleLingo (NAACL 2024, ACL Anthology):\n   — 已验证。使用 LLM 在 DML 框架内进行因果估计，仅提供渐近保证，\n     未量化 LLM 抽取噪声的有限样本不确定性。\n\n4. Barnatchez et al. \"Debiased ML for Conformal Prediction of Counterfactual \n   Outcomes Under Runtime Confounding\" (arXiv 2604.03772, Apr 2026):\n   — 已验证。处理的是训练时观测到但部署时缺失的混杂因子（runtime confounding），\n     与本 proposal 的\"噪声抽取\"设定确实不同（missing vs. noisy）。\n     Proposal 对此区分的描述准确。\n\n5. Gasparin & Ramdas \"Improving the statistical efficiency of cross-conformal \n   prediction\" (arXiv 2503.01495, ICML 2025 poster):\n   — 已验证。本 proposal 用于将三路数据划分降为两路，提升样本效率。\n     工具性引用，使用合理。\n\n6. Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025):\n   — 已验证。将 PPI 扩展到因果推断，但使用的是点预测 imputation，\n     非 conformal set-predictor。\n\n7. Kato \"Semi-Supervised Treatment Effect Estimation\" (arXiv 2511.08303, \n   NeurIPS 2025):\n   — 已验证。半监督因果效应估计，可解读为 PPI 框架下的工作。\n     提供了效率界和有效估计量。\n\n8. 直接竞争工作搜索结果：未找到任何现有工作直接将 conformal prediction\n   + LLM confounder extraction + causal inference 三者结合。该交叉空白\n   确实存在。\n\n- 调研总结：conformal prediction × causal inference 是 2024-2026 年的活跃\n  方向（系统综述 arXiv 2509.21660 覆盖 11 篇核心论文），但现有工作均假设\n  混杂因子无误差观测。LLM 用于文本因果推断（DoubleLingo, Ma et al.）也是\n  活跃方向，但仅提供渐近保证。这两条线尚未被连接。本 proposal 定位在\n  这一交叉空白上，定位清晰，空白真实存在。\n\n========================================================================\n\n【Trivial Alternative 检验】:\n\n最简单的替代方案：LLM 点预测抽取 + 标准 doubly robust 估计 + bootstrap \n置信区间。这正是 DoubleLingo 等工作的路线。\n\nProposal 的 claim 是：当 LLM 抽取噪声具有异质性时，bootstrap CI 会\nundercover。这是一个合理的理论论点——measurement error 在因果推断中\n确实会导致偏差，bootstrap 无法校正系统性的测量误差。\n\n然而，第二个 trivial alternative 更具威胁：**直接使用 PPI（非 conformal \n版本）进行因果推断**（如 arXiv 2502.06343 已经做的），配合标准误差估计。\nTrack B 相对于 vanilla PPI causal inference 的增量价值在于用 conformal \nset-predictor 替代点预测 imputation，获得有限样本有效性而非渐近有效性。\n这个增量是真实的，但边际性较强——在大样本下两者表现趋同。\n\n对于 Track A，trivial alternative 是：对 LLM 抽取结果做 sensitivity \nanalysis（如 Manski bounds 风格的 partial identification），不需要 \nconformal prediction 机制也能给出包含真实效应的区间。Proposal 的增量\n在于 conformal 框架能自适应地根据 LLM 质量调整区间宽度（|C| 小则窄），\n而 Manski bounds 是全域最坏情况。这个区分有意义但需要实证验证优势大小。\n\n总结：存在 trivial alternatives，但 proposal 相对于它们有可辨识的增量价值。\n增量的大小取决于实验验证，属于\"有意义但非压倒性\"的增量。\n\n========================================================================\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的关键假设：\n\n1. **\"Modular residual decomposition 在因果可交换性条件下成立\"**\n   — 这是 proposal 自认的主要理论贡献。Zhang et al. 的原始框架处理的是\n   标准预测问题，不涉及加权可交换性（propensity weighting 导致的 \n   non-exchangeability）。将其推广到 doubly robust pseudo-outcomes 需要\n   新的证明。这不是\"想当然\"，但确实是未完成的理论工作。如果这一步\n   证不出来，Track A 的理论基础就不存在。\n\n2. **\"Conformal prediction sets 足够小以使区间实用\"**\n   — Pilot analysis 表明 |C|≤2（K=5 时）才能使 widening 可控（~60%）。\n   这要求 LLM 分类准确率极高（top-2 覆盖率 ≥ 1-α）。对于真实临床文本\n   中的多类别抽取（如疾病严重程度），LLM 是否能达到这一水平是经验问题。\n   如果不能，方法虽然\"正确反映不确定性\"，但实际产出的区间宽到无法\n   指导决策——正确但无用。\n\n3. **\"连续嵌入 track 的 Lipschitz 连续性假设\"**\n   — Proposal 承认此 track 需要平滑估计器，排除了树模型。但即使用神经网络，\n   128-256 维嵌入空间中的椭球 conformal sets 的体积增长极快，worst-case \n   优化可能导致极宽区间。Proposal 对此缺乏 pilot analysis（仅对 categorical \n   track 做了）。\n\n4. **\"Causal exchangeability 在 LLM 抽取噪声下仍然成立\"**\n   — 标准因果推断假设无未观测混杂。如果 LLM 抽取引入的\"噪声\"本质上\n   是一种测量误差，那么 adjusted estimator 用的是带噪声的 confounder，\n   可能违反无未观测混杂假设。Conformal sets 能否完全补偿这一点，\n   取决于 conformal set 是否覆盖了真实值——这正是 conformal coverage \n   保证的，但前提是校准数据中有 ground-truth labels，回到了对标注数据\n   的依赖。\n\n========================================================================\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   — 理由：交叉空白确实存在——搜索未找到任何直接竞争工作。但这是一篇\n   典型的 \"bridge paper\"：将已有的 modular CP (Zhang et al. 2510.04406)、\n   conformal PPI (Csillag et al. 2510.16166)、和 doubly robust causal \n   estimation (DoubleLingo/Ma et al.) 组合到一起。核心技术组件均为现有方法，\n   novelty 主要在于 (a) 证明 modular decomposition 在因果设定下成立，\n   (b) 显式 propensity score propagation 的处理。这些是非 trivial 的\n   技术工作，但不是概念性突破。一个熟悉这三条文献线的审稿人看到这个\n   idea 会说 \"natural next step\" 而非 \"surprising\"。\n\n2. Significance: 【中偏强】\n   — 理由：问题本身重要且时机好。LLM 用于文本因果推断正在快速增长\n   （DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），但都缺乏有限\n   样本保证。提供此保证有真实的实践价值，尤其在高风险场景（临床决策）。\n   但实际 significance 受限于 conservatism：pilot analysis 显示方法\n   仅在 LLM 质量高时实用（|C|≤2），这限制了适用范围。此外，目标受众\n   相对小众（同时关注 conformal prediction + causal inference + NLP 的\n   研究者）。\n\n3. Related Work: 【强】\n   — 理由：这是本 proposal 最突出的优点。对领域格局的覆盖极为全面：\n   从 conformal ITE (Lei & Candès 2021, Alaa et al. NeurIPS 2023) 到 \n   PPI causal (arXiv 2502.06343, Kato NeurIPS 2025)，到 LLM causal \n   (DoubleLingo, Ma et al.)，再到最新的 Barnatchez et al. (2604.03772) \n   和 Vovk & Wang (2603.11134)，均有准确覆盖和清晰区分。引用的论文\n   经调研验证均真实存在，描述准确。差异化定位（noisy extraction vs. \n   missing confounders vs. confounding in prediction）逻辑清晰。\n\n========================================================================\n\n【概率估计】（针对 proposal 自身目标会议 AAAI/AISTATS 级别）: \n[22% - 32%] 中位 27%\n\n【针对 CoRL 2026】: ≈0%（scope 完全不匹配，desk reject）\n\n【估计理由】:\nNovelty 评为\"中\"是主要限制上界的因素。这是一篇连接三条现有技术线的 \nbridge paper，核心组件已存在，贡献在于证明组合在因果设定下成立 + 显式\npropensity propagation 分析。对于 AAAI/AISTATS 的审稿人来说，这是一个\n\"natural extension\"——方向正确、技术 sound、但不 surprising。\n\nSignificance 为\"中偏强\"提供了一定支撑：问题确实重要且时机好，如果\n实验执行出色（coverage 保证 + 合理区间宽度），有望达到 30%+ 的上界。\n但 conservatism 问题（仅在 LLM 质量高时实用）限制了 impact story。\n\nRelated work 为\"强\"是一个加分项，说明作者对领域理解深入，但 related \nwork 的完备性不能弥补 novelty 的不足。\n\n概率区间 22-32% 对应 rubric 中 \"idea 有实质内核，方向正确，有真实的 \nnovelty delta，但核心发现如果 positive 审稿人可能会说 'I would have \nguessed this'\" 的描述，略低于该档中位（因为 bridge paper 性质 + \nconservatism 限制实用性）。\n\n【主要风险】:\n1. **\"Natural combination\" 质疑**：审稿人可能认为将 modular CP + PPI + DR \n   estimation 组合在一起虽然技术上非 trivial，但概念上是 \"obvious next step\"，\n   缺乏 surprising insight。这是 bridge paper 面临的系统性风险。\n2. **Conservatism 导致实用性存疑**：如果实验中 conformal set size 普遍 ≥3\n   （真实 LLM 在临床文本上的表现），区间可能宽到无实用价值，\n   审稿人会质疑 \"compared to just using bootstrap with a good LLM, \n   what do I gain in practice?\"\n```\n\nSources:\n- [Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition](https://arxiv.org/abs/2510.04406)\n- [Extending Prediction-Powered Inference through Conformal Prediction](https://arxiv.org/abs/2510.16166)\n- [DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)](https://aclanthology.org/2024.naacl-short.71/)\n- [Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding](https://arxiv.org/abs/2604.03772)\n- [Improving the statistical efficiency of cross-conformal prediction (ICML 2025)](https://arxiv.org/abs/2503.01495)\n- [Prediction-Powered Causal Inferences](https://arxiv.org/abs/2502.06343)\n- [Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates](https://arxiv.org/abs/2511.08303)\n- [A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation](https://arxiv.org/html/2509.21660)\n- [Conformal Prediction for Causal Effects of Continuous Treatments](https://arxiv.org/abs/2407.03094)\n- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 关键前置问题：严重的 VENUE MISMATCH ⚠️\n\n本 proposal 被要求评估投稿 CoRL 2026（Conference on Robot Learning）的中稿潜力。\n然而 CoRL 的核心 scope 是：robotic perception, control, manipulation, navigation, \nlocomotion, driving, imitation learning, reinforcement learning for physical robots, \nrobot foundation models 等。\n\n本 proposal 是关于 conformal prediction + prediction-powered inference 用于 LLM\n文本 confounder 提取后的因果推断——这是一篇纯粹的 统计方法论/因果推断/NLP 论文，\n与机器人学习没有任何关联。proposal 自身列出的 target venues 也是 AAAI 2027、\nARR→EACL 2027、AISTATS 2027，均不包含 CoRL。\n\n这篇论文投 CoRL 几乎必定 desk reject（scope 不匹配）。\n\n以下评估将分两部分：(A) venue-agnostic 的 idea 质量评估，(B) CoRL 2026 特定概率。\n\n═══════════════════════════════════════════════════\n(A) VENUE-AGNOSTIC IDEA 质量评估（适用于 AAAI/AISTATS/NeurIPS 等）\n═══════════════════════════════════════════════════\n\n【领域调研】:\n- Zhang et al. \"Modular and Adaptive Conformal Prediction for Sequential Models \n  via Residual Decomposition\" (arXiv 2510.04406, 2025): 本 proposal 的 Track A \n  核心基础。提出了 two-stage pipeline 的模块化 conformal prediction 框架，通过 \n  residual decomposition 实现 stage-wise 不确定性归因。原文应用于 supply chain \n  和 stock market，未涉及因果推断。proposal 的贡献是将其扩展到 causal setting \n  with weighted exchangeability。\n  \n- Csillag et al. \"Extending Prediction-Powered Inference through Conformal \n  Prediction\" (arXiv 2510.16166, 2025): Track B 的核心基础。将 PPI 与 conformal \n  set-predictor 结合，实现 Z-estimation 和 M-estimation 的有效推断。原文是通用 \n  统计框架，未专门处理因果推断场景。proposal 将其扩展到 ATE 估计。\n\n- Barnatchez et al. \"Debiased ML for Conformal Prediction of Counterfactual \n  Outcomes Under Runtime Confounding\" (arXiv 2604.03772, April 2026): 最直接的\n  竞争工作。但处理的是 confounders MISSING at deployment（缺失）而非 noisy \n  extraction（有噪声）。proposal 对此区分是清晰且成立的。\n\n- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025): 将 PPI 扩展到\n  因果场景，使用 conditional calibration。但未使用 conformal set-predictor。\n\n- Kato \"Semi-Supervised Treatment Effect Estimation\" (arXiv 2511.08303, \n  NeurIPS 2025): 理论上建立了 semi-supervised setting 下 treatment effect \n  estimation 的 efficiency bounds。是 PPI+causal 方向的理论基础。\n\n- DoubleLingo (NAACL 2024): 在 DML 框架内使用 LLM 做 nuisance estimation，\n  仅提供渐近保证。\n\n- Ma et al. \"LLM-Driven Treatment Effect Estimation Under Inference Time Text \n  Confounding\" (NeurIPS 2025): 处理 LLM 文本 confounding，但同样仅有渐近保证。\n\n- Conformal Prediction for Medical Entity Extraction (arXiv 2603.00924, 2026): \n  将 conformal prediction 用于 LLM 医学实体提取，提供 FDR 保证。但仅处理\n  extraction quality，未连接到下游因果推断。\n\n- Gasparin & Ramdas \"Improving Statistical Efficiency of Cross-Conformal \n  Prediction\" (ICML 2025): proposal 用于减少 data split 的工具，是成熟技术。\n\n- Singer et al. \"Conformal Prediction for Astronomy Data with Measurement \n  Error\" (MNRAS 2025): 唯一直接处理 measurement error + conformal prediction \n  的工作，但领域完全不同（天文学），且不涉及因果推断。\n\n- 调研总结: 这个领域处于 conformal prediction × causal inference × LLM-based \n  text processing 三者交汇处，2025-2026 年各两两交叉都有活跃进展，但三者的\n  完整统一（特别是 noisy extraction 而非 missing confounders）确实尚无直接先例。\n  Proposal 的 gap identification 是准确的。\n\n【Trivial Alternative 检验】:\n\n存在两个需要认真回答的 trivial alternative 威胁：\n\n1. **End-to-end black-box conformal prediction**: 不做模块化分解，直接对整个 \n   pipeline（LLM extraction → causal estimation）做 black-box conformal \n   prediction。这会更简单，且同样提供 finite-sample 保证。Proposal 的增量价值\n   在于：(a) 模块化分解可以 attribute uncertainty 到具体 stage，(b) 声称 FWER \n   控制比 Bonferroni 更 tight。但问题是：(a) 是 interpretability 收益（nice to \n   have 但非 essential），(b) 需要实验证明 tightness 提升有多大。如果 black-box \n   approach 的 interval 只宽 10-20%，模块化方法的复杂性就难以 justify。\n\n2. **Standard measurement error correction + bootstrap**: 传统因果推断文献中\n   有成熟的 measurement error correction 方法（SIMEX, regression calibration）。\n   虽然这些是渐近方法，但配合 bootstrap 可能在实际中表现不差。proposal 声称 \n   bootstrap \"undercovers\"，但这是需要实验验证的 claim，不是不证自明的。\n\n增量价值结论：proposal 的真正增量在于 finite-sample guarantee 本身（vs 渐近\n保证），以及对 noisy extraction 的 honest uncertainty quantification。但 trivial \nalternative 威胁是实质性的——必须在实验中展示 black-box CP 和 bootstrap 的 \ninterval 质量确实显著劣于模块化方法，否则 reviewers 会质疑复杂性是否 justified。\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的关键假设：\n\n1. **\"模块化 residual decomposition 在 causal exchangeability 条件下成立\"** \n   —— 这是 proposal 声称的核心理论贡献，但 proposal 只说 \"proving the modular \n   residual decomposition holds\"，未给出证明思路或困难程度评估。Zhang et al. \n   (2025) 的原始 decomposition 假设标准 exchangeability，而 causal setting \n   需要 weighted exchangeability (Barber et al. 2023)。这个扩展是否 \n   straightforward 还是 non-trivial，proposal 没有给出信号。如果证明是 trivial \n   的，理论贡献就很薄；如果证明是困难的，可能 10 周内无法完成。\n\n2. **\"Worst-case enumeration over conformal sets 产生的 conservatism 是可接受的\"** \n   —— pilot analysis 显示 |C|=2 时 widening 60%，|C|=3 时 100%。这些数字是\n   基于一个特定数值例子的 back-of-envelope 计算，不是一般性结果。实际数据中\n   propensity score 分布和 outcome 函数形状可能导致更大或更小的 widening。\n   关键假设是 \"好的 LLM 通常能 achieve |C|≤2\"，但这取决于 calibration 数据量\n   和 LLM quality，在 clinical text 等困难场景中未必成立。\n\n3. **\"Conformal PPI 的 Z-estimation bound 在因果 setting 中不会过于 loose\"** \n   —— Track B 的 ATE interval bound 包含 M·Err(C) 项，其中 M 是 influence \n   function 的 bounded range。在 doubly robust estimation 中，influence function \n   涉及 1/propensity score，如果 propensity 接近 0/1，M 可以很大，使得 \n   bound 变得 vacuous。\n\n4. **\"连续 embedding track 的 ellipsoidal conformal sets + convex relaxation \n   在 128-256 维度是 tractable 且 meaningful 的\"** —— 高维 conformal sets \n   体积随维度指数增长（curse of dimensionality），128-256 维的 ellipsoidal \n   sets 可能覆盖了 embedding space 的大部分，使 worst-case bounds trivially \n   wide。proposal 承认限制于 smooth nuisance estimators，但未分析维度对 \n   interval width 的影响。\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   理由：proposal 准确识别了一个真实存在的 gap——三个成熟子领域（modular CP, \n   conformal PPI, LLM-based causal inference）的交汇处确实没有被直接 addressed。\n   与 Barnatchez et al. (2604.03772) 的区分（noisy vs. missing confounders）是\n   清晰且有意义的。然而，核心方法论是 \"将 Zhang et al. 2025 的框架 + Csillag \n   et al. 2025 的框架应用到 causal setting\"——这是 combination novelty 而非 \n   conceptual novelty。审稿人看到这篇论文时，反应更可能是 \"yes, this combination \n   makes sense and someone should do it\" 而不是 \"this is a surprising insight I \n   wouldn't have thought of\"。Singer et al. (MNRAS 2025) 已在天文学中处理了\n   measurement error + CP 的组合（虽然不涉及因果推断），说明 \"CP for noisy \n   covariates\" 不是全新概念。Novelty 的实质深度取决于 weighted exchangeability \n   proof 的 non-triviality，但 proposal 未提供足够信息判断。\n\n2. Significance: 【中偏强】\n   理由：研究问题本身很重要——LLM-based confounder extraction 正在成为 text-based \n   causal inference 的标准实践（DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），\n   而这些方法都缺乏 finite-sample guarantee。随着 LLM 在 clinical NLP 和 social \n   science 中的部署扩大，对 extraction noise 的 honest UQ 有明确需求。但 \n   significance 受限于：(a) 实际用户群体较窄（做 text-based causal inference 的\n   人本身就是小众），(b) interval widening 60-100% 可能让 practitioners 觉得\n   方法 \"too conservative to be useful\"，(c) 如果核心发现是 \"conformal methods \n   maintain coverage but with wider intervals\"，这几乎是 by construction 的结论，\n   不 surprising。\n\n3. Related Work: 【强】\n   理由：这是 proposal 最突出的优点。对近期文献（直到 2026 年 4-6 月）的覆盖非常\n   全面，包括 Barnatchez et al. (April 2026), Vovk & Wang (March 2026), \n   Lützow et al. (2026), Gasparin & Ramdas (ICML 2025) 等非常新的工作。与\n   最相关竞争工作的 differentiation 清晰且有说服力（特别是 noisy extraction \n   vs. missing confounders 的区分）。引用的论文经验证均真实存在且描述准确。\n   Landscape section 对三个子领域的 gap 分析是系统性的。\n\n═══════════════════════════════════════════════════\n(B) CoRL 2026 特定评估\n═══════════════════════════════════════════════════\n\nCoRL (Conference on Robot Learning) 的 scope 是 robot learning：robotic \nperception, control, manipulation, navigation, locomotion, driving, flight, \nimitation learning, RL for physical robots, robot foundation models 等。\n\n本 proposal 是关于 conformal prediction 用于 LLM 文本 confounder 提取后的\n因果推断——与机器人学习没有任何实质性关联。proposal 自身的 target venues \n(AAAI 2027, ARR→EACL 2027, AISTATS 2027) 也不包含 CoRL。\n\n即使忽略 scope 问题只看 idea 质量，这篇论文在 CoRL 也找不到合适的 reviewer——\n该社区的审稿人不具备评审 causal inference + conformal prediction 理论贡献\n的背景。\n\n【概率估计 — CoRL 2026】: [1% - 5%] 中位 2%\n【估计理由 — CoRL】: \nScope 完全不匹配是 decisive factor。CoRL 关注 robot learning，本文是纯粹的\n统计方法论/因果推断/NLP 工作。极高概率 desk reject。即使进入 review，reviewer \npool 也不匹配，无法获得公正评审。1-5% 的非零下界仅反映 \"AC 误判 scope\" 的\n极小概率。\n\n【概率估计 — Venue-Agnostic（AAAI/AISTATS 级别会议）】: [20% - 35%] 中位 27%\n【估计理由 — Venue-Agnostic】: \nIdea 的 novelty 是 combination-level（中），将两个现有框架 extend 到新 setting，\ngap identification 准确但 \"someone should do this\" 性质明显。Significance 中偏强\n（问题重要但用户群窄、interval widening 可能 limit 实际价值）。Related work \ncoverage 强——这是最好的维度。上界受限于 novelty 维度：核心发现若 positive，\n审稿人更可能说 \"makes sense\" 而非 \"surprising\"。下界由 significance 和 related \nwork 支撑——问题真实、gap 确实存在、执行如果 solid 可以 pass。对于 AAAI/AISTATS \n这类会议，combination novelty + solid execution 可以中稿，但需要实验显著超越 \ntrivial alternatives。\n\n【主要风险】:\n1. **[Scope — CoRL 致命风险] 论文与 CoRL 的 scope 完全不匹配**，几乎必定 \n   desk reject。这不是 idea 质量问题，而是 venue 选择错误。建议维持原定的 \n   AAAI 2027 / AISTATS 2027 投稿计划。\n   \n2. **[Idea 层面 — Trivial Alternative 威胁] Black-box end-to-end conformal \n   prediction 可能以远低的复杂度达到类似效果**。如果模块化分解相比 black-box \n   CP 的 interval width 改善不显著（<15-20%），整个方法论复杂性的 justification \n   就会被审稿人质疑。这是实验无法完全补救的 idea 层面问题——如果 black-box \n   approach 效果相近，说明模块化分解在这个 application 中 value-add 有限。\n\n3. **[Idea 层面 — Conservatism 可能使方法实际无用] 60-100% interval widening \n   在实际临床决策中可能被视为 too conservative**。如果主要实验结果是 \"our method \n   has correct coverage but intervals are 2x wider than oracle\"，reviewers 可能\n   认为这是一个 \"correct but useless\" 的方法。\n```\n\n**总结**：这是一篇 idea 质量中等偏上的 combination paper，gap identification 准确，related work 覆盖优秀，但核心 novelty 是 framework integration 而非 conceptual breakthrough。**然而投稿 CoRL 2026 是严重的 venue mismatch**——CoRL 是机器人学习会议，本文是统计方法论/因果推断工作，几乎必定被 desk reject。强烈建议维持 proposal 自身原定的 target venues（AAAI 2027 / AISTATS 2027）。\n\nSources:\n- [Modular and Adaptive Conformal Prediction for Sequential Models (Zhang et al. 2025)](https://arxiv.org/abs/2510.04406)\n- [Extending Prediction-Powered Inference through Conformal Prediction (Csillag et al. 2025)](https://arxiv.org/abs/2510.16166)\n- [Debiased ML for Conformal Prediction Under Runtime Confounding (Barnatchez et al. 2026)](https://arxiv.org/abs/2604.03772)\n- [Prediction-Powered Causal Inferences (2025)](https://arxiv.org/abs/2502.06343)\n- [Semi-Supervised Treatment Effect Estimation (Kato, NeurIPS 2025)](https://arxiv.org/abs/2511.08303)\n- [Improving Statistical Efficiency of Cross-Conformal Prediction (Gasparin & Ramdas, ICML 2025)](https://arxiv.org/abs/2503.01495)\n- [Systematic Review of Conformal Inference for Treatment Effects](https://arxiv.org/html/2509.21660)\n- [DoubleLingo: Causal Estimation with LLMs (NAACL 2024)](https://aclanthology.org/2024.naacl-short.71/)\n- [LLM-Driven Treatment Effect Estimation (Ma et al. NeurIPS 2025)](https://openreview.net/forum?id=sv41aaGTit)\n- [Conformal Prediction for Astronomy with Measurement Error (MNRAS 2025)](https://arxiv.org/abs/2412.10544)\n- [Conformal e-prediction under confounding (Vovk & Wang 2026)](https://arxiv.org/pdf/2603.11134)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 About](https://www.corl.org/about-corl)\n- [Conformal Prediction for Medical Entity Extraction (2026)](https://arxiv.org/html/2603.00924)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\n调研完成，现在我可以给出完整的入口评估。\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- Zhang et al. \"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition\" (arXiv 2510.04406, Oct 2025): 本 proposal Track A 的核心技术基础。MIT 团队提出的 two-stage pipeline 的模块化 CP 框架，通过残差分解实现跨 stage FWER 控制。已验证于供应链和股市数据，但 **未涉及因果推断设定**（无 weighted exchangeability、无 propensity score 传播）。Proposal 声称将其推广到因果设定的 claim 有据。\n- Csillag et al. \"Extending Prediction-Powered Inference through Conformal Prediction\" (arXiv 2510.16166, Oct 2025): Track B 的核心技术基础。将 CP set-predictor 引入 PPI 框架，实现 Z-estimation、M-estimation 等下游推断的 finite-sample 有效性。该工作 **未涉及因果推断（ATE/ITE 估计）**，因此 proposal 将其扩展到 causal PPI 是未被覆盖的。\n- DoubleLingo (NAACL 2024, ACL Anthology): 用 LLM 作为 DML 框架中的 nuisance model，从文本数据中做因果估计。**仅提供渐近保证**，不处理 LLM 抽取噪声的 finite-sample UQ。Proposal 对其定位准确。\n- Ma et al. \"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding\" (NeurIPS 2025, arXiv 2507.02843): 解决训练时有完整 confounders、推断时仅有文本描述的问题。使用 doubly robust learner + LLM。与本 proposal 问题设定不同（训练/推断时的信息不对称 vs. 全程噪声抽取），但都在 LLM + 因果推断的大方向上。**仅渐近保证**。\n- Barnatchez et al. \"Debiased ML for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding\" (arXiv 2604.03772, April 2026): 处理 confounders 在部署时 **完全缺失** 的场景（runtime confounding），通过 semiparametric debiasing 边际化未观测变量。与本 proposal 的 **noisy extraction**（变量存在但有噪声）设定本质不同。Proposal 对其区分清晰。\n- Prediction-Powered Causal Inferences (NeurIPS 2025 poster, OpenReview): 将 PPI 应用于因果推断中的未标注目标实验，关注跨实验 transferability，**未使用 conformal sets 来量化 imputed covariates 的不确定性**。\n- Systematic Review of Conformal Inference for Treatment Effects (arXiv 2509.21660, 2025): 综述覆盖 11 篇核心论文（Lei & Candès 2021, Alaa et al. NeurIPS 2023, KDD 2024 wTCP-DR 等）。确认所有现有 conformal ITE 方法 **假设 confounders 无误差观测**。\n- Vovk & Wang \"Conformal e-prediction in the presence of confounding\" (arXiv 2603.11134, March 2026): 用 e-values 处理 X-Y 之间的 confounding，目标是预测而非因果效应估计。与本 proposal 互补但不竞争。\n- 调研总结: 在\"conformal prediction × causal inference\"和\"LLM × text-based causal inference\"两个活跃领域的交叉点，**确实存在一个未被填补的空缺**：没有现有工作提供 LLM 抽取文本 confounders 下治疗效应估计的 finite-sample coverage 保证。但这个空缺更多是\"自然的下一步整合\"，而非\"根本性的方法论突破\"。\n\n【Trivial Alternative 检验】:\n存在至少三个更简单的替代方案需要考量：\n1. **Bootstrap + multiple imputation**：经典处理含噪/缺失协变量的方法。对 LLM 多次抽取结果做 multiple imputation + Rubin's combining rules，可能在实践中产生类似宽度的置信区间，无需 conformal 框架的复杂性。Proposal 提到 bootstrap \"undercovers\"，但这是一个需要实验验证的 claim，而非理论定论——适当修正的 bootstrap（如 wild bootstrap for DML）在有限样本下表现通常尚可。\n2. **贝叶斯方法**：对 LLM 抽取不确定性建立先验，通过后验边际化传播到治疗效应估计。贝叶斯 DML 已有相关工作。\n3. **简单的 sensitivity analysis**：Manski bounds 或 Rosenbaum sensitivity analysis 风格的方法，对 confounder 误分类率做最坏情况分析。\n\n**增量价值在哪？** Proposal 的核心增量是 **distribution-free finite-sample guarantee**——不依赖渐近理论或分布假设。这确实是上述替代方案不具备的。但实际价值取决于 intervals 是否足够紧以提供有用信息，而 pilot analysis 显示 60-100% 的 widening 已经相当可观。\n\n【前提假设检验】:\n核心 claim 的逻辑链中存在以下未经验证的关键假设：\n1. **LLM 抽取误差可被 conformal prediction 有效捕获**：CP 要求（近似）exchangeability。LLM 的抽取误差可能对特定 subpopulation 系统性偏差（如对少数族裔的临床描述更容易误判严重程度），此时 marginal coverage 保证可能掩盖 conditional miscoverage。Proposal 未讨论这一点。\n2. **Weighted exchangeability 在 DR pseudo-outcomes 下成立**：这是 proposal 自认的理论贡献核心，但尚未证明。如果证明过程中需要额外条件（如 positivity 加强版、nuisance 函数收敛率约束），实际适用性可能大幅缩小。\n3. **Worst-case enumeration 的保守性是\"可接受的\"**：Pilot analysis 基于一组特定数值假设。在真实临床场景中，propensity score 的变异可能更极端（如罕见疾病），导致 intervals 实际上 vacuously wide。\n4. **连续 embedding track 的凸松弛质量**：Taylor 展开 + Lipschitz 连续性在 128-256 维椭球上的近似质量未知，且限制只能用 smooth nuisance estimators，排除了 GBDT 等实践中最常用的方法。\n\n【3 维度打分】:\n  1. Novelty: 中 — \n     该 proposal 正确识别了一个真实存在的研究空缺：systematic review (arXiv 2509.21660) 确认所有 conformal ITE 方法假设无误差 confounders；DoubleLingo (NAACL 2024) 和 Ma et al. (NeurIPS 2025) 仅提供渐近保证；Zhang et al. (2510.04406) 的模块化 CP 未涉及因果设定；Csillag et al. (2510.16166) 的 conformal PPI 未涉及因果推断。空缺真实存在。\n     然而，novelty 本质上是 **integrative**：将 Zhang et al. 的 framework 应用到 \"LLM 抽取 → 因果估计\" 的 pipeline，将 Csillag et al. 的 conformal PPI 扩展到 ATE 估计。理论贡献（weighted exchangeability 下 DR pseudo-outcomes 的模块化残差分解）是对已有框架在新设定下的推广，而非方法论上的根本创新。对领域熟悉的审稿人可能会说 \"natural extension\" 而非 \"surprising contribution\"。\n\n  2. Significance: 中 — \n     问题本身有实际意义：LLM 从文本抽取 confounders 是 causal NLP 的活跃方向（DoubleLingo, Ma et al.），而抽取噪声确实威胁 causal estimate 的有效性。但：(a) 受众较窄——同时关心 \"text-based causal inference\" + \"finite-sample guarantees\" + \"LLM extraction noise\" 的研究者群体有限；(b) 如果核心结果是 \"我们的方法在 LLM 噪声下维持 coverage，但 intervals 比 oracle 宽 60-100%\"，大多数审稿人会说 \"I would have guessed this\"——coverage 保证是 conformal 方法的固有属性，而保守性是 worst-case 推理的固有代价；(c) 对更广泛的 NLP/ML 社区影响有限，主要服务于方法论研究者。\n\n  3. Related Work: 强 — \n     Proposal 对领域的覆盖非常全面，对每个相关工作的定位准确且区分清晰。特别突出的是：(a) 对 Barnatchez et al. (2604.03772) 的区分（missing vs. noisy）准确且实质；(b) 对 Vovk & Wang (2603.11134) 的 e-value 方法的定位恰当；(c) 对 DoubleLingo / Ma et al. 的渐近保证局限性分析中肯；(d) 引用的所有关键论文均经验证真实存在且描述准确；(e) 对三条独立研究线索的交汇时机判断合理。这是一个对该领域有深入了解的研究者写的 proposal。\n\n【概率估计】: 22% - 33%, 中位 27%\n\n【估计理由】: \nRelated Work 维度强（定位清晰、差异化充分），保证了论文不会因 \"忽视相关工作\" 被拒——这提高了下限。但 Novelty 和 Significance 均为\"中\"限制了上界：\n- Novelty 层面，integrative contribution 在顶会中通常需要额外的\"惊喜因素\"来补偿。审稿人极可能评价为 \"technically sound but incremental\"——将两个已有 framework 应用到新场景。\n- Significance 层面，核心 finding（如果 positive）的 surprise factor 低。\"Conformal 方法在噪声下维持 coverage 但更保守\" 是几乎可以先验预测的结论。\n- 对于 AISTATS（proposal 的 stretch target），这种方法论整合型工作相对更被接受（~30-33%）；对于 AAAI（primary target），偏理论/niche 的 statistical methodology 可能不占优势（~22-25%）。\n\n**特别注意**：Proposal 系统提示中提到 CoRL 2026，但本 proposal 与机器人学习完全无关。如果确实投稿 CoRL，中稿概率接近 0%。以下评估基于 proposal 自身声明的目标会议（AAAI 2027 / ARR / AISTATS 2027）。\n\n【主要风险】:\n1. **\"Natural extension\" 感过强**：最大的拒稿风险在于审稿人认为这是将 Zhang et al. + Csillag et al. 的框架\"搬运\"到因果设定，理论贡献（weighted exchangeability 下的证明）不足以构成独立贡献。如果证明过程中不出现非 trivial 的技术挑战（如需要全新的分析工具），这一风险尤为突出。\n2. **实际价值 vs. 保守性的 trade-off 不利**：Pilot analysis 显示即使 good LLM (|C|=2) 也有 60% widening。审稿人可能质疑：在 intervals 如此宽的情况下，这些 finite-sample 保证相对于渐近方法（或简单的 bootstrap with correction）的实际增量价值有多大？如果实验中 bootstrap 表现\"足够好\"（尽管理论上 undercovers），方法的卖点将被严重削弱。\n```\n\nSources:\n- [Systematic Review of Conformal Inference for Treatment Effects](https://arxiv.org/html/2509.21660v1)\n- [Zhang et al. - Modular Conformal Prediction](https://arxiv.org/abs/2510.04406)\n- [Csillag et al. - Extending PPI through CP](https://arxiv.org/abs/2510.16166)\n- [DoubleLingo - NAACL 2024](https://aclanthology.org/2024.naacl-short.71/)\n- [Ma et al. - LLM-Driven Treatment Effect Estimation (NeurIPS 2025)](https://arxiv.org/abs/2507.02843)\n- [Barnatchez et al. - Runtime Confounding](https://arxiv.org/abs/2604.03772)\n- [Prediction-Powered Causal Inferences (NeurIPS 2025)](https://openreview.net/forum?id=HOa6LTIjyn)\n- [Vovk & Wang - Conformal e-prediction under confounding](https://arxiv.org/pdf/2603.11134)\n- [Conformal Prediction for Causal Effects of Continuous Treatments](https://arxiv.org/abs/2407.03094)\n- [LLM-based Agents for Confounder Discovery](https://arxiv.org/abs/2508.07221)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders\n\n## Description\nWe propose ConformalPPITextCausal, a framework providing finite-sample coverage guarantees for treatment effects estimated using LLM-extracted text confounders. Current methods (DoubleLingo, Ma et al.) rely on asymptotic guarantees that break down when LLM extraction introduces unquantified heterogeneous noise. Our dual-track approach addresses this via: Track A (ITE intervals) — adapting modular conformal prediction (Zhang et al. 2025) to a causal two-stage pipeline where Stage 1 produces conformal prediction sets over LLM-extracted categorical confounders (with worst-case pseudo-outcome enumeration including explicit propensity score propagation, O(|C|) per unit) or low-dimensional Matryoshka embeddings (with ellipsoidal sets and convex relaxation restricted to smooth nuisance estimators), and Stage 2 constructs doubly robust treatment effect intervals with FWER-controlled coverage tighter than Bonferroni; Track B (ATE intervals) — extending conformal prediction-powered inference (Csillag et al. 2025) to the causal setting, where a small expert-labeled and large LLM-imputed dataset yield valid confidence intervals via Z-estimation with conformal set-predictors. Cross-conformal calibration (Gasparin & Ramdas, ICML 2025) reduces the three-way data split to two-way, improving sample efficiency for labeled-data-scarce settings. A pilot conservatism analysis shows practical viability: for K=5 confounder categories, interval widening is ~60% with conformal set size |C|=2 (good LLM) and ~100% with |C|=3 (decent LLM), driven primarily by propensity score variation across conformal set members. The method is practically useful when the LLM achieves small conformal sets and correctly signals insufficient information otherwise. We differentiate from Barnatchez et al. (2604.03772), who handle missing confounders at deployment via semiparametric debiasing — a complementary but distinct setting from our noisy-extraction framework. The genuine theoretical contribution is proving the modular residual decomposition holds under causal exchangeability conditions specific to doubly robust pseudo-outcomes with explicit propensity propagation. Experiments on semi-synthetic MIMIC-IV clinical notes, social media data, and synthetic benchmarks demonstrate maintained nominal coverage where bootstrap alternatives undercover, with a dedicated conservatism experiment varying |C|/K to validate the pilot analysis.\n\n## Core Problem\nCausal inference from observational text data (clinical notes, social media, policy documents) requires adjusting for confounders embedded in unstructured text. Modern LLMs can extract these confounders, but extraction is imperfect — introducing measurement error that invalidates standard causal estimators' asymptotic guarantees. No existing framework provides finite-sample coverage guarantees for treatment effect estimates when confounders are extracted by a fallible LLM. Naive approaches (plugging in LLM point predictions as if they were ground truth) can produce arbitrarily biased causal conclusions when extraction noise is heterogeneous across subpopulations.\n\n## Opportunity\nThree independent research threads have matured to the point where they can be unified into a principled solution: (1) modular conformal prediction for sequential pipelines (Zhang et al. 2025, arXiv 2510.04406) provides a residual decomposition framework that controls family-wise error across pipeline stages without resorting to loose Bonferroni corrections; (2) prediction-powered inference extended through conformal prediction (Csillag et al. 2025, arXiv 2510.16166) yields valid population-level confidence intervals when a prediction model (here, the LLM) imputes covariates on a large unlabeled set alongside a small human-labeled set; and (3) conformal meta-learners for individual treatment effects (Alaa et al. NeurIPS 2023) provide conformal intervals for heterogeneous effects but assume perfectly observed confounders. Additionally, Matryoshka embedding models (Qwen3-Embedding-8B) now support flexible dimensionality from 32 to 4096, making conformal prediction over embedding spaces tractable at reduced dimensions. Recent work on conformal prediction under confounding — including Barnatchez et al. (arXiv 2604.03772) on runtime confounding (missing confounders at deployment) and Vovk & Wang (arXiv 2603.11134) on conformal e-prediction — demonstrates growing interest but targets distinct problem settings from ours (noisy extraction vs. missing variables, and e-values for prediction vs. p-values for treatment effects). By bridging these threads, we can deliver both individual-level (ITE) and population-level (ATE) treatment effect intervals that honestly account for LLM extraction uncertainty — a capability no current method provides.\n\n## Landscape\nThe intersection of conformal prediction and causal inference has seen rapid growth (Systematic Review, arXiv 2509.21660, covering 11 key papers), but existing conformal ITE methods (Lei & Candès JRSS-B 2021; Alaa et al. NeurIPS 2023; KDD 2024 wTCP-DR) assume confounders are observed without error. The conformal prediction for NLP survey (Campos et al. TACL 2024) covers classification, QA, and generation quality but not downstream causal validity. Prediction-powered inference (Angelopoulos et al. Science 2023) and its causal extensions (arXiv 2502.06343; Kato arXiv 2511.08303 NeurIPS 2025) address the labeled/unlabeled split for treatment effects but do not incorporate conformal sets for the imputed covariates. Zhang et al. (2025) handle sequential model pipelines with modular conformal guarantees but do not treat the causal setting or weighted exchangeability. DoubleLingo (NAACL 2024) and Ma et al. (NeurIPS 2025) use LLMs within doubly robust causal estimators for text data but provide only asymptotic guarantees with no finite-sample uncertainty quantification for LLM extraction noise. Multi-variable conformal prediction (Lützow et al. arXiv 2605.12341, 2026) and ellipsoidal conformal sets (Xu et al. ICML 2024) now provide tractable geometric tools for moderate-dimensional conformal regions.\n\nTwo recent works merit explicit differentiation: Barnatchez et al. (arXiv 2604.03772, April 2026) address conformal prediction for counterfactual outcomes under 'runtime confounding' — where confounders measured in training are entirely MISSING at deployment. Their semiparametric debiasing approach marginalizes over unobserved confounders via multiply-robust influence functions, assuming Y(a)⊥S|V (systematic differences explained by the observed subset V). Our setting is fundamentally different: all confounders are present in the text and extracted by the LLM, but with NOISE — the confounders are measured with error, not missing entirely. Their debiasing marginalizes over missing variables; our conformal sets quantify extraction uncertainty over observed-but-noisy variables. Vovk & Wang (arXiv 2603.11134, March 2026) extend conformal e-prediction to handle observed confounding between X and Y using e-values (nonnegative random variables with expectation ≤ 1) rather than p-values. While e-values provide attractive anytime-valid guarantees under optional stopping, their framework targets prediction of Y given X under confounding, not treatment effect estimation. Our framework uses standard conformal prediction sets combined with PPI, targeting ITE/ATE estimation — a complementary but distinct goal. The e-value approach could be an interesting alternative foundation for future work.\n\nThe gap we fill is the integration of modular conformal prediction and conformal PPI into a unified framework for the two-stage pipeline of LLM confounder extraction followed by causal effect estimation, with proven finite-sample validity under noisy (not missing) confounder extraction.\n\n## Approach\nWe propose a dual-track framework, ConformalPPITextCausal, for valid causal inference when text confounders are extracted by an LLM.\n\n**Data Splitting and Sample Efficiency.** The baseline design uses a three-way data split: (S1) training data for fine-tuning the LLM extraction model and fitting nuisance functions (propensity score, outcome regression), (S2) calibration data for Stage 1 conformal sets on the extracted confounders, and (S3) calibration data for Stage 2 conformal intervals on treatment effects. To address sample efficiency — critical for clinical text datasets like MIMIC-IV where expert-labeled samples are expensive — we propose two improvements: (i) K-fold cross-fitting for nuisance function estimation within S1, following Chernozhukov et al. (2018) DML, which uses all training data for both estimation and evaluation; (ii) cross-conformal calibration for Stage 1, following Gasparin & Ramdas (ICML 2025, arXiv 2503.01495), which achieves coverage ≥ 1−2α₁ using K-fold rotation rather than a dedicated hold-out set, effectively merging S2 into S1 and reducing the three-way split to a two-way split (train+Stage1-calibrate vs. Stage2-calibrate). The coverage cost (1−2α₁ vs. 1−α₁) is manageable by setting α₁ conservatively (e.g., α₁=0.025 for effective 95% Stage 1 coverage). We discuss minimum sample size requirements: Stage 2 calibration requires n₃ ≥ ⌈1/α₂⌉ ≈ 100-200 for reliable conformal quantiles at α₂=0.05, and we recommend n_total ≥ 500 for the full pipeline, with n₃ ≥ 150 reserved for Stage 2. For very small labeled datasets (n < 300), Track B (PPI) is preferred as it leverages large unlabeled corpora.\n\n**Track A — Modular Conformal ITE Intervals.** We adapt the residual decomposition of Zhang et al. (2025), where the total prediction residual R decomposes as R ≤ ΔR₁ + R₂, with Stage 1 = LLM confounder extraction and Stage 2 = doubly robust pseudo-outcome estimation.\n\nIn the primary setting, the LLM extracts CATEGORICAL confounders (e.g., disease severity ∈ {mild, moderate, severe}, smoking status ∈ {never, former, current}) via prompted classification. Conformal prediction sets for classification are natural finite sets with guaranteed coverage.\n\n**Explicit Propensity Score Propagation.** The worst-case pseudo-outcome over the conformal set is computed by full enumeration with explicit propagation through BOTH the outcome regression AND the propensity score. For each possible confounder value c ∈ C(x), the DR pseudo-outcome is:\n\nφ̂(c; Yᵢ, Aᵢ) = [μ̂₁(c) − μ̂₀(c)] + Aᵢ·(Yᵢ − μ̂₁(c))/ê(c) − (1−Aᵢ)·(Yᵢ − μ̂₀(c))/(1−ê(c))\n\nCritically, different confounder values c yield different propensity scores ê(c), which enter the augmentation term as 1/ê(c) (for treated) or 1/(1−ê(c)) (for control). This propensity variation is a distinct and compounding source of uncertainty beyond outcome regression variation. The augmentation term amplifies when propensity scores are extreme: a confounder value with ê(c)=0.1 magnifies residuals 10×. The worst-case interval is [min_c φ̂(c), max_c φ̂(c)] with complexity O(|C|) per unit. We recommend propensity score trimming (truncating ê(c) to [0.05, 0.95]) to prevent a single extreme-propensity confounder value from dominating the interval.\n\n**Pilot Conservatism Analysis.** We provide a back-of-envelope quantification of interval widening due to worst-case enumeration. Consider a clinical setting with K=5 severity categories {none, mild, moderate, severe, critical} and realistic nuisance function values:\n\n| Category | μ̂₁(c) | μ̂₀(c) | ê(c) | CATE |\n|----------|--------|--------|-------|------|\n| none     | 0.40   | 0.30   | 0.50  | 0.10 |\n| mild     | 0.50   | 0.35   | 0.45  | 0.15 |\n| moderate | 0.60   | 0.40   | 0.40  | 0.20 |\n| severe   | 0.72   | 0.45   | 0.35  | 0.27 |\n| critical | 0.85   | 0.50   | 0.25  | 0.35 |\n\nFor a treated patient with Y=0.65 and true severity=moderate, the DR pseudo-outcomes across categories are: φ̂(none)=0.60, φ̂(mild)=0.48, φ̂(moderate)=0.33, φ̂(severe)=0.07, φ̂(critical)=−0.45. The variation is dominated by the augmentation term (Y−μ̂₁(c))/ê(c), where propensity changes from 0.50 to 0.25 amplify residuals 2×. The extraction uncertainty width (Δφ = max−min over C(x)) for different conformal set sizes:\n\n- |C|=1 (excellent LLM, singleton): Δφ=0, no widening vs. oracle.\n- |C|=2 (good LLM, e.g., {moderate, severe}): Δφ≈0.26, widening ≈ 60% over oracle CI width of ~0.40.\n- |C|=3 (decent LLM, e.g., {mild, moderate, severe}): Δφ≈0.41, widening ≈ 100% over oracle.\n- |C|=4+ (poor LLM): Δφ>1.0, intervals become vacuously wide — correctly reflecting that the LLM provides insufficient information for credible causal conclusions.\n\nThe general widening ratio is approximately W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle, where Δ_CATE is the CATE variation across the conformal set, |r| is the outcome residual magnitude, and Δ(1/ê) is the inverse propensity variation. Key practical determinants: (a) conformal set size |C|/K — the LLM quality directly controls conservatism; (b) propensity score stability across confounder categories — good overlap reduces widening; (c) outcome residual magnitude — well-fitted outcome models reduce augmentation-driven widening. The method is practically useful (W < 2) when the LLM achieves conformal set size |C| ≤ 2 for K=5 categories, and correctly signals 'insufficient information' otherwise.\n\nFor the secondary continuous track, we use Qwen3-Embedding-8B with Matryoshka dimensionality reduction to 128–256 dimensions, construct ellipsoidal conformal sets (Xu et al. ICML 2024; Lützow et al. 2026), and bound worst-case pseudo-outcomes via convex relaxation: local Lipschitz continuity of nuisance functions plus first-order Taylor expansion over the ellipsoid, following the decision-theoretic framework of Wang & Dobriban (arXiv 2602.00989, 2026). **Important restriction**: the convex relaxation via Lipschitz continuity and Taylor expansion requires smooth nuisance estimators. This is compatible with neural network outcome models (e.g., TARNet, DragonNet) and kernel methods, but NOT with tree-based models (gradient-boosted trees, random forests) that are piecewise constant with jump discontinuities. We therefore restrict the continuous embedding track to smooth nuisance estimators. Note that the categorical track (primary) works with ANY nuisance estimator, including tree-based methods, since worst-case computation is by direct enumeration without smoothness assumptions. The modular framework's FWER control across both stages yields provably tighter intervals than naive Bonferroni.\n\n**Track B — Conformal PPI for ATE Intervals.** We apply the conformal PPI framework of Csillag et al. (2025) to estimate average treatment effects. The LLM serves as the prediction model in the PPI sense: a small human-labeled dataset has expert-annotated confounders, and a large dataset has LLM-extracted confounders. The conformal set-predictor from Stage 1 replaces point imputation, yielding valid ATE confidence intervals via Z-estimation: E[inf φ(C(X))] − M·Err(C) ≤ ATE ≤ E[sup φ(C(X))] + M·Err(C), where M is the bounded range of the influence function and Err(C) is the conformal miscoverage rate. This extends PPI causal inference (arXiv 2502.06343) by using conformal rather than point imputation, providing finite-sample validity without distributional assumptions on the LLM. Track B is especially suited to small-labeled-data settings (MIMIC-IV) because it leverages large unlabeled corpora.\n\nWe evaluate on three benchmarks: (1) semi-synthetic MIMIC-IV clinical notes (treatment escalation effect on ICU outcomes, disease severity as text confounder), (2) semi-synthetic social media data (content moderation effect on engagement, toxicity level as confounder), and (3) fully synthetic data with known ground-truth for calibration validation. Key metrics: empirical coverage at 90%/95% nominal levels, interval width relative to oracle (perfectly observed confounders) and bootstrap baselines, widening ratio W as a function of conformal set size and propensity overlap, and sensitivity to LLM extraction quality via deliberately degraded models. We include a dedicated conservatism experiment varying |C|/K from 0.2 to 0.8 to empirically validate the pilot analysis above.\n\nWe are transparent that worst-case reasoning over conformal sets introduces conservatism relative to oracle methods. The honest framing: our intervals maintain nominal coverage where bootstrap intervals undercover due to LLM extraction noise, with comparable width when LLM quality is high (|C|=1-2). The conservatism correctly reflects true uncertainty in the LLM-as-measurement-instrument setting, and the pilot analysis above shows it is quantifiably bounded for reasonable LLM quality.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '200-300', 'timeline': '10 weeks (targeting AAAI 2027 July 28 deadline)', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'breakdown': 'Weeks 1-2: Formalize theoretical framework (modular decomposition under weighted exchangeability, conformal PPI ATE estimator, cross-conformal Stage 1 calibration). Weeks 3-4: Implement cross-fitted pipeline, categorical conformal extraction, worst-case enumeration with explicit propensity propagation. Weeks 5-6: Implement continuous embedding track (Matryoshka 128-256d, ellipsoidal sets, convex relaxation with smooth nuisance estimators) and PPI ATE track. Weeks 7-8: Experiments on MIMIC-IV, social media, synthetic benchmarks including conservatism analysis. Week 9: Ablations (LLM quality sensitivity via |C|/K sweep, propensity overlap analysis, embedding dimension, calibration set size, cross-conformal vs. split comparison). Week 10: Paper writing and proof polishing.'}, 'human_in_loop': {'gpu_hours': '200-300', 'timeline': '8 weeks', 'claude_api_cost': '$100-150', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'notes': 'AI assists with literature integration, boilerplate code, proof sketch verification. Human focuses on theoretical contributions (weighted exchangeability conditions, tight bounds for DR pseudo-outcomes, propensity propagation analysis) and experimental design. Requires ~5 hours domain expert time for confounder annotation guidelines.'}, 'auto_research': {'gpu_hours': '250-350', 'timeline': '5-6 weeks', 'claude_api_cost': '$250-350', 'estimated_gpu_cost': '$375-525 (A100 at ~$1.50/hr)', 'speed_bottleneck': 'Theoretical proof verification requires human mathematician; three-way split calibration across multiple seeds requires sequential experiment iterations; domain expert annotation for MIMIC-IV confounder labels cannot be automated'}}\n\n## Inspired By\nGap: Existing conformal causal methods assume error-free confounders; existing LLM conformal methods ignore causal settings; existing text-based causal methods provide only asymptotic guarantees; Barnatchez et al. handle missing confounders but not noisy extraction; Vovk & Wang handle confounding in prediction but not treatment effects. Pattern: Three converging literatures (modular CP, conformal PPI, conformal causal inference) that have not been connected. Key enablers: Zhang et al. (arXiv 2510.04406) modular residual decomposition framework; Csillag et al. (arXiv 2510.16166) conformal set-predictor for PPI; Alaa et al. (NeurIPS 2023) conformal meta-learners for ITE; Barber et al. (Annals of Statistics 2023) weighted exchangeability beyond standard CP assumptions.\n\n## Target Venues\n- AAAI 2027 (Primary — abstract July 21, full paper July 28, 2026; ~10 weeks from today)\n- ARR August 2026 cycle (Secondary — submission August 3, 2026) → EACL 2027 (commitment October 11, 2026)\n- AISTATS 2027 (Stretch — estimated deadline ~October 2026, not yet announced)\n\n## Key References\n- Zhang et al. 'Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition' (arXiv 2510.04406, 2025)\n- Csillag et al. 'Extending Prediction-Powered Inference through Conformal Prediction' (arXiv 2510.16166, 2025)\n- Angelopoulos et al. 'Prediction-Powered Inference' (Science, 2023)\n- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)\n- Kato 'Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression' (arXiv 2511.08303, NeurIPS 2025)\n- Barber et al. 'Conformal prediction beyond exchangeability' (Annals of Statistics, 2023)\n- Alaa et al. 'Conformal Meta-learners for Predictive Inference of Individual Treatment Effects' (NeurIPS 2023)\n- Wang & Dobriban 'Optimal Decision-Making Based on Prediction Sets' (arXiv 2602.00989, 2026)\n- Lützow et al. 'Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting' (arXiv 2605.12341, 2026)\n- Xu et al. 'Conformal prediction for multi-dimensional time series by ellipsoidal sets' (ICML 2024)\n- Campos et al. 'Conformal Prediction for Natural Language Processing: A Survey' (TACL, 2024)\n- Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation (arXiv 2509.21660, 2025)\n- Lei & Candès 'Conformal Inference of Counterfactuals and Individual Treatment Effects' (JRSS-B, 2021)\n- DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)\n- Ma et al. 'LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding' (NeurIPS 2025)\n- Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)\n- Veitch et al. 'Adapting Text Embeddings for Causal Inference' (UAI 2020)\n- Barnatchez et al. 'Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding' (arXiv 2604.03772, 2026)\n- Vovk & Wang 'Conformal e-prediction in the presence of confounding' (arXiv 2603.11134, 2026)\n- Gasparin & Ramdas 'Improving the statistical efficiency of cross-conformal prediction' (arXiv 2503.01495, ICML 2025)\n- Chernozhukov et al. 'Double/debiased machine learning for treatment and structural parameters' (Econometrics Journal, 2018)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:30:42.838Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:30:42.838Z",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-20T03:30:42.850Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

⚠️ 致命前置问题：Venue Mismatch ⚠️

本 proposal 被要求评估投稿 CoRL 2026（Conference on Robot Learning）的中稿潜力。
然而，CoRL 的 scope 明确要求论文 "focus on a core robotics problem"，涵盖
机器人感知、控制、操控、运动、模仿学习、强化学习、sim-to-real 等方向。

本 proposal 是一篇纯粹的统计方法论论文——将 conformal prediction 和
prediction-powered inference 整合用于 LLM 文本抽取混杂因子下的因果推断。
应用场景是临床笔记（MIMIC-IV）、社交媒体数据，完全不涉及机器人。
Proposal 自身列出的目标会议也是 AAAI 2027 / ARR→EACL 2027 / AISTATS 2027。

结论：本 proposal 与 CoRL 2026 的 scope 完全不匹配，投 CoRL 主会的中稿概率
实质为 0%（desk reject）。以下评估将基于 proposal 自身适合的会议
（AAAI/AISTATS 级别 AI/统计方法论会议）进行 idea 质量评估，供后续流程参考。

========================================================================

【领域调研】:

1. Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential 
   Models via Residual Decomposition" (arXiv 2510.04406, Oct 2025):
   — 本 proposal Track A 的核心理论基础。提出两阶段 pipeline 的残差分解框架，
     用 FWER 控制校准各阶段参数。已验证存在，但原文处理的是供应链/股市等
     非因果场景，未涉及加权可交换性或因果估计。

2. Csillag et al. "Extending Prediction-Powered Inference through Conformal 
   Prediction" (arXiv 2510.16166, Oct 2025):
   — 本 proposal Track B 的核心基础。将 PPI 与 conformal set-predictor 结合，
     实现 Z-estimation 和 M-estimation 的有效推断。已验证存在。原文未涉及
     因果效应估计。

3. DoubleLingo (NAACL 2024, ACL Anthology):
   — 已验证。使用 LLM 在 DML 框架内进行因果估计，仅提供渐近保证，
     未量化 LLM 抽取噪声的有限样本不确定性。

4. Barnatchez et al. "Debiased ML for Conformal Prediction of Counterfactual 
   Outcomes Under Runtime Confounding" (arXiv 2604.03772, Apr 2026):
   — 已验证。处理的是训练时观测到但部署时缺失的混杂因子（runtime confounding），
     与本 proposal 的"噪声抽取"设定确实不同（missing vs. noisy）。
     Proposal 对此区分的描述准确。

5. Gasparin & Ramdas "Improving the statistical efficiency of cross-conformal 
   prediction" (arXiv 2503.01495, ICML 2025 poster):
   — 已验证。本 proposal 用于将三路数据划分降为两路，提升样本效率。
     工具性引用，使用合理。

6. Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025):
   — 已验证。将 PPI 扩展到因果推断，但使用的是点预测 imputation，
     非 conformal set-predictor。

7. Kato "Semi-Supervised Treatment Effect Estimation" (arXiv 2511.08303, 
   NeurIPS 2025):
   — 已验证。半监督因果效应估计，可解读为 PPI 框架下的工作。
     提供了效率界和有效估计量。

8. 直接竞争工作搜索结果：未找到任何现有工作直接将 conformal prediction
   + LLM confounder extraction + causal inference 三者结合。该交叉空白
   确实存在。

- 调研总结：conformal prediction × causal inference 是 2024-2026 年的活跃
  方向（系统综述 arXiv 2509.21660 覆盖 11 篇核心论文），但现有工作均假设
  混杂因子无误差观测。LLM 用于文本因果推断（DoubleLingo, Ma et al.）也是
  活跃方向，但仅提供渐近保证。这两条线尚未被连接。本 proposal 定位在
  这一交叉空白上，定位清晰，空白真实存在。

========================================================================

【Trivial Alternative 检验】:

最简单的替代方案：LLM 点预测抽取 + 标准 doubly robust 估计 + bootstrap 
置信区间。这正是 DoubleLingo 等工作的路线。

Proposal 的 claim 是：当 LLM 抽取噪声具有异质性时，bootstrap CI 会
undercover。这是一个合理的理论论点——measurement error 在因果推断中
确实会导致偏差，bootstrap 无法校正系统性的测量误差。

然而，第二个 trivial alternative 更具威胁：**直接使用 PPI（非 conformal 
版本）进行因果推断**（如 arXiv 2502.06343 已经做的），配合标准误差估计。
Track B 相对于 vanilla PPI causal inference 的增量价值在于用 conformal 
set-predictor 替代点预测 imputation，获得有限样本有效性而非渐近有效性。
这个增量是真实的，但边际性较强——在大样本下两者表现趋同。

对于 Track A，trivial alternative 是：对 LLM 抽取结果做 sensitivity 
analysis（如 Manski bounds 风格的 partial identification），不需要 
conformal prediction 机制也能给出包含真实效应的区间。Proposal 的增量
在于 conformal 框架能自适应地根据 LLM 质量调整区间宽度（|C| 小则窄），
而 Manski bounds 是全域最坏情况。这个区分有意义但需要实证验证优势大小。

总结：存在 trivial alternatives，但 proposal 相对于它们有可辨识的增量价值。
增量的大小取决于实验验证，属于"有意义但非压倒性"的增量。

========================================================================

【前提假设检验】:

核心逻辑链中有以下未经验证的关键假设：

1. **"Modular residual decomposition 在因果可交换性条件下成立"**
   — 这是 proposal 自认的主要理论贡献。Zhang et al. 的原始框架处理的是
   标准预测问题，不涉及加权可交换性（propensity weighting 导致的 
   non-exchangeability）。将其推广到 doubly robust pseudo-outcomes 需要
   新的证明。这不是"想当然"，但确实是未完成的理论工作。如果这一步
   证不出来，Track A 的理论基础就不存在。

2. **"Conformal prediction sets 足够小以使区间实用"**
   — Pilot analysis 表明 |C|≤2（K=5 时）才能使 widening 可控（~60%）。
   这要求 LLM 分类准确率极高（top-2 覆盖率 ≥ 1-α）。对于真实临床文本
   中的多类别抽取（如疾病严重程度），LLM 是否能达到这一水平是经验问题。
   如果不能，方法虽然"正确反映不确定性"，但实际产出的区间宽到无法
   指导决策——正确但无用。

3. **"连续嵌入 track 的 Lipschitz 连续性假设"**
   — Proposal 承认此 track 需要平滑估计器，排除了树模型。但即使用神经网络，
   128-256 维嵌入空间中的椭球 conformal sets 的体积增长极快，worst-case 
   优化可能导致极宽区间。Proposal 对此缺乏 pilot analysis（仅对 categorical 
   track 做了）。

4. **"Causal exchangeability 在 LLM 抽取噪声下仍然成立"**
   — 标准因果推断假设无未观测混杂。如果 LLM 抽取引入的"噪声"本质上
   是一种测量误差，那么 adjusted estimator 用的是带噪声的 confounder，
   可能违反无未观测混杂假设。Conformal sets 能否完全补偿这一点，
   取决于 conformal set 是否覆盖了真实值——这正是 conformal coverage 
   保证的，但前提是校准数据中有 ground-truth labels，回到了对标注数据
   的依赖。

========================================================================

【3 维度打分】:

1. Novelty: 【中】
   — 理由：交叉空白确实存在——搜索未找到任何直接竞争工作。但这是一篇
   典型的 "bridge paper"：将已有的 modular CP (Zhang et al. 2510.04406)、
   conformal PPI (Csillag et al. 2510.16166)、和 doubly robust causal 
   estimation (DoubleLingo/Ma et al.) 组合到一起。核心技术组件均为现有方法，
   novelty 主要在于 (a) 证明 modular decomposition 在因果设定下成立，
   (b) 显式 propensity score propagation 的处理。这些是非 trivial 的
   技术工作，但不是概念性突破。一个熟悉这三条文献线的审稿人看到这个
   idea 会说 "natural next step" 而非 "surprising"。

2. Significance: 【中偏强】
   — 理由：问题本身重要且时机好。LLM 用于文本因果推断正在快速增长
   （DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），但都缺乏有限
   样本保证。提供此保证有真实的实践价值，尤其在高风险场景（临床决策）。
   但实际 significance 受限于 conservatism：pilot analysis 显示方法
   仅在 LLM 质量高时实用（|C|≤2），这限制了适用范围。此外，目标受众
   相对小众（同时关注 conformal prediction + causal inference + NLP 的
   研究者）。

3. Related Work: 【强】
   — 理由：这是本 proposal 最突出的优点。对领域格局的覆盖极为全面：
   从 conformal ITE (Lei & Candès 2021, Alaa et al. NeurIPS 2023) 到 
   PPI causal (arXiv 2502.06343, Kato NeurIPS 2025)，到 LLM causal 
   (DoubleLingo, Ma et al.)，再到最新的 Barnatchez et al. (2604.03772) 
   和 Vovk & Wang (2603.11134)，均有准确覆盖和清晰区分。引用的论文
   经调研验证均真实存在，描述准确。差异化定位（noisy extraction vs. 
   missing confounders vs. confounding in prediction）逻辑清晰。

========================================================================

【概率估计】（针对 proposal 自身目标会议 AAAI/AISTATS 级别）: 
[22% - 32%] 中位 27%

【针对 CoRL 2026】: ≈0%（scope 完全不匹配，desk reject）

【估计理由】:
Novelty 评为"中"是主要限制上界的因素。这是一篇连接三条现有技术线的 
bridge paper，核心组件已存在，贡献在于证明组合在因果设定下成立 + 显式
propensity propagation 分析。对于 AAAI/AISTATS 的审稿人来说，这是一个
"natural extension"——方向正确、技术 sound、但不 surprising。

Significance 为"中偏强"提供了一定支撑：问题确实重要且时机好，如果
实验执行出色（coverage 保证 + 合理区间宽度），有望达到 30%+ 的上界。
但 conservatism 问题（仅在 LLM 质量高时实用）限制了 impact story。

Related work 为"强"是一个加分项，说明作者对领域理解深入，但 related 
work 的完备性不能弥补 novelty 的不足。

概率区间 22-32% 对应 rubric 中 "idea 有实质内核，方向正确，有真实的 
novelty delta，但核心发现如果 positive 审稿人可能会说 'I would have 
guessed this'" 的描述，略低于该档中位（因为 bridge paper 性质 + 
conservatism 限制实用性）。

【主要风险】:
1. **"Natural combination" 质疑**：审稿人可能认为将 modular CP + PPI + DR 
   estimation 组合在一起虽然技术上非 trivial，但概念上是 "obvious next step"，
   缺乏 surprising insight。这是 bridge paper 面临的系统性风险。
2. **Conservatism 导致实用性存疑**：如果实验中 conformal set size 普遍 ≥3
   （真实 LLM 在临床文本上的表现），区间可能宽到无实用价值，
   审稿人会质疑 "compared to just using bootstrap with a good LLM, 
   what do I gain in practice?"
```

Sources:
- [Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition](https://arxiv.org/abs/2510.04406)
- [Extending Prediction-Powered Inference through Conformal Prediction](https://arxiv.org/abs/2510.16166)
- [DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)](https://aclanthology.org/2024.naacl-short.71/)
- [Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding](https://arxiv.org/abs/2604.03772)
- [Improving the statistical efficiency of cross-conformal prediction (ICML 2025)](https://arxiv.org/abs/2503.01495)
- [Prediction-Powered Causal Inferences](https://arxiv.org/abs/2502.06343)
- [Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates](https://arxiv.org/abs/2511.08303)
- [A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation](https://arxiv.org/html/2509.21660)
- [Conformal Prediction for Causal Effects of Continuous Treatments](https://arxiv.org/abs/2407.03094)
- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile my analysis.

---

```
【阶段】: Triage

⚠️ 关键前置问题：严重的 VENUE MISMATCH ⚠️

本 proposal 被要求评估投稿 CoRL 2026（Conference on Robot Learning）的中稿潜力。
然而 CoRL 的核心 scope 是：robotic perception, control, manipulation, navigation, 
locomotion, driving, imitation learning, reinforcement learning for physical robots, 
robot foundation models 等。

本 proposal 是关于 conformal prediction + prediction-powered inference 用于 LLM
文本 confounder 提取后的因果推断——这是一篇纯粹的 统计方法论/因果推断/NLP 论文，
与机器人学习没有任何关联。proposal 自身列出的 target venues 也是 AAAI 2027、
ARR→EACL 2027、AISTATS 2027，均不包含 CoRL。

这篇论文投 CoRL 几乎必定 desk reject（scope 不匹配）。

以下评估将分两部分：(A) venue-agnostic 的 idea 质量评估，(B) CoRL 2026 特定概率。

═══════════════════════════════════════════════════
(A) VENUE-AGNOSTIC IDEA 质量评估（适用于 AAAI/AISTATS/NeurIPS 等）
═══════════════════════════════════════════════════

【领域调研】:
- Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential Models 
  via Residual Decomposition" (arXiv 2510.04406, 2025): 本 proposal 的 Track A 
  核心基础。提出了 two-stage pipeline 的模块化 conformal prediction 框架，通过 
  residual decomposition 实现 stage-wise 不确定性归因。原文应用于 supply chain 
  和 stock market，未涉及因果推断。proposal 的贡献是将其扩展到 causal setting 
  with weighted exchangeability。
  
- Csillag et al. "Extending Prediction-Powered Inference through Conformal 
  Prediction" (arXiv 2510.16166, 2025): Track B 的核心基础。将 PPI 与 conformal 
  set-predictor 结合，实现 Z-estimation 和 M-estimation 的有效推断。原文是通用 
  统计框架，未专门处理因果推断场景。proposal 将其扩展到 ATE 估计。

- Barnatchez et al. "Debiased ML for Conformal Prediction of Counterfactual 
  Outcomes Under Runtime Confounding" (arXiv 2604.03772, April 2026): 最直接的
  竞争工作。但处理的是 confounders MISSING at deployment（缺失）而非 noisy 
  extraction（有噪声）。proposal 对此区分是清晰且成立的。

- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025): 将 PPI 扩展到
  因果场景，使用 conditional calibration。但未使用 conformal set-predictor。

- Kato "Semi-Supervised Treatment Effect Estimation" (arXiv 2511.08303, 
  NeurIPS 2025): 理论上建立了 semi-supervised setting 下 treatment effect 
  estimation 的 efficiency bounds。是 PPI+causal 方向的理论基础。

- DoubleLingo (NAACL 2024): 在 DML 框架内使用 LLM 做 nuisance estimation，
  仅提供渐近保证。

- Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text 
  Confounding" (NeurIPS 2025): 处理 LLM 文本 confounding，但同样仅有渐近保证。

- Conformal Prediction for Medical Entity Extraction (arXiv 2603.00924, 2026): 
  将 conformal prediction 用于 LLM 医学实体提取，提供 FDR 保证。但仅处理
  extraction quality，未连接到下游因果推断。

- Gasparin & Ramdas "Improving Statistical Efficiency of Cross-Conformal 
  Prediction" (ICML 2025): proposal 用于减少 data split 的工具，是成熟技术。

- Singer et al. "Conformal Prediction for Astronomy Data with Measurement 
  Error" (MNRAS 2025): 唯一直接处理 measurement error + conformal prediction 
  的工作，但领域完全不同（天文学），且不涉及因果推断。

- 调研总结: 这个领域处于 conformal prediction × causal inference × LLM-based 
  text processing 三者交汇处，2025-2026 年各两两交叉都有活跃进展，但三者的
  完整统一（特别是 noisy extraction 而非 missing confounders）确实尚无直接先例。
  Proposal 的 gap identification 是准确的。

【Trivial Alternative 检验】:

存在两个需要认真回答的 trivial alternative 威胁：

1. **End-to-end black-box conformal prediction**: 不做模块化分解，直接对整个 
   pipeline（LLM extraction → causal estimation）做 black-box conformal 
   prediction。这会更简单，且同样提供 finite-sample 保证。Proposal 的增量价值
   在于：(a) 模块化分解可以 attribute uncertainty 到具体 stage，(b) 声称 FWER 
   控制比 Bonferroni 更 tight。但问题是：(a) 是 interpretability 收益（nice to 
   have 但非 essential），(b) 需要实验证明 tightness 提升有多大。如果 black-box 
   approach 的 interval 只宽 10-20%，模块化方法的复杂性就难以 justify。

2. **Standard measurement error correction + bootstrap**: 传统因果推断文献中
   有成熟的 measurement error correction 方法（SIMEX, regression calibration）。
   虽然这些是渐近方法，但配合 bootstrap 可能在实际中表现不差。proposal 声称 
   bootstrap "undercovers"，但这是需要实验验证的 claim，不是不证自明的。

增量价值结论：proposal 的真正增量在于 finite-sample guarantee 本身（vs 渐近
保证），以及对 noisy extraction 的 honest uncertainty quantification。但 trivial 
alternative 威胁是实质性的——必须在实验中展示 black-box CP 和 bootstrap 的 
interval 质量确实显著劣于模块化方法，否则 reviewers 会质疑复杂性是否 justified。

【前提假设检验】:

核心逻辑链中有以下未经验证的关键假设：

1. **"模块化 residual decomposition 在 causal exchangeability 条件下成立"** 
   —— 这是 proposal 声称的核心理论贡献，但 proposal 只说 "proving the modular 
   residual decomposition holds"，未给出证明思路或困难程度评估。Zhang et al. 
   (2025) 的原始 decomposition 假设标准 exchangeability，而 causal setting 
   需要 weighted exchangeability (Barber et al. 2023)。这个扩展是否 
   straightforward 还是 non-trivial，proposal 没有给出信号。如果证明是 trivial 
   的，理论贡献就很薄；如果证明是困难的，可能 10 周内无法完成。

2. **"Worst-case enumeration over conformal sets 产生的 conservatism 是可接受的"** 
   —— pilot analysis 显示 |C|=2 时 widening 60%，|C|=3 时 100%。这些数字是
   基于一个特定数值例子的 back-of-envelope 计算，不是一般性结果。实际数据中
   propensity score 分布和 outcome 函数形状可能导致更大或更小的 widening。
   关键假设是 "好的 LLM 通常能 achieve |C|≤2"，但这取决于 calibration 数据量
   和 LLM quality，在 clinical text 等困难场景中未必成立。

3. **"Conformal PPI 的 Z-estimation bound 在因果 setting 中不会过于 loose"** 
   —— Track B 的 ATE interval bound 包含 M·Err(C) 项，其中 M 是 influence 
   function 的 bounded range。在 doubly robust estimation 中，influence function 
   涉及 1/propensity score，如果 propensity 接近 0/1，M 可以很大，使得 
   bound 变得 vacuous。

4. **"连续 embedding track 的 ellipsoidal conformal sets + convex relaxation 
   在 128-256 维度是 tractable 且 meaningful 的"** —— 高维 conformal sets 
   体积随维度指数增长（curse of dimensionality），128-256 维的 ellipsoidal 
   sets 可能覆盖了 embedding space 的大部分，使 worst-case bounds trivially 
   wide。proposal 承认限制于 smooth nuisance estimators，但未分析维度对 
   interval width 的影响。

【3 维度打分】:

1. Novelty: 【中】
   理由：proposal 准确识别了一个真实存在的 gap——三个成熟子领域（modular CP, 
   conformal PPI, LLM-based causal inference）的交汇处确实没有被直接 addressed。
   与 Barnatchez et al. (2604.03772) 的区分（noisy vs. missing confounders）是
   清晰且有意义的。然而，核心方法论是 "将 Zhang et al. 2025 的框架 + Csillag 
   et al. 2025 的框架应用到 causal setting"——这是 combination novelty 而非 
   conceptual novelty。审稿人看到这篇论文时，反应更可能是 "yes, this combination 
   makes sense and someone should do it" 而不是 "this is a surprising insight I 
   wouldn't have thought of"。Singer et al. (MNRAS 2025) 已在天文学中处理了
   measurement error + CP 的组合（虽然不涉及因果推断），说明 "CP for noisy 
   covariates" 不是全新概念。Novelty 的实质深度取决于 weighted exchangeability 
   proof 的 non-triviality，但 proposal 未提供足够信息判断。

2. Significance: 【中偏强】
   理由：研究问题本身很重要——LLM-based confounder extraction 正在成为 text-based 
   causal inference 的标准实践（DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），
   而这些方法都缺乏 finite-sample guarantee。随着 LLM 在 clinical NLP 和 social 
   science 中的部署扩大，对 extraction noise 的 honest UQ 有明确需求。但 
   significance 受限于：(a) 实际用户群体较窄（做 text-based causal inference 的
   人本身就是小众），(b) interval widening 60-100% 可能让 practitioners 觉得
   方法 "too conservative to be useful"，(c) 如果核心发现是 "conformal methods 
   maintain coverage but with wider intervals"，这几乎是 by construction 的结论，
   不 surprising。

3. Related Work: 【强】
   理由：这是 proposal 最突出的优点。对近期文献（直到 2026 年 4-6 月）的覆盖非常
   全面，包括 Barnatchez et al. (April 2026), Vovk & Wang (March 2026), 
   Lützow et al. (2026), Gasparin & Ramdas (ICML 2025) 等非常新的工作。与
   最相关竞争工作的 differentiation 清晰且有说服力（特别是 noisy extraction 
   vs. missing confounders 的区分）。引用的论文经验证均真实存在且描述准确。
   Landscape section 对三个子领域的 gap 分析是系统性的。

═══════════════════════════════════════════════════
(B) CoRL 2026 特定评估
═══════════════════════════════════════════════════

CoRL (Conference on Robot Learning) 的 scope 是 robot learning：robotic 
perception, control, manipulation, navigation, locomotion, driving, flight, 
imitation learning, RL for physical robots, robot foundation models 等。

本 proposal 是关于 conformal prediction 用于 LLM 文本 confounder 提取后的
因果推断——与机器人学习没有任何实质性关联。proposal 自身的 target venues 
(AAAI 2027, ARR→EACL 2027, AISTATS 2027) 也不包含 CoRL。

即使忽略 scope 问题只看 idea 质量，这篇论文在 CoRL 也找不到合适的 reviewer——
该社区的审稿人不具备评审 causal inference + conformal prediction 理论贡献
的背景。

【概率估计 — CoRL 2026】: [1% - 5%] 中位 2%
【估计理由 — CoRL】: 
Scope 完全不匹配是 decisive factor。CoRL 关注 robot learning，本文是纯粹的
统计方法论/因果推断/NLP 工作。极高概率 desk reject。即使进入 review，reviewer 
pool 也不匹配，无法获得公正评审。1-5% 的非零下界仅反映 "AC 误判 scope" 的
极小概率。

【概率估计 — Venue-Agnostic（AAAI/AISTATS 级别会议）】: [20% - 35%] 中位 27%
【估计理由 — Venue-Agnostic】: 
Idea 的 novelty 是 combination-level（中），将两个现有框架 extend 到新 setting，
gap identification 准确但 "someone should do this" 性质明显。Significance 中偏强
（问题重要但用户群窄、interval widening 可能 limit 实际价值）。Related work 
coverage 强——这是最好的维度。上界受限于 novelty 维度：核心发现若 positive，
审稿人更可能说 "makes sense" 而非 "surprising"。下界由 significance 和 related 
work 支撑——问题真实、gap 确实存在、执行如果 solid 可以 pass。对于 AAAI/AISTATS 
这类会议，combination novelty + solid execution 可以中稿，但需要实验显著超越 
trivial alternatives。

【主要风险】:
1. **[Scope — CoRL 致命风险] 论文与 CoRL 的 scope 完全不匹配**，几乎必定 
   desk reject。这不是 idea 质量问题，而是 venue 选择错误。建议维持原定的 
   AAAI 2027 / AISTATS 2027 投稿计划。
   
2. **[Idea 层面 — Trivial Alternative 威胁] Black-box end-to-end conformal 
   prediction 可能以远低的复杂度达到类似效果**。如果模块化分解相比 black-box 
   CP 的 interval width 改善不显著（<15-20%），整个方法论复杂性的 justification 
   就会被审稿人质疑。这是实验无法完全补救的 idea 层面问题——如果 black-box 
   approach 效果相近，说明模块化分解在这个 application 中 value-add 有限。

3. **[Idea 层面 — Conservatism 可能使方法实际无用] 60-100% interval widening 
   在实际临床决策中可能被视为 too conservative**。如果主要实验结果是 "our method 
   has correct coverage but intervals are 2x wider than oracle"，reviewers 可能
   认为这是一个 "correct but useless" 的方法。
```

**总结**：这是一篇 idea 质量中等偏上的 combination paper，gap identification 准确，related work 覆盖优秀，但核心 novelty 是 framework integration 而非 conceptual breakthrough。**然而投稿 CoRL 2026 是严重的 venue mismatch**——CoRL 是机器人学习会议，本文是统计方法论/因果推断工作，几乎必定被 desk reject。强烈建议维持 proposal 自身原定的 target venues（AAAI 2027 / AISTATS 2027）。

Sources:
- [Modular and Adaptive Conformal Prediction for Sequential Models (Zhang et al. 2025)](https://arxiv.org/abs/2510.04406)
- [Extending Prediction-Powered Inference through Conformal Prediction (Csillag et al. 2025)](https://arxiv.org/abs/2510.16166)
- [Debiased ML for Conformal Prediction Under Runtime Confounding (Barnatchez et al. 2026)](https://arxiv.org/abs/2604.03772)
- [Prediction-Powered Causal Inferences (2025)](https://arxiv.org/abs/2502.06343)
- [Semi-Supervised Treatment Effect Estimation (Kato, NeurIPS 2025)](https://arxiv.org/abs/2511.08303)
- [Improving Statistical Efficiency of Cross-Conformal Prediction (Gasparin & Ramdas, ICML 2025)](https://arxiv.org/abs/2503.01495)
- [Systematic Review of Conformal Inference for Treatment Effects](https://arxiv.org/html/2509.21660)
- [DoubleLingo: Causal Estimation with LLMs (NAACL 2024)](https://aclanthology.org/2024.naacl-short.71/)
- [LLM-Driven Treatment Effect Estimation (Ma et al. NeurIPS 2025)](https://openreview.net/forum?id=sv41aaGTit)
- [Conformal Prediction for Astronomy with Measurement Error (MNRAS 2025)](https://arxiv.org/abs/2412.10544)
- [Conformal e-prediction under confounding (Vovk & Wang 2026)](https://arxiv.org/pdf/2603.11134)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)
- [Conformal Prediction for Medical Entity Extraction (2026)](https://arxiv.org/html/2603.00924)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
调研完成，现在我可以给出完整的入口评估。

---

```
【阶段】: Triage

【领域调研】:
- Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition" (arXiv 2510.04406, Oct 2025): 本 proposal Track A 的核心技术基础。MIT 团队提出的 two-stage pipeline 的模块化 CP 框架，通过残差分解实现跨 stage FWER 控制。已验证于供应链和股市数据，但 **未涉及因果推断设定**（无 weighted exchangeability、无 propensity score 传播）。Proposal 声称将其推广到因果设定的 claim 有据。
- Csillag et al. "Extending Prediction-Powered Inference through Conformal Prediction" (arXiv 2510.16166, Oct 2025): Track B 的核心技术基础。将 CP set-predictor 引入 PPI 框架，实现 Z-estimation、M-estimation 等下游推断的 finite-sample 有效性。该工作 **未涉及因果推断（ATE/ITE 估计）**，因此 proposal 将其扩展到 causal PPI 是未被覆盖的。
- DoubleLingo (NAACL 2024, ACL Anthology): 用 LLM 作为 DML 框架中的 nuisance model，从文本数据中做因果估计。**仅提供渐近保证**，不处理 LLM 抽取噪声的 finite-sample UQ。Proposal 对其定位准确。
- Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding" (NeurIPS 2025, arXiv 2507.02843): 解决训练时有完整 confounders、推断时仅有文本描述的问题。使用 doubly robust learner + LLM。与本 proposal 问题设定不同（训练/推断时的信息不对称 vs. 全程噪声抽取），但都在 LLM + 因果推断的大方向上。**仅渐近保证**。
- Barnatchez et al. "Debiased ML for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding" (arXiv 2604.03772, April 2026): 处理 confounders 在部署时 **完全缺失** 的场景（runtime confounding），通过 semiparametric debiasing 边际化未观测变量。与本 proposal 的 **noisy extraction**（变量存在但有噪声）设定本质不同。Proposal 对其区分清晰。
- Prediction-Powered Causal Inferences (NeurIPS 2025 poster, OpenReview): 将 PPI 应用于因果推断中的未标注目标实验，关注跨实验 transferability，**未使用 conformal sets 来量化 imputed covariates 的不确定性**。
- Systematic Review of Conformal Inference for Treatment Effects (arXiv 2509.21660, 2025): 综述覆盖 11 篇核心论文（Lei & Candès 2021, Alaa et al. NeurIPS 2023, KDD 2024 wTCP-DR 等）。确认所有现有 conformal ITE 方法 **假设 confounders 无误差观测**。
- Vovk & Wang "Conformal e-prediction in the presence of confounding" (arXiv 2603.11134, March 2026): 用 e-values 处理 X-Y 之间的 confounding，目标是预测而非因果效应估计。与本 proposal 互补但不竞争。
- 调研总结: 在"conformal prediction × causal inference"和"LLM × text-based causal inference"两个活跃领域的交叉点，**确实存在一个未被填补的空缺**：没有现有工作提供 LLM 抽取文本 confounders 下治疗效应估计的 finite-sample coverage 保证。但这个空缺更多是"自然的下一步整合"，而非"根本性的方法论突破"。

【Trivial Alternative 检验】:
存在至少三个更简单的替代方案需要考量：
1. **Bootstrap + multiple imputation**：经典处理含噪/缺失协变量的方法。对 LLM 多次抽取结果做 multiple imputation + Rubin's combining rules，可能在实践中产生类似宽度的置信区间，无需 conformal 框架的复杂性。Proposal 提到 bootstrap "undercovers"，但这是一个需要实验验证的 claim，而非理论定论——适当修正的 bootstrap（如 wild bootstrap for DML）在有限样本下表现通常尚可。
2. **贝叶斯方法**：对 LLM 抽取不确定性建立先验，通过后验边际化传播到治疗效应估计。贝叶斯 DML 已有相关工作。
3. **简单的 sensitivity analysis**：Manski bounds 或 Rosenbaum sensitivity analysis 风格的方法，对 confounder 误分类率做最坏情况分析。

**增量价值在哪？** Proposal 的核心增量是 **distribution-free finite-sample guarantee**——不依赖渐近理论或分布假设。这确实是上述替代方案不具备的。但实际价值取决于 intervals 是否足够紧以提供有用信息，而 pilot analysis 显示 60-100% 的 widening 已经相当可观。

【前提假设检验】:
核心 claim 的逻辑链中存在以下未经验证的关键假设：
1. **LLM 抽取误差可被 conformal prediction 有效捕获**：CP 要求（近似）exchangeability。LLM 的抽取误差可能对特定 subpopulation 系统性偏差（如对少数族裔的临床描述更容易误判严重程度），此时 marginal coverage 保证可能掩盖 conditional miscoverage。Proposal 未讨论这一点。
2. **Weighted exchangeability 在 DR pseudo-outcomes 下成立**：这是 proposal 自认的理论贡献核心，但尚未证明。如果证明过程中需要额外条件（如 positivity 加强版、nuisance 函数收敛率约束），实际适用性可能大幅缩小。
3. **Worst-case enumeration 的保守性是"可接受的"**：Pilot analysis 基于一组特定数值假设。在真实临床场景中，propensity score 的变异可能更极端（如罕见疾病），导致 intervals 实际上 vacuously wide。
4. **连续 embedding track 的凸松弛质量**：Taylor 展开 + Lipschitz 连续性在 128-256 维椭球上的近似质量未知，且限制只能用 smooth nuisance estimators，排除了 GBDT 等实践中最常用的方法。

【3 维度打分】:
  1. Novelty: 中 — 
     该 proposal 正确识别了一个真实存在的研究空缺：systematic review (arXiv 2509.21660) 确认所有 conformal ITE 方法假设无误差 confounders；DoubleLingo (NAACL 2024) 和 Ma et al. (NeurIPS 2025) 仅提供渐近保证；Zhang et al. (2510.04406) 的模块化 CP 未涉及因果设定；Csillag et al. (2510.16166) 的 conformal PPI 未涉及因果推断。空缺真实存在。
     然而，novelty 本质上是 **integrative**：将 Zhang et al. 的 framework 应用到 "LLM 抽取 → 因果估计" 的 pipeline，将 Csillag et al. 的 conformal PPI 扩展到 ATE 估计。理论贡献（weighted exchangeability 下 DR pseudo-outcomes 的模块化残差分解）是对已有框架在新设定下的推广，而非方法论上的根本创新。对领域熟悉的审稿人可能会说 "natural extension" 而非 "surprising contribution"。

  2. Significance: 中 — 
     问题本身有实际意义：LLM 从文本抽取 confounders 是 causal NLP 的活跃方向（DoubleLingo, Ma et al.），而抽取噪声确实威胁 causal estimate 的有效性。但：(a) 受众较窄——同时关心 "text-based causal inference" + "finite-sample guarantees" + "LLM extraction noise" 的研究者群体有限；(b) 如果核心结果是 "我们的方法在 LLM 噪声下维持 coverage，但 intervals 比 oracle 宽 60-100%"，大多数审稿人会说 "I would have guessed this"——coverage 保证是 conformal 方法的固有属性，而保守性是 worst-case 推理的固有代价；(c) 对更广泛的 NLP/ML 社区影响有限，主要服务于方法论研究者。

  3. Related Work: 强 — 
     Proposal 对领域的覆盖非常全面，对每个相关工作的定位准确且区分清晰。特别突出的是：(a) 对 Barnatchez et al. (2604.03772) 的区分（missing vs. noisy）准确且实质；(b) 对 Vovk & Wang (2603.11134) 的 e-value 方法的定位恰当；(c) 对 DoubleLingo / Ma et al. 的渐近保证局限性分析中肯；(d) 引用的所有关键论文均经验证真实存在且描述准确；(e) 对三条独立研究线索的交汇时机判断合理。这是一个对该领域有深入了解的研究者写的 proposal。

【概率估计】: 22% - 33%, 中位 27%

【估计理由】: 
Related Work 维度强（定位清晰、差异化充分），保证了论文不会因 "忽视相关工作" 被拒——这提高了下限。但 Novelty 和 Significance 均为"中"限制了上界：
- Novelty 层面，integrative contribution 在顶会中通常需要额外的"惊喜因素"来补偿。审稿人极可能评价为 "technically sound but incremental"——将两个已有 framework 应用到新场景。
- Significance 层面，核心 finding（如果 positive）的 surprise factor 低。"Conformal 方法在噪声下维持 coverage 但更保守" 是几乎可以先验预测的结论。
- 对于 AISTATS（proposal 的 stretch target），这种方法论整合型工作相对更被接受（~30-33%）；对于 AAAI（primary target），偏理论/niche 的 statistical methodology 可能不占优势（~22-25%）。

**特别注意**：Proposal 系统提示中提到 CoRL 2026，但本 proposal 与机器人学习完全无关。如果确实投稿 CoRL，中稿概率接近 0%。以下评估基于 proposal 自身声明的目标会议（AAAI 2027 / ARR / AISTATS 2027）。

【主要风险】:
1. **"Natural extension" 感过强**：最大的拒稿风险在于审稿人认为这是将 Zhang et al. + Csillag et al. 的框架"搬运"到因果设定，理论贡献（weighted exchangeability 下的证明）不足以构成独立贡献。如果证明过程中不出现非 trivial 的技术挑战（如需要全新的分析工具），这一风险尤为突出。
2. **实际价值 vs. 保守性的 trade-off 不利**：Pilot analysis 显示即使 good LLM (|C|=2) 也有 60% widening。审稿人可能质疑：在 intervals 如此宽的情况下，这些 finite-sample 保证相对于渐近方法（或简单的 bootstrap with correction）的实际增量价值有多大？如果实验中 bootstrap 表现"足够好"（尽管理论上 undercovers），方法的卖点将被严重削弱。
```

Sources:
- [Systematic Review of Conformal Inference for Treatment Effects](https://arxiv.org/html/2509.21660v1)
- [Zhang et al. - Modular Conformal Prediction](https://arxiv.org/abs/2510.04406)
- [Csillag et al. - Extending PPI through CP](https://arxiv.org/abs/2510.16166)
- [DoubleLingo - NAACL 2024](https://aclanthology.org/2024.naacl-short.71/)
- [Ma et al. - LLM-Driven Treatment Effect Estimation (NeurIPS 2025)](https://arxiv.org/abs/2507.02843)
- [Barnatchez et al. - Runtime Confounding](https://arxiv.org/abs/2604.03772)
- [Prediction-Powered Causal Inferences (NeurIPS 2025)](https://openreview.net/forum?id=HOa6LTIjyn)
- [Vovk & Wang - Conformal e-prediction under confounding](https://arxiv.org/pdf/2603.11134)
- [Conformal Prediction for Causal Effects of Continuous Treatments](https://arxiv.org/abs/2407.03094)
- [LLM-based Agents for Confounder Discovery](https://arxiv.org/abs/2508.07221)


【原始 proposal（允许参考但不是主要依据）】:
# Conformal and Prediction-Powered Guarantees for Causal Inference with LLM-Extracted Text Confounders

## Description
We propose ConformalPPITextCausal, a framework providing finite-sample coverage guarantees for treatment effects estimated using LLM-extracted text confounders. Current methods (DoubleLingo, Ma et al.) rely on asymptotic guarantees that break down when LLM extraction introduces unquantified heterogeneous noise. Our dual-track approach addresses this via: Track A (ITE intervals) — adapting modular conformal prediction (Zhang et al. 2025) to a causal two-stage pipeline where Stage 1 produces conformal prediction sets over LLM-extracted categorical confounders (with worst-case pseudo-outcome enumeration including explicit propensity score propagation, O(|C|) per unit) or low-dimensional Matryoshka embeddings (with ellipsoidal sets and convex relaxation restricted to smooth nuisance estimators), and Stage 2 constructs doubly robust treatment effect intervals with FWER-controlled coverage tighter than Bonferroni; Track B (ATE intervals) — extending conformal prediction-powered inference (Csillag et al. 2025) to the causal setting, where a small expert-labeled and large LLM-imputed dataset yield valid confidence intervals via Z-estimation with conformal set-predictors. Cross-conformal calibration (Gasparin & Ramdas, ICML 2025) reduces the three-way data split to two-way, improving sample efficiency for labeled-data-scarce settings. A pilot conservatism analysis shows practical viability: for K=5 confounder categories, interval widening is ~60% with conformal set size |C|=2 (good LLM) and ~100% with |C|=3 (decent LLM), driven primarily by propensity score variation across conformal set members. The method is practically useful when the LLM achieves small conformal sets and correctly signals insufficient information otherwise. We differentiate from Barnatchez et al. (2604.03772), who handle missing confounders at deployment via semiparametric debiasing — a complementary but distinct setting from our noisy-extraction framework. The genuine theoretical contribution is proving the modular residual decomposition holds under causal exchangeability conditions specific to doubly robust pseudo-outcomes with explicit propensity propagation. Experiments on semi-synthetic MIMIC-IV clinical notes, social media data, and synthetic benchmarks demonstrate maintained nominal coverage where bootstrap alternatives undercover, with a dedicated conservatism experiment varying |C|/K to validate the pilot analysis.

## Core Problem
Causal inference from observational text data (clinical notes, social media, policy documents) requires adjusting for confounders embedded in unstructured text. Modern LLMs can extract these confounders, but extraction is imperfect — introducing measurement error that invalidates standard causal estimators' asymptotic guarantees. No existing framework provides finite-sample coverage guarantees for treatment effect estimates when confounders are extracted by a fallible LLM. Naive approaches (plugging in LLM point predictions as if they were ground truth) can produce arbitrarily biased causal conclusions when extraction noise is heterogeneous across subpopulations.

## Opportunity
Three independent research threads have matured to the point where they can be unified into a principled solution: (1) modular conformal prediction for sequential pipelines (Zhang et al. 2025, arXiv 2510.04406) provides a residual decomposition framework that controls family-wise error across pipeline stages without resorting to loose Bonferroni corrections; (2) prediction-powered inference extended through conformal prediction (Csillag et al. 2025, arXiv 2510.16166) yields valid population-level confidence intervals when a prediction model (here, the LLM) imputes covariates on a large unlabeled set alongside a small human-labeled set; and (3) conformal meta-learners for individual treatment effects (Alaa et al. NeurIPS 2023) provide conformal intervals for heterogeneous effects but assume perfectly observed confounders. Additionally, Matryoshka embedding models (Qwen3-Embedding-8B) now support flexible dimensionality from 32 to 4096, making conformal prediction over embedding spaces tractable at reduced dimensions. Recent work on conformal prediction under confounding — including Barnatchez et al. (arXiv 2604.03772) on runtime confounding (missing confounders at deployment) and Vovk & Wang (arXiv 2603.11134) on conformal e-prediction — demonstrates growing interest but targets distinct problem settings from ours (noisy extraction vs. missing variables, and e-values for prediction vs. p-values for treatment effects). By bridging these threads, we can deliver both individual-level (ITE) and population-level (ATE) treatment effect intervals that honestly account for LLM extraction uncertainty — a capability no current method provides.

## Landscape
The intersection of conformal prediction and causal inference has seen rapid growth (Systematic Review, arXiv 2509.21660, covering 11 key papers), but existing conformal ITE methods (Lei & Candès JRSS-B 2021; Alaa et al. NeurIPS 2023; KDD 2024 wTCP-DR) assume confounders are observed without error. The conformal prediction for NLP survey (Campos et al. TACL 2024) covers classification, QA, and generation quality but not downstream causal validity. Prediction-powered inference (Angelopoulos et al. Science 2023) and its causal extensions (arXiv 2502.06343; Kato arXiv 2511.08303 NeurIPS 2025) address the labeled/unlabeled split for treatment effects but do not incorporate conformal sets for the imputed covariates. Zhang et al. (2025) handle sequential model pipelines with modular conformal guarantees but do not treat the causal setting or weighted exchangeability. DoubleLingo (NAACL 2024) and Ma et al. (NeurIPS 2025) use LLMs within doubly robust causal estimators for text data but provide only asymptotic guarantees with no finite-sample uncertainty quantification for LLM extraction noise. Multi-variable conformal prediction (Lützow et al. arXiv 2605.12341, 2026) and ellipsoidal conformal sets (Xu et al. ICML 2024) now provide tractable geometric tools for moderate-dimensional conformal regions.

Two recent works merit explicit differentiation: Barnatchez et al. (arXiv 2604.03772, April 2026) address conformal prediction for counterfactual outcomes under 'runtime confounding' — where confounders measured in training are entirely MISSING at deployment. Their semiparametric debiasing approach marginalizes over unobserved confounders via multiply-robust influence functions, assuming Y(a)⊥S|V (systematic differences explained by the observed subset V). Our setting is fundamentally different: all confounders are present in the text and extracted by the LLM, but with NOISE — the confounders are measured with error, not missing entirely. Their debiasing marginalizes over missing variables; our conformal sets quantify extraction uncertainty over observed-but-noisy variables. Vovk & Wang (arXiv 2603.11134, March 2026) extend conformal e-prediction to handle observed confounding between X and Y using e-values (nonnegative random variables with expectation ≤ 1) rather than p-values. While e-values provide attractive anytime-valid guarantees under optional stopping, their framework targets prediction of Y given X under confounding, not treatment effect estimation. Our framework uses standard conformal prediction sets combined with PPI, targeting ITE/ATE estimation — a complementary but distinct goal. The e-value approach could be an interesting alternative foundation for future work.

The gap we fill is the integration of modular conformal prediction and conformal PPI into a unified framework for the two-stage pipeline of LLM confounder extraction followed by causal effect estimation, with proven finite-sample validity under noisy (not missing) confounder extraction.

## Approach
We propose a dual-track framework, ConformalPPITextCausal, for valid causal inference when text confounders are extracted by an LLM.

**Data Splitting and Sample Efficiency.** The baseline design uses a three-way data split: (S1) training data for fine-tuning the LLM extraction model and fitting nuisance functions (propensity score, outcome regression), (S2) calibration data for Stage 1 conformal sets on the extracted confounders, and (S3) calibration data for Stage 2 conformal intervals on treatment effects. To address sample efficiency — critical for clinical text datasets like MIMIC-IV where expert-labeled samples are expensive — we propose two improvements: (i) K-fold cross-fitting for nuisance function estimation within S1, following Chernozhukov et al. (2018) DML, which uses all training data for both estimation and evaluation; (ii) cross-conformal calibration for Stage 1, following Gasparin & Ramdas (ICML 2025, arXiv 2503.01495), which achieves coverage ≥ 1−2α₁ using K-fold rotation rather than a dedicated hold-out set, effectively merging S2 into S1 and reducing the three-way split to a two-way split (train+Stage1-calibrate vs. Stage2-calibrate). The coverage cost (1−2α₁ vs. 1−α₁) is manageable by setting α₁ conservatively (e.g., α₁=0.025 for effective 95% Stage 1 coverage). We discuss minimum sample size requirements: Stage 2 calibration requires n₃ ≥ ⌈1/α₂⌉ ≈ 100-200 for reliable conformal quantiles at α₂=0.05, and we recommend n_total ≥ 500 for the full pipeline, with n₃ ≥ 150 reserved for Stage 2. For very small labeled datasets (n < 300), Track B (PPI) is preferred as it leverages large unlabeled corpora.

**Track A — Modular Conformal ITE Intervals.** We adapt the residual decomposition of Zhang et al. (2025), where the total prediction residual R decomposes as R ≤ ΔR₁ + R₂, with Stage 1 = LLM confounder extraction and Stage 2 = doubly robust pseudo-outcome estimation.

In the primary setting, the LLM extracts CATEGORICAL confounders (e.g., disease severity ∈ {mild, moderate, severe}, smoking status ∈ {never, former, current}) via prompted classification. Conformal prediction sets for classification are natural finite sets with guaranteed coverage.

**Explicit Propensity Score Propagation.** The worst-case pseudo-outcome over the conformal set is computed by full enumeration with explicit propagation through BOTH the outcome regression AND the propensity score. For each possible confounder value c ∈ C(x), the DR pseudo-outcome is:

φ̂(c; Yᵢ, Aᵢ) = [μ̂₁(c) − μ̂₀(c)] + Aᵢ·(Yᵢ − μ̂₁(c))/ê(c) − (1−Aᵢ)·(Yᵢ − μ̂₀(c))/(1−ê(c))

Critically, different confounder values c yield different propensity scores ê(c), which enter the augmentation term as 1/ê(c) (for treated) or 1/(1−ê(c)) (for control). This propensity variation is a distinct and compounding source of uncertainty beyond outcome regression variation. The augmentation term amplifies when propensity scores are extreme: a confounder value with ê(c)=0.1 magnifies residuals 10×. The worst-case interval is [min_c φ̂(c), max_c φ̂(c)] with complexity O(|C|) per unit. We recommend propensity score trimming (truncating ê(c) to [0.05, 0.95]) to prevent a single extreme-propensity confounder value from dominating the interval.

**Pilot Conservatism Analysis.** We provide a back-of-envelope quantification of interval widening due to worst-case enumeration. Consider a clinical setting with K=5 severity categories {none, mild, moderate, severe, critical} and realistic nuisance function values:

| Category | μ̂₁(c) | μ̂₀(c) | ê(c) | CATE |
|----------|--------|--------|-------|------|
| none     | 0.40   | 0.30   | 0.50  | 0.10 |
| mild     | 0.50   | 0.35   | 0.45  | 0.15 |
| moderate | 0.60   | 0.40   | 0.40  | 0.20 |
| severe   | 0.72   | 0.45   | 0.35  | 0.27 |
| critical | 0.85   | 0.50   | 0.25  | 0.35 |

For a treated patient with Y=0.65 and true severity=moderate, the DR pseudo-outcomes across categories are: φ̂(none)=0.60, φ̂(mild)=0.48, φ̂(moderate)=0.33, φ̂(severe)=0.07, φ̂(critical)=−0.45. The variation is dominated by the augmentation term (Y−μ̂₁(c))/ê(c), where propensity changes from 0.50 to 0.25 amplify residuals 2×. The extraction uncertainty width (Δφ = max−min over C(x)) for different conformal set sizes:

- |C|=1 (excellent LLM, singleton): Δφ=0, no widening vs. oracle.
- |C|=2 (good LLM, e.g., {moderate, severe}): Δφ≈0.26, widening ≈ 60% over oracle CI width of ~0.40.
- |C|=3 (decent LLM, e.g., {mild, moderate, severe}): Δφ≈0.41, widening ≈ 100% over oracle.
- |C|=4+ (poor LLM): Δφ>1.0, intervals become vacuously wide — correctly reflecting that the LLM provides insufficient information for credible causal conclusions.

The general widening ratio is approximately W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle, where Δ_CATE is the CATE variation across the conformal set, |r| is the outcome residual magnitude, and Δ(1/ê) is the inverse propensity variation. Key practical determinants: (a) conformal set size |C|/K — the LLM quality directly controls conservatism; (b) propensity score stability across confounder categories — good overlap reduces widening; (c) outcome residual magnitude — well-fitted outcome models reduce augmentation-driven widening. The method is practically useful (W < 2) when the LLM achieves conformal set size |C| ≤ 2 for K=5 categories, and correctly signals 'insufficient information' otherwise.

For the secondary continuous track, we use Qwen3-Embedding-8B with Matryoshka dimensionality reduction to 128–256 dimensions, construct ellipsoidal conformal sets (Xu et al. ICML 2024; Lützow et al. 2026), and bound worst-case pseudo-outcomes via convex relaxation: local Lipschitz continuity of nuisance functions plus first-order Taylor expansion over the ellipsoid, following the decision-theoretic framework of Wang & Dobriban (arXiv 2602.00989, 2026). **Important restriction**: the convex relaxation via Lipschitz continuity and Taylor expansion requires smooth nuisance estimators. This is compatible with neural network outcome models (e.g., TARNet, DragonNet) and kernel methods, but NOT with tree-based models (gradient-boosted trees, random forests) that are piecewise constant with jump discontinuities. We therefore restrict the continuous embedding track to smooth nuisance estimators. Note that the categorical track (primary) works with ANY nuisance estimator, including tree-based methods, since worst-case computation is by direct enumeration without smoothness assumptions. The modular framework's FWER control across both stages yields provably tighter intervals than naive Bonferroni.

**Track B — Conformal PPI for ATE Intervals.** We apply the conformal PPI framework of Csillag et al. (2025) to estimate average treatment effects. The LLM serves as the prediction model in the PPI sense: a small human-labeled dataset has expert-annotated confounders, and a large dataset has LLM-extracted confounders. The conformal set-predictor from Stage 1 replaces point imputation, yielding valid ATE confidence intervals via Z-estimation: E[inf φ(C(X))] − M·Err(C) ≤ ATE ≤ E[sup φ(C(X))] + M·Err(C), where M is the bounded range of the influence function and Err(C) is the conformal miscoverage rate. This extends PPI causal inference (arXiv 2502.06343) by using conformal rather than point imputation, providing finite-sample validity without distributional assumptions on the LLM. Track B is especially suited to small-labeled-data settings (MIMIC-IV) because it leverages large unlabeled corpora.

We evaluate on three benchmarks: (1) semi-synthetic MIMIC-IV clinical notes (treatment escalation effect on ICU outcomes, disease severity as text confounder), (2) semi-synthetic social media data (content moderation effect on engagement, toxicity level as confounder), and (3) fully synthetic data with known ground-truth for calibration validation. Key metrics: empirical coverage at 90%/95% nominal levels, interval width relative to oracle (perfectly observed confounders) and bootstrap baselines, widening ratio W as a function of conformal set size and propensity overlap, and sensitivity to LLM extraction quality via deliberately degraded models. We include a dedicated conservatism experiment varying |C|/K from 0.2 to 0.8 to empirically validate the pilot analysis above.

We are transparent that worst-case reasoning over conformal sets introduces conservatism relative to oracle methods. The honest framing: our intervals maintain nominal coverage where bootstrap intervals undercover due to LLM extraction noise, with comparable width when LLM quality is high (|C|=1-2). The conservatism correctly reflects true uncertainty in the LLM-as-measurement-instrument setting, and the pilot analysis above shows it is quantifiably bounded for reasonable LLM quality.

## Resource Estimate
{'manual': {'gpu_hours': '200-300', 'timeline': '10 weeks (targeting AAAI 2027 July 28 deadline)', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'breakdown': 'Weeks 1-2: Formalize theoretical framework (modular decomposition under weighted exchangeability, conformal PPI ATE estimator, cross-conformal Stage 1 calibration). Weeks 3-4: Implement cross-fitted pipeline, categorical conformal extraction, worst-case enumeration with explicit propensity propagation. Weeks 5-6: Implement continuous embedding track (Matryoshka 128-256d, ellipsoidal sets, convex relaxation with smooth nuisance estimators) and PPI ATE track. Weeks 7-8: Experiments on MIMIC-IV, social media, synthetic benchmarks including conservatism analysis. Week 9: Ablations (LLM quality sensitivity via |C|/K sweep, propensity overlap analysis, embedding dimension, calibration set size, cross-conformal vs. split comparison). Week 10: Paper writing and proof polishing.'}, 'human_in_loop': {'gpu_hours': '200-300', 'timeline': '8 weeks', 'claude_api_cost': '$100-150', 'estimated_gpu_cost': '$300-450 (A100 at ~$1.50/hr)', 'notes': 'AI assists with literature integration, boilerplate code, proof sketch verification. Human focuses on theoretical contributions (weighted exchangeability conditions, tight bounds for DR pseudo-outcomes, propensity propagation analysis) and experimental design. Requires ~5 hours domain expert time for confounder annotation guidelines.'}, 'auto_research': {'gpu_hours': '250-350', 'timeline': '5-6 weeks', 'claude_api_cost': '$250-350', 'estimated_gpu_cost': '$375-525 (A100 at ~$1.50/hr)', 'speed_bottleneck': 'Theoretical proof verification requires human mathematician; three-way split calibration across multiple seeds requires sequential experiment iterations; domain expert annotation for MIMIC-IV confounder labels cannot be automated'}}

## Inspired By
Gap: Existing conformal causal methods assume error-free confounders; existing LLM conformal methods ignore causal settings; existing text-based causal methods provide only asymptotic guarantees; Barnatchez et al. handle missing confounders but not noisy extraction; Vovk & Wang handle confounding in prediction but not treatment effects. Pattern: Three converging literatures (modular CP, conformal PPI, conformal causal inference) that have not been connected. Key enablers: Zhang et al. (arXiv 2510.04406) modular residual decomposition framework; Csillag et al. (arXiv 2510.16166) conformal set-predictor for PPI; Alaa et al. (NeurIPS 2023) conformal meta-learners for ITE; Barber et al. (Annals of Statistics 2023) weighted exchangeability beyond standard CP assumptions.

## Target Venues
- AAAI 2027 (Primary — abstract July 21, full paper July 28, 2026; ~10 weeks from today)
- ARR August 2026 cycle (Secondary — submission August 3, 2026) → EACL 2027 (commitment October 11, 2026)
- AISTATS 2027 (Stretch — estimated deadline ~October 2026, not yet announced)

## Key References
- Zhang et al. 'Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition' (arXiv 2510.04406, 2025)
- Csillag et al. 'Extending Prediction-Powered Inference through Conformal Prediction' (arXiv 2510.16166, 2025)
- Angelopoulos et al. 'Prediction-Powered Inference' (Science, 2023)
- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)
- Kato 'Semi-Supervised Treatment Effect Estimation with Unlabeled Covariates via Generalized Riesz Regression' (arXiv 2511.08303, NeurIPS 2025)
- Barber et al. 'Conformal prediction beyond exchangeability' (Annals of Statistics, 2023)
- Alaa et al. 'Conformal Meta-learners for Predictive Inference of Individual Treatment Effects' (NeurIPS 2023)
- Wang & Dobriban 'Optimal Decision-Making Based on Prediction Sets' (arXiv 2602.00989, 2026)
- Lützow et al. 'Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting' (arXiv 2605.12341, 2026)
- Xu et al. 'Conformal prediction for multi-dimensional time series by ellipsoidal sets' (ICML 2024)
- Campos et al. 'Conformal Prediction for Natural Language Processing: A Survey' (TACL, 2024)
- Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation (arXiv 2509.21660, 2025)
- Lei & Candès 'Conformal Inference of Counterfactuals and Individual Treatment Effects' (JRSS-B, 2021)
- DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)
- Ma et al. 'LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding' (NeurIPS 2025)
- Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)
- Veitch et al. 'Adapting Text Embeddings for Causal Inference' (UAI 2020)
- Barnatchez et al. 'Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding' (arXiv 2604.03772, 2026)
- Vovk & Wang 'Conformal e-prediction in the presence of confounding' (arXiv 2603.11134, 2026)
- Gasparin & Ramdas 'Improving the statistical efficiency of cross-conformal prediction' (arXiv 2503.01495, ICML 2025)
- Chernozhukov et al. 'Double/debiased machine learning for treatment and structural parameters' (Econometrics Journal, 2018)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2302adb6-ef46-4eca-a35a-3f8c90e30a2f",
  "type": "user",
  "uuid": "323f22b4-67bb-48f0-88a7-528548a3fcd6",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:30:42.848Z_

```json
{
  "parentUuid": "323f22b4-67bb-48f0-88a7-528548a3fcd6",
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
  "uuid": "765494fc-80cc-44b3-aab6-36533f21a14f",
  "timestamp": "2026-05-20T03:30:42.848Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:30:42.848Z_

```json
{
  "parentUuid": "765494fc-80cc-44b3-aab6-36533f21a14f",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "3cc538e8-f19e-4759-ad08-25a649384927",
  "timestamp": "2026-05-20T03:30:42.848Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T03:30:42.848Z_

```json
{
  "parentUuid": "3cc538e8-f19e-4759-ad08-25a649384927",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9aef8057-90b4-4f20-bc30-ecdc7a641ab9",
  "timestamp": "2026-05-20T03:30:42.848Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a thorough evalua…",
  "leafUuid": "9aef8057-90b4-4f20-bc30-ecdc7a641ab9",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize three reviewer assessments of causal inference proposal",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818"
}
```

---

### Assistant

_source line 9 · 2026-05-20T03:31:13.349Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as the Meta Judge.

First, let me extract the key information from each reviewer:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability (venue-agnostic, AAAI/AISTATS): [22% - 32%] 中位 27%
- CoRL: ≈0% (desk reject)
- Key risks: "Natural combination" concern, conservatism limiting practical utility
  
**Reviewer 2:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability (venue-agnostic): [20% - 35%] 中位 27%
- CoRL: [1% - 5%] 中位 2%
- Key risks: Venue mismatch (CoRL), trivial alternative threat (black-box CP), conservatism

**Reviewer 3:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium) — slightly lower than the other two reviewers
- Related Work: 强 (Strong)
- Probability: [22% - 33%] 中位 27%
- Key risks: "Natural extension" feel, conservatism vs. practical value trade-off

All three reviewers converged on a 27% acceptance probability with zero standard deviation, showing remarkable consensus. They unanimously rated novelty and related work as medium and strong respectively, though significance shows slight variation with Reviewer 3 being more conservative. The core concerns across all reviewers center on venue fit for CoRL, the risk of the work feeling like a natural combination rather than a breakthrough, and tension between methodological conservatism and practical utility.

Beyond these shared observations, individual reviewers flagged distinct technical threats: Reviewer 2 emphasized black-box end-to-end conformal prediction as a trivial alternative and cited Singer et al.'s recent work on measurement error in astronomy, Reviewer 1 pointed to Manski bounds as a simpler approach for one track, and Reviewer 3 raised concerns about conditional miscoverage when the model exhibits bias across subpopulations. Despite these divergent technical critiques, all three identified the paper's integrative nature and confirmed that the proposal does have identifiable value beyond trivial alternatives.

The three reviewers converged on a 27% probability estimate with zero standard deviation—remarkably tight agreement. Given this consensus, I should narrow the interval from the overlapping range of [22%-32%] down to something tighter around the median, like [24%-30%], to reflect the high confidence in this assessment.

For CoRL specifically, all three reviewers essentially agree it's not viable—ranging from 0% to a median of 2%—making it a clear desk reject. Since the question asks specifically about CoRL 2026 acceptance potential, I need to flag this clearly, but I should also present the venue-agnostic assessment since that's what the proposal is actually targeting. Let me structure the output to address both.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9aef8057-90b4-4f20-bc30-ecdc7a641ab9",
  "isSidechain": false,
  "requestId": "req_011CbD7ZPnb1xuUHpTo3vTnn",
  "type": "assistant",
  "uuid": "7e85804c-c22d-4558-8f5e-556262634cb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXhmMYLPfLLhFxzKJNBMby",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21973,
      "cache_read_input_tokens": 16166,
      "output_tokens": 3705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3705,
          "cache_read_input_tokens": 16166,
          "cache_creation_input_tokens": 21973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21973
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

_source line 10 · 2026-05-20T03:32:19.050Z_

【阶段】: Meta Judge
【三次中位】: [27%, 27%, 27%]  std=0%
【共识维度】: 
- **Venue Mismatch（致命）**: 3/3 审稿人一致判定本 proposal 与 CoRL 2026 scope 完全不匹配，几乎必定 desk reject。Proposal 自身目标会议为 AAAI 2027 / AISTATS 2027，不含 CoRL。信号极强。
- **Novelty = 中**: 3/3 一致。核心判断完全吻合——将 Zhang et al. (2510.04406) modular CP + Csillag et al. (2510.16166) conformal PPI 应用到因果设定，属于 integrative/combination novelty 而非 conceptual breakthrough。审稿人可能评价为 "natural next step"。
- **Related Work = 强**: 3/3 一致。对领域覆盖全面（直至 2026 年最新工作），引用经验证真实且描述准确，差异化定位（尤其 noisy extraction vs. missing confounders）清晰有力。
- **Conservatism 实用性风险（中）**: 3/3 一致指出 pilot analysis 显示 |C|=2 时 widening 60%、|C|=3 时 100%，可能使方法在实际中 "correct but not useful enough"。
- **"Natural extension" 拒稿风险（中）**: 3/3 一致认为最大拒稿风险是审稿人判定为 "technically sound but incremental"。
- **Gap 真实存在**: 3/3 确认 conformal CP × causal inference × LLM extraction 的三路交叉空白确实未被填补，定位准确。
- **Trivial alternatives 存在但有可辨识增量**: 3/3 认同 proposal 相对于简单替代方案（bootstrap、vanilla PPI）有 finite-sample guarantee 这一真实增量，但增量大小需实验验证。

【异常维度】: 
- **Significance 评级轻微分歧**: R1、R2 评"中偏强"，R3 评"中"。R3 更加悲观，认为核心 finding 的 surprise factor 低（"conformal 方法维持 coverage 但更保守"几乎是 by construction 的结论）。此分歧不影响最终概率（三人中位完全一致），但 R3 的观点有道理——降权 Significance 至"中"更保守、更安全。
- **Black-box end-to-end CP 替代方案**: R2 特别强调了 black-box CP（不做模块化分解，直接对整个 pipeline 做 conformal）作为威胁，要求实验证明模块化相比 black-box 的 tightness 优势超过 15-20%。R1/R3 未突出此点。但此观点合理——是一个实验设计层面的要求，不影响 idea 评估。
- **Conditional miscoverage**: 仅 R3 提到 LLM 抽取误差可能对特定 subpopulation 系统性偏差，marginal coverage 可能掩盖 conditional miscoverage。合理关切但属于已知的 conformal prediction 通用局限，非本 proposal 特有问题。
- **Bayesian 替代方案**: 仅 R3 提到贝叶斯 DML 作为 trivial alternative。未展开论证，降权处理。

【最终概率】: 
- **CoRL 2026**: [0% - 3%] 中位 1%（scope 致命不匹配，desk reject）
- **Venue-Agnostic（AAAI/AISTATS 级别）**: [22% - 31%] 中位 26%

【一致性】: 高（std=0%，三人中位完全一致，rubric 判决高度吻合）

【综合理由】: 

**CoRL 概率**：三位审稿人对 venue mismatch 的判断完全一致且逻辑无可辩驳——本文是纯粹的统计方法论/因果推断/NLP 工作，与机器人学习零关联。Proposal 自身也未将 CoRL 列为目标会议。取三人中最严格的估计（R1 的 ≈0%），给出 [0%-3%] 中位 1%。

**Venue-Agnostic 概率**：三人中位完全收敛于 27%，std=0%，属于"高一致"档位，应取中位附近并缩窄区间。但考虑到 R3 将 Significance 降为"中"（而非"中偏强"），且其理由有实质说服力（核心 finding 的 surprise factor 低），我将最终中位微调至 26%，区间从三人并集 [20%-35%] 收窄至 [22%-31%]。

**概率天花板分析**：Novelty=中 是 3/3 共识的硬约束。对于 combination/bridge paper，即使实验执行出色、Related Work 无懈可击，在 AAAI/AISTATS 级别会议的天花板约 35%。Significance 在"中"到"中偏强"之间，进一步将天花板压至 ~31%。Related Work=强 是主要的地板支撑——保证论文不会因文献覆盖不足被拒。

**概率地板分析**：实验设计（含 conservatism sweep、coverage 验证、多 benchmark）如果执行 solid，地板约 22%。但存在多个需要实验回答的关键问题（black-box CP 对比、bootstrap 到底 undercover 多少、真实临床数据上 |C| 的分布），任何一个回答不理想都可能拉低实际中稿概率。

【建议】: 边缘（venue-agnostic）/ KILL（CoRL 2026）

**对 CoRL 2026：明确 KILL**。Scope 完全不匹配，不应投稿，这不是 idea 质量问题而是 venue 选择错误。

**对 AAAI 2027 / AISTATS 2027：边缘**。中位 26% 处于"有机会但需要实验 execution 显著超预期"的区间。主要瓶颈是 Novelty（combination nature）和 Significance（核心 finding 的 predictability），这两个维度由 idea 立意决定，实验无法根本改变。建议维持原定投稿计划，但需做好 idea framing 的锐化工作，以及在实验中展示相对于 trivial alternatives 的显著优势。

【实施评估】:
- **计算资源**: 200-350 GPU hours (A100)，预估成本 $300-525。主要消耗在 LLM inference（Qwen3-Embedding-8B 的嵌入提取）、nuisance function 交叉拟合（TARNet/DragonNet）、多 seed 校准实验。计算需求适中，不构成瓶颈。
- **数据需求**: MIMIC-IV（公开可得，需 PhysioNet credentialed access）；社交媒体数据（需构建半合成 benchmark）；全合成数据（自行生成）。MIMIC-IV 的临床笔记文本质量和 confounder 标注需要领域专家参与（约 5 小时）。无需大规模新数据采集。
- **人工介入**: (1) 领域专家制定 confounder 标注指南（~5 小时）；(2) 理论证明（weighted exchangeability 下 modular decomposition 的严格推导）需要有数理统计背景的研究者，**这是最大的人工瓶颈**——如果证明是 non-trivial 的，可能占用 2-3 周；(3) 论文写作和证明 polish。
- **训练需求**: 不需要从头训练大模型。需要 fine-tune LLM 抽取模型（或 prompt engineering）+ 训练 nuisance functions（propensity score、outcome regression），均为中等规模训练任务。Qwen3-Embedding-8B 用于 inference 无需训练。
- **新 Benchmark**: 需构建 2 个半合成 benchmark（MIMIC-IV based、social media based）和 1 个全合成 benchmark。半合成 benchmark 需要在真实文本上叠加已知的因果结构，工作量中等（约 1-2 周）。
- **预估周期**: 8-10 周（与 proposal 自述一致）。关键路径：理论证明（2-3 周）→ 实现 pipeline（2 周）→ 实验（2-3 周）→ 写作（1-2 周）。AAAI 2027 deadline（July 28, 2026）距今约 10 周，时间紧但可行。理论证明的难度是最大不确定因素——如果 weighted exchangeability 证明遇到根本性困难，整个时间线将被推迟。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e85804c-c22d-4558-8f5e-556262634cb5",
  "isSidechain": false,
  "requestId": "req_011CbD7ZPnb1xuUHpTo3vTnn",
  "type": "assistant",
  "uuid": "08740e19-0cf9-46ad-b516-cccc4effa972",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXhmMYLPfLLhFxzKJNBMby",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21973,
      "cache_read_input_tokens": 16166,
      "output_tokens": 3705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3705,
          "cache_read_input_tokens": 16166,
          "cache_creation_input_tokens": 21973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21973
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a thorough evalua…",
  "leafUuid": "08740e19-0cf9-46ad-b516-cccc4effa972",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize three reviewer assessments of causal inference proposal",
  "sessionId": "b65d38de-e0ab-4717-bbf3-128111222818"
}
```

---
