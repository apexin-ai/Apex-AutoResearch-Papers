# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/c4a69647-f298-44eb-bf56-636a42ff4e75.jsonl`
- **Structured JSON:** [`17e98eb7770d8c1761d6.json`](../../sessions/17/17e98eb7770d8c1761d6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T22:56:39.079Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T22:56:39.079Z",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nI now have comprehensive field knowledge. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv 2604.04207, Apr 2026):\n   直接支撑 proposal 的动机之一。证实推理 VLM 在 CoT 过程中对视觉 evidence 区域的 attention 丢失 >50%。但关键细节：该现象特指 *visual tokens* 的 attention 衰减，而非文本 token 的丢失。论文提出的 mitigation 是 inference-time 的 \"vision veto\"，不涉及训练或 symbolic memory。\n\n2. PRCO / Seeing with You: Perception-Reasoning Coevolution (arXiv 2603.28618, Mar 2026):\n   Proposal 的直接前序工作和主要 baseline。Observer-Solver 双角色 RL 框架，Observer 输出 NL evidence caption，Solver 基于 caption 推理，平均 +7pts。Proposal 声称 PRCO 的 NL caption 不可验证——这一判断准确，PRCO 的 Observer 奖励来自 Solver 的下游成功，不独立验证 Observer 输出的准确性。\n\n3. Geoparsing (arXiv 2604.11600, Apr 2026):\n   SFT+RLVR 训练形式化几何图解析器，GDP-29K 数据集，实现 SOTA parsing。Proposal 直接复用其训练 recipe。论文本身只做 parsing 不做持久化 memory 或 RL reasoning。\n\n4. Symbolic Grounding Reveals Representational Bottlenecks (arXiv 2604.21346, Apr 2026):\n   **关键论文**——证明将图表转为 symbolic 输入后 LLM 准确率从 near-chance 跳至 mid-90s。这既支撑了 proposal 的方向，**也构成了 trivial alternative 的威胁**：仅仅\"转换为 symbolic 再推理\"（不需要 persistent memory 或 dual RL）已能大幅弥合 gap。\n\n5. SymHPR / Hierarchical Process Reward Models are Symbolic Vision Learners (arXiv 2512.03126, Dec 2025):\n   自监督 symbolic auto-encoder，98.2% reconstruction fidelity。Proposal 复用其重建验证机制作为 Observer reward。论文本身不做 reasoning 或 RL training。\n\n6. CogFlow (ICLR 2026):\n   三阶段 perception→internalization→reasoning 框架，76.8% MathVista。使用文本 internalization（非形式化）。Proposal 正确识别了与 CogFlow 的差异点。\n\n7. MathLens / What MLLMs Learn... (arXiv 2510.01719, Oct 2025):\n   证明 integration 是主要失败模式：RL 主要提升 perception，SFT 主要提升 reasoning，但 integration 始终 lagging。Proposal 的 integration reward 直接针对此发现。\n\n8. Hilbert-Geo (arXiv 2605.16385, May 2026):\n   形式化立体几何语言 + Parse2Reason pipeline，无 RL、无 persistent memory。在 SolidFGeo2k 上 77.3%，MathVerse-Solid 上 84.1%。与 proposal 高度相关但方法不同。\n\n9. TVC / Take-along Visual Conditioning (ACL 2025):\n   在长 CoT 中周期性重新注入 visual token，+3.4%。Proposal 称其无法纠正初始感知错误——判断合理。\n\n10. MathVista 当前 SOTA：o3 = 86.8%, Qwen3-VL = 85.8%, Step3-VL-10B = 84.0%。\n\n11. Persistent Visual Memory (arXiv 2605.00814, May 2026):\n    在 LVLM 中加入 lightweight PVM 模块维持 visual perception——但使用连续 embedding，非 symbolic。\n\n- 调研总结：该领域正经历快速迭代，形式化 symbolic parsing (Geoparsing, Hilbert-Geo)、evidence collapse 诊断 (Don't Blink)、perception-reasoning 解耦 (PRCO, CogFlow, MathLens) 三条线在 2025-2026 同步成熟。Proposal 试图在三者交汇点构建系统。但 Symbolic Grounding 论文已证明\"symbolic 表示 + LLM 推理\"本身就能大幅提升性能，使得 proposal 中\"持久化 memory + 双角色 RL + integration reward\"的增量价值面临质疑。\n\n\n【Trivial Alternative 检验】:\n\n**存在明确的 trivial alternative 威胁。**\n\nSymbolic Grounding (Apr 2026) 已证明：仅将 diagram 转为 symbolic 表示再交给 LLM，准确率从 near-chance 跃升至 mid-90s。最直接的 trivial baseline 是：\n- 用 Geoparsing 将 diagram 解析为 symbolic predicates\n- 将 predicates 作为文本 prepend 到 prompt 中\n- 直接让 VLM/LLM 进行推理\n\n这个方案不需要 persistent memory、不需要 dual-role RL、不需要 integration reward，但已能获得大部分收益。\n\nProposal 的 \"persistent queryable scratchpad\" 的核心论据是防止 evidence collapse——但 Don't Blink 发现的 evidence collapse 是 **visual tokens 的 attention 衰减**，而非 text tokens 的问题。一旦 diagram 被转为 text-based symbolic predicates，这些 text tokens 在 causal attention 下并不会像 visual embeddings 那样 \"collapse\"——它们始终存在于 KV cache 中，模型可以通过标准 attention 访问。因此，\"discrete predicates are inherently immune to evidence collapse\" 这个核心 claim 虽然技术上正确，但它的 trivial 实现方式（simply prepend as text）已经满足了这一性质，不需要额外的 scratchpad 机制。\n\n**增量价值在于**：(1) reconstruction-verified Observer reward 提供了独立于 ground-truth 的感知质量信号，这是对 PRCO 的实质改进；(2) integration reward 直接优化 MathLens 识别的瓶颈。但这些增量价值需要与 trivial baseline 对比才能验证，且审稿人几乎必然会要求此 ablation。\n\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的假设：\n\n1. **\"Visual evidence collapse 是 symbolic 表示下的主要瓶颈\"** ——这是最大的逻辑跳跃。Don't Blink 证明的是 *visual token* 的 attention 衰减。一旦信息被编码为 text-based symbolic predicates，衰减模式可能完全不同。Proposal 将 visual token 的衰减问题直接类推到 symbolic reasoning 场景，缺乏直接的实证支撑。Symbolic Grounding 的 mid-90s 结果反而暗示：转为 symbolic 后，evidence collapse 可能已不再是主要瓶颈。\n\n2. **\"Predicate-matching retrieval 优于 standard attention over prepended text\"** ——Proposal 假设显式的 predicate-matching 检索机制优于让 Transformer 自己通过 attention 找到相关信息。这一假设在 Transformer 架构的 in-context retrieval 能力被广泛研究的背景下并非显然成立，特别是当 predicate 集合规模不大（一张几何图的 predicates 通常在几十个量级）时。\n\n3. **\"Reconstruction fidelity 是可靠的 Observer 验证机制\"** ——假设 re-rendering engine 足够精确，且 rendered image 与 original diagram 的视觉比较可以可靠地量化。但 diagram re-rendering 的保真度受限于 rendering engine 的能力，原始 diagram 可能包含 hand-drawn noise、非标准标注等，rendering comparison 的 metric 设计非 trivial。\n\n4. **\"Integration reward (predicate utilization) 能有效优化 cross-modal integration\"** ——衡量 \"predicate utilization across steps\" 是一个 proxy metric。高 utilization 不等于正确 integration；低 utilization 也可能是合理的（某些 step 不需要参考 diagram）。这个 reward 的设计空间和潜在 reward hacking 风险未被讨论。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — 核心贡献是将三个已有组件（Geoparsing 的 formal parsing、SymHPR 的 reconstruction verification、PRCO 的 dual-role RL）进行系统集成，并新增 integration reward。每个单独组件都已存在于近 6 个月的文献中。集成的 engineering novelty 不等于 conceptual novelty。最核心的\"persistent symbolic memory prevents evidence collapse\"这一 claim 的逻辑基础存在问题——Symbolic Grounding (Apr 2026) 已证明仅转换为 symbolic 表示即可大幅提升性能，使得 persistent memory 的增量价值不清晰。Integration reward 是真正的新贡献点，但单一 reward signal 的设计创新在 novelty 层面分量有限。Hilbert-Geo (May 2026) 也在同一时期做了 formal language + reasoning 的工作，进一步压缩了 novelty space。\n\n2. **Significance: 中** — 研究问题（visual math reasoning 中的 perception-reasoning integration）是重要且 timely 的，得到了 MathLens、Don't Blink、PRCO 等多篇论文的独立验证。但 proposal 的方法局限于 geometry domain（symbolic predicates 针对 points、lines、angles、relations），无法直接推广到 charts、plots、统计图等其他 visual math 类型，限制了影响力。此外，目标 benchmark 正在被大型模型快速饱和（o3 已达 86.8% MathVista），在 8B 模型上期望 3-5 点提升虽合理，但影响力受限于 model scale。结论的 surprising 程度有限——\"用 symbolic 表示 + RL 提升 visual math\" 的大方向已被多篇论文验证，核心发现如果 positive，审稿人可能会说 \"makes sense, I would have expected this to work\"。\n\n3. **Related Work: 强** — Proposal 对近期文献的覆盖非常全面且准确。所有引用的关键论文均经验证存在，描述基本准确。与 Geoparsing、SymHPR、PRCO、CogFlow、Don't Blink、MathLens、Hilbert-Geo、GeoMathCode、CoRGI、KAWHI 等工作的差异化定位清晰。特别值得肯定的是对 concurrent work (May 2026) 的覆盖和对 MathLens 的深入引用。\n\n\n【概率估计】: [22% - 32%] 中位 26%\n\n【估计理由】:\nRelated Work 是强项但不影响概率上限。Significance 处于中等——问题重要但方法的 domain 限制和 benchmark 饱和压低了影响力。**概率上限主要受 Novelty 限制**：核心 \"persistent symbolic memory\" claim 面临 trivial alternative（prepend symbolic predicates as text）的严重威胁，逻辑链中将 visual token 的 evidence collapse 类推到 text-based symbolic predicates 的环节缺乏实证支撑。如果审稿人指出 \"just prepend Geoparsing output already solves the evidence collapse problem you identify\"，proposal 的核心立论将被动摇。Integration reward 是真正的新贡献点，但不足以独立支撑一篇顶会论文。整体来看，这是一个工程集成优于概念创新的 proposal，在 \"方向正确但核心 claim 的增量价值不清晰\" 的区间。\n\n【主要风险】:\n1. **Trivial alternative 致命威胁**：Symbolic Grounding 已证明 \"symbolic 表示 + LLM\" 即可达 mid-90s；简单 prepend Geoparsing output 可能捕获 SymMem 大部分收益，使整套 persistent memory + dual RL + integration reward 的增量价值在 ablation 中表现为 marginal improvement。\n2. **Evidence collapse 类推的逻辑漏洞**：Don't Blink 的 evidence collapse 是 visual token 特有现象；text-based symbolic predicates 天然存在于 KV cache 中不会\"collapse\"，使得 \"persistent memory prevents evidence collapse\" 这一核心 framing 在审稿人追问下可能站不住脚，导致整篇论文的 motivation 被质疑。\n```\n\nSources:\n- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/pdf/2604.04207)\n- [PRCO: Seeing with You: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)\n- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)\n- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)\n- [CogFlow: Bridging Perception and Reasoning (ICLR 2026)](https://openreview.net/forum?id=sZ0DsaRsd4)\n- [MathLens: What MLLMs Learn about Multimodal Reasoning](https://arxiv.org/abs/2510.01719)\n- [Hilbert-Geo: Solving Solid Geometric Problems](https://arxiv.org/abs/2605.16385)\n- [TVC: Mitigating Visual Forgetting (ACL 2025)](https://aclanthology.org/2025.acl-long.257/)\n- [MathVista Leaderboard](https://llm-stats.com/benchmarks/mathvista)\n- [Persistent Visual Memory for LVLMs](https://arxiv.org/abs/2605.00814)\n- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research data. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/abs/2604.04207) (arXiv Apr 2026): 直接支撑本 proposal 的动机。量化了多步推理中 >50% 的视觉注意力衰减。但注意：该文研究的是 **visual token** 的注意力衰减——即图像 embedding 在 causal attention 下的权重递减，并非 text token 的衰减。\n- [PRCO: Seeing with You](https://arxiv.org/abs/2603.28618) (arXiv Mar 2026): 本 proposal 最直接的 baseline。Observer-Solver 双角色 RL 框架，用 NL caption 桥接感知-推理，8 个 benchmark 平均 +7 pts。Proposal 准确描述了其局限（NL caption 不可验证）。\n- [Geoparsing](https://arxiv.org/abs/2604.11600) (arXiv Apr 2026): 平面+立体几何的 SOTA 形式化解析，SFT+RLVR 训练范式，GDP-29K 数据集。Proposal 准确引用。\n- [SymHPR](https://arxiv.org/abs/2512.03126) (arXiv Dec 2025): 自监督符号自编码器，98.2% 重建保真度。Proposal 准确引用，拟用其重建验证思路。\n- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346) (arXiv Apr 2026): **关键竞争论文**。证明仅将视觉输入替换为符号输入（无需任何架构改动），LLM 就能从 near-chance 跃升至 mid-90s。这对 proposal 构成 trivial alternative 威胁：如果仅做符号转换就够了，额外的 persistent memory + dual-role RL 增量在哪？\n- [MathLens / What MLLMs Learn](https://arxiv.org/abs/2510.01719) (arXiv Oct 2025): 将多模态推理分解为 Perception/Reasoning/Integration，发现 integration 是主要瓶颈，RL 主要改善感知。Proposal 准确引用。\n- [Hilbert-Geo](https://arxiv.org/abs/2605.16385) (arXiv May 2026): **最近的直接竞争者**。为立体几何设计形式化语言 + Parse2Reason pipeline，SolidFGeo2k 达 77.3%，大幅超越 Gemini-2.5-pro。与 proposal 的差异仅在于：Hilbert-Geo 无 RL 训练、无 persistent memory。但它验证了\"形式化解析 → 推理\"这一 pipeline 本身就已非常有效。\n- [GeoMathCode](https://arxiv.org/abs/2605.25384) (arXiv May 2026): 代码作为中间可执行表示辅助几何推理。与本 proposal 方向相似但机制不同（code vs. symbolic predicates）。\n- [CogFlow](https://openreview.net/forum?id=Jivgo2qRGI) (ICLR 2026): perception→internalization→reasoning 三阶段，MathVista 76.8%。使用 text-based 内化而非形式化验证。\n\n- **调研总结**: 2025-2026年，视觉数学推理领域出现了两条并行路线：(1) RL 驱动的感知-推理协同（PRCO, KAWHI），(2) 形式化符号解析（Geoparsing, Hilbert-Geo, SymHPR）。两条路线目前尚未被系统性地融合，proposal 定位在这个交叉口。但 Symbolic Grounding 论文和 Hilbert-Geo 的结果暗示，符号转换本身（无需额外架构）就可能获得大部分收益。\n\n【Trivial Alternative 检验】:\n**存在明确的 trivial alternative 威胁。** 最简单的替代方案是：Geoparsing 将图转换为符号谓词 → 将谓词作为文本直接 prepend 到 prompt → 标准 CoT 推理。理由：\n1. \"Don't Blink\" 量化的 evidence collapse 是针对 **visual tokens**（连续 embedding）在 causal attention 下的衰减。一旦图被解析为 **text tokens**（符号谓词），它们就和推理链处于同一模态，不再受视觉特有的衰减机制影响。\n2. Symbolic Grounding 论文已证明，仅做输入格式转换（visual → symbolic text），无需任何训练或架构改动，就能获得 25-30 pt 的提升。\n3. Hilbert-Geo 的 Parse2Reason pipeline（无 RL、无 persistent memory）已在固体几何上大幅超越 frontier models。\n\n因此，proposal 的**增量价值**必须来自三个额外组件的叠加效益：(a) persistent queryable scratchpad vs. one-time prepend, (b) reconstruction-based verification reward, (c) integration reward。其中 (b) 是最有说服力的增量——PRCO 的 NL caption 不可验证，而符号谓词可通过重建来验证。但 (a) 的增量价值存疑：text tokens 不是 visual tokens，\"persistent scratchpad\" 和 \"prepend once\" 在功能上可能差异不大。\n\n【前提假设检验】:\n核心 claim 的逻辑链有以下未经验证的关键假设：\n\n1. **\"符号谓词在 causal attention 下不衰减\"**——这是 proposal 最核心的前提，但未经验证。Don't Blink 研究的是 visual tokens 的衰减，proposal 将结论外推到\"所有 continuous representations 都衰减，只有 discrete predicates 不衰减\"。然而，符号谓词一旦被 tokenize 为 text tokens，它们在 transformer 中和其他 text tokens 一样参与 attention 计算，同样可能在长序列中被稀释。Proposal 混淆了\"离散 vs 连续\"和\"visual modality vs text modality\"两个维度。\n\n2. **\"重建保真度是 Observer 质量的可靠信号\"**——SymHPR 在受控的几何图上达到 98.2% 重建保真度，但实际考试/教科书图形往往包含手写标注、不规范绘制、遮挡等。重建验证的鲁棒性未经验证。\n\n3. **\"Integration reward（谓词利用率）能有效优化感知-推理桥接\"**——\"用了更多谓词\"不等于\"更好地整合了信息\"。一个 Solver 可以引用大量谓词但推理方向错误，也可以仅引用关键谓词就得出正确答案。以利用率为 reward signal 可能导致 reward hacking。\n\n4. **\"8B 模型可以在形式化解析 + 推理 + RL 三重任务上同时达到高水平\"**——Geoparsing 用专门模型做解析已是 SOTA；PRCO 用专门框架做 RL 已是 SOTA。将两者压缩到同一个 8B 模型中同时训练，容量是否足够？\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — 核心贡献是将 3 个已有组件（Geoparsing 的符号解析 + PRCO 的双角色 RL + SymHPR 的重建验证）组合成一个 pipeline，并加入 persistent scratchpad 和 integration reward。这是一个合理的系统组合，但缺乏概念层面的突破。Hilbert-Geo（May 2026）已经实现了\"形式化解析 → 推理\"这一核心思路并取得 SOTA；PRCO 已经实现了 Observer-Solver RL。Proposal 的独特增量在于 (i) 可验证的 Observer 和 (ii) integration reward，前者有一定新意，后者属于增量。Symbolic Grounding 论文进一步削弱了 novelty——如果符号转换本身就能 close the gap，那额外的架构复杂度的增量价值需要更强的论证。\n\n2. **Significance: 中** — 问题本身（视觉数学推理中的 evidence collapse 和 integration failure）是重要的、被社区广泛关注的问题（Don't Blink, MathLens, CogFlow 均在 2025-2026 发表于顶会/arXiv）。但 proposal 的适用范围限于**几何图形**——符号谓词（点、线、角、关系）是几何特有的表示，难以推广到图表、函数图、统计图等其他视觉数学问题类型。这限制了贡献的普适性。预期提升 3-5 pts over PRCO 也较为保守，在 MathVista SOTA 已达 86.8% 的背景下，如果最终结果在 open-source 8B 模型上从 ~78 提升到 ~83，审稿人可能会认为这是合理但不 surprising 的改进。\n\n3. **Related Work: 强** — 这是 proposal 最突出的优点。对领域的覆盖非常全面，包括最新的 concurrent works（Hilbert-Geo May 2026, GeoMathCode May 2026）。每篇引用的描述经验证均准确。与各竞争工作的差异化定位清晰（vs. PRCO: 可验证 vs NL caption; vs. Geoparsing: 解析+记忆+RL vs 仅解析; vs. Hilbert-Geo: RL训练 vs pipeline; vs. CoRGI: 训练时集成 vs 推理时验证）。\n\n【概率估计】: [22% - 30%] 中位 26%\n\n【估计理由】: Related Work 覆盖是强项，表明作者对领域有深入理解，但这主要保证了论文的\"形式下限\"。Novelty 是主要瓶颈——核心贡献是系统组合而非概念突破，且面临 Symbolic Grounding 论文揭示的 trivial alternative 威胁（仅做符号转换就可能获得大部分收益）。Significance 受限于几何领域的局限性和保守的预期提升。最关键的是，proposal 的核心逻辑前提（\"符号谓词不衰减\"）混淆了 visual token decay 和 text token attention patterns，这一漏洞如果被审稿人抓住会严重削弱立论基础。整体来看，这是一个\"well-executed combination paper\"，有望进入 borderline 区间，但在 idea 层面不足以让审稿人写出 \"surprising\"。Novelty 的中偏弱评价限制了上界。\n\n【主要风险】:\n1. **Trivial alternative 风险**：审稿人可能指出\"直接 prepend 符号谓词 + 标准 CoT\"就能获得类似效果（参考 Symbolic Grounding 和 Hilbert-Geo 的结果），从而质疑 persistent scratchpad + dual-role RL + integration reward 的增量价值是否值得这么大的系统复杂度。\n2. **核心前提漏洞**：proposal 将 \"evidence collapse\"（visual token 衰减）的结论外推到所有 continuous representations，并声称 discrete predicates 天然免疫——但符号谓词作为 text tokens 参与 attention 计算时同样受长序列注意力稀释的影响。审稿人可能指出这一逻辑跳跃，动摇整个 persistent memory 的动机基础。\n```\n\nSources:\n- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/abs/2604.04207)\n- [PRCO: Seeing with You](https://arxiv.org/abs/2603.28618)\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)\n- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)\n- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)\n- [MathLens: What MLLMs Learn about Multimodal Reasoning](https://arxiv.org/abs/2510.01719)\n- [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/abs/2605.16385)\n- [GeoMathCode: Interleaved Math-Code Reasoning](https://arxiv.org/abs/2605.25384)\n- [MathVista Leaderboard](https://mathvista.github.io/)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to make a thorough assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **PRCO: \"Seeing with You: Perception-Reasoning Coevolution\" (arXiv 2603.28618, Mar 2026)**:\n   最直接的竞争工作。提出 Observer-Solver 双角色 RL 框架，Observer 生成 NL caption，Solver 基于 caption 推理。平均 +7pts 提升。本 proposal 的核心设计（双角色 RL）直接继承自 PRCO，区别在于用 formal symbolic predicates 替代 NL captions。\n\n2. **Geoparsing (arXiv 2604.11600, Apr 2026)**:\n   构建 GDP-29K 数据集，SFT+RLVR 训练 formal diagram parser，达到 SOTA 几何图解析。本 proposal 的 formal parser 模块直接复用该方法。\n\n3. **Don't Blink: Evidence Collapse (arXiv 2604.04207, Apr 2026)**:\n   量化了推理 VLM 在 chain-of-thought 过程中 >50% 的 visual evidence attention loss。本 proposal 的核心 motivation 之一。但注意：该论文测量的是对**视觉 token**的注意力衰减，而非对**文本化符号谓词**的衰减。\n\n4. **Symbolic Grounding (arXiv 2604.21346, Apr 2026)**:\n   证明给 LLM 提供符号化输入（替代原始图像），抽象视觉推理从 near-chance 提升到 mid-90s。证明了符号表示的价值，但该工作是**诊断性**的（探测瓶颈在哪里），并非提出持久化记忆或 RL 训练方案。\n\n5. **SymHPR (arXiv 2512.03126, Dec 2025)**:\n   符号化自编码器 + 层级过程奖励模型，98.2% 重建保真度。本 proposal 借用其 reconstruction fidelity 作为 Observer reward 信号。\n\n6. **CogFlow (ICLR 2026, arXiv 2601.01874)**:\n   三阶段框架 perception→internalization→reasoning，用知识内化奖励桥接感知与推理。MathVista 76.8%。与本 proposal 目标相似（桥接感知-推理），但用 text-based internalization 而非 formal symbolic。\n\n7. **MathLens (arXiv 2510.01719, Oct 2025)**:\n   分解多模态推理为 perception / reasoning / integration，发现 integration 是主要失败模式，RL 主要提升 perception 而非 integration。本 proposal 的 integration reward 设计直接针对该发现。\n\n8. **v1 (arXiv 2505.18842, May 2025)**:\n   point-and-copy 机制让模型在推理过程中动态回引视觉 token。缓解 evidence decay 但无法纠正初始感知错误。\n\n9. **Hilbert-Geo (arXiv 2605.16385, May 2026)**:\n   固体几何形式语言 + Parse2Reason pipeline，但无 RL 训练、无持久记忆。功能上部分重叠。\n\n10. **KAWHI (arXiv 2603.27375, Mar 2026)**:\n    注意力加权奖励重分配，将视觉证据与推理步骤对齐，但不使用符号表示。\n\n11. **FIGR (arXiv 2512.24297, Jan 2026)**:\n    通过 RL 在推理中生成可执行代码构建图表。类似\"外化中间状态\"思路，但方向不同（生成新图 vs. 解析已有图为符号记忆）。\n\n12. **GeoMathCode (arXiv 2605.25384, May 2026)**:\n    交错数学-代码推理，代码作为辅助可执行表示而非持久化可查询记忆。\n\n13. **CoRGI (arXiv 2508.00378, Aug 2025)**:\n    推理后逐步视觉验证，改善幻觉。仅推理时使用，未集成到 RL 训练。\n\n- **调研总结**: 视觉数学推理领域在 2025-2026 年极其活跃，围绕 evidence decay（Don't Blink, v1）、感知-推理桥接（PRCO, CogFlow, MathLens）、形式化图解析（Geoparsing, Hilbert-Geo）三条线并行推进。本 proposal 处于这三条线的交汇点，试图将 formal symbolic parsing + persistent memory + dual-role RL 组合为统一框架。每个组件已有成熟先例，核心贡献在于组合方式。\n\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial baseline：**直接将 Geoparsing 的 formal output 拼接到 prompt 前面，让模型在推理时直接引用**（即 \"parse once, prepend, then reason\"）。Symbolic Grounding 论文已经证明，仅仅给 LLM 提供符号化输入就能从 near-chance 跳到 mid-90s。\n\n这个 trivial alternative 是真实威胁。本 proposal 的增量价值在于：\n- **持久化可查询记忆**：通过 predicate-matching retrieval 避免 long-context 注意力衰减。但这里有一个关键问题：Don't Blink 测量的是**视觉 token**的注意力衰减，而 symbolic predicates 一旦文本化后就是**语言 token**，是否同样受 causal attention decay 影响并不清楚。proposal 声称\"discrete predicates do not degrade under causal attention\"缺乏理论或实证支撑。\n- **Reconstruction-based verification**：无需 ground-truth 标签就能验证 Observer 准确性。这是比 PRCO 的 NL caption 真正的改进点。\n- **Integration reward**：显式优化 predicate 利用率。这是一个有意义但相对常规的 RL reward shaping 设计。\n\n**结论**：存在明确的 trivial alternative 威胁。proposal 的增量价值主要在 reconstruction verification 和 integration reward，而非\"持久化记忆\"本身——因为\"持久化\"的必要性假设（symbolic text tokens 也会 decay）未被充分论证。\n\n\n【前提假设检验】:\n\n核心逻辑链中有**三个关键未验证假设**：\n\n1. **\"离散符号谓词在 causal attention 下不衰减\"** — 这是整个架构的理论基石。但 Don't Blink 研究的是 visual token attention decay，而非 text token decay。如果符号谓词被编码为文本 token（就是普通 token），它们仍然会受到 long-context attention 稀释的影响。proposal 将 visual token 的衰减问题偷换为所有 token 的衰减问题，然后声称文本化符号 token 免疫——这一步逻辑跳跃缺乏支撑。\n\n2. **重建保真度能充当可靠的 Observer reward** — re-render predicates 并与原图比较，能否检测所有类型的解析错误？几何关系可能在重建中\"看起来正确\"但丢失了微妙的空间语义（例如角度近似、比例关系）。SymHPR 报告 98.2% fidelity，但这是在其受控数据上的表现，迁移到更复杂的 real-world diagrams 时是否保持，是未知的。\n\n3. **3-5 point gains over PRCO 是可实现的** — MathVista SOTA (o3) 是 86.8%，open-model SOTA (Qwen3-VL) 85.8%，PRCO 在 base model 上 +7pts。在已接近 ceiling 的情况下，再获 3-5pts 增量（且只在几何子集上有效的方法）是非常困难的。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中 (偏弱)** — 核心贡献是 PRCO（双角色 RL）+ Geoparsing（formal parsing）+ SymHPR（reconstruction verification）+ 持久记忆的**系统性组合**。每个组件都有直接先例。组合本身是**自然的 next step**：任何同时读过 PRCO、Geoparsing、Don't Blink 三篇论文的研究者都会想到\"用 formal symbolic parsing 替代 PRCO 的 NL Observer 并维持 persistent memory\"。Hilbert-Geo (May 2026) 已经在做 formal parsing + reasoning pipeline（只是没有 RL）；FIGR 已经在做推理过程中外化中间状态（只是用代码而非符号谓词）。在如此密集的竞争格局下，\"组合 novelty\"的存活空间有限。Reconstruction verification 作为 Observer reward 是相对最新颖的子贡献，但单独来看偏 incremental。\n\n2. **Significance: 中** — 问题本身（evidence collapse + integration failure）是重要且有文献支撑的。但 proposal 的方法**高度 geometry-specific**：formal parsers（Geoparsing, FormalGeo）仅覆盖几何图，不适用于 MathVista 中的函数图、表格、统计图等其他视觉数学类型。这严重限制了方法的泛化性。如果方法只在几何子集上有效，对整个 visual math reasoning 领域的影响有限。此外，3-5pts 的预期增量在 ceiling 效应下属于 marginal improvement。\n\n3. **Related Work: 强** — 对近期工作的覆盖非常全面且准确。所有引用论文均经验证真实存在，描述与实际内容匹配度高。差异化定位清晰——对每个 concurrent work 都明确说明了 proposal 的区别（Hilbert-Geo: 无 RL/persistent memory; KAWHI: 无符号表示; GeoMathCode: code as auxiliary; CoRGI: inference-only）。MathLens → integration reward 的 motivation chain 特别有说服力。这是 proposal 最强的维度。\n\n\n【概率估计】: [22% - 32%] 中位 27%\n\n【估计理由】:\n- Related Work 维度强，说明作者对领域有深度理解，但这提升的是执行质量的下限，不改变 idea 上限。\n- Novelty 偏弱是主要瓶颈：核心贡献是已有组件的 natural combination，审稿人大概率会写 \"the contribution is primarily in combining existing techniques\" 或 \"incremental over PRCO + Geoparsing\"。这直接限制了概率上界。\n- Significance 受限于 geometry-specific 性质和 ceiling 效应，进一步压缩了概率。\n- 如果核心实验结果 positive（3-5pts gain），审稿人的反应更可能是 \"makes sense, I would have expected formal representations to help\" 而非 \"surprising\"——这将 idea 定位在 25-35% 区间的下半段。\n- 前提假设中\"symbolic text tokens 不衰减\"的逻辑漏洞如果被审稿人抓住，可能成为致命伤。\n\n【主要风险】:\n1. **\"Systems combination\" novelty 不足**：每个组件（formal parsing, dual-role RL, reconstruction reward, persistent memory）都有直接先例，组合方式是 natural next step，审稿人可能判定 novelty 不够 AAAI main conference 的门槛。\n2. **核心理论假设有逻辑漏洞**：proposal 将 Don't Blink 发现的 visual token decay 外推为\"所有 evidence 都会 collapse\"，然后声称 symbolic text tokens 免疫——这一推理链条中间有跳跃，如果审稿人追问\"为什么 symbolic predicates 作为 text tokens 就不会在 long context 中被忽略\"，proposal 目前无法给出有力回应。\n```\n\nSources:\n- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/pdf/2604.04207)\n- [PRCO: Seeing with You: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)\n- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)\n- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)\n- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)\n- [CogFlow: Bridging Perception and Reasoning through Knowledge Internalization](https://arxiv.org/abs/2601.01874)\n- [MathLens: What MLLMs Learn about Multimodal Reasoning](https://arxiv.org/abs/2510.01719)\n- [v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning](https://arxiv.org/abs/2505.18842)\n- [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/abs/2605.16385)\n- [KAWHI: Bridging Visual Representation and RLVR](https://arxiv.org/abs/2603.27375)\n- [FIGR: Figure It Out - Executable Visual States](https://arxiv.org/abs/2512.24297)\n- [GeoMathCode: Understanding Interleaved Math-Code Reasoning](https://arxiv.org/abs/2605.25384)\n- [CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding](https://arxiv.org/abs/2508.00378)\n- [MathVista Leaderboard](https://mathvista.github.io/)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Verifiable Symbolic Memory Prevents Evidence Collapse in Visual Math\n\n## Core Problem\n\nMulti-step visual mathematical reasoning suffers from evidence collapse (>50% visual attention loss during chain-of-thought) and cross-modal integration failure (the dominant error mode even as perception and reasoning independently improve), because models encode diagrams once into continuous embeddings that progressively decay under causal attention masking.\n\n## Research Opportunity\n\nRecent formal diagram parsers (Geoparsing Apr 2026, SymHPR Dec 2025) achieve SOTA conversion of diagrams into verifiable symbolic predicates, and the Symbolic Grounding paper (Apr 2026) proves that symbolic representations close the vision-reasoning gap entirely (near-chance → mid-90s). Yet no work uses these formal representations as persistent, queryable, step-level memory during reasoning — they are consumed once then forgotten. Meanwhile, the best integration method (PRCO, Mar 2026) still uses unverifiable NL captions as the perception-reasoning bridge, leaving a clear opportunity to combine formal symbolic parsing with dual-role RL training to simultaneously solve evidence collapse and integration failure.\n\n## Research Landscape\n\nCurrent MathVista SOTA is o3 at 86.8%; open models like Qwen3-VL reach 85.8% and Step3-VL-10B reach 84.0%. PRCO (Mar 2026) achieves +7pts average via an NL Observer-Solver RL framework but cannot independently verify observer accuracy. CogFlow (ICLR 2026) models perception→internalization→reasoning as three stages achieving 76.8% MathVista, but uses text-based (not formally verifiable) internalization. Geoparsing (Apr 2026) achieves SOTA formal diagram parsing for plane+solid geometry via SFT+RLVR; SymHPR (Dec 2025) demonstrates self-supervised symbolic auto-encoding at 98.2% reconstruction fidelity. Don't Blink (Apr 2026) quantifies >50% evidence mass loss during reasoning, and v1 (May 2025) mitigates decay via visual-token re-attention but cannot correct initial perception errors. MathLens (2025) shows integration remains the principal failure mode as perception and reasoning improve — RL predominantly improves perception while integration lags regardless of pretraining. Concurrent: Hilbert-Geo (May 2026) proposes a formal language for solid geometry with a Parse2Reason pipeline but uses no RL training or persistent memory; KAWHI (Mar 2026) bridges visual representation with RLVR via attention-based reward reweighting but does not employ symbolic representations; GeoMathCode (May 2026) interleaves math-code reasoning but code serves as auxiliary executable representation rather than persistent queryable symbolic memory; CoRGI (2025) performs post-hoc step-wise visual verification but is inference-only and not integrated into RL training.\n\n## Proposed Approach\n\nTrain a formal symbolic parser on Qwen3-VL-8B using Geoparsing's SFT+RLVR recipe over GDP-29K and FormalGeo data, converting visual diagrams into a structured set of verifiable symbolic predicates (points, lines, angles, relations) stored in a persistent symbolic scratchpad. Replace PRCO's natural-language Observer with a formal Observer that outputs symbolic predicates verified via SymHPR-style reconstruction fidelity (re-render predicates and compare against the original diagram), while the Solver queries this symbolic scratchpad at each chain-of-thought step through predicate-matching retrieval — preventing evidence decay by design since discrete predicates do not degrade under causal attention. Train both roles jointly using dual-objective RL: the Observer receives reconstruction-verification rewards (computable without ground-truth labels), the Solver receives outcome-correctness rewards, and an auxiliary integration reward measures symbolic predicate utilization across reasoning steps to explicitly optimize the perception-reasoning bridge that MathLens identifies as the dominant failure mode. Evaluate on MathVista, MathVerse, GeoQA, and WeMath, with ablations isolating the contributions of formal parsing, persistent memory, and the integration reward.\n\n## Detailed Description\n\nWe propose SymMem, a method that converts visual diagrams into formally verifiable symbolic predicates and maintains them as a persistent, queryable scratchpad throughout multi-step mathematical reasoning. Current approaches either parse diagrams into formal representations consumed once then discarded (Geoparsing, Hilbert-Geo), or use unverifiable natural-language captions as the perception-reasoning bridge (PRCO, CogFlow). Our key insight is that discrete symbolic predicates are inherently immune to the evidence collapse phenomenon (>50% attention loss quantified by Don't Blink) that plagues continuous embeddings under causal attention. We build on Qwen3-VL-8B and train a formal Observer via SFT+RLVR that outputs structured geometric predicates verified through reconstruction fidelity (re-rendering and comparing against source diagrams, following SymHPR). A Solver queries this symbolic memory at each reasoning step via predicate-matching retrieval. Dual-role RL jointly optimizes the Observer (reconstruction reward) and Solver (outcome reward), with an explicit integration reward measuring predicate utilization across steps — directly targeting the integration failure mode identified by MathLens as the dominant bottleneck. We target MathVista, MathVerse, GeoQA, and WeMath, expecting 3–5 point gains over PRCO baselines.\n\n## Key References\n\n- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning (arXiv 2026)\n- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)\n- Hierarchical Process Reward Models are Symbolic Vision Learners (arXiv 2025)\n- Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv 2026)\n- Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning (arXiv 2026)\n- v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning (arXiv 2025)\n- What MLLMs Learn about When they Learn about Multimodal Reasoning: Perception, Reasoning, or their Integration? (arXiv 2025)\n- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026)\n- Mitigating Visual Forgetting via Take-along Visual Conditioning for Multi-modal Long CoT Reasoning (ACL 2025)\n- Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models (arXiv 2026)\n- CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding (arXiv 2025)\n- STEP3-VL-10B Technical Report (arXiv 2026)\n- Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning (arXiv 2026)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 500–650 H100-hours (Phase 1 formal parser SFT: ~120h on 8×H100; Phase 2 reconstruction verifier: ~60h; Phase 3 dual-role RL: ~300h; Phase 4 evaluation + ablations: ~80h), timeline: 12–14 weeks (2 wks parser data curation, 2 wks parser SFT+RLVR, 2 wks verifier, 4 wks dual-role RL tuning, 2–4 wks eval+writing), estimated_gpu_cost: $1,250–$1,625 at $2.50/hr spot H100\n- **human_in_loop**: gpu_hours: 400–550 H100-hours (Claude assists with reward function design, data augmentation, hyperparameter search space, ablation analysis), timeline: 8–10 weeks, claude_api_cost: $150–$250 (experiment orchestration, code generation for symbolic parser integration, result analysis with Sonnet 4.6), estimated_gpu_cost: $1,000–$1,375 at $2.50/hr spot H100\n- **auto_research**: gpu_hours: 600–800 H100-hours (wider hyperparameter sweeps, automated ablation matrix, additional dataset variants), timeline: 5–7 weeks (parallelized experiment execution), claude_api_cost: $400–$600 (continuous experiment monitoring, automated code repair, paper drafting assistance), estimated_gpu_cost: $1,500–$2,000 at $2.50/hr spot H100, speed_bottleneck: Reward function design for symbolic reconstruction verification requires human judgment on geometric consistency metrics; RL training loop debugging for dual-role credit assignment is poorly suited to full automation; symbolic parser failure modes on out-of-distribution diagrams need expert inspection\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T22:56:39.082Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T22:56:39.082Z",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T22:56:39.145Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
I now have comprehensive field knowledge. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv 2604.04207, Apr 2026):
   直接支撑 proposal 的动机之一。证实推理 VLM 在 CoT 过程中对视觉 evidence 区域的 attention 丢失 >50%。但关键细节：该现象特指 *visual tokens* 的 attention 衰减，而非文本 token 的丢失。论文提出的 mitigation 是 inference-time 的 "vision veto"，不涉及训练或 symbolic memory。

