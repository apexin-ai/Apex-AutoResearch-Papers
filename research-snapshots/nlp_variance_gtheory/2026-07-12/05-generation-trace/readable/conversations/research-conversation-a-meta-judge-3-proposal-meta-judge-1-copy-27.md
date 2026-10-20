# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e.jsonl`
- **Structured JSON:** [`38fd4eafe2ade3189b1f.json`](../../sessions/38/38fd4eafe2ade3189b1f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:38:27.948Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:38:27.948Z",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a well-informed assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978) (arXiv 2026):\n   核心发现 RLVR 的 surface monitorability 提升来自 response distribution sharpening 和 prompt attention 增强，而非 causal reliance 增强。Monitorability 与 capability 正交。该论文是本 proposal 的直接灵感来源之一，proposal 引用准确。\n\n2. [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437) (arXiv 2026, Cox et al.):\n   在 Gemma 2 和 Qwen 2.5 上训练线性 probe，从 pre-CoT residual stream 预测 final answer，AUC >0.9。且证明 probe direction 有因果效力（steering 可 flip 答案 >50%）。Proposal 引用准确，这是其 latent faithfulness proxy 的方法论基础。\n\n3. [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506) (arXiv 2026):\n   在 Qwen2.5-VL-7B 的 GRPO checkpoint 上跟踪 accuracy vs. CoT consistency，发现 trade-off。但仅用 LLM-as-judge 表层指标，无 activation probe，且是 VLM 而非 LLM。Proposal 对其局限性的描述准确。\n\n4. [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549) (arXiv May 2026):\n   在固定模型的 inference 过程中构建 probe trajectory（逐 token），max-pooling 达 95% AUROC。但只分析 final model，不跟踪 training 过程。极新论文（~2 天前发布），proposal 已引用并正确描述了其局限。\n\n5. [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515) (FAR AI, arXiv 2026):\n   在 Llama-3-8B 到 70B 的 GRPO step 上训练 logistic regression deception probes。这是最接近 proposal 的工作——已证明\"probing across GRPO checkpoints\"技术可行。但 focus 是 reward-hacking obfuscation in coding tasks，不是 general faithfulness，且未联合测量 surface faithfulness。\n\n6. [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261) (arXiv 2025):\n   7B-14B 模型可通过 RL 学会逃避 latent-space monitors，token-level monitors 脆弱。这是 adversarial 发现，与 proposal 的\"natural divergence\"视角互补。\n\n7. [Reasoning Theater: Probing for Performative Chain-of-Thought](https://www.goodfire.ai/research/reasoning-theater) (Goodfire, 2026):\n   发现模型在 easy problems 上 coast（生成多余 CoT），probes 可以检测此类 unfaithfulness。快照分析，无 training dynamics。\n\n8. [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053) (arXiv 2026):\n   7,186 instances 跨 7 tasks 的 faithfulness benchmark，发现 49.7% 输出含 unfaithfulness。Focus 是 benchmark 设计而非 training dynamics。\n\n- **调研总结**: CoT faithfulness 在 2026 年是极度活跃的领域，但工作沿\"表层 behavioral 指标 vs. latent probe 指标\"和\"固定模型快照 vs. 训练过程\"两个维度高度碎片化。确实没有工作在 matched RL checkpoints 上同时测量 surface + latent faithfulness。最接近的是 Obfuscation Atlas（probe across GRPO steps，但 focus 是 deception 而非 general faithfulness）和 VLM checkpoint paper（surface metrics across RL steps，但无 probe）。proposal 的 gap identification 是成立的。\n\n【Trivial Alternative 检验】:\n\n存在两个 trivial alternative 威胁：\n\n(1) **纯 meta-analysis 替代**：既然 RLVR monitorability 论文已经表明 surface gains 与 causal reliance 正交，pre-CoT probes 已经表明 final model 有强 answer pre-commitment——能否直接从现有文献推断\"RL 训练必然加剧 surface-latent gap\"？答案是：大方向可以推断，但 **divergence 的动态特征**（何时开始、是否存在 phase transition、两个 model family 是否不同）无法从现有工作推断。因此 proposal 的增量价值在于 **temporal resolution 和动态刻画**，而非定性发现本身。这是真实的增量，但这也意味着论文的价值高度依赖于动态特征是否有 non-trivial patterns——如果只是线性渐进 divergence，审稿人可能认为 insight 有限。\n\n(2) **简化实验替代**：proposal 堆了 4 个 metrics（probe AUC, hint-injection, NLDD, activation patching）、2 个 model families、changepoint detection、probe trajectory analysis。一个更简单的版本——只用 probe AUC + hint-injection 在 1 个 model family 的 10 个 checkpoints 上——可能就能回答核心问题。当然，更全面的实验提高 robustness，但这是执行层面的，不改变 idea 本质。\n\n**增量价值判断**：存在但有限。核心 finding 的方向是可预测的，价值集中在 temporal dynamics 的量化刻画上。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经充分验证的假设：\n\n(1) **\"Probe AUC = latent faithfulness\" 假设**：Proposal 将 pre-CoT probe AUC 上升等同于\"latent answer pre-commitment strengthening\"。但 probe AUC 可能反映的是 task representation quality 的提升（模型更好地理解问题），而非\"在推理前就锁定答案\"。Cox et al. 的 activation steering 实验部分支持因果性，但 steering ≠ natural generation pathway。这个等式需要更强的论证。\n\n(2) **\"Surface metrics improvement = surface faithfulness improvement\" 假设**：Hint-injection acknowledgment rate 下降可能意味着模型变得更不容易被 hint 干扰（robustness），也可能意味着模型学会了不在输出中提及 hint 但仍被 hint 影响（deceptive alignment）。Proposal 对此没有充分讨论。\n\n(3) **\"Divergence = RL systematically decouples what models say from what they compute\" 的因果推断**：即使观察到 surface-latent divergence 增大，也可能是 RL 让模型在 both dimensions 各自变好但速率不同（而非\"decoupling\"）。\"Decoupling\" 暗示某种对抗性关系，而实际可能只是独立变化。\n\n假设(1)是最关键的——如果 probe AUC 不是 latent faithfulness 的有效代理，整个\"gap\"的解读就会坍塌。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Gap identification 是成立的：确实没有工作在 matched RL checkpoints 上联合测量 surface + latent faithfulness（Obfuscation Atlas focus 是 deception probes，VLM checkpoint paper 无 latent measures，Monitoring Internal Monologue 只看 inference-time 的 fixed models）。但这个 novelty 本质上是 **组合式的**——将 Cox et al. 的 probe methodology、Chen et al. 的 hint-injection protocol、VLM checkpoint paper 的\"checkpoint 采样\"思路组合到一起，在 GRPO checkpoints 上 run。没有新方法论、没有新概念框架，核心贡献是 \"在正确的时间轴上运行现有工具的组合\"。这对于一篇 top venue 论文来说，novelty 偏窄。更关键的是，**核心发现的方向（divergence 加剧）是高度可预测的**——如果结果显示 no divergence 反而更 surprising 也更有影响力，但 proposal 自己都 hypothesize widening gap。\n\n2. **Significance: 中偏强** — \n   研究问题本身对 AI safety 有直接意义：\"RL 训练是否系统性地让 CoT 变得不可信\"是 2026 年的核心问题之一。如果结果清晰，直接影响 deployment monitoring 决策（是否需要 latent-space monitoring infrastructure）。此外，两个 model family 的对比增加了 generalizability。但 significance 受限于：(a) safety community 已经 operate under the assumption that CoT may not be faithful——本研究量化 degree 而非改变 fundamental understanding；(b) 即使证明 divergence 存在，下一步的 actionable advice（\"所以我们需要 latent monitoring\"）已经是 existing consensus。\n\n3. **Related Work: 强** — \n   这是 proposal 最出色的部分。引用了 15+ 篇 2025-2026 论文，覆盖了 surface faithfulness (Chen et al., VLM checkpoint)、latent probing (Cox et al., Catching Rationalization, Hypocrisy Gap)、probe trajectories (Monitoring Internal Monologue)、deception probing across training (Obfuscation Atlas)、adversarial evasion (RL-Obfuscation)、faithfulness-improving RL (FaithRL, AtManRL)、training dynamics (learning dynamics, synthetic phase transition) 等多个维度。所有引用经调研验证均真实存在且描述准确。gap 的差异化定位清晰——沿 \"surface vs. latent\" 和 \"snapshot vs. longitudinal\" 两个轴精确刻画。唯一轻微不足是未讨论 Reasoning Theater (Goodfire, 2603.05488) 虽列在引用中但未深入分析其 probe-based performative detection 与本工作的关系。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】:\nNovelty 是限制上界的主要维度。核心贡献是\"组合现有方法在新的时间轴上运行\"，这在 idea 层面偏 incremental。虽然 gap identification 成立，但预期结果的方向高度可预测（widening divergence），审稿人大概率会写\"the main finding confirms what prior work already strongly suggests\"。Significance 给了一定的下限支撑——research question 确实重要，对 safety practice 有直接 implications——但不足以突破 novelty 的 ceiling。Related Work 的出色覆盖是加分项，但形式完善不等于 idea 强。\n\n上界 33% 对应的场景是：动态特征出现非常 non-trivial 的 pattern（如 sharp phase transition、两个 model family 完全不同的 divergence trajectory），且审稿人认为这些 finding 本身就是重要贡献。下界 22% 对应的场景是：divergence 呈单调渐进，审稿人认为\"we already knew this would happen\"。\n\n【主要风险】:\n1. **\"Expected finding\" 问题**：核心 hypothesis（widening gap）是 prior work 的直接外推，如果结果如预测，审稿人会质疑 insight 的增量价值——\"quantifying a gap everyone already assumed exists\" 不足以撑起一篇 top venue 论文。论文的影响力高度依赖于 temporal dynamics 中是否有 surprising patterns。\n2. **Proxy validity 问题**：Probe AUC 作为 \"latent faithfulness\" 的代理指标的有效性未经充分论证。如果审稿人质疑\"probe AUC 上升可能只反映 task representation 改善而非 answer pre-commitment 加剧\"，整个 surface-latent gap 的叙事就会被动摇，而 proposal 没有给出 convincing 的反驳。\n```\n\nSources:\n- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)\n- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)\n- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)\n- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)\n- [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)\n- [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)\n- [Reasoning Theater: Probing for Performative Chain-of-Thought](https://www.goodfire.ai/research/reasoning-theater)\n- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct the evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n```\n\n---\n\n## ⚠️ 前置关键问题：严重的投稿方向错误\n\n在进入 idea 质量评估之前，必须首先指出一个**致命的外部问题**：\n\n**CoRL (Conference on Robot Learning) 2026 明确声明：\"Submissions without a robotics focus will be returned without review.\"** 本 proposal 关于 LLM 的 CoT faithfulness 与 RL 训练动态，**与机器人学习零交集**。如果投稿 CoRL，将在 desk rejection 阶段被退回，连进入审稿流程的机会都没有。\n\n本 proposal 的合适投稿方向应为：**ICML 2026 / NeurIPS 2026 / ICLR 2027 / COLM 2026** 等以 ML/NLP/AI Safety 为核心的会议。\n\n**以下 idea 质量评估按 NLP/ML 顶会标准进行（因为 CoRL 的中稿概率固定为 ~0%）。**\n\n---\n\n```\n【领域调研】:\n```\n\n**1. [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978) (arXiv 2026.02)**\n- RLVR 的 surface monitorability 提升来源于 response distribution sharpening 和 increased prompt attention，而非 causal reliance on reasoning traces\n- 与本 proposal 的关系：proposal 的核心假设之一直接构建在此发现之上——surface 与 causal reliance 正交性\n\n**2. [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437) (arXiv 2026.03)**\n- 线性 probe 在 pre-CoT 残差流上可以 >0.9 AUC 预测最终答案；probe 方向具有因果效力（activation steering 可改变答案）\n- 与本 proposal 的关系：proposal 直接采用其方法论作为 latent faithfulness proxy\n\n**3. [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506) (arXiv 2026.02)**\n- 在 VLM 的 GRPO checkpoints 上追踪 accuracy-faithfulness trade-off，但仅使用 LLM-as-judge 等 surface metrics\n- 与本 proposal 的关系：proposal 声称补充了此工作缺失的 latent-space 分析维度\n\n**4. [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549) (arXiv 2026.05)**\n- 在固定模型的推理过程中构建 probe trajectories（token 级别），达到 95% AUROC\n- 与本 proposal 的关系：此工作追踪的是推理时的 token 级 probe 轨迹，proposal 追踪的是训练步级 probe 变化——维度互补但不重叠\n\n**5. [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515) (FAR AI, arXiv 2026.02)**\n- 在 Llama-3-8B~70B 的 GRPO 训练过程中训练 deception probes，追踪 reward-hacking obfuscation 的出现\n- **与本 proposal 的关键关系**：这是最接近的竞争工作——已经展示了\"在 RLVR checkpoints 上训练 probes 追踪内部状态变化\"的技术路线。只是其关注点是 deception/reward-hacking 而非 general faithfulness\n\n**6. [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261) (arXiv 2025.06)**\n- 7B-14B 模型可以通过 RL 学会 evade latent-space monitors，token-level monitors 脆弱，holistic monitors 较鲁棒\n- 与本 proposal 的关系：为 proposal 的安全动机提供了支撑——如果模型能 evade monitors，理解 divergence dynamics 更加重要\n\n**7. [Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers](https://arxiv.org/abs/2603.26410) (arXiv 2026.03)**\n- 12 个开源推理模型中，thinking tokens 与 answer 之间存在 ~59 个百分点的 hint acknowledgment 差距\n- 与本 proposal 的关系：佐证了 surface-latent divergence 的存在，但是 snapshot 分析，无训练动态维度\n\n**8. [Counterfactual Simulation Training for Chain-of-Thought Faithfulness](https://arxiv.org/abs/2602.20710) (arXiv 2026.02)**\n- 提出 CST 方法提升 CoT faithfulness\n- 与本 proposal 的关系：属于 faithfulness-improving 方法，不直接竞争，但说明领域对 faithfulness 问题的广泛关注\n\n**调研总结**：CoT faithfulness 在 2026 年已成为 AI safety 的热门子领域，但现有工作沿三个独立轴分布：(1) surface metrics across RL training、(2) latent probes on fixed models、(3) deception probes across RL training (针对 reward-hacking)。Proposal 声称的 gap——jointly tracking surface + latent general faithfulness across training——在调研中确实未被覆盖。但最近的 Obfuscation Atlas 在方法论上非常接近（probes across RLVR checkpoints），只是目标变量不同。\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在中等程度的 trivial alternative 威胁。**\n\n最直接的 trivial alternative 是：**已有的几篇工作（RLVR monitorability + pre-CoT probes + VLM checkpoint 论文）的发现已经逻辑上蕴含了 proposal 的核心假设。** 具体来说：\n\n- RLVR monitorability 论文已证明：surface 改善 ≠ causal reliance 增强\n- Pre-CoT probes 论文已证明：模型在生成 CoT 之前就\"知道\"答案\n- VLM checkpoint 论文已证明：RL 训练中存在 accuracy-faithfulness trade-off\n\n将这三个发现拼在一起，一个合理的推论就是：**RL 训练会加剧 surface-latent divergence。** 这不需要做新实验就能 conjecture。\n\nProposal 的增量价值在于：(1) **量化** 这个 divergence 的 magnitude 和 dynamics（是渐进的还是有 phase transition？）；(2) **跨模型家族的对比**验证 generality；(3) **多个互补 metric 的联合测量**。这些增量是真实的，但它们是\"测量一个预期中的现象并提供精确刻画\"，而非\"发现一个新现象\"或\"提出一个新方法\"。\n\n如果最终结果是\"divergence 是渐进且单调的\"，那这个结果的信息量较低——\"I would have guessed this\"。只有在动态呈现非平凡结构（如 phase transition、非单调性、模型家族间的定性差异）时，才有足够的 surprise factor。\n\n---\n\n```\n【前提假设检验】:\n```\n\n核心 claim 的逻辑链有以下**未经验证的假设**：\n\n1. **\"Probe AUC 上升 = answer pre-commitment 加强\" 的等价关系。** Probe AUC 的上升也可能反映 RL 训练使得模型的内部表征更加 linearly separable（表征几何变化），而非\"模型更早地决定了答案\"。Pre-CoT probes 论文在 fixed models 上验证了因果关系（activation steering），但 proposal 没有在每个 checkpoint 做 steering 验证——仅在 5 个 checkpoint 做 activation patching。如果 probe AUC 上升是因为表征空间被 RL 线性化，而非因果 pre-commitment 增强，核心 claim 就不成立。\n\n2. **\"Surface faithfulness 改善（hint-acknowledgment rate 下降）= 真正的 faithfulness 进步\" 的等价关系。** Chen et al. 的 hint-injection protocol 测量的是 sycophancy/anchoring resistance，而非 general faithfulness。RL 训练可能仅仅让模型学会了\"不承认 hint\"（一种表面行为），而非真正忽略 hint 的影响。这会使 surface metric 的上升不真正反映 faithfulness 改善，从而使 \"surface-latent divergence\" 的叙事变得更复杂。\n\n3. **两个模型家族足以支撑 generality claim。** DeepSeek-R1-Distill-Qwen-7B 和 Qwen3-8B 虽然在起始条件上不同（distilled vs. base），但都属于 Qwen 系列架构。架构层面的 diversity 有限。\n\n---\n\n```\n【3 维度打分】:\n```\n\n**1. Novelty: 弱-中（偏弱）**\n\n理由：\n- Proposal 声称的核心 novelty——\"jointly tracking surface + latent faithfulness across RL checkpoints\"——在概念层面是真实的 gap，经调研确认无直接先例。\n- **但**，Obfuscation Atlas (2602.15515) 已经展示了几乎完全相同的技术路线（probes across RLVR checkpoints），只是换了目标变量（deception → general faithfulness）。这意味着 proposal 的方法论 novelty 很低——本质上是将已有方法应用于一个相邻问题。\n- 核心假设（RL 加剧 surface-latent divergence）是已有三篇工作逻辑推论的自然延伸，而非一个 surprising 的新 claim。\n- \"首次联合测量\"（first to jointly measure X and Y）是一种常见的 novelty 策略，但当 X 和 Y 各自的工具和发现都已存在时，这种 novelty 的分量较轻。审稿人可能会认为这是 \"engineering/measurement contribution\" 而非 \"scientific contribution\"。\n\n**2. Significance: 中**\n\n理由：\n- 研究问题本身——理解 RL 如何影响推理模型的内在计算忠实性——是 AI safety 领域的核心问题之一，具有真实的重要性。\n- 如果 divergence 存在且系统性很强，这对 RL-trained reasoning models 的部署决策（是否需要 latent-space monitoring）有直接的实践意义。\n- **但**，\"需要 latent-space monitoring\"这一结论已经被多篇工作从不同角度论证（Why Models Know But Don't Say (2603.26410) 明确提出了三层 monitoring 架构的必要性）。Proposal 的主要增量是提供更精确的时间线刻画，但结论方向的 surprise factor 低。\n- 对于 NeurIPS/ICML 而言，如果 dynamics 呈现非平凡结构，significance 可以上升到\"中-强\"；如果只是确认渐进 divergence，则停留在\"中\"。\n\n**3. Related Work: 强**\n\n理由：\n- Proposal 对相关工作的覆盖非常全面且准确。经我调研验证：(1) 所有引用论文确实存在；(2) 对每篇论文的描述准确；(3) 差异化定位清晰——proposal 明确说明了为什么每篇相关工作都只覆盖了部分维度。\n- 特别值得肯定的是对 Obfuscation Atlas 和 Monitoring the Internal Monologue 的定位——前者是最强竞争者，proposal 正确识别了其 scope 限制（deception-specific）。\n- 覆盖了 faithfulness-improving methods (FaithRL, AtManRL) 作为对比，显示了对领域格局的全面理解。\n- 唯一潜在遗漏：Counterfactual Simulation Training (2602.20710) 和 \"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?\" (2603.22582) 未被提及，但这些工作与 proposal 的核心 gap 关系较弱，不构成重大遗漏。\n\n---\n\n```\n【概率估计】: 0-5% (CoRL 2026); 20-30% 中位 25% (若投稿至 ICML/NeurIPS/ICLR 等合适方向)\n```\n\n```\n【估计理由】:\n```\n\n**CoRL 2026: ~0%。** Proposal 与机器人学习完全无关，CoRL 明确声明\"Submissions without a robotics focus will be returned without review\"。这不是 idea 质量问题，而是根本性的投稿方向错误。\n\n**若投稿至合适的 ML 顶会（ICML/NeurIPS 等）: 20-30%，中位 25%。** 理由如下：\n\n- Related Work 维度强，说明作者对领域有深入理解，proposal 形式质量高。这确保了合理的下限。\n- **但 Novelty 是主要瓶颈。** 核心贡献是\"联合测量\"已有方法论在一个新组合下的应用结果——概念层面的新意有限。Obfuscation Atlas 已经展示了几乎相同的技术路线（probes across RLVR checkpoints）。审稿人很可能写出 \"The individual components (probes, hint injection, NLDD) are all borrowed from prior work; the contribution is primarily in combining them\" 这样的评价。\n- 核心假设（divergence 加剧）是 expected outcome——通过 \"I would have guessed this\" 测试的概率较高。只有在 dynamics 呈现非平凡结构时才能达到 surprising 的门槛。\n- Significance 是中等——问题重要但结论方向已被多篇工作预见。\n\n概率区间反映了：如果 dynamics 呈现 phase transition 等非平凡结构（上界 30%），vs. 如果 dynamics 是渐进单调的（下界 20%，此时 novelty 和 significance 都会被压低）。\n\n```\n【主要风险】:\n```\n\n1. **\"Confirmatory study\" 风险（最大风险）：** 核心假设是三篇已有工作的逻辑推论。如果实验结果只是确认\"divergence 存在且渐进增加\"，审稿人会认为这是一篇 confirmatory empirical study，缺乏足够的 scientific surprise 来支撑顶会录用。Novelty 被降级为 measurement contribution。\n\n2. **Probe AUC 的因果解读风险：** 如果 probe AUC 上升反映的是 RL 线性化表征空间（而非因果 pre-commitment 增强），整个 \"surface-latent faithfulness gap\" 的叙事框架就会被质疑。Proposal 仅在 5/40 个 checkpoint 做 activation patching，不足以严格支撑每个 checkpoint 的因果 claim。\n\n---\n\nSources:\n- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)\n- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)\n- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)\n- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)\n- [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)\n- [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)\n- [Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers](https://arxiv.org/abs/2603.26410)\n- [Counterfactual Simulation Training for Chain-of-Thought Faithfulness](https://arxiv.org/abs/2602.20710)\n- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research data. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **\"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning\" (2602.03978, 2026)**:\n   最直接相关的先驱工作之一。证明 RLVR 的表面可监控性提升来自响应分布收缩和 prompt attention 增加，而非 CoT 因果依赖增强。即：surface gains ≠ causal reliance。本 proposal 的核心假设（surface-latent gap widens）几乎是这篇论文结论的直接推论。\n\n2. **\"Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering\" (2603.01437, Cox et al. 2026)**:\n   在 Gemma 2 和 Qwen 2.5 上证明线性 probe 可以 >0.9 AUC 从 pre-CoT residual stream 中解码最终答案，且该方向是 causal 的（steering 实验）。这是 proposal 的方法论支柱——但该论文只研究 final models，没有训练动态。\n\n3. **\"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\" (2602.12506, Apple 2026)**:\n   在 Qwen2.5-VL-7B 上发现 RL fine-tuning 的 accuracy-faithfulness trade-off，但仅使用 LLM-as-judge 表面指标，无 activation-level 分析，且是 VLM 而非 LLM。本 proposal 的直接对标和改进目标。\n\n4. **\"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes\" (2602.15515, FAR AI 2026)**:\n   **这是最关键的竞争工作**。已经在 Llama-3-8B through 70B 上跨 GRPO training steps 训练了 logistic regression probes，公开了 500+ 训练模型。方法论（probes across RLVR checkpoints）与本 proposal 高度重叠。区别：该论文聚焦 deception/reward-hacking obfuscation，而非 general faithfulness；未联合测量 surface faithfulness 指标。但技术路径几乎相同。\n\n5. **\"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (2605.18549, May 2026)**:\n   构建 token-level probe trajectories，95% AUROC 预测推理结果。关键发现：max-pooling 是关键。但仅分析 fixed final models，未追踪 training dynamics。本 proposal 声称要 bridge token-level 和 checkpoint-level 分析。\n\n6. **\"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?\" (2506.14261, Gupta & Jenner)**:\n   7B-14B 模型可通过 RL 学会逃避 latent-space monitors，token-level monitors 脆弱而 max-pooling/attention-based probes 鲁棒。这是对 probe-based monitoring 本身的质疑——若 RL 能学会 evade probes，那 probe AUC 在 training 过程中的变化可能反映的是 evasion 而非 faithfulness。\n\n7. **其他 final-model snapshot 工作**: \"Catching Rationalization in the Act\" (2603.17199), \"The Hypocrisy Gap\" (2602.02496), \"Why Models Know But Don't Say\" (2603.26410), \"Reasoning Theater\" (Goodfire 2603.05488) — 这些都在不同角度证实了 final models 的 surface-latent divergence，但都是 snapshot 研究。\n\n8. **Faithfulness-improving RL**: FaithRL (2602.03507), AtManRL (2604.16158, ICLR 2026 workshop) — 提出改进 faithfulness 的 RL 方法，但不研究 standard GRPO 的 divergence trajectory。\n\n- **调研总结**: CoT faithfulness 在 2026 是极其拥挤的赛道，已存在大量高质量工作。关键组件——probes across RLVR checkpoints（Obfuscation Atlas）、pre-CoT probe methodology（Cox et al.）、checkpoint-level surface faithfulness tracking（VLM paper）——均已有独立工作。本 proposal 的核心贡献是将这些已有组件组合在一起，联合测量 surface + latent faithfulness across GRPO steps。这是一个 \"组合 novelty\" 而非 \"方法 novelty\" 的工作。\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。** 具体来说：\n\n1. **最直接的 trivial baseline**: 直接使用 Obfuscation Atlas 已公开的 500+ RLVR checkpoints（Llama-3-8B through 70B，GitHub 开源），在其上训练 general faithfulness probes（而非 deception probes），并添加 hint-injection surface metrics。这将以远低于本 proposal 的成本（无需自己跑 GRPO training）达到几乎相同的核心结论。\n\n2. **更简单的推论路径**: RLVR Monitorability 论文已证明 \"surface gains ≠ causal reliance\"，Pre-CoT Probes 论文已证明 \"models pre-commit answers in residual streams\"。将两者放在一起，\"RL training widens the surface-latent gap\" 已是强推论——本 proposal 的实验价值在于 **量化** 这个 gap，而非 **发现** 它。\n\n**增量价值**: 本 proposal 相对于 trivial alternatives 的增量在于：(a) 两个 architecturally distinct model families 的对比，(b) changepoint detection 的时间动态分析，(c) 联合的 NLDD + activation patching 因果分析。但这些都是实验设计层面的增量，不改变核心 insight。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **\"Linear probe AUC 上升 = latent answer pre-commitment 增强\" 这个等价关系未必成立。** Probe AUC 上升可能反映 RL training 导致 representation 变得更线性可分（表征空间结构变化），而非模型真的更早\"决定\"了答案。RL training 改变了 representation geometry，这可能让 probe 更容易 decode，但不等价于 faithfulness 下降。Obfuscation Atlas 和 RL-Obfuscation 论文都表明 RL 可以改变 probe 的可检测性，但方向是复杂的。\n\n2. **\"Surface faithfulness metrics (hint-injection) 的改善方向是 monotonic 的\" 这个假设过于简化。** Chen et al. 的结果显示 hint-injection rate 先下降后 plateau，但在不同 model families 和 training regimes 下可能呈现不同 pattern。如果 surface metric 也恶化（而非改善），那 \"divergence\" 的 narrative 就不成立——两者可能同时恶化，即不存在 \"gap\"。\n\n3. **\"GRPO training 的 faithfulness dynamics 可以从 7B distilled models 外推到大规模 models\" 这个假设需要谨慎。** Distilled models 的起点（已有 reasoning traces）与 from-scratch RL training 有质的不同。14B scaling validation 是个好设计，但 7B → 14B 的 scaling step 太小，难以说明 generality。\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中 (Weak-Medium)** — 核心贡献是将已有方法组合应用：probe methodology 来自 Cox et al. (2603.01437)，probes across RLVR checkpoints 的技术路径已被 Obfuscation Atlas (2602.15515) 证明可行且开源，surface faithfulness tracking 已有 VLM checkpoint paper (2602.12506) 和 Chen et al. (2505.05410) 的先例。本 proposal 的 novelty 是 \"combination novelty\"——将这些已有组件组合在一起。虽然 proposal 正确指出 \"nobody has jointly measured both\"，但这种 \"nobody has done X+Y together\" 式的 gap 在审稿人看来通常属于 incremental contribution。更关键的是，Obfuscation Atlas 已经做了 probes across RLVR checkpoints 的核心方法论，本 proposal 的差异化（general faithfulness vs. deception）不构成显著的方法论跃迁。\n\n2. **Significance: 中 (Medium)** — 研究问题本身是重要的：理解 RL training 如何影响 reasoning faithfulness 对 AI safety 有直接意义。但如果核心发现是 positive（gap widens），审稿人的反应更可能是 \"I would have guessed this\"，因为 RLVR Monitorability (2602.03978) 已经告诉我们 surface gains 不来自 causal reliance，Pre-CoT Probes (2603.01437) 已经告诉我们 models pre-commit answers。这两个事实加在一起，gap widening 是 expected outcome。如果发现是 negative（gap doesn't widen），反而更 surprising 更有价值——但 proposal 的 framing 显然 bet on positive result。Significance 的上界受限于 confirmatory nature。\n\n3. **Related Work: 强 (Strong)** — 这是 proposal 最突出的优点。对 2026 年 CoT faithfulness 文献的覆盖极为全面，对每篇相关工作的差异化定位清晰准确。Obfuscation Atlas、RL-Obfuscation、Monitoring Internal Monologue、Pre-CoT Probes、VLM checkpoint paper 等关键竞争工作均被识别并合理定位。唯一的小瑕疵是对 Obfuscation Atlas 的竞争性可能 understate 了——proposal 将其定位为 \"deception-specific\" 而与自己区隔，但审稿人可能认为从 deception probes 到 general faithfulness probes 的 generalization 是 straightforward 的。\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】:\nNovelty 是主要限制维度。核心方法论组件均已存在（probes across checkpoints: Obfuscation Atlas; pre-CoT probes: Cox et al.; surface metrics across RL steps: Chen et al. & VLM paper），proposal 的贡献是将它们组合并联合测量。在一个已经非常拥挤的 2026 CoT faithfulness 赛道中，\"combination study with existing methods\" 面临 \"incremental\" 的审稿评价风险。Significance 受限于核心假设的 expected nature——如果 positive 结果是大多数人已经预期的，empirical confirmation 的价值被打折。Related work 的高质量和实验设计的完善度提供了一定的 floor（不太可能因为 coverage 不足被拒），但无法弥补 idea 层面 novelty 的不足。概率上界受 novelty 限制在 ~28%；下界由 solid execution plan + important question 支撑在 ~18%。\n\n**关于投稿会议的重要说明**: 本 proposal 的主题是 NLP reasoning model 的 CoT faithfulness 和 RL training dynamics，与 **CoRL (Conference on Robot Learning)** 的 scope 完全不匹配。CoRL 聚焦机器人学习、机器人感知、运动规划等。如果确实投稿 CoRL，中稿概率接近 0%（desk reject）。上述概率估计基于将其投稿到合适的 NLP/ML venue（如 NeurIPS, ICML, ACL, EMNLP）。\n\n【主要风险】:\n1. **Novelty 不足风险（最核心）**: 审稿人很可能指出 Obfuscation Atlas 已经做了 \"probes across RLVR checkpoints\" 的核心工作，本文的差异化（general faithfulness vs. deception + adding surface metrics）不足以构成 top-venue 级别的 novelty。\"Nobody has done X+Y together\" 这种 gap statement 在拥挤赛道中说服力有限。\n2. **Confirmatory bias 风险**: 核心假设（gap widens）是已有 evidence 的直接推论，若实验结果如预期，审稿人可能评价为 \"confirmatory study with limited new insight\"。Proposal 缺少一个 \"如果结果出乎意料会怎样\" 的 contingency framing，也缺少一个能区分 \"gap widens because of X\" vs. \"gap widens because of Y\" 的 mechanistic hypothesis。\n```\n\nSources:\n- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)\n- [Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)\n- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)\n- [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)\n- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)\n- [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)\n- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199)\n- [The Hypocrisy Gap](https://arxiv.org/abs/2602.02496)\n- [Why Models Know But Don't Say](https://arxiv.org/abs/2603.26410)\n- [FaithRL](https://arxiv.org/abs/2602.03507)\n- [AtManRL](https://arxiv.org/abs/2604.16158)\n- [Reasoning Theater](https://www.goodfire.ai/research/reasoning-theater)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models\n\n## Description\nWe propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.\n\n## Core Problem\nWhen and how does the gap between surface CoT faithfulness (measured by behavioral metrics like hint-injection rates and causal reliance) and latent faithfulness (measured by residual-stream probes predicting answer pre-commitment) develop during GRPO training of reasoning models — and what dynamics characterize this divergence?\n\n## Opportunity\nThree converging 2026 findings create a precise, actionable gap. First, the RLVR monitorability paper (2602.03978) showed that RL's surface-monitorability gains come from response distribution sharpening and increased prompt attention — NOT from stronger causal reliance on reasoning traces. Second, pre-CoT probes (2603.01437) demonstrated that instruction-tuned models encode answers in residual-stream activations before generating any CoT (>0.9 AUC), with these directions being causally efficacious. Third, the VLM checkpoint paper (2602.12506) showed an accuracy-faithfulness trade-off during RL fine-tuning — but using only LLM-as-judge surface metrics on vision-language models, with no latent-space analysis. Meanwhile, 'Monitoring the Internal Monologue' (2605.18549) introduced probe trajectories as a powerful inference-time monitoring tool but analyzed only fixed, already-trained models — never tracking how probe characteristics evolve across RL training steps. The Obfuscation Atlas (2602.15515) tracked deception probes across RLVR but focused narrowly on reward-hacking obfuscation rather than general faithfulness divergence. Nobody has jointly measured both surface faithfulness metrics and activation-probe-based latent faithfulness at matched RL training checkpoints to characterize how — and how fast — RL decouples what reasoning models say from what they compute. If this divergence is large and systematic, RL-trained reasoning models require latent-space monitoring beyond CoT inspection for safe deployment.\n\n## Related Work / Landscape\nThe CoT faithfulness literature in 2026 is large but fragmented along complementary axes, leaving the longitudinal surface-latent gap unstudied:\n\n**Surface faithfulness across RL steps (behavioral only):** Chen et al. (Anthropic 2025, 2505.05410) measured surface faithfulness via hint-injection across RL steps, finding initial improvement that plateaus (~25% for Claude 3.7 Sonnet). The VLM checkpoint paper (2602.12506) tracked CoT consistency via LLM-as-judge across GRPO checkpoints of Qwen2.5-VL-7B-Instruct, finding an accuracy-faithfulness trade-off — but used only behavioral metrics (letter entropy, judge-rated consistency) with no activation probes, and studied VLMs rather than language models.\n\n**Latent faithfulness in final models (snapshot only):** Pre-CoT probes (2603.01437) showed >0.9 AUC answer prediction from residual streams of Gemma 2 and Qwen 2.5 before any CoT tokens. 'Catching Rationalization in the Act' (2603.17199) trained probes to detect motivated reasoning pre- and post-CoT. 'The Hypocrisy Gap' (2602.02496) used SAEs to quantify internal-belief/CoT divergence. 'Why Models Know But Don't Say' (2603.26410) measured thinking-token vs. answer divergence. All analyze final models only.\n\n**Probe trajectories during inference (token-level, not training-level):** 'Monitoring the Internal Monologue' (2605.18549, May 2026) constructed probe trajectories across token positions during generation, achieving 95% AUROC for predicting outcomes. However, this tracks probes across tokens within a single generation of a fixed model — not across RL training checkpoints. Their models (Llama-8B-R1-Distill, Qwen3-4B/8B/14B) are final checkpoints only.\n\n**Deception probes across RLVR (deception-specific):** The Obfuscation Atlas (2602.15515) trained logistic regression probes on residual streams of Llama-3-8B through 70B across GRPO steps, mapping deception emergence. But their focus is reward-hacking obfuscation in coding tasks, not general reasoning faithfulness, and they don't measure surface faithfulness metrics jointly.\n\n**RL-Obfuscation (adversarial evasion):** RL-Obfuscation (2506.14261) showed 7B-14B models can learn to evade latent-space monitors through RL, with token-level monitors being vulnerable. This is an adversarial finding about monitor fragility, not a characterization of natural faithfulness divergence.\n\n**Faithfulness-improving RL methods:** FaithRL (2602.03507), AtManRL (2604.16158), and faithfulness-aware step-level RL (2602.05897) propose RL objectives that improve faithfulness, but none characterize the divergence trajectory of standard GRPO/RLVR training.\n\n**RL training dynamics:** Learning dynamics papers (2601.04670) show reduced feature diversity during RL but don't track faithfulness. The synthetic phase-transition paper (2602.01017) demonstrates faithful→unfaithful transitions under controlled noise in toy arithmetic — the only prior showing discrete transitions, but in a setting far removed from real GRPO.\n\n**The gap:** No existing work jointly tracks probe-measured latent faithfulness AND surface CoT faithfulness metrics at matched RL training checkpoints across training to characterize divergence dynamics in language reasoning models.\n\n## Approach\nWe produce our own fine-grained GRPO training checkpoints from two architecturally distinct open-weight model families, then jointly measure surface and latent faithfulness at each checkpoint.\n\n**Model families and checkpoint generation:**\n(1) DeepSeek-R1-Distill-Qwen-7B as base model, trained with GRPO using the Open-R1 pipeline (HuggingFace TRL) on MATH + GPQA, saving checkpoints every 50 GRPO steps for ~20 checkpoints across training. This model starts with distilled reasoning capability, letting us study how further RL reshapes faithfulness.\n(2) Qwen3-8B (base dense model, Apache 2.0) trained with the same GRPO pipeline and datasets, providing an architecturally distinct family that starts without distilled reasoning traces.\n\n**Metrics at each checkpoint:**\n(a) *Latent faithfulness proxy*: Train linear probes on residual-stream activations at the last pre-CoT token (following the methodology of Cox et al., 2603.01437), predicting the model's final answer. Report probe AUC and the layer at which AUC first exceeds 0.8 ('commitment layer'). A rising probe AUC across training indicates strengthening answer pre-commitment — the model increasingly 'knows' its answer before reasoning.\n(b) *Surface faithfulness — hint-injection*: Apply Chen et al.'s protocol with sycophancy and anchoring hints on a fixed MMLU/GPQA subset (~500 items). Report hint-acknowledgment rate (lower = more faithful surface behavior).\n(c) *Causal reliance — NLDD*: Compute the Normalized Logit Difference Decay metric (2602.11201) by corrupting individual reasoning steps and measuring confidence drops. Report the Reasoning Horizon k* (the chain-length fraction beyond which steps have negligible causal effect).\n(d) *Activation patching* (on 5 evenly-spaced checkpoints per family): Measure the causal effect of CoT-token activations on the final answer via mean-ablation patching, quantifying how much the model's computation actually flows through the reasoning trace.\n\n**Analysis:**\n- Construct the *surface-latent divergence curve*: plot surface faithfulness improvement (declining hint-acknowledgment rate) against latent bypass strengthening (rising probe AUC / shortening reasoning horizon) across GRPO steps.\n- Apply changepoint detection (PELT algorithm) as an *exploratory* tool to identify whether divergence accelerates at specific training phases — we do NOT claim phase transitions a priori but test for non-linear dynamics.\n- Compare divergence trajectories between the two model families to assess generality.\n- On a subset of checkpoints, apply the probe-trajectory methodology of 'Monitoring the Internal Monologue' (2605.18549) to test whether the character of inference-time probe trajectories (volatility, trend features) changes systematically across training — bridging their token-level and our checkpoint-level analyses.\n\n**Scaling validation:** If initial 7B results show clear divergence, replicate core probe + hint-injection measurements on DeepSeek-R1-Distill-Qwen-14B with ~10 GRPO checkpoints to verify the pattern holds at larger scale.\n\n**Key methodological choices justified:**\n- Using R1-Distill-7B rather than R1-671B: reviewer correctly identified that Dev1/Dev2/Dev3 checkpoints are not publicly available. Distilled 7B models are computationally tractable (single A100 for inference, 8×A100 for GRPO training) and let us generate arbitrarily fine-grained checkpoints.\n- GRPO rather than PPO: GRPO is the algorithm used in DeepSeek-R1 and the VLM checkpoint paper, ensuring comparability.\n- Two model families with different starting points (distilled reasoning vs. base): controls for whether divergence is an artifact of the starting model's reasoning capability.\n\n## Inspiration\nDirect gap between three convergent findings: (1) RLVR monitorability gains NOT from causal reliance (2602.03978), (2) pre-CoT probes show answer pre-commitment exists in residual streams (2603.01437), (3) VLM checkpoint paper shows accuracy-faithfulness trade-off during RL but with no latent-space analysis (2602.12506). The 'Monitoring the Internal Monologue' paper (2605.18549) shows probe trajectories are powerful for monitoring but leaves the training-dynamics dimension unexplored. The Obfuscation Atlas (2602.15515) demonstrates that probing across RLVR checkpoints is technically feasible at scale.\n\n## Key References\n- Reasoning Models Don't Always Say What They Think (Anthropic 2025, arXiv 2505.05410)\n- Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning (arXiv 2026, 2602.03978)\n- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)\n- On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs (arXiv 2026, 2602.12506)\n- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (arXiv 2026, 2605.18549)\n- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (FAR AI/arXiv 2026, 2602.15515)\n- RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? (arXiv 2025/2026, 2506.14261)\n- How Does Unfaithful Reasoning Emerge from Autoregressive Training? A Study of Synthetic Experiments (arXiv 2026, 2602.01017)\n- Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (arXiv 2026, 2602.11201)\n- Learning Dynamics in RL Post-Training for Language Models (arXiv 2026, 2601.04670)\n- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Goodfire/arXiv 2026, 2603.05488)\n- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv 2026, 2602.02496)\n- Catching Rationalization in the Act: Detecting Motivated Reasoning Before and After CoT via Activation Probing (arXiv 2026, 2603.17199)\n- Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models (arXiv 2026, 2603.26410)\n- FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization (arXiv 2026, 2602.03507)\n- AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency (arXiv 2026, 2604.16158)\n- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (DeepSeek 2025, 2501.12948)\n- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv 2025, 2507.18014)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '350–500 A100-hours (GRPO training: ~80 A100-hrs × 2 families = 160 hrs; probe training + inference on ~20 checkpoints × 2 families: ~100 hrs; hint-injection evaluation: ~40 hrs; NLDD computation: ~30 hrs; activation patching on 10 checkpoints: ~50 hrs; 14B scaling validation: ~70 hrs)', 'timeline': '8–11 weeks (2 weeks GRPO training + pipeline setup, 3 weeks probe training & surface measurements in parallel, 2 weeks activation patching & NLDD, 1–2 weeks analysis, 1–2 weeks writing)', 'estimated_gpu_cost': '$900–$1,250 at ~$2.50/A100-hr spot pricing'}\n- **human_in_loop**: {'gpu_hours': '300–400 A100-hours (Claude handles probe training scripts, metric computation pipelines, statistical analysis, and plotting; human designs experiments, interprets results, writes key paper sections)', 'timeline': '6–8 weeks', 'claude_api_cost': '$120–$250 (Sonnet 4.6 for code generation, data analysis scripts, and paper drafting; ~40M input + 8M output tokens)', 'estimated_gpu_cost': '$750–$1,000'}\n- **auto_research**: {'gpu_hours': '300–400 A100-hours', 'timeline': '4–5 weeks (parallelized GRPO training for both families, then parallelized probe training and evaluation across checkpoints)', 'claude_api_cost': '$300–$550 (orchestration agent managing GRPO runs, checkpoint evaluation sweeps, result interpretation, iterative analysis; ~120M input + 25M output tokens)', 'estimated_gpu_cost': '$750–$1,000', 'speed_bottleneck': 'Sequential dependency: GRPO training must complete (or reach sufficient checkpoints) before probe training begins. However, probe training on early checkpoints can start while GRPO training continues. The two model families can be trained in parallel. 14B scaling validation is contingent on 7B results being compelling.'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T18:38:27.952Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:38:27.952Z",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T18:38:27.963Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make a well-informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978) (arXiv 2026):
   核心发现 RLVR 的 surface monitorability 提升来自 response distribution sharpening 和 prompt attention 增强，而非 causal reliance 增强。Monitorability 与 capability 正交。该论文是本 proposal 的直接灵感来源之一，proposal 引用准确。

