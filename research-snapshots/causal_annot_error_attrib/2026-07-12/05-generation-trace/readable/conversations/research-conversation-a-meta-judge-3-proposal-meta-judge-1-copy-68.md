# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/7f153888-4058-4d8a-8bf7-14562511eba6.jsonl`
- **Structured JSON:** [`968b06ea91b56b200723.json`](../../sessions/96/968b06ea91b56b200723.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:11:11.494Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:11:11.494Z",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n⚠️ 致命性前置问题：venue mismatch（投稿目标错误）\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n在进入 idea 质量评估之前，必须首先指出：\n\n**本 proposal 与 CoRL 2026 存在根本性的 venue mismatch。** \n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求：\n- 投稿必须聚焦于核心的 robotics problem\n- 必须展示所提出的 models/algorithms/datasets/benchmarks 对 robotics 的 relevance\n- \"Submissions without a robotics focus will be returned without review\"（无机器人焦点的投稿将不经审稿直接退回）\n\n本 proposal 的内容是 **LLM 安全对齐的训练时可复现性审计**——完全属于 NLP/AI Safety 领域，与 robot learning 无任何交集。投稿 CoRL 将 100% 被 desk reject。\n\n**如果用户实际目标是 NeurIPS 2026、ICML 2026、ICLR 2027 或 EMNLP 2026 等 NLP/ML 主会，以下 idea 质量评估仍然适用。** 以下评估假设投稿目标是一个接受 LLM safety 话题的 top venue（如 NeurIPS/ICML/ICLR）。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n【领域调研】:\n\n- [Larsen 2025, arXiv:2512.12066] (Dec 2025): 提出 SSI 指标，发现 18–28% 的 prompt 在不同 inference seed/temperature 下在 refusal 和 compliance 之间翻转。本 proposal 的直接前驱，但仅关注 inference-time variance（固定权重），未触及 training-time variance。论文存在且描述准确。\n\n- [Fraser et al. 2025, arXiv:2506.17209] (June 2025, LLMSEC): 首次证明 training-seed variance 影响安全性——5 个 SFT seed 在 Llama-3.2-1B 上产生最高 9pp 的 harmfulness score 变化。使用 LoRA + 4-bit quantization + SORRY-Bench。论文存在且描述准确。**但注意：这是 SFT 而非 preference optimization，且仅 5 seeds、2 models、1 benchmark——proposal 将其作为核心 gap 依据是合理的。**\n\n- [OXRL, arXiv:2603.19335] (March 2026): 51 种 post-training 算法在 Qwen 2.5 (0.5B–7B) 上的 controlled comparison。发现 scale-dependent ranking inversions（SimPO 在 1.5B 最差、7B 最好）。提供了 GSM8K 上 SGRPO 的 cross-seed std ±0.57pp 作为 capability variance baseline。**但 OXRL 未做任何 safety evaluation**——proposal 准确地将此定位为 gap。\n\n- [SafeDPO, arXiv:2505.20065] (ICLR 2026 Oral): DPO + PKU-SafeRLHF-30K 达到 ~97% harmless ratio。确认了数据集和方法的成熟度，但未报告 cross-seed variance。论文存在且描述准确。\n\n- [SafeGRPO, arXiv:2511.12982] (Nov 2025): 验证了 classifier-as-reward 的 GRPO 安全对齐范式。论文存在。\n\n- [SafeTuneBed, arXiv:2506.00676] (May 2025): 安全微调 toolkit，3-seed averaging，提到 refusal consistency 但未正式定义。\n\n- [LLM-Safety Evaluations Lack Robustness, arXiv:2503.02574] (March 2025): evaluation pipeline 选择导致最高 28% ASR variance，动机化了 fixed-pipeline 设计。\n\n- [TRACEALIGN, arXiv:2508.02063] (2025): 追踪对齐失败到训练时信念来源，减少 alignment drift 达 85%，但方法论完全不同（mechanistic interpretation vs empirical audit）。\n\n- 调研总结：**safety alignment 的 fragility 是一个已被多个角度初步验证的现象（inference-time: Larsen; SFT training-time: Fraser; evaluation pipeline: arXiv:2503.02574），但 preference-based alignment (DPO/PPO/GRPO) 的 training-time safety reproducibility 确实没有被系统研究过。** 该 gap 真实存在，但 gap 的 \"width\" 有限——核心问题方向已被邻近工作大致框定，本 proposal 的贡献本质是 scale-up + 组合 + 方法扩展。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁。**\n\n核心问题是\"safety 在 retraining 中是否比 capability 更 fragile\"。一个成本远低的替代方案是：\n1. 仅跑 DPO 一种算法（最成熟的 open-source 方法），在 1-2 个 scale 上，用 10 seeds，对比 safety vs capability variance。这已经足以回答核心问题，compute 成本不到 proposal 的 1/5。\n2. 如果发现 safety 确实更 fragile（高概率，因为 Fraser et al. 已在 SFT 上证明了），增量发现不令人惊讶。\n3. 260 runs 的大规模设计增加了 **thoroughness**（hardware ablation, reward model ablation, 3 algorithms × 3 scales），但这些都是实验设计层面的完善，不改变核心发现的 novelty。\n\n增量价值在于：(a) 覆盖三种不同范式的 preference optimization 而非仅 SFT；(b) ANOVA 方差分解跨多因素；(c) minimum-seed lookup tables 的实用工具。但这些增量价值更接近 \"engineering thoroughness\" 而非 \"conceptual breakthrough\"。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n【前提假设检验】:\n\n核心 claim 逻辑链中有以下未经验证的假设：\n\n1. **\"Safety 比 capability 在 training-time 上更 fragile\" 几乎是预期结论。** Fraser et al. 在 SFT 上已经显示 9pp safety variance vs 一般认为的 <1pp capability variance。如果 preference optimization 也呈现相同模式，审稿人会说 \"I would have guessed this\"——safety decisions 本质上是在 decision boundary 附近的二元分类，而 capability（如 GSM8K 准确率）是在整个分布上的聚合指标，前者天然更 noisy。这不需要大规模实验来\"发现\"，更像是在验证一个已有的 prior。\n\n2. **SCI-T 的学术贡献被高估。** SCI-T(p) = max_c(n_c)/K 本质上就是\"K 个 seed 中多数决策的比例\"——这是一个 trivially simple metric。Proposal 将其包装为\"extending Larsen's SSI to training-time\"，但实际上 SSI 也是一个简单的 agreement metric，从 inference-time 到 training-time 的\"扩展\"不涉及任何方法论创新，仅仅是改变了 variance source（sampling noise → training noise）。\n\n3. **Minimum-seed lookup tables 的假设前提。** 这些 tables 假设 variance 在不同 hyperparameter settings、不同 base models、不同数据集上是稳定的（否则 tables 不可推广）。但 variance 高度依赖于具体配置，一个在 Qwen3 + PKU-SafeRLHF 上得出的 \"minimum 15 seeds\" 结论对 Llama + 其他数据集是否适用，完全未被论证。\n\n4. **Full fine-tuning 消除 LoRA confound 的论证是合理的**，但也引入了新问题——real-world deployment 中很多人用 LoRA，full FT 的结论对 LoRA practitioners 的实用性受限。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心发现方向（safety 比 capability 更 fragile under retraining）已被 Fraser et al. 在 SFT 上初步证明，Larsen 在 inference-time 上证明。Proposal 的 novelty delta 是\"从 SFT 扩展到 DPO/PPO/GRPO + 从 2 models 扩展到 3 scales + 从 5 seeds 扩展到 20 seeds + ANOVA 分解\"——这是 **quantitative scaling**，不是 qualitative leap。SCI-T 是一个 trivial metric（max agreement ratio），几乎不贡献方法论 novelty。Minimum-seed tables 是标准 power analysis 的直接应用（Cédric et al. 2018），方法论上无新意。OXRL (arXiv:2603.19335) 已经建立了 controlled post-training comparison 的范式，本 proposal 本质上是将 OXRL 的框架加了 safety 维度。\n\n2. **Significance: 中** — \n   研究问题本身重要——AI governance 需要知道 safety claim 的 reproducibility bound，EU AI Act 和 NIST AI RMF 确实需要这类 empirical evidence。但问题的重要性和 idea 的 contribution 是两回事。如果核心发现是 \"safety 确实比 capability 更 fragile\"（高概率如此），这不令人惊讶。如果核心发现是 \"safety 和 capability 一样 stable\"（低概率），那反而更 surprising 和有价值。Proposal 的 dual-outcome 设计部分缓解了这个问题，但主路径的 expected finding 缺乏 surprise value。\n\n3. **Related Work: 强** — \n   Proposal 对 related work 的覆盖异常全面，清晰定位了与 Larsen (inference-time), Fraser et al. (SFT, small-scale), OXRL (capability-only), SafeDPO (no variance), SafeGRPO (method validation), SafeTuneBed (3-seed, no metric) 各自的差异。引用的论文经核实均真实存在，描述准确。差异化定位清晰：no prior work combines (a) preference optimization, (b) multi-scale, (c) 20+ seeds, (d) multi-benchmark, (e) formal metric, (f) ANOVA decomposition——这是事实。但 related work 的完善度本身也暴露了一个问题：prior work 已经非常接近这个 proposal 在做的事情，剩余的 gap 相对狭窄。\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n【概率估计】: \n\n- 如投 CoRL 2026: 0%（desk reject，venue mismatch，无任何 robotics 内容）\n- 如投适当 venue（NeurIPS/ICML/ICLR）: [18% - 28%]，中位 22%\n\n【估计理由】:\n\nIdea 处于 rubric 中 \"15-25%: idea 方向站得住脚但内核薄弱\" 到 \"25-35%: idea 有实质内核但 expected finding not surprising\" 的边界。\n\n向上拉的因素：\n- 研究问题对 AI governance 确实重要（Significance 中等偏上）\n- 实验设计严谨（但这是执行层面，不影响 idea 评分）\n- Related work 定位清晰，gap 真实存在\n\n向下拉的因素（限制上界的关键维度：**Novelty**）：\n- 核心 expected finding（safety > capability fragility）缺乏 surprise value——审稿人大概率会说 \"I would have guessed this\"\n- 贡献本质是 scale-up + combination of existing directions，不是 conceptual innovation\n- SCI-T 和 minimum-seed tables 的方法论贡献过于 trivial\n- 存在明显的 trivial alternative：小规模实验即可验证核心 hypothesis\n\nNovelty 是限制上界的主要维度。即使实验执行完美，idea 的 ceiling 也在 ~30%。\n\n【主要风险】:\n\n1. **\"Confirmatory study\" 质疑**：核心发现（safety 比 capability 更 fragile）几乎是 prior work 的直接预期推论——审稿人可能认为这是一个 expensive 但 unsurprising 的 confirmatory study，而非 discovery paper。在 top venue 中，\"the answer is what we expected, but now we know for sure\" 型论文的接受门槛远高于 \"surprising finding\" 型论文。\n\n2. **Generalizability 质疑**：所有实验基于 Qwen3-Instruct + PKU-SafeRLHF-30K 这一组合。Minimum-seed lookup tables 的推广性（到不同 base model families, 不同 safety 数据集, 不同 scale ranges）缺乏理论保障——审稿人会质疑 \"your tables are for Qwen3 on PKU-SafeRLHF; why should I trust them for my Llama model on my dataset?\"\n```\n\n---\n\n**补充说明**：本 proposal 在**形式完善度**上极高——power analysis、ANOVA 设计、dual-outcome、多 ablation 等都表明作者具有强实验设计能力。但形式完善度本身不等于 idea 质量。如果将此 proposal 视为一个 \"empirical benchmark/audit\" 类型的贡献（类似 HELM、AlpacaEval 等 benchmark paper），而非一个 \"discovery\" paper，投稿 workshop（如 NeurIPS SafeGenAI workshop）或 Datasets & Benchmarks track 可能更匹配其贡献类型。\n\nSources:\n- [The Instability of Safety (Larsen 2025)](https://arxiv.org/abs/2512.12066)\n- [Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (Fraser et al. 2025)](https://arxiv.org/abs/2506.17209)\n- [OXRL: Do Post-Training Algorithms Actually Differ? (2026)](https://arxiv.org/abs/2603.19335)\n- [SafeDPO (ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 About](https://www.corl.org/about-corl)\n- [Assessing Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs](https://arxiv.org/html/2503.07329v2)\n- [TRACEALIGN](https://arxiv.org/pdf/2508.02063)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to produce my evaluation. Let me synthesize.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 【重要前置警告：严重的投稿目标不匹配】\nCoRL (Conference on Robot Learning) 的投稿范围明确要求论文 \"focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\"。本 proposal 是一篇纯 LLM 安全对齐可复现性的实证研究，不涉及任何机器人学习内容。投稿 CoRL 几乎必然被 desk reject。本 proposal 更适合的目标会议包括：NeurIPS (尤其 Datasets & Benchmarks track)、ICML、ACL/EMNLP、或 AAAI。以下评估基于 idea 本身的质量（假设投稿到一个 scope 匹配的顶会），但请注意若坚持投 CoRL，中稿概率接近 0%。\n\n【领域调研】:\n- [Larsen 2025, arXiv:2512.12066] (Dec 2025): 提出 SSI 指标，发现 18-28% 的 prompt 在不同 inference seed/temperature 下 refusal 行为翻转。核心局限：只测量 inference-time variance（固定权重，不同采样），不涉及 training-time variance。本 proposal 正确识别了这一gap。\n- [Fraser et al. 2025, arXiv:2506.17209] (LLMSEC 2025): 首次实证 SFT seed variance 对 safety 的影响，5 seeds、LoRA+4bit、SORRY-Bench，发现最高 9pp harmfulness score variance。核心局限：只用 SFT（非 preference optimization），LoRA 初始化 variance 与 seed variance 纠缠，样本量小。本 proposal 的核心论据来源。\n- [OXRL, arXiv:2603.19335] (March 2026): 51 种 post-training 算法在 Qwen 2.5 (0.5B-7B) 的受控对比，发现 scale-dependent ranking inversions，3-5 seeds per config，但完全没有 safety evaluation。提供了 capability variance baseline (±0.57pp on GSM8K)。\n- [SafeDPO, arXiv:2505.20065] (ICLR 2026 Oral): DPO on PKU-SafeRLHF-30K 达到 ~97% harmless ratio，确立了数据集和方法的成熟度，但未报告任何 cross-seed variance。\n- [SafeTuneBed, arXiv:2506.00676] (May 2025): 安全微调工具包，3-seed averaging，提到 \"refusal consistency\" 但未正式定义。\n- [RVPO, arXiv:2605.05750] (May 2026, Apple): 提出 inter-reward variance penalty，在 multi-objective alignment 中惩罚 reward 间方差。与本 proposal 的 reward model ablation 动机相关但方法不同。\n- [arXiv:2503.02574] (March 2025): 证明 evaluation pipeline 选择可导致最高 28% ASR variance，支持本 proposal 的 fixed-pipeline 设计。\n- [SafeGRPO, arXiv:2511.12982] (Nov 2025): 验证 classifier-as-reward 用于 GRPO 安全对齐的可行性。\n- 调研总结：training-time safety reproducibility 确实是一个被 identify 但未被系统研究的 gap。Fraser et al. 开了头（SFT only, small scale），OXRL 建了基础设施（capability only），但两者的交叉——preference optimization 的 training-time safety variance——确实没有被覆盖。这个 gap 是真实的。\n\n【Trivial Alternative 检验】:\n存在中等程度的 trivial alternative 威胁。最直接的替代方案：\n1. **简单 scale-up Fraser et al.**: 直接将 Fraser 的实验从 SFT 扩展到 DPO/PPO/GRPO，用 5-10 seeds（而非 20），不需要 ANOVA、SCI-T 等完整框架，即可获得 \"preference optimization 也有 safety variance\" 这一核心发现。本 proposal 的增量在于统计严谨性（power analysis、20 seeds、variance decomposition）和系统性（多算法、多尺度、多 benchmark），但这些是 rigor 的增量，非 insight 的增量。\n2. **直接复用 OXRL 框架加 safety eval**: 在 OXRL 已有的 controlled runs 上追加 safety evaluation（WildGuard/HarmBench），即可获得 safety vs. capability variance 的直接对比，无需从头训练 260 runs。\n3. SCI-T 指标本质是 max(n_refuse, n_comply)/K，与 SSI 是同一公式、不同的 variance source。这不是一个有深度的 methodological contribution。\n\n增量价值在于：(a) 完整的 ANOVA variance decomposition across 5 factors，(b) power-justified 20-seed design，(c) minimum-seed lookup tables 的 governance 应用价值。这些是工程完备性和实用价值的增量，而非概念性突破。\n\n【前提假设检验】:\n核心 claim 的逻辑链中有以下未经验证的假设：\n1. **\"Safety 比 capability 在 training-time 更 fragile\" 是预期结论，不是 surprising finding。** 大多数 alignment 研究者会预测这个结果，因为：safety 行为是对边界情况的学习、safety 训练数据相对 noisy、safety 与 helpfulness 之间存在张力创造不稳定的优化面。如果结论是 positive，审稿人大概率会说 \"I would have guessed this\"。如果结论是 negative（safety 比 capability 更稳定），这反而更 surprising 也更有发表价值。\n2. **从 Fraser et al. 的 SFT/LoRA 实验外推 σ̂_safety ≈ 3.9pp 用于 preference optimization 的 power analysis 是有风险的。** DPO/PPO/GRPO 的优化 landscape 与 SFT 有本质不同，实际 variance 可能远大或远小于 3.9pp。作者提到了 adaptive provision（pilot 后增加到 25 seeds），但 power analysis 的前提假设本身是 borrowed 的。\n3. **Full fine-tuning 是否真的 \"cleanly isolates\" training-seed variance 也存疑。** Full FT 引入了更多参数自由度，可能使 variance 更大，也可能因为优化更充分而更小。\"消除 LoRA confound\" 的逻辑成立，但 full FT 本身也引入了新的 confound（更高的 overfitting 风险、不同的 loss landscape）。\n4. **WildGuard 同时作为 GRPO 的 reward signal 和 evaluation judge 存在评估循环。** 虽然这在 safety alignment 研究中常见，但审稿人可能会质疑：GRPO 训出的模型在 WildGuard eval 上表现好只是因为它 overfit 到了 WildGuard 的判断偏好。\n\n【3 维度打分】:\n1. **Novelty: 弱-中** — 核心贡献是将已知方法论（seed variance analysis、ANOVA、power analysis）系统性地应用到一个新场景（preference optimization safety）。SCI-T 是 SSI 的直接平移，ANOVA 和 power analysis 是标准统计工具。Gap 是真实的（Fraser et al. 只做了 SFT，OXRL 没有 safety eval），但填补方式是 \"scale up + apply standard tools\"，而非提出新的 conceptual framework。对比 OXRL（arXiv:2603.19335）发现了 scale-dependent ranking inversions 这样的 surprising finding，本 proposal 预期的核心 finding（safety 更 fragile）缺乏 surprise value。\n2. **Significance: 中** — 研究问题本身很重要：safety alignment 的可复现性直接影响 AI governance 和部署决策。Minimum-seed lookup tables 有真实的政策应用价值（EU AI Act、NIST AI RMF）。但影响力主要在 evaluation methodology 和 governance，不在推进 alignment 算法本身。这是一个 \"measurement\" paper，不是一个 \"mechanism\" paper。对领域的推动是增量性的——它不会改变人们做 alignment 的方式，只会改变人们评估 alignment 的方式。\n3. **Related Work: 强** — 对相关工作的覆盖非常全面且准确。每篇引用的论文都真实存在且描述准确（Larsen arXiv:2512.12066 ✓，Fraser arXiv:2506.17209 ✓，OXRL arXiv:2603.19335 ✓，SafeDPO ICLR 2026 Oral ✓，RVPO arXiv:2605.05750 ✓）。差异化定位清晰——明确说明了 Fraser (SFT only)、OXRL (capability only)、Larsen (inference only) 各自的局限，以及本 proposal 如何覆盖交叉地带。唯一的小瑕疵是 SafeTuneBed (arXiv:2506.00676) 已经在做类似的 safety fine-tuning benchmark + seed averaging，但 proposal 正确指出了它\"mentioned but never formally defined\" refusal consistency。\n\n【概率估计】（假设投稿到 scope 匹配的顶会如 NeurIPS/ICML/ACL）: [20% - 32%] 中位 25%\n【如果坚持投 CoRL】: [0% - 3%] 中位 1%\n\n【估计理由】:\nIdea 内核是一个设计精良、动机充分的大规模实证 audit，填补了一个真实的 gap。Related work 覆盖优秀，实验设计（如果执行到位）会产出有用的 governance deliverables。但三个因素限制了上界：\n(1) **Novelty 天花板低**——核心贡献是 \"apply standard methodology to new domain\" 而非 conceptual breakthrough，SCI-T 缺乏方法论深度；\n(2) **核心 finding 的 surprise value 低**——\"safety 比 capability 更 fragile\" 是大多数人的 prior，positive result 确认性强但缺乏 \"aha moment\"；\n(3) **Trivial alternative 存在**——一个 50% compute 成本的简化版实验（5-10 seeds、2 algorithms、1 scale）可能产出定性相同的结论，使得 260 runs 的完整 audit 在 marginal insight/compute 比上不够高效。\n\n这使得 idea 落在 \"solid but expected\" 区间 (25-35%)，但因 surprise value 偏低，中位数在该区间的下半部分。\n\n**投 CoRL 的额外致命问题**: 这篇论文与 robot learning 完全无关。CoRL 明确要求 \"demonstrate the relevance to robotics\"，本 proposal 无任何 robotics 成分。这不是 \"might be borderline\" 的问题，是 100% out of scope。\n\n【主要风险】:\n1. **Predictability risk（idea 层面最大风险）**: 如果核心发现是 \"safety 确实比 capability 更 fragile\"，审稿人大概率评价为 \"confirmatory, not surprising\"。论文的价值将取决于 secondary findings（哪些 harm categories 最 fragile、scale 如何影响 fragility ratio、算法间差异）是否足够 surprising 来 carry the paper。\n2. **Venue mismatch risk（如果投 CoRL）**: 完全 out of scope，desk reject 概率极高。即使进入 review，也会因 \"no relevance to robotics\" 被直接拒绝。强烈建议更换目标会议。\n```\n\nSources:\n- [The Instability of Safety (Larsen 2025)](https://arxiv.org/abs/2512.12066)\n- [Fine-Tuning Lowers Safety (Fraser et al. 2025)](https://arxiv.org/abs/2506.17209)\n- [OXRL: Do Post-Training Algorithms Actually Differ?](https://arxiv.org/abs/2603.19335)\n- [SafeDPO (ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065)\n- [SafeTuneBed](https://arxiv.org/abs/2506.00676)\n- [RVPO: Risk-Sensitive Alignment](https://arxiv.org/abs/2605.05750)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [SafeGRPO](https://arxiv.org/abs/2511.12982)\n- [LLM-Safety Evaluations Lack Robustness](https://arxiv.org/abs/2503.02574)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 严重 Venue 不匹配警告】:\n本 proposal 研究的是 LLM 安全对齐的训练时可复现性（DPO/PPO/GRPO 跨 seed 安全方差），属于纯 NLP/AI Safety 课题。CoRL (Conference on Robot Learning) 聚焦于机器人学习——操纵、导航、机器人感知、sim-to-real 等。该 proposal 与机器人学习毫无关联，未涉及任何机器人应用场景。如果确实投稿 CoRL 主会，中稿概率接近 0%（desk reject 概率极高）。以下评估基于该 idea 投稿 **适配 venue**（如 NeurIPS/ICML/ICLR 主会、或 NeurIPS D&B track、ACL）的中稿潜力。如果用户确认目标就是 CoRL，请直接更换 venue。\n\n【领域调研】:\n- [Larsen, \"The Instability of Safety\" (arXiv:2512.12066, Dec 2025)](https://arxiv.org/abs/2512.12066): 推理时安全一致性研究。SSI 指标衡量同一模型在不同 sampling 配置下的拒答一致性。发现 18-28% prompts 出现 flip。关键：这是 inference-time（权重固定，sampling 随机性），不是 training-time。\n- [Fraser et al., \"Fine-Tuning Lowers Safety\" (arXiv:2506.17209, LLMSEC 2025)](https://arxiv.org/abs/2506.17209): **最直接的前驱工作**。首次展示 SFT 训练 seed 导致安全指标方差（5 seeds, Llama-1B/Mistral-7B, LoRA+4bit, SORRY-Bench, 最高 9pp 方差）。局限：仅 SFT、仅 LoRA、仅 2 个模型、仅 1 个 benchmark、无方差分解。\n- [OXRL (arXiv:2603.19335, Mar 2026)](https://arxiv.org/abs/2603.19335): 51 个 post-training 算法的受控对比框架，发现 scale-dependent ranking inversions。但 **零安全评估**，仅报告能力基准方差（GSM8K ±0.57pp）。\n- [SafeDPO (arXiv:2505.20065, ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065): DPO+PKU-SafeRLHF-30K 达 ~97% harmless ratio，确认方法+数据集成熟度。**未报告 cross-seed 方差**。\n- [SafeGRPO (arXiv:2511.12982, Nov 2025)](https://arxiv.org/abs/2511.12982): 验证 classifier-as-reward 范式用于 GRPO 安全对齐——是 multimodal 安全场景，非纯文本 LLM。\n- [SafeTuneBed (arXiv:2506.00676, May 2025)](https://arxiv.org/abs/2506.00676): 安全微调工具箱，提到 refusal consistency 但未正式定义/操作化。仅用 3 seeds。\n- [RVPO (arXiv:2605.05750, May 2026)](https://arxiv.org/abs/2605.05750): 从 Apple MLR，penalize inter-reward variance in single runs。方向相关但解决不同问题（单次训练中跨 RM 方差 vs. 跨 seed 方差）。\n- [LLM-Safety Evaluations Lack Robustness (arXiv:2503.02574, Mar 2025)](https://arxiv.org/abs/2503.02574): 评估 pipeline 选择导致最高 28% ASR 方差。\n\n- **调研总结**: 当前领域格局是——inference-time 安全不一致性已被 Larsen 记录；SFT-time 安全 seed 方差已被 Fraser et al. 初步证实（小规模）；preference optimization 方法（DPO/PPO/GRPO）的 training-time 安全方差确实无人系统研究。**这个 gap 是真实存在的**。但这是一个 \"natural next step\" 型 gap，而非一个 \"nobody thought of this\" 型 gap——Fraser et al. 的论文明确 call out 了这个扩展方向。\n\n【Trivial Alternative 检验】:\n**存在部分 trivial alternative 威胁。** 最简单的方案是：直接拿 Fraser et al. 的 setup，将 SFT 替换为 DPO/PPO/GRPO，跑 5-10 seeds，在 2-3 个 benchmark 上报告方差。这大概能用 proposal 1/10 的 compute 覆盖 proposal 60-70% 的核心发现。\n\nProposal 的增量价值在于：(a) 20 seeds + formal power analysis 带来统计可靠性；(b) full fine-tuning 消除 LoRA 初始化噪声混淆；(c) ANOVA 多因素方差分解；(d) 三尺度 scaling 分析；(e) minimum-seed lookup tables 的实用产出。这些增量是真实的，但本质是 **方法论严谨性和工程规模的提升**，不是概念性突破。审稿人可能会认为 \"做得更大更干净\" 不等于 \"想到了新东西\"。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有两个关键假设需要审视：\n\n1. **\"Safety 比 capability 方差更大\" 假设**：Proposal 的中心假设是 safety metrics 的 cross-seed 方差显著大于 capability metrics。这基于 Fraser (σ̂_safety ≈ 3.9pp) vs OXRL (σ̂_capability ≈ 0.55pp) 的 cross-study 比较。但这两个数字来自 **完全不同的实验设置**（不同模型、不同训练方法（SFT vs SGRPO）、不同规模、LoRA vs full FT）。用它们做 power analysis 的先验估计是合理的，但如果将其作为 \"safety fragility 比 capability fragility 高 ~50 倍\" 的证据来支撑核心假设的 motivation，逻辑上是不严密的。好消息是 proposal 本身就是要去验证这个假设，所以这不是 fatal flaw，但审稿人可能质疑 \"你的 motivation 已经预设了结论\"。\n\n2. **\"Full FT 能 cleanly isolate seed variance\" 假设**：Proposal 认为 full fine-tuning 消除了 LoRA 随机初始化噪声，因此能干净地分离 seed 方差。这是对的，但 full FT 引入了自己的方差来源——不同 seed 下权重更新路径的 chaotic divergence 在 full FT 中可能更剧烈（因为参数空间更大）。结果是：full FT 的 seed 方差可能比 LoRA 更大，但这不一定意味着 safety \"更 fragile\"——可能只是 full FT 本身方差更大。Proposal 缺乏 LoRA vs full FT 的对照来 disentangle 这个效应。\n\n3. **SCI-T 的有效性假设**：SCI-T(p) = max_c(n_c)/K 是一个非常简单的一致性指标（本质上是 majority vote 的比例）。它假设 binary REFUSE/COMPLY 分类已经足够刻画安全行为——但实际上，模型可能以不同程度 refuse（部分拒绝、带 disclaimer 回答等），binary 化会丢失这些 nuance。\n\n【3 维度打分】:\n\n1. **Novelty: 弱 (Weak)** — 核心 idea 是 \"把 Fraser et al. 从 SFT 扩展到 preference optimization，从小规模扩展到多规模，从 5 seeds 扩展到 20 seeds\"。这是一个 natural scale-up，而非概念性创新。Fraser et al. 自己在论文结语中就 call out 了 \"extend to preference optimization methods\" 作为 future work。SCI-T 是 SSI 的直接改写（把 inference randomness 替换为 training randomness），定义上几乎是 trivial extension（公式结构完全相同）。ANOVA 方差分解是标准统计方法，minimum-seed lookup table 是 standard power analysis 的 inverse application（Cédric et al. 2018 已提供方法论）。没有任何组件是 \"审稿人之前没见过\" 的。与 OXRL 相比，本质上是 \"OXRL + safety benchmarks\"。在 novelty 这个维度上，proposal 的贡献更接近 \"rigorous engineering\" 而非 \"new idea\"。\n\n2. **Significance: 中 (Medium)** — 研究问题本身是重要的：如果安全对齐在 retraining 下真的很脆弱，这对 AI 治理框架（EU AI Act, NIST AI RMF）有直接影响。Minimum-seed lookup tables 是有真实实用价值的 deliverable。但 significance 受限于两点：(a) 核心发现如果是 positive（\"safety 确实比 capability 更 fragile\"），大多数审稿人的反应会是 **\"I would have guessed this\"** 而不是 \"surprising\"——已有的 inference-time flip rate 证据（Larsen）和 SFT seed 证据（Fraser）已经让这个结论高度可预期；(b) 这是一个纯 measurement/characterization 研究，不提出新方法来解决发现的问题（不提出 \"如何使 safety alignment 更 robust\"），限制了其影响力的广度。\n\n3. **Related Work: 强 (Strong)** — 这是 proposal 最强的维度。相关工作覆盖全面且准确：所有关键引用（Larsen, Fraser, OXRL, SafeDPO, SafeGRPO, SafeTuneBed, PKU-SafeRLHF, RVPO）均已验证为真实存在的论文，描述准确。Gap 的定位清晰——\"no published work combines (a)-(f)\"——虽然这种 intersection novelty 可能被审稿人视为 \"stacking dimensions\" 而非真正创新，但差异化定位本身是 well-argued 的。\n\n【概率估计】: [15% - 28%] 中位 20%\n（注：此估计针对 **适配 venue**，如 NeurIPS/ICML 主会。若投稿 CoRL，概率降至 0-3%。若投稿 NeurIPS D&B track，概率可升至 25-35%。）\n\n【估计理由】:\nNovelty 是限制上界的核心维度。这是一个 \"natural next step\" 型实证研究，核心发现高度可预期（\"I would have guessed this\"），没有概念性突破。Significance 处于中等——问题重要但结果不 surprising。Related Work 很强但无法弥补 novelty 的不足。按照 rubric 锚点，这落在 \"idea 方向站得住脚但内核薄弱，存在 trivial alternative 威胁\" 的 15-25% 区间内，考虑到 related work 的扎实程度和 governance deliverable 的实用性，上界可以触及 28%。\n\n从审稿人视角：这篇论文会被认可为 \"well-executed, thorough, and needed\"，但审稿人更可能在 novelty/contribution 维度给 borderline-reject，理由是 \"the main finding is expected\" 和 \"this is more of an engineering/measurement contribution than a scientific contribution\"。\n\n【主要风险】:\n1. **\"I would have guessed this\" 风险**：如果核心发现确认 \"safety 比 capability 更 fragile under retraining\"，审稿人会认为这是已有证据的自然推论，不够 surprising。论文的价值将完全依赖于 **二阶发现**（例如 scale-dependent patterns、algorithm-specific fragility profiles、particular harm categories 的差异），但这些目前都是未知的——如果二阶发现平淡无奇，论文就只剩 \"confirming the obvious at scale\"。\n2. **纯 measurement 无 solution 风险**：Proposal 识别了 fragility 问题但不提出解决方案。对于偏好方法论贡献的 venue（如 NeurIPS main），审稿人可能期待 \"你发现了问题，那怎么 fix 它？\"。一个可能的补救方向是加入 seed averaging/ensemble 等简单 mitigation 实验，但这进一步增加 compute burden。\n```\n\nSources:\n- [The Instability of Safety (Larsen, 2025)](https://arxiv.org/abs/2512.12066)\n- [Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (Fraser et al., 2025)](https://arxiv.org/abs/2506.17209)\n- [OXRL: Do Post-Training Algorithms Actually Differ? (2026)](https://arxiv.org/abs/2603.19335)\n- [SafeDPO (ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065)\n- [SafeGRPO (2025)](https://arxiv.org/abs/2511.12982)\n- [SafeTuneBed (2025)](https://arxiv.org/abs/2506.00676)\n- [RVPO: Risk-Sensitive Alignment via Variance Regularization (2026)](https://arxiv.org/abs/2605.05750)\n- [LLM-Safety Evaluations Lack Robustness (2025)](https://arxiv.org/abs/2503.02574)\n- [Assessing Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs](https://arxiv.org/html/2503.07329v2)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# How Fragile Is Safety Under Retraining? A Large-Scale Reproducibility Audit of Post-Training Alignment\n\n## Description\nPreliminary evidence shows that safety alignment is fragile: Larsen (2025) found 18–28% of prompts flip between refusal and compliance across inference seeds, and Fraser et al. (2025) found up to 9-percentage-point variance in harmfulness scores across 5 SFT seeds on small models using LoRA. Yet no study has systematically measured training-time safety reproducibility for the preference optimization methods (DPO, PPO-RLHF, GRPO) that actually power deployed alignment, characterized how fragility scales with model size, disentangled LoRA initialization variance from seed variance, or provided power-justified minimum-seed recommendations for reliable safety claims. We propose the first large-scale training-time safety reproducibility audit of preference-based alignment. Using TRL v1.0's unified training stack with full fine-tuning throughout (eliminating LoRA initialization as a confound), we train DPO, PPO-RLHF, and GRPO on Qwen3-Instruct at 1.7B, 4B, and 8B scales with 20 seeds per configuration using PKU-SafeRLHF-30K safety preference data (~260 total runs including hardware and reward model ablations). The three algorithms cover distinct paradigms: offline preference optimization (DPO), online reward-model-based RL (PPO with Skywork/ArmoRM/FsfairX reward models), and online classifier-based RL (GRPO with WildGuard as safety reward). We evaluate on WildGuard, HarmBench, SORRY-Bench, and four capability benchmarks under a fixed evaluation pipeline. We introduce SCI-T (Safety Consistency Index for Training), extending Larsen's inference-time SSI to training-time: while SSI measures agreement across sampling randomness with fixed weights, SCI-T measures agreement across different training seeds under fixed inference—capturing fundamentally different learned safety boundaries. We decompose variance via ANOVA across seed, algorithm, scale, hardware, and reward model factors, testing the central hypothesis that safety is significantly more fragile than capabilities under retraining. A priori power analysis using Fraser et al.'s empirical variance (σ̂_safety ≈ 3.9pp) and OXRL's capability baseline (σ̂_capability ≈ 0.55pp) confirms 20 seeds provides ≥88% power for detecting safety/capability variance ratios ≥3:1 and ≥82% power for ANOVA interaction effects. The primary deliverable is empirically-grounded minimum-seed lookup tables for AI governance frameworks.\n\n## Core Problem\nWhen the same preference-based alignment algorithm (DPO/PPO-RLHF/GRPO) is rerun with different random seeds, hardware configurations, or reward model instances, how much do safety properties—refusal behavior, harmlessness scores, and instance-level safety decisions—vary compared to general capabilities? Preliminary evidence from SFT (Fraser et al. 2025) and inference-time sampling (Larsen 2025) shows safety decisions are surprisingly inconsistent, but no study has systematically measured training-time safety reproducibility for the preference optimization methods that actually power deployed safety alignment (PPO-RLHF at OpenAI/Anthropic, DPO in open-source pipelines, GRPO at DeepSeek), or characterized how this fragility scales with model size.\n\n## Opportunity\nThree converging lines of evidence create a clear gap. First, Larsen (arXiv:2512.12066) introduced the Safety Stability Index (SSI) showing 18–28% of prompts flip between refusal and compliance across inference seeds and temperatures—but this measures generation-level variance with fixed model weights, not the deeper question of whether retraining produces models with fundamentally different safety boundaries. Second, Fraser et al. (arXiv:2506.17209) demonstrated up to 9-percentage-point variance in harmfulness scores across 5 SFT seeds on Llama-3.2-1B and Mistral-7B using LoRA with 4-bit quantization and SORRY-Bench—establishing that training-time safety variance exists but leaving preference-based alignment (DPO/PPO/GRPO), larger scales, multi-benchmark evaluation, LoRA-vs-full-FT variance confounds, and formal consistency metrics unexplored. Third, OXRL (arXiv:2603.19335) revealed dramatic scale-dependent ranking inversions across post-training algorithms on capability benchmarks using Qwen 2.5 at 0.5B–7B, but evaluated no safety properties. Fourth, SafeDPO (arXiv:2505.20065, ICLR 2026 Oral) demonstrated that safety alignment via DPO on PKU-SafeRLHF-30K can achieve ~97% harmless ratio, establishing both the dataset and method as mature—but reported no cross-seed variance. Meanwhile, TRL v1.0 (March 2026) now provides a unified training stack for DPO, PPO, and GRPO, eliminating infrastructure confounds. We propose to close this gap with the first large-scale, multi-algorithm, multi-scale reproducibility audit of training-time safety alignment, using full fine-tuning throughout to cleanly isolate training-seed variance from LoRA initialization noise.\n\n## Related Work / Landscape\nLarsen (arXiv:2512.12066, Dec 2025) introduced the SSI metric measuring per-prompt refusal agreement across inference configurations (5 seeds × 4 temperatures), finding 18–28% flip rates on BeaverTails across four 7–12B models. Critically, SSI captures generation-level stochasticity (same weights, different sampling), not model-level variance from retraining. Fraser et al. (arXiv:2506.17209, June 2025, LLMSEC) studied SFT seed variance with 5 seeds on Llama-3.2-1B and Mistral-7B using LoRA with 4-bit quantization and AdamW-8bit optimizer, evaluating on SORRY-Bench (440 class-balanced unsafe instructions); they found up to 9pp harmfulness score variance (e.g., 0.73 to 0.82 on Llama-1B fine-tuned on Dolly) and called for 'multiple runs to estimate random variation' but used only SFT, not preference optimization, and did not disentangle LoRA initialization variance from true seed variance. SafeTuneBed (arXiv:2506.00676, May 2025) offers a fine-tuning safety toolkit that averages results over 3 seeds and lists 'refusal consistency' as a metric but never formally defines or operationalizes it. OXRL (arXiv:2603.19335, March 2026) provides a controlled framework for 51 post-training algorithms using Qwen 2.5 Instruct at 0.5B–7B with full FT at ≤3B and LoRA (rank 16, α=32) at 7B, using 3–5 seeds per configuration on GSM8K self-play data—but evaluates only capability benchmarks with no safety evaluation. Notably, OXRL found scale-dependent ranking inversions (SimPO worst at 1.5B, best at 7B) and cross-seed std of ±0.57pp on GSM8K for SGRPO at 1.5B with 5 seeds, establishing a baseline for capability variance. SafeDPO (arXiv:2505.20065, ICLR 2026 Oral) achieves ~97% harmless ratio using DPO on PKU-SafeRLHF-30K but reports no cross-seed variance. The 'LLM-Safety Evaluations Lack Robustness' paper (arXiv:2503.02574, March 2025) demonstrates that evaluation pipeline choices cause up to 28% ASR variance, motivating fixed-evaluation-pipeline designs. SafeGRPO (arXiv:2511.12982, Nov 2025) proposes rule-governed reward construction for GRPO-based safety alignment, demonstrating that safety classifiers can serve as GRPO reward signals—validating our approach to using WildGuard as GRPO's safety reward function. TRL v1.0 (March 2026) provides a unified post-training stack for SFT, DPO, PPO, and GRPO with consistent infrastructure, enabling fair cross-algorithm comparison. PKU-SafeRLHF (arXiv:2406.15513, ACL 2025) provides 30K+ expert comparisons with decoupled safety/helpfulness annotations across 19 harm categories and 3 severity levels—the standard safety preference dataset used by SafeDPO and related work. Open-source reward models (Skywork-Reward-Llama-3.1-8B-v0.2, ArmoRM-Llama3-8B-v0.1, FsfairX-LLaMA3-RM-v0.1) achieve strong RewardBench scores including explicit safety dimensions, enabling controlled reward model ablations for PPO. No published work combines: (a) three distinct alignment paradigms (offline DPO, online PPO-RLHF, online GRPO), (b) multiple model scales with full fine-tuning, (c) ≥20 seeds per configuration with a priori power justification, (d) multiple safety benchmarks with fixed evaluation pipeline, (e) a formal training-time consistency metric, and (f) separated variance decomposition across seed, algorithm, scale, hardware, and reward model factors.\n\n## Approach\nPhase 1 — Infrastructure (3 weeks): Build unified training and evaluation pipeline using TRL v1.0 as the training backbone and OXRL-inspired evaluation infrastructure. Training setup: Configure DPO, PPO-RLHF, and GRPO trainers in TRL v1.0 with full fine-tuning at all scales using DeepSpeed ZeRO-2 for memory management at 8B. We use full fine-tuning throughout (not LoRA) to eliminate LoRA random A/B matrix initialization as a variance source—a confound identified in Fraser et al.'s LoRA-based SFT study where LoRA initialization and seed variance were entangled. This increases compute by ~50% at 8B but produces cleaner variance isolation, which is essential for a paper whose central contribution is variance decomposition. Preference dataset: PKU-SafeRLHF-30K (PKU-Alignment, ACL 2025), selected for three reasons: (i) decoupled safety/helpfulness annotations enable isolating safety-specific preference learning, (ii) it is the standard benchmark used by SafeDPO (ICLR 2026 Oral) enabling direct comparability, (iii) 19 harm categories with 3 severity levels enable fine-grained analysis of which safety dimensions are most fragile. Dataset adaptation per algorithm: DPO receives safety preference pairs directly (safer response as chosen, less safe as rejected); PPO uses the 27K prompts with an external reward model scoring generated responses; GRPO uses the same prompts with WildGuard (7B) as a binary safety classifier reward (safe=1, unsafe=0), following the classifier-as-reward paradigm validated by SafeGRPO (arXiv:2511.12982). Evaluation pipeline: Fix the evaluation pipeline completely (WildGuard as primary safety judge, deterministic decoding at temperature=0, fixed chat template, bf16 quantization) per the robustness findings of arXiv:2503.02574 to isolate training-time variance from evaluation-time variance. Integrate WildGuard (prompt + response classification, 7B Mistral-based), HarmBench (400 harmful behaviors with 7B Mistral classifier), SORRY-Bench (440 category-balanced unsafe instructions), and capability benchmarks (GSM8K, MATH, AlpacaEval 2, MT-Bench).\n\nPhase 2 — Training Runs (6–7 weeks): Algorithm selection rationale: We select DPO, PPO-RLHF, and GRPO to cover three fundamentally distinct alignment paradigms—(i) DPO: offline, reference-model-regularized preference optimization without a reward model, the dominant method in open-source safety alignment; (ii) PPO-RLHF: online, reward-model-based reinforcement learning, the method deployed for safety-critical systems at OpenAI and Anthropic; (iii) GRPO: online, group-relative optimization with classifier-based rewards, the emerging paradigm (DeepSeek-R1) increasingly applied to safety via SafeGRPO. This replaces the originally proposed SimPO, which is architecturally a DPO variant (reference-free but still offline preference optimization)—including both DPO and SimPO would over-represent the offline paradigm while leaving online RL unrepresented, creating an algorithmic coverage gap for the methods that actually power deployed safety alignment. Core runs: Train DPO, PPO, and GRPO on Qwen3-Instruct at three scales (1.7B, 4B, 8B) with 20 random seeds each, holding all hyperparameters fixed per algorithm. Full fine-tuning with DeepSpeed ZeRO-2; 1 H100 for 1.7B/4B DPO/GRPO, 2 H100s for 8B and all PPO runs (policy + reference + reward/value models). Total core: 180 runs (3 × 3 × 20). Hardware ablation: For the 8B DPO configuration, run 20 seeds on A100-80GB vs H100-80GB and 20 seeds with bf16 vs fp16 to isolate hardware/precision effects (40 additional runs, comparing against the 20 core H100/bf16 runs). Reward model ablation: For the 8B PPO configuration, run 20 seeds each with three independently-developed open-source reward models: (RM1) Skywork-Reward-Llama-3.1-8B-v0.2 — Bradley-Terry RM, #1 on RewardBench among 8B models, trained on Skywork's curated preference data; (RM2) ArmoRM-Llama3-8B-v0.1 — multi-objective RM with mixture-of-experts gating across 19 reward dimensions including an explicit safety objective, 89.0 RewardBench overall; (RM3) FsfairX-LLaMA3-RM-v0.1 — Bradley-Terry RM trained on the RLHFlow dataset, different training distribution from Skywork. The core PPO runs use ArmoRM as default (its explicit safety dimension makes it most appropriate for safety alignment); the ablation adds 40 additional runs with Skywork-RM and FsfairX-RM. All three RMs are ~8B parameters, Llama-3-based, publicly available, and independently trained with different objectives, architectures (Bradley-Terry vs MoE-gated multi-objective), and training data—providing genuine variance in the reward signal. Total runs: 180 core + 40 hardware + 40 reward model = 260 runs.\n\nPhase 3 — Evaluation and Analysis (3–4 weeks): For each of 260 checkpoints, evaluate safety (WildGuard refusal rate on WildGuardTest 5K subset, HarmBench ASR with 400 behaviors, SORRY-Bench harmfulness with 440 prompts) and capabilities (GSM8K 1.3K, MATH 5K, AlpacaEval 2 805 prompts, MT-Bench 80 turns). All safety evaluations use deterministic decoding (temperature=0) to ensure SCI-T captures training-time variance only. Introduce the Safety Consistency Index for Training (SCI-T), explicitly extending Larsen's SSI from inference-time to training-time: SCI-T(p) = max_c(n_c) / K where n_c counts training-seed runs in category c ∈ {REFUSE, COMPLY} and K = number of seeds. While SSI measures whether the same model produces consistent safety decisions across sampling randomness, SCI-T measures whether different models (from different training seeds) make consistent safety decisions under fixed inference conditions (temperature=0). This distinction matters because training-time inconsistency implies fundamentally different learned safety boundaries, not mere sampling noise. Compute SCI-T for every prompt × algorithm × scale combination. Apply ANOVA decomposition: Var(safety_metric) = Var(seed) + Var(algorithm) + Var(scale) + Var(hardware) + Var(reward_model) + Var(algorithm×scale) + residual. Test the central hypothesis: safety properties exhibit significantly higher cross-seed variance than capability properties at the same scale, and this differential fragility changes with scale. Additionally analyze which of PKU-SafeRLHF's 19 harm categories show highest SCI-T fragility—identifying 'fragile safety categories' that are most sensitive to training randomness.\n\nPhase 4 — Minimum-Seed Recommendations (2–3 weeks): A priori power justification for 20 seeds: We apply Cédric et al.'s (2018) framework to our own experimental design before running. From Fraser et al.'s empirical data: 5 SFT seeds on Llama-1B produced harmfulness scores ranging 0.73–0.82, yielding σ̂_safety ≈ 3.9pp (range/d₂ for n=5). From OXRL: 5 SGRPO seeds at 1.5B on GSM8K produced ±0.57pp std, yielding σ̂_capability ≈ 0.55pp. For our central F-test (H₀: σ²_safety = σ²_capability vs H₁: σ²_safety > σ²_capability) with df=(19,19): at true variance ratio λ=3 (conservative estimate from Fraser/OXRL data suggesting λ≈50), power ≥ 0.88 at α=0.05. For ANOVA main effects (3 levels, N=180, medium effect f=0.25): power ≈ 0.92. For ANOVA interactions (3×3 design, df=(4,171)): power ≈ 0.82 for medium effects. For variance estimation precision: with n=20 (df=19), the 95% CI for σ² spans a factor of 3.69 (χ²_{0.975,19}/χ²_{0.025,19} = 32.85/8.91), sufficient for categorizing configurations as 'high-fragility' vs 'low-fragility.' Conclusion: 20 seeds per cell provides ≥80% power for all planned analyses, meeting the standard power threshold. Adaptive provision: if Phase 2 pilot (first 5 seeds per cell) reveals smaller effect sizes than estimated, we increase to 25 seeds with ~25% additional compute within budget contingency. Post-hoc deliverable: Using the full empirical variance estimates, derive minimum seed counts needed for P(detecting a true safety difference ≥ δ) ≥ 0.8 at α=0.05 via inverse power analysis. Produce concrete lookup tables: 'To claim safety refusal rate ≥ R% with 95% confidence for algorithm X at scale Y, run ≥ N seeds.' This is the actionable regulatory deliverable targeting EU AI Act verifiable safety requirements and NIST AI RMF reproducibility standards.\n\n## Inspiration\nExtension: Larsen's SSI measures inference-time safety agreement; we extend this concept to training-time agreement across different model weights, a fundamentally harder reproducibility challenge since different weights may encode different safety boundaries. Scale-up: Fraser et al.'s SFT seed study (2 models, 5 seeds, 1 benchmark, LoRA) demonstrated the phenomenon exists; we scale to 3 algorithms × 3 model sizes × 20 seeds × 4 benchmarks with full fine-tuning (eliminating LoRA initialization variance) and formal ANOVA decomposition. Bridge: OXRL's controlled post-training infrastructure + TRL v1.0's unified training stack + PKU-SafeRLHF-30K's decoupled safety preference data + WildGuard/HarmBench classifiers can be composed to create a safety-aware reproducibility audit pipeline that none provides alone. Safety reward signals: SafeGRPO's demonstration that safety classifiers can serve as GRPO reward functions validates our approach to using WildGuard as GRPO's reward signal for safety alignment. Reward model variance: ArmoRM's multi-objective design (with explicit safety dimension), Skywork-Reward's top RewardBench performance, and FsfairX's Bradley-Terry approach provide three independently-trained reward models for PPO ablation, operationalizing RVPO's concern about inter-reward variance. Statistical grounding: Cédric et al.'s power analysis framework for RL seed selection (arXiv:1806.08295) provides the methodology for deriving minimum-seed recommendations—never applied to safety alignment. We apply it a priori to justify our 20-seed design.\n\n## Key References\n- The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior (arXiv:2512.12066, Dec 2025) — introduces SSI metric for inference-time refusal consistency; SCI-T extends SSI to training-time\n- Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (arXiv:2506.17209, June 2025, LLMSEC) — first evidence of training-seed safety variance: 9pp range across 5 SFT seeds on Llama-1B with LoRA/4-bit, SORRY-Bench; establishes σ̂_safety ≈ 3.9pp used in our power analysis\n- SafeTuneBed: A Toolkit for Benchmarking LLM Safety Alignment in Fine-Tuning (arXiv:2506.00676, May 2025) — safety fine-tuning toolkit with 3-seed averaging; mentions 'refusal consistency' without formal definition\n- Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales (arXiv:2603.19335, March 2026) — OXRL framework, Qwen 2.5 at 0.5B–7B, scale-dependent ranking inversions, ±0.57pp GSM8K std providing σ̂_capability baseline for our power analysis\n- LLM-Safety Evaluations Lack Robustness (arXiv:2503.02574, March 2025) — evaluation pipeline variance up to 28%, motivates our fixed-pipeline design\n- PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference (arXiv:2406.15513, ACL 2025) — 30K+ expert comparisons with decoupled safety/helpfulness annotations across 19 harm categories; our primary training dataset\n- SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety (arXiv:2505.20065, ICLR 2026 Oral) — achieves ~97% harmless ratio via DPO on PKU-SafeRLHF-30K; establishes dataset+method maturity but reports no cross-seed variance\n- SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization (arXiv:2511.12982, Nov 2025) — validates classifier-as-reward paradigm for GRPO safety alignment; motivates our WildGuard-as-reward design\n- TRL v1.0: Post-Training Library Built to Move with the Field (Hugging Face, March 2026) — unified training stack for DPO, PPO, GRPO eliminating infrastructure confounds across algorithms\n- How Many Random Seeds? Statistical Power Analysis in Deep RL Experiments (arXiv:1806.08295, 2018) — methodology for minimum-seed derivation via power analysis; we extend to safety alignment and apply a priori to justify our 20-seed design\n- What Matters For Safety Alignment? (arXiv:2601.03868, Jan 2026) — cross-model safety comparison across 32 models and 13 families\n- WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs (arXiv:2406.18495, 2024) — 7B safety classifier achieving 94.7% F1 on response harmfulness; our primary safety judge and GRPO reward signal\n- Skywork-Reward: Bag of Tricks for Reward Modeling in LLMs (arXiv:2410.18451, 2024) — Skywork-Reward-Llama-3.1-8B-v0.2, #1 8B model on RewardBench; one of three PPO reward models in our ablation\n- Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts (arXiv:2406.12845, 2024) — ArmoRM-Llama3-8B-v0.1, 89.0 RewardBench with explicit safety dimension; default PPO reward model\n- Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping (arXiv 2020) — seed variance methodology for NLP\n- Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs (IJCNLP-AACL 2025) — macro/micro consistency metrics for LLM fine-tuning\n- RVPO: Risk-Sensitive Alignment via Variance Regularization (arXiv:2605.05750, May 2026) — inter-reward variance penalization in single runs; motivates reward model ablation\n- Improving Safety Alignment via Balanced Direct Preference Optimization (arXiv:2603.22829, March 2026) — safety alignment overfitting in DPO\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv:2603.02229, March 2026) — safety-helpfulness Pareto frontier under DPO\n- Reproducibility in Machine-Learning-Based Research: Overview, Barriers, and Drivers (AI Magazine 2025)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '~2,800 H100-hours total: ~1,600 training (260 runs across 3 algorithms × 3 scales × 20+ seeds, all full fine-tuning with DeepSpeed ZeRO-2; PPO runs require 2 H100s for policy+reference+RM) + ~1,200 evaluation (260 checkpoints × 8 benchmarks including WildGuard 7B and HarmBench 7B classifier inference, each checkpoint requiring ~3-4 GPU-hours for generation + classification across all benchmarks)', 'timeline': '17–19 weeks (infrastructure + TRL v1.0 pipeline setup 3w, training runs 6–7w on 8×H100 cluster, evaluation 3–4w, statistical analysis + minimum-seed derivation + paper writing 5–6w)', 'estimated_gpu_cost': '$7,000 at ~$2.50/H100-hr on mid-tier providers'}\n- **human_in_loop**: {'gpu_hours': '~2,800 H100-hours (identical core compute; full FT precludes further memory optimization)', 'timeline': '14–16 weeks (Claude accelerates TRL v1.0 pipeline integration, ANOVA analysis scripts, power analysis code, per-category fragility analysis, and paper drafting)', 'claude_api_cost': '$500–700 (Sonnet 4.6 for code generation, statistical analysis automation, and drafting; ~150M tokens)', 'estimated_gpu_cost': '$7,000'}\n- **auto_research**: {'gpu_hours': '~2,800 H100-hours', 'timeline': '11–14 weeks (parallelized experiment orchestration with automated sweep management, evaluation pipelines, and ANOVA analysis)', 'claude_api_cost': '$1,500–2,200 (experiment orchestration, automated analysis, full paper draft generation; ~600M tokens)', 'estimated_gpu_cost': '$7,000', 'speed_bottleneck': 'GPU cluster queue time for 260 training jobs (PPO runs ~2× longer than DPO/GRPO due to multi-model training); sequential dependency between training completion and safety evaluation; WildGuard 7B + HarmBench 7B classifier inference throughput across 260 checkpoints × ~6K safety evaluation prompts each'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T21:11:11.498Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:11:11.498Z",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T21:11:11.511Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ 致命性前置问题：venue mismatch（投稿目标错误）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

在进入 idea 质量评估之前，必须首先指出：

**本 proposal 与 CoRL 2026 存在根本性的 venue mismatch。** 

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求：
- 投稿必须聚焦于核心的 robotics problem
- 必须展示所提出的 models/algorithms/datasets/benchmarks 对 robotics 的 relevance
- "Submissions without a robotics focus will be returned without review"（无机器人焦点的投稿将不经审稿直接退回）

本 proposal 的内容是 **LLM 安全对齐的训练时可复现性审计**——完全属于 NLP/AI Safety 领域，与 robot learning 无任何交集。投稿 CoRL 将 100% 被 desk reject。

**如果用户实际目标是 NeurIPS 2026、ICML 2026、ICLR 2027 或 EMNLP 2026 等 NLP/ML 主会，以下 idea 质量评估仍然适用。** 以下评估假设投稿目标是一个接受 LLM safety 话题的 top venue（如 NeurIPS/ICML/ICLR）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【领域调研】:

- [Larsen 2025, arXiv:2512.12066] (Dec 2025): 提出 SSI 指标，发现 18–28% 的 prompt 在不同 inference seed/temperature 下在 refusal 和 compliance 之间翻转。本 proposal 的直接前驱，但仅关注 inference-time variance（固定权重），未触及 training-time variance。论文存在且描述准确。

- [Fraser et al. 2025, arXiv:2506.17209] (June 2025, LLMSEC): 首次证明 training-seed variance 影响安全性——5 个 SFT seed 在 Llama-3.2-1B 上产生最高 9pp 的 harmfulness score 变化。使用 LoRA + 4-bit quantization + SORRY-Bench。论文存在且描述准确。**但注意：这是 SFT 而非 preference optimization，且仅 5 seeds、2 models、1 benchmark——proposal 将其作为核心 gap 依据是合理的。**

- [OXRL, arXiv:2603.19335] (March 2026): 51 种 post-training 算法在 Qwen 2.5 (0.5B–7B) 上的 controlled comparison。发现 scale-dependent ranking inversions（SimPO 在 1.5B 最差、7B 最好）。提供了 GSM8K 上 SGRPO 的 cross-seed std ±0.57pp 作为 capability variance baseline。**但 OXRL 未做任何 safety evaluation**——proposal 准确地将此定位为 gap。

- [SafeDPO, arXiv:2505.20065] (ICLR 2026 Oral): DPO + PKU-SafeRLHF-30K 达到 ~97% harmless ratio。确认了数据集和方法的成熟度，但未报告 cross-seed variance。论文存在且描述准确。

- [SafeGRPO, arXiv:2511.12982] (Nov 2025): 验证了 classifier-as-reward 的 GRPO 安全对齐范式。论文存在。

- [SafeTuneBed, arXiv:2506.00676] (May 2025): 安全微调 toolkit，3-seed averaging，提到 refusal consistency 但未正式定义。

- [LLM-Safety Evaluations Lack Robustness, arXiv:2503.02574] (March 2025): evaluation pipeline 选择导致最高 28% ASR variance，动机化了 fixed-pipeline 设计。

- [TRACEALIGN, arXiv:2508.02063] (2025): 追踪对齐失败到训练时信念来源，减少 alignment drift 达 85%，但方法论完全不同（mechanistic interpretation vs empirical audit）。

- 调研总结：**safety alignment 的 fragility 是一个已被多个角度初步验证的现象（inference-time: Larsen; SFT training-time: Fraser; evaluation pipeline: arXiv:2503.02574），但 preference-based alignment (DPO/PPO/GRPO) 的 training-time safety reproducibility 确实没有被系统研究过。** 该 gap 真实存在，但 gap 的 "width" 有限——核心问题方向已被邻近工作大致框定，本 proposal 的贡献本质是 scale-up + 组合 + 方法扩展。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁。**

核心问题是"safety 在 retraining 中是否比 capability 更 fragile"。一个成本远低的替代方案是：
1. 仅跑 DPO 一种算法（最成熟的 open-source 方法），在 1-2 个 scale 上，用 10 seeds，对比 safety vs capability variance。这已经足以回答核心问题，compute 成本不到 proposal 的 1/5。
2. 如果发现 safety 确实更 fragile（高概率，因为 Fraser et al. 已在 SFT 上证明了），增量发现不令人惊讶。
3. 260 runs 的大规模设计增加了 **thoroughness**（hardware ablation, reward model ablation, 3 algorithms × 3 scales），但这些都是实验设计层面的完善，不改变核心发现的 novelty。

增量价值在于：(a) 覆盖三种不同范式的 preference optimization 而非仅 SFT；(b) ANOVA 方差分解跨多因素；(c) minimum-seed lookup tables 的实用工具。但这些增量价值更接近 "engineering thoroughness" 而非 "conceptual breakthrough"。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【前提假设检验】:

核心 claim 逻辑链中有以下未经验证的假设：

1. **"Safety 比 capability 在 training-time 上更 fragile" 几乎是预期结论。** Fraser et al. 在 SFT 上已经显示 9pp safety variance vs 一般认为的 <1pp capability variance。如果 preference optimization 也呈现相同模式，审稿人会说 "I would have guessed this"——safety decisions 本质上是在 decision boundary 附近的二元分类，而 capability（如 GSM8K 准确率）是在整个分布上的聚合指标，前者天然更 noisy。这不需要大规模实验来"发现"，更像是在验证一个已有的 prior。

2. **SCI-T 的学术贡献被高估。** SCI-T(p) = max_c(n_c)/K 本质上就是"K 个 seed 中多数决策的比例"——这是一个 trivially simple metric。Proposal 将其包装为"extending Larsen's SSI to training-time"，但实际上 SSI 也是一个简单的 agreement metric，从 inference-time 到 training-time 的"扩展"不涉及任何方法论创新，仅仅是改变了 variance source（sampling noise → training noise）。

3. **Minimum-seed lookup tables 的假设前提。** 这些 tables 假设 variance 在不同 hyperparameter settings、不同 base models、不同数据集上是稳定的（否则 tables 不可推广）。但 variance 高度依赖于具体配置，一个在 Qwen3 + PKU-SafeRLHF 上得出的 "minimum 15 seeds" 结论对 Llama + 其他数据集是否适用，完全未被论证。

4. **Full fine-tuning 消除 LoRA confound 的论证是合理的**，但也引入了新问题——real-world deployment 中很多人用 LoRA，full FT 的结论对 LoRA practitioners 的实用性受限。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心发现方向（safety 比 capability 更 fragile under retraining）已被 Fraser et al. 在 SFT 上初步证明，Larsen 在 inference-time 上证明。Proposal 的 novelty delta 是"从 SFT 扩展到 DPO/PPO/GRPO + 从 2 models 扩展到 3 scales + 从 5 seeds 扩展到 20 seeds + ANOVA 分解"——这是 **quantitative scaling**，不是 qualitative leap。SCI-T 是一个 trivial metric（max agreement ratio），几乎不贡献方法论 novelty。Minimum-seed tables 是标准 power analysis 的直接应用（Cédric et al. 2018），方法论上无新意。OXRL (arXiv:2603.19335) 已经建立了 controlled post-training comparison 的范式，本 proposal 本质上是将 OXRL 的框架加了 safety 维度。

2. **Significance: 中** — 
   研究问题本身重要——AI governance 需要知道 safety claim 的 reproducibility bound，EU AI Act 和 NIST AI RMF 确实需要这类 empirical evidence。但问题的重要性和 idea 的 contribution 是两回事。如果核心发现是 "safety 确实比 capability 更 fragile"（高概率如此），这不令人惊讶。如果核心发现是 "safety 和 capability 一样 stable"（低概率），那反而更 surprising 和有价值。Proposal 的 dual-outcome 设计部分缓解了这个问题，但主路径的 expected finding 缺乏 surprise value。

3. **Related Work: 强** — 
   Proposal 对 related work 的覆盖异常全面，清晰定位了与 Larsen (inference-time), Fraser et al. (SFT, small-scale), OXRL (capability-only), SafeDPO (no variance), SafeGRPO (method validation), SafeTuneBed (3-seed, no metric) 各自的差异。引用的论文经核实均真实存在，描述准确。差异化定位清晰：no prior work combines (a) preference optimization, (b) multi-scale, (c) 20+ seeds, (d) multi-benchmark, (e) formal metric, (f) ANOVA decomposition——这是事实。但 related work 的完善度本身也暴露了一个问题：prior work 已经非常接近这个 proposal 在做的事情，剩余的 gap 相对狭窄。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【概率估计】: 

- 如投 CoRL 2026: 0%（desk reject，venue mismatch，无任何 robotics 内容）
- 如投适当 venue（NeurIPS/ICML/ICLR）: [18% - 28%]，中位 22%

【估计理由】:

Idea 处于 rubric 中 "15-25%: idea 方向站得住脚但内核薄弱" 到 "25-35%: idea 有实质内核但 expected finding not surprising" 的边界。

向上拉的因素：
- 研究问题对 AI governance 确实重要（Significance 中等偏上）
- 实验设计严谨（但这是执行层面，不影响 idea 评分）
- Related work 定位清晰，gap 真实存在

向下拉的因素（限制上界的关键维度：**Novelty**）：
- 核心 expected finding（safety > capability fragility）缺乏 surprise value——审稿人大概率会说 "I would have guessed this"
- 贡献本质是 scale-up + combination of existing directions，不是 conceptual innovation
- SCI-T 和 minimum-seed tables 的方法论贡献过于 trivial
- 存在明显的 trivial alternative：小规模实验即可验证核心 hypothesis

Novelty 是限制上界的主要维度。即使实验执行完美，idea 的 ceiling 也在 ~30%。

【主要风险】:

1. **"Confirmatory study" 质疑**：核心发现（safety 比 capability 更 fragile）几乎是 prior work 的直接预期推论——审稿人可能认为这是一个 expensive 但 unsurprising 的 confirmatory study，而非 discovery paper。在 top venue 中，"the answer is what we expected, but now we know for sure" 型论文的接受门槛远高于 "surprising finding" 型论文。

2. **Generalizability 质疑**：所有实验基于 Qwen3-Instruct + PKU-SafeRLHF-30K 这一组合。Minimum-seed lookup tables 的推广性（到不同 base model families, 不同 safety 数据集, 不同 scale ranges）缺乏理论保障——审稿人会质疑 "your tables are for Qwen3 on PKU-SafeRLHF; why should I trust them for my Llama model on my dataset?"
```

---

**补充说明**：本 proposal 在**形式完善度**上极高——power analysis、ANOVA 设计、dual-outcome、多 ablation 等都表明作者具有强实验设计能力。但形式完善度本身不等于 idea 质量。如果将此 proposal 视为一个 "empirical benchmark/audit" 类型的贡献（类似 HELM、AlpacaEval 等 benchmark paper），而非一个 "discovery" paper，投稿 workshop（如 NeurIPS SafeGenAI workshop）或 Datasets & Benchmarks track 可能更匹配其贡献类型。

Sources:
- [The Instability of Safety (Larsen 2025)](https://arxiv.org/abs/2512.12066)
- [Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (Fraser et al. 2025)](https://arxiv.org/abs/2506.17209)
- [OXRL: Do Post-Training Algorithms Actually Differ? (2026)](https://arxiv.org/abs/2603.19335)
- [SafeDPO (ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)
- [Assessing Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs](https://arxiv.org/html/2503.07329v2)
- [TRACEALIGN](https://arxiv.org/pdf/2508.02063)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to produce my evaluation. Let me synthesize.

---

```
【阶段】: Triage

⚠️ 【重要前置警告：严重的投稿目标不匹配】
CoRL (Conference on Robot Learning) 的投稿范围明确要求论文 "focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics"。本 proposal 是一篇纯 LLM 安全对齐可复现性的实证研究，不涉及任何机器人学习内容。投稿 CoRL 几乎必然被 desk reject。本 proposal 更适合的目标会议包括：NeurIPS (尤其 Datasets & Benchmarks track)、ICML、ACL/EMNLP、或 AAAI。以下评估基于 idea 本身的质量（假设投稿到一个 scope 匹配的顶会），但请注意若坚持投 CoRL，中稿概率接近 0%。

【领域调研】:
- [Larsen 2025, arXiv:2512.12066] (Dec 2025): 提出 SSI 指标，发现 18-28% 的 prompt 在不同 inference seed/temperature 下 refusal 行为翻转。核心局限：只测量 inference-time variance（固定权重，不同采样），不涉及 training-time variance。本 proposal 正确识别了这一gap。
- [Fraser et al. 2025, arXiv:2506.17209] (LLMSEC 2025): 首次实证 SFT seed variance 对 safety 的影响，5 seeds、LoRA+4bit、SORRY-Bench，发现最高 9pp harmfulness score variance。核心局限：只用 SFT（非 preference optimization），LoRA 初始化 variance 与 seed variance 纠缠，样本量小。本 proposal 的核心论据来源。
- [OXRL, arXiv:2603.19335] (March 2026): 51 种 post-training 算法在 Qwen 2.5 (0.5B-7B) 的受控对比，发现 scale-dependent ranking inversions，3-5 seeds per config，但完全没有 safety evaluation。提供了 capability variance baseline (±0.57pp on GSM8K)。
- [SafeDPO, arXiv:2505.20065] (ICLR 2026 Oral): DPO on PKU-SafeRLHF-30K 达到 ~97% harmless ratio，确立了数据集和方法的成熟度，但未报告任何 cross-seed variance。
- [SafeTuneBed, arXiv:2506.00676] (May 2025): 安全微调工具包，3-seed averaging，提到 "refusal consistency" 但未正式定义。
- [RVPO, arXiv:2605.05750] (May 2026, Apple): 提出 inter-reward variance penalty，在 multi-objective alignment 中惩罚 reward 间方差。与本 proposal 的 reward model ablation 动机相关但方法不同。
- [arXiv:2503.02574] (March 2025): 证明 evaluation pipeline 选择可导致最高 28% ASR variance，支持本 proposal 的 fixed-pipeline 设计。
- [SafeGRPO, arXiv:2511.12982] (Nov 2025): 验证 classifier-as-reward 用于 GRPO 安全对齐的可行性。
- 调研总结：training-time safety reproducibility 确实是一个被 identify 但未被系统研究的 gap。Fraser et al. 开了头（SFT only, small scale），OXRL 建了基础设施（capability only），但两者的交叉——preference optimization 的 training-time safety variance——确实没有被覆盖。这个 gap 是真实的。

【Trivial Alternative 检验】:
存在中等程度的 trivial alternative 威胁。最直接的替代方案：
1. **简单 scale-up Fraser et al.**: 直接将 Fraser 的实验从 SFT 扩展到 DPO/PPO/GRPO，用 5-10 seeds（而非 20），不需要 ANOVA、SCI-T 等完整框架，即可获得 "preference optimization 也有 safety variance" 这一核心发现。本 proposal 的增量在于统计严谨性（power analysis、20 seeds、variance decomposition）和系统性（多算法、多尺度、多 benchmark），但这些是 rigor 的增量，非 insight 的增量。
2. **直接复用 OXRL 框架加 safety eval**: 在 OXRL 已有的 controlled runs 上追加 safety evaluation（WildGuard/HarmBench），即可获得 safety vs. capability variance 的直接对比，无需从头训练 260 runs。
3. SCI-T 指标本质是 max(n_refuse, n_comply)/K，与 SSI 是同一公式、不同的 variance source。这不是一个有深度的 methodological contribution。

增量价值在于：(a) 完整的 ANOVA variance decomposition across 5 factors，(b) power-justified 20-seed design，(c) minimum-seed lookup tables 的 governance 应用价值。这些是工程完备性和实用价值的增量，而非概念性突破。

【前提假设检验】:
核心 claim 的逻辑链中有以下未经验证的假设：
1. **"Safety 比 capability 在 training-time 更 fragile" 是预期结论，不是 surprising finding。** 大多数 alignment 研究者会预测这个结果，因为：safety 行为是对边界情况的学习、safety 训练数据相对 noisy、safety 与 helpfulness 之间存在张力创造不稳定的优化面。如果结论是 positive，审稿人大概率会说 "I would have guessed this"。如果结论是 negative（safety 比 capability 更稳定），这反而更 surprising 也更有发表价值。
2. **从 Fraser et al. 的 SFT/LoRA 实验外推 σ̂_safety ≈ 3.9pp 用于 preference optimization 的 power analysis 是有风险的。** DPO/PPO/GRPO 的优化 landscape 与 SFT 有本质不同，实际 variance 可能远大或远小于 3.9pp。作者提到了 adaptive provision（pilot 后增加到 25 seeds），但 power analysis 的前提假设本身是 borrowed 的。
3. **Full fine-tuning 是否真的 "cleanly isolates" training-seed variance 也存疑。** Full FT 引入了更多参数自由度，可能使 variance 更大，也可能因为优化更充分而更小。"消除 LoRA confound" 的逻辑成立，但 full FT 本身也引入了新的 confound（更高的 overfitting 风险、不同的 loss landscape）。
4. **WildGuard 同时作为 GRPO 的 reward signal 和 evaluation judge 存在评估循环。** 虽然这在 safety alignment 研究中常见，但审稿人可能会质疑：GRPO 训出的模型在 WildGuard eval 上表现好只是因为它 overfit 到了 WildGuard 的判断偏好。

【3 维度打分】:
1. **Novelty: 弱-中** — 核心贡献是将已知方法论（seed variance analysis、ANOVA、power analysis）系统性地应用到一个新场景（preference optimization safety）。SCI-T 是 SSI 的直接平移，ANOVA 和 power analysis 是标准统计工具。Gap 是真实的（Fraser et al. 只做了 SFT，OXRL 没有 safety eval），但填补方式是 "scale up + apply standard tools"，而非提出新的 conceptual framework。对比 OXRL（arXiv:2603.19335）发现了 scale-dependent ranking inversions 这样的 surprising finding，本 proposal 预期的核心 finding（safety 更 fragile）缺乏 surprise value。
2. **Significance: 中** — 研究问题本身很重要：safety alignment 的可复现性直接影响 AI governance 和部署决策。Minimum-seed lookup tables 有真实的政策应用价值（EU AI Act、NIST AI RMF）。但影响力主要在 evaluation methodology 和 governance，不在推进 alignment 算法本身。这是一个 "measurement" paper，不是一个 "mechanism" paper。对领域的推动是增量性的——它不会改变人们做 alignment 的方式，只会改变人们评估 alignment 的方式。
3. **Related Work: 强** — 对相关工作的覆盖非常全面且准确。每篇引用的论文都真实存在且描述准确（Larsen arXiv:2512.12066 ✓，Fraser arXiv:2506.17209 ✓，OXRL arXiv:2603.19335 ✓，SafeDPO ICLR 2026 Oral ✓，RVPO arXiv:2605.05750 ✓）。差异化定位清晰——明确说明了 Fraser (SFT only)、OXRL (capability only)、Larsen (inference only) 各自的局限，以及本 proposal 如何覆盖交叉地带。唯一的小瑕疵是 SafeTuneBed (arXiv:2506.00676) 已经在做类似的 safety fine-tuning benchmark + seed averaging，但 proposal 正确指出了它"mentioned but never formally defined" refusal consistency。

【概率估计】（假设投稿到 scope 匹配的顶会如 NeurIPS/ICML/ACL）: [20% - 32%] 中位 25%
【如果坚持投 CoRL】: [0% - 3%] 中位 1%

【估计理由】:
Idea 内核是一个设计精良、动机充分的大规模实证 audit，填补了一个真实的 gap。Related work 覆盖优秀，实验设计（如果执行到位）会产出有用的 governance deliverables。但三个因素限制了上界：
(1) **Novelty 天花板低**——核心贡献是 "apply standard methodology to new domain" 而非 conceptual breakthrough，SCI-T 缺乏方法论深度；
(2) **核心 finding 的 surprise value 低**——"safety 比 capability 更 fragile" 是大多数人的 prior，positive result 确认性强但缺乏 "aha moment"；
(3) **Trivial alternative 存在**——一个 50% compute 成本的简化版实验（5-10 seeds、2 algorithms、1 scale）可能产出定性相同的结论，使得 260 runs 的完整 audit 在 marginal insight/compute 比上不够高效。

这使得 idea 落在 "solid but expected" 区间 (25-35%)，但因 surprise value 偏低，中位数在该区间的下半部分。

**投 CoRL 的额外致命问题**: 这篇论文与 robot learning 完全无关。CoRL 明确要求 "demonstrate the relevance to robotics"，本 proposal 无任何 robotics 成分。这不是 "might be borderline" 的问题，是 100% out of scope。

【主要风险】:
1. **Predictability risk（idea 层面最大风险）**: 如果核心发现是 "safety 确实比 capability 更 fragile"，审稿人大概率评价为 "confirmatory, not surprising"。论文的价值将取决于 secondary findings（哪些 harm categories 最 fragile、scale 如何影响 fragility ratio、算法间差异）是否足够 surprising 来 carry the paper。
2. **Venue mismatch risk（如果投 CoRL）**: 完全 out of scope，desk reject 概率极高。即使进入 review，也会因 "no relevance to robotics" 被直接拒绝。强烈建议更换目标会议。
```

Sources:
- [The Instability of Safety (Larsen 2025)](https://arxiv.org/abs/2512.12066)
- [Fine-Tuning Lowers Safety (Fraser et al. 2025)](https://arxiv.org/abs/2506.17209)
- [OXRL: Do Post-Training Algorithms Actually Differ?](https://arxiv.org/abs/2603.19335)
- [SafeDPO (ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065)
- [SafeTuneBed](https://arxiv.org/abs/2506.00676)
- [RVPO: Risk-Sensitive Alignment](https://arxiv.org/abs/2605.05750)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [SafeGRPO](https://arxiv.org/abs/2511.12982)
- [LLM-Safety Evaluations Lack Robustness](https://arxiv.org/abs/2503.02574)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【⚠️ 严重 Venue 不匹配警告】:
本 proposal 研究的是 LLM 安全对齐的训练时可复现性（DPO/PPO/GRPO 跨 seed 安全方差），属于纯 NLP/AI Safety 课题。CoRL (Conference on Robot Learning) 聚焦于机器人学习——操纵、导航、机器人感知、sim-to-real 等。该 proposal 与机器人学习毫无关联，未涉及任何机器人应用场景。如果确实投稿 CoRL 主会，中稿概率接近 0%（desk reject 概率极高）。以下评估基于该 idea 投稿 **适配 venue**（如 NeurIPS/ICML/ICLR 主会、或 NeurIPS D&B track、ACL）的中稿潜力。如果用户确认目标就是 CoRL，请直接更换 venue。

【领域调研】:
- [Larsen, "The Instability of Safety" (arXiv:2512.12066, Dec 2025)](https://arxiv.org/abs/2512.12066): 推理时安全一致性研究。SSI 指标衡量同一模型在不同 sampling 配置下的拒答一致性。发现 18-28% prompts 出现 flip。关键：这是 inference-time（权重固定，sampling 随机性），不是 training-time。
- [Fraser et al., "Fine-Tuning Lowers Safety" (arXiv:2506.17209, LLMSEC 2025)](https://arxiv.org/abs/2506.17209): **最直接的前驱工作**。首次展示 SFT 训练 seed 导致安全指标方差（5 seeds, Llama-1B/Mistral-7B, LoRA+4bit, SORRY-Bench, 最高 9pp 方差）。局限：仅 SFT、仅 LoRA、仅 2 个模型、仅 1 个 benchmark、无方差分解。
- [OXRL (arXiv:2603.19335, Mar 2026)](https://arxiv.org/abs/2603.19335): 51 个 post-training 算法的受控对比框架，发现 scale-dependent ranking inversions。但 **零安全评估**，仅报告能力基准方差（GSM8K ±0.57pp）。
- [SafeDPO (arXiv:2505.20065, ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065): DPO+PKU-SafeRLHF-30K 达 ~97% harmless ratio，确认方法+数据集成熟度。**未报告 cross-seed 方差**。
- [SafeGRPO (arXiv:2511.12982, Nov 2025)](https://arxiv.org/abs/2511.12982): 验证 classifier-as-reward 范式用于 GRPO 安全对齐——是 multimodal 安全场景，非纯文本 LLM。
- [SafeTuneBed (arXiv:2506.00676, May 2025)](https://arxiv.org/abs/2506.00676): 安全微调工具箱，提到 refusal consistency 但未正式定义/操作化。仅用 3 seeds。
- [RVPO (arXiv:2605.05750, May 2026)](https://arxiv.org/abs/2605.05750): 从 Apple MLR，penalize inter-reward variance in single runs。方向相关但解决不同问题（单次训练中跨 RM 方差 vs. 跨 seed 方差）。
- [LLM-Safety Evaluations Lack Robustness (arXiv:2503.02574, Mar 2025)](https://arxiv.org/abs/2503.02574): 评估 pipeline 选择导致最高 28% ASR 方差。

- **调研总结**: 当前领域格局是——inference-time 安全不一致性已被 Larsen 记录；SFT-time 安全 seed 方差已被 Fraser et al. 初步证实（小规模）；preference optimization 方法（DPO/PPO/GRPO）的 training-time 安全方差确实无人系统研究。**这个 gap 是真实存在的**。但这是一个 "natural next step" 型 gap，而非一个 "nobody thought of this" 型 gap——Fraser et al. 的论文明确 call out 了这个扩展方向。

【Trivial Alternative 检验】:
**存在部分 trivial alternative 威胁。** 最简单的方案是：直接拿 Fraser et al. 的 setup，将 SFT 替换为 DPO/PPO/GRPO，跑 5-10 seeds，在 2-3 个 benchmark 上报告方差。这大概能用 proposal 1/10 的 compute 覆盖 proposal 60-70% 的核心发现。

Proposal 的增量价值在于：(a) 20 seeds + formal power analysis 带来统计可靠性；(b) full fine-tuning 消除 LoRA 初始化噪声混淆；(c) ANOVA 多因素方差分解；(d) 三尺度 scaling 分析；(e) minimum-seed lookup tables 的实用产出。这些增量是真实的，但本质是 **方法论严谨性和工程规模的提升**，不是概念性突破。审稿人可能会认为 "做得更大更干净" 不等于 "想到了新东西"。

【前提假设检验】:
核心 claim 的逻辑链条中有两个关键假设需要审视：

1. **"Safety 比 capability 方差更大" 假设**：Proposal 的中心假设是 safety metrics 的 cross-seed 方差显著大于 capability metrics。这基于 Fraser (σ̂_safety ≈ 3.9pp) vs OXRL (σ̂_capability ≈ 0.55pp) 的 cross-study 比较。但这两个数字来自 **完全不同的实验设置**（不同模型、不同训练方法（SFT vs SGRPO）、不同规模、LoRA vs full FT）。用它们做 power analysis 的先验估计是合理的，但如果将其作为 "safety fragility 比 capability fragility 高 ~50 倍" 的证据来支撑核心假设的 motivation，逻辑上是不严密的。好消息是 proposal 本身就是要去验证这个假设，所以这不是 fatal flaw，但审稿人可能质疑 "你的 motivation 已经预设了结论"。

2. **"Full FT 能 cleanly isolate seed variance" 假设**：Proposal 认为 full fine-tuning 消除了 LoRA 随机初始化噪声，因此能干净地分离 seed 方差。这是对的，但 full FT 引入了自己的方差来源——不同 seed 下权重更新路径的 chaotic divergence 在 full FT 中可能更剧烈（因为参数空间更大）。结果是：full FT 的 seed 方差可能比 LoRA 更大，但这不一定意味着 safety "更 fragile"——可能只是 full FT 本身方差更大。Proposal 缺乏 LoRA vs full FT 的对照来 disentangle 这个效应。

3. **SCI-T 的有效性假设**：SCI-T(p) = max_c(n_c)/K 是一个非常简单的一致性指标（本质上是 majority vote 的比例）。它假设 binary REFUSE/COMPLY 分类已经足够刻画安全行为——但实际上，模型可能以不同程度 refuse（部分拒绝、带 disclaimer 回答等），binary 化会丢失这些 nuance。

【3 维度打分】:

1. **Novelty: 弱 (Weak)** — 核心 idea 是 "把 Fraser et al. 从 SFT 扩展到 preference optimization，从小规模扩展到多规模，从 5 seeds 扩展到 20 seeds"。这是一个 natural scale-up，而非概念性创新。Fraser et al. 自己在论文结语中就 call out 了 "extend to preference optimization methods" 作为 future work。SCI-T 是 SSI 的直接改写（把 inference randomness 替换为 training randomness），定义上几乎是 trivial extension（公式结构完全相同）。ANOVA 方差分解是标准统计方法，minimum-seed lookup table 是 standard power analysis 的 inverse application（Cédric et al. 2018 已提供方法论）。没有任何组件是 "审稿人之前没见过" 的。与 OXRL 相比，本质上是 "OXRL + safety benchmarks"。在 novelty 这个维度上，proposal 的贡献更接近 "rigorous engineering" 而非 "new idea"。

2. **Significance: 中 (Medium)** — 研究问题本身是重要的：如果安全对齐在 retraining 下真的很脆弱，这对 AI 治理框架（EU AI Act, NIST AI RMF）有直接影响。Minimum-seed lookup tables 是有真实实用价值的 deliverable。但 significance 受限于两点：(a) 核心发现如果是 positive（"safety 确实比 capability 更 fragile"），大多数审稿人的反应会是 **"I would have guessed this"** 而不是 "surprising"——已有的 inference-time flip rate 证据（Larsen）和 SFT seed 证据（Fraser）已经让这个结论高度可预期；(b) 这是一个纯 measurement/characterization 研究，不提出新方法来解决发现的问题（不提出 "如何使 safety alignment 更 robust"），限制了其影响力的广度。

3. **Related Work: 强 (Strong)** — 这是 proposal 最强的维度。相关工作覆盖全面且准确：所有关键引用（Larsen, Fraser, OXRL, SafeDPO, SafeGRPO, SafeTuneBed, PKU-SafeRLHF, RVPO）均已验证为真实存在的论文，描述准确。Gap 的定位清晰——"no published work combines (a)-(f)"——虽然这种 intersection novelty 可能被审稿人视为 "stacking dimensions" 而非真正创新，但差异化定位本身是 well-argued 的。

【概率估计】: [15% - 28%] 中位 20%
（注：此估计针对 **适配 venue**，如 NeurIPS/ICML 主会。若投稿 CoRL，概率降至 0-3%。若投稿 NeurIPS D&B track，概率可升至 25-35%。）

【估计理由】:
Novelty 是限制上界的核心维度。这是一个 "natural next step" 型实证研究，核心发现高度可预期（"I would have guessed this"），没有概念性突破。Significance 处于中等——问题重要但结果不 surprising。Related Work 很强但无法弥补 novelty 的不足。按照 rubric 锚点，这落在 "idea 方向站得住脚但内核薄弱，存在 trivial alternative 威胁" 的 15-25% 区间内，考虑到 related work 的扎实程度和 governance deliverable 的实用性，上界可以触及 28%。

从审稿人视角：这篇论文会被认可为 "well-executed, thorough, and needed"，但审稿人更可能在 novelty/contribution 维度给 borderline-reject，理由是 "the main finding is expected" 和 "this is more of an engineering/measurement contribution than a scientific contribution"。

【主要风险】:
1. **"I would have guessed this" 风险**：如果核心发现确认 "safety 比 capability 更 fragile under retraining"，审稿人会认为这是已有证据的自然推论，不够 surprising。论文的价值将完全依赖于 **二阶发现**（例如 scale-dependent patterns、algorithm-specific fragility profiles、particular harm categories 的差异），但这些目前都是未知的——如果二阶发现平淡无奇，论文就只剩 "confirming the obvious at scale"。
2. **纯 measurement 无 solution 风险**：Proposal 识别了 fragility 问题但不提出解决方案。对于偏好方法论贡献的 venue（如 NeurIPS main），审稿人可能期待 "你发现了问题，那怎么 fix 它？"。一个可能的补救方向是加入 seed averaging/ensemble 等简单 mitigation 实验，但这进一步增加 compute burden。
```

Sources:
- [The Instability of Safety (Larsen, 2025)](https://arxiv.org/abs/2512.12066)
- [Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (Fraser et al., 2025)](https://arxiv.org/abs/2506.17209)
- [OXRL: Do Post-Training Algorithms Actually Differ? (2026)](https://arxiv.org/abs/2603.19335)
- [SafeDPO (ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065)
- [SafeGRPO (2025)](https://arxiv.org/abs/2511.12982)
- [SafeTuneBed (2025)](https://arxiv.org/abs/2506.00676)
- [RVPO: Risk-Sensitive Alignment via Variance Regularization (2026)](https://arxiv.org/abs/2605.05750)
- [LLM-Safety Evaluations Lack Robustness (2025)](https://arxiv.org/abs/2503.02574)
- [Assessing Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs](https://arxiv.org/html/2503.07329v2)


【原始 proposal（允许参考但不是主要依据）】:
# How Fragile Is Safety Under Retraining? A Large-Scale Reproducibility Audit of Post-Training Alignment

## Description
Preliminary evidence shows that safety alignment is fragile: Larsen (2025) found 18–28% of prompts flip between refusal and compliance across inference seeds, and Fraser et al. (2025) found up to 9-percentage-point variance in harmfulness scores across 5 SFT seeds on small models using LoRA. Yet no study has systematically measured training-time safety reproducibility for the preference optimization methods (DPO, PPO-RLHF, GRPO) that actually power deployed alignment, characterized how fragility scales with model size, disentangled LoRA initialization variance from seed variance, or provided power-justified minimum-seed recommendations for reliable safety claims. We propose the first large-scale training-time safety reproducibility audit of preference-based alignment. Using TRL v1.0's unified training stack with full fine-tuning throughout (eliminating LoRA initialization as a confound), we train DPO, PPO-RLHF, and GRPO on Qwen3-Instruct at 1.7B, 4B, and 8B scales with 20 seeds per configuration using PKU-SafeRLHF-30K safety preference data (~260 total runs including hardware and reward model ablations). The three algorithms cover distinct paradigms: offline preference optimization (DPO), online reward-model-based RL (PPO with Skywork/ArmoRM/FsfairX reward models), and online classifier-based RL (GRPO with WildGuard as safety reward). We evaluate on WildGuard, HarmBench, SORRY-Bench, and four capability benchmarks under a fixed evaluation pipeline. We introduce SCI-T (Safety Consistency Index for Training), extending Larsen's inference-time SSI to training-time: while SSI measures agreement across sampling randomness with fixed weights, SCI-T measures agreement across different training seeds under fixed inference—capturing fundamentally different learned safety boundaries. We decompose variance via ANOVA across seed, algorithm, scale, hardware, and reward model factors, testing the central hypothesis that safety is significantly more fragile than capabilities under retraining. A priori power analysis using Fraser et al.'s empirical variance (σ̂_safety ≈ 3.9pp) and OXRL's capability baseline (σ̂_capability ≈ 0.55pp) confirms 20 seeds provides ≥88% power for detecting safety/capability variance ratios ≥3:1 and ≥82% power for ANOVA interaction effects. The primary deliverable is empirically-grounded minimum-seed lookup tables for AI governance frameworks.

## Core Problem
When the same preference-based alignment algorithm (DPO/PPO-RLHF/GRPO) is rerun with different random seeds, hardware configurations, or reward model instances, how much do safety properties—refusal behavior, harmlessness scores, and instance-level safety decisions—vary compared to general capabilities? Preliminary evidence from SFT (Fraser et al. 2025) and inference-time sampling (Larsen 2025) shows safety decisions are surprisingly inconsistent, but no study has systematically measured training-time safety reproducibility for the preference optimization methods that actually power deployed safety alignment (PPO-RLHF at OpenAI/Anthropic, DPO in open-source pipelines, GRPO at DeepSeek), or characterized how this fragility scales with model size.

## Opportunity
Three converging lines of evidence create a clear gap. First, Larsen (arXiv:2512.12066) introduced the Safety Stability Index (SSI) showing 18–28% of prompts flip between refusal and compliance across inference seeds and temperatures—but this measures generation-level variance with fixed model weights, not the deeper question of whether retraining produces models with fundamentally different safety boundaries. Second, Fraser et al. (arXiv:2506.17209) demonstrated up to 9-percentage-point variance in harmfulness scores across 5 SFT seeds on Llama-3.2-1B and Mistral-7B using LoRA with 4-bit quantization and SORRY-Bench—establishing that training-time safety variance exists but leaving preference-based alignment (DPO/PPO/GRPO), larger scales, multi-benchmark evaluation, LoRA-vs-full-FT variance confounds, and formal consistency metrics unexplored. Third, OXRL (arXiv:2603.19335) revealed dramatic scale-dependent ranking inversions across post-training algorithms on capability benchmarks using Qwen 2.5 at 0.5B–7B, but evaluated no safety properties. Fourth, SafeDPO (arXiv:2505.20065, ICLR 2026 Oral) demonstrated that safety alignment via DPO on PKU-SafeRLHF-30K can achieve ~97% harmless ratio, establishing both the dataset and method as mature—but reported no cross-seed variance. Meanwhile, TRL v1.0 (March 2026) now provides a unified training stack for DPO, PPO, and GRPO, eliminating infrastructure confounds. We propose to close this gap with the first large-scale, multi-algorithm, multi-scale reproducibility audit of training-time safety alignment, using full fine-tuning throughout to cleanly isolate training-seed variance from LoRA initialization noise.

## Related Work / Landscape
Larsen (arXiv:2512.12066, Dec 2025) introduced the SSI metric measuring per-prompt refusal agreement across inference configurations (5 seeds × 4 temperatures), finding 18–28% flip rates on BeaverTails across four 7–12B models. Critically, SSI captures generation-level stochasticity (same weights, different sampling), not model-level variance from retraining. Fraser et al. (arXiv:2506.17209, June 2025, LLMSEC) studied SFT seed variance with 5 seeds on Llama-3.2-1B and Mistral-7B using LoRA with 4-bit quantization and AdamW-8bit optimizer, evaluating on SORRY-Bench (440 class-balanced unsafe instructions); they found up to 9pp harmfulness score variance (e.g., 0.73 to 0.82 on Llama-1B fine-tuned on Dolly) and called for 'multiple runs to estimate random variation' but used only SFT, not preference optimization, and did not disentangle LoRA initialization variance from true seed variance. SafeTuneBed (arXiv:2506.00676, May 2025) offers a fine-tuning safety toolkit that averages results over 3 seeds and lists 'refusal consistency' as a metric but never formally defines or operationalizes it. OXRL (arXiv:2603.19335, March 2026) provides a controlled framework for 51 post-training algorithms using Qwen 2.5 Instruct at 0.5B–7B with full FT at ≤3B and LoRA (rank 16, α=32) at 7B, using 3–5 seeds per configuration on GSM8K self-play data—but evaluates only capability benchmarks with no safety evaluation. Notably, OXRL found scale-dependent ranking inversions (SimPO worst at 1.5B, best at 7B) and cross-seed std of ±0.57pp on GSM8K for SGRPO at 1.5B with 5 seeds, establishing a baseline for capability variance. SafeDPO (arXiv:2505.20065, ICLR 2026 Oral) achieves ~97% harmless ratio using DPO on PKU-SafeRLHF-30K but reports no cross-seed variance. The 'LLM-Safety Evaluations Lack Robustness' paper (arXiv:2503.02574, March 2025) demonstrates that evaluation pipeline choices cause up to 28% ASR variance, motivating fixed-evaluation-pipeline designs. SafeGRPO (arXiv:2511.12982, Nov 2025) proposes rule-governed reward construction for GRPO-based safety alignment, demonstrating that safety classifiers can serve as GRPO reward signals—validating our approach to using WildGuard as GRPO's safety reward function. TRL v1.0 (March 2026) provides a unified post-training stack for SFT, DPO, PPO, and GRPO with consistent infrastructure, enabling fair cross-algorithm comparison. PKU-SafeRLHF (arXiv:2406.15513, ACL 2025) provides 30K+ expert comparisons with decoupled safety/helpfulness annotations across 19 harm categories and 3 severity levels—the standard safety preference dataset used by SafeDPO and related work. Open-source reward models (Skywork-Reward-Llama-3.1-8B-v0.2, ArmoRM-Llama3-8B-v0.1, FsfairX-LLaMA3-RM-v0.1) achieve strong RewardBench scores including explicit safety dimensions, enabling controlled reward model ablations for PPO. No published work combines: (a) three distinct alignment paradigms (offline DPO, online PPO-RLHF, online GRPO), (b) multiple model scales with full fine-tuning, (c) ≥20 seeds per configuration with a priori power justification, (d) multiple safety benchmarks with fixed evaluation pipeline, (e) a formal training-time consistency metric, and (f) separated variance decomposition across seed, algorithm, scale, hardware, and reward model factors.

## Approach
Phase 1 — Infrastructure (3 weeks): Build unified training and evaluation pipeline using TRL v1.0 as the training backbone and OXRL-inspired evaluation infrastructure. Training setup: Configure DPO, PPO-RLHF, and GRPO trainers in TRL v1.0 with full fine-tuning at all scales using DeepSpeed ZeRO-2 for memory management at 8B. We use full fine-tuning throughout (not LoRA) to eliminate LoRA random A/B matrix initialization as a variance source—a confound identified in Fraser et al.'s LoRA-based SFT study where LoRA initialization and seed variance were entangled. This increases compute by ~50% at 8B but produces cleaner variance isolation, which is essential for a paper whose central contribution is variance decomposition. Preference dataset: PKU-SafeRLHF-30K (PKU-Alignment, ACL 2025), selected for three reasons: (i) decoupled safety/helpfulness annotations enable isolating safety-specific preference learning, (ii) it is the standard benchmark used by SafeDPO (ICLR 2026 Oral) enabling direct comparability, (iii) 19 harm categories with 3 severity levels enable fine-grained analysis of which safety dimensions are most fragile. Dataset adaptation per algorithm: DPO receives safety preference pairs directly (safer response as chosen, less safe as rejected); PPO uses the 27K prompts with an external reward model scoring generated responses; GRPO uses the same prompts with WildGuard (7B) as a binary safety classifier reward (safe=1, unsafe=0), following the classifier-as-reward paradigm validated by SafeGRPO (arXiv:2511.12982). Evaluation pipeline: Fix the evaluation pipeline completely (WildGuard as primary safety judge, deterministic decoding at temperature=0, fixed chat template, bf16 quantization) per the robustness findings of arXiv:2503.02574 to isolate training-time variance from evaluation-time variance. Integrate WildGuard (prompt + response classification, 7B Mistral-based), HarmBench (400 harmful behaviors with 7B Mistral classifier), SORRY-Bench (440 category-balanced unsafe instructions), and capability benchmarks (GSM8K, MATH, AlpacaEval 2, MT-Bench).

Phase 2 — Training Runs (6–7 weeks): Algorithm selection rationale: We select DPO, PPO-RLHF, and GRPO to cover three fundamentally distinct alignment paradigms—(i) DPO: offline, reference-model-regularized preference optimization without a reward model, the dominant method in open-source safety alignment; (ii) PPO-RLHF: online, reward-model-based reinforcement learning, the method deployed for safety-critical systems at OpenAI and Anthropic; (iii) GRPO: online, group-relative optimization with classifier-based rewards, the emerging paradigm (DeepSeek-R1) increasingly applied to safety via SafeGRPO. This replaces the originally proposed SimPO, which is architecturally a DPO variant (reference-free but still offline preference optimization)—including both DPO and SimPO would over-represent the offline paradigm while leaving online RL unrepresented, creating an algorithmic coverage gap for the methods that actually power deployed safety alignment. Core runs: Train DPO, PPO, and GRPO on Qwen3-Instruct at three scales (1.7B, 4B, 8B) with 20 random seeds each, holding all hyperparameters fixed per algorithm. Full fine-tuning with DeepSpeed ZeRO-2; 1 H100 for 1.7B/4B DPO/GRPO, 2 H100s for 8B and all PPO runs (policy + reference + reward/value models). Total core: 180 runs (3 × 3 × 20). Hardware ablation: For the 8B DPO configuration, run 20 seeds on A100-80GB vs H100-80GB and 20 seeds with bf16 vs fp16 to isolate hardware/precision effects (40 additional runs, comparing against the 20 core H100/bf16 runs). Reward model ablation: For the 8B PPO configuration, run 20 seeds each with three independently-developed open-source reward models: (RM1) Skywork-Reward-Llama-3.1-8B-v0.2 — Bradley-Terry RM, #1 on RewardBench among 8B models, trained on Skywork's curated preference data; (RM2) ArmoRM-Llama3-8B-v0.1 — multi-objective RM with mixture-of-experts gating across 19 reward dimensions including an explicit safety objective, 89.0 RewardBench overall; (RM3) FsfairX-LLaMA3-RM-v0.1 — Bradley-Terry RM trained on the RLHFlow dataset, different training distribution from Skywork. The core PPO runs use ArmoRM as default (its explicit safety dimension makes it most appropriate for safety alignment); the ablation adds 40 additional runs with Skywork-RM and FsfairX-RM. All three RMs are ~8B parameters, Llama-3-based, publicly available, and independently trained with different objectives, architectures (Bradley-Terry vs MoE-gated multi-objective), and training data—providing genuine variance in the reward signal. Total runs: 180 core + 40 hardware + 40 reward model = 260 runs.

Phase 3 — Evaluation and Analysis (3–4 weeks): For each of 260 checkpoints, evaluate safety (WildGuard refusal rate on WildGuardTest 5K subset, HarmBench ASR with 400 behaviors, SORRY-Bench harmfulness with 440 prompts) and capabilities (GSM8K 1.3K, MATH 5K, AlpacaEval 2 805 prompts, MT-Bench 80 turns). All safety evaluations use deterministic decoding (temperature=0) to ensure SCI-T captures training-time variance only. Introduce the Safety Consistency Index for Training (SCI-T), explicitly extending Larsen's SSI from inference-time to training-time: SCI-T(p) = max_c(n_c) / K where n_c counts training-seed runs in category c ∈ {REFUSE, COMPLY} and K = number of seeds. While SSI measures whether the same model produces consistent safety decisions across sampling randomness, SCI-T measures whether different models (from different training seeds) make consistent safety decisions under fixed inference conditions (temperature=0). This distinction matters because training-time inconsistency implies fundamentally different learned safety boundaries, not mere sampling noise. Compute SCI-T for every prompt × algorithm × scale combination. Apply ANOVA decomposition: Var(safety_metric) = Var(seed) + Var(algorithm) + Var(scale) + Var(hardware) + Var(reward_model) + Var(algorithm×scale) + residual. Test the central hypothesis: safety properties exhibit significantly higher cross-seed variance than capability properties at the same scale, and this differential fragility changes with scale. Additionally analyze which of PKU-SafeRLHF's 19 harm categories show highest SCI-T fragility—identifying 'fragile safety categories' that are most sensitive to training randomness.

Phase 4 — Minimum-Seed Recommendations (2–3 weeks): A priori power justification for 20 seeds: We apply Cédric et al.'s (2018) framework to our own experimental design before running. From Fraser et al.'s empirical data: 5 SFT seeds on Llama-1B produced harmfulness scores ranging 0.73–0.82, yielding σ̂_safety ≈ 3.9pp (range/d₂ for n=5). From OXRL: 5 SGRPO seeds at 1.5B on GSM8K produced ±0.57pp std, yielding σ̂_capability ≈ 0.55pp. For our central F-test (H₀: σ²_safety = σ²_capability vs H₁: σ²_safety > σ²_capability) with df=(19,19): at true variance ratio λ=3 (conservative estimate from Fraser/OXRL data suggesting λ≈50), power ≥ 0.88 at α=0.05. For ANOVA main effects (3 levels, N=180, medium effect f=0.25): power ≈ 0.92. For ANOVA interactions (3×3 design, df=(4,171)): power ≈ 0.82 for medium effects. For variance estimation precision: with n=20 (df=19), the 95% CI for σ² spans a factor of 3.69 (χ²_{0.975,19}/χ²_{0.025,19} = 32.85/8.91), sufficient for categorizing configurations as 'high-fragility' vs 'low-fragility.' Conclusion: 20 seeds per cell provides ≥80% power for all planned analyses, meeting the standard power threshold. Adaptive provision: if Phase 2 pilot (first 5 seeds per cell) reveals smaller effect sizes than estimated, we increase to 25 seeds with ~25% additional compute within budget contingency. Post-hoc deliverable: Using the full empirical variance estimates, derive minimum seed counts needed for P(detecting a true safety difference ≥ δ) ≥ 0.8 at α=0.05 via inverse power analysis. Produce concrete lookup tables: 'To claim safety refusal rate ≥ R% with 95% confidence for algorithm X at scale Y, run ≥ N seeds.' This is the actionable regulatory deliverable targeting EU AI Act verifiable safety requirements and NIST AI RMF reproducibility standards.

## Inspiration
Extension: Larsen's SSI measures inference-time safety agreement; we extend this concept to training-time agreement across different model weights, a fundamentally harder reproducibility challenge since different weights may encode different safety boundaries. Scale-up: Fraser et al.'s SFT seed study (2 models, 5 seeds, 1 benchmark, LoRA) demonstrated the phenomenon exists; we scale to 3 algorithms × 3 model sizes × 20 seeds × 4 benchmarks with full fine-tuning (eliminating LoRA initialization variance) and formal ANOVA decomposition. Bridge: OXRL's controlled post-training infrastructure + TRL v1.0's unified training stack + PKU-SafeRLHF-30K's decoupled safety preference data + WildGuard/HarmBench classifiers can be composed to create a safety-aware reproducibility audit pipeline that none provides alone. Safety reward signals: SafeGRPO's demonstration that safety classifiers can serve as GRPO reward functions validates our approach to using WildGuard as GRPO's reward signal for safety alignment. Reward model variance: ArmoRM's multi-objective design (with explicit safety dimension), Skywork-Reward's top RewardBench performance, and FsfairX's Bradley-Terry approach provide three independently-trained reward models for PPO ablation, operationalizing RVPO's concern about inter-reward variance. Statistical grounding: Cédric et al.'s power analysis framework for RL seed selection (arXiv:1806.08295) provides the methodology for deriving minimum-seed recommendations—never applied to safety alignment. We apply it a priori to justify our 20-seed design.

## Key References
- The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior (arXiv:2512.12066, Dec 2025) — introduces SSI metric for inference-time refusal consistency; SCI-T extends SSI to training-time
- Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (arXiv:2506.17209, June 2025, LLMSEC) — first evidence of training-seed safety variance: 9pp range across 5 SFT seeds on Llama-1B with LoRA/4-bit, SORRY-Bench; establishes σ̂_safety ≈ 3.9pp used in our power analysis
- SafeTuneBed: A Toolkit for Benchmarking LLM Safety Alignment in Fine-Tuning (arXiv:2506.00676, May 2025) — safety fine-tuning toolkit with 3-seed averaging; mentions 'refusal consistency' without formal definition
- Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales (arXiv:2603.19335, March 2026) — OXRL framework, Qwen 2.5 at 0.5B–7B, scale-dependent ranking inversions, ±0.57pp GSM8K std providing σ̂_capability baseline for our power analysis
- LLM-Safety Evaluations Lack Robustness (arXiv:2503.02574, March 2025) — evaluation pipeline variance up to 28%, motivates our fixed-pipeline design
- PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference (arXiv:2406.15513, ACL 2025) — 30K+ expert comparisons with decoupled safety/helpfulness annotations across 19 harm categories; our primary training dataset
- SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety (arXiv:2505.20065, ICLR 2026 Oral) — achieves ~97% harmless ratio via DPO on PKU-SafeRLHF-30K; establishes dataset+method maturity but reports no cross-seed variance
- SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization (arXiv:2511.12982, Nov 2025) — validates classifier-as-reward paradigm for GRPO safety alignment; motivates our WildGuard-as-reward design
- TRL v1.0: Post-Training Library Built to Move with the Field (Hugging Face, March 2026) — unified training stack for DPO, PPO, GRPO eliminating infrastructure confounds across algorithms
- How Many Random Seeds? Statistical Power Analysis in Deep RL Experiments (arXiv:1806.08295, 2018) — methodology for minimum-seed derivation via power analysis; we extend to safety alignment and apply a priori to justify our 20-seed design
- What Matters For Safety Alignment? (arXiv:2601.03868, Jan 2026) — cross-model safety comparison across 32 models and 13 families
- WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs (arXiv:2406.18495, 2024) — 7B safety classifier achieving 94.7% F1 on response harmfulness; our primary safety judge and GRPO reward signal
- Skywork-Reward: Bag of Tricks for Reward Modeling in LLMs (arXiv:2410.18451, 2024) — Skywork-Reward-Llama-3.1-8B-v0.2, #1 8B model on RewardBench; one of three PPO reward models in our ablation
- Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts (arXiv:2406.12845, 2024) — ArmoRM-Llama3-8B-v0.1, 89.0 RewardBench with explicit safety dimension; default PPO reward model
- Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping (arXiv 2020) — seed variance methodology for NLP
- Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs (IJCNLP-AACL 2025) — macro/micro consistency metrics for LLM fine-tuning
- RVPO: Risk-Sensitive Alignment via Variance Regularization (arXiv:2605.05750, May 2026) — inter-reward variance penalization in single runs; motivates reward model ablation
- Improving Safety Alignment via Balanced Direct Preference Optimization (arXiv:2603.22829, March 2026) — safety alignment overfitting in DPO
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv:2603.02229, March 2026) — safety-helpfulness Pareto frontier under DPO
- Reproducibility in Machine-Learning-Based Research: Overview, Barriers, and Drivers (AI Magazine 2025)

## Resource Estimate
- **manual**: {'gpu_hours': '~2,800 H100-hours total: ~1,600 training (260 runs across 3 algorithms × 3 scales × 20+ seeds, all full fine-tuning with DeepSpeed ZeRO-2; PPO runs require 2 H100s for policy+reference+RM) + ~1,200 evaluation (260 checkpoints × 8 benchmarks including WildGuard 7B and HarmBench 7B classifier inference, each checkpoint requiring ~3-4 GPU-hours for generation + classification across all benchmarks)', 'timeline': '17–19 weeks (infrastructure + TRL v1.0 pipeline setup 3w, training runs 6–7w on 8×H100 cluster, evaluation 3–4w, statistical analysis + minimum-seed derivation + paper writing 5–6w)', 'estimated_gpu_cost': '$7,000 at ~$2.50/H100-hr on mid-tier providers'}
- **human_in_loop**: {'gpu_hours': '~2,800 H100-hours (identical core compute; full FT precludes further memory optimization)', 'timeline': '14–16 weeks (Claude accelerates TRL v1.0 pipeline integration, ANOVA analysis scripts, power analysis code, per-category fragility analysis, and paper drafting)', 'claude_api_cost': '$500–700 (Sonnet 4.6 for code generation, statistical analysis automation, and drafting; ~150M tokens)', 'estimated_gpu_cost': '$7,000'}
- **auto_research**: {'gpu_hours': '~2,800 H100-hours', 'timeline': '11–14 weeks (parallelized experiment orchestration with automated sweep management, evaluation pipelines, and ANOVA analysis)', 'claude_api_cost': '$1,500–2,200 (experiment orchestration, automated analysis, full paper draft generation; ~600M tokens)', 'estimated_gpu_cost': '$7,000', 'speed_bottleneck': 'GPU cluster queue time for 260 training jobs (PPO runs ~2× longer than DPO/GRPO due to multi-model training); sequential dependency between training completion and safety evaluation; WildGuard 7B + HarmBench 7B classifier inference throughput across 260 checkpoints × ~6K safety evaluation prompts each'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fe0ff742-1c6f-469d-b921-9c60e7970b5b",
  "type": "user",
  "uuid": "9e84d69a-7e29-4a5e-9b7b-b905f23b02de",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:11:11.509Z_

```json
{
  "parentUuid": "9e84d69a-7e29-4a5e-9b7b-b905f23b02de",
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
  "uuid": "e5b3ec9a-016b-487d-a92b-fc77224ef0d1",
  "timestamp": "2026-05-19T21:11:11.509Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:11:11.509Z_

```json
{
  "parentUuid": "e5b3ec9a-016b-487d-a92b-fc77224ef0d1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "98ba08f9-9c7a-4c37-a2e1-335ccaaa6816",
  "timestamp": "2026-05-19T21:11:11.509Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make my assessment. Let m…",
  "leafUuid": "98ba08f9-9c7a-4c37-a2e1-335ccaaa6816",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit safety alignment reproducibility across training seeds",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:11:39.844Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as the Meta Judge.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability (appropriate venue): [18% - 28%] 中位 22%
- CoRL: 0%
- Key concerns: venue mismatch, confirmatory study, trivial alternative, SCI-T trivial, expected findings


**Reviewer 2:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability (appropriate venue): [20% - 32%] 中位 25%
- CoRL: [0% - 3%] 中位 1%
- Key concerns: venue mismatch, confirmatory study, trivial alternative, WildGuard evaluation circularity

**Reviewer 3:**
- Novelty: 弱
- Significance: 中
- Related Work: 强
- Probability (appropriate venue): [15% - 28%] 中位 20%
- CoRL: (no estimate provided)

All three reviewers converge on weak-to-medium novelty and medium significance with strong related work coverage, with venue appropriateness estimates clustering around 20-25%. The main criticisms center on confirmatory findings and evaluation concerns. Looking at the consensus criticisms across all three reviewers, the paper faces fundamental issues: weak to moderate novelty, narrow significance despite being real, strong related work coverage, and the core finding reads as confirmatory rather than surprising. Multiple reviewers flag that trivial alternatives exist and the SCI-T metric itself is trivial, while two reviewers raise concerns about confounding variables introduced by full fine-tuning and the reliability of borrowed variance estimates for power analysis. There's also a circularity issue with WildGuard evaluation and a risk that the work is purely measurement-focused without offering solutions.

On implementation, all three reviewers align on the resource requirements from the proposal itself—roughly 2,800 H100-hours across 260 runs over 17-19 weeks. Now I'm calculating the final probability assessment based on this high consistency in both technical concerns and feasibility estimates.

Looking at the three probability ranges, they cluster tightly around a median of 22% with standard deviation under 2.1%, which suggests strong convergence. The individual ranges are R1 at 18-28%, R2 at 20-32%, and R3 at 15-28%, giving an intersection of 20-28%. Given this consistency, I'd narrow to around 18-27% with the median at 22%.

But the most critical finding cuts across all three reviewers: they unanimously flagged CoRL as a fundamental venue mismatch, which frames all these assessments as conditional on that core issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ba08f9-9c7a-4c37-a2e1-335ccaaa6816",
  "isSidechain": false,
  "requestId": "req_011CbCccpZYzNRZSYmxExTyA",
  "type": "assistant",
  "uuid": "7c414506-fa1a-4632-9dee-10b121c47bda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1TMu6fsj1b5WgFczHnVFc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20761,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3512,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 20761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20761
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

_source line 9 · 2026-05-19T21:12:33.716Z_

【阶段】: Meta Judge
【三次中位】: [22%, 25%, 20%]  std=2.1%
【共识维度】:
- **Venue Mismatch（致命）**: 3/3 审稿人一致判定——proposal 与 CoRL 2026 完全不匹配，0% 中稿概率，必然 desk reject。以下所有评估均基于投稿至适配 venue（NeurIPS/ICML/ICLR 主会）的假设。
- **Novelty（弱-中）**: 3/3 一致——核心贡献是 "scale-up + apply standard tools to new domain"（Fraser SFT→preference optimization, OXRL capability→safety），非概念性突破。SCI-T 是 SSI 的 trivial 平移，ANOVA/power analysis 是标准统计方法。Fraser et al. 自己在 future work 中已 call out 了本 proposal 的方向。
- **Significance（中）**: 3/3 一致——研究问题对 AI governance 确实重要，minimum-seed tables 有实用价值；但核心预期发现（"safety 比 capability 更 fragile"）缺乏 surprise value，大多数审稿人反应为 "I would have guessed this"。
- **Related Work（强）**: 3/3 一致——覆盖全面，引用真实准确，gap 定位清晰。但 related work 的完善度同时暴露 gap 的狭窄。
- **Trivial Alternative 威胁（中等-明显）**: 3/3 一致——小规模实验（5-10 seeds, 1-2 算法）即可获得定性相同的核心发现，260 runs 的增量在 rigor 而非 insight。
- **"Confirmatory study" 风险**: 3/3 一致——positive result（safety 更 fragile）是高度可预期的，论文价值依赖于二阶发现是否 surprising。
- **Full FT confound**: 2/3（R2、R3）——消除 LoRA confound 的同时引入新 confound（更大参数空间的 chaotic divergence），缺乏 LoRA vs full FT 对照。
- **Power analysis 借用方差**: 2/3（R2、R3）——从 Fraser(SFT/LoRA) 外推 σ̂_safety ≈ 3.9pp 到 preference optimization/full FT 场景，前提假设有风险。

【异常维度】:
- **WildGuard 评估循环**（仅 R2）: GRPO 用 WildGuard 作 reward signal 同时用 WildGuard 作 evaluation judge，存在 overfit-to-judge 风险。此为有效技术关切但非致命——安全对齐研究中常见做法，且 proposal 有 HarmBench/SORRY-Bench 作独立交叉验证。降权但保留为次要风险。
- **"纯 measurement 无 solution" 风险**（R3 显式标注，R2 隐含提及）: 实际上接近 2/3 共识——proposal 识别 fragility 但不提出 mitigation。对 NeurIPS main 来说这是一个弱点，对 D&B track 则不是。
- **R3 给 Novelty 评"弱"**（其余两位给"弱-中"）: R3 稍严于 R1/R2，但差异不大，结论方向一致。

【最终概率】: [18% - 27%] 中位 22%
【一致性】: 高（std=2.1% < 3%，三位审稿人在所有核心维度判决方向完全一致）
【综合理由】:
三份评审呈现罕见的高度一致性——Novelty/Significance/Related Work 三个维度的判决完全收敛，概率估计 std 仅 2.1%。处理逻辑：

1. **共识驱动定价**：三位审稿人对 Novelty（弱-中）的判决完全一致，这是限制概率上界的核心维度。"Scale-up + standard methodology applied to adjacent domain" 在 top venue 的 novelty bar 下天花板约 30%。Significance（中）进一步将实际上界压至 ~27%。

2. **异常维度处理**：R2 提出的 WildGuard 评估循环是有效关切，但 proposal 有多 benchmark 交叉验证（HarmBench、SORRY-Bench），不构成致命威胁。降权处理，不影响中位估计。R3 偏严（Novelty 评"弱"而非"弱-中"），但考虑到三位均在同一方向（弱端），不需额外调整。

3. **高一致性处理规则**：按规则取中位附近、缩窄区间。三份评审的交集区间为 [20%-28%]，考虑到 R3 的下界 15% 是最严格的声音，在高一致性场景下取中位 22%，略向严格方向收窄区间至 [18%-27%]。

4. **CoRL 特殊说明**：若坚持投 CoRL 2026，概率为 0-1%（desk reject 确定性极高）。以上估计严格基于适配 venue 假设。

5. **Venue 建议**：三位审稿人均建议转投 NeurIPS/ICML/ICLR。考虑到 proposal 的 "measurement/audit" 特质，**NeurIPS 2026 Datasets & Benchmarks track** 可能是最优选择（R3 估计该 track 概率可升至 25-35%），其评审标准更看重 rigor 和 utility 而非 conceptual novelty。

【建议】: 边缘（适配 venue 下） / KILL（CoRL 2026 下）。若用户确认目标为 CoRL，立即止损；若可更换 venue，进入迭代优化有意义但上限有限。

【实施评估】:
  - 计算资源: ~2,800 H100-hours（~1,600 训练 + ~1,200 评估），260 runs 全部使用 full fine-tuning + DeepSpeed ZeRO-2。需 8×H100 集群，PPO 需 2×H100/run（policy+reference+RM）。GPU 成本约 $7,000（中端云平台 ~$2.50/H100-hr）。
  - 数据需求: PKU-SafeRLHF-30K（公开可得，ACL 2025）作为训练数据；WildGuardTest 5K + HarmBench 400 + SORRY-Bench 440 + GSM8K/MATH/AlpacaEval/MT-Bench 作为评估数据（均公开可得）。无数据获取瓶颈。
  - 人工介入: 低。主要为实验管理、结果分析和论文撰写。无人工标注需求（所有评估使用自动化 classifier judge）。Claude API 辅助下可加速 pipeline 搭建和统计分析脚本编写。
  - 训练需求: 需要训练 260 个 alignment 模型（非从头预训练，均为 post-training fine-tuning）。单次 DPO/GRPO 训练 1.7B/4B 约 2-4 H100-hours，8B 约 6-10 H100-hours；PPO 训练时间约 2× DPO。不需要训练新的 reward model 或 safety classifier（均使用现有开源模型）。
  - 新 Benchmark: 不需要构建全新 benchmark。SCI-T 是一个轻量级指标定义（非 benchmark），minimum-seed lookup tables 是统计分析产出物。
  - 预估周期: 14-19 周（取决于自动化程度）。关键瓶颈为 260 训练 job 的 GPU 队列时间和 PPO 的较长训练周期。若 8×H100 集群可持续使用，训练阶段 6-7 周可并行化完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c414506-fa1a-4632-9dee-10b121c47bda",
  "isSidechain": false,
  "requestId": "req_011CbCccpZYzNRZSYmxExTyA",
  "type": "assistant",
  "uuid": "cef94b51-4ce6-487f-a764-19726d2b7481",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1TMu6fsj1b5WgFczHnVFc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20761,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3512,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 20761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20761
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make my assessment. Let m…",
  "leafUuid": "cef94b51-4ce6-487f-a764-19726d2b7481",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit safety alignment reproducibility across training seeds",
  "sessionId": "7f153888-4058-4d8a-8bf7-14562511eba6"
}
```

---
