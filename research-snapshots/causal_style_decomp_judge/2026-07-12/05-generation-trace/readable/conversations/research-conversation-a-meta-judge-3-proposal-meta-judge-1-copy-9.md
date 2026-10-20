# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/7f00dd12-7cdf-413f-aa59-15c7a0f1ea82.jsonl`
- **Structured JSON:** [`f8030d99fe1e2fc1e219.json`](../../sessions/f8/f8030d99fe1e2fc1e219.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:24:43.938Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:24:43.938Z",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide my evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084) (NeurIPS 2025): 在无标签数据上通过多数投票伪标签进行 GRPO 训练，Qwen2.5-Math-7B 在 AIME 2024 上从 16.7%→43.3%。本 proposal 的基础框架，但 TTRL 仅用于非形式化数学推理，依赖数值答案的多数投票——这正是 proposal 要解决的问题之一（形式化语句无法直接做 majority voting）。\n\n- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327) (ACL 2026 Findings): 诊断并修复 GRPO 在 TTRL 中的 spurious signal amplification，提出 frequency-based balanced sampling + fixed ±1 advantages + consensus-based off-policy refinement。在 AIME 2024 上相对 TTRL baseline（15.8→25.0 for Qwen2.5-Math-1.5B）提升显著。**但仅支持 binary rewards**，其作者明确将 multi-reward 扩展留作 future work。proposal 的 \"binarize-then-enrich\" 正是回应这一 gap。\n\n- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242) (NVIDIA, Jan 2026): 发现 GRPO 在 multi-reward 场景下会将不同 reward 组合 collapse 成相同 advantage 值，提出 per-reward decoupled normalization。已在 tool calling、math reasoning、coding 上验证。proposal 借用其 per-reward normalization 作为 enrichment layer。\n\n- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181) (ByteDance/Nanjing, July 2025): 训练 CriticLeanGPT-14B-RL 达到 84.8% accuracy（32B 版本 87.0%），将 autoformalization pipeline 准确率从 54%→84%。但仅在 balanced 250/250 分布上评估，OOD 场景下的 skewed distribution 表现未知。proposal 的 Phase 0 calibration 正是针对此 gap。\n\n- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914) (COLM 2025): 首个将 GRPO+compilation reward 用于 autoformalization，Qwen2.5-Coder-7B 在 ProofNet 上从 4%→26%。但使用 LLM consistency 作为语义 reward（而非 trained critic），且无 retrieval，仅在 in-distribution 场景。\n\n- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization) (Wang et al., NeurIPS 2025 MAR Workshop): 使用 GRPO + composite BEq+embedding rewards 在 Lean 4 上做 autoformalization RL，TC1: 17.29%→26.01%。**最近的 baseline**，但属于 training-time RL，使用 embedding similarity 而非 trained critic，无 retrieval 和 test-time adaptation。\n\n- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990) (2025): 构建 500K 样本依赖数据集，量化 ICL 生成的依赖中~30% 为 hallucinated identifiers（Hall_m=0.21-0.39），retrieval-based DDR 将 hallucination 降至 <2%。proposal 使用其数据集和 retriever 架构作为起点。\n\n- [Construction-Verification/AMBER Benchmark](https://arxiv.org/abs/2602.01291) (Yang et al., Feb 2026): 在 applied math 领域分析 3,189 个编译错误，发现 47.3% 为 hallucination of non-existent theorems/definitions。这是 proposal 关于 \"identifier hallucination 是 dominant error mode\" 的最强实证支撑。\n\n- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652) (NeurIPS 2025): 通过 trial-and-feedback reinforced contrastive learning 优化 RAG 环境中的 retriever。proposal 的 co-adaptive retrieval 借鉴其 contrastive learning 框架，但应用到完全不同的 domain（Lean 4 dependency retrieval）。\n\n- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061) (May 2026): 52K graduate-level 问题，最佳模型仅 9.8% correctness on theorems，MA-Hard 上 2.6%。验证了 OOD autoformalization 仍是极具挑战性的开放问题。\n\n- 调研总结: Autoformalization 领域在 2025-2026 经历快速发展：RL-based 方法（FormaRL, Online RL）已初步验证，semantic critic（CriticLean）提供了编译之外的 reward 信号，static retrieval（DDR, DRIFT, CRAMF）大幅降低了 identifier hallucination，TTRL 在非形式化数学推理中取得突破。但**尚无工作将 TTRL 应用于 autoformalization，尚无工作在 RL 过程中对 retriever 做 co-adaptive 更新，尚无工作将 DDRL 的 binary debiasing 扩展到 multi-tier rewards**。Proposal 定位在这三个 gap 的交叉点上。\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative 是：**static DDR retrieval + CriticLean reward + vanilla GRPO（不做 co-adaptive retrieval，不做 DDRL debiasing）**。这基本上是把 FormaRL 的 reward 换成更好的 CriticLean，再加上 DDR 提供的 Mathlib 依赖。\n\n这个 trivial baseline 的关键弱点在于：\n1. **Static retrieval 在 OOD 域会失效**：DDR 的 retriever 在训练数据分布上训练，面对 condensed mathematics 或 algebraic geometry 等 far-OOD 域，retrieval recall 会显著下降，因为 query distribution 发生了 shift。这是 co-adaptive retrieval 的核心增量价值——retriever 随 formalizer 的行为变化而适应。\n2. **Vanilla GRPO 在低 consensus 场景会放大噪声**：DDRL 已经实证证明了这一点（AIME 2024 上 TTRL baseline 仅 15.8 vs DDRL 的 25.0）。在 autoformalization 的 OOD 场景中，compilable rate 很低，consensus 更差，噪声放大问题会更严重。\n\n但也必须承认：**在 near-OOD 域，static retrieval + CriticLean + vanilla GRPO 可能已经足够好**。Proposal 的增量价值主要体现在 far-OOD 场景。如果实验发现大多数 benchmark 属于 near-OOD，co-adaptive retrieval 和 DDRL debiasing 的 marginal gain 可能很小。\n\n**增量价值判断**：co-adaptive retrieval 是最有说服力的增量贡献（问题明确、机制新颖、利用了 Lean 4 独特的结构化错误信息）。Binarize-then-enrich 的增量价值较弱（在 DDRL 和 GDPO 都已存在的前提下，这一步近乎 obvious）。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中，以下环节是未经验证的假设：\n\n1. **\"CriticLean-14B 在 OOD skewed distribution 下仍能保持足够的 precision\"**：CriticLeanBench 仅在 balanced 250/250 分布上评估（84.8% accuracy）。在 TTRL 的 OOD 场景下，>90% 的 candidate 可能不正确，critic 的 false positive rate 可能会显著恶化。Proposal 的 Phase 0 calibration 试图验证这一假设，但这也意味着**如果这个假设不成立，整个 pipeline 的基础就会动摇**。这是最关键的风险点。\n\n2. **\"Lean 4 的 unknownIdentifier 等 Tier 1 错误在 OOD 域占比足够高（≥40%）以支撑 co-adaptive retrieval\"**：AMBER 的 47.3% 来自 DeepSeek-R1 on applied math，但 proposal 使用更小的 formalizer 在不同 OOD 域上。Proposal 承认了这一点（Phase -1 就是为了验证），但如果 Tier 1 比例很低（如 <20%），co-adaptive retrieval 的 core mechanism 会大打折扣。\n\n3. **\"co-adaptive retriever 更新不会 destabilize RL training\"**：交替优化 retriever 和 formalizer 在理论上可能导致不稳定——retriever 变化改变 input context → formalizer 的 reward landscape 发生 shift → GRPO 的 advantage estimation 受到干扰。Proposal 借鉴 R3 和 Reinforced-IR 的 decoupled optimization，但这些工作是在 text QA 领域验证的，autoformalization 场景的 reward 更加 sparse 和 noisy，是否同样稳定未经验证。\n\n4. **\"Binarize-then-enrich 的 DDRL 扩展在 multi-tier reward 场景下能保持 DDRL 的 debiasing 效果\"**：DDRL 的理论分析基于 binary reward 的简洁结构（correct/incorrect）。加入 GDPO enrichment layer 后，fixed ±1 advantages 被 BEq bonus 打破，debiasing 的理论保证是否仍然成立是一个开放问题。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Co-adaptive retrieval exploiting Lean 4's structured error taxonomy 是最强的新颖贡献：没有先前工作在 RL-based autoformalization 过程中对 retriever 做 online adaptation，利用 unknownIdentifier/type mismatch 等结构化错误信号构建 graded contrastive training data 的设计是 domain-specific 且有新意的。这一点与 R3 (NeurIPS 2025) 和 Reinforced-IR (ACL 2025) 在 text QA 上的 co-adaptive retrieval 形成清晰区分——后者不涉及编译器的结构化错误信号。\n\n   但整体而言，proposal 的 novelty 分布不均匀。\"Binarize-then-enrich\" 的贡献较薄：一旦知道 DDRL 处理 binary rewards、GDPO 处理 multi-reward normalization，将二者组合（先 binarize 使 DDRL 适用，再用 GDPO 对 continuous component 做 enrichment）是一个**几乎 obvious 的工程决策**，缺乏深层 insight。CriticLean 作为 TTRL reward 也是自然的应用延伸（CriticLean 论文本身就在 RL pipeline 中使用了 critic reward）。\n\n   此外，TTRL 应用于 autoformalization 虽然是\"首次\"，但 Online RL for Autoformalization (Wang et al.) 已经做了 training-time RL for autoformalization with composite rewards，从 training-time 到 test-time 的跨越虽有价值但不构成根本性 novelty 突破。\n\n   **总体判断**：有一个扎实的新贡献点（co-adaptive retrieval with error taxonomy），其余贡献是competent combination work。对于 AAAI，这处于中等水平——不是 trivial incremental，但也达不到 \"surprising insight\"。\n\n2. **Significance: 中偏强** — \n   Autoformalization 的 OOD generalization 是一个真实且重要的问题。MathAtlas (2026) 显示最佳模型在 MA-Hard 上仅 2.6%，AMBER (2026) 量化了 47.3% 的编译错误来自 identifier hallucination——**问题的重要性和 urgency 是有充分实证支撑的**。\n\n   如果 proposal 的方法在 far-OOD 域（condensed mathematics, algebraic geometry）上实现显著提升，这对 AI for mathematics 社区有实际价值。Co-adaptive retrieval 机制如果成功，可以推广到其他涉及编译器反馈的形式化任务（proof generation, code synthesis）。Binarize-then-enrich 虽然 insight 有限，但作为通用方法论确实有跨领域适用性。\n\n   限制 significance 的因素：autoformalization 仍是一个相对小众的子领域。虽然在 AI for math 热潮中受到更多关注，但与 LLM reasoning、code generation 等热门方向相比，直接受众有限。\n\n3. **Related Work: 强** — \n   这是 proposal 最突出的优势。覆盖了 5 个相关研究脉络，引用了 25+ 篇论文，包括最新的 2026 年工作（DDRL, GDPO, MathAtlas, Construction-Verification/AMBER）。关键对比点清晰：\n   - 与 FormaRL: 使用 trained critic 而非 LLM consistency，加入 retrieval 和 test-time adaptation\n   - 与 Online RL for Autoformalization: test-time 而非 training-time，trained critic 而非 embedding similarity\n   - 与 DDR/DRIFT: dynamic co-adaptive 而非 static retrieval\n   - 与 DDRL: multi-tier reward 而非 binary\n   \n   调研中确认的引用（DDR 的 500K 数据集、AMBER 的 47.3% hallucination rate、CriticLean 的 84.8% accuracy、DDRL 的 AIME 结果）均与原始论文一致。差异化定位清晰且准确。唯一的轻微不足是：对 ATLAS (NeurIPS 2025) 和 Monotonic Refinement 的讨论主要作为 reference point，没有深入分析它们的 inference-time refinement 策略是否能部分替代 TTRL 的功能。\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \nNovelty 是中等水平（一个扎实的新贡献 + 若干 obvious combination），这限制了概率的上界——一个审稿人可能会写 \"the co-adaptive retrieval idea is interesting, but the binarize-then-enrich and critic integration feel like natural engineering choices rather than research contributions\"。Significance 中偏强但受限于子领域的受众规模。Related work 是真正的强项，降低了被 \"missing related work\" 拒稿的风险。\n\n从 rubric 锚点来看：proposal 有真实的 novelty delta（co-adaptive retrieval with error taxonomy），方向正确，问题重要，但核心发现如果 positive（\"co-adaptive retrieval + debiased RL 在 OOD autoformalization 上优于 static retrieval + vanilla GRPO\"），审稿人更可能说 \"this makes sense, I would have expected retrieval adaptation to help\" 而非 \"this is surprising\"。这将其定位在 25-35% 区间。\n\n上界被 novelty 深度限制：proposal 的创新主要在 combination 层面，单个贡献的 insight 深度有限。下界被 related work 覆盖度和 Phase 0 de-risking 设计支撑：这是一个 well-crafted proposal，不太可能因为\"方向不对\"或\"遗漏关键工作\"而被直接拒绝。\n\n【主要风险】:\n1. **\"Kitchen sink\" / combination paper 质疑**：Proposal 集成了 4+ 个现有技术（TTRL, DDRL, GDPO, co-adaptive retrieval, CriticLean, progressive curriculum），审稿人可能认为没有任何一个单独贡献有足够的深度，整体是 \"competent systems work\" 而非 \"research contribution\"。Binarize-then-enrich 尤其容易被认为 trivial。\n2. **核心前提（CriticLean 在 OOD skewed distribution 下的可靠性）未经验证**：如果 Phase 0 calibration 发现 critic precision 在 skewed distribution 下显著低于 80%，整个 pipeline 的 reward signal 基础就会受到质疑。即使 proposal 设计了 confidence gating 作为 fallback，审稿人可能会认为这是在 patch 一个根本性的 weakness。\n```\n\nSources:\n- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)\n- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327)\n- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242)\n- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181)\n- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)\n- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)\n- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)\n- [Construction-Verification/AMBER Benchmark](https://arxiv.org/abs/2602.01291)\n- [R3: Optimizing Retrieval for RAG via Reinforcement Learning](https://arxiv.org/abs/2510.24652)\n- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)\n- [NVIDIA GDPO Official Page](https://nvlabs.github.io/GDPO/)\n- [Kimina-Prover: Test-time RL on Formal Reasoning](https://huggingface.co/blog/AI-MO/kimina-prover)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084) (NeurIPS 2025): 提出在测试时利用 majority voting 伪标签进行 RL 训练，在 AIME 2024 上将 Qwen-2.5-Math-7B 的 pass@1 提升约 211%。这是本 proposal 的核心基础之一，但仅适用于有明确数值答案可做 majority voting 的非形式化数学推理。\n- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327) (ACL 2026 Findings): 识别了 GRPO 归一化在低共识场景下放大伪信号的问题，提出频率平衡采样 + 固定 ±1 advantages + 共识离策略优化三组件方案。在 AIME 2024 上对 Qwen2.5-Math-1.5B 实现 21.0→25.0 的提升。**关键限制：仅处理二元 (correct/incorrect) 奖励。**\n- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242) (NVIDIA, Jan 2026): 针对多奖励 GRPO 的 reward signal collapse 问题，提出每个奖励独立归一化后再聚合。在工具调用、数学推理、代码生成任务上优于标准 GRPO。\n- [CriticLean](https://arxiv.org/abs/2507.06181) (Jul 2025, ByteDance/Nanjing): 训练 CriticLeanGPT 作为语义保真度判别器，14B-RL 变体在 CriticLeanBench (250 correct / 250 incorrect 平衡分布) 上达到 84.8% 精度。**关键限制：仅在平衡分布上评测，严重倾斜分布下的表现未知。**\n- [FormaRL](https://arxiv.org/abs/2508.18914) (COLM 2025): 使用 GRPO + 编译检查 + LLM 一致性检查作为奖励，在 ProofNet 上将 pass@1 从 4% 提升至 26%。训练时 RL，无 retrieval 适应，无测试时适应。\n- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045) (Wang et al., NeurIPS 2025 MAR Workshop): 使用 GRPO + BEq + embedding 奖励，在 RLMEval 上 TC1 从 17.29% 提升至 26.01%。**与本 proposal 最接近的先驱工作，但为训练时 RL，使用 embedding 相似度而非训练过的 semantic critic，无 retrieval 适应。**\n- [DDR: Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990) (arXiv 2025): 构建 500K 样本依赖检索数据集，将 ICL 生成依赖的幻觉率从 21-39% 降至 <2%。**关键数据：量化了 identifier hallucination 的严重程度，为本 proposal 提供了 co-adaptive retrieval 的动机基础。**\n- [Construction-Verification/AMBER](https://arxiv.org/abs/2602.01291) (Feb 2026): 分析了 DeepSeek-R1 在应用数学上的 3,189 个编译错误，发现 47.3% 是不存在的定理/定义幻觉，32.7% 是形式化能力错误。**直接支撑了 proposal 的 ≥40% Tier 1 错误阈值假设。**\n- [R3: Optimizing Retrieval for RAG via Reinforcement Learning](https://arxiv.org/abs/2510.24652) (NeurIPS 2025): 通过强化对比学习在 RAG 环境中自适应优化 retriever，比原始 retriever 提升 5.2%。**为本 proposal 的 co-adaptive retrieval 提供了方法论基础。**\n- [TTARAG](https://arxiv.org/abs/2601.11443) (Jan 2026): 在推理时通过自监督预测任务动态更新 LM 参数以适应新领域。验证了测试时检索适应的可行性，但方法完全不同（前缀-后缀预测）。\n- [MathAtlas](https://arxiv.org/abs/2605.14061) (May 2026): 52K 研究生级别数学问题，最强模型在 MA-Hard 上仅 2.6% 正确率。**为本 proposal 提供了理想的 OOD 评测场景。**\n- [DRIFT](https://arxiv.org/abs/2510.10815) (ICLR 2026): 分解-检索-举例-形式化流水线，在 Con-NF 上达到 62.33% BEq+@10。静态检索，无 RL 适应。\n- [RAutoformalizer](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d630537fc4402cfa3ebbc7450a0cac91-Abstract-Conference.html) (ICLR 2025 Spotlight): 将编译错误分类为\"Hallucination\"和\"Others\"两大类，确立了 identifier hallucination 作为主要错误类别。\n\n- **调研总结**: 自动形式化领域正在快速发展，RL（FormaRL, Wang et al.）和 retrieval（DDR, DRIFT, CRAMF）两条技术路线已分别取得显著进展，但二者的结合——尤其是在测试时进行 co-adaptive retrieval + RL——目前确实是空白。TTRL 范式已在非形式化数学推理中验证，但因 majority voting 不适用于形式化语句，直接迁移存在技术挑战。DDRL 解决了 TTRL 的伪信号放大问题但仅限二元奖励。本 proposal 处于多条成熟技术路线的交汇点。\n\n【Trivial Alternative 检验】:\n最直接的 trivial alternative 是：**DDR (静态检索) + CriticLean 奖励 + 标准 GRPO**，不需要 co-adaptive retrieval、不需要 DDRL debiasing、不需要 binarize-then-enrich。\n\n具体分析：\n1. **静态检索 vs. co-adaptive 检索**: DDR 已将 identifier hallucination 从 21-39% 降至 <2%。如果静态检索已经基本解决了 identifier hallucination 问题，co-adaptive retrieval 的增量价值可能有限。但 proposal 的反论点有一定道理：DDR 的 <2% 是在 in-distribution 评测，OOD 域（如凝聚态数学、代数几何）的 Mathlib 依赖分布可能与训练分布显著不同，静态检索可能退化。这一点是否成立取决于 Phase -1 的实证结果。\n2. **DDRL debiasing vs. vanilla GRPO**: FormaRL 已经证明 vanilla GRPO 在 autoformalization 上有效（4→26%）。DDRL 在非形式化数学上的提升为 15.8→25.0（AIME 2024），即约 58% 相对提升。但 autoformalization 的奖励结构（compilation + critic + BEq）与数学推理的二元对错有本质区别，DDRL 的收益能否迁移是未经验证的。\n3. **Binarize-then-enrich 的必要性**: 如果直接用 GDPO 的 per-reward 归一化就足够了，binarize-then-enrich 这一\"先二值化再丰富\"的两步法可能是过度工程。\n\n**增量价值判断**: co-adaptive retrieval 在 OOD 场景的理论动机成立（静态检索在 distribution shift 下可能退化），但实际增量大小高度依赖经验验证。binarize-then-enrich 的增量价值不确定——它试图同时获得 DDRL 的 debiasing 和 GDPO 的多奖励保真度，但能否 outperform 二者单独使用尚不清楚。\n\n【前提假设检验】:\n核心逻辑链中存在以下未经验证的假设：\n\n1. **\"Lean 4 结构化错误信号足以驱动有效的 retriever 对比训练\"（关键假设）**: 虽然 AMBER 证明了 47.3% 的错误是 identifier hallucination，但从\"知道缺了什么 identifier\"到\"能据此有效更新 retriever 的 embedding 空间\"之间有显著的技术跳跃。R3 在通用 QA 的 RAG 场景验证了这一路径，但 Mathlib 的依赖空间结构（层级化、高度互联、数学类型系统约束）与通用文档检索有质的不同。Tier 2 信号（类型不匹配）到检索正样本的映射质量未知。\n2. **\"CriticLean-14B 在严重倾斜分布下仍能保持足够的 precision\"（已部分 de-risk）**: Proposal 在 Phase 0 设计了显式的 calibration 实验，这是正确的做法。但如果 precision <80%（即使加了 confidence gating），整个奖励机制的基础就不稳固——Phase 0 的 go/no-go 设计是合理的。\n3. **\"DDRL 的 debiasing 机制在多层奖励下仍然有效\"（弱假设）**: DDRL 的三组件（平衡采样、固定 advantage、共识离策略优化）是为二元奖励设计的。将其中的\"正确/错误\"替换为\"compile+critic 通过/不通过\"在概念上合理，但原始 DDRL 论文中\"ambiguous zone\"的定义（30-70% 正确率）是否适用于 autoformalization 的奖励结构？如果 OOD 域的编译率极低（<10%），几乎所有样本都是\"rejected\"，balanced sampling 可能退化。\n4. **\"Progressive curriculum 能有效解决 bootstrapping 问题\"（弱假设）**: 从近分布到远 OOD 的渐进适应策略直觉上合理，但过渡准则（编译率 ≥40%、critic approval ≥60%）是主观设定的。如果近分布域的收益无法有效转移到远 OOD 域，curriculum 可能只是推迟了问题而非解决了问题。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 本 proposal 的核心贡献是**将多个独立验证的技术路线进行非平凡组合**，而非提出根本性的新方法。具体而言：\n   - Co-adaptive retrieval (Phase 2) 的方法论基础来自 R3 (NeurIPS 2025) 和 Reinforced-IR (ACL 2025)，创新点在于将其应用于 Lean 4 的结构化错误信号层级。这是一个有意义的 domain adaptation，Lean 4 的类型检查器确实提供了比通用 QA 场景更丰富的结构化反馈，Tier 1/2/3 的分层设计利用了领域特有属性。但核心技术（对比学习 + 环境反馈训练 retriever）不是新的。\n   - Binarize-then-enrich (Phase 3) 是 DDRL + GDPO 的嫁接。DDRL 处理二元奖励的 debiasing，GDPO 处理多奖励归一化——将二者串联（先二值化获得 DDRL 的好处，再用 GDPO 恢复连续奖励信息）是一个合理的工程思路，但\"先 binarize 再 enrich\"的框架并非深刻的方法论洞察。\n   - CriticLean 作为 TTRL 奖励 (Phase 0-1) 的应用是直接的——CriticLean 论文本身就是作为 RL 奖励设计的，只是未在 TTRL 场景下评估。Proposal 的分布偏移 calibration 是务实的工程贡献，但不是概念突破。\n   - **最有新意的元素**是利用 Lean 4 的 structured error taxonomy 构建 graded retriever training signal——这确实是一个 domain-specific insight，尚无先例。但它更接近\"clever engineering\"而非\"new paradigm\"。\n   - 对比：FormaRL (COLM 2025) 提出了 RL for autoformalization (无标注数据)；DDRL (ACL 2026) 提出了 TTRL debiasing 的新方法论；R3 (NeurIPS 2025) 提出了 RL-driven retriever 优化。这些工作各自有独立的方法论贡献。本 proposal 的贡献更多在于\"合理组合 + 领域特化适配\"。\n\n2. **Significance: 中** — \n   - **问题重要性高**: OOD autoformalization 退化是一个真实且重要的问题。MathAtlas 上 2.6% 的 MA-Hard 正确率说明当前方法在 OOD 域几乎完全失效。AMBER 的 47.3% identifier hallucination 率确认了问题的根源。\n   - **影响范围受限**: 目标受众是 autoformalization + RL + formal verification 的交叉社区，相对较窄。Binarize-then-enrich 号称可推广到任何多层奖励场景，但未在其他领域验证，实际影响力有待证明。\n   - **结果预期性**: 如果实验结果是 positive（TTRA 在 OOD 域显著优于 baselines），审稿人的反应更可能是\"reasonable, this is what I would expect from combining better retrieval + better reward + better RL optimization\"而非\"surprising\"。方向正确、预期合理，但缺乏反直觉元素。\n   - **实际价值**: 如果 TTRA 确实能使自动形式化模型在 OOD 域大幅提升（例如 MathAtlas MA-Hard 从 2.6% 到 15%+），这将有显著的实际意义。但这是执行层面的期望，不是 idea 层面的保证。\n\n3. **Related Work: 强** — \n   - 该 proposal 对文献的覆盖极为全面，横跨 RL for autoformalization (FormaRL, Wang et al., ReForm)、semantic critics (CriticLean, ATF)、debiased RL (DDRL, GDPO)、co-adaptive retrieval (R3, Reinforced-IR, TTARAG)、static retrieval & error analysis (DDR, DRIFT, CRAMF, AMBER, RAutoformalizer) 五条研究脉络。\n   - 差异化定位清晰：准确指出了与每个相关工作的具体差异——Wang et al. 是训练时 RL 无 retrieval；FormaRL 用 LLM 一致性而非 trained critic；DDRL 仅限二元奖励；DDR/DRIFT 是静态检索。\n   - 引用的论文经我搜索验证基本准确：AMBER 的 47.3% identifier hallucination 率、DDR 的 <2% 幻觉率、DDRL 的性能数字、CriticLean 的 84.8% 精度等均可通过搜索确认。\n   - 唯一小瑕疵：部分引用（如 MathAtlas May 2026, Monotonic Refinement 2026）因过于新近，难以完全独立验证所有数字。但整体文献素养在 proposal 中属于顶尖水平。\n\n【概率估计】: [23% - 33%] 中位 27%\n\n【估计理由】: \n- **Novelty（中）限制了上界**: 核心贡献是多个已有技术的非平凡组合+领域特化适配，而非根本性的方法论创新。在 AAAI 的审稿标准下，纯\"组合创新\"论文需要 (a) 证明组合本身是非显然的，(b) 各组件产生大于部分之和的协同效应。Proposal 论证了 (a) 但 (b) 需要实验支撑。\n- **Significance（中）将中位数限制在 30% 以下**: 目标受众相对窄（autoformalization + RL + retrieval 交叉），结果若 positive 则\"合理但不意外\"。\n- **Related Work（强）提供了下限保障**: 极为全面的文献覆盖和精确的差异化定位确保了 proposal 不会因 related work 不足而被拒，也使得\"novelty claim 不成立\"的攻击面较小。\n- **上界因素**: 如果利用 Lean 4 error taxonomy 的 graded retrieval signal 被审稿人视为一个 genuine domain-specific insight（而非简单 engineering），novelty 评分可能提升至\"中-强\"，概率上界可达 33%。\n- **下界因素**: 如果审稿人认为这本质上是\"DDR + CriticLean + DDRL + GDPO 的拼接\"且 binarize-then-enrich 不够 principled，novelty 评分会降至\"中-弱\"，概率可能低至 23%。\n\n【主要风险】:\n1. **\"系统拼装\"质疑 (Novelty risk)**: 审稿人可能认为 TTRA 是将 R3 的 co-adaptive retrieval、DDRL 的 debiasing、GDPO 的 multi-reward 归一化、CriticLean 的 semantic critic 简单拼装而成，每个模块的创新都在原始论文中，本文的贡献仅是\"将它们放在一起\"。虽然 proposal 论证了组合的非显然性（如 Lean 4 error taxonomy 的领域特有信号、binarize-then-enrich 的方法论框架），但这取决于审稿人是否 buy 这种组合创新的价值主张。\n2. **Trivial alternative 竞争力 (Core claim risk)**: 如果 DDR 静态检索 + CriticLean + vanilla GRPO 已能获得大部分 OOD 提升（因为 DDR 在 in-distribution 已将幻觉降至 <2%，CriticLean 提供了比 LLM 一致性更好的奖励信号），那么 co-adaptive retrieval 和 binarize-then-enrich 的增量贡献可能不足以支撑一篇 AAAI 论文。Proposal 的 contribution floor analysis 部分缓解了这一风险，但核心创新的增量价值仍是最大不确定性。\n```\n\nSources:\n- [TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)](https://arxiv.org/abs/2504.16084)\n- [DDRL: Spurious Signal Amplification in TTRL (ACL 2026 Findings)](https://arxiv.org/abs/2604.21327)\n- [GDPO: Group reward-Decoupled Normalization (NVIDIA, 2026)](https://arxiv.org/abs/2601.05242)\n- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181)\n- [FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)](https://arxiv.org/abs/2508.18914)\n- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)\n- [Construction-Verification/AMBER Benchmark (Feb 2026)](https://arxiv.org/abs/2602.01291)\n- [R3: Optimizing Retrieval for RAG via Reinforcement Learning (NeurIPS 2025)](https://arxiv.org/abs/2510.24652)\n- [TTARAG: Test-Time Adaptation for RAG (Jan 2026)](https://arxiv.org/abs/2601.11443)\n- [MathAtlas: A Benchmark for Autoformalization in the Wild (May 2026)](https://arxiv.org/abs/2605.14061)\n- [RAutoformalizer (ICLR 2025 Spotlight)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d630537fc4402cfa3ebbc7450a0cac91-Abstract-Conference.html)\n- [Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop)](https://www.researchgate.net/publication/396825045)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to conduct a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. TTRL (NeurIPS 2025, arXiv 2504.16084): 提出 test-time RL 范式，在无标注数据上利用 majority voting 作为伪标签驱动 GRPO 训练，Qwen2.5-Math-7B 在 AIME 2024 上 pass@1 提升约 211%。但 TTRL 的 majority voting 依赖数值答案的可比性，无法直接迁移到形式化数学的结构化输出。\n\n2. DDRL (ACL 2026 Findings, arXiv 2604.21327): 诊断并修复 GRPO 在低一致性区间的虚假信号放大问题，通过频率平衡采样、固定 ±1 advantage、基于共识的 off-policy 精炼实现去偏。关键限制：仅支持二元 reward（正确/错误），作者明确将\"更具表达力的 advantage 公式\"列为 future work。与本 proposal 直接相关——proposal 的 binarize-then-enrich 正是对 DDRL 的扩展。\n\n3. GDPO (NVIDIA, arXiv 2601.05242, Jan 2026): 解决 GRPO 在多 reward 场景下的 reward signal collapse 问题，通过 per-reward 解耦归一化保持不同 reward 维度的区分度。本 proposal 的\"enrich\"层直接借鉴此方法。该工作已开源并有实验验证。\n\n4. CriticLean (arXiv 2507.06181, ByteDance): CriticLeanGPT-14B-RL 在平衡分布的 CriticLeanBench 上达到 84.8% 准确率（32B 达 87.0%），将 autoformalization pipeline 准确率从 54% 提升至 84%。关键缺口：评估仅在 250 正/250 负的平衡分布上，OOD TTRL 中的偏斜分布（>90% 不正确）下的表现未知。Proposal 的 Phase 0 calibration 正是针对此缺口。\n\n5. FormaRL (COLM 2025, arXiv 2508.18914): 使用 GRPO + Lean 编译检查 + LLM 一致性检查作为 reward，在 ProofNet 上 pass@1 从 4% 提升至 26%。无 retrieval，无 test-time adaptation，无 trained semantic critic。是本 proposal 最直接的消融基线之一。\n\n6. Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop): 使用 GRPO + BEq + embedding 相似度复合 reward 进行 Lean 4 autoformalization RL，TC1: 17.29%→26.01%，TC50: 76.41%→85.46%。但在训练时操作（非 test-time），使用 embedding 相似度（非 trained critic），无 retrieval。是最接近的先行工作。\n\n7. DDR (arXiv 2511.11990): 构建 50 万样本依赖数据集，量化 ICL 生成的依赖中约 30% 为幻觉标识符（Hall_m=0.21-0.39），retrieval-based DDR 将幻觉率降至 <2%。为 co-adaptive retriever 提供基础设施和动机。\n\n8. Construction-Verification/AMBER (arXiv 2602.01291, Feb 2026): 分析 DeepSeek-R1 在应用数学域上 3,189 个编译错误，47.3% 为不存在的定理/定义的幻觉——直接支持 Tier 1 错误信号 ≥40% 的假设。\n\n9. R3 (NeurIPS 2025, arXiv 2510.24652): 通过强化对比学习优化 RAG 检索器，证明环境反馈可训练检索器。Reinforced-IR (ACL 2025): 交替 RLRF/RLGF 实现检索器-生成器互适应。两者均未应用于 autoformalization。\n\n10. MathAtlas (arXiv 2605.14061, May 2026): 52K 研究生级别问题，最佳模型在 MA-Hard 上仅 2.6%，Mathlib-grounded 定义比非 grounded 高 66%（27.9% vs 16.8%）。进一步确认依赖可用性是瓶颈。\n\n11. DRIFT (ICLR 2026): 分解-检索-示例-形式化框架，Con-NF 上 62.33% BEq+@10，但 ProofNet 上 21.93%（低于其他方法）。静态检索，无 RL。\n\n12. StepFun-Formalizer (AAAI 2026): 知识-推理融合的 autoformalization，已被 AAAI 2026 接收，证明 autoformalization 方向在 AAAI 有接收先例。\n\n13. ReForm (arXiv 2510.24592): 反射式 autoformalization + PBSO 位置感知 RL reward，平均提升 22.6pp。关注 semantic consistency 但不涉及 retrieval adaptation。\n\n14. ATF (arXiv 2025): SFT + expert iteration + DPO + multi-LLM 一致性检查，FormalMath-Lite 上 94.51% Pass@1。强 in-distribution 性能但无 OOD 适应能力。\n\n- 调研总结: Autoformalization 领域在 2025-2026 年经历爆发式发展，RL（FormaRL, Online RL）、semantic critic（CriticLean）、retrieval（DDR, DRIFT, CRAMF）、benchmark（MathAtlas, AMBER, FormalMATH）各条线独立推进。OOD domain adaptation 是公认的核心瓶颈（MathAtlas MA-Hard 仅 2.6%），但尚无工作在 test-time 同时做 retriever co-adaptation + debiased RL + semantic critic reward。Proposal 处于这些独立线索的交汇点，其组合确实尚无先例。\n\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative 是：**静态 retrieval (DDR/CRAMF) + CriticLean 作为 reranker（非 RL reward）+ 多次采样取最优**。这种 inference-time 方法无需任何权重更新，成本远低于 TTRL。\n\n具体而言：\n- DDR 已将标识符幻觉率从 30% 降至 <2%，如果静态检索已经足够好，co-adaptive retrieval 的增量可能有限\n- CriticLean 84.8% 准确率作为 filter/reranker（不作为 RL reward）+ best-of-N 采样，已经可以显著提升质量（CriticLean 论文自身报告从 54% 提升至 84%）\n- ATF 的 expert iteration + DPO 在 in-distribution 达到 94.51%，说明非 TTRL 的迭代方法也能走很远\n\n**增量价值何在**：Proposal 的增量价值集中在 **OOD 适应** 场景——当目标域与训练分布差异大时（如 condensed mathematics、algebraic geometry），静态方法的天花板明显降低。MathAtlas MA-Hard 上 2.6% 的表现证明现有方法在远 OOD 域几乎失效。TTRA 的核心价值主张是：在这些现有方法崩溃的 OOD 域上，通过 test-time weight adaptation 突破天花板。这个价值主张成立，但需要实验证明 OOD 增量是实质性的（而非 marginal）。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中，以下环节是未经验证的假设：\n\n1. **CriticLean 在 OOD 偏斜分布下仍有足够 precision**（Proposal 已识别此风险并设计 Phase 0 验证——这是正确的，但假设本身尚未验证）。CriticLeanBench 的 84.8% 准确率来自 250/250 平衡分布；在 >90% 错误的 OOD 分布下，即使 FPR 不变，precision 可能大幅下降。如果 critic precision 不足，整个 multi-tier reward 体系的基础就动摇了。\n\n2. **Lean 4 编译错误中 Tier 1 信号在目标 OOD 域上足够丰富**。AMBER 的 47.3% 数据来自 DeepSeek-R1（大模型）在应用数学域，本 proposal 使用 Qwen3-8B（小模型）在不同 OOD 域（condensed math, algebraic geometry）。小模型的错误分布可能与大模型有质的差异——小模型可能产生更多低级语法/类型错误（Tier 3），而非精确的标识符幻觉（Tier 1）。Phase -1 设计了验证，但这是关键前提。\n\n3. **TTRL 在 autoformalization 上能产生有意义的 policy improvement**。TTRL 在 informal math reasoning 上的成功依赖于 majority voting 提供的较高质量伪标签。在 autoformalization 中，伪标签质量取决于 compilation + critic 的组合准确性。如果 OOD 域上 <10% 的候选能编译通过（proposal 自己预期如此），GRPO 的每个 group 中 positive 样本极少，学习信号可能太弱，即使加了 DDRL 去偏也难以稳定训练。\n\n4. **Retriever co-adaptation 不会引入灾难性遗忘或漂移**。每 N_ret=50 步更新一次检索器，重建 FAISS 索引，但新检索结果可能将 formalizer 引向不同方向，形成振荡。R3 和 Reinforced-IR 在常规 NLP 任务上验证了交替优化的稳定性，但 autoformalization 的 reward landscape 更稀疏、更离散，稳定性假设需要验证。\n\n5. **Binarize-then-enrich 能有效结合 DDRL 和 GDPO 的优势**。DDRL 的去偏依赖固定 ±1 advantage，而 GDPO enrichment 在 accepted 样本内添加连续 bonus。这两种机制的交互是否真的互补（而非干扰）缺乏理论支撑，仅是直觉性的组合设计。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Proposal 的核心贡献本质上是将 4 个已有技术（TTRL, DDRL/GDPO, CriticLean, R3/Reinforced-IR 式 co-adaptive retrieval）适配并组合到 autoformalization 场景。每个单独组件都是对现有工作的适配而非从零创造：\n   - Binarize-then-enrich 是 DDRL（ACL 2026）+ GDPO（NVIDIA, Jan 2026）的组合适配，methodological novelty 有限但非 trivial\n   - Co-adaptive retrieval 借鉴 R3（NeurIPS 2025）和 Reinforced-IR（ACL 2025）的范式，应用于 Lean 4 error taxonomy 是新的应用场景\n   - CriticLean 作为 RL reward 是对 CriticLean（2025）的直接应用 + 分布偏移分析\n   \n   最具 novelty 的部分是 **Lean 4 结构化错误信号的分级利用**（Tier 1/2/3 hierarchy 用于 contrastive retriever training）——这确实没有先例，且利用了 Lean 4 特有的结构化反馈优势。但这更像是一个 domain-specific engineering insight 而非 general methodological breakthrough。\n   \n   与最近的 FormaRL（COLM 2025）、Online RL for Autoformalization（NeurIPS 2025 Workshop）、ReForm（2026）相比，TTRA 增加了 retrieval co-adaptation 和 debiased multi-tier RL，这些是真实的增量。但与 CriticLean（2025）相比，将 critic 从 reranker 变为 RL reward signal 的增量相对有限。\n   \n   总体而言，这是一篇 **well-crafted combination paper**，novelty 来自组合而非单一突破。对于 AAAI，组合创新被接受但需要实验结果证明组合的协同效应大于各组件之和。\n\n2. **Significance: 中偏强** — \n   研究问题（OOD autoformalization）的重要性得到了充分的数据支撑：MathAtlas MA-Hard 上 2.6% 的表现（arXiv 2605.14061）表明现有方法在远 OOD 域几乎完全失效；AMBER 的 47.3% 标识符幻觉率（arXiv 2602.01291）确认了问题根源。如果 TTRA 能在这些 benchmark 上实现实质性提升，其影响力是真实的。\n   \n   但影响面有一定局限：(a) 受众主要是 autoformalization + formal math 社区，虽然在增长但仍相对小众；(b) binarize-then-enrich 虽声称可推广到\"任何多层 reward 场景\"，但实际推广性需要额外实验验证；(c) co-adaptive retrieval 的 Lean 4 error taxonomy 依赖高度 domain-specific，难以直接迁移到其他任务。\n   \n   正面看：autoformalization 是通向 AI for mathematics 的关键管线，AlphaProof（Nature 2025）已证明这一方向的战略重要性。StepFun-Formalizer 被 AAAI 2026 接收也证明该方向在顶会有接受度。\n\n3. **Related Work: 强** — \n   这是该 proposal 最强的维度。Related work 覆盖极其全面，跨越 5 个研究线索（RL for autoformalization, semantic critics, debiased RL, co-adaptive retrieval, static retrieval + error analysis），引用了截至 2026 年 5 月的最新工作（MathAtlas May 2026, DDRL ACL 2026, StepFun-Formalizer AAAI 2026）。\n   \n   关键论文描述准确：CriticLean 的 84.8%/87.0% 数字、DDRL 的三组件设计、GDPO 的 per-reward 解耦归一化、AMBER 的 47.3% 数字——均经调研确认与原文一致。DDR 的 500K 数据集、R3 的 reinforced contrastive learning、FormaRL 的 GRPO + 编译/一致性 reward——定位准确。\n   \n   差异化定位清晰：与 FormaRL 的区分（无 retrieval、无 test-time）、与 Online RL for Autoformalization 的区分（training-time、无 trained critic、无 retrieval）、与 CriticLean 的区分（非 RL reward、平衡分布评估）均有说服力。\n   \n   唯一瑕疵：部分引用（如\"Online RL for Autoformalization\" Wang et al.）在公开搜索中较难找到完整信息，可能是 workshop paper 或最新 preprint，但不影响整体评估。\n\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \n这个 proposal 的核心是一篇 **well-executed combination paper**。它的 related work 覆盖和问题动机都很强（Related Work: 强，Significance: 中偏强），但 **novelty 受限于组合适配的本质**（Novelty: 中）。\n\n从 rubric 角度：方向正确、有真实的 novelty delta（特别是 Lean 4 error taxonomy 分级利用和 binarize-then-enrich），但如果核心发现是 positive（即\"更好的 retrieval + 更好的 reward + 更好的 RL 优化 = OOD 域上更好的表现\"），审稿人很可能会说 **\"I would have guessed this\"**——这将中位概率锚定在 25-35% 区间。\n\n限制上界的主要因素是 **Novelty 维度**：4 个已有技术的组合适配，即使每个适配都合理，整体仍缺乏一个 \"surprising\" 的核心发现或反直觉的 insight。系统复杂度高（Tier 1/2/3 + binarize-then-enrich 3 组件 + GDPO enrichment + progressive curriculum 4 阶段），审稿人可能质疑 ablation 能否清晰归因。\n\n向下拉的风险因素：(a) trivial alternative 威胁——静态 DDR + CriticLean reranker + best-of-N 可能在某些 OOD 域上已经足够好，削弱 TTRL 的增量价值；(b) 前提假设 #2（小模型 Tier 1 信号丰富度）和 #3（OOD 极稀疏 reward 下 GRPO 学习信号强度）如果不成立，核心机制失效。\n\n向上拉的因素：(a) autoformalization 是 2025-2026 热点方向（StepFun-Formalizer AAAI 2026 接收）；(b) proposal 的 Phase -1/Phase 0 go/no-go 设计非常成熟，contribution floor 分析确保 partial success 也可发表；(c) binarize-then-enrich 作为独立方法论贡献有一定推广价值。\n\n【主要风险】: \n1. **Novelty 不足的 \"kitchen sink\" 质疑**：审稿人可能认为这是 4 个已有技术的工程组合（TTRL + DDRL/GDPO + CriticLean + R3-style co-adaptive retrieval），每个单独适配的 novelty 有限，整体缺乏统一的 deep insight——这是 AAAI 审稿中 combination paper 最常被拒的原因。\n2. **OOD 增量被 trivial alternative 侵蚀**：如果静态 DDR + CriticLean reranker + best-of-N 在 OOD benchmark 上的表现与 TTRA 差距不大（例如 <5pp），那么引入 TTRL + co-adaptive retrieval 的巨大复杂度和计算成本就难以 justify，审稿人会要求证明 \"why do you need test-time weight adaptation when inference-time methods already work reasonably?\"\n```\n\nSources:\n- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)\n- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327)\n- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242)\n- [CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization](https://arxiv.org/abs/2507.06181)\n- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)\n- [Online Reinforcement Learning for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)\n- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)\n- [Construction-Verification/AMBER: A Benchmark for Applied Mathematics in Lean 4](https://arxiv.org/abs/2602.01291)\n- [R3: Optimizing Retrieval for RAG via Reinforcement Learning](https://arxiv.org/abs/2510.24652)\n- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)\n- [DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems](https://arxiv.org/abs/2510.10815)\n- [StepFun-Formalizer: AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40691)\n- [ReForm: Reflective Autoformalization](https://arxiv.org/abs/2510.24592)\n- [TTARAG: Test-Time Adaptation for RAG](https://arxiv.org/abs/2601.11443)\n- [NVlabs/GDPO GitHub](https://github.com/NVlabs/GDPO)\n- [THUNLP-MT/FormaRL GitHub](https://github.com/THUNLP-MT/FormaRL)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization\n\n## Core Problem\n\nCurrent autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning dramatically but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in the multi-tier reward setting (compilation + critic + BEq); and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation, yet no prior work fine-tunes the retriever during test-time RL. Can we make TTRL viable for autoformalization by combining compilation-error-driven co-adaptive retrieval that exploits Lean 4's full structured error taxonomy, a calibrated semantic critic reward, and principled adaptation of binary-reward debiased RL to multi-tier rewards?\n\n## Research Opportunity\n\nFour independently validated capabilities have never been combined: (1) Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode. R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv 2601.11443, Jan 2026) shows test-time retrieval adaptation is achievable via self-supervised prediction. Critically, the prevalence of identifier hallucination as the dominant error class is now established by converging evidence from multiple independent studies: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) provides the strongest quantitative evidence, finding that 47.3% of 3,189 sampled compilation errors from DeepSeek-R1 on applied mathematics domains stem from 'invocation of non-existent theorems or definitions'—directly exceeding Phase -1's ≥40% Tier 1 threshold. DDR (arXiv 2511.11990) quantifies that ICL-based dependency generation produces ~30% hallucinated (non-existent) Mathlib identifiers (Hall_m=0.21-0.39 across frontier LLMs), while retrieval-based DDR reduces hallucination to <2% (Hall_m=0.016). The RAutoformalizer (ICLR 2025 Spotlight) explicitly classifies compilation errors into 'Hallucination' (errors caused by hallucination of identifiers) and 'Others', establishing identifier hallucination as a primary error class. MathAtlas (May 2026) further shows a 66% performance advantage for Mathlib-grounded definitions (27.9% vs 16.8% correct, p<0.001), confirming that dependency availability is the critical bottleneck. Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL-based autoformalization—where Lean's structured error taxonomy (unknownIdentifier, type mismatch with type signatures, failed to synthesize with typeclass names, unknown namespace) provides a graded hierarchy of machine-parseable signals for retriever training. (2) TTRL with debiasing has advanced rapidly. DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed +/-1 advantages, and consensus-based off-policy refinement, achieving up to 19.0% relative improvement over ETMR on AIME 2024 (4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B). But DDRL assumes binary correct/incorrect rewards. GDPO (NVIDIA, arXiv 2601.05242, Jan 2026) addresses multi-reward GRPO through per-reward decoupled normalization, preventing reward signal collapse. The combination—binarize multi-tier rewards for DDRL's debiasing, then enrich with GDPO's per-reward normalization for continuous components—has not been attempted. (3) CriticLean (July 2025) provides the missing reward signal: CriticLeanGPT-14B-RL achieves 84.8% accuracy on CriticLeanBench (87.0% for the 32B variant), raising autoformalization pipeline accuracy from 54% to 84% over compilation-only feedback. However, CriticLeanBench evaluates on a balanced 250-correct/250-incorrect distribution, while OOD TTRL produces heavily skewed distributions (often <10% compilable candidates). This distributional shift gap has not been characterized, motivating our Phase 0 calibration protocol. (4) Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) validates RL for autoformalization (TC1: 17.29% to 26.01% on RLMEval using GRPO with composite BEq + embedding rewards), but operates at training time with labeled/unlabeled data on in-distribution problems, without retrieval, test-time adaptation, or a trained semantic critic. Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.\n\n## Research Landscape\n\nThe landscape spans five relevant lineages. (1) RL for autoformalization: FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards, improving pass@1 from 4% to 26% on ProofNet. Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with composite rewards (BEq + embedding-based similarity) for Lean 4, achieving TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46% on RLMEval—the closest prior work but operates at training time on in-distribution problems, uses embedding similarity rather than a trained semantic critic, and lacks retrieval and test-time adaptation. ReForm (2026) applies position-aware RL rewards for reflective autoformalization (+22.6pp average). (2) Semantic critics and iterative refinement: CriticLean (July 2025) introduces CriticLeanGPT, with the 32B-RL variant achieving 87.0% accuracy and the 14B-RL variant reaching 84.8% on the balanced CriticLeanBench (250 correct, 250 incorrect). The paper reports TPR, FPR, TNR, and FNR metrics but evaluates only on balanced distributions, leaving the heavily skewed OOD regime uncharacterized. ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO with multi-LLM consistency checking. Monotonic Refinement achieves 90.27% composite on miniF2F through multi-model ensemble orchestration. These achieve impressive results but cannot adapt model weights to new domains. (3) Debiased RL and multi-reward optimization: DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification through three components: frequency-based balanced sampling excluding ambiguous samples, fixed +/-1 advantages, and consensus-based off-policy refinement—achieving up to 19.0% relative improvement over ETMR on AIME 2024 (4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B; the TTRL baseline without debiasing scores 15.8, illustrating the severity of signal amplification that DDRL corrects). Critically, DDRL operates exclusively with binary rewards and its authors note that 'more expressive advantage formulations' are left for future work. GDPO (NVIDIA, arXiv 2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization, demonstrating that standard GRPO collapses distinct reward combinations into identical advantage values. (4) Co-adaptive retrieval: R3 (NeurIPS 2025) optimizes retrieval for RAG via reinforced contrastive learning. Reinforced-IR (ACL 2025) alternates RLRF and RLGF for mutual adaptation. TTARAG (arXiv 2601.11443) demonstrates test-time adaptation for RAG. None of these have been applied to autoformalization or Lean 4. (5) Static retrieval, error analysis, and identifier hallucination quantification for autoformalization: The Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) provides the most comprehensive error taxonomy to date: analyzing 3,189 sampled compilation errors from DeepSeek-R1 on applied math (convex analysis, optimization, numerical algebra, high-dimensional probability), they find 47.3% are hallucination of non-existent theorems/definitions, 32.7% are formalization competence errors, 15.2% are incomplete outputs, and 4.8% are formatting/syntax—concluding that 'future improvements should prioritize retrieval-augmented generation or specialized fine-tuning.' DDR builds a 500K-sample dependency dataset and quantifies that ~30% of ICL-generated dependencies are hallucinated identifiers (Hall_m ranging 0.21-0.39 across frontier LLMs), reduced to <2% with retrieval-based DDR. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF but falls short on ProofNet (21.93% vs 27.54%). CRAMF indexes 26K+ Mathlib definitions for concept-level retrieval, documenting that models fabricate identifiers like 'Function.Continuous' instead of 'ContinuousOn' and 'Group.index' instead of 'Subgroup.index'. MathAtlas (May 2026) introduces 52K graduate-level problems where the best model achieves only 2.6% on MA-Hard and adding local context degrades prompted systems' performance. The RAutoformalizer (ICLR 2025 Spotlight) explicitly categorizes compilation errors into 'Hallucination' (identifier hallucination) vs 'Others', establishing that identifier-related errors constitute a major error class. After exhaustive search through May 2026, no work combines (a) co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, (b) a calibrated semantic critic as RL reward with distributional shift analysis, (c) principled adaptation of binary-reward debiased RL to multi-tier rewards, and (d) test-time adaptation on fully unlabeled OOD domains.\n\n## Proposed Approach\n\nWe propose TTRA (Test-Time Retrieval-Augmented autoformalization), a framework that makes TTRL viable for autoformalization through three technical innovations: (1) a dual-loop architecture with co-adaptive retrieval exploiting Lean 4's full structured error taxonomy, (2) integration of CriticLean-14B as semantic RL reward with explicit calibration under distributional shift, and (3) a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards using GDPO's per-reward decoupled normalization.\n\n**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Before committing to the pipeline design, we quantify the retrieval signal coverage that Lean 4's error taxonomy provides on OOD domains. We compile 500 candidate formalizations from an existing model (e.g., FormaRL or Kimina-7B) on Con-NF (OOD) and 500 on MathAtlas MA-Hard, collecting all compilation error messages. We classify each error into the following hierarchy:\n  (a) Tier 1 — Direct identifier signals: `lean.unknownIdentifier` (names the missing constant), `unknown namespace` (names the namespace). These provide direct, machine-parseable mapping from error to needed Mathlib dependency.\n  (b) Tier 2 — Type-based signals: `type mismatch` (contains expected vs actual type signatures), `failed to synthesize instance` (names the typeclass). These provide weaker but still informative retrieval signals—type signatures can be matched against Mathlib's type index, and typeclass names map to specific Mathlib modules.\n  (c) Tier 3 — Indirect signals: tactic failures, elaboration errors, syntax errors. These provide no direct retrieval signal but can serve as negative examples (confirming that retrieved dependencies were insufficient).\n  Quantitative thresholds: If Tier 1 errors constitute ≥40% of compilation failures, the co-adaptive retrieval mechanism is well-supported as designed. If Tier 1 is 20-40%, we rely on both Tier 1 and Tier 2 signals (requiring the type-signature matching extension). If Tier 1 is <20%, we must fall back primarily to Tier 2 signals with type-signature-based retrieval. Prior evidence now strongly supports ≥40%: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291) finds that 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math domains are hallucination of non-existent theorems/definitions—directly exceeding the ≥40% threshold on an OOD domain. DDR shows ~30% of ICL-generated dependencies are hallucinated identifiers (Hall_m=0.21-0.39 across frontier LLMs), the RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' (identifier hallucination) as one of two major error classes, and CRAMF documents systematic fabrication of close-but-wrong identifiers. Phase -1 nonetheless remains essential because AMBER's error distribution is from DeepSeek-R1 on applied math, and our pipeline uses a smaller formalizer on different OOD domains (condensed mathematics, algebraic geometry)—the error distribution may differ. Resource: ~8 A100-hours for generation, ~10 CPU-hours for compilation and error parsing. No model training required.\n\n**Phase 0 — Minimal Pilot Experiment with Critic Calibration (De-risking).** Before committing to the full pipeline, we validate two riskiest assumptions with a minimal experiment. Setup: Take FormaRL's GRPO pipeline, replace its LLM-consistency reward with CriticLean-14B as the sole semantic reward signal (reward = r_compile × r_critic). Data: 200 problems from Con-NF (OOD) + 200 from FormalMATH number theory (near-distribution). No retrieval, no curriculum, no DDRL debiasing—just vanilla GRPO with the critic reward.\n  Primary hypothesis: if CriticLean-14B reward achieves ≥3pp BEq@1 improvement over compilation-only GRPO on Con-NF, the core premise (semantic critic rewards enable OOD adaptation) is validated.\n  Secondary hypothesis — Critic calibration under distributional shift: We explicitly measure CriticLean-14B's precision and recall SEPARATELY on the skewed distribution produced during TTRL. Specifically: (a) Among K=32 candidates per problem, record the number that compile and the number the critic approves. (b) For problems where <10% of candidates compile (the regime expected on hard OOD domains), manually inspect 100 random critic-approved candidates and 100 critic-rejected candidates to compute precision and recall in this hardest regime. (c) Report calibration curves: for each critic confidence bin (if logit-based confidence is available from the critic model), plot the empirical correctness rate. Key concern: on CriticLeanBench's balanced 250/250 distribution, 84.8% accuracy could correspond to very different precision/recall trade-offs. Under OOD TTRL's heavily skewed distribution (90%+ incorrect), even moderate false positive rates could produce substantial noise. Our conservative binarization (requiring BOTH compile AND critic approval) inherently prioritizes precision over recall—a candidate must pass two independent filters. If critic precision on the skewed distribution is <80% (i.e., >20% of critic-approved compilable candidates are semantically wrong), we introduce critic confidence gating: only accept critic judgments with confidence >0.8, trading recall for precision.\n  Resource: ~50 A100-hours (increased from 40 to include calibration analysis), 2-3 weeks. Go/no-go decision: proceed only if primary hypothesis confirmed AND critic precision on the skewed distribution ≥80% (or ≥80% with confidence gating).\n\n**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune a Qwen3-8B base model as a retrieval-augmented autoformalizer using DDR's 500K-sample dependency dataset and GRPO with the multi-tier reward function R(y, x) = r_compile × (α·r_critic + β·r_beq), where: r_compile ∈ {0,1} is the Lean 4 compilation gate (verified via Kimina Lean Server with 128 parallel pre-warmed REPL workers); r_critic ∈ {0,1} is the semantic fidelity judgment from CriticLeanGPT-Qwen3-14B-RL, gated by the confidence threshold established in Phase 0; r_beq ∈ [0,1] is the BEq consensus density (fraction of compilable candidates in the same BEq equivalence class). We set α=0.7, β=0.3 to weight semantic fidelity over syntactic consensus, since BEq has high precision (98.6%) but low recall (~33% on ProofNet). Adaptive reward degradation: when fewer than M=4 candidates out of K=32 compile, BEq becomes degenerate, and the reward falls back to R = r_compile × r_critic.\n\n**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever is a DDR-style dense encoder whose parameters ARE updated during TTRL—not frozen. This exploits a key structural property: Lean 4's type checker produces machine-parseable error messages with a hierarchy of retrieval informativeness.\n\n  Loop 1 — Formalizer GRPO (every step): Generate K=32 candidate formalizations per problem, compile each against Lean 4, compute multi-tier rewards, and perform debiased GRPO updates (Phase 3).\n\n  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Accumulated compilation feedback generates contrastive training data for the retriever using a graded error signal hierarchy:\n    (a) Tier 1 — Direct identifier signals (highest confidence): When a formalization fails with `lean.unknownIdentifier` (tagged with `unknownIdentifierMessageTag`), the error explicitly names the missing Mathlib constant (e.g., 'unknown identifier Finset.sum_comm'). The dependencies that WERE retrieved but did NOT include this constant are hard negatives. The missing constant—looked up in the CRAMF/DDR Mathlib constant index—becomes the positive example. When the error is `unknown namespace`, the namespace maps to a Mathlib module, providing a coarser positive signal.\n    (b) Tier 2 — Type-based signals (moderate confidence): When a formalization fails with `type mismatch`, the error contains expected vs actual type signatures. We match these type signatures against Mathlib's type index (built from DDR's 500K-sample dataset) to identify candidate dependencies that would resolve the mismatch, generating softer positive examples with reduced weight (0.5× in the InfoNCE loss). When `failed to synthesize instance` names a typeclass, we retrieve Mathlib instances of that typeclass as positives.\n    (c) Tier 3 — Negative confirmation from non-identifier errors: Tactic failures, elaboration errors, and syntax errors do not provide positive retrieval signals but confirm that the retrieved dependency set was insufficient for reasons beyond identifier resolution. These contribute only negative examples to the contrastive loss.\n    (d) Positive confirmation from successful compilations: When a formalization compiles successfully, all retrieved Mathlib dependencies that appear in the compiled formalization are confirmed positives.\n    (e) Weighted InfoNCE contrastive loss: L_InfoNCE = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), where w_k = 1.0 for Tier 1 positives, w_k = 0.5 for Tier 2 positives, w_k = 1.0 for compilation-confirmed positives, and τ is the temperature (initialized at 0.07).\n    (f) Decoupled optimization: The retriever's gradient does NOT flow through the formalizer's policy gradient. This alternating optimization prevents instability, following R3 (NeurIPS 2025) and Reinforced-IR (ACL 2025). After each retriever update, the FAISS index over Mathlib dependency embeddings is rebuilt.\n\n  The graded error signal hierarchy ensures the retriever update loop has sufficient signal even on the hardest OOD domains where pure unknownIdentifier errors may be sparse. Phase -1's micro-analysis determines the empirical signal mix, allowing the weighting scheme to be calibrated before full-scale experiments.\n\n**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** DDRL's three-component fix was designed for binary correct/incorrect rewards on informal math. Autoformalization's multi-tier reward has a continuous range. We adapt via binarize-then-enrich:\n\n  (a) Binarization layer (for DDRL compatibility): Define binary acceptance r_accept = I(r_compile=1 AND r_critic=1). Compilation is a non-negotiable binary gate; the critic's precision (characterized in Phase 0 under distributional shift) makes it the most informative signal after compilation.\n    - Balanced sampling: Partition K=32 candidates into 'accepted' (compile + critic approves) and 'rejected' (otherwise). Exclude problems where acceptance frequency is in the ambiguous zone (30-70%, i.e., ~10-22 of 32 accepted), following DDRL's insight that medium-consistency samples are the primary source of reward noise.\n    - Fixed advantages: A_i = +1 for accepted candidates, A_i = -1 for rejected, eliminating GRPO's group-relative normalization that DDRL identifies as the amplification pathway.\n    - Consensus-based off-policy refinement: After each TTRL epoch, sample M=128 formalizations per problem, apply acceptance filtering, perform rejection sampling on high-confidence samples (>80% acceptance rate), and run SFT on this high-quality dataset for 5 epochs.\n  (b) GDPO-style enrichment layer (for BEq signal preservation): Among accepted candidates only, apply per-reward decoupled normalization for the BEq component. The BEq consensus density is normalized independently, preserving its ranking information without collapsing it into the binary acceptance signal. This adds an additive gradient bonus δ·norm(r_beq) to the fixed +1 advantage for accepted candidates, where δ=0.3 scales the enrichment relative to the debiased signal.\n  (c) Methodological contribution: This binarize-then-enrich adaptation from single-reward to multi-tier debiased RL is applicable beyond autoformalization to any multi-tier reward where one component is continuous and others are binary.\n\n**Phase 4 — Progressive Domain Curriculum for Test-Time Adaptation.** To break the bootstrapping problem (poor OOD retrieval → bad formalizations → noisy rewards → failed adaptation), we apply a progressive curriculum with quantitative transition criteria:\n\n  (a) Near-distribution warm-start: TTRL on domains close to training data where retrieval coverage is high. Transition criterion (a)→(b): compilation rate ≥40%, critic approval rate ≥60% among compilable candidates, BEq@32 improves ≥3pp over pre-adaptation baseline. Timeout: T_max=500 GRPO steps.\n  (b) Retrieval bootstrapping: Use the adapted model to generate improved formalization attempts on moderately OOD domains. Failed attempts with structured error signals (Tier 1 and Tier 2) feed the retriever's contrastive updates (Phase 2). Transition criterion (b)→(c): retrieval recall@10 ≥30% on bootstrapped queries, compilation rate on moderate-OOD ≥25%. Early transition: compilation rate plateaus (<2pp improvement over 200 consecutive steps).\n  (c) Far-OOD adaptation: TTRL on truly OOD domains (algebraic geometry, condensed mathematics, MathAtlas MA-Hard) using the bootstrapped retriever and adaptive reward fallback (R = r_compile × r_critic when <4 candidates compile).\n\n**Contribution Floor Analysis.** The three innovations are designed to be synergistic but are independently valuable, ensuring the paper makes a publishable contribution even under partial success:\n  (1) Co-adaptive retrieval alone (Phase 2) + CriticLean TTRL (Phase 0-1): If binarize-then-enrich (Phase 3) provides only marginal gains over vanilla GRPO or plain DDRL, the paper still contributes the first co-adaptive retrieval mechanism for autoformalization exploiting Lean 4's structured error taxonomy, and the first application of TTRL to formal mathematics with a calibrated semantic critic. The co-adaptive retriever is an independent module that can be integrated into any RL-based autoformalization pipeline.\n  (2) Binarize-then-enrich alone (Phase 3): If co-adaptive retrieval provides marginal gains (e.g., because static retrieval is already sufficient for near-OOD domains), the binarize-then-enrich adaptation of DDRL to multi-tier rewards is a standalone methodological contribution applicable to any domain with mixed binary/continuous rewards—not limited to autoformalization.\n  (3) Progressive curriculum alone (Phase 4): If both innovations work but the curriculum provides marginal improvement over direct OOD adaptation, dropping Phase 4 simplifies the pipeline without losing the core contributions.\n  (4) Essential floor: The minimal publishable contribution requires that CriticLean-guided TTRL outperforms compilation-only TTRL on OOD domains (validated in Phase 0) AND at least one of co-adaptive retrieval or binarize-then-enrich provides statistically significant improvement over the CriticLean TTRL baseline. Phase 0's go/no-go gate ensures we do not invest in the full pipeline unless the foundational premise holds.\n\n**Evaluation.** Measure BEq@K and compilation success on FormalMATH's 5,560-problem multi-domain benchmark, Con-NF, CombiBench, and MathAtlas's MA-Hard (700 entities, average dependency depth 30, best current model: 2.6%).\n  Same-scale comparisons (primary, all ~7-8B parameter models): (1) FormaRL (Qwen2.5-Coder-7B) as RL-without-retrieval baseline, (2) Online RL for Autoformalization (Wang et al.) as training-time RL baseline with composite rewards, (3) DRIFT with Qwen3-8B as strongest static retrieval baseline, (4) compilation-only TTRL and critic-only TTRL ablations, (5) standard GRPO vs. DDRL debiased vs. binarize-then-enrich (with separate ablations for each DDRL component and the GDPO enrichment layer), (6) frozen retriever vs. co-adaptive retriever during TTRL (isolating the value of compilation-error-driven retriever updates from natural query improvement), (7) Tier 1-only vs. Tier 1+2 vs. all-tier error signals (isolating the value of the graded error hierarchy), (8) no curriculum vs. progressive curriculum.\n  Cross-scale reference points (for contextualizing absolute performance, NOT for claiming superiority): (9) ATF-32B as iterative refinement SOTA (94.51%/65.38% FormalMath-Lite/CombiBench), (10) ATLAS as SFT-only reference (70.08% pass@1 miniF2F), (11) Monotonic Refinement as inference-time orchestration upper bound (90.27% miniF2F, multi-model ensemble with GPT-4+ level models). All evaluation tables explicitly annotate model scale and compute budget to ensure fair interpretation.\n  Sensitivity analysis: Dedicated ablation for N_ret ∈ {25, 50, 100} (retriever update frequency), as this controls the retriever-formalizer alternation and is critical for stability.\n\n## Detailed Description\n\nCurrent autoformalization models achieve strong in-distribution results but collapse on unfamiliar mathematical domains due to missing domain-specific Mathlib dependencies and fixed inference-time behavior. We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a framework making TTRL viable for autoformalization through three technical innovations. First, a dual-loop co-adaptive retrieval architecture where a DDR-style dense retriever is explicitly fine-tuned during test-time RL using a graded hierarchy of Lean 4 compilation error signals: Tier 1 signals from `lean.unknownIdentifier` errors (which explicitly name the missing Mathlib constant, providing direct hard negatives for InfoNCE training), Tier 2 signals from type mismatches and failed typeclass synthesis (providing softer retrieval signals via type-signature matching), and Tier 3 negative confirmation from other errors. This graded hierarchy addresses the key concern that not all OOD errors produce clean identifier signals—the prevalence of identifier errors is now established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are hallucination of non-existent theorems/definitions, DDR shows ~30% of ICL-generated dependencies are hallucinated identifiers, and the RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as one of two primary error classes. A Phase -1 micro-analysis (2-3 days, ~8 A100-hours) validates the error distribution on our specific OOD benchmarks before committing to the pipeline. Second, integration of CriticLean-14B (84.8% accuracy on balanced CriticLeanBench) as semantic RL reward, with explicit calibration under distributional shift: Phase 0 measures the critic's precision and recall SEPARATELY on the heavily skewed distribution expected during OOD TTRL (where >90% of candidates may be incorrect), reports calibration curves, and establishes a confidence gating threshold to maintain precision ≥80%—the conservative binarization (requiring BOTH compile AND critic approval) inherently prioritizes precision over recall. Third, a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards: binary acceptance (compile AND critic approval) provides DDRL's frequency-based balanced sampling and fixed ±1 advantages for debiasing, while GDPO-style per-reward decoupled normalization preserves BEq consensus density as a secondary ranking bonus among accepted candidates—this adaptation is itself a methodological contribution applicable beyond autoformalization. A progressive domain curriculum with quantitative transition criteria breaks the bootstrapping problem on OOD domains. Crucially, the three innovations are independently valuable: if binarize-then-enrich provides marginal gains, the paper still contributes the first co-adaptive retrieval for autoformalization and the first TTRL application to formal math with a calibrated semantic critic; if co-adaptive retrieval is marginal, binarize-then-enrich stands as a general methodology for multi-tier debiased RL. This contribution floor ensures publishable results even under partial success, with Phase 0's go/no-go gate preventing wasted effort on the foundational premise. Evaluation spans FormalMATH, Con-NF, CombiBench, and MathAtlas MA-Hard (best current: 2.6%), with same-scale comparisons (FormaRL, Online RL, DRIFT, ablations on error tiers and N_ret sensitivity) explicitly separated from cross-scale reference points (ATF-32B, Monotonic Refinement) to ensure fair interpretation. N_ret=50 GRPO steps between retriever updates is justified by signal accumulation: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle, sufficient for stable InfoNCE learning.\n\n## Key References\n\n- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)\n- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)\n- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv 2601.05242, NVIDIA, January 2026)\n- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv 2507.06181, ByteDance/Nanjing)\n- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)\n- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv 2510.24652)\n- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)\n- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv 2601.11443, January 2026)\n- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv 2602.01291, February 2026)\n- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)\n- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\n- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)\n- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)\n- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\n- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)\n- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv 2025)\n- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)\n- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)\n- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)\n- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\n- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\n- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2605.14061, May 2026)\n- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\n- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\n- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\n- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025)\n- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv 2512.00997, Microsoft Research)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 950-1400 A100-80GB hours (Phase -1 error micro-analysis: ~8h; Phase 0 pilot with critic calibration: ~50h; base formalizer GRPO training with multi-tier reward: ~300h on 8 GPUs; DDR retriever fine-tuning + co-adaptive contrastive updates: ~100h on 4 GPUs; TTRL progressive adaptation across 3 curriculum stages with binarize-then-enrich DDRL and ablations: ~400h on 4 GPUs; CriticLean-14B inference during training: ~60h on 2 GPUs; N_ret sensitivity analysis: ~50h; error tier ablation: ~40h; evaluation: ~80h) + 10,000-15,000 CPU-hours for Lean 4 verification (128 parallel workers via Kimina Lean Server), timeline: 12-16 weeks (0.5 wk Phase -1 micro-analysis, 2-3 wk Phase 0 pilot + critic calibration + go/no-go, 3 wk base training + critic integration, 2 wk retriever co-adaptation infrastructure, 4 wk progressive TTRL experiments, 2-3 wk ablations including N_ret sensitivity and error tier analysis, 2 wk writing), estimated_gpu_cost: $1,900-$3,500 at ~$2.00/A100-hr + ~$500-$750 CPU verification costs\n- **human_in_loop**: gpu_hours: 750-1100 A100-80GB hours (Claude handles Phase -1 analysis, Phase 0 calibration analysis, experiment scheduling; reduced ablation overhead ~25%) + 8,000-12,000 CPU-hours for Lean verification, timeline: 9-12 weeks (0.5 wk Phase -1; 2 wk Phase 0 with Claude-assisted calibration analysis; 3 wk base training + co-adaptive retriever; 3 wk progressive TTRL; 2-3 wk ablations + writing), claude_api_cost: $400-$700 (critic reward calibration, Phase -1/0 analysis, automated curriculum scheduling, ablation analysis), estimated_gpu_cost: $1,500-$2,700 + ~$400-$600 CPU costs\n- **auto_research**: gpu_hours: 1600-2200 A100-80GB hours (automated hyperparameter sweeps over N_ret ∈ {25,50,100}, InfoNCE temperature τ, Tier 1/2 weighting, DDRL binarization ambiguity zone, GRPO group sizes K ∈ {16,32,64}, curriculum transition thresholds, enrichment weight δ, critic confidence threshold, plus multi-seed evaluation) + 20,000-30,000 CPU-hours for Lean verification at scale, timeline: 6-9 weeks (highly parallelized; Phase -1 in day 1-2 with automatic error taxonomy analysis; Phase 0 pilot in week 1-2 with automatic go/no-go gate and calibration analysis; wall-clock bottleneck is Lean 4 verification, mitigated by 128+ Kimina Lean Server workers), claude_api_cost: $800-$1,200 (automated experiment design, Phase -1/0 analysis, reward function ablation, curriculum optimization, paper drafting), estimated_gpu_cost: $3,200-$5,500 + ~$1,000-$1,500 CPU costs, speed_bottleneck: Lean 4 compilation latency (~3.65s per statement with warm LRU cache; ~0.10s amortized at 64 workers) dominates reward computation. CriticLean-14B inference adds ~0.5s per candidate on A100. Retriever co-adaptation adds ~15 min per update cycle (every N_ret GRPO steps) for re-encoding 26K Mathlib constants and rebuilding FAISS index.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-28T05:24:43.942Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:24:43.942Z",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-28T05:24:43.978Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide my evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084) (NeurIPS 2025): 在无标签数据上通过多数投票伪标签进行 GRPO 训练，Qwen2.5-Math-7B 在 AIME 2024 上从 16.7%→43.3%。本 proposal 的基础框架，但 TTRL 仅用于非形式化数学推理，依赖数值答案的多数投票——这正是 proposal 要解决的问题之一（形式化语句无法直接做 majority voting）。

- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327) (ACL 2026 Findings): 诊断并修复 GRPO 在 TTRL 中的 spurious signal amplification，提出 frequency-based balanced sampling + fixed ±1 advantages + consensus-based off-policy refinement。在 AIME 2024 上相对 TTRL baseline（15.8→25.0 for Qwen2.5-Math-1.5B）提升显著。**但仅支持 binary rewards**，其作者明确将 multi-reward 扩展留作 future work。proposal 的 "binarize-then-enrich" 正是回应这一 gap。

- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242) (NVIDIA, Jan 2026): 发现 GRPO 在 multi-reward 场景下会将不同 reward 组合 collapse 成相同 advantage 值，提出 per-reward decoupled normalization。已在 tool calling、math reasoning、coding 上验证。proposal 借用其 per-reward normalization 作为 enrichment layer。

- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181) (ByteDance/Nanjing, July 2025): 训练 CriticLeanGPT-14B-RL 达到 84.8% accuracy（32B 版本 87.0%），将 autoformalization pipeline 准确率从 54%→84%。但仅在 balanced 250/250 分布上评估，OOD 场景下的 skewed distribution 表现未知。proposal 的 Phase 0 calibration 正是针对此 gap。

- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914) (COLM 2025): 首个将 GRPO+compilation reward 用于 autoformalization，Qwen2.5-Coder-7B 在 ProofNet 上从 4%→26%。但使用 LLM consistency 作为语义 reward（而非 trained critic），且无 retrieval，仅在 in-distribution 场景。

- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization) (Wang et al., NeurIPS 2025 MAR Workshop): 使用 GRPO + composite BEq+embedding rewards 在 Lean 4 上做 autoformalization RL，TC1: 17.29%→26.01%。**最近的 baseline**，但属于 training-time RL，使用 embedding similarity 而非 trained critic，无 retrieval 和 test-time adaptation。

- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990) (2025): 构建 500K 样本依赖数据集，量化 ICL 生成的依赖中~30% 为 hallucinated identifiers（Hall_m=0.21-0.39），retrieval-based DDR 将 hallucination 降至 <2%。proposal 使用其数据集和 retriever 架构作为起点。

- [Construction-Verification/AMBER Benchmark](https://arxiv.org/abs/2602.01291) (Yang et al., Feb 2026): 在 applied math 领域分析 3,189 个编译错误，发现 47.3% 为 hallucination of non-existent theorems/definitions。这是 proposal 关于 "identifier hallucination 是 dominant error mode" 的最强实证支撑。

- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652) (NeurIPS 2025): 通过 trial-and-feedback reinforced contrastive learning 优化 RAG 环境中的 retriever。proposal 的 co-adaptive retrieval 借鉴其 contrastive learning 框架，但应用到完全不同的 domain（Lean 4 dependency retrieval）。

- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061) (May 2026): 52K graduate-level 问题，最佳模型仅 9.8% correctness on theorems，MA-Hard 上 2.6%。验证了 OOD autoformalization 仍是极具挑战性的开放问题。

- 调研总结: Autoformalization 领域在 2025-2026 经历快速发展：RL-based 方法（FormaRL, Online RL）已初步验证，semantic critic（CriticLean）提供了编译之外的 reward 信号，static retrieval（DDR, DRIFT, CRAMF）大幅降低了 identifier hallucination，TTRL 在非形式化数学推理中取得突破。但**尚无工作将 TTRL 应用于 autoformalization，尚无工作在 RL 过程中对 retriever 做 co-adaptive 更新，尚无工作将 DDRL 的 binary debiasing 扩展到 multi-tier rewards**。Proposal 定位在这三个 gap 的交叉点上。

【Trivial Alternative 检验】:

最直接的 trivial alternative 是：**static DDR retrieval + CriticLean reward + vanilla GRPO（不做 co-adaptive retrieval，不做 DDRL debiasing）**。这基本上是把 FormaRL 的 reward 换成更好的 CriticLean，再加上 DDR 提供的 Mathlib 依赖。

这个 trivial baseline 的关键弱点在于：
1. **Static retrieval 在 OOD 域会失效**：DDR 的 retriever 在训练数据分布上训练，面对 condensed mathematics 或 algebraic geometry 等 far-OOD 域，retrieval recall 会显著下降，因为 query distribution 发生了 shift。这是 co-adaptive retrieval 的核心增量价值——retriever 随 formalizer 的行为变化而适应。
2. **Vanilla GRPO 在低 consensus 场景会放大噪声**：DDRL 已经实证证明了这一点（AIME 2024 上 TTRL baseline 仅 15.8 vs DDRL 的 25.0）。在 autoformalization 的 OOD 场景中，compilable rate 很低，consensus 更差，噪声放大问题会更严重。

