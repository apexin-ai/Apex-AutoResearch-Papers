# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/919dcc97-f2f3-4370-8b57-04d58b699071.jsonl`
- **Structured JSON:** [`78bd9c0b6e672fcdcd63.json`](../../sessions/78/78bd9c0b6e672fcdcd63.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T06:05:40.105Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T06:05:40.105Z",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **TTRL (NeurIPS 2025, arXiv:2504.16084)**: 提出在无标签数据上用 majority voting 作为伪奖励进行 test-time RL，在 informal 数学推理上取得显著提升。但仅适用于有唯一数值答案的场景，不直接适用于形式化陈述（无法 majority vote）。\n\n2. **DDRL (ACL 2026 Findings, arXiv:2604.21327)**: 识别并修复 GRPO 在 unsupervised 设置下的 spurious signal amplification，提出 balanced sampling + fixed advantages + consensus off-policy refinement。但明确限于 binary rewards，论文自身将 \"multi-tier reward\" 列为 future work。确认存在。\n\n3. **GDPO (NVIDIA, arXiv:2601.05242)**: 发现 GRPO 在 multi-reward 设置下将不同 reward 组合 normalize 到相同 advantage 值，导致信息坍缩。提出 per-reward decoupled normalization。与 DDRL 解决的是不同问题（debiasing vs multi-reward resolution），确认两者未被统一。\n\n4. **CriticLean (arXiv:2507.06181, ByteDance/Nanjing)**: CriticLeanGPT-14B-RL 在 balanced CriticLeanBench 上达 84.8% 准确率。模型已开源（HuggingFace: m-a-p/CriticLeanGPT-Qwen3-14B-RL）。论文聚焦于 critic 训练和 benchmark 构建，未探索将 CriticLean 作为 TTRL 的 reward 信号。确认存在。\n\n5. **FormaRL (COLM 2025, arXiv:2508.18914)**: 使用 GRPO + compilation reward + LLM consistency check，在 ProofNet 上 pass@1 从 4.04% 提升至 26.15%。但是 training-time RL，非 test-time adaptation。确认存在。\n\n6. **Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop)**: 使用 GRPO + BEq + embedding similarity，training-time。TC1: 17.29%→26.01%。无 retrieval，无 test-time adaptation。确认存在。\n\n7. **Aria (ICLR 2026, arXiv:2510.04520)**: 当前 retrieval-augmented autoformalization 的 SOTA。通过 dependency graph + iterative formalization + AriaScorer 在 ProofNet 上达 91.6% compilation / 68.5% accuracy，homological conjectures 上达 42.9%。关键局限：retriever 是 static 的，不随 formalizer 行为变化而适应。确认存在，确认 ICLR 2026 poster。\n\n8. **DDR (arXiv:2511.11990)**: 构建 500K 依赖检索数据集，将 Hall_m 从 0.21-0.39 降至 <0.02。验证了 identifier hallucination 是重要错误源且 retrieval 可大幅降低。确认存在。\n\n9. **R3 (NeurIPS 2025, arXiv:2510.24652)**: 通过 reinforced contrastive learning 优化 RAG retriever，在通用 QA 任务上验证了 co-adaptive retrieval 可行。未应用于 autoformalization。确认存在。\n\n10. **FormalEvolve (arXiv:2603.19828)**: 将 autoformalization 建模为 budgeted evolutionary search，SH@100=58.0% CombiBench / 84.9% ProofNet。搜索固定模型输出空间，无权重更新，不利用编译错误结构。确认存在。\n\n11. **MathAtlas (arXiv:2605.14061, May 2026)**: 52K graduate-level problems，best baseline 在 MA-Hard 上仅 2.6%。含 178K dependency relations。确认存在，确认其极高难度。\n\n12. **TEMPO (arXiv:2604.19295, Apr 2026)**: 将 TTT 形式化为 EM 过程，证明 omitting critic recalibration 导致 ELBO 退化。OLMO3-7B AIME 2024: 33.0%→51.1%。概念上与 TTRA 的 dual-loop 有平行关系。确认存在。\n\n13. **AMBER / Construction-Verification (arXiv:2602.01291)**: 对 DeepSeek-R1 在 applied math 上的 3189 个编译错误分类，47.3% 为 identifier hallucination。确认存在。\n\n14. **Reinforced Co-adaptation Framework (arXiv:2602.22584)**: 工业 RAG 中通过 GRPO + multi-dimensional rewards 联合优化 retrieval 和 generation，减少 72% hallucination。验证 co-adaptive RAG 方向可行，但在 FAQ/客服场景，非形式化数学。\n\n- **调研总结**: Autoformalization 领域 2025-2026 年处于快速发展期。RL for autoformalization（FormaRL、Wang et al.）、retrieval-augmented autoformalization（Aria、DDR、DRIFT）、test-time RL（TTRL）、co-adaptive retrieval（R3、Reinforced-IR）分别是活跃的研究线。但这四条线尚未交叉：(a) 现有 RL for autoformalization 均为 training-time；(b) 现有 retrieval-augmented autoformalization 均用 static retriever；(c) 现有 TTRL 均面向 informal reasoning 的 binary reward；(d) 现有 co-adaptive retrieval 未应用于 Lean 4。Proposal 的定位——在这四条线的交叉点上——是一个真实存在的 gap。\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative 是 **Best-of-N sampling + CriticLean filtering + static DDR retrieval**：给定同等 test-time compute，从 base formalizer（如已 SFT/RL 训练好的模型）采样大量候选，用 DDR 做 static retrieval 增强，然后用 CriticLean 过滤。这不需要 test-time 权重更新，也不需要 co-adaptive retrieval。\n\nProposal 的增量价值在两处：\n1. **Weight adaptation**：当模型的 output space 根本不包含正确的 OOD formalization 时（MathAtlas MA-Hard 2.6%），任何 inference-time scaling 都无法找到不存在的解。这个论点在概念上成立，但实证强度取决于 OOD 程度——如果 pass@128 或 pass@512 仍然很低，才能证明 weight adaptation 是必要的。\n2. **Co-adaptive retrieval**：static retriever 无法跟踪 formalizer 在 TTRL 过程中行为的漂移。但这个论点有一个隐含假设：formalizer 在 50-200 步 TTRL 后行为漂移足够大，以至于 static retriever 的 recall 显著下降。这一点未被验证。\n\n**结论**：Trivial alternative 威胁是 **中等** 的。在 near-OOD 场景下，Best-of-N + static RAG + CriticLean filtering 可能已经足够好。增量价值主要体现在 far-OOD 场景（如 MA-Hard），前提是 inference-time scaling 确实触顶。Proposal 意识到了这一点并包含了 compute-matched baseline，这是正确的。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条包含以下未经验证的假设：\n\n1. **\"Lean 4 的 unknownIdentifier 错误可以作为 oracle-quality retrieval training signal\"** — 这是整个 co-adaptive retrieval 的基石。概念上合理（错误确实指名缺失的 identifier），但实际有两个子假设：(a) 错误中提到的 identifier 确实对应 Mathlib 中可检索的常量（而非 locally-defined 变量或 model 自创的名字），(b) 基于这些 positives/negatives 的 InfoNCE 训练在仅 ~240 对/cycle 的信号密度下能有效更新 retriever。假设 (a) 的 Phase -1 micro-analysis 是合理的验证手段；假设 (b) 的低数据量下 contrastive learning 效果存疑。\n\n2. **\"CriticLean 在 OOD + 严重 class imbalance (<10% compilable) 下仍可用\"** — CriticLean 训练于 balanced 250/250 distribution，在 <10% compilable 的 TTRL distribution 下 precision 可能大幅下降（误将错误 formalization 判为正确）。Phase 0 calibration 是必要的，但如果 precision 不过关，整个 reward structure 需要大幅调整。这是一个 **高风险假设**。\n\n3. **\"Binarize-then-enrich 保留 DDRL 的 debiasing 性质\"** — 先 binarize（compilation AND critic），然后在 accepted candidates 中加 BEq enrichment。DDRL 的理论分析基于 binary reward 的特定结构；加入连续的 enrichment 是否破坏 debiasing 性质未被分析。这是一个 **中等风险假设**。\n\n4. **\"TTRL 过程中 formalizer 行为漂移足以使 static retriever 失效\"** — 这是 co-adaptive retrieval 必要性的前提。在 TTRL 的典型步数（几百步）内，8B 模型的权重更新幅度是否足以改变 retrieval 需求模式是未知的。如果漂移很小，co-adaptive retrieval 的增量价值就很小。\n\n5. **\"Compilation success rate 在 OOD TTRL 中能从极低 baseline 逐步上升\"** — 如果 MA-Hard 的 pass@32 在 TTRL 初期接近 0%，GRPO 几乎收不到 positive signal，可能无法启动学习。Curriculum（Phase 4）部分缓解了这一问题，但 cold-start 风险仍在。\n\n【3 维度打分】:\n\n1. **Novelty: 中（偏强）** — \n   核心 novelty 在于识别并利用 formal language 与 informal reasoning 之间的 **结构性不对称**：Lean 4 的编译错误提供了 oracle-quality、token-level 的 retrieval training signal，这在 informal reasoning 中不存在。这一 insight 是 **genuinely novel** 的——R3 (NeurIPS 2025) 和 Reinforced-IR (ACL 2025) 验证了 co-adaptive retrieval 的可行性，但未在 formal language setting 中利用编译器反馈作为 retrieval signal；Aria (ICLR 2026) 和 DDR 做了 retrieval for autoformalization 但 retriever 是 static 的；FormaRL (COLM 2025) 和 Wang et al. 做了 RL for autoformalization 但在 training time 且无 retrieval adaptation。四条研究线的交叉点确实是空白。\n   \n   然而，novelty 的限制在于：(a) 这本质上是一篇 **combination paper**——将 DDRL + GDPO + CriticLean + R3/Reinforced-IR 的既有技术应用到新 domain，每个组件的技术贡献是 adaptation 而非 invention；(b) \"binarize-then-enrich\" 虽填补了 DDRL 论文自述的 future work，但技术深度有限——它是一个 two-layer heuristic 而非有理论支撑的 principled solution；(c) 核心发现如果 positive（\"利用结构化反馈比 binary 反馈好\"），审稿人可能会说 \"intuitive, not surprising\"。\n\n2. **Significance: 中** — \n   研究问题本身重要：OOD autoformalization 是实用化形式化数学的关键瓶颈（MathAtlas MA-Hard 2.6% 说明 SOTA 几乎无法处理 graduate-level math）。如果 TTRA 在 far-OOD 上显著提升（如从 2.6% 到 8-10%），这将是有意义的进展。\"Test-time learning as a third scaling axis for formal math\" 的 framing 也有启发价值（与 TEMPO 的 EM 视角互补）。\n   \n   但 significance 受限于：(a) autoformalization 目前仍是一个 **相对 niche** 的子领域，对 broader AI community 的直接影响有限；(b) 方法的可推广性存疑——co-adaptive retrieval via compiler error 是 formal language 特有的，不易迁移到其他 domain；(c) 即使所有组件 work，绝对性能提升可能仍然有限（far-OOD autoformalization 的天花板可能本身很低）。\n\n3. **Related Work: 强** — \n   这是 proposal 最强的维度。覆盖了截至 May 2026 的几乎所有相关工作：RL for autoformalization (FormaRL, Wang et al., ReForm)、retrieval-augmented autoformalization (Aria, DDR, DRIFT, CRAMF, ProofBridge)、TTRL 及其改进 (DDRL, GDPO, T³RL, SCOPE)、semantic critics (CriticLean)、test-time compute (FormalEvolve, TEMPO)、error analysis (AMBER)。每篇工作的差异化定位清晰。对 R3、Reinforced-IR、TTARAG 的 co-adaptive retrieval 线引用准确。我调研中发现的所有关键论文均已被覆盖。唯一可补充的是 Reinforced Co-adaptation Framework (arXiv:2602.22584) 作为工业 RAG 中 co-adaptive 的额外验证。\n\n【概率估计】: [23% - 33%] 中位 27%\n\n【估计理由】: \nIdea 的核心 insight（formal language 的结构化编译反馈可作为 co-adaptive retrieval 的 oracle-quality training signal）是 genuinely novel 且 well-motivated 的，支撑了概率下界不低于 23%。Related work 覆盖极为充分，差异化定位清晰。\n\n但概率受到三方面限制：\n- **Novelty 的 \"combination\" 性质限制了上界**：四个组件（co-adaptive retrieval + CriticLean reward + DDRL debiasing + GDPO multi-reward）中每个的技术贡献都是 adaptation-to-new-domain 而非 fundamental innovation。AAAI 审稿人可能认为这是 \"well-engineered integration\" 而非 \"conceptual breakthrough\"。\n- **\"Surprising\" 检验未通过**：核心发现如果 positive（\"利用编译器结构化反馈比 binary feedback 好\"），这是 intuitive 而非 surprising 的。审稿人不太会写 \"I would not have expected this\"。\n- **系统复杂度过高**：4 phases、dual loops、multi-tier rewards、curriculum learning、多个 go/no-go gates——这些增加了实现可靠性，但也让 paper 读起来像 systems paper 而非 idea paper。在 AAAI 这样的综合会议上，过于复杂的 pipeline 可能被要求 \"simplify and focus on the core contribution\"。\n\n中位 27% 反映了：idea 方向正确、gap 真实存在、but 核心发现偏 incremental、combination nature 是主要扣分项。\n\n【主要风险】:\n1. **Combination paper 风险**：审稿人可能认为将 DDRL + GDPO + CriticLean + R3 组合应用到 autoformalization 是 engineering integration 而非 scientific contribution——\"the whole is not greater than the sum of its parts\"。每个组件的技术深度不足以独立支撑论文，但组合在一起又过于复杂。\n2. **Core finding 缺乏 surprise**：如果实验结果是 \"structured feedback > binary feedback\" 且 \"adaptive retrieval > static retrieval\"，审稿人可能会说 \"I would have guessed this, the interesting question is by how much, and the margin might not be large enough to justify the complexity\"。\n```\n\nSources:\n- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)\n- [DDRL: Understanding and Mitigating Spurious Signal Amplification in Test-Time RL](https://arxiv.org/html/2604.21327)\n- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242)\n- [CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization](https://arxiv.org/abs/2507.06181)\n- [CriticLeanGPT-Qwen3-14B-RL on HuggingFace](https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL)\n- [FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)](https://arxiv.org/abs/2508.18914)\n- [Aria: An Agent For Retrieval and Iterative Auto-Formalization (ICLR 2026)](https://arxiv.org/abs/2510.04520)\n- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)\n- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652)\n- [FormalEvolve: Neuro-Symbolic Evolutionary Search for Autoformalization](https://arxiv.org/abs/2603.19828)\n- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)\n- [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/abs/2604.19295)\n- [Towards Faithful Industrial RAG: Reinforced Co-adaptation](https://arxiv.org/abs/2602.22584)\n- [Online Reinforcement Learning for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)\n- [AMBER: Construction-Verification Benchmark](https://arxiv.org/abs/2602.01291)\n- [GDPO Explained (AI Papers Academy)](https://aipapersacademy.com/gdpo/)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research data. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- TTRL (arXiv:2504.16084, NeurIPS 2025): 奠基性工作，在无标注数据上用 majority voting 做 pseudo reward 驱动 RL，Qwen-2.5-Math-7B 在 AIME 2024 上 pass@1 提升约 211%。仅适用于有明确数值答案的 informal math，不处理 formal statement。\n- DDRL (arXiv:2604.21327, ACL 2026 Findings): 发现 GRPO 在低共识域放大 spurious reward，提出频率平衡采样 + 固定 ±1 advantage + consensus off-policy refinement。明确指出\"更丰富的 advantage 公式\"为 future work，仅处理 binary reward。确认 proposal 对其描述准确。\n- CriticLean (arXiv:2507.06181, 2025): 训练 CriticLeanGPT 模型判断 Lean 4 formalization 的语义正确性，14B-RL 在 balanced CriticLeanBench 上 84.8%。开源模型在 HuggingFace 可用。Proposal 对其 balanced vs. skewed 分布差异的担忧是合理的。\n- R3 (arXiv:2510.24652, NeurIPS 2025): 用 RL 环境反馈训练 retriever 的 contrastive learning，1-shot accuracy 平均 +5.2%。验证了\"RAG 环境反馈可训练 retriever\"这一前提。\n- Reinforced-IR (ACL 2025): 交替 RLRF/RLGF 实现 retriever-generator 共适应。验证了 co-adaptive retrieval 的可行性。\n- Aria (arXiv:2510.04520, ICLR 2026): 当前 retrieval-augmented autoformalization 的 SOTA，ProofNet 91.6% compilation / 68.5% accuracy，dependency graph + iterative formalization。关键局限：静态 pipeline，retriever 不随 formalizer 演化而更新，模型权重不更新。\n- FormaRL (COLM 2025): GRPO + compilation + LLM consistency reward 用于 autoformalization，pass@1 4%→26% on ProofNet。Training-time RL，无 retrieval，无 test-time adaptation。\n- FormalEvolve (arXiv:2603.19828, 2026): 将 autoformalization 建模为 budgeted evolutionary search，SH@100=58.0% CombiBench。Test-time compute 但无 weight adaptation，丢弃 compilation error 结构。\n- TEMPO (arXiv:2604.19295, 2026): 将 TTT 形式化为 EM 框架，证明省略 critic recalibration 导致 ELBO degradation 和 diversity collapse。概念上支持 proposal 的 dual-loop 设计。\n- MathAtlas (arXiv:2605.14061, May 2026): 52K graduate-level 问题 + 178K dependency relations，MA-Hard 最佳仅 2.6%。验证了 OOD autoformalization 的严峻挑战。\n- AMBER/Construction-Verification (arXiv:2602.01291, 2026): 47.3% compilation errors 来自 identifier hallucination。支持 proposal 对 Tier 1 error 占比 ≥40% 的预期。\n\n**调研总结**: Autoformalization 领域正在沿三条轴线快速发展：(1) RL-based training (FormaRL, Wang et al.)、(2) retrieval augmentation (Aria, DDR, DRIFT)、(3) test-time compute (FormalEvolve, TTRL)。这三条轴线目前是独立的——没有工作将 test-time RL 应用于 autoformalization，也没有工作在 TTRL 中实现 co-adaptive retrieval。Proposal 定位在三者的交叉点，gap 是真实的。\n\n【Trivial Alternative 检验】:\n最直接的 trivial alternative 是 **Best-of-N + CriticLean 过滤**：给基础模型分配等量 test-time compute 采样更多候选，用 CriticLean-14B 过滤，不做任何 weight adaptation。Proposal 已将其纳入 compute-matched baseline，这是好的。\n\n第二个 trivial alternative 是 **static retrieval + TTRL**：直接在 autoformalization 上跑 TTRL，用 compilation-only reward，retriever 固定不更新。这实际上是 proposal 的一个 ablation。\n\nProposal 对这两个 trivial alternative 有明确的应对。增量价值的核心论证是：(a) weight adaptation 能产生 inference-time scaling 无法到达的 OOD 泛化（因为固定模型的输出空间可能根本不包含正确 formalization），(b) co-adaptive retrieval 利用 compilation error 的结构化信息实现 retriever-formalizer 协同进化。论证逻辑上是通的，但 (a) 的实证支撑依赖于 MathAtlas MA-Hard 2.6% 这个极端数据点，在 moderate OOD 场景下 Best-of-N 可能就够了。\n\n**结论**: Trivial alternative 威胁在 moderate OOD 场景下存在，但在 extreme OOD 场景下 proposal 的论证成立。Proposal 意识到了这一点并设计了 compute-matched baseline。\n\n【前提假设检验】:\n核心 claim 的逻辑链有几个关键假设：\n\n1. **\"Lean 4 的 structured error 能提供 oracle-quality retrieval training signal\"** — 这是最核心的假设。AMBER 的 47.3% identifier hallucination 数据和 DDR 的 Hall_m=0.21-0.39 提供了间接支撑，但这些数据来自不同模型（DeepSeek-R1 / frontier LLMs）、不同设置。在 TTRL 过程中，随着模型权重更新，error 分布会变化——proposal 的 Phase -1 micro-analysis 旨在验证这一假设，这是合理的。此假设有中等程度的实证支撑，但尚未在 TTRL 动态场景下验证。\n\n2. **\"CriticLean 在 skewed OOD 分布下仍能保持足够精度\"** — CriticLeanBench 是 250/250 balanced，而 OOD TTRL 下 <10% compilable，分布偏移巨大。Proposal 用 Phase 0 calibration + confidence gating 来应对，但这仍是未经验证的假设。如果 CriticLean 在 OOD skewed 分布下 precision 不达标，整个 multi-tier reward 体系的核心组件就不成立。\n\n3. **\"Binarize-then-enrich 能有效处理 heterogeneous reward\"** — 这是对 DDRL + GDPO 的嫁接，逻辑上合理但完全是未经实验验证的组合。特别是 binarization 层丢弃了 critic 的 soft signal 信息（30-70% ambiguity zone 被排除），这可能在数据稀缺的 OOD 场景下浪费宝贵的训练信号。\n\n4. **\"Co-adaptive retrieval 的收益会超过其引入的复杂性和不稳定性\"** — 同时更新 formalizer 权重和 retriever 权重是一个 non-trivial 的双优化问题。R3 和 Reinforced-IR 在 QA 场景验证了可行性，但 autoformalization + TTRL 场景的 signal density 更低（50 steps × 32 candidates × ~15% compile rate ≈ 240 对/cycle），retriever 更新的样本效率是个问号。\n\n**结论**: 假设 1 和 2 有 partial evidence 但需要 proposal 中的 de-risking phases 验证；假设 3 和 4 是更强的未验证假设。但 proposal 的 phased design 和 go/no-go gates 表明作者清楚这些风险。\n\n【3 维度打分】:\n\n1. **Novelty: 中偏强** —\n理由：核心 insight——\"formal languages 的 structured compilation errors 构成一个 graded hierarchy of adaptation signals，使得 co-adaptive retrieval 成为 TTRL 在 formal setting 中独有的 emergent capability\"——是真正的 novelty。这不仅仅是\"把 A 应用到 B\"，而是识别了 formal vs. informal reasoning 之间的一个 structural asymmetry 并系统性地利用它。调研确认无现有工作做到这一点：Aria (ICLR 2026) 是 static retrieval，FormaRL (COLM 2025) 是 training-time RL without retrieval，FormalEvolve 丢弃 error structure，TTRL 仅处理 informal math。Gap 是真实的。\n\n但我必须指出两个 novelty 折扣：(a) 这是一个 **combination paper**——四个独立验证的组件的首次整合。每个组件单独看（co-adaptive retrieval, TTRL, critic reward, debiased RL）都已有前人工作，novelty 来自组合而非单个突破。AAAI 审稿人可能以\"engineering novelty\"而非\"conceptual novelty\"定性。(b) \"Binarize-then-enrich\"这个贡献虽然填补了 DDRL 的 explicit future work gap，但本身较为 incremental——本质是在 DDRL 的 binary framework 上叠加 GDPO 的 per-reward normalization。\n\n2. **Significance: 中偏强** —\n理由：OOD autoformalization 是一个重要且日益突出的问题。MathAtlas MA-Hard 2.6%（arXiv:2605.14061）量化了现有方法在 graduate-level 数学上的惨淡表现。如果 TTRA 能在 OOD 域上显著提升 autoformalization 质量，对 formal mathematics、AI for math、proof assistants 社区都有实际影响。\n\nTest-time adaptation 作为 formal math 的\"第三 scaling axis\"（complementing training-time 和 inference-time compute）的 framing 具有概念上的吸引力，并与 TEMPO (arXiv:2604.19295) 的 TTT 叙事相呼应。\n\n但 significance 的上限受限于：autoformalization 仍是一个相对 niche 的子领域。虽然 AAAI 作为综合 AI 会议接受范围很广，但 reviewer pool 中深度理解 Lean 4 + TTRL + retrieval 这个交叉点的人有限。如果 reviewer 不具备足够背景，可能低估 contribution。\n\n3. **Related Work: 强** —\n理由：Proposal 对 related work 的覆盖在我调研范围内是全面且准确的。所有我查证的关键论文（TTRL、CriticLean、DDRL、R3、Reinforced-IR、Aria、FormaRL、FormalEvolve、TEMPO、MathAtlas、AMBER）均真实存在，描述准确，差异化定位清晰。Proposal 不仅列出了竞争工作，还精确指出了每个工作的局限性与 TTRA 的差异。对 6 个子方向（RL for autoformalization, semantic critics, debiased RL, retrieval-augmented autoformalization, test-time compute, error analysis）的分类组织清晰。\n\n特别值得肯定的是：proposal 将最近的工作（TEMPO April 2026, MathAtlas May 2026, Dymetman May 2026）也纳入了 landscape 分析，说明作者持续跟踪领域动态。唯一的小缺陷是部分引用密度过高，可能在实际论文中需要精简以保持可读性。\n\n【概率估计】: [28% - 38%] 中位 33%\n\n【估计理由】:\nNovelty 是\"中偏强\"而非\"强\"，因为这本质是一个 combination/integration paper。核心 insight（structural asymmetry enabling co-adaptive retrieval as emergent TTRL capability）是真正的 novelty，但四个组件的整合属于 system-level contribution。AAAI 审稿人对 combination novelty 的接受度因人而异。Significance 在 autoformalization 社区内是强的，但受限于子领域的 niche 程度。Related work 覆盖出色，不构成扣分因素。\n\n上界受限于 **Novelty 的 combination 性质**：如果审稿人认为\"each piece exists, you just put them together\"，evaluation 无论多精致都无法拯救。下界受支撑于 **gap 的真实性和 insight 的原创性**：no existing work exploits structured compilation errors for co-adaptive retrieval during TTRL，这一点在领域调研中得到了确认。\n\n【主要风险】:\n1. **\"Lego novelty\" 批评**：审稿人可能认为 TTRA 是四个现有技术（TTRL + co-adaptive retrieval + CriticLean + DDRL/GDPO）的工程整合，而非概念突破。Proposal 对 structural asymmetry 的论述需要在论文中更加突出以对冲这一批评。\n2. **系统复杂性与可归因性**：dual-loop + multi-tier reward + progressive curriculum + critic calibration 的复杂度极高。如果实验结果是 moderate improvement，审稿人难以判断哪个组件真正起作用；如果是 negative 或 mixed result，复杂性本身成为攻击面（\"too many moving parts, unclear what matters\"）。\n```\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- TTRL (NeurIPS 2025, arXiv:2504.16084): 首个在无标注数据上通过多数投票产生伪标签进行 test-time RL 的工作。Qwen2.5-Math-7B 在 AIME 2024 上 pass@1 提升 ~211%。仅适用于有确定数值答案的非形式化数学推理——多数投票对形式化语句不适用。TTRA 的出发点正是解决这一局限。\n\n- DDRL (ACL 2026 Findings, arXiv:2604.21327): 识别并修复 GRPO 在低共识区间对伪奖励的放大效应。使用频率感知平衡采样 + 固定 ±1 advantage + 共识离策略精炼。在 AIME 2024 上对 Qwen2.5-Math-1.5B 实现 19% 相对提升。但**明确限于二值奖励**，作者自己将多层级奖励列为 future work。TTRA 的 binarize-then-enrich 直接回应此 gap。\n\n- GDPO (NVIDIA, arXiv:2601.05242): 解决多奖励 GRPO 训练中信号坍缩问题，对每个奖励分量独立归一化。在 AIME 上对 DeepSeek-R1-1.5B 精度提升 6.3%。但不处理伪标签噪声/去偏。TTRA 将 GDPO 的多奖励归一化与 DDRL 的去偏结合。\n\n- CriticLean (arXiv:2507.06181, ByteDance/南京): CriticLeanGPT-14B-RL 在平衡 CriticLeanBench 上达 84.8% 准确率。首个训练专门的语义评判器来评估 Lean 4 形式化是否忠实于原始语义。但**基准分布是 250/250 平衡**的，与 OOD TTRL 中 <10% 可编译的极度偏斜分布不同。TTRA 的 Phase 0 校准协议正是针对此分布偏移。\n\n- FormaRL (COLM 2025, arXiv:2508.18914): 首个用 GRPO 做 autoformalization RL 的工作。编译检查 + LLM 一致性检查作为奖励。Qwen2.5-Coder-7B 在 ProofNet 上 pass@1 从 4.04% 提升至 26.15%。但是**训练时 RL**，无 test-time 适应，无检索。\n\n- Wang et al. (NeurIPS 2025 MAR Workshop): 在线 RL for autoformalization，使用 GRPO + BEq + embedding 奖励。TC1: 17.29%→26.01%。最接近的先前工作，但仍是**训练时、分布内**，无检索，无 test-time 适应，无训练过的语义评判器。\n\n- Aria (ICLR 2026, arXiv:2510.04520): 当前检索增强 autoformalization 的 SOTA。通过依赖图分解 + 迭代形式化 + AriaScorer 在 ProofNet 上达 91.6% 编译 / 68.5% 精度，在同调猜想上 42.9%（其他系统 0%）。关键局限：**检索器是固定的**，不随形式化器行为漂移而适应；**模型权重不更新**。\n\n- DDR (arXiv:2511.11990): 构建 500K 样本依赖数据集。量化前沿 LLM 的标识符幻觉率 Hall_m=0.21-0.39，通过检索降至 <0.02。证实标识符幻觉是可量化的主要错误模式。\n\n- AMBER/Construction-Verification (arXiv:2602.01291): 在 3,189 个编译错误中，47.3% 来自标识符幻觉（DeepSeek-R1 在应用数学上）。为 TTRA 关于 Tier 1 错误占主导的假设提供独立实证。\n\n- FormalEvolve (arXiv:2603.19828): 将 autoformalization 表述为有预算的进化搜索。SH@100 在 CombiBench 58.0%，ProofNet 84.9%。**搜索固定模型的输出空间，不做权重适应或检索器共适应**。与 TTRA 正交。\n\n- TEMPO (arXiv:2604.19295): 将 TTT 形式化为 EM（策略精炼 = M-step，评判器重校准 = E-step）。证明省略重校准导致 ELBO 退化和多样性坍缩。为 TTRA 的双循环设计提供概念支撑。\n\n- T³RL (arXiv:2603.02203): 将外部工具验证引入 TTRL，用代码执行输出加权投票。但**将工具反馈压缩为单个二值信号**（verified/unverified），丢弃工具输出的内部结构。\n\n- R3 (NeurIPS 2025, arXiv:2510.24652): 通过强化对比学习优化 RAG 检索。在通用 RAG 上提升 5.2%。验证了基于环境反馈训练检索器的范式可行性。\n\n- Reinforced-IR (ACL 2025): 交替 RLRF/RLGF 实现检索器-生成器互适应。验证共适应检索的范式，但未应用于 autoformalization。\n\n- MathAtlas (arXiv:2605.14061, May 2026): 52K 研究生级数学问题，178K 依赖关系。最强基线仅 9.8% 定理正确率，MA-Hard 上 2.6%。证实 OOD autoformalization 是未解决的挑战。\n\n- **调研总结**: Autoformalization 领域正处于方法快速演进阶段：训练时 RL（FormaRL, Wang et al.）、检索增强（Aria, DDR, DRIFT）、推理时搜索（FormalEvolve）、语义评判（CriticLean）各自取得显著进展，但**尚无工作将 test-time RL 应用于 autoformalization**，也**无工作在 TTRL 中实现检索器共适应**。TTRA 位于这些独立研究线的交汇处，填补的是一个真实存在的空白。\n\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative 是 **Best-of-N 采样 + CriticLean 过滤 + 静态检索**（即 Aria 风格的检索 + 大量采样 + CriticLean 打分筛选）。Proposal 已预见到这一点并将其作为 compute-matched baseline。关键问题是：TTRA 的权重适应相对于这个 trivial baseline 的增量价值是什么？\n\nProposal 的论证是：对于真正的 OOD 领域（MathAtlas MA-Hard: 2.6%），固定模型的输出空间可能根本不包含正确的形式化——无论采样多少次都无法找到模型无法生成的内容。这个论证在概念上是合理的，但其成立程度取决于 OOD 的\"远\"程度。对于中等 OOD，Best-of-N + 检索可能已经足够。因此 TTRA 的增量价值主要体现在**极端 OOD 场景**，这限制了其适用范围但也提高了其在该场景下的 significance。\n\n另一个 trivial alternative：**标准 SFT/继续预训练在 OOD 领域数据上** + 静态检索。如果有少量 OOD 领域的标注数据，常规微调可能比 TTRL 更简单有效。但 TTRA 的设定是**无标注 OOD 数据**的 test-time 适应，这使得这个 alternative 不完全可比。\n\n**结论**：存在 trivial alternative 威胁，但 proposal 已明确将其纳入实验对比。增量价值的论证在极端 OOD 场景下合理，在中等 OOD 场景下需实验验证。\n\n【前提假设检验】:\n\n1. **\"Lean 4 结构化错误信号可以作为检索器训练的 oracle-quality 信号\"** — **部分成立，但有过度声称的风险**。当编译器报告 `unknownIdentifier \"Finset.sum_bij\"` 时，确实直接指出需要的标识符。但\"oracle-quality\"措辞过强：(a) 模型可能幻觉出不存在的标识符名称，此时错误信号指向一个不存在的目标；(b) 对于 Tier 2 错误（类型不匹配），从错误信息到正确依赖的映射并不总是一对一的。AMBER 的 47.3% 数据支持 Tier 1 错误占主导，但这是 DeepSeek-R1 的数据，TTRA 使用 Qwen3-8B 可能分布不同——Phase -1 旨在验证此点。\n\n2. **\"CriticLean-14B 在极度偏斜分布下仍可保持足够精度\"** — **未经验证但有合理的去风险策略**。CriticLeanBench 是 250/250 平衡的，而 OOD TTRL 中 <10% 可编译。Phase 0 的 go/no-go gate 是合理的，但如果 CriticLean 在此分布下精度不足，整个框架的核心组件就失效了。\n\n3. **\"共适应检索的增量收益足够显著\"** — **最关键的未验证假设**。R3 和 Reinforced-IR 在通用 RAG 上验证了共适应检索的价值，但 autoformalization 的检索空间（Mathlib 26K+ 定义）结构非常不同于通用文档检索。FAISS 在高频重建下的性能开销也是实际考量。\n\n4. **\"DDRL 的去偏 + GDPO 的多奖励归一化可以直接组合\"** — **合理但简化**。两个方法各自被验证，但它们的组合是否引入新的交互效应（如去偏采样改变了多奖励归一化的有效样本分布）未被讨论。\n\n5. **\"TTRL 中的政策漂移不会导致检索器训练信号退化\"** — Proposal 引用 TEMPO 的 EM 分析，但 TEMPO 处理的是评判器重校准而非检索器。检索器-形式化器共适应可能存在不同的稳定性特征。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n\nTTRA 的核心 novelty 是一个**领域交叉集成创新**：将 co-adaptive retrieval（R3, Reinforced-IR 验证了范式）、test-time RL（TTRL 验证了范式）、debiased multi-tier reward（DDRL + GDPO 各自验证了组件）、semantic critic（CriticLean 验证了工具）四条独立研究线首次组合应用于 autoformalization。\n\n关键创新点：\n- **Lean 4 结构化错误 → 检索器训练信号** 的洞察是非平凡的，在我的调研范围内确实无先前工作发现并利用此联系。T³RL 将工具反馈压缩为二值信号丢弃了内部结构，FormalEvolve 仅用编译成功/失败，Aria 的检索器不适应——TTRA 对此的差异化定位清晰。\n- **Binarize-then-enrich** 直接回应 DDRL 论文自身声明的 future work，填补真实 gap。\n\n但需要诚实承认：\n- 这本质上是一个**系统集成**论文，每个组件独立存在，novelty 在于组合而非单个组件。\n- \"形式语言提供比二值奖励更丰富的反馈\"这一核心洞察，一旦被陈述出来就显得**合理但不令人惊讶**——reviewer 可能会说 \"of course compilers give richer feedback\"。\n- Binarize-then-enrich 的技术贡献相对直接（在 DDRL 的二值化层上叠加 GDPO 的多奖励归一化）。\n\n2. **Significance: 中偏强** — \n\n问题本身重要：OOD autoformalization 是真实且困难的挑战（MathAtlas MA-Hard 2.6% 证实了这一点）。如果 TTRA 成功，它：\n- 建立 test-time learning 作为形式数学的第三个 scaling axis（训练时、推理时之外），这是有影响力的框架性贡献\n- 提供首个将 TTRL 扩展到非数值答案领域（形式化语句）的方法，可能推广到其他有结构化编译/验证反馈的任务（如代码生成）\n- 解决 static retriever 不适应 policy drift 的已知局限（Aria 的核心瓶颈之一）\n\n但 significance 受限于：\n- 实际影响取决于改进幅度——如果在 MathAtlas MA-Hard 上从 2.6% 到 5%，技术上有意义但实用价值有限\n- 应用场景相对窄（Lean 4 autoformalization with Mathlib），不是一个通用方法\n- 资源需求高（1400-1900 A100-hours），但这不影响 idea 评估\n\n3. **Related Work: 强** — \n\n这是整个 proposal 最强的维度。覆盖了：\n- 6 个相关研究方向的所有核心工作\n- 每篇工作的具体数据、局限性和与 TTRA 的差异\n- 最新至 2026 年 5 月的工作（MathAtlas, Dymetman binary rewards）\n- 明确的差异化定位：对 Aria（静态检索器）、DDRL（二值奖励限制）、T³RL（丢弃工具反馈结构）、FormalEvolve（无权重适应）等逐一清晰区分\n\n我的调研验证了 proposal 中引用的论文均真实存在，描述基本准确。未发现遗漏的重要竞争工作。唯一轻微疏漏：proposal 未充分讨论 **Lean 4 Cycle Consistency Fine-tuning** (arXiv:2603.24372) 等更小规模但相关的工作，但这不影响核心定位。\n\n【概率估计】: [28% - 38%] 中位 32%\n\n【估计理由】: \n\nNovelty 是限制上界的主要维度。TTRA 是一个高质量的系统集成工作，而非根本性的方法论创新。核心洞察（Lean 4 错误信号 → 检索器训练信号）虽然在调研范围内确认为 novel，但不属于\"反直觉\"级别——一旦认识到形式语言的结构化反馈优势，方法论自然跟进。审稿人可能会评价为 \"well-motivated combination, but the individual pieces are not new\"。\n\nSignificance 处于中偏强：问题重要（OOD autoformalization 确实困难且未解决），框架性贡献（第三 scaling axis）有价值，但应用面相对窄。\n\nRelated Work 是强项，不会成为被拒原因。\n\n综合来看：这个 proposal 的 idea 内核处于 \"方向正确 + 有真实 novelty delta + 但核心发现 if positive 审稿人大概率说 'makes sense, well-engineered' 而非 'surprising'\" 的区间，对应 rubric 中 25-35% 的锚点。考虑到 related work 极其充分且问题的时效性/重要性，上调至 28-38%，中位 32%。\n\n【主要风险】: \n1. **\"组合 vs 创新\" 的审稿人争论**：核心贡献是四条研究线的首次组合，每个组件独立存在。审稿人可能认为 \"engineering contribution > intellectual contribution\"，尤其是如果 binarize-then-enrich 被认为是 DDRL + GDPO 的直接拼接。\n2. **核心洞察的 surprise 不足**：\"形式语言编译器提供比二值奖励更丰富的反馈\" 这一洞察，虽然在此前工作中未被利用，但陈述后显得近乎显然，可能被审稿人认为缺乏深度——从而将整体贡献降级为 \"a solid system paper\" 而非 \"a paper with a deep new insight\"。\n```\n\nSources:\n- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/pdf/2504.16084)\n- [DDRL: Spurious Signal Amplification in TTRL](https://arxiv.org/html/2604.21327)\n- [GDPO: Group reward-Decoupled Normalization](https://arxiv.org/abs/2601.05242)\n- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181)\n- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)\n- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)\n- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652)\n- [Aria: An Agent for Retrieval and Iterative Auto-Formalization](https://arxiv.org/abs/2510.04520)\n- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)\n- [FormalEvolve: Neuro-Symbolic Evolutionary Search](https://arxiv.org/abs/2603.19828)\n- [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/abs/2604.19295)\n- [T³RL: Tool Verification for Test-Time RL](https://arxiv.org/abs/2603.02203)\n- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)\n- [AMBER/Construction-Verification Benchmark](https://arxiv.org/abs/2602.01291)\n- [TTARAG: Test Time Adaptation for RAG](https://arxiv.org/abs/2601.11443)\n- [CriticLeanGPT-Qwen3-14B-RL on HuggingFace](https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization\n\n## Core Problem\n\nCurrent autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in multi-tier reward settings; and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation.\n\nA key structural asymmetry motivates our approach: in informal math reasoning, TTRL obtains only binary correct/incorrect signals with no information about *why* a solution failed or *what knowledge is missing*—and binary rewards create a fundamental degeneracy for policy gradient methods, leading to diversity collapse (Dymetman, arXiv:2605.02375). In contrast, Lean 4's compiler produces machine-parseable error messages that precisely identify missing identifiers, type mismatches, and unresolved typeclass instances—constituting a graded hierarchy of structured feedback signals. Critically, these signals are not merely \"richer rewards\": when a compilation error reports `unknownIdentifier \"Finset.sum_bij\"`, it provides an oracle-quality, token-level retrieval training signal that directly specifies which Mathlib dependency is needed. Such signals are unavailable during pre-training or SFT (no compilation feedback), discarded by inference-time search methods like FormalEvolve (which uses only compile success/failure), and unexploited by static retrieval pipelines like Aria (whose retriever cannot adapt). Only during test-time RL can these structured error signals be continuously collected and used to co-adapt the retriever—making co-adaptive retrieval an emergent capability uniquely enabled by TTRL in formal language settings.\n\nFor domains where model performance is extremely low (MathAtlas MA-Hard: 2.6%), inference-time scaling alone is insufficient: the fixed model's output space may not contain correct formalizations for truly OOD domains, so no amount of sampling can find what the model cannot generate. Weight adaptation is necessary, and it produces compounding improvement—better formalizations yield more informative compilation errors, which improve the retriever, which enables even better formalizations in subsequent rounds.\n\n## Research Opportunity\n\nFour independently validated capabilities have never been combined, and their integration is enabled by the structured feedback properties unique to formal languages.\n\n(1) **Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode.** R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv:2601.11443, Jan 2026) shows test-time retrieval adaptation via self-supervised prediction. The prevalence of identifier hallucination is established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math stem from hallucination of non-existent theorems/definitions. DDR (arXiv:2511.11990) quantifies Hall_m=0.21-0.39 across frontier LLMs, reduced to <0.02 with retrieval. The RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as a primary error class. MathAtlas (arXiv:2605.14061, May 2026) shows a 66% advantage for Mathlib-grounded definitions (27.9% vs 16.8%, p<0.001). Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL—where Lean's structured error taxonomy provides graded, machine-parseable signals for retriever training.\n\n(2) **TTRL with debiasing has advanced but remains limited to binary rewards in informal settings.** DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed ±1 advantages, and consensus-based off-policy refinement (19.0% relative improvement over ETMR on AIME 2024; 4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B), but assumes binary rewards with 'more expressive advantage formulations' left as future work. GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization but does not address debiasing. T³RL (arXiv:2603.02203, Mar 2026) introduces tool-verified rewards into TTRL, using code execution output to upweight verified rollouts—but collapses all tool feedback into a single binary bit (verified/unverified), discarding the internal structure of tool output. SCOPE (arXiv:2512.15146, Dec 2025) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, but remains within the homogeneous binary-reward paradigm. The combination of DDRL's debiasing with GDPO's multi-reward normalization for heterogeneous reward components (hard binary gate + noisy soft critic + drifting population statistic) has not been attempted.\n\n(3) **CriticLean provides the missing semantic reward signal.** CriticLeanGPT-14B-RL (arXiv:2507.06181, July 2025) achieves 84.8% accuracy on balanced CriticLeanBench (87.0% for 32B), but CriticLeanBench's 250/250 balanced distribution differs from OOD TTRL's heavily skewed distribution (<10% compilable). This distributional shift gap motivates our Phase 0 calibration protocol.\n\n(4) **Online RL for autoformalization validated at training time only.** Wang et al. (NeurIPS 2025 MAR Workshop) achieves TC1: 17.29%→26.01% on RLMEval using GRPO with BEq + embedding rewards, but operates at training time on in-distribution problems without retrieval, test-time adaptation, or a trained semantic critic.\n\nRecent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.\n\n## Research Landscape\n\n**(1) RL for autoformalization.** FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards (pass@1: 4%→26% on ProofNet). Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with BEq + embedding similarity (TC1: 17.29%→26.01%, TC50: 76.41%→85.46% on RLMEval)—closest prior work but training-time, no retrieval, no test-time adaptation. ReForm (arXiv:2510.24592) applies PBSO position-aware RL rewards for reflective autoformalization; ReForm-8B (Qwen3-8B) achieves +18.0pp average improvement.\n\n**(2) Semantic critics and iterative refinement.** CriticLean (July 2025) introduces CriticLeanGPT (32B-RL: 87.0%, 14B-RL: 84.8% on balanced CriticLeanBench). ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO. Monotonic Refinement achieves 90.27% on miniF2F through multi-model ensemble orchestration. These cannot adapt model weights to new domains.\n\n**(3) Debiased RL, multi-reward optimization, and TTRL reward improvements.** DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification exclusively with binary rewards; GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward normalization. Binary Rewards and RL (Dymetman, arXiv:2605.02375, May 2026) proves binary rewards create fundamental degeneracy (diversity collapse). T³RL (arXiv:2603.02203, Mar 2026) introduces external tool verification into TTRL, upweighting verified rollouts via verification-aware voting—but treats tool output as a single binary signal (verified/unverified), discarding the structured content of tool feedback. SCOPE (arXiv:2512.15146) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, remaining within the homogeneous binary-reward paradigm. All these improvements assume homogeneous reward signals. TTRA addresses a qualitatively different problem: heterogeneous reward components (hard compilation gate, noisy critic signal, policy-drifting BEq statistic) requiring a two-layer binarize-then-enrich adaptation.\n\n**(4) Retrieval-augmented autoformalization and co-adaptive retrieval.** Aria (ICLR 2026, arXiv:2510.04520) achieves ProofNet 91.6% compilation / 68.5% accuracy and 42.9% on homological conjectures (vs. 0% for all others) via dependency graph + iterative formalization + AriaScorer—current frontier of retrieval-augmented autoformalization, but a fixed inference pipeline: retriever does not adapt to formalizer's evolving behavior and model weights are not updated. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF. DDR builds a 500K-sample dataset (Hall_m reduced from 0.21-0.39 to <0.02). CRAMF indexes 26K+ Mathlib definitions. ProofBridge (ICLR 2026, arXiv:2510.15681) uses joint embeddings + retrieval-augmented fine-tuning. On co-adaptive retrieval: R3 (NeurIPS 2025, arXiv:2510.24652) optimizes RAG retrieval via reinforced contrastive learning; Reinforced-IR (ACL 2025) alternates RLRF/RLGF; TTARAG (arXiv:2601.11443) demonstrates test-time retrieval adaptation. None applied to autoformalization or Lean 4.\n\n**(5) Test-time compute for autoformalization.** FormalEvolve (arXiv:2603.19828, Mar 2026) formulates autoformalization as budgeted evolutionary search (SH@100=58.0% CombiBench, 84.9% ProofNet) using LLM-driven mutation/crossover with AST rewrites. This is orthogonal to TTRA: FormalEvolve searches a fixed model's output space without weight adaptation or retriever co-adaptation, discarding compilation error structure. TEMPO (arXiv:2604.19295, Apr 2026) formalizes test-time training as EM (policy refinement = M-step, critic recalibration = E-step), proving that omitting recalibration leads to ELBO degradation and diversity collapse—a conceptual parallel to TTRA's dual-loop where omitting retriever co-adaptation (= static retrieval TTRL) accumulates retriever-formalizer distribution mismatch.\n\n**(6) Error analysis and identifier hallucination.** The AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are identifier hallucination (32.7% competence, 15.2% incomplete, 4.8% syntax). RAutoformalizer (ICLR 2025 Spotlight) categorizes errors into 'Hallucination' vs 'Others'. MathAtlas (arXiv:2605.14061) introduces 52K graduate-level problems (best: 2.6% on MA-Hard).\n\nAfter exhaustive search through May 2026, no work combines co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, a calibrated semantic critic with distributional shift analysis, principled adaptation of binary-reward debiased RL to heterogeneous multi-tier rewards, and test-time adaptation on unlabeled OOD domains. Existing retrieval methods (Aria, DRIFT, DDR) use static retrievers; existing RL methods (FormaRL, Wang et al., ReForm) operate at training time; existing test-time methods (FormalEvolve) search without learning; existing TTRL improvements (T³RL, SCOPE, DDRL) assume homogeneous binary rewards.\n\n## Proposed Approach\n\nWe propose TTRA (Test-Time Retrieval-Augmented autoformalization), making TTRL viable for autoformalization through three technical innovations unified by a single insight: formal languages' structured compilation feedback creates a graded hierarchy of adaptation signals unavailable in informal reasoning, enabling co-adaptive test-time learning as a new scaling axis for formal mathematics—complementing training-time compute (more data, larger models) and inference-time compute (more samples, longer search). Drawing a conceptual parallel with TEMPO's EM formalization of TTT, TTRA's dual-loop design ensures the retriever co-adapts with the formalizer (analogous to not omitting the E-step), preventing the retriever-formalizer distribution mismatch that would degrade a static-retrieval TTRL.\n\n**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Quantify Lean 4 error taxonomy coverage on OOD domains. Compile 500 candidate formalizations on Con-NF and 500 on MathAtlas MA-Hard, classify errors into: Tier 1 (direct identifier: `lean.unknownIdentifier`, `unknown namespace`), Tier 2 (type-based: `type mismatch`, `failed to synthesize instance`), Tier 3 (indirect: tactic/elaboration/syntax errors). Thresholds: Tier 1 ≥40% → co-adaptive retrieval well-supported; 20-40% → rely on Tier 1+2; <20% → fall back to Tier 2 with type-signature matching. Prior evidence strongly supports ≥40% (AMBER: 47.3%; DDR: Hall_m=0.21-0.39; RAutoformalizer treats 'Hallucination' as primary class; CRAMF documents systematic fabrication). Phase -1 validates on our specific model/domain. Simultaneously verify MathAtlas MA-Hard gold formalization coverage; if <50%, downgrade to secondary benchmark and activate IndiMathBench (arXiv:2512.00997) as contingency OOD benchmark. Resource: ~8 A100-hours generation, ~10 CPU-hours parsing.\n\n**Phase 0 — Minimal Pilot with Critic Calibration (De-risking).** FormaRL's GRPO pipeline with CriticLean-14B replacing LLM-consistency reward. 200 Con-NF + 200 FormalMATH number theory problems. Primary hypothesis: ≥3pp BEq@1 over compilation-only GRPO on Con-NF. Critic calibration under distributional shift: measure precision/recall separately on skewed distribution (<10% compilable); report calibration curves; if precision <80%, introduce confidence gating >0.8. Go/no-go: proceed only if primary hypothesis confirmed AND precision ≥80%. Additionally, establish critic calibration monitoring protocol: during subsequent TTRL phases, checkpoint critic precision every ~100 GRPO steps; if precision drops >10pp from Phase 0 baseline, adjust confidence threshold (periodic recalibration, motivated by TEMPO's finding that reward signal drift without recalibration leads to performance plateaus). Resource: ~50 A100-hours, 2-3 weeks.\n\n**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune Qwen3-8B using DDR's 500K-sample dataset and GRPO with R(y, x) = r_compile × (α·r_critic + β·r_beq). r_compile ∈ {0,1} (Kimina Lean Server, 128 parallel workers); r_critic ∈ {0,1} (CriticLeanGPT-Qwen3-14B-RL, gated by Phase 0 threshold); r_beq ∈ [0,1] (BEq consensus density). α=0.7, β=0.3. Fallback: when <4 of K=32 compile, R = r_compile × r_critic.\n\n**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever (DDR-style dense encoder) is explicitly updated during TTRL. This exploits Lean 4's unique structural property: compilation errors provide oracle-quality, token-level retrieval training signals that directly specify which Mathlib dependencies are needed—signals unavailable during pre-training, discarded by inference-time search, and unexploited by static retrieval pipelines.\n\n  Loop 1 — Formalizer GRPO (every step): K=32 candidates, compile, multi-tier rewards, debiased GRPO.\n\n  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Graded error hierarchy:\n    (a) Tier 1 (highest confidence): `lean.unknownIdentifier` names missing constant → hard negatives from retrieved set; constant from CRAMF/DDR index = positive. `unknown namespace` → coarser module-level positive.\n    (b) Tier 2 (moderate): `type mismatch` → type signatures matched against Mathlib type index, 0.5× weight. `failed to synthesize instance` → typeclass instances as positives.\n    (c) Tier 3: tactic/elaboration/syntax → negatives only.\n    (d) Compilation success → all retrieved dependencies in compiled output = confirmed positives.\n    (e) Weighted InfoNCE: L = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), w_k = 1.0 (Tier 1/confirmed), 0.5 (Tier 2), τ=0.07.\n    (f) Decoupled optimization (per R3 and Reinforced-IR): retriever gradient does not flow through formalizer. FAISS rebuild after each update.\n\n  Signal density: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle.\n\n**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** Autoformalization's reward components are fundamentally heterogeneous: compilation is a hard binary gate (non-negotiable), the critic is a noisy soft signal (calibrated but imperfect), BEq is a population statistic (drifts with policy). This heterogeneity distinguishes TTRA from all existing TTRL reward improvements (DDRL, T³RL, SCOPE, GDPO), which assume homogeneous reward signals. Neither DDRL alone (cannot handle multi-tier) nor GDPO alone (does not address spurious amplification) suffices:\n\n  (a) Binarization layer: r_accept = I(r_compile=1 AND r_critic=1). Balanced sampling (exclude 30-70% ambiguity zone per DDRL). Fixed advantages: +1 (accepted), -1 (rejected). Consensus off-policy refinement: M=128, rejection-sample >80% acceptance, SFT 5 epochs.\n  (b) GDPO-style enrichment: among accepted candidates, per-reward decoupled normalization for BEq. Additive bonus δ·norm(r_beq) to +1 advantage, δ=0.3.\n\n**Phase 4 — Progressive Domain Curriculum.** (a) Near-distribution warm-start: compilation ≥40%, critic approval ≥60%, BEq@32 ≥3pp above baseline. Timeout: 500 steps. (b) Retrieval bootstrapping: Tier 1/2 errors feed retriever updates. Transition: recall@10 ≥30%, compilation ≥25%. Early transition: plateau <2pp over 200 steps. (c) Far-OOD: algebraic geometry, condensed mathematics, MathAtlas MA-Hard with adaptive fallback.\n\n**Contribution Floor Analysis.** (1) Co-adaptive retrieval + CriticLean TTRL alone: first co-adaptive retrieval for autoformalization + first TTRL for formal math with calibrated critic. (2) Binarize-then-enrich alone: addresses DDRL's explicit future work on multi-tier rewards. (3) Curriculum: droppable. (4) Essential floor: CriticLean TTRL outperforms compilation-only (Phase 0 gate) AND ≥1 of co-adaptive retrieval / binarize-then-enrich shows statistically significant improvement.\n\n**Evaluation.**\n\n  *Benchmarks:* In-distribution: miniF2F-test (244), ProofNet (~371). Multi-domain: FormalMATH (5,560). OOD stress tests: Con-NF, CombiBench, MathAtlas MA-Hard (700 entities, best: 2.6%; contingency: IndiMathBench if gold coverage <50%).\n\n  *Metrics:* BEq@K, BEq+@K (per DRIFT), pass@K (K=1,32), compilation@K on all benchmarks. GTED (arXiv:2507.07399, continuous [0,1] similarity with better precision-recall balance than BEq) on OOD benchmarks. Hall_m (DDR's hallucination rate) in retriever ablation. Human evaluation: 100-150 samples on Con-NF + 200 samples on MathAtlas MA-Hard (inter-annotator agreement reported).\n\n  *Same-scale primary baselines (~7-8B):* (1) FormaRL (Qwen2.5-Coder-7B, COLM 2025); (2) Online RL for Autoformalization (Wang et al., faithfully reimplemented if code unavailable); (3) DRIFT with Qwen3-8B (ICLR 2026); (4) Aria (ICLR 2026, reimplemented on shared benchmarks or reported numbers annotated); (5) StepFun-Formalizer-7B (AAAI 2026, open-source); (6) ReForm-8B (Qwen3-8B, arXiv:2510.24592); (7) compilation-only TTRL and critic-only TTRL ablations.\n\n  *Cross-paradigm reference:* FormalEvolve (arXiv:2603.19828, reported SH@100 on CombiBench/ProofNet).\n\n  *Compute-matched baseline:* Best-of-N (matched FLOPs) + CriticLean filtering: allocate equivalent test-time compute to sampling more candidates from base formalizer, filter with CriticLean-14B, report BEq@1 and compilation@1. Directly tests whether TTRA's weight adaptation provides value beyond inference-time scaling.\n\n  *Ablations:* (a) Standard GRPO vs. DDRL vs. binarize-then-enrich (component-wise); (b) frozen vs. co-adaptive retriever; (c) Tier 1-only vs. Tier 1+2 vs. all-tier error signals; (d) no curriculum vs. progressive; (e) CriticLean-14B reward vs. embedding-based similarity reward (isolating trained critic value).\n\n  *Sensitivity:* N_ret ∈ {25, 50, 100}; δ ∈ {0.0, 0.1, 0.3, 0.5} (δ=0.0 = pure DDRL); ambiguity zone ∈ {[20%-80%], [30%-70%], [40%-60%]}; critic confidence threshold ∈ {0.6, 0.7, 0.8, 0.9}; K ∈ {16, 32, 64} (test-time compute scaling behavior).\n\n  *Cross-scale references:* ATF-32B, ATLAS (NeurIPS 2025), Monotonic Refinement (multi-model ensemble). All tables annotate scale and compute.\n\n  *Statistical rigor:* Key comparisons ≥3 seeds, mean ± std, bootstrap CI (p<0.05).\n\n## Detailed Description\n\nTTRA makes TTRL viable for autoformalization by exploiting a structural asymmetry: Lean 4's compiler provides oracle-quality, token-level feedback (identifier names, type signatures, typeclass requirements) that serves simultaneously as retriever training signal, multi-tier reward components, and domain adaptation indicators—signals unavailable in informal reasoning and unexploited by existing methods. The dual-loop architecture co-adapts the retriever during test-time RL via weighted InfoNCE over Lean 4's error hierarchy, addressing the limitation that static retrievers (Aria, DRIFT, DDR) cannot track formalizer evolution. CriticLean-14B integration includes distributional shift calibration and periodic drift monitoring (motivated by TEMPO's EM analysis of reward signal degradation). Binarize-then-enrich addresses the specific gap between DDRL (binary debiasing) and GDPO (multi-reward normalization) for formal verification's heterogeneous reward landscape—a qualitatively different problem from the homogeneous-reward improvements in T³RL and SCOPE. Compute-matched evaluation against best-of-N + critic filtering directly tests whether weight adaptation provides value beyond inference-time scaling. The framework positions test-time learning as a third scaling axis for formal mathematics alongside training-time and inference-time compute.\n\n## Key References\n\n- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)\n- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)\n- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, NVIDIA, January 2026)\n- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv:2507.06181, ByteDance/Nanjing)\n- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)\n- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv:2510.24652)\n- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)\n- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv:2601.11443, January 2026)\n- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv:2602.01291, February 2026)\n- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)\n- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\n- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)\n- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)\n- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\n- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)\n- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv:2511.11990)\n- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)\n- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)\n- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)\n- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\n- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv:2505.02735)\n- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)\n- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\n- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026, arXiv:2510.04520)\n- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026, arXiv:2510.15681)\n- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv:2510.24592)\n- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv:2512.00997, Microsoft Research)\n- FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv:2603.19828, March 2026)\n- Binary Rewards and Reinforcement Learning: Fundamental Challenges (Dymetman, arXiv:2605.02375, May 2026)\n- TEMPO: Scaling Test-time Training for Large Reasoning Models (arXiv:2604.19295, April 2026)\n- T³RL: Tool Verification for Test-Time Reinforcement Learning (arXiv:2603.02203, March 2026)\n- SCOPE: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning (arXiv:2512.15146, December 2025)\n- GTED: Generalized Tree Edit Distance: A Faithful Evaluation Metric for Statement Autoformalization (arXiv:2507.07399)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1400-1900 A100-80GB hours (Phase -1 micro-analysis + MathAtlas coverage: ~10h; Phase 0 pilot + calibration: ~50h; Phase 1 base GRPO: ~300h; DDR retriever + co-adaptive updates: ~100h; Phase 4 progressive TTRL + ablations: ~400h; CriticLean-14B inference all phases: ~200-300h; N_ret/δ/ambiguity/critic-threshold/K sensitivity: ~100h; baseline evaluation (Aria reimpl + StepFun + ReForm): ~100-120h; compute-matched best-of-N baseline: ~30h; CriticLean vs embedding ablation: ~25h; multi-seed (3 seeds × key ablations): ~200h; human eval annotation: ~60-80h; miniF2F/ProofNet + remaining eval: ~80h) + 15,000-20,000 CPU-hours Lean verification (Kimina Lean Server), timeline: 14-18 weeks (0.5 wk Phase -1; 2-3 wk Phase 0 + go/no-go; 3 wk Phase 1; 2 wk retriever infrastructure; 4 wk TTRL experiments; 3 wk ablations + sensitivity + multi-seed; 2 wk writing), estimated_gpu_cost: $2,800-$4,700 + $750-$1,000 CPU + ~$1,500-$2,500 human annotation. GPU architecture: policy (8B) + ref (8B) on 4×A100 tensor parallel, CriticLean-14B on dedicated 2×A100 with vLLM batch inference, retriever + FAISS on CPU/1×A100; async pipeline.\n- **human_in_loop**: gpu_hours: 1100-1500 A100-80GB hours (~25% reduction), timeline: 11-14 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,200-$3,700 + $600-$800 CPU + ~$1,200-$2,000 annotation\n- **auto_research**: gpu_hours: 2000-2700 A100-80GB hours (full sweep), timeline: 8-11 weeks, claude_api_cost: $800-$1,200, estimated_gpu_cost: $4,000-$6,700 + $1,000-$1,350 CPU + ~$1,500-$2,500 annotation, speed_bottleneck: Lean 4 compilation (~3.65s/statement warm cache, ~0.10s amortized at 64 workers). CriticLean-14B ~0.5s/candidate (→~0.1-0.2s with vLLM). Retriever co-adaptation ~15 min/cycle (re-encode 26K constants, rebuild FAISS)."
}
````

