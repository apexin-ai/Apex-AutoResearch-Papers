# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/e079606a-0e1e-4146-af49-536d0b121d5f.jsonl`
- **Structured JSON:** [`712becd1df3049e2d4ac.json`](../../sessions/71/712becd1df3049e2d4ac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:35:52.585Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:35:52.585Z",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Baumann et al., \"Large Language Model Hacking\" (arXiv:2509.08825, 2025)]: 本 proposal 的核心动机来源。18 LLMs × 37 tasks × 13M labels 的大规模实验，发现 31% 的假设检验结论可被 pipeline 选择翻转。提供了 proposal 所用的公开数据集（MIT license）。Proposal 正确定位：Baumann 诊断了问题但未提供推断框架。\n- [McLaren et al., \"Magic Words or Methodical Work?\" (arXiv:2603.26898, 2026)]: 政治学文本标注中 pipeline 交互效应主导主效应的发现。直接支持 proposal 的核心论点——逐对敏感性检查低估真实不稳定性。Proposal 对该文的引用和定位准确。\n- [Messing, \"Hidden Measurement Error in LLM Pipelines\" (arXiv:2604.11581, 2026)]: TEE-corrected SE，发现 naive SE 小 40-60%。Proposal 准确将其定位为互补工具（TEE 修正单一 pipeline 内的误差，multiverse 评估跨 pipeline 稳健性），且提出将 TEE 作为 specification curve 内每个点的误差估计器——这是一个有价值的整合思路。\n- [Gligorić et al., \"CDI\" (NAACL 2025)] + [Egami et al., \"DSL\" (NeurIPS 2023)] + [Audinet de Pieuchon et al. (EMNLP 2025)]: 单一 pipeline 内的纠偏方法。Proposal 正确指出这些方法解决 pipeline-internal validity 但忽略 pipeline-external robustness，并设计了直接对比实验（robustness × validity 正交性验证）。\n- [Mehrotra et al., \"Multi-Perspective LLM Annotations\" (arXiv:2603.21404, 2026)]: Perspective-Driven Inference 处理主观任务。Proposal 通过 E/N/U Type U 分类吸收此问题，设计合理。\n- [Del Giudice & Gangestad (AMPPS, 2021)]: E/N/U 分类框架原始来源。Proposal 将其适配到 LLM annotation pipeline 是核心方法论贡献。\n- [Auspurg (PNAS 2025)] vs [Ganslmeier & Vlandas (PNAS 2025)]: multiverse 方法论的正反辩论。Proposal 以 LLM annotation 作为 Auspurg 批判的第一个\"正面案例\"，论证 LLM annotation 满足其三个条件——这是一个有深度的认识论贡献。\n- [Krähmer & Young, \"Visualizing Vastness\" (PLOS One 2026)]: 大型 multiverse 可视化方法。Proposal 在 >150 specifications 时补充 multiverse plots，显示对最新文献的跟进。\n- [Carlson & Burbano (SMJ 2026)]: 推荐 3-5 个 model+prompt 组合的非正式敏感性分析。Proposal 将其作为实验基线（ad hoc subsampling），直接量化 principled multiverse 相对于 ad hoc 检查的增量价值。\n\n- 调研总结: LLM annotation 不稳定性在 2025-2026 年被多项独立研究充分记录（Baumann、McLaren、Messing），但现有工作分为两类——\"诊断但不处方\"（diagnostic studies）和\"纠偏但忽略跨 pipeline 稳健性\"（DSL/PPI/CDI）。**没有任何已发表工作将形式化的 multiverse methodology（specification curve analysis + E/N/U 分类 + 联合推断）应用于 LLM annotation pipelines。** Proposal 准确识别并占据了这一空白。\n\n【整体印象】:\n作为审稿人，我的第一反应是**倾向 accept，但有保留意见**。这是一篇方向准确、动机清晰、实验设计异常完备的方法论 proposal。它解决一个已被充分记录的真实问题（LLM annotation pipeline 不稳定性），提出的解决方案有坚实的方法论基础（specification curve analysis + E/N/U 分类），并且用公开数据集大幅降低了执行风险。认识论贡献（回应 Auspurg 批判）增加了学术深度。\n\n然而，核心贡献本质上是将一个已有框架（E/N/U multiverse）适配到一个新领域（LLM annotation），而非提出根本性的新方法。这种\"框架迁移\"虽然做得很好，但 novelty 的天花板有限。最终能否中稿取决于审稿人是看重\"识别并占据了一个真正的空白 + 极其完备的实验设计\"，还是认为\"本质上是应用已有方法论\"。\n\n【核心贡献】:\n1. **方法论贡献**（primary）：将 E/N/U multiverse 分类框架首次适配到 LLM annotation pipeline，配合任务条件规则和 Boba-style DSL 形式化，使 CSS 研究者可以构建有原则的\"可辩护配置空间\"。\n2. **认识论贡献**：论证 LLM annotation pipeline 满足 Auspurg (2025) 提出的穷举 multiverse 合理性三条件（常量 estimand、无经典误设定、可操作的 E/N/U 分类），且通过 Type U 处理主观任务中的 perspectivism 张力——这是 Auspurg-Ganslmeier & Vlandas 辩论中的第一个正面案例。\n3. **实证贡献**：跨 10 个 CSS 任务的稳健性景观图谱，量化哪些 pipeline 维度和交互驱动推断不稳定性，以及 principled multiverse 相对于 ad hoc 检查和 PPI/DSL 纠偏的增量价值。\n\n这些贡献对 CSS 方法论有明确价值。对核心 NLP 社区的价值相对间接——主要体现在\"LLM 评估方法论\"和\"measurement reliability\"方面。\n\n【方法合理性】:\n方法在逻辑上是合理的。Specification curve analysis 是成熟的统计方法论（Simonsohn et al., Nature Human Behaviour, 2020），E/N/U 分类是 multiverse 文献中被广泛引用的框架。将两者结合应用于 LLM annotation pipeline 在概念上自然。\n\n**潜在的更简单替代方案**：\n- Carlson & Burbano 的 3-5 组合非正式敏感性分析确实更简单，但 proposal 通过 ad hoc baseline 实验直接论证了其不足——这是一个很好的设计选择。\n- 简单的 bootstrap / cross-validation 方法可以评估 pipeline 变异性，但不提供 E/N/U 分类带来的\"可辩护空间\"概念和 specification curve 的联合推断。\n- TEE (Messing) 更简单但解决的是不同问题（单一 pipeline 内的误差修正 vs 跨 pipeline 稳健性）。\n\n总体而言，方法的复杂度与问题的复杂度匹配。没有明显的\"用简单方法就能达到同样效果\"的替代方案。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — LLM annotation pipeline 不稳定性已被 Baumann et al. (2025)、McLaren et al. (2026)、Messing (2026) 充分记录，31% 的假设检验可被翻转、交互效应主导主效应、naive SE 低估 40-60%——这是一个有真实影响的方法论问题。现有工作要么只诊断不处方，要么只在单一 pipeline 内纠偏。\"跨 pipeline 稳健性评估\"是一个清晰的、未被解决的空白。问题的重要性、时效性和文献中的缺口都很清晰。\n\n  2. 方法与创新: 【中】 — E/N/U multiverse 分类框架（Del Giudice & Gangestad, AMPPS 2021）和 specification curve analysis（Simonsohn et al., Nature Human Behaviour 2020）均为已有方法论。核心贡献是将两者适配到 LLM annotation domain——虽然适配过程有智慧（任务条件 E/N/U 规则、Type U 处理主观任务、Boba DSL 形式化），但本质是\"框架迁移\"而非\"框架创新\"。认识论贡献（回应 Auspurg 批判的正面案例）增加了深度，但严格来说是一个\"观察\"而非\"方法\"。与 Audinet de Pieuchon et al. (EMNLP 2025) 的 DSL/PPI benchmarking 相比，本 proposal 的技术新颖度在类似水平——都是将已有方法应用到 LLM annotation 场景并做系统性评估。\n\n  3. 实验设计: 【强】 — 这是 proposal 最突出的优势。实验设计极其完备：(a) 使用 Baumann et al. 公开数据集（MIT license），消除数据收集风险；(b) 10 个任务按类型分层选取，假设来自原始研究（避免 researcher degrees of freedom）；(c) 6 模型跨 5 家族 3 规模；(d) 4 类 baselines/comparisons（specification curve + joint inference、ad hoc sensitivity baseline、PPI/DSL comparison、ANOVA variance decomposition + TEE comparison）；(e) 4 项 ablation studies（E/N/U sensitivity、task-conditional constraint、model diversity curve、batch-size）；(f) 预注册 on OSF；(g) pilot phase 验证成本和 batch-size。(h) 甚至考虑了大型 multiverse 的可视化问题（Krähmer & Young 的 multiverse plots）。这种实验设计的完备程度在 proposal 阶段非常少见，本身就是重要加分项。唯一小瑕疵是 ANOVA 中 Medium（仅 Scout）和 Small（仅 Gemma 4）各只有 1 个模型，size-class 对比可能欠动力。\n\n  4. 可行性: 【强】 — 高可行性。(a) 公开数据集已有，无需数据收集；(b) 预算 $1,200-$2,000 合理且有 pilot 验证；(c) 技术栈无重大未知（API 调用 + 统计分析）；(d) 时间线 10-12 周现实；(e) 不需要训练模型；(f) 最大风险是 API 成本超出预算，但 pilot phase 可以早期发现。E/N/U 专家分类的人员招募可能需要一些协调，但 proposal 已将其纳入时间线。\n\n  5. 写作与呈现: 【强】 — Proposal 本身的写作质量极高。文献定位精准（每项工作都有明确的差异化分析），逻辑链清晰（问题→现有方案的不足→机会→方法→实验→贡献），技术细节丰富但不凌乱。E/N/U 分类表格、模型选择表格、实验设计的结构化呈现都很专业。唯一隐忧是实际论文可能面临内容过多的问题——认识论贡献 + 方法论框架 + 大规模实证分析，需要在会议论文的篇幅限制内做取舍。\n\n【概率估计】: [30% - 47%] 中位 38%\n\n【估计理由】:\n上界 47% 的理由：(1) 问题动机极强且时效性好（2025-2026 年多篇独立研究记录了同一问题）；(2) 实验设计在方法论论文中属于极其完备的水平，多个 baseline、ablation、pre-registration、public data 构成了一个几乎无懈可击的实验方案；(3) 认识论贡献（Auspurg 辩论的首个正面案例）增加了学术深度；(4) 执行风险极低。\n\n下界 30% 的理由：(1) 核心方法创新有限——本质是将已有的 E/N/U multiverse 框架和 specification curve analysis 迁移到新领域，没有提出新的统计方法或算法；(2) 研究定位偏 CSS 方法论，可能不是所有 EMNLP 审稿人的兴趣范围；(3) 如果审稿人认为 Carlson & Burbano 的非正式 3-5 组合敏感性分析\"已经足够好\"，则会质疑 principled multiverse 的增量价值；(4) 纯方法论论文在 EMNLP 的接收率通常低于有明确技术突破的论文。\n\n中位 38% 的核心判断：这是一篇方向正确、执行方案极其扎实的方法论研究，但缺乏让审稿人\"眼前一亮\"的核心技术突破。它的竞争力主要来自问题的重要性和实验设计的完备性，而非方法本身的新颖性。在 EMNLP 这样竞争激烈的会议中，这种\"solid but not exciting\"的定位通常处于 borderline 区间。\n\n【主要风险】:\n1. **Novelty 不足被拒**：审稿人可能认为\"将 E/N/U multiverse 应用于 LLM annotation\"本质上是框架迁移，方法论贡献不足以支撑顶会主会论文——尤其如果 reviewer 不认可认识论贡献的价值。\n2. **受众匹配问题**：这篇论文的核心受众是使用 LLM 做标注的 CSS 研究者，而非 NLP/CL 核心社区。如果分配到不熟悉 CSS 方法论辩论（Auspurg vs Ganslmeier & Vlandas）或 multiverse methodology 的审稿人，可能会低估其贡献。建议在投稿时仔细选择 track（如 \"Resources and Evaluation\" 或 \"NLP Applications\"），并在 introduction 中更强调对 NLP 评估方法论的广泛影响。\n\n【实施评估】:\n  - 计算资源: 低。主要是 API 调用（500M-1.2B tokens）+ 标准 CPU 统计分析。无 GPU 训练需求。\n  - 数据需求: 已满足。Baumann et al. 公开数据集（MIT license, 18 LLMs × 37 tasks × 13M labels），无需额外数据收集或人工标注。\n  - 人工介入: 中等。E/N/U 分类需要人类领域专家（~1 周），如招募独立专家面板则需额外 1-2 周协调。\n  - 训练需求: 无。不需要训练或微调任何模型，仅使用 LLM API 进行推断。\n  - 新 Benchmark: 否。使用已有数据集和任务，但产出物（E/N/U 分类规则的 Boba DSL 形式化、robustness classification schema）可作为方法论工具发布。\n  - 预估周期: 10-12 周（pilot 1 周 + annotation 2-3 周 + analysis 2-3 周 + writing 3-4 周，E/N/U 分类并行），API 成本 $1,200-$2,000 + pilot $50-100。总预算约 $1,300-$2,100，时间线在 EMNLP 2026 截稿前可完成。\n```\n\nSources:\n- [Baumann et al., \"Large Language Model Hacking\" (arXiv:2509.08825)](https://arxiv.org/abs/2509.08825)\n- [McLaren et al., \"Magic Words or Methodical Work?\" (arXiv:2603.26898)](https://arxiv.org/abs/2603.26898)\n- [Messing, \"Hidden Measurement Error in LLM Pipelines\" (arXiv:2604.11581)](https://arxiv.org/abs/2604.11581)\n- [Mehrotra et al., \"Multi-Perspective LLM Annotations\" (arXiv:2603.21404)](https://arxiv.org/abs/2603.21404)\n- [Del Giudice & Gangestad, \"A Traveler's Guide to the Multiverse\" (AMPPS, 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Auspurg, \"Robustness is better assessed with a few thoughtful models\" (PNAS, 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Ganslmeier & Vlandas, \"Reply to Auspurg\" (PNAS, 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [Gligorić et al., \"Can Unconfident LLM Annotations Be Used for Confident Conclusions?\" (NAACL 2025)](https://aclanthology.org/2025.naacl-long.179/)\n- [Audinet de Pieuchon et al., \"Benchmarking Debiasing Methods\" (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)\n- [Egami et al., \"DSL\" (NeurIPS 2023)](https://naokiegami.com/paper/dsl.pdf)\n- [Krähmer & Young, \"Visualizing Vastness\" (PLOS One, 2026)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/)\n- [Carlson & Burbano, \"LLMs as Annotators\" (SMJ, 2026)](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)\n- [Variance-Aware LLM Annotation (arXiv:2601.02370)](https://arxiv.org/pdf/2601.02370)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have comprehensive literature coverage. Let me compile the full evaluation.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Baumann et al., arXiv:2509.08825](https://arxiv.org/abs/2509.08825) (2025): 最直接的上游工作——18 LLMs × 37 tasks × 13M labels 的大规模实证研究，量化了 ~31% 的\"LLM hacking\"风险。本 proposal 直接复用其公开数据集（MIT license），并将其诊断性发现延伸为一个推断框架。核心关系：Baumann 诊断问题，本 proposal 提供方法论解决方案。\n- [McLaren et al., arXiv:2603.26898](https://arxiv.org/abs/2603.26898) (2026): 在政治学文本标注中验证了交互效应（model × prompt × learning approach）主导主效应，直接支撑 proposal 的核心论点——逐一敏感性检验不够，需要遍历整个配置空间。\n- [Messing, arXiv:2604.11581](https://arxiv.org/abs/2604.11581) (2026): 提出 TEE-corrected standard errors，解决单管线内的方差低估问题。Proposal 准确定位了其与 TEE 的互补关系：TEE 修正单配置内的推断，multiverse 评估跨配置的稳健性。两者可组合使用。\n- [Variance-Aware LLM Annotation, arXiv:2601.02370](https://arxiv.org/pdf/2601.02370) (2026): 用 G-theory 分解标注精度层面的方差。Proposal 正确区分了标注精度方差 vs. 下游推断方差——这是一个有意义的概念区分。\n- [Egami et al. DSL](https://naokiegami.com/paper/dsl.pdf) (NeurIPS 2023) / [Gligorić et al. CDI](https://aclanthology.org/2025.naacl-long.179/) (NAACL 2025) / [Audinet de Pieuchon et al.](https://aclanthology.org/2025.emnlp-main.1000/) (EMNLP 2025): 三篇构成\"单管线纠偏\"方法线。Proposal 清晰论证了 multiverse 与纠偏方法的正交性（robustness vs. validity），并设计了对比实验。\n- [Mehrotra et al., arXiv:2603.21404](https://arxiv.org/html/2603.21404) (2026): \"Perspective-Driven Inference\" 挑战了主观任务中的\"constant estimand\"假设。Proposal 巧妙地通过 E/N/U 的 Type U 分类吸收了这一张力。\n- [Simonsohn et al.](https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/) (Nature Human Behaviour 2020) / [Del Giudice & Gangestad](https://journals.sagepub.com/doi/10.1177/2515245920954925) (AMPPS 2021): 分别提供 specification curve analysis 和 E/N/U 分类框架——proposal 的两大方法论基础。\n- [Auspurg](https://www.pnas.org/doi/10.1073/pnas.2521917122) (PNAS 2025) vs. [Ganslmeier & Vlandas](https://www.pnas.org/doi/10.1073/pnas.2523374122) (PNAS 2025): multiverse 方法论辩论。Auspurg 批评暴力穷举混入不合理规格。Proposal 的核心认识论贡献正是回应这一批评——论证 LLM 标注管线是少见的满足 Auspurg 三个条件的场景。\n- [Krähmer & Young, \"Visualizing Vastness\"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/) (PLOS One 2026): 提出 multiverse plots 作为大规模 specification curve 的可视化替代方案。Proposal 已计划在 >150 配置时使用。\n\n- **调研总结**: 该领域正处于一个从\"诊断 LLM 标注不稳定性\"向\"提供推断框架\"过渡的关键时刻。诊断性工作（Baumann、McLaren、Messing）已充分建立了问题的紧迫性，纠偏方法（DSL、PPI）解决了单管线内的偏差问题，但**跨管线稳健性的推断框架**确实是一个清晰的空白。我未搜索到任何已有工作将 formal multiverse methodology / specification curve analysis 应用于 LLM 标注管线。这个 gap 是真实的、有价值的。\n\n【整体印象】:\n这是一份极其成熟的 proposal，接近\"可以直接作为论文 introduction + method section 初稿\"的水平。作为审稿人，我的第一反应是\"impressed by the thoroughness\"——文献定位精确、gap 论证充分、实验设计详尽且务实。整体倾向 **weak accept 到 accept**。\n\n核心让我倾向积极评价的因素：(1) 研究 gap 真实存在且论证令人信服；(2) 认识论贡献（LLM 管线满足 Auspurg 条件）是一个genuine intellectual contribution，而非简单的\"方法迁移\"；(3) 实验设计的完备度（pilot → full execution → ablation → baseline comparison）在 proposal 阶段已经非常高；(4) 复用 Baumann 公开数据集大幅降低了执行风险。\n\n让我犹豫的因素：(1) 核心方法（specification curve + E/N/U）均来自既有工作，NLP 社区审稿人可能质疑\"方法论新颖性\"——这是\"将社科方法论应用到 NLP 实践\"而非\"提出新的 NLP 方法\"；(2) 论文最终产出是\"诊断框架+实证发现\"而非可直接使用的工具或算法，可能被部分审稿人视为缺乏可操作性。\n\n【核心贡献】:\n三层贡献结构清晰：\n1. **方法论贡献**（主）: 将 E/N/U multiverse 分类适配到 LLM 标注管线，提出任务条件化的分类准则。这不是简单套用——五个管线维度的 E/N/U 分类需要领域专业知识，且 task-conditional override 机制（如主观任务中 temperature 从 Type U 变为 Type E）是有思想的设计。\n2. **认识论贡献**: 论证 LLM 标注管线是 multiverse analysis 的理想场景——回应了 Auspurg 对 multiverse 方法的根本质疑。这个贡献的价值在于它不仅服务于本文，还为整个 CSS×LLM 社区提供了一个方法论基础。\n3. **实证贡献**: 10 个 CSS 任务的稳健性图谱——哪些发现 robust、哪些 fragile、哪些 sign-inconsistent，以及管线维度的方差分解。\n\n贡献价值：**中高**。对于 CSS×NLP 交叉领域，这是一个及时且必要的工作。但对于纯 NLP 审稿人，可能需要额外说服其研究问题的重要性。\n\n【方法合理性】:\n方法整体合理且设计严谨。具体评估：\n\n1. **E/N/U 分类的适配**: 合理。五个管线维度的选择覆盖了主要的 researcher degrees of freedom。Task-conditional override 不是 ad hoc 的——有清晰的理论基础（如确定性事实任务不需要 temperature 变化）。但分类依赖人类专家判断，引入了主观性——proposal 已通过 reliability protocol（Fleiss' κ + boundary perturbation）部分缓解了这个问题，但 κ 评估仅标记为\"推荐\"而非必做。\n2. **Specification curve + permutation-based joint inference**: 直接采用 Simonsohn et al. (2020) 的标准方法，方法论上无争议。在 cached outputs 上做 permutation（不需要重新调用 API）是一个聪明的设计，大幅降低了计算成本。\n3. **ANOVA 方差分解**: 标准方法，加入 model-size nesting 和 assumption checks（permutation ANOVA / aligned rank transform 作为非参替代）是负责任的统计实践。\n4. **与 PPI/DSL 的比较**: 设计精巧——测试 robustness × validity 的正交性假设。\n\n**是否有更简单的替代方案？** Carlson & Burbano (SMJ 2026) 的 3-5 配置 informal sensitivity analysis 就是更简单的替代方案，但 proposal 已明确论证了其不足（缺乏覆盖保证、无形式化推断、可能错过交互效应），并将其作为 experimental baseline 进行定量比较。这是对\"更简单替代方案\"的正面回应，说服力较强。\n\n**一个潜在问题**: E/N/U 分类的可迁移性——本文的分类准则是为特定的 5 维管线设计的。如果管线增加新维度（如 few-shot examples 的选择、retrieval augmentation），分类准则需要重新制定。但这更像是 future work 而非方法缺陷。\n\n【5 维度打分】:\n\n1. **研究问题: 强** — 问题的紧迫性已被多篇高质量实证工作充分建立（Baumann 的 31% LLM hacking rate、McLaren 的交互效应主导、Messing 的 SE 低估 40-60%）。现有解决方案（DSL/PPI 纠偏、ad hoc sensitivity checks）都只解决了部分问题，formal multiverse framework 的缺失是一个真实的、有价值的 gap。问题定位精准——不是\"LLM 标注不靠谱\"（这已经有人说了），而是\"我们需要一个原则性框架来评估跨管线稳健性\"。\n\n2. **方法与创新: 中偏强** — 方法合理、适配有思想，但核心方法（specification curve analysis、E/N/U 分类）均来自既有工作（Simonsohn 2020、Del Giudice & Gangestad 2021）。创新主要体现在\"适配\"和\"认识论论证\"层面——论证 LLM 管线满足 Auspurg 条件的 dual-layer argument 是一个 genuine intellectual contribution，但从纯技术角度看没有提出新的统计方法或算法。与 Audinet de Pieuchon et al. (EMNLP 2025) 和 Gligorić et al. (NAACL 2025) 相比，本 proposal 的方法论深度是可比的（它们也是将既有统计方法适配到 LLM 标注场景），但 novelty claim 的支撑主要在认识论层面而非技术层面。E/N/U 的 task-conditional 适配和 Boba DSL 形式化是加分项。\n\n3. **实验设计: 强** — 这是 proposal 的最大亮点之一。实验设计的完备度远超同类 proposal：\n   - **数据**: 复用 Baumann et al. 公开数据集，无额外数据收集风险\n   - **任务选择**: 10 tasks stratified across 4 types，预注册在 OSF——消除了\"挑选有利任务\"的质疑\n   - **模型选择**: 6 models × 5 families × 3 scale tiers × open/proprietary，覆盖全面\n   - **Baselines**: (a) ad hoc sensitivity (k=3,5,10, 100 repetitions)——直接定量回应 Carlson & Burbano; (b) PPI/DSL 比较——测试 robustness × validity 正交性; (c) TEE 比较\n   - **Ablations**: E/N/U sensitivity、task-conditional override effect、model diversity curve（含 top/random/bottom stratification）——设计精细且有针对性\n   - **Pilot phase**: 先验证 token 消耗和 batch-size 效应，是负责任的实验实践\n   - **统计严谨性**: permutation-based joint inference (≥500)、ANOVA assumption checks、非参替代方案\n\n4. **可行性: 强** — 这是风险极低的 proposal：\n   - 数据已公开（MIT license），无收集风险\n   - 预算合理（$1,200-$2,000 for full execution），远低于大多数 LLM 实验\n   - 时间线可行（10-12 weeks），有清晰的 milestone\n   - 所有分析在 cached outputs 上进行，后分析阶段成本极低\n   - 不需要训练模型、不需要构建新 benchmark\n   - 唯一不确定性：E/N/U 独立专家评审的协调（1-2 weeks），但即使没有外部专家，boundary-case testing 也能部分替代\n\n5. **写作与呈现: 强** — Proposal 本身的质量极高：\n   - 文献综述结构化、全面、无遗漏（所有核心引用均经我搜索验证为真实论文且描述准确）\n   - 研究 gap 的论证层层推进（诊断工作 → 纠偏方法 → 缺失的 multiverse framework）\n   - 方法论各 stage 之间逻辑连贯\n   - 预期贡献的三层结构（方法论 → 认识论 → 实证）清晰且不overclaim\n   - 表格使用恰当（模型选择表、E/N/U 分类表）增强可读性\n   - 对潜在质疑的预判到位（Auspurg critique、perspectivism tension、ad hoc sensitivity sufficiency）\n\n【概率估计】: [32% - 48%] 中位 40%\n\n【估计理由】:\n**上界 48% 的支撑**: (1) 研究 gap 真实且有价值，已被 2025-2026 的多篇诊断性工作充分铺垫，时机恰好；(2) 实验设计的完备度是顶级的，在 proposal 阶段已接近可执行状态；(3) 认识论贡献（LLM 管线作为 Auspurg 辩论的 positive case study）增加了 intellectual depth，使论文不仅仅是\"方法迁移\"；(4) 可行性极高——公开数据、低预算、无训练需求——大幅降低了执行风险；(5) CSS×NLP 交叉方向在 EMNLP 有成功先例（Gligorić NAACL 2025、Audinet EMNLP 2025、Baumann 的工作方向）。\n\n**下界 32% 的风险**: (1) 核心方法（specification curve + E/N/U）均为既有方法的适配，NLP 审稿人可能判定 novelty 不足——\"没有新算法、新模型、新数据集\"；(2) 论文产出是\"诊断框架+实证图谱\"而非可直接部署的工具，部分审稿人可能质疑 practical impact；(3) E/N/U 分类依赖专家判断，如果 inter-rater agreement 不高，可能动摇方法论基础；(4) 10 tasks × 6 models × ~200 configs 的大规模实验需要大量结果呈现，论文可能面临空间压力（如何在 8 页内清晰呈现 specification curves、ANOVA、ablation 等多层结果）。\n\n**中位 40% 的推理**: 这是一篇定位清晰、执行风险低、intellectual contribution genuine 的方法论论文。它不是\"wow paper\"（没有惊人的新方法或新发现），但它解决了一个真实的、被充分文档化的问题，且解决方式在认识论层面有深度。在 EMNLP 的审稿光谱中，这类论文如果执行到位（实验结果确实展示了 multiverse 的增量价值 vs. ad hoc sensitivity），有相当概率被接收。关键变量是审稿人组成——如果遇到熟悉 CSS 方法论辩论的审稿人，概率可能在 45%+；如果遇到偏 core NLP / model-focused 的审稿人，可能降到 30% 左右。\n\n【主要风险】:\n1. **Novelty 质疑（最大风险）**: 审稿人可能认为\"将 specification curve analysis 应用于 LLM 管线\"是一个 straightforward adaptation，方法论新颖性不足以达到 EMNLP 主会标准。论文需要强调认识论贡献（Auspurg debate response）和 task-conditional E/N/U 设计的独特性来对抗这一质疑。\n2. **结果呈现的空间压力**: 10 tasks × multiple analyses (specification curves, ANOVA, ablation, PPI/DSL comparison) 需要大量图表空间。如何在有限版面内有效传达核心发现，避免\"堆砌结果\"的印象，是写作层面的重大挑战。建议考虑 2-3 tasks 深入展示 + appendix 策略。\n\n【实施评估】:\n  - 计算资源: 极低。所有 LLM 调用通过 API 完成，后分析在标准计算资源上运行（permutation tests <24h）。无 GPU 训练需求。\n  - 数据需求: 已满足。Baumann et al. 公开数据集（MIT license），含 18 LLMs × 37 tasks × 13M labels + gold-standard human annotations。无需额外数据收集。\n  - 人工介入: 中等。E/N/U 分类需要人类领域专家（~1 week）；如招募独立专家 panel 计算 Fleiss' κ，额外 1-2 weeks 协调。预注册在 OSF。\n  - 训练需求: 无。纯 inference + 统计分析。\n  - 新 Benchmark: 无。使用现有 benchmark + 现有数据集。但 E/N/U 分类准则本身可视为方法论工具的贡献。\n  - 预估周期: 10-12 weeks（pilot 1w → annotation 2-3w → analysis 2-3w → writing 3-4w，E/N/U reliability 与 annotation 并行）。周期合理且有余量。API 总成本 $1,300-$2,100（含 pilot）。\n```\n\nSources:\n- [Baumann et al. - Large Language Model Hacking](https://arxiv.org/abs/2509.08825)\n- [McLaren et al. - Magic Words or Methodical Work](https://arxiv.org/abs/2603.26898)\n- [Messing - Hidden Measurement Error in LLM Pipelines](https://arxiv.org/abs/2604.11581)\n- [Variance-Aware LLM Annotation](https://arxiv.org/pdf/2601.02370)\n- [Egami et al. - Design-based Supervised Learning](https://naokiegami.com/paper/dsl.pdf)\n- [Gligorić et al. - Unconfident LLM Annotations](https://aclanthology.org/2025.naacl-long.179/)\n- [Audinet de Pieuchon et al. - Benchmarking Debiasing Methods](https://aclanthology.org/2025.emnlp-main.1000/)\n- [Mehrotra et al. - Multi-Perspective LLM Annotations](https://arxiv.org/html/2603.21404)\n- [Del Giudice & Gangestad - A Traveler's Guide to the Multiverse](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Auspurg - Robustness with Thoughtful Models](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Ganslmeier & Vlandas - Reply to Auspurg](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [Krähmer & Young - Visualizing Vastness](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to make a thorough assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Baumann et al., arXiv:2509.08825] (2025): 最直接的上游工作和数据来源。18 LLMs × 37 tasks × 13M labels 的大规模诊断研究，发现 31% 的假设检验可以通过选择不同 LLM 配置来翻转结论（\"LLM hacking\"）。本 proposal 正是建立在该诊断发现之上，提供推断框架。数据集已公开（MIT license），proposal 直接复用。\n- [McLaren et al., arXiv:2603.26898] (2026): 政治学文本标注中 LLM pipeline 的 interaction effects 研究。核心发现：交互效应 > 主效应，说明逐对敏感性检查不足以捕捉不稳定性。直接支持 proposal \"为何需要完整 multiverse 而非 ad hoc 检查\" 的论点。\n- [Messing, arXiv:2604.11581] (2026): TEE-corrected standard errors，naive SE 偏小 40-60%。定位互补：TEE 修正单一配置下的置信区间，proposal 的 multiverse 提供跨配置鲁棒性。Proposal 计划将 TEE 作为 per-specification 误差估计器嵌入。\n- [Variance-Aware LLM Annotation, arXiv:2601.02370] (2026): G-theory 分解 5 个方差源（construct, interface, model, output, aggregation），12-85pp 偏移。关键区别：G-theory 在标注准确率层面分解方差，proposal 在下游推断层面分解方差——两者未必相关。\n- [Egami et al., NeurIPS 2023] DSL + [Gligorić et al., NAACL 2025] CDI/PPI + [Audinet de Pieuchon et al., EMNLP 2025] benchmark: 单管道校正方法线。DSL/PPI 用小量人工标注校正 LLM 标注偏差，但都假设固定管道配置。Proposal 与之正交：校正解决管道内有效性，multiverse 解决管道间鲁棒性。\n- [Mehrotra et al., arXiv:2603.21404] (2026): Perspective-Driven Inference，主张在主观任务中不同 LLM 视角是合法变异。直接挑战 multiverse 的\"恒定估计量\"假设——proposal 通过 Type U 分类吸收此张力。\n- [Simonsohn et al., Nature Human Behaviour, 2020]: specification curve analysis 方法论基础。\n- [Del Giudice & Gangestad, AMPPS, 2021]: E/N/U 分类框架——proposal 的核心方法论来源。\n- [Auspurg, PNAS 2025] critique + [Ganslmeier & Vlandas, PNAS 2025] reply: multiverse 分析的合理性辩论。Proposal 的认识论贡献直接介入此辩论。\n\n- 调研总结: LLM annotation instability 是一个快速升温的研究方向（2025-2026 密集出现诊断、校正、方差分解工作），但\"formal multiverse methodology applied to LLM annotation pipelines\"这一具体交叉点确实空白——没有搜索到任何现有工作将 specification curve analysis + E/N/U 分类应用于 LLM annotation。Proposal 的 novelty claim 成立。\n\n【整体印象】:\n作为审稿人，第一反应是\"这是一篇思考深度很高、文献定位极其精准的方法论 proposal\"。它识别了一个真实且重要的方法论空白：现有工作要么诊断问题（Baumann, McLaren）、要么修正单管道误差（DSL, PPI）、要么分解方差成分（Messing, G-theory），但没有人提供一个系统性的框架来回答\"我的结论是否依赖于我选择了哪条管道\"。这个问题在 CSS 社区每天都会遇到，但没有标准答案。\n\n核心方法是将心理学/社会科学的成熟方法论（specification curve + E/N/U 分类）迁移到 LLM annotation 这个新领域。这种\"方法迁移\"既是优势（理论基础扎实）也是风险（创新性可能被质疑为\"only applying existing methods\"）。但 proposal 通过认识论论证（LLM annotation 是 Auspurg 条件的第一个正面案例）提升了智识贡献，这不是机械迁移。\n\n实验设计是主要加分项——pilot validation、pre-registration、多层 baseline/ablation、与 PPI/DSL 的正交性检验——完备度远超平均 proposal。\n\n倾向：**weak accept 到 borderline**。如果执行质量高、实证发现有意义（如发现某些管道维度对下游推断的方差贡献远大于预期），可以进入 accept 区间。\n\n【核心贡献】:\n1. **方法论贡献（主要）**: 首次将 E/N/U 分类框架适配到 LLM annotation pipeline，提供从管道维度分类到 specification curve 到联合推断的完整流程。这给 CSS 研究者一个可操作的工具来评估结论鲁棒性。\n2. **认识论贡献**: 论证 LLM annotation 是 Auspurg 批评的第一个正面反例——穷举式 multiverse 在此场景下既有理论正当性又有实践可行性。这对方法论文献有独立价值。\n3. **实证贡献**: 10 个任务的鲁棒性图景、方差分解、ad hoc vs principled multiverse 的定量比较、与 PPI/DSL 的正交性检验。\n\n这些贡献对快速扩张的\"LLM-as-annotator\"社区有实质价值。贡献大小为\"中到强\"——不是范式突破，但填补了一个明确且重要的空白。\n\n【方法合理性】:\n方法整体合理，逻辑链清晰：\n- E/N/U 分类 → 管道空间构建 → specification curve → 联合推断 → 方差分解。每一步都有成熟的方法论支撑。\n- 将 E/N/U 做任务条件化（objective vs subjective）是合理的设计选择，直接回应了 Mehrotra et al. 的透视主义挑战。\n- Boba DSL 的可执行化是好的工程选择，增加可复现性。\n\n**可能的替代方案/简化方案：**\n1. Carlson & Burbano (SMJ 2026) 提出的 3-5 组合 ad hoc 敏感性分析——proposal 已将其作为 baseline 进行定量比较，论证充分。\n2. 直接用 Messing 的 TEE 做全局方差估计——但 TEE 不构建/遍历 multiverse，且不提供 specification-curve-based joint inference，proposal 的互补定位合理。\n3. 纯蒙特卡洛抽样（随机采样管道配置）——但缺乏 principled construction 的理论保证，proposal 通过 ad hoc baseline ablation 实证说明了这一点。\n\n**方法上的潜在弱点：**\n- E/N/U 分类本身引入了研究者自由度（meta-level 讽刺），但 proposal 意识到了这一点并设计了 reliability protocol（boundary-case testing + 独立专家面板）。\n- Permutation-based joint inference 的 500 次置换是否足够？文献中常用 1000+，建议增加。\n- ANOVA 假设在 LLM annotation 数据上可能不成立（非正态、异方差），但 proposal 预见了这一点，提出了 permutation ANOVA 和 aligned rank transform 作为备选。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — \"我的结论是否依赖于 LLM pipeline 的选择\"是一个实际且紧迫的问题。Baumann et al. 的 31% LLM hacking risk 和 McLaren et al. 的交互效应主导发现都直接支持这个问题的重要性。CSS 社区对此有强烈需求但缺乏标准方案。问题定义清晰，研究价值高。\n\n  2. 方法与创新: 【中偏强】 — 核心方法是成熟框架（specification curve + E/N/U）向新领域的迁移，而非全新方法。但迁移并非机械的：(a) 认识论论证（Auspurg 条件的正面案例）增加了智识深度；(b) 任务条件化的 E/N/U 分类是领域特定的创新；(c) 与 PPI/DSL 的正交性框架提供了新视角。引用对比：Messing (2604.11581) 提出 TEE 但不做 multiverse traversal；Baumann et al. (2509.08825) 诊断但不开药方；Audinet de Pieuchon et al. (EMNLP 2025) benchmark 校正方法但在固定管道内——本 proposal 的方法覆盖了这些工作留下的空白。创新性不算开创性但充分且有差异化。\n\n  3. 实验设计: 【强】 — 这是 proposal 最突出的优势。(a) 数据来源低风险（Baumann et al. 公开数据集，MIT license）；(b) 10 个任务跨 4 种类型、6 个模型跨 5 家族 3 规模层级；(c) 多层 baseline（ad hoc k={3,5,10} 抽样 × 100 重复 vs full multiverse）；(d) 与 PPI/DSL 的正交性检验；(e) 4 个精心设计的 ablation（E/N/U 敏感性、任务条件约束、模型多样性曲线、batch-size 效应）；(f) pilot 阶段验证；(g) 预注册。对比领域标准（Audinet de Pieuchon et al. EMNLP 2025 的 benchmark 设计），本 proposal 的实验方案覆盖面更广、ablation 更系统。唯一小缺点：PPI/DSL 比较仅 2-3 个任务，可能不够说服力。\n\n  4. 可行性: 【强】 — (a) 预算合理（$1,200-$2,000，无需 GPU 训练）；(b) 数据已有（无需新数据收集或人工标注）；(c) 时间线可行（10-12 周）；(d) 后标注分析（permutation tests, ANOVA, ablations）全部在缓存输出上操作，成本可忽略；(e) pilot 阶段降低了执行风险。这是一个\"纯分析\"项目，计算资源需求低，最大的执行风险是 API 调用的 token 估算偏差和 E/N/U 专家面板的招募——但都有缓解措施。\n\n  5. 写作与呈现: 【强】 — Proposal 的逻辑结构非常清晰：问题定义 → 文献定位（诊断 / 校正 / 方差分解三条线的空白） → 认识论论证 → 三阶段方法 → 实验设计 → 预期贡献。文献覆盖全面，每个引用都有明确的定位功能（不是堆砌）。E/N/U 分类表格、模型选择表格、维度选项表格都增加了可读性。论证有层次感（epistemological argument → methodological contribution → empirical contribution）。少数可改进点：(a) 对\"为何是这 6 个模型\"的论证可更明确；(b) \"expected contributions\" 可以更突出预期的反直觉发现。\n\n【概率估计】: [33% - 43%] 中位 38%\n\n【估计理由】:\n**上行因素（支持 43%）：** (1) 研究问题紧迫且定义清晰，直接回应 2025-2026 密集出现的 LLM annotation instability 文献；(2) 文献定位极其精准，空白识别可验证（搜索未发现任何现有 specification curve + E/N/U 应用于 LLM annotation 的工作）；(3) 认识论论证增加了智识深度，不是机械的方法迁移；(4) 实验设计完备度远超平均水平，多层 baseline 和 ablation 直接预防了常见审稿质疑；(5) 可行性极高，执行风险低。\n\n**下行因素（拉向 33%）：** (1) \"方法迁移\"的创新性天花板——核心方法（specification curve + E/N/U）来自心理学，审稿人可能认为 intellectual novelty 不足以支撑顶会；(2) 论文可能被感知为\"主要为 CSS 服务的方法论工具\"，NLP 审稿人对其通用性存疑；(3) 实证发现的 upside 不确定——如果所有结论都是\"这个维度重要，那个不重要\"，可能缺乏令人兴奋的发现；(4) E/N/U 分类本身的主观性可能引发审稿质疑，即使有 reliability protocol。\n\n**中位 38% 的理由：** 这是一篇方向正确、执行方案扎实、文献定位优秀的 proposal，在\"整体合格、有实质贡献但需要强执行来弥补创新性天花板\"的区间。在 EMNLP 接收率约 22-24% 的背景下，38% 的估计反映了它\"高于 borderline 但需要实验结果来最终定论\"的位置。如果实证发现揭示了反直觉或高影响力的模式（如某个被广泛使用的管道维度实际上是不稳定性的主要来源），概率可进入 40%+。\n\n【主要风险】:\n1. **\"方法迁移\"创新性质疑**: 审稿人可能认为将心理学的 specification curve + E/N/U 应用到 LLM annotation 只是\"applying existing methods to a new domain\"，intellectual novelty 不足。认识论论证可以部分缓解，但这仍是最可能导致 reject 的单一因素。\n2. **实证发现平淡化**: 如果 10 个任务的结果只是\"有些 robust、有些 fragile、不同维度重要性不同\"而没有更深层的结构性洞察或反直觉发现，论文可能被评为\"technically sound but not sufficiently insightful\"——这在 EMNLP 是常见的 borderline reject 理由。\n\n【实施评估】:\n  - 计算资源: 低。无 GPU 训练需求，仅需 API 调用（$1,200-$2,000）和标准 CPU 后处理。\n  - 数据需求: 已满足。Baumann et al. 公开数据集（MIT license），18 LLMs × 37 tasks × 13M labels。无需新数据收集。\n  - 人工介入: 中等。E/N/U 分类需人工专家（~1 周），可选的独立专家面板（额外 1-2 周）。下游假设使用原始研究的预设假设，无需新假设构造。\n  - 训练需求: 无。纯推理/分析项目，不涉及模型训练或微调。\n  - 新 Benchmark: 否。不构建新 benchmark，但产出可复用的 E/N/U 分类 rubric 和 Boba DSL 规则。\n  - 预估周期: 10-12 周（pilot 1 周 + annotation 2-3 周 + 分析/ablation 2-3 周 + 写作 3-4 周，E/N/U reliability 与 annotation 并行）。\n```\n\nSources:\n- [Baumann et al. - Large Language Model Hacking](https://arxiv.org/abs/2509.08825)\n- [McLaren et al. - Magic Words or Methodical Work?](https://arxiv.org/abs/2603.26898)\n- [Messing - Hidden Measurement Error in LLM Pipelines](https://arxiv.org/abs/2604.11581)\n- [Variance-Aware LLM Annotation](https://arxiv.org/abs/2601.02370)\n- [Mehrotra et al. - Multi-Perspective LLM Annotations](https://arxiv.org/abs/2603.21404)\n- [Egami et al. - Design-based Supervised Learning (DSL)](https://arxiv.org/abs/2306.04746)\n- [Gligorić et al. - CDI/PPI (NAACL 2025)](https://aclanthology.org/2025.naacl-long.179/)\n- [Audinet de Pieuchon et al. - Benchmarking Debiasing Methods (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)\n- [Del Giudice & Gangestad - A Traveler's Guide to the Multiverse (AMPPS 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Auspurg - Robustness is better assessed with a few thoughtful models (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Ganslmeier & Vlandas - Reply to Auspurg (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [Krähmer & Young - Visualizing Vastness (PLOS One 2026)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science\n\n### Motivation\n\nLLM-based text annotation has become the default measurement instrument in computational social science (CSS), yet the pipeline involves numerous researcher degrees of freedom—model selection, prompt template, temperature, system instruction, output parsing—each capable of shifting substantive conclusions. Baumann et al. (arXiv:2509.08825, 2025) document a 31% \"LLM hacking\" risk across 18 LLMs × 37 tasks × 13M labels: for nearly one-third of hypothesis tests, a researcher can find a pipeline configuration that reverses the statistical conclusion. McLaren et al. (arXiv:2603.26898, 2026) show that interaction effects among pipeline dimensions dominate main effects, meaning pairwise sensitivity checks underestimate true instability. Messing (arXiv:2604.11581, 2026) demonstrates that naive standard errors in LLM pipelines are 40–60% smaller than TEE-corrected standard errors that account for prompt, temperature, and judge-model variance. Kosch & Feger (CACM 2026) label this phenomenon \"prompt-hacking\"—the LLM analogue of p-hacking—but offer no formal remedy.\n\nThe methodological status quo offers two partial responses. Diagnostic studies (Baumann et al. 2025; McLaren et al. 2026; arXiv:2601.02370, 2026) quantify instability but prescribe no inferential framework. Statistical correction methods—DSL (Egami et al., NeurIPS 2023), PPI/CDI (Gligorić et al., NAACL 2025), benchmarked by Audinet de Pieuchon et al. (EMNLP 2025)—use small human-label sets to debias LLM annotations within a single chosen pipeline. These corrections answer \"given my pipeline choice, how do I get an unbiased estimate?\" but cannot answer the logically prior question: \"does my conclusion depend on which pipeline I chose?\" No existing work applies formal multiverse methodology—specification curve analysis with principled multiverse construction and joint statistical inference—to LLM annotation pipelines.\n\n### Research Landscape\n\n**Diagnostic work.** Baumann et al. (arXiv:2509.08825) provide the largest controlled study of LLM annotation instability (18 models, 37 tasks, 21 mitigation strategies). McLaren et al. (arXiv:2603.26898) extend this to interaction effects in political science annotation. The Variance-Aware LLM Annotation framework (arXiv:2601.02370, 2026) uses generalizability theory (G-theory) to decompose five variance sources (construct, interface, model, output, aggregation), reporting 12–85 pp outcome shifts from minor design choices. Crucially, G-theory decomposes variance at the annotation-accuracy level (how much does label quality vary?), whereas our ANOVA decomposes variance at the downstream-inference level (how much does the substantive conclusion vary?)—these need not correlate, as systematically biased but directionally consistent annotations may yield stable conclusions despite poor accuracy.\n\n**Measurement error correction.** Messing (arXiv:2604.11581, 2026) decomposes LLM pipeline uncertainty into variance components and proposes TEE-corrected standard errors. TEE corrects the confidence interval around a single estimate within a design-study projection paradigm, but does not construct or traverse a multiverse of defensible configurations, classify pipeline dimensions, or provide specification-curve-based joint inference. Our framework is complementary: Messing's TEE can serve as the per-specification error estimator within each point on our specification curve, while our framework provides the global robustness assessment that TEE alone cannot deliver.\n\n**Single-pipeline correction.** DSL (Egami et al., NeurIPS 2023) uses small human-label sets to debias LLM annotations for downstream inference; CDI (Gligorić et al., NAACL 2025) combines LLM confidence scores with human labels; Audinet de Pieuchon et al. (EMNLP 2025) benchmark DSL vs PPI across annotation budgets. All assume a fixed pipeline configuration—they solve pipeline-internal error but are blind to pipeline-external robustness. Multiverse analysis and correction methods address orthogonal dimensions of annotation credibility: robustness (does the conclusion hold across defensible pipelines?) and validity (is the conclusion correct within a given pipeline?). A finding can be robust yet invalid (all pipelines share the same systematic bias) or fragile yet valid in specific configurations. This orthogonality motivates our comparative evaluation with PPI/DSL.\n\n**Perspectivism.** Mehrotra et al. (arXiv:2603.21404, 2026) propose Perspective-Driven Inference for subjective annotation tasks, treating different LLM perspectives as legitimate viewpoints. This directly challenges the \"constant estimand\" assumption for subjective tasks—a tension we address through our dual-layer epistemological argument (see Opportunity section).\n\n**Multiverse methodology.** Simonsohn et al. (Nature Human Behaviour, 2020) formalize specification curve analysis: enumerate justified specifications, visualize the distribution of effects, and conduct permutation-based joint inference. Del Giudice & Gangestad (AMPPS, 2021) propose the E/N/U classification—Type E (equivalent: defensible alternatives expanding the multiverse), Type N (nonequivalent: one option clearly superior, fixed), Type U (uncertain: run separate sub-multiverses)—to discipline which specifications enter the multiverse. Auspurg (PNAS 2025) critiques brute-force multiverse for mixing justified and unjustified models; Ganslmeier & Vlandas (PNAS 2025) reply that what counts as \"justified\" is itself contested. Carlson & Burbano (SMJ 2026) recommend informal sensitivity analysis (3–5 model+prompt combinations) as practical guidance. Krähmer & Young (\"Visualizing Vastness,\" PLOS One 2026) identify interpretability limits of specification curves in large multiverses and propose multiverse plots as an alternative visualization.\n\n### Opportunity and Core Argument\n\n**LLM annotation as an epistemically ideal setting for multiverse analysis.** Auspurg's (PNAS 2025) critique of multiverse analysis—that it conflates justified and unjustified specifications—rests on three conditions rarely satisfied in social science: (a) constant estimand across specifications, (b) no classical misspecification, (c) principled basis for classifying defensible specifications. We argue that LLM annotation pipelines satisfy these conditions, establishing the first positive case for principled exhaustive multiverse enumeration:\n\n- **(a) Constant estimand—with a task-type-dependent nuance.** For objective/factual tasks (NER, factual binary classification), all pipeline configurations target the same annotation label for the same text—the estimand is defined by the coding scheme, not the model. However, for subjective tasks (toxicity, sentiment intensity, stance), Mehrotra et al. (arXiv:2603.21404, 2026) argue that different LLM \"perspectives\" may constitute legitimate construct variation, not mere measurement error. We resolve this tension through the E/N/U framework itself: for objective tasks, pipeline dimensions like model choice are Type E (equivalent alternatives targeting the same estimand); for subjective tasks, dimensions that may alter the construct (e.g., model family, temperature for stochastic perspective sampling) are classified as Type U, triggering separate sub-multiverses that each maintain a constant estimand. The E/N/U framework thus provides a task-adaptive mechanism for handling the constant-estimand condition—rather than assuming it universally holds or universally fails, it lets the classification absorb the objective/subjective distinction at the operationalization level.\n- **(b) No misspecification in the classical sense.** Each pipeline configuration is a deterministic (or stochastic with known seed) mapping from text to label—no omitted-variable bias or functional-form misspecification, only measurement quality variation.\n- **(c) Principled E/N/U classification is feasible.** Pipeline dimensions have well-defined semantics (model architecture, prompt verbosity, temperature value) with clear task-conditional constraints that make E/N/U classification less contested than in regression multiverse. E/N/U classification is performed by human domain experts (not LLM-assisted) to avoid circularity.\n\nThis epistemological argument is a core intellectual contribution: it demonstrates that the Auspurg critique, while valid for many social science applications, does not apply to LLM annotation (with appropriate task-type-dependent handling), establishing the first setting where exhaustive multiverse enumeration is both theoretically justified and practically feasible.\n\n**Why principled multiverse, not ad hoc sensitivity checks?** Carlson & Burbano (SMJ 2026) recommend 3–5 model+prompt combinations as informal sensitivity analysis. This is insufficient because: (1) ad hoc selection may cluster in a narrow region of the specification space, missing interactions that reverse conclusions (McLaren et al. 2026); (2) without principled construction of the defensible space, there is no basis for claiming coverage; (3) ad hoc checks provide no formal joint inference. We quantitatively validate this argument by comparing ad hoc subsampling (k={3,5,10} random configurations, 100 repetitions) against full-multiverse robustness classifications as an experimental baseline.\n\n### Approach\n\n**Stage 1: E/N/U Multiverse Construction (Primary Methodological Contribution)**\n\nAdapt Del Giudice & Gangestad's (AMPPS, 2021) E/N/U classification to LLM annotation pipeline dimensions. Five dimensions, each with task-conditional rules:\n\n| Dimension | Options | Default | Task-conditional overrides |\n|-----------|---------|---------|---------------------------|\n| Model | 6 (see below) | Type E | — |\n| Prompt template | 3 (minimal / instructed / CoT) | Type E | Simple binary tasks: CoT → Type N |\n| Temperature | {0, 0.3, 0.7} | Type U | Deterministic factual tasks: temp=0 → Type N; Subjective tasks: all → Type E |\n| System instruction | {generic, domain-specific, none} | Type E | — |\n| Output parsing | {regex, structured JSON, first-token} | Type E | Free-form tasks → Type U |\n\nNaïve Cartesian product: 6 × 3 × 3 × 3 × 3 = 486 per model subset, ~810 total. After E/N/U pruning: ~90–270 configurations per task. Classification criteria formalized in a Boba-style DSL (Liu et al., CHI 2021) as executable, reproducible rules.\n\n**E/N/U classification rubric:**\n- **Type E**: Multiple options defensible with no prior evidence favoring one for the given task type.\n- **Type N**: One option clearly superior based on prior evidence or theoretical argument.\n- **Type U**: Genuine uncertainty about whether options target the same construct; triggers separate sub-multiverses.\n\n**E/N/U reliability protocol:** (1) Systematic boundary-case testing: for all E/N/U decisions at classification boundaries (e.g., CoT for binary tasks: N or E? Temperature for subjective tasks: E or U?), perturb the classification and measure downstream robustness impact. (2) Recommended: invite 2–3 independent CSS researchers to independently classify all dimensions for all tasks, compute inter-rater agreement (Fleiss' κ), and run sensitivity analysis on disagreement points.\n\n**Stage 2: Specification Curve Analysis + Joint Inference**\n\nFor each task, execute all configurations in the pruned multiverse across all 6 models. For each configuration, compute the downstream hypothesis test on the annotated data. Apply specification curve methodology (Simonsohn et al., Nature Human Behaviour, 2020):\n\n1. Rank specifications by effect size; visualize as specification curve. For tasks with >150 specifications, supplement with multiverse plots (Krähmer & Young, PLOS One 2026) and pipeline-dimension color/shape encoding for interpretability.\n2. Classify each hypothesis as **robust** (sign-consistent and jointly significant), **fragile** (sign-consistent but not jointly significant), or **sign-inconsistent**.\n3. Permutation-based joint inference (≥500 permutations): shuffle the mapping between pipeline dimensions and annotations, re-compute specification curves, derive joint p-value. Permutations operate on cached annotation outputs—no re-annotation required.\n\n**Stage 3: Variance Decomposition**\n\nFactorial ANOVA over the full-factorial results, quantifying each pipeline dimension's main effect and interactions on downstream inference instability. Model nested within model-size class (large: >250B total params; medium: ~110B; small: <30B) to disentangle scale from family effects. Report main effects, all two-way interactions, and the top-5 highest-variance three-way interactions. Effect sizes reported as η² (or ω² for unbalanced cells). ANOVA assumptions (normality, homoscedasticity) verified; if violated, use permutation-based ANOVA or aligned rank transform as nonparametric alternative. Compare downstream-inference variance decomposition with Messing-style (arXiv:2604.11581) TEE annotation-accuracy decomposition on the same configurations, testing whether annotation-accuracy variance predicts inference instability.\n\n### Experimental Design\n\n**Data source.** Baumann et al. (arXiv:2509.08825) public dataset (MIT license): 18 LLMs × 37 tasks × 13M labels with gold-standard human annotations.\n\n**Task selection.** 10 tasks from Baumann's 37, stratified across: binary classification (3), multi-class classification (3), ordinal rating (2), subjective/contested (2). Selection criteria: (i) gold labels available, (ii) sample size ≥1,000, (iii) downstream hypothesis drawn from the original published study associated with the task in Baumann et al.'s dataset (the 37 tasks originate from 21 published social science studies, each with pre-existing research hypotheses). Using original hypotheses avoids researcher degrees of freedom. Task selection and hypotheses pre-registered on OSF before any annotation execution.\n\n**Models.** 6 models spanning 5 families, 3 scale tiers, and open/proprietary divide:\n\n| Model | Family | Architecture | Total params | Active params | Access |\n|-------|--------|-------------|-------------|--------------|--------|\n| Llama 4 Maverick | Meta | MoE | 400B | 17B | Open (Llama license) |\n| Qwen 3.5 | Alibaba | MoE | 397B | 17B | Open (Apache 2.0) |\n| Llama 4 Scout | Meta | MoE | 109B | 17B | Open (Llama license) |\n| Gemma 4 | Google | MoE | 26B | — | Open |\n| GPT-4o | OpenAI | Proprietary | — | — | API |\n| Claude 3.5 Sonnet | Anthropic | Proprietary | — | — | API |\n\nModel-size classes for ANOVA: Large (Maverick, Qwen 3.5, GPT-4o, Claude 3.5 Sonnet), Medium (Scout), Small (Gemma 4). E/N/U classification is human expert–only, so no circularity from including Claude.\n\n**Pilot phase (prerequisite, ~$50–100).** Before full execution: (1) Run 2 tasks × 2 models to validate token consumption estimates. (2) Batch-size validation: compare batch=1 vs batch=10 vs batch=25 on these tasks, including position-effect analysis (accuracy by item position within batch). If batch=25 degrades accuracy >3pp vs batch=1, fall back to smaller batch. Literature suggests batch=25 is within safe range (BatchPrompt, ICLR 2024: 6/8 models stable through batch=100), but task-specific validation is prudent.\n\n**Full execution.** Full-factorial execution of pruned multiverse per task across 6 models. Batched prompts (size determined by pilot). Estimated total: 500M–1.2B tokens, $1,200–$2,000 (Qwen 3.5 and Llama models via OpenRouter; GPT-4o via OpenAI API; Claude via Anthropic API).\n\n**Evaluation and baselines.**\n1. *Specification curve + joint inference*: For each of 10 tasks, produce specification curves (+ multiverse plots for large multiverses), classify hypotheses as robust/fragile/sign-inconsistent.\n2. *Ad hoc sensitivity baseline*: For each task, randomly sample k={3, 5, 10} configurations (100 repetitions each), compute robustness classification, and report agreement rate with full-multiverse conclusion. This quantifies the incremental value of principled multiverse over informal sensitivity checks. No additional API cost (uses cached annotations).\n3. *PPI/DSL comparison*: On 2–3 representative tasks, run PPI (Gligorić et al., NAACL 2025) and DSL (Egami et al., NeurIPS 2023) using gold labels from Baumann et al. as human-annotation budget. Compare: when multiverse says \"robust,\" does corrected inference agree? When multiverse says \"fragile,\" can correction resolve the fragility? This tests the robustness × validity orthogonality—whether pipeline-external robustness and pipeline-internal validity are indeed independent dimensions.\n4. *Variance decomposition*: Factorial ANOVA with model-size nesting, assumption checks, effect sizes, and TEE comparison (see Stage 3).\n\n**Ablation studies** (on 2–3 representative tasks):\n1. *E/N/U sensitivity analysis*: (a) Perturb boundary E/N/U decisions and compare resulting specification curves and robustness classifications. (b) Compare principled (pruned) multiverse vs naïve (full Cartesian) multiverse to quantify pruning impact. Directly addresses Auspurg (PNAS 2025) critique with empirical evidence.\n2. *Task-conditional constraint effect*: Remove task-type-specific overrides; measure change in specification curve and robustness classification.\n3. *Model diversity curve*: Compute robustness using 6 → 3 → 1 models; additionally stratify as top-3-performing vs random-3 vs bottom-3 to separate model-count effect from model-quality effect. Report as stratified specification curves by model-size class (large-only vs full).\n4. *Batch-size effect*: Results from pilot phase reported as validation evidence.\n\n### Expected Contributions\n\n1. **Methodological (primary):** The first adaptation of E/N/U multiverse classification (Del Giudice & Gangestad, AMPPS 2021) to LLM annotation pipelines, with a task-conditional classification rubric formalized in executable DSL (Liu et al., CHI 2021), enabling principled construction of the defensible configuration space.\n2. **Epistemological:** A dual-layer argument that LLM annotation pipelines satisfy Auspurg's (PNAS 2025) conditions for justified exhaustive multiverse analysis—fully for objective tasks, and via E/N/U Type U classification for subjective tasks where the constant-estimand condition is modulated by perspectivism (Mehrotra et al., arXiv:2603.21404). This provides the first positive case study in the Auspurg–Ganslmeier & Vlandas (PNAS 2025) debate.\n3. **Empirical:** A robustness landscape across 10 CSS tasks: which findings are robust/fragile/sign-inconsistent, which pipeline dimensions and interactions drive instability, how principled multiverse compares with ad hoc sensitivity checks and PPI/DSL correction, and whether annotation-accuracy variance (Messing-style TEE; arXiv:2604.11581) predicts inference instability.\n\n### Budget and Feasibility\n\n- **Pilot phase:** $50–100, ~1 week. Validates token estimates and batch-size effects.\n- **Full annotation:** $1,200–$2,000 (6 models × 10 tasks × 90–270 configs × 1,000–3,000 samples; batched prompts). ~2–3 weeks, parallelized across model APIs.\n- **Post-annotation analysis:** Permutation tests (≥500), ANOVA, ablations, ad hoc baseline simulations, PPI/DSL runs—all operate on cached outputs. <24 hours on standard compute.\n- **E/N/U reliability:** Human expert classification (~1 week); if independent expert panel recruited, additional 1–2 weeks for coordination.\n- **Data:** Baumann et al. public dataset (MIT license). No additional data collection or human annotation required.\n- **Total timeline:** ~10–12 weeks to submission-ready manuscript (pilot: 1 week; annotation: 2–3 weeks; analysis + ablations: 2–3 weeks; writing: 3–4 weeks; E/N/U reliability: parallel with annotation)."
}
````

