# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/332a1257-ba0b-45b9-8bcc-d7440fbd7e12.jsonl`
- **Structured JSON:** [`db4f95740972b9cf8914.json`](../../sessions/db/db4f95740972b9cf8914.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:58:29.152Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:58:29.152Z",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have comprehensive field understanding. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- LU-LAFNs (COLING 2025, arXiv:2406.16416): 最直接的 prior work。通过跨语言激活频率交集识别 language-agnostic factual neurons (LAFNs)，在 Bi-ZsRE 上 bloomz-7b1-mt 达到 77.87 avg。关键发现：67.9% 的 neurons 被标记为 LAFNs（极粗粒度），且**所有方法**在 portability EM 上均 < 10。作者自己承认这是普遍难题而非方法特定失败。\n- FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483): 首个基于 SAE feature 的模型编辑方法。在 PrivacyParaRel 隐私知识擦除任务上证明 features 优于 neurons（reliability ~0.80 vs ~0.65, generalization ~0.70 vs ~0.25）。但任务是隐私擦除而非事实编辑，模型是 Gemma-2，非跨语言场景。\n- CLM-Bench (arXiv:2601.17397, Jan 2026): 提供了中英编辑向量近乎正交的几何证据，解释了 ROME/MEMIT 跨语言失败（~20% reliability）。\n- Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456): 独立证据表明 neuron-level language-specific interventions 对跨语言迁移无效（XNLI/XQuAD），支持\"neuron 粒度不够\"的论点。\n- LangSAE Editing (arXiv:2601.04768, Jan 2026): 用 SAE feature suppression 移除 language identity，在多语言检索上 +21.9% nDCG@20。但目标是检索而非知识编辑。\n- Chou et al. (arXiv:2507.13410, Jul 2025): 通过修改单个 SAE feature 在 Gemma-2B/9B 上实现高达 90% 的语言转向成功率，证明 SAE-based language manipulation 的可行性。\n- Peng et al. (arXiv:2506.23845): 论证 SAE 适合 concept discovery 而非 acting on known concepts，SAE steering 不如 prompting/fine-tuning。\n- Arad et al. (EMNLP 2025, arXiv:2505.20063): 反驳 Peng et al.，通过 output-score filtering 实现 SAE steering 2-3× 提升，匹配 supervised methods。\n- Leask et al. (ICLR 2025, arXiv:2502.04878): 证明 SAE features 非 atomic/canonical units，大 SAE 的 latents 可分解为小 SAE latents 的组合。建议按任务需要选择 dictionary size。\n- SCAN (arXiv:2603.15226, Mar 2026): 用 sparse transcoders 做 lifelong editing（Qwen3/Llama3.1），但目标是 sequential stability 而非跨语言迁移。\n- X-KDE (ACL 2025 Findings, arXiv:2502.14645): 用 instruction tuning + preference optimization 做跨语言知识同步，+8.19% avg improvement。\n- LangEdit (ACL 2025 Findings, arXiv:2506.10800): 用 null-space projection 做多语言 sequential editing。\n- AlphaEdit (ICLR 2025): 用 null-space constraints 做知识编辑。\n- Merging Methods for MKE (arXiv:2605.13919, May 2026): 用 vector merging + shared covariance 做 12 语言编辑，但没有 representation-level decomposition。\n- SAE-LAPE/LangFIR (arXiv:2604.03532, ACL 2025 arXiv:2505.05111): 用 activation probability contrasts 发现 sparse language-specific features。\n\n- **调研总结**: 跨语言知识编辑是一个活跃的研究方向，2025-2026 年密集出现了多种方法（LU-LAFNs、X-KDE、LangEdit、AlphaEdit、Merging Methods）。与此并行，SAE-based 方法在知识擦除 (FeatureEdit)、语言转向 (Chou et al.)、语言 identity 移除 (LangSAE) 等任务上已证明有效。但**确实没有工作将 SAE feature decomposition 直接应用于跨语言知识编辑**——这个 gap 是真实存在的。Proposal 处于两条成熟研究线（跨语言编辑 + SAE intervention）的交汇点，是一个\"natural next step\"型组合创新。\n\n【Trivial Alternative 检验】:\n存在至少两个更简单的 alternative 需要考虑：\n\n1. **线性子空间投影（非 SAE）**: LangEdit 已经使用 null-space projection 处理多语言编辑，AlphaEdit 也用了 null-space constraints。如果语言特定分量和事实分量在 residual stream 中是线性可分的（这本身是一个合理的假设，CLM-Bench 的正交性发现暗示了这一点），那么一个简单的 PCA-based 或 linear probe-based 语言分量移除（不需要 SAE）可能就够了。Proposal 没有解释为什么 SAE 提供的非线性稀疏分解比线性投影本质上更好。\n\n2. **多语言并行编辑**: 直接在每种目标语言中独立执行编辑（即对每种语言分别生成 edit vector 并应用），虽然 compute 成本更高但避免了跨语言迁移问题。X-KDE 的 instruction tuning 方法本质上也是绕过了 representation-level 分解。\n\n**增量价值所在**: Proposal 的增量价值在于：(a) 如果 polysemantic entanglement 假说正确，线性方法确实无法处理非线性的 factual-language 纠缠；(b) SAE 的 ~64K monosemantic features 提供了 neurons (~14K) 无法达到的粒度。但这两个前提都未经验证——(a) 是核心假设本身，(b) 在 Leask et al. 的 non-atomicity 发现下有所减弱。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中，有以下未验证的关键假设：\n\n1. **\"Portability 瓶颈是由 polysemantic entanglement 造成的\"** —— 这是整个工作的核心假设，但完全未经验证。LU-LAFNs 作者自己将低 portability 归因于\"the difficulty of measuring reasoning without a reasoning process\"，即 portability metric 本身可能测量的是推理能力而非事实迁移。如果瓶颈不是 representation-level 的（而是 decoding/reasoning-level 的），那么无论多精细的 representation 分解都无法解决。\n\n2. **\"SAE features 能对 factual 和 language-specific 分量做比 neurons 更干净的分离\"** —— Leask et al. (ICLR 2025) 已证明 SAE features 不是 atomic canonical units。虽然 proposal 用 continuous weighting 来 accommodate，但这本质上是在承认分离不干净的前提下做 soft mitigation，削弱了\"finer granularity = cleaner separation\"的核心论点。\n\n3. **\"FCE metric 能可靠识别 factual-language 纠缠程度\"** —— FCE 是 ablation-based 的（去掉 feature → 测 factual recall 变化），但 ablation 只测量 necessary condition（feature 是否 necessary for recall），不测量 sufficiency。一个 feature 可能对 factual recall 不是 necessary（因为有冗余编码）但仍然 encode factual information。这可能导致高估\"safe to remove\"的 language-specific features 的数量。\n\n4. **\"FeatureEdit 在知识擦除上的优势能迁移到跨语言事实编辑\"** —— Proposal 自己承认了这个 gap，但整个工作的 motivation 部分仍然大量依赖 FeatureEdit 的结果作为\"features > neurons\"的证据。擦除和编辑是不同操作（一个是移除信息，一个是替换信息 + 保持结构），迁移性未知。\n\n其中第 1 点是最关键的——如果 portability bottleneck 的原因不是 representation entanglement 而是更深层的 reasoning limitation，整个技术路线就失去了根基。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Gap 确实存在：搜索确认无工作将 SAE feature decomposition 应用于跨语言知识编辑。但这本质上是一个 \"combine A (SAE features, well-studied) with B (cross-lingual editing, well-studied)\" 型创新。对熟悉 FeatureEdit (ACL 2025) + LU-LAFNs (COLING 2025) + LangSAE (2026) 的研究者来说，\"用 SAE features 代替 neurons 做跨语言编辑\"是相当自然的 next step——不是\"为什么没人想到\"，而是\"时间问题\"。\n   \n   具体技术贡献上：activation-probability contrasts 来自 SAE-LAPE；output-score filtering 来自 Arad et al.；soft projection 而非 binary zeroing 的 insight 来自 Farrell et al.。Proposal 自己发明的核心技术只有 FCE metric 和 adaptive λ-projection 机制，这些是 solid 但 incremental 的方法贡献。\n   \n   如果核心发现是 positive（SAE features 确实提升了 portability），审稿人的反应更可能是 \"makes sense, this is what I'd expect given FeatureEdit + LangSAE results\" 而非 \"surprising\"。如果是 negative（SAE features 也无法提升 portability），这会更 surprising 也更有诊断价值——但 proposal 将此定位为 fallback 而非主打结论。\n\n2. **Significance: 中** — \n   正面：跨语言知识编辑的 portability bottleneck 是一个被社区广泛认可的真实问题（survey arXiv:2505.14393 将其列为 key challenge）。如果能突破 EM < 10 的 universal ceiling，影响力确实显著。\n   \n   限制因素：(a) 即使 SAE decomposition 有帮助，从 EM ~5 提升到 EM ~15-20 仍然是相当 modest 的绝对改进，可能不足以让人感到\"paradigm shift\"；(b) 依赖 pre-trained SAEs（Qwen-Scope, Llama Scope），方法的通用性受限于 SAE 的可用性；(c) 目前的 SOTA 模型越来越强大，knowledge editing 这个范式本身面临来自 RAG、continual pretraining 等替代方案的竞争——如果 editing 范式本身在实践中被弱化，这条线的长期价值有限。\n   \n   此外，结果的可推广性取决于 polysemantic entanglement 假说的正确性，如果假说错误，方法就缺乏 principled 的理论基础。\n\n3. **Related Work: 强** — \n   这是 proposal 最强的维度。四层分类（direct multilingual editing → neuron-level → SAE-based → SAE skepticism/counter-evidence）结构清晰。对每篇关键工作的描述经我搜索验证均准确——包括 FeatureEdit 的任务域限制（privacy erasure not factual editing）、Peng et al. vs Arad et al. 的论辩、Leask et al. 的 non-canonicality 挑战及其 pragmatic recommendation、Farrell et al. 的 binary zeroing 失败。\n   \n   特别值得肯定的是：(a) 对 adversarial work 的诚实对待和 principled engagement（多数 proposal 会回避 Peng et al. 和 Leask et al.）；(b) 对 FeatureEdit 结果的审慎引用（明确标注 domain mismatch）；(c) 对 Mondal et al. 的引用作为独立支持证据。References 经搜索验证均真实存在且描述准确。\n   \n   唯一的小缺口是未讨论 null-space projection methods (AlphaEdit, LangEdit) 作为更简单的 language component removal baseline——这正是 Trivial Alternative 检验中暴露的问题。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \nNovelty（中）是主要的上界限制因素——这是一个\"自然的下一步\"组合创新，核心 insight（用 SAE features 代替 neurons）对领域内研究者来说不 surprising。Related Work（强）抬高了下限——proposal 对领域的理解和定位是出色的，降低了\"审稿人发现致命遗漏\"的风险。Significance（中）居中——问题真实但改进空间的绝对值可能有限。\n\n核心假设（polysemantic entanglement 是 portability 瓶颈的原因）未经验证且存在 plausible alternative explanation（portability 测的是 reasoning 而非 representation），这构成了 idea 层面的实质风险——如果这个假设错误，即使实验执行完美，审稿人也会认为整个 framing 有问题。Trivial alternative（线性子空间投影）的威胁也降低了估值——如果一个简单的 PCA-based 语言分量移除达到类似效果，SAE 的复杂度就难以 justify。\n\nDual-outcome 设计（negative result 也有诊断价值）是合理的 hedge，但在竞争激烈的 top venue 中，以 negative result 为主的 paper 中稿概率会显著低于 positive result paper。\n\n**注意**: Proposal 目标投稿 CoRL 2026（Conference on Robot Learning）。这是一个纯 NLP/mechanistic interpretability 工作，与 CoRL 的 robotics scope 完全不匹配。如果确实投稿 CoRL，中稿概率实际上接近 0%。上述 22-33% 的估计是假设投稿至合适的 NLP 会议（如 ACL/EMNLP/NAACL 2026）。\n\n【主要风险】: \n1. **核心假设可能为假**: Portability bottleneck 的真正原因可能不是 polysemantic entanglement，而是 portability metric 测量的是 reasoning ability（LU-LAFNs 作者自己的解释）。如果如此，任何 representation-level decomposition（无论多精细）都无法改善 portability，整个技术路线的 framing 将被审稿人质疑。\n2. **Trivial alternative 未被排除**: Proposal 没有论证为什么 SAE-based decomposition 比更简单的线性子空间投影（类似 AlphaEdit/LangEdit 的 null-space approach 但针对 language component）本质上更优。审稿人可能要求一个\"linear projection baseline\"并发现 SAE 的增量收益不 justify 其复杂度。\n```\n\nSources:\n- [LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons](https://aclanthology.org/2025.coling-main.385/)\n- [The Knowledge Microscope: Features as Better Analytical Lenses than Neurons](https://arxiv.org/abs/2502.12483)\n- [CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment](https://arxiv.org/pdf/2601.17397)\n- [Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer](https://aclanthology.org/2025.insights-1.6/)\n- [LangSAE Editing: Improving Multilingual Information Retrieval](https://arxiv.org/abs/2601.04768)\n- [Chou et al.: Causal Language Control via Sparse Feature Steering](https://arxiv.org/abs/2507.13410)\n- [Peng et al.: Use SAEs to Discover Unknown Concepts](https://arxiv.org/html/2506.23845v1)\n- [Arad et al.: SAEs Are Good for Steering — If You Select the Right Features](https://arxiv.org/abs/2505.20063)\n- [Leask et al.: Sparse Autoencoders Do Not Find Canonical Units](https://arxiv.org/abs/2502.04878)\n- [SCAN: Sparse Circuit Anchor for Lifelong Editing](https://arxiv.org/pdf/2603.15226)\n- [X-KDE: Edit Once, Update Everywhere](https://arxiv.org/pdf/2502.14645)\n- [Editing Across Languages: A Survey](https://arxiv.org/html/2505.14393)\n- [Emergent Mind: SAE Steering Topic](https://www.emergentmind.com/topics/sparse-autoencoder-steering)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- LU-LAFNs (COLING 2025, arXiv:2406.16416): 最直接的竞争工作。通过激活频率交集识别跨语言共享的\"语言无关事实神经元\"(LAFNs)，在Bi-ZsRE上达到77.87 avg。但67.9%的神经元被识别为LAFNs（极粗粒度），且所有方法在portability EM上均<10。论文真实存在，proposal描述准确。\n- FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483): SAE特征用于知识擦除（非事实编辑），在PrivacyParaRel上特征vs神经元有显著优势（~0.80 vs ~0.65 reliability）。论文真实存在，proposal对其适用范围的限定（隐私擦除而非跨语言编辑）是诚实的。\n- LangSAE Editing (arXiv:2601.04768, Jan 2026): 用SAE特征抑制语言身份信号改善多语言信息检索，+21.9% nDCG@20。论文真实，但其目标是检索而非知识编辑。\n- Chou et al. (arXiv:2507.13410, Jul 2025): 修改单个SAE特征实现高达90%语言转向成功率（Gemma-2B/9B）。论文真实，为SAE语言操控的可行性提供了直接证据。\n- Arad et al. (EMNLP 2025, arXiv:2505.20063): 证明SAE steering失败源于特征选择不当而非SAE范式本身，output-score filtering带来2-3×提升。论文真实存在于ACL Anthology，proposal的引用和解读准确。\n- Leask et al. (ICLR 2025, arXiv:2502.04878): 证明SAE特征非原子/非规范化单位。论文真实，proposal对其的应对策略（连续加权基而非二值开关）是合理的。\n- Mondal et al. (NAACL 2025 InsightsNLP Workshop, arXiv:2503.17456): 证明神经元级语言特定干预不足以实现跨语言迁移。注意：这是NAACL的Insights from Negative Results Workshop论文，非主会论文，影响力有限。\n- SCAN (arXiv:2603.15226, Mar 2026): 用sparse transcoders做lifelong editing，在Qwen3/Llama3.1上实验，但目标是sequential stability而非跨语言传播。\n- Merging Methods for MKE (arXiv:2605.13919, May 2026): 极新工作，探索向量合并方法用于12语言编辑，发现vector summation + shared covariance最稳定，但无表示级分解。\n- Editing Across Languages Survey (arXiv:2505.14393): 综述确认language anisotropy和edit scalability为关键挑战。\n- 调研总结: 跨语言知识编辑是一个被综述和多篇近期工作认可的开放问题，portability是公认瓶颈。SAE特征已分别被用于知识擦除（FeatureEdit）、语言身份操控（LangSAE、Chou et al.）和lifelong editing（SCAN），但**确实没有工作将SAE特征分解与跨语言知识编辑结合**——proposal的gap claim成立。然而，这一组合是两条成熟线路的\"显然下一步\"衔接。\n\n【Trivial Alternative 检验】:\n存在明显的更简单替代方案威胁：\n(1) **直接应用LangSAE方法到编辑向量**：LangSAE已经能通过SAE特征抑制语言身份信号。将其直接用于编辑向量的语言成分去除（不需要FCE指标、不需要自适应λ），是一个成本极低的baseline。Proposal的增量价值声称在于\"自适应软投影考虑了事实-语言纠缠\"——但这一增量是否真正必要，取决于纯语言特征和事实特征之间的纠缠程度，而这恰恰是proposal试图验证的假设，尚无先验证据。\n(2) **简单的Chou et al.式单特征操控**：既然单个SAE特征就能实现90%语言转向，直接在编辑后做语言特征转向（而非在编辑向量上做投影）可能是更简单的路径。\n增量价值：Proposal的核心增量在于FCE指标引导的自适应程度控制，以及对\"为什么neuron级别不够\"的因果假设检验。但如果简单方案（如直接LangSAE-style suppression + ROME/MEMIT）已经能显著改善portability，则整个elaborate pipeline的价值大幅缩水。\n\n【前提假设检验】:\n核心逻辑链中有两个关键未验证假设：\n(1) **\"Portability bottleneck源于polysemantic entanglement\"假设**：这是整篇论文的因果前提，但LU-LAFNs作者自己提出了一个竞争性解释——portability指标本身可能在测量推理能力而非可编辑的事实关联。如果portability EM低是因为这些问题需要multi-hop reasoning（编辑无法触及的能力），那么无论用多细的特征分解都不会改善结果。Proposal虽然在risk mitigation中提到了这一点并设计了A2 ablation，但这不改变核心claim的前提是未经验证的。\n(2) **\"SAE特征足够monosemantic来实现clean separation\"假设**：Leask et al.已经证明SAE特征不是原子化的规范单位，meta-SAE可以进一步分解大特征。Proposal通过连续加权来应对，但这实质上承认了特征并非真正monosemantic——那么\"比neuron更细粒度\"的优势到底能带来多少实际改善？从67.9% LAFNs到64K features的粒度跃升，在portability这个具体指标上能否转化为可测量的改善，是完全开放的。\n\n【3 维度打分】:\n\n1. Novelty: 中 — \n组合novelty成立：经调研确认，SAE特征分解+跨语言知识编辑的交叉点确实无人占据。但这是一个\"bridge combination\"而非新范式——SAE用于语言操控（LangSAE, Chou et al.）、SAE用于知识编辑（FeatureEdit, SCAN, SSPU）、跨语言知识编辑（LU-LAFNs, X-KDE, LangEdit）三条线各自成熟，将它们组合是一个可预见的下一步。FCE指标和自适应λ投影是合理的工程贡献，但不构成方法论突破。核心假设\"更细粒度→更好分离→更好portability\"是直觉性的，审稿人的反应更可能是\"I would have guessed this\"而非\"surprising\"。类比：如果FeatureEdit已经证明features > neurons for knowledge erasure，LangSAE已经证明SAE可以去除语言信号，那将二者组合用于跨语言编辑几乎是\"显然应该尝试的事情\"。\n\n2. Significance: 中 —\n正面：跨语言知识编辑的portability是被综述（arXiv:2505.14393）和多篇论文（LU-LAFNs, CLM-Bench）共同确认的开放问题，所有方法EM<10的普遍失败确实需要新思路。假设检验设计（A3 falsification test）有独立的科学价值。\n负面：(a) 跨语言知识编辑本身是NLP中一个相对小众的子领域；(b) 知识编辑整体仍处于研究阶段，实际落地遥远；(c) 即使positive result，提升幅度可能有限——从EM<10到EM=15-25仍然不具备实用价值；(d) 该工作绑定特定模型的pre-trained SAE（Qwen-Scope, Llama Scope），可推广性受限于SAE的可用性。\n\n3. Related Work: 强 —\n这是proposal最突出的优势。覆盖范围极为全面，四层分类清晰（直接baseline → 神经元级 → SAE编辑 → SAE干预质疑）。对adversarial evidence的引用和应对诚实且具体（Peng et al. → Arad et al.反驳；Leask et al. → 连续基处理；Farrell et al. → 软投影而非零化）。对FeatureEdit适用范围的限定（知识擦除而非事实编辑）显示了学术诚信。唯一小瑕疵：Mondal et al.被标为\"NAACL 2025 InsightsNLP\"，实际是NAACL的Negative Results Workshop论文，非主会，作为\"independent evidence\"的权重应有所调降。\n\n【概率估计】: [22% - 32%] 中位 27%\n（注：此概率假设投稿至ACL/EMNLP等NLP主会。若真的投稿CoRL 2026——一个机器人学习会议——则概率接近0%，因为完全不在scope内。）\n\n【估计理由】:\n从3维度到概率的推理：Related Work强是执行层面的优势，不拉高idea上限；Significance中等限制了ceiling（审稿人可能认为子领域太窄、practical impact不足）；**Novelty中等是主要上限限制因素**——\"bridge combination\"类工作在顶会的认可度取决于组合后是否产生非trivial的insight，而本proposal的核心假设\"finer granularity → better separation\"直觉性过强。如果positive result只是modest improvement（比如portability EM从<10升到15-25），审稿人很可能评价为\"reasonable engineering contribution but limited novelty\"。Proposal的falsifiability设计和dual-outcome framing可以保底（negative result也有价值），但这本身说明了idea的风险——需要用\"即使失败也有价值\"来对冲，侧面反映了作者对positive outcome的信心有限。上界32%的情景是：positive result显著（portability EM大幅跃升）+ 分析揭示出关于多语言表示的deep insight；下界22%的情景是：提升modest + 审稿人质疑trivial alternative。\n\n【主要风险】:\n1. **Trivial alternative威胁**：审稿人可能要求与\"直接LangSAE-style suppression on edit vectors\"做对比——如果这个极简baseline已经能获得大部分改善，则整个FCE + adaptive λ pipeline的增量价值被严重削弱，论文会被评为over-engineered。\n2. **核心因果前提不成立的风险**：如果portability bottleneck的真正原因是metric本身测量推理能力（如LU-LAFNs作者所暗示），或者是更深层的表示对齐问题（而非polysemanticity），那么无论SAE特征分解做得多好，portability都不会显著改善——此时论文沦为一篇\"negative result with analysis\"，发表难度大幅增加。\n```\n\nSources:\n- [LU-LAFNs - ACL Anthology (COLING 2025)](https://aclanthology.org/2025.coling-main.385/)\n- [FeatureEdit / The Knowledge Microscope (arXiv:2502.12483)](https://arxiv.org/abs/2502.12483)\n- [LangSAE Editing (arXiv:2601.04768)](https://arxiv.org/abs/2601.04768)\n- [Chou et al. - Causal Language Control (arXiv:2507.13410)](https://arxiv.org/abs/2507.13410)\n- [Arad et al. - SAEs Are Good for Steering (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.519/)\n- [Leask et al. - SAE Canonical Units (ICLR 2025)](https://arxiv.org/abs/2502.04878)\n- [Mondal et al. - Language-Specific Neurons (NAACL InsightsNLP 2025)](https://aclanthology.org/2025.insights-1.6/)\n- [SCAN (arXiv:2603.15226)](https://arxiv.org/pdf/2603.15226)\n- [Merging Methods for MKE (arXiv:2605.13919)](https://arxiv.org/abs/2605.13919)\n- [CLM-Bench (arXiv:2601.17397)](https://arxiv.org/pdf/2601.17397)\n- [Editing Across Languages Survey (arXiv:2505.14393)](https://alt.qcri.org/~ndurrani/pubs/EMNLP25a.pdf)\n- [X-KDE (arXiv:2502.14645)](https://arxiv.org/pdf/2502.14645)\n- [SSPU (arXiv:2505.24428)](https://arxiv.org/pdf/2505.24428)\n- [SpARE (arXiv:2410.15999)](https://arxiv.org/pdf/2410.15999)\n- [Farrell et al. (arXiv:2410.19278)](https://arxiv.org/pdf/2410.19278)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient field research to make an informed assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- LU-LAFNs (COLING 2025, arXiv:2406.16416): 最直接的 prior work。通过 activation frequency intersection 识别 language-agnostic factual neurons (LAFNs)，在 Bi-ZsRE 上达到 77.87 avg，但所有方法（包括 LU-LAFNs 本身）portability EM < 10。该论文确实存在，proposal 对其描述准确。\n- FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483): 确认存在。首个 SAE-feature-based editing 方法，在 PrivacyParaRel 上 features 优于 neurons（~0.80 vs ~0.65 reliability）。但确如 proposal 所述，仅限单语英文的 privacy-knowledge erasure，非 factual editing 或跨语言场景。\n- Arad et al. (EMNLP 2025, arXiv:2505.20063): 确认存在。区分 input features 与 output features，通过 output-score filtering 使 SAE steering 提升 2-3×，匹配 supervised methods。确实可视为对 Peng et al. 的有效回应。\n- Peng et al. (arXiv:2506.23845, Jun 2025): 确认存在。论证 SAE 更适合 discovery 而非 intervention。该 proposal 对其描述准确。\n- Leask et al. (ICLR 2025, arXiv:2502.04878): 确认存在。通过 meta-SAE 证明 SAE features 不是 atomic canonical units。proposal 对其描述准确。\n- Mondal et al. (NAACL 2025, arXiv:2503.17456): 确认存在。在 XNLI/XQuAD 上证明 neuron-level language-specific intervention 不足以实现 cross-lingual transfer。为 proposal 的 motivation 提供了独立支撑。\n- LangSAE (arXiv:2601.04768, Jan 2026): 确认存在。通过 SAE feature suppression 去除 language identity，提升多语言检索 nDCG。\n- Chou et al. (arXiv:2507.13410): 确认存在。单 SAE feature 修改即可达 90% 语言 steering 成功率（Gemma-2B/9B）。\n- SCAN (arXiv:2603.15226, Mar 2026): 确认存在。用 Sparse Transcoders 做 lifelong editing，但解决的是 sequential stability 问题，非跨语言迁移。\n- Merging Methods for MKE (arXiv:2605.13919, May 2026): 确认存在。最新 concurrent work，探索 vector merging + shared covariance 做 12 语言编辑，但不涉及 representation-level decomposition。\n- SAE-LAPE (ACL 2025), LangFIR (arXiv:2604.03532), SSPU (EMNLP 2025), SALVE (arXiv:2512.15938): 均为 SAE-based intervention/editing 的相关工作，构成本 proposal 的 building blocks。\n\n- 调研总结: 跨语言知识编辑是 2024-2026 年的活跃研究方向，portability bottleneck (EM < 10) 是公认的 open challenge。同时 SAE-based intervention 领域正在快速发展，但尚处于\"有效性争议\"阶段（Peng et al. vs Arad et al.）。SAE features + cross-lingual editing 的 exact combination 确实尚未被探索，proposal 的 gap identification 是准确的。但该 gap 更多是两条已有研究线的自然交叉点，而非源于根本性的 insight 突破。\n\n【Trivial Alternative 检验】:\n存在多个成本更低的 alternative 需要认真考虑：\n\n(1) **线性子空间投影**：AlphaEdit (ICLR 2025) 已使用 null-space constraints，LangEdit (ACL 2025 Findings) 已使用 null-space projection 做多语言 sequential editing。如果 portability 问题的本质是 edit vector 中的 language-specific component 干扰，一个简单的 PCA/SVD-based language subspace projection（不需要 SAE）能否达到类似效果？这些方法已经存在但尚未被直接用于解决 portability 问题，因此存在一个 simpler baseline gap。\n(2) **直接使用 LangSAE 方法 + ROME/MEMIT**：LangSAE 已经证明 SAE-based language identity removal 有效（+21.9% nDCG），直接将 LangSAE 的 language feature suppression pipeline 嫁接到 edit vector 上，无需 FCE metric、adaptive λ 等复杂组件，是否已经能捕获大部分增益？\n\nProposal 的增量价值声称在于\"adaptive soft projection with FCE\"——即不是简单地去除所有 language features，而是根据每个 feature 的 factual causal effect 自适应保留。这个增量是否真正关键，取决于 language-specific features 和 factual features 之间的 entanglement 程度。如果 entanglement 很低（大部分 language features 的 FCE 也很低），那么 simple binary suppression 就够了，adaptive λ 的增量价值有限。如果 entanglement 很高，那么即使 adaptive λ 也可能无法有效分离——因为高 entanglement 意味着 FCE 高的 feature 正是 language-specific 的，你保留了 language component。\n\n【前提假设检验】:\n核心逻辑链条中有 **两个关键未验证假设**：\n\n**(假设 A) Portability 失败的因果归因**：Proposal 假设 portability EM < 10 是因为 polysemantic neurons 将 factual relational structure 与 language identity 纠缠在一起。但 LU-LAFNs 原作者自己提出了另一个解释——portability metric 本身测量的是 reasoning ability（事实之间的推理链），而 parametric editing 根本无法改变 reasoning chains，只能改变 isolated facts。如果这个替代解释成立，那么无论 granularity 多细，representation-level editing 都无法改善 portability。这不是一个可以通过\"做更好的实验\"修补的假设缺陷——它质疑的是 idea 的根本前提。\n\nProposal 确实承认了这个风险并设计了 fallback（ablation A3 作为 falsification test），但这并不改变\"如果假设 A 错误，idea 的核心价值主张就不成立\"这个事实。负面结果虽有诊断价值，但在顶会接收标准下，\"我们证明了 SAE features 也不能解决 portability\"的故事线明显弱于\"SAE features 解决了 portability\"。\n\n**(假设 B) SAE features 的 language-factual 可分离性**：Proposal 假设 SAE features 能将 language-specific 和 factual components 分离到不同的 feature 上。但 Leask et al. (ICLR 2025) 已证明 SAE features 不是 atomic canonical units——一个 \"language\" feature 可能在更高分辨率下分解为多个 sub-features，其中一些同时 encode factual 信息。如果 language 和 factual 信息在 SAE feature 层面仍然高度纠缠（只是纠缠粒度变细了），adaptive λ 的有效性就会大打折扣。Proposal 声称用 \"continuous basis treatment\" 应对非原子性，但这更多是一个工程 patch 而非对根本问题的解决。\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   — 从\"两条现有 research line 的交叉组合\"来看，gap 确实存在，没有人做过 SAE features + cross-lingual editing 的 exact combination。但这个 gap 是一个 natural next step——FeatureEdit (ACL 2025) 证明了 SAE features > neurons for editing，LangSAE (2026) 证明了 SAE-based language feature suppression 有效，将两者结合做 cross-lingual editing 是一个几乎所有了解两篇论文的人都能想到的 extension。方法层面，adaptive soft projection with FCE 是 weighted feature suppression 的 variant，并非方法论上的范式创新。Chou et al. (arXiv:2507.13410) 已经证明了 single SAE feature 的 language steering 可行性，SCAN (arXiv:2603.15226) 已将 SAE-adjacent 方法用于 editing。总结：novelty 类型为 **combinatorial synthesis** 而非 **conceptual breakthrough**。在顶会标准下，这种 novelty 水平处于 borderline。\n\n2. Significance: 【中】\n   — 问题本身（portability bottleneck）是重要的、被公认的 open challenge（survey arXiv:2505.14393 explicitly 将其列为 key challenge）。如果方法 works，对 multilingual KE 领域确有推进。但问题在于：(a) 如果 positive result，审稿人可能会说 \"This is what I'd expect given polysemanticity theory\"——polysemantic neurons → 换 monosemantic features → 效果更好，逻辑链太顺畅，缺乏反直觉的 surprising element；(b) 如果 negative result，虽然有诊断价值但 impact 显著降低；(c) portability 的改善幅度可能有限（从 EM < 10 到，比如，EM ~15-20？），不一定构成 convincing breakthrough。此外，整个 claim 的 significance 高度依赖于假设 A 的正确性——而假设 A 本身未经验证。\n\n3. Related Work: 【强】\n   — Related work 覆盖极为全面，包括 4 个 tier 的分层梳理，涵盖了直接 baseline（LU-LAFNs, MEMIT, AlphaEdit, X-KDE, LangEdit）、methodological predecessors（FeatureEdit, SSPU, LangSAE, SCAN）、以及 adversarial work（Peng et al., Leask et al.）和 counter-evidence（Arad et al., Chou et al., Zhao et al.）。特别值得肯定的是，proposal 主动引入并回应了 SAE intervention skepticism，而非回避。Merging Methods for MKE (arXiv:2605.13919, May 2026) 作为 concurrent work 也被覆盖到。所有被引用的论文经调研均真实存在，描述基本准确。少数需要注意的点：FeatureEdit 的 context note（privacy erasure vs. factual editing 的区分）是诚实且恰当的。总体而言，这是该 proposal 最强的维度。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】:\nRelated work 维度的出色表现（强）为 proposal 提供了良好的学术基底，但 **Novelty 的 combinatorial 性质和 Significance 对未验证假设的依赖共同限制了上界**。\n\n具体推理：\n- Related Work【强】→ 确保不会因为 \"miss related work\" 或 \"unclear positioning\" 被拒，这是一个正面因素。\n- Novelty【中】→ 组合型 novelty 在顶会中处于 borderline。审稿人可能评价为 \"interesting engineering combination but the intellectual contribution is assembling existing pieces\"。FeatureEdit + LangSAE + cross-lingual editing 的组合虽然尚无人做，但 conceptual gap 较小，任何熟悉这两条 line 的研究者都能自然想到。这是限制上界的主要因素。\n- Significance【中】→ 问题重要但核心假设（假设 A：polysemantic entanglement 导致 portability 失败）未经验证，且存在替代解释（editing 根本无法传递 reasoning chains）。即使 positive result，\"monosemantic > polysemantic for editing\" 不够 surprising。\n- 概率区间 22-33% 对应 rubric 中\"有实质内核但核心发现可能 'I would have guessed this'\"的定位。中位 27% 反映了 Related Work 的加分和 Novelty/Significance 的限制之间的平衡。\n\n【主要风险】:\n1. **核心假设可能根本就错**：Portability bottleneck 的真实原因可能不是 polysemantic entanglement，而是 parametric editing 的根本局限（无法传递 reasoning chains）。如果假设 A 错误，整个 idea 的核心价值主张坍塌——即使实验做得再完美，也只能产出一篇 negative result 的诊断性论文。\n2. **Combinatorial novelty 不足以说服审稿人**：最核心的 methodological contribution（adaptive soft projection with FCE）本质上是 weighted feature suppression 的 variant，不是方法论范式创新。在\"SAE + X\"的研究已经日趋拥挤的背景下（SCAN, SSPU, SALVE, SpARE, FeatureEdit, SASFT 等均在 2025-2026 发表），审稿人可能认为\"又一个 SAE application\"的增量价值不够。\n```\n\n**补充说明（venue concern）**：本 proposal 的内容完全属于 NLP/计算语言学领域（多语言知识编辑），而 CoRL (Conference on Robot Learning) 是机器人学习会议。如果确实投稿 CoRL，则 topic mismatch 会导致 desk rejection 概率极高。建议确认目标会议是否为 ACL/EMNLP/NAACL/COLING 等 NLP 会议——上述概率估计基于投稿至 NLP 顶会的假设。\n\nSources:\n- [LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons (COLING 2025)](https://arxiv.org/abs/2406.16416)\n- [FeatureEdit / The Knowledge Microscope (ACL 2025)](https://arxiv.org/abs/2502.12483)\n- [Arad et al.: SAEs Are Good for Steering (EMNLP 2025)](https://arxiv.org/abs/2505.20063)\n- [Peng et al.: Use SAEs to Discover Unknown Concepts (2025)](https://arxiv.org/abs/2506.23845)\n- [Leask et al.: SAEs Do Not Find Canonical Units (ICLR 2025)](https://arxiv.org/abs/2502.04878)\n- [Mondal et al.: Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer (NAACL 2025)](https://arxiv.org/abs/2503.17456)\n- [LangSAE Editing (2026)](https://arxiv.org/abs/2601.04768)\n- [Chou et al.: Causal Language Control via Sparse Feature Steering](https://arxiv.org/abs/2507.13410)\n- [SCAN: Sparse Circuit Anchor for Lifelong Editing (2026)](https://arxiv.org/pdf/2603.15226)\n- [Merging Methods for Multilingual Knowledge Editing (2026)](https://arxiv.org/abs/2605.13919)\n- [CLM-Bench (2026)](https://arxiv.org/abs/2601.17397)\n- [X-KDE: Edit Once, Update Everywhere (ACL 2025 Findings)](https://arxiv.org/abs/2502.14645)\n- [Editing Across Languages: Survey (2025)](https://arxiv.org/abs/2505.14393)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation\n\n## Description\nCurrent cross-lingual knowledge editing faces a universal portability bottleneck: not just LU-LAFNs (COLING 2025) but ALL current methods achieve near-zero portability EM (< 10) on Bi-ZsRE, with the LU-LAFNs authors themselves noting 'all methods underperform on this metric without significant difference.' We hypothesize that this bottleneck has a specific causal mechanism: polysemantic neurons entangle factual relational structure with language identity, so any neuron-level editing that removes language components inevitably corrupts relational knowledge needed for portability. This hypothesis is independently supported by Mondal et al. (NAACL 2025 InsightsNLP), who showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer even outside the editing setting.\n\nWe propose SAE-Projected Editing: using pre-trained Qwen-Scope SAEs (64K features on Qwen3-8B) and Llama Scope SAEs (128K features on Llama-3.1-8B) to decompose edit vectors into finer-grained sparse features, classify each as language-specific or language-agnostic via cross-lingual activation-probability contrasts, then apply adaptive soft projection that suppresses language-specific components proportionally to their Factual Causal Effect (FCE) — a per-feature ablation-based metric measuring how much factual recall degrades when the feature is removed. Unlike binary feature zeroing — which Farrell et al. (2024) showed is ineffective — our adaptive λ-projection preserves factual content encoded in partially-entangled features while removing pure language-identity signal.\n\n**Engagement with SAE intervention skepticism:** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovery than intervention; however, Arad et al. (EMNLP 2025) directly rebut this by showing that output-score-based feature selection yields 2–3× improvement in SAE steering, matching supervised methods. The critique applies to naive feature selection, not SAE interventions as a paradigm. We incorporate output-score filtering into our pipeline. Chou et al. (arXiv:2507.13410) provide further feasibility evidence: modifying a single SAE feature achieves up to 90% language steering success on Gemma-2B/9B. Leask et al. (ICLR 2025) show SAE features are not atomic canonical units — larger latents decompose into sub-components. We accommodate this by: (a) treating features as a continuous weighted basis rather than binary switches, (b) using adaptive λ coefficients that handle partial feature overlap, and (c) ablating across SAE widths (16K/64K/128K) to identify task-appropriate granularity per Leask et al.'s recommendation.\n\n**FeatureEdit context note:** The +23% reliability and 2.8× generalization gains from FeatureEdit (ACL 2025) are for knowledge erasure on the PrivacyParaRel privacy dataset using Gemma-2 models, not factual knowledge editing or cross-lingual propagation. We cite these as evidence that features outperform neurons as representation-level intervention units, but do not assume these specific gains transfer to the editing setting.\n\n**FCE metric protocol:** For each of ~64K SAE features, we first compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success across ≥5,000 multilingual facts (computational cost: ~4 GPU-hours for forward passes). The top ~2K features by |r_pb| undergo full causal ablation: each feature is individually zeroed, and the change in factual recall probability is measured (FCE). This two-stage approach reduces the 64K × 5K evaluation matrix to a tractable 2K × 5K, requiring ~40 GPU-hours. Bootstrap confidence intervals (1000 resamples) provide uncertainty estimates for FCE values. As a validation check, we compute Spearman rank correlation between r_pb and FCE on the 2K features to verify the proxy quality.\n\nKey contributions: (1) First application of SAE feature decomposition to cross-lingual knowledge editing, providing ~5-10× finer granularity than neuron-level LAFN identification; (2) Adaptive soft projection mechanism that explicitly accounts for factual-language feature entanglement via a concrete, causal FCE metric with a two-stage efficient computation protocol; (3) Principled engagement with SAE intervention skepticism (Peng et al., Leask et al.) through output-score filtering, continuous-basis treatment, and multi-width ablation; (4) Testable portability hypothesis: if SAE features do NOT improve portability EM over neuron-level approaches (ablation A3), this falsifies the polysemanticity-entanglement explanation and has standalone diagnostic value; (5) Reconstruction fidelity validation protocol establishing whether SAE round-trip preserves edit vector quality across dictionary sizes.\n\nWe evaluate on CLM-Bench (zh-en), Bi-ZsRE, and MzsRE across 12 languages, targeting improvements over LU-LAFNs (77.87 Bi-ZsRE avg on bloomz-7b1-mt; MzsRE results reported as per-language heatmaps rather than a single average) particularly on portability metrics. Primary baselines: LU-LAFNs, FeatureEdit (adapted cross-lingual), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit.\n\n**Risk mitigation:** The core risk is that the portability bottleneck is NOT caused by polysemantic entanglement but by a more fundamental limitation (e.g., the portability metric itself measuring reasoning ability that editing cannot improve). We address this through: (a) explicit FCE measurement before editing to quantify the entanglement ceiling, (b) adaptive λ-projection that preserves high-FCE features, (c) reconstruction fidelity go/no-go gate, (d) ablation A3 as a direct falsification test, and (e) relational follow-up evaluation (A2) that provides a complementary portability measure independent of the Bi-ZsRE metric. If SAE features fail to improve portability, the negative result still contributes a rigorous decomposition analysis of what fraction of factual information resides in language-specific vs. language-agnostic features — valuable for the multilingual interpretability community. Fallback: hybrid approach combining SAE-projected editing for low-entanglement facts with LU-LAFNs for high-entanglement cases.\n\n## Core Problem\nCross-lingual knowledge editing methods face two linked failures: (1) raw edit vectors reside in nearly orthogonal, language-specific subspaces (CLM-Bench), and (2) neuron-level approaches like LU-LAFNs that identify language-agnostic neurons achieve high monolingual reliability but suffer catastrophically low portability (26.43% F1, EM < 5) — a failure shared by ALL current methods (all EM < 10 on Bi-ZsRE portability), suggesting a fundamental representation-level bottleneck. We hypothesize that this bottleneck stems from polysemantic neurons entangling factual relational structure with language identity: edits that operate at neuron granularity cannot cleanly separate these components, corrupting relational knowledge during cross-lingual transfer. Can sparse autoencoder feature decomposition — which yields finer-grained, more monosemantic units — provide a cleaner separation that better preserves relational structure, and is this hypothesis even testable given recent challenges to SAE feature canonicality (Leask et al., ICLR 2025)?\n\n## Opportunity\nCLM-Bench (arXiv:2601.17397, Jan 2026) provided geometric evidence that Chinese and English edit vectors are nearly orthogonal, explaining why ROME/MEMIT fail cross-lingually (~20% reliability). LU-LAFNs (COLING 2025) achieved 77.87 avg on Bi-ZsRE by targeting language-agnostic neurons, but its neuron-level approach identifies 67.9% of neurons as LAFNs — an extremely coarse decomposition reflecting neuron polysemanticity — and ALL methods achieve near-zero portability EM (< 10 across the board), which the authors attribute to the difficulty of measuring reasoning without a reasoning process. Crucially, Mondal et al. (NAACL 2025 InsightsNLP) independently showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer on XNLI/XQuAD, reinforcing the case that neuron-level decomposition is fundamentally too coarse.\n\nMeanwhile, FeatureEdit (ACL 2025) demonstrated that SAE features outperform neurons for knowledge erasure on PrivacyParaRel (~0.80 vs ~0.65 reliability, ~0.70 vs ~0.25 generalization on Gemma-2 2B/9B) — though notably this was for privacy-knowledge erasure, not factual editing or cross-lingual propagation, so these gains may not directly transfer. LangSAE (arXiv:2601.04768) proved SAE-based language identity removal improves cross-lingual retrieval by +21.9% nDCG@20. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying a single SAE feature on Gemma-2B/9B, demonstrating that SAE-based language manipulation is feasible and precise.\n\nHowever, recent work challenges SAE interventions: Peng et al. (arXiv:2506.23845) argue SAEs are better for concept discovery than acting on known concepts, finding SAE-based steering underperforms prompting/fine-tuning. Critically, Arad et al. (EMNLP 2025) rebut this: proper feature selection via output-score filtering yields 2–3× improvement in SAE steering, matching supervised methods — the issue was feature selection, not SAE interventions per se. Leask et al. (ICLR 2025) show SAE features aren't canonical atomic units — larger latents decompose into combinations — but recommend pragmatic choice of dictionary size suited to task, and our adaptive soft projection naturally accommodates non-atomicity by treating features as a continuous basis rather than binary switches.\n\nThe missing link: no work has combined SAE feature-level decomposition with cross-lingual knowledge editing. SAE features offer ~64K monosemantic units (vs. ~14K polysemantic neurons), enabling more precisely targeted language-component manipulation that may better preserve relational/factual structure — a hypothesis we propose to test directly.\n\n## Related Work / Landscape\nCross-lingual knowledge editing is a recognized open problem: the survey (arXiv:2505.14393) identifies language anisotropy and edit scalability as key challenges. The field is structured in three tiers:\n\n**Tier 1 — Direct multilingual editing baselines:** MEMIT/M-MEMIT apply locate-then-edit across languages (74.86 avg on Bi-ZsRE but ~20% cross-lingual reliability). AlphaEdit (ICLR 2025) uses null-space constraints. Merging Methods for MKE (arXiv:2605.13919, May 2026) explores vector merging with shared covariance for 12-language editing but without representation-level decomposition.\n\n**Tier 2 — Neuron/representation-level multilingual editing:** LU-LAFNs (COLING 2025, arXiv:2406.16416) is the closest prior work — identifies language-agnostic factual neurons via activation frequency intersection across languages, achieving 77.87 avg on Bi-ZsRE (bloomz-7b1-mt). However, it identifies 67.9% of neurons as LAFNs (extremely coarse), and ALL methods achieve near-zero portability (EM < 10, F1 ~26-36%), which the authors acknowledge as a universal challenge rather than a method-specific failure. Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456) provide independent evidence that neuron-level language-specific interventions are insufficient for cross-lingual transfer. MEMLA (arXiv:2406.11566) uses neuron masking with LoRA but doesn't leverage monosemantic features. X-KDE (ACL 2025 Findings, arXiv:2502.14645) uses instruction tuning + preference optimization (+8.19% avg improvement). LangEdit (ACL 2025 Findings, arXiv:2506.10800) applies null-space projection for multilingual sequential editing across 6 languages.\n\n**Tier 3 — SAE-based editing and language feature work (our building blocks):** FeatureEdit from 'The Knowledge Microscope' (ACL 2025, arXiv:2502.12483) is the first SAE-feature-based model editing method — uses Gemma Scope JumpReLU SAEs to identify knowledge features and zero out specific weight positions. On the PrivacyParaRel knowledge-erasure benchmark (not factual editing), features achieve ~0.80 reliability (vs. ~0.65 for neurons) and ~0.70 generalization (vs. ~0.25), demonstrating features' advantage for representation-level interventions. However, it is monolingual English-only, targets knowledge erasure rather than cross-lingual propagation, and these gains may not directly transfer to the editing setting. SSPU (EMNLP 2025, arXiv:2505.24428) shows SAE-guided subspace projection via QR decomposition can unlearn knowledge while preserving non-target capabilities. LangSAE (arXiv:2601.04768) removes language identity from embeddings using SAE feature suppression (+21.9% nDCG@20). SAE-LAPE/LangFIR (arXiv:2604.03532) discover sparse language-specific features using activation probability contrasts. SASFT (ICLR 2026) shows SAE-guided fine-tuning preserves targeted knowledge. SpARE (NAACL 2025, arXiv:2410.15999) uses SAE-based representation engineering for knowledge selection steering but not cross-lingually. SCAN (arXiv:2603.15226, Mar 2026) uses sparse transcoders for lifelong editing on Qwen3/Llama3.1 but addresses sequential stability, not cross-lingual transfer. Farrell et al. (arXiv:2410.19278) found that zero ablation of SAE features is ineffective for knowledge unlearning — negative scaling is necessary. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying single SAE features on Gemma-2B/9B, providing direct feasibility evidence for SAE-based language manipulation.\n\n**Tier 4 — SAE intervention skepticism and counter-evidence (critical context):** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovering unknown concepts than acting on known ones, finding SAE-based steering underperforms prompting/fine-tuning. However, Arad et al. (EMNLP 2025, arXiv:2505.20063) directly rebut this: by distinguishing 'input features' (capture input patterns) from 'output features' (causally affect model behavior) and filtering by output scores, SAE steering achieves 2–3× improvement, matching supervised methods. The issue was naive feature selection, not SAE interventions as a paradigm. Zhao et al. (arXiv:2505.15038) further show denoising concept vectors via SAE improves steering 4–16%. SAE-SSV (EMNLP 2025, arXiv:2505.16188) achieves high steering success rates using supervised feature selection in sparse spaces. Leask et al. (ICLR 2025, arXiv:2502.04878) demonstrate SAE features are neither atomic nor canonical — meta-SAEs decompose latents into sub-components (e.g., 'Einstein' → 'scientist' + 'Germany' + 'famous person'), and smaller SAEs miss information captured by larger ones. They recommend pragmatic dictionary size selection rather than assuming canonicality. Our approach accommodates this by treating SAE features as a practical continuous basis with adaptive coefficients, not as binary canonical units.\n\n**The gap:** No work combines SAE feature decomposition with cross-lingual knowledge editing. Specifically, no one has (a) used monosemantic SAE features instead of polysemantic neurons to decompose cross-lingual edit vectors, (b) tested whether finer-grained decomposition causally improves portability by preserving relational structure, or (c) engaged with the feature-selection insights from Arad et al. to ensure intervention-effective features are targeted.\n\n## Approach\n**Phase 1: Feature Classification with Output-Score Filtering (Weeks 1-2).** Leverage pre-trained SAEs — Qwen-Scope (64K features, 16× expansion) on Qwen3-8B and Llama Scope (128K features, 32× expansion) on Llama-3.1-8B — to decompose residual-stream activations at editing-critical layers (layers 12-25 for Qwen3-8B based on LU-LAFNs' LAFN distribution peaks). Classify each feature as language-specific, language-agnostic, or factual using activation-probability contrasts across Chinese, English, and 4+ additional languages (following SAE-LAPE/LangFIR methodology). Critically, following Arad et al.'s (EMNLP 2025) insight that input-pattern features and output-causal features rarely co-occur, compute output scores for all features to ensure we target features that causally affect model behavior, not merely correlational activations — this addresses the core criticism of Peng et al. For each language-specific feature f_i, compute its Factual Causal Effect (FCE): ablate f_i and measure the change in correct factual recall probability across a multilingual fact corpus of ≥5,000 facts (drawn from Bi-ZsRE + MzsRE test sets, held out from editing evaluation). FCE(f_i) = |P(correct | f_i active) - P(correct | f_i ablated)|. This produces a per-feature entanglement map. FCE is preferred over mutual information because: (a) it is causal rather than correlational, (b) it avoids the curse-of-dimensionality problems that plague MI estimation with 64K+ features (KSG estimators break down beyond ~10 dimensions), and (c) it is directly interpretable as the factual cost of removing a feature. As a computationally efficient proxy during initial screening, we also compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success, filtering to the top ~2K candidate features for full FCE ablation (reducing 64K × 5K evaluations to ~2K × 5K).\n\n**Phase 2: SAE-Projected Editing with Adaptive Soft Projection (Weeks 3-5).** For a given ROME/MEMIT edit vector e, decompose it into the SAE feature basis: e ≈ Σ_j α_j d_j (where d_j are SAE decoder directions and α_j are coefficients from the encoder). Following Farrell et al.'s finding that binary zeroing is ineffective and Leask et al.'s evidence that features are not atomic canonical units, we apply adaptive soft projection that treats features as a continuous basis: e_proj = e - Σ_{i ∈ L_spec} λ_i · α_i · d_i, where λ_i ∈ [0, 1] is inversely proportional to FCE(f_i) — features with high factual causal effect are preserved more, pure language-identity features (low FCE, high language specificity) are fully suppressed. This formulation naturally handles Leask et al.'s non-atomicity concern: since features are weighted continuously rather than treated as binary switches, partial overlap between sub-features is accommodated through the λ gradient. The projected vector e_proj is then applied via the standard locate-then-edit pipeline.\n\n**Phase 3: Reconstruction Fidelity Validation (Weeks 3-4, parallel).** Before full-scale editing, validate that SAE round-trip reconstruction preserves edit vector fidelity. Measure: (a) cosine similarity between original and reconstructed edit vectors, (b) monolingual edit success rate with SAE-reconstructed vectors (no language feature removal) vs. original ROME/MEMIT — this isolates reconstruction error from projection effects. If reconstruction degrades edit quality by >5%, investigate top-k sparsity adjustments or layer-specific SAE selection. Following Leask et al.'s recommendation, test multiple SAE widths (16K, 64K, 128K where available) to identify task-appropriate granularity rather than assuming larger is better. Establish a reconstruction quality threshold as a go/no-go gate.\n\n**Phase 4: Evaluation and Ablation (Weeks 5-8).** Evaluate on CLM-Bench (1,010 zh-en pairs), Bi-ZsRE, and MzsRE (12 languages) using Qwen3-8B and Llama-3.1-8B. Primary baselines: LU-LAFNs (77.87/Bi-ZsRE on bloomz-7b1-mt — the SOTA to beat), FeatureEdit (adapted to cross-lingual setting), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit. Secondary baselines: SCAN, MEMLA. Key ablations: (A1) Full zeroing vs. soft projection — measuring factual content loss, directly testing Farrell et al.'s finding in the cross-lingual setting. (A2) Relational structure preservation: for edited facts, measure whether the model correctly answers relational follow-up questions (e.g., after editing 'capital of X', test 'X is in which continent?') — this directly tests the portability hypothesis. (A3) Feature granularity: SAE features (64K/128K) vs. neuron-level LAFNs (~10K) vs. random subspace projection — if SAE features do not improve portability over neurons, this falsifies our core hypothesis. (A4) λ scheduling: fixed λ vs. FCE-adaptive λ vs. oracle λ (per-fact optimal). (A5) Layer selection: which layers' SAEs are most critical for cross-lingual transfer. (A6) SAE width: 16K vs. 64K vs. 128K features, testing Leask et al.'s prediction that task-appropriate granularity matters more than raw dictionary size. (A7) Output-score filtering (per Arad et al.): restrict projection to high-output-score features vs. all language-classified features.\n\n## Inspiration\nLU-LAFNs' universal portability failure (all methods EM < 10) revealing a fundamental representation-level bottleneck + Mondal et al.'s independent evidence that neuron-level language interventions are insufficient + FeatureEdit's demonstration that SAE features outperform neurons for knowledge erasure + LangSAE proving language features can be surgically suppressed + Chou et al.'s 90% language steering with single SAE features + CLM-Bench's geometric evidence of language-specific subspaces + SSPU's QR-decomposition subspace methodology + Arad et al.'s insight that output-score feature selection rescues SAE interventions + Farrell et al.'s finding that soft scaling outperforms zero ablation\n\n## Key References\n- LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons (COLING 2025, arXiv:2406.16416) — PRIMARY BASELINE\n- FeatureEdit / The Knowledge Microscope: Features as Better Analytical Lenses than Neurons (ACL 2025, arXiv:2502.12483) — METHODOLOGICAL PREDECESSOR (knowledge erasure, not editing)\n- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026, arXiv:2601.17397)\n- LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal (arXiv 2026, arXiv:2601.04768)\n- LangEdit: Mitigating Negative Interference in Multilingual Sequential Knowledge Editing through Null-Space Constraints (ACL 2025 Findings, arXiv:2506.10800)\n- SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing (arXiv 2026, arXiv:2603.15226)\n- SSPU: Model Unlearning via Sparse Autoencoder Subspace Guided Projections (EMNLP 2025, arXiv:2505.24428)\n- Applying Sparse Autoencoders to Unlearn Knowledge in Language Models (arXiv 2024, arXiv:2410.19278)\n- X-KDE: Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs (ACL 2025 Findings, arXiv:2502.14645)\n- MEMLA: Enhancing Multilingual Knowledge Editing with Neuron-Masked Low-Rank Adaptation (arXiv 2024, arXiv:2406.11566)\n- Editing Across Languages: A Survey of Multilingual Knowledge Editing (arXiv 2025, arXiv:2505.14393)\n- SAE-LAPE: Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders (ACL 2025, arXiv:2505.05111)\n- LinguaLens: Towards Interpreting Linguistic Mechanisms of Large Language Models via Sparse Auto-Encoder (EMNLP 2025)\n- SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs (ICLR 2026)\n- AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models (ICLR 2025)\n- SpARE: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (NAACL 2025, arXiv:2410.15999)\n- LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering (arXiv 2026, arXiv:2604.03532)\n- Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey (arXiv 2026, arXiv:2605.13919)\n- SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks (arXiv 2025, arXiv:2512.15938)\n- Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models (arXiv 2026, arXiv:2605.11887)\n- Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders (arXiv 2024, arXiv:2410.20526)\n- Language-Specific Neurons: The Key to Multilingual Capabilities in Large Language Models (ACL 2024, arXiv:2402.16438)\n- Peng et al.: Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts (arXiv 2025, arXiv:2506.23845) — ADVERSARIAL: argues SAEs underperform for interventions\n- Leask et al.: Sparse Autoencoders Do Not Find Canonical Units of Analysis (ICLR 2025, arXiv:2502.04878) — ADVERSARIAL: shows features are not atomic/canonical\n- Arad et al.: SAEs Are Good for Steering — If You Select the Right Features (EMNLP 2025, arXiv:2505.20063) — REBUTTAL to Peng et al.: output-score filtering yields 2-3× improvement\n- Mondal et al.: Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer (NAACL 2025 InsightsNLP, arXiv:2503.17456) — SUPPORTS motivation: neuron-level is insufficient\n- Chou et al.: Causal Language Control in Multilingual Transformers via Sparse Feature Steering (arXiv 2025, arXiv:2507.13410) — FEASIBILITY: 90% language steering with single SAE feature\n- Zhao et al.: Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering (arXiv 2025, arXiv:2505.15038) — SAE steering improves 4-16% with denoising\n- SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models (EMNLP 2025, arXiv:2505.16188)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '450-550 (SAE feature classification + FCE ablation analysis ~120h on 1×A100 — increased due to per-feature ablation; reconstruction fidelity validation across SAE widths ~40h; editing experiments across 2 models × 3 benchmarks × 8+ baselines ~250h; ablation studies A1-A7 ~120h; analysis ~40h)', 'timeline': '10-12 weeks', 'estimated_gpu_cost': '$1,125-$1,375 (A100 at ~$2.50/hr; major savings from pre-trained Qwen-Scope and Llama Scope SAEs)'}\n- **human_in_loop**: {'gpu_hours': '400-500', 'timeline': '7-9 weeks', 'claude_api_cost': '$150-$250 (code generation for SAE analysis pipeline, FCE computation, experiment orchestration)', 'estimated_gpu_cost': '$1,000-$1,250'}\n- **auto_research**: {'gpu_hours': '400-500', 'timeline': '5-7 weeks', 'claude_api_cost': '$400-$550 (end-to-end experiment management, hyperparameter sweeps for λ, paper drafting)', 'estimated_gpu_cost': '$1,000-$1,250', 'speed_bottleneck': 'FCE ablation requires sequential per-feature evaluation (mitigated by r_pb pre-screening to ~2K features); sequential editing experiments per model-benchmark pair; CLM-Bench evaluation involves Chinese cultural knowledge judgment requiring human spot-checking'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T18:58:29.155Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:58:29.155Z",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T18:58:29.169Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have comprehensive field understanding. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- LU-LAFNs (COLING 2025, arXiv:2406.16416): 最直接的 prior work。通过跨语言激活频率交集识别 language-agnostic factual neurons (LAFNs)，在 Bi-ZsRE 上 bloomz-7b1-mt 达到 77.87 avg。关键发现：67.9% 的 neurons 被标记为 LAFNs（极粗粒度），且**所有方法**在 portability EM 上均 < 10。作者自己承认这是普遍难题而非方法特定失败。
- FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483): 首个基于 SAE feature 的模型编辑方法。在 PrivacyParaRel 隐私知识擦除任务上证明 features 优于 neurons（reliability ~0.80 vs ~0.65, generalization ~0.70 vs ~0.25）。但任务是隐私擦除而非事实编辑，模型是 Gemma-2，非跨语言场景。
- CLM-Bench (arXiv:2601.17397, Jan 2026): 提供了中英编辑向量近乎正交的几何证据，解释了 ROME/MEMIT 跨语言失败（~20% reliability）。
- Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456): 独立证据表明 neuron-level language-specific interventions 对跨语言迁移无效（XNLI/XQuAD），支持"neuron 粒度不够"的论点。
- LangSAE Editing (arXiv:2601.04768, Jan 2026): 用 SAE feature suppression 移除 language identity，在多语言检索上 +21.9% nDCG@20。但目标是检索而非知识编辑。
- Chou et al. (arXiv:2507.13410, Jul 2025): 通过修改单个 SAE feature 在 Gemma-2B/9B 上实现高达 90% 的语言转向成功率，证明 SAE-based language manipulation 的可行性。
- Peng et al. (arXiv:2506.23845): 论证 SAE 适合 concept discovery 而非 acting on known concepts，SAE steering 不如 prompting/fine-tuning。
- Arad et al. (EMNLP 2025, arXiv:2505.20063): 反驳 Peng et al.，通过 output-score filtering 实现 SAE steering 2-3× 提升，匹配 supervised methods。
- Leask et al. (ICLR 2025, arXiv:2502.04878): 证明 SAE features 非 atomic/canonical units，大 SAE 的 latents 可分解为小 SAE latents 的组合。建议按任务需要选择 dictionary size。
- SCAN (arXiv:2603.15226, Mar 2026): 用 sparse transcoders 做 lifelong editing（Qwen3/Llama3.1），但目标是 sequential stability 而非跨语言迁移。
- X-KDE (ACL 2025 Findings, arXiv:2502.14645): 用 instruction tuning + preference optimization 做跨语言知识同步，+8.19% avg improvement。
- LangEdit (ACL 2025 Findings, arXiv:2506.10800): 用 null-space projection 做多语言 sequential editing。
- AlphaEdit (ICLR 2025): 用 null-space constraints 做知识编辑。
- Merging Methods for MKE (arXiv:2605.13919, May 2026): 用 vector merging + shared covariance 做 12 语言编辑，但没有 representation-level decomposition。
- SAE-LAPE/LangFIR (arXiv:2604.03532, ACL 2025 arXiv:2505.05111): 用 activation probability contrasts 发现 sparse language-specific features。

