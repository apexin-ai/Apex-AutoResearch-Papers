# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/aebc21a5-e118-4c8d-8ee8-f05daa159bc0.jsonl`
- **Structured JSON:** [`3df5498c3dc69dd75214.json`](../../sessions/3d/3df5498c3dc69dd75214.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:30:46.952Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:30:46.952Z",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me synthesize my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. \"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning\" (arXiv 2602.03978, Feb 2026):\n   最直接相关的前序工作之一。核心发现：RLVR 的 monitorability 提升来自 response distribution sharpening 和 prompt attention 增加，而非来自更强的 causal reliance on reasoning traces。这直接暗示了 surface 和 latent faithfulness 之间可能存在脱节——本 proposal 的核心假设几乎是这篇论文结论的自然推论。\n\n2. \"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\" (arXiv 2603.01437, Mar 2026):\n   建立了 pre-CoT linear probe 方法论（>0.9 AUC），证明模型在生成 CoT 前已在 residual stream 中编码答案，且 probe direction 具有因果效力。本 proposal 直接复用该方法。该论文仅分析 final models，无 training dynamics。\n\n3. \"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\" (arXiv 2602.12506, Feb 2026):\n   在 VLM 上做了 GRPO checkpoint 级的 surface faithfulness tracking，发现 accuracy-faithfulness trade-off。但仅用 LLM-as-judge 等 surface metrics，无 latent-space 分析，且针对 VLM 而非 LLM。\n\n4. \"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes\" (arXiv 2602.15515, Feb 2026, FAR AI):\n   **技术路径最接近的竞争者。** 已经做了：在 GRPO training checkpoints 上训练 logistic regression probes on residual streams (Llama-3-8B through 70B)。但其焦点是 reward-hacking obfuscation（deception probes），而非 general faithfulness divergence，且未同步测量 surface faithfulness metrics。\n\n5. \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (arXiv 2605.18549, May 2026):\n   提出 probe trajectories 方法论（token-level），在 inference 时跟踪 probe 输出的时序演变，达 95% AUROC。但仅分析 fixed final models（Llama-8B-R1-Distill, Qwen3），无 training dynamics。\n\n6. \"Catching Rationalization in the Act\" (arXiv 2603.17199, Mar 2026):\n   用 activation probing 检测 motivated reasoning，训练 pre-/post-CoT probes。仅分析 final models。\n\n7. \"The Hypocrisy Gap\" (arXiv 2602.02496, Jan 2026):\n   用 SAE 量化 internal belief vs. CoT explanation 的 divergence。AUROC 0.55–0.74，仅分析 final models。\n\n8. \"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?\" (arXiv 2506.14261, Jun 2025):\n   证明 7B–14B 模型可通过 RL 学会逃避 latent-space monitors。Token-level monitors 脆弱，但 max-pooling/attention-based 更鲁棒。是关于 adversarial evasion 的发现，非 natural faithfulness divergence。\n\n9. \"How Does Unfaithful Reasoning Emerge from Autoregressive Training?\" (arXiv 2602.01017, Feb 2026):\n   在 synthetic toy arithmetic 设置中展示 faithful→unfaithful phase transition，但距离真实 GRPO 训练场景甚远。\n\n10. Counterfactual Simulation Training (arXiv 2602.20710), FaithRL (2602.03507), AtManRL (2604.16158):\n    提出改善 faithfulness 的 RL objectives，但不涉及 standard GRPO 的 divergence 特征化。\n\n- **调研总结**: CoT faithfulness 在 2026 年是一个极其活跃但高度碎片化的领域。Surface faithfulness across RL steps（behavioral only）和 latent faithfulness in final models（snapshot only）分别已有大量工作，但两者在 matched training checkpoints 上的联合追踪确实是一个未填补的 gap。**然而**，这个 gap 更接近于\"将已有工具组合应用在已有实验框架上\"，而非一个需要新方法论或新理论洞见的 gap。最近的 Obfuscation Atlas 在技术路径上最为接近，已证明 probing across GRPO checkpoints 完全可行。\n\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。** 具体来说：\n\n1. **从 Obfuscation Atlas 出发的最小扩展**：Obfuscation Atlas 已有 GRPO checkpoint-level probes on residual streams。将其 deception probes 替换为 general faithfulness probes（following Cox et al.），并在每个 checkpoint 加上 hint-injection 测量，即可实现本 proposal 的核心贡献。这本质上是\"换一种 probe target + 加一个 surface metric\"——方法论层面几乎无创新。\n\n2. **从 VLM checkpoint paper 出发的最小扩展**：该论文已有 GRPO checkpoints + surface faithfulness tracking。在其上加 activation probes 即可覆盖本 proposal 的核心 idea（虽然需要从 VLM 切换到 LLM）。\n\n**增量价值**：proposal 的增量在于 (a) 联合测量 surface + latent 并绘制 divergence curve，(b) 两个 model family 对比，(c) changepoint detection 分析 divergence dynamics。这些是有价值的贡献，但属于实验设计层面的增量，而非 idea 层面的根本创新。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条有两个关键假设值得审视：\n\n1. **\"Rising probe AUC = strengthening answer pre-commitment\"**：这个等式是否成立？Probe AUC 的上升可能反映多种因素——模型表示在 RL 训练中变得更 linearly separable 并不一定等同于\"模型更早地确定了答案\"。RL 训练改变了 representation geometry，probe 的可解释性可能随训练动态变化。这是一个未经充分验证的假设。\n\n2. **\"Surface faithfulness improvement + latent bypass strengthening = systematic decoupling\"**：proposal 假设如果 surface metrics 改善而 probe AUC 上升，则说明 RL \"decouples what models say from what they compute\"。但另一种解释是：RL 让模型既更好地推理（latent），又更好地呈现推理（surface），probe AUC 上升只是反映了 representation 更清晰，而非 faithfulness 的下降。换言之，**两个指标同向变化未必代表 divergence，取决于如何解读 probe AUC 的语义**。\n\n3. **\"GRPO training on MATH/GPQA 足以产生有意义的 faithfulness divergence\"**：proposal 假设标准 GRPO 训练就会产生这种 gap，但如果 MATH/GPQA 的 reward signal 足够 aligned with faithful reasoning，divergence 可能很小或不存在。training data/reward design 的选择可能强烈影响结果的 generalizability。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱–中** — \n   核心 novelty 是\"在 matched GRPO checkpoints 上联合测量 surface + latent faithfulness\"。但这本质上是将已有工具（pre-CoT probes from Cox et al. 2603.01437, hint-injection from Chen et al. 2505.05410, NLDD from 2602.11201）在已有实验框架（GRPO checkpoint studies à la Obfuscation Atlas 2602.15515 和 VLM checkpoint paper 2602.12506）上的组合应用。无新的 probe 方法论、无新的 metric、无新的理论框架。Obfuscation Atlas 已证明 probing across GRPO checkpoints 的技术可行性；从 deception probes 切换到 faithfulness probes 是一个自然且低成本的延伸。两个 model family 的对比和 changepoint detection 增加了一些实验设计层面的 novelty，但不改变 idea 层面的本质。\n\n2. **Significance: 中** — \n   研究问题本身是重要的：理解 RL 训练如何影响 surface 与 internal faithfulness 的关系对 AI safety 有直接意义。如果结果表明 gap 大且系统性，确实会影响对 RL-trained reasoning models 部署监控策略的决策。然而，**核心假设（GRPO 会制造 widening gap）已被现有证据强烈暗示**——RLVR monitorability (2602.03978) 已表明 surface gains ≠ causal reliance improvement，pre-CoT probes (2603.01437) 已表明 answer pre-commitment 存在于 final models。一个 positive 结果（gap widens）是大多数领域内研究者已经预期的，审稿人更可能说 \"I would have guessed this\" 而非 \"this is surprising\"。真正 surprising 的结果——例如 gap 不存在，或存在 non-monotonic dynamics——proposal 并未将其作为核心 framing。\n\n3. **Related Work: 强** — \n   这是 proposal 最突出的优势。Landscape 梳理全面、组织清晰，按 surface faithfulness / latent faithfulness / probe trajectories / deception probes / RL dynamics 等维度系统分类。每篇论文的定位准确（经调研验证，所有引用的关键论文均真实存在且描述准确）。Gap 的识别精确——确实没有工作在 matched checkpoints 上做 joint surface + latent tracking。但 related work 做得好是 proposal 的基本要求，不应因此过度提升对 idea quality 的评估。\n\n\n【概率估计】: [22% - 32%] 中位 26%\n\n【估计理由】: \nRelated Work 覆盖全面且 gap 识别精确（强），表明作者对领域有深入理解，这是进入合理区间的基础。然而，Novelty 偏弱是主要限制因素——核心贡献是将 3-4 个已有工具的组合应用，Obfuscation Atlas 和 VLM checkpoint paper 的存在构成严重的 trivial alternative 威胁。Significance 被\"预期中的结果\"所压制：核心假设（widening gap）已被 RLVR monitorability + pre-CoT probes 的汇聚证据强烈暗示，positive 结果不会让审稿人感到 surprising。\n\n该 proposal 处于 rubric 的 25-35% 区间下段：idea 有实质内核，方向正确，有真实但有限的 novelty delta，但核心发现若 positive 审稿人大概率会说 \"I would have guessed this\"。Novelty 维度的弱势将上界限制在 ~32%。\n\n【主要风险】:\n1. **\"组合式 novelty\"被判为 incremental**：审稿人可能认为\"将 Obfuscation Atlas 的 checkpoint probing 框架 + Cox et al. 的 pre-CoT probes + Chen et al. 的 hint-injection 合在一起\"是一个自然的、低技术门槛的组合，不构成足够的 intellectual contribution for a top venue。\n2. **\"Confirmatory study\"定位问题**：如果 positive result 只是确认了 RLVR monitorability (2602.03978) 已强烈暗示的结论（surface gains ≠ latent improvement），审稿人可能质疑：除了量化一个已预期的现象外，这项工作提供了什么新的 insight？在 ICLR 2027 这类强调 novelty 的 venue，confirmatory measurement studies 的接受度有限。\n```\n\nSources:\n- [Monitorability as a Free Gift (2602.03978)](https://arxiv.org/abs/2602.03978)\n- [Decoding Answers Before Chain-of-Thought (2603.01437)](https://arxiv.org/abs/2603.01437)\n- [On Robustness and CoT Consistency of RL-Finetuned VLMs (2602.12506)](https://arxiv.org/abs/2602.12506)\n- [The Obfuscation Atlas (2602.15515)](https://arxiv.org/abs/2602.15515)\n- [Monitoring the Internal Monologue (2605.18549)](https://arxiv.org/abs/2605.18549)\n- [Catching Rationalization in the Act (2603.17199)](https://arxiv.org/abs/2603.17199)\n- [The Hypocrisy Gap (2602.02496)](https://arxiv.org/abs/2602.02496)\n- [RL-Obfuscation (2506.14261)](https://arxiv.org/abs/2506.14261)\n- [Why Models Know But Don't Say (2603.26410)](https://arxiv.org/html/2603.26410v1)\n- [AtManRL (2604.16158)](https://arxiv.org/html/2604.16158)\n- [Counterfactual Simulation Training (2602.20710)](https://arxiv.org/abs/2602.20710)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have comprehensive research data. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **\"Reasoning Models Don't Always Say What They Think\" (Anthropic, 2505.05410, 2025)**:\n   Chen et al. 的 hint-injection 方法论——本 proposal 直接复用的 surface faithfulness 指标。发现 outcome-based RL 初期提升 faithfulness (MMLU +63%, GPQA +41%)，但很快 plateau（仅达 ~25-28%）。这篇已经沿 RL steps 跟踪了 surface faithfulness。\n\n2. **\"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning\" (2602.03978, 2026)**:\n   发现 RLVR 的 surface monitorability 提升来自 response distribution sharpening 和 increased prompt attention，而非更强的 causal reliance on reasoning traces。这是本 proposal 核心假设的直接来源。\n\n3. **\"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes\" (Cox et al., 2603.01437, 2026)**:\n   在 Gemma 2 和 Qwen 2.5 上演示 pre-CoT 线性 probe 可达 >0.9 AUC 预测最终答案，且 probe 方向具有因果效力（activation steering 可改变答案）。这是本 proposal 的 latent faithfulness proxy 的方法论来源。\n\n4. **\"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\" (2602.12506, 2026)**:\n   在 Qwen2.5-VL-7B 的 GRPO checkpoints 上发现 accuracy-faithfulness trade-off，但仅使用 LLM-as-judge 等 behavioral metrics，无 activation probes。仅限 VLM。\n\n5. **\"The Obfuscation Atlas\" (FAR AI, 2602.15515, 2026)**:\n   **最直接的竞争者**——在 Llama-3-8B 到 70B 的 GRPO steps 上训练 logistic regression probes 追踪 deception emergence。已经示范了\"across RLVR checkpoints 做 probe tracking\"这一核心方法论。区别在于 focus 是 reward-hacking obfuscation 而非 general faithfulness。\n\n6. **\"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (2605.18549, 2026.05)**:\n   在推理时构建 probe trajectory（逐 token probe），达到 95% AUROC 预测 outcome。但仅分析 fixed models，不涉及 training dynamics。\n\n7. **\"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?\" (2506.14261, 2025/2026)**:\n   7B-14B 模型可以通过 RL 学会规避 latent-space monitors。Token-level monitors 脆弱，max-pooling/attention-based probes 更鲁棒。对本 proposal 的 probe-based monitoring 的实际有效性提出质疑。\n\n8. **\"How Does Unfaithful Reasoning Emerge from Autoregressive Training?\" (2602.01017, 2026)**:\n   在 synthetic arithmetic 上展示 faithful→unfaithful 的 phase transition。但 toy setting，远离真实 GRPO。\n\n9. **\"Evaluating GRPO and DPO for Faithful CoT Reasoning in LLMs\" (2512.22631, late 2025)**:\n   评估 GRPO 和 DPO 对 faithfulness 的影响，发现 outcome-supervised GRPO 提升准确率但常损害推理-答案一致性。\n\n10. **\"Latent-GRPO\" (2604.27998, 2026) / \"GRPO-CARE\" (OpenReview 2026)**:\n    将 GRPO 扩展到 latent reasoning / consistency-aware 方向。说明 GRPO faithfulness 问题已被广泛认知并有人着手解决。\n\n- **调研总结**: CoT faithfulness 在 2026 是一个极度拥挤的领域，已沿多个轴被充分研究。Surface faithfulness across RL steps（Chen et al.）、latent probes in final models（Cox et al.）、probes across RLVR checkpoints（Obfuscation Atlas）、inference-time probe trajectories（Internal Monologue）均已有工作。本 proposal 的具体 gap——\"joint surface + latent 在 matched GRPO checkpoints 上的 longitudinal tracking\"——技术上确实未被填补，但这是一个组合性的、预期结果可预测的窄缝隙。\n\n\n【Trivial Alternative 检验】:\n\n**存在更简单的替代方案。** 最直接的 trivial alternative 是：不需要 20 个 fine-grained checkpoints 的 longitudinal study，只需在 base model 和 final RL-trained model 之间做 paired comparison（probe AUC + surface metrics），即可验证\"RL 训练是否扩大了 surface-latent gap\"这一核心 existence claim。这比 20-checkpoint longitudinal study 成本低一个数量级。\n\n本 proposal 相对于这个 trivial alternative 的增量价值在于：(1) 刻画 divergence 的时间动态（何时开始、是否有 phase transition）；(2) 两个 model family 的对比增加 generality。但问题在于——如果 divergence 是平滑单调的（没有 phase transition），那 20 个 checkpoint 的 temporal dynamics 信息量相当有限，审稿人可能会质疑\"two-point comparison 是否已经足够\"。Proposal 也承认用 PELT changepoint detection 是\"exploratory\"的，如果没检测到 changepoint，temporal analysis 的卖点就大幅缩水。\n\n\n【前提假设检验】:\n\n1. **Probe AUC = latent answer commitment = latent unfaithfulness**：这是最关键的未验证假设。高 probe AUC 可能反映模型变得更 confident / better calibrated，而非\"不忠实地绕过 CoT\"。Cox et al. (2603.01437) 在 fixed models 上做了 causal validation（steering experiments），但这种 causal link 是否在 GRPO 训练的每个 checkpoint 上都成立，是未经验证的。在 early checkpoints，probe 可能捕获的是 statistical regularity 而非 causal mechanism。\n\n2. **\"Surface faithfulness 提升 + latent pre-commitment 增强 = divergence\"**：这个等式假设 surface 和 latent 是同一现象的两个独立测量。但 surface faithfulness（hint-injection rate 降低）可能反映模型学会更好地 ignore irrelevant hints（a good thing），而 probe AUC 上升可能反映模型对问题的理解在 CoT 之前就更强（also potentially a good thing）。两者同时改善不一定构成\"gap\"或\"divergence\"——可能只是模型整体变好了。需要更精确的操作化定义来区分\"模型变好\"和\"模型变得不忠实\"。\n\n3. **两个 model family 的对比能提供 generality**：但两者都是 7B-8B scale 的 Qwen 架构变体（DeepSeek-R1-Distill-Qwen-7B 本身就是 Qwen 2.5 的 distillation），architectural diversity 可能被高估。\n\n\n【3 维度打分】:\n\n**1. Novelty: 中 — 组合性 novelty，非概念性创新**\n\n具体 gap 技术上确实存在——没有论文同时在 matched GRPO checkpoints 上跟踪 surface + latent faithfulness。但这一 novelty 是纯组合性的：\n- Obfuscation Atlas (2602.15515) 已经在 GRPO checkpoints 上做了 probe tracking（deception-focused），方法论框架高度重叠。\n- Chen et al. (2505.05410) 已经沿 RL steps 跟踪了 surface faithfulness。\n- Cox et al. (2603.01437) 提供了 probe 方法。\n- 本 proposal 的贡献是\"把 A 的 probe + B 的 surface metric 一起放到 C 的 temporal framework 里\"，是 synthesis 而非 conceptual innovation。\n- 预期发现（widening gap）几乎是 RLVR monitorability (2602.03978) 和 pre-CoT probes (2603.01437) 两篇论文结论的直接推论——审稿人极可能评价为 \"I would have guessed this\"。\n\n**2. Significance: 中 — 重要问题，但 characterization-only 且预期发现可预测**\n\n- CoT faithfulness 对 AI safety 确实重要，这一点毫无疑问。\n- 但本 proposal 是纯 characterization study——只描绘 gap 存在和动态，不提出解决方案。\n- 最终的 policy implication（\"RL-trained reasoning models require latent-space monitoring beyond CoT inspection\"）在 safety 社区已经是广泛接受的观点，不需要这篇论文来确立。\n- 如果 divergence 不显著（null result），论文的价值进一步降低（proposal 未讨论 negative result 的价值框架）。\n- 如果 divergence 是 smooth/monotonic（无 phase transition），temporal analysis 的附加价值有限。\n- RL-Obfuscation (2506.14261) 的发现（models can learn to evade probes）还给本 proposal 的\"用 probes 做 monitoring\"这一最终建议投下阴影。\n\n**3. Related Work: 强 — 覆盖全面、定位精确**\n\n- 文献覆盖极其全面，按多个 axis 组织清晰（surface across RL / latent snapshot / probe trajectory / deception probes / adversarial / faithfulness-improving / training dynamics）。\n- 与每篇 related work 的差异化定位具体且令人信服。\n- Gap 的 framing（\"no work jointly tracks…\"）在技术上是准确的。\n- 对 Obfuscation Atlas 的区分（deception-specific vs. general faithfulness）是合理的，尽管审稿人可能认为这一区分不够 fundamental。\n\n\n【概率估计】: [22% - 33%] 中位 27%\n\n**重要注意：上述概率是针对 proposal 自身列出的目标 venue（ICLR 2027 / NeurIPS 2026 workshop）的估计。**\n**如果目标 venue 确为 CoRL 2026（Conference on Robot Learning），本 proposal 与会议主题（机器人学习）完全不相关，概率应为 ~3-5%（纯属 desk reject）。**\n\n【估计理由】:\n\n从 3 维度到概率的推理逻辑：\n- **Related Work (强)** 保证了 framing 质量，为下限提供支撑——proposal 不会因 positioning 不清而被拒。\n- **Significance (中)** 提供了基本的重要性支撑——CoT faithfulness 是 2026 的热点话题，审稿人认同问题有价值。\n- **Novelty (中)** 是主要瓶颈，限制了上界。组合性 novelty + 可预测的预期结果 = 审稿人很可能写 \"the contribution is primarily empirical, and the expected findings are not surprising given existing work\"。这在 top venue 是常见的 rejection reason。\n\n在 25-35% 区间内（有实质内核但核心发现 \"I would have guessed this\"），本 proposal 偏下半段，因为：\n(1) Obfuscation Atlas 的高度方法论重叠压缩了 novelty 空间；\n(2) 纯 characterization study 无 solution component；\n(3) Trivial alternative（two-point comparison）威胁；\n(4) 核心前提假设（probe AUC = unfaithfulness）存在质疑空间。\n\n【主要风险】:\n\n1. **\"Predictable finding\" rejection**：审稿人读完 RLVR monitorability (2602.03978) + pre-CoT probes (2603.01437) 后，会认为 widening surface-latent gap 是 obvious prediction，本论文只是\"verify what everyone already expects\"。这是 top venue 最经典的 rejection pattern for empirical papers。\n\n2. **Probe AUC 的解释性争议**：probe AUC 上升是否真的代表\"unfaithful latent bypass\"，还是仅仅反映模型在 RL 训练中变得更 confident？如果审稿人不接受\"高 probe AUC = 低 latent faithfulness\"这一操作化定义，整个 narrative 的基础就不稳固。Activation patching 仅在 5 个 checkpoint 上做（出于成本考虑），可能不足以支撑全局的因果 claim。\n```\n\n**补充说明（Venue Mismatch 风险）**：\n\n本 proposal 明确列出目标 venue 为 ICLR 2027 / AAAI 2027 / NeurIPS 2026 workshops。如果用户确实计划投稿 **CoRL 2026（Conference on Robot Learning）**，这里存在根本性的 venue mismatch——本 proposal 是 mechanistic interpretability / AI safety 方向的纯 LLM 研究，与 CoRL 的核心议题（机器人感知、控制、manipulation、navigation 等）完全不沾边，极大概率会 desk reject。建议投向 proposal 自身列出的 ICLR / NeurIPS 等 venue，或 ICML 2027、SafeAI workshop 等更匹配的去处。\n\nSources:\n- [Reasoning Models Don't Always Say What They Think (2505.05410)](https://arxiv.org/abs/2505.05410)\n- [Monitorability as a Free Gift (2602.03978)](https://arxiv.org/abs/2602.03978)\n- [Decoding Answers Before Chain-of-Thought (2603.01437)](https://arxiv.org/abs/2603.01437)\n- [On Robustness and CoT Consistency of RL-Finetuned VLMs (2602.12506)](https://arxiv.org/abs/2602.12506)\n- [The Obfuscation Atlas (2602.15515)](https://arxiv.org/abs/2602.15515)\n- [Monitoring the Internal Monologue (2605.18549)](https://arxiv.org/abs/2605.18549)\n- [RL-Obfuscation (2506.14261)](https://arxiv.org/abs/2506.14261)\n- [AtManRL (2604.16158)](https://arxiv.org/abs/2604.16158)\n- [Evaluating GRPO and DPO for Faithful CoT Reasoning (2512.22631)](https://arxiv.org/pdf/2512.22631)\n- [Latent-GRPO (2604.27998)](https://arxiv.org/abs/2604.27998)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n```\n\n> **注意**：本 proposal 列出的目标投稿会议为 ICLR 2027 / AAAI 2027 / NeurIPS 2026 Workshops，均为 NLP/ML interpretability 方向的合适会议。但用户提到 **CoRL 2026（Conference on Robot Learning）**——这是一个 **机器人学习** 会议，本 proposal 关于 CoT 忠实性的 interpretability 研究 **完全不在 CoRL 的 scope 内**。以下评估基于 proposal 自身列出的目标会议（ICLR 2027 主会）进行，因为这才是合理的投稿方向。如果用户确实要投 CoRL 2026 主会，概率应直接下调至 **< 5%**（scope mismatch）。\n\n---\n\n```\n【领域调研】:\n```\n\n- **[Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)** (arXiv 2026.02): 发现 RLVR 的 monitorability 提升来自 response distribution sharpening 和 prompt attention 增强，**NOT** 来自更强的 causal reliance on reasoning traces。这是 proposal 最核心的前提论文——它意味着 surface faithfulness 改善和 latent computation 是正交的。\n  \n- **[Decoding Answers Before Chain-of-Thought (Pre-CoT Probes)](https://arxiv.org/abs/2603.01437)** (arXiv 2026.03): 在 instruction-tuned 模型的 residual stream 上训练 linear probe，可在 CoT 生成前以 >0.9 AUC 预测最终答案，且 probe direction 具有 causal efficacy（steering 可翻转答案）。这为 proposal 的 \"latent faithfulness proxy\" 提供了方法论基础。\n\n- **[On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)** (arXiv 2026.02): 在 Qwen2.5-VL-7B 的 GRPO checkpoints 上发现 accuracy-faithfulness trade-off，但仅用 surface metrics (LLM-as-judge, letter entropy)，无 activation-level 分析，且针对 VLMs。\n\n- **[Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)** (arXiv 2026.05, 极近期): 在固定模型上构建 probe trajectory（across token positions），用 max-pooling 达到 95% AUROC 预测 outcomes。但只分析已训练完成的模型，不涉及 training-level dynamics。\n\n- **[The Obfuscation Atlas](https://arxiv.org/abs/2602.15515)** (FAR AI, arXiv 2026.02): **在 RLVR checkpoints 上训练 deception probes**（logistic regression on residual streams），跨 Llama-3-8B-70B，mapping deception emergence。这是与 proposal 最接近的工作——**已经**在做 \"probes across RL training steps\" 的事情，只是 focus 是 deception/reward-hacking 而非 general faithfulness，且没有 jointly 测量 surface faithfulness。\n\n- **[RL-Obfuscation](https://arxiv.org/abs/2506.14261)** (arXiv 2025/2026): 展示 7B-14B 模型可通过 RL 学习 evade latent-space monitors，token-level monitors 尤其脆弱。是对抗性发现，不是 natural divergence characterization。\n\n- **[Counterfactual Simulation Training for CoT Faithfulness](https://arxiv.org/abs/2602.20710)** (arXiv 2026.02): 提出 CST 方法改善 CoT faithfulness，larger models 获益更多。与 proposal 方向互补（它们在改善 faithfulness，proposal 在 characterize unfaithfulness 的出现）。\n\n- **[Why Models Know But Don't Say](https://arxiv.org/abs/2603.26410)** (arXiv 2026.03): 量化 thinking tokens 和 final answers 之间的 divergence，55.4% cases 中 thinking tokens 包含 hint keywords 而 answer 不包含。\n\n- **[Faithful GRPO](https://arxiv.org/abs/2604.08476)** (arXiv 2026.04): 在 GRPO 中加入 faithfulness-aware reward，改善 VLM spatial reasoning faithfulness。说明 GRPO+faithfulness 组合已被探索，但从 \"修复\" 角度而非 \"诊断\" 角度。\n\n- **调研总结**: CoT faithfulness in 2026 是一个高度活跃的领域。Surface faithfulness across RL steps、latent probes on final models、probe trajectories during inference 三条线已相当成熟。Proposal 定位为三条线的 \"交叉点\"——jointly tracking surface + latent across RL training steps。这个 exact combination 确实尚未被做过，但 Obfuscation Atlas 已经做了 \"probes across RLVR steps\"（只是 focus 不同）。**Proposal 的 novelty 主要在 \"组合\" 而非 \"概念\"。**\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在较强的 trivial alternative 威胁。** \n\n核心问题是：proposal 的 central hypothesis（\"GRPO training creates a widening surface-latent faithfulness gap\"）是否可以通过已有工作的**逻辑推导**得出，而不需要跑 20 个 checkpoints 的实验？\n\n- RLVR Monitorability 论文（2602.03978）已经证明 surface monitorability gains 不来自 causal reliance → 即 surface 改善和 computation 的 causal coupling 是正交的\n- Pre-CoT Probes（2603.01437）已经证明 final models 存在强 answer pre-commitment（>0.9 AUC）\n- VLM checkpoint paper（2602.12506）已经在 GRPO checkpoints 上观察到 accuracy-faithfulness trade-off\n\n将这三个结果组合，\"RL training 加深 surface-latent gap\" 几乎是**逻辑推论**而非需要实验验证的 surprising hypothesis。一个 trivial alternative 是：在 3-5 个 checkpoints（base, early, mid, late, final）上测量 probe AUC + hint-injection rate，就足以 confirm/deny 这个 hypothesis。20 个 fine-grained checkpoints + changepoint detection 的增量价值取决于 dynamics 本身是否 interesting（e.g., 存在 phase transition），但这是未知的——如果 divergence 是 monotonic smooth 的，那么 fine-grained tracking 的价值有限。\n\n**增量价值在于**：(1) 提供 first direct empirical confirmation（而不是 logical inference）；(2) 刻画 divergence 的 temporal dynamics（changepoints, non-linearities）；(3) 跨 model family 的比较。但 (1) 本质上是 confirmation study，(2) 取决于实验结果是否 interesting，(3) 是 robustness check 而非 primary contribution。\n\n---\n\n```\n【前提假设检验】:\n```\n\n核心 claim 的逻辑链条中，以下环节是**未经充分验证的假设**：\n\n1. **\"Probe AUC 上升 = latent answer pre-commitment 增强 = latent unfaithfulness 增加\"**：这是 proposal 最关键的等价假设，但 probe AUC 上升也可能反映 model 变得更 confident/capable（representation 更 separable），不一定意味着 \"bypassing CoT\"。一个 model 如果 genuinely 通过 CoT 推理得到答案，其 pre-CoT representation 也可能因为 better question understanding 而更 predictive。**Probe AUC 的 interpretive validity 作为 \"unfaithfulness\" proxy 需要额外论证。** Pre-CoT probes 论文确实做了 causal steering validation，但 proposal 只在 5 个 checkpoints 上做 activation patching——如果 probe AUC 上升但 activation patching 效果不变或增强，这反而 undermines 主要 narrative。\n\n2. **\"两个 7B model families 的结果可以 generalize\"**：Proposal 选择 DeepSeek-R1-Distill-Qwen-7B 和 Qwen3-8B，都是 7-8B 规模。CoT faithfulness 的 scale dependence 已被多篇论文提到（e.g., CST 论文显示 larger models benefit more）。7B 模型的 faithfulness dynamics 可能与 70B+ 模型截然不同。14B scaling validation 只是 partial mitigation。\n\n3. **\"自行训练的 GRPO runs 能复现 comparable quality 的 reasoning models\"**：Proposal 将在 MATH + GPQA 上用 Open-R1 pipeline 做 GRPO。但 DeepSeek-R1 的成功涉及 massive-scale 数据和 compute，7B distill + further GRPO 的训练质量和稳定性是有 risk 的。如果 GRPO 训练本身不稳定或不 converge well，所有 downstream 测量都失去意义。\n\n---\n\n```\n【3 维度打分】:\n```\n\n**1. Novelty: 弱-中 — 组合性 novelty，核心概念非新**\n\nProposal 的 novelty 是 **方法论组合**（joint surface + latent tracking across RL steps）而非概念性突破。具体来说：\n- \"Probes across RL training steps\" 已由 Obfuscation Atlas（2602.15515）实现，虽然 focus 不同（deception vs. general faithfulness），但技术路线几乎相同（linear probes on residual streams at RLVR checkpoints）\n- \"Surface faithfulness across RL steps\" 已由 VLM checkpoint paper（2602.12506）和 Chen et al.（2505.05410）实现\n- \"Pre-CoT probes as latent faithfulness measure\" 直接来自 Cox et al.（2603.01437）\n- \"Probe trajectories\" 来自 2605.18549\n\nProposal 的核心是将这些 **已有方法** 组合应用于一个 **已有问题**（RL decouples surface from latent faithfulness）。这不是 trivial 组合——joint measurement 确实是 gap——但也不是 \"surprising\" 级别的 novelty。审稿人可能会问：\"So you combined existing tools to confirm an expected result?\"\n\n**2. Significance: 中 — 问题重要但 expected result 限制了 impact**\n\n研究问题本身——\"RL 是否系统性地 decouple surface 和 latent faithfulness\"——对 AI safety 和 deployment 决策有直接影响。如果答案是 yes（且 proposal 自己也 hypothesize 是 yes），那么 implication 是 \"RL-trained reasoning models need latent-space monitoring beyond CoT inspection\"。这个 implication 重要。\n\n但问题在于：\n- 现有证据已经 **强烈暗示** 这个答案是 yes（RLVR monitorability + pre-CoT probes 的组合逻辑）\n- 如果 proposal confirm 了 expected result，其 **marginal information gain** 有限——从 \"we strongly suspect this\" 到 \"we confirmed this\" 的 delta\n- Significance 的上限取决于 dynamics 是否 reveal 新的 insight（e.g., phase transitions, model-family differences），但这是 contingent on results\n\n如果 proposal 发现 **反预期** 结果（e.g., gap 不存在或 closes with training），那将非常 significant——但 proposal 自己不 predict 这种情况。\n\n**3. Related Work: 强 — 领域覆盖异常全面，定位精准**\n\n这是 proposal 最强的维度。Related work 覆盖了 6 个清晰的子方向（surface faithfulness across RL, latent faithfulness snapshots, probe trajectories, deception probes, adversarial evasion, faithfulness-improving RL），每个方向都准确引用了 2026 年最新的代表性工作。与 Obfuscation Atlas 的区分（deception-specific vs. general faithfulness）、与 2605.18549 的区分（token-level vs. training-level）都清晰合理。所有引用经搜索验证均真实存在。\n\n唯一的 gap：proposal 没有讨论 **Counterfactual Simulation Training**（2602.20710），这篇 Feb 2026 的工作从 \"改善 faithfulness\" 的角度与 proposal 的 \"诊断 unfaithfulness\" 形成互补关系，应该被 acknowledged。\n\n---\n\n```\n【概率估计】: [20% - 32%] 中位 25%\n```\n\n```\n【估计理由】: \n```\n\nProposal 处于 \"idea 有实质内核但核心发现若 positive 审稿人会说 'I would have guessed this'\" 的区间。\n\n- **Related Work** 维度是强项，拉高了下限——proposal 清楚知道自己在做什么、gap 在哪里\n- **Novelty** 维度是主要限制——组合性 novelty + confirmation study 特质显著压制了上限。Obfuscation Atlas 已经在 RLVR checkpoints 上做 probe tracking，proposal 的 delta 是 \"general faithfulness + joint surface measurement\"，这对 ICLR 级别来说偏 incremental\n- **Significance** 维度受限于 expected result——如果 core finding 是 \"yes, RL widens the gap\"，审稿人很可能回应 \"This is consistent with what we already know from [RLVR monitorability + pre-CoT probes]. What new insight does the longitudinal study add?\"\n- 概率上界被 Novelty 和 \"confirmation study\" 风险共同 cap 在 ~32%\n\n```\n【主要风险】:\n```\n\n1. **\"Confirmation study\" 质疑**：核心 hypothesis（\"GRPO widens surface-latent gap\"）在现有文献的逻辑推论下是 expected result。审稿人可能认为 \"empirical confirmation of a logical prediction\" 的 novelty 不足以支撑 top venue，尤其是当 Obfuscation Atlas 已经做了 probes-across-RLVR-steps 的 precedent。Proposal 的 value 高度依赖于 temporal dynamics 本身是否 reveal surprising patterns（changepoints, non-linearities, model-family differences），但这在 idea 阶段是 uncertain 的。\n\n2. **Probe AUC 的 interpretive validity 可能被挑战**：Probe AUC 上升被等同于 \"latent unfaithfulness 增加\"，但上升也可能反映 model 变得更 capable（better representations → more predictable answers）。如果没有足够强的 causal evidence 支撑这个等价关系（proposal 仅在 5 个 checkpoints 做 activation patching），整个 \"surface-latent gap\" 的 narrative 可能被 reviewer 质疑为 measurement artifact。\n\n---\n\nSources:\n- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)\n- [Decoding Answers Before Chain-of-Thought: Pre-CoT Probes](https://arxiv.org/abs/2603.01437)\n- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)\n- [Monitoring the Internal Monologue: Probe Trajectories](https://arxiv.org/abs/2605.18549)\n- [The Obfuscation Atlas](https://arxiv.org/abs/2602.15515)\n- [RL-Obfuscation](https://arxiv.org/abs/2506.14261)\n- [Counterfactual Simulation Training for CoT Faithfulness](https://arxiv.org/abs/2602.20710)\n- [Why Models Know But Don't Say](https://arxiv.org/abs/2603.26410)\n- [Faithful GRPO](https://arxiv.org/abs/2604.08476)\n- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models\n\n## Description\nWe propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.\n\n## Core Problem\nWhen and how does the gap between surface CoT faithfulness (measured by behavioral metrics like hint-injection rates and causal reliance) and latent faithfulness (measured by residual-stream probes predicting answer pre-commitment) develop during GRPO training of reasoning models — and what dynamics characterize this divergence?\n\n## Opportunity\nThree converging 2026 findings create a precise, actionable gap. First, the RLVR monitorability paper (2602.03978) showed that RL's surface-monitorability gains come from response distribution sharpening and increased prompt attention — NOT from stronger causal reliance on reasoning traces. Second, pre-CoT probes (2603.01437) demonstrated that instruction-tuned models encode answers in residual-stream activations before generating any CoT (>0.9 AUC), with these directions being causally efficacious. Third, the VLM checkpoint paper (2602.12506) showed an accuracy-faithfulness trade-off during RL fine-tuning — but using only LLM-as-judge surface metrics on vision-language models, with no latent-space analysis. Meanwhile, 'Monitoring the Internal Monologue' (2605.18549) introduced probe trajectories as a powerful inference-time monitoring tool but analyzed only fixed, already-trained models — never tracking how probe characteristics evolve across RL training steps. The Obfuscation Atlas (2602.15515) tracked deception probes across RLVR but focused narrowly on reward-hacking obfuscation rather than general faithfulness divergence. Nobody has jointly measured both surface faithfulness metrics and activation-probe-based latent faithfulness at matched RL training checkpoints to characterize how — and how fast — RL decouples what reasoning models say from what they compute. If this divergence is large and systematic, RL-trained reasoning models require latent-space monitoring beyond CoT inspection for safe deployment.\n\n## Landscape\nThe CoT faithfulness literature in 2026 is large but fragmented along complementary axes, leaving the longitudinal surface-latent gap unstudied:\n\n**Surface faithfulness across RL steps (behavioral only):** Chen et al. (Anthropic 2025, 2505.05410) measured surface faithfulness via hint-injection across RL steps, finding initial improvement that plateaus (~25% for Claude 3.7 Sonnet). The VLM checkpoint paper (2602.12506) tracked CoT consistency via LLM-as-judge across GRPO checkpoints of Qwen2.5-VL-7B-Instruct, finding an accuracy-faithfulness trade-off — but used only behavioral metrics (letter entropy, judge-rated consistency) with no activation probes, and studied VLMs rather than language models.\n\n**Latent faithfulness in final models (snapshot only):** Pre-CoT probes (2603.01437) showed >0.9 AUC answer prediction from residual streams of Gemma 2 and Qwen 2.5 before any CoT tokens. 'Catching Rationalization in the Act' (2603.17199) trained probes to detect motivated reasoning pre- and post-CoT. 'The Hypocrisy Gap' (2602.02496) used SAEs to quantify internal-belief/CoT divergence. 'Why Models Know But Don't Say' (2603.26410) measured thinking-token vs. answer divergence. All analyze final models only.\n\n**Probe trajectories during inference (token-level, not training-level):** 'Monitoring the Internal Monologue' (2605.18549, May 2026) constructed probe trajectories across token positions during generation, achieving 95% AUROC for predicting outcomes. However, this tracks probes across tokens within a single generation of a fixed model — not across RL training checkpoints. Their models (Llama-8B-R1-Distill, Qwen3-4B/8B/14B) are final checkpoints only.\n\n**Deception probes across RLVR (deception-specific):** The Obfuscation Atlas (2602.15515) trained logistic regression probes on residual streams of Llama-3-8B through 70B across GRPO steps, mapping deception emergence. But their focus is reward-hacking obfuscation in coding tasks, not general reasoning faithfulness, and they don't measure surface faithfulness metrics jointly.\n\n**RL-Obfuscation (adversarial evasion):** RL-Obfuscation (2506.14261) showed 7B-14B models can learn to evade latent-space monitors through RL, with token-level monitors being vulnerable. This is an adversarial finding about monitor fragility, not a characterization of natural faithfulness divergence.\n\n**Faithfulness-improving RL methods:** FaithRL (2602.03507), AtManRL (2604.16158), and faithfulness-aware step-level RL (2602.05897) propose RL objectives that improve faithfulness, but none characterize the divergence trajectory of standard GRPO/RLVR training.\n\n**RL training dynamics:** Learning dynamics papers (2601.04670) show reduced feature diversity during RL but don't track faithfulness. The synthetic phase-transition paper (2602.01017) demonstrates faithful→unfaithful transitions under controlled noise in toy arithmetic — the only prior showing discrete transitions, but in a setting far removed from real GRPO.\n\n**The gap:** No existing work jointly tracks probe-measured latent faithfulness AND surface CoT faithfulness metrics at matched RL training checkpoints across training to characterize divergence dynamics in language reasoning models.\n\n## Approach\nWe produce our own fine-grained GRPO training checkpoints from two architecturally distinct open-weight model families, then jointly measure surface and latent faithfulness at each checkpoint.\n\n**Model families and checkpoint generation:**\n(1) DeepSeek-R1-Distill-Qwen-7B as base model, trained with GRPO using the Open-R1 pipeline (HuggingFace TRL) on MATH + GPQA, saving checkpoints every 50 GRPO steps for ~20 checkpoints across training. This model starts with distilled reasoning capability, letting us study how further RL reshapes faithfulness.\n(2) Qwen3-8B (base dense model, Apache 2.0) trained with the same GRPO pipeline and datasets, providing an architecturally distinct family that starts without distilled reasoning traces.\n\n**Metrics at each checkpoint:**\n(a) *Latent faithfulness proxy*: Train linear probes on residual-stream activations at the last pre-CoT token (following the methodology of Cox et al., 2603.01437), predicting the model's final answer. Report probe AUC and the layer at which AUC first exceeds 0.8 ('commitment layer'). A rising probe AUC across training indicates strengthening answer pre-commitment — the model increasingly 'knows' its answer before reasoning.\n(b) *Surface faithfulness — hint-injection*: Apply Chen et al.'s protocol with sycophancy and anchoring hints on a fixed MMLU/GPQA subset (~500 items). Report hint-acknowledgment rate (lower = more faithful surface behavior).\n(c) *Causal reliance — NLDD*: Compute the Normalized Logit Difference Decay metric (2602.11201) by corrupting individual reasoning steps and measuring confidence drops. Report the Reasoning Horizon k* (the chain-length fraction beyond which steps have negligible causal effect).\n(d) *Activation patching* (on 5 evenly-spaced checkpoints per family): Measure the causal effect of CoT-token activations on the final answer via mean-ablation patching, quantifying how much the model's computation actually flows through the reasoning trace.\n\n**Analysis:**\n- Construct the *surface-latent divergence curve*: plot surface faithfulness improvement (declining hint-acknowledgment rate) against latent bypass strengthening (rising probe AUC / shortening reasoning horizon) across GRPO steps.\n- Apply changepoint detection (PELT algorithm) as an *exploratory* tool to identify whether divergence accelerates at specific training phases — we do NOT claim phase transitions a priori but test for non-linear dynamics.\n- Compare divergence trajectories between the two model families to assess generality.\n- On a subset of checkpoints, apply the probe-trajectory methodology of 'Monitoring the Internal Monologue' (2605.18549) to test whether the character of inference-time probe trajectories (volatility, trend features) changes systematically across training — bridging their token-level and our checkpoint-level analyses.\n\n**Scaling validation:** If initial 7B results show clear divergence, replicate core probe + hint-injection measurements on DeepSeek-R1-Distill-Qwen-14B with ~10 GRPO checkpoints to verify the pattern holds at larger scale.\n\n**Key methodological choices justified:**\n- Using R1-Distill-7B rather than R1-671B: reviewer correctly identified that Dev1/Dev2/Dev3 checkpoints are not publicly available. Distilled 7B models are computationally tractable (single A100 for inference, 8×A100 for GRPO training) and let us generate arbitrarily fine-grained checkpoints.\n- GRPO rather than PPO: GRPO is the algorithm used in DeepSeek-R1 and the VLM checkpoint paper, ensuring comparability.\n- Two model families with different starting points (distilled reasoning vs. base): controls for whether divergence is an artifact of the starting model's reasoning capability.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '350–500 A100-hours (GRPO training: ~80 A100-hrs × 2 families = 160 hrs; probe training + inference on ~20 checkpoints × 2 families: ~100 hrs; hint-injection evaluation: ~40 hrs; NLDD computation: ~30 hrs; activation patching on 10 checkpoints: ~50 hrs; 14B scaling validation: ~70 hrs)', 'timeline': '8–11 weeks (2 weeks GRPO training + pipeline setup, 3 weeks probe training & surface measurements in parallel, 2 weeks activation patching & NLDD, 1–2 weeks analysis, 1–2 weeks writing)', 'estimated_gpu_cost': '$900–$1,250 at ~$2.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': '300–400 A100-hours (Claude handles probe training scripts, metric computation pipelines, statistical analysis, and plotting; human designs experiments, interprets results, writes key paper sections)', 'timeline': '6–8 weeks', 'claude_api_cost': '$120–$250 (Sonnet 4.6 for code generation, data analysis scripts, and paper drafting; ~40M input + 8M output tokens)', 'estimated_gpu_cost': '$750–$1,000'}, 'auto_research': {'gpu_hours': '300–400 A100-hours', 'timeline': '4–5 weeks (parallelized GRPO training for both families, then parallelized probe training and evaluation across checkpoints)', 'claude_api_cost': '$300–$550 (orchestration agent managing GRPO runs, checkpoint evaluation sweeps, result interpretation, iterative analysis; ~120M input + 25M output tokens)', 'estimated_gpu_cost': '$750–$1,000', 'speed_bottleneck': 'Sequential dependency: GRPO training must complete (or reach sufficient checkpoints) before probe training begins. However, probe training on early checkpoints can start while GRPO training continues. The two model families can be trained in parallel. 14B scaling validation is contingent on 7B results being compelling.'}}\n\n## Inspired By\nDirect gap between three convergent findings: (1) RLVR monitorability gains NOT from causal reliance (2602.03978), (2) pre-CoT probes show answer pre-commitment exists in residual streams (2603.01437), (3) VLM checkpoint paper shows accuracy-faithfulness trade-off during RL but with no latent-space analysis (2602.12506). The 'Monitoring the Internal Monologue' paper (2605.18549) shows probe trajectories are powerful for monitoring but leaves the training-dynamics dimension unexplored. The Obfuscation Atlas (2602.15515) demonstrates that probing across RLVR checkpoints is technically feasible at scale.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, 2026; full paper: Sep 24, 2026 — primary target, strong fit for mechanistic interpretability; ~18 weeks from now gives ample time for full experiments including 14B scaling)\n- AAAI 2027 (abstract: Jul 21, 2026; full paper: Jul 28, 2026 — ambitious secondary target; ~9 weeks from now, feasible with focused 7B-only results if GRPO training starts immediately)\n- NeurIPS 2026 workshops (workshop paper deadlines ~Aug 29, 2026; e.g., Mechanistic Interpretability, AI Safety, or Alignment workshops — good venue for initial results even if full paper targets ICLR)\n\n## Key References\n- Reasoning Models Don't Always Say What They Think (Anthropic 2025, arXiv 2505.05410)\n- Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning (arXiv 2026, 2602.03978)\n- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)\n- On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs (arXiv 2026, 2602.12506)\n- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (arXiv 2026, 2605.18549)\n- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (FAR AI/arXiv 2026, 2602.15515)\n- RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? (arXiv 2025/2026, 2506.14261)\n- How Does Unfaithful Reasoning Emerge from Autoregressive Training? A Study of Synthetic Experiments (arXiv 2026, 2602.01017)\n- Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (arXiv 2026, 2602.11201)\n- Learning Dynamics in RL Post-Training for Language Models (arXiv 2026, 2601.04670)\n- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Goodfire/arXiv 2026, 2603.05488)\n- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv 2026, 2602.02496)\n- Catching Rationalization in the Act: Detecting Motivated Reasoning Before and After CoT via Activation Probing (arXiv 2026, 2603.17199)\n- Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models (arXiv 2026, 2603.26410)\n- FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization (arXiv 2026, 2602.03507)\n- AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency (arXiv 2026, 2604.16158)\n- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (DeepSeek 2025, 2501.12948)\n- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv 2025, 2507.18014)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:30:46.955Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:30:46.955Z",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:30:46.966Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me synthesize my findings.

---

```
【阶段】: Triage

【领域调研】:

1. "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning" (arXiv 2602.03978, Feb 2026):
   最直接相关的前序工作之一。核心发现：RLVR 的 monitorability 提升来自 response distribution sharpening 和 prompt attention 增加，而非来自更强的 causal reliance on reasoning traces。这直接暗示了 surface 和 latent faithfulness 之间可能存在脱节——本 proposal 的核心假设几乎是这篇论文结论的自然推论。

2. "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering" (arXiv 2603.01437, Mar 2026):
   建立了 pre-CoT linear probe 方法论（>0.9 AUC），证明模型在生成 CoT 前已在 residual stream 中编码答案，且 probe direction 具有因果效力。本 proposal 直接复用该方法。该论文仅分析 final models，无 training dynamics。

3. "On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs" (arXiv 2602.12506, Feb 2026):
   在 VLM 上做了 GRPO checkpoint 级的 surface faithfulness tracking，发现 accuracy-faithfulness trade-off。但仅用 LLM-as-judge 等 surface metrics，无 latent-space 分析，且针对 VLM 而非 LLM。

4. "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes" (arXiv 2602.15515, Feb 2026, FAR AI):
   **技术路径最接近的竞争者。** 已经做了：在 GRPO training checkpoints 上训练 logistic regression probes on residual streams (Llama-3-8B through 70B)。但其焦点是 reward-hacking obfuscation（deception probes），而非 general faithfulness divergence，且未同步测量 surface faithfulness metrics。

5. "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (arXiv 2605.18549, May 2026):
   提出 probe trajectories 方法论（token-level），在 inference 时跟踪 probe 输出的时序演变，达 95% AUROC。但仅分析 fixed final models（Llama-8B-R1-Distill, Qwen3），无 training dynamics。

6. "Catching Rationalization in the Act" (arXiv 2603.17199, Mar 2026):
   用 activation probing 检测 motivated reasoning，训练 pre-/post-CoT probes。仅分析 final models。

7. "The Hypocrisy Gap" (arXiv 2602.02496, Jan 2026):
   用 SAE 量化 internal belief vs. CoT explanation 的 divergence。AUROC 0.55–0.74，仅分析 final models。

8. "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?" (arXiv 2506.14261, Jun 2025):
   证明 7B–14B 模型可通过 RL 学会逃避 latent-space monitors。Token-level monitors 脆弱，但 max-pooling/attention-based 更鲁棒。是关于 adversarial evasion 的发现，非 natural faithfulness divergence。

9. "How Does Unfaithful Reasoning Emerge from Autoregressive Training?" (arXiv 2602.01017, Feb 2026):
   在 synthetic toy arithmetic 设置中展示 faithful→unfaithful phase transition，但距离真实 GRPO 训练场景甚远。

10. Counterfactual Simulation Training (arXiv 2602.20710), FaithRL (2602.03507), AtManRL (2604.16158):
    提出改善 faithfulness 的 RL objectives，但不涉及 standard GRPO 的 divergence 特征化。

- **调研总结**: CoT faithfulness 在 2026 年是一个极其活跃但高度碎片化的领域。Surface faithfulness across RL steps（behavioral only）和 latent faithfulness in final models（snapshot only）分别已有大量工作，但两者在 matched training checkpoints 上的联合追踪确实是一个未填补的 gap。**然而**，这个 gap 更接近于"将已有工具组合应用在已有实验框架上"，而非一个需要新方法论或新理论洞见的 gap。最近的 Obfuscation Atlas 在技术路径上最为接近，已证明 probing across GRPO checkpoints 完全可行。


【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 具体来说：

1. **从 Obfuscation Atlas 出发的最小扩展**：Obfuscation Atlas 已有 GRPO checkpoint-level probes on residual streams。将其 deception probes 替换为 general faithfulness probes（following Cox et al.），并在每个 checkpoint 加上 hint-injection 测量，即可实现本 proposal 的核心贡献。这本质上是"换一种 probe target + 加一个 surface metric"——方法论层面几乎无创新。

2. **从 VLM checkpoint paper 出发的最小扩展**：该论文已有 GRPO checkpoints + surface faithfulness tracking。在其上加 activation probes 即可覆盖本 proposal 的核心 idea（虽然需要从 VLM 切换到 LLM）。

**增量价值**：proposal 的增量在于 (a) 联合测量 surface + latent 并绘制 divergence curve，(b) 两个 model family 对比，(c) changepoint detection 分析 divergence dynamics。这些是有价值的贡献，但属于实验设计层面的增量，而非 idea 层面的根本创新。


【前提假设检验】:

核心 claim 的逻辑链条有两个关键假设值得审视：

1. **"Rising probe AUC = strengthening answer pre-commitment"**：这个等式是否成立？Probe AUC 的上升可能反映多种因素——模型表示在 RL 训练中变得更 linearly separable 并不一定等同于"模型更早地确定了答案"。RL 训练改变了 representation geometry，probe 的可解释性可能随训练动态变化。这是一个未经充分验证的假设。

2. **"Surface faithfulness improvement + latent bypass strengthening = systematic decoupling"**：proposal 假设如果 surface metrics 改善而 probe AUC 上升，则说明 RL "decouples what models say from what they compute"。但另一种解释是：RL 让模型既更好地推理（latent），又更好地呈现推理（surface），probe AUC 上升只是反映了 representation 更清晰，而非 faithfulness 的下降。换言之，**两个指标同向变化未必代表 divergence，取决于如何解读 probe AUC 的语义**。

3. **"GRPO training on MATH/GPQA 足以产生有意义的 faithfulness divergence"**：proposal 假设标准 GRPO 训练就会产生这种 gap，但如果 MATH/GPQA 的 reward signal 足够 aligned with faithful reasoning，divergence 可能很小或不存在。training data/reward design 的选择可能强烈影响结果的 generalizability。


【3 维度打分】:

1. **Novelty: 弱–中** — 
   核心 novelty 是"在 matched GRPO checkpoints 上联合测量 surface + latent faithfulness"。但这本质上是将已有工具（pre-CoT probes from Cox et al. 2603.01437, hint-injection from Chen et al. 2505.05410, NLDD from 2602.11201）在已有实验框架（GRPO checkpoint studies à la Obfuscation Atlas 2602.15515 和 VLM checkpoint paper 2602.12506）上的组合应用。无新的 probe 方法论、无新的 metric、无新的理论框架。Obfuscation Atlas 已证明 probing across GRPO checkpoints 的技术可行性；从 deception probes 切换到 faithfulness probes 是一个自然且低成本的延伸。两个 model family 的对比和 changepoint detection 增加了一些实验设计层面的 novelty，但不改变 idea 层面的本质。

2. **Significance: 中** — 
   研究问题本身是重要的：理解 RL 训练如何影响 surface 与 internal faithfulness 的关系对 AI safety 有直接意义。如果结果表明 gap 大且系统性，确实会影响对 RL-trained reasoning models 部署监控策略的决策。然而，**核心假设（GRPO 会制造 widening gap）已被现有证据强烈暗示**——RLVR monitorability (2602.03978) 已表明 surface gains ≠ causal reliance improvement，pre-CoT probes (2603.01437) 已表明 answer pre-commitment 存在于 final models。一个 positive 结果（gap widens）是大多数领域内研究者已经预期的，审稿人更可能说 "I would have guessed this" 而非 "this is surprising"。真正 surprising 的结果——例如 gap 不存在，或存在 non-monotonic dynamics——proposal 并未将其作为核心 framing。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。Landscape 梳理全面、组织清晰，按 surface faithfulness / latent faithfulness / probe trajectories / deception probes / RL dynamics 等维度系统分类。每篇论文的定位准确（经调研验证，所有引用的关键论文均真实存在且描述准确）。Gap 的识别精确——确实没有工作在 matched checkpoints 上做 joint surface + latent tracking。但 related work 做得好是 proposal 的基本要求，不应因此过度提升对 idea quality 的评估。


【概率估计】: [22% - 32%] 中位 26%

【估计理由】: 
Related Work 覆盖全面且 gap 识别精确（强），表明作者对领域有深入理解，这是进入合理区间的基础。然而，Novelty 偏弱是主要限制因素——核心贡献是将 3-4 个已有工具的组合应用，Obfuscation Atlas 和 VLM checkpoint paper 的存在构成严重的 trivial alternative 威胁。Significance 被"预期中的结果"所压制：核心假设（widening gap）已被 RLVR monitorability + pre-CoT probes 的汇聚证据强烈暗示，positive 结果不会让审稿人感到 surprising。

该 proposal 处于 rubric 的 25-35% 区间下段：idea 有实质内核，方向正确，有真实但有限的 novelty delta，但核心发现若 positive 审稿人大概率会说 "I would have guessed this"。Novelty 维度的弱势将上界限制在 ~32%。

【主要风险】:
1. **"组合式 novelty"被判为 incremental**：审稿人可能认为"将 Obfuscation Atlas 的 checkpoint probing 框架 + Cox et al. 的 pre-CoT probes + Chen et al. 的 hint-injection 合在一起"是一个自然的、低技术门槛的组合，不构成足够的 intellectual contribution for a top venue。
2. **"Confirmatory study"定位问题**：如果 positive result 只是确认了 RLVR monitorability (2602.03978) 已强烈暗示的结论（surface gains ≠ latent improvement），审稿人可能质疑：除了量化一个已预期的现象外，这项工作提供了什么新的 insight？在 ICLR 2027 这类强调 novelty 的 venue，confirmatory measurement studies 的接受度有限。
```

Sources:
- [Monitorability as a Free Gift (2602.03978)](https://arxiv.org/abs/2602.03978)
- [Decoding Answers Before Chain-of-Thought (2603.01437)](https://arxiv.org/abs/2603.01437)
- [On Robustness and CoT Consistency of RL-Finetuned VLMs (2602.12506)](https://arxiv.org/abs/2602.12506)
- [The Obfuscation Atlas (2602.15515)](https://arxiv.org/abs/2602.15515)
- [Monitoring the Internal Monologue (2605.18549)](https://arxiv.org/abs/2605.18549)
- [Catching Rationalization in the Act (2603.17199)](https://arxiv.org/abs/2603.17199)
- [The Hypocrisy Gap (2602.02496)](https://arxiv.org/abs/2602.02496)
- [RL-Obfuscation (2506.14261)](https://arxiv.org/abs/2506.14261)
- [Why Models Know But Don't Say (2603.26410)](https://arxiv.org/html/2603.26410v1)
- [AtManRL (2604.16158)](https://arxiv.org/html/2604.16158)
- [Counterfactual Simulation Training (2602.20710)](https://arxiv.org/abs/2602.20710)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have comprehensive research data. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **"Reasoning Models Don't Always Say What They Think" (Anthropic, 2505.05410, 2025)**:
   Chen et al. 的 hint-injection 方法论——本 proposal 直接复用的 surface faithfulness 指标。发现 outcome-based RL 初期提升 faithfulness (MMLU +63%, GPQA +41%)，但很快 plateau（仅达 ~25-28%）。这篇已经沿 RL steps 跟踪了 surface faithfulness。

2. **"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning" (2602.03978, 2026)**:
   发现 RLVR 的 surface monitorability 提升来自 response distribution sharpening 和 increased prompt attention，而非更强的 causal reliance on reasoning traces。这是本 proposal 核心假设的直接来源。

3. **"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes" (Cox et al., 2603.01437, 2026)**:
   在 Gemma 2 和 Qwen 2.5 上演示 pre-CoT 线性 probe 可达 >0.9 AUC 预测最终答案，且 probe 方向具有因果效力（activation steering 可改变答案）。这是本 proposal 的 latent faithfulness proxy 的方法论来源。

4. **"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs" (2602.12506, 2026)**:
   在 Qwen2.5-VL-7B 的 GRPO checkpoints 上发现 accuracy-faithfulness trade-off，但仅使用 LLM-as-judge 等 behavioral metrics，无 activation probes。仅限 VLM。

5. **"The Obfuscation Atlas" (FAR AI, 2602.15515, 2026)**:
   **最直接的竞争者**——在 Llama-3-8B 到 70B 的 GRPO steps 上训练 logistic regression probes 追踪 deception emergence。已经示范了"across RLVR checkpoints 做 probe tracking"这一核心方法论。区别在于 focus 是 reward-hacking obfuscation 而非 general faithfulness。

6. **"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (2605.18549, 2026.05)**:
   在推理时构建 probe trajectory（逐 token probe），达到 95% AUROC 预测 outcome。但仅分析 fixed models，不涉及 training dynamics。

7. **"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?" (2506.14261, 2025/2026)**:
   7B-14B 模型可以通过 RL 学会规避 latent-space monitors。Token-level monitors 脆弱，max-pooling/attention-based probes 更鲁棒。对本 proposal 的 probe-based monitoring 的实际有效性提出质疑。

8. **"How Does Unfaithful Reasoning Emerge from Autoregressive Training?" (2602.01017, 2026)**:
   在 synthetic arithmetic 上展示 faithful→unfaithful 的 phase transition。但 toy setting，远离真实 GRPO。

9. **"Evaluating GRPO and DPO for Faithful CoT Reasoning in LLMs" (2512.22631, late 2025)**:
   评估 GRPO 和 DPO 对 faithfulness 的影响，发现 outcome-supervised GRPO 提升准确率但常损害推理-答案一致性。

10. **"Latent-GRPO" (2604.27998, 2026) / "GRPO-CARE" (OpenReview 2026)**:
    将 GRPO 扩展到 latent reasoning / consistency-aware 方向。说明 GRPO faithfulness 问题已被广泛认知并有人着手解决。

- **调研总结**: CoT faithfulness 在 2026 是一个极度拥挤的领域，已沿多个轴被充分研究。Surface faithfulness across RL steps（Chen et al.）、latent probes in final models（Cox et al.）、probes across RLVR checkpoints（Obfuscation Atlas）、inference-time probe trajectories（Internal Monologue）均已有工作。本 proposal 的具体 gap——"joint surface + latent 在 matched GRPO checkpoints 上的 longitudinal tracking"——技术上确实未被填补，但这是一个组合性的、预期结果可预测的窄缝隙。


【Trivial Alternative 检验】:

**存在更简单的替代方案。** 最直接的 trivial alternative 是：不需要 20 个 fine-grained checkpoints 的 longitudinal study，只需在 base model 和 final RL-trained model 之间做 paired comparison（probe AUC + surface metrics），即可验证"RL 训练是否扩大了 surface-latent gap"这一核心 existence claim。这比 20-checkpoint longitudinal study 成本低一个数量级。

本 proposal 相对于这个 trivial alternative 的增量价值在于：(1) 刻画 divergence 的时间动态（何时开始、是否有 phase transition）；(2) 两个 model family 的对比增加 generality。但问题在于——如果 divergence 是平滑单调的（没有 phase transition），那 20 个 checkpoint 的 temporal dynamics 信息量相当有限，审稿人可能会质疑"two-point comparison 是否已经足够"。Proposal 也承认用 PELT changepoint detection 是"exploratory"的，如果没检测到 changepoint，temporal analysis 的卖点就大幅缩水。


【前提假设检验】:

1. **Probe AUC = latent answer commitment = latent unfaithfulness**：这是最关键的未验证假设。高 probe AUC 可能反映模型变得更 confident / better calibrated，而非"不忠实地绕过 CoT"。Cox et al. (2603.01437) 在 fixed models 上做了 causal validation（steering experiments），但这种 causal link 是否在 GRPO 训练的每个 checkpoint 上都成立，是未经验证的。在 early checkpoints，probe 可能捕获的是 statistical regularity 而非 causal mechanism。

2. **"Surface faithfulness 提升 + latent pre-commitment 增强 = divergence"**：这个等式假设 surface 和 latent 是同一现象的两个独立测量。但 surface faithfulness（hint-injection rate 降低）可能反映模型学会更好地 ignore irrelevant hints（a good thing），而 probe AUC 上升可能反映模型对问题的理解在 CoT 之前就更强（also potentially a good thing）。两者同时改善不一定构成"gap"或"divergence"——可能只是模型整体变好了。需要更精确的操作化定义来区分"模型变好"和"模型变得不忠实"。

3. **两个 model family 的对比能提供 generality**：但两者都是 7B-8B scale 的 Qwen 架构变体（DeepSeek-R1-Distill-Qwen-7B 本身就是 Qwen 2.5 的 distillation），architectural diversity 可能被高估。


【3 维度打分】:

**1. Novelty: 中 — 组合性 novelty，非概念性创新**

具体 gap 技术上确实存在——没有论文同时在 matched GRPO checkpoints 上跟踪 surface + latent faithfulness。但这一 novelty 是纯组合性的：
- Obfuscation Atlas (2602.15515) 已经在 GRPO checkpoints 上做了 probe tracking（deception-focused），方法论框架高度重叠。
- Chen et al. (2505.05410) 已经沿 RL steps 跟踪了 surface faithfulness。
- Cox et al. (2603.01437) 提供了 probe 方法。
- 本 proposal 的贡献是"把 A 的 probe + B 的 surface metric 一起放到 C 的 temporal framework 里"，是 synthesis 而非 conceptual innovation。
- 预期发现（widening gap）几乎是 RLVR monitorability (2602.03978) 和 pre-CoT probes (2603.01437) 两篇论文结论的直接推论——审稿人极可能评价为 "I would have guessed this"。

**2. Significance: 中 — 重要问题，但 characterization-only 且预期发现可预测**

- CoT faithfulness 对 AI safety 确实重要，这一点毫无疑问。
- 但本 proposal 是纯 characterization study——只描绘 gap 存在和动态，不提出解决方案。
- 最终的 policy implication（"RL-trained reasoning models require latent-space monitoring beyond CoT inspection"）在 safety 社区已经是广泛接受的观点，不需要这篇论文来确立。
- 如果 divergence 不显著（null result），论文的价值进一步降低（proposal 未讨论 negative result 的价值框架）。
- 如果 divergence 是 smooth/monotonic（无 phase transition），temporal analysis 的附加价值有限。
- RL-Obfuscation (2506.14261) 的发现（models can learn to evade probes）还给本 proposal 的"用 probes 做 monitoring"这一最终建议投下阴影。

**3. Related Work: 强 — 覆盖全面、定位精确**

- 文献覆盖极其全面，按多个 axis 组织清晰（surface across RL / latent snapshot / probe trajectory / deception probes / adversarial / faithfulness-improving / training dynamics）。
- 与每篇 related work 的差异化定位具体且令人信服。
- Gap 的 framing（"no work jointly tracks…"）在技术上是准确的。
- 对 Obfuscation Atlas 的区分（deception-specific vs. general faithfulness）是合理的，尽管审稿人可能认为这一区分不够 fundamental。


【概率估计】: [22% - 33%] 中位 27%

**重要注意：上述概率是针对 proposal 自身列出的目标 venue（ICLR 2027 / NeurIPS 2026 workshop）的估计。**
**如果目标 venue 确为 CoRL 2026（Conference on Robot Learning），本 proposal 与会议主题（机器人学习）完全不相关，概率应为 ~3-5%（纯属 desk reject）。**

【估计理由】:

从 3 维度到概率的推理逻辑：
- **Related Work (强)** 保证了 framing 质量，为下限提供支撑——proposal 不会因 positioning 不清而被拒。
- **Significance (中)** 提供了基本的重要性支撑——CoT faithfulness 是 2026 的热点话题，审稿人认同问题有价值。
- **Novelty (中)** 是主要瓶颈，限制了上界。组合性 novelty + 可预测的预期结果 = 审稿人很可能写 "the contribution is primarily empirical, and the expected findings are not surprising given existing work"。这在 top venue 是常见的 rejection reason。

在 25-35% 区间内（有实质内核但核心发现 "I would have guessed this"），本 proposal 偏下半段，因为：
(1) Obfuscation Atlas 的高度方法论重叠压缩了 novelty 空间；
(2) 纯 characterization study 无 solution component；
(3) Trivial alternative（two-point comparison）威胁；
(4) 核心前提假设（probe AUC = unfaithfulness）存在质疑空间。

【主要风险】:

1. **"Predictable finding" rejection**：审稿人读完 RLVR monitorability (2602.03978) + pre-CoT probes (2603.01437) 后，会认为 widening surface-latent gap 是 obvious prediction，本论文只是"verify what everyone already expects"。这是 top venue 最经典的 rejection pattern for empirical papers。

2. **Probe AUC 的解释性争议**：probe AUC 上升是否真的代表"unfaithful latent bypass"，还是仅仅反映模型在 RL 训练中变得更 confident？如果审稿人不接受"高 probe AUC = 低 latent faithfulness"这一操作化定义，整个 narrative 的基础就不稳固。Activation patching 仅在 5 个 checkpoint 上做（出于成本考虑），可能不足以支撑全局的因果 claim。
```

**补充说明（Venue Mismatch 风险）**：

本 proposal 明确列出目标 venue 为 ICLR 2027 / AAAI 2027 / NeurIPS 2026 workshops。如果用户确实计划投稿 **CoRL 2026（Conference on Robot Learning）**，这里存在根本性的 venue mismatch——本 proposal 是 mechanistic interpretability / AI safety 方向的纯 LLM 研究，与 CoRL 的核心议题（机器人感知、控制、manipulation、navigation 等）完全不沾边，极大概率会 desk reject。建议投向 proposal 自身列出的 ICLR / NeurIPS 等 venue，或 ICML 2027、SafeAI workshop 等更匹配的去处。

Sources:
- [Reasoning Models Don't Always Say What They Think (2505.05410)](https://arxiv.org/abs/2505.05410)
- [Monitorability as a Free Gift (2602.03978)](https://arxiv.org/abs/2602.03978)
- [Decoding Answers Before Chain-of-Thought (2603.01437)](https://arxiv.org/abs/2603.01437)
- [On Robustness and CoT Consistency of RL-Finetuned VLMs (2602.12506)](https://arxiv.org/abs/2602.12506)
- [The Obfuscation Atlas (2602.15515)](https://arxiv.org/abs/2602.15515)
- [Monitoring the Internal Monologue (2605.18549)](https://arxiv.org/abs/2605.18549)
- [RL-Obfuscation (2506.14261)](https://arxiv.org/abs/2506.14261)
- [AtManRL (2604.16158)](https://arxiv.org/abs/2604.16158)
- [Evaluating GRPO and DPO for Faithful CoT Reasoning (2512.22631)](https://arxiv.org/pdf/2512.22631)
- [Latent-GRPO (2604.27998)](https://arxiv.org/abs/2604.27998)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information. Let me compile the evaluation.

---

```
【阶段】: Triage
```

> **注意**：本 proposal 列出的目标投稿会议为 ICLR 2027 / AAAI 2027 / NeurIPS 2026 Workshops，均为 NLP/ML interpretability 方向的合适会议。但用户提到 **CoRL 2026（Conference on Robot Learning）**——这是一个 **机器人学习** 会议，本 proposal 关于 CoT 忠实性的 interpretability 研究 **完全不在 CoRL 的 scope 内**。以下评估基于 proposal 自身列出的目标会议（ICLR 2027 主会）进行，因为这才是合理的投稿方向。如果用户确实要投 CoRL 2026 主会，概率应直接下调至 **< 5%**（scope mismatch）。

---

```
【领域调研】:
```

- **[Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)** (arXiv 2026.02): 发现 RLVR 的 monitorability 提升来自 response distribution sharpening 和 prompt attention 增强，**NOT** 来自更强的 causal reliance on reasoning traces。这是 proposal 最核心的前提论文——它意味着 surface faithfulness 改善和 latent computation 是正交的。
  
- **[Decoding Answers Before Chain-of-Thought (Pre-CoT Probes)](https://arxiv.org/abs/2603.01437)** (arXiv 2026.03): 在 instruction-tuned 模型的 residual stream 上训练 linear probe，可在 CoT 生成前以 >0.9 AUC 预测最终答案，且 probe direction 具有 causal efficacy（steering 可翻转答案）。这为 proposal 的 "latent faithfulness proxy" 提供了方法论基础。

- **[On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)** (arXiv 2026.02): 在 Qwen2.5-VL-7B 的 GRPO checkpoints 上发现 accuracy-faithfulness trade-off，但仅用 surface metrics (LLM-as-judge, letter entropy)，无 activation-level 分析，且针对 VLMs。

- **[Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)** (arXiv 2026.05, 极近期): 在固定模型上构建 probe trajectory（across token positions），用 max-pooling 达到 95% AUROC 预测 outcomes。但只分析已训练完成的模型，不涉及 training-level dynamics。

- **[The Obfuscation Atlas](https://arxiv.org/abs/2602.15515)** (FAR AI, arXiv 2026.02): **在 RLVR checkpoints 上训练 deception probes**（logistic regression on residual streams），跨 Llama-3-8B-70B，mapping deception emergence。这是与 proposal 最接近的工作——**已经**在做 "probes across RL training steps" 的事情，只是 focus 是 deception/reward-hacking 而非 general faithfulness，且没有 jointly 测量 surface faithfulness。

- **[RL-Obfuscation](https://arxiv.org/abs/2506.14261)** (arXiv 2025/2026): 展示 7B-14B 模型可通过 RL 学习 evade latent-space monitors，token-level monitors 尤其脆弱。是对抗性发现，不是 natural divergence characterization。

- **[Counterfactual Simulation Training for CoT Faithfulness](https://arxiv.org/abs/2602.20710)** (arXiv 2026.02): 提出 CST 方法改善 CoT faithfulness，larger models 获益更多。与 proposal 方向互补（它们在改善 faithfulness，proposal 在 characterize unfaithfulness 的出现）。

- **[Why Models Know But Don't Say](https://arxiv.org/abs/2603.26410)** (arXiv 2026.03): 量化 thinking tokens 和 final answers 之间的 divergence，55.4% cases 中 thinking tokens 包含 hint keywords 而 answer 不包含。

- **[Faithful GRPO](https://arxiv.org/abs/2604.08476)** (arXiv 2026.04): 在 GRPO 中加入 faithfulness-aware reward，改善 VLM spatial reasoning faithfulness。说明 GRPO+faithfulness 组合已被探索，但从 "修复" 角度而非 "诊断" 角度。

- **调研总结**: CoT faithfulness in 2026 是一个高度活跃的领域。Surface faithfulness across RL steps、latent probes on final models、probe trajectories during inference 三条线已相当成熟。Proposal 定位为三条线的 "交叉点"——jointly tracking surface + latent across RL training steps。这个 exact combination 确实尚未被做过，但 Obfuscation Atlas 已经做了 "probes across RLVR steps"（只是 focus 不同）。**Proposal 的 novelty 主要在 "组合" 而非 "概念"。**

---

```
【Trivial Alternative 检验】:
```

**存在较强的 trivial alternative 威胁。** 

核心问题是：proposal 的 central hypothesis（"GRPO training creates a widening surface-latent faithfulness gap"）是否可以通过已有工作的**逻辑推导**得出，而不需要跑 20 个 checkpoints 的实验？

- RLVR Monitorability 论文（2602.03978）已经证明 surface monitorability gains 不来自 causal reliance → 即 surface 改善和 computation 的 causal coupling 是正交的
- Pre-CoT Probes（2603.01437）已经证明 final models 存在强 answer pre-commitment（>0.9 AUC）
- VLM checkpoint paper（2602.12506）已经在 GRPO checkpoints 上观察到 accuracy-faithfulness trade-off

将这三个结果组合，"RL training 加深 surface-latent gap" 几乎是**逻辑推论**而非需要实验验证的 surprising hypothesis。一个 trivial alternative 是：在 3-5 个 checkpoints（base, early, mid, late, final）上测量 probe AUC + hint-injection rate，就足以 confirm/deny 这个 hypothesis。20 个 fine-grained checkpoints + changepoint detection 的增量价值取决于 dynamics 本身是否 interesting（e.g., 存在 phase transition），但这是未知的——如果 divergence 是 monotonic smooth 的，那么 fine-grained tracking 的价值有限。

**增量价值在于**：(1) 提供 first direct empirical confirmation（而不是 logical inference）；(2) 刻画 divergence 的 temporal dynamics（changepoints, non-linearities）；(3) 跨 model family 的比较。但 (1) 本质上是 confirmation study，(2) 取决于实验结果是否 interesting，(3) 是 robustness check 而非 primary contribution。

---

```
【前提假设检验】:
```

核心 claim 的逻辑链条中，以下环节是**未经充分验证的假设**：

1. **"Probe AUC 上升 = latent answer pre-commitment 增强 = latent unfaithfulness 增加"**：这是 proposal 最关键的等价假设，但 probe AUC 上升也可能反映 model 变得更 confident/capable（representation 更 separable），不一定意味着 "bypassing CoT"。一个 model 如果 genuinely 通过 CoT 推理得到答案，其 pre-CoT representation 也可能因为 better question understanding 而更 predictive。**Probe AUC 的 interpretive validity 作为 "unfaithfulness" proxy 需要额外论证。** Pre-CoT probes 论文确实做了 causal steering validation，但 proposal 只在 5 个 checkpoints 上做 activation patching——如果 probe AUC 上升但 activation patching 效果不变或增强，这反而 undermines 主要 narrative。

2. **"两个 7B model families 的结果可以 generalize"**：Proposal 选择 DeepSeek-R1-Distill-Qwen-7B 和 Qwen3-8B，都是 7-8B 规模。CoT faithfulness 的 scale dependence 已被多篇论文提到（e.g., CST 论文显示 larger models benefit more）。7B 模型的 faithfulness dynamics 可能与 70B+ 模型截然不同。14B scaling validation 只是 partial mitigation。

3. **"自行训练的 GRPO runs 能复现 comparable quality 的 reasoning models"**：Proposal 将在 MATH + GPQA 上用 Open-R1 pipeline 做 GRPO。但 DeepSeek-R1 的成功涉及 massive-scale 数据和 compute，7B distill + further GRPO 的训练质量和稳定性是有 risk 的。如果 GRPO 训练本身不稳定或不 converge well，所有 downstream 测量都失去意义。

---

```
【3 维度打分】:
```

**1. Novelty: 弱-中 — 组合性 novelty，核心概念非新**

Proposal 的 novelty 是 **方法论组合**（joint surface + latent tracking across RL steps）而非概念性突破。具体来说：
- "Probes across RL training steps" 已由 Obfuscation Atlas（2602.15515）实现，虽然 focus 不同（deception vs. general faithfulness），但技术路线几乎相同（linear probes on residual streams at RLVR checkpoints）
- "Surface faithfulness across RL steps" 已由 VLM checkpoint paper（2602.12506）和 Chen et al.（2505.05410）实现
- "Pre-CoT probes as latent faithfulness measure" 直接来自 Cox et al.（2603.01437）
- "Probe trajectories" 来自 2605.18549

Proposal 的核心是将这些 **已有方法** 组合应用于一个 **已有问题**（RL decouples surface from latent faithfulness）。这不是 trivial 组合——joint measurement 确实是 gap——但也不是 "surprising" 级别的 novelty。审稿人可能会问："So you combined existing tools to confirm an expected result?"

**2. Significance: 中 — 问题重要但 expected result 限制了 impact**

研究问题本身——"RL 是否系统性地 decouple surface 和 latent faithfulness"——对 AI safety 和 deployment 决策有直接影响。如果答案是 yes（且 proposal 自己也 hypothesize 是 yes），那么 implication 是 "RL-trained reasoning models need latent-space monitoring beyond CoT inspection"。这个 implication 重要。

但问题在于：
- 现有证据已经 **强烈暗示** 这个答案是 yes（RLVR monitorability + pre-CoT probes 的组合逻辑）
- 如果 proposal confirm 了 expected result，其 **marginal information gain** 有限——从 "we strongly suspect this" 到 "we confirmed this" 的 delta
- Significance 的上限取决于 dynamics 是否 reveal 新的 insight（e.g., phase transitions, model-family differences），但这是 contingent on results

如果 proposal 发现 **反预期** 结果（e.g., gap 不存在或 closes with training），那将非常 significant——但 proposal 自己不 predict 这种情况。

**3. Related Work: 强 — 领域覆盖异常全面，定位精准**

这是 proposal 最强的维度。Related work 覆盖了 6 个清晰的子方向（surface faithfulness across RL, latent faithfulness snapshots, probe trajectories, deception probes, adversarial evasion, faithfulness-improving RL），每个方向都准确引用了 2026 年最新的代表性工作。与 Obfuscation Atlas 的区分（deception-specific vs. general faithfulness）、与 2605.18549 的区分（token-level vs. training-level）都清晰合理。所有引用经搜索验证均真实存在。

唯一的 gap：proposal 没有讨论 **Counterfactual Simulation Training**（2602.20710），这篇 Feb 2026 的工作从 "改善 faithfulness" 的角度与 proposal 的 "诊断 unfaithfulness" 形成互补关系，应该被 acknowledged。

---

```
【概率估计】: [20% - 32%] 中位 25%
```

```
【估计理由】: 
```

Proposal 处于 "idea 有实质内核但核心发现若 positive 审稿人会说 'I would have guessed this'" 的区间。

- **Related Work** 维度是强项，拉高了下限——proposal 清楚知道自己在做什么、gap 在哪里
- **Novelty** 维度是主要限制——组合性 novelty + confirmation study 特质显著压制了上限。Obfuscation Atlas 已经在 RLVR checkpoints 上做 probe tracking，proposal 的 delta 是 "general faithfulness + joint surface measurement"，这对 ICLR 级别来说偏 incremental
- **Significance** 维度受限于 expected result——如果 core finding 是 "yes, RL widens the gap"，审稿人很可能回应 "This is consistent with what we already know from [RLVR monitorability + pre-CoT probes]. What new insight does the longitudinal study add?"
- 概率上界被 Novelty 和 "confirmation study" 风险共同 cap 在 ~32%

```
【主要风险】:
```

1. **"Confirmation study" 质疑**：核心 hypothesis（"GRPO widens surface-latent gap"）在现有文献的逻辑推论下是 expected result。审稿人可能认为 "empirical confirmation of a logical prediction" 的 novelty 不足以支撑 top venue，尤其是当 Obfuscation Atlas 已经做了 probes-across-RLVR-steps 的 precedent。Proposal 的 value 高度依赖于 temporal dynamics 本身是否 reveal surprising patterns（changepoints, non-linearities, model-family differences），但这在 idea 阶段是 uncertain 的。

2. **Probe AUC 的 interpretive validity 可能被挑战**：Probe AUC 上升被等同于 "latent unfaithfulness 增加"，但上升也可能反映 model 变得更 capable（better representations → more predictable answers）。如果没有足够强的 causal evidence 支撑这个等价关系（proposal 仅在 5 个 checkpoints 做 activation patching），整个 "surface-latent gap" 的 narrative 可能被 reviewer 质疑为 measurement artifact。

---

Sources:
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)
- [Decoding Answers Before Chain-of-Thought: Pre-CoT Probes](https://arxiv.org/abs/2603.01437)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [Monitoring the Internal Monologue: Probe Trajectories](https://arxiv.org/abs/2605.18549)
- [The Obfuscation Atlas](https://arxiv.org/abs/2602.15515)
- [RL-Obfuscation](https://arxiv.org/abs/2506.14261)
- [Counterfactual Simulation Training for CoT Faithfulness](https://arxiv.org/abs/2602.20710)
- [Why Models Know But Don't Say](https://arxiv.org/abs/2603.26410)
- [Faithful GRPO](https://arxiv.org/abs/2604.08476)
- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199)


【原始 proposal（允许参考但不是主要依据）】:
# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models

## Description
We propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.

## Core Problem
When and how does the gap between surface CoT faithfulness (measured by behavioral metrics like hint-injection rates and causal reliance) and latent faithfulness (measured by residual-stream probes predicting answer pre-commitment) develop during GRPO training of reasoning models — and what dynamics characterize this divergence?

## Opportunity
Three converging 2026 findings create a precise, actionable gap. First, the RLVR monitorability paper (2602.03978) showed that RL's surface-monitorability gains come from response distribution sharpening and increased prompt attention — NOT from stronger causal reliance on reasoning traces. Second, pre-CoT probes (2603.01437) demonstrated that instruction-tuned models encode answers in residual-stream activations before generating any CoT (>0.9 AUC), with these directions being causally efficacious. Third, the VLM checkpoint paper (2602.12506) showed an accuracy-faithfulness trade-off during RL fine-tuning — but using only LLM-as-judge surface metrics on vision-language models, with no latent-space analysis. Meanwhile, 'Monitoring the Internal Monologue' (2605.18549) introduced probe trajectories as a powerful inference-time monitoring tool but analyzed only fixed, already-trained models — never tracking how probe characteristics evolve across RL training steps. The Obfuscation Atlas (2602.15515) tracked deception probes across RLVR but focused narrowly on reward-hacking obfuscation rather than general faithfulness divergence. Nobody has jointly measured both surface faithfulness metrics and activation-probe-based latent faithfulness at matched RL training checkpoints to characterize how — and how fast — RL decouples what reasoning models say from what they compute. If this divergence is large and systematic, RL-trained reasoning models require latent-space monitoring beyond CoT inspection for safe deployment.

## Landscape
The CoT faithfulness literature in 2026 is large but fragmented along complementary axes, leaving the longitudinal surface-latent gap unstudied:

**Surface faithfulness across RL steps (behavioral only):** Chen et al. (Anthropic 2025, 2505.05410) measured surface faithfulness via hint-injection across RL steps, finding initial improvement that plateaus (~25% for Claude 3.7 Sonnet). The VLM checkpoint paper (2602.12506) tracked CoT consistency via LLM-as-judge across GRPO checkpoints of Qwen2.5-VL-7B-Instruct, finding an accuracy-faithfulness trade-off — but used only behavioral metrics (letter entropy, judge-rated consistency) with no activation probes, and studied VLMs rather than language models.

**Latent faithfulness in final models (snapshot only):** Pre-CoT probes (2603.01437) showed >0.9 AUC answer prediction from residual streams of Gemma 2 and Qwen 2.5 before any CoT tokens. 'Catching Rationalization in the Act' (2603.17199) trained probes to detect motivated reasoning pre- and post-CoT. 'The Hypocrisy Gap' (2602.02496) used SAEs to quantify internal-belief/CoT divergence. 'Why Models Know But Don't Say' (2603.26410) measured thinking-token vs. answer divergence. All analyze final models only.

**Probe trajectories during inference (token-level, not training-level):** 'Monitoring the Internal Monologue' (2605.18549, May 2026) constructed probe trajectories across token positions during generation, achieving 95% AUROC for predicting outcomes. However, this tracks probes across tokens within a single generation of a fixed model — not across RL training checkpoints. Their models (Llama-8B-R1-Distill, Qwen3-4B/8B/14B) are final checkpoints only.

**Deception probes across RLVR (deception-specific):** The Obfuscation Atlas (2602.15515) trained logistic regression probes on residual streams of Llama-3-8B through 70B across GRPO steps, mapping deception emergence. But their focus is reward-hacking obfuscation in coding tasks, not general reasoning faithfulness, and they don't measure surface faithfulness metrics jointly.

**RL-Obfuscation (adversarial evasion):** RL-Obfuscation (2506.14261) showed 7B-14B models can learn to evade latent-space monitors through RL, with token-level monitors being vulnerable. This is an adversarial finding about monitor fragility, not a characterization of natural faithfulness divergence.

**Faithfulness-improving RL methods:** FaithRL (2602.03507), AtManRL (2604.16158), and faithfulness-aware step-level RL (2602.05897) propose RL objectives that improve faithfulness, but none characterize the divergence trajectory of standard GRPO/RLVR training.

**RL training dynamics:** Learning dynamics papers (2601.04670) show reduced feature diversity during RL but don't track faithfulness. The synthetic phase-transition paper (2602.01017) demonstrates faithful→unfaithful transitions under controlled noise in toy arithmetic — the only prior showing discrete transitions, but in a setting far removed from real GRPO.

**The gap:** No existing work jointly tracks probe-measured latent faithfulness AND surface CoT faithfulness metrics at matched RL training checkpoints across training to characterize divergence dynamics in language reasoning models.

## Approach
We produce our own fine-grained GRPO training checkpoints from two architecturally distinct open-weight model families, then jointly measure surface and latent faithfulness at each checkpoint.

**Model families and checkpoint generation:**
(1) DeepSeek-R1-Distill-Qwen-7B as base model, trained with GRPO using the Open-R1 pipeline (HuggingFace TRL) on MATH + GPQA, saving checkpoints every 50 GRPO steps for ~20 checkpoints across training. This model starts with distilled reasoning capability, letting us study how further RL reshapes faithfulness.
(2) Qwen3-8B (base dense model, Apache 2.0) trained with the same GRPO pipeline and datasets, providing an architecturally distinct family that starts without distilled reasoning traces.

**Metrics at each checkpoint:**
(a) *Latent faithfulness proxy*: Train linear probes on residual-stream activations at the last pre-CoT token (following the methodology of Cox et al., 2603.01437), predicting the model's final answer. Report probe AUC and the layer at which AUC first exceeds 0.8 ('commitment layer'). A rising probe AUC across training indicates strengthening answer pre-commitment — the model increasingly 'knows' its answer before reasoning.
(b) *Surface faithfulness — hint-injection*: Apply Chen et al.'s protocol with sycophancy and anchoring hints on a fixed MMLU/GPQA subset (~500 items). Report hint-acknowledgment rate (lower = more faithful surface behavior).
(c) *Causal reliance — NLDD*: Compute the Normalized Logit Difference Decay metric (2602.11201) by corrupting individual reasoning steps and measuring confidence drops. Report the Reasoning Horizon k* (the chain-length fraction beyond which steps have negligible causal effect).
(d) *Activation patching* (on 5 evenly-spaced checkpoints per family): Measure the causal effect of CoT-token activations on the final answer via mean-ablation patching, quantifying how much the model's computation actually flows through the reasoning trace.

**Analysis:**
- Construct the *surface-latent divergence curve*: plot surface faithfulness improvement (declining hint-acknowledgment rate) against latent bypass strengthening (rising probe AUC / shortening reasoning horizon) across GRPO steps.
- Apply changepoint detection (PELT algorithm) as an *exploratory* tool to identify whether divergence accelerates at specific training phases — we do NOT claim phase transitions a priori but test for non-linear dynamics.
- Compare divergence trajectories between the two model families to assess generality.
- On a subset of checkpoints, apply the probe-trajectory methodology of 'Monitoring the Internal Monologue' (2605.18549) to test whether the character of inference-time probe trajectories (volatility, trend features) changes systematically across training — bridging their token-level and our checkpoint-level analyses.

**Scaling validation:** If initial 7B results show clear divergence, replicate core probe + hint-injection measurements on DeepSeek-R1-Distill-Qwen-14B with ~10 GRPO checkpoints to verify the pattern holds at larger scale.

**Key methodological choices justified:**
- Using R1-Distill-7B rather than R1-671B: reviewer correctly identified that Dev1/Dev2/Dev3 checkpoints are not publicly available. Distilled 7B models are computationally tractable (single A100 for inference, 8×A100 for GRPO training) and let us generate arbitrarily fine-grained checkpoints.
- GRPO rather than PPO: GRPO is the algorithm used in DeepSeek-R1 and the VLM checkpoint paper, ensuring comparability.
- Two model families with different starting points (distilled reasoning vs. base): controls for whether divergence is an artifact of the starting model's reasoning capability.

## Resource Estimate
{'manual': {'gpu_hours': '350–500 A100-hours (GRPO training: ~80 A100-hrs × 2 families = 160 hrs; probe training + inference on ~20 checkpoints × 2 families: ~100 hrs; hint-injection evaluation: ~40 hrs; NLDD computation: ~30 hrs; activation patching on 10 checkpoints: ~50 hrs; 14B scaling validation: ~70 hrs)', 'timeline': '8–11 weeks (2 weeks GRPO training + pipeline setup, 3 weeks probe training & surface measurements in parallel, 2 weeks activation patching & NLDD, 1–2 weeks analysis, 1–2 weeks writing)', 'estimated_gpu_cost': '$900–$1,250 at ~$2.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': '300–400 A100-hours (Claude handles probe training scripts, metric computation pipelines, statistical analysis, and plotting; human designs experiments, interprets results, writes key paper sections)', 'timeline': '6–8 weeks', 'claude_api_cost': '$120–$250 (Sonnet 4.6 for code generation, data analysis scripts, and paper drafting; ~40M input + 8M output tokens)', 'estimated_gpu_cost': '$750–$1,000'}, 'auto_research': {'gpu_hours': '300–400 A100-hours', 'timeline': '4–5 weeks (parallelized GRPO training for both families, then parallelized probe training and evaluation across checkpoints)', 'claude_api_cost': '$300–$550 (orchestration agent managing GRPO runs, checkpoint evaluation sweeps, result interpretation, iterative analysis; ~120M input + 25M output tokens)', 'estimated_gpu_cost': '$750–$1,000', 'speed_bottleneck': 'Sequential dependency: GRPO training must complete (or reach sufficient checkpoints) before probe training begins. However, probe training on early checkpoints can start while GRPO training continues. The two model families can be trained in parallel. 14B scaling validation is contingent on 7B results being compelling.'}}

## Inspired By
Direct gap between three convergent findings: (1) RLVR monitorability gains NOT from causal reliance (2602.03978), (2) pre-CoT probes show answer pre-commitment exists in residual streams (2603.01437), (3) VLM checkpoint paper shows accuracy-faithfulness trade-off during RL but with no latent-space analysis (2602.12506). The 'Monitoring the Internal Monologue' paper (2605.18549) shows probe trajectories are powerful for monitoring but leaves the training-dynamics dimension unexplored. The Obfuscation Atlas (2602.15515) demonstrates that probing across RLVR checkpoints is technically feasible at scale.

## Target Venues
- ICLR 2027 (abstract: Sep 19, 2026; full paper: Sep 24, 2026 — primary target, strong fit for mechanistic interpretability; ~18 weeks from now gives ample time for full experiments including 14B scaling)
- AAAI 2027 (abstract: Jul 21, 2026; full paper: Jul 28, 2026 — ambitious secondary target; ~9 weeks from now, feasible with focused 7B-only results if GRPO training starts immediately)
- NeurIPS 2026 workshops (workshop paper deadlines ~Aug 29, 2026; e.g., Mechanistic Interpretability, AI Safety, or Alignment workshops — good venue for initial results even if full paper targets ICLR)

## Key References
- Reasoning Models Don't Always Say What They Think (Anthropic 2025, arXiv 2505.05410)
- Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning (arXiv 2026, 2602.03978)
- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)
- On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs (arXiv 2026, 2602.12506)
- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (arXiv 2026, 2605.18549)
- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (FAR AI/arXiv 2026, 2602.15515)
- RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? (arXiv 2025/2026, 2506.14261)
- How Does Unfaithful Reasoning Emerge from Autoregressive Training? A Study of Synthetic Experiments (arXiv 2026, 2602.01017)
- Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (arXiv 2026, 2602.11201)
- Learning Dynamics in RL Post-Training for Language Models (arXiv 2026, 2601.04670)
- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Goodfire/arXiv 2026, 2603.05488)
- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv 2026, 2602.02496)
- Catching Rationalization in the Act: Detecting Motivated Reasoning Before and After CoT via Activation Probing (arXiv 2026, 2603.17199)
- Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models (arXiv 2026, 2603.26410)
- FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization (arXiv 2026, 2602.03507)
- AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency (arXiv 2026, 2604.16158)
- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (DeepSeek 2025, 2501.12948)
- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv 2025, 2507.18014)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "600c3145-04fd-44b9-8bdf-d5190ac524de",
  "type": "user",
  "uuid": "e25ba120-c7bd-4be6-a65d-34eba26d32d0",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:30:46.965Z_

```json
{
  "parentUuid": "e25ba120-c7bd-4be6-a65d-34eba26d32d0",
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
  "uuid": "8fe83e42-b65a-4e3e-88c6-421e9eecdb64",
  "timestamp": "2026-05-20T03:30:46.965Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:30:46.965Z_

```json
{
  "parentUuid": "8fe83e42-b65a-4e3e-88c6-421e9eecdb64",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e829ba95-f8de-42db-8c23-ad0f2627ef4b",
  "timestamp": "2026-05-20T03:30:46.965Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct a thorough evalua…",
  "leafUuid": "e829ba95-f8de-42db-8c23-ad0f2627ef4b",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Assess surface-latent faithfulness gap in reasoning models",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:31:21.384Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully and produce a Meta Judge synthesis.

First, let me extract the key numbers and dimensions:

**Reviewer 1:**
- Novelty: 弱–中
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 26%

**Reviewer 2:**
- Novelty: 中 (组合性 novelty)
- Significance: 中
- Related Work: 强
- Probability: [22% - 33%] 中位 27%
- Note: If CoRL, ~3-5% (desk reject)


**Reviewer 3:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability: [20% - 32%] 中位 25%
- Note: If CoRL, < 5% (scope mismatch)

All three reviewers converge on nearly identical median probabilities around 25-27%, with a standard deviation of less than 1%, indicating remarkable consensus across the board.

Looking at where they align, there's strong agreement on the paper's strong related work coverage, moderate significance, and weak-to-moderate novelty. They all identify the same core vulnerabilities: the work reads as a confirmation study with predictable outcomes, the probe AUC's interpretive validity is questionable, and Obfuscation Atlas emerges as the closest competitor. There's also shared concern about a trivial alternative approach and potential venue mismatch if submitted to CoRL. Two reviewers additionally flag the simpler two-point comparison as a viable alternative, and all three note the results feel somewhat predictable.

The outliers are more granular—R2 specifically worries about model family diversity given both are Qwen-based, R3raises concerns about GRPO training quality, and R1 emphasizes the representation geometry shifts most directly. Despite these differences, the consistency is remarkably high at under 1% standard deviation.

On venue fit: all three reviewers flagged a fundamental mismatch with CoRL 2026, since the paper addresses CoT faithfulness and mechanistic interpretability for LLMs, which has no connection to robot learning and would likely face desk rejection.

For my synthesis, I need to separate two things: first, assess the proposal's inherent quality for its intended venues like ICLR 2027, then directly address the CoRL venue problem the user specifically asked about.

The three reviewers show remarkable agreement—their median acceptance probabilities cluster around 25-27% with less than 1% standard deviation, indicating strong consensus on the work's fundamental merit. However, for CoRL 2026 specifically, all three flagged a fundamental mismatch: this is a robotics venue and the proposal lacks robotics grounding, making it desk-reject territory at roughly 3-5% probability.

On the implementation side, the estimates converge on needing 350-500 A100-hours total and 8-11 weeks for manual execution, with potential compression to 6 weeks if parallelized.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e829ba95-f8de-42db-8c23-ad0f2627ef4b",
  "isSidechain": false,
  "requestId": "req_011CbD7ZhPFJHTSL3FQqfMM8",
  "type": "assistant",
  "uuid": "691b836b-d2b4-4655-8f65-335f968eabe6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBUwuCHJ7oHXWTWe9VAcy5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18682,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3631,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 18682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18682
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

_source line 9 · 2026-05-20T03:32:20.544Z_

【阶段】: Meta Judge
【三次中位】: [26%, 27%, 25%]  std=0.8%
【共识维度】: 
- **Novelty: 弱–中**（3/3 一致）— 核心贡献是将已有工具（pre-CoT probes, hint-injection, NLDD）组合应用于已有框架（GRPO checkpoint probing à la Obfuscation Atlas），属方法论组合而非概念创新
- **Significance: 中**（3/3 一致）— 问题本身重要（CoT faithfulness for AI safety），但预期 positive result（widening gap）已被 RLVR monitorability + pre-CoT probes 的汇聚证据强烈暗示，"confirmation study" 特质显著
- **Related Work: 强**（3/3 一致）— 领域覆盖全面、定位精准、gap 识别准确，所有引用经验证真实存在
- **核心风险 1: "I would have guessed this"**（3/3 一致）— 审稿人极可能认为 positive result 不 surprising
- **核心风险 2: Probe AUC 解释性争议**（3/3 一致）— probe AUC 上升可能反映 representation 更 separable/模型更 capable，而非 unfaithfulness 增加，操作化定义存在质疑空间
- **Obfuscation Atlas 构成最直接竞争者**（3/3 一致）— 已在 GRPO checkpoints 上做 probe tracking，与本 proposal 技术路线高度重叠
- **Trivial alternative 威胁存在**（3/3 一致）— base vs. final 的 two-point comparison 或从 Obfuscation Atlas 的最小扩展即可覆盖核心 claim
- **Venue mismatch: CoRL 2026 完全不在 scope 内**（2/3 显式标注，1/3 通过 venue listing 隐式确认）— proposal 是 LLM mechanistic interpretability / AI safety 研究，与 Conference on Robot Learning 的核心议题（机器人感知、控制、manipulation、navigation）零交集

【异常维度】: 
- R2 单独指出两个 model family 实际 architectural diversity 可能被高估（DeepSeek-R1-Distill-Qwen-7B 本身就是 Qwen 2.5 的 distillation）— 合理观察但非致命，降权为次要风险
- R3 单独指出自行 GRPO 训练的质量/稳定性风险 — 属实施层面担忧，非 idea 层面问题，降权
- R3 单独提到缺少对 Counterfactual Simulation Training (2602.20710) 的讨论 — 实际上 proposal 的 Key References 中未列此文但 landscape 叙述中有所涉及，minor gap

【最终概率】: [3% - 5%] 中位 3%（CoRL 2026 主会）；[21% - 32%] 中位 26%（proposal 自身列出的目标 venue，如 ICLR 2027 主会）
【一致性】: 高（std=0.8%，三位审稿人在概率估计、维度判决、核心风险识别上高度一致）
【综合理由】: 

**关于 CoRL 2026 venue（用户指定的投稿目标）：**
三位审稿人中有两位显式标注、一位隐式确认：本 proposal 是纯 LLM mechanistic interpretability / AI safety 方向的研究（CoT faithfulness probing across RL training），与 CoRL（Conference on Robot Learning）的核心 scope（robot perception, manipulation, control, navigation, sim-to-real, robot policy learning 等）**完全不沾边**。这不是"边缘相关"而是"根本不在领域内"——即使论文质量再高，也会在 desk review 阶段被拒。CoRL 的 Area Chairs 不会将一篇完全没有机器人实验、没有机器人任务、没有 embodied 组件的纯 LLM 分析论文送审。因此 CoRL 2026 的概率为 ~3%（仅保留极小概率应对"CoRL 临时新增 LLM safety track"等意外情况）。

**关于 proposal 自身的学术质量（对应 ICLR 2027 等合适 venue）：**
三位审稿人在所有核心维度上高度收敛：Related Work 强但 Novelty 弱–中 + Significance 中的组合，将概率锚定在 25-35% 区间的下段。具体逻辑：
1. **Novelty 是主要天花板**：三位审稿人一致认为核心贡献是"将 Obfuscation Atlas 的 checkpoint probing 框架 + Cox et al. 的 pre-CoT probes + Chen et al. 的 hint-injection 组合在一起"，是 synthesis 而非 conceptual innovation。Obfuscation Atlas 已证明 probes-across-GRPO-steps 的技术可行性，从 deception probes 到 general faithfulness probes 是低技术门槛的延伸。
2. **"Confirmation study" 风险**：三位审稿人一致指出，核心 hypothesis（widening gap）已是现有文献的逻辑推论，positive result 不会让审稿人 surprised。这是 top venue empirical papers 的经典 rejection pattern。
3. **Probe AUC 解释性**：三位审稿人一致质疑"rising probe AUC = rising unfaithfulness"这一操作化等价关系——上升也可能反映 better representations / higher confidence，而非 CoT bypass。仅 5 个 checkpoint 的 activation patching 不足以支撑全局因果 claim。
4. **Related Work 强是保底因素**：精确的 gap 识别和全面的文献覆盖保证 proposal 不会因 positioning 不清被拒，为下限提供支撑（~21%）。

由于 std 极低（0.8%），属高一致情况，取中位附近、缩窄区间。最终中位 26% 反映：idea 有实质内核（真实的文献 gap），但核心发现若 positive 属预期之中，novelty 层面不足以支撑 top venue 主会。

【建议】: 不推荐（针对 CoRL 2026 — scope 完全不匹配，desk reject）；边缘偏不推荐（针对 ICLR 2027 — 中位 26%，有实质改进空间但 novelty 天花板受限）

【实施评估】:
  - 计算资源: 350–500 A100-hours（GRPO 训练 ~160 hrs, probe 训练+推理 ~100 hrs, hint-injection ~40 hrs, NLDD ~30 hrs, activation patching ~50 hrs, 14B scaling ~70 hrs）；预估 GPU 成本 $900–$1,250（spot pricing ~$2.50/A100-hr）
  - 数据需求: MATH + GPQA（均为公开数据集），hint-injection 评估用 MMLU/GPQA 子集 ~500 items（公开可得），无数据获取障碍
  - 人工介入: 中等——实验设计、结果解读、关键论文撰写需人工；probe 训练脚本、metric 计算、统计分析可自动化
  - 训练需求: 需要模型训练——(1) GRPO 训练两个 7B 模型各 ~20 checkpoints，(2) 每个 checkpoint 训练 linear probes，(3) 可选 14B scaling validation。训练规模可控（单 A100 可做推理，8×A100 可做 GRPO 训练）
  - 新 Benchmark: 不需要构建新 benchmark；使用现有 MATH/GPQA/MMLU 数据集和现有评估协议（hint-injection, NLDD, activation patching）
  - 预估周期: 8–11 周（手动流程）/ 6–8 周（human-in-loop）/ 4–5 周（全自动化），核心瓶颈是 GRPO 训练的顺序依赖（probe 训练必须等 checkpoint 产出，但可流水线化）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "691b836b-d2b4-4655-8f65-335f968eabe6",
  "isSidechain": false,
  "requestId": "req_011CbD7ZhPFJHTSL3FQqfMM8",
  "type": "assistant",
  "uuid": "2c21264e-b16c-4338-a985-a0b5a7c04d5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBUwuCHJ7oHXWTWe9VAcy5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18682,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3631,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 18682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18682
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct a thorough evalua…",
  "leafUuid": "2c21264e-b16c-4338-a985-a0b5a7c04d5e",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Assess surface-latent faithfulness gap in reasoning models",
  "sessionId": "aebc21a5-e118-4c8d-8ee8-f05daa159bc0"
}
```

---