但也必须承认：**在 near-OOD 域，static retrieval + CriticLean + vanilla GRPO 可能已经足够好**。Proposal 的增量价值主要体现在 far-OOD 场景。如果实验发现大多数 benchmark 属于 near-OOD，co-adaptive retrieval 和 DDRL debiasing 的 marginal gain 可能很小。

**增量价值判断**：co-adaptive retrieval 是最有说服力的增量贡献（问题明确、机制新颖、利用了 Lean 4 独特的结构化错误信息）。Binarize-then-enrich 的增量价值较弱（在 DDRL 和 GDPO 都已存在的前提下，这一步近乎 obvious）。

【前提假设检验】:

核心 claim 的逻辑链中，以下环节是未经验证的假设：

1. **"CriticLean-14B 在 OOD skewed distribution 下仍能保持足够的 precision"**：CriticLeanBench 仅在 balanced 250/250 分布上评估（84.8% accuracy）。在 TTRL 的 OOD 场景下，>90% 的 candidate 可能不正确，critic 的 false positive rate 可能会显著恶化。Proposal 的 Phase 0 calibration 试图验证这一假设，但这也意味着**如果这个假设不成立，整个 pipeline 的基础就会动摇**。这是最关键的风险点。

2. **"Lean 4 的 unknownIdentifier 等 Tier 1 错误在 OOD 域占比足够高（≥40%）以支撑 co-adaptive retrieval"**：AMBER 的 47.3% 来自 DeepSeek-R1 on applied math，但 proposal 使用更小的 formalizer 在不同 OOD 域上。Proposal 承认了这一点（Phase -1 就是为了验证），但如果 Tier 1 比例很低（如 <20%），co-adaptive retrieval 的 core mechanism 会大打折扣。

3. **"co-adaptive retriever 更新不会 destabilize RL training"**：交替优化 retriever 和 formalizer 在理论上可能导致不稳定——retriever 变化改变 input context → formalizer 的 reward landscape 发生 shift → GRPO 的 advantage estimation 受到干扰。Proposal 借鉴 R3 和 Reinforced-IR 的 decoupled optimization，但这些工作是在 text QA 领域验证的，autoformalization 场景的 reward 更加 sparse 和 noisy，是否同样稳定未经验证。

4. **"Binarize-then-enrich 的 DDRL 扩展在 multi-tier reward 场景下能保持 DDRL 的 debiasing 效果"**：DDRL 的理论分析基于 binary reward 的简洁结构（correct/incorrect）。加入 GDPO enrichment layer 后，fixed ±1 advantages 被 BEq bonus 打破，debiasing 的理论保证是否仍然成立是一个开放问题。

【3 维度打分】:

1. **Novelty: 中** — 
   Co-adaptive retrieval exploiting Lean 4's structured error taxonomy 是最强的新颖贡献：没有先前工作在 RL-based autoformalization 过程中对 retriever 做 online adaptation，利用 unknownIdentifier/type mismatch 等结构化错误信号构建 graded contrastive training data 的设计是 domain-specific 且有新意的。这一点与 R3 (NeurIPS 2025) 和 Reinforced-IR (ACL 2025) 在 text QA 上的 co-adaptive retrieval 形成清晰区分——后者不涉及编译器的结构化错误信号。

   但整体而言，proposal 的 novelty 分布不均匀。"Binarize-then-enrich" 的贡献较薄：一旦知道 DDRL 处理 binary rewards、GDPO 处理 multi-reward normalization，将二者组合（先 binarize 使 DDRL 适用，再用 GDPO 对 continuous component 做 enrichment）是一个**几乎 obvious 的工程决策**，缺乏深层 insight。CriticLean 作为 TTRL reward 也是自然的应用延伸（CriticLean 论文本身就在 RL pipeline 中使用了 critic reward）。

   此外，TTRL 应用于 autoformalization 虽然是"首次"，但 Online RL for Autoformalization (Wang et al.) 已经做了 training-time RL for autoformalization with composite rewards，从 training-time 到 test-time 的跨越虽有价值但不构成根本性 novelty 突破。

   **总体判断**：有一个扎实的新贡献点（co-adaptive retrieval with error taxonomy），其余贡献是competent combination work。对于 AAAI，这处于中等水平——不是 trivial incremental，但也达不到 "surprising insight"。

2. **Significance: 中偏强** — 
   Autoformalization 的 OOD generalization 是一个真实且重要的问题。MathAtlas (2026) 显示最佳模型在 MA-Hard 上仅 2.6%，AMBER (2026) 量化了 47.3% 的编译错误来自 identifier hallucination——**问题的重要性和 urgency 是有充分实证支撑的**。

   如果 proposal 的方法在 far-OOD 域（condensed mathematics, algebraic geometry）上实现显著提升，这对 AI for mathematics 社区有实际价值。Co-adaptive retrieval 机制如果成功，可以推广到其他涉及编译器反馈的形式化任务（proof generation, code synthesis）。Binarize-then-enrich 虽然 insight 有限，但作为通用方法论确实有跨领域适用性。

   限制 significance 的因素：autoformalization 仍是一个相对小众的子领域。虽然在 AI for math 热潮中受到更多关注，但与 LLM reasoning、code generation 等热门方向相比，直接受众有限。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。覆盖了 5 个相关研究脉络，引用了 25+ 篇论文，包括最新的 2026 年工作（DDRL, GDPO, MathAtlas, Construction-Verification/AMBER）。关键对比点清晰：
   - 与 FormaRL: 使用 trained critic 而非 LLM consistency，加入 retrieval 和 test-time adaptation
   - 与 Online RL for Autoformalization: test-time 而非 training-time，trained critic 而非 embedding similarity
   - 与 DDR/DRIFT: dynamic co-adaptive 而非 static retrieval
   - 与 DDRL: multi-tier reward 而非 binary
   
   调研中确认的引用（DDR 的 500K 数据集、AMBER 的 47.3% hallucination rate、CriticLean 的 84.8% accuracy、DDRL 的 AIME 结果）均与原始论文一致。差异化定位清晰且准确。唯一的轻微不足是：对 ATLAS (NeurIPS 2025) 和 Monotonic Refinement 的讨论主要作为 reference point，没有深入分析它们的 inference-time refinement 策略是否能部分替代 TTRL 的功能。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty 是中等水平（一个扎实的新贡献 + 若干 obvious combination），这限制了概率的上界——一个审稿人可能会写 "the co-adaptive retrieval idea is interesting, but the binarize-then-enrich and critic integration feel like natural engineering choices rather than research contributions"。Significance 中偏强但受限于子领域的受众规模。Related work 是真正的强项，降低了被 "missing related work" 拒稿的风险。

从 rubric 锚点来看：proposal 有真实的 novelty delta（co-adaptive retrieval with error taxonomy），方向正确，问题重要，但核心发现如果 positive（"co-adaptive retrieval + debiased RL 在 OOD autoformalization 上优于 static retrieval + vanilla GRPO"），审稿人更可能说 "this makes sense, I would have expected retrieval adaptation to help" 而非 "this is surprising"。这将其定位在 25-35% 区间。

上界被 novelty 深度限制：proposal 的创新主要在 combination 层面，单个贡献的 insight 深度有限。下界被 related work 覆盖度和 Phase 0 de-risking 设计支撑：这是一个 well-crafted proposal，不太可能因为"方向不对"或"遗漏关键工作"而被直接拒绝。

【主要风险】:
1. **"Kitchen sink" / combination paper 质疑**：Proposal 集成了 4+ 个现有技术（TTRL, DDRL, GDPO, co-adaptive retrieval, CriticLean, progressive curriculum），审稿人可能认为没有任何一个单独贡献有足够的深度，整体是 "competent systems work" 而非 "research contribution"。Binarize-then-enrich 尤其容易被认为 trivial。
2. **核心前提（CriticLean 在 OOD skewed distribution 下的可靠性）未经验证**：如果 Phase 0 calibration 发现 critic precision 在 skewed distribution 下显著低于 80%，整个 pipeline 的 reward signal 基础就会受到质疑。即使 proposal 设计了 confidence gating 作为 fallback，审稿人可能会认为这是在 patch 一个根本性的 weakness。
```

Sources:
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)
- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327)
- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242)
- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181)
- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)
- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)
- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)
- [Construction-Verification/AMBER Benchmark](https://arxiv.org/abs/2602.01291)
- [R3: Optimizing Retrieval for RAG via Reinforcement Learning](https://arxiv.org/abs/2510.24652)
- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)
- [NVIDIA GDPO Official Page](https://nvlabs.github.io/GDPO/)
- [Kimina-Prover: Test-time RL on Formal Reasoning](https://huggingface.co/blog/AI-MO/kimina-prover)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084) (NeurIPS 2025): 提出在测试时利用 majority voting 伪标签进行 RL 训练，在 AIME 2024 上将 Qwen-2.5-Math-7B 的 pass@1 提升约 211%。这是本 proposal 的核心基础之一，但仅适用于有明确数值答案可做 majority voting 的非形式化数学推理。
- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327) (ACL 2026 Findings): 识别了 GRPO 归一化在低共识场景下放大伪信号的问题，提出频率平衡采样 + 固定 ±1 advantages + 共识离策略优化三组件方案。在 AIME 2024 上对 Qwen2.5-Math-1.5B 实现 21.0→25.0 的提升。**关键限制：仅处理二元 (correct/incorrect) 奖励。**
- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242) (NVIDIA, Jan 2026): 针对多奖励 GRPO 的 reward signal collapse 问题，提出每个奖励独立归一化后再聚合。在工具调用、数学推理、代码生成任务上优于标准 GRPO。
- [CriticLean](https://arxiv.org/abs/2507.06181) (Jul 2025, ByteDance/Nanjing): 训练 CriticLeanGPT 作为语义保真度判别器，14B-RL 变体在 CriticLeanBench (250 correct / 250 incorrect 平衡分布) 上达到 84.8% 精度。**关键限制：仅在平衡分布上评测，严重倾斜分布下的表现未知。**
- [FormaRL](https://arxiv.org/abs/2508.18914) (COLM 2025): 使用 GRPO + 编译检查 + LLM 一致性检查作为奖励，在 ProofNet 上将 pass@1 从 4% 提升至 26%。训练时 RL，无 retrieval 适应，无测试时适应。
- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045) (Wang et al., NeurIPS 2025 MAR Workshop): 使用 GRPO + BEq + embedding 奖励，在 RLMEval 上 TC1 从 17.29% 提升至 26.01%。**与本 proposal 最接近的先驱工作，但为训练时 RL，使用 embedding 相似度而非训练过的 semantic critic，无 retrieval 适应。**
- [DDR: Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990) (arXiv 2025): 构建 500K 样本依赖检索数据集，将 ICL 生成依赖的幻觉率从 21-39% 降至 <2%。**关键数据：量化了 identifier hallucination 的严重程度，为本 proposal 提供了 co-adaptive retrieval 的动机基础。**
- [Construction-Verification/AMBER](https://arxiv.org/abs/2602.01291) (Feb 2026): 分析了 DeepSeek-R1 在应用数学上的 3,189 个编译错误，发现 47.3% 是不存在的定理/定义幻觉，32.7% 是形式化能力错误。**直接支撑了 proposal 的 ≥40% Tier 1 错误阈值假设。**
- [R3: Optimizing Retrieval for RAG via Reinforcement Learning](https://arxiv.org/abs/2510.24652) (NeurIPS 2025): 通过强化对比学习在 RAG 环境中自适应优化 retriever，比原始 retriever 提升 5.2%。**为本 proposal 的 co-adaptive retrieval 提供了方法论基础。**
- [TTARAG](https://arxiv.org/abs/2601.11443) (Jan 2026): 在推理时通过自监督预测任务动态更新 LM 参数以适应新领域。验证了测试时检索适应的可行性，但方法完全不同（前缀-后缀预测）。
- [MathAtlas](https://arxiv.org/abs/2605.14061) (May 2026): 52K 研究生级别数学问题，最强模型在 MA-Hard 上仅 2.6% 正确率。**为本 proposal 提供了理想的 OOD 评测场景。**
- [DRIFT](https://arxiv.org/abs/2510.10815) (ICLR 2026): 分解-检索-举例-形式化流水线，在 Con-NF 上达到 62.33% BEq+@10。静态检索，无 RL 适应。
- [RAutoformalizer](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d630537fc4402cfa3ebbc7450a0cac91-Abstract-Conference.html) (ICLR 2025 Spotlight): 将编译错误分类为"Hallucination"和"Others"两大类，确立了 identifier hallucination 作为主要错误类别。

- **调研总结**: 自动形式化领域正在快速发展，RL（FormaRL, Wang et al.）和 retrieval（DDR, DRIFT, CRAMF）两条技术路线已分别取得显著进展，但二者的结合——尤其是在测试时进行 co-adaptive retrieval + RL——目前确实是空白。TTRL 范式已在非形式化数学推理中验证，但因 majority voting 不适用于形式化语句，直接迁移存在技术挑战。DDRL 解决了 TTRL 的伪信号放大问题但仅限二元奖励。本 proposal 处于多条成熟技术路线的交汇点。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是：**DDR (静态检索) + CriticLean 奖励 + 标准 GRPO**，不需要 co-adaptive retrieval、不需要 DDRL debiasing、不需要 binarize-then-enrich。

具体分析：
1. **静态检索 vs. co-adaptive 检索**: DDR 已将 identifier hallucination 从 21-39% 降至 <2%。如果静态检索已经基本解决了 identifier hallucination 问题，co-adaptive retrieval 的增量价值可能有限。但 proposal 的反论点有一定道理：DDR 的 <2% 是在 in-distribution 评测，OOD 域（如凝聚态数学、代数几何）的 Mathlib 依赖分布可能与训练分布显著不同，静态检索可能退化。这一点是否成立取决于 Phase -1 的实证结果。
2. **DDRL debiasing vs. vanilla GRPO**: FormaRL 已经证明 vanilla GRPO 在 autoformalization 上有效（4→26%）。DDRL 在非形式化数学上的提升为 15.8→25.0（AIME 2024），即约 58% 相对提升。但 autoformalization 的奖励结构（compilation + critic + BEq）与数学推理的二元对错有本质区别，DDRL 的收益能否迁移是未经验证的。
3. **Binarize-then-enrich 的必要性**: 如果直接用 GDPO 的 per-reward 归一化就足够了，binarize-then-enrich 这一"先二值化再丰富"的两步法可能是过度工程。

**增量价值判断**: co-adaptive retrieval 在 OOD 场景的理论动机成立（静态检索在 distribution shift 下可能退化），但实际增量大小高度依赖经验验证。binarize-then-enrich 的增量价值不确定——它试图同时获得 DDRL 的 debiasing 和 GDPO 的多奖励保真度，但能否 outperform 二者单独使用尚不清楚。

【前提假设检验】:
核心逻辑链中存在以下未经验证的假设：

1. **"Lean 4 结构化错误信号足以驱动有效的 retriever 对比训练"（关键假设）**: 虽然 AMBER 证明了 47.3% 的错误是 identifier hallucination，但从"知道缺了什么 identifier"到"能据此有效更新 retriever 的 embedding 空间"之间有显著的技术跳跃。R3 在通用 QA 的 RAG 场景验证了这一路径，但 Mathlib 的依赖空间结构（层级化、高度互联、数学类型系统约束）与通用文档检索有质的不同。Tier 2 信号（类型不匹配）到检索正样本的映射质量未知。
2. **"CriticLean-14B 在严重倾斜分布下仍能保持足够的 precision"（已部分 de-risk）**: Proposal 在 Phase 0 设计了显式的 calibration 实验，这是正确的做法。但如果 precision <80%（即使加了 confidence gating），整个奖励机制的基础就不稳固——Phase 0 的 go/no-go 设计是合理的。
3. **"DDRL 的 debiasing 机制在多层奖励下仍然有效"（弱假设）**: DDRL 的三组件（平衡采样、固定 advantage、共识离策略优化）是为二元奖励设计的。将其中的"正确/错误"替换为"compile+critic 通过/不通过"在概念上合理，但原始 DDRL 论文中"ambiguous zone"的定义（30-70% 正确率）是否适用于 autoformalization 的奖励结构？如果 OOD 域的编译率极低（<10%），几乎所有样本都是"rejected"，balanced sampling 可能退化。
4. **"Progressive curriculum 能有效解决 bootstrapping 问题"（弱假设）**: 从近分布到远 OOD 的渐进适应策略直觉上合理，但过渡准则（编译率 ≥40%、critic approval ≥60%）是主观设定的。如果近分布域的收益无法有效转移到远 OOD 域，curriculum 可能只是推迟了问题而非解决了问题。

【3 维度打分】:

1. **Novelty: 中** — 本 proposal 的核心贡献是**将多个独立验证的技术路线进行非平凡组合**，而非提出根本性的新方法。具体而言：
   - Co-adaptive retrieval (Phase 2) 的方法论基础来自 R3 (NeurIPS 2025) 和 Reinforced-IR (ACL 2025)，创新点在于将其应用于 Lean 4 的结构化错误信号层级。这是一个有意义的 domain adaptation，Lean 4 的类型检查器确实提供了比通用 QA 场景更丰富的结构化反馈，Tier 1/2/3 的分层设计利用了领域特有属性。但核心技术（对比学习 + 环境反馈训练 retriever）不是新的。
   - Binarize-then-enrich (Phase 3) 是 DDRL + GDPO 的嫁接。DDRL 处理二元奖励的 debiasing，GDPO 处理多奖励归一化——将二者串联（先二值化获得 DDRL 的好处，再用 GDPO 恢复连续奖励信息）是一个合理的工程思路，但"先 binarize 再 enrich"的框架并非深刻的方法论洞察。
   - CriticLean 作为 TTRL 奖励 (Phase 0-1) 的应用是直接的——CriticLean 论文本身就是作为 RL 奖励设计的，只是未在 TTRL 场景下评估。Proposal 的分布偏移 calibration 是务实的工程贡献，但不是概念突破。
   - **最有新意的元素**是利用 Lean 4 的 structured error taxonomy 构建 graded retriever training signal——这确实是一个 domain-specific insight，尚无先例。但它更接近"clever engineering"而非"new paradigm"。
   - 对比：FormaRL (COLM 2025) 提出了 RL for autoformalization (无标注数据)；DDRL (ACL 2026) 提出了 TTRL debiasing 的新方法论；R3 (NeurIPS 2025) 提出了 RL-driven retriever 优化。这些工作各自有独立的方法论贡献。本 proposal 的贡献更多在于"合理组合 + 领域特化适配"。

2. **Significance: 中** — 
   - **问题重要性高**: OOD autoformalization 退化是一个真实且重要的问题。MathAtlas 上 2.6% 的 MA-Hard 正确率说明当前方法在 OOD 域几乎完全失效。AMBER 的 47.3% identifier hallucination 率确认了问题的根源。
   - **影响范围受限**: 目标受众是 autoformalization + RL + formal verification 的交叉社区，相对较窄。Binarize-then-enrich 号称可推广到任何多层奖励场景，但未在其他领域验证，实际影响力有待证明。
   - **结果预期性**: 如果实验结果是 positive（TTRA 在 OOD 域显著优于 baselines），审稿人的反应更可能是"reasonable, this is what I would expect from combining better retrieval + better reward + better RL optimization"而非"surprising"。方向正确、预期合理，但缺乏反直觉元素。
   - **实际价值**: 如果 TTRA 确实能使自动形式化模型在 OOD 域大幅提升（例如 MathAtlas MA-Hard 从 2.6% 到 15%+），这将有显著的实际意义。但这是执行层面的期望，不是 idea 层面的保证。

3. **Related Work: 强** — 
   - 该 proposal 对文献的覆盖极为全面，横跨 RL for autoformalization (FormaRL, Wang et al., ReForm)、semantic critics (CriticLean, ATF)、debiased RL (DDRL, GDPO)、co-adaptive retrieval (R3, Reinforced-IR, TTARAG)、static retrieval & error analysis (DDR, DRIFT, CRAMF, AMBER, RAutoformalizer) 五条研究脉络。
   - 差异化定位清晰：准确指出了与每个相关工作的具体差异——Wang et al. 是训练时 RL 无 retrieval；FormaRL 用 LLM 一致性而非 trained critic；DDRL 仅限二元奖励；DDR/DRIFT 是静态检索。
   - 引用的论文经我搜索验证基本准确：AMBER 的 47.3% identifier hallucination 率、DDR 的 <2% 幻觉率、DDRL 的性能数字、CriticLean 的 84.8% 精度等均可通过搜索确认。
   - 唯一小瑕疵：部分引用（如 MathAtlas May 2026, Monotonic Refinement 2026）因过于新近，难以完全独立验证所有数字。但整体文献素养在 proposal 中属于顶尖水平。

【概率估计】: [23% - 33%] 中位 27%

【估计理由】: 
- **Novelty（中）限制了上界**: 核心贡献是多个已有技术的非平凡组合+领域特化适配，而非根本性的方法论创新。在 AAAI 的审稿标准下，纯"组合创新"论文需要 (a) 证明组合本身是非显然的，(b) 各组件产生大于部分之和的协同效应。Proposal 论证了 (a) 但 (b) 需要实验支撑。
- **Significance（中）将中位数限制在 30% 以下**: 目标受众相对窄（autoformalization + RL + retrieval 交叉），结果若 positive 则"合理但不意外"。
- **Related Work（强）提供了下限保障**: 极为全面的文献覆盖和精确的差异化定位确保了 proposal 不会因 related work 不足而被拒，也使得"novelty claim 不成立"的攻击面较小。
- **上界因素**: 如果利用 Lean 4 error taxonomy 的 graded retrieval signal 被审稿人视为一个 genuine domain-specific insight（而非简单 engineering），novelty 评分可能提升至"中-强"，概率上界可达 33%。
- **下界因素**: 如果审稿人认为这本质上是"DDR + CriticLean + DDRL + GDPO 的拼接"且 binarize-then-enrich 不够 principled，novelty 评分会降至"中-弱"，概率可能低至 23%。

【主要风险】:
1. **"系统拼装"质疑 (Novelty risk)**: 审稿人可能认为 TTRA 是将 R3 的 co-adaptive retrieval、DDRL 的 debiasing、GDPO 的 multi-reward 归一化、CriticLean 的 semantic critic 简单拼装而成，每个模块的创新都在原始论文中，本文的贡献仅是"将它们放在一起"。虽然 proposal 论证了组合的非显然性（如 Lean 4 error taxonomy 的领域特有信号、binarize-then-enrich 的方法论框架），但这取决于审稿人是否 buy 这种组合创新的价值主张。
2. **Trivial alternative 竞争力 (Core claim risk)**: 如果 DDR 静态检索 + CriticLean + vanilla GRPO 已能获得大部分 OOD 提升（因为 DDR 在 in-distribution 已将幻觉降至 <2%，CriticLean 提供了比 LLM 一致性更好的奖励信号），那么 co-adaptive retrieval 和 binarize-then-enrich 的增量贡献可能不足以支撑一篇 AAAI 论文。Proposal 的 contribution floor analysis 部分缓解了这一风险，但核心创新的增量价值仍是最大不确定性。
```