---

### Runtime record

_source line 2 · 2026-05-28T06:05:40.115Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T06:05:40.115Z",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-28T06:05:40.131Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **TTRL (NeurIPS 2025, arXiv:2504.16084)**: 提出在无标签数据上用 majority voting 作为伪奖励进行 test-time RL，在 informal 数学推理上取得显著提升。但仅适用于有唯一数值答案的场景，不直接适用于形式化陈述（无法 majority vote）。

2. **DDRL (ACL 2026 Findings, arXiv:2604.21327)**: 识别并修复 GRPO 在 unsupervised 设置下的 spurious signal amplification，提出 balanced sampling + fixed advantages + consensus off-policy refinement。但明确限于 binary rewards，论文自身将 "multi-tier reward" 列为 future work。确认存在。

3. **GDPO (NVIDIA, arXiv:2601.05242)**: 发现 GRPO 在 multi-reward 设置下将不同 reward 组合 normalize 到相同 advantage 值，导致信息坍缩。提出 per-reward decoupled normalization。与 DDRL 解决的是不同问题（debiasing vs multi-reward resolution），确认两者未被统一。

4. **CriticLean (arXiv:2507.06181, ByteDance/Nanjing)**: CriticLeanGPT-14B-RL 在 balanced CriticLeanBench 上达 84.8% 准确率。模型已开源（HuggingFace: m-a-p/CriticLeanGPT-Qwen3-14B-RL）。论文聚焦于 critic 训练和 benchmark 构建，未探索将 CriticLean 作为 TTRL 的 reward 信号。确认存在。

