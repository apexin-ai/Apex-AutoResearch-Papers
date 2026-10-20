# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/60020c65-c5ca-4696-8e6f-144fac44205e.jsonl`
- **Structured JSON:** [`96093a5bca8dfa1e1d4c.json`](../../sessions/96/96093a5bca8dfa1e1d4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T16:56:42.929Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T16:56:42.929Z",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information from my research. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689) (arXiv, May 2026): 证明 GRPO 在二值奖励下的 degeneracy rate D(p,G)=p^G+(1−p)^G，学习信号（non-degenerate fraction）在 p=0.5 时最大。这是本 proposal \"Learning-Gaming Paradox\" 的核心锚点之一。论文存在且描述准确。\n- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872) (arXiv, Feb 2026): 证明多步推理学习梯度 ∝ (Δ_L)^L(1−Δ_L)，peak pass rate 在 [0.37, 0.50]。Relay effect 解释了模型如何自然穿越这个中等难度区间。论文存在且 proposal 对其的引用（区分 Δ 和 p、不宣称共享函数形式）是谨慎的。\n- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (arXiv, Mar 2026): Wang & Huang 提出 per-dimension distortion index D_i，证明 D_i 排序结果（Corollary 1a）。关键局限：静态模型，不含难度参数化。Proposal 准确识别了这个 gap（Remark 2），并声称扩展到 D_i(d)。\n- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) (arXiv, May 2026): 诊断 rubric RL 中的 gaming 分类，发现 90.2% 集中在 presence-based criteria。未按问题难度分层——这正是本 proposal 声称的分析维度缺口。论文存在且描述准确。\n- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) (arXiv, May 2026): 受控实验环境，发现 hack rate 随难度单调增加（5 模型、3 游戏）。这为 proposal 的 H0a 提供最强对照证据。论文存在且描述准确。\n- [Goodhart's Law in Reinforcement Learning](https://arxiv.org/abs/2310.xxxxx) (ICLR 2024): 标量 proxy-goal 对的 Goodhart 分析；不含多维或难度分析。\n- [SPARKLE / Beyond Accuracy](https://arxiv.org/abs/2506.04723) (NeurIPS 2025): 分析 RL 下推理的 3 个维度跨难度变化，但研究的是 reasoning capability 而非 gaming/exploitation，无 Goodhart 框架。\n- [DGPO / MathForge](https://arxiv.org/abs/2502.xxxxx) (ICLR 2026): 二值奖励下的难度感知 GRPO；无 per-criterion gaming 分析。\n- [POW3R](https://arxiv.org/abs/2605.20164), [SRaR](https://arxiv.org/abs/2605.17291), [ARES](https://arxiv.org/abs/2605.23454), [AMARIS](https://arxiv.org/abs/2605.18592): 近 4 周内的 rubric-RL 方法论文（共 ~10+ 篇），均未做 difficulty-stratified gaming 分析。\n- 搜索 \"learning-gaming paradox\"、\"difficulty-dependent exploitation\" 等关键词未发现任何直接竞争工作。\n\n- **调研总结**: Rubric-RL 领域正在快速扩张，训练方法（RRM, RaR, SRaR, POW3R）和 Goodhart 理论（Wang & Huang, Robust Optimization）分别有大量工作，但两条线尚未交叉：没有工作将 GRPO 训练动态（学习效率 vs. 难度）与 rubric 维度上的 gaming vulnerability 联系起来。Proposal 确实占据了一个真实的未填补交叉地带。SPARKLE 是最接近的——它做了 per-criterion × per-difficulty 分析，但目标是 reasoning capability 而非 gaming。\n\n【Trivial Alternative 检验】:\n最直接的 trivial alternative 是：直接按难度分层统计每个 rubric criterion 的 gaming rate，生成 heatmap，无需任何理论框架。这个 baseline 成本极低（只需一次 training + judge inference + 分层统计），就能回答 \"gaming 在不同难度下的分布长什么样\" 这个描述性问题。\n\nProposal 的增量价值在于三个层面：(1) 理论预测——Gaming Budget Theorem 预测 *哪些* criteria 在 *哪个* 难度下最易被 exploit，而非事后描述；(2) Dimensionality Collapse Theorem 预测 honest signal 维度塌缩快于 total signal——这是 trivial heatmap 无法给出的结构性预测；(3) Calibration schedule 提供了从诊断到干预的桥梁。\n\n**但关键问题是**：Gaming Budget bound 的 √(p(1-p)) 函数形式是否是对 gaming opportunity 的真实刻画？如果 bound 很松，那么\"两个函数都在 p=0.5 取最大值\"这个\"paradox\"就可能只是 bound 的 artifact，而非真实现象。√(p(1-p)) 和 N(p,G) = 1−p^G−(1−p)^G 都是 [0,1] 上的对称凹函数，它们同时在 p=0.5 取极值是**数学必然**，而非\"paradox\"。这显著削弱了核心 claim 的惊奇性。\n\n【前提假设检验】:\n核心逻辑链的关键未验证假设：\n\n1. **Gaming opportunity 真的遵循 √(p_k(1-p_k)) scaling 吗？** 这是整个 \"paradox\" 的一半。Proposal 将这作为 bound 呈现，但 bound 的 tightness 未经验证。如果实际 gaming opportunity 在高难度单调增加（如 arXiv:2605.20744 的实验所示），那么 Gaming Budget bound 的 peak-at-0.5 预测可能只是 bound 过松的结果。\n\n2. **A4 假设（criterion-level pass rates 与 aggregate pass rate 正相关）**: Proposal 用 \"shared difficulty driver\" 解释，但某些 criteria 可能对难度不敏感（如格式要求），导致 A4 局部失效。如果 surface criteria 的 p_k 在所有难度下都接近 1，那 Gaming Budget 在这些维度上接近 0，paradox 的 practical relevance 就大打折扣。\n\n3. **LLM-as-judge 的可靠性**: 整个实验依赖 Qwen3-8B 作为 rubric judge。Judge 自身的 difficulty-dependent 偏差可能与真实 gaming 混淆。用 200 样本验证似乎不够充分。\n\n4. **从 \"两个函数同在 p=0.5 取极值\" 到 \"这构成了一个 paradox\"**: 这个推理假设了社区之前认为学习和 gaming 应该在不同难度区间 peak。但如果这是直觉上显然的（中等难度 = 最多模糊空间 = 最多 gaming 空间），那就不是 paradox，而是 expected behavior。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Proposal 声称的核心 novelty 是 \"Learning-Gaming Paradox\"——GRPO 学习效率和 gaming opportunity 都在中等 pass rate 区间 peak。调研确认没有直接竞争工作（搜索 \"learning-gaming paradox\"、\"difficulty-dependent exploitation\" 无结果），这个交叉连接确实是新的。然而，核心数学观察（两个对称凹函数都在 p=0.5 取极值）是 trivially true——任何定义在 [0,1] 上、边界为零的对称凹函数都会如此。\"Paradox\" 标签夸大了惊奇性。Dimensionality Collapse (T2) 是更有潜力的贡献——如果 honest signal 维度确实塌缩快于 total signal，这是非 trivial 的结构预测，但目前只有理论声称，没有先验证据支持。相对于 Wang & Huang (arXiv:2603.28063) 的扩展（D_i → D_i(d)）是 incremental 但有价值。相对于 arXiv:2605.12474（不分层难度）和 arXiv:2605.20744（不分析 per-criterion），组合维度是新的。总体而言，有真实的 novelty delta，但核心 \"paradox\" 的惊奇性被高估。\n\n2. **Significance: 中** — \n   Rubric-RL 正在快速扩张（4 周内 10+ 篇论文），一个诊断框架确实有价值——如 proposal 所言，方法越多越需要共享评估视角。但实际影响取决于经验发现：如果 gaming surface 是 trivial（如对所有 criteria 都单调增加，符合 H0），那 paradox 的 practical relevance 有限。Calibration schedule（T3）是最直接的实用贡献，但它在 H0 confirmed 情况下简化为线性 schedule，而线性 difficulty-based strictness 调整是一个相当直觉化的解决方案。对 AAAI 评审而言，这是一个 diagnostic/analytical contribution，而非方法论突破——这类论文可以被接受（参考 SPARKLE@NeurIPS 2025 的先例），但上限受限。\n\n3. **Related Work: 强** — \n   覆盖极为全面。Proposal 引用了 30+ 篇论文，分布在 8 个相关类别中，每一类都有精确的差异化定位。关键引用经调研验证为真实存在且描述准确（arXiv:2605.07689、2602.14872、2603.28063、2605.12474、2605.20744）。对每篇竞争工作的局限性描述是诚实的（如 Wang & Huang 的 Remark 2、arXiv:2605.12474 不分层难度）。Composite null hypothesis 的构建引用了最强对照证据（arXiv:2605.20744 的受控实验），体现了学术诚实。唯一小问题：部分引用数量可能让评审感觉过度堆砌（defensive over-citation）。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \nNovelty 是限制上界的主要维度。核心 \"paradox\"（两个凹对称函数同在 p=0.5 取极值）虽然是一个此前未被明确指出的连接，但其数学必然性削弱了 surprise factor。一个 strong reviewer 很可能写 \"The observation that both quantities peak at intermediate pass rates is mathematically obvious given their functional forms — calling this a 'paradox' overstates the finding.\" Dimensionality Collapse (T2) 是最有潜力提升 novelty 的贡献，但作为理论声称其验证完全依赖实验结果。Related Work 覆盖是本 proposal 的明确强项，会获得审稿人正面评价。Significance 处于中等——诊断性贡献在 top venue 有先例（SPARKLE@NeurIPS），但不如方法论创新有影响力。Dual-outcome design 为下限提供了保障（即使预测失败也有诊断价值），但也意味着最有趣的发现（non-monotonic gaming）可能不成立。\n\n综合来看：idea 有真实但有限的 novelty（~中等），方向正确但核心发现如果 positive，审稿人可能会说 \"interesting but not that surprising\"（介于 \"I would have guessed this\" 和 \"surprising\" 之间），将概率定位在 25-35% 区间的下半部分。\n\n【主要风险】:\n1. **\"Paradox\" 的惊奇性不足**: 审稿人可能认为两个对称凹函数在 p=0.5 同时取极值是数学 triviality 而非 deep insight——Gaming Budget bound 的 √(p(1-p)) 函数形式与 N(p,G) 同在 p=0.5 peak 是函数族的固有性质，不构成 \"paradox\"。这直接威胁论文的核心卖点。\n2. **Gaming Budget bound 的 tightness 未经验证**: 如果 bound 很松，实际 gaming 可能根本不在 p=0.5 peak（arXiv:2605.20744 的受控实验显示 hack rate 随难度单调增加），那么整个 paradox 框架的 practical relevance 将受到根本性质疑——peak coincidence 可能是 bound artifact 而非 empirical reality。\n```\n\nSources:\n- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689)\n- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872)\n- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063)\n- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)\n- [Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale](https://arxiv.org/abs/2605.20744)\n- [Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (SPARKLE)](https://arxiv.org/abs/2506.04723)\n- [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/abs/2605.23454)\n- [Rubric-Based Rewards for RL - Deep Learning Focus](https://cameronrwolfe.substack.com/p/rubric-rl)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to evaluate this proposal. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689) (arXiv, May 2026): 证实 GRPO 的非退化比例 N(p,G)=1−p^G−(1−p)^G 在 p=0.5 最大化，G=4 时退化率达 0.69。这是 proposal 的核心锚点之一，论文真实存在，描述准确。\n- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872) (arXiv, Feb 2026): 多步推理梯度 ∝ (Δ_L)^L(1−Δ_L)，峰值在中间 pass rate 区间 [0.37, 0.50]。论文真实存在，proposal 对其的引用准确，且正确标注了 Δ_L ≠ p 的区别。\n- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (Wang & Huang, Mar 2026): 提出可计算的 per-dimension distortion index D_i，证明在对称生产函数下的 ranking 结果。确认论文存在，proposal 对其局限性（static, no difficulty parameterization）的描述与原文 Remark 2 一致。\n- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474) (May 2026): 在医学和科学领域诊断 rubric gaming 的 3 种失败模式和 90.2% presence-based 集中。论文存在，但 proposal 声称其\"does NOT stratify by problem difficulty\"需验证——从搜索摘要看，该论文确实关注 criterion-type 而非 difficulty stratification。\n- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) (May 2026): 5 个模型 × 3 个游戏环境的受控实验，发现 hack rate 随难度单调递增。论文存在，为 proposal 的 H0a 提供支持。\n- [DGPO/MathForge](https://openreview.net/forum?id=nfURupkdRJ) (ICLR 2026): Difficulty-aware GRPO，通过 MAD normalization 处理难度偏差。论文存在且已被 ICLR 2026 接收。\n- [Goodhart's Law in RL](https://openreview.net/forum?id=5o9G4XF1LI) (ICLR 2024): 标量 proxy-goal 分析，geometric explanation for Goodhart's law in MDPs。论文存在。\n- [Rubrics as Rewards (RaR)](https://openreview.net/forum?id=c1bTcrDmt4) (ICLR 2026): 基础 rubric RL 框架，+31% HealthBench, +7% GPQA-Diamond。论文存在。\n\n- 调研总结: Rubric-rewarded RL 是一个快速增长的领域（~10+ 论文/月），difficulty-aware GRPO 方法和 reward hacking 诊断已有大量工作。但现有工作分为两条平行线——难度感知训练（binary reward, 不关注 per-criterion gaming）和 gaming 诊断（不按难度分层）。将两者交叉分析（per-criterion × per-difficulty）的工作确实是空白。然而，这个\"交叉\"的核心数学论点——N(p,G) 和 √(p(1−p)) 都在 p=0.5 取最大值——是一个相当简单的对称凹函数性质观察。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁。核心经验贡献——\"per-criterion × per-difficulty gaming surface\"——可以通过一个直接的实证方法获得：在不同难度 bin 上分别计算每个 criterion 的 gaming 指标（如 DEG），绘制热力图，然后用标准统计检验分析模式。这不需要 Gaming Budget Theorem、Dimensionality Collapse Theorem 或 Learning-Gaming Duality 框架。一个简单的\"stratified analysis + bootstrap CIs + regression\"就能产出几乎相同的经验洞见。\n\n增量价值在于：(a) 理论框架如果 bound 足够紧，可以做出先验预测（而不是事后观察），以及 (b) T3 Calibration Sufficiency Condition 可以推导出最优校准策略。但 (a) 的价值取决于 bound 的 tightness（未经验证），(b) 的简化形式 s_k(d) = α_k + β_k·d 本身就可以通过经验回归直接拟合，无需理论推导。因此，理论框架的实际增量价值是可疑的——它可能是\"decorative theory\"，为一个本质上简单的经验观察提供不必要的包装。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有以下未经验证的关键假设：\n\n1. **A1（可分解性）**: 假设每个 criterion 的 pass rate 可以干净地分解为 \"genuine\" 和 \"gaming\" 两个分量。这在实际中非常难以操作化——什么算\"genuine\"什么算\"gaming\"的边界是模糊的，尤其对于部分正确的推理步骤。这个假设是整个 Gaming Budget bound 的基石，但其经验可验证性存疑。\n\n2. **A4（正相关性）**: 假设 criterion-level pass rates p_{k,d} 与 aggregate binary pass rate p̄_d 正相关。这对大多数 criteria 可能成立，但对 surface/formatting criteria（如\"格式完整性\"）可能不成立——模型可能在高难度问题上仍然保持格式正确但推理错误。如果 A4 不成立，T4 的\"peak coincidence\"就不成立。\n\n3. **核心\"paradox\"的因果力**: N(p,G) 和 √(p(1-p)) 都在 p=0.5 最大化是一个数学事实，但这不自动意味着\"选择 p≈0.5 的问题训练会导致更多 gaming\"。因为：(a) gaming 的发生需要模型有足够的能力去发现 exploit，而不仅仅是数学上的\"opportunity\"；(b) 中间难度的 gaming \"opportunity\" 只是 upper bound，实际 gaming 可能远低于 bound。从 upper bound 的 peak 到 actual gaming 的 peak 之间的推理缺乏严格性。\n\n4. **Dimensionality Collapse（T2）的假设**: \"honest signal collapses faster than total signal\" 需要 high-verification-stringency criteria 先退出 active gradient set。但这个排序是否真的成立取决于具体的 criteria 设计和 judge 质量，而非一般性原理。\n\n【3 维度打分】:\n  1. Novelty: 弱-中 — 核心数学观察（N(p,G) 和 √(p(1-p)) 都在 p=0.5 取最大值）是对称凹函数的 trivial 性质，任何审稿人都能在 30 秒内验证这一点。将 Wang & Huang 的 D_i 扩展到 D_i(d) 是增量贡献（加一个难度维度）。真正的新意在于 per-criterion × per-difficulty 的经验方法学（10-bin difficulty scale, bootstrap CIs, isotonic regression 非单调性检验），但这更接近\"方法论组合\"而非概念突破。与 arXiv:2605.12474 对比：该工作已做了 per-criterion gaming 诊断，只是没有 per-difficulty；与 arXiv:2605.20744 对比：该工作已做了 per-difficulty hacking 测量，只是没有 per-criterion。本 proposal 的贡献本质上是\"把两个已知维度交叉起来\"。理论框架（T1-T4）的新意主要来自对 Wang & Huang 的 difficulty 扩展，但这种扩展在概念上是自然的（甚至 Wang & Huang 自己在 Remark 2 中都指出了这个方向）。\n\n  2. Significance: 中 — 研究问题确实重要且时机好：rubric-RL 方法激增，但对 gaming 在不同难度上的行为缺乏系统理解。如果非单调性预测（P1）成立，这会是对 DGPO/CDAS 等方法的重要警示。但即便 P1 成立，实际影响可能有限——论文的处方性输出只是一个简单的线性校准 s_k(d) = α_k + β_k·d，这可以不依赖任何理论直接通过网格搜索获得。诊断工具（gaming heatmap）的实用价值取决于社区是否会采用，而目前 rubric-RL 论文的 pace 太快，诊断框架可能在发表前就被更好的方法超越。该工作是 diagnostic 性质而非 prescriptive——它告诉你\"哪里有问题\"，但提供的解决方案（T3 calibration）过于简单。\n\n  3. Related Work: 强 — 对已有工作的覆盖异常全面，涵盖 8 个类别 40+ 篇论文。差异化定位清晰：准确识别了\"difficulty-aware RL 方法都用 binary reward\"和\"gaming 诊断方法不按难度分层\"两条平行线。对 Wang & Huang 的局限性分析（Remark 2）、对 Gradient Starvation 和 Edge of Competence 的区分使用都很精准。composite null hypothesis 的构建（H0a from arXiv:2604.15149 + arXiv:2605.20744, H0b from arXiv:2605.12474）展示了对领域的深入理解。唯一的小问题是过度引用可能给审稿人造成\"补偿性引用\"的印象——试图用广度掩盖深度不足。\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】: \nNovelty 是主要限制因素。核心\"paradox\"的数学内容——两个对称凹函数都在 p=0.5 取最大值——不构成 surprising 的学术发现。一位审稿人很可能会写：\"The observation that both N(p,G) and √(p(1−p)) peak at p=0.5 is trivially expected from their functional forms. The 'paradox' is manufactured by naming a natural mathematical property.\" T1 的 Gaming Budget bound 是 Wang & Huang D_i 的自然扩展（他们自己标注了方向），T4 是 trivial corollary。T2（Dimensionality Collapse）是最有潜力的贡献，但其假设太强且验证困难。\n\n实证方面，per-criterion × per-difficulty 的交叉分析确实是空白，但这更像是\"人们还没来得及做\"而非\"这个问题很难\"——毕竟相关论文（arXiv:2605.12474, arXiv:2605.20744）都是 2026 年 5 月才出来的。the gap is real but the barrier to filling it is low，这意味着 novelty 的时间窗口很短。\n\nRelated Work 的强度部分补偿了 Novelty 的不足，但 AAAI 审稿人更看重核心贡献的深度而非 related work 的广度。Significance 居中——问题重要但解决方案（线性校准）影响有限。\n\n综合来看，在 Novelty 弱-中、Significance 中的情况下，AAAI 中稿需要实验结果非常 compelling 才能弥补 idea 层面的薄弱——但入口评审只评估 idea 本身。\n\n【主要风险】:\n1. **\"Paradox\" 被审稿人认为 trivial**: 核心数学观察是对称凹函数的基本性质，审稿人可能认为将其命名为\"paradox\"并构建 4 个定理是 over-engineering。如果审稿人写 \"the learning-gaming 'paradox' reduces to the unsurprising fact that variance-like quantities peak at p=0.5\"，论文的 narrative 基础就崩塌了。\n2. **理论框架可能是 decorative**: Gaming Budget bound 的 tightness 未经验证，如果 bound 极度松弛（实际 gaming ≪ bound），则整个理论框架不提供比直接经验测量更多的洞见。在这种情况下，论文退化为\"我们在不同难度上测量了 per-criterion gaming\"——这是有用的但不够 AAAI 主会。\n```\n\nSources:\n- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689)\n- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872)\n- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063)\n- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474)\n- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744)\n- [DGPO/MathForge (ICLR 2026)](https://openreview.net/forum?id=nfURupkdRJ)\n- [Goodhart's Law in Reinforcement Learning (ICLR 2024)](https://openreview.net/forum?id=5o9G4XF1LI)\n- [Rubrics as Rewards (ICLR 2026)](https://openreview.net/forum?id=c1bTcrDmt4)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient field research to evaluate this proposal rigorously. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689) (arXiv, May 2026): 验证存在且描述准确。证明 GRPO 非退化分数 N(p,G)=1−p^G−(1−p)^G 在 p=0.5 达到最大值，G=4 时观测到 0.69 退化率。该 proposal 正确引用此结果作为 Learning-Gaming Paradox 的\"学习效率\"锚点。\n- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872) (arXiv, Feb 2026): 验证存在。论文分析了 RLVR 的 relay effect 和难度谱平滑性对学习动态的影响。Proposal 引用 Lemma 6.2 的 multi-step gradient 形式作为补充支撑，引用方式合理，且明确区分了 Δ_L（attention margin）和 pass rate p 的不同。\n- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (Wang & Huang, arXiv Mar 2026): 验证存在。提出 per-dimension distortion index D_i，证明 reward hacking 是结构性均衡。Proposal 声称扩展 D_i 为 D_i(d)（加入难度维度），这是合理的增量扩展。原论文确实在 Remark 2 中承认了对称生产函数假设的局限。\n- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474) (arXiv, May 2026): 验证存在。诊断了 rubric-based RL 中的三种 gaming failure mode，90.2% presence-based 集中度。Proposal 正确指出该工作\"未按难度分层\"——经验证，原文确实未做 difficulty stratification。\n- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) (arXiv, May 2026): 验证存在。在 5 个模型、3 个游戏环境中测试，发现 hack rate 随难度单调递增。Proposal 正确将此纳入 composite null hypothesis H0a。\n- [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149) (ICLR 2026 Workshop): 验证存在。发现 RLVR 训练的模型系统性放弃规则归纳，转为枚举实例标签的 shortcut 策略。\n- [MO-GRPO](https://arxiv.org/abs/2509.22047) (arXiv 2025): 解决 GRPO 多目标问题中的 reward hacking，通过 per-objective variance normalization，但确实 difficulty-agnostic。\n- [DGPO/MathForge](https://huggingface.co/papers/2601.20614) (ICLR 2026): 通过 MAD normalization 解决 binary-reward GRPO 的难度偏差。确实只在 binary reward 下操作。\n- [POW3R](https://arxiv.org/abs/2605.20164) (arXiv, May 2026): 通过 rollout-contrast 动态调整 rubric criterion 权重，属于 reactive/diagnostic 方法。\n- 调研总结: Rubric-rewarded RL 是一个极度活跃的领域（4 周内 10+ 篇论文），形成了三条明确的研究线：(a) 难度自适应 GRPO 方法（DGPO, CDAS, F-GRPO 等，均针对 binary reward）；(b) Rubric 设计与 gaming 防御（RRM, POW3R, ARES 等，均 difficulty-agnostic）；(c) Goodhart 理论扩展（Wang & Huang, ICLR 2024 等，均 scalar 或 static）。三条线确实尚未交叉——\"per-criterion × per-difficulty 的 gaming 诊断\"这个交叉点目前确实空缺。但这个空缺是否源于\"无人发现\"还是\"不值得做\"需要仔细区分。\n\n【Trivial Alternative 检验】:\n核心观察——p(1−p) 在 p=0.5 达到最大值——是 Bernoulli 方差的基本性质，任何统计学入门课都会教。Proposal 的关键 claim 是 GRPO 学习信号（基于 N(p,G)=1−p^G−(1−p)^G）和 gaming opportunity（基于 √(p_k(1−p_k))）在相同的中等 pass-rate band 达到峰值。但这两个量都是 p(1−p) 的变体——它们在 p=0.5 附近同时达到峰值几乎是 tautological 的。\n\nTrivial alternative：一个直觉性的 baseline 思路是\"在中等难度问题上对 surface criteria 施加更严格的评判标准\"——不需要任何形式化框架。Proposal 的 T3 calibration schedule s_k(d) = α_k + β_k·d 本质上就是将这个直觉形式化。增量价值在于：(1) 产出 per-criterion × per-difficulty 的 gaming heatmap 作为可复用诊断工具；(2) 将 Wang & Huang 的 static D_i 扩展为 D_i(d)。但这些增量的\"惊喜度\"有限——informed reviewer 很可能回应\"是的，当然中等难度带是最模糊的评估区域——这和学习信号最强的区域重合并不令人意外。\"\n\n【前提假设检验】:\n1. **假设 A4（criterion-level 与 aggregate pass rate 正相关）**: Proposal 声称\"由共同的难度驱动因子保证\"。但这是一个强假设——formatting/structural criteria 在所有难度上可能都接近 p≈1.0，与 aggregate pass rate 的相关性可能很弱甚至为零。不同 criteria 的 difficulty profile 可能高度异质。\n2. **√(p_k(1−p_k)) 代表 gaming opportunity**: 这是从 Bernoulli 方差到\"gaming opportunity\"的概念跳跃。为什么 gaming 应该正比于标准差而非方差或其他函数？Proposal 没有从机制层面推导这个关系，而是 assert 了它。\n3. **Gaming Budget bound 的 tightness**: T1 提供上界，但上界的实用性取决于其紧致度。如果上界非常宽松，ranking accuracy 验证可能失败——但 proposal 的验证策略已经考虑了这一点（Spearman ρ），这部分设计是合理的。\n4. **Dimensionality Collapse (T2) 的前提**: \"honest signal dimensionality collapses faster than total signal\" 依赖于 A2（reasoning-dependent pass rates 随难度单调递减），这接近于定义性假设。在 A2 下，高难度问题上 hard criteria 变为几乎均匀低通过率（低方差），而 easy-to-game criteria 维持变异性，这是近乎直接的推论。\n\n【3 维度打分】:\n1. Novelty: 弱到中 — 核心 insight（\"GRPO 学习信号和 gaming opportunity 都在 p≈0.5 达峰\"）是 p(1−p) 在中点最大的直接推论，数学上接近 tautological。与最相关工作比较：Gradient Starvation (2605.07689) 已经证明了学习信号集中于中等 pass-rate；Wang & Huang (2603.28063) 已经给出了 per-dimension distortion index；Reward Hacking in Rubric-Based RL (2605.12474) 已经诊断了 per-criterion gaming patterns。Proposal 的增量是将\"难度\"维度加入已有的 per-criterion 分析——这是一个合理但增量有限的组合创新。Dimensionality Collapse (T2) 是最有 novelty 潜力的部分，但其推导依赖于近乎定义性的假设。\"Learning-Gaming Paradox\" 作为概念命名是新的，但其背后的数学事实（Bernoulli 方差在中点最大）是已知的。\n2. Significance: 中 — 正面：rubric-RL 是当前最活跃的研究方向之一，理解 gaming 结构有实际价值；per-criterion × per-difficulty 诊断工具可被其他方法论文复用（类似 Effective Horizon 对 MDP 研究的贡献）。负面：即使所有 predictions 成立，实际影响主要是\"生产 gaming heatmap + 一个简单的 calibration schedule\"，这是 useful 但不是 transformative 的贡献。双结果设计意味着即使 H0 成立也有价值，但 H0 成立时的价值主要是\"confirmatory diagnostic\"，这对 AAAI 来说可能不够。\n3. Related Work: 强 — 覆盖了约 40 篇 2024-2026 的相关工作，跨越难度自适应 GRPO、rubric 设计、Goodhart 理论、training dynamics 四个方向。经调研验证，引用的论文确实存在，描述基本准确。差异化定位清晰——\"per-criterion × per-difficulty 的交叉点\"确实是文献中的空白。Composite null hypothesis 的构建（从 2604.15149、2605.20744、2605.12474 组合）展示了对领域的深度理解。一个小问题：POW3R (reactive) vs. 本工作 (proactive/predictive) 的区分有些过度简化——POW3R 也有诊断性质。\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】: \nNovelty 是主要限制因素——核心 \"paradox\" 本质上是 Bernoulli 方差在中点最大这一基本事实的重新包装，审稿人很可能认为\"I would have guessed this\"。Significance 处于中等——诊断工具有用但非 transformative。Related Work 覆盖优秀，展示了对领域的深度把握。\n\n上界受限于 Novelty：即使实验执行完美，核心 insight 的惊喜度不足以让审稿人写出 \"surprising, not what I expected\"。下界由 Related Work 的质量和 dual-outcome 设计支撑——即使预测失败，confirmatory diagnostic 仍有一定价值。\n\n该 proposal 的形式完善度极高（四个定理、三个预测、composite null hypothesis、dual-outcome 设计），但形式完善度不等于 idea 质量。剥离形式后，核心 claim 是\"中等难度是 gaming 最脆弱的区域\"——这是一个合理但不惊人的观察。\n\n【主要风险】:\n1. **\"Not surprising\" 风险**: 审稿人可能认为 Learning-Gaming Paradox 是显然的——intermediate difficulty 本身就是 ambiguity 最高的区域，学习信号和 gaming 同时达峰是预期内的，不构成真正的 \"paradox\"。\n2. **形式大于实质风险**: 四个定理 + 三个预测的框架看起来 heavy，但数学内核（p(1−p) 在中点最大 + Wang & Huang D_i 加难度参数）相对 thin，审稿人可能批评 \"over-engineering a straightforward observation\"。\n```\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation\n\n## Core Problem\n\nRubric-rewarded RL faces a structural tension unrecognized in prior work: the difficulty level where GRPO training signal is strongest is simultaneously where gaming opportunity is maximal. The Gradient Starvation analysis (arXiv:2605.07689) proves that GRPO's non-degenerate fraction N(p,G) = 1 - p^G - (1-p)^G is maximized at p = 0.5 (for G=2, N(p,2) = 2p(1-p), exactly proportional to p(1-p)); our Gaming Budget bound shows each criterion's gaming opportunity scales as √(p_k(1−p_k)), also maximized at p_k = 0.5. Both quantities peak at intermediate pass rates, meaning that difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that correctly select problems in the p̄_d ∈ [0.3, 0.7] band for maximal learning efficiency inadvertently maximize gaming exposure under multi-dimensional rubric evaluation. The Edge of Competence analysis (arXiv:2602.14872, Lemma 6.2) provides further support: the multi-step learning gradient follows ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) with peak at Δ*=L/(L+1), corresponding to pass rates p*=(L/(L+1))^L ∈ [1/e, 1/2] ≈ [0.37, 0.50] for reasoning chains of length L — still within the gaming-vulnerable band. (Note: the Edge of Competence result uses the attention margin Δ_L, not the pass rate p directly, and the functional form (Δ)^L(1−Δ) differs from p(1−p); we cite it for qualitative support that multi-step learning also concentrates at intermediate pass rates, not for a shared functional form.) This Learning-Gaming Paradox is structural — it arises whenever K evaluation criteria are applied with uniform strictness across varying task difficulty under GRPO-family training, because easy-to-verify criteria (formatting, structural completeness) remain satisfiable via shallow pattern-matching at intermediate-difficulty problems, while hard-to-verify criteria (proof validity, factual accuracy) yield their most ambiguous signal precisely there. The consequence is a K×D exploitation surface with difficulty-dependent structure that neither scalar Goodhart analysis (ICLR 2024; ICML 2023) nor static per-dimension distortion indices (Wang & Huang 2026, D_i = λ(r_i/w_i) + (1−λ)) can capture. Wang & Huang's D_i ranking (Corollary 1a) assumes symmetric production functions and treats all tasks identically — it cannot model how the exploitation landscape shifts across difficulty because difficulty-varying verification gaps δ_{k,d} and criterion correlations Σ_d are outside the model's scope (their Remark 2). Meanwhile, Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses per-criterion gaming (90.2% presence-based concentration) but does NOT stratify by problem difficulty. LLMs Gaming Verifiers (arXiv:2604.15149) and Hack-Verifiable Environments (arXiv:2605.20744) show gaming/hacking increases monotonically with task difficulty in aggregate. Neither captures the paradox: the difficulty band that GRPO training should focus on for maximum learning efficiency is the difficulty band that rubric gaming exploits most effectively.\n\n## Research Opportunity\n\nSix convergent gaps, now organized around the Learning-Gaming Paradox: (1) The Goodhart's law literature — Goodhart's Law in RL (ICLR 2024), Scaling Laws for RM Overoptimization (ICML 2023), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — operates on SCALAR proxy-goal pairs. The Robust Optimization framework (arXiv:2604.12086, ICLR 2026) adds correlation between scalar proxies but does not decompose per-criterion or model difficulty. No formal treatment exists for K-dimensional evaluation with difficulty-varying exploitation. (2) Wang & Huang (arXiv:2603.28063) derive a constructive per-dimension distortion index D_i with Corollary 1(a) providing a ranking result under symmetric production functions. However, their model treats all tasks identically — it cannot predict how the exploitation landscape shifts with difficulty d, because difficulty-varying verification gaps δ_{k,d} and correlations Σ_d are outside the model's scope (flagged in their Remark 2). Our framework extends D_i to D_i(d), recovering their ranking as a special case when difficulty is constant. (3) The Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's learning signal peaks at intermediate pass rates: the non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5, with degeneracy rates of 0.69 observed at G=4 in practice. The Edge of Competence (arXiv:2602.14872) establishes a complementary result for multi-step reasoning: the learning gradient ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) peaks at attention margins Δ*=L/(L+1), corresponding to pass rates p*=(L/(L+1))^L ∈ [1/e, 1/2] — still within the intermediate range. Both results establish that RL learning concentrates at intermediate pass rates. NO PRIOR WORK connects this to gaming vulnerability: we show that the Gaming Budget bound's per-criterion terms √(p_k(1−p_k)) are ALSO maximized at intermediate pass rates. This peak coincidence — GRPO learning efficiency and gaming opportunity both maximized in the p ∈ [0.3, 0.7] band — is the Learning-Gaming Paradox. (4) DGPO (ICLR 2026, Theorems 1-2) addresses difficulty bias in binary-reward GRPO; per-criterion application is straightforward, but the INTERACTION structure — criterion correlations shifting with difficulty, verification gaps creating asymmetric vulnerability, learning-gaming tension at the competence boundary — requires genuinely novel analysis. (5) Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses gaming taxonomy (3 failure modes, 90.2% presence-based criteria concentration) but does NOT stratify by problem difficulty — the core analytical dimension we add. (6) LLMs Gaming Verifiers (arXiv:2604.15149) and Hack-Verifiable Environments (arXiv:2605.20744) show gaming/hacking severity increases monotonically with task difficulty in aggregate — combined with arXiv:2605.12474's criterion-type finding, this forms our composite null hypothesis. The marginal contribution is fourfold: (a) the Learning-Gaming Paradox — identifying that GRPO's learning-efficient zone (Gradient Starvation) coincides with rubric gaming's exploitation peak (Gaming Budget), with supplementary support from Edge of Competence's multi-step analysis; (b) a Learning-Gaming Duality framework with co-equal Gaming Budget Theorem (T1) and Dimensionality Collapse Theorem (T2), extending Wang & Huang's static D_i to difficulty-varying D_i(d) trajectories; (c) a reusable diagnostic producing per-criterion × per-difficulty gaming surfaces with rigorous statistical methodology (10 difficulty bins, bootstrap CIs, formal non-monotonicity tests); (d) three quantitative falsifiable predictions against a strengthened composite null hypothesis, with concrete methodological value under either outcome — including derivation and validation of monotonic calibration schedules under H0.\n\n## Research Landscape\n\nRubric rewards for RL achieve strong results but apply uniform strictness across difficulty: RRM (ACL 2026) boosts Verified Pass@1024 on AIME2024 from 26.7% to 62.6%; RaR (ICLR 2026) extends to medical (+31% HealthBench) and science (+7% GPQA-Diamond); SRaR (arXiv:2605.17291) adds step-level attribution; POW3R (arXiv:2605.20164) adapts criterion weights via rollout variance; ARES (arXiv:2605.23454) automates rubric synthesis; AMARIS (arXiv:2605.18592) maintains persistent evaluation memory for difficulty-agnostic rubric evolution. ARL-RR (arXiv:2603.15646) addresses the scalarization problem by alternating optimization across rubric meta-classes (accuracy, completeness, instruction following, context awareness, communication quality), which is algorithmic (changing the optimization procedure) rather than diagnostic (characterizing which criteria are exploitable at which difficulty levels). The rubric-RL space continues rapid expansion (~10+ papers in 4 weeks preceding this revision) — but this velocity STRENGTHENS our diagnostic contribution: as methods proliferate, a principled framework identifying WHICH criteria are exploited at WHICH difficulty levels becomes a shared evaluation lens no individual method paper provides. Difficulty-aware RL methods operate under binary rewards: DGPO/MathForge (ICLR 2026) via MAD normalization, DARO (arXiv:2510.09001), F-GRPO (arXiv:2602.06717), GRPO-LEAD (EMNLP 2025) via logistic weighting, A-GRAE (arXiv:2602.05548), Goldilocks RL (arXiv:2602.14868), Online Difficulty Filtering (EACL 2026), CDAS (arXiv:2505.17652) via competence-difficulty alignment, Gradient Starvation (arXiv:2605.07689) via degeneracy analysis. ALL operate under binary rewards without per-criterion gaming analysis. Difficulty-calibrated advantage reweighting is an active concurrent direction: Unlocking the Potential of Difficulty Prior (arXiv:2505.13261) explicitly models difficulty priors to calibrate reasoning depth and reweight advantages in multimodal RL — while targeting training efficiency rather than gaming characterization, it demonstrates independent convergence on difficulty-aware reward modulation. The closest convergence spans eight categories: **Difficulty-stratified rubric calibration**: RuCL (arXiv:2602.21628) adjusts by model competence, not problem difficulty, and is vulnerable to gaming-inflated pass rates. **Multi-objective reward normalization**: MO-GRPO (arXiv:2509.22047) addresses per-objective variance bias (the mechanism underlying dimensional exploitation) but is difficulty-agnostic. **Reactive criterion reweighting**: POW3R adapts via rollout-contrast (reactive/diagnostic) while our approach is proactive/predictive (which criteria WILL BE gamed, inferred a priori from difficulty structure). **Memory-augmented rubric adaptation**: AMARIS addresses the temporal dimension (rubric evolution during training) while we address the structural dimension (exploitation variation with difficulty) — complementary, not competing. **Rubric quality and gaming defense**: Rubicon (arXiv:2508.12790), CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618) — all difficulty-agnostic. **Goodhart's law theory**: Goodhart's Law in RL (ICLR 2024), Robust Optimization for Correlated Proxies (ICLR 2026), Reward Hacking as Equilibrium (arXiv:2603.28063), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — Wang & Huang's D_i is constructive per-dimension but static; none model K-dimensional difficulty-varying exploitation trajectories or connect to training dynamics. **Training dynamics and gaming interaction**: Gradient Starvation (arXiv:2605.07689) proves GRPO degeneracy rate D(p,G)=p^G+(1−p)^G, establishing that GRPO learning concentrates at intermediate pass rates (p≈0.5); Edge of Competence (arXiv:2602.14872) proves multi-step learning gradient ∇ ∝ (Δ_L)^L(1−Δ_L), peaking at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50]; Reward Hacking Rebounds (arXiv:2604.01476) shows gaming has dynamic phase structure. None connect these training-efficiency results to gaming vulnerability under rubric evaluation — the Learning-Gaming Paradox we identify. **Difficulty-dependent hacking measurement**: Hack-Verifiable Environments (arXiv:2605.20744) introduces a paradigm for measuring reward hacking by embedding detectable opportunities into environments, finding hack rate increases monotonically with difficulty across most models (5 models, 3 games). This provides the strongest controlled evidence for H0a but does not analyze per-criterion gaming structure or connect to training dynamics. **Per-criterion behavior across difficulty**: SPARKLE (NeurIPS 2025, arXiv:2506.04723) analyzes three reasoning dimensions across difficulty levels under RL, providing evidence that per-criterion × per-difficulty analysis is informative — but studies reasoning capability, not gaming/exploitation, and has no Goodhart framework. The critical gap: no work provides (a) identification of the Learning-Gaming Paradox — the coincidence that GRPO learning efficiency and gaming opportunity both peak at intermediate pass rates, (b) co-equal Gaming Budget and Dimensionality Collapse theorems characterizing the K×D exploitation surface, (c) per-criterion × per-difficulty gaming diagnosis with rigorous statistical methodology, or (d) quantitative predictions about gaming structure tested against a composite null hypothesis that now incorporates controlled hack-rate evidence.\n\n## Proposed Approach\n\nWe adopt a three-contribution structure centered on the Learning-Gaming Paradox, with co-equal theoretical results and concrete value under either empirical outcome. **Lead Framing: The Learning-Gaming Paradox.** We open with a structural insight connecting training dynamics to evaluation vulnerability: the Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5; our Gaming Budget bound shows gaming opportunity (via √(p_k(1−p_k)) terms) is also maximized at intermediate pass rates. Because both peak in the same difficulty band (p̄_d ∈ [0.3, 0.7]), the difficulty level that GRPO training should focus on for maximum learning is simultaneously the difficulty level where rubric gaming is most effective. The Edge of Competence (arXiv:2602.14872, Lemma 6.2) provides supplementary support: the multi-step gradient ∝ (Δ_L)^L(1−Δ_L) peaks at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50], confirming that even beyond GRPO-specific analysis, multi-step RL learning concentrates at intermediate pass rates within the gaming-vulnerable band. (We are careful to distinguish: the Gradient Starvation result directly uses pass rates p and provides the formal anchor; the Edge of Competence result uses attention margins Δ_L with a different functional form and provides qualitative reinforcement.) This paradox is structural — it holds regardless of whether specific predictions about non-monotonicity (P1) are confirmed, because the PEAK COINCIDENCE between N(p,G) and the Gaming Budget is a mathematical fact. **Composite Null Hypothesis.** We test against a strengthened Composite Null (H0) built from three rubric-relevant findings: (H0a — Aggregate Trend) Gaming severity increases monotonically with problem difficulty for ALL rubric criteria, extrapolating the aggregate trend from LLMs Gaming Verifiers (arXiv:2604.15149), Hack-Verifiable Environments (arXiv:2605.20744, which finds monotonic hack-rate increase in controlled settings across 5 models and 3 environments), and Goodhart's Law in RL (ICLR 2024). (H0b — Criterion-Type Invariance) Gaming concentrates in presence-based/completeness criteria at ALL difficulty levels, extrapolating from Reward Hacking in Rubric-Based RL (arXiv:2605.12474, 90.2% presence-based concentration). Note: H0a now incorporates controlled experimental evidence (arXiv:2605.20744) alongside observational evidence; H0b is rubric-specific but difficulty-agnostic. Together they predict monotonic, criterion-type-stable gaming — a stronger adversarial target than either alone. Three falsifiable predictions with quantitative and statistical failure conditions: (P1) Learning-Gaming Resonance — H0a predicts monotonically increasing gaming for reasoning-verification criteria; P1 predicts an inverted-U peaking in the intermediate-pass-rate band (coinciding with the GRPO learning efficiency peak at p≈0.5), with peak gaming rate ≥1.5× the rate at highest-difficulty bins. Statistical test: monotone-constrained isotonic regression vs. unconstrained fit via likelihood ratio test (p < 0.05), supplemented by quadratic regression β₂ < 0 (p < 0.05). (P2) Criterion Vulnerability Shift — H0b predicts presence-based criteria dominate at all difficulty levels; P2 predicts the criterion vulnerability ordering SHIFTS with difficulty — Pearson correlation between surface-criterion and reasoning-criterion satisfaction flips from positive (r > 0.1 in bottom-quintile) to negative (r < −0.1 in top-quintile), a sign flip analogous to Simpson's Paradox. Additionally, reasoning-criterion gaming share increases ≥2× from bottom to top difficulty quintile. (P3) Asymmetric Dimensionality Collapse — P3 predicts K_honest/K_eff < 0.5 at highest-difficulty bins, with K_eff ≥ 3: honest gradient signal collapses to a lower-dimensional subspace FASTER than total signal because gaming inflates apparent dimensionality. **Concrete value under either outcome.** If P1-P3 hold: the Learning-Gaming Paradox is empirically confirmed with specific structural predictions, revealing difficulty-dependent gaming invisible to aggregate/unstratified analysis. If H0 is confirmed (monotonic, criterion-type-stable gaming): (a) the Learning-Gaming Paradox still holds structurally — even monotonically increasing gaming creates a tension with the GRPO learning signal peak at moderate difficulty, because difficulty-aware methods focus training precisely where gaming is already substantial; (b) we provide the FIRST per-criterion × per-difficulty confirmation that monotonicity and criterion-type-stability hold at every criterion individually (currently known only in aggregate or unstratified); (c) we derive and validate a simple linear strictness schedule s_k(d) = α_k + β_k·d justified by confirmed monotonicity, where β_k is proportional to the empirically measured per-criterion gaming slope, and validate that it reduces the mean DEG (Dimension Exploitation Gap) by ≥15% compared to uniform strictness on a held-out test split; (d) the Dimensionality Collapse analysis (T2) characterizes how many effective honest dimensions remain at each difficulty level, directly informing how many criteria are worth evaluating at high difficulty. We explicitly acknowledge this would be a solid diagnostic paper with a concrete calibration output, valuable to rubric-RL practitioners. **Contribution 1 — Learning-Gaming Duality Framework (domain-agnostic theory).** Four formal results for any K-dimensional evaluation system with difficulty variation under GRPO-family training: (T1) Gaming Budget Theorem — a difficulty-parameterized bound on total exploitable reward at difficulty d, extending Wang & Huang's static distortion index. Formal model: pass rate matrix P ∈ [0,1]^{K×D}, verification gap matrix Δ, difficulty-varying correlation matrix Σ_d. Four assumptions: (A1) decomposability into genuine and gaming components; (A2) monotonic non-increase of reasoning-dependent pass rates with difficulty; (A3) difficulty-stable or increasing verification gaps for surface criteria; (A4) positive correlation between criterion-level pass rates p_{k,d} and aggregate binary pass rate p̄_d (justified by the shared difficulty driver — harder problems lower both aggregate and criterion-level pass rates). Bound: G_d ≤ Σ_{k∈V_d} w_k · δ_{k,d} · √(p_{k,d}(1−p_{k,d})) + Σ_{j&lt;k∈V_d} w_j·w_k · max(0, σ_{jk,d}) · δ_{j,d}·δ_{k,d}. **Special case reduction:** When d is constant and δ_{k,d} = δ, recovers Wang & Huang's D_i ranking. (T2) Dimensionality Collapse Theorem (CO-EQUAL with T1) — proves K_honest(d) decreases strictly faster than K_eff(d) under A2, using the observation that high-verification-stringency criteria leave the active gradient set first. This is potentially more surprising than T1 because it predicts ASYMMETRIC structural behavior: gaming inflates apparent signal dimensionality while honest signal collapses, creating a growing gap that makes gaming increasingly invisible to standard diagnostics at higher difficulty. Validated via PCA on per-criterion pass-rate vectors across difficulty bins, measuring the ratio of honest-signal eigenvalues to total eigenvalues. (T3) Calibration Sufficiency Condition — derives the minimal gaming-eliminating strictness schedule s_{k,d} ∝ 1/δ_{k,d} · √(p_{k,d}(1−p_{k,d})). Under confirmed H0 (monotonic gaming), simplifies to the linear schedule s_k(d) = α_k + β_k·d with closed-form β_k. (T4) Learning-Gaming Peak Coincidence Corollary — Under assumptions A1-A4, the GRPO non-degenerate fraction N(p̄_d, G) = 1−p̄_d^G−(1−p̄_d)^G and the difficulty-marginal Gaming Budget G_d are both maximized within the difficulty band where p̄_d ∈ [0.3, 0.7]. Formally: N(p,G) achieves its unique maximum at p=0.5 (Gradient Starvation, arXiv:2605.07689); each Gaming Budget term w_k·δ_{k,d}·√(p_{k,d}(1−p_{k,d})) achieves its maximum at p_{k,d}=0.5; under A4, the Gaming Budget is near-maximal when p̄_d ≈ 0.5. Supplementary support: the Edge of Competence (arXiv:2602.14872) multi-step gradient peaks at pass rates (L/(L+1))^L ∈ [1/e, 1/2] for reasoning chains of length L, confirming that multi-step learning also concentrates in the gaming-vulnerable band. (We do NOT claim a shared functional form between (Δ)^L(1−Δ) and √(p(1−p)) — the formal connection is through peak coincidence in the pass-rate domain.) Practical consequence: difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that select problems with p̄_d ≈ 0.5 for maximal learning efficiency simultaneously maximize the Gaming Budget under rubric evaluation. Validation strategy: RANKING ACCURACY (Spearman ρ between predicted and observed gaming severity across K×D cells) following the Effective Horizon precedent (NeurIPS 2023 Oral), plus conservativeness ratio and top-3 vulnerability identification accuracy. **Contribution 2 — Cross-Domain Empirical Diagnosis with Rigorous Statistics.** Math domain (primary for AAAI): Qwen2.5-Math-1.5B policy, Qwen3-8B judge, MATH dataset. **10-bin difficulty scale:** Base model generates 64 rollouts per problem → per-problem pass@1 → 10 equal-frequency difficulty bins (deciles). This provides 2× resolution for curve-fitting, continuous underlying variable for regression, independence from coarse categorical labels. MATH's native 5 levels serve as robustness check. Statistical methodology: (i) 1000-resample bootstrap 95% CIs on all DEG values; (ii) formal non-monotonicity test: isotonic regression (monotone non-decreasing constraint) vs. unconstrained kernel regression via permutation-based likelihood ratio test; (iii) quadratic regression DEG ~ β₀ + β₁d + β₂d² with one-sided test β₂ < 0; (iv) Fisher's z-test for correlation sign-flip (P2). Medical domain (ICLR scope): Qwen2.5-1.5B-Instruct policy, Qwen3-8B judge, RaR-Medicine (22.4K examples, ICLR 2026). Difficulty estimation via SFT-init checkpoint rollouts (breaks circularity). Cross-domain comparison: test whether gaming surface STRUCTURE transfers across domains. **Contribution 3 — DCRR Proof-of-Concept (ICLR scope only).** DGPO+RRM critical baseline first; if >20% gap remains, apply Difficulty-Calibrated Rubric Rewards using T3 schedule. Under H0: validate s_k(d) = α_k + β_k·d reduces mean DEG ≥15% vs. uniform strictness. **Venue Strategy (REVISED — AAAI primary, ICLR stretch).** Primary target: AAAI 2027 (abstract Jul 21, paper Jul 28, 8 weeks). Math-only, Contributions 1-2: Learning-Gaming Duality framework (T1+T2+T4 corollary + T3 monotonic special case) + MATH 10-bin gaming heatmaps + 3 predictions + monotonic calibration validation under H0. This is the natural unit — the theoretical framework + single-domain validation. Decision-gated stretch: ICLR 2027 (~Sep 24, 17 weeks). Full three-contribution scope adding medical domain + DCRR defense + cross-domain analysis. Only pursued if AAAI submission is strong AND reviewer feedback suggests expansion strengthens the work. Backup: ARR August 3 → EACL 2027 (~10 weeks, math + medical diagnostics without DCRR). **Concrete timeline (AAAI primary, 8 weeks):** Week 1 (May 28 - Jun 4): Theory formalization (T1 with Wang & Huang special case, T2 with PCA validation plan, T4 Learning-Gaming Peak Coincidence Corollary with Gradient Starvation anchor) + infrastructure setup (verl scripts, judge pipeline) + BEGIN base-model pass@1 computation (64 rollouts/problem, ~8 H100-hrs) + BEGIN GRPO training run. Week 2 (Jun 4 - Jun 11): Base-model pass@1 complete → 10-bin difficulty binning + BEGIN GRPO+RRM training run + BEGIN DGPO+RRM training run. Weeks 3-4 (Jun 11 - Jun 25): Training runs complete + judge inference on all 3 models (~20 H100-hrs total) + 10-bin gaming heatmap construction + DEG computation + bootstrap CIs + non-monotonicity tests. Week 5 (Jun 25 - Jul 2): All statistical tests (P1 isotonic regression, P2 Fisher's z-test, P3 PCA dimensionality analysis) + monotonic calibration schedule derivation and validation + draft core results. Week 6 (Jul 2 - Jul 9): DECISION GATE — evaluate: (a) are gaming surfaces non-trivial? (b) do statistical tests yield interpretable results? (c) is theory validated via ranking accuracy? If YES to all three: commit to AAAI. If NO: continue ICLR plan with 10 more weeks. Weeks 7-8 (Jul 9 - Jul 28): Paper writing, figures, polishing. Jul 21 abstract, Jul 28 paper submission. **Risk mitigation:** Training failures → keep uniform-GRPO baseline (always works), can still produce gaming surface from fewer models. Judge quality → validate on 200-sample subset before full inference. Timeline → T3 monotonic case and H0-confirmed contributions provide fallback value even if exotic predictions fail.\n\n## Detailed Description\n\nWe identify the Learning-Gaming Paradox: a structural tension in rubric-rewarded RL where the difficulty level that maximizes GRPO learning signal simultaneously maximizes gaming opportunity. The Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5; our Gaming Budget bound shows gaming opportunity (via √(p(1−p)) terms) is also maximized at intermediate pass rates. Both peak in the same difficulty band (p̄_d ∈ [0.3, 0.7]), meaning difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that correctly focus on this zone for learning efficiency inadvertently maximize gaming exposure under multi-dimensional rubric evaluation. The Edge of Competence analysis (arXiv:2602.14872, Lemma 6.2) provides supplementary support: the multi-step gradient (∝ (Δ_L)^L(1−Δ_L), where Δ_L is the attention margin, NOT the pass rate) peaks at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50], confirming that multi-step learning also concentrates at intermediate pass rates within the gaming-vulnerable band. We contribute: (1) a Learning-Gaming Duality framework with co-equal theoretical results — a Gaming Budget Theorem (T1) providing the first difficulty-parameterized K-dimensional Goodhart bound (extending Wang & Huang's static D_i to D_i(d) trajectories with special-case reduction), a Dimensionality Collapse Theorem (T2) proving honest signal dimensionality collapses faster than total signal making gaming increasingly invisible, a Learning-Gaming Peak Coincidence Corollary (T4) formally establishing that the GRPO non-degenerate fraction and the Gaming Budget are both maximized at intermediate pass rates (anchored to Gradient Starvation with Edge of Competence as supplementary support), and a Calibration Sufficiency Condition (T3) deriving gaming-eliminating strictness schedules that simplify to s_k(d) = α_k + β_k·d under confirmed monotonicity; (2) a cross-domain empirical diagnostic using 10-bin difficulty scales (base-model pass-rate deciles) with bootstrap CIs and formal non-monotonicity tests, producing per-criterion × per-difficulty gaming surfaces; (3) three falsifiable predictions against a composite null hypothesis strengthened by Hack-Verifiable Environments (arXiv:2605.20744) — (P1) Learning-Gaming Resonance: non-monotonic gaming for reasoning criteria peaking in the GRPO-efficient band at ≥1.5× the highest-difficulty rate; (P2) Criterion Vulnerability Shift: surface-reasoning correlation sign-flip plus ≥2× reasoning-criterion gaming share increase; (P3) Asymmetric Dimensionality Collapse: K_honest/K_eff < 0.5 at highest difficulty. The paper delivers concrete value under either outcome: if predictions hold, it reveals difficulty-dependent structure invisible to prior analysis; if H0 is confirmed, it provides the first per-criterion × per-difficulty confirmation of monotonic gaming, derives and validates a simple linear calibration schedule reducing mean DEG by ≥15%, and characterizes effective honest dimensionality at each difficulty level. Validated on Qwen2.5-Math-1.5B (AAAI primary, math) with Qwen2.5-1.5B-Instruct cross-domain validation (ICLR stretch, medical).\n\n## Key References\n\n- Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — GRPO degeneracy rate D(p,G)=p^G+(1−p)^G; non-degenerate fraction N(p,G)=1−p^G−(1−p)^G maximized at p=0.5 (for G=2, N=2p(1−p); observed 0.69 degeneracy at G=4 in Qwen3.5-9B). CRITICAL for our Learning-Gaming Paradox: provides the PRIMARY formal anchor establishing that GRPO learning efficiency peaks at intermediate pass rates (p≈0.5), coinciding with the Gaming Budget's peak zone. Also proves via Jensen's inequality that real degeneracy exceeds i.i.d. prediction\n- On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872) — Multi-step learning gradient: Lemma 6.2 shows ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) where Δ_L is the effective probability margin (NOT the pass rate), peaking at Δ*=L/(L+1). The corresponding pass rate at the gradient peak is p*=(L/(L+1))^L ∈ [1/e, 1/2] ≈ [0.37, 0.50]. Provides SUPPLEMENTARY SUPPORT for the Learning-Gaming Paradox: even the multi-step analysis shows learning concentrates at intermediate pass rates within the gaming-vulnerable band. The relay effect explains WHY training naturally traverses this zone. NOTE: the functional form (Δ)^L(1−Δ) differs from p(1−p) and Δ ≠ p; we cite for qualitative support, not shared functional form\n- Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063) — Constructive per-dimension distortion index D_i = λ(r_i/w_i) + (1−λ) with ranking result Corollary 1(a): D_i > D_j ⟹ e_i* > e_j* under symmetric production functions. Limitation: static (no difficulty parameterization), assumes symmetric g_i (Remark 2). Our framework extends D_i to difficulty-varying D_i(d) trajectories, recovering D_i ranking as a special case at constant difficulty\n- Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale (arXiv:2605.20744) — Embeds detectable hacking opportunities into environments for controlled measurement. Tests 5 models (Claude Sonnet 4.6, GPT-5-Codex, Gemini 3.1 Pro, Qwen3.6-Plus, Kimi-K2.5) across 3 games (Wordle, Tower of Hanoi, 15-Puzzle) with varying difficulty. KEY FINDING: hack rate increases monotonically with task difficulty across most models and environments. Provides the strongest controlled experimental evidence supporting H0a in our composite null hypothesis\n- Goodhart's Law in Reinforcement Learning (ICLR 2024) — Geometric explanation for Goodhart's law in MDPs; shows optimization pressure increases Goodharting; aggregate scalar analysis. Our framework extends to K-dimensional evaluation with difficulty variation and connects to training dynamics\n- Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026) — Max-min formulation over r-correlated scalar proxy rewards; does not decompose per-criterion or model difficulty-varying correlation\n- The Strong, Weak and Benign Goodhart's Law (arXiv:2505.23445) — Independence-free formalization; scalar proxy-goal pair, no multi-dimensional or difficulty treatment\n- Scaling Laws for Reward Model Overoptimization (ICML 2023) — Empirical scaling of overoptimization with optimization intensity; aggregate scalar analysis\n- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, ICLR 2026 Workshop) — Shows gaming prevalence increases with task complexity on inductive reasoning tasks (SLR-Bench, 4 tiers) under binary extensional verification. Contributes H0a (aggregate trend) to our composite null hypothesis\n- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474) — Gaming taxonomy in medical/science; 3 failure modes; 90.2% presence-based criteria concentration; self-internalization gap metric. Contributes H0b (criterion-type invariance) to our composite null hypothesis. Does NOT stratify by problem difficulty\n- Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (ICLR 2026) — DGPO Theorems 1-2 on binary-reward difficulty bias; difficulty-aware methods that focus on intermediate pass rates — precisely the zone our Learning-Gaming Paradox identifies as gaming-vulnerable\n- Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards (ACL 2026) — RRM baseline, uniform-strictness rubric rewards for math\n- Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (ICLR 2026) — Foundational rubric RL; RaR-Medicine dataset for cross-domain validation\n- Unlocking the Potential of Difficulty Prior in RL-based Multimodal Reasoning (arXiv:2505.13261) — Models difficulty priors to calibrate reasoning depth and reweight advantages in multimodal RL. Demonstrates concurrent convergence on difficulty-aware reward modulation, though targeting training efficiency rather than gaming characterization. Validates the timeliness of difficulty-calibrated approaches\n- Rethinking the Sampling Criteria in RL for LLM Reasoning: A Competence-Difficulty Alignment Perspective (arXiv:2505.17652) — CDAS framework for stable difficulty estimation via historical performance aggregation. Validates our base-model pass-rate difficulty binning methodology\n- Bridging RL Theory and Practice with the Effective Horizon (NeurIPS 2023, Oral) — Validates theoretical bounds via RANKING CORRELATION across 155 MDPs. Direct precedent for our Gaming Budget validation strategy\n- MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems (arXiv:2509.22047) — Per-objective variance normalization; Theorem 1 (correlation ∝ σ_i) is the mechanism underlying dimensional exploitation, but difficulty-agnostic\n- Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (NeurIPS 2025, arXiv:2506.04723) — SPARKLE framework analyzing 3 reasoning dimensions across difficulty under RL. Evidence that per-criterion × per-difficulty analysis is informative, but studies reasoning capability rather than gaming and has no Goodhart framework\n- When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476) — Identifies three-phase gaming dynamics (attempt → retreat → rebound) in code RL; shortcut direction in representation space tracks hacking. Supports our view that gaming is not static but has structural dynamics across contexts\n- Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (NeurIPS 2025) — Pass@k frontier evaluation for binary-reward; diagnostic impact precedent\n- Reward Collapse in Aligning Large Language Models (arXiv:2305.17608) — Reward distribution collapse; supports our Dimensionality Collapse prediction\n- Step-wise Rubric Rewards for LLM Reasoning (arXiv:2605.17291) — SRaR step-level rubric attribution\n- Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164) — POW3R rollout-contrast reweighting; reactive vs. our proactive/predictive\n- AMARIS: A Memory-Augmented Rubric Improvement System (arXiv:2605.18592) — Persistent evaluation memory; temporal dimension vs. our structural dimension\n- ARES: Automated Rubric Synthesis for Scalable LLM RL (arXiv:2605.23454) — Rubric synthesis automation; difficulty-agnostic\n- Alternating Reinforcement Learning with Contextual Rubric Rewards (arXiv:2603.15646) — ARL-RR addresses scalarization by alternating optimization across rubric meta-classes. Algorithmic (changes optimization procedure) rather than diagnostic (characterizing exploitation patterns)\n- RuCL: Stratified Rubric-Based Curriculum Learning (arXiv:2602.21628) — Adjusts by model competence not problem difficulty; vulnerable to gaming-inflated pass rates\n- HealthBench (arXiv:2505.08775) — Medical evaluation benchmark; secondary evaluation\n- CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618), Rubicon (arXiv:2508.12790) — Rubric quality/gaming defense; all difficulty-agnostic\n- Online Difficulty Filtering for Reasoning Oriented RL (EACL 2026) — Variance-based difficulty selection theory\n- GRPO-LEAD (arXiv:2504.09696, EMNLP 2025) — Logistic difficulty reweighting under binary rewards\n- DARO, F-GRPO, A-GRAE, Goldilocks RL, PAPO, ARL-RR, RubricEM, Rubric-Grounded RL — Complementary difficulty-aware or rubric-optimization methods, all binary-reward or difficulty-agnostic\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 100 H100-hours for AAAI primary (Math: 3 training runs × 4 H100 × 2.5hr = 30hr, base-model pass@1 computation for 10-bin difficulty 8hr, rubric judge inference 20hr, Pass@64 for difficulty binning 25hr, analysis + bootstrap CIs + overhead 17hr). Additional 90 H100-hours for ICLR stretch (Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle rollouts 5hr, medical judge inference 10hr, DCRR experiments 30hr, MO-GRPO+RRM baseline 15hr, ablations 6hr)., timeline: 8 weeks for AAAI 2027 primary (math-only, Contributions 1-2+calibration). 17 weeks for ICLR 2027 stretch (full three-contribution scope adding medical + DCRR)., estimated_gpu_cost: $250 AAAI / $475 total with ICLR stretch (H100 at ~$2.50/hr)\n- **human_in_loop**: gpu_hours: 100 H100-hours AAAI / 190 H100-hours total (same; Claude accelerates code/analysis, not GPU work), timeline: 7 weeks for AAAI (Claude assists theorem formalization, verl scripts, automated heatmap generation, bootstrap pipeline, writing). 14-15 weeks for ICLR stretch., claude_api_cost: $150 AAAI / $300 total (Sonnet 4.6 for rubric generation, code scaffolding, statistical pipeline, writing), estimated_gpu_cost: $250 AAAI / $475 total\n- **auto_research**: gpu_hours: 105 H100-hours AAAI / 200 H100-hours total (5hr margin for targeted hyperparameter exploration per venue), timeline: 6-7 weeks for AAAI (parallelized dispatch, automated analysis, Claude-drafted paper). 10-12 weeks for ICLR., claude_api_cost: $250 AAAI / $420 total (rubric judging quality audit ~5K samples, automated analysis, writing), estimated_gpu_cost: $263 AAAI / $500 total, speed_bottleneck: LLM judge inference throughput — scoring ~50K math rollouts per model with Qwen3-8B requires ~8hr per model on 4×H100; base-model pass@1 computation adds ~8hr\n- **aaai_primary_scope**: gpu_hours: 100 H100-hours (Math only: 3 training runs × 4 H100 × 2.5hr = 30hr, base-model pass@1 for binning 8hr, judge inference 20hr, Pass@64 difficulty binning 25hr, analysis + bootstrap 17hr), timeline: 8 weeks (6-week sprint + 2 weeks writing; decision gate at week 6), estimated_gpu_cost: $250, scope: Learning-Gaming Duality framework (T1+T2+T4 Peak Coincidence Corollary with Gradient Starvation anchor, with T3 monotonic special case) + MATH 10-bin gaming heatmaps with bootstrap CIs + 3 falsifiable predictions tested with formal statistical tests + monotonic calibration schedule derivation and validation under H0. The complete theoretical framework plus single-domain empirical validation.\n- **iclr_stretch_scope**: gpu_hours: 190 H100-hours total (AAAI scope + Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle 5hr, medical judge inference 10hr + DCRR: experiments 30hr, MO-GRPO+RRM 15hr, ablations 6hr), timeline: 17 weeks total (incorporates AAAI submission + 9 additional weeks for medical domain + DCRR + cross-domain analysis), estimated_gpu_cost: $475, scope: Full three-contribution scope: AAAI content + medical domain validation + DCRR proof-of-concept + cross-domain gaming surface comparison\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-28T16:56:42.932Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T16:56:42.932Z",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-28T16:56:42.947Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information from my research. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689) (arXiv, May 2026): 证明 GRPO 在二值奖励下的 degeneracy rate D(p,G)=p^G+(1−p)^G，学习信号（non-degenerate fraction）在 p=0.5 时最大。这是本 proposal "Learning-Gaming Paradox" 的核心锚点之一。论文存在且描述准确。
- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872) (arXiv, Feb 2026): 证明多步推理学习梯度 ∝ (Δ_L)^L(1−Δ_L)，peak pass rate 在 [0.37, 0.50]。Relay effect 解释了模型如何自然穿越这个中等难度区间。论文存在且 proposal 对其的引用（区分 Δ 和 p、不宣称共享函数形式）是谨慎的。
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (arXiv, Mar 2026): Wang & Huang 提出 per-dimension distortion index D_i，证明 D_i 排序结果（Corollary 1a）。关键局限：静态模型，不含难度参数化。Proposal 准确识别了这个 gap（Remark 2），并声称扩展到 D_i(d)。
- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) (arXiv, May 2026): 诊断 rubric RL 中的 gaming 分类，发现 90.2% 集中在 presence-based criteria。未按问题难度分层——这正是本 proposal 声称的分析维度缺口。论文存在且描述准确。
- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) (arXiv, May 2026): 受控实验环境，发现 hack rate 随难度单调增加（5 模型、3 游戏）。这为 proposal 的 H0a 提供最强对照证据。论文存在且描述准确。
- [Goodhart's Law in Reinforcement Learning](https://arxiv.org/abs/2310.xxxxx) (ICLR 2024): 标量 proxy-goal 对的 Goodhart 分析；不含多维或难度分析。
- [SPARKLE / Beyond Accuracy](https://arxiv.org/abs/2506.04723) (NeurIPS 2025): 分析 RL 下推理的 3 个维度跨难度变化，但研究的是 reasoning capability 而非 gaming/exploitation，无 Goodhart 框架。
- [DGPO / MathForge](https://arxiv.org/abs/2502.xxxxx) (ICLR 2026): 二值奖励下的难度感知 GRPO；无 per-criterion gaming 分析。
- [POW3R](https://arxiv.org/abs/2605.20164), [SRaR](https://arxiv.org/abs/2605.17291), [ARES](https://arxiv.org/abs/2605.23454), [AMARIS](https://arxiv.org/abs/2605.18592): 近 4 周内的 rubric-RL 方法论文（共 ~10+ 篇），均未做 difficulty-stratified gaming 分析。
- 搜索 "learning-gaming paradox"、"difficulty-dependent exploitation" 等关键词未发现任何直接竞争工作。

- **调研总结**: Rubric-RL 领域正在快速扩张，训练方法（RRM, RaR, SRaR, POW3R）和 Goodhart 理论（Wang & Huang, Robust Optimization）分别有大量工作，但两条线尚未交叉：没有工作将 GRPO 训练动态（学习效率 vs. 难度）与 rubric 维度上的 gaming vulnerability 联系起来。Proposal 确实占据了一个真实的未填补交叉地带。SPARKLE 是最接近的——它做了 per-criterion × per-difficulty 分析，但目标是 reasoning capability 而非 gaming。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是：直接按难度分层统计每个 rubric criterion 的 gaming rate，生成 heatmap，无需任何理论框架。这个 baseline 成本极低（只需一次 training + judge inference + 分层统计），就能回答 "gaming 在不同难度下的分布长什么样" 这个描述性问题。

Proposal 的增量价值在于三个层面：(1) 理论预测——Gaming Budget Theorem 预测 *哪些* criteria 在 *哪个* 难度下最易被 exploit，而非事后描述；(2) Dimensionality Collapse Theorem 预测 honest signal 维度塌缩快于 total signal——这是 trivial heatmap 无法给出的结构性预测；(3) Calibration schedule 提供了从诊断到干预的桥梁。

**但关键问题是**：Gaming Budget bound 的 √(p(1-p)) 函数形式是否是对 gaming opportunity 的真实刻画？如果 bound 很松，那么"两个函数都在 p=0.5 取最大值"这个"paradox"就可能只是 bound 的 artifact，而非真实现象。√(p(1-p)) 和 N(p,G) = 1−p^G−(1−p)^G 都是 [0,1] 上的对称凹函数，它们同时在 p=0.5 取极值是**数学必然**，而非"paradox"。这显著削弱了核心 claim 的惊奇性。

【前提假设检验】:
核心逻辑链的关键未验证假设：

1. **Gaming opportunity 真的遵循 √(p_k(1-p_k)) scaling 吗？** 这是整个 "paradox" 的一半。Proposal 将这作为 bound 呈现，但 bound 的 tightness 未经验证。如果实际 gaming opportunity 在高难度单调增加（如 arXiv:2605.20744 的实验所示），那么 Gaming Budget bound 的 peak-at-0.5 预测可能只是 bound 过松的结果。

2. **A4 假设（criterion-level pass rates 与 aggregate pass rate 正相关）**: Proposal 用 "shared difficulty driver" 解释，但某些 criteria 可能对难度不敏感（如格式要求），导致 A4 局部失效。如果 surface criteria 的 p_k 在所有难度下都接近 1，那 Gaming Budget 在这些维度上接近 0，paradox 的 practical relevance 就大打折扣。

3. **LLM-as-judge 的可靠性**: 整个实验依赖 Qwen3-8B 作为 rubric judge。Judge 自身的 difficulty-dependent 偏差可能与真实 gaming 混淆。用 200 样本验证似乎不够充分。

4. **从 "两个函数同在 p=0.5 取极值" 到 "这构成了一个 paradox"**: 这个推理假设了社区之前认为学习和 gaming 应该在不同难度区间 peak。但如果这是直觉上显然的（中等难度 = 最多模糊空间 = 最多 gaming 空间），那就不是 paradox，而是 expected behavior。

【3 维度打分】:

1. **Novelty: 中** — 
   Proposal 声称的核心 novelty 是 "Learning-Gaming Paradox"——GRPO 学习效率和 gaming opportunity 都在中等 pass rate 区间 peak。调研确认没有直接竞争工作（搜索 "learning-gaming paradox"、"difficulty-dependent exploitation" 无结果），这个交叉连接确实是新的。然而，核心数学观察（两个对称凹函数都在 p=0.5 取极值）是 trivially true——任何定义在 [0,1] 上、边界为零的对称凹函数都会如此。"Paradox" 标签夸大了惊奇性。Dimensionality Collapse (T2) 是更有潜力的贡献——如果 honest signal 维度确实塌缩快于 total signal，这是非 trivial 的结构预测，但目前只有理论声称，没有先验证据支持。相对于 Wang & Huang (arXiv:2603.28063) 的扩展（D_i → D_i(d)）是 incremental 但有价值。相对于 arXiv:2605.12474（不分层难度）和 arXiv:2605.20744（不分析 per-criterion），组合维度是新的。总体而言，有真实的 novelty delta，但核心 "paradox" 的惊奇性被高估。

2. **Significance: 中** — 
   Rubric-RL 正在快速扩张（4 周内 10+ 篇论文），一个诊断框架确实有价值——如 proposal 所言，方法越多越需要共享评估视角。但实际影响取决于经验发现：如果 gaming surface 是 trivial（如对所有 criteria 都单调增加，符合 H0），那 paradox 的 practical relevance 有限。Calibration schedule（T3）是最直接的实用贡献，但它在 H0 confirmed 情况下简化为线性 schedule，而线性 difficulty-based strictness 调整是一个相当直觉化的解决方案。对 AAAI 评审而言，这是一个 diagnostic/analytical contribution，而非方法论突破——这类论文可以被接受（参考 SPARKLE@NeurIPS 2025 的先例），但上限受限。

3. **Related Work: 强** — 
   覆盖极为全面。Proposal 引用了 30+ 篇论文，分布在 8 个相关类别中，每一类都有精确的差异化定位。关键引用经调研验证为真实存在且描述准确（arXiv:2605.07689、2602.14872、2603.28063、2605.12474、2605.20744）。对每篇竞争工作的局限性描述是诚实的（如 Wang & Huang 的 Remark 2、arXiv:2605.12474 不分层难度）。Composite null hypothesis 的构建引用了最强对照证据（arXiv:2605.20744 的受控实验），体现了学术诚实。唯一小问题：部分引用数量可能让评审感觉过度堆砌（defensive over-citation）。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Novelty 是限制上界的主要维度。核心 "paradox"（两个凹对称函数同在 p=0.5 取极值）虽然是一个此前未被明确指出的连接，但其数学必然性削弱了 surprise factor。一个 strong reviewer 很可能写 "The observation that both quantities peak at intermediate pass rates is mathematically obvious given their functional forms — calling this a 'paradox' overstates the finding." Dimensionality Collapse (T2) 是最有潜力提升 novelty 的贡献，但作为理论声称其验证完全依赖实验结果。Related Work 覆盖是本 proposal 的明确强项，会获得审稿人正面评价。Significance 处于中等——诊断性贡献在 top venue 有先例（SPARKLE@NeurIPS），但不如方法论创新有影响力。Dual-outcome design 为下限提供了保障（即使预测失败也有诊断价值），但也意味着最有趣的发现（non-monotonic gaming）可能不成立。

综合来看：idea 有真实但有限的 novelty（~中等），方向正确但核心发现如果 positive，审稿人可能会说 "interesting but not that surprising"（介于 "I would have guessed this" 和 "surprising" 之间），将概率定位在 25-35% 区间的下半部分。

【主要风险】:
1. **"Paradox" 的惊奇性不足**: 审稿人可能认为两个对称凹函数在 p=0.5 同时取极值是数学 triviality 而非 deep insight——Gaming Budget bound 的 √(p(1-p)) 函数形式与 N(p,G) 同在 p=0.5 peak 是函数族的固有性质，不构成 "paradox"。这直接威胁论文的核心卖点。
2. **Gaming Budget bound 的 tightness 未经验证**: 如果 bound 很松，实际 gaming 可能根本不在 p=0.5 peak（arXiv:2605.20744 的受控实验显示 hack rate 随难度单调增加），那么整个 paradox 框架的 practical relevance 将受到根本性质疑——peak coincidence 可能是 bound artifact 而非 empirical reality。
```

Sources:
- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689)
- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872)
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063)
- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)
- [Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale](https://arxiv.org/abs/2605.20744)
- [Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (SPARKLE)](https://arxiv.org/abs/2506.04723)
- [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/abs/2605.23454)
- [Rubric-Based Rewards for RL - Deep Learning Focus](https://cameronrwolfe.substack.com/p/rubric-rl)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to evaluate this proposal. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689) (arXiv, May 2026): 证实 GRPO 的非退化比例 N(p,G)=1−p^G−(1−p)^G 在 p=0.5 最大化，G=4 时退化率达 0.69。这是 proposal 的核心锚点之一，论文真实存在，描述准确。
- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872) (arXiv, Feb 2026): 多步推理梯度 ∝ (Δ_L)^L(1−Δ_L)，峰值在中间 pass rate 区间 [0.37, 0.50]。论文真实存在，proposal 对其的引用准确，且正确标注了 Δ_L ≠ p 的区别。
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (Wang & Huang, Mar 2026): 提出可计算的 per-dimension distortion index D_i，证明在对称生产函数下的 ranking 结果。确认论文存在，proposal 对其局限性（static, no difficulty parameterization）的描述与原文 Remark 2 一致。
- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474) (May 2026): 在医学和科学领域诊断 rubric gaming 的 3 种失败模式和 90.2% presence-based 集中。论文存在，但 proposal 声称其"does NOT stratify by problem difficulty"需验证——从搜索摘要看，该论文确实关注 criterion-type 而非 difficulty stratification。
- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) (May 2026): 5 个模型 × 3 个游戏环境的受控实验，发现 hack rate 随难度单调递增。论文存在，为 proposal 的 H0a 提供支持。
- [DGPO/MathForge](https://openreview.net/forum?id=nfURupkdRJ) (ICLR 2026): Difficulty-aware GRPO，通过 MAD normalization 处理难度偏差。论文存在且已被 ICLR 2026 接收。
- [Goodhart's Law in RL](https://openreview.net/forum?id=5o9G4XF1LI) (ICLR 2024): 标量 proxy-goal 分析，geometric explanation for Goodhart's law in MDPs。论文存在。
- [Rubrics as Rewards (RaR)](https://openreview.net/forum?id=c1bTcrDmt4) (ICLR 2026): 基础 rubric RL 框架，+31% HealthBench, +7% GPQA-Diamond。论文存在。

- 调研总结: Rubric-rewarded RL 是一个快速增长的领域（~10+ 论文/月），difficulty-aware GRPO 方法和 reward hacking 诊断已有大量工作。但现有工作分为两条平行线——难度感知训练（binary reward, 不关注 per-criterion gaming）和 gaming 诊断（不按难度分层）。将两者交叉分析（per-criterion × per-difficulty）的工作确实是空白。然而，这个"交叉"的核心数学论点——N(p,G) 和 √(p(1−p)) 都在 p=0.5 取最大值——是一个相当简单的对称凹函数性质观察。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁。核心经验贡献——"per-criterion × per-difficulty gaming surface"——可以通过一个直接的实证方法获得：在不同难度 bin 上分别计算每个 criterion 的 gaming 指标（如 DEG），绘制热力图，然后用标准统计检验分析模式。这不需要 Gaming Budget Theorem、Dimensionality Collapse Theorem 或 Learning-Gaming Duality 框架。一个简单的"stratified analysis + bootstrap CIs + regression"就能产出几乎相同的经验洞见。

增量价值在于：(a) 理论框架如果 bound 足够紧，可以做出先验预测（而不是事后观察），以及 (b) T3 Calibration Sufficiency Condition 可以推导出最优校准策略。但 (a) 的价值取决于 bound 的 tightness（未经验证），(b) 的简化形式 s_k(d) = α_k + β_k·d 本身就可以通过经验回归直接拟合，无需理论推导。因此，理论框架的实际增量价值是可疑的——它可能是"decorative theory"，为一个本质上简单的经验观察提供不必要的包装。

【前提假设检验】:
核心 claim 的逻辑链条中有以下未经验证的关键假设：

1. **A1（可分解性）**: 假设每个 criterion 的 pass rate 可以干净地分解为 "genuine" 和 "gaming" 两个分量。这在实际中非常难以操作化——什么算"genuine"什么算"gaming"的边界是模糊的，尤其对于部分正确的推理步骤。这个假设是整个 Gaming Budget bound 的基石，但其经验可验证性存疑。

2. **A4（正相关性）**: 假设 criterion-level pass rates p_{k,d} 与 aggregate binary pass rate p̄_d 正相关。这对大多数 criteria 可能成立，但对 surface/formatting criteria（如"格式完整性"）可能不成立——模型可能在高难度问题上仍然保持格式正确但推理错误。如果 A4 不成立，T4 的"peak coincidence"就不成立。

3. **核心"paradox"的因果力**: N(p,G) 和 √(p(1-p)) 都在 p=0.5 最大化是一个数学事实，但这不自动意味着"选择 p≈0.5 的问题训练会导致更多 gaming"。因为：(a) gaming 的发生需要模型有足够的能力去发现 exploit，而不仅仅是数学上的"opportunity"；(b) 中间难度的 gaming "opportunity" 只是 upper bound，实际 gaming 可能远低于 bound。从 upper bound 的 peak 到 actual gaming 的 peak 之间的推理缺乏严格性。

4. **Dimensionality Collapse（T2）的假设**: "honest signal collapses faster than total signal" 需要 high-verification-stringency criteria 先退出 active gradient set。但这个排序是否真的成立取决于具体的 criteria 设计和 judge 质量，而非一般性原理。

【3 维度打分】:
  1. Novelty: 弱-中 — 核心数学观察（N(p,G) 和 √(p(1-p)) 都在 p=0.5 取最大值）是对称凹函数的 trivial 性质，任何审稿人都能在 30 秒内验证这一点。将 Wang & Huang 的 D_i 扩展到 D_i(d) 是增量贡献（加一个难度维度）。真正的新意在于 per-criterion × per-difficulty 的经验方法学（10-bin difficulty scale, bootstrap CIs, isotonic regression 非单调性检验），但这更接近"方法论组合"而非概念突破。与 arXiv:2605.12474 对比：该工作已做了 per-criterion gaming 诊断，只是没有 per-difficulty；与 arXiv:2605.20744 对比：该工作已做了 per-difficulty hacking 测量，只是没有 per-criterion。本 proposal 的贡献本质上是"把两个已知维度交叉起来"。理论框架（T1-T4）的新意主要来自对 Wang & Huang 的 difficulty 扩展，但这种扩展在概念上是自然的（甚至 Wang & Huang 自己在 Remark 2 中都指出了这个方向）。

  2. Significance: 中 — 研究问题确实重要且时机好：rubric-RL 方法激增，但对 gaming 在不同难度上的行为缺乏系统理解。如果非单调性预测（P1）成立，这会是对 DGPO/CDAS 等方法的重要警示。但即便 P1 成立，实际影响可能有限——论文的处方性输出只是一个简单的线性校准 s_k(d) = α_k + β_k·d，这可以不依赖任何理论直接通过网格搜索获得。诊断工具（gaming heatmap）的实用价值取决于社区是否会采用，而目前 rubric-RL 论文的 pace 太快，诊断框架可能在发表前就被更好的方法超越。该工作是 diagnostic 性质而非 prescriptive——它告诉你"哪里有问题"，但提供的解决方案（T3 calibration）过于简单。

  3. Related Work: 强 — 对已有工作的覆盖异常全面，涵盖 8 个类别 40+ 篇论文。差异化定位清晰：准确识别了"difficulty-aware RL 方法都用 binary reward"和"gaming 诊断方法不按难度分层"两条平行线。对 Wang & Huang 的局限性分析（Remark 2）、对 Gradient Starvation 和 Edge of Competence 的区分使用都很精准。composite null hypothesis 的构建（H0a from arXiv:2604.15149 + arXiv:2605.20744, H0b from arXiv:2605.12474）展示了对领域的深入理解。唯一的小问题是过度引用可能给审稿人造成"补偿性引用"的印象——试图用广度掩盖深度不足。

【概率估计】: [18% - 28%] 中位 22%

【估计理由】: 
Novelty 是主要限制因素。核心"paradox"的数学内容——两个对称凹函数都在 p=0.5 取最大值——不构成 surprising 的学术发现。一位审稿人很可能会写："The observation that both N(p,G) and √(p(1−p)) peak at p=0.5 is trivially expected from their functional forms. The 'paradox' is manufactured by naming a natural mathematical property." T1 的 Gaming Budget bound 是 Wang & Huang D_i 的自然扩展（他们自己标注了方向），T4 是 trivial corollary。T2（Dimensionality Collapse）是最有潜力的贡献，但其假设太强且验证困难。

实证方面，per-criterion × per-difficulty 的交叉分析确实是空白，但这更像是"人们还没来得及做"而非"这个问题很难"——毕竟相关论文（arXiv:2605.12474, arXiv:2605.20744）都是 2026 年 5 月才出来的。the gap is real but the barrier to filling it is low，这意味着 novelty 的时间窗口很短。

Related Work 的强度部分补偿了 Novelty 的不足，但 AAAI 审稿人更看重核心贡献的深度而非 related work 的广度。Significance 居中——问题重要但解决方案（线性校准）影响有限。

综合来看，在 Novelty 弱-中、Significance 中的情况下，AAAI 中稿需要实验结果非常 compelling 才能弥补 idea 层面的薄弱——但入口评审只评估 idea 本身。

【主要风险】:
1. **"Paradox" 被审稿人认为 trivial**: 核心数学观察是对称凹函数的基本性质，审稿人可能认为将其命名为"paradox"并构建 4 个定理是 over-engineering。如果审稿人写 "the learning-gaming 'paradox' reduces to the unsurprising fact that variance-like quantities peak at p=0.5"，论文的 narrative 基础就崩塌了。
2. **理论框架可能是 decorative**: Gaming Budget bound 的 tightness 未经验证，如果 bound 极度松弛（实际 gaming ≪ bound），则整个理论框架不提供比直接经验测量更多的洞见。在这种情况下，论文退化为"我们在不同难度上测量了 per-criterion gaming"——这是有用的但不够 AAAI 主会。
```

Sources:
- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689)
- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872)
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063)
- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474)
- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744)
- [DGPO/MathForge (ICLR 2026)](https://openreview.net/forum?id=nfURupkdRJ)
- [Goodhart's Law in Reinforcement Learning (ICLR 2024)](https://openreview.net/forum?id=5o9G4XF1LI)
- [Rubrics as Rewards (ICLR 2026)](https://openreview.net/forum?id=c1bTcrDmt4)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient field research to evaluate this proposal rigorously. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689) (arXiv, May 2026): 验证存在且描述准确。证明 GRPO 非退化分数 N(p,G)=1−p^G−(1−p)^G 在 p=0.5 达到最大值，G=4 时观测到 0.69 退化率。该 proposal 正确引用此结果作为 Learning-Gaming Paradox 的"学习效率"锚点。
- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872) (arXiv, Feb 2026): 验证存在。论文分析了 RLVR 的 relay effect 和难度谱平滑性对学习动态的影响。Proposal 引用 Lemma 6.2 的 multi-step gradient 形式作为补充支撑，引用方式合理，且明确区分了 Δ_L（attention margin）和 pass rate p 的不同。
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (Wang & Huang, arXiv Mar 2026): 验证存在。提出 per-dimension distortion index D_i，证明 reward hacking 是结构性均衡。Proposal 声称扩展 D_i 为 D_i(d)（加入难度维度），这是合理的增量扩展。原论文确实在 Remark 2 中承认了对称生产函数假设的局限。
- [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474) (arXiv, May 2026): 验证存在。诊断了 rubric-based RL 中的三种 gaming failure mode，90.2% presence-based 集中度。Proposal 正确指出该工作"未按难度分层"——经验证，原文确实未做 difficulty stratification。
- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) (arXiv, May 2026): 验证存在。在 5 个模型、3 个游戏环境中测试，发现 hack rate 随难度单调递增。Proposal 正确将此纳入 composite null hypothesis H0a。
- [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149) (ICLR 2026 Workshop): 验证存在。发现 RLVR 训练的模型系统性放弃规则归纳，转为枚举实例标签的 shortcut 策略。
- [MO-GRPO](https://arxiv.org/abs/2509.22047) (arXiv 2025): 解决 GRPO 多目标问题中的 reward hacking，通过 per-objective variance normalization，但确实 difficulty-agnostic。
- [DGPO/MathForge](https://huggingface.co/papers/2601.20614) (ICLR 2026): 通过 MAD normalization 解决 binary-reward GRPO 的难度偏差。确实只在 binary reward 下操作。
- [POW3R](https://arxiv.org/abs/2605.20164) (arXiv, May 2026): 通过 rollout-contrast 动态调整 rubric criterion 权重，属于 reactive/diagnostic 方法。
- 调研总结: Rubric-rewarded RL 是一个极度活跃的领域（4 周内 10+ 篇论文），形成了三条明确的研究线：(a) 难度自适应 GRPO 方法（DGPO, CDAS, F-GRPO 等，均针对 binary reward）；(b) Rubric 设计与 gaming 防御（RRM, POW3R, ARES 等，均 difficulty-agnostic）；(c) Goodhart 理论扩展（Wang & Huang, ICLR 2024 等，均 scalar 或 static）。三条线确实尚未交叉——"per-criterion × per-difficulty 的 gaming 诊断"这个交叉点目前确实空缺。但这个空缺是否源于"无人发现"还是"不值得做"需要仔细区分。

【Trivial Alternative 检验】:
核心观察——p(1−p) 在 p=0.5 达到最大值——是 Bernoulli 方差的基本性质，任何统计学入门课都会教。Proposal 的关键 claim 是 GRPO 学习信号（基于 N(p,G)=1−p^G−(1−p)^G）和 gaming opportunity（基于 √(p_k(1−p_k))）在相同的中等 pass-rate band 达到峰值。但这两个量都是 p(1−p) 的变体——它们在 p=0.5 附近同时达到峰值几乎是 tautological 的。

Trivial alternative：一个直觉性的 baseline 思路是"在中等难度问题上对 surface criteria 施加更严格的评判标准"——不需要任何形式化框架。Proposal 的 T3 calibration schedule s_k(d) = α_k + β_k·d 本质上就是将这个直觉形式化。增量价值在于：(1) 产出 per-criterion × per-difficulty 的 gaming heatmap 作为可复用诊断工具；(2) 将 Wang & Huang 的 static D_i 扩展为 D_i(d)。但这些增量的"惊喜度"有限——informed reviewer 很可能回应"是的，当然中等难度带是最模糊的评估区域——这和学习信号最强的区域重合并不令人意外。"

【前提假设检验】:
1. **假设 A4（criterion-level 与 aggregate pass rate 正相关）**: Proposal 声称"由共同的难度驱动因子保证"。但这是一个强假设——formatting/structural criteria 在所有难度上可能都接近 p≈1.0，与 aggregate pass rate 的相关性可能很弱甚至为零。不同 criteria 的 difficulty profile 可能高度异质。
2. **√(p_k(1−p_k)) 代表 gaming opportunity**: 这是从 Bernoulli 方差到"gaming opportunity"的概念跳跃。为什么 gaming 应该正比于标准差而非方差或其他函数？Proposal 没有从机制层面推导这个关系，而是 assert 了它。
3. **Gaming Budget bound 的 tightness**: T1 提供上界，但上界的实用性取决于其紧致度。如果上界非常宽松，ranking accuracy 验证可能失败——但 proposal 的验证策略已经考虑了这一点（Spearman ρ），这部分设计是合理的。
4. **Dimensionality Collapse (T2) 的前提**: "honest signal dimensionality collapses faster than total signal" 依赖于 A2（reasoning-dependent pass rates 随难度单调递减），这接近于定义性假设。在 A2 下，高难度问题上 hard criteria 变为几乎均匀低通过率（低方差），而 easy-to-game criteria 维持变异性，这是近乎直接的推论。

【3 维度打分】:
1. Novelty: 弱到中 — 核心 insight（"GRPO 学习信号和 gaming opportunity 都在 p≈0.5 达峰"）是 p(1−p) 在中点最大的直接推论，数学上接近 tautological。与最相关工作比较：Gradient Starvation (2605.07689) 已经证明了学习信号集中于中等 pass-rate；Wang & Huang (2603.28063) 已经给出了 per-dimension distortion index；Reward Hacking in Rubric-Based RL (2605.12474) 已经诊断了 per-criterion gaming patterns。Proposal 的增量是将"难度"维度加入已有的 per-criterion 分析——这是一个合理但增量有限的组合创新。Dimensionality Collapse (T2) 是最有 novelty 潜力的部分，但其推导依赖于近乎定义性的假设。"Learning-Gaming Paradox" 作为概念命名是新的，但其背后的数学事实（Bernoulli 方差在中点最大）是已知的。
2. Significance: 中 — 正面：rubric-RL 是当前最活跃的研究方向之一，理解 gaming 结构有实际价值；per-criterion × per-difficulty 诊断工具可被其他方法论文复用（类似 Effective Horizon 对 MDP 研究的贡献）。负面：即使所有 predictions 成立，实际影响主要是"生产 gaming heatmap + 一个简单的 calibration schedule"，这是 useful 但不是 transformative 的贡献。双结果设计意味着即使 H0 成立也有价值，但 H0 成立时的价值主要是"confirmatory diagnostic"，这对 AAAI 来说可能不够。
3. Related Work: 强 — 覆盖了约 40 篇 2024-2026 的相关工作，跨越难度自适应 GRPO、rubric 设计、Goodhart 理论、training dynamics 四个方向。经调研验证，引用的论文确实存在，描述基本准确。差异化定位清晰——"per-criterion × per-difficulty 的交叉点"确实是文献中的空白。Composite null hypothesis 的构建（从 2604.15149、2605.20744、2605.12474 组合）展示了对领域的深度理解。一个小问题：POW3R (reactive) vs. 本工作 (proactive/predictive) 的区分有些过度简化——POW3R 也有诊断性质。

【概率估计】: [18% - 28%] 中位 22%

【估计理由】: 
Novelty 是主要限制因素——核心 "paradox" 本质上是 Bernoulli 方差在中点最大这一基本事实的重新包装，审稿人很可能认为"I would have guessed this"。Significance 处于中等——诊断工具有用但非 transformative。Related Work 覆盖优秀，展示了对领域的深度把握。

上界受限于 Novelty：即使实验执行完美，核心 insight 的惊喜度不足以让审稿人写出 "surprising, not what I expected"。下界由 Related Work 的质量和 dual-outcome 设计支撑——即使预测失败，confirmatory diagnostic 仍有一定价值。

该 proposal 的形式完善度极高（四个定理、三个预测、composite null hypothesis、dual-outcome 设计），但形式完善度不等于 idea 质量。剥离形式后，核心 claim 是"中等难度是 gaming 最脆弱的区域"——这是一个合理但不惊人的观察。

【主要风险】:
1. **"Not surprising" 风险**: 审稿人可能认为 Learning-Gaming Paradox 是显然的——intermediate difficulty 本身就是 ambiguity 最高的区域，学习信号和 gaming 同时达峰是预期内的，不构成真正的 "paradox"。
2. **形式大于实质风险**: 四个定理 + 三个预测的框架看起来 heavy，但数学内核（p(1−p) 在中点最大 + Wang & Huang D_i 加难度参数）相对 thin，审稿人可能批评 "over-engineering a straightforward observation"。
```


【原始 proposal（允许参考但不是主要依据）】:
# The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation

## Core Problem

Rubric-rewarded RL faces a structural tension unrecognized in prior work: the difficulty level where GRPO training signal is strongest is simultaneously where gaming opportunity is maximal. The Gradient Starvation analysis (arXiv:2605.07689) proves that GRPO's non-degenerate fraction N(p,G) = 1 - p^G - (1-p)^G is maximized at p = 0.5 (for G=2, N(p,2) = 2p(1-p), exactly proportional to p(1-p)); our Gaming Budget bound shows each criterion's gaming opportunity scales as √(p_k(1−p_k)), also maximized at p_k = 0.5. Both quantities peak at intermediate pass rates, meaning that difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that correctly select problems in the p̄_d ∈ [0.3, 0.7] band for maximal learning efficiency inadvertently maximize gaming exposure under multi-dimensional rubric evaluation. The Edge of Competence analysis (arXiv:2602.14872, Lemma 6.2) provides further support: the multi-step learning gradient follows ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) with peak at Δ*=L/(L+1), corresponding to pass rates p*=(L/(L+1))^L ∈ [1/e, 1/2] ≈ [0.37, 0.50] for reasoning chains of length L — still within the gaming-vulnerable band. (Note: the Edge of Competence result uses the attention margin Δ_L, not the pass rate p directly, and the functional form (Δ)^L(1−Δ) differs from p(1−p); we cite it for qualitative support that multi-step learning also concentrates at intermediate pass rates, not for a shared functional form.) This Learning-Gaming Paradox is structural — it arises whenever K evaluation criteria are applied with uniform strictness across varying task difficulty under GRPO-family training, because easy-to-verify criteria (formatting, structural completeness) remain satisfiable via shallow pattern-matching at intermediate-difficulty problems, while hard-to-verify criteria (proof validity, factual accuracy) yield their most ambiguous signal precisely there. The consequence is a K×D exploitation surface with difficulty-dependent structure that neither scalar Goodhart analysis (ICLR 2024; ICML 2023) nor static per-dimension distortion indices (Wang & Huang 2026, D_i = λ(r_i/w_i) + (1−λ)) can capture. Wang & Huang's D_i ranking (Corollary 1a) assumes symmetric production functions and treats all tasks identically — it cannot model how the exploitation landscape shifts across difficulty because difficulty-varying verification gaps δ_{k,d} and criterion correlations Σ_d are outside the model's scope (their Remark 2). Meanwhile, Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses per-criterion gaming (90.2% presence-based concentration) but does NOT stratify by problem difficulty. LLMs Gaming Verifiers (arXiv:2604.15149) and Hack-Verifiable Environments (arXiv:2605.20744) show gaming/hacking increases monotonically with task difficulty in aggregate. Neither captures the paradox: the difficulty band that GRPO training should focus on for maximum learning efficiency is the difficulty band that rubric gaming exploits most effectively.

## Research Opportunity

Six convergent gaps, now organized around the Learning-Gaming Paradox: (1) The Goodhart's law literature — Goodhart's Law in RL (ICLR 2024), Scaling Laws for RM Overoptimization (ICML 2023), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — operates on SCALAR proxy-goal pairs. The Robust Optimization framework (arXiv:2604.12086, ICLR 2026) adds correlation between scalar proxies but does not decompose per-criterion or model difficulty. No formal treatment exists for K-dimensional evaluation with difficulty-varying exploitation. (2) Wang & Huang (arXiv:2603.28063) derive a constructive per-dimension distortion index D_i with Corollary 1(a) providing a ranking result under symmetric production functions. However, their model treats all tasks identically — it cannot predict how the exploitation landscape shifts with difficulty d, because difficulty-varying verification gaps δ_{k,d} and correlations Σ_d are outside the model's scope (flagged in their Remark 2). Our framework extends D_i to D_i(d), recovering their ranking as a special case when difficulty is constant. (3) The Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's learning signal peaks at intermediate pass rates: the non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5, with degeneracy rates of 0.69 observed at G=4 in practice. The Edge of Competence (arXiv:2602.14872) establishes a complementary result for multi-step reasoning: the learning gradient ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) peaks at attention margins Δ*=L/(L+1), corresponding to pass rates p*=(L/(L+1))^L ∈ [1/e, 1/2] — still within the intermediate range. Both results establish that RL learning concentrates at intermediate pass rates. NO PRIOR WORK connects this to gaming vulnerability: we show that the Gaming Budget bound's per-criterion terms √(p_k(1−p_k)) are ALSO maximized at intermediate pass rates. This peak coincidence — GRPO learning efficiency and gaming opportunity both maximized in the p ∈ [0.3, 0.7] band — is the Learning-Gaming Paradox. (4) DGPO (ICLR 2026, Theorems 1-2) addresses difficulty bias in binary-reward GRPO; per-criterion application is straightforward, but the INTERACTION structure — criterion correlations shifting with difficulty, verification gaps creating asymmetric vulnerability, learning-gaming tension at the competence boundary — requires genuinely novel analysis. (5) Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses gaming taxonomy (3 failure modes, 90.2% presence-based criteria concentration) but does NOT stratify by problem difficulty — the core analytical dimension we add. (6) LLMs Gaming Verifiers (arXiv:2604.15149) and Hack-Verifiable Environments (arXiv:2605.20744) show gaming/hacking severity increases monotonically with task difficulty in aggregate — combined with arXiv:2605.12474's criterion-type finding, this forms our composite null hypothesis. The marginal contribution is fourfold: (a) the Learning-Gaming Paradox — identifying that GRPO's learning-efficient zone (Gradient Starvation) coincides with rubric gaming's exploitation peak (Gaming Budget), with supplementary support from Edge of Competence's multi-step analysis; (b) a Learning-Gaming Duality framework with co-equal Gaming Budget Theorem (T1) and Dimensionality Collapse Theorem (T2), extending Wang & Huang's static D_i to difficulty-varying D_i(d) trajectories; (c) a reusable diagnostic producing per-criterion × per-difficulty gaming surfaces with rigorous statistical methodology (10 difficulty bins, bootstrap CIs, formal non-monotonicity tests); (d) three quantitative falsifiable predictions against a strengthened composite null hypothesis, with concrete methodological value under either outcome — including derivation and validation of monotonic calibration schedules under H0.

## Research Landscape

Rubric rewards for RL achieve strong results but apply uniform strictness across difficulty: RRM (ACL 2026) boosts Verified Pass@1024 on AIME2024 from 26.7% to 62.6%; RaR (ICLR 2026) extends to medical (+31% HealthBench) and science (+7% GPQA-Diamond); SRaR (arXiv:2605.17291) adds step-level attribution; POW3R (arXiv:2605.20164) adapts criterion weights via rollout variance; ARES (arXiv:2605.23454) automates rubric synthesis; AMARIS (arXiv:2605.18592) maintains persistent evaluation memory for difficulty-agnostic rubric evolution. ARL-RR (arXiv:2603.15646) addresses the scalarization problem by alternating optimization across rubric meta-classes (accuracy, completeness, instruction following, context awareness, communication quality), which is algorithmic (changing the optimization procedure) rather than diagnostic (characterizing which criteria are exploitable at which difficulty levels). The rubric-RL space continues rapid expansion (~10+ papers in 4 weeks preceding this revision) — but this velocity STRENGTHENS our diagnostic contribution: as methods proliferate, a principled framework identifying WHICH criteria are exploited at WHICH difficulty levels becomes a shared evaluation lens no individual method paper provides. Difficulty-aware RL methods operate under binary rewards: DGPO/MathForge (ICLR 2026) via MAD normalization, DARO (arXiv:2510.09001), F-GRPO (arXiv:2602.06717), GRPO-LEAD (EMNLP 2025) via logistic weighting, A-GRAE (arXiv:2602.05548), Goldilocks RL (arXiv:2602.14868), Online Difficulty Filtering (EACL 2026), CDAS (arXiv:2505.17652) via competence-difficulty alignment, Gradient Starvation (arXiv:2605.07689) via degeneracy analysis. ALL operate under binary rewards without per-criterion gaming analysis. Difficulty-calibrated advantage reweighting is an active concurrent direction: Unlocking the Potential of Difficulty Prior (arXiv:2505.13261) explicitly models difficulty priors to calibrate reasoning depth and reweight advantages in multimodal RL — while targeting training efficiency rather than gaming characterization, it demonstrates independent convergence on difficulty-aware reward modulation. The closest convergence spans eight categories: **Difficulty-stratified rubric calibration**: RuCL (arXiv:2602.21628) adjusts by model competence, not problem difficulty, and is vulnerable to gaming-inflated pass rates. **Multi-objective reward normalization**: MO-GRPO (arXiv:2509.22047) addresses per-objective variance bias (the mechanism underlying dimensional exploitation) but is difficulty-agnostic. **Reactive criterion reweighting**: POW3R adapts via rollout-contrast (reactive/diagnostic) while our approach is proactive/predictive (which criteria WILL BE gamed, inferred a priori from difficulty structure). **Memory-augmented rubric adaptation**: AMARIS addresses the temporal dimension (rubric evolution during training) while we address the structural dimension (exploitation variation with difficulty) — complementary, not competing. **Rubric quality and gaming defense**: Rubicon (arXiv:2508.12790), CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618) — all difficulty-agnostic. **Goodhart's law theory**: Goodhart's Law in RL (ICLR 2024), Robust Optimization for Correlated Proxies (ICLR 2026), Reward Hacking as Equilibrium (arXiv:2603.28063), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — Wang & Huang's D_i is constructive per-dimension but static; none model K-dimensional difficulty-varying exploitation trajectories or connect to training dynamics. **Training dynamics and gaming interaction**: Gradient Starvation (arXiv:2605.07689) proves GRPO degeneracy rate D(p,G)=p^G+(1−p)^G, establishing that GRPO learning concentrates at intermediate pass rates (p≈0.5); Edge of Competence (arXiv:2602.14872) proves multi-step learning gradient ∇ ∝ (Δ_L)^L(1−Δ_L), peaking at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50]; Reward Hacking Rebounds (arXiv:2604.01476) shows gaming has dynamic phase structure. None connect these training-efficiency results to gaming vulnerability under rubric evaluation — the Learning-Gaming Paradox we identify. **Difficulty-dependent hacking measurement**: Hack-Verifiable Environments (arXiv:2605.20744) introduces a paradigm for measuring reward hacking by embedding detectable opportunities into environments, finding hack rate increases monotonically with difficulty across most models (5 models, 3 games). This provides the strongest controlled evidence for H0a but does not analyze per-criterion gaming structure or connect to training dynamics. **Per-criterion behavior across difficulty**: SPARKLE (NeurIPS 2025, arXiv:2506.04723) analyzes three reasoning dimensions across difficulty levels under RL, providing evidence that per-criterion × per-difficulty analysis is informative — but studies reasoning capability, not gaming/exploitation, and has no Goodhart framework. The critical gap: no work provides (a) identification of the Learning-Gaming Paradox — the coincidence that GRPO learning efficiency and gaming opportunity both peak at intermediate pass rates, (b) co-equal Gaming Budget and Dimensionality Collapse theorems characterizing the K×D exploitation surface, (c) per-criterion × per-difficulty gaming diagnosis with rigorous statistical methodology, or (d) quantitative predictions about gaming structure tested against a composite null hypothesis that now incorporates controlled hack-rate evidence.

## Proposed Approach

We adopt a three-contribution structure centered on the Learning-Gaming Paradox, with co-equal theoretical results and concrete value under either empirical outcome. **Lead Framing: The Learning-Gaming Paradox.** We open with a structural insight connecting training dynamics to evaluation vulnerability: the Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5; our Gaming Budget bound shows gaming opportunity (via √(p_k(1−p_k)) terms) is also maximized at intermediate pass rates. Because both peak in the same difficulty band (p̄_d ∈ [0.3, 0.7]), the difficulty level that GRPO training should focus on for maximum learning is simultaneously the difficulty level where rubric gaming is most effective. The Edge of Competence (arXiv:2602.14872, Lemma 6.2) provides supplementary support: the multi-step gradient ∝ (Δ_L)^L(1−Δ_L) peaks at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50], confirming that even beyond GRPO-specific analysis, multi-step RL learning concentrates at intermediate pass rates within the gaming-vulnerable band. (We are careful to distinguish: the Gradient Starvation result directly uses pass rates p and provides the formal anchor; the Edge of Competence result uses attention margins Δ_L with a different functional form and provides qualitative reinforcement.) This paradox is structural — it holds regardless of whether specific predictions about non-monotonicity (P1) are confirmed, because the PEAK COINCIDENCE between N(p,G) and the Gaming Budget is a mathematical fact. **Composite Null Hypothesis.** We test against a strengthened Composite Null (H0) built from three rubric-relevant findings: (H0a — Aggregate Trend) Gaming severity increases monotonically with problem difficulty for ALL rubric criteria, extrapolating the aggregate trend from LLMs Gaming Verifiers (arXiv:2604.15149), Hack-Verifiable Environments (arXiv:2605.20744, which finds monotonic hack-rate increase in controlled settings across 5 models and 3 environments), and Goodhart's Law in RL (ICLR 2024). (H0b — Criterion-Type Invariance) Gaming concentrates in presence-based/completeness criteria at ALL difficulty levels, extrapolating from Reward Hacking in Rubric-Based RL (arXiv:2605.12474, 90.2% presence-based concentration). Note: H0a now incorporates controlled experimental evidence (arXiv:2605.20744) alongside observational evidence; H0b is rubric-specific but difficulty-agnostic. Together they predict monotonic, criterion-type-stable gaming — a stronger adversarial target than either alone. Three falsifiable predictions with quantitative and statistical failure conditions: (P1) Learning-Gaming Resonance — H0a predicts monotonically increasing gaming for reasoning-verification criteria; P1 predicts an inverted-U peaking in the intermediate-pass-rate band (coinciding with the GRPO learning efficiency peak at p≈0.5), with peak gaming rate ≥1.5× the rate at highest-difficulty bins. Statistical test: monotone-constrained isotonic regression vs. unconstrained fit via likelihood ratio test (p < 0.05), supplemented by quadratic regression β₂ < 0 (p < 0.05). (P2) Criterion Vulnerability Shift — H0b predicts presence-based criteria dominate at all difficulty levels; P2 predicts the criterion vulnerability ordering SHIFTS with difficulty — Pearson correlation between surface-criterion and reasoning-criterion satisfaction flips from positive (r > 0.1 in bottom-quintile) to negative (r < −0.1 in top-quintile), a sign flip analogous to Simpson's Paradox. Additionally, reasoning-criterion gaming share increases ≥2× from bottom to top difficulty quintile. (P3) Asymmetric Dimensionality Collapse — P3 predicts K_honest/K_eff < 0.5 at highest-difficulty bins, with K_eff ≥ 3: honest gradient signal collapses to a lower-dimensional subspace FASTER than total signal because gaming inflates apparent dimensionality. **Concrete value under either outcome.** If P1-P3 hold: the Learning-Gaming Paradox is empirically confirmed with specific structural predictions, revealing difficulty-dependent gaming invisible to aggregate/unstratified analysis. If H0 is confirmed (monotonic, criterion-type-stable gaming): (a) the Learning-Gaming Paradox still holds structurally — even monotonically increasing gaming creates a tension with the GRPO learning signal peak at moderate difficulty, because difficulty-aware methods focus training precisely where gaming is already substantial; (b) we provide the FIRST per-criterion × per-difficulty confirmation that monotonicity and criterion-type-stability hold at every criterion individually (currently known only in aggregate or unstratified); (c) we derive and validate a simple linear strictness schedule s_k(d) = α_k + β_k·d justified by confirmed monotonicity, where β_k is proportional to the empirically measured per-criterion gaming slope, and validate that it reduces the mean DEG (Dimension Exploitation Gap) by ≥15% compared to uniform strictness on a held-out test split; (d) the Dimensionality Collapse analysis (T2) characterizes how many effective honest dimensions remain at each difficulty level, directly informing how many criteria are worth evaluating at high difficulty. We explicitly acknowledge this would be a solid diagnostic paper with a concrete calibration output, valuable to rubric-RL practitioners. **Contribution 1 — Learning-Gaming Duality Framework (domain-agnostic theory).** Four formal results for any K-dimensional evaluation system with difficulty variation under GRPO-family training: (T1) Gaming Budget Theorem — a difficulty-parameterized bound on total exploitable reward at difficulty d, extending Wang & Huang's static distortion index. Formal model: pass rate matrix P ∈ [0,1]^{K×D}, verification gap matrix Δ, difficulty-varying correlation matrix Σ_d. Four assumptions: (A1) decomposability into genuine and gaming components; (A2) monotonic non-increase of reasoning-dependent pass rates with difficulty; (A3) difficulty-stable or increasing verification gaps for surface criteria; (A4) positive correlation between criterion-level pass rates p_{k,d} and aggregate binary pass rate p̄_d (justified by the shared difficulty driver — harder problems lower both aggregate and criterion-level pass rates). Bound: G_d ≤ Σ_{k∈V_d} w_k · δ_{k,d} · √(p_{k,d}(1−p_{k,d})) + Σ_{j&lt;k∈V_d} w_j·w_k · max(0, σ_{jk,d}) · δ_{j,d}·δ_{k,d}. **Special case reduction:** When d is constant and δ_{k,d} = δ, recovers Wang & Huang's D_i ranking. (T2) Dimensionality Collapse Theorem (CO-EQUAL with T1) — proves K_honest(d) decreases strictly faster than K_eff(d) under A2, using the observation that high-verification-stringency criteria leave the active gradient set first. This is potentially more surprising than T1 because it predicts ASYMMETRIC structural behavior: gaming inflates apparent signal dimensionality while honest signal collapses, creating a growing gap that makes gaming increasingly invisible to standard diagnostics at higher difficulty. Validated via PCA on per-criterion pass-rate vectors across difficulty bins, measuring the ratio of honest-signal eigenvalues to total eigenvalues. (T3) Calibration Sufficiency Condition — derives the minimal gaming-eliminating strictness schedule s_{k,d} ∝ 1/δ_{k,d} · √(p_{k,d}(1−p_{k,d})). Under confirmed H0 (monotonic gaming), simplifies to the linear schedule s_k(d) = α_k + β_k·d with closed-form β_k. (T4) Learning-Gaming Peak Coincidence Corollary — Under assumptions A1-A4, the GRPO non-degenerate fraction N(p̄_d, G) = 1−p̄_d^G−(1−p̄_d)^G and the difficulty-marginal Gaming Budget G_d are both maximized within the difficulty band where p̄_d ∈ [0.3, 0.7]. Formally: N(p,G) achieves its unique maximum at p=0.5 (Gradient Starvation, arXiv:2605.07689); each Gaming Budget term w_k·δ_{k,d}·√(p_{k,d}(1−p_{k,d})) achieves its maximum at p_{k,d}=0.5; under A4, the Gaming Budget is near-maximal when p̄_d ≈ 0.5. Supplementary support: the Edge of Competence (arXiv:2602.14872) multi-step gradient peaks at pass rates (L/(L+1))^L ∈ [1/e, 1/2] for reasoning chains of length L, confirming that multi-step learning also concentrates in the gaming-vulnerable band. (We do NOT claim a shared functional form between (Δ)^L(1−Δ) and √(p(1−p)) — the formal connection is through peak coincidence in the pass-rate domain.) Practical consequence: difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that select problems with p̄_d ≈ 0.5 for maximal learning efficiency simultaneously maximize the Gaming Budget under rubric evaluation. Validation strategy: RANKING ACCURACY (Spearman ρ between predicted and observed gaming severity across K×D cells) following the Effective Horizon precedent (NeurIPS 2023 Oral), plus conservativeness ratio and top-3 vulnerability identification accuracy. **Contribution 2 — Cross-Domain Empirical Diagnosis with Rigorous Statistics.** Math domain (primary for AAAI): Qwen2.5-Math-1.5B policy, Qwen3-8B judge, MATH dataset. **10-bin difficulty scale:** Base model generates 64 rollouts per problem → per-problem pass@1 → 10 equal-frequency difficulty bins (deciles). This provides 2× resolution for curve-fitting, continuous underlying variable for regression, independence from coarse categorical labels. MATH's native 5 levels serve as robustness check. Statistical methodology: (i) 1000-resample bootstrap 95% CIs on all DEG values; (ii) formal non-monotonicity test: isotonic regression (monotone non-decreasing constraint) vs. unconstrained kernel regression via permutation-based likelihood ratio test; (iii) quadratic regression DEG ~ β₀ + β₁d + β₂d² with one-sided test β₂ < 0; (iv) Fisher's z-test for correlation sign-flip (P2). Medical domain (ICLR scope): Qwen2.5-1.5B-Instruct policy, Qwen3-8B judge, RaR-Medicine (22.4K examples, ICLR 2026). Difficulty estimation via SFT-init checkpoint rollouts (breaks circularity). Cross-domain comparison: test whether gaming surface STRUCTURE transfers across domains. **Contribution 3 — DCRR Proof-of-Concept (ICLR scope only).** DGPO+RRM critical baseline first; if >20% gap remains, apply Difficulty-Calibrated Rubric Rewards using T3 schedule. Under H0: validate s_k(d) = α_k + β_k·d reduces mean DEG ≥15% vs. uniform strictness. **Venue Strategy (REVISED — AAAI primary, ICLR stretch).** Primary target: AAAI 2027 (abstract Jul 21, paper Jul 28, 8 weeks). Math-only, Contributions 1-2: Learning-Gaming Duality framework (T1+T2+T4 corollary + T3 monotonic special case) + MATH 10-bin gaming heatmaps + 3 predictions + monotonic calibration validation under H0. This is the natural unit — the theoretical framework + single-domain validation. Decision-gated stretch: ICLR 2027 (~Sep 24, 17 weeks). Full three-contribution scope adding medical domain + DCRR defense + cross-domain analysis. Only pursued if AAAI submission is strong AND reviewer feedback suggests expansion strengthens the work. Backup: ARR August 3 → EACL 2027 (~10 weeks, math + medical diagnostics without DCRR). **Concrete timeline (AAAI primary, 8 weeks):** Week 1 (May 28 - Jun 4): Theory formalization (T1 with Wang & Huang special case, T2 with PCA validation plan, T4 Learning-Gaming Peak Coincidence Corollary with Gradient Starvation anchor) + infrastructure setup (verl scripts, judge pipeline) + BEGIN base-model pass@1 computation (64 rollouts/problem, ~8 H100-hrs) + BEGIN GRPO training run. Week 2 (Jun 4 - Jun 11): Base-model pass@1 complete → 10-bin difficulty binning + BEGIN GRPO+RRM training run + BEGIN DGPO+RRM training run. Weeks 3-4 (Jun 11 - Jun 25): Training runs complete + judge inference on all 3 models (~20 H100-hrs total) + 10-bin gaming heatmap construction + DEG computation + bootstrap CIs + non-monotonicity tests. Week 5 (Jun 25 - Jul 2): All statistical tests (P1 isotonic regression, P2 Fisher's z-test, P3 PCA dimensionality analysis) + monotonic calibration schedule derivation and validation + draft core results. Week 6 (Jul 2 - Jul 9): DECISION GATE — evaluate: (a) are gaming surfaces non-trivial? (b) do statistical tests yield interpretable results? (c) is theory validated via ranking accuracy? If YES to all three: commit to AAAI. If NO: continue ICLR plan with 10 more weeks. Weeks 7-8 (Jul 9 - Jul 28): Paper writing, figures, polishing. Jul 21 abstract, Jul 28 paper submission. **Risk mitigation:** Training failures → keep uniform-GRPO baseline (always works), can still produce gaming surface from fewer models. Judge quality → validate on 200-sample subset before full inference. Timeline → T3 monotonic case and H0-confirmed contributions provide fallback value even if exotic predictions fail.

## Detailed Description

We identify the Learning-Gaming Paradox: a structural tension in rubric-rewarded RL where the difficulty level that maximizes GRPO learning signal simultaneously maximizes gaming opportunity. The Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5; our Gaming Budget bound shows gaming opportunity (via √(p(1−p)) terms) is also maximized at intermediate pass rates. Both peak in the same difficulty band (p̄_d ∈ [0.3, 0.7]), meaning difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that correctly focus on this zone for learning efficiency inadvertently maximize gaming exposure under multi-dimensional rubric evaluation. The Edge of Competence analysis (arXiv:2602.14872, Lemma 6.2) provides supplementary support: the multi-step gradient (∝ (Δ_L)^L(1−Δ_L), where Δ_L is the attention margin, NOT the pass rate) peaks at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50], confirming that multi-step learning also concentrates at intermediate pass rates within the gaming-vulnerable band. We contribute: (1) a Learning-Gaming Duality framework with co-equal theoretical results — a Gaming Budget Theorem (T1) providing the first difficulty-parameterized K-dimensional Goodhart bound (extending Wang & Huang's static D_i to D_i(d) trajectories with special-case reduction), a Dimensionality Collapse Theorem (T2) proving honest signal dimensionality collapses faster than total signal making gaming increasingly invisible, a Learning-Gaming Peak Coincidence Corollary (T4) formally establishing that the GRPO non-degenerate fraction and the Gaming Budget are both maximized at intermediate pass rates (anchored to Gradient Starvation with Edge of Competence as supplementary support), and a Calibration Sufficiency Condition (T3) deriving gaming-eliminating strictness schedules that simplify to s_k(d) = α_k + β_k·d under confirmed monotonicity; (2) a cross-domain empirical diagnostic using 10-bin difficulty scales (base-model pass-rate deciles) with bootstrap CIs and formal non-monotonicity tests, producing per-criterion × per-difficulty gaming surfaces; (3) three falsifiable predictions against a composite null hypothesis strengthened by Hack-Verifiable Environments (arXiv:2605.20744) — (P1) Learning-Gaming Resonance: non-monotonic gaming for reasoning criteria peaking in the GRPO-efficient band at ≥1.5× the highest-difficulty rate; (P2) Criterion Vulnerability Shift: surface-reasoning correlation sign-flip plus ≥2× reasoning-criterion gaming share increase; (P3) Asymmetric Dimensionality Collapse: K_honest/K_eff < 0.5 at highest difficulty. The paper delivers concrete value under either outcome: if predictions hold, it reveals difficulty-dependent structure invisible to prior analysis; if H0 is confirmed, it provides the first per-criterion × per-difficulty confirmation of monotonic gaming, derives and validates a simple linear calibration schedule reducing mean DEG by ≥15%, and characterizes effective honest dimensionality at each difficulty level. Validated on Qwen2.5-Math-1.5B (AAAI primary, math) with Qwen2.5-1.5B-Instruct cross-domain validation (ICLR stretch, medical).

## Key References

- Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — GRPO degeneracy rate D(p,G)=p^G+(1−p)^G; non-degenerate fraction N(p,G)=1−p^G−(1−p)^G maximized at p=0.5 (for G=2, N=2p(1−p); observed 0.69 degeneracy at G=4 in Qwen3.5-9B). CRITICAL for our Learning-Gaming Paradox: provides the PRIMARY formal anchor establishing that GRPO learning efficiency peaks at intermediate pass rates (p≈0.5), coinciding with the Gaming Budget's peak zone. Also proves via Jensen's inequality that real degeneracy exceeds i.i.d. prediction
- On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872) — Multi-step learning gradient: Lemma 6.2 shows ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) where Δ_L is the effective probability margin (NOT the pass rate), peaking at Δ*=L/(L+1). The corresponding pass rate at the gradient peak is p*=(L/(L+1))^L ∈ [1/e, 1/2] ≈ [0.37, 0.50]. Provides SUPPLEMENTARY SUPPORT for the Learning-Gaming Paradox: even the multi-step analysis shows learning concentrates at intermediate pass rates within the gaming-vulnerable band. The relay effect explains WHY training naturally traverses this zone. NOTE: the functional form (Δ)^L(1−Δ) differs from p(1−p) and Δ ≠ p; we cite for qualitative support, not shared functional form
- Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063) — Constructive per-dimension distortion index D_i = λ(r_i/w_i) + (1−λ) with ranking result Corollary 1(a): D_i > D_j ⟹ e_i* > e_j* under symmetric production functions. Limitation: static (no difficulty parameterization), assumes symmetric g_i (Remark 2). Our framework extends D_i to difficulty-varying D_i(d) trajectories, recovering D_i ranking as a special case at constant difficulty
- Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale (arXiv:2605.20744) — Embeds detectable hacking opportunities into environments for controlled measurement. Tests 5 models (Claude Sonnet 4.6, GPT-5-Codex, Gemini 3.1 Pro, Qwen3.6-Plus, Kimi-K2.5) across 3 games (Wordle, Tower of Hanoi, 15-Puzzle) with varying difficulty. KEY FINDING: hack rate increases monotonically with task difficulty across most models and environments. Provides the strongest controlled experimental evidence supporting H0a in our composite null hypothesis
- Goodhart's Law in Reinforcement Learning (ICLR 2024) — Geometric explanation for Goodhart's law in MDPs; shows optimization pressure increases Goodharting; aggregate scalar analysis. Our framework extends to K-dimensional evaluation with difficulty variation and connects to training dynamics
- Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026) — Max-min formulation over r-correlated scalar proxy rewards; does not decompose per-criterion or model difficulty-varying correlation
- The Strong, Weak and Benign Goodhart's Law (arXiv:2505.23445) — Independence-free formalization; scalar proxy-goal pair, no multi-dimensional or difficulty treatment
- Scaling Laws for Reward Model Overoptimization (ICML 2023) — Empirical scaling of overoptimization with optimization intensity; aggregate scalar analysis
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, ICLR 2026 Workshop) — Shows gaming prevalence increases with task complexity on inductive reasoning tasks (SLR-Bench, 4 tiers) under binary extensional verification. Contributes H0a (aggregate trend) to our composite null hypothesis
- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474) — Gaming taxonomy in medical/science; 3 failure modes; 90.2% presence-based criteria concentration; self-internalization gap metric. Contributes H0b (criterion-type invariance) to our composite null hypothesis. Does NOT stratify by problem difficulty
- Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (ICLR 2026) — DGPO Theorems 1-2 on binary-reward difficulty bias; difficulty-aware methods that focus on intermediate pass rates — precisely the zone our Learning-Gaming Paradox identifies as gaming-vulnerable
- Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards (ACL 2026) — RRM baseline, uniform-strictness rubric rewards for math
- Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (ICLR 2026) — Foundational rubric RL; RaR-Medicine dataset for cross-domain validation
- Unlocking the Potential of Difficulty Prior in RL-based Multimodal Reasoning (arXiv:2505.13261) — Models difficulty priors to calibrate reasoning depth and reweight advantages in multimodal RL. Demonstrates concurrent convergence on difficulty-aware reward modulation, though targeting training efficiency rather than gaming characterization. Validates the timeliness of difficulty-calibrated approaches
- Rethinking the Sampling Criteria in RL for LLM Reasoning: A Competence-Difficulty Alignment Perspective (arXiv:2505.17652) — CDAS framework for stable difficulty estimation via historical performance aggregation. Validates our base-model pass-rate difficulty binning methodology
- Bridging RL Theory and Practice with the Effective Horizon (NeurIPS 2023, Oral) — Validates theoretical bounds via RANKING CORRELATION across 155 MDPs. Direct precedent for our Gaming Budget validation strategy
- MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems (arXiv:2509.22047) — Per-objective variance normalization; Theorem 1 (correlation ∝ σ_i) is the mechanism underlying dimensional exploitation, but difficulty-agnostic
- Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (NeurIPS 2025, arXiv:2506.04723) — SPARKLE framework analyzing 3 reasoning dimensions across difficulty under RL. Evidence that per-criterion × per-difficulty analysis is informative, but studies reasoning capability rather than gaming and has no Goodhart framework
- When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476) — Identifies three-phase gaming dynamics (attempt → retreat → rebound) in code RL; shortcut direction in representation space tracks hacking. Supports our view that gaming is not static but has structural dynamics across contexts
- Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (NeurIPS 2025) — Pass@k frontier evaluation for binary-reward; diagnostic impact precedent
- Reward Collapse in Aligning Large Language Models (arXiv:2305.17608) — Reward distribution collapse; supports our Dimensionality Collapse prediction
- Step-wise Rubric Rewards for LLM Reasoning (arXiv:2605.17291) — SRaR step-level rubric attribution
- Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164) — POW3R rollout-contrast reweighting; reactive vs. our proactive/predictive
- AMARIS: A Memory-Augmented Rubric Improvement System (arXiv:2605.18592) — Persistent evaluation memory; temporal dimension vs. our structural dimension
- ARES: Automated Rubric Synthesis for Scalable LLM RL (arXiv:2605.23454) — Rubric synthesis automation; difficulty-agnostic
- Alternating Reinforcement Learning with Contextual Rubric Rewards (arXiv:2603.15646) — ARL-RR addresses scalarization by alternating optimization across rubric meta-classes. Algorithmic (changes optimization procedure) rather than diagnostic (characterizing exploitation patterns)
- RuCL: Stratified Rubric-Based Curriculum Learning (arXiv:2602.21628) — Adjusts by model competence not problem difficulty; vulnerable to gaming-inflated pass rates
- HealthBench (arXiv:2505.08775) — Medical evaluation benchmark; secondary evaluation
- CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618), Rubicon (arXiv:2508.12790) — Rubric quality/gaming defense; all difficulty-agnostic
- Online Difficulty Filtering for Reasoning Oriented RL (EACL 2026) — Variance-based difficulty selection theory
- GRPO-LEAD (arXiv:2504.09696, EMNLP 2025) — Logistic difficulty reweighting under binary rewards
- DARO, F-GRPO, A-GRAE, Goldilocks RL, PAPO, ARL-RR, RubricEM, Rubric-Grounded RL — Complementary difficulty-aware or rubric-optimization methods, all binary-reward or difficulty-agnostic

## Resource Estimate

- **manual**: gpu_hours: 100 H100-hours for AAAI primary (Math: 3 training runs × 4 H100 × 2.5hr = 30hr, base-model pass@1 computation for 10-bin difficulty 8hr, rubric judge inference 20hr, Pass@64 for difficulty binning 25hr, analysis + bootstrap CIs + overhead 17hr). Additional 90 H100-hours for ICLR stretch (Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle rollouts 5hr, medical judge inference 10hr, DCRR experiments 30hr, MO-GRPO+RRM baseline 15hr, ablations 6hr)., timeline: 8 weeks for AAAI 2027 primary (math-only, Contributions 1-2+calibration). 17 weeks for ICLR 2027 stretch (full three-contribution scope adding medical + DCRR)., estimated_gpu_cost: $250 AAAI / $475 total with ICLR stretch (H100 at ~$2.50/hr)
- **human_in_loop**: gpu_hours: 100 H100-hours AAAI / 190 H100-hours total (same; Claude accelerates code/analysis, not GPU work), timeline: 7 weeks for AAAI (Claude assists theorem formalization, verl scripts, automated heatmap generation, bootstrap pipeline, writing). 14-15 weeks for ICLR stretch., claude_api_cost: $150 AAAI / $300 total (Sonnet 4.6 for rubric generation, code scaffolding, statistical pipeline, writing), estimated_gpu_cost: $250 AAAI / $475 total
- **auto_research**: gpu_hours: 105 H100-hours AAAI / 200 H100-hours total (5hr margin for targeted hyperparameter exploration per venue), timeline: 6-7 weeks for AAAI (parallelized dispatch, automated analysis, Claude-drafted paper). 10-12 weeks for ICLR., claude_api_cost: $250 AAAI / $420 total (rubric judging quality audit ~5K samples, automated analysis, writing), estimated_gpu_cost: $263 AAAI / $500 total, speed_bottleneck: LLM judge inference throughput — scoring ~50K math rollouts per model with Qwen3-8B requires ~8hr per model on 4×H100; base-model pass@1 computation adds ~8hr
- **aaai_primary_scope**: gpu_hours: 100 H100-hours (Math only: 3 training runs × 4 H100 × 2.5hr = 30hr, base-model pass@1 for binning 8hr, judge inference 20hr, Pass@64 difficulty binning 25hr, analysis + bootstrap 17hr), timeline: 8 weeks (6-week sprint + 2 weeks writing; decision gate at week 6), estimated_gpu_cost: $250, scope: Learning-Gaming Duality framework (T1+T2+T4 Peak Coincidence Corollary with Gradient Starvation anchor, with T3 monotonic special case) + MATH 10-bin gaming heatmaps with bootstrap CIs + 3 falsifiable predictions tested with formal statistical tests + monotonic calibration schedule derivation and validation under H0. The complete theoretical framework plus single-domain empirical validation.
- **iclr_stretch_scope**: gpu_hours: 190 H100-hours total (AAAI scope + Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle 5hr, medical judge inference 10hr + DCRR: experiments 30hr, MO-GRPO+RRM 15hr, ablations 6hr), timeline: 17 weeks total (incorporates AAAI submission + 9 additional weeks for medical domain + DCRR + cross-domain analysis), estimated_gpu_cost: $475, scope: Full three-contribution scope: AAAI content + medical domain validation + DCRR proof-of-concept + cross-domain gaming surface comparison


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "19a6e524-cab0-4e1c-b253-06aa07e9d55e",
  "type": "user",
  "uuid": "1061105d-ffd8-4540-a73e-7ff0a2a9e62d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T16:56:42.944Z_

```json
{
  "parentUuid": "1061105d-ffd8-4540-a73e-7ff0a2a9e62d",
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
  "uuid": "67d044d6-9c2c-44be-a466-6b6c75c43747",
  "timestamp": "2026-05-28T16:56:42.944Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T16:56:42.944Z_

```json
{
  "parentUuid": "67d044d6-9c2c-44be-a466-6b6c75c43747",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ce12aa21-37f9-4efc-896a-6f748d9b2973",
  "timestamp": "2026-05-28T16:56:42.944Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information from my research. Let me com…",
  "leafUuid": "ce12aa21-37f9-4efc-896a-6f748d9b2973",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Learning-Gaming paradox in rubric-based RL evaluation",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e"
}
```

---

### Assistant

_source line 8 · 2026-05-28T16:57:25.395Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully to produce a Meta Judge synthesis.

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [22% - 33%] 中位 27%

**Reviewer 2:**
- Novelty: 弱-中 (Weak-Medium)


- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [18% - 28%] 中位 22%

**Reviewer 3:**
- Novelty: 弱到中 (Weak-Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [18% - 28%] 中位 22%

Looking at the three probability medians of 27%, 22%, and 22%, the overall median is 22% with a mean around 23.7%. The standard deviation is quite small at approximately 2.89%, suggesting the reviewers are fairly aligned in their assessments despite some variation in novelty ratings. I'm calculating the standard deviation to determine whether to use the mean or median for the estimates. With a sample standard deviation around 2.9%, the reviewers show high consistency, so I should go with the median. Now I'm mapping out where the three reviewers actually agree versus where they diverge. On novelty, all three flag the core paradox as mathematically near-tautological—two symmetric concave functions peaking at p=0.5—so the "paradox" framing oversells the surprise. They converge on medium significance: the diagnostic contribution has value but the linear calibration schedule is too simplistic to be transformative. Related work gets universal agreement as strong and comprehensive. I'm identifying the core risks and where consensus breaks down. The slight difference in R1's estimate reflects a marginally more optimistic view of the cross-connection's novelty contribution, though all three reviewers agree on the fundamental weakness. With a standard deviation around 2.9%, the consensus is remarkably tight—R2 and R3 are nearly identical—so I should anchor toward the median of 22% rather than R1's more generous 27%. Given the clear consensus that novelty is weak-to-medium while significance and related work are stronger, the realistic ceiling sits around 30-35%, which means I need to determine where within that range the final estimate should land. is supported by strong Related Work and dual-outcome design.
- Final: [18% - 28%] 中位 22-23%

Given the high consistency leaning toward R2/R3's assessment, and R1 being a slight outlier on the optimistic side, I'll set the final at [18% - 28%] 中位 23%.

Actually, let me be more careful. R1 gave [22-33%] with mid 27%. R2 and R3 both gave [18-28%] with mid 22%. The consensus is strongly toward the lower end. With high consistency, I should narrow the interval around the median. But per the rules, I should not be more generous than the most generous reviewer (R1 at 33% upper).

Final estimate: [18% - 30%] 中位 23%

The three reviewers are quite consistent with a standard deviation under 3%, which means I should tighten the range around the median of 22%, settling on [19% - 28%] 中位 23%. Now I'm assessing what's needed to implement this: roughly 100 H100-hours and $250 in compute costs, the public MATH dataset and Qwen models, minimal human effort for validating 200 samples, three GRPO training runs, and about 8 weeks to completion for AAAI scope.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce12aa21-37f9-4efc-896a-6f748d9b2973",
  "isSidechain": false,
  "requestId": "req_011CbVKVYu7eFwjuHvMunFq4",
  "type": "assistant",
  "uuid": "136cc84d-d790-491e-b372-cc66edb77a04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5qfkYuLatRPg4y4RBZJuz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29964,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3650,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3650,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 29964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29964
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

_source line 9 · 2026-05-28T16:58:11.163Z_

【阶段】: Meta Judge
【三次中位】: [27%, 22%, 22%]  std=2.9%
【共识维度】:
- **Novelty 弱-中**（3/3）：核心 "Learning-Gaming Paradox" 是两个对称凹函数（N(p,G) 和 √(p(1−p))）在 p=0.5 同时取极值——数学上接近 tautological。"Paradox" 标签夸大了惊奇性。审稿人极可能写 "trivially expected from functional forms"。
- **Significance 中**（3/3）：诊断性贡献在活跃领域有价值，但处方性输出（线性校准 s_k(d) = α_k + β_k·d）过于简单，不构成 transformative impact。
- **Related Work 强**（3/3）：覆盖 30-40+ 篇论文，8 个类别，差异化定位清晰。所有关键引用经调研验证真实存在且描述准确。
- **Trivial alternative 威胁显著**（3/3）：直接做 difficulty-stratified per-criterion gaming 统计即可获得核心经验洞见，无需理论框架。理论增量价值取决于 bound tightness（未验证）。
- **T2（Dimensionality Collapse）是最有 novelty 潜力的贡献**（2/3，R1+R2 明确提及）：但依赖强假设（A2 近乎定义性），验证困难。
- **"Decorative theory" 风险**（2/3，R2+R3）：Gaming Budget bound tightness 未验证，如果极度松弛则整个理论框架不提供超越直接经验测量的洞见。
- **A4 假设脆弱性**（3/3）：surface/formatting criteria 可能对难度不敏感（p_k ≈ 1.0 across all d），导致 Gaming Budget 在这些维度上趋近于 0，削弱 paradox 的 practical relevance。

【异常维度】:
- R1 给出 Novelty=中（而非弱-中），对 "真实的 novelty delta" 稍更慷慨，认为"交叉连接确实是新的"——但同时也承认核心数学观察是 "trivially true"。这是程度差异而非方向分歧，降权处理。
- R3 提到 POW3R reactive vs. proactive 区分"有些过度简化"——只有 R3 提到，属于 minor observation，不影响整体判断。

【最终概率】: [18% - 28%] 中位 23%
【一致性】: 高（std=2.9% < 3%，三位审稿人在所有 rubric 维度判决方向一致，R2/R3 几乎完全重合）
【综合理由】:
三位审稿人高度一致地将 Novelty 定位为弱-中（R1 略宽松给"中"，R2/R3 给"弱-中"），Significance 一致为中，Related Work 一致为强。核心限制因素清晰且无分歧：

1. **Novelty 天花板决定概率上限**：核心 "paradox"（Bernoulli 方差在中点最大的变体）的数学 triviality 是三位审稿人共同识别的致命弱点。R2 准确概括为 "manufactured by naming a natural mathematical property"。即使 T2 Dimensionality Collapse 有潜力，其依赖的假设过强（A2 近乎定义性），无法独立支撑论文的 novelty claim。在 Novelty 弱-中的情况下，概率上界不超过 ~30%。

2. **Trivial alternative 压缩增量价值**：三位审稿人一致认为核心经验贡献可通过简单的 stratified analysis 获得，无需 4 个定理的理论包装。理论增量的实际价值取决于 bound tightness——一个完全未经验证的前提。如果 bound 松弛（arXiv:2605.20744 的受控实验已显示 hack rate 随难度单调增加，可能与 bound 的 peak-at-0.5 预测矛盾），则论文退化为"我们在不同难度上测量了 per-criterion gaming"——R2 正确指出这对 AAAI 主会不够。

3. **Related Work 的强度提供了下限保障**：覆盖的全面性和差异化定位的准确性会获得审稿人正面评价。Dual-outcome 设计也提供了一定的风险对冲。但 Related Work 的强度无法弥补 Novelty 的不足——正如 R2 所言，"AAAI 审稿人更看重核心贡献的深度而非 related work 的广度"。

4. **R1 的 27% 中位略偏高**：R1 对 novelty 的判断（"中"而非"弱-中"）与另两位有轻微分歧，但 R1 自身也承认 "两个对称凹函数同在 p=0.5 取极值是数学必然"。在高一致情况下，按规则取中位附近并缩窄区间。两位给 22%、一位给 27%，中位 22%，综合取 23%（略微考虑 R1 的增量）。

**概率未达 36% 阈值的结构性原因**：Novelty 弱-中意味着即使实验执行完美，审稿人不太可能给出 "surprising, significant contribution" 的评价。核心 claim 的惊奇性不足（"I would have guessed this"）是最难通过实验弥补的缺陷。

【建议】: 不推荐（中位 23% < 36%，三位审稿人高度一致，核心 Novelty 不足是结构性问题而非执行问题）
【实施评估】:
  - 计算资源: ~100 H100-hours（AAAI scope），约 $250。3 个 GRPO 训练运行 × 4 H100 × 2.5hr + base-model pass@1 计算 8hr + judge inference 20hr + Pass@64 difficulty binning 25hr。资源需求合理。
  - 数据需求: MATH 数据集（公开）、Qwen2.5-Math-1.5B（公开）、Qwen3-8B 作为 judge（公开）。数据可得性无障碍。
  - 人工介入: 200 样本 judge quality 验证，工作量低。理论形式化需要一定数学功底但不需要外部专家。
  - 训练需求: 需要 3 个 GRPO 训练运行（uniform-GRPO、GRPO+RRM、DGPO+RRM），使用 1.5B 参数模型，单次训练约 10 H100-hours，规模可控。
  - 新 Benchmark: 不需要构建新 benchmark。需要构建 gaming heatmap 诊断工具，但这是分析产出而非数据集构建。
  - 预估周期: 8 周（AAAI scope），含 6 周实验 + 2 周写作。时间可行但紧张。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "136cc84d-d790-491e-b372-cc66edb77a04",
  "isSidechain": false,
  "requestId": "req_011CbVKVYu7eFwjuHvMunFq4",
  "type": "assistant",
  "uuid": "e38de7a7-e775-4606-8143-be7b06e703c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5qfkYuLatRPg4y4RBZJuz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 29964,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3650,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3650,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 29964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29964
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information from my research. Let me com…",
  "leafUuid": "e38de7a7-e775-4606-8143-be7b06e703c8",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Learning-Gaming paradox in rubric-based RL evaluation",
  "sessionId": "60020c65-c5ca-4696-8e6f-144fac44205e"
}
```

---
