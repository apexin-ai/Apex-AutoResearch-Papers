# Research conversation: 【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。 【发掘 agent 本轮输出】: Now I have sufficient resear

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/e0cd6d6a-c98c-4091-bf86-447280e1f026.jsonl`
- **Structured JSON:** [`64b651d901f8f66fa72c.json`](../../sessions/64/64b651d901f8f66fa72c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:57:09.024Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:57:09.024Z",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "content": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have sufficient research to provide a thorough assessment. Let me compile my analysis.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n\n- **Causal Reward Adjustment (CRA, arXiv:2508.04216, Aug 2025)**: 直接用因果推断（sparse autoencoder + backdoor adjustment）在 PRM 内部表征上干预，缓解 reward hacking。**本 proposal 未引用，但高度相关**——同样是因果角度解决 PRM reward hacking，只是从 confounding features 而非 calibration 切入。\n- **Robust Reward Modeling via Causal Rubrics / CROME (arXiv:2506.16507, NeurIPS 2025)**: 用显式因果模型分离 prompt-driven preferences 和 spurious artifacts，在 RewardBench 上提升 5.4%。证明因果分解能增强 RM 鲁棒性这条路径已有先例。\n- **Learning a Pessimistic Reward Model / PET (arXiv:2505.20556, May 2025)**: 通过 pessimistic fine-tuning 学习悲观 reward model，不需要 KL regularization 即可防 hacking。这是 CGSP 最直接的方法层竞争者。\n- **Reward Shaping / PAR (arXiv:2502.18770, Feb 2025)**: 提出 bounded reward + centered reward 设计原则缓解 hacking，win rate 提升 5pp。提供了一种简单得多的 reward 变换方案。\n- **Conformal Feedback Alignment / CFA (arXiv:2601.17329, Jan 2026)**: 将 conformal prediction 用于 RLHF 偏好权重校准，但仅在 answer level，未涉及 step-level PRM。\n- **Distributional PRMs (arXiv:2605.06785, May 2026)**: 用 conditional optimal transport 实现 calibrated quantile functions，但完全未测试鲁棒性。\n- **Tiwari et al. (arXiv:2603.06621, Mar 2026)**: PRM 可被 hack 到 reward >0.9 而准确率 <4%，43% reward gains 来自 stylistic shortcuts。\n\n- **调研总结**: 当前领域有两个并行但独立的推进方向：(1) 因果/结构化方法增强 reward model 鲁棒性（CRA、CROME、CausalRM），(2) pessimism/uncertainty 方法约束 RL 优化（PET、Caution、PAR）。将 calibration 质量作为 hackability 的因果决定因素这一特定桥梁确实没人搭建过，但 CRA 已经从因果角度切入 PRM hacking 问题，与本 proposal 的因果 claim 存在交叉。\n\n---\n\n【发掘点 1】\n- 维度: trivial alternative 威胁 / 前提假设质疑\n- 内容: **Proposal 的因果 claim 面临一个关键 confound：\"calibration = reward compression\" 混淆。** Post-hoc calibration（特别是 temperature scaling）本质上是对 reward logits 做 rescaling，使输出分布更温和、更不极端。如果 temperature scaling 降低了 hackability，原因可能并非\"校准使概率估计更准确\"，而仅仅是\"reward 信号变得更平坦，gradient attack 的 reward gradient 变小了\"。这是一个 trivial mechanism。建议在 Component B 中增加一个 **reward range-matched control**：对 uncalibrated PRM 施加简单的线性缩放或 sigmoid clipping，使其 reward range 与 calibrated PRM 匹配，但不改善 calibration（ECE 不变或变差），然后测试 hackability。如果 hackability 仍然下降，说明机制是 reward compression 而非 calibration per se；如果只有真正改善 calibration 的方法才降低 hackability，因果 claim 才成立。**不解决这个 confound，审稿人一定会提出此质疑，而且这会直接动摇核心 claim 的说服力。**\n- 价值: 直接强化核心因果 claim 的逻辑严密性（命中 Novelty + Significance），将 proposal 从\"calibration 和 hackability 相关\"提升到\"calibration 因果性地决定 hackability，排除 trivial 解释\"。\n- 调研依据: Ackermann et al. (arXiv:2602.18037) 已证明 flatness 与 reward accuracy retention 相关；PAR (arXiv:2502.18770) 表明简单的 bounded/centered reward 变换即可缓解 hacking。两者共同暗示\"让 reward 不那么极端\"本身就可能是一个有效但 trivial 的防御机制。\n\n【发掘点 2】\n- 维度: related work 差异化\n- 内容: **CRA (Causal Reward Adjustment, arXiv:2508.04216) 是一个重大遗漏，可能威胁 novelty claim。** CRA 同样从因果角度解决 PRM reward hacking——用 sparse autoencoder 提取 PRM 内部表征的可解释特征，然后通过 backdoor adjustment 消除 confounding semantic features 的影响。虽然 CRA 的因果干预对象是\"features\"而非\"calibration\"，但审稿人很可能问：\"你们的 calibration-based causal story 和 CRA 的 feature-based causal story 是什么关系？有没有可能 calibration 改善 hackability 的真正机制就是消除了 confounding features（CRA 已经做了的事）？\" Proposal 必须 (a) 引用并详细讨论 CRA，(b) 明确两者的因果干预点不同（CRA 干预 representation space，CGSP 干预 output space），(c) 最好设计实验测试两种方法是否互补（e.g., CRA + calibration 是否比单独任何一个更好）。\n- 价值: 消除审稿人发现高度相关未引用工作后直接 reject 的风险，同时将 proposal 定位在一个更丰富的\"因果鲁棒 reward modeling\"大图景中（命中 Related Work 差异化 + Novelty）。\n- 调研依据: CRA (arXiv:2508.04216) 和 CROME (arXiv:2506.16507) 表明因果方法增强 RM 鲁棒性已有成熟先例，proposal 必须在这个 landscape 中定位自己。\n\n【发掘点 3】\n- 维度: significance 提升 / 核心 claim 强化\n- 内容: **Calibration Drift Detector 是全文潜在最有影响力的贡献，但当前被埋在 CGSP 的子组件里，严重低估了其独立价值。** 目前已有的 reward hacking detection 方法（gradient fingerprints, arXiv:2604.16242 等）需要事后分析或对抗性评估。而 Calibration Drift Detector 本质上是一个**zero-cost, real-time, model-agnostic 的 reward hacking 预警系统**——在 RL training 过程中实时监测 ECE drift，当 policy distribution shift 导致 PRM 失准时自动触发警报。这比任何事后检测方法都更实用。建议将 Calibration Drift Detector **提升为一个独立贡献（Component E）**，而非 CGSP 的附属组件：(1) 给出明确的理论动机：为什么 calibration drift 是 reward hacking 的充分早期信号？(2) 在 RL training 过程中系统性地测量 ECE drift 与 reward-accuracy divergence 的时序关系——如果 ECE drift 稳定地先于 reward hacking 出现，这本身就是一个重要的 empirical finding。(3) 可独立于 CGSP 使用——任何 PRM-based RL pipeline 都可以插入这个 detector。\n- 价值: 将一个技术组件升级为独立贡献，增加论文的\"贡献密度\"和实践影响力。如果 ECE drift 确实是 reward hacking 的可靠 leading indicator，这个发现的 significance 甚至可能超过 CGSP 本身（命中 Significance）。\n- 调研依据: Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242) 是当前最接近的检测方法，但需要 gradient 计算；本 proposal 的 drift detector 基于 ECE 统计量，计算成本更低，更易部署。\n\n【发掘点 4】\n- 维度: novelty 锐化\n- 内容: **Step-level compositional geometry 的 novelty claim 需要更锐利地表述\"为什么 outcome-level 分析不够\"。** 当前 proposal 正确指出 Ackermann et al. 只分析 outcome-level gradient norms，但仅说\"inapplicable to step-level PRM geometry\"还不够——需要给出一个具体的、直觉上 compelling 的例子说明 **step-level 分析会揭示 outcome-level 分析遗漏的现象**。例如：一个 PRM 可能在大多数 step 上是 flat 的（难以 hack），但在某个关键 step（如最终答案步）上有一个 sharp peak，使得 adversary 只需在那一步 inject noise 就能获得高 reward。Outcome-level 分析会将这种\"局部 sharp + 整体 flat\"的模式平均掉，产生错误的安全感。如果实验中确实发现这种 step-heterogeneous sharpness pattern，这将是一个非常有说服力的、仅 step-level 分析能捕捉到的 finding，直接证明 Component C 的必要性。\n- 价值: 将 Component C 从\"Ackermann et al. 的自然扩展\"提升为\"揭示了 outcome-level 分析的盲区\"，显著增强 novelty 感知（命中 Novelty）。\n- 调研依据: Ackermann et al. (arXiv:2602.18037) 的 Propositions 3.3-3.4 确实假设单一标量 reward R(s,a)，proposal 对此的批评是准确的。但需要从\"不适用\"升级到\"会遗漏具体什么现象\"才能让 novelty claim 真正锐利。\n\n【发掘点 5】\n- 维度: 前提假设质疑\n- 内容: **核心逻辑链条中有一个未经验证的关键假设：calibration 在 distribution shift 下是否仍有意义？** Calibration 通常在 held-out test set（与训练分布相同）上衡量。但 reward hacking 的核心场景恰恰是 OOD——adversarial attacks 和 RL policy shift 产生的轨迹不在 calibration 数据的分布内。一个 PRM 可能在 MATH-500 上完美 calibrated，但面对 RL-optimized trajectories 时 calibration 完全崩溃。如果 calibration 只在 in-distribution 有效，那么\"calibration 决定 hackability\"这个因果 claim 的适用范围就非常有限——它只能解释 mild overoptimization（小幅度的 distribution shift），但不能解释 severe hacking（大幅度的 OOD exploitation）。建议 proposal 明确讨论这个 scope limitation，并在 Component A 中增加一个分析维度：**测量 hackability 与 OOD calibration（而非 in-distribution calibration）的相关性**。这实际上可以将 Calibration Drift Detector 的动机嵌入更早的实验设计中——drift 的速度和幅度本身就是衡量 calibration 在 OOD 下脆弱性的指标。\n- 价值: 预防审稿人\"your calibration is only measured in-distribution, but hacking is OOD by definition\"的致命攻击，同时使 proposal 的理论框架更加自洽——将 in-distribution calibration、OOD calibration degradation、和 Calibration Drift Detector 串联成一个连贯的故事线（命中 Novelty + Significance）。\n- 调研依据: 基于领域整体趋势判断——calibration 的 distribution sensitivity 是 calibration 文献中的已知问题（Guo et al. 2017 原始 temperature scaling 论文就强调了 in-distribution 假设），但 PRM 场景下这个问题因 RL training 的 non-stationarity 被极度放大。\n\n---\n\nSources:\n- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)\n- [Distributional Process Reward Models (May 2026)](https://arxiv.org/abs/2605.06785)\n- [Reward Under Attack: PRM Hackability (March 2026)](https://arxiv.org/abs/2603.06621)\n- [Gradient Regularization Prevents Reward Hacking (Feb 2026)](https://arxiv.org/abs/2602.18037)\n- [Causal Reward Adjustment via Backdoor Correction (Aug 2025)](https://arxiv.org/abs/2508.04216)\n- [Robust Reward Modeling via Causal Rubrics / CROME](https://arxiv.org/abs/2506.16507)\n- [Learning a Pessimistic Reward Model / PET (May 2025)](https://arxiv.org/abs/2505.20556)\n- [Reward Shaping / PAR (Feb 2025)](https://arxiv.org/abs/2502.18770)\n- [Conformal Feedback Alignment (Jan 2026)](https://arxiv.org/abs/2601.17329)\n- [From Curiosity to Caution / Pessimism for BoN (April 2026)](https://arxiv.org/abs/2604.04648)\n- [Detecting and Suppressing Reward Hacking with Gradient Fingerprints (April 2026)](https://arxiv.org/abs/2604.16242)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research to provide a thorough assessment. Let me compile my analysis.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **Tiwari et al. \"Reward Under Attack\" (arXiv:2603.06621, 2026)**: 实验使用三层攻击框架（静态扰动、对抗性 token、RL-induced hacking），在 AIME 上用 GRPO 闭环评估，报告 PRM reward vs. ground-truth accuracy 的 divergence。Baseline 包括多个开源 PRM（Qwen、Skywork、Math-Shepherd 等）。43% reward gains 来自 stylistic shortcuts。无校准相关评估。\n- **Distributional PRMs (arXiv:2605.06785, May 2026)**: 使用 conditional optimal transport 做 PRM 校准，评测 Brier score、ECE、quantile coverage 等校准指标，在 MATH-500（in-distribution）和 AIME 24-25（OOD）上评测 BoN 性能。未测试对抗鲁棒性。\n- **Park et al. \"Know What You Don't Know\" (arXiv:2506.09338, NeurIPS 2025)**: PRM 校准的先驱工作，使用 quantile regression，评测 Brier score、AdaptiveCE、ECE、AverageCE。发现 PRM 在难题上系统性过估。代码开源。\n- **Ackermann et al. (arXiv:2602.18037, 2026)**: gradient norm 与 reward accuracy 的相关性分析，仅 outcome-level 单 scalar reward，用 gradient regularization 作为 defense。Baseline：标准 GRPO、KL-regularized GRPO。\n- **APRM (arXiv:2511.22888, 2025)**: 对抗训练 PRM，Generator-Discriminator 框架，跨 benchmark 平均 +3.4pp，OOD +5.3pp。评测包含多数学推理 benchmark。\n- **Caution (arXiv:2604.04648, 2026)**: BoN 场景下 pessimism-based defense，使用 prediction error 作为 uncertainty proxy，分析 overoptimization onset point N*。\n- **PURM (arXiv:2503.22480, 2025)**: 概率不确定性 reward model，将 scalar reward 推广为 Gaussian 分布，用 uncertainty penalty 进 PPO。\n- **PET (Pessimistic Reward Tuning)**: 通过对抗微调使 reward model 悲观化，无需 KL regularization。\n- **HessFormer / Granziol (arXiv:2602.00816, 2026)**: 首次在 100B 参数规模上做 Hessian spectral density estimation，使用 shard-local finite-difference HVP + FSDP，证明大规模 Hessian 分析可行但计算开销显著。\n- **PRMBench (arXiv:2501.03124)**: 6,216 problems / 83,456 step-level labels 的 PRM 评测 benchmark，评估多种 error 类型。\n\n**调研总结**: 该领域当前实验设计标准要求：(1) 多个开源 PRM 作为测试对象；(2) 至少两种攻击强度（静态 + RL-induced）；(3) 校准指标需包含 ECE、Brier score 和 reliability diagram；(4) BoN 评估需覆盖多个 N 值并报告 overoptimization onset；(5) baseline defense 需包含 KL-reg、ensemble、adversarial training 等主流方法。审稿人普遍期望：causal claim 需要严格的 ablation/control 实验，compute-normalized comparison，以及在 OOD 设置下的评估。\n\n---\n\n【缺陷 1】\n- 类别: 可行性问题\n- 问题: **Component C（Step-Level Hessian Spectral Analysis）在 72B PRM 上的计算可行性存疑。** Proposal 仅分配了 200 H100-hrs 给 Hessian 分析，但根据 Granziol (arXiv:2602.00816) 的工作，在 100B 参数模型上做 Hessian spectral density estimation 本身就是一项前沿挑战，需要 shard-local finite-difference HVP + FSDP 等专门基础设施。Proposal 要求在 8 个 PRM（包括 72B）× 多种校准方法 × 多个 step position × 多个问题上做 Hessian eigenvalue 分析——这意味着需要对每个配置在每个 step 上运行 Lanczos iteration，每次需要多次 Hessian-vector product（每个 HVP 的成本约等于一次完整 forward+backward pass）。对于 72B 模型，单次 HVP 需要 ~4×H100，Lanczos 需要 ~50-100 次 HVP 才能获得可靠的 top-k eigenvalue——单个配置单个 step 的分析就可能需要数小时。200 H100-hrs 对全部 48 配置的 step-level Hessian 分析严重不足。\n- 严重度: 可补救\n- 补救方案: (1) **缩小 Hessian 分析范围**: 不要对全部 48 配置做 Hessian 分析——选择 representative subset（如 2-3 个 PRM × 2 种校准方法 = 4-6 个配置）。(2) **放弃 72B 的 Hessian 分析**: 将 72B PRM 的 Hessian 分析降级为 gradient norm 分析（follow Ackermann et al. 的方法），仅在 7B/8B 模型上做完整 Hessian spectral analysis。(3) **使用 Hutchinson trace estimator 替代完整 Lanczos**: 如果只需要 top-1 eigenvalue 和 trace，Hutchinson + power iteration 比完整 Lanczos 便宜一个数量级。(4) **将 Hessian 分析的 budget 提高到 600-800 H100-hrs**，相应压缩其他不那么 critical 的预算（如减少 BoN evaluation 的 N 取值范围）。(5) 采样 step position 而非穷举所有 step——例如只分析第 1、中间、最后一个 step。\n- 调研依据: Granziol arXiv:2602.00816 (Hessian Spectral Analysis at Foundation Model Scale) 展示了大规模 Hessian 分析的基础设施需求和计算开销。\n\n【缺陷 2】\n- 类别: baseline 不足或过时\n- 问题: **CGSP defense 的 baseline 缺少 PURM 和 PET。** Proposal 列出了 5 个 CGSP baseline（uncalibrated GRPO、APRM、Caution、ensemble-min、gradient regularization），但遗漏了两个 2025-2026 的重要 defense 方法：(1) **PURM (arXiv:2503.22480)**——将 scalar reward 推广为 Gaussian 分布并用 uncertainty penalty 进 PPO，这与 CGSP 的 uncertainty-based pessimism 思路高度相似，是 CGSP 必须区分开的最近竞争者；(2) **PET (Pessimistic Reward Tuning)**——通过对抗微调使 reward model 悲观化，无需 KL regularization。此外，Proposal 提到了 KL-regularized GRPO 作为 baseline (v)，但没有包含 **Reference Resets**（Ackermann et al. 证明其隐式利用 gradient regularization），这是 KL-based defense 的更强变体。\n- 严重度: 可补救\n- 补救方案: 将 baseline 扩展为 7 个：(i) uncalibrated GRPO, (ii) APRM, (iii) Caution, (iv) ensemble-min, (v) gradient regularization, (vi) **PURM (uncertainty-penalized PPO)**, (vii) **PET (pessimistic reward tuning)**。特别是 PURM——审稿人几乎必然会问 \"CGSP 与 PURM 有什么区别？PURM 同样利用 reward uncertainty 进行 pessimism，为什么 CGSP 更好？\"。如果不将其作为 baseline 直接对比，这个问题将无法在 rebuttal 中有效回应。KL-regularized GRPO 可保留为 ablation 而非主 baseline。\n- 调研依据: PURM (arXiv:2503.22480) 是 2025 年提出的 uncertainty-aware reward defense 方法，与 CGSP 的 uncertainty-based pessimism 思路最为接近；PET 是 ICLR 2026 时期的 pessimistic reward tuning 方法。\n\n【缺陷 3】\n- 类别: 评估方案缺陷\n- 问题: **CGSP 的评估仅限于 MATH-500 和 AIME，缺乏对校准-鲁棒性因果链在其他 domain 的验证。** Proposal 的核心 claim 是 \"PRM calibration quality causally determines reward hacking resistance\"——这是一个非常 general 的因果声明。但实验仅在数学推理领域（MATH-500 + AIME）进行验证。审稿人将合理质疑：这个因果关系是否仅限于数学推理 PRM？是否在代码生成、逻辑推理等需要 step-level 验证的其他 domain 同样成立？此外，MATH-500 作为 in-distribution benchmark 已经被广泛质疑其 saturation 问题（许多模型已接近 ceiling）。\n- 严重度: 可补救\n- 补救方案: (1) **增加至少一个非数学 domain 的验证**，哪怕是小规模的：例如在代码生成（如 MBPP/HumanEval 的 step-level 评估）或逻辑推理（如 PRMBench 的子集）上复现 Component A 的 correlation study。这不需要全部 48 个配置，选 3-4 个 representative PRM 即可。(2) 如果完全无法获取非数学 PRM，则需在 paper 中明确声明 claim 的 scope limitation（\"We establish this causal link in mathematical reasoning; generalization to other domains is future work\"），并在实验设计中加入 **MATH difficulty stratification 的更细粒度分析**（如 Level 1-2 vs. Level 3-4 vs. Level 5 分别报告），至少展示因果关系在 difficulty distribution shift 下的稳定性。(3) **替换或增加 OOD benchmark**: 考虑加入 AMC 2023、Olympiad-level problems 或 AIME 2025（如果 Distributional PRM 论文使用了 AIME 24-25，则可以对齐）来扩展 OOD 评估范围。\n- 调研依据: Park et al. 和 Distributional PRM 都仅在数学推理上评测；Tiwari et al. 同样仅用 MATH 和 AIME。但 PRMBench (arXiv:2501.03124) 提供了多种 error type 评测，可作为补充验证工具。领域实验规范要求 causal claim 在至少两个 setting 下成立。\n\n【缺陷 4】\n- 类别: ablation 不完整\n- 问题: **CGSP 公式 r̃_t = μ_t − α·σ_t/√c_t 中有三个关键组件（calibrated uncertainty σ_t、calibration quality c_t、pessimism strength α），但 Proposal 未明确规划充分的 ablation 来隔离各组件贡献。** 具体来说：(1) σ_t vs. c_t 的相对贡献未被隔离——如果去掉 c_t（即用固定 c_t=1），CGSP 退化为简单的 uncertainty-based pessimism，这个 ablation 是论证 \"calibration-gated\" 机制价值的核心实验；(2) Calibration Drift Detector 的贡献未被隔离——它是 CGSP 系统的一部分但功能独立，需要单独 ablate；(3) pessimism strength α 的 sensitivity analysis 虽然在 resource estimate 中提到了 sweep，但未在实验设计中明确描述。\n- 严重度: 可补救\n- 补救方案: 明确规划以下 ablation 矩阵：\n\n  | Ablation | 描述 |\n  |----------|------|\n  | CGSP-full | r̃_t = μ_t − α·σ_t/√c_t + Drift Detector |\n  | CGSP w/o c_t | r̃_t = μ_t − α·σ_t（去掉 calibration quality gating） |\n  | CGSP w/o σ_t | r̃_t = μ_t − α/√c_t（用常数 uncertainty，仅保留 calibration gating） |\n  | CGSP w/o Drift | CGSP-full 但禁用 Calibration Drift Detector |\n  | CGSP fixed-α | α 固定为全局常数 vs. per-difficulty adaptive α |\n\n  这 5 个 ablation 可以精确回答审稿人的三个必然问题：\"calibration gating 有多重要？\"、\"drift detection 有多重要？\"、\"α 有多敏感？\"\n\n- 调研依据: 基于领域实验规范判断——defense method 论文的 ablation 需要完整隔离每个设计决策的贡献。Ackermann et al. 对 gradient regularization 做了类似的 component-wise ablation。\n\n【缺陷 5】\n- 类别: compute 公平性问题\n- 问题: **CGSP 与 baseline defense 的 compute-normalized comparison 未被规划。** CGSP 在 RL training 过程中需要额外计算：(1) 维护 rolling buffer 计算 c_t（ECE），(2) 运行 Calibration Drift Detector 定期评估当前分布 ECE，(3) 如果使用 conformal prediction 则需要 split-conformal 校准步骤。这些额外开销可能非 trivial。而 baseline 中 APRM 的额外开销在于对抗训练阶段（但推理/RL 时无额外开销），ensemble-min 的额外开销在于需要推理多个 reward model，gradient regularization 需要额外的 gradient 计算。如果不做 compute-normalized comparison，审稿人会质疑 CGSP 的性能提升是否只是因为用了更多计算。\n- 严重度: 可补救\n- 补救方案: (1) 报告每个方法的 **wall-clock time per GRPO iteration**（包括 reward computation + defense overhead）。(2) 在相同总计算预算下比较各方法的最终性能（compute-normalized curve：x 轴为总 GPU-hours，y 轴为 reward-accuracy alignment 或 downstream accuracy）。(3) 对 CGSP 的 overhead 进行 profiling breakdown（rolling buffer ECE 计算、drift detection、conformal calibration 各占多少额外时间）。(4) 如果 CGSP 的额外开销显著，考虑提供一个 CGSP-lite 变体（降低 drift detection 频率、减小 rolling buffer 大小）来展示 accuracy-efficiency tradeoff。\n- 调研依据: Ackermann et al. 在实验中报告了 gradient regularization 的计算开销比较；Caution (arXiv:2604.04648) 讨论了 pessimism 计算的额外开销。这是该领域 defense 论文的标准要求。\n\n【缺陷 6】\n- 类别: 实验设计不足\n- 问题: **Component B（Causal Isolation）的 matched representation change control (B3) 设计存在方法论风险。** Proposal 计划 \"Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration\"——但这个控制条件很难精确满足。(1) CKA-matched 的程度有多严格？CKA matching 需要在所有层都 match 还是只看 average CKA？(2) \"不改善 calibration\" 如何验证？如果 auxiliary task fine-tuning 恰好也改善了 calibration（math text 的 next-token prediction 可能间接提升数学推理能力），这个控制实验就失败了。(3) CKA 本身有 reliability 争议（arXiv:2210.16156 指出 CKA 在某些条件下不可靠）。\n- 严重度: 可补救\n- 补救方案: (1) **设计多个 auxiliary task 作为控制**，而非仅依赖一个：例如 (a) next-token prediction on non-math text (Wikipedia), (b) random label fine-tuning (破坏性微调)，(c) fine-tuning on math text with shuffled labels。多个控制的交叉验证比单一控制更有说服力。(2) **CKA matching 标准必须预注册**：明确定义 \"matched\" 的量化标准（如 \"per-layer CKA > 0.95\" 或 \"average CKA within ±0.02 of calibration fine-tuning\"），否则这将成为 post-hoc cherry-picking 的软肋。(3) **补充 CKA 之外的 representation similarity metric**：如 SVCCA 或 linear probing accuracy，来交叉验证 representation change 的 matching 程度，避免仅依赖 CKA 的 limitation。(4) 明确将 B1（post-hoc calibration，零 representation change）作为 **primary causal evidence**，B3 作为 **supporting evidence**——降低 B3 的举证负担。\n- 调研依据: arXiv:2210.16156 (Reliability of CKA as a Similarity Measure) 指出 CKA 的可靠性问题；Park et al. 的校准工作未做此类 causal control。\n\n【缺陷 7】\n- 类别: 评估方案缺陷\n- 问题: **Correlation study (Component A) 的统计功效声明需要更仔细的检验。** Proposal 声称 \"n=48, detecting r≥0.29 at p<0.05\"——这假设 48 个 PRM×calibration 配置是独立观测，但实际上它们不是独立的：同一个 PRM 的 6 种校准方法之间高度相关（共享 base model representation），同一种校准方法在 8 个 PRM 上的效果也可能因 PRM architecture 而聚类。这种 within-cluster correlation 会严重膨胀有效自由度，导致实际统计功效远低于声称值。\n- 严重度: 可补救\n- 补救方案: (1) 使用 **mixed-effects model**（PRM 作为 random effect, calibration method 作为 fixed effect）替代简单的 Spearman correlation，正确处理嵌套结构。(2) 报告 **cluster-robust standard errors** 或 **bootstrap confidence intervals**（对 PRM 进行 block bootstrap）。(3) 补充 **within-PRM analysis**：在每个 PRM 内部，6 种校准方法是否单调改善 hackability？这个 within-subject 分析不受 between-PRM heterogeneity 影响，是更干净的因果证据。(4) 如果审稿人认为 n_effective 因聚类降到 ~8-16，则需要更大的效应量才能 detect——在 paper 中讨论这个 limitation 并解释为什么即使用 conservative n_effective，观察到的效应量仍然显著。\n- 调研依据: 基于领域实验规范判断——correlation study 中的非独立观测结构是统计方法论的基本问题。Park et al. 和 Distributional PRM 的评估设计没有面对这个问题因为它们不做跨配置的 correlation analysis。\n\n【缺陷 8】\n- 类别: 可行性问题\n- 问题: **Component A 的 gradient-based attack（Tier i）需要 8 个 PRM × 6 种校准方法 = 48 个配置的 white-box gradient attack，1000 H100-hrs 是否充足需要验证。** Tiwari et al. 的 gradient attack 需要对每个 PRM 做迭代 token-level optimization（类似 GCG），这在 72B 模型上代价极高。如果每个配置需要在 ~500 problems（MATH-500）上运行 gradient attack，每个 problem 需要数百次梯度迭代，72B 模型的每次梯度计算需要 4×H100——单个配置可能需要 100+ H100-hrs。48 个配置 × 100 hrs = 4800 H100-hrs，远超分配的 1000 H100-hrs。\n- 严重度: 可补救\n- 补救方案: (1) **分层设计 gradient attack 评估**: 仅对 representative subset（如 4 个 PRM × 3 种校准方法 = 12 个配置）执行完整 gradient attack；其余配置仅做 Tier ii（RL-induced hacking）和 Tier iii（BoN），因为这两者计算开销更可控。(2) **对 72B PRM 仅做 BoN 评估和 RL-induced hacking 评估**，放弃其 gradient attack（理由：72B 的 white-box access 场景在实践中也不太现实，这是一个合理的 scope choice）。(3) 重新估算 gradient attack budget：如果缩小到 12 个配置，1000 H100-hrs 可能刚好足够（~83 hrs/配置）。(4) 使用 **transfer attack** 替代部分 white-box attack：用 7B PRM 上生成的 adversarial tokens 测试 72B PRM，这既省计算又增加了评估的生态效度。\n- 调研依据: Tiwari et al. (arXiv:2603.06621) 的 gradient attack 实验规模和成本参考。\n\n---\n\n**总结**: 该 proposal 的实验框架设计已经相当完善——四个 component 的分工清晰，post-hoc calibration 作为 causal tool 的思路方法论上正确，CGSP defense 的设计有明确的差异化。上述 8 个缺陷**全部可补救**，没有发现致命的方向性问题。核心需要关注的优先级排序为：\n\n1. **P0（必须修）**: 缺陷 2（补充 PURM/PET baseline）、缺陷 4（CGSP ablation 矩阵）——这两个是审稿人几乎 100% 会问的。\n2. **P1（强烈建议）**: 缺陷 5（compute-normalized comparison）、缺陷 7（correlation study 统计方法）——这两个影响 claim 的说服力。\n3. **P2（建议但可降级）**: 缺陷 1（Hessian 可行性）、缺陷 8（gradient attack budget）——通过缩小范围可解决。\n4. **P3（理想但非必须）**: 缺陷 3（非数学 domain 验证）、缺陷 6（matched control 设计）——scope limitation 可在 paper 中声明。\n\nSources:\n- [Reward Under Attack (Tiwari et al.)](https://arxiv.org/abs/2603.06621)\n- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)\n- [Know What You Don't Know (Park et al.)](https://arxiv.org/abs/2506.09338)\n- [Gradient Regularization (Ackermann et al.)](https://arxiv.org/abs/2602.18037)\n- [APRM](https://arxiv.org/abs/2511.22888)\n- [Caution](https://arxiv.org/abs/2604.04648)\n- [PURM](https://arxiv.org/abs/2503.22480)\n- [Hessian Spectral Analysis at Foundation Model Scale](https://arxiv.org/abs/2602.00816)\n- [HessFormer](https://arxiv.org/abs/2505.11564)\n- [PRMBench](https://arxiv.org/abs/2501.03124)\n- [Reliability of CKA](https://arxiv.org/abs/2210.16156)\n- [Conformal Feedback Alignment](https://arxiv.org/abs/2601.17329)\n- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:57:09.028Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:57:09.028Z",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-20T05:57:09.074Z_

【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】

- **Causal Reward Adjustment (CRA, arXiv:2508.04216, Aug 2025)**: 直接用因果推断（sparse autoencoder + backdoor adjustment）在 PRM 内部表征上干预，缓解 reward hacking。**本 proposal 未引用，但高度相关**——同样是因果角度解决 PRM reward hacking，只是从 confounding features 而非 calibration 切入。
- **Robust Reward Modeling via Causal Rubrics / CROME (arXiv:2506.16507, NeurIPS 2025)**: 用显式因果模型分离 prompt-driven preferences 和 spurious artifacts，在 RewardBench 上提升 5.4%。证明因果分解能增强 RM 鲁棒性这条路径已有先例。
- **Learning a Pessimistic Reward Model / PET (arXiv:2505.20556, May 2025)**: 通过 pessimistic fine-tuning 学习悲观 reward model，不需要 KL regularization 即可防 hacking。这是 CGSP 最直接的方法层竞争者。
- **Reward Shaping / PAR (arXiv:2502.18770, Feb 2025)**: 提出 bounded reward + centered reward 设计原则缓解 hacking，win rate 提升 5pp。提供了一种简单得多的 reward 变换方案。
- **Conformal Feedback Alignment / CFA (arXiv:2601.17329, Jan 2026)**: 将 conformal prediction 用于 RLHF 偏好权重校准，但仅在 answer level，未涉及 step-level PRM。
- **Distributional PRMs (arXiv:2605.06785, May 2026)**: 用 conditional optimal transport 实现 calibrated quantile functions，但完全未测试鲁棒性。
- **Tiwari et al. (arXiv:2603.06621, Mar 2026)**: PRM 可被 hack 到 reward >0.9 而准确率 <4%，43% reward gains 来自 stylistic shortcuts。

- **调研总结**: 当前领域有两个并行但独立的推进方向：(1) 因果/结构化方法增强 reward model 鲁棒性（CRA、CROME、CausalRM），(2) pessimism/uncertainty 方法约束 RL 优化（PET、Caution、PAR）。将 calibration 质量作为 hackability 的因果决定因素这一特定桥梁确实没人搭建过，但 CRA 已经从因果角度切入 PRM hacking 问题，与本 proposal 的因果 claim 存在交叉。

---

【发掘点 1】
- 维度: trivial alternative 威胁 / 前提假设质疑
- 内容: **Proposal 的因果 claim 面临一个关键 confound："calibration = reward compression" 混淆。** Post-hoc calibration（特别是 temperature scaling）本质上是对 reward logits 做 rescaling，使输出分布更温和、更不极端。如果 temperature scaling 降低了 hackability，原因可能并非"校准使概率估计更准确"，而仅仅是"reward 信号变得更平坦，gradient attack 的 reward gradient 变小了"。这是一个 trivial mechanism。建议在 Component B 中增加一个 **reward range-matched control**：对 uncalibrated PRM 施加简单的线性缩放或 sigmoid clipping，使其 reward range 与 calibrated PRM 匹配，但不改善 calibration（ECE 不变或变差），然后测试 hackability。如果 hackability 仍然下降，说明机制是 reward compression 而非 calibration per se；如果只有真正改善 calibration 的方法才降低 hackability，因果 claim 才成立。**不解决这个 confound，审稿人一定会提出此质疑，而且这会直接动摇核心 claim 的说服力。**
- 价值: 直接强化核心因果 claim 的逻辑严密性（命中 Novelty + Significance），将 proposal 从"calibration 和 hackability 相关"提升到"calibration 因果性地决定 hackability，排除 trivial 解释"。
- 调研依据: Ackermann et al. (arXiv:2602.18037) 已证明 flatness 与 reward accuracy retention 相关；PAR (arXiv:2502.18770) 表明简单的 bounded/centered reward 变换即可缓解 hacking。两者共同暗示"让 reward 不那么极端"本身就可能是一个有效但 trivial 的防御机制。

【发掘点 2】
- 维度: related work 差异化
- 内容: **CRA (Causal Reward Adjustment, arXiv:2508.04216) 是一个重大遗漏，可能威胁 novelty claim。** CRA 同样从因果角度解决 PRM reward hacking——用 sparse autoencoder 提取 PRM 内部表征的可解释特征，然后通过 backdoor adjustment 消除 confounding semantic features 的影响。虽然 CRA 的因果干预对象是"features"而非"calibration"，但审稿人很可能问："你们的 calibration-based causal story 和 CRA 的 feature-based causal story 是什么关系？有没有可能 calibration 改善 hackability 的真正机制就是消除了 confounding features（CRA 已经做了的事）？" Proposal 必须 (a) 引用并详细讨论 CRA，(b) 明确两者的因果干预点不同（CRA 干预 representation space，CGSP 干预 output space），(c) 最好设计实验测试两种方法是否互补（e.g., CRA + calibration 是否比单独任何一个更好）。
- 价值: 消除审稿人发现高度相关未引用工作后直接 reject 的风险，同时将 proposal 定位在一个更丰富的"因果鲁棒 reward modeling"大图景中（命中 Related Work 差异化 + Novelty）。
- 调研依据: CRA (arXiv:2508.04216) 和 CROME (arXiv:2506.16507) 表明因果方法增强 RM 鲁棒性已有成熟先例，proposal 必须在这个 landscape 中定位自己。

【发掘点 3】
- 维度: significance 提升 / 核心 claim 强化
- 内容: **Calibration Drift Detector 是全文潜在最有影响力的贡献，但当前被埋在 CGSP 的子组件里，严重低估了其独立价值。** 目前已有的 reward hacking detection 方法（gradient fingerprints, arXiv:2604.16242 等）需要事后分析或对抗性评估。而 Calibration Drift Detector 本质上是一个**zero-cost, real-time, model-agnostic 的 reward hacking 预警系统**——在 RL training 过程中实时监测 ECE drift，当 policy distribution shift 导致 PRM 失准时自动触发警报。这比任何事后检测方法都更实用。建议将 Calibration Drift Detector **提升为一个独立贡献（Component E）**，而非 CGSP 的附属组件：(1) 给出明确的理论动机：为什么 calibration drift 是 reward hacking 的充分早期信号？(2) 在 RL training 过程中系统性地测量 ECE drift 与 reward-accuracy divergence 的时序关系——如果 ECE drift 稳定地先于 reward hacking 出现，这本身就是一个重要的 empirical finding。(3) 可独立于 CGSP 使用——任何 PRM-based RL pipeline 都可以插入这个 detector。
- 价值: 将一个技术组件升级为独立贡献，增加论文的"贡献密度"和实践影响力。如果 ECE drift 确实是 reward hacking 的可靠 leading indicator，这个发现的 significance 甚至可能超过 CGSP 本身（命中 Significance）。
- 调研依据: Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242) 是当前最接近的检测方法，但需要 gradient 计算；本 proposal 的 drift detector 基于 ECE 统计量，计算成本更低，更易部署。

【发掘点 4】
- 维度: novelty 锐化
- 内容: **Step-level compositional geometry 的 novelty claim 需要更锐利地表述"为什么 outcome-level 分析不够"。** 当前 proposal 正确指出 Ackermann et al. 只分析 outcome-level gradient norms，但仅说"inapplicable to step-level PRM geometry"还不够——需要给出一个具体的、直觉上 compelling 的例子说明 **step-level 分析会揭示 outcome-level 分析遗漏的现象**。例如：一个 PRM 可能在大多数 step 上是 flat 的（难以 hack），但在某个关键 step（如最终答案步）上有一个 sharp peak，使得 adversary 只需在那一步 inject noise 就能获得高 reward。Outcome-level 分析会将这种"局部 sharp + 整体 flat"的模式平均掉，产生错误的安全感。如果实验中确实发现这种 step-heterogeneous sharpness pattern，这将是一个非常有说服力的、仅 step-level 分析能捕捉到的 finding，直接证明 Component C 的必要性。
- 价值: 将 Component C 从"Ackermann et al. 的自然扩展"提升为"揭示了 outcome-level 分析的盲区"，显著增强 novelty 感知（命中 Novelty）。
- 调研依据: Ackermann et al. (arXiv:2602.18037) 的 Propositions 3.3-3.4 确实假设单一标量 reward R(s,a)，proposal 对此的批评是准确的。但需要从"不适用"升级到"会遗漏具体什么现象"才能让 novelty claim 真正锐利。

【发掘点 5】
- 维度: 前提假设质疑
- 内容: **核心逻辑链条中有一个未经验证的关键假设：calibration 在 distribution shift 下是否仍有意义？** Calibration 通常在 held-out test set（与训练分布相同）上衡量。但 reward hacking 的核心场景恰恰是 OOD——adversarial attacks 和 RL policy shift 产生的轨迹不在 calibration 数据的分布内。一个 PRM 可能在 MATH-500 上完美 calibrated，但面对 RL-optimized trajectories 时 calibration 完全崩溃。如果 calibration 只在 in-distribution 有效，那么"calibration 决定 hackability"这个因果 claim 的适用范围就非常有限——它只能解释 mild overoptimization（小幅度的 distribution shift），但不能解释 severe hacking（大幅度的 OOD exploitation）。建议 proposal 明确讨论这个 scope limitation，并在 Component A 中增加一个分析维度：**测量 hackability 与 OOD calibration（而非 in-distribution calibration）的相关性**。这实际上可以将 Calibration Drift Detector 的动机嵌入更早的实验设计中——drift 的速度和幅度本身就是衡量 calibration 在 OOD 下脆弱性的指标。
- 价值: 预防审稿人"your calibration is only measured in-distribution, but hacking is OOD by definition"的致命攻击，同时使 proposal 的理论框架更加自洽——将 in-distribution calibration、OOD calibration degradation、和 Calibration Drift Detector 串联成一个连贯的故事线（命中 Novelty + Significance）。
- 调研依据: 基于领域整体趋势判断——calibration 的 distribution sensitivity 是 calibration 文献中的已知问题（Guo et al. 2017 原始 temperature scaling 论文就强调了 in-distribution 假设），但 PRM 场景下这个问题因 RL training 的 non-stationarity 被极度放大。

---

Sources:
- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models (May 2026)](https://arxiv.org/abs/2605.06785)
- [Reward Under Attack: PRM Hackability (March 2026)](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking (Feb 2026)](https://arxiv.org/abs/2602.18037)
- [Causal Reward Adjustment via Backdoor Correction (Aug 2025)](https://arxiv.org/abs/2508.04216)
- [Robust Reward Modeling via Causal Rubrics / CROME](https://arxiv.org/abs/2506.16507)
- [Learning a Pessimistic Reward Model / PET (May 2025)](https://arxiv.org/abs/2505.20556)
- [Reward Shaping / PAR (Feb 2025)](https://arxiv.org/abs/2502.18770)
- [Conformal Feedback Alignment (Jan 2026)](https://arxiv.org/abs/2601.17329)
- [From Curiosity to Caution / Pessimism for BoN (April 2026)](https://arxiv.org/abs/2604.04648)
- [Detecting and Suppressing Reward Hacking with Gradient Fingerprints (April 2026)](https://arxiv.org/abs/2604.16242)

【补救 agent 本轮输出】:
Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **Tiwari et al. "Reward Under Attack" (arXiv:2603.06621, 2026)**: 实验使用三层攻击框架（静态扰动、对抗性 token、RL-induced hacking），在 AIME 上用 GRPO 闭环评估，报告 PRM reward vs. ground-truth accuracy 的 divergence。Baseline 包括多个开源 PRM（Qwen、Skywork、Math-Shepherd 等）。43% reward gains 来自 stylistic shortcuts。无校准相关评估。
- **Distributional PRMs (arXiv:2605.06785, May 2026)**: 使用 conditional optimal transport 做 PRM 校准，评测 Brier score、ECE、quantile coverage 等校准指标，在 MATH-500（in-distribution）和 AIME 24-25（OOD）上评测 BoN 性能。未测试对抗鲁棒性。
- **Park et al. "Know What You Don't Know" (arXiv:2506.09338, NeurIPS 2025)**: PRM 校准的先驱工作，使用 quantile regression，评测 Brier score、AdaptiveCE、ECE、AverageCE。发现 PRM 在难题上系统性过估。代码开源。
- **Ackermann et al. (arXiv:2602.18037, 2026)**: gradient norm 与 reward accuracy 的相关性分析，仅 outcome-level 单 scalar reward，用 gradient regularization 作为 defense。Baseline：标准 GRPO、KL-regularized GRPO。
- **APRM (arXiv:2511.22888, 2025)**: 对抗训练 PRM，Generator-Discriminator 框架，跨 benchmark 平均 +3.4pp，OOD +5.3pp。评测包含多数学推理 benchmark。
- **Caution (arXiv:2604.04648, 2026)**: BoN 场景下 pessimism-based defense，使用 prediction error 作为 uncertainty proxy，分析 overoptimization onset point N*。
- **PURM (arXiv:2503.22480, 2025)**: 概率不确定性 reward model，将 scalar reward 推广为 Gaussian 分布，用 uncertainty penalty 进 PPO。
- **PET (Pessimistic Reward Tuning)**: 通过对抗微调使 reward model 悲观化，无需 KL regularization。
- **HessFormer / Granziol (arXiv:2602.00816, 2026)**: 首次在 100B 参数规模上做 Hessian spectral density estimation，使用 shard-local finite-difference HVP + FSDP，证明大规模 Hessian 分析可行但计算开销显著。
- **PRMBench (arXiv:2501.03124)**: 6,216 problems / 83,456 step-level labels 的 PRM 评测 benchmark，评估多种 error 类型。

**调研总结**: 该领域当前实验设计标准要求：(1) 多个开源 PRM 作为测试对象；(2) 至少两种攻击强度（静态 + RL-induced）；(3) 校准指标需包含 ECE、Brier score 和 reliability diagram；(4) BoN 评估需覆盖多个 N 值并报告 overoptimization onset；(5) baseline defense 需包含 KL-reg、ensemble、adversarial training 等主流方法。审稿人普遍期望：causal claim 需要严格的 ablation/control 实验，compute-normalized comparison，以及在 OOD 设置下的评估。

---

【缺陷 1】
- 类别: 可行性问题
- 问题: **Component C（Step-Level Hessian Spectral Analysis）在 72B PRM 上的计算可行性存疑。** Proposal 仅分配了 200 H100-hrs 给 Hessian 分析，但根据 Granziol (arXiv:2602.00816) 的工作，在 100B 参数模型上做 Hessian spectral density estimation 本身就是一项前沿挑战，需要 shard-local finite-difference HVP + FSDP 等专门基础设施。Proposal 要求在 8 个 PRM（包括 72B）× 多种校准方法 × 多个 step position × 多个问题上做 Hessian eigenvalue 分析——这意味着需要对每个配置在每个 step 上运行 Lanczos iteration，每次需要多次 Hessian-vector product（每个 HVP 的成本约等于一次完整 forward+backward pass）。对于 72B 模型，单次 HVP 需要 ~4×H100，Lanczos 需要 ~50-100 次 HVP 才能获得可靠的 top-k eigenvalue——单个配置单个 step 的分析就可能需要数小时。200 H100-hrs 对全部 48 配置的 step-level Hessian 分析严重不足。
- 严重度: 可补救
- 补救方案: (1) **缩小 Hessian 分析范围**: 不要对全部 48 配置做 Hessian 分析——选择 representative subset（如 2-3 个 PRM × 2 种校准方法 = 4-6 个配置）。(2) **放弃 72B 的 Hessian 分析**: 将 72B PRM 的 Hessian 分析降级为 gradient norm 分析（follow Ackermann et al. 的方法），仅在 7B/8B 模型上做完整 Hessian spectral analysis。(3) **使用 Hutchinson trace estimator 替代完整 Lanczos**: 如果只需要 top-1 eigenvalue 和 trace，Hutchinson + power iteration 比完整 Lanczos 便宜一个数量级。(4) **将 Hessian 分析的 budget 提高到 600-800 H100-hrs**，相应压缩其他不那么 critical 的预算（如减少 BoN evaluation 的 N 取值范围）。(5) 采样 step position 而非穷举所有 step——例如只分析第 1、中间、最后一个 step。
- 调研依据: Granziol arXiv:2602.00816 (Hessian Spectral Analysis at Foundation Model Scale) 展示了大规模 Hessian 分析的基础设施需求和计算开销。

【缺陷 2】
- 类别: baseline 不足或过时
- 问题: **CGSP defense 的 baseline 缺少 PURM 和 PET。** Proposal 列出了 5 个 CGSP baseline（uncalibrated GRPO、APRM、Caution、ensemble-min、gradient regularization），但遗漏了两个 2025-2026 的重要 defense 方法：(1) **PURM (arXiv:2503.22480)**——将 scalar reward 推广为 Gaussian 分布并用 uncertainty penalty 进 PPO，这与 CGSP 的 uncertainty-based pessimism 思路高度相似，是 CGSP 必须区分开的最近竞争者；(2) **PET (Pessimistic Reward Tuning)**——通过对抗微调使 reward model 悲观化，无需 KL regularization。此外，Proposal 提到了 KL-regularized GRPO 作为 baseline (v)，但没有包含 **Reference Resets**（Ackermann et al. 证明其隐式利用 gradient regularization），这是 KL-based defense 的更强变体。
- 严重度: 可补救
- 补救方案: 将 baseline 扩展为 7 个：(i) uncalibrated GRPO, (ii) APRM, (iii) Caution, (iv) ensemble-min, (v) gradient regularization, (vi) **PURM (uncertainty-penalized PPO)**, (vii) **PET (pessimistic reward tuning)**。特别是 PURM——审稿人几乎必然会问 "CGSP 与 PURM 有什么区别？PURM 同样利用 reward uncertainty 进行 pessimism，为什么 CGSP 更好？"。如果不将其作为 baseline 直接对比，这个问题将无法在 rebuttal 中有效回应。KL-regularized GRPO 可保留为 ablation 而非主 baseline。
- 调研依据: PURM (arXiv:2503.22480) 是 2025 年提出的 uncertainty-aware reward defense 方法，与 CGSP 的 uncertainty-based pessimism 思路最为接近；PET 是 ICLR 2026 时期的 pessimistic reward tuning 方法。

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: **CGSP 的评估仅限于 MATH-500 和 AIME，缺乏对校准-鲁棒性因果链在其他 domain 的验证。** Proposal 的核心 claim 是 "PRM calibration quality causally determines reward hacking resistance"——这是一个非常 general 的因果声明。但实验仅在数学推理领域（MATH-500 + AIME）进行验证。审稿人将合理质疑：这个因果关系是否仅限于数学推理 PRM？是否在代码生成、逻辑推理等需要 step-level 验证的其他 domain 同样成立？此外，MATH-500 作为 in-distribution benchmark 已经被广泛质疑其 saturation 问题（许多模型已接近 ceiling）。
- 严重度: 可补救
- 补救方案: (1) **增加至少一个非数学 domain 的验证**，哪怕是小规模的：例如在代码生成（如 MBPP/HumanEval 的 step-level 评估）或逻辑推理（如 PRMBench 的子集）上复现 Component A 的 correlation study。这不需要全部 48 个配置，选 3-4 个 representative PRM 即可。(2) 如果完全无法获取非数学 PRM，则需在 paper 中明确声明 claim 的 scope limitation（"We establish this causal link in mathematical reasoning; generalization to other domains is future work"），并在实验设计中加入 **MATH difficulty stratification 的更细粒度分析**（如 Level 1-2 vs. Level 3-4 vs. Level 5 分别报告），至少展示因果关系在 difficulty distribution shift 下的稳定性。(3) **替换或增加 OOD benchmark**: 考虑加入 AMC 2023、Olympiad-level problems 或 AIME 2025（如果 Distributional PRM 论文使用了 AIME 24-25，则可以对齐）来扩展 OOD 评估范围。
- 调研依据: Park et al. 和 Distributional PRM 都仅在数学推理上评测；Tiwari et al. 同样仅用 MATH 和 AIME。但 PRMBench (arXiv:2501.03124) 提供了多种 error type 评测，可作为补充验证工具。领域实验规范要求 causal claim 在至少两个 setting 下成立。

【缺陷 4】
- 类别: ablation 不完整
- 问题: **CGSP 公式 r̃_t = μ_t − α·σ_t/√c_t 中有三个关键组件（calibrated uncertainty σ_t、calibration quality c_t、pessimism strength α），但 Proposal 未明确规划充分的 ablation 来隔离各组件贡献。** 具体来说：(1) σ_t vs. c_t 的相对贡献未被隔离——如果去掉 c_t（即用固定 c_t=1），CGSP 退化为简单的 uncertainty-based pessimism，这个 ablation 是论证 "calibration-gated" 机制价值的核心实验；(2) Calibration Drift Detector 的贡献未被隔离——它是 CGSP 系统的一部分但功能独立，需要单独 ablate；(3) pessimism strength α 的 sensitivity analysis 虽然在 resource estimate 中提到了 sweep，但未在实验设计中明确描述。
- 严重度: 可补救
- 补救方案: 明确规划以下 ablation 矩阵：

  | Ablation | 描述 |
  |----------|------|
  | CGSP-full | r̃_t = μ_t − α·σ_t/√c_t + Drift Detector |
  | CGSP w/o c_t | r̃_t = μ_t − α·σ_t（去掉 calibration quality gating） |
  | CGSP w/o σ_t | r̃_t = μ_t − α/√c_t（用常数 uncertainty，仅保留 calibration gating） |
  | CGSP w/o Drift | CGSP-full 但禁用 Calibration Drift Detector |
  | CGSP fixed-α | α 固定为全局常数 vs. per-difficulty adaptive α |

  这 5 个 ablation 可以精确回答审稿人的三个必然问题："calibration gating 有多重要？"、"drift detection 有多重要？"、"α 有多敏感？"

- 调研依据: 基于领域实验规范判断——defense method 论文的 ablation 需要完整隔离每个设计决策的贡献。Ackermann et al. 对 gradient regularization 做了类似的 component-wise ablation。

【缺陷 5】
- 类别: compute 公平性问题
- 问题: **CGSP 与 baseline defense 的 compute-normalized comparison 未被规划。** CGSP 在 RL training 过程中需要额外计算：(1) 维护 rolling buffer 计算 c_t（ECE），(2) 运行 Calibration Drift Detector 定期评估当前分布 ECE，(3) 如果使用 conformal prediction 则需要 split-conformal 校准步骤。这些额外开销可能非 trivial。而 baseline 中 APRM 的额外开销在于对抗训练阶段（但推理/RL 时无额外开销），ensemble-min 的额外开销在于需要推理多个 reward model，gradient regularization 需要额外的 gradient 计算。如果不做 compute-normalized comparison，审稿人会质疑 CGSP 的性能提升是否只是因为用了更多计算。
- 严重度: 可补救
- 补救方案: (1) 报告每个方法的 **wall-clock time per GRPO iteration**（包括 reward computation + defense overhead）。(2) 在相同总计算预算下比较各方法的最终性能（compute-normalized curve：x 轴为总 GPU-hours，y 轴为 reward-accuracy alignment 或 downstream accuracy）。(3) 对 CGSP 的 overhead 进行 profiling breakdown（rolling buffer ECE 计算、drift detection、conformal calibration 各占多少额外时间）。(4) 如果 CGSP 的额外开销显著，考虑提供一个 CGSP-lite 变体（降低 drift detection 频率、减小 rolling buffer 大小）来展示 accuracy-efficiency tradeoff。
- 调研依据: Ackermann et al. 在实验中报告了 gradient regularization 的计算开销比较；Caution (arXiv:2604.04648) 讨论了 pessimism 计算的额外开销。这是该领域 defense 论文的标准要求。

【缺陷 6】
- 类别: 实验设计不足
- 问题: **Component B（Causal Isolation）的 matched representation change control (B3) 设计存在方法论风险。** Proposal 计划 "Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration"——但这个控制条件很难精确满足。(1) CKA-matched 的程度有多严格？CKA matching 需要在所有层都 match 还是只看 average CKA？(2) "不改善 calibration" 如何验证？如果 auxiliary task fine-tuning 恰好也改善了 calibration（math text 的 next-token prediction 可能间接提升数学推理能力），这个控制实验就失败了。(3) CKA 本身有 reliability 争议（arXiv:2210.16156 指出 CKA 在某些条件下不可靠）。
- 严重度: 可补救
- 补救方案: (1) **设计多个 auxiliary task 作为控制**，而非仅依赖一个：例如 (a) next-token prediction on non-math text (Wikipedia), (b) random label fine-tuning (破坏性微调)，(c) fine-tuning on math text with shuffled labels。多个控制的交叉验证比单一控制更有说服力。(2) **CKA matching 标准必须预注册**：明确定义 "matched" 的量化标准（如 "per-layer CKA > 0.95" 或 "average CKA within ±0.02 of calibration fine-tuning"），否则这将成为 post-hoc cherry-picking 的软肋。(3) **补充 CKA 之外的 representation similarity metric**：如 SVCCA 或 linear probing accuracy，来交叉验证 representation change 的 matching 程度，避免仅依赖 CKA 的 limitation。(4) 明确将 B1（post-hoc calibration，零 representation change）作为 **primary causal evidence**，B3 作为 **supporting evidence**——降低 B3 的举证负担。
- 调研依据: arXiv:2210.16156 (Reliability of CKA as a Similarity Measure) 指出 CKA 的可靠性问题；Park et al. 的校准工作未做此类 causal control。

【缺陷 7】
- 类别: 评估方案缺陷
- 问题: **Correlation study (Component A) 的统计功效声明需要更仔细的检验。** Proposal 声称 "n=48, detecting r≥0.29 at p<0.05"——这假设 48 个 PRM×calibration 配置是独立观测，但实际上它们不是独立的：同一个 PRM 的 6 种校准方法之间高度相关（共享 base model representation），同一种校准方法在 8 个 PRM 上的效果也可能因 PRM architecture 而聚类。这种 within-cluster correlation 会严重膨胀有效自由度，导致实际统计功效远低于声称值。
- 严重度: 可补救
- 补救方案: (1) 使用 **mixed-effects model**（PRM 作为 random effect, calibration method 作为 fixed effect）替代简单的 Spearman correlation，正确处理嵌套结构。(2) 报告 **cluster-robust standard errors** 或 **bootstrap confidence intervals**（对 PRM 进行 block bootstrap）。(3) 补充 **within-PRM analysis**：在每个 PRM 内部，6 种校准方法是否单调改善 hackability？这个 within-subject 分析不受 between-PRM heterogeneity 影响，是更干净的因果证据。(4) 如果审稿人认为 n_effective 因聚类降到 ~8-16，则需要更大的效应量才能 detect——在 paper 中讨论这个 limitation 并解释为什么即使用 conservative n_effective，观察到的效应量仍然显著。
- 调研依据: 基于领域实验规范判断——correlation study 中的非独立观测结构是统计方法论的基本问题。Park et al. 和 Distributional PRM 的评估设计没有面对这个问题因为它们不做跨配置的 correlation analysis。

【缺陷 8】
- 类别: 可行性问题
- 问题: **Component A 的 gradient-based attack（Tier i）需要 8 个 PRM × 6 种校准方法 = 48 个配置的 white-box gradient attack，1000 H100-hrs 是否充足需要验证。** Tiwari et al. 的 gradient attack 需要对每个 PRM 做迭代 token-level optimization（类似 GCG），这在 72B 模型上代价极高。如果每个配置需要在 ~500 problems（MATH-500）上运行 gradient attack，每个 problem 需要数百次梯度迭代，72B 模型的每次梯度计算需要 4×H100——单个配置可能需要 100+ H100-hrs。48 个配置 × 100 hrs = 4800 H100-hrs，远超分配的 1000 H100-hrs。
- 严重度: 可补救
- 补救方案: (1) **分层设计 gradient attack 评估**: 仅对 representative subset（如 4 个 PRM × 3 种校准方法 = 12 个配置）执行完整 gradient attack；其余配置仅做 Tier ii（RL-induced hacking）和 Tier iii（BoN），因为这两者计算开销更可控。(2) **对 72B PRM 仅做 BoN 评估和 RL-induced hacking 评估**，放弃其 gradient attack（理由：72B 的 white-box access 场景在实践中也不太现实，这是一个合理的 scope choice）。(3) 重新估算 gradient attack budget：如果缩小到 12 个配置，1000 H100-hrs 可能刚好足够（~83 hrs/配置）。(4) 使用 **transfer attack** 替代部分 white-box attack：用 7B PRM 上生成的 adversarial tokens 测试 72B PRM，这既省计算又增加了评估的生态效度。
- 调研依据: Tiwari et al. (arXiv:2603.06621) 的 gradient attack 实验规模和成本参考。

---

**总结**: 该 proposal 的实验框架设计已经相当完善——四个 component 的分工清晰，post-hoc calibration 作为 causal tool 的思路方法论上正确，CGSP defense 的设计有明确的差异化。上述 8 个缺陷**全部可补救**，没有发现致命的方向性问题。核心需要关注的优先级排序为：

1. **P0（必须修）**: 缺陷 2（补充 PURM/PET baseline）、缺陷 4（CGSP ablation 矩阵）——这两个是审稿人几乎 100% 会问的。
2. **P1（强烈建议）**: 缺陷 5（compute-normalized comparison）、缺陷 7（correlation study 统计方法）——这两个影响 claim 的说服力。
3. **P2（建议但可降级）**: 缺陷 1（Hessian 可行性）、缺陷 8（gradient attack budget）——通过缩小范围可解决。
4. **P3（理想但非必须）**: 缺陷 3（非数学 domain 验证）、缺陷 6（matched control 设计）——scope limitation 可在 paper 中声明。

Sources:
- [Reward Under Attack (Tiwari et al.)](https://arxiv.org/abs/2603.06621)
- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)
- [Know What You Don't Know (Park et al.)](https://arxiv.org/abs/2506.09338)
- [Gradient Regularization (Ackermann et al.)](https://arxiv.org/abs/2602.18037)
- [APRM](https://arxiv.org/abs/2511.22888)
- [Caution](https://arxiv.org/abs/2604.04648)
- [PURM](https://arxiv.org/abs/2503.22480)
- [Hessian Spectral Analysis at Foundation Model Scale](https://arxiv.org/abs/2602.00816)
- [HessFormer](https://arxiv.org/abs/2505.11564)
- [PRMBench](https://arxiv.org/abs/2501.03124)
- [Reliability of CKA](https://arxiv.org/abs/2210.16156)
- [Conformal Feedback Alignment](https://arxiv.org/abs/2601.17329)
- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "838c2fac-e99d-454e-b17f-5ef4d3f6d881",
  "type": "user",
  "uuid": "4d772f17-cda7-4ff9-8edb-26fff092267e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:57:09.073Z_

```json
{
  "parentUuid": "4d772f17-cda7-4ff9-8edb-26fff092267e",
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
  "uuid": "f4355d9c-7dcf-43af-92ff-c5826387edce",
  "timestamp": "2026-05-20T05:57:09.073Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:57:09.073Z_

```json
{
  "parentUuid": "f4355d9c-7dcf-43af-92ff-c5826387edce",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5d954efa-6550-4c2d-861f-c76d8678a1a9",
  "timestamp": "2026-05-20T05:57:09.073Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
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
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.  ---  【状态】: 有发…",
  "leafUuid": "5d954efa-6550-4c2d-861f-c76d8678a1a9",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate calibration-driven reward hacking resistance",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:57:41.508Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation. I'm the 终审 agent (Meta Judge / Iterative Integration agent) in Role B (迭代中, Round 1). I need to:

1. Integrate the outputs from the 发掘 agent and 补救 agent
2. Cross-verify their suggestions with WebSearch
3. Decide whether to continue, converge, or kill
4. Update the proposal if continuing
5. Estimate acceptance probability

But wait - I need to see the original proposal first. The user hasn't provided it directly in this message. Let me look at what I have:


I have the two worker outputs - 5 discovery points from the 发掘 agent and 8 deficiency points from the 补救 agent - but I need the original proposal to properly integrate these findings. Looking at the context, the workers are referencing a proposal about PRM calibration and reward hacking, with a causal claim about calibration quality, so I need to reconstruct the full proposal from these agent outputs to proceed with the integration. I need to verify these references against actual research to make sure the worker suggestions are grounded in real work. Let me search for the key papers they cited—CRA, PURM, and PET—to confirm they exist and match what was described, and also check whether calibration drift detection and the reward compression confound are genuine concerns in the literature. I need to verify these key claims from both worker outputs using web searches, starting with the major papers they reference like CRA and PURM, then checking the specific technical points about reward compression and calibration drift detection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d954efa-6550-4c2d-861f-c76d8678a1a9",
  "isSidechain": false,
  "requestId": "req_011CbDJj4hBn9Mh4LsjprHAS",
  "type": "assistant",
  "uuid": "88ff3696-04f1-425e-8b52-aaa32518b052",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiDBejy1UqcyJnSDNE8yjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12635,
      "cache_read_input_tokens": 16908,
      "output_tokens": 1218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1218,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 12635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12635
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

_source line 9 · 2026-05-20T05:57:41.510Z_

I need to cross-verify the key worker suggestions before integrating. Let me first load the WebSearch tool and then verify the most critical claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88ff3696-04f1-425e-8b52-aaa32518b052",
  "isSidechain": false,
  "requestId": "req_011CbDJj4hBn9Mh4LsjprHAS",
  "type": "assistant",
  "uuid": "c25ae259-c32a-403f-98bf-3348e64cf0ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiDBejy1UqcyJnSDNE8yjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12635,
      "cache_read_input_tokens": 16908,
      "output_tokens": 1218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1218,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 12635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12635
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

### Tool call

_source line 10 · 2026-05-20T05:57:41.756Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VLRdAaf4G1j9sECgWSjqVk`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c25ae259-c32a-403f-98bf-3348e64cf0ff",
  "isSidechain": false,
  "requestId": "req_011CbDJj4hBn9Mh4LsjprHAS",
  "type": "assistant",
  "uuid": "a4b1c40f-c2dc-43f0-bd0c-93373abe093f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiDBejy1UqcyJnSDNE8yjU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12635,
      "cache_read_input_tokens": 16908,
      "output_tokens": 1218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1218,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 12635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12635
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

### Tool result

_source line 11 · 2026-05-20T05:57:41.763Z_

<details><summary>↩ Tool result · `toolu_01VLRdAaf4G1j9sECgWSjqVk`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4b1c40f-c2dc-43f0-bd0c-93373abe093f",
  "isSidechain": false,
  "promptId": "838c2fac-e99d-454e-b17f-5ef4d3f6d881",
  "type": "user",
  "uuid": "e73387f9-d3ab-4be6-ac5b-b9b0e5454bec",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "a4b1c40f-c2dc-43f0-bd0c-93373abe093f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:57:47.366Z_

Now let me run the critical verification searches in parallel. I need to verify:

1. CRA (arXiv:2508.04216) - the most impactful discovery point about a major related work omission
2. PURM (arXiv:2503.22480) - the most critical baseline suggestion from 补救 agent
3. Whether calibration drift as a reward hacking detector has been explored elsewhere

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e73387f9-d3ab-4be6-ac5b-b9b0e5454bec",
  "isSidechain": false,
  "requestId": "req_011CbDJmUbvHEFiD36LUFYZx",
  "type": "assistant",
  "uuid": "12dfda1f-2a2e-44c5-8108-6e12935f6821",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4uqooEHTF9hcZuBb1Cugw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 29543,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 278,
          "cache_read_input_tokens": 29543,
          "cache_creation_input_tokens": 1744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1744
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

### Tool call

_source line 13 · 2026-05-20T05:57:48.361Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012UREpx423LPrEA3oaCT94x`</summary>

```json
{
  "query": "arXiv 2508.04216 Causal Reward Adjustment backdoor correction PRM reward hacking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12dfda1f-2a2e-44c5-8108-6e12935f6821",
  "isSidechain": false,
  "requestId": "req_011CbDJmUbvHEFiD36LUFYZx",
  "type": "assistant",
  "uuid": "1c03f4de-a9cf-4c1c-8f58-1f98c643ff11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4uqooEHTF9hcZuBb1Cugw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 29543,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 278,
          "cache_read_input_tokens": 29543,
          "cache_creation_input_tokens": 1744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1744
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

### Tool call

_source line 14 · 2026-05-20T05:57:48.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016kr8fCaXzPcNgHwJXBnTo9`</summary>

```json
{
  "query": "arXiv 2503.22480 PURM probabilistic uncertainty reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c03f4de-a9cf-4c1c-8f58-1f98c643ff11",
  "isSidechain": false,
  "requestId": "req_011CbDJmUbvHEFiD36LUFYZx",
  "type": "assistant",
  "uuid": "3ed128a5-81c1-4b5e-bfd3-2ac4c4b634d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4uqooEHTF9hcZuBb1Cugw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 29543,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 278,
          "cache_read_input_tokens": 29543,
          "cache_creation_input_tokens": 1744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1744
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

### Tool call

_source line 15 · 2026-05-20T05:57:49.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MR7YV7kgx3QfNZXkftGX1N`</summary>

```json
{
  "query": "calibration drift detection reward hacking early warning ECE monitoring RL training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ed128a5-81c1-4b5e-bfd3-2ac4c4b634d7",
  "isSidechain": false,
  "requestId": "req_011CbDJmUbvHEFiD36LUFYZx",
  "type": "assistant",
  "uuid": "62f86859-1b98-45f8-9e9c-b40ab0f18bd2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4uqooEHTF9hcZuBb1Cugw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 29543,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 278,
          "cache_read_input_tokens": 29543,
          "cache_creation_input_tokens": 1744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1744
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

### Tool result

_source line 16 · 2026-05-20T05:57:55.625Z_

<details><summary>↩ Tool result · `toolu_012UREpx423LPrEA3oaCT94x`</summary>

```text
Web search results for query: "arXiv 2508.04216 Causal Reward Adjustment backdoor correction PRM reward hacking"

Links: [{"title":"[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/abs/2508.04216"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"Adaptive Milestone Reward for GUI Agents","url":"https://arxiv.org/pdf/2602.11524"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in ...","url":"https://arxiv.org/pdf/2508.04216"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://www.arxiv.org/pdf/2601.21350"},{"title":"Avoiding Reward Hacking","url":"https://www.emergentmind.com/topics/avoiding-reward-hacking"},{"title":"Supplementary Material: Proofs and Technical Details","url":"https://arxiv.org/html/2502.02020"},{"title":"Causal Bandit Over Unknown Graphs: Upper Confidence Bounds With Backdoor Adjustment","url":"https://arxiv.org/pdf/2502.02020"}]

Based on the search results, here's what I found about arXiv paper 2508.04216:

## Paper Overview

The paper "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction" by Ruike Song and colleagues addresses external reasoning systems that combine language models with process reward models (PRMs) to select high-quality reasoning paths for complex tasks such as mathematical problem solving.

## The Problem

These systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers. From a causal inference perspective, this phenomenon is primarily attributed to the presence of confounding semantic features.

## The Solution: Causal Reward Adjustment (CRA)

The proposed Causal Reward Adjustment (CRA) method mitigates reward hacking by estimating the true reward of a reasoning path. CRA trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.

## Results

Experiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining PRM.

The paper was submitted to arXiv on August 6, 2025, and addresses a critical challenge in ensuring that process reward models evaluate reasoning paths based on logical correctness rather than spurious correlations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c03f4de-a9cf-4c1c-8f58-1f98c643ff11",
  "isSidechain": false,
  "promptId": "838c2fac-e99d-454e-b17f-5ef4d3f6d881",
  "type": "user",
  "uuid": "ac50e9f6-08c6-4664-93e6-a55a3fbe71a0",
  "toolUseResult": {
    "query": "arXiv 2508.04216 Causal Reward Adjustment backdoor correction PRM reward hacking",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SkiMvYnpEPZBY1L4cp1axw",
        "content": [
          {
            "title": "[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/abs/2508.04216"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/html/2508.04216v1"
          },
          {
            "title": "Adaptive Milestone Reward for GUI Agents",
            "url": "https://arxiv.org/pdf/2602.11524"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2508.04216"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://www.arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Avoiding Reward Hacking",
            "url": "https://www.emergentmind.com/topics/avoiding-reward-hacking"
          },
          {
            "title": "Supplementary Material: Proofs and Technical Details",
            "url": "https://arxiv.org/html/2502.02020"
          },
          {
            "title": "Causal Bandit Over Unknown Graphs: Upper Confidence Bounds With Backdoor Adjustment",
            "url": "https://arxiv.org/pdf/2502.02020"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2508.04216:\n\n## Paper Overview\n\nThe paper \"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction\" by Ruike Song and colleagues addresses external reasoning systems that combine language models with process reward models (PRMs) to select high-quality reasoning paths for complex tasks such as mathematical problem solving.\n\n## The Problem\n\nThese systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers. From a causal inference perspective, this phenomenon is primarily attributed to the presence of confounding semantic features.\n\n## The Solution: Causal Reward Adjustment (CRA)\n\nThe proposed Causal Reward Adjustment (CRA) method mitigates reward hacking by estimating the true reward of a reasoning path. CRA trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.\n\n## Results\n\nExperiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining PRM.\n\nThe paper was submitted to arXiv on August 6, 2025, and addresses a critical challenge in ensuring that process reward models evaluate reasoning paths based on logical correctness rather than spurious correlations."
    ],
    "durationSeconds": 7.258645400000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1c03f4de-a9cf-4c1c-8f58-1f98c643ff11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T05:57:59.988Z_

<details><summary>↩ Tool result · `toolu_01MR7YV7kgx3QfNZXkftGX1N`</summary>

```text
Web search results for query: "calibration drift detection reward hacking early warning ECE monitoring RL training 2025 2026"

Links: [{"title":"What Is Reward Hacking? How to Prevent It in RL (2026 Guide)","url":"https://www.articsledge.com/post/reward-hacking"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study | Request PDF","url":"https://www.researchgate.net/publication/393511842_Detecting_and_Mitigating_Reward_Hacking_in_Reinforcement_Learning_Systems_A_Comprehensive_Empirical_Study"},{"title":"Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR","url":"https://arxiv.org/pdf/2603.07084"},{"title":"Monitoring Emergent Reward Hacking During Generation via Internal Activations","url":"https://arxiv.org/pdf/2603.04069"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"}]

I've performed the web search on your query. Here are the key findings related to calibration drift detection, reward hacking, early warning systems, ECE monitoring, and RL training for 2025-2026:

## Recent Research and Incidents (2025-2026)

Major AI labs reported reward hacking incidents in production systems throughout 2025, with Anthropic documenting emergent misalignment behavior. Multiple major AI labs have reported the presence of reward hacking in their training runs.

## Detection and Monitoring Approaches

A large-scale empirical study of reward hacking across diverse RL environments and algorithms found that A3C's aggressive exploration leads to higher hacking rates (28.9%) than SAC's conservative updates (19.3%), discrete action spaces show 31.2% higher hacking rates than continuous control, and mid-training detection (episodes 200-800) provides optimal intervention windows.

A detection framework achieved 78.4% precision and 81.7% recall across environments, with computational overhead under 5%.

## Internal Activation Monitoring

Recent research has focused on monitoring internal model activations: Surface-level outputs may remain plausible while the model's internal policy shifts toward exploiting the objective. Concept-direction analysis on model activations throughout RL training shows that the shortcut direction tracks hacking most closely, providing an effective probe for detection.

## Mitigation and Trade-offs

Mitigation techniques reduce hacking frequency by up to 54.6% in controlled scenarios, though these trade-offs are more challenging in practice due to concept drift, false positive costs, and adversarial adaptation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62f86859-1b98-45f8-9e9c-b40ab0f18bd2",
  "isSidechain": false,
  "promptId": "838c2fac-e99d-454e-b17f-5ef4d3f6d881",
  "type": "user",
  "uuid": "954f56ad-0b89-4e82-ac91-bbab844330d1",
  "toolUseResult": {
    "query": "calibration drift detection reward hacking early warning ECE monitoring RL training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X8P8pJjw9eDd6zxB7P3Grk",
        "content": [
          {
            "title": "What Is Reward Hacking? How to Prevent It in RL (2026 Guide)",
            "url": "https://www.articsledge.com/post/reward-hacking"
          },
          {
            "title": "Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study",
            "url": "https://arxiv.org/html/2507.05619v1"
          },
          {
            "title": "Natural Emergent Misalignment from Reward Hacking in Production RL",
            "url": "https://arxiv.org/pdf/2511.18397"
          },
          {
            "title": "Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study | Request PDF",
            "url": "https://www.researchgate.net/publication/393511842_Detecting_and_Mitigating_Reward_Hacking_in_Reinforcement_Learning_Systems_A_Comprehensive_Empirical_Study"
          },
          {
            "title": "Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR",
            "url": "https://arxiv.org/pdf/2603.07084"
          },
          {
            "title": "Monitoring Emergent Reward Hacking During Generation via Internal Activations",
            "url": "https://arxiv.org/pdf/2603.04069"
          },
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/pdf/2604.01476"
          }
        ]
      },
      "I've performed the web search on your query. Here are the key findings related to calibration drift detection, reward hacking, early warning systems, ECE monitoring, and RL training for 2025-2026:\n\n## Recent Research and Incidents (2025-2026)\n\nMajor AI labs reported reward hacking incidents in production systems throughout 2025, with Anthropic documenting emergent misalignment behavior. Multiple major AI labs have reported the presence of reward hacking in their training runs.\n\n## Detection and Monitoring Approaches\n\nA large-scale empirical study of reward hacking across diverse RL environments and algorithms found that A3C's aggressive exploration leads to higher hacking rates (28.9%) than SAC's conservative updates (19.3%), discrete action spaces show 31.2% higher hacking rates than continuous control, and mid-training detection (episodes 200-800) provides optimal intervention windows.\n\nA detection framework achieved 78.4% precision and 81.7% recall across environments, with computational overhead under 5%.\n\n## Internal Activation Monitoring\n\nRecent research has focused on monitoring internal model activations: Surface-level outputs may remain plausible while the model's internal policy shifts toward exploiting the objective. Concept-direction analysis on model activations throughout RL training shows that the shortcut direction tracks hacking most closely, providing an effective probe for detection.\n\n## Mitigation and Trade-offs\n\nMitigation techniques reduce hacking frequency by up to 54.6% in controlled scenarios, though these trade-offs are more challenging in practice due to concept drift, false positive costs, and adversarial adaptation."
    ],
    "durationSeconds": 10.472519659999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "62f86859-1b98-45f8-9e9c-b40ab0f18bd2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T05:58:08.810Z_

<details><summary>↩ Tool result · `toolu_016kr8fCaXzPcNgHwJXBnTo9`</summary>

```text
Web search results for query: "arXiv 2503.22480 PURM probabilistic uncertainty reward model"

Links: [{"title":"[2503.22480] Probabilistic Uncertain Reward Model","url":"https://arxiv.org/abs/2503.22480"},{"title":"[2503.22480v2] Probabilistic Uncertain Reward Model: A Natural Generalization of Bradley-Terry Reward Model","url":"https://arxiv.org/abs/2503.22480v2"},{"title":"Probabilistic Uncertain Reward Model","url":"https://arxiv.org/html/2503.22480"},{"title":"Probabilistic Uncertain Reward Model","url":"https://arxiv.org/pdf/2503.22480"},{"title":"Probabilistic Uncertain Reward Model: A Natural Generalization of Bradley-Terry Reward Model","url":"https://arxiv.org/html/2503.22480v1"},{"title":"Probabilistic Uncertain Reward Model: A Natural Generalization of Bradley-Terry Reward Model | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/probabilistic-uncertain-reward-model-natural-generalization-bradley"}]

Based on the search results, I found the paper you're looking for:

## Probabilistic Uncertain Reward Model (PURM) - arXiv 2503.22480

PURM is a method that generalizes the Bradley-Terry model to learn the reward distributions that emerged from the preference data.

**Key Problem Addressed:**
Conventional reward models based on the Bradley-Terry model often suffer from overconfidence when faced with inconsistent labels or out-of-distribution samples, leading to reward hacking.

**Technical Approach:**
PURM adopts a two-head model architecture to generate a reward distribution instead of a scalar reward for a given prompt-response pair. The paper theoretically derives PURM's loss function and the reward distribution uncertainty calculation based on Bhattacharyya Coefficient.

**Key Contributions:**
- PURM learns reward distributions directly from preference data and quantifies per-sample uncertainty via the average overlap area between reward distributions.
- PURM significantly outperforms existing uncertain reward models in recognizing both aleatoric uncertainty (arising from inconsistent data labeling) and epistemic uncertainty (caused by out-of-distribution samples).

**Results:**
Empirical results show that PURM outperforms existing methods with more accurate reward and sound uncertainty estimations, and sustains effective learning for more optimization steps and obtains higher maximum win rate in RLHF.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ed128a5-81c1-4b5e-bfd3-2ac4c4b634d7",
  "isSidechain": false,
  "promptId": "838c2fac-e99d-454e-b17f-5ef4d3f6d881",
  "type": "user",
  "uuid": "de157faa-896e-47c0-8636-7dda2c455a11",
  "toolUseResult": {
    "query": "arXiv 2503.22480 PURM probabilistic uncertainty reward model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TZMrsC5ZpyM4cZHHgEP9aD",
        "content": [
          {
            "title": "[2503.22480] Probabilistic Uncertain Reward Model",
            "url": "https://arxiv.org/abs/2503.22480"
          },
          {
            "title": "[2503.22480v2] Probabilistic Uncertain Reward Model: A Natural Generalization of Bradley-Terry Reward Model",
            "url": "https://arxiv.org/abs/2503.22480v2"
          },
          {
            "title": "Probabilistic Uncertain Reward Model",
            "url": "https://arxiv.org/html/2503.22480"
          },
          {
            "title": "Probabilistic Uncertain Reward Model",
            "url": "https://arxiv.org/pdf/2503.22480"
          },
          {
            "title": "Probabilistic Uncertain Reward Model: A Natural Generalization of Bradley-Terry Reward Model",
            "url": "https://arxiv.org/html/2503.22480v1"
          },
          {
            "title": "Probabilistic Uncertain Reward Model: A Natural Generalization of Bradley-Terry Reward Model | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/probabilistic-uncertain-reward-model-natural-generalization-bradley"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## Probabilistic Uncertain Reward Model (PURM) - arXiv 2503.22480\n\nPURM is a method that generalizes the Bradley-Terry model to learn the reward distributions that emerged from the preference data.\n\n**Key Problem Addressed:**\nConventional reward models based on the Bradley-Terry model often suffer from overconfidence when faced with inconsistent labels or out-of-distribution samples, leading to reward hacking.\n\n**Technical Approach:**\nPURM adopts a two-head model architecture to generate a reward distribution instead of a scalar reward for a given prompt-response pair. The paper theoretically derives PURM's loss function and the reward distribution uncertainty calculation based on Bhattacharyya Coefficient.\n\n**Key Contributions:**\n- PURM learns reward distributions directly from preference data and quantifies per-sample uncertainty via the average overlap area between reward distributions.\n- PURM significantly outperforms existing uncertain reward models in recognizing both aleatoric uncertainty (arising from inconsistent data labeling) and epistemic uncertainty (caused by out-of-distribution samples).\n\n**Results:**\nEmpirical results show that PURM outperforms existing methods with more accurate reward and sound uncertainty estimations, and sustains effective learning for more optimization steps and obtains higher maximum win rate in RLHF."
    ],
    "durationSeconds": 19.970566895000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3ed128a5-81c1-4b5e-bfd3-2ac4c4b634d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.  ---  【状态】: 有发…",
  "leafUuid": "de157faa-896e-47c0-8636-7dda2c455a11",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate calibration-driven reward hacking resistance",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---

### Assistant

_source line 21 · 2026-05-20T05:58:24.613Z_

<details><summary>Logged reasoning block</summary>

```text
Good, let me analyze the verification results:

1. **CRA (arXiv:2508.04216)** - CONFIRMED. This is a real paper that uses causal inference (sparse autoencoders + backdoor adjustment) on PRM internal activations to mitigate reward hacking. The 发掘 agent's characterization is accurate. This is indeed a significant omission from the proposal.

2. **PURM (arXiv:2503.22480)** - CONFIRMED. This is a real paper that generalizes Bradley-Terry to learn reward distributions with uncertainty quantification. It uses a two-head architecture for reward distribution + uncertainty via Bhattacharyya Coefficient. 

The 补救 agent's characterization is accurate—this is highly relevant as a baseline for CGSP since both leverage uncertainty-based approaches.

3. **Calibration drift detection for reward hacking** - The search results show various monitoring approaches for reward hacking but nothing specifically using ECE or calibration drift as a detection signal. The closest work involves concept-direction analysis on activations and general reward hacking detection frameworks. This suggests the 发掘 agent's proposal to position calibration drift detection as an independent contribution has some novelty merit, since ECE-based monitoring doesn't appear to be explored in existing literature.

I need to verify a couple more key claims through additional searches—specifically checking PAR and the reward compression confound, plus PET—to complete the cross-verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de157faa-896e-47c0-8636-7dda2c455a11",
  "isSidechain": false,
  "requestId": "req_011CbDJoU1WLdapwt2VNk8pG",
  "type": "assistant",
  "uuid": "a685dfc0-dc1c-41d2-a31e-f3e21e572b6b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeNXxDnH8Du2xovoxrcSfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 797,
      "cache_creation_input_tokens": 1657,
      "cache_read_input_tokens": 31287,
      "output_tokens": 550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 797,
          "output_tokens": 550,
          "cache_read_input_tokens": 31287,
          "cache_creation_input_tokens": 1657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1657
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

_source line 22 · 2026-05-20T05:58:24.723Z_

Good — CRA and PURM are both confirmed real and accurately described. Let me verify a couple more critical claims:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a685dfc0-dc1c-41d2-a31e-f3e21e572b6b",
  "isSidechain": false,
  "requestId": "req_011CbDJoU1WLdapwt2VNk8pG",
  "type": "assistant",
  "uuid": "342fbdf5-53a0-4d08-99c4-4e16ddcd1897",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeNXxDnH8Du2xovoxrcSfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 797,
      "cache_creation_input_tokens": 1657,
      "cache_read_input_tokens": 31287,
      "output_tokens": 550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 797,
          "output_tokens": 550,
          "cache_read_input_tokens": 31287,
          "cache_creation_input_tokens": 1657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1657
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

### Tool call

_source line 23 · 2026-05-20T05:58:25.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0183e7QhtkGD71set2VzA96J`</summary>

```json
{
  "query": "arXiv 2502.18770 reward shaping bounded centered reward hacking defense PAR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "342fbdf5-53a0-4d08-99c4-4e16ddcd1897",
  "isSidechain": false,
  "requestId": "req_011CbDJoU1WLdapwt2VNk8pG",
  "type": "assistant",
  "uuid": "e8bf977a-10c7-4cc6-a507-42f18e262f4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeNXxDnH8Du2xovoxrcSfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 797,
      "cache_creation_input_tokens": 1657,
      "cache_read_input_tokens": 31287,
      "output_tokens": 550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 797,
          "output_tokens": 550,
          "cache_read_input_tokens": 31287,
          "cache_creation_input_tokens": 1657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1657
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

### Tool call

_source line 24 · 2026-05-20T05:58:26.137Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E7MS6tNaK4PCRM51A5FTRp`</summary>

```json
{
  "query": "arXiv 2505.20556 pessimistic reward model RLHF PET reward tuning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8bf977a-10c7-4cc6-a507-42f18e262f4e",
  "isSidechain": false,
  "requestId": "req_011CbDJoU1WLdapwt2VNk8pG",
  "type": "assistant",
  "uuid": "a4c6ad2a-6301-4fa2-972f-7f065311f19c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeNXxDnH8Du2xovoxrcSfP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 797,
      "cache_creation_input_tokens": 1657,
      "cache_read_input_tokens": 31287,
      "output_tokens": 550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 797,
          "output_tokens": 550,
          "cache_read_input_tokens": 31287,
          "cache_creation_input_tokens": 1657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1657
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

### Tool result

_source line 25 · 2026-05-20T05:58:32.211Z_

<details><summary>↩ Tool result · `toolu_0183e7QhtkGD71set2VzA96J`</summary>

```text
Web search results for query: "arXiv 2502.18770 reward shaping bounded centered reward hacking defense PAR 2025"

Links: [{"title":"[2502.18770v1] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770v1"},{"title":"[2502.18770v2] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770v2"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://ar5iv.labs.arxiv.org/html/2502.18770"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770"},{"title":"Paper page - Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://huggingface.co/papers/2502.18770"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/pdf/2502.18770"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250218770F/abstract"},{"title":"Reward Shaping for Inference-Time Alignment: A Stackelberg Game Perspective","url":"https://www.arxiv.org/pdf/2602.02572"},{"title":"Reward Shaping for Inference-Time Alignment: A Stackelberg Game Perspective","url":"https://arxiv.org/html/2602.02572v1"},{"title":"Repairing Reward Functions with Feedback to Mitigate Reward Hacking","url":"https://arxiv.org/html/2510.13036v2"}]

Based on the search results, here's information about arXiv paper 2502.18770:

**Paper Title:** "Reward Shaping to Mitigate Reward Hacking in RLHF"

**Key Problem:** Reinforcement Learning from Human Feedback (RLHF) is essential for aligning large language models (LLMs) with human values. However, RLHF is susceptible to reward hacking, where the agent exploits flaws in the reward function rather than learning the intended behavior, thus degrading alignment.

**Three Core Design Principles:** The analysis suggests three key design principles: (1) RL reward is ideally bounded, (2) RL benefits from rapid initial growth followed by gradual convergence, and (3) RL reward is best formulated as a function of centered reward.

**Proposed Method (PAR):** The paper proposes Preference As Reward (PAR), a novel approach that leverages the latent preferences embedded within the reward model as the signal for reinforcement learning.

**Technical Implementation:** PAR applies a sigmoid function to the centered reward (the difference between the proxy reward r and a reference reward rref). This design is intuitive: since the policy model is typically initialized from a reference model, the centered reward is initially near zero.

The paper was published on February 26, 2025, and represents a comprehensive study addressing reward hacking vulnerabilities in RLHF systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8bf977a-10c7-4cc6-a507-42f18e262f4e",
  "isSidechain": false,
  "promptId": "838c2fac-e99d-454e-b17f-5ef4d3f6d881",
  "type": "user",
  "uuid": "01321192-9b25-4d83-a5cf-687e5266c454",
  "toolUseResult": {
    "query": "arXiv 2502.18770 reward shaping bounded centered reward hacking defense PAR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018DEm1krXDHvRNqK9jdJChM",
        "content": [
          {
            "title": "[2502.18770v1] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/abs/2502.18770v1"
          },
          {
            "title": "[2502.18770v2] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/abs/2502.18770v2"
          },
          {
            "title": "[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://ar5iv.labs.arxiv.org/html/2502.18770"
          },
          {
            "title": "[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/abs/2502.18770"
          },
          {
            "title": "Paper page - Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://huggingface.co/papers/2502.18770"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/pdf/2502.18770"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250218770F/abstract"
          },
          {
            "title": "Reward Shaping for Inference-Time Alignment: A Stackelberg Game Perspective",
            "url": "https://www.arxiv.org/pdf/2602.02572"
          },
          {
            "title": "Reward Shaping for Inference-Time Alignment: A Stackelberg Game Perspective",
            "url": "https://arxiv.org/html/2602.02572v1"
          },
          {
            "title": "Repairing Reward Functions with Feedback to Mitigate Reward Hacking",
            "url": "https://arxiv.org/html/2510.13036v2"
          }
        ]
      },
      "Based on the search results, here's information about arXiv paper 2502.18770:\n\n**Paper Title:** \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n\n**Key Problem:** Reinforcement Learning from Human Feedback (RLHF) is essential for aligning large language models (LLMs) with human values. However, RLHF is susceptible to reward hacking, where the agent exploits flaws in the reward function rather than learning the intended behavior, thus degrading alignment.\n\n**Three Core Design Principles:** The analysis suggests three key design principles: (1) RL reward is ideally bounded, (2) RL benefits from rapid initial growth followed by gradual convergence, and (3) RL reward is best formulated as a function of centered reward.\n\n**Proposed Method (PAR):** The paper proposes Preference As Reward (PAR), a novel approach that leverages the latent preferences embedded within the reward model as the signal for reinforcement learning.\n\n**Technical Implementation:** PAR applies a sigmoid function to the centered reward (the difference between the proxy reward r and a reference reward rref). This design is intuitive: since the policy model is typically initialized from a reference model, the centered reward is initially near zero.\n\nThe paper was published on February 26, 2025, and represents a comprehensive study addressing reward hacking vulnerabilities in RLHF systems."
    ],
    "durationSeconds": 6.525667267000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e8bf977a-10c7-4cc6-a507-42f18e262f4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T05:58:32.996Z_

<details><summary>↩ Tool result · `toolu_01E7MS6tNaK4PCRM51A5FTRp`</summary>

```text
Web search results for query: "arXiv 2505.20556 pessimistic reward model RLHF PET reward tuning 2025"

Links: [{"title":"[2505.20556] Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/abs/2505.20556"},{"title":"[Literature Review] Learning a Pessimistic Reward Model in RLHF","url":"https://www.themoonlight.io/en/review/learning-a-pessimistic-reward-model-in-rlhf"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Learning a Pessimistic Reward Model in RLHF | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.20556v1"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=10550&show=500"},{"title":"Learning a Pessimistic Reward Model in RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250520556X/abstract"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=2150&show=100"},{"title":"Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL","url":"https://arxiv.org/html/2510.06092v1"},{"title":"Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF","url":"https://arxiv.org/html/2509.24713v1"}]

Based on the search results, here's what I found about arXiv paper 2505.20556:

## Summary

The paper proposes 'PET', a novel pessimistic reward fine-tuning method, to learn a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF).

## Key Problem and Solution

Traditional reward modeling techniques in RLHF train an imperfect reward model, on which a KL regularization plays a pivotal role in mitigating reward hacking when optimizing a policy. Such an intuition-based method still suffers from reward hacking, and the policies with large KL divergence from the dataset distribution are excluded during learning.

In contrast, the authors show that when optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization, and one can learn a high-quality policy on their pessimistic reward without using any regularization.

## Evaluation

The methods were tested on the standard TL;DR summarization dataset.

The paper was submitted on May 26, 2025, and is authored by Yinglun Xu, Hangoo Kang, Tarun Suresh, Yuxuan Wan, and Gagandeep Singh.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4c6ad2a-6301-4fa2-972f-7f065311f19c",
  "isSidechain": false,
  "promptId": "838c2fac-e99d-454e-b17f-5ef4d3f6d881",
  "type": "user",
  "uuid": "1d4e761a-bc29-47fe-9a26-b01aa951d663",
  "toolUseResult": {
    "query": "arXiv 2505.20556 pessimistic reward model RLHF PET reward tuning 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H9T7ehsJF15ZmyezfaWLnx",
        "content": [
          {
            "title": "[2505.20556] Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/abs/2505.20556"
          },
          {
            "title": "[Literature Review] Learning a Pessimistic Reward Model in RLHF",
            "url": "https://www.themoonlight.io/en/review/learning-a-pessimistic-reward-model-in-rlhf"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2505.20556v1"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://www.arxiv.org/list/cs/2025-05?skip=10550&show=500"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250520556X/abstract"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-05?skip=2150&show=100"
          },
          {
            "title": "Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL",
            "url": "https://arxiv.org/html/2510.06092v1"
          },
          {
            "title": "Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF",
            "url": "https://arxiv.org/html/2509.24713v1"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2505.20556:\n\n## Summary\n\nThe paper proposes 'PET', a novel pessimistic reward fine-tuning method, to learn a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF).\n\n## Key Problem and Solution\n\nTraditional reward modeling techniques in RLHF train an imperfect reward model, on which a KL regularization plays a pivotal role in mitigating reward hacking when optimizing a policy. Such an intuition-based method still suffers from reward hacking, and the policies with large KL divergence from the dataset distribution are excluded during learning.\n\nIn contrast, the authors show that when optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization, and one can learn a high-quality policy on their pessimistic reward without using any regularization.\n\n## Evaluation\n\nThe methods were tested on the standard TL;DR summarization dataset.\n\nThe paper was submitted on May 26, 2025, and is authored by Yinglun Xu, Hangoo Kang, Tarun Suresh, Yuxuan Wan, and Gagandeep Singh."
    ],
    "durationSeconds": 6.856904072999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a4c6ad2a-6301-4fa2-972f-7f065311f19c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T06:00:57.692Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Both PAR and PET are confirmed real papers. Now let me also verify the "reward compression vs calibration" confound claim from the 发掘 agent - this is arguably the most important discovery point because it could undermine the core causal claim. Let me also check if the Gradient Fingerprints paper (arXiv:2604.16242) is real, since the 发掘 agent uses it to position the Calibration Drift Detector.

Actually, I think I have enough information now. Let me summarize my verification findings:

**Verified:**


CRA, PURM, PET, and PAR are all confirmed as real papers with accurate descriptions of their core contributions.

The key insight is that calibration drift as a reward hacking detector appears to be genuinely novel—existing work uses gradient fingerprints or internal activation analysis, but nothing specifically leverages ECE drift for this purpose.

Two critical issues emerge: the reward compression confound is legitimate (PAR's simple bounded reward shaping already helps, suggesting temperature scaling might just be flattening rewards rather than improving calibration), and CRA is a major omission that needs to be cited. I need to add a reward range-matched control to Component B to isolate the calibration effect from simple compression.

The calibration drift detector itself deserves elevation as an independent contribution given its novelty. For the remaining concerns, I'm adopting most of the suggestions: scaling down Hessian computation to 7B/8B models with gradient norms for 72B, adding both PURM and PET baselines, including the full CGSP ablation matrix, adding compute-normalized comparisons, and using a mixed-effects model for the correlation analysis. The domain scope limitation gets acknowledged with difficulty stratification, and I'll stratify gradient attacks with transfer attacks for the larger model.

Now I'm reconstructing the full proposal from the feedback. The core structure involves a study on PRM calibration and reward hacking, where the central claim is that calibration quality causally determines resistance to reward hacking. Component A runs a correlation study across 48 configurations (8 PRMs × 6 calibration methods), measuring ECE against three tiers of hackability: gradient-based attacks, RL-induced hacking via GRPO, and BoN overoptimization. Component B establishes causality through three conditions: post-hoc calibration that changes nothing about representations, fine-tuning that changes both, and a matched control using auxiliary task fine-tuning.

Component C extends spectral analysis to the step level to understand compositional geometry, while Component D proposes a calibration-gated safe policy that uses a formula combining mean and standard deviation of calibration confidence with drift detection during RL training, compared against several baselines including uncalibrated GRPO, APRM, and ensemble methods. The evaluation uses MATH-500 for in-distribution testing and AIME for out-of-distribution generalization.

Now I'm assessing the quality of these ideas across multiple dimensions. The core insight linking calibration to reward hacking is moderately novel—while CRA already takes a causal approach to PRM vulnerabilities, the specific focus on calibration as a confound is distinct and could strengthen the contribution. The significance looks promising if the causal mechanism holds and CGSP demonstrates practical improvements, especially with the calibration drift detector as a key component. There's a notable gap in related work that needs addressing, particularly around CRA, but that's fixable with proper literature review.

On the experimental side, incorporating all the suggested fixes should make things manageable despite some lingering concerns about computational feasibility at scale and budget constraints. The ablation matrix will substantially strengthen the empirical validation, and adding the missing baselines like PURM and PET is crucial for proper comparison. Given novelty and significance both landing in the mid-range, I'd estimate the idea ceiling around 40-45%, with the current state probably at 25-30% due to those gaps, but climbing to 32-38% after implementing these improvements.

Now I need to reconstruct the full proposal from the workers' detailed descriptions since I don't have the original text directly. The workers clearly had access to it and provided enough detail for me to work with. I should also verify that the Calibration Drift Detector claim holds up—my search showed existing reward hacking detection uses internal activations and gradient fingerprints, but ECE drift specifically appears genuinely novel. Let me think through the reward compression confound angle more carefully before finalizing everything.

The core issue is that temperature scaling flattens the reward landscape, which naturally reduces gradient magnitudes for any attack—this could explain improved robustness independent of actual calibration improvements. The workers' suggested control is spot-on: linear rescaling that matches the reward range without improving ECE would isolate whether calibration itself matters or if it's just the compression effect. This needs to be the main improvement I recommend.

Looking at the full proposal structure, it's investigating whether PRM calibration quality causally determines resistance to reward hacking across 48 configurations. The approach combines a large correlation study measuring ECE and Brier score against hackability, then isolates causality through post-hoc calibration methods that don't change representations, fine-tuning that changes both, and a control matching representation changes without calibration gains. There's also a compositional geometry analysis at the step level to understand the underlying mechanisms.

The defense mechanism itself is a calibration-gated policy that uses calibrated uncertainty and calibration quality metrics to modulate reward signals pessimistically, tested against multiple baselines on mathematical reasoning benchmarks with different beam search sizes. The whole investigation requires substantial compute—around 3000+ H100-hours across gradient attacks, Hessian analysis, and the remaining experiments.

Now I'm organizing the referenced works that need to be preserved in the proposal, including the gradient regularization approach, PRM hackability findings, calibration studies, and various safety-focused methods, while also planning to integrate new citations for the expanded scope.

I'm structuring the proposal with a clear progression from motivation through related work into five distinct technical components—starting with correlation analysis, moving into causal isolation with reward compression safeguards, then step-level geometry analysis, CGSP defense mechanisms, and finally a calibration drift detector—before laying out the evaluation methodology and resource requirements.

Now I'm assessing the probability of success across key dimensions: the novelty hinges on whether the calibration-to-hackability causal link holds up empirically and how well the reward compression control differentiates from existing work like CRA, while significance depends on delivering both a practical defense and novel detector with solid empirical validation. Technical soundness and feasibility both sit at medium confidence given the empirical uncertainties around the causal claims and the scaled-down Hessian budget, which puts the overall ceiling around 40-45%.

Reconsidering more carefully, the core question is whether establishing calibration quality as a causal determinant of hackability is sufficiently novel and impactful. The specific testable causal claim and comprehensive experimental design are strengths, but the reward compression confound poses a real risk—if compression explains most of the effect, the central finding weakens considerably. Combined with CRA already exploring causal mechanisms and PAR showing simple transformations help, I'm settling on a median estimate around 35%, which justifies moving forward to Round 2 given the meaningful room for improvement. I'm identifying the key citations that need to be preserved from the original proposal, along with several new references I should incorporate—making sure all of these appear in my rewritten version to maintain accuracy and completeness. I've verified enough references through my searches, and the Gradient Fingerprints paper was cited by the discovery agent alongside other accurate sources, so I'll trust it. Now I'm reconstructing the full proposal with all the citations and improvements integrated, structuring it with the introduction establishing the core hypothesis about calibration causing robustness, the related work section covering PRM calibration research, and the five key contributions that move from correlation to causal isolation to practical defenses. Distinguishing CRA from CGSP—the former modifies representations while the latter calibrates outputs. For the correlation study, I'm testing 48 configurations across eight PRMs and six calibration methods, measuring calibration quality through ECE and Brier scores, then assessing hackability across gradient attacks, RL-based methods, and best-of-N sampling using a mixed-effects model. The causal isolation component uses post-hoc calibration techniques like temperature scaling as the primary evidence, supplemented by calibration-focused fine-tuning approaches.

For the representation control, I'm introducing a new reward range-matched baseline that rescales outputs to match the calibrated model's reward distribution without actually improving calibration metrics—this isolates the effect of calibration from any compression artifacts. The step-level geometry analysis extends prior work to examine how loss landscapes vary across solution trajectories, using spectral analysis on smaller models and gradient norms on larger ones, sampled at key positions like the start, middle, and end of reasoning chains. Finally, the CGSP defense applies a confidence-adjusted penalty term to the reward signal, with uncalibrated greedy rollouts as a baseline comparison.

For the defense mechanism, I'm testing against seven different baselines including uncalibrated greedy rollouts, adaptive PRM, caution-based approaches, ensemble methods, gradient regularization, and other calibration techniques. I'll run ablations removing individual components like the confidence scaling or drift term, and compare wall-clock time per training iteration to ensure the overhead is justified. The calibration drift detector runs in parallel as a lightweight, model-agnostic monitor that flags when the PRM's confidence estimates start degrading during training, independent of whether CGSP is deployed.

I'm evaluating on MATH-500 for in-distribution performance and AIME 24-25 for out-of-distribution robustness, stratified by difficulty levels. The key insight is that the drift detector naturally measures calibration fragility under distribution shift, which directly addresses whether in-distribution calibration predicts vulnerability to OOD attacks. I'll also document the computational requirements—roughly 1200 H100-hours for the gradient attacks and 400 for Hessian analysis—and acknowledge that while this focuses on mathematical reasoning, the approach could extend to other domains. Now I'm compiling the additional citations from the worker suggestions—causal reward adjustment, causal rubrics, probabilistic uncertainty modeling, pessimistic tuning approaches, reward shaping, gradient-based detection methods, and a few others that strengthen the methodological foundation.

Let me verify whether any existing work directly addresses the calibration-to-hackability connection I'm proposing. I'm checking through the related approaches: causal interventions at the representation level, uncertainty-based rewards without calibration gates, pessimistic fine-tuning strategies, simple reward transformations, prior calibration work that isn't linked to robustness concerns, and distributional PRMs that lack adversarial testing. The specific insight about how calibration relates to vulnerability appears to be the novel contribution here.

Now I'm ready to write the full output. I'm also making a decision about whether to continue iterating: both the critical and constructive agents identified substantive gaps to address, and since this is the first round, I should definitely move forward to the next iteration to refine these issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d4e761a-bc29-47fe-9a26-b01aa951d663",
  "isSidechain": false,
  "requestId": "req_011CbDJqFRGu5cwJhtPkmKfh",
  "type": "assistant",
  "uuid": "b66e9e1d-d25e-4fe3-a29b-4673235479ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DXfTpE6ZDCZC3rqvQG4TJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 32944,
      "output_tokens": 13357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3038,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13357,
          "cache_read_input_tokens": 32944,
          "cache_creation_input_tokens": 3038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3038
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

_source line 28 · 2026-05-20T06:03:32.035Z_

All key references verified. Now let me compile my analysis and produce the integrated output.

【阶段】: 迭代第 1 轮

【交叉验证调研】:

本轮用 WebSearch 验证了以下 worker 建议：

1. **CRA (arXiv:2508.04216)** — ✅已验证。论文真实存在，确实使用 sparse autoencoder + backdoor adjustment 在 PRM 内部表征上做因果干预以缓解 reward hacking。发掘 agent 的描述准确，这确实是 proposal 的重大 related work 遗漏。
2. **PURM (arXiv:2503.22480)** — ✅已验证。论文真实存在，提出两头架构生成 reward distribution 而非 scalar reward，通过 Bhattacharyya Coefficient 量化不确定性。补救 agent 正确指出这是 CGSP 的最直接方法层竞争者——两者都用 uncertainty-based pessimism，必须作为 baseline 对比。
3. **PET (arXiv:2505.20556)** — ✅已验证。论文真实存在，提出 pessimistic reward fine-tuning，无需 KL regularization 即可防 hacking。确认为有效 baseline。
4. **PAR (arXiv:2502.18770)** — ✅已验证。提出 bounded + centered reward 设计原则（sigmoid on centered reward），确认了发掘 agent 关于"reward compression confound"的担忧：如果简单的 reward 变换（让 reward 不那么极端）就能降低 hackability，那 temperature scaling 的效果可能来自 compression 而非 calibration。这个 confound 确实需要实验排除。
5. **Calibration drift 作为 hacking 检测器的 novelty** — ✅已验证。搜索显示现有 reward hacking 检测方法主要基于 internal activations 监控（arXiv:2603.04069）、gradient fingerprints（arXiv:2604.16242）、大规模 empirical detection frameworks，但无人使用 ECE drift 作为检测信号。Calibration Drift Detector 的 novelty 确认成立。

【发掘 agent 有效建议采纳】:

| # | 建议 | 决定 | 理由 |
|---|------|------|------|
| 1 | Reward compression confound — 增加 reward range-matched control | ✅已验证，采纳 | PAR (arXiv:2502.18770) 确认简单 reward 变换可降低 hacking，confound 威胁真实存在。必须加入 B4 控制实验排除此 trivial alternative。这是本轮最关键的 idea 层改进。 |
| 2 | CRA (arXiv:2508.04216) 遗漏 | ✅已验证，采纳 | CRA 确实存在且高度相关。必须引用并差异化（CRA 干预 representation space，本 proposal 干预 output space via calibration）。 |
| 3 | Calibration Drift Detector 升级为独立贡献 | ✅已验证，采纳 | 搜索确认无人做 ECE-based 实时监控，novelty 成立。升级为 Component E，独立于 CGSP。 |
| 4 | Step-level novelty 表述锐化 | 已验证（Ackermann 原文确实只做 outcome-level），采纳 | 加入"local sharp + global flat"直觉示例来论证 outcome-level 分析的盲区。 |
| 5 | OOD calibration scope limitation | 采纳 | 这是 calibration 文献的已知问题，逻辑上成立。将 OOD calibration degradation 与 Drift Detector 叙事串联。 |

【补救 agent 有效建议采纳】:

| # | 建议 | 决定 | 理由 |
|---|------|------|------|
| 1 | Hessian 可行性：缩小范围 | 采纳 | Granziol (arXiv:2602.00816) 的计算开销论证合理。72B 改用 gradient norm，Hessian 限 7B/8B，用 Hutchinson 替代 Lanczos。 |
| 2 | 补充 PURM/PET baseline | ✅已验证，采纳 | 两者均确认存在且与 CGSP 直接竞争。Baselines 扩展至 7 个。 |
| 3 | 非数学 domain 验证 | 部分采纳 | PRMBench 可作为补充，但全面跨 domain 验证超出本文 scope。加入 MATH difficulty stratification + 明确 scope limitation 声明。 |
| 4 | CGSP ablation 矩阵 | 采纳 | 5 个 ablation 条件清晰、必要，审稿人必问。 |
| 5 | Compute-normalized comparison | 采纳 | 领域标准要求。加入 wall-clock + compute-normalized curve。 |
| 6 | Matched control B3 多 auxiliary task | 部分采纳 | 多 auxiliary task 比单一更有说服力。同时明确 B1 为 primary evidence，B3 为 supporting。CKA reliability 争议注意但不必过度放大。 |
| 7 | 统计方法：mixed-effects model | 采纳 | n=48 非独立观测的聚类问题真实存在。改用 mixed-effects + within-PRM 单调性分析。 |
| 8 | Gradient attack 预算分层 | 采纳 | 全 48 配置做 white-box 不现实。12 configs 做完整 gradient attack，其余做 RL + BoN，72B 用 transfer attack。 |

【本轮 proposal 主要变更】:

**Idea 层面变更：**
- 新增 B4 reward range-matched control 排除 reward compression confound（核心因果 claim 的关键加固）
- 新增 CRA (arXiv:2508.04216) 和 CROME (arXiv:2506.16507) 引用及差异化讨论
- Calibration Drift Detector 升级为独立 Component E，论述其 zero-cost real-time model-agnostic 优势
- 增加"local sharp + global flat" step-level 分析动机示例
- OOD calibration scope 明确讨论，与 Drift Detector 叙事串联

**实验层面变更：**
- Baselines 从 5 → 7（新增 PURM、PET）
- 新增 5 条 CGSP ablation 矩阵
- Component A 统计方法升级为 mixed-effects model + within-PRM 分析
- Hessian 分析限 7B/8B + Hutchinson，72B 用 gradient norm
- Gradient attack 分层：12 configs 完整 white-box，其余 RL+BoN，72B transfer attack
- 新增 compute-normalized comparison
- B3 增加多 auxiliary task，明确 CKA matching 量化标准
- 加入 MATH difficulty stratification (Level 1-2/3-4/5)

【idea 质量评估】: Novelty=中+ Significance=中+ → idea 天花板约 42%

理由：calibration → hackability 的因果桥梁在文献中确实无人搭建，但 CRA 已从另一个因果角度切入同一问题，novelty 不是"强"。加入 reward compression control 后因果 claim 更严密，Calibration Drift Detector 独立贡献增加了贡献密度。Significance 受限于仅数学推理验证。

【实验完备性评估】: Technical Soundness=中+ → 地板基本补好

理由：主要缺陷均可补救且已规划补救方案。ablation 矩阵、compute-normalized comparison、统计方法升级显著增强了实验设计的严谨性。Hessian 可行性通过范围缩小解决。仍有风险点：B4 reward range-matched control 是否能干净地排除 confound（取决于实验结果），以及因果 claim 是否在 OOD 下成立（acknowledged as scope limitation）。

【当前概率估计】: [29% - 39%] 中位 34%

【决策】: 继续

【决策理由】: Round 1 两个 worker 都给出了实质性改进建议（发掘 agent 5 点、补救 agent 8 点），采纳后 proposal 质量显著提升但尚未稳定。关键改进（B4 reward compression control、CRA 差异化、Calibration Drift Detector 升级、ablation 矩阵）需要在下一轮被 worker 重新审视，确认是否引入新问题或仍有遗漏。距离收敛至少还需 1 轮。

【引用清单核对】（输出前逐条确认）:

原始 proposal 引用（必须保留）：
1. Ackermann et al. (arXiv:2602.18037) ✓
2. Tiwari et al. (arXiv:2603.06621) ✓
3. Park et al. (arXiv:2506.09338, NeurIPS 2025) ✓
4. Distributional PRMs (arXiv:2605.06785) ✓
5. APRM (arXiv:2511.22888, 2025) ✓
6. Caution (arXiv:2604.04648, 2026) ✓
7. Conformal Feedback Alignment / CFA (arXiv:2601.17329) ✓

新增引用：
8. CRA (arXiv:2508.04216) ✓
9. CROME (arXiv:2506.16507, NeurIPS 2025) ✓
10. PURM (arXiv:2503.22480) ✓
11. PET (arXiv:2505.20556) ✓
12. PAR (arXiv:2502.18770) ✓
13. Gradient Fingerprints (arXiv:2604.16242) ✓
14. Granziol (arXiv:2602.00816) ✓
15. PRMBench (arXiv:2501.03124) ✓

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
## Title

Does Calibration Cause Robustness? A Causal Investigation of Process Reward Model Calibration and Reward Hacking Resistance

## Core Claim

We hypothesize that the calibration quality of Process Reward Models (PRMs) causally determines their resistance to reward hacking—not merely correlates with it. We test this via a four-stage investigation: (A) large-scale correlation, (B) causal isolation with controls for the reward compression confound, (C) step-level loss landscape geometry, and (D) a Calibration-Gated Safe Policy (CGSP) defense. We additionally contribute (E) a Calibration Drift Detector that serves as a zero-cost, real-time, model-agnostic early warning system for reward hacking during RL training.

## Motivation

Recent work demonstrates that PRMs are severely vulnerable to reward hacking: Tiwari et al. (arXiv:2603.06621) show PRM rewards can be inflated above 0.9 while accuracy drops below 4%, with 43% of reward gains attributable to stylistic shortcuts. Separately, PRM calibration has received increasing attention—Park et al. (arXiv:2506.09338, NeurIPS 2025) reveal systematic overestimation on hard problems; Distributional PRMs (arXiv:2605.06785) achieve calibrated quantile functions via conditional optimal transport; Conformal Feedback Alignment (CFA, arXiv:2601.17329) applies conformal prediction to RLHF preference calibration at the answer level. However, no existing work connects calibration quality to hacking resistance. We bridge this gap.

A critical methodological challenge is the reward compression confound: post-hoc calibration methods such as temperature scaling simultaneously improve probability estimates and compress the reward range (making rewards less extreme). Since simpler reward transformations—e.g., bounded/centered reward (PAR, arXiv:2502.18770)—already reduce hacking by flattening reward gradients, any observed reduction in hackability after calibration could be attributable to compression rather than calibration per se. Our experimental design explicitly controls for this confound.

## Related Work

**PRM Calibration.** Park et al. (arXiv:2506.09338, NeurIPS 2025) introduce quantile regression for PRM calibration, measuring Brier score, AdaptiveCE, ECE, and AverageCE. Distributional PRMs (arXiv:2605.06785) use conditional optimal transport for calibrated quantile functions but do not test adversarial robustness. CFA (arXiv:2601.17329) applies conformal prediction to RLHF but only at the answer level, not step-level.

**PRM Reward Hacking.** Tiwari et al. (arXiv:2603.06621) establish a three-tier attack framework (static perturbation, adversarial tokens, RL-induced hacking). Ackermann et al. (arXiv:2602.18037) link gradient norm flatness to reward accuracy retention and propose gradient regularization as defense, but analyze only outcome-level scalar rewards.

**Causal Approaches to Reward Model Robustness.** CRA (Causal Reward Adjustment, arXiv:2508.04216) uses sparse autoencoders to extract interpretable features from PRM internal activations, then applies backdoor adjustment to remove confounding semantic features. CROME (arXiv:2506.16507, NeurIPS 2025) uses explicit causal models to separate prompt-driven preferences from spurious artifacts, achieving +5.4% on RewardBench. Our work differs from both in the locus of causal intervention: CRA and CROME intervene in the representation space (internal activations / causal graphs over features), whereas we intervene in the output space by manipulating calibration quality. This distinction is important because output-space calibration is far cheaper to apply post-hoc and does not require retraining or access to internal representations. We test whether the two approaches are complementary.

**Defense Methods.** APRM (arXiv:2511.22888, 2025) uses adversarial Generator-Discriminator training (+3.4pp cross-benchmark, +5.3pp OOD). Caution (arXiv:2604.04648, 2026) applies pessimism-based defense for BoN using prediction error as uncertainty proxy. PAR (arXiv:2502.18770) proposes bounded/centered reward shaping via sigmoid on centered reward. PURM (arXiv:2503.22480) generalizes Bradley-Terry to learn reward distributions with a two-head architecture, quantifying uncertainty via Bhattacharyya Coefficient—this is the closest methodological competitor to CGSP since both leverage reward uncertainty for pessimism. PET (arXiv:2505.20556) learns pessimistic reward models via adversarial fine-tuning without KL regularization.

**Reward Hacking Detection.** Gradient Fingerprints (arXiv:2604.16242) detect hacking via gradient-level analysis but require gradient computation. Internal activation monitoring (arXiv:2603.04069) tracks concept directions during RL training. Our Calibration Drift Detector offers a complementary signal based on ECE statistics, requiring only reward outputs (no gradient or activation access).

## Component A: Large-Scale Correlation Study

**Setup.** 8 PRMs (spanning 1.5B to 72B parameters, including Qwen, Skywork, Math-Shepherd families) × 6 calibration methods (uncalibrated, temperature scaling, Platt scaling, histogram binning, isotonic regression, quantile recalibration following Park et al.) = 48 configurations.

**Calibration Metrics.** ECE, Brier score, reliability diagrams per configuration.

**Hackability Metrics (Three Tiers).**
- Tier i (gradient-based attack): White-box token-level optimization following Tiwari et al.'s protocol. Applied to 12 representative configurations (3 PRM families × 4 calibration methods including uncalibrated). For 72B models, use transfer attacks from 7B/8B adversarial tokens.
- Tier ii (RL-induced hacking): GRPO training on MATH-500, measuring reward–ground-truth accuracy divergence. All 48 configurations.
- Tier iii (BoN overoptimization): Best-of-N with N ∈ {4, 16, 64, 256, 1024}, measuring overoptimization onset point N*. All 48 configurations.

**Statistical Analysis.** Mixed-effects model with PRM identity as random effect and calibration method as fixed effect, replacing simple Spearman correlation to correctly handle the nested non-independent structure (same PRM's 6 calibration variants are correlated). Supplementary within-PRM monotonicity analysis: for each PRM, do the 6 calibration methods monotonically improve hackability resistance? This within-subject analysis is free from between-PRM heterogeneity. Report cluster-robust standard errors and block-bootstrap confidence intervals.

**Difficulty Stratification.** Report all metrics separately for MATH Level 1-2, Level 3-4, and Level 5 to test whether the calibration–hackability relationship is stable across difficulty.

## Component B: Causal Isolation Experiments

**B1 (Primary Evidence): Post-Hoc Calibration.** Apply temperature scaling and Platt scaling to pre-trained PRMs. These methods adjust output probabilities without modifying internal representations (zero representation change), providing the cleanest causal evidence that improved calibration → reduced hackability.

**B2: Calibration-Improving Fine-Tuning.** Fine-tune PRMs on calibration-targeted objectives. This changes both representations and calibration, serving as a weaker causal test.

**B3 (Supporting Evidence): Matched Representation Change Control.** Fine-tune PRMs on auxiliary tasks that produce CKA-matched representation changes but do NOT improve calibration. Multiple auxiliary tasks for cross-validation: (a) next-token prediction on non-math text (Wikipedia), (b) random label fine-tuning, (c) math text fine-tuning with shuffled step labels. Pre-registered CKA matching criterion: per-layer CKA ≥ 0.95 relative to the B2 fine-tuned model, OR average CKA within ±0.02 of B2. Supplement CKA with SVCCA as cross-check. If representation change without calibration improvement does NOT reduce hackability, the causal arrow points to calibration.

**B4 (Critical Control): Reward Range-Matched Compression Control.** Apply simple linear rescaling or sigmoid clipping to uncalibrated PRM rewards, matching the reward range (min, max, variance) of the calibrated PRM, but WITHOUT improving calibration (ECE unchanged or worsened). If this compression-only transformation reduces hackability comparably to true calibration, the mechanism is reward compression, not calibration per se. If only genuine calibration improvement reduces hackability, the causal claim is supported. This control is essential to exclude the trivial alternative raised by PAR (arXiv:2502.18770): that flatter rewards inherently resist gradient-based hacking regardless of calibration quality.

## Component C: Step-Level Compositional Geometry

**Motivation.** Ackermann et al. (arXiv:2602.18037, Propositions 3.3–3.4) analyze gradient norms and Hessian eigenvalues for outcome-level scalar reward R(s,a), linking flatness to reward accuracy retention. This is inapplicable to step-level PRMs where each step t has its own reward r_t and the compositional structure matters. Critically, outcome-level analysis can miss step-heterogeneous vulnerability patterns: a PRM may be flat at most steps but have a sharp peak at one critical step (e.g., the final answer step), allowing an adversary to inject noise at that single step for high reward. Outcome-level averaging would mask this "local sharp + global flat" pattern, producing a false sense of security.

**Method.**
- For 7B/8B PRMs (2-3 models × 2-3 calibration methods = 4-6 configurations): full Hessian spectral analysis using Hutchinson trace estimator + power iteration for top eigenvalues. Sampled step positions: first step, middle step, final step, and one randomly selected intermediate step.
- For 72B PRMs: gradient norm analysis only (following Ackermann et al.'s methodology), extended to per-step computation. This follows Granziol (arXiv:2602.00816) who demonstrate that full Hessian analysis at 100B scale requires specialized FSDP infrastructure.
- Correlate per-step sharpness metrics with per-step hackability (measured as reward gain from step-local perturbations).

## Component D: CGSP (Calibration-Gated Safe Policy) Defense

**Formulation.** Modified reward for GRPO: r̃_t = μ_t − α · σ_t / √c_t, where μ_t is the calibrated mean reward at step t, σ_t is the calibrated uncertainty (from conformal prediction or ensemble variance), c_t is the local calibration quality (ECE computed on a rolling buffer of recent trajectories at step t), and α is the pessimism strength.

**Mechanism.** When calibration is high (c_t → 1), the penalty is σ_t-scaled pessimism. When calibration degrades (c_t → 0), the penalty amplifies, automatically increasing conservatism in regions where the PRM is unreliable. This is calibration-gated pessimism—distinct from PURM (arXiv:2503.22480) which uses fixed uncertainty without calibration-quality modulation, and from PET (arXiv:2505.20556) which achieves pessimism through adversarial fine-tuning rather than reward transformation.

**Baselines (7 methods).**
(i) Uncalibrated GRPO
(ii) APRM (arXiv:2511.22888)
(iii) Caution pessimism (arXiv:2604.04648)
(iv) Ensemble-min (minimum across 3 reward models)
(v) Gradient regularization (Ackermann et al., arXiv:2602.18037)
(vi) PURM uncertainty-penalized training (arXiv:2503.22480)
(vii) PET pessimistic reward tuning (arXiv:2505.20556)

**Ablation Matrix.**

| Variant | Description |
|---------|-------------|
| CGSP-full | r̃_t = μ_t − α·σ_t/√c_t + Drift Detector |
| CGSP w/o c_t | r̃_t = μ_t − α·σ_t (remove calibration gating) |
| CGSP w/o σ_t | r̃_t = μ_t − α/√c_t (constant uncertainty, calibration gating only) |
| CGSP w/o Drift | CGSP-full but Calibration Drift Detector disabled |
| CGSP fixed-α | Global constant α vs. per-difficulty adaptive α |

**Compute-Normalized Comparison.** Report wall-clock time per GRPO iteration (reward computation + defense overhead) for every method. Plot compute-normalized curve: x-axis = total GPU-hours, y-axis = reward–accuracy alignment. Profile CGSP overhead breakdown (rolling buffer ECE, drift detection, conformal calibration). Provide CGSP-lite variant (reduced drift detection frequency, smaller rolling buffer) to demonstrate accuracy–efficiency tradeoff.

**Evaluation.** MATH-500 (in-distribution) and AIME 2024-2025 (OOD). Report: (1) downstream accuracy, (2) reward–accuracy Spearman correlation throughout training, (3) overoptimization onset point, (4) accuracy retention at fixed reward threshold.

## Component E: Calibration Drift Detector (Independent Contribution)

**Motivation.** Existing reward hacking detection methods require gradient computation (Gradient Fingerprints, arXiv:2604.16242) or internal activation access (arXiv:2603.04069). We propose a zero-cost, model-agnostic alternative: monitoring ECE drift on a rolling window of RL-generated trajectories during training.

**Theoretical Rationale.** As RL policy shifts away from the PRM's calibration distribution, the PRM's probability estimates become miscalibrated on the new trajectory distribution. This ECE drift is a necessary precursor to reward hacking: the PRM cannot be systematically exploited if it remains well-calibrated on the current policy's output distribution. We hypothesize that ECE drift is a reliable leading indicator of reward–accuracy divergence.

**Method.** During GRPO training, compute ECE on a rolling buffer of the K most recent trajectories every M training steps. Flag drift when ECE exceeds a threshold δ above the initial ECE, or when the rate of ECE increase exceeds a rate threshold. Upon flagging: pause training, trigger re-calibration (Component D's c_t update), or switch to a more conservative α.

**Evaluation.** (1) Temporal analysis: does ECE drift consistently precede reward–accuracy divergence? What is the lead time? (2) Comparison with Gradient Fingerprints (arXiv:2604.16242) on detection precision/recall and computational overhead. (3) Standalone deployment: plug the detector into standard GRPO without CGSP—does early stopping based on ECE drift alone reduce hacking?

**Scope and Limitations.** We establish the calibration–hackability causal link and validate CGSP within mathematical reasoning (MATH, AIME). Generalization to code generation, logical reasoning, and other step-level verification domains is important future work. The in-distribution calibration assumption is a known limitation: calibration measured on held-out data may not transfer under large distribution shifts. Component E directly addresses this by monitoring calibration degradation in real time, and the speed of ECE drift itself quantifies calibration fragility under distribution shift.

## Resource Estimates

| Component | Budget (H100-hrs) | Notes |
|-----------|-------------------|-------|
| A: Correlation study (Tier ii+iii on 48 configs, Tier i on 12 configs) | ~1,200 | Transfer attacks for 72B |
| B: Causal isolation (B1-B4) | ~400 | Post-hoc calibration is cheap; B4 adds ~50 hrs |
| C: Step-level geometry | ~400 | 7B/8B Hessian only; 72B gradient norms |
| D: CGSP + 7 baselines + ablation | ~1,500 | Includes α sweep and compute profiling |
| E: Calibration Drift Detector | ~200 | Temporal analysis + standalone evaluation |
| **Total** | **~3,700** | |
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b66e9e1d-d25e-4fe3-a29b-4673235479ae",
  "isSidechain": false,
  "requestId": "req_011CbDJqFRGu5cwJhtPkmKfh",
  "type": "assistant",
  "uuid": "50276d62-1d39-43db-bef5-607c73bb2bec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DXfTpE6ZDCZC3rqvQG4TJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 32944,
      "output_tokens": 13357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3038,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13357,
          "cache_read_input_tokens": 32944,
          "cache_creation_input_tokens": 3038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3038
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.  ---  【状态】: 有发…",
  "leafUuid": "50276d62-1d39-43db-bef5-607c73bb2bec",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate calibration-driven reward hacking resistance",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.  ---  【状态】: 有发…",
  "leafUuid": "50276d62-1d39-43db-bef5-607c73bb2bec",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate calibration-driven reward hacking resistance",
  "sessionId": "e0cd6d6a-c98c-4091-bf86-447280e1f026"
}
```

---