5. **FormaRL (COLM 2025, arXiv:2508.18914)**: 使用 GRPO + compilation reward + LLM consistency check，在 ProofNet 上 pass@1 从 4.04% 提升至 26.15%。但是 training-time RL，非 test-time adaptation。确认存在。

6. **Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop)**: 使用 GRPO + BEq + embedding similarity，training-time。TC1: 17.29%→26.01%。无 retrieval，无 test-time adaptation。确认存在。

7. **Aria (ICLR 2026, arXiv:2510.04520)**: 当前 retrieval-augmented autoformalization 的 SOTA。通过 dependency graph + iterative formalization + AriaScorer 在 ProofNet 上达 91.6% compilation / 68.5% accuracy，homological conjectures 上达 42.9%。关键局限：retriever 是 static 的，不随 formalizer 行为变化而适应。确认存在，确认 ICLR 2026 poster。

8. **DDR (arXiv:2511.11990)**: 构建 500K 依赖检索数据集，将 Hall_m 从 0.21-0.39 降至 <0.02。验证了 identifier hallucination 是重要错误源且 retrieval 可大幅降低。确认存在。

9. **R3 (NeurIPS 2025, arXiv:2510.24652)**: 通过 reinforced contrastive learning 优化 RAG retriever，在通用 QA 任务上验证了 co-adaptive retrieval 可行。未应用于 autoformalization。确认存在。

