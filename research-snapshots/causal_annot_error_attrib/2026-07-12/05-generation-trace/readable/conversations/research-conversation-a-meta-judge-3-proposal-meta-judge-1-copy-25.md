# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/e10f70ec-57b9-40a7-ac79-90fdae8bdf74.jsonl`
- **Structured JSON:** [`f2e064ace2c6f280455c.json`](../../sessions/f2/f2e064ace2c6f280455c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:49:12.134Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:49:12.134Z",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make a well-grounded assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562)](https://arxiv.org/abs/2504.13562): 推理时注意力重分配防御。通过识别对越狱敏感的注意力头，运行时在 intent token 位置放大注意力（β=5.0），LLaMA-2 上 ASR 46%→1.2%。仅限单轮，需运行时识别 intent token。Proposal 将其作为\"推理时注意力重分配有效\"的因果证据基础，定位准确。\n- [Wan et al. CPL (ICML 2026, arXiv:2602.03664)](https://arxiv.org/abs/2602.03664): 识别对话惯性（diagonal attention），提出 Context Preference Learning（LoRA rank-16 DPO, β=0.01），在 8 个 agentic 环境上验证。关键：对角注意力**仅在 aggregate 层面刻画**（显式说明\"所有注意力头被平均\"），**从未评估过安全性**。CPL 降低对角注意力 >10%，提升系统注意力。Proposal 的核心干预方法。\n- [ASGuard (Park et al., ICLR 2026, arXiv:2509.25843)](https://arxiv.org/abs/2509.25843): 训练时电路层面注意力头修改。通过 EAP-IG 定位 tense jailbreaking 的脆弱注意力头，channel-wise scaling + preventative fine-tuning，ASR 42%→8%。识别 Llama-3.1-8B 中 11 个脆弱头（4 个在 Layer 13）。局限：依赖可定位的因果电路，针对特定攻击类型。\n- [Deng et al. (arXiv:2603.08234, Mar 2026)](https://arxiv.org/abs/2603.08234): 揭示 continuation head（中间层 ~L13）与 safety head（L25-27）的对抗性竞争机制，continuation-triggered jailbreak 源于这种内在竞争。独立佐证 Layer 13 是安全竞争的关键枢纽。\n- [Johnson & Huo (arXiv:2602.14370, Feb 2026)](https://arxiv.org/abs/2602.14370): 数学化注意力竞争的 tipping point 理论——dot-product 竞争创造动态翻转点 n*，超过后从安全行为转变为不安全行为。为\"累积惯性跨轮推动系统越过阈值\"提供理论框架。\n- [Zhou et al. (ICLR 2025, arXiv:2410.13708)](https://arxiv.org/abs/2410.13708): 提出 Ships 分数，识别安全关键注意力头。单个头消融可使模型对 16 倍有害查询做出响应，仅修改 0.006% 参数。\n- [AISA (Song et al., arXiv:2602.13547)](https://arxiv.org/abs/2602.13547): 通过时空分析定位安全感知头（top-K=16，0.92 检测精度），提供轻量级 logits-level steering。\n- [X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990)](https://arxiv.org/abs/2502.09990): 表示层面安全边界，多轮 ASR 58.5%→16.5%，降低过拒绝 ~20%。\n- [Steering Dialogue Dynamics (arXiv:2503.00187)](https://arxiv.org/abs/2503.00187): 通过学习安全预测器实现每轮对话的不变安全性，防止上下文漂移——与 proposal 的多轮安全防御方向相关但方法不同。\n- 额外搜索确认：**目前没有任何工作测试过话语层面干预（特别是对话惯性削减）对安全性的因果影响**。CPL→安全性的连接确实是一个未被探索的空白。\n\n- 调研总结: 该领域已形成清晰的多线收敛格局——推理时注意力重分配（DETAM）、训练时电路修改（ASGuard）、多轮安全训练（XGuard-Train, MUSE-D, X-Boundary, MTSA）、安全头定位（Zhou, AISA, Depth Charge）、注意力竞争理论（Johnson & Huo）、话语动力学（Wan CPL）各自独立发展，但\"话语层面惯性削减→安全改善\"的因果桥梁确实是空白。Proposal 处于这个交叉点上，gap 是真实的。\n\n【Trivial Alternative 检验】: \n**存在显著的 trivial alternative 威胁。** 最直接的替代方案是：直接在安全标注数据上做 LoRA DPO/SFT（如 XGuard-Train 已证明 48.3% vulnerability reduction，MUSE-D 实现 24% ASR reduction）。如果目标是\"改善多轮安全性\"，直接用安全数据训练是成本更低、效果已验证的方法。Proposal 试图通过\"间接\"路径（话语惯性削减→注意力重分配→安全改善）达到类似效果。其增量价值在于：(1) 如果 CPL 不使用任何安全标注数据就能改善安全性，这揭示了一个关于注意力竞争的因果机制洞察；(2) 间接方法可能泛化到直接方法无法覆盖的分布外攻击。但关键问题是：**审稿人极有可能问 \"为什么不直接训练安全数据？间接路径的实际优势是什么？\"** Proposal 的回答（\"CPL 不需要安全数据\"）是合理的，但需要实证证明 CPL 确实在 XGuard-SFT 无法覆盖的场景中表现更好，否则间接路径的价值仅停留在\"机制洞察\"层面。\n\n【前提假设检验】: \n核心逻辑链：对角注意力（惯性）→ 与安全注意力竞争 → 累积跨轮 → 越过 tipping point → 安全退化。CPL 削减惯性 → 释放注意力容量 → 安全改善。\n**未经验证的关键假设**:\n1. **假设 A（头级重叠）**: 对角注意力头与安全头存在实质重叠。这是 Level 1 假设的前提，而 Wan et al. 从未做过 per-head 分解，这个重叠可能为零或极低。Proposal 意识到了这一点并设计了三级框架来对冲，但如果结果是 Level 3（表示级），竞争机制变得模糊且几乎不可证伪。\n2. **假设 B（因果方向）**: 假设是\"惯性→安全退化\"，但因果方向可能相反——安全退化（如 alignment erosion）可能导致模型更依赖惯性续写模式，而非惯性\"挤占\"安全注意力。Proposal 的混合效应回归和 Granger 因果检验在一定程度上可以区分，但观察数据上的因果推断能力有限。\n3. **假设 C（CPL 效果可迁移）**: CPL 在 agentic 环境（ALFWorld, WebShop 等）上训练的惯性削减能力能迁移到安全评估场景。两者的分布差异（工具使用任务 vs. 安全对话）可能使 CPL 的惯性削减效果在安全场景中大打折扣。\n4. **假设 D（tipping point 可操作性）**: Johnson & Huo 的 tipping point 理论在抽象数学层面有效，但在实际 Transformer 的 multi-head attention 中是否真的存在可观察的\"阈值效应\"尚无实证。该理论更多是类比框架而非可量化预测。\n\n【3 维度打分】:\n  1. Novelty: 中 — 研究问题本身是真正新颖的：将话语动力学（CPL/对角注意力）与安全性因果联系起来，确实是一个未被探索的交叉点（搜索确认无直接竞争工作）。per-head 对角注意力分解和三方法安全头识别比较是真正的分析性贡献。但核心操作是\"将别人的方法（CPL）应用到新评估场景（安全性）\"，而非提出新方法。且核心预测——\"如果惯性占用注意力容量，减少惯性应该释放安全注意力\"——是已知成分（softmax 零和 + 安全头 + 对角注意力）的自然推论，审稿人可能判断为 \"I would have guessed this\"。三级假设框架虽然结构化但有unfalsifiable之嫌（任何结果都可以被归入某个level）。相比 Deng et al. 发现 continuation-safety 头竞争、DETAM 证明注意力重分配改善安全性这些\"令人惊讶\"的发现，本 proposal 更像是对已知机制的系统化验证而非新发现。\n  \n  2. Significance: 中 — 多轮安全是重要且活跃的研究方向（MT-AgentRisk, OpenAgentSafety, MultiBreak 等 benchmark 的涌现证实了这一点）。如果 CPL 确实在无安全标注数据的情况下改善安全性，这对理解注意力机制与安全性的关系有深远意义。但实际影响受限于两个因素：(a) 如果结果是 positive 但不如 XGuard-SFT 等直接方法，实用价值有限，贡献主要在机制洞察层面；(b) 如果结果是 negative/weak（落入 Level 3），论文退化为\"per-head 分析 + 安全头比较\"的分析性贡献，虽有价值但影响力显著降低。最佳情形（CPL 大幅改善安全性且通过注意力竞争机制）是有意义的，但这个情形发生的概率本身也是未知的。Proposal 的\"dual-outcome\"设计保证了有输出，但不保证输出有高影响力。\n  \n  3. Related Work: 强 — 覆盖面极其全面，涵盖了 6 条独立研究线索，每条线索的定位和差异化分析都很准确。DETAM、ASGuard、Wan et al.、Deng et al.、Johnson & Huo、AISA 等关键论文的描述经调研验证均准确。Gap 识别是真实的——确实无人测试话语干预→安全改善的因果链。与 ASGuard Layer 13 头的交叉引用（独立佐证 continuation-safety 竞争）是一个有说服力的论证。唯一小瑕疵：部分引用（如 \"Agent Drift\", \"SafetyDrift\" 等 2026 论文）未提供 arXiv ID，无法完全验证；但核心论证所依赖的文献均真实可查。\n\n【概率估计】: [22% - 32%] 中位 27%\n\n【估计理由】: \nNovelty 是中等水平——研究问题真正新颖但核心洞察不够 surprising（\"减少注意力竞争改善安全\"是自然推论而非反直觉发现），这限制了上界无法突破 35%。Significance 同样中等——最佳情形有价值但最佳情形发生概率不确定，且存在强 trivial alternative（直接安全训练）。Related Work 的强势表现提供了坚实下限。三者综合：这是一个方向正确、gap 真实、分析框架有贡献的 proposal，但核心 claim 的内核——\"间接话语训练能因果改善安全\"——即使被证实，审稿人更可能评价为 \"interesting empirical finding\" 而非 \"surprising insight\"。**上界主要被 Novelty 限制**：核心假设是已知成分的组合，三级框架的 unfalsifiable 特性可能被视为 hedging 而非科学严谨。\n\n【主要风险】: \n1. **\"Apply X to Y\" 感知风险**: 审稿人可能将此视为\"把 CPL（别人的方法）应用于安全评估（新场景）\"的增量工作，而非独立的方法论贡献。三级假设框架和 per-head 分析是真正的贡献，但容易被这一感知淹没。\n2. **三级假设 unfalsifiable 风险**: Level 1→Level 2→Level 3 的递降框架确保了\"总有某个 level 成立\"，审稿人可能质疑：如果任何结果都能被纳入框架，这个假设的科学价值是什么？特别是 Level 3（表示级竞争）过于宽泛，几乎任何 DPO 训练效果都可以被归因于\"表示级竞争\"。\n```\n\nSources:\n- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification](https://arxiv.org/abs/2504.13562)\n- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026)](https://arxiv.org/abs/2602.03664)\n- [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (ICLR 2026)](https://arxiv.org/abs/2509.25843)\n- [The Struggle Between Continuation and Refusal (Deng et al., 2026)](https://arxiv.org/abs/2603.08234)\n- [Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, 2026)](https://arxiv.org/abs/2602.14370)\n- [On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)\n- [AISA: Awakening Intrinsic Safety Awareness in LLMs (Song et al., 2026)](https://arxiv.org/abs/2602.13547)\n- [X-Boundary: Establishing Exact Safety Boundary (Lu et al., EMNLP 2025)](https://arxiv.org/abs/2502.09990)\n- [Steering Dialogue Dynamics for Robustness against Multi-Turn Jailbreaking](https://arxiv.org/abs/2503.00187)\n- [DeTAM - ACL Anthology](https://aclanthology.org/2025.findings-acl.613/)\n- [ASGuard - OpenReview ICLR 2026](https://openreview.net/forum?id=wmiEXNEXPs)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Wan et al. \"Mitigating Conversational Inertia in Multi-Turn Agents\" arXiv:2602.03664](https://arxiv.org/abs/2602.03664) (ICML 2026): 提出 conversational inertia 概念和 CPL 方法。确认论文存在、已发表于 ICML 2026。关键细节验证：CPL 使用 LoRA rank-16 DPO beta=0.01，减少 diagonal attention 10%+。论文明确声明\"All attention heads are averaged to create a unified attention matrix\"——per-head decomposition 确实不存在。**但 CPL 仅在 agent 性能（ALFWorld, WebShop 等 8 个环境）上验证，从未评估安全性。**\n\n- [DETAM (Li et al.) arXiv:2504.13562](https://arxiv.org/abs/2504.13562) (ACL 2025 Findings): 确认存在。通过推理时注意力重分配（mask modification, beta=5.0）将 ASR 从 46% 降至 1.2%。确认仅限 single-turn。确认需要运行时识别 intent tokens。\n\n- [ASGuard (Park et al.) arXiv:2509.25843](https://arxiv.org/abs/2509.25843) (ICLR 2026): 确认存在。通过 EAP-IG 识别 vulnerable heads，channel-wise scaling vectors + preventative fine-tuning。确认针对 tense jailbreaking 等特定攻击类型，自述 \"efficacy hinges on localizable causal circuits\"。\n\n- [Johnson & Huo arXiv:2602.14370](https://arxiv.org/abs/2602.14370) (arXiv Feb 2026): 确认存在。提出 dot-product competition 的 tipping point n* 数学公式。但注意：该论文关注 edge AI 的 good-to-bad tipping，是偏理论/物理学视角的分析，并非专门针对 diagonal attention 或多轮安全。\n\n- [Deng et al. arXiv:2603.08234](https://arxiv.org/abs/2603.08234) (arXiv Mar 2026): 确认存在。分析 continuation vs. refusal heads 的竞争机制。提供了 safety heads (layers 25-27) vs. continuation heads (middle layers ~Layer 13) 的定位。\n\n- [AISA (Song et al.) arXiv:2602.13547](https://arxiv.org/abs/2602.13547) (arXiv Feb 2026): 确认存在。通过 spatiotemporal analysis 定位 safety heads，top-K=16 heads 达到 0.92 检测准确率。\n\n- [Zhou et al. arXiv:2410.13708](https://arxiv.org/abs/2410.13708) (ICLR 2025): 确认存在。Ships score（Safety Head ImPortant Score），Sahara 算法定位安全注意力头。\n\n- **直接竞争检索结果**：搜索 \"conversational inertia safety\" 未找到任何已有工作将 conversational inertia/CPL 与安全联系起来。该 gap 目前看是真实的。\n\n- 调研总结：多轮安全领域（攻防、机制分析、防御训练）和 attention-level 安全机制分析（safety heads, continuation heads, attention competition）是两个活跃但仍较独立的研究方向。Conversational inertia（Wan et al.）目前仅在 agent 性能维度被研究，尚无人将其连接到安全问题。本 proposal 试图搭建这座桥梁。\n\n\n【Trivial Alternative 检验】:\n\n**存在两个显著的 trivial alternative 威胁：**\n\n1. **逐轮 DETAM**：虽然 proposal 论证了 DETAM 在多轮场景下 \"intent tokens 不可定位\"，但这个论证是概念层面的，并未实证验证。一个更 trivial 的做法是：在每一轮都应用 DETAM（将当前轮的 user input 视为 intent），测试是否足够有效。如果逐轮 DETAM 已经很好地解决了多轮安全问题，那么 CPL 的增量价值就很小。Proposal 并未包含\"multi-turn DETAM\"作为 baseline。\n\n2. **直接在安全数据上做 DPO/SFT**：XGuard-Train SFT 作为 control 被包含了——但核心问题是：为什么一个 **不在安全数据上训练、仅在 agent 环境上训练** 的 discourse intervention (CPL) 会比 **直接在安全数据上训练** 的方法更好？如果 CPL 的安全提升不如 XGuard-Train（这是可能性最高的结果），那 proposal 的故事就变成了\"间接方法不如直接方法\"——虽然可以 publish 但 significance 大打折扣。\n\n**增量价值的核心依赖**：CPL 的独特价值必须来自\"不用安全标注数据就能提升安全性\"这个属性——即 unsupervised safety improvement via discourse training。这是有意义的，但需要 CPL 的效果足够大才能让审稿人信服这不只是噪声。\n\n\n【前提假设检验】:\n\n核心逻辑链存在 **三个关键未验证假设**：\n\n1. **Head Overlap 假设（最关键）**：整个\"attention capacity competition\"假设的前提是 diagonal attention heads 与 safety heads 在某种程度上重叠（或至少在相同 layer 竞争）。Proposal 正确地在 Phase 0.5 测试这个假设——但如果 overlap 极低（Level 3），整个 softmax zero-sum 竞争机制就不成立，论文的理论叙事从\"attention competition\"退化为\"representation drift\"，novelty 大幅下降（representation drift 已被 X-Boundary 研究过）。\n\n2. **CPL 效果迁移假设**：CPL 在 AgentGym 环境（ALFWorld, WebShop 等）上训练和验证。假设它学到的 attention 变化能迁移到完全不同的安全评估场景（MT-AgentRisk, 恶意多轮对话）。这个迁移并非显然——CPL 训练的 preference pairs 来自 agent 任务的 long-context vs. short-context，与安全场景的分布可能相差很大。\n\n3. **因果方向假设**：论文假设 \"diagonal attention → 安全下降\" 是因果关系。但同样可能的替代解释是：多轮对话本身增加了复杂性/context length，导致 diagonal attention 和安全下降 **同时发生但无因果关系**（confounded by conversation length/complexity）。CPL 减少 diagonal attention 时，如果安全确实提升，还需要排除 CPL 同时引入的其他变化（如 response style changes、length changes 等）。Proposal 包含了 response-length control，但未控制所有可能的 confounds。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   - **确认的真实 novelty delta**：(a) 首次将 conversational inertia 连接到 multi-turn safety——搜索确认此 gap 真实存在；(b) 首个 per-head diagonal attention decomposition（Wan et al. 明确只做 aggregate-level averaging）；(c) 三种 safety head 定位方法的对比研究。\n   - **Novelty 的局限**：核心实验本质上是\"将一个已有方法（CPL）应用到一个新评估维度（安全）\"——这是 transfer/application study 而非新方法提出。三级竞争假说是理论贡献，但它尚未被验证，如果 Phase 0.5 结果不支持 Level 1/2，这个贡献就变成了一个被否决的假设。方法论上未提出新技术（CPL 来自 Wan et al.，Ships 来自 Zhou et al.，DETAM sensitivity 来自 Li et al.，AISA 来自 Song et al.）——所有分析工具都是现成的。\n   - **与最近工作的对比**：无直接竞争者（gap 真实），但核心贡献的 novelty 性质偏向 empirical study 而非 methodological innovation。审稿人可能认为这是一个 well-designed empirical investigation，但不是一个 novel approach。\n\n2. **Significance: 中** — \n   - **正面**：多轮安全是一个重要且活跃的问题（16% ASR increase documented by Yang et al.）。如果 CPL 确实能在不使用安全标注数据的情况下显著提升多轮安全，这对 alignment 领域有重要启示——意味着 discourse dynamics 是安全的一个被忽视的维度。\n   - **限制**：(a) 最可能的结果是 CPL 有 modest improvement（因为任何改变模型 attention 分布的训练都可能对安全有微弱影响），这不够 surprising 来支撑高 significance；(b) 如果 CPL 效果弱于直接安全训练方法（XGuard-Train, MUSE-D），实际应用价值有限——practitioners 会直接选择用安全数据训练；(c) 即使 positive，结论的可推广性受限于 CPL 这一特定方法——无法确定是 \"减少 inertia\" 还是 CPL 的某个副作用导致了安全提升。\n\n3. **Related Work: 强** — \n   - 调研确认 proposal 引用的所有关键论文（DETAM, ASGuard, Wan et al., Johnson & Huo, Deng et al., Zhou et al., AISA）都真实存在且描述准确。与现有工作的差异化定位清晰且诚实（DETAM: single-turn + runtime; ASGuard: circuit-specific; XGuard-Train: safety-labeled data）。文献覆盖面在本领域可能是最全面的——涵盖攻击、防御、机制分析、基准测试、理论框架等多个子方向。唯一可能的遗漏：未讨论\"逐轮 DETAM\"作为一个 straightforward extension 的可行性。\n\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \n- **Related Work (强)** 提供了坚实的基础，确保论文不会因文献遗漏被拒。\n- **Novelty (中)** 是主要限制因素——核心贡献是 \"apply existing method to new evaluation dimension\"，方法论创新不足。Per-head decomposition 和 triple triangulation 是 solid 但 incremental 的贡献。审稿人可能认为这更像一个 thorough empirical study 而非一个有 conceptual breakthrough 的论文。\n- **Significance (中)** 进一步限制上界——最可能的实验结果（CPL 有 modest effect but weaker than direct safety training）会让审稿人说 \"I would have guessed this\"。只有在 CPL 效果显著且机制分析清晰展示 head overlap 时，才能达到 surprising 的程度，但这需要多个未验证假设同时成立。\n- **概率上界受限于**：idea 本质是 application study + hypothesis testing，而非 method proposal。即使执行完美，核心发现的 surprise factor 有上限。\n- **概率下界受益于**：gap 真实、实验设计有 5 个 controls、有多个 standalone 贡献（per-head decomposition, head comparison）可以在 negative result 时提供 fallback value。\n\n【主要风险】: \n1. **\"I would have guessed this\" 风险**：无论 CPL 的安全效果是正向还是负向，审稿人都可能认为结果在预期范围内——正向（\"当然，改变 attention 分布会影响安全\"）或负向（\"当然，不在安全数据上训练不会提升安全\"）。缺乏一个 clear a priori reason to expect a *surprising* outcome。\n2. **Assumption Cascade 风险**：论文的核心叙事（attention competition hypothesis）依赖一连串未验证假设（head overlap → softmax competition → cumulative tipping → CPL as implicit DETAM）。任何一环断裂，理论框架就需要大幅调整，论文从\"验证了一个 elegant theory\"变成\"做了一个 comprehensive but inconclusive empirical study\"。\n```\n\nSources:\n- [Wan et al. - Mitigating Conversational Inertia in Multi-Turn Agents (ICML 2026)](https://arxiv.org/abs/2602.03664)\n- [DETAM - Li et al. (ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)\n- [ASGuard - Park et al. (ICLR 2026)](https://arxiv.org/abs/2509.25843)\n- [Johnson & Huo - Competition for attention predicts good-to-bad tipping in AI](https://arxiv.org/abs/2602.14370)\n- [Deng et al. - The Struggle Between Continuation and Refusal](https://arxiv.org/abs/2603.08234)\n- [AISA - Song et al.](https://arxiv.org/abs/2602.13547)\n- [Zhou et al. - On the Role of Attention Heads in LLM Safety (ICLR 2025)](https://arxiv.org/abs/2410.13708)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nThis is very relevant. Let me now compile my full evaluation based on all the research.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. Wan et al., \"Mitigating Conversational Inertia in Multi-Turn Agents\" (ICML 2026, arXiv:2602.03664):\n   - 确认存在且已发表。定义了 diagonal attention（conversational inertia），提出 CPL（LoRA rank-16 DPO, beta=0.01）。\n   - 仅在 8 个 agentic 环境上评估 task performance，**从未评估 safety**。Proposal 对该论文的描述准确。\n   - 关键细节确认：原文确实仅报告 aggregate-level attention（所有 head 平均），未做 per-head 分解。\n\n2. DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562):\n   - 确认存在。推理时修改 attention mask 放大 intent token 注意力，LLaMA-2 ASR 46%→1.2%。确实是 single-turn only。\n   - Proposal 描述准确。\n\n3. ASGuard (Park et al., ICLR 2026, arXiv:2509.25843):\n   - 确认存在且已发表在 ICLR 2026。使用 EAP-IG 定位 vulnerable heads，channel-wise scaling vectors，针对 tense jailbreaking。\n   - Proposal 描述准确，包括 Layer 13 的 4 个 vulnerable heads。\n\n4. Johnson & Huo, \"Competition for attention predicts good-to-bad tipping in AI\" (arXiv:2602.14370, Feb 2026):\n   - 确认存在。提出 dot-product attention 竞争导致 good-to-bad tipping point 的数学框架。\n   - 但注意：这是一篇 **physics 视角的理论论文**（来自 GWU 物理系），将 attention competition 建模为物理系统的相变。它提供的是一个 analogy/框架，而非 NLP 社区内的 empirical 发现。Proposal 将其作为核心理论支柱之一，但审稿人可能质疑其对 transformer 内部机制的直接适用性。\n\n5. Deng et al., \"The Struggle Between Continuation and Refusal\" (arXiv:2603.08234, Mar 2026):\n   - 确认存在。确实发现 continuation heads 与 safety heads 的竞争关系。Proposal 描述准确。\n\n6. AISA (Song et al., arXiv:2602.13547, Feb 2026):\n   - 确认存在。通过 spatiotemporal analysis 定位 safety heads，K=16 heads 达到 0.92 detection accuracy。Proposal 描述准确。\n\n7. Zhou et al., \"On the Role of Attention Heads in LLM Safety\" (ICLR 2025, arXiv:2410.13708):\n   - 确认存在，ICLR 2025 Oral。提出 Ships score。Proposal 描述准确。\n\n8. **未被引用的重要工作**:\n   - **\"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\"** (arXiv:2605.12922, May 13 2026): 直接研究多轮交互中 attention 如何逐渐失去对 goal-defining tokens 的访问能力。提出 Goal Accessibility Ratio (GAR)，发现不同架构的 failure mode 不同，layer range 从 2 到 27。这与 proposal 的 \"attention capacity competition\" 高度相关——该论文提供了多轮 attention 衰减的独立证据，且研究 attention 在残差流中的持久性，直接相关于 proposal 的 Level 3 hypothesis。发表于 2026 年 5 月，proposal 可能来不及引用。\n\n9. **调研总结**: 该领域正处于一个活跃的交叉点：多轮安全（MUSE-D, XGuard-Train, X-Boundary, MTSA）、attention 机制解释（safety heads, continuation heads, 竞争理论）、discourse dynamics（conversational inertia）。这三条线确实尚未被交叉——\"用 discourse-level 训练干预来改善 safety\"确实是一个未被测试的桥梁。但该桥梁的 insight depth 存疑：它更像是一个自然的 \"apply X to Y\" 连接，而非一个深刻的反直觉发现。\n\n\n【Trivial Alternative 检验】:\n\n存在两个层次的 trivial alternative 威胁：\n\n(1) **直接安全训练 baseline**: XGuard-Train SFT 已经在 Llama-3.1-8B 和 Qwen-2.5-7B 上实现了高达 48.3% 的 vulnerability reduction，MTSA 将 ASR 从 74.5% 降到 23.5%，X-Boundary 将 ASR 降到 16-25%。如果 CPL 的 safety improvement 弱于或可比于这些专门为 safety 设计的方法，那么\"通过 discourse 训练间接改善 safety\"的 story 就缺乏实际意义——审稿人会问 \"why not just train on safety data directly?\"\n\nProposal 的回应是\"CPL 不用 safety-labeled data\"，但这个优势需要 CPL 在 safety 上至少达到 comparable 水平才有说服力。如果 CPL 显著弱于 XGuard-SFT，那么 \"discourse intervention can help safety\" 是一个有趣但 marginal 的发现。\n\n(2) **Response quality confound**: CPL 的核心效果是让模型\"less inertial\"——即输出更少地重复/模仿之前的 pattern。更高质量、更 contextual 的回复自然倾向于更安全，因为 unsafe 回复往往是模型被 primed 后\"顺着说\"的结果。如果 CPL 的 safety improvement 完全可以被\"回复质量普遍提升\"解释（而非 attention competition 机制），那么 mechanistic 贡献就被架空了。Proposal 设计了 length control，但 length 不等于 quality——更难控制的是 \"CPL 让模型更 'thoughtful' in general\" 这一全局效应。\n\n**增量价值判断**: 如果 Phase 0.5 显示 diagonal attention heads 与 safety heads 高度重叠（Level 1），且 CPL 确实在这些 specific heads 上改变了 attention distribution，那么 mechanistic story 有实质内容。但如果是 Level 3（low overlap），整个 \"attention competition\" 叙事就弱化为 \"representation-level 的模糊改善\"，与 X-Boundary 等工作的差异化不明显。\n\n\n【前提假设检验】:\n\n核心逻辑链: diagonal attention (inertia) → softmax zero-sum competition with safety attention → reduced safety → CPL reduces inertia → safety improves\n\n**未经验证的关键假设**:\n\n(A) **\"Diagonal attention 与 safety attention 在 softmax 层面竞争\"**: 这是整个 hypothesis 的核心前提。Softmax 的 zero-sum 约束确实存在，但只在 **单个 head 内** 成立。Proposal 的 Level 1 hypothesis 要求 inertia 和 safety 发生在同一些 heads 中——这是一个 empirical question（Phase 0.5 的目标），但如果答案是 no（只有 Level 2 或 Level 3），整个 \"softmax zero-sum competition\" 叙事的直接性就大大减弱。\n- Level 2（same layer, different heads）的竞争通过 residual stream 间接发生，机制更复杂、更难验证\n- Level 3（different layers）的竞争更像是\"一般性的 representation drift\"，这几乎无法与 \"attention competition\" 区分开来\n\n(B) **\"Conversational inertia 是多轮安全退化的因果驱动力，而非伴随现象\"**: Proposal 引用 ASJA（attention dispersion 与 ASR 的相关性）和 Johnson & Huo（tipping point 理论），但这些只建立了相关性/理论可能性。一个替代解释是：多轮安全退化主要由 **alignment tax exhaustion**（长对话中 alignment 信号衰减）驱动，diagonal attention 只是长对话的一个 epiphenomenon。CPL 可能改善 safety 不是因为减少了 inertia 对 safety heads 的竞争，而是因为 DPO 训练附带增强了模型对 context 的审慎处理。\n\n(C) **\"CPL 的效果可以迁移到 safety 域\"**: CPL 在 agentic task performance 上有效，但 agentic environments（ALFWorld, WebShop 等）与 safety scenarios（jailbreak resistance）的 attention dynamics 可能有根本差异。在 agentic 环境中，\"减少 inertia\" 意味着 \"不重复之前低效的 action patterns\"；在 safety 场景中，模型需要的是 \"即使在长对话 context 下也 maintain refusal capability\"。这两种 \"不被之前的 output 牵着走\" 是否走同一条 attention pathway，并不显然。\n\n(D) **Johnson & Huo 的 tipping point 理论直接适用于 transformer 内部**: 该论文来自物理系，提供的是 dot-product attention competition 的数学抽象。但 transformer 的 multi-head, multi-layer 架构比该理论的假设复杂得多——tipping point n* 的计算假设了一个简化的 attention competition 模型，真实 transformer 中是否出现类似的相变行为并未被验证。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中**\n   - 正面：CPL → safety 的桥梁确实无人测试过；per-head diagonal attention 分解是一个真实的、Wan et al. 明确留下的空白；triple-method safety head identification comparison 是一个有价值的方法论贡献。\n   - 局限：核心 idea 本质是 \"apply technique A (CPL) to domain B (safety)\" 的 bridge study，conceptual leap 有限。\"discourse dynamics 影响 safety\" 这个 high-level insight 并不反直觉——Deng et al. (2603.08234) 已经证明 continuation heads 与 safety heads 竞争，ASJA (AAAI 2025) 已经证明 attention dispersion 影响 safety，\"When Attention Closes\" (2605.12922) 独立发现多轮 attention 衰减。Proposal 的增量是\"用 CPL 这个特定工具测试\"，而非\"提出这个概念\"。\n   - 与最近工作的距离：与 \"When Attention Closes\" (May 2026) 有显著概念重叠——该论文也研究多轮交互中 attention 如何逐步失去对关键 token 的访问，用 GAR 量化这一过程，且同样考虑了 residual stream 中信息是否持久。Proposal 需要明确区分。\n\n2. **Significance: 中**\n   - 正面：多轮安全是 NLP/AI safety 领域的重要问题（16% ASR increase, MTSA 显示 round 5 peak attack）；理解 discourse dynamics 与 safety 的因果关系有理论价值；如果 CPL 确实能\"免费\"改善 safety（无需 safety-labeled data），这对实践有意义。\n   - 局限：**核心发现的 surprise factor 有限**。如果 CPL 改善了 safety → \"训练模型更好地处理 context 也改善了 safety\"，审稿人可能说 \"I would have guessed this\"。如果 CPL 没改善 safety → 负面结果 + 分析性贡献。两种结果都不是 \"surprising, not what I expected\" 级别。真正的 surprise 需要：(a) CPL 在 safety 上超过专门的 safety training（这非常 unlikely），或 (b) 发现一个非常精确的 mechanistic 联系（如 Level 1 overlap >50%），但这是 empirical question 而非 idea 的内在 significance。\n   - 另一个 significance 限制：即使所有 hypotheses 都得到验证，practical takeaway 是什么？\"在部署时先跑一轮 CPL 可以改善 safety\"——但工程上人们更可能直接用 safety training。Mechanistic 理解有学术价值，但 impact scope 主要限于 safety interpretability 子社区。\n\n3. **Related Work: 强**\n   - 极其全面的 literature coverage：涵盖了 attention 机制（DETAM, ASGuard, AISA, Zhou et al., Depth Charge, Attention Eclipse）、多轮安全（MUSE-D, XGuard-Train, X-Boundary, MTSA, MT-AgentRisk, OpenAgentSafety）、理论框架（Johnson & Huo）、mechanistic interpretability（Deng et al., safety layers, refusal direction）。\n   - 差异化定位清晰：明确指出 DETAM 的 single-turn 限制、ASGuard 的 circuit-specific 限制、现有安全训练方法的 \"safety-labeled data\" 依赖。\n   - 唯一缺失：**\"When Attention Closes\" (arXiv:2605.12922, May 2026)** ——该论文高度相关（多轮 attention 衰减、GAR 指标、residual stream 分析），应当被引用和差异化。但考虑到该论文发表于 May 13, 2026，可能晚于 proposal 撰写时间，这不是严重疏漏。\n\n\n【概率估计】: 22% - 32%，中位 27%\n\n【估计理由】:\n- Novelty 为\"中\"（有真实的 novelty delta，但 conceptual leap 有限，核心是 bridge study）限制了上界在 ~35% 以下\n- Significance 为\"中\"（无论正面还是负面结果，surprise factor 都有限）进一步将中位数锚定在 25-30%\n- Related Work 为\"强\"（但 related work 的完备性是基础素养而非加分项，不提升 idea 质量上限）\n- 三维综合：idea 方向正确、有真实 gap、但核心发现如果 positive 审稿人大概率会说 \"I would have guessed this\"——这正好落在 25-35% 区间\n- 上界被 significance 限制：即使 execution 完美，idea 的上限取决于 \"CPL 改善 safety 是否 surprising\"，这个 bar 较难跨过\n- 下界被 related work 和 novelty 支撑：per-head decomposition、triple-method comparison、confound-controlled design 提供了实质性的分析贡献，即使主要 hypothesis 不成立也有 fallback value\n\n【主要风险】:\n1. **\"So what\" 风险**: 如果 CPL 确实改善了 safety，审稿人可能认为这是 \"general model improvement helps safety\" 的一个 instance，而非 attention competition mechanism 的特定验证——即 positive result 但 mechanistic claim 不被信服，导致论文贡献降级为 \"another safety training method\"，而在这个赛道上 CPL 不如专门的 safety training 有竞争力。\n2. **前提假设链断裂风险**: 如果 Phase 0.5 显示 diagonal attention heads 与 safety heads 低重叠（Level 3），核心 \"attention capacity competition\" 叙事的直接性严重削弱，论文需要 pivot 到更弱的 \"representation-level\" story，与 X-Boundary (EMNLP 2025) 的 framing 趋近，差异化空间被压缩。\n```\n\nSources:\n- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026)](https://arxiv.org/abs/2602.03664)\n- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)\n- [ASGuard: Activation-Scaling Guard (ICLR 2026)](https://arxiv.org/abs/2509.25843)\n- [Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, 2026)](https://arxiv.org/abs/2602.14370)\n- [The Struggle Between Continuation and Refusal (Deng et al., 2026)](https://arxiv.org/abs/2603.08234)\n- [AISA: Awakening Intrinsic Safety Awareness (Song et al., 2026)](https://arxiv.org/abs/2602.13547)\n- [On the Role of Attention Heads in LLM Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)\n- [When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction (May 2026)](https://arxiv.org/abs/2605.12922)\n- [MTSA: Multi-turn Safety Alignment (ACL 2025)](https://arxiv.org/abs/2505.17147)\n- [X-Boundary (EMNLP 2025)](https://arxiv.org/abs/2502.09990)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypothesis\n\n## Description\nThis project conducts the first controlled interventional study testing whether mitigating conversational inertia — diagonal attention to previous outputs (Wan et al., ICML 2026) — causally reduces multi-turn safety erosion, organized around a refined three-level 'attention capacity competition hypothesis.' We build on DETAM's proof that inference-time attention reallocation improves safety (ASR 46%→1.2%) and ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities, testing whether CPL achieves broad attention reallocation through untargeted discourse training — addressing the progressive multi-turn erosion that DETAM (single-turn, requires runtime intent localization) and ASGuard (targets specific localizable circuits) structurally cannot. In multi-turn crescendo attacks, malicious intent is distributed across turns, making DETAM's intent-token identification ill-defined; CPL instead reduces the cumulative inertia that pushes systems past Johnson & Huo's tipping point. A novel Phase 0.5 provides the first per-head decomposition of diagonal attention (Wan et al. explicitly averages all heads) and measures overlap with safety-critical heads using triple triangulation (Ships score, DETAM sensitivity, AISA spatiotemporal analysis), cross-validated against published head sets (Zhou et al., Depth Charge, ASGuard — whose 4 Layer-13 vulnerable heads independently corroborate the continuation-safety nexus). Our five-phase causal design tests CPL against five confound controls including XGuard-Train SFT at both published and CPL-matched ranks. Mechanistic verification tests whether CPL achieves 'implicit DETAM' (same heads, same direction) and 'implicit circuit modification' (affecting ASGuard's identified vulnerable heads without targeting them). The study is designed for informative outcomes at all three competition levels, with the per-head diagonal attention decomposition, triple-method head identification comparison, and DETAM/ASGuard mechanistic comparison constituting standalone contributions.\n\n## Core Problem\nMulti-turn agent interactions exhibit systematic safety degradation (16% higher attack success rates), and while recent work has identified attention-level mechanisms — attention dispersion on safety keywords (ASJA, AAAI 2025), competition between safety and continuation heads (Deng et al., 2026), and attention reallocation as a defense (DETAM, ACL 2025 Findings) — and developed multi-turn safety defenses (MUSE-D turn-level DPO, EMNLP 2025; XGuard-Train SFT, COLM 2025; X-Boundary representation boundaries, EMNLP 2025; MTSA RL-based alignment, ACL 2025), and even training-time attention head interventions for specific vulnerability types (ASGuard circuit-targeted scaling, ICLR 2026), these studies are either attack-oriented, single-turn, operate at inference time, target specific localizable vulnerabilities, or train directly on safety-labeled data without testing whether discourse-level mechanisms causally drive safety erosion. Critically, DETAM (Li et al., ACL 2025 Findings) demonstrates that simply reallocating attention from attack tokens toward safety-relevant tokens at inference time — without any weight changes — reduces ASR from 46% to 1.2% on LLaMA-2, providing the strongest existing evidence that attention redistribution causally improves safety. Yet DETAM requires explicit identification of 'intent tokens' at runtime and operates only in single-turn settings — in multi-turn crescendo attacks where malicious intent is progressively distributed across turns, the notion of localizable 'intent tokens' breaks down fundamentally. ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant heads is feasible via circuit-targeted scaling vectors, but its efficacy 'hinges on localizable causal circuits' for specific attack types (tense jailbreaking) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits. No work has tested whether a training-time discourse intervention (reducing conversational inertia) achieves broad attention reallocation indirectly, nor whether the specific attention heads carrying diagonal inertia patterns overlap with safety-critical heads — a prerequisite for the softmax zero-sum competition mechanism to operate at the head level. Notably, the only characterization of diagonal attention (Wan et al., ICML 2026) reports aggregate-level patterns averaged across all heads; no per-head decomposition exists, leaving the head-level competition question empirically open. Additionally, the response-length confound in DPO-based interventions has never been explicitly controlled for in safety evaluations of discourse-level interventions.\n\n## Opportunity\nSix independent research threads have converged to make a controlled causal study newly feasible: (1) Conversational Inertia (Wan et al., ICML 2026) identifies diagonal attention where the i-th token attends to the i-th previous output position and provides Context Preference Learning (CPL) as a parameter-efficient intervention (0.4% params, LoRA rank-16 DPO with beta=0.01), validated on Qwen3-8B and Llama 3.1-8B-Instruct across eight agentic environments but never evaluated for safety — crucially, the diagonal attention pattern is characterized only at the aggregate level (averaged across all heads), so the per-head distribution remains unknown; (2) DETAM (Li et al., ACL 2025 Findings) provides direct causal evidence that attention reallocation toward safety-relevant tokens improves safety — reducing ASR by 97%+ without weight modification — but requires runtime intent token identification and is single-turn only, creating a fundamental limitation for multi-turn settings where intent is distributed across turns; (3) ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant attention heads is feasible via circuit-targeted channel-wise scaling vectors and preventative fine-tuning — crucially, ASGuard identifies 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30), exactly where Deng et al. find continuation heads, providing independent corroboration that Layer 13 is a nexus of safety-relevant competition — but ASGuard targets specific localizable vulnerability circuits (tense jailbreaking) rather than discourse-level dynamics; (4) Multi-turn safety erosion is now well-benchmarked via MT-AgentRisk (365 tasks, 5 tools, avg 3.19 turns) with ToolShield as a defense baseline, and supplemented by OpenAgentSafety (ICLR 2026, 356 real-tool tasks with multi-turn multi-user dynamics); (5) Multi-turn safety training has mature baselines spanning multiple paradigms: XGuard-Train SFT (COLM 2025, up to 48.3% vulnerability reduction), MUSE-D turn-level DPO (EMNLP 2025, 24% ASR reduction), X-Boundary representation-level boundaries (EMNLP 2025, ASR reduction to 16-25%), and MTSA RL with future rewards (ACL 2025, ASR 74.5% to 23.5%) — but all train directly on safety-labeled data; (6) AISA (Song et al., arXiv:2602.13547) provides a third complementary method for localizing safety-critical attention heads via spatiotemporal analysis — identifying that safety-discriminative signals concentrate in middle-layer head outputs with K=16 heads achieving 0.92 detection accuracy — enabling methodological triangulation in our head overlap analysis. This six-thread convergence, combined with Johnson & Huo's (2026) formalization of attention competition tipping points and the layered distribution of safety mechanisms across layers 2-27, motivates a three-level attention capacity competition hypothesis testable through a novel Phase 0.5 head overlap analysis.\n\n## Landscape\n**Attention reallocation defenses:** DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) is the most directly relevant inference-time prior work. It identifies attention heads sensitive to jailbreaks by computing attention score differences between successful and unsuccessful defenses (threshold alpha: 0.1 for LLaMA-2, 0.03 for Vicuna). During inference, it modifies the causal mask matrix by multiplying mask values at intent token positions by beta=5.0, amplifying attention to the user's core intention. DETAM reduces average ASR from 46.0% to 1.2% on LLaMA-2-7b-chat and from 81.8% to 4.0% on Vicuna-13b-v1.5. Cross-model transferability: sensitive heads from LLaMA-2 transferred to Meta-LLaMA-3 achieve 4% ASR vs. 96% vanilla. However, DETAM has three fundamental limitations for multi-turn agent settings: (a) it requires runtime identification of 'intent tokens' — in multi-turn crescendo attacks (Russinovich et al., USENIX Security 2025) where harmful intent is progressively distributed across turns, no single set of tokens constitutes 'the intent,' making DETAM's token-level localization fundamentally ill-defined; (b) it is tested only in single-turn settings and cannot address the cumulative attention shift across turns that Johnson & Huo's tipping point theory predicts; (c) it imposes per-turn computational overhead for mask modification in each forward pass across all turns of agent interaction. Our study tests whether CPL achieves DETAM-like attention redistribution persistently through training, addressing a failure mode DETAM structurally cannot: the gradual accumulation of continuation pressure across turns that progressively dilutes safety attention below the tipping point. **Training-time attention head intervention:** ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) is the closest existing work to training-time attention head modification for safety. It uses Edge Attribution Patching with Integrated Gradients (EAP-IG) to identify attention heads causally linked to specific jailbreaking vulnerabilities, trains channel-wise activation scaling vectors (s_j ∈ R^{d_head}, applied via Hadamard product H'_{l,j} = H_{l,j} ⊙ s_j) on identified heads, and applies preventative fine-tuning with scaling vectors frozen. On tense jailbreaking, ASGuard reduces ASR from 42% to 8% on Llama-3.1-8B and 51% to 8% on Qwen2.5-7B, achieving Pareto-optimal safety-utility balance. Critically, ASGuard identifies 11 vulnerable heads in Llama-3.1-8B, of which 4 are at Layer 13 (L13H8, L13H18, L13H25, L13H30) — exactly where Deng et al. find continuation heads — providing independent corroboration that Layer 13 is a nexus of safety-relevant attention competition. However, ASGuard differs from our approach in three key ways: (a) it targets specific, localizable vulnerability circuits ('efficacy hinges on localizable causal circuits' — their Limitations, Section 7) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits, as the failure is progressive rather than circuit-specific; (b) it surgically fixes known attack types (tense jailbreaking, GCG, LogiBreak) one at a time, whereas CPL is an untargeted discourse intervention testing whether reducing general inertia achieves broad safety benefits; (c) it is single-turn only. ASGuard's success actually supports a key premise of our hypothesis: training-time modification of attention heads CAN improve safety. Our study tests whether indirect, untargeted discourse training achieves what targeted head intervention achieves — and whether it generalizes to the multi-turn progressive erosion that targeted approaches cannot address. **Safety head localization methods:** AISA (Song et al., arXiv:2602.13547) provides a third complementary approach to localizing safety-critical heads via spatiotemporal analysis — large-scale linear probing across 15 positions per layer identifies that attention head outputs demonstrate superior safety separability, with top-K=16 heads (concentrated in middle layers) achieving 0.92 detection accuracy and O(1) runtime overhead. AISA's finding that safety heads cluster in middle layers in standard models but shift toward higher layers in strongly safety-aligned models adds nuance to the competition hypothesis — the relevant layers may differ by alignment strength. **Attack-side mechanisms:** Du et al. (ASJA, AAAI 2025) show that successful multi-turn jailbreaks correlate with attention dispersion away from safety keywords (p=4.38e-07), achieving 44.9% higher ASR. Deng et al. (arXiv:2603.08234) identify competing safety and continuation attention heads — safety heads concentrated in layers 25-27, continuation heads in middle layers (~Layer 13) — whose antagonistic interaction determines jailbreak success. Notably, continuation heads at Layer 13 occupy the same layer range as both induction/copying mechanisms AND ASGuard's identified vulnerable heads, suggesting this layer is a critical nexus where diagonal attention patterns, continuation signals, and safety vulnerability converge. Depth Charge (Wu et al., arXiv:2603.05772, March 2026) introduces SAHA using Ablation-Impact Ranking and Layer-Wise Perturbation, achieving 82-91% ASR, revealing layer-specific safety head concentrations (layer 7 for Llama 3.1-8B, layer 5 for Qwen 1.5-7B, head 31 universally important) and sharp threshold behavior. Attention Eclipse (Zaree et al., arXiv:2502.15334) achieves 91.2% ASR by manipulating attention to strengthen harmful content focus and weaken safety focus. **Attention competition theory:** Johnson & Huo (arXiv:2602.14370, Feb 2026) formalize the competition-for-attention mechanism mathematically, showing that dot-product competition creates dynamical tipping points (n*) where behavior transitions from safe to unsafe — providing the theoretical framework for why cumulative inertia across turns can push the system past a tipping point that single-turn defenses like DETAM cannot prevent. **Multi-turn safety benchmarking:** Yang et al. (arXiv 2026) document 16% average ASR increase on MT-AgentRisk and propose ToolShield (~30% ASR reduction). OpenAgentSafety (ICLR 2026) provides 356 multi-turn, multi-user tasks with real tools. Li et al. (STAR, arXiv:2603.15684) show monotonic drift from refusal representations. MultiBreak (arXiv:2605.01687) provides 10,389 multi-turn adversarial prompts. **Multi-turn safety defenses:** X-Teaming (COLM 2025, arXiv:2504.13203) introduces XGuard-Train, a 30K multi-turn safety training dataset. Models SFT-trained on a 14K subset with LoRA rank-8, lr=1e-4, 3 epochs achieve up to 48.3% vulnerability reduction on Llama-3.1-8B and Qwen-2.5-7B. MUSE-D (EMNLP 2025, arXiv:2509.14651) applies turn-level DPO achieving 24% ASR reduction. X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990) operates at the representation level, reducing multi-turn ASR from 58.5-76.0% to 16.0-25.0% while reducing over-refusal by ~20%. MTSA (Guo et al., ACL 2025, arXiv:2505.17147) performs RL with future rewards, reducing ASR from 74.5% to 23.5%, with the finding that maximum attack effectiveness peaks at round 5 — confirming multi-turn pressure accumulates through discourse dynamics. Agent Safety Alignment (Sha et al., arXiv:2507.08270) proposes unified sandboxed RL with benign/malicious/sensitive taxonomy. STREAM (arXiv:2506.00668) proposes safety reasoning moderator reducing ASR by 51.2%. TurnGate (arXiv:2605.05630) introduces turn-level harm detection. **Discourse dynamics:** Wan et al. (ICML 2026, arXiv:2602.03664; note: also submitted to ICLR 2026 as OpenReview #UubLs3lUfk, subsequently published in PMLR 306 at ICML 2026, Seoul, July 6-11) identify conversational inertia and propose CPL. The paper characterizes diagonal attention only at the aggregate level — explicitly stating 'All attention heads are averaged to create a unified attention matrix' and 'the trend of diagonal attention in the final layer is similar to other layers' — with no per-head decomposition. Code not released. **Safety attention head mechanisms:** Zhou et al. (ICLR 2025, arXiv:2410.13708) show the single most critical head in Llama-2-7B-Chat is Head (2, 26) at Layer 2. Wei et al. identify safety layers at layers 9-14. The refusal direction (Arditi et al.) is strongest around layer 15. Safety Alignment Should Be Made More Than Just A Few Attention Heads (arXiv:2508.19697) proposes distributed safety head training. **Safety persistence:** Plaut (arXiv:2603.02229) shows LoRA safety DPO persists with 90-94% retention, Pareto frontier R-squared=0.77, slope=-0.83. **DPO length bias:** Park et al. (2024) and Meng et al. (2024) document hidden length dependence. **Gap:** Despite convergent progress on inference-time attention reallocation (DETAM), training-time targeted head intervention (ASGuard), training-time safety defenses (XGuard-Train, MUSE-D, X-Boundary, MTSA), safety head localization (Zhou et al., AISA, Depth Charge), attention competition theory (Johnson & Huo), and discourse dynamics (conversational inertia), no work has: (a) tested whether a training-time discourse intervention achieves broad DETAM-like attention reallocation and causally reduces safety erosion in multi-turn settings — addressing the progressive accumulation that both DETAM (single-turn only) and ASGuard (circuit-specific only) cannot; (b) provided a per-head decomposition of diagonal attention to determine whether inertia heads overlap with safety heads; (c) compared discourse-targeted vs. safety-targeted training under matched parameter budgets; or (d) controlled for DPO response-length confounds in discourse-safety evaluations.\n\n## Approach\nWe run a five-phase causal study on MT-AgentRisk (primary) and OpenAgentSafety (secondary) benchmarks using Qwen3-8B and Llama 3.1-8B-Instruct, organized around the 'attention capacity competition hypothesis' and motivated by a specific gap that neither DETAM nor ASGuard can address: progressive multi-turn safety erosion through cumulative discourse dynamics.\n\n**Why Training-Time Discourse Intervention? The Multi-Turn Intent Distribution Problem.** DETAM achieves 97%+ ASR reduction in single-turn settings at zero training cost — but it requires identifying 'intent tokens' at runtime. In multi-turn crescendo attacks where harmful intent is progressively distributed across 3-10 turns (MTSA finds peak attack at round 5), no single set of tokens constitutes 'the intent.' The malicious instruction at turn 7 is only harmful in the context of the innocuous-seeming turns 1-6 that established the frame. DETAM cannot solve this because its mechanism — amplifying attention to intent tokens in sensitive heads — presupposes that intent is localizable within a single turn. ASGuard demonstrates training-time head modification is feasible but targets specific localizable circuits (tense jailbreaking), and its own Limitations section notes 'efficacy hinges on localizable causal circuits.' Multi-turn safety erosion through cumulative inertia is NOT a localizable circuit — it's a progressive process where each turn incrementally shifts the attention distribution. CPL's advantage is that it operates at the discourse dynamics level: reducing the cumulative inertia that progressively dilutes safety attention across turns, without needing to identify which tokens are 'intent' tokens or which circuits carry a specific vulnerability. It addresses the ROOT CAUSE (attention inertia accumulation across turns) rather than the SYMPTOM (misallocated attention at any single turn). This is the failure mode that Johnson & Huo's tipping point theory predicts: gradual accumulation of continuation pressure pushes the system past n* — and the only way to prevent reaching the tipping point is to reduce the per-turn accumulation rate, which is exactly what CPL does.\n\n**The Attention Capacity Competition Hypothesis (Three-Level Framework):** We theorize that diagonal attention (the inertia mechanism) competes with safety-keyword attention at three distinct levels: **Level 1 (Head-level, strong form):** If diagonal attention and safety attention share the same heads, softmax's zero-sum constraint directly displaces safety-keyword attention. Given that safety heads span layers 2-27 and induction/copying mechanisms typically concentrate in middle layers, partial overlap is plausible. **Level 2 (Layer-level, medium form):** If diagonal and safety attention occupy different heads within the same or adjacent layers, competition occurs through the residual stream. This is supported by Deng et al.'s finding that continuation heads (Layer 13) antagonize safety heads (Layers 25-27), and strikingly corroborated by ASGuard's identification of 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30) — the same layer where continuation heads reside, independently confirming Layer 13 as a nexus of safety-relevant competition. **Level 3 (Representation-level, weak form):** Competition mediated through accumulated representation drift, validated by X-Boundary's success (ASR 58.5% to 16.5%). Phase 0.5 empirically determines which level(s) apply.\n\n**Phase 0 — CPL Acquisition/Reproduction + Baseline Preparation (weeks 1-3):** Contact Wan et al. for CPL checkpoints (ICML 2026 July 6-11). Simultaneously reproduce CPL using TRL DPOTrainer + PEFT: LoRA rank-16, alpha-16, 0.4% params, DPO with beta=0.01, sigmoid loss, 2 epochs, lr=5e-7, AdamW, 1000 preference pairs per environment. The training recipe maps directly to TRL v1.0+ (sigmoid loss is the default DPOConfig, all hyperparameters natively supported); the main reproduction risk is the preference pair construction pipeline (dual-rollout with long-context vs. short-context on AgentGym environments) rather than the training loop itself. Estimated: ~40 A100-hours per model. In parallel, prepare XGuard-Train SFT baselines: (a) LoRA rank-8 with lr=1e-4, 3 epochs (matching published configuration from X-Teaming, validated on Llama-3.1-8B and Qwen-2.5-7B); (b) LoRA rank-16 with CPL-matched hyperparameters for parameter-matched comparison. Construct extended-turn variants: prepend 4-6 benign tool-use turns to 50 representative MT-AgentRisk tasks.\n\n**Hard Go/No-Go Checkpoint at Week 3:** The project proceeds to Phase 0.5 only if ALL criteria are met: (1) AgentGym environment setup working for >=3 of 8 environments (prioritizing ALFWorld, WebShop, HotpotQA); (2) dual-rollout preference pair generation produces pairs where long-context trajectories show measurably higher diagonal attention scores than short-context trajectories (statistically significant at p<0.05 on at least 2 environments); (3) DPO training pipeline converges (decreasing loss, increasing reward margins over 2 epochs); (4) base model evaluation on >=2 environments matches Wan et al.'s published baselines within 1 SEM. **Fallback paths:** (a) environment failure: proceed with 2-3 most reliable environments; (b) inertia differential failure: pivot to correlational-only study (Phases 1 and 4 only); (c) training failure: debug 1 additional week — if still failing by week 4, pivot to 'DETAM in multi-turn settings' (extending DETAM's mechanism to MT-AgentRisk, testing whether Focus Loss intensifies across turns).\n\n**Phase 0.5 — Head Overlap Test and Per-Head Diagonal Attention Decomposition (weeks 3-4, ~20 A100-hours):** This phase provides the first per-head decomposition of diagonal attention patterns and tests the prerequisite assumption of the competition hypothesis. Using both base models on 50 MT-AgentRisk tasks: (a) **Novel per-head diagonal attention decomposition:** Compute diagonal attention scores per head (not just aggregate) using Wan et al.'s metric (attention between current output position i and previous assistant output position i +/- 5 tokens) — this is the first such decomposition, given that Wan et al. explicitly average all heads ('All attention heads are averaged to create a unified attention matrix'). Identify which heads carry the strongest diagonal patterns and their layer distribution. (b) **Safety head identification via triple triangulation:** Apply three complementary methods: (i) Ships score (Zhou et al., ICLR 2025) via KL divergence after head ablation; (ii) DETAM's sensitivity metric (attention score differences between successful/unsuccessful safety responses); (iii) AISA's spatiotemporal analysis — linear probing on head outputs at final structural tokens to identify safety-discriminative heads (K=16). Cross-validate against published localizations: Zhou et al.'s Head (2,26) for Llama-2-family; Depth Charge's layer-specific data (layer 7 for Llama 3.1-8B); ASGuard's EAP-IG identified heads (11 heads for Llama-3.1-8B including 4 at Layer 13). Using three independent methods plus cross-validation against three published head sets provides robust head identification. (c) **Overlap analysis:** Compute Jaccard index between top-k diagonal attention heads and top-k safety heads (k = 5, 10, 20, 50) with permutation tests. Also measure layer-level co-occurrence (same layer, different heads). Cross-reference against ASGuard's Layer 13 vulnerable heads — if diagonal attention heads concentrate at Layer 13, this would connect conversational inertia to the continuation-safety competition nexus identified by both Deng et al. and ASGuard independently. (d) **Level determination:** Level 1 (>30% head overlap) — proceed with strong per-head softmax hypothesis; Level 2 (same layers, <30% head overlap) — reformulate around residual stream competition, particularly the Layer 13 continuation-inertia-safety nexus; Level 3 (<10% overlap in both heads and layers) — reformulate around representation-level competition. Each determination shapes subsequent analysis. This phase costs ~20 A100-hours but de-risks the project and provides standalone novel contributions (first per-head diagonal attention map; first triple-method safety head identification comparison).\n\n**Phase 1 — Correlational with Attention Capacity Analysis (weeks 4-7):** Measure diagonal attention (per-head, informed by Phase 0.5) AND safety-keyword attention concentration at each turn on 365 MT-AgentRisk tasks and 50 extended-turn variants. Calibrate analysis to competition level from Phase 0.5. Fit mixed-effects regressions testing P1 (diagonal attention negatively correlates with safety attention at the operative level), controlling for turn position, task category, model, and response token count. Test Granger causality for temporal dynamics.\n\n**Phase 2 — Interventional with Confound Controls (weeks 7-11):** Apply CPL and re-evaluate on MT-AgentRisk. Five control conditions: (a) **Random-Preference LoRA** — shuffled preference labels, same architecture; (b) **Reversed-CPL** — prefer long-context over short-context; (c) **XGuard-Train SFT (rank-8)** — published configuration for validation against published results; (d) **XGuard-Train SFT (rank-16)** — CPL-matched parameters for direct paradigm comparison (discourse-targeted vs. safety-targeted training); (e) **Response-Length Analysis** — ASR stratified by length quartiles, per-100-token normalization, regression with length covariate (testing P3: CPL's safety effect, if any, is not explained by response-length changes). Frame CPL's effect relative to both DETAM and ASGuard: test whether CPL affects the same heads DETAM identifies as sensitive and shifts attention in the same direction (implicit DETAM test), and whether it affects ASGuard's identified vulnerable heads at Layer 13 (implicit untargeted circuit modification test). Compare against ToolShield baseline and MUSE-D's published results.\n\n**Phase 3 — Autonomy Tax Audit (weeks 9-11, parallel):** Step-1 completion rate, cascade failure rate, end-to-end success, over-refusal. Report safety-competence Pareto frontier extending Plaut's analysis. Compare CPL's frontier position with X-Boundary's ~20% over-refusal reduction, ASGuard's Pareto-optimal balance, and XGuard-SFT's published results.\n\n**Phase 4 — Mechanistic Verification (weeks 10-14):** (a) SRI signal framework for step-wise refusal dynamics; (b) Head-level analysis extending Deng et al.'s safety-continuation head identification to multi-turn, calibrated by Phase 0.5 overlap findings — test whether CPL modulates the Layer 13 continuation vs. Layer 25-27 safety head balance across conversation turns; (c) **DETAM-informed analysis:** Apply DETAM's sensitivity metric to CPL-treated models — does CPL training shift attention in the same heads and direction that DETAM targets at inference time? If so, CPL achieves 'implicit DETAM' through discourse training, but persistently and without runtime intent localization; (d) **ASGuard-informed analysis:** Test whether CPL affects ASGuard's identified vulnerable heads (particularly the 4 at Layer 13) despite not targeting them — this would demonstrate that untargeted discourse training can modify the same heads that targeted circuit analysis identifies, but as a side effect of reducing general inertia rather than through explicit circuit surgery; (e) Level-appropriate analysis: Level 2 — residual stream composition analysis at shared layers; Level 3 — representation trajectory analysis following X-Boundary's framework.\n\n**Secondary Evaluation — OpenAgentSafety (weeks 12-14):** Best-performing config and XGuard-SFT on a subset for ecological validity.\n\n**Null-Result Framing Strategy:** (1) First per-head decomposition of diagonal attention patterns and their overlap (or non-overlap) with safety heads — novel regardless of CPL results; (2) First triple-method safety head identification comparison (Ships + DETAM sensitivity + AISA spatiotemporal), cross-validated against three published head sets (Zhou et al., Depth Charge, ASGuard); (3) Empirical evidence for or against the three-level competition hierarchy; (4) First confound-controlled causal framework for discourse-safety evaluation; (5) First discourse-targeted vs. safety-targeted training comparison under matched parameters; (6) First multi-turn extension of DETAM's Focus Loss analysis; (7) Empirical test of whether CPL-like untargeted training affects the same heads as ASGuard's targeted circuit intervention.\n\n**Extended-Turn Variant Validity (Limitation):** Acknowledged with mitigations: OpenAgentSafety for ecological validity, attention pattern validation, conservative amplification framing.\n\nAll primary experiments use MT-AgentRisk (365 tasks), ToolShield codebase (GitHub: CHATS-lab/ToolShield), XGuard-Train (HuggingFace: marslabucla/XGuard-Train), and the CPL training recipe from Wan et al. (ICML 2026).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '720-900 A100-hours (CPL reproduction 2 models ~80h, XGuard-SFT rank-8 + rank-16 training 2 models ~60h, 2 control LoRAs for 2 models ~80h, Phase 0.5 head overlap test with AISA probing ~25h, MT-AgentRisk evaluation across 6 conditions x 2 models ~240h, extended-turn evaluation ~40h, OpenAgentSafety subset ~60h, SRI signal analysis ~30h, attention analysis including per-head diagonal decomposition + DETAM-informed + ASGuard-informed metrics ~85h, head-level safety-continuation analysis ~40h, response-length analysis ~10h)', 'timeline': '15-17 weeks (3 weeks Phase 0 + go/no-go, 1 week Phase 0.5, 3 weeks Phase 1, 4 weeks Phase 2 + Phase 3 parallel, 4 weeks Phase 4 + OpenAgentSafety, 3 weeks writing; comfortable for ICLR 2027)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': '720-900 A100-hours', 'timeline': '13-15 weeks (Claude accelerates CPL reproduction, Phase 0.5 triple-method pipeline, DETAM/ASGuard comparison metrics, statistical analysis)', 'claude_api_cost': '$300-450 (CPL reproduction, per-head diagonal decomposition, triple-method head overlap analysis, DETAM/ASGuard-informed metrics, experiment orchestration, statistical modeling)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}, 'auto_research': {'gpu_hours': '920-1140 A100-hours (additional automated sweeps, full OpenAgentSafety evaluation, extended ablation across competition levels, comprehensive per-head analysis with triple methods)', 'timeline': '9-11 weeks (parallelized execution, automated Phase 0.5 -> Phase 1 pipeline)', 'claude_api_cost': '$600-850 (end-to-end orchestration including CPL reproduction, triple-method head analysis, DETAM/ASGuard comparison, control sweeps, result interpretation, draft generation)', 'estimated_gpu_cost': '$1380-1710 at $1.50/A100-hr spot pricing', 'speed_bottleneck': 'Sequential multi-turn interaction generation; 12 model configurations (2 models x 6 conditions); Phase 0.5 is a serial dependency before Phase 1; triple-method safety head analysis computationally intensive'}}\n\n## Inspired By\nField guide Section 4 (cascading failures, production gap) + Section 5.2 (error propagation as primary bottleneck). Key insight: DETAM's demonstration that inference-time attention reallocation dramatically improves safety (ASR 46% to 1.2%) establishes the empirical foundation for our hypothesis — if explicitly redirecting attention works, does implicit redirection via discourse training also work? ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities raises the natural question: can untargeted discourse training achieve what targeted circuit intervention achieves, but for the progressive multi-turn erosion that circuit-based approaches cannot address? The three-level competition hierarchy was motivated by the finding that Wan et al. only characterizes diagonal attention at the aggregate level (explicitly averaging all heads into a unified matrix) and that safety heads span multiple layer ranges (L2, L9-14, L25-27), while continuation heads at Layer 13 overlap with both induction/copying head territory and ASGuard's identified vulnerable heads (4 of 11 Llama-3.1-8B vulnerable heads are at L13). Johnson & Huo's (2026) formalization of attention competition tipping points provides the theoretical framework for why cumulative discourse inertia can push multi-turn interactions past a safety threshold that per-turn defenses cannot prevent. The reviewer's observation about per-head specificity led to Phase 0.5, which provides the first per-head decomposition of diagonal attention — a novel contribution regardless of results. AISA's spatiotemporal analysis provides methodological triangulation for safety head identification, strengthening Phase 0.5's robustness.\n\n## Target Venues\n- ICLR 2027 (abstract September 19 2026, full paper September 24 2026 [estimated] — primary target, ~18 weeks from project start, comfortable timeline with 3+ weeks buffer including Phase 0.5)\n- AAAI 2027 (abstract July 21 2026, full paper July 28 2026 — stretch target, ~10 weeks; feasible only if CPL checkpoints obtained by week 2, Phase 0.5 shows Level 1 or 2 overlap, and Phase 1 results are clean)\n\n## Key References\n- DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings, arXiv:2504.13562)\n- ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026, arXiv:2509.25843)\n- AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks (Song et al., arXiv:2602.13547, Feb 2026)\n- Multi-Turn Jailbreaking Large Language Models via Attention Shifting (ASJA, AAAI 2025)\n- Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026, arXiv:2602.03664)\n- Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents (Yang et al., arXiv 2026)\n- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents (COLM 2025, arXiv:2504.13203)\n- MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety (EMNLP 2025, arXiv:2509.14651)\n- X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability (Lu et al., EMNLP 2025, arXiv:2502.09990)\n- MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming (Guo et al., ACL 2025, arXiv:2505.17147)\n- Agent Safety Alignment via Reinforcement Learning (Sha et al., arXiv:2507.08270)\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut, arXiv:2603.02229, March 2026)\n- The Struggle Between Continuation and Refusal (Deng et al., arXiv:2603.08234, Mar 2026)\n- The Autonomy Tax: Defense Training Breaks LLM Agents (Li & Zhao, arXiv:2603.19423, Mar 2026)\n- On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025, arXiv:2410.13708)\n- Depth Charge: Jailbreak Large Language Models from Deep Safety Attention Heads (Wu et al., arXiv:2603.05772, Mar 2026)\n- Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., arXiv:2508.19697, 2025)\n- Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, arXiv:2602.14370, Feb 2026)\n- Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment (Zaree et al., arXiv:2502.15334, Feb 2025)\n- Safety Layers in Aligned Large Language Models (Wei et al., arXiv:2408.17003, 2024)\n- Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., arXiv:2406.11717, 2024)\n- State-Dependent Safety Failures in Multi-Turn Language Model Interaction (STAR, arXiv:2603.15684, Mar 2026)\n- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026, arXiv:2507.06134)\n- One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue (TurnGate, arXiv:2605.05630, May 2026)\n- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv:2605.01687, May 2026)\n- STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (arXiv:2506.00668, May 2025)\n- Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions (arXiv 2026)\n- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2026)\n- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv 2025)\n- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction (arXiv 2026)\n- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv 2026)\n- Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction (arXiv 2026)\n- Asking Forever: Universal Activations Behind Turn Amplification (arXiv:2602.17778, Feb 2026)\n- Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models (arXiv:2602.02600, Feb 2026)\n- Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection (arXiv:2604.28129, Apr 2026)\n- Many-Turn Jailbreaking (arXiv:2508.06755, Aug 2025)\n- Disentangling Length from Quality in Direct Preference Optimization (Park et al., arXiv:2403.19159, 2024)\n- Length Desensitization in Direct Preference Optimization (Meng et al., arXiv:2409.06411, 2024)\n- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., USENIX Security 2025, arXiv:2404.01833)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:49:12.138Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:49:12.138Z",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:49:12.153Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make a well-grounded assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- [DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562)](https://arxiv.org/abs/2504.13562): 推理时注意力重分配防御。通过识别对越狱敏感的注意力头，运行时在 intent token 位置放大注意力（β=5.0），LLaMA-2 上 ASR 46%→1.2%。仅限单轮，需运行时识别 intent token。Proposal 将其作为"推理时注意力重分配有效"的因果证据基础，定位准确。
- [Wan et al. CPL (ICML 2026, arXiv:2602.03664)](https://arxiv.org/abs/2602.03664): 识别对话惯性（diagonal attention），提出 Context Preference Learning（LoRA rank-16 DPO, β=0.01），在 8 个 agentic 环境上验证。关键：对角注意力**仅在 aggregate 层面刻画**（显式说明"所有注意力头被平均"），**从未评估过安全性**。CPL 降低对角注意力 >10%，提升系统注意力。Proposal 的核心干预方法。
- [ASGuard (Park et al., ICLR 2026, arXiv:2509.25843)](https://arxiv.org/abs/2509.25843): 训练时电路层面注意力头修改。通过 EAP-IG 定位 tense jailbreaking 的脆弱注意力头，channel-wise scaling + preventative fine-tuning，ASR 42%→8%。识别 Llama-3.1-8B 中 11 个脆弱头（4 个在 Layer 13）。局限：依赖可定位的因果电路，针对特定攻击类型。
- [Deng et al. (arXiv:2603.08234, Mar 2026)](https://arxiv.org/abs/2603.08234): 揭示 continuation head（中间层 ~L13）与 safety head（L25-27）的对抗性竞争机制，continuation-triggered jailbreak 源于这种内在竞争。独立佐证 Layer 13 是安全竞争的关键枢纽。
- [Johnson & Huo (arXiv:2602.14370, Feb 2026)](https://arxiv.org/abs/2602.14370): 数学化注意力竞争的 tipping point 理论——dot-product 竞争创造动态翻转点 n*，超过后从安全行为转变为不安全行为。为"累积惯性跨轮推动系统越过阈值"提供理论框架。
- [Zhou et al. (ICLR 2025, arXiv:2410.13708)](https://arxiv.org/abs/2410.13708): 提出 Ships 分数，识别安全关键注意力头。单个头消融可使模型对 16 倍有害查询做出响应，仅修改 0.006% 参数。
- [AISA (Song et al., arXiv:2602.13547)](https://arxiv.org/abs/2602.13547): 通过时空分析定位安全感知头（top-K=16，0.92 检测精度），提供轻量级 logits-level steering。
- [X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990)](https://arxiv.org/abs/2502.09990): 表示层面安全边界，多轮 ASR 58.5%→16.5%，降低过拒绝 ~20%。
- [Steering Dialogue Dynamics (arXiv:2503.00187)](https://arxiv.org/abs/2503.00187): 通过学习安全预测器实现每轮对话的不变安全性，防止上下文漂移——与 proposal 的多轮安全防御方向相关但方法不同。
- 额外搜索确认：**目前没有任何工作测试过话语层面干预（特别是对话惯性削减）对安全性的因果影响**。CPL→安全性的连接确实是一个未被探索的空白。

- 调研总结: 该领域已形成清晰的多线收敛格局——推理时注意力重分配（DETAM）、训练时电路修改（ASGuard）、多轮安全训练（XGuard-Train, MUSE-D, X-Boundary, MTSA）、安全头定位（Zhou, AISA, Depth Charge）、注意力竞争理论（Johnson & Huo）、话语动力学（Wan CPL）各自独立发展，但"话语层面惯性削减→安全改善"的因果桥梁确实是空白。Proposal 处于这个交叉点上，gap 是真实的。

【Trivial Alternative 检验】: 
**存在显著的 trivial alternative 威胁。** 最直接的替代方案是：直接在安全标注数据上做 LoRA DPO/SFT（如 XGuard-Train 已证明 48.3% vulnerability reduction，MUSE-D 实现 24% ASR reduction）。如果目标是"改善多轮安全性"，直接用安全数据训练是成本更低、效果已验证的方法。Proposal 试图通过"间接"路径（话语惯性削减→注意力重分配→安全改善）达到类似效果。其增量价值在于：(1) 如果 CPL 不使用任何安全标注数据就能改善安全性，这揭示了一个关于注意力竞争的因果机制洞察；(2) 间接方法可能泛化到直接方法无法覆盖的分布外攻击。但关键问题是：**审稿人极有可能问 "为什么不直接训练安全数据？间接路径的实际优势是什么？"** Proposal 的回答（"CPL 不需要安全数据"）是合理的，但需要实证证明 CPL 确实在 XGuard-SFT 无法覆盖的场景中表现更好，否则间接路径的价值仅停留在"机制洞察"层面。

【前提假设检验】: 
核心逻辑链：对角注意力（惯性）→ 与安全注意力竞争 → 累积跨轮 → 越过 tipping point → 安全退化。CPL 削减惯性 → 释放注意力容量 → 安全改善。
**未经验证的关键假设**:
1. **假设 A（头级重叠）**: 对角注意力头与安全头存在实质重叠。这是 Level 1 假设的前提，而 Wan et al. 从未做过 per-head 分解，这个重叠可能为零或极低。Proposal 意识到了这一点并设计了三级框架来对冲，但如果结果是 Level 3（表示级），竞争机制变得模糊且几乎不可证伪。
2. **假设 B（因果方向）**: 假设是"惯性→安全退化"，但因果方向可能相反——安全退化（如 alignment erosion）可能导致模型更依赖惯性续写模式，而非惯性"挤占"安全注意力。Proposal 的混合效应回归和 Granger 因果检验在一定程度上可以区分，但观察数据上的因果推断能力有限。
3. **假设 C（CPL 效果可迁移）**: CPL 在 agentic 环境（ALFWorld, WebShop 等）上训练的惯性削减能力能迁移到安全评估场景。两者的分布差异（工具使用任务 vs. 安全对话）可能使 CPL 的惯性削减效果在安全场景中大打折扣。
4. **假设 D（tipping point 可操作性）**: Johnson & Huo 的 tipping point 理论在抽象数学层面有效，但在实际 Transformer 的 multi-head attention 中是否真的存在可观察的"阈值效应"尚无实证。该理论更多是类比框架而非可量化预测。

【3 维度打分】:
  1. Novelty: 中 — 研究问题本身是真正新颖的：将话语动力学（CPL/对角注意力）与安全性因果联系起来，确实是一个未被探索的交叉点（搜索确认无直接竞争工作）。per-head 对角注意力分解和三方法安全头识别比较是真正的分析性贡献。但核心操作是"将别人的方法（CPL）应用到新评估场景（安全性）"，而非提出新方法。且核心预测——"如果惯性占用注意力容量，减少惯性应该释放安全注意力"——是已知成分（softmax 零和 + 安全头 + 对角注意力）的自然推论，审稿人可能判断为 "I would have guessed this"。三级假设框架虽然结构化但有unfalsifiable之嫌（任何结果都可以被归入某个level）。相比 Deng et al. 发现 continuation-safety 头竞争、DETAM 证明注意力重分配改善安全性这些"令人惊讶"的发现，本 proposal 更像是对已知机制的系统化验证而非新发现。
  
  2. Significance: 中 — 多轮安全是重要且活跃的研究方向（MT-AgentRisk, OpenAgentSafety, MultiBreak 等 benchmark 的涌现证实了这一点）。如果 CPL 确实在无安全标注数据的情况下改善安全性，这对理解注意力机制与安全性的关系有深远意义。但实际影响受限于两个因素：(a) 如果结果是 positive 但不如 XGuard-SFT 等直接方法，实用价值有限，贡献主要在机制洞察层面；(b) 如果结果是 negative/weak（落入 Level 3），论文退化为"per-head 分析 + 安全头比较"的分析性贡献，虽有价值但影响力显著降低。最佳情形（CPL 大幅改善安全性且通过注意力竞争机制）是有意义的，但这个情形发生的概率本身也是未知的。Proposal 的"dual-outcome"设计保证了有输出，但不保证输出有高影响力。
  
  3. Related Work: 强 — 覆盖面极其全面，涵盖了 6 条独立研究线索，每条线索的定位和差异化分析都很准确。DETAM、ASGuard、Wan et al.、Deng et al.、Johnson & Huo、AISA 等关键论文的描述经调研验证均准确。Gap 识别是真实的——确实无人测试话语干预→安全改善的因果链。与 ASGuard Layer 13 头的交叉引用（独立佐证 continuation-safety 竞争）是一个有说服力的论证。唯一小瑕疵：部分引用（如 "Agent Drift", "SafetyDrift" 等 2026 论文）未提供 arXiv ID，无法完全验证；但核心论证所依赖的文献均真实可查。

【概率估计】: [22% - 32%] 中位 27%

【估计理由】: 
Novelty 是中等水平——研究问题真正新颖但核心洞察不够 surprising（"减少注意力竞争改善安全"是自然推论而非反直觉发现），这限制了上界无法突破 35%。Significance 同样中等——最佳情形有价值但最佳情形发生概率不确定，且存在强 trivial alternative（直接安全训练）。Related Work 的强势表现提供了坚实下限。三者综合：这是一个方向正确、gap 真实、分析框架有贡献的 proposal，但核心 claim 的内核——"间接话语训练能因果改善安全"——即使被证实，审稿人更可能评价为 "interesting empirical finding" 而非 "surprising insight"。**上界主要被 Novelty 限制**：核心假设是已知成分的组合，三级框架的 unfalsifiable 特性可能被视为 hedging 而非科学严谨。

【主要风险】: 
1. **"Apply X to Y" 感知风险**: 审稿人可能将此视为"把 CPL（别人的方法）应用于安全评估（新场景）"的增量工作，而非独立的方法论贡献。三级假设框架和 per-head 分析是真正的贡献，但容易被这一感知淹没。
2. **三级假设 unfalsifiable 风险**: Level 1→Level 2→Level 3 的递降框架确保了"总有某个 level 成立"，审稿人可能质疑：如果任何结果都能被纳入框架，这个假设的科学价值是什么？特别是 Level 3（表示级竞争）过于宽泛，几乎任何 DPO 训练效果都可以被归因于"表示级竞争"。
```

Sources:
- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification](https://arxiv.org/abs/2504.13562)
- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026)](https://arxiv.org/abs/2602.03664)
- [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (ICLR 2026)](https://arxiv.org/abs/2509.25843)
- [The Struggle Between Continuation and Refusal (Deng et al., 2026)](https://arxiv.org/abs/2603.08234)
- [Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, 2026)](https://arxiv.org/abs/2602.14370)
- [On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)
- [AISA: Awakening Intrinsic Safety Awareness in LLMs (Song et al., 2026)](https://arxiv.org/abs/2602.13547)
- [X-Boundary: Establishing Exact Safety Boundary (Lu et al., EMNLP 2025)](https://arxiv.org/abs/2502.09990)
- [Steering Dialogue Dynamics for Robustness against Multi-Turn Jailbreaking](https://arxiv.org/abs/2503.00187)
- [DeTAM - ACL Anthology](https://aclanthology.org/2025.findings-acl.613/)
- [ASGuard - OpenReview ICLR 2026](https://openreview.net/forum?id=wmiEXNEXPs)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Wan et al. "Mitigating Conversational Inertia in Multi-Turn Agents" arXiv:2602.03664](https://arxiv.org/abs/2602.03664) (ICML 2026): 提出 conversational inertia 概念和 CPL 方法。确认论文存在、已发表于 ICML 2026。关键细节验证：CPL 使用 LoRA rank-16 DPO beta=0.01，减少 diagonal attention 10%+。论文明确声明"All attention heads are averaged to create a unified attention matrix"——per-head decomposition 确实不存在。**但 CPL 仅在 agent 性能（ALFWorld, WebShop 等 8 个环境）上验证，从未评估安全性。**

- [DETAM (Li et al.) arXiv:2504.13562](https://arxiv.org/abs/2504.13562) (ACL 2025 Findings): 确认存在。通过推理时注意力重分配（mask modification, beta=5.0）将 ASR 从 46% 降至 1.2%。确认仅限 single-turn。确认需要运行时识别 intent tokens。

- [ASGuard (Park et al.) arXiv:2509.25843](https://arxiv.org/abs/2509.25843) (ICLR 2026): 确认存在。通过 EAP-IG 识别 vulnerable heads，channel-wise scaling vectors + preventative fine-tuning。确认针对 tense jailbreaking 等特定攻击类型，自述 "efficacy hinges on localizable causal circuits"。

- [Johnson & Huo arXiv:2602.14370](https://arxiv.org/abs/2602.14370) (arXiv Feb 2026): 确认存在。提出 dot-product competition 的 tipping point n* 数学公式。但注意：该论文关注 edge AI 的 good-to-bad tipping，是偏理论/物理学视角的分析，并非专门针对 diagonal attention 或多轮安全。

- [Deng et al. arXiv:2603.08234](https://arxiv.org/abs/2603.08234) (arXiv Mar 2026): 确认存在。分析 continuation vs. refusal heads 的竞争机制。提供了 safety heads (layers 25-27) vs. continuation heads (middle layers ~Layer 13) 的定位。

- [AISA (Song et al.) arXiv:2602.13547](https://arxiv.org/abs/2602.13547) (arXiv Feb 2026): 确认存在。通过 spatiotemporal analysis 定位 safety heads，top-K=16 heads 达到 0.92 检测准确率。

- [Zhou et al. arXiv:2410.13708](https://arxiv.org/abs/2410.13708) (ICLR 2025): 确认存在。Ships score（Safety Head ImPortant Score），Sahara 算法定位安全注意力头。

- **直接竞争检索结果**：搜索 "conversational inertia safety" 未找到任何已有工作将 conversational inertia/CPL 与安全联系起来。该 gap 目前看是真实的。

- 调研总结：多轮安全领域（攻防、机制分析、防御训练）和 attention-level 安全机制分析（safety heads, continuation heads, attention competition）是两个活跃但仍较独立的研究方向。Conversational inertia（Wan et al.）目前仅在 agent 性能维度被研究，尚无人将其连接到安全问题。本 proposal 试图搭建这座桥梁。


【Trivial Alternative 检验】:

**存在两个显著的 trivial alternative 威胁：**

1. **逐轮 DETAM**：虽然 proposal 论证了 DETAM 在多轮场景下 "intent tokens 不可定位"，但这个论证是概念层面的，并未实证验证。一个更 trivial 的做法是：在每一轮都应用 DETAM（将当前轮的 user input 视为 intent），测试是否足够有效。如果逐轮 DETAM 已经很好地解决了多轮安全问题，那么 CPL 的增量价值就很小。Proposal 并未包含"multi-turn DETAM"作为 baseline。

2. **直接在安全数据上做 DPO/SFT**：XGuard-Train SFT 作为 control 被包含了——但核心问题是：为什么一个 **不在安全数据上训练、仅在 agent 环境上训练** 的 discourse intervention (CPL) 会比 **直接在安全数据上训练** 的方法更好？如果 CPL 的安全提升不如 XGuard-Train（这是可能性最高的结果），那 proposal 的故事就变成了"间接方法不如直接方法"——虽然可以 publish 但 significance 大打折扣。

**增量价值的核心依赖**：CPL 的独特价值必须来自"不用安全标注数据就能提升安全性"这个属性——即 unsupervised safety improvement via discourse training。这是有意义的，但需要 CPL 的效果足够大才能让审稿人信服这不只是噪声。


【前提假设检验】:

核心逻辑链存在 **三个关键未验证假设**：

1. **Head Overlap 假设（最关键）**：整个"attention capacity competition"假设的前提是 diagonal attention heads 与 safety heads 在某种程度上重叠（或至少在相同 layer 竞争）。Proposal 正确地在 Phase 0.5 测试这个假设——但如果 overlap 极低（Level 3），整个 softmax zero-sum 竞争机制就不成立，论文的理论叙事从"attention competition"退化为"representation drift"，novelty 大幅下降（representation drift 已被 X-Boundary 研究过）。

2. **CPL 效果迁移假设**：CPL 在 AgentGym 环境（ALFWorld, WebShop 等）上训练和验证。假设它学到的 attention 变化能迁移到完全不同的安全评估场景（MT-AgentRisk, 恶意多轮对话）。这个迁移并非显然——CPL 训练的 preference pairs 来自 agent 任务的 long-context vs. short-context，与安全场景的分布可能相差很大。

3. **因果方向假设**：论文假设 "diagonal attention → 安全下降" 是因果关系。但同样可能的替代解释是：多轮对话本身增加了复杂性/context length，导致 diagonal attention 和安全下降 **同时发生但无因果关系**（confounded by conversation length/complexity）。CPL 减少 diagonal attention 时，如果安全确实提升，还需要排除 CPL 同时引入的其他变化（如 response style changes、length changes 等）。Proposal 包含了 response-length control，但未控制所有可能的 confounds。


【3 维度打分】:

1. **Novelty: 中** — 
   - **确认的真实 novelty delta**：(a) 首次将 conversational inertia 连接到 multi-turn safety——搜索确认此 gap 真实存在；(b) 首个 per-head diagonal attention decomposition（Wan et al. 明确只做 aggregate-level averaging）；(c) 三种 safety head 定位方法的对比研究。
   - **Novelty 的局限**：核心实验本质上是"将一个已有方法（CPL）应用到一个新评估维度（安全）"——这是 transfer/application study 而非新方法提出。三级竞争假说是理论贡献，但它尚未被验证，如果 Phase 0.5 结果不支持 Level 1/2，这个贡献就变成了一个被否决的假设。方法论上未提出新技术（CPL 来自 Wan et al.，Ships 来自 Zhou et al.，DETAM sensitivity 来自 Li et al.，AISA 来自 Song et al.）——所有分析工具都是现成的。
   - **与最近工作的对比**：无直接竞争者（gap 真实），但核心贡献的 novelty 性质偏向 empirical study 而非 methodological innovation。审稿人可能认为这是一个 well-designed empirical investigation，但不是一个 novel approach。

2. **Significance: 中** — 
   - **正面**：多轮安全是一个重要且活跃的问题（16% ASR increase documented by Yang et al.）。如果 CPL 确实能在不使用安全标注数据的情况下显著提升多轮安全，这对 alignment 领域有重要启示——意味着 discourse dynamics 是安全的一个被忽视的维度。
   - **限制**：(a) 最可能的结果是 CPL 有 modest improvement（因为任何改变模型 attention 分布的训练都可能对安全有微弱影响），这不够 surprising 来支撑高 significance；(b) 如果 CPL 效果弱于直接安全训练方法（XGuard-Train, MUSE-D），实际应用价值有限——practitioners 会直接选择用安全数据训练；(c) 即使 positive，结论的可推广性受限于 CPL 这一特定方法——无法确定是 "减少 inertia" 还是 CPL 的某个副作用导致了安全提升。

3. **Related Work: 强** — 
   - 调研确认 proposal 引用的所有关键论文（DETAM, ASGuard, Wan et al., Johnson & Huo, Deng et al., Zhou et al., AISA）都真实存在且描述准确。与现有工作的差异化定位清晰且诚实（DETAM: single-turn + runtime; ASGuard: circuit-specific; XGuard-Train: safety-labeled data）。文献覆盖面在本领域可能是最全面的——涵盖攻击、防御、机制分析、基准测试、理论框架等多个子方向。唯一可能的遗漏：未讨论"逐轮 DETAM"作为一个 straightforward extension 的可行性。


【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
- **Related Work (强)** 提供了坚实的基础，确保论文不会因文献遗漏被拒。
- **Novelty (中)** 是主要限制因素——核心贡献是 "apply existing method to new evaluation dimension"，方法论创新不足。Per-head decomposition 和 triple triangulation 是 solid 但 incremental 的贡献。审稿人可能认为这更像一个 thorough empirical study 而非一个有 conceptual breakthrough 的论文。
- **Significance (中)** 进一步限制上界——最可能的实验结果（CPL 有 modest effect but weaker than direct safety training）会让审稿人说 "I would have guessed this"。只有在 CPL 效果显著且机制分析清晰展示 head overlap 时，才能达到 surprising 的程度，但这需要多个未验证假设同时成立。
- **概率上界受限于**：idea 本质是 application study + hypothesis testing，而非 method proposal。即使执行完美，核心发现的 surprise factor 有上限。
- **概率下界受益于**：gap 真实、实验设计有 5 个 controls、有多个 standalone 贡献（per-head decomposition, head comparison）可以在 negative result 时提供 fallback value。

【主要风险】: 
1. **"I would have guessed this" 风险**：无论 CPL 的安全效果是正向还是负向，审稿人都可能认为结果在预期范围内——正向（"当然，改变 attention 分布会影响安全"）或负向（"当然，不在安全数据上训练不会提升安全"）。缺乏一个 clear a priori reason to expect a *surprising* outcome。
2. **Assumption Cascade 风险**：论文的核心叙事（attention competition hypothesis）依赖一连串未验证假设（head overlap → softmax competition → cumulative tipping → CPL as implicit DETAM）。任何一环断裂，理论框架就需要大幅调整，论文从"验证了一个 elegant theory"变成"做了一个 comprehensive but inconclusive empirical study"。
```

Sources:
- [Wan et al. - Mitigating Conversational Inertia in Multi-Turn Agents (ICML 2026)](https://arxiv.org/abs/2602.03664)
- [DETAM - Li et al. (ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)
- [ASGuard - Park et al. (ICLR 2026)](https://arxiv.org/abs/2509.25843)
- [Johnson & Huo - Competition for attention predicts good-to-bad tipping in AI](https://arxiv.org/abs/2602.14370)
- [Deng et al. - The Struggle Between Continuation and Refusal](https://arxiv.org/abs/2603.08234)
- [AISA - Song et al.](https://arxiv.org/abs/2602.13547)
- [Zhou et al. - On the Role of Attention Heads in LLM Safety (ICLR 2025)](https://arxiv.org/abs/2410.13708)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
This is very relevant. Let me now compile my full evaluation based on all the research.

---

```
【阶段】: Triage

【领域调研】:

1. Wan et al., "Mitigating Conversational Inertia in Multi-Turn Agents" (ICML 2026, arXiv:2602.03664):
   - 确认存在且已发表。定义了 diagonal attention（conversational inertia），提出 CPL（LoRA rank-16 DPO, beta=0.01）。
   - 仅在 8 个 agentic 环境上评估 task performance，**从未评估 safety**。Proposal 对该论文的描述准确。
   - 关键细节确认：原文确实仅报告 aggregate-level attention（所有 head 平均），未做 per-head 分解。

2. DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562):
   - 确认存在。推理时修改 attention mask 放大 intent token 注意力，LLaMA-2 ASR 46%→1.2%。确实是 single-turn only。
   - Proposal 描述准确。

3. ASGuard (Park et al., ICLR 2026, arXiv:2509.25843):
   - 确认存在且已发表在 ICLR 2026。使用 EAP-IG 定位 vulnerable heads，channel-wise scaling vectors，针对 tense jailbreaking。
   - Proposal 描述准确，包括 Layer 13 的 4 个 vulnerable heads。

4. Johnson & Huo, "Competition for attention predicts good-to-bad tipping in AI" (arXiv:2602.14370, Feb 2026):
   - 确认存在。提出 dot-product attention 竞争导致 good-to-bad tipping point 的数学框架。
   - 但注意：这是一篇 **physics 视角的理论论文**（来自 GWU 物理系），将 attention competition 建模为物理系统的相变。它提供的是一个 analogy/框架，而非 NLP 社区内的 empirical 发现。Proposal 将其作为核心理论支柱之一，但审稿人可能质疑其对 transformer 内部机制的直接适用性。

5. Deng et al., "The Struggle Between Continuation and Refusal" (arXiv:2603.08234, Mar 2026):
   - 确认存在。确实发现 continuation heads 与 safety heads 的竞争关系。Proposal 描述准确。

6. AISA (Song et al., arXiv:2602.13547, Feb 2026):
   - 确认存在。通过 spatiotemporal analysis 定位 safety heads，K=16 heads 达到 0.92 detection accuracy。Proposal 描述准确。

7. Zhou et al., "On the Role of Attention Heads in LLM Safety" (ICLR 2025, arXiv:2410.13708):
   - 确认存在，ICLR 2025 Oral。提出 Ships score。Proposal 描述准确。

8. **未被引用的重要工作**:
   - **"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction"** (arXiv:2605.12922, May 13 2026): 直接研究多轮交互中 attention 如何逐渐失去对 goal-defining tokens 的访问能力。提出 Goal Accessibility Ratio (GAR)，发现不同架构的 failure mode 不同，layer range 从 2 到 27。这与 proposal 的 "attention capacity competition" 高度相关——该论文提供了多轮 attention 衰减的独立证据，且研究 attention 在残差流中的持久性，直接相关于 proposal 的 Level 3 hypothesis。发表于 2026 年 5 月，proposal 可能来不及引用。

9. **调研总结**: 该领域正处于一个活跃的交叉点：多轮安全（MUSE-D, XGuard-Train, X-Boundary, MTSA）、attention 机制解释（safety heads, continuation heads, 竞争理论）、discourse dynamics（conversational inertia）。这三条线确实尚未被交叉——"用 discourse-level 训练干预来改善 safety"确实是一个未被测试的桥梁。但该桥梁的 insight depth 存疑：它更像是一个自然的 "apply X to Y" 连接，而非一个深刻的反直觉发现。


【Trivial Alternative 检验】:

存在两个层次的 trivial alternative 威胁：

(1) **直接安全训练 baseline**: XGuard-Train SFT 已经在 Llama-3.1-8B 和 Qwen-2.5-7B 上实现了高达 48.3% 的 vulnerability reduction，MTSA 将 ASR 从 74.5% 降到 23.5%，X-Boundary 将 ASR 降到 16-25%。如果 CPL 的 safety improvement 弱于或可比于这些专门为 safety 设计的方法，那么"通过 discourse 训练间接改善 safety"的 story 就缺乏实际意义——审稿人会问 "why not just train on safety data directly?"

Proposal 的回应是"CPL 不用 safety-labeled data"，但这个优势需要 CPL 在 safety 上至少达到 comparable 水平才有说服力。如果 CPL 显著弱于 XGuard-SFT，那么 "discourse intervention can help safety" 是一个有趣但 marginal 的发现。

(2) **Response quality confound**: CPL 的核心效果是让模型"less inertial"——即输出更少地重复/模仿之前的 pattern。更高质量、更 contextual 的回复自然倾向于更安全，因为 unsafe 回复往往是模型被 primed 后"顺着说"的结果。如果 CPL 的 safety improvement 完全可以被"回复质量普遍提升"解释（而非 attention competition 机制），那么 mechanistic 贡献就被架空了。Proposal 设计了 length control，但 length 不等于 quality——更难控制的是 "CPL 让模型更 'thoughtful' in general" 这一全局效应。

**增量价值判断**: 如果 Phase 0.5 显示 diagonal attention heads 与 safety heads 高度重叠（Level 1），且 CPL 确实在这些 specific heads 上改变了 attention distribution，那么 mechanistic story 有实质内容。但如果是 Level 3（low overlap），整个 "attention competition" 叙事就弱化为 "representation-level 的模糊改善"，与 X-Boundary 等工作的差异化不明显。


【前提假设检验】:

核心逻辑链: diagonal attention (inertia) → softmax zero-sum competition with safety attention → reduced safety → CPL reduces inertia → safety improves

**未经验证的关键假设**:

(A) **"Diagonal attention 与 safety attention 在 softmax 层面竞争"**: 这是整个 hypothesis 的核心前提。Softmax 的 zero-sum 约束确实存在，但只在 **单个 head 内** 成立。Proposal 的 Level 1 hypothesis 要求 inertia 和 safety 发生在同一些 heads 中——这是一个 empirical question（Phase 0.5 的目标），但如果答案是 no（只有 Level 2 或 Level 3），整个 "softmax zero-sum competition" 叙事的直接性就大大减弱。
- Level 2（same layer, different heads）的竞争通过 residual stream 间接发生，机制更复杂、更难验证
- Level 3（different layers）的竞争更像是"一般性的 representation drift"，这几乎无法与 "attention competition" 区分开来

(B) **"Conversational inertia 是多轮安全退化的因果驱动力，而非伴随现象"**: Proposal 引用 ASJA（attention dispersion 与 ASR 的相关性）和 Johnson & Huo（tipping point 理论），但这些只建立了相关性/理论可能性。一个替代解释是：多轮安全退化主要由 **alignment tax exhaustion**（长对话中 alignment 信号衰减）驱动，diagonal attention 只是长对话的一个 epiphenomenon。CPL 可能改善 safety 不是因为减少了 inertia 对 safety heads 的竞争，而是因为 DPO 训练附带增强了模型对 context 的审慎处理。

(C) **"CPL 的效果可以迁移到 safety 域"**: CPL 在 agentic task performance 上有效，但 agentic environments（ALFWorld, WebShop 等）与 safety scenarios（jailbreak resistance）的 attention dynamics 可能有根本差异。在 agentic 环境中，"减少 inertia" 意味着 "不重复之前低效的 action patterns"；在 safety 场景中，模型需要的是 "即使在长对话 context 下也 maintain refusal capability"。这两种 "不被之前的 output 牵着走" 是否走同一条 attention pathway，并不显然。

(D) **Johnson & Huo 的 tipping point 理论直接适用于 transformer 内部**: 该论文来自物理系，提供的是 dot-product attention competition 的数学抽象。但 transformer 的 multi-head, multi-layer 架构比该理论的假设复杂得多——tipping point n* 的计算假设了一个简化的 attention competition 模型，真实 transformer 中是否出现类似的相变行为并未被验证。


【3 维度打分】:

1. **Novelty: 中**
   - 正面：CPL → safety 的桥梁确实无人测试过；per-head diagonal attention 分解是一个真实的、Wan et al. 明确留下的空白；triple-method safety head identification comparison 是一个有价值的方法论贡献。
   - 局限：核心 idea 本质是 "apply technique A (CPL) to domain B (safety)" 的 bridge study，conceptual leap 有限。"discourse dynamics 影响 safety" 这个 high-level insight 并不反直觉——Deng et al. (2603.08234) 已经证明 continuation heads 与 safety heads 竞争，ASJA (AAAI 2025) 已经证明 attention dispersion 影响 safety，"When Attention Closes" (2605.12922) 独立发现多轮 attention 衰减。Proposal 的增量是"用 CPL 这个特定工具测试"，而非"提出这个概念"。
   - 与最近工作的距离：与 "When Attention Closes" (May 2026) 有显著概念重叠——该论文也研究多轮交互中 attention 如何逐步失去对关键 token 的访问，用 GAR 量化这一过程，且同样考虑了 residual stream 中信息是否持久。Proposal 需要明确区分。

2. **Significance: 中**
   - 正面：多轮安全是 NLP/AI safety 领域的重要问题（16% ASR increase, MTSA 显示 round 5 peak attack）；理解 discourse dynamics 与 safety 的因果关系有理论价值；如果 CPL 确实能"免费"改善 safety（无需 safety-labeled data），这对实践有意义。
   - 局限：**核心发现的 surprise factor 有限**。如果 CPL 改善了 safety → "训练模型更好地处理 context 也改善了 safety"，审稿人可能说 "I would have guessed this"。如果 CPL 没改善 safety → 负面结果 + 分析性贡献。两种结果都不是 "surprising, not what I expected" 级别。真正的 surprise 需要：(a) CPL 在 safety 上超过专门的 safety training（这非常 unlikely），或 (b) 发现一个非常精确的 mechanistic 联系（如 Level 1 overlap >50%），但这是 empirical question 而非 idea 的内在 significance。
   - 另一个 significance 限制：即使所有 hypotheses 都得到验证，practical takeaway 是什么？"在部署时先跑一轮 CPL 可以改善 safety"——但工程上人们更可能直接用 safety training。Mechanistic 理解有学术价值，但 impact scope 主要限于 safety interpretability 子社区。

3. **Related Work: 强**
   - 极其全面的 literature coverage：涵盖了 attention 机制（DETAM, ASGuard, AISA, Zhou et al., Depth Charge, Attention Eclipse）、多轮安全（MUSE-D, XGuard-Train, X-Boundary, MTSA, MT-AgentRisk, OpenAgentSafety）、理论框架（Johnson & Huo）、mechanistic interpretability（Deng et al., safety layers, refusal direction）。
   - 差异化定位清晰：明确指出 DETAM 的 single-turn 限制、ASGuard 的 circuit-specific 限制、现有安全训练方法的 "safety-labeled data" 依赖。
   - 唯一缺失：**"When Attention Closes" (arXiv:2605.12922, May 2026)** ——该论文高度相关（多轮 attention 衰减、GAR 指标、residual stream 分析），应当被引用和差异化。但考虑到该论文发表于 May 13, 2026，可能晚于 proposal 撰写时间，这不是严重疏漏。


【概率估计】: 22% - 32%，中位 27%

【估计理由】:
- Novelty 为"中"（有真实的 novelty delta，但 conceptual leap 有限，核心是 bridge study）限制了上界在 ~35% 以下
- Significance 为"中"（无论正面还是负面结果，surprise factor 都有限）进一步将中位数锚定在 25-30%
- Related Work 为"强"（但 related work 的完备性是基础素养而非加分项，不提升 idea 质量上限）
- 三维综合：idea 方向正确、有真实 gap、但核心发现如果 positive 审稿人大概率会说 "I would have guessed this"——这正好落在 25-35% 区间
- 上界被 significance 限制：即使 execution 完美，idea 的上限取决于 "CPL 改善 safety 是否 surprising"，这个 bar 较难跨过
- 下界被 related work 和 novelty 支撑：per-head decomposition、triple-method comparison、confound-controlled design 提供了实质性的分析贡献，即使主要 hypothesis 不成立也有 fallback value

【主要风险】:
1. **"So what" 风险**: 如果 CPL 确实改善了 safety，审稿人可能认为这是 "general model improvement helps safety" 的一个 instance，而非 attention competition mechanism 的特定验证——即 positive result 但 mechanistic claim 不被信服，导致论文贡献降级为 "another safety training method"，而在这个赛道上 CPL 不如专门的 safety training 有竞争力。
2. **前提假设链断裂风险**: 如果 Phase 0.5 显示 diagonal attention heads 与 safety heads 低重叠（Level 3），核心 "attention capacity competition" 叙事的直接性严重削弱，论文需要 pivot 到更弱的 "representation-level" story，与 X-Boundary (EMNLP 2025) 的 framing 趋近，差异化空间被压缩。
```

Sources:
- [Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026)](https://arxiv.org/abs/2602.03664)
- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (ACL 2025 Findings)](https://arxiv.org/abs/2504.13562)
- [ASGuard: Activation-Scaling Guard (ICLR 2026)](https://arxiv.org/abs/2509.25843)
- [Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, 2026)](https://arxiv.org/abs/2602.14370)
- [The Struggle Between Continuation and Refusal (Deng et al., 2026)](https://arxiv.org/abs/2603.08234)
- [AISA: Awakening Intrinsic Safety Awareness (Song et al., 2026)](https://arxiv.org/abs/2602.13547)
- [On the Role of Attention Heads in LLM Safety (Zhou et al., ICLR 2025)](https://arxiv.org/abs/2410.13708)
- [When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction (May 2026)](https://arxiv.org/abs/2605.12922)
- [MTSA: Multi-turn Safety Alignment (ACL 2025)](https://arxiv.org/abs/2505.17147)
- [X-Boundary (EMNLP 2025)](https://arxiv.org/abs/2502.09990)


【原始 proposal（允许参考但不是主要依据）】:
# Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypothesis

## Description
This project conducts the first controlled interventional study testing whether mitigating conversational inertia — diagonal attention to previous outputs (Wan et al., ICML 2026) — causally reduces multi-turn safety erosion, organized around a refined three-level 'attention capacity competition hypothesis.' We build on DETAM's proof that inference-time attention reallocation improves safety (ASR 46%→1.2%) and ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities, testing whether CPL achieves broad attention reallocation through untargeted discourse training — addressing the progressive multi-turn erosion that DETAM (single-turn, requires runtime intent localization) and ASGuard (targets specific localizable circuits) structurally cannot. In multi-turn crescendo attacks, malicious intent is distributed across turns, making DETAM's intent-token identification ill-defined; CPL instead reduces the cumulative inertia that pushes systems past Johnson & Huo's tipping point. A novel Phase 0.5 provides the first per-head decomposition of diagonal attention (Wan et al. explicitly averages all heads) and measures overlap with safety-critical heads using triple triangulation (Ships score, DETAM sensitivity, AISA spatiotemporal analysis), cross-validated against published head sets (Zhou et al., Depth Charge, ASGuard — whose 4 Layer-13 vulnerable heads independently corroborate the continuation-safety nexus). Our five-phase causal design tests CPL against five confound controls including XGuard-Train SFT at both published and CPL-matched ranks. Mechanistic verification tests whether CPL achieves 'implicit DETAM' (same heads, same direction) and 'implicit circuit modification' (affecting ASGuard's identified vulnerable heads without targeting them). The study is designed for informative outcomes at all three competition levels, with the per-head diagonal attention decomposition, triple-method head identification comparison, and DETAM/ASGuard mechanistic comparison constituting standalone contributions.

## Core Problem
Multi-turn agent interactions exhibit systematic safety degradation (16% higher attack success rates), and while recent work has identified attention-level mechanisms — attention dispersion on safety keywords (ASJA, AAAI 2025), competition between safety and continuation heads (Deng et al., 2026), and attention reallocation as a defense (DETAM, ACL 2025 Findings) — and developed multi-turn safety defenses (MUSE-D turn-level DPO, EMNLP 2025; XGuard-Train SFT, COLM 2025; X-Boundary representation boundaries, EMNLP 2025; MTSA RL-based alignment, ACL 2025), and even training-time attention head interventions for specific vulnerability types (ASGuard circuit-targeted scaling, ICLR 2026), these studies are either attack-oriented, single-turn, operate at inference time, target specific localizable vulnerabilities, or train directly on safety-labeled data without testing whether discourse-level mechanisms causally drive safety erosion. Critically, DETAM (Li et al., ACL 2025 Findings) demonstrates that simply reallocating attention from attack tokens toward safety-relevant tokens at inference time — without any weight changes — reduces ASR from 46% to 1.2% on LLaMA-2, providing the strongest existing evidence that attention redistribution causally improves safety. Yet DETAM requires explicit identification of 'intent tokens' at runtime and operates only in single-turn settings — in multi-turn crescendo attacks where malicious intent is progressively distributed across turns, the notion of localizable 'intent tokens' breaks down fundamentally. ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant heads is feasible via circuit-targeted scaling vectors, but its efficacy 'hinges on localizable causal circuits' for specific attack types (tense jailbreaking) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits. No work has tested whether a training-time discourse intervention (reducing conversational inertia) achieves broad attention reallocation indirectly, nor whether the specific attention heads carrying diagonal inertia patterns overlap with safety-critical heads — a prerequisite for the softmax zero-sum competition mechanism to operate at the head level. Notably, the only characterization of diagonal attention (Wan et al., ICML 2026) reports aggregate-level patterns averaged across all heads; no per-head decomposition exists, leaving the head-level competition question empirically open. Additionally, the response-length confound in DPO-based interventions has never been explicitly controlled for in safety evaluations of discourse-level interventions.

## Opportunity
Six independent research threads have converged to make a controlled causal study newly feasible: (1) Conversational Inertia (Wan et al., ICML 2026) identifies diagonal attention where the i-th token attends to the i-th previous output position and provides Context Preference Learning (CPL) as a parameter-efficient intervention (0.4% params, LoRA rank-16 DPO with beta=0.01), validated on Qwen3-8B and Llama 3.1-8B-Instruct across eight agentic environments but never evaluated for safety — crucially, the diagonal attention pattern is characterized only at the aggregate level (averaged across all heads), so the per-head distribution remains unknown; (2) DETAM (Li et al., ACL 2025 Findings) provides direct causal evidence that attention reallocation toward safety-relevant tokens improves safety — reducing ASR by 97%+ without weight modification — but requires runtime intent token identification and is single-turn only, creating a fundamental limitation for multi-turn settings where intent is distributed across turns; (3) ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant attention heads is feasible via circuit-targeted channel-wise scaling vectors and preventative fine-tuning — crucially, ASGuard identifies 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30), exactly where Deng et al. find continuation heads, providing independent corroboration that Layer 13 is a nexus of safety-relevant competition — but ASGuard targets specific localizable vulnerability circuits (tense jailbreaking) rather than discourse-level dynamics; (4) Multi-turn safety erosion is now well-benchmarked via MT-AgentRisk (365 tasks, 5 tools, avg 3.19 turns) with ToolShield as a defense baseline, and supplemented by OpenAgentSafety (ICLR 2026, 356 real-tool tasks with multi-turn multi-user dynamics); (5) Multi-turn safety training has mature baselines spanning multiple paradigms: XGuard-Train SFT (COLM 2025, up to 48.3% vulnerability reduction), MUSE-D turn-level DPO (EMNLP 2025, 24% ASR reduction), X-Boundary representation-level boundaries (EMNLP 2025, ASR reduction to 16-25%), and MTSA RL with future rewards (ACL 2025, ASR 74.5% to 23.5%) — but all train directly on safety-labeled data; (6) AISA (Song et al., arXiv:2602.13547) provides a third complementary method for localizing safety-critical attention heads via spatiotemporal analysis — identifying that safety-discriminative signals concentrate in middle-layer head outputs with K=16 heads achieving 0.92 detection accuracy — enabling methodological triangulation in our head overlap analysis. This six-thread convergence, combined with Johnson & Huo's (2026) formalization of attention competition tipping points and the layered distribution of safety mechanisms across layers 2-27, motivates a three-level attention capacity competition hypothesis testable through a novel Phase 0.5 head overlap analysis.

## Landscape
**Attention reallocation defenses:** DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) is the most directly relevant inference-time prior work. It identifies attention heads sensitive to jailbreaks by computing attention score differences between successful and unsuccessful defenses (threshold alpha: 0.1 for LLaMA-2, 0.03 for Vicuna). During inference, it modifies the causal mask matrix by multiplying mask values at intent token positions by beta=5.0, amplifying attention to the user's core intention. DETAM reduces average ASR from 46.0% to 1.2% on LLaMA-2-7b-chat and from 81.8% to 4.0% on Vicuna-13b-v1.5. Cross-model transferability: sensitive heads from LLaMA-2 transferred to Meta-LLaMA-3 achieve 4% ASR vs. 96% vanilla. However, DETAM has three fundamental limitations for multi-turn agent settings: (a) it requires runtime identification of 'intent tokens' — in multi-turn crescendo attacks (Russinovich et al., USENIX Security 2025) where harmful intent is progressively distributed across turns, no single set of tokens constitutes 'the intent,' making DETAM's token-level localization fundamentally ill-defined; (b) it is tested only in single-turn settings and cannot address the cumulative attention shift across turns that Johnson & Huo's tipping point theory predicts; (c) it imposes per-turn computational overhead for mask modification in each forward pass across all turns of agent interaction. Our study tests whether CPL achieves DETAM-like attention redistribution persistently through training, addressing a failure mode DETAM structurally cannot: the gradual accumulation of continuation pressure across turns that progressively dilutes safety attention below the tipping point. **Training-time attention head intervention:** ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) is the closest existing work to training-time attention head modification for safety. It uses Edge Attribution Patching with Integrated Gradients (EAP-IG) to identify attention heads causally linked to specific jailbreaking vulnerabilities, trains channel-wise activation scaling vectors (s_j ∈ R^{d_head}, applied via Hadamard product H'_{l,j} = H_{l,j} ⊙ s_j) on identified heads, and applies preventative fine-tuning with scaling vectors frozen. On tense jailbreaking, ASGuard reduces ASR from 42% to 8% on Llama-3.1-8B and 51% to 8% on Qwen2.5-7B, achieving Pareto-optimal safety-utility balance. Critically, ASGuard identifies 11 vulnerable heads in Llama-3.1-8B, of which 4 are at Layer 13 (L13H8, L13H18, L13H25, L13H30) — exactly where Deng et al. find continuation heads — providing independent corroboration that Layer 13 is a nexus of safety-relevant attention competition. However, ASGuard differs from our approach in three key ways: (a) it targets specific, localizable vulnerability circuits ('efficacy hinges on localizable causal circuits' — their Limitations, Section 7) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits, as the failure is progressive rather than circuit-specific; (b) it surgically fixes known attack types (tense jailbreaking, GCG, LogiBreak) one at a time, whereas CPL is an untargeted discourse intervention testing whether reducing general inertia achieves broad safety benefits; (c) it is single-turn only. ASGuard's success actually supports a key premise of our hypothesis: training-time modification of attention heads CAN improve safety. Our study tests whether indirect, untargeted discourse training achieves what targeted head intervention achieves — and whether it generalizes to the multi-turn progressive erosion that targeted approaches cannot address. **Safety head localization methods:** AISA (Song et al., arXiv:2602.13547) provides a third complementary approach to localizing safety-critical heads via spatiotemporal analysis — large-scale linear probing across 15 positions per layer identifies that attention head outputs demonstrate superior safety separability, with top-K=16 heads (concentrated in middle layers) achieving 0.92 detection accuracy and O(1) runtime overhead. AISA's finding that safety heads cluster in middle layers in standard models but shift toward higher layers in strongly safety-aligned models adds nuance to the competition hypothesis — the relevant layers may differ by alignment strength. **Attack-side mechanisms:** Du et al. (ASJA, AAAI 2025) show that successful multi-turn jailbreaks correlate with attention dispersion away from safety keywords (p=4.38e-07), achieving 44.9% higher ASR. Deng et al. (arXiv:2603.08234) identify competing safety and continuation attention heads — safety heads concentrated in layers 25-27, continuation heads in middle layers (~Layer 13) — whose antagonistic interaction determines jailbreak success. Notably, continuation heads at Layer 13 occupy the same layer range as both induction/copying mechanisms AND ASGuard's identified vulnerable heads, suggesting this layer is a critical nexus where diagonal attention patterns, continuation signals, and safety vulnerability converge. Depth Charge (Wu et al., arXiv:2603.05772, March 2026) introduces SAHA using Ablation-Impact Ranking and Layer-Wise Perturbation, achieving 82-91% ASR, revealing layer-specific safety head concentrations (layer 7 for Llama 3.1-8B, layer 5 for Qwen 1.5-7B, head 31 universally important) and sharp threshold behavior. Attention Eclipse (Zaree et al., arXiv:2502.15334) achieves 91.2% ASR by manipulating attention to strengthen harmful content focus and weaken safety focus. **Attention competition theory:** Johnson & Huo (arXiv:2602.14370, Feb 2026) formalize the competition-for-attention mechanism mathematically, showing that dot-product competition creates dynamical tipping points (n*) where behavior transitions from safe to unsafe — providing the theoretical framework for why cumulative inertia across turns can push the system past a tipping point that single-turn defenses like DETAM cannot prevent. **Multi-turn safety benchmarking:** Yang et al. (arXiv 2026) document 16% average ASR increase on MT-AgentRisk and propose ToolShield (~30% ASR reduction). OpenAgentSafety (ICLR 2026) provides 356 multi-turn, multi-user tasks with real tools. Li et al. (STAR, arXiv:2603.15684) show monotonic drift from refusal representations. MultiBreak (arXiv:2605.01687) provides 10,389 multi-turn adversarial prompts. **Multi-turn safety defenses:** X-Teaming (COLM 2025, arXiv:2504.13203) introduces XGuard-Train, a 30K multi-turn safety training dataset. Models SFT-trained on a 14K subset with LoRA rank-8, lr=1e-4, 3 epochs achieve up to 48.3% vulnerability reduction on Llama-3.1-8B and Qwen-2.5-7B. MUSE-D (EMNLP 2025, arXiv:2509.14651) applies turn-level DPO achieving 24% ASR reduction. X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990) operates at the representation level, reducing multi-turn ASR from 58.5-76.0% to 16.0-25.0% while reducing over-refusal by ~20%. MTSA (Guo et al., ACL 2025, arXiv:2505.17147) performs RL with future rewards, reducing ASR from 74.5% to 23.5%, with the finding that maximum attack effectiveness peaks at round 5 — confirming multi-turn pressure accumulates through discourse dynamics. Agent Safety Alignment (Sha et al., arXiv:2507.08270) proposes unified sandboxed RL with benign/malicious/sensitive taxonomy. STREAM (arXiv:2506.00668) proposes safety reasoning moderator reducing ASR by 51.2%. TurnGate (arXiv:2605.05630) introduces turn-level harm detection. **Discourse dynamics:** Wan et al. (ICML 2026, arXiv:2602.03664; note: also submitted to ICLR 2026 as OpenReview #UubLs3lUfk, subsequently published in PMLR 306 at ICML 2026, Seoul, July 6-11) identify conversational inertia and propose CPL. The paper characterizes diagonal attention only at the aggregate level — explicitly stating 'All attention heads are averaged to create a unified attention matrix' and 'the trend of diagonal attention in the final layer is similar to other layers' — with no per-head decomposition. Code not released. **Safety attention head mechanisms:** Zhou et al. (ICLR 2025, arXiv:2410.13708) show the single most critical head in Llama-2-7B-Chat is Head (2, 26) at Layer 2. Wei et al. identify safety layers at layers 9-14. The refusal direction (Arditi et al.) is strongest around layer 15. Safety Alignment Should Be Made More Than Just A Few Attention Heads (arXiv:2508.19697) proposes distributed safety head training. **Safety persistence:** Plaut (arXiv:2603.02229) shows LoRA safety DPO persists with 90-94% retention, Pareto frontier R-squared=0.77, slope=-0.83. **DPO length bias:** Park et al. (2024) and Meng et al. (2024) document hidden length dependence. **Gap:** Despite convergent progress on inference-time attention reallocation (DETAM), training-time targeted head intervention (ASGuard), training-time safety defenses (XGuard-Train, MUSE-D, X-Boundary, MTSA), safety head localization (Zhou et al., AISA, Depth Charge), attention competition theory (Johnson & Huo), and discourse dynamics (conversational inertia), no work has: (a) tested whether a training-time discourse intervention achieves broad DETAM-like attention reallocation and causally reduces safety erosion in multi-turn settings — addressing the progressive accumulation that both DETAM (single-turn only) and ASGuard (circuit-specific only) cannot; (b) provided a per-head decomposition of diagonal attention to determine whether inertia heads overlap with safety heads; (c) compared discourse-targeted vs. safety-targeted training under matched parameter budgets; or (d) controlled for DPO response-length confounds in discourse-safety evaluations.

## Approach
We run a five-phase causal study on MT-AgentRisk (primary) and OpenAgentSafety (secondary) benchmarks using Qwen3-8B and Llama 3.1-8B-Instruct, organized around the 'attention capacity competition hypothesis' and motivated by a specific gap that neither DETAM nor ASGuard can address: progressive multi-turn safety erosion through cumulative discourse dynamics.

**Why Training-Time Discourse Intervention? The Multi-Turn Intent Distribution Problem.** DETAM achieves 97%+ ASR reduction in single-turn settings at zero training cost — but it requires identifying 'intent tokens' at runtime. In multi-turn crescendo attacks where harmful intent is progressively distributed across 3-10 turns (MTSA finds peak attack at round 5), no single set of tokens constitutes 'the intent.' The malicious instruction at turn 7 is only harmful in the context of the innocuous-seeming turns 1-6 that established the frame. DETAM cannot solve this because its mechanism — amplifying attention to intent tokens in sensitive heads — presupposes that intent is localizable within a single turn. ASGuard demonstrates training-time head modification is feasible but targets specific localizable circuits (tense jailbreaking), and its own Limitations section notes 'efficacy hinges on localizable causal circuits.' Multi-turn safety erosion through cumulative inertia is NOT a localizable circuit — it's a progressive process where each turn incrementally shifts the attention distribution. CPL's advantage is that it operates at the discourse dynamics level: reducing the cumulative inertia that progressively dilutes safety attention across turns, without needing to identify which tokens are 'intent' tokens or which circuits carry a specific vulnerability. It addresses the ROOT CAUSE (attention inertia accumulation across turns) rather than the SYMPTOM (misallocated attention at any single turn). This is the failure mode that Johnson & Huo's tipping point theory predicts: gradual accumulation of continuation pressure pushes the system past n* — and the only way to prevent reaching the tipping point is to reduce the per-turn accumulation rate, which is exactly what CPL does.

**The Attention Capacity Competition Hypothesis (Three-Level Framework):** We theorize that diagonal attention (the inertia mechanism) competes with safety-keyword attention at three distinct levels: **Level 1 (Head-level, strong form):** If diagonal attention and safety attention share the same heads, softmax's zero-sum constraint directly displaces safety-keyword attention. Given that safety heads span layers 2-27 and induction/copying mechanisms typically concentrate in middle layers, partial overlap is plausible. **Level 2 (Layer-level, medium form):** If diagonal and safety attention occupy different heads within the same or adjacent layers, competition occurs through the residual stream. This is supported by Deng et al.'s finding that continuation heads (Layer 13) antagonize safety heads (Layers 25-27), and strikingly corroborated by ASGuard's identification of 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30) — the same layer where continuation heads reside, independently confirming Layer 13 as a nexus of safety-relevant competition. **Level 3 (Representation-level, weak form):** Competition mediated through accumulated representation drift, validated by X-Boundary's success (ASR 58.5% to 16.5%). Phase 0.5 empirically determines which level(s) apply.

**Phase 0 — CPL Acquisition/Reproduction + Baseline Preparation (weeks 1-3):** Contact Wan et al. for CPL checkpoints (ICML 2026 July 6-11). Simultaneously reproduce CPL using TRL DPOTrainer + PEFT: LoRA rank-16, alpha-16, 0.4% params, DPO with beta=0.01, sigmoid loss, 2 epochs, lr=5e-7, AdamW, 1000 preference pairs per environment. The training recipe maps directly to TRL v1.0+ (sigmoid loss is the default DPOConfig, all hyperparameters natively supported); the main reproduction risk is the preference pair construction pipeline (dual-rollout with long-context vs. short-context on AgentGym environments) rather than the training loop itself. Estimated: ~40 A100-hours per model. In parallel, prepare XGuard-Train SFT baselines: (a) LoRA rank-8 with lr=1e-4, 3 epochs (matching published configuration from X-Teaming, validated on Llama-3.1-8B and Qwen-2.5-7B); (b) LoRA rank-16 with CPL-matched hyperparameters for parameter-matched comparison. Construct extended-turn variants: prepend 4-6 benign tool-use turns to 50 representative MT-AgentRisk tasks.

**Hard Go/No-Go Checkpoint at Week 3:** The project proceeds to Phase 0.5 only if ALL criteria are met: (1) AgentGym environment setup working for >=3 of 8 environments (prioritizing ALFWorld, WebShop, HotpotQA); (2) dual-rollout preference pair generation produces pairs where long-context trajectories show measurably higher diagonal attention scores than short-context trajectories (statistically significant at p<0.05 on at least 2 environments); (3) DPO training pipeline converges (decreasing loss, increasing reward margins over 2 epochs); (4) base model evaluation on >=2 environments matches Wan et al.'s published baselines within 1 SEM. **Fallback paths:** (a) environment failure: proceed with 2-3 most reliable environments; (b) inertia differential failure: pivot to correlational-only study (Phases 1 and 4 only); (c) training failure: debug 1 additional week — if still failing by week 4, pivot to 'DETAM in multi-turn settings' (extending DETAM's mechanism to MT-AgentRisk, testing whether Focus Loss intensifies across turns).

**Phase 0.5 — Head Overlap Test and Per-Head Diagonal Attention Decomposition (weeks 3-4, ~20 A100-hours):** This phase provides the first per-head decomposition of diagonal attention patterns and tests the prerequisite assumption of the competition hypothesis. Using both base models on 50 MT-AgentRisk tasks: (a) **Novel per-head diagonal attention decomposition:** Compute diagonal attention scores per head (not just aggregate) using Wan et al.'s metric (attention between current output position i and previous assistant output position i +/- 5 tokens) — this is the first such decomposition, given that Wan et al. explicitly average all heads ('All attention heads are averaged to create a unified attention matrix'). Identify which heads carry the strongest diagonal patterns and their layer distribution. (b) **Safety head identification via triple triangulation:** Apply three complementary methods: (i) Ships score (Zhou et al., ICLR 2025) via KL divergence after head ablation; (ii) DETAM's sensitivity metric (attention score differences between successful/unsuccessful safety responses); (iii) AISA's spatiotemporal analysis — linear probing on head outputs at final structural tokens to identify safety-discriminative heads (K=16). Cross-validate against published localizations: Zhou et al.'s Head (2,26) for Llama-2-family; Depth Charge's layer-specific data (layer 7 for Llama 3.1-8B); ASGuard's EAP-IG identified heads (11 heads for Llama-3.1-8B including 4 at Layer 13). Using three independent methods plus cross-validation against three published head sets provides robust head identification. (c) **Overlap analysis:** Compute Jaccard index between top-k diagonal attention heads and top-k safety heads (k = 5, 10, 20, 50) with permutation tests. Also measure layer-level co-occurrence (same layer, different heads). Cross-reference against ASGuard's Layer 13 vulnerable heads — if diagonal attention heads concentrate at Layer 13, this would connect conversational inertia to the continuation-safety competition nexus identified by both Deng et al. and ASGuard independently. (d) **Level determination:** Level 1 (>30% head overlap) — proceed with strong per-head softmax hypothesis; Level 2 (same layers, <30% head overlap) — reformulate around residual stream competition, particularly the Layer 13 continuation-inertia-safety nexus; Level 3 (<10% overlap in both heads and layers) — reformulate around representation-level competition. Each determination shapes subsequent analysis. This phase costs ~20 A100-hours but de-risks the project and provides standalone novel contributions (first per-head diagonal attention map; first triple-method safety head identification comparison).

**Phase 1 — Correlational with Attention Capacity Analysis (weeks 4-7):** Measure diagonal attention (per-head, informed by Phase 0.5) AND safety-keyword attention concentration at each turn on 365 MT-AgentRisk tasks and 50 extended-turn variants. Calibrate analysis to competition level from Phase 0.5. Fit mixed-effects regressions testing P1 (diagonal attention negatively correlates with safety attention at the operative level), controlling for turn position, task category, model, and response token count. Test Granger causality for temporal dynamics.

**Phase 2 — Interventional with Confound Controls (weeks 7-11):** Apply CPL and re-evaluate on MT-AgentRisk. Five control conditions: (a) **Random-Preference LoRA** — shuffled preference labels, same architecture; (b) **Reversed-CPL** — prefer long-context over short-context; (c) **XGuard-Train SFT (rank-8)** — published configuration for validation against published results; (d) **XGuard-Train SFT (rank-16)** — CPL-matched parameters for direct paradigm comparison (discourse-targeted vs. safety-targeted training); (e) **Response-Length Analysis** — ASR stratified by length quartiles, per-100-token normalization, regression with length covariate (testing P3: CPL's safety effect, if any, is not explained by response-length changes). Frame CPL's effect relative to both DETAM and ASGuard: test whether CPL affects the same heads DETAM identifies as sensitive and shifts attention in the same direction (implicit DETAM test), and whether it affects ASGuard's identified vulnerable heads at Layer 13 (implicit untargeted circuit modification test). Compare against ToolShield baseline and MUSE-D's published results.

**Phase 3 — Autonomy Tax Audit (weeks 9-11, parallel):** Step-1 completion rate, cascade failure rate, end-to-end success, over-refusal. Report safety-competence Pareto frontier extending Plaut's analysis. Compare CPL's frontier position with X-Boundary's ~20% over-refusal reduction, ASGuard's Pareto-optimal balance, and XGuard-SFT's published results.

**Phase 4 — Mechanistic Verification (weeks 10-14):** (a) SRI signal framework for step-wise refusal dynamics; (b) Head-level analysis extending Deng et al.'s safety-continuation head identification to multi-turn, calibrated by Phase 0.5 overlap findings — test whether CPL modulates the Layer 13 continuation vs. Layer 25-27 safety head balance across conversation turns; (c) **DETAM-informed analysis:** Apply DETAM's sensitivity metric to CPL-treated models — does CPL training shift attention in the same heads and direction that DETAM targets at inference time? If so, CPL achieves 'implicit DETAM' through discourse training, but persistently and without runtime intent localization; (d) **ASGuard-informed analysis:** Test whether CPL affects ASGuard's identified vulnerable heads (particularly the 4 at Layer 13) despite not targeting them — this would demonstrate that untargeted discourse training can modify the same heads that targeted circuit analysis identifies, but as a side effect of reducing general inertia rather than through explicit circuit surgery; (e) Level-appropriate analysis: Level 2 — residual stream composition analysis at shared layers; Level 3 — representation trajectory analysis following X-Boundary's framework.

**Secondary Evaluation — OpenAgentSafety (weeks 12-14):** Best-performing config and XGuard-SFT on a subset for ecological validity.

**Null-Result Framing Strategy:** (1) First per-head decomposition of diagonal attention patterns and their overlap (or non-overlap) with safety heads — novel regardless of CPL results; (2) First triple-method safety head identification comparison (Ships + DETAM sensitivity + AISA spatiotemporal), cross-validated against three published head sets (Zhou et al., Depth Charge, ASGuard); (3) Empirical evidence for or against the three-level competition hierarchy; (4) First confound-controlled causal framework for discourse-safety evaluation; (5) First discourse-targeted vs. safety-targeted training comparison under matched parameters; (6) First multi-turn extension of DETAM's Focus Loss analysis; (7) Empirical test of whether CPL-like untargeted training affects the same heads as ASGuard's targeted circuit intervention.

**Extended-Turn Variant Validity (Limitation):** Acknowledged with mitigations: OpenAgentSafety for ecological validity, attention pattern validation, conservative amplification framing.

All primary experiments use MT-AgentRisk (365 tasks), ToolShield codebase (GitHub: CHATS-lab/ToolShield), XGuard-Train (HuggingFace: marslabucla/XGuard-Train), and the CPL training recipe from Wan et al. (ICML 2026).

## Resource Estimate
{'manual': {'gpu_hours': '720-900 A100-hours (CPL reproduction 2 models ~80h, XGuard-SFT rank-8 + rank-16 training 2 models ~60h, 2 control LoRAs for 2 models ~80h, Phase 0.5 head overlap test with AISA probing ~25h, MT-AgentRisk evaluation across 6 conditions x 2 models ~240h, extended-turn evaluation ~40h, OpenAgentSafety subset ~60h, SRI signal analysis ~30h, attention analysis including per-head diagonal decomposition + DETAM-informed + ASGuard-informed metrics ~85h, head-level safety-continuation analysis ~40h, response-length analysis ~10h)', 'timeline': '15-17 weeks (3 weeks Phase 0 + go/no-go, 1 week Phase 0.5, 3 weeks Phase 1, 4 weeks Phase 2 + Phase 3 parallel, 4 weeks Phase 4 + OpenAgentSafety, 3 weeks writing; comfortable for ICLR 2027)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}, 'human_in_loop': {'gpu_hours': '720-900 A100-hours', 'timeline': '13-15 weeks (Claude accelerates CPL reproduction, Phase 0.5 triple-method pipeline, DETAM/ASGuard comparison metrics, statistical analysis)', 'claude_api_cost': '$300-450 (CPL reproduction, per-head diagonal decomposition, triple-method head overlap analysis, DETAM/ASGuard-informed metrics, experiment orchestration, statistical modeling)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}, 'auto_research': {'gpu_hours': '920-1140 A100-hours (additional automated sweeps, full OpenAgentSafety evaluation, extended ablation across competition levels, comprehensive per-head analysis with triple methods)', 'timeline': '9-11 weeks (parallelized execution, automated Phase 0.5 -> Phase 1 pipeline)', 'claude_api_cost': '$600-850 (end-to-end orchestration including CPL reproduction, triple-method head analysis, DETAM/ASGuard comparison, control sweeps, result interpretation, draft generation)', 'estimated_gpu_cost': '$1380-1710 at $1.50/A100-hr spot pricing', 'speed_bottleneck': 'Sequential multi-turn interaction generation; 12 model configurations (2 models x 6 conditions); Phase 0.5 is a serial dependency before Phase 1; triple-method safety head analysis computationally intensive'}}

## Inspired By
Field guide Section 4 (cascading failures, production gap) + Section 5.2 (error propagation as primary bottleneck). Key insight: DETAM's demonstration that inference-time attention reallocation dramatically improves safety (ASR 46% to 1.2%) establishes the empirical foundation for our hypothesis — if explicitly redirecting attention works, does implicit redirection via discourse training also work? ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities raises the natural question: can untargeted discourse training achieve what targeted circuit intervention achieves, but for the progressive multi-turn erosion that circuit-based approaches cannot address? The three-level competition hierarchy was motivated by the finding that Wan et al. only characterizes diagonal attention at the aggregate level (explicitly averaging all heads into a unified matrix) and that safety heads span multiple layer ranges (L2, L9-14, L25-27), while continuation heads at Layer 13 overlap with both induction/copying head territory and ASGuard's identified vulnerable heads (4 of 11 Llama-3.1-8B vulnerable heads are at L13). Johnson & Huo's (2026) formalization of attention competition tipping points provides the theoretical framework for why cumulative discourse inertia can push multi-turn interactions past a safety threshold that per-turn defenses cannot prevent. The reviewer's observation about per-head specificity led to Phase 0.5, which provides the first per-head decomposition of diagonal attention — a novel contribution regardless of results. AISA's spatiotemporal analysis provides methodological triangulation for safety head identification, strengthening Phase 0.5's robustness.

## Target Venues
- ICLR 2027 (abstract September 19 2026, full paper September 24 2026 [estimated] — primary target, ~18 weeks from project start, comfortable timeline with 3+ weeks buffer including Phase 0.5)
- AAAI 2027 (abstract July 21 2026, full paper July 28 2026 — stretch target, ~10 weeks; feasible only if CPL checkpoints obtained by week 2, Phase 0.5 shows Level 1 or 2 overlap, and Phase 1 results are clean)

## Key References
- DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings, arXiv:2504.13562)
- ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026, arXiv:2509.25843)
- AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks (Song et al., arXiv:2602.13547, Feb 2026)
- Multi-Turn Jailbreaking Large Language Models via Attention Shifting (ASJA, AAAI 2025)
- Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026, arXiv:2602.03664)
- Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents (Yang et al., arXiv 2026)
- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents (COLM 2025, arXiv:2504.13203)
- MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety (EMNLP 2025, arXiv:2509.14651)
- X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability (Lu et al., EMNLP 2025, arXiv:2502.09990)
- MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming (Guo et al., ACL 2025, arXiv:2505.17147)
- Agent Safety Alignment via Reinforcement Learning (Sha et al., arXiv:2507.08270)
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut, arXiv:2603.02229, March 2026)
- The Struggle Between Continuation and Refusal (Deng et al., arXiv:2603.08234, Mar 2026)
- The Autonomy Tax: Defense Training Breaks LLM Agents (Li & Zhao, arXiv:2603.19423, Mar 2026)
- On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025, arXiv:2410.13708)
- Depth Charge: Jailbreak Large Language Models from Deep Safety Attention Heads (Wu et al., arXiv:2603.05772, Mar 2026)
- Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., arXiv:2508.19697, 2025)
- Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, arXiv:2602.14370, Feb 2026)
- Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment (Zaree et al., arXiv:2502.15334, Feb 2025)
- Safety Layers in Aligned Large Language Models (Wei et al., arXiv:2408.17003, 2024)
- Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., arXiv:2406.11717, 2024)
- State-Dependent Safety Failures in Multi-Turn Language Model Interaction (STAR, arXiv:2603.15684, Mar 2026)
- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026, arXiv:2507.06134)
- One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue (TurnGate, arXiv:2605.05630, May 2026)
- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv:2605.01687, May 2026)
- STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (arXiv:2506.00668, May 2025)
- Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions (arXiv 2026)
- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2026)
- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv 2025)
- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction (arXiv 2026)
- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv 2026)
- Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction (arXiv 2026)
- Asking Forever: Universal Activations Behind Turn Amplification (arXiv:2602.17778, Feb 2026)
- Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models (arXiv:2602.02600, Feb 2026)
- Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection (arXiv:2604.28129, Apr 2026)
- Many-Turn Jailbreaking (arXiv:2508.06755, Aug 2025)
- Disentangling Length from Quality in Direct Preference Optimization (Park et al., arXiv:2403.19159, 2024)
- Length Desensitization in Direct Preference Optimization (Meng et al., arXiv:2409.06411, 2024)
- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., USENIX Security 2025, arXiv:2404.01833)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c6de8b04-e2d5-4298-8b62-ff2c819fd45e",
  "type": "user",
  "uuid": "35e1cd52-e5f5-4397-b20d-7b9c4655ef2c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:49:12.151Z_

```json
{
  "parentUuid": "35e1cd52-e5f5-4397-b20d-7b9c4655ef2c",
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
  "uuid": "63d71dc7-a734-40bf-8c99-47b6c1951528",
  "timestamp": "2026-05-20T03:49:12.151Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:49:12.151Z_

```json
{
  "parentUuid": "63d71dc7-a734-40bf-8c99-47b6c1951528",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b1eced42-7751-4940-bd10-1684569e0fd1",
  "timestamp": "2026-05-20T03:49:12.151Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make a well-grounded asse…",
  "leafUuid": "b1eced42-7751-4940-bd10-1684569e0fd1",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Testing attention competition hypothesis in multi-turn LLM safety",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:49:53.211Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them according to the Meta Judge format.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 27%

**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强


- Probability: [22% - 33%] 中位 27%

**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 27%

The three reviewers show striking agreement across all dimensions. Computing the statistics, all three median estimates converge at 27% with zero standard deviation, indicating exceptional consistency in their independent assessments. All three reviewers unanimously rated novelty, significance, and related work coverage at the same levels.

The core tension they identify is consistent: applying an existing method (CPL) to a new domain (safety) represents a bridge study rather than fundamental methodological innovation. While they acknowledge the genuine contribution of per-head decomposition and recognize that no prior work has tested CPL for safety, they all flag concerns about the three-level hypothesis framework. On significance, all three note the "I would have guessed this" risk and point to direct safety training as a simpler, already-validated alternative, though they recognize multi-turn safety as a genuinely important problem. The related work coverage earns unanimous praise for comprehensiveness and accuracy.

Beyond these consensus points, they surface several shared vulnerabilities: the perception that this is primarily an application study, the risk that Phase 0.5 might reveal low head overlap and undermine the theoretical narrative, uncertainty about whether CPL's effects trained on agentic tasks will transfer to safety scenarios, and ambiguity around causal direction that all three reviewers flag in different ways. One outlier observation comes from R3, who caught a very recent reference (May 2026) that the others missed, though given its publication date this isn't a critical omission. R2's anomalous point appears incomplete in the notes.

The consistency metrics are striking—all three reviewers converged on identical median scores (27%) with zero standard deviation, and they unanimously rated novelty, significance, and related work the same way. Given this near-perfect alignment on risk assessments, I should weight their shared concerns heavily.

Looking at the confidence intervals, there's substantial overlap: R1 and R3 both span 22-32%, while R2 extends slightly to 33%. The intersection is tight at 22-32%, which gives me confidence to anchor on 27% as the central estimate.

Now I'm reviewing the implementation details all three flagged—the GPU requirements (720-900 A100-hours), the 15-17 week timeline, and the dependencies on CPL reproduction and phase overlap analysis. They're consistent that no new benchmarks or human annotation are needed, just the training work for CPL reproduction.

With the median locked at 27%, this falls below the 36% threshold. The consensus is clear: the work has genuine merit and addresses a real gap, but it's fundamentally constrained as an application study without sufficient novelty. This leans toward "不推荐" rather than "通过." 边缘" — there's potential to improve with iteration, but the ceiling is constrained by the nature of the idea.

Wait, let me reconsider the "建议" options: 强推荐 / 边缘 / 不推荐 / KILL / 人工复核

At 27% median with all reviewers agreeing, this is solidly in "边缘" territory — not terrible enough for KILL or 不推荐, but not strong enough for anything better. The key question is whether iteration can push it above 36%.

The ceiling is limited by Novelty (中) and Significance (中). All three reviewers agree that even with perfect execution, the "I would have guessed this" factor limits the upside. However, there might be room to sharpen the framing and strengthen the novelty angle.

I'll go with "边缘" — the work shows promise but needs substantial refinement to break through.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1eced42-7751-4940-bd10-1684569e0fd1",
  "isSidechain": false,
  "requestId": "req_011CbD8yAZP9UsS1FW713gBp",
  "type": "assistant",
  "uuid": "6cc0f078-57b7-44bc-ac36-29586e5b5e9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZydkYPJpSoMw6VxSkMac1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 30841,
      "cache_read_input_tokens": 11374,
      "output_tokens": 4252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4252,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 30841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30841
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

_source line 9 · 2026-05-20T03:50:53.159Z_

【阶段】: Meta Judge
【三次中位】: [27%, 27%, 27%]  std=0%
【共识维度】: 
- **Novelty = 中**（3/3 一致）：核心贡献是"将已有方法 CPL 应用于新评估维度 safety"，属 bridge/application study 而非方法论创新。Gap 真实（搜索确认无直接竞争工作），per-head diagonal attention 分解是真正的分析性新贡献，但 conceptual leap 有限——"减少注意力竞争改善安全"是已知组件（softmax 零和 + safety heads + diagonal attention）的自然推论。三级假设框架有 unfalsifiable 之嫌（任何结果都可归入某个 level）。
- **Significance = 中**（3/3 一致）：多轮安全是重要问题，但核心发现的 surprise factor 有上限——正面结果审稿人可能说"I would have guessed this"（训练改善 context 处理自然也改善安全），负面结果则贡献降级为分析性工作。即使所有假设被验证，practical takeaway 有限（practitioners 仍会选择直接安全训练）。
- **Related Work = 强**（3/3 一致）：文献覆盖极其全面且描述准确（DETAM、ASGuard、Wan et al.、Deng et al.、Johnson & Huo、Zhou et al.、AISA 等均经调研验证），gap 识别真实，差异化定位清晰诚实。
- **Trivial alternative 威胁显著**（3/3 一致）：直接安全训练（XGuard-Train SFT 已实现 48.3% vulnerability reduction）是成本更低、效果已验证的替代方案。CPL 的增量价值完全依赖于"不用安全标注数据就能改善安全"这一属性，且需效果足够显著才有说服力。
- **"Apply X to Y" 感知风险**（3/3 一致）：审稿人极可能将论文定性为 application study，核心操作是将 Wan et al. 的 CPL 应用于安全评估，方法论工具全部现成。
- **Head overlap 假设风险**（3/3 一致）：如果 Phase 0.5 显示低重叠（Level 3），整个 "attention capacity competition" 叙事退化为 "representation drift"，与 X-Boundary 等已有工作的差异化空间被压缩，novelty 进一步下降。
- **CPL 效果迁移假设未验证**（3/3 一致）：CPL 在 agentic 环境训练，迁移至安全场景的效果不确定，两种场景的 attention dynamics 可能有根本差异。
- **因果方向歧义**（3/3 均提到变体）：diagonal attention 与安全退化可能是 confounded by conversation length/complexity 的伴随现象而非因果关系。

【异常维度】: 
- R3 独有：发现 "When Attention Closes"（arXiv:2605.12922, May 2026）与 proposal 有显著概念重叠（多轮 attention 衰减、GAR 指标）。该论文 May 13 发表，可能晚于 proposal 撰写，但需关注差异化。信号有效但权重适度——属新增文献而非致命遗漏。
- R2 独有：明确指出"逐轮 DETAM"应作为 baseline——每轮将 user input 视为 intent 直接应用 DETAM，测试是否足够有效。合理建议但仅 1 人提出，降权处理。
- R3 独有：指出 Johnson & Huo 论文来自物理系，是 analogy/框架而非 NLP 社区的 empirical 发现，审稿人可能质疑对 transformer 内部机制的直接适用性。有效观察但不影响核心判断。
- R2 独有：区分"response quality confound"与"response length confound"——CPL 让模型全局 "更 thoughtful" 的效应比长度更难控制。有效的实验设计提醒。

【最终概率】: [22% - 32%] 中位 27%
【一致性】: 高（std = 0%，三位审稿人在所有 rubric 维度和中位数上完全一致，区间高度重叠 [22-32] / [22-33] / [22-32]）
【综合理由】: 
三位审稿人独立到达完全一致的判断——这在审稿中极为罕见，说明 proposal 的优劣势信号非常清晰：

**概率上限（~32%）由 idea 质量硬性限制：** Novelty 和 Significance 均为"中"意味着即使实验执行完美，论文的天花板在 ~35%。核心制约是 surprise factor——无论 CPL 对安全的效果是正面还是负面，结果都在审稿人的预期范围内。正面："改善 attention 分布自然也改善安全"；负面："不在安全数据上训练当然不能有效改善安全"。真正的 surprise 需要 CPL 在安全上超过专门的安全训练（highly unlikely）或发现极精确的机制联系（Level 1 >50% overlap），但这些是 empirical gambles 而非 idea 内在的 significance。

**概率下限（~22%）由 Related Work 和 standalone 贡献支撑：** 文献覆盖强、gap 真实、per-head 分解和 triple-method 比较是独立贡献、实验设计含 5 个 confound controls。即使主假设失败，fallback value 真实存在。

**中位锚定在 27% 的核心原因：** 这是一个 well-designed empirical investigation of a real gap，但不是一个 conceptual breakthrough。审稿人对 bridge study 的容忍度取决于发现的 surprise level，而这个 proposal 的最可能结果恰恰落在"neither surprising nor trivial"的灰色地带。三级假设的 unfalsifiable 特性可能被视为 hedging（降低科学严谨性评价），而非增强稳健性。

鉴于 std=0% 的极高一致性，无需进行偏向调整，直接取共识值。区间取三位审稿人区间的交集 [22%-32%]。

【建议】: 边缘
【实施评估】:
  - 计算资源: 720-900 A100-hours（~$1080-1350 spot pricing），涵盖 CPL 复现（~80h×2 models）、XGuard-SFT 训练（~60h）、控制组 LoRA（~80h）、Phase 0.5 head 分析含 AISA probing（~25h）、MT-AgentRisk 全条件评估（~240h）、扩展轮次评估（~40h）、OpenAgentSafety 子集（~60h）、机制分析（~155h）、响应长度分析（~10h）。对学术团队而言属中等规模，需稳定的多 GPU 集群访问。
  - 数据需求: MT-AgentRisk（365 tasks，公开）、OpenAgentSafety（356 tasks，公开）、XGuard-Train（HuggingFace 公开）、AgentGym 环境（CPL 复现用）。所有数据集公开可得，无数据瓶颈。
  - 人工介入: 无需人工标注。主要人工工作是 CPL 复现的工程调试（preference pair 构建 pipeline 是主要风险点）、Phase 0.5 head 分析的解读、以及与 Wan et al. 联系获取 checkpoints。需 1-2 名具备 mechanistic interpretability 经验的研究者。
  - 训练需求: 需要训练——CPL 复现（LoRA rank-16 DPO，2 个 8B 模型）、XGuard-SFT（rank-8 和 rank-16 各 2 个模型）、2 个控制组 LoRA（随机偏好 + 反向 CPL）。模型规模 7-8B 参数，单次训练可在单卡 A100 完成，总训练量约 300 A100-hours。
  - 新 Benchmark: 不需要构建新 benchmark。使用已有的 MT-AgentRisk 和 OpenAgentSafety。需构建 extended-turn variants（50 个任务前置 4-6 轮良性交互），工作量较小。
  - 预估周期: 15-17 周（Phase 0 含 go/no-go 3 周 → Phase 0.5 head 分析 1 周 → Phase 1 相关性分析 3 周 → Phase 2+3 干预实验 4 周 → Phase 4 机制验证 + OpenAgentSafety 4 周 → 写作 3 周）。关键路径依赖：CPL 复现成功（Week 3 go/no-go）和 Phase 0.5 结果决定后续分析框架。若目标 EMNLP 2026（假设 deadline 约 2026 年 6 月），时间非常紧张；若目标 ICLR 2027（September 2026），timeline 较为宽裕。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cc0f078-57b7-44bc-ac36-29586e5b5e9f",
  "isSidechain": false,
  "requestId": "req_011CbD8yAZP9UsS1FW713gBp",
  "type": "assistant",
  "uuid": "09acd29e-84bf-4a6a-88bd-8fca52144e81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZydkYPJpSoMw6VxSkMac1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 30841,
      "cache_read_input_tokens": 11374,
      "output_tokens": 4252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4252,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 30841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30841
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make a well-grounded asse…",
  "leafUuid": "09acd29e-84bf-4a6a-88bd-8fca52144e81",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Testing attention competition hypothesis in multi-turn LLM safety",
  "sessionId": "e10f70ec-57b9-40a7-ac79-90fdae8bdf74"
}
```

---
