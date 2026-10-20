# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/5f5cea7c-74aa-4f26-a86e-c8a24f574c29.jsonl`
- **Structured JSON:** [`3dff4dc5d16f9cc9786e.json`](../../sessions/3d/3dff4dc5d16f9cc9786e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:03:42.905Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:03:42.905Z",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to write the triage assessment. Let me synthesize my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437) (arXiv, Mar 2026): 直接竞争工作。已证明 pre-CoT residual stream 上的 linear probe 可达 0.9 AUC 预测最终答案，且 probe direction 具有因果性（steering 可翻转答案 >50% 的案例）。本 proposal 的 metric (1)（pre-CoT probe AUC）本质上是该论文方法的直接复用。\n- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488) (arXiv, Mar 2026): 高度相关。在 DeepSeek-R1 671B 和 GPT-OSS 120B 上用 activation probing 证明模型在 CoT 远早于完成时即已 commit 到最终答案，CoT 后段是 \"performative reasoning\"。直接支持 \"latent commitment precedes surface reasoning\" 的叙事——但也意味着这一发现已经被建立。\n- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning](https://arxiv.org/abs/2602.11201) (arXiv/ICLR 2026 LIT Workshop): 本 proposal 的 metric (3) NLDD 和 \"reasoning horizon\" 概念的原始出处。已经定义了 Reasoning Horizon (k* ≈ 70-85% chain length) 以及 step-level faithfulness 的度量框架。\n- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978) (arXiv, Feb 2026): 本 proposal 直接引用的核心发现——RLVR 的 surface monitorability 改善主要来自 response distribution sharpening 和 prompt attention 增强，而非 causal reliance 加强。本 proposal 的中心假设（surface gains orthogonal to causal reliance）直接建立在此工作之上。\n- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506) (arXiv, Feb 2026): 已对 VLM 的 RL finetuning checkpoints 进行 faithfulness 追踪，发现 accuracy-faithfulness trade-off（准确率提升但 reasoning consistency 下降）。本 proposal 自我定位为该工作的扩展（加入 latent probe metrics + 文本 reasoning models）。\n- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549) (arXiv, May 2026): 在固定模型上构建 probe trajectory（每个 token 处评估 probe），发现 full trajectory 比 single-point prediction 提供更好的可分离性。本 proposal 自我定位为该工作的互补（加入训练时间维度）。\n- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053) (arXiv, Feb 2026): 跨 12 个开源 reasoning model 的 faithfulness benchmark，发现 49.7% 输出存在 unfaithfulness，且与 post-training regimes 相关。\n- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199) (arXiv, Mar 2026): 用 activation probing 在 CoT 前后检测 motivated reasoning，方法论与本 proposal 高度重叠。\n\n- 调研总结: CoT faithfulness / latent-vs-surface gap 是 2025 下半年-2026 上半年的研究热点，已有大量工作从不同角度（probing、causal intervention、steering、benchmark）建立了\"模型在 CoT 之前即已 commit 答案\"和\"RL 训练提升 surface 指标但不增强 causal reliance\"的核心叙事。本 proposal 的贡献定位是将这些已有发现的工具组合起来，在训练时间维度上进行纵向追踪——这是一个尚未被填充的具体组合空白，但并非概念性创新。\n\n【Trivial Alternative 检验】:\n存在显著的 trivial alternative 威胁。核心问题是：**取 3-5 个关键 checkpoints（初始、early RL、mid RL、late RL）而非 ~20 个 fine-grained checkpoints，直接复用 2603.01437 的 pre-CoT probe + 2602.11201 的 NLDD + 标准 hint-injection protocol，是否能回答同样的核心问题？** 答案很可能是\"是\"。\n\n~20 个 checkpoints + changepoint detection 的增量价值在于能够刻画 gap 的具体动态轨迹（是线性增长、阶梯式跳变、还是先缩后扩？），但：(a) 如果结果符合假设（monotonic widening），那么粗粒度采样就够了；(b) 如果结果不符合假设（非单调），那 changepoint detection 的发现才有价值，但这依赖于特定的实验结果——proposal 不能在 idea 层面 guarantee 这一点。\n\n此外，\"Monitorability as a Free Gift\"(2602.03978) 已经在 RLVR 训练过程中追踪了 monitorability 的变化动态，虽然未使用 probe-based latent measures，但其核心结论（surface ≠ causal reliance）已经建立。本 proposal 的增量是用更精细的工具确认这一已知结论在 GRPO + text reasoning models 上的适用性。\n\n【前提假设检验】:\n1. **Linear probe AUC = \"latent answer commitment\"**: 这是核心假设中最关键的一环。2603.01437 提供了因果证据（steering 可翻转答案），但 linear probes 的解释性仍有争议——高 AUC 可能反映 residual stream 中的 task-relevant features 而非真正的 \"commitment\"。Proposal 直接将 probe AUC 等同于 latent faithfulness 的度量，但这一等价关系本身需要论证，不能简单借用。\n2. **Surface faithfulness metrics 的有效性**: Hint-injection acknowledgment rate 作为 \"surface faithfulness\" 的 proxy 也并非无争议。模型不 acknowledge hint 可能是因为 faithfully 忽略了无关信息，而非 unfaithfully 隐藏了使用。\n3. **GRPO 训练 = widening gap**: 中心假设假定 GRPO 训练系统性地扩大 gap，但这可能高度依赖于 (a) reward function 的设计、(b) training data 的分布、(c) 模型初始化。两个模型家族不足以建立 \"GRPO training systematically decouples\" 的 general claim。\n4. **两个模型家族足以代表 \"architecturally distinct\"**: DeepSeek-R1-Distill-Qwen-7B 和 Qwen3-8B 虽然起点不同（distilled vs. base），但 Qwen 系列本身架构相近，代表性有限。\n\n【3 维度打分】:\n  1. Novelty: 弱 — 四个测量工具（pre-CoT probe, hint-injection, NLDD, activation patching）均直接借自 2603.01437、2602.11201、Chen et al. 等已有工作，无方法论创新。贡献仅在于\"将已有工具在训练 checkpoint 维度上组合应用\"——这是实验设计层面的组合，而非概念或方法论层面的创新。2602.12506 已经做了 VLM 的 checkpoint 级 faithfulness 追踪，2602.03978 已经建立了 \"surface ≠ causal reliance\" 的 RLVR 训练动态结论。本 proposal 填充的是一个具体的 \"组合空白\"（latent probes × training checkpoints × text reasoning models），但剔除 surface differences 后，核心 insight 增量有限。\n  2. Significance: 中 — 研究问题本身（RL 训练是否系统性地解耦模型的表面推理与内部计算）对 AI safety 和 reasoning model 部署决策有实际意义。但问题在于：如果核心发现是 positive（gap widens），审稿人大概率会说 \"I would have guessed this\"——因为 2602.03978 的 monitorability 结论和 2603.05488 的 \"Reasoning Theater\" 发现已经强烈暗示了这一方向。如果结果是 negative 或 non-monotonic，那倒是 surprising 的，但 proposal 将自己框定为假设确认性研究（\"central hypothesis is that GRPO training creates a widening gap\"），限制了意外发现的叙事空间。对领域的推动力更接近 \"confirmatory evidence for an emerging consensus\" 而非 \"new insight\"。\n  3. Related Work: 中 — Proposal 对 2602.12506 和 2605.18549 的定位清晰，但明显遗漏了两篇高度相关的竞争工作：(a) \"Reasoning Theater\"(2603.05488) 的 activation probing 发现直接挑战了本 proposal 的增量价值（performative CoT 已被 established）；(b) \"Decoding Answers Before CoT\"(2603.01437) 作为 pre-CoT probe 的原始工作，其 causal evidence 对本 proposal 的假设检验至关重要但未被充分讨论。此外，\"Catching Rationalization in the Act\"(2603.17199) 使用了高度类似的方法论（activation probing 检测 CoT 前后的 commitment）也未被提及。Related work 覆盖有明显盲区。\n\n【概率估计】: [12% - 22%] 中位 17%\n【估计理由】: Novelty 是主要限制维度。这个 proposal 的核心贡献是\"工具组合 × 时间维度\"的实验设计，而非概念性或方法论的创新。在一个已经有 6-8 篇高度相关的 2026 年论文建立了 \"CoT faithfulness is problematic + latent commitment precedes surface reasoning + RL surface gains ≠ causal reliance\" 叙事的领域，本 proposal 提供的增量是用更精细的工具确认已知结论在 GRPO training dynamics 上的适用性。中心假设的预期结果（gap widens）并不 surprising，限制了即使实验完美执行后的 impact 上限。Significance 给了它一定的下限支撑（问题本身重要），但 novelty 的弱势严重限制了上界。如果投稿 top venue 主会（NeurIPS/ICML/ICLR），作为 empirical study 需要在发现层面有 surprise element 才能突破 25%，而当前 framing 不具备这一条件。\n【主要风险】: \n1. **\"Confirmatory study\" 定位的致命性**：中心假设（gap widens）是现有文献的自然推论，审稿人极可能评价为 \"expected result, limited novelty\"。如果 proposal 不将自己重新框定为 exploratory/discovery-oriented（例如：\"我们不知道 gap 的动态轨迹是什么形状，这是首次精确刻画\"），confirmatory framing 本身就是最大的拒稿风险。\n2. **方法论零创新的可累积负面印象**：四个 metrics 全部直接复用已有工作，无任何方法论贡献。对于 empirical study track，审稿人对\"全用别人的工具做新实验\"的容忍度有限——至少需要一个 methodological contribution（例如：新的 gap 度量、新的 probe 训练方式、或对已有 metric 的系统性比较/改进）来支撑 paper 的学术贡献。\n```\n\nSources:\n- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)\n- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488)\n- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning](https://arxiv.org/abs/2602.11201)\n- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)\n- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)\n- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)\n- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)\n- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough information to make a thorough assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **\"Reasoning Models Don't Always Say What They Think\" (Anthropic, arXiv 2505.05410, May 2025)**:\n   本 proposal 引用的 Chen et al. hint-injection 协议的原始来源。该工作发现 Claude 3.7 Sonnet 仅 25% 的情况下承认 hint 的影响，DeepSeek-R1 为 39%。建立了 surface faithfulness 的标准测量方法。与本 proposal 的关系：proposal 直接复用其 hint-injection 协议作为 surface metric，无方法论创新。\n\n2. **\"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\" (Cox et al., arXiv 2603.01437, March 2026)**:\n   **最直接竞争工作。** 该论文已经在 pre-CoT residual stream activations 上训练线性 probe，实现 0.9 AUC 预测最终答案，并证明这些方向不仅是 predictive 还是 causal（activation steering 可以在 >50% 的案例中翻转答案）。与本 proposal 的关系：proposal 的 latent answer-commitment proxy（metric 1）与该工作高度重叠，差异仅在于本 proposal 沿 training checkpoints 追踪。\n\n3. **\"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning\" (Xiong et al., arXiv 2602.03978, Feb 2026)**:\n   **核心竞争 + 前置工作。** 该论文已经发现 RLVR 的 monitorability gains 来自 response distribution sharpening 和 increased attention to prompt，**而非 stronger causal reliance on reasoning traces**。即 surface gains 与 causal reliance 是 orthogonal 的。与本 proposal 的关系：proposal 的核心假设（\"surface-latent gap widens\"）可以被视为该工作结论的直接推论——如果 surface gains 与 causal reliance orthogonal，那么沿 training 追踪两者自然会看到 divergence。\n\n4. **\"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\" (ICLR 2026, arXiv 2602.11201)**:\n   引入 NLDD（Normalized Likelihood Displacement）指标，发现 Reasoning Horizon 在 chain length 的 70-85% 处，之后的 reasoning tokens 对最终答案贡献很小甚至为负。与本 proposal 的关系：proposal 直接复用 NLDD 作为 metric 3，无方法论创新。\n\n5. **\"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (arXiv 2605.18549, May 2026)**:\n   在固定模型上追踪 probe trajectories across inference tokens，发现 max-pooling 可达 95% AUROC。与本 proposal 的关系：proposal 明确定位自身与该工作的差异——该工作是\"inference-time probe trajectory on fixed models\"，本 proposal 是\"training-time probe trajectory across checkpoints\"。但两者的方法论思路高度同构。\n\n6. **\"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\" (arXiv 2602.12506, Feb 2026)**:\n   在 VLM 上做 RL checkpoint 研究，发现 RL finetuning 提升 headline accuracy 但 reasoning 变得 increasingly inconsistent。与本 proposal 的关系：proposal 明确区分自身——该工作仅用 LLM-as-judge surface metrics 且在 VLM 上。\n\n7. **\"Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs\" (arXiv 2512.22631, Dec 2025)**:\n   直接评估 GRPO 和 DPO 对 CoT faithfulness 的影响，发现 GRPO 在大模型上优于 DPO。与本 proposal 的关系：该工作已评估 GRPO 对 faithfulness 的影响，但未做 checkpoint-level 纵向追踪，也未使用 latent probes。\n\n8. **\"Faithful GRPO\" (arXiv 2604.08476, April 2026)**:\n   在 GRPO reward 中加入 faithfulness 约束，将 inconsistency rate 从 24.5% 降到 1.7%。与本 proposal 的关系：从干预角度解决了 GRPO faithfulness 问题，而 proposal 是从诊断角度追踪。\n\n- **调研总结**: CoT faithfulness 领域在 2025-2026 年极度拥挤。Pre-CoT probes 已被证明能以 0.9 AUC 预测答案（Cox et al.），RLVR 的 monitorability 与 causal reliance 的正交性已被建立（Xiong et al.），NLDD 已在 ICLR 2026 发表。本 proposal 处于这些工作的\"交叉合成\"位置——将已有的四个独立 metrics 应用于 GRPO training checkpoints 这一新维度。核心创新是时间维度的追踪粒度，而非方法论或理论层面的突破。\n\n\n【Trivial Alternative 检验】:\n\n存在一个明显的低成本替代方案：**取 3 个 checkpoint（early/mid/final）而非 ~20 个，用相同的 4 个 metrics 做快照对比。** 如果核心发现只是\"latent pre-commitment 增强而 surface faithfulness 停滞\"，这个 3-point 设计就够了，不需要 20 个 checkpoint 的 fine-grained 追踪。\n\nProposal 的增量价值在于：(1) fine-grained dynamics 可能揭示非线性转变点（changepoint detection），这确实需要密集 checkpoint；(2) 两个架构族的对比可能揭示 architecture-dependent 差异。但这些增量价值的大小取决于结果是否显示有趣的非线性 pattern——如果 divergence 是单调渐进的，那 3-point 设计就足够传达全部信息。\n\n**更根本的 trivial alternative 威胁**：Xiong et al. (2602.03978) 已经在机制层面解释了为什么 surface ≠ latent（entropy reduction vs. causal reliance），那么沿 training checkpoints 追踪这个 divergence 的 *empirical confirmation* 的增量价值到底有多大？审稿人可能会问：\"We already know WHY these diverge; showing WHEN they diverge adds limited insight.\"\n\n\n【前提假设检验】:\n\n1. **\"Linear probe AUC on pre-CoT activations 是 latent answer-commitment 的有效 proxy\"**——这个假设有实证支撑（Cox et al. 2603.01437 达到 0.9 AUC），但有一个重要 caveat：probe 是在**单个 checkpoint 的数据上训练的**。当追踪 ~20 个 checkpoints 时，每个 checkpoint 的 representation space 可能发生剧烈变化，probe 的 transferability 是一个未解决的问题。如果每个 checkpoint 重新训练 probe，那 AUC 的变化可能反映 probe 训练的 variance 而非真实的 latent commitment 变化。这是一个 methodological gap。\n\n2. **\"GRPO training 会创造 widening gap\"（核心假设）**——这更像是从 Xiong et al. 的 orthogonality finding 直接推导出的 prediction，而非一个需要 elaborate study 来验证的假设。如果结果是 positive（gap widens），审稿人会说\"this follows logically from the monitorability paper\"；如果结果是 negative（gap doesn't widen），那 changepoint detection 的整套框架就失去了意义。这是一个\"难以 surprise 审稿人\"的假设。\n\n3. **\"两个 model families 的差异有 informative 的架构归因\"**——仅有两个 model families（一个 distilled，一个 base）无法在架构 vs. 训练数据 vs. 初始化 之间做因果归因。任何差异都可能来自 confounds。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — 核心贡献是将 4 个已有 metrics（pre-CoT linear probe [Cox et al. 2603.01437]、hint-injection [Chen et al. 2505.05410]、NLDD [2602.11201]、activation patching）应用于 GRPO training checkpoints 这一新维度。方法论层面无任何创新——全部是 off-the-shelf tools 的直接应用。时间维度的追踪确实填补了一个 gap，但这是一个\"measurement study\"式的 gap，而非概念或方法论的 gap。更关键的是，核心假设（surface-latent divergence）已经可以从 Xiong et al. (2602.03978) 的 orthogonality 结论直接推导出来，降低了发现的 surprisingness。在 CoT faithfulness 这个 2025-2026 年极度拥挤的领域，仅靠\"在新维度上做 measurement\"难以构成强 novelty。\n\n2. **Significance: 中** — 研究问题本身是重要的：如果 RL training 系统性地 decouples surface from latent，这对 AI safety monitoring 有直接实践意义。但实际 significance 受限于两个因素：(a) Xiong et al. 已经从机制角度解释了 why this happens（entropy reduction），temporal dynamics 的补充价值是 incremental 的；(b) 仅在 7B/8B 的 open-weight models 上做，对 frontier model safety monitoring 的 generalizability 存疑。如果核心发现是 positive（gap widens），审稿人大概率会说 \"I would have guessed this given the monitorability paper\"。实际 surprise potential 较低。\n\n3. **Related Work: 强** — Proposal 对已有工作的覆盖相当充分，正确引用了 2602.12506（VLM checkpoint）、2605.18549（probe trajectories at inference）、2602.03978（RLVR monitorability），并清晰定位了自身的差异化。但正是因为 related work 做得好，反而暴露了 novelty 的薄弱——每个差异化声明都是\"unlike X which only did Y, we also do Z\"，这种\"existing work A + B + C + new axis\"的定位模式容易被审稿人读为 incremental combination。\n\n\n【概率估计】: [18% - 28%] 中位 22%\n\n【估计理由】:\nRelated Work 维度强，说明 proposal 的学术定位是 well-informed 的，这提升了下限。但 Novelty 弱-中 严重限制了上界：核心贡献是已有 metrics 在新维度上的应用（measurement study），且核心假设可从已有工作（Xiong et al. 的 orthogonality 结论）逻辑推导，降低了 surprise potential。Significance 中等——问题重要但预期发现不够 surprising。三个维度综合指向 borderline-reject 区间。Novelty 是主要限制因素。\n\n**额外注意：venue mismatch 风险。** 如果目标 venue 确实是 CoRL（Conference on Robot Learning），本 proposal 与机器人学习完全无关，中稿概率接近 0%。上述概率估计基于假设目标 venue 为 NeurIPS/ICML/ICLR 等 ML/AI 主会或 COLM/EMNLP 等 NLP 会议。请确认目标 venue。\n\n【主要风险】:\n1. **\"Predictable finding\" 风险**：核心假设（surface-latent gap widens during GRPO training）可被视为 Xiong et al. orthogonality 结论的直接 corollary。如果审稿人认为\"我们已经知道 WHY 它们 diverge，那么 WHEN 它们 diverge 的 empirical confirmation 是 incremental 的\"，这将是 rejection 的主要依据。\n2. **\"Combination without insight\" 风险**：4 个 off-the-shelf metrics × 20 checkpoints × 2 model families = 大量实验，但审稿人可能会问\"beyond confirming the expected divergence, what new theoretical or mechanistic insight does this temporal tracking provide?\" 如果 changepoint detection 未能揭示 non-trivial 的 phase transition pattern，整个 fine-grained 追踪的 motivation 会被质疑。\n```\n\nSources:\n- [Reasoning Models Don't Always Say What They Think (Chen et al., 2025)](https://arxiv.org/abs/2505.05410)\n- [Decoding Answers Before Chain-of-Thought (Cox et al., 2026)](https://arxiv.org/abs/2603.01437)\n- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning (Xiong et al., 2026)](https://arxiv.org/abs/2602.03978)\n- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (ICLR 2026)](https://arxiv.org/abs/2602.11201)\n- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)\n- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)\n- [Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs](https://arxiv.org/abs/2512.22631)\n- [Faithful GRPO (VLM)](https://arxiv.org/abs/2604.08476)\n- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?](https://arxiv.org/abs/2603.22582)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. Cox et al. \"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\" (arXiv 2603.01437, Mar 2026):\n   - 与本 proposal 的关系：**最直接的竞争工作**。已经证明在指令微调模型上，线性探针可以在 pre-CoT residual-stream activations 上以 >0.9 AUC 预测最终答案，且这些方向不仅是预测性的，还是因果性的（activation steering 可以在 >50% 的情况下翻转答案）。\n   - 关键发现：模型在生成 CoT 之前就已经\"决定\"了答案。本 proposal 的核心度量之一（线性探针 AUC on pre-CoT activations）已被该工作系统验证。\n\n2. \"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning\" (arXiv 2602.03978, Feb 2026):\n   - 与本 proposal 的关系：**核心假设的直接来源**。本 proposal 的中心假设（\"surface gains are orthogonal to causal reliance\"）直接引用该论文的发现。\n   - 关键发现：RLVR 的 monitorability 提升主要来自 response distribution sharpening（熵降低）和对 prompt 注意力增加，**而非更强的 causal reliance on reasoning traces**。这意味着 surface-level 的改善与 latent reasoning 的改善是解耦的——即本 proposal 要验证的核心主张已有强证据支持。\n\n3. \"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\" (arXiv 2602.12506, Feb 2026):\n   - 与本 proposal 的关系：proposal 显式定位自己相对于该工作的增量——本 proposal 声称该工作\"仅使用 LLM-as-judge 的表面指标\"而缺乏 latent measures。\n   - 关键发现：在 VLM 上追踪 RL finetuning 中间 checkpoints，发现 accuracy 提升但 reasoning consistency 下降——即 surface-latent gap 在 VLM 场景已被观察到。\n\n4. \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (arXiv 2605.18549, May 2026):\n   - 与本 proposal 的关系：proposal 显式定位——该工作在**固定模型**上追踪推理过程中的 probe trajectories，缺乏**跨训练的时间维度**。\n   - 关键发现：probe trajectories（在推理的每个 token 处评估探针）能提取推理动态信息，max-pooling 达到 95% AUROC。\n\n5. \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\" (arXiv 2602.11201, Feb 2026):\n   - 与本 proposal 的关系：NLDD 指标和 Reasoning Horizon 概念的来源论文。proposal 借用其 NLDD 作为 causal reliance 度量。\n   - 关键发现：在 70-85% 的 chain length 之后，reasoning tokens 对最终答案几乎没有或有负面影响。\n\n6. RFEval (arXiv 2602.17053, Feb 2026):\n   - 与本 proposal 的关系：从 benchmark 角度验证了同一现象。\n   - 关键发现：在 SFT 之上添加 RL-style 目标**可以降低 reasoning faithfulness**，即使 accuracy 保持不变。这直接支持了 proposal 的\"gap 加宽\"假设，但也意味着该假设已有实证支撑。\n\n7. \"Faithful GRPO\" (arXiv 2604.08476, Apr 2026):\n   - 与本 proposal 的关系：从解决方案角度反映同一问题——如果 GRPO 本身不产生 faithfulness gap，就不需要\"Faithful GRPO\"。\n   - 关键发现：通过 constrained policy optimization 可以显著降低 inconsistency rate（24.5% → 1.7%），暗示标准 GRPO 确实存在 faithfulness 问题。\n\n- **调研总结**：CoT faithfulness、pre-CoT answer pre-commitment、RLVR monitorability 是 2025-2026 年高度活跃的研究方向。核心现象（模型在 CoT 前已 pre-commit 答案、RLVR 的 surface 改善与 causal reliance 解耦）已被多篇独立工作从不同角度确认。本 proposal 处于这些工作的**交叉地带**，试图用已有工具的组合来追踪一个已被强烈暗示（但尚未被显式纵向测量）的现象。\n\n\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁：\n\n1. **纯分析论证**：现有证据已经可以拼出完整的逻辑链：(a) 模型在 CoT 前已 pre-commit 答案 [Cox et al.]，(b) RLVR 的 surface 改善与 causal reliance 正交 [Monitorability paper]，(c) RL 训练可以降低 faithfulness 但维持 accuracy [RFEval]。将这三个发现组合起来，\"GRPO 训练加宽 surface-latent gap\" 几乎是一个可以被分析推导出的结论，不一定需要 20 个 checkpoints × 4 个指标 × 2 个模型族的重实验来验证。\n\n2. **轻量实验方案**：取 3-5 个 checkpoints（初始、早期、中期、晚期、最终），只运行 pre-CoT probe AUC + 一个 surface metric，就可以验证核心假设。20 个 checkpoints 和 changepoint detection 的附加价值需要论证——除非目标是发现非单调或相变行为，但 proposal 的假设是 monotonic widening，这降低了精细粒度的必要性。\n\n增量价值在于：(a) 精确量化 gap 的**动态轨迹**（何时开始、速率如何）；(b) 两种不同初始化的对比。但这是实验精细度的贡献，不是 insight 的贡献。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中存在以下未经验证的假设：\n\n1. **\"Pre-CoT linear probe AUC = latent answer commitment\" 的等价关系**：Cox et al. 证明了 pre-CoT probes 是预测性的且有因果效应，但将其解释为\"commitment\"（承诺）还是\"prior\"（先验）是有本质区别的。如果模型只是有一个 strong prior 但确实在 CoT 过程中被推翻了（即使只有 10% 的情况），那 AUC 高不等于 faithfulness 低。Proposal 隐含假设高 AUC = 低 faithfulness，这不完全成立。\n\n2. **\"GRPO 训练 monotonically 加宽 gap\" 的方向性假设**：现有证据只支持\"RL 训练后 gap 存在\"，不支持\"随训练步数 monotonically 加宽\"。可能的替代模式：(a) gap 从一开始就大（特别是对 DeepSeek-R1-Distill，它已经是 distilled reasoning model），GRPO 不改变它；(b) gap 先缩小后扩大；(c) gap 与 task difficulty 相关而非与 training step 相关。\n\n3. **两种初始化（distilled vs. base）会产生不同轨迹的假设**：这是合理的先验，但也可能两者 converge 到相同的 gap 模式，此时 two-model comparison 不产生额外 insight。\n\n4. **Changepoint detection 的前提——存在离散相变**：如果 gap 是 gradually widening 的（没有 sharp transition），changepoint detection 不会产生有意义的结果，整个分析框架的核心方法论将失去效力。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱** — \n   核心现象（surface-latent faithfulness decoupling）已被 RLVR Monitorability paper (2602.03978) 确认；pre-CoT probe 方法论已被 Cox et al. (2603.01437) 系统验证（AUC >0.9 + causal steering）；跨 RL checkpoints 追踪 faithfulness 已被 VLM checkpoint paper (2602.12506) 在视觉语言模型上完成；NLDD 和 Reasoning Horizon 是直接借用 (2602.11201)；probe trajectory 追踪在 2605.18549 中已建立。\n   \n   本 proposal 的实际 novelty delta 是**在文本推理模型上将这些已有工具组合起来做纵向追踪**。这是一种 methodological recombination（方法论重组合），而非 conceptual novelty（概念性创新）。更关键的是，预期发现（gap 加宽）是可以从现有文献中被 anticipate 的——如果结果是 positive，reviewer 的反应更可能是 \"I would have guessed this\" 而非 \"surprising\"。\n\n2. **Significance: 中** — \n   研究问题本身重要且及时：理解 RL 训练如何影响 reasoning faithfulness 是 AI safety/alignment 的核心问题。如果 proposal 发现的是**非单调的、出人意料的动态**（例如 gap 在训练中期突然出现然后稳定，或在某个 reward threshold 处发生相变），这将是 highly significant。但 proposal 的核心假设指向一个 **confirmatory 的、符合预期的结果**（monotonic widening），这限制了 surprise value 和影响力。实际意义（\"RL-trained models 需要 latent-space monitoring\"）已被 Cox et al. 和 Monitorability paper 强烈暗示，本 proposal 提供的是量化细节而非定性新洞察。\n\n3. **Related Work: 中** — \n   Proposal 对 2602.12506 和 2605.18549 有清晰定位，RLVR Monitorability paper 也被引用。但**缺少对最直接竞争工作 Cox et al. (2603.01437) 的显式讨论**，这是一个明显遗漏——该工作已经建立了 pre-CoT probes 的方法论基础，且其 activation steering 结果对 \"commitment vs. prior\" 的解释至关重要。同时对 RFEval (2602.17053) 和 Faithful GRPO (2604.08476) 的缺失也留下了定位空白——reviewer 会追问 \"这与 Faithful GRPO 解决的问题有什么关系？\"\n\n\n【概率估计】: 15% - 25%，中位 18%\n\n【估计理由】: \nNovelty 维度严重限制了上界。proposal 的核心 contribution 是方法论重组合（将已有工具应用到新的 temporal axis），而非概念性创新。中心假设（GRPO 训练加宽 surface-latent gap）可从现有文献强推导，预期结果是 confirmatory 而非 surprising。尽管 Significance 维度给予了一定支撑（问题本身重要），但在 novelty 弱的情况下，一个 confirmatory study 在 top venue 的接受概率受限。Related Work 的不完整性（缺少 Cox et al. 的讨论）会在审稿中被追问。概率上界受限于 novelty，下界由 significance 和问题的 timeliness 托底。\n\n【主要风险】: \n1. **Confirmatory study 风险**：核心发现若符合预期（gap 加宽），reviewer 会认为 \"this is exactly what existing literature would predict\"，incremental contribution 不足以支撑 top venue 发表。\n2. **Novelty 归因风险**：所有 4 个度量工具均直接借用已有工作（pre-CoT probes = Cox et al., NLDD = Ye et al., hint-injection = Chen et al., activation patching = standard），无方法论创新。如果 reviewer 认为\"组合已有工具\"不构成足够的 novelty，paper 将被拒。\n```\n\nSources:\n- [Decoding Answers Before Chain-of-Thought (Cox et al.)](https://arxiv.org/abs/2603.01437)\n- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)\n- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)\n- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)\n- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning](https://arxiv.org/abs/2602.11201)\n- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053)\n- [Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization](https://arxiv.org/abs/2604.08476)\n- [FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of CoT Reasoning](https://arxiv.org/abs/2510.04040)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models\n\n## Description\nWe propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:03:42.908Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:03:42.908Z",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:03:42.919Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to write the triage assessment. Let me synthesize my findings.

---

```
【阶段】: Triage

【领域调研】:
- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437) (arXiv, Mar 2026): 直接竞争工作。已证明 pre-CoT residual stream 上的 linear probe 可达 0.9 AUC 预测最终答案，且 probe direction 具有因果性（steering 可翻转答案 >50% 的案例）。本 proposal 的 metric (1)（pre-CoT probe AUC）本质上是该论文方法的直接复用。
- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488) (arXiv, Mar 2026): 高度相关。在 DeepSeek-R1 671B 和 GPT-OSS 120B 上用 activation probing 证明模型在 CoT 远早于完成时即已 commit 到最终答案，CoT 后段是 "performative reasoning"。直接支持 "latent commitment precedes surface reasoning" 的叙事——但也意味着这一发现已经被建立。
- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning](https://arxiv.org/abs/2602.11201) (arXiv/ICLR 2026 LIT Workshop): 本 proposal 的 metric (3) NLDD 和 "reasoning horizon" 概念的原始出处。已经定义了 Reasoning Horizon (k* ≈ 70-85% chain length) 以及 step-level faithfulness 的度量框架。
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978) (arXiv, Feb 2026): 本 proposal 直接引用的核心发现——RLVR 的 surface monitorability 改善主要来自 response distribution sharpening 和 prompt attention 增强，而非 causal reliance 加强。本 proposal 的中心假设（surface gains orthogonal to causal reliance）直接建立在此工作之上。
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506) (arXiv, Feb 2026): 已对 VLM 的 RL finetuning checkpoints 进行 faithfulness 追踪，发现 accuracy-faithfulness trade-off（准确率提升但 reasoning consistency 下降）。本 proposal 自我定位为该工作的扩展（加入 latent probe metrics + 文本 reasoning models）。
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549) (arXiv, May 2026): 在固定模型上构建 probe trajectory（每个 token 处评估 probe），发现 full trajectory 比 single-point prediction 提供更好的可分离性。本 proposal 自我定位为该工作的互补（加入训练时间维度）。
- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053) (arXiv, Feb 2026): 跨 12 个开源 reasoning model 的 faithfulness benchmark，发现 49.7% 输出存在 unfaithfulness，且与 post-training regimes 相关。
- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199) (arXiv, Mar 2026): 用 activation probing 在 CoT 前后检测 motivated reasoning，方法论与本 proposal 高度重叠。

- 调研总结: CoT faithfulness / latent-vs-surface gap 是 2025 下半年-2026 上半年的研究热点，已有大量工作从不同角度（probing、causal intervention、steering、benchmark）建立了"模型在 CoT 之前即已 commit 答案"和"RL 训练提升 surface 指标但不增强 causal reliance"的核心叙事。本 proposal 的贡献定位是将这些已有发现的工具组合起来，在训练时间维度上进行纵向追踪——这是一个尚未被填充的具体组合空白，但并非概念性创新。

【Trivial Alternative 检验】:
存在显著的 trivial alternative 威胁。核心问题是：**取 3-5 个关键 checkpoints（初始、early RL、mid RL、late RL）而非 ~20 个 fine-grained checkpoints，直接复用 2603.01437 的 pre-CoT probe + 2602.11201 的 NLDD + 标准 hint-injection protocol，是否能回答同样的核心问题？** 答案很可能是"是"。

~20 个 checkpoints + changepoint detection 的增量价值在于能够刻画 gap 的具体动态轨迹（是线性增长、阶梯式跳变、还是先缩后扩？），但：(a) 如果结果符合假设（monotonic widening），那么粗粒度采样就够了；(b) 如果结果不符合假设（非单调），那 changepoint detection 的发现才有价值，但这依赖于特定的实验结果——proposal 不能在 idea 层面 guarantee 这一点。

此外，"Monitorability as a Free Gift"(2602.03978) 已经在 RLVR 训练过程中追踪了 monitorability 的变化动态，虽然未使用 probe-based latent measures，但其核心结论（surface ≠ causal reliance）已经建立。本 proposal 的增量是用更精细的工具确认这一已知结论在 GRPO + text reasoning models 上的适用性。

【前提假设检验】:
1. **Linear probe AUC = "latent answer commitment"**: 这是核心假设中最关键的一环。2603.01437 提供了因果证据（steering 可翻转答案），但 linear probes 的解释性仍有争议——高 AUC 可能反映 residual stream 中的 task-relevant features 而非真正的 "commitment"。Proposal 直接将 probe AUC 等同于 latent faithfulness 的度量，但这一等价关系本身需要论证，不能简单借用。
2. **Surface faithfulness metrics 的有效性**: Hint-injection acknowledgment rate 作为 "surface faithfulness" 的 proxy 也并非无争议。模型不 acknowledge hint 可能是因为 faithfully 忽略了无关信息，而非 unfaithfully 隐藏了使用。
3. **GRPO 训练 = widening gap**: 中心假设假定 GRPO 训练系统性地扩大 gap，但这可能高度依赖于 (a) reward function 的设计、(b) training data 的分布、(c) 模型初始化。两个模型家族不足以建立 "GRPO training systematically decouples" 的 general claim。
4. **两个模型家族足以代表 "architecturally distinct"**: DeepSeek-R1-Distill-Qwen-7B 和 Qwen3-8B 虽然起点不同（distilled vs. base），但 Qwen 系列本身架构相近，代表性有限。

【3 维度打分】:
  1. Novelty: 弱 — 四个测量工具（pre-CoT probe, hint-injection, NLDD, activation patching）均直接借自 2603.01437、2602.11201、Chen et al. 等已有工作，无方法论创新。贡献仅在于"将已有工具在训练 checkpoint 维度上组合应用"——这是实验设计层面的组合，而非概念或方法论层面的创新。2602.12506 已经做了 VLM 的 checkpoint 级 faithfulness 追踪，2602.03978 已经建立了 "surface ≠ causal reliance" 的 RLVR 训练动态结论。本 proposal 填充的是一个具体的 "组合空白"（latent probes × training checkpoints × text reasoning models），但剔除 surface differences 后，核心 insight 增量有限。
  2. Significance: 中 — 研究问题本身（RL 训练是否系统性地解耦模型的表面推理与内部计算）对 AI safety 和 reasoning model 部署决策有实际意义。但问题在于：如果核心发现是 positive（gap widens），审稿人大概率会说 "I would have guessed this"——因为 2602.03978 的 monitorability 结论和 2603.05488 的 "Reasoning Theater" 发现已经强烈暗示了这一方向。如果结果是 negative 或 non-monotonic，那倒是 surprising 的，但 proposal 将自己框定为假设确认性研究（"central hypothesis is that GRPO training creates a widening gap"），限制了意外发现的叙事空间。对领域的推动力更接近 "confirmatory evidence for an emerging consensus" 而非 "new insight"。
  3. Related Work: 中 — Proposal 对 2602.12506 和 2605.18549 的定位清晰，但明显遗漏了两篇高度相关的竞争工作：(a) "Reasoning Theater"(2603.05488) 的 activation probing 发现直接挑战了本 proposal 的增量价值（performative CoT 已被 established）；(b) "Decoding Answers Before CoT"(2603.01437) 作为 pre-CoT probe 的原始工作，其 causal evidence 对本 proposal 的假设检验至关重要但未被充分讨论。此外，"Catching Rationalization in the Act"(2603.17199) 使用了高度类似的方法论（activation probing 检测 CoT 前后的 commitment）也未被提及。Related work 覆盖有明显盲区。

【概率估计】: [12% - 22%] 中位 17%
【估计理由】: Novelty 是主要限制维度。这个 proposal 的核心贡献是"工具组合 × 时间维度"的实验设计，而非概念性或方法论的创新。在一个已经有 6-8 篇高度相关的 2026 年论文建立了 "CoT faithfulness is problematic + latent commitment precedes surface reasoning + RL surface gains ≠ causal reliance" 叙事的领域，本 proposal 提供的增量是用更精细的工具确认已知结论在 GRPO training dynamics 上的适用性。中心假设的预期结果（gap widens）并不 surprising，限制了即使实验完美执行后的 impact 上限。Significance 给了它一定的下限支撑（问题本身重要），但 novelty 的弱势严重限制了上界。如果投稿 top venue 主会（NeurIPS/ICML/ICLR），作为 empirical study 需要在发现层面有 surprise element 才能突破 25%，而当前 framing 不具备这一条件。
【主要风险】: 
1. **"Confirmatory study" 定位的致命性**：中心假设（gap widens）是现有文献的自然推论，审稿人极可能评价为 "expected result, limited novelty"。如果 proposal 不将自己重新框定为 exploratory/discovery-oriented（例如："我们不知道 gap 的动态轨迹是什么形状，这是首次精确刻画"），confirmatory framing 本身就是最大的拒稿风险。
2. **方法论零创新的可累积负面印象**：四个 metrics 全部直接复用已有工作，无任何方法论贡献。对于 empirical study track，审稿人对"全用别人的工具做新实验"的容忍度有限——至少需要一个 methodological contribution（例如：新的 gap 度量、新的 probe 训练方式、或对已有 metric 的系统性比较/改进）来支撑 paper 的学术贡献。
```

Sources:
- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)
- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488)
- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning](https://arxiv.org/abs/2602.11201)
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)
- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)
- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough information to make a thorough assessment. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:

