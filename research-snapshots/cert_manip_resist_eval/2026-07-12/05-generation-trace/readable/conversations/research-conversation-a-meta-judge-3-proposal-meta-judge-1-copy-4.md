# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/98160e49-8e4d-448d-8928-ded4e23f03a3.jsonl`
- **Structured JSON:** [`951a82cbc81d2a8df2c0.json`](../../sessions/95/951a82cbc81d2a8df2c0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:31:15.596Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:31:15.596Z",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient context from the field research. Let me compile the full evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- Zhang et al. \"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition\" (arXiv 2510.04406, 2025): Track A 的直接理论基础。提出两阶段序贯模型的残差分解框架，用于供应链和股票市场预测，但未涉及因果推断设置。本 proposal 的 Track A 将其扩展到 DR 估计器是合理的延伸。\n- Csillag et al. \"Extending Prediction-Powered Inference through Conformal Prediction\" (arXiv 2510.16166, 2025): Track B 的直接理论基础。将 conformal set-predictor 引入 PPI 框架，实现 Z-estimation 和 M-estimation 的有效推断。本 proposal 将其应用于 ATE 因果推断是新的应用方向。\n- Kluger et al. \"PPI with Imputed Covariates and Nonuniform Sampling\" (arXiv 2501.18577, 2025): 最直接的竞争工作。使用 Predict-Then-Debias Bootstrap 处理 imputed covariates，提供渐近有效的 CI。proposal 明确将其列为 head-to-head baseline，声称在 heterogeneous noise 和小样本下 conformal 方法更优——这一 claim 需要实验验证。\n- Mani et al. \"No Free Lunch: Non-Asymptotic Analysis of PPI\" (arXiv 2505.20178, 2025): 证明 PPI++ 在 pseudo-label 相关性低时可能劣于仅使用 gold-standard。Proposal 对此有明确回应（conformal set-predictor 产生更宽区间而非无效区间），positioning 合理。\n- DoubleLingo (NAACL 2024): 使用 LLM 作为 nuisance model 进行 Double ML 因果估计，但仅提供渐近保证。是 proposal 的重要 baseline。\n- Ma et al. \"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding\" (NeurIPS 2025): 处理推断时文本混杂，使用自定义 DR learner，同样仅渐近保证。\n- Lei & Candès (JRSS-B 2021); Alaa et al. (NeurIPS 2023); wTCP-DR (KDD 2024): Conformal ITE 方法，均假设无误差混杂变量。Proposal 的 gap 声称成立。\n- Campos et al. \"Conformal Prediction for NLP: A Survey\" (TACL 2024): 覆盖分类/QA/生成，不涉及因果有效性，证实该交叉领域存在空白。\n- Barnatchez et al. (arXiv 2604.03772, 2026); Vovk & Wang (arXiv 2603.11134, 2026): 最新的 conformal + causal 工作，但分别处理 missing confounders 和 conformal e-prediction，与本 proposal 的 noisy-extraction 设定不同。\n- 调研总结: Conformal prediction × causal inference × LLM text extraction 的三重交叉确实是一个未被填补的 gap。现有工作要么假设无误差混杂（conformal causal），要么仅提供渐近保证（LLM causal），要么处理不同设定（missing confounders）。Proposal 的定位在文献中是准确的，novelty claim 基本成立。但这个交叉非常 niche，目标受众较窄。\n\n【整体印象】: \n作为审稿人，第一反应是\"这是一份技术上极其详尽的 proposal，作者显然深度掌握了三个交叉领域的文献\"。proposal 识别了一个真实存在的 gap（conformal + causal + noisy LLM extraction），理论动机清晰（IPW amplification 的 finite-sample 刻画），实验设计堪称 exhaustive。然而，几个关键顾虑会让我犹豫：(1) 核心方法论本质上是将已有框架（Zhang et al. 的 modular CP + Csillag et al. 的 conformal PPI + 标准 DR 估计器）组合应用到一个新设定，而非提出根本性的新方法；(2) pilot analysis 显示方法实际有用的窗口很窄（|C|≤2 for K=5），这削弱了实践价值；(3) 论文密度极高，同时包含 Track A、Track B、exploratory embedding track、6 层 baseline、多维 ablation，存在\"什么都做但什么都不深\"的风险。倾向 borderline，偏向 weak accept/reject 之间。\n\n【核心贡献】: \n核心贡献有三层：(1) 理论层——首次在 distribution-free、finite-sample 框架下刻画了 IPW amplification 如何放大 conformal set 中的提取不确定性，给出了区间宽度的 worst-case bound W；(2) 方法层——将 modular conformal prediction 和 conformal PPI 统一为一个两阶段因果推断框架（Track A for ITE, Track B for ATE）；(3) 实践层——principled abstention 机制，当 LLM 提取质量不足时自动检测并报告。\n价值评估：理论贡献是最有价值的部分，因为 IPW amplification 的 finite-sample conformal 刻画确实是新的。但方法贡献更多是已有工具的组合，实践贡献（abstention）虽然有用但技术含量有限。整体而言，对领域的贡献是 incremental-to-moderate：它填补了一个真实的 gap，但不太可能改变这个方向的研究范式。\n\n【方法合理性】: \n方法在技术上是合理的：\n- Stage 1 使用 APS 对 LLM 提取的 categorical confounders 构建 conformal prediction sets 是标准做法\n- Stage 2 通过 worst-case pseudo-outcome enumeration 传播不确定性，利用 DR 估计器的结构是合理的\n- 两个 track 分别处理 ITE 和 ATE 是合理的分工\n\n**更简单的替代方案问题**：这是主要风险点。一个审稿人可能会问：\n(a) 如果 LLM 提取质量足够高（|C|≤2），直接用 point prediction + bootstrap CI（如 DoubleLingo）是否已经足够好？pilot analysis 显示只有在这个窗口内方法才实用，但在这个窗口内 naive 方法可能也表现不错。\n(b) 为什么不直接用 calibrated LLM probabilities 做 soft imputation，而要走 conformal set 这条更复杂的路？这需要强有力的实验证据来回答。\n(c) Propensity trimming（τ=0.05）已经是标准做法来控制 IPW amplification，conformal propagation 的额外价值需要清晰展示。\n\nproposal 承认了 honest framing（大样本 + 均匀噪声下渐近方法表现相当），这是加分项，但也意味着方法的优势区间可能较窄。\n\n【5 维度打分】:\n  1. 研究问题: [强] — 因果推断 + LLM 提取 + finite-sample 保证的交叉是一个真实、重要、有时效性的问题。随着 LLM 在文本数据因果分析中的应用增加（DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），对提取不确定性的严格处理有明确需求。Barnatchez et al. (2026) 和 Vovk & Wang (2026) 的最新工作进一步确认了 conformal + causal 方向的热度。研究问题的价值不依赖于特定方法的选择。\n  \n  2. 方法与创新: [中] — Novelty 主要在于将 Zhang et al. (2510.04406) 的 modular CP 和 Csillag et al. (2510.16166) 的 conformal PPI 组合应用到因果推断设定，并加入 IPW amplification 的 finite-sample 刻画。IPW amplification 本身是 well-known phenomenon（Babanezhad et al. 2010），novelty 在于 conformal 框架下的刻画，这是增量式创新而非突破式创新。与 Kluger et al. (2501.18577) 的差异化（distribution-free vs. asymptotic）是清晰的，但实际优势需要实验验证。exploratory embedding track 增加了方法的广度但降低了深度。\n  \n  3. 实验设计: [强] — 这是 proposal 最突出的亮点。6 层 baseline 设计（Oracle → Naive → SIMEX → Asymptotic → PTD Bootstrap → Proposed）层次分明，覆盖了所有合理的对比方法。三类 benchmark（MIMIC-IV 半合成、社交媒体半合成、全合成 3 场景）覆盖了不同数据特征。ablation 设计系统性强（nonconformity score、trimming threshold、cross-conformal vs. split、|C|/K sweep、n_labeled sensitivity）。评估指标全面（coverage + width + conditional coverage + calibration plot）。Honest framing（大样本优势消失）是加分项。唯一不足：缺少真实因果效应的 ground-truth 数据集（所有都是半合成或全合成），但这在因果推断领域是普遍限制。\n  \n  4. 可行性: [中] — 资源估计合理（200-300 GPU hours, 10 weeks, ~$450）。但执行风险较高：(a) 同时推进 Track A + Track B + exploratory embedding track + 6 层 baseline + 3 类 benchmark + 多维 ablation，工作量巨大；(b) MIMIC-IV 需要 PhysioNet credentialing，存在时间风险（proposal 提到了 MIMIC-III backup）；(c) exploratory embedding track 明确需要 feasibility pilot，可能不可行；(d) 理论证明（modular decomposition under weighted exchangeability）的难度可能被低估。10 周时间线非常紧张。\n  \n  5. 写作与呈现: [中] — 作为 proposal，逻辑结构清晰，文献定位精准，differentiation 细致。但信息密度极高——同时覆盖理论贡献、两个主要 track、一个探索 track、多个 benchmark、大量 ablation。在 8 页正文的限制下，如何有效组织这些内容是重大挑战。存在\"什么都想展示，结果哪个都讲不透\"的风险。建议明确主次：Track A 为主、Track B 为辅、embedding track 放 appendix。\n\n【概率估计】: [22% - 38%] 中位 30%\n\n【估计理由】: \n研究问题真实且有时效性（强），实验设计非常完备（强），这两个维度显著拉高了中稿概率。但方法创新度为增量式组合（中），实际有用的窗口较窄（|C|≤2），且论文的 scope 过于庞大，在 8 页篇幅内难以充分展开。EMNLP 审稿人背景偏 NLP，对 conformal prediction 和因果推断的 heavy theory 可能缺乏足够专业知识来充分评估，审稿人匹配是额外的不确定性因素。与 Kluger et al. (PTD Bootstrap) 的实际性能差距（即 conformal 方法在 heterogeneous noise 下的优势幅度）是决定性的实验问题——如果优势不显著，novelty claim 会被大幅削弱。30% 反映\"方向正确、执行可期但创新度和实用性存在审稿人合理质疑\"的判断。上界 38% 对应\"实验结果清晰展示了 conformal 方法在目标场景下的优势\"的乐观情景；下界 22% 对应\"审稿人认为是已有方法的简单组合 + 实用窗口太窄\"的悲观情景。\n\n【主要风险】: \n1. **\"组合 vs. 创新\"质疑**：审稿人可能认为核心方法是 Zhang et al. modular CP + Csillag et al. conformal PPI + 标准 DR 的直接拼接，IPW amplification 的 finite-sample 刻画虽然新但属于 incremental contribution，insufficiently novel for a top venue。\n2. **实用性窗口过窄**：pilot analysis 自己揭示了 |C|≤2（K=5 时）才实用的限制。审稿人会追问：在 LLM 提取质量好到 |C|≤2 的场景下，更简单的 baseline（naive plug-in + bootstrap）是否已经足够好？如果答案是\"差距不大\"，整个方法的 practical motivation 会被动摇。\n\n【实施评估】:\n  - 计算资源: 200-300 A100 GPU hours (~$300-450)，合理\n  - 数据需求: MIMIC-IV-Note（需 PhysioNet credentialing）+ 社交媒体文本 + 合成数据；需要 ~200 条人工标注用于 calibration 验证\n  - 人工介入: ~20h annotation（标注指南验证 + spot check），使用 MIMIC 结构化字段作为 proxy ground truth\n  - 训练需求: 需要训练/微调 propensity score 模型和 outcome 模型（nuisance estimators），但计算量不大；LLM 推断（GPT-4/Claude/Llama extraction）是主要成本\n  - 新 Benchmark: 3 类半合成/全合成 benchmark（MIMIC-IV, 社交媒体, 全合成），非全新 benchmark 但需要构建 DGP pipeline\n  - 预估周期: 10 周（紧张但可能，如果 exploratory track 可以放松为 future work）\n```\n\nSources:\n- [Modular and Adaptive Conformal Prediction for Sequential Models](https://arxiv.org/abs/2510.04406)\n- [Extending Prediction-Powered Inference through Conformal Prediction](https://arxiv.org/abs/2510.16166)\n- [Prediction-Powered Inference with Imputed Covariates](https://arxiv.org/abs/2501.18577)\n- [No Free Lunch: Non-Asymptotic Analysis of PPI](https://arxiv.org/abs/2505.20178)\n- [DoubleLingo: Causal Estimation with Large Language Models](https://aclanthology.org/2024.naacl-short.71/)\n- [LLM-Driven Treatment Effect Estimation Under Text Confounding](https://arxiv.org/pdf/2507.02843)\n- [Conformal Prediction for NLP: A Survey (TACL 2024)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/)\n- [Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)](https://dl.acm.org/doi/10.1145/3637528.3671976)\n- [A Systematic Review of Conformal Inference for Treatment Effects](https://www.arxiv.org/pdf/2509.21660)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct the evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- Zhang et al. \"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition\" (arXiv 2510.04406, Oct 2025): Track A 的直接理论基础。该工作提出了两阶段顺序模型的残差分解 CP 框架，但未涉及因果估计或加权可交换性。本 proposal 将其扩展到因果 DR 估计器是自然但非平凡的延伸。\n- Csillag et al. \"Extending Prediction-Powered Inference through Conformal Prediction\" (arXiv 2510.16166, Oct 2025): Track B 的直接理论基础。将 PPI 与 conformal set-predictor 结合，提供 Z-/M-estimation 下的有效推断。本 proposal 将其扩展到 ATE 估计是合理的增量。\n- Kluger et al. \"PPI with Imputed Covariates and Nonuniform Sampling\" (arXiv 2501.18577, Jan 2025): 最直接的竞争者。使用 PTD Bootstrap 处理 imputed covariates，提供渐近有效的 bootstrap CI。本 proposal 的核心差异化在于有限样本分布无关保证 vs. 渐近保证。\n- Mani et al. \"No Free Lunch: Non-Asymptotic Analysis of PPI\" (arXiv 2505.20178, May 2025): 证明 PPI++ 在 pseudo-label 相关性低时可能劣于仅用 gold-standard。本 proposal 正确识别了这一风险，并论证 conformal set-predictor 在质量差时会变宽而非失效。\n- DoubleLingo (NAACL 2024): 将 LLM 嵌入 DR 因果估计器中处理文本混杂变量，但仅提供渐近保证。本 proposal 补充了有限样本 UQ 层。\n- Ma et al. \"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding\" (NeurIPS 2025): 处理推断时文本混杂问题（训练时完整观测、推断时仅有文本），与本 proposal 的 noisy extraction setting 不同但高度相关。同样仅渐近保证。\n- Barnatchez et al. (arXiv 2604.03772, Apr 2026): 处理部署时混杂变量完全缺失的场景（runtime confounding），用半参数去偏。与本 proposal 的 noisy extraction 场景明确区分。\n- Alaa et al. \"Conformal Meta-learners for Predictive Inference of ITE\" (NeurIPS 2023): 假设混杂变量无误差的 conformal ITE 方法。本 proposal 放松了这一假设。\n- Systematic Review of Conformal Inference for Treatment Effects (arXiv 2509.21660, 2025): 综述确认该领域活跃但尚无工作同时处理 ML-extracted confounders + finite-sample guarantees。\n- 调研总结: conformal prediction × causal inference 是2025-2026年的活跃研究前沿，但现有工作要么假设无误差混杂变量（Alaa et al.），要么仅提供渐近保证（DoubleLingo, Ma et al.），要么不使用 conformal sets（Kluger et al.）。本 proposal 填补了一个真实的空白：将 conformal uncertainty 从 ML extraction 阶段传播到因果估计阶段的分布无关有限样本框架。\n\n【整体印象】:\n作为审稿人，我的第一反应是：这是一篇技术上非常 solid、问题定义清晰、实验设计极其充分的 proposal。它填补了 conformal prediction + causal inference + LLM extraction 三个领域交叉处的一个真实空白。但核心贡献本质上是**组合性**的——将已有的 modular CP (Zhang et al.) 和 conformal PPI (Csillag et al.) 适配到因果设定中，关键的 IPW amplification analysis 虽然是新的形式化但基于已知现象。我会倾向于 **weak accept / borderline**，最终取决于理论贡献的深度和实验结果的说服力。\n\n【核心贡献】:\n1. **理论贡献**: 首个在 conformal set 框架下对 IPW amplification 的分布无关有限样本刻画（W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle）\n2. **方法贡献**: 两条互补的 track——Track A (modular conformal ITE intervals) 和 Track B (conformal PPI ATE intervals)——为不同场景提供适用方案\n3. **实践贡献**: principled abstention 机制（当 |C|/K ≥ 0.6 时自动检测 LLM extraction 质量不足）\n\n这些贡献对领域的价值是**中等偏上**的。问题重要且及时（LLM 提取文本混杂变量越来越常见），但方法的核心是已有技术的组合与适配，而非根本性创新。IPW amplification 的 conformal 形式化有一定理论新意，但其实际影响取决于证明的紧致性。\n\n【方法合理性】:\n方法整体合理，逻辑链清晰：LLM extraction → conformal calibration (Stage 1) → uncertainty propagation through DR estimator (Stage 2)。关键设计选择（APS 作为 nonconformity score、propensity trimming、worst-case pseudo-outcome enumeration）都有充分的文献支撑。\n\n**潜在替代方案的威胁**:\n- Kluger et al. 的 PTD Bootstrap 是最直接的竞争者。本 proposal 的优势（有限样本保证 vs. 渐近保证）在小样本 + 异质噪声场景下最为显著，但在大样本场景下渐近方法可能表现相当——proposal 自身也承认了这一点（honest framing）。\n- 一个更简单的替代方案是：直接用 LLM softmax probabilities 进行加权 DR 估计（不经 conformal calibration），这可能在某些场景下效果相当。Proposal 需要在实验中明确展示 conformal calibration 相对于 naive softmax weighting 的增益。\n\n**理论风险**: proposal 中有一个\"conjecture\"（worst-case pseudo-outcomes 出现在 propensity-extreme confounder values），这需要严格证明或充分的经验验证。如果这一 conjecture 不成立，selective enumeration 的效率优势不保。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】— 问题重要且定义清晰。LLM 提取文本混杂变量的不确定性传播缺乏有限样本保证，这是一个被 systematic review (arXiv 2509.21660) 确认的真实空白。与 classical measurement error 的区分论证有力（categorical, context-dependent, heterogeneous noise vs. additive Gaussian noise）。\n\n2. 方法与创新: 【中】— 核心方法是已有技术的组合适配：Track A 适配 Zhang et al. (2025)，Track B 扩展 Csillag et al. (2025)。IPW amplification 的 conformal 形式化是新的（对比 Babanezhad et al. 2010、Yi & Chen 2023 的渐近/参数化分析），但本质上是已知现象的新 wrapper。与 Kluger et al. (2025) 的差异化（finite-sample vs. asymptotic）清晰但增量性明显。Principled abstention 机制虽有实用价值但技术上并不深刻（conformal set 大 → interval 宽是 conformal prediction 的自然性质）。\n\n3. 实验设计: 【强】— 这是 proposal 最突出的优势。六层 baseline（从 oracle 到 proposed method）层次分明；三类 benchmark 覆盖不同场景；评估指标全面（coverage with Clopper-Pearson CI、conditional coverage stratification、calibration plots）；ablation 设计系统化（nonconformity score、propensity trimming、cross-conformal、n_labeled sensitivity）。Honest framing（承认大样本 + 均匀噪声下渐近方法可能表现相当）大幅提升可信度。直接包含 Kluger et al. PTD Bootstrap 和 SIMEX 作为 head-to-head baseline 也是加分项。\n\n4. 可行性: 【中偏强】— GPU 需求（200-300 A100 hours）和预算（~$450）非常可控。10 周时间线对 core Track A+B 可行，但包含 embedding exploratory track + 所有 ablation 可能偏紧。主要风险：(a) PhysioNet credentialing 可能延迟 MIMIC 数据获取；(b) 理论证明（尤其是 conjecture 的严格化）可能比预期耗时；(c) 范围过于宽泛（两个 track + exploratory track + 大量 ablation），需要严格优先级管理。\n\n5. 写作与呈现: 【强】— Proposal 逻辑清晰、结构完整。问题动机→现有工作不足→方法→实验的论证链条流畅。与相关工作的差异化（五个方向逐一对比）非常到位。数学形式化具体（给出了 DR pseudo-outcome 公式、widening ratio W 的表达式、pilot conservatism analysis table）。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n向上推动因素：(1) 问题重要且时机好——conformal + causal 是2025-2026热点但尚无工作处理 LLM extraction uncertainty；(2) 实验设计极其充分，远超多数 proposal 的水平；(3) honest framing 和 thorough differentiation 提升可信度；(4) 资源需求合理，核心实验可执行。\n向下拉动因素：(1) 核心创新是组合性的——审稿人可能认为这是 Zhang et al. + Csillag et al. 的\"trivial\" adaptation，尤其如果 IPW amplification analysis 的证明深度不足；(2) 理论中存在未证明的 conjecture；(3) 范围过广（两个 track + embedding track），可能给人\"散而不精\"的印象；(4) 对于 EMNLP 评审池而言，conformal prediction 理论的审稿专业度参差不齐，可能导致评分方差大。中位 35% 反映了这是一篇扎实但未必突出的投稿——在\"solid work\"和\"borderline\"之间。\n\n【主要风险】:\n1. **Novelty 被质疑为组合性增量**: 最可能的拒稿理由。审稿人可能认为\"将 modular CP 应用于因果估计 + 将 conformal PPI 扩展到 ATE\"是已有方法的直接扩展，IPW amplification analysis 的新意不足以支撑一篇顶会论文。需要在理论深度（tight bounds, 非 trivial proofs）或实验中展示 surprising findings 来对冲此风险。\n2. **理论贡献与实验贡献的平衡问题**: 如果理论证明不够紧致（尤其是 conjecture 未能严格证明），论文会被当作\"实验 paper\"评审；但如果实验不够充分（虽然 proposal 设计很好，执行中可能缩水），又会被当作\"不完整的理论 paper\"。两头都需要做实。\n\n【实施评估】:\n  - 计算资源: 200-300 A100 GPU hours (~$300-450)，非常可控，无瓶颈\n  - 数据需求: MIMIC-IV-Note (需 PhysioNet credentialing，有 MIMIC-III 备选)；社交媒体数据 (Veitch et al. UAI 2020 范式，公开可用)；全合成数据 (无障碍)\n  - 人工介入: ~20h 用于标注指南验证和抽样检查（使用 MIMIC 结构化字段作为 proxy ground truth），工作量极小\n  - 训练需求: 无大规模模型训练。需要 fine-tune/prompt LLM 进行 confounder extraction，训练 DR 估计器的 nuisance models（propensity score + outcome models），但这些都是轻量级的\n  - 新 Benchmark: 需要构建 semi-synthetic benchmark（MIMIC + social media），但有明确的 DGP 设计，不需要大规模标注\n  - 预估周期: 10 周（理论 3 周 + 实现 3 周 + 实验 3 周 + 写作 1 周）。核心 Track A+B 可行；embedding exploratory track 可能被降级为 future work。PhysioNet credentialing 是时间线上的最大风险。\n```\n\nSources:\n- [Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition](https://arxiv.org/abs/2510.04406)\n- [Extending Prediction-Powered Inference through Conformal Prediction](https://arxiv.org/abs/2510.16166)\n- [PPI with Imputed Covariates and Nonuniform Sampling](https://arxiv.org/abs/2501.18577)\n- [No Free Lunch: Non-Asymptotic Analysis of Prediction-Powered Inference](https://arxiv.org/abs/2505.20178)\n- [DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)](https://aclanthology.org/2024.naacl-short.71/)\n- [LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding (NeurIPS 2025)](https://arxiv.org/abs/2507.02843)\n- [Debiased Machine Learning for Conformal Prediction Under Runtime Confounding](https://arxiv.org/abs/2604.03772)\n- [A Systematic Review of Conformal Inference for Treatment Effect Estimation](https://arxiv.org/abs/2509.21660)\n- [Conformal Meta-learners for Predictive Inference of ITE (NeurIPS 2023)](https://arxiv.org/abs/2202.04012)\n- [Conformal Prediction for Natural Language Processing: A Survey (TACL 2024)](https://arxiv.org/abs/2405.01976)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nBased on my research, I now have sufficient information to provide a comprehensive evaluation. Let me compile my assessment.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- Zhang et al. \"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition\" (arXiv 2510.04406, 2025): 核心建筑块之一。处理两阶段流水线中的模块化不确定性分解，但未涉及因果设定或加权可交换性。Proposal 正确识别了从该工作到因果设定的 gap。\n- Csillag et al. \"Extending Prediction-Powered Inference through Conformal Prediction\" (arXiv 2510.16166, 2025): 另一核心建筑块。将 PPI 与 conformal prediction 连接，但未处理因果估计器中的倾向得分放大效应。Proposal 的 Track B 直接建立在此基础上。\n- Kluger et al. \"Prediction-Powered Inference with Imputed Covariates and Nonuniform Sampling\" (arXiv 2501.18577, 2025): 最直接的竞争者。使用 Predict-Then-Debias Bootstrap 处理 imputed covariates，但提供渐近保证而非有限样本保证。Proposal 正确地将其纳入 baseline。\n- Mani et al. \"No Free Lunch: Non-Asymptotic Analysis of PPI\" (arXiv 2505.20178, 2025): 证明 PPI++ 在低伪标签相关性时可能劣于纯 gold-standard。Proposal 恰当地讨论了这一限制，并将其转化为 conformal set-predictor 的优势论证。\n- DoubleLingo (NAACL 2024): 在 DR 因果估计器中使用 LLM，但仅提供渐近保证。Proposal 正确识别了 finite-sample UQ 的 gap。\n- Ma et al. \"LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding\" (NeurIPS 2025): 处理文本混淆因子的最新工作，同样仅提供渐近保证。\n- Systematic Review of Conformal Inference for Treatment Effect Estimation (arXiv 2509.21660, 2025): 确认该领域活跃但现有方法均假设无误差的混淆因子。\n- 调研总结: Proposal 处于三个活跃研究方向（模块化 CP、conformal PPI、因果推断 + LLM）的交汇点。其核心 novelty claim——\"首个在 conformal set 框架下对 IPW 放大效应的无分布有限样本刻画\"——在现有文献中确实未被占据。最直接竞争者（Kluger et al.）提供渐近保证，而非有限样本保证。\n\n【整体印象】: 作为审稿人，我的第一反应是这是一篇 technically ambitious、问题定义清晰的 proposal，有真实的理论贡献。然而，我会有三个主要顾虑：(1) 论文试图在一篇工作中呈现 Track A + Track B + 探索性 embedding track，scope 过大；(2) Pilot analysis 显示实际有用的区间仅在 |C| ≤ 2 时成立（K=5），这意味着方法的实用场景相当受限；(3) 核心理论贡献（amplification characterization）目前是\"conjecture and empirically test\"状态，如果无法严格证明，论文主贡献将大打折扣。总体倾向：borderline，偏 weak accept 但需要执行质量非常高。\n\n【核心贡献】: (1) 首个将 conformal prediction set 不确定性传播到因果估计器（特别是 DR 估计器的 IPW 组件）的理论框架，提供有限样本覆盖保证；(2) 对倾向得分放大效应的无分布刻画 W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle；(3) 原则性弃权机制作为 LLM 可靠性内置评估。对领域的价值中等偏上——解决了一个真实存在的理论 gap，但实际应用场景受限。\n\n【方法合理性】: 方法在理论上合理——利用 conformal prediction 的分布自由特性来规避经典测量误差校正的参数假设，通过穷举 conformal set 中的最坏情况来获得有效区间。这是一个自然的思路。但存在两个替代方案的挑战：(1) 对于 ATE 估计（Track B），Kluger et al. 的 PTD Bootstrap 在大样本下可能表现类似且计算更简单；(2) 一个更简单的替代方案是直接使用多个 LLM 提取的 ensemble（而非 conformal set），通过对不同提取结果的分散度来量化不确定性。Proposal 需要在实验中清楚展示 conformal 方法何时（以及为何）优于这些更简单的替代品。\n\n【5 维度打分】:\n  1. 研究问题: [强] — 问题真实存在且重要。LLM 从文本中提取混淆因子用于因果推断是一个增长中的实践场景（DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），但现有方法缺乏有限样本保证。这个 gap 被 systematic review (arXiv 2509.21660) 和 No Free Lunch 结果间接证实。\n  \n  2. 方法与创新: [中] — 创新性真实但有限。核心思路是将两个已有框架（Zhang et al. 2025 的模块化 CP + Csillag et al. 2025 的 conformal PPI）应用到因果设定中。IPW 放大效应的有限样本刻画是新的，但本质上是已知渐近现象（Babanezhad et al. 2010）的 conformal 版本。与 Kluger et al. (2025) 的差异化——有限样本 vs 渐近——在实践中差距可能不大（大样本时两者趋同）。\n  \n  3. 实验设计: [强] — 实验设计非常完备。6 层 baseline（Oracle → Naive → SIMEX → Asymptotic → PTD Bootstrap → Proposed）覆盖了所有合理替代方案。三类 benchmark（MIMIC-IV 半合成 + 社交媒体 + 全合成）提供多样化验证。Ablation 设计全面（非conformity score、propensity trimming、cross-conformal vs split、|C|/K sweep）。Honest framing（承认大样本 + 均匀噪声时渐近方法可能媲美）增强可信度。这在同类 proposal 中是 top-tier 的实验规划。\n  \n  4. 可行性: [中] — 10 周时间线紧张但不是不可能。200-300 GPU hours 合理。主要风险：(a) MIMIC-IV 需要 PhysioNet 认证（有 MIMIC-III backup）；(b) 理论证明可能比预期更难（\"conjecture and empirically test\"表明尚未完成严格证明）；(c) 探索性 embedding track 可能需要砍掉以集中资源；(d) 如果 conformal set 在实际数据上普遍 |C| ≥ 3，方法可能无法展示实用性。\n  \n  5. 写作与呈现: [中] — Proposal 本身逻辑清晰、文献综述全面、differentiation 精确。但论文写作的挑战在于：两个 track + 探索性 track 的复杂结构需要极其清晰的表达来让审稿人理解。存在\"信息过载\"风险——审稿人可能觉得论文试图做太多事情而每件都不够深入。\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】: \n- 加分项：真实的理论 gap、极其完备的实验设计、timely topic（conformal + causal + LLM 三线交汇）、对局限性的诚实讨论、完善的 baseline 覆盖\n- 减分项：(1) Scope 过大——两个完整 track + 探索性 track 在一篇论文中很难充分展开；(2) 实用性受限——仅在 |C| ≤ 2 时有用，这意味着 LLM 提取质量必须已经很高，限制了方法的适用场景；(3) 核心理论贡献尚未严格证明（\"conjecture\"状态）；(4) 有限样本优势主要在 n < 1000 时显现，这恰恰是 conformal calibration 数据最不充裕的区间，存在 tension；(5) EMNLP 审稿人可能对重统计理论的论文接受度较低（核心贡献更适合 AISTATS/JMLR）\n\n【主要风险】: \n1. **实用性窄**：Pilot analysis 表明方法仅在 LLM 已经足够好（|C| ≤ 2/5）时才产生有意义的区间。审稿人可能质问：\"如果 LLM 提取已经这么准确，为什么还需要这个复杂框架？直接用 point estimate 的误差有多大？\"\n2. **理论执行风险**：核心 amplification characterization 目前是 conjecture 状态。如果无法在提交前严格证明（或证明过程中发现需要额外强假设），论文的核心贡献将从\"理论+实证\"降级为\"纯实证\"，显著降低竞争力。\n\n【实施评估】:\n  - 计算资源: 200-300 GPU hours (A100)，约 $300-450，合理且可负担\n  - 数据需求: MIMIC-IV-Note（需 PhysioNet 认证，有 MIMIC-III backup）+ Veitch et al. 社交媒体数据（公开）+ 全合成数据\n  - 人工介入: ~20h 标注验证（利用 MIMIC 结构化字段作为 proxy），轻量级\n  - 训练需求: 无需训练大模型；需要训练/微调 nuisance estimators（propensity score, outcome models），计算量不大\n  - 新 Benchmark: 需要构建 semi-synthetic benchmark（MIMIC-IV 上的因果 DGP），但基于已有数据和范式（Veitch et al. 2020），非从零开始\n  - 预估周期: 10 周（紧张但可行，前提是理论部分能按时完成）\n```\n\nSources:\n- [Modular and Adaptive Conformal Prediction for Sequential Models](https://arxiv.org/abs/2510.04406)\n- [Extending Prediction-Powered Inference through Conformal Prediction](https://arxiv.org/abs/2510.16166)\n- [Prediction-Powered Inference with Imputed Covariates and Nonuniform Sampling](https://arxiv.org/abs/2501.18577)\n- [No Free Lunch: Non-Asymptotic Analysis of PPI](https://arxiv.org/abs/2505.20178)\n- [DoubleLingo: Causal Estimation with Large Language Models](https://aclanthology.org/2024.naacl-short.71/)\n- [A Systematic Review of Conformal Inference for Treatment Effect Estimation](https://arxiv.org/html/2509.21660)\n- [Conformal Prediction for Causal Effects of Continuous Treatments](https://arxiv.org/abs/2407.03094)\n- [Prediction-Powered Inference (Science 2023)](https://www.science.org/doi/10.1126/science.adi6000)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Conformal Uncertainty Propagation for Causal Inference with LLM-Extracted Text Confounders\n\n## Description\n\nWe propose a framework — ConformalPPITextCausal — for valid causal inference when text confounders are extracted by a fallible LLM. The core intellectual contribution is a general theory of **conformal uncertainty propagation through causal estimators**: how Stage 1 conformal prediction sets over ML-extracted variables interact with Stage 2 causal effect estimation, and how to exploit this interaction structure for provably tight finite-sample bounds.\n\nThe key structural insight is that in doubly robust (DR) estimators, extraction uncertainty propagates asymmetrically through the propensity score component via inverse probability weighting: a confounder value with ê(c)=0.25 amplifies outcome residuals 4×, while ê(c)=0.50 amplifies only 2×. The phenomenon of IPW amplifying measurement error is well-documented in the causal inference literature (Babanezhad et al. 2010; Yi & Chen 2023; Shu 2019), but existing analyses are asymptotic and assume parametric error models. We provide the **first distribution-free, finite-sample characterization** of this amplification within a conformal set framework, proving that the worst-case interval width is governed by W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle, where Δ(1/ê) is the inverse propensity variation across the conformal set. We conjecture and empirically test that worst-case pseudo-outcomes are achieved at propensity-extreme confounder values, enabling selective enumeration.\n\nThis framework instantiates as two tracks: **Track A (ITE intervals)** adapts modular conformal prediction (Zhang et al. 2025, arXiv 2510.04406) to a causal two-stage pipeline — Stage 1 produces conformal prediction sets over LLM-extracted categorical confounders using Adaptive Prediction Sets (APS; Romano, Sesia & Candès, NeurIPS 2020), Stage 2 constructs DR treatment effect intervals with FWER-controlled coverage tighter than Bonferroni via worst-case pseudo-outcome enumeration with explicit propensity propagation (O(|C|) per unit). **Track B (ATE intervals)** extends conformal prediction-powered inference (Csillag et al. 2025, arXiv 2510.16166) to the causal setting, where a small expert-labeled and large LLM-imputed dataset yield valid confidence intervals via Z-estimation with conformal set-predictors.\n\nA distinctive practical contribution is **principled abstention**: when conformal sets are large (|C|/K ≥ 0.6), intervals become vacuously wide, automatically detecting that LLM extraction quality is insufficient for credible causal conclusions. This constitutes a built-in LLM reliability assessment protocol for downstream causal analysis. We provide an operational decision rule: run conformal calibration on a held-out set; if median |C|/K > threshold, report \"extraction quality insufficient\" and estimate the human annotation volume needed to bring |C|/K below threshold.\n\n**Differentiation from closest related work:**\n\n(a) Classical measurement error correction (SIMEX, Cook & Stefanski 1994; regression calibration, Carroll et al. 2006) requires parametric assumptions — additive noise, independence from true values, Gaussian distribution — all violated by LLM extraction noise, which is categorical, context-dependent, and heterogeneous across subpopulations. We demonstrate this empirically: SIMEX coverage collapses under heterogeneous LLM noise.\n\n(b) Kluger et al. (arXiv 2501.18577, 2025) address PPI with imputed covariates via Predict-Then-Debias (PTD) Bootstrap — point imputation with asymptotic bootstrap CI. Our conformal set-predictor provides distribution-free finite-sample validity rather than asymptotic guarantees. We include PTD Bootstrap as a head-to-head experimental baseline to empirically demonstrate where conformal PPI improves over PTD, particularly in heterogeneous noise and small-sample regimes.\n\n(c) The \"No Free Lunch\" result (Mani et al. arXiv 2505.20178, 2025) proves PPI++ can underperform gold-standard-only estimation when pseudo-label correlation is low. Our conformal set-predictor (Csillag et al. 2025) differs: validity holds regardless of LLM quality (wider intervals, not invalid intervals), but efficiency gain over labeled-only estimation requires conformal sets to be sufficiently tight. We empirically characterize the crossover: Track B improves over labeled-only estimation when median |C|/K ≤ 0.4.\n\n(d) Barnatchez et al. (arXiv 2604.03772, 2026) handle confounders entirely MISSING at deployment via semiparametric debiasing — distinct from our noisy-extraction setting. Vovk & Wang (arXiv 2603.11134, 2026) extend conformal e-prediction under confounding for prediction, not treatment effects.\n\n(e) DoubleLingo (NAACL 2024) and Ma et al. (NeurIPS 2025) use LLMs within DR causal estimators for text data but provide only asymptotic guarantees with no finite-sample uncertainty quantification for LLM extraction noise.\n\nCross-conformal calibration (Gasparin & Ramdas, ICML 2025, arXiv 2503.01495) reduces the three-way data split to two-way, improving sample efficiency. A secondary exploratory track uses Matryoshka embeddings (128–256d) with ellipsoidal conformal sets (Xu et al. ICML 2024; Lützow et al. arXiv 2605.12341, 2026) and convex relaxation restricted to smooth nuisance estimators (Wang & Dobriban, arXiv 2602.00989, 2026); this requires a feasibility pilot before committing.\n\nWhile the framework is theoretically domain-agnostic (applicable wherever ML models extract features for downstream causal inference), we focus on LLM-extracted text confounders as the primary instantiation.\n\n**Exchangeability conditions.** Stage 1 conformal calibration requires (approximate) exchangeability between calibration and test examples. This holds when texts are i.i.d. from the same distribution. When systematic distributional shift exists (e.g., different hospital systems, temporal drift in clinical language), we invoke weighted exchangeability (Barber et al. Annals of Statistics 2023) with likelihood ratio weights estimated from observable text features. Coverage degrades gracefully as a function of weight variability, which we empirically characterize.\n\n## Core Problem\n\nCausal inference from observational text data (clinical notes, social media, policy documents) requires adjusting for confounders embedded in unstructured text. LLMs can extract these confounders, but extraction is imperfect. No existing framework provides finite-sample coverage guarantees for treatment effects when confounders are extracted by a fallible LLM.\n\nThe problem is distinct from classical measurement error: (1) LLM extraction noise is heterogeneous and context-dependent (confusion rates between \"critical\" and \"severe\" depend on text content), violating the additive-noise-independent-of-truth assumptions of SIMEX (Cook & Stefanski 1994) and regression calibration (Carroll et al. 2006); (2) LLM extraction produces categorical or embedding-space outputs, not continuous measurements. Conformal prediction provides a distribution-free, finite-sample alternative.\n\n## Opportunity\n\nThree research threads can now be unified: (1) modular conformal prediction for sequential pipelines (Zhang et al. 2025, arXiv 2510.04406); (2) conformal PPI (Csillag et al. 2025, arXiv 2510.16166) for valid inference with ML-imputed covariates; (3) conformal meta-learners for ITE (Alaa et al. NeurIPS 2023) assuming error-free confounders. The critical missing piece is understanding how extraction uncertainty propagates through the DR estimator's propensity component — the 1/ê(c) amplification creates a previously uncharacterized (in finite-sample, distribution-free terms) interaction between extraction and estimation stages. Matryoshka embedding models (Qwen3-Embedding-8B) make conformal prediction over embedding spaces potentially tractable. Growing interest in conformal + causal (Barnatchez et al. arXiv 2604.03772; Vovk & Wang arXiv 2603.11134; Systematic Review arXiv 2509.21660) confirms timeliness.\n\n## Landscape\n\nConformal ITE methods (Lei & Candès JRSS-B 2021; Alaa et al. NeurIPS 2023; wTCP-DR KDD 2024) assume error-free confounders. The conformal NLP survey (Campos et al. TACL 2024) covers classification/QA/generation but not causal validity. PPI causal extensions (arXiv 2502.06343; Kato arXiv 2511.08303, NeurIPS 2025) do not incorporate conformal sets for imputed covariates. Zhang et al. (2025) handle sequential pipelines but not causal settings or weighted exchangeability. PPI (Angelopoulos et al. Science 2023) and its extensions address labeled/unlabeled splits but not conformal set propagation. Multi-variable conformal prediction (Lützow et al. arXiv 2605.12341, 2026) and ellipsoidal sets (Xu et al. ICML 2024) provide geometric tools for moderate-dimensional conformal regions. Recent work on LLM extraction calibration (Shrestha & Kim, arXiv 2603.00924, 2026) shows domain/category-dependent miscalibration, motivating careful nonconformity score design in Stage 1.\n\n## Approach\n\n**Data Splitting.** Baseline three-way split: (S1) training, (S2) Stage 1 calibration, (S3) Stage 2 calibration. Improvements: K-fold cross-fitting within S1 (Chernozhukov et al. 2018 DML); cross-conformal Stage 1 (Gasparin & Ramdas, ICML 2025, arXiv 2503.01495) merging S2 into S1 (coverage ≥ 1−2α₁). Requirements: n₃ ≥ 150, n_total ≥ 500. For n < 300, Track B preferred.\n\n**Track A — Modular Conformal ITE Intervals (Primary).** Adapts Zhang et al. (2025) residual decomposition R ≤ ΔR₁ + R₂. Stage 1: LLM extracts categorical confounders via prompted classification. Nonconformity score: APS (Romano, Sesia & Candès, NeurIPS 2020) as default, with ablation against RAPS and naïve softmax (THR). Stage 2: worst-case pseudo-outcome enumeration.\n\nFor each c ∈ C(x): φ̂(c; Yᵢ, Aᵢ) = [μ̂₁(c) − μ̂₀(c)] + Aᵢ·(Yᵢ − μ̂₁(c))/ê(c) − (1−Aᵢ)·(Yᵢ − μ̂₀(c))/(1−ê(c))\n\nThe propensity variation Δ(1/ê) across the conformal set is the dominant widening driver. Propensity trimming (ê(c) clipped to [τ, 1−τ], default τ=0.05) bounds amplification; we ablate τ ∈ {0.01, 0.05, 0.10}. The modular FWER control yields provably tighter intervals than naive Bonferroni.\n\n**Pilot Conservatism Analysis.** K=5 severity categories:\n\n| Category | μ̂₁(c) | μ̂₀(c) | ê(c) | CATE |\n|----------|--------|--------|-------|------|\n| none     | 0.40   | 0.30   | 0.50  | 0.10 |\n| mild     | 0.50   | 0.35   | 0.45  | 0.15 |\n| moderate | 0.60   | 0.40   | 0.40  | 0.20 |\n| severe   | 0.72   | 0.45   | 0.35  | 0.27 |\n| critical | 0.85   | 0.50   | 0.25  | 0.35 |\n\nWidening: |C|=1 → 0%; |C|=2 → ~60%; |C|=3 → ~100%; |C|≥4 → vacuously wide (principled abstention). Method is practically useful when |C| ≤ 2 for K=5.\n\n**Continuous Embedding Track (Exploratory).** Qwen3-Embedding-8B with Matryoshka 128–256d, ellipsoidal conformal sets, convex relaxation (Lipschitz + Taylor) restricted to smooth nuisance estimators. Requires feasibility pilot; if intervals >5× oracle, reported as preliminary/future work.\n\n**Track B — Conformal PPI for ATE Intervals.** Applies conformal PPI (Csillag et al. 2025, arXiv 2510.16166) to ATE estimation via Z-estimation with conformal set-predictors: E[inf φ(C(X))] − M·Err(C) ≤ ATE ≤ E[sup φ(C(X))] + M·Err(C). Extends PPI causal inference (arXiv 2502.06343). Efficiency gain over labeled-only requires median |C|/K ≤ 0.4.\n\n**Experimental Design.**\n\n*Baselines (six layers):*\n- Layer 0 (Oracle): Ground-truth confounders → DR estimator + conformal ITE (Alaa et al. NeurIPS 2023)\n- Layer 1 (Naive plug-in): LLM point prediction as ground truth → DR + BCa bootstrap CI\n- Layer 1.5 (Classical ME correction): SIMEX (Cook & Stefanski 1994) applied to LLM point predictions → DR estimator\n- Layer 2 (Asymptotic): DoubleLingo (NAACL 2024) / Ma et al. (NeurIPS 2025) asymptotic CI\n- Layer 2.5 (PTD Bootstrap): Kluger et al. (arXiv 2501.18577) Predict-Then-Debias Bootstrap (for Track B comparison)\n- Layer 3 (Proposed): ConformalPPITextCausal Track A / Track B\n\n*Benchmarks:*\n\n(1) Semi-synthetic MIMIC-IV clinical notes (MIMIC-IV-Note v2.2; MIMIC-III NOTEEVENTS backup): treatment = escalation to aggressive therapy; confounder = disease severity from discharge summaries. MIMIC structured fields (ICD codes, lab values) as proxy ground-truth confounders. DGP: p(A=1|C) = σ(β₀ + β₁·severity_score); Y(a) = f(C, a) + ε with heterogeneous CATE. LLM noise: (a) real extraction (GPT-4/Claude/Llama), (b) controlled noise injection (misclassification rate 5%–40%). Fixed text + resampled (A, Y) following Veitch et al. (UAI 2020).\n\n(2) Semi-synthetic social media (Veitch et al. UAI 2020 paradigm): content moderation effect on engagement, toxicity as confounder.\n\n(3) Fully synthetic (3 scenarios, 200+ seeds each):\n- Scenario 1 (Benign): moderate overlap ê(c) ∈ [0.25, 0.75], 5% misclassification\n- Scenario 2 (Challenging propensity): poor overlap ê(c) ∈ [0.1, 0.9]\n- Scenario 3 (Heterogeneous noise): extraction error 2%–30% by subgroup\n\n*Evaluation:*\n- Empirical coverage at 90%/95% with binomial exact CI (Clopper-Pearson) and one-sided test H₀: coverage < 1−α\n- Interval width relative to oracle/baselines; widening ratio W vs. |C|/K\n- Conditional coverage stratified by: |C| (1/2/3+), propensity quintile, treatment group\n- Calibration plots: α swept 0.01–0.20 with ±2σ binomial band\n- Computational cost table (per-sample time)\n- LLM extraction quality table: per-LLM accuracy, F1, confusion matrix, empirical |C| distribution at α₁=0.05/0.10\n\n*Ablations:*\n- Stage-wise uncertainty attribution (Stage 1 Δφ vs. Stage 2 conformal quantile decomposition)\n- Track A vs. Track B on ATE under identical settings\n- n_labeled sensitivity for Track B (50–500+) with labeled-only crossover analysis\n- |C|/K sweep 0.2–0.8\n- Nonconformity score: APS vs. RAPS vs. THR\n- Propensity trimming threshold: τ ∈ {0.01, 0.05, 0.10}\n- Cross-conformal vs. split (sample efficiency cost)\n\n*Honest framing:* Finite-sample advantage is most pronounced at n < 1000 with heterogeneous noise. At large samples with uniform noise, asymptotic methods may perform comparably.\n\n## Resource Estimate\n\nGPU hours: 200–300 (A100), ~$300–450. Timeline: 10 weeks. Weeks 1–3: Theory (modular decomposition under weighted exchangeability, amplification characterization, conformal PPI ATE). Weeks 4–5: Implement categorical pipeline + PPI track + baseline suite (PTD Bootstrap, SIMEX). Week 6: Continuous track feasibility pilot. Weeks 7–8: Core experiments. Week 9: Ablations + conditional coverage. Week 10: Writing. Annotation: ~20h (guideline verification + spot check using MIMIC structured fields as proxy ground truth). PhysioNet credentialing: apply immediately; MIMIC-III backup. Claude API (human-in-loop): $100–150.\n\n## Inspired By\n\nGap: Existing conformal causal methods assume error-free confounders; text-based causal methods provide only asymptotic guarantees; classical measurement error correction requires parametric assumptions; Kluger et al. use asymptotic debiasing only; IPW amplification of measurement error is known asymptotically but lacks finite-sample conformal characterization. Pattern: Three converging literatures (modular CP, conformal PPI, conformal causal inference) unified by the insight that propensity score amplification governs the extraction-estimation interaction. Key enablers: Zhang et al. (arXiv 2510.04406); Csillag et al. (arXiv 2510.16166); Alaa et al. (NeurIPS 2023); Barber et al. (Annals of Statistics 2023).\n\n## Target Venues\n\n- AAAI 2027 (Primary — abstract July 21, full paper July 28, 2026)\n- ARR August 2026 cycle (Secondary — submission August 3, 2026) → EACL 2027\n- AISTATS 2027 (Stretch — estimated deadline ~October 2026)\n\n## Key References\n\n- Zhang et al. 'Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition' (arXiv 2510.04406, 2025)\n- Csillag et al. 'Extending Prediction-Powered Inference through Conformal Prediction' (arXiv 2510.16166, 2025)\n- Angelopoulos et al. 'Prediction-Powered Inference' (Science, 2023)\n- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)\n- Kato 'Semi-Supervised Treatment Effect Estimation via Generalized Riesz Regression' (arXiv 2511.08303, NeurIPS 2025)\n- Barber et al. 'Conformal prediction beyond exchangeability' (Annals of Statistics, 2023)\n- Alaa et al. 'Conformal Meta-learners for Predictive Inference of Individual Treatment Effects' (NeurIPS 2023)\n- Wang & Dobriban 'Optimal Decision-Making Based on Prediction Sets' (arXiv 2602.00989, 2026)\n- Lützow et al. 'Multi-Variable Conformal Prediction without Data Splitting' (arXiv 2605.12341, 2026)\n- Xu et al. 'Conformal prediction for multi-dimensional time series by ellipsoidal sets' (ICML 2024)\n- Campos et al. 'Conformal Prediction for Natural Language Processing: A Survey' (TACL, 2024)\n- Systematic Review of Conformal Inference for Treatment Effect Estimation (arXiv 2509.21660, 2025)\n- Lei & Candès 'Conformal Inference of Counterfactuals and Individual Treatment Effects' (JRSS-B, 2021)\n- DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)\n- Ma et al. 'LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding' (NeurIPS 2025)\n- Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)\n- Veitch et al. 'Adapting Text Embeddings for Causal Inference' (UAI 2020)\n- Barnatchez et al. 'Debiased ML for Conformal Prediction under Runtime Confounding' (arXiv 2604.03772, 2026)\n- Vovk & Wang 'Conformal e-prediction in the presence of confounding' (arXiv 2603.11134, 2026)\n- Gasparin & Ramdas 'Improving cross-conformal prediction' (arXiv 2503.01495, ICML 2025)\n- Chernozhukov et al. 'Double/debiased machine learning' (Econometrics Journal, 2018)\n- Kluger et al. 'PPI with Imputed Covariates and Nonuniform Sampling' (arXiv 2501.18577, 2025)\n- Mani et al. 'No Free Lunch: Non-Asymptotic Analysis of PPI' (arXiv 2505.20178, 2025)\n- Carroll et al. 'Measurement Error in Nonlinear Models' (2nd ed., Chapman & Hall, 2006)\n- Cook & Stefanski 'Simulation-Extrapolation Estimation in Parametric Measurement Error Models' (JASA, 1994)\n- Romano, Sesia & Candès 'Classification with Valid and Adaptive Coverage' (NeurIPS 2020)\n- Shrestha & Kim 'Conformal Prediction for Risk-Controlled Medical Entity Extraction' (arXiv 2603.00924, 2026)"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:31:15.599Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:31:15.599Z",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-20T04:31:15.610Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient context from the field research. Let me compile the full evaluation.

---

```
【阶段】: Triage

【领域调研】:
- Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition" (arXiv 2510.04406, 2025): Track A 的直接理论基础。提出两阶段序贯模型的残差分解框架，用于供应链和股票市场预测，但未涉及因果推断设置。本 proposal 的 Track A 将其扩展到 DR 估计器是合理的延伸。
- Csillag et al. "Extending Prediction-Powered Inference through Conformal Prediction" (arXiv 2510.16166, 2025): Track B 的直接理论基础。将 conformal set-predictor 引入 PPI 框架，实现 Z-estimation 和 M-estimation 的有效推断。本 proposal 将其应用于 ATE 因果推断是新的应用方向。
- Kluger et al. "PPI with Imputed Covariates and Nonuniform Sampling" (arXiv 2501.18577, 2025): 最直接的竞争工作。使用 Predict-Then-Debias Bootstrap 处理 imputed covariates，提供渐近有效的 CI。proposal 明确将其列为 head-to-head baseline，声称在 heterogeneous noise 和小样本下 conformal 方法更优——这一 claim 需要实验验证。
- Mani et al. "No Free Lunch: Non-Asymptotic Analysis of PPI" (arXiv 2505.20178, 2025): 证明 PPI++ 在 pseudo-label 相关性低时可能劣于仅使用 gold-standard。Proposal 对此有明确回应（conformal set-predictor 产生更宽区间而非无效区间），positioning 合理。
- DoubleLingo (NAACL 2024): 使用 LLM 作为 nuisance model 进行 Double ML 因果估计，但仅提供渐近保证。是 proposal 的重要 baseline。
- Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding" (NeurIPS 2025): 处理推断时文本混杂，使用自定义 DR learner，同样仅渐近保证。
- Lei & Candès (JRSS-B 2021); Alaa et al. (NeurIPS 2023); wTCP-DR (KDD 2024): Conformal ITE 方法，均假设无误差混杂变量。Proposal 的 gap 声称成立。
- Campos et al. "Conformal Prediction for NLP: A Survey" (TACL 2024): 覆盖分类/QA/生成，不涉及因果有效性，证实该交叉领域存在空白。
- Barnatchez et al. (arXiv 2604.03772, 2026); Vovk & Wang (arXiv 2603.11134, 2026): 最新的 conformal + causal 工作，但分别处理 missing confounders 和 conformal e-prediction，与本 proposal 的 noisy-extraction 设定不同。
- 调研总结: Conformal prediction × causal inference × LLM text extraction 的三重交叉确实是一个未被填补的 gap。现有工作要么假设无误差混杂（conformal causal），要么仅提供渐近保证（LLM causal），要么处理不同设定（missing confounders）。Proposal 的定位在文献中是准确的，novelty claim 基本成立。但这个交叉非常 niche，目标受众较窄。

【整体印象】: 
作为审稿人，第一反应是"这是一份技术上极其详尽的 proposal，作者显然深度掌握了三个交叉领域的文献"。proposal 识别了一个真实存在的 gap（conformal + causal + noisy LLM extraction），理论动机清晰（IPW amplification 的 finite-sample 刻画），实验设计堪称 exhaustive。然而，几个关键顾虑会让我犹豫：(1) 核心方法论本质上是将已有框架（Zhang et al. 的 modular CP + Csillag et al. 的 conformal PPI + 标准 DR 估计器）组合应用到一个新设定，而非提出根本性的新方法；(2) pilot analysis 显示方法实际有用的窗口很窄（|C|≤2 for K=5），这削弱了实践价值；(3) 论文密度极高，同时包含 Track A、Track B、exploratory embedding track、6 层 baseline、多维 ablation，存在"什么都做但什么都不深"的风险。倾向 borderline，偏向 weak accept/reject 之间。

【核心贡献】: 
核心贡献有三层：(1) 理论层——首次在 distribution-free、finite-sample 框架下刻画了 IPW amplification 如何放大 conformal set 中的提取不确定性，给出了区间宽度的 worst-case bound W；(2) 方法层——将 modular conformal prediction 和 conformal PPI 统一为一个两阶段因果推断框架（Track A for ITE, Track B for ATE）；(3) 实践层——principled abstention 机制，当 LLM 提取质量不足时自动检测并报告。
价值评估：理论贡献是最有价值的部分，因为 IPW amplification 的 finite-sample conformal 刻画确实是新的。但方法贡献更多是已有工具的组合，实践贡献（abstention）虽然有用但技术含量有限。整体而言，对领域的贡献是 incremental-to-moderate：它填补了一个真实的 gap，但不太可能改变这个方向的研究范式。

【方法合理性】: 
方法在技术上是合理的：
- Stage 1 使用 APS 对 LLM 提取的 categorical confounders 构建 conformal prediction sets 是标准做法
- Stage 2 通过 worst-case pseudo-outcome enumeration 传播不确定性，利用 DR 估计器的结构是合理的
- 两个 track 分别处理 ITE 和 ATE 是合理的分工

**更简单的替代方案问题**：这是主要风险点。一个审稿人可能会问：
(a) 如果 LLM 提取质量足够高（|C|≤2），直接用 point prediction + bootstrap CI（如 DoubleLingo）是否已经足够好？pilot analysis 显示只有在这个窗口内方法才实用，但在这个窗口内 naive 方法可能也表现不错。
(b) 为什么不直接用 calibrated LLM probabilities 做 soft imputation，而要走 conformal set 这条更复杂的路？这需要强有力的实验证据来回答。
(c) Propensity trimming（τ=0.05）已经是标准做法来控制 IPW amplification，conformal propagation 的额外价值需要清晰展示。

proposal 承认了 honest framing（大样本 + 均匀噪声下渐近方法表现相当），这是加分项，但也意味着方法的优势区间可能较窄。

【5 维度打分】:
  1. 研究问题: [强] — 因果推断 + LLM 提取 + finite-sample 保证的交叉是一个真实、重要、有时效性的问题。随着 LLM 在文本数据因果分析中的应用增加（DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），对提取不确定性的严格处理有明确需求。Barnatchez et al. (2026) 和 Vovk & Wang (2026) 的最新工作进一步确认了 conformal + causal 方向的热度。研究问题的价值不依赖于特定方法的选择。
  
  2. 方法与创新: [中] — Novelty 主要在于将 Zhang et al. (2510.04406) 的 modular CP 和 Csillag et al. (2510.16166) 的 conformal PPI 组合应用到因果推断设定，并加入 IPW amplification 的 finite-sample 刻画。IPW amplification 本身是 well-known phenomenon（Babanezhad et al. 2010），novelty 在于 conformal 框架下的刻画，这是增量式创新而非突破式创新。与 Kluger et al. (2501.18577) 的差异化（distribution-free vs. asymptotic）是清晰的，但实际优势需要实验验证。exploratory embedding track 增加了方法的广度但降低了深度。
  
  3. 实验设计: [强] — 这是 proposal 最突出的亮点。6 层 baseline 设计（Oracle → Naive → SIMEX → Asymptotic → PTD Bootstrap → Proposed）层次分明，覆盖了所有合理的对比方法。三类 benchmark（MIMIC-IV 半合成、社交媒体半合成、全合成 3 场景）覆盖了不同数据特征。ablation 设计系统性强（nonconformity score、trimming threshold、cross-conformal vs. split、|C|/K sweep、n_labeled sensitivity）。评估指标全面（coverage + width + conditional coverage + calibration plot）。Honest framing（大样本优势消失）是加分项。唯一不足：缺少真实因果效应的 ground-truth 数据集（所有都是半合成或全合成），但这在因果推断领域是普遍限制。
  
  4. 可行性: [中] — 资源估计合理（200-300 GPU hours, 10 weeks, ~$450）。但执行风险较高：(a) 同时推进 Track A + Track B + exploratory embedding track + 6 层 baseline + 3 类 benchmark + 多维 ablation，工作量巨大；(b) MIMIC-IV 需要 PhysioNet credentialing，存在时间风险（proposal 提到了 MIMIC-III backup）；(c) exploratory embedding track 明确需要 feasibility pilot，可能不可行；(d) 理论证明（modular decomposition under weighted exchangeability）的难度可能被低估。10 周时间线非常紧张。
  
  5. 写作与呈现: [中] — 作为 proposal，逻辑结构清晰，文献定位精准，differentiation 细致。但信息密度极高——同时覆盖理论贡献、两个主要 track、一个探索 track、多个 benchmark、大量 ablation。在 8 页正文的限制下，如何有效组织这些内容是重大挑战。存在"什么都想展示，结果哪个都讲不透"的风险。建议明确主次：Track A 为主、Track B 为辅、embedding track 放 appendix。

【概率估计】: [22% - 38%] 中位 30%

【估计理由】: 
研究问题真实且有时效性（强），实验设计非常完备（强），这两个维度显著拉高了中稿概率。但方法创新度为增量式组合（中），实际有用的窗口较窄（|C|≤2），且论文的 scope 过于庞大，在 8 页篇幅内难以充分展开。EMNLP 审稿人背景偏 NLP，对 conformal prediction 和因果推断的 heavy theory 可能缺乏足够专业知识来充分评估，审稿人匹配是额外的不确定性因素。与 Kluger et al. (PTD Bootstrap) 的实际性能差距（即 conformal 方法在 heterogeneous noise 下的优势幅度）是决定性的实验问题——如果优势不显著，novelty claim 会被大幅削弱。30% 反映"方向正确、执行可期但创新度和实用性存在审稿人合理质疑"的判断。上界 38% 对应"实验结果清晰展示了 conformal 方法在目标场景下的优势"的乐观情景；下界 22% 对应"审稿人认为是已有方法的简单组合 + 实用窗口太窄"的悲观情景。

【主要风险】: 
1. **"组合 vs. 创新"质疑**：审稿人可能认为核心方法是 Zhang et al. modular CP + Csillag et al. conformal PPI + 标准 DR 的直接拼接，IPW amplification 的 finite-sample 刻画虽然新但属于 incremental contribution，insufficiently novel for a top venue。
2. **实用性窗口过窄**：pilot analysis 自己揭示了 |C|≤2（K=5 时）才实用的限制。审稿人会追问：在 LLM 提取质量好到 |C|≤2 的场景下，更简单的 baseline（naive plug-in + bootstrap）是否已经足够好？如果答案是"差距不大"，整个方法的 practical motivation 会被动摇。

【实施评估】:
  - 计算资源: 200-300 A100 GPU hours (~$300-450)，合理
  - 数据需求: MIMIC-IV-Note（需 PhysioNet credentialing）+ 社交媒体文本 + 合成数据；需要 ~200 条人工标注用于 calibration 验证
  - 人工介入: ~20h annotation（标注指南验证 + spot check），使用 MIMIC 结构化字段作为 proxy ground truth
  - 训练需求: 需要训练/微调 propensity score 模型和 outcome 模型（nuisance estimators），但计算量不大；LLM 推断（GPT-4/Claude/Llama extraction）是主要成本
  - 新 Benchmark: 3 类半合成/全合成 benchmark（MIMIC-IV, 社交媒体, 全合成），非全新 benchmark 但需要构建 DGP pipeline
  - 预估周期: 10 周（紧张但可能，如果 exploratory track 可以放松为 future work）
```

Sources:
- [Modular and Adaptive Conformal Prediction for Sequential Models](https://arxiv.org/abs/2510.04406)
- [Extending Prediction-Powered Inference through Conformal Prediction](https://arxiv.org/abs/2510.16166)
- [Prediction-Powered Inference with Imputed Covariates](https://arxiv.org/abs/2501.18577)
- [No Free Lunch: Non-Asymptotic Analysis of PPI](https://arxiv.org/abs/2505.20178)
- [DoubleLingo: Causal Estimation with Large Language Models](https://aclanthology.org/2024.naacl-short.71/)
- [LLM-Driven Treatment Effect Estimation Under Text Confounding](https://arxiv.org/pdf/2507.02843)
- [Conformal Prediction for NLP: A Survey (TACL 2024)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/)
- [Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)](https://dl.acm.org/doi/10.1145/3637528.3671976)
- [A Systematic Review of Conformal Inference for Treatment Effects](https://www.arxiv.org/pdf/2509.21660)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct the evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:
- Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition" (arXiv 2510.04406, Oct 2025): Track A 的直接理论基础。该工作提出了两阶段顺序模型的残差分解 CP 框架，但未涉及因果估计或加权可交换性。本 proposal 将其扩展到因果 DR 估计器是自然但非平凡的延伸。
- Csillag et al. "Extending Prediction-Powered Inference through Conformal Prediction" (arXiv 2510.16166, Oct 2025): Track B 的直接理论基础。将 PPI 与 conformal set-predictor 结合，提供 Z-/M-estimation 下的有效推断。本 proposal 将其扩展到 ATE 估计是合理的增量。
- Kluger et al. "PPI with Imputed Covariates and Nonuniform Sampling" (arXiv 2501.18577, Jan 2025): 最直接的竞争者。使用 PTD Bootstrap 处理 imputed covariates，提供渐近有效的 bootstrap CI。本 proposal 的核心差异化在于有限样本分布无关保证 vs. 渐近保证。
- Mani et al. "No Free Lunch: Non-Asymptotic Analysis of PPI" (arXiv 2505.20178, May 2025): 证明 PPI++ 在 pseudo-label 相关性低时可能劣于仅用 gold-standard。本 proposal 正确识别了这一风险，并论证 conformal set-predictor 在质量差时会变宽而非失效。
- DoubleLingo (NAACL 2024): 将 LLM 嵌入 DR 因果估计器中处理文本混杂变量，但仅提供渐近保证。本 proposal 补充了有限样本 UQ 层。
- Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding" (NeurIPS 2025): 处理推断时文本混杂问题（训练时完整观测、推断时仅有文本），与本 proposal 的 noisy extraction setting 不同但高度相关。同样仅渐近保证。
- Barnatchez et al. (arXiv 2604.03772, Apr 2026): 处理部署时混杂变量完全缺失的场景（runtime confounding），用半参数去偏。与本 proposal 的 noisy extraction 场景明确区分。
- Alaa et al. "Conformal Meta-learners for Predictive Inference of ITE" (NeurIPS 2023): 假设混杂变量无误差的 conformal ITE 方法。本 proposal 放松了这一假设。
- Systematic Review of Conformal Inference for Treatment Effects (arXiv 2509.21660, 2025): 综述确认该领域活跃但尚无工作同时处理 ML-extracted confounders + finite-sample guarantees。
- 调研总结: conformal prediction × causal inference 是2025-2026年的活跃研究前沿，但现有工作要么假设无误差混杂变量（Alaa et al.），要么仅提供渐近保证（DoubleLingo, Ma et al.），要么不使用 conformal sets（Kluger et al.）。本 proposal 填补了一个真实的空白：将 conformal uncertainty 从 ML extraction 阶段传播到因果估计阶段的分布无关有限样本框架。

【整体印象】:
作为审稿人，我的第一反应是：这是一篇技术上非常 solid、问题定义清晰、实验设计极其充分的 proposal。它填补了 conformal prediction + causal inference + LLM extraction 三个领域交叉处的一个真实空白。但核心贡献本质上是**组合性**的——将已有的 modular CP (Zhang et al.) 和 conformal PPI (Csillag et al.) 适配到因果设定中，关键的 IPW amplification analysis 虽然是新的形式化但基于已知现象。我会倾向于 **weak accept / borderline**，最终取决于理论贡献的深度和实验结果的说服力。

【核心贡献】:
1. **理论贡献**: 首个在 conformal set 框架下对 IPW amplification 的分布无关有限样本刻画（W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle）
2. **方法贡献**: 两条互补的 track——Track A (modular conformal ITE intervals) 和 Track B (conformal PPI ATE intervals)——为不同场景提供适用方案
3. **实践贡献**: principled abstention 机制（当 |C|/K ≥ 0.6 时自动检测 LLM extraction 质量不足）

这些贡献对领域的价值是**中等偏上**的。问题重要且及时（LLM 提取文本混杂变量越来越常见），但方法的核心是已有技术的组合与适配，而非根本性创新。IPW amplification 的 conformal 形式化有一定理论新意，但其实际影响取决于证明的紧致性。

【方法合理性】:
方法整体合理，逻辑链清晰：LLM extraction → conformal calibration (Stage 1) → uncertainty propagation through DR estimator (Stage 2)。关键设计选择（APS 作为 nonconformity score、propensity trimming、worst-case pseudo-outcome enumeration）都有充分的文献支撑。

**潜在替代方案的威胁**:
- Kluger et al. 的 PTD Bootstrap 是最直接的竞争者。本 proposal 的优势（有限样本保证 vs. 渐近保证）在小样本 + 异质噪声场景下最为显著，但在大样本场景下渐近方法可能表现相当——proposal 自身也承认了这一点（honest framing）。
- 一个更简单的替代方案是：直接用 LLM softmax probabilities 进行加权 DR 估计（不经 conformal calibration），这可能在某些场景下效果相当。Proposal 需要在实验中明确展示 conformal calibration 相对于 naive softmax weighting 的增益。

**理论风险**: proposal 中有一个"conjecture"（worst-case pseudo-outcomes 出现在 propensity-extreme confounder values），这需要严格证明或充分的经验验证。如果这一 conjecture 不成立，selective enumeration 的效率优势不保。

【5 维度打分】:

1. 研究问题: 【强】— 问题重要且定义清晰。LLM 提取文本混杂变量的不确定性传播缺乏有限样本保证，这是一个被 systematic review (arXiv 2509.21660) 确认的真实空白。与 classical measurement error 的区分论证有力（categorical, context-dependent, heterogeneous noise vs. additive Gaussian noise）。

2. 方法与创新: 【中】— 核心方法是已有技术的组合适配：Track A 适配 Zhang et al. (2025)，Track B 扩展 Csillag et al. (2025)。IPW amplification 的 conformal 形式化是新的（对比 Babanezhad et al. 2010、Yi & Chen 2023 的渐近/参数化分析），但本质上是已知现象的新 wrapper。与 Kluger et al. (2025) 的差异化（finite-sample vs. asymptotic）清晰但增量性明显。Principled abstention 机制虽有实用价值但技术上并不深刻（conformal set 大 → interval 宽是 conformal prediction 的自然性质）。

3. 实验设计: 【强】— 这是 proposal 最突出的优势。六层 baseline（从 oracle 到 proposed method）层次分明；三类 benchmark 覆盖不同场景；评估指标全面（coverage with Clopper-Pearson CI、conditional coverage stratification、calibration plots）；ablation 设计系统化（nonconformity score、propensity trimming、cross-conformal、n_labeled sensitivity）。Honest framing（承认大样本 + 均匀噪声下渐近方法可能表现相当）大幅提升可信度。直接包含 Kluger et al. PTD Bootstrap 和 SIMEX 作为 head-to-head baseline 也是加分项。

4. 可行性: 【中偏强】— GPU 需求（200-300 A100 hours）和预算（~$450）非常可控。10 周时间线对 core Track A+B 可行，但包含 embedding exploratory track + 所有 ablation 可能偏紧。主要风险：(a) PhysioNet credentialing 可能延迟 MIMIC 数据获取；(b) 理论证明（尤其是 conjecture 的严格化）可能比预期耗时；(c) 范围过于宽泛（两个 track + exploratory track + 大量 ablation），需要严格优先级管理。

5. 写作与呈现: 【强】— Proposal 逻辑清晰、结构完整。问题动机→现有工作不足→方法→实验的论证链条流畅。与相关工作的差异化（五个方向逐一对比）非常到位。数学形式化具体（给出了 DR pseudo-outcome 公式、widening ratio W 的表达式、pilot conservatism analysis table）。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
向上推动因素：(1) 问题重要且时机好——conformal + causal 是2025-2026热点但尚无工作处理 LLM extraction uncertainty；(2) 实验设计极其充分，远超多数 proposal 的水平；(3) honest framing 和 thorough differentiation 提升可信度；(4) 资源需求合理，核心实验可执行。
向下拉动因素：(1) 核心创新是组合性的——审稿人可能认为这是 Zhang et al. + Csillag et al. 的"trivial" adaptation，尤其如果 IPW amplification analysis 的证明深度不足；(2) 理论中存在未证明的 conjecture；(3) 范围过广（两个 track + embedding track），可能给人"散而不精"的印象；(4) 对于 EMNLP 评审池而言，conformal prediction 理论的审稿专业度参差不齐，可能导致评分方差大。中位 35% 反映了这是一篇扎实但未必突出的投稿——在"solid work"和"borderline"之间。

【主要风险】:
1. **Novelty 被质疑为组合性增量**: 最可能的拒稿理由。审稿人可能认为"将 modular CP 应用于因果估计 + 将 conformal PPI 扩展到 ATE"是已有方法的直接扩展，IPW amplification analysis 的新意不足以支撑一篇顶会论文。需要在理论深度（tight bounds, 非 trivial proofs）或实验中展示 surprising findings 来对冲此风险。
2. **理论贡献与实验贡献的平衡问题**: 如果理论证明不够紧致（尤其是 conjecture 未能严格证明），论文会被当作"实验 paper"评审；但如果实验不够充分（虽然 proposal 设计很好，执行中可能缩水），又会被当作"不完整的理论 paper"。两头都需要做实。

【实施评估】:
  - 计算资源: 200-300 A100 GPU hours (~$300-450)，非常可控，无瓶颈
  - 数据需求: MIMIC-IV-Note (需 PhysioNet credentialing，有 MIMIC-III 备选)；社交媒体数据 (Veitch et al. UAI 2020 范式，公开可用)；全合成数据 (无障碍)
  - 人工介入: ~20h 用于标注指南验证和抽样检查（使用 MIMIC 结构化字段作为 proxy ground truth），工作量极小
  - 训练需求: 无大规模模型训练。需要 fine-tune/prompt LLM 进行 confounder extraction，训练 DR 估计器的 nuisance models（propensity score + outcome models），但这些都是轻量级的
  - 新 Benchmark: 需要构建 semi-synthetic benchmark（MIMIC + social media），但有明确的 DGP 设计，不需要大规模标注
  - 预估周期: 10 周（理论 3 周 + 实现 3 周 + 实验 3 周 + 写作 1 周）。核心 Track A+B 可行；embedding exploratory track 可能被降级为 future work。PhysioNet credentialing 是时间线上的最大风险。
```

Sources:
- [Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition](https://arxiv.org/abs/2510.04406)
- [Extending Prediction-Powered Inference through Conformal Prediction](https://arxiv.org/abs/2510.16166)
- [PPI with Imputed Covariates and Nonuniform Sampling](https://arxiv.org/abs/2501.18577)
- [No Free Lunch: Non-Asymptotic Analysis of Prediction-Powered Inference](https://arxiv.org/abs/2505.20178)
- [DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)](https://aclanthology.org/2024.naacl-short.71/)
- [LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding (NeurIPS 2025)](https://arxiv.org/abs/2507.02843)
- [Debiased Machine Learning for Conformal Prediction Under Runtime Confounding](https://arxiv.org/abs/2604.03772)
- [A Systematic Review of Conformal Inference for Treatment Effect Estimation](https://arxiv.org/abs/2509.21660)
- [Conformal Meta-learners for Predictive Inference of ITE (NeurIPS 2023)](https://arxiv.org/abs/2202.04012)
- [Conformal Prediction for Natural Language Processing: A Survey (TACL 2024)](https://arxiv.org/abs/2405.01976)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Based on my research, I now have sufficient information to provide a comprehensive evaluation. Let me compile my assessment.

```
【阶段】: Triage

【领域调研】:
- Zhang et al. "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition" (arXiv 2510.04406, 2025): 核心建筑块之一。处理两阶段流水线中的模块化不确定性分解，但未涉及因果设定或加权可交换性。Proposal 正确识别了从该工作到因果设定的 gap。
- Csillag et al. "Extending Prediction-Powered Inference through Conformal Prediction" (arXiv 2510.16166, 2025): 另一核心建筑块。将 PPI 与 conformal prediction 连接，但未处理因果估计器中的倾向得分放大效应。Proposal 的 Track B 直接建立在此基础上。
- Kluger et al. "Prediction-Powered Inference with Imputed Covariates and Nonuniform Sampling" (arXiv 2501.18577, 2025): 最直接的竞争者。使用 Predict-Then-Debias Bootstrap 处理 imputed covariates，但提供渐近保证而非有限样本保证。Proposal 正确地将其纳入 baseline。
- Mani et al. "No Free Lunch: Non-Asymptotic Analysis of PPI" (arXiv 2505.20178, 2025): 证明 PPI++ 在低伪标签相关性时可能劣于纯 gold-standard。Proposal 恰当地讨论了这一限制，并将其转化为 conformal set-predictor 的优势论证。
- DoubleLingo (NAACL 2024): 在 DR 因果估计器中使用 LLM，但仅提供渐近保证。Proposal 正确识别了 finite-sample UQ 的 gap。
- Ma et al. "LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding" (NeurIPS 2025): 处理文本混淆因子的最新工作，同样仅提供渐近保证。
- Systematic Review of Conformal Inference for Treatment Effect Estimation (arXiv 2509.21660, 2025): 确认该领域活跃但现有方法均假设无误差的混淆因子。
- 调研总结: Proposal 处于三个活跃研究方向（模块化 CP、conformal PPI、因果推断 + LLM）的交汇点。其核心 novelty claim——"首个在 conformal set 框架下对 IPW 放大效应的无分布有限样本刻画"——在现有文献中确实未被占据。最直接竞争者（Kluger et al.）提供渐近保证，而非有限样本保证。

【整体印象】: 作为审稿人，我的第一反应是这是一篇 technically ambitious、问题定义清晰的 proposal，有真实的理论贡献。然而，我会有三个主要顾虑：(1) 论文试图在一篇工作中呈现 Track A + Track B + 探索性 embedding track，scope 过大；(2) Pilot analysis 显示实际有用的区间仅在 |C| ≤ 2 时成立（K=5），这意味着方法的实用场景相当受限；(3) 核心理论贡献（amplification characterization）目前是"conjecture and empirically test"状态，如果无法严格证明，论文主贡献将大打折扣。总体倾向：borderline，偏 weak accept 但需要执行质量非常高。

【核心贡献】: (1) 首个将 conformal prediction set 不确定性传播到因果估计器（特别是 DR 估计器的 IPW 组件）的理论框架，提供有限样本覆盖保证；(2) 对倾向得分放大效应的无分布刻画 W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle；(3) 原则性弃权机制作为 LLM 可靠性内置评估。对领域的价值中等偏上——解决了一个真实存在的理论 gap，但实际应用场景受限。

【方法合理性】: 方法在理论上合理——利用 conformal prediction 的分布自由特性来规避经典测量误差校正的参数假设，通过穷举 conformal set 中的最坏情况来获得有效区间。这是一个自然的思路。但存在两个替代方案的挑战：(1) 对于 ATE 估计（Track B），Kluger et al. 的 PTD Bootstrap 在大样本下可能表现类似且计算更简单；(2) 一个更简单的替代方案是直接使用多个 LLM 提取的 ensemble（而非 conformal set），通过对不同提取结果的分散度来量化不确定性。Proposal 需要在实验中清楚展示 conformal 方法何时（以及为何）优于这些更简单的替代品。

【5 维度打分】:
  1. 研究问题: [强] — 问题真实存在且重要。LLM 从文本中提取混淆因子用于因果推断是一个增长中的实践场景（DoubleLingo NAACL 2024, Ma et al. NeurIPS 2025），但现有方法缺乏有限样本保证。这个 gap 被 systematic review (arXiv 2509.21660) 和 No Free Lunch 结果间接证实。
  
  2. 方法与创新: [中] — 创新性真实但有限。核心思路是将两个已有框架（Zhang et al. 2025 的模块化 CP + Csillag et al. 2025 的 conformal PPI）应用到因果设定中。IPW 放大效应的有限样本刻画是新的，但本质上是已知渐近现象（Babanezhad et al. 2010）的 conformal 版本。与 Kluger et al. (2025) 的差异化——有限样本 vs 渐近——在实践中差距可能不大（大样本时两者趋同）。
  
  3. 实验设计: [强] — 实验设计非常完备。6 层 baseline（Oracle → Naive → SIMEX → Asymptotic → PTD Bootstrap → Proposed）覆盖了所有合理替代方案。三类 benchmark（MIMIC-IV 半合成 + 社交媒体 + 全合成）提供多样化验证。Ablation 设计全面（非conformity score、propensity trimming、cross-conformal vs split、|C|/K sweep）。Honest framing（承认大样本 + 均匀噪声时渐近方法可能媲美）增强可信度。这在同类 proposal 中是 top-tier 的实验规划。
  
  4. 可行性: [中] — 10 周时间线紧张但不是不可能。200-300 GPU hours 合理。主要风险：(a) MIMIC-IV 需要 PhysioNet 认证（有 MIMIC-III backup）；(b) 理论证明可能比预期更难（"conjecture and empirically test"表明尚未完成严格证明）；(c) 探索性 embedding track 可能需要砍掉以集中资源；(d) 如果 conformal set 在实际数据上普遍 |C| ≥ 3，方法可能无法展示实用性。
  
  5. 写作与呈现: [中] — Proposal 本身逻辑清晰、文献综述全面、differentiation 精确。但论文写作的挑战在于：两个 track + 探索性 track 的复杂结构需要极其清晰的表达来让审稿人理解。存在"信息过载"风险——审稿人可能觉得论文试图做太多事情而每件都不够深入。

【概率估计】: [25% - 38%] 中位 30%

【估计理由】: 
- 加分项：真实的理论 gap、极其完备的实验设计、timely topic（conformal + causal + LLM 三线交汇）、对局限性的诚实讨论、完善的 baseline 覆盖
- 减分项：(1) Scope 过大——两个完整 track + 探索性 track 在一篇论文中很难充分展开；(2) 实用性受限——仅在 |C| ≤ 2 时有用，这意味着 LLM 提取质量必须已经很高，限制了方法的适用场景；(3) 核心理论贡献尚未严格证明（"conjecture"状态）；(4) 有限样本优势主要在 n < 1000 时显现，这恰恰是 conformal calibration 数据最不充裕的区间，存在 tension；(5) EMNLP 审稿人可能对重统计理论的论文接受度较低（核心贡献更适合 AISTATS/JMLR）

【主要风险】: 
1. **实用性窄**：Pilot analysis 表明方法仅在 LLM 已经足够好（|C| ≤ 2/5）时才产生有意义的区间。审稿人可能质问："如果 LLM 提取已经这么准确，为什么还需要这个复杂框架？直接用 point estimate 的误差有多大？"
2. **理论执行风险**：核心 amplification characterization 目前是 conjecture 状态。如果无法在提交前严格证明（或证明过程中发现需要额外强假设），论文的核心贡献将从"理论+实证"降级为"纯实证"，显著降低竞争力。

【实施评估】:
  - 计算资源: 200-300 GPU hours (A100)，约 $300-450，合理且可负担
  - 数据需求: MIMIC-IV-Note（需 PhysioNet 认证，有 MIMIC-III backup）+ Veitch et al. 社交媒体数据（公开）+ 全合成数据
  - 人工介入: ~20h 标注验证（利用 MIMIC 结构化字段作为 proxy），轻量级
  - 训练需求: 无需训练大模型；需要训练/微调 nuisance estimators（propensity score, outcome models），计算量不大
  - 新 Benchmark: 需要构建 semi-synthetic benchmark（MIMIC-IV 上的因果 DGP），但基于已有数据和范式（Veitch et al. 2020），非从零开始
  - 预估周期: 10 周（紧张但可行，前提是理论部分能按时完成）
```

Sources:
- [Modular and Adaptive Conformal Prediction for Sequential Models](https://arxiv.org/abs/2510.04406)
- [Extending Prediction-Powered Inference through Conformal Prediction](https://arxiv.org/abs/2510.16166)
- [Prediction-Powered Inference with Imputed Covariates and Nonuniform Sampling](https://arxiv.org/abs/2501.18577)
- [No Free Lunch: Non-Asymptotic Analysis of PPI](https://arxiv.org/abs/2505.20178)
- [DoubleLingo: Causal Estimation with Large Language Models](https://aclanthology.org/2024.naacl-short.71/)
- [A Systematic Review of Conformal Inference for Treatment Effect Estimation](https://arxiv.org/html/2509.21660)
- [Conformal Prediction for Causal Effects of Continuous Treatments](https://arxiv.org/abs/2407.03094)
- [Prediction-Powered Inference (Science 2023)](https://www.science.org/doi/10.1126/science.adi6000)


【原始 proposal（允许参考但不是主要依据）】:
# Conformal Uncertainty Propagation for Causal Inference with LLM-Extracted Text Confounders

## Description

We propose a framework — ConformalPPITextCausal — for valid causal inference when text confounders are extracted by a fallible LLM. The core intellectual contribution is a general theory of **conformal uncertainty propagation through causal estimators**: how Stage 1 conformal prediction sets over ML-extracted variables interact with Stage 2 causal effect estimation, and how to exploit this interaction structure for provably tight finite-sample bounds.

The key structural insight is that in doubly robust (DR) estimators, extraction uncertainty propagates asymmetrically through the propensity score component via inverse probability weighting: a confounder value with ê(c)=0.25 amplifies outcome residuals 4×, while ê(c)=0.50 amplifies only 2×. The phenomenon of IPW amplifying measurement error is well-documented in the causal inference literature (Babanezhad et al. 2010; Yi & Chen 2023; Shu 2019), but existing analyses are asymptotic and assume parametric error models. We provide the **first distribution-free, finite-sample characterization** of this amplification within a conformal set framework, proving that the worst-case interval width is governed by W ≈ 1 + [Δ_CATE + |r|·Δ(1/ê)] / width_oracle, where Δ(1/ê) is the inverse propensity variation across the conformal set. We conjecture and empirically test that worst-case pseudo-outcomes are achieved at propensity-extreme confounder values, enabling selective enumeration.

This framework instantiates as two tracks: **Track A (ITE intervals)** adapts modular conformal prediction (Zhang et al. 2025, arXiv 2510.04406) to a causal two-stage pipeline — Stage 1 produces conformal prediction sets over LLM-extracted categorical confounders using Adaptive Prediction Sets (APS; Romano, Sesia & Candès, NeurIPS 2020), Stage 2 constructs DR treatment effect intervals with FWER-controlled coverage tighter than Bonferroni via worst-case pseudo-outcome enumeration with explicit propensity propagation (O(|C|) per unit). **Track B (ATE intervals)** extends conformal prediction-powered inference (Csillag et al. 2025, arXiv 2510.16166) to the causal setting, where a small expert-labeled and large LLM-imputed dataset yield valid confidence intervals via Z-estimation with conformal set-predictors.

A distinctive practical contribution is **principled abstention**: when conformal sets are large (|C|/K ≥ 0.6), intervals become vacuously wide, automatically detecting that LLM extraction quality is insufficient for credible causal conclusions. This constitutes a built-in LLM reliability assessment protocol for downstream causal analysis. We provide an operational decision rule: run conformal calibration on a held-out set; if median |C|/K > threshold, report "extraction quality insufficient" and estimate the human annotation volume needed to bring |C|/K below threshold.

**Differentiation from closest related work:**

(a) Classical measurement error correction (SIMEX, Cook & Stefanski 1994; regression calibration, Carroll et al. 2006) requires parametric assumptions — additive noise, independence from true values, Gaussian distribution — all violated by LLM extraction noise, which is categorical, context-dependent, and heterogeneous across subpopulations. We demonstrate this empirically: SIMEX coverage collapses under heterogeneous LLM noise.

(b) Kluger et al. (arXiv 2501.18577, 2025) address PPI with imputed covariates via Predict-Then-Debias (PTD) Bootstrap — point imputation with asymptotic bootstrap CI. Our conformal set-predictor provides distribution-free finite-sample validity rather than asymptotic guarantees. We include PTD Bootstrap as a head-to-head experimental baseline to empirically demonstrate where conformal PPI improves over PTD, particularly in heterogeneous noise and small-sample regimes.

(c) The "No Free Lunch" result (Mani et al. arXiv 2505.20178, 2025) proves PPI++ can underperform gold-standard-only estimation when pseudo-label correlation is low. Our conformal set-predictor (Csillag et al. 2025) differs: validity holds regardless of LLM quality (wider intervals, not invalid intervals), but efficiency gain over labeled-only estimation requires conformal sets to be sufficiently tight. We empirically characterize the crossover: Track B improves over labeled-only estimation when median |C|/K ≤ 0.4.

(d) Barnatchez et al. (arXiv 2604.03772, 2026) handle confounders entirely MISSING at deployment via semiparametric debiasing — distinct from our noisy-extraction setting. Vovk & Wang (arXiv 2603.11134, 2026) extend conformal e-prediction under confounding for prediction, not treatment effects.

(e) DoubleLingo (NAACL 2024) and Ma et al. (NeurIPS 2025) use LLMs within DR causal estimators for text data but provide only asymptotic guarantees with no finite-sample uncertainty quantification for LLM extraction noise.

Cross-conformal calibration (Gasparin & Ramdas, ICML 2025, arXiv 2503.01495) reduces the three-way data split to two-way, improving sample efficiency. A secondary exploratory track uses Matryoshka embeddings (128–256d) with ellipsoidal conformal sets (Xu et al. ICML 2024; Lützow et al. arXiv 2605.12341, 2026) and convex relaxation restricted to smooth nuisance estimators (Wang & Dobriban, arXiv 2602.00989, 2026); this requires a feasibility pilot before committing.

While the framework is theoretically domain-agnostic (applicable wherever ML models extract features for downstream causal inference), we focus on LLM-extracted text confounders as the primary instantiation.

**Exchangeability conditions.** Stage 1 conformal calibration requires (approximate) exchangeability between calibration and test examples. This holds when texts are i.i.d. from the same distribution. When systematic distributional shift exists (e.g., different hospital systems, temporal drift in clinical language), we invoke weighted exchangeability (Barber et al. Annals of Statistics 2023) with likelihood ratio weights estimated from observable text features. Coverage degrades gracefully as a function of weight variability, which we empirically characterize.

## Core Problem

Causal inference from observational text data (clinical notes, social media, policy documents) requires adjusting for confounders embedded in unstructured text. LLMs can extract these confounders, but extraction is imperfect. No existing framework provides finite-sample coverage guarantees for treatment effects when confounders are extracted by a fallible LLM.

The problem is distinct from classical measurement error: (1) LLM extraction noise is heterogeneous and context-dependent (confusion rates between "critical" and "severe" depend on text content), violating the additive-noise-independent-of-truth assumptions of SIMEX (Cook & Stefanski 1994) and regression calibration (Carroll et al. 2006); (2) LLM extraction produces categorical or embedding-space outputs, not continuous measurements. Conformal prediction provides a distribution-free, finite-sample alternative.

## Opportunity

Three research threads can now be unified: (1) modular conformal prediction for sequential pipelines (Zhang et al. 2025, arXiv 2510.04406); (2) conformal PPI (Csillag et al. 2025, arXiv 2510.16166) for valid inference with ML-imputed covariates; (3) conformal meta-learners for ITE (Alaa et al. NeurIPS 2023) assuming error-free confounders. The critical missing piece is understanding how extraction uncertainty propagates through the DR estimator's propensity component — the 1/ê(c) amplification creates a previously uncharacterized (in finite-sample, distribution-free terms) interaction between extraction and estimation stages. Matryoshka embedding models (Qwen3-Embedding-8B) make conformal prediction over embedding spaces potentially tractable. Growing interest in conformal + causal (Barnatchez et al. arXiv 2604.03772; Vovk & Wang arXiv 2603.11134; Systematic Review arXiv 2509.21660) confirms timeliness.

## Landscape

Conformal ITE methods (Lei & Candès JRSS-B 2021; Alaa et al. NeurIPS 2023; wTCP-DR KDD 2024) assume error-free confounders. The conformal NLP survey (Campos et al. TACL 2024) covers classification/QA/generation but not causal validity. PPI causal extensions (arXiv 2502.06343; Kato arXiv 2511.08303, NeurIPS 2025) do not incorporate conformal sets for imputed covariates. Zhang et al. (2025) handle sequential pipelines but not causal settings or weighted exchangeability. PPI (Angelopoulos et al. Science 2023) and its extensions address labeled/unlabeled splits but not conformal set propagation. Multi-variable conformal prediction (Lützow et al. arXiv 2605.12341, 2026) and ellipsoidal sets (Xu et al. ICML 2024) provide geometric tools for moderate-dimensional conformal regions. Recent work on LLM extraction calibration (Shrestha & Kim, arXiv 2603.00924, 2026) shows domain/category-dependent miscalibration, motivating careful nonconformity score design in Stage 1.

## Approach

**Data Splitting.** Baseline three-way split: (S1) training, (S2) Stage 1 calibration, (S3) Stage 2 calibration. Improvements: K-fold cross-fitting within S1 (Chernozhukov et al. 2018 DML); cross-conformal Stage 1 (Gasparin & Ramdas, ICML 2025, arXiv 2503.01495) merging S2 into S1 (coverage ≥ 1−2α₁). Requirements: n₃ ≥ 150, n_total ≥ 500. For n < 300, Track B preferred.

**Track A — Modular Conformal ITE Intervals (Primary).** Adapts Zhang et al. (2025) residual decomposition R ≤ ΔR₁ + R₂. Stage 1: LLM extracts categorical confounders via prompted classification. Nonconformity score: APS (Romano, Sesia & Candès, NeurIPS 2020) as default, with ablation against RAPS and naïve softmax (THR). Stage 2: worst-case pseudo-outcome enumeration.

For each c ∈ C(x): φ̂(c; Yᵢ, Aᵢ) = [μ̂₁(c) − μ̂₀(c)] + Aᵢ·(Yᵢ − μ̂₁(c))/ê(c) − (1−Aᵢ)·(Yᵢ − μ̂₀(c))/(1−ê(c))

The propensity variation Δ(1/ê) across the conformal set is the dominant widening driver. Propensity trimming (ê(c) clipped to [τ, 1−τ], default τ=0.05) bounds amplification; we ablate τ ∈ {0.01, 0.05, 0.10}. The modular FWER control yields provably tighter intervals than naive Bonferroni.

**Pilot Conservatism Analysis.** K=5 severity categories:

| Category | μ̂₁(c) | μ̂₀(c) | ê(c) | CATE |
|----------|--------|--------|-------|------|
| none     | 0.40   | 0.30   | 0.50  | 0.10 |
| mild     | 0.50   | 0.35   | 0.45  | 0.15 |
| moderate | 0.60   | 0.40   | 0.40  | 0.20 |
| severe   | 0.72   | 0.45   | 0.35  | 0.27 |
| critical | 0.85   | 0.50   | 0.25  | 0.35 |

Widening: |C|=1 → 0%; |C|=2 → ~60%; |C|=3 → ~100%; |C|≥4 → vacuously wide (principled abstention). Method is practically useful when |C| ≤ 2 for K=5.

**Continuous Embedding Track (Exploratory).** Qwen3-Embedding-8B with Matryoshka 128–256d, ellipsoidal conformal sets, convex relaxation (Lipschitz + Taylor) restricted to smooth nuisance estimators. Requires feasibility pilot; if intervals >5× oracle, reported as preliminary/future work.

**Track B — Conformal PPI for ATE Intervals.** Applies conformal PPI (Csillag et al. 2025, arXiv 2510.16166) to ATE estimation via Z-estimation with conformal set-predictors: E[inf φ(C(X))] − M·Err(C) ≤ ATE ≤ E[sup φ(C(X))] + M·Err(C). Extends PPI causal inference (arXiv 2502.06343). Efficiency gain over labeled-only requires median |C|/K ≤ 0.4.

**Experimental Design.**

*Baselines (six layers):*
- Layer 0 (Oracle): Ground-truth confounders → DR estimator + conformal ITE (Alaa et al. NeurIPS 2023)
- Layer 1 (Naive plug-in): LLM point prediction as ground truth → DR + BCa bootstrap CI
- Layer 1.5 (Classical ME correction): SIMEX (Cook & Stefanski 1994) applied to LLM point predictions → DR estimator
- Layer 2 (Asymptotic): DoubleLingo (NAACL 2024) / Ma et al. (NeurIPS 2025) asymptotic CI
- Layer 2.5 (PTD Bootstrap): Kluger et al. (arXiv 2501.18577) Predict-Then-Debias Bootstrap (for Track B comparison)
- Layer 3 (Proposed): ConformalPPITextCausal Track A / Track B

*Benchmarks:*

(1) Semi-synthetic MIMIC-IV clinical notes (MIMIC-IV-Note v2.2; MIMIC-III NOTEEVENTS backup): treatment = escalation to aggressive therapy; confounder = disease severity from discharge summaries. MIMIC structured fields (ICD codes, lab values) as proxy ground-truth confounders. DGP: p(A=1|C) = σ(β₀ + β₁·severity_score); Y(a) = f(C, a) + ε with heterogeneous CATE. LLM noise: (a) real extraction (GPT-4/Claude/Llama), (b) controlled noise injection (misclassification rate 5%–40%). Fixed text + resampled (A, Y) following Veitch et al. (UAI 2020).

(2) Semi-synthetic social media (Veitch et al. UAI 2020 paradigm): content moderation effect on engagement, toxicity as confounder.

(3) Fully synthetic (3 scenarios, 200+ seeds each):
- Scenario 1 (Benign): moderate overlap ê(c) ∈ [0.25, 0.75], 5% misclassification
- Scenario 2 (Challenging propensity): poor overlap ê(c) ∈ [0.1, 0.9]
- Scenario 3 (Heterogeneous noise): extraction error 2%–30% by subgroup

*Evaluation:*
- Empirical coverage at 90%/95% with binomial exact CI (Clopper-Pearson) and one-sided test H₀: coverage < 1−α
- Interval width relative to oracle/baselines; widening ratio W vs. |C|/K
- Conditional coverage stratified by: |C| (1/2/3+), propensity quintile, treatment group
- Calibration plots: α swept 0.01–0.20 with ±2σ binomial band
- Computational cost table (per-sample time)
- LLM extraction quality table: per-LLM accuracy, F1, confusion matrix, empirical |C| distribution at α₁=0.05/0.10

*Ablations:*
- Stage-wise uncertainty attribution (Stage 1 Δφ vs. Stage 2 conformal quantile decomposition)
- Track A vs. Track B on ATE under identical settings
- n_labeled sensitivity for Track B (50–500+) with labeled-only crossover analysis
- |C|/K sweep 0.2–0.8
- Nonconformity score: APS vs. RAPS vs. THR
- Propensity trimming threshold: τ ∈ {0.01, 0.05, 0.10}
- Cross-conformal vs. split (sample efficiency cost)

*Honest framing:* Finite-sample advantage is most pronounced at n < 1000 with heterogeneous noise. At large samples with uniform noise, asymptotic methods may perform comparably.

## Resource Estimate

GPU hours: 200–300 (A100), ~$300–450. Timeline: 10 weeks. Weeks 1–3: Theory (modular decomposition under weighted exchangeability, amplification characterization, conformal PPI ATE). Weeks 4–5: Implement categorical pipeline + PPI track + baseline suite (PTD Bootstrap, SIMEX). Week 6: Continuous track feasibility pilot. Weeks 7–8: Core experiments. Week 9: Ablations + conditional coverage. Week 10: Writing. Annotation: ~20h (guideline verification + spot check using MIMIC structured fields as proxy ground truth). PhysioNet credentialing: apply immediately; MIMIC-III backup. Claude API (human-in-loop): $100–150.

## Inspired By

Gap: Existing conformal causal methods assume error-free confounders; text-based causal methods provide only asymptotic guarantees; classical measurement error correction requires parametric assumptions; Kluger et al. use asymptotic debiasing only; IPW amplification of measurement error is known asymptotically but lacks finite-sample conformal characterization. Pattern: Three converging literatures (modular CP, conformal PPI, conformal causal inference) unified by the insight that propensity score amplification governs the extraction-estimation interaction. Key enablers: Zhang et al. (arXiv 2510.04406); Csillag et al. (arXiv 2510.16166); Alaa et al. (NeurIPS 2023); Barber et al. (Annals of Statistics 2023).

## Target Venues

- AAAI 2027 (Primary — abstract July 21, full paper July 28, 2026)
- ARR August 2026 cycle (Secondary — submission August 3, 2026) → EACL 2027
- AISTATS 2027 (Stretch — estimated deadline ~October 2026)

## Key References

- Zhang et al. 'Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition' (arXiv 2510.04406, 2025)
- Csillag et al. 'Extending Prediction-Powered Inference through Conformal Prediction' (arXiv 2510.16166, 2025)
- Angelopoulos et al. 'Prediction-Powered Inference' (Science, 2023)
- Prediction-Powered Causal Inferences (arXiv 2502.06343, 2025)
- Kato 'Semi-Supervised Treatment Effect Estimation via Generalized Riesz Regression' (arXiv 2511.08303, NeurIPS 2025)
- Barber et al. 'Conformal prediction beyond exchangeability' (Annals of Statistics, 2023)
- Alaa et al. 'Conformal Meta-learners for Predictive Inference of Individual Treatment Effects' (NeurIPS 2023)
- Wang & Dobriban 'Optimal Decision-Making Based on Prediction Sets' (arXiv 2602.00989, 2026)
- Lützow et al. 'Multi-Variable Conformal Prediction without Data Splitting' (arXiv 2605.12341, 2026)
- Xu et al. 'Conformal prediction for multi-dimensional time series by ellipsoidal sets' (ICML 2024)
- Campos et al. 'Conformal Prediction for Natural Language Processing: A Survey' (TACL, 2024)
- Systematic Review of Conformal Inference for Treatment Effect Estimation (arXiv 2509.21660, 2025)
- Lei & Candès 'Conformal Inference of Counterfactuals and Individual Treatment Effects' (JRSS-B, 2021)
- DoubleLingo: Causal Estimation with Large Language Models (NAACL 2024)
- Ma et al. 'LLM-Driven Treatment Effect Estimation Under Inference Time Text Confounding' (NeurIPS 2025)
- Conformal Counterfactual Inference under Hidden Confounding (KDD 2024)
- Veitch et al. 'Adapting Text Embeddings for Causal Inference' (UAI 2020)
- Barnatchez et al. 'Debiased ML for Conformal Prediction under Runtime Confounding' (arXiv 2604.03772, 2026)
- Vovk & Wang 'Conformal e-prediction in the presence of confounding' (arXiv 2603.11134, 2026)
- Gasparin & Ramdas 'Improving cross-conformal prediction' (arXiv 2503.01495, ICML 2025)
- Chernozhukov et al. 'Double/debiased machine learning' (Econometrics Journal, 2018)
- Kluger et al. 'PPI with Imputed Covariates and Nonuniform Sampling' (arXiv 2501.18577, 2025)
- Mani et al. 'No Free Lunch: Non-Asymptotic Analysis of PPI' (arXiv 2505.20178, 2025)
- Carroll et al. 'Measurement Error in Nonlinear Models' (2nd ed., Chapman & Hall, 2006)
- Cook & Stefanski 'Simulation-Extrapolation Estimation in Parametric Measurement Error Models' (JASA, 1994)
- Romano, Sesia & Candès 'Classification with Valid and Adaptive Coverage' (NeurIPS 2020)
- Shrestha & Kim 'Conformal Prediction for Risk-Controlled Medical Entity Extraction' (arXiv 2603.00924, 2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e7f036a7-ef93-4a47-99ea-76846499b33f",
  "type": "user",
  "uuid": "70509faf-6c25-489f-b45b-2ac4328d6b94",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:31:15.609Z_

```json
{
  "parentUuid": "70509faf-6c25-489f-b45b-2ac4328d6b94",
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
  "uuid": "55b5bc7e-7f89-4e07-a738-1d76402921a2",
  "timestamp": "2026-05-20T04:31:15.609Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:31:15.609Z_

```json
{
  "parentUuid": "55b5bc7e-7f89-4e07-a738-1d76402921a2",
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
  "uuid": "0fb23f8b-aa79-443f-8f80-d499301be48c",
  "timestamp": "2026-05-20T04:31:15.609Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T04:31:15.609Z_

```json
{
  "parentUuid": "0fb23f8b-aa79-443f-8f80-d499301be48c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cb84845f-6513-47ac-9476-3baf84d3fdbb",
  "timestamp": "2026-05-20T04:31:15.609Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient context from the field research. Let me…",
  "leafUuid": "cb84845f-6513-47ac-9476-3baf84d3fdbb",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal causal inference with LLM-extracted text confounders",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3"
}
```

---

### Assistant

_source line 9 · 2026-05-20T04:31:49.405Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments systematically to produce the Meta Judge output.

**Extracting key data:**

Reviewer 1: [22% - 38%] 中位 30%
Reviewer 2: [28% - 42%] 中位 35%
Reviewer 3: [25% - 38%] 中位 30%

Three medians: 30%, 35%, 30%
Mean of medians: 31.67%
Median of medians: 30%
Std of medians: sqrt(((30-31.67)^2 + (35-31.67)^2 + (30-31.67)^2)/3) = sqrt((2.79 + 11.09 + 2.79)/3) = sqrt(5.56) ≈ 2.36%


The standard deviation is under 3%, indicating strong agreement among the reviewers. Now I'm checking the rubric dimensions across all three assessments to identify where consensus exists. The research problem, experimental design, and method innovation dimensions show consistent ratings, with the research problem and experimental design both rated as strong across all three reviewers, while methods and innovation are rated as medium across the board.

For feasibility, there's near-consensus with two reviewers rating it medium and one slightly higher. Writing quality shows the most variation, with one reviewer rating it strong while the other two rate it medium. Looking at the broader consensus points, all three reviewers agree on several key observations: the research problem is strong and timely, the method represents incremental or combinatorial innovation, the experimental design is the strongest component, the practical utility window is narrow, and the project scope is too broad across multiple tracks.

There's also unanimous agreement on the core theory contribution carrying conjecture-status risk, Kluger et al.'s PTD Bootstrap being the key competitive baseline, a tight 10-week timeline, and MIMIC PhysioNet credentialing presenting a timeline bottleneck. Two reviewers flagged potential expertise mismatch with EMNLP reviewers. The outliers are R2's more optimistic writing assessment and slightly higher success probability estimate compared to the other two reviewers, plus R3's noted tension between finite-sample advantages at smaller sample sizes and confidence interval coverage.

All three reviewers identify the same two critical risks: novelty appearing combinatorial or incremental, and practical utility being too narrow. They also converge on implementation details—200-300 A100 GPU hours costing $300-450, using MIMIC-IV plus social media and synthetic data, requiring about 20 hours of annotation, no large-scale model training, and a 10-week timeline that's quite constrained.

The standard deviation across estimates is roughly 2.36%, which is well below the 3% threshold, indicating strong consistency. The individual medians are 30%, 35%, and 30%, giving an overall median of 30%. Given this high consistency, I should anchor to the median vicinity and narrow the confidence interval accordingly. Though I should also weigh the most optimistic assessment from R2 before finalizing.

Looking at the three ranges—R1 at [22-38], R2 at [28-42], and R3 at [25-38]—the intersection is [28-38] and the union is [22-42]. With high consistency supporting a tighter interval around the median, I'm settling on [25%-37%] with a median of 30%, since all three reviewers fundamentally agree on the work's character: solid execution with a genuine gap, but ultimately incremental innovation with a narrow window of practical applicability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb84845f-6513-47ac-9476-3baf84d3fdbb",
  "isSidechain": false,
  "requestId": "req_011CbDCBBQR6Yu2EzrZfFf1f",
  "type": "assistant",
  "uuid": "ea6dd024-6ba1-4fb9-b3c7-fac45d8d02f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALK6pTSFtMaDsVHQ3yqfjf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19901,
      "cache_read_input_tokens": 16514,
      "output_tokens": 3165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3165,
          "cache_read_input_tokens": 16514,
          "cache_creation_input_tokens": 19901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19901
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

_source line 10 · 2026-05-20T04:32:34.188Z_

【阶段】: Meta Judge
【三次中位】: [30%, 35%, 30%]  std=2.4%
【共识维度】:
- **研究问题 = 强**（3/3 一致）：三位审稿人均确认 conformal CP × causal inference × LLM extraction 的三重交叉是真实、重要、有时效性的 gap，被 systematic review (arXiv 2509.21660) 和近期工作（Barnatchez et al. 2026; Vovk & Wang 2026）佐证。
- **方法与创新 = 中**（3/3 一致）：三位审稿人均判定核心贡献为"组合性增量"——将 Zhang et al. (2510.04406) 的 modular CP 和 Csillag et al. (2510.16166) 的 conformal PPI 适配到因果设定。IPW amplification 的 conformal 刻画虽然是新的形式化，但基于已知现象（Babanezhad et al. 2010），属 incremental 而非 breakthrough。
- **实验设计 = 强**（3/3 一致）：六层 baseline、三类 benchmark、系统化 ablation、honest framing 均被三位审稿人高度认可，认为是 proposal 最突出的亮点。
- **实用性窗口过窄**（3/3 一致）：pilot analysis 显示 |C|≤2（K=5）才实用，三位审稿人均将此识别为核心风险，质疑"LLM 已经足够好时是否还需要这个复杂框架"。
- **Scope 过大**（3/3 一致）：Track A + Track B + exploratory embedding track 在一篇 8 页论文中难以充分展开，存在"散而不精"风险。
- **可行性 = 中**（2/3 中，1/3 中偏强）：10 周时间线紧张、PhysioNet credentialing 风险、理论证明难度可能被低估。
- **理论 conjecture 未严格证明**（2/3 明确提及——R2、R3）：worst-case pseudo-outcomes 出现在 propensity-extreme 处目前是 conjecture 状态，若无法严格证明将显著削弱理论贡献。

【异常维度】:
- **写作与呈现**：R2 评"强"，R1/R3 评"中"。R2 更关注 proposal 本身的逻辑与结构，R1/R3 更关注最终论文的呈现挑战（信息密度、8 页篇幅限制）。鉴于后者是实际投稿面临的问题，按多数判定为"中"，R2 的"强"降权。
- **finite-sample vs. calibration data 的内在张力**：仅 R3 提出"有限样本优势在 n<1000 时最显著，但 conformal calibration 在小样本时数据最不充裕"——这是一个有洞察力的观察，但属于技术层面的 nuance 而非方向性判断，不影响整体概率估计。

【最终概率】: [25% - 37%] 中位 30%
【一致性】: 高（std=2.4% < 3%）
【综合理由】:
三位审稿人在所有核心维度上高度一致：研究问题真实且及时（强），实验设计极其完备（强），但方法创新为组合性增量（中），实用窗口窄（|C|≤2），scope 过大。三个中位数（30%, 35%, 30%）std 仅 2.4%，属高一致性，按规则取中位附近并缩窄区间。R2 的 35% 略高于 R1/R3 的 30%，但 R2 在写作维度评"强"已被降权，且其推理逻辑与另两位并无本质分歧，仅在"solid work"的定义阈值上略宽松。最终中位取 30%，区间缩窄至 [25%-37%]。

30% 的判断反映：这是一篇方向正确、执行规划极其充分、但核心创新度不足以明确跨过顶会门槛的投稿。决定性因素有二：(1) 实验结果能否展示 conformal 方法在目标场景下的显著优势（尤其 vs. Kluger et al. PTD Bootstrap），这决定能否触及上界；(2) conjecture 能否严格证明，这决定理论贡献是否被承认。两项均属执行层面的不确定性，概率区间已反映。

【建议】: 边缘（中位 30% 低于 36% 通过线，但距离不远；idea 层面的天花板受限于组合性创新，需要在 novelty framing 或理论深度上有实质突破才能进入可推荐区间）
【实施评估】:
  - 计算资源: 200–300 A100 GPU hours（~$300–450），三位审稿人一致认为合理且无瓶颈
  - 数据需求: MIMIC-IV-Note v2.2（需 PhysioNet credentialing，有 MIMIC-III backup）+ Veitch et al. 社交媒体数据（公开可用）+ 全合成数据（无障碍）
  - 人工介入: ~20h 标注验证（使用 MIMIC 结构化字段作为 proxy ground truth），工作量极小
  - 训练需求: 无需训练大模型；需训练轻量级 nuisance estimators（propensity score + outcome models）；LLM 推断（GPT-4/Claude/Llama extraction）是主要计算成本
  - 新 Benchmark: 需构建 3 类 semi-synthetic/synthetic benchmark 的 DGP pipeline，基于已有数据范式（Veitch et al. 2020），非从零开始
  - 预估周期: 10 周（理论 3 周 + 实现 3 周 + 实验 3 周 + 写作 1 周）。核心 Track A+B 可行；embedding exploratory track 大概率需降级为 future work。PhysioNet credentialing 是时间线最大风险点。三位审稿人均认为"紧张但可行"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea6dd024-6ba1-4fb9-b3c7-fac45d8d02f7",
  "isSidechain": false,
  "requestId": "req_011CbDCBBQR6Yu2EzrZfFf1f",
  "type": "assistant",
  "uuid": "be6f9339-36cf-4146-b3b4-05f8fc5f8423",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALK6pTSFtMaDsVHQ3yqfjf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19901,
      "cache_read_input_tokens": 16514,
      "output_tokens": 3165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3165,
          "cache_read_input_tokens": 16514,
          "cache_creation_input_tokens": 19901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19901
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient context from the field research. Let me…",
  "leafUuid": "be6f9339-36cf-4146-b3b4-05f8fc5f8423",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal causal inference with LLM-extracted text confounders",
  "sessionId": "98160e49-8e4d-448d-8928-ded4e23f03a3"
}
```

---