Sources:
- [TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)](https://arxiv.org/abs/2504.16084)
- [DDRL: Spurious Signal Amplification in TTRL (ACL 2026 Findings)](https://arxiv.org/abs/2604.21327)
- [GDPO: Group reward-Decoupled Normalization (NVIDIA, 2026)](https://arxiv.org/abs/2601.05242)
- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181)
- [FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)](https://arxiv.org/abs/2508.18914)
- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)
- [Construction-Verification/AMBER Benchmark (Feb 2026)](https://arxiv.org/abs/2602.01291)
- [R3: Optimizing Retrieval for RAG via Reinforcement Learning (NeurIPS 2025)](https://arxiv.org/abs/2510.24652)
- [TTARAG: Test-Time Adaptation for RAG (Jan 2026)](https://arxiv.org/abs/2601.11443)
- [MathAtlas: A Benchmark for Autoformalization in the Wild (May 2026)](https://arxiv.org/abs/2605.14061)
- [RAutoformalizer (ICLR 2025 Spotlight)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d630537fc4402cfa3ebbc7450a0cac91-Abstract-Conference.html)
- [Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop)](https://www.researchgate.net/publication/396825045)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to conduct a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. TTRL (NeurIPS 2025, arXiv 2504.16084): 提出 test-time RL 范式，在无标注数据上利用 majority voting 作为伪标签驱动 GRPO 训练，Qwen2.5-Math-7B 在 AIME 2024 上 pass@1 提升约 211%。但 TTRL 的 majority voting 依赖数值答案的可比性，无法直接迁移到形式化数学的结构化输出。

2. DDRL (ACL 2026 Findings, arXiv 2604.21327): 诊断并修复 GRPO 在低一致性区间的虚假信号放大问题，通过频率平衡采样、固定 ±1 advantage、基于共识的 off-policy 精炼实现去偏。关键限制：仅支持二元 reward（正确/错误），作者明确将"更具表达力的 advantage 公式"列为 future work。与本 proposal 直接相关——proposal 的 binarize-then-enrich 正是对 DDRL 的扩展。

3. GDPO (NVIDIA, arXiv 2601.05242, Jan 2026): 解决 GRPO 在多 reward 场景下的 reward signal collapse 问题，通过 per-reward 解耦归一化保持不同 reward 维度的区分度。本 proposal 的"enrich"层直接借鉴此方法。该工作已开源并有实验验证。

4. CriticLean (arXiv 2507.06181, ByteDance): CriticLeanGPT-14B-RL 在平衡分布的 CriticLeanBench 上达到 84.8% 准确率（32B 达 87.0%），将 autoformalization pipeline 准确率从 54% 提升至 84%。关键缺口：评估仅在 250 正/250 负的平衡分布上，OOD TTRL 中的偏斜分布（>90% 不正确）下的表现未知。Proposal 的 Phase 0 calibration 正是针对此缺口。

5. FormaRL (COLM 2025, arXiv 2508.18914): 使用 GRPO + Lean 编译检查 + LLM 一致性检查作为 reward，在 ProofNet 上 pass@1 从 4% 提升至 26%。无 retrieval，无 test-time adaptation，无 trained semantic critic。是本 proposal 最直接的消融基线之一。

6. Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop): 使用 GRPO + BEq + embedding 相似度复合 reward 进行 Lean 4 autoformalization RL，TC1: 17.29%→26.01%，TC50: 76.41%→85.46%。但在训练时操作（非 test-time），使用 embedding 相似度（非 trained critic），无 retrieval。是最接近的先行工作。

7. DDR (arXiv 2511.11990): 构建 50 万样本依赖数据集，量化 ICL 生成的依赖中约 30% 为幻觉标识符（Hall_m=0.21-0.39），retrieval-based DDR 将幻觉率降至 <2%。为 co-adaptive retriever 提供基础设施和动机。

8. Construction-Verification/AMBER (arXiv 2602.01291, Feb 2026): 分析 DeepSeek-R1 在应用数学域上 3,189 个编译错误，47.3% 为不存在的定理/定义的幻觉——直接支持 Tier 1 错误信号 ≥40% 的假设。

9. R3 (NeurIPS 2025, arXiv 2510.24652): 通过强化对比学习优化 RAG 检索器，证明环境反馈可训练检索器。Reinforced-IR (ACL 2025): 交替 RLRF/RLGF 实现检索器-生成器互适应。两者均未应用于 autoformalization。

10. MathAtlas (arXiv 2605.14061, May 2026): 52K 研究生级别问题，最佳模型在 MA-Hard 上仅 2.6%，Mathlib-grounded 定义比非 grounded 高 66%（27.9% vs 16.8%）。进一步确认依赖可用性是瓶颈。

11. DRIFT (ICLR 2026): 分解-检索-示例-形式化框架，Con-NF 上 62.33% BEq+@10，但 ProofNet 上 21.93%（低于其他方法）。静态检索，无 RL。

12. StepFun-Formalizer (AAAI 2026): 知识-推理融合的 autoformalization，已被 AAAI 2026 接收，证明 autoformalization 方向在 AAAI 有接收先例。

13. ReForm (arXiv 2510.24592): 反射式 autoformalization + PBSO 位置感知 RL reward，平均提升 22.6pp。关注 semantic consistency 但不涉及 retrieval adaptation。

14. ATF (arXiv 2025): SFT + expert iteration + DPO + multi-LLM 一致性检查，FormalMath-Lite 上 94.51% Pass@1。强 in-distribution 性能但无 OOD 适应能力。

- 调研总结: Autoformalization 领域在 2025-2026 年经历爆发式发展，RL（FormaRL, Online RL）、semantic critic（CriticLean）、retrieval（DDR, DRIFT, CRAMF）、benchmark（MathAtlas, AMBER, FormalMATH）各条线独立推进。OOD domain adaptation 是公认的核心瓶颈（MathAtlas MA-Hard 仅 2.6%），但尚无工作在 test-time 同时做 retriever co-adaptation + debiased RL + semantic critic reward。Proposal 处于这些独立线索的交汇点，其组合确实尚无先例。


【Trivial Alternative 检验】:

最直接的 trivial alternative 是：**静态 retrieval (DDR/CRAMF) + CriticLean 作为 reranker（非 RL reward）+ 多次采样取最优**。这种 inference-time 方法无需任何权重更新，成本远低于 TTRL。

具体而言：
- DDR 已将标识符幻觉率从 30% 降至 <2%，如果静态检索已经足够好，co-adaptive retrieval 的增量可能有限
- CriticLean 84.8% 准确率作为 filter/reranker（不作为 RL reward）+ best-of-N 采样，已经可以显著提升质量（CriticLean 论文自身报告从 54% 提升至 84%）
- ATF 的 expert iteration + DPO 在 in-distribution 达到 94.51%，说明非 TTRL 的迭代方法也能走很远

**增量价值何在**：Proposal 的增量价值集中在 **OOD 适应** 场景——当目标域与训练分布差异大时（如 condensed mathematics、algebraic geometry），静态方法的天花板明显降低。MathAtlas MA-Hard 上 2.6% 的表现证明现有方法在远 OOD 域几乎失效。TTRA 的核心价值主张是：在这些现有方法崩溃的 OOD 域上，通过 test-time weight adaptation 突破天花板。这个价值主张成立，但需要实验证明 OOD 增量是实质性的（而非 marginal）。


【前提假设检验】:

核心 claim 的逻辑链中，以下环节是未经验证的假设：

1. **CriticLean 在 OOD 偏斜分布下仍有足够 precision**（Proposal 已识别此风险并设计 Phase 0 验证——这是正确的，但假设本身尚未验证）。CriticLeanBench 的 84.8% 准确率来自 250/250 平衡分布；在 >90% 错误的 OOD 分布下，即使 FPR 不变，precision 可能大幅下降。如果 critic precision 不足，整个 multi-tier reward 体系的基础就动摇了。

2. **Lean 4 编译错误中 Tier 1 信号在目标 OOD 域上足够丰富**。AMBER 的 47.3% 数据来自 DeepSeek-R1（大模型）在应用数学域，本 proposal 使用 Qwen3-8B（小模型）在不同 OOD 域（condensed math, algebraic geometry）。小模型的错误分布可能与大模型有质的差异——小模型可能产生更多低级语法/类型错误（Tier 3），而非精确的标识符幻觉（Tier 1）。Phase -1 设计了验证，但这是关键前提。

3. **TTRL 在 autoformalization 上能产生有意义的 policy improvement**。TTRL 在 informal math reasoning 上的成功依赖于 majority voting 提供的较高质量伪标签。在 autoformalization 中，伪标签质量取决于 compilation + critic 的组合准确性。如果 OOD 域上 <10% 的候选能编译通过（proposal 自己预期如此），GRPO 的每个 group 中 positive 样本极少，学习信号可能太弱，即使加了 DDRL 去偏也难以稳定训练。

4. **Retriever co-adaptation 不会引入灾难性遗忘或漂移**。每 N_ret=50 步更新一次检索器，重建 FAISS 索引，但新检索结果可能将 formalizer 引向不同方向，形成振荡。R3 和 Reinforced-IR 在常规 NLP 任务上验证了交替优化的稳定性，但 autoformalization 的 reward landscape 更稀疏、更离散，稳定性假设需要验证。

5. **Binarize-then-enrich 能有效结合 DDRL 和 GDPO 的优势**。DDRL 的去偏依赖固定 ±1 advantage，而 GDPO enrichment 在 accepted 样本内添加连续 bonus。这两种机制的交互是否真的互补（而非干扰）缺乏理论支撑，仅是直觉性的组合设计。


【3 维度打分】:

1. **Novelty: 中** — 
   Proposal 的核心贡献本质上是将 4 个已有技术（TTRL, DDRL/GDPO, CriticLean, R3/Reinforced-IR 式 co-adaptive retrieval）适配并组合到 autoformalization 场景。每个单独组件都是对现有工作的适配而非从零创造：
   - Binarize-then-enrich 是 DDRL（ACL 2026）+ GDPO（NVIDIA, Jan 2026）的组合适配，methodological novelty 有限但非 trivial
   - Co-adaptive retrieval 借鉴 R3（NeurIPS 2025）和 Reinforced-IR（ACL 2025）的范式，应用于 Lean 4 error taxonomy 是新的应用场景
   - CriticLean 作为 RL reward 是对 CriticLean（2025）的直接应用 + 分布偏移分析
   
   最具 novelty 的部分是 **Lean 4 结构化错误信号的分级利用**（Tier 1/2/3 hierarchy 用于 contrastive retriever training）——这确实没有先例，且利用了 Lean 4 特有的结构化反馈优势。但这更像是一个 domain-specific engineering insight 而非 general methodological breakthrough。
   
   与最近的 FormaRL（COLM 2025）、Online RL for Autoformalization（NeurIPS 2025 Workshop）、ReForm（2026）相比，TTRA 增加了 retrieval co-adaptation 和 debiased multi-tier RL，这些是真实的增量。但与 CriticLean（2025）相比，将 critic 从 reranker 变为 RL reward signal 的增量相对有限。
   
   总体而言，这是一篇 **well-crafted combination paper**，novelty 来自组合而非单一突破。对于 AAAI，组合创新被接受但需要实验结果证明组合的协同效应大于各组件之和。

2. **Significance: 中偏强** — 
   研究问题（OOD autoformalization）的重要性得到了充分的数据支撑：MathAtlas MA-Hard 上 2.6% 的表现（arXiv 2605.14061）表明现有方法在远 OOD 域几乎完全失效；AMBER 的 47.3% 标识符幻觉率（arXiv 2602.01291）确认了问题根源。如果 TTRA 能在这些 benchmark 上实现实质性提升，其影响力是真实的。
   
   但影响面有一定局限：(a) 受众主要是 autoformalization + formal math 社区，虽然在增长但仍相对小众；(b) binarize-then-enrich 虽声称可推广到"任何多层 reward 场景"，但实际推广性需要额外实验验证；(c) co-adaptive retrieval 的 Lean 4 error taxonomy 依赖高度 domain-specific，难以直接迁移到其他任务。
   
   正面看：autoformalization 是通向 AI for mathematics 的关键管线，AlphaProof（Nature 2025）已证明这一方向的战略重要性。StepFun-Formalizer 被 AAAI 2026 接收也证明该方向在顶会有接受度。

3. **Related Work: 强** — 
   这是该 proposal 最强的维度。Related work 覆盖极其全面，跨越 5 个研究线索（RL for autoformalization, semantic critics, debiased RL, co-adaptive retrieval, static retrieval + error analysis），引用了截至 2026 年 5 月的最新工作（MathAtlas May 2026, DDRL ACL 2026, StepFun-Formalizer AAAI 2026）。
   
   关键论文描述准确：CriticLean 的 84.8%/87.0% 数字、DDRL 的三组件设计、GDPO 的 per-reward 解耦归一化、AMBER 的 47.3% 数字——均经调研确认与原文一致。DDR 的 500K 数据集、R3 的 reinforced contrastive learning、FormaRL 的 GRPO + 编译/一致性 reward——定位准确。
   
   差异化定位清晰：与 FormaRL 的区分（无 retrieval、无 test-time）、与 Online RL for Autoformalization 的区分（training-time、无 trained critic、无 retrieval）、与 CriticLean 的区分（非 RL reward、平衡分布评估）均有说服力。
   
   唯一瑕疵：部分引用（如"Online RL for Autoformalization" Wang et al.）在公开搜索中较难找到完整信息，可能是 workshop paper 或最新 preprint，但不影响整体评估。


【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
这个 proposal 的核心是一篇 **well-executed combination paper**。它的 related work 覆盖和问题动机都很强（Related Work: 强，Significance: 中偏强），但 **novelty 受限于组合适配的本质**（Novelty: 中）。

从 rubric 角度：方向正确、有真实的 novelty delta（特别是 Lean 4 error taxonomy 分级利用和 binarize-then-enrich），但如果核心发现是 positive（即"更好的 retrieval + 更好的 reward + 更好的 RL 优化 = OOD 域上更好的表现"），审稿人很可能会说 **"I would have guessed this"**——这将中位概率锚定在 25-35% 区间。

限制上界的主要因素是 **Novelty 维度**：4 个已有技术的组合适配，即使每个适配都合理，整体仍缺乏一个 "surprising" 的核心发现或反直觉的 insight。系统复杂度高（Tier 1/2/3 + binarize-then-enrich 3 组件 + GDPO enrichment + progressive curriculum 4 阶段），审稿人可能质疑 ablation 能否清晰归因。

向下拉的风险因素：(a) trivial alternative 威胁——静态 DDR + CriticLean reranker + best-of-N 可能在某些 OOD 域上已经足够好，削弱 TTRL 的增量价值；(b) 前提假设 #2（小模型 Tier 1 信号丰富度）和 #3（OOD 极稀疏 reward 下 GRPO 学习信号强度）如果不成立，核心机制失效。

向上拉的因素：(a) autoformalization 是 2025-2026 热点方向（StepFun-Formalizer AAAI 2026 接收）；(b) proposal 的 Phase -1/Phase 0 go/no-go 设计非常成熟，contribution floor 分析确保 partial success 也可发表；(c) binarize-then-enrich 作为独立方法论贡献有一定推广价值。

【主要风险】: 
1. **Novelty 不足的 "kitchen sink" 质疑**：审稿人可能认为这是 4 个已有技术的工程组合（TTRL + DDRL/GDPO + CriticLean + R3-style co-adaptive retrieval），每个单独适配的 novelty 有限，整体缺乏统一的 deep insight——这是 AAAI 审稿中 combination paper 最常被拒的原因。
2. **OOD 增量被 trivial alternative 侵蚀**：如果静态 DDR + CriticLean reranker + best-of-N 在 OOD benchmark 上的表现与 TTRA 差距不大（例如 <5pp），那么引入 TTRL + co-adaptive retrieval 的巨大复杂度和计算成本就难以 justify，审稿人会要求证明 "why do you need test-time weight adaptation when inference-time methods already work reasonably?"
```

Sources:
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)
- [DDRL: Understanding and Mitigating Spurious Signal Amplification in TTRL](https://arxiv.org/abs/2604.21327)
- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242)
- [CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization](https://arxiv.org/abs/2507.06181)
- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)
- [Online Reinforcement Learning for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)
- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)
- [Construction-Verification/AMBER: A Benchmark for Applied Mathematics in Lean 4](https://arxiv.org/abs/2602.01291)
- [R3: Optimizing Retrieval for RAG via Reinforcement Learning](https://arxiv.org/abs/2510.24652)
- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)
- [DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems](https://arxiv.org/abs/2510.10815)
- [StepFun-Formalizer: AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40691)
- [ReForm: Reflective Autoformalization](https://arxiv.org/abs/2510.24592)
- [TTARAG: Test-Time Adaptation for RAG](https://arxiv.org/abs/2601.11443)
- [NVlabs/GDPO GitHub](https://github.com/NVlabs/GDPO)
- [THUNLP-MT/FormaRL GitHub](https://github.com/THUNLP-MT/FormaRL)


【原始 proposal（允许参考但不是主要依据）】:
# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization

## Core Problem

Current autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning dramatically but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in the multi-tier reward setting (compilation + critic + BEq); and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation, yet no prior work fine-tunes the retriever during test-time RL. Can we make TTRL viable for autoformalization by combining compilation-error-driven co-adaptive retrieval that exploits Lean 4's full structured error taxonomy, a calibrated semantic critic reward, and principled adaptation of binary-reward debiased RL to multi-tier rewards?

## Research Opportunity

Four independently validated capabilities have never been combined: (1) Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode. R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv 2601.11443, Jan 2026) shows test-time retrieval adaptation is achievable via self-supervised prediction. Critically, the prevalence of identifier hallucination as the dominant error class is now established by converging evidence from multiple independent studies: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) provides the strongest quantitative evidence, finding that 47.3% of 3,189 sampled compilation errors from DeepSeek-R1 on applied mathematics domains stem from 'invocation of non-existent theorems or definitions'—directly exceeding Phase -1's ≥40% Tier 1 threshold. DDR (arXiv 2511.11990) quantifies that ICL-based dependency generation produces ~30% hallucinated (non-existent) Mathlib identifiers (Hall_m=0.21-0.39 across frontier LLMs), while retrieval-based DDR reduces hallucination to <2% (Hall_m=0.016). The RAutoformalizer (ICLR 2025 Spotlight) explicitly classifies compilation errors into 'Hallucination' (errors caused by hallucination of identifiers) and 'Others', establishing identifier hallucination as a primary error class. MathAtlas (May 2026) further shows a 66% performance advantage for Mathlib-grounded definitions (27.9% vs 16.8% correct, p<0.001), confirming that dependency availability is the critical bottleneck. Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL-based autoformalization—where Lean's structured error taxonomy (unknownIdentifier, type mismatch with type signatures, failed to synthesize with typeclass names, unknown namespace) provides a graded hierarchy of machine-parseable signals for retriever training. (2) TTRL with debiasing has advanced rapidly. DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed +/-1 advantages, and consensus-based off-policy refinement, achieving up to 19.0% relative improvement over ETMR on AIME 2024 (4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B). But DDRL assumes binary correct/incorrect rewards. GDPO (NVIDIA, arXiv 2601.05242, Jan 2026) addresses multi-reward GRPO through per-reward decoupled normalization, preventing reward signal collapse. The combination—binarize multi-tier rewards for DDRL's debiasing, then enrich with GDPO's per-reward normalization for continuous components—has not been attempted. (3) CriticLean (July 2025) provides the missing reward signal: CriticLeanGPT-14B-RL achieves 84.8% accuracy on CriticLeanBench (87.0% for the 32B variant), raising autoformalization pipeline accuracy from 54% to 84% over compilation-only feedback. However, CriticLeanBench evaluates on a balanced 250-correct/250-incorrect distribution, while OOD TTRL produces heavily skewed distributions (often <10% compilable candidates). This distributional shift gap has not been characterized, motivating our Phase 0 calibration protocol. (4) Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) validates RL for autoformalization (TC1: 17.29% to 26.01% on RLMEval using GRPO with composite BEq + embedding rewards), but operates at training time with labeled/unlabeled data on in-distribution problems, without retrieval, test-time adaptation, or a trained semantic critic. Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.

## Research Landscape

The landscape spans five relevant lineages. (1) RL for autoformalization: FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards, improving pass@1 from 4% to 26% on ProofNet. Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with composite rewards (BEq + embedding-based similarity) for Lean 4, achieving TC1: 17.29% to 26.01%, TC50: 76.41% to 85.46% on RLMEval—the closest prior work but operates at training time on in-distribution problems, uses embedding similarity rather than a trained semantic critic, and lacks retrieval and test-time adaptation. ReForm (2026) applies position-aware RL rewards for reflective autoformalization (+22.6pp average). (2) Semantic critics and iterative refinement: CriticLean (July 2025) introduces CriticLeanGPT, with the 32B-RL variant achieving 87.0% accuracy and the 14B-RL variant reaching 84.8% on the balanced CriticLeanBench (250 correct, 250 incorrect). The paper reports TPR, FPR, TNR, and FNR metrics but evaluates only on balanced distributions, leaving the heavily skewed OOD regime uncharacterized. ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO with multi-LLM consistency checking. Monotonic Refinement achieves 90.27% composite on miniF2F through multi-model ensemble orchestration. These achieve impressive results but cannot adapt model weights to new domains. (3) Debiased RL and multi-reward optimization: DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification through three components: frequency-based balanced sampling excluding ambiguous samples, fixed +/-1 advantages, and consensus-based off-policy refinement—achieving up to 19.0% relative improvement over ETMR on AIME 2024 (4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B; the TTRL baseline without debiasing scores 15.8, illustrating the severity of signal amplification that DDRL corrects). Critically, DDRL operates exclusively with binary rewards and its authors note that 'more expressive advantage formulations' are left for future work. GDPO (NVIDIA, arXiv 2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization, demonstrating that standard GRPO collapses distinct reward combinations into identical advantage values. (4) Co-adaptive retrieval: R3 (NeurIPS 2025) optimizes retrieval for RAG via reinforced contrastive learning. Reinforced-IR (ACL 2025) alternates RLRF and RLGF for mutual adaptation. TTARAG (arXiv 2601.11443) demonstrates test-time adaptation for RAG. None of these have been applied to autoformalization or Lean 4. (5) Static retrieval, error analysis, and identifier hallucination quantification for autoformalization: The Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) provides the most comprehensive error taxonomy to date: analyzing 3,189 sampled compilation errors from DeepSeek-R1 on applied math (convex analysis, optimization, numerical algebra, high-dimensional probability), they find 47.3% are hallucination of non-existent theorems/definitions, 32.7% are formalization competence errors, 15.2% are incomplete outputs, and 4.8% are formatting/syntax—concluding that 'future improvements should prioritize retrieval-augmented generation or specialized fine-tuning.' DDR builds a 500K-sample dependency dataset and quantifies that ~30% of ICL-generated dependencies are hallucinated identifiers (Hall_m ranging 0.21-0.39 across frontier LLMs), reduced to <2% with retrieval-based DDR. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF but falls short on ProofNet (21.93% vs 27.54%). CRAMF indexes 26K+ Mathlib definitions for concept-level retrieval, documenting that models fabricate identifiers like 'Function.Continuous' instead of 'ContinuousOn' and 'Group.index' instead of 'Subgroup.index'. MathAtlas (May 2026) introduces 52K graduate-level problems where the best model achieves only 2.6% on MA-Hard and adding local context degrades prompted systems' performance. The RAutoformalizer (ICLR 2025 Spotlight) explicitly categorizes compilation errors into 'Hallucination' (identifier hallucination) vs 'Others', establishing that identifier-related errors constitute a major error class. After exhaustive search through May 2026, no work combines (a) co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, (b) a calibrated semantic critic as RL reward with distributional shift analysis, (c) principled adaptation of binary-reward debiased RL to multi-tier rewards, and (d) test-time adaptation on fully unlabeled OOD domains.

## Proposed Approach

We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a framework that makes TTRL viable for autoformalization through three technical innovations: (1) a dual-loop architecture with co-adaptive retrieval exploiting Lean 4's full structured error taxonomy, (2) integration of CriticLean-14B as semantic RL reward with explicit calibration under distributional shift, and (3) a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards using GDPO's per-reward decoupled normalization.

**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Before committing to the pipeline design, we quantify the retrieval signal coverage that Lean 4's error taxonomy provides on OOD domains. We compile 500 candidate formalizations from an existing model (e.g., FormaRL or Kimina-7B) on Con-NF (OOD) and 500 on MathAtlas MA-Hard, collecting all compilation error messages. We classify each error into the following hierarchy:
  (a) Tier 1 — Direct identifier signals: `lean.unknownIdentifier` (names the missing constant), `unknown namespace` (names the namespace). These provide direct, machine-parseable mapping from error to needed Mathlib dependency.
  (b) Tier 2 — Type-based signals: `type mismatch` (contains expected vs actual type signatures), `failed to synthesize instance` (names the typeclass). These provide weaker but still informative retrieval signals—type signatures can be matched against Mathlib's type index, and typeclass names map to specific Mathlib modules.
  (c) Tier 3 — Indirect signals: tactic failures, elaboration errors, syntax errors. These provide no direct retrieval signal but can serve as negative examples (confirming that retrieved dependencies were insufficient).
  Quantitative thresholds: If Tier 1 errors constitute ≥40% of compilation failures, the co-adaptive retrieval mechanism is well-supported as designed. If Tier 1 is 20-40%, we rely on both Tier 1 and Tier 2 signals (requiring the type-signature matching extension). If Tier 1 is <20%, we must fall back primarily to Tier 2 signals with type-signature-based retrieval. Prior evidence now strongly supports ≥40%: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291) finds that 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math domains are hallucination of non-existent theorems/definitions—directly exceeding the ≥40% threshold on an OOD domain. DDR shows ~30% of ICL-generated dependencies are hallucinated identifiers (Hall_m=0.21-0.39 across frontier LLMs), the RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' (identifier hallucination) as one of two major error classes, and CRAMF documents systematic fabrication of close-but-wrong identifiers. Phase -1 nonetheless remains essential because AMBER's error distribution is from DeepSeek-R1 on applied math, and our pipeline uses a smaller formalizer on different OOD domains (condensed mathematics, algebraic geometry)—the error distribution may differ. Resource: ~8 A100-hours for generation, ~10 CPU-hours for compilation and error parsing. No model training required.

**Phase 0 — Minimal Pilot Experiment with Critic Calibration (De-risking).** Before committing to the full pipeline, we validate two riskiest assumptions with a minimal experiment. Setup: Take FormaRL's GRPO pipeline, replace its LLM-consistency reward with CriticLean-14B as the sole semantic reward signal (reward = r_compile × r_critic). Data: 200 problems from Con-NF (OOD) + 200 from FormalMATH number theory (near-distribution). No retrieval, no curriculum, no DDRL debiasing—just vanilla GRPO with the critic reward.
  Primary hypothesis: if CriticLean-14B reward achieves ≥3pp BEq@1 improvement over compilation-only GRPO on Con-NF, the core premise (semantic critic rewards enable OOD adaptation) is validated.
  Secondary hypothesis — Critic calibration under distributional shift: We explicitly measure CriticLean-14B's precision and recall SEPARATELY on the skewed distribution produced during TTRL. Specifically: (a) Among K=32 candidates per problem, record the number that compile and the number the critic approves. (b) For problems where <10% of candidates compile (the regime expected on hard OOD domains), manually inspect 100 random critic-approved candidates and 100 critic-rejected candidates to compute precision and recall in this hardest regime. (c) Report calibration curves: for each critic confidence bin (if logit-based confidence is available from the critic model), plot the empirical correctness rate. Key concern: on CriticLeanBench's balanced 250/250 distribution, 84.8% accuracy could correspond to very different precision/recall trade-offs. Under OOD TTRL's heavily skewed distribution (90%+ incorrect), even moderate false positive rates could produce substantial noise. Our conservative binarization (requiring BOTH compile AND critic approval) inherently prioritizes precision over recall—a candidate must pass two independent filters. If critic precision on the skewed distribution is <80% (i.e., >20% of critic-approved compilable candidates are semantically wrong), we introduce critic confidence gating: only accept critic judgments with confidence >0.8, trading recall for precision.
  Resource: ~50 A100-hours (increased from 40 to include calibration analysis), 2-3 weeks. Go/no-go decision: proceed only if primary hypothesis confirmed AND critic precision on the skewed distribution ≥80% (or ≥80% with confidence gating).

**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune a Qwen3-8B base model as a retrieval-augmented autoformalizer using DDR's 500K-sample dependency dataset and GRPO with the multi-tier reward function R(y, x) = r_compile × (α·r_critic + β·r_beq), where: r_compile ∈ {0,1} is the Lean 4 compilation gate (verified via Kimina Lean Server with 128 parallel pre-warmed REPL workers); r_critic ∈ {0,1} is the semantic fidelity judgment from CriticLeanGPT-Qwen3-14B-RL, gated by the confidence threshold established in Phase 0; r_beq ∈ [0,1] is the BEq consensus density (fraction of compilable candidates in the same BEq equivalence class). We set α=0.7, β=0.3 to weight semantic fidelity over syntactic consensus, since BEq has high precision (98.6%) but low recall (~33% on ProofNet). Adaptive reward degradation: when fewer than M=4 candidates out of K=32 compile, BEq becomes degenerate, and the reward falls back to R = r_compile × r_critic.

**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever is a DDR-style dense encoder whose parameters ARE updated during TTRL—not frozen. This exploits a key structural property: Lean 4's type checker produces machine-parseable error messages with a hierarchy of retrieval informativeness.

  Loop 1 — Formalizer GRPO (every step): Generate K=32 candidate formalizations per problem, compile each against Lean 4, compute multi-tier rewards, and perform debiased GRPO updates (Phase 3).

  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Accumulated compilation feedback generates contrastive training data for the retriever using a graded error signal hierarchy:
    (a) Tier 1 — Direct identifier signals (highest confidence): When a formalization fails with `lean.unknownIdentifier` (tagged with `unknownIdentifierMessageTag`), the error explicitly names the missing Mathlib constant (e.g., 'unknown identifier Finset.sum_comm'). The dependencies that WERE retrieved but did NOT include this constant are hard negatives. The missing constant—looked up in the CRAMF/DDR Mathlib constant index—becomes the positive example. When the error is `unknown namespace`, the namespace maps to a Mathlib module, providing a coarser positive signal.
    (b) Tier 2 — Type-based signals (moderate confidence): When a formalization fails with `type mismatch`, the error contains expected vs actual type signatures. We match these type signatures against Mathlib's type index (built from DDR's 500K-sample dataset) to identify candidate dependencies that would resolve the mismatch, generating softer positive examples with reduced weight (0.5× in the InfoNCE loss). When `failed to synthesize instance` names a typeclass, we retrieve Mathlib instances of that typeclass as positives.
    (c) Tier 3 — Negative confirmation from non-identifier errors: Tactic failures, elaboration errors, and syntax errors do not provide positive retrieval signals but confirm that the retrieved dependency set was insufficient for reasons beyond identifier resolution. These contribute only negative examples to the contrastive loss.
    (d) Positive confirmation from successful compilations: When a formalization compiles successfully, all retrieved Mathlib dependencies that appear in the compiled formalization are confirmed positives.
    (e) Weighted InfoNCE contrastive loss: L_InfoNCE = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), where w_k = 1.0 for Tier 1 positives, w_k = 0.5 for Tier 2 positives, w_k = 1.0 for compilation-confirmed positives, and τ is the temperature (initialized at 0.07).
    (f) Decoupled optimization: The retriever's gradient does NOT flow through the formalizer's policy gradient. This alternating optimization prevents instability, following R3 (NeurIPS 2025) and Reinforced-IR (ACL 2025). After each retriever update, the FAISS index over Mathlib dependency embeddings is rebuilt.

  The graded error signal hierarchy ensures the retriever update loop has sufficient signal even on the hardest OOD domains where pure unknownIdentifier errors may be sparse. Phase -1's micro-analysis determines the empirical signal mix, allowing the weighting scheme to be calibrated before full-scale experiments.

**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** DDRL's three-component fix was designed for binary correct/incorrect rewards on informal math. Autoformalization's multi-tier reward has a continuous range. We adapt via binarize-then-enrich:

  (a) Binarization layer (for DDRL compatibility): Define binary acceptance r_accept = I(r_compile=1 AND r_critic=1). Compilation is a non-negotiable binary gate; the critic's precision (characterized in Phase 0 under distributional shift) makes it the most informative signal after compilation.
    - Balanced sampling: Partition K=32 candidates into 'accepted' (compile + critic approves) and 'rejected' (otherwise). Exclude problems where acceptance frequency is in the ambiguous zone (30-70%, i.e., ~10-22 of 32 accepted), following DDRL's insight that medium-consistency samples are the primary source of reward noise.
    - Fixed advantages: A_i = +1 for accepted candidates, A_i = -1 for rejected, eliminating GRPO's group-relative normalization that DDRL identifies as the amplification pathway.
    - Consensus-based off-policy refinement: After each TTRL epoch, sample M=128 formalizations per problem, apply acceptance filtering, perform rejection sampling on high-confidence samples (>80% acceptance rate), and run SFT on this high-quality dataset for 5 epochs.
  (b) GDPO-style enrichment layer (for BEq signal preservation): Among accepted candidates only, apply per-reward decoupled normalization for the BEq component. The BEq consensus density is normalized independently, preserving its ranking information without collapsing it into the binary acceptance signal. This adds an additive gradient bonus δ·norm(r_beq) to the fixed +1 advantage for accepted candidates, where δ=0.3 scales the enrichment relative to the debiased signal.
  (c) Methodological contribution: This binarize-then-enrich adaptation from single-reward to multi-tier debiased RL is applicable beyond autoformalization to any multi-tier reward where one component is continuous and others are binary.

**Phase 4 — Progressive Domain Curriculum for Test-Time Adaptation.** To break the bootstrapping problem (poor OOD retrieval → bad formalizations → noisy rewards → failed adaptation), we apply a progressive curriculum with quantitative transition criteria:

  (a) Near-distribution warm-start: TTRL on domains close to training data where retrieval coverage is high. Transition criterion (a)→(b): compilation rate ≥40%, critic approval rate ≥60% among compilable candidates, BEq@32 improves ≥3pp over pre-adaptation baseline. Timeout: T_max=500 GRPO steps.
  (b) Retrieval bootstrapping: Use the adapted model to generate improved formalization attempts on moderately OOD domains. Failed attempts with structured error signals (Tier 1 and Tier 2) feed the retriever's contrastive updates (Phase 2). Transition criterion (b)→(c): retrieval recall@10 ≥30% on bootstrapped queries, compilation rate on moderate-OOD ≥25%. Early transition: compilation rate plateaus (<2pp improvement over 200 consecutive steps).
  (c) Far-OOD adaptation: TTRL on truly OOD domains (algebraic geometry, condensed mathematics, MathAtlas MA-Hard) using the bootstrapped retriever and adaptive reward fallback (R = r_compile × r_critic when <4 candidates compile).

**Contribution Floor Analysis.** The three innovations are designed to be synergistic but are independently valuable, ensuring the paper makes a publishable contribution even under partial success:
  (1) Co-adaptive retrieval alone (Phase 2) + CriticLean TTRL (Phase 0-1): If binarize-then-enrich (Phase 3) provides only marginal gains over vanilla GRPO or plain DDRL, the paper still contributes the first co-adaptive retrieval mechanism for autoformalization exploiting Lean 4's structured error taxonomy, and the first application of TTRL to formal mathematics with a calibrated semantic critic. The co-adaptive retriever is an independent module that can be integrated into any RL-based autoformalization pipeline.
  (2) Binarize-then-enrich alone (Phase 3): If co-adaptive retrieval provides marginal gains (e.g., because static retrieval is already sufficient for near-OOD domains), the binarize-then-enrich adaptation of DDRL to multi-tier rewards is a standalone methodological contribution applicable to any domain with mixed binary/continuous rewards—not limited to autoformalization.
  (3) Progressive curriculum alone (Phase 4): If both innovations work but the curriculum provides marginal improvement over direct OOD adaptation, dropping Phase 4 simplifies the pipeline without losing the core contributions.
  (4) Essential floor: The minimal publishable contribution requires that CriticLean-guided TTRL outperforms compilation-only TTRL on OOD domains (validated in Phase 0) AND at least one of co-adaptive retrieval or binarize-then-enrich provides statistically significant improvement over the CriticLean TTRL baseline. Phase 0's go/no-go gate ensures we do not invest in the full pipeline unless the foundational premise holds.

**Evaluation.** Measure BEq@K and compilation success on FormalMATH's 5,560-problem multi-domain benchmark, Con-NF, CombiBench, and MathAtlas's MA-Hard (700 entities, average dependency depth 30, best current model: 2.6%).
  Same-scale comparisons (primary, all ~7-8B parameter models): (1) FormaRL (Qwen2.5-Coder-7B) as RL-without-retrieval baseline, (2) Online RL for Autoformalization (Wang et al.) as training-time RL baseline with composite rewards, (3) DRIFT with Qwen3-8B as strongest static retrieval baseline, (4) compilation-only TTRL and critic-only TTRL ablations, (5) standard GRPO vs. DDRL debiased vs. binarize-then-enrich (with separate ablations for each DDRL component and the GDPO enrichment layer), (6) frozen retriever vs. co-adaptive retriever during TTRL (isolating the value of compilation-error-driven retriever updates from natural query improvement), (7) Tier 1-only vs. Tier 1+2 vs. all-tier error signals (isolating the value of the graded error hierarchy), (8) no curriculum vs. progressive curriculum.
  Cross-scale reference points (for contextualizing absolute performance, NOT for claiming superiority): (9) ATF-32B as iterative refinement SOTA (94.51%/65.38% FormalMath-Lite/CombiBench), (10) ATLAS as SFT-only reference (70.08% pass@1 miniF2F), (11) Monotonic Refinement as inference-time orchestration upper bound (90.27% miniF2F, multi-model ensemble with GPT-4+ level models). All evaluation tables explicitly annotate model scale and compute budget to ensure fair interpretation.
  Sensitivity analysis: Dedicated ablation for N_ret ∈ {25, 50, 100} (retriever update frequency), as this controls the retriever-formalizer alternation and is critical for stability.

## Detailed Description

Current autoformalization models achieve strong in-distribution results but collapse on unfamiliar mathematical domains due to missing domain-specific Mathlib dependencies and fixed inference-time behavior. We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a framework making TTRL viable for autoformalization through three technical innovations. First, a dual-loop co-adaptive retrieval architecture where a DDR-style dense retriever is explicitly fine-tuned during test-time RL using a graded hierarchy of Lean 4 compilation error signals: Tier 1 signals from `lean.unknownIdentifier` errors (which explicitly name the missing Mathlib constant, providing direct hard negatives for InfoNCE training), Tier 2 signals from type mismatches and failed typeclass synthesis (providing softer retrieval signals via type-signature matching), and Tier 3 negative confirmation from other errors. This graded hierarchy addresses the key concern that not all OOD errors produce clean identifier signals—the prevalence of identifier errors is now established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv 2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are hallucination of non-existent theorems/definitions, DDR shows ~30% of ICL-generated dependencies are hallucinated identifiers, and the RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as one of two primary error classes. A Phase -1 micro-analysis (2-3 days, ~8 A100-hours) validates the error distribution on our specific OOD benchmarks before committing to the pipeline. Second, integration of CriticLean-14B (84.8% accuracy on balanced CriticLeanBench) as semantic RL reward, with explicit calibration under distributional shift: Phase 0 measures the critic's precision and recall SEPARATELY on the heavily skewed distribution expected during OOD TTRL (where >90% of candidates may be incorrect), reports calibration curves, and establishes a confidence gating threshold to maintain precision ≥80%—the conservative binarization (requiring BOTH compile AND critic approval) inherently prioritizes precision over recall. Third, a binarize-then-enrich adaptation of DDRL's binary debiasing to multi-tier rewards: binary acceptance (compile AND critic approval) provides DDRL's frequency-based balanced sampling and fixed ±1 advantages for debiasing, while GDPO-style per-reward decoupled normalization preserves BEq consensus density as a secondary ranking bonus among accepted candidates—this adaptation is itself a methodological contribution applicable beyond autoformalization. A progressive domain curriculum with quantitative transition criteria breaks the bootstrapping problem on OOD domains. Crucially, the three innovations are independently valuable: if binarize-then-enrich provides marginal gains, the paper still contributes the first co-adaptive retrieval for autoformalization and the first TTRL application to formal math with a calibrated semantic critic; if co-adaptive retrieval is marginal, binarize-then-enrich stands as a general methodology for multi-tier debiased RL. This contribution floor ensures publishable results even under partial success, with Phase 0's go/no-go gate preventing wasted effort on the foundational premise. Evaluation spans FormalMATH, Con-NF, CombiBench, and MathAtlas MA-Hard (best current: 2.6%), with same-scale comparisons (FormaRL, Online RL, DRIFT, ablations on error tiers and N_ret sensitivity) explicitly separated from cross-scale reference points (ATF-32B, Monotonic Refinement) to ensure fair interpretation. N_ret=50 GRPO steps between retriever updates is justified by signal accumulation: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle, sufficient for stable InfoNCE learning.

## Key References

- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)
- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)
- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv 2601.05242, NVIDIA, January 2026)
- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv 2507.06181, ByteDance/Nanjing)
- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)
- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv 2510.24652)
- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)
- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv 2601.11443, January 2026)
- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv 2602.01291, February 2026)
- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)
- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)
- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)
- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)
- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)
- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)
- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv 2025)
- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)
- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)
- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)
- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)
- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)
- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2605.14061, May 2026)
- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)
- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)
- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)
- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025)
- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv 2512.00997, Microsoft Research)

## Resource Estimate

- **manual**: gpu_hours: 950-1400 A100-80GB hours (Phase -1 error micro-analysis: ~8h; Phase 0 pilot with critic calibration: ~50h; base formalizer GRPO training with multi-tier reward: ~300h on 8 GPUs; DDR retriever fine-tuning + co-adaptive contrastive updates: ~100h on 4 GPUs; TTRL progressive adaptation across 3 curriculum stages with binarize-then-enrich DDRL and ablations: ~400h on 4 GPUs; CriticLean-14B inference during training: ~60h on 2 GPUs; N_ret sensitivity analysis: ~50h; error tier ablation: ~40h; evaluation: ~80h) + 10,000-15,000 CPU-hours for Lean 4 verification (128 parallel workers via Kimina Lean Server), timeline: 12-16 weeks (0.5 wk Phase -1 micro-analysis, 2-3 wk Phase 0 pilot + critic calibration + go/no-go, 3 wk base training + critic integration, 2 wk retriever co-adaptation infrastructure, 4 wk progressive TTRL experiments, 2-3 wk ablations including N_ret sensitivity and error tier analysis, 2 wk writing), estimated_gpu_cost: $1,900-$3,500 at ~$2.00/A100-hr + ~$500-$750 CPU verification costs
- **human_in_loop**: gpu_hours: 750-1100 A100-80GB hours (Claude handles Phase -1 analysis, Phase 0 calibration analysis, experiment scheduling; reduced ablation overhead ~25%) + 8,000-12,000 CPU-hours for Lean verification, timeline: 9-12 weeks (0.5 wk Phase -1; 2 wk Phase 0 with Claude-assisted calibration analysis; 3 wk base training + co-adaptive retriever; 3 wk progressive TTRL; 2-3 wk ablations + writing), claude_api_cost: $400-$700 (critic reward calibration, Phase -1/0 analysis, automated curriculum scheduling, ablation analysis), estimated_gpu_cost: $1,500-$2,700 + ~$400-$600 CPU costs
- **auto_research**: gpu_hours: 1600-2200 A100-80GB hours (automated hyperparameter sweeps over N_ret ∈ {25,50,100}, InfoNCE temperature τ, Tier 1/2 weighting, DDRL binarization ambiguity zone, GRPO group sizes K ∈ {16,32,64}, curriculum transition thresholds, enrichment weight δ, critic confidence threshold, plus multi-seed evaluation) + 20,000-30,000 CPU-hours for Lean verification at scale, timeline: 6-9 weeks (highly parallelized; Phase -1 in day 1-2 with automatic error taxonomy analysis; Phase 0 pilot in week 1-2 with automatic go/no-go gate and calibration analysis; wall-clock bottleneck is Lean 4 verification, mitigated by 128+ Kimina Lean Server workers), claude_api_cost: $800-$1,200 (automated experiment design, Phase -1/0 analysis, reward function ablation, curriculum optimization, paper drafting), estimated_gpu_cost: $3,200-$5,500 + ~$1,000-$1,500 CPU costs, speed_bottleneck: Lean 4 compilation latency (~3.65s per statement with warm LRU cache; ~0.10s amortized at 64 workers) dominates reward computation. CriticLean-14B inference adds ~0.5s per candidate on A100. Retriever co-adaptation adds ~15 min per update cycle (every N_ret GRPO steps) for re-encoding 26K Mathlib constants and rebuilding FAISS index.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4f8c06bd-a424-46fa-91e8-a4d8157f2cc9",
  "type": "user",
  "uuid": "f5a4a350-ac57-4119-b2ac-a8eb233f0808",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:24:43.975Z_

```json
{
  "parentUuid": "f5a4a350-ac57-4119-b2ac-a8eb233f0808",
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
  "uuid": "11a87d90-fc94-4443-b031-0072161a4aa7",
  "timestamp": "2026-05-28T05:24:43.975Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:24:43.975Z_

```json
{
  "parentUuid": "11a87d90-fc94-4443-b031-0072161a4aa7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "44242264-9ef5-4dfb-a6cc-186e1b265cad",
  "timestamp": "2026-05-28T05:24:43.975Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide my evaluation. Le…",
  "leafUuid": "44242264-9ef5-4dfb-a6cc-186e1b265cad",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Design TTRA for OOD autoformalization with test-time RL",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82"
}
```

---

### Assistant

_source line 8 · 2026-05-28T05:25:13.591Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

Let me extract the key data points:

**Reviewer 1:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [25% - 35%] 中位 30%
- Main risks: "Kitchen sink" combination paper, CriticLean OOD precision unverified

**Reviewer 2:**
- Novelty: 中
- Significance: 中


- Related Work: 强
- Probability: [23% - 33%] 中位 27%
- Main risks: "系统拼装" novelty concern, trivial alternative competitiveness

**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [22% - 33%] 中位 27%
- Main risks: "Kitchen sink" novelty, OOD incremental value vs trivial alternative

Now I'm computing the aggregate statistics across all three reviewers. The median probabilities cluster around 27-30%, with a mean of 28% and a median of medians at 27%. There's relatively low variance in their assessments, suggesting consistent concerns about the paper's novelty and the incremental value of the approach. Looking at where all three reviewers align, I see strong agreement on the paper's core weaknesses: the "kitchen sink" combination approach, the trivial alternative threat model, unverified assumptions about CriticLean's OOD precision, and limited novelty in the binarize-then-enrich component. They also converge that co-adaptive retrieval is the strongest novelty contribution and that significance is constrained by a niche audience. The only individual outliers are Reviewer 3 citing StepFun-Formalizer's AAAI 2026 acceptance as a positive signal and Reviewer 2 mentioning TTARAG as relevant prior work.

On significance, Reviewers 1 and 3 lean toward 中偏强 while Reviewer 2 sits at 中—a minor divergence I'd resolve toward 中偏强 given the 2-to-1 split. With novelty scores clustering tightly across the three intervals (R1: 25-35%, R2: 23-33%, R3: 22-33%) and a standard deviation under 1.5%, the consistency is high enough to anchor on the median range and tighten the bounds. The consensus picture is a well-executed combination paper where limited novelty is the binding constraint, despite solid related work coverage.

For the final probability estimate, I'm taking the median of the lower bounds (23%), the median of the upper bounds (33%), and the median of the midpoints (27%), which gives me [23%-33%] with a central estimate of 27%. This stays close to the consensus while respecting the high consistency across reviewers. Now I need to pull together the implementation assessment based on what the proposal claims about resource requirements and what the reviews say about feasibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44242264-9ef5-4dfb-a6cc-186e1b265cad",
  "isSidechain": false,
  "requestId": "req_011CbUQj1TE1JVRRU4KbaFWV",
  "type": "assistant",
  "uuid": "8373dbce-75ee-4d93-89c0-f808e00f0169",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3PqoXFeKZNvxjDWAP74Ea",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34400,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34400,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3535,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 34400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34400
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

_source line 9 · 2026-05-28T05:26:09.954Z_

【阶段】: Meta Judge
【三次中位】: [30%, 27%, 27%]  std=1.4%
【共识维度】:
- **Novelty: 中**（3/3 一致）— 核心贡献是多个已有技术的非平凡组合+领域适配，非根本性方法论创新。Co-adaptive retrieval exploiting Lean 4 error taxonomy 是最强新颖点，但更接近 domain-specific engineering insight 而非 new paradigm。Binarize-then-enrich 被 3 人一致判定为"近乎 obvious 的工程决策"。
- **Related Work: 强**（3/3 一致）— 覆盖 5 条研究脉络、25+ 篇论文（含 2026 最新工作），差异化定位清晰准确，数据引用经验证与原文一致。三位审稿人均认为这是 proposal 最突出的优势。
- **"Kitchen sink" / combination paper 质疑**（3/3 一致）— 审稿人最可能攻击的方向：4+ 个已有技术的工程组合，每个单独适配 novelty 有限，整体缺乏统一的 deep insight。
- **Trivial alternative 威胁**（3/3 一致）— 静态 DDR + CriticLean + vanilla GRPO（或 best-of-N）在 near-OOD 域可能已足够好，削弱 TTRA 增量价值。增量价值集中在 far-OOD 场景，但需实验证明增量是实质性的。
- **CriticLean OOD 分布偏移风险**（3/3 一致）— 84.8% accuracy 来自平衡 250/250 分布，OOD TTRL 的 >90% 错误偏斜分布下 precision 可能大幅下降。Phase 0 calibration 设计合理但前提本身尚未验证，是最关键的单点风险。
- **Tier 1 信号丰富度前提**（3/3 一致）— AMBER 47.3% 来自大模型 DeepSeek-R1，小模型 Qwen3-8B 在不同 OOD 域的错误分布可能有质的差异。Phase -1 设计了验证，但若 Tier 1 < 20%，co-adaptive retrieval 核心机制大打折扣。
- **Co-adaptive retrieval 稳定性未经验证**（3/3 一致）— R3/Reinforced-IR 在通用 NLP 验证，autoformalization 的 reward landscape 更稀疏离散，交替优化可能振荡。
【异常维度】:
- Significance 评级轻微分歧：R1/R3 判定"中偏强"，R2 判定"中"。2:1 倾向"中偏强"，但差异微小，不影响概率估计。
- R3 独有提及 StepFun-Formalizer 被 AAAI 2026 接收作为方向可行性佐证（正面信号但权重有限，不改变 novelty 评估）。
- R3 独有提及 ATF 94.51% 作为 trivial alternative 的组件（inference-time 方法无需权重更新），但 ATF 是 in-distribution 结果，不直接威胁 OOD 场景的价值主张。
【最终概率】: [23% - 33%] 中位 27%
【一致性】: 高（std=1.4% < 3%，三人在 Novelty/Related Work/主要风险上完全一致）
【综合理由】:
三位审稿人在所有关键维度上高度一致：Novelty 中、Related Work 强、核心风险集中在"combination paper 质疑"和"trivial alternative 竞争"。std=1.4% 属于高一致区间，取中位附近并缩窄区间。

中位定为 27% 而非三人算术均值 28%，原因是"宁缺毋滥"原则——两位审稿人独立给出 27%，仅一位给出 30%（且该审稿人的 Significance 评级略高于另两位）。在高一致情况下，偏向多数判断。

上界 33% 的支撑：co-adaptive retrieval with Lean 4 error taxonomy 若被审稿人视为 genuine domain-specific insight（而非 engineering）+ autoformalization 作为 2025-2026 热点方向（AAAI 2026 已有接收先例）+ 极其完善的 related work 和 de-risking 设计。

下界 23% 的支撑：若审稿人认为整体是"DDR + CriticLean + DDRL + GDPO 拼装"且 binarize-then-enrich 不够 principled + trivial alternative 在多数 benchmark 上已足够好 + 系统复杂度高导致 ablation 难以清晰归因。

核心限制因素：**Novelty 天花板**。三位审稿人一致认为，即使实验结果 positive（"更好的 retrieval + 更好的 reward + 更好的 RL = OOD 更好的表现"），审稿人的反应更可能是 "reasonable, I would have expected this" 而非 "surprising"。这将概率牢牢锚定在 30% 以下区间。Related Work 的强势和 Phase 0 de-risking 设计为下界提供了保障（不太可能低于 20%）。

【建议】: 边缘（中位 27% < 36% 通过线，但 idea 质量有明确的优化空间；建议进入迭代尝试提升 novelty 锐度，尤其聚焦 co-adaptive retrieval 的差异化深化和 binarize-then-enrich 的理论支撑强化）

【实施评估】:
  - 计算资源: 950-1400 A100-80GB GPU 小时（human-in-loop 模式 750-1100h），估算 GPU 成本 $1,500-$3,500；另需 10,000-15,000 CPU 小时用于 Lean 4 编译验证（128 并行 Kimina Lean Server workers），CPU 成本 $400-$750。总计算成本 $2,000-$4,250（human-in-loop 模式）。需要至少 4-8 块 A100-80GB 的持续访问权限。
  - 数据需求: DDR 500K 样本依赖数据集（公开）、CRAMF 26K Mathlib 概念索引（公开）、FormalMATH 5,560 题 benchmark（公开）、Con-NF（公开）、MathAtlas 52K 题（公开，May 2026）、CombiBench（公开）。所有关键数据集均为公开可得，无数据获取瓶颈。
  - 人工介入: Phase 0 需人工检查 200 条 critic 判断以计算 precision/recall（约 1-2 人日）；Phase -1 需人工验证错误分类准确性（约 0.5 人日）。其余环节可自动化。无需大规模人工标注。
  - 训练需求: 需要训练——Qwen3-8B base formalizer GRPO 训练（~300h on 8 GPUs）、DDR retriever 微调 + co-adaptive 更新（~100h on 4 GPUs）、TTRL progressive adaptation（~400h on 4 GPUs）。CriticLean-14B 使用预训练模型做推理，不需额外训练。
  - 新 Benchmark: 不需要构建全新 benchmark。使用现有的 FormalMATH、Con-NF、CombiBench、MathAtlas MA-Hard。Phase -1 的 1,000 条错误分析可视为小规模 diagnostic dataset，非正式 benchmark。
  - 预估周期: 9-16 周（取决于模式：human-in-loop 9-12 周，纯手动 12-16 周）。关键路径：Phase 0 pilot（2-3 周）→ Phase 1-2 基础训练 + retriever（5 周）→ Phase 3-4 TTRL 实验 + ablations（4 周）→ 写作（2 周）。瓶颈是 Lean 4 编译延迟（~3.65s/statement with warm cache）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8373dbce-75ee-4d93-89c0-f808e00f0169",
  "isSidechain": false,
  "requestId": "req_011CbUQj1TE1JVRRU4KbaFWV",
  "type": "assistant",
  "uuid": "ad03f457-d02a-4f5f-9645-8040020861d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3PqoXFeKZNvxjDWAP74Ea",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 34400,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3535,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 34400,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3535,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 34400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 34400
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide my evaluation. Le…",
  "leafUuid": "ad03f457-d02a-4f5f-9645-8040020861d7",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Design TTRA for OOD autoformalization with test-time RL",
  "sessionId": "7f00dd12-7cdf-413f-aa59-15c7a0f1ea82"
}
```

---