2. PRCO / Seeing with You: Perception-Reasoning Coevolution (arXiv 2603.28618, Mar 2026):
   Proposal 的直接前序工作和主要 baseline。Observer-Solver 双角色 RL 框架，Observer 输出 NL evidence caption，Solver 基于 caption 推理，平均 +7pts。Proposal 声称 PRCO 的 NL caption 不可验证——这一判断准确，PRCO 的 Observer 奖励来自 Solver 的下游成功，不独立验证 Observer 输出的准确性。

3. Geoparsing (arXiv 2604.11600, Apr 2026):
   SFT+RLVR 训练形式化几何图解析器，GDP-29K 数据集，实现 SOTA parsing。Proposal 直接复用其训练 recipe。论文本身只做 parsing 不做持久化 memory 或 RL reasoning。

4. Symbolic Grounding Reveals Representational Bottlenecks (arXiv 2604.21346, Apr 2026):
   **关键论文**——证明将图表转为 symbolic 输入后 LLM 准确率从 near-chance 跳至 mid-90s。这既支撑了 proposal 的方向，**也构成了 trivial alternative 的威胁**：仅仅"转换为 symbolic 再推理"（不需要 persistent memory 或 dual RL）已能大幅弥合 gap。

5. SymHPR / Hierarchical Process Reward Models are Symbolic Vision Learners (arXiv 2512.03126, Dec 2025):
   自监督 symbolic auto-encoder，98.2% reconstruction fidelity。Proposal 复用其重建验证机制作为 Observer reward。论文本身不做 reasoning 或 RL training。

