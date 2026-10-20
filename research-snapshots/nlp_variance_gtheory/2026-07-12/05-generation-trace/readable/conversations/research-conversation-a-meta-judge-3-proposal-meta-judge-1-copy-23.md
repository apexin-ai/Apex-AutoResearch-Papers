# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/1aa66f20-d684-443a-bb5e-8ecc8081ddae.jsonl`
- **Structured JSON:** [`a0e28ac5f97d7f8c2d39.json`](../../sessions/a0/a0e28ac5f97d7f8c2d39.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:44:15.575Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:44:15.575Z",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- \"Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking\" (ICLR 2025): 在 152,380 数据点上证明 LLM judges 系统性地优先考虑 style 而非 factuality 和 safety。提出 SOS-Bench 但未提供修复方案。本 proposal 的核心动机之一，确认真实存在。\n- \"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge\" (arXiv 2602.06625, Feb 2026): 通过 SFT→DPO→GRPO 训练去偏 judge（Qwen3-VL 2B/4B/8B），在 PandaLM 达到 76.83% agreement。是最直接的竞争者，但需要模型再训练，无法应用于黑盒商业 API。Proposal 的定位准确。\n- \"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies\" (arXiv 2604.23178, Soumik, April 2026): 跨 5 个 judge 模型测试 9 种去偏策略，确认 style bias 主导 (0.76–0.92)，position bias 极小 (≤0.04)。是 proposal 引用的关键证据，确认真实存在且描述准确。\n- \"RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals\" (ICML 2025, Reber et al.): 提出 double-rewrite 协议修正不完美反事实带来的偏差，用于 reward model 可解释性。是本 proposal 的核心方法论前驱，但原文目标是 reward model explainability，不是 judge debiasing。确认真实存在。\n- \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\" (ICLR 2025, Dubois et al.): 仅控制 length 一个维度的回归去偏，将与 Chatbot Arena 的相关性从 0.94 提升到 0.98。**是最重要的 trivial alternative 威胁**——简单回归方法在单维度上已极其有效。\n- \"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation\" (arXiv 2603.05485, March 2026): DP 启发的高斯噪声注入，保留 61-99% ranking correlation。非因果方法，proposal 正确区分。\n- \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features\" (CASSE, arXiv 2601.10809, Jan 2026): 证明 style features 深度纠缠（如简洁降低感知专业度），支持 proposal 的 legitimacy-aware correction 设计动机。确认真实存在。\n- \"Causal Effect Estimation with Latent Textual Treatments\" (arXiv 2602.15730, Feb 2026, Feldman et al.): 提出基于 SAE 的潜在文本因果效应估计，使用 covariate residualization 解决偏差问题。方法论上相关但未应用于 judge debiasing。确认真实存在。\n- \"Doubly-Robust LLM-as-a-Judge: Externally Valid Estimation with Imperfect Personas\" (arXiv 2509.22957): 使用 doubly-robust 框架结合 persona ratings 和 human ratings。名称相近但解决的是外部有效性问题，非 style debiasing。\n- 调研总结: LLM judge style bias 已被充分记录为主导偏差（远超 position bias），但现有修复方案要么需要模型再训练（FairJudge）、要么仅控制单一维度（LC-AlpacaEval）、要么是非因果方法（BBE）。将因果反事实估计应用于黑盒 judge 多维 style debiasing 的空白确实存在，proposal 的定位准确。截至调研时点，未发现与本 proposal 完全重叠的已发表工作。\n\n【Trivial Alternative 检验】:\n最大的 trivial alternative 威胁来自 **多维回归去偏**——即直接将 LC-AlpacaEval 的回归方法扩展到多个 style 维度。具体而言：(1) 用现成分类器测量 formality score、word count、markdown element count 等 style 特征；(2) 拟合多元回归模型控制这些特征。LC-AlpacaEval 仅用 length 回归就已将与 Arena 的 Spearman 相关性从 0.94 提升到 0.98，这是一个极高的基线。\n\nProposal 相对于此 trivial alternative 的增量价值在于：(a) 因果识别——回归方法只能控制可观测的 style 特征，而反事实方法可以捕获与 style axis 相关的所有效应（包括未被显式度量的）；(b) legitimacy-aware correction 的 domain-conditional α——区分 bias vs. legitimate style-quality correlation，这比简单回归更精细；(c) RATE 双重改写修正不完美反事实偏差。但这些增量价值是否能转化为实质性的实证改进（相比多维回归），是 proposal 最大的不确定性。如果经验上改进微小，审稿人会认为\"大量因果机制只换来边际收益\"。\n\n另一个更简单的 baseline 是 **format normalization**（剥离 markdown 后评分），proposal 已将其列为 baseline，这是合理的。\n\n【前提假设检验】:\n1. **三个二元轴足以捕获\"style bias\"的主要变异**: Proposal 选择 formality、verbosity、formatting 三个轴，但 style 是一个高维概念。Soumik (2026) 测试了多种 bias 类型，CASSE 列举了 12 种 style features。Tone、sentence complexity、hedging/confidence、vocabulary sophistication 等维度未被覆盖。如果这些未建模的维度贡献了大量 style bias，CSD 的去偏效果会被低估。**这一假设缺乏理论或实证支撑——没有现有工作证明这三个轴解释了 style bias 变异的主要部分。**\n\n2. **内容保持性假设**: 整个因果识别链条依赖于 style 反事实仅改变 style 而不改变 content。虽然 proposal 设计了多重验证（BERTScore ≥ 0.92, NLI ≥ 0.95, GPT-4o-mini 验证），但 CASSE 已证明 style features 深度纠缠——例如让回答变\"terse\"本质上会移除部分内容信息。BERTScore 和 NLI 可能无法完全检测到这种 subtle content leakage。如果 content preservation 不完美，因果估计就存在偏差，而此时 DML 的 doubly-robust 属性也无法修正（因为违反的是 treatment assignment 的清洁性，不是 nuisance model specification）。\n\n3. **RATE 假设的适用性**: RATE 的 Assumption 1（方向无关的改写噪声）要求正向改写和反向改写引入的噪声具有相同分布。在 style 轴上，这是否成立？例如，将 formal text 变为 casual 可能比将 casual text 变为 formal 更容易保持内容（因为 formal → casual 是\"放松约束\"，而 casual → formal 可能需要添加信息）。这一假设在 style 轴上是否成立是经验问题，proposal 未提供论证。\n\n4. **α 参数的可靠估计**: Legitimacy-aware correction 需要在 held-out validation set 上最大化 Spearman correlation with ground-truth quality 来确定 α。但 ground-truth quality 的获取本身就依赖于人工标注（或 objective benchmarks），而不同 benchmark 上的\"最优 α\"可能差异很大。Domain-conditional α 进一步增加了待估参数数量，可能导致过拟合。\n\n【3 维度打分】:\n1. Novelty: 中 — 核心贡献是将已有因果方法（RATE double-rewrite + DML partially linear model）组合应用于 LLM judge style debiasing 这一新设定。每个组件单独都是 well-established 的（RATE: ICML 2025; DML: Chernozhukov 2018; style transfer: 成熟技术），但这一特定组合和应用场景（黑盒 judge 多维 style 去偏 + legitimacy-aware correction）在调研中确未发现先例。与 LC-AlpacaEval (ICLR 2025) 的关键区别在于因果识别 + 多维度 + 区分 bias/legitimate correlation；与 FairJudge (2026) 的区别在于无需再训练。Novelty 是真实的但主要在\"组合+应用\"层面，而非方法论上的根本性创新。Legitimacy-aware correction (domain-conditional α) 是概念上最有新意的部分。**关键弱点：如果多维回归 baseline 就能达到类似效果，组合的因果机制的增量 novelty 会被大幅稀释。**\n\n2. Significance: 强 — Style bias 被多项独立研究（SOS-Bench ICLR 2025, Soumik 2026, CASSE 2026, Preference Leakage ICLR 2026）证实为 LLM judge 的主导偏差（0.76-0.92），远超被过度研究的 position bias（≤0.04）。黑盒 judge debiasing 具有高度实践价值——GPT-4o、Claude、Gemini 等商业 API 无法被再训练。如果 CSD 确实有效，它填补了一个被明确记录但未被解决的空白。问题本身的重要性不成疑问。唯一的 significance 折扣来自：如果 trivial alternative（多维回归）效果接近，则 CSD 的实际影响力有限。\n\n3. Related Work: 强 — Proposal 对领域现状的覆盖极为全面。调研中确认的所有关键论文（SOS-Bench, FairJudge, RATE, LC-AlpacaEval, BBE, CASSE, Soumik 2026, 潜在文本因果估计）均被引用且描述准确。对 ISE (Choi et al. NAACL 2024) 关于 positivity violation 批评的反驳（binary treatments vs. free-text treatments）是合理的。差异化定位清晰：相对于 FairJudge（需再训练）、LC-AlpacaEval（单维度）、BBE（非因果）的区分都准确。\"Doubly-Robust LLM-as-a-Judge\" (arXiv 2509.22957) 这篇名称相近但实际解决不同问题的论文未被提及，但它确实不直接竞争，不构成覆盖缺陷。\n\n【概率估计】: [28% - 40%] 中位 34%\n\n【估计理由】:\nSignificance 维度是最强项（强），supported by 多项独立研究确认的 real gap。Related Work 同样扎实（强），覆盖全面且定位准确。Novelty 是限制上界的关键维度（中）：方法论是已有组件的组合应用，核心创新集中在 legitimacy-aware correction 和应用场景定义上。这使得 proposal 处于\"idea 有实质内核、方向正确、有真实 novelty delta\"的区间（25-35%），但 legitimacy-aware correction 的设计和黑盒适用性提供了一定的 uplift（toward 35-40%）。\n\n上界主要受两个因素制约：(1) trivial alternative 威胁——多维回归去偏可能以 1/10 的成本达到 CSD 80-90% 的效果，这会严重削弱\"需要因果机制\"的 argument；(2) novelty 主要在组合层面，而非方法论创新，如果实证改进不显著，审稿人可能评价为\"principled but unnecessary complexity\"。\n\n下界由问题重要性和定位准确性支撑——即使实验结果一般，\"第一个将因果反事实方法系统性应用于黑盒 judge style debiasing\"的贡献仍有一定价值。\n\n【主要风险】:\n1. **Trivial alternative 威胁**: 多维回归（LC-AlpacaEval 的自然扩展）可能以极低成本达到类似去偏效果，使因果机制的复杂性显得不justified。如果实验中 CSD 与多维回归的差距小于 2-3 个百分点，审稿人会质疑整个 pipeline 的必要性。\n2. **三轴覆盖度不足 + 内容泄漏**: 仅选择三个 style 轴缺乏充分性论证，且 CASSE 已证明 style features 深度纠缠，意味着 style 反事实改写很可能同时改变了部分 content，违反因果识别的核心假设。这一风险不可通过后续实验设计完全消除——它是 idea 层面的固有脆弱性。\n```\n\nSources:\n- [Style Outweighs Substance (ICLR 2025)](https://arxiv.org/abs/2409.15268)\n- [FairJudge (arXiv 2602.06625)](https://arxiv.org/abs/2602.06625)\n- [RATE: Causal Explainability of Reward Models (ICML 2025)](https://arxiv.org/abs/2410.11348)\n- [Judging the Judges: Soumik (arXiv 2604.23178)](https://arxiv.org/abs/2604.23178)\n- [CASSE: Concise Agent is Less Expert (arXiv 2601.10809)](https://arxiv.org/abs/2601.10809)\n- [Length-Controlled AlpacaEval (ICLR 2025)](https://arxiv.org/abs/2404.04475)\n- [Bias-Bounded Evaluation (arXiv 2603.05485)](https://arxiv.org/abs/2603.05485)\n- [Causal Effect Estimation with Latent Textual Treatments (arXiv 2602.15730)](https://arxiv.org/abs/2602.15730)\n- [Doubly-Robust LLM-as-a-Judge (arXiv 2509.22957)](https://arxiv.org/abs/2509.22957)\n- [Toward Robust LLM-Based Judges (arXiv 2603.08091)](https://arxiv.org/html/2603.08091)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **SOS-Bench / \"Style Outweighs Substance\" (ICLR 2025, arXiv 2409.15268)**:\n   Proposal 的核心动机来源。该论文在 152,380 数据点上证明 LLM judges 将 style 优先于 factuality 和 safety，但**只诊断不治疗**——未提出任何 debiasing 方法。Proposal 对此的定位（\"documents but doesn't fix\"）准确。\n\n2. **FairJudge (arXiv 2602.06625, Feb 2026)**:\n   最直接的竞争者。通过 SFT→DPO→GRPO 训练流程在 Qwen3-VL 2B/4B/8B 上训练去偏 judge，取得 76.83%（PandaLM）和 78.82%（JudgeLM）agreement。**关键局限**：需要 retraining，无法对 GPT-4o/Claude 等黑盒 API 去偏。Proposal 的差异化定位（model-agnostic post-hoc）准确且成立。\n\n3. **RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025, arXiv 2410.11348)**:\n   Proposal 的核心方法论基础。RATE 用 double-rewrite 协议估计 reward model 对高层属性的因果效应，发表于 ICML 2025 (PMLR 267:51341-51368)。**Proposal 对 RATE 的使用是合理的**——RATE 面向 reward model explainability，CSD 将其扩展到 judge debiasing + DML 框架 + 多维同时估计。但这也构成了 \"application extension\" 的风险。\n\n4. **Length-Controlled AlpacaEval (ICLR 2025, arXiv 2404.04475)**:\n   最重要的 trivial alternative 威胁。通过 logistic regression 控制 length bias，将 AlpacaEval 与 Chatbot Arena 的 Spearman 相关从 0.93 提升到 0.98。**关键问题**：其方法仅控制单维度（length），但将其扩展到多维度（formality, verbosity, formatting）的 regression 并不需要因果反事实生成，是显而易见的 baseline。\n\n5. **Bias-Bounded Evaluation (arXiv 2603.05485, March 2026)**:\n   注入校准高斯噪声实现 differential-privacy-inspired 去偏，保留 61-99% ranking correlation。非因果方法，与 CSD 形成正交对比。Proposal 将其作为 baseline 是合理的。\n\n6. **Preference Leakage (ICLR 2026, arXiv 2502.01534)**:\n   研究 judge 与 generator 之间的 contamination bias，发现 judges 依赖 \"stylistic regularities—tone consistency, sentence cadence, punctuation density\"。这为 style bias 的存在提供了额外实证支持，但解决的是不同问题（contamination vs. style debiasing）。\n\n7. **CASSE (arXiv 2601.10809, Jan 2026)**:\n   发现 style features \"deeply entangled rather than orthogonal\"——prompting for conciseness significantly reduces perceived expertise。这为 Proposal 的 legitimacy-aware correction 设计提供了实证动机，引用合理。\n\n8. **Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2025)**:\n   生成 250,000+ 反事实写作样本来度量修辞风格。方法论上与 CSD 有相似之处（counterfactual style generation），但目标不同（度量 vs. 去偏）。Proposal 未引用此工作，是一个覆盖盲点。\n\n9. **Judging the Judges (arXiv 2604.23178, April 2026)**:\n   系统评估 9 种 debiasing 策略在 5 个 judges 上的效果，结论是现有策略 \"necessary but insufficient\"。这进一步证明了 style debiasing 的 gap 存在。\n\n10. **Causal Effect Estimation-guided Multi-Bias Elimination / CMBE (arXiv 2505.16522)**:\n    用因果效应估计指导多偏差消除，但面向 LLM 自身的社会偏见（如性别/种族），而非 judge 评分中的 style bias。方法论有交集但问题域不同。\n\n- **调研总结**: LLM-as-a-judge 的 style bias 已被 SOS-Bench 等大规模研究确认为最大系统性偏差（effect size 0.76-0.92），远超 position bias。现有 debiasing 方案要么需要 retraining（FairJudge）、只控制单一维度（LC AlpacaEval）、或非因果（Bias-Bounded Evaluation）。**对黑盒 judge 进行多维因果 style debiasing 的空白确实存在**，但这个空白是否需要完整的 counterfactual generation + DML 管道来填补，还是简单的多维 regression 就够了，是核心争议点。\n\n\n【Trivial Alternative 检验】:\n\n**存在一个成本显著更低的替代方案**：将 Length-Controlled AlpacaEval 的 regression 方法扩展到多维度。具体地，提取每个 response 的可观测 style 特征（word count、markdown 元素数量、formality classifier score、sentence length 等），然后在 judge score 上做多维回归控制。这不需要任何反事实生成（省去 6 rewrites/response 的计算开销）和额外的 judge 调用（省去 7x overhead），成本接近零。\n\n**CSD 的增量价值在于**：(1) 因果识别——regression on observables 受遗漏变量偏差影响，而反事实干预提供因果估计；(2) 反事实验证——可以直观地看到\"同一内容换了风格后分数如何变化\"；(3) DML 的 doubly-robust 性质提供更稳健的估计。\n\n**但这个增量价值是否实质性的**，取决于实证结果：如果简单 regression 已经能达到 CSD 90%+ 的去偏效果，那 7x 的额外开销就很难 justify。Proposal 确实将 LC AlpacaEval 作为 baseline，这是关键消融实验——但如果结果显示差距不大，整篇论文的 contribution 会被大幅削弱。这是一个 \"bet on empirical results\" 的 idea。\n\n\n【前提假设检验】:\n\n1. **\"三个 style 轴是独立的且足够覆盖 style bias\"**——这是未验证的假设。Proposal 声称 formality、verbosity、formatting \"genuinely independent\"，但 CASSE 恰好发现 style features 是 \"deeply entangled\"。此外，style bias 可能还包括 tone、confidence、hedging、example usage 等维度，三个轴能捕获多少 style bias variance 是未知的。如果三轴只解释了 40% 的 style bias，debiasing 效果上限就受限。\n\n2. **\"反事实生成能做到 content-preserving\"**——这是整个方法论的基石假设。虽然 Proposal 设置了多重验证（BERTScore ≥ 0.92, NLI ≥ 0.95, GPT-4o-mini 验证），但 style 和 content 在自然语言中高度纠缠（CASSE 的核心发现）。改变 formality 几乎不可避免地改变 perceived expertise（CASSE 实证结论）——这到底是 content change 还是 style change？BERTScore/NLI 是否能捕获这种细微差异？RATE 的 double-rewrite 能纠正多少 imperfect-counterfactual bias？这些都没有在 judge debiasing 场景下被验证过。\n\n3. **\"α 参数可以通过验证集优化来区分 legitimate 和 illegitimate style-quality correlation\"**——这假设存在可靠的 ground-truth quality annotation。但如果 ground truth 本身就受 style bias 影响（人类标注者也有 style bias），α 的校准就失去了锚点。Proposal 设计了 200 人 pilot study 分别标注 content quality 和 presentation quality，但 200 样本是否足够、人类是否能真正分离 content 和 presentation 判断，都是未经验证的。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — CSD 的核心贡献是将 RATE 的 double-rewrite 协议（ICML 2025）与 DML 的 partially linear model（Chernozhukov et al. 2018）组合，应用于 black-box judge debiasing 这个新场景。调研确认没有现有工作做过完全相同的组合（截至 2026 年 5 月无 arXiv 预印本覆盖此交叉点）。但这本质上是 **\"known method A + known method B → new application\"** 的组合创新，方法论层面没有新的理论贡献。Legitimacy-aware correction（α 参数）是一个有价值的设计，但技术上就是 regularization tuning，不构成重大创新。与 LC AlpacaEval (ICLR 2025) 的核心差异是\"因果反事实 vs. 观测回归\"——这个差异是否实质性取决于实验结果。整体属于 solid incremental novelty，不是 surprising insight。\n\n2. **Significance: 中偏强** — 研究问题毫无疑问是重要的。SOS-Bench (ICLR 2025) 定量证明 style bias 是 LLM judge 最大偏差（effect size 0.76-0.92），Judging the Judges (arXiv 2604.23178) 确认现有 debiasing 策略不充分。LLM-as-a-judge 已成为模型评估和对齐的核心基础设施，style bias 直接影响 RLHF/alignment 的可靠性。一个 model-agnostic 的解决方案（适用于 GPT-4o、Claude 等商业 API）有明确的实际需求。但影响力受限于：(a) 如果 simple regression baseline 效果接近，实际 adoption 不太可能选择 7x overhead 的 CSD；(b) 三个 style 轴的覆盖范围可能不足以 fully solve 问题。\n\n3. **Related Work: 强** — Proposal 的 related work 覆盖非常全面。所有关键竞争者（FairJudge、LC AlpacaEval、Bias-Bounded Evaluation、RATE、SOS-Bench、CASSE、Preference Leakage）均被引用且描述准确（经调研验证）。差异化定位清晰：vs. FairJudge（retraining vs. model-agnostic）、vs. LC AlpacaEval（single-dim vs. multi-dim causal）、vs. Bias-Bounded（noise injection vs. causal decomposition）。对 ISE 框架（Choi et al. NAACL 2024）关于 positivity violation 的反驳（binary treatment vs. free-text treatment）方法论上合理。唯一的小缺口是未引用\"Counterfactual LLM-based Framework for Measuring Rhetorical Style\"（arXiv 2025），该工作在方法论上有一定相似性（counterfactual style generation），但影响不大。\n\n\n【概率估计】: [28% - 38%] 中位 32%\n\n【估计理由】:\n- **Novelty (中)** 是上界的主要限制因素。核心贡献是 RATE + DML 的组合应用，审稿人可能会评价为 \"well-executed but not surprising\"。如果核心发现是 positive（CSD 有效去偏），审稿人的反应更可能是 \"makes sense, this is what I'd expect from applying causal inference tools to this problem\" 而非 \"surprising, I wouldn't have predicted this\"。\n- **Significance (中偏强)** 支撑了下界不低于 28%。问题确实重要，gap 确实存在，方案差异化明确。\n- **Related Work (强)** 确保论文不会因 related work 不足被拒，但也不会因此加分。\n- 概率未达 35%+ 区间的原因：trivial alternative（多维 regression）威胁是真实的——如果 LC AlpacaEval 扩展到多维度后效果接近 CSD，论文的 contribution 叙事会被严重削弱。这个风险使得 idea 的上限受限。\n\n【主要风险】:\n1. **Trivial alternative 风险**：多维 observational regression（LC AlpacaEval 的自然扩展）可能以接近零的额外成本达到 CSD 80-90% 的去偏效果，使得 7x overhead 的因果管道难以 justify。这是最可能被审稿人质疑的点——\"Why not just regress out multiple style features without counterfactuals?\"\n2. **Content-style 不可分性风险**：CASSE 的核心发现（style features are deeply entangled）实际上对 CSD 的前提假设构成双刃剑——它既证明了 legitimacy-aware correction 的必要性，也暗示了 content-preserving style counterfactual 可能本质上不存在。如果审稿人认为\"改变 formality 必然改变 perceived content quality\"，CSD 的因果识别策略就会受到根本性质疑。\n```\n\nSources:\n- [SOS-Bench: Style Outweighs Substance (ICLR 2025)](https://arxiv.org/abs/2409.15268)\n- [FairJudge (arXiv Feb 2026)](https://arxiv.org/abs/2602.06625)\n- [RATE: Causal Explainability of Reward Models (ICML 2025)](https://arxiv.org/abs/2410.11348)\n- [Length-Controlled AlpacaEval (ICLR 2025)](https://arxiv.org/abs/2404.04475)\n- [Bias-Bounded Evaluation (arXiv March 2026)](https://arxiv.org/abs/2603.05485)\n- [Preference Leakage (ICLR 2026)](https://arxiv.org/abs/2502.01534)\n- [CASSE: A Concise Agent is Less Expert (arXiv Jan 2026)](https://arxiv.org/abs/2601.10809)\n- [Judging the Judges (arXiv April 2026)](https://arxiv.org/abs/2604.23178)\n- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style)\n- [CMBE: Multi-Bias Elimination via Causal Effect Estimation](https://arxiv.org/abs/2505.16522)\n- [RBD: Reasoning-based Bias Detector (NeurIPS 2025)](https://openreview.net/forum?id=sLNz60fJFF)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough research context to make an informed assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- **SOS-Bench / \"Style Outweighs Substance\" (ICLR 2025, arXiv 2409.15268)**: 最大规模的 LLM judge 偏差元基准（152K 数据点），证实 style bias 在所有主流 judge 中占主导地位（sarcasm 导致 96% 偏好损失，而错误答案仅 13%）。该工作只诊断不治疗——没有提出任何 debiasing 方案。Proposal 正确识别了这个\"诊断无方案\"的空白。\n- **FairJudge (arXiv 2602.06625, Feb 2026)**: 最直接的竞争者。通过 SFT→DPO→GRPO 课程式训练（Qwen3-VL 2B/4B/8B backbone）构建去偏 judge，在 PandaLM 76.83%、JudgeLM 78.82% agreement。**核心局限**：需要重新训练 judge 模型，无法适用于 GPT-4o/Claude/Gemini 等黑盒 API。Proposal 的 model-agnostic 定位与之差异化合理。\n- **RATE (ICML 2025, arXiv 2410.11348)**: 本 proposal 最核心的方法论前身。使用 double-rewrite protocol 校正不完美反事实，估计 reward model 对高层属性的因果效应。**关键区别**：RATE 的目标是 reward model explainability，而非 judge debiasing。CSD 本质上是将 RATE 的 rewrite protocol 嫁接到 DML 框架并应用于 judge 去偏——这是一个 application pivot 而非方法论创新。\n- **Length-Controlled AlpacaEval (ICLR 2025, arXiv 2404.04475)**: 通过 logistic regression 控制 length 的 post-hoc debiasing 方案，将与 ChatBot Arena 的 Spearman 相关性从 0.93 提升到 0.98。**这是最重要的 trivial alternative 参照物**：该方法成本为零，单维度回归即取得巨大效果。Proposal 需要令人信服地证明多维因果分解（7x 成本开销）相对于\"多维回归控制\"的增量价值。\n- **Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2512.19908, Dec 2025)**: 使用 LLM 生成反事实风格重写 + Bradley-Terry 模型量化学术论文的修辞风格。在 8,485 篇 ICLR 投稿上生成 250K+ 反事实文本。该工作与 CSD 共享\"反事实风格重写\"的核心技术思路，但目标是 style measurement 而非 judge debiasing。\n- **Bias-Bounded Evaluation (arXiv 2603.05485, March 2026)**: 差分隐私启发的校准高斯噪声注入，在 Arena-Hard-Auto 上保留 61-99% 排名相关性。非因果方法，提供形式化偏差上界保证。\n- **Preference Leakage (ICLR 2026, arXiv 2502.01534)**: 发现 judge 与生成模型的\"亲缘关系\"导致评估偏差，属于 contamination bias 而非 style bias，与本 proposal 正交但同属 judge bias 生态。\n- **CASSE (arXiv 2601.10809, Jan 2026)**: 研究 12 种 style feature 的交互效应，核心发现 style features \"deeply entangled rather than orthogonal\"。这同时支持了 proposal 的 legitimacy-aware correction 设计，但也威胁了其\"三轴独立\"假设。\n- **Choi et al. ISE (NAACL 2024)**: 论证 ATE 在自由文本 treatment 上因 positivity violation 不可行。Proposal 通过限制 binary style intervention 来规避此批评，这个应对策略在方法论上是合理的。\n- **Judging the Judges / Soumik (arXiv 2604.23178, April 2026)**: 系统测试 9 种 debiasing 策略 × 5 种 judge，但聚焦 position/verbosity bias，没有系统性因果 style removal。\n- **调研总结**: Style bias in LLM judges 是一个已被充分诊断但 debiasing 方案稀缺的领域。现有方案要么需要训练（FairJudge），要么只控单维度（LC-AlpacaEval），要么非因果（BBE）。Post-hoc + model-agnostic + 多维因果的组合确实存在空白。但 RATE 的 double-rewrite + 反事实风格重写 的技术路线已在邻近工作中被探索，CSD 的核心创新更多在于\"组合与应用场景\"而非\"方法论突破\"。\n\n\n【Trivial Alternative 检验】:\n\n**存在两个严重的 trivial alternative 威胁：**\n\n1. **多维回归控制（Multi-dimensional LC-AlpacaEval 扩展）**: LC-AlpacaEval 仅用单维度 logistic regression 控制 length 就将相关性从 0.93→0.98，零额外推理成本。一个自然的扩展是：提取多个 surface features（token count、markdown 标记密度、平均句长、正式词占比等），用多维回归做 post-hoc 控制。这个方法：无需反事实生成（省去 7x 成本）、无需 DML 框架、无需 content preservation 验证。如果这个 trivial baseline 能达到 CSD 80%+ 的去偏效果，CSD 的增量价值将严重受损。Proposal 确实包含了 LC-AlpacaEval 作为 baseline，但仅作为\"单维度\"对比——真正的威胁是多维度扩展版，proposal 未直接面对这个问题。\n\n2. **Format normalization + 简单 prompt engineering**: Proposal 自己也列了 \"strip all markdown before judging\" 作为 baseline，加上 \"请忽略风格只关注内容\" 的 prompt，这组合的成本几乎为零。如果格式化是 style bias 的主要来源（markdown/列表视觉效果），这个 trivial 方法可能已覆盖大部分效应。\n\n**增量价值声称**：CSD 的增量价值需建立在以下论证上：(a) 多维回归无法捕捉 style 与 content 之间的非线性交互，而 DML 可以；(b) 因果估计提供了 per-response 的风格归因（而非群体平均），对个案审查有价值；(c) legitimacy-aware correction 需要因果框架才能区分 bias 与合法相关性。论证 (c) 最具说服力，但也最难验证。\n\n\n【前提假设检验】:\n\n**核心 claim 的逻辑链中，有以下关键未验证假设：**\n\n1. **\"三轴独立\"假设**：Proposal 声称 formality、verbosity、formatting \"genuinely independent\"，但 CASSE (Jan 2026) 的核心发现恰恰是 style features \"deeply entangled\"。例如：formal 文本通常更 verbose、更倾向使用 structured formatting。虽然 proposal 提到用 multivariate DML 处理残余相关，但反事实生成阶段仍假定可以独立翻转单个轴而不影响其他轴。如果 flip formality 的同时系统性地改变了 verbosity（因为 casual 文本天然更短），整个因果估计框架的有效性就受到威胁。\n\n2. **Content preservation under style rewriting**: BERTScore ≥ 0.92 和 NLI ≥ 0.95 是否足以保证\"内容等价\"？一篇高度技术性的 formal 文本被重写为 casual 版本时，术语精确度和推理严谨度可能系统性降低——这种降低不会被 BERTScore（表面语义相似度）或 NLI（单向蕴含）捕捉到。如果 content quality 在 style flip 过程中被系统性地改变，那估计的\"style effect\"实际上混杂了 content degradation effect。\n\n3. **RATE 的 Assumption 1 & 2 跨 judge 迁移**：RATE 的双重重写校正依赖两个假设——方向无关的重写噪声和加性分解。这些假设在 RATE 原论文中只在特定 reward model 上验证。不同的 LLM judge（GPT-4o vs. Claude vs. Llama）可能有非常不同的评分机制，假设的跨 judge 一致性缺乏理论支撑。\n\n4. **Style 效应线性可加性**：DML partially linear model 假定 score = β₁·formality + β₂·verbosity + β₃·formatting + g(content) + ε。但 style 效应很可能与 content domain 存在交互作用（coding 场景下 formatting 的效应远大于 creative writing 场景）。虽然 Stage 3 的 domain-conditional α 部分缓解了这个问题，但 Stage 2 的估计阶段仍假定全局线性可加性。\n\n5. **α 的可识别性**: legitimacy-aware correction 的 α 通过\"最大化与 ground-truth quality 的 Spearman 相关性\"来确定。但如果 ground-truth 本身有限（200-response pilot study），α 可能过拟合这个小样本。而且如果不同 benchmark 的最优 α 差异很大，\"legitimacy\"本身就成了一个 benchmark-dependent 的概念而非通用原则。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — CSD 的核心技术组件（反事实风格重写、double-rewrite 校正、DML partially linear model）均已在各自领域存在成熟先例。RATE (ICML 2025) 提供了 double-rewrite protocol，LC-AlpacaEval (ICLR 2025) 示范了 post-hoc regression debiasing，DML (Chernozhukov 2018) 是标准因果推断工具。Counterfactual LLM-based Framework (arXiv 2512.19908) 已经在使用反事实风格重写。CSD 的新颖性主要在于这些组件的**组合应用**——将 RATE 的 rewrite protocol 嫁接到 DML 框架、增加 legitimacy-aware correction、面向黑盒 judge debiasing。这是一个合理的 application novelty，但不是方法论突破。Legitimacy-aware correction (α parameter + domain-conditional analysis) 是最具原创性的贡献，但本质上是一个调参策略。如果核心结果是 \"CSD 比 raw judge 提高了 correlation\"，审稿人会说 \"I would have guessed this works\"。\n\n2. **Significance: 中偏强** — 问题本身非常重要。SOS-Bench (ICLR 2025) 以 152K 数据点证实 style bias 是 dominant bias，CASSE 进一步揭示 style 效应的 entanglement，Preference Leakage (ICLR 2026) 揭示 judge bias 的更多维度。LLM-as-a-judge 已成为 NLP 评估基础设施的核心组件，其去偏是一个有广泛影响力的实用问题。Model-agnostic 的 post-hoc 方案填补了 FairJudge（需训练）和 LC-AlpacaEval（单维度）之间的空白。然而，7x 推理成本开销限制了实际采用场景（大规模 leaderboard 可能不愿支付这个成本），amortized 版本虽降低成本但需要训练，与 \"no training needed\" 的主打优势有内在张力。\n\n3. **Related Work: 强** — 覆盖非常全面。FairJudge、RATE、LC-AlpacaEval、SOS-Bench、CASSE、BBE、Preference Leakage、ISE (Choi et al.)、DML、RBD、UDA、CyclicJudge 等均有讨论。对 ISE (NAACL 2024) 关于 positivity violation 的批评有直接回应（binary intervention 规避），与 LC-AlpacaEval 的差异化定位清晰。Landscape section 几乎覆盖了 2024-2026 的所有相关工作。唯一缺漏是 Counterfactual LLM-based Framework (arXiv 2512.19908) 虽在引用列表中但 landscape 段没有深入对比。\n\n\n【概率估计】: [23% - 33%] 中位 28%\n\n【估计理由】: \n- **Significance 是最强维度**（中偏强），问题重要且空白真实，这撑住了下界不至于太低。\n- **Novelty 是主要限制维度**（中），组合应用型创新在顶会审稿中通常被视为 incremental。审稿人会认出 RATE + DML 的组合，并质疑 \"what is the fundamental new insight beyond combining existing tools?\"。核心发现若 positive（\"去偏后 correlation 更高\"），审稿人不会感到 surprising。\n- **Trivial alternative 威胁真实**：多维回归控制（零成本）vs. CSD（7x 成本）的性价比对比，如果 CSD 不能在实验中碾压 trivial baseline，论文说服力大打折扣。这个风险拉低了上界。\n- 上界 33% 反映了\"如果 trivial baseline 被有效击败 + legitimacy-aware correction 展示出意想不到的效果\"的最佳情景。下界 23% 反映了\"novelty 被判 incremental + trivial baseline 表现相近\"的情景。\n\n【主要风险】: \n1. **Novelty 被判为 incremental（\"RATE + DML = CSD\"）**: 审稿人可能认为这是将两个已知工具组合应用到一个新场景，缺乏方法论深度。尤其当 RATE 已经做了 double-rewrite 因果效应估计、LC-AlpacaEval 已经做了 post-hoc regression debiasing 时，\"把它们合在一起做 multi-dimensional causal debiasing\" 的 novelty increment 可能不足以支撑一篇顶会论文。\n2. **Trivial alternative 表现出人意料地好**: 如果 \"多维 surface feature 回归 + format stripping\" 这个零成本方案已经能消除大部分 style bias，CSD 的 7x 推理成本开销就变得不可辩护。这是一个实验才能回答的问题，但它是 idea 层面的结构性风险——如果 trivial baseline 表现好，说明问题本身不需要因果框架来解决。\n```\n\nSources:\n- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)](https://arxiv.org/abs/2409.15268)\n- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625)](https://arxiv.org/abs/2602.06625)\n- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)](https://arxiv.org/abs/2410.11348)\n- [Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)](https://arxiv.org/abs/2404.04475)\n- [Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2512.19908)](https://arxiv.org/abs/2512.19908)\n- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2603.05485)](https://arxiv.org/abs/2603.05485)\n- [Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)](https://arxiv.org/abs/2502.01534)\n- [A Concise Agent is Less Expert: CASSE (arXiv 2601.10809)](https://arxiv.org/abs/2601.10809)\n- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies (arXiv 2604.23178)](https://arxiv.org/abs/2604.23178)\n- [Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation (arXiv 2603.08091)](https://arxiv.org/abs/2603.08091)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation\n\n## Description\nStyle bias is the dominant systematic bias in LLM-as-a-judge evaluations (effect size 0.76–0.92 across all major models), vastly exceeding position bias (≤0.04), yet no existing method causally isolates and removes style's contribution to black-box judge scores. FairJudge (Feb 2026) addresses style bias by retraining a dedicated judge, but cannot debias commercial APIs like GPT-4o or Claude. We introduce Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework that generates content-preserving binary style counterfactuals along three independent axes (formality, verbosity, formatting) using RATE's double-rewrite protocol, then estimates per-axis causal effects via a Double Machine Learning partially linear model (Chernozhukov et al. 2018) that preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects. A legitimacy-aware correction avoids over-debiasing by tuning a conservatism parameter α that distinguishes domain-invariant style bias from legitimate style-quality correlations. Unlike FairJudge (requires retraining), Length-Controlled AlpacaEval (single dimension), or Bias-Bounded Evaluation (non-causal noise injection), CSD provides a principled, multi-dimensional causal decomposition applicable to any black-box judge. We evaluate across five LLM judges on SOS-Bench (objective correctness), LLMBar adversarial (style resistance), RewardBench (domain-specific), and RubricBench (atomic rubric-based), supplemented by a 200-response pilot study with separate human annotations for content and presentation quality. An optional amortized deployment stage trains a lightweight predictor to estimate style effects without generating new counterfactuals, reducing marginal overhead to near-zero. CSD requires no judge retraining, applies to any black-box judge API, and reduces per-response debiasing cost from 25x (naive) to ~7x (full pipeline) or near-zero (amortized).\n\n## Core Problem\nHow can we isolate and remove the causal effect of surface-level style on LLM judge scores while preserving legitimate style-content associations, recovering a score that more faithfully reflects content quality?\n\n## Opportunity\nStyle bias is the dominant bias in LLM judges (effect size 0.76–0.92 across all models per Soumik 2026), vastly exceeding position bias (≤0.04), yet debiasing research overwhelmingly targets position bias. SOS-Bench (ICLR 2025) demonstrated that LLM judges prioritize style over factuality and safety across 152,380 data points. The 'Preference Leakage' paper (ICLR 2026) found judges rely heavily on 'stylistic regularities—tone consistency, sentence cadence, punctuation density.' FairJudge (arXiv Feb 2026) addresses style bias through judge retraining (SFT+DPO+GRPO), but this requires training a new judge model and does not apply to black-box commercial judges. Meanwhile, the CASSE study (Jan 2026) shows style features are 'deeply entangled rather than orthogonal'—prompting for conciseness significantly reduces perceived expertise—highlighting that naive style removal risks destroying legitimate quality signals. This creates a need for a principled causal method that can (a) apply to any black-box judge, (b) quantify per-response style contributions, and (c) distinguish bias from legitimate style-quality correlation. Causal intervention techniques for LLMs now achieve 92.3% style transfer accuracy while preserving content, and the RATE framework (ICML 2025) provides a double-rewrite protocol for unbiased estimation with imperfect counterfactuals, making this technically feasible.\n\n## Landscape\nSOS-Bench (ICLR 2025) is the largest meta-benchmark documenting style-over-substance failure but proposes no fix. FairJudge (arXiv 2602.06625, Feb 2026) is the most directly relevant concurrent work: it trains a dedicated judge via SFT→DPO→GRPO on a curated 16K-instance dataset with contrastive perturbations along five non-semantic dimensions (position, length, format, reasoning style, model provenance), achieving 76.83% agreement on PandaLM and 78.82% on JudgeLM; however, it requires retraining a new judge model (Qwen3-VL 2B/4B/8B backbones) and cannot debias existing black-box commercial judges (GPT-4o, Claude, Gemini). Soumik (April 2026) tests 9 debiasing strategies across 5 judges but focuses on position/verbosity bias without systematic causal style removal. JudgeBiasBench (March 2026) uses Gemini-2.0-Flash for counterfactual bias injection but applies this to construct biased test instances rather than to estimate and remove style effects. RATE (ICML 2025) is the closest methodological precedent—it estimates causal effects of high-level attributes on reward model scores via a double-rewrite correction for imperfect counterfactuals—but targets reward model explainability, not judge debiasing. The ISE framework (Choi et al., NAACL 2024) argues ATE is inapplicable to text treatments due to positivity violations from high dimensionality, but this criticism applies to free-text treatments, not to well-defined binary style interventions where positivity holds by construction (Pryzant et al. 2021; Veitch et al. UAI 2020). Length-Controlled AlpacaEval (ICLR 2025) demonstrates effective post-hoc regression debiasing but only controls for a single dimension (length) at zero additional inference cost. Bias-Bounded Evaluation (arXiv March 2026) injects calibrated Gaussian noise for differential-privacy-inspired debiasing, retaining 61–99% ranking correlation on Arena-Hard-Auto. CyclicJudge (arXiv March 2026) uses round-robin judge assignment to reduce inter-judge variance but is style-agnostic. RBD (NeurIPS 2025) fine-tunes a reasoning-based bias detector achieving 18.5% accuracy improvement but without causal style decomposition. UDA (AAAI 2026) reduces inter-judge Elo divergence by 63.4% via adaptive K-factor calibration. The CASSE dataset (Jan 2026) documents cross-feature stylistic interactions across 12 style features, showing conciseness reduces perceived expertise, supporting our legitimacy-aware correction design. Causal Effect Estimation with Latent Textual Treatments (arXiv Feb 2026) proposes SAE-based causal estimation for latent text features but has not been applied to judge debiasing. Double Machine Learning (Chernozhukov et al. 2018) provides the partially linear model framework and DoubleML Python package we adopt for flexible decomposition. No arXiv preprint or OpenReview submission as of May 2026 proposes content-preserving binary style counterfactuals combined with doubly-robust DML estimation for black-box judge debiasing.\n\n## Approach\nWe propose Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework in four stages.\n\n**Stage 1 — Binary Style Counterfactual Generation.** For each response under evaluation, generate style counterfactuals along three binary axes: (A1) formality (formal ↔ casual), (A2) verbosity (verbose ↔ terse), (A3) formatting (structured/markdown ↔ plain prose). These three axes are chosen for genuine independence: formality concerns register and word choice, verbosity concerns information density, and formatting concerns visual layout. We use Qwen3-32B with axis-specific prompts, applying the RATE double-rewrite protocol: for each axis, generate (i) a counterfactual x' by flipping the axis and (ii) a double-rewrite x'' by flipping x' back. This yields 6 rewrites per response (2 per axis). Content preservation is enforced via a conjunction of BERTScore ≥ 0.92, NLI entailment ≥ 0.95 (DeBERTa-v3-large-MNLI), GPT-4o-mini content-preservation verification, and human spot-checks on a 10% random sample. **Theoretical justification for binary ATE:** Unlike free-text treatments where positivity is structurally violated (Choi et al. NAACL 2024), binary style axes define well-posed interventions satisfying positivity—any text can be made formal or casual, verbose or terse, structured or plain—following the functional intervention framework (Pryzant et al. 2021; Veitch et al. UAI 2020). RATE's Assumption 1 (direction-independent rewrite noise) and Assumption 2 (additive decomposition of reward into attribute and noise components) provide sufficient conditions for unbiased ATE estimation under imperfect counterfactuals.\n\n**Stage 2 — Doubly-Robust Causal Effect Estimation via DML.** Score each original response and its 6 counterfactuals with the target LLM judge (7 scorings per response). Estimate per-axis treatment effects using a Double Machine Learning partially linear model (Chernozhukov et al. 2018): score = β₁·formality + β₂·verbosity + β₃·formatting + g(content_features) + ε, where β coefficients capture interpretable style effects and g(·) is a nonparametric function of content features (estimated via gradient-boosted trees with 5-fold cross-fitting). This replaces the linear additive SCM: the partially linear form preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects, and the doubly-robust property ensures consistency if either the outcome model or propensity model is correctly specified. For handling residual axis correlations (e.g., formatting weakly correlating with verbosity), we use the multivariate treatment extension of DoubleML, jointly estimating all three β coefficients rather than decomposing them independently. We include ablations comparing: (i) linear additive, (ii) DML partially linear, and (iii) fully nonparametric (kernel-based) decompositions, plus an ISE-based continuous estimator as a methodological comparison.\n\n**Stage 3 — Legitimacy-Aware Score Adjustment.** Rather than naively subtracting the full estimated style ATE (which risks over-correction when style legitimately signals quality—e.g., well-structured markdown for technical content), we introduce a conservatism parameter α ∈ [0,1]: debiased_score = raw_score − α · Σ β_k · style_k. We determine α by maximizing Spearman correlation with ground-truth quality on a held-out validation set. Additionally, we test domain-conditional α values: for each content domain (coding, reasoning, creative writing, factual QA), we estimate whether style-quality correlations are legitimate by checking if style effects are consistent across domains (bias) vs. domain-specific (potentially legitimate). Style effects that are large and domain-invariant are classified as bias; domain-specific effects are partially retained.\n\n**Stage 4 — Amortized Deployment (optional).** To reduce the ~7x overhead of full CSD for large-scale deployment, we train a lightweight amortized style-effect predictor: a small regression model (e.g., linear probe on text embeddings from a frozen encoder) trained on the counterfactual data from Stage 1–2 to predict per-response style attribution vectors from response features alone. At deployment, this predictor estimates style effects without generating new counterfactuals, reducing marginal cost to near-zero. We validate that the amortized predictor recovers ≥90% of the debiasing improvement of the full pipeline.\n\n**Evaluation.** We evaluate across five LLM judges (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Llama-3.3-70B, Qwen3-32B) on four benchmarks: (1) SOS-Bench—measuring whether debiased scores better correlate with objective correctness on constituent benchmarks (IFEval, MMLU-Pro, GPQA) rather than style; (2) LLMBar adversarial set—measuring whether debiased judges resist choosing wrong-but-polished over correct-but-plain responses; (3) RewardBench—domain-specific analysis across chat-hard, safety, and reasoning subsets; (4) RubricBench—1,147 pairwise comparisons with expert-annotated atomic rubrics targeting misleading surface bias. We additionally conduct a 200-response pilot human annotation study with separate 5-point Likert scales for content quality and presentation quality, providing direct validation that debiased scores correlate with content ratings while discounting presentation ratings. Baselines: FairJudge-8B, Length-Controlled AlpacaEval regression, Bias-Bounded Evaluation, raw (undebiased) judges, and a 'format normalization' baseline that strips all markdown before judging.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '100–140 A100-80GB hours (style counterfactual generation with Qwen3-32B: 6 rewrites/response × ~2K responses ≈ 30h; content verification BERTScore/NLI: 3h; open-source judge inference: 25h; DML estimation and ablations: 5h; amortized model training: 2h; iteration buffer: 35–75h)', 'timeline': '12–14 weeks', 'estimated_gpu_cost': '$250–350 (A100 spot ~$2.50/hr) + $200–350 commercial judge API costs (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro) + $100–150 GPT-4o-mini content verification + $800–1200 pilot annotation study (200 responses × 3 annotators)'}, 'human_in_loop': {'gpu_hours': '100–140 A100-80GB hours', 'timeline': '9–11 weeks', 'claude_api_cost': '$150–300 (Sonnet 4.6 at $3/$15 per MTok for prompt engineering, counterfactual quality analysis, DML specification, ablation design, and paper drafting)', 'estimated_gpu_cost': '$250–350 + $200–350 commercial judge API + $100–150 GPT-4o-mini + $800–1200 annotation study'}, 'auto_research': {'gpu_hours': '150–220 A100-80GB hours (additional ablations: linear vs. DML vs. nonparametric, ISE comparison, α sensitivity sweeps, domain-conditional analysis, amortized predictor architectures)', 'timeline': '5–7 weeks', 'claude_api_cost': '$500–750 (Sonnet 4.6 for experiment orchestration, automated counterfactual quality filtering, DML cross-fitting, statistical analysis, and full paper drafting)', 'estimated_gpu_cost': '$375–550 + $300–450 commercial judge API + $150–200 GPT-4o-mini + $800–1200 annotation study', 'speed_bottleneck': 'Sequential dependency chain: style counterfactual generation → content-preservation validation (including human spot-checks) → judge scoring → DML estimation; human annotation study runs in parallel but requires ~2 weeks for annotator recruitment and completion'}}\n\n## Inspired By\nField guide finding: 'Style bias is the dominant bias (0.76–0.92) yet has received minimal research attention'; SOS-Bench limitation that it documents but doesn't solve the problem; FairJudge's success at training-based debiasing motivating the question of whether a model-agnostic alternative exists; RATE's double-rewrite correction as a principled solution to imperfect-counterfactual bias; DML/partially-linear models as the standard tool for flexible causal decomposition with interpretable treatment coefficients; CASSE's finding that style features are entangled motivating legitimacy-aware correction.\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — primary target, 10 weeks)\n- ICLR 2027 (estimated deadline: September 24, 2026 — comfortable 18-week runway)\n- ARR October 2026 cycle (estimated deadline: October 15, 2026 — tertiary option, 21-week runway)\n\n## Key References\n- Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)\n- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)\n- FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625, Feb 2026)\n- Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines (arXiv 2026)\n- Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization (arXiv 2026)\n- RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)\n- Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al., Econometrics Journal 2018)\n- Causal Inference for Human-Language Model Collaboration (Choi et al., NAACL 2024)\n- Adapting Text Embeddings for Causal Inference (Veitch, Sridhar & Blei, UAI 2020)\n- Causal Effects of Linguistic Properties (Pryzant et al., NAACL 2021)\n- A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents (CASSE, arXiv 2601.10809, Jan 2026)\n- Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2025)\n- Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)\n- Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector (NeurIPS 2025)\n- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2026)\n- CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025)\n- RubricBench: Aligning Model-Generated Rubrics with Human Standards (arXiv 2603.01562, March 2026)\n- Estimating Causal Effects of Text Interventions Leveraging LLMs (Findings of AACL-IJCNLP 2025)\n- Causal Effect Estimation with Latent Textual Treatments (arXiv 2026)\n- How to Make Causal Inferences Using Texts (Egami et al., Science Advances 2022)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:44:15.578Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:44:15.578Z",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T04:44:15.591Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- "Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking" (ICLR 2025): 在 152,380 数据点上证明 LLM judges 系统性地优先考虑 style 而非 factuality 和 safety。提出 SOS-Bench 但未提供修复方案。本 proposal 的核心动机之一，确认真实存在。
- "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge" (arXiv 2602.06625, Feb 2026): 通过 SFT→DPO→GRPO 训练去偏 judge（Qwen3-VL 2B/4B/8B），在 PandaLM 达到 76.83% agreement。是最直接的竞争者，但需要模型再训练，无法应用于黑盒商业 API。Proposal 的定位准确。
- "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies" (arXiv 2604.23178, Soumik, April 2026): 跨 5 个 judge 模型测试 9 种去偏策略，确认 style bias 主导 (0.76–0.92)，position bias 极小 (≤0.04)。是 proposal 引用的关键证据，确认真实存在且描述准确。
- "RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals" (ICML 2025, Reber et al.): 提出 double-rewrite 协议修正不完美反事实带来的偏差，用于 reward model 可解释性。是本 proposal 的核心方法论前驱，但原文目标是 reward model explainability，不是 judge debiasing。确认真实存在。
- "Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators" (ICLR 2025, Dubois et al.): 仅控制 length 一个维度的回归去偏，将与 Chatbot Arena 的相关性从 0.94 提升到 0.98。**是最重要的 trivial alternative 威胁**——简单回归方法在单维度上已极其有效。
- "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation" (arXiv 2603.05485, March 2026): DP 启发的高斯噪声注入，保留 61-99% ranking correlation。非因果方法，proposal 正确区分。
- "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features" (CASSE, arXiv 2601.10809, Jan 2026): 证明 style features 深度纠缠（如简洁降低感知专业度），支持 proposal 的 legitimacy-aware correction 设计动机。确认真实存在。
- "Causal Effect Estimation with Latent Textual Treatments" (arXiv 2602.15730, Feb 2026, Feldman et al.): 提出基于 SAE 的潜在文本因果效应估计，使用 covariate residualization 解决偏差问题。方法论上相关但未应用于 judge debiasing。确认真实存在。
- "Doubly-Robust LLM-as-a-Judge: Externally Valid Estimation with Imperfect Personas" (arXiv 2509.22957): 使用 doubly-robust 框架结合 persona ratings 和 human ratings。名称相近但解决的是外部有效性问题，非 style debiasing。
- 调研总结: LLM judge style bias 已被充分记录为主导偏差（远超 position bias），但现有修复方案要么需要模型再训练（FairJudge）、要么仅控制单一维度（LC-AlpacaEval）、要么是非因果方法（BBE）。将因果反事实估计应用于黑盒 judge 多维 style debiasing 的空白确实存在，proposal 的定位准确。截至调研时点，未发现与本 proposal 完全重叠的已发表工作。

【Trivial Alternative 检验】:
最大的 trivial alternative 威胁来自 **多维回归去偏**——即直接将 LC-AlpacaEval 的回归方法扩展到多个 style 维度。具体而言：(1) 用现成分类器测量 formality score、word count、markdown element count 等 style 特征；(2) 拟合多元回归模型控制这些特征。LC-AlpacaEval 仅用 length 回归就已将与 Arena 的 Spearman 相关性从 0.94 提升到 0.98，这是一个极高的基线。

Proposal 相对于此 trivial alternative 的增量价值在于：(a) 因果识别——回归方法只能控制可观测的 style 特征，而反事实方法可以捕获与 style axis 相关的所有效应（包括未被显式度量的）；(b) legitimacy-aware correction 的 domain-conditional α——区分 bias vs. legitimate style-quality correlation，这比简单回归更精细；(c) RATE 双重改写修正不完美反事实偏差。但这些增量价值是否能转化为实质性的实证改进（相比多维回归），是 proposal 最大的不确定性。如果经验上改进微小，审稿人会认为"大量因果机制只换来边际收益"。

另一个更简单的 baseline 是 **format normalization**（剥离 markdown 后评分），proposal 已将其列为 baseline，这是合理的。

【前提假设检验】:
1. **三个二元轴足以捕获"style bias"的主要变异**: Proposal 选择 formality、verbosity、formatting 三个轴，但 style 是一个高维概念。Soumik (2026) 测试了多种 bias 类型，CASSE 列举了 12 种 style features。Tone、sentence complexity、hedging/confidence、vocabulary sophistication 等维度未被覆盖。如果这些未建模的维度贡献了大量 style bias，CSD 的去偏效果会被低估。**这一假设缺乏理论或实证支撑——没有现有工作证明这三个轴解释了 style bias 变异的主要部分。**

2. **内容保持性假设**: 整个因果识别链条依赖于 style 反事实仅改变 style 而不改变 content。虽然 proposal 设计了多重验证（BERTScore ≥ 0.92, NLI ≥ 0.95, GPT-4o-mini 验证），但 CASSE 已证明 style features 深度纠缠——例如让回答变"terse"本质上会移除部分内容信息。BERTScore 和 NLI 可能无法完全检测到这种 subtle content leakage。如果 content preservation 不完美，因果估计就存在偏差，而此时 DML 的 doubly-robust 属性也无法修正（因为违反的是 treatment assignment 的清洁性，不是 nuisance model specification）。

3. **RATE 假设的适用性**: RATE 的 Assumption 1（方向无关的改写噪声）要求正向改写和反向改写引入的噪声具有相同分布。在 style 轴上，这是否成立？例如，将 formal text 变为 casual 可能比将 casual text 变为 formal 更容易保持内容（因为 formal → casual 是"放松约束"，而 casual → formal 可能需要添加信息）。这一假设在 style 轴上是否成立是经验问题，proposal 未提供论证。

4. **α 参数的可靠估计**: Legitimacy-aware correction 需要在 held-out validation set 上最大化 Spearman correlation with ground-truth quality 来确定 α。但 ground-truth quality 的获取本身就依赖于人工标注（或 objective benchmarks），而不同 benchmark 上的"最优 α"可能差异很大。Domain-conditional α 进一步增加了待估参数数量，可能导致过拟合。

【3 维度打分】:
1. Novelty: 中 — 核心贡献是将已有因果方法（RATE double-rewrite + DML partially linear model）组合应用于 LLM judge style debiasing 这一新设定。每个组件单独都是 well-established 的（RATE: ICML 2025; DML: Chernozhukov 2018; style transfer: 成熟技术），但这一特定组合和应用场景（黑盒 judge 多维 style 去偏 + legitimacy-aware correction）在调研中确未发现先例。与 LC-AlpacaEval (ICLR 2025) 的关键区别在于因果识别 + 多维度 + 区分 bias/legitimate correlation；与 FairJudge (2026) 的区别在于无需再训练。Novelty 是真实的但主要在"组合+应用"层面，而非方法论上的根本性创新。Legitimacy-aware correction (domain-conditional α) 是概念上最有新意的部分。**关键弱点：如果多维回归 baseline 就能达到类似效果，组合的因果机制的增量 novelty 会被大幅稀释。**

2. Significance: 强 — Style bias 被多项独立研究（SOS-Bench ICLR 2025, Soumik 2026, CASSE 2026, Preference Leakage ICLR 2026）证实为 LLM judge 的主导偏差（0.76-0.92），远超被过度研究的 position bias（≤0.04）。黑盒 judge debiasing 具有高度实践价值——GPT-4o、Claude、Gemini 等商业 API 无法被再训练。如果 CSD 确实有效，它填补了一个被明确记录但未被解决的空白。问题本身的重要性不成疑问。唯一的 significance 折扣来自：如果 trivial alternative（多维回归）效果接近，则 CSD 的实际影响力有限。

3. Related Work: 强 — Proposal 对领域现状的覆盖极为全面。调研中确认的所有关键论文（SOS-Bench, FairJudge, RATE, LC-AlpacaEval, BBE, CASSE, Soumik 2026, 潜在文本因果估计）均被引用且描述准确。对 ISE (Choi et al. NAACL 2024) 关于 positivity violation 批评的反驳（binary treatments vs. free-text treatments）是合理的。差异化定位清晰：相对于 FairJudge（需再训练）、LC-AlpacaEval（单维度）、BBE（非因果）的区分都准确。"Doubly-Robust LLM-as-a-Judge" (arXiv 2509.22957) 这篇名称相近但实际解决不同问题的论文未被提及，但它确实不直接竞争，不构成覆盖缺陷。

【概率估计】: [28% - 40%] 中位 34%

【估计理由】:
Significance 维度是最强项（强），supported by 多项独立研究确认的 real gap。Related Work 同样扎实（强），覆盖全面且定位准确。Novelty 是限制上界的关键维度（中）：方法论是已有组件的组合应用，核心创新集中在 legitimacy-aware correction 和应用场景定义上。这使得 proposal 处于"idea 有实质内核、方向正确、有真实 novelty delta"的区间（25-35%），但 legitimacy-aware correction 的设计和黑盒适用性提供了一定的 uplift（toward 35-40%）。

上界主要受两个因素制约：(1) trivial alternative 威胁——多维回归去偏可能以 1/10 的成本达到 CSD 80-90% 的效果，这会严重削弱"需要因果机制"的 argument；(2) novelty 主要在组合层面，而非方法论创新，如果实证改进不显著，审稿人可能评价为"principled but unnecessary complexity"。

下界由问题重要性和定位准确性支撑——即使实验结果一般，"第一个将因果反事实方法系统性应用于黑盒 judge style debiasing"的贡献仍有一定价值。

【主要风险】:
1. **Trivial alternative 威胁**: 多维回归（LC-AlpacaEval 的自然扩展）可能以极低成本达到类似去偏效果，使因果机制的复杂性显得不justified。如果实验中 CSD 与多维回归的差距小于 2-3 个百分点，审稿人会质疑整个 pipeline 的必要性。
2. **三轴覆盖度不足 + 内容泄漏**: 仅选择三个 style 轴缺乏充分性论证，且 CASSE 已证明 style features 深度纠缠，意味着 style 反事实改写很可能同时改变了部分 content，违反因果识别的核心假设。这一风险不可通过后续实验设计完全消除——它是 idea 层面的固有脆弱性。
```

Sources:
- [Style Outweighs Substance (ICLR 2025)](https://arxiv.org/abs/2409.15268)
- [FairJudge (arXiv 2602.06625)](https://arxiv.org/abs/2602.06625)
- [RATE: Causal Explainability of Reward Models (ICML 2025)](https://arxiv.org/abs/2410.11348)
- [Judging the Judges: Soumik (arXiv 2604.23178)](https://arxiv.org/abs/2604.23178)
- [CASSE: Concise Agent is Less Expert (arXiv 2601.10809)](https://arxiv.org/abs/2601.10809)
- [Length-Controlled AlpacaEval (ICLR 2025)](https://arxiv.org/abs/2404.04475)
- [Bias-Bounded Evaluation (arXiv 2603.05485)](https://arxiv.org/abs/2603.05485)
- [Causal Effect Estimation with Latent Textual Treatments (arXiv 2602.15730)](https://arxiv.org/abs/2602.15730)
- [Doubly-Robust LLM-as-a-Judge (arXiv 2509.22957)](https://arxiv.org/abs/2509.22957)
- [Toward Robust LLM-Based Judges (arXiv 2603.08091)](https://arxiv.org/html/2603.08091)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **SOS-Bench / "Style Outweighs Substance" (ICLR 2025, arXiv 2409.15268)**:
   Proposal 的核心动机来源。该论文在 152,380 数据点上证明 LLM judges 将 style 优先于 factuality 和 safety，但**只诊断不治疗**——未提出任何 debiasing 方法。Proposal 对此的定位（"documents but doesn't fix"）准确。

2. **FairJudge (arXiv 2602.06625, Feb 2026)**:
   最直接的竞争者。通过 SFT→DPO→GRPO 训练流程在 Qwen3-VL 2B/4B/8B 上训练去偏 judge，取得 76.83%（PandaLM）和 78.82%（JudgeLM）agreement。**关键局限**：需要 retraining，无法对 GPT-4o/Claude 等黑盒 API 去偏。Proposal 的差异化定位（model-agnostic post-hoc）准确且成立。

3. **RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025, arXiv 2410.11348)**:
   Proposal 的核心方法论基础。RATE 用 double-rewrite 协议估计 reward model 对高层属性的因果效应，发表于 ICML 2025 (PMLR 267:51341-51368)。**Proposal 对 RATE 的使用是合理的**——RATE 面向 reward model explainability，CSD 将其扩展到 judge debiasing + DML 框架 + 多维同时估计。但这也构成了 "application extension" 的风险。

4. **Length-Controlled AlpacaEval (ICLR 2025, arXiv 2404.04475)**:
   最重要的 trivial alternative 威胁。通过 logistic regression 控制 length bias，将 AlpacaEval 与 Chatbot Arena 的 Spearman 相关从 0.93 提升到 0.98。**关键问题**：其方法仅控制单维度（length），但将其扩展到多维度（formality, verbosity, formatting）的 regression 并不需要因果反事实生成，是显而易见的 baseline。

5. **Bias-Bounded Evaluation (arXiv 2603.05485, March 2026)**:
   注入校准高斯噪声实现 differential-privacy-inspired 去偏，保留 61-99% ranking correlation。非因果方法，与 CSD 形成正交对比。Proposal 将其作为 baseline 是合理的。

6. **Preference Leakage (ICLR 2026, arXiv 2502.01534)**:
   研究 judge 与 generator 之间的 contamination bias，发现 judges 依赖 "stylistic regularities—tone consistency, sentence cadence, punctuation density"。这为 style bias 的存在提供了额外实证支持，但解决的是不同问题（contamination vs. style debiasing）。

7. **CASSE (arXiv 2601.10809, Jan 2026)**:
   发现 style features "deeply entangled rather than orthogonal"——prompting for conciseness significantly reduces perceived expertise。这为 Proposal 的 legitimacy-aware correction 设计提供了实证动机，引用合理。

8. **Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2025)**:
   生成 250,000+ 反事实写作样本来度量修辞风格。方法论上与 CSD 有相似之处（counterfactual style generation），但目标不同（度量 vs. 去偏）。Proposal 未引用此工作，是一个覆盖盲点。

9. **Judging the Judges (arXiv 2604.23178, April 2026)**:
   系统评估 9 种 debiasing 策略在 5 个 judges 上的效果，结论是现有策略 "necessary but insufficient"。这进一步证明了 style debiasing 的 gap 存在。

10. **Causal Effect Estimation-guided Multi-Bias Elimination / CMBE (arXiv 2505.16522)**:
    用因果效应估计指导多偏差消除，但面向 LLM 自身的社会偏见（如性别/种族），而非 judge 评分中的 style bias。方法论有交集但问题域不同。

- **调研总结**: LLM-as-a-judge 的 style bias 已被 SOS-Bench 等大规模研究确认为最大系统性偏差（effect size 0.76-0.92），远超 position bias。现有 debiasing 方案要么需要 retraining（FairJudge）、只控制单一维度（LC AlpacaEval）、或非因果（Bias-Bounded Evaluation）。**对黑盒 judge 进行多维因果 style debiasing 的空白确实存在**，但这个空白是否需要完整的 counterfactual generation + DML 管道来填补，还是简单的多维 regression 就够了，是核心争议点。


【Trivial Alternative 检验】:

**存在一个成本显著更低的替代方案**：将 Length-Controlled AlpacaEval 的 regression 方法扩展到多维度。具体地，提取每个 response 的可观测 style 特征（word count、markdown 元素数量、formality classifier score、sentence length 等），然后在 judge score 上做多维回归控制。这不需要任何反事实生成（省去 6 rewrites/response 的计算开销）和额外的 judge 调用（省去 7x overhead），成本接近零。

**CSD 的增量价值在于**：(1) 因果识别——regression on observables 受遗漏变量偏差影响，而反事实干预提供因果估计；(2) 反事实验证——可以直观地看到"同一内容换了风格后分数如何变化"；(3) DML 的 doubly-robust 性质提供更稳健的估计。

**但这个增量价值是否实质性的**，取决于实证结果：如果简单 regression 已经能达到 CSD 90%+ 的去偏效果，那 7x 的额外开销就很难 justify。Proposal 确实将 LC AlpacaEval 作为 baseline，这是关键消融实验——但如果结果显示差距不大，整篇论文的 contribution 会被大幅削弱。这是一个 "bet on empirical results" 的 idea。


【前提假设检验】:

1. **"三个 style 轴是独立的且足够覆盖 style bias"**——这是未验证的假设。Proposal 声称 formality、verbosity、formatting "genuinely independent"，但 CASSE 恰好发现 style features 是 "deeply entangled"。此外，style bias 可能还包括 tone、confidence、hedging、example usage 等维度，三个轴能捕获多少 style bias variance 是未知的。如果三轴只解释了 40% 的 style bias，debiasing 效果上限就受限。

2. **"反事实生成能做到 content-preserving"**——这是整个方法论的基石假设。虽然 Proposal 设置了多重验证（BERTScore ≥ 0.92, NLI ≥ 0.95, GPT-4o-mini 验证），但 style 和 content 在自然语言中高度纠缠（CASSE 的核心发现）。改变 formality 几乎不可避免地改变 perceived expertise（CASSE 实证结论）——这到底是 content change 还是 style change？BERTScore/NLI 是否能捕获这种细微差异？RATE 的 double-rewrite 能纠正多少 imperfect-counterfactual bias？这些都没有在 judge debiasing 场景下被验证过。

3. **"α 参数可以通过验证集优化来区分 legitimate 和 illegitimate style-quality correlation"**——这假设存在可靠的 ground-truth quality annotation。但如果 ground truth 本身就受 style bias 影响（人类标注者也有 style bias），α 的校准就失去了锚点。Proposal 设计了 200 人 pilot study 分别标注 content quality 和 presentation quality，但 200 样本是否足够、人类是否能真正分离 content 和 presentation 判断，都是未经验证的。


【3 维度打分】:

1. **Novelty: 中** — CSD 的核心贡献是将 RATE 的 double-rewrite 协议（ICML 2025）与 DML 的 partially linear model（Chernozhukov et al. 2018）组合，应用于 black-box judge debiasing 这个新场景。调研确认没有现有工作做过完全相同的组合（截至 2026 年 5 月无 arXiv 预印本覆盖此交叉点）。但这本质上是 **"known method A + known method B → new application"** 的组合创新，方法论层面没有新的理论贡献。Legitimacy-aware correction（α 参数）是一个有价值的设计，但技术上就是 regularization tuning，不构成重大创新。与 LC AlpacaEval (ICLR 2025) 的核心差异是"因果反事实 vs. 观测回归"——这个差异是否实质性取决于实验结果。整体属于 solid incremental novelty，不是 surprising insight。

2. **Significance: 中偏强** — 研究问题毫无疑问是重要的。SOS-Bench (ICLR 2025) 定量证明 style bias 是 LLM judge 最大偏差（effect size 0.76-0.92），Judging the Judges (arXiv 2604.23178) 确认现有 debiasing 策略不充分。LLM-as-a-judge 已成为模型评估和对齐的核心基础设施，style bias 直接影响 RLHF/alignment 的可靠性。一个 model-agnostic 的解决方案（适用于 GPT-4o、Claude 等商业 API）有明确的实际需求。但影响力受限于：(a) 如果 simple regression baseline 效果接近，实际 adoption 不太可能选择 7x overhead 的 CSD；(b) 三个 style 轴的覆盖范围可能不足以 fully solve 问题。

3. **Related Work: 强** — Proposal 的 related work 覆盖非常全面。所有关键竞争者（FairJudge、LC AlpacaEval、Bias-Bounded Evaluation、RATE、SOS-Bench、CASSE、Preference Leakage）均被引用且描述准确（经调研验证）。差异化定位清晰：vs. FairJudge（retraining vs. model-agnostic）、vs. LC AlpacaEval（single-dim vs. multi-dim causal）、vs. Bias-Bounded（noise injection vs. causal decomposition）。对 ISE 框架（Choi et al. NAACL 2024）关于 positivity violation 的反驳（binary treatment vs. free-text treatment）方法论上合理。唯一的小缺口是未引用"Counterfactual LLM-based Framework for Measuring Rhetorical Style"（arXiv 2025），该工作在方法论上有一定相似性（counterfactual style generation），但影响不大。


【概率估计】: [28% - 38%] 中位 32%

【估计理由】:
- **Novelty (中)** 是上界的主要限制因素。核心贡献是 RATE + DML 的组合应用，审稿人可能会评价为 "well-executed but not surprising"。如果核心发现是 positive（CSD 有效去偏），审稿人的反应更可能是 "makes sense, this is what I'd expect from applying causal inference tools to this problem" 而非 "surprising, I wouldn't have predicted this"。
- **Significance (中偏强)** 支撑了下界不低于 28%。问题确实重要，gap 确实存在，方案差异化明确。
- **Related Work (强)** 确保论文不会因 related work 不足被拒，但也不会因此加分。
- 概率未达 35%+ 区间的原因：trivial alternative（多维 regression）威胁是真实的——如果 LC AlpacaEval 扩展到多维度后效果接近 CSD，论文的 contribution 叙事会被严重削弱。这个风险使得 idea 的上限受限。

【主要风险】:
1. **Trivial alternative 风险**：多维 observational regression（LC AlpacaEval 的自然扩展）可能以接近零的额外成本达到 CSD 80-90% 的去偏效果，使得 7x overhead 的因果管道难以 justify。这是最可能被审稿人质疑的点——"Why not just regress out multiple style features without counterfactuals?"
2. **Content-style 不可分性风险**：CASSE 的核心发现（style features are deeply entangled）实际上对 CSD 的前提假设构成双刃剑——它既证明了 legitimacy-aware correction 的必要性，也暗示了 content-preserving style counterfactual 可能本质上不存在。如果审稿人认为"改变 formality 必然改变 perceived content quality"，CSD 的因果识别策略就会受到根本性质疑。
```

Sources:
- [SOS-Bench: Style Outweighs Substance (ICLR 2025)](https://arxiv.org/abs/2409.15268)
- [FairJudge (arXiv Feb 2026)](https://arxiv.org/abs/2602.06625)
- [RATE: Causal Explainability of Reward Models (ICML 2025)](https://arxiv.org/abs/2410.11348)
- [Length-Controlled AlpacaEval (ICLR 2025)](https://arxiv.org/abs/2404.04475)
- [Bias-Bounded Evaluation (arXiv March 2026)](https://arxiv.org/abs/2603.05485)
- [Preference Leakage (ICLR 2026)](https://arxiv.org/abs/2502.01534)
- [CASSE: A Concise Agent is Less Expert (arXiv Jan 2026)](https://arxiv.org/abs/2601.10809)
- [Judging the Judges (arXiv April 2026)](https://arxiv.org/abs/2604.23178)
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style](https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style)
- [CMBE: Multi-Bias Elimination via Causal Effect Estimation](https://arxiv.org/abs/2505.16522)
- [RBD: Reasoning-based Bias Detector (NeurIPS 2025)](https://openreview.net/forum?id=sLNz60fJFF)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough research context to make an informed assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- **SOS-Bench / "Style Outweighs Substance" (ICLR 2025, arXiv 2409.15268)**: 最大规模的 LLM judge 偏差元基准（152K 数据点），证实 style bias 在所有主流 judge 中占主导地位（sarcasm 导致 96% 偏好损失，而错误答案仅 13%）。该工作只诊断不治疗——没有提出任何 debiasing 方案。Proposal 正确识别了这个"诊断无方案"的空白。
- **FairJudge (arXiv 2602.06625, Feb 2026)**: 最直接的竞争者。通过 SFT→DPO→GRPO 课程式训练（Qwen3-VL 2B/4B/8B backbone）构建去偏 judge，在 PandaLM 76.83%、JudgeLM 78.82% agreement。**核心局限**：需要重新训练 judge 模型，无法适用于 GPT-4o/Claude/Gemini 等黑盒 API。Proposal 的 model-agnostic 定位与之差异化合理。
- **RATE (ICML 2025, arXiv 2410.11348)**: 本 proposal 最核心的方法论前身。使用 double-rewrite protocol 校正不完美反事实，估计 reward model 对高层属性的因果效应。**关键区别**：RATE 的目标是 reward model explainability，而非 judge debiasing。CSD 本质上是将 RATE 的 rewrite protocol 嫁接到 DML 框架并应用于 judge 去偏——这是一个 application pivot 而非方法论创新。
- **Length-Controlled AlpacaEval (ICLR 2025, arXiv 2404.04475)**: 通过 logistic regression 控制 length 的 post-hoc debiasing 方案，将与 ChatBot Arena 的 Spearman 相关性从 0.93 提升到 0.98。**这是最重要的 trivial alternative 参照物**：该方法成本为零，单维度回归即取得巨大效果。Proposal 需要令人信服地证明多维因果分解（7x 成本开销）相对于"多维回归控制"的增量价值。
- **Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2512.19908, Dec 2025)**: 使用 LLM 生成反事实风格重写 + Bradley-Terry 模型量化学术论文的修辞风格。在 8,485 篇 ICLR 投稿上生成 250K+ 反事实文本。该工作与 CSD 共享"反事实风格重写"的核心技术思路，但目标是 style measurement 而非 judge debiasing。
- **Bias-Bounded Evaluation (arXiv 2603.05485, March 2026)**: 差分隐私启发的校准高斯噪声注入，在 Arena-Hard-Auto 上保留 61-99% 排名相关性。非因果方法，提供形式化偏差上界保证。
- **Preference Leakage (ICLR 2026, arXiv 2502.01534)**: 发现 judge 与生成模型的"亲缘关系"导致评估偏差，属于 contamination bias 而非 style bias，与本 proposal 正交但同属 judge bias 生态。
- **CASSE (arXiv 2601.10809, Jan 2026)**: 研究 12 种 style feature 的交互效应，核心发现 style features "deeply entangled rather than orthogonal"。这同时支持了 proposal 的 legitimacy-aware correction 设计，但也威胁了其"三轴独立"假设。
- **Choi et al. ISE (NAACL 2024)**: 论证 ATE 在自由文本 treatment 上因 positivity violation 不可行。Proposal 通过限制 binary style intervention 来规避此批评，这个应对策略在方法论上是合理的。
- **Judging the Judges / Soumik (arXiv 2604.23178, April 2026)**: 系统测试 9 种 debiasing 策略 × 5 种 judge，但聚焦 position/verbosity bias，没有系统性因果 style removal。
- **调研总结**: Style bias in LLM judges 是一个已被充分诊断但 debiasing 方案稀缺的领域。现有方案要么需要训练（FairJudge），要么只控单维度（LC-AlpacaEval），要么非因果（BBE）。Post-hoc + model-agnostic + 多维因果的组合确实存在空白。但 RATE 的 double-rewrite + 反事实风格重写 的技术路线已在邻近工作中被探索，CSD 的核心创新更多在于"组合与应用场景"而非"方法论突破"。


【Trivial Alternative 检验】:

**存在两个严重的 trivial alternative 威胁：**

1. **多维回归控制（Multi-dimensional LC-AlpacaEval 扩展）**: LC-AlpacaEval 仅用单维度 logistic regression 控制 length 就将相关性从 0.93→0.98，零额外推理成本。一个自然的扩展是：提取多个 surface features（token count、markdown 标记密度、平均句长、正式词占比等），用多维回归做 post-hoc 控制。这个方法：无需反事实生成（省去 7x 成本）、无需 DML 框架、无需 content preservation 验证。如果这个 trivial baseline 能达到 CSD 80%+ 的去偏效果，CSD 的增量价值将严重受损。Proposal 确实包含了 LC-AlpacaEval 作为 baseline，但仅作为"单维度"对比——真正的威胁是多维度扩展版，proposal 未直接面对这个问题。

2. **Format normalization + 简单 prompt engineering**: Proposal 自己也列了 "strip all markdown before judging" 作为 baseline，加上 "请忽略风格只关注内容" 的 prompt，这组合的成本几乎为零。如果格式化是 style bias 的主要来源（markdown/列表视觉效果），这个 trivial 方法可能已覆盖大部分效应。

**增量价值声称**：CSD 的增量价值需建立在以下论证上：(a) 多维回归无法捕捉 style 与 content 之间的非线性交互，而 DML 可以；(b) 因果估计提供了 per-response 的风格归因（而非群体平均），对个案审查有价值；(c) legitimacy-aware correction 需要因果框架才能区分 bias 与合法相关性。论证 (c) 最具说服力，但也最难验证。


【前提假设检验】:

**核心 claim 的逻辑链中，有以下关键未验证假设：**

1. **"三轴独立"假设**：Proposal 声称 formality、verbosity、formatting "genuinely independent"，但 CASSE (Jan 2026) 的核心发现恰恰是 style features "deeply entangled"。例如：formal 文本通常更 verbose、更倾向使用 structured formatting。虽然 proposal 提到用 multivariate DML 处理残余相关，但反事实生成阶段仍假定可以独立翻转单个轴而不影响其他轴。如果 flip formality 的同时系统性地改变了 verbosity（因为 casual 文本天然更短），整个因果估计框架的有效性就受到威胁。

2. **Content preservation under style rewriting**: BERTScore ≥ 0.92 和 NLI ≥ 0.95 是否足以保证"内容等价"？一篇高度技术性的 formal 文本被重写为 casual 版本时，术语精确度和推理严谨度可能系统性降低——这种降低不会被 BERTScore（表面语义相似度）或 NLI（单向蕴含）捕捉到。如果 content quality 在 style flip 过程中被系统性地改变，那估计的"style effect"实际上混杂了 content degradation effect。

3. **RATE 的 Assumption 1 & 2 跨 judge 迁移**：RATE 的双重重写校正依赖两个假设——方向无关的重写噪声和加性分解。这些假设在 RATE 原论文中只在特定 reward model 上验证。不同的 LLM judge（GPT-4o vs. Claude vs. Llama）可能有非常不同的评分机制，假设的跨 judge 一致性缺乏理论支撑。

4. **Style 效应线性可加性**：DML partially linear model 假定 score = β₁·formality + β₂·verbosity + β₃·formatting + g(content) + ε。但 style 效应很可能与 content domain 存在交互作用（coding 场景下 formatting 的效应远大于 creative writing 场景）。虽然 Stage 3 的 domain-conditional α 部分缓解了这个问题，但 Stage 2 的估计阶段仍假定全局线性可加性。

5. **α 的可识别性**: legitimacy-aware correction 的 α 通过"最大化与 ground-truth quality 的 Spearman 相关性"来确定。但如果 ground-truth 本身有限（200-response pilot study），α 可能过拟合这个小样本。而且如果不同 benchmark 的最优 α 差异很大，"legitimacy"本身就成了一个 benchmark-dependent 的概念而非通用原则。


【3 维度打分】:

1. **Novelty: 中** — CSD 的核心技术组件（反事实风格重写、double-rewrite 校正、DML partially linear model）均已在各自领域存在成熟先例。RATE (ICML 2025) 提供了 double-rewrite protocol，LC-AlpacaEval (ICLR 2025) 示范了 post-hoc regression debiasing，DML (Chernozhukov 2018) 是标准因果推断工具。Counterfactual LLM-based Framework (arXiv 2512.19908) 已经在使用反事实风格重写。CSD 的新颖性主要在于这些组件的**组合应用**——将 RATE 的 rewrite protocol 嫁接到 DML 框架、增加 legitimacy-aware correction、面向黑盒 judge debiasing。这是一个合理的 application novelty，但不是方法论突破。Legitimacy-aware correction (α parameter + domain-conditional analysis) 是最具原创性的贡献，但本质上是一个调参策略。如果核心结果是 "CSD 比 raw judge 提高了 correlation"，审稿人会说 "I would have guessed this works"。

2. **Significance: 中偏强** — 问题本身非常重要。SOS-Bench (ICLR 2025) 以 152K 数据点证实 style bias 是 dominant bias，CASSE 进一步揭示 style 效应的 entanglement，Preference Leakage (ICLR 2026) 揭示 judge bias 的更多维度。LLM-as-a-judge 已成为 NLP 评估基础设施的核心组件，其去偏是一个有广泛影响力的实用问题。Model-agnostic 的 post-hoc 方案填补了 FairJudge（需训练）和 LC-AlpacaEval（单维度）之间的空白。然而，7x 推理成本开销限制了实际采用场景（大规模 leaderboard 可能不愿支付这个成本），amortized 版本虽降低成本但需要训练，与 "no training needed" 的主打优势有内在张力。

3. **Related Work: 强** — 覆盖非常全面。FairJudge、RATE、LC-AlpacaEval、SOS-Bench、CASSE、BBE、Preference Leakage、ISE (Choi et al.)、DML、RBD、UDA、CyclicJudge 等均有讨论。对 ISE (NAACL 2024) 关于 positivity violation 的批评有直接回应（binary intervention 规避），与 LC-AlpacaEval 的差异化定位清晰。Landscape section 几乎覆盖了 2024-2026 的所有相关工作。唯一缺漏是 Counterfactual LLM-based Framework (arXiv 2512.19908) 虽在引用列表中但 landscape 段没有深入对比。


【概率估计】: [23% - 33%] 中位 28%

【估计理由】: 
- **Significance 是最强维度**（中偏强），问题重要且空白真实，这撑住了下界不至于太低。
- **Novelty 是主要限制维度**（中），组合应用型创新在顶会审稿中通常被视为 incremental。审稿人会认出 RATE + DML 的组合，并质疑 "what is the fundamental new insight beyond combining existing tools?"。核心发现若 positive（"去偏后 correlation 更高"），审稿人不会感到 surprising。
- **Trivial alternative 威胁真实**：多维回归控制（零成本）vs. CSD（7x 成本）的性价比对比，如果 CSD 不能在实验中碾压 trivial baseline，论文说服力大打折扣。这个风险拉低了上界。
- 上界 33% 反映了"如果 trivial baseline 被有效击败 + legitimacy-aware correction 展示出意想不到的效果"的最佳情景。下界 23% 反映了"novelty 被判 incremental + trivial baseline 表现相近"的情景。

【主要风险】: 
1. **Novelty 被判为 incremental（"RATE + DML = CSD"）**: 审稿人可能认为这是将两个已知工具组合应用到一个新场景，缺乏方法论深度。尤其当 RATE 已经做了 double-rewrite 因果效应估计、LC-AlpacaEval 已经做了 post-hoc regression debiasing 时，"把它们合在一起做 multi-dimensional causal debiasing" 的 novelty increment 可能不足以支撑一篇顶会论文。
2. **Trivial alternative 表现出人意料地好**: 如果 "多维 surface feature 回归 + format stripping" 这个零成本方案已经能消除大部分 style bias，CSD 的 7x 推理成本开销就变得不可辩护。这是一个实验才能回答的问题，但它是 idea 层面的结构性风险——如果 trivial baseline 表现好，说明问题本身不需要因果框架来解决。
```

Sources:
- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)](https://arxiv.org/abs/2409.15268)
- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625)](https://arxiv.org/abs/2602.06625)
- [RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)](https://arxiv.org/abs/2410.11348)
- [Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)](https://arxiv.org/abs/2404.04475)
- [Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2512.19908)](https://arxiv.org/abs/2512.19908)
- [Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2603.05485)](https://arxiv.org/abs/2603.05485)
- [Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)](https://arxiv.org/abs/2502.01534)
- [A Concise Agent is Less Expert: CASSE (arXiv 2601.10809)](https://arxiv.org/abs/2601.10809)
- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies (arXiv 2604.23178)](https://arxiv.org/abs/2604.23178)
- [Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation (arXiv 2603.08091)](https://arxiv.org/abs/2603.08091)


【原始 proposal（允许参考但不是主要依据）】:
# Causal Style Decomposition for LLM Judge Debiasing via Doubly-Robust Counterfactual Estimation

## Description
Style bias is the dominant systematic bias in LLM-as-a-judge evaluations (effect size 0.76–0.92 across all major models), vastly exceeding position bias (≤0.04), yet no existing method causally isolates and removes style's contribution to black-box judge scores. FairJudge (Feb 2026) addresses style bias by retraining a dedicated judge, but cannot debias commercial APIs like GPT-4o or Claude. We introduce Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework that generates content-preserving binary style counterfactuals along three independent axes (formality, verbosity, formatting) using RATE's double-rewrite protocol, then estimates per-axis causal effects via a Double Machine Learning partially linear model (Chernozhukov et al. 2018) that preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects. A legitimacy-aware correction avoids over-debiasing by tuning a conservatism parameter α that distinguishes domain-invariant style bias from legitimate style-quality correlations. Unlike FairJudge (requires retraining), Length-Controlled AlpacaEval (single dimension), or Bias-Bounded Evaluation (non-causal noise injection), CSD provides a principled, multi-dimensional causal decomposition applicable to any black-box judge. We evaluate across five LLM judges on SOS-Bench (objective correctness), LLMBar adversarial (style resistance), RewardBench (domain-specific), and RubricBench (atomic rubric-based), supplemented by a 200-response pilot study with separate human annotations for content and presentation quality. An optional amortized deployment stage trains a lightweight predictor to estimate style effects without generating new counterfactuals, reducing marginal overhead to near-zero. CSD requires no judge retraining, applies to any black-box judge API, and reduces per-response debiasing cost from 25x (naive) to ~7x (full pipeline) or near-zero (amortized).

## Core Problem
How can we isolate and remove the causal effect of surface-level style on LLM judge scores while preserving legitimate style-content associations, recovering a score that more faithfully reflects content quality?

## Opportunity
Style bias is the dominant bias in LLM judges (effect size 0.76–0.92 across all models per Soumik 2026), vastly exceeding position bias (≤0.04), yet debiasing research overwhelmingly targets position bias. SOS-Bench (ICLR 2025) demonstrated that LLM judges prioritize style over factuality and safety across 152,380 data points. The 'Preference Leakage' paper (ICLR 2026) found judges rely heavily on 'stylistic regularities—tone consistency, sentence cadence, punctuation density.' FairJudge (arXiv Feb 2026) addresses style bias through judge retraining (SFT+DPO+GRPO), but this requires training a new judge model and does not apply to black-box commercial judges. Meanwhile, the CASSE study (Jan 2026) shows style features are 'deeply entangled rather than orthogonal'—prompting for conciseness significantly reduces perceived expertise—highlighting that naive style removal risks destroying legitimate quality signals. This creates a need for a principled causal method that can (a) apply to any black-box judge, (b) quantify per-response style contributions, and (c) distinguish bias from legitimate style-quality correlation. Causal intervention techniques for LLMs now achieve 92.3% style transfer accuracy while preserving content, and the RATE framework (ICML 2025) provides a double-rewrite protocol for unbiased estimation with imperfect counterfactuals, making this technically feasible.

## Landscape
SOS-Bench (ICLR 2025) is the largest meta-benchmark documenting style-over-substance failure but proposes no fix. FairJudge (arXiv 2602.06625, Feb 2026) is the most directly relevant concurrent work: it trains a dedicated judge via SFT→DPO→GRPO on a curated 16K-instance dataset with contrastive perturbations along five non-semantic dimensions (position, length, format, reasoning style, model provenance), achieving 76.83% agreement on PandaLM and 78.82% on JudgeLM; however, it requires retraining a new judge model (Qwen3-VL 2B/4B/8B backbones) and cannot debias existing black-box commercial judges (GPT-4o, Claude, Gemini). Soumik (April 2026) tests 9 debiasing strategies across 5 judges but focuses on position/verbosity bias without systematic causal style removal. JudgeBiasBench (March 2026) uses Gemini-2.0-Flash for counterfactual bias injection but applies this to construct biased test instances rather than to estimate and remove style effects. RATE (ICML 2025) is the closest methodological precedent—it estimates causal effects of high-level attributes on reward model scores via a double-rewrite correction for imperfect counterfactuals—but targets reward model explainability, not judge debiasing. The ISE framework (Choi et al., NAACL 2024) argues ATE is inapplicable to text treatments due to positivity violations from high dimensionality, but this criticism applies to free-text treatments, not to well-defined binary style interventions where positivity holds by construction (Pryzant et al. 2021; Veitch et al. UAI 2020). Length-Controlled AlpacaEval (ICLR 2025) demonstrates effective post-hoc regression debiasing but only controls for a single dimension (length) at zero additional inference cost. Bias-Bounded Evaluation (arXiv March 2026) injects calibrated Gaussian noise for differential-privacy-inspired debiasing, retaining 61–99% ranking correlation on Arena-Hard-Auto. CyclicJudge (arXiv March 2026) uses round-robin judge assignment to reduce inter-judge variance but is style-agnostic. RBD (NeurIPS 2025) fine-tunes a reasoning-based bias detector achieving 18.5% accuracy improvement but without causal style decomposition. UDA (AAAI 2026) reduces inter-judge Elo divergence by 63.4% via adaptive K-factor calibration. The CASSE dataset (Jan 2026) documents cross-feature stylistic interactions across 12 style features, showing conciseness reduces perceived expertise, supporting our legitimacy-aware correction design. Causal Effect Estimation with Latent Textual Treatments (arXiv Feb 2026) proposes SAE-based causal estimation for latent text features but has not been applied to judge debiasing. Double Machine Learning (Chernozhukov et al. 2018) provides the partially linear model framework and DoubleML Python package we adopt for flexible decomposition. No arXiv preprint or OpenReview submission as of May 2026 proposes content-preserving binary style counterfactuals combined with doubly-robust DML estimation for black-box judge debiasing.

## Approach
We propose Causal Style Decomposition (CSD), a model-agnostic post-hoc debiasing framework in four stages.

**Stage 1 — Binary Style Counterfactual Generation.** For each response under evaluation, generate style counterfactuals along three binary axes: (A1) formality (formal ↔ casual), (A2) verbosity (verbose ↔ terse), (A3) formatting (structured/markdown ↔ plain prose). These three axes are chosen for genuine independence: formality concerns register and word choice, verbosity concerns information density, and formatting concerns visual layout. We use Qwen3-32B with axis-specific prompts, applying the RATE double-rewrite protocol: for each axis, generate (i) a counterfactual x' by flipping the axis and (ii) a double-rewrite x'' by flipping x' back. This yields 6 rewrites per response (2 per axis). Content preservation is enforced via a conjunction of BERTScore ≥ 0.92, NLI entailment ≥ 0.95 (DeBERTa-v3-large-MNLI), GPT-4o-mini content-preservation verification, and human spot-checks on a 10% random sample. **Theoretical justification for binary ATE:** Unlike free-text treatments where positivity is structurally violated (Choi et al. NAACL 2024), binary style axes define well-posed interventions satisfying positivity—any text can be made formal or casual, verbose or terse, structured or plain—following the functional intervention framework (Pryzant et al. 2021; Veitch et al. UAI 2020). RATE's Assumption 1 (direction-independent rewrite noise) and Assumption 2 (additive decomposition of reward into attribute and noise components) provide sufficient conditions for unbiased ATE estimation under imperfect counterfactuals.

**Stage 2 — Doubly-Robust Causal Effect Estimation via DML.** Score each original response and its 6 counterfactuals with the target LLM judge (7 scorings per response). Estimate per-axis treatment effects using a Double Machine Learning partially linear model (Chernozhukov et al. 2018): score = β₁·formality + β₂·verbosity + β₃·formatting + g(content_features) + ε, where β coefficients capture interpretable style effects and g(·) is a nonparametric function of content features (estimated via gradient-boosted trees with 5-fold cross-fitting). This replaces the linear additive SCM: the partially linear form preserves interpretable style coefficients while allowing arbitrary nonlinear content-quality effects, and the doubly-robust property ensures consistency if either the outcome model or propensity model is correctly specified. For handling residual axis correlations (e.g., formatting weakly correlating with verbosity), we use the multivariate treatment extension of DoubleML, jointly estimating all three β coefficients rather than decomposing them independently. We include ablations comparing: (i) linear additive, (ii) DML partially linear, and (iii) fully nonparametric (kernel-based) decompositions, plus an ISE-based continuous estimator as a methodological comparison.

**Stage 3 — Legitimacy-Aware Score Adjustment.** Rather than naively subtracting the full estimated style ATE (which risks over-correction when style legitimately signals quality—e.g., well-structured markdown for technical content), we introduce a conservatism parameter α ∈ [0,1]: debiased_score = raw_score − α · Σ β_k · style_k. We determine α by maximizing Spearman correlation with ground-truth quality on a held-out validation set. Additionally, we test domain-conditional α values: for each content domain (coding, reasoning, creative writing, factual QA), we estimate whether style-quality correlations are legitimate by checking if style effects are consistent across domains (bias) vs. domain-specific (potentially legitimate). Style effects that are large and domain-invariant are classified as bias; domain-specific effects are partially retained.

**Stage 4 — Amortized Deployment (optional).** To reduce the ~7x overhead of full CSD for large-scale deployment, we train a lightweight amortized style-effect predictor: a small regression model (e.g., linear probe on text embeddings from a frozen encoder) trained on the counterfactual data from Stage 1–2 to predict per-response style attribution vectors from response features alone. At deployment, this predictor estimates style effects without generating new counterfactuals, reducing marginal cost to near-zero. We validate that the amortized predictor recovers ≥90% of the debiasing improvement of the full pipeline.

**Evaluation.** We evaluate across five LLM judges (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, Llama-3.3-70B, Qwen3-32B) on four benchmarks: (1) SOS-Bench—measuring whether debiased scores better correlate with objective correctness on constituent benchmarks (IFEval, MMLU-Pro, GPQA) rather than style; (2) LLMBar adversarial set—measuring whether debiased judges resist choosing wrong-but-polished over correct-but-plain responses; (3) RewardBench—domain-specific analysis across chat-hard, safety, and reasoning subsets; (4) RubricBench—1,147 pairwise comparisons with expert-annotated atomic rubrics targeting misleading surface bias. We additionally conduct a 200-response pilot human annotation study with separate 5-point Likert scales for content quality and presentation quality, providing direct validation that debiased scores correlate with content ratings while discounting presentation ratings. Baselines: FairJudge-8B, Length-Controlled AlpacaEval regression, Bias-Bounded Evaluation, raw (undebiased) judges, and a 'format normalization' baseline that strips all markdown before judging.

## Resource Estimate
{'manual': {'gpu_hours': '100–140 A100-80GB hours (style counterfactual generation with Qwen3-32B: 6 rewrites/response × ~2K responses ≈ 30h; content verification BERTScore/NLI: 3h; open-source judge inference: 25h; DML estimation and ablations: 5h; amortized model training: 2h; iteration buffer: 35–75h)', 'timeline': '12–14 weeks', 'estimated_gpu_cost': '$250–350 (A100 spot ~$2.50/hr) + $200–350 commercial judge API costs (GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro) + $100–150 GPT-4o-mini content verification + $800–1200 pilot annotation study (200 responses × 3 annotators)'}, 'human_in_loop': {'gpu_hours': '100–140 A100-80GB hours', 'timeline': '9–11 weeks', 'claude_api_cost': '$150–300 (Sonnet 4.6 at $3/$15 per MTok for prompt engineering, counterfactual quality analysis, DML specification, ablation design, and paper drafting)', 'estimated_gpu_cost': '$250–350 + $200–350 commercial judge API + $100–150 GPT-4o-mini + $800–1200 annotation study'}, 'auto_research': {'gpu_hours': '150–220 A100-80GB hours (additional ablations: linear vs. DML vs. nonparametric, ISE comparison, α sensitivity sweeps, domain-conditional analysis, amortized predictor architectures)', 'timeline': '5–7 weeks', 'claude_api_cost': '$500–750 (Sonnet 4.6 for experiment orchestration, automated counterfactual quality filtering, DML cross-fitting, statistical analysis, and full paper drafting)', 'estimated_gpu_cost': '$375–550 + $300–450 commercial judge API + $150–200 GPT-4o-mini + $800–1200 annotation study', 'speed_bottleneck': 'Sequential dependency chain: style counterfactual generation → content-preservation validation (including human spot-checks) → judge scoring → DML estimation; human annotation study runs in parallel but requires ~2 weeks for annotator recruitment and completion'}}

## Inspired By
Field guide finding: 'Style bias is the dominant bias (0.76–0.92) yet has received minimal research attention'; SOS-Bench limitation that it documents but doesn't solve the problem; FairJudge's success at training-based debiasing motivating the question of whether a model-agnostic alternative exists; RATE's double-rewrite correction as a principled solution to imperfect-counterfactual bias; DML/partially-linear models as the standard tool for flexible causal decomposition with interpretable treatment coefficients; CASSE's finding that style features are entangled motivating legitimacy-aware correction.

## Target Venues
- AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — primary target, 10 weeks)
- ICLR 2027 (estimated deadline: September 24, 2026 — comfortable 18-week runway)
- ARR October 2026 cycle (estimated deadline: October 15, 2026 — tertiary option, 21-week runway)

## Key References
- Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking (ICLR 2025)
- Preference Leakage: A Contamination Problem in LLM-as-a-judge (ICLR 2026)
- FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge (arXiv 2602.06625, Feb 2026)
- Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines (arXiv 2026)
- Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization (arXiv 2026)
- RATE: Causal Explainability of Reward Models with Imperfect Counterfactuals (ICML 2025)
- Double/Debiased Machine Learning for Treatment and Structural Parameters (Chernozhukov et al., Econometrics Journal 2018)
- Causal Inference for Human-Language Model Collaboration (Choi et al., NAACL 2024)
- Adapting Text Embeddings for Causal Inference (Veitch, Sridhar & Blei, UAI 2020)
- Causal Effects of Linguistic Properties (Pryzant et al., NAACL 2021)
- A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents (CASSE, arXiv 2601.10809, Jan 2026)
- Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2025)
- Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (ICLR 2025)
- Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector (NeurIPS 2025)
- Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation (arXiv 2026)
- CausalPFN: Amortized Causal Effect Estimation via In-Context Learning (NeurIPS 2025)
- RubricBench: Aligning Model-Generated Rubrics with Human Standards (arXiv 2603.01562, March 2026)
- Estimating Causal Effects of Text Interventions Leveraging LLMs (Findings of AACL-IJCNLP 2025)
- Causal Effect Estimation with Latent Textual Treatments (arXiv 2026)
- How to Make Causal Inferences Using Texts (Egami et al., Science Advances 2022)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7d640c73-2c7a-4aca-8865-962f2cebf6fa",
  "type": "user",
  "uuid": "8bded759-8cbf-40db-a09a-be15d9c833f2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:44:15.590Z_

```json
{
  "parentUuid": "8bded759-8cbf-40db-a09a-be15d9c833f2",
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
  "uuid": "b0ada230-abc6-4408-abe0-6d62230551dd",
  "timestamp": "2026-05-20T04:44:15.590Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:44:15.590Z_

```json
{
  "parentUuid": "b0ada230-abc6-4408-abe0-6d62230551dd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2b21284a-734c-4f9f-9fc9-15207aa103cf",
  "timestamp": "2026-05-20T04:44:15.590Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make an informed assessment.…",
  "leafUuid": "2b21284a-734c-4f9f-9fc9-15207aa103cf",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal for LLM judge style debiasing method",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:44:45.475Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' independent evaluations and synthesize them as the Meta Judge.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 中
- Significance: 强
- Related Work: 强
- Probability: [28% - 40%] 中位 34%
- Main risks: Trivial alternative (multi-dim regression), 3-axis coverage + content leakage

**Reviewer 2:**
- Novelty: 中
- Significance: 中偏强


- Related Work: 强
- Probability: [28% - 38%] 中位 32%
- Main risks: Trivial alternative (multi-dim regression), Content-style inseparability

**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [23% - 33%] 中位 28%
- Main risks: Novelty judged incremental (RATE + DML = CSD), Trivial alternative performance

The three probability medians converge around 28-34%, averaging to roughly 31%, with consistent concerns about whether this represents a trivial extension of existing methods rather than a genuinely novel contribution. The key risks all three reviewers flagged are the trivial alternative threat from multi-dimensional regression, the entanglement between content and style, and insufficient coverage across the three axes—plus they all agree this is more about application novelty than methodological innovation. There are a few outliers: R3 mentions a specific related work that the others don't emphasize, R1 is slightly more optimistic on significance, and R3 is the most skeptical overall, but the high consistency suggests I should anchor near the median estimate.

Given the tight consensus around novelty being "中" and the strong agreement on related work coverage, I'm settling on a narrower interval around 32%, which is the median of the three estimates. The upper bound stays at 40% per the principle of not exceeding the most lenient reviewer, and with such low variance I can confidently compress the range to 26-36%.

Now I'm turning to the implementation assessment, looking at what the reviewers noted alongside the proposal's own resource breakdown: compute requirements around 100-220 A100 hours with associated costs, publicly available datasets across multiple benchmarks, a modest pilot study with human annotators, and inference-only usage of an existing model for counterfactual generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b21284a-734c-4f9f-9fc9-15207aa103cf",
  "isSidechain": false,
  "requestId": "req_011CbDDAg8tqMiWDdidpSvfj",
  "type": "assistant",
  "uuid": "42cd9f85-89c4-41df-a73f-ba1c65ee1167",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3mNfgAsRXr7UxeSnJ8b2j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19883,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3511,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 19883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19883
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

_source line 9 · 2026-05-20T04:45:43.356Z_

【阶段】: Meta Judge
【三次中位】: [34%, 32%, 28%]  std=2.5%
【共识维度】:
- **Novelty = 中**（3/3 一致）：核心贡献是 RATE double-rewrite + DML partially linear model 的组合应用于黑盒 judge style debiasing 新场景，属于 "known A + known B → new application" 型创新，方法论层面无根本性突破。Legitimacy-aware correction (α) 是最具原创性的贡献点，但本质是调参策略。
- **Related Work = 强**（3/3 一致）：覆盖极为全面，所有关键竞争者（FairJudge、RATE、LC-AlpacaEval、SOS-Bench、CASSE、BBE、Preference Leakage、ISE 等）均被引用且描述准确，差异化定位清晰。
- **Trivial Alternative 威胁真实且严重**（3/3 一致，均列为 #1 风险）：将 LC-AlpacaEval 的回归方法扩展到多维度（word count + formality score + markdown density 等 surface features）是零成本替代方案，如果 CSD 不能在实验中显著碾压这个 trivial baseline，7x 成本开销无法 justify，论文 contribution 叙事将被严重削弱。
- **Content-style 不可分性风险**（3/3 均提及）：CASSE 已证明 style features "deeply entangled"，改变 formality 几乎不可避免地改变 perceived expertise，BERTScore/NLI 可能无法检测 subtle content leakage，威胁因果识别的核心假设。
- **三轴覆盖度不足**（3/3 均提及）：仅选 formality/verbosity/formatting 三个轴，缺乏充分性论证（style bias 还包括 tone、confidence、hedging、vocabulary sophistication 等维度），如果三轴只解释部分 style bias variance，去偏效果上限受限。
- **Significance ≥ 中偏强**（3/3 一致）：问题本身非常重要，SOS-Bench 152K 数据点确认 style bias 是主导偏差（0.76-0.92），黑盒 judge debiasing 有明确实践需求，空白真实存在。

【异常维度】:
- R1 给 Significance "强"（vs. R2/R3 的"中偏强"）→ R1 略偏宽松，但差异不大，不构成实质分歧。
- R3 提到 "Counterfactual LLM-based Framework for Measuring Rhetorical Style (arXiv 2512.19908)" 作为方法论上的邻近工作（反事实风格重写已被探索），R2 也提及但判断影响不大，R1 未提及。该工作目标不同（style measurement vs. debiasing），不构成直接竞争，但进一步稀释了"反事实风格重写"这一技术组件的 novelty。降权处理：作为 Novelty 判断的辅助证据，不改变"中"的结论。
- R3 下界更低（23%），反映了对 "novelty 被判 incremental" 最坏情景的更保守估计。在高一致情况下，该偏差被中位吸收。

【最终概率】: [26% - 36%] 中位 31%
【一致性】: 高
【综合理由】:

三位审稿人在所有核心维度上高度一致（std=2.5% < 3%），形成了清晰的共识画面：

1. **Novelty 是天花板约束**（3/3 判"中"）。CSD 的每个技术组件（RATE double-rewrite、DML partially linear model、反事实风格重写）均有成熟先例，核心贡献在于组合与应用场景定义。这类 "principled combination" 在顶会审稿中通常被视为 solid but incremental，不会让审稿人感到 surprising。Novelty = 中 将 idea 天花板锁定在 ~38%，无论实验多完美也难以突破。

2. **Trivial alternative 是实际上界的关键约束**（3/3 共识的 #1 风险）。多维 surface feature 回归（LC-AlpacaEval 的自然扩展）是零成本替代方案。如果 CSD 与这个 trivial baseline 的差距小于 2-3 个百分点（审稿人会预期这种可能性不低），论文变成 "principled but unnecessary complexity"。这个结构性风险将实际上界从 ~38% 进一步压低到 ~36%。

3. **Significance 撑住下界**（3/3 均认可问题重要性）。Style bias 作为 LLM judge 的主导偏差已被充分实证，黑盒 model-agnostic 去偏方案确实有空白。即使实验结果一般，"第一个将因果反事实方法系统性应用于黑盒 judge 多维 style debiasing"的贡献仍有一定价值，不至于被直接拒稿。下界 26%。

4. **高一致性处理**：std=2.5% < 3%，取中位附近缩窄区间。三份中位的中位值为 32%，鉴于"宁缺毋滥"原则且 R3 的更保守估计有合理依据（对组合创新 novelty 的更严格标准），最终中位取 31%，略偏向严格方向。

【建议】: 边缘（中位 31%，接近但未达 36% 推荐阈值。idea 层面 Novelty = 中是核心瓶颈，需在发掘阶段尝试锐化 novelty angle；trivial alternative 威胁需在实验设计中直接面对。有优化空间但空间有限。）

【实施评估】:
- **计算资源**: 100–220 A100-80GB 小时（视实验模式而定）。GPU 成本 $250–550；商业 judge API 成本 $200–450（GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro）；GPT-4o-mini 内容验证 $100–200。总计算成本 $550–1,200，属于中等偏低水平，可行。
- **数据需求**: SOS-Bench、LLMBar、RewardBench、RubricBench 均为公开 benchmark，无数据获取障碍。反事实生成数据由 Qwen3-32B 自动生成，无需额外数据收集。
- **人工介入**: 需要 200-response pilot study，3 名标注员分别标注 content quality 和 presentation quality，预算 $800–1,200。另需 10% 反事实质量人工抽检。标注员招募和完成约需 2 周。人工需求可控但不可省略（是验证 legitimacy-aware correction 的关键证据）。
- **训练需求**: 主 pipeline 不需要模型训练（inference-only）。可选的 Stage 4 amortized predictor 需要训练轻量回归模型（线性探针），训练成本极低（~2 A100 小时）。DML 交叉拟合使用 gradient-boosted trees，计算量小。
- **新 Benchmark**: 不需要构建新 benchmark。评测使用现有公开 benchmark。
- **预估周期**: 手动模式 12–14 周；有 Claude API 辅助 9–11 周；全自动化 5–7 周。关键瓶颈是顺序依赖链（反事实生成 → 内容验证 → judge 评分 → DML 估计）和人工标注周期（~2 周）。以 proposal 列出的 AAAI 2027 deadline（2026.7.28）计，从现在起约 10 周，时间紧但在手动模式下可行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42cd9f85-89c4-41df-a73f-ba1c65ee1167",
  "isSidechain": false,
  "requestId": "req_011CbDDAg8tqMiWDdidpSvfj",
  "type": "assistant",
  "uuid": "9a44d255-2b90-4da8-8ac6-b278cfeacdfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3mNfgAsRXr7UxeSnJ8b2j",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19883,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3511,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3511,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 19883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19883
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make an informed assessment.…",
  "leafUuid": "9a44d255-2b90-4da8-8ac6-b278cfeacdfa",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal for LLM judge style debiasing method",
  "sessionId": "1aa66f20-d684-443a-bb5e-8ecc8081ddae"
}
```

---
