# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/14b61dac-0d91-4525-bbad-6d4372584af1.jsonl`
- **Structured JSON:** [`05e0191fdd8fb3fe949c.json`](../../sessions/05/05e0191fdd8fb3fe949c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:45:47.213Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:45:47.213Z",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have a thorough understanding of the landscape. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- BRIGHT (ICLR 2025, arXiv 2407.12883): 首个推理密集型检索基准，1,384 queries 跨 12 领域。SOTA 模型在 MTEB 上 59.0 nDCG@10 但 BRIGHT 上仅 18.3，证明推理密集型检索是未解决的难题。RARE 以此为主评测平台，方向正确。\n- RaDeR (EMNLP 2025, arXiv 2505.18405): 使用 MCTS 生成检索增强推理轨迹 + 自反思相关性评估，生成合成训练数据。bi-encoder-only SOTA 39.2 nDCG@10。RARE 的直接竞争对手，但方法论不同（合成数据 vs. 学习型 RM）。\n- ReasonEmbed (arXiv 2510.08252): 提出 ReMixer 合成 82K 训练样本 + Redapter 自适应训练算法，Qwen3-8B 骨干达 38.1 nDCG@10。另一个合成数据路线竞争者。\n- Q-RAG (ICLR 2026 Oral, arXiv 2511.07328): 将检索建模为 MDP，用 TD 学习训练嵌入器的 Q 值，聚焦多步检索。方法论上属于 outcome supervision 范畴，单 A100 训练。\n- UAE (arXiv 2604.22722, April 2026): 使用困惑度降低作为实用性信号，通过 Utility-Modulated InfoNCE 蒸馏到 bi-encoder。RARE 的最近方法论祖先——RARE 本质上将 UAE 的 outcome RM 替换为 process RM。\n- ThinkPRM (arXiv 2504.16828, 2025): 证明生成式 PRM 仅需 ~1K 样本即可训练，在 ProcessBench/MATH-500/AIME 上超越判别式 PRM。为 RARE 的 Stage 1 提供技术基础和数据效率先例。\n- LREM (arXiv 2510.14321, 2025): 用 Query-CoT-Item 三元组 + RL 精化推理轨迹训练推理嵌入。与 RARE 正交：LREM 修改嵌入模型的输入，RARE 修改嵌入模型的优化目标。\n- ReARTeR (SIGIR 2025, arXiv 2501.07861): 使用 PRM+PEM 在推理时做过程奖励引导的精化。PRM 用于生成端，非检索器训练。\n- Revela (arXiv 2506.16552): 自监督 LM 训练检索器，无标注数据，~1000x 更少数据量在 BRIGHT/BEIR 上有竞争力。\n- DIVER (arXiv 2508.07995): 多阶段 pipeline 达 46.8 nDCG@10，LATTICE 达 46.7-49.1。但均非 bi-encoder-only 方法。\n- BGE-Reasoner-Embed-Qwen3-8B (BAAI, 2025): bi-encoder 模式 37.1 nDCG@10，基于合成数据微调。\n\n- 调研总结: 推理密集型检索是 2025-2026 年活跃的前沿方向，bi-encoder SOTA 约 39.2 nDCG@10 (RaDeR)。现有方法均使用合成对比数据或 outcome 信号——无任何工作将 process supervision (PRM) 引入检索器训练。这个空白是真实存在的。但竞争激烈，该领域 6 个月内涌现了大量新方法。\n\n【整体印象】:\n作为审稿人的第一反应是 **weak accept 倾向**。这是一篇定位清晰、motivation 有说服力的 proposal。\"将 process supervision 引入 dense retriever training\"这个 gap 是真实的——我在调研中确认没有现有工作做过这件事。概念贡献（document utility 连续谱）提供了有洞察力的理论框架。评估方案异常完整（9 baselines、6 ablation 轴、RM 质量分析、下游推理评测），在 proposal 阶段就展示了严谨的实验思维。\n\n但核心方法论本质上是\"在 UAE 框架中用 PRM 替换 outcome RM\"，这使得贡献的增量性值得关注。此外，能否在仅 ~1.2K-2.4K 样本下训练出跨 12 个异质领域（数学/编程/经济/心理学/法律等）泛化良好的 PRM 存在不确定性。最终的价值完全取决于实验能否证明：PRM 信号确实捕获了 outcome 信号遗漏的推理脚手架文档效用，且这种捕获转化为可测量的检索改进。\n\n【核心贡献】:\n核心贡献是**首次将 process supervision (PRM) 引入 dense retriever 训练**，提出文档效用是一个从\"直接证据\"到\"推理脚手架\"的连续谱，并论证 process reward 信号可以捕获 outcome 信号系统性忽略的推理脚手架端效用。\n\n贡献价值评估：\n- 概念层面：有明确的洞察力，\"document utility spectrum\"框架为理解检索效用提供了新视角\n- 方法层面：中等——本质上是组合现有组件（ThinkPRM + UAE 的 Utility-Modulated InfoNCE），而非设计全新架构\n- 潜在影响力：如果实验成功验证假设，将为推理密集型检索开辟一条新的研究路线（learned process-based RM vs. synthetic contrastive data），影响面可观\n\n【方法合理性】:\n方法整体上合理，但存在几个值得审视的问题：\n\n1. **三阶段 pipeline 设计合理**：PRM 训练 → 文档打分 → 嵌入蒸馏的流程清晰，每一步都有现有工作支撑（ThinkPRM 证明 ~1K 样本可训练生成式 PRM；UAE 证明 Utility-Modulated InfoNCE 可蒸馏效用信号）。\n\n2. **更简单的替代方案？** \n   - 最直接的替代是使用 outcome-based RM 在 BRIGHT 上训练（proposal 中已作为 baseline 6-7 考虑），这本身说明作者有自觉\n   - BRIGHT 自带的 CoT-augmented queries 已能提升 +12.2 nDCG，这是零成本方案（proposal 已作为 baseline 8）\n   - RaDeR 的 MCTS 合成数据方法在 bi-encoder 上已达 39.2，且不需要训练 RM\n   - 这些替代方案的存在意味着 RARE 必须展示显著的增量收益才能证明额外复杂度的合理性\n\n3. **PRM 跨域泛化的关键假设**：\n   - 100-200 examples/domain × 12 domains ≈ 1.2K-2.4K 总量，ThinkPRM 的 ~1K 先例主要在数学领域验证\n   - 法律、心理学、经济学的\"推理链质量\"评估与数学差异巨大——PRM 能否在如此异质的领域间泛化是核心技术风险\n   - Proposal 设计了 250 对人工标注验证（Spearman ρ ≥ 0.7），这是好的，但阈值可能过于乐观\n\n4. **bi-encoder 的表达能力**：核心问题是 bi-encoder 是否有足够的表达能力在嵌入空间中编码\"推理效用\"这样的高阶语义属性。这不是一个可以预先保证的假设，但如果失败，也是有价值的负面结果。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】\n   — 推理密集型检索是 2025-2026 年检索领域最热门的前沿方向之一（BRIGHT ICLR 2025、RaDeR EMNLP 2025、Q-RAG ICLR 2026 Oral）。现有方法均依赖 outcome supervision 或合成对比数据，将 process supervision 引入检索器训练是一个真正未被探索的方向。研究问题（\"bi-encoder 能否编码推理效用？\"）有明确的 yes/no 答案，且无论结果都有科学价值。问题的重要性和时效性都很强。\n\n2. 方法与创新: 【中】\n   — 优点：novelty claim 成立——调研确认无现有工作将 PRM 应用于 retriever training。与 LREM（修改输入）、ReARTeR（推理时使用 PRM）等工作有清晰的差异化定位。\n   — 不足：方法论上是\"UAE framework + PRM 替换 outcome RM\"，属于组件替换而非方法创新。三阶段 pipeline 每一步都直接借用现有技术（ThinkPRM 的训练范式、UAE 的 Utility-Modulated InfoNCE）。与 Q-RAG 的 RL-based value learning、RaDeR 的 MCTS 探索相比，方法论新颖度偏低。一个审稿人可能会问：\"如果核心贡献是将 PRM 信号插入已有框架，这是否更像一个有价值的实验研究（empirical study）而非方法贡献？\"\n\n3. 实验设计: 【强】\n   — 9 个 baselines 覆盖了该领域几乎所有重要竞争方法，包括直接对比（RaDeR、ReasonEmbed、BGE-Reasoner）、消融控制（UAE reimplementation、capacity-controlled variant）、零成本替代（CoT-augmented queries）。6 轴 ablation 设计周全，特别是 signal type ablation（process vs. outcome vs. perplexity-reduction）直接验证核心假设。RM Quality Analysis 包含人工标注、per-domain 分析、bootstrapped CIs，达到了一线顶会的实验标准。唯一缺失：未包含 LREM 作为 baseline（同样将推理融入嵌入，虽然机制不同）。3 random seeds + compute budget 报告体现了可复现性意识。\n\n4. 可行性: 【中】\n   — 计算资源合理：PRM 训练 ~1-2h A100、文档打分 ~7-14h、嵌入训练 TBD 但预计适中，单台 A100 可完成核心实验。\n   — 主要风险点：(a) 跨 12 领域的 PRM 质量——特别是非 STEM 领域（法律、心理学、经济学）的推理链质量评估远比数学主观，100-200 examples 可能不足以捕获这些领域的推理模式；(b) paired reasoning comparison 数据构造需要 DeepSeek-R1 大量推理生成，实际成本可能高于估计；(c) 目标 Spearman ρ ≥ 0.7 在异质领域间可能过于乐观，如果某些领域达不到，需要有应急方案。\n   — 总体可执行，但存在中等程度的技术风险，且 proposal 未充分讨论失败预案。\n\n5. 写作与呈现: 【强】\n   — Proposal 结构清晰、论证逻辑严密。Related work 的定位非常精准，对 5 类相关工作的区分（outcome supervision、reasoning-intensive retrieval、CoT augmentation、reasoning injection taxonomy、concurrent work）有很强的组织能力。\"Reasoning injection taxonomy\"的三插入点分类（query-time / inference-time / training-time）是一个有效的贡献。具体例子（BRIGHT coding/economics/math 任务中的 answer-containing vs. reasoning-scaffolding 文档）增强了 motivation 的说服力。参考文献覆盖全面且时效性极强（含 2026 年 5 月的最新工作）。\n\n【概率估计】: [28% - 40%] 中位 34%\n\n【估计理由】:\n推理过程如下：\n- **加分因素**：(1) 研究问题在热门前沿方向上占据真实空白（process supervision → retriever training），novelty claim 经调研确认成立；(2) 评估方案在 proposal 阶段就达到了一线顶会标准，9 baselines + 6 ablation 轴 + RM 质量验证 + 下游推理评测，审稿人难以在实验设计上挑出重大缺陷；(3) 写作和 positioning 质量高，相关工作覆盖全面且分类精准；(4) 选题时效性好，2025-2026 年推理密集型检索是热门方向。\n- **减分因素**：(1) 方法论核心是组件替换（PRM 替换 outcome RM in UAE framework），创新幅度有限，可能被视为 empirical study 而非 methodological contribution；(2) PRM 跨 12 个异质领域的泛化是未经验证的核心假设，数据量（100-200/domain）较小；(3) 该领域竞争极其激烈，6 个月内涌现 RaDeR、ReasonEmbed、BGE-Reasoner、Revela、DIVER 等大量工作，RARE 需要在实验中展示显著的增量收益才能脱颖而出；(4) 目标 >39.2 nDCG@10 的 margin 如果很小（<1-2 点），说服力有限。\n- **综合判断**：这是一篇 solid 的 proposal，方向正确、执行方案完备，但核心方法论创新度中等。在 AAAI 这样的顶会，仅有良好的实验设计和清晰的 gap 可能不够——还需要方法上的深度或出乎意料的强实验结果。如果实验结果能显著超越 BRIGHT SOTA 并清晰验证 process vs. outcome supervision 的差异，中稿概率可以上探至 40%；如果实验提升有限或 PRM 泛化不佳，概率会下探至 28% 左右。\n\n【主要风险】:\n1. **方法被视为增量性组件替换**：审稿人可能认为\"在 UAE 框架中用 PRM 替换 outcome RM\"不构成足够的方法论贡献，而更像一个 ablation study 或 empirical investigation。需要通过充分的分析（RM Quality Analysis、per-domain breakdown）来论证 process supervision 带来的质的差异，而非仅仅量的提升。\n2. **PRM 跨域泛化失败**：如果 PRM 在非 STEM 领域（法律、心理学等）的推理效用评分质量显著下降（Spearman ρ < 0.5），整个框架在 BRIGHT 全 12 域上的综合性能可能无法超越基于大规模合成数据的竞争方法（RaDeR 82K+ 合成 pairs）。\n\n【实施评估】:\n  - 计算资源: 中等偏低。PRM 训练 ~1-2h A100，文档打分 ~7-14h A100，嵌入训练预计 ~8-24h A100（基于 Qwen3-8B 规模），总计 ~20-40h A100。单卡可完成核心实验，包含完整 ablation 预计需 ~100-200h A100。\n  - 数据需求: 需从外部语料（Proof Wiki、MATH train、StackOverflow、S2ORC、法律案例库）构造 ~1.2K-2.4K paired reasoning comparison 数据。需 BRIGHT benchmark 评测数据（公开可用）。BEIR 子集（公开可用）。\n  - 人工介入: 需要 250 对文档的人工标注（2 标注员，~20/domain），用于 PRM 验证和 utility-source 量表评估。标注工作量中等（约 2-4 人天）。\n  - 训练需求: 三阶段训练——(1) PRM fine-tuning on DeepSeek-R1-Distill-Qwen-7B；(2) PRM inference for document scoring；(3) Qwen3-Embedding-8B 的 contrastive distillation训练。均需 GPU 但规模适中。\n  - 新 Benchmark: 不需要构建新 benchmark，使用现有 BRIGHT + BEIR。但需构建 PRM 训练数据集（paired reasoning comparison）和人工标注集，这些可作为数据贡献。\n  - 预估周期: 数据构造 2-3 周，PRM 训练+验证 1 周，文档打分 1-2 天，嵌入训练+调参 2-3 周，完整实验+ablation 2-3 周，写作 2-3 周。总计约 8-12 周，适合 AAAI 2026 投稿周期。\n```\n\nSources:\n- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883)\n- [RaDeR: Reasoning-aware Dense Retrieval Models](https://arxiv.org/abs/2505.18405)\n- [ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2510.08252)\n- [Q-RAG: Long Context Multi-step Retrieval via Value-based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)\n- [UAE: Aligning Dense Retrievers with LLM Utility via Distillation](https://arxiv.org/abs/2604.22722)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [LREM: Large Reasoning Embedding Models](https://arxiv.org/abs/2510.14321)\n- [ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding](https://arxiv.org/abs/2501.07861)\n- [Revela: Dense Retriever Learning via Language Modeling](https://arxiv.org/abs/2506.16552)\n- [DIVER: A Multi-Stage Approach for Reasoning-intensive IR](https://arxiv.org/pdf/2508.07995)\n- [BGE-Reasoner-Embed-Qwen3-8B](https://huggingface.co/BAAI/bge-reasoner-embed-qwen3-8b-0923)\n- [A Survey of Reasoning-Intensive Retrieval](https://arxiv.org/html/2605.00063)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide my comprehensive evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [BRIGHT (arXiv 2407.12883)] (ICLR 2025): 定义了 reasoning-intensive retrieval 的基准，1384 queries，12 domains。当前最佳 retriever-only nDCG@10 约 39.2 (RaDeR)，最佳全 pipeline 为 DIVER 的 46.8。\n- [RaDeR (arXiv 2505.18405)] (EMNLP 2025): 用 MCTS 合成数据训练 reasoning-aware dense retriever，BRIGHT nDCG@10 ≈ 39.2，retriever-only SOTA。方法是合成对比数据，非 learned RM。\n- [ReasonEmbed (arXiv 2510.08252)] (arXiv 2025): ReMixer 合成 82K 样本 + Redapter 自适应学习，BRIGHT nDCG@10 = 38.1。同样依赖合成对比数据。\n- [BGE-Reasoner-Embed-Qwen3-8B] (BAAI, 2025): BRIGHT nDCG@10 = 37.1 (bi-encoder mode)，同系 backbone (Qwen3-8B)。\n- [UAE (arXiv 2604.22722)] (April 2026): 基于 perplexity-reduction 的 utility RM + Utility-Modulated InfoNCE 蒸馏到 bi-encoder。评估在 QASPER 上，未涉及 BRIGHT。RARE 的最直接方法论前身。\n- [Q-RAG (arXiv 2511.07328)] (ICLR 2026 Oral): Value-based RL 训练 embedder 做 multi-step retrieval，评估在 BabiLong/RULER 长上下文 benchmark，非 BRIGHT。\n- [SCARLet (arXiv 2504.00573)] (EMNLP 2025): 扰动归因法估计 passage-level utility，训练 retriever。10 个数据集评估。\n- [ThinkPRM (arXiv 2504.16828)] (arXiv 2025): 生成式 PRM，仅需 ~1K 合成验证 CoT + 8K process labels 即可超越判别式 PRM。支持 R1-Distill-Qwen-1.5B/7B/14B/QwQ-32B。\n- [LREM (arXiv 2510.14321)] (arXiv 2025): Query-CoT-Item triplets + RL 精炼推理轨迹做 reasoning embedding。修改 embedding 模型的输入端，与 RARE 修改训练信号端正交。\n- [Revela (arXiv 2506.16552)] (arXiv 2025): 自监督 LM 目标训练 retriever，无需标注/合成 query-doc 对，在 BRIGHT 上超越更大监督模型，~1000x 更少数据。\n- 调研总结: Reasoning-intensive retrieval 是 2025-2026 年的活跃方向，当前方法以合成对比数据（RaDeR, ReasonEmbed）和自监督学习（Revela）为主，outcome-based utility RM（UAE, SCARLet）已在标准 QA 上验证但未扩展到 BRIGHT。**将 process supervision (PRM) 引入 dense retriever 训练这一交叉点确实是未被占据的空白。**\n\n【整体印象】:\n这是一份极为成熟、定位精准的 proposal。作为审稿人，我的第一反应是 **borderline accept, leaning positive**。核心吸引力在于：(1) 它识别出了一个真实且未被填补的研究空白——process supervision 用于 retriever 训练；(2) 概念贡献（document utility 连续谱）有独立价值且可测试；(3) 评估方案之详尽远超多数投稿（9 baselines、6 ablation axes、human annotation、RM quality validation）。主要犹豫在于：**核心技术贡献本质上是 UAE pipeline 中将 outcome RM 替换为 PRM 的 principled component swap**，方法创新的 \"跨度\" 有限。是否 accept 取决于实验能否充分验证概念贡献——即 PRM 信号确实捕获了 outcome 信号遗漏的 reasoning-scaffolding utility。\n\n【核心贡献】:\n1. **概念贡献**（最核心）：提出 document utility 的 answer-containing ↔ reasoning-scaffolding 连续谱，论证 outcome supervision 系统性低估谱的 scaffolding 端，而 process supervision 可弥补。这是一个可证伪的理论命题，如果实验验证成功，对 retriever 训练范式有实质推动。\n2. **方法贡献**：首次将 PRM-based process supervision 作为 dense retriever 的训练信号（via distillation），保持 bi-encoder 的推理效率。\n3. **对领域的价值**：中等偏高。如果概念命题成立，它不仅改进 BRIGHT 性能，还为 retriever 训练信号的设计提供了新维度（从 \"文档是否有用\" 细化到 \"文档在哪个层面有用\"）。但如果实验显示 PRM 信号与 outcome 信号高度相关（即 scaffolding 文档的 outcome utility 也不低），概念贡献会被削弱。\n\n【方法合理性】:\n方法整体合理，三阶段 pipeline 的每个组件都有充分的先行工作支撑（ThinkPRM → PRM 训练；UAE → 蒸馏损失）。但需审视两个关键点：\n\n1. **PRM 训练数据构造的可靠性**：paired reasoning comparison（有/无文档的推理链质量差异）的信噪比可能有问题。LLM 的推理链对单个文档的响应可能高度随机——同一文档的 reasoning-utility label 在不同 sampling 下可能差异很大。proposal 提到 250 human annotations (ρ≥0.7) 作为验证，这是好的，但 ρ=0.7 是一个中等门槛。\n2. **更简单的替代方案**：(a) 直接用 ThinkPRM 作为 reranker（类似 ReasonRank 但更轻量），不需要蒸馏到 bi-encoder，可能更 cost-effective；(b) 直接用 CoT-augmented queries（proposal 自己列为 baseline 8，BRIGHT 原文报告 +12.2 nDCG）作为零成本替代。Proposal 需要在实验中充分证明蒸馏到 embedding space 的必要性——如果 PRM reranking 或 CoT queries 已经能达到类似效果，training-time 注入的价值就大打折扣。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — Process supervision 用于 retriever 训练是一个清晰的未探索方向。Document utility 连续谱的概念框架有理论价值且可测试。问题的成立不依赖于特定假设——即使最终 PRM 信号改进有限，negative result 本身也有信息量（说明 bi-encoder 的表征瓶颈或 scaffolding utility 的可学习性边界）。\n  \n  2. 方法与创新: 【中】 — 方法合理但创新跨度有限。核心操作是将 UAE 的 outcome RM 替换为 PRM（ThinkPRM 架构），蒸馏损失直接复用 Utility-Modulated InfoNCE。与 UAE 的差异仅在 RM 信号类型，与 ThinkPRM 的差异仅在应用场景。每个组件都是成熟技术的组合（\"bridging\" 型贡献），没有新的损失函数、架构或训练范式。调研中 RaDeR（MCTS 合成数据）和 ReasonEmbed（ReMixer + Redapter）在方法层面有更大的原创性。不过，\"正确的组合\"在正确的问题上仍有价值——关键在于实验能否证明这个组合产生了非平凡的 emergent effect。\n\n  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点。9 个 baselines 覆盖了领域内几乎所有竞争方法（RaDeR, ReasonEmbed, BGE-Reasoner, Revela, ReasonIR, UAE reimpl, capacity-controlled UAE, CoT-query, standard contrastive）。Baseline 6-7（UAE reimpl + capacity-controlled variant）是精心设计的——直接隔离信号类型 vs. RM 容量的贡献，这正是验证核心概念贡献所需的对比。6 轴 ablation 全面且有重点。RM Quality Analysis（250 human annotations, utility-source scale, Spearman/Kendall + bootstrap CI）直接验证核心假设。Downstream reasoning evaluation（统一 LLM + prompt，k=5,10）填补了 retrieval metric 与实际推理效果之间的 gap。3 seeds + compute-normalized comparison 体现了方法论的严谨。与 RaDeR 和 ReasonEmbed 的论文相比，这个评估方案的完整度和控制度都更高。\n\n  4. 可行性: 【强】 — 资源需求非常合理：PRM 训练 1-2h A100、document scoring 7-14h A100、embedding 训练 TBD 但基于 UAE pipeline 预计中等。总计 <30 GPU-hours（不含 embedding 训练）。PRM 数据仅需 1.2K-2.4K labeled pairs + 250 human annotations，human annotation 量可控（~20 per domain × 12 domains）。不需要构建新 benchmark。Backbone 选择（DeepSeek-R1-Distill-Qwen-7B, Qwen3-Embedding-8B）均为公开模型。Pipeline 的每一步都有参考实现（ThinkPRM 开源、UAE 方法公开）。唯一不确定性是 multi-domain PRM 的泛化质量——12 个 domain 各 100-200 pairs 是否足够需要实验验证，但 ThinkPRM 的 ~1K 数据效率结论提供了信心。\n\n  5. 写作与呈现: 【强】 — Proposal 的写作水准极高。研究动机从 outcome vs. process supervision 的差异自然推导，概念贡献（连续谱）清晰且有具体例子支撑。Research landscape 的梳理极为全面——不仅覆盖了直接竞争者，还建立了 \"reasoning injection taxonomy\"（query-time / inference-time / training-time）来定位自己的方法。与 concurrent work 的辨析（RICE-PO, Retrieval/Reward/Training Protocols）显示了对领域前沿的实时跟踪。Hypothesized contributions 的措辞恰当——用 \"targets\" 而非 \"achieves\" SOTA，体现了 proposal 阶段的适度性。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n**上行因素**：(1) 研究问题清晰且有真实空白（process supervision → retriever training 无先行工作）；(2) 评估方案极为完整，显著降低了 \"实验不充分\" 这一常见拒稿原因的概率；(3) 概念贡献（连续谱 + process/outcome 信号差异）如果被实验验证，有独立的理论贡献价值；(4) 可行性高，不存在 \"做不出来\" 的风险。\n\n**下行因素**：(1) **核心方法创新有限** — 审稿人可能评价为 \"UAE + ThinkPRM 的直接组合\"，缺乏方法论层面的原创贡献。在 AAAI 这样的顶会，仅凭 \"正确的组合\" 可能不够，尤其当组合本身没有产生新的技术挑战需要解决时。(2) **BRIGHT 基准的规模较小**（1384 queries），在小 benchmark 上的 SOTA claim 说服力相对有限，且其他工作已接近 39-40 nDCG@10，留给改进的 headroom 不大。(3) **概念贡献存在被反驳的风险** — 如果实验显示 outcome utility 和 process utility 高度相关（Spearman ρ>0.85），连续谱的区分价值就被削弱，此时 RARE 退化为 \"换了一种方式估 utility 的 UAE variant\"。(4) **缺少与 reranking 方案的 end-to-end 成本效益对比** — 如果直接用 PRM 做 reranking 就能达到或超过蒸馏到 bi-encoder 的效果，training-time 注入的动机就不成立。\n\n**中位 35% 的推理**：这是一篇 solid 的投稿，问题和评估都很好，但方法创新的 \"ceiling\" 限制了它。在典型的 AAAI 评审中，它可能获得 1 个 weak accept（被概念贡献和实验设计打动）、1 个 borderline（认可问题但质疑方法创新）、1 个 weak reject（认为是 incremental combination），最终需要 meta-reviewer 裁定。35% 反映了 \"有实质性贡献但不是 clear accept\" 的位置。\n\n【主要风险】:\n1. **\"Incremental combination\" 评价**：核心方法被审稿人视为 UAE pipeline 的 RM 组件替换，缺乏独立的方法论贡献（无新损失函数、无新架构、无新训练范式），这是最可能的拒稿理由。\n2. **Core hypothesis 未被充分验证或被反驳**：如果 PRM scores 与 outcome-based utility scores 在 BRIGHT 文档上的相关性很高（即 outcome supervision 并未 \"系统性低估\" scaffolding 文档），整篇论文的概念基础就会动摇。250 pairs 的 human annotation 可能不足以在统计上有力地区分两种信号。\n\n【实施评估】:\n  - 计算资源: 低-中。PRM 训练 ~1-2h A100，文档打分 ~7-14h A100，embedding 蒸馏预估 ~8-16h A100（基于 UAE 规模推测）。总计 ~20-35 A100-hours，远低于 RaDeR (MCTS) 和 ReasonEmbed (82K synthesis) 的成本。\n  - 数据需求: 中。需要从 ProofWiki, MATH, StackOverflow, S2ORC, legal databases 等外部语料采集 1.2K-2.4K paired reasoning samples + BM25 top-500 candidate 文档 (~50K-100K pairs)。无需新数据集收集，但 multi-domain 数据准备有一定工程量。\n  - 人工介入: 低-中。250 human annotations（2 annotators, ~20 per domain），用于 PRM quality validation 和 utility-source scale 标注。估计 ~40-60 人时。\n  - 训练需求: 是，需要训练 PRM (fine-tune DeepSeek-R1-Distill-Qwen-7B) 和 embedding model (fine-tune Qwen3-Embedding-8B)。均为 fine-tuning 而非从头训练。\n  - 新 Benchmark: 否。使用现有 BRIGHT + BEIR subset。但需要构建 multi-domain PRM 训练数据和 human annotation 数据，这些可作为资源贡献发布。\n  - 预估周期: 约 8-12 周。数据准备 2-3 周，PRM 训练与验证 1-2 周，文档打分 1 周，embedding 训练与 ablation 实验 2-3 周，downstream evaluation + 分析 1-2 周，写作 2 周。\n```\n\nSources:\n- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883)\n- [RaDeR: Reasoning-aware Dense Retrieval Models](https://arxiv.org/abs/2505.18405)\n- [ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2510.08252)\n- [UAE: Aligning Dense Retrievers with LLM Utility via Distillation](https://arxiv.org/abs/2604.22722)\n- [Q-RAG: Long Context Multi-step Retrieval via Value-based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [SCARLet: Training a Utility-based Retriever Through Shared Context Attribution](https://arxiv.org/abs/2504.00573)\n- [LREM: Large Reasoning Embedding Models](https://arxiv.org/abs/2510.14321)\n- [Revela: Dense Retriever Learning via Language Modeling](https://arxiv.org/abs/2506.16552)\n- [BGE-Reasoner-Embed-Qwen3-8B](https://huggingface.co/BAAI/bge-reasoner-embed-qwen3-8b-0923)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Here is my assessment:\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883) (ICLR 2025): 定义了reasoning-intensive retrieval任务，初始SOTA仅24.3 nDCG@10，是RARE的主要评测平台。\n- [RaDeR: Reasoning-aware Dense Retrieval Models](https://aclanthology.org/2025.emnlp-main.1011/) (EMNLP 2025): 当前retriever-only BRIGHT SOTA (~39.2 nDCG@10)，使用MCTS生成合成数据。RARE的直接竞争者。\n- [ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2510.08252) (arXiv 2025): 使用ReMixer合成数据+RI-InfoNCE，BRIGHT上38.1 nDCG@10。另一直接竞争者。\n- [BGE-Reasoner-Embed-Qwen3-8B](https://huggingface.co/BAAI/bge-reasoner-embed-qwen3-8b-0923) (BAAI 2025): bi-encoder模式37.1 nDCG@10，同backbone家族，关键baseline。\n- [UAE: Aligning Dense Retrievers with LLM Utility via Distillation](https://arxiv.org/abs/2604.22722) (arXiv April 2026): RARE最近的方法论祖先——使用Utility-Modulated InfoNCE进行perplexity-reduction utility蒸馏。仅在QASPER上评测，未在BRIGHT上测试。RARE本质上是将UAE的outcome-based RM替换为process-based PRM。\n- [Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training](https://arxiv.org/abs/2511.07328) (ICLR 2026 Oral): 使用RL（TD学习）训练embedder进行多步检索。证明了learned utility signals对检索有效，但方向不同（multi-step sequential retrieval vs. single-step reasoning-intensive retrieval）。\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828) (arXiv 2025): 证明了generative PRMs仅需~1K样本即可训练，是RARE Stage 1的技术基础。\n- [SCARLet: Training a Utility-based Retriever Through Shared Context Attribution](https://arxiv.org/abs/2504.00573) (EMNLP 2025): 使用perturbation attribution估计passage-level utility。Outcome supervision的代表性工作。\n- [ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding](https://arxiv.org/abs/2501.07861) (SIGIR 2025): 在inference-time使用PRM+PEM进行reasoning refinement。PRM用于RAG但在inference端而非training端，与RARE正交。\n- [Revela: Dense Retriever Learning via Language Modeling](https://arxiv.org/abs/2506.16552) (arXiv 2025): 自监督方法，在BRIGHT上表现competitive，使用~1000x更少数据。\n- [LREM: Large Reasoning Embedding Models](https://arxiv.org/abs/2510.14321) (arXiv 2025): 通过Query-CoT-Item triplets注入reasoning能力。RARE与其正交——LREM改变embedding模型看到什么，RARE改变embedding模型优化什么。\n- [Agentic-R: Learning to Retrieve for Agentic Search](https://arxiv.org/abs/2601.11888) (arXiv 2026): 使用binary EM的outcome supervision训练retriever for agentic search。\n\n- **调研总结**: Reasoning-intensive retrieval是2025-2026年的热门方向，BRIGHT上SOTA从24→39+快速演进。现有方法主要通过合成对比数据（RaDeR/ReasonEmbed）、self-supervised LM（Revela）或CoT增强输入（LREM/BGE-Reasoner）来提升性能。将process supervision（PRM）引入dense retriever training确实是一个尚未被填补的gap——现有PRM在retrieval中的应用限于query refinement（SmartSearch）和inference-time reranking/refinement（ReARTeR、ReasonRank），尚无人在training-time通过PRM指导bi-encoder学习。\n\n【整体印象】:\n作为审稿人，我的第一反应是这是一篇**定位精准、实验设计出色、但方法论增量偏轻**的投稿。Proposal对领域的梳理异常全面——对outcome supervision四个代表性工作、reasoning-intensive retrieval SOTA、reasoning injection taxonomy的三个插入点、以及concurrent work的区分都非常清晰，展现了作者对领域的深度理解。核心novelty claim（将process supervision引入retriever training）经调研确认成立。\n\n但冷静审视，方法论的核心操作是\"在UAE框架中将outcome-based RM替换为process-based PRM\"，这个delta虽然conceptually motivated，但methodologically较thin。一个审稿人可能会问：这本质上只是换了一个reward signal的来源，而非提出新的训练范式。Conceptual contribution（document utility as continuous spectrum）虽然elegant，但更接近observation而非formalizable theory。\n\n我会倾向于**borderline accept/weak reject**——如果实验结果强有力（显著超过SOTA，ablation清晰验证process vs. outcome的差异），可以接受；如果结果marginal，方法论创新不足以支撑。\n\n【核心贡献】:\n1. **概念贡献**：提出document utility存在从\"直接证据\"到\"推理脚手架\"的连续谱系，outcome supervision系统性地忽略了推理脚手架端——这是一个有价值的观察，但需要强有力的实验验证。\n2. **方法贡献**：首次将process supervision引入dense retriever training，通过PRM-guided distillation将reasoning utility编码进bi-encoder表示。\n3. **实验贡献**：在BRIGHT上提供了第一个process vs. outcome supervision的controlled comparison。\n\n贡献的价值中等偏上。核心insight（process vs. outcome supervision for retriever training）是genuine的，但作为一个新research direction的开创性贡献还缺少足够的理论深度——更像是一个well-motivated engineering contribution。\n\n【方法合理性】:\n方法整体合理，但存在几个需要审视的点：\n\n1. **PRM数据构建的可靠性**：通过\"paired reasoning comparison\"（有/无document d的reasoning chain质量差异）来构建training labels是方法的核心假设。这假设DeepSeek-R1能稳定地反映document对reasoning的影响——但LLM reasoning的randomness可能导致noise。Proposal设定了Spearman ρ ≥ 0.7的人工标注验证标准，这是合理的safeguard。\n\n2. **更简单的替代方案**：一个reviewer可能会问——为什么不直接用reasoning chain的outcome improvement作为连续标签（而非binary EM），而需要额外训练一个PRM？即，outcome supervision的\"连续化\"版本是否已经能捕获大部分RARE声称的信号？Proposal的capacity-controlled UAE variant (Baseline 7) 部分地址了这个问题，但需要清晰展示process signal捕获的是outcome signal无法捕获的信息。\n\n3. **Bi-encoder的表达瓶颈**：RARE声称bi-encoder可以编码\"reasoning utility\"这样的high-order semantic property。但bi-encoder的独立编码特性天然限制了它捕获query-document交互级推理关系的能力。这是一个fundamental tension，Proposal承认了但未充分讨论。\n\n4. **与LREM的组合可能性**：LREM改变embedding model的输入（CoT-augmented），RARE改变优化目标（PRM scoring）。两者声称正交，但未讨论组合效果——这既是一个遗漏也可能是一个机会。\n\n【5 维度打分】:\n\n1. **研究问题**: 【中偏强】— 问题定义清晰且有价值。Reasoning-intensive retrieval是活跃方向，process supervision在retriever training中的缺位是real gap。但问题的\"重要性\"略受限于应用范围——BRIGHT虽然是标准benchmark，但reasoning-intensive retrieval在实际部署中的需求规模尚不明确。相比Q-RAG (ICLR 2026 Oral)这样定义新范式的工作，RARE更多是在已有范式内的refinement。\n\n2. **方法与创新**: 【中】— Novelty claim经调研确认成立，无prior work将PRM用于retriever training。但方法论delta偏轻——核心操作是在UAE的Utility-Modulated InfoNCE框架中替换reward signal来源。与RaDeR的MCTS合成数据、Q-RAG的RL-based value learning、Revela的self-supervised LM相比，RARE的方法论创新幅度较小。UAE (arXiv 2604.22722) 已经建立了utility distillation的完整框架，RARE的创新集中在Stage 1的PRM训练和document utility spectrum的概念框架。\n\n3. **实验设计**: 【强】— 这是Proposal最突出的优势。9个baselines（包括capacity-controlled variant用于公平比较）、6个ablation axes（信号类型、损失函数、数据规模、backbone大小、域覆盖、per-domain分析）、RM quality validation（250人工标注样本、inter-annotator agreement、correlation analysis）、downstream reasoning evaluation——实验设计的完备性在proposal阶段非常少见。特别值得注意的是Baseline 6（UAE-style on BRIGHT）和Baseline 7（capacity-controlled variant）的设置，直接回答了\"是signal type还是RM capacity\"的confounding问题。与RaDeR、ReasonEmbed等发表工作的实验设计相比，这里的ablation更加系统。\n\n4. **可行性**: 【中偏强】— 计算需求合理（PRM训练1-2h，document scoring 7-14h on A100），数据构建规模适中（1.2K-2.4K labeled pairs），基于ThinkPRM的data-efficient PRM训练已被验证。主要风险是PRM数据质量——paired reasoning comparison依赖LLM的稳定性，可能需要多次采样取平均来降噪。另外，embedding training的compute cost标注为TBD，这是一个gap。\n\n5. **写作与呈现**: 【强】— Proposal的组织结构清晰，positioning section是我见过的proposal中最全面的之一。Reasoning injection taxonomy（query-time / inference-time / training-time）的框架化非常有效。与concurrent work的区分（RICE-PO、Retrieval Reward and Training Protocols）表明作者持续跟踪领域。概念贡献（continuous spectrum）虽然thin，但表述清晰有力。\n\n【概率估计】: [25% - 38%] 中位 31%\n\n【估计理由】:\n- **上行因素**：(1) Novelty claim confirmed——确实无人做过process supervision for retriever training；(2) 实验设计极为完备，若结果有力可构成solid empirical contribution；(3) 领域热度高，reasoning-intensive retrieval是2025-2026的焦点方向；(4) 与UAE/ThinkPRM的技术衔接自然，方案可行性高。\n- **下行因素**：(1) 方法论增量偏轻——本质是\"换reward signal\"，缺乏architectural或training paradigm层面的创新；(2) 核心假设风险——bi-encoder能否真正编码reasoning utility是open question，如果实验结果marginal，paper缺少足够的方法创新来支撑；(3) 竞争激烈——RaDeR (39.2) 用MCTS、ReasonEmbed (38.1) 用大规模合成数据，RARE能否仅凭1.2K-2.4K PRM标注数据超越SOTA存疑；(4) conceptual contribution虽然elegant但thin——\"continuous spectrum\"更像observation而非theory。\n- **中位31%的理由**：这是一篇方向正确、执行方案solid的工作，但方法创新深度不足以稳定进入accept区间。如果实验结果强有力（显著超SOTA + ablation清晰展示process vs. outcome差异），概率推向38%；如果结果marginal（与SOTA comparable但不显著优于），方法创新不足以弥补，概率滑向25%。AAAI的接收率通常在23-25%左右，这篇处于borderline位置。\n\n【主要风险】:\n1. **方法论增量不足**：如果reviewer认为\"在UAE框架中换reward signal\"不构成sufficient novelty，且实验结果未能decisively证明process > outcome supervision，paper可能因\"incremental contribution\"被拒。这是最大的单一风险。\n2. **核心假设验证失败**：PRM scores能否有效指导bi-encoder学习reasoning utility是一个未经验证的假设。如果PRM标注质量不达标（Spearman ρ < 0.7）或PRM-guided training未能在BRIGHT上显著超过outcome-based baseline，核心叙事崩塌。\n\n【实施评估】:\n  - 计算资源: 中等偏低。PRM训练~1-2h A100，document scoring ~7-14h A100，embedding training TBD但基于Qwen3-8B fine-tuning预估10-20h A100。总计~30-40h A100，非常可控。\n  - 数据需求: 中等。需要从Proof Wiki、MATH、StackOverflow、S2ORC等构建1.2K-2.4K标注对，需要DeepSeek-R1进行reasoning chain生成（大量inference calls），需要250条人工标注进行validation。\n  - 人工介入: 需要2名标注员对250条BRIGHT正例文档进行utility-source标注（pure evidence ↔ pure scaffolding），规模可控但需要domain expertise（覆盖12个领域）。\n  - 训练需求: 需要训练——(1) PRM fine-tuning on DeepSeek-R1-Distill-Qwen-7B; (2) Qwen3-Embedding-8B embedding distillation。两阶段训练，但规模适中。\n  - 新 Benchmark: 不需要构建新benchmark。使用现有BRIGHT（primary）和BEIR subset（regression test）。\n  - 预估周期: 4-6周。数据构建1-2周（含LLM inference），PRM训练+验证1周，embedding训练+评测1-2周，ablation+分析1周。\n```\n\nSources:\n- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883)\n- [RaDeR: Reasoning-aware Dense Retrieval Models](https://aclanthology.org/2025.emnlp-main.1011/)\n- [ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2510.08252)\n- [BGE-Reasoner-Embed-Qwen3-8B](https://huggingface.co/BAAI/bge-reasoner-embed-qwen3-8b-0923)\n- [UAE: Aligning Dense Retrievers with LLM Utility via Distillation](https://arxiv.org/abs/2604.22722)\n- [Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training](https://arxiv.org/abs/2511.07328)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [SCARLet: Training a Utility-based Retriever Through Shared Context Attribution](https://arxiv.org/abs/2504.00573)\n- [ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding](https://arxiv.org/abs/2501.07861)\n- [Revela: Dense Retriever Learning via Language Modeling](https://arxiv.org/abs/2506.16552)\n- [LREM: Large Reasoning Embedding Models](https://arxiv.org/abs/2510.14321)\n- [Agentic-R: Learning to Retrieve for Agentic Search](https://arxiv.org/abs/2601.11888)\n- [DIVER: A Multi-Stage Approach for Reasoning-intensive IR](https://arxiv.org/abs/2508.07995)\n- [ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability](https://arxiv.org/abs/2508.07050)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Reasoning-Chain-Aware Reward Model for Dense Retriever Training (RARE)\n\n## Core Problem\n\nCurrent utility-based retriever training methods — binary EM (Agentic-R, arXiv 2026), perturbation attribution (SCARLet, EMNLP 2025), factorized Q-values (Q-RAG, ICLR 2026 Oral), perplexity reduction (UAE, arXiv 2604.22722, April 2026) — all provide **outcome supervision**: they evaluate documents by their effect on the final answer, treating document utility as a single undifferentiated dimension. This conflates documents that reduce uncertainty over the **answer space** (answer-containing documents providing direct evidence) with documents that reduce uncertainty over the **reasoning trajectory space** (reasoning-scaffolding documents enabling multi-step inference without containing the answer). On standard QA where answer-containing documents dominate, outcome supervision suffices. On reasoning-intensive retrieval (BRIGHT, ICLR 2025), reasoning-scaffolding documents are critical — a theorem explanation may be essential for solving a math problem while containing no part of the answer. Outcome signals systematically under-value such documents.\n\nMeanwhile, the PRM literature (survey: arXiv 2510.08049) has established that **process supervision** — evaluating intermediate reasoning steps rather than final outcomes — captures qualitatively different information from outcome supervision. Yet no work has brought process supervision into dense retriever training.\n\n**Core Question**: Can a process reward model that evaluates reasoning-chain quality serve as a training signal for dense retrievers, enabling them to encode reasoning utility — a high-order semantic property — in bi-encoder representations?\n\n## Conceptual Contribution: Document Utility as a Continuous Spectrum\n\nWe propose that document utility for reasoning-intensive tasks lies on a **continuous spectrum** from pure direct evidence (answer-containing) to pure reasoning scaffolding, with most documents exhibiting a mixture. Existing outcome-based utility signals collapse this spectrum into a single scalar dominated by the answer-containing end, because their loss functions are defined over the answer space. A process reward signal is sensitive to the reasoning-scaffolding end of the spectrum, because it evaluates quality changes in intermediate reasoning steps — capturing utility that outcome signals miss. This is not merely a taxonomic observation: it predicts that process-supervised retriever training will produce qualitatively different retrieval behavior — higher recall of reasoning-scaffolding documents — compared to outcome-supervised training, even when both achieve similar aggregate scores.\n\nConcrete examples: In BRIGHT's coding tasks, answer-containing = solution code, reasoning-scaffolding = relevant algorithm description. In economics, answer-containing = stated conclusion, reasoning-scaffolding = theoretical framework for derivation. In mathematics, answer-containing = final result, reasoning-scaffolding = applicable lemma or proof technique.\n\n## Research Landscape and Positioning\n\n**Outcome supervision for retriever training**: SCARLet (EMNLP 2025) uses perturbation attribution; Agentic-R (arXiv 2026) uses binary EM; Q-RAG (ICLR 2026 Oral) uses factorized Q-values; UAE (arXiv 2604.22722, April 2026) trains a DeBERTa RM on perplexity-reduction utility with Utility-Modulated InfoNCE distillation. All evaluated on standard QA, none on BRIGHT. UAE is RARE's closest methodological ancestor — RARE replaces its outcome-based RM with a process-based PRM and targets reasoning-intensive domains.\n\n**Reasoning-intensive retrieval**: On BRIGHT, retriever-only SOTA: RaDeR 39.2 nDCG@10 (EMNLP 2025, MCTS synthetic data); ReasonEmbed 38.1 (arXiv 2025, ReMixer synthetic data + RI-InfoNCE); BGE-Reasoner-Embed-Qwen3-8B 37.1 in bi-encoder mode; Revela (arXiv 2506.16552) competitive via self-supervised LM with ~1000x less data. Full pipeline DIVER (arXiv 2508.07995) reaches 46.8. All use synthetic contrastive data or self-supervised signals — none use a learned RM targeting reasoning-chain quality.\n\n**Reasoning embedding via CoT augmentation**: Large Reasoning Embedding Models (LREM, arXiv 2510.14321, 2025) embed reasoning by using Query-CoT-Item triplets as training data and RL-refined reasoning trajectories. LREM treats CoT as input augmentation to the embedding model; RARE treats reasoning-chain quality as a soft training label via PRM scoring. These are orthogonal approaches: LREM modifies what the embedding model sees, RARE modifies what the embedding model optimizes for.\n\n**Reasoning injection taxonomy — three insertion points**: (1) **Query-time**: SmartSearch (arXiv 2601.04888) uses PRM for query refinement; BRIGHT's own CoT-augmented queries yield up to +12.2 nDCG. (2) **Inference-time**: ReasonRank (arXiv 2508.07050) uses LRM reranking (40.8 nDCG@10, 32B); ReARTeR (arXiv 2501.07861, SIGIR 2025) uses PRM+PEM for reasoning refinement in RAG. (3) **Training-time**: RARE injects process supervision into bi-encoder training via PRM-guided distillation — preserving inference-time efficiency.\n\n**Concurrent work**: RICE-PO (arXiv 2605.26352, May 2026) optimizes LLM retrieval policies, not bi-encoder embeddings. 'Retrieval, Reward, and Training Protocols' (arXiv 2605.27881, May 2026) finds simple outcome rewards competitive for search agents — but this finding pertains to agentic pipelines where reasoning is delegated to the LLM; in bi-encoder training, reasoning utility must be internalized in the embedding space.\n\n**PRM foundations**: ThinkPRM (arXiv 2504.16828, 2025) shows generative PRMs need only ~1K examples. Reward-RAG (arXiv 2024) uses RMs for generation quality, not retriever training. ReasonIR (arXiv 2025) trains retrievers for reasoning via synthetic data without learned RMs.\n\n## Proposed Approach\n\n**RARE** (Reasoning-Aware Reward-modeled Embeddings): a three-stage pipeline bringing process supervision to dense retriever training.\n\n**Stage 1 — Multi-Domain Reasoning-Utility PRM**: Fine-tune a generative PRM on DeepSeek-R1-Distill-Qwen-7B (~1.2K–2K examples). Data construction via **paired reasoning comparison**: for each (q, d) pair, prompt DeepSeek-R1 to generate reasoning chains with and without document d; score reasoning-chain quality delta via outcome correctness + chain coherence (step validity, intermediate conclusion soundness), yielding a continuous reasoning-utility label. Sample 100–200 pairs per domain from external corpora: Proof Wiki + MATH train set (math), filtered StackOverflow (coding), S2ORC subsets (science/economics/psychology), legal case databases (law). Total: ~1.2K–2.4K labeled pairs covering BRIGHT's 12 domains. Validate silver labels against 250 human-annotated pairs (~20 per domain), targeting Spearman ρ ≥ 0.7. Report per-domain PRM scoring quality.\n\n**Stage 2 — Document Scoring**: Apply trained PRM to candidate documents from domain-matched external corpora (not BRIGHT evaluation data). Pre-filter candidates via BM25 top-500 per query to control inference cost. Estimated scoring cost: ~50K–100K (q,d) pairs × ~0.5s per pair on A100 ≈ 7–14 GPU-hours.\n\n**Stage 3 — Embedding Distillation**: Distill PRM scores into Qwen3-Embedding-8B via Utility-Modulated InfoNCE (UAE's loss formulation), where contrastive weights reflect process-based reasoning utility.\n\n## Evaluation Plan\n\n**Benchmarks**: (1) BRIGHT (ICLR 2025) — primary, all 12 domains with per-domain nDCG@10 and Recall@1/5/10/100; (2) BEIR subset (NQ, HotpotQA, FiQA, SciFact, TREC-COVID) — regression test for general retrieval performance.\n\n**Baselines** (9 methods):\n1. RaDeR (EMNLP 2025) — MCTS synthetic data, retriever-only SOTA\n2. ReasonEmbed (arXiv 2025) — ReMixer synthetic data\n3. BGE-Reasoner-Embed-Qwen3-8B — same backbone family\n4. Revela (arXiv 2506.16552) — self-supervised, no synthetic pairs\n5. ReasonIR-8B (arXiv 2025)\n6. UAE-style perplexity-reduction RM (reimplementation on BRIGHT) — direct outcome-vs-process comparison\n7. UAE-style with 7B RM (capacity-controlled variant) — isolates signal type from RM capacity\n8. Qwen3-Embedding-8B with CoT-augmented queries (no training) — zero-cost query-time alternative\n9. Qwen3-Embedding-8B standard contrastive training (no RM)\n\n**Ablation studies** (6 axes):\n- Signal type: process-based PRM vs. outcome-based binary EM vs. perplexity-reduction RM — core claim validation\n- Loss function: Utility-Modulated InfoNCE vs. standard InfoNCE vs. margin-based loss\n- PRM data scale: 500 / 1K / 2K / 4K examples\n- PRM backbone size: DeepSeek-R1-Distill-Qwen-1.5B vs. 7B\n- Domain coverage: math+coding only vs. all 12 domains — cross-domain transfer test\n- Per-domain analysis: identify which reasoning types benefit most from process supervision\n\n**RM Quality Analysis** (core assumption validation):\n- Annotate 250 BRIGHT positive documents (~20 per domain) with 2 annotators on a continuous utility-source scale (pure evidence ↔ pure scaffolding). Operational criterion: if removing all answer-matching content leaves the document still reasoning-helpful → scaffolding end. Target Cohen's Kappa ≥ 0.7.\n- Verify that PRM scores correlate more strongly with scaffolding-end ratings than outcome-based utility scores do.\n- Report Spearman/Kendall correlation between PRM scores and downstream reasoning improvement. Use bootstrapped 95% CIs.\n- Qualitative case studies: PRM high-score vs. low-score documents across representative domains.\n\n**Downstream reasoning evaluation**: Retrieve top-k documents (k=5, 10) using each retriever, feed to Qwen2.5-72B-Instruct with unified prompt (\"Given the following documents, solve the problem step by step\"). Measure reasoning accuracy per domain (exact match for math, pass@1 for coding, F1 for others). All retrievers share identical downstream LLM and prompt.\n\n**Reproducibility**: 3 random seeds, mean ± std. Full compute budget in A100 GPU-hours: PRM training (~1–2h), document scoring (~7–14h), embedding training (~TBD). Compute-normalized comparison with RaDeR (MCTS cost) and ReasonEmbed (82K synthesis cost).\n\n## Hypothesized Contributions\n\n(1) **Conceptual**: First application of process supervision to dense retriever training, demonstrating that document utility lies on a continuous spectrum that outcome supervision systematically under-explores.\n(2) **Empirical**: RARE targets retriever-only SOTA on BRIGHT (>39.2 nDCG@10) while answering whether bi-encoder representations can encode reasoning utility — a high-order semantic property beyond lexical/semantic similarity.\n(3) **Methodological**: The process supervision signal, unlike synthetic contrastive data, is a learned continuous scorer transferable across domains without domain-specific data regeneration.\n\n## Key References\n\n- Process Reward Models That Think (ThinkPRM, arXiv 2504.16828, 2025)\n- Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training (ICLR 2026)\n- Aligning Dense Retrievers with LLM Utility via Distillation (UAE, arXiv 2604.22722, April 2026)\n- Training a Utility-based Retriever Through Shared Context Attribution (SCARLet, EMNLP 2025)\n- RaDeR: Reasoning-aware Dense Retrieval Models (EMNLP 2025)\n- ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval (arXiv 2025)\n- BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval (ICLR 2025)\n- Agentic-R: Learning to Retrieve for Agentic Search (arXiv 2026)\n- Reward-RAG: Enhancing RAG with Reward Driven Supervision (arXiv 2024)\n- ReasonIR: Training Retrievers for Reasoning Tasks (arXiv 2025)\n- RICE-PO: Turning Retrieval Interactions into Credit Signals (arXiv 2605.26352, May 2026)\n- Retrieval, Reward, and Training Protocols (arXiv 2605.27881, May 2026)\n- ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability (arXiv 2508.07050)\n- SmartSearch: Process Reward-Guided Query Refinement (arXiv 2601.04888, Jan 2026)\n- BGE-Reasoner-Embed-Qwen3-8B (BAAI, 2025)\n- Revela: Dense Retriever Learning via Language Modeling (arXiv 2506.16552, 2025)\n- DIVER: A Multi-Stage Approach for Reasoning-intensive IR (arXiv 2508.07995, 2025)\n- Large Reasoning Embedding Models (LREM, arXiv 2510.14321, 2025)\n- ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding (arXiv 2501.07861, SIGIR 2025)\n- A Survey of Process Reward Models (arXiv 2510.08049, 2025)"
}
````

