# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/a6e9b467-2dce-4246-8775-da445c4ad66f.jsonl`
- **Structured JSON:** [`00432132c51578f6db97.json`](../../sessions/00/00432132c51578f6db97.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:29:38.773Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:29:38.773Z",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have enough information to make my assessment. Let me note a critical issue I've identified — this proposal targets **CoRL 2026** (Conference on Robot Learning), but the proposal is entirely about CoT faithfulness in language models with zero robotics content. Let me verify the target venues listed in the proposal itself.\n\nLooking at the proposal again, I see the **Target Venues** listed are actually **ICLR 2027** and **ICML 2027**, not CoRL. However, the user's task says to evaluate for \"CoRL 2026 主会\". This is a critical mismatch. Let me proceed with the evaluation, addressing this venue mismatch.\n\nNow let me compile my full triage evaluation:\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [Yuan et al., arXiv 2605.09502] (May 2026): \"Hidden Error Awareness: The Signal Is Diagnostic, Not Causal\" — 核心动机论文之一。确认存在，描述准确。证明 linear probe 可达 0.95 AUROC 检测错误，但四种 causal intervention 均失败。这是本 proposal 的核心前提。\n\n2. [Chrabąszcz et al., arXiv 2605.18549] (May 2026): \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" — 最直接的竞争工作。确认存在，描述准确。提出 probe trajectory + 60+ signal-processing features，max-pooling 达 91-97% AUROC。关键：该工作只有 probe 侧，没有 causal contribution 维度。Proposal 对差异化的描述基本准确。\n\n3. [Cox et al., arXiv 2603.01437] (Mar 2026): \"Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering\" — 确认存在。证明 instruction-tuned models 上 steering 有效（>50% flip），但 reasoning model 上失败。Proposal 引用准确。\n\n4. [Wang, arXiv 2604.15726] (Apr 2026): \"LLM Reasoning Is Latent, Not the Chain of Thought\" — 确认存在。提出 H1/H2/H0 三假说框架。Proposal 声称 ICG 可 operationalize 这个区分，引用准确。\n\n5. [Ballon et al., arXiv 2601.23163] (Jan 2026): \"Probing the Trajectories of Reasoning Traces in LLMs\" — 确认存在。truncation-reinjection protocol。Proposal 将其作为 C(t) estimator 的基础，引用准确。\n\n6. [Gjølbye et al., arXiv 2605.15454] (May 2026): \"Reasoning Models Don't Just Think Longer, They Move Differently\" — 确认存在。difficulty-geometry coupling，length correction 方法。Proposal 引用准确。\n\n7. CoRL 2026 Call for Papers: CoRL 是 Conference on Robot Learning，要求 submissions 聚焦 core robotics problem，鼓励 real-robot experiments 或 sim-to-real evidence。**本 proposal 与 robotics 完全无关。**\n\n- 调研总结: CoT faithfulness 是 2025-2026 年的高热领域，大量独立工作从 probing、causal intervention、temporal dynamics 等角度切入，产出密集。Proposal 引用的关键论文均真实存在且描述准确。Proposal 试图做的\"将 probe trajectory 与 causal contribution 联合追踪\"确实是现有工作的空白（Chrabąszcz 只有 probe 侧，Ballon 只有 behavioral 侧），但这个空白更像是自然的 engineering integration，而非概念上的突破。**最严重的问题是：proposal 的 target venue 与内容完全不匹配——CoRL 是 robotics 会议，而本 proposal 是纯 NLP/interpretability 工作。**\n\n\n【Trivial Alternative 检验】:\n\n存在显著的 trivial alternative 威胁：\n\n1. **直接拼接现有工具**: Chrabąszcz et al. 的 probe trajectory + Ballon et al. 的 truncation-reinjection protocol，不加任何新框架，直接在同一 model/dataset 上跑两个管线然后对比，就能产出类似的 \"information vs. contribution\" 对比。ICG 框架的增量价值主要在于 (a) null-probe calibration, (b) G*(t) 这个 formalization, (c) phenomenon taxonomy。其中 null-probe calibration 是 Hewitt & Liang 2019 的标准技术；G*(t) 的 formalization 虽然整洁，但本质上就是 \"probe accuracy 减去 causal contribution\" 的减法；phenomenon taxonomy 是否真能 work 取决于 Phase 0b 的实验结果。\n\n2. **Phenomenon classification 的可行性存疑**: Proposal 自己承认 phenomenon signature 是 \"predictions\"，依赖 Phase 0b pilot 验证。如果 d < 0.3，就 downscope 为 \"characterization paper\"。一个 characterization paper 的核心贡献就变成了 \"我们在同一个 model 上同时跑了 probe 和 truncation ablation，发现 gap 存在\"——这接近 trivial integration。\n\n增量价值在于：如果 phenomenon classification 确实 work（d > 0.5），且 difficulty conditioning 揭示了有实践意义的 decorative→load-bearing 转换点，那框架就有超越 trivial integration 的价值。但这是一个 conditional novelty——novelty 依赖于实验结果。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有多个未经验证的假设：\n\n1. **\"Probe accuracy 减去 causal contribution = faithfulness signal\" 的假设**: 这是整个框架的核心等式 G*(t) = P*(t) − C(t)。但 P*(t) 测量的是 \"hidden state 中是否编码了 correctness awareness\"，C(t) 测量的是 \"CoT prefix 对最终答案的因果贡献\"。这两个量的度量尺度不同（一个是 AUROC，一个是 accuracy change），直接相减的语义不清晰。Proposal 没有严格论证为什么这个差值是 faithfulness 的有效操作化定义，而不仅仅是两个不同测量的 arbitrary 组合。\n\n2. **\"不同 faithfulness phenomena 会产生可区分的 G*(t) trajectory shapes\" 的假设**: 这是 phenomenon classification 的基础。Proposal 的 signature predictions（如 pre-CoT encoding → 大常数 gap，genuine reasoning → 收敛到零）看起来合理，但它们是从不同 study、不同 model、不同 dataset 的结果拼接推导出来的。在同一 model 同一 dataset 上，这些 pattern 是否可分离是完全未知的。Proposal 诚实地承认了这一点并设计了 Phase 0b pilot，这是好的，但也意味着核心 novelty claim 在实验前是悬空的。\n\n3. **\"Null-probe calibration 能有效去除 correlative inflation\" 的假设**: Hewitt & Liang 的 selectivity 方法是对 MLP probe 设计的，对 linear probe 的适用性更直接，但 \"shuffled labels\" 的 null probe 是否能捕捉到 Chun et al. 发现的 non-uniform 几何 inflation 是另一个问题。Proposal 加入了 MCT 验证，但 MCT 本身在这个 context 中是否是有效的校准工具也需要实验验证。\n\n4. **\"三种 C(t) estimators 可以提供 convergent evidence\" 的假设**: prefix truncation、paraphrase perturbation、NLDD 测量的是不同的 causal 概念。prefix truncation 测的是 \"reasoning trace 到这个位置为止的整体贡献\"，NLDD 测的是 \"特定位置的局部影响\"，paraphrase perturbation 测的是 \"语义内容 vs. 表面形式\"。它们是否收敛以及不收敛时如何解释，proposal 没有清晰回答。\n\n\n【3 维度打分】:\n\n1. Novelty: 【中】— \n   Proposal 的核心创新是将 probe trajectory (à la Chrabąszcz et al. 2605.18549) 和 causal contribution trajectory (à la Ballon et al. 2601.23163) 联合追踪，形成 G*(t) gap metric。这个组合确实是文献空白——Chrabąszcz 只有 probe 侧，Ballon 只有 behavioral 侧，没有人同时做过两侧并 formalize gap。但这个 novelty 更接近 \"integration novelty\" 而非 \"conceptual novelty\"。G*(t) = P*(t) − C(t) 的 formalization 虽然整洁，但概念上就是 \"同时测量两个已知量然后做减法\"。Null-probe calibration 是 2019 年的标准技术。Phenomenon taxonomy 的 novelty 取决于实验结果（是否真的可分离）。\n   \n   相比之下，Yuan et al. (2605.09502) 的 novelty 在于发现一个 surprising empirical fact（四种 intervention 全部失败），Wang (2604.15726) 的 novelty 在于概念框架的重新构造。本 proposal 的 novelty 层次更接近 \"measurement framework\" 而非 \"discovery\" 或 \"reconceptualization\"。\n\n2. Significance: 【中偏强】— \n   CoT faithfulness 是当前 LLM safety 和 interpretability 的核心问题，research question 的重要性毋庸置疑。\"模型知道但不使用\" 这个现象的系统性表征确实有价值。如果 difficulty conditioning 能揭示 \"CoT 在什么时候从装饰性变为功能性\"，这对实践有指导意义。但 significance 受限于两点：(a) 这是一个 diagnostic/measurement 贡献，不提供 actionable improvement；(b) 结果的 generalizability 受限于所测试的 model 和 benchmark 的范围。\n\n   **然而，最致命的 significance 问题是 venue mismatch**: CoRL 是 Conference on Robot Learning，要求 submissions 聚焦 robotics 问题并展示 real-robot 或 sim-to-real evidence。本 proposal 是纯 NLP/interpretability 工作，与 robotics 零相关。即使 idea 质量再高，投 CoRL 的中稿概率接近零，除非做根本性的方向调整（如将 framework 应用于 robot reasoning/planning 中的 CoT faithfulness）。Proposal 自身的 target venues 也写的是 ICLR 2027 和 ICML 2027，不是 CoRL。\n\n3. Related Work: 【强】— \n   这是 proposal 最突出的优点。文献覆盖极其全面，引用了 40+ 篇高度相关的近期工作，且对每篇工作的描述经核实基本准确。与最直接竞争工作 (Chrabąszcz et al.) 的差异化定位清晰——明确指出自己多出的维度（causal contribution, gap metric, calibration, phenomenon taxonomy）。对 probe calibration 文献（Hewitt & Liang, Voita & Titov, Chun et al.）的引用表明作者对方法论风险有清醒认识。唯一的小缺陷是引用数量过多可能导致在正式论文中难以充分讨论每一篇。\n\n\n【概率估计】: [2% - 8%] 中位 3%\n\n【估计理由】: \n这个极低的概率估计主要由一个**致命的 venue mismatch** 驱动：CoRL 是 Conference on Robot Learning，而本 proposal 是纯 NLP/interpretability 研究，与 robotics 完全无关。CoRL 的 CFP 明确要求 \"submissions should focus on a core robotics problem\" 并 \"demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\"。无论 idea 质量如何，desk reject 的风险极高。\n\n如果忽略 venue mismatch，仅评估 idea 在 NLP/ML 顶会（如 ICLR 2027, 其自身 target venue）的潜力，我的估计会是 [25% - 38%] 中位 30%。理由：idea 方向正确，research question 重要，literature 覆盖出色，但 novelty 偏向 integration/measurement 而非 discovery，核心 claim（phenomenon classification via trajectory shapes）依赖实验结果验证，且存在 trivial alternative 威胁（直接拼接现有工具）。审稿人看到 G*(t) = P*(t) − C(t) 时，可能会说 \"this is a natural combination, I would have expected someone to do this\"——属于 \"I would have guessed this\" 区间，对应 25-35%。Phase 0b 的 honest scoping 和 extensive robustness plan 提高了下限但不提高上限。\n\n【主要风险】:\n1. **致命 venue mismatch**: CoRL 是 robotics 会议，本 proposal 与 robotics 零相关，大概率 desk reject。\n2. **Conditional novelty**: 框架的核心卖点（phenomenon classification via G*(t) trajectory shapes）的 novelty 取决于 Phase 0b 的实验结果。如果 phenomena 不可分离，剩余的 \"characterization paper\" 贡献度接近 trivial integration，novelty 降至 \"弱\"。\n```\n\n---\n\n**补充说明给后续流程**：\n\n本 proposal 存在一个需要立即确认的根本性问题——**投稿目标是 CoRL 2026（robotics 会议）还是 ICLR/ICML 2027（ML 顶会）？** Proposal 自身写的 target venues 是 ICLR 2027 和 ICML 2027，而任务要求评估 CoRL 2026 中稿概率。如果确实要投 CoRL，需要从根本上重新定位 proposal（例如将 CoT faithfulness framework 应用于 embodied reasoning / robot planning），否则中稿概率近乎为零。如果 target 实际是 ICLR/ICML，那 idea 质量属于中等偏上水平（~30%），值得进入后续迭代流程。\n\nSources:\n- [Yuan et al. - Hidden Error Awareness](https://arxiv.org/abs/2605.09502)\n- [Chrabąszcz et al. - Probe Trajectories](https://arxiv.org/abs/2605.18549)\n- [Cox et al. - Pre-CoT Probes](https://arxiv.org/abs/2603.01437)\n- [Wang - LLM Reasoning Is Latent](https://arxiv.org/abs/2604.15726)\n- [Ballon et al. - Reasoning Trace Trajectories](https://arxiv.org/abs/2601.23163)\n- [Gjølbye et al. - Reasoning Models Move Differently](https://arxiv.org/abs/2605.15454)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [FaithCoT-Bench (ICLR 2026)](https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf)\n- [Ye et al. - Faithfulness Decay / NLDD](https://arxiv.org/html/2602.11201v1)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命性前置问题：venue 完全不匹配】\n\n本 proposal 投稿目标为 **CoRL 2026（Conference on Robot Learning）**。\n然而，CoRL 的 Call for Papers 明确要求：\"Submissions should focus on a core robotics problem \nand demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to \nrobotics. Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 的内容是 **LLM chain-of-thought faithfulness 的可解释性度量框架**——\n纯粹的 NLP/ML interpretability 研究，没有任何机器人学习相关内容（无 embodiment、\n无 manipulation、无 navigation、无 sim-to-real、无 robot policy learning）。\n这篇论文会在 CoRL 被 **desk reject without review**。\n\nproposal 自身列出的 target venues 是 ICLR 2027 和 ICML 2027，\n这与用户指定的 CoRL 2026 完全矛盾。\n\n➡️ **对 CoRL 2026 的中稿概率：0-2%（会被 desk reject）。**\n\n以下评估将基于 idea 本身的质量，假设投稿到合理的 venue（如 ICLR/ICML/NeurIPS），\n供后续流程参考。\n\n\n【领域调研】:\n\n- [Yuan et al. \"Hidden Error Awareness\" arXiv 2605.09502] (2026): \n  最直接的前置工作。系统证明 4 种 causal intervention（activation steering, \n  probe-guided best-of-N, self-correction, activation patching）在 reasoning models \n  上全部失败，确立 \"diagnostic not causal\" 发现。本 proposal 的核心动机直接来源于此。\n  \n- [Cox et al. \"Pre-CoT Probes\" arXiv 2603.01437] (2026): \n  在 instruction-tuned models 上 probe steering 可实现 >50% flip rate，\n  但在 reasoning model (GPT-OSS-20B) 上 flip rate \"negligible against orthogonal \n  baseline\"。本 proposal 的另一核心动机来源。\n  \n- [Chrabąszcz et al. \"Probe Trajectories\" arXiv 2605.18549] (2026.05): \n  最接近的并发工作。已经做了 probe trajectory 的全时程追踪，提取 60+ \n  signal-processing features，在 4 个 reasoning models 上达到 91-97% AUROC。\n  与本 proposal 的 P*(t) 方向高度重叠，但缺少 causal contribution 维度。\n  \n- [Ballon et al. \"Truncation-Reinjection\" arXiv 2601.23163] (2026.01): \n  已经做了 behavioral C(t) curves，在 decile intervals 上测量 truncated CoT \n  的 causal contribution。与本 proposal 的 C(t) 方向高度重叠。\n\n- [Wang \"LLM Reasoning Is Latent\" arXiv 2604.15726] (2026.04): \n  形式化了 H1(latent-mediated)/H2(CoT-mediated)/H0(serial compute) 三假说。\n  本 proposal 的 G*(t) 本质上是 Wang 框架的一个经验化实现。\n\n- [CMI framework / Sathyanarayanan et al. arXiv 2602.03994] (2026.02): \n  已结合 probing 与 causal intervention（activation patching），引入 CoT \n  Mediation Index，在 StrategyQA/TruthfulQA/GSM8K 上发现 \"bypass regimes\"。\n  \n- [Gjølbye et al. arXiv 2605.15454] (2026.05):\n  hidden-state trajectory geometry + difficulty conditioning + length correction，\n  在 11 models 上证明 difficulty-geometry coupling 是 domain-specific 的。\n  \n- [Project Ariadne arXiv 2601.02314] (2026.01):\n  用 SCM + counterfactual logic 审计 agentic CoT faithfulness，发现 \n  \"Faithfulness Gap\" 和 \"Causal Decoupling\" 作为 failure mode。\n\n- 调研总结: CoT faithfulness 是 2025-2026 年最拥挤的研究方向之一，\n  已有 30+ 篇高质量论文从不同角度攻克。probe trajectory（Chrabąszcz et al.）\n  和 behavioral causal curves（Ballon et al.）已分别被独立完成；\n  probe + causal intervention 的结合也已被 CMI framework 和 Kudo et al. (EACL 2026) \n  覆盖。本 proposal 的核心位置是\"将已有的 P(t) 和 C(t) 测量做差形成 G*(t) \n  gap metric\"——这是一个 synthesis/unification framework，而非全新的发现。\n\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁。**\n\nG*(t) = P*(t) − C(t) 的核心操作是：取 Chrabąszcz et al. 风格的 probe trajectory，\n取 Ballon et al. 风格的 truncation-reinjection causal curve，然后做差。\n一个更简单的替代方案是：\n1. 直接在同一模型/数据集上分别复现 probe trajectory 和 truncation curves\n2. 将两条曲线并排展示，用简单的 correlation/divergence 统计量描述其差异\n3. 按 difficulty conditioning 做分组分析\n\n这不需要提出一个全新的 \"ICG framework\"，不需要 null-probe calibration 的复杂\nmachinery，不需要 phenomenon taxonomy 的分类体系。proposal 的增量价值在于：\n(a) null-probe calibration 作为方法论贡献（有价值但较小）；\n(b) 将 gap 映射到 named phenomena 的 taxonomy（目前完全未验证）；\n(c) TIF score 作为 instance-level diagnostic（需要验证实用性）。\n\n增量价值存在，但需要诚实地承认核心操作的简单性。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有 **3 个关键未验证假设**：\n\n1. **P*(t) 和 C(t) 的可减性假设**：P*(t) 是 AUROC（0-1 范围的分类性能），\n   C(t) 是 behavioral accuracy change under truncation（一个因果效应量）。\n   这两个量在量纲和语义上不直接可减。G*(t) = P*(t) − C(t) 的物理意义\n   取决于两者如何被归一化到可比较的尺度——proposal 对此没有充分论证。\n   \"correctness awareness the model has but doesn't channel through its CoT\" \n   这个解释是直觉上 appealing 但数学上 hand-wavy 的。\n\n2. **Trajectory shape → phenomenon type 的映射假设**：proposal 假设不同 \n   faithfulness phenomena（pre-CoT encoding, genuine reasoning, post-hoc \n   rationalization）会产生可区分的 G*(t) trajectory shapes。这是整个 \n   classification pipeline 的核心前提，但目前完全基于\"从不同论文拼接的 \n   cross-study measurements\"的推测。proposal 本身也承认这一点并设计了 \n   Phase 0b pilot，但如果 Phase 0b 失败（d < 0.3），整个框架的分类功能就不成立。\n\n3. **Null-probe calibration 能有效去除 correlative inflation**：Hewitt & Liang \n   的 selectivity 方法和 shuffled-label baseline 能去除 uniform inflation，\n   但 Chun et al. (2602.20338) 的 MCT 发现表明 inflation 是 non-uniform \n   且 temporally varying 的。P*(t) = P(t) − P_null(t) 是否足够处理 \n   non-uniform inflation 是一个开放问题。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心贡献是将两个已存在的测量维度（probe trajectories à la Chrabąszcz et al., \n   causal contribution curves à la Ballon et al.）做差形成 gap metric。\n   这是一个 natural combination，而非 surprising insight。\n   CMI framework (2602.03994) 已结合 probing 与 causal intervention；\n   Wang (2604.15726) 已形式化了 H1/H2 框架；Chrabąszcz et al. (2605.18549) \n   已做了 probe trajectories；Ballon et al. (2601.23163) 已做了 behavioral C(t)。\n   本 proposal 的 novelty delta 在于：(a) 显式的 gap metric 定义，(b) null-probe \n   calibration，(c) phenomenon taxonomy via trajectory shapes——\n   其中 (a) 是 straightforward，(b) 是方法论细节，(c) 是未验证的假设。\n   剔除 surface differences 后，真正新颖的部分不多。\n\n2. **Significance: 中** — \n   研究问题本身（CoT faithfulness）无疑是重要的，是当前 LLM safety/alignment \n   的核心议题。但三个因素限制了 significance：\n   (a) 领域极度拥挤（30+ 篇 2025-2026 论文），一个新框架的边际贡献受到稀释；\n   (b) 即使成功度量了 G*(t)，practical implication 不清晰——\n   你知道了 CoT 是 unfaithful 的，然后呢？proposal 未提出如何利用 G*(t) \n   改善 faithfulness 或指导 training；\n   (c) 如果核心发现是 positive（不同 phenomena 确实有不同 trajectory shapes），\n   多数审稿人会说 \"I would have guessed this\"——这符合直觉而非 surprising。\n   如果 negative（trajectory shapes 不可区分），则退化为 characterization paper，\n   贡献更有限。\n\n3. **Related Work: 强** — \n   Related work 覆盖极其详尽，引用了 40+ 篇相关论文，包括最新的 2026 年 5 月\n   工作（Chrabąszcz et al., Gjølbye et al., Yuan et al.）。对每篇工作的定位\n   和差异化描述准确。proposal 对 Chrabąszcz et al. 作为 \"closest concurrent work\" \n   的分析尤为到位。唯一的风险是：如此详尽的 related work 反而暴露了 novelty \n   的有限性——proposal 本质上是在已有工作的 \"缝隙\" 中填补一个 natural combination。\n\n\n【概率估计】: [18% - 28%] 中位 22%\n（注：此概率针对合理 venue 如 ICLR/ICML/NeurIPS。对 CoRL 2026: 0-2%，desk reject。）\n\n【估计理由】: \nidea 方向站得住脚——CoT faithfulness 是重要问题，probe + causal 的 temporal gap \n是一个 logical next step。但 novelty delta 有限（essentially combining two existing \nmeasurement traditions with a subtraction），且核心发现无论 positive 还是 negative \n都缺乏 surprise factor。significance 受到领域拥挤度的稀释和 practical implication \n缺失的限制。Related work 覆盖是 proposal 的亮点，但无法弥补 idea 内核的薄弱。\n形式上非常完善（dual-outcome, Phase 0b pilot, honest scoping），但形式完善度 ≠ \nidea 质量。上界主要被 Novelty（弱-中）限制——如果审稿人问 \"what's the surprising \nfinding here that I couldn't have predicted?\"，proposal 难以给出有力回答。\n\n【主要风险】: \n1. **Novelty 不足被挑战**：审稿人可能认为 G*(t) = P*(t) − C(t) 是 Chrabąszcz et al. \n   + Ballon et al. 的 trivial combination，核心 \"insight\"（gap IS the faithfulness \n   signal）是 obvious reframing of Yuan et al.'s finding，不构成独立贡献。\n2. **量纲不可比性**：P*(t)（AUROC）和 C(t)（behavioral accuracy delta）的直接相减\n   在数学上缺乏严格支撑，审稿人可能质疑 G*(t) 的物理意义和可解释性，\n   导致整个框架的理论基础被动摇。\n```\n\n**补充说明**：\n\n关于 **CoRL 2026 作为投稿目标的致命问题**：proposal 自身列出的 target venues 是 ICLR 2027（primary）和 ICML 2027（fallback），这两个都是合理选择。但如果真的要投 CoRL 2026，这篇论文会因为完全不涉及 robotics 而被 desk reject。建议确认投稿目标是否为 ICLR 2027 而非 CoRL 2026——如果确实是 ICLR 2027，上述 idea 质量评估（中位 22%）是有参考价值的。\n\nSources:\n- [Yuan et al. \"Hidden Error Awareness\" arXiv 2605.09502](https://arxiv.org/abs/2605.09502)\n- [Cox et al. \"Pre-CoT Probes\" arXiv 2603.01437](https://arxiv.org/abs/2603.01437)\n- [Chrabąszcz et al. \"Probe Trajectories\" arXiv 2605.18549](https://arxiv.org/abs/2605.18549)\n- [Ballon et al. \"Truncation-Reinjection\" arXiv 2601.23163](https://arxiv.org/abs/2601.23163)\n- [Wang \"LLM Reasoning Is Latent\" arXiv 2604.15726](https://arxiv.org/abs/2604.15726)\n- [CMI framework arXiv 2602.03994](https://arxiv.org/abs/2602.03994)\n- [Gjølbye et al. arXiv 2605.15454](https://arxiv.org/abs/2605.15454)\n- [Project Ariadne arXiv 2601.02314](https://arxiv.org/abs/2601.02314)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)\n- [FaithCoT-Bench ICLR 2026](https://arxiv.org/abs/2510.04040)\n- [Young \"Measuring Faithfulness\" arXiv 2603.20172](https://arxiv.org/abs/2603.20172)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命问题：投稿目标与会议 scope 完全不匹配】\n\n本 proposal 是一篇纯 NLP/LLM interpretability 论文，研究链式推理（Chain-of-Thought）的忠实性诊断。\nCoRL（Conference on Robot Learning）2026 是一个机器人学习会议，其 Call for Papers 明确列出的 topic 包括：\n• 机器人感知与控制的表征学习\n• 模仿学习、强化学习用于物理机器人控制\n• 机器人操作、导航、运动、驾驶、飞行\n• 机器人安全与对齐\n• 人机交互与自然语言机器人指令\n\n本 proposal 不包含任何机器人相关内容——没有机器人系统、没有物理交互、没有 sim-to-real、没有 embodied agent。Proposal 自身的 \"Target Venues\" 也写的是 ICLR 2027 和 ICML 2027，而非 CoRL。\n\n→ 投稿 CoRL 2026 的中稿概率本质上为 0%，几乎确定会被 desk reject。\n\n以下评估仍按标准 rubric 对 idea 质量进行客观打分（可为后续投稿 ICLR/ICML 提供参考），但概率估计将基于 CoRL 这个具体目标会议。\n\n\n【领域调研】:\n- [Chrabąszcz et al., arXiv 2605.18549] (2026): \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\"。最直接的竞争工作。在 Llama-8B-R1-Distill 和 Qwen3-4B/8B/14B 上追踪每个 token 位置的 probe 轨迹，提取 60+ 信号处理特征（volatility、trend、steady-state、autocorrelation 等），max-pooling 达到 91-97% AUROC，比 static probe 提升最高 17pp。但缺少 causal contribution 维度和 gap metric。本 proposal 的 P*(t) 部分与此高度重叠。\n\n- [Yuan et al., arXiv 2605.09502] (2026): \"Hidden Error Awareness: The Signal Is Diagnostic, Not Causal\"。确立了 \"diagnostic-not-causal\" 这一核心发现——linear probe 在首步即达 0.79 AUROC、整体 0.95 AUROC，但四种干预策略（activation steering、probe-guided best-of-N、self-correction、activation patching）全部失败。这是本 proposal 整个 framework 的 motivating observation，但也意味着核心 insight 已经被他人报告。\n\n- [Cox et al., arXiv 2603.01437] (2026): \"Decoding Answers Before Chain-of-Thought\"。在 instruction-tuned 模型上 probe AUC > 0.9，steering flip rate > 50%；但在 reasoning model (GPT-OSS-20B) 上 flip rate \"negligible\"。独立确认了 diagnostic-causal gap。\n\n- [Ballon et al., arXiv 2601.23163] (2026): \"Probing the Trajectories of Reasoning Traces\"。提供 truncation-reinjection 协议：在 decile interval 截断 CoT 后重新注入，测量准确率单调上升。三种 control condition（random tokens、swapped traces、shuffled tokens）验证 sequential content 是关键因素。这正是本 proposal C(t) 的主要方法之一，方法论层面已被前人建立。\n\n- [Wang, arXiv 2604.15726] (2026): \"LLM Reasoning Is Latent, Not the Chain of Thought\"。提出 H1（latent-mediated）/ H2（CoT-mediated）/ H0（serial compute）三假设框架。本 proposal 声称 G*(t) 可 operationalize H1/H2 区分——但这一理论映射较为表面（G*(t) >> 0 → H1, G*(t) ≈ 0 → H2），并非严格的因果推断。\n\n- [Gjølbye et al., arXiv 2605.15454] (2026): \"Reasoning Models Don't Just Think Longer, They Move Differently\"。研究 hidden-state trajectory geometry 与 difficulty 的耦合关系，发现 length correction 后 difficulty 仍与 trajectory 几何系统性相关（ρ⊥ = +0.41 on Codeforces），但 domain-specific。本 proposal 的 difficulty conditioning 思路与此高度一致。\n\n- [FaithCoT-Bench, ICLR 2026]: 首个 instance-level CoT unfaithfulness benchmark，1000+ trajectories，细粒度标注。提供了 ground-truth 标准，本 proposal 的 TIF score 需要与之对标。\n\n- 调研总结：CoT faithfulness 是 2025-2026 年的热点方向，已经出现了大量高质量工作分别覆盖了 (1) probe 时序动态、(2) causal intervention 失败、(3) 截断-重注入行为测试、(4) difficulty conditioning。本 proposal 的核心定位是\"将已有的 probe 端（P*(t)）和 causal 端（C(t)）组合起来计算差值 G*(t)\"——这是一个 synthesis/integration 型贡献，而非根本性新洞见。各组成部分的方法论均已由他人建立。\n\n\n【Trivial Alternative 检验】:\n存在明显的更简单替代方案。\n\n(1) 最简单的版本：直接比较 probe accuracy（来自 Yuan et al. / David / Zhang et al. 的现成数据）和 behavioral accuracy gain（来自 Ballon et al. 的截断曲线），画在同一张图上即可观察到所谓的 \"information-contribution gap\"。不需要定义新 metric、不需要 null-probe calibration、不需要 phenomenon classification pipeline。这个简单对比已经足以传达核心 message \"models know more than their CoT uses\"，而这一 message 已被 Yuan et al. 和 Cox et al. 直接报告。\n\n(2) 对于 phenomenon classification：简单地按 P*(0) 的高低（pre-CoT encoding vs. not）和 behavioral accuracy gain 的斜率（genuine reasoning vs. rationalization）做 2D 分桶，可能就能区分 2-3 种现象。是否需要完整的 G*(t) temporal fingerprint + 60+ signal features + DTW 分类？这一复杂度的增量价值尚不明确。\n\n增量价值：proposal 的增量主要在 (a) null-probe calibration 提供更干净的信号，(b) temporal resolution 提供更细粒度的分析，(c) multi-method C(t) 提供鲁棒性。这些是 methodological polish，不是 conceptual breakthrough。\n\n\n【前提假设检验】:\n核心逻辑链中有两个关键的未验证假设：\n\n(1) **\"不同 faithfulness phenomena 会产生可区分的 G*(t) temporal signature\"——这是整篇论文的核心赌注，且目前完全未经验证。** Proposal 的 phenomenon predictions（pre-CoT encoding → constant high gap; genuine reasoning → converging gap; rationalization → widening gap）是从不同论文、不同模型、不同数据集的结果 \"组装\" 出来的理论预测。Phase 0b pilot 正是为了验证这一点，但 proposal 自己也承认 \"cross-study heterogeneity may overestimate separability\"。如果同一模型同一数据集上的 G*(t) 曲线没有清晰的形状差异（d < 0.3），则核心 contribution 崩塌。\n\n(2) **P*(t) 和 C(t) 是否在数学上可减（commensurable）。** P*(t) 是 probe AUROC（一个分类性能度量），C(t) 是 behavioral accuracy change（一个因果效应度量）。这两个量的量纲和尺度完全不同。直接做减法 G*(t) = P*(t) − C(t) 的物理意义不明确——AUROC 0.8 减去 accuracy gain 0.3 等于 0.5，这个 0.5 代表什么？Proposal 没有讨论这一 commensurability 问题。\n\n\n【3 维度打分】:\n  1. Novelty: 弱 — 核心 idea 是 \"将 probe 时序曲线和 causal contribution 时序曲线放在一起做差值\"。两端的方法论分别由 Chrabąszcz et al. (probe trajectories)、Ballon et al. (truncation-reinjection C(t)) 建立；\"diagnostic-not-causal\" gap 已由 Yuan et al. 和 Cox et al. 直接报告。Proposal 的增量是 combination + calibration + phenomenon classification——这是 methodological integration，而非 conceptual novelty。即使 phenomenon classification 成功，预测的 signatures 大多是 \"从定义中可推导出来的\"（e.g., pre-CoT encoding 当然 P*(0) 高且 C(t) 低），审稿人更可能评价 \"I would have guessed this\" 而非 \"surprising\"。与 Chrabąszcz et al. 的差异化主要在于加入了 C(t) 维度，但 C(t) 的方法论也来自 Ballon et al.。\n\n  2. Significance: 中 — CoT faithfulness 是一个重要的研究方向，理解 \"models know but don't use\" 对 alignment 和安全有实际意义。如果 temporal fingerprint classification 能够工作，提供 instance-level 诊断工具有实用价值。但 (a) 这是一篇纯 diagnostic/measurement 论文，不提供解决方案；(b) practical impact 有限——得到 TIF score 后能做什么？(c) 如果 phenomenon classification 失败（Phase 0b d < 0.3），退化为 \"gap exists and varies with difficulty\" 的 characterization paper，贡献进一步缩水。对于 ICLR/ICML 属中等重要性；对于 CoRL 完全不相关。\n\n  3. Related Work: 强 — 这是本 proposal 最突出的优点。对近期文献的覆盖非常全面（30+ 篇），对 Chrabąszcz et al.、Yuan et al.、Cox et al.、Ballon et al. 等最直接竞争/互补工作的定位清晰，差异化描述诚实（不过分夸大自己的 novelty）。引用的论文经调研验证确实存在且描述准确。文献综合水平高于多数 proposal。\n\n\n【概率估计】: [0% - 2%] 中位 0%\n【估计理由】: \n这个概率估计基于目标会议 CoRL 2026。CoRL 是 Conference on Robot Learning，其 scope 严格限定在机器人学习交叉领域（机器人感知、控制、操作、导航、模仿学习、强化学习用于物理机器人等）。本 proposal 是一篇纯 NLP/LLM interpretability 论文，研究 Chain-of-Thought 推理的忠实性度量，不包含任何机器人相关内容。这是一个根本性的 venue mismatch，几乎确定会被 desk reject。Proposal 自身列出的 Target Venues 也是 ICLR 2027 和 ICML 2027，进一步确认了这不是为 CoRL 准备的工作。\n\n如果改投 ICLR 2027（proposal 自己的首选目标），仅基于 idea 质量我估计概率约为 20-30%（中位 ~25%）。理由：idea 方向正确（CoT faithfulness 是热点），文献覆盖出色，但核心 novelty 是 synthesis/integration 型，各组成部分已有前人工作；核心 phenomenon classification 是未验证的赌注；核心 metric G*(t) 的 commensurability 存疑；predicted temporal signatures 偏 \"obvious from definitions\"。Novelty 弱这一维度是限制上界的关键因素。\n\n【主要风险】: \n1. **致命：venue mismatch。** CoRL 2026 不接受纯 NLP interpretability 工作，投稿等同于浪费一次提交机会。\n2. **Idea 层面（针对 ICLR/ICML 投稿）：novelty 是 integration 型而非 conceptual 型。** 审稿人很可能认为 \"just putting Chrabąszcz's P(t) and Ballon's C(t) together and subtracting\" 不构成足够的 novelty delta，尤其当 \"diagnostic-not-causal gap\" 这一 core message 已被 Yuan et al. 直接报告的情况下。\n```\n\n**补充建议**：如果团队希望推进这个 idea，强烈建议：\n1. **立即更换目标会议**为 ICLR 2027 或 ICML 2027（与 proposal 自身的 Target Venues 一致）；\n2. 认真解决 G*(t) = P*(t) − C(t) 的 commensurability 问题——两个量纲不同的量做减法需要严格的归一化论证；\n3. 尽早执行 Phase 0b pilot——如果 phenomenon separability 不成立，需要及时调整论文定位。\n\nSources:\n- [Chrabąszcz et al. - Monitoring the Internal Monologue](https://arxiv.org/abs/2605.18549)\n- [Yuan et al. - Hidden Error Awareness](https://arxiv.org/abs/2605.09502)\n- [Cox et al. - Decoding Answers Before Chain-of-Thought](https://arxiv.org/abs/2603.01437)\n- [Ballon et al. - Probing the Trajectories of Reasoning Traces](https://arxiv.org/abs/2601.23163)\n- [Wang - LLM Reasoning Is Latent](https://arxiv.org/abs/2604.15726)\n- [Gjølbye et al. - Reasoning Models Move Differently](https://arxiv.org/abs/2605.15454)\n- [FaithCoT-Bench (ICLR 2026)](https://openreview.net/forum?id=lN3yKqqzF1)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWe propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.\n\nThe framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness (explicitly targeting right/wrong prediction — justified over answer-content probes by broader applicability beyond binary tasks, grounding in the diagnostic-not-causal finding which is about correctness, and more direct faithfulness interpretation — with supplementary answer-content analysis on binary/MC subsets), and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions validating sequential content matters, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\nPositioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes across 4 reasoning models — our framework adds the entire causal contribution dimension, the calibrated gap metric, null-probe calibration with MCT geometric validation, phenomenon taxonomy, and task-difficulty conditioning. Their probe-trajectory methodology validates our P*(t) direction; we extend it to the dual-estimator gap that no existing framework provides.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) constructs real G*(t) curves from the SAME model and dataset and tests whether at least 2 phenomena produce distinguishable trajectories (effect size d > 0.5) before committing to the full classification pipeline — addressing the concern that semi-synthetic simulation from cross-study measurements overestimates real-data accuracy. The semi-synthetic simulation is retained as hypothesis generation producing testable predictions, not as evidence.\n\nTask-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits, the ICLR 2026 Workshop finding, and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific (weaker on MATH) — reveals the decorative→load-bearing transition with practical guidance on when chain-of-thought adds genuine value, applying length correction (residualizing on log(N)) to avoid generation-length confounds.\n\nThe paper focuses on four core contributions: (a) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. to demonstrate the value of the causal contribution dimension; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real data; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) probe-target analysis contrasting correctness vs. answer-content gaps. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs) as the primary bottleneck.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — with linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find that steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four distinct intervention strategies (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B parameters and report that ALL fail: 'RL training does not close the diagnostic–causal gap.' This diagnostic-causal gap — the divergence between what information is available in a model's hidden states and what information the chain-of-thought reasoning text causally contributes — is NOT a methodological obstacle to overcome; it IS the central phenomenon. Critically, the literature conflates two distinct probe targets: answer-content probes (Cox et al.: predicting the specific answer on binary tasks, models ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: predicting right/wrong on models up to 72B; Zhang et al.: per-chunk correctness on 7B-70B). This distinction matters because the gap's interpretation differs: answer-content gaps mean 'the model has already decided but CoT doesn't derive the answer,' while correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.' Meanwhile, the temporal dynamics of this gap are now empirically grounded: David (2511.14773) shows probe accuracy stabilizes at 0.84 AUC by token 4, remaining ~0.8 through token 100, with task-difficulty conditioning revealing easy (0.84) vs. hard (0.76) signatures. Zhang et al. (2504.05419) report chunk-level probe trajectories rising from 65% at 10% of reasoning to 79% at 100% on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with a characteristic dip at 5-10% of reasoning followed by recovery. Chrabąszcz et al. (2605.18549) demonstrate that temporal probe trajectories with 60+ signal-processing features achieve up to 17pp improvement over static probes, showing that trajectory dynamics capture information invisible to single-timepoint measurements. These temporal profiles suggest that different modes of CoT unfaithfulness — pre-CoT encoding, post-hoc rationalization, reasoning theater, myopic planning, thinking-answer gap — produce distinguishable temporal divergence signatures. Yet no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline: Chrabąszcz et al. provide the closest probe-trajectory methodology but lack any causal contribution component, gap metric, probe calibration, or phenomenon taxonomy; Ballon et al. (2601.23163) provide behavioral causal curves via truncation-reinjection but lack hidden-state measurement; the CMI framework provides layerwise causal audit on ~50 examples but no temporal resolution; Zhao et al.'s True Thinking Score provides per-step causal contribution but no probe-side measurement. The gap between diagnostic information availability and causal contribution IS the phenomenon of interest, not an obstacle.\n\n## Opportunity\nThe field has independently produced the measurement tools needed for a unified temporal framework, but these tools remain siloed. The opportunity is fourfold:\n\n(1) **Temporal gap measurement.** Despite rapid accumulation of probe measurements (David: 0.84 at t=4; Zhang: 0.82-0.91 on chunks; Yuan: 0.95 overall, 0.787 first-step; Esakkiraja: >90% pre-generation; Chrabąszcz et al.: 91-97% AUROC with max-pooling on trajectories), no work tracks the full-timeline divergence between probe-estimated information availability and intervention-estimated causal contribution. Chrabąszcz et al. (2605.18549) come closest on the probe side — extracting 60+ signal-processing features from probe trajectories across 4 reasoning models and 4 datasets, achieving up to 17pp improvement over static probes on GSM8K — but they target outcome prediction (correctness, harmfulness) rather than the faithfulness gap, and provide no causal contribution measurement. Their work validates that temporal probe trajectories capture dynamics invisible to static probes (confirming our P*(t) direction); our framework extends this via the dual-estimator gap G*(t) = P*(t) − C(t) that requires the additional causal contribution dimension, null-probe calibration, and phenomenon mapping. On the causal side, Ballon et al. (2601.23163) provide behavioral C(t) curves via truncation-reinjection at decile intervals on Qwen3/gpt-oss across GPQA-Diamond and MMLU-Pro — showing monotonic accuracy increase from 30.8-42.3% to 49.0-73.1% with control conditions validating that sequential content (not just context length) matters — but lack hidden-state measurement. The gap between these two measurement traditions IS the framework's niche.\n\n(2) **Phenomenon unification with honest scoping.** The CoT faithfulness literature treats each failure mode as separate: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al. 2603.01437; Esakkiraja et al. 2604.01202), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103), thinking-answer gap. We propose that 2-3 of these are confidently distinguishable via trajectory-shape signatures in the information-contribution gap G*(t), with 4-5 as a stretch goal requiring additional features. The honest scoping — validated through an empirical pilot on real data before committing to full classification — is itself a contribution to a field prone to over-claiming.\n\n(3) **Task-difficulty conditioning.** The ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration show easy→decorative, hard→faithful. David's easy/hard splits (0.84 vs. 0.76 at t=32) provide probe-level evidence. Gjølbye et al. (2605.15454) demonstrate that difficulty is systematically coupled to hidden-state trajectory geometry even after length correction (ρ⊥ = +0.41 for reasoning models vs. −0.06 for baselines on competitive programming), with domain-specific strength. A difficulty-conditioned gap framework can answer the practical question: at what difficulty level does CoT transition from decorative to load-bearing?\n\n(4) **Probe target clarification.** The field has not confronted the distinction between answer-content probes (Cox et al.: binary tasks, ≤9B) and correctness probes (Yuan et al.: up to 72B). A framework that explicitly measures correctness awareness gap — and contrasts it with answer-content gap on applicable tasks — provides the first principled treatment of what 'knowing but not using' means.\n\nTwo prior works have combined probing with causal interventions: Kudo et al. (EACL 2026) on synthetic arithmetic, and the CMI framework (2602.03994) on ~50 examples. Wang (2604.15726) formalizes the need via competing hypotheses (H1: latent-mediated, H2: CoT-mediated, H0: serial compute) and proposes compute-audited designs — our ICG framework provides an empirical methodology to distinguish H1 from H2 at each token position. Neither Kudo et al. nor CMI provides: (a) full temporal-position coverage on natural benchmarks, (b) mapping to named faithfulness phenomena, (c) a standalone instance-level diagnostic, (d) systematic multi-model comparison, (e) robustness validation — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) an empirical pilot validating phenomenon separability on real data.\n\n## Landscape\n**Probe-based temporal measurement (foundational for our P*(t) component).** Chrabąszcz et al. (2605.18549) is the closest concurrent work: they introduce probe trajectories — tracking concept probability at each generated token — and extract 60+ signal-processing features (volatility, trend, steady-state, temporal segmentation, boundary transients, autocorrelation) via 3-layer MLP probes with Multi-Instance Learning meta-probe across layers. Key results: max-pooling achieves 91-97% AUROC on harmfulness detection (vs. 33-61% for average-pooling, demonstrating average/last-token pooling collapses to near-random); up to 17pp improvement over static probes on GSM8K mathematical error prediction across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours total). Critical differentiators from our framework: (a) NO causal contribution component — they measure only probe accuracy trajectories, not whether CoT causally contributes; (b) NO gap metric — just trajectory vs. static comparison for outcome prediction; (c) NO null-probe calibration or MCT geometric validation — their 3-layer MLP probes are uncalibrated; (d) NO phenomenon taxonomy — they separate correct/incorrect or safe/harmful, not faithfulness modes; (e) NO task-difficulty conditioning. Their 60+ feature extraction methodology is complementary and could enhance our trajectory-shape classification. David (2511.14773) trains per-position probes on reasoning models, finding 0.84 AUC at t=4, stable ~0.8 through t≈100, with easy/hard splits of 0.84 vs. 0.76 at t=32 on Qwen3-8B. Zhang et al. (2504.05419) probe R1-Distill models (7B/32B/70B) for correctness at each reasoning chunk, achieving 0.82-0.91 AUROC on GSM8K/MATH/AIME, with a rising trajectory from 65% at 10% chunk to 79% at 100%, enabling 24% token reduction via early-exit. Yuan et al. (2605.09502) report 0.95 AUROC on Qwen-3B, 0.852 on DeepSeek-R1-7B, 0.787 from first-step hidden states alone, and a concealment gap of 0.197 AUROC between hidden-state (0.787) and text-surface (0.590) classifiers — using correctness probes (right/wrong), not answer-content probes. Esakkiraja et al. (2604.01202) find >90% AUROC pre-generation on Qwen3-4B and GLM-Z1-9B, with a characteristic dip at 5-10% of reasoning and recovery to near-100% by think_end. Cox et al. (2603.01437) use answer-content probes (predicting specific answer A/B on binary tasks: Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) achieving >0.9 AUC on instruction-tuned Gemma-2 (2B, 9B) and Qwen-2.5 (1.5B, 3B, 7B) models, with causal validation via steering (>50% flip rates) — but 'the answer flip rate is negligible against the orthogonal baseline' on the reasoning model GPT-OSS-20B. Additional probing work: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop, probing F1 90-100%, steering 46% recovery).\n\n**The diagnostic-not-causal evidence (motivating our framework).** Yuan et al. (2605.09502) is the decisive study: four interventions — activation steering (at most +4%), probe-guided best-of-N (matches random), self-correction (hurts accuracy −3%), activation patching (destroys coherence at α=0.5) — all fail. Tested on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. Key quote: 'The error signal is a diagnostic readout—a summary statistic of computation quality—not a causal component that can be edited.' Cox et al. (2603.01437) independently confirm: steering fails on reasoning models despite high probe accuracy. This establishes that probe accuracy ≠ causal potency on reasoning models, which is the foundational observation our framework exploits.\n\n**Behavioral trajectory probing (foundational for our C(t) component).** Ballon et al. (2601.23163) introduce the truncation-reinjection protocol: generate full reasoning traces on Qwen3-4B/8B/14B and gpt-oss-20B/120B, truncate at decile intervals (10-100%), reinject with early-stopping suffix, measure answer-choice probability distributions. Key results: accuracy increases monotonically from 30.8-42.3% (no reasoning) to 49.0-73.1% (full trace) on GPQA-Diamond; decision commitment tracks similarly. Three control conditions validate causal content: random tokens (+2.1-4.3%), swapped traces (+3.2-8.7%), and shuffled tokens (+0.3-10.8%) all substantially underperform intact truncated traces (+18.1-33.1%), confirming sequential content — not just context length — drives gains. Stronger models rescue weak-model errors at 43-68% rate with free continuation vs. 28-51% anchoring in base mode. Explicitly disclaims faithfulness-to-internal-computations analysis, making it a direct precursor to our prefix-truncation C(t) estimator. Zhao et al. (2510.24941) introduce the True Thinking Score (TTS), measuring per-step causal contribution via numerical perturbation and ATE computation on DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7. Ye et al. (2602.11201) introduce NLDD, finding a Reasoning Horizon at 70-85% of chain length on 3 models across synthetic tasks. Basu & Chakraborty (2603.22816) propose a decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026) provides another causal measurement approach.\n\n**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize. The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, DialoGPT on StrategyQA (20), TruthfulQA (10), GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors operating on small samples or synthetic tasks.\n\n**Latent-reasoning theory.** Wang (2604.15726) formalizes three competing hypotheses about LLM reasoning: H1 (reasoning is primarily mediated by latent-state trajectories), H2 (reasoning is primarily mediated by explicit surface CoT), H0 (most reasoning gains are better explained by generic serial compute). Proposes compute-audited designs with six experimental arms (baseline, surface manipulation, surface control, latent intervention, latent control, compute-only expansion) and evidence tiers (probe-only = suggestive, compute-matched causal = strongest). Our ICG framework operationalizes Wang's H1/H2 distinction: when G*(t) >> 0, hidden states encode correctness awareness that CoT doesn't contribute (H1-consistent); when G*(t) ≈ 0, CoT is mediating (H2-consistent).\n\n**Temporal hidden-state dynamics (concurrent complementary work).** Gjølbye et al. (2605.15454) study hidden-state trajectory geometry across 11 models (6 reasoning: R1-Distill-Qwen-7B/14B/32B, R1-Distill-Llama-8B, QwQ-32B, Phi-4-Reasoning; 5 instruction-tuned baselines) on competitive programming (500 Codeforces), math (500 MATH), and Boolean SAT (500 SATBench). After length correction (residualizing directness/curvature on log(N)), difficulty remains systematically coupled to trajectory geometry: reasoning models show ρ⊥^D = +0.41 on Codeforces vs. −0.06 for baselines (raw correlations reverse from −0.73 to +0.41), with weaker effects in math (+0.05 vs. −0.07) and non-specific effects in SAT (+0.27 vs. +0.23). Critically, prompt-stage linear probes do NOT mirror these geometric effects — reasoning dynamics manifest during generation, not at input. Their length correction methodology and domain-specificity finding are relevant for our temporal analysis and difficulty conditioning. Furuya & Tanimura (2605.01853) introduce StALT, a training-free trajectory statistic separating correct from incorrect reasoning trajectories. Herrmann et al. (2605.09159) study 'internal polylogue' dynamics: persona vectors tracked temporally across MMLU-Pro in four open-weight models. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, tracking concept-direction alignment per step on Qwen 3-4B; find easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals, achieving 14-70% token savings on R1-Distill/Phi-4/Qwen3.\n\n**Probe calibration and inflation (methodological foundation).** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity. Ravichander et al. (2020) demonstrate properties recoverable even when unused. Voita & Titov (2020) show MDL-based probing reveals accuracy doesn't substantially favor pretrained over random. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning: geometric separability peaks transiently as a 'geometric pulse' while probe accuracy remains high afterward — direct evidence that probe accuracy overestimates information availability. We address this via null-probe calibration: P*(t) = P(t) − P_null(t).\n\n**Trajectory-shape analysis (supporting our shape-based classification).** Entropy trajectory paper (2603.18940): monotonicity predicts reliability regardless of absolute levels (+5.8pp). RQA analysis (2602.06266): temporal features outperform aggregates 36.94% vs. 28.97%. Microsoft trajectory geometry (2604.05655): 0.852 AUC from shape features vs. 0.649 baseline. This literature validates trajectory shapes as diagnostic features.\n\n**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence. Task-difficulty moderation: ICLR 2026 Workshop and Li et al. (2510.22362).\n\n**Reasoning-model internal dynamics.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill.\n\n**Benchmarks, surveys, pathology diagnostics.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Liu et al. (2602.13904): text-level metrics for rationalization/encoded/internalized reasoning. Reasoning Theater (2603.05488). Young (2603.26410). 'Lie to Me' (2603.22582). Various early-exit methods: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT.\n\n**What remains open.** No extant framework provides: (1) a full-timeline information-contribution gap curve pairing calibrated probe trajectories with causal contribution estimation — Chrabąszcz et al.'s probe trajectories are the closest but lack the entire C(t) dimension, gap metric, and calibration; (2) an empirically-validated phenomenon trajectory-shape taxonomy grounded in real within-model, within-dataset G*(t) curves rather than cross-study semi-synthetic assembly; (3) an instance-level diagnostic score derived from the temporal gap; (4) difficulty-conditioned gap analysis with domain-specific nuance (following Gjølbye et al.'s finding of domain-dependent coupling strength); or (5) a principled treatment of the probe-target distinction (correctness vs. answer-content) and its implications for gap interpretation. The calibrated temporal ICG framework is unique in combining all five.\n\n## Approach\nWe propose the Information-Contribution Gap (ICG) framework: a calibrated, temporally-resolved diagnostic that measures the divergence between information available in hidden states and information that causally contributes to model outputs, tracked across the full chain-of-thought generation trajectory.\n\n**Formal Framework.** Define two time-varying quantities at each token position t during CoT generation:\n\n(i) *Calibrated Information Availability* P*(t): Cross-validated AUROC of a linear probe on layer-l hidden states at position t, calibrated via null-probe normalization (P*(t) = P(t) − P_null(t), following Hewitt & Liang 2019 selectivity, where P_null is trained on shuffled labels). **Probe target: correctness (right/wrong).** We choose correctness over answer-content for three reasons: (a) broader applicability — correctness probes generalize beyond binary/MC tasks (Cox et al.'s answer-content probes are limited to binary A/B on 4 tasks), while correctness probes (Yuan et al.) work across model families up to 72B; (b) the 'diagnostic not causal' finding that motivates the entire framework is specifically about correctness probes (Yuan et al.'s four-intervention failure on correctness probes); (c) correctness gaps are more directly interpretable for faithfulness — G*(t) >> 0 means 'the model's hidden states encode awareness that its answer is right/wrong, but its CoT does not causally reflect this self-monitoring.' On binary/MC task subsets, we additionally train answer-content probes to test whether the 'what answer' gap differs from the 'whether correct' gap — a supplementary analysis testing whether pre-CoT encoding operates on content or meta-cognition. This measures excess correctness awareness above correlative features. We probe at layers L/4, L/2, 3L/4, L to capture layer-wise dynamics. MCT geometric validation (Chun et al. 2602.20338) on 500 examples confirms whether calibrated probe signal reflects geometrically organized information rather than mere retrievability. Note: Chrabąszcz et al. (2605.18549) demonstrate that probe trajectories with 60+ signal-processing features substantially outperform static probes (up to 17pp on GSM8K). We adopt their insight that temporal dynamics are essential, while adding null-probe calibration (which they lack) and extending to the dual-estimator gap. Where applicable, we incorporate their feature categories (volatility, trend, steady-state, boundary transients) as additional trajectory descriptors for phenomenon classification in Phase 3.\n\n(ii) *Causal Contribution* C(t): The causal contribution of CoT up to position t, estimated via three complementary methods: (a) prefix-truncation ablation — measuring P(correct | CoT[:t]) vs. P(correct | full CoT), following Ballon et al.'s (2601.23163) truncation-reinjection protocol with their three control conditions (random tokens, swapped traces, shuffled tokens) to validate that C(t) measures genuine sequential content contribution rather than context-length effects (their finding: shuffled tokens retain +0.3-10.8% vs. intact +18.1-33.1%); (b) paraphrase perturbation — replacing CoT segments with meaning-preserving paraphrases and measuring answer stability; (c) NLDD-based influence scoring (Ye et al. 2602.11201) — measuring how corruption at position t degrades the answer distribution. Using multiple C(t) estimators provides robustness against single-method artifacts, following Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive.\n\n**The Information-Contribution Gap.** G*(t) = P*(t) − C(t). This gap is the primary diagnostic signal:\n- G*(t) ≈ 0: Correctness awareness and causal contribution are aligned (necessary for faithfulness)\n- G*(t) >> 0: The model encodes correctness awareness it does not causally use in its CoT (diagnostic excess — the model 'knows but doesn't use')\n- G*(t) < 0: The CoT contributes to correctness beyond what hidden states encode at that point (information assembled during reasoning)\n\nBecause P*(t) is null-probe-calibrated, uniform correlative inflation is removed. C(t) is not subject to probe inflation as it measures behavioral change under intervention. The gap G*(t) is interpretable as 'calibrated correctness awareness the model has but doesn't channel through its CoT at position t.' Following Wang's (2604.15726) H1/H2 framework: G*(t) >> 0 is H1-consistent (latent-mediated reasoning), G*(t) ≈ 0 is H2-consistent (CoT-mediated reasoning).\n\n**Phenomenon Signature Predictions (2-3 confident, 4-5 stretch).** We ground predictions in real probe data but adopt honest scoping informed by the concern that cross-study heterogeneity may overestimate separability:\n\n*Primary targets (HIGH confidence, validated in Phase 0b pilot):*\n(i) *Pre-CoT encoding*: G*(t) starts high and stays high. Grounded in: David's 0.84 AUC at t=4, Esakkiraja's >90% pre-generation AUROC, Cox's >0.9 pre-CoT AUC. P*(0) > 0.5 (after calibration), C(t) rises slowly. Shape: large constant gap.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. Grounded in: Zhang et al.'s 65%→79% chunk trajectory, Li et al.'s finding that hard→faithful, Ballon et al.'s monotonic accuracy increase with reasoning length. P*(t) rises gradually, C(t) tracks P*(t). Shape: co-rising curves, small/decreasing gap.\n(iii) *Post-hoc rationalization*: G*(t) starts moderate, rises during CoT. P*(t) stable (David: ~0.80 from t=4 through t=100), C(t) remains flat despite token generation. Shape: widening gap.\n\n*Stretch targets (MODERATE confidence, require additional features):*\n(iv) *Steganographic encoding*: G*(t) dip-and-recovery. Potentially consistent with Esakkiraja's dip at 5-10%. May require multi-layer analysis to separate from noise.\n(v) *Reasoning Theater*: EMPIRICAL QUESTION. Under non-uniform inflation, may overlap with pre-CoT encoding or post-hoc rationalization. Additional features — layer-wise P*(t) distribution, C(t) variance under paraphrase perturbation, Chrabąszcz-style signal features (autocorrelation, boundary transients, dwell-time run-lengths) — may enable separation. Whether Theater is cleanly separable is reported honestly with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** We construct semi-synthetic G*(t) curves grounded in real published data to generate testable predictions about trajectory-shape separability — but we do NOT treat this as evidence of real-data separability (published measurements come from different models, datasets, and setups, introducing heterogeneity that does not match within-dataset variance). Instead, the simulation identifies: (a) which trajectory features are most discriminative in principle, (b) what minimum effect sizes real-data classification needs to achieve, (c) where non-uniform inflation causes theoretical overlap between phenomena. I_probe(t) profiles drawn from published measurements (David, Zhang, Esakkiraja, Yuan), C(t) profiles modeled from NLDD (Ye et al.) and TTS (Zhao et al.) data, non-uniform inflation calibrated against Chun et al.'s MCT finding. The real validation comes from Phase 0b.\n\n**Phase 0a: Gap Characterization (Weeks 1-2.5).** Three objectives on 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct empirical P*(t) and C(t) curves at token-level resolution\n(ii) Validate null-probe calibration: P_null(t) shows high accuracy (inflation exists) but P*(t) shows meaningful variance (calibration reveals structure)\n(iii) Characterize causal potency: following Cox et al.'s protocol, measure answer flip rates via probe-direction steering on reasoning vs. instruction-tuned models\n\nExpected outcome (base case): Causal potency is low on reasoning models, confirming the diagnostic-not-causal property and validating the ICG framework's interpretive power. If causal potency is unexpectedly high, this is an exciting upgrade. Either outcome is scientifically valuable.\n\n**Phase 0b: Empirical Pilot for Phenomenon Separability (Weeks 2.5-4).** This phase validates that trajectory-shape classification is feasible on real data before committing to the full pipeline. On the SAME model (R1-Distill-Qwen-7B) and datasets (GSM8K + MATH-500, 1000 examples), construct real G*(t) curves and test whether at least 2 phenomena produce distinguishable trajectories. Protocol: (i) partition examples by difficulty quintile and model behavior (easy-correct with high P*(0) → pre-CoT encoding candidates; hard-correct with rising P*(t) tracking C(t) → genuine reasoning candidates; incorrect with stable P*(t) and flat C(t) → post-hoc rationalization candidates); (ii) compute full G*(t) for each partition; (iii) test effect size d > 0.5 on at least 2 trajectory features between partitions. Apply Gjølbye et al.'s (2605.15454) length correction (residualizing trajectory features on log(N)) to ensure differences are not conflated with generation-length effects. Success criterion: d > 0.5 between at least 2 partitions on 2+ features. If d < 0.3 across all features, downscope to a characterization paper (gap exists and varies with difficulty, but trajectory shapes are not cleanly phenotypic) — still a strong contribution given no prior full-timeline G*(t) measurement exists.\n\n**Phase 1: Full ICG Construction (Weeks 4-9).** Conditional on Phase 0b showing separability (d > 0.5). Extend to 4 models (add QwQ-32B or R1-Distill-32B) × 4 benchmarks (add GPQA-Diamond or AIME). Full calibrated P*(t) with null-probe normalization + MCT concordance check on 500 examples. Three C(t) estimators with Ballon et al.-style controls (random, swap, shuffle baselines). Cross-reference with TTS (Zhao et al.) at step boundaries. Bootstrap confidence intervals on G*(t).\n\n**Phase 2: Task-Difficulty Conditioning (Weeks 7-11).** Partition each benchmark into difficulty quintiles (using model accuracy as proxy). Measure G*(t) per quintile. Hypothesis grounded in David's easy/hard data, Li et al.'s finding, and Gjølbye et al.'s difficulty-geometry coupling: easy problems show large persistent gap (decorative CoT), hard problems show converging gap (load-bearing CoT). Following Gjølbye et al., apply length correction and report domain-specific effects — expecting stronger effects on math/code benchmarks than MMLU, given their finding of ρ⊥ = +0.41 on Codeforces vs. +0.05 on MATH. The transition point — where G*(t) shifts from decorative to genuine — provides practical guidance on when CoT adds value.\n\n**Phase 3: Phenomenon Classification and Robustness (Weeks 9-14).** Apply trajectory-shape classification to real data. Target: 2-3 cleanly separable phenomena, with 4-5 reported honestly including overlap. Incorporate Chrabąszcz et al.'s feature categories (volatility, trend, boundary transients, autocorrelation) alongside our gap-specific features (initial G* value, G* slope, convergence rate, dC/dt locality). Six robustness ablations following Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection (single best vs. multi-layer); (c) C(t) estimator agreement (prefix vs. paraphrase vs. NLDD); (d) gap normalization method; (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content on binary/MC subsets). Report sensitivity ranges across all dimensions.\n\n**TIF Score.** Temporal Information-contribution Faithfulness score: normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s text-level metrics.\n\n**Paper Focus (Tightened).** Core contributions: (1) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al.'s probe trajectories — demonstrating the value added by the causal contribution dimension and gap metric; (2) Phase 0b empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real within-model, within-dataset data; (3) task-difficulty conditioning revealing the decorative→load-bearing transition with domain-specific strength following Gjølbye et al.'s nuance. Supporting: robustness ablations (6 dimensions); TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness probe comparison; semi-synthetic simulation as hypothesis generation.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT cross-reference. Gjølbye-style length correction on all temporal analyses.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~830 H100-hours (Phase 0a characterization: 80 hrs [3 models × 3 datasets, probe training + prefix ablation + steering tests]; Phase 0b empirical pilot: 30 hrs [1 model × 2 datasets, full G*(t) construction + partition analysis + length correction]; Phase 1 full ICG: 120 hrs [4 models × 4 benchmarks, multi-layer probes + 3 C(t) estimators]; Phase 2 difficulty conditioning: 50 hrs; Phase 3 phenomenon classification + robustness ablations: 50 hrs; NLDD on 32B model: 250 hrs [primary bottleneck — up to 20 perturbation positions × 5K examples × forward passes]; NLDD on 7B/14B models: 100 hrs; MCT geometric validation: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic simulation: 50 hrs [mostly CPU, some GPU for validation])', 'timeline': '15-17 weeks (2 researchers: 4 weeks Phase 0a+0b characterization + pilot; 5 weeks Phase 1 full ICG; 4 weeks Phases 2-3 in parallel with NLDD; 2-3 weeks writing + ablations)', 'estimated_gpu_cost': '$2,500 at ~$3/H100-hour (cloud spot pricing)', 'storage': '3-5 TB (4 layers per model, fp16); reducible to ~1.5 TB via PCA'}, 'human_in_loop': {'gpu_hours': '~830 H100-hours', 'timeline': '13 weeks (1 researcher + Claude for experiment design and analysis)', 'claude_api_cost': '$350', 'estimated_gpu_cost': '$2,500'}, 'auto_research': {'gpu_hours': '~830 H100-hours', 'timeline': '11 weeks', 'claude_api_cost': '$700', 'estimated_gpu_cost': '$2,500', 'speed_bottleneck': 'NLDD on 32B (~250 H100-hours, ~30% of total compute) is the primary bottleneck. Each NLDD evaluation requires corrupting reasoning at multiple positions and measuring logit degradation — O(T × N) forward passes where T≈20 perturbation positions and N≈5K examples. For 32B models, this cannot be easily parallelized beyond 8-GPU data parallelism. Secondary: 671B subset (8×H100, ~50 hrs); MCT geometric validation (~50 hrs). Phase 0b pilot (30 hrs) provides early go/no-go signal before committing full Phase 1-3 compute.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s finding that answer-content probe steering fails on reasoning models despite high accuracy; (b) Yuan et al.'s systematic demonstration that four interventions all fail on correctness probes, establishing 'diagnostic not causal'; (c) the temporal probe dynamics now empirically characterized by David (0.84 AUC at t=4, stable ~0.8), Zhang et al. (chunk-level rising trajectory), Esakkiraja et al. (pre-generation >90% with dip-recovery), and Chrabąszcz et al. (60+ trajectory features capturing dynamics invisible to static probes, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection protocol demonstrating monotonic behavioral C(t) curves with rigorous controls (sequential content +18.1-33.1% vs. shuffled +0.3-10.8%) — all pointing to the same insight: the gap between diagnostic information availability and causal contribution IS the phenomenon of interest. Additionally inspired by: Wang's (2604.15726) formalization of H1/H2/H0 hypotheses providing the theoretical scaffold for what our framework empirically measures; Gjølbye et al.'s (2605.15454) finding that difficulty-geometry coupling is domain-specific and requires length correction; Herrmann et al.'s concurrent temporal persona-vector dynamics; and the trajectory-shape literature showing shapes can distinguish phenomena regardless of absolute-value calibration.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)\n- ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces in Large Language Models (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent, Not the Chain of Thought (Wang, arXiv 2604.15726)\n- Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- Can Aha Moments Be Fake? True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Do LLMs Experience an Internal Polylogue? (Herrmann et al., arXiv 2605.09159)\n- LLMs Faithfully and Iteratively Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- When Chains of Thought Don't Matter: Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- Spatiotemporal Hidden-State Dynamics / StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Mapping Faithful Reasoning / Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- Emergent Manifold Separability / MCT (Chun et al., arXiv 2602.20338)\n- Tracing the Traces: Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940)\n- Is My Model Mind Blurting? RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability via Information Theory (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics with MI (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination via Transport Geometry (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE: Perfect Linear Concept Erasure (Belrose et al., NeurIPS 2023, arXiv 2306.03819)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:29:38.776Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:29:38.776Z",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:29:38.788Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have enough information to make my assessment. Let me note a critical issue I've identified — this proposal targets **CoRL 2026** (Conference on Robot Learning), but the proposal is entirely about CoT faithfulness in language models with zero robotics content. Let me verify the target venues listed in the proposal itself.

Looking at the proposal again, I see the **Target Venues** listed are actually **ICLR 2027** and **ICML 2027**, not CoRL. However, the user's task says to evaluate for "CoRL 2026 主会". This is a critical mismatch. Let me proceed with the evaluation, addressing this venue mismatch.

Now let me compile my full triage evaluation:

---

```
【阶段】: Triage

【领域调研】:

1. [Yuan et al., arXiv 2605.09502] (May 2026): "Hidden Error Awareness: The Signal Is Diagnostic, Not Causal" — 核心动机论文之一。确认存在，描述准确。证明 linear probe 可达 0.95 AUROC 检测错误，但四种 causal intervention 均失败。这是本 proposal 的核心前提。

2. [Chrabąszcz et al., arXiv 2605.18549] (May 2026): "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" — 最直接的竞争工作。确认存在，描述准确。提出 probe trajectory + 60+ signal-processing features，max-pooling 达 91-97% AUROC。关键：该工作只有 probe 侧，没有 causal contribution 维度。Proposal 对差异化的描述基本准确。

3. [Cox et al., arXiv 2603.01437] (Mar 2026): "Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering" — 确认存在。证明 instruction-tuned models 上 steering 有效（>50% flip），但 reasoning model 上失败。Proposal 引用准确。

4. [Wang, arXiv 2604.15726] (Apr 2026): "LLM Reasoning Is Latent, Not the Chain of Thought" — 确认存在。提出 H1/H2/H0 三假说框架。Proposal 声称 ICG 可 operationalize 这个区分，引用准确。

5. [Ballon et al., arXiv 2601.23163] (Jan 2026): "Probing the Trajectories of Reasoning Traces in LLMs" — 确认存在。truncation-reinjection protocol。Proposal 将其作为 C(t) estimator 的基础，引用准确。

6. [Gjølbye et al., arXiv 2605.15454] (May 2026): "Reasoning Models Don't Just Think Longer, They Move Differently" — 确认存在。difficulty-geometry coupling，length correction 方法。Proposal 引用准确。

7. CoRL 2026 Call for Papers: CoRL 是 Conference on Robot Learning，要求 submissions 聚焦 core robotics problem，鼓励 real-robot experiments 或 sim-to-real evidence。**本 proposal 与 robotics 完全无关。**

- 调研总结: CoT faithfulness 是 2025-2026 年的高热领域，大量独立工作从 probing、causal intervention、temporal dynamics 等角度切入，产出密集。Proposal 引用的关键论文均真实存在且描述准确。Proposal 试图做的"将 probe trajectory 与 causal contribution 联合追踪"确实是现有工作的空白（Chrabąszcz 只有 probe 侧，Ballon 只有 behavioral 侧），但这个空白更像是自然的 engineering integration，而非概念上的突破。**最严重的问题是：proposal 的 target venue 与内容完全不匹配——CoRL 是 robotics 会议，而本 proposal 是纯 NLP/interpretability 工作。**


【Trivial Alternative 检验】:

存在显著的 trivial alternative 威胁：

1. **直接拼接现有工具**: Chrabąszcz et al. 的 probe trajectory + Ballon et al. 的 truncation-reinjection protocol，不加任何新框架，直接在同一 model/dataset 上跑两个管线然后对比，就能产出类似的 "information vs. contribution" 对比。ICG 框架的增量价值主要在于 (a) null-probe calibration, (b) G*(t) 这个 formalization, (c) phenomenon taxonomy。其中 null-probe calibration 是 Hewitt & Liang 2019 的标准技术；G*(t) 的 formalization 虽然整洁，但本质上就是 "probe accuracy 减去 causal contribution" 的减法；phenomenon taxonomy 是否真能 work 取决于 Phase 0b 的实验结果。

2. **Phenomenon classification 的可行性存疑**: Proposal 自己承认 phenomenon signature 是 "predictions"，依赖 Phase 0b pilot 验证。如果 d < 0.3，就 downscope 为 "characterization paper"。一个 characterization paper 的核心贡献就变成了 "我们在同一个 model 上同时跑了 probe 和 truncation ablation，发现 gap 存在"——这接近 trivial integration。

增量价值在于：如果 phenomenon classification 确实 work（d > 0.5），且 difficulty conditioning 揭示了有实践意义的 decorative→load-bearing 转换点，那框架就有超越 trivial integration 的价值。但这是一个 conditional novelty——novelty 依赖于实验结果。


【前提假设检验】:

核心 claim 的逻辑链条中有多个未经验证的假设：

1. **"Probe accuracy 减去 causal contribution = faithfulness signal" 的假设**: 这是整个框架的核心等式 G*(t) = P*(t) − C(t)。但 P*(t) 测量的是 "hidden state 中是否编码了 correctness awareness"，C(t) 测量的是 "CoT prefix 对最终答案的因果贡献"。这两个量的度量尺度不同（一个是 AUROC，一个是 accuracy change），直接相减的语义不清晰。Proposal 没有严格论证为什么这个差值是 faithfulness 的有效操作化定义，而不仅仅是两个不同测量的 arbitrary 组合。

2. **"不同 faithfulness phenomena 会产生可区分的 G*(t) trajectory shapes" 的假设**: 这是 phenomenon classification 的基础。Proposal 的 signature predictions（如 pre-CoT encoding → 大常数 gap，genuine reasoning → 收敛到零）看起来合理，但它们是从不同 study、不同 model、不同 dataset 的结果拼接推导出来的。在同一 model 同一 dataset 上，这些 pattern 是否可分离是完全未知的。Proposal 诚实地承认了这一点并设计了 Phase 0b pilot，这是好的，但也意味着核心 novelty claim 在实验前是悬空的。

3. **"Null-probe calibration 能有效去除 correlative inflation" 的假设**: Hewitt & Liang 的 selectivity 方法是对 MLP probe 设计的，对 linear probe 的适用性更直接，但 "shuffled labels" 的 null probe 是否能捕捉到 Chun et al. 发现的 non-uniform 几何 inflation 是另一个问题。Proposal 加入了 MCT 验证，但 MCT 本身在这个 context 中是否是有效的校准工具也需要实验验证。

4. **"三种 C(t) estimators 可以提供 convergent evidence" 的假设**: prefix truncation、paraphrase perturbation、NLDD 测量的是不同的 causal 概念。prefix truncation 测的是 "reasoning trace 到这个位置为止的整体贡献"，NLDD 测的是 "特定位置的局部影响"，paraphrase perturbation 测的是 "语义内容 vs. 表面形式"。它们是否收敛以及不收敛时如何解释，proposal 没有清晰回答。


【3 维度打分】:

1. Novelty: 【中】— 
   Proposal 的核心创新是将 probe trajectory (à la Chrabąszcz et al. 2605.18549) 和 causal contribution trajectory (à la Ballon et al. 2601.23163) 联合追踪，形成 G*(t) gap metric。这个组合确实是文献空白——Chrabąszcz 只有 probe 侧，Ballon 只有 behavioral 侧，没有人同时做过两侧并 formalize gap。但这个 novelty 更接近 "integration novelty" 而非 "conceptual novelty"。G*(t) = P*(t) − C(t) 的 formalization 虽然整洁，但概念上就是 "同时测量两个已知量然后做减法"。Null-probe calibration 是 2019 年的标准技术。Phenomenon taxonomy 的 novelty 取决于实验结果（是否真的可分离）。
   
   相比之下，Yuan et al. (2605.09502) 的 novelty 在于发现一个 surprising empirical fact（四种 intervention 全部失败），Wang (2604.15726) 的 novelty 在于概念框架的重新构造。本 proposal 的 novelty 层次更接近 "measurement framework" 而非 "discovery" 或 "reconceptualization"。

2. Significance: 【中偏强】— 
   CoT faithfulness 是当前 LLM safety 和 interpretability 的核心问题，research question 的重要性毋庸置疑。"模型知道但不使用" 这个现象的系统性表征确实有价值。如果 difficulty conditioning 能揭示 "CoT 在什么时候从装饰性变为功能性"，这对实践有指导意义。但 significance 受限于两点：(a) 这是一个 diagnostic/measurement 贡献，不提供 actionable improvement；(b) 结果的 generalizability 受限于所测试的 model 和 benchmark 的范围。

   **然而，最致命的 significance 问题是 venue mismatch**: CoRL 是 Conference on Robot Learning，要求 submissions 聚焦 robotics 问题并展示 real-robot 或 sim-to-real evidence。本 proposal 是纯 NLP/interpretability 工作，与 robotics 零相关。即使 idea 质量再高，投 CoRL 的中稿概率接近零，除非做根本性的方向调整（如将 framework 应用于 robot reasoning/planning 中的 CoT faithfulness）。Proposal 自身的 target venues 也写的是 ICLR 2027 和 ICML 2027，不是 CoRL。

3. Related Work: 【强】— 
   这是 proposal 最突出的优点。文献覆盖极其全面，引用了 40+ 篇高度相关的近期工作，且对每篇工作的描述经核实基本准确。与最直接竞争工作 (Chrabąszcz et al.) 的差异化定位清晰——明确指出自己多出的维度（causal contribution, gap metric, calibration, phenomenon taxonomy）。对 probe calibration 文献（Hewitt & Liang, Voita & Titov, Chun et al.）的引用表明作者对方法论风险有清醒认识。唯一的小缺陷是引用数量过多可能导致在正式论文中难以充分讨论每一篇。


【概率估计】: [2% - 8%] 中位 3%

【估计理由】: 
这个极低的概率估计主要由一个**致命的 venue mismatch** 驱动：CoRL 是 Conference on Robot Learning，而本 proposal 是纯 NLP/interpretability 研究，与 robotics 完全无关。CoRL 的 CFP 明确要求 "submissions should focus on a core robotics problem" 并 "demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics"。无论 idea 质量如何，desk reject 的风险极高。

如果忽略 venue mismatch，仅评估 idea 在 NLP/ML 顶会（如 ICLR 2027, 其自身 target venue）的潜力，我的估计会是 [25% - 38%] 中位 30%。理由：idea 方向正确，research question 重要，literature 覆盖出色，但 novelty 偏向 integration/measurement 而非 discovery，核心 claim（phenomenon classification via trajectory shapes）依赖实验结果验证，且存在 trivial alternative 威胁（直接拼接现有工具）。审稿人看到 G*(t) = P*(t) − C(t) 时，可能会说 "this is a natural combination, I would have expected someone to do this"——属于 "I would have guessed this" 区间，对应 25-35%。Phase 0b 的 honest scoping 和 extensive robustness plan 提高了下限但不提高上限。

【主要风险】:
1. **致命 venue mismatch**: CoRL 是 robotics 会议，本 proposal 与 robotics 零相关，大概率 desk reject。
2. **Conditional novelty**: 框架的核心卖点（phenomenon classification via G*(t) trajectory shapes）的 novelty 取决于 Phase 0b 的实验结果。如果 phenomena 不可分离，剩余的 "characterization paper" 贡献度接近 trivial integration，novelty 降至 "弱"。
```

---

**补充说明给后续流程**：

本 proposal 存在一个需要立即确认的根本性问题——**投稿目标是 CoRL 2026（robotics 会议）还是 ICLR/ICML 2027（ML 顶会）？** Proposal 自身写的 target venues 是 ICLR 2027 和 ICML 2027，而任务要求评估 CoRL 2026 中稿概率。如果确实要投 CoRL，需要从根本上重新定位 proposal（例如将 CoT faithfulness framework 应用于 embodied reasoning / robot planning），否则中稿概率近乎为零。如果 target 实际是 ICLR/ICML，那 idea 质量属于中等偏上水平（~30%），值得进入后续迭代流程。

Sources:
- [Yuan et al. - Hidden Error Awareness](https://arxiv.org/abs/2605.09502)
- [Chrabąszcz et al. - Probe Trajectories](https://arxiv.org/abs/2605.18549)
- [Cox et al. - Pre-CoT Probes](https://arxiv.org/abs/2603.01437)
- [Wang - LLM Reasoning Is Latent](https://arxiv.org/abs/2604.15726)
- [Ballon et al. - Reasoning Trace Trajectories](https://arxiv.org/abs/2601.23163)
- [Gjølbye et al. - Reasoning Models Move Differently](https://arxiv.org/abs/2605.15454)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [FaithCoT-Bench (ICLR 2026)](https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf)
- [Ye et al. - Faithfulness Decay / NLDD](https://arxiv.org/html/2602.11201v1)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information. Let me compile my evaluation.

---

```
【阶段】: Triage

【⚠️ 致命性前置问题：venue 完全不匹配】

本 proposal 投稿目标为 **CoRL 2026（Conference on Robot Learning）**。
然而，CoRL 的 Call for Papers 明确要求："Submissions should focus on a core robotics problem 
and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to 
robotics. Submissions without a robotics focus will be returned without review."

本 proposal 的内容是 **LLM chain-of-thought faithfulness 的可解释性度量框架**——
纯粹的 NLP/ML interpretability 研究，没有任何机器人学习相关内容（无 embodiment、
无 manipulation、无 navigation、无 sim-to-real、无 robot policy learning）。
这篇论文会在 CoRL 被 **desk reject without review**。

proposal 自身列出的 target venues 是 ICLR 2027 和 ICML 2027，
这与用户指定的 CoRL 2026 完全矛盾。

➡️ **对 CoRL 2026 的中稿概率：0-2%（会被 desk reject）。**

以下评估将基于 idea 本身的质量，假设投稿到合理的 venue（如 ICLR/ICML/NeurIPS），
供后续流程参考。


【领域调研】:

- [Yuan et al. "Hidden Error Awareness" arXiv 2605.09502] (2026): 
  最直接的前置工作。系统证明 4 种 causal intervention（activation steering, 
  probe-guided best-of-N, self-correction, activation patching）在 reasoning models 
  上全部失败，确立 "diagnostic not causal" 发现。本 proposal 的核心动机直接来源于此。
  
- [Cox et al. "Pre-CoT Probes" arXiv 2603.01437] (2026): 
  在 instruction-tuned models 上 probe steering 可实现 >50% flip rate，
  但在 reasoning model (GPT-OSS-20B) 上 flip rate "negligible against orthogonal 
  baseline"。本 proposal 的另一核心动机来源。
  
- [Chrabąszcz et al. "Probe Trajectories" arXiv 2605.18549] (2026.05): 
  最接近的并发工作。已经做了 probe trajectory 的全时程追踪，提取 60+ 
  signal-processing features，在 4 个 reasoning models 上达到 91-97% AUROC。
  与本 proposal 的 P*(t) 方向高度重叠，但缺少 causal contribution 维度。
  
- [Ballon et al. "Truncation-Reinjection" arXiv 2601.23163] (2026.01): 
  已经做了 behavioral C(t) curves，在 decile intervals 上测量 truncated CoT 
  的 causal contribution。与本 proposal 的 C(t) 方向高度重叠。

- [Wang "LLM Reasoning Is Latent" arXiv 2604.15726] (2026.04): 
  形式化了 H1(latent-mediated)/H2(CoT-mediated)/H0(serial compute) 三假说。
  本 proposal 的 G*(t) 本质上是 Wang 框架的一个经验化实现。

- [CMI framework / Sathyanarayanan et al. arXiv 2602.03994] (2026.02): 
  已结合 probing 与 causal intervention（activation patching），引入 CoT 
  Mediation Index，在 StrategyQA/TruthfulQA/GSM8K 上发现 "bypass regimes"。
  
- [Gjølbye et al. arXiv 2605.15454] (2026.05):
  hidden-state trajectory geometry + difficulty conditioning + length correction，
  在 11 models 上证明 difficulty-geometry coupling 是 domain-specific 的。
  
- [Project Ariadne arXiv 2601.02314] (2026.01):
  用 SCM + counterfactual logic 审计 agentic CoT faithfulness，发现 
  "Faithfulness Gap" 和 "Causal Decoupling" 作为 failure mode。

- 调研总结: CoT faithfulness 是 2025-2026 年最拥挤的研究方向之一，
  已有 30+ 篇高质量论文从不同角度攻克。probe trajectory（Chrabąszcz et al.）
  和 behavioral causal curves（Ballon et al.）已分别被独立完成；
  probe + causal intervention 的结合也已被 CMI framework 和 Kudo et al. (EACL 2026) 
  覆盖。本 proposal 的核心位置是"将已有的 P(t) 和 C(t) 测量做差形成 G*(t) 
  gap metric"——这是一个 synthesis/unification framework，而非全新的发现。


【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁。**

G*(t) = P*(t) − C(t) 的核心操作是：取 Chrabąszcz et al. 风格的 probe trajectory，
取 Ballon et al. 风格的 truncation-reinjection causal curve，然后做差。
一个更简单的替代方案是：
1. 直接在同一模型/数据集上分别复现 probe trajectory 和 truncation curves
2. 将两条曲线并排展示，用简单的 correlation/divergence 统计量描述其差异
3. 按 difficulty conditioning 做分组分析

这不需要提出一个全新的 "ICG framework"，不需要 null-probe calibration 的复杂
machinery，不需要 phenomenon taxonomy 的分类体系。proposal 的增量价值在于：
(a) null-probe calibration 作为方法论贡献（有价值但较小）；
(b) 将 gap 映射到 named phenomena 的 taxonomy（目前完全未验证）；
(c) TIF score 作为 instance-level diagnostic（需要验证实用性）。

增量价值存在，但需要诚实地承认核心操作的简单性。


【前提假设检验】:

核心 claim 的逻辑链中有 **3 个关键未验证假设**：

1. **P*(t) 和 C(t) 的可减性假设**：P*(t) 是 AUROC（0-1 范围的分类性能），
   C(t) 是 behavioral accuracy change under truncation（一个因果效应量）。
   这两个量在量纲和语义上不直接可减。G*(t) = P*(t) − C(t) 的物理意义
   取决于两者如何被归一化到可比较的尺度——proposal 对此没有充分论证。
   "correctness awareness the model has but doesn't channel through its CoT" 
   这个解释是直觉上 appealing 但数学上 hand-wavy 的。

2. **Trajectory shape → phenomenon type 的映射假设**：proposal 假设不同 
   faithfulness phenomena（pre-CoT encoding, genuine reasoning, post-hoc 
   rationalization）会产生可区分的 G*(t) trajectory shapes。这是整个 
   classification pipeline 的核心前提，但目前完全基于"从不同论文拼接的 
   cross-study measurements"的推测。proposal 本身也承认这一点并设计了 
   Phase 0b pilot，但如果 Phase 0b 失败（d < 0.3），整个框架的分类功能就不成立。

3. **Null-probe calibration 能有效去除 correlative inflation**：Hewitt & Liang 
   的 selectivity 方法和 shuffled-label baseline 能去除 uniform inflation，
   但 Chun et al. (2602.20338) 的 MCT 发现表明 inflation 是 non-uniform 
   且 temporally varying 的。P*(t) = P(t) − P_null(t) 是否足够处理 
   non-uniform inflation 是一个开放问题。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是将两个已存在的测量维度（probe trajectories à la Chrabąszcz et al., 
   causal contribution curves à la Ballon et al.）做差形成 gap metric。
   这是一个 natural combination，而非 surprising insight。
   CMI framework (2602.03994) 已结合 probing 与 causal intervention；
   Wang (2604.15726) 已形式化了 H1/H2 框架；Chrabąszcz et al. (2605.18549) 
   已做了 probe trajectories；Ballon et al. (2601.23163) 已做了 behavioral C(t)。
   本 proposal 的 novelty delta 在于：(a) 显式的 gap metric 定义，(b) null-probe 
   calibration，(c) phenomenon taxonomy via trajectory shapes——
   其中 (a) 是 straightforward，(b) 是方法论细节，(c) 是未验证的假设。
   剔除 surface differences 后，真正新颖的部分不多。

2. **Significance: 中** — 
   研究问题本身（CoT faithfulness）无疑是重要的，是当前 LLM safety/alignment 
   的核心议题。但三个因素限制了 significance：
   (a) 领域极度拥挤（30+ 篇 2025-2026 论文），一个新框架的边际贡献受到稀释；
   (b) 即使成功度量了 G*(t)，practical implication 不清晰——
   你知道了 CoT 是 unfaithful 的，然后呢？proposal 未提出如何利用 G*(t) 
   改善 faithfulness 或指导 training；
   (c) 如果核心发现是 positive（不同 phenomena 确实有不同 trajectory shapes），
   多数审稿人会说 "I would have guessed this"——这符合直觉而非 surprising。
   如果 negative（trajectory shapes 不可区分），则退化为 characterization paper，
   贡献更有限。

3. **Related Work: 强** — 
   Related work 覆盖极其详尽，引用了 40+ 篇相关论文，包括最新的 2026 年 5 月
   工作（Chrabąszcz et al., Gjølbye et al., Yuan et al.）。对每篇工作的定位
   和差异化描述准确。proposal 对 Chrabąszcz et al. 作为 "closest concurrent work" 
   的分析尤为到位。唯一的风险是：如此详尽的 related work 反而暴露了 novelty 
   的有限性——proposal 本质上是在已有工作的 "缝隙" 中填补一个 natural combination。


【概率估计】: [18% - 28%] 中位 22%
（注：此概率针对合理 venue 如 ICLR/ICML/NeurIPS。对 CoRL 2026: 0-2%，desk reject。）

【估计理由】: 
idea 方向站得住脚——CoT faithfulness 是重要问题，probe + causal 的 temporal gap 
是一个 logical next step。但 novelty delta 有限（essentially combining two existing 
measurement traditions with a subtraction），且核心发现无论 positive 还是 negative 
都缺乏 surprise factor。significance 受到领域拥挤度的稀释和 practical implication 
缺失的限制。Related work 覆盖是 proposal 的亮点，但无法弥补 idea 内核的薄弱。
形式上非常完善（dual-outcome, Phase 0b pilot, honest scoping），但形式完善度 ≠ 
idea 质量。上界主要被 Novelty（弱-中）限制——如果审稿人问 "what's the surprising 
finding here that I couldn't have predicted?"，proposal 难以给出有力回答。

【主要风险】: 
1. **Novelty 不足被挑战**：审稿人可能认为 G*(t) = P*(t) − C(t) 是 Chrabąszcz et al. 
   + Ballon et al. 的 trivial combination，核心 "insight"（gap IS the faithfulness 
   signal）是 obvious reframing of Yuan et al.'s finding，不构成独立贡献。
2. **量纲不可比性**：P*(t)（AUROC）和 C(t)（behavioral accuracy delta）的直接相减
   在数学上缺乏严格支撑，审稿人可能质疑 G*(t) 的物理意义和可解释性，
   导致整个框架的理论基础被动摇。
```

**补充说明**：

关于 **CoRL 2026 作为投稿目标的致命问题**：proposal 自身列出的 target venues 是 ICLR 2027（primary）和 ICML 2027（fallback），这两个都是合理选择。但如果真的要投 CoRL 2026，这篇论文会因为完全不涉及 robotics 而被 desk reject。建议确认投稿目标是否为 ICLR 2027 而非 CoRL 2026——如果确实是 ICLR 2027，上述 idea 质量评估（中位 22%）是有参考价值的。

Sources:
- [Yuan et al. "Hidden Error Awareness" arXiv 2605.09502](https://arxiv.org/abs/2605.09502)
- [Cox et al. "Pre-CoT Probes" arXiv 2603.01437](https://arxiv.org/abs/2603.01437)
- [Chrabąszcz et al. "Probe Trajectories" arXiv 2605.18549](https://arxiv.org/abs/2605.18549)
- [Ballon et al. "Truncation-Reinjection" arXiv 2601.23163](https://arxiv.org/abs/2601.23163)
- [Wang "LLM Reasoning Is Latent" arXiv 2604.15726](https://arxiv.org/abs/2604.15726)
- [CMI framework arXiv 2602.03994](https://arxiv.org/abs/2602.03994)
- [Gjølbye et al. arXiv 2605.15454](https://arxiv.org/abs/2605.15454)
- [Project Ariadne arXiv 2601.02314](https://arxiv.org/abs/2601.02314)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [FaithCoT-Bench ICLR 2026](https://arxiv.org/abs/2510.04040)
- [Young "Measuring Faithfulness" arXiv 2603.20172](https://arxiv.org/abs/2603.20172)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【⚠️ 致命问题：投稿目标与会议 scope 完全不匹配】

本 proposal 是一篇纯 NLP/LLM interpretability 论文，研究链式推理（Chain-of-Thought）的忠实性诊断。
CoRL（Conference on Robot Learning）2026 是一个机器人学习会议，其 Call for Papers 明确列出的 topic 包括：
• 机器人感知与控制的表征学习
• 模仿学习、强化学习用于物理机器人控制
• 机器人操作、导航、运动、驾驶、飞行
• 机器人安全与对齐
• 人机交互与自然语言机器人指令

本 proposal 不包含任何机器人相关内容——没有机器人系统、没有物理交互、没有 sim-to-real、没有 embodied agent。Proposal 自身的 "Target Venues" 也写的是 ICLR 2027 和 ICML 2027，而非 CoRL。

→ 投稿 CoRL 2026 的中稿概率本质上为 0%，几乎确定会被 desk reject。

以下评估仍按标准 rubric 对 idea 质量进行客观打分（可为后续投稿 ICLR/ICML 提供参考），但概率估计将基于 CoRL 这个具体目标会议。


【领域调研】:
- [Chrabąszcz et al., arXiv 2605.18549] (2026): "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"。最直接的竞争工作。在 Llama-8B-R1-Distill 和 Qwen3-4B/8B/14B 上追踪每个 token 位置的 probe 轨迹，提取 60+ 信号处理特征（volatility、trend、steady-state、autocorrelation 等），max-pooling 达到 91-97% AUROC，比 static probe 提升最高 17pp。但缺少 causal contribution 维度和 gap metric。本 proposal 的 P*(t) 部分与此高度重叠。

- [Yuan et al., arXiv 2605.09502] (2026): "Hidden Error Awareness: The Signal Is Diagnostic, Not Causal"。确立了 "diagnostic-not-causal" 这一核心发现——linear probe 在首步即达 0.79 AUROC、整体 0.95 AUROC，但四种干预策略（activation steering、probe-guided best-of-N、self-correction、activation patching）全部失败。这是本 proposal 整个 framework 的 motivating observation，但也意味着核心 insight 已经被他人报告。

- [Cox et al., arXiv 2603.01437] (2026): "Decoding Answers Before Chain-of-Thought"。在 instruction-tuned 模型上 probe AUC > 0.9，steering flip rate > 50%；但在 reasoning model (GPT-OSS-20B) 上 flip rate "negligible"。独立确认了 diagnostic-causal gap。

- [Ballon et al., arXiv 2601.23163] (2026): "Probing the Trajectories of Reasoning Traces"。提供 truncation-reinjection 协议：在 decile interval 截断 CoT 后重新注入，测量准确率单调上升。三种 control condition（random tokens、swapped traces、shuffled tokens）验证 sequential content 是关键因素。这正是本 proposal C(t) 的主要方法之一，方法论层面已被前人建立。

- [Wang, arXiv 2604.15726] (2026): "LLM Reasoning Is Latent, Not the Chain of Thought"。提出 H1（latent-mediated）/ H2（CoT-mediated）/ H0（serial compute）三假设框架。本 proposal 声称 G*(t) 可 operationalize H1/H2 区分——但这一理论映射较为表面（G*(t) >> 0 → H1, G*(t) ≈ 0 → H2），并非严格的因果推断。

- [Gjølbye et al., arXiv 2605.15454] (2026): "Reasoning Models Don't Just Think Longer, They Move Differently"。研究 hidden-state trajectory geometry 与 difficulty 的耦合关系，发现 length correction 后 difficulty 仍与 trajectory 几何系统性相关（ρ⊥ = +0.41 on Codeforces），但 domain-specific。本 proposal 的 difficulty conditioning 思路与此高度一致。

- [FaithCoT-Bench, ICLR 2026]: 首个 instance-level CoT unfaithfulness benchmark，1000+ trajectories，细粒度标注。提供了 ground-truth 标准，本 proposal 的 TIF score 需要与之对标。

- 调研总结：CoT faithfulness 是 2025-2026 年的热点方向，已经出现了大量高质量工作分别覆盖了 (1) probe 时序动态、(2) causal intervention 失败、(3) 截断-重注入行为测试、(4) difficulty conditioning。本 proposal 的核心定位是"将已有的 probe 端（P*(t)）和 causal 端（C(t)）组合起来计算差值 G*(t)"——这是一个 synthesis/integration 型贡献，而非根本性新洞见。各组成部分的方法论均已由他人建立。


【Trivial Alternative 检验】:
存在明显的更简单替代方案。

(1) 最简单的版本：直接比较 probe accuracy（来自 Yuan et al. / David / Zhang et al. 的现成数据）和 behavioral accuracy gain（来自 Ballon et al. 的截断曲线），画在同一张图上即可观察到所谓的 "information-contribution gap"。不需要定义新 metric、不需要 null-probe calibration、不需要 phenomenon classification pipeline。这个简单对比已经足以传达核心 message "models know more than their CoT uses"，而这一 message 已被 Yuan et al. 和 Cox et al. 直接报告。

(2) 对于 phenomenon classification：简单地按 P*(0) 的高低（pre-CoT encoding vs. not）和 behavioral accuracy gain 的斜率（genuine reasoning vs. rationalization）做 2D 分桶，可能就能区分 2-3 种现象。是否需要完整的 G*(t) temporal fingerprint + 60+ signal features + DTW 分类？这一复杂度的增量价值尚不明确。

增量价值：proposal 的增量主要在 (a) null-probe calibration 提供更干净的信号，(b) temporal resolution 提供更细粒度的分析，(c) multi-method C(t) 提供鲁棒性。这些是 methodological polish，不是 conceptual breakthrough。


【前提假设检验】:
核心逻辑链中有两个关键的未验证假设：

(1) **"不同 faithfulness phenomena 会产生可区分的 G*(t) temporal signature"——这是整篇论文的核心赌注，且目前完全未经验证。** Proposal 的 phenomenon predictions（pre-CoT encoding → constant high gap; genuine reasoning → converging gap; rationalization → widening gap）是从不同论文、不同模型、不同数据集的结果 "组装" 出来的理论预测。Phase 0b pilot 正是为了验证这一点，但 proposal 自己也承认 "cross-study heterogeneity may overestimate separability"。如果同一模型同一数据集上的 G*(t) 曲线没有清晰的形状差异（d < 0.3），则核心 contribution 崩塌。

(2) **P*(t) 和 C(t) 是否在数学上可减（commensurable）。** P*(t) 是 probe AUROC（一个分类性能度量），C(t) 是 behavioral accuracy change（一个因果效应度量）。这两个量的量纲和尺度完全不同。直接做减法 G*(t) = P*(t) − C(t) 的物理意义不明确——AUROC 0.8 减去 accuracy gain 0.3 等于 0.5，这个 0.5 代表什么？Proposal 没有讨论这一 commensurability 问题。


【3 维度打分】:
  1. Novelty: 弱 — 核心 idea 是 "将 probe 时序曲线和 causal contribution 时序曲线放在一起做差值"。两端的方法论分别由 Chrabąszcz et al. (probe trajectories)、Ballon et al. (truncation-reinjection C(t)) 建立；"diagnostic-not-causal" gap 已由 Yuan et al. 和 Cox et al. 直接报告。Proposal 的增量是 combination + calibration + phenomenon classification——这是 methodological integration，而非 conceptual novelty。即使 phenomenon classification 成功，预测的 signatures 大多是 "从定义中可推导出来的"（e.g., pre-CoT encoding 当然 P*(0) 高且 C(t) 低），审稿人更可能评价 "I would have guessed this" 而非 "surprising"。与 Chrabąszcz et al. 的差异化主要在于加入了 C(t) 维度，但 C(t) 的方法论也来自 Ballon et al.。

  2. Significance: 中 — CoT faithfulness 是一个重要的研究方向，理解 "models know but don't use" 对 alignment 和安全有实际意义。如果 temporal fingerprint classification 能够工作，提供 instance-level 诊断工具有实用价值。但 (a) 这是一篇纯 diagnostic/measurement 论文，不提供解决方案；(b) practical impact 有限——得到 TIF score 后能做什么？(c) 如果 phenomenon classification 失败（Phase 0b d < 0.3），退化为 "gap exists and varies with difficulty" 的 characterization paper，贡献进一步缩水。对于 ICLR/ICML 属中等重要性；对于 CoRL 完全不相关。

  3. Related Work: 强 — 这是本 proposal 最突出的优点。对近期文献的覆盖非常全面（30+ 篇），对 Chrabąszcz et al.、Yuan et al.、Cox et al.、Ballon et al. 等最直接竞争/互补工作的定位清晰，差异化描述诚实（不过分夸大自己的 novelty）。引用的论文经调研验证确实存在且描述准确。文献综合水平高于多数 proposal。


【概率估计】: [0% - 2%] 中位 0%
【估计理由】: 
这个概率估计基于目标会议 CoRL 2026。CoRL 是 Conference on Robot Learning，其 scope 严格限定在机器人学习交叉领域（机器人感知、控制、操作、导航、模仿学习、强化学习用于物理机器人等）。本 proposal 是一篇纯 NLP/LLM interpretability 论文，研究 Chain-of-Thought 推理的忠实性度量，不包含任何机器人相关内容。这是一个根本性的 venue mismatch，几乎确定会被 desk reject。Proposal 自身列出的 Target Venues 也是 ICLR 2027 和 ICML 2027，进一步确认了这不是为 CoRL 准备的工作。

如果改投 ICLR 2027（proposal 自己的首选目标），仅基于 idea 质量我估计概率约为 20-30%（中位 ~25%）。理由：idea 方向正确（CoT faithfulness 是热点），文献覆盖出色，但核心 novelty 是 synthesis/integration 型，各组成部分已有前人工作；核心 phenomenon classification 是未验证的赌注；核心 metric G*(t) 的 commensurability 存疑；predicted temporal signatures 偏 "obvious from definitions"。Novelty 弱这一维度是限制上界的关键因素。

【主要风险】: 
1. **致命：venue mismatch。** CoRL 2026 不接受纯 NLP interpretability 工作，投稿等同于浪费一次提交机会。
2. **Idea 层面（针对 ICLR/ICML 投稿）：novelty 是 integration 型而非 conceptual 型。** 审稿人很可能认为 "just putting Chrabąszcz's P(t) and Ballon's C(t) together and subtracting" 不构成足够的 novelty delta，尤其当 "diagnostic-not-causal gap" 这一 core message 已被 Yuan et al. 直接报告的情况下。
```

**补充建议**：如果团队希望推进这个 idea，强烈建议：
1. **立即更换目标会议**为 ICLR 2027 或 ICML 2027（与 proposal 自身的 Target Venues 一致）；
2. 认真解决 G*(t) = P*(t) − C(t) 的 commensurability 问题——两个量纲不同的量做减法需要严格的归一化论证；
3. 尽早执行 Phase 0b pilot——如果 phenomenon separability 不成立，需要及时调整论文定位。

Sources:
- [Chrabąszcz et al. - Monitoring the Internal Monologue](https://arxiv.org/abs/2605.18549)
- [Yuan et al. - Hidden Error Awareness](https://arxiv.org/abs/2605.09502)
- [Cox et al. - Decoding Answers Before Chain-of-Thought](https://arxiv.org/abs/2603.01437)
- [Ballon et al. - Probing the Trajectories of Reasoning Traces](https://arxiv.org/abs/2601.23163)
- [Wang - LLM Reasoning Is Latent](https://arxiv.org/abs/2604.15726)
- [Gjølbye et al. - Reasoning Models Move Differently](https://arxiv.org/abs/2605.15454)
- [FaithCoT-Bench (ICLR 2026)](https://openreview.net/forum?id=lN3yKqqzF1)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness

## Description
We propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.

The framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness (explicitly targeting right/wrong prediction — justified over answer-content probes by broader applicability beyond binary tasks, grounding in the diagnostic-not-causal finding which is about correctness, and more direct faithfulness interpretation — with supplementary answer-content analysis on binary/MC subsets), and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions validating sequential content matters, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).

Positioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes across 4 reasoning models — our framework adds the entire causal contribution dimension, the calibrated gap metric, null-probe calibration with MCT geometric validation, phenomenon taxonomy, and task-difficulty conditioning. Their probe-trajectory methodology validates our P*(t) direction; we extend it to the dual-estimator gap that no existing framework provides.

We adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) constructs real G*(t) curves from the SAME model and dataset and tests whether at least 2 phenomena produce distinguishable trajectories (effect size d > 0.5) before committing to the full classification pipeline — addressing the concern that semi-synthetic simulation from cross-study measurements overestimates real-data accuracy. The semi-synthetic simulation is retained as hypothesis generation producing testable predictions, not as evidence.

Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits, the ICLR 2026 Workshop finding, and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific (weaker on MATH) — reveals the decorative→load-bearing transition with practical guidance on when chain-of-thought adds genuine value, applying length correction (residualizing on log(N)) to avoid generation-length confounds.

The paper focuses on four core contributions: (a) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. to demonstrate the value of the causal contribution dimension; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real data; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) probe-target analysis contrasting correctness vs. answer-content gaps. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs) as the primary bottleneck.

## Core Problem
A striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — with linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find that steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four distinct intervention strategies (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B parameters and report that ALL fail: 'RL training does not close the diagnostic–causal gap.' This diagnostic-causal gap — the divergence between what information is available in a model's hidden states and what information the chain-of-thought reasoning text causally contributes — is NOT a methodological obstacle to overcome; it IS the central phenomenon. Critically, the literature conflates two distinct probe targets: answer-content probes (Cox et al.: predicting the specific answer on binary tasks, models ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: predicting right/wrong on models up to 72B; Zhang et al.: per-chunk correctness on 7B-70B). This distinction matters because the gap's interpretation differs: answer-content gaps mean 'the model has already decided but CoT doesn't derive the answer,' while correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.' Meanwhile, the temporal dynamics of this gap are now empirically grounded: David (2511.14773) shows probe accuracy stabilizes at 0.84 AUC by token 4, remaining ~0.8 through token 100, with task-difficulty conditioning revealing easy (0.84) vs. hard (0.76) signatures. Zhang et al. (2504.05419) report chunk-level probe trajectories rising from 65% at 10% of reasoning to 79% at 100% on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with a characteristic dip at 5-10% of reasoning followed by recovery. Chrabąszcz et al. (2605.18549) demonstrate that temporal probe trajectories with 60+ signal-processing features achieve up to 17pp improvement over static probes, showing that trajectory dynamics capture information invisible to single-timepoint measurements. These temporal profiles suggest that different modes of CoT unfaithfulness — pre-CoT encoding, post-hoc rationalization, reasoning theater, myopic planning, thinking-answer gap — produce distinguishable temporal divergence signatures. Yet no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline: Chrabąszcz et al. provide the closest probe-trajectory methodology but lack any causal contribution component, gap metric, probe calibration, or phenomenon taxonomy; Ballon et al. (2601.23163) provide behavioral causal curves via truncation-reinjection but lack hidden-state measurement; the CMI framework provides layerwise causal audit on ~50 examples but no temporal resolution; Zhao et al.'s True Thinking Score provides per-step causal contribution but no probe-side measurement. The gap between diagnostic information availability and causal contribution IS the phenomenon of interest, not an obstacle.

## Opportunity
The field has independently produced the measurement tools needed for a unified temporal framework, but these tools remain siloed. The opportunity is fourfold:

(1) **Temporal gap measurement.** Despite rapid accumulation of probe measurements (David: 0.84 at t=4; Zhang: 0.82-0.91 on chunks; Yuan: 0.95 overall, 0.787 first-step; Esakkiraja: >90% pre-generation; Chrabąszcz et al.: 91-97% AUROC with max-pooling on trajectories), no work tracks the full-timeline divergence between probe-estimated information availability and intervention-estimated causal contribution. Chrabąszcz et al. (2605.18549) come closest on the probe side — extracting 60+ signal-processing features from probe trajectories across 4 reasoning models and 4 datasets, achieving up to 17pp improvement over static probes on GSM8K — but they target outcome prediction (correctness, harmfulness) rather than the faithfulness gap, and provide no causal contribution measurement. Their work validates that temporal probe trajectories capture dynamics invisible to static probes (confirming our P*(t) direction); our framework extends this via the dual-estimator gap G*(t) = P*(t) − C(t) that requires the additional causal contribution dimension, null-probe calibration, and phenomenon mapping. On the causal side, Ballon et al. (2601.23163) provide behavioral C(t) curves via truncation-reinjection at decile intervals on Qwen3/gpt-oss across GPQA-Diamond and MMLU-Pro — showing monotonic accuracy increase from 30.8-42.3% to 49.0-73.1% with control conditions validating that sequential content (not just context length) matters — but lack hidden-state measurement. The gap between these two measurement traditions IS the framework's niche.

(2) **Phenomenon unification with honest scoping.** The CoT faithfulness literature treats each failure mode as separate: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al. 2603.01437; Esakkiraja et al. 2604.01202), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103), thinking-answer gap. We propose that 2-3 of these are confidently distinguishable via trajectory-shape signatures in the information-contribution gap G*(t), with 4-5 as a stretch goal requiring additional features. The honest scoping — validated through an empirical pilot on real data before committing to full classification — is itself a contribution to a field prone to over-claiming.

(3) **Task-difficulty conditioning.** The ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration show easy→decorative, hard→faithful. David's easy/hard splits (0.84 vs. 0.76 at t=32) provide probe-level evidence. Gjølbye et al. (2605.15454) demonstrate that difficulty is systematically coupled to hidden-state trajectory geometry even after length correction (ρ⊥ = +0.41 for reasoning models vs. −0.06 for baselines on competitive programming), with domain-specific strength. A difficulty-conditioned gap framework can answer the practical question: at what difficulty level does CoT transition from decorative to load-bearing?

(4) **Probe target clarification.** The field has not confronted the distinction between answer-content probes (Cox et al.: binary tasks, ≤9B) and correctness probes (Yuan et al.: up to 72B). A framework that explicitly measures correctness awareness gap — and contrasts it with answer-content gap on applicable tasks — provides the first principled treatment of what 'knowing but not using' means.

Two prior works have combined probing with causal interventions: Kudo et al. (EACL 2026) on synthetic arithmetic, and the CMI framework (2602.03994) on ~50 examples. Wang (2604.15726) formalizes the need via competing hypotheses (H1: latent-mediated, H2: CoT-mediated, H0: serial compute) and proposes compute-audited designs — our ICG framework provides an empirical methodology to distinguish H1 from H2 at each token position. Neither Kudo et al. nor CMI provides: (a) full temporal-position coverage on natural benchmarks, (b) mapping to named faithfulness phenomena, (c) a standalone instance-level diagnostic, (d) systematic multi-model comparison, (e) robustness validation — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) an empirical pilot validating phenomenon separability on real data.

## Landscape
**Probe-based temporal measurement (foundational for our P*(t) component).** Chrabąszcz et al. (2605.18549) is the closest concurrent work: they introduce probe trajectories — tracking concept probability at each generated token — and extract 60+ signal-processing features (volatility, trend, steady-state, temporal segmentation, boundary transients, autocorrelation) via 3-layer MLP probes with Multi-Instance Learning meta-probe across layers. Key results: max-pooling achieves 91-97% AUROC on harmfulness detection (vs. 33-61% for average-pooling, demonstrating average/last-token pooling collapses to near-random); up to 17pp improvement over static probes on GSM8K mathematical error prediction across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours total). Critical differentiators from our framework: (a) NO causal contribution component — they measure only probe accuracy trajectories, not whether CoT causally contributes; (b) NO gap metric — just trajectory vs. static comparison for outcome prediction; (c) NO null-probe calibration or MCT geometric validation — their 3-layer MLP probes are uncalibrated; (d) NO phenomenon taxonomy — they separate correct/incorrect or safe/harmful, not faithfulness modes; (e) NO task-difficulty conditioning. Their 60+ feature extraction methodology is complementary and could enhance our trajectory-shape classification. David (2511.14773) trains per-position probes on reasoning models, finding 0.84 AUC at t=4, stable ~0.8 through t≈100, with easy/hard splits of 0.84 vs. 0.76 at t=32 on Qwen3-8B. Zhang et al. (2504.05419) probe R1-Distill models (7B/32B/70B) for correctness at each reasoning chunk, achieving 0.82-0.91 AUROC on GSM8K/MATH/AIME, with a rising trajectory from 65% at 10% chunk to 79% at 100%, enabling 24% token reduction via early-exit. Yuan et al. (2605.09502) report 0.95 AUROC on Qwen-3B, 0.852 on DeepSeek-R1-7B, 0.787 from first-step hidden states alone, and a concealment gap of 0.197 AUROC between hidden-state (0.787) and text-surface (0.590) classifiers — using correctness probes (right/wrong), not answer-content probes. Esakkiraja et al. (2604.01202) find >90% AUROC pre-generation on Qwen3-4B and GLM-Z1-9B, with a characteristic dip at 5-10% of reasoning and recovery to near-100% by think_end. Cox et al. (2603.01437) use answer-content probes (predicting specific answer A/B on binary tasks: Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) achieving >0.9 AUC on instruction-tuned Gemma-2 (2B, 9B) and Qwen-2.5 (1.5B, 3B, 7B) models, with causal validation via steering (>50% flip rates) — but 'the answer flip rate is negligible against the orthogonal baseline' on the reasoning model GPT-OSS-20B. Additional probing work: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop, probing F1 90-100%, steering 46% recovery).

**The diagnostic-not-causal evidence (motivating our framework).** Yuan et al. (2605.09502) is the decisive study: four interventions — activation steering (at most +4%), probe-guided best-of-N (matches random), self-correction (hurts accuracy −3%), activation patching (destroys coherence at α=0.5) — all fail. Tested on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. Key quote: 'The error signal is a diagnostic readout—a summary statistic of computation quality—not a causal component that can be edited.' Cox et al. (2603.01437) independently confirm: steering fails on reasoning models despite high probe accuracy. This establishes that probe accuracy ≠ causal potency on reasoning models, which is the foundational observation our framework exploits.

**Behavioral trajectory probing (foundational for our C(t) component).** Ballon et al. (2601.23163) introduce the truncation-reinjection protocol: generate full reasoning traces on Qwen3-4B/8B/14B and gpt-oss-20B/120B, truncate at decile intervals (10-100%), reinject with early-stopping suffix, measure answer-choice probability distributions. Key results: accuracy increases monotonically from 30.8-42.3% (no reasoning) to 49.0-73.1% (full trace) on GPQA-Diamond; decision commitment tracks similarly. Three control conditions validate causal content: random tokens (+2.1-4.3%), swapped traces (+3.2-8.7%), and shuffled tokens (+0.3-10.8%) all substantially underperform intact truncated traces (+18.1-33.1%), confirming sequential content — not just context length — drives gains. Stronger models rescue weak-model errors at 43-68% rate with free continuation vs. 28-51% anchoring in base mode. Explicitly disclaims faithfulness-to-internal-computations analysis, making it a direct precursor to our prefix-truncation C(t) estimator. Zhao et al. (2510.24941) introduce the True Thinking Score (TTS), measuring per-step causal contribution via numerical perturbation and ATE computation on DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7. Ye et al. (2602.11201) introduce NLDD, finding a Reasoning Horizon at 70-85% of chain length on 3 models across synthetic tasks. Basu & Chakraborty (2603.22816) propose a decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026) provides another causal measurement approach.

**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize. The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, DialoGPT on StrategyQA (20), TruthfulQA (10), GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors operating on small samples or synthetic tasks.

**Latent-reasoning theory.** Wang (2604.15726) formalizes three competing hypotheses about LLM reasoning: H1 (reasoning is primarily mediated by latent-state trajectories), H2 (reasoning is primarily mediated by explicit surface CoT), H0 (most reasoning gains are better explained by generic serial compute). Proposes compute-audited designs with six experimental arms (baseline, surface manipulation, surface control, latent intervention, latent control, compute-only expansion) and evidence tiers (probe-only = suggestive, compute-matched causal = strongest). Our ICG framework operationalizes Wang's H1/H2 distinction: when G*(t) >> 0, hidden states encode correctness awareness that CoT doesn't contribute (H1-consistent); when G*(t) ≈ 0, CoT is mediating (H2-consistent).

**Temporal hidden-state dynamics (concurrent complementary work).** Gjølbye et al. (2605.15454) study hidden-state trajectory geometry across 11 models (6 reasoning: R1-Distill-Qwen-7B/14B/32B, R1-Distill-Llama-8B, QwQ-32B, Phi-4-Reasoning; 5 instruction-tuned baselines) on competitive programming (500 Codeforces), math (500 MATH), and Boolean SAT (500 SATBench). After length correction (residualizing directness/curvature on log(N)), difficulty remains systematically coupled to trajectory geometry: reasoning models show ρ⊥^D = +0.41 on Codeforces vs. −0.06 for baselines (raw correlations reverse from −0.73 to +0.41), with weaker effects in math (+0.05 vs. −0.07) and non-specific effects in SAT (+0.27 vs. +0.23). Critically, prompt-stage linear probes do NOT mirror these geometric effects — reasoning dynamics manifest during generation, not at input. Their length correction methodology and domain-specificity finding are relevant for our temporal analysis and difficulty conditioning. Furuya & Tanimura (2605.01853) introduce StALT, a training-free trajectory statistic separating correct from incorrect reasoning trajectories. Herrmann et al. (2605.09159) study 'internal polylogue' dynamics: persona vectors tracked temporally across MMLU-Pro in four open-weight models. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, tracking concept-direction alignment per step on Qwen 3-4B; find easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals, achieving 14-70% token savings on R1-Distill/Phi-4/Qwen3.

**Probe calibration and inflation (methodological foundation).** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity. Ravichander et al. (2020) demonstrate properties recoverable even when unused. Voita & Titov (2020) show MDL-based probing reveals accuracy doesn't substantially favor pretrained over random. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning: geometric separability peaks transiently as a 'geometric pulse' while probe accuracy remains high afterward — direct evidence that probe accuracy overestimates information availability. We address this via null-probe calibration: P*(t) = P(t) − P_null(t).

**Trajectory-shape analysis (supporting our shape-based classification).** Entropy trajectory paper (2603.18940): monotonicity predicts reliability regardless of absolute levels (+5.8pp). RQA analysis (2602.06266): temporal features outperform aggregates 36.94% vs. 28.97%. Microsoft trajectory geometry (2604.05655): 0.852 AUC from shape features vs. 0.649 baseline. This literature validates trajectory shapes as diagnostic features.

**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence. Task-difficulty moderation: ICLR 2026 Workshop and Li et al. (2510.22362).

**Reasoning-model internal dynamics.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill.

**Benchmarks, surveys, pathology diagnostics.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Liu et al. (2602.13904): text-level metrics for rationalization/encoded/internalized reasoning. Reasoning Theater (2603.05488). Young (2603.26410). 'Lie to Me' (2603.22582). Various early-exit methods: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT.

**What remains open.** No extant framework provides: (1) a full-timeline information-contribution gap curve pairing calibrated probe trajectories with causal contribution estimation — Chrabąszcz et al.'s probe trajectories are the closest but lack the entire C(t) dimension, gap metric, and calibration; (2) an empirically-validated phenomenon trajectory-shape taxonomy grounded in real within-model, within-dataset G*(t) curves rather than cross-study semi-synthetic assembly; (3) an instance-level diagnostic score derived from the temporal gap; (4) difficulty-conditioned gap analysis with domain-specific nuance (following Gjølbye et al.'s finding of domain-dependent coupling strength); or (5) a principled treatment of the probe-target distinction (correctness vs. answer-content) and its implications for gap interpretation. The calibrated temporal ICG framework is unique in combining all five.

## Approach
We propose the Information-Contribution Gap (ICG) framework: a calibrated, temporally-resolved diagnostic that measures the divergence between information available in hidden states and information that causally contributes to model outputs, tracked across the full chain-of-thought generation trajectory.

**Formal Framework.** Define two time-varying quantities at each token position t during CoT generation:

(i) *Calibrated Information Availability* P*(t): Cross-validated AUROC of a linear probe on layer-l hidden states at position t, calibrated via null-probe normalization (P*(t) = P(t) − P_null(t), following Hewitt & Liang 2019 selectivity, where P_null is trained on shuffled labels). **Probe target: correctness (right/wrong).** We choose correctness over answer-content for three reasons: (a) broader applicability — correctness probes generalize beyond binary/MC tasks (Cox et al.'s answer-content probes are limited to binary A/B on 4 tasks), while correctness probes (Yuan et al.) work across model families up to 72B; (b) the 'diagnostic not causal' finding that motivates the entire framework is specifically about correctness probes (Yuan et al.'s four-intervention failure on correctness probes); (c) correctness gaps are more directly interpretable for faithfulness — G*(t) >> 0 means 'the model's hidden states encode awareness that its answer is right/wrong, but its CoT does not causally reflect this self-monitoring.' On binary/MC task subsets, we additionally train answer-content probes to test whether the 'what answer' gap differs from the 'whether correct' gap — a supplementary analysis testing whether pre-CoT encoding operates on content or meta-cognition. This measures excess correctness awareness above correlative features. We probe at layers L/4, L/2, 3L/4, L to capture layer-wise dynamics. MCT geometric validation (Chun et al. 2602.20338) on 500 examples confirms whether calibrated probe signal reflects geometrically organized information rather than mere retrievability. Note: Chrabąszcz et al. (2605.18549) demonstrate that probe trajectories with 60+ signal-processing features substantially outperform static probes (up to 17pp on GSM8K). We adopt their insight that temporal dynamics are essential, while adding null-probe calibration (which they lack) and extending to the dual-estimator gap. Where applicable, we incorporate their feature categories (volatility, trend, steady-state, boundary transients) as additional trajectory descriptors for phenomenon classification in Phase 3.

(ii) *Causal Contribution* C(t): The causal contribution of CoT up to position t, estimated via three complementary methods: (a) prefix-truncation ablation — measuring P(correct | CoT[:t]) vs. P(correct | full CoT), following Ballon et al.'s (2601.23163) truncation-reinjection protocol with their three control conditions (random tokens, swapped traces, shuffled tokens) to validate that C(t) measures genuine sequential content contribution rather than context-length effects (their finding: shuffled tokens retain +0.3-10.8% vs. intact +18.1-33.1%); (b) paraphrase perturbation — replacing CoT segments with meaning-preserving paraphrases and measuring answer stability; (c) NLDD-based influence scoring (Ye et al. 2602.11201) — measuring how corruption at position t degrades the answer distribution. Using multiple C(t) estimators provides robustness against single-method artifacts, following Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive.

**The Information-Contribution Gap.** G*(t) = P*(t) − C(t). This gap is the primary diagnostic signal:
- G*(t) ≈ 0: Correctness awareness and causal contribution are aligned (necessary for faithfulness)
- G*(t) >> 0: The model encodes correctness awareness it does not causally use in its CoT (diagnostic excess — the model 'knows but doesn't use')
- G*(t) < 0: The CoT contributes to correctness beyond what hidden states encode at that point (information assembled during reasoning)

Because P*(t) is null-probe-calibrated, uniform correlative inflation is removed. C(t) is not subject to probe inflation as it measures behavioral change under intervention. The gap G*(t) is interpretable as 'calibrated correctness awareness the model has but doesn't channel through its CoT at position t.' Following Wang's (2604.15726) H1/H2 framework: G*(t) >> 0 is H1-consistent (latent-mediated reasoning), G*(t) ≈ 0 is H2-consistent (CoT-mediated reasoning).

**Phenomenon Signature Predictions (2-3 confident, 4-5 stretch).** We ground predictions in real probe data but adopt honest scoping informed by the concern that cross-study heterogeneity may overestimate separability:

*Primary targets (HIGH confidence, validated in Phase 0b pilot):*
(i) *Pre-CoT encoding*: G*(t) starts high and stays high. Grounded in: David's 0.84 AUC at t=4, Esakkiraja's >90% pre-generation AUROC, Cox's >0.9 pre-CoT AUC. P*(0) > 0.5 (after calibration), C(t) rises slowly. Shape: large constant gap.
(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. Grounded in: Zhang et al.'s 65%→79% chunk trajectory, Li et al.'s finding that hard→faithful, Ballon et al.'s monotonic accuracy increase with reasoning length. P*(t) rises gradually, C(t) tracks P*(t). Shape: co-rising curves, small/decreasing gap.
(iii) *Post-hoc rationalization*: G*(t) starts moderate, rises during CoT. P*(t) stable (David: ~0.80 from t=4 through t=100), C(t) remains flat despite token generation. Shape: widening gap.

*Stretch targets (MODERATE confidence, require additional features):*
(iv) *Steganographic encoding*: G*(t) dip-and-recovery. Potentially consistent with Esakkiraja's dip at 5-10%. May require multi-layer analysis to separate from noise.
(v) *Reasoning Theater*: EMPIRICAL QUESTION. Under non-uniform inflation, may overlap with pre-CoT encoding or post-hoc rationalization. Additional features — layer-wise P*(t) distribution, C(t) variance under paraphrase perturbation, Chrabąszcz-style signal features (autocorrelation, boundary transients, dwell-time run-lengths) — may enable separation. Whether Theater is cleanly separable is reported honestly with confusion matrices.

**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** We construct semi-synthetic G*(t) curves grounded in real published data to generate testable predictions about trajectory-shape separability — but we do NOT treat this as evidence of real-data separability (published measurements come from different models, datasets, and setups, introducing heterogeneity that does not match within-dataset variance). Instead, the simulation identifies: (a) which trajectory features are most discriminative in principle, (b) what minimum effect sizes real-data classification needs to achieve, (c) where non-uniform inflation causes theoretical overlap between phenomena. I_probe(t) profiles drawn from published measurements (David, Zhang, Esakkiraja, Yuan), C(t) profiles modeled from NLDD (Ye et al.) and TTS (Zhao et al.) data, non-uniform inflation calibrated against Chun et al.'s MCT finding. The real validation comes from Phase 0b.

**Phase 0a: Gap Characterization (Weeks 1-2.5).** Three objectives on 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):
(i) Construct empirical P*(t) and C(t) curves at token-level resolution
(ii) Validate null-probe calibration: P_null(t) shows high accuracy (inflation exists) but P*(t) shows meaningful variance (calibration reveals structure)
(iii) Characterize causal potency: following Cox et al.'s protocol, measure answer flip rates via probe-direction steering on reasoning vs. instruction-tuned models

Expected outcome (base case): Causal potency is low on reasoning models, confirming the diagnostic-not-causal property and validating the ICG framework's interpretive power. If causal potency is unexpectedly high, this is an exciting upgrade. Either outcome is scientifically valuable.

**Phase 0b: Empirical Pilot for Phenomenon Separability (Weeks 2.5-4).** This phase validates that trajectory-shape classification is feasible on real data before committing to the full pipeline. On the SAME model (R1-Distill-Qwen-7B) and datasets (GSM8K + MATH-500, 1000 examples), construct real G*(t) curves and test whether at least 2 phenomena produce distinguishable trajectories. Protocol: (i) partition examples by difficulty quintile and model behavior (easy-correct with high P*(0) → pre-CoT encoding candidates; hard-correct with rising P*(t) tracking C(t) → genuine reasoning candidates; incorrect with stable P*(t) and flat C(t) → post-hoc rationalization candidates); (ii) compute full G*(t) for each partition; (iii) test effect size d > 0.5 on at least 2 trajectory features between partitions. Apply Gjølbye et al.'s (2605.15454) length correction (residualizing trajectory features on log(N)) to ensure differences are not conflated with generation-length effects. Success criterion: d > 0.5 between at least 2 partitions on 2+ features. If d < 0.3 across all features, downscope to a characterization paper (gap exists and varies with difficulty, but trajectory shapes are not cleanly phenotypic) — still a strong contribution given no prior full-timeline G*(t) measurement exists.

**Phase 1: Full ICG Construction (Weeks 4-9).** Conditional on Phase 0b showing separability (d > 0.5). Extend to 4 models (add QwQ-32B or R1-Distill-32B) × 4 benchmarks (add GPQA-Diamond or AIME). Full calibrated P*(t) with null-probe normalization + MCT concordance check on 500 examples. Three C(t) estimators with Ballon et al.-style controls (random, swap, shuffle baselines). Cross-reference with TTS (Zhao et al.) at step boundaries. Bootstrap confidence intervals on G*(t).

**Phase 2: Task-Difficulty Conditioning (Weeks 7-11).** Partition each benchmark into difficulty quintiles (using model accuracy as proxy). Measure G*(t) per quintile. Hypothesis grounded in David's easy/hard data, Li et al.'s finding, and Gjølbye et al.'s difficulty-geometry coupling: easy problems show large persistent gap (decorative CoT), hard problems show converging gap (load-bearing CoT). Following Gjølbye et al., apply length correction and report domain-specific effects — expecting stronger effects on math/code benchmarks than MMLU, given their finding of ρ⊥ = +0.41 on Codeforces vs. +0.05 on MATH. The transition point — where G*(t) shifts from decorative to genuine — provides practical guidance on when CoT adds value.

**Phase 3: Phenomenon Classification and Robustness (Weeks 9-14).** Apply trajectory-shape classification to real data. Target: 2-3 cleanly separable phenomena, with 4-5 reported honestly including overlap. Incorporate Chrabąszcz et al.'s feature categories (volatility, trend, boundary transients, autocorrelation) alongside our gap-specific features (initial G* value, G* slope, convergence rate, dC/dt locality). Six robustness ablations following Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection (single best vs. multi-layer); (c) C(t) estimator agreement (prefix vs. paraphrase vs. NLDD); (d) gap normalization method; (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content on binary/MC subsets). Report sensitivity ranges across all dimensions.

**TIF Score.** Temporal Information-contribution Faithfulness score: normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s text-level metrics.

**Paper Focus (Tightened).** Core contributions: (1) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al.'s probe trajectories — demonstrating the value added by the causal contribution dimension and gap metric; (2) Phase 0b empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real within-model, within-dataset data; (3) task-difficulty conditioning revealing the decorative→load-bearing transition with domain-specific strength following Gjølbye et al.'s nuance. Supporting: robustness ablations (6 dimensions); TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness probe comparison; semi-synthetic simulation as hypothesis generation.

**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT cross-reference. Gjølbye-style length correction on all temporal analyses.

## Resource Estimate
{'manual': {'gpu_hours': '~830 H100-hours (Phase 0a characterization: 80 hrs [3 models × 3 datasets, probe training + prefix ablation + steering tests]; Phase 0b empirical pilot: 30 hrs [1 model × 2 datasets, full G*(t) construction + partition analysis + length correction]; Phase 1 full ICG: 120 hrs [4 models × 4 benchmarks, multi-layer probes + 3 C(t) estimators]; Phase 2 difficulty conditioning: 50 hrs; Phase 3 phenomenon classification + robustness ablations: 50 hrs; NLDD on 32B model: 250 hrs [primary bottleneck — up to 20 perturbation positions × 5K examples × forward passes]; NLDD on 7B/14B models: 100 hrs; MCT geometric validation: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic simulation: 50 hrs [mostly CPU, some GPU for validation])', 'timeline': '15-17 weeks (2 researchers: 4 weeks Phase 0a+0b characterization + pilot; 5 weeks Phase 1 full ICG; 4 weeks Phases 2-3 in parallel with NLDD; 2-3 weeks writing + ablations)', 'estimated_gpu_cost': '$2,500 at ~$3/H100-hour (cloud spot pricing)', 'storage': '3-5 TB (4 layers per model, fp16); reducible to ~1.5 TB via PCA'}, 'human_in_loop': {'gpu_hours': '~830 H100-hours', 'timeline': '13 weeks (1 researcher + Claude for experiment design and analysis)', 'claude_api_cost': '$350', 'estimated_gpu_cost': '$2,500'}, 'auto_research': {'gpu_hours': '~830 H100-hours', 'timeline': '11 weeks', 'claude_api_cost': '$700', 'estimated_gpu_cost': '$2,500', 'speed_bottleneck': 'NLDD on 32B (~250 H100-hours, ~30% of total compute) is the primary bottleneck. Each NLDD evaluation requires corrupting reasoning at multiple positions and measuring logit degradation — O(T × N) forward passes where T≈20 perturbation positions and N≈5K examples. For 32B models, this cannot be easily parallelized beyond 8-GPU data parallelism. Secondary: 671B subset (8×H100, ~50 hrs); MCT geometric validation (~50 hrs). Phase 0b pilot (30 hrs) provides early go/no-go signal before committing full Phase 1-3 compute.'}}

## Inspired By
The convergence of five independent lines of evidence — (a) Cox et al.'s finding that answer-content probe steering fails on reasoning models despite high accuracy; (b) Yuan et al.'s systematic demonstration that four interventions all fail on correctness probes, establishing 'diagnostic not causal'; (c) the temporal probe dynamics now empirically characterized by David (0.84 AUC at t=4, stable ~0.8), Zhang et al. (chunk-level rising trajectory), Esakkiraja et al. (pre-generation >90% with dip-recovery), and Chrabąszcz et al. (60+ trajectory features capturing dynamics invisible to static probes, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection protocol demonstrating monotonic behavioral C(t) curves with rigorous controls (sequential content +18.1-33.1% vs. shuffled +0.3-10.8%) — all pointing to the same insight: the gap between diagnostic information availability and causal contribution IS the phenomenon of interest. Additionally inspired by: Wang's (2604.15726) formalization of H1/H2/H0 hypotheses providing the theoretical scaffold for what our framework empirically measures; Gjølbye et al.'s (2605.15454) finding that difficulty-geometry coupling is domain-specific and requires length correction; Herrmann et al.'s concurrent temporal persona-vector dynamics; and the trajectory-shape literature showing shapes can distinguish phenomena regardless of absolute-value calibration.

## Target Venues
- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)
- ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)

## Key References
- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al., arXiv 2605.18549)
- Probing the Trajectories of Reasoning Traces in Large Language Models (Ballon et al., arXiv 2601.23163)
- LLM Reasoning Is Latent, Not the Chain of Thought (Wang, arXiv 2604.15726)
- Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al., arXiv 2605.15454)
- Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502)
- Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437)
- Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773)
- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (Zhang et al., arXiv 2504.05419)
- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)
- Can Aha Moments Be Fake? True Thinking Score (Zhao et al., arXiv 2510.24941)
- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)
- Do LLMs Experience an Internal Polylogue? (Herrmann et al., arXiv 2605.09159)
- LLMs Faithfully and Iteratively Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)
- When Chains of Thought Don't Matter: Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)
- Spatiotemporal Hidden-State Dynamics / StALT (Furuya & Tanimura, arXiv 2605.01853)
- Mapping Faithful Reasoning / Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)
- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)
- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)
- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)
- Emergent Manifold Separability / MCT (Chun et al., arXiv 2602.20338)
- Tracing the Traces: Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)
- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)
- Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019)
- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)
- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)
- Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940)
- Is My Model Mind Blurting? RQA of Reasoning Dynamics (arXiv 2602.06266)
- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)
- Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128)
- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)
- Breaking the Chain (Somov et al., arXiv 2603.16475)
- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)
- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)
- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)
- Reasoning Theater (Boppana et al., arXiv 2603.05488)
- No Global Plan in CoT (Xu et al., arXiv 2602.02103)
- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)
- CoT Monitorability via Information Theory (Anwar et al., arXiv 2602.18297)
- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)
- Demystifying Reasoning Dynamics with MI (Qian et al., NeurIPS 2025, arXiv 2506.02867)
- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)
- Why Models Know But Don't Say (Young, arXiv 2603.26410)
- Lie to Me (arXiv 2603.22582)
- Step-Level Hallucination via Transport Geometry (Alvarez & Baheri, arXiv 2605.13772)
- From Reasoning to Answer (arXiv 2509.23676)
- SAE Reasoning Features (arXiv 2503.18878)
- FRIT (Swaroop et al., arXiv 2509.13334)
- Solution Hides in Hidden States (arXiv 2604.23351)
- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)
- LEACE: Perfect Linear Concept Erasure (Belrose et al., NeurIPS 2023, arXiv 2306.03819)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "716ad6a8-42c4-4c99-ab74-9ec77738fd36",
  "type": "user",
  "uuid": "d60ab530-6bd0-44c2-9ad3-9038a2808ba9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:29:38.786Z_

```json
{
  "parentUuid": "d60ab530-6bd0-44c2-9ad3-9038a2808ba9",
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
  "uuid": "fc90a28f-6687-4fb3-9e8e-15c860d5f0ef",
  "timestamp": "2026-05-20T03:29:38.786Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:29:38.786Z_

```json
{
  "parentUuid": "fc90a28f-6687-4fb3-9e8e-15c860d5f0ef",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b8096280-5fe4-423e-9708-b16bbf649c5d",
  "timestamp": "2026-05-20T03:29:38.786Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information to make my assessment. Let me no…",
  "leafUuid": "b8096280-5fe4-423e-9708-b16bbf649c5d",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate CoT faithfulness framework for CoRL 2026",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:30:15.542Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully and produce a Meta Judge output.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中偏强 (Medium-Strong)
- Related Work: 强 (Strong)
- Probability for CoRL: [2% - 8%] 中位 3%
- Probability for ICLR/ICML (hypothetical): [25% - 38%] 中位 30%
- Key concerns: Venue mismatch (致命), conditional novelty, trivial alternative threat
  
**Reviewer 2:**
- Novelty: 弱-中 (Weak-Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability for CoRL: 0-2% (desk reject)
- Probability for ICLR/ICML (hypothetical): [18% - 28%] 中位 22%
- Key concerns: Venue mismatch (致命), trivial combination, commensurability of P*(t) and C(t)

**Reviewer 3:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)

All three reviewers agree on a fatal venue mismatch and strong related work coverage, with novelty assessments ranging from weak to medium and significance consistently at medium level. The CoRL acceptance probabilities are extremely low across the board (0-8%), while hypothetical ICLR/ICML probabilities cluster around 22-30%, suggesting this work might be better suited for a general ML venue rather than a robotics-specific conference. Looking at where the reviewers align, there's unanimous agreement on the fatal venue mismatch and that the novelty is integration-focused rather than conceptual, plus consensus that the phenomenon classification is unvalidated and the core diagnostic-not-causal finding isn't new. The commensurability problem between P*(t) and C(t) appears in two reviewers' explicit critiques. One anomaly stands out: R1 rates significance as medium-strong while R2 and R3 both rate it as medium.

For CoRL 2026, all three reviewers converge on essentially 0-3% acceptance probability—the venue mismatch is disqualifying since the proposal itself targets ICLR/ICML instead. But if we assess this for those target venues, the estimates cluster around 22-30% with a median of 25% and tight consistency, suggesting the work has modest but real potential in the right venue.

The key insight is that this is a desk reject at CoRL due to misalignment, not fundamental quality issues. I should report both the CoRL probability as the official answer and the ICLR/ICML assessment since that's where the actual decision-making value lies for the user. I need to recalibrate my upper bound based on the constraint that my aggregate estimate shouldn't exceed the most generous individual estimate—R1's 3% for CoRL—so I'm capping my final probability at 8%. Now I'll write up the Meta Judge output with the CoRL 2026 target as the primary recommendation, noting that the venue mismatch is fatal for acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8096280-5fe4-423e-9708-b16bbf649c5d",
  "isSidechain": false,
  "requestId": "req_011CbD7UfvYknPyRRZWgSPTe",
  "type": "assistant",
  "uuid": "f6e6884d-eaf2-499e-be7d-eb6aa1d53863",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRBGrHxJcZFYWV6kRZDw2i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26658,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4101,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 26658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26658
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

_source line 9 · 2026-05-20T03:31:20.254Z_

【阶段】: Meta Judge
【三次中位】: [3%, 1%, 0%]  std=1.2%
（注：以上为 CoRL 2026 目标概率。三位审稿人同时给出了假设投 ICLR/ICML 的 idea 质量概率：[30%, 22%, 25%]  std=3.3%）

【共识维度】:
- **Venue Mismatch = 致命**（3/3 一致）：CoRL 是 Conference on Robot Learning，proposal 是纯 NLP/interpretability 工作，零 robotics 内容。Proposal 自身 Target Venues 也写的是 ICLR 2027 / ICML 2027。三位审稿人均判定 desk reject 风险极高，这是不可修补的结构性问题（除非彻底重构 proposal 方向）。
- **Novelty = 弱至中，integration 型而非 conceptual 型**（3/3 一致）：核心操作 G*(t) = P*(t) − C(t) 是将 Chrabąszcz et al. 的 probe trajectory 和 Ballon et al. 的 truncation-reinjection C(t) 做差。三位均认为这是 "natural combination / synthesis"，而非 surprising insight。
- **Related Work = 强**（3/3 一致）：40+ 篇引用覆盖全面且描述准确，是 proposal 最突出的优点。
- **Trivial Alternative 威胁存在**（3/3 一致）：直接并排展示已有的 P(t) 和 C(t) 曲线 + 简单统计量即可传达核心 message，不需要完整的 ICG 框架。
- **Phenomenon classification 未验证**（3/3 一致）：核心赌注（不同 faithfulness phenomena 产生可区分的 G*(t) trajectory shapes）完全依赖 Phase 0b 实验结果，若 d < 0.3 则核心贡献崩塌为 characterization paper。
- **P*(t) 与 C(t) 的可减性/量纲问题**（3/3 均提及，R2 和 R3 尤为强调）：AUROC 与 behavioral accuracy delta 的量纲和语义不同，直接做减法的物理意义不清晰，proposal 未提供充分论证。
- **核心 message 已被他人报告**（3/3 一致）：Yuan et al. 和 Cox et al. 已直接报告 "diagnostic-not-causal gap"，本 proposal 更多是 operationalize 而非 discover。
- **Significance = 中**（R2、R3 一致为"中"；R1 为"中偏强"，见下方异常处理）：CoT faithfulness 问题本身重要，但领域极度拥挤（30+ 篇 2025-2026 论文），纯 diagnostic/measurement 贡献无 actionable improvement，边际价值受稀释。

【异常维度】:
- **R1 Significance 评"中偏强"**：R1 比 R2、R3 更看好 significance，主要因为"difficulty conditioning 揭示 decorative→load-bearing 转换点有实践指导意义"。但 R2 和 R3 均指出 practical implication 不清晰（"你知道了 CoT 是 unfaithful 的，然后呢？"），且领域拥挤度稀释了边际贡献。2 vs 1，降权 R1 的乐观判断，综合定为"中"。
- **R1 Novelty 评"中"**：R2 评"弱-中"，R3 评"弱"。R1 对 null-probe calibration + phenomenon taxonomy 的组合赋予了更高增量价值。但 R2 和 R3 的论证更具体——R2 指出 CMI framework (2602.03994) 已结合 probing 与 causal intervention，R3 指出 predicted signatures 多为 "obvious from definitions"。综合定为"弱-中"，偏向更严格的两位。

【最终概率】: [0% - 3%] 中位 1%
（CoRL 2026 目标。附 ICLR/ICML 假设概率：[18% - 30%] 中位 23%）

【一致性】: 高（CoRL 概率 std=1.2%；ICLR/ICML 假设概率 std=3.3% 属中一致，按规则偏向更严格方 R2 的 22%，取中位 23%）

【综合理由】:

**CoRL 2026 概率（主判决）**：三位审稿人对 venue mismatch 的判定完全一致，且有硬证据支撑——CoRL CFP 明确要求 "submissions should focus on a core robotics problem"，本 proposal 不包含任何 robotics 内容，proposal 自身也未将 CoRL 列为 target venue。这不是一个可以通过迭代优化修补的问题，而是根本性的方向不匹配。中位 1%（几乎确定 desk reject）。

**ICLR/ICML 假设概率（参考判决）**：三位审稿人在 idea 质量上也呈现较好的收敛——Novelty 是限制上界的关键因素。R2（22%）最严格，其论证最为扎实：(a) "diagnostic-not-causal gap" 这一 core message 已被 Yuan et al. 直接报告，本 proposal 是 operationalization 而非 discovery；(b) G*(t) = P*(t) − C(t) 的量纲不可比性是一个尚未解决的理论弱点；(c) CMI framework 已做了 probing + causal intervention 的组合。R1（30%）最宽松，给了 significance 更高分，但其理由（difficulty conditioning 的实践价值）不足以突破 novelty 的天花板。按"分歧时偏严"原则，中位定为 23%，不超过 R1 的 30% 上界。

**核心判断**：idea 本身属于"方向正确、执行严谨、但 novelty delta 有限"的 integration 型工作。Related work 覆盖是真正的强项，但 related work 做得好反而暴露了 novelty 空间的狭小。即便投 ICLR/ICML，也处于 borderline 区间下半段。而投 CoRL 则是致命性的方向错误。

【建议】: KILL（CoRL 2026 投稿方向致命不匹配，无法通过 proposal 迭代修补）

【实施评估】:
- 计算资源: ~830 H100-hours（约 $2,500 cloud spot pricing），NLDD on 32B 模型（~250 hrs）为主要瓶颈。整体计算量在学术实验室可承受范围内，不构成实施障碍。
- 数据需求: GSM8K、MATH-500、MMLU、GPQA-Diamond、AIME——均为公开 benchmark，无数据获取障碍。
- 人工介入: 需要 1-2 名研究者持续投入 13-17 周。Phase 0b pilot 需要人工判断 go/no-go 决策。无需人工标注（使用已有 benchmark labels）。
- 训练需求: 仅训练 linear probe（极轻量），不涉及 LLM 训练或微调。推理成本（forward pass for probing + truncation-reinjection）是主要 GPU 消耗。
- 新 Benchmark: 不需要构建新 benchmark。TIF score 需与 FaithCoT-Bench (ICLR 2026) 对标验证。
- 预估周期: 15-17 周（含 Phase 0a/0b pilot 4 周 + Phase 1 full ICG 5 周 + Phase 2-3 4 周 + 写作 2-3 周）。时间线对 ICLR 2027 Sep deadline 可行（从现在起约 4 个月），对 CoRL 2026 不适用。

---

**补充说明（传递给后续流程）**：

本 proposal 在 CoRL 2026 投稿目标下触发 KILL 条件——venue mismatch 是致命且不可修补的结构性问题。三位审稿人完全一致。

若用户确认实际目标为 ICLR 2027 / ICML 2027（与 proposal 自身 Target Venues 一致），则 idea 质量的综合估计为 [18%-30%] 中位 23%，属于"边缘"区间，有进入迭代优化流程的价值，但需解决以下核心问题才能提升概率：
1. Novelty 强化：需要超越 "integration of existing tools" 的定位，找到 conceptual surprise
2. G*(t) 量纲问题：P*(t) (AUROC) 与 C(t) (behavioral accuracy delta) 的直接相减需要严格的归一化/commensurability 论证
3. Phenomenon classification 的可行性需 Phase 0b 尽早验证
4. Trivial alternative 的差异化需更锐利的论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6e6884d-eaf2-499e-be7d-eb6aa1d53863",
  "isSidechain": false,
  "requestId": "req_011CbD7UfvYknPyRRZWgSPTe",
  "type": "assistant",
  "uuid": "f79e36d9-18e9-4dbe-9183-8e97f44555d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRBGrHxJcZFYWV6kRZDw2i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26658,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4101,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 26658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26658
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information to make my assessment. Let me no…",
  "leafUuid": "f79e36d9-18e9-4dbe-9183-8e97f44555d7",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate CoT faithfulness framework for CoRL 2026",
  "sessionId": "a6e9b467-2dce-4246-8775-da445c4ad66f"
}
```

---