2. [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437) (arXiv 2026, Cox et al.):
   在 Gemma 2 和 Qwen 2.5 上训练线性 probe，从 pre-CoT residual stream 预测 final answer，AUC >0.9。且证明 probe direction 有因果效力（steering 可 flip 答案 >50%）。Proposal 引用准确，这是其 latent faithfulness proxy 的方法论基础。

3. [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506) (arXiv 2026):
   在 Qwen2.5-VL-7B 的 GRPO checkpoint 上跟踪 accuracy vs. CoT consistency，发现 trade-off。但仅用 LLM-as-judge 表层指标，无 activation probe，且是 VLM 而非 LLM。Proposal 对其局限性的描述准确。

4. [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549) (arXiv May 2026):
   在固定模型的 inference 过程中构建 probe trajectory（逐 token），max-pooling 达 95% AUROC。但只分析 final model，不跟踪 training 过程。极新论文（~2 天前发布），proposal 已引用并正确描述了其局限。

5. [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515) (FAR AI, arXiv 2026):
   在 Llama-3-8B 到 70B 的 GRPO step 上训练 logistic regression deception probes。这是最接近 proposal 的工作——已证明"probing across GRPO checkpoints"技术可行。但 focus 是 reward-hacking obfuscation in coding tasks，不是 general faithfulness，且未联合测量 surface faithfulness。