---

### Runtime record

_source line 2 · 2026-05-20T04:35:52.589Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:35:52.589Z",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T04:35:52.602Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Baumann et al., "Large Language Model Hacking" (arXiv:2509.08825, 2025)]: 本 proposal 的核心动机来源。18 LLMs × 37 tasks × 13M labels 的大规模实验，发现 31% 的假设检验结论可被 pipeline 选择翻转。提供了 proposal 所用的公开数据集（MIT license）。Proposal 正确定位：Baumann 诊断了问题但未提供推断框架。
- [McLaren et al., "Magic Words or Methodical Work?" (arXiv:2603.26898, 2026)]: 政治学文本标注中 pipeline 交互效应主导主效应的发现。直接支持 proposal 的核心论点——逐对敏感性检查低估真实不稳定性。Proposal 对该文的引用和定位准确。
- [Messing, "Hidden Measurement Error in LLM Pipelines" (arXiv:2604.11581, 2026)]: TEE-corrected SE，发现 naive SE 小 40-60%。Proposal 准确将其定位为互补工具（TEE 修正单一 pipeline 内的误差，multiverse 评估跨 pipeline 稳健性），且提出将 TEE 作为 specification curve 内每个点的误差估计器——这是一个有价值的整合思路。
- [Gligorić et al., "CDI" (NAACL 2025)] + [Egami et al., "DSL" (NeurIPS 2023)] + [Audinet de Pieuchon et al. (EMNLP 2025)]: 单一 pipeline 内的纠偏方法。Proposal 正确指出这些方法解决 pipeline-internal validity 但忽略 pipeline-external robustness，并设计了直接对比实验（robustness × validity 正交性验证）。
- [Mehrotra et al., "Multi-Perspective LLM Annotations" (arXiv:2603.21404, 2026)]: Perspective-Driven Inference 处理主观任务。Proposal 通过 E/N/U Type U 分类吸收此问题，设计合理。
- [Del Giudice & Gangestad (AMPPS, 2021)]: E/N/U 分类框架原始来源。Proposal 将其适配到 LLM annotation pipeline 是核心方法论贡献。
- [Auspurg (PNAS 2025)] vs [Ganslmeier & Vlandas (PNAS 2025)]: multiverse 方法论的正反辩论。Proposal 以 LLM annotation 作为 Auspurg 批判的第一个"正面案例"，论证 LLM annotation 满足其三个条件——这是一个有深度的认识论贡献。
- [Krähmer & Young, "Visualizing Vastness" (PLOS One 2026)]: 大型 multiverse 可视化方法。Proposal 在 >150 specifications 时补充 multiverse plots，显示对最新文献的跟进。
- [Carlson & Burbano (SMJ 2026)]: 推荐 3-5 个 model+prompt 组合的非正式敏感性分析。Proposal 将其作为实验基线（ad hoc subsampling），直接量化 principled multiverse 相对于 ad hoc 检查的增量价值。