10. **FormalEvolve (arXiv:2603.19828)**: 将 autoformalization 建模为 budgeted evolutionary search，SH@100=58.0% CombiBench / 84.9% ProofNet。搜索固定模型输出空间，无权重更新，不利用编译错误结构。确认存在。

11. **MathAtlas (arXiv:2605.14061, May 2026)**: 52K graduate-level problems，best baseline 在 MA-Hard 上仅 2.6%。含 178K dependency relations。确认存在，确认其极高难度。

12. **TEMPO (arXiv:2604.19295, Apr 2026)**: 将 TTT 形式化为 EM 过程，证明 omitting critic recalibration 导致 ELBO 退化。OLMO3-7B AIME 2024: 33.0%→51.1%。概念上与 TTRA 的 dual-loop 有平行关系。确认存在。

13. **AMBER / Construction-Verification (arXiv:2602.01291)**: 对 DeepSeek-R1 在 applied math 上的 3189 个编译错误分类，47.3% 为 identifier hallucination。确认存在。

14. **Reinforced Co-adaptation Framework (arXiv:2602.22584)**: 工业 RAG 中通过 GRPO + multi-dimensional rewards 联合优化 retrieval 和 generation，减少 72% hallucination。验证 co-adaptive RAG 方向可行，但在 FAQ/客服场景，非形式化数学。

- **调研总结**: Autoformalization 领域 2025-2026 年处于快速发展期。RL for autoformalization（FormaRL、Wang et al.）、retrieval-augmented autoformalization（Aria、DDR、DRIFT）、test-time RL（TTRL）、co-adaptive retrieval（R3、Reinforced-IR）分别是活跃的研究线。但这四条线尚未交叉：(a) 现有 RL for autoformalization 均为 training-time；(b) 现有 retrieval-augmented autoformalization 均用 static retriever；(c) 现有 TTRL 均面向 informal reasoning 的 binary reward；(d) 现有 co-adaptive retrieval 未应用于 Lean 4。Proposal 的定位——在这四条线的交叉点上——是一个真实存在的 gap。

【Trivial Alternative 检验】:

最直接的 trivial alternative 是 **Best-of-N sampling + CriticLean filtering + static DDR retrieval**：给定同等 test-time compute，从 base formalizer（如已 SFT/RL 训练好的模型）采样大量候选，用 DDR 做 static retrieval 增强，然后用 CriticLean 过滤。这不需要 test-time 权重更新，也不需要 co-adaptive retrieval。

Proposal 的增量价值在两处：
1. **Weight adaptation**：当模型的 output space 根本不包含正确的 OOD formalization 时（MathAtlas MA-Hard 2.6%），任何 inference-time scaling 都无法找到不存在的解。这个论点在概念上成立，但实证强度取决于 OOD 程度——如果 pass@128 或 pass@512 仍然很低，才能证明 weight adaptation 是必要的。
2. **Co-adaptive retrieval**：static retriever 无法跟踪 formalizer 在 TTRL 过程中行为的漂移。但这个论点有一个隐含假设：formalizer 在 50-200 步 TTRL 后行为漂移足够大，以至于 static retriever 的 recall 显著下降。这一点未被验证。

**结论**：Trivial alternative 威胁是 **中等** 的。在 near-OOD 场景下，Best-of-N + static RAG + CriticLean filtering 可能已经足够好。增量价值主要体现在 far-OOD 场景（如 MA-Hard），前提是 inference-time scaling 确实触顶。Proposal 意识到了这一点并包含了 compute-matched baseline，这是正确的。

【前提假设检验】:

核心 claim 的逻辑链条包含以下未经验证的假设：