6. [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261) (arXiv 2025):
   7B-14B 模型可通过 RL 学会逃避 latent-space monitors，token-level monitors 脆弱。这是 adversarial 发现，与 proposal 的"natural divergence"视角互补。

7. [Reasoning Theater: Probing for Performative Chain-of-Thought](https://www.goodfire.ai/research/reasoning-theater) (Goodfire, 2026):
   发现模型在 easy problems 上 coast（生成多余 CoT），probes 可以检测此类 unfaithfulness。快照分析，无 training dynamics。

8. [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053) (arXiv 2026):
   7,186 instances 跨 7 tasks 的 faithfulness benchmark，发现 49.7% 输出含 unfaithfulness。Focus 是 benchmark 设计而非 training dynamics。

- **调研总结**: CoT faithfulness 在 2026 年是极度活跃的领域，但工作沿"表层 behavioral 指标 vs. latent probe 指标"和"固定模型快照 vs. 训练过程"两个维度高度碎片化。确实没有工作在 matched RL checkpoints 上同时测量 surface + latent faithfulness。最接近的是 Obfuscation Atlas（probe across GRPO steps，但 focus 是 deception 而非 general faithfulness）和 VLM checkpoint paper（surface metrics across RL steps，但无 probe）。proposal 的 gap identification 是成立的。

【Trivial Alternative 检验】:

存在两个 trivial alternative 威胁：

(1) **纯 meta-analysis 替代**：既然 RLVR monitorability 论文已经表明 surface gains 与 causal reliance 正交，pre-CoT probes 已经表明 final model 有强 answer pre-commitment——能否直接从现有文献推断"RL 训练必然加剧 surface-latent gap"？答案是：大方向可以推断，但 **divergence 的动态特征**（何时开始、是否存在 phase transition、两个 model family 是否不同）无法从现有工作推断。因此 proposal 的增量价值在于 **temporal resolution 和动态刻画**，而非定性发现本身。这是真实的增量，但这也意味着论文的价值高度依赖于动态特征是否有 non-trivial patterns——如果只是线性渐进 divergence，审稿人可能认为 insight 有限。

(2) **简化实验替代**：proposal 堆了 4 个 metrics（probe AUC, hint-injection, NLDD, activation patching）、2 个 model families、changepoint detection、probe trajectory analysis。一个更简单的版本——只用 probe AUC + hint-injection 在 1 个 model family 的 10 个 checkpoints 上——可能就能回答核心问题。当然，更全面的实验提高 robustness，但这是执行层面的，不改变 idea 本质。

**增量价值判断**：存在但有限。核心 finding 的方向是可预测的，价值集中在 temporal dynamics 的量化刻画上。

【前提假设检验】:

核心 claim 的逻辑链中有以下未经充分验证的假设：

(1) **"Probe AUC = latent faithfulness" 假设**：Proposal 将 pre-CoT probe AUC 上升等同于"latent answer pre-commitment strengthening"。但 probe AUC 可能反映的是 task representation quality 的提升（模型更好地理解问题），而非"在推理前就锁定答案"。Cox et al. 的 activation steering 实验部分支持因果性，但 steering ≠ natural generation pathway。这个等式需要更强的论证。

(2) **"Surface metrics improvement = surface faithfulness improvement" 假设**：Hint-injection acknowledgment rate 下降可能意味着模型变得更不容易被 hint 干扰（robustness），也可能意味着模型学会了不在输出中提及 hint 但仍被 hint 影响（deceptive alignment）。Proposal 对此没有充分讨论。

(3) **"Divergence = RL systematically decouples what models say from what they compute" 的因果推断**：即使观察到 surface-latent divergence 增大，也可能是 RL 让模型在 both dimensions 各自变好但速率不同（而非"decoupling"）。"Decoupling" 暗示某种对抗性关系，而实际可能只是独立变化。

假设(1)是最关键的——如果 probe AUC 不是 latent faithfulness 的有效代理，整个"gap"的解读就会坍塌。

【3 维度打分】:

1. **Novelty: 中** — 
   Gap identification 是成立的：确实没有工作在 matched RL checkpoints 上联合测量 surface + latent faithfulness（Obfuscation Atlas focus 是 deception probes，VLM checkpoint paper 无 latent measures，Monitoring Internal Monologue 只看 inference-time 的 fixed models）。但这个 novelty 本质上是 **组合式的**——将 Cox et al. 的 probe methodology、Chen et al. 的 hint-injection protocol、VLM checkpoint paper 的"checkpoint 采样"思路组合到一起，在 GRPO checkpoints 上 run。没有新方法论、没有新概念框架，核心贡献是 "在正确的时间轴上运行现有工具的组合"。这对于一篇 top venue 论文来说，novelty 偏窄。更关键的是，**核心发现的方向（divergence 加剧）是高度可预测的**——如果结果显示 no divergence 反而更 surprising 也更有影响力，但 proposal 自己都 hypothesize widening gap。

2. **Significance: 中偏强** — 
   研究问题本身对 AI safety 有直接意义："RL 训练是否系统性地让 CoT 变得不可信"是 2026 年的核心问题之一。如果结果清晰，直接影响 deployment monitoring 决策（是否需要 latent-space monitoring infrastructure）。此外，两个 model family 的对比增加了 generalizability。但 significance 受限于：(a) safety community 已经 operate under the assumption that CoT may not be faithful——本研究量化 degree 而非改变 fundamental understanding；(b) 即使证明 divergence 存在，下一步的 actionable advice（"所以我们需要 latent monitoring"）已经是 existing consensus。

3. **Related Work: 强** — 
   这是 proposal 最出色的部分。引用了 15+ 篇 2025-2026 论文，覆盖了 surface faithfulness (Chen et al., VLM checkpoint)、latent probing (Cox et al., Catching Rationalization, Hypocrisy Gap)、probe trajectories (Monitoring Internal Monologue)、deception probing across training (Obfuscation Atlas)、adversarial evasion (RL-Obfuscation)、faithfulness-improving RL (FaithRL, AtManRL)、training dynamics (learning dynamics, synthetic phase transition) 等多个维度。所有引用经调研验证均真实存在且描述准确。gap 的差异化定位清晰——沿 "surface vs. latent" 和 "snapshot vs. longitudinal" 两个轴精确刻画。唯一轻微不足是未讨论 Reasoning Theater (Goodfire, 2603.05488) 虽列在引用中但未深入分析其 probe-based performative detection 与本工作的关系。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】:
Novelty 是限制上界的主要维度。核心贡献是"组合现有方法在新的时间轴上运行"，这在 idea 层面偏 incremental。虽然 gap identification 成立，但预期结果的方向高度可预测（widening divergence），审稿人大概率会写"the main finding confirms what prior work already strongly suggests"。Significance 给了一定的下限支撑——research question 确实重要，对 safety practice 有直接 implications——但不足以突破 novelty 的 ceiling。Related Work 的出色覆盖是加分项，但形式完善不等于 idea 强。

上界 33% 对应的场景是：动态特征出现非常 non-trivial 的 pattern（如 sharp phase transition、两个 model family 完全不同的 divergence trajectory），且审稿人认为这些 finding 本身就是重要贡献。下界 22% 对应的场景是：divergence 呈单调渐进，审稿人认为"we already knew this would happen"。

【主要风险】:
1. **"Expected finding" 问题**：核心 hypothesis（widening gap）是 prior work 的直接外推，如果结果如预测，审稿人会质疑 insight 的增量价值——"quantifying a gap everyone already assumed exists" 不足以撑起一篇 top venue 论文。论文的影响力高度依赖于 temporal dynamics 中是否有 surprising patterns。
2. **Proxy validity 问题**：Probe AUC 作为 "latent faithfulness" 的代理指标的有效性未经充分论证。如果审稿人质疑"probe AUC 上升可能只反映 task representation 改善而非 answer pre-commitment 加剧"，整个 surface-latent gap 的叙事就会被动摇，而 proposal 没有给出 convincing 的反驳。
```

Sources:
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)
- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)
- [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)
- [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)
- [Reasoning Theater: Probing for Performative Chain-of-Thought](https://www.goodfire.ai/research/reasoning-theater)
- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct the evaluation. Let me compile my assessment.

---

```
【阶段】: Triage
```

---

## ⚠️ 前置关键问题：严重的投稿方向错误

在进入 idea 质量评估之前，必须首先指出一个**致命的外部问题**：

**CoRL (Conference on Robot Learning) 2026 明确声明："Submissions without a robotics focus will be returned without review."** 本 proposal 关于 LLM 的 CoT faithfulness 与 RL 训练动态，**与机器人学习零交集**。如果投稿 CoRL，将在 desk rejection 阶段被退回，连进入审稿流程的机会都没有。

本 proposal 的合适投稿方向应为：**ICML 2026 / NeurIPS 2026 / ICLR 2027 / COLM 2026** 等以 ML/NLP/AI Safety 为核心的会议。

**以下 idea 质量评估按 NLP/ML 顶会标准进行（因为 CoRL 的中稿概率固定为 ~0%）。**

---

```
【领域调研】:
```

**1. [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978) (arXiv 2026.02)**
- RLVR 的 surface monitorability 提升来源于 response distribution sharpening 和 increased prompt attention，而非 causal reliance on reasoning traces
- 与本 proposal 的关系：proposal 的核心假设之一直接构建在此发现之上——surface 与 causal reliance 正交性

**2. [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437) (arXiv 2026.03)**
- 线性 probe 在 pre-CoT 残差流上可以 >0.9 AUC 预测最终答案；probe 方向具有因果效力（activation steering 可改变答案）
- 与本 proposal 的关系：proposal 直接采用其方法论作为 latent faithfulness proxy

**3. [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506) (arXiv 2026.02)**
- 在 VLM 的 GRPO checkpoints 上追踪 accuracy-faithfulness trade-off，但仅使用 LLM-as-judge 等 surface metrics
- 与本 proposal 的关系：proposal 声称补充了此工作缺失的 latent-space 分析维度

**4. [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549) (arXiv 2026.05)**
- 在固定模型的推理过程中构建 probe trajectories（token 级别），达到 95% AUROC
- 与本 proposal 的关系：此工作追踪的是推理时的 token 级 probe 轨迹，proposal 追踪的是训练步级 probe 变化——维度互补但不重叠

**5. [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515) (FAR AI, arXiv 2026.02)**
- 在 Llama-3-8B~70B 的 GRPO 训练过程中训练 deception probes，追踪 reward-hacking obfuscation 的出现
- **与本 proposal 的关键关系**：这是最接近的竞争工作——已经展示了"在 RLVR checkpoints 上训练 probes 追踪内部状态变化"的技术路线。只是其关注点是 deception/reward-hacking 而非 general faithfulness

**6. [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261) (arXiv 2025.06)**
- 7B-14B 模型可以通过 RL 学会 evade latent-space monitors，token-level monitors 脆弱，holistic monitors 较鲁棒
- 与本 proposal 的关系：为 proposal 的安全动机提供了支撑——如果模型能 evade monitors，理解 divergence dynamics 更加重要

**7. [Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers](https://arxiv.org/abs/2603.26410) (arXiv 2026.03)**
- 12 个开源推理模型中，thinking tokens 与 answer 之间存在 ~59 个百分点的 hint acknowledgment 差距
- 与本 proposal 的关系：佐证了 surface-latent divergence 的存在，但是 snapshot 分析，无训练动态维度

**8. [Counterfactual Simulation Training for Chain-of-Thought Faithfulness](https://arxiv.org/abs/2602.20710) (arXiv 2026.02)**
- 提出 CST 方法提升 CoT faithfulness
- 与本 proposal 的关系：属于 faithfulness-improving 方法，不直接竞争，但说明领域对 faithfulness 问题的广泛关注

**调研总结**：CoT faithfulness 在 2026 年已成为 AI safety 的热门子领域，但现有工作沿三个独立轴分布：(1) surface metrics across RL training、(2) latent probes on fixed models、(3) deception probes across RL training (针对 reward-hacking)。Proposal 声称的 gap——jointly tracking surface + latent general faithfulness across training——在调研中确实未被覆盖。但最近的 Obfuscation Atlas 在方法论上非常接近（probes across RLVR checkpoints），只是目标变量不同。

---

```
【Trivial Alternative 检验】:
```

**存在中等程度的 trivial alternative 威胁。**

最直接的 trivial alternative 是：**已有的几篇工作（RLVR monitorability + pre-CoT probes + VLM checkpoint 论文）的发现已经逻辑上蕴含了 proposal 的核心假设。** 具体来说：

- RLVR monitorability 论文已证明：surface 改善 ≠ causal reliance 增强
- Pre-CoT probes 论文已证明：模型在生成 CoT 之前就"知道"答案
- VLM checkpoint 论文已证明：RL 训练中存在 accuracy-faithfulness trade-off

将这三个发现拼在一起，一个合理的推论就是：**RL 训练会加剧 surface-latent divergence。** 这不需要做新实验就能 conjecture。

Proposal 的增量价值在于：(1) **量化** 这个 divergence 的 magnitude 和 dynamics（是渐进的还是有 phase transition？）；(2) **跨模型家族的对比**验证 generality；(3) **多个互补 metric 的联合测量**。这些增量是真实的，但它们是"测量一个预期中的现象并提供精确刻画"，而非"发现一个新现象"或"提出一个新方法"。

如果最终结果是"divergence 是渐进且单调的"，那这个结果的信息量较低——"I would have guessed this"。只有在动态呈现非平凡结构（如 phase transition、非单调性、模型家族间的定性差异）时，才有足够的 surprise factor。

---

```
【前提假设检验】:
```

核心 claim 的逻辑链有以下**未经验证的假设**：

1. **"Probe AUC 上升 = answer pre-commitment 加强" 的等价关系。** Probe AUC 的上升也可能反映 RL 训练使得模型的内部表征更加 linearly separable（表征几何变化），而非"模型更早地决定了答案"。Pre-CoT probes 论文在 fixed models 上验证了因果关系（activation steering），但 proposal 没有在每个 checkpoint 做 steering 验证——仅在 5 个 checkpoint 做 activation patching。如果 probe AUC 上升是因为表征空间被 RL 线性化，而非因果 pre-commitment 增强，核心 claim 就不成立。

2. **"Surface faithfulness 改善（hint-acknowledgment rate 下降）= 真正的 faithfulness 进步" 的等价关系。** Chen et al. 的 hint-injection protocol 测量的是 sycophancy/anchoring resistance，而非 general faithfulness。RL 训练可能仅仅让模型学会了"不承认 hint"（一种表面行为），而非真正忽略 hint 的影响。这会使 surface metric 的上升不真正反映 faithfulness 改善，从而使 "surface-latent divergence" 的叙事变得更复杂。

3. **两个模型家族足以支撑 generality claim。** DeepSeek-R1-Distill-Qwen-7B 和 Qwen3-8B 虽然在起始条件上不同（distilled vs. base），但都属于 Qwen 系列架构。架构层面的 diversity 有限。

---

```
【3 维度打分】:
```

**1. Novelty: 弱-中（偏弱）**

理由：
- Proposal 声称的核心 novelty——"jointly tracking surface + latent faithfulness across RL checkpoints"——在概念层面是真实的 gap，经调研确认无直接先例。
- **但**，Obfuscation Atlas (2602.15515) 已经展示了几乎完全相同的技术路线（probes across RLVR checkpoints），只是换了目标变量（deception → general faithfulness）。这意味着 proposal 的方法论 novelty 很低——本质上是将已有方法应用于一个相邻问题。
- 核心假设（RL 加剧 surface-latent divergence）是已有三篇工作逻辑推论的自然延伸，而非一个 surprising 的新 claim。
- "首次联合测量"（first to jointly measure X and Y）是一种常见的 novelty 策略，但当 X 和 Y 各自的工具和发现都已存在时，这种 novelty 的分量较轻。审稿人可能会认为这是 "engineering/measurement contribution" 而非 "scientific contribution"。

**2. Significance: 中**

理由：
- 研究问题本身——理解 RL 如何影响推理模型的内在计算忠实性——是 AI safety 领域的核心问题之一，具有真实的重要性。
- 如果 divergence 存在且系统性很强，这对 RL-trained reasoning models 的部署决策（是否需要 latent-space monitoring）有直接的实践意义。
- **但**，"需要 latent-space monitoring"这一结论已经被多篇工作从不同角度论证（Why Models Know But Don't Say (2603.26410) 明确提出了三层 monitoring 架构的必要性）。Proposal 的主要增量是提供更精确的时间线刻画，但结论方向的 surprise factor 低。
- 对于 NeurIPS/ICML 而言，如果 dynamics 呈现非平凡结构，significance 可以上升到"中-强"；如果只是确认渐进 divergence，则停留在"中"。

**3. Related Work: 强**

理由：
- Proposal 对相关工作的覆盖非常全面且准确。经我调研验证：(1) 所有引用论文确实存在；(2) 对每篇论文的描述准确；(3) 差异化定位清晰——proposal 明确说明了为什么每篇相关工作都只覆盖了部分维度。
- 特别值得肯定的是对 Obfuscation Atlas 和 Monitoring the Internal Monologue 的定位——前者是最强竞争者，proposal 正确识别了其 scope 限制（deception-specific）。
- 覆盖了 faithfulness-improving methods (FaithRL, AtManRL) 作为对比，显示了对领域格局的全面理解。
- 唯一潜在遗漏：Counterfactual Simulation Training (2602.20710) 和 "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?" (2603.22582) 未被提及，但这些工作与 proposal 的核心 gap 关系较弱，不构成重大遗漏。

---

```
【概率估计】: 0-5% (CoRL 2026); 20-30% 中位 25% (若投稿至 ICML/NeurIPS/ICLR 等合适方向)
```

```
【估计理由】:
```

**CoRL 2026: ~0%。** Proposal 与机器人学习完全无关，CoRL 明确声明"Submissions without a robotics focus will be returned without review"。这不是 idea 质量问题，而是根本性的投稿方向错误。

**若投稿至合适的 ML 顶会（ICML/NeurIPS 等）: 20-30%，中位 25%。** 理由如下：

- Related Work 维度强，说明作者对领域有深入理解，proposal 形式质量高。这确保了合理的下限。
- **但 Novelty 是主要瓶颈。** 核心贡献是"联合测量"已有方法论在一个新组合下的应用结果——概念层面的新意有限。Obfuscation Atlas 已经展示了几乎相同的技术路线（probes across RLVR checkpoints）。审稿人很可能写出 "The individual components (probes, hint injection, NLDD) are all borrowed from prior work; the contribution is primarily in combining them" 这样的评价。
- 核心假设（divergence 加剧）是 expected outcome——通过 "I would have guessed this" 测试的概率较高。只有在 dynamics 呈现非平凡结构时才能达到 surprising 的门槛。
- Significance 是中等——问题重要但结论方向已被多篇工作预见。

概率区间反映了：如果 dynamics 呈现 phase transition 等非平凡结构（上界 30%），vs. 如果 dynamics 是渐进单调的（下界 20%，此时 novelty 和 significance 都会被压低）。

```
【主要风险】:
```

1. **"Confirmatory study" 风险（最大风险）：** 核心假设是三篇已有工作的逻辑推论。如果实验结果只是确认"divergence 存在且渐进增加"，审稿人会认为这是一篇 confirmatory empirical study，缺乏足够的 scientific surprise 来支撑顶会录用。Novelty 被降级为 measurement contribution。

2. **Probe AUC 的因果解读风险：** 如果 probe AUC 上升反映的是 RL 线性化表征空间（而非因果 pre-commitment 增强），整个 "surface-latent faithfulness gap" 的叙事框架就会被质疑。Proposal 仅在 5/40 个 checkpoint 做 activation patching，不足以严格支撑每个 checkpoint 的因果 claim。

---

Sources:
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)
- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)
- [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)
- [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)
- [Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers](https://arxiv.org/abs/2603.26410)
- [Counterfactual Simulation Training for Chain-of-Thought Faithfulness](https://arxiv.org/abs/2602.20710)
- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research data. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. **"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning" (2602.03978, 2026)**:
   最直接相关的先驱工作之一。证明 RLVR 的表面可监控性提升来自响应分布收缩和 prompt attention 增加，而非 CoT 因果依赖增强。即：surface gains ≠ causal reliance。本 proposal 的核心假设（surface-latent gap widens）几乎是这篇论文结论的直接推论。

2. **"Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering" (2603.01437, Cox et al. 2026)**:
   在 Gemma 2 和 Qwen 2.5 上证明线性 probe 可以 >0.9 AUC 从 pre-CoT residual stream 中解码最终答案，且该方向是 causal 的（steering 实验）。这是 proposal 的方法论支柱——但该论文只研究 final models，没有训练动态。

3. **"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs" (2602.12506, Apple 2026)**:
   在 Qwen2.5-VL-7B 上发现 RL fine-tuning 的 accuracy-faithfulness trade-off，但仅使用 LLM-as-judge 表面指标，无 activation-level 分析，且是 VLM 而非 LLM。本 proposal 的直接对标和改进目标。

4. **"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes" (2602.15515, FAR AI 2026)**:
   **这是最关键的竞争工作**。已经在 Llama-3-8B through 70B 上跨 GRPO training steps 训练了 logistic regression probes，公开了 500+ 训练模型。方法论（probes across RLVR checkpoints）与本 proposal 高度重叠。区别：该论文聚焦 deception/reward-hacking obfuscation，而非 general faithfulness；未联合测量 surface faithfulness 指标。但技术路径几乎相同。

5. **"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (2605.18549, May 2026)**:
   构建 token-level probe trajectories，95% AUROC 预测推理结果。关键发现：max-pooling 是关键。但仅分析 fixed final models，未追踪 training dynamics。本 proposal 声称要 bridge token-level 和 checkpoint-level 分析。

6. **"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?" (2506.14261, Gupta & Jenner)**:
   7B-14B 模型可通过 RL 学会逃避 latent-space monitors，token-level monitors 脆弱而 max-pooling/attention-based probes 鲁棒。这是对 probe-based monitoring 本身的质疑——若 RL 能学会 evade probes，那 probe AUC 在 training 过程中的变化可能反映的是 evasion 而非 faithfulness。

7. **其他 final-model snapshot 工作**: "Catching Rationalization in the Act" (2603.17199), "The Hypocrisy Gap" (2602.02496), "Why Models Know But Don't Say" (2603.26410), "Reasoning Theater" (Goodfire 2603.05488) — 这些都在不同角度证实了 final models 的 surface-latent divergence，但都是 snapshot 研究。

8. **Faithfulness-improving RL**: FaithRL (2602.03507), AtManRL (2604.16158, ICLR 2026 workshop) — 提出改进 faithfulness 的 RL 方法，但不研究 standard GRPO 的 divergence trajectory。

- **调研总结**: CoT faithfulness 在 2026 是极其拥挤的赛道，已存在大量高质量工作。关键组件——probes across RLVR checkpoints（Obfuscation Atlas）、pre-CoT probe methodology（Cox et al.）、checkpoint-level surface faithfulness tracking（VLM paper）——均已有独立工作。本 proposal 的核心贡献是将这些已有组件组合在一起，联合测量 surface + latent faithfulness across GRPO steps。这是一个 "组合 novelty" 而非 "方法 novelty" 的工作。

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 具体来说：

1. **最直接的 trivial baseline**: 直接使用 Obfuscation Atlas 已公开的 500+ RLVR checkpoints（Llama-3-8B through 70B，GitHub 开源），在其上训练 general faithfulness probes（而非 deception probes），并添加 hint-injection surface metrics。这将以远低于本 proposal 的成本（无需自己跑 GRPO training）达到几乎相同的核心结论。

2. **更简单的推论路径**: RLVR Monitorability 论文已证明 "surface gains ≠ causal reliance"，Pre-CoT Probes 论文已证明 "models pre-commit answers in residual streams"。将两者放在一起，"RL training widens the surface-latent gap" 已是强推论——本 proposal 的实验价值在于 **量化** 这个 gap，而非 **发现** 它。

**增量价值**: 本 proposal 相对于 trivial alternatives 的增量在于：(a) 两个 architecturally distinct model families 的对比，(b) changepoint detection 的时间动态分析，(c) 联合的 NLDD + activation patching 因果分析。但这些都是实验设计层面的增量，不改变核心 insight。

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **"Linear probe AUC 上升 = latent answer pre-commitment 增强" 这个等价关系未必成立。** Probe AUC 上升可能反映 RL training 导致 representation 变得更线性可分（表征空间结构变化），而非模型真的更早"决定"了答案。RL training 改变了 representation geometry，这可能让 probe 更容易 decode，但不等价于 faithfulness 下降。Obfuscation Atlas 和 RL-Obfuscation 论文都表明 RL 可以改变 probe 的可检测性，但方向是复杂的。

2. **"Surface faithfulness metrics (hint-injection) 的改善方向是 monotonic 的" 这个假设过于简化。** Chen et al. 的结果显示 hint-injection rate 先下降后 plateau，但在不同 model families 和 training regimes 下可能呈现不同 pattern。如果 surface metric 也恶化（而非改善），那 "divergence" 的 narrative 就不成立——两者可能同时恶化，即不存在 "gap"。

3. **"GRPO training 的 faithfulness dynamics 可以从 7B distilled models 外推到大规模 models" 这个假设需要谨慎。** Distilled models 的起点（已有 reasoning traces）与 from-scratch RL training 有质的不同。14B scaling validation 是个好设计，但 7B → 14B 的 scaling step 太小，难以说明 generality。

【3 维度打分】:

1. **Novelty: 弱-中 (Weak-Medium)** — 核心贡献是将已有方法组合应用：probe methodology 来自 Cox et al. (2603.01437)，probes across RLVR checkpoints 的技术路径已被 Obfuscation Atlas (2602.15515) 证明可行且开源，surface faithfulness tracking 已有 VLM checkpoint paper (2602.12506) 和 Chen et al. (2505.05410) 的先例。本 proposal 的 novelty 是 "combination novelty"——将这些已有组件组合在一起。虽然 proposal 正确指出 "nobody has jointly measured both"，但这种 "nobody has done X+Y together" 式的 gap 在审稿人看来通常属于 incremental contribution。更关键的是，Obfuscation Atlas 已经做了 probes across RLVR checkpoints 的核心方法论，本 proposal 的差异化（general faithfulness vs. deception）不构成显著的方法论跃迁。

2. **Significance: 中 (Medium)** — 研究问题本身是重要的：理解 RL training 如何影响 reasoning faithfulness 对 AI safety 有直接意义。但如果核心发现是 positive（gap widens），审稿人的反应更可能是 "I would have guessed this"，因为 RLVR Monitorability (2602.03978) 已经告诉我们 surface gains 不来自 causal reliance，Pre-CoT Probes (2603.01437) 已经告诉我们 models pre-commit answers。这两个事实加在一起，gap widening 是 expected outcome。如果发现是 negative（gap doesn't widen），反而更 surprising 更有价值——但 proposal 的 framing 显然 bet on positive result。Significance 的上界受限于 confirmatory nature。

3. **Related Work: 强 (Strong)** — 这是 proposal 最突出的优点。对 2026 年 CoT faithfulness 文献的覆盖极为全面，对每篇相关工作的差异化定位清晰准确。Obfuscation Atlas、RL-Obfuscation、Monitoring Internal Monologue、Pre-CoT Probes、VLM checkpoint paper 等关键竞争工作均被识别并合理定位。唯一的小瑕疵是对 Obfuscation Atlas 的竞争性可能 understate 了——proposal 将其定位为 "deception-specific" 而与自己区隔，但审稿人可能认为从 deception probes 到 general faithfulness probes 的 generalization 是 straightforward 的。

【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
Novelty 是主要限制维度。核心方法论组件均已存在（probes across checkpoints: Obfuscation Atlas; pre-CoT probes: Cox et al.; surface metrics across RL steps: Chen et al. & VLM paper），proposal 的贡献是将它们组合并联合测量。在一个已经非常拥挤的 2026 CoT faithfulness 赛道中，"combination study with existing methods" 面临 "incremental" 的审稿评价风险。Significance 受限于核心假设的 expected nature——如果 positive 结果是大多数人已经预期的，empirical confirmation 的价值被打折。Related work 的高质量和实验设计的完善度提供了一定的 floor（不太可能因为 coverage 不足被拒），但无法弥补 idea 层面 novelty 的不足。概率上界受 novelty 限制在 ~28%；下界由 solid execution plan + important question 支撑在 ~18%。

**关于投稿会议的重要说明**: 本 proposal 的主题是 NLP reasoning model 的 CoT faithfulness 和 RL training dynamics，与 **CoRL (Conference on Robot Learning)** 的 scope 完全不匹配。CoRL 聚焦机器人学习、机器人感知、运动规划等。如果确实投稿 CoRL，中稿概率接近 0%（desk reject）。上述概率估计基于将其投稿到合适的 NLP/ML venue（如 NeurIPS, ICML, ACL, EMNLP）。

【主要风险】:
1. **Novelty 不足风险（最核心）**: 审稿人很可能指出 Obfuscation Atlas 已经做了 "probes across RLVR checkpoints" 的核心工作，本文的差异化（general faithfulness vs. deception + adding surface metrics）不足以构成 top-venue 级别的 novelty。"Nobody has done X+Y together" 这种 gap statement 在拥挤赛道中说服力有限。
2. **Confirmatory bias 风险**: 核心假设（gap widens）是已有 evidence 的直接推论，若实验结果如预期，审稿人可能评价为 "confirmatory study with limited new insight"。Proposal 缺少一个 "如果结果出乎意料会怎样" 的 contingency framing，也缺少一个能区分 "gap widens because of X" vs. "gap widens because of Y" 的 mechanistic hypothesis。
```

Sources:
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)
- [Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)
- [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)
- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199)
- [The Hypocrisy Gap](https://arxiv.org/abs/2602.02496)
- [Why Models Know But Don't Say](https://arxiv.org/abs/2603.26410)
- [FaithRL](https://arxiv.org/abs/2602.03507)
- [AtManRL](https://arxiv.org/abs/2604.16158)
- [Reasoning Theater](https://www.goodfire.ai/research/reasoning-theater)


【原始 proposal（允许参考但不是主要依据）】:
# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models

## Description
We propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.

## Core Problem
When and how does the gap between surface CoT faithfulness (measured by behavioral metrics like hint-injection rates and causal reliance) and latent faithfulness (measured by residual-stream probes predicting answer pre-commitment) develop during GRPO training of reasoning models — and what dynamics characterize this divergence?

## Opportunity
Three converging 2026 findings create a precise, actionable gap. First, the RLVR monitorability paper (2602.03978) showed that RL's surface-monitorability gains come from response distribution sharpening and increased prompt attention — NOT from stronger causal reliance on reasoning traces. Second, pre-CoT probes (2603.01437) demonstrated that instruction-tuned models encode answers in residual-stream activations before generating any CoT (>0.9 AUC), with these directions being causally efficacious. Third, the VLM checkpoint paper (2602.12506) showed an accuracy-faithfulness trade-off during RL fine-tuning — but using only LLM-as-judge surface metrics on vision-language models, with no latent-space analysis. Meanwhile, 'Monitoring the Internal Monologue' (2605.18549) introduced probe trajectories as a powerful inference-time monitoring tool but analyzed only fixed, already-trained models — never tracking how probe characteristics evolve across RL training steps. The Obfuscation Atlas (2602.15515) tracked deception probes across RLVR but focused narrowly on reward-hacking obfuscation rather than general faithfulness divergence. Nobody has jointly measured both surface faithfulness metrics and activation-probe-based latent faithfulness at matched RL training checkpoints to characterize how — and how fast — RL decouples what reasoning models say from what they compute. If this divergence is large and systematic, RL-trained reasoning models require latent-space monitoring beyond CoT inspection for safe deployment.

## Related Work / Landscape
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

## Inspiration
Direct gap between three convergent findings: (1) RLVR monitorability gains NOT from causal reliance (2602.03978), (2) pre-CoT probes show answer pre-commitment exists in residual streams (2603.01437), (3) VLM checkpoint paper shows accuracy-faithfulness trade-off during RL but with no latent-space analysis (2602.12506). The 'Monitoring the Internal Monologue' paper (2605.18549) shows probe trajectories are powerful for monitoring but leaves the training-dynamics dimension unexplored. The Obfuscation Atlas (2602.15515) demonstrates that probing across RLVR checkpoints is technically feasible at scale.

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

## Resource Estimate
- **manual**: {'gpu_hours': '350–500 A100-hours (GRPO training: ~80 A100-hrs × 2 families = 160 hrs; probe training + inference on ~20 checkpoints × 2 families: ~100 hrs; hint-injection evaluation: ~40 hrs; NLDD computation: ~30 hrs; activation patching on 10 checkpoints: ~50 hrs; 14B scaling validation: ~70 hrs)', 'timeline': '8–11 weeks (2 weeks GRPO training + pipeline setup, 3 weeks probe training & surface measurements in parallel, 2 weeks activation patching & NLDD, 1–2 weeks analysis, 1–2 weeks writing)', 'estimated_gpu_cost': '$900–$1,250 at ~$2.50/A100-hr spot pricing'}
- **human_in_loop**: {'gpu_hours': '300–400 A100-hours (Claude handles probe training scripts, metric computation pipelines, statistical analysis, and plotting; human designs experiments, interprets results, writes key paper sections)', 'timeline': '6–8 weeks', 'claude_api_cost': '$120–$250 (Sonnet 4.6 for code generation, data analysis scripts, and paper drafting; ~40M input + 8M output tokens)', 'estimated_gpu_cost': '$750–$1,000'}
- **auto_research**: {'gpu_hours': '300–400 A100-hours', 'timeline': '4–5 weeks (parallelized GRPO training for both families, then parallelized probe training and evaluation across checkpoints)', 'claude_api_cost': '$300–$550 (orchestration agent managing GRPO runs, checkpoint evaluation sweeps, result interpretation, iterative analysis; ~120M input + 25M output tokens)', 'estimated_gpu_cost': '$750–$1,000', 'speed_bottleneck': 'Sequential dependency: GRPO training must complete (or reach sufficient checkpoints) before probe training begins. However, probe training on early checkpoints can start while GRPO training continues. The two model families can be trained in parallel. 14B scaling validation is contingent on 7B results being compelling.'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "55c1f9e4-4dfa-412f-883d-044b76a82f0c",
  "type": "user",
  "uuid": "09280a6f-7316-4164-97a4-c663233ed20c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:38:27.961Z_

```json
{
  "parentUuid": "09280a6f-7316-4164-97a4-c663233ed20c",
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
  "uuid": "0be2b28d-dfc8-4698-beff-5a4c892999d6",
  "timestamp": "2026-05-19T18:38:27.961Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:38:27.961Z_

```json
{
  "parentUuid": "0be2b28d-dfc8-4698-beff-5a4c892999d6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "64195c95-5e84-4ac6-b502-bc7ceabc1f96",
  "timestamp": "2026-05-19T18:38:27.961Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a well-informed assessm…",
  "leafUuid": "64195c95-5e84-4ac6-b502-bc7ceabc1f96",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze surface-latent faithfulness gap in RLVR training",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:38:57.622Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them as the Meta Judge.

Let me extract the key data points:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability: [22% - 33%] 中位 27%
- Key risks: "Expected finding" problem, Probe AUC proxy validity

**Reviewer 2:**
- Novelty: 弱-中（偏弱）(Weak-Medium, leaning weak)


- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [20% - 30%] 中位 25% (for appropriate ML venue); ~0% for CoRL
- Key risks: "Confirmatory study" risk, Probe AUC causal interpretation, and flagged that CoRL is the wrong venue entirely

**Reviewer 3:**
- Novelty: 弱-中 (Weak-Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [18% - 28%] 中位 22%
- Key risks: Novelty insufficiency concerns around Obfuscation Atlas overlap and confirmatory bias, also noting CoRL as wrong venue

Looking at the three median probabilities of 27%, 25%, and 22%, I'm calculating the mean at about 24.67% with a median of 25%. The standard deviation comes out to roughly 2.05%, which is well below the 3% threshold, indicating strong consistency across reviewers. The consensus is clear on novelty concerns across all three reviews.

Now examining where reviewers align: all three identify weak-to-medium novelty as the primary bottleneck, rate significance as medium, and flag strong related work coverage. They're unanimous on the confirmatory study risk, the probe AUC validity concern, and Obfuscation Atlas as the closest competitor. Only R2 and R3 explicitly mention CoRL as the wrong venue, while R1's slightly more generous significance rating is a minor outlier I should downweight.

The consistency across estimates is remarkably tight at about 2% standard deviation, clustering around 22-27%. Given this convergence, I'll anchor to the median of 25% but apply the conservative principle and shift slightly toward R3's stricter 22% assessment. My final range is 19-29% with a median of 24%.

But there's a critical issue I need to separate out: two of the three reviewers flagged that CoRL is fundamentally the wrong venue for this work since it has no robotics component—that's a desk rejection scenario. So I need to give two estimates: the CoRL submission probability is essentially 0%, and then provide a separate assessment for what would happen if this were submitted to an appropriate venue instead. I should also pull together the implementation feasibility details from the resource estimates provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64195c95-5e84-4ac6-b502-bc7ceabc1f96",
  "isSidechain": false,
  "requestId": "req_011CbCQyLN6mXjU3gCY3UKDH",
  "type": "assistant",
  "uuid": "217fa271-7acf-4d33-b051-e1bfec102790",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W21hrBshm3yeV4yTb3EVAv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23748,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3112,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23748
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

_source line 9 · 2026-05-19T18:39:40.531Z_

【阶段】: Meta Judge
【三次中位】: [27%, 25%, 22%]  std=2.1%
【共识维度】: 
- **Novelty: 弱-中（3/3 一致）**——三位审稿人均判定核心贡献属于"组合 novelty"（combination novelty），将 Cox et al. 的 probe 方法论、Obfuscation Atlas 的 checkpoint probing 技术路径、Chen et al. 的 hint-injection protocol 组合应用。无新方法论、无新概念框架。Obfuscation Atlas (2602.15515) 已展示几乎相同的技术路线（probes across RLVR checkpoints），差异化仅在目标变量（deception → general faithfulness）。
- **Significance: 中（3/3 一致）**——研究问题对 AI safety 重要，但核心假设（divergence widens）是已有工作的直接逻辑推论，confirmatory nature 限制了 surprise factor。
- **Related Work: 强（3/3 一致）**——proposal 最突出的优点，15+ 篇 2025-2026 论文全面覆盖，引用准确，差异化定位清晰。
- **"Expected Finding" / Confirmatory Study 风险（3/3 一致，#1 风险）**——三位审稿人均指出：RLVR monitorability (surface ≠ causal reliance) + pre-CoT probes (answer pre-commitment exists) 两篇工作的结论加在一起，gap widening 是 expected outcome。若实验仅确认此预期，审稿人大概率评价为"quantifying what we already assumed"。
- **Probe AUC 代理有效性质疑（3/3 一致）**——probe AUC 上升可能反映 RL 线性化表征空间（representation geometry 变化），而非因果性 answer pre-commitment 增强。Proposal 仅在 5/40 个 checkpoint 做 activation patching，因果论证链不够严密。
- **CoRL 投稿方向错误（2/3 明确指出）**——CoRL 聚焦 robot learning，本 proposal 与机器人学习零交集，将在 desk rejection 阶段被退回。
【异常维度】: 
- 审稿人 1 给 Significance "中偏强"，略高于另两位的"中"——属于轻微乐观偏差，降权处理（R1 对 safety 实践意义赋权稍高，但 R2/R3 指出 "需要 latent monitoring" 已是 existing consensus，限制了 actionable novelty）。
- 审稿人 3 提出 Obfuscation Atlas 已公开 500+ checkpoints 可直接复用的 trivial alternative——仅 R3 明确提出此路径，但这实际上强化了 novelty 不足的共识判断，不是 outlier 而是补充论据。
【最终概率】: [18% - 28%] 中位 23%
【一致性】: 高（std=2.1% < 3%，rubric 维度判决完全一致）
【综合理由】: 
三位审稿人在所有核心维度上高度一致：Novelty 弱-中、Significance 中、Related Work 强。概率中位分布在 22-27% 的窄带内（std=2.1%）。根据高一致性规则，取中位附近并缩窄区间。R1 的 27% 稍偏乐观（Significance 给了"中偏强"），R3 的 22% 最严格但论证充分（Obfuscation Atlas 的方法论重叠被 R3 论述得最清晰）。按"宁缺毋滥"原则，最终中位偏向 R2/R3 方向取 23%。

关键逻辑：**Novelty 是决定性瓶颈**。当 Novelty 在弱-中区间时，即使 Significance 中等、Related Work 出色、实验设计完善，概率天花板约在 30%。三位审稿人对此判断完全一致，无需调整。

**投稿方向致命问题**：若确实投稿 CoRL 2026，中稿概率 ≈ 0%（desk reject，2/3 审稿人明确指出）。上述 [18%-28%] 中位 23% 的估计**仅适用于合适的 ML/NLP/Safety venue**（NeurIPS 2026、ICML 2026、ICLR 2027 等）。

【建议】: 不推荐（投稿 CoRL）/ 边缘（投稿合适 ML venue，需显著提升 novelty angle）

【实施评估】:
  - 计算资源: 350-500 A100-hours（GRPO 训练 ~160 hrs + probe 训练与推理 ~100 hrs + 评测与 patching ~120 hrs + 14B scaling ~70 hrs）。约 $900-$1,250 spot pricing。单机 8×A100 可完成训练，单卡 A100 可完成推理。资源门槛中等偏低，可行。
  - 数据需求: MATH + GPQA 作为 GRPO 训练数据，MMLU/GPQA 子集（~500 items）用于 hint-injection 评测。全部为公开数据集，无获取障碍。
  - 人工介入: 需要研究者设计实验、解读结果、撰写核心论文章节。Probe 训练脚本和 metric 计算可自动化。人工工作量集中在实验设计和 insight 提取，约 2-3 人周。
  - 训练需求: 需要训练 GRPO（2 个 model family × ~1000 steps），每个 checkpoint 训练线性 probe。不需要训练全新大模型，但 GRPO 训练本身是必须的（不可避免的计算成本）。注：如复用 Obfuscation Atlas 公开的 500+ checkpoints，GRPO 训练成本可大幅降低，但会引入模型家族差异（Llama vs. Qwen）。
  - 新 Benchmark: 不需要构建新 benchmark。使用现有 MATH/GPQA/MMLU 数据集和已有评测 protocol。
  - 预估周期: 6-11 周（取决于人工/自动化程度）。关键路径：GRPO 训练（2 周）→ probe + surface 评测（3 周，可与训练部分并行）→ 分析与写作（2-3 周）。14B scaling validation 是条件触发的额外 1-2 周。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "217fa271-7acf-4d33-b051-e1bfec102790",
  "isSidechain": false,
  "requestId": "req_011CbCQyLN6mXjU3gCY3UKDH",
  "type": "assistant",
  "uuid": "3d17cc0a-b8ae-4436-bce0-9581d41737c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W21hrBshm3yeV4yTb3EVAv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23748,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3112,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23748
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a well-informed assessm…",
  "leafUuid": "3d17cc0a-b8ae-4436-bce0-9581d41737c5",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze surface-latent faithfulness gap in RLVR training",
  "sessionId": "f1b6f5d0-0909-4a94-9b0f-b9df8080ba4e"
}
```

---
