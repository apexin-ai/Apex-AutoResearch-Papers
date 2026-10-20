# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/74c081e8-daac-4892-9632-a68f43cd99a4.jsonl`
- **Structured JSON:** [`05a785b153a427f5f4ca.json`](../../sessions/05/05a785b153a427f5f4ca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:51:40.427Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:51:40.427Z",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to evaluate this proposal rigorously. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [Kaneko & Baldwin, \"Bits Leaked per Query\", arXiv 2510.17000] (NeurIPS 2025 Spotlight): \n  建立了单模型信息论攻击成本下界 N_min ≥ log₂(1/ε)/I_max。本 proposal 的 Pillar 1 直接建立在此基础上，声称将其推广到多 judge composition。论文已验证存在且描述准确。\n\n- [Robertson & Koyejo, \"Let's Measure Information Step-by-Step\", arXiv 2508.05469] (Under TMLR review, 2025): \n  提出 TVD-MI 框架，证明有界 f-divergence 在对抗攻击下保持多项式认证保证（Theorem 3.3），而 KL 等无界度量指数退化。本 proposal 将此从 pairwise 扩展到 N-agent。论文已验证，描述准确。\n\n- [Yang et al., \"Understanding Agent Scaling via Diversity\", arXiv 2602.03794] (ICLR 2026 Workshop AIMS): \n  信息论多智能体性能 scaling 框架，提出有效通道数 K*、residual uncertainty 以 (1-α_c)^{K*} 衰减。本 proposal 声称提供其\"adversarial dual\"。论文已验证，描述准确。注意这是 workshop paper，非主会。\n\n- [Turkmen et al., \"Don't Always Pick the Highest-Performing Model\", arXiv 2602.08003] (Feb 2026): \n  Gaussian copula 相关误差模型，证明信息论误差下限，三项 MI 分解。本 proposal 的 K_eff 公式直接由此推导。论文已验证，描述准确。注意这是 arXiv preprint，尚未被会议接收。\n\n- [Chen et al., \"Incentivizing Truthful Language Models via PEG\", arXiv 2505.13636] (NeurIPS 2025 Oral): \n  DMI-based peer elicitation，证明 dominant strategy truthfulness。proposal 中描述为 NeurIPS 2025，实际确认为 NeurIPS 2025 Oral，描述准确。\n\n- [Qiu et al., \"Truthfulness Despite Weak Supervision\", arXiv 2601.20299] (ICLR 2026): \n  Peer prediction 用于 LLM 评估/训练，BNE 保证。论文已验证，描述准确。\n\n- [Kim et al., \"Correlated Errors in Large Language Models\", arXiv 2506.07962] (ICML 2025): \n  350+ LLMs 误差相关性实证：60% pairwise agreement when both err，same-company +0.066，same-architecture +0.076。为 proposal 的 α regime 估计提供实证基础。论文已验证，描述准确。\n\n- [SoK on LLM-as-Judge Security, arXiv 2603.29403] (April 2026): \n  全面漏洞目录，开源模型 50-68% ASR，7-model committee 经验降低到 10-19% 但无形式化解释。论文已验证，与 proposal 描述一致。\n\n- 直接竞争工作搜索结果：**未发现任何已发表工作正式证明 N-judge manipulation cost 的信息论 scaling bounds**。现有工作要么关注单模型（Kaneko & Baldwin），要么关注 incentive compatibility（Chen et al., Qiu et al.），要么关注 task performance scaling（Yang et al.），但没有将这些 unified 为 adversarial manipulation cost 的形式化 scaling 结果。\n\n- 调研总结：LLM-as-judge 安全是一个活跃且重要的研究方向。现有工作在 (a) 单模型攻击成本下界、(b) peer prediction incentive compatibility、(c) task-performance diversity scaling、(d) 经验性 committee 防御 等方面分别取得进展，但确实缺乏将 manipulation cost 与可测量的 inter-judge 信号相关性形式化联系的理论。Proposal 的 gap 定位基本成立。\n\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative 是 **简单多数投票 (majority voting)**。SoK 已经表明 7-model committee 通过 majority voting 将 ASR 从 50-68% 降至 10-19%（约 4-5× 改善）。这是一个零理论、零额外设计成本的 baseline。\n\n本 proposal 的 certified bound 对 K=7 给出 2.65-3.7× 改善——**在数值上弱于 majority voting 的经验性改善**。Proposal 自身也承认了这一点，并诉诸\"certified robustness\"类比（类似 randomized smoothing 提供比 empirical defense 更保守但可证明的保证）。\n\n增量价值在于：(1) 形式化保证——即使面对未来未知攻击也成立；(2) 可计算的 per-evaluation robustness certificate；(3) 将 diversity scaling 理论从 task performance 推广到 adversarial manipulation。但这个增量价值的说服力取决于审稿人是否认同\"modest certified bound > strong empirical defense without guarantee\"的价值体系。在 certified adversarial robustness 社区这被接受，但在 NLP 社区这一价值主张的接受度尚不确定。\n\n**结论：存在有力的 trivial alternative，增量价值是 certifiability，但实际数值 margin 确实 modest。**\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中存在以下未经充分验证的假设：\n\n1. **Gaussian copula 等相关假设在对抗条件下仍然成立**：Turkmen et al. 的 copula 相关性（cross-family ρ~0.4-0.5）是在 benign evaluation 条件下测量的。但在 adversarial 攻击下，judges 的相关结构可能发生剧变——例如，所有 judges 可能对同一类型的 prompt injection 或 adversarial suffix 同等脆弱，使得 effective ρ 在攻击条件下远高于 benign 条件下的估计值。这意味着 α 可能在实际攻击中坍缩到接近 0，使 certified bound 接近 vacuous。**这是最关键的未验证假设。**\n\n2. **对抗操纵可以被建模为通过噪声信道的扰动**：proposal 将每个 judge 建模为从\"真实质量\"到评分的噪声信道，adversary 的操纵是信道扰动。但现实攻击（如 prompt injection、adversarial suffix）可能绕过信道模型——它们直接修改 judge 的输入而非扰动信道本身。SDPI 框架假设 adversary 的操纵受信道容量限制，但某些攻击可能 exploit 模型的具体漏洞而非通用信息论限制。\n\n3. **Equicorrelation 假设的可推广性**：closed-form 结果需要所有 pairwise MI 相等（I_max），而 Kim et al. 的数据明确表明 same-family 和 cross-family 相关性差异很大（ρ 从 0.4 到 0.8）。虽然 proposal 提供了 heterogeneous correlation 的弱化结果（g ≥ ½·λ_min(Σ)），但 λ_min-based bound 通常非常松散，可能实际上 vacuous。\n\n4. **从 single-model 到 multi-judge 的 composition 假设**：Kaneko & Baldwin 的单模型 bound 假设 adaptive adversary 在每次 query 中获取固定的 mutual information。Multi-judge 设置中 adversary 可以利用 judges 之间的信息泄漏（e.g., 一个 judge 的响应可能泄漏另一个 judge 的决策信息），这并非简单的独立信道 composition。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心贡献是将已有数学工具（SDPI from Polyanskiy & Wu 2017, Fano decomposition from Morishita et al. ICML 2022, Gaussian copula from Turkmen et al. 2026, √K scaling from Horvath et al. 2021, single-model bounds from Kaneko & Baldwin NeurIPS 2025）综合应用于新的问题设定（multi-judge adversarial manipulation cost）。经搜索确认，\"adversarial dual of diversity scaling\"这个特定联系在现有文献中确实未出现——这是一个真实的 novelty delta。\n   \n   但 novelty 的 **深度** 有限：(a) K_eff = 1+(K-1)·exp(-2·I_max) 本质上是等相关矩阵特征值的标准推导加上 ρ-to-MI 的变量替换；(b) √K 缩放直接来自 Horvath et al.；(c) 三个 pillar 中每一个都是已有工具的直接应用。这是 synthesis novelty 而非 fundamental novelty。核心发现（diverse judges → higher manipulation cost, modulated by correlation）在定性层面完全符合直觉。\n\n2. **Significance: 中** — \n   LLM-as-judge 安全是一个重要且 timely 的方向（SoK 2603.29403 的发现令人担忧，50-68% ASR）。形式化保证在原则上有价值。但显著性受限于：(a) certified bounds 在数值上弱于 trivial majority voting 的经验效果，这使得实际部署价值存疑；(b) 对 NLP 社区而言，\"certified robustness for evaluation\"这个概念是否足够 impactful 尚不明确——不同于 certified robustness for classification（模型被部署在安全关键场景），evaluation protocol 的 certifiability 需求可能被视为一个较小的问题；(c) 理论结果对已知经验现象（committee 降低 ASR）的解释力是正面的，但 \"formalizing what we already observed empirically\" 的 significance ceiling 有限。\n\n3. **Related Work: 强** — \n   这是 proposal 最突出的优势。引用了 20+ 篇高度相关的论文，覆盖面极广（information theory, peer prediction, certified robustness, empirical security, error correlation, collusion, multi-agent evaluation）。经验证的所有关键论文（Kaneko & Baldwin, Robertson & Koyejo, Yang et al., Turkmen et al., Chen et al., Qiu et al., Kim et al.）均真实存在且描述准确。Gap 定位清晰且经搜索确认基本成立。唯一的小瑕疵：Yang et al. 是 workshop paper（ICLR 2026 Workshop AIMS），而非主会论文，proposal 中已标注但在 framing 中将其与主会论文并列使用时可能被审稿人挑战其 authority。\n\n\n【概率估计】: [23% - 33%] 中位 28%\n\n【估计理由】: \nNovelty 是限制上界的主要维度。虽然 \"adversarial dual of diversity scaling\" 在特定联系层面确实新颖，但核心技术贡献是已有数学工具的综合应用，核心定性结论（多样性 judges 提高操纵成本，受相关性调节）完全符合直觉——如果结果为 positive，大多数审稿人会说 \"makes sense, I would have guessed the direction\"。Significance 因 certified bounds 在数值上弱于经验性 majority voting 而进一步受限——这使得\"为什么不直接用 majority voting\"成为一个难以完全回答的审稿问题。Related Work 的强势提升了下界（proposal 形式完善、定位清晰，不会因 coverage 问题被轻易拒绝）。\n\n从 rubric 对应：Novelty 中 + Significance 中 → idea 核心处于 \"方向正确、有真实 novelty delta，但核心发现不够 surprising\" 的 25-35% 区间。certified bounds 弱于 trivial baseline 的问题以及 Gaussian copula 在对抗条件下的假设风险进一步将中位数拉向区间下半部分。\n\n【主要风险】: \n1. **\"Why not just majority vote?\" 问题**：certified bounds (2.65-3.7×) 在数值上弱于 majority voting 的经验效果 (~4-5×)。审稿人可能认为 certifiability 的价值不足以弥补 practical margin 的差距，尤其在 NLP 社区（相比 ML safety/robustness 社区）对 formal certification 的重视程度较低的背景下。\n2. **Benign-condition correlation ≠ adversarial-condition correlation**：整个理论框架依赖于 benign 条件下测量的 ρ 值来 certify 对抗条件下的 manipulation cost，但 adversarial 攻击可能系统性地利用所有 judges 的共享弱点（如共享训练数据来源的 vulnerability），使得 effective ρ 在攻击下远高于预期，potentially 使 certified bound 接近 vacuous。这是一个 idea 层面的逻辑链漏洞，无法通过补实验解决。\n```\n\nSources:\n- [Bits Leaked per Query (Kaneko & Baldwin, NeurIPS 2025)](https://arxiv.org/abs/2510.17000)\n- [Let's Measure Information Step-by-Step (Robertson & Koyejo)](https://arxiv.org/abs/2508.05469)\n- [Understanding Agent Scaling via Diversity (Yang et al., ICLR 2026 Workshop)](https://arxiv.org/abs/2602.03794)\n- [Don't Always Pick the Highest-Performing Model (Turkmen et al.)](https://arxiv.org/abs/2602.08003)\n- [Incentivizing Truthful Language Models via PEG (Chen et al., NeurIPS 2025)](https://arxiv.org/abs/2505.13636)\n- [Truthfulness Despite Weak Supervision (Qiu et al., ICLR 2026)](https://arxiv.org/abs/2601.20299)\n- [Correlated Errors in Large Language Models (Kim et al., ICML 2025)](https://arxiv.org/abs/2506.07962)\n- [SoK on LLM-as-Judge Security](https://arxiv.org/abs/2603.29403)\n- [LLMs Cannot Reliably Judge (RobustJudge)](https://arxiv.org/abs/2506.09443)\n- [Certified Ensemble Robustness (Horvath et al.)](https://arxiv.org/abs/2106.06946)\n- [Certifying Joint Adversarial Robustness for Model Ensembles (Chiang et al.)](https://arxiv.org/abs/2004.10250)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **Robertson & Koyejo, \"Let's Measure Information Step-by-Step\" (arXiv 2508.05469, 2025, under TMLR review)**:\n   确认存在。提出 TVD-MI 框架，证明 bounded f-divergences（如 TVD）在对抗攻击下保持多项式认证保证（Theorem 3.3），而 KL 等 unbounded measures 指数退化。在对抗攻击下 AUC 达 0.70-0.77。本 proposal 声称从 pairwise 扩展到 N-judge——准确。但 Robertson & Koyejo 本身只做了 single/pairwise evaluator 理论，没有 multi-judge composition theory。\n\n2. **Kaneko & Baldwin, \"Bits Leaked per Query\" (NeurIPS 2025 Spotlight, arXiv 2510.17000)**:\n   确认存在且为 NeurIPS 2025 Spotlight。建立单模型攻击成本下界 N_min ≥ log₂(1/ε)/I_max。在 7 个 LLM 上验证。proposal 声称将此结果扩展到多 judge composition——定位准确，Kaneko & Baldwin 确实未涉及多 judge 组合。\n\n3. **Yang et al., \"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\" (ICLR 2026 Workshop AIMS, arXiv 2602.03794)**:\n   确认存在。建立 information-theoretic diversity scaling 框架：有效通道数 K* = 2^{H(ρ)}，残余不确定性以 (1-α_c)^{K*} 几何衰减。但该工作仅分析任务性能（information recovery），不涉及对抗操纵成本——proposal 的 \"adversarial dual\" framing 是准确的。注意：这是 workshop paper，非主会论文。\n\n4. **Turkmen et al., \"Don't Always Pick the Highest-Performing Model\" (arXiv 2602.08003, Feb 2026)**:\n   确认存在。Gaussian copula 相关误差模型，信息论 error floor Φ(Φ⁻¹(1-p)/√ρ)，三项 MI 分解。within-family ρ~0.7-0.8，cross-family ρ~0.4-0.5。proposal 借用其 copula 模型推导 K_eff——合理。但注意该论文本身是做 ensemble selection，不涉及 adversarial robustness。\n\n5. **Chen et al., \"Incentivizing Truthful Language Models via Peer Elicitation Games\" (NeurIPS 2025 Poster, arXiv 2505.13636)**:\n   确认存在。DMI-based dominant strategy truthfulness（Lemma 1），O(√T) regret bound，需要 n≥2 discriminators 和条件独立性。proposal 正确指出 PEG 没有分析条件独立假设违反时的退化行为。\n\n6. **Qiu et al., \"Truthfulness Despite Weak Supervision\" (ICLR 2026, arXiv 2601.20299)**:\n   确认存在。Peer prediction for LLM evaluation/training，BNE guarantees，inverse scaling property。proposal 正确定位其与本工作的差异（BNE vs. adversarial robustness，无多项式成本界）。\n\n7. **SoK on LLM-as-Judge Security (arXiv 2603.29403, April 2026)**:\n   确认存在。分析 863 篇论文，7-model diverse committee 将 ASR 从 50-68% 降至 10-19%——但无形式化解释。这是本 proposal 要解决的核心 empirical gap。\n\n8. **Horvath et al. (arXiv 2106.06946, ICLR 2022)**:\n   Randomized smoothing ensemble 通过方差减少实现 √K 型 certified radius improvement。这是 proposal 中 g(0) = 1/2（独立 judge）的直接 precedent。\n\n9. **直接竞争搜索**:\n   未找到任何已发表工作提供 formal N-judge manipulation cost scaling bounds as a function of measurable inter-judge correlation。这一 gap 看上去是真实存在的。\n\n- **调研总结**: LLM-as-judge 安全领域正在快速发展：单模型攻击成本界（Kaneko & Baldwin）、single-evaluator 信息论框架（Robertson & Koyejo）、peer prediction 激励兼容（Qiu et al., Chen et al.）、多 agent 性能 scaling（Yang et al.）、ensemble 相关性建模（Turkmen et al.）均已就位。但\"多 judge 操纵成本的形式化 scaling law（作为可测相关性的函数）\"这一特定组合确实尚无人做。proposal 定位于将这些独立工具组合为统一的 certified manipulation-resistance 框架。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。**\n\n最直接的 trivial baseline 是 **simple majority voting**。SoK (2603.29403) 已经证实 7-model committee 将 ASR 从 50-68% 降至 10-19%（~4-5× empirical reduction），且零形式化——纯粹靠投票。proposal 的 certified bound 在 K=7、α=0.5 时给出 2.65× manipulation cost increase，在最乐观的 α=0.65 时给出 3.7×。\n\n也就是说：**简单多数投票在实证上已经比 proposal 的 certified bound 提供了更大的防护**。proposal 对此的回应是\"certifiability\"——certified bounds 即使数值modest，但提供了对任意未来攻击的 provable guarantee，而多数投票没有形式保证。\n\n这是一个合理的论点，但审稿人的直觉反应很可能是：\"certified bound 在数值上弱于无任何理论支持的 majority voting 经验结果，实际意义何在？\" 这类似于 randomized smoothing 在 adversarial robustness 领域的处境——理论优雅但 certified radii 远小于 empirical robustness margins。\n\n**增量价值在于**：(1) 形式化 certification——可量化每次 evaluation 的 manipulation-resistance guarantee；(2) correlation-aware bound——知道 when diversity helps and when it doesn't（而 majority voting 不知道）；(3) 对 judge 选择的指导——K_eff 公式可以指导如何组建最有效的 ensemble。但这些增量价值主要是理论性的，实际部署的吸引力有限。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有几个未经验证的关键假设：\n\n1. **Equicorrelated Gaussian copula 假设**：闭式结果依赖于 judge 信号遵循等相关 Gaussian copula。这是一个数学上方便但现实中可能不成立的假设。真实 judge 的相关结构可能是异质的（跨任务、跨 prompt 变化），且非 Gaussian 依赖结构（如 tail dependence）可能很重要。proposal 提供了更一般但更弱的结果（基于相关矩阵最小特征值），但核心narrative 和所有数值预测都基于 copula 假设。\n\n2. **对抗扰动通过独立通道传播的假设**：SDPI 组合论证假设对抗者的扰动通过各个 judge \"通道\"传播。但实际上，adversarial attacks 往往利用 judge 模型的**共享脆弱性**——例如 universal adversarial suffixes 可以同时欺骗多个模型，因为它们共享训练数据和类似的 tokenization。在这种情况下，有效独立通道数可能远低于 K_eff 预测。**这是最关键的未验证假设。**\n\n3. **先代模型的 ρ 估计适用于当代模型**：proposal 用 Turkmen et al.（2602.08003）的 cross-family ρ~0.4-0.5 和 Kim et al.（ICML 2025）的 350+ 模型相关性数据来估计 α。但这些数据来自较早一代模型。DeepSeek-V4、Qwen-3.5、Llama-4-Maverick 可能因为共享更多合成训练数据而更相关。proposal 承认了这一风险但没有提供缓解方案。\n\n4. **从 MI bound 到操纵成本的连接**：通过 Marton's inequality（TV² ≤ ½·KL）连接信息论 bound 到操作性操纵成本。这一步虽然数学上有效，但可能很松——Marton bound 通常不紧，导致 certified bound 过于保守。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** —\n   proposal 所声称的 gap 确实存在：调研确认没有任何已发表工作提供 formal N-judge manipulation cost scaling as a function of measurable correlation。这是真实的 novelty delta。\n   \n   然而，技术层面的 novelty 较为有限。核心推导是将已有数学工具进行组合：(a) Turkmen et al. 的 Gaussian copula → K_eff 公式（本质上是等相关矩阵的有效秩，这是教科书级线性代数）；(b) Horvath et al. 的 √K 方差减少 → g(0)=1/2 的 boundary condition；(c) SDPI 的乘法组合（Polyanskiy & Wu 2017 的直接应用）。每一步都是现有工具的 standard application，组合本身不需要深刻的新洞察。\n   \n   \"adversarial dual of diversity scaling\" 的概念框架是优雅的，但对于 information-theory literate 的审稿人来说，这个 duality 是相当自然的——同一个通道的容量（capacity）既决定了信息恢复速率，也决定了扰动成本。\n   \n   Qualitative result（\"更多样化的 judge = 更难操纵，且关系由相关性决定\"）是直觉上显而易见的。Quantitative closed form 是有用的，但不 surprising。\n\n2. **Significance: 中** —\n   问题的重要性毋庸置疑：LLM evaluation 安全是热门且重要的方向，SoK 的发现（50-68% ASR）凸显了紧迫性。形式化保证的缺失也是被广泛认可的 gap。\n   \n   然而，practical significance 受限于两个因素：\n   - Certified bounds 数值上弱于 empirical majority voting（2.65× vs. ~4-5× ASR reduction）——这降低了实际部署的吸引力\n   - 结果高度依赖 distributional assumptions（equicorrelated Gaussian copula），限制了可推广性\n   \n   对领域的影响路径也需审慎评估。如果结果 positive，审稿人大概率会说 \"I would have guessed that manipulation cost scales polynomially with effective independent judge count\"——定性结论是直觉预期的。定量贡献（K_eff 的闭式表达式）有用但不改变人们对问题的根本理解。\n   \n   与之对比，Kaneko & Baldwin 的 single-model bound 之所以获得 NeurIPS spotlight，部分原因是它量化了一个之前完全未知的量（per-query information leakage across disclosure regimes），且揭示了 \"few bits leak can collapse attack cost from quadratic to logarithmic\" 这一 surprising 的 threshold 效应。本 proposal 的 multi-judge composition 没有类似的 surprising threshold 或 phase transition。\n\n3. **Related Work: 强** —\n   Related work 覆盖是本 proposal 最强的维度。25+ 篇论文的引用，每一篇的定位和差异化都清晰且准确（调研验证了所有关键论文的存在性和描述准确性）。proposal 不仅引用了直接竞争者，还覆盖了 adjacent areas（peer prediction、ensemble robustness、behavioral entanglement、collusion fragility 等），展示了对整个研究生态的深入理解。\n   \n   gap 的识别是精准的：Robertson & Koyejo 做 single-evaluator 理论、Kaneko & Baldwin 做 single-model 攻击界、Yang et al. 做任务性能 scaling、Turkmen et al. 做 ensemble selection——没有人做 multi-judge manipulation cost scaling as f(correlation)。\n   \n   唯一的minor weakness：部分引用是 workshop papers（Yang et al. ICLR 2026 Workshop AIMS）或预印本，在正式审稿时可能需要注意措辞。\n\n---\n\n【概率估计】: [22% - 32%] 中位 27%\n\n【估计理由】:\n- **Related Work 强**（+）：gap 识别精准，定位清晰，无遗漏的直接竞争者\n- **Novelty 中**（限制上界）：技术贡献主要是现有工具的标准组合（copula 有效秩 + SDPI 组合 + √K 方差减少），缺少需要深刻新洞察的步骤。\"Adversarial dual\" 框架优雅但对信息论专家来说是自然的\n- **Significance 中**（限制上界）：定性结果直觉上可预期（\"更多样 = 更难操纵\"）；certified bound 数值上弱于 empirical majority voting；无 surprising threshold effect\n- 上界主要被 **Novelty** 和 **Significance** 共同限制：核心发现如果 positive，审稿人很可能说 \"I would have guessed this\" 而非 \"surprising\"\n- 下界受益于 gap 的真实性和 framing 的完整性——这不是一个 flawed idea，而是一个 solid but incremental 的理论贡献\n\n【主要风险】:\n1. **\"I would have guessed this\" 风险**：核心定性结论（多样 judge 的操纵成本多项式增长，指数取决于相关性）是直觉上可预期的。审稿人可能认为 formal proof 虽然正确但 incremental，特别是当每一步都是现有工具的标准应用时。这是最可能导致 reject 的 idea-level 风险。\n2. **Trivial alternative 被动性**：certified bound（K=7 时 2.65-3.7×）在数值上弱于 naive majority voting 的经验结果（~4-5× ASR reduction），审稿人可能认为 \"certifiability\" 的价值不足以弥补数值差距——特别是在 NLP/CL 社区（相比理论 CS 社区），empirical results 通常比 formal guarantees 更受重视。\n```\n\nSources:\n- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403)\n- [LLMs Cannot Reliably Judge (Yet?) - RobustJudge](https://arxiv.org/abs/2506.09443)\n- [Bits Leaked per Query - Kaneko & Baldwin](https://arxiv.org/abs/2510.17000)\n- [Let's Measure Information Step-by-Step - Robertson & Koyejo](https://arxiv.org/abs/2508.05469)\n- [Understanding Agent Scaling via Diversity - Yang et al.](https://arxiv.org/abs/2602.03794)\n- [Don't Always Pick the Highest-Performing Model - Turkmen et al.](https://arxiv.org/abs/2602.08003)\n- [Incentivizing Truthful Language Models via Peer Elicitation Games - Chen et al.](https://arxiv.org/abs/2505.13636)\n- [Truthfulness Despite Weak Supervision - Qiu et al.](https://arxiv.org/abs/2601.20299)\n- [Boosting Randomized Smoothing with Variance Reduced Classifiers - Horvath et al.](https://www.sri.inf.ethz.ch/blog/smoothens)\n- [MBZUAI - How many queries to break an AI?](https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research data. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- Robertson & Koyejo, \"Let's Measure Information Step-by-Step\" (arXiv 2508.05469, under TMLR review): 确认存在。提出TVD-MI框架用于无标签LLM评估，证明有界f-散度（TVD）在对抗操纵下维持多项式认证保证（Theorem 3.3），AUC 0.70-0.77。是本proposal的直接基础工作，但仅处理pairwise评估，无多评判者理论。\n- Kaneko & Baldwin, \"Bits Leaked per Query\" (arXiv 2510.17000, NeurIPS 2025 spotlight): 确认存在。建立单模型信息论攻击成本下界 N_min ≥ log₂(1/ε)/I_max，验证跨7个LLM。是本proposal的单通道基础，proposal声称将其扩展到多评判者组合——这一扩展方向确实尚未被该论文覆盖。\n- Yang et al., \"Understanding Agent Scaling via Diversity\" (arXiv 2602.03794, ICLR 2026 Workshop): 确认存在。建立信息论多智能体性能缩放框架，有效通道数K* = 2^{H(ρ)}，残差不确定性以(1-α_c)^{K*}几何收缩。处理任务性能而非对抗鲁棒性——proposal声称提供\"对抗对偶\"。\n- Turkmen et al., \"Don't Always Pick the Highest-Performing Model\" (arXiv 2602.08003, Feb 2026): 确认存在。Gaussian copula相关误差模型，MI分解（accuracy-redundancy-error correlation），证明信息论误差下限。经验发现跨家族ρ~0.4-0.5。proposal使用其copula模型推导K_eff公式。\n- Chen et al., \"Peer Elicitation Games\" (arXiv 2505.13636, NeurIPS 2025): 确认存在。DMI评分的多智能体对等引出，dominant strategy truthfulness，O(√T) regret bound。但不分析条件独立性违反时的退化——proposal声称填补此缝隙。\n- Kim et al., \"Correlated Errors in LLMs\" (arXiv 2506.07962, ICML 2025): 确认存在。350+ LLM大规模经验研究，60%两模型同时出错时一致（vs 33%基线），same-company +0.066, same-architecture +0.076。为proposal的α估计提供经验基础。\n- SoK on LLM-as-Judge Security (arXiv 2603.29403, April 2026): 确认存在。全面漏洞分类，开源模型50-68% ASR，7模型委员会降至10-19%但无形式解释。\n- Horvath et al. (arXiv 2106.06946, 2021): 随机平滑集成实现√K型认证半径改进。是proposal中独立评判者√K缩放的直接先例。\n- Chen et al. (arXiv 2107.10873, 2021): 证明多样化梯度+大置信度边距是认证集成鲁棒性的充要条件。\n- **未找到直接竞争工作**: 多次搜索未发现任何已发表工作明确提供\"多评判者操纵成本作为评判者间信号相关性的显式函数\"这一结果。gap claim在当前文献中基本成立。\n\n- 调研总结: LLM-as-Judge安全是2025-2026的热门方向，经验性工作丰富（SoK, RobustJudge, 各种攻击/防御），但形式化理论工作稀缺。Robertson & Koyejo的TVD-MI和Kaneko & Baldwin的单模型信息论界是仅有的两个严格理论框架，均未扩展到多评判者设置。Yang et al.和Turkmen et al.从性能侧提供了多智能体/集成的信息论框架，但未涉及对抗鲁棒性。Proposal处于这些理论线之间的真实空白地带。\n\n【Trivial Alternative 检验】:\n最直接的trivial alternative是**简单多数投票（majority voting）**。SoK已经报告K=7的多数投票将ASR从50-68%降至10-19%——这是一个~4-5×的经验改善，无需任何理论框架。Proposal的认证界在K=7时给出2.65-3.7×操纵成本增加，**数值上甚至不如多数投票的经验改善幅度**。\n\nProposal对此的辩护是\"认证 vs. 经验\"类比（类似randomized smoothing）：认证界虽然modest但对未来未知攻击有保证，而经验ASR可能被自适应攻击突破。这个辩护逻辑上成立，但有两个问题：\n1. **认证界的实际效用取决于威胁模型的精确性**。Randomized smoothing的认证半径是在精确定义的ℓ₂扰动模型下的。本proposal的\"操纵成本\"定义较模糊——是查询次数？扰动幅度？这直接影响认证的可操作性。\n2. **如果多数投票的经验表现已经很好，认证的增量价值有限**。实践中，部署者可能直接用多数投票+经验监控，而非部署一个理论上更\"认证\"但经验ASR相当的系统。\n\n**结论**: Trivial alternative确实存在且有竞争力。Proposal的增量价值主要在于**形式保证**而非**实际性能提升**，这将是审稿人的主要质疑点。\n\n【前提假设检验】:\n核心claim的逻辑链有以下未经验证的关键假设：\n\n1. **等相关Gaussian copula假设**: K_eff闭式公式依赖于所有评判者对之间的MI相等（equicorrelation）。真实评判者间的相关性是异质的（Kim et al.的数据本身就显示same-company vs. cross-company的显著差异）。Proposal承认了这一点并给出了更弱的一般性结果（g ≥ ½·λ_min(Σ)），但这个bound可能过松而缺乏实用价值。\n\n2. **\"对抗对偶\"的数学严谨性**: Proposal声称建立了Yang et al.任务性能缩放的\"对抗对偶\"。但Yang et al.的框架处理的是信息恢复（从K个通道恢复关于Y的信息），而对抗鲁棒性处理的是信息扰动成本（迫使K个通道的聚合结果偏离真值）。这两者之间的对偶关系不是数学上的严格对偶（如LP对偶），而更像是概念类比。如果审稿人追问\"对偶在什么形式意义上成立\"，proposal可能难以给出令人满意的答案。\n\n3. **SDPI contraction的可组合性假设**: Pillar 1声称SDPI contraction coefficients在独立通道间乘法组合。但评判者之间有相关性时，它们不是独立通道。Proposal通过引入K_eff来\"折算\"为等效独立通道数，但这个从相关通道到K_eff个独立通道的约化步骤本身需要严格证明——proposal未提供这一步的proof sketch。\n\n4. **三支柱的组合完整性**: SDPI（Pillar 1）提供perturbation decay bound，Fano分解（Pillar 2）提供MI分解，Gaussian copula（Pillar 3）提供闭式K_eff。但proposal未清晰说明这三个结果如何**数学地组合**为最终的Ω(K^{g(I_max)})定理。这是一个proof strategy而非proof——从strategy到完整proof之间可能存在非trivial的技术困难。\n\n5. **α估计的时效性**: ρ~0.4-0.5的经验估计来自Turkmen et al.和Kim et al.的数据，基于前代模型。Proposal选择的DeepSeek-V4-Flash、Qwen-3.5、Llama-4-Maverick是更新的模型，由于共享训练数据趋同（Common Crawl、合成数据）和架构趋同（均为MoE），实际ρ可能高于估计，导致α低于预期。Proposal对此有sensitivity分析，但acknowledge了这一风险。\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   理由: Gap identification是真实的——多次搜索确认无现有工作提供多评判者操纵成本作为评判者间相关性的显式函数。然而，核心技术贡献的novelty是**组合性的**而非**原创性的**：SDPI composition来自Polyanskiy & Wu (2017)，Fano分解来自Morishita et al. (ICML 2022)，Gaussian copula来自Turkmen et al. (2602.08003)，√K scaling来自Horvath et al. (2106.06946)。Proposal的novelty在于将这些已有工具组合应用到LLM评估对抗鲁棒性这一新设定。对于独立评判者，结果退化为√K——这正是randomized smoothing集成的已知结果。核心新颖点是\"√K如何随相关性退化\"的显式刻画，但这是一个可预见的结果方向（\"更相关的评判者→更少的有效冗余→更低的鲁棒性增益\"）。审稿人可能评价为\"technically sound composition of known tools, but the qualitative insight is unsurprising.\"\n\n2. Significance: 【中偏强】\n   理由: LLM-as-Judge安全是一个timely且重要的问题，SoK (2603.29403)的全面漏洞目录和RobustJudge的15种攻击方法都证明了这一点。提供形式化理论框架来理解多评判者委员会为何有效（而非仅有经验观察）有genuine学术价值。如果理论能指导评估协议设计（如何选择评判者以最大化认证鲁棒性），实际影响也可期。但significance受限于：(a) 认证界在实际中可能过松（2.65-3.7× vs. 经验4-5×）；(b) 如果认证界被证明不tight，理论对实践的指导价值有限。\n\n3. Related Work: 【强】\n   理由: 这是proposal最强的方面。30+篇引用涵盖了所有主要研究线——Robertson & Koyejo的TVD-MI理论、Kaneko & Baldwin的单模型攻击成本界、Yang et al.的多智能体性能缩放、Turkmen et al.的copula模型、Chen et al.的PEG、Kim et al.的相关误差、SoK、认证集成鲁棒性文献等。差异化定位清晰，honest地承认了与每项工作的关系和差异。Proposal对每篇论文的描述与我的调研结果一致（所有检查的论文均真实存在，描述准确）。唯一minor issue是\"对抗对偶\"的positioning可能被审稿人认为对Yang et al.的框架做了过度类比。\n\n【概率估计】: [22% - 35%] 中位 28%\n\n【估计理由】:\n- Related Work的深度和gap identification的准确性为proposal建立了solid的研究定位（上推）\n- Significance因问题的timely性和理论框架的实际需求而较强（上推）\n- 但Novelty受限于\"组合已知工具，定性洞察可预见\"——如果核心发现是positive（√K随相关性退化），审稿人很可能说\"I would have guessed this\"而非\"surprising\"（下拉，这是限制上界的主要维度）\n- Trivial alternative（多数投票）的存在进一步限制了增量价值的说服力（下拉）\n- \"对抗对偶\"claim的数学严谨性和三支柱组合的proof gap是风险点（下拉）\n- 综合来看，这是一个solid incremental contribution，方向正确但内核不够surprising，处于25-35%区间的中下部\n\n【主要风险】:\n1. **\"Unsurprising\" criticism**: 核心结论\"独立评判者越多→操纵成本越高，但相关性越强则增益越小\"是直觉上显而易见的。审稿人可能认为将这个直觉形式化虽然有技术贡献，但定性上并无新发现（\"the theorem confirms what we already knew\"）。这是idea层面的根本风险。\n2. **认证界 vs. 经验表现的差距**: 如果认证界（2.65-3.7×）显著松于经验ASR降低（4-5×），审稿人可能质疑理论的实用价值——认证界如果vacuously loose，其\"对未来攻击的保证\"就不具备实际指导意义。这直接削弱了proposal的核心价值主张。\n```\n\nSources:\n- [Let's Measure Information Step-by-Step (Robertson & Koyejo)](https://arxiv.org/abs/2508.05469)\n- [Bits Leaked per Query (Kaneko & Baldwin)](https://arxiv.org/abs/2510.17000)\n- [Understanding Agent Scaling via Diversity (Yang et al.)](https://arxiv.org/abs/2602.03794)\n- [Don't Always Pick the Highest-Performing Model (Turkmen et al.)](https://arxiv.org/abs/2602.08003)\n- [Incentivizing Truthful Language Models via Peer Elicitation Games (Chen et al.)](https://arxiv.org/abs/2505.13636)\n- [Correlated Errors in Large Language Models (Kim et al.)](https://arxiv.org/abs/2506.07962)\n- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403)\n- [On the Certified Robustness for Ensemble Models and Beyond (Chen et al.)](https://arxiv.org/abs/2107.10873)\n- [Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al.)](https://arxiv.org/abs/2106.06946)\n- [Adversarial Attacks on LLM-as-a-Judge Systems](https://arxiv.org/abs/2504.18333)\n- [Investigating Vulnerability of LLM-as-a-Judge to Prompt-Injection](https://arxiv.org/abs/2505.13348)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure\n\n## Description\nLLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, via BNE; Chen et al., NeurIPS 2025, via dominant-strategy DMI), and Kaneko & Baldwin (NeurIPS 2025 spotlight) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling—the adversarial dual of the task-performance scaling recently established by Yang et al. (ICLR 2026 Workshop AIMS). We bridge this gap by proving that adversarial manipulation cost grows as Ω(K^{g(I_max)}) where g is an explicit decreasing function of inter-judge signal correlation, derived via a three-pillar proof strategy: (1) SDPI contraction composition (Polyanskiy & Wu) showing perturbation decays multiplicatively across independent channels; (2) Fano-ensemble decomposition (Morishita et al., ICML 2022) separating relevance, redundancy, and combination loss; (3) Gaussian-copula closed form—adapting Turkmen et al.'s equicorrelated model, we derive K_eff = 1+(K-1)·exp(-2·I_max). Under the copula model, g(I_max) = ½·log(K_eff)/log(K), which equals ½ for independent judges (matching √K certified radius scaling from randomized smoothing) and degrades gracefully with correlation. For cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025), providing certified manipulation-cost bounds of 2.6–3.7× for K=7. We frame this as certifiable robustness for LLM evaluation: just as certified adversarial defenses provide provable guarantees despite sometimes modest empirical margins, our protocol certifies per-evaluation manipulation-resistance bounds that hold against arbitrary future attacks—a guarantee majority voting fundamentally cannot provide. We validate against RobustJudge's 15 realistic attack methods, reporting certified bounds alongside empirical ASR, with sensitivity analysis for α ∈ [0.2, 0.8].\n\n## Core Problem\nCan we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against realistic adversarial attacks?\n\n## Opportunity\nRobertson & Koyejo (2025) established that bounded f-divergences like TVD maintain polynomial certification guarantees under adversarial manipulation while unbounded measures (KL) fail (Theorem 3.3), and multiple concurrent works have established peer prediction incentive-compatibility for LLM evaluation (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025). However, three critical gaps remain: (1) No existing work provides formal N-agent scaling results connecting manipulation cost to measurable inter-judge signal correlation—Robertson & Koyejo analyze pairwise evaluations without multi-judge aggregation theory, Qiu et al. provide no polynomial cost bounds tied to judge count, and Chen et al.'s PEG dominant-strategy guarantee requires conditional independence without characterizing degradation under partial correlation; (2) Empirical validation uses only generic semantic-preserving transforms or deceptive finetuning, not realistic attack vectors documented by the SoK (prompt injection ASR 50–68%, adversarial suffixes, strategic vote rigging); (3) The information-theoretic diversity-scaling framework of Yang et al. (ICLR 2026 Workshop AIMS) shows that multi-agent system performance is bounded by effective channel count K* with residual uncertainty decaying as (1-α_c)^{K*}, but this addresses task performance, not adversarial manipulation resistance—no work establishes the dual result for manipulation cost. Meanwhile, Turkmen et al. (2602.08003) prove that correlated ensembles hit an irreducible error floor Φ(Φ⁻¹(1-p)/√ρ) under their Gaussian copula model, and their three-term MI decomposition (accuracy - redundancy + error correlation) provides the mathematical toolkit for our α estimation. Kaneko & Baldwin (NeurIPS 2025 spotlight) prove tight single-model information-theoretic attack cost bounds N_min ≥ log₂(1/ε)/I_max via Fano inequality, but do not address multi-judge composition. The SoK (2603.29403) finds that 7-model committees empirically reduce ASR to 10–19% but provides no formal explanation. We aim to bridge these gaps by providing the adversarial-robustness dual of the task-performance scaling theory, yielding certifiable manipulation-resistance bounds analogous to certified adversarial robustness in classification.\n\n## Landscape\nRobertson & Koyejo's 'Let's Measure Information Step-by-Step' (arXiv 2508.05469, under TMLR review) formalizes LLM evaluation as an information elicitation game using TVD-MI, proves that bounded f-divergences maintain polynomial certification guarantees under mode-collapse attacks (Theorem 3.3) while unbounded measures like KL degrade exponentially, and demonstrates TVD-MI effectiveness (AUC 0.70–0.77) under generic semantic transforms. Their Identity-Link IRT follow-up (2510.14966) extends to sparse evaluation with two-judge validation (Spearman ρ=0.872) but without formal multi-judge theory.\n\nQiu et al.'s 'Truthfulness Despite Weak Supervision' (ICLR 2026, 2601.20299) applies peer prediction to LLM evaluation/training with Bayesian Nash equilibrium guarantees (Theorem 1) and an empirical inverse scaling property, but targets output truthfulness rather than adversarial robustness of the evaluation protocol itself, acknowledges only unilateral deception (not collusion), and uses no information-theoretic divergence measures.\n\nChen et al.'s 'Incentivizing Truthful Language Models via Peer Elicitation Games' (NeurIPS 2025, 2505.13636) introduces multi-agent peer elicitation using Determinant Mutual Information (DMI) scoring and proves a strictly stronger result: dominant strategy truthfulness (Lemma 1), meaning truthful reporting is optimal regardless of other agents' strategies—not just in Bayesian Nash equilibrium. Their sublinear O(√T) regret bound (Theorem 2) and last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent provide a complementary theoretical foundation to Qiu et al.'s BNE. PEG requires n≥2 discriminators and K_t≥4 tasks with conditional independence (Assumption 4), and their experiments use 3 discriminators with the theoretical minimum n≥2 and K_t≥4 tasks required by Lemma 1. However, PEG does not characterize how its manipulation-resistance guarantees degrade when the conditional independence assumption is violated—precisely the regime we analyze.\n\nYang et al.'s 'Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity' (ICLR 2026 Workshop AIMS, 2602.03794) provides an information-theoretic framework where multi-agent system performance is bounded by intrinsic task uncertainty H(Y|X) with residual uncertainty decaying as (1-α_c)^{K*}, where α_c is the complementarity rate and K* = 2^{H(ρ)} is the effective channel count computed via von Neumann entropy of the embedding Gram matrix (Theorem 4.3). Their heterogeneity advantage corollary (Corollary 4.4) formally shows α_het·K_het > α_hom·K_hom implies strictly better performance. Critically, K* captures diversity in embedding space without labels and empirically correlates with accuracy (r=0.388 overall, r=0.535 for K*_c among correct agents). However, their framework addresses task performance (information recovery) not adversarial manipulation resistance (information perturbation cost). Our work establishes the adversarial dual: while their K* governs how quickly residual uncertainty decreases, our framework shows that the same correlation structure governs how quickly manipulation cost increases.\n\nTurkmen et al.'s 'Don't Always Pick the Highest-Performing Model' (arXiv 2602.08003, Feb 2026) formulates ensemble selection as MI maximization with a Gaussian-copula correlated error model and proves an information-theoretic error floor (Theorem 4.4): lim_{m→∞} P_e = Φ(Φ⁻¹(1-p)/√ρ) > 0 for equicorrelated ensembles with pairwise copula correlation ρ. Their three-term MI decomposition (Theorem 4.3)—Δ(j|S) = I(Y;X_j) - I(X_j;X_S) + I(E_j;E_S)—separates accuracy, redundancy, and error correlation. Empirically, they find within-family correlations ρ~0.7-0.8 and cross-family ρ~0.4-0.5. Their copula model provides the mathematical foundation for our derivation of effective independent channel count K_eff.\n\nKaneko & Baldwin's 'Bits Leaked per Query' (NeurIPS 2025 spotlight, arXiv 2510.17000) establishes tight information-theoretic bounds on adversarial attack costs against individual LLMs: any adaptive attack achieving error ≤ ε requires at least N_min ≥ log₂(1/ε)/I_max queries, where I_max is the maximum per-query mutual information leakage (Theorem 1), and this bound is achieved by sequential probability ratio tests (Theorem 2). Validated across 7 LLMs including Llama-4 and DeepSeek-R1, they identify four disclosure regimes (answer-only ~0.001-0.01 bits to full-access ~1.0+ bits). This provides the single-model information-theoretic attack cost foundation; our work extends the composition theory to multi-judge settings where an adversary must simultaneously fool K correlated judges.\n\nShen et al.'s 'Robust LLM Performance Certification via Constrained MLE' (arXiv 2604.03257, Google DeepMind/UCL, 2026) proposes constrained maximum likelihood estimation fusing human labels, LLM-judge annotations, and domain constraints (known TPR/FPR bounds) for certified LLM performance estimation. While addressing performance certification under benign judge noise, it assumes honest judges and does not model adversarial manipulation—precisely the threat model we address.\n\nFeng et al.'s 'Noisy but Valid' (ICLR 2026, arXiv 2601.20913) provides a statistical hypothesis testing framework for certifying LLM failure rates using imperfect judges, with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty. Using a small human-labeled calibration set to estimate judge TPR/FPR, they derive variance-corrected critical thresholds (Theorem 5.4 gives exact conditions for judge adoption). Like Shen et al., this assumes honest but fallible judges, not adversarial manipulation. Our work complements both: Shen et al. certify performance estimates via constrained MLE, Feng et al. certify statistical validity via hypothesis testing, and we certify manipulation resistance under adversarial attacks.\n\nJung & Na's 'Logarithmic Scores, Power-Law Discoveries' (arXiv 2604.00477, April 2026) identifies a score-coverage dissociation in multi-agent evaluation panels: scoring reliability (ICC) scales logarithmically with panel size N (R²=0.974) while unique issue discovery follows a sublinear power law y=7.8·N^0.69 (R²=0.999). Scores saturate ~2× faster than discoveries, with N=8 achieving 82% of maximum scoring reliability but only ~42% of N=32 discovery level. This has direct implications for our K-scaling claims: manipulation-cost scaling benefits may exhibit similar dissociation, where formal robustness guarantees saturate faster than empirical coverage of attack surface. We analyze this explicitly.\n\nThe SoK on LLM-as-Judge Security (2603.29403, April 2026) catalogs extensive vulnerabilities: open-source models showing 50–68% average ASR and frontier models 27–44%; 7-model diverse committees reduce ASR to 10–19% empirically but without formal explanation. RobustJudge (2506.09443) benchmarks 15 attack methods and 7 defense strategies. CAP (OpenReview 2026) shows comparative assessment is more robust than absolute scoring but provides no formal guarantees.\n\nOn error correlation and independence: Kim et al.'s 'Correlated Errors in Large Language Models' (ICML 2025, arXiv 2506.07962) shows 60% pairwise agreement when both err on Helm (vs. 33% random baseline), with same-company adding +0.066 and same-architecture adding +0.076 agreement. Chen et al.'s behavioral entanglement framework (arXiv 2604.07650) introduces BEI and CIG metrics across 18 LLMs from 6 families, finding cross-family entanglement 40–60% lower than intra-family.\n\nOn coordination failure: Frongillo et al. (2503.16280) prove that uninformative equilibria become unstable with fine-grained signals. Keppo et al.'s collusion fragility analysis (2603.20281) finds increasing LLM count from 2→5 breaks collusion (+22%→+3%), but same-family size heterogeneity stabilizes via leader-follower dynamics—motivating cross-family diversity.\n\nOn multi-agent evaluation: CollabEval (2603.00993) proposes three-phase multi-agent evaluation without formal adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, 2505.24239) uses credibility-based iterative aggregation for adversary resistance without information-theoretic measures.\n\nOn certified ensemble robustness: Chen et al. (2107.10873) prove that diversified gradient and large confidence margin are jointly necessary and sufficient for certified ensemble robustness—standard ensembles achieve only marginal improvements without explicit diversity. Horvath et al. (2106.06946) show randomized smoothing ensembles achieve √K-type certified radius improvement. These provide precedent for polynomial scaling bounds from diversity.\n\nTHE KEY GAP: No existing work provides formal N-agent manipulation-cost scaling results—the adversarial dual of Yang et al.'s task-performance scaling—where the bound is an explicit computable function of measurable inter-judge signal correlation, yielding certifiable robustness guarantees validated against realistic attacks. Kaneko & Baldwin provide the single-model attack cost foundation; we provide the multi-judge composition theory. Shen et al. and Feng et al. certify evaluation quality under noise; we certify resistance under adversarial attacks.\n\n## Approach\nWe extend Robertson & Koyejo's TVD-MI framework from pairwise evaluation to N-agent multi-judge settings with certifiable manipulation-resistance bounds, drawing on the Gaussian-copula correlation model (Turkmen et al.) and information-theoretic diversity scaling (Yang et al.) for the formal machinery, and extending Kaneko & Baldwin's single-model attack cost bounds to multi-judge composition. Our contribution has five components:\n\n**Component 1: Theoretical Framework—The Adversarial Dual of Diversity Scaling.**\n\nWe prove that when K judge models evaluate candidate responses using TVD-MI scoring, the adversarial manipulation cost grows as Ω(K^{g(I_max)}), where g is an explicit decreasing function of the maximum pairwise mutual information I_max between judge signals. This establishes the adversarial dual of Yang et al.'s task-performance result: while their Theorem 4.3 shows residual uncertainty decreases as (1-α_c)^{K*}, we show manipulation cost increases polynomially in K with exponent determined by the same underlying correlation structure.\n\n**Proof Strategy (Three-Pillar Approach):**\n\n*Pillar 1—Strong Data Processing Inequality (SDPI) Composition.* We model each judge as a noisy channel from the 'true quality' signal to an evaluation score. Following Polyanskiy & Wu (2017), SDPI contraction coefficients compose multiplicatively across independent channels: an adversary pushing perturbation through K independent channels experiences η^K total contraction, where η ∈ (0,1) is the per-channel contraction coefficient. Under inter-judge correlation, the effective number of independent channels is reduced from K to K_eff. This extends Kaneko & Baldwin's single-channel result (N_min ≥ log₂(1/ε)/I_max) to multi-channel settings: the adversary's total information gain across K correlated judges is bounded by K_eff · I_max per query round.\n\n*Pillar 2—Fano-Ensemble Decomposition.* Following Morishita et al. (ICML 2022), we decompose the total MI I(Y; Z_1,...,Z_K) available to the aggregator into K individual relevance terms, pairwise redundancy terms involving I_max, and combination loss terms. The adversary must reduce this total MI below the Fano threshold for correct decision-making, and the required perturbation energy is lower-bounded by the effective information.\n\n*Pillar 3—Gaussian Copula Closed Form.* Adapting Turkmen et al.'s equicorrelated Gaussian copula model (where Z_j = √ρ·U + √(1-ρ)·ξ_j with shared latent factor U), we derive the effective independent channel count:\n\n  K_eff = 1 + (K-1)·exp(-2·I_max)\n\nwhere I_max = -½ log(1-ρ²) is the pairwise MI under the copula model. This formula is our own derivation, obtained by computing the effective rank of the K×K correlation matrix under equicorrelation: eigenvalues are λ₁ = 1+(K-1)ρ (multiplicity 1) and λ₂ = 1-ρ (multiplicity K-1), and the effective independent dimensionality follows from the ratio of total to maximum variance, expressed as a function of MI via the ρ-to-I_max mapping ρ² = 1-exp(-2·I_max).\n\nThe manipulation cost lower bound is then Ω(K_eff^{1/2}) from variance-reduction arguments (following Horvath et al.'s √K certified radius scaling for randomized smoothing ensembles), giving:\n\n  g(I_max) = ½ · log(1 + (K-1)·exp(-2·I_max)) / log(K)\n\nThis satisfies the boundary conditions: g(0) = ½·log(K)/log(K) = ½ for fully independent judges (matching √K variance reduction), and g(I_max) → 0 as I_max → ∞ (fully correlated judges collapse to a single effective channel). The ½ exponent for independent judges is tight under the variance-reduction argument; if the SDPI chain yields linear rather than √K scaling, we get g(0) = 1.\n\n*Key Lemma (Connection from MI to Perturbation Budget):* We connect information-theoretic bounds to operational manipulation cost via Marton's inequality: TV(P,Q)² ≤ ½·KL(P||Q), combined with Robertson & Koyejo's Theorem 3.3 relating TVD-MI to certification bounds. The adversary's perturbation must overcome the TVD gap, which scales with √K_eff under the copula model.\n\n*Distributional Assumptions:* The closed-form result requires the equicorrelated Gaussian copula on judge signals (marginals can be arbitrary; only the dependence structure is Gaussian) and equicorrelation (all pairwise MIs equal I_max). We prove a weaker but more general result under arbitrary pairwise MI structure: g depends on the minimum eigenvalue of the correlation matrix, giving g ≥ ½·λ_min(Σ). For heterogeneous correlation, we use the effective rank of the correlation matrix (analogous to Yang et al.'s K* = 2^{H(ρ)}) as a tighter proxy.\n\n**Component 2: Practical α Regime Analysis with Sensitivity Bounds.**\n\nUsing Turkmen et al.'s empirical copula correlations (within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5) and Kim et al.'s correlated error data (same-company +0.066, same-architecture +0.076; ICML 2025, arXiv 2506.07962), we estimate for the proposed three-judge cross-family ensemble:\n\n- Central estimate: ρ ≈ 0.45, I_max ≈ 0.11, α = g(I_max) ∈ [0.35, 0.65]\n- At α=0.5, K=7: manipulation cost ≈ 7^0.5 ≈ 2.65× single-judge baseline\n- At α=0.65, K=7: manipulation cost ≈ 7^0.65 ≈ 3.7×\n\n*Sensitivity analysis and break-even:* We explicitly plan for the possibility that empirically measured α falls outside our predicted range, since current correlation data is from prior-generation models (Kim et al.'s 350+ mostly older LLMs, Chen et al.'s 18 models from prior families). DeepSeek-V4, Qwen-3.5, and Llama-4-Maverick may show different correlation structures due to shared training data evolution (Common Crawl, synthetic data from frontier models) and partial architectural convergence (all three use MoE, though with different routing and attention mechanisms).\n\n- If α = 0.2 (more correlated than expected, ρ ≈ 0.65): K=7 yields only 7^0.2 ≈ 1.55× cost increase. The protocol still provides formal guarantees that majority voting cannot, but the practical margin is thin. At this α, our protocol's value proposition is primarily the certifiability—analogous to how randomized smoothing provides modest certified radii but with provable guarantees.\n- If α = 0.8 (more independent than expected, ρ ≈ 0.25): K=7 yields 7^0.8 ≈ 5.2× cost increase—substantially better than baseline. This would indicate that cross-family diversity is even more effective than prior-generation data suggested.\n- Break-even analysis: Majority voting with K=7 achieves empirical ASR reduction from 50-68% to 10-19% (SoK), a ~4-5× reduction in success probability. Our protocol must provide comparable ASR reduction plus formal guarantees to be justified. We identify the critical α threshold where the certified bound becomes vacuous (i.e., the formal guarantee is weaker than the trivially achievable baseline): for K=7, this occurs at approximately α ≤ 0.05, corresponding to ρ ≥ 0.95 (near-identical judges). For any realistic cross-family ensemble, we are well above this threshold.\n- Diminishing returns analysis: Following Jung & Na's (2604.00477) finding that scoring reliability scales logarithmically while discovery scales as N^0.69, we analyze whether our manipulation-cost scaling exhibits similar dissociation. The formal certified bound may saturate faster (logarithmically in K) than the empirical ASR reduction (which may follow a power law), creating a gap between what we can certify and what we observe.\n\n**Component 3: Practical Protocol Design.**\n\nWe instantiate the framework as a deployable multi-judge evaluation protocol using three architecturally diverse open-weight model families—DeepSeek-V4-Flash (284B MoE, 13B active, Multi-head Latent Attention), Qwen-3.5 (397B MoE, 17B active), and Llama-4-Maverick (400B MoE, 17B active). These models are chosen because: (a) they come from three different organizations with different training data pipelines, minimizing same-company correlation (+0.066 per Kim et al.); (b) they use different architectural innovations, minimizing same-architecture correlation (+0.076); (c) Turkmen et al.'s copula framework predicts cross-family ρ~0.4-0.5 for such configurations.\n\nThe protocol operates in three phases:\n1. **Independence measurement:** Compute pairwise TVD-MI scores between all judge pairs on a calibration set; estimate the copula correlation ρ_ij and I_max; compute effective channel count K* (à la Yang et al.) and predicted α.\n2. **Evaluation with certified scoring:** Each judge evaluates candidates using TVD-MI; the aggregator combines scores via DMI-weighted aggregation (adapting PEG's determinant-based scoring from Chen et al., NeurIPS 2025), which provides dominant-strategy truthfulness (Lemma 1) when judges are approximately conditionally independent.\n3. **Certification:** Output both the aggregated evaluation and the certified manipulation-cost bound Ω(K^α) with the empirically measured α, constituting a per-evaluation robustness certificate.\n\nWe prove the coordination failure argument leveraging both PEG's dominant-strategy result (which applies under conditional independence) and Qiu et al.'s BNE framework (which applies under the weaker shared-prior assumption). For the regime between these extremes—partial correlation that violates conditional independence but maintains bounded MI—we provide interpolating bounds via the SDPI framework.\n\n**Component 4: Certifiable Robustness Framing.**\n\nWe explicitly frame our contribution as 'certifiable robustness for LLM evaluation,' drawing the analogy to certified adversarial robustness in classification (randomized smoothing, interval bound propagation). Just as certified adversarial defenses often achieve smaller empirical improvements than heuristic defenses but provide provable guarantees, our protocol may achieve ASR reductions comparable to majority voting but with formal certificates. The value proposition is:\n\n- Majority voting: empirically reduces ASR from ~60% to ~15% for K=7 (SoK), but with no formal guarantee—the ASR could spike under novel attacks.\n- Our protocol: achieves comparable empirical ASR reduction AND provides a formal lower bound on the manipulation cost that scales as Ω(K^α), certified per-evaluation. This means even against unforeseen future attacks, the manipulation cost is provably bounded below.\n- Connection to single-model bounds: Kaneko & Baldwin's N_min ≥ log₂(1/ε)/I_max provides the per-judge attack cost floor; our multi-judge composition shows that the adversary's total cost scales as K_eff times this single-judge bound, yielding certifiable multi-judge manipulation resistance.\n\nThis framing directly addresses the concern that 2.65-4.0× scaling may seem modest: in certified adversarial robustness, even modest certified radii are valued because they are provable, while large empirical margins can be broken by adaptive attacks.\n\n**Component 5: Realistic Adversarial Validation.**\n\nWe evaluate against RobustJudge's 15 attack methods (including PAIR, combined attacks, adversarial suffixes, and prompt injection) plus the SoK's documented attack vectors, on text summarization, code generation, and knowledge-intensive QA tasks. We benchmark against: (a) all 7 RobustJudge heuristic defenses; (b) CAP comparative augmented prompting; (c) CollabEval's consensus-based multi-agent approach; (d) Ebrahimi et al.'s credibility-scoring framework; (e) Robertson & Koyejo's single-evaluator TVD-MI baseline; (f) simple majority voting (K=3,5,7); (g) PEG with DMI scoring (Chen et al.). For each experimental condition, we report: (i) attack success rate, (ii) empirically measured ρ_ij and I_max, (iii) computed α, (iv) the gap between the certified manipulation-cost bound and the observed empirical manipulation cost, and (v) whether the formal bound is tight (ratio of empirical to certified). Following the score-coverage dissociation insight (Jung & Na), we separately analyze certification tightness (how close the formal bound is to the empirical one) and attack surface coverage (what fraction of attack types the bound holds against).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,000-1,500 H100-equivalent', 'timeline': '14-18 weeks', 'estimated_gpu_cost': '$2,500-$3,750 at $2.50/hr H100 spot', 'gpu_breakdown': 'DeepSeek-V4-Flash: 2×H100 FP8 (~160GB VRAM); Qwen-3.5: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB); Llama-4-Maverick: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB). Running all 3 simultaneously: 10×H100 (INT4) to 18×H100 (FP8). Per-experiment: single-judge baselines across 15 attacks × 3 tasks × 3 models ≈ 450 H100-hrs; multi-judge protocol evaluation across 45 conditions on 10-GPU cluster ≈ 500 H100-hrs; signal independence measurement, copula fitting, and α estimation ≈ 100 H100-hrs; ablations (K=1,2,3,5,7 judges, homogeneous vs. heterogeneous) ≈ 200 H100-hrs; development/debugging ≈ 150 H100-hrs'}, 'human_in_loop': {'gpu_hours': '800-1,200 H100-equivalent', 'timeline': '10-14 weeks', 'claude_api_cost': '$400-$600 (Sonnet 4.6 for code generation, proof assistance, paper drafting; ~130-200M tokens)', 'estimated_gpu_cost': '$2,000-$3,000 at $2.50/hr H100 spot', 'gpu_breakdown': 'Same per-model requirements; efficiency gains from Claude-assisted theorem proving, experiment scheduling, and copula fitting, reducing wasted debugging runs by ~20%'}, 'auto_research': {'gpu_hours': '1,200-1,800 H100-equivalent', 'timeline': '6-9 weeks', 'claude_api_cost': '$1,200-$2,000 (Opus 4.7 for theorem proving, SDPI chain verification, experiment design; ~250-400M tokens)', 'estimated_gpu_cost': '$3,000-$4,500 at $2.50/hr H100 spot', 'speed_bottleneck': 'The three-pillar proof strategy (SDPI + Fano + copula) has well-defined mathematical components that autonomous systems can work on in parallel, but ensuring the chain composes correctly across the three pillars requires human mathematical judgment. The key risk is that the SDPI contraction yields a weaker-than-expected bound, requiring fallback to the √K variance-reduction argument.'}}\n\n## Inspired By\nThe convergence of seven lines of work: (1) Robertson & Koyejo's bounded f-divergence theory for single-evaluator manipulation resistance; (2) The dual peer prediction results—Qiu et al.'s BNE and Chen et al.'s dominant-strategy PEG—providing complementary incentive-compatibility guarantees; (3) Yang et al.'s information-theoretic diversity-scaling framework establishing the task-performance scaling law via effective channel count K*—we provide the adversarial dual; (4) Turkmen et al.'s Gaussian-copula model with its error floor theorem and MI decomposition, which provides the mathematical foundation from which we derive our closed-form K_eff; (5) Kaneko & Baldwin's tight single-model information-theoretic attack cost bounds (N_min ≥ log₂(1/ε)/I_max), which we extend to multi-judge composition; (6) The SoK's empirical finding that 7-model committees reduce ASR to 10–19% without formal explanation; (7) The behavioral entanglement and correlated error literature (Chen et al. 2604.07650, Kim et al. ICML 2025) providing quantitative inter-judge independence measurements. We unify these into a certifiable manipulation-resistance framework where the certified bound is an explicit function of measurable signal correlation.\n\n## Target Venues\n- AAAI 2027 Main Technical Track (abstract: July 21, 2026; full paper: July 28, 2026; primary target—theory + experiments with certified robustness framing)\n- USENIX Security 2027 Cycle 1 (abstract: August 18, 2026; full paper: August 25, 2026; security-focused version emphasizing certifiable robustness against realistic attacks)\n- NeurIPS 2026 Workshops (contributed papers: ~August 29, 2026; workshop version connecting to the diversity-scaling and certified robustness communities)\n- ICLR 2027 (estimated deadline: October 2026; polished archival version with extended theory, comprehensive experiments, and tightness analysis)\n\n## Key References\n- Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes (Robertson & Koyejo, arXiv 2508.05469, 2025) — foundational TVD-MI theory, Theorem 3.3 polynomial certification bounds, primary work we extend\n- Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores (Robertson, arXiv 2510.14966, 2025) — sparse TVD-MI evaluation, two-judge preliminary validation\n- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (Qiu et al., ICLR 2026, 2601.20299) — BNE incentive-compatibility for LLM peer prediction, inverse scaling property\n- Incentivizing Truthful Language Models via Peer Elicitation Games (Chen et al., NeurIPS 2025, 2505.13636) — DMI-based multi-agent peer elicitation with dominant strategy truthfulness (Lemma 1), sublinear O(√T) regret bound (Theorem 2), last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent; experiments use 3 discriminators (n≥2 required by Lemma 1)\n- Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity (Yang et al., ICLR 2026 Workshop AIMS, 2602.03794) — information-theoretic diversity-scaling framework: effective channel count K* = 2^{H(ρ)}, residual uncertainty (1-α_c)^{K*} geometric contraction (Theorem 4.3), heterogeneity advantage (Corollary 4.4); we provide the adversarial dual of their task-performance result\n- Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection (Turkmen et al., arXiv 2602.08003, 2026) — Gaussian-copula correlated error model (Z_j = √ρ·U + √(1-ρ)·ξ_j), information-theoretic error floor Φ(Φ⁻¹(1-p)/√ρ) (Theorem 4.4), three-term MI decomposition into accuracy-redundancy-error correlation (Theorem 4.3); copula model provides the mathematical foundation from which we derive our K_eff formula\n- Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000) — tight single-model attack cost bound N_min ≥ log₂(1/ε)/I_max via K-ary Fano inequality (Theorem 1), achieved by SPRT (Theorem 2); validated across 7 LLMs including Llama-4 and DeepSeek-R1; provides single-channel foundation that we extend to multi-judge composition\n- Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation (Shen et al., arXiv 2604.03257, Google DeepMind/UCL, 2026) — constrained MLE fusing human labels, LLM-judge annotations, and domain constraints for certified performance estimation; addresses honest-judge noise, not adversarial manipulation; occupies adjacent 'certifiable evaluation' space\n- Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges (Feng, Shen, Balashankar, Gerner-Beuerle & Rodrigues, ICLR 2026, arXiv 2601.20913) — statistical hypothesis testing framework for LLM evaluation certification with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty; variance-corrected thresholds using judge TPR/FPR estimation; assumes honest but fallible judges, not adversarial manipulation; complements Shen et al. in the 'certifiable evaluation' space\n- Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation (Jung & Na, arXiv 2604.00477, 2026) — score-coverage dissociation: scoring reliability scales logarithmically, discovery follows power law N^0.69; informs our analysis of when certified bounds saturate vs. empirical gains\n- Security in LLM-as-a-Judge: A Comprehensive SoK (arXiv 2603.29403, April 2026) — comprehensive vulnerability catalog, 50-68% ASR on open-source, 7-model committee reduces ASR to 10-19%; primary empirical evidence for diversity benefit without formal explanation\n- LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge (arXiv 2506.09443, 2025) — RobustJudge benchmark, 15 attacks, 7 defenses, 12 models\n- Correlated Errors in Large Language Models (Kim, Garg, Peng & Garg, ICML 2025, arXiv 2506.07962) — error correlation across 350+ LLMs: 60% agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076; KEY for α regime analysis\n- How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026) — BEI and CIG metrics across 18 LLMs from 6 families; cross-family entanglement 40-60% lower than intra-family\n- Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences (arXiv 2602.11898, 2026) — 16-38% disagreement among top frontier models despite similar accuracy\n- Strong Data-Processing Inequalities for Channels and Bayesian Networks (Polyanskiy & Wu, arXiv 1508.06025, 2017) — SDPI contraction coefficients compose multiplicatively; foundational for our Pillar 1 proof strategy\n- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683) — decomposes Fano bound for ensembles into relevance, redundancy, and combination loss; foundational for our Pillar 2 proof strategy\n- On the Certified Robustness for Ensemble Models and Beyond (Chen et al., arXiv 2107.10873, 2021) — diversified gradient + large confidence margin jointly necessary and sufficient for certified ensemble robustness\n- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021) — ensemble variance reduction yields √K-type certified radius improvement; precedent for polynomial scaling from diversity\n- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020) — proves attack cost scales up with number of redundant signal copies; direct precedent for manipulation cost scaling with K\n- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026) — increasing LLM count 2→5 breaks collusion (+22%→+3%); same-family size heterogeneity stabilizes via leader-follower; motivates cross-family diversity\n- CollabEval: Multi-Agent Collaborative Evaluation (arXiv 2603.00993, March 2026) — three-phase multi-agent evaluation without formal adversarial guarantees\n- An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239) — credibility-based iterative aggregation; game-theoretic but not information-theoretic\n- Certifying Joint Adversarial Robustness for Model Ensembles (Chiang et al., arXiv 2004.10250, 2020) — vulnerability space disjointness for ensemble certification\n- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025) — fine-grained signals destabilize uninformative equilibria\n- Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)\n- Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)\n- am-ELO: A Stable Framework for Arena-based LLM Evaluation (ICML 2025 Poster)\n- CAP: Improving the Robustness of LLM-as-a-Judge Against Adversarial Score Manipulation via Comparative Augmented Prompting (OpenReview 2026)\n- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)\n- Can You Trick the Grader? Adversarial Persuasion of LLM Judges (EMNLP 2025 Findings)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:51:40.430Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:51:40.430Z",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T04:51:40.442Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to evaluate this proposal rigorously. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

- [Kaneko & Baldwin, "Bits Leaked per Query", arXiv 2510.17000] (NeurIPS 2025 Spotlight): 
  建立了单模型信息论攻击成本下界 N_min ≥ log₂(1/ε)/I_max。本 proposal 的 Pillar 1 直接建立在此基础上，声称将其推广到多 judge composition。论文已验证存在且描述准确。

- [Robertson & Koyejo, "Let's Measure Information Step-by-Step", arXiv 2508.05469] (Under TMLR review, 2025): 
  提出 TVD-MI 框架，证明有界 f-divergence 在对抗攻击下保持多项式认证保证（Theorem 3.3），而 KL 等无界度量指数退化。本 proposal 将此从 pairwise 扩展到 N-agent。论文已验证，描述准确。

- [Yang et al., "Understanding Agent Scaling via Diversity", arXiv 2602.03794] (ICLR 2026 Workshop AIMS): 
  信息论多智能体性能 scaling 框架，提出有效通道数 K*、residual uncertainty 以 (1-α_c)^{K*} 衰减。本 proposal 声称提供其"adversarial dual"。论文已验证，描述准确。注意这是 workshop paper，非主会。

- [Turkmen et al., "Don't Always Pick the Highest-Performing Model", arXiv 2602.08003] (Feb 2026): 
  Gaussian copula 相关误差模型，证明信息论误差下限，三项 MI 分解。本 proposal 的 K_eff 公式直接由此推导。论文已验证，描述准确。注意这是 arXiv preprint，尚未被会议接收。

- [Chen et al., "Incentivizing Truthful Language Models via PEG", arXiv 2505.13636] (NeurIPS 2025 Oral): 
  DMI-based peer elicitation，证明 dominant strategy truthfulness。proposal 中描述为 NeurIPS 2025，实际确认为 NeurIPS 2025 Oral，描述准确。

- [Qiu et al., "Truthfulness Despite Weak Supervision", arXiv 2601.20299] (ICLR 2026): 
  Peer prediction 用于 LLM 评估/训练，BNE 保证。论文已验证，描述准确。

- [Kim et al., "Correlated Errors in Large Language Models", arXiv 2506.07962] (ICML 2025): 
  350+ LLMs 误差相关性实证：60% pairwise agreement when both err，same-company +0.066，same-architecture +0.076。为 proposal 的 α regime 估计提供实证基础。论文已验证，描述准确。

- [SoK on LLM-as-Judge Security, arXiv 2603.29403] (April 2026): 
  全面漏洞目录，开源模型 50-68% ASR，7-model committee 经验降低到 10-19% 但无形式化解释。论文已验证，与 proposal 描述一致。

- 直接竞争工作搜索结果：**未发现任何已发表工作正式证明 N-judge manipulation cost 的信息论 scaling bounds**。现有工作要么关注单模型（Kaneko & Baldwin），要么关注 incentive compatibility（Chen et al., Qiu et al.），要么关注 task performance scaling（Yang et al.），但没有将这些 unified 为 adversarial manipulation cost 的形式化 scaling 结果。

- 调研总结：LLM-as-judge 安全是一个活跃且重要的研究方向。现有工作在 (a) 单模型攻击成本下界、(b) peer prediction incentive compatibility、(c) task-performance diversity scaling、(d) 经验性 committee 防御 等方面分别取得进展，但确实缺乏将 manipulation cost 与可测量的 inter-judge 信号相关性形式化联系的理论。Proposal 的 gap 定位基本成立。


【Trivial Alternative 检验】:

最直接的 trivial alternative 是 **简单多数投票 (majority voting)**。SoK 已经表明 7-model committee 通过 majority voting 将 ASR 从 50-68% 降至 10-19%（约 4-5× 改善）。这是一个零理论、零额外设计成本的 baseline。

本 proposal 的 certified bound 对 K=7 给出 2.65-3.7× 改善——**在数值上弱于 majority voting 的经验性改善**。Proposal 自身也承认了这一点，并诉诸"certified robustness"类比（类似 randomized smoothing 提供比 empirical defense 更保守但可证明的保证）。

增量价值在于：(1) 形式化保证——即使面对未来未知攻击也成立；(2) 可计算的 per-evaluation robustness certificate；(3) 将 diversity scaling 理论从 task performance 推广到 adversarial manipulation。但这个增量价值的说服力取决于审稿人是否认同"modest certified bound > strong empirical defense without guarantee"的价值体系。在 certified adversarial robustness 社区这被接受，但在 NLP 社区这一价值主张的接受度尚不确定。

**结论：存在有力的 trivial alternative，增量价值是 certifiability，但实际数值 margin 确实 modest。**


【前提假设检验】:

核心 claim 的逻辑链中存在以下未经充分验证的假设：

1. **Gaussian copula 等相关假设在对抗条件下仍然成立**：Turkmen et al. 的 copula 相关性（cross-family ρ~0.4-0.5）是在 benign evaluation 条件下测量的。但在 adversarial 攻击下，judges 的相关结构可能发生剧变——例如，所有 judges 可能对同一类型的 prompt injection 或 adversarial suffix 同等脆弱，使得 effective ρ 在攻击条件下远高于 benign 条件下的估计值。这意味着 α 可能在实际攻击中坍缩到接近 0，使 certified bound 接近 vacuous。**这是最关键的未验证假设。**

2. **对抗操纵可以被建模为通过噪声信道的扰动**：proposal 将每个 judge 建模为从"真实质量"到评分的噪声信道，adversary 的操纵是信道扰动。但现实攻击（如 prompt injection、adversarial suffix）可能绕过信道模型——它们直接修改 judge 的输入而非扰动信道本身。SDPI 框架假设 adversary 的操纵受信道容量限制，但某些攻击可能 exploit 模型的具体漏洞而非通用信息论限制。

3. **Equicorrelation 假设的可推广性**：closed-form 结果需要所有 pairwise MI 相等（I_max），而 Kim et al. 的数据明确表明 same-family 和 cross-family 相关性差异很大（ρ 从 0.4 到 0.8）。虽然 proposal 提供了 heterogeneous correlation 的弱化结果（g ≥ ½·λ_min(Σ)），但 λ_min-based bound 通常非常松散，可能实际上 vacuous。

4. **从 single-model 到 multi-judge 的 composition 假设**：Kaneko & Baldwin 的单模型 bound 假设 adaptive adversary 在每次 query 中获取固定的 mutual information。Multi-judge 设置中 adversary 可以利用 judges 之间的信息泄漏（e.g., 一个 judge 的响应可能泄漏另一个 judge 的决策信息），这并非简单的独立信道 composition。


【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是将已有数学工具（SDPI from Polyanskiy & Wu 2017, Fano decomposition from Morishita et al. ICML 2022, Gaussian copula from Turkmen et al. 2026, √K scaling from Horvath et al. 2021, single-model bounds from Kaneko & Baldwin NeurIPS 2025）综合应用于新的问题设定（multi-judge adversarial manipulation cost）。经搜索确认，"adversarial dual of diversity scaling"这个特定联系在现有文献中确实未出现——这是一个真实的 novelty delta。
   
   但 novelty 的 **深度** 有限：(a) K_eff = 1+(K-1)·exp(-2·I_max) 本质上是等相关矩阵特征值的标准推导加上 ρ-to-MI 的变量替换；(b) √K 缩放直接来自 Horvath et al.；(c) 三个 pillar 中每一个都是已有工具的直接应用。这是 synthesis novelty 而非 fundamental novelty。核心发现（diverse judges → higher manipulation cost, modulated by correlation）在定性层面完全符合直觉。

2. **Significance: 中** — 
   LLM-as-judge 安全是一个重要且 timely 的方向（SoK 2603.29403 的发现令人担忧，50-68% ASR）。形式化保证在原则上有价值。但显著性受限于：(a) certified bounds 在数值上弱于 trivial majority voting 的经验效果，这使得实际部署价值存疑；(b) 对 NLP 社区而言，"certified robustness for evaluation"这个概念是否足够 impactful 尚不明确——不同于 certified robustness for classification（模型被部署在安全关键场景），evaluation protocol 的 certifiability 需求可能被视为一个较小的问题；(c) 理论结果对已知经验现象（committee 降低 ASR）的解释力是正面的，但 "formalizing what we already observed empirically" 的 significance ceiling 有限。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。引用了 20+ 篇高度相关的论文，覆盖面极广（information theory, peer prediction, certified robustness, empirical security, error correlation, collusion, multi-agent evaluation）。经验证的所有关键论文（Kaneko & Baldwin, Robertson & Koyejo, Yang et al., Turkmen et al., Chen et al., Qiu et al., Kim et al.）均真实存在且描述准确。Gap 定位清晰且经搜索确认基本成立。唯一的小瑕疵：Yang et al. 是 workshop paper（ICLR 2026 Workshop AIMS），而非主会论文，proposal 中已标注但在 framing 中将其与主会论文并列使用时可能被审稿人挑战其 authority。


【概率估计】: [23% - 33%] 中位 28%

【估计理由】: 
Novelty 是限制上界的主要维度。虽然 "adversarial dual of diversity scaling" 在特定联系层面确实新颖，但核心技术贡献是已有数学工具的综合应用，核心定性结论（多样性 judges 提高操纵成本，受相关性调节）完全符合直觉——如果结果为 positive，大多数审稿人会说 "makes sense, I would have guessed the direction"。Significance 因 certified bounds 在数值上弱于经验性 majority voting 而进一步受限——这使得"为什么不直接用 majority voting"成为一个难以完全回答的审稿问题。Related Work 的强势提升了下界（proposal 形式完善、定位清晰，不会因 coverage 问题被轻易拒绝）。

从 rubric 对应：Novelty 中 + Significance 中 → idea 核心处于 "方向正确、有真实 novelty delta，但核心发现不够 surprising" 的 25-35% 区间。certified bounds 弱于 trivial baseline 的问题以及 Gaussian copula 在对抗条件下的假设风险进一步将中位数拉向区间下半部分。

【主要风险】: 
1. **"Why not just majority vote?" 问题**：certified bounds (2.65-3.7×) 在数值上弱于 majority voting 的经验效果 (~4-5×)。审稿人可能认为 certifiability 的价值不足以弥补 practical margin 的差距，尤其在 NLP 社区（相比 ML safety/robustness 社区）对 formal certification 的重视程度较低的背景下。
2. **Benign-condition correlation ≠ adversarial-condition correlation**：整个理论框架依赖于 benign 条件下测量的 ρ 值来 certify 对抗条件下的 manipulation cost，但 adversarial 攻击可能系统性地利用所有 judges 的共享弱点（如共享训练数据来源的 vulnerability），使得 effective ρ 在攻击下远高于预期，potentially 使 certified bound 接近 vacuous。这是一个 idea 层面的逻辑链漏洞，无法通过补实验解决。
```

Sources:
- [Bits Leaked per Query (Kaneko & Baldwin, NeurIPS 2025)](https://arxiv.org/abs/2510.17000)
- [Let's Measure Information Step-by-Step (Robertson & Koyejo)](https://arxiv.org/abs/2508.05469)
- [Understanding Agent Scaling via Diversity (Yang et al., ICLR 2026 Workshop)](https://arxiv.org/abs/2602.03794)
- [Don't Always Pick the Highest-Performing Model (Turkmen et al.)](https://arxiv.org/abs/2602.08003)
- [Incentivizing Truthful Language Models via PEG (Chen et al., NeurIPS 2025)](https://arxiv.org/abs/2505.13636)
- [Truthfulness Despite Weak Supervision (Qiu et al., ICLR 2026)](https://arxiv.org/abs/2601.20299)
- [Correlated Errors in Large Language Models (Kim et al., ICML 2025)](https://arxiv.org/abs/2506.07962)
- [SoK on LLM-as-Judge Security](https://arxiv.org/abs/2603.29403)
- [LLMs Cannot Reliably Judge (RobustJudge)](https://arxiv.org/abs/2506.09443)
- [Certified Ensemble Robustness (Horvath et al.)](https://arxiv.org/abs/2106.06946)
- [Certifying Joint Adversarial Robustness for Model Ensembles (Chiang et al.)](https://arxiv.org/abs/2004.10250)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **Robertson & Koyejo, "Let's Measure Information Step-by-Step" (arXiv 2508.05469, 2025, under TMLR review)**:
   确认存在。提出 TVD-MI 框架，证明 bounded f-divergences（如 TVD）在对抗攻击下保持多项式认证保证（Theorem 3.3），而 KL 等 unbounded measures 指数退化。在对抗攻击下 AUC 达 0.70-0.77。本 proposal 声称从 pairwise 扩展到 N-judge——准确。但 Robertson & Koyejo 本身只做了 single/pairwise evaluator 理论，没有 multi-judge composition theory。

2. **Kaneko & Baldwin, "Bits Leaked per Query" (NeurIPS 2025 Spotlight, arXiv 2510.17000)**:
   确认存在且为 NeurIPS 2025 Spotlight。建立单模型攻击成本下界 N_min ≥ log₂(1/ε)/I_max。在 7 个 LLM 上验证。proposal 声称将此结果扩展到多 judge composition——定位准确，Kaneko & Baldwin 确实未涉及多 judge 组合。

3. **Yang et al., "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" (ICLR 2026 Workshop AIMS, arXiv 2602.03794)**:
   确认存在。建立 information-theoretic diversity scaling 框架：有效通道数 K* = 2^{H(ρ)}，残余不确定性以 (1-α_c)^{K*} 几何衰减。但该工作仅分析任务性能（information recovery），不涉及对抗操纵成本——proposal 的 "adversarial dual" framing 是准确的。注意：这是 workshop paper，非主会论文。

4. **Turkmen et al., "Don't Always Pick the Highest-Performing Model" (arXiv 2602.08003, Feb 2026)**:
   确认存在。Gaussian copula 相关误差模型，信息论 error floor Φ(Φ⁻¹(1-p)/√ρ)，三项 MI 分解。within-family ρ~0.7-0.8，cross-family ρ~0.4-0.5。proposal 借用其 copula 模型推导 K_eff——合理。但注意该论文本身是做 ensemble selection，不涉及 adversarial robustness。

5. **Chen et al., "Incentivizing Truthful Language Models via Peer Elicitation Games" (NeurIPS 2025 Poster, arXiv 2505.13636)**:
   确认存在。DMI-based dominant strategy truthfulness（Lemma 1），O(√T) regret bound，需要 n≥2 discriminators 和条件独立性。proposal 正确指出 PEG 没有分析条件独立假设违反时的退化行为。

6. **Qiu et al., "Truthfulness Despite Weak Supervision" (ICLR 2026, arXiv 2601.20299)**:
   确认存在。Peer prediction for LLM evaluation/training，BNE guarantees，inverse scaling property。proposal 正确定位其与本工作的差异（BNE vs. adversarial robustness，无多项式成本界）。

7. **SoK on LLM-as-Judge Security (arXiv 2603.29403, April 2026)**:
   确认存在。分析 863 篇论文，7-model diverse committee 将 ASR 从 50-68% 降至 10-19%——但无形式化解释。这是本 proposal 要解决的核心 empirical gap。

8. **Horvath et al. (arXiv 2106.06946, ICLR 2022)**:
   Randomized smoothing ensemble 通过方差减少实现 √K 型 certified radius improvement。这是 proposal 中 g(0) = 1/2（独立 judge）的直接 precedent。

9. **直接竞争搜索**:
   未找到任何已发表工作提供 formal N-judge manipulation cost scaling bounds as a function of measurable inter-judge correlation。这一 gap 看上去是真实存在的。

- **调研总结**: LLM-as-judge 安全领域正在快速发展：单模型攻击成本界（Kaneko & Baldwin）、single-evaluator 信息论框架（Robertson & Koyejo）、peer prediction 激励兼容（Qiu et al., Chen et al.）、多 agent 性能 scaling（Yang et al.）、ensemble 相关性建模（Turkmen et al.）均已就位。但"多 judge 操纵成本的形式化 scaling law（作为可测相关性的函数）"这一特定组合确实尚无人做。proposal 定位于将这些独立工具组合为统一的 certified manipulation-resistance 框架。

---

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

最直接的 trivial baseline 是 **simple majority voting**。SoK (2603.29403) 已经证实 7-model committee 将 ASR 从 50-68% 降至 10-19%（~4-5× empirical reduction），且零形式化——纯粹靠投票。proposal 的 certified bound 在 K=7、α=0.5 时给出 2.65× manipulation cost increase，在最乐观的 α=0.65 时给出 3.7×。

也就是说：**简单多数投票在实证上已经比 proposal 的 certified bound 提供了更大的防护**。proposal 对此的回应是"certifiability"——certified bounds 即使数值modest，但提供了对任意未来攻击的 provable guarantee，而多数投票没有形式保证。

这是一个合理的论点，但审稿人的直觉反应很可能是："certified bound 在数值上弱于无任何理论支持的 majority voting 经验结果，实际意义何在？" 这类似于 randomized smoothing 在 adversarial robustness 领域的处境——理论优雅但 certified radii 远小于 empirical robustness margins。

**增量价值在于**：(1) 形式化 certification——可量化每次 evaluation 的 manipulation-resistance guarantee；(2) correlation-aware bound——知道 when diversity helps and when it doesn't（而 majority voting 不知道）；(3) 对 judge 选择的指导——K_eff 公式可以指导如何组建最有效的 ensemble。但这些增量价值主要是理论性的，实际部署的吸引力有限。

---

【前提假设检验】:

核心 claim 的逻辑链中有几个未经验证的关键假设：

1. **Equicorrelated Gaussian copula 假设**：闭式结果依赖于 judge 信号遵循等相关 Gaussian copula。这是一个数学上方便但现实中可能不成立的假设。真实 judge 的相关结构可能是异质的（跨任务、跨 prompt 变化），且非 Gaussian 依赖结构（如 tail dependence）可能很重要。proposal 提供了更一般但更弱的结果（基于相关矩阵最小特征值），但核心narrative 和所有数值预测都基于 copula 假设。

2. **对抗扰动通过独立通道传播的假设**：SDPI 组合论证假设对抗者的扰动通过各个 judge "通道"传播。但实际上，adversarial attacks 往往利用 judge 模型的**共享脆弱性**——例如 universal adversarial suffixes 可以同时欺骗多个模型，因为它们共享训练数据和类似的 tokenization。在这种情况下，有效独立通道数可能远低于 K_eff 预测。**这是最关键的未验证假设。**

3. **先代模型的 ρ 估计适用于当代模型**：proposal 用 Turkmen et al.（2602.08003）的 cross-family ρ~0.4-0.5 和 Kim et al.（ICML 2025）的 350+ 模型相关性数据来估计 α。但这些数据来自较早一代模型。DeepSeek-V4、Qwen-3.5、Llama-4-Maverick 可能因为共享更多合成训练数据而更相关。proposal 承认了这一风险但没有提供缓解方案。

4. **从 MI bound 到操纵成本的连接**：通过 Marton's inequality（TV² ≤ ½·KL）连接信息论 bound 到操作性操纵成本。这一步虽然数学上有效，但可能很松——Marton bound 通常不紧，导致 certified bound 过于保守。

---

【3 维度打分】:

1. **Novelty: 中** —
   proposal 所声称的 gap 确实存在：调研确认没有任何已发表工作提供 formal N-judge manipulation cost scaling as a function of measurable correlation。这是真实的 novelty delta。
   
   然而，技术层面的 novelty 较为有限。核心推导是将已有数学工具进行组合：(a) Turkmen et al. 的 Gaussian copula → K_eff 公式（本质上是等相关矩阵的有效秩，这是教科书级线性代数）；(b) Horvath et al. 的 √K 方差减少 → g(0)=1/2 的 boundary condition；(c) SDPI 的乘法组合（Polyanskiy & Wu 2017 的直接应用）。每一步都是现有工具的 standard application，组合本身不需要深刻的新洞察。
   
   "adversarial dual of diversity scaling" 的概念框架是优雅的，但对于 information-theory literate 的审稿人来说，这个 duality 是相当自然的——同一个通道的容量（capacity）既决定了信息恢复速率，也决定了扰动成本。
   
   Qualitative result（"更多样化的 judge = 更难操纵，且关系由相关性决定"）是直觉上显而易见的。Quantitative closed form 是有用的，但不 surprising。

2. **Significance: 中** —
   问题的重要性毋庸置疑：LLM evaluation 安全是热门且重要的方向，SoK 的发现（50-68% ASR）凸显了紧迫性。形式化保证的缺失也是被广泛认可的 gap。
   
   然而，practical significance 受限于两个因素：
   - Certified bounds 数值上弱于 empirical majority voting（2.65× vs. ~4-5× ASR reduction）——这降低了实际部署的吸引力
   - 结果高度依赖 distributional assumptions（equicorrelated Gaussian copula），限制了可推广性
   
   对领域的影响路径也需审慎评估。如果结果 positive，审稿人大概率会说 "I would have guessed that manipulation cost scales polynomially with effective independent judge count"——定性结论是直觉预期的。定量贡献（K_eff 的闭式表达式）有用但不改变人们对问题的根本理解。
   
   与之对比，Kaneko & Baldwin 的 single-model bound 之所以获得 NeurIPS spotlight，部分原因是它量化了一个之前完全未知的量（per-query information leakage across disclosure regimes），且揭示了 "few bits leak can collapse attack cost from quadratic to logarithmic" 这一 surprising 的 threshold 效应。本 proposal 的 multi-judge composition 没有类似的 surprising threshold 或 phase transition。

3. **Related Work: 强** —
   Related work 覆盖是本 proposal 最强的维度。25+ 篇论文的引用，每一篇的定位和差异化都清晰且准确（调研验证了所有关键论文的存在性和描述准确性）。proposal 不仅引用了直接竞争者，还覆盖了 adjacent areas（peer prediction、ensemble robustness、behavioral entanglement、collusion fragility 等），展示了对整个研究生态的深入理解。
   
   gap 的识别是精准的：Robertson & Koyejo 做 single-evaluator 理论、Kaneko & Baldwin 做 single-model 攻击界、Yang et al. 做任务性能 scaling、Turkmen et al. 做 ensemble selection——没有人做 multi-judge manipulation cost scaling as f(correlation)。
   
   唯一的minor weakness：部分引用是 workshop papers（Yang et al. ICLR 2026 Workshop AIMS）或预印本，在正式审稿时可能需要注意措辞。

---

【概率估计】: [22% - 32%] 中位 27%

【估计理由】:
- **Related Work 强**（+）：gap 识别精准，定位清晰，无遗漏的直接竞争者
- **Novelty 中**（限制上界）：技术贡献主要是现有工具的标准组合（copula 有效秩 + SDPI 组合 + √K 方差减少），缺少需要深刻新洞察的步骤。"Adversarial dual" 框架优雅但对信息论专家来说是自然的
- **Significance 中**（限制上界）：定性结果直觉上可预期（"更多样 = 更难操纵"）；certified bound 数值上弱于 empirical majority voting；无 surprising threshold effect
- 上界主要被 **Novelty** 和 **Significance** 共同限制：核心发现如果 positive，审稿人很可能说 "I would have guessed this" 而非 "surprising"
- 下界受益于 gap 的真实性和 framing 的完整性——这不是一个 flawed idea，而是一个 solid but incremental 的理论贡献

【主要风险】:
1. **"I would have guessed this" 风险**：核心定性结论（多样 judge 的操纵成本多项式增长，指数取决于相关性）是直觉上可预期的。审稿人可能认为 formal proof 虽然正确但 incremental，特别是当每一步都是现有工具的标准应用时。这是最可能导致 reject 的 idea-level 风险。
2. **Trivial alternative 被动性**：certified bound（K=7 时 2.65-3.7×）在数值上弱于 naive majority voting 的经验结果（~4-5× ASR reduction），审稿人可能认为 "certifiability" 的价值不足以弥补数值差距——特别是在 NLP/CL 社区（相比理论 CS 社区），empirical results 通常比 formal guarantees 更受重视。
```

Sources:
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403)
- [LLMs Cannot Reliably Judge (Yet?) - RobustJudge](https://arxiv.org/abs/2506.09443)
- [Bits Leaked per Query - Kaneko & Baldwin](https://arxiv.org/abs/2510.17000)
- [Let's Measure Information Step-by-Step - Robertson & Koyejo](https://arxiv.org/abs/2508.05469)
- [Understanding Agent Scaling via Diversity - Yang et al.](https://arxiv.org/abs/2602.03794)
- [Don't Always Pick the Highest-Performing Model - Turkmen et al.](https://arxiv.org/abs/2602.08003)
- [Incentivizing Truthful Language Models via Peer Elicitation Games - Chen et al.](https://arxiv.org/abs/2505.13636)
- [Truthfulness Despite Weak Supervision - Qiu et al.](https://arxiv.org/abs/2601.20299)
- [Boosting Randomized Smoothing with Variance Reduced Classifiers - Horvath et al.](https://www.sri.inf.ethz.ch/blog/smoothens)
- [MBZUAI - How many queries to break an AI?](https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research data. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- Robertson & Koyejo, "Let's Measure Information Step-by-Step" (arXiv 2508.05469, under TMLR review): 确认存在。提出TVD-MI框架用于无标签LLM评估，证明有界f-散度（TVD）在对抗操纵下维持多项式认证保证（Theorem 3.3），AUC 0.70-0.77。是本proposal的直接基础工作，但仅处理pairwise评估，无多评判者理论。
- Kaneko & Baldwin, "Bits Leaked per Query" (arXiv 2510.17000, NeurIPS 2025 spotlight): 确认存在。建立单模型信息论攻击成本下界 N_min ≥ log₂(1/ε)/I_max，验证跨7个LLM。是本proposal的单通道基础，proposal声称将其扩展到多评判者组合——这一扩展方向确实尚未被该论文覆盖。
- Yang et al., "Understanding Agent Scaling via Diversity" (arXiv 2602.03794, ICLR 2026 Workshop): 确认存在。建立信息论多智能体性能缩放框架，有效通道数K* = 2^{H(ρ)}，残差不确定性以(1-α_c)^{K*}几何收缩。处理任务性能而非对抗鲁棒性——proposal声称提供"对抗对偶"。
- Turkmen et al., "Don't Always Pick the Highest-Performing Model" (arXiv 2602.08003, Feb 2026): 确认存在。Gaussian copula相关误差模型，MI分解（accuracy-redundancy-error correlation），证明信息论误差下限。经验发现跨家族ρ~0.4-0.5。proposal使用其copula模型推导K_eff公式。
- Chen et al., "Peer Elicitation Games" (arXiv 2505.13636, NeurIPS 2025): 确认存在。DMI评分的多智能体对等引出，dominant strategy truthfulness，O(√T) regret bound。但不分析条件独立性违反时的退化——proposal声称填补此缝隙。
- Kim et al., "Correlated Errors in LLMs" (arXiv 2506.07962, ICML 2025): 确认存在。350+ LLM大规模经验研究，60%两模型同时出错时一致（vs 33%基线），same-company +0.066, same-architecture +0.076。为proposal的α估计提供经验基础。
- SoK on LLM-as-Judge Security (arXiv 2603.29403, April 2026): 确认存在。全面漏洞分类，开源模型50-68% ASR，7模型委员会降至10-19%但无形式解释。
- Horvath et al. (arXiv 2106.06946, 2021): 随机平滑集成实现√K型认证半径改进。是proposal中独立评判者√K缩放的直接先例。
- Chen et al. (arXiv 2107.10873, 2021): 证明多样化梯度+大置信度边距是认证集成鲁棒性的充要条件。
- **未找到直接竞争工作**: 多次搜索未发现任何已发表工作明确提供"多评判者操纵成本作为评判者间信号相关性的显式函数"这一结果。gap claim在当前文献中基本成立。

- 调研总结: LLM-as-Judge安全是2025-2026的热门方向，经验性工作丰富（SoK, RobustJudge, 各种攻击/防御），但形式化理论工作稀缺。Robertson & Koyejo的TVD-MI和Kaneko & Baldwin的单模型信息论界是仅有的两个严格理论框架，均未扩展到多评判者设置。Yang et al.和Turkmen et al.从性能侧提供了多智能体/集成的信息论框架，但未涉及对抗鲁棒性。Proposal处于这些理论线之间的真实空白地带。

【Trivial Alternative 检验】:
最直接的trivial alternative是**简单多数投票（majority voting）**。SoK已经报告K=7的多数投票将ASR从50-68%降至10-19%——这是一个~4-5×的经验改善，无需任何理论框架。Proposal的认证界在K=7时给出2.65-3.7×操纵成本增加，**数值上甚至不如多数投票的经验改善幅度**。

Proposal对此的辩护是"认证 vs. 经验"类比（类似randomized smoothing）：认证界虽然modest但对未来未知攻击有保证，而经验ASR可能被自适应攻击突破。这个辩护逻辑上成立，但有两个问题：
1. **认证界的实际效用取决于威胁模型的精确性**。Randomized smoothing的认证半径是在精确定义的ℓ₂扰动模型下的。本proposal的"操纵成本"定义较模糊——是查询次数？扰动幅度？这直接影响认证的可操作性。
2. **如果多数投票的经验表现已经很好，认证的增量价值有限**。实践中，部署者可能直接用多数投票+经验监控，而非部署一个理论上更"认证"但经验ASR相当的系统。

**结论**: Trivial alternative确实存在且有竞争力。Proposal的增量价值主要在于**形式保证**而非**实际性能提升**，这将是审稿人的主要质疑点。

【前提假设检验】:
核心claim的逻辑链有以下未经验证的关键假设：

1. **等相关Gaussian copula假设**: K_eff闭式公式依赖于所有评判者对之间的MI相等（equicorrelation）。真实评判者间的相关性是异质的（Kim et al.的数据本身就显示same-company vs. cross-company的显著差异）。Proposal承认了这一点并给出了更弱的一般性结果（g ≥ ½·λ_min(Σ)），但这个bound可能过松而缺乏实用价值。

2. **"对抗对偶"的数学严谨性**: Proposal声称建立了Yang et al.任务性能缩放的"对抗对偶"。但Yang et al.的框架处理的是信息恢复（从K个通道恢复关于Y的信息），而对抗鲁棒性处理的是信息扰动成本（迫使K个通道的聚合结果偏离真值）。这两者之间的对偶关系不是数学上的严格对偶（如LP对偶），而更像是概念类比。如果审稿人追问"对偶在什么形式意义上成立"，proposal可能难以给出令人满意的答案。

3. **SDPI contraction的可组合性假设**: Pillar 1声称SDPI contraction coefficients在独立通道间乘法组合。但评判者之间有相关性时，它们不是独立通道。Proposal通过引入K_eff来"折算"为等效独立通道数，但这个从相关通道到K_eff个独立通道的约化步骤本身需要严格证明——proposal未提供这一步的proof sketch。

4. **三支柱的组合完整性**: SDPI（Pillar 1）提供perturbation decay bound，Fano分解（Pillar 2）提供MI分解，Gaussian copula（Pillar 3）提供闭式K_eff。但proposal未清晰说明这三个结果如何**数学地组合**为最终的Ω(K^{g(I_max)})定理。这是一个proof strategy而非proof——从strategy到完整proof之间可能存在非trivial的技术困难。

5. **α估计的时效性**: ρ~0.4-0.5的经验估计来自Turkmen et al.和Kim et al.的数据，基于前代模型。Proposal选择的DeepSeek-V4-Flash、Qwen-3.5、Llama-4-Maverick是更新的模型，由于共享训练数据趋同（Common Crawl、合成数据）和架构趋同（均为MoE），实际ρ可能高于估计，导致α低于预期。Proposal对此有sensitivity分析，但acknowledge了这一风险。

【3 维度打分】:

1. Novelty: 【中】
   理由: Gap identification是真实的——多次搜索确认无现有工作提供多评判者操纵成本作为评判者间相关性的显式函数。然而，核心技术贡献的novelty是**组合性的**而非**原创性的**：SDPI composition来自Polyanskiy & Wu (2017)，Fano分解来自Morishita et al. (ICML 2022)，Gaussian copula来自Turkmen et al. (2602.08003)，√K scaling来自Horvath et al. (2106.06946)。Proposal的novelty在于将这些已有工具组合应用到LLM评估对抗鲁棒性这一新设定。对于独立评判者，结果退化为√K——这正是randomized smoothing集成的已知结果。核心新颖点是"√K如何随相关性退化"的显式刻画，但这是一个可预见的结果方向（"更相关的评判者→更少的有效冗余→更低的鲁棒性增益"）。审稿人可能评价为"technically sound composition of known tools, but the qualitative insight is unsurprising."

2. Significance: 【中偏强】
   理由: LLM-as-Judge安全是一个timely且重要的问题，SoK (2603.29403)的全面漏洞目录和RobustJudge的15种攻击方法都证明了这一点。提供形式化理论框架来理解多评判者委员会为何有效（而非仅有经验观察）有genuine学术价值。如果理论能指导评估协议设计（如何选择评判者以最大化认证鲁棒性），实际影响也可期。但significance受限于：(a) 认证界在实际中可能过松（2.65-3.7× vs. 经验4-5×）；(b) 如果认证界被证明不tight，理论对实践的指导价值有限。

3. Related Work: 【强】
   理由: 这是proposal最强的方面。30+篇引用涵盖了所有主要研究线——Robertson & Koyejo的TVD-MI理论、Kaneko & Baldwin的单模型攻击成本界、Yang et al.的多智能体性能缩放、Turkmen et al.的copula模型、Chen et al.的PEG、Kim et al.的相关误差、SoK、认证集成鲁棒性文献等。差异化定位清晰，honest地承认了与每项工作的关系和差异。Proposal对每篇论文的描述与我的调研结果一致（所有检查的论文均真实存在，描述准确）。唯一minor issue是"对抗对偶"的positioning可能被审稿人认为对Yang et al.的框架做了过度类比。

【概率估计】: [22% - 35%] 中位 28%

【估计理由】:
- Related Work的深度和gap identification的准确性为proposal建立了solid的研究定位（上推）
- Significance因问题的timely性和理论框架的实际需求而较强（上推）
- 但Novelty受限于"组合已知工具，定性洞察可预见"——如果核心发现是positive（√K随相关性退化），审稿人很可能说"I would have guessed this"而非"surprising"（下拉，这是限制上界的主要维度）
- Trivial alternative（多数投票）的存在进一步限制了增量价值的说服力（下拉）
- "对抗对偶"claim的数学严谨性和三支柱组合的proof gap是风险点（下拉）
- 综合来看，这是一个solid incremental contribution，方向正确但内核不够surprising，处于25-35%区间的中下部

【主要风险】:
1. **"Unsurprising" criticism**: 核心结论"独立评判者越多→操纵成本越高，但相关性越强则增益越小"是直觉上显而易见的。审稿人可能认为将这个直觉形式化虽然有技术贡献，但定性上并无新发现（"the theorem confirms what we already knew"）。这是idea层面的根本风险。
2. **认证界 vs. 经验表现的差距**: 如果认证界（2.65-3.7×）显著松于经验ASR降低（4-5×），审稿人可能质疑理论的实用价值——认证界如果vacuously loose，其"对未来攻击的保证"就不具备实际指导意义。这直接削弱了proposal的核心价值主张。
```

Sources:
- [Let's Measure Information Step-by-Step (Robertson & Koyejo)](https://arxiv.org/abs/2508.05469)
- [Bits Leaked per Query (Kaneko & Baldwin)](https://arxiv.org/abs/2510.17000)
- [Understanding Agent Scaling via Diversity (Yang et al.)](https://arxiv.org/abs/2602.03794)
- [Don't Always Pick the Highest-Performing Model (Turkmen et al.)](https://arxiv.org/abs/2602.08003)
- [Incentivizing Truthful Language Models via Peer Elicitation Games (Chen et al.)](https://arxiv.org/abs/2505.13636)
- [Correlated Errors in Large Language Models (Kim et al.)](https://arxiv.org/abs/2506.07962)
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403)
- [On the Certified Robustness for Ensemble Models and Beyond (Chen et al.)](https://arxiv.org/abs/2107.10873)
- [Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al.)](https://arxiv.org/abs/2106.06946)
- [Adversarial Attacks on LLM-as-a-Judge Systems](https://arxiv.org/abs/2504.18333)
- [Investigating Vulnerability of LLM-as-a-Judge to Prompt-Injection](https://arxiv.org/abs/2505.13348)


【原始 proposal（允许参考但不是主要依据）】:
# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure

## Description
LLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, via BNE; Chen et al., NeurIPS 2025, via dominant-strategy DMI), and Kaneko & Baldwin (NeurIPS 2025 spotlight) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling—the adversarial dual of the task-performance scaling recently established by Yang et al. (ICLR 2026 Workshop AIMS). We bridge this gap by proving that adversarial manipulation cost grows as Ω(K^{g(I_max)}) where g is an explicit decreasing function of inter-judge signal correlation, derived via a three-pillar proof strategy: (1) SDPI contraction composition (Polyanskiy & Wu) showing perturbation decays multiplicatively across independent channels; (2) Fano-ensemble decomposition (Morishita et al., ICML 2022) separating relevance, redundancy, and combination loss; (3) Gaussian-copula closed form—adapting Turkmen et al.'s equicorrelated model, we derive K_eff = 1+(K-1)·exp(-2·I_max). Under the copula model, g(I_max) = ½·log(K_eff)/log(K), which equals ½ for independent judges (matching √K certified radius scaling from randomized smoothing) and degrades gracefully with correlation. For cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025), providing certified manipulation-cost bounds of 2.6–3.7× for K=7. We frame this as certifiable robustness for LLM evaluation: just as certified adversarial defenses provide provable guarantees despite sometimes modest empirical margins, our protocol certifies per-evaluation manipulation-resistance bounds that hold against arbitrary future attacks—a guarantee majority voting fundamentally cannot provide. We validate against RobustJudge's 15 realistic attack methods, reporting certified bounds alongside empirical ASR, with sensitivity analysis for α ∈ [0.2, 0.8].

## Core Problem
Can we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against realistic adversarial attacks?

## Opportunity
Robertson & Koyejo (2025) established that bounded f-divergences like TVD maintain polynomial certification guarantees under adversarial manipulation while unbounded measures (KL) fail (Theorem 3.3), and multiple concurrent works have established peer prediction incentive-compatibility for LLM evaluation (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025). However, three critical gaps remain: (1) No existing work provides formal N-agent scaling results connecting manipulation cost to measurable inter-judge signal correlation—Robertson & Koyejo analyze pairwise evaluations without multi-judge aggregation theory, Qiu et al. provide no polynomial cost bounds tied to judge count, and Chen et al.'s PEG dominant-strategy guarantee requires conditional independence without characterizing degradation under partial correlation; (2) Empirical validation uses only generic semantic-preserving transforms or deceptive finetuning, not realistic attack vectors documented by the SoK (prompt injection ASR 50–68%, adversarial suffixes, strategic vote rigging); (3) The information-theoretic diversity-scaling framework of Yang et al. (ICLR 2026 Workshop AIMS) shows that multi-agent system performance is bounded by effective channel count K* with residual uncertainty decaying as (1-α_c)^{K*}, but this addresses task performance, not adversarial manipulation resistance—no work establishes the dual result for manipulation cost. Meanwhile, Turkmen et al. (2602.08003) prove that correlated ensembles hit an irreducible error floor Φ(Φ⁻¹(1-p)/√ρ) under their Gaussian copula model, and their three-term MI decomposition (accuracy - redundancy + error correlation) provides the mathematical toolkit for our α estimation. Kaneko & Baldwin (NeurIPS 2025 spotlight) prove tight single-model information-theoretic attack cost bounds N_min ≥ log₂(1/ε)/I_max via Fano inequality, but do not address multi-judge composition. The SoK (2603.29403) finds that 7-model committees empirically reduce ASR to 10–19% but provides no formal explanation. We aim to bridge these gaps by providing the adversarial-robustness dual of the task-performance scaling theory, yielding certifiable manipulation-resistance bounds analogous to certified adversarial robustness in classification.

## Landscape
Robertson & Koyejo's 'Let's Measure Information Step-by-Step' (arXiv 2508.05469, under TMLR review) formalizes LLM evaluation as an information elicitation game using TVD-MI, proves that bounded f-divergences maintain polynomial certification guarantees under mode-collapse attacks (Theorem 3.3) while unbounded measures like KL degrade exponentially, and demonstrates TVD-MI effectiveness (AUC 0.70–0.77) under generic semantic transforms. Their Identity-Link IRT follow-up (2510.14966) extends to sparse evaluation with two-judge validation (Spearman ρ=0.872) but without formal multi-judge theory.

Qiu et al.'s 'Truthfulness Despite Weak Supervision' (ICLR 2026, 2601.20299) applies peer prediction to LLM evaluation/training with Bayesian Nash equilibrium guarantees (Theorem 1) and an empirical inverse scaling property, but targets output truthfulness rather than adversarial robustness of the evaluation protocol itself, acknowledges only unilateral deception (not collusion), and uses no information-theoretic divergence measures.

Chen et al.'s 'Incentivizing Truthful Language Models via Peer Elicitation Games' (NeurIPS 2025, 2505.13636) introduces multi-agent peer elicitation using Determinant Mutual Information (DMI) scoring and proves a strictly stronger result: dominant strategy truthfulness (Lemma 1), meaning truthful reporting is optimal regardless of other agents' strategies—not just in Bayesian Nash equilibrium. Their sublinear O(√T) regret bound (Theorem 2) and last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent provide a complementary theoretical foundation to Qiu et al.'s BNE. PEG requires n≥2 discriminators and K_t≥4 tasks with conditional independence (Assumption 4), and their experiments use 3 discriminators with the theoretical minimum n≥2 and K_t≥4 tasks required by Lemma 1. However, PEG does not characterize how its manipulation-resistance guarantees degrade when the conditional independence assumption is violated—precisely the regime we analyze.

Yang et al.'s 'Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity' (ICLR 2026 Workshop AIMS, 2602.03794) provides an information-theoretic framework where multi-agent system performance is bounded by intrinsic task uncertainty H(Y|X) with residual uncertainty decaying as (1-α_c)^{K*}, where α_c is the complementarity rate and K* = 2^{H(ρ)} is the effective channel count computed via von Neumann entropy of the embedding Gram matrix (Theorem 4.3). Their heterogeneity advantage corollary (Corollary 4.4) formally shows α_het·K_het > α_hom·K_hom implies strictly better performance. Critically, K* captures diversity in embedding space without labels and empirically correlates with accuracy (r=0.388 overall, r=0.535 for K*_c among correct agents). However, their framework addresses task performance (information recovery) not adversarial manipulation resistance (information perturbation cost). Our work establishes the adversarial dual: while their K* governs how quickly residual uncertainty decreases, our framework shows that the same correlation structure governs how quickly manipulation cost increases.

Turkmen et al.'s 'Don't Always Pick the Highest-Performing Model' (arXiv 2602.08003, Feb 2026) formulates ensemble selection as MI maximization with a Gaussian-copula correlated error model and proves an information-theoretic error floor (Theorem 4.4): lim_{m→∞} P_e = Φ(Φ⁻¹(1-p)/√ρ) > 0 for equicorrelated ensembles with pairwise copula correlation ρ. Their three-term MI decomposition (Theorem 4.3)—Δ(j|S) = I(Y;X_j) - I(X_j;X_S) + I(E_j;E_S)—separates accuracy, redundancy, and error correlation. Empirically, they find within-family correlations ρ~0.7-0.8 and cross-family ρ~0.4-0.5. Their copula model provides the mathematical foundation for our derivation of effective independent channel count K_eff.

Kaneko & Baldwin's 'Bits Leaked per Query' (NeurIPS 2025 spotlight, arXiv 2510.17000) establishes tight information-theoretic bounds on adversarial attack costs against individual LLMs: any adaptive attack achieving error ≤ ε requires at least N_min ≥ log₂(1/ε)/I_max queries, where I_max is the maximum per-query mutual information leakage (Theorem 1), and this bound is achieved by sequential probability ratio tests (Theorem 2). Validated across 7 LLMs including Llama-4 and DeepSeek-R1, they identify four disclosure regimes (answer-only ~0.001-0.01 bits to full-access ~1.0+ bits). This provides the single-model information-theoretic attack cost foundation; our work extends the composition theory to multi-judge settings where an adversary must simultaneously fool K correlated judges.

Shen et al.'s 'Robust LLM Performance Certification via Constrained MLE' (arXiv 2604.03257, Google DeepMind/UCL, 2026) proposes constrained maximum likelihood estimation fusing human labels, LLM-judge annotations, and domain constraints (known TPR/FPR bounds) for certified LLM performance estimation. While addressing performance certification under benign judge noise, it assumes honest judges and does not model adversarial manipulation—precisely the threat model we address.

Feng et al.'s 'Noisy but Valid' (ICLR 2026, arXiv 2601.20913) provides a statistical hypothesis testing framework for certifying LLM failure rates using imperfect judges, with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty. Using a small human-labeled calibration set to estimate judge TPR/FPR, they derive variance-corrected critical thresholds (Theorem 5.4 gives exact conditions for judge adoption). Like Shen et al., this assumes honest but fallible judges, not adversarial manipulation. Our work complements both: Shen et al. certify performance estimates via constrained MLE, Feng et al. certify statistical validity via hypothesis testing, and we certify manipulation resistance under adversarial attacks.

Jung & Na's 'Logarithmic Scores, Power-Law Discoveries' (arXiv 2604.00477, April 2026) identifies a score-coverage dissociation in multi-agent evaluation panels: scoring reliability (ICC) scales logarithmically with panel size N (R²=0.974) while unique issue discovery follows a sublinear power law y=7.8·N^0.69 (R²=0.999). Scores saturate ~2× faster than discoveries, with N=8 achieving 82% of maximum scoring reliability but only ~42% of N=32 discovery level. This has direct implications for our K-scaling claims: manipulation-cost scaling benefits may exhibit similar dissociation, where formal robustness guarantees saturate faster than empirical coverage of attack surface. We analyze this explicitly.

The SoK on LLM-as-Judge Security (2603.29403, April 2026) catalogs extensive vulnerabilities: open-source models showing 50–68% average ASR and frontier models 27–44%; 7-model diverse committees reduce ASR to 10–19% empirically but without formal explanation. RobustJudge (2506.09443) benchmarks 15 attack methods and 7 defense strategies. CAP (OpenReview 2026) shows comparative assessment is more robust than absolute scoring but provides no formal guarantees.

On error correlation and independence: Kim et al.'s 'Correlated Errors in Large Language Models' (ICML 2025, arXiv 2506.07962) shows 60% pairwise agreement when both err on Helm (vs. 33% random baseline), with same-company adding +0.066 and same-architecture adding +0.076 agreement. Chen et al.'s behavioral entanglement framework (arXiv 2604.07650) introduces BEI and CIG metrics across 18 LLMs from 6 families, finding cross-family entanglement 40–60% lower than intra-family.

On coordination failure: Frongillo et al. (2503.16280) prove that uninformative equilibria become unstable with fine-grained signals. Keppo et al.'s collusion fragility analysis (2603.20281) finds increasing LLM count from 2→5 breaks collusion (+22%→+3%), but same-family size heterogeneity stabilizes via leader-follower dynamics—motivating cross-family diversity.

On multi-agent evaluation: CollabEval (2603.00993) proposes three-phase multi-agent evaluation without formal adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, 2505.24239) uses credibility-based iterative aggregation for adversary resistance without information-theoretic measures.

On certified ensemble robustness: Chen et al. (2107.10873) prove that diversified gradient and large confidence margin are jointly necessary and sufficient for certified ensemble robustness—standard ensembles achieve only marginal improvements without explicit diversity. Horvath et al. (2106.06946) show randomized smoothing ensembles achieve √K-type certified radius improvement. These provide precedent for polynomial scaling bounds from diversity.

THE KEY GAP: No existing work provides formal N-agent manipulation-cost scaling results—the adversarial dual of Yang et al.'s task-performance scaling—where the bound is an explicit computable function of measurable inter-judge signal correlation, yielding certifiable robustness guarantees validated against realistic attacks. Kaneko & Baldwin provide the single-model attack cost foundation; we provide the multi-judge composition theory. Shen et al. and Feng et al. certify evaluation quality under noise; we certify resistance under adversarial attacks.

## Approach
We extend Robertson & Koyejo's TVD-MI framework from pairwise evaluation to N-agent multi-judge settings with certifiable manipulation-resistance bounds, drawing on the Gaussian-copula correlation model (Turkmen et al.) and information-theoretic diversity scaling (Yang et al.) for the formal machinery, and extending Kaneko & Baldwin's single-model attack cost bounds to multi-judge composition. Our contribution has five components:

**Component 1: Theoretical Framework—The Adversarial Dual of Diversity Scaling.**

We prove that when K judge models evaluate candidate responses using TVD-MI scoring, the adversarial manipulation cost grows as Ω(K^{g(I_max)}), where g is an explicit decreasing function of the maximum pairwise mutual information I_max between judge signals. This establishes the adversarial dual of Yang et al.'s task-performance result: while their Theorem 4.3 shows residual uncertainty decreases as (1-α_c)^{K*}, we show manipulation cost increases polynomially in K with exponent determined by the same underlying correlation structure.

**Proof Strategy (Three-Pillar Approach):**

*Pillar 1—Strong Data Processing Inequality (SDPI) Composition.* We model each judge as a noisy channel from the 'true quality' signal to an evaluation score. Following Polyanskiy & Wu (2017), SDPI contraction coefficients compose multiplicatively across independent channels: an adversary pushing perturbation through K independent channels experiences η^K total contraction, where η ∈ (0,1) is the per-channel contraction coefficient. Under inter-judge correlation, the effective number of independent channels is reduced from K to K_eff. This extends Kaneko & Baldwin's single-channel result (N_min ≥ log₂(1/ε)/I_max) to multi-channel settings: the adversary's total information gain across K correlated judges is bounded by K_eff · I_max per query round.

*Pillar 2—Fano-Ensemble Decomposition.* Following Morishita et al. (ICML 2022), we decompose the total MI I(Y; Z_1,...,Z_K) available to the aggregator into K individual relevance terms, pairwise redundancy terms involving I_max, and combination loss terms. The adversary must reduce this total MI below the Fano threshold for correct decision-making, and the required perturbation energy is lower-bounded by the effective information.

*Pillar 3—Gaussian Copula Closed Form.* Adapting Turkmen et al.'s equicorrelated Gaussian copula model (where Z_j = √ρ·U + √(1-ρ)·ξ_j with shared latent factor U), we derive the effective independent channel count:

  K_eff = 1 + (K-1)·exp(-2·I_max)

where I_max = -½ log(1-ρ²) is the pairwise MI under the copula model. This formula is our own derivation, obtained by computing the effective rank of the K×K correlation matrix under equicorrelation: eigenvalues are λ₁ = 1+(K-1)ρ (multiplicity 1) and λ₂ = 1-ρ (multiplicity K-1), and the effective independent dimensionality follows from the ratio of total to maximum variance, expressed as a function of MI via the ρ-to-I_max mapping ρ² = 1-exp(-2·I_max).

The manipulation cost lower bound is then Ω(K_eff^{1/2}) from variance-reduction arguments (following Horvath et al.'s √K certified radius scaling for randomized smoothing ensembles), giving:

  g(I_max) = ½ · log(1 + (K-1)·exp(-2·I_max)) / log(K)

This satisfies the boundary conditions: g(0) = ½·log(K)/log(K) = ½ for fully independent judges (matching √K variance reduction), and g(I_max) → 0 as I_max → ∞ (fully correlated judges collapse to a single effective channel). The ½ exponent for independent judges is tight under the variance-reduction argument; if the SDPI chain yields linear rather than √K scaling, we get g(0) = 1.

*Key Lemma (Connection from MI to Perturbation Budget):* We connect information-theoretic bounds to operational manipulation cost via Marton's inequality: TV(P,Q)² ≤ ½·KL(P||Q), combined with Robertson & Koyejo's Theorem 3.3 relating TVD-MI to certification bounds. The adversary's perturbation must overcome the TVD gap, which scales with √K_eff under the copula model.

*Distributional Assumptions:* The closed-form result requires the equicorrelated Gaussian copula on judge signals (marginals can be arbitrary; only the dependence structure is Gaussian) and equicorrelation (all pairwise MIs equal I_max). We prove a weaker but more general result under arbitrary pairwise MI structure: g depends on the minimum eigenvalue of the correlation matrix, giving g ≥ ½·λ_min(Σ). For heterogeneous correlation, we use the effective rank of the correlation matrix (analogous to Yang et al.'s K* = 2^{H(ρ)}) as a tighter proxy.

**Component 2: Practical α Regime Analysis with Sensitivity Bounds.**

Using Turkmen et al.'s empirical copula correlations (within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5) and Kim et al.'s correlated error data (same-company +0.066, same-architecture +0.076; ICML 2025, arXiv 2506.07962), we estimate for the proposed three-judge cross-family ensemble:

- Central estimate: ρ ≈ 0.45, I_max ≈ 0.11, α = g(I_max) ∈ [0.35, 0.65]
- At α=0.5, K=7: manipulation cost ≈ 7^0.5 ≈ 2.65× single-judge baseline
- At α=0.65, K=7: manipulation cost ≈ 7^0.65 ≈ 3.7×

*Sensitivity analysis and break-even:* We explicitly plan for the possibility that empirically measured α falls outside our predicted range, since current correlation data is from prior-generation models (Kim et al.'s 350+ mostly older LLMs, Chen et al.'s 18 models from prior families). DeepSeek-V4, Qwen-3.5, and Llama-4-Maverick may show different correlation structures due to shared training data evolution (Common Crawl, synthetic data from frontier models) and partial architectural convergence (all three use MoE, though with different routing and attention mechanisms).

- If α = 0.2 (more correlated than expected, ρ ≈ 0.65): K=7 yields only 7^0.2 ≈ 1.55× cost increase. The protocol still provides formal guarantees that majority voting cannot, but the practical margin is thin. At this α, our protocol's value proposition is primarily the certifiability—analogous to how randomized smoothing provides modest certified radii but with provable guarantees.
- If α = 0.8 (more independent than expected, ρ ≈ 0.25): K=7 yields 7^0.8 ≈ 5.2× cost increase—substantially better than baseline. This would indicate that cross-family diversity is even more effective than prior-generation data suggested.
- Break-even analysis: Majority voting with K=7 achieves empirical ASR reduction from 50-68% to 10-19% (SoK), a ~4-5× reduction in success probability. Our protocol must provide comparable ASR reduction plus formal guarantees to be justified. We identify the critical α threshold where the certified bound becomes vacuous (i.e., the formal guarantee is weaker than the trivially achievable baseline): for K=7, this occurs at approximately α ≤ 0.05, corresponding to ρ ≥ 0.95 (near-identical judges). For any realistic cross-family ensemble, we are well above this threshold.
- Diminishing returns analysis: Following Jung & Na's (2604.00477) finding that scoring reliability scales logarithmically while discovery scales as N^0.69, we analyze whether our manipulation-cost scaling exhibits similar dissociation. The formal certified bound may saturate faster (logarithmically in K) than the empirical ASR reduction (which may follow a power law), creating a gap between what we can certify and what we observe.

**Component 3: Practical Protocol Design.**

We instantiate the framework as a deployable multi-judge evaluation protocol using three architecturally diverse open-weight model families—DeepSeek-V4-Flash (284B MoE, 13B active, Multi-head Latent Attention), Qwen-3.5 (397B MoE, 17B active), and Llama-4-Maverick (400B MoE, 17B active). These models are chosen because: (a) they come from three different organizations with different training data pipelines, minimizing same-company correlation (+0.066 per Kim et al.); (b) they use different architectural innovations, minimizing same-architecture correlation (+0.076); (c) Turkmen et al.'s copula framework predicts cross-family ρ~0.4-0.5 for such configurations.

The protocol operates in three phases:
1. **Independence measurement:** Compute pairwise TVD-MI scores between all judge pairs on a calibration set; estimate the copula correlation ρ_ij and I_max; compute effective channel count K* (à la Yang et al.) and predicted α.
2. **Evaluation with certified scoring:** Each judge evaluates candidates using TVD-MI; the aggregator combines scores via DMI-weighted aggregation (adapting PEG's determinant-based scoring from Chen et al., NeurIPS 2025), which provides dominant-strategy truthfulness (Lemma 1) when judges are approximately conditionally independent.
3. **Certification:** Output both the aggregated evaluation and the certified manipulation-cost bound Ω(K^α) with the empirically measured α, constituting a per-evaluation robustness certificate.

We prove the coordination failure argument leveraging both PEG's dominant-strategy result (which applies under conditional independence) and Qiu et al.'s BNE framework (which applies under the weaker shared-prior assumption). For the regime between these extremes—partial correlation that violates conditional independence but maintains bounded MI—we provide interpolating bounds via the SDPI framework.

**Component 4: Certifiable Robustness Framing.**

We explicitly frame our contribution as 'certifiable robustness for LLM evaluation,' drawing the analogy to certified adversarial robustness in classification (randomized smoothing, interval bound propagation). Just as certified adversarial defenses often achieve smaller empirical improvements than heuristic defenses but provide provable guarantees, our protocol may achieve ASR reductions comparable to majority voting but with formal certificates. The value proposition is:

- Majority voting: empirically reduces ASR from ~60% to ~15% for K=7 (SoK), but with no formal guarantee—the ASR could spike under novel attacks.
- Our protocol: achieves comparable empirical ASR reduction AND provides a formal lower bound on the manipulation cost that scales as Ω(K^α), certified per-evaluation. This means even against unforeseen future attacks, the manipulation cost is provably bounded below.
- Connection to single-model bounds: Kaneko & Baldwin's N_min ≥ log₂(1/ε)/I_max provides the per-judge attack cost floor; our multi-judge composition shows that the adversary's total cost scales as K_eff times this single-judge bound, yielding certifiable multi-judge manipulation resistance.

This framing directly addresses the concern that 2.65-4.0× scaling may seem modest: in certified adversarial robustness, even modest certified radii are valued because they are provable, while large empirical margins can be broken by adaptive attacks.

**Component 5: Realistic Adversarial Validation.**

We evaluate against RobustJudge's 15 attack methods (including PAIR, combined attacks, adversarial suffixes, and prompt injection) plus the SoK's documented attack vectors, on text summarization, code generation, and knowledge-intensive QA tasks. We benchmark against: (a) all 7 RobustJudge heuristic defenses; (b) CAP comparative augmented prompting; (c) CollabEval's consensus-based multi-agent approach; (d) Ebrahimi et al.'s credibility-scoring framework; (e) Robertson & Koyejo's single-evaluator TVD-MI baseline; (f) simple majority voting (K=3,5,7); (g) PEG with DMI scoring (Chen et al.). For each experimental condition, we report: (i) attack success rate, (ii) empirically measured ρ_ij and I_max, (iii) computed α, (iv) the gap between the certified manipulation-cost bound and the observed empirical manipulation cost, and (v) whether the formal bound is tight (ratio of empirical to certified). Following the score-coverage dissociation insight (Jung & Na), we separately analyze certification tightness (how close the formal bound is to the empirical one) and attack surface coverage (what fraction of attack types the bound holds against).

## Resource Estimate
{'manual': {'gpu_hours': '1,000-1,500 H100-equivalent', 'timeline': '14-18 weeks', 'estimated_gpu_cost': '$2,500-$3,750 at $2.50/hr H100 spot', 'gpu_breakdown': 'DeepSeek-V4-Flash: 2×H100 FP8 (~160GB VRAM); Qwen-3.5: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB); Llama-4-Maverick: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB). Running all 3 simultaneously: 10×H100 (INT4) to 18×H100 (FP8). Per-experiment: single-judge baselines across 15 attacks × 3 tasks × 3 models ≈ 450 H100-hrs; multi-judge protocol evaluation across 45 conditions on 10-GPU cluster ≈ 500 H100-hrs; signal independence measurement, copula fitting, and α estimation ≈ 100 H100-hrs; ablations (K=1,2,3,5,7 judges, homogeneous vs. heterogeneous) ≈ 200 H100-hrs; development/debugging ≈ 150 H100-hrs'}, 'human_in_loop': {'gpu_hours': '800-1,200 H100-equivalent', 'timeline': '10-14 weeks', 'claude_api_cost': '$400-$600 (Sonnet 4.6 for code generation, proof assistance, paper drafting; ~130-200M tokens)', 'estimated_gpu_cost': '$2,000-$3,000 at $2.50/hr H100 spot', 'gpu_breakdown': 'Same per-model requirements; efficiency gains from Claude-assisted theorem proving, experiment scheduling, and copula fitting, reducing wasted debugging runs by ~20%'}, 'auto_research': {'gpu_hours': '1,200-1,800 H100-equivalent', 'timeline': '6-9 weeks', 'claude_api_cost': '$1,200-$2,000 (Opus 4.7 for theorem proving, SDPI chain verification, experiment design; ~250-400M tokens)', 'estimated_gpu_cost': '$3,000-$4,500 at $2.50/hr H100 spot', 'speed_bottleneck': 'The three-pillar proof strategy (SDPI + Fano + copula) has well-defined mathematical components that autonomous systems can work on in parallel, but ensuring the chain composes correctly across the three pillars requires human mathematical judgment. The key risk is that the SDPI contraction yields a weaker-than-expected bound, requiring fallback to the √K variance-reduction argument.'}}

## Inspired By
The convergence of seven lines of work: (1) Robertson & Koyejo's bounded f-divergence theory for single-evaluator manipulation resistance; (2) The dual peer prediction results—Qiu et al.'s BNE and Chen et al.'s dominant-strategy PEG—providing complementary incentive-compatibility guarantees; (3) Yang et al.'s information-theoretic diversity-scaling framework establishing the task-performance scaling law via effective channel count K*—we provide the adversarial dual; (4) Turkmen et al.'s Gaussian-copula model with its error floor theorem and MI decomposition, which provides the mathematical foundation from which we derive our closed-form K_eff; (5) Kaneko & Baldwin's tight single-model information-theoretic attack cost bounds (N_min ≥ log₂(1/ε)/I_max), which we extend to multi-judge composition; (6) The SoK's empirical finding that 7-model committees reduce ASR to 10–19% without formal explanation; (7) The behavioral entanglement and correlated error literature (Chen et al. 2604.07650, Kim et al. ICML 2025) providing quantitative inter-judge independence measurements. We unify these into a certifiable manipulation-resistance framework where the certified bound is an explicit function of measurable signal correlation.

## Target Venues
- AAAI 2027 Main Technical Track (abstract: July 21, 2026; full paper: July 28, 2026; primary target—theory + experiments with certified robustness framing)
- USENIX Security 2027 Cycle 1 (abstract: August 18, 2026; full paper: August 25, 2026; security-focused version emphasizing certifiable robustness against realistic attacks)
- NeurIPS 2026 Workshops (contributed papers: ~August 29, 2026; workshop version connecting to the diversity-scaling and certified robustness communities)
- ICLR 2027 (estimated deadline: October 2026; polished archival version with extended theory, comprehensive experiments, and tightness analysis)

## Key References
- Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes (Robertson & Koyejo, arXiv 2508.05469, 2025) — foundational TVD-MI theory, Theorem 3.3 polynomial certification bounds, primary work we extend
- Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores (Robertson, arXiv 2510.14966, 2025) — sparse TVD-MI evaluation, two-judge preliminary validation
- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (Qiu et al., ICLR 2026, 2601.20299) — BNE incentive-compatibility for LLM peer prediction, inverse scaling property
- Incentivizing Truthful Language Models via Peer Elicitation Games (Chen et al., NeurIPS 2025, 2505.13636) — DMI-based multi-agent peer elicitation with dominant strategy truthfulness (Lemma 1), sublinear O(√T) regret bound (Theorem 2), last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent; experiments use 3 discriminators (n≥2 required by Lemma 1)
- Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity (Yang et al., ICLR 2026 Workshop AIMS, 2602.03794) — information-theoretic diversity-scaling framework: effective channel count K* = 2^{H(ρ)}, residual uncertainty (1-α_c)^{K*} geometric contraction (Theorem 4.3), heterogeneity advantage (Corollary 4.4); we provide the adversarial dual of their task-performance result
- Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection (Turkmen et al., arXiv 2602.08003, 2026) — Gaussian-copula correlated error model (Z_j = √ρ·U + √(1-ρ)·ξ_j), information-theoretic error floor Φ(Φ⁻¹(1-p)/√ρ) (Theorem 4.4), three-term MI decomposition into accuracy-redundancy-error correlation (Theorem 4.3); copula model provides the mathematical foundation from which we derive our K_eff formula
- Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000) — tight single-model attack cost bound N_min ≥ log₂(1/ε)/I_max via K-ary Fano inequality (Theorem 1), achieved by SPRT (Theorem 2); validated across 7 LLMs including Llama-4 and DeepSeek-R1; provides single-channel foundation that we extend to multi-judge composition
- Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation (Shen et al., arXiv 2604.03257, Google DeepMind/UCL, 2026) — constrained MLE fusing human labels, LLM-judge annotations, and domain constraints for certified performance estimation; addresses honest-judge noise, not adversarial manipulation; occupies adjacent 'certifiable evaluation' space
- Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges (Feng, Shen, Balashankar, Gerner-Beuerle & Rodrigues, ICLR 2026, arXiv 2601.20913) — statistical hypothesis testing framework for LLM evaluation certification with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty; variance-corrected thresholds using judge TPR/FPR estimation; assumes honest but fallible judges, not adversarial manipulation; complements Shen et al. in the 'certifiable evaluation' space
- Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation (Jung & Na, arXiv 2604.00477, 2026) — score-coverage dissociation: scoring reliability scales logarithmically, discovery follows power law N^0.69; informs our analysis of when certified bounds saturate vs. empirical gains
- Security in LLM-as-a-Judge: A Comprehensive SoK (arXiv 2603.29403, April 2026) — comprehensive vulnerability catalog, 50-68% ASR on open-source, 7-model committee reduces ASR to 10-19%; primary empirical evidence for diversity benefit without formal explanation
- LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge (arXiv 2506.09443, 2025) — RobustJudge benchmark, 15 attacks, 7 defenses, 12 models
- Correlated Errors in Large Language Models (Kim, Garg, Peng & Garg, ICML 2025, arXiv 2506.07962) — error correlation across 350+ LLMs: 60% agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076; KEY for α regime analysis
- How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026) — BEI and CIG metrics across 18 LLMs from 6 families; cross-family entanglement 40-60% lower than intra-family
- Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences (arXiv 2602.11898, 2026) — 16-38% disagreement among top frontier models despite similar accuracy
- Strong Data-Processing Inequalities for Channels and Bayesian Networks (Polyanskiy & Wu, arXiv 1508.06025, 2017) — SDPI contraction coefficients compose multiplicatively; foundational for our Pillar 1 proof strategy
- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683) — decomposes Fano bound for ensembles into relevance, redundancy, and combination loss; foundational for our Pillar 2 proof strategy
- On the Certified Robustness for Ensemble Models and Beyond (Chen et al., arXiv 2107.10873, 2021) — diversified gradient + large confidence margin jointly necessary and sufficient for certified ensemble robustness
- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021) — ensemble variance reduction yields √K-type certified radius improvement; precedent for polynomial scaling from diversity
- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020) — proves attack cost scales up with number of redundant signal copies; direct precedent for manipulation cost scaling with K
- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026) — increasing LLM count 2→5 breaks collusion (+22%→+3%); same-family size heterogeneity stabilizes via leader-follower; motivates cross-family diversity
- CollabEval: Multi-Agent Collaborative Evaluation (arXiv 2603.00993, March 2026) — three-phase multi-agent evaluation without formal adversarial guarantees
- An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239) — credibility-based iterative aggregation; game-theoretic but not information-theoretic
- Certifying Joint Adversarial Robustness for Model Ensembles (Chiang et al., arXiv 2004.10250, 2020) — vulnerability space disjointness for ensemble certification
- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025) — fine-grained signals destabilize uninformative equilibria
- Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)
- Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)
- am-ELO: A Stable Framework for Arena-based LLM Evaluation (ICML 2025 Poster)
- CAP: Improving the Robustness of LLM-as-a-Judge Against Adversarial Score Manipulation via Comparative Augmented Prompting (OpenReview 2026)
- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)
- Can You Trick the Grader? Adversarial Persuasion of LLM Judges (EMNLP 2025 Findings)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e8145263-7c4b-44d7-a5f8-1aa5729207e7",
  "type": "user",
  "uuid": "a6d4cbc3-bff9-4943-9089-87cfcd0a98f5",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:51:40.440Z_

```json
{
  "parentUuid": "a6d4cbc3-bff9-4943-9089-87cfcd0a98f5",
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
  "uuid": "cffd616f-62e1-4c3c-bb64-12a23681ea78",
  "timestamp": "2026-05-20T04:51:40.440Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:51:40.440Z_

```json
{
  "parentUuid": "cffd616f-62e1-4c3c-bb64-12a23681ea78",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e9d17d30-29aa-4bf8-bfa1-b647bc2e9acd",
  "timestamp": "2026-05-20T04:51:40.440Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to evaluate this proposal rigor…",
  "leafUuid": "e9d17d30-29aa-4bf8-bfa1-b647bc2e9acd",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Aggregate Meta Judge assessment for multi-judge manipulation cost proposal",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:52:14.449Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews carefully to produce a Meta Judge synthesis.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [23% - 33%] 中位 28%

**Reviewer 2:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)


- Related Work: 强 (Strong)
- Probability: [22% - 32%] 中位 27%

**Reviewer 3:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability: [22% - 35%] 中位 28%

Now I'm calculating the aggregate statistics across all three reviewers. The median acceptance probabilities cluster tightly around 27-28%, with a mean of 27.67% and very low variance, suggesting strong consensus among the reviewers.

Looking at the specific evaluation dimensions, all three reviewers agree on novelty being medium—the work combines existing techniques rather than introducing fundamentally new concepts. There's also unanimous agreement that the related work section is strong. Significance shows consensus in the medium range, with only reviewer 3 leaning slightly stronger. The trivial alternative threat appears to be a minor concern.

All three reviewers independently flagged that majority voting achieves 4-5× improvement empirically compared to the certified 2.65-3.7× improvement here, and they all noted the qualitative result feels intuitive. Both reviewers 1 and 2 raised a critical assumption issue: the Gaussian copula correlation structure observed under benign conditions may not hold when adversarial perturbations are applied. The equicorrelation assumption also drew unanimous concern across all reviewers. On the positive side, all three confirmed the gap identification is legitimate—there's no direct competitor in this space.

The one notable outlier is reviewer 3 rating significance as medium-to-strong rather than medium, reasoning that the problem is timely and theoretically valuable.

Now I'm looking at the implementation requirements: roughly 1,000-1,500 GPU hours on H100-equivalent hardware using DeepSeek-V4-Flash models.

The work involves mathematical proof verification since the three-pillar strategy has gaps, but no model training is needed—just inference with existing models against the RobustJudge benchmark and standard attack vectors. The timeline stretches 10-18 weeks depending on the approach taken.

The standard deviation is extremely tight at 0.47%, indicating strong consensus, so I can confidently narrow my probability interval around the 27-28% center point with a slight lean toward the stricter estimates, settling on lower bounds around 22-23%.

For the upper bounds, the three reviewers converge around 32-33%, with one estimate at 35% being slightly optimistic. This gives me a final range of 22-32% with a median of 27%, which falls below the 36% threshold and suggests this leans toward the lower end of acceptable—there's legitimate technical work here, but the structural issues around synthesis novelty and the unsurprising qualitative results are fundamental problems unlikely to be easily resolved, making this a borderline case that may not quite meet the bar for a top venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9d17d30-29aa-4bf8-bfa1-b647bc2e9acd",
  "isSidechain": false,
  "requestId": "req_011CbDDjU6XJGag62BBzN8Ws",
  "type": "assistant",
  "uuid": "78dfef8e-6093-44e3-9428-a840ddd0631c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PK1T5zoDcmtQdLYz3nLtm6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25366,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3557,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 25366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25366
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

_source line 9 · 2026-05-20T04:53:04.372Z_

【阶段】: Meta Judge
【三次中位】: [28%, 27%, 28%]  std=0.5%
【共识维度】:
- **Novelty = 中**（3/3 一致）：核心技术贡献是已有数学工具（SDPI + Fano + Gaussian copula + √K variance reduction）的组合应用，非原创性突破。"Adversarial dual of diversity scaling" 框架优雅但对信息论专家而言是自然延伸。
- **Related Work = 强**（3/3 一致）：25-30+ 篇引用覆盖全面，所有关键论文经验证真实且描述准确，gap 定位精准——确认无直接竞争者。
- **Trivial Alternative 威胁显著**（3/3 一致）：简单多数投票经验性 ASR 改善 ~4-5× 在数值上优于 certified bound 的 2.65-3.7×，proposal 的增量价值仅在 certifiability，审稿人对此价值判断可能不一。
- **"I would have guessed this" 风险**（3/3 一致）：定性结论（"更多样 judge → 操纵成本更高，受相关性调节"）直觉上可预期，形式化贡献虽正确但 incremental。
- **Equicorrelation 假设局限**（3/3 一致）：闭式 K_eff 依赖等相关 copula，真实 judge 间相关性异质；一般化 bound（λ_min-based）可能过松。
- **Benign ρ ≠ Adversarial ρ 的核心假设风险**（2/3：R1、R2 重点标注）：理论框架依赖 benign 条件下测量的 ρ 来 certify 对抗条件下的 manipulation cost，但对抗攻击可能系统性利用共享弱点使 effective ρ 坍缩，致 certified bound 接近 vacuous。
- **Significance = 中**（2/3：R1、R2 明确标"中"）：问题重要且 timely，但 certified bound 数值弱于 empirical baseline + 无 surprising threshold effect 限制了影响力。

【异常维度】:
- R3 将 Significance 评为"中偏强"（仅 1/3）：理由是"如果理论能指导评估协议设计则有实际影响"——合理但偏乐观，R1/R2 均认为 certified bound 的 looseness 限制了实际指导价值。**降权处理，Significance 最终取"中"。**
- R3 独有地质疑"adversarial dual"是概念类比而非数学严格对偶（LP dual 意义上）——有效质疑但属于 framing 问题而非致命缺陷，可通过修辞调整缓解。
- R3 独有地质疑 SDPI 在相关通道下的可组合性——从相关通道到 K_eff 个独立通道的约化步骤缺乏 proof sketch。技术上重要，但其他审稿人未标注为关键风险，**作为次要风险保留**。
- R1 独有地提及 Marton inequality 的松弛性——有效但属于 tightness 讨论范畴，非致命。

【最终概率】: [22% - 32%] 中位 27%
【一致性】: 高（std=0.5%，三位审稿人在所有核心维度判定高度一致）
【综合理由】:

三位审稿人展现出罕见的高度一致性：

1. **Novelty 一致判"中"是概率天花板的决定性因素。** 三位均独立指出核心技术贡献是 SDPI composition + Fano decomposition + Gaussian copula closed form 的标准组合应用，每一步都是已有工具的直接应用而非需要深刻新洞察的步骤。K_eff = 1+(K-1)·exp(-2·I_max) 本质上是等相关矩阵特征值的标准推导。这将 idea 质量天花板锁定在 ~35% 以下。

2. **Trivial alternative 问题进一步压缩空间。** 三位均标注 majority voting 经验效果（4-5×）优于 certified bound（2.65-3.7×）是审稿人最可能的攻击点。Proposal 的 "certifiability" 辩护逻辑上成立，但在 NLP 社区（vs. 理论 CS / ML safety 社区）的接受度不确定。

3. **Related Work 的一致"强"评价提供了坚实下界。** Gap 经三位独立验证确认真实存在，定位精准，论文引用全部 check out。这确保 proposal 不会因 coverage 或 positioning 问题被低分拒绝，下界稳定在 22%。

4. **R3 的 Significance "中偏强"是唯一 outlier，但不足以上移中位。** R3 的乐观基于"理论指导协议设计"的潜在价值，但 R1/R2 均指出 certified bound 的 looseness 限制了指导价值，且无 surprising threshold effect。取三方共识的"中"更稳健。

5. **最终中位 27% 的逻辑**：Novelty 中 + Significance 中 → idea 天花板约 33-35%。Trivial alternative 的数值劣势 + benign ρ ≠ adversarial ρ 的假设风险 → 从天花板下调 6-8 个百分点。Related Work 强 → 下界稳固在 22%。中位落在 27%。

【建议】: 边缘（偏不推荐侧）——idea 方向正确、gap 真实、framework 完整，但核心贡献的 novelty depth 和 significance 均不足以达到 top venue 的 accept 阈值。如果通过迭代能 (a) 找到 surprising 的理论结果（如 phase transition / tightness result）或 (b) 显著强化 certified bound 的实用价值主张，有上升空间但上限有限。

【实施评估】:
  - 计算资源: 1,000-1,500 H100-equivalent GPU hours（约 $2,500-$3,750），需 10-18× H100 并行运行三个大模型（DeepSeek-V4-Flash 2×H100, Qwen-3.5 4-8×H100, Llama-4-Maverick 4-8×H100），资源需求中等偏高但可行
  - 数据需求: RobustJudge benchmark（公开）、SoK 攻击向量（公开）、text summarization / code generation / knowledge QA 标准数据集——数据可得性无障碍
  - 人工介入: 三支柱证明策略（SDPI + Fano + copula）的数学严谨性验证需要信息论专家参与；从 proof strategy 到完整 proof 可能存在非 trivial 技术困难（R3 特别标注）；copula 拟合和 α 校准需要统计专业判断
  - 训练需求: 无模型训练，纯推理实验——这是显著优势，降低了实施门槛
  - 新 Benchmark: 不需要构建新 benchmark，使用已有 RobustJudge（15 attacks × 7 defenses × 12 models）
  - 预估周期: 10-18 周（理论证明 4-6 周 + 实验 4-8 周 + 写作 2-4 周），主要瓶颈是三支柱证明的数学完备性验证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78dfef8e-6093-44e3-9428-a840ddd0631c",
  "isSidechain": false,
  "requestId": "req_011CbDDjU6XJGag62BBzN8Ws",
  "type": "assistant",
  "uuid": "672ce0ef-0f2d-4905-bff4-7146857400a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PK1T5zoDcmtQdLYz3nLtm6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25366,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3557,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 25366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25366
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to evaluate this proposal rigor…",
  "leafUuid": "672ce0ef-0f2d-4905-bff4-7146857400a6",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Aggregate Meta Judge assessment for multi-judge manipulation cost proposal",
  "sessionId": "74c081e8-daac-4892-9632-a68f43cd99a4"
}
```

---