- **调研总结**: 跨语言知识编辑是一个活跃的研究方向，2025-2026 年密集出现了多种方法（LU-LAFNs、X-KDE、LangEdit、AlphaEdit、Merging Methods）。与此并行，SAE-based 方法在知识擦除 (FeatureEdit)、语言转向 (Chou et al.)、语言 identity 移除 (LangSAE) 等任务上已证明有效。但**确实没有工作将 SAE feature decomposition 直接应用于跨语言知识编辑**——这个 gap 是真实存在的。Proposal 处于两条成熟研究线（跨语言编辑 + SAE intervention）的交汇点，是一个"natural next step"型组合创新。

【Trivial Alternative 检验】:
存在至少两个更简单的 alternative 需要考虑：

1. **线性子空间投影（非 SAE）**: LangEdit 已经使用 null-space projection 处理多语言编辑，AlphaEdit 也用了 null-space constraints。如果语言特定分量和事实分量在 residual stream 中是线性可分的（这本身是一个合理的假设，CLM-Bench 的正交性发现暗示了这一点），那么一个简单的 PCA-based 或 linear probe-based 语言分量移除（不需要 SAE）可能就够了。Proposal 没有解释为什么 SAE 提供的非线性稀疏分解比线性投影本质上更好。

2. **多语言并行编辑**: 直接在每种目标语言中独立执行编辑（即对每种语言分别生成 edit vector 并应用），虽然 compute 成本更高但避免了跨语言迁移问题。X-KDE 的 instruction tuning 方法本质上也是绕过了 representation-level 分解。