6. CogFlow (ICLR 2026):
   三阶段 perception→internalization→reasoning 框架，76.8% MathVista。使用文本 internalization（非形式化）。Proposal 正确识别了与 CogFlow 的差异点。

7. MathLens / What MLLMs Learn... (arXiv 2510.01719, Oct 2025):
   证明 integration 是主要失败模式：RL 主要提升 perception，SFT 主要提升 reasoning，但 integration 始终 lagging。Proposal 的 integration reward 直接针对此发现。

8. Hilbert-Geo (arXiv 2605.16385, May 2026):
   形式化立体几何语言 + Parse2Reason pipeline，无 RL、无 persistent memory。在 SolidFGeo2k 上 77.3%，MathVerse-Solid 上 84.1%。与 proposal 高度相关但方法不同。

9. TVC / Take-along Visual Conditioning (ACL 2025):
   在长 CoT 中周期性重新注入 visual token，+3.4%。Proposal 称其无法纠正初始感知错误——判断合理。

10. MathVista 当前 SOTA：o3 = 86.8%, Qwen3-VL = 85.8%, Step3-VL-10B = 84.0%。

11. Persistent Visual Memory (arXiv 2605.00814, May 2026):
    在 LVLM 中加入 lightweight PVM 模块维持 visual perception——但使用连续 embedding，非 symbolic。

