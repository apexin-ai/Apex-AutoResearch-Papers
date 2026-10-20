# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/3377e962-fe73-4efd-98f1-cf877a08dee4.jsonl`
- **Structured JSON:** [`5905acffa42638025767.json`](../../sessions/59/5905acffa42638025767.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:41:20.454Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:41:20.454Z",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient background to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Geoparsing (arXiv:2604.11600)](https://arxiv.org/abs/2604.11600) (ACL 2026): 最直接的基线。使用 SFT + RLVR（基于规则的本地一致性验证器）在 GDP-29K 上训练 Qwen3-VL-4B，CDL 解析达到 96.4 F1。验证器检查句法正确性、参数类型、元数等，但不检查坐标级约束满足。本 proposal 在其之上改进 reward 信号。\n- [CGD-Bridge (arXiv:2601.21164)](https://arxiv.org/html/2601.21164) (CVPR 2026): 使用 CDL 匹配奖励 + GRPO，将生成的 CDL 与 GT CDL 逐项匹配作为 reward。在 formalgeo7k 上训练。Proposal 正确指出其 representation sensitivity 问题——匹配奖励惩罚语义等价但形式不同的 CDL 表示。\n- [GeoDPO (arXiv:2602.22703)](https://arxiv.org/abs/2602.22703) (ICLR 2026): 翻译器引导的 RL，用 NL-to-DSL 翻译器计算 DSL 级分数作为 reward，获得 +26.5% 域内感知提升和 +39% 下游推理提升。依赖翻译器训练数据，存在 annotation dependence 问题。\n- [SIRL (arXiv:2505.11792)](https://arxiv.org/abs/2505.11792) (arXiv 2025): Solver-as-verifier RL 用于优化建模，使用外部求解器提供 syntax/feasibility/solution-quality 三级 reward。7B 模型超过 DeepSeek-V3 和 o3。本 proposal 的最重要跨领域先例，验证了\"外部形式化验证器作 RL reward\"范式的有效性。\n- [SGVR (arXiv:2601.05073)](https://arxiv.org/abs/2601.05073) (arXiv 2026): 子目标可验证奖励，将抽象证明转化为可验证数值子目标，用 Skeleton Rate 作为密集 reward。几何推理 +9.7%，通用数学 +8.0%。与本 proposal 共享\"密集可验证奖励\"理念，但 SGVR 面向推理阶段，本 proposal 面向感知阶段。\n- [PRCO (arXiv:2603.28618)](https://arxiv.org/abs/2603.28618) (arXiv 2026): 感知-推理协同进化，Observer 生成证据 caption，Solver 基于 caption 推理。Observer 通过 Solver 的 utility reward 获得间接监督。与本 proposal 共享\"感知阶段需要独立 reward\"的动机，但 PRCO 使用间接/学习信号，CCV 使用直接/形式化信号。\n- [\"Bad Seeing or Bad Thinking?\" (arXiv:2605.14054)](https://arxiv.org/abs/2605.14054) (arXiv 2026): 提出 Perception Verification 作为 VLM reward，解决感知-推理的 credit assignment 模糊问题。验证了 proposal 的核心前提：感知阶段需要独立的、基于验证的 reward 信号。\n- [FormalGeo (arXiv:2310.18021)](https://arxiv.org/abs/2310.18021): 88 个几何谓词 + 196 条定理的形式化框架。formalgeo7k 数据集提供 GeoGebra 标注的点坐标——这是本 proposal CCV reward 的关键数据来源。\n\n- **调研总结**: 几何图表解析的 RL 训练是 2025-2026 年的活跃研究方向，已有多种 reward 设计（规则验证、GT 匹配、翻译器引导），但**无人使用坐标级几何约束满足作为 reward**。Proposal 的 novelty claim 成立。同时，\"感知阶段需要独立可验证 reward\"的大趋势（PRCO、Vision-SR1、\"Bad Seeing or Bad Thinking?\"）为本工作提供了理论支撑。主要竞争对手是 Geoparsing（同 base model，同数据，不同 reward）。\n\n【整体印象】:\n作为审稿人，我的第一反应是**borderline positive**。这是一篇思路清晰、定位精准的工作：在一个活跃的研究方向上，识别了现有 reward 设计的两个真实局限（表示敏感性、标注依赖），并提出了一个简洁优雅的解决方案。核心 idea（用坐标约束验证替代 GT 匹配/规则验证作为 RL reward）概念上自然、技术上可行。实验设计异常全面——6 个 baseline、7 组 ablation、统计显著性测试、误差分析，这本身就是一个强加分项。\n\n**但我有两个主要顾虑**：(1) 核心技术贡献的深度——\"检查谓词是否满足坐标约束\"这件事本身并不复杂，novelty 可能被质疑为\"engineering trick\"而非\"研究贡献\"；(2) 改进空间不确定——在 96.4 F1 的 baseline 上，parsing 层面的提升可能非常有限，虽然 proposal 合理地论证了对端到端求解的放大效应，但这需要实验验证。\n\n我会倾向给一个 weak accept，前提是实验结果能显示清晰的端到端求解提升和半监督训练的价值。\n\n【核心贡献】:\n1. **坐标约束验证（CCV）作为表示不变的 RL reward**：消除 GT 匹配奖励中的假阴性惩罚，任何几何上正确的 CDL 表示都能获得完整奖励。\n2. **CDL 标注无关训练**：CCV 仅需点坐标（不需要 CDL 标注），使半监督 RL 训练成为可能。\n3. **系统性的实验设计**：包括训练-推理分离实验（CCV 作为 reranker vs. 作为 RL reward）、多层次 oracle 对比、半监督实验。\n\n对领域的价值：**中等偏高**。如果半监督训练路径有效，这将打破几何解析 RL 训练的标注瓶颈，具有实际扩展意义。表示不变性是一个原则性改进。但如果仅仅是 parsing F1 的微小提升，价值会大幅下降。\n\n【方法合理性】:\n方法合理性**总体良好**，但有几个需要审视的点：\n\n1. **逐谓词独立验证 vs. 联合约束满足**：CCV 逐个谓词验证坐标满足，这能捕获单谓词错误，但对于多谓词联合不一致性（每个谓词单独看在容差内但联合矛盾），效果可能有限。Proposal 意识到了这一点并设计了 Tier B（联合约束可满足性）作为 oracle 对比，这是正确的。但核心方法（Tier A/CCV）的局限需要诚实报告。\n\n2. **数值容差的鲁棒性**：几何图表的坐标可能来自不同来源（GeoGebra 精确标注 vs. 图像点检测估计），精度差异大。容差选择可能成为一个不那么 trivial 的工程问题。Proposal 计划 5 级容差 ablation（1e-6 到 1e-1），这很好。\n\n3. **是否存在更简单的替代方案？** 一个审稿人可能会问：与其在 RL 训练中使用 CCV reward，直接用 CCV 做推理时 reranking（生成 k 个候选，按 CCV 分数选择）是否就够了？Proposal 很聪明地把这个作为 baseline 6 纳入了实验设计，这消除了最大的方法论质疑。\n\n4. **坐标可用性假设**：formalgeo7k 有精确坐标，但 Geometry3K/GDP-3K 可能没有。这限制了方法的通用性。如果需要视觉点检测来获取坐标，那么坐标的噪声会直接影响 CCV reward 的质量，形成一个\"感知误差 → reward 噪声 → 训练信号失真\"的级联问题。\n\n【5 维度打分】:\n\n1. **研究问题: 强** — 几何解析的 RL reward 设计是当前活跃且重要的研究问题。Proposal 识别的两个局限（表示敏感性、标注依赖）在 Geoparsing、CGD-Bridge、GeoDPO 中确实存在，不是人为构造的问题。\"感知阶段需要独立的形式化 reward\"这一方向得到了 PRCO、\"Bad Seeing or Bad Thinking?\"、Vision-SR1 等多项同期工作的验证。问题的实际意义也清晰：CDL 解析错误是端到端几何求解的主要瓶颈（Hilbert-Geo 已指出）。\n\n2. **方法与创新: 中** — 核心 idea 概念上自然且正确——用坐标约束验证替代表面形式匹配是一个原则性改进。但技术深度有限：\"对每个谓词，用坐标验证数值满足\"这一操作本身是直接的工程实现（检查斜率相等、面积为零、距离等于半径等），不涉及新的算法设计或理论贡献。与 SIRL（solver-as-verifier for optimization）的关系类似\"将已有范式应用到新领域\"。Novelty 的核心价值在于识别问题和连接已有组件，而非方法本身的技术创新。相比 GeoDPO（设计翻译器引导的 reward）或 SGVR（设计子目标可验证 reward 框架），本工作的技术深度较浅。但 representation-invariance 和 annotation-free 两个性质的结合是一个有意义的贡献点。\n\n3. **实验设计: 强** — 这是本 proposal 最突出的优势。6 个 baseline（包括非常必要的 CCV-reranking 推理时 baseline），7 组 ablation（reward 类型、粒度、容差、优化器、初始化、约束类型分解、训练 vs. 推理），半监督实验，预实验误差分析，统计显著性测试（≥3 seeds + paired bootstrap），compute fairness——实验方案的完备程度远超同领域平均水平。特别值得肯定的是：(a) CCV reranking baseline 直接回答了\"是否需要 RL 训练\"这个核心方法论问题；(b) 半监督实验是验证 annotation-free 贡献的必要设计；(c) 预实验误差分析量化了改进天花板，避免了\"做了但没用\"的风险。\n\n4. **可行性: 强** — 所有技术组件已存在：Qwen3-VL-4B（base model）、GRPO（RL 算法）、FormalGeo/formalgeo7k（形式化框架和数据集）、NumPy 向量化检查（CCV 实现）。计算需求合理（4B 模型 + 微秒级 reward 计算）。主要风险是坐标可用性（Geometry3K/GDP-3K），但 proposal 已有降级方案（这些 benchmark 只用规则/匹配 reward）。\n\n5. **写作与呈现: 强** — Proposal 逻辑清晰，从 problem → opportunity → approach → experiments 的叙事流畅。对现有工作的定位精准，既不过度贬低也不过度抬高自身。\"Why not extend rule-based verifiers?\" 这个反驳段落预判了审稿人的自然质疑。研究假设明确可检验。唯一的小问题是 proposal 长度偏长，实际写成论文时需要大幅精简。\n\n【概率估计】: [28% - 40%] 中位 33%\n\n【估计理由】:\n向上推力：(1) 研究问题时效性强，2025-2026 年几何解析 RL 是热点方向；(2) Novelty claim 成立——确实无人用坐标约束验证作为 parsing RL reward；(3) 实验设计非常完备，远超领域平均水平，这在审稿中是实质加分；(4) 半监督训练路径（CCV-RLVR on coordinate-only data）是有实际价值的独立贡献；(5) 与同期感知-推理分离趋势（PRCO、\"Bad Seeing or Bad Thinking?\"）高度契合。\n\n向下压力：(1) 核心技术贡献深度有限——\"用坐标检查谓词满足\"概念直接，可能被部分审稿人视为 engineering contribution 而非 research contribution；(2) 在 96.4 F1 的 baseline 上，提升空间有限，如果端到端求解提升不显著则说服力大减；(3) 主要对比限于 formalgeo7k（坐标已确认可用），benchmark 覆盖面偏窄；(4) 逐谓词独立验证可能无法充分捕获多谓词联合不一致性——而这恰恰是 proposal 的核心假设（\"disproportionately reduce multi-predicate inconsistency errors\"）；(5) 竞争激烈——Geoparsing、CGD-Bridge、GeoDPO、SGVR 等多项强工作同期发表，审稿人对\"又一种 reward 设计\"可能产生审美疲劳。\n\n综合判断：这是一篇 solid 但不 outstanding 的投稿。方向正确、定位精准、实验全面，但核心技术创新的深度是软肋。如果实验结果强（端到端求解有显著提升，半监督路径有效），概率向 40% 靠近；如果提升微弱，则接近下界。33% 反映了\"实验结果中等\"的预期情景。\n\n【主要风险】:\n1. **Novelty 深度不足**：核心方法（逐谓词坐标验证）技术上过于直接，可能被审稿人评为\"缺乏足够的技术创新\"或\"SIRL 在几何领域的直接应用\"。这是最可能触发 reject 的风险。\n2. **改进幅度不足**：在 96.4 F1 的 baseline 上，如果端到端求解精度提升仅为 1-2 个百分点，审稿人可能认为贡献不足以支撑一篇顶会论文。核心假设（\"多谓词不一致性导致不成比例的求解失败\"）需要强有力的实证支持。\n\n【实施评估】:\n  - 计算资源: 中等偏低。Qwen3-VL-4B 的 GRPO 训练在 4×A100 上数天可完成；CCV reward 计算为微秒级 NumPy 操作，几乎无额外开销。Tier B（FGPS 联合验证）较慢（~0.1-1s/call）但仅作 oracle 对比。\n  - 数据需求: formalgeo7k（已公开，含坐标）为主实验数据源；GDP-29K（Geoparsing 提供）用于训练；Geometry3K/PGPS9K 用于评测。所有数据集已公开可用。坐标可用性需确认 Geometry3K/GDP-3K。\n  - 人工介入: 低。CCV 验证逻辑（~88 谓词的坐标检查）需要手动实现，但每个谓词的检查逻辑是简单的数值计算。可能需要少量工程工作来桥接 FormalGeo 的谓词格式。\n  - 训练需求: 需要 RL 微调 Qwen3-VL-4B（GRPO），需要 SFT 预训练作为初始化。共计 ~2-3 轮训练（SFT + 多种 reward 的 RL 对比）。\n  - 新 Benchmark: 不需要构建新 benchmark。使用已有的 formalgeo7k、Geometry3K、PGPS9K、GDP-3K。\n  - 预估周期: 8-12 周。包括：CCV 实现与验证（1-2 周）、预实验误差分析（1 周）、主实验 RL 训练与对比（3-4 周，多 baseline × 多 seed）、ablation 实验（2-3 周）、论文写作（2-3 周）。\n```\n\nSources:\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language](https://arxiv.org/abs/2604.11600)\n- [CGD-Bridge: Concise Geometric Description as a Bridge](https://arxiv.org/html/2601.21164)\n- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning](https://arxiv.org/abs/2602.22703)\n- [SIRL: Solver-Informed RL for Optimization Modeling](https://arxiv.org/abs/2505.11792)\n- [SGVR: Milestones over Outcome](https://arxiv.org/abs/2601.05073)\n- [FormalGeo: An Extensible Formalized Framework](https://arxiv.org/abs/2310.18021)\n- [PRCO: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)\n- [Bad Seeing or Bad Thinking? Rewarding Perception for VL Reasoning](https://arxiv.org/abs/2605.14054)\n- [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/html/2605.16385)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a comprehensive evaluation. Let me synthesize all findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Geoparsing (arXiv:2604.11600)](https://arxiv.org/abs/2604.11600) (ACL 2026): 直接前置工作。使用 Qwen3-VL-4B 做 SFT + RLVR，rule-based verifier 检查语法和局部几何一致性，达到 96.4 F1。本 proposal 的直接 baseline 和起点。\n- [CGD-Bridge (arXiv:2601.21164)](https://arxiv.org/abs/2601.21164) (CVPR 2026): 用 CDL matching rewards + GRPO 训练 MLLM Interpreter，仅 5.5k 数据即有竞争力。其 CDL matching reward 是 piece-by-piece greedy matching（recall + precision），正是本 proposal 指出的\"representation-sensitive\"问题的典型代表。\n- [GeoDPO (arXiv:2602.22703)](https://arxiv.org/abs/2602.22703) (ICLR 2026): translator-guided RL，NL→DSL translator 计算 DSL-level reward，+26.5% in-domain，+39% 下游推理。需要训练额外 translator 模型，是本 proposal 指出的\"annotation dependence\"问题的例证。\n- [SIRL (arXiv:2505.11792)](https://arxiv.org/abs/2505.11792) (NeurIPS 2025): solver-as-verifier RL 用于优化建模，syntax/feasibility/solution-quality 三级 reward。本 proposal 的跨领域 precedent，验证了 solver verification 作为 RL reward 的范式可行性。\n- [Bad Seeing or Bad Thinking? (arXiv:2605.14054)](https://arxiv.org/abs/2605.14054) (arXiv 2026): Perception Verification 独立奖励感知忠实度，Modality-Aware Credit Assignment 区分感知/推理错误。属于 perception-reasoning decomposition 趋势的最新工作，与本 proposal 的 perception-level reward 设计形成互补定位。\n- [FormalGeo (arXiv:2310.18021)](https://arxiv.org/abs/2310.18021): 提供 formalgeo7k 数据集，含 GeoGebra 标注的点坐标和 88 predicates/196 theorems 的形式化系统。本 proposal 的 CCV reward 依赖此数据集的坐标标注。\n\n- **调研总结**: 几何图形解析的 RL reward 设计是 2025-2026 年的活跃方向，已有 rule-based (Geoparsing)、CDL matching (CGD-Bridge)、translator-guided (GeoDPO) 三种 reward 范式。坐标级几何约束满足性作为 RL reward 尚无人做，是一个真实的空白点。但这个空白点的影响范围较窄（仅限于几何解析的 reward 信号改进），且 baseline 已经很强（96.4 F1），提升空间受限。\n\n【整体印象】:\n如果我是审稿人，第一反应是：这是一篇动机清晰、方法简洁、实验设计极为充分的 proposal，但核心贡献的量级（novelty depth）让我犹豫。核心 idea 可以用一句话概括：\"用坐标约束验证替代字符串匹配作为几何解析的 RL reward\"。这个 idea 合理且有效，但技术深度有限——坐标级几何验证（检查斜率相等、面积为零、距离等于半径等）本身是计算几何的基础操作，将其包装为 RL reward 的工程复杂度不高。我会倾向于 borderline/weak accept，取决于实验结果能否展示出令人信服的提升，尤其是在 end-to-end solving accuracy 上的改善。\n\n【核心贡献】:\n1. 提出坐标约束验证（CCV）作为几何解析的 RL reward，具有 representation-invariant 和 CDL-annotation-free 两个优势。\n2. Semi-supervised 训练范式：SFT on annotated data + CCV-RLVR on coordinate-only data。\n3. 系统性地比较和消融四种 reward 设计（rule-based / CDL matching / CCV / joint constraint）。\n\n贡献对领域的价值：中等偏上。reward 设计改进对于几何解析-推理管线有实际意义，但影响面主要局限在 geometry problem solving 子方向。semi-supervised 训练范式如果被验证有效，可能更具推广价值。\n\n【方法合理性】:\n方法本身是合理的。用坐标验证检查几何 predicate 的满足性是数学上正确的。但有以下需要审视的点：\n\n1. **Precision-only reward 的偏差**: CCV reward = 满足约束的 predicate 占比，这本质是一个 precision 指标。RL 优化此 reward 可能导致模型趋向保守——只预测高置信度的 predicates，牺牲 recall。proposal 没有显式讨论这个问题，也没有设计 recall 补偿机制（如 predicate 数量下限惩罚）。\n2. **Per-predicate 验证 vs. Joint consistency**: CCV 逐 predicate 检查，可能漏掉某些 predicates 单独满足但联合不一致的情况（虽然坐标验证本身已经隐式处理了大部分此类情况）。Tier B（joint constraint satisfiability via FGPS）被标为\"oracle comparison only\"，但如果 Tier B 效果显著优于 CCV，则 CCV 的贡献会被削弱。\n3. **是否有更简单的替代方案**: CCV reranking baseline（实验设计 #6）已经覆盖了这一点——如果 inference-time reranking 就能获得大部分收益，那 RL 训练的必要性会被质疑。这是一个很好的自我对照设计。\n4. **Tolerance 选择的脆弱性**: 数值验证依赖容差参数，proposal 设计了 5 级 tolerance 消融，但容差选择对不同 predicate 类型（角度 vs. 距离 vs. 共线性）可能需要不同尺度，统一容差可能不够。\n\n【5 维度打分】:\n\n1. **研究问题: 中** — 问题真实存在：representation sensitivity 和 annotation dependence 是当前 geometry RL reward 的实际限制，在 CGD-Bridge 和 GeoDPO 的设计中可以明确看到。但问题的影响面较窄（仅限于几何解析 reward 设计），且 Geoparsing 已经 96.4 F1，进一步提升的边际价值需要在 end-to-end solving 上证明。\n\n2. **方法与创新: 中** — 坐标约束验证作为 RL reward 在几何解析领域确实无人做过（调研未发现直接竞争工作）。但技术贡献偏轻——CCV 本质是标准计算几何操作的包装，不涉及新的算法或理论。与 SIRL 的跨领域 precedent 相比，本工作的 unique challenge（visual input, per-predicate granularity, constraint coupling）确实存在但增量有限。创新更多体现在 \"insight\" 层面（recognizing coordinate verification is the right reward signal）而非 \"method\" 层面。\n\n3. **实验设计: 强** — 这是 proposal 最大的亮点。6 个 baselines（含直接消融对照 Geoparsing SFT+RLVR 和 inference-time reranking baseline），7 组消融实验覆盖了审稿人可能提出的几乎所有问题（reward type / granularity / tolerance / optimizer / initialization / constraint type / training vs. inference），semi-supervised 实验直接验证 annotation-free claim，pre-experiment error analysis 量化改进上限，统计显著性检验（paired bootstrap, ≥3 seeds）。实验设计的完备度在 proposal 阶段罕见地高。参照 SIRL 和 SGVR 的实验标准，本 proposal 的实验方案达到甚至超过了领域标准。\n\n4. **可行性: 中** — 主要风险在于：(a) formalgeo7k 的坐标确认可用，但 Geometry3K 和 GDP-3K 的坐标可用性\"must be confirmed\"——如果这两个主流 benchmark 没有坐标，工作将主要局限于 formalgeo7k，说服力大打折扣；(b) 96.4 F1 的 baseline 意味着绝对提升可能很小，如果 end-to-end solving accuracy 提升不显著，论文故事难以成立；(c) Qwen3-VL-4B + GRPO 的训练本身可行，计算需求合理。\n\n5. **写作与呈现: 强** — Proposal 逻辑极为清晰：两个 limitation → 一个统一解决方案 → 完备实验验证。研究定位精准，与相关工作的差异化阐述到位（rule-based vs. CDL matching vs. translator-guided vs. CCV 的四方对比）。broader context 的引用（SIRL, perception-reasoning decomposition 趋势）增强了工作的 significance framing。\n\n【概率估计】: [28% - 38%] 中位 33%\n\n【估计理由】:\n优势面：(1) novelty claim 成立——坐标约束验证作为几何解析 RL reward 确实无人做过；(2) 实验设计在 proposal 阶段已经非常完备，大幅降低了\"实验不充分\"被拒的风险；(3) 故事线清晰，两个 limitation → 一个解决方案的叙事有说服力；(4) semi-supervised 训练范式有实际推广价值。\n\n劣势面：(1) 技术深度有限——核心方法是标准计算几何操作作为 reward，没有新算法/新理论贡献；(2) 研究范围较窄，仅限于几何解析的 reward 信号改进；(3) 96.4 F1 baseline 下的提升空间受限，如果 end-to-end solving 改善不够显著，paper 的 impact 会被质疑；(4) 关键 benchmark 的坐标可用性存在不确定性。\n\n综合来看，这是一篇方向正确、实验充分、但技术贡献偏轻的 proposal。在 AAAI 审稿中，这类 \"clean insight + thorough experiments\" 的工作如果实验结果扎实，可以被接收，但也容易因为 novelty 不足被 borderline reject。中位概率 33% 反映了这种不确定性。\n\n【主要风险】:\n1. **提升幅度不够显著**: 96.4 F1 的 baseline 意味着 parsing 层面的绝对提升可能很小（<1 F1），如果 end-to-end solving accuracy 的改善也有限（<2-3%），审稿人会质疑这个工作的 practical significance。\n2. **技术贡献深度不足以支撑顶会**: 核心方法（坐标验证 → reward）的技术复杂度低，审稿人可能认为这更接近一个\"好的工程实践\"而非\"研究贡献\"。如果 Tier B (FGPS joint verification) 效果相当或更好且开销可接受，CCV 的独立价值进一步被削弱。\n\n【实施评估】:\n  - 计算资源: 中等。Qwen3-VL-4B GRPO 训练需 4-8 张 A100 GPU，约 1-2 天/实验配置。总计含所有消融约 200-400 GPU hours。\n  - 数据需求: formalgeo7k（坐标确认可用）、GDP-29K（Geoparsing 已有）、Geometry3K/PGPS9K（坐标待确认）。无需新标注，但可能需要对现有 benchmark 补充坐标提取。\n  - 人工介入: 低。CCV verifier 实现为自动化 NumPy 检查。可能需要少量人工验证 tolerance 参数在不同 predicate 类型上的适用性。\n  - 训练需求: 需要训练。SFT 初始化 + GRPO RL，多组消融（≥3 seeds × 7 ablation groups = 21+ 训练 run）。\n  - 新 Benchmark: 不需要构建新 benchmark，使用现有 formalgeo7k / GDP-3K / Geometry3K / PGPS9K。\n  - 预估周期: 6-8 周。Week 1-2: CCV verifier 实现 + pre-experiment error analysis；Week 3-5: 主实验 + 消融；Week 6-7: semi-supervised 实验 + error analysis；Week 8: 论文撰写。前提是 Geometry3K/GDP-3K 坐标可用性能快速确认。\n```\n\nSources:\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry (ACL 2026)](https://arxiv.org/abs/2604.11600)\n- [CGD-Bridge: Concise Geometric Description as a Bridge (CVPR 2026)](https://arxiv.org/abs/2601.21164)\n- [GeoDPO: Enhancing Geometric Perception via Translator-Guided RL (ICLR 2026)](https://arxiv.org/abs/2602.22703)\n- [SIRL: Solver-Informed RL for Optimization Modeling (NeurIPS 2025)](https://arxiv.org/abs/2505.11792)\n- [Bad Seeing or Bad Thinking? Rewarding Perception for VL Reasoning](https://arxiv.org/abs/2605.14054)\n- [FormalGeo: Extensible Formalized Framework for Geometry](https://arxiv.org/abs/2310.18021)\n- [formalgeo7k GitHub repository](https://github.com/BitSecret/formalgeo7k)\n- [Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition](https://arxiv.org/html/2508.19652v1)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile the full evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Geoparsing (arXiv:2604.11600)](https://arxiv.org/abs/2604.11600) (ACL 2026): 当前最直接的 baseline。在 Qwen3-VL-4B 上用 SFT + RLVR 达到 96.4 F1 的 CDL 解析，其 verifier 仅检查句法正确性和局部几何一致性（参数类型、元数、结构有效性），不涉及跨谓词的坐标级约束验证。GDP-29K 数据集为本 proposal 的主要训练数据来源。\n- [CGD-Bridge (arXiv:2601.21164)](https://arxiv.org/abs/2601.21164) (CVPR 2026): 用 CDL matching reward + GRPO 训练 MLLM Interpreter 生成 CDL。关键发现：CDL matching rewards 比 solution-based rewards 在 GRPO 训练中更有效。但其 reward 基于 GT CDL 表面形式匹配，存在 proposal 指出的 representation sensitivity 问题。\n- [GeoDPO (arXiv:2602.22703)](https://arxiv.org/abs/2602.22703) (ICLR 2026): 用 NL-to-DSL translator 计算细粒度 DSL-level score 作为 RL reward，增强 VLM 几何感知能力。+26.5% 域内提升。依赖 translator 训练数据，存在 annotation dependence。\n- [SIRL (arXiv:2505.11792)](https://arxiv.org/abs/2505.11792): 将优化求解器作为 verifier 提供 syntax/feasibility/solution-quality 三级 reward，7B 模型超越 DeepSeek-V3 和 o3。这是本 proposal \"solver-as-verifier\" 范式的直接跨领域先驱，但 SIRL 处理的是文本到优化模型，而非视觉输入到结构化解析。\n- [Hilbert-Geo (arXiv:2605.16385)](https://arxiv.org/abs/2605.16385) (CVPR 2026): Parse2Reason 流水线，在 PlaneFGeo3k 达 80.2%。识别 CDL distortion 为主要失败模式但无反馈机制——间接支持本 proposal 的动机。\n- [SGVR (arXiv:2601.05073)](https://arxiv.org/abs/2601.05073): 用 sub-goal verifiable reward 为几何推理提供 dense reward，+9.7% 几何性能。但作用于推理阶段而非感知阶段。\n- [PRCO (arXiv:2603.28618)](https://arxiv.org/abs/2603.28618): 感知-推理协同进化框架，Observer+Solver 双角色，用 utility reward 反馈给感知模块。验证了感知端独立 reward 信号的价值。\n- [\"Bad Seeing or Bad Thinking?\" (arXiv:2605.14054)](https://arxiv.org/abs/2605.14054): 提出 Perception Verification (PV)，独立奖励感知保真度。与本 proposal 的感知级 reward 设计理念一致，但该工作使用学习型 proxy 而非形式化数学验证。\n- [FormalGeo (arXiv:2310.18021)](https://arxiv.org/abs/2310.18021): 88 个几何谓词 + 196 条定理，formalgeo7k 含 6981 题，提供 GeoGebra 标注的点坐标。FGPS 求解器是 proposal 中 Tier B oracle 的基础。\n- [AutoGPS (arXiv:2505.23381)](https://arxiv.org/abs/2505.23381): MPF+DSR 框架，Geometry3K 上 81.6%，具有运行时反馈但无 RL 训练信号。\n\n- **调研总结**: 几何图解析领域在 2025-2026 年经历了快速发展，形成了 SFT+RL 训练感知模块的明确趋势。当前所有 RL reward 设计（规则验证、GT 匹配、translator-guided）均不利用坐标级约束满足性，这是一个未被填补的空白。同时，感知-推理 reward 解耦（PRCO、PV、SIRL）是更广泛的研究趋势，本 proposal 可以自然嵌入这一趋势。但需注意：(1) 96.4 F1 的高 baseline 限制了绝对提升空间；(2) 坐标可用性限制了实验规模。\n\n【整体印象】:\n作为审稿人，我的第一反应是：这是一个 **clean、well-motivated 的 idea**，问题定义清晰，技术路线自然，实验设计异常完备。Proposal 的学术素养很高——它准确识别了现有 reward 设计的两个真实局限（representation sensitivity 和 annotation dependence），并提出了一个在数学上优雅的解决方案。\"用坐标验证谓词满足性作为 reward\" 这个 idea 有一种 \"为什么之前没人做\" 的感觉，这通常是好 idea 的标志。\n\n然而，我会倾向于 **borderline**，原因有三：(1) 核心技术贡献的 novelty 偏窄——本质上是为现有 GRPO pipeline 设计了一个新的 reward function，没有新的算法或架构创新；(2) 改进天花板不确定——在 96.4 F1 baseline 上能有多少提升，以及这些提升能否显著传导到下游 solving accuracy，proposal 自己也只能假设；(3) 坐标可用性问题使得完整实验可能仅限于 formalgeo7k 一个数据集。但极其完善的实验设计（7 组 ablation、pre-experiment error analysis、training vs. inference 对比）是明显的加分项。\n\n【核心贡献】:\n1. **Coordinate Constraint Verification (CCV) reward**：一种基于坐标级几何约束满足性的 RL reward 信号，具有 representation-invariance 和 annotation-efficiency 两个理论优势。\n2. **CDL-annotation-free training paradigm**：仅需点坐标即可进行 RLVR 训练的半监督范式。\n3. **系统性对比研究**：对几何解析领域三类 reward 设计（rule-based、GT-matching、constraint-grounded）的全面实验对比。\n\n贡献 1 是主要贡献，在概念层面有价值——它将 \"形式化验证作为 reward\" 的 SIRL 范式迁移到视觉几何感知领域，并增加了 per-predicate 粒度和视觉输入的独特挑战。但贡献的深度取决于实验结果能否验证 key hypothesis（CCV 对多谓词不一致性错误的不成比例减少）。\n\n【方法合理性】:\n方法在技术上是 **完全合理** 的。用坐标验证几何谓词是数学上严格的——Parallel 检查斜率相等、Collinear 检查三角形面积为零等，这些都是解析几何的基本运算。微秒级的向量化 NumPy 计算使其在 RL 训练中不会成为瓶颈。\n\n**潜在替代方案的考虑**:\n- Proposal 已经讨论了 \"扩展规则验证器\" 的替代方案并合理地 argue 了其不可行性（组合爆炸）。\n- Tier B（FGPS 联合约束可满足性）是一个更强但更慢的替代方案，proposal 正确地将其定位为 oracle 比较。\n- 一个未被充分讨论的替代方案是：CCV 作为 inference-time reranker 而非 RL reward。Proposal 在 Baseline 6 和 Ablation 7 中设计了这个对比，这是方法论上的加分。\n\n**关键技术风险**：tolerance 参数的设定对 reward 质量至关重要。坐标噪声（来自 GeoGebra 标注或视觉检测的误差）可能导致 false negatives（正确谓词被判为不满足）或 false positives（错误谓词因容差过大被判为满足）。5 级 tolerance ablation 是合理的缓解措施，但 proposal 应更深入讨论坐标精度对 CCV 可靠性的影响。\n\n【5 维度打分】:\n  1. 研究问题: 【中偏强】 — Representation sensitivity 和 annotation dependence 是 geometry diagram parsing RL 方法中的真实问题，Hilbert-Geo 识别的 \"CDL distortion as primary failure mode\" 从侧面支持了这一研究动机。但该问题的影响范围相对较窄（仅限几何图解析的 RL reward 设计），且在 96.4 F1 的高 baseline 下，实际问题的严重程度有待实验验证。\n\n  2. 方法与创新: 【中】 — CCV 的概念自然、技术合理，SIRL（arXiv:2505.11792）已证明 solver-as-verifier 范式在优化领域的有效性，本 proposal 将其迁移到视觉几何感知是合理的领域适配。但核心 novelty 偏窄：(a) 与 SIRL 的差异主要在于领域（视觉输入 + per-predicate 粒度），方法论框架相似；(b) 与 \"Bad Seeing or Bad Thinking?\" (arXiv:2605.14054) 的 Perception Verification 在理念上有重叠，区别在于本 proposal 使用形式化数学验证而非学习型 proxy；(c) CCV 本身是解析几何基本运算的直接应用，技术深度有限。representation-invariance 是一个优雅的理论性质，但其实际价值取决于 GT 表面形式偏差在训练中造成多大的 reward corruption。\n\n  3. 实验设计: 【强】 — 这是 proposal 最突出的优势。6 个 baselines 覆盖了领域内所有主要方法（Geoparsing、CGD-Bridge、GeoDPO、AutoGPS）以及关键消融基线（SFT-only、CCV reranking）。7 组 ablation 全面覆盖 reward type、granularity、tolerance、optimizer、initialization、constraint type、training vs. inference。Pre-experiment error analysis 和 semi-supervised experiment 展示了很高的方法论素养。统计严谨性（≥3 seeds, paired bootstrap test）和计算公平性（GPU-hour matched comparison）超过领域平均水平。唯一弱点：坐标可用性问题可能使完整 CCV 实验仅限于 formalgeo7k。\n\n  4. 可行性: 【中偏强】 — 技术实现可行性高：CCV 验证是标准数学运算，Qwen3-VL-4B + GRPO 训练管线可复用 Geoparsing 和 CGD-Bridge 的公开代码。计算需求适中（4B 模型 + 微秒级 reward 计算）。主要风险：(a) Geometry3K 和 GDP-3K 的坐标可用性未确认，可能需要额外的点检测工作或缩小实验范围；(b) tolerance 调优可能需要大量预实验；(c) 如果 96.4 F1 baseline 上的多谓词不一致性错误数量很少，key hypothesis 可能无法验证。\n\n  5. 写作与呈现: 【强】 — Proposal 逻辑清晰、层次分明。Research Opportunity 部分精准定位两个 limitations 并解释 CCV 如何同时解决两者。\"Why not extend rule-based verifiers?\" 的主动回答展示了审稿人视角的意识。Cross-domain precedent 和 Research Landscape 的梳理全面准确。Oracle tiers 的设计和 representation-invariance example 增强了说服力。唯一建议：对 tolerance sensitivity 和坐标精度的讨论可以更深入。\n\n【概率估计】: [28% - 38%] 中位 33%\n\n【估计理由】:\n- **上行因素** (推向 38%): (1) 实验设计的完备性在 AAAI 投稿中属于 top-tier，审稿人很难在实验方案上找到明显漏洞；(2) idea 的优雅性——\"坐标约束满足性作为 reward\" 概念上简洁、数学上严格、动机清晰；(3) 嵌入感知-推理 reward 解耦的更广泛趋势（PRCO、PV、SIRL），positioning 合理；(4) semi-supervised 训练范式有独立的实用价值。\n- **下行因素** (推向 28%): (1) 核心 novelty 偏窄——本质是一个新 reward function，没有新算法/架构贡献，SIRL 已证明 solver-as-verifier 范式的有效性，本 proposal 是领域迁移；(2) 改进天花板不确定——96.4 F1 baseline 上多谓词不一致性错误的实际占比未知，如果很少则 key hypothesis 不成立；(3) 实验范围可能受限于单一数据集（formalgeo7k）；(4) 子领域较窄（几何图解析），审稿人池和影响力受限。\n- **中位 33%** 的逻辑：这是一篇整体合格、方向正确、实验扎实的投稿，但缺乏突出的 novelty 或广泛的影响力来进入 top 区间。在 AAAI 的竞争中，它属于 \"solid but not exciting\" 的范畴——不太会被强 reject，但也不容易拿到 strong accept。\n\n【主要风险】:\n1. **改进天花板过低**: 在 96.4 F1 的高 baseline 下，CCV 能修正的多谓词不一致性错误可能数量有限，导致实验提升微小（<1% 绝对值），难以说服审稿人这是一个有实质性影响的贡献。Pre-experiment error analysis 可以提前揭示这个风险，但如果分析结果不乐观，整个 proposal 的价值主张会被严重削弱。\n2. **Novelty 不足被审稿人质疑**: 审稿人可能认为 \"用坐标验证谓词\" 是一个 straightforward 的工程贡献而非研究贡献，特别是在 SIRL 已建立 solver-as-verifier 范式的背景下。如果 CCV 的实验提升不够显著，这一质疑将更加致命。\n\n【实施评估】:\n  - 计算资源: 中等。Qwen3-VL-4B 的 GRPO 训练需 4-8 张 A100/H100，CCV reward 计算开销可忽略（微秒级 NumPy），但需多个 ablation 实验 × ≥3 seeds。估计总计 200-400 GPU-hours。\n  - 数据需求: GDP-29K（Geoparsing 公开）+ formalgeo7k（公开，含坐标）。Geometry3K 和 GDP-3K 的坐标可用性需确认，可能需要额外的视觉点检测管线。\n  - 人工介入: 低。CCV 验证全自动，主要人工工作在实验配置和分析。如需为缺少坐标的数据集标注/检测点坐标，人工介入中等。\n  - 训练需求: 需要训练。在 Geoparsing SFT checkpoint 基础上进行 GRPO RL 微调，多组实验配置。无需从零预训练。\n  - 新 Benchmark: 不需要构建新 benchmark，使用现有的 formalgeo7k、Geometry3K、PGPS9K、GDP-3K。\n  - 预估周期: 6-10 周。包括：pre-experiment error analysis (1 周) → 坐标可用性确认与处理 (1-2 周) → 主实验训练 (2-3 周) → ablation 实验 (2-3 周) → 分析与写作 (1-2 周)。\n```\n\nSources:\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language](https://arxiv.org/abs/2604.11600)\n- [CGD-Bridge: Concise Geometric Description as a Bridge](https://arxiv.org/abs/2601.21164)\n- [GeoDPO: Enhancing Geometric Perception via Translator-Guided RL](https://arxiv.org/abs/2602.22703)\n- [SIRL: Solver-Informed RL for Optimization Modeling](https://arxiv.org/abs/2505.11792)\n- [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/abs/2605.16385)\n- [SGVR: Milestones over Outcome - Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)\n- [PRCO: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)\n- [Bad Seeing or Bad Thinking? Rewarding Perception for VL Reasoning](https://arxiv.org/abs/2605.14054)\n- [FormalGeo: An Extensible Formalized Framework](https://arxiv.org/abs/2310.18021)\n- [AutoGPS: Automated Geometry Problem Solving](https://arxiv.org/abs/2505.23381)\n- [Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition](https://arxiv.org/abs/2508.19652)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Constraint-Grounded Reward for Geometry Diagram Parsing\n\n## Core Problem\n\nCan geometric constraint verification — checking whether predicted CDL predicates satisfy the diagram's coordinate-level geometric constraints — serve as a representation-invariant, annotation-efficient RL reward for diagram parsers, surpassing both rule-based format rewards and GT-matching rewards that penalize valid alternative representations?\n\n## Research Opportunity\n\nAll components exist but remain unconnected. Geoparsing (ACL 2026) achieves 96.4 F1 CDL parsing via SFT + RLVR with a rule-based verifier checking syntactic correctness and local geometric consistency (argument types, arity, structural validity). CGD-Bridge (CVPR 2026) uses CDL matching rewards (predicted vs. GT CDL) with GRPO. GeoDPO (ICLR 2026) uses translator-guided RL with DSL-level scores. All three reward designs share two fundamental limitations:\n\n**Limitation 1 — Representation sensitivity**: GT-matching rewards (CGD-Bridge) and translator-based rewards (GeoDPO) penalize semantically equivalent but syntactically different CDL representations. Geometry inherently admits multiple valid descriptions of the same configuration (e.g., a triangle can be described via three angle predicates, three side predicates, or mixed). Current rewards treat any deviation from the GT surface form as error, producing false-negative penalties that corrupt the RL signal.\n\n**Limitation 2 — Annotation dependence**: All current CDL-RL methods require full CDL annotations for training. Rule-based rewards need CDL structure definitions; GT-matching needs paired (diagram, CDL) annotations; translator rewards need NL-to-DSL training data. This creates an annotation bottleneck limiting scalability.\n\nGeometric constraint verification resolves both limitations simultaneously. By checking whether predicted predicates are satisfied by the diagram's point coordinates, it provides: (1) **representation-invariant reward** — any CDL set that correctly describes the geometry receives full reward regardless of surface form; (2) **CDL-annotation-free training** — verification requires only point coordinates (obtainable via standard visual point detection), not full CDL annotations, enabling RL training on diagrams with coordinate-only annotation.\n\n**Why not extend rule-based verifiers?** A natural question is whether Geoparsing's rule-based verifier could be extended with pairwise consistency rules (e.g., \"Parallel(l1,l2) ∧ PointOnLine(P,l1) ∧ PointOnLine(P,l2) → Collinear\"). This approach fails at scale: multi-predicate inconsistencies involve combinatorial interactions that cannot be exhaustively enumerated as rules. Coordinate verification is a \"check\" not an \"enumerate\" — it automatically covers all inconsistency types including non-obvious ones, and adapts to new predicate types without manual rule authoring.\n\nCross-domain precedent: SIRL (arXiv:2505.11792) demonstrates solver-as-verifier RL for optimization modeling (syntax/feasibility/solution-quality rewards), achieving SOTA with 7B model. Our work instantiates this paradigm in geometry with unique challenges: visual input (diagram → structured CDL), per-predicate reward granularity (vs. SIRL's problem-level), and geometric constraint coupling across predicates. The broader trend of perception-reasoning reward decomposition — Vision-SR1 (arXiv:2508.19652) decomposes VLM advantage into perception vs. reasoning stages; \"Bad Seeing or Bad Thinking?\" (arXiv:2605.14054) proposes Perception Verification to reward perceptual fidelity independently; PRCO (arXiv 2026) feeds downstream reasoning success back to perception via utility rewards — validates the need for principled perception reward signals. Our constraint-grounded approach differs from these learned/proxy approaches: it provides a formal, deterministic, task-agnostic verification signal derived from mathematical structure, requires no verifier training, and gives per-predicate dense reward rather than problem-level binary feedback.\n\n## Research Landscape\n\n**Parsers with RL**: Geoparsing (ACL 2026) — SFT + RLVR with rule-based local consistency verifier, 96.4 F1; GeoDPO (ICLR 2026) — translator-guided RL, +26.5% perception; CGD-Bridge (CVPR 2026) — CDL matching rewards + GRPO, strong results from 5.5k examples. All use perception-level rewards.\n\n**Sequential pipelines**: Hilbert-Geo (CVPR 2026) — 80.2% on PlaneFGeo3k, sequential parse-then-reason, identifies CDL distortion as primary failure mode but has no feedback; AutoGPS (arXiv 2025) — 81.6% on Geometry3K, MPF+DSR collaboration, runtime feedback but no RL training signal.\n\n**Text-only symbolic solvers**: InternGeometry — 44/50 IMO via DDAR; AlphaGeometry2 — 42/50 via DDAR2 (C++, 300× speedup), both text-only.\n\n**Perception-reasoning reward decomposition**: SIRL (arXiv:2505.11792) — solver verification as RL reward for optimization; PRCO (arXiv 2026) — perception-reasoning coevolution via utility rewards; Vision-SR1 (arXiv:2508.19652) — advantage decomposition into perception/reasoning stages; \"Bad Seeing or Bad Thinking?\" (arXiv:2605.14054) — Perception Verification for VLM reward; SGVR (arXiv 2026) — dense sub-goal rewards for geometric reasoning +37.5%; SVE-Math (arXiv 2025) — visual encoding quality impacts downstream reasoning. GeoPQA (arXiv:2509.17437) trains perception and reasoning separately without solver verification.\n\n**Key gap**: No existing work uses coordinate-level geometric constraint satisfaction as a representation-invariant, annotation-efficient reward for training diagram parsers.\n\n## Proposed Approach\n\nFine-tune Qwen3-VL-4B (Geoparsing's base) via GRPO with geometric constraint verification as the reward signal.\n\n**Primary reward — Coordinate Constraint Verification (CCV)**: For each predicted CDL predicate, instantiate using the diagram's point coordinates and verify numerical satisfaction. Examples: Parallel(l1,l2) → check slope equality within tolerance; Collinear(A,B,C) → check triangle area ≈ 0; Tangent(circle,line) → check distance from center to line ≈ radius. Reward per sample = fraction of constraint-satisfied predicates. This operates at microsecond scale via vectorized NumPy checks.\n\n**Representation-invariance example**: Consider a triangle ABC. GT CDL uses {Triangle(A,B,C), Angle(A,60°), Angle(B,70°)}. An alternative valid description is {Segment(AB), Segment(BC), Segment(CA), Angle(A,60°), Angle(B,70°), Angle(C,50°)}. CDL matching reward: the alternative gets partial match penalty. CCV reward: both get full reward because both satisfy the coordinate constraints.\n\n**Oracle tiers for ablation**:\n- Tier B — Joint constraint satisfiability: submit all predicted predicates to FormalGeo's FGPS as complete constraint system; reward = satisfiable/not. Most semantically powerful but ~0.1–1s per call. Oracle comparison only.\n- Tier C — Solver-guided semantic matching: check predicate entailment against GT constraint system via FormalGeo's theorem library. Intermediate cost.\n\n**Coordinate availability**: formalgeo7k provides GeoGebra-annotated point coordinates directly. For Geometry3K and GDP-3K, coordinate availability must be confirmed; if unavailable, these benchmarks use only rule-based/GT-matching reward variants and serve as cross-system evaluation.\n\n**CDL-annotation-free training**: CCV requires only point coordinates, not CDL annotations. This enables a semi-supervised training paradigm: SFT on fully-annotated data, then CCV-RLVR on coordinate-only data without CDL labels, expanding effective training set beyond annotated corpora.\n\n## Experimental Design\n\n**Baselines** (6 comparisons):\n1. Geoparsing SFT-only (no RL, lower bound)\n2. Geoparsing SFT + rule-based RLVR (direct ablation — same base, same data, different reward)\n3. CGD-Bridge (CDL matching rewards + GRPO)\n4. GeoDPO (translator-guided RL reward)\n5. AutoGPS (MPF+DSR, current end-to-end SOTA on Geometry3K at 81.6%)\n6. Geoparsing SFT+RLVR + CCV reranking (inference-time baseline — generate k candidates, select by CCV score; isolates whether CCV's value comes from signal quality or from RL training)\n\n**Benchmarks** (tiered by coordinate availability):\n- **Primary (coordinates confirmed)**: Formalgeo7k — full CCV reward + all ablations; enables direct comparison with CGD-Bridge\n- **Standard solving benchmarks**: Geometry3K, PGPS9K — end-to-end solving accuracy; CCV reward if coordinates available, otherwise rule-based/GT-matching variants\n- **Parsing quality**: GDP-3K (PGDP-2K + SGDP-1K) — direct comparison with Geoparsing\n\n**Primary evaluation metric**: End-to-end solving accuracy (not parsing F1). Rationale: at 96.4 F1 baseline, parsing improvements may be small in absolute terms but disproportionately impact solving because multi-predicate inconsistencies invalidate entire proof chains.\n\n**Pre-experiment error analysis** (before RL training): Run CCV on Geoparsing baseline outputs to (a) classify errors into single-predicate errors vs. multi-predicate inconsistency errors, (b) quantify each error type's contribution to end-to-end solving failures, (c) estimate CCV reward's achievable improvement ceiling.\n\n**Ablation studies** (7 groups):\n1. Reward type: rule-based vs. CDL matching vs. CCV vs. joint constraint (Tier B) — isolates constraint verification's incremental contribution\n2. Reward granularity: per-predicate dense vs. diagram-level binary\n3. CCV tolerance sensitivity: 5 tolerance levels (1e-6 to 1e-1) — measures precision/recall tradeoff of reward signal\n4. RL optimizer: GRPO vs. PPO (following SGVR's design)\n5. SFT initialization: random init vs. Geoparsing SFT init\n6. Constraint type decomposition: angle-only vs. distance-only vs. full CCV (backup for Newclid ablation if format bridging infeasible)\n7. Training vs. inference: CCV as RL reward vs. CCV as inference-time reranker (isolates RL training's necessity)\n\n**Semi-supervised experiment**: Split training data into annotated portion (CDL + coordinates, used for SFT) and coordinate-only portion (CDL labels withheld, used for CCV-RLVR only). Compare: (a) SFT on annotated only, (b) SFT + rule-based RLVR on annotated only, (c) SFT on annotated + CCV-RLVR on coordinate-only — quantifies CDL-annotation-free training's value.\n\n**Training data configuration**: Primary comparison uses Geoparsing's GDP-29K for controlled comparison (same data, different reward). Cross-system evaluation on formalgeo7k uses CGD-Bridge's train/test split. Semi-supervised experiment uses GDP-29K split with held-out CDL labels.\n\n**Statistical rigor**: All experiments run with ≥3 random seeds, reporting mean ± std. Key comparisons (CCV vs. rule-based RLVR) use paired bootstrap test with p-values. Per-instance analysis for fine-grained error category improvements.\n\n**Error analysis**: Taxonomy of single-predicate errors vs. multi-predicate inconsistencies; per-category reduction rates; case studies showing inconsistencies caught by CCV but missed by rule-based/GT-matching rewards; \"cascading fix\" analysis quantifying how resolving one inconsistency impacts downstream solving.\n\n**Compute fairness**: Report wall-clock time and GPU hours for all methods. Compute-matched comparison under same GPU-hour budget. Performance vs. training compute curves.\n\n## Key Hypothesis\n\nCCV rewards disproportionately reduce multi-predicate inconsistency errors — cases where individual predicates are locally valid but jointly violate geometric constraints. While potentially a minority of total parsing errors, these inconsistencies cause disproportionate end-to-end solving failures because a single geometric contradiction invalidates entire proof chains. The representation-invariant property additionally eliminates false-negative reward penalties that corrupt RL training under GT-matching rewards.\n\n## Key References\n\n- Geoparsing: Diagram Parsing with Unified Formal Language (ACL 2026)\n- Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning (CVPR 2026)\n- Milestones over Outcome: Sub-Goal Verifiable Reward [SGVR] (arXiv 2026)\n- AlphaGeometry2: Gold-medalist Olympiad Geometry (arXiv 2025)\n- InternGeometry: Olympia-Level Geometry LLM Agent (arXiv 2025)\n- AutoGPS: Automated Geometry Problem Solving (arXiv 2025)\n- Enhancing Geometric Perception via Translator-Guided RL [GeoDPO] (ICLR 2026)\n- Concise Geometric Description as a Bridge [CGD-Bridge] (CVPR 2026)\n- Open Eyes Then Reason: SVE-Math (arXiv 2025)\n- PRCO: Perception-Reasoning Coevolution (arXiv 2026)\n- Solver-Informed RL [SIRL] (arXiv:2505.11792)\n- FormalGeo: Extensible Formalized Framework (arXiv:2310.18021)\n- Newclid: A User-Friendly Replacement for AlphaGeometry (arXiv:2411.11938)\n- GeoPQA: Two-Stage RL for Geometry (arXiv:2509.17437)\n- Bad Seeing or Bad Thinking? Rewarding Perception for VL Reasoning (arXiv:2605.14054)\n- Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition (arXiv:2508.19652)"
}
````

