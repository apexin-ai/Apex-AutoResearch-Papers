# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/492b9128-915f-49d8-849b-1d9e07c76669.jsonl`
- **Structured JSON:** [`909c585bfd7fea2ec694.json`](../../sessions/90/909c585bfd7fea2ec694.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:36:02.669Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:36:02.669Z",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have comprehensive research coverage. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01272) (ICLR 2025): 奠定了 patch-level late-interaction VDR 范式。本 proposal 在此基础上提出 region-level 扩展，构成方法论的直接上游。\n- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992) (arXiv Feb 2026): 当前 ViDoRe V3 SOTA，8B 模型 63.42 NDCG@10。本 proposal 选择同系 Qwen3-VL-4B backbone 并对齐训练 recipe，baseline 设定合理。\n- [RegionRAG](https://arxiv.org/abs/2510.27261) (AAAI 2026): 最直接竞争者之一——region-level RAG，但使用外部检测器生成固定 proposals，无法随 retrieval objective 调整。proposal 的\"可微 region proposal\"正好针对此限制。\n- [ColParse / Beyond the Grid](https://arxiv.org/abs/2603.01666) (arXiv Mar 2026): 外部 parser pipeline，storage 降 95%，但 regions task-agnostic 且继承 parser errors。另一条需对比的 pipeline 路线。\n- [AGREE](https://arxiv.org/abs/2511.13415) (SIGIR 2026): 用 frozen MLLM attention 做 proxy grounding，+12.82% nDCG@1，但 spatial signal 非可微、仅优化 page-level metric。\n- [ReAlign](https://arxiv.org/abs/2604.07419) (SIGIR 2026): VLM distillation 做 fine-grained alignment，无 bbox 输出，offline region identification。与本 proposal 的 end-to-end 可微方案形成鲜明对比。\n- [Groma](https://arxiv.org/abs/2404.13013) (ECCV 2024): 用 class-agnostic region proposals 做 localized visual tokenization for MLLMs。proposal 借鉴其 neighbor-patch 策略构造多分辨率特征。\n- [GAR / Grasp Any Region](https://arxiv.org/abs/2510.18876) (ICLR 2026): RoI-Align over ViT features for region-level understanding，1B 超越 78B。证明 RoI-Align + ViT 的可行性，但应用于 understanding 而非 retrieval。\n- [SEAL](https://arxiv.org/abs/2508.20778) (EMNLP 2025): Element-level contrastive alignment for text document retrieval，+3.88 NDCG@10。proposal 的 element-level loss 直接受此启发，但移植到 visual domain。\n- [Multi-Granularity Framework](https://arxiv.org/abs/2505.01457) (arXiv May 2025): ColQwen2+GME+VLM+RRF 多模型融合，MMDocIR layout-level 65.56。pipeline 方案，无 grounding。\n- [Snappy](https://arxiv.org/abs/2512.02660) (arXiv Dec 2025): Training-free 方案，patch similarity → OCR regions，59.7% IoU@0.5。grounding baseline。\n- [BBox-DocVQA](https://arxiv.org/abs/2511.15090) (arXiv Nov 2025): 3.6K documents, 32K QA pairs with bbox grounding。proposal 使用其 training split 作为 IoU grounding loss 的监督源。\n- [MMDocIR](https://arxiv.org/abs/2501.08828) (arXiv Jan 2025): 1,685 expert + 173K bootstrapped pairs，page-level + layout-level dual task。proposal 的 element-level loss 直接使用其 layout annotations。\n\n- **调研总结**: Sub-page VDR 是 2025-2026 年的活跃前沿，已出现 5+ 并行工作（ColParse、RegionRAG、AGREE、ReAlign、Multi-Granularity Framework），但全部依赖 task-agnostic 的区域定义（parser/detector/VLM）。将可微 region proposals 嵌入 retrieval 梯度流是一个尚未被占领的方法空间。同时，Groma、GAR 已在 VLM understanding 侧证明了 RoI-Align + ViT 的可行性，SEAL 已在 text retrieval 侧证明了 element-level alignment 的有效性，但两者均未被迁移到 visual document retrieval。本 proposal 处于这两个成熟技术流的交汇点，方向正确且时机恰当。\n\n【整体印象】:\n作为审稿人，我的第一反应是 **lean accept (weak accept)**。这是一篇方向清晰、定位精准、实验设计异常完备的 proposal。核心 idea——将 differentiable region proposals 嵌入 retrieval 梯度流——填补了一个清晰且被多篇并行工作间接验证的研究空白。proposal 对文献的掌握程度接近 survey 级别，每一个竞争方法的结构性限制都被准确指出。特别值得赞赏的是其科学诚实性：proposal 明确讨论了\"如果 divergence 很小怎么办\"的 fallback 论点，以及 pipeline oracle baseline 的设计。\n\n主要犹豫点在于：(1) 核心假设（learned proposals 会系统性偏离 layout categories）是否能在实验中得到强有力验证尚不确定；(2) 三路 loss + 多数据源的训练复杂度可能导致工程困难；(3) 部分审稿人可能认为这是\"在 retrieval 模型上接一个 detection head\"的 incremental 工作。但整体来看，novelty claim 经得起检验，实验方案的完备性是显著加分项。\n\n【核心贡献】:\n1. **结构性创新**：首个将 region proposal 生成置于 retrieval loss 梯度流内的 VDR 模型，实现了从 task-agnostic regions 到 retrieval-optimal regions 的范式转变。这不是工程集成，而是一个有明确假设可验证的结构性区分（retrieval gradients → proposal positions/sizes）。\n2. **Multi-granularity unification**：单个 forward pass 内生成 page/region/element 三级 retrieval embeddings + spatial grounding，消除 pipeline 依赖。\n3. **Cross-community bridge**：将 detection 社区的 Deformable DETR + RoI-Align 和 retrieval 社区的 late interaction + contrastive alignment 在 VDR 中首次融合。\n\n这些贡献对领域的价值：如果核心假设成立（learned regions ≠ layout categories），这将重新定义 sub-page VDR 的研究方向——从\"如何更好地利用预定义区域\"转向\"如何学习 retrieval-specific 区域\"。即使假设不完全成立，zero-marginal-cost grounding + pipeline error elimination 也有实用价值。\n\n【方法合理性】:\n方法整体合理，技术选择有据可循：\n- **Deformable DETR decoder**: class-agnostic region proposal 的标准选择，已在 Groma (ECCV 2024) 和 GAR (ICLR 2026) 中验证。将其接在 Qwen3-VL-4B 的 ViT feature map 上是自然的架构选择。\n- **DeepStack multi-resolution**: 利用不同 depth 的 intermediate outputs + spatial pooling 构造分辨率金字塔，为 multi-scale deformable attention 提供输入。这比简单使用最后一层更合理，类似 Groma 的 neighbor-patch 策略。\n- **RoI-Align → late interaction**: 从 proposals 提取 region embeddings 用于 late interaction scoring，梯度可以通过 RoI-Align 反传到 proposal decoder，这是方法的核心创新点，技术上可行（RoI-Align 本身是可微的）。\n- **三路 loss 设计**: page-level InfoNCE + element-level contrastive + IoU grounding 的组合覆盖了 retrieval + grounding 两个目标，GradNorm/uncertainty weighting 是处理多任务 loss 的标准做法。\n\n**更简单的替代方案？** 是的——最直接的替代是 pipeline 方案：DocLayout-YOLO → ColQwen2.5（proposal 已将其作为 \"pipeline oracle\" baseline）。如果 pipeline oracle 已经很强，end-to-end 的边际收益可能有限。但 proposal 的论点是：(1) pipeline regions 无法随 retrieval 目标调整；(2) pipeline 无法提供 grounding。这个论点逻辑上成立，但需要实验验证边际收益的实际大小。\n\n**潜在方法问题**：\n1. Region-level late interaction 中，top-K proposals 会引入大量额外 embedding vectors（K=100-300），对 index storage 和 query latency 有显著影响。proposal 的 efficiency analysis 需要认真对待这一点。\n2. 三路 loss 的 balancing 可能非常敏感，GradNorm 不总是有效。proposal 规划了 3-5 ratio configurations，这是合理的但可能不够。\n3. DocLayNet pre-training → joint fine-tuning 的 two-stage 设计引入了额外复杂度。如果 from-scratch 训练效果接近，two-stage 的必要性需要论证。\n\n【5 维度打分】:\n\n1. **研究问题: 强** — Sub-page VDR 是领域当前最活跃的研究前沿（AAAI 2026 的 RegionRAG、SIGIR 2026 的 AGREE 和 ReAlign、arXiv 2026 的 ColParse 和 Multi-Granularity Framework 均在尝试解决此问题），但所有现有方法都依赖 task-agnostic 区域定义。\"retrieval-optimal regions 是否与 layout categories 不同\"是一个有明确科学价值的假设，值得验证。研究问题的时效性和重要性都很强。\n\n2. **方法与创新: 中-强** — 核心创新（differentiable region proposals in retrieval gradient flow）是genuinely novel的——经调研确认，没有任何已发表或公开的工作做过这件事。Groma/GAR 在 understanding 侧用了 RoI-Align，SEAL 在 text retrieval 侧用了 element-level alignment，但将它们结合并应用于 VDR 是新的。但个别审稿人可能认为这是\"已有组件的组合\"（Deformable DETR + ColPali + RoI-Align），评价为 incremental。proposal 需要在核心假设验证（learned regions vs. layout categories 的 divergence analysis）上提供强有力的实验证据来化解这一质疑。\n\n3. **实验设计: 强** — 这是 proposal 最突出的亮点。\n   - **Baselines**: 4 组 baselines 覆盖 page-level（ColPali、Nemotron V2）、layout-level（ColParse、RegionRAG、Multi-Gran）、grounding（Snappy、AGREE）、以及关键的 pipeline oracle（DocLayout-YOLO + ColQwen2.5），这个 pipeline oracle 是直接回答\"为什么不用 pipeline\"的最佳实验设计。\n   - **Ablation**: 8 个 ablation 维度系统地剥离每个组件的贡献，特别是 multi-level feature utilization 的 3 级对比（final layer only → same resolution → multi-resolution）设计精良。\n   - **核心假设验证**: 专门设计了 proposal divergence analysis（IoU overlap 度量、learned vs. fixed proposals 对比、可视化），这是论文最关键的实验，设计合理。\n   - **统计报告**: 主要结果 3 runs + std，ablation 标注单 run，符合社区标准。\n   - 唯一不足：缺少下游 RAG/QA 端到端评估，这在近期 VDR 论文中越来越被期望（但不是致命缺陷）。\n\n4. **可行性: 中** — \n   - **计算**: 4-8× A100-80GB 是严肃的资源需求，但对于学术界的 VDR 研究来说属于可接受范围（Nemotron V2 的训练也需要类似规模）。batch size 1-4 per A100 可能限制 in-batch negatives 的效果，需要 gradient accumulation。\n   - **数据**: 所有数据集（DocLayNet 80K、MMDocIR 173K+1.7K、BBox-DocVQA 32K、page-level retrieval data）均公开可用，但整合 3 个不同来源的 supervision signals 增加了工程复杂度。\n   - **Training complexity**: 三路 loss + two-stage training + LoRA + gradient checkpointing 的组合引入了大量超参数。loss balancing 失败可能导致某一 granularity 的性能退化。proposal 规划了 3-5 ratio configurations，但实际调参可能需要更多。\n   - **Timeline**: 合理估计需要 3-4 个月的全职工作（1 个月搭建 pipeline + DocLayNet pre-training pilot，1.5 个月联合训练调参，1 个月评估与论文撰写），对 AAAI 2026 ddl 来说时间紧但可行。\n\n5. **写作与呈现: 强** — Proposal 的写作质量在我审过的 proposals 中属于上乘：\n   - 文献定位精准，每个竞争方法的结构性限制被逐一分析\n   - \"Why end-to-end beats pipeline\" 段落直接回应了最明显的 trivial alternative 质疑\n   - 科学诚实性好——明确讨论了假设不成立时的 fallback\n   - 术语使用一致，架构描述清晰\n   - 唯一建议：可以增加一个 high-level architecture figure 的描述，使审稿人更快把握整体流程\n\n【概率估计】: [30% - 48%] 中位 38%\n\n【估计理由】:\n推理过程如下：\n\n(1) **方向和 novelty**: 经调研确认，\"将可微 region proposals 嵌入 VDR 梯度流\"是一个genuinely novel的方向，no prior work 做过这件事。方向正确且时机好（sub-page VDR 是 2025-2026 热点）。这把 baseline 提到了 ~30%。\n\n(2) **实验设计加分**: 实验方案的完备性（4 组 baselines、8 ablation dimensions、核心假设验证、pipeline oracle、统计报告）在 proposal 阶段就达到了很高的标准。如果执行到位，实验部分不会成为被拒的理由。这加 ~5-8%。\n\n(3) **风险折扣**:\n   - 核心假设风险：如果 learned proposals 与 layout categories 的 divergence 很小，论文的核心 narrative 会被削弱。proposal 有 fallback 论点（zero-marginal-cost grounding + pipeline error elimination），但审稿人可能认为贡献不够显著。此风险折扣 ~5%。\n   - \"组件组合\" 质疑：部分审稿人可能认为这是 Deformable DETR + ColPali 的 straightforward combination。proposal 需要在 divergence analysis 上有强结果来反驳。此风险折扣 ~3%。\n   - 训练复杂度风险：三路 loss 的 balancing 失败可能导致实际结果不如预期。此风险折扣 ~2%。\n   - 缺少端到端 RAG 评估：虽不致命，但可能被 1-2 位审稿人提及。此风险折扣 ~1%。\n\n(4) **综合**: 30% (方向+novelty baseline) + 8% (实验设计) - 5% (假设风险) - 3% (incremental质疑) - 2% (训练复杂度) = ~28% lower bound → 因写作质量和positioning的加分调整至 30%。Upper bound 48% 对应\"核心假设得到验证 + 所有实验按计划完成 + 论文写作清晰\"的乐观情景。中位 38% 反映了\"方向正确、实验完备、但核心贡献的 impact 取决于实验结果\"的不确定性。\n\n注：38% 对应\"整体扎实、有明确 novelty、实验方案强，但存在合理风险\"的投稿，在AAAI的接收率背景下属于 competitive but not guaranteed 的区间。\n\n【主要风险】:\n1. **核心假设验证风险**: 如果 learned proposals 最终与 DocLayNet layout categories 高度重合（divergence analysis 显示 IoU overlap > 0.7），论文的核心 narrative——\"retrieval-optimal regions ≠ layout regions\"——将难以支撑，贡献退化为\"端到端训练的 marginal improvement + 附带 grounding\"，部分审稿人会认为 contribution 不足以 accept。\n2. **\"组件组合 vs. 本质创新\" 质疑**: 1-2 位审稿人可能认为这是将 detection 社区的 Deformable DETR/RoI-Align 和 retrieval 社区的 late interaction 做 straightforward engineering integration，novelty 评分为 borderline。如果核心假设的实验证据不够强，这一质疑会被放大。\n\n【实施评估】:\n  - 计算资源: 4-8× A100-80GB（或等价），~2-4 周 GPU 时间用于联合训练和 ablation studies。DocLayNet pre-training 约需 1-2 天。全部 ablation（8 configurations × multiple seeds）可能需要 ~100-200 GPU-days。\n  - 数据需求: DocLayNet (80K pages, 公开), MMDocIR (173K+1.7K pairs, 公开), BBox-DocVQA (32K QA pairs, 公开), page-level retrieval training data (需对齐 Nemotron V2 recipe, 部分可能需要自行构造)。所有数据公开可用，但数据处理 pipeline 较复杂。\n  - 人工介入: 中等。需要手动对齐不同数据源的格式，设计 loss balancing 实验，进行 proposal divergence 的定性可视化分析。无需人工标注。\n  - 训练需求: 是，需要训练。Two-stage: (1) Deformable DETR decoder on DocLayNet; (2) Joint fine-tuning with 3 losses on Qwen3-VL-4B (LoRA + gradient checkpointing)。预计每次完整训练 2-5 天 (4× A100)。\n  - 新 Benchmark: 否。使用现有 benchmarks (ViDoRe V3, MMDocIR, BBox-DocVQA)。\n  - 预估周期: 3-4 个月全职工作。Month 1: pipeline 搭建 + DocLayNet pre-training + 内存 profiling。Month 2-2.5: 联合训练调参 + ablation studies。Month 2.5-3.5: evaluation + divergence analysis + 论文撰写。Month 3.5-4: revision + 补充实验。\n```\n\nSources:\n- [RegionRAG: Region-level Retrieval-Augmented Generation](https://arxiv.org/abs/2510.27261)\n- [Beyond the Grid / ColParse](https://arxiv.org/abs/2603.01666)\n- [Snappy: Spatially-Grounded Document Retrieval](https://arxiv.org/abs/2512.02660)\n- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992)\n- [AGREE: Attention Grounded Enhancement for VDR](https://arxiv.org/abs/2511.13415)\n- [ReAlign: Reasoning-Guided Fine-Grained Alignment](https://arxiv.org/abs/2604.07419)\n- [Groma: Localized Visual Tokenization](https://arxiv.org/abs/2404.13013)\n- [GAR: Grasp Any Region](https://arxiv.org/abs/2510.18876)\n- [SEAL: Structure and Element Aware Learning](https://arxiv.org/abs/2508.20778)\n- [Multi-Granularity Retrieval Framework](https://arxiv.org/abs/2505.01457)\n- [MMDocIR Benchmark](https://arxiv.org/abs/2501.08828)\n- [BBox-DocVQA](https://arxiv.org/abs/2511.15090)\n- [Reproducibility and Insights into VDR](https://arxiv.org/abs/2505.07730)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have comprehensive research to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Nemotron ColEmbed V2] (arXiv 2602.03992, Feb 2026): 当前 ViDoRe V3 SOTA，8B 模型达 63.42 NDCG@10。同 backbone (Qwen3-VL) 为 DiffRegion-VDR 提供直接可比基线。\n- [ColPali] (ICLR 2025): 确立了 late-interaction 视觉文档检索范式，每页 ~1030 patch embeddings，是整个领域的基础。\n- [ColParse / Beyond the Grid] (arXiv 2603.01666, Mar 2026): 利用外部文档解析器生成 layout-informed sub-image embeddings，存储量减少 95%+，但 region 完全依赖解析器、不可学习。\n- [RegionRAG] (AAAI 2026): 将检索从 document-level 转向 region-level，但使用固定外部检测器生成 proposals，proposals 无法适配检索目标。\n- [Multi-Granularity Framework] (arXiv 2505.01457): 训练无关的多模型融合 (ColQwen2 + GME + VLM + RRF)，MMDocIR layout-level 达 65.56，但依赖多个独立模型、无 grounding 能力。\n- [AGREE] (SIGIR 2026): 利用冻结 MLLM 注意力作为 proxy 局部监督，nDCG@1 提升 12.82%，但仅优化 page-level 指标，注意力信号不对检索 loss 可微。\n- [ReAlign] (SIGIR 2026, arXiv:2604.07419): VLM 蒸馏实现 fine-grained alignment，但 region 识别离线进行、无 bbox grounding 输出、质量受限于 teacher VLM。\n- [Snappy] (arXiv 2512.02660): 训练无关的 patch-to-region relevance propagation，BBox-DocVQA 上 59.7% IoU@0.5，建立了 grounding 基线。\n- [BBox-DocVQA] (arXiv 2511.15090): 大规模 bbox-grounded DocVQA 数据集，Qwen2.5VL-72B 仅达 35.20% mean IoU，表明当前 VLM grounding 能力不足。\n- [Groma] (ECCV 2024): 在 VLM understanding 中使用 class-agnostic Deformable DETR proposals + RoI-Align 进行 localized visual tokenization，是本 proposal 架构灵感来源。\n- [GAR / Grasp Any Region] (ICLR 2026): 1B 模型通过 RoI-aligned feature replay 超越 78B 模型，证明 RoI-Align over ViT features 的有效性。\n- [SEAL] (EMNLP 2025): structure-aware masked element alignment 在文本文档检索中 NDCG@10 +3.88，element-level 对齐的灵感来源。\n- [MMDocIR] (arXiv 2501.08828): 定义了 page-level 和 layout-level 两级检索任务，173K bootstrapped + 1,685 expert-annotated pairs。\n\n- 调研总结: Visual document retrieval 正从 page-level 向 sub-page/layout-level 演进，但现有方法均使用 task-agnostic 的 region 定义（外部解析器、固定检测器、VLM 离线推理）。将可微 region proposals 置于检索梯度流内是一个尚未被探索的结构性空白。该 proposal 精准定位了这一空白，且相关技术组件（Deformable DETR + RoI-Align on ViT）已在 VLM understanding 中被验证（Groma, GAR），但从未应用于检索。\n\n【整体印象】: \n作为审稿人，我的第一反应是 **lean accept**。这篇 proposal 展现了对领域格局极为深入的理解，核心 insight 清晰且有结构性新颖度——不是在已有范式上微调，而是提出了一种全新的结构设计，将 region proposal generation 纳入检索梯度流。proposal 对与 5+ 并发工作的差异化分析令人信服，每个对比都精确到梯度是否可微这一结构性判据。实验设计非常完备，包含 pipeline oracle baseline、核心假设验证实验和充分的 ablation。主要顾虑在于：(1) 架构复杂度高，三路 loss 训练稳定性存疑；(2) 核心假设（retrieval-optimal regions 显著偏离 layout 类别）可能只有温和的验证结果。\n\n【核心贡献】: \n首个将可微 region proposal generation（Deformable DETR decoder + RoI-Align）置于 VDR 检索梯度流内部的端到端模型。这意味着检索目标不仅决定如何匹配 region 与 query，还决定应该 propose 哪些 region。这是相对于所有现有方法（AGREE 的冻结注意力、ReAlign 的离线 VLM、ColParse 的外部解析器、RegionRAG 的固定检测器）的结构性区分，而非增量改进。附带贡献包括：单模型内统一 page/region/element 三粒度检索 + 零额外成本的空间 grounding。\n\n对领域的价值：**较高**。如果实验证实端到端学习确实优于 pipeline 方法，这将为 sub-page VDR 确立新范式。即使改进幅度温和，将检测社区的成熟技术（Deformable DETR）引入检索社区也具有 bridge 价值。\n\n【方法合理性】: \n方法整体合理，各组件选择都有明确依据：\n- Deformable DETR 作为 region proposer：已在 Groma (ECCV 2024) 和 GAR (ICLR 2026) 中验证其在 ViT 特征上的有效性\n- RoI-Align 提供可微梯度路径：标准操作\n- DeepStack 多分辨率构造：利用 Qwen3-VL 中间层输出，为 Deformable DETR 的多尺度注意力提供真正的分辨率金字塔\n- 两阶段训练（DocLayNet 预训练 → 联合微调）：合理的 curriculum，先建立空间先验再端到端优化\n- 三路 loss（page InfoNCE + element contrastive + IoU grounding）：每个 loss 对应明确的训练信号\n\n**更简单的替代方案**：最直接的简化是 pipeline 方案（DocLayout-YOLO → ColQwen2.5 region embedding），proposal 中已将其作为 \"Pipeline oracle\" baseline 纳入对比。这恰恰是方法论争论的核心——proposal 的论点是端到端优于 pipeline，且 ablation 设计可验证此论点。另一个替代是 AGREE 式的注意力 proxy，但其结构性局限（不对检索 loss 可微）已被充分论证。\n\n**潜在问题**：三路 loss 的平衡（GradNorm/uncertainty weighting）增加了超参搜索空间和训练不稳定风险。batch size 1-4 per A100 可能限制 in-batch negatives 的有效性。\n\n【5 维度打分】:\n  1. 研究问题: 【强】— 问题定义精准，定位在 page-level → sub-page retrieval 的明确 gap 上，有 MMDocIR、BBox-DocVQA 等多个 benchmark 量化佐证（Snappy 59.7% IoU@0.5, VLMs 0.089 F1 vs 0.60 human F1）。Sub-page retrieval 正处于快速演进期（2025-2026 涌现 5+ 并发工作），问题的时效性和重要性毋庸置疑。\n\n  2. 方法与创新: 【强】— 核心创新点（可微 region proposals in retrieval gradient flow）具有结构性新颖度，不是对现有方法的增量改进。与 Groma (ECCV 2024) 和 GAR (ICLR 2026) 的关系是跨领域迁移（detection/understanding → retrieval），而非简单复用。与 AGREE (SIGIR 2026)、ReAlign (SIGIR 2026)、ColParse (arXiv 2026)、RegionRAG (AAAI 2026) 的差异化论证清晰且有说服力。架构选择有充分技术依据。唯一扣分点：核心假设（retrieval-optimal regions 系统性偏离 layout 类别）仍需实验验证，存在假设不成立的风险。\n\n  3. 实验设计: 【强】— 这是 proposal 最突出的亮点之一。4 组 baseline 覆盖所有现有范式（page-level, layout-level, grounding, pipeline oracle）；8 个 ablation 逐步验证各组件贡献；核心假设验证实验（Proposal Divergence Analysis）直接测试 IoU 重叠度和检索性能对比；效率分析含 Pareto frontier；统计报告含 3 runs with mean±std。相比 MMDocIR (arXiv 2505.01457) 的训练无关多模型融合和 AGREE 的单一 page-level nDCG 优化，本 proposal 的评估方案显著更全面。\n\n  4. 可行性: 【中】— 计算需求合理但偏高（4-8× A100-80GB）；训练数据可获取（DocLayNet 80K, MMDocIR annotations, BBox-DocVQA 30K+ pairs）。主要风险：(a) 三路 loss 优化的稳定性——GradNorm 在多任务学习中有效但增加调参复杂度；(b) batch size 受限（1-4 per A100-80GB）可能影响 contrastive learning 效果，需要 gradient accumulation 弥补；(c) DeepStack 多分辨率构造需 pilot validation（proposal 已承认）；(d) 整体工程复杂度高，从零实现到产出结果的周期较长。\n\n  5. 写作与呈现: 【强】— Proposal 结构清晰，逻辑链条完整。从问题定义 → 关键 insight → 与现有工作的精确差异化 → 方法设计 → 实验设计 → 可行性分析，每一步都有量化依据。对失败情形的预案（\"If divergence is minimal...\"）体现了成熟的研究思维。术语使用准确，引用详实。\n\n【概率估计】: [33% - 47%] 中位 40%\n\n【估计理由】: \n这份 proposal 在问题定义、方法创新和实验设计三个维度均表现出色，显著超过 AAAI 投稿的平均水平。核心贡献——将可微 region proposals 置于检索梯度流内——具有结构性新颖度，且与 5+ 并发工作的差异化论证令人信服。实验设计的完备性（pipeline oracle baseline、核心假设验证、8 个 ablation）本身就是显著加分项。\n\n向上拉动因素：(1) 跨社区桥接价值（detection ↔ retrieval）在 AAAI 这样的综合会议上尤其受欢迎；(2) 问题时效性强，sub-page VDR 是 2025-2026 热点方向；(3) 实验设计质量在 proposal 阶段就已超过许多已发表论文。\n\n向下拉动因素：(1) 架构复杂度高（Deformable DETR + RoI-Align + 三路 loss + 多分辨率特征），实验执行难度大，结果可能不如预期；(2) 核心假设（proposal 显著偏离 layout 类别）可能仅获温和验证，削弱 narrative；(3) 无任何初步结果，纯 proposal 状态增加不确定性；(4) 训练稳定性风险（三路 loss 平衡、小 batch size contrastive learning）；(5) 领域竞争激烈，AAAI 截稿前可能出现新的强竞争者。\n\n中位 40% 反映了这是一篇质量上乘的 proposal，但从 proposal 到强结果之间存在非平凡的执行风险。如果实验结果清晰支持端到端优于 pipeline 的论点且核心假设获得验证，概率可上探 47%+；如果结果仅有温和改进或训练不稳定，可能下滑至 33% 附近。\n\n【主要风险】: \n1. **执行复杂度风险**：架构包含过多耦合组件（Deformable DETR decoder + RoI-Align + 三路 loss + 多分辨率特征金字塔 + LoRA + gradient checkpointing），任何环节的工程问题都可能导致整体效果不达预期。三路 loss 的平衡尤其棘手——如果 loss weight 敏感性高，可能需要大量超参搜索，消耗本就紧张的 GPU 预算。\n2. **核心假设温和验证风险**：如果端到端学习的 proposals 与 DocLayNet layout categories 的 IoU 偏离不大（比如 >0.7），那么核心 narrative（\"检索发现了 layout taxonomy 无法捕获的空间结构\"）将被显著削弱。虽然 proposal 准备了 fallback 论点（zero-marginal-cost grounding + 无 pipeline 误差传播），但审稿人可能认为这不足以支撑一篇顶会论文的核心贡献。\n\n【实施评估】:\n  - 计算资源: 4-8× A100-80GB，两阶段训练（DocLayNet 预训练 + 联合微调），需 gradient checkpointing 和 gradient accumulation。保守估计总训练时间 1-2 周（含超参搜索）。\n  - 数据需求: DocLayNet (80K pages, 公开), MMDocIR (173K bootstrapped + 1,685 expert, 公开), BBox-DocVQA (30K+ auto-generated pairs, 公开), Nemotron V2 训练数据对齐（部分可能需要复现/近似）。数据均可获取，无 blocking 问题。\n  - 人工介入: 中等。需要工程实现 Deformable DETR → Qwen3-VL 的集成、多分辨率特征构造的 pilot validation、三路 loss 平衡调优。不需要人工标注。\n  - 训练需求: 必须训练。两阶段：(1) Deformable DETR decoder 在 DocLayNet 上预训练；(2) 全模型联合微调（LoRA on ViT backbone + 全量 DDETR decoder）。\n  - 新 Benchmark: 不需要。使用已有 benchmark（ViDoRe V3, MMDocIR, BBox-DocVQA）。\n  - 预估周期: 从零开始到论文完成约 3-4 个月。架构实现 + pilot validation ~3-4 周；训练 + 超参搜索 ~2-3 周；全量实验 + ablation ~2-3 周；论文写作 ~2-3 周。时间紧凑但可行（距 AAAI 2026 deadline 尚有时间）。\n```\n\nSources:\n- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992)\n- [ColPali](https://arxiv.org/abs/2407.01449)\n- [ColParse / Beyond the Grid](https://arxiv.org/abs/2603.01666)\n- [RegionRAG](https://arxiv.org/pdf/2510.27261)\n- [Multi-Granularity Framework](https://arxiv.org/abs/2505.01457)\n- [AGREE](https://arxiv.org/abs/2511.13415)\n- [ReAlign (GitHub)](https://github.com/NEUIR/ReAlign)\n- [Snappy](https://arxiv.org/abs/2512.02660)\n- [BBox-DocVQA](https://arxiv.org/abs/2511.15090)\n- [Groma](https://arxiv.org/abs/2404.13013)\n- [GAR / Grasp Any Region](https://openreview.net/pdf?id=Gp9lGS9GfY)\n- [SEAL](https://arxiv.org/abs/2508.20778)\n- [MMDocIR](https://arxiv.org/abs/2501.08828)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to evaluate this proposal thoroughly. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- ColPali (ICLR 2025): 奠基性工作，确立了视觉文档检索中late-interaction多向量范式。本proposal在此基础上向sub-page粒度扩展。\n- Nemotron ColEmbed V2 (arXiv 2602.03992, Feb 2026): 当前ViDoRe V3 SOTA (63.42 NDCG@10, Qwen3-VL-8B)。Proposal以其4B版本为同backbone对比基准，定位合理。\n- RegionRAG (AAAI 2026): 区域级RAG，使用外部检测器产生固定proposal，不可随检索目标调整。Proposal核心novelty（可微分proposal在检索梯度流内）直接针对此局限。\n- ColParse / Beyond the Grid (arXiv 2603.01666, Mar 2026): 利用文档解析器产生layout子图做紧凑多向量表示，存储降低95%但区域与任务无关。与proposal的pipeline baseline设计直接对应。\n- AGREE (SIGIR 2026, arXiv 2511.13415): 利用MLLM attention作为空间监督代理，+12.82% nDCG@1，但仅优化页级指标，attention信号对检索loss不可微。Proposal正确识别了这一结构性限制。\n- ReAlign (SIGIR 2026, arXiv 2604.07419): VLM推理驱动的细粒度对齐，离线区域识别，无bbox输出。Proposal的端到端学习方式与之形成互补/竞争关系。\n- Multi-Granularity Framework (arXiv 2505.01457): 多模型融合(ColQwen2+GME+VLM+RRF)达65.56 MMDocIR layout-level，但需多模型且无grounding。\n- Snappy (arXiv 2512.02660): 训练无关的patch-to-region相似度传播，59.7% IoU@0.5。设定了grounding的baseline水平。\n- SEAL (EMNLP 2025): 文本检索中结构感知+masked element alignment，+3.88 NDCG@10。Proposal的element-level contrastive loss直接借鉴此思路，属于合理的跨领域迁移。\n- Groma (ECCV 2024): 类无关Deformable DETR proposal用于MLLM的localized visual tokenization。Proposal的架构设计直接参考此工作。\n- GAR / Grasp Any Region (ICLR 2026): RoI-Align over ViT features用于区域级视觉理解，1B模型超越78B。证明了RoI-Align+ViT的可行性，是proposal的关键技术先例。\n- BBox-DocVQA (arXiv 2511.15090): 空间grounding benchmark，30K+ QA pairs with bbox。Proposal用作IoU grounding loss的监督数据和评测集。\n- DocLayNet: 80K页面、11类layout标注，用作proposal预训练数据。\n\n- 调研总结: 视觉文档检索正从页级向sub-page粒度快速演进，但现有方法均使用task-agnostic的区域定义（layout类别、OCR框、parser输出、VLM识别区域）。将可微分区域proposal置于检索梯度流内是一个尚未被探索的结构性空白，proposal精准定位了这一gap。该领域2025-2026年论文密集（AGREE、ReAlign、ColParse、RegionRAG均为2026年发表），竞争激烈但证明了方向的时效性。\n\n【整体印象】:\n作为审稿人，我的第一反应是积极的——这是一篇有明确结构性创新的proposal。它不是在现有框架上做incremental改进，而是提出了一个新的架构范式：将区域proposal生成嵌入检索梯度流。对现有工作的分析非常清晰，每个competing work的结构性局限都被准确识别。实验设计的完备程度远超一般proposal。总体倾向weak accept到accept之间。\n\n主要顾虑：(1) 架构复杂度较高，如果实验收益不够显著会被质疑 \"over-engineered\"；(2) 核心假设（learned proposals会系统性偏离layout类别）如果不成立，narrative会弱化（虽然proposal有graceful degradation论述）；(3) 多源监督（DocLayNet + MMDocIR + BBox-DocVQA + retrieval pairs）的组合是否引入了不公平优势需要careful discussion。\n\n【核心贡献】:\n核心贡献是**首次将可微分区域proposal置于视觉文档检索的梯度流中**，使检索目标不仅决定\"如何匹配区域与查询\"，更决定\"提出哪些区域\"。这是一个结构性区分（structural distinction），而非参数/训练技巧的改进。附带贡献包括：单模型同时产出page/region/element三粒度检索embedding + 零边际成本的空间grounding。\n\n对领域的价值：中高。它为sub-page视觉文档检索提出了一条新路径（从task-agnostic regions到retrieval-optimal regions），如果实验验证假设成立，将重新定义该子领域的研究方向。即便假设仅部分成立，端到端统一框架本身也有工程和学术价值。\n\n【方法合理性】:\n方法在技术上是合理且有据可循的：\n- Deformable DETR作为proposal生成器已在检测和VLM理解中广泛验证（Groma ECCV 2024, GAR ICLR 2026）\n- RoI-Align的可微性保证了梯度可以从检索loss传回proposal decoder，这是核心技术可行性的基础\n- 多分辨率特征金字塔构建（DeepStack中间层 → 不同步长空间池化）是Deformable DETR多尺度注意力的标准做法\n- 三段式loss（page InfoNCE + element contrastive + IoU grounding）的设计有各自独立的motivation\n- 两阶段训练（proposal预训练 → 联合微调）是合理的warm-start策略\n\n**更简单的替代方案**：最直接的替代是pipeline方案（DocLayout-YOLO → ColQwen region embedding），proposal已将其作为pipeline oracle baseline纳入。另一个替代是在AGREE/ReAlign基础上改进，但这些方法的结构性限制（attention/VLM作为代理而非端到端）已被清晰论述。我认为proposal对\"为什么需要端到端\"的论证是充分的，但最终需要实验数据证明end-to-end优于pipeline的具体幅度。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — 视觉文档检索从页级到sub-page粒度的演进是领域当前最活跃的研究方向（2025-2026年密集产出AGREE、ReAlign、ColParse、RegionRAG等多篇论文）。现有方法均使用task-agnostic区域定义这一观察是准确的，\"检索最优区域可能偏离预定义layout类别\"这一假设有理论吸引力且可实证检验。问题的重要性和时效性毋庸置疑。\n\n  2. 方法与创新: 【强】 — 核心创新点（可微分region proposal在检索梯度流内）是一个genuine structural novelty，不是对现有方法的incremental改进。与所有6个directly competing works（AGREE、ReAlign、ColParse、RegionRAG、Multi-Gran Framework、Snappy）的结构性差异已被清晰阐述。技术组件（Deformable DETR + RoI-Align + late interaction）各自成熟可靠，但组合方式新颖。从检测/VLM理解社区（Groma ECCV 2024, GAR ICLR 2026）到检索社区的技术迁移是合理且timely的。轻微扣分：架构复杂度较高，如果最终gains modest，\"Occam's razor\" argument可能被reviewer提出。\n\n  3. 实验设计: 【强】 — 这是proposal最突出的亮点之一。4类benchmark（ViDoRe V3, MMDocIR, BBox-DocVQA, ViDoRe V3 grounding）覆盖page-level、layout-level和spatial grounding。4组baseline（page-level、layout-level、grounding、pipeline oracle）非常完备，特别是pipeline oracle baseline直接回应了\"为什么不用pipeline\"的reviewer质疑。8项ablation study设计精细，逐步叠加components可清晰展示各组件贡献。核心假设验证分析（proposal divergence from layout categories）是加分项。效率分析和统计报告（3 runs, mean±std）体现了严谨性。实验标准与该领域顶会论文（如Nemotron ColEmbed V2的评测设置）对齐。\n\n  4. 可行性: 【中】 — 技术路线每一步都有先例可循（Deformable DETR、RoI-Align、DocLayNet预训练等），但系统集成的复杂度不低。训练需要4-8× A100-80GB，是substantial但可获取的资源。多源数据依赖（DocLayNet + MMDocIR + BBox-DocVQA + retrieval pairs）增加了数据准备的工作量。批大小1-4 per GPU可能限制in-batch negatives的效果，需要gradient accumulation，增加训练不稳定性风险。DeepStack多分辨率构建的pilot验证是必要的前置步骤。总体：对有经验的团队可行，但执行风险中等。\n\n  5. 写作与呈现: 【强】 — Proposal的组织结构非常清晰：问题→洞察→landscape→方法→实验。对每个competing work的分析精准且公平，不过度贬低也不回避比较。核心假设的formulation清晰且有fallback plan。技术细节（如三粒度的precise定义、loss公式的设计动机）充分但不冗余。对可行性的坦诚讨论（如内存估算标注\"pending pilot profiling\"）增加了可信度。\n\n【概率估计】: [35% - 48%] 中位 40%\n\n【估计理由】:\n这是一篇novelty清晰、实验设计完备、定位精准的proposal，在方法创新和实验计划方面表现出色。给出35-48%而非更高的原因：\n\n(1) **执行风险**：这仍是一个proposal而非completed paper——核心假设（proposal divergence）需要实验验证，端到端训练的收益幅度未知。如果gains modest（如仅2-3 points on benchmarks），reviewer可能认为复杂度不值得。\n\n(2) **领域竞争激烈**：2025-2026年该领域产出密集（AGREE、ReAlign、ColParse、RegionRAG、Nemotron V2等），投稿时可能面临更多concurrent/新出现的competing works。\n\n(3) **Reviewers' complexity concern**：三源监督 + 两阶段训练 + 三粒度输出的系统可能被部分reviewer视为over-engineered，特别是如果ColParse这类简洁方法能达到comparable结果。\n\n(4) **AAAI审稿variance**：AAAI审稿有较大variance，遇到不熟悉VDR sub-field的reviewer可能低估贡献。\n\n上限48%的理由：如果实验结果显著优于pipeline oracle且假设验证成功，加上excellent实验设计，可以达到strong accept territory。下限35%的理由：如果gains marginal或某些组件ablation表现不佳，但novelty claim仍成立。\n\n【主要风险】:\n1. **收益幅度不确定性**：端到端可微分proposal相比简单pipeline（如DocLayout-YOLO + ColQwen）的性能提升可能不足以justify架构复杂度。如果improvement < 3-5 points，reviewer很可能以\"complexity不值得\"为由给borderline reject。这是最核心的风险。\n2. **核心假设可能不成立**：learned proposals可能并不显著偏离DocLayNet layout categories（即layout taxonomy已足够覆盖retrieval-optimal regions）。虽然proposal有graceful degradation论述（零边际成本grounding + 消除pipeline error propagation），但这会使narrative从\"发现新的retrieval-specific spatial structures\"弱化为\"更便捷的端到端pipeline\"，contribution weight下降。\n\n【实施评估】:\n  - 计算资源: 4-8× A100-80GB GPU（训练），估计训练周期2-4周（含pilot验证）。推理时需要支持Deformable DETR forward pass，但overhead相对可控（~16-40M额外参数）。\n  - 数据需求: DocLayNet (80K页面, 公开可用) + MMDocIR annotations (~173K bootstrapped + ~1,685 expert) + BBox-DocVQA (30K+ QA pairs with bbox) + 标准检索query-page pairs。所有数据集均为公开可用，但多数据源的准备和对齐需要工程工作量。\n  - 人工介入: 中等。主要在数据预处理、多分辨率特征金字塔pilot验证、loss weight调参阶段需要人工判断和迭代。\n  - 训练需求: 两阶段训练——(1) Deformable DETR decoder在DocLayNet上预训练（估计1-2天on 4 GPUs）; (2) 联合微调三路loss（估计1-2周含超参搜索和多次run）。需要GradNorm/uncertainty weighting调试。\n  - 新 Benchmark: 不需要。所有评测benchmark（ViDoRe V3, MMDocIR, BBox-DocVQA）已有现成。\n  - 预估周期: 从proposal到可投稿paper约10-14周（含2周pilot验证 + 3-4周主实验 + 2周ablation和分析 + 2-3周写作和修改 + buffer）。如果pilot阶段遇到内存或训练不稳定问题，可能延长2-4周。\n```\n\nSources:\n- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449)\n- [Nemotron ColEmbed V2](https://arxiv.org/html/2602.03992v1)\n- [RegionRAG: Region-level Retrieval-Augmented Generation](https://arxiv.org/abs/2510.27261)\n- [Beyond the Grid / ColParse](https://arxiv.org/abs/2603.01666)\n- [AGREE: Attention Grounded Enhancement for VDR](https://arxiv.org/abs/2511.13415)\n- [ReAlign: Reasoning-Guided Fine-Grained Alignment](https://arxiv.org/abs/2604.07419)\n- [Snappy: Spatially-Grounded Document Retrieval](https://arxiv.org/pdf/2512.02660)\n- [BBox-DocVQA](https://arxiv.org/abs/2511.15090)\n- [SEAL: Structure and Element Aware Learning](https://arxiv.org/abs/2508.20778)\n- [Groma: Localized Visual Tokenization](https://arxiv.org/abs/2404.13013)\n- [GAR: Grasp Any Region](https://openreview.net/pdf?id=Gp9lGS9GfY)\n- [A Multi-Granularity Retrieval Framework](https://arxiv.org/pdf/2505.01457)\n- [ViDoRe Benchmark](https://github.com/illuin-tech/vidore-benchmark)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# End-to-End Multi-Granularity Visual Document Retrieval via Differentiable Region Proposals\n\n## Core Problem\n\nVisual document retrieval (VDR) models operate at page granularity, leaving a ~32pp gap to layout-level retrieval (MMDocIR) and limited spatial grounding (Snappy achieves 59.7% IoU@0.5 without training, arXiv 2512.02660; BBox-DocVQA shows Qwen2.5VL-72B reaches only 35.20% mean IoU, arXiv 2511.15090). Existing sub-page approaches rely on external parsers (ColParse, arXiv 2026), task-agnostic fixed region proposals (RegionRAG, AAAI 2026), multi-model fusion pipelines (Multi-Granularity Framework, arXiv 2505.01457, reaching 65.56 on MMDocIR layout-level), proxy supervision that optimizes only page-level metrics (AGREE, SIGIR 2026), or VLM distillation for fine-grained alignment without spatial grounding output (ReAlign, SIGIR 2026, arXiv:2604.07419). No single model produces retrieval embeddings at page, region, and element granularities with learned spatial grounding.\n\n## Key Insight: Region Proposals Inside the Retrieval Gradient Flow\n\nPost-hoc analysis reveals that ViT patch embeddings already encode spatial neighborhood information (SIGIR 2025 reproducibility study), and inference-time methods can partially recover it (Snappy's 59.7% IoU@0.5, AGREE's attention proxy with +12.82% nDCG@1). But because no existing model places region proposal generation within the retrieval gradient flow, spatial structure recovery has an inherent ceiling.\n\nDiffRegion-VDR is the first VDR model where retrieval loss gradients directly modify region proposal positions and sizes through differentiable RoI-Align. This is a structural distinction from all existing approaches: AGREE's spatial signal comes from a frozen MLLM's attention (not differentiable w.r.t. retrieval loss); ReAlign's comes from offline VLM reasoning (not part of the forward-backward pass); ColParse's regions are from an external parser (no gradient connection); RegionRAG's proposals are from a fixed detector (trained separately). Only in DiffRegion-VDR does the retrieval objective determine not just how to match regions to queries, but which regions to propose.\n\n**Core hypothesis**: Joint fine-tuning will cause proposals to diverge systematically from DocLayNet layout categories — the model will discover retrieval-specific spatial structures that no predefined layout taxonomy captures. This represents the evolution of structured retrieval embeddings from grid-structured (ColBERT token-level → ColPali patch-level) to content-structured (learned semantic regions).\n\n## Research Landscape and Differentiation\n\n**Page-level VDR** is maturing: Nemotron ColEmbed V2 (arXiv 2602.03992) achieves 63.42 NDCG@10 on ViDoRe V3 with Qwen3-VL-8B. ColPali (ICLR 2025) established late-interaction visual retrieval.\n\n**Sub-page retrieval** is fragmented across four paradigms, each structurally limited:\n- *External parser pipeline*: ColParse (arXiv 2026) segments pages via document parsers, reducing storage by 95%, but regions are task-agnostic and inherit parser errors.\n- *Fixed-proposal training*: RegionRAG (AAAI 2026) trains region-level alignment on fixed proposals from external detectors; proposals cannot adapt to retrieval objectives.\n- *Training-free fusion*: Multi-Granularity Framework (arXiv 2505.01457) combines ColQwen2+GME+VLM+RRF for 65.56 on MMDocIR layout-level, but requires multiple models and lacks grounding.\n- *VLM distillation*: ReAlign (SIGIR 2026, arXiv:2604.07419) uses superior VLMs to identify query-related regions and generate query-aware descriptions as supervision. Fine-grained alignment is learned, but: (a) quality is upper-bounded by teacher VLM's grounding ability; (b) no bounding-box grounding output; (c) region identification is offline during training, not dynamic at inference.\n\n**Grounding** is limited: Snappy (arXiv 2512.02660) maps patch similarity to OCR regions at inference (59.7% IoU@0.5 on BBox-DocVQA); AGREE (SIGIR 2026) uses MLLM attention as proxy but optimizes page-level nDCG only. ViDoRe V3 VLMs achieve 0.089 F1 on bbox localization vs. 0.60 human F1.\n\n**The gap**: All sub-page methods use task-agnostic region definitions (layout categories, OCR boxes, parser outputs, VLM-identified regions). The optimal retrieval region for a given query may not align with predefined layout classes. Hypothesis: retrieval-optimal regions exhibit systematic geometric divergence from standard layout categories. Even if this divergence is modest, end-to-end learning provides zero-marginal-cost grounding and eliminates pipeline error propagation.\n\n**Detection–retrieval community gap**: Differentiable region proposals via Deformable DETR are proven in VLM understanding — Groma (ECCV 2024) uses class-agnostic proposals for localized visual tokenization; GAR (ICLR 2026) applies RoI-Align over ViT features to outperform 78B models with 1B parameters. Element-level alignment is proven for text retrieval — SEAL (EMNLP 2025) achieves +3.88 NDCG@10 via structure-aware masked element alignment. Neither technique has been applied to visual document retrieval.\n\n## Proposed Approach\n\n**Architecture.** Attach a lightweight class-agnostic Deformable DETR decoder to Qwen3-VL-4B's ViT feature maps. To provide genuine multi-resolution input for Deformable DETR's multi-scale deformable attention, apply different-stride 2D spatial pooling to the 4 DeepStack intermediate outputs (layers sharing the same spatial resolution but differing in semantic abstraction), constructing a resolution pyramid analogous to Groma's neighbor-patch concatenation strategy on DINOv2. RoI-Align extracts context-aware region embeddings from proposed regions. Multi-granularity late-interaction scoring operates at three levels within a single forward pass.\n\n**Three granularity levels** (precise definitions):\n- *Page-level*: All ViT patch token embeddings participate in late interaction with query tokens (standard ColPali-style).\n- *Region-level*: Deformable DETR top-K learned proposals → RoI-Align → region embeddings for late interaction. These are the model's primary sub-page retrieval units, dynamically generated per document.\n- *Element-level*: During training, region proposals matched (by IoU) to MMDocIR layout annotations serve as supervised targets for element-level contrastive alignment. At inference, region proposals naturally approximate element-level retrieval without ground-truth layout information.\n\n**Training.** Two-stage:\n1. *Proposer pre-training*: Train the Deformable DETR decoder on DocLayNet (80K annotated pages, 11 layout classes) for class-agnostic region proposal generation, establishing spatial priors.\n2. *Joint fine-tuning* with three losses:\n   - (a) Page-level InfoNCE: global retrieval on query-page pairs (training data aligned with Nemotron ColEmbed V2 recipe where possible for fair comparison; differences documented).\n   - (b) Element-level contrastive alignment (inspired by SEAL, EMNLP 2025): on MMDocIR layout annotations (~173K bootstrapped + ~1,685 expert-annotated pairs; ablation on bootstrapped vs. expert-only).\n   - (c) IoU grounding loss: spatial localization supervised by BBox-DocVQA training split (30K+ auto-generated QA pairs with bbox, arXiv:2511.15090) + DocLayNet layout boxes as supplement.\n   - Loss balancing via GradNorm or uncertainty weighting. Retrieval losses backpropagate through RoI-Align into the proposal decoder, enabling proposals to evolve from layout-generic to retrieval-optimal.\n\n**Why end-to-end beats pipeline** (addressing the trivial alternative): (1) Pipeline regions are task-agnostic — parser/detector categories cannot adapt to retrieval needs; learned proposals can, and our core hypothesis predicts they will diverge. (2) Pipeline requires multiple independent models, preventing joint optimization. (3) Pipeline methods produce zero grounding output; DiffRegion-VDR provides bounding boxes at zero marginal cost.\n\n## Experimental Design\n\n### Benchmarks\n- **ViDoRe V3**: Page-level retrieval — NDCG@5, NDCG@10 (per-dataset breakdown by document type)\n- **MMDocIR**: Page-level Recall@1/3/5; Layout-level Recall@1/3/5\n- **BBox-DocVQA** (primary grounding, arXiv:2511.15090): IoU@0.25, IoU@0.5, IoU@0.7, mean IoU\n- **ViDoRe V3 grounding** (supplementary): F1@IoU=0.5\n\n### Baselines (4 groups)\n- **Page-level**: ColPali v1.3 (ICLR 2025), ColQwen2.5-v0.2, Nemotron ColEmbed V2-4B (same backbone, arXiv 2602.03992), Nemotron ColEmbed V2-8B\n- **Layout-level**: ColParse (arXiv 2026), Multi-Granularity Framework (arXiv 2505.01457), RegionRAG (AAAI 2026)\n- **Grounding**: Snappy (arXiv 2512.02660, training-free), AGREE (SIGIR 2026)\n- **Pipeline oracle**: DocLayout-YOLO → ColQwen2.5 region embedding → late interaction (same backbone, external detector)\n\n### Ablation Studies\n1. Qwen3-VL-4B + page-level InfoNCE only (≈Nemotron V2-4B training recipe)\n2. \\+ Deformable DETR decoder + RoI-Align, page-level loss only\n3. \\+ Element-level contrastive alignment loss\n4. \\+ IoU grounding loss (full model)\n5. Two-stage (DocLayNet pre-train → joint fine-tune) vs. end-to-end from scratch\n6. Loss weight sensitivity (3–5 ratio configurations, each 2+ runs)\n7. Proposal count: top-K ∈ {50, 100, 200, 300}\n8. Multi-level feature utilization: (a) DDETR on final ViT layer only; (b) DDETR on 4 DeepStack levels, same resolution; (c) DDETR on 4 DeepStack levels with spatial pooling (multi-resolution)\n\n### Core Hypothesis Validation: Proposal Divergence Analysis\n- Measure IoU overlap between learned proposals (after stage 2) and DocLayNet ground-truth layout annotations → quantify geometric divergence\n- Compare retrieval performance of learned proposals vs. DocLayNet-category proposals (used as fixed regions in a pipeline)\n- Visualize proposal distributions across document types: which retrieval-specific structures emerge that layout taxonomy misses?\n- If divergence is minimal: the contribution is still valid via zero-marginal-cost grounding + pipeline error elimination; explicitly discuss\n\n### Region Proposer Analysis\n- Class-agnostic proposal recall@50/100/300 on DocLayNet test set\n- Proposal quality change after joint fine-tuning — does retrieval loss improve or degrade detection recall?\n- Visualization across document types (papers, slides, invoices, infographics)\n\n### Efficiency Analysis\n- Parameter overhead: DDETR decoder ~16–40M params on Qwen3-VL-4B (4.44B); report exact count and percentage\n- Vectors/page: page + region + element tokens vs. ColPali (~1030/page) vs. ColParse (<10/page)\n- Query latency (ms/query) and index storage (MB/1K pages)\n- Performance vs. storage and performance vs. latency Pareto frontier\n\n### Statistical Reporting\n- Main results: 3 independent runs, report mean ± std\n- Ablation: at minimum full model and page-only baseline with 3 runs; others single-run with notation\n\n### Feasibility\n- Multi-resolution construction: 4 DeepStack levels → 2D reshape → stride-{1,2,4,8} spatial pooling → multi-resolution pyramid for Deformable DETR. Pilot validation on DocLayNet detection AP.\n- Training memory: Qwen3-VL-4B FP16 ~9GB + DDETR decoder + RoI-Align regions + three-way late interaction. Conservative estimate: batch size 1–4 per A100-80GB (pending pilot profiling). Memory optimizations: top-K proposals only for retrieval loss (remainder for detection pre-training only), LoRA on backbone ViT, gradient checkpointing, gradient accumulation with in-batch negatives. Target: 4–8× A100-80GB.\n- OOD generalization: per-dataset analysis on ViDoRe V3 document types absent from DocLayNet (slides, web screenshots, infographics).\n\n## Key References\n\n- Groma: Localized Visual Tokenization for Grounding MLLMs (ECCV 2024)\n- Grasp Any Region (GAR): Contextual Pixel Understanding for MLLMs (ICLR 2026)\n- SEAL: Structure and Element Aware Learning for Document Retrieval (EMNLP 2025)\n- ColPali: Efficient Document Retrieval with Vision Language Models (ICLR 2025)\n- MMDocIR: Benchmarking Multimodal Retrieval for Long Documents (arXiv 2025)\n- AGREE: Attention Grounded Enhancement for VDR (SIGIR 2026)\n- ReAlign: Optimizing VDR with Reasoning-Guided Fine-Grained Alignment (SIGIR 2026, arXiv:2604.07419)\n- RegionRAG: Region-level RAG for Visual Document Understanding (AAAI 2026)\n- Beyond the Grid / ColParse: Layout-Informed Multi-Vector Retrieval (arXiv 2026)\n- Deformable DETR: Deformable Transformers for Object Detection (ICLR 2021)\n- Reproducibility and Insights into VDR with Late Interaction (SIGIR 2025)\n- Nemotron ColEmbed V2: Efficient Retrieval with Late Interaction (arXiv 2602.03992, Feb 2026)\n- A Multi-Granularity Multimodal Retrieval Framework (arXiv 2505.01457)\n- Snappy: Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation (arXiv 2512.02660)\n- BBox-DocVQA: Bounding-Box Grounded Document VQA (arXiv:2511.15090)\n- DocLayNet: A Large-scale Dataset for Document Layout Segmentation"
}
````

