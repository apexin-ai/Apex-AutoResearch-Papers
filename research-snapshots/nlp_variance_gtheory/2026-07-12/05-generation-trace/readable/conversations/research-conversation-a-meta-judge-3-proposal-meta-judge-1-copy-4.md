# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/1228067e-47cd-4ff5-b219-82d93c755583.jsonl`
- **Structured JSON:** [`5741692f33247760b8a7.json`](../../sessions/57/5741692f33247760b8a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T09:10:03.038Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T09:10:03.038Z",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research material to conduct a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **STAT: Skill-Targeted Adaptive Training (ICLR 2026, arXiv 2510.10023)**:\n   最直接的竞争者之一。STAT 使用强 LLM 教师（如 GPT-4）做元认知技能诊断，创建 Missing-Skill-Profile，然后针对性地重采样或合成训练数据。在 Llama/Qwen 上 MATH 提升达 7.5%，OOD 平均提升 4.6%。本 proposal 的核心差异化在于用 formal tools 替代 LLM 教师做诊断——消除教师偏差和幻觉归因。\n\n2. **NSRSA: Symbolic Recursive Self-Alignment (arXiv 2603.21558, March 2026)**:\n   最近的竞争者。NSRSA 已经在迭代自训练中使用 SymPy 做算术运算级别的符号验证，过滤掉约 34% 的\"lucky guess\"正确答案，并结合 DPO。但 NSRSA 仅覆盖算术操作验证，**不做错误分类或针对性合成**，DPO 是 solution-level 而非 step-localized。在 GSM8K + Qwen3-4B 上实验，规模较小。本 proposal 的增量在于：(a) 错误类型分类，(b) 针对性合成，(c) step-localized DPO。\n\n3. **FoVer (ACL 2026 Findings, arXiv 2505.15960)**:\n   使用 Z3 和 Isabelle 对 formal reasoning 任务的 LLM 响应做 step-level error label 标注，合成 PRM 训练数据（FoVer-40K）。在 12 个 benchmark 上训练的 PRM 超越 baseline。FoVer 的目标是训练通用 PRM，不做闭环自改进或错误分类。本 proposal 的差异在于直接使用 formal verification 做诊断+针对性合成，而非间接训练 PRM。\n\n4. **SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025, arXiv 2506.08989)**:\n   通过 pass-rate 分析识别 RL 训练中模型持续失败的问题，提取核心概念后合成新问题。7B 模型平均提升 10.0%，32B 提升 7.7%。SwS 的弱点诊断基于 pass-rate（统计层面），不做 step-level 错误归因。本 proposal 的优势在于 formal step-level diagnosis 提供更精细的技能分解。\n\n5. **Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, Feb 2026)**:\n   使用 SymPy 的符号表示空间做闭环 RLVR 问题生成，自适应调整难度。但是全局难度调整，不做错误类型诊断。是最接近的\"使用符号工具做闭环自改进\"的工作，但粒度不同（全局难度 vs. 错误类型针对）。\n\n6. **Solver-Verifier Gap Theory (ICLR 2026, arXiv 2507.00075)**:\n   理论建模 LLM 自改进的训练动力学，证明验证器可靠性决定自改进的天花板，能力提升遵循指数律趋近极限。为本 proposal 的\"formal verification 作为 collapse-proof verifier\"提供了理论基础。\n\n7. **Imperfect Verifier (arXiv 2604.07666, April 2026)**:\n   实证表明噪声率 ≤15% 时，RLVR 验证准确率在 clean baseline 2 个百分点以内。precision 比 recall 更重要。为本 proposal 的\"precision-coverage tradeoff hypothesis\"提供了直接实证支撑。\n\n8. **LLMs Cannot Spot Math Errors (EMNLP 2025, arXiv 2509.01395)**:\n   证明 SOTA LLMs 在有参考解答的情况下仍难以定位学生解答中的第一个错误步骤。为本 proposal \"LLM 教师诊断不可靠\"的前提提供了实证支撑。\n\n- **调研总结**: 数学推理自改进是 2025-2026 最活跃的研究方向之一。当前格局中，formal verification 已被用于 PRM 训练数据合成（FoVer）和迭代自训练过滤（NSRSA），weakness-driven synthesis 已有 pass-rate 方法（SwS）和 LLM 教师方法（STAT），step-level DPO 已有 LLM/人工标注版本（Step-DPO, Full-Step-DPO）。本 proposal 处于这些工作的**交汇点**——将 formal verification 从\"验证/过滤工具\"升级为\"诊断+分类+针对性合成\"的完整闭环，这一具体组合尚无先例，但各组件均有成熟前驱工作。\n\n【Trivial Alternative 检验】:\n\n存在两个值得认真考虑的 trivial alternatives：\n\n**(1) NSRSA + 更广的符号覆盖**：NSRSA 已经用 SymPy 做算术验证 + 迭代 DPO。如果简单扩展 NSRSA 的符号验证范围（从算术到代数），是否就能获得大部分收益？本 proposal 的增量价值在于：(a) 错误分类 taxonomy（5 种类型），(b) 基于分类的针对性合成，(c) step-localized DPO pair 构造。其中 (a)+(b) 是核心增量——问题是这个增量有多大。如果简单地用 formal verification 做更严格的过滤（不分类）就能获得主要收益，那分类+针对性合成的边际价值可能有限。Proposal 承诺通过 ablation (targeting vs. uniform) 量化这一增量，设计合理。\n\n**(2) Subcategory-level outcome targeting**：Proposal 自身承认这是最简单的替代方案，并纳入 baseline。核心问题是：MATH 的 7 个子类别粒度是否足够？Proposal 声称 within-subcategory skill decomposition 有价值，但这一主张尚未验证。如果 subcategory-level targeting 就能获得 80-90% 的收益，formal error profiling 的工程复杂度就不划算了。\n\n**增量价值判断**：增量价值真实存在但可能有限。最有价值的独特贡献是 (1) step-localized formal DPO pairs 和 (2) error profile dynamics 分析——这两者确实无法通过 trivial alternatives 实现。\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的前提假设：\n\n**(1) \"LLM-to-formal translation 成功率 60-70% 是足够的\"**：这是最关键的假设。Proposal 声称 formal verification 覆盖代数/算术领域的 60-70%，但这个数字本身是估计。更关键的是：formalization 失败的 30-40% 是否会引入系统性偏差？如果 formalization 更容易对简单问题成功，error profile 就会偏向高难度错误的低估。Proposal 提到了 selection bias analysis（pilot study），说明作者意识到了这个问题，但目前没有证据表明偏差可控。\n\n**(2) \"5 类 formal error taxonomy 足以捕获有意义的技能分解\"**：Taxonomy 包括 algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference。这个分类是否与模型实际的能力瓶颈对齐？STAT 的 LLM-driven taxonomy 是 data-driven 的，可能更贴合实际；formal taxonomy 受制于 Z3/SymPy 能区分的错误类型，可能遗漏重要维度（如 problem comprehension errors, strategy selection errors）。\n\n**(3) \"Targeted synthesis 优于 uniform synthesis 的效果来自错误分类的精细度\"**：这个因果关系未经验证。也许 targeted synthesis 的优势主要来自\"更多练习弱项\"这个粗粒度策略，而非\"精确知道是 equation solving 还是 algebraic manipulation\"。如果 2-type taxonomy (arithmetic/non-arithmetic) 就能获得大部分收益，5-type taxonomy 的价值就存疑。Proposal 设计了 taxonomy granularity ablation，但结果未知。\n\n**(4) \"Formal verification 在迭代中保持独立校准\"**：Proposal 声称 formal diagnosis 不会像 LLM 教师那样在迭代中积累偏差。这在技术上成立（Z3/SymPy 是确定性的），但忽略了一个间接路径：如果模型学会了\"在 formally verifiable 的步骤上做得更好\"但在 non-verifiable 的步骤上退化（Goodhart's Law），迭代稳定性可能是表面的。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   各核心组件均有明确前驱：formal verification for math → FoVer (ACL 2026), MATH-VF (arXiv 2025); symbolic verification in iterative self-training → NSRSA (arXiv 2026); weakness-targeted synthesis → STAT (ICLR 2026), SwS (NeurIPS 2025); step-level DPO → Step-DPO (NeurIPS 2024), Full-Step-DPO (ACL 2025 Findings); symbolic problem generation in closed-loop → Adaptive Problem Generation (arXiv 2602.19187)。\n\n   真正的 novelty delta 在于：(a) formal verification 从\"过滤/验证工具\"升级为\"诊断+分类+针对性合成引擎\"的完整闭环——这个组合确实无先例；(b) step-localized formal DPO pairs（相对于 NSRSA 的 solution-level 和 Step-DPO 的 LLM-annotated）；(c) ground-truth error profile dynamics 分析（无先例）。\n\n   但剔除 surface differences 后，核心洞察（\"用 formal tools 替代 LLM 做更精确的错误诊断\"）是一个 **自然的方向延伸**，而非 conceptual surprise。NSRSA 已经走了一半路（SymPy 验证 + 迭代 DPO），本 proposal 走完了另一半（分类 + 针对性合成 + step-localized）。\n\n2. **Significance: 中** — \n   研究问题（self-improvement stability 和 targeted synthesis for math reasoning）毫无疑问是重要且 trending 的方向。但本 proposal 的影响力受限于：\n   - **覆盖范围有限**：仅对代数/算术类问题有效（~60-70% formalization 成功率，且仅在 amenable categories 上），几何、组合等必须 fallback 到 outcome verification。这不是一个通用方案。\n   - **结果可预测性偏高**：如果 formal diagnosis + targeted synthesis 优于 LLM diagnosis + targeted synthesis，审稿人可能反应为 \"makes sense — formal tools are more precise by definition, so of course they work better where they can be applied\"。真正的 insight 在于 precision-coverage tradeoff 的量化分析，但这更像一个 empirical finding 而非 paradigm shift。\n   - **可推广性问题**：方法的核心依赖 Z3/SymPy 的可形式化特性，难以推广到其他推理领域（代码、逻辑、常识推理）。\n\n   积极面：error profile dynamics 的分析贡献对理解 self-improvement 机制有独立价值，precision-coverage tradeoff 的量化对 imperfect verifier 研究方向有参考意义。\n\n3. **Related Work: 强** — \n   这是 proposal 最突出的优势。覆盖了几乎所有直接竞争工作（STAT, NSRSA, FoVer, SwS, Step-DPO, Full-Step-DPO, MATH-VF, Safe, Adaptive Problem Generation, Reasoning Core, Bidirectional Curriculum, SPARQ, CoTEvol, MathMixup, SPICE, SvS, WarriorMath, Self-Error-Instruct），引用的论文经验证均真实存在且描述准确。差异化定位清晰且诚实——特别是 \"Why Not Simpler Alternatives\" 部分主动讨论了 trivial alternatives 并设计了针对性 baseline。这种水平的 related work 覆盖在 AAAI submissions 中属于上游。\n\n【概率估计】: [25% - 35%] 中位 29%\n\n【估计理由】: \n三个维度中，Related Work 是明确的强项，不会成为拒稿理由。Novelty 和 Significance 均为\"中\"——novelty 是组合式的（各组件有前驱，组合本身新颖但方向自然/可预测），significance 受限于 formal verification 的覆盖范围和结果可预测性。\n\n**上界限制因素是 Novelty**。核心问题是：审稿人看到\"用 formal tools 替代 LLM 做错误诊断\"时，反应很可能是 \"natural extension, well-executed but not surprising\" 而非 \"I wouldn't have thought of this\"。NSRSA (arXiv 2026, March) 已经在同一方向走了一大步，将本 proposal 的 novelty space 进一步压缩。\n\n**中位 29% 的定位依据**：idea 有实质的 novelty delta（error profile dynamics、step-localized formal DPO 是真正的新贡献），方向正确且重要，但核心发现的 surprise factor 偏低。在 25-35% 区间的下半段，因为 (1) 最接近的竞争者 NSRSA 非常近且发表在 proposal 之前，(2) 如果核心实验结果是 positive，审稿人大概率反应为 \"I would have guessed this\"。\n\n【主要风险】:\n1. **Novelty 被判为 incremental over NSRSA + STAT**：NSRSA 已做 SymPy 验证 + 迭代 DPO，STAT 已做 skill profiling + targeted synthesis。审稿人可能认为本 proposal 只是将两者的最佳部分拼接（formal diagnosis from NSRSA 的方向 + targeting from STAT 的策略），组合本身不构成足够的 conceptual contribution。\n2. **核心结果可预测性导致 significance 质疑**：\"Formal verification is more precise than LLM diagnosis → better targeted synthesis → better self-improvement\" 这条因果链过于直觉化。如果实验验证了这一预期，审稿人可能认为 contribution 主要在工程层面而非科学发现层面。唯一能打破这一预期的结果是 precision-coverage tradeoff 显示出非直觉的 sweet spot，但这是 ablation 级别的发现，难以支撑整篇论文的 significance。\n```\n\nSources:\n- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://openreview.net/forum?id=m3jG3GaNIj)\n- [NSRSA: Symbolic Recursive Self-Alignment (arXiv 2603.21558)](https://arxiv.org/abs/2603.21558)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL 2026 Findings)](https://arxiv.org/abs/2505.15960)\n- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)\n- [Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187)](https://arxiv.org/abs/2602.19187)\n- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)\n- [An Imperfect Verifier is Good Enough (arXiv 2604.07666)](https://arxiv.org/abs/2604.07666)\n- [LLMs Cannot Spot Math Errors (EMNLP 2025)](https://arxiv.org/abs/2509.01395)\n- [Step-DPO (NeurIPS 2024)](https://openreview.net/forum?id=H5FUVj0vMd)\n- [Full-Step-DPO (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.1249/)\n- [MATH-VF: Step-Wise Formal Verification (arXiv 2505.20869)](https://arxiv.org/html/2505.20869v1)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **FoVer (ACL 2026 Findings, arXiv 2505.15960)**: 使用 Z3 和 Isabelle 等形式验证工具合成 PRM 训练数据，在 12 个推理 benchmark 上表现优于人工标注或强模型标注的 PRM。证明了形式验证在 step-level 数学验证上的可行性。与本 proposal 的关系：FoVer 用形式验证训练 PRM（间接使用），proposal 则直接在 self-improvement loop 中使用形式验证做 error diagnosis 和 targeted synthesis（直接使用）。是最近的竞争性工作，但技术路径不同。\n\n2. **STAT (ICLR 2026, arXiv 2510.10023)**: 使用 LLM teacher（GPT-4o）进行 skill profiling，创建 Missing-Skill-Profile 后自适应重采样或合成训练数据。在 MATH 上提升 7.5%，OOD benchmark 平均提升 4.6%。与本 proposal 的关系：STAT 是本 proposal 最直接的竞争对手——同样做 skill-targeted synthesis，但依赖 LLM teacher。Proposal 的核心 claim 就是用 formal tools 替代 STAT 中的 LLM teacher。\n\n3. **NSRSA (arXiv 2603.21558, 2026)**: 使用 SymPy 验证每个算术操作，在 GSM8K 上用 Qwen3-4B 进行 5 轮迭代自训练，包含 solution-level DPO。拒绝了约 34% 通过 outcome verification 的\"lucky guess\"。与本 proposal 的关系：**这是最接近的工作**——同样使用 SymPy 在迭代 self-training 中做形式验证。但 NSRSA 仅覆盖算术操作、无 error categorization、做 solution-level DPO 而非 step-localized DPO。Proposal 是 NSRSA 的自然且显著扩展。\n\n4. **SwS (NeurIPS 2025, arXiv 2506.08989)**: 通过 pass-rate 分析识别弱点，合成针对性问题。7B/32B 模型在 8 个 benchmark 上分别提升 10%/7.7%。与本 proposal 的关系：SwS 做 weakness-driven synthesis 但不用 formal diagnosis——是一个重要的 ablation 对照点。SwS 的强结果构成对 proposal 的\"trivial alternative\"威胁：pass-rate 分析可能已足够好。\n\n5. **Adaptive Problem Generation (arXiv 2602.19187, Feb 2026)**: 使用 SymPy 在 closed-loop RLVR 中生成自适应难度问题，但全局调整难度而不做 error-type diagnosis。与本 proposal 的关系：同样使用 SymPy + closed-loop，但无 error categorization——是另一个重要对照。\n\n6. **Imperfect Verifier (arXiv 2604.07666, Apr 2026)**: 证明 noise rate ≤15% 时 RLVR 仍可有效训练，precision 比 recall 更重要。在 Qwen3、GLM4、Llama 3.1 上验证。与本 proposal 的关系：直接支持 proposal 的 precision-coverage tradeoff 假说——高精度低覆盖可能优于低精度高覆盖。\n\n7. **Solver-Verifier Gap Theory (ICLR 2026, arXiv 2507.00075)**: 理论建模 self-improvement 训练动态，证明 verifier 可靠性决定 self-improvement 上限。与本 proposal 的关系：为 proposal 的 formal verification 动机提供理论基础。\n\n8. **LLMs Cannot Spot Math Errors (EMNLP 2025, arXiv 2509.01395)**: 实证表明即使给出参考解答，SOTA LLM 仍难以定位数学推理中的第一个错误步骤。与本 proposal 的关系：直接支持 proposal \"LLM error diagnosis 不可靠\"的前提假设。\n\n9. **Self-Error-Instruct (ACL 2025, arXiv 2505.22591)**: 使用 GPT-4o 分析错误 keyphrases 并聚类为 error types，然后合成训练数据。与本 proposal 的关系：同样做 error-type-driven synthesis，但依赖 LLM teacher。\n\n10. **Step-DPO (NeurIPS 2024) / Full-Step-DPO (ACL 2025 Findings)**: Step-DPO 以单个推理步骤为偏好对比单元，Full-Step-DPO 用自监督 PRM 打分避免人工/GPT-4 标注。与本 proposal 的关系：Proposal 的 step-localized DPO 使用 formal verification 而非 LLM/PRM 来保证 step-level 正确性。\n\n- **调研总结**: 数学推理 self-improvement 领域在 2025-2026 年极度活跃，形式验证（FoVer）、error-targeted synthesis（STAT、Self-Error-Instruct）、weakness-driven RL（SwS）、symbolic self-training（NSRSA、Adaptive Problem Generation）各自推进了不同方面。**尚无工作将形式验证直接用于 error categorization + targeted synthesis 的闭环迭代 self-improvement**。Proposal 处于多个活跃方向的交叉点，novelty 来自整合而非单一概念突破。NSRSA 是最近的已有工作，proposal 可被视为 NSRSA 的大幅扩展（更广的验证范围、error taxonomy、step-localized DPO、targeted synthesis）。\n\n\n【Trivial Alternative 检验】:\n\n存在两个严肃的 trivial alternative 威胁：\n\n1. **SwS-style pass-rate targeting（无需任何 formal verification）**: SwS 已证明通过 pass-rate 分析识别弱点并合成针对性问题，7B 模型在 8 个 benchmark 上平均提升 10%。这种方法零额外成本（无 Z3/SymPy pipeline），且完全不受 formalization 覆盖率限制。Proposal 的增量价值在于：(a) within-subcategory 的 fine-grained skill decomposition（SwS 只能定位到 problem-level，不能区分同一 subcategory 内的不同 skill gaps），(b) step-level error localization（SwS 无法知道错在哪一步），(c) formally-verified DPO pairs（SwS 的偏好信号更 noisy）。但如果 SwS 的 coarse-grained targeting 已经捕获了大部分收益，formal profiling 的 marginal gain 可能很小。**这是核心实验必须回答的问题，proposal 正确地将其列为 baseline。**\n\n2. **Subcategory-level outcome targeting（连 SymPy 都不需要）**: 直接用 MATH 的 7 个 subcategory 标签做 oversampling。Proposal 承认这一点并将其作为 baseline。但如果 subcategory granularity 已足够（考虑到大部分模型的弱点确实可以在 subcategory 层面被识别），formal profiling 的 within-subcategory 优势可能不显著。\n\n**增量价值判断**: Proposal 的增量价值取决于一个经验性问题——\"within-subcategory skill decomposition 比 subcategory-level targeting 好多少\"。如果好很多，proposal 有实质贡献；如果差不多，形式验证 pipeline 的复杂性就不值得。Proposal 意识到了这一点，但这仍是一个未经验证的前提。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **\"形式化成功率足以避免严重选择偏差\"（关键假设）**: Proposal 预估 amenable categories 上 60-70% formalization success rate。但这意味着 30-40% 的 solutions 被排除在 formal diagnosis 之外。如果 formalization 失败的解法与成功的解法在 error type 分布上有系统性差异（例如，更复杂的推理更难形式化，而恰恰是复杂推理包含更有价值的 error signal），则 formal profiling 的代表性会严重不足。Proposal 在 pilot study 中包含了 selection bias analysis，但这个假设是否成立仍是未知的。\n\n2. **\"Near-zero noise on 60-70% coverage > 15% noise on 100% coverage\"（precision-coverage tradeoff 假说）**: 这是 proposal 的核心理论赌注。Imperfect verifier 论文证明 15% noise 是可容忍的，但并未证明 0% noise + 低覆盖就一定优于 15% noise + 全覆盖。覆盖率损失意味着 training signal 减少，可能抵消精度优势。这个假说 plausible 但远未确定。\n\n3. **\"Step-localized DPO pairs 的 yield 足够构建有效训练集\"**: 构建 step-localized pairs 需要同时满足：(a) 两条 trajectory 在前 k 步都 formally verified correct，(b) 在 step k+1 diverge。这比 solution-level pairs 的约束严格得多，yield 可能非常低。Proposal 提到用 pilot study 估计 yield 并混入 solution-level pairs 作为 fallback——这是务实的，但如果 step-localized pairs 的 yield 极低（<5%），这个 contribution 就变成了一个概念而非实际可用的方法。\n\n4. **\"Formal error taxonomy 中的 5 类错误是互斥且穷尽的\"**: Taxonomy 的质量直接影响 profiling 和 targeted synthesis 的有效性。如果实际错误不 cleanly 落入这 5 类（特别是多种错误交织的情况），targeting 的精度会下降。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   - 每个组件单独来看都不新颖：形式验证用于数学推理（FoVer, MATH-VF, Safe），error-targeted synthesis（STAT, Self-Error-Instruct），step-level DPO（Step-DPO, Full-Step-DPO），iterative self-improvement（NSRSA, SwS）。\n   - 整合层面的 novelty 是真实的：将形式验证**直接用于** error categorization + targeted synthesis + step-localized DPO 的闭环系统，没有现有工作做过。NSRSA 是最近的，但仅覆盖算术、无 taxonomy、无 targeted synthesis、仅 solution-level DPO。\n   - 但这种 novelty 是\"如果你知道 FoVer 和 STAT 各做了什么，把它们组合起来是一个自然的 next step\"——integration novelty 而非 conceptual surprise。审稿人可能评价为 \"well-executed combination, but not particularly surprising in its conception\"。\n   - error profile dynamics（Contribution 3）是一个有趣的分析贡献，如果发现 skill dependency 或 entropy-convergence 关系，有独立价值。但这更像 bonus insight 而非核心 novelty driver。\n\n2. **Significance: 中** —\n   - 研究问题确实重要：teacher-free self-improvement 是活跃方向，formal verification 消除 verifier noise 有理论支撑（Solver-Verifier Gap, ICLR 2026）。\n   - 但 **practical significance 受限于 coverage**：形式验证仅适用于 algebraic/arithmetic domains（MATH 的 ~60-70% amenable categories），geometry、counting & probability 退化为 outcome verification。这意味着方法无法通用化到所有数学推理，更不用说其他推理领域。\n   - **如果核心实验 positive**，审稿人的反应可能是 \"formal verification is more precise than LLM diagnosis — this is expected, not surprising\"。核心发现的方向性（formal > LLM for error diagnosis in amenable domains）是高度可预测的；surprise 更多来自 magnitude（好多少）和 dynamics（error profile 如何演化）。\n   - 对领域的推进作用：提供了一个有价值的 data point（formal diagnosis 在 self-improvement loop 中的定量优势），但不会改变领域的研究范式。\n\n3. **Related Work: 强** —\n   - 对已有工作的覆盖非常全面：涵盖了 self-improvement（NSRSA, SwS, SPICE, SvS），formal verification（FoVer, MATH-VF, Safe），error-targeted synthesis（STAT, Self-Error-Instruct），DPO 变体（Step-DPO, Full-Step-DPO），理论基础（Solver-Verifier Gap, Imperfect Verifier），以及 synthetic data（SPARQ, CoTEvol, MathMixup）等多个方向。\n   - 差异化定位清晰：对每个最相关工作都有具体的技术路径区分（FoVer: 间接 vs. 直接使用 formal verification; NSRSA: 仅算术 vs. 完整 taxonomy; SwS: pass-rate vs. formal diagnosis; STAT: teacher-dependent vs. teacher-free）。\n   - 经我调研验证，引用的关键论文（FoVer ACL 2026, STAT ICLR 2026, NSRSA arXiv 2603.21558, SwS NeurIPS 2025, Imperfect Verifier arXiv 2604.07666, Solver-Verifier Gap ICLR 2026, LLMs Cannot Spot Math Errors EMNLP 2025）均真实存在且描述准确。\n   - 唯一轻微不足：未讨论 Reasoning Core、Bidirectional Curriculum 等工作的具体技术细节（仅一句话提及），但这些工作与本 proposal 的距离较远，不影响定位。\n\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \n- Novelty（中）是主要限制因素，将上界压在 35% 左右。这是一个 well-motivated integration，但缺乏 conceptual surprise——\"用 formal tools 替代 LLM 做 error diagnosis\"是一个自然的 next step，不是一个反直觉的发现。NSRSA 的存在进一步压缩了 novelty delta。\n- Significance（中）提供了合理的下界支撑（~25%）。研究问题重要，有理论基础支持，但 coverage 限制和结果的可预测性阻止了更高估计。\n- Related Work（强）是正面因素，说明作者对领域的理解深入，定位清晰，降低了被\"已有工作覆盖\"直接拒稿的风险。\n- 如果 error profile dynamics 揭示出意外的 pattern（如 skill dependency ordering），可能推高到 35%；如果 SwS-style pass-rate targeting 已经接近 formal profiling 的效果，则可能跌至 25% 以下。\n\n【主要风险】:\n1. **\"Incremental combination\" 判断**：审稿人可能认为 FoVer (formal verification) + STAT (skill-targeted synthesis) + Step-DPO (step-level preference) 的组合虽然 technically sound，但 novelty 不足以单独成文——每个组件都有现成解决方案，组合本身不构成足够的 intellectual contribution。\n2. **Trivial alternative 威胁无法在实验前排除**：SwS 的 pass-rate-based targeting 已经实现了强效果（+10%），如果 formal profiling 相比 SwS 的 marginal gain 很小（例如 <2%），审稿人会质疑整个 formal verification pipeline 的 cost-effectiveness，导致 \"engineering contribution, not research contribution\" 的评价。\n```\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://openreview.net/forum?id=m3jG3GaNIj)\n- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)\n- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)\n- [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666)\n- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)\n- [LLMs Cannot Spot Math Errors (EMNLP 2025)](https://arxiv.org/abs/2509.01395)\n- [Self-Error-Instruct (ACL 2025)](https://aclanthology.org/2025.acl-long.417/)\n- [Step-DPO (NeurIPS 2024)](https://openreview.net/forum?id=H5FUVj0vMd)\n- [Full-Step-DPO (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.1249/)\n- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/html/2505.20869v1)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to evaluate this proposal. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **FoVer** (arXiv 2505.15960, ACL 2026 Findings): 使用 Z3/Isabelle 进行 formal verification 来合成 PRM 训练数据，实现 step-level 错误标注。与本 proposal 最直接相关——但 FoVer 的目标是训练 PRM（间接使用 formal verification），而非直接用 formal verification 进行 error categorization + targeted synthesis。本 proposal 明确将 FoVer-PRM+RLVR 作为 baseline。\n\n2. **STAT: Skill-Targeted Adaptive Training** (arXiv 2510.10023, ICLR 2026): 使用强 LLM teacher 进行 skill profiling，识别 missing skills，然后 reweight (STAT-Sel) 或合成 (STAT-Syn) 训练数据。在 MATH 上提升 7.5%、OOD benchmark 平均 4.6%。与本 proposal 最核心的竞争关系——STAT 做的事和 FormalLoop 高度同构，区别在于 error diagnosis 来源：LLM teacher vs. formal tools。\n\n3. **NSRSA** (arXiv 2603.21558, March 2026): 使用 SymPy 验证 arithmetic operations 来过滤 self-training 数据，构建 DPO pairs。在 GSM8K + Qwen3-4B 上测试。**这是当前与本 proposal 最接近的工作**——也用 SymPy、也做 iterative self-training、也构建 DPO pairs。但 NSRSA 仅覆盖 arithmetic verification、不做 error categorization、不做 targeted synthesis。本 proposal 的增量：error taxonomy + targeted problem generation + step-localized DPO。\n\n4. **Solver-Verifier Gap Theory** (arXiv 2507.00075, ICLR 2026): 理论建模 self-improvement dynamics，证明 verifier capability 决定 self-improvement ceiling，dynamics 遵循 exponential law。为本 proposal 的动机提供了理论支撑——formal verification 作为 near-perfect verifier 应能提升 ceiling。\n\n5. **Imperfect Verifier** (arXiv 2604.07666, April 2026): 实证发现 noise rate ≤15% 时 RLVR 仍可达到 clean baseline 2% 以内的 accuracy。Precision matters more than recall。这支撑了 proposal 的\"precision-coverage tradeoff\"假说，但也构成潜在威胁——如果 15% noise 是可容忍的，formal verification 的 near-zero noise 优势可能边际收益递减。\n\n6. **SwS** (arXiv 2506.08989, NeurIPS 2025): 基于 pass-rate 分析识别 weakness，按 category 聚类失败问题后合成新问题。7B/32B 模型在 8 个 benchmark 平均提升 10%/7.7%。与本 proposal 竞争——SwS 不需要 formal verification，仅用 pass-rate 就能做 weakness-driven synthesis，简单得多。\n\n7. **Adaptive Problem Generation** (arXiv 2602.19187, Feb 2026): 在 symbolic space 用 SymPy 做 closed-loop RLVR problem generation，通过 prompt optimization 适配 difficulty。与 FormalLoop 共享\"SymPy + closed-loop\"元素，但不做 error-type diagnosis。\n\n8. **LEMMA** (arXiv 2503.17439, 2025): 对 LLM 生成的 math solutions 做 fine-grained error categorization (question misinterpretation → calculation error)，用 error-corrective trajectories 训练。LLaMA3-8B 上 13.3% accuracy improvement。**Proposal 未引用此工作**，但 LEMMA 做的 error categorization + targeted training 思路与本 proposal 类似（区别：LEMMA 用 LLM 做 error analysis，本 proposal 用 formal tools）。\n\n**调研总结**: 这个领域正在快速发展，形成了几条平行的研究线：(a) LLM teacher-based skill profiling + targeted training (STAT, Self-Error-Instruct, LEMMA)；(b) pass-rate/outcome-based weakness targeting (SwS)；(c) symbolic verification for data quality/PRM training (FoVer, NSRSA, MATH-VF)；(d) symbolic problem generation (Adaptive Problem Generation, Reasoning Core)。本 proposal 试图桥接 (c) 和 (a)——用 formal tools 替代 LLM teacher 做 error profiling，这个具体交叉点确实尚未被占据，但周围的工作已经非常密集，留给本 proposal 的 novelty space 是\"组合型\"的而非\"开创型\"的。\n\n\n【Trivial Alternative 检验】:\n\n**存在多个成本更低的替代方案：**\n\n1. **SwS-style pass-rate targeting（最大威胁）**：SwS 仅使用 pass-rate 分析就能识别 weakness 并合成 targeted problems，不需要任何 formal verification，在 8 个 benchmark 上取得了 7.7-10% 的提升。FormalLoop 的 formal error profiling 需要 Z3/SymPy formalization pipeline（成功率仅 60-70%），工程复杂度高得多。核心问题是：formal error profiling 提供的 granularity advantage 能否显著超过 pass-rate targeting？\n\n2. **Outcome verification + category oversampling**：用 MATH 已有的 7 个 subcategory labels，对 weak subcategories 做 oversampling。完全不需要 formal verification。Proposal 承认了这个 alternative 并将其作为 baseline，这是好的。但如果 subcategory-level targeting 已经捕获了大部分收益，formal error profiling 的 within-subcategory granularity advantage 可能是边际的。\n\n3. **FoVer-PRM + Best-of-N/RLVR**：利用 FoVer 已训练好的 PRM 做 verification，在标准 self-improvement loop 中使用。不需要自己构建 formalization pipeline。\n\n**增量价值核心**在于：formal error *categorization*（不仅是 verification）+ *targeted synthesis*（不仅是 filtering）。如果 ablation 显示 error categorization → targeted synthesis 的链条中每一步都有显著增量，idea 成立；否则 trivial alternatives 就够了。这是一个需要实验验证的假设，不是逻辑上显然的。\n\n\n【前提假设检验】:\n\n**核心 claim 的逻辑链条中有 3 个关键假设未经验证：**\n\n1. **Z3/SymPy 能可靠地将 step-level errors 分类到 5-type taxonomy**：Proposal 假设 formal verification 不仅能判定 step 对错，还能将错误归类为 algebraic manipulation / equation solving / arithmetic / constraint reasoning / logical inference。但 Z3/SymPy 的 verification 本质是检查 symbolic expression 的等价性，从 \"verification failure\" 到 \"error type classification\" 之间存在 gap。一个 step 可能同时涉及多种操作，formalization failure 也可能被误分类。这个假设是否成立直接决定 pipeline 的核心功能是否可行。\n\n2. **Error-type-level targeting 显著优于 problem-level targeting**：知道\"模型在 equation solving 上弱\"比知道\"模型做错了这道题\"能产生多大的额外收益？这取决于 SymPy 合成的 targeted problems 是否真正练到了弱技能，而不仅仅是生成了更多同类题。数学技能之间的可迁移性（或不可迁移性）是一个未经验证的前提。\n\n3. **Precision-coverage tradeoff 假说中 τ ≈ 15% 的适用性**：Imperfect verifier 论文的 15% threshold 是在 RLVR 设定下测得的（reward noise 对 policy optimization 的影响），而 FormalLoop 的设定是 error profiling → targeted synthesis（diagnosis noise 对 data selection 的影响）。这两个设定下 noise tolerance 是否相同是一个未经验证的类比。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心贡献是将 formal verification 从\"verification/filtering tool\"提升为\"error diagnostician + targeted synthesis driver\"，这个具体交叉点确实尚未被占据。NSRSA (arXiv 2603.21558) 最接近但仅做 arithmetic verification 不做 error categorization；STAT (ICLR 2026) 做 skill profiling 但依赖 LLM teacher；SwS (NeurIPS 2025) 做 weakness targeting 但用 pass-rate。FormalLoop 的 step-localized formal DPO 相比 Step-DPO (NeurIPS 2024) 和 NSRSA 的 solution-level DPO 也有实质区别。但这本质上是 **组合型 novelty**——formal verification (from FoVer/MATH-VF) + error profiling (from STAT/LEMMA) + targeted synthesis (from SwS/STAT) + step-localized DPO (from Step-DPO/NSRSA) 的交叉。每个组件都有近期先例。Error profile dynamics 是相对独特的分析贡献，但作为 paper 的核心卖点偏弱。\n\n2. **Significance: 中** — \n   研究问题（teacher-free targeted self-improvement）确实重要且 timely，对应 solver-verifier gap theory (ICLR 2026) 指出的 verifier quality 瓶颈。但**核心发现的方向是可预测的**：ground-truth error diagnosis（formal tools）理应优于 noisy error diagnosis（LLM teacher）——如果结果是 positive，审稿人大概率会说 \"I would have guessed this, formal verification gives cleaner signals\"。真正 interesting 的是 by how much 以及 error profile dynamics 的 patterns，但这些属于 empirical findings 而非 idea-level surprise。此外，60-70% 的 formalization coverage 限制了方法的 generalizability——只有代数和算术类问题能享受 formal profiling，geometry 和 combinatorics 仍用 fallback。Imperfect verifier 论文 (arXiv 2604.07666) 的 15% tolerance 发现也削弱了 near-zero noise 的边际价值。\n\n3. **Related Work: 强** — \n   这是本 proposal 最突出的优势。Related work 覆盖极为全面，包括直接竞争者 (STAT, SwS, Self-Error-Instruct, WarriorMath)、formal verification 线 (FoVer, MATH-VF, Safe)、理论基础 (solver-verifier gap)、concurrent work (Adaptive Problem Generation, NSRSA, Reasoning Core, Bidirectional Curriculum)、以及 imperfect verifier 研究。对每个 related work 的差异化定位清晰准确。唯一遗漏是 LEMMA (arXiv 2503.17439) 做 fine-grained error categorization + targeted training，思路与本 proposal 类似（LLM-based vs. formal-based）。但整体 related work 质量在 AAAI 投稿中属于上乘。\n\n\n【概率估计】: [28% - 38%] 中位 33%\n\n【估计理由】: \nNovelty 中等（组合型创新，具体交叉点确实空白但非范式转变）+ Significance 中等（问题重要但核心发现方向可预测、coverage 受限）+ Related Work 强（定位清晰，差异化到位）。Related work 的强覆盖保证了下限（不会因为 \"missing important baselines\" 被直接拒），但 Novelty 和 Significance 的中等评价限制了上限——审稿人可能认可这是 solid engineering integration work 但质疑 \"what's the surprising insight?\"。上界主要受 Significance 限制：如果核心结果 positive，审稿人可能评价为 \"expected result, well-executed\"，这在顶会中通常对应 borderline accept/reject。\n\n【主要风险】: \n1. **\"Expected result\" 风险**：审稿人可能认为 \"formal verification 提供更好的 error diagnosis → 更好的 targeted training\" 是一个 obvious hypothesis，positive 结果不够 surprising，从而降低 novelty/significance 评分。\n2. **Trivial alternative 威胁**：SwS 的 pass-rate targeting 或 subcategory-level oversampling 已经很强且简单得多。如果 FormalLoop 的 formal error profiling 仅带来边际提升（比如 1-2% accuracy gain），审稿人会质疑 engineering complexity 是否值得——这不是 idea 层面的问题，但会放大\"组合型 novelty 不够\"的 perception。\n```\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL 2026)](https://arxiv.org/abs/2505.15960)\n- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://arxiv.org/abs/2510.10023)\n- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)\n- [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666)\n- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://arxiv.org/abs/2506.08989)\n- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)\n- [LEMMA: Learning from Errors for Mathematical Advancement in LLMs](https://arxiv.org/abs/2503.17439)\n- [MATH-VF: Step-Wise Formal Verification for LLM-Based Math Problem Solving](https://arxiv.org/abs/2505.20869)\n- [Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement\n\n## Core Problem\n\nSelf-improvement loops for mathematical reasoning suffer from model collapse (solver-verifier gap theory, ICLR 2026) and untargeted data waste. All existing error-targeted synthesis methods — STAT (ICLR 2026), Self-Error-Instruct (ACL 2025), SwS (NeurIPS 2025), WarriorMath (arXiv 2025) — depend on LLM teachers or LLM metacognition for error diagnosis, introducing teacher bias, hallucinated attributions, and scalability ceilings. Empirically, LLMs cannot reliably spot mathematical errors even with reference solutions (arXiv 2509.01395, EMNLP 2025). Can formal symbolic tools serve as collapse-proof verifiers and ground-truth error diagnosticians, enabling stable, teacher-free, targeted self-improvement?\n\n## Core Contributions\n\n1. **Teacher-free error-targeted self-improvement**: The first self-improvement system where error diagnosis and targeted synthesis are driven entirely by formal symbolic tools (Z3, SymPy), eliminating LLM teacher dependency. Unlike RLVR/GRPO (also teacher-free), FormalLoop targets specific error types rather than optimizing globally.\n\n2. **Formally-verified step-localized DPO**: Preference pairs where trajectories share k formally-verified-correct steps and diverge at step k+1 — providing step-localized credit assignment with formal guarantees. Unlike Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) which use LLM/human annotations, and unlike NSRSA (arXiv 2026) which constructs solution-level accept/reject pairs, our pairs provide zero-noise step-localized preference signals.\n\n3. **Ground-truth error profile dynamics**: FormalLoop uniquely enables tracking formally-verified per-skill-type error evolution across self-improvement iterations — answering whether error types have fixed reduction priority orderings, whether skill dependencies exist (e.g., arithmetic errors must resolve before algebraic errors become visible), and whether error profile entropy predicts convergence. No prior work provides ground-truth skill-decomposed self-improvement dynamics.\n\n4. **Precision-coverage tradeoff hypothesis**: We hypothesize that in self-improvement loops, there exists a verifier noise threshold τ beyond which expanding coverage yields negative marginal returns. Imperfect verifier research (arXiv 2604.07666, arXiv 2026) estimates τ ≈ 15%; solver-verifier gap theory (ICLR 2026) predicts verifier reliability determines the self-improvement ceiling. FormalLoop tests this: formal verification achieves near-zero noise within its scope (~60-70% of amenable categories), which should outperform full-coverage but noisier LLM diagnosis. We validate via noise injection ablation.\n\n## Why Not Simpler Alternatives?\n\n**vs. Outcome verification + STAT-style LLM teacher profiling**: (1) Error attribution precision — outcome verification doesn't localize errors; LLM step diagnosis hallucinates (arXiv 2509.01395, EMNLP 2025); formal verification provides guaranteed step-level attribution. (2) Iterative stability — LLM teacher biases compound across iterations; formal diagnosis is independently calibrated each round. (3) No teacher ceiling — STAT's profiling quality is bounded by teacher metacognition.\n\n**vs. Subcategory-level outcome targeting** (using MATH's existing 7 subcategory labels to oversample weak categories): This requires no formal verification at all. However, subcategory labels are coarse — within Algebra alone, a model may struggle specifically with equation solving but not algebraic manipulation. Formal step-level diagnosis provides within-subcategory skill decomposition that subcategory-level targeting cannot. We include subcategory-level targeting as an explicit baseline to quantify this granularity advantage.\n\n**vs. FoVer-PRM as verifier in a standard self-improvement loop**: FoVer (ACL 2026) trains PRMs from formal verification data for general use. A natural alternative is using a FoVer-trained PRM as the verifier in a self-improvement loop (via Best-of-N or RLVR). FormalLoop differs by using formal verification directly for error categorization and targeted synthesis — not indirectly through a learned PRM. We include FoVer-PRM + RLVR as a baseline to isolate direct formal profiling's advantage.\n\n## Research Landscape\n\nCurrent SOTA in synthetic math data: SPARQ (June 2025, +24% via quality-diversity from 7.5K seeds), CoTEvol (April 2026, +6.6% via evolutionary CoT synthesis), MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). Self-improvement: SPICE (Oct 2025, +8.9% via document-grounded self-play), SvS (Aug 2025, +18.3% Pass@32 on AIME24 via variational problem synthesis). Verification: FoVer (ACL 2026) trains PRMs from formal verification across 12 benchmarks; imperfect verifier research (arXiv 2604.07666, arXiv 2026) shows ≤15% noise is tolerable with precision mattering more than recall. Concurrent: Adaptive Problem Generation (arXiv 2602.19187, Feb 2026) uses SymPy in closed-loop RLVR but adapts difficulty globally without error-type diagnosis. SwS (NeurIPS 2025) identifies weaknesses via pass-rate analysis without formal diagnosis. Reasoning Core (March 2026) generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) does step-aware Lean 4 verification in one-shot refinement, not closed-loop. Bidirectional Curriculum (March 2026) dynamically adjusts difficulty without formal verification. NSRSA (arXiv 2026) uses SymPy arithmetic verification for iterative self-training on GSM8K with solution-level DPO, but covers only arithmetic operations without error categorization or targeted synthesis. MATH-VF (arXiv 2025) uses Z3+SymPy for step-wise verification but as a training-free inference tool.\n\n## Proposed Approach\n\nFormalLoop runs iterative cycles on a student model (Qwen3.5-9B primary, Qwen3.5-4B validation): (1) student solves problems, (2) solutions are formalized and verified step-by-step via Z3/SymPy, (3) step-level errors classified into a formal taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), (4) SymPy-based synthesis generates targeted problems exercising weak skills with solver-guaranteed solutions, (5) student trains via SFT+DPO on targeted data and formally-constructed preference pairs, then re-profiled.\n\n**Formal coverage scope**: Formal verification covers algebraic and arithmetic domains amenable to Z3/SymPy (Algebra, Number Theory, Prealgebra, portions of Intermediate Algebra and Precalculus). Geometry and Counting & Probability use outcome-based verification as fallback. Per-category formalization success rates are reported. Even partial coverage with near-zero noise can outperform full-coverage noisy LLM diagnosis (imperfect verifier research, arXiv 2604.07666).\n\n**Formalization quality control**: To prevent conflating formalization failures with reasoning errors: (a) distinguish \"verification failed\" from \"formalization failed\" status, (b) exclude solutions where formal rejection co-occurs with correct final answer, (c) use only high-confidence pairs for DPO. Target noise rate well below the 15% tolerance threshold (arXiv 2604.07666).\n\n**DPO pair construction with fallback**: Primary: step-localized pairs (shared k correct steps, diverge at k+1). When step-localized pairs are insufficient (estimated via pilot study yield analysis), mix in solution-level formally-verified pairs (NSRSA-style). Report mixing ratio and its effect on training.\n\n## Experimental Design\n\n**Models**: Qwen3.5-9B (primary, 5 iterations) + Qwen3.5-4B (validation, 3 iterations). Pilot study includes Llama 3.1-8B formalization success rate comparison (not full training loop).\n\n**Benchmarks**: GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench. OOD generalization on AIME24/25. Per-MATH-subcategory breakdown (formally-covered vs. fallback).\n\n**Evaluation protocol**: Greedy accuracy + Pass@K (K=8, 32) + majority voting@K. 3 independent runs, mean ± std, significance tests. Per-problem sampling: 16-32 solutions for DPO pair construction.\n\n**Baseline matrix**:\n- Training paradigm: Vanilla SFT (uniform), SFT+DPO (uniform), GRPO/RLVR\n- Targeting: SwS (NeurIPS 2025, pass-rate weakness targeting), STAT-style (GPT-4o teacher) profiling + targeted synthesis, subcategory-level outcome targeting\n- Symbolic: Adaptive Problem Generation (arXiv 2602.19187, global difficulty adaptation)\n- Verification: FoVer-PRM (ACL 2026, github.com/psunlpgroup/FoVer) + Best-of-N/RLVR loop, outcome-only verification loop (NSRSA-style)\n\n**Ablation studies** (priority-ranked; ablations run on Qwen3.5-4B, 2-3 iterations, 3 benchmarks: GSM8K, MATH-500, AIME24):\n1. [Must] Error profiling source: Formal vs. LLM-based vs. pass-rate-based vs. subcategory-level vs. random\n2. [Must] Preference pair source: Step-localized formal DPO vs. solution-level formal DPO (NSRSA-style) vs. outcome DPO vs. LLM-annotated DPO (Step-DPO style)\n3. [Must] Targeting vs. uniform: Targeted synthesis vs. uniform synthesis (same quantity)\n4. [Should] Training objective: SFT only vs. DPO only vs. SFT+DPO\n5. [Should] Taxonomy granularity: 5-type vs. 2-type (arithmetic/non-arithmetic) vs. single aggregate\n6. [Should] Iteration dynamics: Per-iteration accuracy, error profile evolution, formalization coverage, entropy curves\n7. [Nice] Precision-coverage tradeoff: Inject artificial noise (5%, 10%, 15%, 20%) into formal labels, measure impact on self-improvement trajectory\n\n**Compute fairness**: Unified metric: total dollar cost (GPU + CPU + API). Report per-method cost breakdown. Compute-matched comparisons: (i) fixed GPU training FLOPs, (ii) fixed total dollar budget. Accuracy vs. total cost curves.\n\n**Pilot study** (before main experiments):\n- Per-subcategory formalization success rate on MATH-Train (200-300 problems per subcategory)\n- Failure mode analysis: formalization failure vs. solver timeout vs. scope limitation\n- Selection bias analysis: compare error type distributions between formalization-success and formalization-failure groups\n- DPO pair yield estimation: 500 problems × 16 solutions, count constructable step-localized pairs\n- Cross-family comparison: Qwen3.5-9B vs. Llama 3.1-8B formalization success rates\n- Taxonomy coverage validation and comparison with STAT's skill taxonomy\n- Human evaluation of 100-200 synthesized problems (well-formedness, difficulty, NL quality)\n\n## Key References\n\n- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)\n- STAT: Skill-Targeted Adaptive Training (ICLR 2026)\n- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)\n- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)\n- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)\n- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)\n- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)\n- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)\n- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)\n- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)\n- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)\n- Adaptive Problem Generation via Symbolic Representations (arXiv 2026, arXiv 2602.19187)\n- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026, arXiv 2604.07666)\n- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)\n- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)\n- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)\n- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)\n- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)\n- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)\n- Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs (NeurIPS 2024)\n- Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning (ACL 2025 Findings)\n- LLMs Cannot Spot Math Errors Even When Allowed to Peek into the Solution (EMNLP 2025, arXiv 2509.01395)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 750 H100 hours (5 iterations 9B + 3 iterations 4B + ablations on 4B + pilot study + evaluation), timeline: 4-5 months, estimated_gpu_cost: $1,875\n- **human_in_loop**: gpu_hours: 700 H100 hours, timeline: 3-4 months, claude_api_cost: $500-700 (pipeline code, taxonomy iteration, analysis), teacher_api_cost: $200-400 (GPT-4o for STAT baseline), estimated_gpu_cost: $1,750\n- **auto_research**: gpu_hours: 700 H100 hours, timeline: 6-8 weeks, claude_api_cost: $1,500-2,500, teacher_api_cost: $200-400, estimated_gpu_cost: $1,750, speed_bottleneck: Z3/SymPy step verification is CPU-bound (~0.5-2s per step); LLM-to-formal translation ~60-70% success rate on amenable categories requires retry loops"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T09:10:03.041Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T09:10:03.041Z",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T09:10:03.053Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research material to conduct a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **STAT: Skill-Targeted Adaptive Training (ICLR 2026, arXiv 2510.10023)**:
   最直接的竞争者之一。STAT 使用强 LLM 教师（如 GPT-4）做元认知技能诊断，创建 Missing-Skill-Profile，然后针对性地重采样或合成训练数据。在 Llama/Qwen 上 MATH 提升达 7.5%，OOD 平均提升 4.6%。本 proposal 的核心差异化在于用 formal tools 替代 LLM 教师做诊断——消除教师偏差和幻觉归因。

2. **NSRSA: Symbolic Recursive Self-Alignment (arXiv 2603.21558, March 2026)**:
   最近的竞争者。NSRSA 已经在迭代自训练中使用 SymPy 做算术运算级别的符号验证，过滤掉约 34% 的"lucky guess"正确答案，并结合 DPO。但 NSRSA 仅覆盖算术操作验证，**不做错误分类或针对性合成**，DPO 是 solution-level 而非 step-localized。在 GSM8K + Qwen3-4B 上实验，规模较小。本 proposal 的增量在于：(a) 错误类型分类，(b) 针对性合成，(c) step-localized DPO。

3. **FoVer (ACL 2026 Findings, arXiv 2505.15960)**:
   使用 Z3 和 Isabelle 对 formal reasoning 任务的 LLM 响应做 step-level error label 标注，合成 PRM 训练数据（FoVer-40K）。在 12 个 benchmark 上训练的 PRM 超越 baseline。FoVer 的目标是训练通用 PRM，不做闭环自改进或错误分类。本 proposal 的差异在于直接使用 formal verification 做诊断+针对性合成，而非间接训练 PRM。

4. **SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025, arXiv 2506.08989)**:
   通过 pass-rate 分析识别 RL 训练中模型持续失败的问题，提取核心概念后合成新问题。7B 模型平均提升 10.0%，32B 提升 7.7%。SwS 的弱点诊断基于 pass-rate（统计层面），不做 step-level 错误归因。本 proposal 的优势在于 formal step-level diagnosis 提供更精细的技能分解。