- 调研总结: LLM annotation 不稳定性在 2025-2026 年被多项独立研究充分记录（Baumann、McLaren、Messing），但现有工作分为两类——"诊断但不处方"（diagnostic studies）和"纠偏但忽略跨 pipeline 稳健性"（DSL/PPI/CDI）。**没有任何已发表工作将形式化的 multiverse methodology（specification curve analysis + E/N/U 分类 + 联合推断）应用于 LLM annotation pipelines。** Proposal 准确识别并占据了这一空白。

【整体印象】:
作为审稿人，我的第一反应是**倾向 accept，但有保留意见**。这是一篇方向准确、动机清晰、实验设计异常完备的方法论 proposal。它解决一个已被充分记录的真实问题（LLM annotation pipeline 不稳定性），提出的解决方案有坚实的方法论基础（specification curve analysis + E/N/U 分类），并且用公开数据集大幅降低了执行风险。认识论贡献（回应 Auspurg 批判）增加了学术深度。

然而，核心贡献本质上是将一个已有框架（E/N/U multiverse）适配到一个新领域（LLM annotation），而非提出根本性的新方法。这种"框架迁移"虽然做得很好，但 novelty 的天花板有限。最终能否中稿取决于审稿人是看重"识别并占据了一个真正的空白 + 极其完备的实验设计"，还是认为"本质上是应用已有方法论"。