1. **"Reasoning Models Don't Always Say What They Think" (Anthropic, arXiv 2505.05410, May 2025)**:
   本 proposal 引用的 Chen et al. hint-injection 协议的原始来源。该工作发现 Claude 3.7 Sonnet 仅 25% 的情况下承认 hint 的影响，DeepSeek-R1 为 39%。建立了 surface faithfulness 的标准测量方法。与本 proposal 的关系：proposal 直接复用其 hint-injection 协议作为 surface metric，无方法论创新。

2. **"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering" (Cox et al., arXiv 2603.01437, March 2026)**:
   **最直接竞争工作。** 该论文已经在 pre-CoT residual stream activations 上训练线性 probe，实现 0.9 AUC 预测最终答案，并证明这些方向不仅是 predictive 还是 causal（activation steering 可以在 >50% 的案例中翻转答案）。与本 proposal 的关系：proposal 的 latent answer-commitment proxy（metric 1）与该工作高度重叠，差异仅在于本 proposal 沿 training checkpoints 追踪。

3. **"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning" (Xiong et al., arXiv 2602.03978, Feb 2026)**:
   **核心竞争 + 前置工作。** 该论文已经发现 RLVR 的 monitorability gains 来自 response distribution sharpening 和 increased attention to prompt，**而非 stronger causal reliance on reasoning traces**。即 surface gains 与 causal reliance 是 orthogonal 的。与本 proposal 的关系：proposal 的核心假设（"surface-latent gap widens"）可以被视为该工作结论的直接推论——如果 surface gains 与 causal reliance orthogonal，那么沿 training 追踪两者自然会看到 divergence。