5. **Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, Feb 2026)**:
   使用 SymPy 的符号表示空间做闭环 RLVR 问题生成，自适应调整难度。但是全局难度调整，不做错误类型诊断。是最接近的"使用符号工具做闭环自改进"的工作，但粒度不同（全局难度 vs. 错误类型针对）。

6. **Solver-Verifier Gap Theory (ICLR 2026, arXiv 2507.00075)**:
   理论建模 LLM 自改进的训练动力学，证明验证器可靠性决定自改进的天花板，能力提升遵循指数律趋近极限。为本 proposal 的"formal verification 作为 collapse-proof verifier"提供了理论基础。

7. **Imperfect Verifier (arXiv 2604.07666, April 2026)**:
   实证表明噪声率 ≤15% 时，RLVR 验证准确率在 clean baseline 2 个百分点以内。precision 比 recall 更重要。为本 proposal 的"precision-coverage tradeoff hypothesis"提供了直接实证支撑。

8. **LLMs Cannot Spot Math Errors (EMNLP 2025, arXiv 2509.01395)**:
   证明 SOTA LLMs 在有参考解答的情况下仍难以定位学生解答中的第一个错误步骤。为本 proposal "LLM 教师诊断不可靠"的前提提供了实证支撑。

- **调研总结**: 数学推理自改进是 2025-2026 最活跃的研究方向之一。当前格局中，formal verification 已被用于 PRM 训练数据合成（FoVer）和迭代自训练过滤（NSRSA），weakness-driven synthesis 已有 pass-rate 方法（SwS）和 LLM 教师方法（STAT），step-level DPO 已有 LLM/人工标注版本（Step-DPO, Full-Step-DPO）。本 proposal 处于这些工作的**交汇点**——将 formal verification 从"验证/过滤工具"升级为"诊断+分类+针对性合成"的完整闭环，这一具体组合尚无先例，但各组件均有成熟前驱工作。