---

### Runtime record

_source line 2 · 2026-05-29T06:41:20.458Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:41:20.458Z",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-29T06:41:20.507Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient background to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Geoparsing (arXiv:2604.11600)](https://arxiv.org/abs/2604.11600) (ACL 2026): 最直接的基线。使用 SFT + RLVR（基于规则的本地一致性验证器）在 GDP-29K 上训练 Qwen3-VL-4B，CDL 解析达到 96.4 F1。验证器检查句法正确性、参数类型、元数等，但不检查坐标级约束满足。本 proposal 在其之上改进 reward 信号。
- [CGD-Bridge (arXiv:2601.21164)](https://arxiv.org/html/2601.21164) (CVPR 2026): 使用 CDL 匹配奖励 + GRPO，将生成的 CDL 与 GT CDL 逐项匹配作为 reward。在 formalgeo7k 上训练。Proposal 正确指出其 representation sensitivity 问题——匹配奖励惩罚语义等价但形式不同的 CDL 表示。
- [GeoDPO (arXiv:2602.22703)](https://arxiv.org/abs/2602.22703) (ICLR 2026): 翻译器引导的 RL，用 NL-to-DSL 翻译器计算 DSL 级分数作为 reward，获得 +26.5% 域内感知提升和 +39% 下游推理提升。依赖翻译器训练数据，存在 annotation dependence 问题。
- [SIRL (arXiv:2505.11792)](https://arxiv.org/abs/2505.11792) (arXiv 2025): Solver-as-verifier RL 用于优化建模，使用外部求解器提供 syntax/feasibility/solution-quality 三级 reward。7B 模型超过 DeepSeek-V3 和 o3。本 proposal 的最重要跨领域先例，验证了"外部形式化验证器作 RL reward"范式的有效性。
- [SGVR (arXiv:2601.05073)](https://arxiv.org/abs/2601.05073) (arXiv 2026): 子目标可验证奖励，将抽象证明转化为可验证数值子目标，用 Skeleton Rate 作为密集 reward。几何推理 +9.7%，通用数学 +8.0%。与本 proposal 共享"密集可验证奖励"理念，但 SGVR 面向推理阶段，本 proposal 面向感知阶段。
- [PRCO (arXiv:2603.28618)](https://arxiv.org/abs/2603.28618) (arXiv 2026): 感知-推理协同进化，Observer 生成证据 caption，Solver 基于 caption 推理。Observer 通过 Solver 的 utility reward 获得间接监督。与本 proposal 共享"感知阶段需要独立 reward"的动机，但 PRCO 使用间接/学习信号，CCV 使用直接/形式化信号。
- ["Bad Seeing or Bad Thinking?" (arXiv:2605.14054)](https://arxiv.org/abs/2605.14054) (arXiv 2026): 提出 Perception Verification 作为 VLM reward，解决感知-推理的 credit assignment 模糊问题。验证了 proposal 的核心前提：感知阶段需要独立的、基于验证的 reward 信号。
- [FormalGeo (arXiv:2310.18021)](https://arxiv.org/abs/2310.18021): 88 个几何谓词 + 196 条定理的形式化框架。formalgeo7k 数据集提供 GeoGebra 标注的点坐标——这是本 proposal CCV reward 的关键数据来源。

- **调研总结**: 几何图表解析的 RL 训练是 2025-2026 年的活跃研究方向，已有多种 reward 设计（规则验证、GT 匹配、翻译器引导），但**无人使用坐标级几何约束满足作为 reward**。Proposal 的 novelty claim 成立。同时，"感知阶段需要独立可验证 reward"的大趋势（PRCO、Vision-SR1、"Bad Seeing or Bad Thinking?"）为本工作提供了理论支撑。主要竞争对手是 Geoparsing（同 base model，同数据，不同 reward）。

【整体印象】:
作为审稿人，我的第一反应是**borderline positive**。这是一篇思路清晰、定位精准的工作：在一个活跃的研究方向上，识别了现有 reward 设计的两个真实局限（表示敏感性、标注依赖），并提出了一个简洁优雅的解决方案。核心 idea（用坐标约束验证替代 GT 匹配/规则验证作为 RL reward）概念上自然、技术上可行。实验设计异常全面——6 个 baseline、7 组 ablation、统计显著性测试、误差分析，这本身就是一个强加分项。

**但我有两个主要顾虑**：(1) 核心技术贡献的深度——"检查谓词是否满足坐标约束"这件事本身并不复杂，novelty 可能被质疑为"engineering trick"而非"研究贡献"；(2) 改进空间不确定——在 96.4 F1 的 baseline 上，parsing 层面的提升可能非常有限，虽然 proposal 合理地论证了对端到端求解的放大效应，但这需要实验验证。

我会倾向给一个 weak accept，前提是实验结果能显示清晰的端到端求解提升和半监督训练的价值。

【核心贡献】:
1. **坐标约束验证（CCV）作为表示不变的 RL reward**：消除 GT 匹配奖励中的假阴性惩罚，任何几何上正确的 CDL 表示都能获得完整奖励。
2. **CDL 标注无关训练**：CCV 仅需点坐标（不需要 CDL 标注），使半监督 RL 训练成为可能。
3. **系统性的实验设计**：包括训练-推理分离实验（CCV 作为 reranker vs. 作为 RL reward）、多层次 oracle 对比、半监督实验。

对领域的价值：**中等偏高**。如果半监督训练路径有效，这将打破几何解析 RL 训练的标注瓶颈，具有实际扩展意义。表示不变性是一个原则性改进。但如果仅仅是 parsing F1 的微小提升，价值会大幅下降。

【方法合理性】:
方法合理性**总体良好**，但有几个需要审视的点：

1. **逐谓词独立验证 vs. 联合约束满足**：CCV 逐个谓词验证坐标满足，这能捕获单谓词错误，但对于多谓词联合不一致性（每个谓词单独看在容差内但联合矛盾），效果可能有限。Proposal 意识到了这一点并设计了 Tier B（联合约束可满足性）作为 oracle 对比，这是正确的。但核心方法（Tier A/CCV）的局限需要诚实报告。

2. **数值容差的鲁棒性**：几何图表的坐标可能来自不同来源（GeoGebra 精确标注 vs. 图像点检测估计），精度差异大。容差选择可能成为一个不那么 trivial 的工程问题。Proposal 计划 5 级容差 ablation（1e-6 到 1e-1），这很好。

3. **是否存在更简单的替代方案？** 一个审稿人可能会问：与其在 RL 训练中使用 CCV reward，直接用 CCV 做推理时 reranking（生成 k 个候选，按 CCV 分数选择）是否就够了？Proposal 很聪明地把这个作为 baseline 6 纳入了实验设计，这消除了最大的方法论质疑。

4. **坐标可用性假设**：formalgeo7k 有精确坐标，但 Geometry3K/GDP-3K 可能没有。这限制了方法的通用性。如果需要视觉点检测来获取坐标，那么坐标的噪声会直接影响 CCV reward 的质量，形成一个"感知误差 → reward 噪声 → 训练信号失真"的级联问题。

【5 维度打分】:

1. **研究问题: 强** — 几何解析的 RL reward 设计是当前活跃且重要的研究问题。Proposal 识别的两个局限（表示敏感性、标注依赖）在 Geoparsing、CGD-Bridge、GeoDPO 中确实存在，不是人为构造的问题。"感知阶段需要独立的形式化 reward"这一方向得到了 PRCO、"Bad Seeing or Bad Thinking?"、Vision-SR1 等多项同期工作的验证。问题的实际意义也清晰：CDL 解析错误是端到端几何求解的主要瓶颈（Hilbert-Geo 已指出）。

2. **方法与创新: 中** — 核心 idea 概念上自然且正确——用坐标约束验证替代表面形式匹配是一个原则性改进。但技术深度有限："对每个谓词，用坐标验证数值满足"这一操作本身是直接的工程实现（检查斜率相等、面积为零、距离等于半径等），不涉及新的算法设计或理论贡献。与 SIRL（solver-as-verifier for optimization）的关系类似"将已有范式应用到新领域"。Novelty 的核心价值在于识别问题和连接已有组件，而非方法本身的技术创新。相比 GeoDPO（设计翻译器引导的 reward）或 SGVR（设计子目标可验证 reward 框架），本工作的技术深度较浅。但 representation-invariance 和 annotation-free 两个性质的结合是一个有意义的贡献点。

3. **实验设计: 强** — 这是本 proposal 最突出的优势。6 个 baseline（包括非常必要的 CCV-reranking 推理时 baseline），7 组 ablation（reward 类型、粒度、容差、优化器、初始化、约束类型分解、训练 vs. 推理），半监督实验，预实验误差分析，统计显著性测试（≥3 seeds + paired bootstrap），compute fairness——实验方案的完备程度远超同领域平均水平。特别值得肯定的是：(a) CCV reranking baseline 直接回答了"是否需要 RL 训练"这个核心方法论问题；(b) 半监督实验是验证 annotation-free 贡献的必要设计；(c) 预实验误差分析量化了改进天花板，避免了"做了但没用"的风险。

4. **可行性: 强** — 所有技术组件已存在：Qwen3-VL-4B（base model）、GRPO（RL 算法）、FormalGeo/formalgeo7k（形式化框架和数据集）、NumPy 向量化检查（CCV 实现）。计算需求合理（4B 模型 + 微秒级 reward 计算）。主要风险是坐标可用性（Geometry3K/GDP-3K），但 proposal 已有降级方案（这些 benchmark 只用规则/匹配 reward）。

5. **写作与呈现: 强** — Proposal 逻辑清晰，从 problem → opportunity → approach → experiments 的叙事流畅。对现有工作的定位精准，既不过度贬低也不过度抬高自身。"Why not extend rule-based verifiers?" 这个反驳段落预判了审稿人的自然质疑。研究假设明确可检验。唯一的小问题是 proposal 长度偏长，实际写成论文时需要大幅精简。

【概率估计】: [28% - 40%] 中位 33%

【估计理由】:
向上推力：(1) 研究问题时效性强，2025-2026 年几何解析 RL 是热点方向；(2) Novelty claim 成立——确实无人用坐标约束验证作为 parsing RL reward；(3) 实验设计非常完备，远超领域平均水平，这在审稿中是实质加分；(4) 半监督训练路径（CCV-RLVR on coordinate-only data）是有实际价值的独立贡献；(5) 与同期感知-推理分离趋势（PRCO、"Bad Seeing or Bad Thinking?"）高度契合。

向下压力：(1) 核心技术贡献深度有限——"用坐标检查谓词满足"概念直接，可能被部分审稿人视为 engineering contribution 而非 research contribution；(2) 在 96.4 F1 的 baseline 上，提升空间有限，如果端到端求解提升不显著则说服力大减；(3) 主要对比限于 formalgeo7k（坐标已确认可用），benchmark 覆盖面偏窄；(4) 逐谓词独立验证可能无法充分捕获多谓词联合不一致性——而这恰恰是 proposal 的核心假设（"disproportionately reduce multi-predicate inconsistency errors"）；(5) 竞争激烈——Geoparsing、CGD-Bridge、GeoDPO、SGVR 等多项强工作同期发表，审稿人对"又一种 reward 设计"可能产生审美疲劳。

综合判断：这是一篇 solid 但不 outstanding 的投稿。方向正确、定位精准、实验全面，但核心技术创新的深度是软肋。如果实验结果强（端到端求解有显著提升，半监督路径有效），概率向 40% 靠近；如果提升微弱，则接近下界。33% 反映了"实验结果中等"的预期情景。

【主要风险】:
1. **Novelty 深度不足**：核心方法（逐谓词坐标验证）技术上过于直接，可能被审稿人评为"缺乏足够的技术创新"或"SIRL 在几何领域的直接应用"。这是最可能触发 reject 的风险。
2. **改进幅度不足**：在 96.4 F1 的 baseline 上，如果端到端求解精度提升仅为 1-2 个百分点，审稿人可能认为贡献不足以支撑一篇顶会论文。核心假设（"多谓词不一致性导致不成比例的求解失败"）需要强有力的实证支持。

【实施评估】:
  - 计算资源: 中等偏低。Qwen3-VL-4B 的 GRPO 训练在 4×A100 上数天可完成；CCV reward 计算为微秒级 NumPy 操作，几乎无额外开销。Tier B（FGPS 联合验证）较慢（~0.1-1s/call）但仅作 oracle 对比。
  - 数据需求: formalgeo7k（已公开，含坐标）为主实验数据源；GDP-29K（Geoparsing 提供）用于训练；Geometry3K/PGPS9K 用于评测。所有数据集已公开可用。坐标可用性需确认 Geometry3K/GDP-3K。
  - 人工介入: 低。CCV 验证逻辑（~88 谓词的坐标检查）需要手动实现，但每个谓词的检查逻辑是简单的数值计算。可能需要少量工程工作来桥接 FormalGeo 的谓词格式。
  - 训练需求: 需要 RL 微调 Qwen3-VL-4B（GRPO），需要 SFT 预训练作为初始化。共计 ~2-3 轮训练（SFT + 多种 reward 的 RL 对比）。
  - 新 Benchmark: 不需要构建新 benchmark。使用已有的 formalgeo7k、Geometry3K、PGPS9K、GDP-3K。
  - 预估周期: 8-12 周。包括：CCV 实现与验证（1-2 周）、预实验误差分析（1 周）、主实验 RL 训练与对比（3-4 周，多 baseline × 多 seed）、ablation 实验（2-3 周）、论文写作（2-3 周）。
```

Sources:
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language](https://arxiv.org/abs/2604.11600)
- [CGD-Bridge: Concise Geometric Description as a Bridge](https://arxiv.org/html/2601.21164)
- [GeoDPO: Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning](https://arxiv.org/abs/2602.22703)
- [SIRL: Solver-Informed RL for Optimization Modeling](https://arxiv.org/abs/2505.11792)
- [SGVR: Milestones over Outcome](https://arxiv.org/abs/2601.05073)
- [FormalGeo: An Extensible Formalized Framework](https://arxiv.org/abs/2310.18021)
- [PRCO: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)
- [Bad Seeing or Bad Thinking? Rewarding Perception for VL Reasoning](https://arxiv.org/abs/2605.14054)
- [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/html/2605.16385)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a comprehensive evaluation. Let me synthesize all findings.

---

```
【阶段】: Triage

【领域调研】:
- [Geoparsing (arXiv:2604.11600)](https://arxiv.org/abs/2604.11600) (ACL 2026): 直接前置工作。使用 Qwen3-VL-4B 做 SFT + RLVR，rule-based verifier 检查语法和局部几何一致性，达到 96.4 F1。本 proposal 的直接 baseline 和起点。
- [CGD-Bridge (arXiv:2601.21164)](https://arxiv.org/abs/2601.21164) (CVPR 2026): 用 CDL matching rewards + GRPO 训练 MLLM Interpreter，仅 5.5k 数据即有竞争力。其 CDL matching reward 是 piece-by-piece greedy matching（recall + precision），正是本 proposal 指出的"representation-sensitive"问题的典型代表。
- [GeoDPO (arXiv:2602.22703)](https://arxiv.org/abs/2602.22703) (ICLR 2026): translator-guided RL，NL→DSL translator 计算 DSL-level reward，+26.5% in-domain，+39% 下游推理。需要训练额外 translator 模型，是本 proposal 指出的"annotation dependence"问题的例证。
- [SIRL (arXiv:2505.11792)](https://arxiv.org/abs/2505.11792) (NeurIPS 2025): solver-as-verifier RL 用于优化建模，syntax/feasibility/solution-quality 三级 reward。本 proposal 的跨领域 precedent，验证了 solver verification 作为 RL reward 的范式可行性。
- [Bad Seeing or Bad Thinking? (arXiv:2605.14054)](https://arxiv.org/abs/2605.14054) (arXiv 2026): Perception Verification 独立奖励感知忠实度，Modality-Aware Credit Assignment 区分感知/推理错误。属于 perception-reasoning decomposition 趋势的最新工作，与本 proposal 的 perception-level reward 设计形成互补定位。
- [FormalGeo (arXiv:2310.18021)](https://arxiv.org/abs/2310.18021): 提供 formalgeo7k 数据集，含 GeoGebra 标注的点坐标和 88 predicates/196 theorems 的形式化系统。本 proposal 的 CCV reward 依赖此数据集的坐标标注。

- **调研总结**: 几何图形解析的 RL reward 设计是 2025-2026 年的活跃方向，已有 rule-based (Geoparsing)、CDL matching (CGD-Bridge)、translator-guided (GeoDPO) 三种 reward 范式。坐标级几何约束满足性作为 RL reward 尚无人做，是一个真实的空白点。但这个空白点的影响范围较窄（仅限于几何解析的 reward 信号改进），且 baseline 已经很强（96.4 F1），提升空间受限。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇动机清晰、方法简洁、实验设计极为充分的 proposal，但核心贡献的量级（novelty depth）让我犹豫。核心 idea 可以用一句话概括："用坐标约束验证替代字符串匹配作为几何解析的 RL reward"。这个 idea 合理且有效，但技术深度有限——坐标级几何验证（检查斜率相等、面积为零、距离等于半径等）本身是计算几何的基础操作，将其包装为 RL reward 的工程复杂度不高。我会倾向于 borderline/weak accept，取决于实验结果能否展示出令人信服的提升，尤其是在 end-to-end solving accuracy 上的改善。

【核心贡献】:
1. 提出坐标约束验证（CCV）作为几何解析的 RL reward，具有 representation-invariant 和 CDL-annotation-free 两个优势。
2. Semi-supervised 训练范式：SFT on annotated data + CCV-RLVR on coordinate-only data。
3. 系统性地比较和消融四种 reward 设计（rule-based / CDL matching / CCV / joint constraint）。

贡献对领域的价值：中等偏上。reward 设计改进对于几何解析-推理管线有实际意义，但影响面主要局限在 geometry problem solving 子方向。semi-supervised 训练范式如果被验证有效，可能更具推广价值。

【方法合理性】:
方法本身是合理的。用坐标验证检查几何 predicate 的满足性是数学上正确的。但有以下需要审视的点：

1. **Precision-only reward 的偏差**: CCV reward = 满足约束的 predicate 占比，这本质是一个 precision 指标。RL 优化此 reward 可能导致模型趋向保守——只预测高置信度的 predicates，牺牲 recall。proposal 没有显式讨论这个问题，也没有设计 recall 补偿机制（如 predicate 数量下限惩罚）。
2. **Per-predicate 验证 vs. Joint consistency**: CCV 逐 predicate 检查，可能漏掉某些 predicates 单独满足但联合不一致的情况（虽然坐标验证本身已经隐式处理了大部分此类情况）。Tier B（joint constraint satisfiability via FGPS）被标为"oracle comparison only"，但如果 Tier B 效果显著优于 CCV，则 CCV 的贡献会被削弱。
3. **是否有更简单的替代方案**: CCV reranking baseline（实验设计 #6）已经覆盖了这一点——如果 inference-time reranking 就能获得大部分收益，那 RL 训练的必要性会被质疑。这是一个很好的自我对照设计。
4. **Tolerance 选择的脆弱性**: 数值验证依赖容差参数，proposal 设计了 5 级 tolerance 消融，但容差选择对不同 predicate 类型（角度 vs. 距离 vs. 共线性）可能需要不同尺度，统一容差可能不够。

【5 维度打分】:

1. **研究问题: 中** — 问题真实存在：representation sensitivity 和 annotation dependence 是当前 geometry RL reward 的实际限制，在 CGD-Bridge 和 GeoDPO 的设计中可以明确看到。但问题的影响面较窄（仅限于几何解析 reward 设计），且 Geoparsing 已经 96.4 F1，进一步提升的边际价值需要在 end-to-end solving 上证明。

2. **方法与创新: 中** — 坐标约束验证作为 RL reward 在几何解析领域确实无人做过（调研未发现直接竞争工作）。但技术贡献偏轻——CCV 本质是标准计算几何操作的包装，不涉及新的算法或理论。与 SIRL 的跨领域 precedent 相比，本工作的 unique challenge（visual input, per-predicate granularity, constraint coupling）确实存在但增量有限。创新更多体现在 "insight" 层面（recognizing coordinate verification is the right reward signal）而非 "method" 层面。

3. **实验设计: 强** — 这是 proposal 最大的亮点。6 个 baselines（含直接消融对照 Geoparsing SFT+RLVR 和 inference-time reranking baseline），7 组消融实验覆盖了审稿人可能提出的几乎所有问题（reward type / granularity / tolerance / optimizer / initialization / constraint type / training vs. inference），semi-supervised 实验直接验证 annotation-free claim，pre-experiment error analysis 量化改进上限，统计显著性检验（paired bootstrap, ≥3 seeds）。实验设计的完备度在 proposal 阶段罕见地高。参照 SIRL 和 SGVR 的实验标准，本 proposal 的实验方案达到甚至超过了领域标准。

4. **可行性: 中** — 主要风险在于：(a) formalgeo7k 的坐标确认可用，但 Geometry3K 和 GDP-3K 的坐标可用性"must be confirmed"——如果这两个主流 benchmark 没有坐标，工作将主要局限于 formalgeo7k，说服力大打折扣；(b) 96.4 F1 的 baseline 意味着绝对提升可能很小，如果 end-to-end solving accuracy 提升不显著，论文故事难以成立；(c) Qwen3-VL-4B + GRPO 的训练本身可行，计算需求合理。

5. **写作与呈现: 强** — Proposal 逻辑极为清晰：两个 limitation → 一个统一解决方案 → 完备实验验证。研究定位精准，与相关工作的差异化阐述到位（rule-based vs. CDL matching vs. translator-guided vs. CCV 的四方对比）。broader context 的引用（SIRL, perception-reasoning decomposition 趋势）增强了工作的 significance framing。

【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
优势面：(1) novelty claim 成立——坐标约束验证作为几何解析 RL reward 确实无人做过；(2) 实验设计在 proposal 阶段已经非常完备，大幅降低了"实验不充分"被拒的风险；(3) 故事线清晰，两个 limitation → 一个解决方案的叙事有说服力；(4) semi-supervised 训练范式有实际推广价值。

劣势面：(1) 技术深度有限——核心方法是标准计算几何操作作为 reward，没有新算法/新理论贡献；(2) 研究范围较窄，仅限于几何解析的 reward 信号改进；(3) 96.4 F1 baseline 下的提升空间受限，如果 end-to-end solving 改善不够显著，paper 的 impact 会被质疑；(4) 关键 benchmark 的坐标可用性存在不确定性。

综合来看，这是一篇方向正确、实验充分、但技术贡献偏轻的 proposal。在 AAAI 审稿中，这类 "clean insight + thorough experiments" 的工作如果实验结果扎实，可以被接收，但也容易因为 novelty 不足被 borderline reject。中位概率 33% 反映了这种不确定性。

【主要风险】:
1. **提升幅度不够显著**: 96.4 F1 的 baseline 意味着 parsing 层面的绝对提升可能很小（<1 F1），如果 end-to-end solving accuracy 的改善也有限（<2-3%），审稿人会质疑这个工作的 practical significance。
2. **技术贡献深度不足以支撑顶会**: 核心方法（坐标验证 → reward）的技术复杂度低，审稿人可能认为这更接近一个"好的工程实践"而非"研究贡献"。如果 Tier B (FGPS joint verification) 效果相当或更好且开销可接受，CCV 的独立价值进一步被削弱。

【实施评估】:
  - 计算资源: 中等。Qwen3-VL-4B GRPO 训练需 4-8 张 A100 GPU，约 1-2 天/实验配置。总计含所有消融约 200-400 GPU hours。
  - 数据需求: formalgeo7k（坐标确认可用）、GDP-29K（Geoparsing 已有）、Geometry3K/PGPS9K（坐标待确认）。无需新标注，但可能需要对现有 benchmark 补充坐标提取。
  - 人工介入: 低。CCV verifier 实现为自动化 NumPy 检查。可能需要少量人工验证 tolerance 参数在不同 predicate 类型上的适用性。
  - 训练需求: 需要训练。SFT 初始化 + GRPO RL，多组消融（≥3 seeds × 7 ablation groups = 21+ 训练 run）。
  - 新 Benchmark: 不需要构建新 benchmark，使用现有 formalgeo7k / GDP-3K / Geometry3K / PGPS9K。
  - 预估周期: 6-8 周。Week 1-2: CCV verifier 实现 + pre-experiment error analysis；Week 3-5: 主实验 + 消融；Week 6-7: semi-supervised 实验 + error analysis；Week 8: 论文撰写。前提是 Geometry3K/GDP-3K 坐标可用性能快速确认。
```

Sources:
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry (ACL 2026)](https://arxiv.org/abs/2604.11600)
- [CGD-Bridge: Concise Geometric Description as a Bridge (CVPR 2026)](https://arxiv.org/abs/2601.21164)
- [GeoDPO: Enhancing Geometric Perception via Translator-Guided RL (ICLR 2026)](https://arxiv.org/abs/2602.22703)
- [SIRL: Solver-Informed RL for Optimization Modeling (NeurIPS 2025)](https://arxiv.org/abs/2505.11792)
- [Bad Seeing or Bad Thinking? Rewarding Perception for VL Reasoning](https://arxiv.org/abs/2605.14054)
- [FormalGeo: Extensible Formalized Framework for Geometry](https://arxiv.org/abs/2310.18021)
- [formalgeo7k GitHub repository](https://github.com/BitSecret/formalgeo7k)
- [Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition](https://arxiv.org/html/2508.19652v1)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile the full evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Geoparsing (arXiv:2604.11600)](https://arxiv.org/abs/2604.11600) (ACL 2026): 当前最直接的 baseline。在 Qwen3-VL-4B 上用 SFT + RLVR 达到 96.4 F1 的 CDL 解析，其 verifier 仅检查句法正确性和局部几何一致性（参数类型、元数、结构有效性），不涉及跨谓词的坐标级约束验证。GDP-29K 数据集为本 proposal 的主要训练数据来源。
- [CGD-Bridge (arXiv:2601.21164)](https://arxiv.org/abs/2601.21164) (CVPR 2026): 用 CDL matching reward + GRPO 训练 MLLM Interpreter 生成 CDL。关键发现：CDL matching rewards 比 solution-based rewards 在 GRPO 训练中更有效。但其 reward 基于 GT CDL 表面形式匹配，存在 proposal 指出的 representation sensitivity 问题。
- [GeoDPO (arXiv:2602.22703)](https://arxiv.org/abs/2602.22703) (ICLR 2026): 用 NL-to-DSL translator 计算细粒度 DSL-level score 作为 RL reward，增强 VLM 几何感知能力。+26.5% 域内提升。依赖 translator 训练数据，存在 annotation dependence。
- [SIRL (arXiv:2505.11792)](https://arxiv.org/abs/2505.11792): 将优化求解器作为 verifier 提供 syntax/feasibility/solution-quality 三级 reward，7B 模型超越 DeepSeek-V3 和 o3。这是本 proposal "solver-as-verifier" 范式的直接跨领域先驱，但 SIRL 处理的是文本到优化模型，而非视觉输入到结构化解析。
- [Hilbert-Geo (arXiv:2605.16385)](https://arxiv.org/abs/2605.16385) (CVPR 2026): Parse2Reason 流水线，在 PlaneFGeo3k 达 80.2%。识别 CDL distortion 为主要失败模式但无反馈机制——间接支持本 proposal 的动机。
- [SGVR (arXiv:2601.05073)](https://arxiv.org/abs/2601.05073): 用 sub-goal verifiable reward 为几何推理提供 dense reward，+9.7% 几何性能。但作用于推理阶段而非感知阶段。
- [PRCO (arXiv:2603.28618)](https://arxiv.org/abs/2603.28618): 感知-推理协同进化框架，Observer+Solver 双角色，用 utility reward 反馈给感知模块。验证了感知端独立 reward 信号的价值。
- ["Bad Seeing or Bad Thinking?" (arXiv:2605.14054)](https://arxiv.org/abs/2605.14054): 提出 Perception Verification (PV)，独立奖励感知保真度。与本 proposal 的感知级 reward 设计理念一致，但该工作使用学习型 proxy 而非形式化数学验证。
- [FormalGeo (arXiv:2310.18021)](https://arxiv.org/abs/2310.18021): 88 个几何谓词 + 196 条定理，formalgeo7k 含 6981 题，提供 GeoGebra 标注的点坐标。FGPS 求解器是 proposal 中 Tier B oracle 的基础。
- [AutoGPS (arXiv:2505.23381)](https://arxiv.org/abs/2505.23381): MPF+DSR 框架，Geometry3K 上 81.6%，具有运行时反馈但无 RL 训练信号。

- **调研总结**: 几何图解析领域在 2025-2026 年经历了快速发展，形成了 SFT+RL 训练感知模块的明确趋势。当前所有 RL reward 设计（规则验证、GT 匹配、translator-guided）均不利用坐标级约束满足性，这是一个未被填补的空白。同时，感知-推理 reward 解耦（PRCO、PV、SIRL）是更广泛的研究趋势，本 proposal 可以自然嵌入这一趋势。但需注意：(1) 96.4 F1 的高 baseline 限制了绝对提升空间；(2) 坐标可用性限制了实验规模。

【整体印象】:
作为审稿人，我的第一反应是：这是一个 **clean、well-motivated 的 idea**，问题定义清晰，技术路线自然，实验设计异常完备。Proposal 的学术素养很高——它准确识别了现有 reward 设计的两个真实局限（representation sensitivity 和 annotation dependence），并提出了一个在数学上优雅的解决方案。"用坐标验证谓词满足性作为 reward" 这个 idea 有一种 "为什么之前没人做" 的感觉，这通常是好 idea 的标志。

然而，我会倾向于 **borderline**，原因有三：(1) 核心技术贡献的 novelty 偏窄——本质上是为现有 GRPO pipeline 设计了一个新的 reward function，没有新的算法或架构创新；(2) 改进天花板不确定——在 96.4 F1 baseline 上能有多少提升，以及这些提升能否显著传导到下游 solving accuracy，proposal 自己也只能假设；(3) 坐标可用性问题使得完整实验可能仅限于 formalgeo7k 一个数据集。但极其完善的实验设计（7 组 ablation、pre-experiment error analysis、training vs. inference 对比）是明显的加分项。

【核心贡献】:
1. **Coordinate Constraint Verification (CCV) reward**：一种基于坐标级几何约束满足性的 RL reward 信号，具有 representation-invariance 和 annotation-efficiency 两个理论优势。
2. **CDL-annotation-free training paradigm**：仅需点坐标即可进行 RLVR 训练的半监督范式。
3. **系统性对比研究**：对几何解析领域三类 reward 设计（rule-based、GT-matching、constraint-grounded）的全面实验对比。

贡献 1 是主要贡献，在概念层面有价值——它将 "形式化验证作为 reward" 的 SIRL 范式迁移到视觉几何感知领域，并增加了 per-predicate 粒度和视觉输入的独特挑战。但贡献的深度取决于实验结果能否验证 key hypothesis（CCV 对多谓词不一致性错误的不成比例减少）。

【方法合理性】:
方法在技术上是 **完全合理** 的。用坐标验证几何谓词是数学上严格的——Parallel 检查斜率相等、Collinear 检查三角形面积为零等，这些都是解析几何的基本运算。微秒级的向量化 NumPy 计算使其在 RL 训练中不会成为瓶颈。

**潜在替代方案的考虑**:
- Proposal 已经讨论了 "扩展规则验证器" 的替代方案并合理地 argue 了其不可行性（组合爆炸）。
- Tier B（FGPS 联合约束可满足性）是一个更强但更慢的替代方案，proposal 正确地将其定位为 oracle 比较。
- 一个未被充分讨论的替代方案是：CCV 作为 inference-time reranker 而非 RL reward。Proposal 在 Baseline 6 和 Ablation 7 中设计了这个对比，这是方法论上的加分。

**关键技术风险**：tolerance 参数的设定对 reward 质量至关重要。坐标噪声（来自 GeoGebra 标注或视觉检测的误差）可能导致 false negatives（正确谓词被判为不满足）或 false positives（错误谓词因容差过大被判为满足）。5 级 tolerance ablation 是合理的缓解措施，但 proposal 应更深入讨论坐标精度对 CCV 可靠性的影响。

【5 维度打分】:
  1. 研究问题: 【中偏强】 — Representation sensitivity 和 annotation dependence 是 geometry diagram parsing RL 方法中的真实问题，Hilbert-Geo 识别的 "CDL distortion as primary failure mode" 从侧面支持了这一研究动机。但该问题的影响范围相对较窄（仅限几何图解析的 RL reward 设计），且在 96.4 F1 的高 baseline 下，实际问题的严重程度有待实验验证。

  2. 方法与创新: 【中】 — CCV 的概念自然、技术合理，SIRL（arXiv:2505.11792）已证明 solver-as-verifier 范式在优化领域的有效性，本 proposal 将其迁移到视觉几何感知是合理的领域适配。但核心 novelty 偏窄：(a) 与 SIRL 的差异主要在于领域（视觉输入 + per-predicate 粒度），方法论框架相似；(b) 与 "Bad Seeing or Bad Thinking?" (arXiv:2605.14054) 的 Perception Verification 在理念上有重叠，区别在于本 proposal 使用形式化数学验证而非学习型 proxy；(c) CCV 本身是解析几何基本运算的直接应用，技术深度有限。representation-invariance 是一个优雅的理论性质，但其实际价值取决于 GT 表面形式偏差在训练中造成多大的 reward corruption。

  3. 实验设计: 【强】 — 这是 proposal 最突出的优势。6 个 baselines 覆盖了领域内所有主要方法（Geoparsing、CGD-Bridge、GeoDPO、AutoGPS）以及关键消融基线（SFT-only、CCV reranking）。7 组 ablation 全面覆盖 reward type、granularity、tolerance、optimizer、initialization、constraint type、training vs. inference。Pre-experiment error analysis 和 semi-supervised experiment 展示了很高的方法论素养。统计严谨性（≥3 seeds, paired bootstrap test）和计算公平性（GPU-hour matched comparison）超过领域平均水平。唯一弱点：坐标可用性问题可能使完整 CCV 实验仅限于 formalgeo7k。

  4. 可行性: 【中偏强】 — 技术实现可行性高：CCV 验证是标准数学运算，Qwen3-VL-4B + GRPO 训练管线可复用 Geoparsing 和 CGD-Bridge 的公开代码。计算需求适中（4B 模型 + 微秒级 reward 计算）。主要风险：(a) Geometry3K 和 GDP-3K 的坐标可用性未确认，可能需要额外的点检测工作或缩小实验范围；(b) tolerance 调优可能需要大量预实验；(c) 如果 96.4 F1 baseline 上的多谓词不一致性错误数量很少，key hypothesis 可能无法验证。

  5. 写作与呈现: 【强】 — Proposal 逻辑清晰、层次分明。Research Opportunity 部分精准定位两个 limitations 并解释 CCV 如何同时解决两者。"Why not extend rule-based verifiers?" 的主动回答展示了审稿人视角的意识。Cross-domain precedent 和 Research Landscape 的梳理全面准确。Oracle tiers 的设计和 representation-invariance example 增强了说服力。唯一建议：对 tolerance sensitivity 和坐标精度的讨论可以更深入。

【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
- **上行因素** (推向 38%): (1) 实验设计的完备性在 AAAI 投稿中属于 top-tier，审稿人很难在实验方案上找到明显漏洞；(2) idea 的优雅性——"坐标约束满足性作为 reward" 概念上简洁、数学上严格、动机清晰；(3) 嵌入感知-推理 reward 解耦的更广泛趋势（PRCO、PV、SIRL），positioning 合理；(4) semi-supervised 训练范式有独立的实用价值。
- **下行因素** (推向 28%): (1) 核心 novelty 偏窄——本质是一个新 reward function，没有新算法/架构贡献，SIRL 已证明 solver-as-verifier 范式的有效性，本 proposal 是领域迁移；(2) 改进天花板不确定——96.4 F1 baseline 上多谓词不一致性错误的实际占比未知，如果很少则 key hypothesis 不成立；(3) 实验范围可能受限于单一数据集（formalgeo7k）；(4) 子领域较窄（几何图解析），审稿人池和影响力受限。
- **中位 33%** 的逻辑：这是一篇整体合格、方向正确、实验扎实的投稿，但缺乏突出的 novelty 或广泛的影响力来进入 top 区间。在 AAAI 的竞争中，它属于 "solid but not exciting" 的范畴——不太会被强 reject，但也不容易拿到 strong accept。

【主要风险】:
1. **改进天花板过低**: 在 96.4 F1 的高 baseline 下，CCV 能修正的多谓词不一致性错误可能数量有限，导致实验提升微小（<1% 绝对值），难以说服审稿人这是一个有实质性影响的贡献。Pre-experiment error analysis 可以提前揭示这个风险，但如果分析结果不乐观，整个 proposal 的价值主张会被严重削弱。
2. **Novelty 不足被审稿人质疑**: 审稿人可能认为 "用坐标验证谓词" 是一个 straightforward 的工程贡献而非研究贡献，特别是在 SIRL 已建立 solver-as-verifier 范式的背景下。如果 CCV 的实验提升不够显著，这一质疑将更加致命。

【实施评估】:
  - 计算资源: 中等。Qwen3-VL-4B 的 GRPO 训练需 4-8 张 A100/H100，CCV reward 计算开销可忽略（微秒级 NumPy），但需多个 ablation 实验 × ≥3 seeds。估计总计 200-400 GPU-hours。
  - 数据需求: GDP-29K（Geoparsing 公开）+ formalgeo7k（公开，含坐标）。Geometry3K 和 GDP-3K 的坐标可用性需确认，可能需要额外的视觉点检测管线。
  - 人工介入: 低。CCV 验证全自动，主要人工工作在实验配置和分析。如需为缺少坐标的数据集标注/检测点坐标，人工介入中等。
  - 训练需求: 需要训练。在 Geoparsing SFT checkpoint 基础上进行 GRPO RL 微调，多组实验配置。无需从零预训练。
  - 新 Benchmark: 不需要构建新 benchmark，使用现有的 formalgeo7k、Geometry3K、PGPS9K、GDP-3K。
  - 预估周期: 6-10 周。包括：pre-experiment error analysis (1 周) → 坐标可用性确认与处理 (1-2 周) → 主实验训练 (2-3 周) → ablation 实验 (2-3 周) → 分析与写作 (1-2 周)。
```

Sources:
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language](https://arxiv.org/abs/2604.11600)
- [CGD-Bridge: Concise Geometric Description as a Bridge](https://arxiv.org/abs/2601.21164)
- [GeoDPO: Enhancing Geometric Perception via Translator-Guided RL](https://arxiv.org/abs/2602.22703)
- [SIRL: Solver-Informed RL for Optimization Modeling](https://arxiv.org/abs/2505.11792)
- [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/abs/2605.16385)
- [SGVR: Milestones over Outcome - Sub-Goal Verifiable Reward](https://arxiv.org/abs/2601.05073)
- [PRCO: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)
- [Bad Seeing or Bad Thinking? Rewarding Perception for VL Reasoning](https://arxiv.org/abs/2605.14054)
- [FormalGeo: An Extensible Formalized Framework](https://arxiv.org/abs/2310.18021)
- [AutoGPS: Automated Geometry Problem Solving](https://arxiv.org/abs/2505.23381)
- [Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition](https://arxiv.org/abs/2508.19652)


【原始 proposal（允许参考但不是主要依据）】:
# Constraint-Grounded Reward for Geometry Diagram Parsing

## Core Problem

Can geometric constraint verification — checking whether predicted CDL predicates satisfy the diagram's coordinate-level geometric constraints — serve as a representation-invariant, annotation-efficient RL reward for diagram parsers, surpassing both rule-based format rewards and GT-matching rewards that penalize valid alternative representations?

## Research Opportunity

All components exist but remain unconnected. Geoparsing (ACL 2026) achieves 96.4 F1 CDL parsing via SFT + RLVR with a rule-based verifier checking syntactic correctness and local geometric consistency (argument types, arity, structural validity). CGD-Bridge (CVPR 2026) uses CDL matching rewards (predicted vs. GT CDL) with GRPO. GeoDPO (ICLR 2026) uses translator-guided RL with DSL-level scores. All three reward designs share two fundamental limitations:

**Limitation 1 — Representation sensitivity**: GT-matching rewards (CGD-Bridge) and translator-based rewards (GeoDPO) penalize semantically equivalent but syntactically different CDL representations. Geometry inherently admits multiple valid descriptions of the same configuration (e.g., a triangle can be described via three angle predicates, three side predicates, or mixed). Current rewards treat any deviation from the GT surface form as error, producing false-negative penalties that corrupt the RL signal.

**Limitation 2 — Annotation dependence**: All current CDL-RL methods require full CDL annotations for training. Rule-based rewards need CDL structure definitions; GT-matching needs paired (diagram, CDL) annotations; translator rewards need NL-to-DSL training data. This creates an annotation bottleneck limiting scalability.

Geometric constraint verification resolves both limitations simultaneously. By checking whether predicted predicates are satisfied by the diagram's point coordinates, it provides: (1) **representation-invariant reward** — any CDL set that correctly describes the geometry receives full reward regardless of surface form; (2) **CDL-annotation-free training** — verification requires only point coordinates (obtainable via standard visual point detection), not full CDL annotations, enabling RL training on diagrams with coordinate-only annotation.

**Why not extend rule-based verifiers?** A natural question is whether Geoparsing's rule-based verifier could be extended with pairwise consistency rules (e.g., "Parallel(l1,l2) ∧ PointOnLine(P,l1) ∧ PointOnLine(P,l2) → Collinear"). This approach fails at scale: multi-predicate inconsistencies involve combinatorial interactions that cannot be exhaustively enumerated as rules. Coordinate verification is a "check" not an "enumerate" — it automatically covers all inconsistency types including non-obvious ones, and adapts to new predicate types without manual rule authoring.

Cross-domain precedent: SIRL (arXiv:2505.11792) demonstrates solver-as-verifier RL for optimization modeling (syntax/feasibility/solution-quality rewards), achieving SOTA with 7B model. Our work instantiates this paradigm in geometry with unique challenges: visual input (diagram → structured CDL), per-predicate reward granularity (vs. SIRL's problem-level), and geometric constraint coupling across predicates. The broader trend of perception-reasoning reward decomposition — Vision-SR1 (arXiv:2508.19652) decomposes VLM advantage into perception vs. reasoning stages; "Bad Seeing or Bad Thinking?" (arXiv:2605.14054) proposes Perception Verification to reward perceptual fidelity independently; PRCO (arXiv 2026) feeds downstream reasoning success back to perception via utility rewards — validates the need for principled perception reward signals. Our constraint-grounded approach differs from these learned/proxy approaches: it provides a formal, deterministic, task-agnostic verification signal derived from mathematical structure, requires no verifier training, and gives per-predicate dense reward rather than problem-level binary feedback.

## Research Landscape

**Parsers with RL**: Geoparsing (ACL 2026) — SFT + RLVR with rule-based local consistency verifier, 96.4 F1; GeoDPO (ICLR 2026) — translator-guided RL, +26.5% perception; CGD-Bridge (CVPR 2026) — CDL matching rewards + GRPO, strong results from 5.5k examples. All use perception-level rewards.

**Sequential pipelines**: Hilbert-Geo (CVPR 2026) — 80.2% on PlaneFGeo3k, sequential parse-then-reason, identifies CDL distortion as primary failure mode but has no feedback; AutoGPS (arXiv 2025) — 81.6% on Geometry3K, MPF+DSR collaboration, runtime feedback but no RL training signal.

**Text-only symbolic solvers**: InternGeometry — 44/50 IMO via DDAR; AlphaGeometry2 — 42/50 via DDAR2 (C++, 300× speedup), both text-only.

**Perception-reasoning reward decomposition**: SIRL (arXiv:2505.11792) — solver verification as RL reward for optimization; PRCO (arXiv 2026) — perception-reasoning coevolution via utility rewards; Vision-SR1 (arXiv:2508.19652) — advantage decomposition into perception/reasoning stages; "Bad Seeing or Bad Thinking?" (arXiv:2605.14054) — Perception Verification for VLM reward; SGVR (arXiv 2026) — dense sub-goal rewards for geometric reasoning +37.5%; SVE-Math (arXiv 2025) — visual encoding quality impacts downstream reasoning. GeoPQA (arXiv:2509.17437) trains perception and reasoning separately without solver verification.

**Key gap**: No existing work uses coordinate-level geometric constraint satisfaction as a representation-invariant, annotation-efficient reward for training diagram parsers.

## Proposed Approach

Fine-tune Qwen3-VL-4B (Geoparsing's base) via GRPO with geometric constraint verification as the reward signal.

**Primary reward — Coordinate Constraint Verification (CCV)**: For each predicted CDL predicate, instantiate using the diagram's point coordinates and verify numerical satisfaction. Examples: Parallel(l1,l2) → check slope equality within tolerance; Collinear(A,B,C) → check triangle area ≈ 0; Tangent(circle,line) → check distance from center to line ≈ radius. Reward per sample = fraction of constraint-satisfied predicates. This operates at microsecond scale via vectorized NumPy checks.

**Representation-invariance example**: Consider a triangle ABC. GT CDL uses {Triangle(A,B,C), Angle(A,60°), Angle(B,70°)}. An alternative valid description is {Segment(AB), Segment(BC), Segment(CA), Angle(A,60°), Angle(B,70°), Angle(C,50°)}. CDL matching reward: the alternative gets partial match penalty. CCV reward: both get full reward because both satisfy the coordinate constraints.

**Oracle tiers for ablation**:
- Tier B — Joint constraint satisfiability: submit all predicted predicates to FormalGeo's FGPS as complete constraint system; reward = satisfiable/not. Most semantically powerful but ~0.1–1s per call. Oracle comparison only.
- Tier C — Solver-guided semantic matching: check predicate entailment against GT constraint system via FormalGeo's theorem library. Intermediate cost.

**Coordinate availability**: formalgeo7k provides GeoGebra-annotated point coordinates directly. For Geometry3K and GDP-3K, coordinate availability must be confirmed; if unavailable, these benchmarks use only rule-based/GT-matching reward variants and serve as cross-system evaluation.

**CDL-annotation-free training**: CCV requires only point coordinates, not CDL annotations. This enables a semi-supervised training paradigm: SFT on fully-annotated data, then CCV-RLVR on coordinate-only data without CDL labels, expanding effective training set beyond annotated corpora.

## Experimental Design

**Baselines** (6 comparisons):
1. Geoparsing SFT-only (no RL, lower bound)
2. Geoparsing SFT + rule-based RLVR (direct ablation — same base, same data, different reward)
3. CGD-Bridge (CDL matching rewards + GRPO)
4. GeoDPO (translator-guided RL reward)
5. AutoGPS (MPF+DSR, current end-to-end SOTA on Geometry3K at 81.6%)
6. Geoparsing SFT+RLVR + CCV reranking (inference-time baseline — generate k candidates, select by CCV score; isolates whether CCV's value comes from signal quality or from RL training)

**Benchmarks** (tiered by coordinate availability):
- **Primary (coordinates confirmed)**: Formalgeo7k — full CCV reward + all ablations; enables direct comparison with CGD-Bridge
- **Standard solving benchmarks**: Geometry3K, PGPS9K — end-to-end solving accuracy; CCV reward if coordinates available, otherwise rule-based/GT-matching variants
- **Parsing quality**: GDP-3K (PGDP-2K + SGDP-1K) — direct comparison with Geoparsing

**Primary evaluation metric**: End-to-end solving accuracy (not parsing F1). Rationale: at 96.4 F1 baseline, parsing improvements may be small in absolute terms but disproportionately impact solving because multi-predicate inconsistencies invalidate entire proof chains.

**Pre-experiment error analysis** (before RL training): Run CCV on Geoparsing baseline outputs to (a) classify errors into single-predicate errors vs. multi-predicate inconsistency errors, (b) quantify each error type's contribution to end-to-end solving failures, (c) estimate CCV reward's achievable improvement ceiling.

**Ablation studies** (7 groups):
1. Reward type: rule-based vs. CDL matching vs. CCV vs. joint constraint (Tier B) — isolates constraint verification's incremental contribution
2. Reward granularity: per-predicate dense vs. diagram-level binary
3. CCV tolerance sensitivity: 5 tolerance levels (1e-6 to 1e-1) — measures precision/recall tradeoff of reward signal
4. RL optimizer: GRPO vs. PPO (following SGVR's design)
5. SFT initialization: random init vs. Geoparsing SFT init
6. Constraint type decomposition: angle-only vs. distance-only vs. full CCV (backup for Newclid ablation if format bridging infeasible)
7. Training vs. inference: CCV as RL reward vs. CCV as inference-time reranker (isolates RL training's necessity)

**Semi-supervised experiment**: Split training data into annotated portion (CDL + coordinates, used for SFT) and coordinate-only portion (CDL labels withheld, used for CCV-RLVR only). Compare: (a) SFT on annotated only, (b) SFT + rule-based RLVR on annotated only, (c) SFT on annotated + CCV-RLVR on coordinate-only — quantifies CDL-annotation-free training's value.

**Training data configuration**: Primary comparison uses Geoparsing's GDP-29K for controlled comparison (same data, different reward). Cross-system evaluation on formalgeo7k uses CGD-Bridge's train/test split. Semi-supervised experiment uses GDP-29K split with held-out CDL labels.

**Statistical rigor**: All experiments run with ≥3 random seeds, reporting mean ± std. Key comparisons (CCV vs. rule-based RLVR) use paired bootstrap test with p-values. Per-instance analysis for fine-grained error category improvements.

**Error analysis**: Taxonomy of single-predicate errors vs. multi-predicate inconsistencies; per-category reduction rates; case studies showing inconsistencies caught by CCV but missed by rule-based/GT-matching rewards; "cascading fix" analysis quantifying how resolving one inconsistency impacts downstream solving.

**Compute fairness**: Report wall-clock time and GPU hours for all methods. Compute-matched comparison under same GPU-hour budget. Performance vs. training compute curves.

## Key Hypothesis

CCV rewards disproportionately reduce multi-predicate inconsistency errors — cases where individual predicates are locally valid but jointly violate geometric constraints. While potentially a minority of total parsing errors, these inconsistencies cause disproportionate end-to-end solving failures because a single geometric contradiction invalidates entire proof chains. The representation-invariant property additionally eliminates false-negative reward penalties that corrupt RL training under GT-matching rewards.

## Key References

- Geoparsing: Diagram Parsing with Unified Formal Language (ACL 2026)
- Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning (CVPR 2026)
- Milestones over Outcome: Sub-Goal Verifiable Reward [SGVR] (arXiv 2026)
- AlphaGeometry2: Gold-medalist Olympiad Geometry (arXiv 2025)
- InternGeometry: Olympia-Level Geometry LLM Agent (arXiv 2025)
- AutoGPS: Automated Geometry Problem Solving (arXiv 2025)
- Enhancing Geometric Perception via Translator-Guided RL [GeoDPO] (ICLR 2026)
- Concise Geometric Description as a Bridge [CGD-Bridge] (CVPR 2026)
- Open Eyes Then Reason: SVE-Math (arXiv 2025)
- PRCO: Perception-Reasoning Coevolution (arXiv 2026)
- Solver-Informed RL [SIRL] (arXiv:2505.11792)
- FormalGeo: Extensible Formalized Framework (arXiv:2310.18021)
- Newclid: A User-Friendly Replacement for AlphaGeometry (arXiv:2411.11938)
- GeoPQA: Two-Stage RL for Geometry (arXiv:2509.17437)
- Bad Seeing or Bad Thinking? Rewarding Perception for VL Reasoning (arXiv:2605.14054)
- Vision-SR1: Self-Rewarding VLM via Reasoning Decomposition (arXiv:2508.19652)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "546ec0ae-74cd-4871-85ee-e948f1ea0c69",
  "type": "user",
  "uuid": "8e5367c9-453c-44d9-b42d-39b456d8b2a3",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:41:20.505Z_

```json
{
  "parentUuid": "8e5367c9-453c-44d9-b42d-39b456d8b2a3",
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
  "uuid": "d96f7d77-5150-485c-9cf6-e4e0b765f8e7",
  "timestamp": "2026-05-29T06:41:20.505Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:41:20.505Z_

```json
{
  "parentUuid": "d96f7d77-5150-485c-9cf6-e4e0b765f8e7",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "c4a1c827-2504-40d3-950a-b8eaefa99e59",
  "timestamp": "2026-05-29T06:41:20.505Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-29T06:41:20.505Z_

```json
{
  "parentUuid": "c4a1c827-2504-40d3-950a-b8eaefa99e59",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3604a17f-df61-459e-b31d-011dd21563c1",
  "timestamp": "2026-05-29T06:41:20.505Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient background to provide a thorough evaluat…",
  "leafUuid": "3604a17f-df61-459e-b31d-011dd21563c1",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Coordinate-based reward signals for geometry diagram parsing",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4"
}
```

---

### Assistant

_source line 9 · 2026-05-29T06:41:44.303Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully to produce a Meta Judge synthesis.

**Reviewer 1**: [28% - 40%] 中位 33%
**Reviewer 2**: [28% - 38%] 中位 33%
**Reviewer 3**: [28% - 38%] 中位 33%

Three midpoints: 33%, 33%, 33%. std = 0%.

This is extremely high consensus. Let me map out the rubric dimensions across all three.

**Research Question / Problem:**


- R1: 强
- R2: 中
- R3: 中偏强

**Method & Innovation:**
- R1: 中
- R2: 中
- R3: 中

**Experimental Design:**
- R1: 强
- R2: 强
- R3: 强

**Feasibility:**
- R1: 强
- R2: 中
- R3: 中偏强

**Writing:**
- R1: 强
- R2: 强
- R3: 强

Now I'm looking at where the reviewers align and where they diverge. The experimental design and writing quality show strong agreement across all three, while the research question formulation and feasibility assessment show more variation, with Reviewer 1 consistently rating higher than the others.

All three reviewers converge on the core concerns: insufficient novelty depth, the ceiling imposed by the 96.4 F1 baseline, and how the SIRL precedent diminishes the contribution's originality. They also unanimously praise the CCV reranking baseline approach and flag the same data availability risk around the Geometry3K and GDP-3K coordinates. Interestingly, they arrive at the identical 33% midpoint estimate.

The main divergence appears in how Reviewer 1 assesses the research question and feasibility as stronger compared to the other two, though Reviewer 2 raises a unique concern about precision-only reward mechanisms that the others don't emphasize.

Given the extremely tight consensus—zero variance on midpoints and nearly overlapping ranges across all three—I should anchor the final estimate very close to 33%, possibly even narrowing the interval slightly since the convergence is so strong. Now let me check whether the implementation assessment shows similar alignment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3604a17f-df61-459e-b31d-011dd21563c1",
  "isSidechain": false,
  "requestId": "req_011CbWQNkk9VmvJtezp1gZQo",
  "type": "assistant",
  "uuid": "789fecfa-ce7b-4d68-b2ff-157592841e8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HU32vampdcPqqZuakvuyi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20240,
      "cache_read_input_tokens": 16149,
      "output_tokens": 3128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3128,
          "cache_read_input_tokens": 16149,
          "cache_creation_input_tokens": 20240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20240
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

_source line 10 · 2026-05-29T06:42:35.262Z_

【阶段】: Meta Judge
【三次中位】: [33%, 33%, 33%]  std=0%
【共识维度】:
- **方法与创新 = 中**（3/3 一致）：所有审稿人均指出核心方法（逐谓词坐标验证作为 reward）技术深度有限，本质是解析几何基本运算的直接应用，不涉及新算法或理论贡献。与 SIRL 的关系被一致认定为"领域迁移"而非方法创新。
- **实验设计 = 强**（3/3 一致）：所有审稿人均将实验设计评为 proposal 最大亮点——6 baselines、7 ablation groups、pre-experiment error analysis、semi-supervised experiment、CCV reranking baseline（回答"是否需要 RL"）、统计严谨性均被高度肯定。
- **写作与呈现 = 强**（3/3 一致）：叙事逻辑、related work 定位、主动回应审稿人可能质疑（"Why not extend rule-based verifiers?"）均获一致好评。
- **主要风险 1 — Novelty 深度不足**（3/3 一致）：均指出"用坐标检查谓词满足"可能被视为 engineering contribution 而非 research contribution，SIRL 已建立 solver-as-verifier 范式使本工作的方法论独创性进一步削弱。
- **主要风险 2 — 改进天花板受限**（3/3 一致）：96.4 F1 baseline 下绝对提升可能极小，如果 end-to-end solving accuracy 提升不显著则论文说服力大打折扣。
- **坐标可用性不确定性**（3/3 一致）：Geometry3K/GDP-3K 坐标可用性未确认，可能使完整 CCV 实验仅限 formalgeo7k，削弱说服力。
- **Semi-supervised 训练范式有独立价值**（3/3 一致）：annotation-free 训练路径被一致认为是有意义的贡献点。

【异常维度】:
- **R2 独有 — Precision-only reward 偏差**：R2 指出 CCV reward 本质是 precision 指标，可能导致模型趋向保守（牺牲 recall），且 proposal 未设计 recall 补偿机制。R1/R3 未提及此风险。**判断：有效关切，但属于实验可验证的次级风险，不影响核心概率判断。**
- **R1 独有 — 级联误差风险**：R1 更详细讨论了非 FormalGeo 数据集中"视觉点检测噪声 → CCV reward 失真"的级联问题。R2/R3 也提及坐标精度但未展开至此深度。**判断：与坐标可用性共识风险同源，属于细化分析而非独立风险。**
- **R1 研究问题评"强"**：R2 评"中"，R3 评"中偏强"。R1 给更高评价的理由是多项同期工作（PRCO、PV、Vision-SR1）验证了"感知阶段需要独立 reward"这一大趋势。**判断：R1 偏乐观，R2/R3 更审慎地指出问题影响面较窄。取中偏保守 → 研究问题 = 中偏强。**

【最终概率】: [28% - 38%] 中位 33%
【一致性】: 高（std=0%，三份评审在中位数、区间范围、rubric 判决、主要风险识别上高度一致）
【综合理由】:
这是我所见过的 triage 阶段最高一致性评审之一。三位审稿人独立得出完全相同的中位估计（33%），区间几乎重合（[28%-40%] vs [28%-38%] vs [28%-38%]），rubric 核心维度判决一致（方法=中、实验=强、写作=强），且主要风险识别完全重叠（novelty 深度不足 + 改进天花板受限）。

在如此高一致性下，取中位附近并略微收紧区间是合理的。最终区间 [28%-38%] 中位 33% 反映了：
- **下界 28%**：核心 novelty 被判定为 engineering contribution、改进幅度微小、实验仅限单一数据集的最差情景
- **上界 38%**：实验结果扎实（end-to-end solving 有显著提升）、semi-supervised 路径验证有效、审稿人认可 insight 价值的最优情景
- **中位 33%**：方向正确、实验充分、idea 简洁优雅，但技术深度不足以在顶会竞争中脱颖而出的基准情景

三个异常维度均不构成推翻共识的理由：R2 的 precision-only 偏差是可验证的次级风险；R1 的级联误差是共识风险的细化；R1 对研究问题偏高的评分被 R2/R3 的更保守判断平衡。

**概率天花板分析**：由于方法与创新维度被 3/3 一致评为"中"，idea 层面的天花板约在 35-40%。实验设计的强势可以帮助触及天花板但无法突破——再完美的实验也无法弥补核心 novelty 的不足。33% 中位反映了 idea 天花板约 38% × 实验地板已补好但改进幅度不确定的综合判断。

【建议】: 边缘（中位 33% 略低于 36% 阈值，但上界 38% 表明存在通过优化触及 borderline accept 的可能性。建议进入迭代优化，重点强化 idea 层面的 novelty depth 和 significance framing。）

【实施评估】:
  - 计算资源: 中等。Qwen3-VL-4B GRPO 训练需 4-8 张 A100/H100，CCV reward 计算开销可忽略（微秒级 NumPy）。多组 ablation × ≥3 seeds，总计约 200-400 GPU-hours。Tier B（FGPS 联合验证）较慢（~0.1-1s/call）但仅作 oracle 对比。
  - 数据需求: GDP-29K（公开）+ formalgeo7k（公开，含坐标）为核心数据。Geometry3K/GDP-3K 坐标可用性待确认，可能需额外点检测管线或缩小实验范围。所有主要数据集均已公开。
  - 人工介入: 低。CCV 验证逻辑（~88 谓词的坐标检查）为自动化 NumPy 实现，主要人工工作在于 FormalGeo 谓词格式桥接和实验分析。如需为缺坐标数据集补充点检测，人工介入升至中等。
  - 训练需求: 需要训练。基于 Geoparsing SFT checkpoint 进行 GRPO RL 微调，无需从零预训练。多组实验配置（6 baselines + 7 ablation groups × ≥3 seeds ≈ 21+ 训练 run）。
  - 新 Benchmark: 不需要。使用现有 formalgeo7k / Geometry3K / PGPS9K / GDP-3K。
  - 预估周期: 8-10 周（取三位审稿人估计的中位偏保守值）。包括：CCV 实现与坐标确认（1-2 周）→ Pre-experiment error analysis（1 周）→ 主实验 + baselines（3-4 周）→ Ablation + semi-supervised 实验（2-3 周）→ 论文撰写（2 周）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "789fecfa-ce7b-4d68-b2ff-157592841e8b",
  "isSidechain": false,
  "requestId": "req_011CbWQNkk9VmvJtezp1gZQo",
  "type": "assistant",
  "uuid": "d3d57568-d4a6-4c16-aaf6-6ba310b39051",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HU32vampdcPqqZuakvuyi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20240,
      "cache_read_input_tokens": 16149,
      "output_tokens": 3128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3128,
          "cache_read_input_tokens": 16149,
          "cache_creation_input_tokens": 20240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20240
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient background to provide a thorough evaluat…",
  "leafUuid": "d3d57568-d4a6-4c16-aaf6-6ba310b39051",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Coordinate-based reward signals for geometry diagram parsing",
  "sessionId": "3377e962-fe73-4efd-98f1-cf877a08dee4"
}
```

---
