# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/49db71ce-bde2-421e-9106-807e39537aff.jsonl`
- **Structured JSON:** [`e31896c914b79a74f018.json`](../../sessions/e3/e31896c914b79a74f018.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:39:28.813Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:39:28.813Z",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a grounded evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [Interpretability without Actionability (Basu et al., arXiv:2603.18353, March 2026)](https://arxiv.org/abs/2603.18353): 直接的对话对象。在临床分诊 LM 上测试了四种机制性干预方法（SAE steering、activation patching 等），发现 knowledge-action gap 高达 53 个百分点——线性探针 AUROC 98.2% 但模型输出灵敏度仅 45.1%。本 proposal 的 Domain Amenability Hypothesis 本质上是为了解释这个失败。\n- [SteerRM (arXiv:2603.12795, March 2026)](https://arxiv.org/abs/2603.12795): Feature-level 基线。使用预训练 LlamaScope SAE 进行 RM debiasing，在 RM-Bench Hard split 上平均提升 7.3 分。Proposal 认为其受限于 layers 0-9，提出用 from-scratch SAE 改进。\n- [CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026)](https://arxiv.org/abs/2604.27495): Neuron-level 基线。用 Spearman 相关+因果中介分析，编辑 <2% 神经元，使小 RM 匹配 70B 性能。\n- [Orgad et al. (arXiv:2605.11161, ICML 2026)](https://arxiv.org/abs/2605.11161): Position paper，提出用 concreteness + validation 两个维度评估可解释性的 actionability。本 proposal 采用其评估标准但声称自己的 Domain Amenability Hypothesis 是独立贡献。\n- [Lee et al. (arXiv:2605.05508, May 2026)](https://arxiv.org/abs/2605.05508): 提出可解释性作为评估的三个科学标准（可证伪性、可复现性、预测性），proposal 也采用其框架。\n- [Arad et al. (arXiv:2505.20063, EMNLP 2025)](https://arxiv.org/abs/2505.20063): 关键方法论来源。区分 input features 和 output features，output-score filtering 带来 2-3x 提升。Proposal 计划将此应用于 PRM SAE。\n- [CRA (arXiv:2508.04216, 2025)](https://arxiv.org/abs/2508.04216): 已在 PRM 激活上从头训练 SAE（8× expansion，8× V100）用于 backdoor correction。Proposal 的 SAE 方法论直接继承自 CRA。\n- [Locate, Steer, and Improve (Zhang et al., arXiv:2601.14004, Jan 2026)](https://arxiv.org/html/2601.14004v1): 最全面的 actionable MI taxonomy，提出 locate-steer-improve pipeline。Proposal 声称实例化了该 pipeline。\n\n- **调研总结**: 2026 年初围绕\"mechanistic interventions 是否真正有效\"形成了一场活跃辩论（Basu et al. 的负面结果 vs. SteerRM/CIRM 的正面结果），多篇 position paper 提出了评估框架（Orgad、Lee）。但目前没有工作在同一 domain 内系统比较不同粒度的干预方法，也没有工作提出明确的\"domain amenability\"条件假说。Proposal 填补的是一个\"组织性/系统性比较\"的空白，但个体方法和工具均已存在。\n\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。** \n1. 对于\"多粒度比较\"这个贡献：直接在相同 benchmark 上独立运行 SteerRM 和 CIRM 的公开代码，就能得到 feature-level vs. neuron-level 的效果对比。不需要从头训练 SAE、不需要电路追踪、不需要 self-repair 量化。一个简单的\"复现+对比\"实验就能回答\"哪个粒度更好\"这个核心问题。\n2. 对于 Domain Amenability Hypothesis：这本质上是一个 post-hoc 的解释框架。只有两个数据点（临床 LM = 失败，PRM = 成功），任何区分这两个 domain 的 4 条性质都能构成一个\"假说\"。没有第三个 domain 的验证，这个假说无法与 trivial 的替代解释区分开（例如：\"interventions 在有标量输出的模型上更好用\"这一条就能解释一切）。\n3. **增量价值**的声称在于 output-score filtering + from-scratch SAE 的结合、circuit-level intervention、以及系统化的评估矩阵。但这些增量价值是实验设计层面的改进，不是 idea 层面的突破。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的关键假设：\n\n1. **最关键假设——\"4 条 domain conditions 是因果性的，而非巧合性的\"**: Proposal 的核心贡献是 Domain Amenability Hypothesis，但该假说的验证逻辑是：PRM 满足 4 条 → 干预成功；临床 LM 不满足 → 干预失败。这是 N=2 的 post-hoc 归纳，无法排除混淆因素（如模型架构差异、任务复杂度、训练数据规模等同样能解释差异）。Proposal 没有提供第三个 domain 的验证点，也没有消融实验来测试\"移除某条 condition 后干预是否失败\"。\n\n2. **\"PRM 干预确实会成功\"**: Proposal 预设了 positive 结果作为主要预期。虽然有 dual-outcome 设计，但整个实验框架和 framing 都围绕\"成功案例\"构建。如果干预效果 < 3%，则 domain amenability hypothesis 没有正面证据，整篇论文的故事线将大幅弱化。\n\n3. **\"from-scratch SAE 在 PRM 上优于 pretrained SAE\"这个方法论 claim**: 这是一个合理的假设但未经直接对比验证。CRA 和 SteerRM 使用了不同的模型、不同的 benchmark、不同的 evaluation metric，不能直接比较。\n\n4. **\"电路结构中 fluency 和 reasoning 是可分离的\"**: H2 假设 multi-method tracing 会发现 separable 的 fluency-reasoning circuits。但如果这些功能高度 entangled（这是完全可能的），整个 circuit-level intervention 方案将失效。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心 novelty 有两个：(a) Domain Amenability Hypothesis——一个新的概念框架，但 N=2 验证使其更像 post-hoc 观察而非可证伪的科学假说；(b) 同一 domain 内的多粒度干预系统比较——这是组织性/工程性的贡献，individual pieces 全部来自已有工作（SAE from scratch → CRA, feature suppression → SteerRM, neuron editing → CIRM, output-score filtering → Arad et al., 电路追踪 → RelP/CLT）。剔除 surface differences 后，真正新的 intellectual contribution 是\"把已有方法放到同一框架下比较\"，这更接近 benchmark/survey 论文的贡献模式而非 research paper 的贡献模式。没有提出新的干预方法、新的分析技术或新的理论框架（Domain Amenability Hypothesis 过于初步，难以称为理论贡献）。\n\n2. **Significance: 中** — \n   \"when do mechanistic interventions succeed\"这个问题本身是重要且 timely 的——Basu et al. 的负面结果引发了真实的社区关注（Orgad et al. 和 Lee et al. 的 position papers 证明了这一点）。但本 proposal 对这个问题的回答可能令审稿人感到\"I would have guessed this\"：PRM 有标量输出、可验证的 ground truth、良好的结构——当然比开放式临床文本更适合机制干预。如果实验结果证实了这一直觉（很可能），contribution 就是\"验证了一个显而易见的假说\"。此外，对实际应用的影响有限——PRM debiasing 已有多种有效方法（SteerRM、CIRM），本文不太可能推翻它们。\n\n3. **Related Work: 强** — \n   这是 proposal 最强的部分。对领域的覆盖极其全面：从 actionability debate（Basu、Orgad、Lee）到 PRM bias（Tiwari、Wang）到具体干预方法（SteerRM、CIRM、CRA、Arad）到分析工具（RelP、CLT-Forge）到自修复（McGrath）到生成式 PRM 趋势（ThinkPRM、GenPRM），每篇引文都经查证存在且描述准确。差异化定位也清晰：明确说明了自己与 SteerRM（pretrained vs. from-scratch SAE）、与 CIRM（neuron vs. multi-granularity）、与 CRA（backdoor correction vs. systematic comparison）的区别。唯一值得注意的是：Wang et al. 的 evolutionary bias discovery 被纳入作为上游组件，但与本文核心 claim 的联系较弱。\n\n\n【概率估计】: [18% - 28%] 中位 23%\n\n【估计理由】: \nSignificance 中等（问题重要但答案可能不够 surprising）+ Novelty 弱-中（核心是已有方法的系统比较，Domain Amenability Hypothesis 的 N=2 验证不够有力）共同限制了上界。Related Work 的强覆盖和整体执行设计的严谨性提供了一定的下限保护——审稿人会认可作者对领域的深入理解。**限制上界的关键维度是 Novelty**：如果审稿人认为这本质上是\"在 PRM 上跑了一遍已有方法的比较实验\"，再加上一个 post-hoc 的 2-data-point hypothesis，novelty 评分会很低。中位 23% 反映了\"solid empirical contribution but predictable insight\"的定位——在 borderline reject 到 weak accept 之间，更偏向前者。\n\n【主要风险】:\n1. **Domain Amenability Hypothesis 的 N=2 问题**: 只有两个 domain（PRM vs. clinical LM）验证一个 4-condition 的假说，审稿人很可能指出这在统计上无法支撑任何因果性 claim，甚至无法排除最简单的 alternative explanation（如\"scalar output 模型更好干预\"一条就够了）。\n2. **\"I would have guessed this\" 风险**: 核心预测——PRM 这种结构化、可验证的 domain 上干预会比开放式临床文本更成功——符合大多数研究者的直觉。如果实验结果确认了这个直觉，审稿人会质疑：\"What did we learn that we didn't already know?\"\n```\n\nSources:\n- [Interpretability without Actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)\n- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495)\n- [Position: Interpretability Can Be Actionable (Orgad et al., ICML 2026)](https://arxiv.org/abs/2605.11161)\n- [Rigorous Interpretation Is a Form of Evaluation (Lee et al.)](https://arxiv.org/abs/2605.05508)\n- [SAEs Are Good for Steering – If You Select the Right Features (Arad et al., EMNLP 2025)](https://arxiv.org/abs/2505.20063)\n- [CRA: Causal Reward Adjustment (arXiv:2508.04216)](https://arxiv.org/abs/2508.04216)\n- [Locate, Steer, and Improve Survey (Zhang et al.)](https://arxiv.org/abs/2601.14004)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research material. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [Interpretability without Actionability](https://arxiv.org/abs/2603.18353) (Basu et al., arXiv 2026.03): 测试了4种机械可解释性干预方法（包括SAE steering和activation patching）在临床分诊LM上的效果，发现知识-行动鸿沟持续存在——SAE steering产生零修正，activation patching在标准强度下净增益为零。线性探针能以98.2% AUROC区分危险/良性案例，但模型输出灵敏度仅45.1%。这是本proposal的核心动机之一，论文真实存在且描述准确。\n\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795) (arXiv 2026.03, 北大): 首个无需训练的RM去偏方法，使用预训练的LlamaScope SAE在RM隐状态上进行特征抑制，在RM-Bench Hard split上平均提升7.3分。限制在layers 0-9（因预训练SAE的分布不匹配）。与Basu形成\"成功vs失败\"的对比。描述准确。\n\n- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495) (Shinoda et al., ACL 2026): 使用Spearman相关性识别偏差相关神经元 + Pearl因果中介分析，编辑<2%的神经元使2个通用RM匹配70B性能。神经元级别干预，偏差信号主要在早期层。描述准确。\n\n- [Interpretability Can Be Actionable](https://arxiv.org/abs/2605.11161) (Orgad et al., ICML 2026): 提出可操作可解释性的二维评估框架（concreteness × validation），定义评估标准包括comparative utility、mechanistic faithfulness、generalization、specificity。本proposal采用其评估标准。描述准确。\n\n- [SAEs Are Good for Steering — If You Select the Right Features](https://aclanthology.org/2025.emnlp-main.519/) (Arad et al., EMNLP 2025): 区分\"输入特征\"和\"输出特征\"，提出output-score过滤方法，过滤后steering效果提升2-3倍。本proposal将此方法应用于PRM的feature-level干预中。描述准确。\n\n- [Locate, Steer, and Improve](https://arxiv.org/abs/2601.14004) (Zhang et al., arXiv 2026.01): 最全面的可操作MI survey，按Locate-Steer-Improve pipeline分类，识别了定位与实际steering之间的gap为核心未解决问题。本proposal声称直接填补这个gap。描述准确。\n\n- [CRA: Causal Reward Adjustment](https://arxiv.org/abs/2508.04216) (arXiv 2025.08): 在PRM激活上从头训练SAE（8×扩展因子），通过后门校正缓解奖励黑客行为。在MATH上准确率从57.3%提升到60.2%。这是\"从头在PRM激活上训练SAE\"方法的先例。描述准确。\n\n- [Rigorous Interpretation Is a Form of Evaluation](https://arxiv.org/abs/2605.05508) (Lee et al., arXiv 2026.05): 提出可解释性需满足falsifiability/reproducibility/predictivity三条科学标准。本proposal采用为评估框架之一。描述准确。\n\n- 调研总结: 该领域处于一个活跃的\"辩论期\"——Basu et al.的失败结果 vs. SteerRM/CIRM的成功结果形成了鲜明对比，多篇2026年position paper（Orgad et al., Lee et al.）呼吁系统化评估。已有多项独立的PRM去偏工作（SteerRM、CIRM、CRA、One Bias After Another），但确实尚无工作在统一框架下比较不同粒度的干预。Proposal处于这个辩论的交汇点上，试图做系统性比较。\n\n【Trivial Alternative 检验】:\n\n存在明确的trivial alternative威胁：\n\n1. **简单fine-tuning baseline**: 在去偏数据上对PRM进行fine-tuning（proposal自身在Phase 4中也承认需要与此比较）。如果fine-tuning on debiased data能以更低成本达到类似或更好的去偏效果，那么280 H100-hours的机械可解释性管线的增量价值就仅限于\"理解性\"而非\"实用性\"。\n\n2. **CIRM本身已经很cheap**: CIRM编辑<2%神经元就能匹配70B性能，这本身就是一个很简单且有效的方法。本proposal在CIRM之上的增量是什么？proposal声称增量是\"系统性比较\"和\"Domain Amenability Hypothesis验证\"——这是一个meta-level的贡献，而非方法贡献。\n\n3. **增量价值分析**: 本proposal的真正增量不在于提出更好的去偏方法，而在于：(a) 提供\"when do interventions work\"的结构化实证框架；(b) 比较不同粒度干预的优劣。这是一个**empirical study/analysis paper**的价值定位，而非一个methods paper。这个定位本身是合理的，但其价值完全取决于实验结论是否能提供超越\"common sense\"的洞察。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **Domain Amenability Hypothesis 的因果推断问题（最关键）**: Proposal 提出四条domain amenability conditions（well-defined output semantics, constrained output structure, verifiable ground truth, testable specificity），并声称PRM满足而clinical LMs不满足，以此解释为何干预在PRM上成功而在clinical domain失败。但这是一个**n=2的对比**（1个成功domain + 1个失败domain），从两个样本点归纳出四条因果条件是严重的过度拟合(overfitting)风险。没有任何方法可以从2个数据点上验证4个条件中哪些是必要条件、哪些是充分条件。Proposal甚至无法排除一个trivial的替代解释：\"PRM上干预成功是因为PRM比clinical LM更简单/更小/信息更集中，与这4个conditions无关。\"\n\n2. **\"43% stylistic exploitation\" 的可迁移性**: Tiwari et al.的43%数字是在特定PRM和特定benchmark上测量的。Proposal将其作为\"PRM conflate fluency with correctness\"的通用claim，但这个数字在不同PRM、不同数据集上的稳定性未知。\n\n3. **电路可分离性假设**: H2假设多方法追踪会发现可分离的fluency-reasoning电路结构。但如果fluency和reasoning在PRM中是deeply entangled的（这完全可能——一个解数学题的步骤的\"质量\"可能本质上就与表达方式相关），那么电路级干预就不会比粗粒度方法好多少。\n\n4. **跨架构对比的可比性**: Basu et al.用的是clinical triage LM（可能是general-purpose LM），本proposal用的是数学PRM（discriminative model）。模型类型、规模、训练方式的差异太大，无法仅归因于\"domain properties\"的差异。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — Proposal的核心新颖点是\"Domain Amenability Hypothesis\"和\"multi-granularity comparison in a unified framework\"。调研确认，确实没有工作在统一框架下比较feature/neuron/circuit-level干预。但实质上：(a) 每个单独的干预方法都已在prior work中提出和实现（SteerRM→feature-level, CIRM→neuron-level, CRA→SAE-on-PRM），proposal的贡献是**组合和比较**，而非新方法；(b) \"Domain Amenability Hypothesis\"本身的验证设计（n=2对比）太弱，难以被视为robust的理论贡献；(c) 采用的评估框架（Orgad et al. + Lee et al.）是直接借用现有框架，非原创。Proposal的novelty更多是\"systematic empirical study\"类型的，这在顶会中是可以接受的定位，但novelty delta集中在实验设计和组合上，而非conceptual breakthrough。\n\n2. **Significance: 中** — 研究问题（when do mechanistic interventions succeed?）确实是当前MI领域的核心未回答问题，且Basu vs. SteerRM/CIRM的辩论是2026年的热门话题。如果实验结论能给出清晰的指导原则，影响力可观。但：(a) 限定在discriminative PRM这一个domain，结论的可推广性有限——审稿人会问\"这些发现能推广到其他domain吗？\"而proposal的设计（n=2对比）无法回答这个问题；(b) 随着generative PRM（ThinkPRM, GenPRM）的崛起，discriminative PRM的实践相关性在下降，虽然proposal已acknowledge了这一点，但这确实降低了practical significance；(c) 如果最终结论是\"finer-grained interventions work better\"或\"interventions work in domains with verifiable ground truth\"，这些都属于\"I would have guessed this\"的范畴。\n\n3. **Related Work: 强** — 这是该proposal最突出的优点。对已有工作的覆盖异常全面且准确——我验证的所有关键引用（Basu, SteerRM, CIRM, Orgad, Arad, Lee, CRA, Zhang et al. survey）均真实存在且描述准确。差异化定位清晰：与SteerRM的区别（from-scratch SAE vs pretrained SAE + output-score filtering）、与CIRM的区别（多粒度比较 vs 仅neuron-level）、与CRA的区别（multi-granularity + Domain Amenability framing vs 仅backdoor correction）。对评估框架的采用（Orgad + Lee）也是合理且有据的。\n\n【概率估计】: [20% - 35%] 中位 25%\n\n【估计理由】: \n该proposal的核心价值是\"systematic empirical comparison\"，这个定位在顶会中是被接受的（如benchmark papers, large-scale empirical studies），但其上限受限于两个关键因素：\n\n(1) **Novelty的天花板是\"中\"**——没有提出新方法，核心贡献是将existing methods在统一框架下比较。审稿人对这类\"comparison paper\"的novelty bar较高，会问\"beyond running existing methods side by side, what do we learn that we couldn't have predicted?\"\n\n(2) **Domain Amenability Hypothesis的验证设计根本性薄弱**——n=2的对比无法支撑4条因果条件的claim。这是idea层面的逻辑链漏洞，不是实验能补救的。即使实验做得完美，审稿人仍会（正确地）指出：\"You showed interventions work on PRMs and don't work on clinical LMs. But you have exactly one success and one failure case — your four conditions are unfalsifiable from this data.\"\n\n上界（35%）对应场景：实验揭示genuinely surprising的粒度-效果关系（如circuit-level反而不如neuron-level），且结论具有指导意义。下界（20%）对应场景：结论符合预期（\"finer is better\" or \"it depends\"），且审稿人认为Domain Amenability Hypothesis的n=2设计是致命伤。\n\n中位25%反映：idea方向正确、文献功课极好、研究问题重要，但核心理论贡献（DAH）的验证设计薄弱 + novelty集中在实验组合而非概念突破。\n\n【主要风险】:\n1. **Domain Amenability Hypothesis 的 n=2 overfitting 问题**: 从2个domain归纳4条因果条件，审稿人几乎必然会指出这无法区分\"这4条conditions导致了成功\"和\"任何其他correlate导致了成功\"。这是idea层面的结构性缺陷。\n2. **\"Comparison paper\" 的 novelty 质疑**: 所有单项干预方法均已发表，proposal的增量是\"unified comparison\"——审稿人可能会认为这更接近一篇survey with experiments，而非一篇有核心新贡献的research paper。如果实验结论不够surprising，这个风险会被放大。\n```\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct my assessment. Let me compile the triage evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Basu et al., arXiv:2603.18353] (March 2026): 在临床分诊 LM 上测试 4 种机制性干预方法（SAE steering、activation patching 等），发现尽管 linear probes 达到 98.2% AUROC，干预却产生零或可忽略的纠正效果——确立了 \"knowledge-action gap\"。这是本 proposal 的核心对比锚点。\n- [SteerRM, arXiv:2603.12795] (March 2026, PKU): 首个无需训练的 SAE steering 去偏方法，用 pretrained LlamaScope SAEs 在 6 个 RM 上 Hard-split 平均提升 7.3 分。限制：仅分析 layers 0-9（预训练 SAE 的分布失配）。本 proposal 的 feature-level baseline 之一。\n- [CIRM/Shinoda et al., arXiv:2604.27495] (April 2026): Neuron-level 因果中介分析去偏 RM，用 Spearman 相关识别偏差神经元，编辑 <2% 神经元匹配 70B RM 性能。本 proposal 的 neuron-level baseline。\n- [CRA, arXiv:2508.04216] (2025): 在 PRM 激活上从头训练 SAE，通过 backdoor adjustment 缓解 reward hacking。本 proposal SAE 方法的直接先驱。\n- [\"One Bias After Another\", arXiv:2603.03291] (Feb 2026): 用 linear activation probes 对 5 个 RM 进行 mechanistic reward shaping，区分 low-complexity（线性可分离）和 high-complexity（纠缠的）偏差。Probe-level intervention 先驱。\n- [Arad et al., arXiv:2505.20063] (EMNLP 2025): 证明 SAE feature 选择对 steering 效果至关重要，区分 \"input features\" 和 \"output features\"，output-score filtering 带来 2-3× 提升。本 proposal 的关键方法组件。\n- [Orgad et al., arXiv:2605.11161] (ICML 2026 Position): 提出以 actionability（concreteness + validation）评估可解释性工作，建立 comparative utility、mechanistic faithfulness、generalization、specificity 四个评估维度。本 proposal 采用的评估框架之一。\n- [Lee et al., arXiv:2605.05508] (May 2026): 主张可解释性应满足科学标准（falsifiability、reproducibility、predictivity）才能构成评估。本 proposal 采用的另一评估框架。\n- [Zhang et al., \"Locate, Steer, Improve\", arXiv:2601.14004] (Jan 2026): 最全面的 actionable MI 分类法，识别 localization→steering 的 gap 为核心未解决问题。\n\n- 调研总结: PRM 去偏的 mechanistic intervention 领域在 2025-2026 年经历了快速发展，feature-level（SteerRM）、neuron-level（CIRM）、probe-level（One Bias After Another）、SAE-on-PRM（CRA/SARM）均已被独立探索。同时，\"何时干预有效\"的 meta-question 因 Basu et al. 的负面结果而成为热点辩题。但**没有工作在同一受控框架内系统比较多粒度干预**，也没有工作提出形式化的\"领域可适性条件\"。本 proposal 处于这个交叉点上。\n\n【Trivial Alternative 检验】:\n存在两个层面的 trivial alternative 威胁：\n\n1. **直接拼接现有结果**: SteerRM 已报告 feature-level 效果，CIRM 已报告 neuron-level 效果。审稿人可能质疑：为什么不能直接对比两篇论文的数字？增量价值在于：这两个工作使用了不同的模型、不同的 benchmark、不同的偏差定义，因此数字不可直接比较。在同一模型、同一评估协议下比较确实有价值——但这是一个\"对齐实验条件\"的工程贡献，不是概念性突破。\n\n2. **Fine-tuning on debiased data**: Proposal 将此作为 baseline，但如果 fine-tuning 效果与 mechanistic interventions 相当甚至更好（这在 Basu et al. 的讨论中被暗示为可能的替代方案），那么整个 mechanistic intervention 路线的增量价值就会受到挑战。Proposal 的回应是 mechanistic interventions 提供\"可解释性\"附加值——但这需要实验证明。\n\n**增量价值判断**: 多粒度受控比较本身有实际价值（解决了\"哪个粒度最好\"的实用问题），但 Domain Amenability Hypothesis 的增量价值较弱——因为它只是一个 n=2 的 post-hoc 观察（PRMs 成功 vs. clinical LMs 失败），无法真正\"检验\"假设。\n\n【前提假设检验】:\n核心逻辑链中有以下未经验证的假设：\n\n1. **「PRMs 满足四个领域条件 → 机制性干预会成功」是因果推断，但证据结构是相关性的。** 临床 LM 与 PRM 在太多维度上不同（模型架构、任务复杂度、输出形式、训练数据规模等），无法将干预效果差异归因于这四个特定条件。这是最大的逻辑漏洞。即使 PRM 干预成功，也只能说\"在这个满足四个条件的领域中干预成功了\"，不能说\"因为满足了这四个条件所以干预成功了\"。\n\n2. **「43% 的 reward gains 来自 stylistic exploitation」这个统计是否在多个 PRM 上复现？** 这来自 Tiwari et al. 的一个研究，但 proposal 将其作为普遍性前提。如果 Qwen2.5-Math-PRM 和 Math-Shepherd-Mistral 的 fluency bias 程度显著不同，那么\"同一偏差在两个架构上的干预效果比较\"的基础就可能不成立。\n\n3. **「从头训练的 SAE 必然优于预训练 SAE」是未验证的假设。** Proposal 提出了合理的论证（分布匹配更好），但这本身就是一个实验性问题，不是前提可以直接假设的。CRA 的成功不代表在这些特定 PRM 上 from-scratch SAE 一定优于 SteerRM 的 pretrained 方法。\n\n4. **「多方法一致性 = 因果有效性」的跳跃。** Proposal 假设 RelP 和 activation patching 的一致结果意味着因果电路被正确识别。但如果两种方法都对相同的 confound 敏感（例如都受 LayerNorm 影响），一致性并不能排除共同偏差。\n\n【3 维度打分】:\n\n1. **Novelty: 中（偏弱）**\n   - 理由: 本 proposal 的核心贡献是 (a) Domain Amenability Hypothesis 框架和 (b) 多粒度受控比较。\n   - 对于 (a): \"Domain Amenability Hypothesis\" 这个术语确实是新的（WebSearch 未找到任何先前使用），但四个条件的内容（well-defined semantics、constrained structure、verifiable ground truth、testable specificity）本身是直觉性的——大多数研究者会\"想当然\"地同意这些条件有利于干预成功。更关键的是，n=2 的领域对比（PRM vs. clinical LM）不是对假设的有意义检验，而是一个 post-hoc 归纳。Orgad et al. (ICML 2026) 已经从评估维度角度讨论了 actionability 的条件，Zhang et al. 的 \"Locate, Steer, Improve\" survey 也已识别了 \"sparse and decomposable mechanisms\" 作为成功条件。本 proposal 的假设与这些已有讨论有重叠。\n   - 对于 (b): 多粒度比较确实是一个尚未填补的 gap（SteerRM、CIRM、CRA 都在不同设置下独立工作），但这本质上是一个 **systematic empirical comparison**——将已有方法在受控条件下对齐比较。这是有价值的，但 novelty 类型偏向\"实验设计\"而非\"概念突破\"。所有单独的技术组件（SAE training、output-score filtering、RelP、CIRM adaptation、self-repair analysis）都直接借用自现有工作。\n   - 最相关竞争: SteerRM 已做 feature-level on RMs; CIRM 已做 neuron-level on RMs; CRA 已做 SAE-on-PRM; \"One Bias After Another\" 已做 probe-level on RMs。本 proposal 的 novelty delta 主要在\"统一比较 + 领域假设框架\"。\n\n2. **Significance: 中（偏强）**\n   - 理由: \"何时机制性干预有效\"确实是 2026 年 MI 领域最紧迫的问题之一——Basu et al. 的负面结果引发了真实的领域焦虑，Orgad et al. 的 ICML position paper 和 Lee et al. 的评估标准论文表明这是活跃辩论。一个在受控条件下比较多种干预粒度的实证研究，如果执行得好，确实能产生实际影响。\n   - 但限制在于: 最可能的结论是\"在 PRM（一个结构化、可验证的领域）上，细粒度干预优于粗粒度干预\"——这虽然有实用价值，但不太可能让审稿人说 \"surprising, not what I expected\"。如果核心发现是 \"circuit-level > feature-level > neuron-level\"，这基本符合直觉（更精确的干预效果更好）。如果发现是反直觉的排序，那 significance 会大幅提升，但 proposal 当前的假设 H3 预测了一个较为温和的结论（\"effectiveness varies by evaluation context\"）。\n   - 可推广性受限: 结论只对\"类 PRM 领域\"（结构化输出、可验证真值）有直接参考价值，对更一般的 LLM 行为编辑场景的指导意义有限。\n\n3. **Related Work: 强**\n   - 理由: Proposal 对相关工作的覆盖非常全面且准确。经 WebSearch 验证：Basu et al. (arXiv:2603.18353)、SteerRM (arXiv:2603.12795)、CIRM (arXiv:2604.27495)、CRA (arXiv:2508.04216)、Arad et al. (arXiv:2505.20063, EMNLP 2025)、Orgad et al. (arXiv:2605.11161, ICML 2026)、Lee et al. (arXiv:2605.05508)、\"One Bias After Another\" (arXiv:2603.03291) 均真实存在，描述基本准确。\n   - 差异化定位清晰：proposal 准确指出了 SteerRM 的 pretrained SAE 局限（layers 0-9）、CIRM 的 correlation-based 选择局限、CRA 的 from-scratch 优势等。\n   - 唯一微小担忧: Shinoda et al. 是否确已被 ACL 2026 接收（搜索结果仅显示 arXiv preprint）无法完全确认，但这不影响技术内容的准确性。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】:\n- **Novelty 是主要限制因素**。核心贡献是\"多粒度受控比较 + 领域假设框架\"，但所有技术组件均借用自现有工作，领域假设的检验设计（n=2）逻辑上过弱。审稿人很可能评价为 \"a well-designed comparison study, but limited conceptual novelty\"。\n- **Significance 提供了一定支撑**。问题本身是重要的、时机是好的（正处于 actionability 辩论的高峰期），这为概率提供了下界支撑。\n- **Related Work 的全面性是加分项**，但无法弥补 novelty 的不足。\n- 上界（33%）对应：如果实验结果产生了反直觉发现（例如 neuron-level 出人意料地优于 circuit-level，或者 PRM 干预也失败），那么论文的价值会显著提升。但基于 proposal 当前的假设设计，这种反直觉结果似乎不是预期方向。\n- 下界（22%）对应：如果审稿人认为这本质上是一个 \"comparison paper\"，缺乏独立的方法论贡献，那么在 top venue 的接收概率会较低。\n\n【主要风险】:\n1. **\"Systematic comparison without conceptual novelty\" 拒稿理由**: 审稿人可能认为将 SteerRM、CIRM、circuit-level 在同一框架下比较虽然有工程价值，但不构成足够的概念性贡献。所有单独组件都是已有方法的直接应用或微调。\n2. **Domain Amenability Hypothesis 的 n=2 检验不具备说服力**: 仅对比 PRM（成功）和 clinical LM（失败）两个领域，存在太多 confounding factors，审稿人可能质疑这不是对假设的真正检验，而仅仅是对两个独立结果的 post-hoc 叙事包装。如果该假设被认为不成立，论文就退化为一个\"PRM 去偏方法比较\"的纯实证工作，significance 和 novelty 都会进一步降低。\n```\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models\n\n## Description\nWhen do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.\n\n## Core Problem\nThe mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).\n\n## Opportunity\nThe interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.\n\n## Landscape\nTHE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.\n\nACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.\n\nPRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.\n\nINTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.\n\nSPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.\n\nSAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.\n\nCIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.\n\nSELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.\n\nGENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.\n\n## Approach\nWe conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.\n\n**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**\n\n*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.\n\n*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.\n\n*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.\n\n**Phase 2: Multi-Method Causal Circuit Tracing.**\n\nTier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).\n\nTier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.\n\n**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.\n\nComponents are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.\n\n**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:\n\n(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.\n\n(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.\n\n**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:\n\n**Core granularities (all 3 PRMs × 3 core benchmarks):**\n(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);\n(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;\n(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.\n\n**Extension granularities (single most informative PRM × 3 core benchmarks):**\n(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;\n(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.\n\nWe benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.\n\n**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:\n\n*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?\n\n*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.\n\nThis produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.\n\n**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.\n\n**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}, 'human_in_loop': {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}, 'auto_research': {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}}\n\n## Inspired By\nPrimary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing\n\n## Target Venues\n- ICLR 2027 (full paper deadline: ~September 2026 AoE — primary target, 12-week comfortable timeline; the domain amenability hypothesis and actionability framing position this as a timely contribution to a live debate)\n- ICML 2027 (full paper deadline: ~January 2027 AoE — safe fallback with time for extended experiments and thorough analysis)\n- AAAI 2027 (full paper deadline: July 28, 2026 AoE — aggressive 10-week target, feasible with human-in-loop or auto-research timeline)\n\n## Key References\n- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)\n- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)\n- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)\n- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)\n- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)\n- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)\n- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)\n- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)\n- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)\n- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)\n- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)\n- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)\n- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)\n- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)\n- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)\n- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)\n- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)\n- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)\n- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)\n- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)\n- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)\n- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)\n- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)\n- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)\n- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)\n- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T05:39:28.816Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:39:28.816Z",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T05:39:28.857Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make a grounded evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

- [Interpretability without Actionability (Basu et al., arXiv:2603.18353, March 2026)](https://arxiv.org/abs/2603.18353): 直接的对话对象。在临床分诊 LM 上测试了四种机制性干预方法（SAE steering、activation patching 等），发现 knowledge-action gap 高达 53 个百分点——线性探针 AUROC 98.2% 但模型输出灵敏度仅 45.1%。本 proposal 的 Domain Amenability Hypothesis 本质上是为了解释这个失败。
- [SteerRM (arXiv:2603.12795, March 2026)](https://arxiv.org/abs/2603.12795): Feature-level 基线。使用预训练 LlamaScope SAE 进行 RM debiasing，在 RM-Bench Hard split 上平均提升 7.3 分。Proposal 认为其受限于 layers 0-9，提出用 from-scratch SAE 改进。
- [CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026)](https://arxiv.org/abs/2604.27495): Neuron-level 基线。用 Spearman 相关+因果中介分析，编辑 <2% 神经元，使小 RM 匹配 70B 性能。
- [Orgad et al. (arXiv:2605.11161, ICML 2026)](https://arxiv.org/abs/2605.11161): Position paper，提出用 concreteness + validation 两个维度评估可解释性的 actionability。本 proposal 采用其评估标准但声称自己的 Domain Amenability Hypothesis 是独立贡献。
- [Lee et al. (arXiv:2605.05508, May 2026)](https://arxiv.org/abs/2605.05508): 提出可解释性作为评估的三个科学标准（可证伪性、可复现性、预测性），proposal 也采用其框架。
- [Arad et al. (arXiv:2505.20063, EMNLP 2025)](https://arxiv.org/abs/2505.20063): 关键方法论来源。区分 input features 和 output features，output-score filtering 带来 2-3x 提升。Proposal 计划将此应用于 PRM SAE。
- [CRA (arXiv:2508.04216, 2025)](https://arxiv.org/abs/2508.04216): 已在 PRM 激活上从头训练 SAE（8× expansion，8× V100）用于 backdoor correction。Proposal 的 SAE 方法论直接继承自 CRA。
- [Locate, Steer, and Improve (Zhang et al., arXiv:2601.14004, Jan 2026)](https://arxiv.org/html/2601.14004v1): 最全面的 actionable MI taxonomy，提出 locate-steer-improve pipeline。Proposal 声称实例化了该 pipeline。

- **调研总结**: 2026 年初围绕"mechanistic interventions 是否真正有效"形成了一场活跃辩论（Basu et al. 的负面结果 vs. SteerRM/CIRM 的正面结果），多篇 position paper 提出了评估框架（Orgad、Lee）。但目前没有工作在同一 domain 内系统比较不同粒度的干预方法，也没有工作提出明确的"domain amenability"条件假说。Proposal 填补的是一个"组织性/系统性比较"的空白，但个体方法和工具均已存在。


【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 
1. 对于"多粒度比较"这个贡献：直接在相同 benchmark 上独立运行 SteerRM 和 CIRM 的公开代码，就能得到 feature-level vs. neuron-level 的效果对比。不需要从头训练 SAE、不需要电路追踪、不需要 self-repair 量化。一个简单的"复现+对比"实验就能回答"哪个粒度更好"这个核心问题。
2. 对于 Domain Amenability Hypothesis：这本质上是一个 post-hoc 的解释框架。只有两个数据点（临床 LM = 失败，PRM = 成功），任何区分这两个 domain 的 4 条性质都能构成一个"假说"。没有第三个 domain 的验证，这个假说无法与 trivial 的替代解释区分开（例如："interventions 在有标量输出的模型上更好用"这一条就能解释一切）。
3. **增量价值**的声称在于 output-score filtering + from-scratch SAE 的结合、circuit-level intervention、以及系统化的评估矩阵。但这些增量价值是实验设计层面的改进，不是 idea 层面的突破。


【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的关键假设：

1. **最关键假设——"4 条 domain conditions 是因果性的，而非巧合性的"**: Proposal 的核心贡献是 Domain Amenability Hypothesis，但该假说的验证逻辑是：PRM 满足 4 条 → 干预成功；临床 LM 不满足 → 干预失败。这是 N=2 的 post-hoc 归纳，无法排除混淆因素（如模型架构差异、任务复杂度、训练数据规模等同样能解释差异）。Proposal 没有提供第三个 domain 的验证点，也没有消融实验来测试"移除某条 condition 后干预是否失败"。

2. **"PRM 干预确实会成功"**: Proposal 预设了 positive 结果作为主要预期。虽然有 dual-outcome 设计，但整个实验框架和 framing 都围绕"成功案例"构建。如果干预效果 < 3%，则 domain amenability hypothesis 没有正面证据，整篇论文的故事线将大幅弱化。

3. **"from-scratch SAE 在 PRM 上优于 pretrained SAE"这个方法论 claim**: 这是一个合理的假设但未经直接对比验证。CRA 和 SteerRM 使用了不同的模型、不同的 benchmark、不同的 evaluation metric，不能直接比较。

4. **"电路结构中 fluency 和 reasoning 是可分离的"**: H2 假设 multi-method tracing 会发现 separable 的 fluency-reasoning circuits。但如果这些功能高度 entangled（这是完全可能的），整个 circuit-level intervention 方案将失效。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心 novelty 有两个：(a) Domain Amenability Hypothesis——一个新的概念框架，但 N=2 验证使其更像 post-hoc 观察而非可证伪的科学假说；(b) 同一 domain 内的多粒度干预系统比较——这是组织性/工程性的贡献，individual pieces 全部来自已有工作（SAE from scratch → CRA, feature suppression → SteerRM, neuron editing → CIRM, output-score filtering → Arad et al., 电路追踪 → RelP/CLT）。剔除 surface differences 后，真正新的 intellectual contribution 是"把已有方法放到同一框架下比较"，这更接近 benchmark/survey 论文的贡献模式而非 research paper 的贡献模式。没有提出新的干预方法、新的分析技术或新的理论框架（Domain Amenability Hypothesis 过于初步，难以称为理论贡献）。

2. **Significance: 中** — 
   "when do mechanistic interventions succeed"这个问题本身是重要且 timely 的——Basu et al. 的负面结果引发了真实的社区关注（Orgad et al. 和 Lee et al. 的 position papers 证明了这一点）。但本 proposal 对这个问题的回答可能令审稿人感到"I would have guessed this"：PRM 有标量输出、可验证的 ground truth、良好的结构——当然比开放式临床文本更适合机制干预。如果实验结果证实了这一直觉（很可能），contribution 就是"验证了一个显而易见的假说"。此外，对实际应用的影响有限——PRM debiasing 已有多种有效方法（SteerRM、CIRM），本文不太可能推翻它们。

3. **Related Work: 强** — 
   这是 proposal 最强的部分。对领域的覆盖极其全面：从 actionability debate（Basu、Orgad、Lee）到 PRM bias（Tiwari、Wang）到具体干预方法（SteerRM、CIRM、CRA、Arad）到分析工具（RelP、CLT-Forge）到自修复（McGrath）到生成式 PRM 趋势（ThinkPRM、GenPRM），每篇引文都经查证存在且描述准确。差异化定位也清晰：明确说明了自己与 SteerRM（pretrained vs. from-scratch SAE）、与 CIRM（neuron vs. multi-granularity）、与 CRA（backdoor correction vs. systematic comparison）的区别。唯一值得注意的是：Wang et al. 的 evolutionary bias discovery 被纳入作为上游组件，但与本文核心 claim 的联系较弱。


【概率估计】: [18% - 28%] 中位 23%

【估计理由】: 
Significance 中等（问题重要但答案可能不够 surprising）+ Novelty 弱-中（核心是已有方法的系统比较，Domain Amenability Hypothesis 的 N=2 验证不够有力）共同限制了上界。Related Work 的强覆盖和整体执行设计的严谨性提供了一定的下限保护——审稿人会认可作者对领域的深入理解。**限制上界的关键维度是 Novelty**：如果审稿人认为这本质上是"在 PRM 上跑了一遍已有方法的比较实验"，再加上一个 post-hoc 的 2-data-point hypothesis，novelty 评分会很低。中位 23% 反映了"solid empirical contribution but predictable insight"的定位——在 borderline reject 到 weak accept 之间，更偏向前者。

【主要风险】:
1. **Domain Amenability Hypothesis 的 N=2 问题**: 只有两个 domain（PRM vs. clinical LM）验证一个 4-condition 的假说，审稿人很可能指出这在统计上无法支撑任何因果性 claim，甚至无法排除最简单的 alternative explanation（如"scalar output 模型更好干预"一条就够了）。
2. **"I would have guessed this" 风险**: 核心预测——PRM 这种结构化、可验证的 domain 上干预会比开放式临床文本更成功——符合大多数研究者的直觉。如果实验结果确认了这个直觉，审稿人会质疑："What did we learn that we didn't already know?"
```

Sources:
- [Interpretability without Actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)
- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495)
- [Position: Interpretability Can Be Actionable (Orgad et al., ICML 2026)](https://arxiv.org/abs/2605.11161)
- [Rigorous Interpretation Is a Form of Evaluation (Lee et al.)](https://arxiv.org/abs/2605.05508)
- [SAEs Are Good for Steering – If You Select the Right Features (Arad et al., EMNLP 2025)](https://arxiv.org/abs/2505.20063)
- [CRA: Causal Reward Adjustment (arXiv:2508.04216)](https://arxiv.org/abs/2508.04216)
- [Locate, Steer, and Improve Survey (Zhang et al.)](https://arxiv.org/abs/2601.14004)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research material. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

- [Interpretability without Actionability](https://arxiv.org/abs/2603.18353) (Basu et al., arXiv 2026.03): 测试了4种机械可解释性干预方法（包括SAE steering和activation patching）在临床分诊LM上的效果，发现知识-行动鸿沟持续存在——SAE steering产生零修正，activation patching在标准强度下净增益为零。线性探针能以98.2% AUROC区分危险/良性案例，但模型输出灵敏度仅45.1%。这是本proposal的核心动机之一，论文真实存在且描述准确。

- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795) (arXiv 2026.03, 北大): 首个无需训练的RM去偏方法，使用预训练的LlamaScope SAE在RM隐状态上进行特征抑制，在RM-Bench Hard split上平均提升7.3分。限制在layers 0-9（因预训练SAE的分布不匹配）。与Basu形成"成功vs失败"的对比。描述准确。

- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495) (Shinoda et al., ACL 2026): 使用Spearman相关性识别偏差相关神经元 + Pearl因果中介分析，编辑<2%的神经元使2个通用RM匹配70B性能。神经元级别干预，偏差信号主要在早期层。描述准确。

- [Interpretability Can Be Actionable](https://arxiv.org/abs/2605.11161) (Orgad et al., ICML 2026): 提出可操作可解释性的二维评估框架（concreteness × validation），定义评估标准包括comparative utility、mechanistic faithfulness、generalization、specificity。本proposal采用其评估标准。描述准确。

- [SAEs Are Good for Steering — If You Select the Right Features](https://aclanthology.org/2025.emnlp-main.519/) (Arad et al., EMNLP 2025): 区分"输入特征"和"输出特征"，提出output-score过滤方法，过滤后steering效果提升2-3倍。本proposal将此方法应用于PRM的feature-level干预中。描述准确。

- [Locate, Steer, and Improve](https://arxiv.org/abs/2601.14004) (Zhang et al., arXiv 2026.01): 最全面的可操作MI survey，按Locate-Steer-Improve pipeline分类，识别了定位与实际steering之间的gap为核心未解决问题。本proposal声称直接填补这个gap。描述准确。

- [CRA: Causal Reward Adjustment](https://arxiv.org/abs/2508.04216) (arXiv 2025.08): 在PRM激活上从头训练SAE（8×扩展因子），通过后门校正缓解奖励黑客行为。在MATH上准确率从57.3%提升到60.2%。这是"从头在PRM激活上训练SAE"方法的先例。描述准确。

- [Rigorous Interpretation Is a Form of Evaluation](https://arxiv.org/abs/2605.05508) (Lee et al., arXiv 2026.05): 提出可解释性需满足falsifiability/reproducibility/predictivity三条科学标准。本proposal采用为评估框架之一。描述准确。

- 调研总结: 该领域处于一个活跃的"辩论期"——Basu et al.的失败结果 vs. SteerRM/CIRM的成功结果形成了鲜明对比，多篇2026年position paper（Orgad et al., Lee et al.）呼吁系统化评估。已有多项独立的PRM去偏工作（SteerRM、CIRM、CRA、One Bias After Another），但确实尚无工作在统一框架下比较不同粒度的干预。Proposal处于这个辩论的交汇点上，试图做系统性比较。

【Trivial Alternative 检验】:

存在明确的trivial alternative威胁：

1. **简单fine-tuning baseline**: 在去偏数据上对PRM进行fine-tuning（proposal自身在Phase 4中也承认需要与此比较）。如果fine-tuning on debiased data能以更低成本达到类似或更好的去偏效果，那么280 H100-hours的机械可解释性管线的增量价值就仅限于"理解性"而非"实用性"。

2. **CIRM本身已经很cheap**: CIRM编辑<2%神经元就能匹配70B性能，这本身就是一个很简单且有效的方法。本proposal在CIRM之上的增量是什么？proposal声称增量是"系统性比较"和"Domain Amenability Hypothesis验证"——这是一个meta-level的贡献，而非方法贡献。

3. **增量价值分析**: 本proposal的真正增量不在于提出更好的去偏方法，而在于：(a) 提供"when do interventions work"的结构化实证框架；(b) 比较不同粒度干预的优劣。这是一个**empirical study/analysis paper**的价值定位，而非一个methods paper。这个定位本身是合理的，但其价值完全取决于实验结论是否能提供超越"common sense"的洞察。

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **Domain Amenability Hypothesis 的因果推断问题（最关键）**: Proposal 提出四条domain amenability conditions（well-defined output semantics, constrained output structure, verifiable ground truth, testable specificity），并声称PRM满足而clinical LMs不满足，以此解释为何干预在PRM上成功而在clinical domain失败。但这是一个**n=2的对比**（1个成功domain + 1个失败domain），从两个样本点归纳出四条因果条件是严重的过度拟合(overfitting)风险。没有任何方法可以从2个数据点上验证4个条件中哪些是必要条件、哪些是充分条件。Proposal甚至无法排除一个trivial的替代解释："PRM上干预成功是因为PRM比clinical LM更简单/更小/信息更集中，与这4个conditions无关。"

2. **"43% stylistic exploitation" 的可迁移性**: Tiwari et al.的43%数字是在特定PRM和特定benchmark上测量的。Proposal将其作为"PRM conflate fluency with correctness"的通用claim，但这个数字在不同PRM、不同数据集上的稳定性未知。

3. **电路可分离性假设**: H2假设多方法追踪会发现可分离的fluency-reasoning电路结构。但如果fluency和reasoning在PRM中是deeply entangled的（这完全可能——一个解数学题的步骤的"质量"可能本质上就与表达方式相关），那么电路级干预就不会比粗粒度方法好多少。

4. **跨架构对比的可比性**: Basu et al.用的是clinical triage LM（可能是general-purpose LM），本proposal用的是数学PRM（discriminative model）。模型类型、规模、训练方式的差异太大，无法仅归因于"domain properties"的差异。

【3 维度打分】:

1. **Novelty: 中** — Proposal的核心新颖点是"Domain Amenability Hypothesis"和"multi-granularity comparison in a unified framework"。调研确认，确实没有工作在统一框架下比较feature/neuron/circuit-level干预。但实质上：(a) 每个单独的干预方法都已在prior work中提出和实现（SteerRM→feature-level, CIRM→neuron-level, CRA→SAE-on-PRM），proposal的贡献是**组合和比较**，而非新方法；(b) "Domain Amenability Hypothesis"本身的验证设计（n=2对比）太弱，难以被视为robust的理论贡献；(c) 采用的评估框架（Orgad et al. + Lee et al.）是直接借用现有框架，非原创。Proposal的novelty更多是"systematic empirical study"类型的，这在顶会中是可以接受的定位，但novelty delta集中在实验设计和组合上，而非conceptual breakthrough。

2. **Significance: 中** — 研究问题（when do mechanistic interventions succeed?）确实是当前MI领域的核心未回答问题，且Basu vs. SteerRM/CIRM的辩论是2026年的热门话题。如果实验结论能给出清晰的指导原则，影响力可观。但：(a) 限定在discriminative PRM这一个domain，结论的可推广性有限——审稿人会问"这些发现能推广到其他domain吗？"而proposal的设计（n=2对比）无法回答这个问题；(b) 随着generative PRM（ThinkPRM, GenPRM）的崛起，discriminative PRM的实践相关性在下降，虽然proposal已acknowledge了这一点，但这确实降低了practical significance；(c) 如果最终结论是"finer-grained interventions work better"或"interventions work in domains with verifiable ground truth"，这些都属于"I would have guessed this"的范畴。

3. **Related Work: 强** — 这是该proposal最突出的优点。对已有工作的覆盖异常全面且准确——我验证的所有关键引用（Basu, SteerRM, CIRM, Orgad, Arad, Lee, CRA, Zhang et al. survey）均真实存在且描述准确。差异化定位清晰：与SteerRM的区别（from-scratch SAE vs pretrained SAE + output-score filtering）、与CIRM的区别（多粒度比较 vs 仅neuron-level）、与CRA的区别（multi-granularity + Domain Amenability framing vs 仅backdoor correction）。对评估框架的采用（Orgad + Lee）也是合理且有据的。

【概率估计】: [20% - 35%] 中位 25%

【估计理由】: 
该proposal的核心价值是"systematic empirical comparison"，这个定位在顶会中是被接受的（如benchmark papers, large-scale empirical studies），但其上限受限于两个关键因素：

(1) **Novelty的天花板是"中"**——没有提出新方法，核心贡献是将existing methods在统一框架下比较。审稿人对这类"comparison paper"的novelty bar较高，会问"beyond running existing methods side by side, what do we learn that we couldn't have predicted?"

(2) **Domain Amenability Hypothesis的验证设计根本性薄弱**——n=2的对比无法支撑4条因果条件的claim。这是idea层面的逻辑链漏洞，不是实验能补救的。即使实验做得完美，审稿人仍会（正确地）指出："You showed interventions work on PRMs and don't work on clinical LMs. But you have exactly one success and one failure case — your four conditions are unfalsifiable from this data."

上界（35%）对应场景：实验揭示genuinely surprising的粒度-效果关系（如circuit-level反而不如neuron-level），且结论具有指导意义。下界（20%）对应场景：结论符合预期（"finer is better" or "it depends"），且审稿人认为Domain Amenability Hypothesis的n=2设计是致命伤。

中位25%反映：idea方向正确、文献功课极好、研究问题重要，但核心理论贡献（DAH）的验证设计薄弱 + novelty集中在实验组合而非概念突破。

【主要风险】:
1. **Domain Amenability Hypothesis 的 n=2 overfitting 问题**: 从2个domain归纳4条因果条件，审稿人几乎必然会指出这无法区分"这4条conditions导致了成功"和"任何其他correlate导致了成功"。这是idea层面的结构性缺陷。
2. **"Comparison paper" 的 novelty 质疑**: 所有单项干预方法均已发表，proposal的增量是"unified comparison"——审稿人可能会认为这更接近一篇survey with experiments，而非一篇有核心新贡献的research paper。如果实验结论不够surprising，这个风险会被放大。
```

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct my assessment. Let me compile the triage evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Basu et al., arXiv:2603.18353] (March 2026): 在临床分诊 LM 上测试 4 种机制性干预方法（SAE steering、activation patching 等），发现尽管 linear probes 达到 98.2% AUROC，干预却产生零或可忽略的纠正效果——确立了 "knowledge-action gap"。这是本 proposal 的核心对比锚点。
- [SteerRM, arXiv:2603.12795] (March 2026, PKU): 首个无需训练的 SAE steering 去偏方法，用 pretrained LlamaScope SAEs 在 6 个 RM 上 Hard-split 平均提升 7.3 分。限制：仅分析 layers 0-9（预训练 SAE 的分布失配）。本 proposal 的 feature-level baseline 之一。
- [CIRM/Shinoda et al., arXiv:2604.27495] (April 2026): Neuron-level 因果中介分析去偏 RM，用 Spearman 相关识别偏差神经元，编辑 <2% 神经元匹配 70B RM 性能。本 proposal 的 neuron-level baseline。
- [CRA, arXiv:2508.04216] (2025): 在 PRM 激活上从头训练 SAE，通过 backdoor adjustment 缓解 reward hacking。本 proposal SAE 方法的直接先驱。
- ["One Bias After Another", arXiv:2603.03291] (Feb 2026): 用 linear activation probes 对 5 个 RM 进行 mechanistic reward shaping，区分 low-complexity（线性可分离）和 high-complexity（纠缠的）偏差。Probe-level intervention 先驱。
- [Arad et al., arXiv:2505.20063] (EMNLP 2025): 证明 SAE feature 选择对 steering 效果至关重要，区分 "input features" 和 "output features"，output-score filtering 带来 2-3× 提升。本 proposal 的关键方法组件。
- [Orgad et al., arXiv:2605.11161] (ICML 2026 Position): 提出以 actionability（concreteness + validation）评估可解释性工作，建立 comparative utility、mechanistic faithfulness、generalization、specificity 四个评估维度。本 proposal 采用的评估框架之一。
- [Lee et al., arXiv:2605.05508] (May 2026): 主张可解释性应满足科学标准（falsifiability、reproducibility、predictivity）才能构成评估。本 proposal 采用的另一评估框架。
- [Zhang et al., "Locate, Steer, Improve", arXiv:2601.14004] (Jan 2026): 最全面的 actionable MI 分类法，识别 localization→steering 的 gap 为核心未解决问题。

- 调研总结: PRM 去偏的 mechanistic intervention 领域在 2025-2026 年经历了快速发展，feature-level（SteerRM）、neuron-level（CIRM）、probe-level（One Bias After Another）、SAE-on-PRM（CRA/SARM）均已被独立探索。同时，"何时干预有效"的 meta-question 因 Basu et al. 的负面结果而成为热点辩题。但**没有工作在同一受控框架内系统比较多粒度干预**，也没有工作提出形式化的"领域可适性条件"。本 proposal 处于这个交叉点上。

【Trivial Alternative 检验】:
存在两个层面的 trivial alternative 威胁：

1. **直接拼接现有结果**: SteerRM 已报告 feature-level 效果，CIRM 已报告 neuron-level 效果。审稿人可能质疑：为什么不能直接对比两篇论文的数字？增量价值在于：这两个工作使用了不同的模型、不同的 benchmark、不同的偏差定义，因此数字不可直接比较。在同一模型、同一评估协议下比较确实有价值——但这是一个"对齐实验条件"的工程贡献，不是概念性突破。

2. **Fine-tuning on debiased data**: Proposal 将此作为 baseline，但如果 fine-tuning 效果与 mechanistic interventions 相当甚至更好（这在 Basu et al. 的讨论中被暗示为可能的替代方案），那么整个 mechanistic intervention 路线的增量价值就会受到挑战。Proposal 的回应是 mechanistic interventions 提供"可解释性"附加值——但这需要实验证明。

**增量价值判断**: 多粒度受控比较本身有实际价值（解决了"哪个粒度最好"的实用问题），但 Domain Amenability Hypothesis 的增量价值较弱——因为它只是一个 n=2 的 post-hoc 观察（PRMs 成功 vs. clinical LMs 失败），无法真正"检验"假设。

【前提假设检验】:
核心逻辑链中有以下未经验证的假设：

1. **「PRMs 满足四个领域条件 → 机制性干预会成功」是因果推断，但证据结构是相关性的。** 临床 LM 与 PRM 在太多维度上不同（模型架构、任务复杂度、输出形式、训练数据规模等），无法将干预效果差异归因于这四个特定条件。这是最大的逻辑漏洞。即使 PRM 干预成功，也只能说"在这个满足四个条件的领域中干预成功了"，不能说"因为满足了这四个条件所以干预成功了"。

2. **「43% 的 reward gains 来自 stylistic exploitation」这个统计是否在多个 PRM 上复现？** 这来自 Tiwari et al. 的一个研究，但 proposal 将其作为普遍性前提。如果 Qwen2.5-Math-PRM 和 Math-Shepherd-Mistral 的 fluency bias 程度显著不同，那么"同一偏差在两个架构上的干预效果比较"的基础就可能不成立。

3. **「从头训练的 SAE 必然优于预训练 SAE」是未验证的假设。** Proposal 提出了合理的论证（分布匹配更好），但这本身就是一个实验性问题，不是前提可以直接假设的。CRA 的成功不代表在这些特定 PRM 上 from-scratch SAE 一定优于 SteerRM 的 pretrained 方法。

4. **「多方法一致性 = 因果有效性」的跳跃。** Proposal 假设 RelP 和 activation patching 的一致结果意味着因果电路被正确识别。但如果两种方法都对相同的 confound 敏感（例如都受 LayerNorm 影响），一致性并不能排除共同偏差。

【3 维度打分】:

1. **Novelty: 中（偏弱）**
   - 理由: 本 proposal 的核心贡献是 (a) Domain Amenability Hypothesis 框架和 (b) 多粒度受控比较。
   - 对于 (a): "Domain Amenability Hypothesis" 这个术语确实是新的（WebSearch 未找到任何先前使用），但四个条件的内容（well-defined semantics、constrained structure、verifiable ground truth、testable specificity）本身是直觉性的——大多数研究者会"想当然"地同意这些条件有利于干预成功。更关键的是，n=2 的领域对比（PRM vs. clinical LM）不是对假设的有意义检验，而是一个 post-hoc 归纳。Orgad et al. (ICML 2026) 已经从评估维度角度讨论了 actionability 的条件，Zhang et al. 的 "Locate, Steer, Improve" survey 也已识别了 "sparse and decomposable mechanisms" 作为成功条件。本 proposal 的假设与这些已有讨论有重叠。
   - 对于 (b): 多粒度比较确实是一个尚未填补的 gap（SteerRM、CIRM、CRA 都在不同设置下独立工作），但这本质上是一个 **systematic empirical comparison**——将已有方法在受控条件下对齐比较。这是有价值的，但 novelty 类型偏向"实验设计"而非"概念突破"。所有单独的技术组件（SAE training、output-score filtering、RelP、CIRM adaptation、self-repair analysis）都直接借用自现有工作。
   - 最相关竞争: SteerRM 已做 feature-level on RMs; CIRM 已做 neuron-level on RMs; CRA 已做 SAE-on-PRM; "One Bias After Another" 已做 probe-level on RMs。本 proposal 的 novelty delta 主要在"统一比较 + 领域假设框架"。

2. **Significance: 中（偏强）**
   - 理由: "何时机制性干预有效"确实是 2026 年 MI 领域最紧迫的问题之一——Basu et al. 的负面结果引发了真实的领域焦虑，Orgad et al. 的 ICML position paper 和 Lee et al. 的评估标准论文表明这是活跃辩论。一个在受控条件下比较多种干预粒度的实证研究，如果执行得好，确实能产生实际影响。
   - 但限制在于: 最可能的结论是"在 PRM（一个结构化、可验证的领域）上，细粒度干预优于粗粒度干预"——这虽然有实用价值，但不太可能让审稿人说 "surprising, not what I expected"。如果核心发现是 "circuit-level > feature-level > neuron-level"，这基本符合直觉（更精确的干预效果更好）。如果发现是反直觉的排序，那 significance 会大幅提升，但 proposal 当前的假设 H3 预测了一个较为温和的结论（"effectiveness varies by evaluation context"）。
   - 可推广性受限: 结论只对"类 PRM 领域"（结构化输出、可验证真值）有直接参考价值，对更一般的 LLM 行为编辑场景的指导意义有限。

3. **Related Work: 强**
   - 理由: Proposal 对相关工作的覆盖非常全面且准确。经 WebSearch 验证：Basu et al. (arXiv:2603.18353)、SteerRM (arXiv:2603.12795)、CIRM (arXiv:2604.27495)、CRA (arXiv:2508.04216)、Arad et al. (arXiv:2505.20063, EMNLP 2025)、Orgad et al. (arXiv:2605.11161, ICML 2026)、Lee et al. (arXiv:2605.05508)、"One Bias After Another" (arXiv:2603.03291) 均真实存在，描述基本准确。
   - 差异化定位清晰：proposal 准确指出了 SteerRM 的 pretrained SAE 局限（layers 0-9）、CIRM 的 correlation-based 选择局限、CRA 的 from-scratch 优势等。
   - 唯一微小担忧: Shinoda et al. 是否确已被 ACL 2026 接收（搜索结果仅显示 arXiv preprint）无法完全确认，但这不影响技术内容的准确性。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】:
- **Novelty 是主要限制因素**。核心贡献是"多粒度受控比较 + 领域假设框架"，但所有技术组件均借用自现有工作，领域假设的检验设计（n=2）逻辑上过弱。审稿人很可能评价为 "a well-designed comparison study, but limited conceptual novelty"。
- **Significance 提供了一定支撑**。问题本身是重要的、时机是好的（正处于 actionability 辩论的高峰期），这为概率提供了下界支撑。
- **Related Work 的全面性是加分项**，但无法弥补 novelty 的不足。
- 上界（33%）对应：如果实验结果产生了反直觉发现（例如 neuron-level 出人意料地优于 circuit-level，或者 PRM 干预也失败），那么论文的价值会显著提升。但基于 proposal 当前的假设设计，这种反直觉结果似乎不是预期方向。
- 下界（22%）对应：如果审稿人认为这本质上是一个 "comparison paper"，缺乏独立的方法论贡献，那么在 top venue 的接收概率会较低。

【主要风险】:
1. **"Systematic comparison without conceptual novelty" 拒稿理由**: 审稿人可能认为将 SteerRM、CIRM、circuit-level 在同一框架下比较虽然有工程价值，但不构成足够的概念性贡献。所有单独组件都是已有方法的直接应用或微调。
2. **Domain Amenability Hypothesis 的 n=2 检验不具备说服力**: 仅对比 PRM（成功）和 clinical LM（失败）两个领域，存在太多 confounding factors，审稿人可能质疑这不是对假设的真正检验，而仅仅是对两个独立结果的 post-hoc 叙事包装。如果该假设被认为不成立，论文就退化为一个"PRM 去偏方法比较"的纯实证工作，significance 和 novelty 都会进一步降低。
```


【原始 proposal（允许参考但不是主要依据）】:
# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models

## Description
When do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.

## Core Problem
The mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).

## Opportunity
The interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.

## Landscape
THE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.

ACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.

PRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.

INTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.

SPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.

SAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.

CIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.

SELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.

GENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.

## Approach
We conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.

**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**

*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.

*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.

*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.

**Phase 2: Multi-Method Causal Circuit Tracing.**

Tier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).

Tier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.

**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.

Components are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.

**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:

(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.

(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.

**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:

**Core granularities (all 3 PRMs × 3 core benchmarks):**
(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);
(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;
(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.

**Extension granularities (single most informative PRM × 3 core benchmarks):**
(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;
(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.

We benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.

**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:

*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?

*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.

This produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.

**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.

**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.

## Resource Estimate
{'manual': {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}, 'human_in_loop': {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}, 'auto_research': {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}}

## Inspired By
Primary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing

## Target Venues
- ICLR 2027 (full paper deadline: ~September 2026 AoE — primary target, 12-week comfortable timeline; the domain amenability hypothesis and actionability framing position this as a timely contribution to a live debate)
- ICML 2027 (full paper deadline: ~January 2027 AoE — safe fallback with time for extended experiments and thorough analysis)
- AAAI 2027 (full paper deadline: July 28, 2026 AoE — aggressive 10-week target, feasible with human-in-loop or auto-research timeline)

## Key References
- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)
- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)
- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)
- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)
- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)
- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)
- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)
- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)
- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)
- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)
- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)
- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)
- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)
- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)
- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)
- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)
- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)
- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)
- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)
- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)
- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)
- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)
- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)
- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)
- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)
- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)
- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)
- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)
- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b6c8af78-89d7-452f-bba1-56fe59b7b01c",
  "type": "user",
  "uuid": "3edeb5fa-64f4-4617-8299-9a0754a9e07f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:39:28.854Z_

```json
{
  "parentUuid": "3edeb5fa-64f4-4617-8299-9a0754a9e07f",
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
  "uuid": "db7e3fd9-9833-4177-8972-a077a84bdb29",
  "timestamp": "2026-05-20T05:39:28.854Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:39:28.854Z_

```json
{
  "parentUuid": "db7e3fd9-9833-4177-8972-a077a84bdb29",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5bbf14de-61ab-43be-8c9c-d460fef8e628",
  "timestamp": "2026-05-20T05:39:28.854Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a grounded evaluation.…",
  "leafUuid": "5bbf14de-61ab-43be-8c9c-d460fef8e628",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:40:01.868Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them according to the Meta Judge format.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability: [18% - 28%] 中位 23%

**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [20% - 35%] 中位 25%


**Reviewer 3:**
- Novelty: 中（偏弱）
- Significance: 中（偏强）
- Related Work: 强
- Probability: [22% - 33%] 中位 27%

Now I'm calculating the aggregate statistics across all three reviewers. The median probabilities are 23%, 25%, and 27%, which average to 25% with a median of 25%. The standard deviation comes out to about 1.63%, which is well below the 3% threshold, indicating high consensus among the reviewers.

Looking at where they converge, all three independently flagged the same core weaknesses: the novelty is limited since this is primarily a systematic empirical comparison of existing methods rather than a conceptual advance, and the domain amenability hypothesis is critically underdeveloped with only two domains and four conditions that can't be causally validated from such limited data. They also all noted the risk that the main finding—that interventions work better in structured, verifiable domains—aligns too closely with intuitive expectations. On the positive side, there's unanimous agreement that the related work is exceptionally thorough, and while the research question itself is important and timely, the significance is ultimately moderate given these limitations.

The comparison paper concern appears across all three reviews: since every individual technique comes from prior work, the novelty hinges entirely on how they're combined and compared. All three also identified some version of a trivial alternative threat, whether that's running existing methods side by side or using fine-tuning as a baseline. The circuit separability assumption gets flagged by both R1 and R3, with R2 also treating it as a key assumption.

R3 adds a distinct concern about multi-method consistency not guaranteeing causal validity—both methods could be subject to the same confounds. Looking at the score ranges, there's remarkable agreement: R1 suggests 18-28 (median 23), R2 proposes 20-35 (median 25), and R3 recommends 22-33 (median 27). The standard deviation is only about 1.63%, indicating very tight convergence. Given this consensus around weak novelty and the n=2 DAH problem, the median area clusters around 25%, so I should narrow toward that range rather than stretching toward the most generous bounds.

I'll settle on [20-30%] with a midpoint of 25%, leaning slightly conservative given the universal concerns. Now I need to pull together the implementation assessment from the resource estimates in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bbf14de-61ab-43be-8c9c-d460fef8e628",
  "isSidechain": false,
  "requestId": "req_011CbDHNunUt1sVWZNtpLH6F",
  "type": "assistant",
  "uuid": "34f2243e-df65-4b03-aadc-a7315dea7353",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01We8WVoNeFX4NBjC2qv3gCF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21425,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3078,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3078,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 21425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21425
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

_source line 9 · 2026-05-20T05:40:45.450Z_

【阶段】: Meta Judge
【三次中位】: [23%, 25%, 27%]  std=1.6%
【共识维度】:
- **Novelty 弱-中**（3/3 一致）：所有审稿人均判定核心贡献是"已有方法的系统比较 + 组合"，而非概念性突破。所有单项技术组件（SAE from-scratch → CRA, feature suppression → SteerRM, neuron editing → CIRM, output-score filtering → Arad et al., RelP → NeurIPS 2025）均来自已有工作。Novelty delta 集中在实验设计层面。
- **Domain Amenability Hypothesis 的 n=2 致命缺陷**（3/3 一致，均标记为"最关键"问题）：从 2 个 domain（PRM 成功 vs. clinical LM 失败）归纳出 4 条因果条件，无法排除 confounding factors（模型架构、任务复杂度、训练规模等），也无法区分必要/充分条件。这是 idea 层面的结构性逻辑漏洞，不可通过实验弥补。
- **"I would have guessed this" 风险**（3/3 一致）：核心预测——结构化、可验证 domain 上干预优于开放式 domain——符合多数研究者直觉。如果实验确认直觉，审稿人会质疑 "What did we learn?"
- **Related Work: 强**（3/3 一致）：文献覆盖异常全面且准确，差异化定位清晰。这是 proposal 最强维度。
- **Significance: 中**（3/3 一致）：研究问题本身重要且 timely（正处于 actionability 辩论高峰），但结论可推广性受限于 PRM 这一个 domain，且 generative PRM 崛起降低了 discriminative PRM 的实践相关性。
- **Trivial Alternative 威胁**（3/3 均识别）：直接运行 SteerRM/CIRM 公开代码并对比即可回答"哪个粒度更好"的核心问题；fine-tuning on debiased data 可能以更低成本达到类似效果。
- **电路可分离性假设未验证**（3/3 均提及）：fluency 与 reasoning 可能高度 entangled，导致 circuit-level intervention 失效。

【异常维度】:
- R3 独有：多方法一致性 ≠ 因果有效性（RelP 和 activation patching 可能对同一 confound 敏感）——合理但权重较低，不改变总体判断。
- R2 对上界给出 35%（其余两位分别 28%、33%），反映其对"反直觉实验结果"场景略更乐观——但这是条件概率，非基础判断分歧。

【最终概率】: [20% - 30%] 中位 25%
【一致性】: 高（std=1.6%，三位审稿人在所有 rubric 维度上判决一致）
【综合理由】:
三位审稿人高度一致地收敛于同一判断结构：**Related Work 极强但 Novelty 是限制天花板的维度**。核心逻辑如下：

1. **Novelty 天花板约 30%**：当所有技术组件均来自 prior work、核心贡献是 "systematic comparison"时，顶会接收概率被 novelty 硬性限制。"Comparison/benchmark paper" 在顶会中有接收先例，但 bar 极高——需要实验结论产生 genuinely surprising insights。Proposal 当前的假设设计（H3 预测"effectiveness varies by context"）指向温和、可预测的结论。

2. **Domain Amenability Hypothesis 的 n=2 问题进一步压低天花板**：这是 idea 层面的结构性缺陷。三位审稿人一致判定：从 2 个 domain 归纳 4 条因果条件是 post-hoc overfitting，无法通过更多实验弥补（除非增加第 3、4 个 domain 的验证，但 proposal 未设计此项）。如果 DAH 被审稿人否定，论文退化为"PRM 去偏方法比较"的纯实证工作，novelty 和 significance 进一步下降。

3. **下界 20% 的支撑**：Related Work 极强 + 问题 timely + 实验设计严谨，保证了即使结论平庸，审稿人也会认可执行质量，不至于 strong reject。

4. **上界 30% 的限制**：即使实验产生反直觉结果（如 neuron-level 优于 circuit-level），DAH 的 n=2 逻辑漏洞仍在，且审稿人对 "comparison without new method" 的 novelty 评价不会因此根本改变。取 R2 上界 35% 并下修至 30%，因为 R2 的 35% 场景条件（genuinely surprising results）概率本身不高。

5. **中位 25%**：三个中位的算术平均，在高一致性下直接取中位附近。

【建议】: 边缘（偏不推荐侧）——idea 质量天花板受限于 novelty 和 DAH n=2 问题，但不至于 KILL；如果能在 idea 层面锐化 novelty angle（而非仅靠实验补救），有提升空间。

【实施评估】:
- **计算资源**: 280 H100-hours（约 $560 on-demand），分布于 SAE 训练（70h）、电路追踪（95h）、自修复量化（20h）、干预实验（50h）、缓冲（15h）。需要至少 4-8 张 A100/H100 的集群访问。资源量级中等偏低，对有 GPU 集群访问的实验室完全可行。
- **数据需求**: PRM-BiasBench、ProcessBench、RM-Bench Hard split、PRMBench、Socratic-PRMBench 均为公开 benchmark。对比输入对需自行构造（基于 PRM-BiasBench + Wang et al. 的进化发现流程）。数据需求可满足。
- **人工介入**: 需要研究者手动设计对比输入对、解读电路追踪结果、判断 fluency/reasoning 分类。Wang et al. 的自动化流程可减少部分人工，但电路解读仍需专家判断。人工工作量中等。
- **训练需求**: 需要从头训练 SAE（非 LLM 微调，计算量可控）。不训练新 LLM 或 PRM。CLT 训练（1.5B 规模）有失败风险，已有 fallback 方案。
- **新 Benchmark**: 不需要构建新 benchmark，使用现有公开 benchmark 组合。
- **预估周期**: 10-12 周（含写作），关键路径是 pilot SAE → layer selection → 7B SAE 训练的串行依赖。总体时间线合理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34f2243e-df65-4b03-aadc-a7315dea7353",
  "isSidechain": false,
  "requestId": "req_011CbDHNunUt1sVWZNtpLH6F",
  "type": "assistant",
  "uuid": "fd27c3a6-df91-49fd-bd57-fe2ec4f89c74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01We8WVoNeFX4NBjC2qv3gCF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21425,
      "cache_read_input_tokens": 16908,
      "output_tokens": 3078,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3078,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 21425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21425
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make a grounded evaluation.…",
  "leafUuid": "fd27c3a6-df91-49fd-bd57-fe2ec4f89c74",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "49db71ce-bde2-421e-9106-807e39537aff"
}
```

---