1. **"Lean 4 的 unknownIdentifier 错误可以作为 oracle-quality retrieval training signal"** — 这是整个 co-adaptive retrieval 的基石。概念上合理（错误确实指名缺失的 identifier），但实际有两个子假设：(a) 错误中提到的 identifier 确实对应 Mathlib 中可检索的常量（而非 locally-defined 变量或 model 自创的名字），(b) 基于这些 positives/negatives 的 InfoNCE 训练在仅 ~240 对/cycle 的信号密度下能有效更新 retriever。假设 (a) 的 Phase -1 micro-analysis 是合理的验证手段；假设 (b) 的低数据量下 contrastive learning 效果存疑。

2. **"CriticLean 在 OOD + 严重 class imbalance (<10% compilable) 下仍可用"** — CriticLean 训练于 balanced 250/250 distribution，在 <10% compilable 的 TTRL distribution 下 precision 可能大幅下降（误将错误 formalization 判为正确）。Phase 0 calibration 是必要的，但如果 precision 不过关，整个 reward structure 需要大幅调整。这是一个 **高风险假设**。

3. **"Binarize-then-enrich 保留 DDRL 的 debiasing 性质"** — 先 binarize（compilation AND critic），然后在 accepted candidates 中加 BEq enrichment。DDRL 的理论分析基于 binary reward 的特定结构；加入连续的 enrichment 是否破坏 debiasing 性质未被分析。这是一个 **中等风险假设**。

4. **"TTRL 过程中 formalizer 行为漂移足以使 static retriever 失效"** — 这是 co-adaptive retrieval 必要性的前提。在 TTRL 的典型步数（几百步）内，8B 模型的权重更新幅度是否足以改变 retrieval 需求模式是未知的。如果漂移很小，co-adaptive retrieval 的增量价值就很小。

5. **"Compilation success rate 在 OOD TTRL 中能从极低 baseline 逐步上升"** — 如果 MA-Hard 的 pass@32 在 TTRL 初期接近 0%，GRPO 几乎收不到 positive signal，可能无法启动学习。Curriculum（Phase 4）部分缓解了这一问题，但 cold-start 风险仍在。

【3 维度打分】:

1. **Novelty: 中（偏强）** — 
   核心 novelty 在于识别并利用 formal language 与 informal reasoning 之间的 **结构性不对称**：Lean 4 的编译错误提供了 oracle-quality、token-level 的 retrieval training signal，这在 informal reasoning 中不存在。这一 insight 是 **genuinely novel** 的——R3 (NeurIPS 2025) 和 Reinforced-IR (ACL 2025) 验证了 co-adaptive retrieval 的可行性，但未在 formal language setting 中利用编译器反馈作为 retrieval signal；Aria (ICLR 2026) 和 DDR 做了 retrieval for autoformalization 但 retriever 是 static 的；FormaRL (COLM 2025) 和 Wang et al. 做了 RL for autoformalization 但在 training time 且无 retrieval adaptation。四条研究线的交叉点确实是空白。
   
   然而，novelty 的限制在于：(a) 这本质上是一篇 **combination paper**——将 DDRL + GDPO + CriticLean + R3/Reinforced-IR 的既有技术应用到新 domain，每个组件的技术贡献是 adaptation 而非 invention；(b) "binarize-then-enrich" 虽填补了 DDRL 论文自述的 future work，但技术深度有限——它是一个 two-layer heuristic 而非有理论支撑的 principled solution；(c) 核心发现如果 positive（"利用结构化反馈比 binary 反馈好"），审稿人可能会说 "intuitive, not surprising"。

2. **Significance: 中** — 
   研究问题本身重要：OOD autoformalization 是实用化形式化数学的关键瓶颈（MathAtlas MA-Hard 2.6% 说明 SOTA 几乎无法处理 graduate-level math）。如果 TTRA 在 far-OOD 上显著提升（如从 2.6% 到 8-10%），这将是有意义的进展。"Test-time learning as a third scaling axis for formal math" 的 framing 也有启发价值（与 TEMPO 的 EM 视角互补）。
   
   但 significance 受限于：(a) autoformalization 目前仍是一个 **相对 niche** 的子领域，对 broader AI community 的直接影响有限；(b) 方法的可推广性存疑——co-adaptive retrieval via compiler error 是 formal language 特有的，不易迁移到其他 domain；(c) 即使所有组件 work，绝对性能提升可能仍然有限（far-OOD autoformalization 的天花板可能本身很低）。

3. **Related Work: 强** — 
   这是 proposal 最强的维度。覆盖了截至 May 2026 的几乎所有相关工作：RL for autoformalization (FormaRL, Wang et al., ReForm)、retrieval-augmented autoformalization (Aria, DDR, DRIFT, CRAMF, ProofBridge)、TTRL 及其改进 (DDRL, GDPO, T³RL, SCOPE)、semantic critics (CriticLean)、test-time compute (FormalEvolve, TEMPO)、error analysis (AMBER)。每篇工作的差异化定位清晰。对 R3、Reinforced-IR、TTARAG 的 co-adaptive retrieval 线引用准确。我调研中发现的所有关键论文均已被覆盖。唯一可补充的是 Reinforced Co-adaptation Framework (arXiv:2602.22584) 作为工业 RAG 中 co-adaptive 的额外验证。

【概率估计】: [23% - 33%] 中位 27%

【估计理由】: 
Idea 的核心 insight（formal language 的结构化编译反馈可作为 co-adaptive retrieval 的 oracle-quality training signal）是 genuinely novel 且 well-motivated 的，支撑了概率下界不低于 23%。Related work 覆盖极为充分，差异化定位清晰。

但概率受到三方面限制：
- **Novelty 的 "combination" 性质限制了上界**：四个组件（co-adaptive retrieval + CriticLean reward + DDRL debiasing + GDPO multi-reward）中每个的技术贡献都是 adaptation-to-new-domain 而非 fundamental innovation。AAAI 审稿人可能认为这是 "well-engineered integration" 而非 "conceptual breakthrough"。
- **"Surprising" 检验未通过**：核心发现如果 positive（"利用编译器结构化反馈比 binary feedback 好"），这是 intuitive 而非 surprising 的。审稿人不太会写 "I would not have expected this"。
- **系统复杂度过高**：4 phases、dual loops、multi-tier rewards、curriculum learning、多个 go/no-go gates——这些增加了实现可靠性，但也让 paper 读起来像 systems paper 而非 idea paper。在 AAAI 这样的综合会议上，过于复杂的 pipeline 可能被要求 "simplify and focus on the core contribution"。

中位 27% 反映了：idea 方向正确、gap 真实存在、but 核心发现偏 incremental、combination nature 是主要扣分项。

【主要风险】:
1. **Combination paper 风险**：审稿人可能认为将 DDRL + GDPO + CriticLean + R3 组合应用到 autoformalization 是 engineering integration 而非 scientific contribution——"the whole is not greater than the sum of its parts"。每个组件的技术深度不足以独立支撑论文，但组合在一起又过于复杂。
2. **Core finding 缺乏 surprise**：如果实验结果是 "structured feedback > binary feedback" 且 "adaptive retrieval > static retrieval"，审稿人可能会说 "I would have guessed this, the interesting question is by how much, and the margin might not be large enough to justify the complexity"。
```

Sources:
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)
- [DDRL: Understanding and Mitigating Spurious Signal Amplification in Test-Time RL](https://arxiv.org/html/2604.21327)
- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://arxiv.org/abs/2601.05242)
- [CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization](https://arxiv.org/abs/2507.06181)
- [CriticLeanGPT-Qwen3-14B-RL on HuggingFace](https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL)
- [FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)](https://arxiv.org/abs/2508.18914)
- [Aria: An Agent For Retrieval and Iterative Auto-Formalization (ICLR 2026)](https://arxiv.org/abs/2510.04520)
- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)
- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652)
- [FormalEvolve: Neuro-Symbolic Evolutionary Search for Autoformalization](https://arxiv.org/abs/2603.19828)
- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)
- [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/abs/2604.19295)
- [Towards Faithful Industrial RAG: Reinforced Co-adaptation](https://arxiv.org/abs/2602.22584)
- [Online Reinforcement Learning for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)
- [AMBER: Construction-Verification Benchmark](https://arxiv.org/abs/2602.01291)
- [GDPO Explained (AI Papers Academy)](https://aipapersacademy.com/gdpo/)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research data. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- TTRL (arXiv:2504.16084, NeurIPS 2025): 奠基性工作，在无标注数据上用 majority voting 做 pseudo reward 驱动 RL，Qwen-2.5-Math-7B 在 AIME 2024 上 pass@1 提升约 211%。仅适用于有明确数值答案的 informal math，不处理 formal statement。
- DDRL (arXiv:2604.21327, ACL 2026 Findings): 发现 GRPO 在低共识域放大 spurious reward，提出频率平衡采样 + 固定 ±1 advantage + consensus off-policy refinement。明确指出"更丰富的 advantage 公式"为 future work，仅处理 binary reward。确认 proposal 对其描述准确。
- CriticLean (arXiv:2507.06181, 2025): 训练 CriticLeanGPT 模型判断 Lean 4 formalization 的语义正确性，14B-RL 在 balanced CriticLeanBench 上 84.8%。开源模型在 HuggingFace 可用。Proposal 对其 balanced vs. skewed 分布差异的担忧是合理的。
- R3 (arXiv:2510.24652, NeurIPS 2025): 用 RL 环境反馈训练 retriever 的 contrastive learning，1-shot accuracy 平均 +5.2%。验证了"RAG 环境反馈可训练 retriever"这一前提。
- Reinforced-IR (ACL 2025): 交替 RLRF/RLGF 实现 retriever-generator 共适应。验证了 co-adaptive retrieval 的可行性。
- Aria (arXiv:2510.04520, ICLR 2026): 当前 retrieval-augmented autoformalization 的 SOTA，ProofNet 91.6% compilation / 68.5% accuracy，dependency graph + iterative formalization。关键局限：静态 pipeline，retriever 不随 formalizer 演化而更新，模型权重不更新。
- FormaRL (COLM 2025): GRPO + compilation + LLM consistency reward 用于 autoformalization，pass@1 4%→26% on ProofNet。Training-time RL，无 retrieval，无 test-time adaptation。
- FormalEvolve (arXiv:2603.19828, 2026): 将 autoformalization 建模为 budgeted evolutionary search，SH@100=58.0% CombiBench。Test-time compute 但无 weight adaptation，丢弃 compilation error 结构。
- TEMPO (arXiv:2604.19295, 2026): 将 TTT 形式化为 EM 框架，证明省略 critic recalibration 导致 ELBO degradation 和 diversity collapse。概念上支持 proposal 的 dual-loop 设计。
- MathAtlas (arXiv:2605.14061, May 2026): 52K graduate-level 问题 + 178K dependency relations，MA-Hard 最佳仅 2.6%。验证了 OOD autoformalization 的严峻挑战。
- AMBER/Construction-Verification (arXiv:2602.01291, 2026): 47.3% compilation errors 来自 identifier hallucination。支持 proposal 对 Tier 1 error 占比 ≥40% 的预期。

**调研总结**: Autoformalization 领域正在沿三条轴线快速发展：(1) RL-based training (FormaRL, Wang et al.)、(2) retrieval augmentation (Aria, DDR, DRIFT)、(3) test-time compute (FormalEvolve, TTRL)。这三条轴线目前是独立的——没有工作将 test-time RL 应用于 autoformalization，也没有工作在 TTRL 中实现 co-adaptive retrieval。Proposal 定位在三者的交叉点，gap 是真实的。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是 **Best-of-N + CriticLean 过滤**：给基础模型分配等量 test-time compute 采样更多候选，用 CriticLean-14B 过滤，不做任何 weight adaptation。Proposal 已将其纳入 compute-matched baseline，这是好的。

第二个 trivial alternative 是 **static retrieval + TTRL**：直接在 autoformalization 上跑 TTRL，用 compilation-only reward，retriever 固定不更新。这实际上是 proposal 的一个 ablation。

Proposal 对这两个 trivial alternative 有明确的应对。增量价值的核心论证是：(a) weight adaptation 能产生 inference-time scaling 无法到达的 OOD 泛化（因为固定模型的输出空间可能根本不包含正确 formalization），(b) co-adaptive retrieval 利用 compilation error 的结构化信息实现 retriever-formalizer 协同进化。论证逻辑上是通的，但 (a) 的实证支撑依赖于 MathAtlas MA-Hard 2.6% 这个极端数据点，在 moderate OOD 场景下 Best-of-N 可能就够了。

**结论**: Trivial alternative 威胁在 moderate OOD 场景下存在，但在 extreme OOD 场景下 proposal 的论证成立。Proposal 意识到了这一点并设计了 compute-matched baseline。

【前提假设检验】:
核心 claim 的逻辑链有几个关键假设：

1. **"Lean 4 的 structured error 能提供 oracle-quality retrieval training signal"** — 这是最核心的假设。AMBER 的 47.3% identifier hallucination 数据和 DDR 的 Hall_m=0.21-0.39 提供了间接支撑，但这些数据来自不同模型（DeepSeek-R1 / frontier LLMs）、不同设置。在 TTRL 过程中，随着模型权重更新，error 分布会变化——proposal 的 Phase -1 micro-analysis 旨在验证这一假设，这是合理的。此假设有中等程度的实证支撑，但尚未在 TTRL 动态场景下验证。

2. **"CriticLean 在 skewed OOD 分布下仍能保持足够精度"** — CriticLeanBench 是 250/250 balanced，而 OOD TTRL 下 <10% compilable，分布偏移巨大。Proposal 用 Phase 0 calibration + confidence gating 来应对，但这仍是未经验证的假设。如果 CriticLean 在 OOD skewed 分布下 precision 不达标，整个 multi-tier reward 体系的核心组件就不成立。

3. **"Binarize-then-enrich 能有效处理 heterogeneous reward"** — 这是对 DDRL + GDPO 的嫁接，逻辑上合理但完全是未经实验验证的组合。特别是 binarization 层丢弃了 critic 的 soft signal 信息（30-70% ambiguity zone 被排除），这可能在数据稀缺的 OOD 场景下浪费宝贵的训练信号。

4. **"Co-adaptive retrieval 的收益会超过其引入的复杂性和不稳定性"** — 同时更新 formalizer 权重和 retriever 权重是一个 non-trivial 的双优化问题。R3 和 Reinforced-IR 在 QA 场景验证了可行性，但 autoformalization + TTRL 场景的 signal density 更低（50 steps × 32 candidates × ~15% compile rate ≈ 240 对/cycle），retriever 更新的样本效率是个问号。

**结论**: 假设 1 和 2 有 partial evidence 但需要 proposal 中的 de-risking phases 验证；假设 3 和 4 是更强的未验证假设。但 proposal 的 phased design 和 go/no-go gates 表明作者清楚这些风险。

【3 维度打分】:

1. **Novelty: 中偏强** —
理由：核心 insight——"formal languages 的 structured compilation errors 构成一个 graded hierarchy of adaptation signals，使得 co-adaptive retrieval 成为 TTRL 在 formal setting 中独有的 emergent capability"——是真正的 novelty。这不仅仅是"把 A 应用到 B"，而是识别了 formal vs. informal reasoning 之间的一个 structural asymmetry 并系统性地利用它。调研确认无现有工作做到这一点：Aria (ICLR 2026) 是 static retrieval，FormaRL (COLM 2025) 是 training-time RL without retrieval，FormalEvolve 丢弃 error structure，TTRL 仅处理 informal math。Gap 是真实的。

但我必须指出两个 novelty 折扣：(a) 这是一个 **combination paper**——四个独立验证的组件的首次整合。每个组件单独看（co-adaptive retrieval, TTRL, critic reward, debiased RL）都已有前人工作，novelty 来自组合而非单个突破。AAAI 审稿人可能以"engineering novelty"而非"conceptual novelty"定性。(b) "Binarize-then-enrich"这个贡献虽然填补了 DDRL 的 explicit future work gap，但本身较为 incremental——本质是在 DDRL 的 binary framework 上叠加 GDPO 的 per-reward normalization。

2. **Significance: 中偏强** —
理由：OOD autoformalization 是一个重要且日益突出的问题。MathAtlas MA-Hard 2.6%（arXiv:2605.14061）量化了现有方法在 graduate-level 数学上的惨淡表现。如果 TTRA 能在 OOD 域上显著提升 autoformalization 质量，对 formal mathematics、AI for math、proof assistants 社区都有实际影响。

Test-time adaptation 作为 formal math 的"第三 scaling axis"（complementing training-time 和 inference-time compute）的 framing 具有概念上的吸引力，并与 TEMPO (arXiv:2604.19295) 的 TTT 叙事相呼应。

但 significance 的上限受限于：autoformalization 仍是一个相对 niche 的子领域。虽然 AAAI 作为综合 AI 会议接受范围很广，但 reviewer pool 中深度理解 Lean 4 + TTRL + retrieval 这个交叉点的人有限。如果 reviewer 不具备足够背景，可能低估 contribution。

3. **Related Work: 强** —
理由：Proposal 对 related work 的覆盖在我调研范围内是全面且准确的。所有我查证的关键论文（TTRL、CriticLean、DDRL、R3、Reinforced-IR、Aria、FormaRL、FormalEvolve、TEMPO、MathAtlas、AMBER）均真实存在，描述准确，差异化定位清晰。Proposal 不仅列出了竞争工作，还精确指出了每个工作的局限性与 TTRA 的差异。对 6 个子方向（RL for autoformalization, semantic critics, debiased RL, retrieval-augmented autoformalization, test-time compute, error analysis）的分类组织清晰。

特别值得肯定的是：proposal 将最近的工作（TEMPO April 2026, MathAtlas May 2026, Dymetman May 2026）也纳入了 landscape 分析，说明作者持续跟踪领域动态。唯一的小缺陷是部分引用密度过高，可能在实际论文中需要精简以保持可读性。

【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
Novelty 是"中偏强"而非"强"，因为这本质是一个 combination/integration paper。核心 insight（structural asymmetry enabling co-adaptive retrieval as emergent TTRL capability）是真正的 novelty，但四个组件的整合属于 system-level contribution。AAAI 审稿人对 combination novelty 的接受度因人而异。Significance 在 autoformalization 社区内是强的，但受限于子领域的 niche 程度。Related work 覆盖出色，不构成扣分因素。

上界受限于 **Novelty 的 combination 性质**：如果审稿人认为"each piece exists, you just put them together"，evaluation 无论多精致都无法拯救。下界受支撑于 **gap 的真实性和 insight 的原创性**：no existing work exploits structured compilation errors for co-adaptive retrieval during TTRL，这一点在领域调研中得到了确认。

【主要风险】:
1. **"Lego novelty" 批评**：审稿人可能认为 TTRA 是四个现有技术（TTRL + co-adaptive retrieval + CriticLean + DDRL/GDPO）的工程整合，而非概念突破。Proposal 对 structural asymmetry 的论述需要在论文中更加突出以对冲这一批评。
2. **系统复杂性与可归因性**：dual-loop + multi-tier reward + progressive curriculum + critic calibration 的复杂度极高。如果实验结果是 moderate improvement，审稿人难以判断哪个组件真正起作用；如果是 negative 或 mixed result，复杂性本身成为攻击面（"too many moving parts, unclear what matters"）。
```

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