- 调研总结：该领域正经历快速迭代，形式化 symbolic parsing (Geoparsing, Hilbert-Geo)、evidence collapse 诊断 (Don't Blink)、perception-reasoning 解耦 (PRCO, CogFlow, MathLens) 三条线在 2025-2026 同步成熟。Proposal 试图在三者交汇点构建系统。但 Symbolic Grounding 论文已证明"symbolic 表示 + LLM 推理"本身就能大幅提升性能，使得 proposal 中"持久化 memory + 双角色 RL + integration reward"的增量价值面临质疑。


【Trivial Alternative 检验】:

**存在明确的 trivial alternative 威胁。**

Symbolic Grounding (Apr 2026) 已证明：仅将 diagram 转为 symbolic 表示再交给 LLM，准确率从 near-chance 跃升至 mid-90s。最直接的 trivial baseline 是：
- 用 Geoparsing 将 diagram 解析为 symbolic predicates
- 将 predicates 作为文本 prepend 到 prompt 中
- 直接让 VLM/LLM 进行推理

这个方案不需要 persistent memory、不需要 dual-role RL、不需要 integration reward，但已能获得大部分收益。

Proposal 的 "persistent queryable scratchpad" 的核心论据是防止 evidence collapse——但 Don't Blink 发现的 evidence collapse 是 **visual tokens 的 attention 衰减**，而非 text tokens 的问题。一旦 diagram 被转为 text-based symbolic predicates，这些 text tokens 在 causal attention 下并不会像 visual embeddings 那样 "collapse"——它们始终存在于 KV cache 中，模型可以通过标准 attention 访问。因此，"discrete predicates are inherently immune to evidence collapse" 这个核心 claim 虽然技术上正确，但它的 trivial 实现方式（simply prepend as text）已经满足了这一性质，不需要额外的 scratchpad 机制。

**增量价值在于**：(1) reconstruction-verified Observer reward 提供了独立于 ground-truth 的感知质量信号，这是对 PRCO 的实质改进；(2) integration reward 直接优化 MathLens 识别的瓶颈。但这些增量价值需要与 trivial baseline 对比才能验证，且审稿人几乎必然会要求此 ablation。


【前提假设检验】:

核心逻辑链中有以下未经验证的假设：

1. **"Visual evidence collapse 是 symbolic 表示下的主要瓶颈"** ——这是最大的逻辑跳跃。Don't Blink 证明的是 *visual token* 的 attention 衰减。一旦信息被编码为 text-based symbolic predicates，衰减模式可能完全不同。Proposal 将 visual token 的衰减问题直接类推到 symbolic reasoning 场景，缺乏直接的实证支撑。Symbolic Grounding 的 mid-90s 结果反而暗示：转为 symbolic 后，evidence collapse 可能已不再是主要瓶颈。

2. **"Predicate-matching retrieval 优于 standard attention over prepended text"** ——Proposal 假设显式的 predicate-matching 检索机制优于让 Transformer 自己通过 attention 找到相关信息。这一假设在 Transformer 架构的 in-context retrieval 能力被广泛研究的背景下并非显然成立，特别是当 predicate 集合规模不大（一张几何图的 predicates 通常在几十个量级）时。

3. **"Reconstruction fidelity 是可靠的 Observer 验证机制"** ——假设 re-rendering engine 足够精确，且 rendered image 与 original diagram 的视觉比较可以可靠地量化。但 diagram re-rendering 的保真度受限于 rendering engine 的能力，原始 diagram 可能包含 hand-drawn noise、非标准标注等，rendering comparison 的 metric 设计非 trivial。

4. **"Integration reward (predicate utilization) 能有效优化 cross-modal integration"** ——衡量 "predicate utilization across steps" 是一个 proxy metric。高 utilization 不等于正确 integration；低 utilization 也可能是合理的（某些 step 不需要参考 diagram）。这个 reward 的设计空间和潜在 reward hacking 风险未被讨论。


【3 维度打分】:

1. **Novelty: 弱-中** — 核心贡献是将三个已有组件（Geoparsing 的 formal parsing、SymHPR 的 reconstruction verification、PRCO 的 dual-role RL）进行系统集成，并新增 integration reward。每个单独组件都已存在于近 6 个月的文献中。集成的 engineering novelty 不等于 conceptual novelty。最核心的"persistent symbolic memory prevents evidence collapse"这一 claim 的逻辑基础存在问题——Symbolic Grounding (Apr 2026) 已证明仅转换为 symbolic 表示即可大幅提升性能，使得 persistent memory 的增量价值不清晰。Integration reward 是真正的新贡献点，但单一 reward signal 的设计创新在 novelty 层面分量有限。Hilbert-Geo (May 2026) 也在同一时期做了 formal language + reasoning 的工作，进一步压缩了 novelty space。

2. **Significance: 中** — 研究问题（visual math reasoning 中的 perception-reasoning integration）是重要且 timely 的，得到了 MathLens、Don't Blink、PRCO 等多篇论文的独立验证。但 proposal 的方法局限于 geometry domain（symbolic predicates 针对 points、lines、angles、relations），无法直接推广到 charts、plots、统计图等其他 visual math 类型，限制了影响力。此外，目标 benchmark 正在被大型模型快速饱和（o3 已达 86.8% MathVista），在 8B 模型上期望 3-5 点提升虽合理，但影响力受限于 model scale。结论的 surprising 程度有限——"用 symbolic 表示 + RL 提升 visual math" 的大方向已被多篇论文验证，核心发现如果 positive，审稿人可能会说 "makes sense, I would have expected this to work"。

3. **Related Work: 强** — Proposal 对近期文献的覆盖非常全面且准确。所有引用的关键论文均经验证存在，描述基本准确。与 Geoparsing、SymHPR、PRCO、CogFlow、Don't Blink、MathLens、Hilbert-Geo、GeoMathCode、CoRGI、KAWHI 等工作的差异化定位清晰。特别值得肯定的是对 concurrent work (May 2026) 的覆盖和对 MathLens 的深入引用。


【概率估计】: [22% - 32%] 中位 26%

【估计理由】:
Related Work 是强项但不影响概率上限。Significance 处于中等——问题重要但方法的 domain 限制和 benchmark 饱和压低了影响力。**概率上限主要受 Novelty 限制**：核心 "persistent symbolic memory" claim 面临 trivial alternative（prepend symbolic predicates as text）的严重威胁，逻辑链中将 visual token 的 evidence collapse 类推到 text-based symbolic predicates 的环节缺乏实证支撑。如果审稿人指出 "just prepend Geoparsing output already solves the evidence collapse problem you identify"，proposal 的核心立论将被动摇。Integration reward 是真正的新贡献点，但不足以独立支撑一篇顶会论文。整体来看，这是一个工程集成优于概念创新的 proposal，在 "方向正确但核心 claim 的增量价值不清晰" 的区间。

【主要风险】:
1. **Trivial alternative 致命威胁**：Symbolic Grounding 已证明 "symbolic 表示 + LLM" 即可达 mid-90s；简单 prepend Geoparsing output 可能捕获 SymMem 大部分收益，使整套 persistent memory + dual RL + integration reward 的增量价值在 ablation 中表现为 marginal improvement。
2. **Evidence collapse 类推的逻辑漏洞**：Don't Blink 的 evidence collapse 是 visual token 特有现象；text-based symbolic predicates 天然存在于 KV cache 中不会"collapse"，使得 "persistent memory prevents evidence collapse" 这一核心 framing 在审稿人追问下可能站不住脚，导致整篇论文的 motivation 被质疑。
```

Sources:
- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/pdf/2604.04207)
- [PRCO: Seeing with You: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)
- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)
- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)
- [CogFlow: Bridging Perception and Reasoning (ICLR 2026)](https://openreview.net/forum?id=sZ0DsaRsd4)
- [MathLens: What MLLMs Learn about Multimodal Reasoning](https://arxiv.org/abs/2510.01719)
- [Hilbert-Geo: Solving Solid Geometric Problems](https://arxiv.org/abs/2605.16385)
- [TVC: Mitigating Visual Forgetting (ACL 2025)](https://aclanthology.org/2025.acl-long.257/)
- [MathVista Leaderboard](https://llm-stats.com/benchmarks/mathvista)
- [Persistent Visual Memory for LVLMs](https://arxiv.org/abs/2605.00814)
- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research data. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/abs/2604.04207) (arXiv Apr 2026): 直接支撑本 proposal 的动机。量化了多步推理中 >50% 的视觉注意力衰减。但注意：该文研究的是 **visual token** 的注意力衰减——即图像 embedding 在 causal attention 下的权重递减，并非 text token 的衰减。
- [PRCO: Seeing with You](https://arxiv.org/abs/2603.28618) (arXiv Mar 2026): 本 proposal 最直接的 baseline。Observer-Solver 双角色 RL 框架，用 NL caption 桥接感知-推理，8 个 benchmark 平均 +7 pts。Proposal 准确描述了其局限（NL caption 不可验证）。
- [Geoparsing](https://arxiv.org/abs/2604.11600) (arXiv Apr 2026): 平面+立体几何的 SOTA 形式化解析，SFT+RLVR 训练范式，GDP-29K 数据集。Proposal 准确引用。
- [SymHPR](https://arxiv.org/abs/2512.03126) (arXiv Dec 2025): 自监督符号自编码器，98.2% 重建保真度。Proposal 准确引用，拟用其重建验证思路。
- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346) (arXiv Apr 2026): **关键竞争论文**。证明仅将视觉输入替换为符号输入（无需任何架构改动），LLM 就能从 near-chance 跃升至 mid-90s。这对 proposal 构成 trivial alternative 威胁：如果仅做符号转换就够了，额外的 persistent memory + dual-role RL 增量在哪？
- [MathLens / What MLLMs Learn](https://arxiv.org/abs/2510.01719) (arXiv Oct 2025): 将多模态推理分解为 Perception/Reasoning/Integration，发现 integration 是主要瓶颈，RL 主要改善感知。Proposal 准确引用。
- [Hilbert-Geo](https://arxiv.org/abs/2605.16385) (arXiv May 2026): **最近的直接竞争者**。为立体几何设计形式化语言 + Parse2Reason pipeline，SolidFGeo2k 达 77.3%，大幅超越 Gemini-2.5-pro。与 proposal 的差异仅在于：Hilbert-Geo 无 RL 训练、无 persistent memory。但它验证了"形式化解析 → 推理"这一 pipeline 本身就已非常有效。
- [GeoMathCode](https://arxiv.org/abs/2605.25384) (arXiv May 2026): 代码作为中间可执行表示辅助几何推理。与本 proposal 方向相似但机制不同（code vs. symbolic predicates）。
- [CogFlow](https://openreview.net/forum?id=Jivgo2qRGI) (ICLR 2026): perception→internalization→reasoning 三阶段，MathVista 76.8%。使用 text-based 内化而非形式化验证。

- **调研总结**: 2025-2026年，视觉数学推理领域出现了两条并行路线：(1) RL 驱动的感知-推理协同（PRCO, KAWHI），(2) 形式化符号解析（Geoparsing, Hilbert-Geo, SymHPR）。两条路线目前尚未被系统性地融合，proposal 定位在这个交叉口。但 Symbolic Grounding 论文和 Hilbert-Geo 的结果暗示，符号转换本身（无需额外架构）就可能获得大部分收益。

【Trivial Alternative 检验】:
**存在明确的 trivial alternative 威胁。** 最简单的替代方案是：Geoparsing 将图转换为符号谓词 → 将谓词作为文本直接 prepend 到 prompt → 标准 CoT 推理。理由：
1. "Don't Blink" 量化的 evidence collapse 是针对 **visual tokens**（连续 embedding）在 causal attention 下的衰减。一旦图被解析为 **text tokens**（符号谓词），它们就和推理链处于同一模态，不再受视觉特有的衰减机制影响。
2. Symbolic Grounding 论文已证明，仅做输入格式转换（visual → symbolic text），无需任何训练或架构改动，就能获得 25-30 pt 的提升。
3. Hilbert-Geo 的 Parse2Reason pipeline（无 RL、无 persistent memory）已在固体几何上大幅超越 frontier models。

因此，proposal 的**增量价值**必须来自三个额外组件的叠加效益：(a) persistent queryable scratchpad vs. one-time prepend, (b) reconstruction-based verification reward, (c) integration reward。其中 (b) 是最有说服力的增量——PRCO 的 NL caption 不可验证，而符号谓词可通过重建来验证。但 (a) 的增量价值存疑：text tokens 不是 visual tokens，"persistent scratchpad" 和 "prepend once" 在功能上可能差异不大。

【前提假设检验】:
核心 claim 的逻辑链有以下未经验证的关键假设：

1. **"符号谓词在 causal attention 下不衰减"**——这是 proposal 最核心的前提，但未经验证。Don't Blink 研究的是 visual tokens 的衰减，proposal 将结论外推到"所有 continuous representations 都衰减，只有 discrete predicates 不衰减"。然而，符号谓词一旦被 tokenize 为 text tokens，它们在 transformer 中和其他 text tokens 一样参与 attention 计算，同样可能在长序列中被稀释。Proposal 混淆了"离散 vs 连续"和"visual modality vs text modality"两个维度。

2. **"重建保真度是 Observer 质量的可靠信号"**——SymHPR 在受控的几何图上达到 98.2% 重建保真度，但实际考试/教科书图形往往包含手写标注、不规范绘制、遮挡等。重建验证的鲁棒性未经验证。

3. **"Integration reward（谓词利用率）能有效优化感知-推理桥接"**——"用了更多谓词"不等于"更好地整合了信息"。一个 Solver 可以引用大量谓词但推理方向错误，也可以仅引用关键谓词就得出正确答案。以利用率为 reward signal 可能导致 reward hacking。

4. **"8B 模型可以在形式化解析 + 推理 + RL 三重任务上同时达到高水平"**——Geoparsing 用专门模型做解析已是 SOTA；PRCO 用专门框架做 RL 已是 SOTA。将两者压缩到同一个 8B 模型中同时训练，容量是否足够？

【3 维度打分】:

1. **Novelty: 中偏弱** — 核心贡献是将 3 个已有组件（Geoparsing 的符号解析 + PRCO 的双角色 RL + SymHPR 的重建验证）组合成一个 pipeline，并加入 persistent scratchpad 和 integration reward。这是一个合理的系统组合，但缺乏概念层面的突破。Hilbert-Geo（May 2026）已经实现了"形式化解析 → 推理"这一核心思路并取得 SOTA；PRCO 已经实现了 Observer-Solver RL。Proposal 的独特增量在于 (i) 可验证的 Observer 和 (ii) integration reward，前者有一定新意，后者属于增量。Symbolic Grounding 论文进一步削弱了 novelty——如果符号转换本身就能 close the gap，那额外的架构复杂度的增量价值需要更强的论证。

2. **Significance: 中** — 问题本身（视觉数学推理中的 evidence collapse 和 integration failure）是重要的、被社区广泛关注的问题（Don't Blink, MathLens, CogFlow 均在 2025-2026 发表于顶会/arXiv）。但 proposal 的适用范围限于**几何图形**——符号谓词（点、线、角、关系）是几何特有的表示，难以推广到图表、函数图、统计图等其他视觉数学问题类型。这限制了贡献的普适性。预期提升 3-5 pts over PRCO 也较为保守，在 MathVista SOTA 已达 86.8% 的背景下，如果最终结果在 open-source 8B 模型上从 ~78 提升到 ~83，审稿人可能会认为这是合理但不 surprising 的改进。

3. **Related Work: 强** — 这是 proposal 最突出的优点。对领域的覆盖非常全面，包括最新的 concurrent works（Hilbert-Geo May 2026, GeoMathCode May 2026）。每篇引用的描述经验证均准确。与各竞争工作的差异化定位清晰（vs. PRCO: 可验证 vs NL caption; vs. Geoparsing: 解析+记忆+RL vs 仅解析; vs. Hilbert-Geo: RL训练 vs pipeline; vs. CoRGI: 训练时集成 vs 推理时验证）。

【概率估计】: [22% - 30%] 中位 26%

【估计理由】: Related Work 覆盖是强项，表明作者对领域有深入理解，但这主要保证了论文的"形式下限"。Novelty 是主要瓶颈——核心贡献是系统组合而非概念突破，且面临 Symbolic Grounding 论文揭示的 trivial alternative 威胁（仅做符号转换就可能获得大部分收益）。Significance 受限于几何领域的局限性和保守的预期提升。最关键的是，proposal 的核心逻辑前提（"符号谓词不衰减"）混淆了 visual token decay 和 text token attention patterns，这一漏洞如果被审稿人抓住会严重削弱立论基础。整体来看，这是一个"well-executed combination paper"，有望进入 borderline 区间，但在 idea 层面不足以让审稿人写出 "surprising"。Novelty 的中偏弱评价限制了上界。

【主要风险】:
1. **Trivial alternative 风险**：审稿人可能指出"直接 prepend 符号谓词 + 标准 CoT"就能获得类似效果（参考 Symbolic Grounding 和 Hilbert-Geo 的结果），从而质疑 persistent scratchpad + dual-role RL + integration reward 的增量价值是否值得这么大的系统复杂度。
2. **核心前提漏洞**：proposal 将 "evidence collapse"（visual token 衰减）的结论外推到所有 continuous representations，并声称 discrete predicates 天然免疫——但符号谓词作为 text tokens 参与 attention 计算时同样受长序列注意力稀释的影响。审稿人可能指出这一逻辑跳跃，动摇整个 persistent memory 的动机基础。
```

Sources:
- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/abs/2604.04207)
- [PRCO: Seeing with You](https://arxiv.org/abs/2603.28618)
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)
- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)
- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)
- [MathLens: What MLLMs Learn about Multimodal Reasoning](https://arxiv.org/abs/2510.01719)
- [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/abs/2605.16385)
- [GeoMathCode: Interleaved Math-Code Reasoning](https://arxiv.org/abs/2605.25384)
- [MathVista Leaderboard](https://mathvista.github.io/)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to make a thorough assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. **PRCO: "Seeing with You: Perception-Reasoning Coevolution" (arXiv 2603.28618, Mar 2026)**:
   最直接的竞争工作。提出 Observer-Solver 双角色 RL 框架，Observer 生成 NL caption，Solver 基于 caption 推理。平均 +7pts 提升。本 proposal 的核心设计（双角色 RL）直接继承自 PRCO，区别在于用 formal symbolic predicates 替代 NL captions。

2. **Geoparsing (arXiv 2604.11600, Apr 2026)**:
   构建 GDP-29K 数据集，SFT+RLVR 训练 formal diagram parser，达到 SOTA 几何图解析。本 proposal 的 formal parser 模块直接复用该方法。

3. **Don't Blink: Evidence Collapse (arXiv 2604.04207, Apr 2026)**:
   量化了推理 VLM 在 chain-of-thought 过程中 >50% 的 visual evidence attention loss。本 proposal 的核心 motivation 之一。但注意：该论文测量的是对**视觉 token**的注意力衰减，而非对**文本化符号谓词**的衰减。

4. **Symbolic Grounding (arXiv 2604.21346, Apr 2026)**:
   证明给 LLM 提供符号化输入（替代原始图像），抽象视觉推理从 near-chance 提升到 mid-90s。证明了符号表示的价值，但该工作是**诊断性**的（探测瓶颈在哪里），并非提出持久化记忆或 RL 训练方案。

5. **SymHPR (arXiv 2512.03126, Dec 2025)**:
   符号化自编码器 + 层级过程奖励模型，98.2% 重建保真度。本 proposal 借用其 reconstruction fidelity 作为 Observer reward 信号。

6. **CogFlow (ICLR 2026, arXiv 2601.01874)**:
   三阶段框架 perception→internalization→reasoning，用知识内化奖励桥接感知与推理。MathVista 76.8%。与本 proposal 目标相似（桥接感知-推理），但用 text-based internalization 而非 formal symbolic。

7. **MathLens (arXiv 2510.01719, Oct 2025)**:
   分解多模态推理为 perception / reasoning / integration，发现 integration 是主要失败模式，RL 主要提升 perception 而非 integration。本 proposal 的 integration reward 设计直接针对该发现。

8. **v1 (arXiv 2505.18842, May 2025)**:
   point-and-copy 机制让模型在推理过程中动态回引视觉 token。缓解 evidence decay 但无法纠正初始感知错误。

9. **Hilbert-Geo (arXiv 2605.16385, May 2026)**:
   固体几何形式语言 + Parse2Reason pipeline，但无 RL 训练、无持久记忆。功能上部分重叠。

10. **KAWHI (arXiv 2603.27375, Mar 2026)**:
    注意力加权奖励重分配，将视觉证据与推理步骤对齐，但不使用符号表示。

11. **FIGR (arXiv 2512.24297, Jan 2026)**:
    通过 RL 在推理中生成可执行代码构建图表。类似"外化中间状态"思路，但方向不同（生成新图 vs. 解析已有图为符号记忆）。

12. **GeoMathCode (arXiv 2605.25384, May 2026)**:
    交错数学-代码推理，代码作为辅助可执行表示而非持久化可查询记忆。

13. **CoRGI (arXiv 2508.00378, Aug 2025)**:
    推理后逐步视觉验证，改善幻觉。仅推理时使用，未集成到 RL 训练。

- **调研总结**: 视觉数学推理领域在 2025-2026 年极其活跃，围绕 evidence decay（Don't Blink, v1）、感知-推理桥接（PRCO, CogFlow, MathLens）、形式化图解析（Geoparsing, Hilbert-Geo）三条线并行推进。本 proposal 处于这三条线的交汇点，试图将 formal symbolic parsing + persistent memory + dual-role RL 组合为统一框架。每个组件已有成熟先例，核心贡献在于组合方式。


【Trivial Alternative 检验】:

最直接的 trivial baseline：**直接将 Geoparsing 的 formal output 拼接到 prompt 前面，让模型在推理时直接引用**（即 "parse once, prepend, then reason"）。Symbolic Grounding 论文已经证明，仅仅给 LLM 提供符号化输入就能从 near-chance 跳到 mid-90s。

这个 trivial alternative 是真实威胁。本 proposal 的增量价值在于：
- **持久化可查询记忆**：通过 predicate-matching retrieval 避免 long-context 注意力衰减。但这里有一个关键问题：Don't Blink 测量的是**视觉 token**的注意力衰减，而 symbolic predicates 一旦文本化后就是**语言 token**，是否同样受 causal attention decay 影响并不清楚。proposal 声称"discrete predicates do not degrade under causal attention"缺乏理论或实证支撑。
- **Reconstruction-based verification**：无需 ground-truth 标签就能验证 Observer 准确性。这是比 PRCO 的 NL caption 真正的改进点。
- **Integration reward**：显式优化 predicate 利用率。这是一个有意义但相对常规的 RL reward shaping 设计。

**结论**：存在明确的 trivial alternative 威胁。proposal 的增量价值主要在 reconstruction verification 和 integration reward，而非"持久化记忆"本身——因为"持久化"的必要性假设（symbolic text tokens 也会 decay）未被充分论证。


【前提假设检验】:

核心逻辑链中有**三个关键未验证假设**：

1. **"离散符号谓词在 causal attention 下不衰减"** — 这是整个架构的理论基石。但 Don't Blink 研究的是 visual token attention decay，而非 text token decay。如果符号谓词被编码为文本 token（就是普通 token），它们仍然会受到 long-context attention 稀释的影响。proposal 将 visual token 的衰减问题偷换为所有 token 的衰减问题，然后声称文本化符号 token 免疫——这一步逻辑跳跃缺乏支撑。

2. **重建保真度能充当可靠的 Observer reward** — re-render predicates 并与原图比较，能否检测所有类型的解析错误？几何关系可能在重建中"看起来正确"但丢失了微妙的空间语义（例如角度近似、比例关系）。SymHPR 报告 98.2% fidelity，但这是在其受控数据上的表现，迁移到更复杂的 real-world diagrams 时是否保持，是未知的。

3. **3-5 point gains over PRCO 是可实现的** — MathVista SOTA (o3) 是 86.8%，open-model SOTA (Qwen3-VL) 85.8%，PRCO 在 base model 上 +7pts。在已接近 ceiling 的情况下，再获 3-5pts 增量（且只在几何子集上有效的方法）是非常困难的。


【3 维度打分】:

1. **Novelty: 弱-中 (偏弱)** — 核心贡献是 PRCO（双角色 RL）+ Geoparsing（formal parsing）+ SymHPR（reconstruction verification）+ 持久记忆的**系统性组合**。每个组件都有直接先例。组合本身是**自然的 next step**：任何同时读过 PRCO、Geoparsing、Don't Blink 三篇论文的研究者都会想到"用 formal symbolic parsing 替代 PRCO 的 NL Observer 并维持 persistent memory"。Hilbert-Geo (May 2026) 已经在做 formal parsing + reasoning pipeline（只是没有 RL）；FIGR 已经在做推理过程中外化中间状态（只是用代码而非符号谓词）。在如此密集的竞争格局下，"组合 novelty"的存活空间有限。Reconstruction verification 作为 Observer reward 是相对最新颖的子贡献，但单独来看偏 incremental。

2. **Significance: 中** — 问题本身（evidence collapse + integration failure）是重要且有文献支撑的。但 proposal 的方法**高度 geometry-specific**：formal parsers（Geoparsing, FormalGeo）仅覆盖几何图，不适用于 MathVista 中的函数图、表格、统计图等其他视觉数学类型。这严重限制了方法的泛化性。如果方法只在几何子集上有效，对整个 visual math reasoning 领域的影响有限。此外，3-5pts 的预期增量在 ceiling 效应下属于 marginal improvement。

3. **Related Work: 强** — 对近期工作的覆盖非常全面且准确。所有引用论文均经验证真实存在，描述与实际内容匹配度高。差异化定位清晰——对每个 concurrent work 都明确说明了 proposal 的区别（Hilbert-Geo: 无 RL/persistent memory; KAWHI: 无符号表示; GeoMathCode: code as auxiliary; CoRGI: inference-only）。MathLens → integration reward 的 motivation chain 特别有说服力。这是 proposal 最强的维度。


【概率估计】: [22% - 32%] 中位 27%

【估计理由】:
- Related Work 维度强，说明作者对领域有深度理解，但这提升的是执行质量的下限，不改变 idea 上限。
- Novelty 偏弱是主要瓶颈：核心贡献是已有组件的 natural combination，审稿人大概率会写 "the contribution is primarily in combining existing techniques" 或 "incremental over PRCO + Geoparsing"。这直接限制了概率上界。
- Significance 受限于 geometry-specific 性质和 ceiling 效应，进一步压缩了概率。
- 如果核心实验结果 positive（3-5pts gain），审稿人的反应更可能是 "makes sense, I would have expected formal representations to help" 而非 "surprising"——这将 idea 定位在 25-35% 区间的下半段。
- 前提假设中"symbolic text tokens 不衰减"的逻辑漏洞如果被审稿人抓住，可能成为致命伤。

【主要风险】:
1. **"Systems combination" novelty 不足**：每个组件（formal parsing, dual-role RL, reconstruction reward, persistent memory）都有直接先例，组合方式是 natural next step，审稿人可能判定 novelty 不够 AAAI main conference 的门槛。
2. **核心理论假设有逻辑漏洞**：proposal 将 Don't Blink 发现的 visual token decay 外推为"所有 evidence 都会 collapse"，然后声称 symbolic text tokens 免疫——这一推理链条中间有跳跃，如果审稿人追问"为什么 symbolic predicates 作为 text tokens 就不会在 long context 中被忽略"，proposal 目前无法给出有力回应。
```

Sources:
- [Don't Blink: Evidence Collapse during Multimodal Reasoning](https://arxiv.org/pdf/2604.04207)
- [PRCO: Seeing with You: Perception-Reasoning Coevolution](https://arxiv.org/abs/2603.28618)
- [Geoparsing: Diagram Parsing for Plane and Solid Geometry](https://arxiv.org/abs/2604.11600)
- [Symbolic Grounding Reveals Representational Bottlenecks](https://arxiv.org/abs/2604.21346)
- [SymHPR: Hierarchical Process Reward Models are Symbolic Vision Learners](https://arxiv.org/abs/2512.03126)
- [CogFlow: Bridging Perception and Reasoning through Knowledge Internalization](https://arxiv.org/abs/2601.01874)
- [MathLens: What MLLMs Learn about Multimodal Reasoning](https://arxiv.org/abs/2510.01719)
- [v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning](https://arxiv.org/abs/2505.18842)
- [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/abs/2605.16385)
- [KAWHI: Bridging Visual Representation and RLVR](https://arxiv.org/abs/2603.27375)
- [FIGR: Figure It Out - Executable Visual States](https://arxiv.org/abs/2512.24297)
- [GeoMathCode: Understanding Interleaved Math-Code Reasoning](https://arxiv.org/abs/2605.25384)
- [CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding](https://arxiv.org/abs/2508.00378)
- [MathVista Leaderboard](https://mathvista.github.io/)


【原始 proposal（允许参考但不是主要依据）】:
# Verifiable Symbolic Memory Prevents Evidence Collapse in Visual Math

## Core Problem

Multi-step visual mathematical reasoning suffers from evidence collapse (>50% visual attention loss during chain-of-thought) and cross-modal integration failure (the dominant error mode even as perception and reasoning independently improve), because models encode diagrams once into continuous embeddings that progressively decay under causal attention masking.

## Research Opportunity

Recent formal diagram parsers (Geoparsing Apr 2026, SymHPR Dec 2025) achieve SOTA conversion of diagrams into verifiable symbolic predicates, and the Symbolic Grounding paper (Apr 2026) proves that symbolic representations close the vision-reasoning gap entirely (near-chance → mid-90s). Yet no work uses these formal representations as persistent, queryable, step-level memory during reasoning — they are consumed once then forgotten. Meanwhile, the best integration method (PRCO, Mar 2026) still uses unverifiable NL captions as the perception-reasoning bridge, leaving a clear opportunity to combine formal symbolic parsing with dual-role RL training to simultaneously solve evidence collapse and integration failure.

## Research Landscape

Current MathVista SOTA is o3 at 86.8%; open models like Qwen3-VL reach 85.8% and Step3-VL-10B reach 84.0%. PRCO (Mar 2026) achieves +7pts average via an NL Observer-Solver RL framework but cannot independently verify observer accuracy. CogFlow (ICLR 2026) models perception→internalization→reasoning as three stages achieving 76.8% MathVista, but uses text-based (not formally verifiable) internalization. Geoparsing (Apr 2026) achieves SOTA formal diagram parsing for plane+solid geometry via SFT+RLVR; SymHPR (Dec 2025) demonstrates self-supervised symbolic auto-encoding at 98.2% reconstruction fidelity. Don't Blink (Apr 2026) quantifies >50% evidence mass loss during reasoning, and v1 (May 2025) mitigates decay via visual-token re-attention but cannot correct initial perception errors. MathLens (2025) shows integration remains the principal failure mode as perception and reasoning improve — RL predominantly improves perception while integration lags regardless of pretraining. Concurrent: Hilbert-Geo (May 2026) proposes a formal language for solid geometry with a Parse2Reason pipeline but uses no RL training or persistent memory; KAWHI (Mar 2026) bridges visual representation with RLVR via attention-based reward reweighting but does not employ symbolic representations; GeoMathCode (May 2026) interleaves math-code reasoning but code serves as auxiliary executable representation rather than persistent queryable symbolic memory; CoRGI (2025) performs post-hoc step-wise visual verification but is inference-only and not integrated into RL training.

## Proposed Approach

Train a formal symbolic parser on Qwen3-VL-8B using Geoparsing's SFT+RLVR recipe over GDP-29K and FormalGeo data, converting visual diagrams into a structured set of verifiable symbolic predicates (points, lines, angles, relations) stored in a persistent symbolic scratchpad. Replace PRCO's natural-language Observer with a formal Observer that outputs symbolic predicates verified via SymHPR-style reconstruction fidelity (re-render predicates and compare against the original diagram), while the Solver queries this symbolic scratchpad at each chain-of-thought step through predicate-matching retrieval — preventing evidence decay by design since discrete predicates do not degrade under causal attention. Train both roles jointly using dual-objective RL: the Observer receives reconstruction-verification rewards (computable without ground-truth labels), the Solver receives outcome-correctness rewards, and an auxiliary integration reward measures symbolic predicate utilization across reasoning steps to explicitly optimize the perception-reasoning bridge that MathLens identifies as the dominant failure mode. Evaluate on MathVista, MathVerse, GeoQA, and WeMath, with ablations isolating the contributions of formal parsing, persistent memory, and the integration reward.

## Detailed Description

We propose SymMem, a method that converts visual diagrams into formally verifiable symbolic predicates and maintains them as a persistent, queryable scratchpad throughout multi-step mathematical reasoning. Current approaches either parse diagrams into formal representations consumed once then discarded (Geoparsing, Hilbert-Geo), or use unverifiable natural-language captions as the perception-reasoning bridge (PRCO, CogFlow). Our key insight is that discrete symbolic predicates are inherently immune to the evidence collapse phenomenon (>50% attention loss quantified by Don't Blink) that plagues continuous embeddings under causal attention. We build on Qwen3-VL-8B and train a formal Observer via SFT+RLVR that outputs structured geometric predicates verified through reconstruction fidelity (re-rendering and comparing against source diagrams, following SymHPR). A Solver queries this symbolic memory at each reasoning step via predicate-matching retrieval. Dual-role RL jointly optimizes the Observer (reconstruction reward) and Solver (outcome reward), with an explicit integration reward measuring predicate utilization across steps — directly targeting the integration failure mode identified by MathLens as the dominant bottleneck. We target MathVista, MathVerse, GeoQA, and WeMath, expecting 3–5 point gains over PRCO baselines.

## Key References

- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning (arXiv 2026)
- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)
- Hierarchical Process Reward Models are Symbolic Vision Learners (arXiv 2025)
- Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv 2026)
- Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning (arXiv 2026)
- v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning (arXiv 2025)
- What MLLMs Learn about When they Learn about Multimodal Reasoning: Perception, Reasoning, or their Integration? (arXiv 2025)
- CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving (ICLR 2026)
- Mitigating Visual Forgetting via Take-along Visual Conditioning for Multi-modal Long CoT Reasoning (ACL 2025)
- Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models (arXiv 2026)
- CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding (arXiv 2025)
- STEP3-VL-10B Technical Report (arXiv 2026)
- Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning (arXiv 2026)

## Resource Estimate

- **manual**: gpu_hours: 500–650 H100-hours (Phase 1 formal parser SFT: ~120h on 8×H100; Phase 2 reconstruction verifier: ~60h; Phase 3 dual-role RL: ~300h; Phase 4 evaluation + ablations: ~80h), timeline: 12–14 weeks (2 wks parser data curation, 2 wks parser SFT+RLVR, 2 wks verifier, 4 wks dual-role RL tuning, 2–4 wks eval+writing), estimated_gpu_cost: $1,250–$1,625 at $2.50/hr spot H100
- **human_in_loop**: gpu_hours: 400–550 H100-hours (Claude assists with reward function design, data augmentation, hyperparameter search space, ablation analysis), timeline: 8–10 weeks, claude_api_cost: $150–$250 (experiment orchestration, code generation for symbolic parser integration, result analysis with Sonnet 4.6), estimated_gpu_cost: $1,000–$1,375 at $2.50/hr spot H100
- **auto_research**: gpu_hours: 600–800 H100-hours (wider hyperparameter sweeps, automated ablation matrix, additional dataset variants), timeline: 5–7 weeks (parallelized experiment execution), claude_api_cost: $400–$600 (continuous experiment monitoring, automated code repair, paper drafting assistance), estimated_gpu_cost: $1,500–$2,000 at $2.50/hr spot H100, speed_bottleneck: Reward function design for symbolic reconstruction verification requires human judgment on geometric consistency metrics; RL training loop debugging for dual-role credit assignment is poorly suited to full automation; symbolic parser failure modes on out-of-distribution diagrams need expert inspection


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8d3bd7bf-d293-4813-bdb4-fd316048c868",
  "type": "user",
  "uuid": "82b83a12-528f-4c32-bb1f-69e8beb2ae6d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T22:56:39.144Z_

```json
{
  "parentUuid": "82b83a12-528f-4c32-bb1f-69e8beb2ae6d",
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
  "uuid": "1aee5ff4-51c4-4e8b-a5b2-a03976dad618",
  "timestamp": "2026-05-27T22:56:39.144Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T22:56:39.144Z_

```json
{
  "parentUuid": "1aee5ff4-51c4-4e8b-a5b2-a03976dad618",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e8d232f0-746e-43c8-b728-9e9866185154",
  "timestamp": "2026-05-27T22:56:39.144Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ I now have comprehensive field knowledge. Let me compile my ev…",
  "leafUuid": "e8d232f0-746e-43c8-b728-9e9866185154",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate visual math reasoning proposal with meta-judgment",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75"
}
```

---

### Assistant

_source line 8 · 2026-05-27T22:57:06.076Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as Meta Judge.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 26%

**Reviewer 2:**
- Novelty: 中偏弱
- Significance: 中
- Related Work: 强
- Probability: [22% - 30%] 中位 26%


**Reviewer 3:**
- Novelty: 弱-中 (偏弱)
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 27%

The three median probabilities are remarkably consistent at 26%, 26%, and 27%, with almost no variation. Computing the mean across these three values gives me 26.33%, and the standard deviation is negligible at around 0.47%.

Looking at where the reviewers align, there's strong consensus across all three on novelty being weak-to-medium, significance being medium, and related work coverage being strong. They also all identified the same potential threat—using prepended symbolic predicates as a baseline alternative.

Beyond that, there's agreement on several critical gaps: the evidence collapse logic flaw where the proposal extrapolates from visual token decay studies to text tokens without justification, reconstruction fidelity concerns on real-world diagrams, and the risk of reward hacking through integration rewards in the RL setup. Both R2 and R3 flag the geometry-specific limitation explicitly, while R1 frames it as a domain constraint. All three converge on the core issue that this is more of a systems combination than a conceptual breakthrough.

R3 goes deeper into related work, covering v1, KAWHI, FIGR, and CoRGI in more detail, while R1 raises additional concerns about persistent visual aspects.

Looking at the implementation feasibility, the proposal estimates 500-800 H100-hours of compute, relies on publicly available datasets like GDP-29K and FormalGeo, and requires human involvement mainly in reward function design and RL debugging. The training involves both SFT and RLVR for the parser plus dual-role RL for the Observer-Solver components, with a timeline of 5-14 weeks depending on automation. Given how tightly the reviewers align on these points—the standard deviation is essentially negligible—I should anchor to the median assessment and tighten my confidence interval accordingly.

The consensus clusters around 26-27%, so I'll set my final estimate at 26% with a range of 22-30%. This falls below the 36% threshold, putting it in the "not recommended" or "marginal-to-low" category.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d232f0-746e-43c8-b728-9e9866185154",
  "isSidechain": false,
  "requestId": "req_011CbTu8an6LfGwd4b4KDY1E",
  "type": "assistant",
  "uuid": "95a8b440-4720-49fd-9037-6ccc93f7e3a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqmNaTftsZhr4Esf44Busa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21118,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2805,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2805,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21118
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

_source line 9 · 2026-05-27T22:57:49.552Z_

【阶段】: Meta Judge
【三次中位】: [26%, 26%, 27%]  std=0.5%
【共识维度】: 
- **Novelty: 弱-中**（3/3 一致）— 核心贡献是已有组件（Geoparsing formal parsing + PRCO dual-role RL + SymHPR reconstruction verification）的系统性组合，每个组件有直接先例，组合方式是 natural next step。Integration reward 是最具新意的子贡献但分量有限。
- **Significance: 中**（3/3 一致）— 问题本身重要且 timely，但方法高度 geometry-specific，无法推广到 charts/plots/统计图等其他视觉数学类型；3-5pts 预期增量在 ceiling 效应下属 marginal improvement。
- **Related Work: 强**（3/3 一致）— 对近期文献覆盖全面准确，差异化定位清晰，是 proposal 最突出的优点。
- **Trivial Alternative 威胁: 致命级**（3/3 一致）— Symbolic Grounding (Apr 2026) 已证明仅将 diagram 转为 symbolic text 即可从 near-chance 跃升至 mid-90s；"parse once, prepend, then reason" 这个零架构改动的 baseline 可能捕获 SymMem 大部分收益，使 persistent memory + dual RL + integration reward 的增量价值存疑。
- **核心前提逻辑漏洞: 致命级**（3/3 一致）— Don't Blink 量化的 evidence collapse 是 visual token 特有现象；symbolic predicates 一旦文本化就是普通 text tokens，天然存在于 KV cache 中，不受 visual token 衰减机制影响。Proposal 将 visual token decay 外推为"所有 evidence 都会 collapse，只有 discrete predicates 免疫"这一逻辑跳跃缺乏理论或实证支撑，若审稿人追问则核心 motivation 动摇。
- **Reconstruction fidelity 鲁棒性存疑**（3/3 提及）— SymHPR 的 98.2% fidelity 是受控数据上的表现，迁移到手绘/非标准/遮挡等 real-world diagrams 时鲁棒性未经验证。
- **Integration reward 的 reward hacking 风险**（2/3 明确提及，R3 隐含）— predicate utilization 是 proxy metric，高利用率≠正确整合，低利用率可能反而合理。

【异常维度】: 
- R2 独提"8B 模型容量是否足以同时支撑 formal parsing + reasoning + RL 三重任务"— 合理关切但属实施层面，非 idea 层面致命问题，降权处理。
- R1 独提 Persistent Visual Memory (arXiv 2605.00814) 作为额外竞争者 — 该工作用连续 embedding 非 symbolic，与 proposal 方法不同，不构成额外威胁，降权。

【最终概率】: [22% - 30%] 中位 26%
【一致性】: 高（std=0.5%，三位审稿人在所有 rubric 维度上判决完全一致）
【综合理由】: 三位审稿人在所有关键维度上达成了罕见的高度一致：Novelty 弱-中、Significance 中、Related Work 强，且均独立识别出相同的两个致命风险（trivial alternative + evidence collapse 逻辑漏洞）。在 std < 1% 的极高一致性下，取中位附近并缩窄区间。概率上限由 Novelty 限制——核心贡献是 systems combination 而非 conceptual breakthrough，且面临"仅 prepend symbolic text 就够了"的 trivial alternative 致命威胁，两个致命级风险叠加使得概率难以突破 30%。概率下限由 Related Work 的强覆盖和 integration reward 的合理性托底，不至于跌破 20%。中位 26% 反映了"well-executed combination paper with a logical flaw in its core claim"的定位，处于 AAAI reject 区间的上部。无异常审稿人需要处理，无需人工复核。

【建议】: 边缘（偏不推荐）— 中位 26% 低于 36% 通过线，但 idea 并非完全不可抢救。核心需要：(1) 重构 motivation，放弃"evidence collapse"叙事，转向"verifiable perception + integration optimization"叙事；(2) 在实验中加入 trivial baseline（prepend-only）并证明显著增量。如果这两点做不到，建议 KILL。

【实施评估】:
  - 计算资源: 500-800 H100-hours（约 $1,250-$2,000 spot price），分 4 阶段：formal parser SFT ~120h、reconstruction verifier ~60h、dual-role RL ~300h、evaluation+ablation ~80h。需 8×H100 节点。
  - 数据需求: GDP-29K（公开）、FormalGeo 数据集（公开）、MathVista / MathVerse / GeoQA / WeMath（均为公开 benchmark）。无需额外数据收集。
  - 人工介入: 中等。reconstruction verification 的 metric 设计需人工判断几何一致性标准；RL reward function 的 dual-role credit assignment 调试需专家经验；symbolic parser 在 out-of-distribution diagrams 上的 failure mode 需人工检查。
  - 训练需求: 需要模型训练。基于 Qwen3-VL-8B，先 SFT+RLVR 训练 formal parser，再 dual-role RL 联合训练 Observer+Solver。8B 规模模型，总训练时长约 480-600 H100-hours。
  - 新 Benchmark: 不需要。使用现有公开 benchmark。
  - 预估周期: 8-14 周（取决于自动化程度），含 2 周数据准备、2 周 parser 训练、2 周 verifier、4 周 RL 调优、2-4 周评测和写作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95a8b440-4720-49fd-9037-6ccc93f7e3a7",
  "isSidechain": false,
  "requestId": "req_011CbTu8an6LfGwd4b4KDY1E",
  "type": "assistant",
  "uuid": "3aee1014-5f15-4334-bf86-13fa8f593cf9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqmNaTftsZhr4Esf44Busa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21118,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2805,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2805,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21118
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ I now have comprehensive field knowledge. Let me compile my ev…",
  "leafUuid": "3aee1014-5f15-4334-bf86-13fa8f593cf9",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate visual math reasoning proposal with meta-judgment",
  "sessionId": "c4a69647-f298-44eb-bf56-636a42ff4e75"
}
```

---
