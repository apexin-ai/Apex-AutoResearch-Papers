# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6.jsonl`
- **Structured JSON:** [`2f11e77bea26131d2d52.json`](../../sessions/2f/2f11e77bea26131d2d52.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:29:16.786Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:29:16.786Z",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 【关键提醒：严重的 Venue Mismatch】\n本 proposal 是一篇纯 NLP/多语言 LLM 评估论文，与 CoRL（Conference on Robot Learning）的 scope 完全不匹配。CoRL 聚焦于机器人学习（manipulation, navigation, sim-to-real, robot perception 等），本文没有任何机器人相关内容。投稿 CoRL 极大概率 desk reject。建议目标会议改为 ACL / EMNLP / NAACL / COLM 等 NLP venue。以下评估基于该 idea 在**合适的 NLP venue**（如 ACL/EMNLP 主会）的质量，供参考。\n\n【领域调研】:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778) (NeurIPS 2025 Workshop Poster, 非主会): 本 proposal 的直接前驱工作。提出\"self-correction blind spot\"概念，在 14 个开源模型上发现平均 64.5% 盲区率，\"Wait\" prompt 可降低 89.3% 盲区。注意：proposal 中称其为\"NeurIPS 2025\"，实际为 **LLM Evaluation Workshop poster**，非主会论文，这一描述可能被审稿人视为 misleading。\n- [Large Language Models Cannot Self-Correct Reasoning Yet (arXiv:2310.01798)](https://arxiv.org/abs/2310.01798) (ICLR 2024): 开创性工作，论证 LLM 在无外部反馈时无法有效自我纠正推理。Proposal 未显式引用此关键工作。\n- [When Can LLMs Actually Correct Their Own Mistakes? (arXiv:2406.01297)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713) (TACL 2024/2025): 综合 survey，系统梳理 self-correction 成功的条件。Proposal 未引用。\n- [Understanding Multilingualism in MoE LLMs (arXiv:2601.14050)](https://arxiv.org/abs/2601.14050) (2026.01): Proposal 直接引用。研究 MoE 模型的多语言路由机制和专家特化。提出 routing-guided steering 方法。论文真实存在，描述基本准确。\n- [MMLU-ProX (arXiv:2503.10497)](https://arxiv.org/abs/2503.10497) (EMNLP 2025): 29 语言多语言 benchmark，文档了高达 24.3% 的跨语言性能差距。Proposal 未引用此直接相关的多语言评估工作。\n- [MM-EVAL (arXiv:2410.17578)](https://arxiv.org/abs/2410.17578): 覆盖 18 语言的多语言 meta-evaluation benchmark。\n- [Cross-Lingual Auto Evaluation (arXiv:2410.13394)](https://arxiv.org/abs/2410.13394) (ACL 2025): 6 语言的跨语言评估框架。\n- [Steering MoE LLMs via Expert (De)Activation (arXiv:2509.09660)](https://arxiv.org/abs/2509.09660): MoE 专家激活/去激活转向方法，与 proposal 的 MoE 机制分析相关。\n\n- **调研总结**: 多语言 LLM 评估（MMLU-ProX, BenchMAX, GlotEval 等）和 LLM self-correction（Self-Correction Bench, \"Cannot Self-Correct\" 等）各自是活跃的研究方向，但二者的**交叉领域——跨语言 self-correction 评估——确实尚无直接前驱工作**。这构成一个真实的研究空白。然而，这个空白之所以存在，部分原因可能是结果过于可预测（已知：LLM 在非英语上一切都更差 + self-correction 本身就脆弱 → 非英语 self-correction 更差，这是 trivially expected）。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁：\n1. **直接翻译 Self-Correction Bench 到多语言**：无需 CGA 公式化，直接在 12 种语言上跑原始 benchmark，报告各语言的盲区率。这个 trivial 版本能覆盖 proposal ~40% 的贡献。\n2. **核心发现的可预测性**：\"非英语语言的 self-correction 更差\"几乎是 trivially expected。已有大量工作（MMLU-ProX 等）证明 LLM 在非英语上的所有能力都更差，self-correction 不太可能是例外。\n\n**增量价值所在**：\n- CGA 假设（β > 1，超线性退化）是非 trivial 的——线性退化是 expected，但超线性退化（即 self-correction 的退化比基础能力退化更严重）如果成立，有安全/对齐领域的重要含义（多语言安全差距比能力差距更大）。\n- \"Wait\" prompt 的跨语言泛化性是一个genuinely interesting 的问题——英文单 token 触发器是否在非拉丁字母语言中也有效？\n- MoE 路由在 generation vs. self-correction 阶段的差异分析是 novel 的机制层面贡献。\n\n但总体而言，增量价值主要来自分析的*深度和方法论*，而非*核心发现的surprise factor*。\n\n【前提假设检验】:\n核心 claim 的逻辑链中存在以下未经验证的假设：\n\n1. **\"Wait\" prompt 的可靠性假设**：proposal 将 \"Wait\" 的 89.3% 盲区降低效果视为 established fact 并在其上构建 cross-lingual 扩展。但原始发现来自一篇 **NeurIPS workshop poster**（非主会），在学术严谨性上尚未经过顶会主会级别的同行评审验证。如果 \"Wait\" 的效果在更严格的评估下不如报告的那么强，本文最高 novelty 的贡献（\"Wait\" 跨语言泛化性）的基础就会动摇。\n\n2. **CGA 的前提假设**：β > 1（超线性退化）假设的成立依赖于 self-correction 比 base accuracy 有\"额外的\"语言敏感性。但自我纠正本质上需要更强的元认知能力，而元认知能力在低资源语言中可能本身就更弱——这可能只是 meta-cognitive ability 整体下降的自然推论，而非 self-correction 特有的现象。换言之，β > 1 可能只是反映了\"困难任务在弱语言上退化更快\"的通用规律，而非 self-correction 的特殊性。\n\n3. **Qwen3 MoE/Dense \"controlled comparison\" 假设**：proposal 声称 Qwen3-30B-A3B (MoE) 和 Qwen3-32B (Dense) \"shares identical tokenizer and training data, enabling controlled architecture comparison\"。但即使 tokenizer 和训练数据相同，模型容量（active parameters 差异巨大：3B vs 32B）、训练 dynamics、收敛行为等都不同，将其简单视为\"仅架构不同\"的 controlled comparison 过于简化。\n\n4. **\"Correction triggers are universal or language-mediated\" 的二元框架**：这一 framing 假设 correction 触发机制要么是 universal 要么是 language-mediated，但现实可能更复杂——可能因任务类型、错误类型、模型而异，而非简单的二元。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   理由：跨语言 self-correction 评估这一交叉方向确实无直接前驱（调研中未找到任何专门评估多语言 self-correction blind spot 的工作），这是真实的 novelty。CGA 公式化（β > 1 超线性假设）和 \"Wait\" prompt 跨语言泛化性测试都超越了简单的 benchmark 翻译。然而，核心方向是两个已有方向（多语言评估 + self-correction 评估）的直接组合，属于\"显而易见但没人做\"的类型。Self-Correction Bench (arXiv:2507.02778) 的多语言扩展是最自然的 next step，审稿人容易将其视为 incremental extension。最核心的 surprise factor 取决于实验结果——如果 β ≈ 1（线性退化），novelty 大打折扣；如果 \"Wait\" 在非英语上完全失效或完全有效，都各有其价值但可预测性不同。\n\n2. **Significance: 中** — \n   理由：研究问题本身有实际意义——如果 self-correction 在非英语中退化比 base accuracy 更严重，这对多语言 AI safety 和 alignment 有直接影响。但需诚实评估：(a) 多语言 LLM 评估领域已有大量 benchmark（MMLU-ProX 等已在 29 语言上系统评估），再增加一个 self-correction 维度是有价值但非变革性的；(b) 核心发现如果是 positive（\"是的，非英语 self-correction 更差，且 disproportionately 更差\"），大多数审稿人的反应可能是 \"I would have guessed this\" 而非 \"surprising\"；(c) 对 robotics 领域（CoRL）的 significance 为零。对 NLP 领域，这是一个 useful empirical contribution，但不是那种改变研究方向的工作。\n\n3. **Related Work: 中偏弱** — \n   理由：proposal 引用了 Self-Correction Bench 和 arXiv:2601.14050，这两个直接相关引用是准确的。但存在以下显著遗漏：(a) 未引用 Huang & Zhao (ICLR 2024) \"Large Language Models Cannot Self-Correct Reasoning Yet\"——这是 self-correction 领域最重要的工作之一；(b) 未引用 TACL 2024 的 self-correction 综合 survey；(c) 未引用 MMLU-ProX (EMNLP 2025)——直接相关的 29 语言多语言 benchmark；(d) 将 Self-Correction Bench 描述为 \"NeurIPS 2025\" 而其实是 workshop poster，可能被视为 misleading。差异化定位（\"first systematic evaluation\"）在交叉领域成立，但对两个母领域的文献覆盖不够充分。\n\n【概率估计】: [20% - 32%] 中位 25%\n（注：此估计基于投稿**合适的 NLP venue**如 ACL/EMNLP 主会。若投稿 CoRL，中稿概率估计为 0-3%，因为完全 out of scope。）\n\n【估计理由】: \nidea 处于\"方向正确、有真实 novelty delta，但核心发现 predictable\"的区间。三个维度均为中等水平，没有致命缺陷但也没有突出亮点。Novelty 的上限被\"两个已有方向的显而易见组合\"所限制——即使 CGA 和 \"Wait\" 泛化测试提供了超越 trivial extension 的深度，审稿人仍可能认为这是 Self-Correction Bench 的自然多语言扩展。Significance 的上限被核心发现的可预测性限制——\"非英语 self-correction 更差\"不会让人 surprised。如果实验中 β 显著 > 1 或 \"Wait\" 表现出 counter-intuitive 的跨语言模式，可以 push 到上界 32%；如果 β ≈ 1 且 \"Wait\" 效果线性下降，则在下界 20% 附近。\n\n【主要风险】: \n1. **\"I would have guessed this\" 风险**：核心发现（非英语 self-correction 更差，且 disproportionately 更差）高度可预测。审稿人可能认为这是 well-known multilingual performance gap 在又一个维度上的确认，缺乏 genuine surprise。除非 \"Wait\" 泛化性测试产生 counter-intuitive 结果（例如非英语语言等价触发词反而比 \"Wait\" 更有效，或 \"Wait\" 在某些语言家族完全失效而在另一些完全保留），否则 story 缺乏记忆点。\n2. **Incremental extension 风险**：论文的最大 novelty 来源——Self-Correction Bench 本身——仅是 NeurIPS workshop poster 级别的工作，尚未被顶会主会认可。在此基础上做多语言扩展，审稿人可能质疑\"基础工作本身的成熟度是否足以支撑扩展\"。此外，proposal 将 workshop poster 描述为 \"NeurIPS 2025\" 可能引发审稿人对学术诚信的 concern。\n```\n\nSources:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)\n- [Self-Correction Bench at NeurIPS 2025 Workshop](https://openreview.net/forum?id=dLz0bnmL2r)\n- [Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)](https://arxiv.org/abs/2310.01798)\n- [When Can LLMs Actually Correct Their Own Mistakes? (TACL Survey)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177)\n- [Understanding Multilingualism in MoE LLMs (arXiv:2601.14050)](https://arxiv.org/abs/2601.14050)\n- [MMLU-ProX (EMNLP 2025)](https://arxiv.org/abs/2503.10497)\n- [Cross-Lingual Auto Evaluation (ACL 2025)](https://arxiv.org/abs/2410.13394)\n- [Steering MoE LLMs via Expert (De)Activation](https://arxiv.org/abs/2509.09660)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to produce my evaluation. Let me compile the findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. Self-Correction Bench (arXiv:2507.02778, NeurIPS 2025 Workshop on LLM Evaluation):\n   - 这是本 proposal 的直接前驱工作。定义了\"Self-Correction Blind Spot\"概念，测试了 14 个开源模型，发现平均 64.5% 的 blind spot 率。关键发现：\"Wait\" prompt 可将 blind spot 降低 89.3%。\n   - ⚠️ 重要：proposal 描述该工作为\"NeurIPS 2025\"，但根据调研，它是 NeurIPS 2025 的 **Workshop paper**（LLM Evaluation Workshop），并非主会论文。这一差异影响对 proposal 所构建基础的评估——该 proposal 本质上是对一篇 workshop paper 进行多语言扩展。\n\n2. Understanding Multilingualism in MoE LLMs (arXiv:2601.14050):\n   - Proposal 引用的 routing-guided steering 方法论来源。论文发现 MoE 路由与语系对齐，早/晚层支持语言特定处理，中间层作为语言无关的 capacity hub。提出 routing-guided steering 方法改善低资源语言性能。\n   - 该论文确实存在且描述准确。\n\n3. Cross-Lingual Prompt Steerability (arXiv:2512.02841, 2025 年 12 月):\n   - 系统研究了 system prompt 在跨语言设置下的效果。发现英语调优的 prompt 迁移到非英语任务时性能退化，CoT/emotion/scenario 等组件与多语言鲁棒性相关。\n   - **与本 proposal 高度相关但未被引用**——该工作直接研究了 prompt 策略的跨语言泛化问题。\n\n4. \"When Can LLMs Actually Correct Their Own Mistakes?\" (TACL 2025):\n   - 自纠正领域的权威综述。核心结论：LLM 在无外部反馈时难以有效自纠正。提供了理解自纠正成败条件的框架。\n\n5. \"Large Language Models Cannot Self-Correct Reasoning Yet\" (ICLR 2025):\n   - Huang & Chen 的开创性工作，证明 intrinsic self-correction 在推理任务中基本失败。这是自纠正领域的基石论文。\n\n6. 多语言性能差距研究 (多篇 2024-2026):\n   - SAHARA benchmark (517 非洲语言), EMCee (2025), Cross-Lingual-Thought Prompting 等。共识是多语言性能差距显著且持续，但均聚焦 base task accuracy，未专门研究自纠正能力的跨语言差异。\n\n- **调研总结**: LLM 自纠正是一个活跃但竞争激烈的领域，\"自纠正在英语以外的表现\"确实是一个文献空白。但核心前驱工作（Self-Correction Bench）仅是 NeurIPS workshop paper，且\"extend to multilingual\"是 NLP 领域公认的增量性研究模式。该 proposal 处于\"已知空白但增量风险高\"的位置。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。**\n\n最直接的低成本替代方案是：直接将 Self-Correction Bench 的英文测试数据翻译成多种语言（用 GPT-4 翻译或人工翻译），然后在翻译后的版本上跑现有评测管线。这个方法不需要构建新 benchmark（X-CorrectBench），也不需要 CGA 的统计框架——只需报告各语言的 blind spot 率并做简单比较即可得到\"自纠正跨语言退化\"的核心发现。\n\n**Proposal 的增量价值在于三点**：\n(a) CGA 的 mixed-effects regression 框架（β > 1 的 super-linear 假设）提供了比简单比较更精确的刻画——但这是统计方法上的改进，不是概念上的突破；\n(b) \"Wait\" prompt 的跨语言泛化测试确实无法通过简单翻译 benchmark 获得——这是真正的 novelty delta；\n(c) MoE routing 的 mechanistic analysis 通过 Qwen3 的 MoE/dense 对照提供了有控制的架构比较。\n\n**总结**：核心发现（多语言自纠正退化）可以通过低成本方式大致复现。Proposal 的增量价值集中在统计精细化和几个特定实验（Wait 泛化、MoE 路由分析），但这些更像是\"锦上添花\"而非\"不可替代的贡献\"。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **\"自纠正能力的退化速度快于 base task accuracy 的退化\"（CGA β > 1 假设）**——这是整篇论文的核心 claim，但目前没有任何理论或实证支撑。一个同样合理的反面假设是：自纠正和 base task accuracy 线性耦合（β ≈ 1），因为两者都受训练数据分布影响。如果 β ≤ 1（即 CGA 不成立），论文的核心叙事将失去锚点。Proposal 有 dual-outcome 设计（声称 β ≤ 1 也是有趣发现），但\"差异不显著\"在顶会是很难发表的。\n\n2. **\"Wait\" prompt 的效果是通过 activation amplification 实现的**——Proposal 将这归因于 NeurIPS 2025 的 mechanistic 分析，但实际上 Self-Correction Bench 主要提供了行为层面的证据（blind spot 降低了 89.3%），\"activation amplification\" 的 mechanistic claim 是否有足够的因果证据支撑尚不清楚。在此基础上构建跨语言泛化的假设，存在前提不牢的风险。\n\n3. **Qwen3 MoE/dense 对\"共享 tokenizer 和训练数据\"的假设**——Proposal 声称这对模型可以做\"controlled architecture comparison\"。但实际上，即使 tokenizer 和训练数据集相同，MoE 和 dense 模型在训练过程中的 loss landscape、梯度动态等完全不同，\"controlled comparison\"的因果推断力有限。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中（偏弱）**\n   - 核心贡献模式是\"将 X 扩展到多语言\"——Self-Correction Bench → X-CorrectBench。这是 NLP 领域最常见的增量研究模式之一。\n   - 更关键的是，前驱工作（Self-Correction Bench, arXiv:2507.02778）本身只是 NeurIPS workshop paper，尚未在顶级主会确立。在 workshop paper 基础上做多语言扩展，novelty bar 更难满足。\n   - CGA 的 mixed-effects regression 框架（β > 1）在方法论上有一定新意，但本质是标准统计方法在新设置下的应用。\n   - \"Wait\" prompt 跨语言泛化测试是最有 novelty 的单点贡献，但它在整篇论文中只占一个实验维度。\n   - Cross-Lingual Prompt Steerability（arXiv:2512.02841）已经研究了 prompt 策略的跨语言泛化，虽然未专门针对 correction trigger，但研究范式相似。\n   - **支撑**：Self-Correction Bench（workshop paper）是直接前驱；Cross-Lingual Prompt Steerability 已探索 prompt 跨语言泛化；\"extend to multilingual\"是公认的增量模式。\n\n2. **Significance: 中**\n   - 多语言公平性是 NLP 领域的重要议题，\"自纠正跨语言差异\"确实是一个有实际意义的空白。\n   - 但影响力取决于核心发现是否 surprising。如果 CGA 成立（β > 1），审稿人可能会说\"this makes sense — harder tasks are harder to self-correct, and self-correction is a higher-order capability that amplifies base deficits\"。这不算反直觉。如果 CGA 不成立，negative result 更难发表。\n   - 实际影响有限：发现问题（disparity exists）比解决问题更容易，而 proposal 主要贡献在诊断而非解决方案。\n   - **支撑**：SAHARA benchmark、EMCee、多项 2024-2025 工作都已在记录多语言差距，本工作是在自纠正维度的补充，但不改变领域格局。\n\n3. **Related Work: 中**\n   - 正确引用了核心前驱工作（Self-Correction Bench, arXiv:2601.14050），关键论文确实存在。\n   - **但存在明显遗漏**：Cross-Lingual Prompt Steerability（arXiv:2512.02841）直接研究了 prompt 跨语言泛化，与 \"Wait\" prompt 泛化实验高度相关但未被引用。\"When Can LLMs Actually Correct Their Own Mistakes?\"（TACL 2025）和 \"Large Language Models Cannot Self-Correct Reasoning Yet\"（ICLR 2025）是自纠正领域的核心论文，proposal 未提及。\n   - Proposal 将 Self-Correction Bench 描述为\"NeurIPS 2025\"而实际是 workshop paper，这属于不准确的归因，审稿人会注意到。\n   - **支撑**：缺少 arXiv:2512.02841 的讨论；缺少 TACL 2025 / ICLR 2025 自纠正综述/核心论文的定位。\n\n---\n\n【概率估计】: 15% - 25%，中位 20%\n\n【估计理由】:\n- **Novelty 是主要限制因素**。\"extend benchmark to multilingual\"是顶会审稿人最常标记为 incremental 的研究模式之一，而且前驱工作仅是 workshop paper。CGA 框架和 Wait 泛化测试提供了一些增量 novelty，但不足以改变整体判断。\n- **Significance 提供了一定支撑**（多语言公平性是重要话题），但核心发现无论正反，审稿人都不太可能觉得 surprising，这限制了上界。\n- **Related work 遗漏**可以修复，但 Self-Correction Bench 的 workshop paper 归因问题可能引起审稿人对作者 rigor 的质疑。\n- 如果投稿 NLP 顶会（ACL/EMNLP/NAACL），20% 是合理中位估计。\n- ⚠️ **严重的额外风险**：Proposal 声明投稿 **CoRL 2026**（Conference on Robot Learning），但内容完全是 NLP/多语言 LLM 评估，与机器人学零相关。CoRL 2026 CFP 明确声明 **\"Submissions without a robotics focus will be returned without review\"**。如果确实投 CoRL，概率接近 0%（desk reject）。本评估的 20% 中位估计是基于假设投稿合适的 NLP 会议。\n\n【主要风险】:\n1. **\"Extend to multilingual\" 增量性风险**：这是 NLP 顶会审稿人最敏感的批评之一。核心贡献被视为对一篇 workshop paper 的多语言翻版，novelty 不足以支撑主会投稿。\n2. **核心假设（CGA β > 1）的\"不意外\"风险**：无论结果正反，审稿人可能认为发现不够 surprising——成立则符合\"higher-order capabilities degrade faster\"的直觉，不成立则是难以发表的 negative result。\n```\n\nSources:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)\n- [NeurIPS 2025 Workshop Poster](https://neurips.cc/virtual/2025/loc/san-diego/122384)\n- [Understanding Multilingualism in MoE LLMs (arXiv:2601.14050)](https://arxiv.org/abs/2601.14050)\n- [Cross-Lingual Prompt Steerability (arXiv:2512.02841)](https://arxiv.org/abs/2512.02841)\n- [When Can LLMs Actually Correct Their Own Mistakes? (TACL 2025)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/)\n- [Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Multilingual AI Gap (TechPolicy.Press)](https://www.techpolicy.press/the-multilingual-ai-gap-is-not-closing-it-is-being-rebranded/)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to make a thorough assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n```\n\n---\n\n## ⚠️ 致命前置问题：投稿 venue 与论文主题完全不匹配\n\n**CoRL (Conference on Robot Learning)** 是机器人学习的顶会，主题涵盖：机器人感知与控制的学习方法、机器人基础模型、模仿学习、强化学习控制物理机器人、机器人操作/导航/运动等。Call for papers 明确鼓励报告真实机器人实验或提供仿真可迁移到真实机器人的证据。\n\n本 proposal 是一篇**纯 NLP/CL 论文**——关于 LLM 多语言自纠错能力的 benchmark + 实证分析——与机器人学习**零相关**。投稿 CoRL 2026 主会，**几乎必然被 desk reject**。\n\n适合的 venue 应为 ACL、EMNLP、NAACL、COLM 等 NLP/CL 会议。**以下评估基于该 idea 在 NLP/CL 顶会的学术质量。**\n\n---\n\n```\n【领域调研】:\n\n1. Self-Correction Bench (arXiv:2507.02778, NeurIPS 2025):\n   - 本 proposal 的直接前置工作。Ken Tsui 等人提出系统性框架评估 LLM 自纠错盲点，\n     测试 14 个模型发现平均 64.5% 盲点率；发现 \"Wait\" prompt 可降低 89.3% 盲点。\n   - 该工作仅在英文上评估，明确提到多语言扩展为 future work。\n   - 关系：本 proposal 本质上是该工作的多语言扩展 + 统计形式化。\n\n2. Understanding Multilingualism in MoE LLMs (arXiv:2601.14050, Jan 2026):\n   - 系统分析 MoE 模型的多语言路由行为和专家特化，\n     提出 routing-guided steering 方法改善多语言性能。\n   - 关系：本 proposal 直接引用其方法论进行 MoE 机制分析。\n\n3. Intrinsic Self-Correction in LLMs: Towards Explainable Prompting \n   via Mechanistic Interpretability (arXiv:2505.11924, 2025):\n   - 从机制可解释性角度分析自纠错为何有效，\n     发现 self-correction 通过沿可解释的潜在方向引导隐表示实现。\n   - 关系：与本 proposal 的 activation amplification 分析方向重叠。\n\n4. MMLU-ProX (arXiv:2503.10497, 2025):\n   - 多语言高级 LLM 评估 benchmark，覆盖多种语言。\n   - 关系：代表了\"将英文 benchmark 扩展到多语言\"这一成熟研究范式。\n\n5. CorrectBench (correctbench.github.io):\n   - 另一个 LLM 自纠错评估 benchmark，从 Task Scenario、\n     Self-Correction Type、LLM Type 三维度评估。\n   - 关系：本 proposal 未提及此竞争性工作。\n\n6. \"When Can LLMs Actually Correct Their Own Mistakes?\" \n   (TACL 2025, arXiv:2406.01297):\n   - 自纠错领域综合 survey，结论：无外部反馈的 intrinsic self-correction\n     目前无法可靠工作，且纠正尝试可能使结果更差。\n   - 关系：本 proposal 研究的自纠错盲点现象在该 survey 已被充分讨论。\n\n7. MuBench (arXiv:2506.19468, 2025):\n   - 覆盖 61 种语言的多语言 LLM 评估，\n     发现声称的语言覆盖与实际性能差距显著。\n   - 关系：代表多语言评估赛道的拥挤程度。\n\n8. Structure Enables Effective Self-Localization of Errors in LLMs \n   (arXiv:2602.02416, Feb 2026):\n   - 近期工作探索结构化方法帮助 LLM 定位自身错误。\n   - 关系：自纠错领域持续有新工作，竞争激烈。\n\n- 调研总结：\n  \"LLM 自纠错\"和\"多语言 LLM 评估\"各自都是活跃赛道。\n  但二者的交叉——\"多语言自纠错评估\"——确实尚无系统性工作。\n  然而本 proposal 的核心方法论（将英文 benchmark 翻译/扩展到多语言并测量 gap）\n  是 NLP 领域非常成熟且竞争激烈的研究范式。\n  Self-Correction Bench 明确将多语言列为 future work，\n  意味着原作者或其他组很可能已在进行类似扩展。\n```\n\n---\n\n```\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁：\n\n1. 最简单的替代方案：直接将 Self-Correction Bench 的英文测试集\n   翻译为其他语言（GPT-4 翻译 + 人工校验），在同样的模型上跑实验，\n   报告跨语言的性能差异。这不需要任何新的 metric 设计，\n   甚至不需要 CGA 形式化——一张表格 + bar chart 即可展示 gap。\n   Self-Correction Bench 原作者自己做这件事的成本极低。\n\n2. CGA 的增量价值：mixed-effects regression 测试 β > 1\n   （correction deficit 是否 super-linearly scale with base deficit）\n   是一个统计形式化，但本质上是在检验一个\"越弱的语言，\n   自纠错退化越严重\"的直觉——这是一个合理但不令人意外的假设。\n   如果结果是 positive（β > 1），审稿人很可能说 \"I would have guessed this\"；\n   如果是 negative（β ≤ 1），结论反而更有趣但 proposal 的叙事会崩塌。\n\n3. \"Wait\" prompt 跨语言测试是最具价值的增量贡献，\n   但即使是这个实验，也是在已知 \"Wait\" 有效的基础上做的自然延伸。\n   且无论结果如何（有效/无效），解释都容易事后合理化。\n\n结论：存在 trivial alternative。本 proposal 的增量价值主要在于：\n(a) 系统性覆盖 12 语言的规模 (b) CGA 的统计形式化 \n(c) \"Wait\" prompt 的跨语言泛化分析。\n但这些增量相对于直接翻译 + 跑实验的 baseline 而言并不 dramatic。\n```\n\n---\n\n```\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的假设：\n\n1. **\"自纠错是一个独立于 base task 的能力维度\"**：\n   CGA 假设的前提是自纠错能力可以与 base task accuracy 解耦度量。\n   但 Self-Correction Bench 的 blind spot 定义本身就依赖于 base accuracy\n   （模型必须先答对 user-input 版本，才能检测 self-generated 版本的盲点）。\n   这意味着在低资源语言中，base accuracy 降低会直接减少可测量 blind spot 的样本数，\n   可能引入 floor effect 导致 CGA 的统计估计不稳定。\n\n2. **\"翻译后的 benchmark 保持等价性\"**：\n   将英文 error injection 翻译为 12 种语言时，\n   错误的\"自然度\"和\"可发现性\"可能因语言而异。\n   例如某些语言的语法错误模式与英文完全不同，\n   简单翻译可能导致 construct validity 问题。\n   MMLU-ProX 等工作已反复指出翻译 benchmark 的系统性偏差\n   （arXiv:2511.05162 \"Mind the Gap\"）。\n\n3. **\"MoE 路由模式差异 = 机制解释\"**：\n   观察到 generation vs. self-correction 阶段的路由模式不同，\n   并不等于理解了为什么自纠错能力退化。\n   相关性 ≠ 因果性，且 MoE routing 的可解释性本身是开放问题。\n\n4. **\"'Wait' prompt 的作用机制可以跨语言迁移\"**：\n   \"Wait\" 在英文中有效可能与其在训练数据中的 context 分布有关\n   （如出现在 chain-of-thought、self-reflection 等上下文中），\n   直接翻译为其他语言的等价词（如中文\"等等\"）\n   不一定携带相同的激活模式。\n   这个假设本 proposal 虽然要检验，但在叙事中已预设了某种\"universality\"。\n```\n\n---\n\n```\n【3 维度打分】:\n\n1. Novelty: 弱 — \n   本 proposal 的核心贡献模式是\"将英文 benchmark 扩展到多语言\"，\n   这是 NLP 领域最常见的增量研究范式之一（参见 MMLU → MMLU-ProX, \n   XTREME, MuBench 等）。具体到自纠错领域，Self-Correction Bench \n   (NeurIPS 2025) 明确将多语言扩展列为 future work，\n   表明这是一个\"显然的下一步\"而非真正的 insight。\n   CGA metric 是合理的统计形式化但不构成概念突破。\n   \"Wait\" prompt 跨语言测试是最有新意的部分，\n   但仍属于\"在已知有效的干预上测试更多条件\"的范畴。\n   此外，本 proposal 未提及同期竞争性工作 CorrectBench，\n   表明对领域覆盖不够全面。\n\n2. Significance: 中 — \n   多语言自纠错确实是一个 underexplored 的交叉方向，\n   对多语言 LLM 的可靠性有实际意义。\n   但核心发现的\"惊喜度\"受限：\n   - 如果 CGA β > 1（自纠错退化 super-linear），这与直觉一致，不 surprising\n   - 如果 CGA β ≤ 1，结论更有趣但 proposal 的叙事框架会受损\n   - \"Wait\" prompt 跨语言结果无论哪个方向都容易被事后解释\n   整体而言，这是一个\"useful but not surprising\"的贡献，\n   适合 Findings 或 workshop，但对主会的 significance bar 偏弱。\n\n3. Related Work: 弱 — \n   - 未提及 CorrectBench（直接竞争性 benchmark）\n   - 未讨论 \"When Can LLMs Actually Correct Their Own Mistakes?\"\n     (TACL 2025) 这个领域最重要的 survey\n   - 未讨论 arXiv:2505.11924 (Intrinsic Self-Correction \n     via Mechanistic Interpretability) 对 \"Wait\" 机制的解释\n   - 多语言评估方面未提及 MMLU-ProX, MuBench 等直接可比的范式\n   - 对 arXiv:2511.05162 \"Mind the Gap\" \n     提出的翻译 benchmark 偏差问题未做讨论\n   存在较明显的 related work 盲区，\n   审稿人很可能指出\"你是否知道 X 已经做了类似的事\"。\n```\n\n---\n\n```\n【概率估计】: [15% - 25%] 中位 20%\n（注：此概率为投稿 NLP/CL 顶会（如 ACL/EMNLP）的估计。\n  投稿 CoRL 2026 的中稿概率约为 0-2%，因主题完全不在 scope 内。）\n\n【估计理由】:\nNovelty 是主要限制因素——\"将英文 benchmark 扩展到多语言\"的范式\n在 NLP 社区已高度饱和，审稿人对此类工作的 novelty bar 很高。\nCGA metric 和 \"Wait\" prompt 跨语言测试提供了一定的差异化，\n使其不完全是机械翻译+重复实验，但增量 novelty 不足以跨越\n\"benchmark extension paper\"的认知标签。\nSignificance 维度处于中等——问题本身有价值但预期发现不够 surprising。\nRelated work 的盲区会被审稿人注意到，进一步降低分数。\n如果实验执行得非常出色（大规模、严谨的统计分析、\n意外发现），有可能进入 25-30% 区间（Findings track）；\n但 idea 本身的天花板决定了主会 oral/poster 的概率偏低。\n\n【主要风险】:\n1. **\"Obvious next step\" 质疑**：Self-Correction Bench 原论文已将多语言\n   列为 future work，审稿人很可能认为这是一个执行层面的扩展\n   而非 conceptual contribution，导致 novelty 评分低。\n2. **核心发现的\"惊喜度\"不足**：CGA 的两种结果（β > 1 或 β ≤ 1）\n   都面临 \"so what\" 风险——前者符合直觉不 surprising，\n   后者虽 surprising 但与 proposal 的叙事框架矛盾。\n```\n\n---\n\n**额外强调**：本 proposal 投稿 **CoRL 2026** 是一个根本性的 venue 选择错误。CoRL 的 scope 是机器人学习，本论文与机器人完全无关。建议改投 ACL 2026、EMNLP 2026、NAACL 2026 或 COLM 2026 等 NLP/CL 会议。\n\nSources:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778v2)\n- [NeurIPS 2025 Self-Correction Bench](https://neurips.cc/virtual/2025/loc/san-diego/122384)\n- [Understanding Multilingualism in MoE LLMs (arXiv:2601.14050)](https://arxiv.org/abs/2601.14050)\n- [Intrinsic Self-Correction via Mechanistic Interpretability (arXiv:2505.11924)](https://arxiv.org/abs/2505.11924)\n- [MMLU-ProX (arXiv:2503.10497)](https://arxiv.org/abs/2503.10497)\n- [CorrectBench](https://correctbench.github.io/)\n- [When Can LLMs Actually Correct Their Own Mistakes? (TACL 2025)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes)\n- [MuBench (arXiv:2506.19468)](https://arxiv.org/pdf/2506.19468)\n- [Mind the Gap (arXiv:2511.05162)](https://arxiv.org/pdf/2511.05162)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Structure Enables Self-Localization of Errors (arXiv:2602.02416)](https://arxiv.org/pdf/2602.02416)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Cross-Lingual Self-Correction Disparity: Disproportionate Blind Spot Amplification and the Universality of Correction Triggers\n\n## Description\nSelf-correction is critical for LLM reliability, yet all benchmarks evaluate only English. We introduce X-CorrectBench, the first systematic evaluation of self-correction blind spots across 12 typologically diverse languages spanning 10 language families and 8 writing systems. Beyond benchmarking, we test a non-trivial hypothesis: self-correction capability degrades *disproportionately* worse than base task accuracy across languages (Correction Gap Amplification), formalized via mixed-effects regression testing whether correction deficit scales super-linearly (β > 1) with base deficit across 144 (language, model, task) observations. We evaluate 4 frontier models via API (Qwen3-235B, Gemini 2.0 Flash, GPT-4o, Claude Sonnet 4) and perform mechanistic analysis on 3 open-weight models (Gemma 4 31B Dense, Qwen3-30B-A3B, Qwen3-32B) — where the Qwen3 MoE/dense pair shares identical tokenizer and training data, enabling controlled architecture comparison. Building on routing-guided steering methodology (arXiv:2601.14050), we compare routing patterns during generation vs. self-correction phases. Our highest-novelty contribution tests whether the 'Wait' prompt — which reduces English blind spots by 89.3% and operates via activation amplification (NeurIPS 2025) — generalizes across languages, comparing English triggers, native-language equivalents, and language-neutral tokens. We provide the first empirical map of multilingual self-correction disparities, a statistically rigorous CGA metric with bootstrap confidence intervals and power analysis, and evidence for whether correction triggers are universal or language-mediated.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:29:16.790Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:29:16.790Z",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:29:16.804Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile my evaluation.

---

```
【阶段】: Triage

⚠️ 【关键提醒：严重的 Venue Mismatch】
本 proposal 是一篇纯 NLP/多语言 LLM 评估论文，与 CoRL（Conference on Robot Learning）的 scope 完全不匹配。CoRL 聚焦于机器人学习（manipulation, navigation, sim-to-real, robot perception 等），本文没有任何机器人相关内容。投稿 CoRL 极大概率 desk reject。建议目标会议改为 ACL / EMNLP / NAACL / COLM 等 NLP venue。以下评估基于该 idea 在**合适的 NLP venue**（如 ACL/EMNLP 主会）的质量，供参考。

【领域调研】:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778) (NeurIPS 2025 Workshop Poster, 非主会): 本 proposal 的直接前驱工作。提出"self-correction blind spot"概念，在 14 个开源模型上发现平均 64.5% 盲区率，"Wait" prompt 可降低 89.3% 盲区。注意：proposal 中称其为"NeurIPS 2025"，实际为 **LLM Evaluation Workshop poster**，非主会论文，这一描述可能被审稿人视为 misleading。
- [Large Language Models Cannot Self-Correct Reasoning Yet (arXiv:2310.01798)](https://arxiv.org/abs/2310.01798) (ICLR 2024): 开创性工作，论证 LLM 在无外部反馈时无法有效自我纠正推理。Proposal 未显式引用此关键工作。
- [When Can LLMs Actually Correct Their Own Mistakes? (arXiv:2406.01297)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713) (TACL 2024/2025): 综合 survey，系统梳理 self-correction 成功的条件。Proposal 未引用。
- [Understanding Multilingualism in MoE LLMs (arXiv:2601.14050)](https://arxiv.org/abs/2601.14050) (2026.01): Proposal 直接引用。研究 MoE 模型的多语言路由机制和专家特化。提出 routing-guided steering 方法。论文真实存在，描述基本准确。
- [MMLU-ProX (arXiv:2503.10497)](https://arxiv.org/abs/2503.10497) (EMNLP 2025): 29 语言多语言 benchmark，文档了高达 24.3% 的跨语言性能差距。Proposal 未引用此直接相关的多语言评估工作。
- [MM-EVAL (arXiv:2410.17578)](https://arxiv.org/abs/2410.17578): 覆盖 18 语言的多语言 meta-evaluation benchmark。
- [Cross-Lingual Auto Evaluation (arXiv:2410.13394)](https://arxiv.org/abs/2410.13394) (ACL 2025): 6 语言的跨语言评估框架。
- [Steering MoE LLMs via Expert (De)Activation (arXiv:2509.09660)](https://arxiv.org/abs/2509.09660): MoE 专家激活/去激活转向方法，与 proposal 的 MoE 机制分析相关。

- **调研总结**: 多语言 LLM 评估（MMLU-ProX, BenchMAX, GlotEval 等）和 LLM self-correction（Self-Correction Bench, "Cannot Self-Correct" 等）各自是活跃的研究方向，但二者的**交叉领域——跨语言 self-correction 评估——确实尚无直接前驱工作**。这构成一个真实的研究空白。然而，这个空白之所以存在，部分原因可能是结果过于可预测（已知：LLM 在非英语上一切都更差 + self-correction 本身就脆弱 → 非英语 self-correction 更差，这是 trivially expected）。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁：
1. **直接翻译 Self-Correction Bench 到多语言**：无需 CGA 公式化，直接在 12 种语言上跑原始 benchmark，报告各语言的盲区率。这个 trivial 版本能覆盖 proposal ~40% 的贡献。
2. **核心发现的可预测性**："非英语语言的 self-correction 更差"几乎是 trivially expected。已有大量工作（MMLU-ProX 等）证明 LLM 在非英语上的所有能力都更差，self-correction 不太可能是例外。

**增量价值所在**：
- CGA 假设（β > 1，超线性退化）是非 trivial 的——线性退化是 expected，但超线性退化（即 self-correction 的退化比基础能力退化更严重）如果成立，有安全/对齐领域的重要含义（多语言安全差距比能力差距更大）。
- "Wait" prompt 的跨语言泛化性是一个genuinely interesting 的问题——英文单 token 触发器是否在非拉丁字母语言中也有效？
- MoE 路由在 generation vs. self-correction 阶段的差异分析是 novel 的机制层面贡献。

但总体而言，增量价值主要来自分析的*深度和方法论*，而非*核心发现的surprise factor*。

【前提假设检验】:
核心 claim 的逻辑链中存在以下未经验证的假设：

1. **"Wait" prompt 的可靠性假设**：proposal 将 "Wait" 的 89.3% 盲区降低效果视为 established fact 并在其上构建 cross-lingual 扩展。但原始发现来自一篇 **NeurIPS workshop poster**（非主会），在学术严谨性上尚未经过顶会主会级别的同行评审验证。如果 "Wait" 的效果在更严格的评估下不如报告的那么强，本文最高 novelty 的贡献（"Wait" 跨语言泛化性）的基础就会动摇。

2. **CGA 的前提假设**：β > 1（超线性退化）假设的成立依赖于 self-correction 比 base accuracy 有"额外的"语言敏感性。但自我纠正本质上需要更强的元认知能力，而元认知能力在低资源语言中可能本身就更弱——这可能只是 meta-cognitive ability 整体下降的自然推论，而非 self-correction 特有的现象。换言之，β > 1 可能只是反映了"困难任务在弱语言上退化更快"的通用规律，而非 self-correction 的特殊性。

3. **Qwen3 MoE/Dense "controlled comparison" 假设**：proposal 声称 Qwen3-30B-A3B (MoE) 和 Qwen3-32B (Dense) "shares identical tokenizer and training data, enabling controlled architecture comparison"。但即使 tokenizer 和训练数据相同，模型容量（active parameters 差异巨大：3B vs 32B）、训练 dynamics、收敛行为等都不同，将其简单视为"仅架构不同"的 controlled comparison 过于简化。

4. **"Correction triggers are universal or language-mediated" 的二元框架**：这一 framing 假设 correction 触发机制要么是 universal 要么是 language-mediated，但现实可能更复杂——可能因任务类型、错误类型、模型而异，而非简单的二元。

【3 维度打分】:

1. **Novelty: 中** — 
   理由：跨语言 self-correction 评估这一交叉方向确实无直接前驱（调研中未找到任何专门评估多语言 self-correction blind spot 的工作），这是真实的 novelty。CGA 公式化（β > 1 超线性假设）和 "Wait" prompt 跨语言泛化性测试都超越了简单的 benchmark 翻译。然而，核心方向是两个已有方向（多语言评估 + self-correction 评估）的直接组合，属于"显而易见但没人做"的类型。Self-Correction Bench (arXiv:2507.02778) 的多语言扩展是最自然的 next step，审稿人容易将其视为 incremental extension。最核心的 surprise factor 取决于实验结果——如果 β ≈ 1（线性退化），novelty 大打折扣；如果 "Wait" 在非英语上完全失效或完全有效，都各有其价值但可预测性不同。

2. **Significance: 中** — 
   理由：研究问题本身有实际意义——如果 self-correction 在非英语中退化比 base accuracy 更严重，这对多语言 AI safety 和 alignment 有直接影响。但需诚实评估：(a) 多语言 LLM 评估领域已有大量 benchmark（MMLU-ProX 等已在 29 语言上系统评估），再增加一个 self-correction 维度是有价值但非变革性的；(b) 核心发现如果是 positive（"是的，非英语 self-correction 更差，且 disproportionately 更差"），大多数审稿人的反应可能是 "I would have guessed this" 而非 "surprising"；(c) 对 robotics 领域（CoRL）的 significance 为零。对 NLP 领域，这是一个 useful empirical contribution，但不是那种改变研究方向的工作。

3. **Related Work: 中偏弱** — 
   理由：proposal 引用了 Self-Correction Bench 和 arXiv:2601.14050，这两个直接相关引用是准确的。但存在以下显著遗漏：(a) 未引用 Huang & Zhao (ICLR 2024) "Large Language Models Cannot Self-Correct Reasoning Yet"——这是 self-correction 领域最重要的工作之一；(b) 未引用 TACL 2024 的 self-correction 综合 survey；(c) 未引用 MMLU-ProX (EMNLP 2025)——直接相关的 29 语言多语言 benchmark；(d) 将 Self-Correction Bench 描述为 "NeurIPS 2025" 而其实是 workshop poster，可能被视为 misleading。差异化定位（"first systematic evaluation"）在交叉领域成立，但对两个母领域的文献覆盖不够充分。

【概率估计】: [20% - 32%] 中位 25%
（注：此估计基于投稿**合适的 NLP venue**如 ACL/EMNLP 主会。若投稿 CoRL，中稿概率估计为 0-3%，因为完全 out of scope。）

【估计理由】: 
idea 处于"方向正确、有真实 novelty delta，但核心发现 predictable"的区间。三个维度均为中等水平，没有致命缺陷但也没有突出亮点。Novelty 的上限被"两个已有方向的显而易见组合"所限制——即使 CGA 和 "Wait" 泛化测试提供了超越 trivial extension 的深度，审稿人仍可能认为这是 Self-Correction Bench 的自然多语言扩展。Significance 的上限被核心发现的可预测性限制——"非英语 self-correction 更差"不会让人 surprised。如果实验中 β 显著 > 1 或 "Wait" 表现出 counter-intuitive 的跨语言模式，可以 push 到上界 32%；如果 β ≈ 1 且 "Wait" 效果线性下降，则在下界 20% 附近。

【主要风险】: 
1. **"I would have guessed this" 风险**：核心发现（非英语 self-correction 更差，且 disproportionately 更差）高度可预测。审稿人可能认为这是 well-known multilingual performance gap 在又一个维度上的确认，缺乏 genuine surprise。除非 "Wait" 泛化性测试产生 counter-intuitive 结果（例如非英语语言等价触发词反而比 "Wait" 更有效，或 "Wait" 在某些语言家族完全失效而在另一些完全保留），否则 story 缺乏记忆点。
2. **Incremental extension 风险**：论文的最大 novelty 来源——Self-Correction Bench 本身——仅是 NeurIPS workshop poster 级别的工作，尚未被顶会主会认可。在此基础上做多语言扩展，审稿人可能质疑"基础工作本身的成熟度是否足以支撑扩展"。此外，proposal 将 workshop poster 描述为 "NeurIPS 2025" 可能引发审稿人对学术诚信的 concern。
```

Sources:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)
- [Self-Correction Bench at NeurIPS 2025 Workshop](https://openreview.net/forum?id=dLz0bnmL2r)
- [Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)](https://arxiv.org/abs/2310.01798)
- [When Can LLMs Actually Correct Their Own Mistakes? (TACL Survey)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177)
- [Understanding Multilingualism in MoE LLMs (arXiv:2601.14050)](https://arxiv.org/abs/2601.14050)
- [MMLU-ProX (EMNLP 2025)](https://arxiv.org/abs/2503.10497)
- [Cross-Lingual Auto Evaluation (ACL 2025)](https://arxiv.org/abs/2410.13394)
- [Steering MoE LLMs via Expert (De)Activation](https://arxiv.org/abs/2509.09660)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to produce my evaluation. Let me compile the findings.

---

```
【阶段】: Triage

【领域调研】:

1. Self-Correction Bench (arXiv:2507.02778, NeurIPS 2025 Workshop on LLM Evaluation):
   - 这是本 proposal 的直接前驱工作。定义了"Self-Correction Blind Spot"概念，测试了 14 个开源模型，发现平均 64.5% 的 blind spot 率。关键发现："Wait" prompt 可将 blind spot 降低 89.3%。
   - ⚠️ 重要：proposal 描述该工作为"NeurIPS 2025"，但根据调研，它是 NeurIPS 2025 的 **Workshop paper**（LLM Evaluation Workshop），并非主会论文。这一差异影响对 proposal 所构建基础的评估——该 proposal 本质上是对一篇 workshop paper 进行多语言扩展。

2. Understanding Multilingualism in MoE LLMs (arXiv:2601.14050):
   - Proposal 引用的 routing-guided steering 方法论来源。论文发现 MoE 路由与语系对齐，早/晚层支持语言特定处理，中间层作为语言无关的 capacity hub。提出 routing-guided steering 方法改善低资源语言性能。
   - 该论文确实存在且描述准确。

3. Cross-Lingual Prompt Steerability (arXiv:2512.02841, 2025 年 12 月):
   - 系统研究了 system prompt 在跨语言设置下的效果。发现英语调优的 prompt 迁移到非英语任务时性能退化，CoT/emotion/scenario 等组件与多语言鲁棒性相关。
   - **与本 proposal 高度相关但未被引用**——该工作直接研究了 prompt 策略的跨语言泛化问题。

4. "When Can LLMs Actually Correct Their Own Mistakes?" (TACL 2025):
   - 自纠正领域的权威综述。核心结论：LLM 在无外部反馈时难以有效自纠正。提供了理解自纠正成败条件的框架。

5. "Large Language Models Cannot Self-Correct Reasoning Yet" (ICLR 2025):
   - Huang & Chen 的开创性工作，证明 intrinsic self-correction 在推理任务中基本失败。这是自纠正领域的基石论文。

6. 多语言性能差距研究 (多篇 2024-2026):
   - SAHARA benchmark (517 非洲语言), EMCee (2025), Cross-Lingual-Thought Prompting 等。共识是多语言性能差距显著且持续，但均聚焦 base task accuracy，未专门研究自纠正能力的跨语言差异。

- **调研总结**: LLM 自纠正是一个活跃但竞争激烈的领域，"自纠正在英语以外的表现"确实是一个文献空白。但核心前驱工作（Self-Correction Bench）仅是 NeurIPS workshop paper，且"extend to multilingual"是 NLP 领域公认的增量性研究模式。该 proposal 处于"已知空白但增量风险高"的位置。

---

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

最直接的低成本替代方案是：直接将 Self-Correction Bench 的英文测试数据翻译成多种语言（用 GPT-4 翻译或人工翻译），然后在翻译后的版本上跑现有评测管线。这个方法不需要构建新 benchmark（X-CorrectBench），也不需要 CGA 的统计框架——只需报告各语言的 blind spot 率并做简单比较即可得到"自纠正跨语言退化"的核心发现。

**Proposal 的增量价值在于三点**：
(a) CGA 的 mixed-effects regression 框架（β > 1 的 super-linear 假设）提供了比简单比较更精确的刻画——但这是统计方法上的改进，不是概念上的突破；
(b) "Wait" prompt 的跨语言泛化测试确实无法通过简单翻译 benchmark 获得——这是真正的 novelty delta；
(c) MoE routing 的 mechanistic analysis 通过 Qwen3 的 MoE/dense 对照提供了有控制的架构比较。

**总结**：核心发现（多语言自纠正退化）可以通过低成本方式大致复现。Proposal 的增量价值集中在统计精细化和几个特定实验（Wait 泛化、MoE 路由分析），但这些更像是"锦上添花"而非"不可替代的贡献"。

---

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **"自纠正能力的退化速度快于 base task accuracy 的退化"（CGA β > 1 假设）**——这是整篇论文的核心 claim，但目前没有任何理论或实证支撑。一个同样合理的反面假设是：自纠正和 base task accuracy 线性耦合（β ≈ 1），因为两者都受训练数据分布影响。如果 β ≤ 1（即 CGA 不成立），论文的核心叙事将失去锚点。Proposal 有 dual-outcome 设计（声称 β ≤ 1 也是有趣发现），但"差异不显著"在顶会是很难发表的。

2. **"Wait" prompt 的效果是通过 activation amplification 实现的**——Proposal 将这归因于 NeurIPS 2025 的 mechanistic 分析，但实际上 Self-Correction Bench 主要提供了行为层面的证据（blind spot 降低了 89.3%），"activation amplification" 的 mechanistic claim 是否有足够的因果证据支撑尚不清楚。在此基础上构建跨语言泛化的假设，存在前提不牢的风险。

3. **Qwen3 MoE/dense 对"共享 tokenizer 和训练数据"的假设**——Proposal 声称这对模型可以做"controlled architecture comparison"。但实际上，即使 tokenizer 和训练数据集相同，MoE 和 dense 模型在训练过程中的 loss landscape、梯度动态等完全不同，"controlled comparison"的因果推断力有限。

---

【3 维度打分】:

1. **Novelty: 弱-中（偏弱）**
   - 核心贡献模式是"将 X 扩展到多语言"——Self-Correction Bench → X-CorrectBench。这是 NLP 领域最常见的增量研究模式之一。
   - 更关键的是，前驱工作（Self-Correction Bench, arXiv:2507.02778）本身只是 NeurIPS workshop paper，尚未在顶级主会确立。在 workshop paper 基础上做多语言扩展，novelty bar 更难满足。
   - CGA 的 mixed-effects regression 框架（β > 1）在方法论上有一定新意，但本质是标准统计方法在新设置下的应用。
   - "Wait" prompt 跨语言泛化测试是最有 novelty 的单点贡献，但它在整篇论文中只占一个实验维度。
   - Cross-Lingual Prompt Steerability（arXiv:2512.02841）已经研究了 prompt 策略的跨语言泛化，虽然未专门针对 correction trigger，但研究范式相似。
   - **支撑**：Self-Correction Bench（workshop paper）是直接前驱；Cross-Lingual Prompt Steerability 已探索 prompt 跨语言泛化；"extend to multilingual"是公认的增量模式。

2. **Significance: 中**
   - 多语言公平性是 NLP 领域的重要议题，"自纠正跨语言差异"确实是一个有实际意义的空白。
   - 但影响力取决于核心发现是否 surprising。如果 CGA 成立（β > 1），审稿人可能会说"this makes sense — harder tasks are harder to self-correct, and self-correction is a higher-order capability that amplifies base deficits"。这不算反直觉。如果 CGA 不成立，negative result 更难发表。
   - 实际影响有限：发现问题（disparity exists）比解决问题更容易，而 proposal 主要贡献在诊断而非解决方案。
   - **支撑**：SAHARA benchmark、EMCee、多项 2024-2025 工作都已在记录多语言差距，本工作是在自纠正维度的补充，但不改变领域格局。

3. **Related Work: 中**
   - 正确引用了核心前驱工作（Self-Correction Bench, arXiv:2601.14050），关键论文确实存在。
   - **但存在明显遗漏**：Cross-Lingual Prompt Steerability（arXiv:2512.02841）直接研究了 prompt 跨语言泛化，与 "Wait" prompt 泛化实验高度相关但未被引用。"When Can LLMs Actually Correct Their Own Mistakes?"（TACL 2025）和 "Large Language Models Cannot Self-Correct Reasoning Yet"（ICLR 2025）是自纠正领域的核心论文，proposal 未提及。
   - Proposal 将 Self-Correction Bench 描述为"NeurIPS 2025"而实际是 workshop paper，这属于不准确的归因，审稿人会注意到。
   - **支撑**：缺少 arXiv:2512.02841 的讨论；缺少 TACL 2025 / ICLR 2025 自纠正综述/核心论文的定位。

---

【概率估计】: 15% - 25%，中位 20%

【估计理由】:
- **Novelty 是主要限制因素**。"extend benchmark to multilingual"是顶会审稿人最常标记为 incremental 的研究模式之一，而且前驱工作仅是 workshop paper。CGA 框架和 Wait 泛化测试提供了一些增量 novelty，但不足以改变整体判断。
- **Significance 提供了一定支撑**（多语言公平性是重要话题），但核心发现无论正反，审稿人都不太可能觉得 surprising，这限制了上界。
- **Related work 遗漏**可以修复，但 Self-Correction Bench 的 workshop paper 归因问题可能引起审稿人对作者 rigor 的质疑。
- 如果投稿 NLP 顶会（ACL/EMNLP/NAACL），20% 是合理中位估计。
- ⚠️ **严重的额外风险**：Proposal 声明投稿 **CoRL 2026**（Conference on Robot Learning），但内容完全是 NLP/多语言 LLM 评估，与机器人学零相关。CoRL 2026 CFP 明确声明 **"Submissions without a robotics focus will be returned without review"**。如果确实投 CoRL，概率接近 0%（desk reject）。本评估的 20% 中位估计是基于假设投稿合适的 NLP 会议。

【主要风险】:
1. **"Extend to multilingual" 增量性风险**：这是 NLP 顶会审稿人最敏感的批评之一。核心贡献被视为对一篇 workshop paper 的多语言翻版，novelty 不足以支撑主会投稿。
2. **核心假设（CGA β > 1）的"不意外"风险**：无论结果正反，审稿人可能认为发现不够 surprising——成立则符合"higher-order capabilities degrade faster"的直觉，不成立则是难以发表的 negative result。
```

Sources:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)
- [NeurIPS 2025 Workshop Poster](https://neurips.cc/virtual/2025/loc/san-diego/122384)
- [Understanding Multilingualism in MoE LLMs (arXiv:2601.14050)](https://arxiv.org/abs/2601.14050)
- [Cross-Lingual Prompt Steerability (arXiv:2512.02841)](https://arxiv.org/abs/2512.02841)
- [When Can LLMs Actually Correct Their Own Mistakes? (TACL 2025)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/)
- [Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Multilingual AI Gap (TechPolicy.Press)](https://www.techpolicy.press/the-multilingual-ai-gap-is-not-closing-it-is-being-rebranded/)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to make a thorough assessment. Let me compile the evaluation.

---

```
【阶段】: Triage
```

---

## ⚠️ 致命前置问题：投稿 venue 与论文主题完全不匹配

**CoRL (Conference on Robot Learning)** 是机器人学习的顶会，主题涵盖：机器人感知与控制的学习方法、机器人基础模型、模仿学习、强化学习控制物理机器人、机器人操作/导航/运动等。Call for papers 明确鼓励报告真实机器人实验或提供仿真可迁移到真实机器人的证据。

本 proposal 是一篇**纯 NLP/CL 论文**——关于 LLM 多语言自纠错能力的 benchmark + 实证分析——与机器人学习**零相关**。投稿 CoRL 2026 主会，**几乎必然被 desk reject**。

适合的 venue 应为 ACL、EMNLP、NAACL、COLM 等 NLP/CL 会议。**以下评估基于该 idea 在 NLP/CL 顶会的学术质量。**

---

```
【领域调研】:

1. Self-Correction Bench (arXiv:2507.02778, NeurIPS 2025):
   - 本 proposal 的直接前置工作。Ken Tsui 等人提出系统性框架评估 LLM 自纠错盲点，
     测试 14 个模型发现平均 64.5% 盲点率；发现 "Wait" prompt 可降低 89.3% 盲点。
   - 该工作仅在英文上评估，明确提到多语言扩展为 future work。
   - 关系：本 proposal 本质上是该工作的多语言扩展 + 统计形式化。

2. Understanding Multilingualism in MoE LLMs (arXiv:2601.14050, Jan 2026):
   - 系统分析 MoE 模型的多语言路由行为和专家特化，
     提出 routing-guided steering 方法改善多语言性能。
   - 关系：本 proposal 直接引用其方法论进行 MoE 机制分析。

3. Intrinsic Self-Correction in LLMs: Towards Explainable Prompting 
   via Mechanistic Interpretability (arXiv:2505.11924, 2025):
   - 从机制可解释性角度分析自纠错为何有效，
     发现 self-correction 通过沿可解释的潜在方向引导隐表示实现。
   - 关系：与本 proposal 的 activation amplification 分析方向重叠。

4. MMLU-ProX (arXiv:2503.10497, 2025):
   - 多语言高级 LLM 评估 benchmark，覆盖多种语言。
   - 关系：代表了"将英文 benchmark 扩展到多语言"这一成熟研究范式。

5. CorrectBench (correctbench.github.io):
   - 另一个 LLM 自纠错评估 benchmark，从 Task Scenario、
     Self-Correction Type、LLM Type 三维度评估。
   - 关系：本 proposal 未提及此竞争性工作。

6. "When Can LLMs Actually Correct Their Own Mistakes?" 
   (TACL 2025, arXiv:2406.01297):
   - 自纠错领域综合 survey，结论：无外部反馈的 intrinsic self-correction
     目前无法可靠工作，且纠正尝试可能使结果更差。
   - 关系：本 proposal 研究的自纠错盲点现象在该 survey 已被充分讨论。

7. MuBench (arXiv:2506.19468, 2025):
   - 覆盖 61 种语言的多语言 LLM 评估，
     发现声称的语言覆盖与实际性能差距显著。
   - 关系：代表多语言评估赛道的拥挤程度。

8. Structure Enables Effective Self-Localization of Errors in LLMs 
   (arXiv:2602.02416, Feb 2026):
   - 近期工作探索结构化方法帮助 LLM 定位自身错误。
   - 关系：自纠错领域持续有新工作，竞争激烈。

- 调研总结：
  "LLM 自纠错"和"多语言 LLM 评估"各自都是活跃赛道。
  但二者的交叉——"多语言自纠错评估"——确实尚无系统性工作。
  然而本 proposal 的核心方法论（将英文 benchmark 翻译/扩展到多语言并测量 gap）
  是 NLP 领域非常成熟且竞争激烈的研究范式。
  Self-Correction Bench 明确将多语言列为 future work，
  意味着原作者或其他组很可能已在进行类似扩展。
```

---

```
【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. 最简单的替代方案：直接将 Self-Correction Bench 的英文测试集
   翻译为其他语言（GPT-4 翻译 + 人工校验），在同样的模型上跑实验，
   报告跨语言的性能差异。这不需要任何新的 metric 设计，
   甚至不需要 CGA 形式化——一张表格 + bar chart 即可展示 gap。
   Self-Correction Bench 原作者自己做这件事的成本极低。

2. CGA 的增量价值：mixed-effects regression 测试 β > 1
   （correction deficit 是否 super-linearly scale with base deficit）
   是一个统计形式化，但本质上是在检验一个"越弱的语言，
   自纠错退化越严重"的直觉——这是一个合理但不令人意外的假设。
   如果结果是 positive（β > 1），审稿人很可能说 "I would have guessed this"；
   如果是 negative（β ≤ 1），结论反而更有趣但 proposal 的叙事会崩塌。

3. "Wait" prompt 跨语言测试是最具价值的增量贡献，
   但即使是这个实验，也是在已知 "Wait" 有效的基础上做的自然延伸。
   且无论结果如何（有效/无效），解释都容易事后合理化。

结论：存在 trivial alternative。本 proposal 的增量价值主要在于：
(a) 系统性覆盖 12 语言的规模 (b) CGA 的统计形式化 
(c) "Wait" prompt 的跨语言泛化分析。
但这些增量相对于直接翻译 + 跑实验的 baseline 而言并不 dramatic。
```

---

```
【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的假设：

1. **"自纠错是一个独立于 base task 的能力维度"**：
   CGA 假设的前提是自纠错能力可以与 base task accuracy 解耦度量。
   但 Self-Correction Bench 的 blind spot 定义本身就依赖于 base accuracy
   （模型必须先答对 user-input 版本，才能检测 self-generated 版本的盲点）。
   这意味着在低资源语言中，base accuracy 降低会直接减少可测量 blind spot 的样本数，
   可能引入 floor effect 导致 CGA 的统计估计不稳定。

2. **"翻译后的 benchmark 保持等价性"**：
   将英文 error injection 翻译为 12 种语言时，
   错误的"自然度"和"可发现性"可能因语言而异。
   例如某些语言的语法错误模式与英文完全不同，
   简单翻译可能导致 construct validity 问题。
   MMLU-ProX 等工作已反复指出翻译 benchmark 的系统性偏差
   （arXiv:2511.05162 "Mind the Gap"）。

3. **"MoE 路由模式差异 = 机制解释"**：
   观察到 generation vs. self-correction 阶段的路由模式不同，
   并不等于理解了为什么自纠错能力退化。
   相关性 ≠ 因果性，且 MoE routing 的可解释性本身是开放问题。

4. **"'Wait' prompt 的作用机制可以跨语言迁移"**：
   "Wait" 在英文中有效可能与其在训练数据中的 context 分布有关
   （如出现在 chain-of-thought、self-reflection 等上下文中），
   直接翻译为其他语言的等价词（如中文"等等"）
   不一定携带相同的激活模式。
   这个假设本 proposal 虽然要检验，但在叙事中已预设了某种"universality"。
```

---

```
【3 维度打分】:

1. Novelty: 弱 — 
   本 proposal 的核心贡献模式是"将英文 benchmark 扩展到多语言"，
   这是 NLP 领域最常见的增量研究范式之一（参见 MMLU → MMLU-ProX, 
   XTREME, MuBench 等）。具体到自纠错领域，Self-Correction Bench 
   (NeurIPS 2025) 明确将多语言扩展列为 future work，
   表明这是一个"显然的下一步"而非真正的 insight。
   CGA metric 是合理的统计形式化但不构成概念突破。
   "Wait" prompt 跨语言测试是最有新意的部分，
   但仍属于"在已知有效的干预上测试更多条件"的范畴。
   此外，本 proposal 未提及同期竞争性工作 CorrectBench，
   表明对领域覆盖不够全面。

2. Significance: 中 — 
   多语言自纠错确实是一个 underexplored 的交叉方向，
   对多语言 LLM 的可靠性有实际意义。
   但核心发现的"惊喜度"受限：
   - 如果 CGA β > 1（自纠错退化 super-linear），这与直觉一致，不 surprising
   - 如果 CGA β ≤ 1，结论更有趣但 proposal 的叙事框架会受损
   - "Wait" prompt 跨语言结果无论哪个方向都容易被事后解释
   整体而言，这是一个"useful but not surprising"的贡献，
   适合 Findings 或 workshop，但对主会的 significance bar 偏弱。

3. Related Work: 弱 — 
   - 未提及 CorrectBench（直接竞争性 benchmark）
   - 未讨论 "When Can LLMs Actually Correct Their Own Mistakes?"
     (TACL 2025) 这个领域最重要的 survey
   - 未讨论 arXiv:2505.11924 (Intrinsic Self-Correction 
     via Mechanistic Interpretability) 对 "Wait" 机制的解释
   - 多语言评估方面未提及 MMLU-ProX, MuBench 等直接可比的范式
   - 对 arXiv:2511.05162 "Mind the Gap" 
     提出的翻译 benchmark 偏差问题未做讨论
   存在较明显的 related work 盲区，
   审稿人很可能指出"你是否知道 X 已经做了类似的事"。
```

---

```
【概率估计】: [15% - 25%] 中位 20%
（注：此概率为投稿 NLP/CL 顶会（如 ACL/EMNLP）的估计。
  投稿 CoRL 2026 的中稿概率约为 0-2%，因主题完全不在 scope 内。）

【估计理由】:
Novelty 是主要限制因素——"将英文 benchmark 扩展到多语言"的范式
在 NLP 社区已高度饱和，审稿人对此类工作的 novelty bar 很高。
CGA metric 和 "Wait" prompt 跨语言测试提供了一定的差异化，
使其不完全是机械翻译+重复实验，但增量 novelty 不足以跨越
"benchmark extension paper"的认知标签。
Significance 维度处于中等——问题本身有价值但预期发现不够 surprising。
Related work 的盲区会被审稿人注意到，进一步降低分数。
如果实验执行得非常出色（大规模、严谨的统计分析、
意外发现），有可能进入 25-30% 区间（Findings track）；
但 idea 本身的天花板决定了主会 oral/poster 的概率偏低。

【主要风险】:
1. **"Obvious next step" 质疑**：Self-Correction Bench 原论文已将多语言
   列为 future work，审稿人很可能认为这是一个执行层面的扩展
   而非 conceptual contribution，导致 novelty 评分低。
2. **核心发现的"惊喜度"不足**：CGA 的两种结果（β > 1 或 β ≤ 1）
   都面临 "so what" 风险——前者符合直觉不 surprising，
   后者虽 surprising 但与 proposal 的叙事框架矛盾。
```

---

**额外强调**：本 proposal 投稿 **CoRL 2026** 是一个根本性的 venue 选择错误。CoRL 的 scope 是机器人学习，本论文与机器人完全无关。建议改投 ACL 2026、EMNLP 2026、NAACL 2026 或 COLM 2026 等 NLP/CL 会议。

Sources:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778v2)
- [NeurIPS 2025 Self-Correction Bench](https://neurips.cc/virtual/2025/loc/san-diego/122384)
- [Understanding Multilingualism in MoE LLMs (arXiv:2601.14050)](https://arxiv.org/abs/2601.14050)
- [Intrinsic Self-Correction via Mechanistic Interpretability (arXiv:2505.11924)](https://arxiv.org/abs/2505.11924)
- [MMLU-ProX (arXiv:2503.10497)](https://arxiv.org/abs/2503.10497)
- [CorrectBench](https://correctbench.github.io/)
- [When Can LLMs Actually Correct Their Own Mistakes? (TACL 2025)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes)
- [MuBench (arXiv:2506.19468)](https://arxiv.org/pdf/2506.19468)
- [Mind the Gap (arXiv:2511.05162)](https://arxiv.org/pdf/2511.05162)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Structure Enables Self-Localization of Errors (arXiv:2602.02416)](https://arxiv.org/pdf/2602.02416)


【原始 proposal（允许参考但不是主要依据）】:
# Cross-Lingual Self-Correction Disparity: Disproportionate Blind Spot Amplification and the Universality of Correction Triggers

## Description
Self-correction is critical for LLM reliability, yet all benchmarks evaluate only English. We introduce X-CorrectBench, the first systematic evaluation of self-correction blind spots across 12 typologically diverse languages spanning 10 language families and 8 writing systems. Beyond benchmarking, we test a non-trivial hypothesis: self-correction capability degrades *disproportionately* worse than base task accuracy across languages (Correction Gap Amplification), formalized via mixed-effects regression testing whether correction deficit scales super-linearly (β > 1) with base deficit across 144 (language, model, task) observations. We evaluate 4 frontier models via API (Qwen3-235B, Gemini 2.0 Flash, GPT-4o, Claude Sonnet 4) and perform mechanistic analysis on 3 open-weight models (Gemma 4 31B Dense, Qwen3-30B-A3B, Qwen3-32B) — where the Qwen3 MoE/dense pair shares identical tokenizer and training data, enabling controlled architecture comparison. Building on routing-guided steering methodology (arXiv:2601.14050), we compare routing patterns during generation vs. self-correction phases. Our highest-novelty contribution tests whether the 'Wait' prompt — which reduces English blind spots by 89.3% and operates via activation amplification (NeurIPS 2025) — generalizes across languages, comparing English triggers, native-language equivalents, and language-neutral tokens. We provide the first empirical map of multilingual self-correction disparities, a statistically rigorous CGA metric with bootstrap confidence intervals and power analysis, and evidence for whether correction triggers are universal or language-mediated.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3a428d34-6594-4a06-a1fd-96bb8f87e9d2",
  "type": "user",
  "uuid": "f6ae9519-5630-4347-bab0-1be6d63b46cf",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:29:16.802Z_

```json
{
  "parentUuid": "f6ae9519-5630-4347-bab0-1be6d63b46cf",
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
  "uuid": "3ad5666e-063b-4aba-b479-41d9b3da4a20",
  "timestamp": "2026-05-20T03:29:16.802Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:29:16.802Z_

```json
{
  "parentUuid": "3ad5666e-063b-4aba-b479-41d9b3da4a20",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "125b48fc-05fd-4a68-b084-85cf674980d8",
  "timestamp": "2026-05-20T03:29:16.802Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research context. Let me compile my eval…",
  "leafUuid": "125b48fc-05fd-4a68-b084-85cf674980d8",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate multilingual LLM self-correction disparities",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:29:53.780Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three reviewer evaluations and synthesize them according to the Meta Judge format.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 中偏弱 (Medium-weak)
- Probability: [20% - 32%] 中位 25%

**Reviewer 2:**
- Novelty: 弱-中（偏弱）(Weak-Medium, leaning weak)


- Significance: 中 (Medium)
- Related Work: 中 (Medium)
- Probability: [15% - 25%] 中位 20%

**Reviewer 3:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 弱 (Weak)
- Probability: [15% - 25%] 中位 20%

Now I'm calculating the standard deviation across the three median probabilities of 25%, 20%, and 20%, which gives me a mean of about 21.67% and a relatively small variance.

The population standard deviation comes out to roughly 2.4%, which is well below the 3% threshold, indicating strong agreement among the reviewers. Now I need to look at where the consensus actually lies and identify any outlier dimensions.

All three reviewers unanimously flagged the venue mismatch with CoRL as a critical issue. They also converge on novelty being weak to medium at best, with the multilingual extension pattern limiting originality. Significance is consistently rated as medium across the board, and there's universal agreement that the core finding—β exceeding 1—is predictable rather than surprising. Additionally, all three caught that the Self-Correction Bench is actually a workshop paper despite how it's presented, and they all noted a trivial alternative exists.

The reviewers also identified a direct translation of Self-Correction Bench as a low-cost workaround. Beyond that, there are substantial gaps in related work: R1 flagged missing references to Huang & Zhao's ICLR 2024 work, a TACL survey, and MMLU-ProX, while R2 pointed out missing Cross-Lingual Prompt Steerability and several 2025 papers, and R3 identified CorrectBench, MuBench, Mind the Gap, and others. All three agree the related work section needs significant expansion. Finally, both R1 and R2 flagged that the Qwen3 MoE versus dense model comparison is oversimplified, with R3 adding concerns about MoE routing correlation.

The "Wait" prompt cross-lingual test stands out as the most novel contribution according to R1 and R2, though R3 views it as incremental. Beyond the consensus issues, R3 raised several unique concerns: the floor effect in low-resource languages limiting measurable blind spot samples, construct validity issues with translation benchmarks, and specific missing references like CorrectBench and the mechanistic interpretability paper. R2 separately highlighted Cross-Lingual Prompt Steerability as a critical missing reference.

Now I'm synthesizing the probability estimates. The three reviewers gave medians of 25%, 20%, and 20%, with very tight consistency (std ≈ 2.4%), so I should anchor to the median neighborhood around 20-21%. The principle is to narrow the interval while respecting the most lenient bound—R1's 25%—and lean toward stricter estimates given the "quality over quantity" principle. This points me toward [17%-27%] with a median of 21%.

Actually, reconsidering the full ranges: the lower bounds cluster at 15-20 (median 15), upper bounds at 25-32 (median 25), and medians at 20-25 (median 20). With such high agreement, I'll settle on [16%-26%] centered at 20%.

Now I need to assess the implementation feasibility. Since this is fundamentally an empirical benchmarking paper, I'm evaluating what's required: API access to four frontier models, plus the infrastructure to run and evaluate them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "125b48fc-05fd-4a68-b084-85cf674980d8",
  "isSidechain": false,
  "requestId": "req_011CbD7T3vKtqM4svXkgQZ4m",
  "type": "assistant",
  "uuid": "ce0d097e-acc1-4649-aefb-04b95096ff92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178RnA7DnDUFERpyhZyrJpB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14604,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4354,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14604
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

_source line 9 · 2026-05-20T03:30:46.699Z_

【阶段】: Meta Judge
【三次中位】: [25%, 20%, 20%]  std=2.4%
【共识维度】:
- **Venue Mismatch（致命）**: 3/3 审稿人一致指出 CoRL 与本 NLP 论文完全不匹配，投 CoRL 概率 ≈ 0%（desk reject）。这是最高信号共识。
- **Novelty（弱→中）**: 3/3 一致认为"将英文 benchmark 扩展到多语言"是 NLP 领域最常见的增量范式，novelty 受限。R1=中, R2=弱-中偏弱, R3=弱。共识偏弱。
- **Significance（中）**: 3/3 一致给出"中"。问题有实际意义但核心发现（β>1 或 β≤1）无论哪个方向都不够 surprising——"I would have guessed this" 风险被三人同时标记。
- **Self-Correction Bench 仅为 workshop paper**: 3/3 一致指出前驱工作是 NeurIPS 2025 Workshop poster 而非主会论文，proposal 描述可能被视为 misleading。在 workshop paper 上做扩展进一步削弱 novelty。
- **Trivial alternative 存在**: 3/3 一致认为直接翻译 Self-Correction Bench + 跑实验即可覆盖核心发现的 ~40%，低成本替代方案明确存在。
- **Related Work 显著遗漏**: 3/3 均指出缺少关键引用（TACL 2025 self-correction survey 被 3 人同时标记；Huang et al. ICLR 2024/2025 被 R1/R2 同时标记；MMLU-ProX 被 R1/R3 同时标记）。
- **Qwen3 MoE/Dense "controlled comparison" 过度简化**: R1/R2/R3 均从不同角度质疑（active params 差异、训练 dynamics 不同、相关性≠因果性）。
- **"Wait" 跨语言泛化是最有价值的单点贡献**: R1/R2 明确标记，R3 承认但仍认为增量。共识为"亮点但不足以翻盘"。

【异常维度】:
- R3 独有：提到 CorrectBench 作为未引用的竞争性 benchmark——有效信号，应纳入 related work 补充建议。
- R3 独有：提出 floor effect 风险（低资源语言 base accuracy 下降导致可测量 blind spot 样本减少，CGA 统计估计不稳定）——这是一个技术上重要但其他两人未涉及的统计方法论质疑，属中等信号。
- R2 独有：提到 Cross-Lingual Prompt Steerability (arXiv:2512.02841) 作为高度相关但未引用的工作——有效信号，直接涉及 prompt 跨语言泛化。
- R3 独有：提到翻译 benchmark 的 construct validity 问题（引用 arXiv:2511.05162 "Mind the Gap"）——方法论层面有效质疑。
- R3 独有：提到 arXiv:2505.11924 (Intrinsic Self-Correction via Mechanistic Interpretability) 与 activation amplification 分析重叠——补充性信号。

【最终概率】: [16% - 26%] 中位 20%
【一致性】: 高（std=2.4% < 3%，三人在 Novelty/Significance/主要风险上高度一致）

【综合理由】:
三份评审展现出罕见的高度一致性——不仅概率估计集中（20-25% 窄带），且在核心判断上几乎完全对齐：

1. **Novelty 是主要瓶颈**。三人一致将本工作定性为"benchmark 多语言扩展"的增量范式。R1 给中（稍宽），R2/R3 给弱-中/弱（更严）。鉴于高一致性下取中位附近，最终判定 Novelty 为**弱-中**。CGA 形式化和 "Wait" 泛化测试提供了超越纯翻译的增量价值，但不足以摆脱"obvious next step"标签——尤其是原作者已明确将多语言列为 future work。

2. **Significance 稳定在中**。三人完全一致。问题本身有实际价值（多语言 AI safety），但核心发现的可预测性严重限制了 surprise factor。这决定了即使实验执行完美，idea 天花板也不高。

3. **Related Work 需要补强**。R1 给中偏弱，R2 给中，R3 给弱。遗漏的关键引用包括 TACL 2025 survey（3 人共识）、ICLR 2024 self-correction 基石论文（2 人共识）、MMLU-ProX（2 人共识），以及 R2/R3 各自独立发现的额外相关工作。虽然 related work 遗漏可修复，但数量和覆盖面之广暗示作者对两个母领域的文献掌握不够深入。

4. **处理异常维度**：R3 提出的 floor effect 和 construct validity 问题虽为独有，但技术上成立，应作为实验设计风险纳入考虑（降权处理，不作为主要扣分项但增加方法论不确定性）。R2 提出的 arXiv:2512.02841 是有效的 related work 补充，应纳入。

5. **概率推导**：三人中位分别为 25/20/20，整体中位 20%。R1 的 25% 稍高但其分析中也明确标注了核心发现可预测性和增量性风险。按"高一致取中位附近、缩窄区间"原则，最终区间 [16%-26%]，中位 20%。不超过最宽松的 R1 上界（32%），因为 R1 的上界条件（β 显著 >1 + "Wait" 出现 counter-intuitive 模式）是乐观情景而非基线预期。

6. **Venue 问题单独说明**：以上 20% 是假设投稿**合适的 NLP venue**（ACL/EMNLP/NAACL/COLM）。若投稿 CoRL 2026，三人一致估计 0-3%，几乎必然 desk reject。

【建议】: 不推荐（投 CoRL 为 KILL；即使改投 NLP venue，idea 天花板有限，中位 20% 低于 36% 通过线，属边缘偏下）

【实施评估】:
- **计算资源**: 中等。4 个 frontier 模型通过 API 调用（Qwen3-235B, Gemini 2.0 Flash, GPT-4o, Claude Sonnet 4），成本取决于 12 语言 × 任务量的 token 消耗，估计 API 费用 $2,000-5,000。3 个开源模型（Gemma 4 31B, Qwen3-30B-A3B, Qwen3-32B）需要 2-4 张 A100 80GB 做推理，routing 分析可能需要额外显存用于 intermediate activation 提取。无需训练，纯推理 + 分析。
- **数据需求**: 需要在 Self-Correction Bench 基础上构建 X-CorrectBench——将英文测试集翻译为 12 种语言（10 语系、8 书写系统）。翻译质量直接影响 construct validity。可用 GPT-4 初翻 + 人工校验，但 12 语言的覆盖面要求较高的多语言资源网络。
- **人工介入**: **高**。12 种语言各需至少 1 名 native speaker 进行翻译校验和错误注入自然度评估。低资源语言（如阿拉伯语变体、斯瓦希里语等）的 native speaker 招募可能较困难。估计需 12-20 名标注人员，每人 5-10 小时工作量。
- **训练需求**: 无模型训练。本质是评估/分析论文，所有模型均直接使用。
- **新 Benchmark**: 是。需构建 X-CorrectBench（12 语言版本的 Self-Correction Bench），包括翻译、质量控制、pilot testing。这是主要工作量来源。
- **预估周期**: 10-14 周。Benchmark 构建（翻译+校验）4-6 周 → API/开源模型实验 2-3 周 → MoE routing 分析 1-2 周 → 统计分析+写作 3-4 周。瓶颈在多语言翻译校验环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce0d097e-acc1-4649-aefb-04b95096ff92",
  "isSidechain": false,
  "requestId": "req_011CbD7T3vKtqM4svXkgQZ4m",
  "type": "assistant",
  "uuid": "628e1fe3-8737-49dd-9e62-7fb2f73f6389",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178RnA7DnDUFERpyhZyrJpB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14604,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4354,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14604
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research context. Let me compile my eval…",
  "leafUuid": "628e1fe3-8737-49dd-9e62-7fb2f73f6389",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate multilingual LLM self-correction disparities",
  "sessionId": "a537eb9e-31e5-4265-8dc0-ad2cb6bcf9c6"
}
```

---