【核心贡献】:
1. **方法论贡献**（primary）：将 E/N/U multiverse 分类框架首次适配到 LLM annotation pipeline，配合任务条件规则和 Boba-style DSL 形式化，使 CSS 研究者可以构建有原则的"可辩护配置空间"。
2. **认识论贡献**：论证 LLM annotation pipeline 满足 Auspurg (2025) 提出的穷举 multiverse 合理性三条件（常量 estimand、无经典误设定、可操作的 E/N/U 分类），且通过 Type U 处理主观任务中的 perspectivism 张力——这是 Auspurg-Ganslmeier & Vlandas 辩论中的第一个正面案例。
3. **实证贡献**：跨 10 个 CSS 任务的稳健性景观图谱，量化哪些 pipeline 维度和交互驱动推断不稳定性，以及 principled multiverse 相对于 ad hoc 检查和 PPI/DSL 纠偏的增量价值。

这些贡献对 CSS 方法论有明确价值。对核心 NLP 社区的价值相对间接——主要体现在"LLM 评估方法论"和"measurement reliability"方面。

【方法合理性】:
方法在逻辑上是合理的。Specification curve analysis 是成熟的统计方法论（Simonsohn et al., Nature Human Behaviour, 2020），E/N/U 分类是 multiverse 文献中被广泛引用的框架。将两者结合应用于 LLM annotation pipeline 在概念上自然。

