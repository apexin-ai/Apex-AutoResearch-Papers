# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/18a4437d-51db-4c71-9343-a08b73d5c23e.jsonl`
- **Structured JSON:** [`3e53f7ad09bd40e66e22.json`](../../sessions/3e/3e53f7ad09bd40e66e22.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:42:27.850Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:42:27.850Z",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a thorough assessment. Let me compile my evaluation.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)](https://arxiv.org/abs/2605.18549) (May 2026): 最直接的竞争者之一。在 reasoning model 上用 per-token probe 构建轨迹，60+ 信号处理特征，max-pooling 达 91-97% AUROC。关键限制：完全没有 causal 维度，无法区分 faithful-correct vs. unfaithful-correct。ICG 的 probe 端正是要站在这个工作的肩上。\n- [Hidden Error Awareness (Yuan et al., arXiv 2605.09502)](https://arxiv.org/abs/2605.09502) (May 2026): 系统验证了 diagnostic-not-causal 现象——0.95 AUROC probe 准确率，但四种 intervention 全部失败。这是 ICG 框架立论的核心经验基础之一。非常新的工作，ICG 的 research question 直接建立在此发现之上。\n- [Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)](https://arxiv.org/abs/2603.01437) (March 2026): 发现 instruction-tuned model 上 steering 可以翻转答案 (>50%)，但 reasoning model 上翻转率 negligible。与 Yuan et al. 互相印证了 diagnostic-causal gap 在 reasoning model 上的独特性。\n- [Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)](https://arxiv.org/abs/2601.23163) (Jan 2026): 提出 truncation-reinjection 协议测量 behavioral C(t)，在 Qwen/GPT-OSS 上实验，accuracy 从 30-42% 升到 49-73%。关键限制：没有 hidden-state 测量，且明确 disclaims faithfulness 分析。ICG 的 C(t) 端直接继承此方法。\n- [FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)](https://arxiv.org/abs/2510.04040): 1000+ expert-annotated 轨迹，11 种检测方法的统一 benchmark。这是 ICG 的主要外部验证标准之一，也是头对头比较的关键对手。\n- [True Thinking Score / TTS (Zhao et al., arXiv 2510.24941)](https://arxiv.org/abs/2510.24941): per-step marginal causal contribution，AIME 上只有 2.3% 的步骤 TTS≥0.7。ICG 明确区分了 cumulative sufficiency (自己的 C(t)) vs. marginal contribution (TTS)。\n- [LLM Reasoning Is Latent (Wang, arXiv 2604.15726)](https://arxiv.org/abs/2604.15726) (April 2026): 形式化 H1(latent-mediated)/H2(CoT-mediated)/H0 假设，结论倾向 H1。ICG 声称可以操作化 H1/H2 区分。\n- [When Chains of Thought Don't Matter / CMI (Sathyanarayanan et al., arXiv 2602.03994)](https://arxiv.org/abs/2602.03994) (Feb 2026): layerwise activation patching 衡量 CoT 结构介导，~50 examples。ICG 区分了 structural mediation (CMI) vs. functional contribution (自己)。\n- [Thought Anchors (arXiv 2506.19143)](https://arxiv.org/abs/2506.19143): sentence-level counterfactual importance via 100-rollout replacement sampling，识别对推理轨迹有重大影响的 \"anchor\" 句子。提供 within-CoT 因果结构，但无 probe 外部参照。\n\n- **调研总结**: CoT faithfulness 是 2025-2026 年 NLP 可解释性最活跃的方向之一，probe 端和 causal 端各有大量独立工作，但确实没有人将二者在时间维度上统一。ICG 的 niche（dual-stream temporal gap）在文献中确实是空白的。但该领域竞争激烈、工作密集，多个同期竞争者可能在 proposal 完成前填补类似空白。\n\n【整体印象】:\n如果我是审稿人，第一反应是：这是一份学术功底极深、文献调研极其扎实的 proposal，研究问题真实且有价值。但第二反应是：(1) 框架核心操作——P*(t) 与 C(t) 的相减——在概念层面存在不可通约性问题；(2) 系统整体复杂度非常高，可能过度工程化；(3) faithfulness ground truth 的缺失使验证只能依赖间接代理。我会倾向 borderline，需要看实验结果才能决定 accept 或 reject。如果 Phase 0b 的效果量显著 (d > 0.5)，这会是一篇 solid 的贡献；如果效果量不够，整个框架的说服力会大打折扣。\n\n【核心贡献】:\n核心贡献是提出第一个能区分 \"faithful-correct\" vs. \"unfaithful-correct\" 推理的诊断框架：通过同时追踪模型内部的信息可用性 (probe) 和 CoT 文本的因果贡献 (behavioral intervention)，用二者的时间轨迹差异（G*(t) 形状）来分类不同的 faithfulness 现象。这个贡献对领域有中等偏高的价值——它试图将分散的 probe 和 causal 两大研究传统统一起来，如果成功，可以为 CoT faithfulness 提供一个更精细的诊断工具。但其价值很大程度上取决于 G*(t) 形状是否真的能稳健地区分不同现象。\n\n【方法合理性】:\n方法的整体设计方向是合理的——probe 端继承 Chrabąszcz/David/Yuan 的成熟方法，causal 端继承 Ballon 的 truncation-reinjection + 扰动方法，都有坚实的先验支撑。但存在三个核心问题：\n\n(1) **不可通约性**：P*(t) 是 AUROC（分类判别能力），C(t) 是 accuracy change（行为差异）。这两个量纲根本不同，直接相减在数学上没有意义。Proposal 承认了这一点并用 rank normalization + \"shapes over magnitudes\" 来辩护，但 rank normalization 后的轨迹形状仍然受到两个流各自 noise profile 和 granularity 的影响。如果 P*(t) 在 20 个 position 上平滑缓变，而 C(t) 因为 truncation 点数量有限而呈阶梯状，那么 G*(t) 的形状主要反映 C(t) 的离散化伪影，而非真正的 faithfulness 信号。这是一个比 proposal 承认的更严重的问题。\n\n(2) **更简单的替代方案**：一个显然的替代方案是不做减法，而是直接用 P*(t) 和 C(t) 各自的轨迹特征作为联合特征输入分类器。这避免了不可通约性问题，且可能获得类似甚至更好的分类性能。Proposal 确实在 ablation 中对比了 probe-only 和 TTS-only，但没有测试\"联合特征但不做 gap\"这个自然基线——审稿人几乎一定会问这个问题。\n\n(3) **Ground truth 缺失**：Faithfulness 本身缺乏可靠的 ground truth。FaithCoT-Bench 的 expert annotations 是目前最好的，但覆盖有限且主观性不可忽视。Proposal 使用 difficulty partition 和 TTS 作为外部验证，但这些都是间接代理——difficulty 和 faithfulness 的关系是 assumed 而非 proven 的。\n\n【5 维度打分】:\n  1. 研究问题: 【强】— Diagnostic-causal gap 是一个真实的、被多个独立团队验证的现象 (Yuan et al. 2605.09502, Cox et al. 2603.01437)，将其从 \"obstacle\" 转为 \"object of study\" 是一个有洞察力的 reframing。问题的重要性和时效性都很高。CoT faithfulness 是当前 NLP 可解释性的核心问题，对 AI safety 有直接意义。\n\n  2. 方法与创新: 【中】— Dual-stream 的概念框架是清晰的且填补了真实的文献空白（Chrabąszcz 无 causal，Ballon 无 probe，CMI 是 structural 而非 functional，Thought Anchors 无外部参照）。但创新主要在框架层面而非方法层面——个体组件 (linear probe, truncation-reinjection, paraphrase perturbation, NLDD) 全部是现有工具的组合。P*(t) 与 C(t) 的不可通约性是核心方法论弱点，shapes-over-magnitudes 的辩护虽有 trajectory 文献支撑 (arXiv 2603.18940, 2602.06266, 2604.05655)，但这些支撑来自不同上下文，对本场景的 transferability 未经验证。缺少\"联合特征但不做 gap\"这个自然消融基线。\n\n  3. 实验设计: 【强】— 这是 proposal 最突出的优点之一。5 models × 4 benchmarks 的覆盖面充分；Phase 0a/0b 的 go/no-go 门控是成熟的研究实践；7 维消融非常全面；多个外部验证标准 (TTS cross-reference, difficulty partition, FaithCoT-Bench)；cross-model 泛化测试 (train A → test B)；统计严谨性 (bootstrap CI, Bonferroni correction, permutation tests)。与领域标准 (FaithCoT-Bench 的 4 种方法, TTS) 的 head-to-head 对比也是该有的。但缺少\"P*(t)+C(t) 联合特征不做减法\"作为 baseline。instruction-tuned control (Qwen2.5-7B-Instruct) 作为 sanity check 也是好设计。\n\n  4. 可行性: 【中】— ~1050 H100-hours 在学术实验室可承受范围内；15-17 周时间线合理但紧张。主要风险：(a) NLDD 在自然 benchmark 上的可行性未验证（Phase 0a 测试，但如果失败需要调整方案）；(b) paraphrase perturbation 的语义保持验证 (NLI-based) 可能引入 noise；(c) 32B 模型上的 NLDD 是计算瓶颈 (250 hrs)；(d) 整个框架依赖 Phase 0b 的 d > 0.5 结果，如果不成立需要大幅降级。Phase 0b 的 go/no-go 设计是明智的，但也意味着有非零概率整个项目需要 pivot。\n\n  5. 写作与呈现: 【中】— Proposal 的逻辑结构清晰，文献定位极其精确（每个竞争者的优势和不足都有细致对比），预判并回应审稿人 objection 的做法非常专业。但过于密集——实际论文需要大幅精简，否则审稿人会因信息过载而降低好感。某些地方有 over-claim 风险（如 \"the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning\"——这在 P*(t)-C(t) 不可通约性未完全解决前是 aggressive 的 claim）。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n**向上因素**：(1) 研究问题真实、重要、时效性强；(2) 文献空白是真实存在的——确实没有 dual-stream temporal 框架；(3) 实验设计非常完备，go/no-go 门控、7 维消融、多重外部验证；(4) honest scoping（2 vs 3 category）是加分项；(5) 与 Thought Anchors、CMI、TTS、Chrabąszcz 的差异化论证清晰有力。\n\n**向下因素**：(1) P*(t) 与 C(t) 的不可通约性是核心方法论弱点，rank normalization + shapes 的辩护可能不足以说服严格审稿人；(2) 创新主要在\"框架组合\"而非\"方法突破\"——所有组件都是现有工具，审稿人可能判定为 engineering contribution；(3) ground truth 缺失，验证只能依赖间接代理，分类的 \"正确性\" 无法严格确认；(4) 该领域竞争极度激烈（2025-2026 已有 30+ 篇相关工作），提交时可能已有类似思路的工作出现；(5) 缺少\"联合特征不做 gap\"这个自然基线，审稿人大概率会指出。\n\n中位 35% 反映了这是一篇方向正确、设计扎实但存在核心方法论争议的 proposal。如果 Phase 0b 效果量优异且能补上\"不做 gap\"的消融，概率可上探 40%+。如果 G*(t) 形状的区分能力不够 robust，或审稿人对不可通约性严厉批评，概率会降到 28% 以下。\n\n【主要风险】:\n1. **P*(t)-C(t) 不可通约性遭到 fundamental objection**：审稿人认为 AUROC 与 accuracy change 的相减在概念上不成立，rank normalization 不足以解决问题，且\"shapes over magnitudes\"的辩护缺乏在本具体场景的直接验证。这可能被视为方法论的 fatal flaw。\n2. **\"组合而非创新\" 的评判**：审稿人认为框架只是将 Chrabąszcz 的 probe + Ballon 的 truncation 简单拼接，没有引入根本性的新洞察或新方法，核心贡献不足以达到 venue 标准。尤其是如果\"联合特征不做 gap\"的 baseline 表现与 G*(t) 相当或更好，会严重削弱框架的存在价值。\n\n【实施评估】:\n  - 计算资源: ~1050 H100-hours，约 $3,200（按 $3/hr），学术可承受。32B NLDD 是瓶颈 (250 hrs)。\n  - 数据需求: 公开 benchmark (GSM8K, MATH-500, GPQA-Diamond, AIME)，无需新数据收集。FaithCoT-Bench (ICLR 2026) 作为外部验证标准需确认 instance-level 数据可获取性。\n  - 人工介入: 无需人工标注（依赖已有 benchmark 和自动化方法）。Paraphrase 生成由 API 完成。\n  - 训练需求: 无大规模模型训练。需训练 linear probes（轻量）和小型分类器 (logistic regression/RF/MLP)。所有目标模型使用现有权重。\n  - 新 Benchmark: 不构建新 benchmark。TIF Score 是新指标但不是 benchmark。\n  - 预估周期: 15-17 周 (2 researchers) 或 12-14 周 (1 researcher + Claude)。Phase 0b 在第 4 周提供 go/no-go 信号。\n```\n\nSources:\n- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)\n- [Hidden Error Awareness (Yuan et al.)](https://arxiv.org/abs/2605.09502)\n- [Decoding Answers Before CoT (Cox et al.)](https://arxiv.org/abs/2603.01437)\n- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)\n- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)\n- [True Thinking Score / TTS (Zhao et al.)](https://arxiv.org/abs/2510.24941)\n- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)\n- [When Chains of Thought Don't Matter / CMI (Sathyanarayanan et al.)](https://arxiv.org/abs/2602.03994)\n- [Thought Anchors](https://arxiv.org/abs/2506.19143)\n- [Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al.)](https://arxiv.org/abs/2602.11201)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient context to provide a thorough assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Chrabąszcz et al., arXiv 2605.18549](https://arxiv.org/abs/2605.18549) (May 2026): 最直接的竞争工作。60+ signal-processing features on probe trajectories, 91-97% AUROC。但完全没有 causal component——这正是本 proposal 声称要填补的空白。该工作发表仅 2 天前（5月18日），说明该领域极度活跃。\n- [Yuan et al., arXiv 2605.09502](https://arxiv.org/abs/2605.09502) (May 2026): 核心 empirical foundation。证明 probe 可诊断但 4 种 causal intervention 全部失败，\"diagnostic not causal\"。本 proposal 将该发现从 obstacle 重新定义为 phenomenon，立意精准。\n- [Cox et al., arXiv 2603.01437](https://arxiv.org/abs/2603.01437) (March 2026): Pre-CoT probes predict answer with >0.9 AUC; steering works on instruction-tuned but fails on reasoning models。独立验证了 diagnostic-causal gap。\n- [Ballon et al., arXiv 2601.23163](https://arxiv.org/abs/2601.23163) (Jan 2026): Truncation-reinjection protocol providing behavioral C(t) curves。本 proposal 直接采用其方法作为 C(t) estimator 之一。\n- [FaithCoT-Bench, ICLR 2026](https://arxiv.org/abs/2510.04040): 1000+ expert-annotated trajectories, 11 detection methods。已被接收为 ICLR 2026 conference paper。本 proposal 将其作为 external validation 和 comparison baseline。\n- [Wang, arXiv 2604.15726](https://arxiv.org/abs/2604.15726) (April 2026): 形式化 H1 (latent-mediated) vs H2 (CoT-mediated) 假设。本 proposal 声称 ICG 可 operationalize 该区分。\n- [CMI / Sathyanarayanan et al., arXiv 2602.03994](https://arxiv.org/abs/2602.03994) (Feb 2026): Causal bypass via hidden-state patching, ~50 examples, structural mediation。本 proposal 正确区分了 structural vs functional faithfulness。\n- [Thought Anchors, arXiv 2506.19143](https://arxiv.org/abs/2506.19143) (June 2025): Per-sentence counterfactual importance via 100-rollout replacement。Within-CoT causal analysis 但无 probe reference。\n- [Kudo et al., EACL 2026](https://arxiv.org/abs/2412.01113): 最接近的先驱——per-position probes + activation patching，但限于 synthetic arithmetic。\n- [TTS / Zhao et al., arXiv 2510.24941](https://arxiv.org/abs/2510.24941): Per-step marginal ATE, only 2.3% AIME steps TTS≥0.7。提供 marginal causal contribution 但无 probe 维度。\n\n- 调研总结: CoT faithfulness 是 2025-2026 年 interpretability/alignment 领域最活跃的方向之一，已有大量 probe-only 和 causal-only 的工作，但确实没有已发表工作将 probe trajectories 与 causal contribution 统一到一个 temporal gap framework 中。该 proposal 的 niche（dual-stream temporal gap）在文献中确实是空白。但该领域极度拥挤且快速移动，window of opportunity 非常窄。\n\n【整体印象】:\n作为审稿人，我的第一反应是：这是一个 **极其 well-researched、positioning 精准的分析型 proposal**，对领域理解极深，literature coverage 几乎无遗漏。核心直觉——\"将 diagnostic-causal gap 本身作为研究对象，而非视其为障碍\"——是一个真正有洞察力的 reframing。\n\n但我同时有几个严重担忧：\n1. **Framework 复杂度过高**：ICG 涉及 P*(t)（多层 probe + null calibration + MCT concordance）和 C(t)（3种 estimator + aggregation + normalization），加上 7 个 ablation 维度、5 个模型、4 个 benchmark。这对一篇 8 页论文来说信息密度过大，有沦为\"measurement study\"的风险。\n2. **核心 contribution 的 novelty 边界模糊**：ICG 本质上是\"用已有方法 A 的输出减去已有方法 B 的输出\"。P*(t) 来自 Chrabąszcz/David/Zhang 等的 probe 方法，C(t) 来自 Ballon/TTS/NLDD。创新点在于 combination + temporal gap analysis，但 reviewer 可能质疑这是否是\"trivial combination\"。Proposal 自己预见了这个 objection 并给出了 cumulative vs marginal 的论证，但说服力取决于 empirical results。\n3. **Shape-based classification 的可靠性**：将 faithfulness phenomena 分类寄托于 G*(t) trajectory shapes（constant-high vs convergence vs widening），但 Phase 0b 的 success criterion 是 d > 0.5 between partitions。如果 d < 0.5，proposal 预注册降级为 characterization paper——这说明作者自己也不确定核心 claim 是否成立。\n\n倾向：**borderline accept**。如果实验结果强，有 accept 的可能；如果 Phase 0b 的 effect sizes 不够强或分类只有 2 categories，可能掉到 weak reject。\n\n【核心贡献】:\n1. 首次提出 dual-stream temporal gap framework (ICG)，将 probe-based information availability 和 causal contribution 统一到时间轴上，能够区分 faithful-correct 和 unfaithful-correct reasoning。\n2. G*(t) trajectory shape 作为 phenomenon fingerprint 的概念，可以 operationalize Wang 的 H1/H2 区分。\n3. Difficulty-conditioned gap analysis，回答\"在什么难度下 CoT 从 decorative 过渡到 load-bearing\"。\n4. 对 reasoning utilization efficiency 的实用意义（early-exit、benchmark validity、safety monitoring）。\n\n价值评估：如果 empirical results 强（d > 0.5，3 categories separable），这是一个高价值的 diagnostic tool，对 interpretability 和 alignment 社区有实质性贡献。如果 results 弱，价值降为\"又一个 measurement framework\"。\n\n【方法合理性】:\n方法在逻辑上是合理的——分别测量 information availability 和 causal contribution 然后计算 gap——但有几个 concerns：\n\n1. **P*(t) 和 C(t) 的可比性**：Proposal 承认两者\"measured via fundamentally different methods with non-commensurable scales\"，并采用 rank-based normalization。但 rank normalization 会丢失 magnitude 信息，而 proposal 又声称 shapes 才是关键。这个 tension 是否真的被 resolved 值得审视。\n2. **C(t) 的 aggregation**：三种 estimator（prefix truncation, paraphrase, NLDD）测量的是不同的东西——cumulative sufficiency、content independence、positional degradation。将它们 aggregate 的理论依据不够强。Young (2603.20172) 已证明不同 faithfulness metrics 之间 kappa 可低至 0.06，说明 aggregation 可能掩盖而非增强信号。\n3. **更简单的替代方案**：直接用 Chrabąszcz 的 probe trajectory features + Ballon 的 truncation accuracy，不做 gap 计算，而是做 multi-feature classification，可能达到类似甚至更好的效果。Proposal 需要证明 gap formulation 提供了超越 simple feature concatenation 的 insight。\n\n【5 维度打分】:\n\n1. 研究问题: [强] — \"模型知道答案但 CoT 并未使用这个知识\"是 2025-2026 年被多组独立验证的核心现象（Yuan et al., Cox et al., Esakkiraja et al.）。将 diagnostic-causal gap 本身作为研究对象而非障碍是一个有价值的 reframing。FaithCoT-Bench (ICLR 2026) 已确认 15-20% correct answers 配对 unfaithful CoTs，验证了问题的实际存在。这个问题对 AI safety（monitoring hidden reasoning）和 efficiency（early-exit compute）都有直接影响。\n\n2. 方法与创新: [中] — ICG 的 novelty 在于 combination 和 temporal gap formulation，而非底层方法（probe 来自多组前人工作，C(t) 来自 Ballon/TTS/NLDD）。与 Chrabąszcz et al. (2605.18549) 相比，ICG 增加了 causal 维度；与 CMI (2602.03994) 相比，ICG 是 functional 而非 structural。区分是清晰的，但 reviewer 可能质疑 gap = P*(t) - C(t) 是否比 feature concatenation 更有信息量。Proposal 对 cumulative vs marginal 的论证（对标 TTS vs Ballon）是一个合理的 preemption，但最终需要 empirical 支撑。Kudo et al. (EACL 2026) 已在 synthetic data 上做了 probe + causal combination，ICG 的增量在于 natural benchmarks + temporal gap formulation。\n\n3. 实验设计: [强] — 这是 proposal 最出色的部分。Phase 0a/0b 的 go/no-go 设计非常成熟；external validation 通过 difficulty partition 和 TTS cross-reference（而非仅依赖 P*/C 自身的 partition）是方法论上的亮点；7 维 ablation 覆盖了几乎所有合理的 robustness concern；head-to-head 比较 probe-only、TTS-only、FaithCoT-Bench 方法提供了清晰的 contribution 量化。5 models × 4 benchmarks（含 instruction-tuned control 作 sanity check）的规模对分析型工作来说充分。与 Young (2603.20172) 的 measurement sensitivity 发现直接对话（报告 inter-estimator kappa）也是加分项。唯一的 concern 是规模可能导致论文过于 dense。\n\n4. 可行性: [中] — ~1050 H100-hours 和 15-17 周在学术组可行但不轻松。主要风险在于：(a) NLDD 在 32B 上的 250 hrs bottleneck 且 Phase 0a 可能判其不可行；(b) paraphrase perturbation 的 API cost（$800-1500）和质量控制；(c) 3-5 TB hidden state 存储需要 engineering。好的方面是 Phase 0a 的早期 go/no-go 设计降低了 sunk cost 风险。如果 NLDD 在 Phase 0a 被 gated out，C(t) 只剩两个 estimator，可能削弱 robustness claim。\n\n5. 写作与呈现: [中] — Proposal 的 literature positioning 极其精准，每个 related work 的区分都有清晰论证。但写作上存在几个问题：(a) 信息过载——一篇 8 页论文要呈现 dual-stream framework + 3 C(t) estimators + 7 ablation + 5 models × 4 benchmarks + difficulty conditioning + TIF score + classification + head-to-head + 671B subset + MCT supplementary + semi-synthetic simulation，几乎不可能在有限篇幅内清晰呈现；(b) framing 偏向 measurement framework，缺少 actionable insight 的前置承诺（beyond \"we can classify phenomena\"，so what？）；(c) phenomenon taxonomy 的 honest scoping（2 vs 3 categories）虽然诚实但也传递了不确定性。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n上界理由 (42%): 如果 Phase 0b 验证成功（d > 0.5, 3 categories separable），shape-based classification 显著优于 probe-only 和 TTS-only baselines，且论文成功聚焦核心 contribution 而非 exhaustive ablation，这将是一篇 solid 的 analysis paper。研究问题的 timeliness（2025-2026 最热话题之一）和实验设计的 rigor 是明确加分项。EMNLP 历来接收高质量的 analysis/interpretability 工作。\n\n下界理由 (28%): (1) 最大风险是 novelty 争议——\"已有方法 A 的输出减已有方法 B 的输出\"可能被 reviewer 视为 incremental combination 而非 fundamental contribution；(2) 如果 Phase 0b effect sizes 不强或 phenomenon taxonomy 坍缩为 2 categories，核心 claim 被削弱；(3) 论文信息密度过高可能导致关键 insight 被淹没；(4) 该领域极度拥挤且快速移动（Chrabąszcz 5月18日才出，Thought Anchors 6月出），在 submission 前可能出现更直接的竞争工作。\n\n中位 35%: 方向正确、实验设计 solid、但 novelty 有争议性且 execution risk 不低。属于\"如果结果强则有希望，但需要 empirical results 来证明 gap formulation 的 added value\"的 proposal。\n\n【主要风险】:\n1. **Novelty 被质疑为 trivial combination**: 审稿人可能认为 ICG = probe trajectory (existing) + causal measurement (existing) 的简单拼接，gap subtraction 不构成足够的方法论创新。Proposal 预见了这一点并给出了 cumulative vs marginal 论证，但如果 ablation 显示 feature concatenation（不做 gap）效果类似或更好，核心 claim 就不成立。\n2. **Phenomenon classification 结果弱**: 如果 G*(t) trajectory shapes 在不同 faithfulness phenomena 之间没有足够大的 effect size（d < 0.5），或 3-category 分类坍缩为 2-category，论文从\"diagnostic framework\"降级为\"characterization study\"，显著降低 impact。在这个竞争激烈的领域，一篇\"我们看了这个 gap 但它没有特别能区分什么\"的论文很难被接收。\n\n【实施评估】:\n  - 计算资源: ~1050 H100-hours (~$3,200)，中等规模，学术组可负担但需要稳定 GPU 集群。NLDD 32B (250 hrs) 是单项最大开销，Phase 0a 可 gate。\n  - 数据需求: 使用现有公开 benchmark（GSM8K, MATH-500, GPQA-Diamond, AIME），无需构建新数据集。FaithCoT-Bench 的 instance-level labels 如可获取将显著增强 validation。\n  - 人工介入: 低。Probe training、C(t) estimation、classification 均可自动化。Paraphrase 需要 NLI-based 质量验证。主要人工投入在实验设计和论文写作。\n  - 训练需求: 轻量级——仅训练 linear probes 和浅层 classifiers（LR/RF/MLP），不涉及 LLM fine-tuning。\n  - 新 Benchmark: 不需要。TIF score 作为 derived metric 但不构成独立 benchmark。\n  - 预估周期: 15-17 周（2 researchers）/ 14 周（1 researcher + Claude）。Phase 0b 在第 4 周提供 early go/no-go。整体 timeline 紧凑但可行。\n```\n\nSources:\n- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)\n- [Hidden Error Awareness (Yuan et al.)](https://arxiv.org/abs/2605.09502)\n- [Decoding Answers Before CoT (Cox et al.)](https://arxiv.org/abs/2603.01437)\n- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)\n- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)\n- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)\n- [When Chains of Thought Don't Matter: Causal Bypass / CMI](https://arxiv.org/abs/2602.03994)\n- [Thought Anchors](https://arxiv.org/abs/2506.19143)\n- [Breaking the Chain (Somov et al.)](https://arxiv.org/abs/2603.16475)\n- [Measuring Faithfulness Depends on How You Measure (Young)](https://arxiv.org/abs/2603.20172)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient context from the literature to provide a thorough evaluation. Let me compile my assessment.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Chrabąszcz et al., arXiv 2605.18549] (May 2026): Probe trajectories with 60+ signal-processing features (volatility, trend, autocorrelation) achieving 91-97% AUROC on harmfulness detection. Most directly competitive work for the P*(t) dimension — BUT entirely lacks a causal component, cannot distinguish faithful-correct from unfaithful-correct reasoning. ICG's closest \"upstream\" building block.\n- [Yuan et al., arXiv 2605.09502] (May 2026): Establishes the \"diagnostic not causal\" finding — probes achieve 0.95 AUROC on correctness, but all four intervention strategies (steering, best-of-N, self-correction, patching) fail on reasoning models. This paper IS the empirical foundation that motivates ICG.\n- [Cox et al., arXiv 2603.01437] (Mar 2026): Pre-CoT probes predict answers at >0.9 AUC; activation steering flips answers on instruction-tuned models but produces \"negligible flip rates\" on reasoning models. Independently confirms Yuan et al.'s diagnostic-causal gap, strengthening ICG's motivation.\n- [Ballon et al., arXiv 2601.23163] (Jan 2026): Truncation-reinjection protocol measuring behavioral accuracy trajectory with three control conditions (random, swapped, shuffled). Provides the C(t) measurement methodology ICG proposes to adopt. Explicitly disclaims faithfulness analysis — leaving the gap ICG claims to fill.\n- [CMI / Sathyanarayanan et al., arXiv 2602.03994] (Feb 2026): Layerwise activation patching measuring CoT Mediation Index on ~50 examples. Measures *structural* mediation (representation routing) not *functional* contribution (behavioral text causation). Small scale, different question. ICG's differentiation claim is valid.\n- [TTS / Zhao et al., arXiv 2510.24941] (Oct 2025): Per-step ATE showing only 2.3% of AIME steps have TTS≥0.7. Measures *marginal* step contribution; ICG proposes *cumulative sufficiency* — a theoretically distinct quantity. ICG plans TTS as external validation benchmark.\n- [Wang, arXiv 2604.15726] (Apr 2026): Formalizes H1 (latent-mediated) / H2 (CoT-mediated) / H0 (generic compute) hypotheses. ICG claims to operationalize H1/H2 distinction via G*(t) — this is a legitimate claim if the framework works.\n- [FaithCoT-Bench, ICLR 2026, arXiv 2510.04040]: 1000+ expert-annotated trajectories, 11 detection methods, 4 paradigms. The current gold standard for faithfulness evaluation. ICG proposes to validate against this — essential baseline.\n- [Thought Anchors, arXiv 2506.19143] (Jun 2025): Per-sentence counterfactual importance via 100-rollout replacement sampling. Provides within-CoT causal structure but no probe dimension — cannot assess whether an \"anchor\" is redundant relative to internal state. ICG's differentiation is sound.\n- [Gjølbye et al., arXiv 2605.15454] (May 2026): Difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). Motivates ICG's difficulty conditioning and length correction.\n- [Kudo et al., EACL 2026, arXiv 2412.01113]: Probes + activation patching on synthetic arithmetic, 9 models. Closest prior work combining probes with causal intervention — but restricted to synthetic tasks, no temporal coverage on natural benchmarks, no phenomenon taxonomy.\n\n- **调研总结**: CoT faithfulness is a rapidly maturing subfield with multiple independent measurement traditions (probe-based and behavioral-causal) that have developed in parallel but remain unintegrated. The specific niche ICG claims — a dual-stream temporal gap metric combining P*(t) and C(t) for instance-level faithfulness diagnosis — is genuinely unoccupied. However, the field is moving fast (Chrabąszcz, Yuan, Gjølbye all from May 2026), and concurrent work risk is substantial.\n\n【整体印象】:\nIf I were reviewing this paper, my first reaction would be: *this is an impressively thorough and well-motivated analysis paper with a genuine research gap, but I'd want to see that the core metric actually works as claimed.* The diagnostic-causal gap (probes detect but interventions fail) is one of the most striking empirical findings in recent interpretability research, and framing this gap itself as the object of study is a clever conceptual move. The honest scoping (pre-registering 2-category as acceptable outcome) shows research maturity.\n\nMy concern would center on whether G*(t) = P*(t) − C(t) is a well-defined quantity given that P*(t) and C(t) are measured via fundamentally different methodologies with non-commensurable scales. The proposal acknowledges this and proposes rank-based normalization plus shapes-over-magnitudes, but this is the kind of thing that either works beautifully in practice or produces noisy, hard-to-interpret results. I would lean toward a weak accept / borderline, conditional on execution quality.\n\n【核心贡献】:\nThe core contribution is a **diagnostic framework (ICG) that can distinguish faithful-correct from unfaithful-correct reasoning** by jointly tracking what the model knows (probe trajectories) and what the CoT causally contributes (behavioral measurement). This fills a genuine gap: probe-only methods (Chrabąszcz) detect internal knowledge but are blind to whether CoT caused the output; causal-only methods (TTS, Ballon) measure CoT's effect but are blind to what the model already knew. The temporal trajectory shape analysis — using G*(t) profiles to classify faithfulness phenomena — is the specific technical novelty.\n\nValue to the field: **High, if it works.** The ability to distinguish decorative from genuine reasoning at the instance level has direct implications for inference-time compute optimization, benchmark validity, and safety monitoring. However, the contribution is primarily diagnostic/analytical rather than prescriptive — it tells you *what's happening* but doesn't directly fix unfaithful reasoning.\n\n【方法合理性】:\nThe method is conceptually sound but has several methodological concerns:\n\n1. **Commensurability**: G*(t) = P*(t) − C(t) subtracts probe AUROC from behavioral accuracy change. Even with rank normalization, the subtraction assumes these quantities are meaningfully comparable at each time point. The shapes-over-magnitudes argument is the strongest defense, but it raises the question: if only shapes matter, why define G*(t) as a subtraction at all? Why not simply analyze P*(t) and C(t) trajectories side-by-side with a joint classifier?\n\n2. **Simpler alternatives**: A reviewer might ask: \"Why not just compute the Spearman correlation between P*(t) and C(t) trajectories?\" If they're aligned (faithful), ρ ≈ 1; if not, ρ << 1. This is simpler, avoids commensurability issues, and captures alignment/divergence directly. The proposal would need to argue that the subtraction provides additional information over correlation — e.g., distinguishing *directionality* (model knows more than CoT uses vs. CoT assembles new knowledge).\n\n3. **C(t) aggregation complexity**: Three estimators (prefix truncation, paraphrase perturbation, NLDD) with multiple aggregation schemes adds substantial methodological complexity. Each estimator has its own assumptions and failure modes. The proposal handles this with ablations, but the risk is that the framework becomes too complex for reviewers to evaluate cleanly.\n\n4. **Validation bootstrapping**: Without ground truth labels for \"faithful\" vs. \"unfaithful,\" all validation is necessarily indirect (TTS cross-reference, difficulty partition, FaithCoT-Bench correlation). This is acknowledged but remains a fundamental limitation.\n\n5. **The cumulative-vs-marginal distinction** between prefix C(t) and TTS is well-articulated and theoretically sound. This is a genuine insight.\n\n【5 维度打分】:\n\n1. **研究问题: 强** — The diagnostic-causal gap is one of the most compelling empirical puzzles in the current interpretability literature, established by multiple independent groups (Yuan et al., Cox et al.). The question \"does the model's CoT faithfully mediate its reasoning, or is it decorative?\" is both scientifically important (understanding what reasoning models actually do) and practically relevant (inference efficiency, safety). The reframing of the gap-as-phenomenon rather than gap-as-obstacle is a genuine intellectual contribution.\n\n2. **方法与创新: 中** — The dual-stream temporal gap is a natural and well-motivated framework. The niche is genuine — no existing work combines probe P*(t) with causal C(t) (Chrabąszcz lacks causal; Ballon/TTS lack probes; CMI measures structural not functional mediation; Kudo et al. is synthetic-only). However, the novelty is primarily in *combination* rather than in *new techniques* — both the probe methodology and the causal measurement methodology are adopted from existing work (Hewitt & Liang calibration, Chrabąszcz-style evaluation, Ballon-style truncation). The shapes-over-magnitudes approach is supported by external evidence (entropy trajectories, RQA, Microsoft trajectory geometry) but remains to be validated for this specific application. The commensurability concern is real and the rank-normalization solution, while reasonable, may not fully satisfy methodologically rigorous reviewers.\n\n3. **实验设计: 强** — This is the proposal's clear strength. The experimental design is remarkably thorough:\n   - 5 models spanning 2 architecture families + instruction-tuned control (sanity check)\n   - 4 benchmarks covering different reasoning domains\n   - Phase 0a/0b with explicit go/no-go gates (d > 0.5 or downscope)\n   - External validation via TTS cross-reference, difficulty partition, and FaithCoT-Bench\n   - 7-dimension ablation suite (probe architecture, layer selection, C(t) estimator agreement, normalization, calibration method, probe target, temporal resolution)\n   - Head-to-head baselines (probe-only, TTS-only, random, majority-class, difficulty-only)\n   - Statistical rigor (bootstrap CI, Bonferroni correction, permutation tests)\n   - Cross-model generalization test (train A → test B)\n   This exceeds the experimental standards of most published papers in this area (cf. CMI on ~50 examples, Kudo on synthetic arithmetic). FaithCoT-Bench (ICLR 2026) establishes the evaluation standard and the proposal plans to validate against it.\n\n4. **可行性: 中** — The ~1050 H100-hour budget is reasonable (~$3,200), and the phased approach with early go/no-go decisions is smart project management. However, the 15-17 week timeline with 2 researchers is aggressive given the complexity (3 C(t) estimators × 5 models × 4 benchmarks × 7 ablation dimensions). Storage (3-5 TB for hidden states) is manageable. The main feasibility risk is that the Phase 0b pilot might fail (d < 0.5), which the proposal honestly acknowledges would trigger downscoping. The conditional NLDD inclusion adds flexibility. The 32B model (QwQ-32B) computation for NLDD (~250 hrs) is the primary bottleneck, appropriately flagged.\n\n5. **写作与呈现: 中** — The proposal demonstrates exceptional command of the literature and proactive objection-handling (addressing TTS marginal-vs-cumulative, CMI structural-vs-functional, Thought Anchors within-CoT-vs-external, endpoint comparison, and trivial combination objections). However, the proposal itself is *extremely* dense and long. Distilling this into an 8-page paper while maintaining clarity will be a significant challenge. The risk is that the paper becomes impenetrable to reviewers who are not deeply familiar with this exact subfield. The interpretive caveats (G*(t) >> 0 ≠ intentional withholding) show commendable intellectual honesty.\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\nThis proposal sits in the solid-but-not-outstanding range. The research question is strong (a genuine, important puzzle in the current literature), the experimental design is comprehensive (exceeding most published work in this area), and the honest scoping shows research maturity. These factors push toward the upper end.\n\nHowever, several factors limit the estimate:\n(a) The core methodological contribution (combining existing probe and causal techniques via a gap metric) may be perceived as incremental rather than fundamentally novel — it's a well-motivated combination, not a new technique.\n(b) The commensurability concern (subtracting probe AUROC from behavioral accuracy change) is a real methodological question that could draw reviewer skepticism, even with the shapes-over-magnitudes defense.\n(c) The extreme density of the proposal (dozens of referenced papers, multiple estimators, 7 ablation dimensions) risks producing a paper that is difficult to parse in review. The core message needs to be crystal clear.\n(d) The field is moving extremely fast (multiple relevant papers from May 2026 alone), creating significant concurrent work risk. By the time this paper is submitted, additional competing frameworks may exist.\n(e) All validation is indirect — the absence of ground truth for faithfulness classification is a fundamental limitation shared by the field, but it still constrains the strength of claims.\n\nThe 35% median reflects a paper that is well-above-average in preparation and experimental design, tackling an important question, but facing methodological concerns that could split a review panel.\n\n【主要风险】:\n1. **Commensurability challenge**: The core metric G*(t) = P*(t) − C(t) subtracts two fundamentally different quantities. Even with rank normalization and the shapes-over-magnitudes argument, a skeptical reviewer may argue this is methodologically unsound — and may propose simpler alternatives (e.g., correlation-based alignment measures) that undermine the need for ICG's specific formulation.\n2. **Concurrent work saturation**: The field is experiencing an extraordinary density of new work (Chrabąszcz, Yuan, Gjølbye, Thought Anchors, and others all in 2025-2026). By submission time, a concurrent paper may occupy a substantially similar niche (e.g., Chrabąszcz adding a causal dimension, or TTS adding a probe dimension), eroding novelty claims.\n\n【实施评估】:\n  - 计算资源: ~1050 H100-hours (~$3,200) — reasonable and well-budgeted; QwQ-32B NLDD is main bottleneck (~250 hrs conditional)\n  - 数据需求: GSM8K, MATH-500, GPQA-Diamond, AIME — all publicly available; FaithCoT-Bench for validation — publicly available (ICLR 2026)\n  - 人工介入: Minimal — framework is automated; some judgment in phenomenon taxonomy interpretation and Phase 0b go/no-go decision\n  - 训练需求: Linear probes only (lightweight); no LLM fine-tuning; paraphrase generation via API (Claude Haiku/GPT-4o-mini, ~$800-1500)\n  - 新 Benchmark: No new benchmark required; proposes TIF score as a diagnostic metric but validates against existing benchmarks\n  - 预估周期: 15-17 weeks (2 researchers) / 12-14 weeks (with AI assistance) — aggressive but feasible given phased structure with go/no-go gates\n```\n\nSources:\n- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)\n- [Hidden Error Awareness in CoT Reasoning (Yuan et al.)](https://arxiv.org/abs/2605.09502)\n- [Decoding Answers Before Chain-of-Thought (Cox et al.)](https://arxiv.org/abs/2603.01437)\n- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)\n- [When Chains of Thought Don't Matter: CMI (Sathyanarayanan et al.)](https://arxiv.org/abs/2602.03994)\n- [Can Aha Moments Be Fake? TTS (Zhao et al.)](https://arxiv.org/abs/2510.24941)\n- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)\n- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)\n- [Thought Anchors (arXiv 2506.19143)](https://arxiv.org/abs/2506.19143)\n- [Reasoning Models Move Differently (Gjølbye et al.)](https://arxiv.org/abs/2605.15454)\n- [Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al.)](https://arxiv.org/html/2602.11201v1)\n- [Breaking the Chain (Somov et al.)](https://arxiv.org/html/2603.16475v1)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWhen a reasoning model gets the right answer, is its chain-of-thought the reason it succeeded — or did it already know the answer and generate decorative reasoning? No existing method can answer this question. Probe-only approaches (Chrabąszcz et al., 2605.18549) reveal what the model knows over time but are structurally blind to whether CoT caused the correct output. Causal-only approaches (TTS, Zhao et al. 2510.24941; NLDD, Ye et al. 2602.11201; Ballon et al. 2601.23163) measure what CoT does but cannot assess what the model already knew internally. Only a dual-stream framework — jointly tracking information availability AND causal contribution — can distinguish faithful-correct from unfaithful-correct reasoning. The Information-Contribution Gap (ICG) framework provides this.\n\nICG exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al. 2603.01437: negligible flip rates; Yuan et al. 2605.09502: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study.\n\nThe framework tracks two calibrated time-varying quantities across the CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation following Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\n**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape, not its absolute magnitude.** P*(t) (probe AUROC) and C(t) (behavioral accuracy change) are measured via fundamentally different methods with non-commensurable scales. We address this via rank-based normalization as primary scheme, but more fundamentally, trajectory-shape profiles carry the diagnostic signal: a model that pre-encodes the answer shows a constant-high shape; genuine reasoning shows convergence toward zero; post-hoc rationalization shows widening. The shapes-over-magnitudes approach is validated by: entropy trajectory monotonicity predicting reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperforming aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieving 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).\n\n**Why not just endpoint comparison or trivial combination?** Two reviewer objections are preempted: (1) \"Why not correlate pre-CoT probe accuracy with final correctness?\" — endpoint comparison detects unfaithfulness presence but collapses distinct failure *mechanisms* (pre-CoT encoding vs. rationalization vs. late shortcutting produce identical endpoints but distinct G*(t) shapes). (2) \"Why not just pair Chrabąszcz's probe trajectories with TTS step scores?\" — TTS measures *marginal* contribution (removing step *s* changes the answer), while prefix-truncation C(t) measures *cumulative sufficiency* (CoT[:t] is sufficient for correctness). A chain where every individual step has low TTS (each individually replaceable) could still have high cumulative C(t) (the ensemble is necessary). This cumulative-vs-marginal distinction is theoretically non-reducible and empirically grounded in the difference between Ballon et al.'s monotonic prefix curves and TTS's per-step ATE.\n\n**Structural vs. functional differentiation from CMI.** The CMI framework (Sathyanarayanan et al., 2602.03994) measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question. ICG answers a *functional* question: does the CoT text causally contribute to behavioral correctness? This generates a testable prediction: models could show high CMI (representations routed through CoT-processing layers) but high G*(t) (CoT serves as timing scaffold rather than contributing semantic content). If confirmed, this would reveal a novel structural-functional dissociation in reasoning models.\n\n**Differentiation from Thought Anchors.** Thought Anchors (arXiv 2506.19143) measures per-sentence counterfactual importance via replacement sampling — identifying sentences with outsized causal influence on reasoning trajectory. This provides *within-CoT structural analysis* (which sentences matter to each other) but no *external reference* to the model's internal state. A thought anchor could be causally critical within the CoT but entirely redundant relative to what the model already knows — a distinction only ICG can make via the probe dimension.\n\n**Interpretive boundary.** G*(t) >> 0 means correctness-correlated information is present but not causally channeled through CoT. It does not entail the model \"decided to withhold\" — the information may exist as computational byproducts rather than semantically actionable knowledge. Chun et al.'s MCT geometric pulse finding (2602.20338) provides evidence of this possibility. We report interpretations with this caveat.\n\n**Practical significance: reasoning utilization efficiency.** G*(t) provides a unified diagnostic for reasoning utilization: G*(t) ≈ 0 means full utilization (knowledge channeled through CoT); G*(t) >> 0 means waste (CoT is decorative overhead); G*(t) < 0 means productive computation (CoT assembles new information). This framing connects to three practical domains: (a) *inference-time compute allocation* — skip CoT generation when G*(t) >> 0 for easy problems, providing the principled diagnostic that current early-exit heuristics (ESTAR, DTSR, FRIT, CoDE-Stop) lack; (b) *benchmark validity* — problems where all models show persistent G*(t) >> 0 are not testing reasoning; (c) *safety monitoring* — the decoupled internal quality-monitoring system (Yuan et al.) is the kind of hidden computation alignment researchers worry about.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. The boundary between pre-CoT encoding and post-hoc rationalization may be empirically blurred (in both cases, the model may have committed to an answer before CoT begins, so P*(t) starts high in both), potentially collapsing the taxonomy to 2 primary categories (pre-committed vs. genuinely reasoning). Phase 0b explicitly tests 2-category vs. 3-category separability; either outcome is a strong contribution. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling (ρ⊥ = +0.41 on Codeforces) — reveals the decorative→load-bearing transition with length correction.\n\nCore contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 5 models (4 reasoning + 1 instruction-tuned control) × 4 benchmarks, the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning; (b) empirical pilot with external validation (TTS cross-reference, difficulty partition, FaithCoT-Bench supplementary) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories. Total compute: ~1050 H100-hours.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four interventions (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B and report ALL fail. This diagnostic-causal gap is NOT an obstacle; it IS the central phenomenon.\n\nThe literature conflates two probe targets: answer-content probes (Cox et al.: specific answer on binary tasks, ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: right/wrong on models up to 72B; Zhang et al. 2504.05419: per-chunk correctness on 7B-70B). Answer-content gaps mean 'the model has decided but CoT doesn't derive the answer'; correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.'\n\nTemporal dynamics are empirically grounded: David (2511.14773) finds probe accuracy at 0.84 AUC by token 4, stable ~0.8 through token 100, with easy (0.84) vs. hard (0.76) splits. Zhang et al. (2504.05419) report 65%→79% chunk trajectories on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with characteristic dip at 5-10%. Chrabąszcz et al. (2605.18549) demonstrate 60+ signal-processing features achieving up to 17pp over static probes. Yet no framework jointly tracks information availability AND causal contribution: Chrabąszcz et al. lack any causal component; Ballon et al. (2601.23163) provide behavioral C(t) but no hidden-state measurement; CMI (2602.03994) provides structural layerwise audit on ~50 examples but measures representation routing, not functional text contribution; TTS provides per-step marginal causal contribution but no probe-side measurement and no cumulative sufficiency assessment; Thought Anchors (2506.19143) provide within-CoT causal structure but no external probe reference.\n\n## Opportunity\n(1) **Temporal gap measurement.** Multiple groups have independently built the measurement components — probe trajectories (Chrabąszcz: 60+ features, 91-97% AUROC; David: per-token; Zhang: per-chunk; Yuan: 0.95 overall; Esakkiraja: >90% pre-generation) and behavioral causal curves (Ballon: truncation-reinjection; TTS: per-step ATE; NLDD: per-position degradation) — but no one has unified them into a dual-stream temporal gap. Chrabąszcz et al. are structurally blind to the faithful-correct vs. unfaithful-correct distinction; Ballon et al. lack hidden-state measurement. The gap between these traditions IS the framework's niche.\n\n(2) **Phenomenon unification with honest scoping.** CoT faithfulness failures are studied in isolation: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al.; Esakkiraja et al.), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103). We propose 2-3 are distinguishable via G*(t) trajectory shapes, honestly pre-registering that pre-CoT encoding and rationalization may collapse to a single \"pre-committed\" category.\n\n(3) **Task-difficulty conditioning.** ICLR 2026 Workshop finding, Li et al. (2510.22362): easy→decorative, hard→faithful. Gjølbye et al. (2605.15454): difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). ICG answers: at what difficulty does CoT transition from decorative to load-bearing?\n\n(4) **Probe target clarification.** First principled treatment contrasting correctness awareness gap vs. answer-content gap on applicable tasks.\n\nTwo prior works combine probing with causal intervention: Kudo et al. (EACL 2026, 2412.01113) on synthetic arithmetic, and CMI (2602.03994) on ~50 examples — CMI measures *structural mediation* (representation routing through layers) while ICG measures *functional contribution* (whether CoT text causally contributes to behavioral correctness). Wang (2604.15726) formalizes H1/H2/H0 hypotheses; ICG operationalizes the H1/H2 distinction empirically. Neither Kudo et al. nor CMI provides: (a) temporal coverage on natural benchmarks, (b) phenomenon mapping, (c) instance-level diagnostic, (d) multi-model comparison across model families, (e) robustness validation per Young's (2603.20172) classifier-sensitivity finding (kappa as low as 0.06), or (f) empirical pilot with external validation standards.\n\n## Landscape\n**Probe-based temporal measurement (P*(t) foundation).** Chrabąszcz et al. (2605.18549): probe trajectories with 60+ signal-processing features (volatility, trend, steady-state, boundary transients, autocorrelation) via 3-layer MLP + Multi-Instance Learning. Max-pooling: 91-97% AUROC harmfulness (vs. 33-61% average-pooling); up to 17pp over static on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours). Critical: (a) NO causal component, (b) NO gap metric, (c) NO calibration, (d) NO faithfulness-mode taxonomy, (e) NO difficulty conditioning, (f) structurally cannot distinguish faithful-correct from unfaithful-correct. David (2511.14773): 0.84 AUC at t=4, stable ~0.8, easy/hard 0.84/0.76 on Qwen3-8B. Zhang et al. (2504.05419): 0.82-0.91 AUROC on GSM8K/MATH/AIME, 65%→79% trajectory, 24% token reduction via early-exit. Yuan et al. (2605.09502): 0.95 AUROC on Qwen-3B, 0.852 on R1-7B, 0.787 first-step, concealment gap 0.197 AUROC. Esakkiraja et al. (2604.01202): >90% pre-generation, dip at 5-10%, recovery to near-100%. Cox et al. (2603.01437): answer-content probes >0.9 AUC on instruction-tuned Gemma-2/Qwen-2.5, negligible flip on reasoning GPT-OSS-20B. Additional: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop).\n\n**Diagnostic-not-causal evidence.** Yuan et al. (2605.09502): four interventions all fail on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. 'The error signal is a diagnostic readout, not a causal component that can be edited.' Cox et al. independently confirm. Probe accuracy ≠ causal potency on reasoning models.\n\n**Behavioral C(t) measurement.** Ballon et al. (2601.23163): truncation-reinjection on Qwen3-4B/8B/14B and gpt-oss-20B/120B, decile intervals. Accuracy: 30.8-42.3% → 49.0-73.1% on GPQA-Diamond. Controls validate sequential content (intact +18.1-33.1% vs. shuffled +0.3-10.8%). Disclaims faithfulness analysis. Zhao et al. (2510.24941, TTS): per-step ATE on R1-Distill-Qwen-7B/14B/Llama-8B, only 2.3% AIME steps TTS≥0.7. Ye et al. (2602.11201, NLDD): Reasoning Horizon at 70-85% on synthetic tasks (natural benchmark generalizability unvalidated). Thought Anchors (2506.19143): per-sentence counterfactual importance via 100-rollout replacement sampling; identifies \"anchor\" sentences steering reasoning trajectory — provides within-CoT causal structure but no probe reference for assessing redundancy relative to internal state. Basu & Chakraborty (2603.22816): decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026).\n\n**Probe-intervention combinations.** Kudo et al. (2412.01113, EACL 2026): per-position probes + activation patching on synthetic arithmetic, 9 models. CMI (2602.03994): layerwise activation patching on Phi/Qwen/DialoGPT, ~50 examples. CMI measures *structural mediation* (representation routing); ICG measures *functional contribution* (behavioral text causation). Both complementary precursors on small/synthetic samples.\n\n**Latent-reasoning theory.** Wang (2604.15726): H1/H2/H0 hypotheses with compute-audited designs. ICG operationalizes H1/H2 distinction.\n\n**Temporal hidden-state dynamics.** Gjølbye et al. (2605.15454): 11 models, 3 domains, length correction. ρ⊥^D = +0.41 Codeforces vs. −0.06 baselines; weaker on MATH (+0.05). Prompt-stage probes don't mirror generation-time dynamics. Furuya & Tanimura (2605.01853, StALT). Herrmann et al. (2605.09159): internal polylogue dynamics. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop, Concept Walk): easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026): 14-70% token savings.\n\n**Probe calibration.** Hewitt & Liang (EMNLP 2019): 4.5 selectivity. Ravichander et al. (2005.00719): properties recoverable when unused. Voita & Titov (EMNLP 2020, 2003.12298): MDL probing. Chun et al. (2602.20338, MCT): geometric pulse — separability peaks transiently while probe accuracy persists. Validates null-probe calibration need.\n\n**Trajectory-shape analysis.** Entropy trajectories (2603.18940): +5.8pp from monotonicity. RQA (2602.06266): temporal 36.94% vs. aggregates 28.97%. Microsoft (2604.05655): 0.852 vs. 0.649 AUC.\n\n**Measurement sensitivity.** Young (2603.20172): kappa as low as 0.06, up to 30.6pp divergence. Young (2603.26410). 'Lie to Me' (2603.22582).\n\n**Additional.** Internal States Before Wait (2510.04128). From Reasoning to Answer (2509.23676). FaithCoT-Bench (ICLR 2026, 2510.04040): 1000+ expert-annotated trajectories, 11 methods, 4 paradigms. Jin et al. survey (ARR for ACL 2026). Liu et al. (2602.13904). Reasoning Theater (2603.05488). Early-exit: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., 2509.13334). Breaking the Chain (Somov et al., 2603.16475). Step-Level Hallucination (Alvarez & Baheri, 2605.13772). SAE Reasoning Features (2503.18878). Solution Hides in Hidden States (2604.23351). Knowing Before Saying (ACL Findings 2025, 2505.24362). LEACE (Belrose et al., NeurIPS 2023, 2306.03819). CoT Monitorability (Anwar et al., 2602.18297). Understanding CoT via Information Theory (Ton et al., ICML 2025, 2411.11984).\n\n**What remains open.** No framework provides: (1) dual-stream temporal gap enabling faithful-vs-unfaithful discrimination for correct instances; (2) empirically-validated phenomenon taxonomy with external validation; (3) instance-level diagnostic from temporal gap; (4) difficulty-conditioned gap with domain nuance; (5) head-to-head comparison against existing causal faithfulness methods; (6) instruction-tuned vs. reasoning model control comparison within the same framework.\n\n## Approach\n**Formal Framework.** Two time-varying quantities at equally-spaced positions (primary: 20-50 percentile-based positions; token-level supplementary on subsets):\n\n(i) *P*(t)*: Cross-validated AUROC of linear probe on layer-l hidden states, calibrated via null-probe (P*(t) = P(t) − P_null(t), Hewitt & Liang 2019). Shared probe evaluated at each position (following Chrabąszcz's per-token evaluation, avoiding per-position training). **Target: correctness (right/wrong)** — broader applicability than answer-content probes, directly tied to the diagnostic-not-causal finding (Yuan et al.), more interpretable for faithfulness. Supplementary answer-content probes on binary/MC subsets. Probed at layers L/4, L/2, 3L/4, L. MCT (Chun et al. 2602.20338) supplementary concordance on 500 examples: if MCT capacity diverges from P*(t), identifies positions where probe signal may reflect retrievability rather than geometrically organized information.\n\n(ii) *C(t)*: Three estimators aggregated into C_agg(t): (a) **Prefix truncation** — Ballon et al.'s (2601.23163) protocol with three controls (random, swapped, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT). This measures *cumulative sufficiency* — whether CoT up to position t is sufficient for correctness — which is theoretically distinct from per-step *marginal contribution* (TTS); (b) **Paraphrase perturbation** — sentence-level segments paraphrased by external model (Claude Haiku or GPT-4o-mini for cost efficiency), 2-3 variants per segment, NLI-based semantic preservation verification. Answer stability: P(same answer | paraphrased CoT). Protocol follows FaithCoT-Bench (ICLR 2026) paraphrasing paradigm. Applied to stratified subset (~40% of examples per cell) for cost control, with full prefix truncation on all examples; (c) **NLDD** (Ye et al. 2602.11201, conditional on Phase 0a feasibility) — logit degradation under corruption. Sentence-level segmentation aligned with TTS approach (Zhao et al.). Multiple estimators provide robustness per Young's (2603.20172) classifier-sensitivity finding.\n\n**C(t) Aggregation and Gap Normalization.** Primary: rank-based normalization — each estimator converted to instance-level percentile ranks within model-benchmark cell, then combined. If NLDD underperforms on specific benchmarks (Phase 0a), two-estimator C_agg(t) (prefix + paraphrase) is primary for those benchmarks; three-estimator as supplementary. Ablation reports: (a) per-estimator G*(t) for phenomenon classification; (b) inverse-variance weighting vs. equal-weight; (c) pairwise Spearman correlation and Cohen's kappa between estimators. Diagnostic value lies in trajectory shapes, not magnitudes, so normalization affects scale but not shape-based signatures.\n\n**G*(t) = P*(t) − C(t).** Primary signal:\n- G*(t) ≈ 0: Aligned (necessary for faithfulness; H2-consistent per Wang 2604.15726)\n- G*(t) >> 0: Diagnostic excess — 'knows but doesn't use' (H1-consistent)\n- G*(t) < 0: Information assembled during reasoning\n\n**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information not causally channeled through CoT, but does not entail intentional withholding — some signals may be computational byproducts rather than actionable knowledge. MCT concordance provides partial validation of this boundary.\n\n**Phenomenon Predictions (honestly scoped).**\n*Primary (HIGH confidence):*\n(i) *Pre-committed reasoning* (encompasses pre-CoT encoding and potentially post-hoc rationalization): G*(t) starts high, stays high or widens. P*(t) high from start (David: 0.84 at t=4; Esakkiraja: >90% pre-generation; Cox: >0.9 pre-CoT), C(t) low or flat.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. P*(t) rises gradually, C(t) tracks P*(t). Zhang et al.'s 65%→79%, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase.\n\n*Secondary (MODERATE confidence — Phase 0b tests whether separable from pre-committed):*\n(iii) *Post-hoc rationalization as distinct from pre-CoT encoding*: If distinguishable, the separation should manifest primarily in C(t) dynamics (rationalization may show spurious partial C(t) increases as the model crafts locally-consistent reasoning, while pre-CoT encoding shows flat-zero C(t)) rather than P*(t). Phase 0b explicitly tests 2-category vs. 3-category separability; 2-category (pre-committed vs. genuine) is pre-registered as an acceptable outcome.\n\n*Stretch (require additional features):*\n(iv) *Steganographic encoding*: Dip-and-recovery, consistent with Esakkiraja's 5-10% dip.\n(v) *Reasoning Theater*: May overlap with pre-committed. Chrabąszcz-style features may enable separation. Reported with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from published data (David, Zhang, Esakkiraja, Yuan for probes; NLDD, TTS for causal; Chun et al. MCT for inflation). Real validation in Phase 0b.\n\n**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct P*(t) and C(t) curves at 20-50 position resolution\n(ii) Validate null-probe calibration\n(iii) Characterize causal potency (Cox et al. protocol: steering on reasoning vs. instruction-tuned)\n(iv) **NLDD feasibility**: 7B × 100 examples on GSM8K (clear steps) + MMLU (ambiguous steps). If SNR uninformative on MMLU, restrict NLDD to math/code or replace with TTS-style perturbation. Cost: <10 GPU-hrs; gates 250+ hrs NLDD investment.\n\n**Phase 0b: Empirical Pilot (Weeks 2.5-4).** R1-Distill-Qwen-7B × GSM8K + MATH-500, 1000 examples.\n\n*Primary validation (external standards):*\n(i) **Difficulty-only partition**: model-independent difficulty bins (easy/medium/hard), no P*/C features used. Test G*(t) shape differences: d > 0.5 AND p < 0.01 (Bonferroni-corrected) on 2+ trajectory features.\n(ii) **TTS cross-reference** (primary external validation): compute Zhao et al.'s TTS on same examples; test whether high-TTS (genuine reasoning) vs. low-TTS (decorative) produce distinguishable G*(t) shapes.\n(iii) **2-category vs. 3-category test**: explicitly test whether pre-CoT encoding and post-hoc rationalization are separable or collapse to single \"pre-committed\" category.\n(iv) **FaithCoT-Bench** (supplementary): if instance-level overlap available, test correlation with expert labels; otherwise dataset-level validation.\n\n*Supplementary*: P*/C-based partition as self-consistency check.\nLength correction per Gjølbye et al. (2605.15454). Success: d > 0.5 between 2+ externally-defined partitions. If d < 0.3, downscope to characterization paper.\n\n**Phase 1: Full ICG (Weeks 4-9).** Conditional on Phase 0b d > 0.5. **5 models**: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, QwQ-32B (reasoning models spanning 2 architecture families) + Qwen2.5-7B-Instruct (instruction-tuned control — expected G*(t) ≈ 0 as sanity check). **4 benchmarks**: GSM8K (500 examples), MATH-500 (500), GPQA-Diamond (~198 full), AIME (~90 full). Per-cell: ~1288 examples × 5 models. Full calibrated P*(t) + MCT supplementary + three C(t) estimators (NLDD conditional, paraphrase on ~40% stratified subset) + Ballon-style controls. Cross-reference with TTS at step boundaries. Bootstrap 95% CI on G*(t). ~250 H100-hours.\n\n**Phase 2: Difficulty Conditioning (Weeks 7-11).** Difficulty quintiles per benchmark. G*(t) per quintile. Expected: easy → persistent gap, hard → converging gap. Length correction; domain-specific reporting (stronger on math/code per Gjølbye et al.'s ρ⊥ = +0.41 code vs. +0.05 math).\n\n**Phase 3: Classification, Baselines, Robustness (Weeks 9-14).**\n\n*Classification framework:* G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → RF → MLP; report all. Metric: macro-F1 (primary) + confusion matrix + reliability diagram. Validation: 5-fold + cross-model (train A → test B, reporting within-family vs. cross-family separately) + cross-benchmark generalization. Paired permutation tests with Bonferroni correction for all head-to-head comparisons.\n\n*Baselines:* (a) Random + majority-class; (b) Difficulty-only classifier; (c) **Probe-trajectory-only** (Chrabąszcz-style P*(t) features, no C(t)) — \"no causal dimension\" ablation; (d) **TTS-only** — per-step marginal causal contribution without probe dimension.\n\n*Head-to-head TIF validation:* TIF score vs. FaithCoT-Bench detection methods (Adding Mistakes, Removing Steps, Early Answering, Paraphrasing) and TTS on overlapping examples, comparing instance-level correlation with ground truth.\n\n*Robustness ablations (7 dimensions):* (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection; (c) C(t) estimator agreement + per-estimator performance + weighting schemes; (d) gap normalization (rank vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content); (g) **temporal resolution** (5/10/20/35/50 positions + token-level — reporting resolution vs. macro-F1 curve and saturation point).\n\n**TIF Score.** Normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.\n\n**Paper Focus.** Core contributions: (1) ICG diagnostic — first framework distinguishing faithful-correct from unfaithful-correct reasoning via dual-stream temporal gap, with instruction-tuned control validating the framework; (2) Phase 0b pilot with external validation demonstrating 2-3 distinguishable G*(t) signatures (or honestly reporting 2-category outcome); (3) difficulty-conditioned gap revealing decorative→load-bearing transition; (4) head-to-head showing ICG's value over probe-only, TTS-only, and FaithCoT-Bench methods. Supporting: 7-dimension ablations; TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness comparison; semi-synthetic simulation; CMI structural-functional prediction if resources allow.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B, DeepSeek-R1-Distill-Llama-8B, QwQ-32B, Qwen2.5-7B-Instruct across GSM8K, MATH-500, GPQA-Diamond, AIME. 671B validation (500-example subset). Calibration: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary. Gjølbye-style length correction throughout.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~1050 H100-hours (Phase 0a: 90 hrs [3 models × 3 datasets + NLDD feasibility]; Phase 0b: 30 hrs [pilot]; Phase 1: 250 hrs [5 models × 4 benchmarks, probes + 3 C(t) estimators + controls]; Phase 2: 50 hrs [difficulty conditioning]; Phase 3: 70 hrs [classification + 7-dim ablations + baselines]; NLDD 32B conditional: 250 hrs [primary bottleneck]; NLDD 7B/14B: 100 hrs; MCT supplementary: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic: 30 hrs; paraphrase model: ~80 hrs inference on target models for stability checks)', 'paraphrase_api_cost': '~$800-1500 (Claude Haiku/GPT-4o-mini on stratified ~40% subset, 2-3 variants)', 'timeline': '15-17 weeks (2 researchers)', 'estimated_gpu_cost': '$3,200 at ~$3/H100-hour', 'storage': '3-5 TB (4 layers, fp16); ~1.5 TB with PCA/on-the-fly'}, 'human_in_loop': {'gpu_hours': '~1050 H100-hours', 'timeline': '14 weeks (1 researcher + Claude)', 'claude_api_cost': '$500 (experiment design) + $800-1500 (paraphrase generation)', 'estimated_gpu_cost': '$3,200'}, 'auto_research': {'gpu_hours': '~1050 H100-hours', 'timeline': '12 weeks', 'claude_api_cost': '$900 + $800-1500 (paraphrase)', 'estimated_gpu_cost': '$3,200', 'speed_bottleneck': 'NLDD on 32B (~250 hrs, conditional on Phase 0a) is primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s steering failure on reasoning models despite high probe accuracy; (b) Yuan et al.'s four-intervention failure establishing 'diagnostic not causal'; (c) temporal probe dynamics (David, Zhang, Esakkiraja, Chrabąszcz: 60+ features, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection demonstrating monotonic behavioral C(t) with controls; (e) trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing shapes carry diagnostic information — all pointing to: the gap between diagnostic availability and causal contribution IS the phenomenon, and its temporal shape reveals the mechanism. Additionally: Wang's (2604.15726) H1/H2/H0; Gjølbye et al.'s (2605.15454) domain-specific coupling; Chun et al.'s (2602.20338) MCT geometric pulse; CMI's (2602.03994) structural mediation; Thought Anchors' (2506.19143) within-CoT causal structure.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; primary target)\n- ICML 2027 (full paper: Jan 29, 2027; fallback)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent (Wang, arXiv 2604.15726)\n- Reasoning Models Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Internal Polylogue (Herrmann et al., arXiv 2605.09159)\n- Faithfully Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- MCT / Emergent Manifold Separability (Chun et al., arXiv 2602.20338)\n- Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Entropy trajectory shapes (arXiv 2603.18940)\n- RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE (Belrose et al., NeurIPS 2023, arXiv 2306.03819)\n- Thought Anchors (arXiv 2506.19143)"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:42:27.852Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:42:27.852Z",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T04:42:27.864Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make a thorough assessment. Let me compile my evaluation.

```
【阶段】: Triage

【领域调研】:
- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)](https://arxiv.org/abs/2605.18549) (May 2026): 最直接的竞争者之一。在 reasoning model 上用 per-token probe 构建轨迹，60+ 信号处理特征，max-pooling 达 91-97% AUROC。关键限制：完全没有 causal 维度，无法区分 faithful-correct vs. unfaithful-correct。ICG 的 probe 端正是要站在这个工作的肩上。
- [Hidden Error Awareness (Yuan et al., arXiv 2605.09502)](https://arxiv.org/abs/2605.09502) (May 2026): 系统验证了 diagnostic-not-causal 现象——0.95 AUROC probe 准确率，但四种 intervention 全部失败。这是 ICG 框架立论的核心经验基础之一。非常新的工作，ICG 的 research question 直接建立在此发现之上。
- [Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)](https://arxiv.org/abs/2603.01437) (March 2026): 发现 instruction-tuned model 上 steering 可以翻转答案 (>50%)，但 reasoning model 上翻转率 negligible。与 Yuan et al. 互相印证了 diagnostic-causal gap 在 reasoning model 上的独特性。
- [Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)](https://arxiv.org/abs/2601.23163) (Jan 2026): 提出 truncation-reinjection 协议测量 behavioral C(t)，在 Qwen/GPT-OSS 上实验，accuracy 从 30-42% 升到 49-73%。关键限制：没有 hidden-state 测量，且明确 disclaims faithfulness 分析。ICG 的 C(t) 端直接继承此方法。
- [FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)](https://arxiv.org/abs/2510.04040): 1000+ expert-annotated 轨迹，11 种检测方法的统一 benchmark。这是 ICG 的主要外部验证标准之一，也是头对头比较的关键对手。
- [True Thinking Score / TTS (Zhao et al., arXiv 2510.24941)](https://arxiv.org/abs/2510.24941): per-step marginal causal contribution，AIME 上只有 2.3% 的步骤 TTS≥0.7。ICG 明确区分了 cumulative sufficiency (自己的 C(t)) vs. marginal contribution (TTS)。
- [LLM Reasoning Is Latent (Wang, arXiv 2604.15726)](https://arxiv.org/abs/2604.15726) (April 2026): 形式化 H1(latent-mediated)/H2(CoT-mediated)/H0 假设，结论倾向 H1。ICG 声称可以操作化 H1/H2 区分。
- [When Chains of Thought Don't Matter / CMI (Sathyanarayanan et al., arXiv 2602.03994)](https://arxiv.org/abs/2602.03994) (Feb 2026): layerwise activation patching 衡量 CoT 结构介导，~50 examples。ICG 区分了 structural mediation (CMI) vs. functional contribution (自己)。
- [Thought Anchors (arXiv 2506.19143)](https://arxiv.org/abs/2506.19143): sentence-level counterfactual importance via 100-rollout replacement sampling，识别对推理轨迹有重大影响的 "anchor" 句子。提供 within-CoT 因果结构，但无 probe 外部参照。

- **调研总结**: CoT faithfulness 是 2025-2026 年 NLP 可解释性最活跃的方向之一，probe 端和 causal 端各有大量独立工作，但确实没有人将二者在时间维度上统一。ICG 的 niche（dual-stream temporal gap）在文献中确实是空白的。但该领域竞争激烈、工作密集，多个同期竞争者可能在 proposal 完成前填补类似空白。

【整体印象】:
如果我是审稿人，第一反应是：这是一份学术功底极深、文献调研极其扎实的 proposal，研究问题真实且有价值。但第二反应是：(1) 框架核心操作——P*(t) 与 C(t) 的相减——在概念层面存在不可通约性问题；(2) 系统整体复杂度非常高，可能过度工程化；(3) faithfulness ground truth 的缺失使验证只能依赖间接代理。我会倾向 borderline，需要看实验结果才能决定 accept 或 reject。如果 Phase 0b 的效果量显著 (d > 0.5)，这会是一篇 solid 的贡献；如果效果量不够，整个框架的说服力会大打折扣。

【核心贡献】:
核心贡献是提出第一个能区分 "faithful-correct" vs. "unfaithful-correct" 推理的诊断框架：通过同时追踪模型内部的信息可用性 (probe) 和 CoT 文本的因果贡献 (behavioral intervention)，用二者的时间轨迹差异（G*(t) 形状）来分类不同的 faithfulness 现象。这个贡献对领域有中等偏高的价值——它试图将分散的 probe 和 causal 两大研究传统统一起来，如果成功，可以为 CoT faithfulness 提供一个更精细的诊断工具。但其价值很大程度上取决于 G*(t) 形状是否真的能稳健地区分不同现象。

【方法合理性】:
方法的整体设计方向是合理的——probe 端继承 Chrabąszcz/David/Yuan 的成熟方法，causal 端继承 Ballon 的 truncation-reinjection + 扰动方法，都有坚实的先验支撑。但存在三个核心问题：

(1) **不可通约性**：P*(t) 是 AUROC（分类判别能力），C(t) 是 accuracy change（行为差异）。这两个量纲根本不同，直接相减在数学上没有意义。Proposal 承认了这一点并用 rank normalization + "shapes over magnitudes" 来辩护，但 rank normalization 后的轨迹形状仍然受到两个流各自 noise profile 和 granularity 的影响。如果 P*(t) 在 20 个 position 上平滑缓变，而 C(t) 因为 truncation 点数量有限而呈阶梯状，那么 G*(t) 的形状主要反映 C(t) 的离散化伪影，而非真正的 faithfulness 信号。这是一个比 proposal 承认的更严重的问题。

(2) **更简单的替代方案**：一个显然的替代方案是不做减法，而是直接用 P*(t) 和 C(t) 各自的轨迹特征作为联合特征输入分类器。这避免了不可通约性问题，且可能获得类似甚至更好的分类性能。Proposal 确实在 ablation 中对比了 probe-only 和 TTS-only，但没有测试"联合特征但不做 gap"这个自然基线——审稿人几乎一定会问这个问题。

(3) **Ground truth 缺失**：Faithfulness 本身缺乏可靠的 ground truth。FaithCoT-Bench 的 expert annotations 是目前最好的，但覆盖有限且主观性不可忽视。Proposal 使用 difficulty partition 和 TTS 作为外部验证，但这些都是间接代理——difficulty 和 faithfulness 的关系是 assumed 而非 proven 的。

【5 维度打分】:
  1. 研究问题: 【强】— Diagnostic-causal gap 是一个真实的、被多个独立团队验证的现象 (Yuan et al. 2605.09502, Cox et al. 2603.01437)，将其从 "obstacle" 转为 "object of study" 是一个有洞察力的 reframing。问题的重要性和时效性都很高。CoT faithfulness 是当前 NLP 可解释性的核心问题，对 AI safety 有直接意义。

  2. 方法与创新: 【中】— Dual-stream 的概念框架是清晰的且填补了真实的文献空白（Chrabąszcz 无 causal，Ballon 无 probe，CMI 是 structural 而非 functional，Thought Anchors 无外部参照）。但创新主要在框架层面而非方法层面——个体组件 (linear probe, truncation-reinjection, paraphrase perturbation, NLDD) 全部是现有工具的组合。P*(t) 与 C(t) 的不可通约性是核心方法论弱点，shapes-over-magnitudes 的辩护虽有 trajectory 文献支撑 (arXiv 2603.18940, 2602.06266, 2604.05655)，但这些支撑来自不同上下文，对本场景的 transferability 未经验证。缺少"联合特征但不做 gap"这个自然消融基线。

  3. 实验设计: 【强】— 这是 proposal 最突出的优点之一。5 models × 4 benchmarks 的覆盖面充分；Phase 0a/0b 的 go/no-go 门控是成熟的研究实践；7 维消融非常全面；多个外部验证标准 (TTS cross-reference, difficulty partition, FaithCoT-Bench)；cross-model 泛化测试 (train A → test B)；统计严谨性 (bootstrap CI, Bonferroni correction, permutation tests)。与领域标准 (FaithCoT-Bench 的 4 种方法, TTS) 的 head-to-head 对比也是该有的。但缺少"P*(t)+C(t) 联合特征不做减法"作为 baseline。instruction-tuned control (Qwen2.5-7B-Instruct) 作为 sanity check 也是好设计。

  4. 可行性: 【中】— ~1050 H100-hours 在学术实验室可承受范围内；15-17 周时间线合理但紧张。主要风险：(a) NLDD 在自然 benchmark 上的可行性未验证（Phase 0a 测试，但如果失败需要调整方案）；(b) paraphrase perturbation 的语义保持验证 (NLI-based) 可能引入 noise；(c) 32B 模型上的 NLDD 是计算瓶颈 (250 hrs)；(d) 整个框架依赖 Phase 0b 的 d > 0.5 结果，如果不成立需要大幅降级。Phase 0b 的 go/no-go 设计是明智的，但也意味着有非零概率整个项目需要 pivot。

  5. 写作与呈现: 【中】— Proposal 的逻辑结构清晰，文献定位极其精确（每个竞争者的优势和不足都有细致对比），预判并回应审稿人 objection 的做法非常专业。但过于密集——实际论文需要大幅精简，否则审稿人会因信息过载而降低好感。某些地方有 over-claim 风险（如 "the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning"——这在 P*(t)-C(t) 不可通约性未完全解决前是 aggressive 的 claim）。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
**向上因素**：(1) 研究问题真实、重要、时效性强；(2) 文献空白是真实存在的——确实没有 dual-stream temporal 框架；(3) 实验设计非常完备，go/no-go 门控、7 维消融、多重外部验证；(4) honest scoping（2 vs 3 category）是加分项；(5) 与 Thought Anchors、CMI、TTS、Chrabąszcz 的差异化论证清晰有力。

**向下因素**：(1) P*(t) 与 C(t) 的不可通约性是核心方法论弱点，rank normalization + shapes 的辩护可能不足以说服严格审稿人；(2) 创新主要在"框架组合"而非"方法突破"——所有组件都是现有工具，审稿人可能判定为 engineering contribution；(3) ground truth 缺失，验证只能依赖间接代理，分类的 "正确性" 无法严格确认；(4) 该领域竞争极度激烈（2025-2026 已有 30+ 篇相关工作），提交时可能已有类似思路的工作出现；(5) 缺少"联合特征不做 gap"这个自然基线，审稿人大概率会指出。

中位 35% 反映了这是一篇方向正确、设计扎实但存在核心方法论争议的 proposal。如果 Phase 0b 效果量优异且能补上"不做 gap"的消融，概率可上探 40%+。如果 G*(t) 形状的区分能力不够 robust，或审稿人对不可通约性严厉批评，概率会降到 28% 以下。

【主要风险】:
1. **P*(t)-C(t) 不可通约性遭到 fundamental objection**：审稿人认为 AUROC 与 accuracy change 的相减在概念上不成立，rank normalization 不足以解决问题，且"shapes over magnitudes"的辩护缺乏在本具体场景的直接验证。这可能被视为方法论的 fatal flaw。
2. **"组合而非创新" 的评判**：审稿人认为框架只是将 Chrabąszcz 的 probe + Ballon 的 truncation 简单拼接，没有引入根本性的新洞察或新方法，核心贡献不足以达到 venue 标准。尤其是如果"联合特征不做 gap"的 baseline 表现与 G*(t) 相当或更好，会严重削弱框架的存在价值。

【实施评估】:
  - 计算资源: ~1050 H100-hours，约 $3,200（按 $3/hr），学术可承受。32B NLDD 是瓶颈 (250 hrs)。
  - 数据需求: 公开 benchmark (GSM8K, MATH-500, GPQA-Diamond, AIME)，无需新数据收集。FaithCoT-Bench (ICLR 2026) 作为外部验证标准需确认 instance-level 数据可获取性。
  - 人工介入: 无需人工标注（依赖已有 benchmark 和自动化方法）。Paraphrase 生成由 API 完成。
  - 训练需求: 无大规模模型训练。需训练 linear probes（轻量）和小型分类器 (logistic regression/RF/MLP)。所有目标模型使用现有权重。
  - 新 Benchmark: 不构建新 benchmark。TIF Score 是新指标但不是 benchmark。
  - 预估周期: 15-17 周 (2 researchers) 或 12-14 周 (1 researcher + Claude)。Phase 0b 在第 4 周提供 go/no-go 信号。
```

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness (Yuan et al.)](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before CoT (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [True Thinking Score / TTS (Zhao et al.)](https://arxiv.org/abs/2510.24941)
- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)
- [When Chains of Thought Don't Matter / CMI (Sathyanarayanan et al.)](https://arxiv.org/abs/2602.03994)
- [Thought Anchors](https://arxiv.org/abs/2506.19143)
- [Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al.)](https://arxiv.org/abs/2602.11201)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient context to provide a thorough assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Chrabąszcz et al., arXiv 2605.18549](https://arxiv.org/abs/2605.18549) (May 2026): 最直接的竞争工作。60+ signal-processing features on probe trajectories, 91-97% AUROC。但完全没有 causal component——这正是本 proposal 声称要填补的空白。该工作发表仅 2 天前（5月18日），说明该领域极度活跃。
- [Yuan et al., arXiv 2605.09502](https://arxiv.org/abs/2605.09502) (May 2026): 核心 empirical foundation。证明 probe 可诊断但 4 种 causal intervention 全部失败，"diagnostic not causal"。本 proposal 将该发现从 obstacle 重新定义为 phenomenon，立意精准。
- [Cox et al., arXiv 2603.01437](https://arxiv.org/abs/2603.01437) (March 2026): Pre-CoT probes predict answer with >0.9 AUC; steering works on instruction-tuned but fails on reasoning models。独立验证了 diagnostic-causal gap。
- [Ballon et al., arXiv 2601.23163](https://arxiv.org/abs/2601.23163) (Jan 2026): Truncation-reinjection protocol providing behavioral C(t) curves。本 proposal 直接采用其方法作为 C(t) estimator 之一。
- [FaithCoT-Bench, ICLR 2026](https://arxiv.org/abs/2510.04040): 1000+ expert-annotated trajectories, 11 detection methods。已被接收为 ICLR 2026 conference paper。本 proposal 将其作为 external validation 和 comparison baseline。
- [Wang, arXiv 2604.15726](https://arxiv.org/abs/2604.15726) (April 2026): 形式化 H1 (latent-mediated) vs H2 (CoT-mediated) 假设。本 proposal 声称 ICG 可 operationalize 该区分。
- [CMI / Sathyanarayanan et al., arXiv 2602.03994](https://arxiv.org/abs/2602.03994) (Feb 2026): Causal bypass via hidden-state patching, ~50 examples, structural mediation。本 proposal 正确区分了 structural vs functional faithfulness。
- [Thought Anchors, arXiv 2506.19143](https://arxiv.org/abs/2506.19143) (June 2025): Per-sentence counterfactual importance via 100-rollout replacement。Within-CoT causal analysis 但无 probe reference。
- [Kudo et al., EACL 2026](https://arxiv.org/abs/2412.01113): 最接近的先驱——per-position probes + activation patching，但限于 synthetic arithmetic。
- [TTS / Zhao et al., arXiv 2510.24941](https://arxiv.org/abs/2510.24941): Per-step marginal ATE, only 2.3% AIME steps TTS≥0.7。提供 marginal causal contribution 但无 probe 维度。

- 调研总结: CoT faithfulness 是 2025-2026 年 interpretability/alignment 领域最活跃的方向之一，已有大量 probe-only 和 causal-only 的工作，但确实没有已发表工作将 probe trajectories 与 causal contribution 统一到一个 temporal gap framework 中。该 proposal 的 niche（dual-stream temporal gap）在文献中确实是空白。但该领域极度拥挤且快速移动，window of opportunity 非常窄。

【整体印象】:
作为审稿人，我的第一反应是：这是一个 **极其 well-researched、positioning 精准的分析型 proposal**，对领域理解极深，literature coverage 几乎无遗漏。核心直觉——"将 diagnostic-causal gap 本身作为研究对象，而非视其为障碍"——是一个真正有洞察力的 reframing。

但我同时有几个严重担忧：
1. **Framework 复杂度过高**：ICG 涉及 P*(t)（多层 probe + null calibration + MCT concordance）和 C(t)（3种 estimator + aggregation + normalization），加上 7 个 ablation 维度、5 个模型、4 个 benchmark。这对一篇 8 页论文来说信息密度过大，有沦为"measurement study"的风险。
2. **核心 contribution 的 novelty 边界模糊**：ICG 本质上是"用已有方法 A 的输出减去已有方法 B 的输出"。P*(t) 来自 Chrabąszcz/David/Zhang 等的 probe 方法，C(t) 来自 Ballon/TTS/NLDD。创新点在于 combination + temporal gap analysis，但 reviewer 可能质疑这是否是"trivial combination"。Proposal 自己预见了这个 objection 并给出了 cumulative vs marginal 的论证，但说服力取决于 empirical results。
3. **Shape-based classification 的可靠性**：将 faithfulness phenomena 分类寄托于 G*(t) trajectory shapes（constant-high vs convergence vs widening），但 Phase 0b 的 success criterion 是 d > 0.5 between partitions。如果 d < 0.5，proposal 预注册降级为 characterization paper——这说明作者自己也不确定核心 claim 是否成立。

倾向：**borderline accept**。如果实验结果强，有 accept 的可能；如果 Phase 0b 的 effect sizes 不够强或分类只有 2 categories，可能掉到 weak reject。

【核心贡献】:
1. 首次提出 dual-stream temporal gap framework (ICG)，将 probe-based information availability 和 causal contribution 统一到时间轴上，能够区分 faithful-correct 和 unfaithful-correct reasoning。
2. G*(t) trajectory shape 作为 phenomenon fingerprint 的概念，可以 operationalize Wang 的 H1/H2 区分。
3. Difficulty-conditioned gap analysis，回答"在什么难度下 CoT 从 decorative 过渡到 load-bearing"。
4. 对 reasoning utilization efficiency 的实用意义（early-exit、benchmark validity、safety monitoring）。

价值评估：如果 empirical results 强（d > 0.5，3 categories separable），这是一个高价值的 diagnostic tool，对 interpretability 和 alignment 社区有实质性贡献。如果 results 弱，价值降为"又一个 measurement framework"。

【方法合理性】:
方法在逻辑上是合理的——分别测量 information availability 和 causal contribution 然后计算 gap——但有几个 concerns：

1. **P*(t) 和 C(t) 的可比性**：Proposal 承认两者"measured via fundamentally different methods with non-commensurable scales"，并采用 rank-based normalization。但 rank normalization 会丢失 magnitude 信息，而 proposal 又声称 shapes 才是关键。这个 tension 是否真的被 resolved 值得审视。
2. **C(t) 的 aggregation**：三种 estimator（prefix truncation, paraphrase, NLDD）测量的是不同的东西——cumulative sufficiency、content independence、positional degradation。将它们 aggregate 的理论依据不够强。Young (2603.20172) 已证明不同 faithfulness metrics 之间 kappa 可低至 0.06，说明 aggregation 可能掩盖而非增强信号。
3. **更简单的替代方案**：直接用 Chrabąszcz 的 probe trajectory features + Ballon 的 truncation accuracy，不做 gap 计算，而是做 multi-feature classification，可能达到类似甚至更好的效果。Proposal 需要证明 gap formulation 提供了超越 simple feature concatenation 的 insight。

【5 维度打分】:

1. 研究问题: [强] — "模型知道答案但 CoT 并未使用这个知识"是 2025-2026 年被多组独立验证的核心现象（Yuan et al., Cox et al., Esakkiraja et al.）。将 diagnostic-causal gap 本身作为研究对象而非障碍是一个有价值的 reframing。FaithCoT-Bench (ICLR 2026) 已确认 15-20% correct answers 配对 unfaithful CoTs，验证了问题的实际存在。这个问题对 AI safety（monitoring hidden reasoning）和 efficiency（early-exit compute）都有直接影响。

2. 方法与创新: [中] — ICG 的 novelty 在于 combination 和 temporal gap formulation，而非底层方法（probe 来自多组前人工作，C(t) 来自 Ballon/TTS/NLDD）。与 Chrabąszcz et al. (2605.18549) 相比，ICG 增加了 causal 维度；与 CMI (2602.03994) 相比，ICG 是 functional 而非 structural。区分是清晰的，但 reviewer 可能质疑 gap = P*(t) - C(t) 是否比 feature concatenation 更有信息量。Proposal 对 cumulative vs marginal 的论证（对标 TTS vs Ballon）是一个合理的 preemption，但最终需要 empirical 支撑。Kudo et al. (EACL 2026) 已在 synthetic data 上做了 probe + causal combination，ICG 的增量在于 natural benchmarks + temporal gap formulation。

3. 实验设计: [强] — 这是 proposal 最出色的部分。Phase 0a/0b 的 go/no-go 设计非常成熟；external validation 通过 difficulty partition 和 TTS cross-reference（而非仅依赖 P*/C 自身的 partition）是方法论上的亮点；7 维 ablation 覆盖了几乎所有合理的 robustness concern；head-to-head 比较 probe-only、TTS-only、FaithCoT-Bench 方法提供了清晰的 contribution 量化。5 models × 4 benchmarks（含 instruction-tuned control 作 sanity check）的规模对分析型工作来说充分。与 Young (2603.20172) 的 measurement sensitivity 发现直接对话（报告 inter-estimator kappa）也是加分项。唯一的 concern 是规模可能导致论文过于 dense。

4. 可行性: [中] — ~1050 H100-hours 和 15-17 周在学术组可行但不轻松。主要风险在于：(a) NLDD 在 32B 上的 250 hrs bottleneck 且 Phase 0a 可能判其不可行；(b) paraphrase perturbation 的 API cost（$800-1500）和质量控制；(c) 3-5 TB hidden state 存储需要 engineering。好的方面是 Phase 0a 的早期 go/no-go 设计降低了 sunk cost 风险。如果 NLDD 在 Phase 0a 被 gated out，C(t) 只剩两个 estimator，可能削弱 robustness claim。

5. 写作与呈现: [中] — Proposal 的 literature positioning 极其精准，每个 related work 的区分都有清晰论证。但写作上存在几个问题：(a) 信息过载——一篇 8 页论文要呈现 dual-stream framework + 3 C(t) estimators + 7 ablation + 5 models × 4 benchmarks + difficulty conditioning + TIF score + classification + head-to-head + 671B subset + MCT supplementary + semi-synthetic simulation，几乎不可能在有限篇幅内清晰呈现；(b) framing 偏向 measurement framework，缺少 actionable insight 的前置承诺（beyond "we can classify phenomena"，so what？）；(c) phenomenon taxonomy 的 honest scoping（2 vs 3 categories）虽然诚实但也传递了不确定性。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
上界理由 (42%): 如果 Phase 0b 验证成功（d > 0.5, 3 categories separable），shape-based classification 显著优于 probe-only 和 TTS-only baselines，且论文成功聚焦核心 contribution 而非 exhaustive ablation，这将是一篇 solid 的 analysis paper。研究问题的 timeliness（2025-2026 最热话题之一）和实验设计的 rigor 是明确加分项。EMNLP 历来接收高质量的 analysis/interpretability 工作。

下界理由 (28%): (1) 最大风险是 novelty 争议——"已有方法 A 的输出减已有方法 B 的输出"可能被 reviewer 视为 incremental combination 而非 fundamental contribution；(2) 如果 Phase 0b effect sizes 不强或 phenomenon taxonomy 坍缩为 2 categories，核心 claim 被削弱；(3) 论文信息密度过高可能导致关键 insight 被淹没；(4) 该领域极度拥挤且快速移动（Chrabąszcz 5月18日才出，Thought Anchors 6月出），在 submission 前可能出现更直接的竞争工作。

中位 35%: 方向正确、实验设计 solid、但 novelty 有争议性且 execution risk 不低。属于"如果结果强则有希望，但需要 empirical results 来证明 gap formulation 的 added value"的 proposal。

【主要风险】:
1. **Novelty 被质疑为 trivial combination**: 审稿人可能认为 ICG = probe trajectory (existing) + causal measurement (existing) 的简单拼接，gap subtraction 不构成足够的方法论创新。Proposal 预见了这一点并给出了 cumulative vs marginal 论证，但如果 ablation 显示 feature concatenation（不做 gap）效果类似或更好，核心 claim 就不成立。
2. **Phenomenon classification 结果弱**: 如果 G*(t) trajectory shapes 在不同 faithfulness phenomena 之间没有足够大的 effect size（d < 0.5），或 3-category 分类坍缩为 2-category，论文从"diagnostic framework"降级为"characterization study"，显著降低 impact。在这个竞争激烈的领域，一篇"我们看了这个 gap 但它没有特别能区分什么"的论文很难被接收。

【实施评估】:
  - 计算资源: ~1050 H100-hours (~$3,200)，中等规模，学术组可负担但需要稳定 GPU 集群。NLDD 32B (250 hrs) 是单项最大开销，Phase 0a 可 gate。
  - 数据需求: 使用现有公开 benchmark（GSM8K, MATH-500, GPQA-Diamond, AIME），无需构建新数据集。FaithCoT-Bench 的 instance-level labels 如可获取将显著增强 validation。
  - 人工介入: 低。Probe training、C(t) estimation、classification 均可自动化。Paraphrase 需要 NLI-based 质量验证。主要人工投入在实验设计和论文写作。
  - 训练需求: 轻量级——仅训练 linear probes 和浅层 classifiers（LR/RF/MLP），不涉及 LLM fine-tuning。
  - 新 Benchmark: 不需要。TIF score 作为 derived metric 但不构成独立 benchmark。
  - 预估周期: 15-17 周（2 researchers）/ 14 周（1 researcher + Claude）。Phase 0b 在第 4 周提供 early go/no-go。整体 timeline 紧凑但可行。
```

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness (Yuan et al.)](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before CoT (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)
- [When Chains of Thought Don't Matter: Causal Bypass / CMI](https://arxiv.org/abs/2602.03994)
- [Thought Anchors](https://arxiv.org/abs/2506.19143)
- [Breaking the Chain (Somov et al.)](https://arxiv.org/abs/2603.16475)
- [Measuring Faithfulness Depends on How You Measure (Young)](https://arxiv.org/abs/2603.20172)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient context from the literature to provide a thorough evaluation. Let me compile my assessment.

```
【阶段】: Triage

【领域调研】:
- [Chrabąszcz et al., arXiv 2605.18549] (May 2026): Probe trajectories with 60+ signal-processing features (volatility, trend, autocorrelation) achieving 91-97% AUROC on harmfulness detection. Most directly competitive work for the P*(t) dimension — BUT entirely lacks a causal component, cannot distinguish faithful-correct from unfaithful-correct reasoning. ICG's closest "upstream" building block.
- [Yuan et al., arXiv 2605.09502] (May 2026): Establishes the "diagnostic not causal" finding — probes achieve 0.95 AUROC on correctness, but all four intervention strategies (steering, best-of-N, self-correction, patching) fail on reasoning models. This paper IS the empirical foundation that motivates ICG.
- [Cox et al., arXiv 2603.01437] (Mar 2026): Pre-CoT probes predict answers at >0.9 AUC; activation steering flips answers on instruction-tuned models but produces "negligible flip rates" on reasoning models. Independently confirms Yuan et al.'s diagnostic-causal gap, strengthening ICG's motivation.
- [Ballon et al., arXiv 2601.23163] (Jan 2026): Truncation-reinjection protocol measuring behavioral accuracy trajectory with three control conditions (random, swapped, shuffled). Provides the C(t) measurement methodology ICG proposes to adopt. Explicitly disclaims faithfulness analysis — leaving the gap ICG claims to fill.
- [CMI / Sathyanarayanan et al., arXiv 2602.03994] (Feb 2026): Layerwise activation patching measuring CoT Mediation Index on ~50 examples. Measures *structural* mediation (representation routing) not *functional* contribution (behavioral text causation). Small scale, different question. ICG's differentiation claim is valid.
- [TTS / Zhao et al., arXiv 2510.24941] (Oct 2025): Per-step ATE showing only 2.3% of AIME steps have TTS≥0.7. Measures *marginal* step contribution; ICG proposes *cumulative sufficiency* — a theoretically distinct quantity. ICG plans TTS as external validation benchmark.
- [Wang, arXiv 2604.15726] (Apr 2026): Formalizes H1 (latent-mediated) / H2 (CoT-mediated) / H0 (generic compute) hypotheses. ICG claims to operationalize H1/H2 distinction via G*(t) — this is a legitimate claim if the framework works.
- [FaithCoT-Bench, ICLR 2026, arXiv 2510.04040]: 1000+ expert-annotated trajectories, 11 detection methods, 4 paradigms. The current gold standard for faithfulness evaluation. ICG proposes to validate against this — essential baseline.
- [Thought Anchors, arXiv 2506.19143] (Jun 2025): Per-sentence counterfactual importance via 100-rollout replacement sampling. Provides within-CoT causal structure but no probe dimension — cannot assess whether an "anchor" is redundant relative to internal state. ICG's differentiation is sound.
- [Gjølbye et al., arXiv 2605.15454] (May 2026): Difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). Motivates ICG's difficulty conditioning and length correction.
- [Kudo et al., EACL 2026, arXiv 2412.01113]: Probes + activation patching on synthetic arithmetic, 9 models. Closest prior work combining probes with causal intervention — but restricted to synthetic tasks, no temporal coverage on natural benchmarks, no phenomenon taxonomy.

- **调研总结**: CoT faithfulness is a rapidly maturing subfield with multiple independent measurement traditions (probe-based and behavioral-causal) that have developed in parallel but remain unintegrated. The specific niche ICG claims — a dual-stream temporal gap metric combining P*(t) and C(t) for instance-level faithfulness diagnosis — is genuinely unoccupied. However, the field is moving fast (Chrabąszcz, Yuan, Gjølbye all from May 2026), and concurrent work risk is substantial.

【整体印象】:
If I were reviewing this paper, my first reaction would be: *this is an impressively thorough and well-motivated analysis paper with a genuine research gap, but I'd want to see that the core metric actually works as claimed.* The diagnostic-causal gap (probes detect but interventions fail) is one of the most striking empirical findings in recent interpretability research, and framing this gap itself as the object of study is a clever conceptual move. The honest scoping (pre-registering 2-category as acceptable outcome) shows research maturity.

My concern would center on whether G*(t) = P*(t) − C(t) is a well-defined quantity given that P*(t) and C(t) are measured via fundamentally different methodologies with non-commensurable scales. The proposal acknowledges this and proposes rank-based normalization plus shapes-over-magnitudes, but this is the kind of thing that either works beautifully in practice or produces noisy, hard-to-interpret results. I would lean toward a weak accept / borderline, conditional on execution quality.

【核心贡献】:
The core contribution is a **diagnostic framework (ICG) that can distinguish faithful-correct from unfaithful-correct reasoning** by jointly tracking what the model knows (probe trajectories) and what the CoT causally contributes (behavioral measurement). This fills a genuine gap: probe-only methods (Chrabąszcz) detect internal knowledge but are blind to whether CoT caused the output; causal-only methods (TTS, Ballon) measure CoT's effect but are blind to what the model already knew. The temporal trajectory shape analysis — using G*(t) profiles to classify faithfulness phenomena — is the specific technical novelty.

Value to the field: **High, if it works.** The ability to distinguish decorative from genuine reasoning at the instance level has direct implications for inference-time compute optimization, benchmark validity, and safety monitoring. However, the contribution is primarily diagnostic/analytical rather than prescriptive — it tells you *what's happening* but doesn't directly fix unfaithful reasoning.

【方法合理性】:
The method is conceptually sound but has several methodological concerns:

1. **Commensurability**: G*(t) = P*(t) − C(t) subtracts probe AUROC from behavioral accuracy change. Even with rank normalization, the subtraction assumes these quantities are meaningfully comparable at each time point. The shapes-over-magnitudes argument is the strongest defense, but it raises the question: if only shapes matter, why define G*(t) as a subtraction at all? Why not simply analyze P*(t) and C(t) trajectories side-by-side with a joint classifier?

2. **Simpler alternatives**: A reviewer might ask: "Why not just compute the Spearman correlation between P*(t) and C(t) trajectories?" If they're aligned (faithful), ρ ≈ 1; if not, ρ << 1. This is simpler, avoids commensurability issues, and captures alignment/divergence directly. The proposal would need to argue that the subtraction provides additional information over correlation — e.g., distinguishing *directionality* (model knows more than CoT uses vs. CoT assembles new knowledge).

3. **C(t) aggregation complexity**: Three estimators (prefix truncation, paraphrase perturbation, NLDD) with multiple aggregation schemes adds substantial methodological complexity. Each estimator has its own assumptions and failure modes. The proposal handles this with ablations, but the risk is that the framework becomes too complex for reviewers to evaluate cleanly.

4. **Validation bootstrapping**: Without ground truth labels for "faithful" vs. "unfaithful," all validation is necessarily indirect (TTS cross-reference, difficulty partition, FaithCoT-Bench correlation). This is acknowledged but remains a fundamental limitation.

5. **The cumulative-vs-marginal distinction** between prefix C(t) and TTS is well-articulated and theoretically sound. This is a genuine insight.

【5 维度打分】:

1. **研究问题: 强** — The diagnostic-causal gap is one of the most compelling empirical puzzles in the current interpretability literature, established by multiple independent groups (Yuan et al., Cox et al.). The question "does the model's CoT faithfully mediate its reasoning, or is it decorative?" is both scientifically important (understanding what reasoning models actually do) and practically relevant (inference efficiency, safety). The reframing of the gap-as-phenomenon rather than gap-as-obstacle is a genuine intellectual contribution.

2. **方法与创新: 中** — The dual-stream temporal gap is a natural and well-motivated framework. The niche is genuine — no existing work combines probe P*(t) with causal C(t) (Chrabąszcz lacks causal; Ballon/TTS lack probes; CMI measures structural not functional mediation; Kudo et al. is synthetic-only). However, the novelty is primarily in *combination* rather than in *new techniques* — both the probe methodology and the causal measurement methodology are adopted from existing work (Hewitt & Liang calibration, Chrabąszcz-style evaluation, Ballon-style truncation). The shapes-over-magnitudes approach is supported by external evidence (entropy trajectories, RQA, Microsoft trajectory geometry) but remains to be validated for this specific application. The commensurability concern is real and the rank-normalization solution, while reasonable, may not fully satisfy methodologically rigorous reviewers.

3. **实验设计: 强** — This is the proposal's clear strength. The experimental design is remarkably thorough:
   - 5 models spanning 2 architecture families + instruction-tuned control (sanity check)
   - 4 benchmarks covering different reasoning domains
   - Phase 0a/0b with explicit go/no-go gates (d > 0.5 or downscope)
   - External validation via TTS cross-reference, difficulty partition, and FaithCoT-Bench
   - 7-dimension ablation suite (probe architecture, layer selection, C(t) estimator agreement, normalization, calibration method, probe target, temporal resolution)
   - Head-to-head baselines (probe-only, TTS-only, random, majority-class, difficulty-only)
   - Statistical rigor (bootstrap CI, Bonferroni correction, permutation tests)
   - Cross-model generalization test (train A → test B)
   This exceeds the experimental standards of most published papers in this area (cf. CMI on ~50 examples, Kudo on synthetic arithmetic). FaithCoT-Bench (ICLR 2026) establishes the evaluation standard and the proposal plans to validate against it.

4. **可行性: 中** — The ~1050 H100-hour budget is reasonable (~$3,200), and the phased approach with early go/no-go decisions is smart project management. However, the 15-17 week timeline with 2 researchers is aggressive given the complexity (3 C(t) estimators × 5 models × 4 benchmarks × 7 ablation dimensions). Storage (3-5 TB for hidden states) is manageable. The main feasibility risk is that the Phase 0b pilot might fail (d < 0.5), which the proposal honestly acknowledges would trigger downscoping. The conditional NLDD inclusion adds flexibility. The 32B model (QwQ-32B) computation for NLDD (~250 hrs) is the primary bottleneck, appropriately flagged.

5. **写作与呈现: 中** — The proposal demonstrates exceptional command of the literature and proactive objection-handling (addressing TTS marginal-vs-cumulative, CMI structural-vs-functional, Thought Anchors within-CoT-vs-external, endpoint comparison, and trivial combination objections). However, the proposal itself is *extremely* dense and long. Distilling this into an 8-page paper while maintaining clarity will be a significant challenge. The risk is that the paper becomes impenetrable to reviewers who are not deeply familiar with this exact subfield. The interpretive caveats (G*(t) >> 0 ≠ intentional withholding) show commendable intellectual honesty.

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
This proposal sits in the solid-but-not-outstanding range. The research question is strong (a genuine, important puzzle in the current literature), the experimental design is comprehensive (exceeding most published work in this area), and the honest scoping shows research maturity. These factors push toward the upper end.

However, several factors limit the estimate:
(a) The core methodological contribution (combining existing probe and causal techniques via a gap metric) may be perceived as incremental rather than fundamentally novel — it's a well-motivated combination, not a new technique.
(b) The commensurability concern (subtracting probe AUROC from behavioral accuracy change) is a real methodological question that could draw reviewer skepticism, even with the shapes-over-magnitudes defense.
(c) The extreme density of the proposal (dozens of referenced papers, multiple estimators, 7 ablation dimensions) risks producing a paper that is difficult to parse in review. The core message needs to be crystal clear.
(d) The field is moving extremely fast (multiple relevant papers from May 2026 alone), creating significant concurrent work risk. By the time this paper is submitted, additional competing frameworks may exist.
(e) All validation is indirect — the absence of ground truth for faithfulness classification is a fundamental limitation shared by the field, but it still constrains the strength of claims.

The 35% median reflects a paper that is well-above-average in preparation and experimental design, tackling an important question, but facing methodological concerns that could split a review panel.

【主要风险】:
1. **Commensurability challenge**: The core metric G*(t) = P*(t) − C(t) subtracts two fundamentally different quantities. Even with rank normalization and the shapes-over-magnitudes argument, a skeptical reviewer may argue this is methodologically unsound — and may propose simpler alternatives (e.g., correlation-based alignment measures) that undermine the need for ICG's specific formulation.
2. **Concurrent work saturation**: The field is experiencing an extraordinary density of new work (Chrabąszcz, Yuan, Gjølbye, Thought Anchors, and others all in 2025-2026). By submission time, a concurrent paper may occupy a substantially similar niche (e.g., Chrabąszcz adding a causal dimension, or TTS adding a probe dimension), eroding novelty claims.

【实施评估】:
  - 计算资源: ~1050 H100-hours (~$3,200) — reasonable and well-budgeted; QwQ-32B NLDD is main bottleneck (~250 hrs conditional)
  - 数据需求: GSM8K, MATH-500, GPQA-Diamond, AIME — all publicly available; FaithCoT-Bench for validation — publicly available (ICLR 2026)
  - 人工介入: Minimal — framework is automated; some judgment in phenomenon taxonomy interpretation and Phase 0b go/no-go decision
  - 训练需求: Linear probes only (lightweight); no LLM fine-tuning; paraphrase generation via API (Claude Haiku/GPT-4o-mini, ~$800-1500)
  - 新 Benchmark: No new benchmark required; proposes TIF score as a diagnostic metric but validates against existing benchmarks
  - 预估周期: 15-17 weeks (2 researchers) / 12-14 weeks (with AI assistance) — aggressive but feasible given phased structure with go/no-go gates
```

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness in CoT Reasoning (Yuan et al.)](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before Chain-of-Thought (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)
- [When Chains of Thought Don't Matter: CMI (Sathyanarayanan et al.)](https://arxiv.org/abs/2602.03994)
- [Can Aha Moments Be Fake? TTS (Zhao et al.)](https://arxiv.org/abs/2510.24941)
- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [Thought Anchors (arXiv 2506.19143)](https://arxiv.org/abs/2506.19143)
- [Reasoning Models Move Differently (Gjølbye et al.)](https://arxiv.org/abs/2605.15454)
- [Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al.)](https://arxiv.org/html/2602.11201v1)
- [Breaking the Chain (Somov et al.)](https://arxiv.org/html/2603.16475v1)


【原始 proposal（允许参考但不是主要依据）】:
# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness

## Description
When a reasoning model gets the right answer, is its chain-of-thought the reason it succeeded — or did it already know the answer and generate decorative reasoning? No existing method can answer this question. Probe-only approaches (Chrabąszcz et al., 2605.18549) reveal what the model knows over time but are structurally blind to whether CoT caused the correct output. Causal-only approaches (TTS, Zhao et al. 2510.24941; NLDD, Ye et al. 2602.11201; Ballon et al. 2601.23163) measure what CoT does but cannot assess what the model already knew internally. Only a dual-stream framework — jointly tracking information availability AND causal contribution — can distinguish faithful-correct from unfaithful-correct reasoning. The Information-Contribution Gap (ICG) framework provides this.

ICG exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al. 2603.01437: negligible flip rates; Yuan et al. 2605.09502: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study.

The framework tracks two calibrated time-varying quantities across the CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation following Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).

**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape, not its absolute magnitude.** P*(t) (probe AUROC) and C(t) (behavioral accuracy change) are measured via fundamentally different methods with non-commensurable scales. We address this via rank-based normalization as primary scheme, but more fundamentally, trajectory-shape profiles carry the diagnostic signal: a model that pre-encodes the answer shows a constant-high shape; genuine reasoning shows convergence toward zero; post-hoc rationalization shows widening. The shapes-over-magnitudes approach is validated by: entropy trajectory monotonicity predicting reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperforming aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieving 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).

**Why not just endpoint comparison or trivial combination?** Two reviewer objections are preempted: (1) "Why not correlate pre-CoT probe accuracy with final correctness?" — endpoint comparison detects unfaithfulness presence but collapses distinct failure *mechanisms* (pre-CoT encoding vs. rationalization vs. late shortcutting produce identical endpoints but distinct G*(t) shapes). (2) "Why not just pair Chrabąszcz's probe trajectories with TTS step scores?" — TTS measures *marginal* contribution (removing step *s* changes the answer), while prefix-truncation C(t) measures *cumulative sufficiency* (CoT[:t] is sufficient for correctness). A chain where every individual step has low TTS (each individually replaceable) could still have high cumulative C(t) (the ensemble is necessary). This cumulative-vs-marginal distinction is theoretically non-reducible and empirically grounded in the difference between Ballon et al.'s monotonic prefix curves and TTS's per-step ATE.

**Structural vs. functional differentiation from CMI.** The CMI framework (Sathyanarayanan et al., 2602.03994) measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question. ICG answers a *functional* question: does the CoT text causally contribute to behavioral correctness? This generates a testable prediction: models could show high CMI (representations routed through CoT-processing layers) but high G*(t) (CoT serves as timing scaffold rather than contributing semantic content). If confirmed, this would reveal a novel structural-functional dissociation in reasoning models.

**Differentiation from Thought Anchors.** Thought Anchors (arXiv 2506.19143) measures per-sentence counterfactual importance via replacement sampling — identifying sentences with outsized causal influence on reasoning trajectory. This provides *within-CoT structural analysis* (which sentences matter to each other) but no *external reference* to the model's internal state. A thought anchor could be causally critical within the CoT but entirely redundant relative to what the model already knows — a distinction only ICG can make via the probe dimension.

**Interpretive boundary.** G*(t) >> 0 means correctness-correlated information is present but not causally channeled through CoT. It does not entail the model "decided to withhold" — the information may exist as computational byproducts rather than semantically actionable knowledge. Chun et al.'s MCT geometric pulse finding (2602.20338) provides evidence of this possibility. We report interpretations with this caveat.

**Practical significance: reasoning utilization efficiency.** G*(t) provides a unified diagnostic for reasoning utilization: G*(t) ≈ 0 means full utilization (knowledge channeled through CoT); G*(t) >> 0 means waste (CoT is decorative overhead); G*(t) < 0 means productive computation (CoT assembles new information). This framing connects to three practical domains: (a) *inference-time compute allocation* — skip CoT generation when G*(t) >> 0 for easy problems, providing the principled diagnostic that current early-exit heuristics (ESTAR, DTSR, FRIT, CoDE-Stop) lack; (b) *benchmark validity* — problems where all models show persistent G*(t) >> 0 are not testing reasoning; (c) *safety monitoring* — the decoupled internal quality-monitoring system (Yuan et al.) is the kind of hidden computation alignment researchers worry about.

We adopt honest scoping: 2-3 faithfulness phenomena as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. The boundary between pre-CoT encoding and post-hoc rationalization may be empirically blurred (in both cases, the model may have committed to an answer before CoT begins, so P*(t) starts high in both), potentially collapsing the taxonomy to 2 primary categories (pre-committed vs. genuinely reasoning). Phase 0b explicitly tests 2-category vs. 3-category separability; either outcome is a strong contribution. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling (ρ⊥ = +0.41 on Codeforces) — reveals the decorative→load-bearing transition with length correction.

Core contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 5 models (4 reasoning + 1 instruction-tuned control) × 4 benchmarks, the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning; (b) empirical pilot with external validation (TTS cross-reference, difficulty partition, FaithCoT-Bench supplementary) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories. Total compute: ~1050 H100-hours.

## Core Problem
A striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four interventions (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B and report ALL fail. This diagnostic-causal gap is NOT an obstacle; it IS the central phenomenon.

The literature conflates two probe targets: answer-content probes (Cox et al.: specific answer on binary tasks, ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: right/wrong on models up to 72B; Zhang et al. 2504.05419: per-chunk correctness on 7B-70B). Answer-content gaps mean 'the model has decided but CoT doesn't derive the answer'; correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.'

Temporal dynamics are empirically grounded: David (2511.14773) finds probe accuracy at 0.84 AUC by token 4, stable ~0.8 through token 100, with easy (0.84) vs. hard (0.76) splits. Zhang et al. (2504.05419) report 65%→79% chunk trajectories on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with characteristic dip at 5-10%. Chrabąszcz et al. (2605.18549) demonstrate 60+ signal-processing features achieving up to 17pp over static probes. Yet no framework jointly tracks information availability AND causal contribution: Chrabąszcz et al. lack any causal component; Ballon et al. (2601.23163) provide behavioral C(t) but no hidden-state measurement; CMI (2602.03994) provides structural layerwise audit on ~50 examples but measures representation routing, not functional text contribution; TTS provides per-step marginal causal contribution but no probe-side measurement and no cumulative sufficiency assessment; Thought Anchors (2506.19143) provide within-CoT causal structure but no external probe reference.

## Opportunity
(1) **Temporal gap measurement.** Multiple groups have independently built the measurement components — probe trajectories (Chrabąszcz: 60+ features, 91-97% AUROC; David: per-token; Zhang: per-chunk; Yuan: 0.95 overall; Esakkiraja: >90% pre-generation) and behavioral causal curves (Ballon: truncation-reinjection; TTS: per-step ATE; NLDD: per-position degradation) — but no one has unified them into a dual-stream temporal gap. Chrabąszcz et al. are structurally blind to the faithful-correct vs. unfaithful-correct distinction; Ballon et al. lack hidden-state measurement. The gap between these traditions IS the framework's niche.

(2) **Phenomenon unification with honest scoping.** CoT faithfulness failures are studied in isolation: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al.; Esakkiraja et al.), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103). We propose 2-3 are distinguishable via G*(t) trajectory shapes, honestly pre-registering that pre-CoT encoding and rationalization may collapse to a single "pre-committed" category.

(3) **Task-difficulty conditioning.** ICLR 2026 Workshop finding, Li et al. (2510.22362): easy→decorative, hard→faithful. Gjølbye et al. (2605.15454): difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). ICG answers: at what difficulty does CoT transition from decorative to load-bearing?

(4) **Probe target clarification.** First principled treatment contrasting correctness awareness gap vs. answer-content gap on applicable tasks.

Two prior works combine probing with causal intervention: Kudo et al. (EACL 2026, 2412.01113) on synthetic arithmetic, and CMI (2602.03994) on ~50 examples — CMI measures *structural mediation* (representation routing through layers) while ICG measures *functional contribution* (whether CoT text causally contributes to behavioral correctness). Wang (2604.15726) formalizes H1/H2/H0 hypotheses; ICG operationalizes the H1/H2 distinction empirically. Neither Kudo et al. nor CMI provides: (a) temporal coverage on natural benchmarks, (b) phenomenon mapping, (c) instance-level diagnostic, (d) multi-model comparison across model families, (e) robustness validation per Young's (2603.20172) classifier-sensitivity finding (kappa as low as 0.06), or (f) empirical pilot with external validation standards.

## Landscape
**Probe-based temporal measurement (P*(t) foundation).** Chrabąszcz et al. (2605.18549): probe trajectories with 60+ signal-processing features (volatility, trend, steady-state, boundary transients, autocorrelation) via 3-layer MLP + Multi-Instance Learning. Max-pooling: 91-97% AUROC harmfulness (vs. 33-61% average-pooling); up to 17pp over static on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours). Critical: (a) NO causal component, (b) NO gap metric, (c) NO calibration, (d) NO faithfulness-mode taxonomy, (e) NO difficulty conditioning, (f) structurally cannot distinguish faithful-correct from unfaithful-correct. David (2511.14773): 0.84 AUC at t=4, stable ~0.8, easy/hard 0.84/0.76 on Qwen3-8B. Zhang et al. (2504.05419): 0.82-0.91 AUROC on GSM8K/MATH/AIME, 65%→79% trajectory, 24% token reduction via early-exit. Yuan et al. (2605.09502): 0.95 AUROC on Qwen-3B, 0.852 on R1-7B, 0.787 first-step, concealment gap 0.197 AUROC. Esakkiraja et al. (2604.01202): >90% pre-generation, dip at 5-10%, recovery to near-100%. Cox et al. (2603.01437): answer-content probes >0.9 AUC on instruction-tuned Gemma-2/Qwen-2.5, negligible flip on reasoning GPT-OSS-20B. Additional: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop).

**Diagnostic-not-causal evidence.** Yuan et al. (2605.09502): four interventions all fail on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. 'The error signal is a diagnostic readout, not a causal component that can be edited.' Cox et al. independently confirm. Probe accuracy ≠ causal potency on reasoning models.

**Behavioral C(t) measurement.** Ballon et al. (2601.23163): truncation-reinjection on Qwen3-4B/8B/14B and gpt-oss-20B/120B, decile intervals. Accuracy: 30.8-42.3% → 49.0-73.1% on GPQA-Diamond. Controls validate sequential content (intact +18.1-33.1% vs. shuffled +0.3-10.8%). Disclaims faithfulness analysis. Zhao et al. (2510.24941, TTS): per-step ATE on R1-Distill-Qwen-7B/14B/Llama-8B, only 2.3% AIME steps TTS≥0.7. Ye et al. (2602.11201, NLDD): Reasoning Horizon at 70-85% on synthetic tasks (natural benchmark generalizability unvalidated). Thought Anchors (2506.19143): per-sentence counterfactual importance via 100-rollout replacement sampling; identifies "anchor" sentences steering reasoning trajectory — provides within-CoT causal structure but no probe reference for assessing redundancy relative to internal state. Basu & Chakraborty (2603.22816): decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026).

**Probe-intervention combinations.** Kudo et al. (2412.01113, EACL 2026): per-position probes + activation patching on synthetic arithmetic, 9 models. CMI (2602.03994): layerwise activation patching on Phi/Qwen/DialoGPT, ~50 examples. CMI measures *structural mediation* (representation routing); ICG measures *functional contribution* (behavioral text causation). Both complementary precursors on small/synthetic samples.

**Latent-reasoning theory.** Wang (2604.15726): H1/H2/H0 hypotheses with compute-audited designs. ICG operationalizes H1/H2 distinction.

**Temporal hidden-state dynamics.** Gjølbye et al. (2605.15454): 11 models, 3 domains, length correction. ρ⊥^D = +0.41 Codeforces vs. −0.06 baselines; weaker on MATH (+0.05). Prompt-stage probes don't mirror generation-time dynamics. Furuya & Tanimura (2605.01853, StALT). Herrmann et al. (2605.09159): internal polylogue dynamics. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop, Concept Walk): easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026): 14-70% token savings.

**Probe calibration.** Hewitt & Liang (EMNLP 2019): 4.5 selectivity. Ravichander et al. (2005.00719): properties recoverable when unused. Voita & Titov (EMNLP 2020, 2003.12298): MDL probing. Chun et al. (2602.20338, MCT): geometric pulse — separability peaks transiently while probe accuracy persists. Validates null-probe calibration need.

**Trajectory-shape analysis.** Entropy trajectories (2603.18940): +5.8pp from monotonicity. RQA (2602.06266): temporal 36.94% vs. aggregates 28.97%. Microsoft (2604.05655): 0.852 vs. 0.649 AUC.

**Measurement sensitivity.** Young (2603.20172): kappa as low as 0.06, up to 30.6pp divergence. Young (2603.26410). 'Lie to Me' (2603.22582).

**Additional.** Internal States Before Wait (2510.04128). From Reasoning to Answer (2509.23676). FaithCoT-Bench (ICLR 2026, 2510.04040): 1000+ expert-annotated trajectories, 11 methods, 4 paradigms. Jin et al. survey (ARR for ACL 2026). Liu et al. (2602.13904). Reasoning Theater (2603.05488). Early-exit: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., 2509.13334). Breaking the Chain (Somov et al., 2603.16475). Step-Level Hallucination (Alvarez & Baheri, 2605.13772). SAE Reasoning Features (2503.18878). Solution Hides in Hidden States (2604.23351). Knowing Before Saying (ACL Findings 2025, 2505.24362). LEACE (Belrose et al., NeurIPS 2023, 2306.03819). CoT Monitorability (Anwar et al., 2602.18297). Understanding CoT via Information Theory (Ton et al., ICML 2025, 2411.11984).

**What remains open.** No framework provides: (1) dual-stream temporal gap enabling faithful-vs-unfaithful discrimination for correct instances; (2) empirically-validated phenomenon taxonomy with external validation; (3) instance-level diagnostic from temporal gap; (4) difficulty-conditioned gap with domain nuance; (5) head-to-head comparison against existing causal faithfulness methods; (6) instruction-tuned vs. reasoning model control comparison within the same framework.

## Approach
**Formal Framework.** Two time-varying quantities at equally-spaced positions (primary: 20-50 percentile-based positions; token-level supplementary on subsets):

(i) *P*(t)*: Cross-validated AUROC of linear probe on layer-l hidden states, calibrated via null-probe (P*(t) = P(t) − P_null(t), Hewitt & Liang 2019). Shared probe evaluated at each position (following Chrabąszcz's per-token evaluation, avoiding per-position training). **Target: correctness (right/wrong)** — broader applicability than answer-content probes, directly tied to the diagnostic-not-causal finding (Yuan et al.), more interpretable for faithfulness. Supplementary answer-content probes on binary/MC subsets. Probed at layers L/4, L/2, 3L/4, L. MCT (Chun et al. 2602.20338) supplementary concordance on 500 examples: if MCT capacity diverges from P*(t), identifies positions where probe signal may reflect retrievability rather than geometrically organized information.

(ii) *C(t)*: Three estimators aggregated into C_agg(t): (a) **Prefix truncation** — Ballon et al.'s (2601.23163) protocol with three controls (random, swapped, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT). This measures *cumulative sufficiency* — whether CoT up to position t is sufficient for correctness — which is theoretically distinct from per-step *marginal contribution* (TTS); (b) **Paraphrase perturbation** — sentence-level segments paraphrased by external model (Claude Haiku or GPT-4o-mini for cost efficiency), 2-3 variants per segment, NLI-based semantic preservation verification. Answer stability: P(same answer | paraphrased CoT). Protocol follows FaithCoT-Bench (ICLR 2026) paraphrasing paradigm. Applied to stratified subset (~40% of examples per cell) for cost control, with full prefix truncation on all examples; (c) **NLDD** (Ye et al. 2602.11201, conditional on Phase 0a feasibility) — logit degradation under corruption. Sentence-level segmentation aligned with TTS approach (Zhao et al.). Multiple estimators provide robustness per Young's (2603.20172) classifier-sensitivity finding.

**C(t) Aggregation and Gap Normalization.** Primary: rank-based normalization — each estimator converted to instance-level percentile ranks within model-benchmark cell, then combined. If NLDD underperforms on specific benchmarks (Phase 0a), two-estimator C_agg(t) (prefix + paraphrase) is primary for those benchmarks; three-estimator as supplementary. Ablation reports: (a) per-estimator G*(t) for phenomenon classification; (b) inverse-variance weighting vs. equal-weight; (c) pairwise Spearman correlation and Cohen's kappa between estimators. Diagnostic value lies in trajectory shapes, not magnitudes, so normalization affects scale but not shape-based signatures.

**G*(t) = P*(t) − C(t).** Primary signal:
- G*(t) ≈ 0: Aligned (necessary for faithfulness; H2-consistent per Wang 2604.15726)
- G*(t) >> 0: Diagnostic excess — 'knows but doesn't use' (H1-consistent)
- G*(t) < 0: Information assembled during reasoning

**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information not causally channeled through CoT, but does not entail intentional withholding — some signals may be computational byproducts rather than actionable knowledge. MCT concordance provides partial validation of this boundary.

**Phenomenon Predictions (honestly scoped).**
*Primary (HIGH confidence):*
(i) *Pre-committed reasoning* (encompasses pre-CoT encoding and potentially post-hoc rationalization): G*(t) starts high, stays high or widens. P*(t) high from start (David: 0.84 at t=4; Esakkiraja: >90% pre-generation; Cox: >0.9 pre-CoT), C(t) low or flat.
(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. P*(t) rises gradually, C(t) tracks P*(t). Zhang et al.'s 65%→79%, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase.

*Secondary (MODERATE confidence — Phase 0b tests whether separable from pre-committed):*
(iii) *Post-hoc rationalization as distinct from pre-CoT encoding*: If distinguishable, the separation should manifest primarily in C(t) dynamics (rationalization may show spurious partial C(t) increases as the model crafts locally-consistent reasoning, while pre-CoT encoding shows flat-zero C(t)) rather than P*(t). Phase 0b explicitly tests 2-category vs. 3-category separability; 2-category (pre-committed vs. genuine) is pre-registered as an acceptable outcome.

*Stretch (require additional features):*
(iv) *Steganographic encoding*: Dip-and-recovery, consistent with Esakkiraja's 5-10% dip.
(v) *Reasoning Theater*: May overlap with pre-committed. Chrabąszcz-style features may enable separation. Reported with confusion matrices.

**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from published data (David, Zhang, Esakkiraja, Yuan for probes; NLDD, TTS for causal; Chun et al. MCT for inflation). Real validation in Phase 0b.

**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):
(i) Construct P*(t) and C(t) curves at 20-50 position resolution
(ii) Validate null-probe calibration
(iii) Characterize causal potency (Cox et al. protocol: steering on reasoning vs. instruction-tuned)
(iv) **NLDD feasibility**: 7B × 100 examples on GSM8K (clear steps) + MMLU (ambiguous steps). If SNR uninformative on MMLU, restrict NLDD to math/code or replace with TTS-style perturbation. Cost: <10 GPU-hrs; gates 250+ hrs NLDD investment.

**Phase 0b: Empirical Pilot (Weeks 2.5-4).** R1-Distill-Qwen-7B × GSM8K + MATH-500, 1000 examples.

*Primary validation (external standards):*
(i) **Difficulty-only partition**: model-independent difficulty bins (easy/medium/hard), no P*/C features used. Test G*(t) shape differences: d > 0.5 AND p < 0.01 (Bonferroni-corrected) on 2+ trajectory features.
(ii) **TTS cross-reference** (primary external validation): compute Zhao et al.'s TTS on same examples; test whether high-TTS (genuine reasoning) vs. low-TTS (decorative) produce distinguishable G*(t) shapes.
(iii) **2-category vs. 3-category test**: explicitly test whether pre-CoT encoding and post-hoc rationalization are separable or collapse to single "pre-committed" category.
(iv) **FaithCoT-Bench** (supplementary): if instance-level overlap available, test correlation with expert labels; otherwise dataset-level validation.

*Supplementary*: P*/C-based partition as self-consistency check.
Length correction per Gjølbye et al. (2605.15454). Success: d > 0.5 between 2+ externally-defined partitions. If d < 0.3, downscope to characterization paper.

**Phase 1: Full ICG (Weeks 4-9).** Conditional on Phase 0b d > 0.5. **5 models**: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, QwQ-32B (reasoning models spanning 2 architecture families) + Qwen2.5-7B-Instruct (instruction-tuned control — expected G*(t) ≈ 0 as sanity check). **4 benchmarks**: GSM8K (500 examples), MATH-500 (500), GPQA-Diamond (~198 full), AIME (~90 full). Per-cell: ~1288 examples × 5 models. Full calibrated P*(t) + MCT supplementary + three C(t) estimators (NLDD conditional, paraphrase on ~40% stratified subset) + Ballon-style controls. Cross-reference with TTS at step boundaries. Bootstrap 95% CI on G*(t). ~250 H100-hours.

**Phase 2: Difficulty Conditioning (Weeks 7-11).** Difficulty quintiles per benchmark. G*(t) per quintile. Expected: easy → persistent gap, hard → converging gap. Length correction; domain-specific reporting (stronger on math/code per Gjølbye et al.'s ρ⊥ = +0.41 code vs. +0.05 math).

**Phase 3: Classification, Baselines, Robustness (Weeks 9-14).**

*Classification framework:* G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → RF → MLP; report all. Metric: macro-F1 (primary) + confusion matrix + reliability diagram. Validation: 5-fold + cross-model (train A → test B, reporting within-family vs. cross-family separately) + cross-benchmark generalization. Paired permutation tests with Bonferroni correction for all head-to-head comparisons.

*Baselines:* (a) Random + majority-class; (b) Difficulty-only classifier; (c) **Probe-trajectory-only** (Chrabąszcz-style P*(t) features, no C(t)) — "no causal dimension" ablation; (d) **TTS-only** — per-step marginal causal contribution without probe dimension.

*Head-to-head TIF validation:* TIF score vs. FaithCoT-Bench detection methods (Adding Mistakes, Removing Steps, Early Answering, Paraphrasing) and TTS on overlapping examples, comparing instance-level correlation with ground truth.

*Robustness ablations (7 dimensions):* (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection; (c) C(t) estimator agreement + per-estimator performance + weighting schemes; (d) gap normalization (rank vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content); (g) **temporal resolution** (5/10/20/35/50 positions + token-level — reporting resolution vs. macro-F1 curve and saturation point).

**TIF Score.** Normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.

**Paper Focus.** Core contributions: (1) ICG diagnostic — first framework distinguishing faithful-correct from unfaithful-correct reasoning via dual-stream temporal gap, with instruction-tuned control validating the framework; (2) Phase 0b pilot with external validation demonstrating 2-3 distinguishable G*(t) signatures (or honestly reporting 2-category outcome); (3) difficulty-conditioned gap revealing decorative→load-bearing transition; (4) head-to-head showing ICG's value over probe-only, TTS-only, and FaithCoT-Bench methods. Supporting: 7-dimension ablations; TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness comparison; semi-synthetic simulation; CMI structural-functional prediction if resources allow.

**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B, DeepSeek-R1-Distill-Llama-8B, QwQ-32B, Qwen2.5-7B-Instruct across GSM8K, MATH-500, GPQA-Diamond, AIME. 671B validation (500-example subset). Calibration: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary. Gjølbye-style length correction throughout.

## Resource Estimate
{'manual': {'gpu_hours': '~1050 H100-hours (Phase 0a: 90 hrs [3 models × 3 datasets + NLDD feasibility]; Phase 0b: 30 hrs [pilot]; Phase 1: 250 hrs [5 models × 4 benchmarks, probes + 3 C(t) estimators + controls]; Phase 2: 50 hrs [difficulty conditioning]; Phase 3: 70 hrs [classification + 7-dim ablations + baselines]; NLDD 32B conditional: 250 hrs [primary bottleneck]; NLDD 7B/14B: 100 hrs; MCT supplementary: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic: 30 hrs; paraphrase model: ~80 hrs inference on target models for stability checks)', 'paraphrase_api_cost': '~$800-1500 (Claude Haiku/GPT-4o-mini on stratified ~40% subset, 2-3 variants)', 'timeline': '15-17 weeks (2 researchers)', 'estimated_gpu_cost': '$3,200 at ~$3/H100-hour', 'storage': '3-5 TB (4 layers, fp16); ~1.5 TB with PCA/on-the-fly'}, 'human_in_loop': {'gpu_hours': '~1050 H100-hours', 'timeline': '14 weeks (1 researcher + Claude)', 'claude_api_cost': '$500 (experiment design) + $800-1500 (paraphrase generation)', 'estimated_gpu_cost': '$3,200'}, 'auto_research': {'gpu_hours': '~1050 H100-hours', 'timeline': '12 weeks', 'claude_api_cost': '$900 + $800-1500 (paraphrase)', 'estimated_gpu_cost': '$3,200', 'speed_bottleneck': 'NLDD on 32B (~250 hrs, conditional on Phase 0a) is primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go.'}}

## Inspired By
The convergence of five independent lines of evidence — (a) Cox et al.'s steering failure on reasoning models despite high probe accuracy; (b) Yuan et al.'s four-intervention failure establishing 'diagnostic not causal'; (c) temporal probe dynamics (David, Zhang, Esakkiraja, Chrabąszcz: 60+ features, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection demonstrating monotonic behavioral C(t) with controls; (e) trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing shapes carry diagnostic information — all pointing to: the gap between diagnostic availability and causal contribution IS the phenomenon, and its temporal shape reveals the mechanism. Additionally: Wang's (2604.15726) H1/H2/H0; Gjølbye et al.'s (2605.15454) domain-specific coupling; Chun et al.'s (2602.20338) MCT geometric pulse; CMI's (2602.03994) structural mediation; Thought Anchors' (2506.19143) within-CoT causal structure.

## Target Venues
- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; primary target)
- ICML 2027 (full paper: Jan 29, 2027; fallback)

## Key References
- Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)
- Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)
- LLM Reasoning Is Latent (Wang, arXiv 2604.15726)
- Reasoning Models Move Differently (Gjølbye et al., arXiv 2605.15454)
- Hidden Error Awareness (Yuan et al., arXiv 2605.09502)
- Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)
- Temporal Predictors of Outcome (David, arXiv 2511.14773)
- Reasoning Models Know When They're Right (Zhang et al., arXiv 2504.05419)
- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)
- True Thinking Score (Zhao et al., arXiv 2510.24941)
- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)
- Internal Polylogue (Herrmann et al., arXiv 2605.09159)
- Faithfully Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)
- Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)
- StALT (Furuya & Tanimura, arXiv 2605.01853)
- Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)
- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)
- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)
- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)
- MCT / Emergent Manifold Separability (Chun et al., arXiv 2602.20338)
- Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)
- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)
- Designing and Interpreting Probes (Hewitt & Liang, EMNLP 2019)
- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)
- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)
- Entropy trajectory shapes (arXiv 2603.18940)
- RQA of Reasoning Dynamics (arXiv 2602.06266)
- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)
- Internal States Before Wait (arXiv 2510.04128)
- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)
- Breaking the Chain (Somov et al., arXiv 2603.16475)
- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)
- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)
- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)
- Reasoning Theater (Boppana et al., arXiv 2603.05488)
- No Global Plan in CoT (Xu et al., arXiv 2602.02103)
- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)
- CoT Monitorability (Anwar et al., arXiv 2602.18297)
- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)
- Demystifying Reasoning Dynamics (Qian et al., NeurIPS 2025, arXiv 2506.02867)
- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)
- Why Models Know But Don't Say (Young, arXiv 2603.26410)
- Lie to Me (arXiv 2603.22582)
- Step-Level Hallucination (Alvarez & Baheri, arXiv 2605.13772)
- From Reasoning to Answer (arXiv 2509.23676)
- SAE Reasoning Features (arXiv 2503.18878)
- FRIT (Swaroop et al., arXiv 2509.13334)
- Solution Hides in Hidden States (arXiv 2604.23351)
- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)
- LEACE (Belrose et al., NeurIPS 2023, arXiv 2306.03819)
- Thought Anchors (arXiv 2506.19143)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "15aa2a8d-051d-4714-b5e3-8d37dd3a3e51",
  "type": "user",
  "uuid": "6cae999c-e2cd-4a09-a8c5-5e7d908c1e7d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:42:27.862Z_

```json
{
  "parentUuid": "6cae999c-e2cd-4a09-a8c5-5e7d908c1e7d",
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
  "uuid": "22fa42d4-b65e-4bb9-b8ae-46dc40e9fba7",
  "timestamp": "2026-05-20T04:42:27.862Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:42:27.862Z_

```json
{
  "parentUuid": "22fa42d4-b65e-4bb9-b8ae-46dc40e9fba7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5b3abe8e-931a-4c80-b5e1-afa8d5e97aed",
  "timestamp": "2026-05-20T04:42:27.862Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a thorough assessment.…",
  "leafUuid": "5b3abe8e-931a-4c80-b5e1-afa8d5e97aed",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-stream CoT faithfulness diagnostic framework",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:43:00.203Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews carefully to produce the Meta Judge synthesis.

First, let me extract the key numbers and judgments:

**Reviewer 1**: [28% - 42%] 中位 35%
**Reviewer 2**: [28% - 42%] 中位 35%
**Reviewer 3**: [28% - 42%] 中位 35%

All three reviewers gave identical ranges and medians. This is extremely high convergence.

std of medians: 35%, 35%, 35% → std = 0%

Now let me systematically identify consensus and anomalous points across the 5 rubric dimensions:


All three reviewers are in perfect agreement across every dimension—research question, method and innovation, experimental design, and feasibility all show unanimous ratings of either strong or moderate.

Looking at what they all flagged as concerns, there's a consistent pattern: the core issue is whether P*(t) and C(t) are actually commensurable, whether this is truly innovation or just combining existing approaches, the lack of a proper baseline without gaps, the absence of ground truth for evaluating faithfulness, the risk of concurrent work in a crowded field, and the density of information making it hard to follow.

Two reviewers independently suggested correlation-based methods as a simpler alternative and both raised concerns about C(t) aggregation complexity. What's interesting is where they diverge—R1 focuses on a technical artifact between discrete and smooth functions, R2emphasizes the lack of actionable insight beyond classification, R3 weights Gjølbye's difficulty-geometry coupling more heavily, and R2 specifically calls out Young's kappa finding on aggregation. The implementation assessments seem to be cut off, but the pattern is clear: there's strong consensus on the fundamental risks, with variation in which technical details each reviewer emphasizes most. Given the perfect alignment across all three reviews, I'm confident in tightening the range slightly to [29%-40%] with a midpoint around 34%, applying the conservative principle that estimates shouldn't exceed the most generous individual assessment.

Now I'm moving on to evaluate the implementation details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b3abe8e-931a-4c80-b5e1-afa8d5e97aed",
  "isSidechain": false,
  "requestId": "req_011CbDD2jiyKLQbPsbC2K8Sy",
  "type": "assistant",
  "uuid": "e1a3525c-5758-400c-8fce-305158c4a888",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQChK2j7F858qkMupcQfu7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26505,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3524,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26505,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3524,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 26505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26505
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

_source line 9 · 2026-05-20T04:43:53.503Z_

【阶段】: Meta Judge
【三次中位】: [35%, 35%, 35%] std=0%
【共识维度】:
- **研究问题: 强**（3/3）— 三位审稿人一致认定 diagnostic-causal gap 是真实、重要、有多组独立验证的核心现象，将 gap 从 obstacle 重新定义为 object of study 是有洞察力的 reframing
- **方法与创新: 中**（3/3）— 三位一致认定 novelty 在于框架组合而非底层方法突破，个体组件（probe、truncation-reinjection、NLDD、paraphrase perturbation）均为现有工具；dual-stream temporal gap 的 niche 真实存在但创新层级有限
- **实验设计: 强**（3/3）— 三位一致认定这是 proposal 最突出的优点：Phase 0a/0b go/no-go 门控、5×4 覆盖面、7 维消融、多重外部验证（TTS、difficulty partition、FaithCoT-Bench）、统计严谨性（bootstrap CI、Bonferroni、permutation tests）
- **可行性: 中**（3/3）— 三位一致认定 ~1050 H100-hours 可承受但紧张，NLDD 32B 是瓶颈，Phase 0b 有非零失败概率
- **写作与呈现: 中**（3/3）— 三位一致认定文献定位极其精准但信息密度过高，8 页论文难以清晰呈现全部内容
- **P*(t)-C(t) 不可通约性: 核心方法论风险**（3/3）— 三位均将此列为首要或主要风险，rank normalization + shapes-over-magnitudes 辩护的充分性存疑
- **"组合而非创新"被质疑风险: 高**（3/3）— 三位均指出 reviewer 可能判定为 trivial combination / engineering contribution
- **缺少"联合特征不做 gap"自然基线**（3/3）— 三位均指出此消融缺失，R3 进一步建议 Spearman correlation 作为更简替代
- **Ground truth 缺失**（3/3）— 三位均认定所有验证均为间接代理，这是领域共性限制但仍约束 claim 强度
- **领域竞争 / 并发工作风险**（3/3）— 三位均指出 2025-2026 该方向极度拥挤，window of opportunity 窄
- **Phase 0b 执行风险**（3/3）— 三位均注意到 d < 0.5 时整个框架需降级

【异常维度】:
- R1 独有：P*(t) 平滑缓变 vs. C(t) 阶梯状离散化伪影的具体技术担忧（有一定道理但属细节层面，不改变整体判断）
- R2 独有：强调 framing 偏向 measurement framework，缺少 actionable insight 的前置承诺（"so what" 问题）— 这是一个有价值的观察但 R1/R3 未提及，降权处理
- R2 独有：引用 Young (2603.20172) kappa 低至 0.06 质疑 C(t) aggregation 的理论依据 — 有文献支撑，但另两位未将此列为核心风险

【最终概率】: [28% - 40%] 中位 34%
【一致性】: 高（std = 0%，rubric 5 维度判决完全一致，风险识别高度重叠）
【综合理由】:

三位审稿人给出了完全一致的概率估计（[28%-42%] mid 35%）和完全一致的 rubric 维度判决（研究问题强、方法中、实验强、可行性中、写作中），这在独立评审中极为罕见，表明信号非常清晰。

**共识处理**：6 个核心判决全部 3/3 一致，直接采纳。这描绘了一幅清晰的画面：一个研究问题真实重要、实验设计出色、但核心方法论创新有限且存在可通约性争议的 proposal。这种 profile（强问题 + 强实验 + 中 novelty）在顶会评审中典型地落在 borderline 区域。

**异常处理**：R1 的离散化伪影担忧、R2 的"so what"问题、R2 的 kappa 引用均为单人提出。R2 的"so what"问题实际上有一定权重——如果分类结果本身不直接 actionable，论文的 impact 会进一步受限——但因另两位未将此列为风险，降权处理。

**最终调整**：鉴于三方完全一致且本系统遵循"宁缺毋滥"原则，最终中位从 35% 微调至 34%（收窄上界至 40%，保留下界 28%）。理由：(1) 三份评审虽独立但可能共享了部分 calibration bias（如对"analysis paper"类型的固有偏好），需要小幅保守修正；(2) R2 提出的"actionable insight 缺失"问题虽为单人异常，但确实点出了一个 impact 维度的隐性风险——"我们能分类 faithfulness 现象，然后呢？"这个问题如果论文没有给出有力回答，会让 accept 更难。

**概率天花板分析**：方法与创新维度 3/3 判"中"，这意味着 idea 质量的天花板约在 40-42%。即使实验执行完美（实验设计已被判"强"），概率也很难突破 42%。当前 34% 中位反映了在这个天花板下，考虑到不可通约性风险和"trivial combination"质疑的合理扣减。

【建议】: 边缘（borderline — 方向正确、实验出色，但核心 novelty 有限且存在方法论争议；值得尝试但需要 Phase 0b 结果和"不做 gap"消融的强力支撑才有希望突破 accept 线）

【实施评估】:
- **计算资源**: ~1050 H100-hours（约 $3,200），学术实验室可承受。NLDD 32B 是单项最大开销（250 hrs，受 Phase 0a 门控）。需稳定 GPU 集群，无需特殊硬件。
- **数据需求**: 全部使用公开 benchmark（GSM8K, MATH-500, GPQA-Diamond, AIME），无需新数据收集。FaithCoT-Bench (ICLR 2026) 的 instance-level labels 获取性需确认（三位审稿人均提及）。存储 3-5 TB（hidden states，fp16），PCA 压缩可降至 ~1.5 TB。
- **人工介入**: 极低。框架全流程自动化，主要人工投入在实验设计决策（Phase 0b go/no-go 判断）和论文写作。Paraphrase 生成由 API 完成（Claude Haiku/GPT-4o-mini，$800-1500）。
- **训练需求**: 轻量级——仅训练 linear probes 和浅层分类器（LR/RF/MLP），不涉及 LLM fine-tuning。所有目标模型使用现有开源权重。
- **新 Benchmark**: 不需要。TIF Score 是新诊断指标但不构成独立 benchmark。
- **预估周期**: 15-17 周（2 researchers）/ 12-14 周（1 researcher + AI 辅助）。Phase 0b 在第 4 周提供 go/no-go 关键信号。时间线紧凑但可行，主要风险在 NLDD feasibility 和 Phase 0b 效果量。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1a3525c-5758-400c-8fce-305158c4a888",
  "isSidechain": false,
  "requestId": "req_011CbDD2jiyKLQbPsbC2K8Sy",
  "type": "assistant",
  "uuid": "4f751224-4ce7-4cc6-9a5b-6ad02b4a4a20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQChK2j7F858qkMupcQfu7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26505,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3524,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26505,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3524,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 26505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26505
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a thorough assessment.…",
  "leafUuid": "4f751224-4ce7-4cc6-9a5b-6ad02b4a4a20",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate dual-stream CoT faithfulness diagnostic framework",
  "sessionId": "18a4437d-51db-4c71-9343-a08b73d5c23e"
}
```

---