---

### Runtime record

_source line 2 · 2026-05-30T07:45:47.216Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:45:47.216Z",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-30T07:45:47.229Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have a thorough understanding of the landscape. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- BRIGHT (ICLR 2025, arXiv 2407.12883): 首个推理密集型检索基准，1,384 queries 跨 12 领域。SOTA 模型在 MTEB 上 59.0 nDCG@10 但 BRIGHT 上仅 18.3，证明推理密集型检索是未解决的难题。RARE 以此为主评测平台，方向正确。
- RaDeR (EMNLP 2025, arXiv 2505.18405): 使用 MCTS 生成检索增强推理轨迹 + 自反思相关性评估，生成合成训练数据。bi-encoder-only SOTA 39.2 nDCG@10。RARE 的直接竞争对手，但方法论不同（合成数据 vs. 学习型 RM）。
- ReasonEmbed (arXiv 2510.08252): 提出 ReMixer 合成 82K 训练样本 + Redapter 自适应训练算法，Qwen3-8B 骨干达 38.1 nDCG@10。另一个合成数据路线竞争者。
- Q-RAG (ICLR 2026 Oral, arXiv 2511.07328): 将检索建模为 MDP，用 TD 学习训练嵌入器的 Q 值，聚焦多步检索。方法论上属于 outcome supervision 范畴，单 A100 训练。
- UAE (arXiv 2604.22722, April 2026): 使用困惑度降低作为实用性信号，通过 Utility-Modulated InfoNCE 蒸馏到 bi-encoder。RARE 的最近方法论祖先——RARE 本质上将 UAE 的 outcome RM 替换为 process RM。
- ThinkPRM (arXiv 2504.16828, 2025): 证明生成式 PRM 仅需 ~1K 样本即可训练，在 ProcessBench/MATH-500/AIME 上超越判别式 PRM。为 RARE 的 Stage 1 提供技术基础和数据效率先例。
- LREM (arXiv 2510.14321, 2025): 用 Query-CoT-Item 三元组 + RL 精化推理轨迹训练推理嵌入。与 RARE 正交：LREM 修改嵌入模型的输入，RARE 修改嵌入模型的优化目标。
- ReARTeR (SIGIR 2025, arXiv 2501.07861): 使用 PRM+PEM 在推理时做过程奖励引导的精化。PRM 用于生成端，非检索器训练。
- Revela (arXiv 2506.16552): 自监督 LM 训练检索器，无标注数据，~1000x 更少数据量在 BRIGHT/BEIR 上有竞争力。
- DIVER (arXiv 2508.07995): 多阶段 pipeline 达 46.8 nDCG@10，LATTICE 达 46.7-49.1。但均非 bi-encoder-only 方法。
- BGE-Reasoner-Embed-Qwen3-8B (BAAI, 2025): bi-encoder 模式 37.1 nDCG@10，基于合成数据微调。