4. **"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning" (ICLR 2026, arXiv 2602.11201)**:
   引入 NLDD（Normalized Likelihood Displacement）指标，发现 Reasoning Horizon 在 chain length 的 70-85% 处，之后的 reasoning tokens 对最终答案贡献很小甚至为负。与本 proposal 的关系：proposal 直接复用 NLDD 作为 metric 3，无方法论创新。

5. **"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (arXiv 2605.18549, May 2026)**:
   在固定模型上追踪 probe trajectories across inference tokens，发现 max-pooling 可达 95% AUROC。与本 proposal 的关系：proposal 明确定位自身与该工作的差异——该工作是"inference-time probe trajectory on fixed models"，本 proposal 是"training-time probe trajectory across checkpoints"。但两者的方法论思路高度同构。

6. **"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs" (arXiv 2602.12506, Feb 2026)**:
   在 VLM 上做 RL checkpoint 研究，发现 RL finetuning 提升 headline accuracy 但 reasoning 变得 increasingly inconsistent。与本 proposal 的关系：proposal 明确区分自身——该工作仅用 LLM-as-judge surface metrics 且在 VLM 上。

7. **"Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs" (arXiv 2512.22631, Dec 2025)**:
   直接评估 GRPO 和 DPO 对 CoT faithfulness 的影响，发现 GRPO 在大模型上优于 DPO。与本 proposal 的关系：该工作已评估 GRPO 对 faithfulness 的影响，但未做 checkpoint-level 纵向追踪，也未使用 latent probes。