【Trivial Alternative 检验】:

存在两个值得认真考虑的 trivial alternatives：

**(1) NSRSA + 更广的符号覆盖**：NSRSA 已经用 SymPy 做算术验证 + 迭代 DPO。如果简单扩展 NSRSA 的符号验证范围（从算术到代数），是否就能获得大部分收益？本 proposal 的增量价值在于：(a) 错误分类 taxonomy（5 种类型），(b) 基于分类的针对性合成，(c) step-localized DPO pair 构造。其中 (a)+(b) 是核心增量——问题是这个增量有多大。如果简单地用 formal verification 做更严格的过滤（不分类）就能获得主要收益，那分类+针对性合成的边际价值可能有限。Proposal 承诺通过 ablation (targeting vs. uniform) 量化这一增量，设计合理。

**(2) Subcategory-level outcome targeting**：Proposal 自身承认这是最简单的替代方案，并纳入 baseline。核心问题是：MATH 的 7 个子类别粒度是否足够？Proposal 声称 within-subcategory skill decomposition 有价值，但这一主张尚未验证。如果 subcategory-level targeting 就能获得 80-90% 的收益，formal error profiling 的工程复杂度就不划算了。

**增量价值判断**：增量价值真实存在但可能有限。最有价值的独特贡献是 (1) step-localized formal DPO pairs 和 (2) error profile dynamics 分析——这两者确实无法通过 trivial alternatives 实现。