**潜在的更简单替代方案**：
- Carlson & Burbano 的 3-5 组合非正式敏感性分析确实更简单，但 proposal 通过 ad hoc baseline 实验直接论证了其不足——这是一个很好的设计选择。
- 简单的 bootstrap / cross-validation 方法可以评估 pipeline 变异性，但不提供 E/N/U 分类带来的"可辩护空间"概念和 specification curve 的联合推断。
- TEE (Messing) 更简单但解决的是不同问题（单一 pipeline 内的误差修正 vs 跨 pipeline 稳健性）。

总体而言，方法的复杂度与问题的复杂度匹配。没有明显的"用简单方法就能达到同样效果"的替代方案。

【5 维度打分】:
  1. 研究问题: 【强】 — LLM annotation pipeline 不稳定性已被 Baumann et al. (2025)、McLaren et al. (2026)、Messing (2026) 充分记录，31% 的假设检验可被翻转、交互效应主导主效应、naive SE 低估 40-60%——这是一个有真实影响的方法论问题。现有工作要么只诊断不处方，要么只在单一 pipeline 内纠偏。"跨 pipeline 稳健性评估"是一个清晰的、未被解决的空白。问题的重要性、时效性和文献中的缺口都很清晰。

  2. 方法与创新: 【中】 — E/N/U multiverse 分类框架（Del Giudice & Gangestad, AMPPS 2021）和 specification curve analysis（Simonsohn et al., Nature Human Behaviour 2020）均为已有方法论。核心贡献是将两者适配到 LLM annotation domain——虽然适配过程有智慧（任务条件 E/N/U 规则、Type U 处理主观任务、Boba DSL 形式化），但本质是"框架迁移"而非"框架创新"。认识论贡献（回应 Auspurg 批判的正面案例）增加了深度，但严格来说是一个"观察"而非"方法"。与 Audinet de Pieuchon et al. (EMNLP 2025) 的 DSL/PPI benchmarking 相比，本 proposal 的技术新颖度在类似水平——都是将已有方法应用到 LLM annotation 场景并做系统性评估。

  3. 实验设计: 【强】 — 这是 proposal 最突出的优势。实验设计极其完备：(a) 使用 Baumann et al. 公开数据集（MIT license），消除数据收集风险；(b) 10 个任务按类型分层选取，假设来自原始研究（避免 researcher degrees of freedom）；(c) 6 模型跨 5 家族 3 规模；(d) 4 类 baselines/comparisons（specification curve + joint inference、ad hoc sensitivity baseline、PPI/DSL comparison、ANOVA variance decomposition + TEE comparison）；(e) 4 项 ablation studies（E/N/U sensitivity、task-conditional constraint、model diversity curve、batch-size）；(f) 预注册 on OSF；(g) pilot phase 验证成本和 batch-size。(h) 甚至考虑了大型 multiverse 的可视化问题（Krähmer & Young 的 multiverse plots）。这种实验设计的完备程度在 proposal 阶段非常少见，本身就是重要加分项。唯一小瑕疵是 ANOVA 中 Medium（仅 Scout）和 Small（仅 Gemma 4）各只有 1 个模型，size-class 对比可能欠动力。

  4. 可行性: 【强】 — 高可行性。(a) 公开数据集已有，无需数据收集；(b) 预算 $1,200-$2,000 合理且有 pilot 验证；(c) 技术栈无重大未知（API 调用 + 统计分析）；(d) 时间线 10-12 周现实；(e) 不需要训练模型；(f) 最大风险是 API 成本超出预算，但 pilot phase 可以早期发现。E/N/U 专家分类的人员招募可能需要一些协调，但 proposal 已将其纳入时间线。

  5. 写作与呈现: 【强】 — Proposal 本身的写作质量极高。文献定位精准（每项工作都有明确的差异化分析），逻辑链清晰（问题→现有方案的不足→机会→方法→实验→贡献），技术细节丰富但不凌乱。E/N/U 分类表格、模型选择表格、实验设计的结构化呈现都很专业。唯一隐忧是实际论文可能面临内容过多的问题——认识论贡献 + 方法论框架 + 大规模实证分析，需要在会议论文的篇幅限制内做取舍。

【概率估计】: [30% - 47%] 中位 38%

【估计理由】:
上界 47% 的理由：(1) 问题动机极强且时效性好（2025-2026 年多篇独立研究记录了同一问题）；(2) 实验设计在方法论论文中属于极其完备的水平，多个 baseline、ablation、pre-registration、public data 构成了一个几乎无懈可击的实验方案；(3) 认识论贡献（Auspurg 辩论的首个正面案例）增加了学术深度；(4) 执行风险极低。

下界 30% 的理由：(1) 核心方法创新有限——本质是将已有的 E/N/U multiverse 框架和 specification curve analysis 迁移到新领域，没有提出新的统计方法或算法；(2) 研究定位偏 CSS 方法论，可能不是所有 EMNLP 审稿人的兴趣范围；(3) 如果审稿人认为 Carlson & Burbano 的非正式 3-5 组合敏感性分析"已经足够好"，则会质疑 principled multiverse 的增量价值；(4) 纯方法论论文在 EMNLP 的接收率通常低于有明确技术突破的论文。

中位 38% 的核心判断：这是一篇方向正确、执行方案极其扎实的方法论研究，但缺乏让审稿人"眼前一亮"的核心技术突破。它的竞争力主要来自问题的重要性和实验设计的完备性，而非方法本身的新颖性。在 EMNLP 这样竞争激烈的会议中，这种"solid but not exciting"的定位通常处于 borderline 区间。

【主要风险】:
1. **Novelty 不足被拒**：审稿人可能认为"将 E/N/U multiverse 应用于 LLM annotation"本质上是框架迁移，方法论贡献不足以支撑顶会主会论文——尤其如果 reviewer 不认可认识论贡献的价值。
2. **受众匹配问题**：这篇论文的核心受众是使用 LLM 做标注的 CSS 研究者，而非 NLP/CL 核心社区。如果分配到不熟悉 CSS 方法论辩论（Auspurg vs Ganslmeier & Vlandas）或 multiverse methodology 的审稿人，可能会低估其贡献。建议在投稿时仔细选择 track（如 "Resources and Evaluation" 或 "NLP Applications"），并在 introduction 中更强调对 NLP 评估方法论的广泛影响。

【实施评估】:
  - 计算资源: 低。主要是 API 调用（500M-1.2B tokens）+ 标准 CPU 统计分析。无 GPU 训练需求。
  - 数据需求: 已满足。Baumann et al. 公开数据集（MIT license, 18 LLMs × 37 tasks × 13M labels），无需额外数据收集或人工标注。
  - 人工介入: 中等。E/N/U 分类需要人类领域专家（~1 周），如招募独立专家面板则需额外 1-2 周协调。
  - 训练需求: 无。不需要训练或微调任何模型，仅使用 LLM API 进行推断。
  - 新 Benchmark: 否。使用已有数据集和任务，但产出物（E/N/U 分类规则的 Boba DSL 形式化、robustness classification schema）可作为方法论工具发布。
  - 预估周期: 10-12 周（pilot 1 周 + annotation 2-3 周 + analysis 2-3 周 + writing 3-4 周，E/N/U 分类并行），API 成本 $1,200-$2,000 + pilot $50-100。总预算约 $1,300-$2,100，时间线在 EMNLP 2026 截稿前可完成。
```

Sources:
- [Baumann et al., "Large Language Model Hacking" (arXiv:2509.08825)](https://arxiv.org/abs/2509.08825)
- [McLaren et al., "Magic Words or Methodical Work?" (arXiv:2603.26898)](https://arxiv.org/abs/2603.26898)
- [Messing, "Hidden Measurement Error in LLM Pipelines" (arXiv:2604.11581)](https://arxiv.org/abs/2604.11581)
- [Mehrotra et al., "Multi-Perspective LLM Annotations" (arXiv:2603.21404)](https://arxiv.org/abs/2603.21404)
- [Del Giudice & Gangestad, "A Traveler's Guide to the Multiverse" (AMPPS, 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Auspurg, "Robustness is better assessed with a few thoughtful models" (PNAS, 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas, "Reply to Auspurg" (PNAS, 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Gligorić et al., "Can Unconfident LLM Annotations Be Used for Confident Conclusions?" (NAACL 2025)](https://aclanthology.org/2025.naacl-long.179/)
- [Audinet de Pieuchon et al., "Benchmarking Debiasing Methods" (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)
- [Egami et al., "DSL" (NeurIPS 2023)](https://naokiegami.com/paper/dsl.pdf)
- [Krähmer & Young, "Visualizing Vastness" (PLOS One, 2026)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/)
- [Carlson & Burbano, "LLMs as Annotators" (SMJ, 2026)](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)
- [Variance-Aware LLM Annotation (arXiv:2601.02370)](https://arxiv.org/pdf/2601.02370)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have comprehensive literature coverage. Let me compile the full evaluation.

```
【阶段】: Triage