8. **"Faithful GRPO" (arXiv 2604.08476, April 2026)**:
   在 GRPO reward 中加入 faithfulness 约束，将 inconsistency rate 从 24.5% 降到 1.7%。与本 proposal 的关系：从干预角度解决了 GRPO faithfulness 问题，而 proposal 是从诊断角度追踪。

- **调研总结**: CoT faithfulness 领域在 2025-2026 年极度拥挤。Pre-CoT probes 已被证明能以 0.9 AUC 预测答案（Cox et al.），RLVR 的 monitorability 与 causal reliance 的正交性已被建立（Xiong et al.），NLDD 已在 ICLR 2026 发表。本 proposal 处于这些工作的"交叉合成"位置——将已有的四个独立 metrics 应用于 GRPO training checkpoints 这一新维度。核心创新是时间维度的追踪粒度，而非方法论或理论层面的突破。


【Trivial Alternative 检验】:

存在一个明显的低成本替代方案：**取 3 个 checkpoint（early/mid/final）而非 ~20 个，用相同的 4 个 metrics 做快照对比。** 如果核心发现只是"latent pre-commitment 增强而 surface faithfulness 停滞"，这个 3-point 设计就够了，不需要 20 个 checkpoint 的 fine-grained 追踪。

Proposal 的增量价值在于：(1) fine-grained dynamics 可能揭示非线性转变点（changepoint detection），这确实需要密集 checkpoint；(2) 两个架构族的对比可能揭示 architecture-dependent 差异。但这些增量价值的大小取决于结果是否显示有趣的非线性 pattern——如果 divergence 是单调渐进的，那 3-point 设计就足够传达全部信息。