- 调研总结: 推理密集型检索是 2025-2026 年活跃的前沿方向，bi-encoder SOTA 约 39.2 nDCG@10 (RaDeR)。现有方法均使用合成对比数据或 outcome 信号——无任何工作将 process supervision (PRM) 引入检索器训练。这个空白是真实存在的。但竞争激烈，该领域 6 个月内涌现了大量新方法。

【整体印象】:
作为审稿人的第一反应是 **weak accept 倾向**。这是一篇定位清晰、motivation 有说服力的 proposal。"将 process supervision 引入 dense retriever training"这个 gap 是真实的——我在调研中确认没有现有工作做过这件事。概念贡献（document utility 连续谱）提供了有洞察力的理论框架。评估方案异常完整（9 baselines、6 ablation 轴、RM 质量分析、下游推理评测），在 proposal 阶段就展示了严谨的实验思维。

但核心方法论本质上是"在 UAE 框架中用 PRM 替换 outcome RM"，这使得贡献的增量性值得关注。此外，能否在仅 ~1.2K-2.4K 样本下训练出跨 12 个异质领域（数学/编程/经济/心理学/法律等）泛化良好的 PRM 存在不确定性。最终的价值完全取决于实验能否证明：PRM 信号确实捕获了 outcome 信号遗漏的推理脚手架文档效用，且这种捕获转化为可测量的检索改进。

