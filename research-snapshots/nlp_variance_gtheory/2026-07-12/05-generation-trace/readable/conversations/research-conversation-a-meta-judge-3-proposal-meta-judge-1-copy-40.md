# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/112d4811-a19c-430d-b92b-7970ecbe98ef.jsonl`
- **Structured JSON:** [`1095a72e5e0b904ecb14.json`](../../sessions/10/1095a72e5e0b904ecb14.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:19:14.996Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:19:14.996Z",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the full evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [PathFinder-PRM / arXiv:2505.19706] (May 2025): 与本 proposal 高度相关的直接竞争工作。PathFinder-PRM 已经实现了 error-aware hierarchical PRM，先分类 math error 和 consistency error，再组合信号估计 step correctness。在 PRMBench 上达到 SOTA (67.7 PRMScore)。本 proposal 的 ETA-PRM 多头架构与此高度重叠——PathFinder 已经做了 error typing → multi-head → step correctness 的流水线。\n\n2. [ODIN / arXiv:2402.07319] (2024): 本 proposal 明确引用的 baseline。ODIN 用两头 reward model + orthogonality loss 解耦 length 和 quality 信号。本 proposal 的 ODIN-K-orthogonal 变体直接扩展自此工作。\n\n3. [CausalRM / arXiv:2603.18736] (March 2026): 因果分解 reward model，通过因果推断消除 spurious attributes（如 response length, sycophantic phrasing），提升 RLHF 性能。本 proposal 将其作为 Tier 2 baseline。\n\n4. [Reward Under Attack / arXiv:2603.06621] (March 2026): 系统评估 PRM 的 robustness 和 hackability。发现 PRM 本质上是 fluency detector 而非 reasoning verifier——43% reward gains 来自 stylistic shortcuts。提出 PRM-BiasBench，即本 proposal 使用的 Stage 1 工具。\n\n5. [ThinkPRM / arXiv:2504.16828] (April 2025): 生成式 PRM，用 verification chain-of-thought 做 step-wise verification，仅用 PRM800K 1% 数据超越判别式 PRM。本 proposal 将其作为 Tier 3 baseline。\n\n6. [MO-GRPO / arXiv:2509.22047] (2025): 针对 GRPO 在多目标问题上的 reward hacking 提出缓解方案。本 proposal 引用为 Tier 2 robustness check。\n\n7. [Socratic-PRMBench / arXiv:2505.23474] (May 2025): 按 6 种推理模式评估 PRM 的 error detection 能力，20 个细粒度 error type 子类别。本 proposal 将其作为 Tier 3 评估工具。\n\n8. [Robust Reward Modeling via Causal Decomposition / arXiv:2604.13833] (April 2026): 另一个因果分解 reward model 方法，消除影响 reward 信号的 spurious factors。\n\n- **调研总结**: PRM hackability 和 reward decomposition 是 2025-2026 年的活跃研究方向，已有多个独立工作从不同角度（error typing、orthogonality、causal decomposition、generative verification）尝试提高 PRM 鲁棒性。**但这些工作全部属于 NLP/LLM alignment 领域**。本 proposal 本质上是一个 empirical comparison study，将上述已有方法放在统一框架下比较——方法论层面无原创贡献，novelty 集中在实验设计（capacity controls、staged hackability evaluation、三方对比）。\n\n---\n\n⚠️ 【致命问题：投稿方向与会议范围根本不匹配】\n\n**CoRL (Conference on Robot Learning) 是机器人学习会议**。其核心议题包括：robot perception and control、imitation learning for robotics、reinforcement learning for physical robots、sim-to-real transfer、manipulation and locomotion 等。\n\n**本 proposal 的全部内容——PRM hackability、error taxonomy decomposition、mathematical reasoning、GRPO exploitation——100% 属于 NLP/LLM alignment 领域，与机器人学习完全无关。** Proposal 中没有任何一个字涉及机器人、物理控制、感知、操作或任何 CoRL 范围内的主题。\n\n这不是一个\"边界情况\"或\"可以包装一下\"的问题。这是根本性的方向不匹配，会导致 **desk rejection**。\n\n---\n\n【Trivial Alternative 检验】:\n1. **对于 hackability resistance**: \"Reward Under Attack\" (2603.06621) 已经表明 PRM 的根本问题是它们是 fluency detectors 而非 reasoning verifiers。一个 trivial alternative 是：与其在 decomposition basis 上做文章，不如直接用 outcome-based verification（如 ground-truth answer checking）或 generative verification（如 ThinkPRM），这些方法从根本上绕过了 discriminative PRM 的 hackability 问题。ThinkPRM 仅用 1% 数据就超越了判别式 PRM，这暗示 decomposition basis 的选择可能根本不是 hackability resistance 的关键变量。\n2. **对于 multi-head 设计**: PathFinder-PRM 已经用 error-type-aware multi-head 架构达到了 SOTA，且只用了 1/3 的数据。本 proposal 的 ETA-PRM 在架构层面与 PathFinder-PRM 高度相似（error classification → multi-head → aggregation），增量价值不清晰。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有多个未经验证的假设：\n\n1. **\"Decomposition basis 是影响 hackability resistance 的关键变量\"** ——这是整篇 proposal 的核心前提，但没有任何先验理论或实证支持。Hackability 可能主要由训练数据质量、模型规模、RL exploitation 强度等因素决定，而非 decomposition basis 的选择。\n2. **\"Error-taxonomic decomposition 应该优于 data-driven orthogonal decomposition\"** ——这是 proposal 的核心假设（Grounded Orthogonality Hypothesis），但缺乏理论依据。有可能 data-driven 的解耦方式反而更能捕捉到 RL agent 的实际 exploitation 模式，因为它不受人工 taxonomy 的偏见限制。\n3. **\"Coverage breadth（head 数量）与 hackability resistance 之间存在可预测的关系\"** ——假设 hacking 会 shift 到 uncovered dimensions，但 RL agent 的 exploitation 模式可能不遵循人类设计的 error taxonomy 的维度结构。\n4. **\"静态 perturbation → BoN → GRPO 的 staged pipeline 能可靠地衡量 hackability\"** ——虽然引用了 Tiwari et al. 关于 static test 弱预测性的发现，但 BoN → GRPO 的递进关系本身也是未经验证的假设。\n\n【3 维度打分】:\n\n1. **Novelty: 弱**\n   - ETA-PRM 的多头 error-type-aware 架构与 PathFinder-PRM (2505.19706) 高度重叠，后者已在 May 2025 发表，先做了 error classification 再 aggregate 信号\n   - ODIN (2402.07319) 已经做了 orthogonality-enforced decomposition\n   - CausalRM (2603.18736) 已经做了 causal reward decomposition\n   - 本 proposal 的核心贡献是\"把这些已有方法放在一起比较\"——这是实验设计层面的贡献，而非方法论层面的 novelty\n   - 实验设计（capacity controls、staged hackability pipeline、pre-registered predictions）虽然严谨，但实验设计的精巧不构成方法论 novelty\n   - **即使放在 NLP 会议上，这也更像一篇 benchmark/empirical study paper，novelty 有限**\n\n2. **Significance: 致命（对 CoRL）/ 中（对 NLP 会议）**\n   - **对 CoRL**: 研究问题与机器人学习完全无关，significance = 0\n   - **对 NLP 会议（假设投到正确会议）**: 研究问题本身有价值——理解 PRM decomposition 对 hackability 的影响确实重要。但核心发现即使 positive，审稿人大概率的反应是 \"I would have guessed this\"（error taxonomy grounding 优于 random decomposition 并不 surprising）；如果 negative（error taxonomy 并不优于其他方法），反而可能更有价值但 framing 需要大改\n\n3. **Related Work: 中**\n   - 对 PRM hackability 领域的覆盖较为全面，正确引用了 PRM-BiasBench、ODIN、CausalRM、ThinkPRM、MO-GRPO、Socratic-PRMBench 等关键工作\n   - **但完全缺乏任何 robot learning 相关的 related work**，因为 proposal 本身与 robotics 无关\n   - 差异化定位相对于 PathFinder-PRM 不够清晰——两者都做 error-type-aware multi-head PRM，但 proposal 未充分说明 ETA-PRM 与 PathFinder-PRM 的架构差异\n\n【概率估计】: [1% - 5%] 中位 3%\n\n【估计理由】:\n**投稿方向与会议范围的根本不匹配是决定性因素。** 这篇 proposal 100% 是 NLP/LLM alignment 领域的工作，投到 CoRL（机器人学习会议）几乎必然被 desk reject。即使不被 desk reject，也不会进入任何 robotics reviewer 的研究兴趣范围。\n\n退一步讲，即使投到正确的会议（如 NeurIPS、ICML、ACL、EMNLP），概率估计也只在 15-25% 区间：\n- Novelty 弱：核心方法组件均来自已有工作，原创贡献集中在实验设计\n- 核心发现若 positive，不 surprising；若 negative，需要大幅重新 framing\n- PathFinder-PRM 的存在严重压缩了 novelty 空间\n\n上界被 **venue mismatch（致命）** 和 **Novelty（弱）** 双重限制。\n\n【主要风险】:\n1. **致命：投稿方向与 CoRL 会议范围完全不匹配** —— 无任何机器人学习内容，极大概率 desk rejection\n2. **方法论 novelty 不足** —— 核心是已有方法的比较研究，PathFinder-PRM 已覆盖了 error-type-aware multi-head PRM 的主要 idea space，即使换到正确会议也面临 novelty 挑战\n```\n\n---\n\n**总结**：这篇 proposal 存在一个无法通过后续迭代补救的致命问题——**venue mismatch**。它是一篇纯 NLP/LLM alignment 领域的 PRM hackability 实证研究，与 CoRL（Conference on Robot Learning）的机器人学习主题完全无关。建议作者考虑将该工作投到 NeurIPS、ICML、ICLR 或 ACL/EMNLP 等 NLP/ML 会议，并在投稿前重点解决与 PathFinder-PRM 的差异化问题。\n\nSources:\n- [PathFinder-PRM: Error Typing for Smarter Rewards](https://arxiv.org/abs/2505.19706)\n- [ODIN: Disentangled Reward Mitigates Hacking in RLHF](https://arxiv.org/pdf/2402.07319)\n- [CausalRM: Causal-Theoretic Reward Modeling](https://arxiv.org/pdf/2603.18736)\n- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [MO-GRPO: Mitigating Reward Hacking of GRPO](https://arxiv.org/html/2509.22047)\n- [Socratic-PRMBench](https://arxiv.org/html/2505.23474v1)\n- [Robust Reward Modeling via Causal Decomposition](https://arxiv.org/html/2604.13833)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 About](https://www.corl.org/about-corl)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nBased on my research, I now have sufficient information to evaluate this proposal. Let me compile the assessment.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Reward Under Attack: Analyzing the Robustness and Hackability of PRMs] (arXiv 2603.06621, 2026): 直接竞争工作。该论文已经建立了PRM-BiasBench perturbation框架和staged hackability评估方法。本proposal的Stage 1直接引用该工作的方法论。关键发现：RL-induced reward hacking可使PRM reward >0.9而accuracy <4%，43%的reward增益来自stylistic shortcuts。\n- [ODIN: Disentangled Reward Mitigates Hacking in RLHF] (ICLR 2025): 本proposal中\"orthogonality-enforced\"方法的直接来源。ODIN已证明orthogonality loss可有效分离quality vs. length维度以抵御reward hacking。本proposal的ODIN-N变体是对该方法的直接扩展。\n- [Error Typing for Smarter Rewards / PathFinder-PRM] (arXiv 2505.19706, May 2025): 与本proposal的ETA-PRM高度相似。PathFinder-PRM已经实现了error-aware hierarchical PRM (math error + consistency error两个头)并在PRMBench上达到SOTA (67.7)。ETA-PRM本质上是PathFinder-PRM从2维扩展到13维ErrorAtlas对齐。\n- [ErrorMap and ErrorAtlas] (arXiv 2601.15812, Jan 2025): 本proposal的error taxonomy基础。提供17个top-level error类别的model-agnostic taxonomy。已有论文将其用于LLM failure分析，但尚未直接用于PRM multi-head architecture。\n- [CausalRM: Causal-Theoretic Reward Modeling for RLHF] (arXiv 2603.18736, 2026): 本proposal Tier 2中的baseline之一。已展示causal disentanglement在reward modeling中的有效性，跨模型规模(7B-72B)和架构一致改善。\n- [Robust Reward Modeling via Causal Decomposition] (arXiv 2604.13833, 2026): 另一个causal decomposition for reward modeling工作，进一步证明该方向的活跃度。\n- [ThinkPRM: Process Reward Models That Think] (arXiv 2504.16828, April 2025): Tier 3 baseline。生成式PRM，用1K synthetic verification CoTs即可超越discriminative PRMs。\n- [Socratic-PRMBench] (arXiv 2505.23474, May 2025): Tier 3评估工具。发现PRM在不同reasoning patterns上表现极不均衡。\n- [OrthAlign] (arXiv 2509.24610, 2025): 另一个orthogonal subspace decomposition用于multi-objective alignment的工作，证明该技术路线的活跃度。\n- [MR-RML / Multidimensional Rubric-oriented Reward Model] (arXiv 2511.16139, 2025): 多维rubric-oriented reward model，使用geometric projection constraints，与本proposal的多维分解思路相似但目标不同(不关注hackability)。\n\n- 调研总结: PRM hackability是2025-2026年的活跃方向。核心组件(ODIN orthogonality、PathFinder error-aware PRM、ErrorAtlas taxonomy、CausalRM、PRM-BiasBench)均已独立存在。本proposal的定位是\"将这些已有组件组合在一起做一个controlled comparison study\"。尚无直接竞争的decomposition-basis comparison paper，但各个组件单独的anti-hacking效果已被独立验证。\n\n【Trivial Alternative 检验】:\n存在多个更简单的替代方案构成威胁：\n1. **Reward Model Ensemble**: 已有研究（Coste et al. 2023, arXiv 2310.02743）表明简单的reward model ensemble即可显著缓解overoptimization，无需设计复杂的decomposition basis。本proposal未讨论为何multi-head decomposition优于独立ensemble。\n2. **Scale-up**: 已知更大的reward model本身就更难被hack (Gao et al. 2022)。如果同样的参数预算用于训练一个更大的single-head RM，是否能达到类似效果？\n3. **Verifiable Rewards Mix**: 已有证据表明仅混入10%的verifiable rewards即可显著缓解PRM hacking。这是一个极低成本的替代方案。\n4. **ThinkPRM路线**: 生成式verification已展示用极少标注数据即可超越discriminative PRM，可能从根本上绕过了decomposition basis的问题。\n\n增量价值：proposal的增量在于回答\"decomposition basis的choice本身是否matter\"这一机制性问题。但如果reviewer认为这个问题的答案不影响实践（因为有更简单的替代方案解决hackability），则incremental value有限。\n\n【前提假设检验】:\n核心逻辑链中存在多个未经验证的假设：\n1. **假设：RL exploitation主要通过\"未覆盖维度\"进行** — 这是proposal预测\"hacking shifts to uncovered dimensions\"的前提。但Tiwari et al.的发现（43% stylistic shortcuts）暗示exploitation可能更多通过\"covered but poorly calibrated\"维度进行，而非\"uncovered\"维度。\n2. **假设：ErrorAtlas的17类taxonomy能穷举exploitable reward dimensions** — ErrorAtlas是为错误分类设计的，不是为reward hacking攻击面设计的。RL可能找到taxonomy内部的漏洞（如某个error type head的calibration gap），而非taxonomy外的维度。\n3. **假设：weight-space orthogonality (ODIN) 和 semantic grounding (ETA) 产生meaningfully different representations** — 如果data-driven orthogonal decomposition自然收敛到类似semantic dimensions，则三者的区别可能很小，核心comparison变得无意义。\n4. **假设：CKA distance是检测\"Grounded Orthogonality Hypothesis\"的正确度量** — CKA的sensitivity是否足以区分这些subtle differences尚无先验证据。\n\n【3 维度打分】:\n1. Novelty: 弱 — \n核心方法ETA-PRM是PathFinder-PRM (2505.19706, 2 error heads) 的直接扩展至13 heads + ErrorAtlas对齐，增量有限。ODIN baseline直接来自ICLR 2025同名论文。CausalRM直接来自arXiv 2603.18736。PRM-BiasBench pipeline直接来自arXiv 2603.06621。本proposal的实质novelty是\"将已有组件组装在一起做comparison\"——这是experimental design层面的贡献，不是method层面的贡献。\"Grounded Orthogonality Hypothesis\"是一个有趣的hypothesis但本身只是对\"semantic labels vs. random labels\"这个常见ablation的命名包装。Random-N capacity control是good practice但不是novelty。\n\n2. Significance: 中 — \nPRM hackability是一个genuinely important problem（Tiwari et al.证明的43% stylistic exploitation严重影响RL训练可靠性）。回答\"decomposition basis是否matter\"这个问题对该领域有一定指导意义。但意义受限于：(a) 限于math reasoning domain; (b) 存在orthogonal替代方案（ensemble, scale, verifiable rewards）可能从根本上绕过该问题; (c) 如果answer是positive（semantic decomposition更好），多数审稿人会说\"I would have guessed this\"——毕竟semantic grounding优于random是一个符合直觉的结果。如果answer是negative（不matter），则更surprising但also更难publish（null result在top venue很难sell）。\n\n3. Related Work: 中 — \nProposal覆盖了该领域的主要工作（ODIN, PathFinder-PRM, CausalRM, ThinkPRM, PRM-BiasBench, Socratic-PRMBench）。但存在显著遗漏：(a) 未讨论reward model ensemble作为competing approach; (b) 未讨论Bayesian Non-negative Reward Modeling (2602.10623); (c) 未讨论PURE (min-form credit assignment, 2504.15275)作为另一类anti-hacking机制; (d) 未讨论verifiable rewards混合策略。差异化定位为\"first controlled comparison study\"是准确的但也暴露了本质是comparison study而非method paper。\n\n【概率估计】: [12% - 22%] 中位 17%\n【估计理由】: Novelty维度是主要限制因素。本proposal本质上是一个empirical comparison study，将已有组件（ODIN, PathFinder-PRM, ErrorAtlas, CausalRM, PRM-BiasBench）组装在一起。核心method (ETA-PRM) 是PathFinder-PRM的直接13维扩展，novelty delta有限。研究问题的答案无论是positive还是negative都不太可能产生\"surprising\"反应：semantic grounding > random是直觉符合的；如果不matter则是null result。此外，存在多个trivial alternatives (ensemble, scale, verifiable rewards) 的威胁，审稿人很可能追问\"为什么不直接用ensemble？\"。形式上虽然极其完善（tiered design, pre-registered predictions, capacity controls），但top venue（假设投NeurIPS/ICML/ICLR等ML会议）对comparison study的bar很高，通常需要novel insight或counter-intuitive finding来支撑。如果投CoRL（Conference on Robot Learning），还存在严重的venue mismatch——本文完全关于math reasoning PRM，与robot learning无关。\n\n【主要风险】:\n1. **\"Comparison Study\" 身份风险**: 审稿人很可能认为这是\"putting together existing methods and comparing them\"，而非提出genuinely new insight。Top venue对pure empirical comparison的acceptance bar远高于method paper——需要产生counter-intuitive或high-impact finding才能过线。\n2. **Trivial Alternative 威胁**: Reward model ensemble已被证明可有效缓解overoptimization且实现成本远低于multi-head decomposition architecture。如果reviewer追问\"why not just ensemble multiple RMs?\"，proposal缺乏convincing response来证明decomposition basis comparison的必要性。\n```\n\nSources:\n- [Reward Under Attack: Analyzing the Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)\n- [ODIN: Disentangled Reward Mitigates Hacking in RLHF (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf)\n- [Error Typing for Smarter Rewards / PathFinder-PRM](https://arxiv.org/abs/2505.19706)\n- [ErrorMap and ErrorAtlas](https://arxiv.org/html/2601.15812v1)\n- [CausalRM: Causal-Theoretic Reward Modeling](https://www.alphaxiv.org/overview/2603.18736v1)\n- [Robust Reward Modeling via Causal Decomposition](https://arxiv.org/abs/2604.13833)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [Socratic-PRMBench](https://arxiv.org/html/2505.23474v1)\n- [OrthAlign: Orthogonal Subspace Decomposition](https://arxiv.org/pdf/2509.24610)\n- [MR-RML: Multidimensional Rubric-oriented Reward Model](https://arxiv.org/html/2511.16139v1)\n- [Reward Model Ensembles Mitigate Overoptimization](https://arxiv.org/pdf/2310.02743)\n- [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760)\n- [PURE: Min-Form Credit Assignment](https://arxiv.org/pdf/2504.15275)\n- [Bayesian Non-negative Reward Modeling](https://arxiv.org/pdf/2602.10623)\n- [Awesome Reward Hacking Repository](https://github.com/xhwang22/Awesome-Reward-Hacking)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **\"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision\" (arXiv 2505.19706, May 2025)**:\n   - 提出 PathFinder-PRM，一个层次化、error-aware 的判别式 PRM，先分类每步的 math error 和 consistency error，再聚合细粒度信号估计步骤正确性。\n   - **与本 proposal 的关系：极度直接竞争。** 本 proposal 的核心 idea——用 error taxonomy 分解 PRM 监督信号——已被 PathFinder-PRM 实现。PathFinder-PRM 在 PRMBench 上取得 SOTA (67.7)，且只用 3× less data。本 proposal 的 ETA-PRM 本质上是 PathFinder-PRM 的扩展版（从 2 维 error type 扩展到 13 维 ErrorAtlas 分类），而非全新方法。\n\n2. **ODIN: Disentangled Reward Mitigates Hacking in RLHF (arXiv 2402.07319, ICML 2024)**:\n   - 提出正交解耦奖励模型，两个 head 分别学习 quality reward 和 length，用正交 loss 去耦合。\n   - **与本 proposal 的关系：** 本 proposal 将 ODIN 作为 baseline 之一进行比较，但 ODIN 原始设计仅针对 length bias，扩展到 6-head 正交分解是 proposal 的设定，不是 ODIN 原始工作。\n\n3. **CausalRM: Causal-Theoretic Reward Modeling (arXiv 2603.18736, March 2026)**:\n   - 用因果推断框架学习去偏的 reward model，显式建模 annotation error 的生成过程。\n   - **与本 proposal 的关系：** 作为 Tier 2 的 baseline 被纳入，但 CausalRM 的 causal decomposition 和本 proposal 的 error-type decomposition 解决的是不同层面的问题。\n\n4. **\"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" (arXiv 2603.06621, March 2026)**:\n   - 系统分析 PRM 的 hackability，发现 PRM 对 surface-level 扰动高度不变但对 logical corruption 检测不一致；RL 训练后的 policy 能达到 >0.9 PRM reward 但 ground-truth accuracy <4%。\n   - **与本 proposal 的关系：** 直接建立了 PRM hackability 的实证基础。本 proposal 引用的 Tiwari et al. 关于 \"static perturbation tests weakly predict RL-based exploitation\" 的发现与此一致。但注意：本 proposal 的 staged evaluation pipeline 本质上是对这篇工作方法论的重组，而非根本创新。\n\n5. **ThinkPRM: Process Reward Models That Think (arXiv 2504.16828, April 2025)**:\n   - 用长 CoT 验证替代判别式 PRM，仅需 8K process labels 就超越 PRM800K 训练的判别式模型。\n   - **与本 proposal 的关系：** 被列为 Tier 3 baseline。ThinkPRM 代表了一种完全不同的 PRM 范式（generative verification vs. discriminative scoring），可能是本 proposal 多头判别式架构的 trivial alternative。\n\n6. **MO-GRPO (arXiv 2509.22047)**:\n   - 多目标 GRPO 缓解 reward hacking，评估 GRPO 在 under-specified reward model 下的表现。\n   - **与本 proposal 的关系：** 作为 Tier 2 的 robustness check 被纳入。\n\n7. **ErrorAtlas / ErrorMap (arXiv 2601.15812, Jan 2026)**:\n   - 17 类顶层 LLM 错误分类的 model-agnostic taxonomy，跨 35 datasets 和 83 models 生成。\n   - **与本 proposal 的关系：** 本 proposal 的 ETA-PRM 13 个 head 直接对齐 ErrorAtlas 的分类体系。ErrorAtlas 本身是描述性工具（事后分类错误），将其转化为 PRM 的监督信号是本 proposal 的核心操作之一。\n\n8. **Socratic-PRMBench (arXiv 2505.23474, May 2025)**:\n   - 用 6 种推理模式（Transformation, Decomposition, Regather, Deduction, Verification, Integration）系统评估 PRM。\n   - **与本 proposal 的关系：** 被列为 Tier 3 评估工具。\n\n- **调研总结：** PRM hackability 是 2025-2026 年的活跃研究方向。error-aware 多头 PRM（PathFinder-PRM）、正交分解（ODIN）、因果分解（CausalRM）、generative PRM（ThinkPRM）等多种方法已被提出。本 proposal 的定位是\"第一个系统比较不同 decomposition basis 对 hackability resistance 影响的受控研究\"，但其核心方法（error-type multi-head PRM）与 PathFinder-PRM 高度重叠，且 hackability 评估 pipeline 基本是 \"Reward Under Attack\" 方法论的结构化重组。\n\n\n【致命问题：投稿 venue 严重不匹配】:\n\n**CoRL (Conference on Robot Learning) 是一个专注于机器人学习的会议。** 其 Call for Papers 明确要求论文聚焦于 \"the intersection of robotics and machine learning\"，涵盖的主题包括：robotic perception and control, robot foundation models, imitation learning, RL for physical robots, human-robot interaction, robot safety 等。\n\n本 proposal 是关于 LLM 数学推理的 Process Reward Model hackability resistance 研究，**与机器人学零关联**。即使 idea 质量极高，投稿 CoRL 也会因 scope mismatch 而被 desk reject。\n\n**合适的投稿 venue：** NeurIPS 2026, ICML 2026, ICLR 2027, ACL 2026, EMNLP 2026。\n\n\n【Trivial Alternative 检验】:\n\n存在多个更简单的替代方案可能达到类似效果：\n\n1. **ThinkPRM (generative verification)：** 不需要任何 multi-head 架构设计、不需要 error taxonomy annotation、仅需 8K labels，就在 OOD 评估上超越了用完整 PRM800K 训练的判别式 PRM。如果目标是 hackability resistance，generative verification 可能天然比 discriminative multi-head 更 robust（因为它验证推理过程而非打分），且成本远低于标注 13 种 error type。\n\n2. **简单的 ensemble：** 与其构建 13-head 架构，直接 ensemble 多个独立训练的 PRM（各自侧重不同 error aspect）可能达到类似效果，且实现更简单。\n\n3. **对抗训练：** 直接用已知 hack patterns 做 adversarial training 可能是更 targeted 的 hackability defense，而不需要走 decomposition 路线。\n\n**增量价值：** 本 proposal 的真正增量价值不在于提出新方法，而在于**系统性比较的实验设计本身**——capacity controls、staged hackability evaluation、Grounded Orthogonality Hypothesis 的 falsifiable predictions。但这更像一篇 benchmarking/empirical study 而非方法创新。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **\"Error taxonomy grounding 能提供比 data-driven orthogonality 更好的 hackability resistance\"——这是核心假设，但缺乏理论支撑。** 为什么基于人类定义的 error taxonomy 的分解会比数据驱动的正交分解更难被 hack？一个可能的反论是：RL exploit 找到的是 reward landscape 中的低谷/漏洞，这些漏洞可能恰好对齐于人类定义的 error boundaries（因为 taxonomy 是有限的、离散的），而数据驱动的分解可能覆盖更连续的空间。\n\n2. **\"Coverage breadth 的增加会线性/单调地提高 hackability resistance\"——未验证。** 增加 head 数可能引入新的 hack surfaces（每个 head 都是一个可被 exploit 的模块），或导致 head 之间的干扰降低整体鲁棒性。\n\n3. **\"ErrorAtlas 的 17 类分类体系适用于 PRM step-level 监督\"——跨粒度假设。** ErrorAtlas 是对 LLM 最终输出的事后错误分类，直接用于 step-level PRM 监督需要假设 step-level errors 和 output-level errors 遵循相同的 taxonomy，但中间推理步骤的错误模式可能与最终输出的错误模式有本质不同。\n\n4. **\"Grounded Orthogonality Hypothesis 的 falsifiability 取决于 CKA distance 和 selective perturbation sensitivity 的可靠测量\"——测量方法的假设。** CKA 作为表征相似性度量在高维空间中的 discriminative power 有限，可能无法区分 semantically grounded vs. data-driven orthogonality 的细微差异。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱**\n   - 核心方法 ETA-PRM（error-type multi-head PRM）与 PathFinder-PRM (arXiv 2505.19706, May 2025) 高度重叠——后者已实现 error-aware hierarchical PRM，只是用 2 种 error type（math + consistency）而非 13 种。从 2 种扩展到 13 种是 engineering scaling，不是 conceptual novelty。\n   - 不同 decomposition basis 的比较本身是一个有价值的研究问题，但核心是 empirical comparison，不是新方法。\n   - Staged hackability evaluation pipeline 基本是 \"Reward Under Attack\" (arXiv 2603.06621) 方法论的重组（perturbation → BoN → RL exploitation），每个 stage 单独都不新。\n   - \"Grounded Orthogonality Hypothesis\" 是一个有趣的假设，但它更像是实验设计中的一个 analysis angle，而非独立的 intellectual contribution。\n   - **综合来看：** 个别元素有增量价值（capacity controls, 系统性比较框架），但整体 novelty 不足以支撑顶会。\n\n2. **Significance: 中**\n   - PRM hackability 是 RLHF/alignment 领域的重要问题，\"Reward Under Attack\" 已证明当前 PRM 严重不可靠（reward >0.9 但 accuracy <4%）。\n   - 理解不同 decomposition basis 的效果确实对 PRM 设计有指导意义。\n   - **但受限因素：**（a）仅限数学推理域，proposal 自己也承认是 \"domain-specific validation\"；（b）即使发现 error-taxonomic 最优，其可推广性存疑——不同 domain 的 error taxonomy 完全不同，无法直接迁移；（c）如果审稿人的反应是 \"I would have guessed that semantic grounding helps more than random orthogonality\"，则 significance 大打折扣。\n   - 目标 venue CoRL 的 significance 更是几乎为零，因为与机器人学无关。\n\n3. **Related Work: 中**\n   - 对 ODIN, CausalRM, ThinkPRM, ErrorAtlas, Socratic-PRMBench 等有覆盖，差异化定位（\"第一个系统比较 decomposition basis\"）是清晰的。\n   - **但存在问题：**（a）PathFinder-PRM (arXiv 2505.19706) 是最直接的竞争者，proposal 是否充分 acknowledge 了与它的重叠？PathFinder-PRM 作为 \"PathFinder trajectory-level\" baseline 出现在 proposal 中，但 proposal 似乎将其定位为 trajectory-level 方法而非 error-type-aware 方法，这可能 mischaracterize 了 PathFinder-PRM 的贡献（它的核心恰恰是 error-type-aware）。（b）PRM-BiasBench 和 Tiwari et al. 的引用未在公开文献中找到确切匹配——需要验证这些引用是否准确。\n\n\n【概率估计】: [1% - 5%] 中位 2%\n\n【估计理由】:\n- **venue mismatch 是 decisive factor：** CoRL 是 robotics 会议，本 proposal 是纯 NLP/RLHF 方向，几乎确定会被 desk reject。仅此一项就将概率压到 <5%。\n- **即使投到合适 venue (NeurIPS/ICML/ICLR)，重新估计：**\n  - Novelty 弱：核心方法与 PathFinder-PRM 重叠，整体定位为 empirical comparison study\n  - Significance 中：问题重要但预期发现不够 surprising\n  - 在合适 venue 的估计概率约 15-25%\n- **上界限制因素：** Novelty 维度。这本质上是一个精心设计的 ablation/comparison study，而非提出新 insight 或新方法。顶会通常需要至少一个维度达到\"强\"。\n\n【主要风险】:\n1. **致命 venue 不匹配：** CoRL 是 robot learning 会议，本 proposal 关于 LLM 数学推理的 PRM hackability，与 robotics 完全无关，极大概率 desk reject。\n2. **Novelty 不足：** 核心方法（error-type multi-head PRM）已被 PathFinder-PRM 实现；整体贡献定位为 empirical comparison + ablation study，缺乏足以支撑顶会的 conceptual innovation。审稿人最可能的批评是 \"an extensive ablation study of known ideas, not a novel contribution.\"\n```\n\n---\n\n**关键提醒：** 本 proposal 投稿 CoRL 2026 存在**致命的 venue 不匹配**问题。CoRL (Conference on Robot Learning) 聚焦于机器人学习，要求论文涉及 robotics + ML 的交叉领域。本 proposal 是纯 NLP/RLHF 方向（LLM 数学推理的 PRM hackability），与 robotics 零关联。建议改投 NeurIPS 2026、ICML 2026、ICLR 2027、ACL 2026 或 EMNLP 2026 等 NLP/ML 主流会议。\n\nSources:\n- [Error Typing for Smarter Rewards (PathFinder-PRM)](https://arxiv.org/abs/2505.19706)\n- [ODIN: Disentangled Reward Mitigates Hacking in RLHF](https://arxiv.org/pdf/2402.07319)\n- [CausalRM: Causal-Theoretic Reward Modeling](https://arxiv.org/pdf/2603.18736)\n- [Reward Under Attack: Analyzing PRM Hackability](https://arxiv.org/abs/2603.06621)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [ErrorAtlas / ErrorMap](https://arxiv.org/abs/2601.15812)\n- [Socratic-PRMBench](https://arxiv.org/abs/2505.23474)\n- [MO-GRPO](https://arxiv.org/pdf/2509.22047)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal Reward Decomposition for PRM Hackability Resistance\n\n## Description\nWe present the first systematic empirical study of how decomposition basis and coverage breadth jointly affect PRM hackability resistance, organized as a tiered experimental program with staged evaluation and capacity controls. Our two central questions: (1) Does the CHOICE of decomposition basis matter — specifically, does grounding multi-dimensional supervision in a systematic error taxonomy outperform orthogonality-enforced, quality-dimension, and causal alternatives? (2) How does coverage breadth (number of supervised error dimensions) affect hackability, and does hacking shift to uncovered dimensions as theory predicts? We introduce ETA-PRM (Error-Type-Aware PRM), a multi-head architecture with up to 13 ErrorAtlas-aligned error-type heads plus a residual head. The guaranteed Tier 1 deliverable compares four decomposition approaches (ETA error-taxonomic, ODIN data-driven orthogonal, single-head, PathFinder trajectory-level) across a 4-level coverage ablation (2→6→13→13+residual heads), with Random-N capacity controls (N=2,6,13) at each coverage level to disentangle coverage breadth from model capacity. The critical three-way comparison — ETA-PRM-6 (error-type labels) vs. ODIN-6-orthogonal (random labels + orthogonality loss) vs. Random-6 (random labels, no orthogonality) — isolates whether semantic grounding, orthogonality enforcement, or raw capacity drives hackability resistance. Hackability is measured through a staged pipeline motivated by Tiwari et al.'s finding that static perturbation tests weakly predict RL-based exploitation: Stage 1 applies PRM-BiasBench perturbations for surface profiling and GOH sensitivity analysis, Stage 2 traces Best-of-N overoptimization curves as an intermediate proxy, and Stage 3 runs full GRPO exploitation on core variants with 3 seeds and paired bootstrap confidence intervals. The Grounded Orthogonality Hypothesis is tested via pre-registered, falsifiable predictions: comparable overall debiased CKA distance but divergent selective perturbation sensitivity (ETA-PRM heads sensitive to matching perturbation types vs. ODIN heads showing uniform sensitivity). Tier 2 extends to CausalRM and DRM baselines, cross-scale robustness verification (Qwen2.5-Math-1.5B-Instruct backbone), and MO-GRPO robustness checks to rule out RL-algorithm-specific exploitation artifacts; Tier 3 adds ThinkPRM comparison, Socratic-PRMBench reasoning-pattern evaluation, and full mechanistic analysis. All evaluation is on mathematical reasoning, explicitly acknowledged as domain-specific validation with methodology designed for cross-domain extension. This is the first controlled study varying both decomposition basis and coverage breadth with capacity controls, staged hackability evaluation, pre-registered mechanistic predictions, and statistical rigor.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:19:14.998Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:19:14.998Z",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:19:15.009Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the full evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. [PathFinder-PRM / arXiv:2505.19706] (May 2025): 与本 proposal 高度相关的直接竞争工作。PathFinder-PRM 已经实现了 error-aware hierarchical PRM，先分类 math error 和 consistency error，再组合信号估计 step correctness。在 PRMBench 上达到 SOTA (67.7 PRMScore)。本 proposal 的 ETA-PRM 多头架构与此高度重叠——PathFinder 已经做了 error typing → multi-head → step correctness 的流水线。

2. [ODIN / arXiv:2402.07319] (2024): 本 proposal 明确引用的 baseline。ODIN 用两头 reward model + orthogonality loss 解耦 length 和 quality 信号。本 proposal 的 ODIN-K-orthogonal 变体直接扩展自此工作。

3. [CausalRM / arXiv:2603.18736] (March 2026): 因果分解 reward model，通过因果推断消除 spurious attributes（如 response length, sycophantic phrasing），提升 RLHF 性能。本 proposal 将其作为 Tier 2 baseline。

4. [Reward Under Attack / arXiv:2603.06621] (March 2026): 系统评估 PRM 的 robustness 和 hackability。发现 PRM 本质上是 fluency detector 而非 reasoning verifier——43% reward gains 来自 stylistic shortcuts。提出 PRM-BiasBench，即本 proposal 使用的 Stage 1 工具。

5. [ThinkPRM / arXiv:2504.16828] (April 2025): 生成式 PRM，用 verification chain-of-thought 做 step-wise verification，仅用 PRM800K 1% 数据超越判别式 PRM。本 proposal 将其作为 Tier 3 baseline。

6. [MO-GRPO / arXiv:2509.22047] (2025): 针对 GRPO 在多目标问题上的 reward hacking 提出缓解方案。本 proposal 引用为 Tier 2 robustness check。

7. [Socratic-PRMBench / arXiv:2505.23474] (May 2025): 按 6 种推理模式评估 PRM 的 error detection 能力，20 个细粒度 error type 子类别。本 proposal 将其作为 Tier 3 评估工具。

8. [Robust Reward Modeling via Causal Decomposition / arXiv:2604.13833] (April 2026): 另一个因果分解 reward model 方法，消除影响 reward 信号的 spurious factors。

- **调研总结**: PRM hackability 和 reward decomposition 是 2025-2026 年的活跃研究方向，已有多个独立工作从不同角度（error typing、orthogonality、causal decomposition、generative verification）尝试提高 PRM 鲁棒性。**但这些工作全部属于 NLP/LLM alignment 领域**。本 proposal 本质上是一个 empirical comparison study，将上述已有方法放在统一框架下比较——方法论层面无原创贡献，novelty 集中在实验设计（capacity controls、staged hackability evaluation、三方对比）。

---

⚠️ 【致命问题：投稿方向与会议范围根本不匹配】

**CoRL (Conference on Robot Learning) 是机器人学习会议**。其核心议题包括：robot perception and control、imitation learning for robotics、reinforcement learning for physical robots、sim-to-real transfer、manipulation and locomotion 等。

**本 proposal 的全部内容——PRM hackability、error taxonomy decomposition、mathematical reasoning、GRPO exploitation——100% 属于 NLP/LLM alignment 领域，与机器人学习完全无关。** Proposal 中没有任何一个字涉及机器人、物理控制、感知、操作或任何 CoRL 范围内的主题。

这不是一个"边界情况"或"可以包装一下"的问题。这是根本性的方向不匹配，会导致 **desk rejection**。

---

【Trivial Alternative 检验】:
1. **对于 hackability resistance**: "Reward Under Attack" (2603.06621) 已经表明 PRM 的根本问题是它们是 fluency detectors 而非 reasoning verifiers。一个 trivial alternative 是：与其在 decomposition basis 上做文章，不如直接用 outcome-based verification（如 ground-truth answer checking）或 generative verification（如 ThinkPRM），这些方法从根本上绕过了 discriminative PRM 的 hackability 问题。ThinkPRM 仅用 1% 数据就超越了判别式 PRM，这暗示 decomposition basis 的选择可能根本不是 hackability resistance 的关键变量。
2. **对于 multi-head 设计**: PathFinder-PRM 已经用 error-type-aware multi-head 架构达到了 SOTA，且只用了 1/3 的数据。本 proposal 的 ETA-PRM 在架构层面与 PathFinder-PRM 高度相似（error classification → multi-head → aggregation），增量价值不清晰。

【前提假设检验】:
核心 claim 的逻辑链条中有多个未经验证的假设：

1. **"Decomposition basis 是影响 hackability resistance 的关键变量"** ——这是整篇 proposal 的核心前提，但没有任何先验理论或实证支持。Hackability 可能主要由训练数据质量、模型规模、RL exploitation 强度等因素决定，而非 decomposition basis 的选择。
2. **"Error-taxonomic decomposition 应该优于 data-driven orthogonal decomposition"** ——这是 proposal 的核心假设（Grounded Orthogonality Hypothesis），但缺乏理论依据。有可能 data-driven 的解耦方式反而更能捕捉到 RL agent 的实际 exploitation 模式，因为它不受人工 taxonomy 的偏见限制。
3. **"Coverage breadth（head 数量）与 hackability resistance 之间存在可预测的关系"** ——假设 hacking 会 shift 到 uncovered dimensions，但 RL agent 的 exploitation 模式可能不遵循人类设计的 error taxonomy 的维度结构。
4. **"静态 perturbation → BoN → GRPO 的 staged pipeline 能可靠地衡量 hackability"** ——虽然引用了 Tiwari et al. 关于 static test 弱预测性的发现，但 BoN → GRPO 的递进关系本身也是未经验证的假设。

【3 维度打分】:

1. **Novelty: 弱**
   - ETA-PRM 的多头 error-type-aware 架构与 PathFinder-PRM (2505.19706) 高度重叠，后者已在 May 2025 发表，先做了 error classification 再 aggregate 信号
   - ODIN (2402.07319) 已经做了 orthogonality-enforced decomposition
   - CausalRM (2603.18736) 已经做了 causal reward decomposition
   - 本 proposal 的核心贡献是"把这些已有方法放在一起比较"——这是实验设计层面的贡献，而非方法论层面的 novelty
   - 实验设计（capacity controls、staged hackability pipeline、pre-registered predictions）虽然严谨，但实验设计的精巧不构成方法论 novelty
   - **即使放在 NLP 会议上，这也更像一篇 benchmark/empirical study paper，novelty 有限**

2. **Significance: 致命（对 CoRL）/ 中（对 NLP 会议）**
   - **对 CoRL**: 研究问题与机器人学习完全无关，significance = 0
   - **对 NLP 会议（假设投到正确会议）**: 研究问题本身有价值——理解 PRM decomposition 对 hackability 的影响确实重要。但核心发现即使 positive，审稿人大概率的反应是 "I would have guessed this"（error taxonomy grounding 优于 random decomposition 并不 surprising）；如果 negative（error taxonomy 并不优于其他方法），反而可能更有价值但 framing 需要大改

3. **Related Work: 中**
   - 对 PRM hackability 领域的覆盖较为全面，正确引用了 PRM-BiasBench、ODIN、CausalRM、ThinkPRM、MO-GRPO、Socratic-PRMBench 等关键工作
   - **但完全缺乏任何 robot learning 相关的 related work**，因为 proposal 本身与 robotics 无关
   - 差异化定位相对于 PathFinder-PRM 不够清晰——两者都做 error-type-aware multi-head PRM，但 proposal 未充分说明 ETA-PRM 与 PathFinder-PRM 的架构差异

【概率估计】: [1% - 5%] 中位 3%

【估计理由】:
**投稿方向与会议范围的根本不匹配是决定性因素。** 这篇 proposal 100% 是 NLP/LLM alignment 领域的工作，投到 CoRL（机器人学习会议）几乎必然被 desk reject。即使不被 desk reject，也不会进入任何 robotics reviewer 的研究兴趣范围。

退一步讲，即使投到正确的会议（如 NeurIPS、ICML、ACL、EMNLP），概率估计也只在 15-25% 区间：
- Novelty 弱：核心方法组件均来自已有工作，原创贡献集中在实验设计
- 核心发现若 positive，不 surprising；若 negative，需要大幅重新 framing
- PathFinder-PRM 的存在严重压缩了 novelty 空间

上界被 **venue mismatch（致命）** 和 **Novelty（弱）** 双重限制。

【主要风险】:
1. **致命：投稿方向与 CoRL 会议范围完全不匹配** —— 无任何机器人学习内容，极大概率 desk rejection
2. **方法论 novelty 不足** —— 核心是已有方法的比较研究，PathFinder-PRM 已覆盖了 error-type-aware multi-head PRM 的主要 idea space，即使换到正确会议也面临 novelty 挑战
```

---

**总结**：这篇 proposal 存在一个无法通过后续迭代补救的致命问题——**venue mismatch**。它是一篇纯 NLP/LLM alignment 领域的 PRM hackability 实证研究，与 CoRL（Conference on Robot Learning）的机器人学习主题完全无关。建议作者考虑将该工作投到 NeurIPS、ICML、ICLR 或 ACL/EMNLP 等 NLP/ML 会议，并在投稿前重点解决与 PathFinder-PRM 的差异化问题。

Sources:
- [PathFinder-PRM: Error Typing for Smarter Rewards](https://arxiv.org/abs/2505.19706)
- [ODIN: Disentangled Reward Mitigates Hacking in RLHF](https://arxiv.org/pdf/2402.07319)
- [CausalRM: Causal-Theoretic Reward Modeling](https://arxiv.org/pdf/2603.18736)
- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [MO-GRPO: Mitigating Reward Hacking of GRPO](https://arxiv.org/html/2509.22047)
- [Socratic-PRMBench](https://arxiv.org/html/2505.23474v1)
- [Robust Reward Modeling via Causal Decomposition](https://arxiv.org/html/2604.13833)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Based on my research, I now have sufficient information to evaluate this proposal. Let me compile the assessment.

```
【阶段】: Triage

【领域调研】:
- [Reward Under Attack: Analyzing the Robustness and Hackability of PRMs] (arXiv 2603.06621, 2026): 直接竞争工作。该论文已经建立了PRM-BiasBench perturbation框架和staged hackability评估方法。本proposal的Stage 1直接引用该工作的方法论。关键发现：RL-induced reward hacking可使PRM reward >0.9而accuracy <4%，43%的reward增益来自stylistic shortcuts。
- [ODIN: Disentangled Reward Mitigates Hacking in RLHF] (ICLR 2025): 本proposal中"orthogonality-enforced"方法的直接来源。ODIN已证明orthogonality loss可有效分离quality vs. length维度以抵御reward hacking。本proposal的ODIN-N变体是对该方法的直接扩展。
- [Error Typing for Smarter Rewards / PathFinder-PRM] (arXiv 2505.19706, May 2025): 与本proposal的ETA-PRM高度相似。PathFinder-PRM已经实现了error-aware hierarchical PRM (math error + consistency error两个头)并在PRMBench上达到SOTA (67.7)。ETA-PRM本质上是PathFinder-PRM从2维扩展到13维ErrorAtlas对齐。
- [ErrorMap and ErrorAtlas] (arXiv 2601.15812, Jan 2025): 本proposal的error taxonomy基础。提供17个top-level error类别的model-agnostic taxonomy。已有论文将其用于LLM failure分析，但尚未直接用于PRM multi-head architecture。
- [CausalRM: Causal-Theoretic Reward Modeling for RLHF] (arXiv 2603.18736, 2026): 本proposal Tier 2中的baseline之一。已展示causal disentanglement在reward modeling中的有效性，跨模型规模(7B-72B)和架构一致改善。
- [Robust Reward Modeling via Causal Decomposition] (arXiv 2604.13833, 2026): 另一个causal decomposition for reward modeling工作，进一步证明该方向的活跃度。
- [ThinkPRM: Process Reward Models That Think] (arXiv 2504.16828, April 2025): Tier 3 baseline。生成式PRM，用1K synthetic verification CoTs即可超越discriminative PRMs。
- [Socratic-PRMBench] (arXiv 2505.23474, May 2025): Tier 3评估工具。发现PRM在不同reasoning patterns上表现极不均衡。
- [OrthAlign] (arXiv 2509.24610, 2025): 另一个orthogonal subspace decomposition用于multi-objective alignment的工作，证明该技术路线的活跃度。
- [MR-RML / Multidimensional Rubric-oriented Reward Model] (arXiv 2511.16139, 2025): 多维rubric-oriented reward model，使用geometric projection constraints，与本proposal的多维分解思路相似但目标不同(不关注hackability)。

- 调研总结: PRM hackability是2025-2026年的活跃方向。核心组件(ODIN orthogonality、PathFinder error-aware PRM、ErrorAtlas taxonomy、CausalRM、PRM-BiasBench)均已独立存在。本proposal的定位是"将这些已有组件组合在一起做一个controlled comparison study"。尚无直接竞争的decomposition-basis comparison paper，但各个组件单独的anti-hacking效果已被独立验证。

【Trivial Alternative 检验】:
存在多个更简单的替代方案构成威胁：
1. **Reward Model Ensemble**: 已有研究（Coste et al. 2023, arXiv 2310.02743）表明简单的reward model ensemble即可显著缓解overoptimization，无需设计复杂的decomposition basis。本proposal未讨论为何multi-head decomposition优于独立ensemble。
2. **Scale-up**: 已知更大的reward model本身就更难被hack (Gao et al. 2022)。如果同样的参数预算用于训练一个更大的single-head RM，是否能达到类似效果？
3. **Verifiable Rewards Mix**: 已有证据表明仅混入10%的verifiable rewards即可显著缓解PRM hacking。这是一个极低成本的替代方案。
4. **ThinkPRM路线**: 生成式verification已展示用极少标注数据即可超越discriminative PRM，可能从根本上绕过了decomposition basis的问题。

增量价值：proposal的增量在于回答"decomposition basis的choice本身是否matter"这一机制性问题。但如果reviewer认为这个问题的答案不影响实践（因为有更简单的替代方案解决hackability），则incremental value有限。

【前提假设检验】:
核心逻辑链中存在多个未经验证的假设：
1. **假设：RL exploitation主要通过"未覆盖维度"进行** — 这是proposal预测"hacking shifts to uncovered dimensions"的前提。但Tiwari et al.的发现（43% stylistic shortcuts）暗示exploitation可能更多通过"covered but poorly calibrated"维度进行，而非"uncovered"维度。
2. **假设：ErrorAtlas的17类taxonomy能穷举exploitable reward dimensions** — ErrorAtlas是为错误分类设计的，不是为reward hacking攻击面设计的。RL可能找到taxonomy内部的漏洞（如某个error type head的calibration gap），而非taxonomy外的维度。
3. **假设：weight-space orthogonality (ODIN) 和 semantic grounding (ETA) 产生meaningfully different representations** — 如果data-driven orthogonal decomposition自然收敛到类似semantic dimensions，则三者的区别可能很小，核心comparison变得无意义。
4. **假设：CKA distance是检测"Grounded Orthogonality Hypothesis"的正确度量** — CKA的sensitivity是否足以区分这些subtle differences尚无先验证据。

【3 维度打分】:
1. Novelty: 弱 — 
核心方法ETA-PRM是PathFinder-PRM (2505.19706, 2 error heads) 的直接扩展至13 heads + ErrorAtlas对齐，增量有限。ODIN baseline直接来自ICLR 2025同名论文。CausalRM直接来自arXiv 2603.18736。PRM-BiasBench pipeline直接来自arXiv 2603.06621。本proposal的实质novelty是"将已有组件组装在一起做comparison"——这是experimental design层面的贡献，不是method层面的贡献。"Grounded Orthogonality Hypothesis"是一个有趣的hypothesis但本身只是对"semantic labels vs. random labels"这个常见ablation的命名包装。Random-N capacity control是good practice但不是novelty。

2. Significance: 中 — 
PRM hackability是一个genuinely important problem（Tiwari et al.证明的43% stylistic exploitation严重影响RL训练可靠性）。回答"decomposition basis是否matter"这个问题对该领域有一定指导意义。但意义受限于：(a) 限于math reasoning domain; (b) 存在orthogonal替代方案（ensemble, scale, verifiable rewards）可能从根本上绕过该问题; (c) 如果answer是positive（semantic decomposition更好），多数审稿人会说"I would have guessed this"——毕竟semantic grounding优于random是一个符合直觉的结果。如果answer是negative（不matter），则更surprising但also更难publish（null result在top venue很难sell）。

3. Related Work: 中 — 
Proposal覆盖了该领域的主要工作（ODIN, PathFinder-PRM, CausalRM, ThinkPRM, PRM-BiasBench, Socratic-PRMBench）。但存在显著遗漏：(a) 未讨论reward model ensemble作为competing approach; (b) 未讨论Bayesian Non-negative Reward Modeling (2602.10623); (c) 未讨论PURE (min-form credit assignment, 2504.15275)作为另一类anti-hacking机制; (d) 未讨论verifiable rewards混合策略。差异化定位为"first controlled comparison study"是准确的但也暴露了本质是comparison study而非method paper。

【概率估计】: [12% - 22%] 中位 17%
【估计理由】: Novelty维度是主要限制因素。本proposal本质上是一个empirical comparison study，将已有组件（ODIN, PathFinder-PRM, ErrorAtlas, CausalRM, PRM-BiasBench）组装在一起。核心method (ETA-PRM) 是PathFinder-PRM的直接13维扩展，novelty delta有限。研究问题的答案无论是positive还是negative都不太可能产生"surprising"反应：semantic grounding > random是直觉符合的；如果不matter则是null result。此外，存在多个trivial alternatives (ensemble, scale, verifiable rewards) 的威胁，审稿人很可能追问"为什么不直接用ensemble？"。形式上虽然极其完善（tiered design, pre-registered predictions, capacity controls），但top venue（假设投NeurIPS/ICML/ICLR等ML会议）对comparison study的bar很高，通常需要novel insight或counter-intuitive finding来支撑。如果投CoRL（Conference on Robot Learning），还存在严重的venue mismatch——本文完全关于math reasoning PRM，与robot learning无关。

【主要风险】:
1. **"Comparison Study" 身份风险**: 审稿人很可能认为这是"putting together existing methods and comparing them"，而非提出genuinely new insight。Top venue对pure empirical comparison的acceptance bar远高于method paper——需要产生counter-intuitive或high-impact finding才能过线。
2. **Trivial Alternative 威胁**: Reward model ensemble已被证明可有效缓解overoptimization且实现成本远低于multi-head decomposition architecture。如果reviewer追问"why not just ensemble multiple RMs?"，proposal缺乏convincing response来证明decomposition basis comparison的必要性。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [ODIN: Disentangled Reward Mitigates Hacking in RLHF (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf)
- [Error Typing for Smarter Rewards / PathFinder-PRM](https://arxiv.org/abs/2505.19706)
- [ErrorMap and ErrorAtlas](https://arxiv.org/html/2601.15812v1)
- [CausalRM: Causal-Theoretic Reward Modeling](https://www.alphaxiv.org/overview/2603.18736v1)
- [Robust Reward Modeling via Causal Decomposition](https://arxiv.org/abs/2604.13833)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [Socratic-PRMBench](https://arxiv.org/html/2505.23474v1)
- [OrthAlign: Orthogonal Subspace Decomposition](https://arxiv.org/pdf/2509.24610)
- [MR-RML: Multidimensional Rubric-oriented Reward Model](https://arxiv.org/html/2511.16139v1)
- [Reward Model Ensembles Mitigate Overoptimization](https://arxiv.org/pdf/2310.02743)
- [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760)
- [PURE: Min-Form Credit Assignment](https://arxiv.org/pdf/2504.15275)
- [Bayesian Non-negative Reward Modeling](https://arxiv.org/pdf/2602.10623)
- [Awesome Reward Hacking Repository](https://github.com/xhwang22/Awesome-Reward-Hacking)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision" (arXiv 2505.19706, May 2025)**:
   - 提出 PathFinder-PRM，一个层次化、error-aware 的判别式 PRM，先分类每步的 math error 和 consistency error，再聚合细粒度信号估计步骤正确性。
   - **与本 proposal 的关系：极度直接竞争。** 本 proposal 的核心 idea——用 error taxonomy 分解 PRM 监督信号——已被 PathFinder-PRM 实现。PathFinder-PRM 在 PRMBench 上取得 SOTA (67.7)，且只用 3× less data。本 proposal 的 ETA-PRM 本质上是 PathFinder-PRM 的扩展版（从 2 维 error type 扩展到 13 维 ErrorAtlas 分类），而非全新方法。

2. **ODIN: Disentangled Reward Mitigates Hacking in RLHF (arXiv 2402.07319, ICML 2024)**:
   - 提出正交解耦奖励模型，两个 head 分别学习 quality reward 和 length，用正交 loss 去耦合。
   - **与本 proposal 的关系：** 本 proposal 将 ODIN 作为 baseline 之一进行比较，但 ODIN 原始设计仅针对 length bias，扩展到 6-head 正交分解是 proposal 的设定，不是 ODIN 原始工作。

3. **CausalRM: Causal-Theoretic Reward Modeling (arXiv 2603.18736, March 2026)**:
   - 用因果推断框架学习去偏的 reward model，显式建模 annotation error 的生成过程。
   - **与本 proposal 的关系：** 作为 Tier 2 的 baseline 被纳入，但 CausalRM 的 causal decomposition 和本 proposal 的 error-type decomposition 解决的是不同层面的问题。

4. **"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (arXiv 2603.06621, March 2026)**:
   - 系统分析 PRM 的 hackability，发现 PRM 对 surface-level 扰动高度不变但对 logical corruption 检测不一致；RL 训练后的 policy 能达到 >0.9 PRM reward 但 ground-truth accuracy <4%。
   - **与本 proposal 的关系：** 直接建立了 PRM hackability 的实证基础。本 proposal 引用的 Tiwari et al. 关于 "static perturbation tests weakly predict RL-based exploitation" 的发现与此一致。但注意：本 proposal 的 staged evaluation pipeline 本质上是对这篇工作方法论的重组，而非根本创新。

5. **ThinkPRM: Process Reward Models That Think (arXiv 2504.16828, April 2025)**:
   - 用长 CoT 验证替代判别式 PRM，仅需 8K process labels 就超越 PRM800K 训练的判别式模型。
   - **与本 proposal 的关系：** 被列为 Tier 3 baseline。ThinkPRM 代表了一种完全不同的 PRM 范式（generative verification vs. discriminative scoring），可能是本 proposal 多头判别式架构的 trivial alternative。

6. **MO-GRPO (arXiv 2509.22047)**:
   - 多目标 GRPO 缓解 reward hacking，评估 GRPO 在 under-specified reward model 下的表现。
   - **与本 proposal 的关系：** 作为 Tier 2 的 robustness check 被纳入。

7. **ErrorAtlas / ErrorMap (arXiv 2601.15812, Jan 2026)**:
   - 17 类顶层 LLM 错误分类的 model-agnostic taxonomy，跨 35 datasets 和 83 models 生成。
   - **与本 proposal 的关系：** 本 proposal 的 ETA-PRM 13 个 head 直接对齐 ErrorAtlas 的分类体系。ErrorAtlas 本身是描述性工具（事后分类错误），将其转化为 PRM 的监督信号是本 proposal 的核心操作之一。

8. **Socratic-PRMBench (arXiv 2505.23474, May 2025)**:
   - 用 6 种推理模式（Transformation, Decomposition, Regather, Deduction, Verification, Integration）系统评估 PRM。
   - **与本 proposal 的关系：** 被列为 Tier 3 评估工具。

- **调研总结：** PRM hackability 是 2025-2026 年的活跃研究方向。error-aware 多头 PRM（PathFinder-PRM）、正交分解（ODIN）、因果分解（CausalRM）、generative PRM（ThinkPRM）等多种方法已被提出。本 proposal 的定位是"第一个系统比较不同 decomposition basis 对 hackability resistance 影响的受控研究"，但其核心方法（error-type multi-head PRM）与 PathFinder-PRM 高度重叠，且 hackability 评估 pipeline 基本是 "Reward Under Attack" 方法论的结构化重组。


【致命问题：投稿 venue 严重不匹配】:

**CoRL (Conference on Robot Learning) 是一个专注于机器人学习的会议。** 其 Call for Papers 明确要求论文聚焦于 "the intersection of robotics and machine learning"，涵盖的主题包括：robotic perception and control, robot foundation models, imitation learning, RL for physical robots, human-robot interaction, robot safety 等。

本 proposal 是关于 LLM 数学推理的 Process Reward Model hackability resistance 研究，**与机器人学零关联**。即使 idea 质量极高，投稿 CoRL 也会因 scope mismatch 而被 desk reject。

**合适的投稿 venue：** NeurIPS 2026, ICML 2026, ICLR 2027, ACL 2026, EMNLP 2026。


【Trivial Alternative 检验】:

存在多个更简单的替代方案可能达到类似效果：

1. **ThinkPRM (generative verification)：** 不需要任何 multi-head 架构设计、不需要 error taxonomy annotation、仅需 8K labels，就在 OOD 评估上超越了用完整 PRM800K 训练的判别式 PRM。如果目标是 hackability resistance，generative verification 可能天然比 discriminative multi-head 更 robust（因为它验证推理过程而非打分），且成本远低于标注 13 种 error type。

2. **简单的 ensemble：** 与其构建 13-head 架构，直接 ensemble 多个独立训练的 PRM（各自侧重不同 error aspect）可能达到类似效果，且实现更简单。

3. **对抗训练：** 直接用已知 hack patterns 做 adversarial training 可能是更 targeted 的 hackability defense，而不需要走 decomposition 路线。

**增量价值：** 本 proposal 的真正增量价值不在于提出新方法，而在于**系统性比较的实验设计本身**——capacity controls、staged hackability evaluation、Grounded Orthogonality Hypothesis 的 falsifiable predictions。但这更像一篇 benchmarking/empirical study 而非方法创新。


【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **"Error taxonomy grounding 能提供比 data-driven orthogonality 更好的 hackability resistance"——这是核心假设，但缺乏理论支撑。** 为什么基于人类定义的 error taxonomy 的分解会比数据驱动的正交分解更难被 hack？一个可能的反论是：RL exploit 找到的是 reward landscape 中的低谷/漏洞，这些漏洞可能恰好对齐于人类定义的 error boundaries（因为 taxonomy 是有限的、离散的），而数据驱动的分解可能覆盖更连续的空间。

2. **"Coverage breadth 的增加会线性/单调地提高 hackability resistance"——未验证。** 增加 head 数可能引入新的 hack surfaces（每个 head 都是一个可被 exploit 的模块），或导致 head 之间的干扰降低整体鲁棒性。

3. **"ErrorAtlas 的 17 类分类体系适用于 PRM step-level 监督"——跨粒度假设。** ErrorAtlas 是对 LLM 最终输出的事后错误分类，直接用于 step-level PRM 监督需要假设 step-level errors 和 output-level errors 遵循相同的 taxonomy，但中间推理步骤的错误模式可能与最终输出的错误模式有本质不同。

4. **"Grounded Orthogonality Hypothesis 的 falsifiability 取决于 CKA distance 和 selective perturbation sensitivity 的可靠测量"——测量方法的假设。** CKA 作为表征相似性度量在高维空间中的 discriminative power 有限，可能无法区分 semantically grounded vs. data-driven orthogonality 的细微差异。


【3 维度打分】:

1. **Novelty: 弱**
   - 核心方法 ETA-PRM（error-type multi-head PRM）与 PathFinder-PRM (arXiv 2505.19706, May 2025) 高度重叠——后者已实现 error-aware hierarchical PRM，只是用 2 种 error type（math + consistency）而非 13 种。从 2 种扩展到 13 种是 engineering scaling，不是 conceptual novelty。
   - 不同 decomposition basis 的比较本身是一个有价值的研究问题，但核心是 empirical comparison，不是新方法。
   - Staged hackability evaluation pipeline 基本是 "Reward Under Attack" (arXiv 2603.06621) 方法论的重组（perturbation → BoN → RL exploitation），每个 stage 单独都不新。
   - "Grounded Orthogonality Hypothesis" 是一个有趣的假设，但它更像是实验设计中的一个 analysis angle，而非独立的 intellectual contribution。
   - **综合来看：** 个别元素有增量价值（capacity controls, 系统性比较框架），但整体 novelty 不足以支撑顶会。

2. **Significance: 中**
   - PRM hackability 是 RLHF/alignment 领域的重要问题，"Reward Under Attack" 已证明当前 PRM 严重不可靠（reward >0.9 但 accuracy <4%）。
   - 理解不同 decomposition basis 的效果确实对 PRM 设计有指导意义。
   - **但受限因素：**（a）仅限数学推理域，proposal 自己也承认是 "domain-specific validation"；（b）即使发现 error-taxonomic 最优，其可推广性存疑——不同 domain 的 error taxonomy 完全不同，无法直接迁移；（c）如果审稿人的反应是 "I would have guessed that semantic grounding helps more than random orthogonality"，则 significance 大打折扣。
   - 目标 venue CoRL 的 significance 更是几乎为零，因为与机器人学无关。

3. **Related Work: 中**
   - 对 ODIN, CausalRM, ThinkPRM, ErrorAtlas, Socratic-PRMBench 等有覆盖，差异化定位（"第一个系统比较 decomposition basis"）是清晰的。
   - **但存在问题：**（a）PathFinder-PRM (arXiv 2505.19706) 是最直接的竞争者，proposal 是否充分 acknowledge 了与它的重叠？PathFinder-PRM 作为 "PathFinder trajectory-level" baseline 出现在 proposal 中，但 proposal 似乎将其定位为 trajectory-level 方法而非 error-type-aware 方法，这可能 mischaracterize 了 PathFinder-PRM 的贡献（它的核心恰恰是 error-type-aware）。（b）PRM-BiasBench 和 Tiwari et al. 的引用未在公开文献中找到确切匹配——需要验证这些引用是否准确。


【概率估计】: [1% - 5%] 中位 2%

【估计理由】:
- **venue mismatch 是 decisive factor：** CoRL 是 robotics 会议，本 proposal 是纯 NLP/RLHF 方向，几乎确定会被 desk reject。仅此一项就将概率压到 <5%。
- **即使投到合适 venue (NeurIPS/ICML/ICLR)，重新估计：**
  - Novelty 弱：核心方法与 PathFinder-PRM 重叠，整体定位为 empirical comparison study
  - Significance 中：问题重要但预期发现不够 surprising
  - 在合适 venue 的估计概率约 15-25%
- **上界限制因素：** Novelty 维度。这本质上是一个精心设计的 ablation/comparison study，而非提出新 insight 或新方法。顶会通常需要至少一个维度达到"强"。

【主要风险】:
1. **致命 venue 不匹配：** CoRL 是 robot learning 会议，本 proposal 关于 LLM 数学推理的 PRM hackability，与 robotics 完全无关，极大概率 desk reject。
2. **Novelty 不足：** 核心方法（error-type multi-head PRM）已被 PathFinder-PRM 实现；整体贡献定位为 empirical comparison + ablation study，缺乏足以支撑顶会的 conceptual innovation。审稿人最可能的批评是 "an extensive ablation study of known ideas, not a novel contribution."
```

---

**关键提醒：** 本 proposal 投稿 CoRL 2026 存在**致命的 venue 不匹配**问题。CoRL (Conference on Robot Learning) 聚焦于机器人学习，要求论文涉及 robotics + ML 的交叉领域。本 proposal 是纯 NLP/RLHF 方向（LLM 数学推理的 PRM hackability），与 robotics 零关联。建议改投 NeurIPS 2026、ICML 2026、ICLR 2027、ACL 2026 或 EMNLP 2026 等 NLP/ML 主流会议。

Sources:
- [Error Typing for Smarter Rewards (PathFinder-PRM)](https://arxiv.org/abs/2505.19706)
- [ODIN: Disentangled Reward Mitigates Hacking in RLHF](https://arxiv.org/pdf/2402.07319)
- [CausalRM: Causal-Theoretic Reward Modeling](https://arxiv.org/pdf/2603.18736)
- [Reward Under Attack: Analyzing PRM Hackability](https://arxiv.org/abs/2603.06621)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [ErrorAtlas / ErrorMap](https://arxiv.org/abs/2601.15812)
- [Socratic-PRMBench](https://arxiv.org/abs/2505.23474)
- [MO-GRPO](https://arxiv.org/pdf/2509.22047)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal Reward Decomposition for PRM Hackability Resistance

## Description
We present the first systematic empirical study of how decomposition basis and coverage breadth jointly affect PRM hackability resistance, organized as a tiered experimental program with staged evaluation and capacity controls. Our two central questions: (1) Does the CHOICE of decomposition basis matter — specifically, does grounding multi-dimensional supervision in a systematic error taxonomy outperform orthogonality-enforced, quality-dimension, and causal alternatives? (2) How does coverage breadth (number of supervised error dimensions) affect hackability, and does hacking shift to uncovered dimensions as theory predicts? We introduce ETA-PRM (Error-Type-Aware PRM), a multi-head architecture with up to 13 ErrorAtlas-aligned error-type heads plus a residual head. The guaranteed Tier 1 deliverable compares four decomposition approaches (ETA error-taxonomic, ODIN data-driven orthogonal, single-head, PathFinder trajectory-level) across a 4-level coverage ablation (2→6→13→13+residual heads), with Random-N capacity controls (N=2,6,13) at each coverage level to disentangle coverage breadth from model capacity. The critical three-way comparison — ETA-PRM-6 (error-type labels) vs. ODIN-6-orthogonal (random labels + orthogonality loss) vs. Random-6 (random labels, no orthogonality) — isolates whether semantic grounding, orthogonality enforcement, or raw capacity drives hackability resistance. Hackability is measured through a staged pipeline motivated by Tiwari et al.'s finding that static perturbation tests weakly predict RL-based exploitation: Stage 1 applies PRM-BiasBench perturbations for surface profiling and GOH sensitivity analysis, Stage 2 traces Best-of-N overoptimization curves as an intermediate proxy, and Stage 3 runs full GRPO exploitation on core variants with 3 seeds and paired bootstrap confidence intervals. The Grounded Orthogonality Hypothesis is tested via pre-registered, falsifiable predictions: comparable overall debiased CKA distance but divergent selective perturbation sensitivity (ETA-PRM heads sensitive to matching perturbation types vs. ODIN heads showing uniform sensitivity). Tier 2 extends to CausalRM and DRM baselines, cross-scale robustness verification (Qwen2.5-Math-1.5B-Instruct backbone), and MO-GRPO robustness checks to rule out RL-algorithm-specific exploitation artifacts; Tier 3 adds ThinkPRM comparison, Socratic-PRMBench reasoning-pattern evaluation, and full mechanistic analysis. All evaluation is on mathematical reasoning, explicitly acknowledged as domain-specific validation with methodology designed for cross-domain extension. This is the first controlled study varying both decomposition basis and coverage breadth with capacity controls, staged hackability evaluation, pre-registered mechanistic predictions, and statistical rigor.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4b354c48-3246-4d2e-ae4c-605ee6b7fee7",
  "type": "user",
  "uuid": "024270df-7890-4eb3-bbb4-de0d25cfbd2d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:19:15.008Z_

```json
{
  "parentUuid": "024270df-7890-4eb3-bbb4-de0d25cfbd2d",
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
  "uuid": "c1a4cd4a-bcae-4f38-9816-aafb1a294702",
  "timestamp": "2026-05-20T03:19:15.008Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:19:15.008Z_

```json
{
  "parentUuid": "c1a4cd4a-bcae-4f38-9816-aafb1a294702",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c66662d2-c6e1-4f3c-bc53-77c53ffc8898",
  "timestamp": "2026-05-20T03:19:15.008Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make my assessment. Let m…",
  "leafUuid": "c66662d2-c6e1-4f3c-bc53-77c53ffc8898",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM decomposition approaches for hackability resistance",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:19:46.406Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully and produce a Meta Judge output.

**Reviewer 1:** 
- Probability: [1% - 5%] median 3%
- Key issues: Fatal venue mismatch (CoRL vs NLP work), weak novelty (PathFinder-PRM overlap), comparison study identity
- Novelty: 弱, Significance: 致命(CoRL)/中(NLP), Related Work: 中

**Reviewer 2:**
- Probability: [12% - 22%] median 17%


- Key issues: Weak novelty as a comparison study with trivial alternatives like ensemble methods, scaling, and verifiable rewards, though acknowledges some merit in the research question itself
- Novelty: 弱, Significance: 中, Related Work: 中
- Note: R2 flags venue mismatch but appears to estimate probability assuming the paper were at the right venue

**Reviewer 3:**
- Probability: [1% - 5%] median 2%
- Key issues: Fatal venue mismatch, weak novelty (PathFinder-PRM overlap), empirical comparison study
- Novelty: 弱, Significance: 中, Related Work: 中

Looking back at R2's reasoning more carefully, they mention venue mismatch as a concern but their 17% median estimate seems to account for a more suitable venue scenario. So R2 is being more generous than R3 despite the same core concerns. Computing the aggregate: R1 at 3%, R2 at 17%, R3 at 2% gives a median of 3% and mean around 7.3%.

But I need to reconsider what each reviewer is actually estimating—R1 and R3 are clearly assessing the paper as submitted to CoRL, while R2's estimate seems to blend venue considerations. Looking at their "correct venue" estimates separately: R1 would give 15-25%, R2 is already at 12-22% median 17%, and R3 would give 15-25% for NeurIPS/ICML/ICLR. This distinction matters for understanding the true disagreement.

For CoRL specifically, the estimates converge: R1 at 1-5% median 3%, R2 lower than 17% but unspecified, and R3 at 1-5% median 2%. Across all three reviewers, there's striking agreement on the core issues—the fatal venue mismatch since CoRL focuses on robotics while this is NLP/RLHF work, weak novelty due to PathFinder-PRM overlap and the comparison study nature, medium significance only if submitted to the right venue, and medium related work quality. They all identify that trivial alternatives exist and recognize this is fundamentally an empirical comparison study rather than a novel method paper, with PathFinder-PRM being a direct competitor with substantial overlap.

R2 stands out as notably more generous with the 17% estimate, apparently evaluating as if the paper were at an appropriate venue, while R1 and R3 both flag the Tiwari et al. citation error. Looking at the three medians—3%, 17%, 2%—the standard deviation around 6.85% puts this at the borderline between medium and high disagreement, but that divergence stems from R2 essentially evaluating under different venue assumptions. When I normalize everything to the actual CoRL submission context, the consensus tightens dramatically to 2-3%, making it clear the venue mismatch is the decisive factor here.

Given that this is explicitly a CoRL 2026 submission, I need to weight that venue incompatibility heavily and keep the final estimate very low. Let me also pull in what the reviews say about the implementation quality before I format the output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c66662d2-c6e1-4f3c-bc53-77c53ffc8898",
  "isSidechain": false,
  "requestId": "req_011CbD6ggxHGsBQHbWrMxMiZ",
  "type": "assistant",
  "uuid": "392a4723-b4c2-41bc-87a7-0bd2508418d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPrReQiCBgVZx1vyxr1mHK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13932,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4153,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 13932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13932
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

_source line 9 · 2026-05-20T03:20:53.802Z_

【阶段】: Meta Judge
【三次中位】: [3%, 17%, 2%]  std=6.9%
【共识维度】:
- **Venue Mismatch（致命）**: 3/3 审稿人一致判定——CoRL 是机器人学习会议，本 proposal 是纯 NLP/RLHF 方向（LLM 数学推理 PRM hackability），与 robotics 零关联，极大概率 desk rejection。这是最高信号共识。
- **Novelty（弱）**: 3/3 一致判定。核心方法 ETA-PRM 与 PathFinder-PRM (arXiv:2505.19706) 高度重叠（后者已实现 error-aware hierarchical PRM）；整体定位为 empirical comparison study 而非方法创新；staged hackability pipeline 是 "Reward Under Attack" (arXiv:2603.06621) 方法论的结构化重组。
- **Significance（中，仅对 NLP venue）**: 3/3 一致认为 PRM hackability 是重要问题，但 (a) 仅限数学推理域，(b) 预期发现不够 surprising（semantic grounding > random 符合直觉），(c) 对 CoRL significance ≈ 0。
- **Related Work（中）**: 3/3 一致评为"中"——覆盖了主要工作但与 PathFinder-PRM 的差异化不够清晰。
- **Trivial Alternative 威胁**: 3/3 均指出 ThinkPRM（generative verification）和其他替代方案（ensemble、scale-up、verifiable rewards mix）可能从根本上绕过 decomposition basis 问题。
- **"Comparison Study" 身份**: 3/3 一致认为本 proposal 本质是将已有组件（ODIN、PathFinder-PRM、ErrorAtlas、CausalRM、PRM-BiasBench）组装后做受控比较，不是方法论创新。

【异常维度】:
- **R2 概率显著偏高 (17% vs 2-3%)**: R2 的评估似乎部分基于"假设投到正确 venue"的情景，而非严格评估 CoRL 投稿。R1 和 R3 均明确给出 CoRL 概率 ≤5%。R2 在理由中也承认"如果投 CoRL 还存在严重的 venue mismatch"，但未在数字中充分反映。判断：R2 的 17% 是 venue-adjusted 估计的混合值，作为 CoRL 投稿估计应降权。
- **R2 额外指出的遗漏 baseline（ensemble, Bayesian Non-negative RM, PURE, verifiable rewards mix）**: 仅 R2 系统性列出。R1 和 R3 提到了 ensemble/ThinkPRM 但未展开。判断：这些遗漏是真实的补充信息，但在 venue mismatch 致命问题面前属于次要维度。

【最终概率】: [1% - 5%] 中位 2%
【一致性】: 中（std=6.9%，但异常值有明确归因——R2 混合了 venue-adjusted 估计；若归一化到 CoRL 投稿场景，实际一致性为高）
【综合理由】:

1. **Venue mismatch 是 decisive factor，三方完全共识。** CoRL 的 scope 是 "intersection of robotics and machine learning"，本 proposal 涉及的 PRM hackability、error taxonomy decomposition、GRPO exploitation 全部属于 NLP/LLM alignment 领域，无任何 robotics 相关内容。这不是可以通过 reframing 解决的边界问题——proposal 中没有一个字涉及机器人、物理控制、感知或操作。desk rejection 概率极高。

2. **R2 的 17% 为异常值，有明确归因。** R2 的估计理由中混合了"假设投到 NeurIPS/ICML/ICLR"的情景分析。将其归一化到 CoRL 场景后，三方实际共识紧密收敛于 2-3%。按规则"分歧时偏严"，最终中位取 2%。

3. **即使假设投到正确 venue（NeurIPS/ICML/ICLR），三方对 novelty 维度的一致判定（弱）也将概率上限压制在 15-25%。** 核心方法与 PathFinder-PRM 重叠、comparison study 身份、trivial alternative 威胁三重叠加，使得即便换 venue 也不乐观。

4. **概率不可能高于三方最宽松估计（R2 的 22%上界）。** 在 CoRL 场景下，上界进一步被压到 5%。

【建议】: KILL
- **对 CoRL 2026 投稿：不推荐，建议止损。** Venue mismatch 是不可修复的致命缺陷。
- **对 NLP/ML venue（NeurIPS 2026 / ICML 2026 / ICLR 2027 / EMNLP 2026）：边缘，但需要重大修改。** 即使换 venue，仍需解决：(a) 与 PathFinder-PRM 的差异化，(b) comparison study 身份的 novelty 不足，(c) trivial alternative 的 defense。三方一致估计换 venue 后概率约 15-25%，属于"边缘"区间。

【实施评估】:
- **计算资源**: 需要多轮 GRPO 训练（Stage 3），每个 variant × 3 seeds；backbone 为 Qwen2.5-Math-7B-Instruct 及 1.5B 变体。估计需要 8×A100 集群，总 GPU 时间约 2000-4000 GPU-hours（Stage 3 的 GRPO exploitation 是主要开销）。
- **数据需求**: PRM800K（公开）、ErrorAtlas taxonomy（公开，arXiv:2601.15812）、PRM-BiasBench perturbation 工具（需确认是否已公开发布）。step-level error type annotation 需要基于 ErrorAtlas 对 PRM800K 重新标注——这是主要数据瓶颈。
- **人工介入**: ErrorAtlas 的 13 维 error type 标注可能需要 LLM-assisted + 人工审核的混合流程。Proposal 未详细说明标注策略，这是一个实施风险点。
- **训练需求**: 需要训练多个 PRM 变体（ETA-PRM-2/6/13/13+R, ODIN-2/6/13, Random-2/6/13, CausalRM, 单头 baseline），每个 variant 至少 3 seeds。总训练 runs 约 30-50 个。
- **新 Benchmark**: 不需要构建全新 benchmark，但需要整合 PRM-BiasBench + BoN pipeline + GRPO exploitation 的 staged evaluation 框架。
- **预估周期**: 数据准备 + 标注：4-6 周；Tier 1 训练 + 评估：6-8 周；Tier 2 扩展：4-6 周；Tier 3（如果推进）：4-6 周。总计约 4-6 个月。

---

基于以上 Meta Judge 判定，本 proposal 投稿 CoRL 2026 的最终建议为 **KILL**。以下是最终拒绝输出：

【拒绝阶段】: Triage（Meta Judge 综合三方独立评审后）
【击穿维度 / 致命缺陷】:
1. **Venue Mismatch（致命，不可修复）**: CoRL 是机器人学习会议（robotic perception, control, manipulation, locomotion, sim-to-real 等），本 proposal 是纯 NLP/LLM alignment 方向（PRM hackability in mathematical reasoning），二者零交集。三位审稿人一致判定会被 desk reject。这不是 framing 问题——proposal 中没有任何 robotics 相关内容可供包装。
2. **Novelty 弱（三方共识）**: 核心方法 ETA-PRM 与 PathFinder-PRM (arXiv:2505.19706, May 2025) 高度重叠；整体定位为已有方法的 empirical comparison study 而非方法创新；hackability evaluation pipeline 是 "Reward Under Attack" (arXiv:2603.06621) 方法论的结构化重组。
3. **Trivial Alternative 威胁未防御**: ThinkPRM (generative verification, 1% 数据超越 discriminative PRM)、reward model ensemble、verifiable rewards mix 等更简单方案可能从根本上绕过 decomposition basis 问题。

【已尝试优化方向】: 无（Triage 阶段即 KILL，未进入迭代）
【可否抢救】:
- **换 venue 可行**: 建议改投 NeurIPS 2026 / ICML 2026 / ICLR 2027 / EMNLP 2026。三方一致估计换到 NLP/ML venue 后概率约 15-25%（边缘区间）。
- **换 venue 后仍需重大修改**: (a) 必须正面处理与 PathFinder-PRM 的差异化——明确 ETA-PRM 相对于 PathFinder-PRM 的增量在哪里（不能只是"2 heads → 13 heads"的 scaling）；(b) 必须 defense trivial alternatives（为什么不直接 ensemble？为什么不用 ThinkPRM？decomposition basis comparison 的独立价值是什么？）；(c) 需要在 framing 上更强调 mechanistic insight 的贡献（如果 Grounded Orthogonality Hypothesis 的验证能产生 counter-intuitive finding，significance 会大幅提升）；(d) 补充 R2 指出的遗漏 baseline（reward model ensemble, verifiable rewards mix）。
- **如果坚持投 CoRL**: 需要将整个研究问题重新设计为 robotics-relevant——例如研究 reward model hackability 在 robot learning / manipulation policy 训练中的影响。但这本质上是一个全新 proposal，与当前 proposal 关系不大。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "392a4723-b4c2-41bc-87a7-0bd2508418d1",
  "isSidechain": false,
  "requestId": "req_011CbD6ggxHGsBQHbWrMxMiZ",
  "type": "assistant",
  "uuid": "1f672e90-da29-48e2-8a23-bddc1324afb3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPrReQiCBgVZx1vyxr1mHK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13932,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4153,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 13932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13932
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make my assessment. Let m…",
  "leafUuid": "1f672e90-da29-48e2-8a23-bddc1324afb3",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM decomposition approaches for hackability resistance",
  "sessionId": "112d4811-a19c-430d-b92b-7970ecbe98ef"
}
```

---