**更根本的 trivial alternative 威胁**：Xiong et al. (2602.03978) 已经在机制层面解释了为什么 surface ≠ latent（entropy reduction vs. causal reliance），那么沿 training checkpoints 追踪这个 divergence 的 *empirical confirmation* 的增量价值到底有多大？审稿人可能会问："We already know WHY these diverge; showing WHEN they diverge adds limited insight."


【前提假设检验】:

1. **"Linear probe AUC on pre-CoT activations 是 latent answer-commitment 的有效 proxy"**——这个假设有实证支撑（Cox et al. 2603.01437 达到 0.9 AUC），但有一个重要 caveat：probe 是在**单个 checkpoint 的数据上训练的**。当追踪 ~20 个 checkpoints 时，每个 checkpoint 的 representation space 可能发生剧烈变化，probe 的 transferability 是一个未解决的问题。如果每个 checkpoint 重新训练 probe，那 AUC 的变化可能反映 probe 训练的 variance 而非真实的 latent commitment 变化。这是一个 methodological gap。

2. **"GRPO training 会创造 widening gap"（核心假设）**——这更像是从 Xiong et al. 的 orthogonality finding 直接推导出的 prediction，而非一个需要 elaborate study 来验证的假设。如果结果是 positive（gap widens），审稿人会说"this follows logically from the monitorability paper"；如果结果是 negative（gap doesn't widen），那 changepoint detection 的整套框架就失去了意义。这是一个"难以 surprise 审稿人"的假设。