**增量价值所在**: Proposal 的增量价值在于：(a) 如果 polysemantic entanglement 假说正确，线性方法确实无法处理非线性的 factual-language 纠缠；(b) SAE 的 ~64K monosemantic features 提供了 neurons (~14K) 无法达到的粒度。但这两个前提都未经验证——(a) 是核心假设本身，(b) 在 Leask et al. 的 non-atomicity 发现下有所减弱。

【前提假设检验】:
核心 claim 的逻辑链条中，有以下未验证的关键假设：

1. **"Portability 瓶颈是由 polysemantic entanglement 造成的"** —— 这是整个工作的核心假设，但完全未经验证。LU-LAFNs 作者自己将低 portability 归因于"the difficulty of measuring reasoning without a reasoning process"，即 portability metric 本身可能测量的是推理能力而非事实迁移。如果瓶颈不是 representation-level 的（而是 decoding/reasoning-level 的），那么无论多精细的 representation 分解都无法解决。

2. **"SAE features 能对 factual 和 language-specific 分量做比 neurons 更干净的分离"** —— Leask et al. (ICLR 2025) 已证明 SAE features 不是 atomic canonical units。虽然 proposal 用 continuous weighting 来 accommodate，但这本质上是在承认分离不干净的前提下做 soft mitigation，削弱了"finer granularity = cleaner separation"的核心论点。

