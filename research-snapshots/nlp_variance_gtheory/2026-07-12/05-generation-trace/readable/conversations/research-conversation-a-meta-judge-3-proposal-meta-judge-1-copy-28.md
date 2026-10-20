# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/42983d27-0cbd-4b46-805e-ef687e8fcc4c.jsonl`
- **Structured JSON:** [`3d63bbc9051dcd9df570.json`](../../sessions/3d/3d63bbc9051dcd9df570.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:58:46.775Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:58:46.775Z",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\n现在我有了足够的调研信息来进行评估。让我整理分析。\n\n---\n\n```\n【阶段】: Triage\n```\n\n## ⚠️ 致命问题：严重的投稿venue不匹配\n\n**在进入正式评估之前，必须首先指出一个致命问题：CoRL（Conference on Robot Learning）是一个机器人学习会议**，其征稿范围明确包括：robot perception、robot control、manipulation、locomotion、sim-to-real transfer、robot foundation models 等。本 proposal 研究的是 LLM 数学推理中的 PRM 校准与 reward hacking 防御（评测数据集为 MATH-500 和 AIME），与机器人学习**零关联**。提交至 CoRL 几乎必然被 desk reject。\n\n**如果投稿目标确实是 CoRL，中稿概率接近 0%，无需进一步评估。**\n\n以下评估假设 proposal 将投稿至**合适的 venue（如 NeurIPS、ICML、ICLR 等 ML/NLP 顶会）**，仅评估 idea 本身的质量。\n\n---\n\n```\n【领域调研】:\n```\n\n- **[Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)** (NeurIPS 2025): 首次系统性研究 PRM 校准问题，发现 PRM 在难题上系统性高估成功概率，提出 quantile regression 校准方法。是 Thread 1 (PRM Calibration) 的奠基工作。本 proposal 的 Component A 直接建立在此基础上。\n\n- **[Distributional PRMs via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)** (May 2026 preprint): 用条件最优传输获得校准的单调分位数函数，改善 BoN 在 MATH-500 和 AIME 上的表现。**从未测试鲁棒性/抗攻击能力**——这正是本 proposal 声称要填补的空白。\n\n- **[Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)** (March 2026): 证明 PRM 是灾难性可攻击的——梯度攻击使 PRM 奖励膨胀 4 倍，RL 训练达到近乎完美的 PRM 奖励但实际准确率 <4%，43% 的奖励增益来自风格捷径。**未提出任何基于校准的防御**。本 proposal 的 Thread 2 基础。\n\n- **[Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)** (Feb 2026, Ackermann et al.): 建立了奖励表面平坦度与准确度保持之间的理论联系，提出梯度正则化偏向平坦区域。**仅在 outcome-level 单标量奖励模型上工作**，未涉及 step-level PRM。本 proposal 声称要将此扩展到 step-level Hessian 分析。\n\n- **[APRM: Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)** (Nov 2025): 对抗训练 PRM，+3.4pp 鲁棒性改善。是 proposal 的 baseline 之一。\n\n- **[From Curiosity to Caution (Caution)](https://arxiv.org/abs/2604.04648)** (April 2026): 使用 prediction error 作为悲观度代理进行 BoN 防御。**使用未校准的不确定性代理，非校准概率**。是 proposal 的 baseline 之一。\n\n- **[Causal Reward Adjustment (CRA)](https://arxiv.org/abs/2508.04216)** (2025): ⚠️ **proposal 未引用此论文**。CRA 用稀疏自编码器识别 PRM 内部的混淆特征，通过 backdoor adjustment 进行因果校正以缓解 reward hacking。虽然机制不同（SAE vs. 校准），但同样是**因果视角下的 PRM reward hacking 防御**，直接威胁 proposal 的 \"first causally rigorous study\" 声明。\n\n- **[Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/abs/2503.22480)** (March 2025): 将标量奖励推广为高斯分布，用不确定性惩罚防止过优化。概念上与 CGSP 的 LCB 思路类似，但在 outcome-level。\n\n- **[Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)** (May 2025): 通过 minimax 目标训练悲观代理奖励作为真实奖励的下界。理论上与 CGSP 的悲观主义方向相似。\n\n- **调研总结**: PRM 校准和 PRM 可攻击性确实是两个相对独立的研究线程，但\"桥接\"的空间正在被多个方向的工作侵蚀。CRA (2508.04216) 已经从因果视角处理 PRM reward hacking；PURM 和 Pessimistic RM 已经在做不确定性驱动的悲观防御。本 proposal 的独特角色——\"用校准质量作为因果变量\"——仍有真实的 delta，但并非如 proposal 所声称的那样是一片完全未被触及的空白。\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在显著的 trivial alternative 威胁。**\n\n核心问题：如果 \"更好的校准 → 更强的抗攻击能力\"，那最简单的 trivial baseline 就是——**直接对 PRM 做 temperature scaling（一个参数的 post-hoc 校准），然后测试抗攻击能力是否改善**。这实际上就是 proposal 自己 Component B1 的一部分。\n\n如果 temperature scaling 就能显著降低 hackability，那么：\n1. 整个 48-configuration 相关性研究的增量价值被大幅削弱（一个参数就够了）\n2. CGSP 的复杂公式（μ_t − α·σ_t/√c_t）相对于 \"简单校准 + 标准 LCB\" 的增量价值需要严格论证\n3. 因果隔离实验变得不那么必要——如果 post-hoc calibration 就有效，因果关系已经隐含地被建立了\n\n**增量价值的真实所在**：如果只有 calibration 改善有效（而 CKA-matched representation change 无效），且 CGSP 的 adaptive pessimism 明显优于 static pessimism，那 proposal 的贡献才能站住脚。但这取决于实验结果，idea 层面上这个风险是真实的。\n\n另一个 trivial alternative：**ensemble disagreement**（已有工作如 Coste et al.）已经是一种不确定性驱动的悲观方法。CGSP 相比 ensemble-min 的增量需要仔细论证——proposal 声称 ensemble 是 \"uncalibrated\"，但 ensemble disagreement 本身就是一种合理的不确定性度量，不需要显式校准。\n\n---\n\n```\n【前提假设检验】:\n```\n\n核心 claim 的逻辑链条：\n\n**校准质量高 → 奖励信号更准确 → 梯度攻击/RL优化更难利用 → hackability 降低**\n\n这条链中有两个关键的未验证假设：\n\n1. **\"校准 = 准确\"的等式假设**: 校准（calibration）衡量的是 \"预测概率与真实频率的匹配度\"，但一个完美校准的模型仍然可能有 sharp but exploitable 的奖励表面。校准改善的是概率输出的可靠性，但未必改变模型在对抗性输入上的决策边界。一个 well-calibrated 但在特定 adversarial direction 上仍然脆弱的 PRM 是完全可能的。**Proposal 隐含假设校准改善等同于鲁棒性改善，这个等式没有理论保证。**\n\n2. **Post-hoc calibration \"provably preserves representations\" 的过度声明**: Temperature scaling 确实不改变 logits 的排序，但它改变了梯度的大小（因为 softmax 的温度影响梯度 landscape）。在梯度攻击场景下，temperature scaling 改变了 loss surface 的曲率，这可能影响攻击效果——但这不是 \"calibration\" 的功劳，而是 \"gradient scaling\" 的副作用。**因果隔离实验可能测到的不是\"校准的因果效应\"，而是\"温度缩放改变梯度 landscape\"的效应。**\n\n3. **Step-level flatness compounding 假设**: Proposal 假设 step-level 的平坦度会以有意义的方式沿轨迹组合，影响 outcome-level hackability。但 T 个 step 的 Hessian 如何 \"组合\" 是一个非平凡的数学问题，proposal 没有给出任何理论框架说明这种组合如何工作。\n\n---\n\n```\n【3 维度打分】:\n```\n\n### 1. Novelty: 中 (偏弱)\n\n**理由**：\n\n- **正面**: 将 PRM 校准线程与 PRM 可攻击性线程显式桥接，这个研究问题的定位是真实的——目前确实没有论文直接测试 \"校准质量是否因果地决定抗攻击能力\"。因果隔离实验设计（post-hoc vs. fine-tuning vs. matched representation change control）在方法论上有新意。\n\n- **负面**:\n  - **CRA (arXiv:2508.04216)** 已经从因果视角（用 backdoor adjustment）处理 PRM reward hacking 防御，且 proposal **未引用**此工作。\"First causally rigorous study\" 的声明可能被审稿人质疑。\n  - CGSP 的核心公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是 **LCB (Lower Confidence Bound) 的标准形式**，加上 calibration quality 的加权。这在 bandit/offline RL 文献中是常见思路。创新性主要在于 \"应用场景\"（step-level PRM + RL training），而非算法本身。\n  - **PURM (arXiv:2503.22480)** 和 **Pessimistic RM (arXiv:2505.20556)** 已经在做不确定性驱动的悲观奖励建模。CGSP 的差异化（step-level + calibration-gated）是增量的，不是范式级的。\n  - 核心发现如果是 positive（\"better calibrated PRMs are harder to hack\"），多数审稿人的反应可能是 **\"I would have guessed this\"** 而非 \"surprising\"。\n\n### 2. Significance: 中\n\n**理由**：\n\n- **正面**: PRM 是 LLM 推理的核心组件，reward hacking 是 RLHF/RLVR 的核心问题。如果能建立校准→鲁棒性的因果链，对实践有直接指导意义（\"先校准再用 PRM 做 RL\"）。\n  \n- **负面**: \n  - 实际影响可能有限——如果结论是 \"校准有帮助\"，practitioners 已经有动机去做校准（因为校准本身就改善 BoN 性能，如 Distributional PRM 所示）。这个工作可能只是为已有实践提供了因果层面的解释，而非开辟新实践。\n  - CGSP 的实用性取决于其相对 simpler baselines（如 temperature scaling + ensemble-min）的增量收益大小。如果增量很小，方法的复杂度不值得。\n  - 研究问题虽然重要，但 \"桥接两个线程\" 的贡献类型在顶会中通常被视为 solid but not exciting。\n\n### 3. Related Work: 强 (偏中)\n\n**理由**：\n\n- **正面**: 对两条主线（PRM Calibration 和 PRM Hackability）的覆盖非常详尽，差异化定位清晰。对 Ackermann et al. 的区分论述（outcome-level vs. step-level）有说服力。对 Caution、InferenceTimePessimism、URM 等相邻工作的区分也到位。\n\n- **负面**: \n  - **遗漏了 CRA (arXiv:2508.04216)**——这是一个从因果视角处理 PRM reward hacking 的直接竞争工作，未引用是严重疏忽。\n  - **遗漏了 PURM (arXiv:2503.22480)**——概率化不确定性奖励建模，概念上与 CGSP 高度相关。\n  - **遗漏了 Pessimistic RM (arXiv:2505.20556)**——悲观奖励建模的理论工作。\n  - 这些遗漏可能导致审稿人认为 proposal 的 novelty 声明过于强烈。\n\n---\n\n```\n【概率估计】: 20% - 32%，中位 25%\n```\n\n（注：此概率基于投稿至合适 venue 如 NeurIPS/ICML/ICLR。**若投稿 CoRL，概率为 ~0%，因 scope 完全不匹配。**）\n\n```\n【估计理由】:\n```\n\nIdea 的研究问题定位是真实的——PRM 校准与可攻击性之间的因果关系确实未被直接研究。但核心贡献受三个因素限制：\n\n1. **Novelty 上界受限**（最主要制约因素）：核心发现若 positive（\"校准好→更难攻击\"），审稿人反应大概率是 \"makes sense, I would have guessed this\"。CRA 已经从因果视角切入 PRM reward hacking，PURM/Pessimistic RM 已经在做不确定性悲观防御。CGSP 的公式是标准 LCB。整体 novelty 是增量级别的组合创新，而非范式级别的新洞察。\n\n2. **Trivial alternative 威胁真实**：temperature scaling 一个参数就可能解释大部分效果，且这个 trivial baseline 是 proposal 自己实验的一部分——如果它效果就很好，paper 的 story 会很尴尬。\n\n3. **因果隔离方法论有漏洞**：post-hoc calibration 改变梯度 landscape 的副作用可能混淆因果推断，使 \"calibration per se causes robustness\" 的声明站不住脚。\n\n这些因素将 idea 定位在 \"方向正确、有真实 delta、但核心发现不 surprising\" 的区间（25-35% 的下半部分）。\n\n```\n【主要风险】:\n```\n\n1. **\"I would have guessed this\" 风险**: 如果核心实验结论是 \"better calibrated PRMs are more robust\"，审稿人可能认为这是一个 trivially expected result，缺乏 surprising insight。这是最大的 idea 层面风险。\n\n2. **因果声明被攻击的风险**: 审稿人可能指出 post-hoc calibration（尤其是 temperature scaling）改变梯度 landscape 是其降低 hackability 的真正机制（而非\"校准\"本身），从而瓦解 \"calibration causally determines hackability\" 的核心 claim。同时 CRA 的存在削弱 \"first causal study\" 的声明。\n\n---\n\nSources:\n- [Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)\n- [Distributional PRMs via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)\n- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)\n- [Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)\n- [APRM: Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)\n- [From Curiosity to Caution](https://arxiv.org/abs/2604.04648)\n- [Causal Reward Adjustment (CRA)](https://arxiv.org/abs/2508.04216)\n- [Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/abs/2503.22480)\n- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命性前置问题：会议选择严重不匹配】\n\n在进入 idea 质量评估之前，必须首先指出一个致命问题：\n\n本 proposal 投稿目标是 **CoRL 2026（Conference on Robot Learning）**。\nCoRL 官方 Call for Papers 明确声明：\n  - \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n  - \"Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 研究的是 **PRM（Process Reward Model）校准与 LLM 数学推理中的 reward hacking 防御**，与机器人学习毫无关系。这不是 scope 边缘的问题——这是完全不在 scope 内，**会被 desk reject**。\n\n如投稿 CoRL，中稿概率为 **0%**。\n\n以下评估假设投稿到合适会议（NeurIPS / ICML / ICLR 2026），仅评估 idea 质量本身。\n\n---\n\n【领域调研】:\n\n1. **Park et al., \"Know What You Don't Know: Uncertainty Calibration of PRMs\"** (arXiv:2506.09338, NeurIPS 2025):\n   - 发现 PRM 系统性高估困难问题的成功概率；提出 instance-adaptive scaling 校准框架。\n   - 与本 proposal 关系：直接的 Thread 1 前置工作，proposal 正确引用。\n\n2. **Ma et al., \"Distributional Process Reward Models\"** (arXiv:2605.06785, May 2026):\n   - 首次将 conditional optimal transport 用于 PRM 校准，产出校准过的单调分位数函数。\n   - 与本 proposal 关系：proposal 引用为 opportunity，描述准确。此文未测试鲁棒性，确实留下了 gap。\n\n3. **Tiwari et al., \"Reward Under Attack\"** (arXiv:2603.06621, March 2026):\n   - 发现梯度攻击可将 PRM reward 膨胀 4×，RL 训练后 PRM reward >0.9 但实际准确率 <4%，43% 的 reward 增益来自风格捷径。\n   - 与本 proposal 关系：直接的 Thread 2 前置工作，proposal 正确引用。\n\n4. **Ackermann et al., \"Gradient Regularization Prevents Reward Hacking\"** (arXiv:2602.18037, Feb 2026):\n   - 建立 reward surface 平坦度与准确率保持之间的理论联系，提出梯度正则化。\n   - 与本 proposal 关系：proposal 声称此文仅处理 outcome-level 单标量 reward，而本文扩展到 step-level——这一差异化定位基本成立。\n\n5. **Yu et al., \"From Curiosity to Caution\"** (arXiv:2604.04648, April 2026):\n   - 将悲观主义原则应用于 BoN，使用 prediction error 作为不确定性代理降低 atypical 响应的 reward 估计。\n   - 与本 proposal 关系：CGSP 的直接竞争者。Caution 使用 prediction error（非校准概率），CGSP 声称使用校准概率更有原则——但实际性能差异未知。\n\n6. **⚠️ PURE: \"Stop Summation: Min-Form Credit Assignment\"** (arXiv:2504.15275, NeurIPS 2025):\n   - 发现求和式 credit assignment 是 PRM reward hacking 的根本原因；提出 min-form credit assignment，用最小值而非求和，显著缓解 reward hacking。\n   - 与本 proposal 关系：**proposal 完全未引用此文**。这是一个严重遗漏——PURE 是比 CGSP 更简单的 step-level PRM 防御方案，直接构成 trivial alternative 威胁。\n\n7. **⚠️ CRA: \"Causal Reward Adjustment\"** (arXiv:2508.04216):\n   - 使用 sparse autoencoders 解析 PRM 内部激活，通过后门校正估计真实 reward，缓解外部推理中的 reward hacking。\n   - 与本 proposal 关系：**proposal 未引用**。另一种因果视角下的 PRM reward hacking 防御。\n\n8. **PURM: \"Probabilistic Uncertain Reward Model\"** (arXiv:2503.22480):\n   - 将标量 reward 输出泛化为高斯分布，利用 Bhattacharyya 系数量化 reward 不确定性，在高不确定性区域施加惩罚。\n   - 与本 proposal 关系：**proposal 未引用**。PURM 的 idea 核心（不确定性感知的 reward 惩罚）与 CGSP 高度重叠。\n\n9. **BNRM: \"Bayesian Non-negative Reward Modeling\"** (arXiv:2602.10623):\n   - 基于贝叶斯的不确定性感知 reward 学习，显著缓解分布偏移下的 reward 过优化。\n   - 与本 proposal 关系：**proposal 未引用**。另一种 uncertainty-aware reward defense。\n\n10. **EDU-PRM: \"More Bang for the Buck\"** (arXiv:2503.22233, March 2026):\n    - 使用熵驱动不确定性进行 PRM 训练，仅用 1.5% 数据达到 strong baseline 水平。\n    - 与本 proposal 关系：未引用，属于 PRM 校准/不确定性的相关工作。\n\n- **调研总结**：PRM 校准和 PRM 可攻击性分别是 2025-2026 年活跃的研究方向。Proposal 正确识别了两个 thread 之间缺乏交叉引用这一 gap。但\"利用不确定性/校准来防御 reward hacking\"这个大方向上，已有多项并行工作（PURM、BNRM、Caution、PURE），且 proposal 遗漏了其中大部分。CGSP 相对于这些工作的增量 novelty 需要更仔细审视。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在至少两个成本更低的 trivial alternative 构成严重威胁：**\n\n1. **温度缩放（Temperature Scaling）+ 标准 RL 训练**：温度缩放是 proposal 自己列出的 Tier 1 校准方法之一，仅需拟合单个参数。如果实验结果显示温度缩放已经显著降低 hackability（这在 Component A 的 correlation study 中很可能出现），那么 CGSP 的全套机制（calibration quality score c_t、rolling buffer ECE、drift detector）的增量价值就会大打折扣。Proposal 需要证明 CGSP 的 adaptive 特性在 distribution shift 场景下显著优于 simple post-hoc calibration，但这是实验问题，不是 idea 层面能保证的。\n\n2. **PURE（Min-form Credit Assignment）**：PURE 通过将求和式 credit assignment 改为 min-form，从更根本的层面解决 PRM reward hacking，且无需任何校准步骤。如果 PURE 在相同 benchmark 上表现相当或更好，CGSP 的复杂性就难以正当化。Proposal 完全没有引用或讨论 PURE，这是一个严重疏忽。\n\n**增量价值的唯一合理论点**：CGSP 声称其优势在于 (i) 适应性（随分布偏移自动调整悲观程度）和 (ii) 基于校准概率而非启发式代理。但这些优势是否能转化为实际性能提升，完全依赖实验结果。从 idea 层面看，\"用校准不确定性做悲观 reward shaping\" 不是一个新的 insight——PURM 和 BNRM 已经在做类似的事情。\n\n---\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的假设：\n\n1. **\"校准质量因果性地决定 hackability\"**：这是整篇论文的中心 claim。逻辑上直觉合理（校准好 = 概率准确 = 不易被膨胀），但存在反向推理的风险：一个模型可能因为学到了更好的内部表征而同时变得更校准且更不可攻击——此时校准只是伴随现象，不是因果因素。Proposal 意识到了这个问题（Component B 的 causal isolation），但 post-hoc 校准方法\"不改变表征\"的说法需要谨慎——虽然 post-hoc 方法不改变模型参数，但梯度攻击通过反向传播计算梯度时，输出层的变换会改变梯度路径，因此\"representation-preserving\"在攻击场景下的含义并不像表面看起来那么简单。\n\n2. **\"Step-level 校准比 outcome-level 更重要\"**：Proposal 暗示 step-level 操作是 CGSP 的关键优势，但没有任何先验证据支持这一假设。可能 outcome-level 校准已经足够，step-level 的细粒度控制带来的边际收益很小。\n\n3. **\"CGSP 公式 r̃_t = μ_t − α·σ_t/√c_t 中的 calibration quality score c_t 可以可靠估计\"**：c_t 基于 rolling buffer 上的 ECE 计算。但 ECE 本身在小样本上非常不稳定，rolling buffer 的窗口大小选择会显著影响 c_t 的质量。这引入了额外的超参数敏感性，可能抵消\"自适应\"带来的好处。\n\n4. **\"Calibration Drift Detector 能在分布偏移发生时实时检测\"**：如果 RL 策略已经偏移到 PRM 校准失效的区域，用该区域的 rollout 计算 ECE 是否还有意义？这里有一个鸡生蛋、蛋生鸡的问题。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** —— \n   - \"PRM 校准与 hackability 的因果联系\"是一个 well-motivated gap，但核心 insight 的 surprisingness 有限。如果实验证实校准确实因果性地降低 hackability，审稿人更可能的反应是 \"this makes sense, I would have guessed this\" 而非 \"surprising\"。\n   - Causal isolation 方法学（post-hoc vs fine-tuning + CKA 验证）在这一特定 context 下是新的，但方法学本身（温度缩放作为 representation-preserving 控制）并不新颖。\n   - CGSP 作为防御方法，\"不确定性感知的悲观 reward shaping\" 已被 PURM (arXiv:2503.22480) 和 BNRM (arXiv:2602.10623) 在 outcome-level 实现；step-level 的扩展是增量贡献而非范式创新。\n   - Hessian spectral analysis 扩展 Ackermann 等人的工作到 step-level 是合理的增量贡献，但不足以支撑独立的 novelty claim。\n   - **关键问题**：proposal 的核心 narrative 是\"首次连接两个孤立的 thread\"，但 PURE、CRA、PURM 等工作表明这个连接正在被多条路径同时建立，先发优势窗口可能已经缩小。\n\n2. **Significance: 中** —— \n   - 研究问题是重要的：PRM reward hacking 是 LLM 推理 scaling 的关键瓶颈，任何有效防御都有实际价值。Tiwari et al. (arXiv:2603.06621) 显示的 <4% 准确率 vs. >0.9 PRM reward 的鸿沟表明问题严重性。\n   - 但 CGSP 即使有效，也是一种\"中等影响\"的贡献——它是 reward shaping 的改进版，不是根本性的新范式。PURE 的 min-form credit assignment 提出了一种更根本的解决思路。\n   - 因果分析部分（Component A-B）如果做得好，可以成为该领域的有价值参考，但属于\"实证 characterization\" 类贡献，影响力取决于发现是否 surprising。\n\n3. **Related Work: 弱** —— \n   - Proposal 对 Thread 1（PRM Calibration）和 Thread 2（PRM Hackability）的覆盖基本完整。\n   - 但**严重遗漏了至少 4 篇高度相关的工作**：PURE (arXiv:2504.15275, NeurIPS 2025)、PURM (arXiv:2503.22480)、BNRM (arXiv:2602.10623)、CRA (arXiv:2508.04216)。这些遗漏不是边缘相关文献——PURE 直接解决同一问题（step-level PRM reward hacking 防御），PURM 和 BNRM 直接实现了类似的 idea（uncertainty-aware reward penalization）。\n   - 如果提交到顶会，审稿人大概率会在第一轮就指出这些遗漏，严重影响可信度。\n   - Proposal 声称\"两个 thread 之间零交叉引用\"——但从调研来看，多项 2025-2026 年的工作已经在不同程度上建立了不确定性/校准与 reward hacking 之间的联系。\n\n---\n\n【概率估计】: [18% - 28%] 中位 22%\n\n（注：此估计基于假设投稿到合适会议如 NeurIPS/ICML/ICLR。若投稿 CoRL，概率为 0%——desk reject。）\n\n【估计理由】:\n\n- 方向正确，研究问题确实重要（Significance 中），这保证了 idea 不会被认为 trivially uninteresting。\n- 但 Novelty 是最大的限制因素：核心发现（校准 → 抗攻击）如果是 positive，审稿人大概率反应是 \"makes sense\" 而非 \"surprising\"；CGSP 作为防御方法，在已有 PURM/BNRM/Caution/PURE 的背景下，增量 novelty 有限。\n- Related Work 的严重遗漏（特别是 PURE）会被审稿人视为对领域不够了解的信号，直接压低分数。\n- 如果能在迭代中（1）补充所有遗漏的 related work 并做清晰的差异化定位，（2）在 CGSP 实验中加入 PURE 作为 baseline 并证明显著优势，（3）在 causal isolation 实验中得到 clean 的因果证据，概率可以提升到 25-30% 区间。但这些都需要实验支撑，idea 层面的上限受限于 novelty 天花板。\n\n【主要风险】:\n\n1. **Trivial alternative 威胁**：PURE（min-form credit assignment）是一个更简单、更根本的 PRM reward hacking 解决方案。如果 PURE 在相同 benchmark 上表现相当，审稿人会质疑 CGSP 复杂机制的必要性。Proposal 完全没有讨论这个 alternative，暴露了对竞争格局的盲区。\n\n2. **\"I would have guessed this\" 风险**：核心发现（校准好的 PRM 更难被 hack）在逻辑上过于符合直觉。即使因果证据 clean，审稿人可能认为这是 expected result 而非 novel insight，将论文评为\"solid but incremental empirical study\"——这在顶会通常不够。\n```\n\n---\n\nSources:\n- [Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)\n- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)\n- [Reward Under Attack: Analyzing the Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)\n- [Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)\n- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)\n- [Stop Summation: Min-Form Credit Assignment (PURE)](https://arxiv.org/abs/2504.15275)\n- [Causal Reward Adjustment (CRA)](https://arxiv.org/abs/2508.04216)\n- [Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/abs/2503.22480)\n- [Bayesian Non-negative Reward Modeling (BNRM)](https://arxiv.org/abs/2602.10623)\n- [More Bang for the Buck: EDU-PRM](https://arxiv.org/abs/2503.22233)\n- [Inference-Time Reward Hacking in LLMs](https://arxiv.org/abs/2506.19248)\n- [Detecting and Suppressing Reward Hacking with Gradient Fingerprints](https://arxiv.org/abs/2604.16242)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my evaluation. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【致命前置问题：会议匹配性】\n\n⚠️ **本 proposal 与 CoRL 2026 存在致命的 venue mismatch。**\n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求：\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\" 并声明 **\"Submissions without a robotics focus will be returned without review\"**（即直接 desk reject）。\n\n本 proposal 研究的是 **PRM (Process Reward Model) 校准与奖励黑客攻击在 LLM 数学推理中的问题**，评估 benchmark 为 MATH-500 和 AIME，使用 GRPO 训练语言模型。全文没有任何 robotics 内容——没有机器人感知、控制、操作、导航，没有真实机器人实验或 sim-to-real 讨论。\n\n**这篇论文会在 CoRL 2026 被 desk reject，概率接近 100%。**\n\n本 proposal 的合适投稿会议应为 **NeurIPS 2026、ICML 2026、ICLR 2027、或 ACL/EMNLP 2026**。\n\n以下评估假设将 proposal 投至一个**合适的 ML/NLP venue**（如 NeurIPS/ICML），对 idea 本身质量进行客观打分。\n\n---\n\n【领域调研】:\n\n- **Park et al., \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" (arXiv:2506.09338, NeurIPS 2025)**: 首次系统性研究 PRM 校准问题，发现 PRM 在困难问题上系统性高估成功概率，提出 quantile regression 校准方法。与本 proposal 的 Thread 1 直接重叠，本 proposal 在其基础上扩展。\n  \n- **\"Distributional Process Reward Models\" (arXiv:2605.06785, May 2026)**: 使用 conditional optimal transport 实现校准的单调分位数函数，改进 BoN 搜索。**未测试鲁棒性**——这是本 proposal 声称要填补的空白。\n\n- **Tiwari et al., \"Reward Under Attack\" (arXiv:2603.06621, March 2026)**: 全面分析 PRM 可攻击性——gradient 攻击可 4× 膨胀 reward，RL 训练可达近完美 PRM reward 但实际准确率 <4%，43% reward gain 来自 stylistic shortcuts。与本 proposal 的 Thread 2 直接重叠。**该论文未提出校准相关防御。**\n\n- **Ackermann et al., \"Gradient Regularization Prevents Reward Hacking\" (arXiv:2602.18037, Feb 2026)**: 建立 reward surface flatness 与 accuracy retention 的理论联系，提出梯度正则化。**仅在 outcome-level RM 上工作，不涉及 step-level PRM。** 本 proposal 声称将其 Hessian 分析扩展到 step-level。\n\n- **\"From Curiosity to Caution\" (arXiv:2604.04648, April 2026)**: 使用 pessimism 缓解 BoN reward hacking，但使用 prediction error 作为不确定性代理，非校准概率。\n\n- **\"Causal Reward Adjustment\" (arXiv:2508.04216)**: 使用 SAE 提取可解释特征 + backdoor adjustment 来修正 PRM reward。这是一个**直接竞争工作**，同样使用因果框架来抗 reward hacking，但方法论不同（SAE-based vs. calibration-based）。\n\n- **\"Learning a Pessimistic Reward Model in RLHF\" (arXiv:2505.20556, May 2025)**: 直接学习 pessimistic reward model 来防止 reward hacking，无需 KL 正则化。方法论上与 CGSP 竞争——区别在于 CGSP 是 step-level 且基于校准。\n\n- **调研总结**: PRM 校准和 PRM hackability 确实是两个近乎零交叉引用的成熟研究线。本 proposal 准确识别了这一空白。但\"更好校准 → 更难被攻击\"的直觉是强的（近乎显然的），真正的贡献取决于这个关系是否比直觉预期更强/更弱/更复杂。同时，pessimism-based reward hacking defense 本身已是一个拥挤的方向。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。**\n\n1. **简单温度缩放 + 固定悲观系数**: 不需要 CGSP 的复杂自适应机制（rolling ECE buffer、drift detector），直接对 PRM 做 temperature scaling 然后使用固定 LCB r̃_t = μ_t − α·σ_t 是否效果相当？CGSP 中的 c_t（rolling calibration quality）和 drift detector 增加的是工程复杂度——如果 ablation 显示它们贡献不大，则 CGSP 退化为标准 LCB。\n\n2. **Ensemble disagreement**: Ensemble minimum（Coste et al.）已经是 baseline，但一个更 strong 的 trivial alternative 是 ensemble 加上简单的 temperature scaling——这不需要 CGSP 的机制但可能达到类似效果。\n\n3. **核心问题**：CGSP 的 formula r̃_t = μ_t − α·σ_t/√c_t 本质上是 LCB (Lower Confidence Bound) 的一个变体，在 RL/bandit 文献中是标准技术。将其应用于 step-level PRM 是自然的工程延伸，而非方法论创新。增量价值主要在 c_t（calibration quality gating）这一项——但如果 c_t 的贡献在实验中不显著，整个 CGSP 的 novelty 就塌缩了。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未验证假设：\n\n1. **\"校准质量与 hackability 存在因果关系\"——这是 hypothesis，不是 premise，但 proposal 的措辞暗示它几乎是既定事实。** 如果实验发现 post-hoc calibration 改善了 ECE 但对 hackability 没有显著影响（即 calibration 和 hackability 共享的只是 confound——模型质量），整个论文的前提就崩溃了。虽然 proposal 设计了 dual-outcome 框架来处理这个风险，但这个假设本身的合理性值得审视：直觉上，校准修改的是 output mapping 的 scaling，而 gradient 攻击利用的是 hidden representation space 中的 sharp directions——这两者之间的联系并不显然。\n\n2. **\"Post-hoc calibration 不改变模型 representation\"——这是 claim，但需要验证。** Temperature scaling 理论上只改变 logit 的 scale，但在 PRM 的上下文中（尤其是 generative PRM 如 GenPRM），\"output mapping\" 的边界可能比预期模糊。\n\n3. **\"Step-level flatness 可以有意义地 compound across trajectory\"——这是 Component C 的核心假设。** 但 T 个 step reward 的 Hessian spectral特性如何组合成 trajectory-level 的 hackability 特征，缺乏先验理论支撑。这可能只是一个有趣的分析，而非一个 well-grounded 的理论贡献。\n\n4. **\"Rolling ECE on current-policy rollouts 可以可靠检测 distribution shift\"——CGSP 的 Calibration Drift Detector 依赖此假设。** 但 ECE 本身是一个有 bias 的 estimator（尤其在小 sample 下），rolling buffer 的大小和更新频率可能严重影响可靠性。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — \n   - 识别 PRM calibration 和 hackability 两个线程的 gap 是真实的贡献，但这种\"bridge two threads\"的 novelty 模式在审稿人眼中通常被视为\"连接工作\"（connecting work），novelty 上限有限。\n   - CGSP 本质上是 LCB（Lower Confidence Bound）在 step-level PRM 上的应用，加上一个 calibration quality gating 项。LCB 在 RL 和 bandit 文献中是成熟技术（pessimism in face of uncertainty 是 offline RL 的核心原则）。将其称为\"novel defense\"有些 overclaim。\n   - Hessian spectral analysis 从 outcome-level 到 step-level 的扩展是增量贡献。\n   - \"Causal Reward Adjustment\" (arXiv:2508.04216) 已经在因果框架下做 PRM reward hacking defense，虽然方法不同，但削弱了\"首个因果严谨研究\"的 claim。\n   - **支撑**: Ackermann et al. (arXiv:2602.18037) 的梯度正则化、Caution (arXiv:2604.04648) 的悲观主义、Pessimistic RM (arXiv:2505.20556) 的直接 pessimistic 建模，共同说明 pessimism-based defense 已是拥挤方向。\n\n2. **Significance: 中** —\n   - 研究问题是重要的：PRM 在 LLM 推理管线中的 reward hacking 是实际痛点。\n   - 但影响面受限于 PRM-guided mathematical reasoning 场景（MATH-500, AIME），向 general RLHF、code generation、或其他 domain 的推广性不明确。\n   - 如果核心发现是 positive（calibration 确实 causally determines hackability），审稿人的反应更可能是 **\"I would have guessed this\"** 而非 \"surprising\"——直觉上，一个给出过度自信 wrong prediction 的 PRM 当然更容易被 exploit。\n   - 如果发现是 negative（calibration 和 hackability 只有弱相关），反而更 surprising 且更有价值。\n\n3. **Related Work: 强** —\n   - Proposal 对相关工作的覆盖非常全面，准确识别了 3 个研究线程及其空白。\n   - 引用的关键论文经搜索验证均真实存在且描述准确。\n   - 与 Ackermann et al. 的技术差异化定位清晰（outcome-level vs. step-level，gradient norm vs. Hessian spectra）。\n   - 与 Caution、ensemble methods、APRM 的比较也准确。\n   - **不足**: 未引用 \"Causal Reward Adjustment\" (arXiv:2508.04216) 和 \"Learning a Pessimistic Reward Model\" (arXiv:2505.20556)，这两篇是直接竞争工作。\n\n---\n\n【概率估计】: 20% - 32%，中位 25%\n\n（注：此为投稿至合适 venue 如 NeurIPS/ICML 的估计。投稿 CoRL 2026 的中稿概率为 ~0%，会被 desk reject。）\n\n【估计理由】:\n- Related Work 覆盖充分（强），proposal 形式上非常完善，实验设计详尽——这些保证了下限不会太低。\n- 但 **Novelty 是限制上界的关键维度**：核心方法 CGSP 是 LCB 在 step-level PRM 的标准应用；\"bridge two threads\" 的贡献模式在 top venue 中 novelty 评分通常中偏低；pessimism-based defense 方向已拥挤。\n- **Significance 的\"I would have guessed this\"风险** 进一步压低上界：核心假设（better calibration → harder to hack）直觉上几乎是显然的，positive result 不会 surprising。\n- 概率区间 20-32% 对应 rubric 中的\"idea 有实质内核但核心发现审稿人可能觉得 expected\"区间的下半段，因为 trivial alternative 威胁（简单 temperature scaling + 固定 LCB）显著。\n\n【主要风险】:\n1. **\"Obvious hypothesis\" 风险**: \"校准好的 PRM 更难被 hack\" 这个核心 claim 直觉上太 natural，positive result 缺乏 surprise value；negative result 反而更有 paper value 但 proposal 并非围绕这个 framing 设计。\n2. **Trivial alternative 威胁**: 简单的 temperature scaling + 固定 pessimism coefficient 可能达到 CGSP 的大部分效果，使 CGSP 的自适应机制（c_t gating, drift detector）看起来是不必要的工程复杂度而非方法论贡献。\n```\n\n---\n\n**补充说明（会议选择）：**\n\n本 proposal 的内容——PRM 校准、reward hacking 防御、LLM 数学推理——完全属于 NLP/ML 领域。CoRL 2026 明确声明 \"Submissions without a robotics focus will be returned without review\"。建议重新选择投稿目标：\n\n- **NeurIPS 2026**（deadline 通常 5 月底）：最匹配，涵盖 RL、reward modeling、LLM alignment\n- **ICML 2026**：如已错过 deadline\n- **ICLR 2027**：如需更多实验时间\n- **EMNLP 2026**：如侧重 NLP 应用面\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)\n- [Distributional Process Reward Models](https://arxiv.org/html/2605.06785)\n- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)\n- [Gradient Regularization Prevents Reward Hacking in RLHF](https://arxiv.org/abs/2602.18037)\n- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/pdf/2604.04648)\n- [Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction](https://arxiv.org/pdf/2508.04216)\n- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/pdf/2505.20556)\n- [Reward Hacking Defense Rubric - Emergent Mind](https://www.emergentmind.com/topics/reward-hacking-defense-rubric)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n\n## Core Problem\nPRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.\n\n## Opportunity\nThree recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.\n\n## Related Work / Landscape\nTwo parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.\n\n## Approach\nThe study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.\n\n**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.\n\n**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.\n\n**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.\n\n**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.\n\nBaseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).\n\nCodebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.\n\n## Inspiration\nField guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone\n\n## Key References\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)\n- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)\n- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)\n- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)\n- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)\n- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)\n- Uncertainty-Aware Reward Model (arXiv:2410.00847)\n- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)\n- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)\n- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)\n- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}\n- **human_in_loop**: {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}\n- **auto_research**: {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T18:58:46.778Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:58:46.778Z",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T18:58:46.789Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
现在我有了足够的调研信息来进行评估。让我整理分析。

---

```
【阶段】: Triage
```

## ⚠️ 致命问题：严重的投稿venue不匹配

**在进入正式评估之前，必须首先指出一个致命问题：CoRL（Conference on Robot Learning）是一个机器人学习会议**，其征稿范围明确包括：robot perception、robot control、manipulation、locomotion、sim-to-real transfer、robot foundation models 等。本 proposal 研究的是 LLM 数学推理中的 PRM 校准与 reward hacking 防御（评测数据集为 MATH-500 和 AIME），与机器人学习**零关联**。提交至 CoRL 几乎必然被 desk reject。

**如果投稿目标确实是 CoRL，中稿概率接近 0%，无需进一步评估。**

以下评估假设 proposal 将投稿至**合适的 venue（如 NeurIPS、ICML、ICLR 等 ML/NLP 顶会）**，仅评估 idea 本身的质量。

---

```
【领域调研】:
```

- **[Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)** (NeurIPS 2025): 首次系统性研究 PRM 校准问题，发现 PRM 在难题上系统性高估成功概率，提出 quantile regression 校准方法。是 Thread 1 (PRM Calibration) 的奠基工作。本 proposal 的 Component A 直接建立在此基础上。

- **[Distributional PRMs via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)** (May 2026 preprint): 用条件最优传输获得校准的单调分位数函数，改善 BoN 在 MATH-500 和 AIME 上的表现。**从未测试鲁棒性/抗攻击能力**——这正是本 proposal 声称要填补的空白。

- **[Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)** (March 2026): 证明 PRM 是灾难性可攻击的——梯度攻击使 PRM 奖励膨胀 4 倍，RL 训练达到近乎完美的 PRM 奖励但实际准确率 <4%，43% 的奖励增益来自风格捷径。**未提出任何基于校准的防御**。本 proposal 的 Thread 2 基础。

- **[Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)** (Feb 2026, Ackermann et al.): 建立了奖励表面平坦度与准确度保持之间的理论联系，提出梯度正则化偏向平坦区域。**仅在 outcome-level 单标量奖励模型上工作**，未涉及 step-level PRM。本 proposal 声称要将此扩展到 step-level Hessian 分析。

- **[APRM: Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)** (Nov 2025): 对抗训练 PRM，+3.4pp 鲁棒性改善。是 proposal 的 baseline 之一。

- **[From Curiosity to Caution (Caution)](https://arxiv.org/abs/2604.04648)** (April 2026): 使用 prediction error 作为悲观度代理进行 BoN 防御。**使用未校准的不确定性代理，非校准概率**。是 proposal 的 baseline 之一。

- **[Causal Reward Adjustment (CRA)](https://arxiv.org/abs/2508.04216)** (2025): ⚠️ **proposal 未引用此论文**。CRA 用稀疏自编码器识别 PRM 内部的混淆特征，通过 backdoor adjustment 进行因果校正以缓解 reward hacking。虽然机制不同（SAE vs. 校准），但同样是**因果视角下的 PRM reward hacking 防御**，直接威胁 proposal 的 "first causally rigorous study" 声明。

- **[Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/abs/2503.22480)** (March 2025): 将标量奖励推广为高斯分布，用不确定性惩罚防止过优化。概念上与 CGSP 的 LCB 思路类似，但在 outcome-level。

- **[Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)** (May 2025): 通过 minimax 目标训练悲观代理奖励作为真实奖励的下界。理论上与 CGSP 的悲观主义方向相似。

- **调研总结**: PRM 校准和 PRM 可攻击性确实是两个相对独立的研究线程，但"桥接"的空间正在被多个方向的工作侵蚀。CRA (2508.04216) 已经从因果视角处理 PRM reward hacking；PURM 和 Pessimistic RM 已经在做不确定性驱动的悲观防御。本 proposal 的独特角色——"用校准质量作为因果变量"——仍有真实的 delta，但并非如 proposal 所声称的那样是一片完全未被触及的空白。

---

```
【Trivial Alternative 检验】:
```

**存在显著的 trivial alternative 威胁。**

核心问题：如果 "更好的校准 → 更强的抗攻击能力"，那最简单的 trivial baseline 就是——**直接对 PRM 做 temperature scaling（一个参数的 post-hoc 校准），然后测试抗攻击能力是否改善**。这实际上就是 proposal 自己 Component B1 的一部分。

如果 temperature scaling 就能显著降低 hackability，那么：
1. 整个 48-configuration 相关性研究的增量价值被大幅削弱（一个参数就够了）
2. CGSP 的复杂公式（μ_t − α·σ_t/√c_t）相对于 "简单校准 + 标准 LCB" 的增量价值需要严格论证
3. 因果隔离实验变得不那么必要——如果 post-hoc calibration 就有效，因果关系已经隐含地被建立了

**增量价值的真实所在**：如果只有 calibration 改善有效（而 CKA-matched representation change 无效），且 CGSP 的 adaptive pessimism 明显优于 static pessimism，那 proposal 的贡献才能站住脚。但这取决于实验结果，idea 层面上这个风险是真实的。

另一个 trivial alternative：**ensemble disagreement**（已有工作如 Coste et al.）已经是一种不确定性驱动的悲观方法。CGSP 相比 ensemble-min 的增量需要仔细论证——proposal 声称 ensemble 是 "uncalibrated"，但 ensemble disagreement 本身就是一种合理的不确定性度量，不需要显式校准。

---

```
【前提假设检验】:
```

核心 claim 的逻辑链条：

**校准质量高 → 奖励信号更准确 → 梯度攻击/RL优化更难利用 → hackability 降低**

这条链中有两个关键的未验证假设：

1. **"校准 = 准确"的等式假设**: 校准（calibration）衡量的是 "预测概率与真实频率的匹配度"，但一个完美校准的模型仍然可能有 sharp but exploitable 的奖励表面。校准改善的是概率输出的可靠性，但未必改变模型在对抗性输入上的决策边界。一个 well-calibrated 但在特定 adversarial direction 上仍然脆弱的 PRM 是完全可能的。**Proposal 隐含假设校准改善等同于鲁棒性改善，这个等式没有理论保证。**

2. **Post-hoc calibration "provably preserves representations" 的过度声明**: Temperature scaling 确实不改变 logits 的排序，但它改变了梯度的大小（因为 softmax 的温度影响梯度 landscape）。在梯度攻击场景下，temperature scaling 改变了 loss surface 的曲率，这可能影响攻击效果——但这不是 "calibration" 的功劳，而是 "gradient scaling" 的副作用。**因果隔离实验可能测到的不是"校准的因果效应"，而是"温度缩放改变梯度 landscape"的效应。**

3. **Step-level flatness compounding 假设**: Proposal 假设 step-level 的平坦度会以有意义的方式沿轨迹组合，影响 outcome-level hackability。但 T 个 step 的 Hessian 如何 "组合" 是一个非平凡的数学问题，proposal 没有给出任何理论框架说明这种组合如何工作。

---

```
【3 维度打分】:
```

### 1. Novelty: 中 (偏弱)

**理由**：

- **正面**: 将 PRM 校准线程与 PRM 可攻击性线程显式桥接，这个研究问题的定位是真实的——目前确实没有论文直接测试 "校准质量是否因果地决定抗攻击能力"。因果隔离实验设计（post-hoc vs. fine-tuning vs. matched representation change control）在方法论上有新意。

- **负面**:
  - **CRA (arXiv:2508.04216)** 已经从因果视角（用 backdoor adjustment）处理 PRM reward hacking 防御，且 proposal **未引用**此工作。"First causally rigorous study" 的声明可能被审稿人质疑。
  - CGSP 的核心公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是 **LCB (Lower Confidence Bound) 的标准形式**，加上 calibration quality 的加权。这在 bandit/offline RL 文献中是常见思路。创新性主要在于 "应用场景"（step-level PRM + RL training），而非算法本身。
  - **PURM (arXiv:2503.22480)** 和 **Pessimistic RM (arXiv:2505.20556)** 已经在做不确定性驱动的悲观奖励建模。CGSP 的差异化（step-level + calibration-gated）是增量的，不是范式级的。
  - 核心发现如果是 positive（"better calibrated PRMs are harder to hack"），多数审稿人的反应可能是 **"I would have guessed this"** 而非 "surprising"。

### 2. Significance: 中

**理由**：

- **正面**: PRM 是 LLM 推理的核心组件，reward hacking 是 RLHF/RLVR 的核心问题。如果能建立校准→鲁棒性的因果链，对实践有直接指导意义（"先校准再用 PRM 做 RL"）。
  
- **负面**: 
  - 实际影响可能有限——如果结论是 "校准有帮助"，practitioners 已经有动机去做校准（因为校准本身就改善 BoN 性能，如 Distributional PRM 所示）。这个工作可能只是为已有实践提供了因果层面的解释，而非开辟新实践。
  - CGSP 的实用性取决于其相对 simpler baselines（如 temperature scaling + ensemble-min）的增量收益大小。如果增量很小，方法的复杂度不值得。
  - 研究问题虽然重要，但 "桥接两个线程" 的贡献类型在顶会中通常被视为 solid but not exciting。

### 3. Related Work: 强 (偏中)

**理由**：

- **正面**: 对两条主线（PRM Calibration 和 PRM Hackability）的覆盖非常详尽，差异化定位清晰。对 Ackermann et al. 的区分论述（outcome-level vs. step-level）有说服力。对 Caution、InferenceTimePessimism、URM 等相邻工作的区分也到位。

- **负面**: 
  - **遗漏了 CRA (arXiv:2508.04216)**——这是一个从因果视角处理 PRM reward hacking 的直接竞争工作，未引用是严重疏忽。
  - **遗漏了 PURM (arXiv:2503.22480)**——概率化不确定性奖励建模，概念上与 CGSP 高度相关。
  - **遗漏了 Pessimistic RM (arXiv:2505.20556)**——悲观奖励建模的理论工作。
  - 这些遗漏可能导致审稿人认为 proposal 的 novelty 声明过于强烈。

---

```
【概率估计】: 20% - 32%，中位 25%
```

（注：此概率基于投稿至合适 venue 如 NeurIPS/ICML/ICLR。**若投稿 CoRL，概率为 ~0%，因 scope 完全不匹配。**）

```
【估计理由】:
```

Idea 的研究问题定位是真实的——PRM 校准与可攻击性之间的因果关系确实未被直接研究。但核心贡献受三个因素限制：

1. **Novelty 上界受限**（最主要制约因素）：核心发现若 positive（"校准好→更难攻击"），审稿人反应大概率是 "makes sense, I would have guessed this"。CRA 已经从因果视角切入 PRM reward hacking，PURM/Pessimistic RM 已经在做不确定性悲观防御。CGSP 的公式是标准 LCB。整体 novelty 是增量级别的组合创新，而非范式级别的新洞察。

2. **Trivial alternative 威胁真实**：temperature scaling 一个参数就可能解释大部分效果，且这个 trivial baseline 是 proposal 自己实验的一部分——如果它效果就很好，paper 的 story 会很尴尬。

3. **因果隔离方法论有漏洞**：post-hoc calibration 改变梯度 landscape 的副作用可能混淆因果推断，使 "calibration per se causes robustness" 的声明站不住脚。

这些因素将 idea 定位在 "方向正确、有真实 delta、但核心发现不 surprising" 的区间（25-35% 的下半部分）。

```
【主要风险】:
```

1. **"I would have guessed this" 风险**: 如果核心实验结论是 "better calibrated PRMs are more robust"，审稿人可能认为这是一个 trivially expected result，缺乏 surprising insight。这是最大的 idea 层面风险。

2. **因果声明被攻击的风险**: 审稿人可能指出 post-hoc calibration（尤其是 temperature scaling）改变梯度 landscape 是其降低 hackability 的真正机制（而非"校准"本身），从而瓦解 "calibration causally determines hackability" 的核心 claim。同时 CRA 的存在削弱 "first causal study" 的声明。

---

Sources:
- [Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)
- [Distributional PRMs via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)
- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)
- [APRM: Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)
- [From Curiosity to Caution](https://arxiv.org/abs/2604.04648)
- [Causal Reward Adjustment (CRA)](https://arxiv.org/abs/2508.04216)
- [Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/abs/2503.22480)
- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【⚠️ 致命性前置问题：会议选择严重不匹配】

在进入 idea 质量评估之前，必须首先指出一个致命问题：

本 proposal 投稿目标是 **CoRL 2026（Conference on Robot Learning）**。
CoRL 官方 Call for Papers 明确声明：
  - "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
  - "Submissions without a robotics focus will be returned without review."

本 proposal 研究的是 **PRM（Process Reward Model）校准与 LLM 数学推理中的 reward hacking 防御**，与机器人学习毫无关系。这不是 scope 边缘的问题——这是完全不在 scope 内，**会被 desk reject**。

如投稿 CoRL，中稿概率为 **0%**。

以下评估假设投稿到合适会议（NeurIPS / ICML / ICLR 2026），仅评估 idea 质量本身。

---

【领域调研】:

1. **Park et al., "Know What You Don't Know: Uncertainty Calibration of PRMs"** (arXiv:2506.09338, NeurIPS 2025):
   - 发现 PRM 系统性高估困难问题的成功概率；提出 instance-adaptive scaling 校准框架。
   - 与本 proposal 关系：直接的 Thread 1 前置工作，proposal 正确引用。

2. **Ma et al., "Distributional Process Reward Models"** (arXiv:2605.06785, May 2026):
   - 首次将 conditional optimal transport 用于 PRM 校准，产出校准过的单调分位数函数。
   - 与本 proposal 关系：proposal 引用为 opportunity，描述准确。此文未测试鲁棒性，确实留下了 gap。

3. **Tiwari et al., "Reward Under Attack"** (arXiv:2603.06621, March 2026):
   - 发现梯度攻击可将 PRM reward 膨胀 4×，RL 训练后 PRM reward >0.9 但实际准确率 <4%，43% 的 reward 增益来自风格捷径。
   - 与本 proposal 关系：直接的 Thread 2 前置工作，proposal 正确引用。

4. **Ackermann et al., "Gradient Regularization Prevents Reward Hacking"** (arXiv:2602.18037, Feb 2026):
   - 建立 reward surface 平坦度与准确率保持之间的理论联系，提出梯度正则化。
   - 与本 proposal 关系：proposal 声称此文仅处理 outcome-level 单标量 reward，而本文扩展到 step-level——这一差异化定位基本成立。

5. **Yu et al., "From Curiosity to Caution"** (arXiv:2604.04648, April 2026):
   - 将悲观主义原则应用于 BoN，使用 prediction error 作为不确定性代理降低 atypical 响应的 reward 估计。
   - 与本 proposal 关系：CGSP 的直接竞争者。Caution 使用 prediction error（非校准概率），CGSP 声称使用校准概率更有原则——但实际性能差异未知。

6. **⚠️ PURE: "Stop Summation: Min-Form Credit Assignment"** (arXiv:2504.15275, NeurIPS 2025):
   - 发现求和式 credit assignment 是 PRM reward hacking 的根本原因；提出 min-form credit assignment，用最小值而非求和，显著缓解 reward hacking。
   - 与本 proposal 关系：**proposal 完全未引用此文**。这是一个严重遗漏——PURE 是比 CGSP 更简单的 step-level PRM 防御方案，直接构成 trivial alternative 威胁。

7. **⚠️ CRA: "Causal Reward Adjustment"** (arXiv:2508.04216):
   - 使用 sparse autoencoders 解析 PRM 内部激活，通过后门校正估计真实 reward，缓解外部推理中的 reward hacking。
   - 与本 proposal 关系：**proposal 未引用**。另一种因果视角下的 PRM reward hacking 防御。

8. **PURM: "Probabilistic Uncertain Reward Model"** (arXiv:2503.22480):
   - 将标量 reward 输出泛化为高斯分布，利用 Bhattacharyya 系数量化 reward 不确定性，在高不确定性区域施加惩罚。
   - 与本 proposal 关系：**proposal 未引用**。PURM 的 idea 核心（不确定性感知的 reward 惩罚）与 CGSP 高度重叠。

9. **BNRM: "Bayesian Non-negative Reward Modeling"** (arXiv:2602.10623):
   - 基于贝叶斯的不确定性感知 reward 学习，显著缓解分布偏移下的 reward 过优化。
   - 与本 proposal 关系：**proposal 未引用**。另一种 uncertainty-aware reward defense。

10. **EDU-PRM: "More Bang for the Buck"** (arXiv:2503.22233, March 2026):
    - 使用熵驱动不确定性进行 PRM 训练，仅用 1.5% 数据达到 strong baseline 水平。
    - 与本 proposal 关系：未引用，属于 PRM 校准/不确定性的相关工作。

- **调研总结**：PRM 校准和 PRM 可攻击性分别是 2025-2026 年活跃的研究方向。Proposal 正确识别了两个 thread 之间缺乏交叉引用这一 gap。但"利用不确定性/校准来防御 reward hacking"这个大方向上，已有多项并行工作（PURM、BNRM、Caution、PURE），且 proposal 遗漏了其中大部分。CGSP 相对于这些工作的增量 novelty 需要更仔细审视。

---

【Trivial Alternative 检验】:

**存在至少两个成本更低的 trivial alternative 构成严重威胁：**

1. **温度缩放（Temperature Scaling）+ 标准 RL 训练**：温度缩放是 proposal 自己列出的 Tier 1 校准方法之一，仅需拟合单个参数。如果实验结果显示温度缩放已经显著降低 hackability（这在 Component A 的 correlation study 中很可能出现），那么 CGSP 的全套机制（calibration quality score c_t、rolling buffer ECE、drift detector）的增量价值就会大打折扣。Proposal 需要证明 CGSP 的 adaptive 特性在 distribution shift 场景下显著优于 simple post-hoc calibration，但这是实验问题，不是 idea 层面能保证的。

2. **PURE（Min-form Credit Assignment）**：PURE 通过将求和式 credit assignment 改为 min-form，从更根本的层面解决 PRM reward hacking，且无需任何校准步骤。如果 PURE 在相同 benchmark 上表现相当或更好，CGSP 的复杂性就难以正当化。Proposal 完全没有引用或讨论 PURE，这是一个严重疏忽。

**增量价值的唯一合理论点**：CGSP 声称其优势在于 (i) 适应性（随分布偏移自动调整悲观程度）和 (ii) 基于校准概率而非启发式代理。但这些优势是否能转化为实际性能提升，完全依赖实验结果。从 idea 层面看，"用校准不确定性做悲观 reward shaping" 不是一个新的 insight——PURM 和 BNRM 已经在做类似的事情。

---

【前提假设检验】:

核心逻辑链中有以下未经验证的假设：

1. **"校准质量因果性地决定 hackability"**：这是整篇论文的中心 claim。逻辑上直觉合理（校准好 = 概率准确 = 不易被膨胀），但存在反向推理的风险：一个模型可能因为学到了更好的内部表征而同时变得更校准且更不可攻击——此时校准只是伴随现象，不是因果因素。Proposal 意识到了这个问题（Component B 的 causal isolation），但 post-hoc 校准方法"不改变表征"的说法需要谨慎——虽然 post-hoc 方法不改变模型参数，但梯度攻击通过反向传播计算梯度时，输出层的变换会改变梯度路径，因此"representation-preserving"在攻击场景下的含义并不像表面看起来那么简单。

2. **"Step-level 校准比 outcome-level 更重要"**：Proposal 暗示 step-level 操作是 CGSP 的关键优势，但没有任何先验证据支持这一假设。可能 outcome-level 校准已经足够，step-level 的细粒度控制带来的边际收益很小。

3. **"CGSP 公式 r̃_t = μ_t − α·σ_t/√c_t 中的 calibration quality score c_t 可以可靠估计"**：c_t 基于 rolling buffer 上的 ECE 计算。但 ECE 本身在小样本上非常不稳定，rolling buffer 的窗口大小选择会显著影响 c_t 的质量。这引入了额外的超参数敏感性，可能抵消"自适应"带来的好处。

4. **"Calibration Drift Detector 能在分布偏移发生时实时检测"**：如果 RL 策略已经偏移到 PRM 校准失效的区域，用该区域的 rollout 计算 ECE 是否还有意义？这里有一个鸡生蛋、蛋生鸡的问题。

---

【3 维度打分】:

1. **Novelty: 弱-中** —— 
   - "PRM 校准与 hackability 的因果联系"是一个 well-motivated gap，但核心 insight 的 surprisingness 有限。如果实验证实校准确实因果性地降低 hackability，审稿人更可能的反应是 "this makes sense, I would have guessed this" 而非 "surprising"。
   - Causal isolation 方法学（post-hoc vs fine-tuning + CKA 验证）在这一特定 context 下是新的，但方法学本身（温度缩放作为 representation-preserving 控制）并不新颖。
   - CGSP 作为防御方法，"不确定性感知的悲观 reward shaping" 已被 PURM (arXiv:2503.22480) 和 BNRM (arXiv:2602.10623) 在 outcome-level 实现；step-level 的扩展是增量贡献而非范式创新。
   - Hessian spectral analysis 扩展 Ackermann 等人的工作到 step-level 是合理的增量贡献，但不足以支撑独立的 novelty claim。
   - **关键问题**：proposal 的核心 narrative 是"首次连接两个孤立的 thread"，但 PURE、CRA、PURM 等工作表明这个连接正在被多条路径同时建立，先发优势窗口可能已经缩小。

2. **Significance: 中** —— 
   - 研究问题是重要的：PRM reward hacking 是 LLM 推理 scaling 的关键瓶颈，任何有效防御都有实际价值。Tiwari et al. (arXiv:2603.06621) 显示的 <4% 准确率 vs. >0.9 PRM reward 的鸿沟表明问题严重性。
   - 但 CGSP 即使有效，也是一种"中等影响"的贡献——它是 reward shaping 的改进版，不是根本性的新范式。PURE 的 min-form credit assignment 提出了一种更根本的解决思路。
   - 因果分析部分（Component A-B）如果做得好，可以成为该领域的有价值参考，但属于"实证 characterization" 类贡献，影响力取决于发现是否 surprising。

3. **Related Work: 弱** —— 
   - Proposal 对 Thread 1（PRM Calibration）和 Thread 2（PRM Hackability）的覆盖基本完整。
   - 但**严重遗漏了至少 4 篇高度相关的工作**：PURE (arXiv:2504.15275, NeurIPS 2025)、PURM (arXiv:2503.22480)、BNRM (arXiv:2602.10623)、CRA (arXiv:2508.04216)。这些遗漏不是边缘相关文献——PURE 直接解决同一问题（step-level PRM reward hacking 防御），PURM 和 BNRM 直接实现了类似的 idea（uncertainty-aware reward penalization）。
   - 如果提交到顶会，审稿人大概率会在第一轮就指出这些遗漏，严重影响可信度。
   - Proposal 声称"两个 thread 之间零交叉引用"——但从调研来看，多项 2025-2026 年的工作已经在不同程度上建立了不确定性/校准与 reward hacking 之间的联系。

---

【概率估计】: [18% - 28%] 中位 22%

（注：此估计基于假设投稿到合适会议如 NeurIPS/ICML/ICLR。若投稿 CoRL，概率为 0%——desk reject。）

【估计理由】:

- 方向正确，研究问题确实重要（Significance 中），这保证了 idea 不会被认为 trivially uninteresting。
- 但 Novelty 是最大的限制因素：核心发现（校准 → 抗攻击）如果是 positive，审稿人大概率反应是 "makes sense" 而非 "surprising"；CGSP 作为防御方法，在已有 PURM/BNRM/Caution/PURE 的背景下，增量 novelty 有限。
- Related Work 的严重遗漏（特别是 PURE）会被审稿人视为对领域不够了解的信号，直接压低分数。
- 如果能在迭代中（1）补充所有遗漏的 related work 并做清晰的差异化定位，（2）在 CGSP 实验中加入 PURE 作为 baseline 并证明显著优势，（3）在 causal isolation 实验中得到 clean 的因果证据，概率可以提升到 25-30% 区间。但这些都需要实验支撑，idea 层面的上限受限于 novelty 天花板。

【主要风险】:

1. **Trivial alternative 威胁**：PURE（min-form credit assignment）是一个更简单、更根本的 PRM reward hacking 解决方案。如果 PURE 在相同 benchmark 上表现相当，审稿人会质疑 CGSP 复杂机制的必要性。Proposal 完全没有讨论这个 alternative，暴露了对竞争格局的盲区。

2. **"I would have guessed this" 风险**：核心发现（校准好的 PRM 更难被 hack）在逻辑上过于符合直觉。即使因果证据 clean，审稿人可能认为这是 expected result 而非 novel insight，将论文评为"solid but incremental empirical study"——这在顶会通常不够。
```

---

Sources:
- [Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)
- [Reward Under Attack: Analyzing the Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)
- [Stop Summation: Min-Form Credit Assignment (PURE)](https://arxiv.org/abs/2504.15275)
- [Causal Reward Adjustment (CRA)](https://arxiv.org/abs/2508.04216)
- [Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/abs/2503.22480)
- [Bayesian Non-negative Reward Modeling (BNRM)](https://arxiv.org/abs/2602.10623)
- [More Bang for the Buck: EDU-PRM](https://arxiv.org/abs/2503.22233)
- [Inference-Time Reward Hacking in LLMs](https://arxiv.org/abs/2506.19248)
- [Detecting and Suppressing Reward Hacking with Gradient Fingerprints](https://arxiv.org/abs/2604.16242)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to make my evaluation. Let me compile my findings.

---

```
【阶段】: Triage

【致命前置问题：会议匹配性】

⚠️ **本 proposal 与 CoRL 2026 存在致命的 venue mismatch。**

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求："Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." 并声明 **"Submissions without a robotics focus will be returned without review"**（即直接 desk reject）。

本 proposal 研究的是 **PRM (Process Reward Model) 校准与奖励黑客攻击在 LLM 数学推理中的问题**，评估 benchmark 为 MATH-500 和 AIME，使用 GRPO 训练语言模型。全文没有任何 robotics 内容——没有机器人感知、控制、操作、导航，没有真实机器人实验或 sim-to-real 讨论。

**这篇论文会在 CoRL 2026 被 desk reject，概率接近 100%。**

本 proposal 的合适投稿会议应为 **NeurIPS 2026、ICML 2026、ICLR 2027、或 ACL/EMNLP 2026**。

以下评估假设将 proposal 投至一个**合适的 ML/NLP venue**（如 NeurIPS/ICML），对 idea 本身质量进行客观打分。

---

【领域调研】:

- **Park et al., "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" (arXiv:2506.09338, NeurIPS 2025)**: 首次系统性研究 PRM 校准问题，发现 PRM 在困难问题上系统性高估成功概率，提出 quantile regression 校准方法。与本 proposal 的 Thread 1 直接重叠，本 proposal 在其基础上扩展。
  
- **"Distributional Process Reward Models" (arXiv:2605.06785, May 2026)**: 使用 conditional optimal transport 实现校准的单调分位数函数，改进 BoN 搜索。**未测试鲁棒性**——这是本 proposal 声称要填补的空白。

- **Tiwari et al., "Reward Under Attack" (arXiv:2603.06621, March 2026)**: 全面分析 PRM 可攻击性——gradient 攻击可 4× 膨胀 reward，RL 训练可达近完美 PRM reward 但实际准确率 <4%，43% reward gain 来自 stylistic shortcuts。与本 proposal 的 Thread 2 直接重叠。**该论文未提出校准相关防御。**

- **Ackermann et al., "Gradient Regularization Prevents Reward Hacking" (arXiv:2602.18037, Feb 2026)**: 建立 reward surface flatness 与 accuracy retention 的理论联系，提出梯度正则化。**仅在 outcome-level RM 上工作，不涉及 step-level PRM。** 本 proposal 声称将其 Hessian 分析扩展到 step-level。

- **"From Curiosity to Caution" (arXiv:2604.04648, April 2026)**: 使用 pessimism 缓解 BoN reward hacking，但使用 prediction error 作为不确定性代理，非校准概率。

- **"Causal Reward Adjustment" (arXiv:2508.04216)**: 使用 SAE 提取可解释特征 + backdoor adjustment 来修正 PRM reward。这是一个**直接竞争工作**，同样使用因果框架来抗 reward hacking，但方法论不同（SAE-based vs. calibration-based）。

- **"Learning a Pessimistic Reward Model in RLHF" (arXiv:2505.20556, May 2025)**: 直接学习 pessimistic reward model 来防止 reward hacking，无需 KL 正则化。方法论上与 CGSP 竞争——区别在于 CGSP 是 step-level 且基于校准。

- **调研总结**: PRM 校准和 PRM hackability 确实是两个近乎零交叉引用的成熟研究线。本 proposal 准确识别了这一空白。但"更好校准 → 更难被攻击"的直觉是强的（近乎显然的），真正的贡献取决于这个关系是否比直觉预期更强/更弱/更复杂。同时，pessimism-based reward hacking defense 本身已是一个拥挤的方向。

---

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

1. **简单温度缩放 + 固定悲观系数**: 不需要 CGSP 的复杂自适应机制（rolling ECE buffer、drift detector），直接对 PRM 做 temperature scaling 然后使用固定 LCB r̃_t = μ_t − α·σ_t 是否效果相当？CGSP 中的 c_t（rolling calibration quality）和 drift detector 增加的是工程复杂度——如果 ablation 显示它们贡献不大，则 CGSP 退化为标准 LCB。

2. **Ensemble disagreement**: Ensemble minimum（Coste et al.）已经是 baseline，但一个更 strong 的 trivial alternative 是 ensemble 加上简单的 temperature scaling——这不需要 CGSP 的机制但可能达到类似效果。

3. **核心问题**：CGSP 的 formula r̃_t = μ_t − α·σ_t/√c_t 本质上是 LCB (Lower Confidence Bound) 的一个变体，在 RL/bandit 文献中是标准技术。将其应用于 step-level PRM 是自然的工程延伸，而非方法论创新。增量价值主要在 c_t（calibration quality gating）这一项——但如果 c_t 的贡献在实验中不显著，整个 CGSP 的 novelty 就塌缩了。

---

【前提假设检验】:

核心 claim 的逻辑链中有以下未验证假设：

1. **"校准质量与 hackability 存在因果关系"——这是 hypothesis，不是 premise，但 proposal 的措辞暗示它几乎是既定事实。** 如果实验发现 post-hoc calibration 改善了 ECE 但对 hackability 没有显著影响（即 calibration 和 hackability 共享的只是 confound——模型质量），整个论文的前提就崩溃了。虽然 proposal 设计了 dual-outcome 框架来处理这个风险，但这个假设本身的合理性值得审视：直觉上，校准修改的是 output mapping 的 scaling，而 gradient 攻击利用的是 hidden representation space 中的 sharp directions——这两者之间的联系并不显然。

2. **"Post-hoc calibration 不改变模型 representation"——这是 claim，但需要验证。** Temperature scaling 理论上只改变 logit 的 scale，但在 PRM 的上下文中（尤其是 generative PRM 如 GenPRM），"output mapping" 的边界可能比预期模糊。

3. **"Step-level flatness 可以有意义地 compound across trajectory"——这是 Component C 的核心假设。** 但 T 个 step reward 的 Hessian spectral特性如何组合成 trajectory-level 的 hackability 特征，缺乏先验理论支撑。这可能只是一个有趣的分析，而非一个 well-grounded 的理论贡献。

4. **"Rolling ECE on current-policy rollouts 可以可靠检测 distribution shift"——CGSP 的 Calibration Drift Detector 依赖此假设。** 但 ECE 本身是一个有 bias 的 estimator（尤其在小 sample 下），rolling buffer 的大小和更新频率可能严重影响可靠性。

---

【3 维度打分】:

1. **Novelty: 中偏弱** — 
   - 识别 PRM calibration 和 hackability 两个线程的 gap 是真实的贡献，但这种"bridge two threads"的 novelty 模式在审稿人眼中通常被视为"连接工作"（connecting work），novelty 上限有限。
   - CGSP 本质上是 LCB（Lower Confidence Bound）在 step-level PRM 上的应用，加上一个 calibration quality gating 项。LCB 在 RL 和 bandit 文献中是成熟技术（pessimism in face of uncertainty 是 offline RL 的核心原则）。将其称为"novel defense"有些 overclaim。
   - Hessian spectral analysis 从 outcome-level 到 step-level 的扩展是增量贡献。
   - "Causal Reward Adjustment" (arXiv:2508.04216) 已经在因果框架下做 PRM reward hacking defense，虽然方法不同，但削弱了"首个因果严谨研究"的 claim。
   - **支撑**: Ackermann et al. (arXiv:2602.18037) 的梯度正则化、Caution (arXiv:2604.04648) 的悲观主义、Pessimistic RM (arXiv:2505.20556) 的直接 pessimistic 建模，共同说明 pessimism-based defense 已是拥挤方向。

2. **Significance: 中** —
   - 研究问题是重要的：PRM 在 LLM 推理管线中的 reward hacking 是实际痛点。
   - 但影响面受限于 PRM-guided mathematical reasoning 场景（MATH-500, AIME），向 general RLHF、code generation、或其他 domain 的推广性不明确。
   - 如果核心发现是 positive（calibration 确实 causally determines hackability），审稿人的反应更可能是 **"I would have guessed this"** 而非 "surprising"——直觉上，一个给出过度自信 wrong prediction 的 PRM 当然更容易被 exploit。
   - 如果发现是 negative（calibration 和 hackability 只有弱相关），反而更 surprising 且更有价值。

3. **Related Work: 强** —
   - Proposal 对相关工作的覆盖非常全面，准确识别了 3 个研究线程及其空白。
   - 引用的关键论文经搜索验证均真实存在且描述准确。
   - 与 Ackermann et al. 的技术差异化定位清晰（outcome-level vs. step-level，gradient norm vs. Hessian spectra）。
   - 与 Caution、ensemble methods、APRM 的比较也准确。
   - **不足**: 未引用 "Causal Reward Adjustment" (arXiv:2508.04216) 和 "Learning a Pessimistic Reward Model" (arXiv:2505.20556)，这两篇是直接竞争工作。

---

【概率估计】: 20% - 32%，中位 25%

（注：此为投稿至合适 venue 如 NeurIPS/ICML 的估计。投稿 CoRL 2026 的中稿概率为 ~0%，会被 desk reject。）

【估计理由】:
- Related Work 覆盖充分（强），proposal 形式上非常完善，实验设计详尽——这些保证了下限不会太低。
- 但 **Novelty 是限制上界的关键维度**：核心方法 CGSP 是 LCB 在 step-level PRM 的标准应用；"bridge two threads" 的贡献模式在 top venue 中 novelty 评分通常中偏低；pessimism-based defense 方向已拥挤。
- **Significance 的"I would have guessed this"风险** 进一步压低上界：核心假设（better calibration → harder to hack）直觉上几乎是显然的，positive result 不会 surprising。
- 概率区间 20-32% 对应 rubric 中的"idea 有实质内核但核心发现审稿人可能觉得 expected"区间的下半段，因为 trivial alternative 威胁（简单 temperature scaling + 固定 LCB）显著。

【主要风险】:
1. **"Obvious hypothesis" 风险**: "校准好的 PRM 更难被 hack" 这个核心 claim 直觉上太 natural，positive result 缺乏 surprise value；negative result 反而更有 paper value 但 proposal 并非围绕这个 framing 设计。
2. **Trivial alternative 威胁**: 简单的 temperature scaling + 固定 pessimism coefficient 可能达到 CGSP 的大部分效果，使 CGSP 的自适应机制（c_t gating, drift detector）看起来是不必要的工程复杂度而非方法论贡献。
```

---

**补充说明（会议选择）：**

本 proposal 的内容——PRM 校准、reward hacking 防御、LLM 数学推理——完全属于 NLP/ML 领域。CoRL 2026 明确声明 "Submissions without a robotics focus will be returned without review"。建议重新选择投稿目标：

- **NeurIPS 2026**（deadline 通常 5 月底）：最匹配，涵盖 RL、reward modeling、LLM alignment
- **ICML 2026**：如已错过 deadline
- **ICLR 2027**：如需更多实验时间
- **EMNLP 2026**：如侧重 NLP 应用面

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models](https://arxiv.org/html/2605.06785)
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking in RLHF](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/pdf/2604.04648)
- [Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction](https://arxiv.org/pdf/2508.04216)
- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/pdf/2505.20556)
- [Reward Hacking Defense Rubric - Emergent Mind](https://www.emergentmind.com/topics/reward-hacking-defense-rubric)


【原始 proposal（允许参考但不是主要依据）】:
# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense

## Description
We present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.

## Core Problem
PRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.

## Opportunity
Three recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.

## Related Work / Landscape
Two parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.

## Approach
The study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.

**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.

**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.

**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.

**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.

Baseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).

Codebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.

## Inspiration
Field guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone

## Key References
- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)
- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)
- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)
- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)
- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)
- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)
- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)
- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)
- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)
- Uncertainty-Aware Reward Model (arXiv:2410.00847)
- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)
- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)
- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)
- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)

## Resource Estimate
- **manual**: {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}
- **human_in_loop**: {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}
- **auto_research**: {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "aeed22b5-ec9d-4907-8015-ee60e2568f7a",
  "type": "user",
  "uuid": "2873545b-b07d-4983-ad1b-6b62af6195b5",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:58:46.787Z_

```json
{
  "parentUuid": "2873545b-b07d-4983-ad1b-6b62af6195b5",
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
  "uuid": "df6b6357-2fe7-4461-aeb5-26426d5c64f2",
  "timestamp": "2026-05-19T18:58:46.787Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:58:46.787Z_

```json
{
  "parentUuid": "df6b6357-2fe7-4461-aeb5-26426d5c64f2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e9c9baae-c65b-4c75-b1cd-33a168c3eb3b",
  "timestamp": "2026-05-19T18:58:46.787Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

````json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ 现在我有了足够的调研信息来进行评估。让我整理分析。  ---  ``` 【阶段】: Triage ```  ## ⚠️ 致命…",
  "leafUuid": "e9c9baae-c65b-4c75-b1cd-33a168c3eb3b",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c"
}
````

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking defense proposal",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:59:44.032Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewer evaluations and synthesize them as Meta Judge.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Novelty: 中 (偏弱)
- Significance: 中
- Related Work: 强 (偏中)
- Probability: [20% - 32%] 中位 25%

**Reviewer 2:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 弱
- Probability: [18% - 28%] 中位 22%


**Reviewer 3:**
- Novelty: 中偏弱
- Significance: 中
- Related Work: 强
- Probability: [20% - 32%] 中位 25%

The three acceptance probabilities cluster tightly around 24% mean with a median of 25%, showing remarkable consistency despite some variation in individual criteria. All three reviewers independently identified the CoRL venue mismatch as a desk-reject issue, though they evaluated the work assuming submission to a more appropriate venue like NeurIPS or ICML. Now I'm looking at where the reviewers align and where they diverge on the substantive issues.

The consensus is striking: all three flag weak-to-medium novelty, the unsurprising nature of positive results, temperature scaling as a simpler alternative, and CGSP as a standard LCB variant without algorithmic innovation. They're also unanimous on medium significance and the critical omission of CRA from related work. Two reviewers caught the PURM paper gap, and there's a shared concern about the post-hoc calibration gradient landscape analysis.

Where they diverge is revealing: R2 is substantially more critical on related work quality, identifying four missing papers (PURE, PURM, BNRM, CRA) while R1 and R3 are more lenient despite flagging some gaps. R2 uniquely emphasizes PURE as a major trivial alternative threat that the other reviewers don't mention. The BNRM paper appears to be another point of divergence, though R3's assessment seems incomplete here.

Looking at the consistency metrics, the three estimates cluster tightly around 22-25% with a standard deviation under 2%, which signals genuine agreement on the core assessment. The median sits at 25%, and this convergence suggests high confidence in that range. All three reviewers align on medium-weak novelty and medium significance, with the core idea quality capping the probability around 30-35% even under ideal conditions. The trivial alternative threats, the "obvious hypothesis" concern, and the missing related work all conspire to push the estimate lower.

For my final probability, I'll center on 23-24% given this high consistency, with a narrower interval reflecting the strong agreement. R2's stricter Related Work rating and the additional papers they flagged (PURE, BNRM, EDU-PRM) versus what R1 and R3 found (CRA, PURM) suggest the coverage gaps are real but not catastrophic—the proposal does address the main research threads even if incompletely. I need to verify whether PURE is actually as critical as R2 suggests. The PURE paper citation with its specific arXiv ID gives it credibility even though only R2 mentions it, so I should acknowledge it as an anomaly point but weight it accordingly. Now I'm compiling the synthesis across all three reviewers — the midpoint estimates cluster tightly around 22-25% with minimal variance, and there's strong consensus on the core weaknesses: modest novelty, medium significance, the "I would have guessed this" concern, temperature scaling as a simpler alternative, and CGSP being essentially an LCB variant. mismatch fatal (3/3) — strong signal
- CRA omission (3/3) — strong signal
- Causal confound in post-hoc calibration (3/3) — strong signal

**Anomaly dimensions:**
- Related Work rating: R2 rates 弱 vs R1/R3 rate 强 — significant divergence on this dimension specifically
- PURE as trivial alternative: only R2 — could be important if valid but should be noted as unverified by other reviewers
- BNRM, EDU-PRM: only R2

Given high consistency (std ~1.4%), I should narrow the interval and take the median. R2's stricter assessment of Related Work appears substantive—all reviewers found omissions, suggesting the true rating sits between weak and strong rather than at either extreme. The venue mismatch independently disqualifies this for CoRL.

Final estimate: [22% - 25%] with median at 25% I'm settling on [20% - 28%] with a median of 24%, slightly below the strict midpoint since R2's findings about missing work like PURE are substantive and align with the pattern of different papers being identified across all three reviews. Now I need to properly flag the venue mismatch as a critical consensus issue and then pull together the implementation assessment using the proposal's resource estimates and reviewer feedback to write up the final output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9c9baae-c65b-4c75-b1cd-33a168c3eb3b",
  "isSidechain": false,
  "requestId": "req_011CbCSXBQrCyE6vgkE8bj4z",
  "type": "assistant",
  "uuid": "d8fe63b7-1a05-4070-a8ad-716e9aa2b233",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTFUUMCy7UjUkn88i3myqv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20096,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4634,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20096,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4634,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 20096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20096
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

_source line 9 · 2026-05-19T19:00:33.123Z_

【阶段】: Meta Judge
【三次中位】: [25%, 22%, 25%]  std=1.4%
【共识维度】:
- **Venue Mismatch = 致命** (3/3)：CoRL 2026 明确要求 robotics focus，本 proposal 与机器人零关联，投 CoRL 必然 desk reject。三位审稿人一致判定。
- **Novelty = 中偏弱** (3/3)：核心方法 CGSP 是 LCB 在 step-level PRM 的标准应用；"bridge two threads" 的贡献模式 novelty 上限有限；pessimism-based defense 已是拥挤方向。
- **Significance = 中** (3/3)：研究问题重要（PRM reward hacking 是实际痛点），但影响面受限于数学推理场景，且 positive result 缺乏 surprise value。
- **"I would have guessed this" 风险 = 致命级** (3/3)：三位审稿人一致认为"better calibrated PRMs are harder to hack"直觉上近乎显然，positive result 不会 surprising——这是 idea 层面最大的天花板制约。
- **Trivial Alternative: Temperature Scaling = 强威胁** (3/3)：单参数 post-hoc 校准可能解释大部分效果，使 CGSP 全套自适应机制的增量价值存疑。
- **CRA (arXiv:2508.04216) 遗漏** (3/3)：因果视角下的 PRM reward hacking 防御，直接威胁 "first causal study" 声明。
- **Post-hoc Calibration 梯度 Landscape 混淆因果** (3/3)：temperature scaling 改变梯度大小/曲率，因果隔离实验可能测到的是"梯度缩放效应"而非"校准的因果效应"。
- **PURM (arXiv:2503.22480) 遗漏** (2/3, R1+R2)：不确定性感知悲观 reward 建模，概念上与 CGSP 高度重叠。
- **Pessimistic RM (arXiv:2505.20556) 遗漏** (2/3, R1+R3)：悲观 reward 建模理论工作，与 CGSP 方向相似。
【异常维度】:
- **Related Work 评分严重分歧**：R1 评"强偏中"、R3 评"强"、R2 评"弱"。分歧根源在于 R2 额外发现了 PURE (arXiv:2504.15275)、BNRM (arXiv:2602.10623)、EDU-PRM (arXiv:2503.22233) 等遗漏。R1/R3 也各自发现了 2-3 篇遗漏但对整体评价更宽容。综合判断：proposal 对两条主线的覆盖确实全面，但在 **交叉领域（uncertainty-aware defense）的覆盖存在系统性盲区**，真实评分应为"中"——有基本面但有实质性遗漏。
- **PURE (arXiv:2504.15275) 作为 trivial alternative**：仅 R2 提出，声称 PURE 通过 min-form credit assignment 从更根本层面解决 PRM reward hacking，且无需校准步骤。若属实，这比 temperature scaling 更具威胁性。但仅 1 位审稿人提及，降权处理——标注为"需人工验证的潜在风险"。
- **BNRM (arXiv:2602.10623)**：仅 R2 提及。贝叶斯不确定性感知 reward 学习，属补充性 related work 而非致命威胁，降权。
【最终概率】: [20% - 28%] 中位 24%
【一致性】: 高（std=1.4%，三位审稿人在核心判断上高度一致）
【综合理由】:

1. **概率锚定**：三位审稿人中位分别为 25%、22%、25%，std 仅 1.4%，属高一致性。按规则取中位附近（25%）并缩窄区间。最终中位微调至 24%，原因见下。

2. **共识驱动的信心**：7 个核心维度有 3/3 共识，这在独立评审中极为罕见，表明这些判断的可靠性很高。特别是"I would have guessed this"风险和"CGSP = 标准 LCB"两个判断，直接限定了 idea 的 novelty 天花板——即使实验完美执行，核心发现的 surprise value 不足以支撑 30%+ 的概率。

3. **异常处理**：Related Work 评分的分歧实质上不影响概率估计——即使 R2 发现的额外遗漏全部成立，这些可以在修改中补上（related work 是"可补"维度），而 novelty 和 significance 的天花板（"不可补"维度）是概率的真正约束。PURE 的 trivial alternative 威胁因仅 1 人提及而降权，但若经验证确实如 R2 所述，可能将上界进一步压低至 25%。

4. **中位微调至 24% 的理由**：严格中位是 25%，但 R2 发现的 PURE 和 BNRM 等遗漏即使降权也提供了额外的下行压力，加上"宁缺毋滥"原则，将中位从 25% 微调至 24%。

5. **Venue Mismatch 独立致命**：以上所有概率估计基于投稿合适 venue（NeurIPS/ICML/ICLR）。**投稿 CoRL 2026 的中稿概率为 0%，三位审稿人一致确认会被 desk reject。**

【建议】: 不推荐（投 CoRL 为 KILL；转投合适 venue 后为边缘偏下，idea 天花板受限）
【实施评估】:
  - 计算资源: 约 3600-5200 H100-GPU-hours（取决于自动化程度），涵盖校准拟合(200h)、rollout 生成(600h)、梯度攻击(1000h)、GRPO RL 训练(1600h)、BoN 评估(400h)、Hessian 分析(200h)、因果隔离控制(200h)。预估 GPU 成本 $9,000-$13,000。需 4×H100 节点用于 72B PRM 推理。
  - 数据需求: MATH-500 和 AIME 数据集（公开可得）；8 个开源 PRM（均公开）。无新数据收集需求。
  - 人工介入: 中等——48 配置实验的超参数调优、因果隔离实验的 CKA 验证、Hessian 分析的解读需要研究者深度参与。无大规模人工标注需求。
  - 训练需求: 需要训练/微调——Tier 2 校准方法（quantile regression、COT）需要微调 PRM；GRPO RL 训练是核心实验；matched representation change 控制实验需要辅助任务微调。单次 GRPO 配置约 18 小时（4×H100）。
  - 新 Benchmark: 不需要构建新 benchmark，使用现有 MATH-500/AIME 和 Tiwari et al. 的 PRM-BiasBench。
  - 预估周期: 10-14 周（从启动到可投稿），主要瓶颈为 GRPO RL 训练的 wall-clock 时间和 48 配置的串行/并行调度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8fe63b7-1a05-4070-a8ad-716e9aa2b233",
  "isSidechain": false,
  "requestId": "req_011CbCSXBQrCyE6vgkE8bj4z",
  "type": "assistant",
  "uuid": "927a8cab-019b-4398-bc71-a856cf2db904",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTFUUMCy7UjUkn88i3myqv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20096,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4634,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20096,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4634,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 20096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20096
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

````json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ 现在我有了足够的调研信息来进行评估。让我整理分析。  ---  ``` 【阶段】: Triage ```  ## ⚠️ 致命…",
  "leafUuid": "927a8cab-019b-4398-bc71-a856cf2db904",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c"
}
````

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking defense proposal",
  "sessionId": "42983d27-0cbd-4b46-805e-ef687e8fcc4c"
}
```

---