【领域调研】:
- [Baumann et al., arXiv:2509.08825](https://arxiv.org/abs/2509.08825) (2025): 最直接的上游工作——18 LLMs × 37 tasks × 13M labels 的大规模实证研究，量化了 ~31% 的"LLM hacking"风险。本 proposal 直接复用其公开数据集（MIT license），并将其诊断性发现延伸为一个推断框架。核心关系：Baumann 诊断问题，本 proposal 提供方法论解决方案。
- [McLaren et al., arXiv:2603.26898](https://arxiv.org/abs/2603.26898) (2026): 在政治学文本标注中验证了交互效应（model × prompt × learning approach）主导主效应，直接支撑 proposal 的核心论点——逐一敏感性检验不够，需要遍历整个配置空间。
- [Messing, arXiv:2604.11581](https://arxiv.org/abs/2604.11581) (2026): 提出 TEE-corrected standard errors，解决单管线内的方差低估问题。Proposal 准确定位了其与 TEE 的互补关系：TEE 修正单配置内的推断，multiverse 评估跨配置的稳健性。两者可组合使用。
- [Variance-Aware LLM Annotation, arXiv:2601.02370](https://arxiv.org/pdf/2601.02370) (2026): 用 G-theory 分解标注精度层面的方差。Proposal 正确区分了标注精度方差 vs. 下游推断方差——这是一个有意义的概念区分。
- [Egami et al. DSL](https://naokiegami.com/paper/dsl.pdf) (NeurIPS 2023) / [Gligorić et al. CDI](https://aclanthology.org/2025.naacl-long.179/) (NAACL 2025) / [Audinet de Pieuchon et al.](https://aclanthology.org/2025.emnlp-main.1000/) (EMNLP 2025): 三篇构成"单管线纠偏"方法线。Proposal 清晰论证了 multiverse 与纠偏方法的正交性（robustness vs. validity），并设计了对比实验。
- [Mehrotra et al., arXiv:2603.21404](https://arxiv.org/html/2603.21404) (2026): "Perspective-Driven Inference" 挑战了主观任务中的"constant estimand"假设。Proposal 巧妙地通过 E/N/U 的 Type U 分类吸收了这一张力。
- [Simonsohn et al.](https://statmodeling.stat.columbia.edu/2024/11/12/specification-curve-analysis-and-the-multiverse/) (Nature Human Behaviour 2020) / [Del Giudice & Gangestad](https://journals.sagepub.com/doi/10.1177/2515245920954925) (AMPPS 2021): 分别提供 specification curve analysis 和 E/N/U 分类框架——proposal 的两大方法论基础。
- [Auspurg](https://www.pnas.org/doi/10.1073/pnas.2521917122) (PNAS 2025) vs. [Ganslmeier & Vlandas](https://www.pnas.org/doi/10.1073/pnas.2523374122) (PNAS 2025): multiverse 方法论辩论。Auspurg 批评暴力穷举混入不合理规格。Proposal 的核心认识论贡献正是回应这一批评——论证 LLM 标注管线是少见的满足 Auspurg 三个条件的场景。
- [Krähmer & Young, "Visualizing Vastness"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/) (PLOS One 2026): 提出 multiverse plots 作为大规模 specification curve 的可视化替代方案。Proposal 已计划在 >150 配置时使用。

- **调研总结**: 该领域正处于一个从"诊断 LLM 标注不稳定性"向"提供推断框架"过渡的关键时刻。诊断性工作（Baumann、McLaren、Messing）已充分建立了问题的紧迫性，纠偏方法（DSL、PPI）解决了单管线内的偏差问题，但**跨管线稳健性的推断框架**确实是一个清晰的空白。我未搜索到任何已有工作将 formal multiverse methodology / specification curve analysis 应用于 LLM 标注管线。这个 gap 是真实的、有价值的。

【整体印象】:
这是一份极其成熟的 proposal，接近"可以直接作为论文 introduction + method section 初稿"的水平。作为审稿人，我的第一反应是"impressed by the thoroughness"——文献定位精确、gap 论证充分、实验设计详尽且务实。整体倾向 **weak accept 到 accept**。

核心让我倾向积极评价的因素：(1) 研究 gap 真实存在且论证令人信服；(2) 认识论贡献（LLM 管线满足 Auspurg 条件）是一个genuine intellectual contribution，而非简单的"方法迁移"；(3) 实验设计的完备度（pilot → full execution → ablation → baseline comparison）在 proposal 阶段已经非常高；(4) 复用 Baumann 公开数据集大幅降低了执行风险。

让我犹豫的因素：(1) 核心方法（specification curve + E/N/U）均来自既有工作，NLP 社区审稿人可能质疑"方法论新颖性"——这是"将社科方法论应用到 NLP 实践"而非"提出新的 NLP 方法"；(2) 论文最终产出是"诊断框架+实证发现"而非可直接使用的工具或算法，可能被部分审稿人视为缺乏可操作性。

【核心贡献】:
三层贡献结构清晰：
1. **方法论贡献**（主）: 将 E/N/U multiverse 分类适配到 LLM 标注管线，提出任务条件化的分类准则。这不是简单套用——五个管线维度的 E/N/U 分类需要领域专业知识，且 task-conditional override 机制（如主观任务中 temperature 从 Type U 变为 Type E）是有思想的设计。
2. **认识论贡献**: 论证 LLM 标注管线是 multiverse analysis 的理想场景——回应了 Auspurg 对 multiverse 方法的根本质疑。这个贡献的价值在于它不仅服务于本文，还为整个 CSS×LLM 社区提供了一个方法论基础。
3. **实证贡献**: 10 个 CSS 任务的稳健性图谱——哪些发现 robust、哪些 fragile、哪些 sign-inconsistent，以及管线维度的方差分解。

贡献价值：**中高**。对于 CSS×NLP 交叉领域，这是一个及时且必要的工作。但对于纯 NLP 审稿人，可能需要额外说服其研究问题的重要性。

【方法合理性】:
方法整体合理且设计严谨。具体评估：

1. **E/N/U 分类的适配**: 合理。五个管线维度的选择覆盖了主要的 researcher degrees of freedom。Task-conditional override 不是 ad hoc 的——有清晰的理论基础（如确定性事实任务不需要 temperature 变化）。但分类依赖人类专家判断，引入了主观性——proposal 已通过 reliability protocol（Fleiss' κ + boundary perturbation）部分缓解了这个问题，但 κ 评估仅标记为"推荐"而非必做。
2. **Specification curve + permutation-based joint inference**: 直接采用 Simonsohn et al. (2020) 的标准方法，方法论上无争议。在 cached outputs 上做 permutation（不需要重新调用 API）是一个聪明的设计，大幅降低了计算成本。
3. **ANOVA 方差分解**: 标准方法，加入 model-size nesting 和 assumption checks（permutation ANOVA / aligned rank transform 作为非参替代）是负责任的统计实践。
4. **与 PPI/DSL 的比较**: 设计精巧——测试 robustness × validity 的正交性假设。

**是否有更简单的替代方案？** Carlson & Burbano (SMJ 2026) 的 3-5 配置 informal sensitivity analysis 就是更简单的替代方案，但 proposal 已明确论证了其不足（缺乏覆盖保证、无形式化推断、可能错过交互效应），并将其作为 experimental baseline 进行定量比较。这是对"更简单替代方案"的正面回应，说服力较强。

**一个潜在问题**: E/N/U 分类的可迁移性——本文的分类准则是为特定的 5 维管线设计的。如果管线增加新维度（如 few-shot examples 的选择、retrieval augmentation），分类准则需要重新制定。但这更像是 future work 而非方法缺陷。

【5 维度打分】:

1. **研究问题: 强** — 问题的紧迫性已被多篇高质量实证工作充分建立（Baumann 的 31% LLM hacking rate、McLaren 的交互效应主导、Messing 的 SE 低估 40-60%）。现有解决方案（DSL/PPI 纠偏、ad hoc sensitivity checks）都只解决了部分问题，formal multiverse framework 的缺失是一个真实的、有价值的 gap。问题定位精准——不是"LLM 标注不靠谱"（这已经有人说了），而是"我们需要一个原则性框架来评估跨管线稳健性"。

2. **方法与创新: 中偏强** — 方法合理、适配有思想，但核心方法（specification curve analysis、E/N/U 分类）均来自既有工作（Simonsohn 2020、Del Giudice & Gangestad 2021）。创新主要体现在"适配"和"认识论论证"层面——论证 LLM 管线满足 Auspurg 条件的 dual-layer argument 是一个 genuine intellectual contribution，但从纯技术角度看没有提出新的统计方法或算法。与 Audinet de Pieuchon et al. (EMNLP 2025) 和 Gligorić et al. (NAACL 2025) 相比，本 proposal 的方法论深度是可比的（它们也是将既有统计方法适配到 LLM 标注场景），但 novelty claim 的支撑主要在认识论层面而非技术层面。E/N/U 的 task-conditional 适配和 Boba DSL 形式化是加分项。

3. **实验设计: 强** — 这是 proposal 的最大亮点之一。实验设计的完备度远超同类 proposal：
   - **数据**: 复用 Baumann et al. 公开数据集，无额外数据收集风险
   - **任务选择**: 10 tasks stratified across 4 types，预注册在 OSF——消除了"挑选有利任务"的质疑
   - **模型选择**: 6 models × 5 families × 3 scale tiers × open/proprietary，覆盖全面
   - **Baselines**: (a) ad hoc sensitivity (k=3,5,10, 100 repetitions)——直接定量回应 Carlson & Burbano; (b) PPI/DSL 比较——测试 robustness × validity 正交性; (c) TEE 比较
   - **Ablations**: E/N/U sensitivity、task-conditional override effect、model diversity curve（含 top/random/bottom stratification）——设计精细且有针对性
   - **Pilot phase**: 先验证 token 消耗和 batch-size 效应，是负责任的实验实践
   - **统计严谨性**: permutation-based joint inference (≥500)、ANOVA assumption checks、非参替代方案

4. **可行性: 强** — 这是风险极低的 proposal：
   - 数据已公开（MIT license），无收集风险
   - 预算合理（$1,200-$2,000 for full execution），远低于大多数 LLM 实验
   - 时间线可行（10-12 weeks），有清晰的 milestone
   - 所有分析在 cached outputs 上进行，后分析阶段成本极低
   - 不需要训练模型、不需要构建新 benchmark
   - 唯一不确定性：E/N/U 独立专家评审的协调（1-2 weeks），但即使没有外部专家，boundary-case testing 也能部分替代

5. **写作与呈现: 强** — Proposal 本身的质量极高：
   - 文献综述结构化、全面、无遗漏（所有核心引用均经我搜索验证为真实论文且描述准确）
   - 研究 gap 的论证层层推进（诊断工作 → 纠偏方法 → 缺失的 multiverse framework）
   - 方法论各 stage 之间逻辑连贯
   - 预期贡献的三层结构（方法论 → 认识论 → 实证）清晰且不overclaim
   - 表格使用恰当（模型选择表、E/N/U 分类表）增强可读性
   - 对潜在质疑的预判到位（Auspurg critique、perspectivism tension、ad hoc sensitivity sufficiency）

【概率估计】: [32% - 48%] 中位 40%

【估计理由】:
**上界 48% 的支撑**: (1) 研究 gap 真实且有价值，已被 2025-2026 的多篇诊断性工作充分铺垫，时机恰好；(2) 实验设计的完备度是顶级的，在 proposal 阶段已接近可执行状态；(3) 认识论贡献（LLM 管线作为 Auspurg 辩论的 positive case study）增加了 intellectual depth，使论文不仅仅是"方法迁移"；(4) 可行性极高——公开数据、低预算、无训练需求——大幅降低了执行风险；(5) CSS×NLP 交叉方向在 EMNLP 有成功先例（Gligorić NAACL 2025、Audinet EMNLP 2025、Baumann 的工作方向）。

**下界 32% 的风险**: (1) 核心方法（specification curve + E/N/U）均为既有方法的适配，NLP 审稿人可能判定 novelty 不足——"没有新算法、新模型、新数据集"；(2) 论文产出是"诊断框架+实证图谱"而非可直接部署的工具，部分审稿人可能质疑 practical impact；(3) E/N/U 分类依赖专家判断，如果 inter-rater agreement 不高，可能动摇方法论基础；(4) 10 tasks × 6 models × ~200 configs 的大规模实验需要大量结果呈现，论文可能面临空间压力（如何在 8 页内清晰呈现 specification curves、ANOVA、ablation 等多层结果）。

**中位 40% 的推理**: 这是一篇定位清晰、执行风险低、intellectual contribution genuine 的方法论论文。它不是"wow paper"（没有惊人的新方法或新发现），但它解决了一个真实的、被充分文档化的问题，且解决方式在认识论层面有深度。在 EMNLP 的审稿光谱中，这类论文如果执行到位（实验结果确实展示了 multiverse 的增量价值 vs. ad hoc sensitivity），有相当概率被接收。关键变量是审稿人组成——如果遇到熟悉 CSS 方法论辩论的审稿人，概率可能在 45%+；如果遇到偏 core NLP / model-focused 的审稿人，可能降到 30% 左右。

【主要风险】:
1. **Novelty 质疑（最大风险）**: 审稿人可能认为"将 specification curve analysis 应用于 LLM 管线"是一个 straightforward adaptation，方法论新颖性不足以达到 EMNLP 主会标准。论文需要强调认识论贡献（Auspurg debate response）和 task-conditional E/N/U 设计的独特性来对抗这一质疑。
2. **结果呈现的空间压力**: 10 tasks × multiple analyses (specification curves, ANOVA, ablation, PPI/DSL comparison) 需要大量图表空间。如何在有限版面内有效传达核心发现，避免"堆砌结果"的印象，是写作层面的重大挑战。建议考虑 2-3 tasks 深入展示 + appendix 策略。

【实施评估】:
  - 计算资源: 极低。所有 LLM 调用通过 API 完成，后分析在标准计算资源上运行（permutation tests <24h）。无 GPU 训练需求。
  - 数据需求: 已满足。Baumann et al. 公开数据集（MIT license），含 18 LLMs × 37 tasks × 13M labels + gold-standard human annotations。无需额外数据收集。
  - 人工介入: 中等。E/N/U 分类需要人类领域专家（~1 week）；如招募独立专家 panel 计算 Fleiss' κ，额外 1-2 weeks 协调。预注册在 OSF。
  - 训练需求: 无。纯 inference + 统计分析。
  - 新 Benchmark: 无。使用现有 benchmark + 现有数据集。但 E/N/U 分类准则本身可视为方法论工具的贡献。
  - 预估周期: 10-12 weeks（pilot 1w → annotation 2-3w → analysis 2-3w → writing 3-4w，E/N/U reliability 与 annotation 并行）。周期合理且有余量。API 总成本 $1,300-$2,100（含 pilot）。
```

Sources:
- [Baumann et al. - Large Language Model Hacking](https://arxiv.org/abs/2509.08825)
- [McLaren et al. - Magic Words or Methodical Work](https://arxiv.org/abs/2603.26898)
- [Messing - Hidden Measurement Error in LLM Pipelines](https://arxiv.org/abs/2604.11581)
- [Variance-Aware LLM Annotation](https://arxiv.org/pdf/2601.02370)
- [Egami et al. - Design-based Supervised Learning](https://naokiegami.com/paper/dsl.pdf)
- [Gligorić et al. - Unconfident LLM Annotations](https://aclanthology.org/2025.naacl-long.179/)
- [Audinet de Pieuchon et al. - Benchmarking Debiasing Methods](https://aclanthology.org/2025.emnlp-main.1000/)
- [Mehrotra et al. - Multi-Perspective LLM Annotations](https://arxiv.org/html/2603.21404)
- [Del Giudice & Gangestad - A Traveler's Guide to the Multiverse](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Auspurg - Robustness with Thoughtful Models](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas - Reply to Auspurg](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Krähmer & Young - Visualizing Vastness](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to make a thorough assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Baumann et al., arXiv:2509.08825] (2025): 最直接的上游工作和数据来源。18 LLMs × 37 tasks × 13M labels 的大规模诊断研究，发现 31% 的假设检验可以通过选择不同 LLM 配置来翻转结论（"LLM hacking"）。本 proposal 正是建立在该诊断发现之上，提供推断框架。数据集已公开（MIT license），proposal 直接复用。
- [McLaren et al., arXiv:2603.26898] (2026): 政治学文本标注中 LLM pipeline 的 interaction effects 研究。核心发现：交互效应 > 主效应，说明逐对敏感性检查不足以捕捉不稳定性。直接支持 proposal "为何需要完整 multiverse 而非 ad hoc 检查" 的论点。
- [Messing, arXiv:2604.11581] (2026): TEE-corrected standard errors，naive SE 偏小 40-60%。定位互补：TEE 修正单一配置下的置信区间，proposal 的 multiverse 提供跨配置鲁棒性。Proposal 计划将 TEE 作为 per-specification 误差估计器嵌入。
- [Variance-Aware LLM Annotation, arXiv:2601.02370] (2026): G-theory 分解 5 个方差源（construct, interface, model, output, aggregation），12-85pp 偏移。关键区别：G-theory 在标注准确率层面分解方差，proposal 在下游推断层面分解方差——两者未必相关。
- [Egami et al., NeurIPS 2023] DSL + [Gligorić et al., NAACL 2025] CDI/PPI + [Audinet de Pieuchon et al., EMNLP 2025] benchmark: 单管道校正方法线。DSL/PPI 用小量人工标注校正 LLM 标注偏差，但都假设固定管道配置。Proposal 与之正交：校正解决管道内有效性，multiverse 解决管道间鲁棒性。
- [Mehrotra et al., arXiv:2603.21404] (2026): Perspective-Driven Inference，主张在主观任务中不同 LLM 视角是合法变异。直接挑战 multiverse 的"恒定估计量"假设——proposal 通过 Type U 分类吸收此张力。
- [Simonsohn et al., Nature Human Behaviour, 2020]: specification curve analysis 方法论基础。
- [Del Giudice & Gangestad, AMPPS, 2021]: E/N/U 分类框架——proposal 的核心方法论来源。
- [Auspurg, PNAS 2025] critique + [Ganslmeier & Vlandas, PNAS 2025] reply: multiverse 分析的合理性辩论。Proposal 的认识论贡献直接介入此辩论。

- 调研总结: LLM annotation instability 是一个快速升温的研究方向（2025-2026 密集出现诊断、校正、方差分解工作），但"formal multiverse methodology applied to LLM annotation pipelines"这一具体交叉点确实空白——没有搜索到任何现有工作将 specification curve analysis + E/N/U 分类应用于 LLM annotation。Proposal 的 novelty claim 成立。

【整体印象】:
作为审稿人，第一反应是"这是一篇思考深度很高、文献定位极其精准的方法论 proposal"。它识别了一个真实且重要的方法论空白：现有工作要么诊断问题（Baumann, McLaren）、要么修正单管道误差（DSL, PPI）、要么分解方差成分（Messing, G-theory），但没有人提供一个系统性的框架来回答"我的结论是否依赖于我选择了哪条管道"。这个问题在 CSS 社区每天都会遇到，但没有标准答案。

核心方法是将心理学/社会科学的成熟方法论（specification curve + E/N/U 分类）迁移到 LLM annotation 这个新领域。这种"方法迁移"既是优势（理论基础扎实）也是风险（创新性可能被质疑为"only applying existing methods"）。但 proposal 通过认识论论证（LLM annotation 是 Auspurg 条件的第一个正面案例）提升了智识贡献，这不是机械迁移。

实验设计是主要加分项——pilot validation、pre-registration、多层 baseline/ablation、与 PPI/DSL 的正交性检验——完备度远超平均 proposal。

倾向：**weak accept 到 borderline**。如果执行质量高、实证发现有意义（如发现某些管道维度对下游推断的方差贡献远大于预期），可以进入 accept 区间。

【核心贡献】:
1. **方法论贡献（主要）**: 首次将 E/N/U 分类框架适配到 LLM annotation pipeline，提供从管道维度分类到 specification curve 到联合推断的完整流程。这给 CSS 研究者一个可操作的工具来评估结论鲁棒性。
2. **认识论贡献**: 论证 LLM annotation 是 Auspurg 批评的第一个正面反例——穷举式 multiverse 在此场景下既有理论正当性又有实践可行性。这对方法论文献有独立价值。
3. **实证贡献**: 10 个任务的鲁棒性图景、方差分解、ad hoc vs principled multiverse 的定量比较、与 PPI/DSL 的正交性检验。

这些贡献对快速扩张的"LLM-as-annotator"社区有实质价值。贡献大小为"中到强"——不是范式突破，但填补了一个明确且重要的空白。

【方法合理性】:
方法整体合理，逻辑链清晰：
- E/N/U 分类 → 管道空间构建 → specification curve → 联合推断 → 方差分解。每一步都有成熟的方法论支撑。
- 将 E/N/U 做任务条件化（objective vs subjective）是合理的设计选择，直接回应了 Mehrotra et al. 的透视主义挑战。
- Boba DSL 的可执行化是好的工程选择，增加可复现性。

**可能的替代方案/简化方案：**
1. Carlson & Burbano (SMJ 2026) 提出的 3-5 组合 ad hoc 敏感性分析——proposal 已将其作为 baseline 进行定量比较，论证充分。
2. 直接用 Messing 的 TEE 做全局方差估计——但 TEE 不构建/遍历 multiverse，且不提供 specification-curve-based joint inference，proposal 的互补定位合理。
3. 纯蒙特卡洛抽样（随机采样管道配置）——但缺乏 principled construction 的理论保证，proposal 通过 ad hoc baseline ablation 实证说明了这一点。

**方法上的潜在弱点：**
- E/N/U 分类本身引入了研究者自由度（meta-level 讽刺），但 proposal 意识到了这一点并设计了 reliability protocol（boundary-case testing + 独立专家面板）。
- Permutation-based joint inference 的 500 次置换是否足够？文献中常用 1000+，建议增加。
- ANOVA 假设在 LLM annotation 数据上可能不成立（非正态、异方差），但 proposal 预见了这一点，提出了 permutation ANOVA 和 aligned rank transform 作为备选。

【5 维度打分】:
  1. 研究问题: 【强】 — "我的结论是否依赖于 LLM pipeline 的选择"是一个实际且紧迫的问题。Baumann et al. 的 31% LLM hacking risk 和 McLaren et al. 的交互效应主导发现都直接支持这个问题的重要性。CSS 社区对此有强烈需求但缺乏标准方案。问题定义清晰，研究价值高。

  2. 方法与创新: 【中偏强】 — 核心方法是成熟框架（specification curve + E/N/U）向新领域的迁移，而非全新方法。但迁移并非机械的：(a) 认识论论证（Auspurg 条件的正面案例）增加了智识深度；(b) 任务条件化的 E/N/U 分类是领域特定的创新；(c) 与 PPI/DSL 的正交性框架提供了新视角。引用对比：Messing (2604.11581) 提出 TEE 但不做 multiverse traversal；Baumann et al. (2509.08825) 诊断但不开药方；Audinet de Pieuchon et al. (EMNLP 2025) benchmark 校正方法但在固定管道内——本 proposal 的方法覆盖了这些工作留下的空白。创新性不算开创性但充分且有差异化。

  3. 实验设计: 【强】 — 这是 proposal 最突出的优势。(a) 数据来源低风险（Baumann et al. 公开数据集，MIT license）；(b) 10 个任务跨 4 种类型、6 个模型跨 5 家族 3 规模层级；(c) 多层 baseline（ad hoc k={3,5,10} 抽样 × 100 重复 vs full multiverse）；(d) 与 PPI/DSL 的正交性检验；(e) 4 个精心设计的 ablation（E/N/U 敏感性、任务条件约束、模型多样性曲线、batch-size 效应）；(f) pilot 阶段验证；(g) 预注册。对比领域标准（Audinet de Pieuchon et al. EMNLP 2025 的 benchmark 设计），本 proposal 的实验方案覆盖面更广、ablation 更系统。唯一小缺点：PPI/DSL 比较仅 2-3 个任务，可能不够说服力。

  4. 可行性: 【强】 — (a) 预算合理（$1,200-$2,000，无需 GPU 训练）；(b) 数据已有（无需新数据收集或人工标注）；(c) 时间线可行（10-12 周）；(d) 后标注分析（permutation tests, ANOVA, ablations）全部在缓存输出上操作，成本可忽略；(e) pilot 阶段降低了执行风险。这是一个"纯分析"项目，计算资源需求低，最大的执行风险是 API 调用的 token 估算偏差和 E/N/U 专家面板的招募——但都有缓解措施。

  5. 写作与呈现: 【强】 — Proposal 的逻辑结构非常清晰：问题定义 → 文献定位（诊断 / 校正 / 方差分解三条线的空白） → 认识论论证 → 三阶段方法 → 实验设计 → 预期贡献。文献覆盖全面，每个引用都有明确的定位功能（不是堆砌）。E/N/U 分类表格、模型选择表格、维度选项表格都增加了可读性。论证有层次感（epistemological argument → methodological contribution → empirical contribution）。少数可改进点：(a) 对"为何是这 6 个模型"的论证可更明确；(b) "expected contributions" 可以更突出预期的反直觉发现。

【概率估计】: [33% - 43%] 中位 38%

【估计理由】:
**上行因素（支持 43%）：** (1) 研究问题紧迫且定义清晰，直接回应 2025-2026 密集出现的 LLM annotation instability 文献；(2) 文献定位极其精准，空白识别可验证（搜索未发现任何现有 specification curve + E/N/U 应用于 LLM annotation 的工作）；(3) 认识论论证增加了智识深度，不是机械的方法迁移；(4) 实验设计完备度远超平均水平，多层 baseline 和 ablation 直接预防了常见审稿质疑；(5) 可行性极高，执行风险低。

**下行因素（拉向 33%）：** (1) "方法迁移"的创新性天花板——核心方法（specification curve + E/N/U）来自心理学，审稿人可能认为 intellectual novelty 不足以支撑顶会；(2) 论文可能被感知为"主要为 CSS 服务的方法论工具"，NLP 审稿人对其通用性存疑；(3) 实证发现的 upside 不确定——如果所有结论都是"这个维度重要，那个不重要"，可能缺乏令人兴奋的发现；(4) E/N/U 分类本身的主观性可能引发审稿质疑，即使有 reliability protocol。

**中位 38% 的理由：** 这是一篇方向正确、执行方案扎实、文献定位优秀的 proposal，在"整体合格、有实质贡献但需要强执行来弥补创新性天花板"的区间。在 EMNLP 接收率约 22-24% 的背景下，38% 的估计反映了它"高于 borderline 但需要实验结果来最终定论"的位置。如果实证发现揭示了反直觉或高影响力的模式（如某个被广泛使用的管道维度实际上是不稳定性的主要来源），概率可进入 40%+。

【主要风险】:
1. **"方法迁移"创新性质疑**: 审稿人可能认为将心理学的 specification curve + E/N/U 应用到 LLM annotation 只是"applying existing methods to a new domain"，intellectual novelty 不足。认识论论证可以部分缓解，但这仍是最可能导致 reject 的单一因素。
2. **实证发现平淡化**: 如果 10 个任务的结果只是"有些 robust、有些 fragile、不同维度重要性不同"而没有更深层的结构性洞察或反直觉发现，论文可能被评为"technically sound but not sufficiently insightful"——这在 EMNLP 是常见的 borderline reject 理由。

【实施评估】:
  - 计算资源: 低。无 GPU 训练需求，仅需 API 调用（$1,200-$2,000）和标准 CPU 后处理。
  - 数据需求: 已满足。Baumann et al. 公开数据集（MIT license），18 LLMs × 37 tasks × 13M labels。无需新数据收集。
  - 人工介入: 中等。E/N/U 分类需人工专家（~1 周），可选的独立专家面板（额外 1-2 周）。下游假设使用原始研究的预设假设，无需新假设构造。
  - 训练需求: 无。纯推理/分析项目，不涉及模型训练或微调。
  - 新 Benchmark: 否。不构建新 benchmark，但产出可复用的 E/N/U 分类 rubric 和 Boba DSL 规则。
  - 预估周期: 10-12 周（pilot 1 周 + annotation 2-3 周 + 分析/ablation 2-3 周 + 写作 3-4 周，E/N/U reliability 与 annotation 并行）。
```

Sources:
- [Baumann et al. - Large Language Model Hacking](https://arxiv.org/abs/2509.08825)
- [McLaren et al. - Magic Words or Methodical Work?](https://arxiv.org/abs/2603.26898)
- [Messing - Hidden Measurement Error in LLM Pipelines](https://arxiv.org/abs/2604.11581)
- [Variance-Aware LLM Annotation](https://arxiv.org/abs/2601.02370)
- [Mehrotra et al. - Multi-Perspective LLM Annotations](https://arxiv.org/abs/2603.21404)
- [Egami et al. - Design-based Supervised Learning (DSL)](https://arxiv.org/abs/2306.04746)
- [Gligorić et al. - CDI/PPI (NAACL 2025)](https://aclanthology.org/2025.naacl-long.179/)
- [Audinet de Pieuchon et al. - Benchmarking Debiasing Methods (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1000/)
- [Del Giudice & Gangestad - A Traveler's Guide to the Multiverse (AMPPS 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Auspurg - Robustness is better assessed with a few thoughtful models (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas - Reply to Auspurg (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Krähmer & Young - Visualizing Vastness (PLOS One 2026)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12875576/)


【原始 proposal（允许参考但不是主要依据）】:
## The LLM Annotation Multiverse: Specification Curve Analysis for Robust Computational Social Science

### Motivation

LLM-based text annotation has become the default measurement instrument in computational social science (CSS), yet the pipeline involves numerous researcher degrees of freedom—model selection, prompt template, temperature, system instruction, output parsing—each capable of shifting substantive conclusions. Baumann et al. (arXiv:2509.08825, 2025) document a 31% "LLM hacking" risk across 18 LLMs × 37 tasks × 13M labels: for nearly one-third of hypothesis tests, a researcher can find a pipeline configuration that reverses the statistical conclusion. McLaren et al. (arXiv:2603.26898, 2026) show that interaction effects among pipeline dimensions dominate main effects, meaning pairwise sensitivity checks underestimate true instability. Messing (arXiv:2604.11581, 2026) demonstrates that naive standard errors in LLM pipelines are 40–60% smaller than TEE-corrected standard errors that account for prompt, temperature, and judge-model variance. Kosch & Feger (CACM 2026) label this phenomenon "prompt-hacking"—the LLM analogue of p-hacking—but offer no formal remedy.

The methodological status quo offers two partial responses. Diagnostic studies (Baumann et al. 2025; McLaren et al. 2026; arXiv:2601.02370, 2026) quantify instability but prescribe no inferential framework. Statistical correction methods—DSL (Egami et al., NeurIPS 2023), PPI/CDI (Gligorić et al., NAACL 2025), benchmarked by Audinet de Pieuchon et al. (EMNLP 2025)—use small human-label sets to debias LLM annotations within a single chosen pipeline. These corrections answer "given my pipeline choice, how do I get an unbiased estimate?" but cannot answer the logically prior question: "does my conclusion depend on which pipeline I chose?" No existing work applies formal multiverse methodology—specification curve analysis with principled multiverse construction and joint statistical inference—to LLM annotation pipelines.

### Research Landscape

**Diagnostic work.** Baumann et al. (arXiv:2509.08825) provide the largest controlled study of LLM annotation instability (18 models, 37 tasks, 21 mitigation strategies). McLaren et al. (arXiv:2603.26898) extend this to interaction effects in political science annotation. The Variance-Aware LLM Annotation framework (arXiv:2601.02370, 2026) uses generalizability theory (G-theory) to decompose five variance sources (construct, interface, model, output, aggregation), reporting 12–85 pp outcome shifts from minor design choices. Crucially, G-theory decomposes variance at the annotation-accuracy level (how much does label quality vary?), whereas our ANOVA decomposes variance at the downstream-inference level (how much does the substantive conclusion vary?)—these need not correlate, as systematically biased but directionally consistent annotations may yield stable conclusions despite poor accuracy.

**Measurement error correction.** Messing (arXiv:2604.11581, 2026) decomposes LLM pipeline uncertainty into variance components and proposes TEE-corrected standard errors. TEE corrects the confidence interval around a single estimate within a design-study projection paradigm, but does not construct or traverse a multiverse of defensible configurations, classify pipeline dimensions, or provide specification-curve-based joint inference. Our framework is complementary: Messing's TEE can serve as the per-specification error estimator within each point on our specification curve, while our framework provides the global robustness assessment that TEE alone cannot deliver.

**Single-pipeline correction.** DSL (Egami et al., NeurIPS 2023) uses small human-label sets to debias LLM annotations for downstream inference; CDI (Gligorić et al., NAACL 2025) combines LLM confidence scores with human labels; Audinet de Pieuchon et al. (EMNLP 2025) benchmark DSL vs PPI across annotation budgets. All assume a fixed pipeline configuration—they solve pipeline-internal error but are blind to pipeline-external robustness. Multiverse analysis and correction methods address orthogonal dimensions of annotation credibility: robustness (does the conclusion hold across defensible pipelines?) and validity (is the conclusion correct within a given pipeline?). A finding can be robust yet invalid (all pipelines share the same systematic bias) or fragile yet valid in specific configurations. This orthogonality motivates our comparative evaluation with PPI/DSL.

**Perspectivism.** Mehrotra et al. (arXiv:2603.21404, 2026) propose Perspective-Driven Inference for subjective annotation tasks, treating different LLM perspectives as legitimate viewpoints. This directly challenges the "constant estimand" assumption for subjective tasks—a tension we address through our dual-layer epistemological argument (see Opportunity section).

**Multiverse methodology.** Simonsohn et al. (Nature Human Behaviour, 2020) formalize specification curve analysis: enumerate justified specifications, visualize the distribution of effects, and conduct permutation-based joint inference. Del Giudice & Gangestad (AMPPS, 2021) propose the E/N/U classification—Type E (equivalent: defensible alternatives expanding the multiverse), Type N (nonequivalent: one option clearly superior, fixed), Type U (uncertain: run separate sub-multiverses)—to discipline which specifications enter the multiverse. Auspurg (PNAS 2025) critiques brute-force multiverse for mixing justified and unjustified models; Ganslmeier & Vlandas (PNAS 2025) reply that what counts as "justified" is itself contested. Carlson & Burbano (SMJ 2026) recommend informal sensitivity analysis (3–5 model+prompt combinations) as practical guidance. Krähmer & Young ("Visualizing Vastness," PLOS One 2026) identify interpretability limits of specification curves in large multiverses and propose multiverse plots as an alternative visualization.

### Opportunity and Core Argument

**LLM annotation as an epistemically ideal setting for multiverse analysis.** Auspurg's (PNAS 2025) critique of multiverse analysis—that it conflates justified and unjustified specifications—rests on three conditions rarely satisfied in social science: (a) constant estimand across specifications, (b) no classical misspecification, (c) principled basis for classifying defensible specifications. We argue that LLM annotation pipelines satisfy these conditions, establishing the first positive case for principled exhaustive multiverse enumeration:

- **(a) Constant estimand—with a task-type-dependent nuance.** For objective/factual tasks (NER, factual binary classification), all pipeline configurations target the same annotation label for the same text—the estimand is defined by the coding scheme, not the model. However, for subjective tasks (toxicity, sentiment intensity, stance), Mehrotra et al. (arXiv:2603.21404, 2026) argue that different LLM "perspectives" may constitute legitimate construct variation, not mere measurement error. We resolve this tension through the E/N/U framework itself: for objective tasks, pipeline dimensions like model choice are Type E (equivalent alternatives targeting the same estimand); for subjective tasks, dimensions that may alter the construct (e.g., model family, temperature for stochastic perspective sampling) are classified as Type U, triggering separate sub-multiverses that each maintain a constant estimand. The E/N/U framework thus provides a task-adaptive mechanism for handling the constant-estimand condition—rather than assuming it universally holds or universally fails, it lets the classification absorb the objective/subjective distinction at the operationalization level.
- **(b) No misspecification in the classical sense.** Each pipeline configuration is a deterministic (or stochastic with known seed) mapping from text to label—no omitted-variable bias or functional-form misspecification, only measurement quality variation.
- **(c) Principled E/N/U classification is feasible.** Pipeline dimensions have well-defined semantics (model architecture, prompt verbosity, temperature value) with clear task-conditional constraints that make E/N/U classification less contested than in regression multiverse. E/N/U classification is performed by human domain experts (not LLM-assisted) to avoid circularity.

This epistemological argument is a core intellectual contribution: it demonstrates that the Auspurg critique, while valid for many social science applications, does not apply to LLM annotation (with appropriate task-type-dependent handling), establishing the first setting where exhaustive multiverse enumeration is both theoretically justified and practically feasible.

**Why principled multiverse, not ad hoc sensitivity checks?** Carlson & Burbano (SMJ 2026) recommend 3–5 model+prompt combinations as informal sensitivity analysis. This is insufficient because: (1) ad hoc selection may cluster in a narrow region of the specification space, missing interactions that reverse conclusions (McLaren et al. 2026); (2) without principled construction of the defensible space, there is no basis for claiming coverage; (3) ad hoc checks provide no formal joint inference. We quantitatively validate this argument by comparing ad hoc subsampling (k={3,5,10} random configurations, 100 repetitions) against full-multiverse robustness classifications as an experimental baseline.

### Approach

**Stage 1: E/N/U Multiverse Construction (Primary Methodological Contribution)**

Adapt Del Giudice & Gangestad's (AMPPS, 2021) E/N/U classification to LLM annotation pipeline dimensions. Five dimensions, each with task-conditional rules:

| Dimension | Options | Default | Task-conditional overrides |
|-----------|---------|---------|---------------------------|
| Model | 6 (see below) | Type E | — |
| Prompt template | 3 (minimal / instructed / CoT) | Type E | Simple binary tasks: CoT → Type N |
| Temperature | {0, 0.3, 0.7} | Type U | Deterministic factual tasks: temp=0 → Type N; Subjective tasks: all → Type E |
| System instruction | {generic, domain-specific, none} | Type E | — |
| Output parsing | {regex, structured JSON, first-token} | Type E | Free-form tasks → Type U |

Naïve Cartesian product: 6 × 3 × 3 × 3 × 3 = 486 per model subset, ~810 total. After E/N/U pruning: ~90–270 configurations per task. Classification criteria formalized in a Boba-style DSL (Liu et al., CHI 2021) as executable, reproducible rules.

**E/N/U classification rubric:**
- **Type E**: Multiple options defensible with no prior evidence favoring one for the given task type.
- **Type N**: One option clearly superior based on prior evidence or theoretical argument.
- **Type U**: Genuine uncertainty about whether options target the same construct; triggers separate sub-multiverses.

**E/N/U reliability protocol:** (1) Systematic boundary-case testing: for all E/N/U decisions at classification boundaries (e.g., CoT for binary tasks: N or E? Temperature for subjective tasks: E or U?), perturb the classification and measure downstream robustness impact. (2) Recommended: invite 2–3 independent CSS researchers to independently classify all dimensions for all tasks, compute inter-rater agreement (Fleiss' κ), and run sensitivity analysis on disagreement points.

**Stage 2: Specification Curve Analysis + Joint Inference**

For each task, execute all configurations in the pruned multiverse across all 6 models. For each configuration, compute the downstream hypothesis test on the annotated data. Apply specification curve methodology (Simonsohn et al., Nature Human Behaviour, 2020):

1. Rank specifications by effect size; visualize as specification curve. For tasks with >150 specifications, supplement with multiverse plots (Krähmer & Young, PLOS One 2026) and pipeline-dimension color/shape encoding for interpretability.
2. Classify each hypothesis as **robust** (sign-consistent and jointly significant), **fragile** (sign-consistent but not jointly significant), or **sign-inconsistent**.
3. Permutation-based joint inference (≥500 permutations): shuffle the mapping between pipeline dimensions and annotations, re-compute specification curves, derive joint p-value. Permutations operate on cached annotation outputs—no re-annotation required.

**Stage 3: Variance Decomposition**

Factorial ANOVA over the full-factorial results, quantifying each pipeline dimension's main effect and interactions on downstream inference instability. Model nested within model-size class (large: >250B total params; medium: ~110B; small: <30B) to disentangle scale from family effects. Report main effects, all two-way interactions, and the top-5 highest-variance three-way interactions. Effect sizes reported as η² (or ω² for unbalanced cells). ANOVA assumptions (normality, homoscedasticity) verified; if violated, use permutation-based ANOVA or aligned rank transform as nonparametric alternative. Compare downstream-inference variance decomposition with Messing-style (arXiv:2604.11581) TEE annotation-accuracy decomposition on the same configurations, testing whether annotation-accuracy variance predicts inference instability.

### Experimental Design

**Data source.** Baumann et al. (arXiv:2509.08825) public dataset (MIT license): 18 LLMs × 37 tasks × 13M labels with gold-standard human annotations.

**Task selection.** 10 tasks from Baumann's 37, stratified across: binary classification (3), multi-class classification (3), ordinal rating (2), subjective/contested (2). Selection criteria: (i) gold labels available, (ii) sample size ≥1,000, (iii) downstream hypothesis drawn from the original published study associated with the task in Baumann et al.'s dataset (the 37 tasks originate from 21 published social science studies, each with pre-existing research hypotheses). Using original hypotheses avoids researcher degrees of freedom. Task selection and hypotheses pre-registered on OSF before any annotation execution.

**Models.** 6 models spanning 5 families, 3 scale tiers, and open/proprietary divide:

| Model | Family | Architecture | Total params | Active params | Access |
|-------|--------|-------------|-------------|--------------|--------|
| Llama 4 Maverick | Meta | MoE | 400B | 17B | Open (Llama license) |
| Qwen 3.5 | Alibaba | MoE | 397B | 17B | Open (Apache 2.0) |
| Llama 4 Scout | Meta | MoE | 109B | 17B | Open (Llama license) |
| Gemma 4 | Google | MoE | 26B | — | Open |
| GPT-4o | OpenAI | Proprietary | — | — | API |
| Claude 3.5 Sonnet | Anthropic | Proprietary | — | — | API |

Model-size classes for ANOVA: Large (Maverick, Qwen 3.5, GPT-4o, Claude 3.5 Sonnet), Medium (Scout), Small (Gemma 4). E/N/U classification is human expert–only, so no circularity from including Claude.

**Pilot phase (prerequisite, ~$50–100).** Before full execution: (1) Run 2 tasks × 2 models to validate token consumption estimates. (2) Batch-size validation: compare batch=1 vs batch=10 vs batch=25 on these tasks, including position-effect analysis (accuracy by item position within batch). If batch=25 degrades accuracy >3pp vs batch=1, fall back to smaller batch. Literature suggests batch=25 is within safe range (BatchPrompt, ICLR 2024: 6/8 models stable through batch=100), but task-specific validation is prudent.

**Full execution.** Full-factorial execution of pruned multiverse per task across 6 models. Batched prompts (size determined by pilot). Estimated total: 500M–1.2B tokens, $1,200–$2,000 (Qwen 3.5 and Llama models via OpenRouter; GPT-4o via OpenAI API; Claude via Anthropic API).

**Evaluation and baselines.**
1. *Specification curve + joint inference*: For each of 10 tasks, produce specification curves (+ multiverse plots for large multiverses), classify hypotheses as robust/fragile/sign-inconsistent.
2. *Ad hoc sensitivity baseline*: For each task, randomly sample k={3, 5, 10} configurations (100 repetitions each), compute robustness classification, and report agreement rate with full-multiverse conclusion. This quantifies the incremental value of principled multiverse over informal sensitivity checks. No additional API cost (uses cached annotations).
3. *PPI/DSL comparison*: On 2–3 representative tasks, run PPI (Gligorić et al., NAACL 2025) and DSL (Egami et al., NeurIPS 2023) using gold labels from Baumann et al. as human-annotation budget. Compare: when multiverse says "robust," does corrected inference agree? When multiverse says "fragile," can correction resolve the fragility? This tests the robustness × validity orthogonality—whether pipeline-external robustness and pipeline-internal validity are indeed independent dimensions.
4. *Variance decomposition*: Factorial ANOVA with model-size nesting, assumption checks, effect sizes, and TEE comparison (see Stage 3).

**Ablation studies** (on 2–3 representative tasks):
1. *E/N/U sensitivity analysis*: (a) Perturb boundary E/N/U decisions and compare resulting specification curves and robustness classifications. (b) Compare principled (pruned) multiverse vs naïve (full Cartesian) multiverse to quantify pruning impact. Directly addresses Auspurg (PNAS 2025) critique with empirical evidence.
2. *Task-conditional constraint effect*: Remove task-type-specific overrides; measure change in specification curve and robustness classification.
3. *Model diversity curve*: Compute robustness using 6 → 3 → 1 models; additionally stratify as top-3-performing vs random-3 vs bottom-3 to separate model-count effect from model-quality effect. Report as stratified specification curves by model-size class (large-only vs full).
4. *Batch-size effect*: Results from pilot phase reported as validation evidence.

### Expected Contributions

1. **Methodological (primary):** The first adaptation of E/N/U multiverse classification (Del Giudice & Gangestad, AMPPS 2021) to LLM annotation pipelines, with a task-conditional classification rubric formalized in executable DSL (Liu et al., CHI 2021), enabling principled construction of the defensible configuration space.
2. **Epistemological:** A dual-layer argument that LLM annotation pipelines satisfy Auspurg's (PNAS 2025) conditions for justified exhaustive multiverse analysis—fully for objective tasks, and via E/N/U Type U classification for subjective tasks where the constant-estimand condition is modulated by perspectivism (Mehrotra et al., arXiv:2603.21404). This provides the first positive case study in the Auspurg–Ganslmeier & Vlandas (PNAS 2025) debate.
3. **Empirical:** A robustness landscape across 10 CSS tasks: which findings are robust/fragile/sign-inconsistent, which pipeline dimensions and interactions drive instability, how principled multiverse compares with ad hoc sensitivity checks and PPI/DSL correction, and whether annotation-accuracy variance (Messing-style TEE; arXiv:2604.11581) predicts inference instability.

### Budget and Feasibility

- **Pilot phase:** $50–100, ~1 week. Validates token estimates and batch-size effects.
- **Full annotation:** $1,200–$2,000 (6 models × 10 tasks × 90–270 configs × 1,000–3,000 samples; batched prompts). ~2–3 weeks, parallelized across model APIs.
- **Post-annotation analysis:** Permutation tests (≥500), ANOVA, ablations, ad hoc baseline simulations, PPI/DSL runs—all operate on cached outputs. <24 hours on standard compute.
- **E/N/U reliability:** Human expert classification (~1 week); if independent expert panel recruited, additional 1–2 weeks for coordination.
- **Data:** Baumann et al. public dataset (MIT license). No additional data collection or human annotation required.
- **Total timeline:** ~10–12 weeks to submission-ready manuscript (pilot: 1 week; annotation: 2–3 weeks; analysis + ablations: 2–3 weeks; writing: 3–4 weeks; E/N/U reliability: parallel with annotation).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9ae5e89c-562e-442b-967e-c15ad7028b0b",
  "type": "user",
  "uuid": "2b24d4fb-68e2-4701-b189-3258a36e6281",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:35:52.600Z_

```json
{
  "parentUuid": "2b24d4fb-68e2-4701-b189-3258a36e6281",
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
  "uuid": "ae2ae63d-d62b-4401-af9d-6616dfa9379a",
  "timestamp": "2026-05-20T04:35:52.600Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:35:52.600Z_

```json
{
  "parentUuid": "ae2ae63d-d62b-4401-af9d-6616dfa9379a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "32979273-25e0-49e7-aa9b-9e8ede2a83ce",
  "timestamp": "2026-05-20T04:35:52.600Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make an informed assessment.…",
  "leafUuid": "32979273-25e0-49e7-aa9b-9e8ede2a83ce",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Multiverse analysis for LLM annotation robustness",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:36:20.173Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them as Meta Judge.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Probability: [30% - 47%] 中位 38%
- 研究问题: 强
- 方法与创新: 中
- 实验设计: 强
- 可行性: 强
- 写作与呈现: 强


**Reviewer 2:**
- Probability: [32% - 48%] 中位 40%
- 研究问题: 强
- 方法与创新: 中偏强
- 实验设计: 强
- 可行性: 强
- 写作与呈现: 强

**Reviewer 3:**
- Probability: [33% - 43%] 中位 38%
- 研究问题: 强
- 方法与创新: 中偏强
- 实验设计: 强
- 可行性: 强

Now I'm looking at the consensus across all three reviewers. The probability estimates cluster tightly around 38-40%, with ranges that overlap substantially. There's strong agreement on the research question, experimental design, feasibility, and presentation quality, while the methodology shows slightly more variation—Reviewer 1 rates it as medium, while Reviewers 2 and 3 see it as medium-to-strong. 写作与呈现: 强 (all 3)
- 方法与创新: 中 to 中偏强 (R1: 中, R2: 中偏强, R3: 中偏强) — consensus on "not strong but adequate"

All three reviewers converge on the same core risks: the framework migration novelty ceiling, potential audience mismatch between CSS-oriented work and core NLP, and they all recognize the experimental design as thorough. They also all identify the Auspurg response as a genuine epistemological contribution. Where they diverge slightly is R2's more optimistic upper bound estimate versus R3's more conservative one, and R3 uniquely flagged the PPI/DSL comparison across only 2-3 tasks as potentially thin. R1 started flagging something about ANOVA and model size but the thought cut off.

Now I'm calculating the final probability by looking at the consistency across all three estimates. The standard deviation is very tight at around 0.94%, well below the 3% threshold, so I should anchor to the median range rather than spreading wide. The medians cluster around 38-40%, the lower bounds converge at 32%, and the upper bounds sit around 47%. Given this high alignment, I'll compress the interval and center it on the consensus. I'm settling on the range [31% - 46%] with a median of 38%, leaning toward the stricter estimates since R1 and R3 both converged there. For the implementation assessment, all three reviewers essentially aligned, so I can synthesize their feedback directly without needing to reconcile major disagreements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32979273-25e0-49e7-aa9b-9e8ede2a83ce",
  "isSidechain": false,
  "requestId": "req_011CbDCXbpAYkWSCUGsApMWE",
  "type": "assistant",
  "uuid": "87c4c47a-42f1-4770-afc0-a64631555c15",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWqfcjpSJBh1orLA93sHeu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23178,
      "cache_read_input_tokens": 16908,
      "output_tokens": 2764,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2764,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 23178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23178
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

_source line 9 · 2026-05-20T04:36:59.480Z_

【阶段】: Meta Judge
【三次中位】: [38%, 40%, 38%]  std=0.94%
【共识维度】:
- 研究问题=强（3/3）：LLM annotation pipeline 不稳定性已被 Baumann (31% LLM hacking)、McLaren（交互效应 > 主效应）、Messing（naive SE 偏小 40-60%）充分记录，"跨管道稳健性推断框架"的空白真实存在且有价值
- 实验设计=强（3/3）：公开数据集复用、10 tasks 分层选取、多层 baseline（ad hoc / PPI-DSL / TEE）、4 项 ablation、pilot 阶段、OSF 预注册——完备度远超同类 proposal
- 可行性=强（3/3）：无训练需求、公开数据、$1,200-$2,000 预算合理、10-12 周时间线现实、执行风险极低
- 写作与呈现=强（3/3）：文献定位精准无遗漏、逻辑链清晰、三层贡献结构不 overclaim
- 方法与创新=中/中偏强（3/3 均指出"框架迁移"天花板）：核心方法（specification curve + E/N/U）均为已有方法论适配到新领域，认识论贡献（Auspurg 辩论的正面案例）是加分项但不足以突破"方法迁移"天花板
- **主要风险共识**（3/3）：novelty 不足是最可能导致 reject 的单一因素——审稿人可能判定"applying existing methods to a new domain"intellectual novelty 不达标

【异常维度】:
- R1 单独指出 ANOVA 中 Medium（仅 Scout）和 Small（仅 Gemma 4）各只有 1 个模型，size-class 对比可能欠动力——有效观察但属实验细节，不影响整体判断
- R3 单独指出 PPI/DSL 比较仅 2-3 个任务可能不够说服力——合理但在方法论论文中 2-3 tasks 的 case study 式对比是可接受的
- R2 更强调论文版面压力（8 页内呈现大量结果）——属写作层面挑战，非学术质量问题

【最终概率】: [31% - 46%] 中位 38%
【一致性】: 高（std=0.94%，三位审稿人在所有 5 个 rubric 维度和核心风险判断上高度一致）
【综合理由】:

三位审稿人达成了罕见的高度一致：研究问题强、实验设计强、可行性强、写作强，但方法创新性受限于"框架迁移"天花板。这种"四强一中"的 profile 对应的正是 borderline accept 区间——proposal 在除 novelty 外的所有维度都表现优异，但 novelty 恰恰是顶会审稿中权重最高的单一维度。

三位审稿人的概率估计几乎完全重叠（中位 38-40%，区间大面积交叉），无需处理分歧。R2 略高 2 个百分点（40% vs 38%），源于其对"中偏强"创新性评价中认识论贡献的稍高权重，但这属正常审稿偏好差异而非实质性分歧。

综合取中位 38%，反映：(1) idea 质量天花板约 45%（研究问题强 + 方法创新中 = 有贡献但非突破性）；(2) 实验完备性将地板托至约 31%（即使审稿人对 novelty 持批评态度，也难以否认实验设计的完备性和问题的真实重要性）；(3) 关键变量是审稿人组成——熟悉 CSS 方法论的审稿人可能给 45%+，纯 NLP/model-focused 审稿人可能压到 30% 左右。

【建议】: 边缘（进入迭代优化，尝试强化 novelty 维度以突破天花板）

【实施评估】:
  - 计算资源: 低。纯 API 推理 + 标准 CPU 统计分析，无 GPU 训练需求。API 调用约 500M-1.2B tokens。
  - 数据需求: 已满足。Baumann et al. 公开数据集（MIT license, 18 LLMs × 37 tasks × 13M labels + gold-standard 人工标注），无需额外数据收集或人工标注。
  - 人工介入: 中等。E/N/U 分类需人类领域专家（~1 周）；可选独立专家面板计算 Fleiss' κ（额外 1-2 周协调）。下游假设取自原始研究，无需新构造。
  - 训练需求: 无。纯推理/分析项目。
  - 新 Benchmark: 否。使用已有数据集和任务，但产出可复用的 E/N/U 分类 rubric 和 Boba DSL 规则作为方法论工具。
  - 预估周期: 10-12 周（pilot 1 周 + annotation 2-3 周 + 分析/ablation 2-3 周 + 写作 3-4 周，E/N/U reliability 与 annotation 并行）。总预算 $1,300-$2,100。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87c4c47a-42f1-4770-afc0-a64631555c15",
  "isSidechain": false,
  "requestId": "req_011CbDCXbpAYkWSCUGsApMWE",
  "type": "assistant",
  "uuid": "a6054616-1f61-47b2-8719-0fcfde3df7bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWqfcjpSJBh1orLA93sHeu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23178,
      "cache_read_input_tokens": 16908,
      "output_tokens": 2764,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2764,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 23178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23178
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to make an informed assessment.…",
  "leafUuid": "a6054616-1f61-47b2-8719-0fcfde3df7bd",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Multiverse analysis for LLM annotation robustness",
  "sessionId": "e079606a-0e1e-4146-af49-536d0b121d5f"
}
```

---