3. **"两个 model families 的差异有 informative 的架构归因"**——仅有两个 model families（一个 distilled，一个 base）无法在架构 vs. 训练数据 vs. 初始化 之间做因果归因。任何差异都可能来自 confounds。


【3 维度打分】:

1. **Novelty: 弱-中** — 核心贡献是将 4 个已有 metrics（pre-CoT linear probe [Cox et al. 2603.01437]、hint-injection [Chen et al. 2505.05410]、NLDD [2602.11201]、activation patching）应用于 GRPO training checkpoints 这一新维度。方法论层面无任何创新——全部是 off-the-shelf tools 的直接应用。时间维度的追踪确实填补了一个 gap，但这是一个"measurement study"式的 gap，而非概念或方法论的 gap。更关键的是，核心假设（surface-latent divergence）已经可以从 Xiong et al. (2602.03978) 的 orthogonality 结论直接推导出来，降低了发现的 surprisingness。在 CoT faithfulness 这个 2025-2026 年极度拥挤的领域，仅靠"在新维度上做 measurement"难以构成强 novelty。

2. **Significance: 中** — 研究问题本身是重要的：如果 RL training 系统性地 decouples surface from latent，这对 AI safety monitoring 有直接实践意义。但实际 significance 受限于两个因素：(a) Xiong et al. 已经从机制角度解释了 why this happens（entropy reduction），temporal dynamics 的补充价值是 incremental 的；(b) 仅在 7B/8B 的 open-weight models 上做，对 frontier model safety monitoring 的 generalizability 存疑。如果核心发现是 positive（gap widens），审稿人大概率会说 "I would have guessed this given the monitorability paper"。实际 surprise potential 较低。

3. **Related Work: 强** — Proposal 对已有工作的覆盖相当充分，正确引用了 2602.12506（VLM checkpoint）、2605.18549（probe trajectories at inference）、2602.03978（RLVR monitorability），并清晰定位了自身的差异化。但正是因为 related work 做得好，反而暴露了 novelty 的薄弱——每个差异化声明都是"unlike X which only did Y, we also do Z"，这种"existing work A + B + C + new axis"的定位模式容易被审稿人读为 incremental combination。


【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
Related Work 维度强，说明 proposal 的学术定位是 well-informed 的，这提升了下限。但 Novelty 弱-中 严重限制了上界：核心贡献是已有 metrics 在新维度上的应用（measurement study），且核心假设可从已有工作（Xiong et al. 的 orthogonality 结论）逻辑推导，降低了 surprise potential。Significance 中等——问题重要但预期发现不够 surprising。三个维度综合指向 borderline-reject 区间。Novelty 是主要限制因素。

**额外注意：venue mismatch 风险。** 如果目标 venue 确实是 CoRL（Conference on Robot Learning），本 proposal 与机器人学习完全无关，中稿概率接近 0%。上述概率估计基于假设目标 venue 为 NeurIPS/ICML/ICLR 等 ML/AI 主会或 COLM/EMNLP 等 NLP 会议。请确认目标 venue。