【核心贡献】:
核心贡献是**首次将 process supervision (PRM) 引入 dense retriever 训练**，提出文档效用是一个从"直接证据"到"推理脚手架"的连续谱，并论证 process reward 信号可以捕获 outcome 信号系统性忽略的推理脚手架端效用。

贡献价值评估：
- 概念层面：有明确的洞察力，"document utility spectrum"框架为理解检索效用提供了新视角
- 方法层面：中等——本质上是组合现有组件（ThinkPRM + UAE 的 Utility-Modulated InfoNCE），而非设计全新架构
- 潜在影响力：如果实验成功验证假设，将为推理密集型检索开辟一条新的研究路线（learned process-based RM vs. synthetic contrastive data），影响面可观

【方法合理性】:
方法整体上合理，但存在几个值得审视的问题：

1. **三阶段 pipeline 设计合理**：PRM 训练 → 文档打分 → 嵌入蒸馏的流程清晰，每一步都有现有工作支撑（ThinkPRM 证明 ~1K 样本可训练生成式 PRM；UAE 证明 Utility-Modulated InfoNCE 可蒸馏效用信号）。

2. **更简单的替代方案？** 
   - 最直接的替代是使用 outcome-based RM 在 BRIGHT 上训练（proposal 中已作为 baseline 6-7 考虑），这本身说明作者有自觉
   - BRIGHT 自带的 CoT-augmented queries 已能提升 +12.2 nDCG，这是零成本方案（proposal 已作为 baseline 8）
   - RaDeR 的 MCTS 合成数据方法在 bi-encoder 上已达 39.2，且不需要训练 RM
   - 这些替代方案的存在意味着 RARE 必须展示显著的增量收益才能证明额外复杂度的合理性