【前提假设检验】:

核心逻辑链中有以下未经验证的前提假设：

**(1) "LLM-to-formal translation 成功率 60-70% 是足够的"**：这是最关键的假设。Proposal 声称 formal verification 覆盖代数/算术领域的 60-70%，但这个数字本身是估计。更关键的是：formalization 失败的 30-40% 是否会引入系统性偏差？如果 formalization 更容易对简单问题成功，error profile 就会偏向高难度错误的低估。Proposal 提到了 selection bias analysis（pilot study），说明作者意识到了这个问题，但目前没有证据表明偏差可控。

**(2) "5 类 formal error taxonomy 足以捕获有意义的技能分解"**：Taxonomy 包括 algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference。这个分类是否与模型实际的能力瓶颈对齐？STAT 的 LLM-driven taxonomy 是 data-driven 的，可能更贴合实际；formal taxonomy 受制于 Z3/SymPy 能区分的错误类型，可能遗漏重要维度（如 problem comprehension errors, strategy selection errors）。

**(3) "Targeted synthesis 优于 uniform synthesis 的效果来自错误分类的精细度"**：这个因果关系未经验证。也许 targeted synthesis 的优势主要来自"更多练习弱项"这个粗粒度策略，而非"精确知道是 equation solving 还是 algebraic manipulation"。如果 2-type taxonomy (arithmetic/non-arithmetic) 就能获得大部分收益，5-type taxonomy 的价值就存疑。Proposal 设计了 taxonomy granularity ablation，但结果未知。

