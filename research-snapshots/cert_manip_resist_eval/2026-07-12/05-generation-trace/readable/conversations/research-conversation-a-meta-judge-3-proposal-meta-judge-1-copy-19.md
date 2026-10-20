# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/c5fd9e1e-23b4-4571-bc6d-e02837953690.jsonl`
- **Structured JSON:** [`bdfb14261b88910ed59e.json`](../../sessions/bd/bdfb14261b88910ed59e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:27:19.226Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:27:19.226Z",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research data. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Audinet de Pieuchon et al., \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\"](https://aclanthology.org/2025.emnlp-main.1000/) (EMNLP 2025): 最直接的同领域工作，对比 DSL/PPI 在 LLM 标注去偏中的效果。证明 EMNLP 接收此类方法论论文。但该工作聚焦 ATE 级别去偏，未涉及 CATE。\n- [Mozer, \"PPI is the Difference Estimator\"](https://arxiv.org/abs/2603.19160) (arXiv 2026): 揭示 PPI 与调查抽样差异估计量的代数等价性，含 arm-specific rectifier。仍限于总体水平估计量，无法处理子群级 CATE 偏差。\n- [Fisch et al., StratPPI](https://arxiv.org/abs/2406.04291) (NeurIPS 2024): 通过分层改进 PPI 的置信区间宽度。方向相关但估计目标仍为总体参数的分层改进，非 CATE 估计。\n- [Sui et al., PPCI](https://arxiv.org/abs/2603.05575) (arXiv 2026): 将 PPI 扩展至条件推断，使用核局部化。关键区分：PPCI 处理的是结果预测噪声，假设条件变量正确；EC-HTE 处理的是条件变量（效应修饰符）本身的误分类。互补而非竞争。\n- [Persson et al., \"Detecting and Mitigating Group Bias in HTE\"](https://arxiv.org/abs/2602.20383) (arXiv 2026): 处理 CATE→GATE 聚合偏差，通过 shrinkage 校正。偏差来源不同（聚合 vs. 测量误差），假设协变量无噪声。互补关系。\n- [Boileau et al., \"Assumption-Lean Differential Variance Inference\"](https://arxiv.org/abs/2512.03254) (arXiv 2025): 在效应修饰符缺失或测量有误时进行异质性假设检验。但只做假设检验（是否存在异质性），不做 CATE 估计。互补关系。\n- [Ashwin et al., \"Using LLMs for Qualitative Analysis can Introduce Serious Bias\"](https://journals.sagepub.com/doi/10.1177/00491241251338246) (Sociological Methods & Research 2025): 直接实证支撑——LLM 在难民访谈编码中的误差与受访者特征（难民身份、性别、教育水平）系统性相关。证实差异性误分类是常态。\n- [Messing, \"Hidden Measurement Error in LLM Pipelines\"](https://arxiv.org/abs/2604.11581) (arXiv 2026): 文档化 LLM 管线中隐藏测量误差导致置信区间 40-60% 欠覆盖。但分析停留在聚合层面。\n- [Jerzak et al., SRI Framework](https://arxiv.org/abs/2509.12416) (arXiv 2025): 在带噪标注下提供有效推断，但未涉及效应修饰符误分类对 HTE 的影响。\n- 调研总结: 该领域存在一个清晰且已被验证的空白——所有现有去偏方法（DSL/PPI/StratPPI/arm-specific rectifier）均锁定于总体级别估计量；所有现有 CATE 方法均假设协变量正确。EC-HTE 恰好填补了\"LLM 标注误分类 × CATE 估计\"的交叉空白，且 Ashwin et al. 的实证数据证实了差异性误分类在实践中普遍存在。\n\n【整体印象】:\n如果我是审稿人，第一反应是：这是一篇问题识别精准、方法设计合理、实验方案异常完备的方法论投稿。问题的动机令人信服——差异性误分类与 CATE 异质性正相关时全局校正反而恶化估计这一反直觉发现，是整篇论文的核心 hook，具有很强的说服力。总体倾向 weak accept。但我会关注技术新颖性是否足够——方法本身是已有技术（层次贝叶斯 + 因果森林 + 自适应分配）的组合式应用，核心贡献更多在问题识别和形式化上。\n\n【核心贡献】:\n1. 首次识别并形式化了 LLM 标注误分类在效应修饰符上对 CATE 估计的结构性偏差，并证明全局校正可能恶化估计（当误分类异质性与 CATE 异质性正相关时）。\n2. 提出可操作的诊断准则（误分类异质性 × CATE 异质性乘积），具有独立的方法论价值。\n3. 三阶段校正框架（层次贝叶斯部分池化 → 三明治方差调整 → 自适应标注分配）。\n这些贡献对计算社会科学和 NLP-for-social-science 领域有显著价值。随着 LLM-as-annotator 成为默认管线，子群分析的可靠性问题日益突出，本工作的实际影响力较大。\n\n【方法合理性】:\n方法整体合理，三阶段设计逻辑自洽。层次贝叶斯部分池化解决了\"独立估计（高方差）vs. 全局估计（有偏）\"的核心张力，是处理子群混淆矩阵的合适选择。三明治方差调整传播第一阶段的 nuisance parameter 不确定性，是标准且正确的做法。自适应分配的准则（误分类不确定性 × CATE 量级）与理论 bias bound 一致。\n\n关于更简单替代方案的考量：\n- 直接用 StratPPI 进行子群级估计？不行——StratPPI 改进的是 CI 宽度，仍是同一估计量的分层，不处理效应修饰符误分类。\n- 直接用子群独立混淆矩阵（无层次结构）？这正是 ablation 中的对照之一，在小样本子群中会高方差。\n- 不做自适应分配？均匀分配会浪费预算在低影响子群上。\n因此，方法的复杂度与问题复杂度匹配，没有明显的过度工程。\n\n【5 维度打分】:\n\n  1. 研究问题: 【强】 — 问题真实、重要、有实证支撑（Ashwin et al. 2025 直接证明差异性误分类是常态），且具有明确的时效性（LLM-as-annotator 管线在 CSS 中爆炸式增长）。反直觉发现（全局校正可恶化估计）提供了强有力的叙事 hook。问题定义清晰，与已有工作的区分（vs. ATE 去偏、vs. CATE-GATE 聚合偏差、vs. PPCI 的条件推断）均有理有据。\n\n  2. 方法与创新: 【中偏强】 — 核心新颖性在于问题识别与形式化（包括 bias bound 推导），而非技术组件本身。层次贝叶斯部分池化、因果森林、自适应采样均为成熟技术。EC-HTE 的贡献是将这些技术以正确的方式组合来解决一个新问题。这在方法论论文中是可接受的，但可能被部分审稿人视为\"组合式创新\"（compositional innovation）。与 Persson et al. (2026) 和 Boileau et al. (2025) 的区分是清晰的。bias bound（误分类异质性 × CATE 异质性乘积）作为独立诊断工具有附加价值。\n\n  3. 实验设计: 【强】 — 这是该 proposal 最突出的亮点之一。DGP 矩阵设计全面，系统性变化误分类-CATE 相关方向（正/负）是关键实验设计决策。6 种对比方法覆盖了所有合理 baseline（uncorrected, global, arm-specific, SIMEX, calibration-only, EC-HTE full）。评估指标全面（PEHE, subgroup CATE bias, CI coverage, CI width, GATE RMSE, bound tightness）。消融研究按阶段分层，覆盖每个设计选择。多 LLM 验证（GPT-4.1, Qwen 3.5, Llama 3.3）增强了泛化性。200+ 次重复保证统计显著性。预算曲线和先验敏感性分析是良好的实验实践。唯一不足：真实数据验证（Ashwin et al.）由于缺乏自然因果结构，只能验证前提（差异性误分类存在）而非完整评估 CATE 校正效果。\n\n  4. 可行性: 【强】 — 不需要训练大模型，仅需 LLM API 调用（标注）和标准统计计算。层次贝叶斯用 VI 拟合，计算成本低。因果森林有成熟实现（R `grf` 包）。Ashwin et al. 数据集公开可用。主要计算瓶颈是仿真规模（~14 配置 × 200 重复 × 多样本量/预算/方法/LLM），但这是可并行化的标准仿真工作，单 GPU 集群数天可完成。无需构建新 benchmark。人工标注方面，使用已有专家标签数据集，无需新增标注。预估总周期 3-5 个月。\n\n  5. 写作与呈现: 【强】 — 结构清晰，问题-动机-方法-实验逻辑连贯。反直觉发现作为 hook 的叙事策略有效。与相关工作的差异化讨论非常详尽（5 条线索），每条区分均有具体论据。限制声明诚实（仅限分类效应修饰符）。\"为什么不直接用专家标签\"这一自然反对意见的预先回应很好。唯一建议：方法描述可能对纯 NLP 审稿人偏技术，需要更多直觉解释。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n该 proposal 在问题识别、实验设计、可行性和写作上均为\"强\"级别，在方法创新上为\"中偏强\"。它填补了一个真实且有实证支撑的研究空白，实验设计异常完备。主要不确定性来自两点：(1) EMNLP 审稿人对纯方法论/因果推断论文的接受度——虽然 Audinet de Pieuchon et al. (EMNLP 2025) 证明此类论文可被接受，但该 proposal 的因果推断成分更重，可能被部分审稿人认为更适合统计学期刊；(2) 技术新颖性是组合式的，核心贡献在问题识别而非算法创新，这在方法论论文中是可接受的，但审稿人对此的容忍度因人而异。综合来看，这是一篇扎实的投稿，在适配的审稿人组合下有较好的接受概率，但也可能因\"NLP 新颖性不足\"或\"更适合 causal inference venue\"被拒。中位估计 35% 反映了\"solid but not guaranteed\"的整体判断。\n\n【主要风险】:\n1. **技术新颖性被质疑为\"组合式\"（compositional）**：审稿人可能认为层次贝叶斯 + 因果森林 + 自适应分配的组合虽然正确但缺乏技术深度，核心贡献更像是一个\"observation paper\"而非\"method paper\"。缓解策略：强调 bias bound 的理论贡献和诊断准则的独立价值。\n2. **真实数据验证有限**：Ashwin et al. 数据集只能验证差异性误分类的存在，无法评估 CATE 校正效果。CATE 评估完全依赖半合成实验。审稿人可能要求至少一个有自然因果结构的真实数据应用。缓解策略：寻找有自然实验结构的 CSS 数据集（如政策干预 + LLM 标注的文本变量），或更明确地论证为什么半合成评估在此场景下是充分的（ground-truth CATE 只有在合成设置中才可知）。\n\n【实施评估】:\n  - 计算资源: 中等。主要是 LLM API 调用费用（3 个 LLM × 多配置 × 多样本量，估计 $500-2000 API 费用）和标准 CPU/GPU 仿真计算。无需大规模 GPU 训练。\n  - 数据需求: 低。使用公开政治科学文本语料（如 immigration framing 数据集）作为半合成基础，Ashwin et al. (2025) Rohingya 数据集公开可用。\n  - 人工介入: 低。不需要新的人工标注——使用已有专家标签数据集，仿真中的\"专家标签\"由 DGP 生成。\n  - 训练需求: 无大模型训练。仅需层次贝叶斯 VI 拟合（秒级）和因果森林训练（分钟级）。\n  - 新 Benchmark: 否。使用已有数据集 + 半合成 DGP。\n  - 预估周期: 3-5 个月（理论推导 1 月 + 代码实现 1 月 + 实验运行 1-2 月 + 写作 1 月）。\n```\n\nSources:\n- [Audinet de Pieuchon et al., \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\" (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)\n- [Mozer, \"PPI is the Difference Estimator\" (arXiv 2026)](https://arxiv.org/abs/2603.19160)\n- [Fisch et al., StratPPI (NeurIPS 2024)](https://arxiv.org/abs/2406.04291)\n- [Sui et al., PPCI (arXiv 2026)](https://arxiv.org/abs/2603.05575)\n- [Persson et al., \"Detecting and Mitigating Group Bias in HTE\" (arXiv 2026)](https://arxiv.org/abs/2602.20383)\n- [Boileau et al., \"Assumption-Lean Differential Variance Inference\" (arXiv 2025)](https://arxiv.org/abs/2512.03254)\n- [Ashwin et al., \"Using LLMs for Qualitative Analysis can Introduce Serious Bias\" (Sociological Methods & Research 2025)](https://journals.sagepub.com/doi/10.1177/00491241251338246)\n- [Messing, \"Hidden Measurement Error in LLM Pipelines\" (arXiv 2026)](https://arxiv.org/abs/2604.11581)\n- [Jerzak et al., SRI Framework (arXiv 2025)](https://arxiv.org/abs/2509.12416)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a comprehensive evaluation. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- Audinet de Pieuchon et al. (EMNLP 2025): \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\" — 直接对比 DSL 和 PPI 在 LLM 标注去偏上的表现，发现 DSL 在中等专家标注量下通常误差最低。该工作锁定在 ATE 级别的总体参数估计，未涉及 CATE/HTE。EC-HTE 的核心主张——这些方法无法处理子群级别的 CATE 纠偏——与本文互补且不冲突。\n\n- Fisch et al. (NeurIPS 2024): \"Stratified Prediction-Powered Inference (StratPPI)\" — 通过数据分层改进 PPI，在自动评分器表现因条件分布不同而异质时显著收紧置信区间。但仍以总体参数为目标估计量，不处理 effect modifier 被误分类导致的 CATE 扭曲。EC-HTE 的分层思想与 StratPPI 有相似之处（都利用子群结构），但估计目标完全不同。\n\n- Mozer (arXiv:2603.19160): \"PPI is the Difference Estimator\" — 揭示 PPI 核心估计量等价于经典调查抽样的差异估计量。该论文的 arm-specific rectifier 处理 ATE 偏差，EC-HTE proposal 正确指出其代数上无法纠正子群级别的 CATE 扭曲。\n\n- Messing (arXiv:2604.11581): \"Hidden Measurement Error in LLM Pipelines\" — 文档记录 LLM pipeline 中隐藏测量误差导致 naive CI 覆盖不足 40-60%。仅限于汇总层面分析，未延伸到因果 HTE 纠偏。EC-HTE 引用此文作为问题紧迫性的证据，引用恰当。\n\n- Ashwin, Chhabra & Rao (Sociological Methods & Research, 2025): \"Using LLMs for Qualitative Analysis can Introduce Serious Bias\" — 在罗兴亚难民访谈转录上提供直接实证，LLM 编码错误与受访者难民身份、性别、教育水平系统性相关。这是 EC-HTE 问题动机的核心实证基础。\n\n- Sui et al. (arXiv:2603.05575): \"Prediction-Powered Conditional Inference (PPCI)\" — 将 PPI 扩展到固定测试点的条件函数推断。关键区别：PPCI 处理结果预测噪声，但假定条件变量（即 effect modifier）是正确的。EC-HTE proposal 准确指出当条件变量本身被误分类时，PPCI 的 kernel localization 无法帮助。\n\n- Persson et al. (arXiv:2602.20383): \"Detecting and Mitigating Group Bias in HTE\" — 发现即使 CATE 模型正确指定，CATE→GATE 的聚合也不能恢复真正的 GATE，提出收缩纠偏。但偏差来源是聚合过程而非测量误差，且假定协变量干净。EC-HTE 处理不同来源的偏差（effect modifier 误分类），二者互补。\n\n- Boileau et al. (arXiv:2512.03254): \"Assumption-Lean Differential Variance Inference for HTE Detection\" — 当 effect modifier 被遗漏或严重测量误差时，通过潜在结果方差对比检测异质性是否存在。关键区别：这是假设检验（异质性是否存在），不是 CATE 估计。EC-HTE 做的是 CATE 纠偏估计，二者互补。\n\n- Jerzak et al. (arXiv:2509.12416): \"Surrogate Representation Inference (SRI)\" — 在噪声标注下提供有效推断，但不处理 effect modifier 误分类对 HTE 的影响。\n\n- AM-PPI (arXiv:2605.08429): \"Active Multiple-Prediction-Powered Inference\" — 多预测器自适应路由 + 预算优化，CI 收窄 10-40%。仍锁定在总体参数估计。\n\n- 调研总结: LLM 标注去偏领域极度活跃（2024-2026 年涌现大量工作），但现有方法几乎全部锁定在 ATE/总体参数级别。CATE 估计中 effect modifier 被 LLM 误分类的问题确实是一个未被占据的交叉空白。EC-HTE 的 novelty claim——no existing method corrects for subgroup-specific misclassification in effect modifiers for CATE——经调研验证成立。\n\n【整体印象】:\n如果我是审稿人，第一反应是：这是一篇 well-motivated、well-scoped 的方法论工作，识别了一个真实且被忽视的技术空白。问题界定清晰，相关工作梳理异常全面（7 篇 2025-2026 新工作的精确定位和差异化分析），实验设计非常完备。我的倾向是 weak accept / borderline accept。\n\n主要犹豫点：(1) 方法论层面的创新深度——三阶段框架本质上是已有工具的组合（hierarchical Bayesian confusion matrix + honest causal forest + sandwich variance + adaptive allocation），每一步都不是新方法，新颖性主要在于问题识别和组合；(2) \"global correction can worsen CATE\" 的 anti-intuitive claim 对测量误差/流行病学专家而言可能不够 surprising（differential misclassification 是经典概念）；(3) 验证主要是 semi-synthetic，real-data 部分只能验证前提假设而非完整框架。\n\n【核心贡献】:\n1. **问题识别与形式化**: 首次明确界定 LLM 标注 effect modifier 误分类导致的 CATE 扭曲问题，并证明全局纠偏在正相关情况下可能恶化估计。这是最有价值的贡献。\n2. **可操作的诊断标准**: misclassification heterogeneity × CATE heterogeneity 的乘积作为事前诊断，独立于 EC-HTE 框架有单独价值。\n3. **三阶段纠偏框架**: 实用但方法论新颖性有限。\n4. **全面的实证验证设计**: 实验方案本身的完备性是一个显著优点。\n\n这些贡献对领域有中等偏上价值。问题识别和诊断标准对日益增长的 \"LLM-as-annotator for causal inference\" 社区有实际指导意义。但核心方法论（hierarchical Bayesian + causal forest + sandwich）都是成熟工具的组合，不是方法论突破。\n\n【方法合理性】:\n方法整体合理。具体评价：\n- **Stage 1 (Hierarchical Bayesian confusion matrix)**: 合理选择，partial pooling 在小样本子群和全局估计之间取得平衡。VI 作为主要拟合方法、MCMC 作为验证是实际的决定。\n- **Stage 2 (Sandwich variance)**: 将 Stage 1 的 nuisance parameter 不确定性传播到 CATE CI 中是正确做法。Bootstrap 作为稳健性检查也合理。\n- **Stage 3 (Adaptive allocation)**: 联合最小化 misclassification 不确定性和 CATE 方差的分配标准是自然的设计。Cold-start protocol 务实。\n\n**替代方案考量**: 一个更简单的替代是直接用 StratPPI 类方法在子群级别独立做 PPI 纠偏（即每个子群独立估计一个 PPI rectifier 然后独立做 CATE）——proposal 应该讨论为什么这不够（可能因为子群样本量太小导致方差爆炸，partial pooling 是关键优势）。另一个替代是 SIMEX（已被列为 baseline，这是好的）。总体来说没有更简单的替代方案能完整覆盖所有三个阶段的功能。\n\n【5 维度打分】:\n\n  1. 研究问题: 【强】— LLM-as-annotator pipeline 已成为 CSS 的默认做法（Audinet de Pieuchon et al., EMNLP 2025 确认），但现有去偏方法全部锁定在 ATE 级别。随着研究者越来越多地将 LLM 标注用于子群分析和效应修饰（heterogeneity analysis），效应修饰变量本身被误分类的问题具有真实且不断增长的实际影响。Ashwin et al. (2025) 提供了直接实证。问题的时效性和实用价值都很高。\n\n  2. 方法与创新: 【中】— Novelty 主要在问题识别层面而非方法论层面。三阶段框架的每一步（hierarchical Bayesian estimation: 经典方法; honest causal forest: Wager & Athey 2018; sandwich variance: 标准技术; adaptive allocation: 常见优化策略）都是成熟工具。创新在于将它们组合起来解决一个新问题，并推导出诊断标准（bias bound）。与 PPCI (Sui et al., 2026) 的区分清晰且有说服力——PPCI 假定条件变量正确，EC-HTE 处理条件变量本身错误的情况。与 Persson et al. (2026) 的区分也清晰——偏差来源不同。但\"global correction worsens estimates\"在测量误差文献中并不 novel（differential misclassification 是 epidemiology 的基础概念，Rothman, Greenland & Lash 的教科书已有详细讨论）。\n\n  3. 实验设计: 【强】— 实验方案非常全面且设计严谨：(a) DGP matrix 覆盖关键因素的 worst/best case 组合，特别包含 misclassification-CATE correlation direction 这一关键变量；(b) 6 种对比方法（uncorrected, global, arm-specific, SIMEX, calibration-only, EC-HTE full）覆盖了所有合理 baseline；(c) 4 层 ablation（partial pooling, variance adjustment, allocation strategy, pilot ratio）各有明确假设验证目标；(d) 评估指标全面（PEHE, subgroup bias, CI coverage, CI width, GATE RMSE, bound tightness）；(e) 200+ replications per configuration 保证统计功效；(f) 3 个 LLM annotator 覆盖不同家族。与 \"Really Doing Great at Estimating CATE?\" (NeurIPS D&B 2021) 建立的 CATE 评估标准基本一致。Real-data validation 的局限性（只能验证前提，不能验证完整框架）被诚实声明，semi-synthetic 实验承担主要验证责任——这是合理的设计。唯一遗憾：没有真正有自然因果结构的 real-world end-to-end validation。\n\n  4. 可行性: 【强】— (a) 计算需求适中：hierarchical Bayesian VI 在小规模数据上很快，honest causal forest 有成熟实现（grf R package），semi-synthetic 实验可在单 GPU/CPU 集群上完成；(b) 数据需求合理：semi-synthetic 用公开政治文本语料，real-data 用 Ashwin et al. 的 Rohingya 语料（已发表）；(c) 无需训练新模型（用现成 LLM API 做标注）；(d) 专家标注预算 B ∈ {100-2000} 是现实范围；(e) 方法实现不涉及复杂的新架构。唯一风险点：12-14 个 DGP 配置 × 200 replications × 多种 N × 多种 B × 3 个 LLM = 实验量较大，但通过 VI（而非 MCMC）和并行化可管理。预估 2-3 个月完成所有实验。\n\n  5. 写作与呈现: 【强】— Proposal 的写作质量很高：(a) 问题动机层层递进——从一般性观察到反直觉发现到数学界定；(b) 相关工作梳理按 5 个 thread 组织，每个 thread 都精确定位差异，特别是对 PPCI vs. EC-HTE 的区分（conditioning variable noise vs. conditioning variable misclassification）非常清晰；(c) 方法描述条理分明，三阶段各有清晰的技术内容；(d) 实验设计的 DGP matrix 和 ablation 结构一目了然；(e) 限制和范围声明诚实（categorical effect modifiers only, semi-synthetic validation）。一个小改进建议：可以在引言中更早地给出一个具体的量化例子（如 proposal 中的 two-subgroup example）来 hook 读者。\n\n【概率估计】: [30% - 42%] 中位 36%\n\n【估计理由】:\n上行因素：(1) 研究问题真实且时效性强，LLM-as-annotator for causal inference 是 2024-2026 最活跃的交叉方向之一；(2) Novelty claim 经调研验证成立——ATE→CATE 的去偏空白确实存在；(3) 实验设计异常完备，如果实验结果如预期，论文的实证部分将非常扎实；(4) 相关工作梳理全面，positioning 精确；(5) 诊断标准有独立实用价值。\n\n下行因素：(1) 方法论新颖性有限——本质是 well-known 工具的组合（hierarchical Bayes + causal forest + sandwich variance），缺乏深层方法论创新，审稿人可能认为 \"incremental\"；(2) \"differential misclassification biases subgroup estimates\" 的核心洞察在测量误差/epidemiology 文献中是经典知识，在 NLP 社区可能 novel 但在统计社区可能被视为 straightforward application；(3) 无 end-to-end real-world CATE validation——real data 只能验证前提（misclassification is differential），不能验证核心主张（EC-HTE improves CATE estimation in practice）；(4) EMNLP reviewer pool 的方法论背景差异较大——如果遇到 causal inference 背景强的审稿人，可能认为 novelty 不足；如果遇到 NLP 背景为主的审稿人，可能觉得 causal inference 技术细节难以评判；(5) 论文的核心受众（做 causal HTE 的 CSS 研究者）在 EMNLP 审稿人中占比可能不高。\n\n综合判断：这是一篇扎实的 borderline paper。问题真实、方法合理、实验设计出色，但方法论创新深度不足以进入 \"clearly above threshold\"。如果实验结果清晰地展示 EC-HTE 的优势（特别是 global correction worsens 的 demonstration），且写作保持 proposal 的高质量，有合理的中稿机会。中位估计 36% 反映了一篇 \"solid but not exciting\" 的 borderline submission 在 EMNLP 的典型命运。\n\n【主要风险】:\n1. **方法论创新深度不足**: 审稿人可能认为三阶段框架只是已有工具的 straightforward 组合，核心洞察（differential misclassification distorts subgroup estimates）在统计文献中不够 novel，leading to \"incremental contribution\" 的评判。\n2. **缺乏 end-to-end real-world validation**: Semi-synthetic 验证虽然设计精良，但审稿人可能质疑 DGP 的外部效度（\"your synthetic setup guarantees the problem exists; show me it matters in the real world\"）。Ashwin 数据只能验证前提，不能验证完整 pipeline 的 CATE 改善。\n\n【实施评估】:\n  - 计算资源: 中等。VI fitting + causal forest + 大规模 simulation 需要多核 CPU 集群，单个 DGP 配置的 200 次 replication 可能需要数小时。LLM annotation 需要 API 调用（GPT-4.1, Qwen 3.5, Llama 3.3），API 成本约 $500-2000（取决于数据规模）。无需 GPU 训练。\n  - 数据需求: 低-中等。Semi-synthetic 使用公开政治文本语料（immigration framing / partisan tweets），Ashwin et al. Rohingya 数据集已发表。不需要新数据收集。\n  - 人工介入: 低。不需要新的人工标注（使用 Ashwin 数据的已有专家标注）。Semi-synthetic 中的\"专家标注\"由 DGP 生成。\n  - 训练需求: 无模型训练。使用现成 LLM API 做标注，使用 grf 等现有 CATE 估计包。Hierarchical Bayesian model fitting 不算\"训练\"。\n  - 新 Benchmark: 否。Semi-synthetic DGP matrix 是验证框架而非 benchmark。但 DGP matrix + 评估 protocol 本身可以作为后续工作的 benchmark 基础。\n  - 预估周期: 2.5-4 个月。方法实现 2-3 周；semi-synthetic 实验 4-6 周（大规模 simulation）；real-data validation 1-2 周；论文写作 3-4 周。可并行化。\n```\n\n---\n\nSources:\n- [Benchmarking Debiasing Methods for LLM-based Parameter Estimates (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)\n- [Stratified Prediction-Powered Inference (NeurIPS 2024)](https://arxiv.org/abs/2406.04291)\n- [PPI is the Difference Estimator (Mozer, 2025)](https://arxiv.org/html/2603.19160)\n- [Hidden Measurement Error in LLM Pipelines (Messing, 2026)](https://arxiv.org/abs/2604.11581)\n- [Using LLMs for Qualitative Analysis can Introduce Serious Bias (Ashwin et al., 2025)](https://journals.sagepub.com/doi/10.1177/00491241251338246)\n- [Prediction-Powered Conditional Inference (Sui et al., 2026)](https://arxiv.org/abs/2603.05575)\n- [Detecting and Mitigating Group Bias in HTE (Persson et al., 2026)](https://arxiv.org/abs/2602.20383)\n- [Assumption-Lean Differential Variance Inference for HTE Detection (Boileau et al., 2025)](https://arxiv.org/abs/2512.03254)\n- [Surrogate Representation Inference (Jerzak et al., 2025)](https://arxiv.org/abs/2509.12416)\n- [Active Multiple-Prediction-Powered Inference (AM-PPI, 2026)](https://arxiv.org/abs/2605.08429)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient field research to provide an informed evaluation. Let me compile the full assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [Audinet de Pieuchon et al., \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\"](https://aclanthology.org/2025.emnlp-main.1000/) (EMNLP 2025): 直接上游工作。系统比较 DSL、PPI 等去偏方法用于 LLM 标注的参数估计。但所有方法限于 population-level estimands (ATE/回归系数)，不涉及 CATE/HTE。验证了 EC-HTE 所声称的\"现有方法只解决 ATE 层面问题\"这一前提。重要的是，此论文被 EMNLP 2025 接收，说明 EMNLP 审稿人对该方向有接受度。\n\n- [Fisch et al., \"Stratified Prediction-Powered Inference for Hybrid Language Model Evaluation\"](https://arxiv.org/abs/2406.04291) (NeurIPS 2024): StratPPI 通过分层采样改进 PPI 的置信区间宽度。虽引入了 subgroup 概念，但目标仍是全局参数的更紧估计，不是 subgroup-specific 因果效应。EC-HTE 的问题设定（校正 effect modifier 中的差异化误分类）与 StratPPI 结构性不同。\n\n- [Ashwin et al., \"Using Large Language Models for Qualitative Analysis can Introduce Serious Bias\"](https://arxiv.org/abs/2309.17147) (Sociological Methods & Research 2025): 直接实证支撑。在 Rohingya 难民访谈数据上证明 LLM 编码错误与受访者的难民身份、性别、教育水平系统性相关。这恰好是 EC-HTE 所针对的\"误分类率与 subgroup 协变\"前提的经验证据。Proposal 选择此数据集做 real-data validation 非常合理。\n\n- [Messing, \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\"](https://arxiv.org/abs/2604.11581) (arXiv 2025): 文档化 LLM 管线中隐藏测量误差导致 naive 置信区间 under-cover 40–60%。但分析停留在 aggregate level，未延伸到因果 HTE。EC-HTE 填补了从 aggregate 到 subgroup-level 因果推断的空白。\n\n- [Sui et al., \"Prediction-Powered Conditional Inference\"](https://arxiv.org/abs/2603.05575) (arXiv 2026): PPCI 将 PPI 扩展到条件泛函（给定固定 test point 的条件均值等），使用 kernel localization。关键区别：PPCI 假设 conditioning variable 是正确的，处理的是 outcome prediction noise；EC-HTE 处理的是 conditioning variable 本身（effect modifier）被误分类的情况。Proposal 对此区别的阐述是准确的。\n\n- [Persson et al., \"Detecting and Mitigating Group Bias in Heterogeneous Treatment Effects\"](https://arxiv.org/abs/2602.20383) (arXiv 2026): 处理 CATE→GATE 聚合产生的偏差，用 shrinkage 校正。但假设 covariates 是干净的——bias 来源是聚合过程而非测量误差。EC-HTE 处理的是更上游的问题：effect modifier 本身就被错标了。\n\n- [Boileau et al., \"Assumption-Lean Differential Variance Inference for Heterogeneous Treatment Effect Detection\"](https://arxiv.org/abs/2512.03254) (arXiv 2025): 在 effect modifier 缺失或严重测量误差下，通过 potential outcomes 方差对比进行 HTE 检测。但目标是假设检验（\"是否存在异质性\"），而非 CATE 估计。与 EC-HTE 互补而非竞争。\n\n- 调研总结: 该领域存在一个清晰且真实的空白——现有 LLM 标注去偏方法全部锁定在 ATE/population-level，而 CATE/HTE 估计中 effect modifier 误分类导致的偏差尚无人系统处理。EC-HTE 精准定位在 Thread 1 (LLM debiasing) 与 Thread 2 (HTE estimation) 的交叉点，novelty claim 成立。\n\n【整体印象】:\n作为审稿人，我的第一反应是\"这是一篇 well-crafted、有理论深度的 proposal，解决了一个真实且尚未被解决的问题\"。问题识别犀利——\"全局校正不仅不够，还可能恶化 CATE 估计\"这个 anti-intuitive finding 非常有力。Related work 的五线程梳理展现了对领域全景的深刻理解，且每一条 differentiation 经我调研验证均准确。实验设计全面、系统。总体倾向 weak accept 至 borderline accept。\n\n主要保留意见：(1) 主题位于因果推断与 NLP 的深度交叉区，对纯 NLP 审稿人可能显得过于统计学化；(2) 三阶段框架的复杂度可能被质疑——是否有更简单的替代方案；(3) Real-data evaluation 仅验证前提（差异化误分类存在），未完成端到端 CATE 校正验证。\n\n【核心贡献】:\n核心贡献有三层：\n1. **问题形式化**：首次识别并形式化\"LLM 标注误分类在 effect modifier 中的差异化导致 CATE distortion\"这一新偏差类别，并证明全局校正可恶化估计——这具有独立的理论价值。\n2. **可操作诊断准则**：误分类异质性 × CATE 异质性的有限样本 bound，任何研究者在做 CATE 分析前可直接计算，判断是否需要 stratified correction。这个诊断的 standalone value 很高。\n3. **三阶段校正框架**：从 hierarchical Bayesian 误分类估计到 sandwich variance 调整再到自适应标注分配，提供了完整的解决方案。\n\n对领域的价值：中高。随着 LLM-as-annotator 在 CSS 中的普及，从 ATE debiasing 扩展到 CATE debiasing 是自然且重要的下一步。诊断准则尤其有实用价值。\n\n【方法合理性】:\n方法整体合理，各组件有充分的统计学基础：\n- **Stage 1** (Hierarchical Bayesian partial pooling): 在\"全局单一混淆矩阵 vs. 每个 subgroup 独立估计\"之间取折中，是处理小样本 subgroup 的标准做法，合理。\n- **Stage 2** (Sandwich variance): 传统的 two-stage estimation 不确定性传播方法，成熟可靠。\n- **Stage 3** (Adaptive allocation): 基于 bias bound 的分配策略逻辑自洽——将标注预算分配给\"误分类不确定性 × CATE magnitude\"最大的 subgroup。\n\n**更简单的替代方案？** 一个自然的简化方案是跳过 hierarchical Bayesian，直接对每个 subgroup 独立估计混淆矩阵然后 plug-in。Proposal 在 ablation 中覆盖了这个对比 (Stage 1 ablation: no pooling vs. partial pooling vs. full pooling)，这是正确的做法。如果 ablation 显示 partial pooling 的增益有限，审稿人可能质疑 Stage 1 的复杂度。但这不是致命问题——empirical result 会给出答案。\n\n另一个替代方案：直接用 PPCI (Sui et al.) 的 kernel localization 方法，将 effect modifier 的 soft probability 作为 continuous conditioning variable。但正如 proposal 所指出的，PPCI 假设 conditioning variable 正确，categorical misclassification 不是 continuous noise，kernel localization 在此无效。Proposal 对此的论述是准确的。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】— 问题真实、重要且尚未解决。经调研验证，现有方法（DSL、PPI、StratPPI、PPCI）均不解决 CATE 层面的 effect modifier 误分类问题。Ashwin et al. (2025) 提供了差异化误分类的直接经验证据，证实这不是人造问题。\"全局校正可恶化 CATE\"的理论发现更增加了问题的紧迫性。唯一的弱点是：做 CATE 分析且使用 LLM 标注作为 effect modifier 的研究者群体，虽在增长，目前可能仍是一个相对小的 niche。\n\n2. 方法与创新: 【中偏强】— Novelty claim 经调研验证成立：无直接竞争工作。与 PPCI (conditioning variable noise vs. conditioning variable misclassification)、Persson (aggregation bias vs. measurement error)、Boileau (detection vs. estimation) 的区别清晰且准确。方法本身是对已有组件（hierarchical Bayesian、sandwich variance、adaptive allocation）的合理组装，单个组件的新颖性有限，但组装方式和问题-方法的匹配是新的。创新更多来自 problem identification + theoretical insight (bias bound) 而非 method design。\n\n3. 实验设计: 【强】— 这是 proposal 的一大亮点。DGP matrix 覆盖了关键因素（误分类严重度、CATE 异质性、subgroup 数、误分类-CATE 相关方向），尤其是包含正/负相关方向来验证理论预测。Comparison methods 涵盖 6 种基线（uncorrected、global、arm-specific、SIMEX、calibration-only、EC-HTE），非常充分。评价指标（PEHE、subgroup bias、CI coverage、CI width、GATE RMSE、bound tightness）覆盖了 accuracy 和 inference validity 两个维度。Ablation 设计系统（3 个 stage 各自 ablation + diagnostic validation + CATE estimator robustness check）。200+ replications per configuration 是足够的。预算曲线 (B ∈ {100, 500, 1000, 2000}) 可展示方法的 practical operating range。依据 NeurIPS D&B 2021 (\"Really Doing Great at Estimating CATE?\") 的评估标准，该实验设计达到了 CATE 文献的严谨要求。\n\n4. 可行性: 【中偏强】— 方案可执行。Semi-synthetic experiments 不需要海量计算（hierarchical Bayesian with VI + causal forest，标准硬件即可）。LLM 标注成本通过使用 API (GPT-4.1) 和开源模型 (Qwen 3.5, Llama 3.3) 可控。Ashwin et al. 数据集已公开。主要风险：(a) 200+ replications × 12-14 configurations × 多种 N 和 B 组合 = 大量实验运行，需要良好的实验管理；(b) hierarchical Bayesian + MCMC validation in appendix 需要一些统计学实现功力。但总体上是一个两人团队在 3-4 个月内可完成的项目。\n\n5. 写作与呈现: 【强】— Proposal 本身的写作质量很高。问题动机以 anti-intuitive finding 开篇，有说服力。五线程 related work 结构清晰，differentiation 精准。方法描述逻辑流畅（三阶段 + cold-start protocol）。Scope 和 limitations 坦诚（仅处理 categorical modifier）。实验设计的呈现有条理。如果正式论文保持这一写作水平，对审稿人来说是一个 pleasant reading experience。\n\n【概率估计】: [32% - 43%] 中位 37%\n\n【估计理由】:\n- **上推因素**: (1) 问题真实、novelty claim 经验证成立，填补 ATE→CATE debiasing 的真实空白；(2) 理论贡献（bias bound + \"全局校正可恶化\"的证明）有独立价值且 anti-intuitive；(3) 实验设计非常完备，达到因果推断文献的严谨标准；(4) Audinet de Pieuchon et al. 在 EMNLP 2025 被接收，证明该方向在 EMNLP 有 reviewer base；(5) 写作质量高。\n- **下拉因素**: (1) 主题深度交叉（因果推断 + 测量误差 + NLP），可能遇到不熟悉因果 HTE 方法论的审稿人，导致 appreciation gap；(2) 方法是已有组件的合理组装（hierarchical Bayesian + sandwich + adaptive allocation），方法层面的 novelty 有限，创新更多在 problem identification 和 theory；(3) Real-data validation 仅验证前提而非端到端 CATE 校正效果，审稿人可能要求更有说服力的真实应用；(4) 实际受益人群（做 LLM-annotated CATE 分析的研究者）目前可能偏小众，impact 论证需要更有说服力；(5) 三阶段框架的复杂度可能被质疑，尤其如果 ablation 显示简化版本效果接近。\n- 综合判断：这是一篇 solid 且有实质贡献的 proposal，质量在 EMNLP 接收线附近。以当前方案执行到位的话，属于 borderline accept，最终结果很大程度取决于审稿人匹配和实验结果的强度。\n\n【主要风险】:\n1. **审稿人匹配风险**: EMNLP 审稿人池中同时精通因果推断 (HTE/CATE) 和 NLP annotation debiasing 的审稿人比例有限。如果匹配到纯 NLP 背景的审稿人，可能对 hierarchical Bayesian confusion matrix estimation 和 sandwich variance 的贡献缺乏 appreciation，给出\"方法过于统计学化、不够 NLP\"的评价。\n2. **Real-data validation 不完整**: 最有说服力的证据应该是在一个具有真实因果结构的数据集上展示端到端的 CATE 校正效果，但当前方案的 Ashwin et al. 数据仅用于验证差异化误分类的前提。审稿人可能要求\"show me it works on a real causal problem\"——而半合成实验虽然设计严谨，说服力天然弱于真实应用。\n\n【实施评估】:\n  - 计算资源: 中等。Hierarchical Bayesian (VI) + Causal Forest 不需要 GPU 训练，标准 CPU 集群即可。200+ replications × ~14 configurations × 多种 N/B 组合需要 batch 运行管理，但单次运行耗时不长。LLM 标注使用 API 调用，成本取决于 corpus 规模（GPT-4.1 API 费用需纳入预算）。\n  - 数据需求: 中等。需要一个有真实语言变异的政治学文本语料（如移民框架数据或党派推文数据集，此类公开数据集较多）。Ashwin et al. (2025) 的 Rohingya 访谈数据集需获取（已发表论文的数据，通常可获得）。\n  - 人工介入: 不需要新的人工标注。Expert labels 在 semi-synthetic 实验中是模拟的（DGP 控制），real-data 部分使用 Ashwin et al. 已有的人工标注。\n  - 训练需求: 不涉及 LLM 训练或微调。仅使用现成 LLM 做 zero-shot/few-shot 标注。Hierarchical Bayesian 模型和 Causal Forest 是传统统计/ML 模型，无需 GPU 训练。\n  - 新 Benchmark: 不需要构建新 benchmark。Semi-synthetic DGP 和 Ashwin et al. 数据即为评估基础。DGP 设计本身可作为社区可复用的 benchmark suite（加分项）。\n  - 预估周期: 3-4 个月（1 个月：理论推导 + 方法实现；1-1.5 个月：semi-synthetic 实验；0.5-1 个月：real-data validation + 写作）。适合 2 人团队，需具备因果推断和 Bayesian 建模经验。\n```\n\nSources:\n- [Benchmarking Debiasing Methods for LLM-based Parameter Estimates (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)\n- [Stratified Prediction-Powered Inference (NeurIPS 2024)](https://arxiv.org/abs/2406.04291)\n- [Ashwin et al., LLM Qualitative Analysis Bias (SMR 2025)](https://arxiv.org/abs/2309.17147)\n- [Messing, Hidden Measurement Error in LLM Pipelines (arXiv 2025)](https://arxiv.org/abs/2604.11581)\n- [Sui et al., Prediction-Powered Conditional Inference (arXiv 2026)](https://arxiv.org/abs/2603.05575)\n- [Persson et al., Detecting and Mitigating Group Bias in HTE (arXiv 2026)](https://arxiv.org/abs/2602.20383)\n- [Boileau et al., Assumption-Lean Differential Variance Inference for HTE Detection (arXiv 2025)](https://arxiv.org/abs/2512.03254)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n## EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation Under LLM Annotation Misclassification\n\n## Problem and Motivation\n\nWhen NLP researchers use LLM-generated annotations as effect modifiers in causal heterogeneous treatment effect (HTE) analysis, a previously unrecognized structural bias arises: LLM misclassification rates covary with the true conditional average treatment effect (CATE). Subgroups where LLMs err most in annotation (e.g., marginalized populations, linguistically complex cases) are often the same subgroups where treatment effects are largest. This creates a confounding between measurement error and causal heterogeneity that cannot be resolved by any global correction method—including arm-specific rectifiers (Mozer, arXiv:2603.19160), which address average treatment effect (ATE) bias but are algebraically incapable of correcting subgroup-level CATE distortions.\n\nThis problem is urgent. LLM-as-annotator has become the default pipeline for computational social science (Audinet de Pieuchon et al., EMNLP 2025, benchmarking DSL vs. PPI debiasing; StratPPI, Fisch et al., NeurIPS 2024, improving PPI via stratification), and researchers increasingly use LLM annotations not just for ATE estimation (where DSL and PPI provide corrections) but for subgroup analysis and effect modification—yet no correction method exists for this latter use case. Messing (arXiv:2604.11581) documents that hidden measurement error in LLM pipelines causes naive confidence intervals to under-cover by 40–60%, but this analysis remains at the aggregate level. Ashwin et al. (Sociological Methods & Research, 2025) provide direct empirical evidence that LLM coding errors in refugee interview transcripts correlate systematically with respondents' refugee status, gender, and education level—precisely the variables used as effect modifiers in downstream causal analysis. Any study using LLM-annotated text variables as moderators produces unreliable heterogeneity findings whenever annotation error rates differ across subgroups—and Ashwin et al. show this is the norm, not the exception.\n\n**Key anti-intuitive finding: global correction can actively worsen CATE estimates.** Consider a two-subgroup example. Subgroup A has high misclassification (25%) and large CATE (0.5 SD); Subgroup B has low misclassification (5%) and small CATE (0.1 SD). A global correction uses a pooled confusion matrix (~15% error), which under-corrects Subgroup A and over-corrects Subgroup B. The net effect: globally-corrected CATE estimates can have *larger* bias than uncorrected estimates. This is not an edge case—it occurs whenever the misclassification pattern and CATE structure are positively correlated, which empirical evidence suggests is common in practice.\n\n## Core Contributions\n\nThis paper makes four contributions:\n\n1. **Problem identification and formalization.** We identify and formalize measurement-error-induced CATE distortion—a new class of bias arising when LLM annotation errors in effect modifiers are differential across subgroups and correlated with the true heterogeneity structure. We show this is structurally distinct from: ATE-level debiasing (Mozer, arXiv:2603.19160; Egami et al., NeurIPS 2023 DSL; Zrnic & Candès, ICML 2024), CATE-to-GATE aggregation bias (Persson et al., arXiv:2602.20383, where bias originates from aggregation, not measurement error), and conditional inference with outcome prediction noise (Sui et al., arXiv:2603.05575 PPCI, which assumes the conditioning variable is correct). We prove that global correction can *increase* CATE bias relative to uncorrected estimates when misclassification and CATE heterogeneity are positively correlated.\n\n2. **Actionable diagnostic criterion (Bias Bound).** We derive a finite-sample bound: the bias of globally-corrected CATE estimates is proportional to the product of (a) misclassification heterogeneity across subgroups and (b) CATE heterogeneity across subgroups. This product yields a practical diagnostic: given pilot data, any researcher can compute this quantity *before* running full CATE analysis to determine whether global correction suffices or stratified correction is necessary. This diagnostic has standalone value independent of the EC-HTE framework—it applies to any CATE analysis using LLM-annotated effect modifiers. The bound implies that bias is worst when annotation is least accurate for subgroups where treatment effects are largest—empirically common (Ashwin et al., 2025).\n\n3. **EC-HTE: A three-stage correction framework** providing subgroup-specific misclassification correction, valid confidence intervals, and optimal annotation allocation (detailed below).\n\n4. **Empirical validation** via semi-synthetic benchmarks with controlled DGPs (including systematic variation of misclassification-CATE correlation direction) and a real-data misclassification pattern validation (Ashwin et al., 2025, Rohingya interview corpus).\n\n## Why Not Just Use Expert Labels?\n\nA natural objection: why not skip LLM annotation entirely and estimate CATEs using only expert-labeled data? The answer is a bias-variance tradeoff specific to CATE estimation. With a budget of ~2,000 expert labels distributed across k subgroups, each subgroup contains ~2,000/k observations. Honest causal forests (Wager & Athey, JASA 2018) split this further into estimation and splitting samples, leaving each cell with ~1,000/k observations—insufficient for detecting moderate heterogeneity when k ≥ 4.\n\nEC-HTE resolves this by using the full unlabeled corpus (potentially hundreds of thousands of LLM-annotated observations) for low-variance CATE estimation, with expert labels only for calibrating subgroup-specific misclassification. This extends the PPI/DSL paradigm—combining noisy large-scale with clean small-scale data—from ATE to CATE, where data demands make the combination even more critical.\n\n## Method: Three-Stage Framework\n\n**Stage 1: Hierarchical Bayesian Subgroup-Specific Misclassification Estimation.** For each effect-modifier subgroup g ∈ {1, …, k}, we estimate a confusion matrix C_g between LLM annotation and expert gold standard using a hierarchical Bayesian model with partial pooling. The hierarchy allows low-sample subgroups to borrow strength from the global structure while permitting genuine cross-subgroup variation. This addresses a key tension: per-subgroup independent estimation (high variance when subgroup expert-label counts are small) vs. single global estimation (biased when misclassification rates genuinely differ). For computational scalability in large-scale simulation studies, we use variational inference (VI) as the primary fitting method, with MCMC validation on representative configurations in the appendix.\n\n**Stage 2: Corrected CATE Estimation with Sandwich Variance Adjustment.** Corrected effect-modifier assignments are fed into an honest causal forest (Wager & Athey, JASA 2018). Because Stage 1 introduces nuisance parameter uncertainty, naive confidence intervals will under-cover. We derive a sandwich variance inflator propagating Stage 1 uncertainty into Stage 2 CIs, ensuring valid coverage. Bootstrap-based CIs serve as a robustness check.\n\n**Stage 3: Adaptive Expert Annotation Allocation.** Given a fixed expert budget B, we optimize allocation across subgroups by jointly minimizing misclassification estimation uncertainty and CATE estimation variance. The allocation criterion targets subgroups where the product of misclassification uncertainty and CATE magnitude is largest—precisely where annotation errors cause the most CATE distortion (as predicted by the bias bound).\n\n**Cold-start protocol.** Since Stage 3 requires initial estimates of both misclassification rates and CATE magnitudes, we employ a multi-batch protocol: (a) allocate 20–30% of B as a uniform pilot batch; (b) estimate initial confusion matrices and CATE values; (c) allocate remaining budget adaptively. We include pilot ratio sensitivity analysis (10%, 20%, 30%) in the experiments.\n\n## Related Work and Differentiation\n\n**Thread 1: LLM annotation debiasing (ATE-level).** DSL (Egami et al., NeurIPS 2023), PPI and its algebraic equivalence to survey-sampling difference estimators (Mozer, arXiv:2603.19160), active inference (Zrnic & Candès, ICML 2024), stratified PPI (StratPPI, Fisch et al., NeurIPS 2024), active multi-predictor PPI (AM-PPI, arXiv:2605.08429), and benchmarking thereof (Audinet de Pieuchon et al., EMNLP 2025). All locked to population-level estimands. Messing (arXiv:2604.11581) diagnoses hidden measurement error causing 40–60% CI under-coverage but does not extend to causal HTE correction.\n\n**Thread 2: HTE/CATE estimation methods.** Honest causal forests (Wager & Athey, JASA 2018), DR-learner, CATE-to-GATE aggregation bias correction (Persson et al., arXiv:2602.20383, shrinkage for aggregation-induced bias assuming clean covariates), and assumption-lean HTE detection under mismeasured modifiers (Boileau et al., arXiv:2512.03254, hypothesis testing for whether heterogeneity exists, not CATE estimation—complementary to EC-HTE). CATE evaluation standards established in \"Really Doing Great at Estimating CATE?\" (NeurIPS D&B 2021).\n\n**Thread 3: Conditional inference with ML predictions.** PPCI (Sui et al., arXiv:2603.05575) extends PPI to conditional functionals at fixed test points via kernel localization. Critical distinction: PPCI addresses outcome prediction noise at a correctly-specified conditioning point; EC-HTE addresses the situation where the conditioning variable (effect modifier) itself is misclassified. PPCI's localization anchors on correct covariate values—when the anchor itself is wrong (categorical misclassification), kernel localization cannot help.\n\n**Thread 4: Measurement error correction for ML-generated variables.** ForestIV (Bu et al., INFORMS JDS 2023) uses random forest tree tuples as instrumental variables, but requires IV exclusion restrictions and is limited to regression settings, not CATE with categorical effect modifiers. Jerzak et al. (arXiv:2509.12416, SRI framework) provide valid inference under noisy annotation but do not address effect modifier misclassification's impact on HTE. SIMEX handles continuous measurement error models but does not directly apply to categorical misclassification.\n\n**Thread 5: Causal inference with textual variables.** Feldman et al. (arXiv:2602.15730) address latent textual treatment estimation using SAE + residualization, assuming clean effect modifiers. Nwankwo et al. (arXiv:2502.10605, NeurIPS 2025 Workshop) optimize annotation allocation for doubly robust ATE with missing outcomes—different estimand (ATE vs. CATE), different error source (outcome missingness vs. effect modifier misclassification), different optimization landscape.\n\nEC-HTE sits at the intersection of Threads 1–4: correcting LLM misclassification specifically in effect modifiers for valid CATE estimation.\n\n## Validation Design\n\n### Semi-Synthetic Experiments\n\n**Corpus.** Political science text corpus with real-world linguistic variation (e.g., immigration framing data or partisan tweet datasets with known ideological annotations).\n\n**DGP Matrix.** Core factors:\n- Misclassification severity: high (25–30%) vs. low (5–10%)\n- CATE heterogeneity magnitude: large (>0.3 SD) vs. small (<0.1 SD)\n- Subgroup count: k=3 vs. k=6\n- **Misclassification-CATE correlation direction**: positive (high-error subgroups have high CATE, worst-case) vs. negative (high-error subgroups have low CATE, best-case)\n\nSelective design: 12–14 configurations covering all worst-case/best-case combinations for the key factors, rather than full 2⁴=16 factorial.\n\nTreatment assignment T ~ Bernoulli(0.5); potential outcomes Y(1), Y(0) generated with known ground-truth CATE τ(x) varying by subgroup.\n\n**Replications.** ≥ 200 per configuration.\n\n**Sample sizes.** N ∈ {2000, 5000, 10000}.\n\n**Expert label budget.** B ∈ {100, 500, 1000, 2000} to produce budget vs. performance curves. All methods compared under identical total budget.\n\n**LLMs.** Three annotators: GPT-4.1 (proprietary frontier), Qwen 3.5 (open-source large), Llama 3.3 (open-source, different family). Fourth LLM as appendix robustness check.\n\n### Comparison Methods (all under fixed expert annotation budget B)\n\n1. **Uncorrected**: LLM annotations used directly as effect modifiers in causal forest.\n2. **Globally-corrected**: Single confusion matrix → corrected annotations → causal forest.\n3. **Arm-specific (Mozer-style)**: Separate confusion matrices for treatment/control arms → causal forest.\n4. **SIMEX + causal forest**: SIMEX-based measurement error correction → causal forest.\n5. **Calibration-only + causal forest**: Platt scaling / temperature scaling → calibrated probabilities as soft effect modifiers → causal forest.\n6. **EC-HTE (full)**: Hierarchical Bayesian subgroup-specific correction → sandwich-adjusted causal forest → adaptive allocation.\n\n### Evaluation Metrics\n\n- **PEHE**: √E[(τ̂(x) − τ(x))²], overall and per-subgroup.\n- **Subgroup CATE bias**: |E[τ̂_g] − τ_g| for each subgroup g.\n- **CI empirical coverage**: Fraction of replications where true CATE falls within 95% CI (target: 0.95).\n- **CI width**: Efficiency measure at fixed coverage.\n- **GATE RMSE**: RMSE of group average treatment effect estimates.\n- **Bound tightness**: Observed bias vs. theoretical bound prediction.\n\n### Ablation Studies\n\n**Stage 1 ablation (partial pooling):**\n- (a) Hierarchical Bayesian with VI (partial pooling)\n- (b) Per-subgroup independent confusion matrices (no pooling)\n- (c) Single global confusion matrix (full pooling)\n- (d) Prior sensitivity: 2–3 prior settings (weakly informative, moderately informative, diffuse) on 1–2 representative DGP configurations\n\n**Stage 2 ablation (variance adjustment):**\n- (a) Sandwich variance-adjusted CIs\n- (b) Bootstrap-based CIs\n- (c) Naive CIs (no adjustment)\n→ Compare empirical coverage rates.\n\n**Stage 3 ablation (allocation strategy):**\n- (a) Joint criterion (misclassification uncertainty × CATE magnitude)\n- (b) Misclassification-uncertainty-only allocation\n- (c) CATE-magnitude-only allocation\n- (d) Uniform allocation\n- (e) Pilot ratio sensitivity: 10%, 20%, 30% of B as uniform pilot batch\n→ Compare PEHE at fixed total budget B.\n\n**Diagnostic validation:** Systematically vary misclassification heterogeneity and CATE heterogeneity (including correlation direction); produce heatmap of EC-HTE improvement over global correction vs. (product of heterogeneity measures). Verify that the theoretical bound predicts when global correction fails and when it suffices. Specifically demonstrate that global correction is worse than uncorrected in positive-correlation configurations.\n\n**CATE estimator robustness (appendix):** In 1–2 worst-case configurations, replace causal forest with DR-learner to verify EC-HTE's correction generalizes beyond a single CATE estimator.\n\n### Real-Data Application (Ashwin et al., 2025)\n\n**Dataset.** Rohingya refugee interview transcripts (Ashwin et al., Sociological Methods & Research 2025). This dataset's primary role is validating the premise of EC-HTE—that LLM misclassification is differential—rather than evaluating CATE estimation accuracy (the dataset lacks a natural causal structure).\n\n**Validation goals:**\n1. **Differential misclassification pattern confirmation**: Quantify and visualize how LLM error rates vary across subgroups defined by refugee status, gender, education.\n2. **Leave-expert-out calibration test**: Treat full human labels as ground truth, subsample B expert labels, evaluate whether EC-HTE's hierarchical confusion matrix estimates recover the true subgroup-specific error patterns better than global estimation.\n3. **Diagnostic criterion demonstration**: Compute the misclassification-heterogeneity × CATE-heterogeneity product on this dataset (constructing a plausible causal question from available variables) to demonstrate the diagnostic's operability.\n4. **Budget curve**: Accuracy of confusion matrix recovery vs. expert label budget B.\n\nCATE estimation accuracy is rigorously evaluated in the semi-synthetic experiments where ground-truth CATE is known.\n\n## Scope and Limitations\n\nEC-HTE targets **categorical effect modifiers** (stance, topic, sentiment, entity type, etc.)—the dominant use case when LLM annotations serve as moderators in computational social science. When the effect modifier is a continuous variable that has been discretized (binned), misclassification includes both LLM errors and discretization error; the current framework does not disentangle these sources. Extension to continuous effect modifiers with measurement error (where SIMEX-type approaches may be more natural) is future work.\n\n## Broader Applicability\n\nWhile our validation focuses on CSS, the same problem structure arises whenever ML-predicted categorical variables serve as effect modifiers: in medical research (ML-classified tumor subtypes as moderators of drug efficacy), education (NLP-coded classroom behaviors moderating intervention effects), and policy evaluation (automated classification of administrative characteristics). EC-HTE's framework and diagnostic criterion apply directly to these settings.\n\n## Expected Contributions\n\nEC-HTE provides (1) the first formal identification of measurement-error-induced CATE distortion in LLM-annotated pipelines, including the proof that global correction can worsen estimates; (2) an actionable diagnostic (the misclassification-heterogeneity × CATE-heterogeneity product) with standalone value for any CATE analysis; (3) a practical three-stage correction framework with valid inference; and (4) comprehensive empirical validation. The framework serves any study using LLM-annotated categorical text variables as effect modifiers in causal analysis."
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:27:19.229Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:27:19.229Z",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T04:27:19.240Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research data. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Audinet de Pieuchon et al., "Benchmarking Debiasing Methods for LLM-based Parameter Estimates"](https://aclanthology.org/2025.emnlp-main.1000/) (EMNLP 2025): 最直接的同领域工作，对比 DSL/PPI 在 LLM 标注去偏中的效果。证明 EMNLP 接收此类方法论论文。但该工作聚焦 ATE 级别去偏，未涉及 CATE。
- [Mozer, "PPI is the Difference Estimator"](https://arxiv.org/abs/2603.19160) (arXiv 2026): 揭示 PPI 与调查抽样差异估计量的代数等价性，含 arm-specific rectifier。仍限于总体水平估计量，无法处理子群级 CATE 偏差。
- [Fisch et al., StratPPI](https://arxiv.org/abs/2406.04291) (NeurIPS 2024): 通过分层改进 PPI 的置信区间宽度。方向相关但估计目标仍为总体参数的分层改进，非 CATE 估计。
- [Sui et al., PPCI](https://arxiv.org/abs/2603.05575) (arXiv 2026): 将 PPI 扩展至条件推断，使用核局部化。关键区分：PPCI 处理的是结果预测噪声，假设条件变量正确；EC-HTE 处理的是条件变量（效应修饰符）本身的误分类。互补而非竞争。
- [Persson et al., "Detecting and Mitigating Group Bias in HTE"](https://arxiv.org/abs/2602.20383) (arXiv 2026): 处理 CATE→GATE 聚合偏差，通过 shrinkage 校正。偏差来源不同（聚合 vs. 测量误差），假设协变量无噪声。互补关系。
- [Boileau et al., "Assumption-Lean Differential Variance Inference"](https://arxiv.org/abs/2512.03254) (arXiv 2025): 在效应修饰符缺失或测量有误时进行异质性假设检验。但只做假设检验（是否存在异质性），不做 CATE 估计。互补关系。
- [Ashwin et al., "Using LLMs for Qualitative Analysis can Introduce Serious Bias"](https://journals.sagepub.com/doi/10.1177/00491241251338246) (Sociological Methods & Research 2025): 直接实证支撑——LLM 在难民访谈编码中的误差与受访者特征（难民身份、性别、教育水平）系统性相关。证实差异性误分类是常态。
- [Messing, "Hidden Measurement Error in LLM Pipelines"](https://arxiv.org/abs/2604.11581) (arXiv 2026): 文档化 LLM 管线中隐藏测量误差导致置信区间 40-60% 欠覆盖。但分析停留在聚合层面。
- [Jerzak et al., SRI Framework](https://arxiv.org/abs/2509.12416) (arXiv 2025): 在带噪标注下提供有效推断，但未涉及效应修饰符误分类对 HTE 的影响。
- 调研总结: 该领域存在一个清晰且已被验证的空白——所有现有去偏方法（DSL/PPI/StratPPI/arm-specific rectifier）均锁定于总体级别估计量；所有现有 CATE 方法均假设协变量正确。EC-HTE 恰好填补了"LLM 标注误分类 × CATE 估计"的交叉空白，且 Ashwin et al. 的实证数据证实了差异性误分类在实践中普遍存在。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇问题识别精准、方法设计合理、实验方案异常完备的方法论投稿。问题的动机令人信服——差异性误分类与 CATE 异质性正相关时全局校正反而恶化估计这一反直觉发现，是整篇论文的核心 hook，具有很强的说服力。总体倾向 weak accept。但我会关注技术新颖性是否足够——方法本身是已有技术（层次贝叶斯 + 因果森林 + 自适应分配）的组合式应用，核心贡献更多在问题识别和形式化上。

【核心贡献】:
1. 首次识别并形式化了 LLM 标注误分类在效应修饰符上对 CATE 估计的结构性偏差，并证明全局校正可能恶化估计（当误分类异质性与 CATE 异质性正相关时）。
2. 提出可操作的诊断准则（误分类异质性 × CATE 异质性乘积），具有独立的方法论价值。
3. 三阶段校正框架（层次贝叶斯部分池化 → 三明治方差调整 → 自适应标注分配）。
这些贡献对计算社会科学和 NLP-for-social-science 领域有显著价值。随着 LLM-as-annotator 成为默认管线，子群分析的可靠性问题日益突出，本工作的实际影响力较大。

【方法合理性】:
方法整体合理，三阶段设计逻辑自洽。层次贝叶斯部分池化解决了"独立估计（高方差）vs. 全局估计（有偏）"的核心张力，是处理子群混淆矩阵的合适选择。三明治方差调整传播第一阶段的 nuisance parameter 不确定性，是标准且正确的做法。自适应分配的准则（误分类不确定性 × CATE 量级）与理论 bias bound 一致。

关于更简单替代方案的考量：
- 直接用 StratPPI 进行子群级估计？不行——StratPPI 改进的是 CI 宽度，仍是同一估计量的分层，不处理效应修饰符误分类。
- 直接用子群独立混淆矩阵（无层次结构）？这正是 ablation 中的对照之一，在小样本子群中会高方差。
- 不做自适应分配？均匀分配会浪费预算在低影响子群上。
因此，方法的复杂度与问题复杂度匹配，没有明显的过度工程。

【5 维度打分】:

  1. 研究问题: 【强】 — 问题真实、重要、有实证支撑（Ashwin et al. 2025 直接证明差异性误分类是常态），且具有明确的时效性（LLM-as-annotator 管线在 CSS 中爆炸式增长）。反直觉发现（全局校正可恶化估计）提供了强有力的叙事 hook。问题定义清晰，与已有工作的区分（vs. ATE 去偏、vs. CATE-GATE 聚合偏差、vs. PPCI 的条件推断）均有理有据。

  2. 方法与创新: 【中偏强】 — 核心新颖性在于问题识别与形式化（包括 bias bound 推导），而非技术组件本身。层次贝叶斯部分池化、因果森林、自适应采样均为成熟技术。EC-HTE 的贡献是将这些技术以正确的方式组合来解决一个新问题。这在方法论论文中是可接受的，但可能被部分审稿人视为"组合式创新"（compositional innovation）。与 Persson et al. (2026) 和 Boileau et al. (2025) 的区分是清晰的。bias bound（误分类异质性 × CATE 异质性乘积）作为独立诊断工具有附加价值。

  3. 实验设计: 【强】 — 这是该 proposal 最突出的亮点之一。DGP 矩阵设计全面，系统性变化误分类-CATE 相关方向（正/负）是关键实验设计决策。6 种对比方法覆盖了所有合理 baseline（uncorrected, global, arm-specific, SIMEX, calibration-only, EC-HTE full）。评估指标全面（PEHE, subgroup CATE bias, CI coverage, CI width, GATE RMSE, bound tightness）。消融研究按阶段分层，覆盖每个设计选择。多 LLM 验证（GPT-4.1, Qwen 3.5, Llama 3.3）增强了泛化性。200+ 次重复保证统计显著性。预算曲线和先验敏感性分析是良好的实验实践。唯一不足：真实数据验证（Ashwin et al.）由于缺乏自然因果结构，只能验证前提（差异性误分类存在）而非完整评估 CATE 校正效果。

  4. 可行性: 【强】 — 不需要训练大模型，仅需 LLM API 调用（标注）和标准统计计算。层次贝叶斯用 VI 拟合，计算成本低。因果森林有成熟实现（R `grf` 包）。Ashwin et al. 数据集公开可用。主要计算瓶颈是仿真规模（~14 配置 × 200 重复 × 多样本量/预算/方法/LLM），但这是可并行化的标准仿真工作，单 GPU 集群数天可完成。无需构建新 benchmark。人工标注方面，使用已有专家标签数据集，无需新增标注。预估总周期 3-5 个月。

  5. 写作与呈现: 【强】 — 结构清晰，问题-动机-方法-实验逻辑连贯。反直觉发现作为 hook 的叙事策略有效。与相关工作的差异化讨论非常详尽（5 条线索），每条区分均有具体论据。限制声明诚实（仅限分类效应修饰符）。"为什么不直接用专家标签"这一自然反对意见的预先回应很好。唯一建议：方法描述可能对纯 NLP 审稿人偏技术，需要更多直觉解释。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
该 proposal 在问题识别、实验设计、可行性和写作上均为"强"级别，在方法创新上为"中偏强"。它填补了一个真实且有实证支撑的研究空白，实验设计异常完备。主要不确定性来自两点：(1) EMNLP 审稿人对纯方法论/因果推断论文的接受度——虽然 Audinet de Pieuchon et al. (EMNLP 2025) 证明此类论文可被接受，但该 proposal 的因果推断成分更重，可能被部分审稿人认为更适合统计学期刊；(2) 技术新颖性是组合式的，核心贡献在问题识别而非算法创新，这在方法论论文中是可接受的，但审稿人对此的容忍度因人而异。综合来看，这是一篇扎实的投稿，在适配的审稿人组合下有较好的接受概率，但也可能因"NLP 新颖性不足"或"更适合 causal inference venue"被拒。中位估计 35% 反映了"solid but not guaranteed"的整体判断。

【主要风险】:
1. **技术新颖性被质疑为"组合式"（compositional）**：审稿人可能认为层次贝叶斯 + 因果森林 + 自适应分配的组合虽然正确但缺乏技术深度，核心贡献更像是一个"observation paper"而非"method paper"。缓解策略：强调 bias bound 的理论贡献和诊断准则的独立价值。
2. **真实数据验证有限**：Ashwin et al. 数据集只能验证差异性误分类的存在，无法评估 CATE 校正效果。CATE 评估完全依赖半合成实验。审稿人可能要求至少一个有自然因果结构的真实数据应用。缓解策略：寻找有自然实验结构的 CSS 数据集（如政策干预 + LLM 标注的文本变量），或更明确地论证为什么半合成评估在此场景下是充分的（ground-truth CATE 只有在合成设置中才可知）。

【实施评估】:
  - 计算资源: 中等。主要是 LLM API 调用费用（3 个 LLM × 多配置 × 多样本量，估计 $500-2000 API 费用）和标准 CPU/GPU 仿真计算。无需大规模 GPU 训练。
  - 数据需求: 低。使用公开政治科学文本语料（如 immigration framing 数据集）作为半合成基础，Ashwin et al. (2025) Rohingya 数据集公开可用。
  - 人工介入: 低。不需要新的人工标注——使用已有专家标签数据集，仿真中的"专家标签"由 DGP 生成。
  - 训练需求: 无大模型训练。仅需层次贝叶斯 VI 拟合（秒级）和因果森林训练（分钟级）。
  - 新 Benchmark: 否。使用已有数据集 + 半合成 DGP。
  - 预估周期: 3-5 个月（理论推导 1 月 + 代码实现 1 月 + 实验运行 1-2 月 + 写作 1 月）。
```

Sources:
- [Audinet de Pieuchon et al., "Benchmarking Debiasing Methods for LLM-based Parameter Estimates" (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)
- [Mozer, "PPI is the Difference Estimator" (arXiv 2026)](https://arxiv.org/abs/2603.19160)
- [Fisch et al., StratPPI (NeurIPS 2024)](https://arxiv.org/abs/2406.04291)
- [Sui et al., PPCI (arXiv 2026)](https://arxiv.org/abs/2603.05575)
- [Persson et al., "Detecting and Mitigating Group Bias in HTE" (arXiv 2026)](https://arxiv.org/abs/2602.20383)
- [Boileau et al., "Assumption-Lean Differential Variance Inference" (arXiv 2025)](https://arxiv.org/abs/2512.03254)
- [Ashwin et al., "Using LLMs for Qualitative Analysis can Introduce Serious Bias" (Sociological Methods & Research 2025)](https://journals.sagepub.com/doi/10.1177/00491241251338246)
- [Messing, "Hidden Measurement Error in LLM Pipelines" (arXiv 2026)](https://arxiv.org/abs/2604.11581)
- [Jerzak et al., SRI Framework (arXiv 2025)](https://arxiv.org/abs/2509.12416)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a comprehensive evaluation. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:

- Audinet de Pieuchon et al. (EMNLP 2025): "Benchmarking Debiasing Methods for LLM-based Parameter Estimates" — 直接对比 DSL 和 PPI 在 LLM 标注去偏上的表现，发现 DSL 在中等专家标注量下通常误差最低。该工作锁定在 ATE 级别的总体参数估计，未涉及 CATE/HTE。EC-HTE 的核心主张——这些方法无法处理子群级别的 CATE 纠偏——与本文互补且不冲突。

- Fisch et al. (NeurIPS 2024): "Stratified Prediction-Powered Inference (StratPPI)" — 通过数据分层改进 PPI，在自动评分器表现因条件分布不同而异质时显著收紧置信区间。但仍以总体参数为目标估计量，不处理 effect modifier 被误分类导致的 CATE 扭曲。EC-HTE 的分层思想与 StratPPI 有相似之处（都利用子群结构），但估计目标完全不同。

- Mozer (arXiv:2603.19160): "PPI is the Difference Estimator" — 揭示 PPI 核心估计量等价于经典调查抽样的差异估计量。该论文的 arm-specific rectifier 处理 ATE 偏差，EC-HTE proposal 正确指出其代数上无法纠正子群级别的 CATE 扭曲。

- Messing (arXiv:2604.11581): "Hidden Measurement Error in LLM Pipelines" — 文档记录 LLM pipeline 中隐藏测量误差导致 naive CI 覆盖不足 40-60%。仅限于汇总层面分析，未延伸到因果 HTE 纠偏。EC-HTE 引用此文作为问题紧迫性的证据，引用恰当。

- Ashwin, Chhabra & Rao (Sociological Methods & Research, 2025): "Using LLMs for Qualitative Analysis can Introduce Serious Bias" — 在罗兴亚难民访谈转录上提供直接实证，LLM 编码错误与受访者难民身份、性别、教育水平系统性相关。这是 EC-HTE 问题动机的核心实证基础。

- Sui et al. (arXiv:2603.05575): "Prediction-Powered Conditional Inference (PPCI)" — 将 PPI 扩展到固定测试点的条件函数推断。关键区别：PPCI 处理结果预测噪声，但假定条件变量（即 effect modifier）是正确的。EC-HTE proposal 准确指出当条件变量本身被误分类时，PPCI 的 kernel localization 无法帮助。

- Persson et al. (arXiv:2602.20383): "Detecting and Mitigating Group Bias in HTE" — 发现即使 CATE 模型正确指定，CATE→GATE 的聚合也不能恢复真正的 GATE，提出收缩纠偏。但偏差来源是聚合过程而非测量误差，且假定协变量干净。EC-HTE 处理不同来源的偏差（effect modifier 误分类），二者互补。

- Boileau et al. (arXiv:2512.03254): "Assumption-Lean Differential Variance Inference for HTE Detection" — 当 effect modifier 被遗漏或严重测量误差时，通过潜在结果方差对比检测异质性是否存在。关键区别：这是假设检验（异质性是否存在），不是 CATE 估计。EC-HTE 做的是 CATE 纠偏估计，二者互补。

- Jerzak et al. (arXiv:2509.12416): "Surrogate Representation Inference (SRI)" — 在噪声标注下提供有效推断，但不处理 effect modifier 误分类对 HTE 的影响。

- AM-PPI (arXiv:2605.08429): "Active Multiple-Prediction-Powered Inference" — 多预测器自适应路由 + 预算优化，CI 收窄 10-40%。仍锁定在总体参数估计。

- 调研总结: LLM 标注去偏领域极度活跃（2024-2026 年涌现大量工作），但现有方法几乎全部锁定在 ATE/总体参数级别。CATE 估计中 effect modifier 被 LLM 误分类的问题确实是一个未被占据的交叉空白。EC-HTE 的 novelty claim——no existing method corrects for subgroup-specific misclassification in effect modifiers for CATE——经调研验证成立。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇 well-motivated、well-scoped 的方法论工作，识别了一个真实且被忽视的技术空白。问题界定清晰，相关工作梳理异常全面（7 篇 2025-2026 新工作的精确定位和差异化分析），实验设计非常完备。我的倾向是 weak accept / borderline accept。

主要犹豫点：(1) 方法论层面的创新深度——三阶段框架本质上是已有工具的组合（hierarchical Bayesian confusion matrix + honest causal forest + sandwich variance + adaptive allocation），每一步都不是新方法，新颖性主要在于问题识别和组合；(2) "global correction can worsen CATE" 的 anti-intuitive claim 对测量误差/流行病学专家而言可能不够 surprising（differential misclassification 是经典概念）；(3) 验证主要是 semi-synthetic，real-data 部分只能验证前提假设而非完整框架。

【核心贡献】:
1. **问题识别与形式化**: 首次明确界定 LLM 标注 effect modifier 误分类导致的 CATE 扭曲问题，并证明全局纠偏在正相关情况下可能恶化估计。这是最有价值的贡献。
2. **可操作的诊断标准**: misclassification heterogeneity × CATE heterogeneity 的乘积作为事前诊断，独立于 EC-HTE 框架有单独价值。
3. **三阶段纠偏框架**: 实用但方法论新颖性有限。
4. **全面的实证验证设计**: 实验方案本身的完备性是一个显著优点。

这些贡献对领域有中等偏上价值。问题识别和诊断标准对日益增长的 "LLM-as-annotator for causal inference" 社区有实际指导意义。但核心方法论（hierarchical Bayesian + causal forest + sandwich）都是成熟工具的组合，不是方法论突破。

【方法合理性】:
方法整体合理。具体评价：
- **Stage 1 (Hierarchical Bayesian confusion matrix)**: 合理选择，partial pooling 在小样本子群和全局估计之间取得平衡。VI 作为主要拟合方法、MCMC 作为验证是实际的决定。
- **Stage 2 (Sandwich variance)**: 将 Stage 1 的 nuisance parameter 不确定性传播到 CATE CI 中是正确做法。Bootstrap 作为稳健性检查也合理。
- **Stage 3 (Adaptive allocation)**: 联合最小化 misclassification 不确定性和 CATE 方差的分配标准是自然的设计。Cold-start protocol 务实。

**替代方案考量**: 一个更简单的替代是直接用 StratPPI 类方法在子群级别独立做 PPI 纠偏（即每个子群独立估计一个 PPI rectifier 然后独立做 CATE）——proposal 应该讨论为什么这不够（可能因为子群样本量太小导致方差爆炸，partial pooling 是关键优势）。另一个替代是 SIMEX（已被列为 baseline，这是好的）。总体来说没有更简单的替代方案能完整覆盖所有三个阶段的功能。

【5 维度打分】:

  1. 研究问题: 【强】— LLM-as-annotator pipeline 已成为 CSS 的默认做法（Audinet de Pieuchon et al., EMNLP 2025 确认），但现有去偏方法全部锁定在 ATE 级别。随着研究者越来越多地将 LLM 标注用于子群分析和效应修饰（heterogeneity analysis），效应修饰变量本身被误分类的问题具有真实且不断增长的实际影响。Ashwin et al. (2025) 提供了直接实证。问题的时效性和实用价值都很高。

  2. 方法与创新: 【中】— Novelty 主要在问题识别层面而非方法论层面。三阶段框架的每一步（hierarchical Bayesian estimation: 经典方法; honest causal forest: Wager & Athey 2018; sandwich variance: 标准技术; adaptive allocation: 常见优化策略）都是成熟工具。创新在于将它们组合起来解决一个新问题，并推导出诊断标准（bias bound）。与 PPCI (Sui et al., 2026) 的区分清晰且有说服力——PPCI 假定条件变量正确，EC-HTE 处理条件变量本身错误的情况。与 Persson et al. (2026) 的区分也清晰——偏差来源不同。但"global correction worsens estimates"在测量误差文献中并不 novel（differential misclassification 是 epidemiology 的基础概念，Rothman, Greenland & Lash 的教科书已有详细讨论）。

  3. 实验设计: 【强】— 实验方案非常全面且设计严谨：(a) DGP matrix 覆盖关键因素的 worst/best case 组合，特别包含 misclassification-CATE correlation direction 这一关键变量；(b) 6 种对比方法（uncorrected, global, arm-specific, SIMEX, calibration-only, EC-HTE full）覆盖了所有合理 baseline；(c) 4 层 ablation（partial pooling, variance adjustment, allocation strategy, pilot ratio）各有明确假设验证目标；(d) 评估指标全面（PEHE, subgroup bias, CI coverage, CI width, GATE RMSE, bound tightness）；(e) 200+ replications per configuration 保证统计功效；(f) 3 个 LLM annotator 覆盖不同家族。与 "Really Doing Great at Estimating CATE?" (NeurIPS D&B 2021) 建立的 CATE 评估标准基本一致。Real-data validation 的局限性（只能验证前提，不能验证完整框架）被诚实声明，semi-synthetic 实验承担主要验证责任——这是合理的设计。唯一遗憾：没有真正有自然因果结构的 real-world end-to-end validation。

  4. 可行性: 【强】— (a) 计算需求适中：hierarchical Bayesian VI 在小规模数据上很快，honest causal forest 有成熟实现（grf R package），semi-synthetic 实验可在单 GPU/CPU 集群上完成；(b) 数据需求合理：semi-synthetic 用公开政治文本语料，real-data 用 Ashwin et al. 的 Rohingya 语料（已发表）；(c) 无需训练新模型（用现成 LLM API 做标注）；(d) 专家标注预算 B ∈ {100-2000} 是现实范围；(e) 方法实现不涉及复杂的新架构。唯一风险点：12-14 个 DGP 配置 × 200 replications × 多种 N × 多种 B × 3 个 LLM = 实验量较大，但通过 VI（而非 MCMC）和并行化可管理。预估 2-3 个月完成所有实验。

  5. 写作与呈现: 【强】— Proposal 的写作质量很高：(a) 问题动机层层递进——从一般性观察到反直觉发现到数学界定；(b) 相关工作梳理按 5 个 thread 组织，每个 thread 都精确定位差异，特别是对 PPCI vs. EC-HTE 的区分（conditioning variable noise vs. conditioning variable misclassification）非常清晰；(c) 方法描述条理分明，三阶段各有清晰的技术内容；(d) 实验设计的 DGP matrix 和 ablation 结构一目了然；(e) 限制和范围声明诚实（categorical effect modifiers only, semi-synthetic validation）。一个小改进建议：可以在引言中更早地给出一个具体的量化例子（如 proposal 中的 two-subgroup example）来 hook 读者。

【概率估计】: [30% - 42%] 中位 36%

【估计理由】:
上行因素：(1) 研究问题真实且时效性强，LLM-as-annotator for causal inference 是 2024-2026 最活跃的交叉方向之一；(2) Novelty claim 经调研验证成立——ATE→CATE 的去偏空白确实存在；(3) 实验设计异常完备，如果实验结果如预期，论文的实证部分将非常扎实；(4) 相关工作梳理全面，positioning 精确；(5) 诊断标准有独立实用价值。

下行因素：(1) 方法论新颖性有限——本质是 well-known 工具的组合（hierarchical Bayes + causal forest + sandwich variance），缺乏深层方法论创新，审稿人可能认为 "incremental"；(2) "differential misclassification biases subgroup estimates" 的核心洞察在测量误差/epidemiology 文献中是经典知识，在 NLP 社区可能 novel 但在统计社区可能被视为 straightforward application；(3) 无 end-to-end real-world CATE validation——real data 只能验证前提（misclassification is differential），不能验证核心主张（EC-HTE improves CATE estimation in practice）；(4) EMNLP reviewer pool 的方法论背景差异较大——如果遇到 causal inference 背景强的审稿人，可能认为 novelty 不足；如果遇到 NLP 背景为主的审稿人，可能觉得 causal inference 技术细节难以评判；(5) 论文的核心受众（做 causal HTE 的 CSS 研究者）在 EMNLP 审稿人中占比可能不高。

综合判断：这是一篇扎实的 borderline paper。问题真实、方法合理、实验设计出色，但方法论创新深度不足以进入 "clearly above threshold"。如果实验结果清晰地展示 EC-HTE 的优势（特别是 global correction worsens 的 demonstration），且写作保持 proposal 的高质量，有合理的中稿机会。中位估计 36% 反映了一篇 "solid but not exciting" 的 borderline submission 在 EMNLP 的典型命运。

【主要风险】:
1. **方法论创新深度不足**: 审稿人可能认为三阶段框架只是已有工具的 straightforward 组合，核心洞察（differential misclassification distorts subgroup estimates）在统计文献中不够 novel，leading to "incremental contribution" 的评判。
2. **缺乏 end-to-end real-world validation**: Semi-synthetic 验证虽然设计精良，但审稿人可能质疑 DGP 的外部效度（"your synthetic setup guarantees the problem exists; show me it matters in the real world"）。Ashwin 数据只能验证前提，不能验证完整 pipeline 的 CATE 改善。

【实施评估】:
  - 计算资源: 中等。VI fitting + causal forest + 大规模 simulation 需要多核 CPU 集群，单个 DGP 配置的 200 次 replication 可能需要数小时。LLM annotation 需要 API 调用（GPT-4.1, Qwen 3.5, Llama 3.3），API 成本约 $500-2000（取决于数据规模）。无需 GPU 训练。
  - 数据需求: 低-中等。Semi-synthetic 使用公开政治文本语料（immigration framing / partisan tweets），Ashwin et al. Rohingya 数据集已发表。不需要新数据收集。
  - 人工介入: 低。不需要新的人工标注（使用 Ashwin 数据的已有专家标注）。Semi-synthetic 中的"专家标注"由 DGP 生成。
  - 训练需求: 无模型训练。使用现成 LLM API 做标注，使用 grf 等现有 CATE 估计包。Hierarchical Bayesian model fitting 不算"训练"。
  - 新 Benchmark: 否。Semi-synthetic DGP matrix 是验证框架而非 benchmark。但 DGP matrix + 评估 protocol 本身可以作为后续工作的 benchmark 基础。
  - 预估周期: 2.5-4 个月。方法实现 2-3 周；semi-synthetic 实验 4-6 周（大规模 simulation）；real-data validation 1-2 周；论文写作 3-4 周。可并行化。
```

---

Sources:
- [Benchmarking Debiasing Methods for LLM-based Parameter Estimates (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)
- [Stratified Prediction-Powered Inference (NeurIPS 2024)](https://arxiv.org/abs/2406.04291)
- [PPI is the Difference Estimator (Mozer, 2025)](https://arxiv.org/html/2603.19160)
- [Hidden Measurement Error in LLM Pipelines (Messing, 2026)](https://arxiv.org/abs/2604.11581)
- [Using LLMs for Qualitative Analysis can Introduce Serious Bias (Ashwin et al., 2025)](https://journals.sagepub.com/doi/10.1177/00491241251338246)
- [Prediction-Powered Conditional Inference (Sui et al., 2026)](https://arxiv.org/abs/2603.05575)
- [Detecting and Mitigating Group Bias in HTE (Persson et al., 2026)](https://arxiv.org/abs/2602.20383)
- [Assumption-Lean Differential Variance Inference for HTE Detection (Boileau et al., 2025)](https://arxiv.org/abs/2512.03254)
- [Surrogate Representation Inference (Jerzak et al., 2025)](https://arxiv.org/abs/2509.12416)
- [Active Multiple-Prediction-Powered Inference (AM-PPI, 2026)](https://arxiv.org/abs/2605.08429)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient field research to provide an informed evaluation. Let me compile the full assessment.

---

```
【阶段】: Triage

【领域调研】:

- [Audinet de Pieuchon et al., "Benchmarking Debiasing Methods for LLM-based Parameter Estimates"](https://aclanthology.org/2025.emnlp-main.1000/) (EMNLP 2025): 直接上游工作。系统比较 DSL、PPI 等去偏方法用于 LLM 标注的参数估计。但所有方法限于 population-level estimands (ATE/回归系数)，不涉及 CATE/HTE。验证了 EC-HTE 所声称的"现有方法只解决 ATE 层面问题"这一前提。重要的是，此论文被 EMNLP 2025 接收，说明 EMNLP 审稿人对该方向有接受度。

- [Fisch et al., "Stratified Prediction-Powered Inference for Hybrid Language Model Evaluation"](https://arxiv.org/abs/2406.04291) (NeurIPS 2024): StratPPI 通过分层采样改进 PPI 的置信区间宽度。虽引入了 subgroup 概念，但目标仍是全局参数的更紧估计，不是 subgroup-specific 因果效应。EC-HTE 的问题设定（校正 effect modifier 中的差异化误分类）与 StratPPI 结构性不同。

- [Ashwin et al., "Using Large Language Models for Qualitative Analysis can Introduce Serious Bias"](https://arxiv.org/abs/2309.17147) (Sociological Methods & Research 2025): 直接实证支撑。在 Rohingya 难民访谈数据上证明 LLM 编码错误与受访者的难民身份、性别、教育水平系统性相关。这恰好是 EC-HTE 所针对的"误分类率与 subgroup 协变"前提的经验证据。Proposal 选择此数据集做 real-data validation 非常合理。

- [Messing, "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking"](https://arxiv.org/abs/2604.11581) (arXiv 2025): 文档化 LLM 管线中隐藏测量误差导致 naive 置信区间 under-cover 40–60%。但分析停留在 aggregate level，未延伸到因果 HTE。EC-HTE 填补了从 aggregate 到 subgroup-level 因果推断的空白。

- [Sui et al., "Prediction-Powered Conditional Inference"](https://arxiv.org/abs/2603.05575) (arXiv 2026): PPCI 将 PPI 扩展到条件泛函（给定固定 test point 的条件均值等），使用 kernel localization。关键区别：PPCI 假设 conditioning variable 是正确的，处理的是 outcome prediction noise；EC-HTE 处理的是 conditioning variable 本身（effect modifier）被误分类的情况。Proposal 对此区别的阐述是准确的。

- [Persson et al., "Detecting and Mitigating Group Bias in Heterogeneous Treatment Effects"](https://arxiv.org/abs/2602.20383) (arXiv 2026): 处理 CATE→GATE 聚合产生的偏差，用 shrinkage 校正。但假设 covariates 是干净的——bias 来源是聚合过程而非测量误差。EC-HTE 处理的是更上游的问题：effect modifier 本身就被错标了。

- [Boileau et al., "Assumption-Lean Differential Variance Inference for Heterogeneous Treatment Effect Detection"](https://arxiv.org/abs/2512.03254) (arXiv 2025): 在 effect modifier 缺失或严重测量误差下，通过 potential outcomes 方差对比进行 HTE 检测。但目标是假设检验（"是否存在异质性"），而非 CATE 估计。与 EC-HTE 互补而非竞争。

- 调研总结: 该领域存在一个清晰且真实的空白——现有 LLM 标注去偏方法全部锁定在 ATE/population-level，而 CATE/HTE 估计中 effect modifier 误分类导致的偏差尚无人系统处理。EC-HTE 精准定位在 Thread 1 (LLM debiasing) 与 Thread 2 (HTE estimation) 的交叉点，novelty claim 成立。

【整体印象】:
作为审稿人，我的第一反应是"这是一篇 well-crafted、有理论深度的 proposal，解决了一个真实且尚未被解决的问题"。问题识别犀利——"全局校正不仅不够，还可能恶化 CATE 估计"这个 anti-intuitive finding 非常有力。Related work 的五线程梳理展现了对领域全景的深刻理解，且每一条 differentiation 经我调研验证均准确。实验设计全面、系统。总体倾向 weak accept 至 borderline accept。

主要保留意见：(1) 主题位于因果推断与 NLP 的深度交叉区，对纯 NLP 审稿人可能显得过于统计学化；(2) 三阶段框架的复杂度可能被质疑——是否有更简单的替代方案；(3) Real-data evaluation 仅验证前提（差异化误分类存在），未完成端到端 CATE 校正验证。

【核心贡献】:
核心贡献有三层：
1. **问题形式化**：首次识别并形式化"LLM 标注误分类在 effect modifier 中的差异化导致 CATE distortion"这一新偏差类别，并证明全局校正可恶化估计——这具有独立的理论价值。
2. **可操作诊断准则**：误分类异质性 × CATE 异质性的有限样本 bound，任何研究者在做 CATE 分析前可直接计算，判断是否需要 stratified correction。这个诊断的 standalone value 很高。
3. **三阶段校正框架**：从 hierarchical Bayesian 误分类估计到 sandwich variance 调整再到自适应标注分配，提供了完整的解决方案。

对领域的价值：中高。随着 LLM-as-annotator 在 CSS 中的普及，从 ATE debiasing 扩展到 CATE debiasing 是自然且重要的下一步。诊断准则尤其有实用价值。

【方法合理性】:
方法整体合理，各组件有充分的统计学基础：
- **Stage 1** (Hierarchical Bayesian partial pooling): 在"全局单一混淆矩阵 vs. 每个 subgroup 独立估计"之间取折中，是处理小样本 subgroup 的标准做法，合理。
- **Stage 2** (Sandwich variance): 传统的 two-stage estimation 不确定性传播方法，成熟可靠。
- **Stage 3** (Adaptive allocation): 基于 bias bound 的分配策略逻辑自洽——将标注预算分配给"误分类不确定性 × CATE magnitude"最大的 subgroup。

**更简单的替代方案？** 一个自然的简化方案是跳过 hierarchical Bayesian，直接对每个 subgroup 独立估计混淆矩阵然后 plug-in。Proposal 在 ablation 中覆盖了这个对比 (Stage 1 ablation: no pooling vs. partial pooling vs. full pooling)，这是正确的做法。如果 ablation 显示 partial pooling 的增益有限，审稿人可能质疑 Stage 1 的复杂度。但这不是致命问题——empirical result 会给出答案。

另一个替代方案：直接用 PPCI (Sui et al.) 的 kernel localization 方法，将 effect modifier 的 soft probability 作为 continuous conditioning variable。但正如 proposal 所指出的，PPCI 假设 conditioning variable 正确，categorical misclassification 不是 continuous noise，kernel localization 在此无效。Proposal 对此的论述是准确的。

【5 维度打分】:

1. 研究问题: 【强】— 问题真实、重要且尚未解决。经调研验证，现有方法（DSL、PPI、StratPPI、PPCI）均不解决 CATE 层面的 effect modifier 误分类问题。Ashwin et al. (2025) 提供了差异化误分类的直接经验证据，证实这不是人造问题。"全局校正可恶化 CATE"的理论发现更增加了问题的紧迫性。唯一的弱点是：做 CATE 分析且使用 LLM 标注作为 effect modifier 的研究者群体，虽在增长，目前可能仍是一个相对小的 niche。

2. 方法与创新: 【中偏强】— Novelty claim 经调研验证成立：无直接竞争工作。与 PPCI (conditioning variable noise vs. conditioning variable misclassification)、Persson (aggregation bias vs. measurement error)、Boileau (detection vs. estimation) 的区别清晰且准确。方法本身是对已有组件（hierarchical Bayesian、sandwich variance、adaptive allocation）的合理组装，单个组件的新颖性有限，但组装方式和问题-方法的匹配是新的。创新更多来自 problem identification + theoretical insight (bias bound) 而非 method design。

3. 实验设计: 【强】— 这是 proposal 的一大亮点。DGP matrix 覆盖了关键因素（误分类严重度、CATE 异质性、subgroup 数、误分类-CATE 相关方向），尤其是包含正/负相关方向来验证理论预测。Comparison methods 涵盖 6 种基线（uncorrected、global、arm-specific、SIMEX、calibration-only、EC-HTE），非常充分。评价指标（PEHE、subgroup bias、CI coverage、CI width、GATE RMSE、bound tightness）覆盖了 accuracy 和 inference validity 两个维度。Ablation 设计系统（3 个 stage 各自 ablation + diagnostic validation + CATE estimator robustness check）。200+ replications per configuration 是足够的。预算曲线 (B ∈ {100, 500, 1000, 2000}) 可展示方法的 practical operating range。依据 NeurIPS D&B 2021 ("Really Doing Great at Estimating CATE?") 的评估标准，该实验设计达到了 CATE 文献的严谨要求。

4. 可行性: 【中偏强】— 方案可执行。Semi-synthetic experiments 不需要海量计算（hierarchical Bayesian with VI + causal forest，标准硬件即可）。LLM 标注成本通过使用 API (GPT-4.1) 和开源模型 (Qwen 3.5, Llama 3.3) 可控。Ashwin et al. 数据集已公开。主要风险：(a) 200+ replications × 12-14 configurations × 多种 N 和 B 组合 = 大量实验运行，需要良好的实验管理；(b) hierarchical Bayesian + MCMC validation in appendix 需要一些统计学实现功力。但总体上是一个两人团队在 3-4 个月内可完成的项目。

5. 写作与呈现: 【强】— Proposal 本身的写作质量很高。问题动机以 anti-intuitive finding 开篇，有说服力。五线程 related work 结构清晰，differentiation 精准。方法描述逻辑流畅（三阶段 + cold-start protocol）。Scope 和 limitations 坦诚（仅处理 categorical modifier）。实验设计的呈现有条理。如果正式论文保持这一写作水平，对审稿人来说是一个 pleasant reading experience。

【概率估计】: [32% - 43%] 中位 37%

【估计理由】:
- **上推因素**: (1) 问题真实、novelty claim 经验证成立，填补 ATE→CATE debiasing 的真实空白；(2) 理论贡献（bias bound + "全局校正可恶化"的证明）有独立价值且 anti-intuitive；(3) 实验设计非常完备，达到因果推断文献的严谨标准；(4) Audinet de Pieuchon et al. 在 EMNLP 2025 被接收，证明该方向在 EMNLP 有 reviewer base；(5) 写作质量高。
- **下拉因素**: (1) 主题深度交叉（因果推断 + 测量误差 + NLP），可能遇到不熟悉因果 HTE 方法论的审稿人，导致 appreciation gap；(2) 方法是已有组件的合理组装（hierarchical Bayesian + sandwich + adaptive allocation），方法层面的 novelty 有限，创新更多在 problem identification 和 theory；(3) Real-data validation 仅验证前提而非端到端 CATE 校正效果，审稿人可能要求更有说服力的真实应用；(4) 实际受益人群（做 LLM-annotated CATE 分析的研究者）目前可能偏小众，impact 论证需要更有说服力；(5) 三阶段框架的复杂度可能被质疑，尤其如果 ablation 显示简化版本效果接近。
- 综合判断：这是一篇 solid 且有实质贡献的 proposal，质量在 EMNLP 接收线附近。以当前方案执行到位的话，属于 borderline accept，最终结果很大程度取决于审稿人匹配和实验结果的强度。

【主要风险】:
1. **审稿人匹配风险**: EMNLP 审稿人池中同时精通因果推断 (HTE/CATE) 和 NLP annotation debiasing 的审稿人比例有限。如果匹配到纯 NLP 背景的审稿人，可能对 hierarchical Bayesian confusion matrix estimation 和 sandwich variance 的贡献缺乏 appreciation，给出"方法过于统计学化、不够 NLP"的评价。
2. **Real-data validation 不完整**: 最有说服力的证据应该是在一个具有真实因果结构的数据集上展示端到端的 CATE 校正效果，但当前方案的 Ashwin et al. 数据仅用于验证差异化误分类的前提。审稿人可能要求"show me it works on a real causal problem"——而半合成实验虽然设计严谨，说服力天然弱于真实应用。

【实施评估】:
  - 计算资源: 中等。Hierarchical Bayesian (VI) + Causal Forest 不需要 GPU 训练，标准 CPU 集群即可。200+ replications × ~14 configurations × 多种 N/B 组合需要 batch 运行管理，但单次运行耗时不长。LLM 标注使用 API 调用，成本取决于 corpus 规模（GPT-4.1 API 费用需纳入预算）。
  - 数据需求: 中等。需要一个有真实语言变异的政治学文本语料（如移民框架数据或党派推文数据集，此类公开数据集较多）。Ashwin et al. (2025) 的 Rohingya 访谈数据集需获取（已发表论文的数据，通常可获得）。
  - 人工介入: 不需要新的人工标注。Expert labels 在 semi-synthetic 实验中是模拟的（DGP 控制），real-data 部分使用 Ashwin et al. 已有的人工标注。
  - 训练需求: 不涉及 LLM 训练或微调。仅使用现成 LLM 做 zero-shot/few-shot 标注。Hierarchical Bayesian 模型和 Causal Forest 是传统统计/ML 模型，无需 GPU 训练。
  - 新 Benchmark: 不需要构建新 benchmark。Semi-synthetic DGP 和 Ashwin et al. 数据即为评估基础。DGP 设计本身可作为社区可复用的 benchmark suite（加分项）。
  - 预估周期: 3-4 个月（1 个月：理论推导 + 方法实现；1-1.5 个月：semi-synthetic 实验；0.5-1 个月：real-data validation + 写作）。适合 2 人团队，需具备因果推断和 Bayesian 建模经验。
```

Sources:
- [Benchmarking Debiasing Methods for LLM-based Parameter Estimates (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)
- [Stratified Prediction-Powered Inference (NeurIPS 2024)](https://arxiv.org/abs/2406.04291)
- [Ashwin et al., LLM Qualitative Analysis Bias (SMR 2025)](https://arxiv.org/abs/2309.17147)
- [Messing, Hidden Measurement Error in LLM Pipelines (arXiv 2025)](https://arxiv.org/abs/2604.11581)
- [Sui et al., Prediction-Powered Conditional Inference (arXiv 2026)](https://arxiv.org/abs/2603.05575)
- [Persson et al., Detecting and Mitigating Group Bias in HTE (arXiv 2026)](https://arxiv.org/abs/2602.20383)
- [Boileau et al., Assumption-Lean Differential Variance Inference for HTE Detection (arXiv 2025)](https://arxiv.org/abs/2512.03254)


【原始 proposal（允许参考但不是主要依据）】:
## EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation Under LLM Annotation Misclassification

## Problem and Motivation

When NLP researchers use LLM-generated annotations as effect modifiers in causal heterogeneous treatment effect (HTE) analysis, a previously unrecognized structural bias arises: LLM misclassification rates covary with the true conditional average treatment effect (CATE). Subgroups where LLMs err most in annotation (e.g., marginalized populations, linguistically complex cases) are often the same subgroups where treatment effects are largest. This creates a confounding between measurement error and causal heterogeneity that cannot be resolved by any global correction method—including arm-specific rectifiers (Mozer, arXiv:2603.19160), which address average treatment effect (ATE) bias but are algebraically incapable of correcting subgroup-level CATE distortions.

This problem is urgent. LLM-as-annotator has become the default pipeline for computational social science (Audinet de Pieuchon et al., EMNLP 2025, benchmarking DSL vs. PPI debiasing; StratPPI, Fisch et al., NeurIPS 2024, improving PPI via stratification), and researchers increasingly use LLM annotations not just for ATE estimation (where DSL and PPI provide corrections) but for subgroup analysis and effect modification—yet no correction method exists for this latter use case. Messing (arXiv:2604.11581) documents that hidden measurement error in LLM pipelines causes naive confidence intervals to under-cover by 40–60%, but this analysis remains at the aggregate level. Ashwin et al. (Sociological Methods & Research, 2025) provide direct empirical evidence that LLM coding errors in refugee interview transcripts correlate systematically with respondents' refugee status, gender, and education level—precisely the variables used as effect modifiers in downstream causal analysis. Any study using LLM-annotated text variables as moderators produces unreliable heterogeneity findings whenever annotation error rates differ across subgroups—and Ashwin et al. show this is the norm, not the exception.

**Key anti-intuitive finding: global correction can actively worsen CATE estimates.** Consider a two-subgroup example. Subgroup A has high misclassification (25%) and large CATE (0.5 SD); Subgroup B has low misclassification (5%) and small CATE (0.1 SD). A global correction uses a pooled confusion matrix (~15% error), which under-corrects Subgroup A and over-corrects Subgroup B. The net effect: globally-corrected CATE estimates can have *larger* bias than uncorrected estimates. This is not an edge case—it occurs whenever the misclassification pattern and CATE structure are positively correlated, which empirical evidence suggests is common in practice.

## Core Contributions

This paper makes four contributions:

1. **Problem identification and formalization.** We identify and formalize measurement-error-induced CATE distortion—a new class of bias arising when LLM annotation errors in effect modifiers are differential across subgroups and correlated with the true heterogeneity structure. We show this is structurally distinct from: ATE-level debiasing (Mozer, arXiv:2603.19160; Egami et al., NeurIPS 2023 DSL; Zrnic & Candès, ICML 2024), CATE-to-GATE aggregation bias (Persson et al., arXiv:2602.20383, where bias originates from aggregation, not measurement error), and conditional inference with outcome prediction noise (Sui et al., arXiv:2603.05575 PPCI, which assumes the conditioning variable is correct). We prove that global correction can *increase* CATE bias relative to uncorrected estimates when misclassification and CATE heterogeneity are positively correlated.

2. **Actionable diagnostic criterion (Bias Bound).** We derive a finite-sample bound: the bias of globally-corrected CATE estimates is proportional to the product of (a) misclassification heterogeneity across subgroups and (b) CATE heterogeneity across subgroups. This product yields a practical diagnostic: given pilot data, any researcher can compute this quantity *before* running full CATE analysis to determine whether global correction suffices or stratified correction is necessary. This diagnostic has standalone value independent of the EC-HTE framework—it applies to any CATE analysis using LLM-annotated effect modifiers. The bound implies that bias is worst when annotation is least accurate for subgroups where treatment effects are largest—empirically common (Ashwin et al., 2025).

3. **EC-HTE: A three-stage correction framework** providing subgroup-specific misclassification correction, valid confidence intervals, and optimal annotation allocation (detailed below).

4. **Empirical validation** via semi-synthetic benchmarks with controlled DGPs (including systematic variation of misclassification-CATE correlation direction) and a real-data misclassification pattern validation (Ashwin et al., 2025, Rohingya interview corpus).

## Why Not Just Use Expert Labels?

A natural objection: why not skip LLM annotation entirely and estimate CATEs using only expert-labeled data? The answer is a bias-variance tradeoff specific to CATE estimation. With a budget of ~2,000 expert labels distributed across k subgroups, each subgroup contains ~2,000/k observations. Honest causal forests (Wager & Athey, JASA 2018) split this further into estimation and splitting samples, leaving each cell with ~1,000/k observations—insufficient for detecting moderate heterogeneity when k ≥ 4.

EC-HTE resolves this by using the full unlabeled corpus (potentially hundreds of thousands of LLM-annotated observations) for low-variance CATE estimation, with expert labels only for calibrating subgroup-specific misclassification. This extends the PPI/DSL paradigm—combining noisy large-scale with clean small-scale data—from ATE to CATE, where data demands make the combination even more critical.

## Method: Three-Stage Framework

**Stage 1: Hierarchical Bayesian Subgroup-Specific Misclassification Estimation.** For each effect-modifier subgroup g ∈ {1, …, k}, we estimate a confusion matrix C_g between LLM annotation and expert gold standard using a hierarchical Bayesian model with partial pooling. The hierarchy allows low-sample subgroups to borrow strength from the global structure while permitting genuine cross-subgroup variation. This addresses a key tension: per-subgroup independent estimation (high variance when subgroup expert-label counts are small) vs. single global estimation (biased when misclassification rates genuinely differ). For computational scalability in large-scale simulation studies, we use variational inference (VI) as the primary fitting method, with MCMC validation on representative configurations in the appendix.

**Stage 2: Corrected CATE Estimation with Sandwich Variance Adjustment.** Corrected effect-modifier assignments are fed into an honest causal forest (Wager & Athey, JASA 2018). Because Stage 1 introduces nuisance parameter uncertainty, naive confidence intervals will under-cover. We derive a sandwich variance inflator propagating Stage 1 uncertainty into Stage 2 CIs, ensuring valid coverage. Bootstrap-based CIs serve as a robustness check.

**Stage 3: Adaptive Expert Annotation Allocation.** Given a fixed expert budget B, we optimize allocation across subgroups by jointly minimizing misclassification estimation uncertainty and CATE estimation variance. The allocation criterion targets subgroups where the product of misclassification uncertainty and CATE magnitude is largest—precisely where annotation errors cause the most CATE distortion (as predicted by the bias bound).

**Cold-start protocol.** Since Stage 3 requires initial estimates of both misclassification rates and CATE magnitudes, we employ a multi-batch protocol: (a) allocate 20–30% of B as a uniform pilot batch; (b) estimate initial confusion matrices and CATE values; (c) allocate remaining budget adaptively. We include pilot ratio sensitivity analysis (10%, 20%, 30%) in the experiments.

## Related Work and Differentiation

**Thread 1: LLM annotation debiasing (ATE-level).** DSL (Egami et al., NeurIPS 2023), PPI and its algebraic equivalence to survey-sampling difference estimators (Mozer, arXiv:2603.19160), active inference (Zrnic & Candès, ICML 2024), stratified PPI (StratPPI, Fisch et al., NeurIPS 2024), active multi-predictor PPI (AM-PPI, arXiv:2605.08429), and benchmarking thereof (Audinet de Pieuchon et al., EMNLP 2025). All locked to population-level estimands. Messing (arXiv:2604.11581) diagnoses hidden measurement error causing 40–60% CI under-coverage but does not extend to causal HTE correction.

**Thread 2: HTE/CATE estimation methods.** Honest causal forests (Wager & Athey, JASA 2018), DR-learner, CATE-to-GATE aggregation bias correction (Persson et al., arXiv:2602.20383, shrinkage for aggregation-induced bias assuming clean covariates), and assumption-lean HTE detection under mismeasured modifiers (Boileau et al., arXiv:2512.03254, hypothesis testing for whether heterogeneity exists, not CATE estimation—complementary to EC-HTE). CATE evaluation standards established in "Really Doing Great at Estimating CATE?" (NeurIPS D&B 2021).

**Thread 3: Conditional inference with ML predictions.** PPCI (Sui et al., arXiv:2603.05575) extends PPI to conditional functionals at fixed test points via kernel localization. Critical distinction: PPCI addresses outcome prediction noise at a correctly-specified conditioning point; EC-HTE addresses the situation where the conditioning variable (effect modifier) itself is misclassified. PPCI's localization anchors on correct covariate values—when the anchor itself is wrong (categorical misclassification), kernel localization cannot help.

**Thread 4: Measurement error correction for ML-generated variables.** ForestIV (Bu et al., INFORMS JDS 2023) uses random forest tree tuples as instrumental variables, but requires IV exclusion restrictions and is limited to regression settings, not CATE with categorical effect modifiers. Jerzak et al. (arXiv:2509.12416, SRI framework) provide valid inference under noisy annotation but do not address effect modifier misclassification's impact on HTE. SIMEX handles continuous measurement error models but does not directly apply to categorical misclassification.

**Thread 5: Causal inference with textual variables.** Feldman et al. (arXiv:2602.15730) address latent textual treatment estimation using SAE + residualization, assuming clean effect modifiers. Nwankwo et al. (arXiv:2502.10605, NeurIPS 2025 Workshop) optimize annotation allocation for doubly robust ATE with missing outcomes—different estimand (ATE vs. CATE), different error source (outcome missingness vs. effect modifier misclassification), different optimization landscape.

EC-HTE sits at the intersection of Threads 1–4: correcting LLM misclassification specifically in effect modifiers for valid CATE estimation.

## Validation Design

### Semi-Synthetic Experiments

**Corpus.** Political science text corpus with real-world linguistic variation (e.g., immigration framing data or partisan tweet datasets with known ideological annotations).

**DGP Matrix.** Core factors:
- Misclassification severity: high (25–30%) vs. low (5–10%)
- CATE heterogeneity magnitude: large (>0.3 SD) vs. small (<0.1 SD)
- Subgroup count: k=3 vs. k=6
- **Misclassification-CATE correlation direction**: positive (high-error subgroups have high CATE, worst-case) vs. negative (high-error subgroups have low CATE, best-case)

Selective design: 12–14 configurations covering all worst-case/best-case combinations for the key factors, rather than full 2⁴=16 factorial.

Treatment assignment T ~ Bernoulli(0.5); potential outcomes Y(1), Y(0) generated with known ground-truth CATE τ(x) varying by subgroup.

**Replications.** ≥ 200 per configuration.

**Sample sizes.** N ∈ {2000, 5000, 10000}.

**Expert label budget.** B ∈ {100, 500, 1000, 2000} to produce budget vs. performance curves. All methods compared under identical total budget.

**LLMs.** Three annotators: GPT-4.1 (proprietary frontier), Qwen 3.5 (open-source large), Llama 3.3 (open-source, different family). Fourth LLM as appendix robustness check.

### Comparison Methods (all under fixed expert annotation budget B)

1. **Uncorrected**: LLM annotations used directly as effect modifiers in causal forest.
2. **Globally-corrected**: Single confusion matrix → corrected annotations → causal forest.
3. **Arm-specific (Mozer-style)**: Separate confusion matrices for treatment/control arms → causal forest.
4. **SIMEX + causal forest**: SIMEX-based measurement error correction → causal forest.
5. **Calibration-only + causal forest**: Platt scaling / temperature scaling → calibrated probabilities as soft effect modifiers → causal forest.
6. **EC-HTE (full)**: Hierarchical Bayesian subgroup-specific correction → sandwich-adjusted causal forest → adaptive allocation.

### Evaluation Metrics

- **PEHE**: √E[(τ̂(x) − τ(x))²], overall and per-subgroup.
- **Subgroup CATE bias**: |E[τ̂_g] − τ_g| for each subgroup g.
- **CI empirical coverage**: Fraction of replications where true CATE falls within 95% CI (target: 0.95).
- **CI width**: Efficiency measure at fixed coverage.
- **GATE RMSE**: RMSE of group average treatment effect estimates.
- **Bound tightness**: Observed bias vs. theoretical bound prediction.

### Ablation Studies

**Stage 1 ablation (partial pooling):**
- (a) Hierarchical Bayesian with VI (partial pooling)
- (b) Per-subgroup independent confusion matrices (no pooling)
- (c) Single global confusion matrix (full pooling)
- (d) Prior sensitivity: 2–3 prior settings (weakly informative, moderately informative, diffuse) on 1–2 representative DGP configurations

**Stage 2 ablation (variance adjustment):**
- (a) Sandwich variance-adjusted CIs
- (b) Bootstrap-based CIs
- (c) Naive CIs (no adjustment)
→ Compare empirical coverage rates.

**Stage 3 ablation (allocation strategy):**
- (a) Joint criterion (misclassification uncertainty × CATE magnitude)
- (b) Misclassification-uncertainty-only allocation
- (c) CATE-magnitude-only allocation
- (d) Uniform allocation
- (e) Pilot ratio sensitivity: 10%, 20%, 30% of B as uniform pilot batch
→ Compare PEHE at fixed total budget B.

**Diagnostic validation:** Systematically vary misclassification heterogeneity and CATE heterogeneity (including correlation direction); produce heatmap of EC-HTE improvement over global correction vs. (product of heterogeneity measures). Verify that the theoretical bound predicts when global correction fails and when it suffices. Specifically demonstrate that global correction is worse than uncorrected in positive-correlation configurations.

**CATE estimator robustness (appendix):** In 1–2 worst-case configurations, replace causal forest with DR-learner to verify EC-HTE's correction generalizes beyond a single CATE estimator.

### Real-Data Application (Ashwin et al., 2025)

**Dataset.** Rohingya refugee interview transcripts (Ashwin et al., Sociological Methods & Research 2025). This dataset's primary role is validating the premise of EC-HTE—that LLM misclassification is differential—rather than evaluating CATE estimation accuracy (the dataset lacks a natural causal structure).

**Validation goals:**
1. **Differential misclassification pattern confirmation**: Quantify and visualize how LLM error rates vary across subgroups defined by refugee status, gender, education.
2. **Leave-expert-out calibration test**: Treat full human labels as ground truth, subsample B expert labels, evaluate whether EC-HTE's hierarchical confusion matrix estimates recover the true subgroup-specific error patterns better than global estimation.
3. **Diagnostic criterion demonstration**: Compute the misclassification-heterogeneity × CATE-heterogeneity product on this dataset (constructing a plausible causal question from available variables) to demonstrate the diagnostic's operability.
4. **Budget curve**: Accuracy of confusion matrix recovery vs. expert label budget B.

CATE estimation accuracy is rigorously evaluated in the semi-synthetic experiments where ground-truth CATE is known.

## Scope and Limitations

EC-HTE targets **categorical effect modifiers** (stance, topic, sentiment, entity type, etc.)—the dominant use case when LLM annotations serve as moderators in computational social science. When the effect modifier is a continuous variable that has been discretized (binned), misclassification includes both LLM errors and discretization error; the current framework does not disentangle these sources. Extension to continuous effect modifiers with measurement error (where SIMEX-type approaches may be more natural) is future work.

## Broader Applicability

While our validation focuses on CSS, the same problem structure arises whenever ML-predicted categorical variables serve as effect modifiers: in medical research (ML-classified tumor subtypes as moderators of drug efficacy), education (NLP-coded classroom behaviors moderating intervention effects), and policy evaluation (automated classification of administrative characteristics). EC-HTE's framework and diagnostic criterion apply directly to these settings.

## Expected Contributions

EC-HTE provides (1) the first formal identification of measurement-error-induced CATE distortion in LLM-annotated pipelines, including the proof that global correction can worsen estimates; (2) an actionable diagnostic (the misclassification-heterogeneity × CATE-heterogeneity product) with standalone value for any CATE analysis; (3) a practical three-stage correction framework with valid inference; and (4) comprehensive empirical validation. The framework serves any study using LLM-annotated categorical text variables as effect modifiers in causal analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6d536250-0dca-4457-a7ff-4a075e19d420",
  "type": "user",
  "uuid": "9d29e0b7-193a-49a0-ae73-29fbaefd6815",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:27:19.239Z_

```json
{
  "parentUuid": "9d29e0b7-193a-49a0-ae73-29fbaefd6815",
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
  "uuid": "d01ece20-fba3-478e-ba74-fcde4c3cd216",
  "timestamp": "2026-05-20T04:27:19.239Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:27:19.239Z_

```json
{
  "parentUuid": "d01ece20-fba3-478e-ba74-fcde4c3cd216",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "618f78ae-3e3f-4aed-9e5b-200246241163",
  "timestamp": "2026-05-20T04:27:19.239Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research data. Let me compile the evalua…",
  "leafUuid": "618f78ae-3e3f-4aed-9e5b-200246241163",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Correct CATE estimates with misclassified LLM annotations",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:27:41.870Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them as Meta Judge.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Probability: [28% - 42%] 中位 35%
- Rubric scores: 研究问题=强, 方法与创新=中偏强, 实验设计=强, 可行性=强, 写作=强
- Main risks: compositional novelty, limited real-data validation


- Reviewer 2 gives a similar probability range of 30-42% (median 36%) with nearly identical rubric assessments, though flagging methodological innovation depth and lack of end-to-end real-world validation as concerns. Reviewer 3 is slightly more optimistic at 32-43% (median 37%), with comparable scores across the board except for a slightly lower feasibility rating, and mentions reviewer matching and real-world validation as remaining issues.

Now I'm calculating the consistency across all three reviewers. The three median probabilities cluster tightly at 35%, 36%, and 37%, giving a mean of 36% with a standard deviation of only about 0.82%—this indicates very strong agreement. Looking at the consensus dimensions, all three reviewers align on the research question, experimental design, and writing quality being strong, while they consistently view methodological innovation as moderate to moderately strong, suggesting the novelty is the primary area of concern. The three reviewers show remarkable consistency on the scoring ranges, with their estimates clustering tightly around 30-42% and a median of 36%, so I'll use that as my final consensus estimate. I'm also noting the implementation assessments are equally consistent across reviewers, so I can compile those findings with confidence before formatting the output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "618f78ae-3e3f-4aed-9e5b-200246241163",
  "isSidechain": false,
  "requestId": "req_011CbDBskoqtqiv9nDzXrELM",
  "type": "assistant",
  "uuid": "d51f5de0-f805-4d0b-b1d0-590033ab348f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01866kByEKrmSu69tNvnZdKn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21609,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3208,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 21609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21609
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

_source line 9 · 2026-05-20T04:28:39.783Z_

【阶段】: Meta Judge
【三次中位】: [35%, 36%, 37%]  std=0.8%
【共识维度】:
- 研究问题 = **强**（3/3 一致）：问题真实、时效性强、有 Ashwin et al. (2025) 直接实证支撑，novelty claim（ATE→CATE 去偏空白）经三方独立调研均验证成立
- 实验设计 = **强**（3/3 一致）：DGP 矩阵设计全面（特别是误分类-CATE 相关方向的正/负变化），6 种 baseline 覆盖充分，评估指标完备，200+ replications，多 LLM 验证
- 写作与呈现 = **强**（3/3 一致）：反直觉发现作为 hook 有效，五线程 related work 结构清晰，differentiation 精准
- 方法与创新 = **中 至 中偏强**（3/3 共识核心判断一致）：创新主要在问题识别和理论洞察（bias bound），而非方法论本身；三阶段框架是成熟工具（层次贝叶斯 + 因果森林 + sandwich variance + 自适应分配）的组合式应用——R1 和 R3 给"中偏强"，R2 给"中"，分歧仅在一个亚档位
- 可行性 = **强 至 中偏强**（3/3 共识：可执行，风险可控）：R1/R2 给"强"，R3 给"中偏强"（强调实验管理复杂度），实质判断一致
- **共识风险 1**：组合式创新 / 方法论新颖性有限（3/3 均提及）——核心贡献被定位为 "problem identification paper" 而非 "method paper"，审稿人可能判 incremental
- **共识风险 2**：Real-data validation 不完整（3/3 均提及）——Ashwin et al. 数据仅验证前提（差异化误分类存在），无法评估端到端 CATE 校正效果，半合成实验承担全部因果验证
- **共识风险 3**：审稿人匹配不确定性（2/3 明确提及，R1 隐含）——需要同时理解因果推断 HTE 和 NLP annotation debiasing 的审稿人

【异常维度】:
- R2 独有：明确指出 "global correction worsens estimates" 在流行病学/测量误差文献中是经典知识（differential misclassification），可能削弱对 NLP 社区的 novelty claim。R1/R3 未挑战此 claim 的 novelty。→ R2 在方法论严格性上更保守，但此点确实有依据（Rothman, Greenland & Lash 教科书），应适度纳入
- R2 独有：发现 AM-PPI (arXiv:2605.08429) 作为新增相关工作。→ 有效补充，但 AM-PPI 仍锁定在 ATE 级别，不改变 novelty claim 的成立性
- R3 独有：对可行性略保守（中偏强 vs. 其他两人的强），强调实验管理复杂度和统计学实现功力要求。→ 合理的务实考量，但不构成降档理由

【最终概率】: [30% - 42%] 中位 36%
【一致性】: 高（std=0.8%，三位审稿人在所有 rubric 维度上判决高度一致，概率区间大幅重叠）
【综合理由】:
三位审稿人的评估呈现罕见的高度收敛——不仅概率中位集中在 35-37% 的极窄区间内，而且在所有 5 个 rubric 维度上的判决几乎完全一致（研究问题=强，实验设计=强，写作=强，方法创新=中/中偏强，可行性=强/中偏强）。三方独立进行的领域调研均验证了 novelty claim 的成立性（ATE→CATE 去偏的空白确实存在），且引用了高度重叠的文献集（Audinet de Pieuchon EMNLP 2025、StratPPI、PPCI、Persson、Boileau、Ashwin 等），交叉验证了调研的可靠性。

在高一致性下（std < 3%），取中位附近并略微缩窄区间是合理的。三方区间的交集是 [32%-42%]，考虑到 R1 下界 28% 仅为微幅保守而无实质性差异判断支撑，最终区间取 [30%-42%]。中位 36% 直接取三方中位的算术均值（36%），与三份评审中最审慎的 R1（35%）和最宽松的 R3（37%）均相差 1%。

对 R2 的异常维度处理：R2 指出 differential misclassification 是流行病学经典概念，这确实降低了 "anti-intuitive finding" 在统计学专家看来的 novelty，但对 NLP/CSS 社区的 EMNLP 审稿人仍具有新颖性。这一分歧已反映在 R2 给方法创新"中"而非"中偏强"的评分中，其影响已内化在 R2 的 36% 中位中，无需额外调整。

**概率天花板分析**：idea 质量由 Novelty（中/中偏强）和 Significance（强）共同决定。Significance 强但 Novelty 仅在"问题识别"层面而非"方法论突破"层面，天花板约 42-45%。实验完备性为"强"，地板已基本补实（唯一缺口是 real-data end-to-end validation）。最终概率在 36% 中位处于天花板以下合理位置。

【建议】: 边缘（Borderline — solid proposal with clear gap, worth iterating）

【实施评估】:
  - 计算资源: 中等。主要是 LLM API 调用费用（GPT-4.1 + Qwen 3.5 + Llama 3.3，预估 $500-2000）和标准 CPU 集群上的大规模仿真（14 配置 × 200 replications × 多 N/B 组合，可并行化）。层次贝叶斯用 VI 拟合（秒级），因果森林有成熟 R 包 `grf`（分钟级）。无需 GPU 训练。
  - 数据需求: 低。半合成实验用公开政治文本语料（immigration framing / partisan tweets），Ashwin et al. (2025) Rohingya 数据集已发表可获取。无需新数据采集。
  - 人工介入: 低。不需要新的人工标注——半合成中"专家标签"由 DGP 生成，真实数据部分使用 Ashwin et al. 已有专家标注。
  - 训练需求: 无大模型训练。使用现成 LLM API 做零/少样本标注，层次贝叶斯 VI 和因果森林为传统统计/ML 模型。
  - 新 Benchmark: 否。DGP 矩阵 + 评估协议本身可作为社区可复用的评测基础，但不需专门构建新 benchmark。
  - 预估周期: 3-4 个月（理论推导 + 方法实现 3-4 周 → 半合成实验 4-6 周 → 真实数据验证 1-2 周 → 论文写作 3-4 周）。适合 2 人团队，需具备因果推断和贝叶斯建模经验。可并行化压缩至 2.5 个月。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d51f5de0-f805-4d0b-b1d0-590033ab348f",
  "isSidechain": false,
  "requestId": "req_011CbDBskoqtqiv9nDzXrELM",
  "type": "assistant",
  "uuid": "1e48aa97-1401-485a-85b9-018e06ea6205",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01866kByEKrmSu69tNvnZdKn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21609,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3208,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 21609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21609
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research data. Let me compile the evalua…",
  "leafUuid": "1e48aa97-1401-485a-85b9-018e06ea6205",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Correct CATE estimates with misclassified LLM annotations",
  "sessionId": "c5fd9e1e-23b4-4571-bc6d-e02837953690"
}
```

---