3. **PRM 跨域泛化的关键假设**：
   - 100-200 examples/domain × 12 domains ≈ 1.2K-2.4K 总量，ThinkPRM 的 ~1K 先例主要在数学领域验证
   - 法律、心理学、经济学的"推理链质量"评估与数学差异巨大——PRM 能否在如此异质的领域间泛化是核心技术风险
   - Proposal 设计了 250 对人工标注验证（Spearman ρ ≥ 0.7），这是好的，但阈值可能过于乐观

4. **bi-encoder 的表达能力**：核心问题是 bi-encoder 是否有足够的表达能力在嵌入空间中编码"推理效用"这样的高阶语义属性。这不是一个可以预先保证的假设，但如果失败，也是有价值的负面结果。

【5 维度打分】:

1. 研究问题: 【强】
   — 推理密集型检索是 2025-2026 年检索领域最热门的前沿方向之一（BRIGHT ICLR 2025、RaDeR EMNLP 2025、Q-RAG ICLR 2026 Oral）。现有方法均依赖 outcome supervision 或合成对比数据，将 process supervision 引入检索器训练是一个真正未被探索的方向。研究问题（"bi-encoder 能否编码推理效用？"）有明确的 yes/no 答案，且无论结果都有科学价值。问题的重要性和时效性都很强。

2. 方法与创新: 【中】
   — 优点：novelty claim 成立——调研确认无现有工作将 PRM 应用于 retriever training。与 LREM（修改输入）、ReARTeR（推理时使用 PRM）等工作有清晰的差异化定位。
   — 不足：方法论上是"UAE framework + PRM 替换 outcome RM"，属于组件替换而非方法创新。三阶段 pipeline 每一步都直接借用现有技术（ThinkPRM 的训练范式、UAE 的 Utility-Modulated InfoNCE）。与 Q-RAG 的 RL-based value learning、RaDeR 的 MCTS 探索相比，方法论新颖度偏低。一个审稿人可能会问："如果核心贡献是将 PRM 信号插入已有框架，这是否更像一个有价值的实验研究（empirical study）而非方法贡献？"

3. 实验设计: 【强】
   — 9 个 baselines 覆盖了该领域几乎所有重要竞争方法，包括直接对比（RaDeR、ReasonEmbed、BGE-Reasoner）、消融控制（UAE reimplementation、capacity-controlled variant）、零成本替代（CoT-augmented queries）。6 轴 ablation 设计周全，特别是 signal type ablation（process vs. outcome vs. perplexity-reduction）直接验证核心假设。RM Quality Analysis 包含人工标注、per-domain 分析、bootstrapped CIs，达到了一线顶会的实验标准。唯一缺失：未包含 LREM 作为 baseline（同样将推理融入嵌入，虽然机制不同）。3 random seeds + compute budget 报告体现了可复现性意识。

4. 可行性: 【中】
   — 计算资源合理：PRM 训练 ~1-2h A100、文档打分 ~7-14h、嵌入训练 TBD 但预计适中，单台 A100 可完成核心实验。
   — 主要风险点：(a) 跨 12 领域的 PRM 质量——特别是非 STEM 领域（法律、心理学、经济学）的推理链质量评估远比数学主观，100-200 examples 可能不足以捕获这些领域的推理模式；(b) paired reasoning comparison 数据构造需要 DeepSeek-R1 大量推理生成，实际成本可能高于估计；(c) 目标 Spearman ρ ≥ 0.7 在异质领域间可能过于乐观，如果某些领域达不到，需要有应急方案。
   — 总体可执行，但存在中等程度的技术风险，且 proposal 未充分讨论失败预案。

5. 写作与呈现: 【强】
   — Proposal 结构清晰、论证逻辑严密。Related work 的定位非常精准，对 5 类相关工作的区分（outcome supervision、reasoning-intensive retrieval、CoT augmentation、reasoning injection taxonomy、concurrent work）有很强的组织能力。"Reasoning injection taxonomy"的三插入点分类（query-time / inference-time / training-time）是一个有效的贡献。具体例子（BRIGHT coding/economics/math 任务中的 answer-containing vs. reasoning-scaffolding 文档）增强了 motivation 的说服力。参考文献覆盖全面且时效性极强（含 2026 年 5 月的最新工作）。

【概率估计】: [28% - 40%] 中位 34%

【估计理由】:
推理过程如下：
- **加分因素**：(1) 研究问题在热门前沿方向上占据真实空白（process supervision → retriever training），novelty claim 经调研确认成立；(2) 评估方案在 proposal 阶段就达到了一线顶会标准，9 baselines + 6 ablation 轴 + RM 质量验证 + 下游推理评测，审稿人难以在实验设计上挑出重大缺陷；(3) 写作和 positioning 质量高，相关工作覆盖全面且分类精准；(4) 选题时效性好，2025-2026 年推理密集型检索是热门方向。
- **减分因素**：(1) 方法论核心是组件替换（PRM 替换 outcome RM in UAE framework），创新幅度有限，可能被视为 empirical study 而非 methodological contribution；(2) PRM 跨 12 个异质领域的泛化是未经验证的核心假设，数据量（100-200/domain）较小；(3) 该领域竞争极其激烈，6 个月内涌现 RaDeR、ReasonEmbed、BGE-Reasoner、Revela、DIVER 等大量工作，RARE 需要在实验中展示显著的增量收益才能脱颖而出；(4) 目标 >39.2 nDCG@10 的 margin 如果很小（<1-2 点），说服力有限。
- **综合判断**：这是一篇 solid 的 proposal，方向正确、执行方案完备，但核心方法论创新度中等。在 AAAI 这样的顶会，仅有良好的实验设计和清晰的 gap 可能不够——还需要方法上的深度或出乎意料的强实验结果。如果实验结果能显著超越 BRIGHT SOTA 并清晰验证 process vs. outcome supervision 的差异，中稿概率可以上探至 40%；如果实验提升有限或 PRM 泛化不佳，概率会下探至 28% 左右。

【主要风险】:
1. **方法被视为增量性组件替换**：审稿人可能认为"在 UAE 框架中用 PRM 替换 outcome RM"不构成足够的方法论贡献，而更像一个 ablation study 或 empirical investigation。需要通过充分的分析（RM Quality Analysis、per-domain breakdown）来论证 process supervision 带来的质的差异，而非仅仅量的提升。
2. **PRM 跨域泛化失败**：如果 PRM 在非 STEM 领域（法律、心理学等）的推理效用评分质量显著下降（Spearman ρ < 0.5），整个框架在 BRIGHT 全 12 域上的综合性能可能无法超越基于大规模合成数据的竞争方法（RaDeR 82K+ 合成 pairs）。

【实施评估】:
  - 计算资源: 中等偏低。PRM 训练 ~1-2h A100，文档打分 ~7-14h A100，嵌入训练预计 ~8-24h A100（基于 Qwen3-8B 规模），总计 ~20-40h A100。单卡可完成核心实验，包含完整 ablation 预计需 ~100-200h A100。
  - 数据需求: 需从外部语料（Proof Wiki、MATH train、StackOverflow、S2ORC、法律案例库）构造 ~1.2K-2.4K paired reasoning comparison 数据。需 BRIGHT benchmark 评测数据（公开可用）。BEIR 子集（公开可用）。
  - 人工介入: 需要 250 对文档的人工标注（2 标注员，~20/domain），用于 PRM 验证和 utility-source 量表评估。标注工作量中等（约 2-4 人天）。
  - 训练需求: 三阶段训练——(1) PRM fine-tuning on DeepSeek-R1-Distill-Qwen-7B；(2) PRM inference for document scoring；(3) Qwen3-Embedding-8B 的 contrastive distillation训练。均需 GPU 但规模适中。
  - 新 Benchmark: 不需要构建新 benchmark，使用现有 BRIGHT + BEIR。但需构建 PRM 训练数据集（paired reasoning comparison）和人工标注集，这些可作为数据贡献。
  - 预估周期: 数据构造 2-3 周，PRM 训练+验证 1 周，文档打分 1-2 天，嵌入训练+调参 2-3 周，完整实验+ablation 2-3 周，写作 2-3 周。总计约 8-12 周，适合 AAAI 2026 投稿周期。