3. **"FCE metric 能可靠识别 factual-language 纠缠程度"** —— FCE 是 ablation-based 的（去掉 feature → 测 factual recall 变化），但 ablation 只测量 necessary condition（feature 是否 necessary for recall），不测量 sufficiency。一个 feature 可能对 factual recall 不是 necessary（因为有冗余编码）但仍然 encode factual information。这可能导致高估"safe to remove"的 language-specific features 的数量。

4. **"FeatureEdit 在知识擦除上的优势能迁移到跨语言事实编辑"** —— Proposal 自己承认了这个 gap，但整个工作的 motivation 部分仍然大量依赖 FeatureEdit 的结果作为"features > neurons"的证据。擦除和编辑是不同操作（一个是移除信息，一个是替换信息 + 保持结构），迁移性未知。

其中第 1 点是最关键的——如果 portability bottleneck 的原因不是 representation entanglement 而是更深层的 reasoning limitation，整个技术路线就失去了根基。

【3 维度打分】:

1. **Novelty: 中** — 
   Gap 确实存在：搜索确认无工作将 SAE feature decomposition 应用于跨语言知识编辑。但这本质上是一个 "combine A (SAE features, well-studied) with B (cross-lingual editing, well-studied)" 型创新。对熟悉 FeatureEdit (ACL 2025) + LU-LAFNs (COLING 2025) + LangSAE (2026) 的研究者来说，"用 SAE features 代替 neurons 做跨语言编辑"是相当自然的 next step——不是"为什么没人想到"，而是"时间问题"。
   
   具体技术贡献上：activation-probability contrasts 来自 SAE-LAPE；output-score filtering 来自 Arad et al.；soft projection 而非 binary zeroing 的 insight 来自 Farrell et al.。Proposal 自己发明的核心技术只有 FCE metric 和 adaptive λ-projection 机制，这些是 solid 但 incremental 的方法贡献。
   
   如果核心发现是 positive（SAE features 确实提升了 portability），审稿人的反应更可能是 "makes sense, this is what I'd expect given FeatureEdit + LangSAE results" 而非 "surprising"。如果是 negative（SAE features 也无法提升 portability），这会更 surprising 也更有诊断价值——但 proposal 将此定位为 fallback 而非主打结论。