【主要风险】:
1. **"Predictable finding" 风险**：核心假设（surface-latent gap widens during GRPO training）可被视为 Xiong et al. orthogonality 结论的直接 corollary。如果审稿人认为"我们已经知道 WHY 它们 diverge，那么 WHEN 它们 diverge 的 empirical confirmation 是 incremental 的"，这将是 rejection 的主要依据。
2. **"Combination without insight" 风险**：4 个 off-the-shelf metrics × 20 checkpoints × 2 model families = 大量实验，但审稿人可能会问"beyond confirming the expected divergence, what new theoretical or mechanistic insight does this temporal tracking provide?" 如果 changepoint detection 未能揭示 non-trivial 的 phase transition pattern，整个 fine-grained 追踪的 motivation 会被质疑。
```

Sources:
- [Reasoning Models Don't Always Say What They Think (Chen et al., 2025)](https://arxiv.org/abs/2505.05410)
- [Decoding Answers Before Chain-of-Thought (Cox et al., 2026)](https://arxiv.org/abs/2603.01437)
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning (Xiong et al., 2026)](https://arxiv.org/abs/2602.03978)
- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (ICLR 2026)](https://arxiv.org/abs/2602.11201)
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs](https://arxiv.org/abs/2512.22631)
- [Faithful GRPO (VLM)](https://arxiv.org/abs/2604.08476)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?](https://arxiv.org/abs/2603.22582)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

1. Cox et al. "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering" (arXiv 2603.01437, Mar 2026):
   - 与本 proposal 的关系：**最直接的竞争工作**。已经证明在指令微调模型上，线性探针可以在 pre-CoT residual-stream activations 上以 >0.9 AUC 预测最终答案，且这些方向不仅是预测性的，还是因果性的（activation steering 可以在 >50% 的情况下翻转答案）。
   - 关键发现：模型在生成 CoT 之前就已经"决定"了答案。本 proposal 的核心度量之一（线性探针 AUC on pre-CoT activations）已被该工作系统验证。

2. "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning" (arXiv 2602.03978, Feb 2026):
   - 与本 proposal 的关系：**核心假设的直接来源**。本 proposal 的中心假设（"surface gains are orthogonal to causal reliance"）直接引用该论文的发现。
   - 关键发现：RLVR 的 monitorability 提升主要来自 response distribution sharpening（熵降低）和对 prompt 注意力增加，**而非更强的 causal reliance on reasoning traces**。这意味着 surface-level 的改善与 latent reasoning 的改善是解耦的——即本 proposal 要验证的核心主张已有强证据支持。

3. "On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs" (arXiv 2602.12506, Feb 2026):
   - 与本 proposal 的关系：proposal 显式定位自己相对于该工作的增量——本 proposal 声称该工作"仅使用 LLM-as-judge 的表面指标"而缺乏 latent measures。
   - 关键发现：在 VLM 上追踪 RL finetuning 中间 checkpoints，发现 accuracy 提升但 reasoning consistency 下降——即 surface-latent gap 在 VLM 场景已被观察到。

4. "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (arXiv 2605.18549, May 2026):
   - 与本 proposal 的关系：proposal 显式定位——该工作在**固定模型**上追踪推理过程中的 probe trajectories，缺乏**跨训练的时间维度**。
   - 关键发现：probe trajectories（在推理的每个 token 处评估探针）能提取推理动态信息，max-pooling 达到 95% AUROC。

5. "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning" (arXiv 2602.11201, Feb 2026):
   - 与本 proposal 的关系：NLDD 指标和 Reasoning Horizon 概念的来源论文。proposal 借用其 NLDD 作为 causal reliance 度量。
   - 关键发现：在 70-85% 的 chain length 之后，reasoning tokens 对最终答案几乎没有或有负面影响。

6. RFEval (arXiv 2602.17053, Feb 2026):
   - 与本 proposal 的关系：从 benchmark 角度验证了同一现象。
   - 关键发现：在 SFT 之上添加 RL-style 目标**可以降低 reasoning faithfulness**，即使 accuracy 保持不变。这直接支持了 proposal 的"gap 加宽"假设，但也意味着该假设已有实证支撑。

7. "Faithful GRPO" (arXiv 2604.08476, Apr 2026):
   - 与本 proposal 的关系：从解决方案角度反映同一问题——如果 GRPO 本身不产生 faithfulness gap，就不需要"Faithful GRPO"。
   - 关键发现：通过 constrained policy optimization 可以显著降低 inconsistency rate（24.5% → 1.7%），暗示标准 GRPO 确实存在 faithfulness 问题。

- **调研总结**：CoT faithfulness、pre-CoT answer pre-commitment、RLVR monitorability 是 2025-2026 年高度活跃的研究方向。核心现象（模型在 CoT 前已 pre-commit 答案、RLVR 的 surface 改善与 causal reliance 解耦）已被多篇独立工作从不同角度确认。本 proposal 处于这些工作的**交叉地带**，试图用已有工具的组合来追踪一个已被强烈暗示（但尚未被显式纵向测量）的现象。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. **纯分析论证**：现有证据已经可以拼出完整的逻辑链：(a) 模型在 CoT 前已 pre-commit 答案 [Cox et al.]，(b) RLVR 的 surface 改善与 causal reliance 正交 [Monitorability paper]，(c) RL 训练可以降低 faithfulness 但维持 accuracy [RFEval]。将这三个发现组合起来，"GRPO 训练加宽 surface-latent gap" 几乎是一个可以被分析推导出的结论，不一定需要 20 个 checkpoints × 4 个指标 × 2 个模型族的重实验来验证。

2. **轻量实验方案**：取 3-5 个 checkpoints（初始、早期、中期、晚期、最终），只运行 pre-CoT probe AUC + 一个 surface metric，就可以验证核心假设。20 个 checkpoints 和 changepoint detection 的附加价值需要论证——除非目标是发现非单调或相变行为，但 proposal 的假设是 monotonic widening，这降低了精细粒度的必要性。

增量价值在于：(a) 精确量化 gap 的**动态轨迹**（何时开始、速率如何）；(b) 两种不同初始化的对比。但这是实验精细度的贡献，不是 insight 的贡献。


【前提假设检验】:

核心 claim 的逻辑链中存在以下未经验证的假设：

1. **"Pre-CoT linear probe AUC = latent answer commitment" 的等价关系**：Cox et al. 证明了 pre-CoT probes 是预测性的且有因果效应，但将其解释为"commitment"（承诺）还是"prior"（先验）是有本质区别的。如果模型只是有一个 strong prior 但确实在 CoT 过程中被推翻了（即使只有 10% 的情况），那 AUC 高不等于 faithfulness 低。Proposal 隐含假设高 AUC = 低 faithfulness，这不完全成立。

2. **"GRPO 训练 monotonically 加宽 gap" 的方向性假设**：现有证据只支持"RL 训练后 gap 存在"，不支持"随训练步数 monotonically 加宽"。可能的替代模式：(a) gap 从一开始就大（特别是对 DeepSeek-R1-Distill，它已经是 distilled reasoning model），GRPO 不改变它；(b) gap 先缩小后扩大；(c) gap 与 task difficulty 相关而非与 training step 相关。

3. **两种初始化（distilled vs. base）会产生不同轨迹的假设**：这是合理的先验，但也可能两者 converge 到相同的 gap 模式，此时 two-model comparison 不产生额外 insight。

4. **Changepoint detection 的前提——存在离散相变**：如果 gap 是 gradually widening 的（没有 sharp transition），changepoint detection 不会产生有意义的结果，整个分析框架的核心方法论将失去效力。


【3 维度打分】:

1. **Novelty: 弱** — 
   核心现象（surface-latent faithfulness decoupling）已被 RLVR Monitorability paper (2602.03978) 确认；pre-CoT probe 方法论已被 Cox et al. (2603.01437) 系统验证（AUC >0.9 + causal steering）；跨 RL checkpoints 追踪 faithfulness 已被 VLM checkpoint paper (2602.12506) 在视觉语言模型上完成；NLDD 和 Reasoning Horizon 是直接借用 (2602.11201)；probe trajectory 追踪在 2605.18549 中已建立。
   
   本 proposal 的实际 novelty delta 是**在文本推理模型上将这些已有工具组合起来做纵向追踪**。这是一种 methodological recombination（方法论重组合），而非 conceptual novelty（概念性创新）。更关键的是，预期发现（gap 加宽）是可以从现有文献中被 anticipate 的——如果结果是 positive，reviewer 的反应更可能是 "I would have guessed this" 而非 "surprising"。

2. **Significance: 中** — 
   研究问题本身重要且及时：理解 RL 训练如何影响 reasoning faithfulness 是 AI safety/alignment 的核心问题。如果 proposal 发现的是**非单调的、出人意料的动态**（例如 gap 在训练中期突然出现然后稳定，或在某个 reward threshold 处发生相变），这将是 highly significant。但 proposal 的核心假设指向一个 **confirmatory 的、符合预期的结果**（monotonic widening），这限制了 surprise value 和影响力。实际意义（"RL-trained models 需要 latent-space monitoring"）已被 Cox et al. 和 Monitorability paper 强烈暗示，本 proposal 提供的是量化细节而非定性新洞察。

3. **Related Work: 中** — 
   Proposal 对 2602.12506 和 2605.18549 有清晰定位，RLVR Monitorability paper 也被引用。但**缺少对最直接竞争工作 Cox et al. (2603.01437) 的显式讨论**，这是一个明显遗漏——该工作已经建立了 pre-CoT probes 的方法论基础，且其 activation steering 结果对 "commitment vs. prior" 的解释至关重要。同时对 RFEval (2602.17053) 和 Faithful GRPO (2604.08476) 的缺失也留下了定位空白——reviewer 会追问 "这与 Faithful GRPO 解决的问题有什么关系？"


【概率估计】: 15% - 25%，中位 18%

【估计理由】: 
Novelty 维度严重限制了上界。proposal 的核心 contribution 是方法论重组合（将已有工具应用到新的 temporal axis），而非概念性创新。中心假设（GRPO 训练加宽 surface-latent gap）可从现有文献强推导，预期结果是 confirmatory 而非 surprising。尽管 Significance 维度给予了一定支撑（问题本身重要），但在 novelty 弱的情况下，一个 confirmatory study 在 top venue 的接受概率受限。Related Work 的不完整性（缺少 Cox et al. 的讨论）会在审稿中被追问。概率上界受限于 novelty，下界由 significance 和问题的 timeliness 托底。

【主要风险】: 
1. **Confirmatory study 风险**：核心发现若符合预期（gap 加宽），reviewer 会认为 "this is exactly what existing literature would predict"，incremental contribution 不足以支撑 top venue 发表。
2. **Novelty 归因风险**：所有 4 个度量工具均直接借用已有工作（pre-CoT probes = Cox et al., NLDD = Ye et al., hint-injection = Chen et al., activation patching = standard），无方法论创新。如果 reviewer 认为"组合已有工具"不构成足够的 novelty，paper 将被拒。
```