---

### Runtime record

_source line 2 · 2026-05-30T07:36:02.680Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:36:02.680Z",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-30T07:36:02.695Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have comprehensive research coverage. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01272) (ICLR 2025): 奠定了 patch-level late-interaction VDR 范式。本 proposal 在此基础上提出 region-level 扩展，构成方法论的直接上游。
- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992) (arXiv Feb 2026): 当前 ViDoRe V3 SOTA，8B 模型 63.42 NDCG@10。本 proposal 选择同系 Qwen3-VL-4B backbone 并对齐训练 recipe，baseline 设定合理。
- [RegionRAG](https://arxiv.org/abs/2510.27261) (AAAI 2026): 最直接竞争者之一——region-level RAG，但使用外部检测器生成固定 proposals，无法随 retrieval objective 调整。proposal 的"可微 region proposal"正好针对此限制。
- [ColParse / Beyond the Grid](https://arxiv.org/abs/2603.01666) (arXiv Mar 2026): 外部 parser pipeline，storage 降 95%，但 regions task-agnostic 且继承 parser errors。另一条需对比的 pipeline 路线。
- [AGREE](https://arxiv.org/abs/2511.13415) (SIGIR 2026): 用 frozen MLLM attention 做 proxy grounding，+12.82% nDCG@1，但 spatial signal 非可微、仅优化 page-level metric。
- [ReAlign](https://arxiv.org/abs/2604.07419) (SIGIR 2026): VLM distillation 做 fine-grained alignment，无 bbox 输出，offline region identification。与本 proposal 的 end-to-end 可微方案形成鲜明对比。
- [Groma](https://arxiv.org/abs/2404.13013) (ECCV 2024): 用 class-agnostic region proposals 做 localized visual tokenization for MLLMs。proposal 借鉴其 neighbor-patch 策略构造多分辨率特征。
- [GAR / Grasp Any Region](https://arxiv.org/abs/2510.18876) (ICLR 2026): RoI-Align over ViT features for region-level understanding，1B 超越 78B。证明 RoI-Align + ViT 的可行性，但应用于 understanding 而非 retrieval。
- [SEAL](https://arxiv.org/abs/2508.20778) (EMNLP 2025): Element-level contrastive alignment for text document retrieval，+3.88 NDCG@10。proposal 的 element-level loss 直接受此启发，但移植到 visual domain。
- [Multi-Granularity Framework](https://arxiv.org/abs/2505.01457) (arXiv May 2025): ColQwen2+GME+VLM+RRF 多模型融合，MMDocIR layout-level 65.56。pipeline 方案，无 grounding。
- [Snappy](https://arxiv.org/abs/2512.02660) (arXiv Dec 2025): Training-free 方案，patch similarity → OCR regions，59.7% IoU@0.5。grounding baseline。
- [BBox-DocVQA](https://arxiv.org/abs/2511.15090) (arXiv Nov 2025): 3.6K documents, 32K QA pairs with bbox grounding。proposal 使用其 training split 作为 IoU grounding loss 的监督源。
- [MMDocIR](https://arxiv.org/abs/2501.08828) (arXiv Jan 2025): 1,685 expert + 173K bootstrapped pairs，page-level + layout-level dual task。proposal 的 element-level loss 直接使用其 layout annotations。

- **调研总结**: Sub-page VDR 是 2025-2026 年的活跃前沿，已出现 5+ 并行工作（ColParse、RegionRAG、AGREE、ReAlign、Multi-Granularity Framework），但全部依赖 task-agnostic 的区域定义（parser/detector/VLM）。将可微 region proposals 嵌入 retrieval 梯度流是一个尚未被占领的方法空间。同时，Groma、GAR 已在 VLM understanding 侧证明了 RoI-Align + ViT 的可行性，SEAL 已在 text retrieval 侧证明了 element-level alignment 的有效性，但两者均未被迁移到 visual document retrieval。本 proposal 处于这两个成熟技术流的交汇点，方向正确且时机恰当。

【整体印象】:
作为审稿人，我的第一反应是 **lean accept (weak accept)**。这是一篇方向清晰、定位精准、实验设计异常完备的 proposal。核心 idea——将 differentiable region proposals 嵌入 retrieval 梯度流——填补了一个清晰且被多篇并行工作间接验证的研究空白。proposal 对文献的掌握程度接近 survey 级别，每一个竞争方法的结构性限制都被准确指出。特别值得赞赏的是其科学诚实性：proposal 明确讨论了"如果 divergence 很小怎么办"的 fallback 论点，以及 pipeline oracle baseline 的设计。

主要犹豫点在于：(1) 核心假设（learned proposals 会系统性偏离 layout categories）是否能在实验中得到强有力验证尚不确定；(2) 三路 loss + 多数据源的训练复杂度可能导致工程困难；(3) 部分审稿人可能认为这是"在 retrieval 模型上接一个 detection head"的 incremental 工作。但整体来看，novelty claim 经得起检验，实验方案的完备性是显著加分项。

【核心贡献】:
1. **结构性创新**：首个将 region proposal 生成置于 retrieval loss 梯度流内的 VDR 模型，实现了从 task-agnostic regions 到 retrieval-optimal regions 的范式转变。这不是工程集成，而是一个有明确假设可验证的结构性区分（retrieval gradients → proposal positions/sizes）。
2. **Multi-granularity unification**：单个 forward pass 内生成 page/region/element 三级 retrieval embeddings + spatial grounding，消除 pipeline 依赖。
3. **Cross-community bridge**：将 detection 社区的 Deformable DETR + RoI-Align 和 retrieval 社区的 late interaction + contrastive alignment 在 VDR 中首次融合。

这些贡献对领域的价值：如果核心假设成立（learned regions ≠ layout categories），这将重新定义 sub-page VDR 的研究方向——从"如何更好地利用预定义区域"转向"如何学习 retrieval-specific 区域"。即使假设不完全成立，zero-marginal-cost grounding + pipeline error elimination 也有实用价值。

【方法合理性】:
方法整体合理，技术选择有据可循：
- **Deformable DETR decoder**: class-agnostic region proposal 的标准选择，已在 Groma (ECCV 2024) 和 GAR (ICLR 2026) 中验证。将其接在 Qwen3-VL-4B 的 ViT feature map 上是自然的架构选择。
- **DeepStack multi-resolution**: 利用不同 depth 的 intermediate outputs + spatial pooling 构造分辨率金字塔，为 multi-scale deformable attention 提供输入。这比简单使用最后一层更合理，类似 Groma 的 neighbor-patch 策略。
- **RoI-Align → late interaction**: 从 proposals 提取 region embeddings 用于 late interaction scoring，梯度可以通过 RoI-Align 反传到 proposal decoder，这是方法的核心创新点，技术上可行（RoI-Align 本身是可微的）。
- **三路 loss 设计**: page-level InfoNCE + element-level contrastive + IoU grounding 的组合覆盖了 retrieval + grounding 两个目标，GradNorm/uncertainty weighting 是处理多任务 loss 的标准做法。

**更简单的替代方案？** 是的——最直接的替代是 pipeline 方案：DocLayout-YOLO → ColQwen2.5（proposal 已将其作为 "pipeline oracle" baseline）。如果 pipeline oracle 已经很强，end-to-end 的边际收益可能有限。但 proposal 的论点是：(1) pipeline regions 无法随 retrieval 目标调整；(2) pipeline 无法提供 grounding。这个论点逻辑上成立，但需要实验验证边际收益的实际大小。

**潜在方法问题**：
1. Region-level late interaction 中，top-K proposals 会引入大量额外 embedding vectors（K=100-300），对 index storage 和 query latency 有显著影响。proposal 的 efficiency analysis 需要认真对待这一点。
2. 三路 loss 的 balancing 可能非常敏感，GradNorm 不总是有效。proposal 规划了 3-5 ratio configurations，这是合理的但可能不够。
3. DocLayNet pre-training → joint fine-tuning 的 two-stage 设计引入了额外复杂度。如果 from-scratch 训练效果接近，two-stage 的必要性需要论证。

【5 维度打分】:

1. **研究问题: 强** — Sub-page VDR 是领域当前最活跃的研究前沿（AAAI 2026 的 RegionRAG、SIGIR 2026 的 AGREE 和 ReAlign、arXiv 2026 的 ColParse 和 Multi-Granularity Framework 均在尝试解决此问题），但所有现有方法都依赖 task-agnostic 区域定义。"retrieval-optimal regions 是否与 layout categories 不同"是一个有明确科学价值的假设，值得验证。研究问题的时效性和重要性都很强。

2. **方法与创新: 中-强** — 核心创新（differentiable region proposals in retrieval gradient flow）是genuinely novel的——经调研确认，没有任何已发表或公开的工作做过这件事。Groma/GAR 在 understanding 侧用了 RoI-Align，SEAL 在 text retrieval 侧用了 element-level alignment，但将它们结合并应用于 VDR 是新的。但个别审稿人可能认为这是"已有组件的组合"（Deformable DETR + ColPali + RoI-Align），评价为 incremental。proposal 需要在核心假设验证（learned regions vs. layout categories 的 divergence analysis）上提供强有力的实验证据来化解这一质疑。

3. **实验设计: 强** — 这是 proposal 最突出的亮点。
   - **Baselines**: 4 组 baselines 覆盖 page-level（ColPali、Nemotron V2）、layout-level（ColParse、RegionRAG、Multi-Gran）、grounding（Snappy、AGREE）、以及关键的 pipeline oracle（DocLayout-YOLO + ColQwen2.5），这个 pipeline oracle 是直接回答"为什么不用 pipeline"的最佳实验设计。
   - **Ablation**: 8 个 ablation 维度系统地剥离每个组件的贡献，特别是 multi-level feature utilization 的 3 级对比（final layer only → same resolution → multi-resolution）设计精良。
   - **核心假设验证**: 专门设计了 proposal divergence analysis（IoU overlap 度量、learned vs. fixed proposals 对比、可视化），这是论文最关键的实验，设计合理。
   - **统计报告**: 主要结果 3 runs + std，ablation 标注单 run，符合社区标准。
   - 唯一不足：缺少下游 RAG/QA 端到端评估，这在近期 VDR 论文中越来越被期望（但不是致命缺陷）。

4. **可行性: 中** — 
   - **计算**: 4-8× A100-80GB 是严肃的资源需求，但对于学术界的 VDR 研究来说属于可接受范围（Nemotron V2 的训练也需要类似规模）。batch size 1-4 per A100 可能限制 in-batch negatives 的效果，需要 gradient accumulation。
   - **数据**: 所有数据集（DocLayNet 80K、MMDocIR 173K+1.7K、BBox-DocVQA 32K、page-level retrieval data）均公开可用，但整合 3 个不同来源的 supervision signals 增加了工程复杂度。
   - **Training complexity**: 三路 loss + two-stage training + LoRA + gradient checkpointing 的组合引入了大量超参数。loss balancing 失败可能导致某一 granularity 的性能退化。proposal 规划了 3-5 ratio configurations，但实际调参可能需要更多。
   - **Timeline**: 合理估计需要 3-4 个月的全职工作（1 个月搭建 pipeline + DocLayNet pre-training pilot，1.5 个月联合训练调参，1 个月评估与论文撰写），对 AAAI 2026 ddl 来说时间紧但可行。

5. **写作与呈现: 强** — Proposal 的写作质量在我审过的 proposals 中属于上乘：
   - 文献定位精准，每个竞争方法的结构性限制被逐一分析
   - "Why end-to-end beats pipeline" 段落直接回应了最明显的 trivial alternative 质疑
   - 科学诚实性好——明确讨论了假设不成立时的 fallback
   - 术语使用一致，架构描述清晰
   - 唯一建议：可以增加一个 high-level architecture figure 的描述，使审稿人更快把握整体流程

【概率估计】: [30% - 48%] 中位 38%

【估计理由】:
推理过程如下：

(1) **方向和 novelty**: 经调研确认，"将可微 region proposals 嵌入 VDR 梯度流"是一个genuinely novel的方向，no prior work 做过这件事。方向正确且时机好（sub-page VDR 是 2025-2026 热点）。这把 baseline 提到了 ~30%。

(2) **实验设计加分**: 实验方案的完备性（4 组 baselines、8 ablation dimensions、核心假设验证、pipeline oracle、统计报告）在 proposal 阶段就达到了很高的标准。如果执行到位，实验部分不会成为被拒的理由。这加 ~5-8%。

(3) **风险折扣**:
   - 核心假设风险：如果 learned proposals 与 layout categories 的 divergence 很小，论文的核心 narrative 会被削弱。proposal 有 fallback 论点（zero-marginal-cost grounding + pipeline error elimination），但审稿人可能认为贡献不够显著。此风险折扣 ~5%。
   - "组件组合" 质疑：部分审稿人可能认为这是 Deformable DETR + ColPali 的 straightforward combination。proposal 需要在 divergence analysis 上有强结果来反驳。此风险折扣 ~3%。
   - 训练复杂度风险：三路 loss 的 balancing 失败可能导致实际结果不如预期。此风险折扣 ~2%。
   - 缺少端到端 RAG 评估：虽不致命，但可能被 1-2 位审稿人提及。此风险折扣 ~1%。

(4) **综合**: 30% (方向+novelty baseline) + 8% (实验设计) - 5% (假设风险) - 3% (incremental质疑) - 2% (训练复杂度) = ~28% lower bound → 因写作质量和positioning的加分调整至 30%。Upper bound 48% 对应"核心假设得到验证 + 所有实验按计划完成 + 论文写作清晰"的乐观情景。中位 38% 反映了"方向正确、实验完备、但核心贡献的 impact 取决于实验结果"的不确定性。

注：38% 对应"整体扎实、有明确 novelty、实验方案强，但存在合理风险"的投稿，在AAAI的接收率背景下属于 competitive but not guaranteed 的区间。

【主要风险】:
1. **核心假设验证风险**: 如果 learned proposals 最终与 DocLayNet layout categories 高度重合（divergence analysis 显示 IoU overlap > 0.7），论文的核心 narrative——"retrieval-optimal regions ≠ layout regions"——将难以支撑，贡献退化为"端到端训练的 marginal improvement + 附带 grounding"，部分审稿人会认为 contribution 不足以 accept。
2. **"组件组合 vs. 本质创新" 质疑**: 1-2 位审稿人可能认为这是将 detection 社区的 Deformable DETR/RoI-Align 和 retrieval 社区的 late interaction 做 straightforward engineering integration，novelty 评分为 borderline。如果核心假设的实验证据不够强，这一质疑会被放大。

【实施评估】:
  - 计算资源: 4-8× A100-80GB（或等价），~2-4 周 GPU 时间用于联合训练和 ablation studies。DocLayNet pre-training 约需 1-2 天。全部 ablation（8 configurations × multiple seeds）可能需要 ~100-200 GPU-days。
  - 数据需求: DocLayNet (80K pages, 公开), MMDocIR (173K+1.7K pairs, 公开), BBox-DocVQA (32K QA pairs, 公开), page-level retrieval training data (需对齐 Nemotron V2 recipe, 部分可能需要自行构造)。所有数据公开可用，但数据处理 pipeline 较复杂。
  - 人工介入: 中等。需要手动对齐不同数据源的格式，设计 loss balancing 实验，进行 proposal divergence 的定性可视化分析。无需人工标注。
  - 训练需求: 是，需要训练。Two-stage: (1) Deformable DETR decoder on DocLayNet; (2) Joint fine-tuning with 3 losses on Qwen3-VL-4B (LoRA + gradient checkpointing)。预计每次完整训练 2-5 天 (4× A100)。
  - 新 Benchmark: 否。使用现有 benchmarks (ViDoRe V3, MMDocIR, BBox-DocVQA)。
  - 预估周期: 3-4 个月全职工作。Month 1: pipeline 搭建 + DocLayNet pre-training + 内存 profiling。Month 2-2.5: 联合训练调参 + ablation studies。Month 2.5-3.5: evaluation + divergence analysis + 论文撰写。Month 3.5-4: revision + 补充实验。
```

Sources:
- [RegionRAG: Region-level Retrieval-Augmented Generation](https://arxiv.org/abs/2510.27261)
- [Beyond the Grid / ColParse](https://arxiv.org/abs/2603.01666)
- [Snappy: Spatially-Grounded Document Retrieval](https://arxiv.org/abs/2512.02660)
- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992)
- [AGREE: Attention Grounded Enhancement for VDR](https://arxiv.org/abs/2511.13415)
- [ReAlign: Reasoning-Guided Fine-Grained Alignment](https://arxiv.org/abs/2604.07419)
- [Groma: Localized Visual Tokenization](https://arxiv.org/abs/2404.13013)
- [GAR: Grasp Any Region](https://arxiv.org/abs/2510.18876)
- [SEAL: Structure and Element Aware Learning](https://arxiv.org/abs/2508.20778)
- [Multi-Granularity Retrieval Framework](https://arxiv.org/abs/2505.01457)
- [MMDocIR Benchmark](https://arxiv.org/abs/2501.08828)
- [BBox-DocVQA](https://arxiv.org/abs/2511.15090)
- [Reproducibility and Insights into VDR](https://arxiv.org/abs/2505.07730)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have comprehensive research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Nemotron ColEmbed V2] (arXiv 2602.03992, Feb 2026): 当前 ViDoRe V3 SOTA，8B 模型达 63.42 NDCG@10。同 backbone (Qwen3-VL) 为 DiffRegion-VDR 提供直接可比基线。
- [ColPali] (ICLR 2025): 确立了 late-interaction 视觉文档检索范式，每页 ~1030 patch embeddings，是整个领域的基础。
- [ColParse / Beyond the Grid] (arXiv 2603.01666, Mar 2026): 利用外部文档解析器生成 layout-informed sub-image embeddings，存储量减少 95%+，但 region 完全依赖解析器、不可学习。
- [RegionRAG] (AAAI 2026): 将检索从 document-level 转向 region-level，但使用固定外部检测器生成 proposals，proposals 无法适配检索目标。
- [Multi-Granularity Framework] (arXiv 2505.01457): 训练无关的多模型融合 (ColQwen2 + GME + VLM + RRF)，MMDocIR layout-level 达 65.56，但依赖多个独立模型、无 grounding 能力。
- [AGREE] (SIGIR 2026): 利用冻结 MLLM 注意力作为 proxy 局部监督，nDCG@1 提升 12.82%，但仅优化 page-level 指标，注意力信号不对检索 loss 可微。
- [ReAlign] (SIGIR 2026, arXiv:2604.07419): VLM 蒸馏实现 fine-grained alignment，但 region 识别离线进行、无 bbox grounding 输出、质量受限于 teacher VLM。
- [Snappy] (arXiv 2512.02660): 训练无关的 patch-to-region relevance propagation，BBox-DocVQA 上 59.7% IoU@0.5，建立了 grounding 基线。
- [BBox-DocVQA] (arXiv 2511.15090): 大规模 bbox-grounded DocVQA 数据集，Qwen2.5VL-72B 仅达 35.20% mean IoU，表明当前 VLM grounding 能力不足。
- [Groma] (ECCV 2024): 在 VLM understanding 中使用 class-agnostic Deformable DETR proposals + RoI-Align 进行 localized visual tokenization，是本 proposal 架构灵感来源。
- [GAR / Grasp Any Region] (ICLR 2026): 1B 模型通过 RoI-aligned feature replay 超越 78B 模型，证明 RoI-Align over ViT features 的有效性。
- [SEAL] (EMNLP 2025): structure-aware masked element alignment 在文本文档检索中 NDCG@10 +3.88，element-level 对齐的灵感来源。
- [MMDocIR] (arXiv 2501.08828): 定义了 page-level 和 layout-level 两级检索任务，173K bootstrapped + 1,685 expert-annotated pairs。

- 调研总结: Visual document retrieval 正从 page-level 向 sub-page/layout-level 演进，但现有方法均使用 task-agnostic 的 region 定义（外部解析器、固定检测器、VLM 离线推理）。将可微 region proposals 置于检索梯度流内是一个尚未被探索的结构性空白。该 proposal 精准定位了这一空白，且相关技术组件（Deformable DETR + RoI-Align on ViT）已在 VLM understanding 中被验证（Groma, GAR），但从未应用于检索。

【整体印象】: 
作为审稿人，我的第一反应是 **lean accept**。这篇 proposal 展现了对领域格局极为深入的理解，核心 insight 清晰且有结构性新颖度——不是在已有范式上微调，而是提出了一种全新的结构设计，将 region proposal generation 纳入检索梯度流。proposal 对与 5+ 并发工作的差异化分析令人信服，每个对比都精确到梯度是否可微这一结构性判据。实验设计非常完备，包含 pipeline oracle baseline、核心假设验证实验和充分的 ablation。主要顾虑在于：(1) 架构复杂度高，三路 loss 训练稳定性存疑；(2) 核心假设（retrieval-optimal regions 显著偏离 layout 类别）可能只有温和的验证结果。

【核心贡献】: 
首个将可微 region proposal generation（Deformable DETR decoder + RoI-Align）置于 VDR 检索梯度流内部的端到端模型。这意味着检索目标不仅决定如何匹配 region 与 query，还决定应该 propose 哪些 region。这是相对于所有现有方法（AGREE 的冻结注意力、ReAlign 的离线 VLM、ColParse 的外部解析器、RegionRAG 的固定检测器）的结构性区分，而非增量改进。附带贡献包括：单模型内统一 page/region/element 三粒度检索 + 零额外成本的空间 grounding。

对领域的价值：**较高**。如果实验证实端到端学习确实优于 pipeline 方法，这将为 sub-page VDR 确立新范式。即使改进幅度温和，将检测社区的成熟技术（Deformable DETR）引入检索社区也具有 bridge 价值。

【方法合理性】: 
方法整体合理，各组件选择都有明确依据：
- Deformable DETR 作为 region proposer：已在 Groma (ECCV 2024) 和 GAR (ICLR 2026) 中验证其在 ViT 特征上的有效性
- RoI-Align 提供可微梯度路径：标准操作
- DeepStack 多分辨率构造：利用 Qwen3-VL 中间层输出，为 Deformable DETR 的多尺度注意力提供真正的分辨率金字塔
- 两阶段训练（DocLayNet 预训练 → 联合微调）：合理的 curriculum，先建立空间先验再端到端优化
- 三路 loss（page InfoNCE + element contrastive + IoU grounding）：每个 loss 对应明确的训练信号

**更简单的替代方案**：最直接的简化是 pipeline 方案（DocLayout-YOLO → ColQwen2.5 region embedding），proposal 中已将其作为 "Pipeline oracle" baseline 纳入对比。这恰恰是方法论争论的核心——proposal 的论点是端到端优于 pipeline，且 ablation 设计可验证此论点。另一个替代是 AGREE 式的注意力 proxy，但其结构性局限（不对检索 loss 可微）已被充分论证。

**潜在问题**：三路 loss 的平衡（GradNorm/uncertainty weighting）增加了超参搜索空间和训练不稳定风险。batch size 1-4 per A100 可能限制 in-batch negatives 的有效性。

【5 维度打分】:
  1. 研究问题: 【强】— 问题定义精准，定位在 page-level → sub-page retrieval 的明确 gap 上，有 MMDocIR、BBox-DocVQA 等多个 benchmark 量化佐证（Snappy 59.7% IoU@0.5, VLMs 0.089 F1 vs 0.60 human F1）。Sub-page retrieval 正处于快速演进期（2025-2026 涌现 5+ 并发工作），问题的时效性和重要性毋庸置疑。

  2. 方法与创新: 【强】— 核心创新点（可微 region proposals in retrieval gradient flow）具有结构性新颖度，不是对现有方法的增量改进。与 Groma (ECCV 2024) 和 GAR (ICLR 2026) 的关系是跨领域迁移（detection/understanding → retrieval），而非简单复用。与 AGREE (SIGIR 2026)、ReAlign (SIGIR 2026)、ColParse (arXiv 2026)、RegionRAG (AAAI 2026) 的差异化论证清晰且有说服力。架构选择有充分技术依据。唯一扣分点：核心假设（retrieval-optimal regions 系统性偏离 layout 类别）仍需实验验证，存在假设不成立的风险。

  3. 实验设计: 【强】— 这是 proposal 最突出的亮点之一。4 组 baseline 覆盖所有现有范式（page-level, layout-level, grounding, pipeline oracle）；8 个 ablation 逐步验证各组件贡献；核心假设验证实验（Proposal Divergence Analysis）直接测试 IoU 重叠度和检索性能对比；效率分析含 Pareto frontier；统计报告含 3 runs with mean±std。相比 MMDocIR (arXiv 2505.01457) 的训练无关多模型融合和 AGREE 的单一 page-level nDCG 优化，本 proposal 的评估方案显著更全面。

  4. 可行性: 【中】— 计算需求合理但偏高（4-8× A100-80GB）；训练数据可获取（DocLayNet 80K, MMDocIR annotations, BBox-DocVQA 30K+ pairs）。主要风险：(a) 三路 loss 优化的稳定性——GradNorm 在多任务学习中有效但增加调参复杂度；(b) batch size 受限（1-4 per A100-80GB）可能影响 contrastive learning 效果，需要 gradient accumulation 弥补；(c) DeepStack 多分辨率构造需 pilot validation（proposal 已承认）；(d) 整体工程复杂度高，从零实现到产出结果的周期较长。

  5. 写作与呈现: 【强】— Proposal 结构清晰，逻辑链条完整。从问题定义 → 关键 insight → 与现有工作的精确差异化 → 方法设计 → 实验设计 → 可行性分析，每一步都有量化依据。对失败情形的预案（"If divergence is minimal..."）体现了成熟的研究思维。术语使用准确，引用详实。

【概率估计】: [33% - 47%] 中位 40%

【估计理由】: 
这份 proposal 在问题定义、方法创新和实验设计三个维度均表现出色，显著超过 AAAI 投稿的平均水平。核心贡献——将可微 region proposals 置于检索梯度流内——具有结构性新颖度，且与 5+ 并发工作的差异化论证令人信服。实验设计的完备性（pipeline oracle baseline、核心假设验证、8 个 ablation）本身就是显著加分项。

向上拉动因素：(1) 跨社区桥接价值（detection ↔ retrieval）在 AAAI 这样的综合会议上尤其受欢迎；(2) 问题时效性强，sub-page VDR 是 2025-2026 热点方向；(3) 实验设计质量在 proposal 阶段就已超过许多已发表论文。

向下拉动因素：(1) 架构复杂度高（Deformable DETR + RoI-Align + 三路 loss + 多分辨率特征），实验执行难度大，结果可能不如预期；(2) 核心假设（proposal 显著偏离 layout 类别）可能仅获温和验证，削弱 narrative；(3) 无任何初步结果，纯 proposal 状态增加不确定性；(4) 训练稳定性风险（三路 loss 平衡、小 batch size contrastive learning）；(5) 领域竞争激烈，AAAI 截稿前可能出现新的强竞争者。

中位 40% 反映了这是一篇质量上乘的 proposal，但从 proposal 到强结果之间存在非平凡的执行风险。如果实验结果清晰支持端到端优于 pipeline 的论点且核心假设获得验证，概率可上探 47%+；如果结果仅有温和改进或训练不稳定，可能下滑至 33% 附近。

【主要风险】: 
1. **执行复杂度风险**：架构包含过多耦合组件（Deformable DETR decoder + RoI-Align + 三路 loss + 多分辨率特征金字塔 + LoRA + gradient checkpointing），任何环节的工程问题都可能导致整体效果不达预期。三路 loss 的平衡尤其棘手——如果 loss weight 敏感性高，可能需要大量超参搜索，消耗本就紧张的 GPU 预算。
2. **核心假设温和验证风险**：如果端到端学习的 proposals 与 DocLayNet layout categories 的 IoU 偏离不大（比如 >0.7），那么核心 narrative（"检索发现了 layout taxonomy 无法捕获的空间结构"）将被显著削弱。虽然 proposal 准备了 fallback 论点（zero-marginal-cost grounding + 无 pipeline 误差传播），但审稿人可能认为这不足以支撑一篇顶会论文的核心贡献。

【实施评估】:
  - 计算资源: 4-8× A100-80GB，两阶段训练（DocLayNet 预训练 + 联合微调），需 gradient checkpointing 和 gradient accumulation。保守估计总训练时间 1-2 周（含超参搜索）。
  - 数据需求: DocLayNet (80K pages, 公开), MMDocIR (173K bootstrapped + 1,685 expert, 公开), BBox-DocVQA (30K+ auto-generated pairs, 公开), Nemotron V2 训练数据对齐（部分可能需要复现/近似）。数据均可获取，无 blocking 问题。
  - 人工介入: 中等。需要工程实现 Deformable DETR → Qwen3-VL 的集成、多分辨率特征构造的 pilot validation、三路 loss 平衡调优。不需要人工标注。
  - 训练需求: 必须训练。两阶段：(1) Deformable DETR decoder 在 DocLayNet 上预训练；(2) 全模型联合微调（LoRA on ViT backbone + 全量 DDETR decoder）。
  - 新 Benchmark: 不需要。使用已有 benchmark（ViDoRe V3, MMDocIR, BBox-DocVQA）。
  - 预估周期: 从零开始到论文完成约 3-4 个月。架构实现 + pilot validation ~3-4 周；训练 + 超参搜索 ~2-3 周；全量实验 + ablation ~2-3 周；论文写作 ~2-3 周。时间紧凑但可行（距 AAAI 2026 deadline 尚有时间）。
```

Sources:
- [Nemotron ColEmbed V2](https://arxiv.org/abs/2602.03992)
- [ColPali](https://arxiv.org/abs/2407.01449)
- [ColParse / Beyond the Grid](https://arxiv.org/abs/2603.01666)
- [RegionRAG](https://arxiv.org/pdf/2510.27261)
- [Multi-Granularity Framework](https://arxiv.org/abs/2505.01457)
- [AGREE](https://arxiv.org/abs/2511.13415)
- [ReAlign (GitHub)](https://github.com/NEUIR/ReAlign)
- [Snappy](https://arxiv.org/abs/2512.02660)
- [BBox-DocVQA](https://arxiv.org/abs/2511.15090)
- [Groma](https://arxiv.org/abs/2404.13013)
- [GAR / Grasp Any Region](https://openreview.net/pdf?id=Gp9lGS9GfY)
- [SEAL](https://arxiv.org/abs/2508.20778)
- [MMDocIR](https://arxiv.org/abs/2501.08828)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to evaluate this proposal thoroughly. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- ColPali (ICLR 2025): 奠基性工作，确立了视觉文档检索中late-interaction多向量范式。本proposal在此基础上向sub-page粒度扩展。
- Nemotron ColEmbed V2 (arXiv 2602.03992, Feb 2026): 当前ViDoRe V3 SOTA (63.42 NDCG@10, Qwen3-VL-8B)。Proposal以其4B版本为同backbone对比基准，定位合理。
- RegionRAG (AAAI 2026): 区域级RAG，使用外部检测器产生固定proposal，不可随检索目标调整。Proposal核心novelty（可微分proposal在检索梯度流内）直接针对此局限。
- ColParse / Beyond the Grid (arXiv 2603.01666, Mar 2026): 利用文档解析器产生layout子图做紧凑多向量表示，存储降低95%但区域与任务无关。与proposal的pipeline baseline设计直接对应。
- AGREE (SIGIR 2026, arXiv 2511.13415): 利用MLLM attention作为空间监督代理，+12.82% nDCG@1，但仅优化页级指标，attention信号对检索loss不可微。Proposal正确识别了这一结构性限制。
- ReAlign (SIGIR 2026, arXiv 2604.07419): VLM推理驱动的细粒度对齐，离线区域识别，无bbox输出。Proposal的端到端学习方式与之形成互补/竞争关系。
- Multi-Granularity Framework (arXiv 2505.01457): 多模型融合(ColQwen2+GME+VLM+RRF)达65.56 MMDocIR layout-level，但需多模型且无grounding。
- Snappy (arXiv 2512.02660): 训练无关的patch-to-region相似度传播，59.7% IoU@0.5。设定了grounding的baseline水平。
- SEAL (EMNLP 2025): 文本检索中结构感知+masked element alignment，+3.88 NDCG@10。Proposal的element-level contrastive loss直接借鉴此思路，属于合理的跨领域迁移。
- Groma (ECCV 2024): 类无关Deformable DETR proposal用于MLLM的localized visual tokenization。Proposal的架构设计直接参考此工作。
- GAR / Grasp Any Region (ICLR 2026): RoI-Align over ViT features用于区域级视觉理解，1B模型超越78B。证明了RoI-Align+ViT的可行性，是proposal的关键技术先例。
- BBox-DocVQA (arXiv 2511.15090): 空间grounding benchmark，30K+ QA pairs with bbox。Proposal用作IoU grounding loss的监督数据和评测集。
- DocLayNet: 80K页面、11类layout标注，用作proposal预训练数据。

- 调研总结: 视觉文档检索正从页级向sub-page粒度快速演进，但现有方法均使用task-agnostic的区域定义（layout类别、OCR框、parser输出、VLM识别区域）。将可微分区域proposal置于检索梯度流内是一个尚未被探索的结构性空白，proposal精准定位了这一gap。该领域2025-2026年论文密集（AGREE、ReAlign、ColParse、RegionRAG均为2026年发表），竞争激烈但证明了方向的时效性。

【整体印象】:
作为审稿人，我的第一反应是积极的——这是一篇有明确结构性创新的proposal。它不是在现有框架上做incremental改进，而是提出了一个新的架构范式：将区域proposal生成嵌入检索梯度流。对现有工作的分析非常清晰，每个competing work的结构性局限都被准确识别。实验设计的完备程度远超一般proposal。总体倾向weak accept到accept之间。

主要顾虑：(1) 架构复杂度较高，如果实验收益不够显著会被质疑 "over-engineered"；(2) 核心假设（learned proposals会系统性偏离layout类别）如果不成立，narrative会弱化（虽然proposal有graceful degradation论述）；(3) 多源监督（DocLayNet + MMDocIR + BBox-DocVQA + retrieval pairs）的组合是否引入了不公平优势需要careful discussion。

【核心贡献】:
核心贡献是**首次将可微分区域proposal置于视觉文档检索的梯度流中**，使检索目标不仅决定"如何匹配区域与查询"，更决定"提出哪些区域"。这是一个结构性区分（structural distinction），而非参数/训练技巧的改进。附带贡献包括：单模型同时产出page/region/element三粒度检索embedding + 零边际成本的空间grounding。

对领域的价值：中高。它为sub-page视觉文档检索提出了一条新路径（从task-agnostic regions到retrieval-optimal regions），如果实验验证假设成立，将重新定义该子领域的研究方向。即便假设仅部分成立，端到端统一框架本身也有工程和学术价值。

【方法合理性】:
方法在技术上是合理且有据可循的：
- Deformable DETR作为proposal生成器已在检测和VLM理解中广泛验证（Groma ECCV 2024, GAR ICLR 2026）
- RoI-Align的可微性保证了梯度可以从检索loss传回proposal decoder，这是核心技术可行性的基础
- 多分辨率特征金字塔构建（DeepStack中间层 → 不同步长空间池化）是Deformable DETR多尺度注意力的标准做法
- 三段式loss（page InfoNCE + element contrastive + IoU grounding）的设计有各自独立的motivation
- 两阶段训练（proposal预训练 → 联合微调）是合理的warm-start策略

**更简单的替代方案**：最直接的替代是pipeline方案（DocLayout-YOLO → ColQwen region embedding），proposal已将其作为pipeline oracle baseline纳入。另一个替代是在AGREE/ReAlign基础上改进，但这些方法的结构性限制（attention/VLM作为代理而非端到端）已被清晰论述。我认为proposal对"为什么需要端到端"的论证是充分的，但最终需要实验数据证明end-to-end优于pipeline的具体幅度。

【5 维度打分】:
  1. 研究问题: 【强】 — 视觉文档检索从页级到sub-page粒度的演进是领域当前最活跃的研究方向（2025-2026年密集产出AGREE、ReAlign、ColParse、RegionRAG等多篇论文）。现有方法均使用task-agnostic区域定义这一观察是准确的，"检索最优区域可能偏离预定义layout类别"这一假设有理论吸引力且可实证检验。问题的重要性和时效性毋庸置疑。

  2. 方法与创新: 【强】 — 核心创新点（可微分region proposal在检索梯度流内）是一个genuine structural novelty，不是对现有方法的incremental改进。与所有6个directly competing works（AGREE、ReAlign、ColParse、RegionRAG、Multi-Gran Framework、Snappy）的结构性差异已被清晰阐述。技术组件（Deformable DETR + RoI-Align + late interaction）各自成熟可靠，但组合方式新颖。从检测/VLM理解社区（Groma ECCV 2024, GAR ICLR 2026）到检索社区的技术迁移是合理且timely的。轻微扣分：架构复杂度较高，如果最终gains modest，"Occam's razor" argument可能被reviewer提出。

  3. 实验设计: 【强】 — 这是proposal最突出的亮点之一。4类benchmark（ViDoRe V3, MMDocIR, BBox-DocVQA, ViDoRe V3 grounding）覆盖page-level、layout-level和spatial grounding。4组baseline（page-level、layout-level、grounding、pipeline oracle）非常完备，特别是pipeline oracle baseline直接回应了"为什么不用pipeline"的reviewer质疑。8项ablation study设计精细，逐步叠加components可清晰展示各组件贡献。核心假设验证分析（proposal divergence from layout categories）是加分项。效率分析和统计报告（3 runs, mean±std）体现了严谨性。实验标准与该领域顶会论文（如Nemotron ColEmbed V2的评测设置）对齐。

  4. 可行性: 【中】 — 技术路线每一步都有先例可循（Deformable DETR、RoI-Align、DocLayNet预训练等），但系统集成的复杂度不低。训练需要4-8× A100-80GB，是substantial但可获取的资源。多源数据依赖（DocLayNet + MMDocIR + BBox-DocVQA + retrieval pairs）增加了数据准备的工作量。批大小1-4 per GPU可能限制in-batch negatives的效果，需要gradient accumulation，增加训练不稳定性风险。DeepStack多分辨率构建的pilot验证是必要的前置步骤。总体：对有经验的团队可行，但执行风险中等。

  5. 写作与呈现: 【强】 — Proposal的组织结构非常清晰：问题→洞察→landscape→方法→实验。对每个competing work的分析精准且公平，不过度贬低也不回避比较。核心假设的formulation清晰且有fallback plan。技术细节（如三粒度的precise定义、loss公式的设计动机）充分但不冗余。对可行性的坦诚讨论（如内存估算标注"pending pilot profiling"）增加了可信度。

【概率估计】: [35% - 48%] 中位 40%

【估计理由】:
这是一篇novelty清晰、实验设计完备、定位精准的proposal，在方法创新和实验计划方面表现出色。给出35-48%而非更高的原因：

(1) **执行风险**：这仍是一个proposal而非completed paper——核心假设（proposal divergence）需要实验验证，端到端训练的收益幅度未知。如果gains modest（如仅2-3 points on benchmarks），reviewer可能认为复杂度不值得。

(2) **领域竞争激烈**：2025-2026年该领域产出密集（AGREE、ReAlign、ColParse、RegionRAG、Nemotron V2等），投稿时可能面临更多concurrent/新出现的competing works。

(3) **Reviewers' complexity concern**：三源监督 + 两阶段训练 + 三粒度输出的系统可能被部分reviewer视为over-engineered，特别是如果ColParse这类简洁方法能达到comparable结果。

(4) **AAAI审稿variance**：AAAI审稿有较大variance，遇到不熟悉VDR sub-field的reviewer可能低估贡献。

上限48%的理由：如果实验结果显著优于pipeline oracle且假设验证成功，加上excellent实验设计，可以达到strong accept territory。下限35%的理由：如果gains marginal或某些组件ablation表现不佳，但novelty claim仍成立。

【主要风险】:
1. **收益幅度不确定性**：端到端可微分proposal相比简单pipeline（如DocLayout-YOLO + ColQwen）的性能提升可能不足以justify架构复杂度。如果improvement < 3-5 points，reviewer很可能以"complexity不值得"为由给borderline reject。这是最核心的风险。
2. **核心假设可能不成立**：learned proposals可能并不显著偏离DocLayNet layout categories（即layout taxonomy已足够覆盖retrieval-optimal regions）。虽然proposal有graceful degradation论述（零边际成本grounding + 消除pipeline error propagation），但这会使narrative从"发现新的retrieval-specific spatial structures"弱化为"更便捷的端到端pipeline"，contribution weight下降。

【实施评估】:
  - 计算资源: 4-8× A100-80GB GPU（训练），估计训练周期2-4周（含pilot验证）。推理时需要支持Deformable DETR forward pass，但overhead相对可控（~16-40M额外参数）。
  - 数据需求: DocLayNet (80K页面, 公开可用) + MMDocIR annotations (~173K bootstrapped + ~1,685 expert) + BBox-DocVQA (30K+ QA pairs with bbox) + 标准检索query-page pairs。所有数据集均为公开可用，但多数据源的准备和对齐需要工程工作量。
  - 人工介入: 中等。主要在数据预处理、多分辨率特征金字塔pilot验证、loss weight调参阶段需要人工判断和迭代。
  - 训练需求: 两阶段训练——(1) Deformable DETR decoder在DocLayNet上预训练（估计1-2天on 4 GPUs）; (2) 联合微调三路loss（估计1-2周含超参搜索和多次run）。需要GradNorm/uncertainty weighting调试。
  - 新 Benchmark: 不需要。所有评测benchmark（ViDoRe V3, MMDocIR, BBox-DocVQA）已有现成。
  - 预估周期: 从proposal到可投稿paper约10-14周（含2周pilot验证 + 3-4周主实验 + 2周ablation和分析 + 2-3周写作和修改 + buffer）。如果pilot阶段遇到内存或训练不稳定问题，可能延长2-4周。
```

Sources:
- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449)
- [Nemotron ColEmbed V2](https://arxiv.org/html/2602.03992v1)
- [RegionRAG: Region-level Retrieval-Augmented Generation](https://arxiv.org/abs/2510.27261)
- [Beyond the Grid / ColParse](https://arxiv.org/abs/2603.01666)
- [AGREE: Attention Grounded Enhancement for VDR](https://arxiv.org/abs/2511.13415)
- [ReAlign: Reasoning-Guided Fine-Grained Alignment](https://arxiv.org/abs/2604.07419)
- [Snappy: Spatially-Grounded Document Retrieval](https://arxiv.org/pdf/2512.02660)
- [BBox-DocVQA](https://arxiv.org/abs/2511.15090)
- [SEAL: Structure and Element Aware Learning](https://arxiv.org/abs/2508.20778)
- [Groma: Localized Visual Tokenization](https://arxiv.org/abs/2404.13013)
- [GAR: Grasp Any Region](https://openreview.net/pdf?id=Gp9lGS9GfY)
- [A Multi-Granularity Retrieval Framework](https://arxiv.org/pdf/2505.01457)
- [ViDoRe Benchmark](https://github.com/illuin-tech/vidore-benchmark)


【原始 proposal（允许参考但不是主要依据）】:
# End-to-End Multi-Granularity Visual Document Retrieval via Differentiable Region Proposals

## Core Problem

Visual document retrieval (VDR) models operate at page granularity, leaving a ~32pp gap to layout-level retrieval (MMDocIR) and limited spatial grounding (Snappy achieves 59.7% IoU@0.5 without training, arXiv 2512.02660; BBox-DocVQA shows Qwen2.5VL-72B reaches only 35.20% mean IoU, arXiv 2511.15090). Existing sub-page approaches rely on external parsers (ColParse, arXiv 2026), task-agnostic fixed region proposals (RegionRAG, AAAI 2026), multi-model fusion pipelines (Multi-Granularity Framework, arXiv 2505.01457, reaching 65.56 on MMDocIR layout-level), proxy supervision that optimizes only page-level metrics (AGREE, SIGIR 2026), or VLM distillation for fine-grained alignment without spatial grounding output (ReAlign, SIGIR 2026, arXiv:2604.07419). No single model produces retrieval embeddings at page, region, and element granularities with learned spatial grounding.

## Key Insight: Region Proposals Inside the Retrieval Gradient Flow

Post-hoc analysis reveals that ViT patch embeddings already encode spatial neighborhood information (SIGIR 2025 reproducibility study), and inference-time methods can partially recover it (Snappy's 59.7% IoU@0.5, AGREE's attention proxy with +12.82% nDCG@1). But because no existing model places region proposal generation within the retrieval gradient flow, spatial structure recovery has an inherent ceiling.

DiffRegion-VDR is the first VDR model where retrieval loss gradients directly modify region proposal positions and sizes through differentiable RoI-Align. This is a structural distinction from all existing approaches: AGREE's spatial signal comes from a frozen MLLM's attention (not differentiable w.r.t. retrieval loss); ReAlign's comes from offline VLM reasoning (not part of the forward-backward pass); ColParse's regions are from an external parser (no gradient connection); RegionRAG's proposals are from a fixed detector (trained separately). Only in DiffRegion-VDR does the retrieval objective determine not just how to match regions to queries, but which regions to propose.

**Core hypothesis**: Joint fine-tuning will cause proposals to diverge systematically from DocLayNet layout categories — the model will discover retrieval-specific spatial structures that no predefined layout taxonomy captures. This represents the evolution of structured retrieval embeddings from grid-structured (ColBERT token-level → ColPali patch-level) to content-structured (learned semantic regions).

## Research Landscape and Differentiation

**Page-level VDR** is maturing: Nemotron ColEmbed V2 (arXiv 2602.03992) achieves 63.42 NDCG@10 on ViDoRe V3 with Qwen3-VL-8B. ColPali (ICLR 2025) established late-interaction visual retrieval.

**Sub-page retrieval** is fragmented across four paradigms, each structurally limited:
- *External parser pipeline*: ColParse (arXiv 2026) segments pages via document parsers, reducing storage by 95%, but regions are task-agnostic and inherit parser errors.
- *Fixed-proposal training*: RegionRAG (AAAI 2026) trains region-level alignment on fixed proposals from external detectors; proposals cannot adapt to retrieval objectives.
- *Training-free fusion*: Multi-Granularity Framework (arXiv 2505.01457) combines ColQwen2+GME+VLM+RRF for 65.56 on MMDocIR layout-level, but requires multiple models and lacks grounding.
- *VLM distillation*: ReAlign (SIGIR 2026, arXiv:2604.07419) uses superior VLMs to identify query-related regions and generate query-aware descriptions as supervision. Fine-grained alignment is learned, but: (a) quality is upper-bounded by teacher VLM's grounding ability; (b) no bounding-box grounding output; (c) region identification is offline during training, not dynamic at inference.

**Grounding** is limited: Snappy (arXiv 2512.02660) maps patch similarity to OCR regions at inference (59.7% IoU@0.5 on BBox-DocVQA); AGREE (SIGIR 2026) uses MLLM attention as proxy but optimizes page-level nDCG only. ViDoRe V3 VLMs achieve 0.089 F1 on bbox localization vs. 0.60 human F1.

**The gap**: All sub-page methods use task-agnostic region definitions (layout categories, OCR boxes, parser outputs, VLM-identified regions). The optimal retrieval region for a given query may not align with predefined layout classes. Hypothesis: retrieval-optimal regions exhibit systematic geometric divergence from standard layout categories. Even if this divergence is modest, end-to-end learning provides zero-marginal-cost grounding and eliminates pipeline error propagation.

**Detection–retrieval community gap**: Differentiable region proposals via Deformable DETR are proven in VLM understanding — Groma (ECCV 2024) uses class-agnostic proposals for localized visual tokenization; GAR (ICLR 2026) applies RoI-Align over ViT features to outperform 78B models with 1B parameters. Element-level alignment is proven for text retrieval — SEAL (EMNLP 2025) achieves +3.88 NDCG@10 via structure-aware masked element alignment. Neither technique has been applied to visual document retrieval.

## Proposed Approach

**Architecture.** Attach a lightweight class-agnostic Deformable DETR decoder to Qwen3-VL-4B's ViT feature maps. To provide genuine multi-resolution input for Deformable DETR's multi-scale deformable attention, apply different-stride 2D spatial pooling to the 4 DeepStack intermediate outputs (layers sharing the same spatial resolution but differing in semantic abstraction), constructing a resolution pyramid analogous to Groma's neighbor-patch concatenation strategy on DINOv2. RoI-Align extracts context-aware region embeddings from proposed regions. Multi-granularity late-interaction scoring operates at three levels within a single forward pass.

**Three granularity levels** (precise definitions):
- *Page-level*: All ViT patch token embeddings participate in late interaction with query tokens (standard ColPali-style).
- *Region-level*: Deformable DETR top-K learned proposals → RoI-Align → region embeddings for late interaction. These are the model's primary sub-page retrieval units, dynamically generated per document.
- *Element-level*: During training, region proposals matched (by IoU) to MMDocIR layout annotations serve as supervised targets for element-level contrastive alignment. At inference, region proposals naturally approximate element-level retrieval without ground-truth layout information.

**Training.** Two-stage:
1. *Proposer pre-training*: Train the Deformable DETR decoder on DocLayNet (80K annotated pages, 11 layout classes) for class-agnostic region proposal generation, establishing spatial priors.
2. *Joint fine-tuning* with three losses:
   - (a) Page-level InfoNCE: global retrieval on query-page pairs (training data aligned with Nemotron ColEmbed V2 recipe where possible for fair comparison; differences documented).
   - (b) Element-level contrastive alignment (inspired by SEAL, EMNLP 2025): on MMDocIR layout annotations (~173K bootstrapped + ~1,685 expert-annotated pairs; ablation on bootstrapped vs. expert-only).
   - (c) IoU grounding loss: spatial localization supervised by BBox-DocVQA training split (30K+ auto-generated QA pairs with bbox, arXiv:2511.15090) + DocLayNet layout boxes as supplement.
   - Loss balancing via GradNorm or uncertainty weighting. Retrieval losses backpropagate through RoI-Align into the proposal decoder, enabling proposals to evolve from layout-generic to retrieval-optimal.

**Why end-to-end beats pipeline** (addressing the trivial alternative): (1) Pipeline regions are task-agnostic — parser/detector categories cannot adapt to retrieval needs; learned proposals can, and our core hypothesis predicts they will diverge. (2) Pipeline requires multiple independent models, preventing joint optimization. (3) Pipeline methods produce zero grounding output; DiffRegion-VDR provides bounding boxes at zero marginal cost.

## Experimental Design

### Benchmarks
- **ViDoRe V3**: Page-level retrieval — NDCG@5, NDCG@10 (per-dataset breakdown by document type)
- **MMDocIR**: Page-level Recall@1/3/5; Layout-level Recall@1/3/5
- **BBox-DocVQA** (primary grounding, arXiv:2511.15090): IoU@0.25, IoU@0.5, IoU@0.7, mean IoU
- **ViDoRe V3 grounding** (supplementary): F1@IoU=0.5

### Baselines (4 groups)
- **Page-level**: ColPali v1.3 (ICLR 2025), ColQwen2.5-v0.2, Nemotron ColEmbed V2-4B (same backbone, arXiv 2602.03992), Nemotron ColEmbed V2-8B
- **Layout-level**: ColParse (arXiv 2026), Multi-Granularity Framework (arXiv 2505.01457), RegionRAG (AAAI 2026)
- **Grounding**: Snappy (arXiv 2512.02660, training-free), AGREE (SIGIR 2026)
- **Pipeline oracle**: DocLayout-YOLO → ColQwen2.5 region embedding → late interaction (same backbone, external detector)

### Ablation Studies
1. Qwen3-VL-4B + page-level InfoNCE only (≈Nemotron V2-4B training recipe)
2. \+ Deformable DETR decoder + RoI-Align, page-level loss only
3. \+ Element-level contrastive alignment loss
4. \+ IoU grounding loss (full model)
5. Two-stage (DocLayNet pre-train → joint fine-tune) vs. end-to-end from scratch
6. Loss weight sensitivity (3–5 ratio configurations, each 2+ runs)
7. Proposal count: top-K ∈ {50, 100, 200, 300}
8. Multi-level feature utilization: (a) DDETR on final ViT layer only; (b) DDETR on 4 DeepStack levels, same resolution; (c) DDETR on 4 DeepStack levels with spatial pooling (multi-resolution)

### Core Hypothesis Validation: Proposal Divergence Analysis
- Measure IoU overlap between learned proposals (after stage 2) and DocLayNet ground-truth layout annotations → quantify geometric divergence
- Compare retrieval performance of learned proposals vs. DocLayNet-category proposals (used as fixed regions in a pipeline)
- Visualize proposal distributions across document types: which retrieval-specific structures emerge that layout taxonomy misses?
- If divergence is minimal: the contribution is still valid via zero-marginal-cost grounding + pipeline error elimination; explicitly discuss

### Region Proposer Analysis
- Class-agnostic proposal recall@50/100/300 on DocLayNet test set
- Proposal quality change after joint fine-tuning — does retrieval loss improve or degrade detection recall?
- Visualization across document types (papers, slides, invoices, infographics)

### Efficiency Analysis
- Parameter overhead: DDETR decoder ~16–40M params on Qwen3-VL-4B (4.44B); report exact count and percentage
- Vectors/page: page + region + element tokens vs. ColPali (~1030/page) vs. ColParse (<10/page)
- Query latency (ms/query) and index storage (MB/1K pages)
- Performance vs. storage and performance vs. latency Pareto frontier

### Statistical Reporting
- Main results: 3 independent runs, report mean ± std
- Ablation: at minimum full model and page-only baseline with 3 runs; others single-run with notation

### Feasibility
- Multi-resolution construction: 4 DeepStack levels → 2D reshape → stride-{1,2,4,8} spatial pooling → multi-resolution pyramid for Deformable DETR. Pilot validation on DocLayNet detection AP.
- Training memory: Qwen3-VL-4B FP16 ~9GB + DDETR decoder + RoI-Align regions + three-way late interaction. Conservative estimate: batch size 1–4 per A100-80GB (pending pilot profiling). Memory optimizations: top-K proposals only for retrieval loss (remainder for detection pre-training only), LoRA on backbone ViT, gradient checkpointing, gradient accumulation with in-batch negatives. Target: 4–8× A100-80GB.
- OOD generalization: per-dataset analysis on ViDoRe V3 document types absent from DocLayNet (slides, web screenshots, infographics).

## Key References

- Groma: Localized Visual Tokenization for Grounding MLLMs (ECCV 2024)
- Grasp Any Region (GAR): Contextual Pixel Understanding for MLLMs (ICLR 2026)
- SEAL: Structure and Element Aware Learning for Document Retrieval (EMNLP 2025)
- ColPali: Efficient Document Retrieval with Vision Language Models (ICLR 2025)
- MMDocIR: Benchmarking Multimodal Retrieval for Long Documents (arXiv 2025)
- AGREE: Attention Grounded Enhancement for VDR (SIGIR 2026)
- ReAlign: Optimizing VDR with Reasoning-Guided Fine-Grained Alignment (SIGIR 2026, arXiv:2604.07419)
- RegionRAG: Region-level RAG for Visual Document Understanding (AAAI 2026)
- Beyond the Grid / ColParse: Layout-Informed Multi-Vector Retrieval (arXiv 2026)
- Deformable DETR: Deformable Transformers for Object Detection (ICLR 2021)
- Reproducibility and Insights into VDR with Late Interaction (SIGIR 2025)
- Nemotron ColEmbed V2: Efficient Retrieval with Late Interaction (arXiv 2602.03992, Feb 2026)
- A Multi-Granularity Multimodal Retrieval Framework (arXiv 2505.01457)
- Snappy: Spatially-Grounded Document Retrieval via Patch-to-Region Relevance Propagation (arXiv 2512.02660)
- BBox-DocVQA: Bounding-Box Grounded Document VQA (arXiv:2511.15090)
- DocLayNet: A Large-scale Dataset for Document Layout Segmentation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "66c0f2c3-77cb-4a77-b06a-13bb36f9179e",
  "type": "user",
  "uuid": "ec274b58-aa4a-4cf7-b1af-1da85956244a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:36:02.693Z_

```json
{
  "parentUuid": "ec274b58-aa4a-4cf7-b1af-1da85956244a",
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
  "uuid": "9fe72402-07f2-46c7-9a3f-db7cd595712e",
  "timestamp": "2026-05-30T07:36:02.693Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:36:02.693Z_

```json
{
  "parentUuid": "9fe72402-07f2-46c7-9a3f-db7cd595712e",
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
  "uuid": "5894cec3-9ffc-4fcd-b315-75328c17012d",
  "timestamp": "2026-05-30T07:36:02.693Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-30T07:36:02.693Z_

```json
{
  "parentUuid": "5894cec3-9ffc-4fcd-b315-75328c17012d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "49e78772-891b-4166-b9d6-8651c64cbdf3",
  "timestamp": "2026-05-30T07:36:02.693Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive research coverage. Let me compile my…",
  "leafUuid": "49e78772-891b-4166-b9d6-8651c64cbdf3",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "End-to-end visual document retrieval with differentiable region proposals",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669"
}
```

---

### Assistant

_source line 9 · 2026-05-30T07:36:20.581Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

First, let me extract the key numbers:
- Reviewer 1: [30% - 48%] 中位 38%
- Reviewer 2: [33% - 47%] 中位 40%
- Reviewer 3: [35% - 48%] 中位 40%

三个中位数: 38%, 40%, 40%
Mean: 39.3%
Std: sqrt(((38-39.3)^2 + (40-39.3)^2 + (40-39.3)^2)/3) = sqrt((1.69 + 0.49 + 0.49)/3) = sqrt(2.67/3) = sqrt(0.89) ≈ 0.94%


The standard deviation is extremely low at under 1%, showing remarkable agreement across all three reviewers. Now I'm looking at where the reviewers align and where they diverge on specific dimensions. The research problem gets unanimous strong ratings from all three, but on methodology and innovation, Reviewer 1 is slightly more conservative with a medium-to-strong assessment while the other two both rate it as strong.

The experimental design also shows perfect consensus with all three rating it strong, and feasibility is unanimously rated as medium across the board. Writing quality receives strong marks from everyone. What's particularly striking is that despite some variation in individual dimension ratings, all three reviewers independently identify the exact same two core concerns: whether the learned proposals will actually diverge meaningfully from the layout categories, and whether the approach risks being overly complex or over-engineered. This consistency in identifying the fundamental risks is a strong signal about what matters most in evaluating this work.

Now looking at the implementation requirements, there's remarkable alignment here too—all three converge on needing 4-8 A100-80GB GPUs, using only publicly available data, a 3-4 month timeline, a two-stage training approach, no new benchmark, and medium-level human intervention. With such tight consensus across reviewers, I can confidently narrow the recommendations to the median values rather than hedging with wide ranges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e78772-891b-4166-b9d6-8651c64cbdf3",
  "isSidechain": false,
  "requestId": "req_011CbYNMcczGBqxq5HDZrkub",
  "type": "assistant",
  "uuid": "d32c24a3-fd85-4274-955a-eea5bb7c616e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6dUBspA9ZZN4TZEoyMyFb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21253,
      "cache_read_input_tokens": 16149,
      "output_tokens": 2743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2743,
          "cache_read_input_tokens": 16149,
          "cache_creation_input_tokens": 21253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21253
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

_source line 10 · 2026-05-30T07:37:09.469Z_

【阶段】: Meta Judge
【三次中位】: [38%, 40%, 40%]  std=0.94%
【共识维度】:
- 研究问题: 强（3/3 一致）— 三位审稿人均确认 sub-page VDR 是 2025-2026 最活跃前沿，"retrieval-optimal regions vs. task-agnostic regions" 的问题定义精准且有明确科学价值
- 实验设计: 强（3/3 一致）— 三位均将实验设计列为 proposal 最突出的亮点，特别提及 pipeline oracle baseline、8 项 ablation、核心假设验证实验的设计质量
- 可行性: 中（3/3 一致）— 三位均指出 4-8× A100-80GB 资源需求合理但偏高，三路 loss balancing 和训练稳定性是主要工程风险
- 写作与呈现: 强（3/3 一致）— 三位均评为上乘，文献定位精准、差异化论证清晰、科学诚实性好
- 主要风险 1: 核心假设验证风险（3/3 一致）— 三位均指出 learned proposals 可能与 layout categories 高度重合，削弱核心 narrative
- 主要风险 2: 复杂度 vs. 收益质疑（3/3 一致）— 三位均担忧架构复杂度高，若 gains modest 会被质疑 over-engineered / incremental
- 实施周期: 3-4 个月（3/3 一致）

【异常维度】:
- 方法与创新: R1 评为"中-强"，R2、R3 评为"强"。R1 更担忧"组件组合 vs. 本质创新"的 incremental 质疑，但 R2、R3 均认为核心创新（可微 region proposals in retrieval gradient flow）构成 structural novelty 而非 incremental improvement。R1 的谨慎有一定道理（确实存在部分审稿人如此认知的风险），但属于 risk factor 而非 dimension downgrade，整体判为"强-（附带 incremental 质疑风险）"更合理
- 缺少端到端 RAG/QA 评估: 仅 R1 提及，R2、R3 未提。属于 nice-to-have 而非致命缺陷，降权处理
- 多源监督公平性: 仅 R3 提及（多源数据是否引入不公平优势），R1、R2 未提。是合理 concern 但可通过实验设计（ablation on data sources）解决，降权处理

【最终概率】: [33% - 47%] 中位 39%
【一致性】: 高（std=0.94%，远低于 3% 阈值）

【综合理由】:
三位审稿人在所有核心维度上展现了罕见的高度一致性。五个评分维度中，研究问题、实验设计、写作与呈现三项获得 3/3 "强"评价；可行性获得 3/3 "中"；方法与创新 2/3 "强" + 1/3 "中-强"。两个主要风险（假设验证 + 复杂度质疑）也被三位同时独立识别。

基于高一致性原则，取中位附近并适度缩窄区间：
- **下界 33%**：取三位下界的中位（30%, 33%, 35% → 33%），对应核心假设不成立 + gains modest 的悲观情景
- **上界 47%**：取三位上界的中位（48%, 47%, 48% → 47%），对应假设验证成功 + 所有实验按计划完成的乐观情景
- **中位 39%**：三个中位（38%, 40%, 40%）的均值约 39.3%，取 39%。R1 略保守的"中-强"方法评价是合理的风险折扣（incremental 质疑确实可能出现在 1-2 位 AAAI 审稿人中），因此中位不宜高于 40%

这是一篇方向正确、novelty 清晰、实验设计达到顶会标准的 proposal，处于 "competitive but execution-dependent" 区间。概率上限受制于两个结构性风险（假设验证 + 复杂度质疑），下限有实验完备性和写作质量托底。

【建议】: 边缘（偏积极）— proposal 质量本身处于可投稿水平，概率区间跨越 36% 阈值，最终结果高度依赖实验执行。建议推进实验，优先完成 pilot validation（DeepStack 多分辨率构建 + 内存 profiling）和核心假设验证实验（proposal divergence analysis），根据初步结果决定是否全力投入。

【实施评估】:
  - 计算资源: 4-8× A100-80GB（三位一致）。DocLayNet 预训练约 1-2 天；联合训练含超参搜索约 1-2 周；全部 ablation（8 configurations × multiple seeds）保守估计 100-200 GPU-days。推理端 Deformable DETR decoder 额外 ~16-40M 参数，overhead 可控。
  - 数据需求: DocLayNet (80K pages)、MMDocIR (173K bootstrapped + 1,685 expert)、BBox-DocVQA (30K+ pairs)、page-level retrieval pairs（对齐 Nemotron V2 recipe）。全部公开可用，无 blocking 依赖。多源数据的格式对齐和预处理有一定工程工作量。
  - 人工介入: 中等（三位一致）。主要集中在：数据预处理与格式对齐、DeepStack 多分辨率构建的 pilot validation、三路 loss weight 调参迭代、proposal divergence 的定性可视化分析。无需人工标注。
  - 训练需求: 必须训练，两阶段。Stage 1: Deformable DETR decoder 在 DocLayNet 预训练（1-2 天/4 GPUs）。Stage 2: Qwen3-VL-4B 联合微调（LoRA on ViT backbone + 全量 DDETR decoder），三路 loss + GradNorm/uncertainty weighting，每次完整训练 2-5 天（4× A100）。
  - 新 Benchmark: 不需要（三位一致）。使用现有 ViDoRe V3、MMDocIR、BBox-DocVQA。
  - 预估周期: 10-16 周全职工作（三位估计的综合）。Week 1-2: pipeline 搭建 + pilot validation（DeepStack + 内存 profiling）。Week 3-4: DocLayNet 预训练 + 初步联合训练。Week 5-8: 超参搜索 + 全量 ablation studies。Week 9-11: evaluation + divergence analysis + 效率分析。Week 11-14: 论文撰写 + revision。Week 14-16: buffer（应对 pilot 阶段问题或补充实验）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d32c24a3-fd85-4274-955a-eea5bb7c616e",
  "isSidechain": false,
  "requestId": "req_011CbYNMcczGBqxq5HDZrkub",
  "type": "assistant",
  "uuid": "5950cd4f-09f3-459a-884c-1a61a9de78d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6dUBspA9ZZN4TZEoyMyFb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21253,
      "cache_read_input_tokens": 16149,
      "output_tokens": 2743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2743,
          "cache_read_input_tokens": 16149,
          "cache_creation_input_tokens": 21253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21253
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive research coverage. Let me compile my…",
  "leafUuid": "5950cd4f-09f3-459a-884c-1a61a9de78d7",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "End-to-end visual document retrieval with differentiable region proposals",
  "sessionId": "492b9128-915f-49d8-849b-1d9e07c76669"
}
```

---
