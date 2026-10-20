# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/7d5ddf17-2274-4765-8596-7cfca4aa1617.jsonl`
- **Structured JSON:** [`72424e75fab67774a93e.json`](../../sessions/72/72424e75fab67774a93e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:02:36.635Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:02:36.635Z",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have enough information to make a thorough assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【致命前置问题 — 投稿venue不匹配】:\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：\n\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n\"Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 是一篇纯粹的 LLM chain-of-thought faithfulness 诊断与度量论文，研究的是语言模型的内部表征与 CoT 因果贡献之间的偏差。全文没有任何与机器人学习相关的内容——没有机器人任务、没有具身智能、没有 sim-to-real、没有 manipulation/navigation/locomotion。\n\n⚠️ 这篇论文投 CoRL 会被 desk reject（不经评审直接退回）。合适的 venue 应该是 NeurIPS、ICML、ICLR、ACL/EMNLP 等。\n\n以下评估假设投稿目标更正为合适的 ML/NLP 顶会（如 NeurIPS 2026 或 ICLR 2027），纯粹评估 idea 质量。\n\n---\n\n【领域调研】:\n\n1. [Chrabąszcz et al., \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\"](https://arxiv.org/abs/2605.18549) (arXiv 2025.05): 对 LRM 构建 probe trajectory，在每个生成 token 处评估 probe，提取 60+ 信号处理特征（波动性、趋势、稳态），max-pooling 达 95% AUROC。证明动态 probe 轨迹比静态单点 probe 更有效。**与本 proposal 的 P*(t) 方向高度重叠，是最直接竞争者。**\n\n2. [Wang, \"LLM Reasoning Is Latent, Not the Chain of Thought\"](https://arxiv.org/abs/2604.15726) (arXiv 2026.04): 形式化三个假设 H1（推理由 latent state 主导）、H2（推理由显式 CoT 主导）、H0（通用串行计算）。本 proposal 直接采用 H1/H2 框架，但 Wang 的工作已经提供了概念基础。\n\n3. [Cox et al., \"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\"](https://arxiv.org/abs/2603.01437) (arXiv 2026.03): 在 CoT 前最后一个 token 训练 linear probe 达 0.9 AUC；**activation steering 沿 probe 方向可在 >50% 情况下翻转答案**。这与 proposal 声称的 \"Cox et al.: negligible flip rates\" 存在潜在矛盾（详见前提假设检验）。\n\n4. [Gjølbye et al., \"Reasoning Models Don't Just Think Longer, They Move Differently\"](https://arxiv.org/abs/2605.15454) (arXiv 2025.05): 证明 difficulty-geometry coupling 在 residualize on length 后仍然存在，但具有领域特异性（代码领域 ρ⊥ = +0.41 强，数学领域较弱）。本 proposal 的 difficulty conditioning 部分直接建立在此工作之上。\n\n5. [\"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\"](https://arxiv.org/abs/2602.11201) (arXiv 2026.02): 提出 NLDD 度量，量化 step-level faithfulness；发现 DeepSeek 依赖 CoT 而 Gemma 在 CoT 被破坏后准确率反而提升。本 proposal 直接使用 NLDD 作为 C(t) 的三种估计方法之一。\n\n6. [\"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures\"](https://arxiv.org/abs/2603.16475) (arXiv 2026.03): 使用参数化方法（activation/attribution patching, causal tracing, propositional probes）和 trace perturbation protocols 评估 faithfulness。方法论上与本 proposal 的 causal contribution 估计有大量重叠。\n\n7. [\"Chain-of-Thought Is Not Explainability\"](https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf) (Barez et al.): 系统论证 CoT 不等于可解释性，为 faithfulness 研究提供概念基础。\n\n- **调研总结**: CoT faithfulness 是 2025-2026 年的热门研究方向，已有大量工作从 probing、causal intervention、trajectory analysis、mechanistic analysis 等角度展开。本 proposal 的核心贡献是将 probe trajectory（P*）与 causal contribution（C）的 gap 形式化为一个统一度量。但各个组件（probe trajectory、causal intervention、NLDD、difficulty conditioning）都已在近期独立工作中被提出。该领域的研究密度极高，novelty 空间被显著压缩。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在明显的更简单替代方案。**\n\n1. **直接逐步比较 probe accuracy vs. truncation effect**：不需要形式化 G*(t) = P*(t) − C(t) 这个框架，研究者可以直接在每个 CoT step 处 (a) 测 probe 对最终答案的预测准确率，(b) 在该步截断后测准确率变化，然后画出两条曲线。这本质上就是 proposal 在做的事，但不需要 null-probe calibration、MCT geometric validation、现象分类法等复杂机制。\n\n2. **Chrabąszcz et al. 的 probe trajectory + 简单 ablation**：已有的 probe trajectory 工作已经能追踪模型内部状态随时间的变化，加上标准的 CoT truncation/perturbation 实验就能得到类似的 insight，不需要 ICG 框架。\n\n3. **增量价值在哪？** Proposal 声称增量价值在于\"calibrated gap metric\"和\"phenomenon taxonomy\"。但 calibration 是技术细节而非概念突破；phenomenon taxonomy（pre-CoT encoding, genuine reasoning, post-hoc rationalization）是已知概念的重新标签化，这些现象已被 Cox et al., Boppana et al. 等分别研究过。\n\n---\n\n【前提假设检验】:\n\n**核心 claim 的逻辑链条中存在至少两个重大未验证假设：**\n\n1. **\"causal interventions based on probes consistently fail on reasoning-trained models\" — 可能与引用文献矛盾**\n   - Proposal 声称 \"Cox et al.: negligible flip rates\"，但我找到的 Cox et al. (2603.01437) 实际报告 \"steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines\"。\n   - 如果 Cox 的 activation steering 确实在 >50% 的情况下有效，那么 proposal 的整个前提——\"probes diagnose but causal interventions fail, therefore the gap IS the faithfulness signal\"——就失去了经验基础。\n   - 可能 proposal 指的是另一篇 Cox 的论文、或者特指 reasoning-trained models（而非 instruction-tuned models），但这一关键区分在 proposal 中未充分阐明。**这是一个潜在致命的前提错误。**\n\n2. **\"G*(t) 的不同 pattern 能区分不同 faithfulness 现象\" — 纯属假设**\n   - Proposal 承认需要 Phase 0b 来验证\"至少 2 个现象产生可区分的轨迹（effect size d > 0.5）\"。这意味着核心 claim 目前完全未经验证。\n   - 不同现象（pre-CoT encoding vs. genuine reasoning vs. post-hoc rationalization）可能在 G*(t) 空间中产生高度重叠的分布，导致分类不可行。\n   - Proposal 的 semi-synthetic simulation 被自己降级为\"hypothesis generation\"而非\"evidence\"，说明作者也认识到这个风险。\n\n3. **\"P*(t) − C(t) 是有意义的减法\" — 数学假设未论证**\n   - P*(t) 是 probe 校准后的概率，C(t) 是因果贡献（通过 truncation/perturbation/NLDD 估计）。这两个量的量纲、尺度、噪声特征可能完全不同，直接相减是否有统计学意义？Proposal 未讨论。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱**\n   - 核心概念\"比较 probing 准确率与 causal contribution 的差异\"是一个自然的组合想法，而非突破性洞见。\n   - P*(t) 方向被 Chrabąszcz et al. (2605.18549) 的 probe trajectory 工作大量覆盖。\n   - C(t) 的三种估计方法（truncation, perturbation, NLDD）都是已有文献中的标准方法。\n   - Wang (2604.15726) 已经形式化了 H1/H2 框架，本 proposal 只是用 G*(t) 来操作化它。\n   - Difficulty conditioning 直接建立在 Gjølbye et al. (2605.15454) 之上。\n   - **在剔除 surface differences 后，真正的 novelty delta 很小**：主要是\"把已有组件拼在一起并定义了一个 gap metric\"。这在高竞争领域中不足以构成强 novelty。\n\n2. **Significance: 中**\n   - CoT faithfulness 是 AI safety 和 interpretability 的核心问题，研究问题本身是重要的。\n   - 但\"度量框架\"论文的影响力取决于该框架是否被社区采用。ICG 框架的复杂度（null-probe calibration、MCT geometric validation、多种 C(t) 估计方法、difficulty conditioning、length correction）可能阻碍其可用性和可复现性。\n   - 即使 G*(t) 曲线能区分不同现象，\"so what\"问题没有很好地回答——知道某个实例是 pre-CoT encoding 还是 post-hoc rationalization 之后，下一步做什么？缺乏 actionable implication。\n   - 如果核心发现是 positive（即 G*(t) 确实能区分现象），审稿人可能会说 \"interesting measurement, but I would have guessed that these phenomena produce different probe/causal patterns\" — 这不是 surprising 的发现。\n\n3. **Related Work: 中**\n   - Proposal 确实覆盖了多个关键近期工作（Chrabąszcz, Wang, Gjølbye, NLDD 等），定位也算清晰。\n   - 但对 Cox et al. 的引用存在潜在事实错误（将 >50% flip rate 描述为 \"negligible flip rates\"），这会严重损害 credibility。\n   - 缺少对 \"Breaking the Chain\" (2603.16475)、FaithCoT-Bench (2510.04040) 等直接相关工作的讨论。\n   - \"Ballon et al.\" 的 truncation control conditions 未能在搜索中验证，可能存在引用准确性问题。\n\n---\n\n【概率估计】: [10% - 20%] 中位 12%\n\n【估计理由】:\n1. **如果投 CoRL：~0%**。会被 desk reject，完全不在 scope 内。\n2. **如果投合适 venue（NeurIPS/ICLR/ICML）**：中位约 12%。Novelty 弱是主要限制因素——这是一个将已有组件（probe trajectory + causal intervention + H1/H2 框架）组合成新 metric 的 framework 论文，在一个研究密度极高的领域中，这种\"组合 + 形式化\"的贡献很难说服审稿人有足够的 novelty delta。核心前提（causal intervention fails on reasoning models）可能与引用文献矛盾，这进一步压低了评估。Significance 中等但缺乏 actionable implication，且核心发现若 positive 不够 surprising。\n3. 上界被 Novelty 维度严格限制：即使实验做得完美，idea 本身的增量贡献空间有限。\n4. 下界被前提假设的潜在错误拉低：如果 Cox et al. 的引用确实是误读，审稿人会直接质疑整个 motivation。\n\n【主要风险】:\n1. **核心前提可能不成立**：Proposal 的整个动机建立在\"probes diagnose but causal interventions fail\"的 empirical finding 上，但 Cox et al. (2603.01437) 实际报告 >50% 的 flip rate，与 proposal 声称的 \"negligible flip rates\" 矛盾。如果这个前提被审稿人推翻，整篇论文的 motivation 就塌了。\n2. **Novelty 被近期工作严重压缩**：Chrabąszcz et al. 已做 probe trajectory，Wang 已形式化 H1/H2，NLDD 已有，difficulty conditioning 建立在 Gjølbye 之上——剩余的 novelty 主要是\"定义了一个 gap metric\"，这在顶会审稿中可能被认为是 incremental combination。\n```\n\n---\n\n**补充说明：venue 问题**\n\n这是一个需要立即纠正的问题。CoRL 2026 的 Call for Papers 明确要求 \"submissions should focus on a core robotics problem\"，且 \"submissions without a robotics focus will be returned without review\"。本 proposal 是纯 NLP/interpretability 研究，与机器人学习完全无关。建议将目标 venue 更换为 NeurIPS 2026、ICLR 2027、ACL/EMNLP 2026 等。上述概率估计已基于合适 venue 给出；若坚持投 CoRL，中稿概率为 **0%**。\n\nSources:\n- [Chrabąszcz et al., \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\"](https://arxiv.org/abs/2605.18549)\n- [Wang, \"LLM Reasoning Is Latent, Not the Chain of Thought\"](https://arxiv.org/abs/2604.15726)\n- [Cox et al., \"Decoding Answers Before Chain-of-Thought\"](https://arxiv.org/abs/2603.01437)\n- [Gjølbye et al., \"Reasoning Models Don't Just Think Longer, They Move Differently\"](https://arxiv.org/abs/2605.15454)\n- [\"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\"](https://arxiv.org/abs/2602.11201)\n- [\"Breaking the Chain: A Causal Analysis of LLM Faithfulness\"](https://arxiv.org/abs/2603.16475)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide my assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【致命前置问题：投稿venue与论文主题严重不匹配】\n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求：\n- \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n- \"Submissions without a robotics focus will be returned without review.\"\n- 议题范围：imitation learning, RL for robots, sim-to-real, robot perception, manipulation, locomotion, learning-based planning 等。\n\n本 proposal 是一篇纯粹的 NLP/LLM 可解释性论文（chain-of-thought faithfulness measurement），与机器人学没有任何关联。提交至 CoRL 将大概率被 desk reject（退回不审）。\n\n这是一个致命的 venue mismatch。以下评估仍按 idea 内在质量给出（假设投稿至合适的 venue 如 NeurIPS / ICML / ACL / EMNLP），但 CoRL 的中稿概率需单独标注。\n\n---\n\n【领域调研】:\n\n1. **Chrabąszcz et al., \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (arXiv 2605.18549, May 2026)**:\n   最直接的竞争工作。在 4 个推理模型上构建 probe trajectory（每个 token 处评估 probe），使用 60+ 信号处理特征，max-pooling 达到 95% AUROC，比静态 probe 提升 17pp。该工作已经验证了\"probe trajectory\"方向的有效性，且已有完整的实验支撑。本 proposal 的 P*(t) 维度本质上是该工作的变体/延伸。\n\n2. **Cox et al., \"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\" (arXiv 2603.01437, March 2026)**:\n   在 instruction-tuned 模型上证明 pre-CoT 阶段 probe 可以 >0.9 AUC 预测最终答案，且 steering 可以在 >50% cases 翻转答案。但明确指出在 reasoning-trained 模型上 causal intervention 效果减弱。proposal 引用此工作的\"negligible flip rates\"作为核心立论依据——但 Cox 的原文是在 instruction-tuned 模型上做的，对 reasoning models 的结果是 limitation 而非主发现，proposal 对此引用可能存在不准确。\n\n3. **Wang, \"LLM Reasoning Is Latent, Not the Chain of Thought\" (arXiv 2604.15726, April 2026)**:\n   形式化 H0/H1/H2 三个假说（H1: latent-state mediated; H2: CoT-mediated; H0: generic serial compute）。这是一篇 position paper，提供概念框架而非实证。proposal 声称 operationalize 其 H1/H2 distinction，但 Wang 的框架还包含 H0（generic compute hypothesis），proposal 似乎忽略了这一可能性。\n\n4. **Gjølbye et al., \"Reasoning Models Don't Just Think Longer, They Move Differently\" (arXiv 2605.15454, May 2026)**:\n   在 hidden-state trajectories 上发现 difficulty-geometry coupling（Codeforces 上 ρ⊥ = +0.41），但在 MATH 和 Boolean SAT 上显著更弱。proposal 引用此工作支撑 task-difficulty conditioning，但 Gjølbye 自身结论是 domain-specific 且效果有限。\n\n5. **\"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\" (arXiv 2602.11201, ICLR 2026 Workshop)**:\n   提出 NLDD 指标，发现 Reasoning Horizon (k*) 在 70-85% chain length 处，之后 reasoning tokens 无正面贡献。proposal 直接将 NLDD 作为其 C(t) 的三种估计方法之一。\n\n6. **\"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures\" (arXiv 2603.16475)**:\n   Front-door causal framework 评估模型对中间结构的 faithfulness，发现 >60% consistency under prompt interventions 但 >50% failure on structural edits。\n\n7. **\"FaithCoT-Bench\" (arXiv 2510.04040) / \"C2-Faith\" (arXiv 2603.05167)**:\n   CoT faithfulness 的 benchmark 化尝试，提供标准化评估。\n\n- **调研总结**: CoT faithfulness 是一个 2025-2026 年的研究热点，已有大量工作从不同角度切入（probe trajectories、causal perturbation、step-level metrics、benchmark 构建）。本 proposal 的核心思路——将 probe-based 诊断和 causal contribution 组合为一个\"gap metric\"——是对现有独立组件的**框架性整合**，而非方法论层面的根本创新。最直接竞争者 Chrabąszcz et al. 已发表且覆盖了 probe trajectory 维度；causal contribution 的三种方法（prefix truncation, paraphrase, NLDD）均为已有技术。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁。**\n\n1. **最简单的替代方案**：直接在现有 probe trajectory 工作（Chrabąszcz et al.）上加一列 per-step NLDD 或 prefix-truncation score，然后做相关性分析。这不需要整个 ICG 框架，不需要 null-probe calibration，不需要 MCT geometric validation，就能回答\"probe 知道的 vs CoT 贡献的 是否有 gap\"这个问题。\n\n2. **增量价值在哪？** proposal 声称的增量是：(a) 将 gap 形式化为时间序列 G*(t)；(b) null-probe calibration；(c) phenomenon taxonomy。但 (a) 本质上是 visualization/framing 层面的贡献而非方法论创新；(b) 是技术细节层面的 robustness check；(c) 的分类目标（pre-CoT encoding vs genuine reasoning vs post-hoc rationalization）在 Cox et al. 和其他工作中已被作为分析维度使用。\n\n3. **核心问题**：如果你给 Chrabąszcz 的 probe trajectories 加上一个 causal contribution 估计并做减法，和这个 proposal 的核心 output 有什么本质区别？proposal 没有清楚回答这个问题。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有多个未经验证的假设：\n\n1. **\"P*(t) − C(t) 是有意义的减法\"（最关键的假设）**: P*(t) 是 probe 在隐藏状态上的 correctness prediction probability，C(t) 是 causal contribution（来自 prefix truncation / paraphrase / NLDD）。这两个量的量纲、尺度、含义完全不同——一个是\"模型内部是否已经'知道'答案\"，另一个是\"CoT 文本对最终答案的 causal effect\"。将它们直接相减产生 G*(t) 在数学上缺乏严格 justification。这就像用温度减去风速——两个都能告诉你天气信息，但减法本身没有物理意义。\n\n2. **\"不同 faithfulness phenomena 会产生可区分的 G*(t) temporal fingerprints\"**: 这是整个框架的核心赌注。proposal 自己也承认这需要 Phase 0b 来验证（effect size d > 0.5），但这同时意味着：如果验证失败，整个 framework 就没有意义。这不是一个已经有理论预期支撑的假设——它是一个纯经验赌注。\n\n3. **\"diagnostic-causal gap 是一个稳定的、可推广的现象\"**: proposal 的立论基于\"probes 能诊断但 causal intervention 失败\"这一观察。但 Cox et al. 的实验主要在 instruction-tuned 模型上（steering 成功率 >50%！），在 reasoning models 上的结果作为 limitation 而非主发现报告。这个 gap 的 robustness 在 reasoning-trained models 上是否真的如 proposal 所声称的那样\"robust\"，尚缺乏跨模型的系统性验证。\n\n4. **忽略 Wang 的 H0**: proposal 将 G*(t) >> 0 映射到 H1，G*(t) ≈ 0 映射到 H2，但完全没有处理 H0（generic serial compute）。如果真正的机制是 H0——模型只是通过更多 compute 步骤获益，而非通过任何\"推理\"——那么 G*(t) 的解读就完全不同。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱**\n   - 核心贡献是\"框架性整合\"而非方法论创新。P*(t) 方向已被 Chrabąszcz et al. (2605.18549) 充分覆盖；C(t) 的三种方法（prefix truncation, paraphrase perturbation, NLDD）全部是已有技术；Wang (2604.15726) 的 H1/H2 概念框架也已存在。\n   - proposal 的真正 novelty delta 是 G*(t) = P*(t) − C(t) 这个\"gap metric\"，但正如前提假设检验所指出的，这个减法在数学上缺乏 justification。\n   - 与 Chrabąszcz et al. 的差异化定位不够有力：proposal 声称\"adds the entire causal contribution dimension\"，但 causal perturbation 方法是 CoT faithfulness 领域的标准工具（prefix truncation 在 Lanham et al. 2023 就已使用），将它和 probe trajectory 放在一起并不产生 1+1>2 的 insight。\n\n2. **Significance: 中**\n   - CoT faithfulness 本身是重要问题，关系到 LLM 的可信度和安全性。\n   - 但该 proposal 的实际影响力受限于：(a) 框架的可操作性存疑（G*(t) 的减法含义不清），(b) phenomenon taxonomy 的实用价值取决于是否真的能区分不同现象（Phase 0b 是赌注），(c) 如果核心发现是 positive（不同现象确实有不同的 temporal fingerprint），审稿人的反应更可能是\"makes sense, I would have guessed this\"而非\"surprising\"——pre-CoT encoding 应该 P*(0) 高 C(0) 低，genuine reasoning 应该两者都增长，这些都是符合直觉的预测。\n   - 对于 CoRL 而言：significance = 0（与机器人学完全无关）。\n\n3. **Related Work: 中**\n   - proposal 对近期工作有较好的覆盖（Chrabąszcz, Wang, Gjølbye, Cox 等），positioning 也有意识地在做。\n   - 但存在引用不准确的风险：对 Cox et al. 的引用可能过度推断了 reasoning models 上的结果（原文主要是 instruction-tuned 模型）；对 Yuan et al. \"all four intervention strategies fail\" 的引用我未能在搜索中验证到一篇完全匹配的论文。\n   - 缺少对 \"Breaking the Chain\" (2603.16475, front-door causal analysis) 和 FaithCoT-Bench (2510.04040) 等 benchmark 工作的讨论，这些是直接相关的竞争方向。\n\n---\n\n【概率估计】:\n\n**针对 CoRL 2026**: 0-2%，中位 1%\n- 理由：致命的 venue mismatch。CoRL 明确声明\"Submissions without a robotics focus will be returned without review\"。本 proposal 是纯 NLP/interpretability 论文，将被 desk reject。\n\n**假设投稿至合适 venue（NeurIPS / ICML / ACL 主会）**: 12-22%，中位 16%\n\n【估计理由】:\n- Novelty 弱是上界的主要限制因素。核心贡献是已有技术的框架性组合（probe trajectory + causal perturbation + gap metric），缺乏方法论层面的真正创新。\n- G*(t) 的数学 justification 薄弱（两个不同量纲量的减法）会成为审稿人攻击的首要目标。\n- 如果 Phase 0b 验证成功，核心发现（不同现象有不同的 temporal signature）的 surprise value 有限——预测方向符合直觉。\n- 积极面：proposal 的实验设计相对完善（有 Phase 0b 验证、honest scoping、compute budget 估计），如果执行得好可以产出一篇 solid 的 empirical paper。但 idea 内核的 novelty 瓶颈限制了上界。\n- 在 CoRL venue 下，这些都不重要——直接 desk reject。\n\n【主要风险】:\n1. **致命 venue mismatch**：CoRL 是机器人学习会议，本论文与机器人学零关联，将被 desk reject。\n2. **核心 metric G*(t) 的数学合理性**：P*(t) 和 C(t) 量纲不同，减法缺乏理论 justification。即使在合适 venue，这也是审稿人最可能质疑的点，可能被要求根本性重构 framework。\n```\n\n---\n\n**总结**：这个 proposal 有两层问题。**第一层是致命的**：CoRL 是 Conference on Robot Learning，明确要求 submissions 必须 focus on a core robotics problem，否则直接 desk reject。本 proposal 是一篇纯粹的 LLM 可解释性/CoT faithfulness 论文，与机器人学没有任何关系。**即使 idea 本身质量极高，在 CoRL 的中稿概率也趋近于 0。** 第二层是 idea 质量本身：即使投稿至合适 venue（NeurIPS/ICML/ACL），核心 novelty 也偏弱——本质上是将已有组件（probe trajectories、causal perturbation methods、H1/H2 框架）进行框架性整合，而非方法论创新，且核心 gap metric G*(t) 的数学 justification 不足。\n\n**强烈建议**：首先更换投稿 venue（考虑 NeurIPS 2026、ICML 2026、ACL/EMNLP 2025 等 NLP/ML venue），然后再进入迭代优化流程。\n\nSources:\n- [Chrabąszcz et al., Probe Trajectories](https://arxiv.org/abs/2605.18549)\n- [Cox et al., Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)\n- [Wang, LLM Reasoning Is Latent](https://arxiv.org/abs/2604.15726)\n- [Gjølbye et al., Reasoning Models Move Differently](https://arxiv.org/abs/2605.15454)\n- [NLDD / Faithfulness Decay](https://arxiv.org/abs/2602.11201)\n- [Breaking the Chain: Causal Analysis](https://arxiv.org/html/2603.16475v1)\n- [FaithCoT-Bench](https://arxiv.org/html/2510.04040v1)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Chrabąszcz et al., \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (arXiv:2605.18549)](https://arxiv.org/abs/2605.18549) (2026): 最直接的竞争工作。已经在 4 个推理模型上做了 probe trajectory + 60+ 信号处理特征，达到比 static probe 高 17pp 的性能。Proposal 的 P*(t) 方向被此工作高度验证但也高度重叠。\n- [Wang, \"LLM Reasoning Is Latent, Not the Chain of Thought\" (arXiv:2604.15726)](https://arxiv.org/abs/2604.15726) (2026): 已经形式化了 H1(latent-mediated) / H2(CoT-mediated) / H0(generic compute) 三假设框架。Proposal 声称 operationalize 此区分，但框架本身来自此文。\n- [Gjølbye et al., \"Reasoning Models Don't Just Think Longer, They Move Differently\" (arXiv:2605.15454)](https://arxiv.org/abs/2605.15454) (2026): 已经做了 difficulty-geometry coupling 分析，发现 ρ⊥ = +0.41 (Codeforces) 且 domain-specific。Proposal 的 task-difficulty conditioning 直接复用此发现。\n- [\"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\" (arXiv:2602.11201)](https://arxiv.org/abs/2602.11201) (ICLR 2026 Workshop): NLDD 指标已存在，已发现 Reasoning Horizon (70-85% chain length)。Proposal 将 NLDD 作为三种因果贡献估计方法之一直接使用。\n- [\"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\" (arXiv:2504.05419)](https://arxiv.org/abs/2504.05419) (2025): 已证明推理模型隐藏状态编码正确性信息但未能利用，probe AUROC 高但介入效果差。Proposal 的核心前提观察来自此类工作。\n- [\"Breaking the Chain: A Causal Analysis of LLM Faithfulness\" (arXiv:2603.16475)](https://arxiv.org/abs/2603.16475) (2026): 系统性因果分析 CoT 对中间结构的忠实度，发现模型对自生成结构比 gold 结构更忠实。\n- [\"Decoding Answers Before Chain-of-Thought\" (arXiv:2603.01437)](https://arxiv.org/abs/2603.01437) (2026): Pre-CoT probes + activation steering，已经在探测 CoT 前答案编码。\n\n- **调研总结**: CoT faithfulness 是 2025-2026 年 NLP 解释性领域的热点方向，已有大量工作分别从 probe trajectory、因果介入、NLDD 指标、difficulty conditioning 等角度展开。该 proposal 的各个组件（probe trajectory, 因果贡献估计, difficulty conditioning）均已有独立的近期论文覆盖；其核心主张的 novelty 在于将这些组件组合为一个统一的 \"gap metric\" 框架。\n\n【Trivial Alternative 检验】:\n**存在显著的 trivial alternative 威胁。** \nProposal 的核心度量 G*(t) = P*(t) − C(t) 本质上是将两个已有的度量（probe correctness prediction 和 causal contribution estimation）相减。一个研究者已经可以：(1) 用 Chrabąszcz 等人的 probe trajectory 方法跟踪内部状态演变；(2) 用 NLDD 或 prefix truncation 单独评估因果贡献；(3) 直接对比两个信号在时间轴上的行为。这不需要一个新的\"框架\"——分别 plot 两条曲线并目视/统计比较，就能得到 proposal 声称的 \"divergence fingerprint\"。将两个已有信号相减并命名为 \"ICG\" 的增量价值有限。真正的增量在于：是否存在 calibration 方法使得 P*(t) 和 C(t) 在同一度量空间中可减，以及减出来的 gap 是否比单独看两个信号提供了**不可通过其他方式获得**的洞见。Proposal 未能令人信服地论证后者。\n\n【前提假设检验】:\n核心 claim 的逻辑链有多个未经验证的环节：\n1. **P*(t) 和 C(t) 在同一标尺上可相减**：probe 输出的概率和因果贡献（truncation accuracy drop / NLDD score / paraphrase sensitivity）是完全不同性质的量。\"null-probe calibration\" 是否真的能让它们 commensurable 是一个未经实证的假设。\n2. **Gap 的 temporal shape 能区分 faithfulness phenomena**：proposal 假设 pre-CoT encoding、genuine reasoning、post-hoc rationalization 会产生可区分的 G*(t) 形状，但这完全是 hypothetical——没有任何先验理论或实证表明这些现象的 gap curve 形状会有 d > 0.5 的效应量。\n3. **跨研究数字的可组合性**：proposal 大量引用不同研究的数字（Cox 的 AUROC, David 的 easy/hard split, Gjølbye 的 ρ⊥）作为框架设计依据，但这些数字来自不同模型、不同任务、不同设置，组合起来的有效性存疑。虽然 proposal 加入了 Phase 0b pilot 来验证，这说明作者意识到了这个问题，但也说明核心 claim 目前缺乏实证基础。\n\n【3 维度打分】:\n\n1. **Novelty: 弱** — Proposal 的每个组件都直接来自近期已发表工作：probe trajectory (Chrabąszcz 2605.18549)、NLDD (arXiv:2602.11201)、H1/H2 框架 (Wang 2604.15726)、difficulty-geometry coupling (Gjølbye 2605.15454)、prefix truncation 因果分析 (Ballon et al.)。\"将 probe 信号与因果贡献信号相减得到 gap\" 是一个 natural next step，而非 surprising insight。核心 novelty claim 是 \"gap metric + calibration + temporal fingerprint → faithfulness taxonomy\"，但这更像是一个工程性的组装，而非概念性的突破。如果最终结果是 positive（gap curve 确实能区分 phenomena），审稿人更可能说 \"makes sense, I would have expected this to work\" 而非 \"surprising\"。\n\n2. **Significance: 中** — CoT faithfulness 确实是重要问题，了解模型\"知道但不使用\"的信息有实际价值。但此 proposal 本质上是一个**诊断/测量框架**，不改进模型、不提供 actionable 的训练信号、不直接解决安全问题。其价值取决于 taxonomy 的实用性——如果最终只能区分 2-3 种现象且无法指导下游干预，影响力有限。此外，830 H100-hours 的计算成本相对于一个诊断工具来说偏高。\n\n3. **Related Work: 中** — Proposal 引用的关键论文（Chrabąszcz 2605.18549, Wang 2604.15726, Gjølbye 2605.15454, NLDD 2602.11201）经验证均真实存在且描述基本准确。差异化定位（\"我们加了 causal contribution 维度\"）也有合理性。但 proposal 对最直接竞争者的差异化论证不够有力——Chrabąszcz 已经用 probe trajectory 做到了很多，加上 causal contribution 维度的**边际价值**没有被清晰论证。同时，对 \"Breaking the Chain\" (2603.16475) 和 \"Decoding Answers Before Chain-of-Thought\" (2603.01437) 等高度相关工作的讨论不足。\n\n【⚠️ 致命问题：venue mismatch】:\n**CoRL (Conference on Robot Learning) 2026 明确要求所有投稿必须聚焦于机器人学习核心问题（\"submissions without a robotics focus will be returned without review\"）。本 proposal 是纯 NLP/AI 可解释性工作（CoT faithfulness 诊断框架），不涉及任何机器人、物理交互、控制、感知或 embodied AI 内容。按照 CoRL 的 scope 政策，本文将在 desk review 阶段被直接退回（desk reject），不会进入同行评审。**\n\n这不是 idea 质量问题，而是投稿目标会议与论文内容的根本性错配。该 proposal 的合适 venue 应为 NeurIPS / ICML / ACL / EMNLP 等 NLP/ML 主会，或 ICLR。\n\n【概率估计】: [0% - 3%] 中位 1%\n\n【估计理由】: \n即使完全不考虑 venue mismatch（假设投到合适的 NLP/ML venue），基于 idea 质量的估计约为 [15% - 25%] 中位 20%——idea 方向站得住脚但内核薄弱，各组件来自已有工作的组装，核心 gap metric 存在 trivial alternative 威胁，前提假设（P* 和 C 可减、gap shape 可区分现象）未经验证。Novelty 弱是限制上界的主要维度。\n\n但考虑到投稿目标是 **CoRL 2026**（Conference on Robot Learning），该 proposal 将几乎确定被 desk reject。因此实际概率接近 0%。\n\n【主要风险】:\n1. **致命 venue mismatch**: CoRL 要求 robotics focus，本文是纯 NLP 可解释性工作，将被 desk reject\n2. **Novelty 不足**: 核心贡献是组合已有工具（probe trajectory + 因果贡献估计 + gap metric），缺乏概念性突破，审稿人可能认为是 \"engineering contribution\" 而非 \"scientific insight\"\n```\n\n---\n\n**总结**：这个 proposal 存在一个**致命的 venue 错配问题**。CoRL 是 Conference on Robot Learning，明确要求论文聚焦机器人学习，non-robotics 投稿会被直接退回。本 proposal 是纯粹的 NLP/AI 可解释性研究（CoT faithfulness 诊断框架），与机器人学习没有任何关联。\n\n即使抛开 venue 问题单看 idea 质量，novelty 也偏弱——各组件（probe trajectory, NLDD, difficulty conditioning, H1/H2 框架）均来自 2025-2026 年的已发表工作，核心创新在于将它们组合为一个 gap metric，但这个组合是 natural next step 而非 surprising insight。\n\n**建议：如果要推进此 proposal，应将目标 venue 改为 NeurIPS / ICML / ACL / EMNLP 等 NLP/ML 主会，并需在 novelty 层面做实质性加强——比如证明 gap metric 能提供单独看 probe 或单独看 causal contribution 所无法获得的独特洞见。**\n\nSources:\n- [Chrabąszcz et al., \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\"](https://arxiv.org/abs/2605.18549)\n- [Wang, \"LLM Reasoning Is Latent, Not the Chain of Thought\"](https://arxiv.org/abs/2604.15726)\n- [Gjølbye et al., \"Reasoning Models Don't Just Think Longer, They Move Differently\"](https://arxiv.org/abs/2605.15454)\n- [\"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\"](https://arxiv.org/abs/2602.11201)\n- [\"Reasoning Models Know When They're Right\"](https://arxiv.org/abs/2504.05419)\n- [\"Breaking the Chain: A Causal Analysis of LLM Faithfulness\"](https://arxiv.org/abs/2603.16475)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWe propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.\n\nThe framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness (explicitly targeting right/wrong prediction — justified over answer-content probes by broader applicability beyond binary tasks, grounding in the diagnostic-not-causal finding which is about correctness, and more direct faithfulness interpretation — with supplementary answer-content analysis on binary/MC subsets), and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions validating sequential content matters, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\nPositioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes across 4 reasoning models — our framework adds the entire causal contribution dimension, the calibrated gap metric, null-probe calibration with MCT geometric validation, phenomenon taxonomy, and task-difficulty conditioning. Their probe-trajectory methodology validates our P*(t) direction; we extend it to the dual-estimator gap that no existing framework provides.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) constructs real G*(t) curves from the SAME model and dataset and tests whether at least 2 phenomena produce distinguishable trajectories (effect size d > 0.5) before committing to the full classification pipeline — addressing the concern that semi-synthetic simulation from cross-study measurements overestimates real-data accuracy. The semi-synthetic simulation is retained as hypothesis generation producing testable predictions, not as evidence.\n\nTask-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits, the ICLR 2026 Workshop finding, and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific (weaker on MATH) — reveals the decorative→load-bearing transition with practical guidance on when chain-of-thought adds genuine value, applying length correction (residualizing on log(N)) to avoid generation-length confounds.\n\nThe paper focuses on four core contributions: (a) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. to demonstrate the value of the causal contribution dimension; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real data; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) probe-target analysis contrasting correctness vs. answer-content gaps. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs) as the primary bottleneck.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:02:36.637Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:02:36.637Z",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:02:36.649Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have enough information to make a thorough assessment. Let me compile my findings.

---

```
【阶段】: Triage

【致命前置问题 — 投稿venue不匹配】:
CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：
"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
"Submissions without a robotics focus will be returned without review."

本 proposal 是一篇纯粹的 LLM chain-of-thought faithfulness 诊断与度量论文，研究的是语言模型的内部表征与 CoT 因果贡献之间的偏差。全文没有任何与机器人学习相关的内容——没有机器人任务、没有具身智能、没有 sim-to-real、没有 manipulation/navigation/locomotion。

⚠️ 这篇论文投 CoRL 会被 desk reject（不经评审直接退回）。合适的 venue 应该是 NeurIPS、ICML、ICLR、ACL/EMNLP 等。

以下评估假设投稿目标更正为合适的 ML/NLP 顶会（如 NeurIPS 2026 或 ICLR 2027），纯粹评估 idea 质量。

---

【领域调研】:

1. [Chrabąszcz et al., "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"](https://arxiv.org/abs/2605.18549) (arXiv 2025.05): 对 LRM 构建 probe trajectory，在每个生成 token 处评估 probe，提取 60+ 信号处理特征（波动性、趋势、稳态），max-pooling 达 95% AUROC。证明动态 probe 轨迹比静态单点 probe 更有效。**与本 proposal 的 P*(t) 方向高度重叠，是最直接竞争者。**

2. [Wang, "LLM Reasoning Is Latent, Not the Chain of Thought"](https://arxiv.org/abs/2604.15726) (arXiv 2026.04): 形式化三个假设 H1（推理由 latent state 主导）、H2（推理由显式 CoT 主导）、H0（通用串行计算）。本 proposal 直接采用 H1/H2 框架，但 Wang 的工作已经提供了概念基础。

3. [Cox et al., "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering"](https://arxiv.org/abs/2603.01437) (arXiv 2026.03): 在 CoT 前最后一个 token 训练 linear probe 达 0.9 AUC；**activation steering 沿 probe 方向可在 >50% 情况下翻转答案**。这与 proposal 声称的 "Cox et al.: negligible flip rates" 存在潜在矛盾（详见前提假设检验）。

4. [Gjølbye et al., "Reasoning Models Don't Just Think Longer, They Move Differently"](https://arxiv.org/abs/2605.15454) (arXiv 2025.05): 证明 difficulty-geometry coupling 在 residualize on length 后仍然存在，但具有领域特异性（代码领域 ρ⊥ = +0.41 强，数学领域较弱）。本 proposal 的 difficulty conditioning 部分直接建立在此工作之上。

5. ["Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning"](https://arxiv.org/abs/2602.11201) (arXiv 2026.02): 提出 NLDD 度量，量化 step-level faithfulness；发现 DeepSeek 依赖 CoT 而 Gemma 在 CoT 被破坏后准确率反而提升。本 proposal 直接使用 NLDD 作为 C(t) 的三种估计方法之一。

6. ["Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures"](https://arxiv.org/abs/2603.16475) (arXiv 2026.03): 使用参数化方法（activation/attribution patching, causal tracing, propositional probes）和 trace perturbation protocols 评估 faithfulness。方法论上与本 proposal 的 causal contribution 估计有大量重叠。

7. ["Chain-of-Thought Is Not Explainability"](https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf) (Barez et al.): 系统论证 CoT 不等于可解释性，为 faithfulness 研究提供概念基础。

- **调研总结**: CoT faithfulness 是 2025-2026 年的热门研究方向，已有大量工作从 probing、causal intervention、trajectory analysis、mechanistic analysis 等角度展开。本 proposal 的核心贡献是将 probe trajectory（P*）与 causal contribution（C）的 gap 形式化为一个统一度量。但各个组件（probe trajectory、causal intervention、NLDD、difficulty conditioning）都已在近期独立工作中被提出。该领域的研究密度极高，novelty 空间被显著压缩。

---

【Trivial Alternative 检验】:

**存在明显的更简单替代方案。**

1. **直接逐步比较 probe accuracy vs. truncation effect**：不需要形式化 G*(t) = P*(t) − C(t) 这个框架，研究者可以直接在每个 CoT step 处 (a) 测 probe 对最终答案的预测准确率，(b) 在该步截断后测准确率变化，然后画出两条曲线。这本质上就是 proposal 在做的事，但不需要 null-probe calibration、MCT geometric validation、现象分类法等复杂机制。

2. **Chrabąszcz et al. 的 probe trajectory + 简单 ablation**：已有的 probe trajectory 工作已经能追踪模型内部状态随时间的变化，加上标准的 CoT truncation/perturbation 实验就能得到类似的 insight，不需要 ICG 框架。

3. **增量价值在哪？** Proposal 声称增量价值在于"calibrated gap metric"和"phenomenon taxonomy"。但 calibration 是技术细节而非概念突破；phenomenon taxonomy（pre-CoT encoding, genuine reasoning, post-hoc rationalization）是已知概念的重新标签化，这些现象已被 Cox et al., Boppana et al. 等分别研究过。

---

【前提假设检验】:

**核心 claim 的逻辑链条中存在至少两个重大未验证假设：**

1. **"causal interventions based on probes consistently fail on reasoning-trained models" — 可能与引用文献矛盾**
   - Proposal 声称 "Cox et al.: negligible flip rates"，但我找到的 Cox et al. (2603.01437) 实际报告 "steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines"。
   - 如果 Cox 的 activation steering 确实在 >50% 的情况下有效，那么 proposal 的整个前提——"probes diagnose but causal interventions fail, therefore the gap IS the faithfulness signal"——就失去了经验基础。
   - 可能 proposal 指的是另一篇 Cox 的论文、或者特指 reasoning-trained models（而非 instruction-tuned models），但这一关键区分在 proposal 中未充分阐明。**这是一个潜在致命的前提错误。**

2. **"G*(t) 的不同 pattern 能区分不同 faithfulness 现象" — 纯属假设**
   - Proposal 承认需要 Phase 0b 来验证"至少 2 个现象产生可区分的轨迹（effect size d > 0.5）"。这意味着核心 claim 目前完全未经验证。
   - 不同现象（pre-CoT encoding vs. genuine reasoning vs. post-hoc rationalization）可能在 G*(t) 空间中产生高度重叠的分布，导致分类不可行。
   - Proposal 的 semi-synthetic simulation 被自己降级为"hypothesis generation"而非"evidence"，说明作者也认识到这个风险。

3. **"P*(t) − C(t) 是有意义的减法" — 数学假设未论证**
   - P*(t) 是 probe 校准后的概率，C(t) 是因果贡献（通过 truncation/perturbation/NLDD 估计）。这两个量的量纲、尺度、噪声特征可能完全不同，直接相减是否有统计学意义？Proposal 未讨论。

---

【3 维度打分】:

1. **Novelty: 弱**
   - 核心概念"比较 probing 准确率与 causal contribution 的差异"是一个自然的组合想法，而非突破性洞见。
   - P*(t) 方向被 Chrabąszcz et al. (2605.18549) 的 probe trajectory 工作大量覆盖。
   - C(t) 的三种估计方法（truncation, perturbation, NLDD）都是已有文献中的标准方法。
   - Wang (2604.15726) 已经形式化了 H1/H2 框架，本 proposal 只是用 G*(t) 来操作化它。
   - Difficulty conditioning 直接建立在 Gjølbye et al. (2605.15454) 之上。
   - **在剔除 surface differences 后，真正的 novelty delta 很小**：主要是"把已有组件拼在一起并定义了一个 gap metric"。这在高竞争领域中不足以构成强 novelty。

2. **Significance: 中**
   - CoT faithfulness 是 AI safety 和 interpretability 的核心问题，研究问题本身是重要的。
   - 但"度量框架"论文的影响力取决于该框架是否被社区采用。ICG 框架的复杂度（null-probe calibration、MCT geometric validation、多种 C(t) 估计方法、difficulty conditioning、length correction）可能阻碍其可用性和可复现性。
   - 即使 G*(t) 曲线能区分不同现象，"so what"问题没有很好地回答——知道某个实例是 pre-CoT encoding 还是 post-hoc rationalization 之后，下一步做什么？缺乏 actionable implication。
   - 如果核心发现是 positive（即 G*(t) 确实能区分现象），审稿人可能会说 "interesting measurement, but I would have guessed that these phenomena produce different probe/causal patterns" — 这不是 surprising 的发现。

3. **Related Work: 中**
   - Proposal 确实覆盖了多个关键近期工作（Chrabąszcz, Wang, Gjølbye, NLDD 等），定位也算清晰。
   - 但对 Cox et al. 的引用存在潜在事实错误（将 >50% flip rate 描述为 "negligible flip rates"），这会严重损害 credibility。
   - 缺少对 "Breaking the Chain" (2603.16475)、FaithCoT-Bench (2510.04040) 等直接相关工作的讨论。
   - "Ballon et al." 的 truncation control conditions 未能在搜索中验证，可能存在引用准确性问题。

---

【概率估计】: [10% - 20%] 中位 12%

【估计理由】:
1. **如果投 CoRL：~0%**。会被 desk reject，完全不在 scope 内。
2. **如果投合适 venue（NeurIPS/ICLR/ICML）**：中位约 12%。Novelty 弱是主要限制因素——这是一个将已有组件（probe trajectory + causal intervention + H1/H2 框架）组合成新 metric 的 framework 论文，在一个研究密度极高的领域中，这种"组合 + 形式化"的贡献很难说服审稿人有足够的 novelty delta。核心前提（causal intervention fails on reasoning models）可能与引用文献矛盾，这进一步压低了评估。Significance 中等但缺乏 actionable implication，且核心发现若 positive 不够 surprising。
3. 上界被 Novelty 维度严格限制：即使实验做得完美，idea 本身的增量贡献空间有限。
4. 下界被前提假设的潜在错误拉低：如果 Cox et al. 的引用确实是误读，审稿人会直接质疑整个 motivation。

【主要风险】:
1. **核心前提可能不成立**：Proposal 的整个动机建立在"probes diagnose but causal interventions fail"的 empirical finding 上，但 Cox et al. (2603.01437) 实际报告 >50% 的 flip rate，与 proposal 声称的 "negligible flip rates" 矛盾。如果这个前提被审稿人推翻，整篇论文的 motivation 就塌了。
2. **Novelty 被近期工作严重压缩**：Chrabąszcz et al. 已做 probe trajectory，Wang 已形式化 H1/H2，NLDD 已有，difficulty conditioning 建立在 Gjølbye 之上——剩余的 novelty 主要是"定义了一个 gap metric"，这在顶会审稿中可能被认为是 incremental combination。
```

---

**补充说明：venue 问题**

这是一个需要立即纠正的问题。CoRL 2026 的 Call for Papers 明确要求 "submissions should focus on a core robotics problem"，且 "submissions without a robotics focus will be returned without review"。本 proposal 是纯 NLP/interpretability 研究，与机器人学习完全无关。建议将目标 venue 更换为 NeurIPS 2026、ICLR 2027、ACL/EMNLP 2026 等。上述概率估计已基于合适 venue 给出；若坚持投 CoRL，中稿概率为 **0%**。

Sources:
- [Chrabąszcz et al., "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"](https://arxiv.org/abs/2605.18549)
- [Wang, "LLM Reasoning Is Latent, Not the Chain of Thought"](https://arxiv.org/abs/2604.15726)
- [Cox et al., "Decoding Answers Before Chain-of-Thought"](https://arxiv.org/abs/2603.01437)
- [Gjølbye et al., "Reasoning Models Don't Just Think Longer, They Move Differently"](https://arxiv.org/abs/2605.15454)
- ["Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning"](https://arxiv.org/abs/2602.11201)
- ["Breaking the Chain: A Causal Analysis of LLM Faithfulness"](https://arxiv.org/abs/2603.16475)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide my assessment. Let me compile my findings.

---

```
【阶段】: Triage

【致命前置问题：投稿venue与论文主题严重不匹配】

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求：
- "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
- "Submissions without a robotics focus will be returned without review."
- 议题范围：imitation learning, RL for robots, sim-to-real, robot perception, manipulation, locomotion, learning-based planning 等。

本 proposal 是一篇纯粹的 NLP/LLM 可解释性论文（chain-of-thought faithfulness measurement），与机器人学没有任何关联。提交至 CoRL 将大概率被 desk reject（退回不审）。

这是一个致命的 venue mismatch。以下评估仍按 idea 内在质量给出（假设投稿至合适的 venue 如 NeurIPS / ICML / ACL / EMNLP），但 CoRL 的中稿概率需单独标注。

---

【领域调研】:

1. **Chrabąszcz et al., "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (arXiv 2605.18549, May 2026)**:
   最直接的竞争工作。在 4 个推理模型上构建 probe trajectory（每个 token 处评估 probe），使用 60+ 信号处理特征，max-pooling 达到 95% AUROC，比静态 probe 提升 17pp。该工作已经验证了"probe trajectory"方向的有效性，且已有完整的实验支撑。本 proposal 的 P*(t) 维度本质上是该工作的变体/延伸。

2. **Cox et al., "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering" (arXiv 2603.01437, March 2026)**:
   在 instruction-tuned 模型上证明 pre-CoT 阶段 probe 可以 >0.9 AUC 预测最终答案，且 steering 可以在 >50% cases 翻转答案。但明确指出在 reasoning-trained 模型上 causal intervention 效果减弱。proposal 引用此工作的"negligible flip rates"作为核心立论依据——但 Cox 的原文是在 instruction-tuned 模型上做的，对 reasoning models 的结果是 limitation 而非主发现，proposal 对此引用可能存在不准确。

3. **Wang, "LLM Reasoning Is Latent, Not the Chain of Thought" (arXiv 2604.15726, April 2026)**:
   形式化 H0/H1/H2 三个假说（H1: latent-state mediated; H2: CoT-mediated; H0: generic serial compute）。这是一篇 position paper，提供概念框架而非实证。proposal 声称 operationalize 其 H1/H2 distinction，但 Wang 的框架还包含 H0（generic compute hypothesis），proposal 似乎忽略了这一可能性。

4. **Gjølbye et al., "Reasoning Models Don't Just Think Longer, They Move Differently" (arXiv 2605.15454, May 2026)**:
   在 hidden-state trajectories 上发现 difficulty-geometry coupling（Codeforces 上 ρ⊥ = +0.41），但在 MATH 和 Boolean SAT 上显著更弱。proposal 引用此工作支撑 task-difficulty conditioning，但 Gjølbye 自身结论是 domain-specific 且效果有限。

5. **"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning" (arXiv 2602.11201, ICLR 2026 Workshop)**:
   提出 NLDD 指标，发现 Reasoning Horizon (k*) 在 70-85% chain length 处，之后 reasoning tokens 无正面贡献。proposal 直接将 NLDD 作为其 C(t) 的三种估计方法之一。

6. **"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures" (arXiv 2603.16475)**:
   Front-door causal framework 评估模型对中间结构的 faithfulness，发现 >60% consistency under prompt interventions 但 >50% failure on structural edits。

7. **"FaithCoT-Bench" (arXiv 2510.04040) / "C2-Faith" (arXiv 2603.05167)**:
   CoT faithfulness 的 benchmark 化尝试，提供标准化评估。

- **调研总结**: CoT faithfulness 是一个 2025-2026 年的研究热点，已有大量工作从不同角度切入（probe trajectories、causal perturbation、step-level metrics、benchmark 构建）。本 proposal 的核心思路——将 probe-based 诊断和 causal contribution 组合为一个"gap metric"——是对现有独立组件的**框架性整合**，而非方法论层面的根本创新。最直接竞争者 Chrabąszcz et al. 已发表且覆盖了 probe trajectory 维度；causal contribution 的三种方法（prefix truncation, paraphrase, NLDD）均为已有技术。

---

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁。**

1. **最简单的替代方案**：直接在现有 probe trajectory 工作（Chrabąszcz et al.）上加一列 per-step NLDD 或 prefix-truncation score，然后做相关性分析。这不需要整个 ICG 框架，不需要 null-probe calibration，不需要 MCT geometric validation，就能回答"probe 知道的 vs CoT 贡献的 是否有 gap"这个问题。

2. **增量价值在哪？** proposal 声称的增量是：(a) 将 gap 形式化为时间序列 G*(t)；(b) null-probe calibration；(c) phenomenon taxonomy。但 (a) 本质上是 visualization/framing 层面的贡献而非方法论创新；(b) 是技术细节层面的 robustness check；(c) 的分类目标（pre-CoT encoding vs genuine reasoning vs post-hoc rationalization）在 Cox et al. 和其他工作中已被作为分析维度使用。

3. **核心问题**：如果你给 Chrabąszcz 的 probe trajectories 加上一个 causal contribution 估计并做减法，和这个 proposal 的核心 output 有什么本质区别？proposal 没有清楚回答这个问题。

---

【前提假设检验】:

核心 claim 的逻辑链中有多个未经验证的假设：

1. **"P*(t) − C(t) 是有意义的减法"（最关键的假设）**: P*(t) 是 probe 在隐藏状态上的 correctness prediction probability，C(t) 是 causal contribution（来自 prefix truncation / paraphrase / NLDD）。这两个量的量纲、尺度、含义完全不同——一个是"模型内部是否已经'知道'答案"，另一个是"CoT 文本对最终答案的 causal effect"。将它们直接相减产生 G*(t) 在数学上缺乏严格 justification。这就像用温度减去风速——两个都能告诉你天气信息，但减法本身没有物理意义。

2. **"不同 faithfulness phenomena 会产生可区分的 G*(t) temporal fingerprints"**: 这是整个框架的核心赌注。proposal 自己也承认这需要 Phase 0b 来验证（effect size d > 0.5），但这同时意味着：如果验证失败，整个 framework 就没有意义。这不是一个已经有理论预期支撑的假设——它是一个纯经验赌注。

3. **"diagnostic-causal gap 是一个稳定的、可推广的现象"**: proposal 的立论基于"probes 能诊断但 causal intervention 失败"这一观察。但 Cox et al. 的实验主要在 instruction-tuned 模型上（steering 成功率 >50%！），在 reasoning models 上的结果作为 limitation 而非主发现报告。这个 gap 的 robustness 在 reasoning-trained models 上是否真的如 proposal 所声称的那样"robust"，尚缺乏跨模型的系统性验证。

4. **忽略 Wang 的 H0**: proposal 将 G*(t) >> 0 映射到 H1，G*(t) ≈ 0 映射到 H2，但完全没有处理 H0（generic serial compute）。如果真正的机制是 H0——模型只是通过更多 compute 步骤获益，而非通过任何"推理"——那么 G*(t) 的解读就完全不同。

---

【3 维度打分】:

1. **Novelty: 弱**
   - 核心贡献是"框架性整合"而非方法论创新。P*(t) 方向已被 Chrabąszcz et al. (2605.18549) 充分覆盖；C(t) 的三种方法（prefix truncation, paraphrase perturbation, NLDD）全部是已有技术；Wang (2604.15726) 的 H1/H2 概念框架也已存在。
   - proposal 的真正 novelty delta 是 G*(t) = P*(t) − C(t) 这个"gap metric"，但正如前提假设检验所指出的，这个减法在数学上缺乏 justification。
   - 与 Chrabąszcz et al. 的差异化定位不够有力：proposal 声称"adds the entire causal contribution dimension"，但 causal perturbation 方法是 CoT faithfulness 领域的标准工具（prefix truncation 在 Lanham et al. 2023 就已使用），将它和 probe trajectory 放在一起并不产生 1+1>2 的 insight。

2. **Significance: 中**
   - CoT faithfulness 本身是重要问题，关系到 LLM 的可信度和安全性。
   - 但该 proposal 的实际影响力受限于：(a) 框架的可操作性存疑（G*(t) 的减法含义不清），(b) phenomenon taxonomy 的实用价值取决于是否真的能区分不同现象（Phase 0b 是赌注），(c) 如果核心发现是 positive（不同现象确实有不同的 temporal fingerprint），审稿人的反应更可能是"makes sense, I would have guessed this"而非"surprising"——pre-CoT encoding 应该 P*(0) 高 C(0) 低，genuine reasoning 应该两者都增长，这些都是符合直觉的预测。
   - 对于 CoRL 而言：significance = 0（与机器人学完全无关）。

3. **Related Work: 中**
   - proposal 对近期工作有较好的覆盖（Chrabąszcz, Wang, Gjølbye, Cox 等），positioning 也有意识地在做。
   - 但存在引用不准确的风险：对 Cox et al. 的引用可能过度推断了 reasoning models 上的结果（原文主要是 instruction-tuned 模型）；对 Yuan et al. "all four intervention strategies fail" 的引用我未能在搜索中验证到一篇完全匹配的论文。
   - 缺少对 "Breaking the Chain" (2603.16475, front-door causal analysis) 和 FaithCoT-Bench (2510.04040) 等 benchmark 工作的讨论，这些是直接相关的竞争方向。

---

【概率估计】:

**针对 CoRL 2026**: 0-2%，中位 1%
- 理由：致命的 venue mismatch。CoRL 明确声明"Submissions without a robotics focus will be returned without review"。本 proposal 是纯 NLP/interpretability 论文，将被 desk reject。

**假设投稿至合适 venue（NeurIPS / ICML / ACL 主会）**: 12-22%，中位 16%

【估计理由】:
- Novelty 弱是上界的主要限制因素。核心贡献是已有技术的框架性组合（probe trajectory + causal perturbation + gap metric），缺乏方法论层面的真正创新。
- G*(t) 的数学 justification 薄弱（两个不同量纲量的减法）会成为审稿人攻击的首要目标。
- 如果 Phase 0b 验证成功，核心发现（不同现象有不同的 temporal signature）的 surprise value 有限——预测方向符合直觉。
- 积极面：proposal 的实验设计相对完善（有 Phase 0b 验证、honest scoping、compute budget 估计），如果执行得好可以产出一篇 solid 的 empirical paper。但 idea 内核的 novelty 瓶颈限制了上界。
- 在 CoRL venue 下，这些都不重要——直接 desk reject。

【主要风险】:
1. **致命 venue mismatch**：CoRL 是机器人学习会议，本论文与机器人学零关联，将被 desk reject。
2. **核心 metric G*(t) 的数学合理性**：P*(t) 和 C(t) 量纲不同，减法缺乏理论 justification。即使在合适 venue，这也是审稿人最可能质疑的点，可能被要求根本性重构 framework。
```

---

**总结**：这个 proposal 有两层问题。**第一层是致命的**：CoRL 是 Conference on Robot Learning，明确要求 submissions 必须 focus on a core robotics problem，否则直接 desk reject。本 proposal 是一篇纯粹的 LLM 可解释性/CoT faithfulness 论文，与机器人学没有任何关系。**即使 idea 本身质量极高，在 CoRL 的中稿概率也趋近于 0。** 第二层是 idea 质量本身：即使投稿至合适 venue（NeurIPS/ICML/ACL），核心 novelty 也偏弱——本质上是将已有组件（probe trajectories、causal perturbation methods、H1/H2 框架）进行框架性整合，而非方法论创新，且核心 gap metric G*(t) 的数学 justification 不足。

**强烈建议**：首先更换投稿 venue（考虑 NeurIPS 2026、ICML 2026、ACL/EMNLP 2025 等 NLP/ML venue），然后再进入迭代优化流程。

Sources:
- [Chrabąszcz et al., Probe Trajectories](https://arxiv.org/abs/2605.18549)
- [Cox et al., Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)
- [Wang, LLM Reasoning Is Latent](https://arxiv.org/abs/2604.15726)
- [Gjølbye et al., Reasoning Models Move Differently](https://arxiv.org/abs/2605.15454)
- [NLDD / Faithfulness Decay](https://arxiv.org/abs/2602.11201)
- [Breaking the Chain: Causal Analysis](https://arxiv.org/html/2603.16475v1)
- [FaithCoT-Bench](https://arxiv.org/html/2510.04040v1)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Chrabąszcz et al., "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (arXiv:2605.18549)](https://arxiv.org/abs/2605.18549) (2026): 最直接的竞争工作。已经在 4 个推理模型上做了 probe trajectory + 60+ 信号处理特征，达到比 static probe 高 17pp 的性能。Proposal 的 P*(t) 方向被此工作高度验证但也高度重叠。
- [Wang, "LLM Reasoning Is Latent, Not the Chain of Thought" (arXiv:2604.15726)](https://arxiv.org/abs/2604.15726) (2026): 已经形式化了 H1(latent-mediated) / H2(CoT-mediated) / H0(generic compute) 三假设框架。Proposal 声称 operationalize 此区分，但框架本身来自此文。
- [Gjølbye et al., "Reasoning Models Don't Just Think Longer, They Move Differently" (arXiv:2605.15454)](https://arxiv.org/abs/2605.15454) (2026): 已经做了 difficulty-geometry coupling 分析，发现 ρ⊥ = +0.41 (Codeforces) 且 domain-specific。Proposal 的 task-difficulty conditioning 直接复用此发现。
- ["Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning" (arXiv:2602.11201)](https://arxiv.org/abs/2602.11201) (ICLR 2026 Workshop): NLDD 指标已存在，已发现 Reasoning Horizon (70-85% chain length)。Proposal 将 NLDD 作为三种因果贡献估计方法之一直接使用。
- ["Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification" (arXiv:2504.05419)](https://arxiv.org/abs/2504.05419) (2025): 已证明推理模型隐藏状态编码正确性信息但未能利用，probe AUROC 高但介入效果差。Proposal 的核心前提观察来自此类工作。
- ["Breaking the Chain: A Causal Analysis of LLM Faithfulness" (arXiv:2603.16475)](https://arxiv.org/abs/2603.16475) (2026): 系统性因果分析 CoT 对中间结构的忠实度，发现模型对自生成结构比 gold 结构更忠实。
- ["Decoding Answers Before Chain-of-Thought" (arXiv:2603.01437)](https://arxiv.org/abs/2603.01437) (2026): Pre-CoT probes + activation steering，已经在探测 CoT 前答案编码。

- **调研总结**: CoT faithfulness 是 2025-2026 年 NLP 解释性领域的热点方向，已有大量工作分别从 probe trajectory、因果介入、NLDD 指标、difficulty conditioning 等角度展开。该 proposal 的各个组件（probe trajectory, 因果贡献估计, difficulty conditioning）均已有独立的近期论文覆盖；其核心主张的 novelty 在于将这些组件组合为一个统一的 "gap metric" 框架。

【Trivial Alternative 检验】:
**存在显著的 trivial alternative 威胁。** 
Proposal 的核心度量 G*(t) = P*(t) − C(t) 本质上是将两个已有的度量（probe correctness prediction 和 causal contribution estimation）相减。一个研究者已经可以：(1) 用 Chrabąszcz 等人的 probe trajectory 方法跟踪内部状态演变；(2) 用 NLDD 或 prefix truncation 单独评估因果贡献；(3) 直接对比两个信号在时间轴上的行为。这不需要一个新的"框架"——分别 plot 两条曲线并目视/统计比较，就能得到 proposal 声称的 "divergence fingerprint"。将两个已有信号相减并命名为 "ICG" 的增量价值有限。真正的增量在于：是否存在 calibration 方法使得 P*(t) 和 C(t) 在同一度量空间中可减，以及减出来的 gap 是否比单独看两个信号提供了**不可通过其他方式获得**的洞见。Proposal 未能令人信服地论证后者。

【前提假设检验】:
核心 claim 的逻辑链有多个未经验证的环节：
1. **P*(t) 和 C(t) 在同一标尺上可相减**：probe 输出的概率和因果贡献（truncation accuracy drop / NLDD score / paraphrase sensitivity）是完全不同性质的量。"null-probe calibration" 是否真的能让它们 commensurable 是一个未经实证的假设。
2. **Gap 的 temporal shape 能区分 faithfulness phenomena**：proposal 假设 pre-CoT encoding、genuine reasoning、post-hoc rationalization 会产生可区分的 G*(t) 形状，但这完全是 hypothetical——没有任何先验理论或实证表明这些现象的 gap curve 形状会有 d > 0.5 的效应量。
3. **跨研究数字的可组合性**：proposal 大量引用不同研究的数字（Cox 的 AUROC, David 的 easy/hard split, Gjølbye 的 ρ⊥）作为框架设计依据，但这些数字来自不同模型、不同任务、不同设置，组合起来的有效性存疑。虽然 proposal 加入了 Phase 0b pilot 来验证，这说明作者意识到了这个问题，但也说明核心 claim 目前缺乏实证基础。

【3 维度打分】:

1. **Novelty: 弱** — Proposal 的每个组件都直接来自近期已发表工作：probe trajectory (Chrabąszcz 2605.18549)、NLDD (arXiv:2602.11201)、H1/H2 框架 (Wang 2604.15726)、difficulty-geometry coupling (Gjølbye 2605.15454)、prefix truncation 因果分析 (Ballon et al.)。"将 probe 信号与因果贡献信号相减得到 gap" 是一个 natural next step，而非 surprising insight。核心 novelty claim 是 "gap metric + calibration + temporal fingerprint → faithfulness taxonomy"，但这更像是一个工程性的组装，而非概念性的突破。如果最终结果是 positive（gap curve 确实能区分 phenomena），审稿人更可能说 "makes sense, I would have expected this to work" 而非 "surprising"。

2. **Significance: 中** — CoT faithfulness 确实是重要问题，了解模型"知道但不使用"的信息有实际价值。但此 proposal 本质上是一个**诊断/测量框架**，不改进模型、不提供 actionable 的训练信号、不直接解决安全问题。其价值取决于 taxonomy 的实用性——如果最终只能区分 2-3 种现象且无法指导下游干预，影响力有限。此外，830 H100-hours 的计算成本相对于一个诊断工具来说偏高。

3. **Related Work: 中** — Proposal 引用的关键论文（Chrabąszcz 2605.18549, Wang 2604.15726, Gjølbye 2605.15454, NLDD 2602.11201）经验证均真实存在且描述基本准确。差异化定位（"我们加了 causal contribution 维度"）也有合理性。但 proposal 对最直接竞争者的差异化论证不够有力——Chrabąszcz 已经用 probe trajectory 做到了很多，加上 causal contribution 维度的**边际价值**没有被清晰论证。同时，对 "Breaking the Chain" (2603.16475) 和 "Decoding Answers Before Chain-of-Thought" (2603.01437) 等高度相关工作的讨论不足。

【⚠️ 致命问题：venue mismatch】:
**CoRL (Conference on Robot Learning) 2026 明确要求所有投稿必须聚焦于机器人学习核心问题（"submissions without a robotics focus will be returned without review"）。本 proposal 是纯 NLP/AI 可解释性工作（CoT faithfulness 诊断框架），不涉及任何机器人、物理交互、控制、感知或 embodied AI 内容。按照 CoRL 的 scope 政策，本文将在 desk review 阶段被直接退回（desk reject），不会进入同行评审。**

这不是 idea 质量问题，而是投稿目标会议与论文内容的根本性错配。该 proposal 的合适 venue 应为 NeurIPS / ICML / ACL / EMNLP 等 NLP/ML 主会，或 ICLR。

【概率估计】: [0% - 3%] 中位 1%

【估计理由】: 
即使完全不考虑 venue mismatch（假设投到合适的 NLP/ML venue），基于 idea 质量的估计约为 [15% - 25%] 中位 20%——idea 方向站得住脚但内核薄弱，各组件来自已有工作的组装，核心 gap metric 存在 trivial alternative 威胁，前提假设（P* 和 C 可减、gap shape 可区分现象）未经验证。Novelty 弱是限制上界的主要维度。

但考虑到投稿目标是 **CoRL 2026**（Conference on Robot Learning），该 proposal 将几乎确定被 desk reject。因此实际概率接近 0%。

【主要风险】:
1. **致命 venue mismatch**: CoRL 要求 robotics focus，本文是纯 NLP 可解释性工作，将被 desk reject
2. **Novelty 不足**: 核心贡献是组合已有工具（probe trajectory + 因果贡献估计 + gap metric），缺乏概念性突破，审稿人可能认为是 "engineering contribution" 而非 "scientific insight"
```

---

**总结**：这个 proposal 存在一个**致命的 venue 错配问题**。CoRL 是 Conference on Robot Learning，明确要求论文聚焦机器人学习，non-robotics 投稿会被直接退回。本 proposal 是纯粹的 NLP/AI 可解释性研究（CoT faithfulness 诊断框架），与机器人学习没有任何关联。

即使抛开 venue 问题单看 idea 质量，novelty 也偏弱——各组件（probe trajectory, NLDD, difficulty conditioning, H1/H2 框架）均来自 2025-2026 年的已发表工作，核心创新在于将它们组合为一个 gap metric，但这个组合是 natural next step 而非 surprising insight。

**建议：如果要推进此 proposal，应将目标 venue 改为 NeurIPS / ICML / ACL / EMNLP 等 NLP/ML 主会，并需在 novelty 层面做实质性加强——比如证明 gap metric 能提供单独看 probe 或单独看 causal contribution 所无法获得的独特洞见。**

Sources:
- [Chrabąszcz et al., "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"](https://arxiv.org/abs/2605.18549)
- [Wang, "LLM Reasoning Is Latent, Not the Chain of Thought"](https://arxiv.org/abs/2604.15726)
- [Gjølbye et al., "Reasoning Models Don't Just Think Longer, They Move Differently"](https://arxiv.org/abs/2605.15454)
- ["Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning"](https://arxiv.org/abs/2602.11201)
- ["Reasoning Models Know When They're Right"](https://arxiv.org/abs/2504.05419)
- ["Breaking the Chain: A Causal Analysis of LLM Faithfulness"](https://arxiv.org/abs/2603.16475)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)


【原始 proposal（允许参考但不是主要依据）】:
# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness

## Description
We propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.

The framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness (explicitly targeting right/wrong prediction — justified over answer-content probes by broader applicability beyond binary tasks, grounding in the diagnostic-not-causal finding which is about correctness, and more direct faithfulness interpretation — with supplementary answer-content analysis on binary/MC subsets), and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions validating sequential content matters, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).

Positioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes across 4 reasoning models — our framework adds the entire causal contribution dimension, the calibrated gap metric, null-probe calibration with MCT geometric validation, phenomenon taxonomy, and task-difficulty conditioning. Their probe-trajectory methodology validates our P*(t) direction; we extend it to the dual-estimator gap that no existing framework provides.

We adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) constructs real G*(t) curves from the SAME model and dataset and tests whether at least 2 phenomena produce distinguishable trajectories (effect size d > 0.5) before committing to the full classification pipeline — addressing the concern that semi-synthetic simulation from cross-study measurements overestimates real-data accuracy. The semi-synthetic simulation is retained as hypothesis generation producing testable predictions, not as evidence.

Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits, the ICLR 2026 Workshop finding, and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific (weaker on MATH) — reveals the decorative→load-bearing transition with practical guidance on when chain-of-thought adds genuine value, applying length correction (residualizing on log(N)) to avoid generation-length confounds.

The paper focuses on four core contributions: (a) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. to demonstrate the value of the causal contribution dimension; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real data; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) probe-target analysis contrasting correctness vs. answer-content gaps. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs) as the primary bottleneck.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "44250894-e962-4e86-918d-3dd16a0bb468",
  "type": "user",
  "uuid": "21dac8bf-8408-410e-a2f6-1766ac5f16c0",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:02:36.647Z_

```json
{
  "parentUuid": "21dac8bf-8408-410e-a2f6-1766ac5f16c0",
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
  "uuid": "443b202e-69ca-4805-a161-0556bdb33e30",
  "timestamp": "2026-05-20T03:02:36.647Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:02:36.648Z_

```json
{
  "parentUuid": "443b202e-69ca-4805-a161-0556bdb33e30",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "05e3f84a-6800-4c4b-9622-ff572316b47c",
  "timestamp": "2026-05-20T03:02:36.648Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information to make a thorough assessment. L…",
  "leafUuid": "05e3f84a-6800-4c4b-9622-ff572316b47c",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM CoT faithfulness diagnostic framework proposal",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:03:05.391Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments systematically as a Meta Judge.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 中 (Medium)
- Probability estimate: [10% - 20%] 中位 12% (assuming correct venue)
- CoRL probability: ~0%
- Key concerns: Core premise may contradict Cox et al., novelty compressed by recent work, trivial alternative exists
  
**Reviewer 2:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 中 (Medium)
- Probability estimate (correct venue): [12% - 22%] 中位 16%
- CoRL probability: [0% - 2%] 中位 1%
- Key concerns: G*(t) mathematical justification weak, venue mismatch fatal, framework is combination of existing components

**Reviewer 3:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 中 (Medium)
- Probability estimate (correct venue): [15% - 25%] 中位 20%
- CoRL probability: [0% - 3%] 中位 1%
- Key concerns: Venue

All three reviewers converge on weak novelty and medium significance, with acceptance probabilities ranging from 12-20% at the correct venue and essentially zero for CoRL. The main criticisms center on weak mathematical foundations, the framework being a recombination of existing work, and potential fundamental issues with the core premise. All three reviewers unanimously agree on the fatal venue mismatch for CoRL, weak novelty, medium significance and related work quality, and that the core components are borrowed from existing work without proper mathematical justification for the gap subtraction. They also concur that the central claim about gap shapes distinguishing phenomena remains unverified, while two reviewers flag potential citation inaccuracies and missing related work discussions, and all three identify Chrabąszcz et al. as the most direct competitor in this space.

A few points stand out as coming from individual reviewers—R2 emphasizes Wang's H0 being overlooked, R1 questions the verifiability of a Ballon et al. citation, and R3 brings up a recent paper on reasoning models knowing when they're right. Now I'm looking at the implementation details: the proposal requires 830 H100-hours with NLDD on 32B models as the computational bottleneck, spanning 4 models across 4 benchmarks, and needs a pilot phase first. For the final probability assessment, CoRL is essentially a desk reject at 0-1%, and for the correct venue, given the standard deviation around 3.3% and three midpoint estimates of 12%, 16%, and 20%, the median sits at 16%, which aligns with the stricter interpretation of the guidelines.

Actually, I need to reconsider the framing here. All three reviewers flagged this as a fundamental venue mismatch for CoRL 2026, making the acceptance probability effectively 0% for that specific venue. However, they all provided conditional estimates assuming an appropriate venue, which is what actually matters for evaluating the idea's merit. I should report both the CoRL probability and the conditional assessment separately, with the recommendation being either a kill for CoRL or a venue pivot for the work itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05e3f84a-6800-4c4b-9622-ff572316b47c",
  "isSidechain": false,
  "requestId": "req_011CbD5R6Y41PccMbTZmtm8F",
  "type": "assistant",
  "uuid": "81cbdb29-e472-448a-a63c-6092fca5800f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AZg1xfzgj2eNgR9JGk84g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20244,
      "cache_read_input_tokens": 11374,
      "output_tokens": 4258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4258,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 20244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20244
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

_source line 9 · 2026-05-20T03:04:04.534Z_

【阶段】: Meta Judge
【三次中位】: [12%, 16%, 20%]  std=3.3%
（注：以上为三位审稿人「假设投稿至合适 ML/NLP venue」的概率中位。三位审稿人对 CoRL 2026 的概率评估一致为 0-1%。）

【共识维度】（2+ 人同时提到，高信号）:

| 维度 | 判决 | 提及人数 | 说明 |
|------|------|----------|------|
| **Venue 匹配** | **致命** | 3/3 | 全票一致：CoRL 要求 robotics focus，本文纯 NLP/interpretability，将被 desk reject |
| **Novelty** | **弱** | 3/3 | 全票一致：各组件（probe trajectory, NLDD, H1/H2, difficulty conditioning）均来自已有工作；核心贡献是"框架性组合"而非方法论创新 |
| **Significance** | **中** | 3/3 | 全票一致：CoT faithfulness 问题本身重要，但诊断/测量框架的 impact 受限于可操作性和 surprise value |
| **Related Work** | **中** | 3/3 | 全票一致：覆盖尚可但存在引用准确性问题 |
| **Trivial Alternative** | **存在威胁** | 3/3 | 全票一致：直接在 Chrabąszcz probe trajectory 上叠加 causal contribution 估计并比较，无需整个 ICG 框架即可回答核心问题 |
| **G*(t) 减法数学合理性** | **弱/未论证** | 3/3 | 全票一致：P*(t) 与 C(t) 量纲、尺度不同，直接相减缺乏理论 justification |
| **核心 claim 未经验证** | **高风险** | 3/3 | 全票一致：不同 faithfulness phenomena 产生可区分 G*(t) fingerprint 纯属假设，Phase 0b 是赌注 |
| **Cox et al. 引用可能不准确** | **高风险** | 2/3 (R1, R2) | Cox 原文报告 >50% flip rate，proposal 称 "negligible flip rates"——若属误读，整个 motivation 前提塌陷 |
| **缺少关键 related work 讨论** | **中风险** | 2/3 (R2, R3) | "Breaking the Chain" (2603.16475)、FaithCoT-Bench (2510.04040) 未被讨论 |

【异常维度】（仅 1 人提到，降权处理）:

| 维度 | 审稿人 | 说明 | 处理 |
|------|--------|------|------|
| 忽略 Wang 的 H0 假设 | R2 | Proposal 只处理 H1/H2，未考虑 H0（generic serial compute） | 有道理但非致命，降权保留为次要风险 |
| "Ballon et al." 引用不可验证 | R1 | 未能在搜索中确认此引用 | 单人提到，标注为"待核实" |
| 830 H100-hours 计算成本偏高 | R3 | 对诊断工具而言成本高 | 合理担忧但非决定性因素 |

【最终概率】: [0% - 2%] 中位 0%

**↑ 以上为 CoRL 2026 投稿概率。三位审稿人全票一致判定 venue 致命错配，desk reject 不进入评审。**

**假设更换至合适 venue（NeurIPS 2026 / ICML 2026 / ICLR 2027）：**
[10% - 18%] 中位 14%

【一致性】: 高

三位审稿人在所有 rubric 维度上判决完全一致（Novelty 弱、Significance 中、Related Work 中），概率估计 std=3.3% 处于高一致与中一致的边界。考虑到 rubric 判决零分歧（远比数字 std 更重要），判定为高一致。按规则取中位附近并略偏严格方向。

【综合理由】:

**1. Venue 问题（致命，决定性）：** 三位审稿人独立发现并全票判定致命。CoRL 2026 Call for Papers 白纸黑字："Submissions without a robotics focus will be returned without review." 本 proposal 是纯 LLM CoT faithfulness 诊断论文，无任何 robotics 内容。CoRL 中稿概率 = 0%，无任何优化空间可改变此结论。

**2. Idea 质量评估（假设合适 venue）：**

- **Novelty 弱是共识性天花板。** 三人一致认为：P*(t) 方向被 Chrabąszcz et al. (2605.18549) 高度覆盖，C(t) 三种方法全是已有技术，H1/H2 框架来自 Wang (2604.15726)，difficulty conditioning 来自 Gjølbye et al. (2605.15454)。核心 novelty delta 仅是"定义了 G*(t) = P*(t) − C(t) 这个 gap metric"，属于 natural next step 而非 surprising insight。在 2025-2026 年该领域研究密度极高的背景下，这种框架性组合的 novelty 不足以支撑顶会接收。

- **Trivial alternative 威胁真实存在。** 三人一致指出：在 Chrabąszcz 的 probe trajectory 上直接叠加 per-step causal contribution 估计并比较，无需整个 ICG 框架即可回答相同的核心问题。Proposal 未能令人信服地论证 ICG 框架提供了"单独看两个信号所无法获得的独特洞见"。

- **G*(t) 减法的数学合理性是共识攻击点。** P*(t)（probe 校准概率）与 C(t)（因果贡献）量纲不同、尺度不同、噪声特征不同，直接相减是否有统计学意义未被论证。R2 的比喻精准："就像用温度减去风速"。

- **Cox et al. 引用潜在误读是前提性风险。** R1 和 R2 均指出 Cox et al. (2603.01437) 实际报告 >50% 的 flip rate（在 instruction-tuned 模型上），而 proposal 称 "negligible flip rates"。若此为误读，"probes diagnose but interventions fail" 的整个 motivation 前提失去经验基础。

- **概率从中位偏严处理。** 三人中位分别为 12%、16%、20%，中位是 16%。鉴于：(a) rubric 判决全部一致偏严（Novelty 全弱），(b) 存在前提可能不成立的风险（Cox 引用），(c) 核心 claim 完全未经验证（Phase 0b 是赌注），按"宁缺毋滥"原则将最终中位下调至 14%，区间压缩至 [10%-18%]。

**3. 异常点处理：**
- R2 关于 H0 忽略的指出有理论价值，但不改变 Novelty 判决，作为次要风险保留。
- R1 关于 "Ballon et al." 不可验证的指出为孤证，不影响整体判决。

【建议】: KILL（CoRL 2026）/ 如更换至 NeurIPS/ICML/ICLR 则为「边缘偏不推荐」

【实施评估】:
  - **计算资源**: ~830 H100-hours（proposal 自估），NLDD on 32B models 约 250 hrs 为主要瓶颈。4 models × 4 benchmarks 的全矩阵实验。对于一篇诊断/测量框架论文，计算成本偏高。
  - **数据需求**: 标准公开推理 benchmark（GSM8K, MATH, Codeforces 等），数据可得性无障碍。
  - **人工介入**: 需要人工设计 semi-synthetic simulation、标注 faithfulness phenomena ground truth（用于 Phase 0b 验证）。phenomenon taxonomy 的 ground truth 获取本身是一个研究难题。
  - **训练需求**: 需要训练 linear probes（计算量小），不需要训练/微调 LLM 本身。但 null-probe calibration 和 MCT geometric validation 增加了实验复杂度。
  - **新 Benchmark**: 不构建新 benchmark，但 Phase 0b pilot 本质上需要构建一个小规模验证数据集，含已知 faithfulness phenomena 的标注实例。
  - **预估周期**: 3-4 个月（Phase 0b pilot 1 个月 + 全矩阵实验 1.5 个月 + 分析写作 1 个月）。前提是 Phase 0b 验证通过；若失败则需根本性重构。

---

鉴于 CoRL 2026 投稿为 0% 概率（desk reject 确定），且即使更换至合适 venue idea 质量中位仅 14%（Novelty 弱为共识性天花板），最终判定为 **KILL（对 CoRL 2026 投稿）**。

若作者希望继续推进此方向，需同时满足：
1. **更换 venue** 至 NeurIPS 2026 / ICML 2026 / ICLR 2027 / ACL-EMNLP 2026
2. **实质性加强 Novelty**：不能止于"框架性组合"，需要证明 G*(t) 能提供两个单独信号无法获得的独特洞见（即 1+1>2），并严格论证减法的数学合理性
3. **核实 Cox et al. 引用**：确认 "negligible flip rates" 的引用是否准确，若不准确需重构 motivation
4. **Phase 0b 先行**：在投入全部计算资源前，先完成 pilot 验证核心假设

即便以上全部完成，中稿概率上界仍受 Novelty 天花板限制（估计 ≤25%），属于边缘投稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81cbdb29-e472-448a-a63c-6092fca5800f",
  "isSidechain": false,
  "requestId": "req_011CbD5R6Y41PccMbTZmtm8F",
  "type": "assistant",
  "uuid": "b3f2cf51-f965-40fc-bae4-121a92fffd00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AZg1xfzgj2eNgR9JGk84g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20244,
      "cache_read_input_tokens": 11374,
      "output_tokens": 4258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4258,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 20244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20244
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information to make a thorough assessment. L…",
  "leafUuid": "b3f2cf51-f965-40fc-bae4-121a92fffd00",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM CoT faithfulness diagnostic framework proposal",
  "sessionId": "7d5ddf17-2274-4765-8596-7cfca4aa1617"
}
```

---