- TTRL (NeurIPS 2025, arXiv:2504.16084): 首个在无标注数据上通过多数投票产生伪标签进行 test-time RL 的工作。Qwen2.5-Math-7B 在 AIME 2024 上 pass@1 提升 ~211%。仅适用于有确定数值答案的非形式化数学推理——多数投票对形式化语句不适用。TTRA 的出发点正是解决这一局限。

- DDRL (ACL 2026 Findings, arXiv:2604.21327): 识别并修复 GRPO 在低共识区间对伪奖励的放大效应。使用频率感知平衡采样 + 固定 ±1 advantage + 共识离策略精炼。在 AIME 2024 上对 Qwen2.5-Math-1.5B 实现 19% 相对提升。但**明确限于二值奖励**，作者自己将多层级奖励列为 future work。TTRA 的 binarize-then-enrich 直接回应此 gap。

- GDPO (NVIDIA, arXiv:2601.05242): 解决多奖励 GRPO 训练中信号坍缩问题，对每个奖励分量独立归一化。在 AIME 上对 DeepSeek-R1-1.5B 精度提升 6.3%。但不处理伪标签噪声/去偏。TTRA 将 GDPO 的多奖励归一化与 DDRL 的去偏结合。

- CriticLean (arXiv:2507.06181, ByteDance/南京): CriticLeanGPT-14B-RL 在平衡 CriticLeanBench 上达 84.8% 准确率。首个训练专门的语义评判器来评估 Lean 4 形式化是否忠实于原始语义。但**基准分布是 250/250 平衡**的，与 OOD TTRL 中 <10% 可编译的极度偏斜分布不同。TTRA 的 Phase 0 校准协议正是针对此分布偏移。

- FormaRL (COLM 2025, arXiv:2508.18914): 首个用 GRPO 做 autoformalization RL 的工作。编译检查 + LLM 一致性检查作为奖励。Qwen2.5-Coder-7B 在 ProofNet 上 pass@1 从 4.04% 提升至 26.15%。但是**训练时 RL**，无 test-time 适应，无检索。

- Wang et al. (NeurIPS 2025 MAR Workshop): 在线 RL for autoformalization，使用 GRPO + BEq + embedding 奖励。TC1: 17.29%→26.01%。最接近的先前工作，但仍是**训练时、分布内**，无检索，无 test-time 适应，无训练过的语义评判器。

- Aria (ICLR 2026, arXiv:2510.04520): 当前检索增强 autoformalization 的 SOTA。通过依赖图分解 + 迭代形式化 + AriaScorer 在 ProofNet 上达 91.6% 编译 / 68.5% 精度，在同调猜想上 42.9%（其他系统 0%）。关键局限：**检索器是固定的**，不随形式化器行为漂移而适应；**模型权重不更新**。

- DDR (arXiv:2511.11990): 构建 500K 样本依赖数据集。量化前沿 LLM 的标识符幻觉率 Hall_m=0.21-0.39，通过检索降至 <0.02。证实标识符幻觉是可量化的主要错误模式。

- AMBER/Construction-Verification (arXiv:2602.01291): 在 3,189 个编译错误中，47.3% 来自标识符幻觉（DeepSeek-R1 在应用数学上）。为 TTRA 关于 Tier 1 错误占主导的假设提供独立实证。

- FormalEvolve (arXiv:2603.19828): 将 autoformalization 表述为有预算的进化搜索。SH@100 在 CombiBench 58.0%，ProofNet 84.9%。**搜索固定模型的输出空间，不做权重适应或检索器共适应**。与 TTRA 正交。

- TEMPO (arXiv:2604.19295): 将 TTT 形式化为 EM（策略精炼 = M-step，评判器重校准 = E-step）。证明省略重校准导致 ELBO 退化和多样性坍缩。为 TTRA 的双循环设计提供概念支撑。

- T³RL (arXiv:2603.02203): 将外部工具验证引入 TTRL，用代码执行输出加权投票。但**将工具反馈压缩为单个二值信号**（verified/unverified），丢弃工具输出的内部结构。

- R3 (NeurIPS 2025, arXiv:2510.24652): 通过强化对比学习优化 RAG 检索。在通用 RAG 上提升 5.2%。验证了基于环境反馈训练检索器的范式可行性。

- Reinforced-IR (ACL 2025): 交替 RLRF/RLGF 实现检索器-生成器互适应。验证共适应检索的范式，但未应用于 autoformalization。

- MathAtlas (arXiv:2605.14061, May 2026): 52K 研究生级数学问题，178K 依赖关系。最强基线仅 9.8% 定理正确率，MA-Hard 上 2.6%。证实 OOD autoformalization 是未解决的挑战。

- **调研总结**: Autoformalization 领域正处于方法快速演进阶段：训练时 RL（FormaRL, Wang et al.）、检索增强（Aria, DDR, DRIFT）、推理时搜索（FormalEvolve）、语义评判（CriticLean）各自取得显著进展，但**尚无工作将 test-time RL 应用于 autoformalization**，也**无工作在 TTRL 中实现检索器共适应**。TTRA 位于这些独立研究线的交汇处，填补的是一个真实存在的空白。

【Trivial Alternative 检验】:

最直接的 trivial alternative 是 **Best-of-N 采样 + CriticLean 过滤 + 静态检索**（即 Aria 风格的检索 + 大量采样 + CriticLean 打分筛选）。Proposal 已预见到这一点并将其作为 compute-matched baseline。关键问题是：TTRA 的权重适应相对于这个 trivial baseline 的增量价值是什么？

Proposal 的论证是：对于真正的 OOD 领域（MathAtlas MA-Hard: 2.6%），固定模型的输出空间可能根本不包含正确的形式化——无论采样多少次都无法找到模型无法生成的内容。这个论证在概念上是合理的，但其成立程度取决于 OOD 的"远"程度。对于中等 OOD，Best-of-N + 检索可能已经足够。因此 TTRA 的增量价值主要体现在**极端 OOD 场景**，这限制了其适用范围但也提高了其在该场景下的 significance。

另一个 trivial alternative：**标准 SFT/继续预训练在 OOD 领域数据上** + 静态检索。如果有少量 OOD 领域的标注数据，常规微调可能比 TTRL 更简单有效。但 TTRA 的设定是**无标注 OOD 数据**的 test-time 适应，这使得这个 alternative 不完全可比。

**结论**：存在 trivial alternative 威胁，但 proposal 已明确将其纳入实验对比。增量价值的论证在极端 OOD 场景下合理，在中等 OOD 场景下需实验验证。

【前提假设检验】:

1. **"Lean 4 结构化错误信号可以作为检索器训练的 oracle-quality 信号"** — **部分成立，但有过度声称的风险**。当编译器报告 `unknownIdentifier "Finset.sum_bij"` 时，确实直接指出需要的标识符。但"oracle-quality"措辞过强：(a) 模型可能幻觉出不存在的标识符名称，此时错误信号指向一个不存在的目标；(b) 对于 Tier 2 错误（类型不匹配），从错误信息到正确依赖的映射并不总是一对一的。AMBER 的 47.3% 数据支持 Tier 1 错误占主导，但这是 DeepSeek-R1 的数据，TTRA 使用 Qwen3-8B 可能分布不同——Phase -1 旨在验证此点。

2. **"CriticLean-14B 在极度偏斜分布下仍可保持足够精度"** — **未经验证但有合理的去风险策略**。CriticLeanBench 是 250/250 平衡的，而 OOD TTRL 中 <10% 可编译。Phase 0 的 go/no-go gate 是合理的，但如果 CriticLean 在此分布下精度不足，整个框架的核心组件就失效了。

3. **"共适应检索的增量收益足够显著"** — **最关键的未验证假设**。R3 和 Reinforced-IR 在通用 RAG 上验证了共适应检索的价值，但 autoformalization 的检索空间（Mathlib 26K+ 定义）结构非常不同于通用文档检索。FAISS 在高频重建下的性能开销也是实际考量。

4. **"DDRL 的去偏 + GDPO 的多奖励归一化可以直接组合"** — **合理但简化**。两个方法各自被验证，但它们的组合是否引入新的交互效应（如去偏采样改变了多奖励归一化的有效样本分布）未被讨论。

5. **"TTRL 中的政策漂移不会导致检索器训练信号退化"** — Proposal 引用 TEMPO 的 EM 分析，但 TEMPO 处理的是评判器重校准而非检索器。检索器-形式化器共适应可能存在不同的稳定性特征。

【3 维度打分】:

1. **Novelty: 中** — 

TTRA 的核心 novelty 是一个**领域交叉集成创新**：将 co-adaptive retrieval（R3, Reinforced-IR 验证了范式）、test-time RL（TTRL 验证了范式）、debiased multi-tier reward（DDRL + GDPO 各自验证了组件）、semantic critic（CriticLean 验证了工具）四条独立研究线首次组合应用于 autoformalization。

关键创新点：
- **Lean 4 结构化错误 → 检索器训练信号** 的洞察是非平凡的，在我的调研范围内确实无先前工作发现并利用此联系。T³RL 将工具反馈压缩为二值信号丢弃了内部结构，FormalEvolve 仅用编译成功/失败，Aria 的检索器不适应——TTRA 对此的差异化定位清晰。
- **Binarize-then-enrich** 直接回应 DDRL 论文自身声明的 future work，填补真实 gap。

但需要诚实承认：
- 这本质上是一个**系统集成**论文，每个组件独立存在，novelty 在于组合而非单个组件。
- "形式语言提供比二值奖励更丰富的反馈"这一核心洞察，一旦被陈述出来就显得**合理但不令人惊讶**——reviewer 可能会说 "of course compilers give richer feedback"。
- Binarize-then-enrich 的技术贡献相对直接（在 DDRL 的二值化层上叠加 GDPO 的多奖励归一化）。

2. **Significance: 中偏强** — 

问题本身重要：OOD autoformalization 是真实且困难的挑战（MathAtlas MA-Hard 2.6% 证实了这一点）。如果 TTRA 成功，它：
- 建立 test-time learning 作为形式数学的第三个 scaling axis（训练时、推理时之外），这是有影响力的框架性贡献
- 提供首个将 TTRL 扩展到非数值答案领域（形式化语句）的方法，可能推广到其他有结构化编译/验证反馈的任务（如代码生成）
- 解决 static retriever 不适应 policy drift 的已知局限（Aria 的核心瓶颈之一）

但 significance 受限于：
- 实际影响取决于改进幅度——如果在 MathAtlas MA-Hard 上从 2.6% 到 5%，技术上有意义但实用价值有限
- 应用场景相对窄（Lean 4 autoformalization with Mathlib），不是一个通用方法
- 资源需求高（1400-1900 A100-hours），但这不影响 idea 评估

3. **Related Work: 强** — 

这是整个 proposal 最强的维度。覆盖了：
- 6 个相关研究方向的所有核心工作
- 每篇工作的具体数据、局限性和与 TTRA 的差异
- 最新至 2026 年 5 月的工作（MathAtlas, Dymetman binary rewards）
- 明确的差异化定位：对 Aria（静态检索器）、DDRL（二值奖励限制）、T³RL（丢弃工具反馈结构）、FormalEvolve（无权重适应）等逐一清晰区分

我的调研验证了 proposal 中引用的论文均真实存在，描述基本准确。未发现遗漏的重要竞争工作。唯一轻微疏漏：proposal 未充分讨论 **Lean 4 Cycle Consistency Fine-tuning** (arXiv:2603.24372) 等更小规模但相关的工作，但这不影响核心定位。

【概率估计】: [28% - 38%] 中位 32%

【估计理由】: 

Novelty 是限制上界的主要维度。TTRA 是一个高质量的系统集成工作，而非根本性的方法论创新。核心洞察（Lean 4 错误信号 → 检索器训练信号）虽然在调研范围内确认为 novel，但不属于"反直觉"级别——一旦认识到形式语言的结构化反馈优势，方法论自然跟进。审稿人可能会评价为 "well-motivated combination, but the individual pieces are not new"。

Significance 处于中偏强：问题重要（OOD autoformalization 确实困难且未解决），框架性贡献（第三 scaling axis）有价值，但应用面相对窄。

Related Work 是强项，不会成为被拒原因。

综合来看：这个 proposal 的 idea 内核处于 "方向正确 + 有真实 novelty delta + 但核心发现 if positive 审稿人大概率说 'makes sense, well-engineered' 而非 'surprising'" 的区间，对应 rubric 中 25-35% 的锚点。考虑到 related work 极其充分且问题的时效性/重要性，上调至 28-38%，中位 32%。