2. **Significance: 中** — 
   正面：跨语言知识编辑的 portability bottleneck 是一个被社区广泛认可的真实问题（survey arXiv:2505.14393 将其列为 key challenge）。如果能突破 EM < 10 的 universal ceiling，影响力确实显著。
   
   限制因素：(a) 即使 SAE decomposition 有帮助，从 EM ~5 提升到 EM ~15-20 仍然是相当 modest 的绝对改进，可能不足以让人感到"paradigm shift"；(b) 依赖 pre-trained SAEs（Qwen-Scope, Llama Scope），方法的通用性受限于 SAE 的可用性；(c) 目前的 SOTA 模型越来越强大，knowledge editing 这个范式本身面临来自 RAG、continual pretraining 等替代方案的竞争——如果 editing 范式本身在实践中被弱化，这条线的长期价值有限。
   
   此外，结果的可推广性取决于 polysemantic entanglement 假说的正确性，如果假说错误，方法就缺乏 principled 的理论基础。

3. **Related Work: 强** — 
   这是 proposal 最强的维度。四层分类（direct multilingual editing → neuron-level → SAE-based → SAE skepticism/counter-evidence）结构清晰。对每篇关键工作的描述经我搜索验证均准确——包括 FeatureEdit 的任务域限制（privacy erasure not factual editing）、Peng et al. vs Arad et al. 的论辩、Leask et al. 的 non-canonicality 挑战及其 pragmatic recommendation、Farrell et al. 的 binary zeroing 失败。
   
   特别值得肯定的是：(a) 对 adversarial work 的诚实对待和 principled engagement（多数 proposal 会回避 Peng et al. 和 Leask et al.）；(b) 对 FeatureEdit 结果的审慎引用（明确标注 domain mismatch）；(c) 对 Mondal et al. 的引用作为独立支持证据。References 经搜索验证均真实存在且描述准确。
   
   唯一的小缺口是未讨论 null-space projection methods (AlphaEdit, LangEdit) 作为更简单的 language component removal baseline——这正是 Trivial Alternative 检验中暴露的问题。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Novelty（中）是主要的上界限制因素——这是一个"自然的下一步"组合创新，核心 insight（用 SAE features 代替 neurons）对领域内研究者来说不 surprising。Related Work（强）抬高了下限——proposal 对领域的理解和定位是出色的，降低了"审稿人发现致命遗漏"的风险。Significance（中）居中——问题真实但改进空间的绝对值可能有限。

核心假设（polysemantic entanglement 是 portability 瓶颈的原因）未经验证且存在 plausible alternative explanation（portability 测的是 reasoning 而非 representation），这构成了 idea 层面的实质风险——如果这个假设错误，即使实验执行完美，审稿人也会认为整个 framing 有问题。Trivial alternative（线性子空间投影）的威胁也降低了估值——如果一个简单的 PCA-based 语言分量移除达到类似效果，SAE 的复杂度就难以 justify。

Dual-outcome 设计（negative result 也有诊断价值）是合理的 hedge，但在竞争激烈的 top venue 中，以 negative result 为主的 paper 中稿概率会显著低于 positive result paper。

**注意**: Proposal 目标投稿 CoRL 2026（Conference on Robot Learning）。这是一个纯 NLP/mechanistic interpretability 工作，与 CoRL 的 robotics scope 完全不匹配。如果确实投稿 CoRL，中稿概率实际上接近 0%。上述 22-33% 的估计是假设投稿至合适的 NLP 会议（如 ACL/EMNLP/NAACL 2026）。

【主要风险】: 
1. **核心假设可能为假**: Portability bottleneck 的真正原因可能不是 polysemantic entanglement，而是 portability metric 测量的是 reasoning ability（LU-LAFNs 作者自己的解释）。如果如此，任何 representation-level decomposition（无论多精细）都无法改善 portability，整个技术路线的 framing 将被审稿人质疑。
2. **Trivial alternative 未被排除**: Proposal 没有论证为什么 SAE-based decomposition 比更简单的线性子空间投影（类似 AlphaEdit/LangEdit 的 null-space approach 但针对 language component）本质上更优。审稿人可能要求一个"linear projection baseline"并发现 SAE 的增量收益不 justify 其复杂度。
```

Sources:
- [LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons](https://aclanthology.org/2025.coling-main.385/)
- [The Knowledge Microscope: Features as Better Analytical Lenses than Neurons](https://arxiv.org/abs/2502.12483)
- [CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment](https://arxiv.org/pdf/2601.17397)
- [Language-Specific Neurons Do Not Facilitate Cross-Lingual Transfer](https://aclanthology.org/2025.insights-1.6/)
- [LangSAE Editing: Improving Multilingual Information Retrieval](https://arxiv.org/abs/2601.04768)
- [Chou et al.: Causal Language Control via Sparse Feature Steering](https://arxiv.org/abs/2507.13410)
- [Peng et al.: Use SAEs to Discover Unknown Concepts](https://arxiv.org/html/2506.23845v1)
- [Arad et al.: SAEs Are Good for Steering — If You Select the Right Features](https://arxiv.org/abs/2505.20063)
- [Leask et al.: Sparse Autoencoders Do Not Find Canonical Units](https://arxiv.org/abs/2502.04878)
- [SCAN: Sparse Circuit Anchor for Lifelong Editing](https://arxiv.org/pdf/2603.15226)
- [X-KDE: Edit Once, Update Everywhere](https://arxiv.org/pdf/2502.14645)
- [Editing Across Languages: A Survey](https://arxiv.org/html/2505.14393)
- [Emergent Mind: SAE Steering Topic](https://www.emergentmind.com/topics/sparse-autoencoder-steering)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- LU-LAFNs (COLING 2025, arXiv:2406.16416): 最直接的竞争工作。通过激活频率交集识别跨语言共享的"语言无关事实神经元"(LAFNs)，在Bi-ZsRE上达到77.87 avg。但67.9%的神经元被识别为LAFNs（极粗粒度），且所有方法在portability EM上均<10。论文真实存在，proposal描述准确。
- FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483): SAE特征用于知识擦除（非事实编辑），在PrivacyParaRel上特征vs神经元有显著优势（~0.80 vs ~0.65 reliability）。论文真实存在，proposal对其适用范围的限定（隐私擦除而非跨语言编辑）是诚实的。
- LangSAE Editing (arXiv:2601.04768, Jan 2026): 用SAE特征抑制语言身份信号改善多语言信息检索，+21.9% nDCG@20。论文真实，但其目标是检索而非知识编辑。
- Chou et al. (arXiv:2507.13410, Jul 2025): 修改单个SAE特征实现高达90%语言转向成功率（Gemma-2B/9B）。论文真实，为SAE语言操控的可行性提供了直接证据。
- Arad et al. (EMNLP 2025, arXiv:2505.20063): 证明SAE steering失败源于特征选择不当而非SAE范式本身，output-score filtering带来2-3×提升。论文真实存在于ACL Anthology，proposal的引用和解读准确。
- Leask et al. (ICLR 2025, arXiv:2502.04878): 证明SAE特征非原子/非规范化单位。论文真实，proposal对其的应对策略（连续加权基而非二值开关）是合理的。
- Mondal et al. (NAACL 2025 InsightsNLP Workshop, arXiv:2503.17456): 证明神经元级语言特定干预不足以实现跨语言迁移。注意：这是NAACL的Insights from Negative Results Workshop论文，非主会论文，影响力有限。
- SCAN (arXiv:2603.15226, Mar 2026): 用sparse transcoders做lifelong editing，在Qwen3/Llama3.1上实验，但目标是sequential stability而非跨语言传播。
- Merging Methods for MKE (arXiv:2605.13919, May 2026): 极新工作，探索向量合并方法用于12语言编辑，发现vector summation + shared covariance最稳定，但无表示级分解。
- Editing Across Languages Survey (arXiv:2505.14393): 综述确认language anisotropy和edit scalability为关键挑战。
- 调研总结: 跨语言知识编辑是一个被综述和多篇近期工作认可的开放问题，portability是公认瓶颈。SAE特征已分别被用于知识擦除（FeatureEdit）、语言身份操控（LangSAE、Chou et al.）和lifelong editing（SCAN），但**确实没有工作将SAE特征分解与跨语言知识编辑结合**——proposal的gap claim成立。然而，这一组合是两条成熟线路的"显然下一步"衔接。

【Trivial Alternative 检验】:
存在明显的更简单替代方案威胁：
(1) **直接应用LangSAE方法到编辑向量**：LangSAE已经能通过SAE特征抑制语言身份信号。将其直接用于编辑向量的语言成分去除（不需要FCE指标、不需要自适应λ），是一个成本极低的baseline。Proposal的增量价值声称在于"自适应软投影考虑了事实-语言纠缠"——但这一增量是否真正必要，取决于纯语言特征和事实特征之间的纠缠程度，而这恰恰是proposal试图验证的假设，尚无先验证据。
(2) **简单的Chou et al.式单特征操控**：既然单个SAE特征就能实现90%语言转向，直接在编辑后做语言特征转向（而非在编辑向量上做投影）可能是更简单的路径。
增量价值：Proposal的核心增量在于FCE指标引导的自适应程度控制，以及对"为什么neuron级别不够"的因果假设检验。但如果简单方案（如直接LangSAE-style suppression + ROME/MEMIT）已经能显著改善portability，则整个elaborate pipeline的价值大幅缩水。

【前提假设检验】:
核心逻辑链中有两个关键未验证假设：
(1) **"Portability bottleneck源于polysemantic entanglement"假设**：这是整篇论文的因果前提，但LU-LAFNs作者自己提出了一个竞争性解释——portability指标本身可能在测量推理能力而非可编辑的事实关联。如果portability EM低是因为这些问题需要multi-hop reasoning（编辑无法触及的能力），那么无论用多细的特征分解都不会改善结果。Proposal虽然在risk mitigation中提到了这一点并设计了A2 ablation，但这不改变核心claim的前提是未经验证的。
(2) **"SAE特征足够monosemantic来实现clean separation"假设**：Leask et al.已经证明SAE特征不是原子化的规范单位，meta-SAE可以进一步分解大特征。Proposal通过连续加权来应对，但这实质上承认了特征并非真正monosemantic——那么"比neuron更细粒度"的优势到底能带来多少实际改善？从67.9% LAFNs到64K features的粒度跃升，在portability这个具体指标上能否转化为可测量的改善，是完全开放的。

【3 维度打分】:

1. Novelty: 中 — 
组合novelty成立：经调研确认，SAE特征分解+跨语言知识编辑的交叉点确实无人占据。但这是一个"bridge combination"而非新范式——SAE用于语言操控（LangSAE, Chou et al.）、SAE用于知识编辑（FeatureEdit, SCAN, SSPU）、跨语言知识编辑（LU-LAFNs, X-KDE, LangEdit）三条线各自成熟，将它们组合是一个可预见的下一步。FCE指标和自适应λ投影是合理的工程贡献，但不构成方法论突破。核心假设"更细粒度→更好分离→更好portability"是直觉性的，审稿人的反应更可能是"I would have guessed this"而非"surprising"。类比：如果FeatureEdit已经证明features > neurons for knowledge erasure，LangSAE已经证明SAE可以去除语言信号，那将二者组合用于跨语言编辑几乎是"显然应该尝试的事情"。

2. Significance: 中 —
正面：跨语言知识编辑的portability是被综述（arXiv:2505.14393）和多篇论文（LU-LAFNs, CLM-Bench）共同确认的开放问题，所有方法EM<10的普遍失败确实需要新思路。假设检验设计（A3 falsification test）有独立的科学价值。
负面：(a) 跨语言知识编辑本身是NLP中一个相对小众的子领域；(b) 知识编辑整体仍处于研究阶段，实际落地遥远；(c) 即使positive result，提升幅度可能有限——从EM<10到EM=15-25仍然不具备实用价值；(d) 该工作绑定特定模型的pre-trained SAE（Qwen-Scope, Llama Scope），可推广性受限于SAE的可用性。

3. Related Work: 强 —
这是proposal最突出的优势。覆盖范围极为全面，四层分类清晰（直接baseline → 神经元级 → SAE编辑 → SAE干预质疑）。对adversarial evidence的引用和应对诚实且具体（Peng et al. → Arad et al.反驳；Leask et al. → 连续基处理；Farrell et al. → 软投影而非零化）。对FeatureEdit适用范围的限定（知识擦除而非事实编辑）显示了学术诚信。唯一小瑕疵：Mondal et al.被标为"NAACL 2025 InsightsNLP"，实际是NAACL的Negative Results Workshop论文，非主会，作为"independent evidence"的权重应有所调降。

【概率估计】: [22% - 32%] 中位 27%
（注：此概率假设投稿至ACL/EMNLP等NLP主会。若真的投稿CoRL 2026——一个机器人学习会议——则概率接近0%，因为完全不在scope内。）

【估计理由】:
从3维度到概率的推理：Related Work强是执行层面的优势，不拉高idea上限；Significance中等限制了ceiling（审稿人可能认为子领域太窄、practical impact不足）；**Novelty中等是主要上限限制因素**——"bridge combination"类工作在顶会的认可度取决于组合后是否产生非trivial的insight，而本proposal的核心假设"finer granularity → better separation"直觉性过强。如果positive result只是modest improvement（比如portability EM从<10升到15-25），审稿人很可能评价为"reasonable engineering contribution but limited novelty"。Proposal的falsifiability设计和dual-outcome framing可以保底（negative result也有价值），但这本身说明了idea的风险——需要用"即使失败也有价值"来对冲，侧面反映了作者对positive outcome的信心有限。上界32%的情景是：positive result显著（portability EM大幅跃升）+ 分析揭示出关于多语言表示的deep insight；下界22%的情景是：提升modest + 审稿人质疑trivial alternative。

【主要风险】:
1. **Trivial alternative威胁**：审稿人可能要求与"直接LangSAE-style suppression on edit vectors"做对比——如果这个极简baseline已经能获得大部分改善，则整个FCE + adaptive λ pipeline的增量价值被严重削弱，论文会被评为over-engineered。
2. **核心因果前提不成立的风险**：如果portability bottleneck的真正原因是metric本身测量推理能力（如LU-LAFNs作者所暗示），或者是更深层的表示对齐问题（而非polysemanticity），那么无论SAE特征分解做得多好，portability都不会显著改善——此时论文沦为一篇"negative result with analysis"，发表难度大幅增加。
```