**(4) "Formal verification 在迭代中保持独立校准"**：Proposal 声称 formal diagnosis 不会像 LLM 教师那样在迭代中积累偏差。这在技术上成立（Z3/SymPy 是确定性的），但忽略了一个间接路径：如果模型学会了"在 formally verifiable 的步骤上做得更好"但在 non-verifiable 的步骤上退化（Goodhart's Law），迭代稳定性可能是表面的。

【3 维度打分】:

1. **Novelty: 中** — 
   各核心组件均有明确前驱：formal verification for math → FoVer (ACL 2026), MATH-VF (arXiv 2025); symbolic verification in iterative self-training → NSRSA (arXiv 2026); weakness-targeted synthesis → STAT (ICLR 2026), SwS (NeurIPS 2025); step-level DPO → Step-DPO (NeurIPS 2024), Full-Step-DPO (ACL 2025 Findings); symbolic problem generation in closed-loop → Adaptive Problem Generation (arXiv 2602.19187)。

   真正的 novelty delta 在于：(a) formal verification 从"过滤/验证工具"升级为"诊断+分类+针对性合成引擎"的完整闭环——这个组合确实无先例；(b) step-localized formal DPO pairs（相对于 NSRSA 的 solution-level 和 Step-DPO 的 LLM-annotated）；(c) ground-truth error profile dynamics 分析（无先例）。

   但剔除 surface differences 后，核心洞察（"用 formal tools 替代 LLM 做更精确的错误诊断"）是一个 **自然的方向延伸**，而非 conceptual surprise。NSRSA 已经走了一半路（SymPy 验证 + 迭代 DPO），本 proposal 走完了另一半（分类 + 针对性合成 + step-localized）。

2. **Significance: 中** — 
   研究问题（self-improvement stability 和 targeted synthesis for math reasoning）毫无疑问是重要且 trending 的方向。但本 proposal 的影响力受限于：
   - **覆盖范围有限**：仅对代数/算术类问题有效（~60-70% formalization 成功率，且仅在 amenable categories 上），几何、组合等必须 fallback 到 outcome verification。这不是一个通用方案。
   - **结果可预测性偏高**：如果 formal diagnosis + targeted synthesis 优于 LLM diagnosis + targeted synthesis，审稿人可能反应为 "makes sense — formal tools are more precise by definition, so of course they work better where they can be applied"。真正的 insight 在于 precision-coverage tradeoff 的量化分析，但这更像一个 empirical finding 而非 paradigm shift。
   - **可推广性问题**：方法的核心依赖 Z3/SymPy 的可形式化特性，难以推广到其他推理领域（代码、逻辑、常识推理）。

   积极面：error profile dynamics 的分析贡献对理解 self-improvement 机制有独立价值，precision-coverage tradeoff 的量化对 imperfect verifier 研究方向有参考意义。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。覆盖了几乎所有直接竞争工作（STAT, NSRSA, FoVer, SwS, Step-DPO, Full-Step-DPO, MATH-VF, Safe, Adaptive Problem Generation, Reasoning Core, Bidirectional Curriculum, SPARQ, CoTEvol, MathMixup, SPICE, SvS, WarriorMath, Self-Error-Instruct），引用的论文经验证均真实存在且描述准确。差异化定位清晰且诚实——特别是 "Why Not Simpler Alternatives" 部分主动讨论了 trivial alternatives 并设计了针对性 baseline。这种水平的 related work 覆盖在 AAAI submissions 中属于上游。

【概率估计】: [25% - 35%] 中位 29%

【估计理由】: 
三个维度中，Related Work 是明确的强项，不会成为拒稿理由。Novelty 和 Significance 均为"中"——novelty 是组合式的（各组件有前驱，组合本身新颖但方向自然/可预测），significance 受限于 formal verification 的覆盖范围和结果可预测性。

**上界限制因素是 Novelty**。核心问题是：审稿人看到"用 formal tools 替代 LLM 做错误诊断"时，反应很可能是 "natural extension, well-executed but not surprising" 而非 "I wouldn't have thought of this"。NSRSA (arXiv 2026, March) 已经在同一方向走了一大步，将本 proposal 的 novelty space 进一步压缩。

**中位 29% 的定位依据**：idea 有实质的 novelty delta（error profile dynamics、step-localized formal DPO 是真正的新贡献），方向正确且重要，但核心发现的 surprise factor 偏低。在 25-35% 区间的下半段，因为 (1) 最接近的竞争者 NSRSA 非常近且发表在 proposal 之前，(2) 如果核心实验结果是 positive，审稿人大概率反应为 "I would have guessed this"。