```

Sources:
- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883)
- [RaDeR: Reasoning-aware Dense Retrieval Models](https://arxiv.org/abs/2505.18405)
- [ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2510.08252)
- [Q-RAG: Long Context Multi-step Retrieval via Value-based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)
- [UAE: Aligning Dense Retrievers with LLM Utility via Distillation](https://arxiv.org/abs/2604.22722)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [LREM: Large Reasoning Embedding Models](https://arxiv.org/abs/2510.14321)
- [ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding](https://arxiv.org/abs/2501.07861)
- [Revela: Dense Retriever Learning via Language Modeling](https://arxiv.org/abs/2506.16552)
- [DIVER: A Multi-Stage Approach for Reasoning-intensive IR](https://arxiv.org/pdf/2508.07995)
- [BGE-Reasoner-Embed-Qwen3-8B](https://huggingface.co/BAAI/bge-reasoner-embed-qwen3-8b-0923)
- [A Survey of Reasoning-Intensive Retrieval](https://arxiv.org/html/2605.00063)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide my comprehensive evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:
- [BRIGHT (arXiv 2407.12883)] (ICLR 2025): 定义了 reasoning-intensive retrieval 的基准，1384 queries，12 domains。当前最佳 retriever-only nDCG@10 约 39.2 (RaDeR)，最佳全 pipeline 为 DIVER 的 46.8。
- [RaDeR (arXiv 2505.18405)] (EMNLP 2025): 用 MCTS 合成数据训练 reasoning-aware dense retriever，BRIGHT nDCG@10 ≈ 39.2，retriever-only SOTA。方法是合成对比数据，非 learned RM。
- [ReasonEmbed (arXiv 2510.08252)] (arXiv 2025): ReMixer 合成 82K 样本 + Redapter 自适应学习，BRIGHT nDCG@10 = 38.1。同样依赖合成对比数据。
- [BGE-Reasoner-Embed-Qwen3-8B] (BAAI, 2025): BRIGHT nDCG@10 = 37.1 (bi-encoder mode)，同系 backbone (Qwen3-8B)。
- [UAE (arXiv 2604.22722)] (April 2026): 基于 perplexity-reduction 的 utility RM + Utility-Modulated InfoNCE 蒸馏到 bi-encoder。评估在 QASPER 上，未涉及 BRIGHT。RARE 的最直接方法论前身。
- [Q-RAG (arXiv 2511.07328)] (ICLR 2026 Oral): Value-based RL 训练 embedder 做 multi-step retrieval，评估在 BabiLong/RULER 长上下文 benchmark，非 BRIGHT。
- [SCARLet (arXiv 2504.00573)] (EMNLP 2025): 扰动归因法估计 passage-level utility，训练 retriever。10 个数据集评估。
- [ThinkPRM (arXiv 2504.16828)] (arXiv 2025): 生成式 PRM，仅需 ~1K 合成验证 CoT + 8K process labels 即可超越判别式 PRM。支持 R1-Distill-Qwen-1.5B/7B/14B/QwQ-32B。
- [LREM (arXiv 2510.14321)] (arXiv 2025): Query-CoT-Item triplets + RL 精炼推理轨迹做 reasoning embedding。修改 embedding 模型的输入端，与 RARE 修改训练信号端正交。
- [Revela (arXiv 2506.16552)] (arXiv 2025): 自监督 LM 目标训练 retriever，无需标注/合成 query-doc 对，在 BRIGHT 上超越更大监督模型，~1000x 更少数据。
- 调研总结: Reasoning-intensive retrieval 是 2025-2026 年的活跃方向，当前方法以合成对比数据（RaDeR, ReasonEmbed）和自监督学习（Revela）为主，outcome-based utility RM（UAE, SCARLet）已在标准 QA 上验证但未扩展到 BRIGHT。**将 process supervision (PRM) 引入 dense retriever 训练这一交叉点确实是未被占据的空白。**

【整体印象】:
这是一份极为成熟、定位精准的 proposal。作为审稿人，我的第一反应是 **borderline accept, leaning positive**。核心吸引力在于：(1) 它识别出了一个真实且未被填补的研究空白——process supervision 用于 retriever 训练；(2) 概念贡献（document utility 连续谱）有独立价值且可测试；(3) 评估方案之详尽远超多数投稿（9 baselines、6 ablation axes、human annotation、RM quality validation）。主要犹豫在于：**核心技术贡献本质上是 UAE pipeline 中将 outcome RM 替换为 PRM 的 principled component swap**，方法创新的 "跨度" 有限。是否 accept 取决于实验能否充分验证概念贡献——即 PRM 信号确实捕获了 outcome 信号遗漏的 reasoning-scaffolding utility。

【核心贡献】:
1. **概念贡献**（最核心）：提出 document utility 的 answer-containing ↔ reasoning-scaffolding 连续谱，论证 outcome supervision 系统性低估谱的 scaffolding 端，而 process supervision 可弥补。这是一个可证伪的理论命题，如果实验验证成功，对 retriever 训练范式有实质推动。
2. **方法贡献**：首次将 PRM-based process supervision 作为 dense retriever 的训练信号（via distillation），保持 bi-encoder 的推理效率。
3. **对领域的价值**：中等偏高。如果概念命题成立，它不仅改进 BRIGHT 性能，还为 retriever 训练信号的设计提供了新维度（从 "文档是否有用" 细化到 "文档在哪个层面有用"）。但如果实验显示 PRM 信号与 outcome 信号高度相关（即 scaffolding 文档的 outcome utility 也不低），概念贡献会被削弱。

【方法合理性】:
方法整体合理，三阶段 pipeline 的每个组件都有充分的先行工作支撑（ThinkPRM → PRM 训练；UAE → 蒸馏损失）。但需审视两个关键点：

1. **PRM 训练数据构造的可靠性**：paired reasoning comparison（有/无文档的推理链质量差异）的信噪比可能有问题。LLM 的推理链对单个文档的响应可能高度随机——同一文档的 reasoning-utility label 在不同 sampling 下可能差异很大。proposal 提到 250 human annotations (ρ≥0.7) 作为验证，这是好的，但 ρ=0.7 是一个中等门槛。
2. **更简单的替代方案**：(a) 直接用 ThinkPRM 作为 reranker（类似 ReasonRank 但更轻量），不需要蒸馏到 bi-encoder，可能更 cost-effective；(b) 直接用 CoT-augmented queries（proposal 自己列为 baseline 8，BRIGHT 原文报告 +12.2 nDCG）作为零成本替代。Proposal 需要在实验中充分证明蒸馏到 embedding space 的必要性——如果 PRM reranking 或 CoT queries 已经能达到类似效果，training-time 注入的价值就大打折扣。

【5 维度打分】:
  1. 研究问题: 【强】 — Process supervision 用于 retriever 训练是一个清晰的未探索方向。Document utility 连续谱的概念框架有理论价值且可测试。问题的成立不依赖于特定假设——即使最终 PRM 信号改进有限，negative result 本身也有信息量（说明 bi-encoder 的表征瓶颈或 scaffolding utility 的可学习性边界）。
  
  2. 方法与创新: 【中】 — 方法合理但创新跨度有限。核心操作是将 UAE 的 outcome RM 替换为 PRM（ThinkPRM 架构），蒸馏损失直接复用 Utility-Modulated InfoNCE。与 UAE 的差异仅在 RM 信号类型，与 ThinkPRM 的差异仅在应用场景。每个组件都是成熟技术的组合（"bridging" 型贡献），没有新的损失函数、架构或训练范式。调研中 RaDeR（MCTS 合成数据）和 ReasonEmbed（ReMixer + Redapter）在方法层面有更大的原创性。不过，"正确的组合"在正确的问题上仍有价值——关键在于实验能否证明这个组合产生了非平凡的 emergent effect。

  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点。9 个 baselines 覆盖了领域内几乎所有竞争方法（RaDeR, ReasonEmbed, BGE-Reasoner, Revela, ReasonIR, UAE reimpl, capacity-controlled UAE, CoT-query, standard contrastive）。Baseline 6-7（UAE reimpl + capacity-controlled variant）是精心设计的——直接隔离信号类型 vs. RM 容量的贡献，这正是验证核心概念贡献所需的对比。6 轴 ablation 全面且有重点。RM Quality Analysis（250 human annotations, utility-source scale, Spearman/Kendall + bootstrap CI）直接验证核心假设。Downstream reasoning evaluation（统一 LLM + prompt，k=5,10）填补了 retrieval metric 与实际推理效果之间的 gap。3 seeds + compute-normalized comparison 体现了方法论的严谨。与 RaDeR 和 ReasonEmbed 的论文相比，这个评估方案的完整度和控制度都更高。

  4. 可行性: 【强】 — 资源需求非常合理：PRM 训练 1-2h A100、document scoring 7-14h A100、embedding 训练 TBD 但基于 UAE pipeline 预计中等。总计 <30 GPU-hours（不含 embedding 训练）。PRM 数据仅需 1.2K-2.4K labeled pairs + 250 human annotations，human annotation 量可控（~20 per domain × 12 domains）。不需要构建新 benchmark。Backbone 选择（DeepSeek-R1-Distill-Qwen-7B, Qwen3-Embedding-8B）均为公开模型。Pipeline 的每一步都有参考实现（ThinkPRM 开源、UAE 方法公开）。唯一不确定性是 multi-domain PRM 的泛化质量——12 个 domain 各 100-200 pairs 是否足够需要实验验证，但 ThinkPRM 的 ~1K 数据效率结论提供了信心。

  5. 写作与呈现: 【强】 — Proposal 的写作水准极高。研究动机从 outcome vs. process supervision 的差异自然推导，概念贡献（连续谱）清晰且有具体例子支撑。Research landscape 的梳理极为全面——不仅覆盖了直接竞争者，还建立了 "reasoning injection taxonomy"（query-time / inference-time / training-time）来定位自己的方法。与 concurrent work 的辨析（RICE-PO, Retrieval/Reward/Training Protocols）显示了对领域前沿的实时跟踪。Hypothesized contributions 的措辞恰当——用 "targets" 而非 "achieves" SOTA，体现了 proposal 阶段的适度性。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
**上行因素**：(1) 研究问题清晰且有真实空白（process supervision → retriever training 无先行工作）；(2) 评估方案极为完整，显著降低了 "实验不充分" 这一常见拒稿原因的概率；(3) 概念贡献（连续谱 + process/outcome 信号差异）如果被实验验证，有独立的理论贡献价值；(4) 可行性高，不存在 "做不出来" 的风险。

**下行因素**：(1) **核心方法创新有限** — 审稿人可能评价为 "UAE + ThinkPRM 的直接组合"，缺乏方法论层面的原创贡献。在 AAAI 这样的顶会，仅凭 "正确的组合" 可能不够，尤其当组合本身没有产生新的技术挑战需要解决时。(2) **BRIGHT 基准的规模较小**（1384 queries），在小 benchmark 上的 SOTA claim 说服力相对有限，且其他工作已接近 39-40 nDCG@10，留给改进的 headroom 不大。(3) **概念贡献存在被反驳的风险** — 如果实验显示 outcome utility 和 process utility 高度相关（Spearman ρ>0.85），连续谱的区分价值就被削弱，此时 RARE 退化为 "换了一种方式估 utility 的 UAE variant"。(4) **缺少与 reranking 方案的 end-to-end 成本效益对比** — 如果直接用 PRM 做 reranking 就能达到或超过蒸馏到 bi-encoder 的效果，training-time 注入的动机就不成立。

**中位 35% 的推理**：这是一篇 solid 的投稿，问题和评估都很好，但方法创新的 "ceiling" 限制了它。在典型的 AAAI 评审中，它可能获得 1 个 weak accept（被概念贡献和实验设计打动）、1 个 borderline（认可问题但质疑方法创新）、1 个 weak reject（认为是 incremental combination），最终需要 meta-reviewer 裁定。35% 反映了 "有实质性贡献但不是 clear accept" 的位置。

【主要风险】:
1. **"Incremental combination" 评价**：核心方法被审稿人视为 UAE pipeline 的 RM 组件替换，缺乏独立的方法论贡献（无新损失函数、无新架构、无新训练范式），这是最可能的拒稿理由。
2. **Core hypothesis 未被充分验证或被反驳**：如果 PRM scores 与 outcome-based utility scores 在 BRIGHT 文档上的相关性很高（即 outcome supervision 并未 "系统性低估" scaffolding 文档），整篇论文的概念基础就会动摇。250 pairs 的 human annotation 可能不足以在统计上有力地区分两种信号。

【实施评估】:
  - 计算资源: 低-中。PRM 训练 ~1-2h A100，文档打分 ~7-14h A100，embedding 蒸馏预估 ~8-16h A100（基于 UAE 规模推测）。总计 ~20-35 A100-hours，远低于 RaDeR (MCTS) 和 ReasonEmbed (82K synthesis) 的成本。
  - 数据需求: 中。需要从 ProofWiki, MATH, StackOverflow, S2ORC, legal databases 等外部语料采集 1.2K-2.4K paired reasoning samples + BM25 top-500 candidate 文档 (~50K-100K pairs)。无需新数据集收集，但 multi-domain 数据准备有一定工程量。
  - 人工介入: 低-中。250 human annotations（2 annotators, ~20 per domain），用于 PRM quality validation 和 utility-source scale 标注。估计 ~40-60 人时。
  - 训练需求: 是，需要训练 PRM (fine-tune DeepSeek-R1-Distill-Qwen-7B) 和 embedding model (fine-tune Qwen3-Embedding-8B)。均为 fine-tuning 而非从头训练。
  - 新 Benchmark: 否。使用现有 BRIGHT + BEIR subset。但需要构建 multi-domain PRM 训练数据和 human annotation 数据，这些可作为资源贡献发布。
  - 预估周期: 约 8-12 周。数据准备 2-3 周，PRM 训练与验证 1-2 周，文档打分 1 周，embedding 训练与 ablation 实验 2-3 周，downstream evaluation + 分析 1-2 周，写作 2 周。
```