Sources:
- [LU-LAFNs - ACL Anthology (COLING 2025)](https://aclanthology.org/2025.coling-main.385/)
- [FeatureEdit / The Knowledge Microscope (arXiv:2502.12483)](https://arxiv.org/abs/2502.12483)
- [LangSAE Editing (arXiv:2601.04768)](https://arxiv.org/abs/2601.04768)
- [Chou et al. - Causal Language Control (arXiv:2507.13410)](https://arxiv.org/abs/2507.13410)
- [Arad et al. - SAEs Are Good for Steering (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.519/)
- [Leask et al. - SAE Canonical Units (ICLR 2025)](https://arxiv.org/abs/2502.04878)
- [Mondal et al. - Language-Specific Neurons (NAACL InsightsNLP 2025)](https://aclanthology.org/2025.insights-1.6/)
- [SCAN (arXiv:2603.15226)](https://arxiv.org/pdf/2603.15226)
- [Merging Methods for MKE (arXiv:2605.13919)](https://arxiv.org/abs/2605.13919)
- [CLM-Bench (arXiv:2601.17397)](https://arxiv.org/pdf/2601.17397)
- [Editing Across Languages Survey (arXiv:2505.14393)](https://alt.qcri.org/~ndurrani/pubs/EMNLP25a.pdf)
- [X-KDE (arXiv:2502.14645)](https://arxiv.org/pdf/2502.14645)
- [SSPU (arXiv:2505.24428)](https://arxiv.org/pdf/2505.24428)
- [SpARE (arXiv:2410.15999)](https://arxiv.org/pdf/2410.15999)
- [Farrell et al. (arXiv:2410.19278)](https://arxiv.org/pdf/2410.19278)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient field research to make an informed assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- LU-LAFNs (COLING 2025, arXiv:2406.16416): 最直接的 prior work。通过 activation frequency intersection 识别 language-agnostic factual neurons (LAFNs)，在 Bi-ZsRE 上达到 77.87 avg，但所有方法（包括 LU-LAFNs 本身）portability EM < 10。该论文确实存在，proposal 对其描述准确。
- FeatureEdit / The Knowledge Microscope (ACL 2025, arXiv:2502.12483): 确认存在。首个 SAE-feature-based editing 方法，在 PrivacyParaRel 上 features 优于 neurons（~0.80 vs ~0.65 reliability）。但确如 proposal 所述，仅限单语英文的 privacy-knowledge erasure，非 factual editing 或跨语言场景。
- Arad et al. (EMNLP 2025, arXiv:2505.20063): 确认存在。区分 input features 与 output features，通过 output-score filtering 使 SAE steering 提升 2-3×，匹配 supervised methods。确实可视为对 Peng et al. 的有效回应。
- Peng et al. (arXiv:2506.23845, Jun 2025): 确认存在。论证 SAE 更适合 discovery 而非 intervention。该 proposal 对其描述准确。
- Leask et al. (ICLR 2025, arXiv:2502.04878): 确认存在。通过 meta-SAE 证明 SAE features 不是 atomic canonical units。proposal 对其描述准确。
- Mondal et al. (NAACL 2025, arXiv:2503.17456): 确认存在。在 XNLI/XQuAD 上证明 neuron-level language-specific intervention 不足以实现 cross-lingual transfer。为 proposal 的 motivation 提供了独立支撑。
- LangSAE (arXiv:2601.04768, Jan 2026): 确认存在。通过 SAE feature suppression 去除 language identity，提升多语言检索 nDCG。
- Chou et al. (arXiv:2507.13410): 确认存在。单 SAE feature 修改即可达 90% 语言 steering 成功率（Gemma-2B/9B）。
- SCAN (arXiv:2603.15226, Mar 2026): 确认存在。用 Sparse Transcoders 做 lifelong editing，但解决的是 sequential stability 问题，非跨语言迁移。
- Merging Methods for MKE (arXiv:2605.13919, May 2026): 确认存在。最新 concurrent work，探索 vector merging + shared covariance 做 12 语言编辑，但不涉及 representation-level decomposition。
- SAE-LAPE (ACL 2025), LangFIR (arXiv:2604.03532), SSPU (EMNLP 2025), SALVE (arXiv:2512.15938): 均为 SAE-based intervention/editing 的相关工作，构成本 proposal 的 building blocks。

- 调研总结: 跨语言知识编辑是 2024-2026 年的活跃研究方向，portability bottleneck (EM < 10) 是公认的 open challenge。同时 SAE-based intervention 领域正在快速发展，但尚处于"有效性争议"阶段（Peng et al. vs Arad et al.）。SAE features + cross-lingual editing 的 exact combination 确实尚未被探索，proposal 的 gap identification 是准确的。但该 gap 更多是两条已有研究线的自然交叉点，而非源于根本性的 insight 突破。

【Trivial Alternative 检验】:
存在多个成本更低的 alternative 需要认真考虑：

(1) **线性子空间投影**：AlphaEdit (ICLR 2025) 已使用 null-space constraints，LangEdit (ACL 2025 Findings) 已使用 null-space projection 做多语言 sequential editing。如果 portability 问题的本质是 edit vector 中的 language-specific component 干扰，一个简单的 PCA/SVD-based language subspace projection（不需要 SAE）能否达到类似效果？这些方法已经存在但尚未被直接用于解决 portability 问题，因此存在一个 simpler baseline gap。
(2) **直接使用 LangSAE 方法 + ROME/MEMIT**：LangSAE 已经证明 SAE-based language identity removal 有效（+21.9% nDCG），直接将 LangSAE 的 language feature suppression pipeline 嫁接到 edit vector 上，无需 FCE metric、adaptive λ 等复杂组件，是否已经能捕获大部分增益？

Proposal 的增量价值声称在于"adaptive soft projection with FCE"——即不是简单地去除所有 language features，而是根据每个 feature 的 factual causal effect 自适应保留。这个增量是否真正关键，取决于 language-specific features 和 factual features 之间的 entanglement 程度。如果 entanglement 很低（大部分 language features 的 FCE 也很低），那么 simple binary suppression 就够了，adaptive λ 的增量价值有限。如果 entanglement 很高，那么即使 adaptive λ 也可能无法有效分离——因为高 entanglement 意味着 FCE 高的 feature 正是 language-specific 的，你保留了 language component。

【前提假设检验】:
核心逻辑链条中有 **两个关键未验证假设**：

**(假设 A) Portability 失败的因果归因**：Proposal 假设 portability EM < 10 是因为 polysemantic neurons 将 factual relational structure 与 language identity 纠缠在一起。但 LU-LAFNs 原作者自己提出了另一个解释——portability metric 本身测量的是 reasoning ability（事实之间的推理链），而 parametric editing 根本无法改变 reasoning chains，只能改变 isolated facts。如果这个替代解释成立，那么无论 granularity 多细，representation-level editing 都无法改善 portability。这不是一个可以通过"做更好的实验"修补的假设缺陷——它质疑的是 idea 的根本前提。

Proposal 确实承认了这个风险并设计了 fallback（ablation A3 作为 falsification test），但这并不改变"如果假设 A 错误，idea 的核心价值主张就不成立"这个事实。负面结果虽有诊断价值，但在顶会接收标准下，"我们证明了 SAE features 也不能解决 portability"的故事线明显弱于"SAE features 解决了 portability"。

**(假设 B) SAE features 的 language-factual 可分离性**：Proposal 假设 SAE features 能将 language-specific 和 factual components 分离到不同的 feature 上。但 Leask et al. (ICLR 2025) 已证明 SAE features 不是 atomic canonical units——一个 "language" feature 可能在更高分辨率下分解为多个 sub-features，其中一些同时 encode factual 信息。如果 language 和 factual 信息在 SAE feature 层面仍然高度纠缠（只是纠缠粒度变细了），adaptive λ 的有效性就会大打折扣。Proposal 声称用 "continuous basis treatment" 应对非原子性，但这更多是一个工程 patch 而非对根本问题的解决。

【3 维度打分】:

1. Novelty: 【中】
   — 从"两条现有 research line 的交叉组合"来看，gap 确实存在，没有人做过 SAE features + cross-lingual editing 的 exact combination。但这个 gap 是一个 natural next step——FeatureEdit (ACL 2025) 证明了 SAE features > neurons for editing，LangSAE (2026) 证明了 SAE-based language feature suppression 有效，将两者结合做 cross-lingual editing 是一个几乎所有了解两篇论文的人都能想到的 extension。方法层面，adaptive soft projection with FCE 是 weighted feature suppression 的 variant，并非方法论上的范式创新。Chou et al. (arXiv:2507.13410) 已经证明了 single SAE feature 的 language steering 可行性，SCAN (arXiv:2603.15226) 已将 SAE-adjacent 方法用于 editing。总结：novelty 类型为 **combinatorial synthesis** 而非 **conceptual breakthrough**。在顶会标准下，这种 novelty 水平处于 borderline。

2. Significance: 【中】
   — 问题本身（portability bottleneck）是重要的、被公认的 open challenge（survey arXiv:2505.14393 explicitly 将其列为 key challenge）。如果方法 works，对 multilingual KE 领域确有推进。但问题在于：(a) 如果 positive result，审稿人可能会说 "This is what I'd expect given polysemanticity theory"——polysemantic neurons → 换 monosemantic features → 效果更好，逻辑链太顺畅，缺乏反直觉的 surprising element；(b) 如果 negative result，虽然有诊断价值但 impact 显著降低；(c) portability 的改善幅度可能有限（从 EM < 10 到，比如，EM ~15-20？），不一定构成 convincing breakthrough。此外，整个 claim 的 significance 高度依赖于假设 A 的正确性——而假设 A 本身未经验证。

3. Related Work: 【强】
   — Related work 覆盖极为全面，包括 4 个 tier 的分层梳理，涵盖了直接 baseline（LU-LAFNs, MEMIT, AlphaEdit, X-KDE, LangEdit）、methodological predecessors（FeatureEdit, SSPU, LangSAE, SCAN）、以及 adversarial work（Peng et al., Leask et al.）和 counter-evidence（Arad et al., Chou et al., Zhao et al.）。特别值得肯定的是，proposal 主动引入并回应了 SAE intervention skepticism，而非回避。Merging Methods for MKE (arXiv:2605.13919, May 2026) 作为 concurrent work 也被覆盖到。所有被引用的论文经调研均真实存在，描述基本准确。少数需要注意的点：FeatureEdit 的 context note（privacy erasure vs. factual editing 的区分）是诚实且恰当的。总体而言，这是该 proposal 最强的维度。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】:
Related work 维度的出色表现（强）为 proposal 提供了良好的学术基底，但 **Novelty 的 combinatorial 性质和 Significance 对未验证假设的依赖共同限制了上界**。

具体推理：
- Related Work【强】→ 确保不会因为 "miss related work" 或 "unclear positioning" 被拒，这是一个正面因素。
- Novelty【中】→ 组合型 novelty 在顶会中处于 borderline。审稿人可能评价为 "interesting engineering combination but the intellectual contribution is assembling existing pieces"。FeatureEdit + LangSAE + cross-lingual editing 的组合虽然尚无人做，但 conceptual gap 较小，任何熟悉这两条 line 的研究者都能自然想到。这是限制上界的主要因素。
- Significance【中】→ 问题重要但核心假设（假设 A：polysemantic entanglement 导致 portability 失败）未经验证，且存在替代解释（editing 根本无法传递 reasoning chains）。即使 positive result，"monosemantic > polysemantic for editing" 不够 surprising。
- 概率区间 22-33% 对应 rubric 中"有实质内核但核心发现可能 'I would have guessed this'"的定位。中位 27% 反映了 Related Work 的加分和 Novelty/Significance 的限制之间的平衡。

【主要风险】:
1. **核心假设可能根本就错**：Portability bottleneck 的真实原因可能不是 polysemantic entanglement，而是 parametric editing 的根本局限（无法传递 reasoning chains）。如果假设 A 错误，整个 idea 的核心价值主张坍塌——即使实验做得再完美，也只能产出一篇 negative result 的诊断性论文。
2. **Combinatorial novelty 不足以说服审稿人**：最核心的 methodological contribution（adaptive soft projection with FCE）本质上是 weighted feature suppression 的 variant，不是方法论范式创新。在"SAE + X"的研究已经日趋拥挤的背景下（SCAN, SSPU, SALVE, SpARE, FeatureEdit, SASFT 等均在 2025-2026 发表），审稿人可能认为"又一个 SAE application"的增量价值不够。
```

**补充说明（venue concern）**：本 proposal 的内容完全属于 NLP/计算语言学领域（多语言知识编辑），而 CoRL (Conference on Robot Learning) 是机器人学习会议。如果确实投稿 CoRL，则 topic mismatch 会导致 desk rejection 概率极高。建议确认目标会议是否为 ACL/EMNLP/NAACL/COLING 等 NLP 会议——上述概率估计基于投稿至 NLP 顶会的假设。

Sources:
- [LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons (COLING 2025)](https://arxiv.org/abs/2406.16416)
- [FeatureEdit / The Knowledge Microscope (ACL 2025)](https://arxiv.org/abs/2502.12483)
- [Arad et al.: SAEs Are Good for Steering (EMNLP 2025)](https://arxiv.org/abs/2505.20063)
- [Peng et al.: Use SAEs to Discover Unknown Concepts (2025)](https://arxiv.org/abs/2506.23845)
- [Leask et al.: SAEs Do Not Find Canonical Units (ICLR 2025)](https://arxiv.org/abs/2502.04878)
- [Mondal et al.: Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer (NAACL 2025)](https://arxiv.org/abs/2503.17456)
- [LangSAE Editing (2026)](https://arxiv.org/abs/2601.04768)
- [Chou et al.: Causal Language Control via Sparse Feature Steering](https://arxiv.org/abs/2507.13410)
- [SCAN: Sparse Circuit Anchor for Lifelong Editing (2026)](https://arxiv.org/pdf/2603.15226)
- [Merging Methods for Multilingual Knowledge Editing (2026)](https://arxiv.org/abs/2605.13919)
- [CLM-Bench (2026)](https://arxiv.org/abs/2601.17397)
- [X-KDE: Edit Once, Update Everywhere (ACL 2025 Findings)](https://arxiv.org/abs/2502.14645)
- [Editing Across Languages: Survey (2025)](https://arxiv.org/abs/2505.14393)


【原始 proposal（允许参考但不是主要依据）】:
# Beyond Neurons: SAE Feature Decomposition for Cross-Lingual Knowledge Edit Propagation

## Description
Current cross-lingual knowledge editing faces a universal portability bottleneck: not just LU-LAFNs (COLING 2025) but ALL current methods achieve near-zero portability EM (< 10) on Bi-ZsRE, with the LU-LAFNs authors themselves noting 'all methods underperform on this metric without significant difference.' We hypothesize that this bottleneck has a specific causal mechanism: polysemantic neurons entangle factual relational structure with language identity, so any neuron-level editing that removes language components inevitably corrupts relational knowledge needed for portability. This hypothesis is independently supported by Mondal et al. (NAACL 2025 InsightsNLP), who showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer even outside the editing setting.

We propose SAE-Projected Editing: using pre-trained Qwen-Scope SAEs (64K features on Qwen3-8B) and Llama Scope SAEs (128K features on Llama-3.1-8B) to decompose edit vectors into finer-grained sparse features, classify each as language-specific or language-agnostic via cross-lingual activation-probability contrasts, then apply adaptive soft projection that suppresses language-specific components proportionally to their Factual Causal Effect (FCE) — a per-feature ablation-based metric measuring how much factual recall degrades when the feature is removed. Unlike binary feature zeroing — which Farrell et al. (2024) showed is ineffective — our adaptive λ-projection preserves factual content encoded in partially-entangled features while removing pure language-identity signal.

**Engagement with SAE intervention skepticism:** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovery than intervention; however, Arad et al. (EMNLP 2025) directly rebut this by showing that output-score-based feature selection yields 2–3× improvement in SAE steering, matching supervised methods. The critique applies to naive feature selection, not SAE interventions as a paradigm. We incorporate output-score filtering into our pipeline. Chou et al. (arXiv:2507.13410) provide further feasibility evidence: modifying a single SAE feature achieves up to 90% language steering success on Gemma-2B/9B. Leask et al. (ICLR 2025) show SAE features are not atomic canonical units — larger latents decompose into sub-components. We accommodate this by: (a) treating features as a continuous weighted basis rather than binary switches, (b) using adaptive λ coefficients that handle partial feature overlap, and (c) ablating across SAE widths (16K/64K/128K) to identify task-appropriate granularity per Leask et al.'s recommendation.

**FeatureEdit context note:** The +23% reliability and 2.8× generalization gains from FeatureEdit (ACL 2025) are for knowledge erasure on the PrivacyParaRel privacy dataset using Gemma-2 models, not factual knowledge editing or cross-lingual propagation. We cite these as evidence that features outperform neurons as representation-level intervention units, but do not assume these specific gains transfer to the editing setting.

**FCE metric protocol:** For each of ~64K SAE features, we first compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success across ≥5,000 multilingual facts (computational cost: ~4 GPU-hours for forward passes). The top ~2K features by |r_pb| undergo full causal ablation: each feature is individually zeroed, and the change in factual recall probability is measured (FCE). This two-stage approach reduces the 64K × 5K evaluation matrix to a tractable 2K × 5K, requiring ~40 GPU-hours. Bootstrap confidence intervals (1000 resamples) provide uncertainty estimates for FCE values. As a validation check, we compute Spearman rank correlation between r_pb and FCE on the 2K features to verify the proxy quality.

Key contributions: (1) First application of SAE feature decomposition to cross-lingual knowledge editing, providing ~5-10× finer granularity than neuron-level LAFN identification; (2) Adaptive soft projection mechanism that explicitly accounts for factual-language feature entanglement via a concrete, causal FCE metric with a two-stage efficient computation protocol; (3) Principled engagement with SAE intervention skepticism (Peng et al., Leask et al.) through output-score filtering, continuous-basis treatment, and multi-width ablation; (4) Testable portability hypothesis: if SAE features do NOT improve portability EM over neuron-level approaches (ablation A3), this falsifies the polysemanticity-entanglement explanation and has standalone diagnostic value; (5) Reconstruction fidelity validation protocol establishing whether SAE round-trip preserves edit vector quality across dictionary sizes.

We evaluate on CLM-Bench (zh-en), Bi-ZsRE, and MzsRE across 12 languages, targeting improvements over LU-LAFNs (77.87 Bi-ZsRE avg on bloomz-7b1-mt; MzsRE results reported as per-language heatmaps rather than a single average) particularly on portability metrics. Primary baselines: LU-LAFNs, FeatureEdit (adapted cross-lingual), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit.

**Risk mitigation:** The core risk is that the portability bottleneck is NOT caused by polysemantic entanglement but by a more fundamental limitation (e.g., the portability metric itself measuring reasoning ability that editing cannot improve). We address this through: (a) explicit FCE measurement before editing to quantify the entanglement ceiling, (b) adaptive λ-projection that preserves high-FCE features, (c) reconstruction fidelity go/no-go gate, (d) ablation A3 as a direct falsification test, and (e) relational follow-up evaluation (A2) that provides a complementary portability measure independent of the Bi-ZsRE metric. If SAE features fail to improve portability, the negative result still contributes a rigorous decomposition analysis of what fraction of factual information resides in language-specific vs. language-agnostic features — valuable for the multilingual interpretability community. Fallback: hybrid approach combining SAE-projected editing for low-entanglement facts with LU-LAFNs for high-entanglement cases.

## Core Problem
Cross-lingual knowledge editing methods face two linked failures: (1) raw edit vectors reside in nearly orthogonal, language-specific subspaces (CLM-Bench), and (2) neuron-level approaches like LU-LAFNs that identify language-agnostic neurons achieve high monolingual reliability but suffer catastrophically low portability (26.43% F1, EM < 5) — a failure shared by ALL current methods (all EM < 10 on Bi-ZsRE portability), suggesting a fundamental representation-level bottleneck. We hypothesize that this bottleneck stems from polysemantic neurons entangling factual relational structure with language identity: edits that operate at neuron granularity cannot cleanly separate these components, corrupting relational knowledge during cross-lingual transfer. Can sparse autoencoder feature decomposition — which yields finer-grained, more monosemantic units — provide a cleaner separation that better preserves relational structure, and is this hypothesis even testable given recent challenges to SAE feature canonicality (Leask et al., ICLR 2025)?

## Opportunity
CLM-Bench (arXiv:2601.17397, Jan 2026) provided geometric evidence that Chinese and English edit vectors are nearly orthogonal, explaining why ROME/MEMIT fail cross-lingually (~20% reliability). LU-LAFNs (COLING 2025) achieved 77.87 avg on Bi-ZsRE by targeting language-agnostic neurons, but its neuron-level approach identifies 67.9% of neurons as LAFNs — an extremely coarse decomposition reflecting neuron polysemanticity — and ALL methods achieve near-zero portability EM (< 10 across the board), which the authors attribute to the difficulty of measuring reasoning without a reasoning process. Crucially, Mondal et al. (NAACL 2025 InsightsNLP) independently showed that neuron-level language-specific interventions are insufficient for cross-lingual transfer on XNLI/XQuAD, reinforcing the case that neuron-level decomposition is fundamentally too coarse.

Meanwhile, FeatureEdit (ACL 2025) demonstrated that SAE features outperform neurons for knowledge erasure on PrivacyParaRel (~0.80 vs ~0.65 reliability, ~0.70 vs ~0.25 generalization on Gemma-2 2B/9B) — though notably this was for privacy-knowledge erasure, not factual editing or cross-lingual propagation, so these gains may not directly transfer. LangSAE (arXiv:2601.04768) proved SAE-based language identity removal improves cross-lingual retrieval by +21.9% nDCG@20. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying a single SAE feature on Gemma-2B/9B, demonstrating that SAE-based language manipulation is feasible and precise.

However, recent work challenges SAE interventions: Peng et al. (arXiv:2506.23845) argue SAEs are better for concept discovery than acting on known concepts, finding SAE-based steering underperforms prompting/fine-tuning. Critically, Arad et al. (EMNLP 2025) rebut this: proper feature selection via output-score filtering yields 2–3× improvement in SAE steering, matching supervised methods — the issue was feature selection, not SAE interventions per se. Leask et al. (ICLR 2025) show SAE features aren't canonical atomic units — larger latents decompose into combinations — but recommend pragmatic choice of dictionary size suited to task, and our adaptive soft projection naturally accommodates non-atomicity by treating features as a continuous basis rather than binary switches.

The missing link: no work has combined SAE feature-level decomposition with cross-lingual knowledge editing. SAE features offer ~64K monosemantic units (vs. ~14K polysemantic neurons), enabling more precisely targeted language-component manipulation that may better preserve relational/factual structure — a hypothesis we propose to test directly.

## Related Work / Landscape
Cross-lingual knowledge editing is a recognized open problem: the survey (arXiv:2505.14393) identifies language anisotropy and edit scalability as key challenges. The field is structured in three tiers:

**Tier 1 — Direct multilingual editing baselines:** MEMIT/M-MEMIT apply locate-then-edit across languages (74.86 avg on Bi-ZsRE but ~20% cross-lingual reliability). AlphaEdit (ICLR 2025) uses null-space constraints. Merging Methods for MKE (arXiv:2605.13919, May 2026) explores vector merging with shared covariance for 12-language editing but without representation-level decomposition.

**Tier 2 — Neuron/representation-level multilingual editing:** LU-LAFNs (COLING 2025, arXiv:2406.16416) is the closest prior work — identifies language-agnostic factual neurons via activation frequency intersection across languages, achieving 77.87 avg on Bi-ZsRE (bloomz-7b1-mt). However, it identifies 67.9% of neurons as LAFNs (extremely coarse), and ALL methods achieve near-zero portability (EM < 10, F1 ~26-36%), which the authors acknowledge as a universal challenge rather than a method-specific failure. Mondal et al. (NAACL 2025 InsightsNLP, arXiv:2503.17456) provide independent evidence that neuron-level language-specific interventions are insufficient for cross-lingual transfer. MEMLA (arXiv:2406.11566) uses neuron masking with LoRA but doesn't leverage monosemantic features. X-KDE (ACL 2025 Findings, arXiv:2502.14645) uses instruction tuning + preference optimization (+8.19% avg improvement). LangEdit (ACL 2025 Findings, arXiv:2506.10800) applies null-space projection for multilingual sequential editing across 6 languages.

**Tier 3 — SAE-based editing and language feature work (our building blocks):** FeatureEdit from 'The Knowledge Microscope' (ACL 2025, arXiv:2502.12483) is the first SAE-feature-based model editing method — uses Gemma Scope JumpReLU SAEs to identify knowledge features and zero out specific weight positions. On the PrivacyParaRel knowledge-erasure benchmark (not factual editing), features achieve ~0.80 reliability (vs. ~0.65 for neurons) and ~0.70 generalization (vs. ~0.25), demonstrating features' advantage for representation-level interventions. However, it is monolingual English-only, targets knowledge erasure rather than cross-lingual propagation, and these gains may not directly transfer to the editing setting. SSPU (EMNLP 2025, arXiv:2505.24428) shows SAE-guided subspace projection via QR decomposition can unlearn knowledge while preserving non-target capabilities. LangSAE (arXiv:2601.04768) removes language identity from embeddings using SAE feature suppression (+21.9% nDCG@20). SAE-LAPE/LangFIR (arXiv:2604.03532) discover sparse language-specific features using activation probability contrasts. SASFT (ICLR 2026) shows SAE-guided fine-tuning preserves targeted knowledge. SpARE (NAACL 2025, arXiv:2410.15999) uses SAE-based representation engineering for knowledge selection steering but not cross-lingually. SCAN (arXiv:2603.15226, Mar 2026) uses sparse transcoders for lifelong editing on Qwen3/Llama3.1 but addresses sequential stability, not cross-lingual transfer. Farrell et al. (arXiv:2410.19278) found that zero ablation of SAE features is ineffective for knowledge unlearning — negative scaling is necessary. Chou et al. (arXiv:2507.13410) achieved up to 90% language steering success by modifying single SAE features on Gemma-2B/9B, providing direct feasibility evidence for SAE-based language manipulation.

**Tier 4 — SAE intervention skepticism and counter-evidence (critical context):** Peng et al. (arXiv:2506.23845) argue SAEs are better for discovering unknown concepts than acting on known ones, finding SAE-based steering underperforms prompting/fine-tuning. However, Arad et al. (EMNLP 2025, arXiv:2505.20063) directly rebut this: by distinguishing 'input features' (capture input patterns) from 'output features' (causally affect model behavior) and filtering by output scores, SAE steering achieves 2–3× improvement, matching supervised methods. The issue was naive feature selection, not SAE interventions as a paradigm. Zhao et al. (arXiv:2505.15038) further show denoising concept vectors via SAE improves steering 4–16%. SAE-SSV (EMNLP 2025, arXiv:2505.16188) achieves high steering success rates using supervised feature selection in sparse spaces. Leask et al. (ICLR 2025, arXiv:2502.04878) demonstrate SAE features are neither atomic nor canonical — meta-SAEs decompose latents into sub-components (e.g., 'Einstein' → 'scientist' + 'Germany' + 'famous person'), and smaller SAEs miss information captured by larger ones. They recommend pragmatic dictionary size selection rather than assuming canonicality. Our approach accommodates this by treating SAE features as a practical continuous basis with adaptive coefficients, not as binary canonical units.

**The gap:** No work combines SAE feature decomposition with cross-lingual knowledge editing. Specifically, no one has (a) used monosemantic SAE features instead of polysemantic neurons to decompose cross-lingual edit vectors, (b) tested whether finer-grained decomposition causally improves portability by preserving relational structure, or (c) engaged with the feature-selection insights from Arad et al. to ensure intervention-effective features are targeted.

## Approach
**Phase 1: Feature Classification with Output-Score Filtering (Weeks 1-2).** Leverage pre-trained SAEs — Qwen-Scope (64K features, 16× expansion) on Qwen3-8B and Llama Scope (128K features, 32× expansion) on Llama-3.1-8B — to decompose residual-stream activations at editing-critical layers (layers 12-25 for Qwen3-8B based on LU-LAFNs' LAFN distribution peaks). Classify each feature as language-specific, language-agnostic, or factual using activation-probability contrasts across Chinese, English, and 4+ additional languages (following SAE-LAPE/LangFIR methodology). Critically, following Arad et al.'s (EMNLP 2025) insight that input-pattern features and output-causal features rarely co-occur, compute output scores for all features to ensure we target features that causally affect model behavior, not merely correlational activations — this addresses the core criticism of Peng et al. For each language-specific feature f_i, compute its Factual Causal Effect (FCE): ablate f_i and measure the change in correct factual recall probability across a multilingual fact corpus of ≥5,000 facts (drawn from Bi-ZsRE + MzsRE test sets, held out from editing evaluation). FCE(f_i) = |P(correct | f_i active) - P(correct | f_i ablated)|. This produces a per-feature entanglement map. FCE is preferred over mutual information because: (a) it is causal rather than correlational, (b) it avoids the curse-of-dimensionality problems that plague MI estimation with 64K+ features (KSG estimators break down beyond ~10 dimensions), and (c) it is directly interpretable as the factual cost of removing a feature. As a computationally efficient proxy during initial screening, we also compute point-biserial correlation r_pb between feature activation magnitude and binary factual recall success, filtering to the top ~2K candidate features for full FCE ablation (reducing 64K × 5K evaluations to ~2K × 5K).

**Phase 2: SAE-Projected Editing with Adaptive Soft Projection (Weeks 3-5).** For a given ROME/MEMIT edit vector e, decompose it into the SAE feature basis: e ≈ Σ_j α_j d_j (where d_j are SAE decoder directions and α_j are coefficients from the encoder). Following Farrell et al.'s finding that binary zeroing is ineffective and Leask et al.'s evidence that features are not atomic canonical units, we apply adaptive soft projection that treats features as a continuous basis: e_proj = e - Σ_{i ∈ L_spec} λ_i · α_i · d_i, where λ_i ∈ [0, 1] is inversely proportional to FCE(f_i) — features with high factual causal effect are preserved more, pure language-identity features (low FCE, high language specificity) are fully suppressed. This formulation naturally handles Leask et al.'s non-atomicity concern: since features are weighted continuously rather than treated as binary switches, partial overlap between sub-features is accommodated through the λ gradient. The projected vector e_proj is then applied via the standard locate-then-edit pipeline.

**Phase 3: Reconstruction Fidelity Validation (Weeks 3-4, parallel).** Before full-scale editing, validate that SAE round-trip reconstruction preserves edit vector fidelity. Measure: (a) cosine similarity between original and reconstructed edit vectors, (b) monolingual edit success rate with SAE-reconstructed vectors (no language feature removal) vs. original ROME/MEMIT — this isolates reconstruction error from projection effects. If reconstruction degrades edit quality by >5%, investigate top-k sparsity adjustments or layer-specific SAE selection. Following Leask et al.'s recommendation, test multiple SAE widths (16K, 64K, 128K where available) to identify task-appropriate granularity rather than assuming larger is better. Establish a reconstruction quality threshold as a go/no-go gate.

**Phase 4: Evaluation and Ablation (Weeks 5-8).** Evaluate on CLM-Bench (1,010 zh-en pairs), Bi-ZsRE, and MzsRE (12 languages) using Qwen3-8B and Llama-3.1-8B. Primary baselines: LU-LAFNs (77.87/Bi-ZsRE on bloomz-7b1-mt — the SOTA to beat), FeatureEdit (adapted to cross-lingual setting), MEMIT, AlphaEdit, M-MEMIT, X-KDE, LangEdit. Secondary baselines: SCAN, MEMLA. Key ablations: (A1) Full zeroing vs. soft projection — measuring factual content loss, directly testing Farrell et al.'s finding in the cross-lingual setting. (A2) Relational structure preservation: for edited facts, measure whether the model correctly answers relational follow-up questions (e.g., after editing 'capital of X', test 'X is in which continent?') — this directly tests the portability hypothesis. (A3) Feature granularity: SAE features (64K/128K) vs. neuron-level LAFNs (~10K) vs. random subspace projection — if SAE features do not improve portability over neurons, this falsifies our core hypothesis. (A4) λ scheduling: fixed λ vs. FCE-adaptive λ vs. oracle λ (per-fact optimal). (A5) Layer selection: which layers' SAEs are most critical for cross-lingual transfer. (A6) SAE width: 16K vs. 64K vs. 128K features, testing Leask et al.'s prediction that task-appropriate granularity matters more than raw dictionary size. (A7) Output-score filtering (per Arad et al.): restrict projection to high-output-score features vs. all language-classified features.

## Inspiration
LU-LAFNs' universal portability failure (all methods EM < 10) revealing a fundamental representation-level bottleneck + Mondal et al.'s independent evidence that neuron-level language interventions are insufficient + FeatureEdit's demonstration that SAE features outperform neurons for knowledge erasure + LangSAE proving language features can be surgically suppressed + Chou et al.'s 90% language steering with single SAE features + CLM-Bench's geometric evidence of language-specific subspaces + SSPU's QR-decomposition subspace methodology + Arad et al.'s insight that output-score feature selection rescues SAE interventions + Farrell et al.'s finding that soft scaling outperforms zero ablation

## Key References
- LU-LAFNs: Multilingual Knowledge Editing with Language-Agnostic Factual Neurons (COLING 2025, arXiv:2406.16416) — PRIMARY BASELINE
- FeatureEdit / The Knowledge Microscope: Features as Better Analytical Lenses than Neurons (ACL 2025, arXiv:2502.12483) — METHODOLOGICAL PREDECESSOR (knowledge erasure, not editing)
- CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing (arXiv 2026, arXiv:2601.17397)
- LangSAE Editing: Improving Multilingual Information Retrieval via Post-hoc Language Identity Removal (arXiv 2026, arXiv:2601.04768)
- LangEdit: Mitigating Negative Interference in Multilingual Sequential Knowledge Editing through Null-Space Constraints (ACL 2025 Findings, arXiv:2506.10800)
- SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Knowledge Editing (arXiv 2026, arXiv:2603.15226)
- SSPU: Model Unlearning via Sparse Autoencoder Subspace Guided Projections (EMNLP 2025, arXiv:2505.24428)
- Applying Sparse Autoencoders to Unlearn Knowledge in Language Models (arXiv 2024, arXiv:2410.19278)
- X-KDE: Edit Once, Update Everywhere: A Simple Framework for Cross-Lingual Knowledge Synchronization in LLMs (ACL 2025 Findings, arXiv:2502.14645)
- MEMLA: Enhancing Multilingual Knowledge Editing with Neuron-Masked Low-Rank Adaptation (arXiv 2024, arXiv:2406.11566)
- Editing Across Languages: A Survey of Multilingual Knowledge Editing (arXiv 2025, arXiv:2505.14393)
- SAE-LAPE: Unveiling Language-Specific Features in Large Language Models via Sparse Autoencoders (ACL 2025, arXiv:2505.05111)
- LinguaLens: Towards Interpreting Linguistic Mechanisms of Large Language Models via Sparse Auto-Encoder (EMNLP 2025)
- SASFT: Sparse Autoencoder-guided Supervised Finetuning to Mitigate Unexpected Code-Switching in LLMs (ICLR 2026)
- AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models (ICLR 2025)
- SpARE: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (NAACL 2025, arXiv:2410.15999)
- LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering (arXiv 2026, arXiv:2604.03532)
- Merging Methods for Multilingual Knowledge Editing for Large Language Models: An Empirical Odyssey (arXiv 2026, arXiv:2605.13919)
- SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks (arXiv 2025, arXiv:2512.15938)
- Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models (arXiv 2026, arXiv:2605.11887)
- Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders (arXiv 2024, arXiv:2410.20526)
- Language-Specific Neurons: The Key to Multilingual Capabilities in Large Language Models (ACL 2024, arXiv:2402.16438)
- Peng et al.: Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts (arXiv 2025, arXiv:2506.23845) — ADVERSARIAL: argues SAEs underperform for interventions
- Leask et al.: Sparse Autoencoders Do Not Find Canonical Units of Analysis (ICLR 2025, arXiv:2502.04878) — ADVERSARIAL: shows features are not atomic/canonical
- Arad et al.: SAEs Are Good for Steering — If You Select the Right Features (EMNLP 2025, arXiv:2505.20063) — REBUTTAL to Peng et al.: output-score filtering yields 2-3× improvement
- Mondal et al.: Language-specific Neurons Do Not Facilitate Cross-Lingual Transfer (NAACL 2025 InsightsNLP, arXiv:2503.17456) — SUPPORTS motivation: neuron-level is insufficient
- Chou et al.: Causal Language Control in Multilingual Transformers via Sparse Feature Steering (arXiv 2025, arXiv:2507.13410) — FEASIBILITY: 90% language steering with single SAE feature
- Zhao et al.: Denoising Concept Vectors with Sparse Autoencoders for Improved Language Model Steering (arXiv 2025, arXiv:2505.15038) — SAE steering improves 4-16% with denoising
- SAE-SSV: Supervised Steering in Sparse Representation Spaces for Reliable Control of Language Models (EMNLP 2025, arXiv:2505.16188)

## Resource Estimate
- **manual**: {'gpu_hours': '450-550 (SAE feature classification + FCE ablation analysis ~120h on 1×A100 — increased due to per-feature ablation; reconstruction fidelity validation across SAE widths ~40h; editing experiments across 2 models × 3 benchmarks × 8+ baselines ~250h; ablation studies A1-A7 ~120h; analysis ~40h)', 'timeline': '10-12 weeks', 'estimated_gpu_cost': '$1,125-$1,375 (A100 at ~$2.50/hr; major savings from pre-trained Qwen-Scope and Llama Scope SAEs)'}
- **human_in_loop**: {'gpu_hours': '400-500', 'timeline': '7-9 weeks', 'claude_api_cost': '$150-$250 (code generation for SAE analysis pipeline, FCE computation, experiment orchestration)', 'estimated_gpu_cost': '$1,000-$1,250'}
- **auto_research**: {'gpu_hours': '400-500', 'timeline': '5-7 weeks', 'claude_api_cost': '$400-$550 (end-to-end experiment management, hyperparameter sweeps for λ, paper drafting)', 'estimated_gpu_cost': '$1,000-$1,250', 'speed_bottleneck': 'FCE ablation requires sequential per-feature evaluation (mitigated by r_pb pre-screening to ~2K features); sequential editing experiments per model-benchmark pair; CLM-Bench evaluation involves Chinese cultural knowledge judgment requiring human spot-checking'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b8675d97-f089-4f4f-82ea-8216fb7f24e8",
  "type": "user",
  "uuid": "a9d99aa9-b7b0-4cf7-9de8-02e56bee985f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:58:29.167Z_

```json
{
  "parentUuid": "a9d99aa9-b7b0-4cf7-9de8-02e56bee985f",
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
  "uuid": "639a510e-f1d9-4760-82dd-0ade9a9227ee",
  "timestamp": "2026-05-19T18:58:29.167Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:58:29.167Z_

```json
{
  "parentUuid": "639a510e-f1d9-4760-82dd-0ade9a9227ee",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f155fc78-a3f1-4d5f-a5bb-3f51a01490fc",
  "timestamp": "2026-05-19T18:58:29.167Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive field understanding. Let me compile t…",
  "leafUuid": "f155fc78-a3f1-4d5f-a5bb-3f51a01490fc",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual knowledge editing with SAE features",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:58:50.330Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as the Meta Judge.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 33%] 中位 27%


**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 27%
**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 33%] 中位 27%

All three reviewers are in complete agreement across every dimension—novelty, significance, and related work assessments are identical, and their probability estimates converge at exactly 27% with zero standard deviation. This remarkable alignment suggests a very consistent evaluation of the paper.

Now I'm identifying where the consensus lies. Every reviewer agrees that the novelty is incremental (combinatorial synthesis of existing approaches), the significance is moderate with an unverified core hypothesis, and the related work coverage is thorough. They also converge on several key concerns: the portability bottleneck may stem from something other than polysemantic entanglement, simpler alternatives like linear projection could achieve similar results, SAE features lack true atomicity, and there's a potential venue mismatch between CoRL and NLP-focused conferences.

The dual-outcome framing is flagged as a weakness indicator by two reviewers. Looking at the outlier observations, Reviewer 2 notes that Mondal et al. is a workshop paper rather than a main conference publication, Reviewer 1 is most explicit about the FCE metric's necessary versus sufficient condition problem, and Reviewer 3 most clearly articulates the paradox where high entanglement makes the adaptive λ approach fail anyway. Remarkably, all three reviewers converge on nearly identical probability estimates with zero standard deviation—the tightest alignment I've encountered. Now I need to assess what the proposal actually requires in terms of implementation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f155fc78-a3f1-4d5f-a5bb-3f51a01490fc",
  "isSidechain": false,
  "requestId": "req_011CbCSVtFSqEd2jzdxR2P69",
  "type": "assistant",
  "uuid": "c0a955e7-594f-4ebb-b7db-7398e7cb8de6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011iGDhUx6G6yLbpdgzT245a",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22470,
      "cache_read_input_tokens": 16560,
      "output_tokens": 2816,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2816,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 22470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22470
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

_source line 9 · 2026-05-19T18:59:43.711Z_

【阶段】: Meta Judge
【三次中位】: [27%, 27%, 27%]  std=0%
【共识维度】: 
- **Novelty = 中**（3/3）：一致认定为 "combinatorial synthesis" / "natural next step" / "bridge combination"——FeatureEdit + LangSAE + cross-lingual editing 的组合对领域内研究者来说是可预见的下一步，非 conceptual breakthrough。FCE metric 和 adaptive λ-projection 是 solid 但 incremental 的工程贡献。
- **Significance = 中**（3/3）：问题真实且被综述确认，但核心假设（polysemantic entanglement 导致 portability 瓶颈）未经验证，存在竞争解释（portability metric 测量 reasoning ability）。即使 positive result，改善幅度可能有限（EM < 10 → ~15-20），不构成 paradigm shift。
- **Related Work = 强**（3/3）：覆盖全面、四层分类清晰、对 adversarial evidence 诚实回应、引用真实准确。一致认为这是 proposal 最强维度。
- **核心假设风险**（3/3）：三位审稿人均独立识别出同一致命风险——portability bottleneck 的真实原因可能不是 polysemantic entanglement（LU-LAFNs 作者自己的替代解释：portability metric 测量的是 reasoning ability）。若此假设错误，整个技术路线的 framing 失去根基。
- **Trivial alternative 威胁**（3/3）：三位均指出未排除更简单的替代方案——线性子空间投影（AlphaEdit/LangEdit 式 null-space approach）和直接 LangSAE-style suppression + ROME/MEMIT。若简单方案获得大部分增益，整个 elaborate pipeline 的增量价值被严重削弱。
- **SAE non-atomicity 削弱核心论点**（3/3）：Leask et al. (ICLR 2025) 的发现意味着 SAE features 并非真正 monosemantic，proposal 的 continuous weighting 应对本质上是承认分离不干净，削弱了 "finer granularity = cleaner separation" 的核心论证。
- **Venue mismatch**（3/3）：一致指出 CoRL 2026 是机器人学习会议，与本 NLP/mechanistic interpretability 工作完全不匹配，若投 CoRL 概率接近 0%。

【异常维度】: 
- R1 最明确指出 FCE metric 的 necessary vs. sufficient condition 问题（ablation 只测 necessary，可能高估 "safe to remove" 的 language features）——其余两位未深入此技术细节，但不构成判决分歧
- R3 最明确展开了 "entanglement 高则 adaptive λ 也失效" 的 catch-22 悖论——逻辑成立但属于对共识风险的更细致展开，非独立异常
- R2 指出 Mondal et al. 是 NAACL Negative Results Workshop 论文（非主会），影响力应降权——合理但影响有限
- 以上均为共识维度的细化而非方向性异常，无需降权处理

【最终概率】: [22% - 32%] 中位 27%
【一致性】: 高（std = 0%，三份评审在所有 rubric 维度和概率估计上完全一致，属于极高收敛）
【综合理由】: 
三位审稿人在所有三个 rubric 维度的判决（Novelty 中 / Significance 中 / Related Work 强）和概率估计（中位均为 27%）上完全一致，std = 0%，这是异常高的收敛度。根据高一致性规则，取中位附近并缩窄区间。

最终中位 27% 的逻辑：
1. **Related Work 强**保底——不会因引用遗漏或定位不清被直接拒稿，为概率提供了 ~22% 的下限
2. **Novelty 中**是主要天花板——"bridge combination" 型工作在顶会的接受度取决于组合后是否产生非 trivial insight，而"monosemantic > polysemantic for editing"的核心 claim 直觉性过强，审稿人反应更可能是 "makes sense, this is what I'd expect" 而非 "surprising"
3. **Significance 中**进一步限制上界——核心假设未经验证且存在有力的竞争解释，即使 positive result 改善幅度可能有限
4. **双重未排除威胁**（trivial alternative + 核心假设可能为假）在三位审稿人中高度一致，不是 outlier 意见
5. 上界 32% 对应最乐观情景：positive result 显著 + 分析揭示 deep insight；下界 22% 对应：提升 modest + 审稿人质疑 trivial alternative

**关键注意**：上述概率假设投稿至合适的 NLP 顶会（ACL/EMNLP/NAACL）。若投稿 CoRL 2026，三位审稿人一致判断为 topic mismatch，实际中稿概率接近 0%（desk rejection 风险极高）。

【建议】: 不推荐（中位 27% < 36% 阈值；三方高度一致，无分歧需人工复核；但 idea 非致命缺陷，不到 KILL 级别——Related Work 出色，问题真实，主要受限于 combinatorial novelty 和核心假设未验证）

【实施评估】:
  - 计算资源: 2× A100 80GB GPU，总计 400-550 GPU-hours（约 $1,000-$1,375）。主要消耗在 FCE per-feature ablation（~120h）、双模型 × 三 benchmark × 8+ baselines 的编辑实验（~250h）、7 组 ablation（~120h）。依赖 pre-trained SAEs（Qwen-Scope 64K、Llama Scope 128K），无需自训 SAE，节省大量计算。
  - 数据需求: Bi-ZsRE、MzsRE（12 语言）、CLM-Bench（1,010 zh-en pairs）——均为公开 benchmark。FCE 计算需 ≥5,000 multilingual facts 作为探测集（从上述 benchmark 的 test split 抽取）。数据获取无障碍。
  - 人工介入: CLM-Bench 评测涉及中文文化知识判断，需人工 spot-checking；FCE 阈值和 λ 调参需研究者判断；整体人工介入量中等。
  - 训练需求: **无需模型训练**——使用 pre-trained SAEs 和 pre-trained LLMs，仅做推理和特征分析。这是一个显著优势，降低了实施门槛。
  - 新 Benchmark: **不需要**——完全基于现有公开 benchmark（CLM-Bench、Bi-ZsRE、MzsRE）。
  - 预估周期: 7-12 周（取决于自动化程度：全手动 10-12 周，human-in-loop 7-9 周，全自动 5-7 周）。瓶颈在 FCE ablation 的 sequential 特性和跨模型跨 benchmark 的实验矩阵规模。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a955e7-594f-4ebb-b7db-7398e7cb8de6",
  "isSidechain": false,
  "requestId": "req_011CbCSVtFSqEd2jzdxR2P69",
  "type": "assistant",
  "uuid": "d50da95f-217f-4338-b5bc-857f5cba6a62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011iGDhUx6G6yLbpdgzT245a",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22470,
      "cache_read_input_tokens": 16560,
      "output_tokens": 2816,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2816,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 22470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22470
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive field understanding. Let me compile t…",
  "leafUuid": "d50da95f-217f-4338-b5bc-857f5cba6a62",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-lingual knowledge editing with SAE features",
  "sessionId": "332a1257-ba0b-45b9-8bcc-d7440fbd7e12"
}
```

---