【主要风险】:
1. **Novelty 被判为 incremental over NSRSA + STAT**：NSRSA 已做 SymPy 验证 + 迭代 DPO，STAT 已做 skill profiling + targeted synthesis。审稿人可能认为本 proposal 只是将两者的最佳部分拼接（formal diagnosis from NSRSA 的方向 + targeting from STAT 的策略），组合本身不构成足够的 conceptual contribution。
2. **核心结果可预测性导致 significance 质疑**："Formal verification is more precise than LLM diagnosis → better targeted synthesis → better self-improvement" 这条因果链过于直觉化。如果实验验证了这一预期，审稿人可能认为 contribution 主要在工程层面而非科学发现层面。唯一能打破这一预期的结果是 precision-coverage tradeoff 显示出非直觉的 sweet spot，但这是 ablation 级别的发现，难以支撑整篇论文的 significance。
```

Sources:
- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://openreview.net/forum?id=m3jG3GaNIj)
- [NSRSA: Symbolic Recursive Self-Alignment (arXiv 2603.21558)](https://arxiv.org/abs/2603.21558)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL 2026 Findings)](https://arxiv.org/abs/2505.15960)
- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)
- [Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187)](https://arxiv.org/abs/2602.19187)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)
- [An Imperfect Verifier is Good Enough (arXiv 2604.07666)](https://arxiv.org/abs/2604.07666)
- [LLMs Cannot Spot Math Errors (EMNLP 2025)](https://arxiv.org/abs/2509.01395)
- [Step-DPO (NeurIPS 2024)](https://openreview.net/forum?id=H5FUVj0vMd)
- [Full-Step-DPO (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.1249/)
- [MATH-VF: Step-Wise Formal Verification (arXiv 2505.20869)](https://arxiv.org/html/2505.20869v1)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

1. **FoVer (ACL 2026 Findings, arXiv 2505.15960)**: 使用 Z3 和 Isabelle 等形式验证工具合成 PRM 训练数据，在 12 个推理 benchmark 上表现优于人工标注或强模型标注的 PRM。证明了形式验证在 step-level 数学验证上的可行性。与本 proposal 的关系：FoVer 用形式验证训练 PRM（间接使用），proposal 则直接在 self-improvement loop 中使用形式验证做 error diagnosis 和 targeted synthesis（直接使用）。是最近的竞争性工作，但技术路径不同。

2. **STAT (ICLR 2026, arXiv 2510.10023)**: 使用 LLM teacher（GPT-4o）进行 skill profiling，创建 Missing-Skill-Profile 后自适应重采样或合成训练数据。在 MATH 上提升 7.5%，OOD benchmark 平均提升 4.6%。与本 proposal 的关系：STAT 是本 proposal 最直接的竞争对手——同样做 skill-targeted synthesis，但依赖 LLM teacher。Proposal 的核心 claim 就是用 formal tools 替代 STAT 中的 LLM teacher。

3. **NSRSA (arXiv 2603.21558, 2026)**: 使用 SymPy 验证每个算术操作，在 GSM8K 上用 Qwen3-4B 进行 5 轮迭代自训练，包含 solution-level DPO。拒绝了约 34% 通过 outcome verification 的"lucky guess"。与本 proposal 的关系：**这是最接近的工作**——同样使用 SymPy 在迭代 self-training 中做形式验证。但 NSRSA 仅覆盖算术操作、无 error categorization、做 solution-level DPO 而非 step-localized DPO。Proposal 是 NSRSA 的自然且显著扩展。

4. **SwS (NeurIPS 2025, arXiv 2506.08989)**: 通过 pass-rate 分析识别弱点，合成针对性问题。7B/32B 模型在 8 个 benchmark 上分别提升 10%/7.7%。与本 proposal 的关系：SwS 做 weakness-driven synthesis 但不用 formal diagnosis——是一个重要的 ablation 对照点。SwS 的强结果构成对 proposal 的"trivial alternative"威胁：pass-rate 分析可能已足够好。

5. **Adaptive Problem Generation (arXiv 2602.19187, Feb 2026)**: 使用 SymPy 在 closed-loop RLVR 中生成自适应难度问题，但全局调整难度而不做 error-type diagnosis。与本 proposal 的关系：同样使用 SymPy + closed-loop，但无 error categorization——是另一个重要对照。

6. **Imperfect Verifier (arXiv 2604.07666, Apr 2026)**: 证明 noise rate ≤15% 时 RLVR 仍可有效训练，precision 比 recall 更重要。在 Qwen3、GLM4、Llama 3.1 上验证。与本 proposal 的关系：直接支持 proposal 的 precision-coverage tradeoff 假说——高精度低覆盖可能优于低精度高覆盖。

7. **Solver-Verifier Gap Theory (ICLR 2026, arXiv 2507.00075)**: 理论建模 self-improvement 训练动态，证明 verifier 可靠性决定 self-improvement 上限。与本 proposal 的关系：为 proposal 的 formal verification 动机提供理论基础。

8. **LLMs Cannot Spot Math Errors (EMNLP 2025, arXiv 2509.01395)**: 实证表明即使给出参考解答，SOTA LLM 仍难以定位数学推理中的第一个错误步骤。与本 proposal 的关系：直接支持 proposal "LLM error diagnosis 不可靠"的前提假设。

9. **Self-Error-Instruct (ACL 2025, arXiv 2505.22591)**: 使用 GPT-4o 分析错误 keyphrases 并聚类为 error types，然后合成训练数据。与本 proposal 的关系：同样做 error-type-driven synthesis，但依赖 LLM teacher。

10. **Step-DPO (NeurIPS 2024) / Full-Step-DPO (ACL 2025 Findings)**: Step-DPO 以单个推理步骤为偏好对比单元，Full-Step-DPO 用自监督 PRM 打分避免人工/GPT-4 标注。与本 proposal 的关系：Proposal 的 step-localized DPO 使用 formal verification 而非 LLM/PRM 来保证 step-level 正确性。

- **调研总结**: 数学推理 self-improvement 领域在 2025-2026 年极度活跃，形式验证（FoVer）、error-targeted synthesis（STAT、Self-Error-Instruct）、weakness-driven RL（SwS）、symbolic self-training（NSRSA、Adaptive Problem Generation）各自推进了不同方面。**尚无工作将形式验证直接用于 error categorization + targeted synthesis 的闭环迭代 self-improvement**。Proposal 处于多个活跃方向的交叉点，novelty 来自整合而非单一概念突破。NSRSA 是最近的已有工作，proposal 可被视为 NSRSA 的大幅扩展（更广的验证范围、error taxonomy、step-localized DPO、targeted synthesis）。


【Trivial Alternative 检验】:

存在两个严肃的 trivial alternative 威胁：

1. **SwS-style pass-rate targeting（无需任何 formal verification）**: SwS 已证明通过 pass-rate 分析识别弱点并合成针对性问题，7B 模型在 8 个 benchmark 上平均提升 10%。这种方法零额外成本（无 Z3/SymPy pipeline），且完全不受 formalization 覆盖率限制。Proposal 的增量价值在于：(a) within-subcategory 的 fine-grained skill decomposition（SwS 只能定位到 problem-level，不能区分同一 subcategory 内的不同 skill gaps），(b) step-level error localization（SwS 无法知道错在哪一步），(c) formally-verified DPO pairs（SwS 的偏好信号更 noisy）。但如果 SwS 的 coarse-grained targeting 已经捕获了大部分收益，formal profiling 的 marginal gain 可能很小。**这是核心实验必须回答的问题，proposal 正确地将其列为 baseline。**

2. **Subcategory-level outcome targeting（连 SymPy 都不需要）**: 直接用 MATH 的 7 个 subcategory 标签做 oversampling。Proposal 承认这一点并将其作为 baseline。但如果 subcategory granularity 已足够（考虑到大部分模型的弱点确实可以在 subcategory 层面被识别），formal profiling 的 within-subcategory 优势可能不显著。

**增量价值判断**: Proposal 的增量价值取决于一个经验性问题——"within-subcategory skill decomposition 比 subcategory-level targeting 好多少"。如果好很多，proposal 有实质贡献；如果差不多，形式验证 pipeline 的复杂性就不值得。Proposal 意识到了这一点，但这仍是一个未经验证的前提。


【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **"形式化成功率足以避免严重选择偏差"（关键假设）**: Proposal 预估 amenable categories 上 60-70% formalization success rate。但这意味着 30-40% 的 solutions 被排除在 formal diagnosis 之外。如果 formalization 失败的解法与成功的解法在 error type 分布上有系统性差异（例如，更复杂的推理更难形式化，而恰恰是复杂推理包含更有价值的 error signal），则 formal profiling 的代表性会严重不足。Proposal 在 pilot study 中包含了 selection bias analysis，但这个假设是否成立仍是未知的。

2. **"Near-zero noise on 60-70% coverage > 15% noise on 100% coverage"（precision-coverage tradeoff 假说）**: 这是 proposal 的核心理论赌注。Imperfect verifier 论文证明 15% noise 是可容忍的，但并未证明 0% noise + 低覆盖就一定优于 15% noise + 全覆盖。覆盖率损失意味着 training signal 减少，可能抵消精度优势。这个假说 plausible 但远未确定。

3. **"Step-localized DPO pairs 的 yield 足够构建有效训练集"**: 构建 step-localized pairs 需要同时满足：(a) 两条 trajectory 在前 k 步都 formally verified correct，(b) 在 step k+1 diverge。这比 solution-level pairs 的约束严格得多，yield 可能非常低。Proposal 提到用 pilot study 估计 yield 并混入 solution-level pairs 作为 fallback——这是务实的，但如果 step-localized pairs 的 yield 极低（<5%），这个 contribution 就变成了一个概念而非实际可用的方法。

4. **"Formal error taxonomy 中的 5 类错误是互斥且穷尽的"**: Taxonomy 的质量直接影响 profiling 和 targeted synthesis 的有效性。如果实际错误不 cleanly 落入这 5 类（特别是多种错误交织的情况），targeting 的精度会下降。


【3 维度打分】:

1. **Novelty: 中** — 
   - 每个组件单独来看都不新颖：形式验证用于数学推理（FoVer, MATH-VF, Safe），error-targeted synthesis（STAT, Self-Error-Instruct），step-level DPO（Step-DPO, Full-Step-DPO），iterative self-improvement（NSRSA, SwS）。
   - 整合层面的 novelty 是真实的：将形式验证**直接用于** error categorization + targeted synthesis + step-localized DPO 的闭环系统，没有现有工作做过。NSRSA 是最近的，但仅覆盖算术、无 taxonomy、无 targeted synthesis、仅 solution-level DPO。
   - 但这种 novelty 是"如果你知道 FoVer 和 STAT 各做了什么，把它们组合起来是一个自然的 next step"——integration novelty 而非 conceptual surprise。审稿人可能评价为 "well-executed combination, but not particularly surprising in its conception"。
   - error profile dynamics（Contribution 3）是一个有趣的分析贡献，如果发现 skill dependency 或 entropy-convergence 关系，有独立价值。但这更像 bonus insight 而非核心 novelty driver。

2. **Significance: 中** —
   - 研究问题确实重要：teacher-free self-improvement 是活跃方向，formal verification 消除 verifier noise 有理论支撑（Solver-Verifier Gap, ICLR 2026）。
   - 但 **practical significance 受限于 coverage**：形式验证仅适用于 algebraic/arithmetic domains（MATH 的 ~60-70% amenable categories），geometry、counting & probability 退化为 outcome verification。这意味着方法无法通用化到所有数学推理，更不用说其他推理领域。
   - **如果核心实验 positive**，审稿人的反应可能是 "formal verification is more precise than LLM diagnosis — this is expected, not surprising"。核心发现的方向性（formal > LLM for error diagnosis in amenable domains）是高度可预测的；surprise 更多来自 magnitude（好多少）和 dynamics（error profile 如何演化）。
   - 对领域的推进作用：提供了一个有价值的 data point（formal diagnosis 在 self-improvement loop 中的定量优势），但不会改变领域的研究范式。

3. **Related Work: 强** —
   - 对已有工作的覆盖非常全面：涵盖了 self-improvement（NSRSA, SwS, SPICE, SvS），formal verification（FoVer, MATH-VF, Safe），error-targeted synthesis（STAT, Self-Error-Instruct），DPO 变体（Step-DPO, Full-Step-DPO），理论基础（Solver-Verifier Gap, Imperfect Verifier），以及 synthetic data（SPARQ, CoTEvol, MathMixup）等多个方向。
   - 差异化定位清晰：对每个最相关工作都有具体的技术路径区分（FoVer: 间接 vs. 直接使用 formal verification; NSRSA: 仅算术 vs. 完整 taxonomy; SwS: pass-rate vs. formal diagnosis; STAT: teacher-dependent vs. teacher-free）。
   - 经我调研验证，引用的关键论文（FoVer ACL 2026, STAT ICLR 2026, NSRSA arXiv 2603.21558, SwS NeurIPS 2025, Imperfect Verifier arXiv 2604.07666, Solver-Verifier Gap ICLR 2026, LLMs Cannot Spot Math Errors EMNLP 2025）均真实存在且描述准确。
   - 唯一轻微不足：未讨论 Reasoning Core、Bidirectional Curriculum 等工作的具体技术细节（仅一句话提及），但这些工作与本 proposal 的距离较远，不影响定位。


【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
- Novelty（中）是主要限制因素，将上界压在 35% 左右。这是一个 well-motivated integration，但缺乏 conceptual surprise——"用 formal tools 替代 LLM 做 error diagnosis"是一个自然的 next step，不是一个反直觉的发现。NSRSA 的存在进一步压缩了 novelty delta。
- Significance（中）提供了合理的下界支撑（~25%）。研究问题重要，有理论基础支持，但 coverage 限制和结果的可预测性阻止了更高估计。
- Related Work（强）是正面因素，说明作者对领域的理解深入，定位清晰，降低了被"已有工作覆盖"直接拒稿的风险。
- 如果 error profile dynamics 揭示出意外的 pattern（如 skill dependency ordering），可能推高到 35%；如果 SwS-style pass-rate targeting 已经接近 formal profiling 的效果，则可能跌至 25% 以下。

【主要风险】:
1. **"Incremental combination" 判断**：审稿人可能认为 FoVer (formal verification) + STAT (skill-targeted synthesis) + Step-DPO (step-level preference) 的组合虽然 technically sound，但 novelty 不足以单独成文——每个组件都有现成解决方案，组合本身不构成足够的 intellectual contribution。
2. **Trivial alternative 威胁无法在实验前排除**：SwS 的 pass-rate-based targeting 已经实现了强效果（+10%），如果 formal profiling 相比 SwS 的 marginal gain 很小（例如 <2%），审稿人会质疑整个 formal verification pipeline 的 cost-effectiveness，导致 "engineering contribution, not research contribution" 的评价。
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://openreview.net/forum?id=m3jG3GaNIj)
- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)
- [LLMs Cannot Spot Math Errors (EMNLP 2025)](https://arxiv.org/abs/2509.01395)
- [Self-Error-Instruct (ACL 2025)](https://aclanthology.org/2025.acl-long.417/)
- [Step-DPO (NeurIPS 2024)](https://openreview.net/forum?id=H5FUVj0vMd)
- [Full-Step-DPO (ACL 2025 Findings)](https://aclanthology.org/2025.findings-acl.1249/)
- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/html/2505.20869v1)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **FoVer** (arXiv 2505.15960, ACL 2026 Findings): 使用 Z3/Isabelle 进行 formal verification 来合成 PRM 训练数据，实现 step-level 错误标注。与本 proposal 最直接相关——但 FoVer 的目标是训练 PRM（间接使用 formal verification），而非直接用 formal verification 进行 error categorization + targeted synthesis。本 proposal 明确将 FoVer-PRM+RLVR 作为 baseline。

2. **STAT: Skill-Targeted Adaptive Training** (arXiv 2510.10023, ICLR 2026): 使用强 LLM teacher 进行 skill profiling，识别 missing skills，然后 reweight (STAT-Sel) 或合成 (STAT-Syn) 训练数据。在 MATH 上提升 7.5%、OOD benchmark 平均 4.6%。与本 proposal 最核心的竞争关系——STAT 做的事和 FormalLoop 高度同构，区别在于 error diagnosis 来源：LLM teacher vs. formal tools。

3. **NSRSA** (arXiv 2603.21558, March 2026): 使用 SymPy 验证 arithmetic operations 来过滤 self-training 数据，构建 DPO pairs。在 GSM8K + Qwen3-4B 上测试。**这是当前与本 proposal 最接近的工作**——也用 SymPy、也做 iterative self-training、也构建 DPO pairs。但 NSRSA 仅覆盖 arithmetic verification、不做 error categorization、不做 targeted synthesis。本 proposal 的增量：error taxonomy + targeted problem generation + step-localized DPO。

4. **Solver-Verifier Gap Theory** (arXiv 2507.00075, ICLR 2026): 理论建模 self-improvement dynamics，证明 verifier capability 决定 self-improvement ceiling，dynamics 遵循 exponential law。为本 proposal 的动机提供了理论支撑——formal verification 作为 near-perfect verifier 应能提升 ceiling。

5. **Imperfect Verifier** (arXiv 2604.07666, April 2026): 实证发现 noise rate ≤15% 时 RLVR 仍可达到 clean baseline 2% 以内的 accuracy。Precision matters more than recall。这支撑了 proposal 的"precision-coverage tradeoff"假说，但也构成潜在威胁——如果 15% noise 是可容忍的，formal verification 的 near-zero noise 优势可能边际收益递减。

6. **SwS** (arXiv 2506.08989, NeurIPS 2025): 基于 pass-rate 分析识别 weakness，按 category 聚类失败问题后合成新问题。7B/32B 模型在 8 个 benchmark 平均提升 10%/7.7%。与本 proposal 竞争——SwS 不需要 formal verification，仅用 pass-rate 就能做 weakness-driven synthesis，简单得多。

7. **Adaptive Problem Generation** (arXiv 2602.19187, Feb 2026): 在 symbolic space 用 SymPy 做 closed-loop RLVR problem generation，通过 prompt optimization 适配 difficulty。与 FormalLoop 共享"SymPy + closed-loop"元素，但不做 error-type diagnosis。

8. **LEMMA** (arXiv 2503.17439, 2025): 对 LLM 生成的 math solutions 做 fine-grained error categorization (question misinterpretation → calculation error)，用 error-corrective trajectories 训练。LLaMA3-8B 上 13.3% accuracy improvement。**Proposal 未引用此工作**，但 LEMMA 做的 error categorization + targeted training 思路与本 proposal 类似（区别：LEMMA 用 LLM 做 error analysis，本 proposal 用 formal tools）。

**调研总结**: 这个领域正在快速发展，形成了几条平行的研究线：(a) LLM teacher-based skill profiling + targeted training (STAT, Self-Error-Instruct, LEMMA)；(b) pass-rate/outcome-based weakness targeting (SwS)；(c) symbolic verification for data quality/PRM training (FoVer, NSRSA, MATH-VF)；(d) symbolic problem generation (Adaptive Problem Generation, Reasoning Core)。本 proposal 试图桥接 (c) 和 (a)——用 formal tools 替代 LLM teacher 做 error profiling，这个具体交叉点确实尚未被占据，但周围的工作已经非常密集，留给本 proposal 的 novelty space 是"组合型"的而非"开创型"的。


【Trivial Alternative 检验】:

**存在多个成本更低的替代方案：**

1. **SwS-style pass-rate targeting（最大威胁）**：SwS 仅使用 pass-rate 分析就能识别 weakness 并合成 targeted problems，不需要任何 formal verification，在 8 个 benchmark 上取得了 7.7-10% 的提升。FormalLoop 的 formal error profiling 需要 Z3/SymPy formalization pipeline（成功率仅 60-70%），工程复杂度高得多。核心问题是：formal error profiling 提供的 granularity advantage 能否显著超过 pass-rate targeting？

2. **Outcome verification + category oversampling**：用 MATH 已有的 7 个 subcategory labels，对 weak subcategories 做 oversampling。完全不需要 formal verification。Proposal 承认了这个 alternative 并将其作为 baseline，这是好的。但如果 subcategory-level targeting 已经捕获了大部分收益，formal error profiling 的 within-subcategory granularity advantage 可能是边际的。

3. **FoVer-PRM + Best-of-N/RLVR**：利用 FoVer 已训练好的 PRM 做 verification，在标准 self-improvement loop 中使用。不需要自己构建 formalization pipeline。

**增量价值核心**在于：formal error *categorization*（不仅是 verification）+ *targeted synthesis*（不仅是 filtering）。如果 ablation 显示 error categorization → targeted synthesis 的链条中每一步都有显著增量，idea 成立；否则 trivial alternatives 就够了。这是一个需要实验验证的假设，不是逻辑上显然的。


【前提假设检验】:

**核心 claim 的逻辑链条中有 3 个关键假设未经验证：**

1. **Z3/SymPy 能可靠地将 step-level errors 分类到 5-type taxonomy**：Proposal 假设 formal verification 不仅能判定 step 对错，还能将错误归类为 algebraic manipulation / equation solving / arithmetic / constraint reasoning / logical inference。但 Z3/SymPy 的 verification 本质是检查 symbolic expression 的等价性，从 "verification failure" 到 "error type classification" 之间存在 gap。一个 step 可能同时涉及多种操作，formalization failure 也可能被误分类。这个假设是否成立直接决定 pipeline 的核心功能是否可行。

2. **Error-type-level targeting 显著优于 problem-level targeting**：知道"模型在 equation solving 上弱"比知道"模型做错了这道题"能产生多大的额外收益？这取决于 SymPy 合成的 targeted problems 是否真正练到了弱技能，而不仅仅是生成了更多同类题。数学技能之间的可迁移性（或不可迁移性）是一个未经验证的前提。

3. **Precision-coverage tradeoff 假说中 τ ≈ 15% 的适用性**：Imperfect verifier 论文的 15% threshold 是在 RLVR 设定下测得的（reward noise 对 policy optimization 的影响），而 FormalLoop 的设定是 error profiling → targeted synthesis（diagnosis noise 对 data selection 的影响）。这两个设定下 noise tolerance 是否相同是一个未经验证的类比。


【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是将 formal verification 从"verification/filtering tool"提升为"error diagnostician + targeted synthesis driver"，这个具体交叉点确实尚未被占据。NSRSA (arXiv 2603.21558) 最接近但仅做 arithmetic verification 不做 error categorization；STAT (ICLR 2026) 做 skill profiling 但依赖 LLM teacher；SwS (NeurIPS 2025) 做 weakness targeting 但用 pass-rate。FormalLoop 的 step-localized formal DPO 相比 Step-DPO (NeurIPS 2024) 和 NSRSA 的 solution-level DPO 也有实质区别。但这本质上是 **组合型 novelty**——formal verification (from FoVer/MATH-VF) + error profiling (from STAT/LEMMA) + targeted synthesis (from SwS/STAT) + step-localized DPO (from Step-DPO/NSRSA) 的交叉。每个组件都有近期先例。Error profile dynamics 是相对独特的分析贡献，但作为 paper 的核心卖点偏弱。

2. **Significance: 中** — 
   研究问题（teacher-free targeted self-improvement）确实重要且 timely，对应 solver-verifier gap theory (ICLR 2026) 指出的 verifier quality 瓶颈。但**核心发现的方向是可预测的**：ground-truth error diagnosis（formal tools）理应优于 noisy error diagnosis（LLM teacher）——如果结果是 positive，审稿人大概率会说 "I would have guessed this, formal verification gives cleaner signals"。真正 interesting 的是 by how much 以及 error profile dynamics 的 patterns，但这些属于 empirical findings 而非 idea-level surprise。此外，60-70% 的 formalization coverage 限制了方法的 generalizability——只有代数和算术类问题能享受 formal profiling，geometry 和 combinatorics 仍用 fallback。Imperfect verifier 论文 (arXiv 2604.07666) 的 15% tolerance 发现也削弱了 near-zero noise 的边际价值。

3. **Related Work: 强** — 
   这是本 proposal 最突出的优势。Related work 覆盖极为全面，包括直接竞争者 (STAT, SwS, Self-Error-Instruct, WarriorMath)、formal verification 线 (FoVer, MATH-VF, Safe)、理论基础 (solver-verifier gap)、concurrent work (Adaptive Problem Generation, NSRSA, Reasoning Core, Bidirectional Curriculum)、以及 imperfect verifier 研究。对每个 related work 的差异化定位清晰准确。唯一遗漏是 LEMMA (arXiv 2503.17439) 做 fine-grained error categorization + targeted training，思路与本 proposal 类似（LLM-based vs. formal-based）。但整体 related work 质量在 AAAI 投稿中属于上乘。


【概率估计】: [28% - 38%] 中位 33%

【估计理由】: 
Novelty 中等（组合型创新，具体交叉点确实空白但非范式转变）+ Significance 中等（问题重要但核心发现方向可预测、coverage 受限）+ Related Work 强（定位清晰，差异化到位）。Related work 的强覆盖保证了下限（不会因为 "missing important baselines" 被直接拒），但 Novelty 和 Significance 的中等评价限制了上限——审稿人可能认可这是 solid engineering integration work 但质疑 "what's the surprising insight?"。上界主要受 Significance 限制：如果核心结果 positive，审稿人可能评价为 "expected result, well-executed"，这在顶会中通常对应 borderline accept/reject。

【主要风险】: 
1. **"Expected result" 风险**：审稿人可能认为 "formal verification 提供更好的 error diagnosis → 更好的 targeted training" 是一个 obvious hypothesis，positive 结果不够 surprising，从而降低 novelty/significance 评分。
2. **Trivial alternative 威胁**：SwS 的 pass-rate targeting 或 subcategory-level oversampling 已经很强且简单得多。如果 FormalLoop 的 formal error profiling 仅带来边际提升（比如 1-2% accuracy gain），审稿人会质疑 engineering complexity 是否值得——这不是 idea 层面的问题，但会放大"组合型 novelty 不够"的 perception。
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL 2026)](https://arxiv.org/abs/2505.15960)
- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://arxiv.org/abs/2510.10023)
- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)
- [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666)
- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://arxiv.org/abs/2506.08989)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [LEMMA: Learning from Errors for Mathematical Advancement in LLMs](https://arxiv.org/abs/2503.17439)
- [MATH-VF: Step-Wise Formal Verification for LLM-Based Math Problem Solving](https://arxiv.org/abs/2505.20869)
- [Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)


【原始 proposal（允许参考但不是主要依据）】:
# Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement

## Core Problem

Self-improvement loops for mathematical reasoning suffer from model collapse (solver-verifier gap theory, ICLR 2026) and untargeted data waste. All existing error-targeted synthesis methods — STAT (ICLR 2026), Self-Error-Instruct (ACL 2025), SwS (NeurIPS 2025), WarriorMath (arXiv 2025) — depend on LLM teachers or LLM metacognition for error diagnosis, introducing teacher bias, hallucinated attributions, and scalability ceilings. Empirically, LLMs cannot reliably spot mathematical errors even with reference solutions (arXiv 2509.01395, EMNLP 2025). Can formal symbolic tools serve as collapse-proof verifiers and ground-truth error diagnosticians, enabling stable, teacher-free, targeted self-improvement?

## Core Contributions

1. **Teacher-free error-targeted self-improvement**: The first self-improvement system where error diagnosis and targeted synthesis are driven entirely by formal symbolic tools (Z3, SymPy), eliminating LLM teacher dependency. Unlike RLVR/GRPO (also teacher-free), FormalLoop targets specific error types rather than optimizing globally.

2. **Formally-verified step-localized DPO**: Preference pairs where trajectories share k formally-verified-correct steps and diverge at step k+1 — providing step-localized credit assignment with formal guarantees. Unlike Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) which use LLM/human annotations, and unlike NSRSA (arXiv 2026) which constructs solution-level accept/reject pairs, our pairs provide zero-noise step-localized preference signals.

3. **Ground-truth error profile dynamics**: FormalLoop uniquely enables tracking formally-verified per-skill-type error evolution across self-improvement iterations — answering whether error types have fixed reduction priority orderings, whether skill dependencies exist (e.g., arithmetic errors must resolve before algebraic errors become visible), and whether error profile entropy predicts convergence. No prior work provides ground-truth skill-decomposed self-improvement dynamics.

4. **Precision-coverage tradeoff hypothesis**: We hypothesize that in self-improvement loops, there exists a verifier noise threshold τ beyond which expanding coverage yields negative marginal returns. Imperfect verifier research (arXiv 2604.07666, arXiv 2026) estimates τ ≈ 15%; solver-verifier gap theory (ICLR 2026) predicts verifier reliability determines the self-improvement ceiling. FormalLoop tests this: formal verification achieves near-zero noise within its scope (~60-70% of amenable categories), which should outperform full-coverage but noisier LLM diagnosis. We validate via noise injection ablation.

## Why Not Simpler Alternatives?

**vs. Outcome verification + STAT-style LLM teacher profiling**: (1) Error attribution precision — outcome verification doesn't localize errors; LLM step diagnosis hallucinates (arXiv 2509.01395, EMNLP 2025); formal verification provides guaranteed step-level attribution. (2) Iterative stability — LLM teacher biases compound across iterations; formal diagnosis is independently calibrated each round. (3) No teacher ceiling — STAT's profiling quality is bounded by teacher metacognition.

**vs. Subcategory-level outcome targeting** (using MATH's existing 7 subcategory labels to oversample weak categories): This requires no formal verification at all. However, subcategory labels are coarse — within Algebra alone, a model may struggle specifically with equation solving but not algebraic manipulation. Formal step-level diagnosis provides within-subcategory skill decomposition that subcategory-level targeting cannot. We include subcategory-level targeting as an explicit baseline to quantify this granularity advantage.

**vs. FoVer-PRM as verifier in a standard self-improvement loop**: FoVer (ACL 2026) trains PRMs from formal verification data for general use. A natural alternative is using a FoVer-trained PRM as the verifier in a self-improvement loop (via Best-of-N or RLVR). FormalLoop differs by using formal verification directly for error categorization and targeted synthesis — not indirectly through a learned PRM. We include FoVer-PRM + RLVR as a baseline to isolate direct formal profiling's advantage.

## Research Landscape

Current SOTA in synthetic math data: SPARQ (June 2025, +24% via quality-diversity from 7.5K seeds), CoTEvol (April 2026, +6.6% via evolutionary CoT synthesis), MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). Self-improvement: SPICE (Oct 2025, +8.9% via document-grounded self-play), SvS (Aug 2025, +18.3% Pass@32 on AIME24 via variational problem synthesis). Verification: FoVer (ACL 2026) trains PRMs from formal verification across 12 benchmarks; imperfect verifier research (arXiv 2604.07666, arXiv 2026) shows ≤15% noise is tolerable with precision mattering more than recall. Concurrent: Adaptive Problem Generation (arXiv 2602.19187, Feb 2026) uses SymPy in closed-loop RLVR but adapts difficulty globally without error-type diagnosis. SwS (NeurIPS 2025) identifies weaknesses via pass-rate analysis without formal diagnosis. Reasoning Core (March 2026) generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) does step-aware Lean 4 verification in one-shot refinement, not closed-loop. Bidirectional Curriculum (March 2026) dynamically adjusts difficulty without formal verification. NSRSA (arXiv 2026) uses SymPy arithmetic verification for iterative self-training on GSM8K with solution-level DPO, but covers only arithmetic operations without error categorization or targeted synthesis. MATH-VF (arXiv 2025) uses Z3+SymPy for step-wise verification but as a training-free inference tool.

## Proposed Approach

FormalLoop runs iterative cycles on a student model (Qwen3.5-9B primary, Qwen3.5-4B validation): (1) student solves problems, (2) solutions are formalized and verified step-by-step via Z3/SymPy, (3) step-level errors classified into a formal taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), (4) SymPy-based synthesis generates targeted problems exercising weak skills with solver-guaranteed solutions, (5) student trains via SFT+DPO on targeted data and formally-constructed preference pairs, then re-profiled.

**Formal coverage scope**: Formal verification covers algebraic and arithmetic domains amenable to Z3/SymPy (Algebra, Number Theory, Prealgebra, portions of Intermediate Algebra and Precalculus). Geometry and Counting & Probability use outcome-based verification as fallback. Per-category formalization success rates are reported. Even partial coverage with near-zero noise can outperform full-coverage noisy LLM diagnosis (imperfect verifier research, arXiv 2604.07666).

**Formalization quality control**: To prevent conflating formalization failures with reasoning errors: (a) distinguish "verification failed" from "formalization failed" status, (b) exclude solutions where formal rejection co-occurs with correct final answer, (c) use only high-confidence pairs for DPO. Target noise rate well below the 15% tolerance threshold (arXiv 2604.07666).

**DPO pair construction with fallback**: Primary: step-localized pairs (shared k correct steps, diverge at k+1). When step-localized pairs are insufficient (estimated via pilot study yield analysis), mix in solution-level formally-verified pairs (NSRSA-style). Report mixing ratio and its effect on training.

## Experimental Design

**Models**: Qwen3.5-9B (primary, 5 iterations) + Qwen3.5-4B (validation, 3 iterations). Pilot study includes Llama 3.1-8B formalization success rate comparison (not full training loop).

**Benchmarks**: GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench. OOD generalization on AIME24/25. Per-MATH-subcategory breakdown (formally-covered vs. fallback).

**Evaluation protocol**: Greedy accuracy + Pass@K (K=8, 32) + majority voting@K. 3 independent runs, mean ± std, significance tests. Per-problem sampling: 16-32 solutions for DPO pair construction.

**Baseline matrix**:
- Training paradigm: Vanilla SFT (uniform), SFT+DPO (uniform), GRPO/RLVR
- Targeting: SwS (NeurIPS 2025, pass-rate weakness targeting), STAT-style (GPT-4o teacher) profiling + targeted synthesis, subcategory-level outcome targeting
- Symbolic: Adaptive Problem Generation (arXiv 2602.19187, global difficulty adaptation)
- Verification: FoVer-PRM (ACL 2026, github.com/psunlpgroup/FoVer) + Best-of-N/RLVR loop, outcome-only verification loop (NSRSA-style)

**Ablation studies** (priority-ranked; ablations run on Qwen3.5-4B, 2-3 iterations, 3 benchmarks: GSM8K, MATH-500, AIME24):
1. [Must] Error profiling source: Formal vs. LLM-based vs. pass-rate-based vs. subcategory-level vs. random
2. [Must] Preference pair source: Step-localized formal DPO vs. solution-level formal DPO (NSRSA-style) vs. outcome DPO vs. LLM-annotated DPO (Step-DPO style)
3. [Must] Targeting vs. uniform: Targeted synthesis vs. uniform synthesis (same quantity)
4. [Should] Training objective: SFT only vs. DPO only vs. SFT+DPO
5. [Should] Taxonomy granularity: 5-type vs. 2-type (arithmetic/non-arithmetic) vs. single aggregate
6. [Should] Iteration dynamics: Per-iteration accuracy, error profile evolution, formalization coverage, entropy curves
7. [Nice] Precision-coverage tradeoff: Inject artificial noise (5%, 10%, 15%, 20%) into formal labels, measure impact on self-improvement trajectory

**Compute fairness**: Unified metric: total dollar cost (GPU + CPU + API). Report per-method cost breakdown. Compute-matched comparisons: (i) fixed GPU training FLOPs, (ii) fixed total dollar budget. Accuracy vs. total cost curves.

**Pilot study** (before main experiments):
- Per-subcategory formalization success rate on MATH-Train (200-300 problems per subcategory)
- Failure mode analysis: formalization failure vs. solver timeout vs. scope limitation
- Selection bias analysis: compare error type distributions between formalization-success and formalization-failure groups
- DPO pair yield estimation: 500 problems × 16 solutions, count constructable step-localized pairs
- Cross-family comparison: Qwen3.5-9B vs. Llama 3.1-8B formalization success rates
- Taxonomy coverage validation and comparison with STAT's skill taxonomy
- Human evaluation of 100-200 synthesized problems (well-formedness, difficulty, NL quality)

## Key References

- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)
- STAT: Skill-Targeted Adaptive Training (ICLR 2026)
- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)
- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)
- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)
- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)
- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)
- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)
- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)
- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)
- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)
- Adaptive Problem Generation via Symbolic Representations (arXiv 2026, arXiv 2602.19187)
- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026, arXiv 2604.07666)
- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)
- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)
- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)
- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)
- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)
- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)
- Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs (NeurIPS 2024)
- Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning (ACL 2025 Findings)
- LLMs Cannot Spot Math Errors Even When Allowed to Peek into the Solution (EMNLP 2025, arXiv 2509.01395)

## Resource Estimate

- **manual**: gpu_hours: 750 H100 hours (5 iterations 9B + 3 iterations 4B + ablations on 4B + pilot study + evaluation), timeline: 4-5 months, estimated_gpu_cost: $1,875
- **human_in_loop**: gpu_hours: 700 H100 hours, timeline: 3-4 months, claude_api_cost: $500-700 (pipeline code, taxonomy iteration, analysis), teacher_api_cost: $200-400 (GPT-4o for STAT baseline), estimated_gpu_cost: $1,750
- **auto_research**: gpu_hours: 700 H100 hours, timeline: 6-8 weeks, claude_api_cost: $1,500-2,500, teacher_api_cost: $200-400, estimated_gpu_cost: $1,750, speed_bottleneck: Z3/SymPy step verification is CPU-bound (~0.5-2s per step); LLM-to-formal translation ~60-70% success rate on amenable categories requires retry loops

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4b0d2f53-e919-472a-8a36-7257f9bee27b",
  "type": "user",
  "uuid": "9a3de26c-0e4c-44b6-8df9-eae157e84017",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T09:10:03.051Z_

```json
{
  "parentUuid": "9a3de26c-0e4c-44b6-8df9-eae157e84017",
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
  "uuid": "ab86ef3c-f4da-47b3-b2c1-d2af5bbf9a15",
  "timestamp": "2026-05-27T09:10:03.051Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T09:10:03.051Z_

```json
{
  "parentUuid": "ab86ef3c-f4da-47b3-b2c1-d2af5bbf9a15",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "43b30503-c87b-4636-a8ef-56f5db0efe2d",
  "timestamp": "2026-05-27T09:10:03.051Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research material to conduct a thorough…",
  "leafUuid": "43b30503-c87b-4636-a8ef-56f5db0efe2d",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate formal error profiling for math self-improvement",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583"
}
```

---

### Assistant

_source line 8 · 2026-05-27T09:10:27.663Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them according to the Meta Judge format.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [25% - 35%] 中位 29%

**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [25% - 35%] 中位 30%


**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [28% - 38%] 中位 33%

Now I'm calculating the aggregate statistics across all three reviewers. The median probabilities are 29%, 30%, and 33%, which gives me a mean of about 30.67% and a median of 30%. The standard deviation comes out to roughly 1.70%, which indicates fairly tight agreement among the reviewers.

Looking at where the reviewers converge, I see strong consensus across all three on several key dimensions: they all rated novelty and significance as medium, and related work as strong. They're also aligned on NSRSA being the closest competitor, SwS as the main trivial alternative, and the "expected result" risk. There's agreement too on the critical assumptions—the 60-70% formalization success rate and the unverified precision-coverage tradeoff hypothesis. A couple of reviewers flagged concerns about step-localized DPO yield and error taxonomy adequacy.

The outliers are minor: R3 alone caught the LEMMA reference gap, and their upper bound estimate is slightly higher at 38% versus 35%. Given how tightly the reviewers clustered (standard deviation around 1.7%), I should anchor to the median and tighten the range. Since all three converge on the same quality ratings and their probability ranges overlap substantially between 25-38%, I'll center on the overlapping region around 30% as the median estimate, settling on 26-35% as the final interval.

Now I need to pull together the implementation feasibility assessment from the proposal details — computational requirements, timeline, data sources, and any novel contributions around the error analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43b30503-c87b-4636-a8ef-56f5db0efe2d",
  "isSidechain": false,
  "requestId": "req_011CbSp6eDKpfmhoBsuVsAZM",
  "type": "assistant",
  "uuid": "c196b441-45ea-4839-94bf-37f7e582e3ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6iLvuBRgGCFnYA5UkRuei",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19486,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19486,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3152,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 19486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19486
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

_source line 9 · 2026-05-27T09:11:18.496Z_

【阶段】: Meta Judge
【三次中位】: [29%, 30%, 33%]  std=1.7%
【共识维度】:
- **Novelty: 中**（3/3 一致）— 组合型创新，各组件均有明确前驱（FoVer/NSRSA/STAT/SwS/Step-DPO），具体交叉点空白但方向自然、可预测。NSRSA 进一步压缩了 novelty space。
- **Significance: 中**（3/3 一致）— 问题重要且 timely，但核心发现方向高度可预测（"formal verification 更精确 → 更好的 targeted training"），60-70% formalization coverage 限制通用性，Imperfect Verifier 的 15% tolerance 发现削弱 near-zero noise 的边际价值。
- **Related Work: 强**（3/3 一致）— 覆盖极全面，差异化定位清晰准确，引用经验证真实。是 proposal 最突出的优势。
- **"Expected result" 风险**（3/3 一致）— 如果核心实验 positive，审稿人大概率反应为 "I would have guessed this"，surprise factor 低。
- **SwS 作为主要 trivial alternative 威胁**（3/3 一致）— pass-rate targeting 零额外工程成本且已有 7.7-10% 提升，formal profiling 的 marginal gain 是核心实验必须回答的问题。
- **Formalization 成功率 60-70% 的选择偏差风险**（3/3 一致）— 30-40% formalization 失败的 solutions 可能引入系统性偏差，pilot study 设计合理但结论未知。
- **Step-localized DPO yield 担忧**（2/3，R1+R2）— 约束过严可能导致 yield 极低，fallback 到 solution-level pairs 可能使这一贡献沦为概念性。
- **Error taxonomy 5 类是否充分/互斥/穷尽**（3/3 一致）— formal taxonomy 受 Z3/SymPy 能力限制，可能遗漏 problem comprehension / strategy selection 等维度。
- **Precision-coverage tradeoff 假说未经验证**（3/3 一致）— 是核心理论赌注，plausible 但 Imperfect Verifier 论文的 15% threshold 在不同设定下的适用性存疑。

【异常维度】:
- R3 独立发现 **LEMMA (arXiv 2503.17439)** 未被 proposal 引用 — 做 fine-grained error categorization + targeted training，思路与本 proposal 类似（LLM-based vs. formal-based）。仅 1 人提到，但属于有效发现，应在迭代中补充。降权处理：不影响 Related Work 从"强"降级（因为 LEMMA 与 proposal 有清晰的技术路径区分），但建议在修改中明确讨论。
- R1 提到 **Goodhart's Law 间接路径**（模型学会在 formally verifiable 步骤上做得更好但在 non-verifiable 步骤上退化）— 仅 1 人提到，但逻辑成立，属于对"迭代稳定性"claim 的有效质疑。降权处理：不作为致命风险，但值得在 proposal 中 acknowledge。

【最终概率】: [27% - 34%] 中位 30%
【一致性】: 高（std=1.7%，三位审稿人在所有维度上判决完全一致）
【综合理由】:

三位审稿人在所有三个 rubric 维度上达成完全一致（中/中/强），且概率估计高度收敛（29%/30%/33%，std=1.7%）。这是极强的收敛信号，表明评估可信度高。

**中位取 30% 的逻辑**：
- 三个中位数的中位是 30%，std < 3% 属于高一致情形，按规则取中位附近缩窄区间。
- R3 略高（33%）主要因为其上界设在 38%，但 R3 给出的 rubric 判决（中/中/强）与 R1/R2 完全一致，概率差异来自对 error profile dynamics 独立价值的稍高估计。综合后不应被 R3 拉高超出共识。
- 区间缩窄至 [27%-34%]：下界从 R1/R2 的 25% 上调至 27%（Related Work 强保证不会因遗漏被直接拒），上界从 R3 的 38% 下调至 34%（Novelty/Significance 双中限制天花板）。

**核心瓶颈明确**：idea 天花板由 Novelty 决定——"用 formal tools 替代 LLM 做 error diagnosis" 是自然延伸而非 conceptual surprise，NSRSA (2026.03) 已走了一半路。即使实验完美执行，"expected result, well-executed" 在顶会中通常对应 borderline reject 区域。突破 35% 需要 error profile dynamics 产出反直觉的发现（如 skill dependency ordering），但这是不可预测的。

【建议】: 边缘（偏不推荐侧，但有优化空间，值得进入迭代）

【实施评估】:
- **计算资源**: ~700-750 H100 GPU hours（约 $1,750-1,875），包含 5 轮 9B 迭代训练 + 3 轮 4B 验证 + ablation + pilot study + evaluation。Z3/SymPy step verification 是 CPU-bound（~0.5-2s/step），需额外 CPU 集群支持。整体计算需求中等，在学术实验室可行范围内。
- **数据需求**: MATH-Train、GSM8K（公开可得）；AMC23、AIME24/25、Olympiad-Bench、Minerva Math（公开可得）。无需构建新数据集，但 pilot study 需要 200-300 problems/subcategory 的 formalization 测试。
- **人工介入**: Pilot study 中 100-200 道合成题的 human evaluation（well-formedness, difficulty, NL quality）；error taxonomy 的初始设计和验证需要数学领域专家参与；formalization pipeline 的 debugging 需要 formal methods 经验。估计 1-2 人月人工标注/评审工作量。
- **训练需求**: 需要模型训练。主模型 Qwen3.5-9B 做 5 轮迭代（每轮 SFT+DPO），验证模型 Qwen3.5-4B 做 3 轮。Ablation 在 4B 上跑 2-3 轮。每轮训练包含 SFT 和 DPO 两阶段。无需从头预训练，但迭代训练总计算量显著。
- **新 Benchmark**: 不需要构建新 benchmark。使用现有公开 benchmark。但 error profile dynamics 分析框架本身是新贡献，需要设计 per-skill-type error tracking 的评估协议。
- **预估周期**: 手动执行 4-5 个月；借助 AI 辅助编码 6-8 周。主要瓶颈在 Z3/SymPy formalization pipeline 的开发和调试（估计占总周期 30-40%）以及迭代训练的串行等待时间。AAAI 2026 投稿截止前需提前规划。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c196b441-45ea-4839-94bf-37f7e582e3ed",
  "isSidechain": false,
  "requestId": "req_011CbSp6eDKpfmhoBsuVsAZM",
  "type": "assistant",
  "uuid": "652d299f-455e-48da-b830-33f15df1f56a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6iLvuBRgGCFnYA5UkRuei",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19486,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19486,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3152,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 19486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19486
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research material to conduct a thorough…",
  "leafUuid": "652d299f-455e-48da-b830-33f15df1f56a",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate formal error profiling for math self-improvement",
  "sessionId": "1228067e-47cd-4ff5-b219-82d93c755583"
}
```

---