【主要风险】: 
1. **"组合 vs 创新" 的审稿人争论**：核心贡献是四条研究线的首次组合，每个组件独立存在。审稿人可能认为 "engineering contribution > intellectual contribution"，尤其是如果 binarize-then-enrich 被认为是 DDRL + GDPO 的直接拼接。
2. **核心洞察的 surprise 不足**："形式语言编译器提供比二值奖励更丰富的反馈" 这一洞察，虽然在此前工作中未被利用，但陈述后显得近乎显然，可能被审稿人认为缺乏深度——从而将整体贡献降级为 "a solid system paper" 而非 "a paper with a deep new insight"。
```

Sources:
- [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/pdf/2504.16084)
- [DDRL: Spurious Signal Amplification in TTRL](https://arxiv.org/html/2604.21327)
- [GDPO: Group reward-Decoupled Normalization](https://arxiv.org/abs/2601.05242)
- [CriticLean: Critic-Guided RL for Mathematical Formalization](https://arxiv.org/abs/2507.06181)
- [FormaRL: Enhancing Autoformalization with no Labeled Data](https://arxiv.org/abs/2508.18914)
- [Online RL for Autoformalization](https://www.researchgate.net/publication/396825045_Online_Reinforcement_Learning_for_Autoformalization)
- [R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning](https://arxiv.org/abs/2510.24652)
- [Aria: An Agent for Retrieval and Iterative Auto-Formalization](https://arxiv.org/abs/2510.04520)
- [DDR: Improving Autoformalization Using Direct Dependency Retrieval](https://arxiv.org/abs/2511.11990)
- [FormalEvolve: Neuro-Symbolic Evolutionary Search](https://arxiv.org/abs/2603.19828)
- [TEMPO: Scaling Test-time Training for Large Reasoning Models](https://arxiv.org/abs/2604.19295)
- [T³RL: Tool Verification for Test-Time RL](https://arxiv.org/abs/2603.02203)
- [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)
- [AMBER/Construction-Verification Benchmark](https://arxiv.org/abs/2602.01291)
- [TTARAG: Test Time Adaptation for RAG](https://arxiv.org/abs/2601.11443)
- [CriticLeanGPT-Qwen3-14B-RL on HuggingFace](https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL)


【原始 proposal（允许参考但不是主要依据）】:
# TTRA: Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization

## Core Problem

Current autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Test-time RL (TTRL) has been shown to boost informal math reasoning but cannot be naively applied to autoformalization: (1) majority voting over formal statements is ill-defined (unlike numerical answers), requiring a trained semantic critic; (2) GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels in multi-tier reward settings; and (3) static retrieval of Mathlib dependencies becomes stale as the formalizer's behavior shifts during adaptation.

A key structural asymmetry motivates our approach: in informal math reasoning, TTRL obtains only binary correct/incorrect signals with no information about *why* a solution failed or *what knowledge is missing*—and binary rewards create a fundamental degeneracy for policy gradient methods, leading to diversity collapse (Dymetman, arXiv:2605.02375). In contrast, Lean 4's compiler produces machine-parseable error messages that precisely identify missing identifiers, type mismatches, and unresolved typeclass instances—constituting a graded hierarchy of structured feedback signals. Critically, these signals are not merely "richer rewards": when a compilation error reports `unknownIdentifier "Finset.sum_bij"`, it provides an oracle-quality, token-level retrieval training signal that directly specifies which Mathlib dependency is needed. Such signals are unavailable during pre-training or SFT (no compilation feedback), discarded by inference-time search methods like FormalEvolve (which uses only compile success/failure), and unexploited by static retrieval pipelines like Aria (whose retriever cannot adapt). Only during test-time RL can these structured error signals be continuously collected and used to co-adapt the retriever—making co-adaptive retrieval an emergent capability uniquely enabled by TTRL in formal language settings.

For domains where model performance is extremely low (MathAtlas MA-Hard: 2.6%), inference-time scaling alone is insufficient: the fixed model's output space may not contain correct formalizations for truly OOD domains, so no amount of sampling can find what the model cannot generate. Weight adaptation is necessary, and it produces compounding improvement—better formalizations yield more informative compilation errors, which improve the retriever, which enables even better formalizations in subsequent rounds.

## Research Opportunity

Four independently validated capabilities have never been combined, and their integration is enabled by the structured feedback properties unique to formal languages.

(1) **Co-adaptive retrieval is newly feasible, and identifier hallucination is a quantifiably dominant error mode.** R3 (NeurIPS 2025) demonstrates that RAG environment feedback can train retrievers via reinforced contrastive learning. Reinforced-IR (ACL 2025) validates alternating retriever-generator mutual adaptation through RLRF/RLGF. TTARAG (arXiv:2601.11443, Jan 2026) shows test-time retrieval adaptation via self-supervised prediction. The prevalence of identifier hallucination is established by converging evidence: the Construction-Verification/AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors from DeepSeek-R1 on applied math stem from hallucination of non-existent theorems/definitions. DDR (arXiv:2511.11990) quantifies Hall_m=0.21-0.39 across frontier LLMs, reduced to <0.02 with retrieval. The RAutoformalizer (ICLR 2025 Spotlight) treats 'Hallucination' as a primary error class. MathAtlas (arXiv:2605.14061, May 2026) shows a 66% advantage for Mathlib-grounded definitions (27.9% vs 16.8%, p<0.001). Yet no work applies co-adaptive retrieval to Lean 4 dependency retrieval during RL—where Lean's structured error taxonomy provides graded, machine-parseable signals for retriever training.

(2) **TTRL with debiasing has advanced but remains limited to binary rewards in informal settings.** DDRL (ACL 2026 Findings) fixes GRPO's spurious signal amplification via frequency-based balanced sampling, fixed ±1 advantages, and consensus-based off-policy refinement (19.0% relative improvement over ETMR on AIME 2024; 4.0pp absolute: 21.0→25.0 for Qwen2.5-Math-1.5B), but assumes binary rewards with 'more expressive advantage formulations' left as future work. GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward GRPO through per-reward decoupled normalization but does not address debiasing. T³RL (arXiv:2603.02203, Mar 2026) introduces tool-verified rewards into TTRL, using code execution output to upweight verified rollouts—but collapses all tool feedback into a single binary bit (verified/unverified), discarding the internal structure of tool output. SCOPE (arXiv:2512.15146, Dec 2025) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, but remains within the homogeneous binary-reward paradigm. The combination of DDRL's debiasing with GDPO's multi-reward normalization for heterogeneous reward components (hard binary gate + noisy soft critic + drifting population statistic) has not been attempted.

(3) **CriticLean provides the missing semantic reward signal.** CriticLeanGPT-14B-RL (arXiv:2507.06181, July 2025) achieves 84.8% accuracy on balanced CriticLeanBench (87.0% for 32B), but CriticLeanBench's 250/250 balanced distribution differs from OOD TTRL's heavily skewed distribution (<10% compilable). This distributional shift gap motivates our Phase 0 calibration protocol.

(4) **Online RL for autoformalization validated at training time only.** Wang et al. (NeurIPS 2025 MAR Workshop) achieves TC1: 17.29%→26.01% on RLMEval using GRPO with BEq + embedding rewards, but operates at training time on in-distribution problems without retrieval, test-time adaptation, or a trained semantic critic.

Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server, open-source CriticLeanGPT models) makes the combined approach newly feasible.

## Research Landscape

**(1) RL for autoformalization.** FormaRL (COLM 2025) applies GRPO with compilation + LLM consistency rewards (pass@1: 4%→26% on ProofNet). Online RL for Autoformalization (Wang et al., NeurIPS 2025 MAR Workshop) uses GRPO with BEq + embedding similarity (TC1: 17.29%→26.01%, TC50: 76.41%→85.46% on RLMEval)—closest prior work but training-time, no retrieval, no test-time adaptation. ReForm (arXiv:2510.24592) applies PBSO position-aware RL rewards for reflective autoformalization; ReForm-8B (Qwen3-8B) achieves +18.0pp average improvement.

**(2) Semantic critics and iterative refinement.** CriticLean (July 2025) introduces CriticLeanGPT (32B-RL: 87.0%, 14B-RL: 84.8% on balanced CriticLeanBench). ATF achieves 94.51% Pass@1 on FormalMath-Lite via SFT + expert iteration + DPO. Monotonic Refinement achieves 90.27% on miniF2F through multi-model ensemble orchestration. These cannot adapt model weights to new domains.

**(3) Debiased RL, multi-reward optimization, and TTRL reward improvements.** DDRL (ACL 2026 Findings) addresses GRPO's spurious signal amplification exclusively with binary rewards; GDPO (NVIDIA, arXiv:2601.05242) addresses multi-reward normalization. Binary Rewards and RL (Dymetman, arXiv:2605.02375, May 2026) proves binary rewards create fundamental degeneracy (diversity collapse). T³RL (arXiv:2603.02203, Mar 2026) introduces external tool verification into TTRL, upweighting verified rollouts via verification-aware voting—but treats tool output as a single binary signal (verified/unverified), discarding the structured content of tool feedback. SCOPE (arXiv:2512.15146) improves TTRL reward via step-wise confidence and dynamic subgroup partitioning, remaining within the homogeneous binary-reward paradigm. All these improvements assume homogeneous reward signals. TTRA addresses a qualitatively different problem: heterogeneous reward components (hard compilation gate, noisy critic signal, policy-drifting BEq statistic) requiring a two-layer binarize-then-enrich adaptation.

**(4) Retrieval-augmented autoformalization and co-adaptive retrieval.** Aria (ICLR 2026, arXiv:2510.04520) achieves ProofNet 91.6% compilation / 68.5% accuracy and 42.9% on homological conjectures (vs. 0% for all others) via dependency graph + iterative formalization + AriaScorer—current frontier of retrieval-augmented autoformalization, but a fixed inference pipeline: retriever does not adapt to formalizer's evolving behavior and model weights are not updated. DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF. DDR builds a 500K-sample dataset (Hall_m reduced from 0.21-0.39 to <0.02). CRAMF indexes 26K+ Mathlib definitions. ProofBridge (ICLR 2026, arXiv:2510.15681) uses joint embeddings + retrieval-augmented fine-tuning. On co-adaptive retrieval: R3 (NeurIPS 2025, arXiv:2510.24652) optimizes RAG retrieval via reinforced contrastive learning; Reinforced-IR (ACL 2025) alternates RLRF/RLGF; TTARAG (arXiv:2601.11443) demonstrates test-time retrieval adaptation. None applied to autoformalization or Lean 4.

**(5) Test-time compute for autoformalization.** FormalEvolve (arXiv:2603.19828, Mar 2026) formulates autoformalization as budgeted evolutionary search (SH@100=58.0% CombiBench, 84.9% ProofNet) using LLM-driven mutation/crossover with AST rewrites. This is orthogonal to TTRA: FormalEvolve searches a fixed model's output space without weight adaptation or retriever co-adaptation, discarding compilation error structure. TEMPO (arXiv:2604.19295, Apr 2026) formalizes test-time training as EM (policy refinement = M-step, critic recalibration = E-step), proving that omitting recalibration leads to ELBO degradation and diversity collapse—a conceptual parallel to TTRA's dual-loop where omitting retriever co-adaptation (= static retrieval TTRL) accumulates retriever-formalizer distribution mismatch.

**(6) Error analysis and identifier hallucination.** The AMBER benchmark (Yang et al., arXiv:2602.01291, Feb 2026) finds 47.3% of 3,189 compilation errors are identifier hallucination (32.7% competence, 15.2% incomplete, 4.8% syntax). RAutoformalizer (ICLR 2025 Spotlight) categorizes errors into 'Hallucination' vs 'Others'. MathAtlas (arXiv:2605.14061) introduces 52K graduate-level problems (best: 2.6% on MA-Hard).

After exhaustive search through May 2026, no work combines co-adaptive retrieval exploiting Lean 4's structured error taxonomy during test-time RL, a calibrated semantic critic with distributional shift analysis, principled adaptation of binary-reward debiased RL to heterogeneous multi-tier rewards, and test-time adaptation on unlabeled OOD domains. Existing retrieval methods (Aria, DRIFT, DDR) use static retrievers; existing RL methods (FormaRL, Wang et al., ReForm) operate at training time; existing test-time methods (FormalEvolve) search without learning; existing TTRL improvements (T³RL, SCOPE, DDRL) assume homogeneous binary rewards.

## Proposed Approach

We propose TTRA (Test-Time Retrieval-Augmented autoformalization), making TTRL viable for autoformalization through three technical innovations unified by a single insight: formal languages' structured compilation feedback creates a graded hierarchy of adaptation signals unavailable in informal reasoning, enabling co-adaptive test-time learning as a new scaling axis for formal mathematics—complementing training-time compute (more data, larger models) and inference-time compute (more samples, longer search). Drawing a conceptual parallel with TEMPO's EM formalization of TTT, TTRA's dual-loop design ensures the retriever co-adapts with the formalizer (analogous to not omitting the E-step), preventing the retriever-formalizer distribution mismatch that would degrade a static-retrieval TTRL.

**Phase -1 — Error Signal Coverage Micro-Analysis (2-3 days).** Quantify Lean 4 error taxonomy coverage on OOD domains. Compile 500 candidate formalizations on Con-NF and 500 on MathAtlas MA-Hard, classify errors into: Tier 1 (direct identifier: `lean.unknownIdentifier`, `unknown namespace`), Tier 2 (type-based: `type mismatch`, `failed to synthesize instance`), Tier 3 (indirect: tactic/elaboration/syntax errors). Thresholds: Tier 1 ≥40% → co-adaptive retrieval well-supported; 20-40% → rely on Tier 1+2; <20% → fall back to Tier 2 with type-signature matching. Prior evidence strongly supports ≥40% (AMBER: 47.3%; DDR: Hall_m=0.21-0.39; RAutoformalizer treats 'Hallucination' as primary class; CRAMF documents systematic fabrication). Phase -1 validates on our specific model/domain. Simultaneously verify MathAtlas MA-Hard gold formalization coverage; if <50%, downgrade to secondary benchmark and activate IndiMathBench (arXiv:2512.00997) as contingency OOD benchmark. Resource: ~8 A100-hours generation, ~10 CPU-hours parsing.

**Phase 0 — Minimal Pilot with Critic Calibration (De-risking).** FormaRL's GRPO pipeline with CriticLean-14B replacing LLM-consistency reward. 200 Con-NF + 200 FormalMATH number theory problems. Primary hypothesis: ≥3pp BEq@1 over compilation-only GRPO on Con-NF. Critic calibration under distributional shift: measure precision/recall separately on skewed distribution (<10% compilable); report calibration curves; if precision <80%, introduce confidence gating >0.8. Go/no-go: proceed only if primary hypothesis confirmed AND precision ≥80%. Additionally, establish critic calibration monitoring protocol: during subsequent TTRL phases, checkpoint critic precision every ~100 GRPO steps; if precision drops >10pp from Phase 0 baseline, adjust confidence threshold (periodic recalibration, motivated by TEMPO's finding that reward signal drift without recalibration leads to performance plateaus). Resource: ~50 A100-hours, 2-3 weeks.

**Phase 1 — Base Formalizer and Critic Integration.** Fine-tune Qwen3-8B using DDR's 500K-sample dataset and GRPO with R(y, x) = r_compile × (α·r_critic + β·r_beq). r_compile ∈ {0,1} (Kimina Lean Server, 128 parallel workers); r_critic ∈ {0,1} (CriticLeanGPT-Qwen3-14B-RL, gated by Phase 0 threshold); r_beq ∈ [0,1] (BEq consensus density). α=0.7, β=0.3. Fallback: when <4 of K=32 compile, R = r_compile × r_critic.

**Phase 2 — Dual-Loop Co-Adaptive Retrieval with Graded Error Signals (Core Innovation #1).** The retriever (DDR-style dense encoder) is explicitly updated during TTRL. This exploits Lean 4's unique structural property: compilation errors provide oracle-quality, token-level retrieval training signals that directly specify which Mathlib dependencies are needed—signals unavailable during pre-training, discarded by inference-time search, and unexploited by static retrieval pipelines.

  Loop 1 — Formalizer GRPO (every step): K=32 candidates, compile, multi-tier rewards, debiased GRPO.

  Loop 2 — Retriever contrastive update (every N_ret=50 GRPO steps): Graded error hierarchy:
    (a) Tier 1 (highest confidence): `lean.unknownIdentifier` names missing constant → hard negatives from retrieved set; constant from CRAMF/DDR index = positive. `unknown namespace` → coarser module-level positive.
    (b) Tier 2 (moderate): `type mismatch` → type signatures matched against Mathlib type index, 0.5× weight. `failed to synthesize instance` → typeclass instances as positives.
    (c) Tier 3: tactic/elaboration/syntax → negatives only.
    (d) Compilation success → all retrieved dependencies in compiled output = confirmed positives.
    (e) Weighted InfoNCE: L = -Σ_k w_k · log(exp(sim(q, d_k+)/τ) / Σ_j exp(sim(q, d_j)/τ)), w_k = 1.0 (Tier 1/confirmed), 0.5 (Tier 2), τ=0.07.
    (f) Decoupled optimization (per R3 and Reinforced-IR): retriever gradient does not flow through formalizer. FAISS rebuild after each update.

  Signal density: 50 steps × 32 candidates × ~15% compile rate ≈ 240 compile/fail pairs per cycle.

**Phase 3 — Binarize-Then-Enrich: Adapting DDRL to Multi-Tier Rewards (Core Innovation #2).** Autoformalization's reward components are fundamentally heterogeneous: compilation is a hard binary gate (non-negotiable), the critic is a noisy soft signal (calibrated but imperfect), BEq is a population statistic (drifts with policy). This heterogeneity distinguishes TTRA from all existing TTRL reward improvements (DDRL, T³RL, SCOPE, GDPO), which assume homogeneous reward signals. Neither DDRL alone (cannot handle multi-tier) nor GDPO alone (does not address spurious amplification) suffices:

  (a) Binarization layer: r_accept = I(r_compile=1 AND r_critic=1). Balanced sampling (exclude 30-70% ambiguity zone per DDRL). Fixed advantages: +1 (accepted), -1 (rejected). Consensus off-policy refinement: M=128, rejection-sample >80% acceptance, SFT 5 epochs.
  (b) GDPO-style enrichment: among accepted candidates, per-reward decoupled normalization for BEq. Additive bonus δ·norm(r_beq) to +1 advantage, δ=0.3.

**Phase 4 — Progressive Domain Curriculum.** (a) Near-distribution warm-start: compilation ≥40%, critic approval ≥60%, BEq@32 ≥3pp above baseline. Timeout: 500 steps. (b) Retrieval bootstrapping: Tier 1/2 errors feed retriever updates. Transition: recall@10 ≥30%, compilation ≥25%. Early transition: plateau <2pp over 200 steps. (c) Far-OOD: algebraic geometry, condensed mathematics, MathAtlas MA-Hard with adaptive fallback.

**Contribution Floor Analysis.** (1) Co-adaptive retrieval + CriticLean TTRL alone: first co-adaptive retrieval for autoformalization + first TTRL for formal math with calibrated critic. (2) Binarize-then-enrich alone: addresses DDRL's explicit future work on multi-tier rewards. (3) Curriculum: droppable. (4) Essential floor: CriticLean TTRL outperforms compilation-only (Phase 0 gate) AND ≥1 of co-adaptive retrieval / binarize-then-enrich shows statistically significant improvement.

**Evaluation.**

  *Benchmarks:* In-distribution: miniF2F-test (244), ProofNet (~371). Multi-domain: FormalMATH (5,560). OOD stress tests: Con-NF, CombiBench, MathAtlas MA-Hard (700 entities, best: 2.6%; contingency: IndiMathBench if gold coverage <50%).

  *Metrics:* BEq@K, BEq+@K (per DRIFT), pass@K (K=1,32), compilation@K on all benchmarks. GTED (arXiv:2507.07399, continuous [0,1] similarity with better precision-recall balance than BEq) on OOD benchmarks. Hall_m (DDR's hallucination rate) in retriever ablation. Human evaluation: 100-150 samples on Con-NF + 200 samples on MathAtlas MA-Hard (inter-annotator agreement reported).

  *Same-scale primary baselines (~7-8B):* (1) FormaRL (Qwen2.5-Coder-7B, COLM 2025); (2) Online RL for Autoformalization (Wang et al., faithfully reimplemented if code unavailable); (3) DRIFT with Qwen3-8B (ICLR 2026); (4) Aria (ICLR 2026, reimplemented on shared benchmarks or reported numbers annotated); (5) StepFun-Formalizer-7B (AAAI 2026, open-source); (6) ReForm-8B (Qwen3-8B, arXiv:2510.24592); (7) compilation-only TTRL and critic-only TTRL ablations.

  *Cross-paradigm reference:* FormalEvolve (arXiv:2603.19828, reported SH@100 on CombiBench/ProofNet).

  *Compute-matched baseline:* Best-of-N (matched FLOPs) + CriticLean filtering: allocate equivalent test-time compute to sampling more candidates from base formalizer, filter with CriticLean-14B, report BEq@1 and compilation@1. Directly tests whether TTRA's weight adaptation provides value beyond inference-time scaling.

  *Ablations:* (a) Standard GRPO vs. DDRL vs. binarize-then-enrich (component-wise); (b) frozen vs. co-adaptive retriever; (c) Tier 1-only vs. Tier 1+2 vs. all-tier error signals; (d) no curriculum vs. progressive; (e) CriticLean-14B reward vs. embedding-based similarity reward (isolating trained critic value).

  *Sensitivity:* N_ret ∈ {25, 50, 100}; δ ∈ {0.0, 0.1, 0.3, 0.5} (δ=0.0 = pure DDRL); ambiguity zone ∈ {[20%-80%], [30%-70%], [40%-60%]}; critic confidence threshold ∈ {0.6, 0.7, 0.8, 0.9}; K ∈ {16, 32, 64} (test-time compute scaling behavior).

  *Cross-scale references:* ATF-32B, ATLAS (NeurIPS 2025), Monotonic Refinement (multi-model ensemble). All tables annotate scale and compute.

  *Statistical rigor:* Key comparisons ≥3 seeds, mean ± std, bootstrap CI (p<0.05).

## Detailed Description

TTRA makes TTRL viable for autoformalization by exploiting a structural asymmetry: Lean 4's compiler provides oracle-quality, token-level feedback (identifier names, type signatures, typeclass requirements) that serves simultaneously as retriever training signal, multi-tier reward components, and domain adaptation indicators—signals unavailable in informal reasoning and unexploited by existing methods. The dual-loop architecture co-adapts the retriever during test-time RL via weighted InfoNCE over Lean 4's error hierarchy, addressing the limitation that static retrievers (Aria, DRIFT, DDR) cannot track formalizer evolution. CriticLean-14B integration includes distributional shift calibration and periodic drift monitoring (motivated by TEMPO's EM analysis of reward signal degradation). Binarize-then-enrich addresses the specific gap between DDRL (binary debiasing) and GDPO (multi-reward normalization) for formal verification's heterogeneous reward landscape—a qualitatively different problem from the homogeneous-reward improvements in T³RL and SCOPE. Compute-matched evaluation against best-of-N + critic filtering directly tests whether weight adaptation provides value beyond inference-time scaling. The framework positions test-time learning as a third scaling axis for formal mathematics alongside training-time and inference-time compute.

## Key References

- TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)
- Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)
- GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, NVIDIA, January 2026)
- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv:2507.06181, ByteDance/Nanjing)
- Online Reinforcement Learning for Autoformalization (Haiming Wang et al., NeurIPS 2025 MAR Workshop)
- R3: Optimizing Retrieval for RAG via Reinforced Contrastive Learning (NeurIPS 2025, arXiv:2510.24652)
- Reinforced-IR: A Self-Boosting Framework for Domain-Adaptive Cross-Domain Retrieval (ACL 2025)
- TTARAG: Predict the Retrieval! Test-Time Adaptation for Retrieval Augmented Generation (arXiv:2601.11443, January 2026)
- Construction-Verification: A Benchmark for Applied Mathematics in Lean 4 [AMBER] (Yang et al., arXiv:2602.01291, February 2026)
- Autoformalizer with Tool Feedback [ATF] (arXiv 2025)
- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)
- Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)
- Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)
- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)
- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach [RAutoformalizer] (ICLR 2025 Spotlight)
- Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv:2511.11990)
- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)
- Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)
- Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)
- Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)
- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv:2505.02735)
- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)
- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)
- Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026, arXiv:2510.04520)
- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026, arXiv:2510.15681)
- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv:2510.24592)
- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (arXiv:2512.00997, Microsoft Research)
- FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization (arXiv:2603.19828, March 2026)
- Binary Rewards and Reinforcement Learning: Fundamental Challenges (Dymetman, arXiv:2605.02375, May 2026)
- TEMPO: Scaling Test-time Training for Large Reasoning Models (arXiv:2604.19295, April 2026)
- T³RL: Tool Verification for Test-Time Reinforcement Learning (arXiv:2603.02203, March 2026)
- SCOPE: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning (arXiv:2512.15146, December 2025)
- GTED: Generalized Tree Edit Distance: A Faithful Evaluation Metric for Statement Autoformalization (arXiv:2507.07399)

## Resource Estimate

- **manual**: gpu_hours: 1400-1900 A100-80GB hours (Phase -1 micro-analysis + MathAtlas coverage: ~10h; Phase 0 pilot + calibration: ~50h; Phase 1 base GRPO: ~300h; DDR retriever + co-adaptive updates: ~100h; Phase 4 progressive TTRL + ablations: ~400h; CriticLean-14B inference all phases: ~200-300h; N_ret/δ/ambiguity/critic-threshold/K sensitivity: ~100h; baseline evaluation (Aria reimpl + StepFun + ReForm): ~100-120h; compute-matched best-of-N baseline: ~30h; CriticLean vs embedding ablation: ~25h; multi-seed (3 seeds × key ablations): ~200h; human eval annotation: ~60-80h; miniF2F/ProofNet + remaining eval: ~80h) + 15,000-20,000 CPU-hours Lean verification (Kimina Lean Server), timeline: 14-18 weeks (0.5 wk Phase -1; 2-3 wk Phase 0 + go/no-go; 3 wk Phase 1; 2 wk retriever infrastructure; 4 wk TTRL experiments; 3 wk ablations + sensitivity + multi-seed; 2 wk writing), estimated_gpu_cost: $2,800-$4,700 + $750-$1,000 CPU + ~$1,500-$2,500 human annotation. GPU architecture: policy (8B) + ref (8B) on 4×A100 tensor parallel, CriticLean-14B on dedicated 2×A100 with vLLM batch inference, retriever + FAISS on CPU/1×A100; async pipeline.
- **human_in_loop**: gpu_hours: 1100-1500 A100-80GB hours (~25% reduction), timeline: 11-14 weeks, claude_api_cost: $400-$700, estimated_gpu_cost: $2,200-$3,700 + $600-$800 CPU + ~$1,200-$2,000 annotation
- **auto_research**: gpu_hours: 2000-2700 A100-80GB hours (full sweep), timeline: 8-11 weeks, claude_api_cost: $800-$1,200, estimated_gpu_cost: $4,000-$6,700 + $1,000-$1,350 CPU + ~$1,500-$2,500 annotation, speed_bottleneck: Lean 4 compilation (~3.65s/statement warm cache, ~0.10s amortized at 64 workers). CriticLean-14B ~0.5s/candidate (→~0.1-0.2s with vLLM). Retriever co-adaptation ~15 min/cycle (re-encode 26K constants, rebuild FAISS).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9f215d28-bb0e-45c9-994f-785fbcbc7980",
  "type": "user",
  "uuid": "36112f94-cd3a-4916-ae3c-73cc9ccd58ae",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T06:05:40.129Z_

```json
{
  "parentUuid": "36112f94-cd3a-4916-ae3c-73cc9ccd58ae",
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
  "uuid": "75ff476f-817a-4ddd-a6ce-76a11114fb1c",
  "timestamp": "2026-05-28T06:05:40.129Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T06:05:40.129Z_

```json
{
  "parentUuid": "75ff476f-817a-4ddd-a6ce-76a11114fb1c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "64ceed8d-3c4a-4d3c-bf1a-04d040329015",
  "timestamp": "2026-05-28T06:05:40.129Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct a thorough evalua…",
  "leafUuid": "64ceed8d-3c4a-4d3c-bf1a-04d040329015",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Test-time RL for out-of-distribution autoformalization",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071"
}
```

---

### Assistant

_source line 8 · 2026-05-28T06:06:21.060Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them according to the Meta Judge format.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 中（偏强）
- Significance: 中
- Related Work: 强
- Probability: [23% - 33%] 中位 27%
- Main risks: Combination paper, core finding lacks surprise

**Reviewer 2:**
- Novelty: 中偏强
- Significance: 中偏强
- Related Work: 强
- Probability: [28% - 38%] 中位 33%


- Main risks: "Lego novelty" criticism, system complexity vs attributability

**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [28% - 38%] 中位 32%
- Main risks: Combination vs innovation, surprise insufficient

Now I'm calculating the aggregate metrics across all three reviewers. The midpoints are 27%, 33%, and 32%, which average to about 30.67% with a median of 32%. I need to compute the standard deviation to understand the variance in their assessments. Now I'm checking whether to use population or sample standard deviation—with the population std at 2.63%, it falls below the 3% threshold for "高一致", so this qualifies as high consistency.

Looking at where the three reviewers align, I can see several strong consensus points: all three agree on novelty being medium to medium-strong, with the core limitation being that this is fundamentally a combination paper; they all recognize the related work as comprehensive and strong; they converge on significance as medium to medium-strong given the niche problem domain; and critically, all three flag the combination/Lego novelty risk as the primary concern, noting that the finding—that compilers provide richer feedback—lacks surprise once stated. Beyond this, reviewers one and two both raise concerns about system complexity being too high.

The calibration risk around CriticLean's out-of-distribution behavior appears across all three reviews, with the skewed distribution being a shared worry. All three also acknowledge that while a compute-matched baseline was included to address the trivial alternative threat, some vulnerability remains in moderate out-of-distribution scenarios.

The outliers are minor: reviewer one rates significance slightly lower than the others, their probability estimate sits noticeably below the other two though still within a tight range, and reviewer three uniquely mentions a potential citation gap regarding Lean 4 cycle consistency fine-tuning.

For the final probability, the high consistency across reviewers—with a standard deviation around 2.6%—suggests I should anchor near the median and keep the interval narrow. The overlap across all three reviewers falls in the 28-33% range, centering around 30.5%, which aligns with the consensus that this is a solid combination paper with genuine but incremental insights. I'm settling on a final range of 25-35% with a median of 30%, which balances R1's more critical stance on significance against R2 and R3's slightly higher assessments while respecting the principle of being conservative. Now I need to compile the implementation assessment from the proposal and review materials.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64ceed8d-3c4a-4d3c-bf1a-04d040329015",
  "isSidechain": false,
  "requestId": "req_011CbUTr4ZJKP4Q7ti5LAbap",
  "type": "assistant",
  "uuid": "0fb9d6a3-d9df-412f-b346-f1e5cfe951dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmS2w1u4ByiDc7nejY5Akb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24809,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3959,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 24809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24809
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

_source line 9 · 2026-05-28T06:07:18.630Z_

【阶段】: Meta Judge
【三次中位】: [27%, 33%, 32%]  std=2.6%
【共识维度】:
- **Novelty = 中（偏强边界）**（3/3）：核心 insight（Lean 4 结构化编译错误 → co-adaptive retrieval 的 oracle-quality training signal）是真实的 novel gap，但本质是 combination paper——DDRL + GDPO + CriticLean + R3/Reinforced-IR 四个已验证组件的领域级整合，每个单独组件贡献为 adaptation 而非 invention。"Binarize-then-enrich" 填补 DDRL 明确声明的 future work，但技术深度有限。
- **核心发现 surprise 不足**（3/3）：三位审稿人一致指出"形式语言编译器提供比二值奖励更丰富的反馈"一旦被陈述就显得 intuitive / near-obvious。审稿人大概率评价为 "well-engineered, makes sense" 而非 "I would not have expected this"。这是压制概率上界的最强共识信号。
- **Related Work = 强**（3/3）：覆盖截至 2026 年 5 月几乎所有相关工作，差异化定位清晰，描述经验证准确。不构成扣分因素。
- **Significance = 中至中偏强**（3/3）：问题本身重要（MathAtlas MA-Hard 2.6%），"第三 scaling axis" framing 有概念吸引力；但 autoformalization 仍为 niche 子领域，方法可推广性受限于 formal language 特有性质。
- **CriticLean OOD 校准风险**（3/3）：balanced 250/250 训练 vs. <10% compilable 的 TTRL 分布，精度可能大幅下降。Phase 0 go/no-go gate 是合理的去风险策略，但假设仍未验证。
- **系统复杂度过高**（2/3，R1+R2 明确，R3 隐含）：dual-loop + multi-tier reward + curriculum + critic calibration + go/no-go gates，可归因性困难——如果结果 moderate，审稿人难以判断哪个组件真正起作用。
- **Trivial alternative 威胁中等**（3/3）：Best-of-N + CriticLean filtering + static retrieval 在 moderate OOD 下可能足够；增量价值主要限于 extreme OOD（MA-Hard），proposal 已纳入 compute-matched baseline。

【异常维度】:
- R1 将 Significance 打为"中"（R2/R3 为"中偏强"）——R1 更强调 niche 性质和方法可推广性限制。差异不大，但 R1 的论证（"autoformalization 对 broader AI community 直接影响有限"、"co-adaptive retrieval via compiler error 不易迁移"）有合理性，应适度降权 Significance。
- R3 单独提及 "Lean 4 Cycle Consistency Fine-tuning (arXiv:2603.24372)" 作为轻微遗漏——仅 1 人提到，且 R3 自己评为"不影响核心定位"，降权处理，不影响 Related Work 判决。
- R2 特别提到"reviewer pool 中深度理解 Lean 4 + TTRL + retrieval 交叉点的人有限"作为 significance 受限因素——只有 R2 提到此点，但这是一个合理的实操风险（AAAI 综合会议的 reviewer 匹配问题），纳入但不作为主要扣分项。

【最终概率】: [25% - 35%] 中位 30%
【一致性】: 高（std=2.6% < 3%）
【综合理由】:

三位审稿人在所有核心维度上高度收敛，分歧仅在 Significance 的微调（"中" vs "中偏强"）和概率区间的位移上。处理逻辑如下：

1. **共识驱动定位**：三位审稿人的核心判决完全一致——这是一篇定位在真实 gap 上、related work 极为充分、但 novelty 受 combination nature 限制且核心发现缺乏 surprise 的 proposal。这个共识锚定了 25-35% 的区间。

2. **中位校准**：R1（27%）略偏保守，R2（33%）和 R3（32%）接近。在高一致性下取中位附近，但遵循"宁缺毋滥"原则，最终中位 30% 略低于三者算术均值（30.7%），反映以下考量：
   - 三位审稿人**全部**指出的 "surprise 不足" 是一个硬约束——AAAI 审稿人对 combination paper 的接受度波动大，概率中位不宜高估
   - R1 对 Significance 的更保守评估（"中"而非"中偏强"）有合理性：autoformalization 确实是相对 niche 的领域，formal language 特有的 co-adaptive retrieval 机制难以推广

3. **区间缩窄**：高一致性允许缩窄区间。下界 25%（反映 combination paper 可能被审稿人严厉评判为"工程整合"），上界 35%（反映 gap 真实性 + related work 极充分 + 若审稿人恰好重视 formal math 可能给更高分）。

4. **上界约束**：即使实验完美执行，idea 的 combination nature + surprise 不足将概率天花板压在 ~38%。三位审稿人中最宽松的 R2 也只给了 38% 上界，且这需要所有组件都 work 且改进幅度足够大。

【建议】: 边缘
【实施评估】:
  - 计算资源: 1400-1900 A100-80GB GPU 小时（manual 模式），需 4×A100 做 policy+ref tensor parallel，2×A100 跑 CriticLean-14B (vLLM batch inference)，1×A100+CPU 跑 retriever+FAISS。估算 GPU 成本 $2,800-$4,700 + CPU $750-$1,000。资源需求在 autoformalization 研究中属于中等偏高但可接受。
  - 数据需求: 依赖多个公开数据集/工具——DDR 500K 依赖数据集、CRAMF 26K+ Mathlib 概念索引、MathAtlas 52K 问题、miniF2F、ProofNet、FormalMATH、Con-NF、CombiBench。均为公开或可获取资源。CriticLeanGPT 模型已开源于 HuggingFace。
  - 人工介入: 需要 100-150 + 200 样本的人工评估（Con-NF + MathAtlas MA-Hard），需要具备 Lean 4 / 形式化数学背景的标注者，估算 $1,500-$2,500 标注成本。Phase -1 的错误分类也可能需要人工抽查验证。
  - 训练需求: 需要训练/微调 Qwen3-8B formalizer（Phase 1 SFT + GRPO），训练/更新 DDR-style dense retriever（Phase 2 co-adaptive updates）。不需要从头训练 CriticLean（使用开源 checkpoint）。模型规模 8B + 14B，训练时长嵌入在总 GPU 小时中。
  - 新 Benchmark: 不需要构建全新 benchmark。使用现有 benchmarks（MathAtlas、miniF2F、ProofNet 等）。Phase -1 的 error taxonomy micro-analysis 是定制分析而非新 benchmark。
  - 预估周期: 14-18 周（manual）/ 11-14 周（human-in-loop）/ 8-11 周（auto-research）。关键瓶颈为 Lean 4 编译延迟（~3.65s/statement warm cache）和 Phase 0 go/no-go 决策点。AAAI 2026 投稿时间线需确认是否充裕。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fb9d6a3-d9df-412f-b346-f1e5cfe951dc",
  "isSidechain": false,
  "requestId": "req_011CbUTr4ZJKP4Q7ti5LAbap",
  "type": "assistant",
  "uuid": "6f922d9d-c5f2-4363-89fc-92320fef7332",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmS2w1u4ByiDc7nejY5Akb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24809,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3959,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 24809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24809
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to conduct a thorough evalua…",
  "leafUuid": "6f922d9d-c5f2-4363-89fc-92320fef7332",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Test-time RL for out-of-distribution autoformalization",
  "sessionId": "919dcc97-f2f3-4370-8b57-04d58b699071"
}
```

---