Sources:
- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883)
- [RaDeR: Reasoning-aware Dense Retrieval Models](https://arxiv.org/abs/2505.18405)
- [ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2510.08252)
- [UAE: Aligning Dense Retrievers with LLM Utility via Distillation](https://arxiv.org/abs/2604.22722)
- [Q-RAG: Long Context Multi-step Retrieval via Value-based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [SCARLet: Training a Utility-based Retriever Through Shared Context Attribution](https://arxiv.org/abs/2504.00573)
- [LREM: Large Reasoning Embedding Models](https://arxiv.org/abs/2510.14321)
- [Revela: Dense Retriever Learning via Language Modeling](https://arxiv.org/abs/2506.16552)
- [BGE-Reasoner-Embed-Qwen3-8B](https://huggingface.co/BAAI/bge-reasoner-embed-qwen3-8b-0923)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Here is my assessment:

---

```
【阶段】: Triage

【领域调研】:
- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883) (ICLR 2025): 定义了reasoning-intensive retrieval任务，初始SOTA仅24.3 nDCG@10，是RARE的主要评测平台。
- [RaDeR: Reasoning-aware Dense Retrieval Models](https://aclanthology.org/2025.emnlp-main.1011/) (EMNLP 2025): 当前retriever-only BRIGHT SOTA (~39.2 nDCG@10)，使用MCTS生成合成数据。RARE的直接竞争者。
- [ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2510.08252) (arXiv 2025): 使用ReMixer合成数据+RI-InfoNCE，BRIGHT上38.1 nDCG@10。另一直接竞争者。
- [BGE-Reasoner-Embed-Qwen3-8B](https://huggingface.co/BAAI/bge-reasoner-embed-qwen3-8b-0923) (BAAI 2025): bi-encoder模式37.1 nDCG@10，同backbone家族，关键baseline。
- [UAE: Aligning Dense Retrievers with LLM Utility via Distillation](https://arxiv.org/abs/2604.22722) (arXiv April 2026): RARE最近的方法论祖先——使用Utility-Modulated InfoNCE进行perplexity-reduction utility蒸馏。仅在QASPER上评测，未在BRIGHT上测试。RARE本质上是将UAE的outcome-based RM替换为process-based PRM。
- [Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training](https://arxiv.org/abs/2511.07328) (ICLR 2026 Oral): 使用RL（TD学习）训练embedder进行多步检索。证明了learned utility signals对检索有效，但方向不同（multi-step sequential retrieval vs. single-step reasoning-intensive retrieval）。
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828) (arXiv 2025): 证明了generative PRMs仅需~1K样本即可训练，是RARE Stage 1的技术基础。
- [SCARLet: Training a Utility-based Retriever Through Shared Context Attribution](https://arxiv.org/abs/2504.00573) (EMNLP 2025): 使用perturbation attribution估计passage-level utility。Outcome supervision的代表性工作。
- [ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding](https://arxiv.org/abs/2501.07861) (SIGIR 2025): 在inference-time使用PRM+PEM进行reasoning refinement。PRM用于RAG但在inference端而非training端，与RARE正交。
- [Revela: Dense Retriever Learning via Language Modeling](https://arxiv.org/abs/2506.16552) (arXiv 2025): 自监督方法，在BRIGHT上表现competitive，使用~1000x更少数据。
- [LREM: Large Reasoning Embedding Models](https://arxiv.org/abs/2510.14321) (arXiv 2025): 通过Query-CoT-Item triplets注入reasoning能力。RARE与其正交——LREM改变embedding模型看到什么，RARE改变embedding模型优化什么。
- [Agentic-R: Learning to Retrieve for Agentic Search](https://arxiv.org/abs/2601.11888) (arXiv 2026): 使用binary EM的outcome supervision训练retriever for agentic search。

- **调研总结**: Reasoning-intensive retrieval是2025-2026年的热门方向，BRIGHT上SOTA从24→39+快速演进。现有方法主要通过合成对比数据（RaDeR/ReasonEmbed）、self-supervised LM（Revela）或CoT增强输入（LREM/BGE-Reasoner）来提升性能。将process supervision（PRM）引入dense retriever training确实是一个尚未被填补的gap——现有PRM在retrieval中的应用限于query refinement（SmartSearch）和inference-time reranking/refinement（ReARTeR、ReasonRank），尚无人在training-time通过PRM指导bi-encoder学习。

【整体印象】:
作为审稿人，我的第一反应是这是一篇**定位精准、实验设计出色、但方法论增量偏轻**的投稿。Proposal对领域的梳理异常全面——对outcome supervision四个代表性工作、reasoning-intensive retrieval SOTA、reasoning injection taxonomy的三个插入点、以及concurrent work的区分都非常清晰，展现了作者对领域的深度理解。核心novelty claim（将process supervision引入retriever training）经调研确认成立。

但冷静审视，方法论的核心操作是"在UAE框架中将outcome-based RM替换为process-based PRM"，这个delta虽然conceptually motivated，但methodologically较thin。一个审稿人可能会问：这本质上只是换了一个reward signal的来源，而非提出新的训练范式。Conceptual contribution（document utility as continuous spectrum）虽然elegant，但更接近observation而非formalizable theory。

我会倾向于**borderline accept/weak reject**——如果实验结果强有力（显著超过SOTA，ablation清晰验证process vs. outcome的差异），可以接受；如果结果marginal，方法论创新不足以支撑。

【核心贡献】:
1. **概念贡献**：提出document utility存在从"直接证据"到"推理脚手架"的连续谱系，outcome supervision系统性地忽略了推理脚手架端——这是一个有价值的观察，但需要强有力的实验验证。
2. **方法贡献**：首次将process supervision引入dense retriever training，通过PRM-guided distillation将reasoning utility编码进bi-encoder表示。
3. **实验贡献**：在BRIGHT上提供了第一个process vs. outcome supervision的controlled comparison。

贡献的价值中等偏上。核心insight（process vs. outcome supervision for retriever training）是genuine的，但作为一个新research direction的开创性贡献还缺少足够的理论深度——更像是一个well-motivated engineering contribution。

【方法合理性】:
方法整体合理，但存在几个需要审视的点：

1. **PRM数据构建的可靠性**：通过"paired reasoning comparison"（有/无document d的reasoning chain质量差异）来构建training labels是方法的核心假设。这假设DeepSeek-R1能稳定地反映document对reasoning的影响——但LLM reasoning的randomness可能导致noise。Proposal设定了Spearman ρ ≥ 0.7的人工标注验证标准，这是合理的safeguard。

2. **更简单的替代方案**：一个reviewer可能会问——为什么不直接用reasoning chain的outcome improvement作为连续标签（而非binary EM），而需要额外训练一个PRM？即，outcome supervision的"连续化"版本是否已经能捕获大部分RARE声称的信号？Proposal的capacity-controlled UAE variant (Baseline 7) 部分地址了这个问题，但需要清晰展示process signal捕获的是outcome signal无法捕获的信息。

3. **Bi-encoder的表达瓶颈**：RARE声称bi-encoder可以编码"reasoning utility"这样的high-order semantic property。但bi-encoder的独立编码特性天然限制了它捕获query-document交互级推理关系的能力。这是一个fundamental tension，Proposal承认了但未充分讨论。

4. **与LREM的组合可能性**：LREM改变embedding model的输入（CoT-augmented），RARE改变优化目标（PRM scoring）。两者声称正交，但未讨论组合效果——这既是一个遗漏也可能是一个机会。

【5 维度打分】:

1. **研究问题**: 【中偏强】— 问题定义清晰且有价值。Reasoning-intensive retrieval是活跃方向，process supervision在retriever training中的缺位是real gap。但问题的"重要性"略受限于应用范围——BRIGHT虽然是标准benchmark，但reasoning-intensive retrieval在实际部署中的需求规模尚不明确。相比Q-RAG (ICLR 2026 Oral)这样定义新范式的工作，RARE更多是在已有范式内的refinement。

2. **方法与创新**: 【中】— Novelty claim经调研确认成立，无prior work将PRM用于retriever training。但方法论delta偏轻——核心操作是在UAE的Utility-Modulated InfoNCE框架中替换reward signal来源。与RaDeR的MCTS合成数据、Q-RAG的RL-based value learning、Revela的self-supervised LM相比，RARE的方法论创新幅度较小。UAE (arXiv 2604.22722) 已经建立了utility distillation的完整框架，RARE的创新集中在Stage 1的PRM训练和document utility spectrum的概念框架。

3. **实验设计**: 【强】— 这是Proposal最突出的优势。9个baselines（包括capacity-controlled variant用于公平比较）、6个ablation axes（信号类型、损失函数、数据规模、backbone大小、域覆盖、per-domain分析）、RM quality validation（250人工标注样本、inter-annotator agreement、correlation analysis）、downstream reasoning evaluation——实验设计的完备性在proposal阶段非常少见。特别值得注意的是Baseline 6（UAE-style on BRIGHT）和Baseline 7（capacity-controlled variant）的设置，直接回答了"是signal type还是RM capacity"的confounding问题。与RaDeR、ReasonEmbed等发表工作的实验设计相比，这里的ablation更加系统。

4. **可行性**: 【中偏强】— 计算需求合理（PRM训练1-2h，document scoring 7-14h on A100），数据构建规模适中（1.2K-2.4K labeled pairs），基于ThinkPRM的data-efficient PRM训练已被验证。主要风险是PRM数据质量——paired reasoning comparison依赖LLM的稳定性，可能需要多次采样取平均来降噪。另外，embedding training的compute cost标注为TBD，这是一个gap。

5. **写作与呈现**: 【强】— Proposal的组织结构清晰，positioning section是我见过的proposal中最全面的之一。Reasoning injection taxonomy（query-time / inference-time / training-time）的框架化非常有效。与concurrent work的区分（RICE-PO、Retrieval Reward and Training Protocols）表明作者持续跟踪领域。概念贡献（continuous spectrum）虽然thin，但表述清晰有力。

【概率估计】: [25% - 38%] 中位 31%

【估计理由】:
- **上行因素**：(1) Novelty claim confirmed——确实无人做过process supervision for retriever training；(2) 实验设计极为完备，若结果有力可构成solid empirical contribution；(3) 领域热度高，reasoning-intensive retrieval是2025-2026的焦点方向；(4) 与UAE/ThinkPRM的技术衔接自然，方案可行性高。
- **下行因素**：(1) 方法论增量偏轻——本质是"换reward signal"，缺乏architectural或training paradigm层面的创新；(2) 核心假设风险——bi-encoder能否真正编码reasoning utility是open question，如果实验结果marginal，paper缺少足够的方法创新来支撑；(3) 竞争激烈——RaDeR (39.2) 用MCTS、ReasonEmbed (38.1) 用大规模合成数据，RARE能否仅凭1.2K-2.4K PRM标注数据超越SOTA存疑；(4) conceptual contribution虽然elegant但thin——"continuous spectrum"更像observation而非theory。
- **中位31%的理由**：这是一篇方向正确、执行方案solid的工作，但方法创新深度不足以稳定进入accept区间。如果实验结果强有力（显著超SOTA + ablation清晰展示process vs. outcome差异），概率推向38%；如果结果marginal（与SOTA comparable但不显著优于），方法创新不足以弥补，概率滑向25%。AAAI的接收率通常在23-25%左右，这篇处于borderline位置。

【主要风险】:
1. **方法论增量不足**：如果reviewer认为"在UAE框架中换reward signal"不构成sufficient novelty，且实验结果未能decisively证明process > outcome supervision，paper可能因"incremental contribution"被拒。这是最大的单一风险。
2. **核心假设验证失败**：PRM scores能否有效指导bi-encoder学习reasoning utility是一个未经验证的假设。如果PRM标注质量不达标（Spearman ρ < 0.7）或PRM-guided training未能在BRIGHT上显著超过outcome-based baseline，核心叙事崩塌。

【实施评估】:
  - 计算资源: 中等偏低。PRM训练~1-2h A100，document scoring ~7-14h A100，embedding training TBD但基于Qwen3-8B fine-tuning预估10-20h A100。总计~30-40h A100，非常可控。
  - 数据需求: 中等。需要从Proof Wiki、MATH、StackOverflow、S2ORC等构建1.2K-2.4K标注对，需要DeepSeek-R1进行reasoning chain生成（大量inference calls），需要250条人工标注进行validation。
  - 人工介入: 需要2名标注员对250条BRIGHT正例文档进行utility-source标注（pure evidence ↔ pure scaffolding），规模可控但需要domain expertise（覆盖12个领域）。
  - 训练需求: 需要训练——(1) PRM fine-tuning on DeepSeek-R1-Distill-Qwen-7B; (2) Qwen3-Embedding-8B embedding distillation。两阶段训练，但规模适中。
  - 新 Benchmark: 不需要构建新benchmark。使用现有BRIGHT（primary）和BEIR subset（regression test）。
  - 预估周期: 4-6周。数据构建1-2周（含LLM inference），PRM训练+验证1周，embedding训练+评测1-2周，ablation+分析1周。
```

Sources:
- [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://arxiv.org/abs/2407.12883)
- [RaDeR: Reasoning-aware Dense Retrieval Models](https://aclanthology.org/2025.emnlp-main.1011/)
- [ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2510.08252)
- [BGE-Reasoner-Embed-Qwen3-8B](https://huggingface.co/BAAI/bge-reasoner-embed-qwen3-8b-0923)
- [UAE: Aligning Dense Retrievers with LLM Utility via Distillation](https://arxiv.org/abs/2604.22722)
- [Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training](https://arxiv.org/abs/2511.07328)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [SCARLet: Training a Utility-based Retriever Through Shared Context Attribution](https://arxiv.org/abs/2504.00573)
- [ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding](https://arxiv.org/abs/2501.07861)
- [Revela: Dense Retriever Learning via Language Modeling](https://arxiv.org/abs/2506.16552)
- [LREM: Large Reasoning Embedding Models](https://arxiv.org/abs/2510.14321)
- [Agentic-R: Learning to Retrieve for Agentic Search](https://arxiv.org/abs/2601.11888)
- [DIVER: A Multi-Stage Approach for Reasoning-intensive IR](https://arxiv.org/abs/2508.07995)
- [ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability](https://arxiv.org/abs/2508.07050)


【原始 proposal（允许参考但不是主要依据）】:
# Reasoning-Chain-Aware Reward Model for Dense Retriever Training (RARE)

## Core Problem

Current utility-based retriever training methods — binary EM (Agentic-R, arXiv 2026), perturbation attribution (SCARLet, EMNLP 2025), factorized Q-values (Q-RAG, ICLR 2026 Oral), perplexity reduction (UAE, arXiv 2604.22722, April 2026) — all provide **outcome supervision**: they evaluate documents by their effect on the final answer, treating document utility as a single undifferentiated dimension. This conflates documents that reduce uncertainty over the **answer space** (answer-containing documents providing direct evidence) with documents that reduce uncertainty over the **reasoning trajectory space** (reasoning-scaffolding documents enabling multi-step inference without containing the answer). On standard QA where answer-containing documents dominate, outcome supervision suffices. On reasoning-intensive retrieval (BRIGHT, ICLR 2025), reasoning-scaffolding documents are critical — a theorem explanation may be essential for solving a math problem while containing no part of the answer. Outcome signals systematically under-value such documents.

Meanwhile, the PRM literature (survey: arXiv 2510.08049) has established that **process supervision** — evaluating intermediate reasoning steps rather than final outcomes — captures qualitatively different information from outcome supervision. Yet no work has brought process supervision into dense retriever training.

**Core Question**: Can a process reward model that evaluates reasoning-chain quality serve as a training signal for dense retrievers, enabling them to encode reasoning utility — a high-order semantic property — in bi-encoder representations?

## Conceptual Contribution: Document Utility as a Continuous Spectrum

We propose that document utility for reasoning-intensive tasks lies on a **continuous spectrum** from pure direct evidence (answer-containing) to pure reasoning scaffolding, with most documents exhibiting a mixture. Existing outcome-based utility signals collapse this spectrum into a single scalar dominated by the answer-containing end, because their loss functions are defined over the answer space. A process reward signal is sensitive to the reasoning-scaffolding end of the spectrum, because it evaluates quality changes in intermediate reasoning steps — capturing utility that outcome signals miss. This is not merely a taxonomic observation: it predicts that process-supervised retriever training will produce qualitatively different retrieval behavior — higher recall of reasoning-scaffolding documents — compared to outcome-supervised training, even when both achieve similar aggregate scores.

Concrete examples: In BRIGHT's coding tasks, answer-containing = solution code, reasoning-scaffolding = relevant algorithm description. In economics, answer-containing = stated conclusion, reasoning-scaffolding = theoretical framework for derivation. In mathematics, answer-containing = final result, reasoning-scaffolding = applicable lemma or proof technique.

## Research Landscape and Positioning

**Outcome supervision for retriever training**: SCARLet (EMNLP 2025) uses perturbation attribution; Agentic-R (arXiv 2026) uses binary EM; Q-RAG (ICLR 2026 Oral) uses factorized Q-values; UAE (arXiv 2604.22722, April 2026) trains a DeBERTa RM on perplexity-reduction utility with Utility-Modulated InfoNCE distillation. All evaluated on standard QA, none on BRIGHT. UAE is RARE's closest methodological ancestor — RARE replaces its outcome-based RM with a process-based PRM and targets reasoning-intensive domains.

**Reasoning-intensive retrieval**: On BRIGHT, retriever-only SOTA: RaDeR 39.2 nDCG@10 (EMNLP 2025, MCTS synthetic data); ReasonEmbed 38.1 (arXiv 2025, ReMixer synthetic data + RI-InfoNCE); BGE-Reasoner-Embed-Qwen3-8B 37.1 in bi-encoder mode; Revela (arXiv 2506.16552) competitive via self-supervised LM with ~1000x less data. Full pipeline DIVER (arXiv 2508.07995) reaches 46.8. All use synthetic contrastive data or self-supervised signals — none use a learned RM targeting reasoning-chain quality.

**Reasoning embedding via CoT augmentation**: Large Reasoning Embedding Models (LREM, arXiv 2510.14321, 2025) embed reasoning by using Query-CoT-Item triplets as training data and RL-refined reasoning trajectories. LREM treats CoT as input augmentation to the embedding model; RARE treats reasoning-chain quality as a soft training label via PRM scoring. These are orthogonal approaches: LREM modifies what the embedding model sees, RARE modifies what the embedding model optimizes for.

**Reasoning injection taxonomy — three insertion points**: (1) **Query-time**: SmartSearch (arXiv 2601.04888) uses PRM for query refinement; BRIGHT's own CoT-augmented queries yield up to +12.2 nDCG. (2) **Inference-time**: ReasonRank (arXiv 2508.07050) uses LRM reranking (40.8 nDCG@10, 32B); ReARTeR (arXiv 2501.07861, SIGIR 2025) uses PRM+PEM for reasoning refinement in RAG. (3) **Training-time**: RARE injects process supervision into bi-encoder training via PRM-guided distillation — preserving inference-time efficiency.

**Concurrent work**: RICE-PO (arXiv 2605.26352, May 2026) optimizes LLM retrieval policies, not bi-encoder embeddings. 'Retrieval, Reward, and Training Protocols' (arXiv 2605.27881, May 2026) finds simple outcome rewards competitive for search agents — but this finding pertains to agentic pipelines where reasoning is delegated to the LLM; in bi-encoder training, reasoning utility must be internalized in the embedding space.

**PRM foundations**: ThinkPRM (arXiv 2504.16828, 2025) shows generative PRMs need only ~1K examples. Reward-RAG (arXiv 2024) uses RMs for generation quality, not retriever training. ReasonIR (arXiv 2025) trains retrievers for reasoning via synthetic data without learned RMs.

## Proposed Approach

**RARE** (Reasoning-Aware Reward-modeled Embeddings): a three-stage pipeline bringing process supervision to dense retriever training.

**Stage 1 — Multi-Domain Reasoning-Utility PRM**: Fine-tune a generative PRM on DeepSeek-R1-Distill-Qwen-7B (~1.2K–2K examples). Data construction via **paired reasoning comparison**: for each (q, d) pair, prompt DeepSeek-R1 to generate reasoning chains with and without document d; score reasoning-chain quality delta via outcome correctness + chain coherence (step validity, intermediate conclusion soundness), yielding a continuous reasoning-utility label. Sample 100–200 pairs per domain from external corpora: Proof Wiki + MATH train set (math), filtered StackOverflow (coding), S2ORC subsets (science/economics/psychology), legal case databases (law). Total: ~1.2K–2.4K labeled pairs covering BRIGHT's 12 domains. Validate silver labels against 250 human-annotated pairs (~20 per domain), targeting Spearman ρ ≥ 0.7. Report per-domain PRM scoring quality.

**Stage 2 — Document Scoring**: Apply trained PRM to candidate documents from domain-matched external corpora (not BRIGHT evaluation data). Pre-filter candidates via BM25 top-500 per query to control inference cost. Estimated scoring cost: ~50K–100K (q,d) pairs × ~0.5s per pair on A100 ≈ 7–14 GPU-hours.

**Stage 3 — Embedding Distillation**: Distill PRM scores into Qwen3-Embedding-8B via Utility-Modulated InfoNCE (UAE's loss formulation), where contrastive weights reflect process-based reasoning utility.

## Evaluation Plan

**Benchmarks**: (1) BRIGHT (ICLR 2025) — primary, all 12 domains with per-domain nDCG@10 and Recall@1/5/10/100; (2) BEIR subset (NQ, HotpotQA, FiQA, SciFact, TREC-COVID) — regression test for general retrieval performance.

**Baselines** (9 methods):
1. RaDeR (EMNLP 2025) — MCTS synthetic data, retriever-only SOTA
2. ReasonEmbed (arXiv 2025) — ReMixer synthetic data
3. BGE-Reasoner-Embed-Qwen3-8B — same backbone family
4. Revela (arXiv 2506.16552) — self-supervised, no synthetic pairs
5. ReasonIR-8B (arXiv 2025)
6. UAE-style perplexity-reduction RM (reimplementation on BRIGHT) — direct outcome-vs-process comparison
7. UAE-style with 7B RM (capacity-controlled variant) — isolates signal type from RM capacity
8. Qwen3-Embedding-8B with CoT-augmented queries (no training) — zero-cost query-time alternative
9. Qwen3-Embedding-8B standard contrastive training (no RM)

**Ablation studies** (6 axes):
- Signal type: process-based PRM vs. outcome-based binary EM vs. perplexity-reduction RM — core claim validation
- Loss function: Utility-Modulated InfoNCE vs. standard InfoNCE vs. margin-based loss
- PRM data scale: 500 / 1K / 2K / 4K examples
- PRM backbone size: DeepSeek-R1-Distill-Qwen-1.5B vs. 7B
- Domain coverage: math+coding only vs. all 12 domains — cross-domain transfer test
- Per-domain analysis: identify which reasoning types benefit most from process supervision

**RM Quality Analysis** (core assumption validation):
- Annotate 250 BRIGHT positive documents (~20 per domain) with 2 annotators on a continuous utility-source scale (pure evidence ↔ pure scaffolding). Operational criterion: if removing all answer-matching content leaves the document still reasoning-helpful → scaffolding end. Target Cohen's Kappa ≥ 0.7.
- Verify that PRM scores correlate more strongly with scaffolding-end ratings than outcome-based utility scores do.
- Report Spearman/Kendall correlation between PRM scores and downstream reasoning improvement. Use bootstrapped 95% CIs.
- Qualitative case studies: PRM high-score vs. low-score documents across representative domains.

**Downstream reasoning evaluation**: Retrieve top-k documents (k=5, 10) using each retriever, feed to Qwen2.5-72B-Instruct with unified prompt ("Given the following documents, solve the problem step by step"). Measure reasoning accuracy per domain (exact match for math, pass@1 for coding, F1 for others). All retrievers share identical downstream LLM and prompt.

**Reproducibility**: 3 random seeds, mean ± std. Full compute budget in A100 GPU-hours: PRM training (~1–2h), document scoring (~7–14h), embedding training (~TBD). Compute-normalized comparison with RaDeR (MCTS cost) and ReasonEmbed (82K synthesis cost).

## Hypothesized Contributions

(1) **Conceptual**: First application of process supervision to dense retriever training, demonstrating that document utility lies on a continuous spectrum that outcome supervision systematically under-explores.
(2) **Empirical**: RARE targets retriever-only SOTA on BRIGHT (>39.2 nDCG@10) while answering whether bi-encoder representations can encode reasoning utility — a high-order semantic property beyond lexical/semantic similarity.
(3) **Methodological**: The process supervision signal, unlike synthetic contrastive data, is a learned continuous scorer transferable across domains without domain-specific data regeneration.

## Key References

- Process Reward Models That Think (ThinkPRM, arXiv 2504.16828, 2025)
- Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training (ICLR 2026)
- Aligning Dense Retrievers with LLM Utility via Distillation (UAE, arXiv 2604.22722, April 2026)
- Training a Utility-based Retriever Through Shared Context Attribution (SCARLet, EMNLP 2025)
- RaDeR: Reasoning-aware Dense Retrieval Models (EMNLP 2025)
- ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Document Retrieval (arXiv 2025)
- BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval (ICLR 2025)
- Agentic-R: Learning to Retrieve for Agentic Search (arXiv 2026)
- Reward-RAG: Enhancing RAG with Reward Driven Supervision (arXiv 2024)
- ReasonIR: Training Retrievers for Reasoning Tasks (arXiv 2025)
- RICE-PO: Turning Retrieval Interactions into Credit Signals (arXiv 2605.26352, May 2026)
- Retrieval, Reward, and Training Protocols (arXiv 2605.27881, May 2026)
- ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability (arXiv 2508.07050)
- SmartSearch: Process Reward-Guided Query Refinement (arXiv 2601.04888, Jan 2026)
- BGE-Reasoner-Embed-Qwen3-8B (BAAI, 2025)
- Revela: Dense Retriever Learning via Language Modeling (arXiv 2506.16552, 2025)
- DIVER: A Multi-Stage Approach for Reasoning-intensive IR (arXiv 2508.07995, 2025)
- Large Reasoning Embedding Models (LREM, arXiv 2510.14321, 2025)
- ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding (arXiv 2501.07861, SIGIR 2025)
- A Survey of Process Reward Models (arXiv 2510.08049, 2025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6a1fe727-177b-446c-996c-f34e2e53ec38",
  "type": "user",
  "uuid": "26f0078c-b708-47bc-bcb9-d5d2a9f1317a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:45:47.228Z_

```json
{
  "parentUuid": "26f0078c-b708-47bc-bcb9-d5d2a9f1317a",
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
  "uuid": "d7afb51a-7e94-4acd-a0dc-e2fdc0724b76",
  "timestamp": "2026-05-30T07:45:47.228Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:45:47.228Z_

```json
{
  "parentUuid": "d7afb51a-7e94-4acd-a0dc-e2fdc0724b76",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "69e66f3d-27da-47ff-8553-4cc828c30ddf",
  "timestamp": "2026-05-30T07:45:47.228Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have a thorough understanding of the landscape. Let me c…",
  "leafUuid": "69e66f3d-27da-47ff-8553-4cc828c30ddf",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize three reviewer assessments for RARE proposal",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1"
}
```

---

### Assistant

_source line 8 · 2026-05-30T07:46:15.146Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviews carefully to produce a Meta Judge synthesis.

**Review 1 (R1):**
- Probability: [28% - 40%] 中位 34%
- Research Question: 强
- Method/Innovation: 中
- Experimental Design: 强
- Feasibility: 中
- Writing: 强

**Review 2 (R2):**
- Probability: [28% - 42%] 中位 35%
- Research Question: 强
- Method/Innovation: 中
- Experimental Design: 强
- Feasibility: 强


- Writing: 强

**Review 3 (R3):**
- Probability: [25% - 38%] 中位 31%
- Research Question: 中偏强
- Method/Innovation: 中
- Experimental Design: 强
- Feasibility: 中偏强
- Writing: 强

Now I'm calculating the aggregate statistics across all three reviews. The median probabilities are 34%, 35%, and 31%, which gives me a mean of 33.3% and a median of 34%. I'm computing the standard deviation to assess the consistency of these probability estimates.

The standard deviation comes out to approximately 1.7%, which is well below the 3% threshold, indicating strong consistency across reviewers. Looking at where reviewers align, the Method/Innovation, Experimental Design, and Writing dimensions show unanimous agreement at the 中 and 强 levels respectively. The Research Question leans toward 强 with two reviewers supporting that rating, while Feasibility shows slight variation across the three assessments but still clusters around the middle-to-strong range.

The most striking pattern is how all three reviewers independently flagged the same core risks: the incremental nature of combining existing components, uncertainty around whether the PRM can generalize across domains, and the fundamental question of whether process rewards actually correlate with outcome quality. They also converge on the need for exceptionally strong experimental results to offset the limited methodological novelty. Beyond these shared concerns, individual reviewers raised distinct points—one questioned BRIGHT's practical applicability, another compared the cost-benefit against simpler PRM reranking approaches, and another suggested missing baselines or alternative combinations worth exploring.

On the implementation side, there's remarkable agreement: the compute requirements are modest at 20-40 A100 hours, the data needs are moderate with around 1.2K-2.4K training pairs plus 250 human annotations, and the timeline estimates cluster around 8-12 weeks, though one reviewer thinks it could be done in 4-6 weeks. Looking at the three median probability estimates of 31%, 34%, and 35%, the consistency is tight enough that I should anchor to the middle ground. The median of those medians is 34%, so I'm setting the final range at 27%-39% with a central estimate of 33%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e66f3d-27da-47ff-8553-4cc828c30ddf",
  "isSidechain": false,
  "requestId": "req_011CbYP6hnjeRkR6K67kYpVf",
  "type": "assistant",
  "uuid": "0a6619ca-452d-422a-a3d2-59e1586d5a3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAMSAtA6sNv9eDSjancXYj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20482,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20482,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3194,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20482
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

_source line 9 · 2026-05-30T07:47:05.980Z_

【阶段】: Meta Judge

【三次中位】: [34%, 35%, 31%]  std=1.7%

【共识维度】:
- **研究问题: 强**（R1 强、R2 强、R3 中偏强）— 3/3 确认 process supervision 用于 retriever training 是真实空白，方向正确且有时效性
- **方法与创新: 中**（R1 中、R2 中、R3 中）— **3/3 一致判定**，这是信号最强的共识维度。核心关切完全一致：方法本质是"UAE 框架中将 outcome RM 替换为 PRM"的组件替换，缺乏新损失函数/架构/训练范式层面的原创贡献
- **实验设计: 强**（R1 强、R2 强、R3 强）— **3/3 一致判定**。9 baselines + 6 ablation axes + 250 human annotations + RM quality validation + downstream evaluation，在 proposal 阶段达到一线顶会标准
- **写作与呈现: 强**（R1 强、R2 强、R3 强）— **3/3 一致判定**。Related work 定位精准，reasoning injection taxonomy 有效，参考文献覆盖全面且时效性极强
- **可行性: 中偏强**（R1 中、R2 强、R3 中偏强）— 2/3 认为中偏强或以上，计算资源合理，pipeline 可执行
- **核心风险共识**（3/3 均提及）：(1) "incremental combination"是最可能的拒稿理由；(2) PRM 跨 12 域泛化的不确定性；(3) 需要强实验结果才能弥补方法创新不足

【异常维度】:
- R3 独有：质疑 reasoning-intensive retrieval 在实际部署中的需求规模（其他两位未提及，且该方向有 ICLR 2025/2026 Oral 级工作，此关切降权）
- R2 独有：强调需要与 PRM reranking 方案的 end-to-end 成本效益对比（有效关切但非致命，不影响整体判定）
- R1 独有：指出缺少 LREM 作为 baseline（合理建议，但非核心缺陷）
- R3 独有：提出 LREM 组合可能性作为潜在机会（属于锦上添花而非必需）
- R3 预估周期偏短（4-6 周 vs R1/R2 的 8-12 周）——R3 可能低估了数据构建和完整 ablation 的工程量，取 R1/R2 的 8-12 周更稳健

【最终概率】: [27% - 38%] 中位 33%

【一致性】: 高（std=1.7% < 3%）

【综合理由】:
三位审稿人展现出罕见的高度一致：std 仅 1.7%，五个核心维度中四个（方法创新、实验设计、写作、核心风险）判定完全一致。这给出了非常高的信号可靠性。

综合逻辑如下：

1. **方法创新是硬天花板**：3/3 一致判定为"中"，这是本 proposal 的决定性瓶颈。无论实验多完美、写作多精良，"UAE + ThinkPRM 的组件替换"这个方法论 delta 限制了论文的 contribution ceiling。在 AAAI 接收率 ~23-25% 的竞争中，仅有"正确的组合"而无方法论层面的原创贡献，使论文处于 borderline 的下半区。

2. **实验设计和写作是强支撑但非充分条件**：3/3 一致判定两者为"强"，这意味着论文不太会因为实验不足或 presentation 问题被拒——但在 AAAI 的评审中，实验设计再好也无法补偿方法创新的不足。这两个维度把下界兜住在 ~27%（不会太低），但无法把上界推过 ~38%。

3. **概率取值逻辑**：高一致性情况下取中位附近、缩窄区间。三位中位 31/34/35 的中位数是 34%，但遵循"宁缺毋滥"原则，略偏保守取 33%。区间 [27%-38%] 反映：若实验结果强有力（显著超 SOTA + process vs. outcome 差异清晰验证），可推至 38%；若结果 marginal 或 PRM 泛化不佳，滑至 27%。

4. **综合后估计不超过三份中最宽松**：R2 最宽松为 [28%-42%]，本最终估计 [27%-38%] 上界低于 42%，合规。

【建议】: 边缘

【实施评估】:
  - 计算资源: 中等偏低。PRM 训练 ~1-2h A100，文档打分 ~7-14h A100，embedding 蒸馏 ~8-20h A100（基于 Qwen3-8B fine-tuning）。核心实验总计 ~20-40h A100，含完整 ablation 和多 seed 重复约 100-200h A100。单卡可完成，无需大规模集群。
  - 数据需求: 中等。需从 Proof Wiki、MATH train、StackOverflow、S2ORC、法律案例库等外部公开语料构建 ~1.2K-2.4K paired reasoning comparison 数据；需 DeepSeek-R1 进行大量推理链生成（inference calls）；BRIGHT + BEIR 评测数据均公开可用。
  - 人工介入: 低-中。250 条 BRIGHT 正例文档的 utility-source 标注（2 标注员，~20/domain × 12 domains），需要跨领域 domain expertise，估计 ~40-60 人时（约 2-4 人天）。
  - 训练需求: 需要两阶段 fine-tuning——(1) PRM: DeepSeek-R1-Distill-Qwen-7B，~1-2h A100；(2) Embedding: Qwen3-Embedding-8B 的 contrastive distillation，~8-20h A100。均为 fine-tuning 而非从头训练，规模适中。
  - 新 Benchmark: 不需要。使用现有 BRIGHT（主评测）+ BEIR 子集（regression test）。但需构建 multi-domain PRM 训练数据集和人工标注集，可作为数据贡献发布。
  - 预估周期: 约 8-12 周（取 R1/R2 共识，R3 的 4-6 周偏乐观）。数据构建 2-3 周，PRM 训练+验证 1-2 周，文档打分 1 周，embedding 训练+调参+ablation 2-3 周，downstream evaluation + 分析 1-2 周，写作 2 周。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a6619ca-452d-422a-a3d2-59e1586d5a3a",
  "isSidechain": false,
  "requestId": "req_011CbYP6hnjeRkR6K67kYpVf",
  "type": "assistant",
  "uuid": "5a077755-6443-4080-976c-c2164e701049",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAMSAtA6sNv9eDSjancXYj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20482,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20482,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3194,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20482
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have a thorough understanding of the landscape. Let me c…",
  "leafUuid": "5a077755-6443-4080-976c-c2164e701049",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize three reviewer assessments for RARE proposal",
  "sessionId": "14b61dac-0d91-4525-bbad-6d4372584af1"
}
```

---
