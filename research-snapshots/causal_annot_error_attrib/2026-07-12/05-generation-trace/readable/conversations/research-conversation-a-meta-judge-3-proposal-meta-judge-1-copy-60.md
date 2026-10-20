# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/0c871b87-25d5-4f4c-85dc-39cc22bcc6ca.jsonl`
- **Structured JSON:** [`c7ee84300fd756d8c4cd.json`](../../sessions/c7/c7ee84300fd756d8c4cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T09:59:37.393Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T09:59:37.393Z",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a comprehensive assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [PAV / \"Rewarding Progress\"] (ICLR 2025): 定义了 process advantage verifier，用 V(s_i) - V(s_{i-1}) 作为 PRM 标签衡量每步的进展，比 ORM 准确率高 8%+。这是最直接的对比基线——同样通过 value function 差异来标注 step 信号。\n  https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html\n\n- [DuaShepherd] (arXiv 2506.17533, June 2025): 提出 correctness + potential 双信号多头架构的 PRM，在 MATH500 和 ProcessBench 上超越单信号模型。本 proposal 直接延伸其架构为三头。\n  https://arxiv.org/abs/2506.17533\n\n- [TCRM / \"Reward Models Are Secretly Value Functions\"] (arXiv 2604.22981, April 2026): 通过 TD/MC 正则化使 reward model 在任意中间 token 输出有意义的 value 估计，ProcessBench F1 达 44.9%（outcome-only SOTA），但与 supervised PRM (78.3% @72B) 仍有 33 点差距。本 proposal 依赖 TCRM 作为 value function 的基座。\n  https://arxiv.org/abs/2604.22981\n\n- [InT] (arXiv 2601.14209, Jan 2026 / ICLR 2025): 使用自提 counterfactual intervention 定位首个错误步并生成修正后续 trace，核心机制与本 proposal 的\"替换步骤观察结果变化\"高度相似，但用于 SFT 训练范式而非 PRM 标签生成。\n  https://arxiv.org/abs/2601.14209\n\n- [IBPO] (arXiv 2605.16302, May 2026): 通过跨多条推理轨迹的 counterfactual 比较构建隐式 process-level advantage estimator，目标是 RL policy optimization 而非 PRM 标签合成。概念上最接近本 proposal 的 counterfactual 框架。\n  https://arxiv.org/html/2605.16302\n\n- [PURE] (NeurIPS 2025): 将 min-form credit assignment 引入 PRM，解决 summation-form 导致的 reward hacking，用 min 而非 sum 定义 value function。\n  https://openreview.net/forum?id=3Sxby0hH1q\n\n- [GenPRM] (AAAI 2026): 将 PRM scoring 重新定义为 generative CoT reasoning + code verification，1.5B 模型超越 GPT-4o，7B 超越 72B PRM。代表了 PRM 的另一发展方向（生成式 vs. 判别式）。\n  https://arxiv.org/abs/2504.00891\n\n- [PRL] (arXiv 2601.10201, Jan 2026): 从策略/参考模型的熵比推导 process reward，将 sparse outcome reward 转化为 step-level supervision。用信息论方法量化步骤重要性。\n  https://arxiv.org/abs/2601.10201\n\n- [Credit Assignment Survey] (arXiv 2604.09459, April 2026): 识别 counterfactual analysis 为 agentic RL credit assignment 的新兴范式（HCAPO, CCPO, C3 均于 2026 年 3 月发表），但这些方法集中在 multi-agent 场景。\n  https://arxiv.org/html/2604.09459v1\n\n- 调研总结: PRM 标签生成领域正从单信号（correctness 或 MC probability）快速演进到多信号融合（DuaShepherd 的 correctness+potential，PAV 的 advantage）。同时，counterfactual credit assignment 在 agentic RL 领域已成熟但尚未系统性地迁移到 PRM 标签合成。本 proposal 处于这两个趋势的交汇点——用 counterfactual 方法为 PRM 生成新型标签信号。这是一个\"显而易见的下一步\"位置，意味着方向正确但 novelty 的窗口正在迅速关闭。\n\n\n【Trivial Alternative 检验】:\n\n存在至少两个成本更低的替代方案需要排除：\n\n1. **PAV-style advantage 直接替代**：PAV 的 advantage 信号 V(s_i) - V(s_{i-1}) 已经衡量了每步对预期结果的贡献。若一个步骤对结果影响大（高 advantage），其在替代方案下往往也有高方差。Proposal 需要论证 CI = Var_k[V(prefix || alt_k)] 提供了 advantage 无法捕获的独立信息。\n\n   不过，仔细分析后，CI 和 advantage 确实衡量不同维度：advantage 衡量*已实现*的进展，而 CI 衡量步骤内容的*敏感性*。一个\"强制步骤\"（如 2+2=4）可能有高 advantage 但低 CI（任何合理替代都会给出相同结果）；一个\"选择点\"（如选择代入哪个变量）可能有中等 advantage 但高 CI（不同选择导致截然不同的结果）。这种区分是有意义的，构成了相对于 advantage 的增量价值。\n\n2. **Policy entropy 作为 proxy**：步骤 s_i 处策略的 entropy 可作为\"选择点\"的低成本近似——高 entropy 意味着多种可能替代。但 entropy 只衡量替代的多样性，不衡量替代的*后果差异*，因此 CI 确实提供了更丰富的信号。\n\n**结论**：增量价值存在但需要实证验证。CI 的理论区分度成立，但实际改进幅度是关键问题。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未验证假设：\n\n1. **TCRM value estimates 的精度足以支撑 counterfactual variance 计算**。TCRM 在 ProcessBench 上仅 44.9% F1，与 supervised PRM 的 78.3% 有 33 点差距。如果 V(s) 本身噪声很大，Var_k[V(prefix || alt_k)] 可能更多反映 value function 的不确定性而非步骤的真实 counterfactual importance。这是整个方法论的根基假设，也是最脆弱的环节。\n\n2. **K=8 个替代样本足以可靠估计 variance**。8 个样本的方差估计本身方差很大（variance of variance estimator scales as O(1/K)），可能导致标签噪声显著。Proposal 未讨论这个统计问题。\n\n3. **CSI 信号与 correctness/potential 信号正交**。Proposal 声称三个信号提供互补信息，但未给出理论论证或初步实证。如果 CSI 与 potential 高度相关（高 potential variance 的步骤往往也是 potential 本身有特定分布的步骤），第三个头可能带来有限增益。\n\n4. **从 Qwen3-32B 采样的替代步骤能代表\"plausible alternatives\"的分布**。如果策略模型本身在某些步骤高度确定，采样 8 个替代可能只得到近似相同的步骤，导致 CI 人为偏低。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 核心贡献是将 counterfactual step replacement 的 variance 作为 PRM 标签信号，这个特定公式化确实尚未被先前工作采用。InT (2601.14209) 使用 counterfactual step replacement 但用于训练范式而非标签生成；IBPO (2605.16302) 做 counterfactual 比较但用于 RL policy optimization；PAV 用 advantage 但不测量 content sensitivity。因此存在真实的 novelty delta。然而，这本质上是将 agentic RL 中已成熟的 counterfactual paradigm（HCAPO, CCPO, C3）以自然方式迁移到 PRM 标签合成，加上 TCRM 的 value function 和 DuaShepherd 的多头架构——三个已有组件的组合。多位审稿人可能会评价为\"自然的下一步\"而非\"surprising insight\"。\n\n2. **Significance: 中** — PRM 改进是当前 LLM reasoning 领域的重要问题，有广泛的下游影响（best-of-N reranking、RL training signal、error detection）。但具体贡献是在 dual-signal PRM 上加第三个 head，预期改进幅度可能有限。如果核心结果是\"三头比两头好 2-3%\"，审稿人可能认为 marginal。更关键的是，GenPRM (AAAI 2026) 展示了一个完全不同且更有前景的方向（生成式 PRM），可能使判别式多头架构的增量改进显得 less impactful。\n\n3. **Related Work: 强** — 领域覆盖非常全面，包括最新的 2026 年工作（TCRM、IBPO、InT、credit assignment survey）。差异化定位清晰——明确区分了 InT（训练范式 vs. 标签生成）、IBPO（RL optimization vs. PRM label synthesis）、CoLD（length debiasing vs. importance scoring）。对 PAV、DuaShepherd、PURE、GenPRM 的定位都准确。唯一缺失的是 PRL (2601.10201) 和 AgentPRM，前者用信息论方法量化步骤重要性，概念上有重叠。\n\n\n【概率估计】: 20% - 30%，中位 25%\n\n【估计理由】: \nNovelty 为\"中\"是主要限制因素——idea 是三个已有组件（TCRM value function + DuaShepherd multi-head + counterfactual paradigm from agentic RL）的自然组合，方向正确但 insight 不够 surprising。Significance 也为\"中\"，因为增量改进的预期幅度有限，且 GenPRM 代表的生成式方向可能使判别式多头架构的增量改进相对暗淡。Related Work 的\"强\"评价有助于稳定下限但不提升上限。核心假设（TCRM value function 精度足够）的脆弱性进一步压低概率——如果 value function 噪声导致 CSI 标签不可靠，整个方法论基础受损。\n\n上界 (30%) 的条件：CSI 信号确实与 correctness/potential 正交，三头模型在 ProcessBench 和 MATH500 上有 >3% 的一致改进，且 ablation 清楚证明第三个头的 marginal contribution。\n下界 (20%) 的条件：审稿人认为这是已有组件的 trivial combination，或 TCRM value function 精度问题被视为致命缺陷。\n\n【主要风险】:\n1. **\"Natural combination\" 质疑**：审稿人可能认为 CSI 只是 counterfactual paradigm 从 agentic RL 到 PRM 的直接迁移，技术贡献不足以支撑顶会论文。核心公式 Var_k[V(prefix || alt_k)] 过于简洁，难以构成独立的 intellectual contribution。\n2. **Value function 精度瓶颈**：TCRM 的 44.9% F1 意味着 value estimates 相当 noisy；在此基础上计算 8 个替代的 variance 可能产生高噪声标签，使整个方法论的可靠性受到根本质疑。\n```\n\nSources:\n- [TCRM - Reward Models Are Secretly Value Functions](https://arxiv.org/abs/2604.22981)\n- [DuaShepherd](https://arxiv.org/abs/2506.17533)\n- [PAV - Rewarding Progress (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html)\n- [InT - Self-Proposed Interventions](https://arxiv.org/abs/2601.14209)\n- [IBPO - Counterfactual Reasoning Paths](https://arxiv.org/html/2605.16302)\n- [PURE - Min-Form Credit Assignment (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)\n- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)\n- [PRL - Process Reward Learning](https://arxiv.org/abs/2601.10201)\n- [Credit Assignment Survey](https://arxiv.org/html/2604.09459v1)\n- [Awesome Credit Assignment in LLM RL](https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research material. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146) (ICLR 2025 Spotlight): 提出 Process Advantage Verifier (PAV)，用 V(s_i) - V(s_{i-1}) 衡量每步\"progress\"，比 ORM 准确率高 8%+。这是与本 proposal 最直接相关的先驱工作——PAV 的 advantage 信号已经隐含了一种\"这一步对结果影响多大\"的度量。\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533) (arXiv Jun 2025): 多头架构同时训练 correctness + potential 两个信号，在 MATH500 和 ProcessBench 上优于单信号 PRM。本 proposal 直接扩展其架构加第三头，定位准确。\n- [Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling (TCRM)](https://arxiv.org/abs/2604.22981) (arXiv Apr 2026): 通过 TD/MC 正则化使 reward model 在任意 intermediate token 处输出 conditional expectation，ProcessBench 上达 44.9% F1（outcome-only SOTA），但与 supervised PRM (78.3% F1 at 72B) 仍有 33 点差距。本 proposal 依赖 TCRM 作为 value function backbone。\n- [IBPO / Reducing Credit Assignment Variance via Counterfactual Reasoning Paths](https://arxiv.org/abs/2605.16302) (arXiv May 2026): 通过跨多条推理轨迹的 counterfactual 比较构建 implicit process-level advantage，用于 RL policy optimization。与本 proposal 共享\"counterfactual 比较\"思路，但目标是 policy optimization 而非 PRM label 生成。\n- [InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning](https://arxiv.org/abs/2601.14209) (arXiv Jan 2026): 模型自身提出 single-step intervention 替换错误步骤，生成 counterfactual continuation。与本 proposal 共享\"替换某一步看结果如何变化\"的核心直觉，但 InT 是 training paradigm，不生成 step importance labels。\n- [Stop Summation (PURE): Min-Form Credit Assignment](https://openreview.net/forum?id=3Sxby0hH1q) (NeurIPS 2025): 指出 summation-form credit assignment 导致 reward hacking，用 min-form 替代。关注 credit assignment 的函数形式，与本 proposal 的 label generation 视角不同但同属 PRM credit assignment 大方向。\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891) (AAAI 2026): 将 PRM 从判别式改为生成式 CoT + code verification，1.5B 模型超越 GPT-4o。代表了 PRM 领域的另一条路线（生成式验证 vs 更好的 label 信号）。\n- [CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models](https://arxiv.org/pdf/2507.15698) (arXiv Jul 2025): 用 counterfactual 方法但仅用于 length debiasing，非 label 生成。\n- [HCAPO, CCPO, C3 — 三篇 March 2026 counterfactual credit assignment 论文]: 三篇同期论文聚焦 agentic RL 的 counterfactual credit assignment，表明这是当前热点范式。\n- [Group Causal Counterfactual Policy Optimization](https://arxiv.org/pdf/2602.06475) (Feb 2026): 构建 token-level counterfactual reward 衡量推理的鲁棒性和有效性，优化策略偏好 counterfactually robust reasoning patterns。\n- 调研总结: PRM 领域正处于高速发展期，主要进展沿三条线推进——(1) 更好的自动 label 生成方法 (PAV advantage, TCRM value, DuaShepherd multi-signal)；(2) 更好的 PRM 架构/范式 (GenPRM 生成式, PURE min-form)；(3) counterfactual credit assignment 从 agentic RL 向 reasoning 迁移 (IBPO, InT, HCAPO 等)。本 proposal 处于 (1) 和 (3) 的交叉点，提出用 counterfactual step replacement + variance 生成新的 PRM label，这个具体组合尚无直接先例，但各组件（counterfactual analysis、variance-based importance、multi-head PRM）均已有成熟工作。\n\n【Trivial Alternative 检验】:\n存在多个成本更低的 trivial alternative 威胁：\n\n1. **PAV advantage 信号本身已隐含 step importance 信息**: V(s_i) - V(s_{i-1}) 度量了每步对 expected outcome 的边际贡献。如果一步 advantage 很高，说明这步\"很重要\"（大幅改变了胜率）。CSI 衡量的是\"如果这步换成别的会怎样\"，与 advantage 高度相关——一步 advantage 很高/很低，通常对应于 alternatives 的 value 散布很广（即 CSI 也高）。\n\n2. **Gradient-based attribution**: 对 value function 输出关于 step representation 求梯度，可以零采样成本得到 step importance 近似值，避免 K=8 alternative generation 的 6M+ forward passes。\n\n3. **MC dropout / ensemble disagreement**: 用 value function 自身的 uncertainty 估计替代 counterfactual variance，计算成本低一个数量级。\n\n**增量价值判断**: CSI 相比这些 alternatives 的真正增量在于它通过 *policy-sampled alternatives* 而非模型内部扰动来衡量 importance，理论上更贴近\"实际可能出现的替代步骤\"。但这个增量价值能否转化为可测量的下游性能提升，是一个 open empirical question。如果 CSI ≈ f(advantage, correctness_uncertainty)，则增量价值趋近于零。\n\n【前提假设检验】:\n核心 claim 的逻辑链中有以下未经验证的关键假设：\n\n1. **TCRM value function 在 intermediate tokens 处足够准确以支撑 counterfactual evaluation**: TCRM 在 ProcessBench 上只有 44.9% F1（vs supervised PRM 78.3%）。用一个准确率不到 50% 的 value function 来计算 variance，噪声会被 variance 运算放大而非平滑——Var[V_noisy] ≠ Var[V_true] + noise_variance，误差项可能 dominate true signal。这是最薄弱的假设。\n\n2. **CSI 信号与 correctness + potential 正交**: Proposal 声称 CSI 提供\"orthogonal\"信息，但未给出理论论证。一个 correct 且 high-potential 的步骤，其 alternatives 很可能包含 incorrect/low-potential 选项（因为好步骤是少数），导致 CSI 天然高。反之亦然。这意味着 CSI 可能与 correctness × potential 高度共线。\n\n3. **\"Pivotality\" 信号在 inference time 有实际效用**: 训练时让 PRM 多学一个 head 预测 step pivotality，但在 best-of-N reranking 或 error detection 时，如何利用 pivotality 分数？一个 correct + high-potential + pivotal 的步骤和一个 correct + high-potential + routine 的步骤，在 reranking 中应该有不同权重吗？Proposal 没有论证 pivotality 信号的 downstream 使用机制。\n\n4. **K=8 alternatives 足以估计 variance**: 从 8 个样本估计 variance 本身的 standard error 很大（chi-squared distribution with df=7），导致 CSI labels 噪声较高。\n\n【3 维度打分】:\n  1. Novelty: 中 — \"用 counterfactual step replacement + variance 作为 PRM training label\"的具体组合确实尚无直接先例（调研中未找到完全匹配的工作）。但拆解来看，各组件都是已有技术的直接组合：counterfactual analysis 已在 IBPO/InT/HCAPO 等中广泛应用于 credit assignment，variance-based importance 是经典 sensitivity analysis 方法，multi-head PRM 在 DuaShepherd 中已验证。核心贡献更多是\"把 A 领域（counterfactual credit assignment for RL）的思路搬到 B 应用（PRM label generation）\"——这种 transfer 有价值但 novelty increment 有限。与 InT 的关键区别（InT 替换步骤后看能否纠正错误 vs 本文替换步骤后看 value variance）是 well-defined 的，但概念距离不远。\n\n  2. Significance: 中 — PRM 是当前 LLM reasoning 领域的热门课题（GenPRM 已被 AAAI 2026 接收，PAV 获 ICLR 2025 Spotlight），更好的 step-level supervision signal 有实际价值。但问题是：DuaShepherd 已经证明 2-signal > 1-signal，本 proposal 验证 3-signal > 2-signal 的边际贡献可能较小（diminishing returns）。即使结果 positive，审稿人的反应更可能是 \"makes sense, not surprising that more diverse signals help\" 而非 \"surprising, didn't expect this\"。此外，GenPRM 的生成式范式（1.5B 超越 GPT-4o）代表了一种可能使 discriminative PRM label engineering 整体边缘化的趋势——如果 PRM 的未来是 generative verification 而非 better label scores，则本工作的长期影响力受限。\n\n  3. Related Work: 强 — Proposal 对近期文献的覆盖相当全面且准确。TCRM、DuaShepherd、PAV、PURE、CoLD、InT、IBPO、GenPRM、HCAPO/CCPO/C3 credit assignment survey 均被引用且定位清晰。与 InT、IBPO 的区分（training paradigm vs label generation）是准确的。与 PAV advantage 的区分（progress vs counterfactual importance）是 well-articulated 的。唯一的小瑕疵是未讨论 gradient-based attribution 或 Shapley value 等经典 feature importance 方法作为 baseline/alternative，这些是 counterfactual importance 的直接理论对手。\n\n【概率估计】: [18% - 30%] 中位 24%\n\n【估计理由】: \nNovelty 处于\"中\"档——有真实的 novelty delta（具体组合未被做过），但核心是已有组件的相对直接组合（counterfactual analysis + variance + multi-head PRM），审稿人可能视为 incremental。Significance 也处于\"中\"档——方向正确且领域热门，但 (a) 3-signal vs 2-signal 的边际贡献可能属于 diminishing returns，(b) 如果结果 positive，并不 surprising，(c) generative PRM (GenPRM) 的崛起可能使 discriminative label engineering 的长期价值存疑。Related Work 是亮点（强），但 related work 质量提升的是下限而非上限。上界被 Novelty 限制：即使实验完美执行，核心 insight \"counterfactual variance as step importance label\" 在审稿人眼中可能是 \"nice but expected transfer\"。下界被 Significance 支撑：PRM 领域足够热，方向不会被认为不重要。此外，前提假设检验中 TCRM value function 准确性不足（44.9% F1）导致 CSI labels 噪声问题，以及 orthogonality 假设缺乏理论支撑，是两个实质性风险。\n\n【主要风险】: \n1. **CSI 与 correctness+potential 高度共线，marginal contribution 可忽略**: 如果 ablation 显示去掉 CSI head 对下游性能影响 < 1%，则整个 contribution 不成立。由于缺乏 orthogonality 的理论保证，这是一个现实风险。\n2. **\"搬运式\" novelty 质疑**: 审稿人可能认为核心贡献是把 counterfactual analysis（已在 agentic RL credit assignment 中广泛存在）直接搬到 PRM label generation，intellectual novelty 有限，尤其是 InT 已经在 reasoning 场景中使用了 step replacement + counterfactual continuation 的思路。\n```\n\nSources:\n- [TCRM: Reward Models Are Secretly Value Functions](https://arxiv.org/abs/2604.22981)\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)\n- [PAV: Rewarding Progress (ICLR 2025)](https://arxiv.org/abs/2410.08146)\n- [IBPO: Reducing Credit Assignment Variance via Counterfactual Reasoning Paths](https://arxiv.org/abs/2605.16302)\n- [InT: Self-Proposed Interventions Enable Credit Assignment](https://arxiv.org/abs/2601.14209)\n- [PURE: Stop Summation (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)\n- [GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026)](https://arxiv.org/abs/2504.00891)\n- [CoLD: Counterfactually-Guided Length Debiasing](https://arxiv.org/pdf/2507.15698)\n- [Credit Assignment Survey: From Reasoning to Agentic](https://arxiv.org/html/2604.09459v1)\n- [Group Causal Counterfactual Policy Optimization](https://arxiv.org/pdf/2602.06475)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have comprehensive research on this field. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- PAV / \"Rewarding Progress\" (ICLR 2025): 定义 advantage labels V(s_i) - V(s_{i-1}) 衡量步骤进展，8%+ accuracy gains over ORMs。是 CSI 最直接的 trivial alternative 威胁——advantage 和 counterfactual importance 高度相关但概念上不同。\n- DuaShepherd (arXiv 2506.17533, June 2025): 多头 PRM 架构 (correctness + potential)，验证了多信号融合优于单信号。本 proposal 的架构直接在此基础上扩展为三头。\n- TCRM (arXiv 2604.22981, April 2026): 时间一致性正则化使 reward model 可在任意中间 token 做 value estimation，ProcessBench 44.9% F1（outcome-only SOTA），但与监督 PRM 的 78.3% F1 仍有 33 个百分点差距。本 proposal 将 TCRM 作为 value function backbone。\n- PURE (NeurIPS 2025): Min-form credit assignment 解决 reward hacking，与本 proposal 关注点不同（credit assignment 形式 vs. label generation）。\n- CoLD (arXiv 2507.15698, July 2025): 用 counterfactual reasoning 做 length debiasing，不涉及 label generation。\n- InT (arXiv 2601.14209, Jan 2026): 通过 self-proposed interventions 做 counterfactual credit assignment，但用于训练范式（找到并修复错误步骤），不生成 importance labels。\n- IBPO / arXiv 2605.16302 (May 2026): 跨轨迹 counterfactual comparison 构建 implicit process-level advantage，但面向 RL policy optimization 而非 PRM label synthesis。\n- GenPRM (AAAI 2026): 将 PRM 重构为 generative CoT + code verification，1.5B 超 GPT-4o。方向与 label generation 正交。\n- SCAR (Cao et al., 2025): 用 Shapley values 做 credit assignment——game-theoretic 版本的 counterfactual baseline，与本 proposal 的 variance-based importance 概念高度相关但未被讨论。\n- MCNIG / \"Process Supervision via Monte Carlo Net Information Gain\" (March 2026): 用信息增益做 PRM step-level label 自动生成，直接竞争方法但 proposal 未提及。\n- EpicPRM (March 2025): 用量化贡献 + adaptive binary search 识别关键步骤并最小化标注成本，相关但 proposal 未提及。\n- Credit Assignment Survey (April 2026): 识别 counterfactual analysis 为 agentic RL credit 的新兴范式，三篇独立工作 (HCAPO, CCPO, C3) 在同一周出现。\n\n- 调研总结: PRM label generation 是当前热点方向，已有方法覆盖 binary correctness、MC completion probability、advantage-as-progress、generative CoT verification 等多种信号类型。Counterfactual analysis 在 agentic RL 中已形成共识范式，但确实尚未被转移到 PRM label 生成领域。本 proposal 处于 TCRM + DuaShepherd 的自然延伸位置，填补的是\"counterfactual step replacement → variance-based importance label\"这一具体技术空缺。\n\n【Trivial Alternative 检验】:\n最直接的 trivial alternative 是 PAV 的 absolute advantage |V(s_i) - V(s_{i-1})|——步骤进展大的地方通常也是重要的。如果某步骤 advantage 值极大，说明它对结果贡献大，这和 \"pivotal step\" 高度相关。Proposal 声称 CSI 与 advantage 概念不同：advantage 衡量\"这一步做了多少进展\"，CSI 衡量\"这一步的选择对结果有多敏感\"。理论上确实可以构造反例（一步是必走之路但进展大 = 高 advantage 低 CI；一步看似平常但在分岔路口 = 低 advantage 高 CI）。但实际上这种 decorrelation 是否显著存在是一个未经验证的假设。此外，Shapley value-based 方法 (SCAR) 是更有理论根基的 counterfactual importance 度量，variance 只是一个简化近似。增量价值取决于 CSI 相对于 advantage 的实际 decorrelation 程度——如果两者 Pearson r > 0.8，则增量很小。\n\n【前提假设检验】:\n1. **TCRM value function 的准确度足以支撑 counterfactual evaluation**: TCRM 在 ProcessBench 上仅 44.9% F1，与监督 PRM 差 33 个百分点。如果 value function 本身的步骤级估计不够准确，基于它算出的 Var_k[V(prefix || alt_k)] 噪声会很大，CSI labels 的信噪比存疑。整个 pipeline 的质量上界被 V(s) 的精度限制。\n2. **K=8 alternative samples 足以估计 outcome variance**: 从高维 policy 分布中抽 8 个 sample 估方差，统计效率很低。特别是对于 pivotal steps（真正重要的步骤），alternatives 可能高度 bimodal（要么对要么错），K=8 可能不够捕捉这种分布结构。\n3. **CSI 与 correctness/potential 信号正交**: Proposal 声称三种信号正交，但错误步骤天然有高 counterfactual importance（替换它会大幅改变结果），高 potential 步骤可能有低 variance（轨迹已在正轨）。信号间相关性可能比预期高，marginal value 可能比预期小。\n4. **Variance 是正确的聚合方式**: 为什么用方差而不是 range、entropy、或其他 dispersion measure？这个选择缺乏理论动机。\n\n【3 维度打分】:\n\n1. Novelty: 中 — \n   具体的技术组合（sample alternatives → evaluate with value function → variance as importance → PRM training label）确实没有被直接做过，与所有调研到的工作都有明确差异点。但这是 **组合式/工程式 novelty** 而非概念突破：每个组件（counterfactual analysis、value function for step evaluation、multi-head PRM）都已存在，贡献在于将它们连接成一个新 pipeline。核心 insight \"步骤重要性 = alternatives 导致结果发散程度\" 在 RL 中是经典思想（cf. Shapley values, counterfactual baselines），迁移到 PRM label 有一定新意但并不 surprising。与 SCAR 的 Shapley value 方法、InT 的 intervention-based counterfactual correction 在概念层面有非 trivial overlap，尽管技术路径不同。MCNIG 的 information gain 方法也是在同一个\"步骤重要性量化\"的方向上竞争，proposal 未讨论这一对比。\n\n2. Significance: 中 — \n   PRM label quality 是当前 LLM reasoning 领域的核心问题，研究问题本身重要且时效性强。TCRM 与监督 PRM 之间 33 点的 F1 gap 表明 label generation 确实有改进空间。然而，如果核心实验结果是 positive（tri-signal > dual-signal），审稿人更可能说 \"adding a third signal helps, as expected\" 而非 \"this is surprising\"。Marginal improvement 的大小决定 significance，但 idea 层面无法保证这个 delta 足够大。此外，该方法对 value function 质量高度依赖，推广性（beyond MATH/GSM8K）未知。\n\n3. Related Work: 中偏强 — \n   覆盖了 PAV、DuaShepherd、TCRM、PURE、CoLD、InT、IBPO、GenPRM 等核心工作，差异化定位清晰。但有两个显著遗漏：(1) SCAR（Shapley value-based credit assignment）是概念上最直接的竞争者，proposal 仅在引用 survey 时间接提及；(2) MCNIG（Monte Carlo Net Information Gain for PRM label generation, March 2026）是同一赛道的直接竞争方法但完全未被讨论。EpicPRM 的 quantified contribution 也相关但未提及。这些遗漏会被熟悉该领域的审稿人发现。\n\n【概率估计】: [22% - 32%] 中位 27%\n\n【估计理由】: \nNovelty 是限制上界的关键维度。核心贡献是将 RL 中经典的 counterfactual importance 概念（类 Shapley value）迁移到 PRM label generation，并以 variance 作为 proxy——这是一个 well-executed engineering contribution，但概念增量有限。\"If positive, expected not surprising\" 的判断将其锚定在 25-35% 区间的下半段。前提假设中 TCRM value function 的 44.9% F1 准确度和 K=8 sampling 的统计效率问题进一步压低估计。Related work 覆盖虽然不错，但对 SCAR 和 MCNIG 的遗漏会在审稿中被指出。Significance 受限于 marginal improvement 的不确定性和 trivial alternative (advantage labels) 的威胁。\n\n【主要风险】:\n1. **Trivial alternative 威胁**: 审稿人会质疑 CSI 相对于 PAV advantage labels 的增量价值——如果两者高度相关，则三头 PRM 相对于 \"advantage + correctness + potential\" 三头 PRM 无明显优势，核心 novelty 被削弱。\n2. **Value function 精度瓶颈**: 整个 pipeline 建立在 TCRM value function 之上（ProcessBench 44.9% F1），审稿人会合理质疑：一个本身不够准确的 value function 算出的 variance 是否是可靠的 importance signal，还是只是在放大噪声。\n```\n\nSources:\n- [TCRM: Reward Models Are Secretly Value Functions](https://arxiv.org/abs/2604.22981)\n- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)\n- [PAV: Rewarding Progress - Scaling Automated Process Verifiers](https://arxiv.org/abs/2410.08146)\n- [PURE: Stop Summation - Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)\n- [CoLD: Counterfactually-Guided Length Debiasing for PRMs](https://arxiv.org/abs/2507.15698)\n- [InT: Self-Proposed Interventions Enable Credit Assignment](https://arxiv.org/abs/2601.14209)\n- [IBPO: Reducing Credit Assignment Variance via Counterfactual Reasoning Paths](https://arxiv.org/abs/2605.16302)\n- [GenPRM: Scaling Test-Time Compute of PRMs via Generative Reasoning](https://arxiv.org/abs/2504.00891)\n- [Credit Assignment Survey: From Reasoning to Agentic](https://arxiv.org/html/2604.09459v1)\n- [CCPO: Counterfactual Credit Policy Optimization](https://arxiv.org/html/2603.21563v1)\n- [MCNIG: Process Supervision via Monte Carlo Net Information Gain](https://arxiv.org/html/2603.17815v1)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Counterfactual Step Importance Labels for Process Reward Models\n\n## Core Problem\n\nPRM training labels (binary correctness, MC completion probability, advantage-as-progress) fail to capture the counterfactual causal importance of each reasoning step — i.e., how much the outcome depends on the specific content of that step versus plausible alternatives — leading to PRMs that cannot distinguish pivotal reasoning choices from routine operations.\n\n## Research Opportunity\n\nTCRM (April 2026) enables efficient value estimation at any intermediate token via TD/MC-regularized reward models, making counterfactual evaluation computationally feasible without expensive full MC rollouts. DuaShepherd (June 2025) demonstrated that multi-signal PRMs (correctness + potential) outperform single-signal models, validating the principle that richer step-level signals improve PRM quality. Meanwhile, the April 2026 credit assignment survey identified counterfactual analysis as the emerging paradigm for agentic RL credit (HCAPO, CCPO, C3 — all March 2026), but this paradigm has not been transferred to reasoning PRM label generation.\n\n## Research Landscape\n\nPAV (ICLR 2025) trains PRMs on advantage labels (V(s_i) - V(s_{i-1})) measuring progress, achieving 8%+ accuracy gains over ORMs. DuaShepherd (June 2025) combines correctness and potential in a multi-head architecture outperforming either signal alone on ProcessBench and MATH500. TCRM (April 2026) achieves 44.9% F1 on ProcessBench via temporal coherence regularization (outcome-only SOTA), but a 33-point gap to supervised PRMs (78.3% at 72B) remains. PURE (NeurIPS 2025) addresses reward hacking via min-form credit assignment. CoLD (July 2025) uses counterfactual reasoning but only for length debiasing, not label generation. IBPO (arXiv 2605.16302, May 2026) introduces counterfactual comparison across multiple reasoning trajectories to construct an implicit process-level advantage estimator for RL policy optimization, but targets training-time credit assignment rather than PRM label synthesis. InT (arXiv 2601.14209, Jan 2026) uses self-proposed interventions to identify and fix the first error step via counterfactual corrections, but operates as a training paradigm rather than generating step importance labels. GenPRM (AAAI 2026) reframes PRM scoring as generative CoT reasoning with code verification. No existing method generates PRM training labels via counterfactual step replacement — measuring the outcome delta when a step is replaced by policy-sampled alternatives and evaluated with a trained value function — which would produce importance scores orthogonal to existing correctness/potential signals.\n\n## Proposed Approach\n\nTrain a TCRM-style temporally coherent value function on Qwen3-8B to enable efficient intermediate-token value estimation V(s) at any reasoning step without requiring full Monte Carlo rollouts. For each step s_i in a reasoning trace, sample K=8 alternative steps from the policy model (Qwen3-32B), prefix-concatenate each alternative with the preceding context, and compute counterfactual step importance as CI(s_i) = Var_k[V(prefix || alt_k)] — high variance indicates a pivotal step where alternatives dramatically change outcomes, low variance indicates a routine step. Generate CSI labels at scale over ~75K MATH/GSM8K solution traces from PRM800K, then train a tri-signal multi-head PRM (correctness + potential + counterfactual importance) extending DuaShepherd's architecture, where the third head learns to predict step pivotality. Evaluate on ProcessBench (error detection F1), MATH500 and GSM8K (best-of-N reranking accuracy), and AIME 2024, ablating each signal's marginal contribution to validate orthogonality of the counterfactual importance signal.\n\n## Detailed Description\n\nProcess reward models (PRMs) evaluate individual reasoning steps but rely on labels — binary correctness, MC completion probability, or advantage-as-progress — that do not capture a step's causal importance to the final outcome. We propose Counterfactual Step Importance (CSI) labels: for each step in a reasoning trace, we sample K alternative continuations from the policy model, evaluate the expected outcome of each using a TCRM-trained value function (which provides efficient intermediate-token value estimation without full rollouts), and compute the outcome variance as a measure of how much the reasoning outcome depends on that specific step versus plausible alternatives. Steps where alternatives lead to dramatically different outcomes are pivotal; steps where all alternatives yield similar outcomes are routine. We integrate CSI as a third training signal alongside correctness and potential in a multi-head PRM architecture inspired by DuaShepherd. Experiments on ProcessBench, MATH500, and GSM8K demonstrate that this tri-signal PRM outperforms dual-signal baselines on both error detection and best-of-N reranking. Our approach bridges the counterfactual credit assignment paradigm from agentic RL to reasoning PRM synthesis, producing importance-aware process supervision at scale.\n\n## Key References\n\n- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (ICLR 2025)\n- DuaShepherd: Integrating Stepwise Correctness and Potential Rewards for Mathematical Reasoning (arXiv 2025)\n- Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling (arXiv 2026)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)\n- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv 2025)\n- From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models (arXiv 2026)\n- Hindsight Credit Assignment for Long-Horizon LLM Agents (arXiv 2026)\n- Counterfactual Credit Policy Optimization for Multi-Agent Collaboration (arXiv 2026)\n- Contextual Counterfactual Credit Assignment for Multi-Agent RL in LLM Collaboration (arXiv 2026)\n- Reducing Credit Assignment Variance via Counterfactual Reasoning Paths (arXiv 2026)\n- InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning (arXiv 2026)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)\n- Let's Verify Step by Step (ICLR 2024)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 400–600 H100-hrs (value function training: 120, counterfactual generation: 200, tri-head PRM training: 80, eval/ablations: 80), timeline: 12–16 weeks (1 researcher), estimated_gpu_cost: $1,000–$1,500 at ~$2.50/H100-hr\n- **human_in_loop**: gpu_hours: 400–600 H100-hrs (same compute; Claude accelerates code/writing, not GPU workload), timeline: 8–11 weeks, claude_api_cost: $150–300 (Sonnet 4.6 for implementation scaffolding, experiment analysis, paper drafting), estimated_gpu_cost: $1,000–$1,500\n- **auto_research**: gpu_hours: 550–850 H100-hrs (additional hyperparameter sweeps over K, variance estimators, and head-weighting ablations), timeline: 4–6 weeks, claude_api_cost: $400–800 (heavy automated experimentation orchestration, iterative paper revision), estimated_gpu_cost: $1,375–$2,125, speed_bottleneck: Counterfactual generation throughput — 6M inference forward passes are embarrassingly parallel but require 8+ concurrent H100 GPUs to complete within days rather than weeks\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T09:59:37.397Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T09:59:37.397Z",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T09:59:37.467Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a comprehensive assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

- [PAV / "Rewarding Progress"] (ICLR 2025): 定义了 process advantage verifier，用 V(s_i) - V(s_{i-1}) 作为 PRM 标签衡量每步的进展，比 ORM 准确率高 8%+。这是最直接的对比基线——同样通过 value function 差异来标注 step 信号。
  https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html

- [DuaShepherd] (arXiv 2506.17533, June 2025): 提出 correctness + potential 双信号多头架构的 PRM，在 MATH500 和 ProcessBench 上超越单信号模型。本 proposal 直接延伸其架构为三头。
  https://arxiv.org/abs/2506.17533

- [TCRM / "Reward Models Are Secretly Value Functions"] (arXiv 2604.22981, April 2026): 通过 TD/MC 正则化使 reward model 在任意中间 token 输出有意义的 value 估计，ProcessBench F1 达 44.9%（outcome-only SOTA），但与 supervised PRM (78.3% @72B) 仍有 33 点差距。本 proposal 依赖 TCRM 作为 value function 的基座。
  https://arxiv.org/abs/2604.22981

- [InT] (arXiv 2601.14209, Jan 2026 / ICLR 2025): 使用自提 counterfactual intervention 定位首个错误步并生成修正后续 trace，核心机制与本 proposal 的"替换步骤观察结果变化"高度相似，但用于 SFT 训练范式而非 PRM 标签生成。
  https://arxiv.org/abs/2601.14209

- [IBPO] (arXiv 2605.16302, May 2026): 通过跨多条推理轨迹的 counterfactual 比较构建隐式 process-level advantage estimator，目标是 RL policy optimization 而非 PRM 标签合成。概念上最接近本 proposal 的 counterfactual 框架。
  https://arxiv.org/html/2605.16302

- [PURE] (NeurIPS 2025): 将 min-form credit assignment 引入 PRM，解决 summation-form 导致的 reward hacking，用 min 而非 sum 定义 value function。
  https://openreview.net/forum?id=3Sxby0hH1q

- [GenPRM] (AAAI 2026): 将 PRM scoring 重新定义为 generative CoT reasoning + code verification，1.5B 模型超越 GPT-4o，7B 超越 72B PRM。代表了 PRM 的另一发展方向（生成式 vs. 判别式）。
  https://arxiv.org/abs/2504.00891

- [PRL] (arXiv 2601.10201, Jan 2026): 从策略/参考模型的熵比推导 process reward，将 sparse outcome reward 转化为 step-level supervision。用信息论方法量化步骤重要性。
  https://arxiv.org/abs/2601.10201

- [Credit Assignment Survey] (arXiv 2604.09459, April 2026): 识别 counterfactual analysis 为 agentic RL credit assignment 的新兴范式（HCAPO, CCPO, C3 均于 2026 年 3 月发表），但这些方法集中在 multi-agent 场景。
  https://arxiv.org/html/2604.09459v1

- 调研总结: PRM 标签生成领域正从单信号（correctness 或 MC probability）快速演进到多信号融合（DuaShepherd 的 correctness+potential，PAV 的 advantage）。同时，counterfactual credit assignment 在 agentic RL 领域已成熟但尚未系统性地迁移到 PRM 标签合成。本 proposal 处于这两个趋势的交汇点——用 counterfactual 方法为 PRM 生成新型标签信号。这是一个"显而易见的下一步"位置，意味着方向正确但 novelty 的窗口正在迅速关闭。


【Trivial Alternative 检验】:

存在至少两个成本更低的替代方案需要排除：

1. **PAV-style advantage 直接替代**：PAV 的 advantage 信号 V(s_i) - V(s_{i-1}) 已经衡量了每步对预期结果的贡献。若一个步骤对结果影响大（高 advantage），其在替代方案下往往也有高方差。Proposal 需要论证 CI = Var_k[V(prefix || alt_k)] 提供了 advantage 无法捕获的独立信息。

   不过，仔细分析后，CI 和 advantage 确实衡量不同维度：advantage 衡量*已实现*的进展，而 CI 衡量步骤内容的*敏感性*。一个"强制步骤"（如 2+2=4）可能有高 advantage 但低 CI（任何合理替代都会给出相同结果）；一个"选择点"（如选择代入哪个变量）可能有中等 advantage 但高 CI（不同选择导致截然不同的结果）。这种区分是有意义的，构成了相对于 advantage 的增量价值。

2. **Policy entropy 作为 proxy**：步骤 s_i 处策略的 entropy 可作为"选择点"的低成本近似——高 entropy 意味着多种可能替代。但 entropy 只衡量替代的多样性，不衡量替代的*后果差异*，因此 CI 确实提供了更丰富的信号。

**结论**：增量价值存在但需要实证验证。CI 的理论区分度成立，但实际改进幅度是关键问题。


【前提假设检验】:

核心 claim 的逻辑链中有以下未验证假设：

1. **TCRM value estimates 的精度足以支撑 counterfactual variance 计算**。TCRM 在 ProcessBench 上仅 44.9% F1，与 supervised PRM 的 78.3% 有 33 点差距。如果 V(s) 本身噪声很大，Var_k[V(prefix || alt_k)] 可能更多反映 value function 的不确定性而非步骤的真实 counterfactual importance。这是整个方法论的根基假设，也是最脆弱的环节。

2. **K=8 个替代样本足以可靠估计 variance**。8 个样本的方差估计本身方差很大（variance of variance estimator scales as O(1/K)），可能导致标签噪声显著。Proposal 未讨论这个统计问题。

3. **CSI 信号与 correctness/potential 信号正交**。Proposal 声称三个信号提供互补信息，但未给出理论论证或初步实证。如果 CSI 与 potential 高度相关（高 potential variance 的步骤往往也是 potential 本身有特定分布的步骤），第三个头可能带来有限增益。

4. **从 Qwen3-32B 采样的替代步骤能代表"plausible alternatives"的分布**。如果策略模型本身在某些步骤高度确定，采样 8 个替代可能只得到近似相同的步骤，导致 CI 人为偏低。


【3 维度打分】:

1. **Novelty: 中** — 核心贡献是将 counterfactual step replacement 的 variance 作为 PRM 标签信号，这个特定公式化确实尚未被先前工作采用。InT (2601.14209) 使用 counterfactual step replacement 但用于训练范式而非标签生成；IBPO (2605.16302) 做 counterfactual 比较但用于 RL policy optimization；PAV 用 advantage 但不测量 content sensitivity。因此存在真实的 novelty delta。然而，这本质上是将 agentic RL 中已成熟的 counterfactual paradigm（HCAPO, CCPO, C3）以自然方式迁移到 PRM 标签合成，加上 TCRM 的 value function 和 DuaShepherd 的多头架构——三个已有组件的组合。多位审稿人可能会评价为"自然的下一步"而非"surprising insight"。

2. **Significance: 中** — PRM 改进是当前 LLM reasoning 领域的重要问题，有广泛的下游影响（best-of-N reranking、RL training signal、error detection）。但具体贡献是在 dual-signal PRM 上加第三个 head，预期改进幅度可能有限。如果核心结果是"三头比两头好 2-3%"，审稿人可能认为 marginal。更关键的是，GenPRM (AAAI 2026) 展示了一个完全不同且更有前景的方向（生成式 PRM），可能使判别式多头架构的增量改进显得 less impactful。

3. **Related Work: 强** — 领域覆盖非常全面，包括最新的 2026 年工作（TCRM、IBPO、InT、credit assignment survey）。差异化定位清晰——明确区分了 InT（训练范式 vs. 标签生成）、IBPO（RL optimization vs. PRM label synthesis）、CoLD（length debiasing vs. importance scoring）。对 PAV、DuaShepherd、PURE、GenPRM 的定位都准确。唯一缺失的是 PRL (2601.10201) 和 AgentPRM，前者用信息论方法量化步骤重要性，概念上有重叠。


【概率估计】: 20% - 30%，中位 25%

【估计理由】: 
Novelty 为"中"是主要限制因素——idea 是三个已有组件（TCRM value function + DuaShepherd multi-head + counterfactual paradigm from agentic RL）的自然组合，方向正确但 insight 不够 surprising。Significance 也为"中"，因为增量改进的预期幅度有限，且 GenPRM 代表的生成式方向可能使判别式多头架构的增量改进相对暗淡。Related Work 的"强"评价有助于稳定下限但不提升上限。核心假设（TCRM value function 精度足够）的脆弱性进一步压低概率——如果 value function 噪声导致 CSI 标签不可靠，整个方法论基础受损。

上界 (30%) 的条件：CSI 信号确实与 correctness/potential 正交，三头模型在 ProcessBench 和 MATH500 上有 >3% 的一致改进，且 ablation 清楚证明第三个头的 marginal contribution。
下界 (20%) 的条件：审稿人认为这是已有组件的 trivial combination，或 TCRM value function 精度问题被视为致命缺陷。

【主要风险】:
1. **"Natural combination" 质疑**：审稿人可能认为 CSI 只是 counterfactual paradigm 从 agentic RL 到 PRM 的直接迁移，技术贡献不足以支撑顶会论文。核心公式 Var_k[V(prefix || alt_k)] 过于简洁，难以构成独立的 intellectual contribution。
2. **Value function 精度瓶颈**：TCRM 的 44.9% F1 意味着 value estimates 相当 noisy；在此基础上计算 8 个替代的 variance 可能产生高噪声标签，使整个方法论的可靠性受到根本质疑。
```

Sources:
- [TCRM - Reward Models Are Secretly Value Functions](https://arxiv.org/abs/2604.22981)
- [DuaShepherd](https://arxiv.org/abs/2506.17533)
- [PAV - Rewarding Progress (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/98711dea460bdefe0e651ca23ec98ba2-Abstract-Conference.html)
- [InT - Self-Proposed Interventions](https://arxiv.org/abs/2601.14209)
- [IBPO - Counterfactual Reasoning Paths](https://arxiv.org/html/2605.16302)
- [PURE - Min-Form Credit Assignment (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)
- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [PRL - Process Reward Learning](https://arxiv.org/abs/2601.10201)
- [Credit Assignment Survey](https://arxiv.org/html/2604.09459v1)
- [Awesome Credit Assignment in LLM RL](https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research material. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning](https://arxiv.org/abs/2410.08146) (ICLR 2025 Spotlight): 提出 Process Advantage Verifier (PAV)，用 V(s_i) - V(s_{i-1}) 衡量每步"progress"，比 ORM 准确率高 8%+。这是与本 proposal 最直接相关的先驱工作——PAV 的 advantage 信号已经隐含了一种"这一步对结果影响多大"的度量。
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533) (arXiv Jun 2025): 多头架构同时训练 correctness + potential 两个信号，在 MATH500 和 ProcessBench 上优于单信号 PRM。本 proposal 直接扩展其架构加第三头，定位准确。
- [Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling (TCRM)](https://arxiv.org/abs/2604.22981) (arXiv Apr 2026): 通过 TD/MC 正则化使 reward model 在任意 intermediate token 处输出 conditional expectation，ProcessBench 上达 44.9% F1（outcome-only SOTA），但与 supervised PRM (78.3% F1 at 72B) 仍有 33 点差距。本 proposal 依赖 TCRM 作为 value function backbone。
- [IBPO / Reducing Credit Assignment Variance via Counterfactual Reasoning Paths](https://arxiv.org/abs/2605.16302) (arXiv May 2026): 通过跨多条推理轨迹的 counterfactual 比较构建 implicit process-level advantage，用于 RL policy optimization。与本 proposal 共享"counterfactual 比较"思路，但目标是 policy optimization 而非 PRM label 生成。
- [InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning](https://arxiv.org/abs/2601.14209) (arXiv Jan 2026): 模型自身提出 single-step intervention 替换错误步骤，生成 counterfactual continuation。与本 proposal 共享"替换某一步看结果如何变化"的核心直觉，但 InT 是 training paradigm，不生成 step importance labels。
- [Stop Summation (PURE): Min-Form Credit Assignment](https://openreview.net/forum?id=3Sxby0hH1q) (NeurIPS 2025): 指出 summation-form credit assignment 导致 reward hacking，用 min-form 替代。关注 credit assignment 的函数形式，与本 proposal 的 label generation 视角不同但同属 PRM credit assignment 大方向。
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891) (AAAI 2026): 将 PRM 从判别式改为生成式 CoT + code verification，1.5B 模型超越 GPT-4o。代表了 PRM 领域的另一条路线（生成式验证 vs 更好的 label 信号）。
- [CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models](https://arxiv.org/pdf/2507.15698) (arXiv Jul 2025): 用 counterfactual 方法但仅用于 length debiasing，非 label 生成。
- [HCAPO, CCPO, C3 — 三篇 March 2026 counterfactual credit assignment 论文]: 三篇同期论文聚焦 agentic RL 的 counterfactual credit assignment，表明这是当前热点范式。
- [Group Causal Counterfactual Policy Optimization](https://arxiv.org/pdf/2602.06475) (Feb 2026): 构建 token-level counterfactual reward 衡量推理的鲁棒性和有效性，优化策略偏好 counterfactually robust reasoning patterns。
- 调研总结: PRM 领域正处于高速发展期，主要进展沿三条线推进——(1) 更好的自动 label 生成方法 (PAV advantage, TCRM value, DuaShepherd multi-signal)；(2) 更好的 PRM 架构/范式 (GenPRM 生成式, PURE min-form)；(3) counterfactual credit assignment 从 agentic RL 向 reasoning 迁移 (IBPO, InT, HCAPO 等)。本 proposal 处于 (1) 和 (3) 的交叉点，提出用 counterfactual step replacement + variance 生成新的 PRM label，这个具体组合尚无直接先例，但各组件（counterfactual analysis、variance-based importance、multi-head PRM）均已有成熟工作。

【Trivial Alternative 检验】:
存在多个成本更低的 trivial alternative 威胁：

1. **PAV advantage 信号本身已隐含 step importance 信息**: V(s_i) - V(s_{i-1}) 度量了每步对 expected outcome 的边际贡献。如果一步 advantage 很高，说明这步"很重要"（大幅改变了胜率）。CSI 衡量的是"如果这步换成别的会怎样"，与 advantage 高度相关——一步 advantage 很高/很低，通常对应于 alternatives 的 value 散布很广（即 CSI 也高）。

2. **Gradient-based attribution**: 对 value function 输出关于 step representation 求梯度，可以零采样成本得到 step importance 近似值，避免 K=8 alternative generation 的 6M+ forward passes。

3. **MC dropout / ensemble disagreement**: 用 value function 自身的 uncertainty 估计替代 counterfactual variance，计算成本低一个数量级。

**增量价值判断**: CSI 相比这些 alternatives 的真正增量在于它通过 *policy-sampled alternatives* 而非模型内部扰动来衡量 importance，理论上更贴近"实际可能出现的替代步骤"。但这个增量价值能否转化为可测量的下游性能提升，是一个 open empirical question。如果 CSI ≈ f(advantage, correctness_uncertainty)，则增量价值趋近于零。

【前提假设检验】:
核心 claim 的逻辑链中有以下未经验证的关键假设：

1. **TCRM value function 在 intermediate tokens 处足够准确以支撑 counterfactual evaluation**: TCRM 在 ProcessBench 上只有 44.9% F1（vs supervised PRM 78.3%）。用一个准确率不到 50% 的 value function 来计算 variance，噪声会被 variance 运算放大而非平滑——Var[V_noisy] ≠ Var[V_true] + noise_variance，误差项可能 dominate true signal。这是最薄弱的假设。

2. **CSI 信号与 correctness + potential 正交**: Proposal 声称 CSI 提供"orthogonal"信息，但未给出理论论证。一个 correct 且 high-potential 的步骤，其 alternatives 很可能包含 incorrect/low-potential 选项（因为好步骤是少数），导致 CSI 天然高。反之亦然。这意味着 CSI 可能与 correctness × potential 高度共线。

3. **"Pivotality" 信号在 inference time 有实际效用**: 训练时让 PRM 多学一个 head 预测 step pivotality，但在 best-of-N reranking 或 error detection 时，如何利用 pivotality 分数？一个 correct + high-potential + pivotal 的步骤和一个 correct + high-potential + routine 的步骤，在 reranking 中应该有不同权重吗？Proposal 没有论证 pivotality 信号的 downstream 使用机制。

4. **K=8 alternatives 足以估计 variance**: 从 8 个样本估计 variance 本身的 standard error 很大（chi-squared distribution with df=7），导致 CSI labels 噪声较高。

【3 维度打分】:
  1. Novelty: 中 — "用 counterfactual step replacement + variance 作为 PRM training label"的具体组合确实尚无直接先例（调研中未找到完全匹配的工作）。但拆解来看，各组件都是已有技术的直接组合：counterfactual analysis 已在 IBPO/InT/HCAPO 等中广泛应用于 credit assignment，variance-based importance 是经典 sensitivity analysis 方法，multi-head PRM 在 DuaShepherd 中已验证。核心贡献更多是"把 A 领域（counterfactual credit assignment for RL）的思路搬到 B 应用（PRM label generation）"——这种 transfer 有价值但 novelty increment 有限。与 InT 的关键区别（InT 替换步骤后看能否纠正错误 vs 本文替换步骤后看 value variance）是 well-defined 的，但概念距离不远。

  2. Significance: 中 — PRM 是当前 LLM reasoning 领域的热门课题（GenPRM 已被 AAAI 2026 接收，PAV 获 ICLR 2025 Spotlight），更好的 step-level supervision signal 有实际价值。但问题是：DuaShepherd 已经证明 2-signal > 1-signal，本 proposal 验证 3-signal > 2-signal 的边际贡献可能较小（diminishing returns）。即使结果 positive，审稿人的反应更可能是 "makes sense, not surprising that more diverse signals help" 而非 "surprising, didn't expect this"。此外，GenPRM 的生成式范式（1.5B 超越 GPT-4o）代表了一种可能使 discriminative PRM label engineering 整体边缘化的趋势——如果 PRM 的未来是 generative verification 而非 better label scores，则本工作的长期影响力受限。

  3. Related Work: 强 — Proposal 对近期文献的覆盖相当全面且准确。TCRM、DuaShepherd、PAV、PURE、CoLD、InT、IBPO、GenPRM、HCAPO/CCPO/C3 credit assignment survey 均被引用且定位清晰。与 InT、IBPO 的区分（training paradigm vs label generation）是准确的。与 PAV advantage 的区分（progress vs counterfactual importance）是 well-articulated 的。唯一的小瑕疵是未讨论 gradient-based attribution 或 Shapley value 等经典 feature importance 方法作为 baseline/alternative，这些是 counterfactual importance 的直接理论对手。

【概率估计】: [18% - 30%] 中位 24%

【估计理由】: 
Novelty 处于"中"档——有真实的 novelty delta（具体组合未被做过），但核心是已有组件的相对直接组合（counterfactual analysis + variance + multi-head PRM），审稿人可能视为 incremental。Significance 也处于"中"档——方向正确且领域热门，但 (a) 3-signal vs 2-signal 的边际贡献可能属于 diminishing returns，(b) 如果结果 positive，并不 surprising，(c) generative PRM (GenPRM) 的崛起可能使 discriminative label engineering 的长期价值存疑。Related Work 是亮点（强），但 related work 质量提升的是下限而非上限。上界被 Novelty 限制：即使实验完美执行，核心 insight "counterfactual variance as step importance label" 在审稿人眼中可能是 "nice but expected transfer"。下界被 Significance 支撑：PRM 领域足够热，方向不会被认为不重要。此外，前提假设检验中 TCRM value function 准确性不足（44.9% F1）导致 CSI labels 噪声问题，以及 orthogonality 假设缺乏理论支撑，是两个实质性风险。

【主要风险】: 
1. **CSI 与 correctness+potential 高度共线，marginal contribution 可忽略**: 如果 ablation 显示去掉 CSI head 对下游性能影响 < 1%，则整个 contribution 不成立。由于缺乏 orthogonality 的理论保证，这是一个现实风险。
2. **"搬运式" novelty 质疑**: 审稿人可能认为核心贡献是把 counterfactual analysis（已在 agentic RL credit assignment 中广泛存在）直接搬到 PRM label generation，intellectual novelty 有限，尤其是 InT 已经在 reasoning 场景中使用了 step replacement + counterfactual continuation 的思路。
```

Sources:
- [TCRM: Reward Models Are Secretly Value Functions](https://arxiv.org/abs/2604.22981)
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)
- [PAV: Rewarding Progress (ICLR 2025)](https://arxiv.org/abs/2410.08146)
- [IBPO: Reducing Credit Assignment Variance via Counterfactual Reasoning Paths](https://arxiv.org/abs/2605.16302)
- [InT: Self-Proposed Interventions Enable Credit Assignment](https://arxiv.org/abs/2601.14209)
- [PURE: Stop Summation (NeurIPS 2025)](https://openreview.net/forum?id=3Sxby0hH1q)
- [GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [CoLD: Counterfactually-Guided Length Debiasing](https://arxiv.org/pdf/2507.15698)
- [Credit Assignment Survey: From Reasoning to Agentic](https://arxiv.org/html/2604.09459v1)
- [Group Causal Counterfactual Policy Optimization](https://arxiv.org/pdf/2602.06475)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have comprehensive research on this field. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- PAV / "Rewarding Progress" (ICLR 2025): 定义 advantage labels V(s_i) - V(s_{i-1}) 衡量步骤进展，8%+ accuracy gains over ORMs。是 CSI 最直接的 trivial alternative 威胁——advantage 和 counterfactual importance 高度相关但概念上不同。
- DuaShepherd (arXiv 2506.17533, June 2025): 多头 PRM 架构 (correctness + potential)，验证了多信号融合优于单信号。本 proposal 的架构直接在此基础上扩展为三头。
- TCRM (arXiv 2604.22981, April 2026): 时间一致性正则化使 reward model 可在任意中间 token 做 value estimation，ProcessBench 44.9% F1（outcome-only SOTA），但与监督 PRM 的 78.3% F1 仍有 33 个百分点差距。本 proposal 将 TCRM 作为 value function backbone。
- PURE (NeurIPS 2025): Min-form credit assignment 解决 reward hacking，与本 proposal 关注点不同（credit assignment 形式 vs. label generation）。
- CoLD (arXiv 2507.15698, July 2025): 用 counterfactual reasoning 做 length debiasing，不涉及 label generation。
- InT (arXiv 2601.14209, Jan 2026): 通过 self-proposed interventions 做 counterfactual credit assignment，但用于训练范式（找到并修复错误步骤），不生成 importance labels。
- IBPO / arXiv 2605.16302 (May 2026): 跨轨迹 counterfactual comparison 构建 implicit process-level advantage，但面向 RL policy optimization 而非 PRM label synthesis。
- GenPRM (AAAI 2026): 将 PRM 重构为 generative CoT + code verification，1.5B 超 GPT-4o。方向与 label generation 正交。
- SCAR (Cao et al., 2025): 用 Shapley values 做 credit assignment——game-theoretic 版本的 counterfactual baseline，与本 proposal 的 variance-based importance 概念高度相关但未被讨论。
- MCNIG / "Process Supervision via Monte Carlo Net Information Gain" (March 2026): 用信息增益做 PRM step-level label 自动生成，直接竞争方法但 proposal 未提及。
- EpicPRM (March 2025): 用量化贡献 + adaptive binary search 识别关键步骤并最小化标注成本，相关但 proposal 未提及。
- Credit Assignment Survey (April 2026): 识别 counterfactual analysis 为 agentic RL credit 的新兴范式，三篇独立工作 (HCAPO, CCPO, C3) 在同一周出现。

- 调研总结: PRM label generation 是当前热点方向，已有方法覆盖 binary correctness、MC completion probability、advantage-as-progress、generative CoT verification 等多种信号类型。Counterfactual analysis 在 agentic RL 中已形成共识范式，但确实尚未被转移到 PRM label 生成领域。本 proposal 处于 TCRM + DuaShepherd 的自然延伸位置，填补的是"counterfactual step replacement → variance-based importance label"这一具体技术空缺。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是 PAV 的 absolute advantage |V(s_i) - V(s_{i-1})|——步骤进展大的地方通常也是重要的。如果某步骤 advantage 值极大，说明它对结果贡献大，这和 "pivotal step" 高度相关。Proposal 声称 CSI 与 advantage 概念不同：advantage 衡量"这一步做了多少进展"，CSI 衡量"这一步的选择对结果有多敏感"。理论上确实可以构造反例（一步是必走之路但进展大 = 高 advantage 低 CI；一步看似平常但在分岔路口 = 低 advantage 高 CI）。但实际上这种 decorrelation 是否显著存在是一个未经验证的假设。此外，Shapley value-based 方法 (SCAR) 是更有理论根基的 counterfactual importance 度量，variance 只是一个简化近似。增量价值取决于 CSI 相对于 advantage 的实际 decorrelation 程度——如果两者 Pearson r > 0.8，则增量很小。

【前提假设检验】:
1. **TCRM value function 的准确度足以支撑 counterfactual evaluation**: TCRM 在 ProcessBench 上仅 44.9% F1，与监督 PRM 差 33 个百分点。如果 value function 本身的步骤级估计不够准确，基于它算出的 Var_k[V(prefix || alt_k)] 噪声会很大，CSI labels 的信噪比存疑。整个 pipeline 的质量上界被 V(s) 的精度限制。
2. **K=8 alternative samples 足以估计 outcome variance**: 从高维 policy 分布中抽 8 个 sample 估方差，统计效率很低。特别是对于 pivotal steps（真正重要的步骤），alternatives 可能高度 bimodal（要么对要么错），K=8 可能不够捕捉这种分布结构。
3. **CSI 与 correctness/potential 信号正交**: Proposal 声称三种信号正交，但错误步骤天然有高 counterfactual importance（替换它会大幅改变结果），高 potential 步骤可能有低 variance（轨迹已在正轨）。信号间相关性可能比预期高，marginal value 可能比预期小。
4. **Variance 是正确的聚合方式**: 为什么用方差而不是 range、entropy、或其他 dispersion measure？这个选择缺乏理论动机。

【3 维度打分】:

1. Novelty: 中 — 
   具体的技术组合（sample alternatives → evaluate with value function → variance as importance → PRM training label）确实没有被直接做过，与所有调研到的工作都有明确差异点。但这是 **组合式/工程式 novelty** 而非概念突破：每个组件（counterfactual analysis、value function for step evaluation、multi-head PRM）都已存在，贡献在于将它们连接成一个新 pipeline。核心 insight "步骤重要性 = alternatives 导致结果发散程度" 在 RL 中是经典思想（cf. Shapley values, counterfactual baselines），迁移到 PRM label 有一定新意但并不 surprising。与 SCAR 的 Shapley value 方法、InT 的 intervention-based counterfactual correction 在概念层面有非 trivial overlap，尽管技术路径不同。MCNIG 的 information gain 方法也是在同一个"步骤重要性量化"的方向上竞争，proposal 未讨论这一对比。

2. Significance: 中 — 
   PRM label quality 是当前 LLM reasoning 领域的核心问题，研究问题本身重要且时效性强。TCRM 与监督 PRM 之间 33 点的 F1 gap 表明 label generation 确实有改进空间。然而，如果核心实验结果是 positive（tri-signal > dual-signal），审稿人更可能说 "adding a third signal helps, as expected" 而非 "this is surprising"。Marginal improvement 的大小决定 significance，但 idea 层面无法保证这个 delta 足够大。此外，该方法对 value function 质量高度依赖，推广性（beyond MATH/GSM8K）未知。

3. Related Work: 中偏强 — 
   覆盖了 PAV、DuaShepherd、TCRM、PURE、CoLD、InT、IBPO、GenPRM 等核心工作，差异化定位清晰。但有两个显著遗漏：(1) SCAR（Shapley value-based credit assignment）是概念上最直接的竞争者，proposal 仅在引用 survey 时间接提及；(2) MCNIG（Monte Carlo Net Information Gain for PRM label generation, March 2026）是同一赛道的直接竞争方法但完全未被讨论。EpicPRM 的 quantified contribution 也相关但未提及。这些遗漏会被熟悉该领域的审稿人发现。

【概率估计】: [22% - 32%] 中位 27%

【估计理由】: 
Novelty 是限制上界的关键维度。核心贡献是将 RL 中经典的 counterfactual importance 概念（类 Shapley value）迁移到 PRM label generation，并以 variance 作为 proxy——这是一个 well-executed engineering contribution，但概念增量有限。"If positive, expected not surprising" 的判断将其锚定在 25-35% 区间的下半段。前提假设中 TCRM value function 的 44.9% F1 准确度和 K=8 sampling 的统计效率问题进一步压低估计。Related work 覆盖虽然不错，但对 SCAR 和 MCNIG 的遗漏会在审稿中被指出。Significance 受限于 marginal improvement 的不确定性和 trivial alternative (advantage labels) 的威胁。

【主要风险】:
1. **Trivial alternative 威胁**: 审稿人会质疑 CSI 相对于 PAV advantage labels 的增量价值——如果两者高度相关，则三头 PRM 相对于 "advantage + correctness + potential" 三头 PRM 无明显优势，核心 novelty 被削弱。
2. **Value function 精度瓶颈**: 整个 pipeline 建立在 TCRM value function 之上（ProcessBench 44.9% F1），审稿人会合理质疑：一个本身不够准确的 value function 算出的 variance 是否是可靠的 importance signal，还是只是在放大噪声。
```

Sources:
- [TCRM: Reward Models Are Secretly Value Functions](https://arxiv.org/abs/2604.22981)
- [DuaShepherd: Integrating Stepwise Correctness and Potential Rewards](https://arxiv.org/abs/2506.17533)
- [PAV: Rewarding Progress - Scaling Automated Process Verifiers](https://arxiv.org/abs/2410.08146)
- [PURE: Stop Summation - Min-Form Credit Assignment](https://arxiv.org/abs/2504.15275)
- [CoLD: Counterfactually-Guided Length Debiasing for PRMs](https://arxiv.org/abs/2507.15698)
- [InT: Self-Proposed Interventions Enable Credit Assignment](https://arxiv.org/abs/2601.14209)
- [IBPO: Reducing Credit Assignment Variance via Counterfactual Reasoning Paths](https://arxiv.org/abs/2605.16302)
- [GenPRM: Scaling Test-Time Compute of PRMs via Generative Reasoning](https://arxiv.org/abs/2504.00891)
- [Credit Assignment Survey: From Reasoning to Agentic](https://arxiv.org/html/2604.09459v1)
- [CCPO: Counterfactual Credit Policy Optimization](https://arxiv.org/html/2603.21563v1)
- [MCNIG: Process Supervision via Monte Carlo Net Information Gain](https://arxiv.org/html/2603.17815v1)


【原始 proposal（允许参考但不是主要依据）】:
# Counterfactual Step Importance Labels for Process Reward Models

## Core Problem

PRM training labels (binary correctness, MC completion probability, advantage-as-progress) fail to capture the counterfactual causal importance of each reasoning step — i.e., how much the outcome depends on the specific content of that step versus plausible alternatives — leading to PRMs that cannot distinguish pivotal reasoning choices from routine operations.

## Research Opportunity

TCRM (April 2026) enables efficient value estimation at any intermediate token via TD/MC-regularized reward models, making counterfactual evaluation computationally feasible without expensive full MC rollouts. DuaShepherd (June 2025) demonstrated that multi-signal PRMs (correctness + potential) outperform single-signal models, validating the principle that richer step-level signals improve PRM quality. Meanwhile, the April 2026 credit assignment survey identified counterfactual analysis as the emerging paradigm for agentic RL credit (HCAPO, CCPO, C3 — all March 2026), but this paradigm has not been transferred to reasoning PRM label generation.

## Research Landscape

PAV (ICLR 2025) trains PRMs on advantage labels (V(s_i) - V(s_{i-1})) measuring progress, achieving 8%+ accuracy gains over ORMs. DuaShepherd (June 2025) combines correctness and potential in a multi-head architecture outperforming either signal alone on ProcessBench and MATH500. TCRM (April 2026) achieves 44.9% F1 on ProcessBench via temporal coherence regularization (outcome-only SOTA), but a 33-point gap to supervised PRMs (78.3% at 72B) remains. PURE (NeurIPS 2025) addresses reward hacking via min-form credit assignment. CoLD (July 2025) uses counterfactual reasoning but only for length debiasing, not label generation. IBPO (arXiv 2605.16302, May 2026) introduces counterfactual comparison across multiple reasoning trajectories to construct an implicit process-level advantage estimator for RL policy optimization, but targets training-time credit assignment rather than PRM label synthesis. InT (arXiv 2601.14209, Jan 2026) uses self-proposed interventions to identify and fix the first error step via counterfactual corrections, but operates as a training paradigm rather than generating step importance labels. GenPRM (AAAI 2026) reframes PRM scoring as generative CoT reasoning with code verification. No existing method generates PRM training labels via counterfactual step replacement — measuring the outcome delta when a step is replaced by policy-sampled alternatives and evaluated with a trained value function — which would produce importance scores orthogonal to existing correctness/potential signals.

## Proposed Approach

Train a TCRM-style temporally coherent value function on Qwen3-8B to enable efficient intermediate-token value estimation V(s) at any reasoning step without requiring full Monte Carlo rollouts. For each step s_i in a reasoning trace, sample K=8 alternative steps from the policy model (Qwen3-32B), prefix-concatenate each alternative with the preceding context, and compute counterfactual step importance as CI(s_i) = Var_k[V(prefix || alt_k)] — high variance indicates a pivotal step where alternatives dramatically change outcomes, low variance indicates a routine step. Generate CSI labels at scale over ~75K MATH/GSM8K solution traces from PRM800K, then train a tri-signal multi-head PRM (correctness + potential + counterfactual importance) extending DuaShepherd's architecture, where the third head learns to predict step pivotality. Evaluate on ProcessBench (error detection F1), MATH500 and GSM8K (best-of-N reranking accuracy), and AIME 2024, ablating each signal's marginal contribution to validate orthogonality of the counterfactual importance signal.

## Detailed Description

Process reward models (PRMs) evaluate individual reasoning steps but rely on labels — binary correctness, MC completion probability, or advantage-as-progress — that do not capture a step's causal importance to the final outcome. We propose Counterfactual Step Importance (CSI) labels: for each step in a reasoning trace, we sample K alternative continuations from the policy model, evaluate the expected outcome of each using a TCRM-trained value function (which provides efficient intermediate-token value estimation without full rollouts), and compute the outcome variance as a measure of how much the reasoning outcome depends on that specific step versus plausible alternatives. Steps where alternatives lead to dramatically different outcomes are pivotal; steps where all alternatives yield similar outcomes are routine. We integrate CSI as a third training signal alongside correctness and potential in a multi-head PRM architecture inspired by DuaShepherd. Experiments on ProcessBench, MATH500, and GSM8K demonstrate that this tri-signal PRM outperforms dual-signal baselines on both error detection and best-of-N reranking. Our approach bridges the counterfactual credit assignment paradigm from agentic RL to reasoning PRM synthesis, producing importance-aware process supervision at scale.

## Key References

- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (ICLR 2025)
- DuaShepherd: Integrating Stepwise Correctness and Potential Rewards for Mathematical Reasoning (arXiv 2025)
- Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling (arXiv 2026)
- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (NeurIPS 2025)
- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv 2025)
- From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models (arXiv 2026)
- Hindsight Credit Assignment for Long-Horizon LLM Agents (arXiv 2026)
- Counterfactual Credit Policy Optimization for Multi-Agent Collaboration (arXiv 2026)
- Contextual Counterfactual Credit Assignment for Multi-Agent RL in LLM Collaboration (arXiv 2026)
- Reducing Credit Assignment Variance via Counterfactual Reasoning Paths (arXiv 2026)
- InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning (arXiv 2026)
- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)
- Let's Verify Step by Step (ICLR 2024)

## Resource Estimate

- **manual**: gpu_hours: 400–600 H100-hrs (value function training: 120, counterfactual generation: 200, tri-head PRM training: 80, eval/ablations: 80), timeline: 12–16 weeks (1 researcher), estimated_gpu_cost: $1,000–$1,500 at ~$2.50/H100-hr
- **human_in_loop**: gpu_hours: 400–600 H100-hrs (same compute; Claude accelerates code/writing, not GPU workload), timeline: 8–11 weeks, claude_api_cost: $150–300 (Sonnet 4.6 for implementation scaffolding, experiment analysis, paper drafting), estimated_gpu_cost: $1,000–$1,500
- **auto_research**: gpu_hours: 550–850 H100-hrs (additional hyperparameter sweeps over K, variance estimators, and head-weighting ablations), timeline: 4–6 weeks, claude_api_cost: $400–800 (heavy automated experimentation orchestration, iterative paper revision), estimated_gpu_cost: $1,375–$2,125, speed_bottleneck: Counterfactual generation throughput — 6M inference forward passes are embarrassingly parallel but require 8+ concurrent H100 GPUs to complete within days rather than weeks


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6ed6121c-534b-4672-b4a0-4df45382ee01",
  "type": "user",
  "uuid": "f1a14f73-f168-40d2-b93a-7298816877df",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T09:59:37.466Z_

```json
{
  "parentUuid": "f1a14f73-f168-40d2-b93a-7298816877df",
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
  "uuid": "d6bada33-0d07-48cd-aeb9-059c1ed5f268",
  "timestamp": "2026-05-27T09:59:37.466Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T09:59:37.466Z_

```json
{
  "parentUuid": "d6bada33-0d07-48cd-aeb9-059c1ed5f268",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "79d462c9-bed5-4050-9c8e-ed5f77d85ac0",
  "timestamp": "2026-05-27T09:59:37.466Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a comprehensive a…",
  "leafUuid": "79d462c9-bed5-4050-9c8e-ed5f77d85ac0",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate counterfactual step importance labels for PRMs",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca"
}
```

---

### Assistant

_source line 8 · 2026-05-27T10:00:06.037Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them according to the Meta Judge format.

Let me first extract the key data points:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [20% - 30%] 中位 25%
- Main risks: "Natural combination" critique, Value function precision bottleneck


**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [18% - 30%] 中位 24%
- Main risks: CSI collinearity with correctness+potential, "搬运式" novelty
**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 中偏强
- Probability: [22% - 32%] 中位 27%
- Main risks: Trivial alternative (PAV advantage), Value function precision bottleneck

Now I'm calculating the median probabilities across all three reviewers: 24%, 25%, and 27%.

Computing the mean and standard deviation of these medians gives me 25.3% with a standard deviation of about 1.25%, which indicates strong consistency across reviewers. Looking at the individual dimensions, there's clear agreement that novelty and significance are both moderate, while related work coverage leans toward strong, and I'm seeing a pattern of concerns around value function precision and the incremental nature of the contributions.

The consensus issues are striking—all three reviewers flag the TCRM value function precision risk, the "搬运式" novelty problem, potential collinearity between CSI and other metrics, and insufficient sampling with K=8, plus the unverified orthogonality assumption. The outliers are more scattered: R3 uniquely brings up SCAR and MCNIG as missing references and questions the choice of variance over range or entropy, while R2 is the only one questioning how pivotality would actually be used downstream.

Now I need to look at what the proposal claims for implementation resources.

Looking at the standard deviation across the three reviewer scores—it's about 1.25%, well under the 3% threshold, which means there's genuinely tight agreement here. All three landed between 24-27% with the same medium novelty and significance ratings. The picture is consistent: methodologically solid but incrementally novel, with TCRM precision and collinearity as the main technical concerns and some gaps in related work coverage. Given how tightly clustered these assessments are, I'll center my estimate around 25% with a narrower band of 20-30%.

Now I need to pull together the implementation feasibility assessment based on what the proposal outlines for resource requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79d462c9-bed5-4050-9c8e-ed5f77d85ac0",
  "isSidechain": false,
  "requestId": "req_011CbSssu2uL5qxn7sBRh9Zn",
  "type": "assistant",
  "uuid": "f3499365-6ae4-4102-bc52-104f024d3ae5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWEXLjxFTF4GpjmBQJo4UU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14836,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2948,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 14836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14836
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

_source line 9 · 2026-05-27T10:00:54.237Z_

【阶段】: Meta Judge
【三次中位】: [25%, 24%, 27%]  std=1.2%
【共识维度】:
- **Novelty: 中**（3/3 一致）— 具体技术组合（counterfactual step replacement → variance → PRM label）确实无直接先例，但本质是已有组件的自然组合（TCRM value function + DuaShepherd multi-head + agentic RL counterfactual paradigm），属"well-executed engineering contribution"而非概念突破
- **Significance: 中**（3/3 一致）— PRM 领域热门且方向正确，但 3-signal vs 2-signal 的边际贡献可能有限，"if positive, expected not surprising"；GenPRM 生成式范式可能使判别式 label engineering 的长期价值存疑
- **TCRM value function 精度瓶颈**（3/3 一致，致命级风险）— TCRM ProcessBench 44.9% F1 vs 监督 PRM 78.3%，33 点差距意味着 value estimates 本身 noisy，variance 运算可能放大而非平滑噪声，整个 CSI pipeline 的信噪比存疑
- **CSI 与 correctness/potential 共线性**（3/3 一致）— 缺乏正交性的理论保证，错误步骤天然有高 counterfactual importance，CSI 可能 ≈ f(advantage, correctness_uncertainty)，marginal contribution 可能可忽略
- **K=8 sampling 统计效率不足**（3/3 一致）— 8 样本方差估计自身方差大（df=7 chi-squared），对 bimodal 分布结构捕捉不够
- **"搬运式/natural combination" novelty 质疑**（3/3 一致）— 核心 insight 在 RL 中是经典思想，迁移到 PRM 有一定新意但 intellectual novelty 有限
- **Related Work: 强至中偏强**（2/3 评"强"，1/3 评"中偏强"）— 近期文献覆盖全面，差异化定位清晰

【异常维度】:
- R3 独家指出 SCAR（Shapley value-based credit assignment）和 MCNIG（Monte Carlo Net Information Gain, March 2026）两篇直接竞争/相关工作未被讨论 — **有效异常**，这两篇尤其是 MCNIG 是同一赛道的直接竞争方法，遗漏会被领域审稿人发现，应纳入考量
- R2 独家提出 gradient-based attribution 和 MC dropout/ensemble disagreement 作为更低成本 trivial alternatives — **有效但次要**，增加了 trivial alternative 的威胁面但不改变总体判断
- R3 独家质疑"为何用 variance 而非 range/entropy/其他 dispersion measure" — **有效但次要**，缺乏理论动机但不构成致命缺陷
- R2 独家质疑 pivotality 信号在 inference time 的 downstream 使用机制 — **有效**，proposal 确实未论证 pivotality score 在 best-of-N reranking 中具体如何被使用

【最终概率】: [20% - 29%] 中位 25%
【一致性】: 高
【综合理由】:
三位审稿人在所有核心维度上高度一致（std=1.2%，远低于 3% 阈值），这给出了很强的信号。Novelty 和 Significance 均为"中"是 3/3 共识，直接锚定了概率上界——即使实验完美执行，"counterfactual variance as step importance label"在审稿人眼中大概率被评为"natural next step"而非"surprising insight"，概率很难突破 35%。三个致命级共识风险（TCRM 精度瓶颈、CSI 共线性、搬运式 novelty）互相强化：如果 value function 不够准、CSI 与已有信号高度相关、且核心 idea 被视为 trivial combination，则三点同时命中时概率可跌破 20%。R3 独家发现的 MCNIG 遗漏是一个被低估的风险——同赛道直接竞争方法未被讨论会显著削弱 Related Work 维度的评分，将其从"强"拉向"中"。

高一致性下取中位附近、略微缩窄区间：原三人区间交集为 [22%-30%]，考虑 R3 的 MCNIG/SCAR 遗漏和 R2 的 gradient attribution trivial alternative 均为有效补充风险点，最终区间微调至 [20%-29%]，中位保持 25%。

【建议】: 边缘（偏不推荐侧）— 中位 25% 低于 36% 通过线，但方向正确且无致命不可救缺陷，有通过迭代优化提升的空间。核心瓶颈在 idea 层面（novelty 天花板），实验层面的问题（TCRM 精度、K 值、共线性验证）可通过实验设计部分缓解。

【实施评估】:
- **计算资源**: 400–850 H100-GPU-hours（value function 训练 ~120h, counterfactual generation ~200h 含 6M+ forward passes, tri-head PRM 训练 ~80h, eval/ablations ~80h）；需 8+ 并发 H100 GPU 以在合理时间内完成 counterfactual generation；预估 GPU 成本 $1,000–$2,125
- **数据需求**: PRM800K 的 ~75K MATH/GSM8K solution traces（公开可得）；ProcessBench, MATH500, GSM8K, AIME 2024 评测集（均公开）
- **人工介入**: 无需人工标注（全自动 label generation pipeline）；需研究者进行实验设计、结果分析和论文写作
- **训练需求**: 需训练 (1) TCRM-style value function（Qwen3-8B 基座）, (2) tri-signal multi-head PRM（DuaShepherd 架构扩展）；两个模型均为 8B 规模，训练量可控
- **新 Benchmark**: 不需要构建新 benchmark，使用现有 ProcessBench + MATH500 + GSM8K + AIME 2024
- **预估周期**: 单研究者 12–16 周（手动），8–11 周（有 AI 辅助），4–6 周（全自动化实验 + 更多 GPU 并行）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3499365-6ae4-4102-bc52-104f024d3ae5",
  "isSidechain": false,
  "requestId": "req_011CbSssu2uL5qxn7sBRh9Zn",
  "type": "assistant",
  "uuid": "26333ec9-c1c4-47f2-82c3-8b54a630482b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWEXLjxFTF4GpjmBQJo4UU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14836,
      "cache_read_input_tokens": 16543,
      "output_tokens": 2948,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2948,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 14836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14836
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a comprehensive a…",
  "leafUuid": "26333ec9-c1c4-47f2-82c3-8b54a630482b",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate counterfactual step importance labels for PRMs",
  "sessionId": "0c871b87-25d5-4f4c-85dc-39cc22bcc6ca"
}
```

---
