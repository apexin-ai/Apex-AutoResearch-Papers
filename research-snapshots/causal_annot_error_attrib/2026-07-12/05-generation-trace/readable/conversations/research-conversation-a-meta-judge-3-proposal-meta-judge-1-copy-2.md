# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/864f810d-4033-4a87-9729-10ef4237166d.jsonl`
- **Structured JSON:** [`3c3a26a2ea004a78b07b.json`](../../sessions/3c/3c3a26a2ea004a78b07b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T01:55:40.870Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T01:55:40.870Z",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information from my literature search to perform a thorough, objective evaluation. Let me compose the triage assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】:\n存在至少两个成本更低的替代方案需要对比：\n\n(1) **Post-hoc probe→rewrite pipeline**: 先正常生成完整长文本，用 Han et al. 的 probes 离线检测每个 claim 的 factuality score，然后对低置信 claims 做 prompt-based 重写加入 hedging 语言。这条路线不需要任何 activation steering 技术，实现成本远低于 RaS，唯一劣势是多 pass。但\"single-pass\"在实际部署中是否真的是刚需？如果 post-hoc 方法能达到类似的 ECE 改善，RaS 的 single-pass 优势就只是工程便利而非学术贡献。\n\n(2) **Uniform confidence steering（无 probe）**: 直接对整个生成过程施加 Miao & Ungar 的 confidence direction steering（固定强度），不做 claim-level probe 监控。如果 uniform steering 的 ECE 改善与 probe-guided adaptive steering 差距不大，那么 probe-guided 的精细化设计增量价值有限。proposal 中已包含此 ablation（\"uniform steering without probe guidance\"），说明作者也意识到了这个威胁——但这恰恰说明这是一个真实风险。\n\n**增量价值**: RaS 的真正增量在于 *real-time, probe-adaptive, graded* steering——如果实验能证明 probe-guided 显著优于 uniform steering（not just statistically significant, but meaningfully better），且 single-pass 在质量上优于 post-hoc pipeline（例如 hedging 更自然、claim 边界处理更好），那增量价值成立。但这高度依赖实验结果，在 idea 层面无法确认。\n\n【前提假设检验】:\n核心逻辑链中有以下未验证假设：\n\n(1) **Accuracy-confidence orthogonality at 70B + long-form（关键假设）**: Miao & Ungar 的 orthogonality 发现仅在 7-8B QA 设置下验证（cosine < 0.04）。proposal 将其外推到 70B 长文本生成场景，这是一个非平凡的假设。70B 模型的 representation geometry 可能不同；长文本生成的 hidden state dynamics 也不同于 short-form QA。proposal 设计了 pilot experiment 来验证——这是好的实验设计，但也说明这个假设本身是脆弱的。如果 orthogonality breaks（outcome c），整个方法论需要重大调整。\n\n(2) **Offline-trained probes transfer to online streaming**: 离线训练的 factuality probes 基于完整 claim 的 hidden states。在线 generation 时，每 K=8 个 token 的 partial hidden states 是否能提供同样可靠的 factuality 信号？token-level probe accuracy 在 incomplete claims 上可能显著退化。这个假设在整个逻辑链中缺乏理论或实证支撑。\n\n(3) **Mid-sentence steering coherence**: 在句子中间激活 activation steering 假设不会破坏生成连贯性。但 mid-sentence 改变 activation trajectory 可能导致语法不通顺或语义断裂——尤其是在 70B 模型上，steering resistance 更强（proposal 引用了 3.8% ESR rate）。\"naturally hedged language\" 的质量是一个 open question。\n\n(4) **Confidence direction steering only affects expression, not content**: 基于 orthogonality 假设，steering verbalized confidence direction 不应影响 factual accuracy。但 orthogonality 是 approximate（cosine < 0.04 ≠ 0），在 cumulative steering over many tokens in long-form generation 中，即使微小的非正交分量也可能 accumulate 并影响 content quality。\n\n【3 维度打分】:\n\n1. **Novelty**: 中 — \n   核心贡献是 **组合式创新**：将 Han et al. 的 claim-level factuality probes（读）与 Miao & Ungar 的 confidence direction steering（写）组合为 single-pass framework。两个核心组件均直接借用自 prior work。Sub-sentence EMA monitoring 和 adaptive steering formula 是工程层面的设计贡献，但不构成 conceptual novelty。\n   \n   关键问题是：**这个组合是否 non-obvious？** Miao & Ungar 论文中明确指出 \"extending to open-ended generation would require rethinking how the probe target is constructed\" — 即原作者已经指明了这个方向。Han et al. 提供了 claim-level probes for long-form generation。将二者结合是一个 **predictable next step**，而非 surprising insight。与 O'Neill et al.（external observer + binary steering）的差异化也更多是 design choices（self-probing vs. external, graded vs. binary）而非 paradigm shift。\n   \n   Novelty 的正面：orthogonality-at-70B verification 作为 secondary contribution 有价值；self-probing + single-pass 的设计确实比 O'Neill et al. 更 elegant。但整体而言，剔除 surface differences 后，residual novelty = \"apply read-accuracy-steer-confidence at claim level in long-form\" ≈ 将已知方法推广到新的 setting。\n\n2. **Significance**: 中 — \n   **问题本身重要**：claim-level calibrated uncertainty in long-form generation 是一个有实际应用价值的未解决问题，用户需要知道长文本输出中哪些部分可靠、哪些需要 caveat。\n   \n   **但 expected result 不够 surprising**：如果 RaS 达到 25% ECE reduction（primary target），审稿人的反应大概率是 \"I would have guessed this works — you combined a good probe with a good steering direction, of course calibration improves.\"  即使达到 40% stretch goal，也不是 counter-intuitive。真正 surprising 的结果需要是：(a) the approach fails in unexpected ways that reveal something about representation geometry，或 (b) it works far better than component-wise predictions would suggest due to synergistic effects。proposal 没有给出为什么会出现 synergy 的理论论证。\n   \n   **推广性有限**：需要 per-model offline probe training + direction extraction；只在 standard transformer 上验证（explicitly avoids hybrid architectures like DeltaNet）；25% ECE reduction target 相比 Miao & Ungar response-level 的 70-90% reduction 是 substantial discount。\n   \n   **正面**：orthogonality scaling result 无论正负都有 mechanistic insight 价值；如果 sub-sentence steering 确实能产生自然的 hedging 语言，这在 deployment 层面有实际影响。\n\n3. **Related Work**: 强 — \n   这是整个 proposal 最强的维度。Related work 覆盖极其详尽（~30 篇近期工作），对每篇相关工作的差异化定位清晰准确。特别是对 O'Neill et al.、CARE、CAST、CLAS、AUSteer 等 concurrent work 的定位明确了 RaS 在三个轴上的区分（self-probing vs. external, graded vs. binary, claim-level vs. response-level）。gap 的论证是充分的：确实没有现有工作在 \"claim-level + calibrated + long-form + single-pass + no training\" 这个交叉点上。\n   \n   **但有一个隐忧**：gap 是通过多个约束的 **conjunction** 定义的。审稿人可能质疑：\"Why do we need all these constraints to hold simultaneously? Is single-pass really necessary? Is no-training-required truly a hard constraint?\" 这种 \"gap by conjunction\" 策略有时不够有说服力。此外，空间极度拥挤（CURE, CAG, CARE, CORAL, CLAS, CAST, O'Neill et al., AUSteer 等都是 2025-2026 的工作），到 ARR August 2026 提交时可能有更多重叠工作出现。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \n三维度综合来看：Related Work（强）确保了定位清晰和 gap 论证充分，这是这篇工作的 floor support——不会因为 \"missed related work\" 或 \"unclear positioning\" 被拒。但 **Novelty（中）是限制上界的主要因素**：组合式创新、predictable next step、核心组件均借用 prior work，这些会让审稿人写出 \"technically sound but limited novelty\" 或 \"incremental extension of Miao & Ungar to long-form setting\"。Significance（中）提供 moderate support 但不足以弥补 novelty 的不足——expected result 如果 positive 不够 surprising，不足以让审稿人 champion 这篇论文。\n\n在 EMNLP main conference（acceptance rate ~22-25%）的语境下，这篇论文处于 **borderline zone**：idea 方向正确、定位清晰，但内核不够突出。强执行 + 好结果可能把它推到 borderline accept，但 idea 本身无法 carry。中位 27% 反映了 \"略高于 random submission 的基线概率，但 idea 质量本身不足以显著提升命中率\"。\n\n【主要风险】:\n1. **\"Obvious combination\" 质疑**: 审稿人可能认为将 Han et al. probes + Miao & Ungar steering 组合是 straightforward engineering，缺乏 conceptual contribution。论文需要证明组合产生了 emergent benefits（不只是 component-wise 效果叠加），否则会被归类为 \"systems paper\" 或 \"application paper\"。\n2. **Crowded space + scooping risk**: 2025-2026 年这个方向的工作发表速度极快（CURE 4月, CAG 5月, CLAS 4月, FLAS 5月, PCNET 5月...），到 ARR August 2026 deadline 时，可能已经有其他组完成了类似的 probe→steer for long-form confidence 组合。如果 Miao & Ungar 组（Penn）自己做了 long-form extension，RaS 的 novelty 将大幅缩水。\n```\n\nSources:\n- [Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, 2026)](https://arxiv.org/abs/2603.25052)\n- [A Single Direction of Truth (O'Neill et al., 2025)](https://arxiv.org/abs/2507.23221)\n- [CLAS: Contextual Linear Activation Steering (Hsu et al., 2026)](https://arxiv.org/abs/2604.24693)\n- [AUSteer: Fine-Grained Activation Steering (ICLR 2026)](https://arxiv.org/abs/2602.04428)\n- [Simple Factuality Probes Detect Hallucinations (Han et al., EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.880/)\n- [Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025)](https://arxiv.org/abs/2503.14477)\n- [How do LLMs Compute Verbal Confidence (Kumaran et al., 2026)](https://arxiv.org/abs/2603.17839)\n- [CORAL (Miao, Cho & Ungar, 2026)](https://arxiv.org/abs/2602.06022)\n- [Activation Steering in 2026: A Practitioner's Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)\n- [CARE/ConFix: Fact-Level Calibration (SIGIR 2025)](https://dl.acm.org/doi/pdf/10.1145/3726302.3730195)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have a comprehensive picture of the landscape. Let me deliver my triage assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】:\n存在两个成本更低的 trivial alternative，构成实质威胁：\n\n(1) **Post-hoc rewriting baseline**: 先用未修改的模型生成完整的 long-form output，然后用 Han et al. 的 probes 对每个 claim 打分，最后对低置信度 claim 进行 hedging rewriting（可通过 prompting 或简单的模板替换完成）。这个流程只需两遍 pass，工程上极其简单，且 probe detection 质量与 RaS 完全相同（因为 probe 看到的是完整 claim 的 hidden states，比 RaS 的 partial-context 在线检测更可靠）。RaS 的增量价值仅在于\"single-pass 效率\"和\"steering 产生比模板替换更自然的 hedging\"——前者是工程优势而非学术贡献，后者是未经验证的假设。\n\n(2) **Sentence-level Miao & Ungar 直接应用**: 将 Miao & Ungar 的 response-level steering 直接按句子级别应用于 long-form generation，无需 sub-sentence EMA monitoring。这是一个更粗粒度但成本极低的 baseline，如果 RaS 的 ECE 改进只比这个 baseline 好少量，则整个 sub-sentence 机制的增量价值可疑。\n\n增量价值的核心论点是\"在线 single-pass 且 mid-sentence steering 能在 claim 内部就开始 hedge\"——但这一优势的实际质量（自然度、coherence）完全未经验证，且理论上 partial-context probing 可能比 complete-context probing 更 noisy。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有 4 个关键的未验证假设：\n\n(1) **Orthogonality scales to 70B + long-form**: Miao & Ungar 的 accuracy-confidence orthogonality (cosine < 0.04) 仅在 7-8B 模型的 short-form QA 上验证。Proposal 承认这一点并设计了 pilot experiment，但这意味着整个方法论的可行性建立在一个待验证的前提上。如果 cosine > 0.3（outcome c），项目退化为 8B-only paper，而 8B short-form 已被 Miao & Ungar 充分覆盖。\n\n(2) **Partial-context probing during online generation**: Han et al. 的 probes 是在完整 claim 的 hidden states 上训练和测试的。RaS 在 autoregressive generation 中对每 K=8 tokens 的 partial hidden states 做 EMA smoothed probing——probe 在只看到部分 claim 时是否还能可靠检测 factuality？这是一个重大假设跳跃，proposal 未提供任何支撑。Kumaran et al. 的\"cached at answer-adjacent positions\"和 Obeso et al. 的\"signals at span onset\"提供了间接支持，但都不是在 partial claim context 下做连续 probing 的直接证据。\n\n(3) **Mid-sentence steering coherence**: 在句子中间激活 steering vector 改变后续 token 的生成方向，可能导致语法不连贯、语义断裂或不自然的 hedging（如突然在一个 factual statement 中间插入 \"reportedly\"）。这是 activation steering 在 long-form generation 中的已知难题（Surgical Activation Steering 2026 专门讨论了这一问题），proposal 只将其标记为 \"known tradeoff\" 但没有机制保障。\n\n(4) **Continuous (soft) factuality labels 的质量**: Han et al. 使用 binary factuality labels。Proposal 提出用 \"verification confidence\" 的 soft labels 训练 probes 以获得 graded uncertainty——但 verification confidence 本身是 noisy 且 pipeline-dependent 的，其 soft scores 是否能 meaningfully 传递给 probe 进而传递给 steering magnitude 是一个弱环节。\n\n【3 维度打分】:\n  1. Novelty: 弱 — 核心贡献是将 Han et al. 的 claim-level probing 与 Miao & Ungar 的 orthogonal confidence steering 结合到一个 single-pass 框架中，加上 EMA-based sub-sentence monitoring 的工程设计。剔除 surface differences 后，这是一个\"A 方法 + B 方法应用于 C 设定\"的 combination paper。每个组件（claim-level probing、confidence steering direction、adaptive steering magnitude、online monitoring）都有直接 prior work。Sub-sentence EMA monitoring 是工程贡献而非概念创新。70B orthogonality verification 是 replication/extension study。关键测试：\"如果 RaS 确实实现了 25% ECE reduction，审稿人会说 surprising 还是 'I would have guessed this'？\"——答案几乎确定是后者。两个已经 individually work 的方法组合在一起 work，这是预期结果，不是发现。\n\n  2. Significance: 中 — 问题本身genuinely important：LLM 在 long-form generation 中的 hallucinated claims 与 factual claims 表达同等高 confidence，claim-level calibration 是一个实际需求。Gap 是真实的——确实没有现有工作在 single-pass 中做 claim-level calibrated confidence expression。但：(a) 方法仅适用于 open-weight models with hidden state access，限制了实际应用范围；(b) 25% ECE reduction 的 target 是 conservative 的，实际 impact 可能有限；(c) verbal hedging 是否真的比 post-hoc confidence annotations 对用户更有用，是一个 HCI 层面的问题，paper 不打算回答；(d) 方法不 generalize 到 API-only models。\n\n  3. Related Work: 强 — 这是 proposal 最显著的优势。覆盖了 20+ 篇高度相关的近期工作，包括 2026 年的最新进展（CLAS, FLAS, CURE, CAG, CORAL, Spherical Steering 等）。每篇工作都有清晰的差异化定位，精确指出 RaS 在每个维度上的区别。Gap statement 严谨且可验证。经我搜索确认，所引用的工作和 gap 定位是准确的——确实没有发现已有工作填补了这个 exact gap。\n\n【概率估计】: [20% - 30%] 中位 25%\n\n【估计理由】:\nRelated Work 的覆盖（强）确保了 positioning 站得住脚，不会因 novelty 定位错误而被直接拒稿。Significance（中）表明问题有价值，但方法的 expected impact 有限。然而，Novelty（弱）是硬性上界约束：这是一个 combination paper，核心发现如果 positive 是 predictable outcome，审稿人很可能写 \"natural extension of Miao & Ungar to long-form setting\" 或 \"engineering contribution rather than scientific insight\"。在 EMNLP 主会的竞争中，combination papers 通常需要 surprising empirical findings（如 negative results 或 counterintuitive scaling behavior）来弥补 conceptual novelty 的不足——但 proposal 的 expected outcome（ECE reduction）是符合直觉的。中位 25% 反映了：gap 真实 + 问题重要 + 执行方案合理，但 idea 内核缺乏惊喜，更可能被录用到 Findings 而非主会。\n\n【主要风险】:\n1. **\"Natural extension\" 评价**: 审稿人很可能将 RaS 定性为 Miao & Ungar + Han et al. 的 straightforward combination applied to a new setting，而非独立的 intellectual contribution。尤其是在 2026 年 activation steering 论文泛滥的背景下，\"probe + steer\" 的框架已成为常见 pattern。\n2. **Trivial post-hoc baseline 威胁**: 如果一个简单的 two-pass 方案（生成 → probe 检测 → 重写/标注）能达到类似甚至更好的 calibration（因为 complete-context probing 比 partial-context probing 更可靠），则 single-pass framework 的增量价值大幅缩水，核心 claim 被削弱为工程效率优势而非学术贡献。\n```\n\nSources:\n- [Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, 2026)](https://arxiv.org/abs/2603.25052)\n- [CLAS: Contextual Linear Activation Steering (Hsu et al., 2026)](https://arxiv.org/abs/2604.24693)\n- [A Single Direction of Truth (O'Neill et al., 2025)](https://arxiv.org/abs/2507.23221)\n- [CURE: Think Through Uncertainty (2026)](https://arxiv.org/abs/2604.12046)\n- [Simple Factuality Probes Detect Hallucinations (Han et al., EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.880.pdf)\n- [Activation Steering Field Guide 2026](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)\n- [Surgical Activation Steering via Generative Causal Mediation (2026)](https://arxiv.org/html/2602.16080v1)\n- [SteerConf (NeurIPS 2025)](https://arxiv.org/abs/2503.02863)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to make a thorough assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【Trivial Alternative 检验】:\n\n存在至少两个成本更低的 trivial alternative，需要认真评估增量价值：\n\n1. **Post-hoc probe-then-rewrite**: 正常生成 → 用 Han et al. 的探针对每个 claim 打分 → 对低分 claim 用 prompting 重新生成带 hedging 的版本。这是多 pass 的，但工程简单得多，不需要发现 confidence direction、不需要实时 EMA 监控。RaS 的增量价值在于「单 pass + 实时」——但审稿人可能会问：这个增量对实际应用而言值多少？long-form generation 本身就不是 latency-critical 的场景，多一轮 post-hoc correction 的代价很低。\n\n2. **直接将 Miao & Ungar 的 response-level steering 按 claim 窗口切分应用**: 即不做 sub-sentence EMA，而是每完成一个 claim（句号为界）后评估探针分数并对下一段 steering。这比 RaS 简单很多，省去了 EMA 设计和 mid-sentence 干预。RaS 的增量价值在于 sub-sentence 粒度——但这到底带来多少 calibration 提升是未知的，且 mid-sentence steering 的连贯性风险显著。\n\n**增量价值结论**: RaS 相对于 trivial alternative 的增量主要是「单 pass 实时性」和「sub-sentence 粒度」，但两者都面临\"这在实际场景中到底重要多少\"的质疑。核心 idea 并非不可替代，而是在一个已有多种解法的空间中提出了一个特定的工程实现路径。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经充分验证的环节：\n\n1. **accuracy-confidence 正交性在 70B + long-form 下成立** — 这是整个方法论的基石。Miao & Ungar 仅在 7-8B QA 上验证（cosine < 0.04）。proposal 正确地将此列为需验证的假设并设计了 pilot，但这仍是一个悬而未决的前提。值得肯定的是 proposal 对此有清醒认知，且设计了三种 outcome 的 fallback。\n\n2. **mid-sentence activation steering 不会破坏生成连贯性** — 在 sentence 中间突然 shift activation 方向，生成从高置信过渡到 hedging 语言，这在语言学上是否自然？\"X was born in [steering 激活] reportedly around 1950\" 这样的输出可能极不自然。proposal 承认了这一 tradeoff 但并未提供理论依据说明连贯性可以保持。\n\n3. **EMA over K=8 tokens 提供的信号既足够平滑又足够及时** — K=8 是 hyperparameter，但 proposal 将其作为核心设计决策。如果 factuality signal 在 claim 开始后才逐渐显现（而非 onset 即可检测），那么 K=8 的 EMA 可能滞后太多，导致 mid-claim steering 实际触发率很低，退化为「下一句才 hedge」。\n\n4. **线性 probe 的连续分数可以可靠地映射到 graded confidence** — Han et al. 的探针是 binary (factual vs. hallucinated)。将 logistic regression 的连续输出作为 calibrated confidence signal 是一个跳跃——需要验证探针的连续输出是否单调且 well-calibrated，而非仅仅二分类准确。\n\n【3 维度打分】:\n\n1. **Novelty: 中（偏弱）** — 核心贡献是将 Miao & Ungar (2026) 的 response-level confidence steering 与 Han et al. (EMNLP 2025) 的 claim-level probing 组合，并加上 sub-sentence EMA 监控。这个组合的 gap 是真实的——确实没人做过这个精确的交叉点。但问题在于：(a) 这是两篇核心先行工作指明的 obvious next step（Miao & Ungar 自己在论文中明确说 \"extending to open-ended generation would require rethinking how the probe target is constructed\"）；(b) 每个组件都是现成的（linear probe, contrastive direction extraction, CAA steering, EMA smoothing），组合方式是自然的而非非平凡的；(c) sub-sentence EMA 是工程贡献而非概念创新。与同期工作 CLAS (April 2026) 相比，RaS 的方法论创新度相当，主要差异在 application domain（confidence calibration vs. general steering）。另外，proposal 遗漏了 LoGU (ACL 2025)——它也做 claim-level uncertainty expression in long-form generation（通过 SFT+DPO），虽然 mechanism 不同，但 problem framing 高度重叠。\n\n2. **Significance: 中（偏强）** — 问题本身是重要且 timely 的：LLM 在 long-form 输出中对 hallucinated claims 过度自信是一个被广泛关注的实际问题。training-free 的解法有明确的实用价值。70B 规模的 orthogonality 验证对 mechanistic interpretability 社区有信息增量。但关键问题是 \"surprising\" test——如果结果 positive（25% ECE reduction），审稿人几乎确定会说 \"I would have guessed this\"：Miao & Ungar 在 response-level 得到 70-90%，折损到 claim-level long-form 得到 25% 是合理预期范围。如果 orthogonality 在 70B 成立，在 CLAS 已经证明 steering 在 70B 工作的背景下，也不太令人惊讶。\n\n3. **Related Work: 强** — 这是 proposal 最突出的优点。覆盖极其全面，对 ~30 篇相关工作进行了系统化分类和精确差异化定位（probe-based detection / confidence steering / conditional steering / training-based / post-hoc）。与每篇关键先行工作的区别都有具体的 axis-by-axis 比较。唯一明显遗漏是 LoGU (ACL 2025)——在 claim-level uncertainty expression for long-form generation 这个 exact problem formulation 上高度相关，虽然方法论不同（training-based），但在 positioning 上需要讨论。此外，Miao & Ungar 目前 under review at COLM 2026，尚未正式发表——这是一个引用风险。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \nNovelty 是限制上界的主要因素。核心贡献是一个 well-motivated 但 predictable 的组合——两篇关键先行工作的 natural intersection，每个组件都是现成的，组合方式是直觉上 obvious 的。审稿人很可能使用\"incremental extension\"或\"straightforward combination\"来描述。Significance 提供了 floor：问题确实重要，training-free single-pass 有实际吸引力，70B orthogonality 验证有真实信息增量。Related work 的扎实覆盖可以防止 \"insufficient differentiation\" 的拒稿理由。但中位估计被拉到 27% 而非更高，是因为即使实验完美执行，positive result 本身也不 surprising——它是先行工作的 expected scaling behavior，而非 counterintuitive finding。EMNLP main conference 对 novelty 的 bar 要求这个 idea 有一个让审稿人说 \"I didn't expect that\" 的 finding，目前看来缺乏这个元素。\n\n【主要风险】:\n1. **\"Straightforward combination\" 拒稿理由**: 最大风险。两篇核心先行工作（Miao & Ungar + Han et al.）都明确指向这个方向作为 future work，审稿人会认为组合缺乏概念创新（\"the authors essentially apply method A in the setting of method B\"），sub-sentence EMA 不足以构成 sufficient novelty delta。\n2. **Positive result 的低 surprise value**: 即使 25% ECE reduction 达成，它是 Miao & Ungar response-level 结果的 expected degraded version，审稿人会认为这验证了而非挑战了现有认知。需要一个 unexpected finding（如 orthogonality 在 70B 上出现非平凡的 breakdown pattern，或 sub-sentence steering 带来 disproportionately large gains）来突破 \"confirmatory study\" 的标签。\n```\n\nSources:\n- [Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, 2026)](https://arxiv.org/abs/2603.25052)\n- [CORAL: Correctness-Optimized Residual Activation Lens](https://arxiv.org/abs/2602.06022)\n- [LoGU: Long-form Generation with Uncertainty Expressions (ACL 2025)](https://aclanthology.org/2025.acl-long.928/)\n- [Think Through Uncertainty / CURE (2026)](https://arxiv.org/abs/2604.12046)\n- [Only Say What You Know / CAG (2026)](https://arxiv.org/html/2605.01749)\n- [SteerConf: Steering LLMs for Confidence Elicitation (NeurIPS 2025)](https://arxiv.org/abs/2503.02863)\n- [ActCab/CoDec: Activation-Based Confidence Calibration (EMNLP 2024)](https://arxiv.org/abs/2406.13230)\n- [CLAS: Contextual Linear Activation Steering](https://arxiv.org/abs/2604.24693)\n- [Miranda Muqing Miao's homepage](https://mmiao2.github.io/)\n- [Activation Steering Field Guide 2026](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation\n\n**状态**: 待审阅  \n**级别**: top-tier  \n**创建时间**: 2026-05-15T15:11:55.979393+00:00\n\n## 描述\nWe propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. A key design improvement is sub-sentence probe monitoring: rather than waiting for sentence boundaries, RaS evaluates an exponential moving average of probe scores every K tokens (K=8), enabling mid-claim steering activation when uncertainty is detected — consistent with evidence that hallucination signals emerge at span onset (Obeso et al., 2025) and that confidence representations are cached at answer-adjacent positions (Kumaran et al., 2026). Unlike O'Neill et al.'s probe→steer pipeline (which uses an external observer for binary hallucination reduction), RaS self-probes for graded confidence calibration with no second model. Unlike CARE (SIGIR 2025, which uses post-hoc iterative fact correction), RaS operates within the forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, θ − EMA_score)) relates to CAST's conditional steering (ICLR 2025) and CLAS's context-dependent steering but is driven by continuous per-claim factuality signals rather than PCA-derived condition vectors or general context sensing. The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (sanity check, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, factual precision, and steering latency distribution. We target ≥25% claim-level ECE reduction (conservatively discounted from Miao & Ungar's 70–90% response-level QA results, given additional challenges of claim-level granularity, long-form generation, and 70B scale), with ≥40% as a stretch goal, while preserving FActScore within 2%. All experiments fit within ~195 H100-hours.\n\n## 核心问题\nLLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping; O'Neill et al., July 2025 — external observer probe + binary steering), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), perform fact-level calibration via post-hoc iterative correction rather than during generation (CARE, SIGIR 2025), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), apply conditional or adaptive steering for behavioral control rather than calibrated confidence expression (CAST, ICLR 2025; Spherical Steering, ICML 2026; FLAS, 2026), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation during a single forward pass without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.\n\n## 机遇 / Why Now\nFour recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation — critically, their finding that hallucination signals emerge at the onset of hallucinated spans supports sub-sentence probe monitoring; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match in real time — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.\n\n## 方法思路\nWe propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.\n\n**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration with reduced total compute (~70h). All three outcomes produce publishable results.\n\n**Offline Stage 1 — Factuality Probe Training (~20h wall on 2× H100 for 70B; ~4h on 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.\n\n**Offline Stage 2 — Verbalized-Confidence Direction Extraction (included in Stage 1 compute; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.\n\n**Online Stage — Sub-Sentence Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead (~0.001% of the forward pass). (2) Maintain a running exponential moving average (EMA) of probe scores over a sliding window of the last K tokens (default K=8), providing smoothed uncertainty estimates that avoid triggering on single noisy tokens while enabling sub-sentence response. (3) When the EMA drops below the calibrated threshold θ, immediately activate steering — even mid-sentence. This means RaS can begin hedging within the current claim by steering subsequent tokens toward uncertainty-expressing language (e.g., generating qualifiers like 'reportedly,' 'I believe,' or reformulations for the remaining tokens in the sentence). The steering magnitude follows the adaptive formula: α = β × max(0, θ − EMA_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CAST's conditional steering (apply only when a condition is met) and CLAS's context-dependent steering, but driven by continuous per-claim factuality probe scores rather than PCA-derived category membership (CAST) or general context sensing vectors (CLAS). (4) Deactivate steering when the EMA recovers above threshold θ, indicating the model has returned to confident territory.\n\n**Steering latency analysis:** The sub-sentence trigger design means that in the best case, the probe detects uncertainty within the first few tokens of a claim (consistent with Kumaran et al.'s finding that confidence signals are cached at answer-adjacent positions and Obeso et al.'s evidence that hallucination signals are detectable at span onset), and steering activates mid-claim with ~K/2 token latency. We will empirically measure the distribution of steering activation timing relative to claim boundaries: what fraction of uncertain claims receive hedging (a) within the same sentence, (b) within K tokens, and (c) only in subsequent sentences. If probe signals rise early in claims as prior work suggests, mid-claim steering should be feasible for most uncertain claims. For claims where steering activates late, the output exhibits forward-looking uncertainty conditioning — subsequent generation is explicitly uncertainty-aware — which we acknowledge as a known tradeoff and measure empirically.\n\n**Key design choices addressing known limitations:** (a) EMA-smoothed probe scores over K-token windows avoid single-token noise while enabling sub-sentence response — a substantial improvement over sentence-boundary-only evaluation. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention and O'Neill et al.'s binary hallucination steering. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Self-probing eliminates the need for an external observer model (unlike O'Neill et al.), keeping the framework single-pass with negligible compute overhead. (f) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.\n\n**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as lightweight sanity check (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.\n\n**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), MT-Bench fluency subset (to verify generation quality preservation), and steering latency distribution (fraction of uncertain claims hedged within-sentence vs. forward-conditioned). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.\n\n**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥25% relative to unsteered baselines on both FActScore and LongFact (primary target), with ≥40% as a stretch goal — the primary target is conservative given that Miao & Ungar's response-level results (70–90% ECE reduction on QA) face additional challenges at claim-level granularity in long-form generation at 70B scale, including noisy claim boundary detection, probe signal dilution from long-context hidden states, and sub-sentence steering latency; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore; (5) ≥60% of uncertain claims receiving within-sentence hedging via sub-sentence triggers.\n\n**Comparisons (3 baselines):** (1) Unsteered baseline (cost: ~3h), (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form; cost: ~13h), (3) CURE (closest training-based method for claim-level calibration, if reproducible; cost: ~14h). We discuss but do not reimplement O'Neill et al. (external observer, different setting), CARE (post-hoc correction, different mechanism), and LoVeC (RL-based, high reproduction cost).\n\n**Ablations (3 core):** (1) Probe-only detection without steering (measures probe quality in isolation), (2) Uniform steering without probe guidance (constant steering magnitude — tests whether probe-adaptive steering outperforms naive uniform application), (3) Steering strength sensitivity (varying β, θ, and K-token window size — analyzes latency vs. signal quality tradeoff).\n\n## 研究现状\n**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.\n\n**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.\n\n**Closest prior work — observer-model probe→steer for hallucinations:** O'Neill et al. (arXiv 2507.23221, July 2025) demonstrated that a generator-agnostic observer model can detect contextual hallucinations via a linear probe on its residual stream, isolating a single transferable direction that outperforms baselines by 5–27 points across Gemma-2 models (2B–27B), and that manipulating this direction causally steers generator hallucination rates. RaS differs on three axes: (a) self-probing rather than requiring an external observer model, eliminating the overhead of a second forward pass; (b) graded confidence calibration rather than binary hallucination detection/reduction — RaS produces proportionally hedged language, not just fewer hallucinations; (c) claim-level granularity in long-form factual generation rather than span-level detection in context-grounded settings.\n\n**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.\n\n**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.\n\n**Fact-level calibration via iterative correction:** CARE (Yuan et al., SIGIR 2025; arXiv 2411.13343) proposes fact-level confidence calibration for long-form generation, decomposing responses into atomic facts, estimating per-fact confidence, and using high-confidence facts to iteratively refine low-confidence ones via ConFix. CARE addresses the same problem space (fact-level calibration in long-form outputs) but via a fundamentally different mechanism: post-hoc multi-pass correction through prompting, rather than single-pass activation steering during generation. RaS operates within the forward pass with no regeneration, targets verbal confidence expression rather than factual correction, and requires no external confidence estimation pipeline.\n\n**Conditional and adaptive steering methods:** CAST (Arditi et al., ICLR 2025) introduced conditional activation steering where a PCA-derived condition vector determines whether to apply a behavior vector via thresholded cosine similarity: h' ← h + f(sim(h, proj_c h)) · α · v. CAST's 'if condition, then steer' paradigm is conceptually related to RaS's probe-triggered steering, but CAST uses a PCA-derived condition vector for behavioral categories (e.g., content moderation), while RaS uses a data-driven factuality probe score for continuous uncertainty calibration — the probe provides graded confidence estimates, not binary category membership. Spherical Steering (You et al., arXiv 2602.08169, February 2026; ICML 2026) replaces additive steering with norm-preserving geodesic rotation and uses a vMF-based confidence gate for input-adaptive strength, achieving +10% on TruthfulQA with Llama-3.1-8B — but targets truthfulness in MCQ rather than calibrated confidence expression in long-form generation. FLAS (Jin et al., arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field enabling curved, multi-step trajectories through activation space, outperforming prompting on AxBench with Gemma-2 models — a more expressive steering mechanism than linear CAA, but tested only on small models (2B–9B) for general behavior control, not confidence calibration.\n\n**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.\n\n**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.\n\n**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation. Their finding that signals are cached before verbalization motivates sub-sentence probe monitoring.\n\n**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.\n\n**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.\n\n**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.\n\n**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.\n\n**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.\n\n**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. O'Neill et al.'s probe→steer pipeline is closest structurally but uses an external observer for binary hallucination reduction rather than self-probing for graded confidence calibration. CARE addresses fact-level calibration in long-form outputs but via post-hoc correction rather than real-time activation steering. CAST provides conditional steering but for behavioral categories, not continuous confidence calibration. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.\n\n## 目标 Venue\n- AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY\n- ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)\n- ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)\n\n## 关键参考\n- Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation\n- A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations (O'Neill et al., arXiv 2507.23221, July 2025) — closest probe→steer pipeline: external observer linear probe detects and steers hallucinations across Gemma-2 2B–27B; differs from RaS in using external observer (vs. self-probing), binary hallucination steering (vs. graded confidence calibration), and context-grounded settings (vs. long-form factual generation)\n- Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions\n- Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only\n- Fact-Level Calibration and Correction for Long-Form Generations [CARE/ConFix] (Yuan et al., SIGIR 2025; arXiv 2411.13343) — fact-level confidence calibration + iterative correction via high-confidence facts refining low-confidence ones; same problem space but fundamentally different mechanism (post-hoc multi-pass correction vs. single-pass activation steering)\n- Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA\n- Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness\n- Programming Refusal with Conditional Activation Steering [CAST] (Arditi et al., ICLR 2025) — conditional steering via PCA-derived condition vectors with thresholded activation; conceptually related 'if condition, then steer' paradigm, but targets behavioral categories rather than continuous confidence calibration\n- Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., arXiv 2602.08169, February 2026; ICML 2026) — norm-preserving geodesic rotation with vMF confidence gating; +10% on TruthfulQA with Llama-3.1-8B; targets truthfulness MCQ, not calibrated confidence in long-form\n- Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention [FLAS] (Jin et al., arXiv 2605.05892, May 2026) — learned concept-conditioned velocity field for curved activation trajectories; more expressive than linear CAA but tested on Gemma-2 2B–9B for general behavior control\n- Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality\n- Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale\n- How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions; supports feasibility of sub-sentence probe monitoring\n- Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based\n- Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design\n- Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern\n- Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models\n- SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration\n- Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control\n- Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation; evidence that hallucination signals are detectable at span onset\n- Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention\n- Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state\n- Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning\n- Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation\n- Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs\n- Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers\n- When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)\n- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level\n- FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)\n- Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)\n- Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)\n\n## 资源估算\n### auto_research\n- **claude_api_cost**: $200-400 (~3000-6000 Opus turns)\n- **estimated_gpu_cost**: $490-680\n- **gpu_hours**: ~195h H100 80GB (agent explores probe architectures, layer selections, K-window sizes, steering schedules on 70B primary model with 8B sanity checks, plus evaluation)\n- **gpu_utilization**: ~80-90% — continuous experiment pipeline with minimal idle\n- **risk_note**: Without human judgment, agent may over-optimize probe thresholds and K-window sizes on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness (mid-sentence steering coherence requires human evaluation), and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)\n- **speed_bottleneck**: Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck\n- **team**: 0 researchers (initial setup + final review only)\n- **timeline**: 7-10 days with 2× H100 80GB\n\n### human_in_loop\n- **claude_api_cost**: $100-200 (~1500-3000 Opus turns)\n- **estimated_gpu_cost**: $425-595\n- **gpu_hours**: ~170h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)\n- **gpu_utilization**: ~50-65% — agent queues experiments between human check-ins\n- **risk_note**: Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~70h H100. Secondary risk: whether sub-sentence probe-guided steering produces natural hedging at 70B or creates incoherent mid-sentence shifts — qualitative human assessment of hedging naturalness across K-token window sizes is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering.\n- **team**: 1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation\n- **timeline**: 3-4 weeks\n\n### manual\n- **estimated_gpu_cost**: $490-680 (at ~$2.50-3.50/hr H100 80GB spot)\n- **gpu_hours**: ~195h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~24h [20h 70B on 2×H100, 4h 8B on 1×H100], Llama 3.1-70B evaluation on FActScore + LongFact ~85h [2×H100], Llama 3.1-8B sanity check ~12h [1×H100], baseline comparisons ~30h [unsteered ~3h, Han et al. ~13h, CURE ~14h], core ablations ×3 ~25h, debugging/rerun buffer ~11h)\n- **gpu_utilization**: ~25-35% effective — GPU idles during code development, pipeline debugging, and results analysis\n- **team**: 1-2 researchers with mechanistic interpretability and activation steering experience\n- **timeline**: 5-6 weeks (1 researcher full-time)\n\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T01:55:40.876Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T01:55:40.876Z",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T01:55:40.892Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information from my literature search to perform a thorough, objective evaluation. Let me compose the triage assessment.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:
存在至少两个成本更低的替代方案需要对比：

(1) **Post-hoc probe→rewrite pipeline**: 先正常生成完整长文本，用 Han et al. 的 probes 离线检测每个 claim 的 factuality score，然后对低置信 claims 做 prompt-based 重写加入 hedging 语言。这条路线不需要任何 activation steering 技术，实现成本远低于 RaS，唯一劣势是多 pass。但"single-pass"在实际部署中是否真的是刚需？如果 post-hoc 方法能达到类似的 ECE 改善，RaS 的 single-pass 优势就只是工程便利而非学术贡献。

(2) **Uniform confidence steering（无 probe）**: 直接对整个生成过程施加 Miao & Ungar 的 confidence direction steering（固定强度），不做 claim-level probe 监控。如果 uniform steering 的 ECE 改善与 probe-guided adaptive steering 差距不大，那么 probe-guided 的精细化设计增量价值有限。proposal 中已包含此 ablation（"uniform steering without probe guidance"），说明作者也意识到了这个威胁——但这恰恰说明这是一个真实风险。

**增量价值**: RaS 的真正增量在于 *real-time, probe-adaptive, graded* steering——如果实验能证明 probe-guided 显著优于 uniform steering（not just statistically significant, but meaningfully better），且 single-pass 在质量上优于 post-hoc pipeline（例如 hedging 更自然、claim 边界处理更好），那增量价值成立。但这高度依赖实验结果，在 idea 层面无法确认。

【前提假设检验】:
核心逻辑链中有以下未验证假设：

(1) **Accuracy-confidence orthogonality at 70B + long-form（关键假设）**: Miao & Ungar 的 orthogonality 发现仅在 7-8B QA 设置下验证（cosine < 0.04）。proposal 将其外推到 70B 长文本生成场景，这是一个非平凡的假设。70B 模型的 representation geometry 可能不同；长文本生成的 hidden state dynamics 也不同于 short-form QA。proposal 设计了 pilot experiment 来验证——这是好的实验设计，但也说明这个假设本身是脆弱的。如果 orthogonality breaks（outcome c），整个方法论需要重大调整。

(2) **Offline-trained probes transfer to online streaming**: 离线训练的 factuality probes 基于完整 claim 的 hidden states。在线 generation 时，每 K=8 个 token 的 partial hidden states 是否能提供同样可靠的 factuality 信号？token-level probe accuracy 在 incomplete claims 上可能显著退化。这个假设在整个逻辑链中缺乏理论或实证支撑。

(3) **Mid-sentence steering coherence**: 在句子中间激活 activation steering 假设不会破坏生成连贯性。但 mid-sentence 改变 activation trajectory 可能导致语法不通顺或语义断裂——尤其是在 70B 模型上，steering resistance 更强（proposal 引用了 3.8% ESR rate）。"naturally hedged language" 的质量是一个 open question。

(4) **Confidence direction steering only affects expression, not content**: 基于 orthogonality 假设，steering verbalized confidence direction 不应影响 factual accuracy。但 orthogonality 是 approximate（cosine < 0.04 ≠ 0），在 cumulative steering over many tokens in long-form generation 中，即使微小的非正交分量也可能 accumulate 并影响 content quality。

【3 维度打分】:

1. **Novelty**: 中 — 
   核心贡献是 **组合式创新**：将 Han et al. 的 claim-level factuality probes（读）与 Miao & Ungar 的 confidence direction steering（写）组合为 single-pass framework。两个核心组件均直接借用自 prior work。Sub-sentence EMA monitoring 和 adaptive steering formula 是工程层面的设计贡献，但不构成 conceptual novelty。
   
   关键问题是：**这个组合是否 non-obvious？** Miao & Ungar 论文中明确指出 "extending to open-ended generation would require rethinking how the probe target is constructed" — 即原作者已经指明了这个方向。Han et al. 提供了 claim-level probes for long-form generation。将二者结合是一个 **predictable next step**，而非 surprising insight。与 O'Neill et al.（external observer + binary steering）的差异化也更多是 design choices（self-probing vs. external, graded vs. binary）而非 paradigm shift。
   
   Novelty 的正面：orthogonality-at-70B verification 作为 secondary contribution 有价值；self-probing + single-pass 的设计确实比 O'Neill et al. 更 elegant。但整体而言，剔除 surface differences 后，residual novelty = "apply read-accuracy-steer-confidence at claim level in long-form" ≈ 将已知方法推广到新的 setting。

2. **Significance**: 中 — 
   **问题本身重要**：claim-level calibrated uncertainty in long-form generation 是一个有实际应用价值的未解决问题，用户需要知道长文本输出中哪些部分可靠、哪些需要 caveat。
   
   **但 expected result 不够 surprising**：如果 RaS 达到 25% ECE reduction（primary target），审稿人的反应大概率是 "I would have guessed this works — you combined a good probe with a good steering direction, of course calibration improves."  即使达到 40% stretch goal，也不是 counter-intuitive。真正 surprising 的结果需要是：(a) the approach fails in unexpected ways that reveal something about representation geometry，或 (b) it works far better than component-wise predictions would suggest due to synergistic effects。proposal 没有给出为什么会出现 synergy 的理论论证。
   
   **推广性有限**：需要 per-model offline probe training + direction extraction；只在 standard transformer 上验证（explicitly avoids hybrid architectures like DeltaNet）；25% ECE reduction target 相比 Miao & Ungar response-level 的 70-90% reduction 是 substantial discount。
   
   **正面**：orthogonality scaling result 无论正负都有 mechanistic insight 价值；如果 sub-sentence steering 确实能产生自然的 hedging 语言，这在 deployment 层面有实际影响。

3. **Related Work**: 强 — 
   这是整个 proposal 最强的维度。Related work 覆盖极其详尽（~30 篇近期工作），对每篇相关工作的差异化定位清晰准确。特别是对 O'Neill et al.、CARE、CAST、CLAS、AUSteer 等 concurrent work 的定位明确了 RaS 在三个轴上的区分（self-probing vs. external, graded vs. binary, claim-level vs. response-level）。gap 的论证是充分的：确实没有现有工作在 "claim-level + calibrated + long-form + single-pass + no training" 这个交叉点上。
   
   **但有一个隐忧**：gap 是通过多个约束的 **conjunction** 定义的。审稿人可能质疑："Why do we need all these constraints to hold simultaneously? Is single-pass really necessary? Is no-training-required truly a hard constraint?" 这种 "gap by conjunction" 策略有时不够有说服力。此外，空间极度拥挤（CURE, CAG, CARE, CORAL, CLAS, CAST, O'Neill et al., AUSteer 等都是 2025-2026 的工作），到 ARR August 2026 提交时可能有更多重叠工作出现。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
三维度综合来看：Related Work（强）确保了定位清晰和 gap 论证充分，这是这篇工作的 floor support——不会因为 "missed related work" 或 "unclear positioning" 被拒。但 **Novelty（中）是限制上界的主要因素**：组合式创新、predictable next step、核心组件均借用 prior work，这些会让审稿人写出 "technically sound but limited novelty" 或 "incremental extension of Miao & Ungar to long-form setting"。Significance（中）提供 moderate support 但不足以弥补 novelty 的不足——expected result 如果 positive 不够 surprising，不足以让审稿人 champion 这篇论文。

在 EMNLP main conference（acceptance rate ~22-25%）的语境下，这篇论文处于 **borderline zone**：idea 方向正确、定位清晰，但内核不够突出。强执行 + 好结果可能把它推到 borderline accept，但 idea 本身无法 carry。中位 27% 反映了 "略高于 random submission 的基线概率，但 idea 质量本身不足以显著提升命中率"。

【主要风险】:
1. **"Obvious combination" 质疑**: 审稿人可能认为将 Han et al. probes + Miao & Ungar steering 组合是 straightforward engineering，缺乏 conceptual contribution。论文需要证明组合产生了 emergent benefits（不只是 component-wise 效果叠加），否则会被归类为 "systems paper" 或 "application paper"。
2. **Crowded space + scooping risk**: 2025-2026 年这个方向的工作发表速度极快（CURE 4月, CAG 5月, CLAS 4月, FLAS 5月, PCNET 5月...），到 ARR August 2026 deadline 时，可能已经有其他组完成了类似的 probe→steer for long-form confidence 组合。如果 Miao & Ungar 组（Penn）自己做了 long-form extension，RaS 的 novelty 将大幅缩水。
```

Sources:
- [Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, 2026)](https://arxiv.org/abs/2603.25052)
- [A Single Direction of Truth (O'Neill et al., 2025)](https://arxiv.org/abs/2507.23221)
- [CLAS: Contextual Linear Activation Steering (Hsu et al., 2026)](https://arxiv.org/abs/2604.24693)
- [AUSteer: Fine-Grained Activation Steering (ICLR 2026)](https://arxiv.org/abs/2602.04428)
- [Simple Factuality Probes Detect Hallucinations (Han et al., EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.880/)
- [Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025)](https://arxiv.org/abs/2503.14477)
- [How do LLMs Compute Verbal Confidence (Kumaran et al., 2026)](https://arxiv.org/abs/2603.17839)
- [CORAL (Miao, Cho & Ungar, 2026)](https://arxiv.org/abs/2602.06022)
- [Activation Steering in 2026: A Practitioner's Field Guide](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)
- [CARE/ConFix: Fact-Level Calibration (SIGIR 2025)](https://dl.acm.org/doi/pdf/10.1145/3726302.3730195)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have a comprehensive picture of the landscape. Let me deliver my triage assessment.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:
存在两个成本更低的 trivial alternative，构成实质威胁：

(1) **Post-hoc rewriting baseline**: 先用未修改的模型生成完整的 long-form output，然后用 Han et al. 的 probes 对每个 claim 打分，最后对低置信度 claim 进行 hedging rewriting（可通过 prompting 或简单的模板替换完成）。这个流程只需两遍 pass，工程上极其简单，且 probe detection 质量与 RaS 完全相同（因为 probe 看到的是完整 claim 的 hidden states，比 RaS 的 partial-context 在线检测更可靠）。RaS 的增量价值仅在于"single-pass 效率"和"steering 产生比模板替换更自然的 hedging"——前者是工程优势而非学术贡献，后者是未经验证的假设。

(2) **Sentence-level Miao & Ungar 直接应用**: 将 Miao & Ungar 的 response-level steering 直接按句子级别应用于 long-form generation，无需 sub-sentence EMA monitoring。这是一个更粗粒度但成本极低的 baseline，如果 RaS 的 ECE 改进只比这个 baseline 好少量，则整个 sub-sentence 机制的增量价值可疑。

增量价值的核心论点是"在线 single-pass 且 mid-sentence steering 能在 claim 内部就开始 hedge"——但这一优势的实际质量（自然度、coherence）完全未经验证，且理论上 partial-context probing 可能比 complete-context probing 更 noisy。

【前提假设检验】:
核心 claim 的逻辑链条中有 4 个关键的未验证假设：

(1) **Orthogonality scales to 70B + long-form**: Miao & Ungar 的 accuracy-confidence orthogonality (cosine < 0.04) 仅在 7-8B 模型的 short-form QA 上验证。Proposal 承认这一点并设计了 pilot experiment，但这意味着整个方法论的可行性建立在一个待验证的前提上。如果 cosine > 0.3（outcome c），项目退化为 8B-only paper，而 8B short-form 已被 Miao & Ungar 充分覆盖。

(2) **Partial-context probing during online generation**: Han et al. 的 probes 是在完整 claim 的 hidden states 上训练和测试的。RaS 在 autoregressive generation 中对每 K=8 tokens 的 partial hidden states 做 EMA smoothed probing——probe 在只看到部分 claim 时是否还能可靠检测 factuality？这是一个重大假设跳跃，proposal 未提供任何支撑。Kumaran et al. 的"cached at answer-adjacent positions"和 Obeso et al. 的"signals at span onset"提供了间接支持，但都不是在 partial claim context 下做连续 probing 的直接证据。

(3) **Mid-sentence steering coherence**: 在句子中间激活 steering vector 改变后续 token 的生成方向，可能导致语法不连贯、语义断裂或不自然的 hedging（如突然在一个 factual statement 中间插入 "reportedly"）。这是 activation steering 在 long-form generation 中的已知难题（Surgical Activation Steering 2026 专门讨论了这一问题），proposal 只将其标记为 "known tradeoff" 但没有机制保障。

(4) **Continuous (soft) factuality labels 的质量**: Han et al. 使用 binary factuality labels。Proposal 提出用 "verification confidence" 的 soft labels 训练 probes 以获得 graded uncertainty——但 verification confidence 本身是 noisy 且 pipeline-dependent 的，其 soft scores 是否能 meaningfully 传递给 probe 进而传递给 steering magnitude 是一个弱环节。

【3 维度打分】:
  1. Novelty: 弱 — 核心贡献是将 Han et al. 的 claim-level probing 与 Miao & Ungar 的 orthogonal confidence steering 结合到一个 single-pass 框架中，加上 EMA-based sub-sentence monitoring 的工程设计。剔除 surface differences 后，这是一个"A 方法 + B 方法应用于 C 设定"的 combination paper。每个组件（claim-level probing、confidence steering direction、adaptive steering magnitude、online monitoring）都有直接 prior work。Sub-sentence EMA monitoring 是工程贡献而非概念创新。70B orthogonality verification 是 replication/extension study。关键测试："如果 RaS 确实实现了 25% ECE reduction，审稿人会说 surprising 还是 'I would have guessed this'？"——答案几乎确定是后者。两个已经 individually work 的方法组合在一起 work，这是预期结果，不是发现。

  2. Significance: 中 — 问题本身genuinely important：LLM 在 long-form generation 中的 hallucinated claims 与 factual claims 表达同等高 confidence，claim-level calibration 是一个实际需求。Gap 是真实的——确实没有现有工作在 single-pass 中做 claim-level calibrated confidence expression。但：(a) 方法仅适用于 open-weight models with hidden state access，限制了实际应用范围；(b) 25% ECE reduction 的 target 是 conservative 的，实际 impact 可能有限；(c) verbal hedging 是否真的比 post-hoc confidence annotations 对用户更有用，是一个 HCI 层面的问题，paper 不打算回答；(d) 方法不 generalize 到 API-only models。

  3. Related Work: 强 — 这是 proposal 最显著的优势。覆盖了 20+ 篇高度相关的近期工作，包括 2026 年的最新进展（CLAS, FLAS, CURE, CAG, CORAL, Spherical Steering 等）。每篇工作都有清晰的差异化定位，精确指出 RaS 在每个维度上的区别。Gap statement 严谨且可验证。经我搜索确认，所引用的工作和 gap 定位是准确的——确实没有发现已有工作填补了这个 exact gap。

【概率估计】: [20% - 30%] 中位 25%

【估计理由】:
Related Work 的覆盖（强）确保了 positioning 站得住脚，不会因 novelty 定位错误而被直接拒稿。Significance（中）表明问题有价值，但方法的 expected impact 有限。然而，Novelty（弱）是硬性上界约束：这是一个 combination paper，核心发现如果 positive 是 predictable outcome，审稿人很可能写 "natural extension of Miao & Ungar to long-form setting" 或 "engineering contribution rather than scientific insight"。在 EMNLP 主会的竞争中，combination papers 通常需要 surprising empirical findings（如 negative results 或 counterintuitive scaling behavior）来弥补 conceptual novelty 的不足——但 proposal 的 expected outcome（ECE reduction）是符合直觉的。中位 25% 反映了：gap 真实 + 问题重要 + 执行方案合理，但 idea 内核缺乏惊喜，更可能被录用到 Findings 而非主会。

【主要风险】:
1. **"Natural extension" 评价**: 审稿人很可能将 RaS 定性为 Miao & Ungar + Han et al. 的 straightforward combination applied to a new setting，而非独立的 intellectual contribution。尤其是在 2026 年 activation steering 论文泛滥的背景下，"probe + steer" 的框架已成为常见 pattern。
2. **Trivial post-hoc baseline 威胁**: 如果一个简单的 two-pass 方案（生成 → probe 检测 → 重写/标注）能达到类似甚至更好的 calibration（因为 complete-context probing 比 partial-context probing 更可靠），则 single-pass framework 的增量价值大幅缩水，核心 claim 被削弱为工程效率优势而非学术贡献。
```

Sources:
- [Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, 2026)](https://arxiv.org/abs/2603.25052)
- [CLAS: Contextual Linear Activation Steering (Hsu et al., 2026)](https://arxiv.org/abs/2604.24693)
- [A Single Direction of Truth (O'Neill et al., 2025)](https://arxiv.org/abs/2507.23221)
- [CURE: Think Through Uncertainty (2026)](https://arxiv.org/abs/2604.12046)
- [Simple Factuality Probes Detect Hallucinations (Han et al., EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.880.pdf)
- [Activation Steering Field Guide 2026](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)
- [Surgical Activation Steering via Generative Causal Mediation (2026)](https://arxiv.org/html/2602.16080v1)
- [SteerConf (NeurIPS 2025)](https://arxiv.org/abs/2503.02863)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to make a thorough assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【Trivial Alternative 检验】:

存在至少两个成本更低的 trivial alternative，需要认真评估增量价值：

1. **Post-hoc probe-then-rewrite**: 正常生成 → 用 Han et al. 的探针对每个 claim 打分 → 对低分 claim 用 prompting 重新生成带 hedging 的版本。这是多 pass 的，但工程简单得多，不需要发现 confidence direction、不需要实时 EMA 监控。RaS 的增量价值在于「单 pass + 实时」——但审稿人可能会问：这个增量对实际应用而言值多少？long-form generation 本身就不是 latency-critical 的场景，多一轮 post-hoc correction 的代价很低。

2. **直接将 Miao & Ungar 的 response-level steering 按 claim 窗口切分应用**: 即不做 sub-sentence EMA，而是每完成一个 claim（句号为界）后评估探针分数并对下一段 steering。这比 RaS 简单很多，省去了 EMA 设计和 mid-sentence 干预。RaS 的增量价值在于 sub-sentence 粒度——但这到底带来多少 calibration 提升是未知的，且 mid-sentence steering 的连贯性风险显著。

**增量价值结论**: RaS 相对于 trivial alternative 的增量主要是「单 pass 实时性」和「sub-sentence 粒度」，但两者都面临"这在实际场景中到底重要多少"的质疑。核心 idea 并非不可替代，而是在一个已有多种解法的空间中提出了一个特定的工程实现路径。

【前提假设检验】:

核心 claim 的逻辑链中有以下未经充分验证的环节：

1. **accuracy-confidence 正交性在 70B + long-form 下成立** — 这是整个方法论的基石。Miao & Ungar 仅在 7-8B QA 上验证（cosine < 0.04）。proposal 正确地将此列为需验证的假设并设计了 pilot，但这仍是一个悬而未决的前提。值得肯定的是 proposal 对此有清醒认知，且设计了三种 outcome 的 fallback。

2. **mid-sentence activation steering 不会破坏生成连贯性** — 在 sentence 中间突然 shift activation 方向，生成从高置信过渡到 hedging 语言，这在语言学上是否自然？"X was born in [steering 激活] reportedly around 1950" 这样的输出可能极不自然。proposal 承认了这一 tradeoff 但并未提供理论依据说明连贯性可以保持。

3. **EMA over K=8 tokens 提供的信号既足够平滑又足够及时** — K=8 是 hyperparameter，但 proposal 将其作为核心设计决策。如果 factuality signal 在 claim 开始后才逐渐显现（而非 onset 即可检测），那么 K=8 的 EMA 可能滞后太多，导致 mid-claim steering 实际触发率很低，退化为「下一句才 hedge」。

4. **线性 probe 的连续分数可以可靠地映射到 graded confidence** — Han et al. 的探针是 binary (factual vs. hallucinated)。将 logistic regression 的连续输出作为 calibrated confidence signal 是一个跳跃——需要验证探针的连续输出是否单调且 well-calibrated，而非仅仅二分类准确。

【3 维度打分】:

1. **Novelty: 中（偏弱）** — 核心贡献是将 Miao & Ungar (2026) 的 response-level confidence steering 与 Han et al. (EMNLP 2025) 的 claim-level probing 组合，并加上 sub-sentence EMA 监控。这个组合的 gap 是真实的——确实没人做过这个精确的交叉点。但问题在于：(a) 这是两篇核心先行工作指明的 obvious next step（Miao & Ungar 自己在论文中明确说 "extending to open-ended generation would require rethinking how the probe target is constructed"）；(b) 每个组件都是现成的（linear probe, contrastive direction extraction, CAA steering, EMA smoothing），组合方式是自然的而非非平凡的；(c) sub-sentence EMA 是工程贡献而非概念创新。与同期工作 CLAS (April 2026) 相比，RaS 的方法论创新度相当，主要差异在 application domain（confidence calibration vs. general steering）。另外，proposal 遗漏了 LoGU (ACL 2025)——它也做 claim-level uncertainty expression in long-form generation（通过 SFT+DPO），虽然 mechanism 不同，但 problem framing 高度重叠。

2. **Significance: 中（偏强）** — 问题本身是重要且 timely 的：LLM 在 long-form 输出中对 hallucinated claims 过度自信是一个被广泛关注的实际问题。training-free 的解法有明确的实用价值。70B 规模的 orthogonality 验证对 mechanistic interpretability 社区有信息增量。但关键问题是 "surprising" test——如果结果 positive（25% ECE reduction），审稿人几乎确定会说 "I would have guessed this"：Miao & Ungar 在 response-level 得到 70-90%，折损到 claim-level long-form 得到 25% 是合理预期范围。如果 orthogonality 在 70B 成立，在 CLAS 已经证明 steering 在 70B 工作的背景下，也不太令人惊讶。

3. **Related Work: 强** — 这是 proposal 最突出的优点。覆盖极其全面，对 ~30 篇相关工作进行了系统化分类和精确差异化定位（probe-based detection / confidence steering / conditional steering / training-based / post-hoc）。与每篇关键先行工作的区别都有具体的 axis-by-axis 比较。唯一明显遗漏是 LoGU (ACL 2025)——在 claim-level uncertainty expression for long-form generation 这个 exact problem formulation 上高度相关，虽然方法论不同（training-based），但在 positioning 上需要讨论。此外，Miao & Ungar 目前 under review at COLM 2026，尚未正式发表——这是一个引用风险。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Novelty 是限制上界的主要因素。核心贡献是一个 well-motivated 但 predictable 的组合——两篇关键先行工作的 natural intersection，每个组件都是现成的，组合方式是直觉上 obvious 的。审稿人很可能使用"incremental extension"或"straightforward combination"来描述。Significance 提供了 floor：问题确实重要，training-free single-pass 有实际吸引力，70B orthogonality 验证有真实信息增量。Related work 的扎实覆盖可以防止 "insufficient differentiation" 的拒稿理由。但中位估计被拉到 27% 而非更高，是因为即使实验完美执行，positive result 本身也不 surprising——它是先行工作的 expected scaling behavior，而非 counterintuitive finding。EMNLP main conference 对 novelty 的 bar 要求这个 idea 有一个让审稿人说 "I didn't expect that" 的 finding，目前看来缺乏这个元素。

【主要风险】:
1. **"Straightforward combination" 拒稿理由**: 最大风险。两篇核心先行工作（Miao & Ungar + Han et al.）都明确指向这个方向作为 future work，审稿人会认为组合缺乏概念创新（"the authors essentially apply method A in the setting of method B"），sub-sentence EMA 不足以构成 sufficient novelty delta。
2. **Positive result 的低 surprise value**: 即使 25% ECE reduction 达成，它是 Miao & Ungar response-level 结果的 expected degraded version，审稿人会认为这验证了而非挑战了现有认知。需要一个 unexpected finding（如 orthogonality 在 70B 上出现非平凡的 breakdown pattern，或 sub-sentence steering 带来 disproportionately large gains）来突破 "confirmatory study" 的标签。
```

Sources:
- [Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, 2026)](https://arxiv.org/abs/2603.25052)
- [CORAL: Correctness-Optimized Residual Activation Lens](https://arxiv.org/abs/2602.06022)
- [LoGU: Long-form Generation with Uncertainty Expressions (ACL 2025)](https://aclanthology.org/2025.acl-long.928/)
- [Think Through Uncertainty / CURE (2026)](https://arxiv.org/abs/2604.12046)
- [Only Say What You Know / CAG (2026)](https://arxiv.org/html/2605.01749)
- [SteerConf: Steering LLMs for Confidence Elicitation (NeurIPS 2025)](https://arxiv.org/abs/2503.02863)
- [ActCab/CoDec: Activation-Based Confidence Calibration (EMNLP 2024)](https://arxiv.org/abs/2406.13230)
- [CLAS: Contextual Linear Activation Steering](https://arxiv.org/abs/2604.24693)
- [Miranda Muqing Miao's homepage](https://mmiao2.github.io/)
- [Activation Steering Field Guide 2026](https://subhadipmitra.com/blog/2026/activation-steering-field-guide/)


【原始 proposal（允许参考但不是主要依据）】:
# Read and Steer: Probe-Guided Claim-Level Confidence Calibration for Long-Form Generation

**状态**: 待审阅  
**级别**: top-tier  
**创建时间**: 2026-05-15T15:11:55.979393+00:00

## 描述
We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. Motivated by two key findings — Han et al. (EMNLP 2025) showed lightweight probes detect claim-level factuality in long-form hidden states, and Miao & Ungar (2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features — RaS combines both insights in a novel way: it reads claim-level accuracy signals via factuality probes during autoregressive generation and steers verbalized confidence to match via targeted activation intervention along the orthogonal confidence direction, all within a single forward pass. A key design improvement is sub-sentence probe monitoring: rather than waiting for sentence boundaries, RaS evaluates an exponential moving average of probe scores every K tokens (K=8), enabling mid-claim steering activation when uncertainty is detected — consistent with evidence that hallucination signals emerge at span onset (Obeso et al., 2025) and that confidence representations are cached at answer-adjacent positions (Kumaran et al., 2026). Unlike O'Neill et al.'s probe→steer pipeline (which uses an external observer for binary hallucination reduction), RaS self-probes for graded confidence calibration with no second model. Unlike CARE (SIGIR 2025, which uses post-hoc iterative fact correction), RaS operates within the forward pass. Unlike Han et al.'s neuron clamping (binary suppression of hallucinations), RaS produces calibrated verbal hedging proportional to the model's internal uncertainty. Unlike CURE, CAG, and LoVeC, it requires no base model training — only lightweight linear probe fitting and contrastive direction extraction. The probe-guided adaptive steering formula (α = β × max(0, θ − EMA_score)) relates to CAST's conditional steering (ICLR 2025) and CLAS's context-dependent steering but is driven by continuous per-claim factuality signals rather than PCA-derived condition vectors or general context sensing. The framework includes a dedicated pilot experiment verifying the accuracy-confidence orthogonality at 70B scale in long-form generation — extending Miao & Ungar's finding beyond the 7–8B QA setting where it was established. We evaluate on Llama 3.1-70B (primary, testing scaling) and Llama 3.1-8B (sanity check, direct comparison with prior work) using FActScore and LongFact, measuring claim-level ECE, Brier score, AUROC, factual precision, and steering latency distribution. We target ≥25% claim-level ECE reduction (conservatively discounted from Miao & Ungar's 70–90% response-level QA results, given additional challenges of claim-level granularity, long-form generation, and 70B scale), with ≥40% as a stretch goal, while preserving FActScore within 2%. All experiments fit within ~195 H100-hours.

## 核心问题
LLMs generate long-form outputs where hallucinated claims are expressed with the same high confidence as factual ones. Existing approaches either detect hallucinations at claim level without calibrating expressed confidence (Han et al., EMNLP 2025 — binary probes + neuron clamping; O'Neill et al., July 2025 — external observer probe + binary steering), calibrate confidence only at response level for short-form QA (Ji et al., EMNLP 2025; Miao & Ungar, 2026; CORAL, 2026), perform fact-level calibration via post-hoc iterative correction rather than during generation (CARE, SIGIR 2025), use probe-guided steering without claim-level granularity or long-form scope (ITI, NeurIPS 2023; CLAS, 2026; ActCab/CoDec, EMNLP 2024), apply conditional or adaptive steering for behavioral control rather than calibrated confidence expression (CAST, ICLR 2025; Spherical Steering, ICML 2026; FLAS, 2026), or require multi-stage training of the base model (CURE, April 2026; CAG, May 2026; LoVeC, May 2025). No existing method performs claim-level calibrated uncertainty expression in long-form generation during a single forward pass without base model training. Furthermore, the accuracy-confidence orthogonality that enables clean steering (Miao & Ungar, 2026) has only been validated on 7–8B models for short-form QA — whether it holds at 70B scale in long-form generation is an open question with practical implications for the entire probe-guided steering paradigm.

## 机遇 / Why Now
Four recent results create a convergent opportunity: (1) Han et al. (EMNLP Findings 2025) showed lightweight linear probes on hidden states detect claim-level factuality in long-form generation, matching expensive multi-sample methods at up to 100× fewer FLOPs — but their neuron clamping intervention is binary (suppress/allow), not calibrated; (2) Miao & Ungar (March 2026) discovered that internal accuracy and verbalized confidence are nearly orthogonal linear features (cosine similarity < 0.04), meaning models internally know when they're wrong but fail to express this — and that adaptive CAA steering along these directions achieves major calibration improvement (ECE 14.9→3.7 on Llama-3.1-8B, 35.1→3.3 on Mistral-7B), but only for response-level QA on 7–8B models; (3) Kumaran et al. (March 2026) demonstrated that confidence representations are cached at answer-adjacent positions before verbalization, enabling real-time detection during generation — critically, their finding that hallucination signals emerge at the onset of hallucinated spans supports sub-sentence probe monitoring; (4) CLAS (April 2026) demonstrated that probe-derived adaptive steering works on models up to Llama 3.1-70B across 11 benchmarks, providing evidence that the steering mechanism scales — though not specifically for confidence calibration. Combining these — reading claim-level accuracy signals via probes during long-form generation, then steering verbalized confidence to match in real time — is unexplored and fills a specific gap. Critically, testing whether the accuracy-confidence orthogonality extends to 70B scale and long-form generation is itself a contribution that informs the feasibility of the entire probe-guided confidence steering paradigm.

## 方法思路
We propose Read-and-Steer (RaS), a single-pass framework for claim-level calibrated uncertainty expression in long-form generation. The system reads internal accuracy signals per-claim via lightweight probes and steers verbalized confidence to match via targeted activation intervention, producing naturally hedged language for uncertain claims while leaving confident-and-correct claims untouched.

**Pilot Experiment — Orthogonality Verification at Scale (~8h, 2× H100, first week):** Before committing the full experimental budget, we replicate Miao & Ungar's orthogonality analysis on Llama 3.1-70B in a long-form generation setting. We extract accuracy and confidence directions from biography-generation hidden states (not QA), measure their cosine similarity, and compare against the < 0.04 value found at 7–8B scale. This pilot has three outcomes: (a) orthogonality holds (cosine < 0.1) — proceed as planned, report the scaling result as a contribution; (b) orthogonality partially holds (cosine 0.1–0.3) — adapt steering to project out the accuracy component from the confidence direction before steering, proceed with modified approach; (c) orthogonality fails (cosine > 0.3) — report as an important negative finding about the limits of linear feature geometry at scale, fall back to the 8B-only configuration with reduced total compute (~70h). All three outcomes produce publishable results.

**Offline Stage 1 — Factuality Probe Training (~20h wall on 2× H100 for 70B; ~4h on 1× H100 for 8B; one-time per model):** Generate long-form outputs (biographies, factual descriptions) from the target model, decompose into atomic claims using FActScore/OpenFActScore decomposition, verify claim factuality against knowledge sources. Extract hidden states at each claim's token span across multiple layers (following Han et al.'s layer-group methodology). Train lightweight linear probes (logistic regression on span-aggregated hidden states) to predict continuous factuality confidence scores. Unlike Han et al.'s binary factuality labels, we train on soft labels derived from verification confidence, enabling graded uncertainty estimation.

**Offline Stage 2 — Verbalized-Confidence Direction Extraction (included in Stage 1 compute; one-time per model):** Extract a verbalized-confidence steering direction via contrastive activation pairs: generate matched claim pairs where the same factual content is expressed with high confidence ('X was born in Y') vs. hedged uncertainty ('X was reportedly born in Y, though I am not certain'). The mean activation difference yields the steering direction, following the contrastive methodology from Ji et al. (VUF) and Miao & Ungar (CAA). For the 70B model, if the pilot reveals partial orthogonality degradation, we apply Gram-Schmidt orthogonalization to project the confidence direction away from the accuracy direction before use.

**Online Stage — Sub-Sentence Probe-Guided Steering During Generation:** During autoregressive generation: (1) At each generated token, run the factuality probe on its hidden states — this is a single matrix-vector multiplication with negligible overhead (~0.001% of the forward pass). (2) Maintain a running exponential moving average (EMA) of probe scores over a sliding window of the last K tokens (default K=8), providing smoothed uncertainty estimates that avoid triggering on single noisy tokens while enabling sub-sentence response. (3) When the EMA drops below the calibrated threshold θ, immediately activate steering — even mid-sentence. This means RaS can begin hedging within the current claim by steering subsequent tokens toward uncertainty-expressing language (e.g., generating qualifiers like 'reportedly,' 'I believe,' or reformulations for the remaining tokens in the sentence). The steering magnitude follows the adaptive formula: α = β × max(0, θ − EMA_score), where β is calibrated on a held-out validation set. This adaptive formula is conceptually related to CAST's conditional steering (apply only when a condition is met) and CLAS's context-dependent steering, but driven by continuous per-claim factuality probe scores rather than PCA-derived category membership (CAST) or general context sensing vectors (CLAS). (4) Deactivate steering when the EMA recovers above threshold θ, indicating the model has returned to confident territory.

**Steering latency analysis:** The sub-sentence trigger design means that in the best case, the probe detects uncertainty within the first few tokens of a claim (consistent with Kumaran et al.'s finding that confidence signals are cached at answer-adjacent positions and Obeso et al.'s evidence that hallucination signals are detectable at span onset), and steering activates mid-claim with ~K/2 token latency. We will empirically measure the distribution of steering activation timing relative to claim boundaries: what fraction of uncertain claims receive hedging (a) within the same sentence, (b) within K tokens, and (c) only in subsequent sentences. If probe signals rise early in claims as prior work suggests, mid-claim steering should be feasible for most uncertain claims. For claims where steering activates late, the output exhibits forward-looking uncertainty conditioning — subsequent generation is explicitly uncertainty-aware — which we acknowledge as a known tradeoff and measure empirically.

**Key design choices addressing known limitations:** (a) EMA-smoothed probe scores over K-token windows avoid single-token noise while enabling sub-sentence response — a substantial improvement over sentence-boundary-only evaluation. (b) Single-pass online monitoring eliminates the two-pass chicken-and-egg problem — no position-aligned regeneration needed. (c) Continuous calibrated steering (not binary neuron clamping) produces graded hedging proportional to internal uncertainty, distinguishing this from Han et al.'s binary intervention and O'Neill et al.'s binary hallucination steering. (d) Operating on the verbalized-confidence direction (orthogonal to accuracy per Miao & Ungar, verified at 70B scale in our pilot) means steering affects expression style without corrupting the model's factual knowledge. (e) Self-probing eliminates the need for an external observer model (unlike O'Neill et al.), keeping the framework single-pass with negligible compute overhead. (f) Adaptive steering magnitude based on probe-detected need may mitigate the diminishing effectiveness of uniform CAA at larger scales (ICML 2025 scaling laws), since steering is only applied where needed and at probe-calibrated intensity.

**Models:** Llama 3.1-70B-Instruct as primary (standard dense transformer architecture, well-studied for probing and steering, large enough to test scaling of the orthogonality finding, with CLAS confirming probe-derived steering viability at this scale). Llama 3.1-8B-Instruct as lightweight sanity check (enables direct comparison with Miao & Ungar and Ji et al. baselines on the same model family, validates the pipeline in well-charted territory). Both models use standard transformer attention across all layers, avoiding the untested territory of hybrid DeltaNet architectures (e.g., Qwen 3.5) where linear probe and steering techniques lack validation.

**Benchmarks:** FActScore (biography generation, primary) and LongFact (diverse long-form factuality). Metrics: claim-level ECE, Brier score (calibration quality), AUROC (uncertainty detection), FActScore/factual precision (to verify steering does not degrade content quality), MT-Bench fluency subset (to verify generation quality preservation), and steering latency distribution (fraction of uncertain claims hedged within-sentence vs. forward-conditioned). We also report the cosine similarity between accuracy and confidence directions at 70B scale as a standalone mechanistic finding.

**Quantitative targets:** We expect RaS to achieve: (1) claim-level ECE reduction of ≥25% relative to unsteered baselines on both FActScore and LongFact (primary target), with ≥40% as a stretch goal — the primary target is conservative given that Miao & Ungar's response-level results (70–90% ECE reduction on QA) face additional challenges at claim-level granularity in long-form generation at 70B scale, including noisy claim boundary detection, probe signal dilution from long-context hidden states, and sub-sentence steering latency; (2) FActScore preservation within 2% of unsteered baseline (steering affects verbal expression, not factual content); (3) uncertainty detection AUROC ≥0.80 (probe-based); (4) superior calibration (lower ECE) compared to Han et al.'s binary neuron clamping at comparable or better FActScore; (5) ≥60% of uncertain claims receiving within-sentence hedging via sub-sentence triggers.

**Comparisons (3 baselines):** (1) Unsteered baseline (cost: ~3h), (2) Han et al.'s probes + neuron clamping (closest representation-based method for long-form; cost: ~13h), (3) CURE (closest training-based method for claim-level calibration, if reproducible; cost: ~14h). We discuss but do not reimplement O'Neill et al. (external observer, different setting), CARE (post-hoc correction, different mechanism), and LoVeC (RL-based, high reproduction cost).

**Ablations (3 core):** (1) Probe-only detection without steering (measures probe quality in isolation), (2) Uniform steering without probe guidance (constant steering magnitude — tests whether probe-adaptive steering outperforms naive uniform application), (3) Steering strength sensitivity (varying β, θ, and K-token window size — analyzes latency vs. signal quality tradeoff).

## 研究现状
**Foundational probe→steer paradigm:** ITI (Li et al., NeurIPS 2023) introduced inference-time intervention: linear probes identify truthful directions in attention heads, and activations are shifted along these directions during generation. Foundational work, but targets truthfulness (content change) rather than calibrated confidence expression, and only on TruthfulQA.

**Closest prior work — claim-level probing in long-form generation:** Han et al. (EMNLP Findings 2025) trained simple linear probes on LLM hidden states that detect claim-level hallucinations in long-form generation with performance matching expensive multi-sample methods (up to 100× fewer FLOPs), testing on models up to Llama 3.1-405B. Their neuron clamping causally reduces hallucinations by fixing activations of factuality-correlated neurons — but this is a binary intervention (suppress or allow) that does not produce calibrated verbal uncertainty expression. Obeso et al. (arXiv 2509.03531, 2025) trains entity-level probes for real-time streaming hallucination detection in long-form generation (AUC 0.90 on Llama-3.3-70B) — detection only, no calibrated steering.

**Closest prior work — observer-model probe→steer for hallucinations:** O'Neill et al. (arXiv 2507.23221, July 2025) demonstrated that a generator-agnostic observer model can detect contextual hallucinations via a linear probe on its residual stream, isolating a single transferable direction that outperforms baselines by 5–27 points across Gemma-2 models (2B–27B), and that manipulating this direction causally steers generator hallucination rates. RaS differs on three axes: (a) self-probing rather than requiring an external observer model, eliminating the overhead of a second forward pass; (b) graded confidence calibration rather than binary hallucination detection/reduction — RaS produces proportionally hedged language, not just fewer hallucinations; (c) claim-level granularity in long-form factual generation rather than span-level detection in context-grounded settings.

**Closest prior work — calibrated confidence steering:** Miao & Ungar (arXiv 2603.25052, March 2026) discovered that calibration accuracy and verbalized confidence are orthogonal linear features (cosine similarity < 0.04), and proposed two-stage adaptive CAA steering that reads internal accuracy and steers verbalized output to match, achieving ECE improvements from 14.9→3.7 (Llama-3.1-8B) and 35.1→3.3 (Mistral-7B) — but only for response-level short-form QA on 7–8B models. They explicitly acknowledge: 'Whether the linear encoding findings hold at larger scales remains open. Evaluation is restricted to question-answering tasks; extending to open-ended generation would require rethinking how the probe target is constructed.' Ji et al. (EMNLP 2025) discovered the Verbal Uncertainty Feature (VUF) and proposed MUC with ~30% reduction in confident hallucinations — also response-level, short-form, on ≤8B models.

**Same-group prior work — CORAL:** CORAL (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) uses regularized MLP probes on residual activations to predict correctness and steers at inference time, achieving 10% accuracy and 50% ECE improvements. However, CORAL targets MCQA on 7B models with response-level steering — no claim-level decomposition or long-form generation. RaS differs in (a) claim-level granularity via factuality probes, (b) long-form generation scope, and (c) confidence expression calibration rather than answer correctness steering.

**Fact-level calibration via iterative correction:** CARE (Yuan et al., SIGIR 2025; arXiv 2411.13343) proposes fact-level confidence calibration for long-form generation, decomposing responses into atomic facts, estimating per-fact confidence, and using high-confidence facts to iteratively refine low-confidence ones via ConFix. CARE addresses the same problem space (fact-level calibration in long-form outputs) but via a fundamentally different mechanism: post-hoc multi-pass correction through prompting, rather than single-pass activation steering during generation. RaS operates within the forward pass with no regeneration, targets verbal confidence expression rather than factual correction, and requires no external confidence estimation pipeline.

**Conditional and adaptive steering methods:** CAST (Arditi et al., ICLR 2025) introduced conditional activation steering where a PCA-derived condition vector determines whether to apply a behavior vector via thresholded cosine similarity: h' ← h + f(sim(h, proj_c h)) · α · v. CAST's 'if condition, then steer' paradigm is conceptually related to RaS's probe-triggered steering, but CAST uses a PCA-derived condition vector for behavioral categories (e.g., content moderation), while RaS uses a data-driven factuality probe score for continuous uncertainty calibration — the probe provides graded confidence estimates, not binary category membership. Spherical Steering (You et al., arXiv 2602.08169, February 2026; ICML 2026) replaces additive steering with norm-preserving geodesic rotation and uses a vMF-based confidence gate for input-adaptive strength, achieving +10% on TruthfulQA with Llama-3.1-8B — but targets truthfulness in MCQ rather than calibrated confidence expression in long-form generation. FLAS (Jin et al., arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field enabling curved, multi-step trajectories through activation space, outperforming prompting on AxBench with Gemma-2 models — a more expressive steering mechanism than linear CAA, but tested only on small models (2B–9B) for general behavior control, not confidence calibration.

**Activation calibration + guided decoding:** ActCab/CoDec (EMNLP 2024) trains a linear layer on LM last-layer activations for confidence calibration, then uses confidence-guided decoding to elicit truthful answers. Same conceptual pipeline (activation-based calibration → guided generation) but operates at response level on QA, and modifies decoding probabilities rather than verbalized confidence expression.

**Adaptive steering strength:** CLAS (Hsu et al., arXiv 2604.24693, April 2026) introduces context-dependent linear activation steering where steering strength adapts via learned sensing vectors: α_ℓ,t = (c_ℓ · [h_ℓ,t, 1]). Tested on Llama-3.1-70B across 11 benchmarks, demonstrating that probe-derived adaptive steering scales to 70B. RaS's α = β × max(0, threshold − probe_score) adapts similarly but is driven by factuality probe scores per-claim rather than a general context sensing vector, and targets confidence calibration specifically.

**Mechanistic understanding:** 'How do LLMs Compute Verbal Confidence?' (Kumaran et al., arXiv 2603.17839, March 2026) provides convergent evidence that confidence representations emerge at answer-adjacent positions via cached retrieval, supporting the feasibility of online detection during generation. Their finding that signals are cached before verbalization motivates sub-sentence probe monitoring.

**Training-free steering baselines:** SteerConf (NeurIPS 2025) does prompt-based training-free confidence steering via multi-prompt aggregation. ACT (WWW 2025) applies tuning-free diverse steering vectors with adaptive intensity for truthfulness, scaling to 65B.

**Claim-level long-form calibration (training-based):** CURE (arXiv 2604.12046, April 2026) uses multi-stage training to teach claim-level confidence reasoning, improving accuracy by up to 39.9%. CAG (arXiv 2605.01749, May 2026) achieves up to 13% factuality gain via training-based calibration-aware generation. LoVeC (arXiv 2505.23912, May 2025) uses RL to train LLMs to append on-the-fly confidence scores per statement in long-form generation, achieving 20× speedup over self-consistency methods. All three require base model fine-tuning or RL.

**Post-generation claim-level approaches:** CSS (arXiv 2604.17487, April 2026) decomposes answers into claims and backs off uncertain ones using external verifiers. Selective Abstraction (arXiv 2602.11908, February 2026) replaces low-confidence atoms with confident abstractions.

**Residual-stream anomaly detection:** PCNET (arXiv 2605.05953, May 2026) uses probabilistic circuits on residual streams for hallucination detection + contrastive decoding, reaching up to 99% AUROC — but targets short-form QA and changes content (different token selection) rather than expressing calibrated uncertainty.

**Scaling concerns for activation steering:** Scaling laws for activation steering (ICML 2025) show that CAA effectiveness diminishes with model size on Llama 2 (7B→13B→70B) for behavioral steering (refusal). Endogenous steering resistance (arXiv 2602.06941, February 2026) shows Llama-3.3-70B has 3.8% ESR rate (vs <1% for smaller models). However, CLAS demonstrates successful probe-derived steering on Llama-3.1-70B, suggesting that adaptive, probe-guided steering may be more robust at scale than uniform CAA.

**Gap:** No existing work combines claim-level factuality probing (à la Han et al.) with calibrated activation steering along the verbalized-confidence direction (à la Miao & Ungar) in a single-pass, online framework for long-form generation. O'Neill et al.'s probe→steer pipeline is closest structurally but uses an external observer for binary hallucination reduction rather than self-probing for graded confidence calibration. CARE addresses fact-level calibration in long-form outputs but via post-hoc correction rather than real-time activation steering. CAST provides conditional steering but for behavioral categories, not continuous confidence calibration. This intersection — reading internal accuracy per-claim and steering verbalized confidence to match during generation — is the contribution space. Additionally, no work has tested whether the accuracy-confidence orthogonality discovered at 7–8B scale holds at 70B or in long-form generation contexts, making this verification itself a contribution to the mechanistic understanding of confidence representations.

## 目标 Venue
- AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — ~10 weeks; conference Feb 16-23, Montréal) — PRIMARY
- ARR August 2026 (submission Aug 3, 2026 — ~11 weeks; committable to EMNLP 2026 Oct 24-29 or later *ACL venues)
- ICLR 2027 (expected submission ~Oct 2026, ~20 weeks; comfortable timeline)

## 关键参考
- Simple Factuality Probes Detect Hallucinations in Long-Form Natural Language Generation (Han et al., Findings of EMNLP 2025) — closest prior work: claim-level probes + neuron clamping in long-form generation
- A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations (O'Neill et al., arXiv 2507.23221, July 2025) — closest probe→steer pipeline: external observer linear probe detects and steers hallucinations across Gemma-2 2B–27B; differs from RaS in using external observer (vs. self-probing), binary hallucination steering (vs. graded confidence calibration), and context-grounded settings (vs. long-form factual generation)
- Closing the Confidence-Faithfulness Gap in LLMs (Miao & Ungar, arXiv 2603.25052, March 2026) — accuracy-confidence orthogonality discovery + adaptive CAA steering; explicitly notes scaling and long-form extension as open questions
- Correctness-Optimized Residual Activation Lens [CORAL] (Miao, Cho & Ungar, arXiv 2602.06022, February 2026) — same group; MLP probes → correctness steering on MCQA at 7B scale; must differentiate as response-level, short-form only
- Fact-Level Calibration and Correction for Long-Form Generations [CARE/ConFix] (Yuan et al., SIGIR 2025; arXiv 2411.13343) — fact-level confidence calibration + iterative correction via high-confidence facts refining low-confidence ones; same problem space but fundamentally different mechanism (post-hoc multi-pass correction vs. single-pass activation steering)
- Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025) — VUF discovery and MUC for response-level short-form QA
- Inference-Time Intervention: Eliciting Truthful Answers from a Language Model [ITI] (Li et al., NeurIPS 2023) — foundational probe→steer paradigm using linear probes on attention heads for truthfulness
- Programming Refusal with Conditional Activation Steering [CAST] (Arditi et al., ICLR 2025) — conditional steering via PCA-derived condition vectors with thresholded activation; conceptually related 'if condition, then steer' paradigm, but targets behavioral categories rather than continuous confidence calibration
- Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., arXiv 2602.08169, February 2026; ICML 2026) — norm-preserving geodesic rotation with vMF confidence gating; +10% on TruthfulQA with Llama-3.1-8B; targets truthfulness MCQ, not calibrated confidence in long-form
- Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention [FLAS] (Jin et al., arXiv 2605.05892, May 2026) — learned concept-conditioned velocity field for curved activation trajectories; more expressive than linear CAA but tested on Gemma-2 2B–9B for general behavior control
- Enhancing Language Model Factuality via Activation-Based Confidence Calibration and Guided Decoding [ActCab/CoDec] (EMNLP 2024) — activation calibration + confidence-guided decoding for QA factuality
- Contextual Linear Activation Steering [CLAS] (Hsu et al., arXiv 2604.24693, April 2026) — probe-derived adaptive steering with context-dependent strength; tested on Llama-3.1-70B, confirming steering viability at 70B scale
- How do LLMs Compute Verbal Confidence? (Kumaran et al., arXiv 2603.17839, March 2026) — mechanistic evidence for cached confidence retrieval at answer-adjacent positions; supports feasibility of sub-sentence probe monitoring
- Reinforcement Learning for Better Verbalized Confidence in Long-Form Generation [LoVeC] (arXiv 2505.23912, May 2025) — RL-based on-the-fly confidence scoring per statement in long-form generation; training-based
- Scaling Laws for Activation Steering with Llama 2 Models and Refusal Mechanisms (ICML 2025) — demonstrates CAA effectiveness diminishes with model size (7B→70B); informs our adaptive steering design
- Endogenous Resistance to Activation Steering in Language Models (arXiv 2602.06941, February 2026) — Llama-3.3-70B shows 3.8% endogenous steering resistance; relevant scaling concern
- Does Transformer Interpretability Transfer to RNNs? (2024) — probing and CAA partially transfer to recurrent architectures with reduced effectiveness; motivates our choice of standard transformer models
- SteerConf: Steering LLMs for Confidence Elicitation (Zhou et al., NeurIPS 2025) — prompt-based training-free confidence calibration
- Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025) — diverse steering vectors with adaptive intensity control
- Real-Time Detection of Hallucinated Entities in Long-Form Generation (Obeso et al., arXiv 2509.03531, 2025) — entity-level streaming probes for long-form generation; evidence that hallucination signals are detectable at span onset
- Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits [PCNET] (arXiv 2605.05953, May 2026) — residual stream anomaly detection + contrastive decoding intervention
- Streaming Hallucination Detection in Long Chain-of-Thought Reasoning (arXiv 2601.02170, January 2026) — online hallucination detection as evolving latent state
- Think Through Uncertainty: Improving Long-Form Generation Factuality via Reasoning Calibration [CURE] (arXiv 2604.12046, April 2026) — multi-stage training for claim-level confidence reasoning
- Only Say What You Know: Calibration-Aware Generation for Long-Form Factuality [CAG] (arXiv 2605.01749, May 2026) — training-based calibration-aware generation
- Atomic Calibration of LLMs in Long-Form Generations (Findings of AACL-IJCNLP 2025) — showed poor claim-level calibration in long-form outputs
- Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control [CSS] (arXiv 2604.17487, April 2026) — post-generation specificity control via external verifiers
- When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation (arXiv 2602.11908, February 2026)
- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (ICML 2024) — linear probes approximate semantic entropy at response level
- FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (EMNLP 2023)
- Long-form Factuality in Large Language Models [LongFact/SAFE] (NeurIPS 2024)
- Steering Language Models With Activation Engineering (Turner et al., arXiv 2308.10248, 2023)

## 资源估算
### auto_research
- **claude_api_cost**: $200-400 (~3000-6000 Opus turns)
- **estimated_gpu_cost**: $490-680
- **gpu_hours**: ~195h H100 80GB (agent explores probe architectures, layer selections, K-window sizes, steering schedules on 70B primary model with 8B sanity checks, plus evaluation)
- **gpu_utilization**: ~80-90% — continuous experiment pipeline with minimal idle
- **risk_note**: Without human judgment, agent may over-optimize probe thresholds and K-window sizes on validation set rather than ensuring robustness, may miss qualitative assessment of hedging naturalness (mid-sentence steering coherence requires human evaluation), and critically may not correctly interpret the orthogonality pilot results (the decision to proceed vs. pivot requires understanding of the mechanistic implications)
- **speed_bottleneck**: Long-form generation throughput on Llama 3.1-70B with 2× H100 tensor parallelism (~20-30 tok/s) — generating and evaluating hundreds of long-form responses per configuration is the computational bottleneck
- **team**: 0 researchers (initial setup + final review only)
- **timeline**: 7-10 days with 2× H100 80GB

### human_in_loop
- **claude_api_cost**: $100-200 (~1500-3000 Opus turns)
- **estimated_gpu_cost**: $425-595
- **gpu_hours**: ~170h H100 80GB (agent handles pipeline code, probe training iteration, evaluation scripting; human approves pilot results, probe design, steering threshold calibration, and ablation priorities)
- **gpu_utilization**: ~50-65% — agent queues experiments between human check-ins
- **risk_note**: Primary risk: whether accuracy-confidence orthogonality holds at 70B scale in long-form generation — the ~8h pilot experiment validates this before committing the full budget. If orthogonality breaks (outcome c), we fall back to an 8B-only paper with the negative scaling result as a contribution, reducing total compute to ~70h H100. Secondary risk: whether sub-sentence probe-guided steering produces natural hedging at 70B or creates incoherent mid-sentence shifts — qualitative human assessment of hedging naturalness across K-token window sizes is essential. Tertiary risk: CAA effectiveness diminishing at 70B scale (per ICML 2025 scaling laws), though our adaptive probe-guided approach may be more robust than uniform steering.
- **team**: 1 researcher, ~30min/day for methodology decisions, pilot outcome assessment, and qualitative hedging evaluation
- **timeline**: 3-4 weeks

### manual
- **estimated_gpu_cost**: $490-680 (at ~$2.50-3.50/hr H100 80GB spot)
- **gpu_hours**: ~195h H100 80GB (orthogonality pilot ~8h [2×H100], probe training + direction extraction ~24h [20h 70B on 2×H100, 4h 8B on 1×H100], Llama 3.1-70B evaluation on FActScore + LongFact ~85h [2×H100], Llama 3.1-8B sanity check ~12h [1×H100], baseline comparisons ~30h [unsteered ~3h, Han et al. ~13h, CURE ~14h], core ablations ×3 ~25h, debugging/rerun buffer ~11h)
- **gpu_utilization**: ~25-35% effective — GPU idles during code development, pipeline debugging, and results analysis
- **team**: 1-2 researchers with mechanistic interpretability and activation steering experience
- **timeline**: 5-6 weeks (1 researcher full-time)



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a92979bc-8aa2-4847-97f6-0c165ae8b4ef",
  "type": "user",
  "uuid": "e7b5b2ea-5024-433d-aa18-fcca3d87ea17",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T01:55:40.890Z_

```json
{
  "parentUuid": "e7b5b2ea-5024-433d-aa18-fcca3d87ea17",
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
  "uuid": "b2cde544-fdb1-4750-a9a6-29c28aa442d3",
  "timestamp": "2026-05-16T01:55:40.890Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T01:55:40.890Z_

```json
{
  "parentUuid": "b2cde544-fdb1-4750-a9a6-29c28aa442d3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b5fd3423-f45d-4f84-86db-887b2971bbe8",
  "timestamp": "2026-05-16T01:55:40.890Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information from my literature search to…",
  "leafUuid": "b5fd3423-f45d-4f84-86db-887b2971bbe8",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate probe-guided confidence calibration proposal",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d"
}
```

---

### Assistant

_source line 8 · 2026-05-16T01:56:11.781Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them as the Meta Judge.

Let me extract the key data points:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [22% - 33%] 中位 27%

**Reviewer 2:**
- Novelty: 弱 (Weak)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability: [20% - 30%] 中位 25%


**Reviewer 3:**
- Novelty: 中（偏弱）(Medium-weak)
- Significance: 中（偏强）(Medium-strong)
- Related Work: 强 (Strong)
- Probability: [22% - 33%] 中位 27%

Looking at the three probability estimates—27%, 25%, and 27%—the median comes to 27% with a mean around 26.3%, showing fairly tight clustering. Now I'm examining where the reviewers align and where they diverge. All three reviewers agree that the related work section is strong, which is a clear consensus point.

The novelty constraint emerges as the decisive factor across all reviews—each reviewer identifies it as the primary barrier to acceptance, using consistent language about this being a straightforward combination of existing techniques. There's also unanimous concern about a simpler alternative: a post-hoc probing-then-rewriting pipeline could potentially be more reliable than the partial-context approach, and the single-pass efficiency gain feels more like an engineering contribution than a conceptual advance. Similarly, all three flag that uniform or sentence-level steering without fine-grained probing represents a viable competing approach. The orthogonal scaling assumption that underpins the method is flagged by all reviewers as a critical gap that remains unverified.

Beyond these shared concerns, there's convergence on several other risks: the coherence of mid-sentence steering, whether probes trained on complete claims actually transfer to online partial-context scenarios, and the fact that even a successful result wouldn't feel surprising—it would read as an expected outcome rather than a discovery. Significance lands at medium across the board, though R2 rates novelty more harshly than R1 and R3.

The probability estimates cluster tightly at 25-27% with minimal variance, and the rubric judgments align well overall. Given this consistency, I should probably anchor to the median assessment and potentially tighten the confidence interval.

Now I'm settling on a final estimate around 26% with a range of [20%-32%], leaning slightly toward the stricter reviewer's bounds while acknowledging the two-reviewer consensus on 27%. I'm also reviewing the implementation feasibility—the compute requirements are substantial at roughly 195 hours on H100s, but the data sources are publicly available and the human effort is minimal, making this achievable within a 3-6 week timeline without requiring new benchmarks or base model training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5fd3423-f45d-4f84-86db-887b2971bbe8",
  "isSidechain": false,
  "requestId": "req_011Cb5R5R2HLabnWnUYLUidH",
  "type": "assistant",
  "uuid": "079b10bc-0ac7-4590-9ff9-785822114864",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcRGMhxrPgJquXGf3iFvEy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23957,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23957,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3500,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23957
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

_source line 9 · 2026-05-16T01:57:03.511Z_

【阶段】: Meta Judge
【三次中位】: [27%, 25%, 27%]  std=1.15%
【共识维度】:
- **Related Work: 强**（3/3 一致）— 覆盖全面（20-30篇近期工作），差异化定位精确，gap 论证严谨
- **Novelty 是概率上界的主要约束**（3/3 一致）— 均使用"combination paper""predictable next step""straightforward combination"等表述，认为核心贡献是 Han et al. probes + Miao & Ungar steering 的 natural intersection
- **Significance: 中**（3/3 一致，R3 偏强但仍为中）— 问题本身重要，但 positive result 不 surprising（"I would have guessed this"）
- **Trivial Alternative: Post-hoc probe→rewrite pipeline 构成实质威胁**（3/3 独立提出）— complete-context probing 可能比 partial-context 更可靠，single-pass 优势仅为工程便利
- **Trivial Alternative: Uniform/粗粒度 steering 的增量价值存疑**（3/3 均提出某种形式）
- **Orthogonality 7-8B→70B 外推是关键未验证前提**（3/3 一致）— pilot 设计合理但前提脆弱
- **Partial-context online probing 可靠性未经验证**（3/3 一致）— 离线 full-claim 训练的 probe 能否在线 streaming 中 K=8 窗口上工作
- **Mid-sentence steering 连贯性风险**（3/3 一致）— 句中激活 steering 可能导致不自然输出
- **Positive result 的 surprise value 低**（3/3 一致）— 25% ECE reduction 是 Miao & Ungar response-level 结果的 expected degraded version

【异常维度】:
- **LoGU (ACL 2025) 作为遗漏 related work**（仅 R3 提出）— problem framing 重叠但 mechanism 不同（SFT+DPO vs. activation steering），属于 positioning 层面的补充而非致命遗漏，降权处理
- **Soft factuality labels 质量问题**（R2/R3 提出，R1 未显式标注）— 2/3 提出，接近共识但非完全共识，作为中等风险保留
- **Novelty 具体评级**：R1=中, R2=弱, R3=中偏弱 — R2 是 outlier（更严），但方向一致（均认为 novelty 不足以 carry）。综合判定为**中偏弱**，不采纳 R2 的"弱"也不采纳 R1 的纯"中"

【最终概率】: [20% - 31%] 中位 26%
【一致性】: 高（std=1.15% < 3%，rubric 判决高度收敛）
【综合理由】:
三位审稿人在所有关键维度上高度收敛，是罕见的强共识情形。具体推理如下：

1. **Novelty 共识锁死了概率上界**：三人一致认为这是一篇 combination paper，核心组件均借用 prior work，组合方式是两篇关键先行工作（Miao & Ungar + Han et al.）的 predicted intersection——Miao & Ungar 自己在论文中已经指明了这个方向。Sub-sentence EMA 是工程贡献而非概念创新。在 EMNLP 主会对 novelty 的 bar 下，这严重限制了上界。R2 给出"弱"但 R1/R3 给"中/中偏弱"，综合为"中偏弱"——对应的概率天花板约 32-35%，但考虑到 positive result 不 surprising，实际上界不超过 31%。

2. **Significance 共识提供了 floor**：问题确实重要（claim-level calibration in long-form generation），training-free 方案有实用价值，70B orthogonality 验证本身有 mechanistic insight。这让概率不至于跌到 base rate 以下。但 expected result 符合直觉（不是 counterintuitive finding），无法弥补 novelty 不足。

3. **Related Work 共识防止了 positioning 层面的致命伤**：gap 真实、定位准确、覆盖全面——不会因"missed related work"或"unclear positioning"被拒。这是这篇工作的安全网。

4. **Trivial Alternative 共识是实质威胁**：三人独立提出的 post-hoc baseline 构成真正的增量价值质疑。如果 two-pass pipeline（生成→probe→rewrite）在 complete-context 下表现相当甚至更好，RaS 的 single-pass 优势缩水为工程便利，核心学术贡献被削弱。

5. **中位取 26% 而非 27% 的理由**：虽然两位给 27%、一位给 25%，但在高一致情形下我略偏向更严格方（R2 的 25%），因为 R2 对 novelty 的"弱"评判虽是 outlier，但其论证逻辑（"两个 individually work 的方法组合在一起 work 是预期结果而非发现"）与 R1/R3 的实质判断一致，只是措辞更直接。下界取 R2 的 20%（最严），上界从 R1/R3 的 33% 收窄至 31%（高一致时缩窄区间）。

【建议】: 边缘（idea 质量限制了天花板，但问题重要、定位扎实，有优化空间值得尝试迭代）

【实施评估】:
- **计算资源**: ~195h H100 80GB（2×H100 张量并行用于 70B 推理），预估 GPU 成本 $490-680（spot pricing）。Pilot 实验 ~8h，probe 训练 ~24h，主实验评估 ~85h，baseline 对比 ~30h，ablation ~25h，buffer ~11h。计算需求合理，不构成瓶颈。
- **数据需求**: FActScore（传记生成）和 LongFact（多样化长文本事实性）——均为公开 benchmark，无数据获取障碍。Probe 训练需要生成+标注的 claim-level 数据，但可通过 pipeline 自动化构建。
- **人工介入**: 最低 1 人 ~30min/day（human-in-loop 模式），主要用于 pilot 结果判读（orthogonality 是否成立的关键决策点）、hedging 自然度的定性评估（mid-sentence steering 连贯性需人工判断）、以及实验优先级决策。全自动模式风险较高——probe 阈值过拟合和 steering 连贯性评估是 agent 难以可靠完成的任务。
- **训练需求**: **无需训练基座模型**。仅需训练轻量线性 probe（logistic regression on hidden states）和提取 contrastive direction——均为 one-time offline 操作，计算开销极小。这是方法的核心卖点之一。
- **新 Benchmark**: 不需要。使用现有的 FActScore 和 LongFact 评测框架，评测指标（ECE, Brier, AUROC, FActScore）均为标准指标。
- **预估周期**: Human-in-loop 模式 3-4 周（1 研究者）；全手动模式 5-6 周（1-2 研究者全职）。距 ARR August 2026 deadline（8月3日）约 11 周，时间充裕。距 AAAI 2027 abstract deadline（7月21日）约 10 周，偏紧但可行。**关键路径风险**：如果 orthogonality pilot 失败（outcome c），需在第 1 周做出 pivot 决策，fallback 到 8B-only 配置（~70h compute），时间仍然充裕但论文 impact 会显著降低。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "079b10bc-0ac7-4590-9ff9-785822114864",
  "isSidechain": false,
  "requestId": "req_011Cb5R5R2HLabnWnUYLUidH",
  "type": "assistant",
  "uuid": "3ea19441-73eb-4b15-a25a-7305c29ff35c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcRGMhxrPgJquXGf3iFvEy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23957,
      "cache_read_input_tokens": 11374,
      "output_tokens": 3500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23957,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3500,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23957
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information from my literature search to…",
  "leafUuid": "3ea19441-73eb-4b15-a25a-7305c29ff35c",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate probe-guided confidence calibration proposal",
  "sessionId": "864f810d-4033-4a87-9729-10ef4237166d"
}
```

---