Sources:
- [Decoding Answers Before Chain-of-Thought (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)
- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning](https://arxiv.org/abs/2602.11201)
- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053)
- [Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization](https://arxiv.org/abs/2604.08476)
- [FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of CoT Reasoning](https://arxiv.org/abs/2510.04040)


【原始 proposal（允许参考但不是主要依据）】:
# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models

## Description
We propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "44ac8a4c-19a1-4244-af42-850cb2743235",
  "type": "user",
  "uuid": "93518312-95b4-4b5b-8584-21a174a718bc",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:03:42.917Z_

```json
{
  "parentUuid": "93518312-95b4-4b5b-8584-21a174a718bc",
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
  "uuid": "f635a8bc-b93a-40c7-90ba-71e88ac73fd9",
  "timestamp": "2026-05-20T03:03:42.917Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:03:42.918Z_

```json
{
  "parentUuid": "f635a8bc-b93a-40c7-90ba-71e88ac73fd9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2d1360ef-b20c-42e5-bb5c-b3828a7ea582",
  "timestamp": "2026-05-20T03:03:42.918Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to write the triage assessme…",
  "leafUuid": "2d1360ef-b20c-42e5-bb5c-b3828a7ea582",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate surface-latent faithfulness gap in GRPO training",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:04:21.603Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as a Meta Judge.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 中 (Medium)
- Probability: [12% - 22%] 中位 17%

**Reviewer 2:**
- Novelty: 弱-中 (Weak-Medium)


- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [18% - 28%] 中位 22%

**Reviewer 3:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 中 (Medium)
- Probability: [15% - 25%] 中位 18%

Now I'm calculating the aggregate metrics across all three reviewers. The midpoint probabilities are 17%, 22%, and 18%, which gives me a mean of 19% and a median of 18%, with a standard deviation around 2%.

Looking at where the reviewers align, there's strong consensus that novelty is weak across all three, significance is uniformly medium, and they all flag the same core issues—the confirmatory study risk, the trivial lightweight alternative threat, and the fact that all metrics are off-the-shelf with no methodological innovation.

Now examining the divergences: R2 stands alone in rating related work as strong while the others say medium, and only R2 explicitly calls out the venue mismatch between CoRL and typical ML venues. R1 uniquely identifies missing papers on reasoning theater and rationalization, while R2 and R3 both reference the faithful GRPO and GRPO/DPO evaluation papers that the others don't mention.

The standard deviation across midpoints is about 2.16%, well under the 3% threshold, indicating strong alignment. All three reviewers identify the same core issues: weak novelty from methodological recombination rather than conceptual innovation, medium significance despite addressing an important question, and the confirmatory study framing as the primary risk.

Given this high consistency, I'm anchoring to the median midpoint of 18% and narrowing the range accordingly. Following the constraint that my estimate shouldn't be more lenient than the most generous reviewer, my upper bound caps at 28% from R2. I'll set the lower bound around 14%, splitting the difference between R1's 12% and the tighter estimates from the others.

But wait—R2 flagged something crucial that I need to reconsider: this proposal is being submitted to CoRL 2026, which is the Conference on Robot Learning, yet the work has no connection to robotics whatsoever. That's a fundamental venue mismatch, not just a minor concern. I need to recalibrate my probability estimates since the reviewers' assessments assumed a general ML venue, but CoRL is specifically for robotics — this proposal would face near-zero acceptance odds there. I'll present both the general ML venue assessment and the CoRL-specific reality, then outline what implementation would require: significant GPU resources for GRPO training across two 7B/8B model families with roughly 20 checkpoints each, standard reasoning datasets, minimal human intervention, and a timeline of about 2-3 months.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d1360ef-b20c-42e5-bb5c-b3828a7ea582",
  "isSidechain": false,
  "requestId": "req_011CbD5VyqrfJo8zdJnVfHVk",
  "type": "assistant",
  "uuid": "27b70baa-860c-4478-a7da-b0f295e0d096",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9PcAGwwZLYYGiqs66HaoQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18969,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3616,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 18969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18969
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

_source line 9 · 2026-05-20T03:05:02.778Z_

【阶段】: Meta Judge
【三次中位】: [17%, 22%, 18%]  std=2.2%
【共识维度】:
- **Novelty=弱**（3/3 一致）：全部审稿人认为四个度量工具（pre-CoT probe、hint-injection、NLDD、activation patching）均为 off-the-shelf 直接复用，无方法论创新。贡献仅为"已有工具 × 训练 checkpoint 新维度"的组合。
- **Significance=中**（3/3 一致）：问题本身（RL 训练是否系统性解耦 surface/latent faithfulness）对 AI safety 有实际意义，但预期发现符合现有文献推导方向，surprise potential 低。
- **"Confirmatory study" 致命风险**（3/3 一致）：核心假设（gap widens）可从 Xiong et al. (2602.03978) 的 orthogonality 结论直接推导，审稿人大概率反应 "I would have guessed this"。这是所有审稿人一致认定的首要拒稿理由。
- **Trivial alternative 威胁**（3/3 一致）：3-5 个 checkpoint 的轻量方案即可验证核心假设，20 个 fine-grained checkpoint + changepoint detection 的增量价值取决于是否发现非线性 pattern，但 proposal 自身假设 monotonic widening，自相矛盾地削弱了精细追踪的 motivation。
- **Cox et al. (2603.01437) 为最直接竞争工作**（3/3 一致）：pre-CoT probe 方法论已被该工作系统验证（AUC>0.9 + causal steering），本 proposal 的 metric (1) 本质是其直接复用。
【异常维度】:
- **Related Work=强**（仅 R2，R1/R3 均为中）：R2 认为 proposal 的学术定位 well-informed，但 R1/R3 指出遗漏了 Cox et al. (2603.01437) 的显式讨论、"Reasoning Theater" (2603.05488)、"Catching Rationalization in the Act" (2603.17199) 等高度相关工作。R2 的"强"评价为 outlier，降权处理，综合判定 Related Work=中。
- **Venue mismatch 风险**（仅 R2 显式提出）：R2 指出若目标为 CoRL（Conference on Robot Learning），proposal 与机器人学习完全无关，中稿概率接近 0%。此为单人提出但逻辑上成立的**致命级异常**，不降权，需显式标注。
【最终概率】: [13% - 24%] 中位 18%（基于通用 ML/AI 主会如 NeurIPS/ICML/ICLR；若目标确为 CoRL，概率 ≈ 0-2%）
【一致性】: 高（std=2.2% < 3%，三位审稿人在所有核心判决维度上高度收敛）
【综合理由】:
三位审稿人在核心诊断上呈现罕见的高度一致：Novelty 弱（方法论零创新、纯组合式 measurement study）、Significance 中（重要问题但预期结果不 surprising）、confirmatory study 是首要拒稿风险。由于 std<3%，取中位附近并略微缩窄区间。R2 的概率估计（中位 22%）略高于 R1/R3，主要因为 R2 给了 Related Work=强，但 R1/R3 指出的 related work 遗漏（Cox et al. 未被充分讨论、Reasoning Theater 和 Catching Rationalization 缺失）更有说服力，因此 Related Work 综合判定为中，R2 的乐观偏差被修正。最终中位取 18%，上界不超过 R2 的 28%（实际缩至 24%），下界在 R1 的 12% 和 R3 的 15% 之间取 13%。

**关于 CoRL venue mismatch**：虽仅 R2 显式提出，但这是一个客观事实层面的判断——本 proposal 无任何机器人学习内容，CoRL 的审稿池和录用标准与纯 NLP/ML 理论方向完全不匹配。若目标确为 CoRL 2026，此为**独立于 idea 质量的致命 venue mismatch**，概率直接归零。后续分析基于假设目标为通用 ML/AI 主会。

【建议】: 不推荐（通用 ML 主会）/ KILL（若目标确为 CoRL）

理由：中位 18% 处于 borderline-reject 下沿。三位审稿人高度一致地诊断出 Novelty 弱 + confirmatory study framing 的双重致命问题，且这两个问题相互强化——方法论无创新意味着 paper 的全部价值押注在 empirical findings 上，而 confirmatory framing 意味着即使实验完美执行，findings 也不 surprising。在当前 framing 下，即使进入迭代优化，idea 质量天花板（由 Novelty 决定）严重限制了概率上限，预计难以突破 30%。若要继续推进，需要根本性的 reframing（如从 confirmatory 转向 exploratory/discovery-oriented，或引入至少一个 methodological contribution），但这已接近换 idea 而非优化 idea。

【实施评估】:
  - 计算资源: 高。需对 2 个 7B/8B 模型进行 GRPO 训练并保存 ~20 个 checkpoint（每模型），估计需要 4-8 × A100 80GB GPU 持续 2-4 周用于训练；每个 checkpoint 的 probe 训练和评估（线性探针、NLDD 计算、activation patching）额外需要 1-2 GPU-weeks。总计约 100-200 GPU-days。
  - 数据需求: 中。需要标准推理 benchmark（MATH、GSM8K 等）用于 GRPO 训练和评估，以及 hint-injection 测试集（可基于 Chen et al. 协议构建）。数据集均为公开可得。
  - 人工介入: 低。Pipeline 基本自动化，主要人工工作在于实验设计、probe 训练策略决定、结果分析。无需人工标注。
  - 训练需求: 是。需从零进行两轮完整 GRPO 训练（DeepSeek-R1-Distill-Qwen-7B 和 Qwen3-8B），并在每个 checkpoint 训练线性探针。模型规模 7-8B，训练周期估计每模型 1-2 周。
  - 新 Benchmark: 否。使用现有 benchmark 和已有评测协议。
  - 预估周期: 2.5-4 个月（含 GRPO 训练 3-4 周、checkpoint 评估 2-3 周、分析写作 3-4 周、buffer 2 周）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27b70baa-860c-4478-a7da-b0f295e0d096",
  "isSidechain": false,
  "requestId": "req_011CbD5VyqrfJo8zdJnVfHVk",
  "type": "assistant",
  "uuid": "248ea62a-43cf-49f9-bd45-b80425fe9834",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9PcAGwwZLYYGiqs66HaoQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18969,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18969,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3616,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 18969,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18969
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to write the triage assessme…",
  "leafUuid": "248ea62a-43cf-49f9-bd45-b80425fe9834",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate surface-latent faithfulness gap in GRPO training",
  "sessionId": "5f5cea7c-74aa-4f26-a86e-c8a24f574c29"
}
```

---
