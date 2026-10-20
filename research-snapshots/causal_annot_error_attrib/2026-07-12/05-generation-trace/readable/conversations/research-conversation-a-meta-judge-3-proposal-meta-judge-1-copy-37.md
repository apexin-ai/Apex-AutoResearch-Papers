# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/1e56692f-e883-4f9b-9710-09e3dca40b3e.jsonl`
- **Structured JSON:** [`ac9b68ae9c92e73d891e.json`](../../sessions/ac/ac9b68ae9c92e73d891e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:38:35.998Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:38:35.998Z",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient field context. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n```\n\n## ⚠️ 关键前置问题：CoRL 2026 严重的 Venue Mismatch\n\n在正式评估 idea 质量之前，必须指出一个**致命的投稿策略问题**：\n\n**CoRL (Conference on Robot Learning)** 的 Call for Papers 明确要求 \"Submissions should focus on a core robotics problem\" 并且 \"Submissions without a robotics focus will be returned without review.\" 这篇 proposal 是一个纯 HCI/Human-AI Interaction 的工作——浏览器扩展检测用户对 LLM 的过度依赖并触发干预——**完全不涉及机器人学习**。如果投稿 CoRL 2026，极大概率会被 desk reject。\n\nProposal 自身列出的目标会议（CHI、IUI、CSCW、IMWUT、AAAI）才是正确的 venue。以下评估基于 idea 本身的学术质量，**以 CHI/IUI 等 HCI venue 为参照系**进行打分。如果用户确实要投 CoRL，概率接近 0%。\n\n---\n\n```\n【领域调研】:\n```\n\n- **[Liu et al., arXiv 2602.11567] (CHI 2026)**: 确认存在。77 名参与者，3 个任务，通过 autoencoder 聚类发现 5 种行为模式区分高/低过度依赖用户。提供了行为信号词汇表，但明确将实时检测和干预留作 future work。这是本 proposal 最直接的前置工作。\n- **[Srinivasan & Thomason, arXiv 2502.13321] (IUI 2026)**: 确认存在。Trust-adaptive intervention，38% 不当依赖降低，但要求每次决策后 11 分量表自报告。Appendix D 的行为估计失败 (F1 ≤ 0.5) 是本 proposal 的核心 motivation。\n- **[Ailin Liu et al., arXiv 2602.00880] (CHI 2026)**: 确认存在。最接近的架构先例——用鼠标+EDA 构建闭环系统，但目标是认知负荷（非过度依赖），需要生理传感器，线性回归分类器仅~61%。\n- **[Campagna et al., arXiv 2601.19856] (RA-L 2025)**: 确认存在。HRI 场景中行为指标预测信任达 84% 准确率 (AUC=0.90)，但样本量极小 (N=14)，且是物理机器人场景——与 LLM 对话场景的 domain gap 非常大。\n- **[Raees & Papangelis, arXiv 2604.23896] (2026)**: 确认存在。区分 trust 和 appropriate reliance 的测量理论工作，为用行为过程指标替代主观信任评分提供了理论基础。\n- **调研总结**: 这个领域处于一个「识别信号→构建系统」的过渡阶段。Liu et al. (CHI 2026) 建立了行为信号基础，Adjust for Trust (IUI 2026) 验证了自适应干预的价值但暴露了行为检测的失败，Sensing What Surveys Miss 建了闭环但在不同任务域且依赖生理传感器。**确实存在一个尚未被填补的 gap：纯行为信号→实时检测→自适应干预，在 LLM 对话场景中。** Proposal 对 gap 的定位是准确的。\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在 partial trivial alternatives，但 proposal 有增量价值。**\n\n1. **最简单的 baseline**：基于规则的启发式（如 Adjust for Trust Appendix D 中尝试的 AIAcc5、CapabilityDiff 等）。但已有证据表明这些方法 F1 ≤ 0.5，不可用。这恰恰是 proposal 的 motivation。\n2. **次简单的 baseline**：用 Liu et al. 识别的 5 种模式直接写规则触发干预（无需训练 CNN）。这是一个 **真正的威胁**——proposal 对此的回应是 weak supervision circularity ablation（条件 i vs ii），设计合理，但**核心问题是：多分辨率 CNN 相比手写规则的增量到底有多大？** 如果 ablation 显示 CNN 只是重新学习了手写规则（条件 iv ≈ 条件 i），则整个检测模块的技术贡献大打折扣。\n3. **另一个 trivial alternative**：不做实时检测，而是在固定时间点（如用户 paste 后、长时间不编辑时）触发静态干预。这种 event-triggered 方法成本极低，可能效果不差。\n\n**增量价值判断**：proposal 的增量在于 (a) 连续流式检测 vs 离散事件触发，(b) 个性化风险阈值 vs 固定规则，(c) 分层干预 vs 单一干预。但这些增量是否能在 empirical results 中体现显著差异，取决于行为信号本身的信息量——这正是核心风险。\n\n---\n\n```\n【前提假设检验】:\n```\n\n核心逻辑链中有**两个关键的未验证假设**：\n\n1. **「行为信号在 LLM 对话场景中包含足够信息来区分过度依赖 vs 非过度依赖，且多分辨率时序建模能提取这些信息」**——这是整个 proposal 的核心赌注。支撑证据来自不同领域（HRI 物理协作、无人机模拟），domain gap 非常大。Adjust for Trust 在**同一领域**的失败 (F1 ≤ 0.5) 和 Sensing What Surveys Miss 加了 EDA 也才 ~61% 的事实，实际上是**反面证据**。Proposal 的论点是\"失败在于建模深度不够\"，但同样合理的解释是\"行为信号本身在这个域中信息量不足\"。\n\n2. **「从 Liu et al. 的 outcome-level labels 可以通过 MIL+弱监督成功训练出 window-level 的流式分类器」**——这是一个非平凡的假设。Liu et al. 的标签是 per-task 粒度，而 proposal 需要 per-30-second-window 粒度的预测。MIL 的成功高度依赖于 bag 内 instance 的区分度——如果一个\"过度依赖\"session 中 80% 的 windows 看起来和\"非过度依赖\"session 一样，MIL 的 attention 机制很难收敛。\n\nProposal 对这些风险有所认知（设计了 dual-outcome 框架），但**这些是 idea 层面的根本性不确定性，不是实验设计能完全化解的**。\n\n---\n\n```\n【3 维度打分】:\n```\n\n**1. Novelty: 中** — Gap 定位准确且目前确实无人填补。将 Liu et al. 的行为信号、Adjust for Trust 的干预框架、轻量级时序分类器整合为闭环系统是一个合理的「untried combination」。但核心 novelty 是**系统集成**而非**方法论突破**。每个组件（1D-CNN 时序分类、Snorkel 弱监督、MIL、分层干预）都是已有技术的直接应用。multi-resolution CNN 相比 MiniRocket/BiLSTM 的技术差异化不够强。在 CHI/IUI 这类 venue，系统集成贡献可以被接受，但审稿人可能会说\"this is a well-motivated engineering contribution rather than a methodological advance\"。\n\n**2. Significance: 中偏强** — 研究问题的重要性毋庸置疑：LLM 过度依赖是 2025-2026 HCI 领域的核心议题之一。如果行为检测确实可行，这会解锁一系列后续研究（个性化干预、长期部署、跨平台泛化）。头对头比较 self-report-adaptive vs behavior-triggered adaptive 的实验设计有独立价值。但**核心发现如果 positive（行为信号 work），审稿人大概率会说 \"I would have guessed this would eventually work with enough engineering\"**，而不是 \"surprising\"。如果 negative（行为信号不 work），informative 但影响力有限——因为已有负面证据（Adjust for Trust Appendix D）。\n\n**3. Related Work: 强** — 这是 proposal 最突出的维度。对 Liu et al., Adjust for Trust, Sensing What Surveys Miss, From Text to Trust, Campagna et al., Raees & Papangelis 等关键工作的覆盖非常全面且准确。差异化定位清晰：每篇先行工作缺什么、本 proposal 怎么填补，逻辑链条完整。对 negative evidence (Adjust for Trust Appendix D, Dechant et al.) 的诚实引用增加了可信度。\n\n---\n\n```\n【概率估计】: [25% - 40%] 中位 30%\n```\n\n**注意：此概率估计是针对 CHI/IUI 等 HCI venue，而非 CoRL。投 CoRL 的概率接近 0%（desk reject）。**\n\n```\n【估计理由】:\n```\n\n- **Related Work 强**：定位精准、差异化清晰，这在 CHI/IUI 审稿中是加分项，支撑了概率下界（不至于 <25%）\n- **Significance 中偏强**：问题重要，但核心发现的 surprise factor 不够高，限制了上界无法突破 40%\n- **Novelty 中**：系统集成型贡献，每个组件都是 existing techniques 的直接应用，限制了中位数——在竞争激烈的 CHI 中，纯集成型工作要靠实验结果的 impressive 来补偿 novelty 的不足\n- **核心张力**：整个 proposal 的价值高度依赖于一个高度不确定的实证结果（行为信号是否 work）。如果 work 且效果显著 → 上界 40%（但不会更高，因为方法不够 novel）；如果 moderate (65-70%) → 25-30%（有 informative negative result 的叙事，但影响力有限）；如果 fail → ~20%（purely methodological contribution）\n\n```\n【主要风险】:\n```\n\n1. **行为信号信息量不足风险**：核心赌注——LLM 对话场景中的 mouse/keyboard 行为信号可能确实不含有足够信息来区分 window-level 的过度依赖状态，无论模型多复杂。同领域的负面证据 (F1 ≤ 0.5, ~61% with EDA) 比跨领域的正面证据 (84% in HRI with N=14) 更有参考价值。这不是实验设计能化解的 idea 层面风险。\n\n2. **Novelty 被质疑为\"pure engineering\"风险**：审稿人可能认为这是把 5-6 篇已有工作的组件拼在一起、加了一个 user study 的系统论文，缺乏深层方法论创新。在 CHI 这样投稿量巨大的会议，这类质疑常见于 borderline 论文。\n\nSources:\n- [Liu et al. - Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)\n- [Srinivasan & Thomason - Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Liu et al. - Sensing What Surveys Miss (CHI 2026)](https://arxiv.org/abs/2602.00880)\n- [Campagna et al. - Estimating Trust in HRC (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Raees & Papangelis - From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n```\n\n> ⚠️ **Venue 注意**: 系统模板指定 CoRL 2026（Conference on Robot Learning），但本 proposal 明确目标为 CHI 2027 / IUI 2027 / CSCW 2027 等 HCI 会议。本 proposal 与 CoRL 的主题完全不匹配（无机器人学习内容），若投 CoRL 中稿概率趋近于 0%。**以下评估基于 proposal 自身目标的 HCI 顶会（CHI/IUI）进行。**\n\n---\n\n```\n【领域调研】:\n\n- [Liu et al., \"Behavioral Indicators of Overreliance During Interaction with Conversational Language Models\"](https://arxiv.org/abs/2602.11567) (CHI 2026): \n  本 proposal 的直接前驱。77 名被试 × 3 tasks，注入 misinformation，通过 autoencoder 聚类识别出 5 种与 overreliance 关联的行为模式（如频繁 copy-paste、跳过任务理解、粗粒度黏贴等）。关键局限：仅做 post-hoc 行为特征刻画，明确将 real-time detection 和 intervention 留作 future work。该论文使用 per-event 37 维编码，与 proposal 中的 30×28 temporal grid 表征有明确差异。确认存在且描述准确。\n\n- [Srinivasan & Thomason, \"Adjust for Trust\"](https://arxiv.org/abs/2502.13321) (IUI 2026): \n  Trust-adaptive 干预系统，通过 11 点自报告量表在每个决策后收集信任值，据此选择 supporting 或 counter-explanation。在科学问答和医学诊断任务中实现最高 38% inappropriate reliance 减少。Appendix D 明确记录了 behavioral trust estimation 的失败尝试（F1 ≤ 0.5）。确认存在且描述准确。\n\n- [Liu et al., \"Sensing What Surveys Miss\"](https://arxiv.org/abs/2602.00880) (CHI 2026): \n  结构上最相似的前驱——闭环系统，用鼠标动态 + EDA 皮肤电驱动个性化 linear regression 分类器，在在线问卷中检测 cognitive load 并触发 LLM-based 干预。N=32，aligned-adaptive 条件下准确率提升 21%，false negative 从 50.9% 降至 22.9%。关键差异：(a) 目标是 cognitive load 而非 overreliance；(b) 需要 EDA 腕带；(c) 使用简单线性回归，仅 ~61% 检测准确率。确认存在且描述准确。\n\n- [Campagna et al., \"Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability\"](https://arxiv.org/abs/2601.19856) (RA-L 2025): \n  化学品混合任务中通过 7 种行为指标（凝视、位移、速度同步等）用 Voting Classifier 达到 84% trust 分类准确率（AUC=0.90）。但样本极小（N=14），且为物理 HRI 场景，与 LLM 对话的 domain gap 很大。确认存在且描述准确。\n\n- [Raees & Papangelis, \"From Trust to Appropriate Reliance\"](https://arxiv.org/abs/2604.23896) (arXiv, April 2026): \n  测量理论 review，区分 trust 与 appropriate reliance 为不同构念，提出 Traditional/Appropriateness/Dominance 三种测量视角。支持用行为过程指标替代主观信任评级。确认存在且描述准确。\n\n- [PRISM: Lightweight Multivariate Time-Series Classification](https://arxiv.org/abs/2508.04503) (Neurocomputing 2026):\n  通过对称 FIR 滤波器实现多分辨率轻量 CNN，~40K 参数在 UCI-HAR 等基准上达到 97.3%。确认存在。Proposal 中已做合理 caveat——UCI-HAR 的 6 类物理活动分类与 overreliance 的噪声行为信号差异巨大。\n\n- 直接竞争者搜索：未发现任何已有系统实现 \"仅用行为信号、无传感器、闭环检测 + 干预 LLM overreliance\" 的组合。Liu et al. 和 Adjust for Trust 都明确指出这是 open gap。\n\n- 调研总结：该领域处于 \"行为信号已被刻画、干预策略已被验证、但二者未被连接\" 的阶段。Proposal 定位于填补这个明确的 gap，核心赌注在于 behavioral signals 单独能否支撑有用精度的 streaming 检测——现有证据正反参半（Adjust for Trust 失败 vs. HRI 领域正面结果），domain transfer 可行性未知。\n```\n\n---\n\n```\n【Trivial Alternative 检验】:\n\n最直接的 trivial alternative：**定时/随机触发 CFF（如每 2 分钟弹一次 metacognitive prompt）**。\n这完全绕过了检测模块——不需要 CNN、不需要 temporal grid、不需要 labeling pipeline。\nBuçinca et al. (CSCW 2021) 已证明 static CFF 确实能降低 overreliance。\n\nProposal 的增量价值声称是：行为触发的 adaptive 干预比 static CFF 更优，因为 (1) 减少 alert fatigue，(2) 将干预精准定位到高风险时刻。但这个增量的大小完全取决于检测准确率——而这正是 proposal 自身标记为 \"core empirical hypothesis\" 的未知数。\n\n第二个 trivial alternative：**用 Liu et al. 的 5 个行为模式直接写 rule-based 阈值检测器**，不需要训练 CNN。Proposal 在 weak supervision circularity ablation 中部分处理了这个问题（condition i: WS-only），但如果 rule-based 检测已经接近 CNN 性能，那么 CNN 的价值就很有限。\n\n结论：Trivial alternative 威胁真实存在。Proposal 对此有意识（包含 static CFF 作为 baseline、设计了 ablation），但核心 delta 取决于检测精度这个未知数。如果最终 CNN ≈ rule-based ≈ 65-70%，那么整个 ML pipeline 的增量价值有限。\n```\n\n---\n\n```\n【前提假设检验】:\n\n核心逻辑链：\n行为信号包含 overreliance 信息 → 30×28 temporal grid 能有效捕获这些信息 → 40K-param CNN 能从 ~30K windows 学到有用模式 → 实时检测精度足以支撑有意义的 adaptive 干预 → adaptive 干预优于 static CFF\n\n逐环检验：\n\n1. ❌ \"行为信号在 window 级别包含足够 overreliance 信息\"——未经验证。\n   Liu et al. 的发现是 session 级别的统计关联（高/低 overreliance 组的行为分布差异），而非 window 级别的可判别性。从 session-level 统计差异到 30-second window-level 实时分类是巨大的粒度跳跃。Adjust for Trust Appendix D 的 F1 ≤ 0.5 正是在更细粒度上的失败证据。\n\n2. ⚠️ \"Campagna (84%) 和 Kaneko (90%) 证明 behavioral trust prediction 可行\"——domain gap 问题严重。\n   Campagna 是物理 HRI（化学混合任务，N=14，使用凝视和空间位移），Kaneko 是无人机/驾驶模拟器中的 trust dynamics。这些场景中的行为信号（身体运动、凝视方向）与 LLM 对话中的鼠标/键盘操作在信息丰富度上有本质差异。将这些作为 \"positive evidence\" 有误导性。\n\n3. ⚠️ \"~30K training windows 足够训练 40K-param CNN\"——comparison to UCI-HAR 不恰当。\n   UCI-HAR 的 6 类物理活动（走路、坐下、站立等）具有明确的运动学特征和清晰的类别边界。Overreliance 的行为信号远比加速度计数据噪声更大、类别边界更模糊。Sample efficiency 不能跨任务类比。\n\n4. ❌ \"MIL 能有效解决 session-level → window-level 的 label 传播\"——假设较强。\n   MIL 在包级别标签到实例级别标签的转换中，依赖于 \"至少一个正例实例存在\" 的假设。但在 overreliance 场景中，一个被标记为 \"overreliant\" 的 session 可能只有少数 windows 真正表现出 overreliant 行为，其余大部分都是正常交互。正/负比例严重不平衡时 MIL 的 attention 学习质量存疑。\n\n总结：逻辑链的第 1 环（window-level 信息充分性）和第 2 环（domain transfer）是最薄弱的，且没有直接的实证支撑。这也是 proposal 自身将检测精度视为 \"core empirical hypothesis\" 的原因——proposal 对此有自我意识，但自我意识不等于问题被解决。\n```\n\n---\n\n```\n【3 维度打分】:\n\n1. Novelty: 【中】\n   \n   理由：该 proposal 填补了一个真实存在且被多篇论文明确指出的 gap——没有系统将 behavioral-only signals 连接到 real-time adaptive intervention for LLM overreliance。这个 gap identification 是准确的（调研确认无直接竞争者）。\n   \n   但剥离 surface differences 后，novelty 的实质是 \"systems integration\"：\n   - 行为信号词汇：直接来自 Liu et al. (CHI 2026)\n   - 干预策略：来自 Adjust for Trust (IUI 2026) 和 Buçinca et al. (CSCW 2021)\n   - CNN 架构：改编自 PRISM（Neurocomputing 2026）\n   - Labeling 方法：MIL + Snorkel weak supervision 均为成熟技术\n   - 闭环架构概念：Sensing What Surveys Miss (CHI 2026) 已经实现，只是不同 domain + 需要传感器\n   \n   最具独立 novelty 的部分是 hybrid labeling methodology（MIL + weak supervision + sparse probes + self-supervised），但这是将已有技术组合应用到新场景，非方法论创新。\n   \n   Weak supervision circularity analysis 是一个 methodological 亮点，显示了严谨性，但它是对 potential flaw 的防御性分析，非 positive novelty contribution。\n   \n   对标：\"Sensing What Surveys Miss\" (CHI 2026) 在概念上非常相似（sensing → real-time detection → adaptive intervention），只是 target construct 不同（cognitive load vs. overreliance）且需要 EDA。去掉 EDA 依赖、换成 overreliance 目标，这是 incremental 的 novelty。\n\n2. Significance: 【中偏强】\n   \n   理由：\n   - 问题本身无可争议地重要：LLM overreliance 是 CHI/IUI 社区 2024-2026 年最热的主题之一。Ibrahim et al. (2025) 的 consolidation paper 和 Raees & Papangelis (2026) 的 measurement 框架都证实了社区的关注度。\n   - 实际影响力：一个 sensor-free、browser-based 的闭环系统如果有效，其部署门槛远低于 EDA-based 方案（Sensing What Surveys Miss），有真正的实用潜力。\n   - 但 significance 被两个因素限制：\n     (a) 核心假设未验证——如果检测精度只有 65-70%，系统的实际价值存疑。Proposal 用 dual-outcome framing 对冲了这一风险（\"即使检测失败，characterization 本身也有价值\"），但这实际上是在降低 significance claim 的力度：一个 \"告诉你什么不行\" 的 characterization study 的 impact 远低于一个 \"working system\"。\n     (b) 如果核心发现是 positive（检测有效），审稿人大概率会说 \"interesting, but expected given the trajectory of Campagna + Kaneko + richer modeling\"——不太会说 \"surprising\"。\n\n3. Related Work: 【强】\n   \n   理由：\n   - 调研确认 proposal 中引用的所有关键论文均真实存在且描述准确（Liu et al., Adjust for Trust, Sensing What Surveys Miss, Campagna et al., Raees & Papangelis, PRISM）。\n   - 差异化定位非常清晰：对每个 prior work 都明确指出了与本工作的区别（Liu: 无 real-time 系统；Adjust for Trust: 需要 self-report；Sensing What Surveys Miss: 需要 EDA + 不同 target construct；Li et al.: structured task only）。\n   - 对 negative evidence 的处理诚实（Dechant 2023, Adjust for Trust Appendix D），没有选择性引用。\n   - 唯一微小不足：对 Campagna et al. (N=14) 和 Kaneko & Yamada 作为 \"positive evidence\" 的引用可能过度乐观——这两项工作的 domain gap 很大，且样本量小，作为 feasibility 论据的说服力有限。但 proposal 确实加了 caveat（\"proof-of-principle rather than direct benchmarks\"），基本诚实。\n```\n\n---\n\n```\n【概率估计】: [22% - 35%] 中位 28%\n\n（注：此概率基于 CHI/IUI 等 HCI 顶会评估。若投 CoRL 2026，概率 ≈ 0-3%，因完全不匹配会议主题。）\n\n【估计理由】:\n\n向上拉的因素：\n- 问题高度时效（LLM overreliance 是 2025-2026 HCI 社区热点）\n- Gap identification 准确且被多篇论文背书（Liu et al. 和 Adjust for Trust 都明确留了这个 future work）\n- Related work 覆盖全面且差异化定位清晰\n- Proposal 形式完善度极高（dual-outcome、circularity ablation、ecological validity 讨论等显示了高度的方法论严谨性）\n- Sensor-free browser-based 方案如果有效，有真正的实用价值\n\n限制上界的因素：\n- **Novelty 是主要瓶颈**。核心贡献是 systems integration，不是方法论或概念创新。每个组件（行为信号、干预策略、CNN 架构、labeling 方法）都有明确来源。最相似的 \"Sensing What Surveys Miss\" (CHI 2026) 已经证明了闭环 sensing→intervention 的可行性，只是在不同 domain。\n- 核心假设（window-level behavioral signals → overreliance detection）缺乏直接支撑。从 Liu et al. 的 session-level 关联到 30-sec window-level 分类是未经验证的跳跃。\n- 如果核心发现是 positive，审稿人更可能说 \"nice engineering, expected result\" 而非 \"surprising\"。\n- Dual-outcome framing 是合理的风险管理，但也暴露了作者对核心 claim 的信心不足——顶会审稿人通常偏好有明确 strong claim 的论文。\n\n概率被锚定在 25-35% 区间（\"idea 有实质内核但核心发现不够 surprising\"），中位 28% 反映了 novelty 偏 integration 且核心假设未验证的 discount。\n\n【主要风险】:\n1. **Novelty 不足风险**: 审稿人可能认为这是 Liu et al. + Adjust for Trust 的 \"obvious next step\"——两篇论文的 future work section 都明确指向了这个方向。CHI 审稿人对 \"filling an explicitly stated gap\" 的态度分化很大：有人认为这是 well-motivated，有人认为缺乏 intellectual surprise。\n2. **\"If positive, I would have guessed this\" 风险**: 如果 CNN 确实比 heuristic 好，这符合 \"更复杂的模型 > 简单 heuristic\" 的一般直觉。如果 CNN 不比 heuristic 好，dual-outcome framing 可以保底但 contribution 的 impact 被显著削弱。无论哪种结果，都缺少一个真正 surprising 的 finding。\n```\n\nSources:\n- [Liu et al., Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)\n- [Srinivasan & Thomason, Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Liu et al., Sensing What Surveys Miss (CHI 2026)](https://arxiv.org/abs/2602.00880)\n- [Campagna et al., Estimating Trust in Human-Robot Collaboration (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Raees & Papangelis, From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)\n- [PRISM: Lightweight Multivariate Time-Series Classification (2025)](https://arxiv.org/abs/2508.04503)\n- [Buçinca et al., Cognitive Forcing Functions (CSCW 2021)](https://dl.acm.org/doi/10.1145/3449287)\n- [Ghosh et al., Cognitive Forcing Functions for AI-Assisted Writing (2026)](https://arxiv.org/abs/2601.18033)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct the evaluation. Let me compile the analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【重要前置说明 — 致命性 venue 不匹配】:\n本 proposal 的目标是构建基于浏览器行为信号的 LLM 过度依赖检测与自适应干预系统，\n属于纯 HCI / Human-AI Interaction 领域。CoRL 2026（Conference on Robot Learning，\n2026年11月9-12日，Austin TX）的 scope 明确限定在\"robot learning\"——强化学习控制\n物理机器人、模仿学习、sim-to-real、机器人感知、操作与运动规划等。本 proposal 不涉及\n任何机器人组件、物理具身、或机器人学习问题。投稿 CoRL 大概率被 desk reject 或在\nscope 审查阶段直接淘汰。proposal 自身列出的目标 venue（CHI 2027、IUI 2027、CSCW 2027、\nIMWUT、AAAI 2027）才是合理选择。\n\n以下评估基于 idea 本身的质量（venue-agnostic），但概率估计会反映 CoRL 的 venue fit。\n\n【领域调研】:\n- [Liu et al., arXiv 2602.11567] (CHI 2026): 77名参与者 × 3个任务，通过自编码器聚类\n  识别出5种与LLM过度依赖相关的行为模式（频繁复制粘贴、跳过初始理解、反复参考LLM等），\n  但明确将实时检测和干预留作future work。本proposal直接建立在此数据集和信号词汇之上。\n  \n- [Srinivasan & Thomason, arXiv 2502.13321] (IUI 2026): \"Adjust for Trust\"系统，\n  通过自报告信任评级（每次决策后11点量表）自适应调整解释策略，实现最高38%不当依赖降低。\n  Appendix D记录了行为信任估计的失败尝试（F1 ≤ 0.5）。本proposal的核心动机之一。\n  \n- [Ailin Liu et al., arXiv 2602.00880] (CHI 2026): \"Sensing What Surveys Miss\"，\n  最接近的架构类比——使用鼠标动力学+EDA构建闭环系统，但：(a)目标是认知负荷而非过度依赖，\n  (b)需要生理传感器，(c)线性回归分类器仅~61%准确率。N=32。\n  \n- [Campagna et al., arXiv 2601.19856] (RA-L 2025): 人-机器人协作中通过行为指标\n  （注视方向、空间位移等）实现84%信任分类准确率。但domain是物理HRI（N=14），\n  与对话式LLM交互存在显著领域差距。\n  \n- [Raees & Papangelis, arXiv 2604.23896] (2026): 测量理论框架，论证信任与适当依赖是\n  概念上不同的构念，提倡行为过程指标——为本proposal的方法论选择提供了理论基础。\n  \n- [PRISM, arXiv 2508.04503] (Neurocomputing 2026): 轻量级多分辨率时序分类架构，\n  ~40K参数在UCI-HAR上达97.3%。proposal借鉴其架构用于浏览器端推理。\n  \n- [Buçinca et al.] (CSCW 2021) + [Ghosh et al., arXiv 2601.18033] (2026): \n  认知强迫函数研究线，表明CFFs可降低过度依赖但可能增加挫折感；Assumption-style CFF最有效。\n  \n- [Chatsparent, arXiv 2601.11526]: 相关但不同——检测LLM对话中的认知疲劳而非过度依赖。\n  \n- 调研总结: 该领域在2025-2026年经历了快速发展。行为信号表征（Liu et al.）、\n  自适应干预（Adjust for Trust）、多模态闭环（Sensing What Surveys Miss）分别推进了\n  各自子问题，但确实没有工作仅用非侵入性浏览器行为信号在对话式LLM场景中实现\n  闭环检测+干预。Proposal准确识别了这个gap。然而，这个gap的存在部分原因是\n  先前尝试失败了（F1 ≤ 0.5），而非被忽视——这让\"能否填补\"成为一个有风险的经验性问题。\n\n【Trivial Alternative 检验】:\n存在多个更简单的替代方案需要考虑：\n\n1. **固定间隔CFF（已作为baseline之一）**: 如果静态认知强迫函数（每次都触发）的效果与\n   行为触发的自适应干预差距不大，那么整个检测管道的增量价值将大大缩水。Buçinca et al. (2021)\n   已经证明always-on CFF有效降低过度依赖，区别只在于用户体验（alert fatigue）。\n   如果自适应干预的主要优势仅是\"减少打扰频率\"而非\"更准确的时机\"，这个contribution就\n   更像一个工程优化而非科学发现。\n\n2. **简单启发式阈值触发**: 不需要CNN，直接用\"复制粘贴后10秒内无编辑\"等规则触发干预。\n   Proposal承认Adjust for Trust的Appendix D用简单启发式只达F1 ≤ 0.5，但那是在\n   预测信任评级——而预测\"何时触发干预\"的阈值可能比精确分类更容易。如果一个简单的\n   规则引擎在干预效果上接近CNN方案，CNN的增量价值就有限。\n\n3. **随机定时干预**: 如果检测准确率只有65-70%（proposal自己承认的现实场景），\n   那么与随机但频率匹配的干预之间的效果差异可能不显著。\n\n增量价值所在: 如果CNN确实能达到≥80%准确率，那么精准时机+降低打扰的组合是有实质价值的。\n但这正是核心经验性假设，且先验证据并不乐观。\n\n【前提假设检验】:\n核心claim的逻辑链条中存在以下未验证假设：\n\n1. **30秒窗口粒度假设（关键薄弱环节）**: 过度依赖是一种可在30秒滑动窗口内被检测的\n   行为状态。Liu et al.的五种模式是通过对整个任务session的post-hoc分析发现的，\n   这些模式是否在30秒粒度上有足够区分度是完全未知的。过度依赖可能是一个\n   session-level的认知倾向，而非moment-to-moment可切换的状态。\n\n2. **训练数据独立性假设**: 从231个session用5秒步长的滑动窗口生成~26K-40K样本，\n   但相邻窗口有83%重叠（25/30秒共享），这些样本高度相关。有效独立样本数远小于\n   26K-40K，可能导致严重的过拟合和虚高的交叉验证结果。Proposal提到的\n   \"sample-to-parameter ratio 0.65-1.0:1\"严重高估了有效比率。\n\n3. **行为信号→过度依赖的因果方向假设**: Liu et al.发现的是行为模式与过度依赖\n   outcome的相关性，不是因果关系。某些行为模式可能是task difficulty的混杂效应，\n   而非过度依赖的因果指标。在streaming预测中，这个问题更为突出——你在看到outcome之前\n   就需要判断\"过度依赖\"，但这个标签本身是outcome-defined的。\n\n4. **领域迁移假设**: 支持\"行为信号可以预测信任/依赖\"的正面证据（Campagna 84%，\n   Kaneko 90%）来自完全不同的领域（物理HRI、无人机/驾驶模拟器），使用的是\n   物理行为指标（注视、空间位移、速度同步等）。从这些结果推断到\"鼠标/键盘信号\n   可以预测对话式LLM过度依赖\"需要一个很大的领域迁移跳跃，proposal对此诚实\n   但跳跃本身仍是未验证的。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Proposal准确识别了一个真实存在的gap：无人仅用非侵入性浏览器行为信号在对话式LLM\n   场景中构建闭环检测+干预系统。这个gap在Liu et al. (CHI 2026)、Adjust for Trust \n   (IUI 2026)、Sensing What Surveys Miss (CHI 2026)三篇同期工作之间确实存在。\n   \n   然而，novelty的本质是**系统集成**而非**方法创新**：将Paper A的信号词汇 + Paper B的\n   干预策略 + Paper C的架构思路组装为一个完整系统。各个组件——temporal grid特征工程、\n   multi-resolution 1D-CNN、MIL+弱监督混合标注、分层干预引擎——均有直接的现有先例。\n   混合标注策略是最有方法论novelty的部分（MIL + weak supervision + sparse probes + \n   self-supervised的组合），但其中每个子技术本身都是成熟的（Snorkel弱监督、TimeMIL、\n   自监督正则化），组合虽新但并非surprising。\n   \n   核心问题：如果CNN检测达到80%+，审稿人的反应更可能是\"合理，行为信号确实应该有信息量\"\n   而非\"surprising，没想到这能work\"。如果只达65-70%，则与prior failures一致。\n   两种结果都不太可能被视为deeply surprising。\n\n2. **Significance: 中偏强** — \n   研究问题本身（如何非侵入式地检测和缓解LLM过度依赖）是重要且及时的。LLM使用量爆发式\n   增长，过度依赖是一个被广泛关注的问题（Ibrahim et al. 2025的综述明确呼吁\n   process-oriented mitigation）。一个可部署的浏览器扩展方案如果work，实际影响大。\n   \n   但significance受限于：(a) 生态效度——受控注入错误信息 vs. 自然LLM幻觉的差距，\n   proposal自身引用Ren et al.承认了这一点；(b) 如果核心检测性能不够好，\n   \"what behavioral signals can and cannot predict\"的characterization贡献虽有价值，\n   但更适合作为workshop paper而非主会contribution的核心。\n   \n   对HCI领域（CHI/IUI）的significance是实质性的；对CoRL完全不相关。\n\n3. **Related Work: 强** — \n   这是proposal最突出的优点。对相关工作的覆盖非常全面且精确：\n   - 直接前序工作（Liu et al., Adjust for Trust, Sensing What Surveys Miss, \n     From Text to Trust）的描述准确，差异化定位清晰\n   - 正面和负面证据都有引用（Campagna/Kaneko的正面 vs. Dechant/Adjust for Trust \n     Appendix D的负面），没有cherry-pick\n   - 测量理论基础（Raees & Papangelis）的引入增强了概念严谨性\n   - 所有查证的关键引用（arXiv ID、venue、发现）均真实准确\n   - 与最近的Chatsparent (2025)等工作没有overlap\n   \n   唯一的轻微gap：没有讨论attention-based或transformer方法在类似规模行为数据上的\n   表现，只与MiniRocket和BiLSTM做对比，但这属于实验设计层面的问题，不影响related work评分。\n\n【概率估计】: \n- 如投CoRL 2026: [1% - 5%] 中位 2%\n- 如投CHI/IUI 2027（proposal实际目标venue）: [25% - 40%] 中位 32%\n\n【估计理由】: \n**CoRL概率（2%）**: 这是一篇纯HCI论文，与CoRL的scope（robot learning）完全不匹配。\n无机器人组件、无物理具身、无学习控制物理系统。大概率在scope审查阶段被拒，\n即使进入审稿也会因\"out of scope\"获得强拒。这不是idea质量问题，是venue选择错误。\n\n**CHI/IUI参考概率（32%）**: idea有真实gap、方向正确、related work扎实。\nNovelty为\"中\"（系统集成型novelty，非surprising发现）限制了上界——即使实验完美执行，\n核心发现大概率落在\"makes sense\"而非\"surprising\"区间。前提假设中30秒窗口粒度和\n训练数据独立性问题增加了核心claim不成立的风险。混合标注方法论是加分项。\nDual-outcome设计提供了一定的下限保障。对CHI/IUI，这个idea处于\"有实质内核但不\noutstanding\"的区间。\n\n【主要风险】:\n1. **（CoRL层面）致命性venue不匹配**: 本proposal与CoRL的scope完全不符。\n   这不是可以通过reframing修复的问题——论文的entire contribution都在HCI领域，\n   没有任何组件可以legitimately声称是robot learning contribution。\n   \n2. **（idea层面）核心经验性假设薄弱**: 30秒窗口内行为信号能否区分过度依赖状态，\n   是整个系统的基础假设，但先验证据指向负面（F1 ≤ 0.5、~61%），\n   正面证据来自完全不同的领域（物理HRI）。如果这个假设不成立，\n   系统的core contribution（闭环检测+干预）就无法兑现。\n   虽然proposal的dual-outcome设计提供了保底，但\"characterizing what doesn't work\"\n   作为CHI主会论文的核心卖点说服力有限。\n```\n\n---\n\n**总结**: 这个proposal作为HCI研究是一份质量中上的工作——gap真实、related work扎实、方法论设计审慎。但**投稿CoRL 2026是根本性的venue选择错误**。CoRL聚焦于robot learning（强化学习控制物理机器人、模仿学习、sim-to-real等），本proposal不含任何机器人学习组件。建议作者回到其原始目标venue列表（CHI 2027 / IUI 2027），在那些venue中这个idea有合理的竞争力（估计~32%中稿概率）。\n\nSources:\n- [Liu et al. - Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)\n- [Srinivasan & Thomason - Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Liu et al. - Sensing What Surveys Miss (CHI 2026)](https://arxiv.org/abs/2602.00880)\n- [Campagna et al. - Estimating Trust in HRC (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Raees & Papangelis - From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)\n- [PRISM - Multi-Resolution Time Series Classification (2025)](https://arxiv.org/abs/2508.04503)\n- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Buçinca et al. - Cognitive Forcing Functions (CSCW 2021)](https://dl.acm.org/doi/abs/10.1145/3449287)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Closing the Loop: From Behavioral Overreliance Detection to Adaptive Intervention in LLM Conversations\n\n## Description\nWe propose OverrelianceGuard, the first closed-loop system that bridges unobtrusively collected behavioral interaction signals to real-time adaptive interventions in free-form conversational LLM interactions—without requiring self-report interruptions or physiological sensors. A browser extension captures non-invasive interaction events in 30-second sliding windows and transforms them into a temporal grid representation: each window is discretized into 30 one-second bins, with 28 aggregated features per bin capturing action type distribution (over 12 categories), mouse dynamics (distance, velocity), scroll behavior (distance, direction), keypress statistics, copy-paste behavior (including post-paste edit indicators), idle duration, dwell context relative to LLM responses, and page focus. This (30 × 28) temporal grid—derived from but explicitly distinct from Liu et al.'s (CHI 2026) per-event 37-dimensional encoding (15-dim action type one-hot + 1-dim timestamp + 2-dim page type + 19-dim type-specific attributes)—feeds a lightweight multi-resolution 1D-CNN (~40K parameters, <5ms browser inference via ONNX Runtime Web) with three parallel temporal branches capturing short-burst (2s), medium-term (10s), and full-window (30s) behavioral dynamics. We cite PRISM's 97.3% accuracy on UCI-HAR as evidence of architectural efficiency at this parameter scale, not as a performance projection—UCI-HAR involves 6-axis accelerometer data with well-separated activity classes, whereas overreliance classification operates on noisier interaction features with subtler boundaries. The architecture choice is motivated by converging evidence that simple models on behavioral signals are insufficient—Adjust for Trust's Appendix D found F1 ≤ 0.5 with surface-level heuristics, 'Sensing What Surveys Miss' (CHI 2026) achieves only ~61% with linear regression on mouse+EDA—while richer models on multi-dimensional behavioral features show substantially better results: Campagna et al. (RA-L 2025) achieve 84% trust classification (AUC=0.90) from behavioral indicators in HRI, and Kaneko & Yamada (2025) reach 90% in cooperative tasks. A methodological contribution is the hybrid labeling strategy addressing temporal misalignment between Liu et al.'s outcome-based labels and streaming prediction: outcome propagation via Multiple Instance Learning, weak supervision from programmatic heuristics encoding the five identified behavioral patterns, sparse event-triggered metacognitive probes (2–3 per task vs. Adjust for Trust's 30 per-decision self-reports), and self-supervised next-action prediction. Critically, we address the weak supervision circularity risk—where labeling functions encode behavioral patterns from the same feature space the CNN processes—through a four-condition ablation: (i) weak-supervision-only, (ii) MIL+probes-only (circularity-free, as labels derive from task outcomes and self-report), (iii) MIL+probes+self-supervised, and (iv) full multi-signal training. Comparing conditions (iv) vs. (ii) isolates whether the weak supervision provides complementary signal or merely teaches the CNN its own hand-coded rules, with Integrated Gradients feature attribution analysis revealing whether the model discovers temporal patterns beyond those encoded in labeling functions. We frame streaming behavioral overreliance detection as the core hypothesis being tested: if classifier accuracy proves disappointing (e.g., 65–70%), the within-subjects intervention comparison, the labeling methodology, and the characterization of what behavioral signals can and cannot predict all constitute independently publishable contributions. We analyze training data sufficiency: Liu et al.'s 77-participant dataset yields ~26K–40K behavioral windows with our proposed windowing, supplemented by augmentation and a phased training strategy. When overreliance risk exceeds personalized thresholds, the system selects from tiered interventions: metacognitive prompts (Assumption-style CFFs), counter-explanations (per Adjust for Trust), and comprehension checkpoints. Following Raees & Papangelis's (2026) measurement framework distinguishing trust from appropriate reliance, we assess overreliance via both Traditional (acceptance rates) and Appropriateness-view (RAIR/RSR) metrics. A within-subjects study (N≈120) across four LLM-assisted tasks compares four conditions: no intervention, static cognitive forcing, self-report-adaptive (replicating Adjust for Trust), and behaviorally-triggered adaptive (OverrelianceGuard). This work fills the gap between behavioral characterization (Liu et al., CHI 2026), trust-adaptive intervention via self-report (Adjust for Trust, IUI 2026), adaptive explanation selection in structured tasks (Li et al., CHI 2025), and sensor-dependent adaptive support (Sensing What Surveys Miss, CHI 2026)—contributing (1) the first streaming behavioral overreliance classifier for conversational LLM settings with a principled hybrid labeling methodology and explicit circularity analysis, (2) a deployable browser-based closed-loop intervention system requiring neither self-report interruptions nor physiological sensors, (3) head-to-head empirical evidence comparing self-report-based vs. behavior-based adaptive intervention, and (4) a rigorous characterization of what behavioral signals can and cannot predict about overreliance, advancing the field regardless of detection accuracy.\n\n## Core Problem\nCan unobtrusively collected behavioral interaction signals (copy-paste patterns, scroll depth, verification dwell time, tab-switch frequency) drive a real-time streaming classifier that triggers adaptive interventions to reduce overreliance on LLM outputs—without requiring self-report interruptions or invasive physiological sensors?\n\n## Opportunity\nLiu et al. (CHI 2026, arXiv 2602.11567) identify five behavioral patterns distinguishing high- vs. low-overreliance users in LLM interactions but explicitly leave real-time detection and intervention as future work. Srinivasan & Thomason's 'Adjust for Trust' system (IUI 2026, arXiv 2502.13321) achieves up to 38% reduction in inappropriate reliance through trust-adaptive interventions, but requires self-reported trust ratings on an 11-point scale after every decision—an intrusive approach whose inadequacy the authors themselves confirm in Appendix D, where their attempts at behavioral trust estimation yielded only 0.25–0.51 correlation and F1 ≤ 0.5 using surface-level interaction heuristics. Li et al.'s 'From Text to Trust' (CHI 2025, arXiv 2502.11919) adaptively selects explanations via POMDP-based hidden state estimation, but operates only in structured tabular decision tasks using coarse binary (agree/disagree) feedback—not rich behavioral signals in free-form LLM conversations. Ailin Liu et al.'s 'Sensing What Surveys Miss' (CHI 2026, arXiv 2602.00880) build the closest architectural parallel—a closed-loop system using mouse dynamics and electrodermal activity (EDA) to trigger adaptive LLM-based interventions—but target cognitive load during online surveys (not overreliance in LLM conversations), require physiological sensors (EDA wristbands), and achieve only ~61% detection accuracy with simple linear regression classifiers and max-fusion of two unimodal models; crucially, the paper provides no ablation separating mouse-only from EDA contributions, leaving open the question of whether interaction signals alone—processed with richer temporal modeling than linear regression—can achieve adequate detection without physiological sensing. The evidence for behavioral trust prediction is mixed but increasingly positive: while Dechant et al. (2023) find mouse trajectories alone insufficient and Adjust for Trust's Appendix D reports F1 ≤ 0.5 with surface-level heuristics, Campagna et al. (RA-L 2025, arXiv 2601.19856) achieve 84% accuracy classifying trust from behavioral indicators in human-robot collaboration using ensemble classifiers, and Kaneko & Yamada (IEEE Access, 2025; arXiv 2407.01752) demonstrate 90% accuracy predicting trust dynamics via dynamic structural equation modeling in physical cooperative tasks—both suggesting that behavioral features CAN support useful trust prediction with appropriate modeling depth, even if the domain gap to conversational LLM settings makes these figures proof-of-principle rather than direct benchmarks. Raees & Papangelis ('From Trust to Appropriate Reliance,' arXiv 2604.23896, April 2026) further argue that trust measurements are conceptually distinct from appropriate reliance—the construct we actually target—and advocate for behavioral process metrics over subjective trust ratings, providing measurement-theoretic grounding for our approach. The bridge remains unbuilt: no system uses fine-grained, continuously captured interaction signals alone to detect overreliance and trigger personalized interventions in conversational LLM settings. This is now technically feasible because (1) Liu et al.'s behavioral characterization provides the validated signal vocabulary via per-event interaction encodings, (2) lightweight time series classifiers like PRISM achieve high efficiency with only ~40K parameters and sub-millisecond inference, enabling browser-embedded real-time classification without physiological hardware, and (3) the converging positive evidence from Campagna et al. and Kaneko & Yamada establishes that behavioral trust prediction is achievable with appropriate modeling depth—though whether this generalizes to conversational LLM interactions remains the core empirical hypothesis we test.\n\n## Landscape\nLiu et al. (CHI 2026) provide the most comprehensive behavioral characterization of LLM overreliance, identifying five patterns—frequent copy-paste without editing, skipped initial task comprehension, rapid LLM-task alternation, coarse block-pasting vs. fine-grained editing, and hesitation-then-acceptance—via autoencoder clustering of per-event interaction encodings (each event represented as a 37-dimensional vector: 15-dim action type one-hot + 1-dim normalized timestamp + 2-dim page type + 19-dim type-specific attributes) from 77 participants across three tasks with injected misinformation. The 'Adjust for Trust' system (Srinivasan & Thomason, IUI 2026) demonstrates that adapting explanations based on trust level (supporting explanations when trust is low, counter-explanations when high, with enforced reading delays) yields up to 38% reduction in inappropriate reliance and 20% accuracy improvement; however, it relies on self-reported trust on an 11-point scale after every one of 30 decisions per session. Critically, Appendix D documents the authors' failed attempt at replacing self-report with behavioral estimation: simple heuristics (AIAcc5, CapabilityDiff, SmoothOutcomes, SmoothConfs) achieved only 0.25–0.51 correlation and F1 ≤ 0.5, concluding that 'surface-level interaction features' are inadequate for trust modeling. Li et al. ('From Text to Trust,' CHI 2025) use a POMDP framework to adaptively select LLM-generated analyses based on inferred user hidden states, significantly improving accuracy on tabular classification tasks—but their interaction paradigm is structured (sequential agree/disagree on feature-level explanations), their state estimation uses only binary response feedback, and they neither capture behavioral signals nor address free-form conversational LLM use. Ailin Liu et al.'s 'Sensing What Surveys Miss' (CHI 2026, arXiv 2602.00880) is the most architecturally analogous prior work: it builds a closed-loop system where mouse dynamics (vertical direction changes, hover time, hover count) and electrodermal activity (tonic EDA level, EDA peaks) feed personalized linear regression classifiers with rule-based threshold adaptation, triggering LLM-generated clarifications during online surveys. In a within-subjects study (N=32), their aligned-adaptive timing improved survey response accuracy by 21% and reduced false negatives from 50.9% to 22.9%. However, three key differences separate their work from ours: (a) they target cognitive load in knowledge-based survey items, not overreliance on LLM outputs in conversational interaction—fundamentally different constructs requiring different signal vocabularies; (b) they require physiological sensors (EDA wristbands), limiting scalability to any-browser deployment; and (c) their simple linear regression classifiers with max-fusion of two unimodal models achieve only ~61% detection accuracy, and they provide no ablation isolating the contribution of mouse dynamics alone vs. EDA alone—leaving open whether their mouse features would function without the physiological channel. Their finding that even combined mouse+EDA with simple models reaches only 61% accuracy actually reinforces our hypothesis that richer temporal signal processing (multi-resolution CNNs operating on the full behavioral feature space) is needed to compensate for the absence of physiological signals. The evidence landscape for behavioral trust/reliance prediction includes both negative and positive results. On the negative side: Dechant et al. (arXiv 2310.16632, 2023) find that mouse trajectory features alone 'might not explain sufficiently the variance to be used on their own'; Adjust for Trust's Appendix D shows F1 ≤ 0.5 with heuristic behavioral features. On the positive side: Campagna et al. (RA-L 2025, arXiv 2601.19856) achieve 84% trust classification accuracy (Voting Classifier, AUC=0.90, F1=0.84) from seven behavioral indicators—gaze direction, spatial displacement, speed synchronization, reaction time, predictability, and legibility—in a human-robot chemical mixing task (N=14), demonstrating that ensemble classifiers on multi-dimensional behavioral features substantially outperform single-signal approaches, albeit in a physical HRI domain with a small sample; Kaneko & Yamada (IEEE Access, 2025) achieve 90% accuracy predicting over/under-trust using dynamic structural equation modeling on interaction data in drone and driving simulators; and Gurney et al. (Persuasive Technologies, 2023; arXiv 2302.01854) show that behavioral predictors outperform self-report psychometric inventories for predicting AI compliance. This pattern—negative results with simple models on narrow feature sets, positive results with richer models on multi-dimensional behavioral features—is central to our technical hypothesis. Raees & Papangelis ('From Trust to Appropriate Reliance,' arXiv 2604.23896, April 2026) provide important measurement-theoretic context, arguing that trust and appropriate reliance are conceptually distinct constructs: trust reflects subjective perception while reliance concerns observable behavioral decisions. They identify three measurement views (Traditional: over/under-reliance rates; Appropriateness: RAIR/RSR; Dominance: AI influence direction) and recommend behavioral process metrics over subjective ratings—directly supporting our approach of measuring reliance behavior rather than trust attitudes. Sun et al. ('Eyes Can't Always Tell,' arXiv 2604.01741, 2026) demonstrate that eye-tracking-to-cognitive-state mappings shift across AI conditions, arguing for multi-signal, context-dependent approaches. Cognitive forcing functions have been studied extensively: Buçinca et al. (CSCW 2021) showed CFFs reduce overreliance but increase frustration; Ghosh et al. (arXiv 2601.18033, 2026) found Assumption-style CFFs most effective at reducing overreliance without increasing cognitive load. Ibrahim et al. (arXiv 2509.08010, 2025) consolidate measurement gaps and call for process-oriented mitigation. The 'From Calibration to Collaboration' position paper (arXiv 2506.07461, June 2025) argues that current UQ methods are misaligned with real user needs. Key limitation across all works: no system closes the loop from non-invasive behavioral detection to adaptive intervention in free-form conversational LLM interactions. Liu et al. characterize signals but build no real-time system; Adjust for Trust intervenes adaptively but requires intrusive every-decision self-report that their own behavioral estimation attempt failed to replace; From Text to Trust adapts but only in structured tasks with coarse feedback; Sensing What Surveys Miss closes the loop but requires physiological sensors and targets cognitive load in surveys with simple classifiers achieving only 61% accuracy; Campagna et al. predict trust behaviorally in HRI but build no intervention system for conversational AI; and Kaneko & Yamada predict trust in physical cooperative tasks but do not address conversational LLM settings.\n\n## Approach\nBuild OverrelianceGuard, a browser-extension-based closed-loop system with three components:\n\n(1) INSTRUMENTATION LAYER: A JavaScript layer that unobtrusively captures interaction events in 30-second sliding windows (5-second stride). FEATURE REPRESENTATION CLARIFICATION: Liu et al.'s original 37-dimensional encoding is a per-event representation—each discrete interaction event (click, scroll, keypress, etc.) is encoded as a 37-dimensional vector comprising a 15-dim action type one-hot, 1-dim normalized timestamp, 2-dim page type, and 19-dim type-specific attributes (e.g., mouse movement distance and duration, scroll distance and direction, keypress count). Their transformer autoencoder operates on variable-length sequences of these event vectors per segment. Our CNN requires fixed-size input per window, so we transform Liu et al.'s event sequences into a temporal grid representation: each 30-second window is discretized into T=30 one-second bins, and for each bin we compute K=28 aggregated features from all events occurring within that bin. Specifically, the 28 per-bin features are: (a) action type distribution—proportions over 12 action categories (mouse movement, click, scroll, keypress, copy, paste, highlight, delete, idle, tab switch, prompt input, element switch; 12 features); (b) mouse dynamics—total movement distance and mean velocity (2); (c) scroll dynamics—total distance and direction ratio (up/down; 2); (d) keypress statistics—count and mean inter-key interval (2); (e) copy-paste behavior—copy count, paste count, and post-paste edit indicator (3); (f) idle time—total idle duration within the bin (1); (g) dwell context—time since last LLM response (1); (h) page context—fraction of time on LLM page vs. task page (1); (i) text interaction—highlight text length and delete count (2). This yields a (30 × 28) input tensor per window, where the temporal dimension (30 timesteps) captures within-window behavioral dynamics that the multi-resolution CNN branches process at different scales. Features are z-score normalized per-user via an initial 5-minute calibration phase to account for individual baseline interaction styles.\n\n(2) STREAMING OVERRELIANCE RISK CLASSIFIER: A multi-resolution 1D-CNN inspired by the PRISM architecture (~40K parameters). Three parallel convolutional branches with symmetric FIR filters at different temporal resolutions—2s (kernel size 2, capturing short-burst behaviors like rapid copy-paste), 10s (kernel size 10, capturing medium-term patterns like comprehension scanning), and 30s (kernel size 30, capturing full-window dynamics like engagement trajectory)—operate on the (30 × 28) temporal grid input, feed into per-branch global average pooling, then concatenate into a 2-layer MLP classification head (128→2) outputting an overreliance risk score ∈ [0,1]. This architecture is chosen because: (a) the (30 × 28) input is a moderately-sized temporal grid (not high-dimensional sensor data where ViT/transformers excel), (b) PRISM achieves 97.3% on UCI-HAR with ~40K parameters—we cite this as evidence of architectural efficiency at this parameter scale and sub-millisecond inference capability, not as a performance projection for our task, since UCI-HAR uses 6-axis accelerometer/gyroscope data with 6 well-separated physical activity classes, whereas overreliance classification operates on noisier mouse/keyboard interaction features with subtler class boundaries; (c) 1D-CNNs run in <5ms via ONNX Runtime Web on commodity CPUs; and (d) the Adjust for Trust Appendix D failure with surface-level heuristics and Sensing What Surveys Miss's ~61% accuracy with linear regression on mouse+EDA both suggest that improvement comes from richer temporal feature processing (multi-resolution convolutions capturing dynamics at multiple scales), not larger models or physiological sensors—while Campagna et al.'s 84% accuracy with ensemble classifiers on multi-dimensional behavioral features in HRI confirms that richer modeling on behavioral features can substantially exceed simple-model baselines. We compare against MiniRocket (fixed kernels + linear head, near-zero learnable parameters) and BiLSTM (128 hidden units, ~200K parameters) baselines to isolate the contribution of the multi-resolution architecture.\n\nTRAINING DATA SUFFICIENCY ANALYSIS: Liu et al.'s dataset comprises 77 participants × 3 tasks = 231 sessions. With our proposed 30-second sliding windows at 5-second stride, assuming average task durations of 10–15 minutes (consistent with their protocol), each session yields ~115–175 windows, producing an estimated 26K–40K behavioral windows total. For a 40K-parameter model, this yields a sample-to-parameter ratio of 0.65–1.0:1, which is tight but viable: for comparison, PRISM achieves 97.3% on UCI-HAR with only 7,352 training samples and ~40K parameters (ratio ~0.18:1). Nevertheless, we address overfitting risks through five mitigation strategies: (a) standard time series data augmentation—Gaussian jittering (σ=0.05), window slicing (90% crops), and time warping—which have been shown to substantially improve 1D-CNN accuracy on small behavioral datasets; (b) model regularization via dropout (p=0.3), L2 weight decay (λ=1e-4), and early stopping on a held-out validation set; (c) attention entropy maximization in the MIL pooling layer to prevent attention collapse onto few instances; (d) the weak supervision labeling functions themselves provide soft probabilistic labels that act as implicit label smoothing, reducing overfitting to noisy hard labels; and (e) a phased data strategy leveraging both datasets—train and validate on Liu et al.'s 77-participant data, then fine-tune on a pilot cohort (first ~20 participants of the 120-participant study) and evaluate on the remaining ~100, ensuring the final evaluation is on held-out participants unseen during any training phase. We will report learning curves (accuracy vs. training set fraction) to empirically demonstrate whether ~30K windows are sufficient or whether the model is still data-hungry, and will release the trained model weights and augmentation pipeline for reproducibility.\n\nGROUND TRUTH LABELING STRATEGY: Liu et al.'s overreliance labels are outcome-based—a single per-task label assigned to all behavioral segments regardless of what happened in each specific window. Training a streaming classifier on these temporally misaligned labels would conflate overreliant and non-overreliant moments within the same session. We adopt a hybrid multi-signal labeling approach: (a) OUTCOME PROPAGATION via Multiple Instance Learning: for each accepted misinformation item, trace back to the behavioral window from first exposure through acceptance, treating the session as a 'bag' with the task-level overreliance label, and let an attention-based MIL pooling layer learn which sub-segments are most predictive; (b) WEAK SUPERVISION via programmatic labeling functions encoding Liu et al.'s five behavioral patterns as heuristic rules (e.g., 'copy-paste within 10s of LLM response without scrolling through response → OVERRELIANT'; 'reads task prompt >15s before first LLM query → NOT_OVERRELIANT'; 'pastes LLM content block without subsequent editing → OVERRELIANT'), reconciled via a Snorkel-style generative model into probabilistic training labels; (c) SPARSE METACOGNITIVE PROBES: at 2–3 event-triggered points per task (triggered by detected behavioral state transitions, not fixed intervals), prompt users briefly: 'How carefully are you evaluating the AI's response right now?' (5-point scale)—far less intrusive than Adjust for Trust's 30 every-decision ratings; (d) SELF-SUPERVISED REGULARIZATION: a next-action prediction auxiliary objective captures behavioral dynamics without requiring labels. The classifier is trained with a weighted multi-task loss combining all four signal types, with outcome labels serving as calibration rather than primary supervision.\n\nWEAK SUPERVISION CIRCULARITY ANALYSIS AND ABLATION: We explicitly address the risk that the CNN trained on weak supervision labels may learn to replicate the hand-coded labeling function rules rather than discover deeper temporal patterns—since the labeling functions encode behavioral patterns (e.g., copy-paste frequency, dwell time thresholds) derived from the same interaction features the CNN processes. While the Snorkel literature demonstrates that discriminative end models typically generalize beyond labeling functions (averaging 9.5-point accuracy improvements over the label model alone, as they learn subtle feature combinations and contextual patterns the heuristics miss), this generalization is not guaranteed and must be empirically verified. We design a four-condition ablation to isolate each labeling signal's contribution: (i) WS-ONLY: trained exclusively on weak supervision labels—establishes the upper bound on circularity risk, as the only supervisory signal comes from features the model also takes as input; (ii) MIL+PROBES ONLY: trained on outcome-propagated MIL labels and sparse metacognitive probe labels with NO weak supervision—these labels are derived from task outcomes and self-report respectively, providing supervision entirely independent of the input behavioral features, thereby serving as the circularity-free baseline; (iii) MIL+PROBES+SELF-SUPERVISED: adds the self-supervised next-action prediction objective to condition (ii)—tests whether temporal dynamics learning further improves outcome-based detection; (iv) FULL MULTI-SIGNAL: all four label sources combined. The critical diagnostic comparison is (iv) vs. (ii): if full training substantially outperforms MIL+probes-only training, the weak supervision provides complementary signal beyond what outcome labels alone capture; if (iv) ≈ (i) >> (ii), the model is primarily learning the hand-coded rules (confirming the circularity concern). Additionally, we conduct feature importance analysis using Integrated Gradients attribution on models from each condition, comparing the learned feature importance profiles against the features explicitly encoded in labeling functions. If the full model assigns substantial attribution to features NOT encoded in any labeling function (e.g., temporal velocity patterns, micro-hesitation dynamics, action transition probabilities), this provides positive evidence of generalization beyond the heuristic rules. We will report these ablation results as a primary finding, following the XPASC framework's principle that measuring generalization beyond labeling functions is essential for validating weakly-supervised classifiers.\n\nCONTRIBUTION ROBUSTNESS: WHAT IF DETECTION ACCURACY IS LOW? We explicitly frame streaming behavioral overreliance detection as the core empirical hypothesis being tested, not an assumed capability. The prior evidence is sobering: Adjust for Trust's Appendix D achieves F1 ≤ 0.5 with surface-level behavioral heuristics, Sensing What Surveys Miss reaches only ~61% with linear regression on mouse+EDA, and Dechant et al. find mouse features alone insufficient. Our hypothesis is that multi-resolution temporal processing on richer multi-dimensional behavioral features—following the positive trajectory shown by Campagna et al. (84% in HRI) and Kaneko & Yamada (90% in cooperative tasks)—can substantially improve on these baselines in the LLM conversation domain. However, there exists a realistic scenario where our classifier achieves only 65–70% accuracy—better than prior baselines but potentially insufficient for reliable real-time intervention. We explicitly plan for this contingency: (1) The within-subjects comparison of four intervention conditions (no intervention, static CFF, self-report-adaptive, behaviorally-triggered adaptive) constitutes a valuable empirical contribution REGARDLESS of detection accuracy—it provides the first head-to-head comparison of these paradigms in free-form LLM conversations, with the self-report-adaptive condition serving as an upper-bound benchmark for behavior-triggered approaches. Even a moderate-accuracy classifier may outperform static interventions by reducing alert fatigue and targeting interventions to riskier moments. (2) The hybrid labeling methodology (MIL + weak supervision + sparse probes + self-supervised regularization) is an independent methodological contribution applicable to any streaming behavioral classification task with outcome-level labels, publishable as a methods contribution for the temporal action localization community. (3) Characterizing WHAT behavioral signals can and cannot predict about overreliance—via the four-condition ablation, feature importance analysis, and learning curves—is itself an informative contribution that advances the field's understanding of the behavioral-detection frontier, directly addressing the open question left by Adjust for Trust's Appendix D. (4) The instrumentation layer and temporal grid feature engineering for LLM conversation interactions provides reusable infrastructure for future research. We will report detection accuracy honestly and frame negative or moderate results as informative findings about the boundaries of behavioral sensing for reliance calibration, following Raees & Papangelis's (2026) call for rigorous behavioral measurement of appropriate reliance.\n\n(3) TIERED ADAPTIVE INTERVENTION ENGINE: When the streaming risk score exceeds personalized thresholds (calibrated from the 5-minute baseline), the system selects from escalating interventions: (Tier 1, risk 0.5–0.7) a lightweight Assumption-style metacognitive prompt ('What might be wrong with this answer?') shown as a non-blocking tooltip; (Tier 2, risk 0.7–0.9) a counter-explanation surfacing potential errors in the LLM's response, modeled on Adjust for Trust's strategy, with a 10-second reading delay; (Tier 3, risk >0.9) a comprehension checkpoint requiring the user to identify one potential issue before proceeding. A cooldown mechanism (minimum 2 minutes between interventions) prevents alert fatigue.\n\nECOLOGICAL VALIDITY CONSIDERATIONS: We acknowledge that our evaluation paradigm—researcher-injected misinformation in controlled tasks—follows the standard methodology employed by both Liu et al. (CHI 2026) and Adjust for Trust (IUI 2026), but has inherent ecological validity limitations. Injected misinformation is typically more blatant, consistently placed, and fact-checkable compared to natural LLM hallucinations, which are subtler, context-dependent, and may involve plausible-sounding but unverifiable claims. As Ren et al. (arXiv 2510.10539) demonstrate with their AuthenHallu benchmark, hallucinations in authentic LLM-human interactions differ qualitatively from artificially constructed errors, occurring in 31.4% of real query-response pairs with highly variable subtlety. Our controlled design is necessary for establishing internal validity—it enables precise measurement of overreliance rates and intervention effects with known ground truth—but a classifier trained solely on controlled-misinformation tasks may not fully generalize to naturalistic LLM use where the 'correct' level of reliance is ambiguous. We address this in two ways: (1) Liu et al.'s misinformation includes varied subtlety levels (hallucinations, outdated knowledge, prompt injection attacks) that partially approximate natural error diversity, and (2) we plan a follow-up naturalistic deployment study where participants use the system during their regular LLM interactions over 2 weeks, with overreliance assessed via retrospective expert review of interaction logs—a design explicitly motivated by ecological validity concerns.\n\nEVALUATION: A within-subjects study (N≈120) across four LLM-assisted decision tasks with injected misinformation (quiz/ranking, article summarization, trip planning, code review), counterbalanced via Latin square across four conditions: (a) no intervention (control), (b) static cognitive forcing (always-on Assumption-CFF per Ghosh et al.), (c) self-report-adaptive (replicating Adjust for Trust's 11-point scale + counter-explanations), and (d) behaviorally-triggered adaptive (OverrelianceGuard). Each participant completes four tasks (~75 min total), one per condition. Primary metrics: overreliance reduction rate (misinformation acceptance, measured via both Traditional over-reliance rate and Appropriateness-view RAIR/RSR metrics per Raees & Papangelis's framework), task accuracy, detection latency (time from overreliance onset to intervention trigger), intervention precision/recall (validated against outcome and metacognitive probe labels), user satisfaction (NASA-TLX + custom intrusiveness scale), and comparative survey interruption burden between conditions (c) and (d). Secondary analysis: per-user classifier calibration curves, learning curves showing accuracy vs. training data fraction, four-condition weak supervision ablation with feature importance analysis, and qualitative analysis of intervention-triggered behavioral shifts.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '80', 'timeline': '7-9 months (2 months system dev + labeling pipeline, 1 month IRB + pilot, 2-3 months main study with 120 participants, 2-3 months analysis and writing)', 'estimated_gpu_cost': '$120 (A100 at ~$1.50/hr spot pricing; model is only ~40K params so training is fast; GPU time dominated by hyperparameter search, data augmentation pipeline, Snorkel label model training, and 4-condition ablation)'}, 'human_in_loop': {'gpu_hours': '60', 'timeline': '5-7 months (Claude accelerates extension code, labeling function design, ONNX export pipeline, and statistical analysis)', 'claude_api_cost': '$250 (Sonnet 4.6 for code generation, weak supervision labeling function refinement, intervention prompt engineering, and analysis scripts; ~80M tokens)', 'estimated_gpu_cost': '$90 (A100 at ~$1.50/hr spot pricing)'}, 'auto_research': {'gpu_hours': '50', 'timeline': '4-6 months (automated architecture search across CNN/MiniRocket/LSTM variants, labeling function optimization, and ablation analysis; human study remains irreducible)', 'claude_api_cost': '$500 (Sonnet 4.6 for automated pipeline: architecture comparison, labeling function generation and evaluation, intervention prompt tuning via batch API, paper drafting; ~160M tokens)', 'estimated_gpu_cost': '$75 (A100 at ~$1.50/hr spot pricing)', 'speed_bottleneck': 'IRB approval (4-8 weeks) and sequential participant recruitment for within-subjects study are irreducible human-in-the-loop requirements that cannot be parallelized by automation'}}\n\n## Inspired By\nUntried combination: rich behavioral interaction signals from Liu et al. (CHI 2026) + trust-adaptive intervention strategies from 'Adjust for Trust' (IUI 2026), without the physiological sensor requirement of 'Sensing What Surveys Miss' (CHI 2026). Gap validation: Adjust for Trust's Appendix D documents that surface-level behavioral features fail to predict trust (F1 ≤ 0.5), and Sensing What Surveys Miss achieves only ~61% accuracy even with combined mouse+EDA using linear regression—both motivating richer multi-resolution temporal processing via deep learning. Positive evidence from Campagna et al. (84% trust classification in HRI) and Kaneko & Yamada (90% in cooperative tasks) establishes that the failure is in modeling depth, not in behavioral signals per se—justifying our investment in multi-resolution temporal architectures. Measurement-theoretic insight from Raees & Papangelis (2026): appropriate reliance is behaviorally observable and conceptually distinct from trust, grounding our choice to detect reliance behavior rather than infer trust attitudes. Cross-paradigm transfer: extending Li et al.'s adaptive explanation selection principle from structured tabular tasks with coarse feedback to free-form conversational LLM interactions with continuous behavioral sensing. Architecture insight: lightweight time series classifiers (PRISM, ~40K params) demonstrate that efficient sub-millisecond browser-embedded inference is feasible at this parameter scale, making sensor-free any-browser deployment practical where prior approaches (Sensing What Surveys Miss) assumed physiological hardware. Labeling methodology: adapting the hybrid weak-supervision + outcome-propagation approach from fraud detection and temporal action localization, informed by TimeMIL's time-aware MIL pooling for temporal sequence data, to solve the streaming-vs-outcome temporal misalignment problem that Liu et al.'s post-hoc analysis did not address—with explicit ablation design to verify the classifier generalizes beyond hand-coded labeling function rules, informed by the XPASC framework for measuring weak supervision generalization.\n\n## Target Venues\n- CHI 2027 (paper deadline: September 10, 2026) — top-tier HCI, ideal fit for closed-loop behavioral+intervention system contribution with within-subjects evaluation\n- IUI 2027 (paper deadline: August 20, 2026) — natural successor venue to the Adjust-for-Trust IUI 2026 paper; strong fit for adaptive UI contribution\n- CSCW 2027 (rolling submissions, fully open 2027) — strong fit for collaborative human-AI reliance calibration framing and the labeling methodology contribution\n- IMWUT / UbiComp (next deadline: November 1, 2026) — fits if emphasizing ubiquitous non-invasive sensing of interaction behavior\n- AAAI 2027 (paper deadline: July 28, 2026) — if framing emphasizes the hybrid labeling methodology and streaming classification contribution\n\n## Key References\n- Liu, Zhou, Shen, Liu, Wu & Chen. Behavioral Indicators of Overreliance During Interaction with Conversational Language Models (CHI 2026, arXiv 2602.11567)\n- Srinivasan & Thomason. Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (IUI 2026, arXiv 2502.13321)\n- Li, Zhu, Lu, Xiao & Yin. From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis (CHI 2025, arXiv 2502.11919)\n- Ailin Liu, Karoui, Draxler, Kreuter & Chiossi. Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM Support by User Modeling (CHI 2026, arXiv 2602.00880)\n- Kaneko & Yamada. Predicting Trust Dynamics with Dynamic SEM in Human-AI Cooperation (IEEE Access 2025, arXiv 2407.01752)\n- Campagna, Lagomarsino, Lorenzini, Chrysostomou, Rehm & Ajoudani. Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability (RA-L 2025, arXiv 2601.19856)\n- Raees & Papangelis. From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making (arXiv 2604.23896, April 2026)\n- Gurney, Pynadath & Wang. Comparing Psychometric and Behavioral Predictors of Compliance During Human-AI Interactions (Persuasive Technologies 2023, arXiv 2302.01854)\n- Sun et al. Eyes Can't Always Tell: Fusing Eye Tracking and User Priors for User Modeling under AI Advice Conditions (arXiv 2604.01741, 2026)\n- Ibrahim et al. Measuring and Mitigating Overreliance Is Necessary for Building Human-Compatible AI (arXiv 2509.08010, 2025)\n- Buçinca, Malaya & Gajos. To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making (CSCW 2021)\n- Ghosh et al. An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, 2026)\n- PRISM: Multi-Resolution Time Series Classification via Symmetric Dilated Convolutions (Neurocomputing 2026, arXiv 2508.04503)\n- From Calibration to Collaboration: LLM Uncertainty Quantification Should Be More Human-Centered (arXiv 2506.07461, June 2025)\n- de Jong et al. Cognitive Forcing for Better Decision-Making: Reducing Overreliance on AI Systems Through Partial Explanations (CSCW 2025)\n- Ren, Gruhlke & Lauscher. Detecting Hallucinations in Authentic LLM-Human Interactions (arXiv 2510.10539, 2025)\n- Dechant, Shukla & Bhatt. Mice, Masks, and Monotones: On the Reliability of Mouse Trajectories as Indicators of Trust (arXiv 2310.16632, 2023)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:38:36.002Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:38:36.002Z",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:38:36.018Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient field context. Let me compile my evaluation.

---

```
【阶段】: Triage
```

## ⚠️ 关键前置问题：CoRL 2026 严重的 Venue Mismatch

在正式评估 idea 质量之前，必须指出一个**致命的投稿策略问题**：

**CoRL (Conference on Robot Learning)** 的 Call for Papers 明确要求 "Submissions should focus on a core robotics problem" 并且 "Submissions without a robotics focus will be returned without review." 这篇 proposal 是一个纯 HCI/Human-AI Interaction 的工作——浏览器扩展检测用户对 LLM 的过度依赖并触发干预——**完全不涉及机器人学习**。如果投稿 CoRL 2026，极大概率会被 desk reject。

Proposal 自身列出的目标会议（CHI、IUI、CSCW、IMWUT、AAAI）才是正确的 venue。以下评估基于 idea 本身的学术质量，**以 CHI/IUI 等 HCI venue 为参照系**进行打分。如果用户确实要投 CoRL，概率接近 0%。

---

```
【领域调研】:
```

- **[Liu et al., arXiv 2602.11567] (CHI 2026)**: 确认存在。77 名参与者，3 个任务，通过 autoencoder 聚类发现 5 种行为模式区分高/低过度依赖用户。提供了行为信号词汇表，但明确将实时检测和干预留作 future work。这是本 proposal 最直接的前置工作。
- **[Srinivasan & Thomason, arXiv 2502.13321] (IUI 2026)**: 确认存在。Trust-adaptive intervention，38% 不当依赖降低，但要求每次决策后 11 分量表自报告。Appendix D 的行为估计失败 (F1 ≤ 0.5) 是本 proposal 的核心 motivation。
- **[Ailin Liu et al., arXiv 2602.00880] (CHI 2026)**: 确认存在。最接近的架构先例——用鼠标+EDA 构建闭环系统，但目标是认知负荷（非过度依赖），需要生理传感器，线性回归分类器仅~61%。
- **[Campagna et al., arXiv 2601.19856] (RA-L 2025)**: 确认存在。HRI 场景中行为指标预测信任达 84% 准确率 (AUC=0.90)，但样本量极小 (N=14)，且是物理机器人场景——与 LLM 对话场景的 domain gap 非常大。
- **[Raees & Papangelis, arXiv 2604.23896] (2026)**: 确认存在。区分 trust 和 appropriate reliance 的测量理论工作，为用行为过程指标替代主观信任评分提供了理论基础。
- **调研总结**: 这个领域处于一个「识别信号→构建系统」的过渡阶段。Liu et al. (CHI 2026) 建立了行为信号基础，Adjust for Trust (IUI 2026) 验证了自适应干预的价值但暴露了行为检测的失败，Sensing What Surveys Miss 建了闭环但在不同任务域且依赖生理传感器。**确实存在一个尚未被填补的 gap：纯行为信号→实时检测→自适应干预，在 LLM 对话场景中。** Proposal 对 gap 的定位是准确的。

---

```
【Trivial Alternative 检验】:
```

**存在 partial trivial alternatives，但 proposal 有增量价值。**

1. **最简单的 baseline**：基于规则的启发式（如 Adjust for Trust Appendix D 中尝试的 AIAcc5、CapabilityDiff 等）。但已有证据表明这些方法 F1 ≤ 0.5，不可用。这恰恰是 proposal 的 motivation。
2. **次简单的 baseline**：用 Liu et al. 识别的 5 种模式直接写规则触发干预（无需训练 CNN）。这是一个 **真正的威胁**——proposal 对此的回应是 weak supervision circularity ablation（条件 i vs ii），设计合理，但**核心问题是：多分辨率 CNN 相比手写规则的增量到底有多大？** 如果 ablation 显示 CNN 只是重新学习了手写规则（条件 iv ≈ 条件 i），则整个检测模块的技术贡献大打折扣。
3. **另一个 trivial alternative**：不做实时检测，而是在固定时间点（如用户 paste 后、长时间不编辑时）触发静态干预。这种 event-triggered 方法成本极低，可能效果不差。

**增量价值判断**：proposal 的增量在于 (a) 连续流式检测 vs 离散事件触发，(b) 个性化风险阈值 vs 固定规则，(c) 分层干预 vs 单一干预。但这些增量是否能在 empirical results 中体现显著差异，取决于行为信号本身的信息量——这正是核心风险。

---

```
【前提假设检验】:
```

核心逻辑链中有**两个关键的未验证假设**：

1. **「行为信号在 LLM 对话场景中包含足够信息来区分过度依赖 vs 非过度依赖，且多分辨率时序建模能提取这些信息」**——这是整个 proposal 的核心赌注。支撑证据来自不同领域（HRI 物理协作、无人机模拟），domain gap 非常大。Adjust for Trust 在**同一领域**的失败 (F1 ≤ 0.5) 和 Sensing What Surveys Miss 加了 EDA 也才 ~61% 的事实，实际上是**反面证据**。Proposal 的论点是"失败在于建模深度不够"，但同样合理的解释是"行为信号本身在这个域中信息量不足"。

2. **「从 Liu et al. 的 outcome-level labels 可以通过 MIL+弱监督成功训练出 window-level 的流式分类器」**——这是一个非平凡的假设。Liu et al. 的标签是 per-task 粒度，而 proposal 需要 per-30-second-window 粒度的预测。MIL 的成功高度依赖于 bag 内 instance 的区分度——如果一个"过度依赖"session 中 80% 的 windows 看起来和"非过度依赖"session 一样，MIL 的 attention 机制很难收敛。

Proposal 对这些风险有所认知（设计了 dual-outcome 框架），但**这些是 idea 层面的根本性不确定性，不是实验设计能完全化解的**。

---

```
【3 维度打分】:
```

**1. Novelty: 中** — Gap 定位准确且目前确实无人填补。将 Liu et al. 的行为信号、Adjust for Trust 的干预框架、轻量级时序分类器整合为闭环系统是一个合理的「untried combination」。但核心 novelty 是**系统集成**而非**方法论突破**。每个组件（1D-CNN 时序分类、Snorkel 弱监督、MIL、分层干预）都是已有技术的直接应用。multi-resolution CNN 相比 MiniRocket/BiLSTM 的技术差异化不够强。在 CHI/IUI 这类 venue，系统集成贡献可以被接受，但审稿人可能会说"this is a well-motivated engineering contribution rather than a methodological advance"。

**2. Significance: 中偏强** — 研究问题的重要性毋庸置疑：LLM 过度依赖是 2025-2026 HCI 领域的核心议题之一。如果行为检测确实可行，这会解锁一系列后续研究（个性化干预、长期部署、跨平台泛化）。头对头比较 self-report-adaptive vs behavior-triggered adaptive 的实验设计有独立价值。但**核心发现如果 positive（行为信号 work），审稿人大概率会说 "I would have guessed this would eventually work with enough engineering"**，而不是 "surprising"。如果 negative（行为信号不 work），informative 但影响力有限——因为已有负面证据（Adjust for Trust Appendix D）。

**3. Related Work: 强** — 这是 proposal 最突出的维度。对 Liu et al., Adjust for Trust, Sensing What Surveys Miss, From Text to Trust, Campagna et al., Raees & Papangelis 等关键工作的覆盖非常全面且准确。差异化定位清晰：每篇先行工作缺什么、本 proposal 怎么填补，逻辑链条完整。对 negative evidence (Adjust for Trust Appendix D, Dechant et al.) 的诚实引用增加了可信度。

---

```
【概率估计】: [25% - 40%] 中位 30%
```

**注意：此概率估计是针对 CHI/IUI 等 HCI venue，而非 CoRL。投 CoRL 的概率接近 0%（desk reject）。**

```
【估计理由】:
```

- **Related Work 强**：定位精准、差异化清晰，这在 CHI/IUI 审稿中是加分项，支撑了概率下界（不至于 <25%）
- **Significance 中偏强**：问题重要，但核心发现的 surprise factor 不够高，限制了上界无法突破 40%
- **Novelty 中**：系统集成型贡献，每个组件都是 existing techniques 的直接应用，限制了中位数——在竞争激烈的 CHI 中，纯集成型工作要靠实验结果的 impressive 来补偿 novelty 的不足
- **核心张力**：整个 proposal 的价值高度依赖于一个高度不确定的实证结果（行为信号是否 work）。如果 work 且效果显著 → 上界 40%（但不会更高，因为方法不够 novel）；如果 moderate (65-70%) → 25-30%（有 informative negative result 的叙事，但影响力有限）；如果 fail → ~20%（purely methodological contribution）

```
【主要风险】:
```

1. **行为信号信息量不足风险**：核心赌注——LLM 对话场景中的 mouse/keyboard 行为信号可能确实不含有足够信息来区分 window-level 的过度依赖状态，无论模型多复杂。同领域的负面证据 (F1 ≤ 0.5, ~61% with EDA) 比跨领域的正面证据 (84% in HRI with N=14) 更有参考价值。这不是实验设计能化解的 idea 层面风险。

2. **Novelty 被质疑为"pure engineering"风险**：审稿人可能认为这是把 5-6 篇已有工作的组件拼在一起、加了一个 user study 的系统论文，缺乏深层方法论创新。在 CHI 这样投稿量巨大的会议，这类质疑常见于 borderline 论文。

Sources:
- [Liu et al. - Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)
- [Srinivasan & Thomason - Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Liu et al. - Sensing What Surveys Miss (CHI 2026)](https://arxiv.org/abs/2602.00880)
- [Campagna et al. - Estimating Trust in HRC (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Raees & Papangelis - From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile my evaluation.

---

```
【阶段】: Triage
```

> ⚠️ **Venue 注意**: 系统模板指定 CoRL 2026（Conference on Robot Learning），但本 proposal 明确目标为 CHI 2027 / IUI 2027 / CSCW 2027 等 HCI 会议。本 proposal 与 CoRL 的主题完全不匹配（无机器人学习内容），若投 CoRL 中稿概率趋近于 0%。**以下评估基于 proposal 自身目标的 HCI 顶会（CHI/IUI）进行。**

---

```
【领域调研】:

- [Liu et al., "Behavioral Indicators of Overreliance During Interaction with Conversational Language Models"](https://arxiv.org/abs/2602.11567) (CHI 2026): 
  本 proposal 的直接前驱。77 名被试 × 3 tasks，注入 misinformation，通过 autoencoder 聚类识别出 5 种与 overreliance 关联的行为模式（如频繁 copy-paste、跳过任务理解、粗粒度黏贴等）。关键局限：仅做 post-hoc 行为特征刻画，明确将 real-time detection 和 intervention 留作 future work。该论文使用 per-event 37 维编码，与 proposal 中的 30×28 temporal grid 表征有明确差异。确认存在且描述准确。

- [Srinivasan & Thomason, "Adjust for Trust"](https://arxiv.org/abs/2502.13321) (IUI 2026): 
  Trust-adaptive 干预系统，通过 11 点自报告量表在每个决策后收集信任值，据此选择 supporting 或 counter-explanation。在科学问答和医学诊断任务中实现最高 38% inappropriate reliance 减少。Appendix D 明确记录了 behavioral trust estimation 的失败尝试（F1 ≤ 0.5）。确认存在且描述准确。

- [Liu et al., "Sensing What Surveys Miss"](https://arxiv.org/abs/2602.00880) (CHI 2026): 
  结构上最相似的前驱——闭环系统，用鼠标动态 + EDA 皮肤电驱动个性化 linear regression 分类器，在在线问卷中检测 cognitive load 并触发 LLM-based 干预。N=32，aligned-adaptive 条件下准确率提升 21%，false negative 从 50.9% 降至 22.9%。关键差异：(a) 目标是 cognitive load 而非 overreliance；(b) 需要 EDA 腕带；(c) 使用简单线性回归，仅 ~61% 检测准确率。确认存在且描述准确。

- [Campagna et al., "Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability"](https://arxiv.org/abs/2601.19856) (RA-L 2025): 
  化学品混合任务中通过 7 种行为指标（凝视、位移、速度同步等）用 Voting Classifier 达到 84% trust 分类准确率（AUC=0.90）。但样本极小（N=14），且为物理 HRI 场景，与 LLM 对话的 domain gap 很大。确认存在且描述准确。

- [Raees & Papangelis, "From Trust to Appropriate Reliance"](https://arxiv.org/abs/2604.23896) (arXiv, April 2026): 
  测量理论 review，区分 trust 与 appropriate reliance 为不同构念，提出 Traditional/Appropriateness/Dominance 三种测量视角。支持用行为过程指标替代主观信任评级。确认存在且描述准确。

- [PRISM: Lightweight Multivariate Time-Series Classification](https://arxiv.org/abs/2508.04503) (Neurocomputing 2026):
  通过对称 FIR 滤波器实现多分辨率轻量 CNN，~40K 参数在 UCI-HAR 等基准上达到 97.3%。确认存在。Proposal 中已做合理 caveat——UCI-HAR 的 6 类物理活动分类与 overreliance 的噪声行为信号差异巨大。

- 直接竞争者搜索：未发现任何已有系统实现 "仅用行为信号、无传感器、闭环检测 + 干预 LLM overreliance" 的组合。Liu et al. 和 Adjust for Trust 都明确指出这是 open gap。

- 调研总结：该领域处于 "行为信号已被刻画、干预策略已被验证、但二者未被连接" 的阶段。Proposal 定位于填补这个明确的 gap，核心赌注在于 behavioral signals 单独能否支撑有用精度的 streaming 检测——现有证据正反参半（Adjust for Trust 失败 vs. HRI 领域正面结果），domain transfer 可行性未知。
```

---

```
【Trivial Alternative 检验】:

最直接的 trivial alternative：**定时/随机触发 CFF（如每 2 分钟弹一次 metacognitive prompt）**。
这完全绕过了检测模块——不需要 CNN、不需要 temporal grid、不需要 labeling pipeline。
Buçinca et al. (CSCW 2021) 已证明 static CFF 确实能降低 overreliance。

Proposal 的增量价值声称是：行为触发的 adaptive 干预比 static CFF 更优，因为 (1) 减少 alert fatigue，(2) 将干预精准定位到高风险时刻。但这个增量的大小完全取决于检测准确率——而这正是 proposal 自身标记为 "core empirical hypothesis" 的未知数。

第二个 trivial alternative：**用 Liu et al. 的 5 个行为模式直接写 rule-based 阈值检测器**，不需要训练 CNN。Proposal 在 weak supervision circularity ablation 中部分处理了这个问题（condition i: WS-only），但如果 rule-based 检测已经接近 CNN 性能，那么 CNN 的价值就很有限。

结论：Trivial alternative 威胁真实存在。Proposal 对此有意识（包含 static CFF 作为 baseline、设计了 ablation），但核心 delta 取决于检测精度这个未知数。如果最终 CNN ≈ rule-based ≈ 65-70%，那么整个 ML pipeline 的增量价值有限。
```

---

```
【前提假设检验】:

核心逻辑链：
行为信号包含 overreliance 信息 → 30×28 temporal grid 能有效捕获这些信息 → 40K-param CNN 能从 ~30K windows 学到有用模式 → 实时检测精度足以支撑有意义的 adaptive 干预 → adaptive 干预优于 static CFF

逐环检验：

1. ❌ "行为信号在 window 级别包含足够 overreliance 信息"——未经验证。
   Liu et al. 的发现是 session 级别的统计关联（高/低 overreliance 组的行为分布差异），而非 window 级别的可判别性。从 session-level 统计差异到 30-second window-level 实时分类是巨大的粒度跳跃。Adjust for Trust Appendix D 的 F1 ≤ 0.5 正是在更细粒度上的失败证据。

2. ⚠️ "Campagna (84%) 和 Kaneko (90%) 证明 behavioral trust prediction 可行"——domain gap 问题严重。
   Campagna 是物理 HRI（化学混合任务，N=14，使用凝视和空间位移），Kaneko 是无人机/驾驶模拟器中的 trust dynamics。这些场景中的行为信号（身体运动、凝视方向）与 LLM 对话中的鼠标/键盘操作在信息丰富度上有本质差异。将这些作为 "positive evidence" 有误导性。

3. ⚠️ "~30K training windows 足够训练 40K-param CNN"——comparison to UCI-HAR 不恰当。
   UCI-HAR 的 6 类物理活动（走路、坐下、站立等）具有明确的运动学特征和清晰的类别边界。Overreliance 的行为信号远比加速度计数据噪声更大、类别边界更模糊。Sample efficiency 不能跨任务类比。

4. ❌ "MIL 能有效解决 session-level → window-level 的 label 传播"——假设较强。
   MIL 在包级别标签到实例级别标签的转换中，依赖于 "至少一个正例实例存在" 的假设。但在 overreliance 场景中，一个被标记为 "overreliant" 的 session 可能只有少数 windows 真正表现出 overreliant 行为，其余大部分都是正常交互。正/负比例严重不平衡时 MIL 的 attention 学习质量存疑。

总结：逻辑链的第 1 环（window-level 信息充分性）和第 2 环（domain transfer）是最薄弱的，且没有直接的实证支撑。这也是 proposal 自身将检测精度视为 "core empirical hypothesis" 的原因——proposal 对此有自我意识，但自我意识不等于问题被解决。
```

---

```
【3 维度打分】:

1. Novelty: 【中】
   
   理由：该 proposal 填补了一个真实存在且被多篇论文明确指出的 gap——没有系统将 behavioral-only signals 连接到 real-time adaptive intervention for LLM overreliance。这个 gap identification 是准确的（调研确认无直接竞争者）。
   
   但剥离 surface differences 后，novelty 的实质是 "systems integration"：
   - 行为信号词汇：直接来自 Liu et al. (CHI 2026)
   - 干预策略：来自 Adjust for Trust (IUI 2026) 和 Buçinca et al. (CSCW 2021)
   - CNN 架构：改编自 PRISM（Neurocomputing 2026）
   - Labeling 方法：MIL + Snorkel weak supervision 均为成熟技术
   - 闭环架构概念：Sensing What Surveys Miss (CHI 2026) 已经实现，只是不同 domain + 需要传感器
   
   最具独立 novelty 的部分是 hybrid labeling methodology（MIL + weak supervision + sparse probes + self-supervised），但这是将已有技术组合应用到新场景，非方法论创新。
   
   Weak supervision circularity analysis 是一个 methodological 亮点，显示了严谨性，但它是对 potential flaw 的防御性分析，非 positive novelty contribution。
   
   对标："Sensing What Surveys Miss" (CHI 2026) 在概念上非常相似（sensing → real-time detection → adaptive intervention），只是 target construct 不同（cognitive load vs. overreliance）且需要 EDA。去掉 EDA 依赖、换成 overreliance 目标，这是 incremental 的 novelty。

2. Significance: 【中偏强】
   
   理由：
   - 问题本身无可争议地重要：LLM overreliance 是 CHI/IUI 社区 2024-2026 年最热的主题之一。Ibrahim et al. (2025) 的 consolidation paper 和 Raees & Papangelis (2026) 的 measurement 框架都证实了社区的关注度。
   - 实际影响力：一个 sensor-free、browser-based 的闭环系统如果有效，其部署门槛远低于 EDA-based 方案（Sensing What Surveys Miss），有真正的实用潜力。
   - 但 significance 被两个因素限制：
     (a) 核心假设未验证——如果检测精度只有 65-70%，系统的实际价值存疑。Proposal 用 dual-outcome framing 对冲了这一风险（"即使检测失败，characterization 本身也有价值"），但这实际上是在降低 significance claim 的力度：一个 "告诉你什么不行" 的 characterization study 的 impact 远低于一个 "working system"。
     (b) 如果核心发现是 positive（检测有效），审稿人大概率会说 "interesting, but expected given the trajectory of Campagna + Kaneko + richer modeling"——不太会说 "surprising"。

3. Related Work: 【强】
   
   理由：
   - 调研确认 proposal 中引用的所有关键论文均真实存在且描述准确（Liu et al., Adjust for Trust, Sensing What Surveys Miss, Campagna et al., Raees & Papangelis, PRISM）。
   - 差异化定位非常清晰：对每个 prior work 都明确指出了与本工作的区别（Liu: 无 real-time 系统；Adjust for Trust: 需要 self-report；Sensing What Surveys Miss: 需要 EDA + 不同 target construct；Li et al.: structured task only）。
   - 对 negative evidence 的处理诚实（Dechant 2023, Adjust for Trust Appendix D），没有选择性引用。
   - 唯一微小不足：对 Campagna et al. (N=14) 和 Kaneko & Yamada 作为 "positive evidence" 的引用可能过度乐观——这两项工作的 domain gap 很大，且样本量小，作为 feasibility 论据的说服力有限。但 proposal 确实加了 caveat（"proof-of-principle rather than direct benchmarks"），基本诚实。
```

---

```
【概率估计】: [22% - 35%] 中位 28%

（注：此概率基于 CHI/IUI 等 HCI 顶会评估。若投 CoRL 2026，概率 ≈ 0-3%，因完全不匹配会议主题。）

【估计理由】:

向上拉的因素：
- 问题高度时效（LLM overreliance 是 2025-2026 HCI 社区热点）
- Gap identification 准确且被多篇论文背书（Liu et al. 和 Adjust for Trust 都明确留了这个 future work）
- Related work 覆盖全面且差异化定位清晰
- Proposal 形式完善度极高（dual-outcome、circularity ablation、ecological validity 讨论等显示了高度的方法论严谨性）
- Sensor-free browser-based 方案如果有效，有真正的实用价值

限制上界的因素：
- **Novelty 是主要瓶颈**。核心贡献是 systems integration，不是方法论或概念创新。每个组件（行为信号、干预策略、CNN 架构、labeling 方法）都有明确来源。最相似的 "Sensing What Surveys Miss" (CHI 2026) 已经证明了闭环 sensing→intervention 的可行性，只是在不同 domain。
- 核心假设（window-level behavioral signals → overreliance detection）缺乏直接支撑。从 Liu et al. 的 session-level 关联到 30-sec window-level 分类是未经验证的跳跃。
- 如果核心发现是 positive，审稿人更可能说 "nice engineering, expected result" 而非 "surprising"。
- Dual-outcome framing 是合理的风险管理，但也暴露了作者对核心 claim 的信心不足——顶会审稿人通常偏好有明确 strong claim 的论文。

概率被锚定在 25-35% 区间（"idea 有实质内核但核心发现不够 surprising"），中位 28% 反映了 novelty 偏 integration 且核心假设未验证的 discount。

【主要风险】:
1. **Novelty 不足风险**: 审稿人可能认为这是 Liu et al. + Adjust for Trust 的 "obvious next step"——两篇论文的 future work section 都明确指向了这个方向。CHI 审稿人对 "filling an explicitly stated gap" 的态度分化很大：有人认为这是 well-motivated，有人认为缺乏 intellectual surprise。
2. **"If positive, I would have guessed this" 风险**: 如果 CNN 确实比 heuristic 好，这符合 "更复杂的模型 > 简单 heuristic" 的一般直觉。如果 CNN 不比 heuristic 好，dual-outcome framing 可以保底但 contribution 的 impact 被显著削弱。无论哪种结果，都缺少一个真正 surprising 的 finding。
```

Sources:
- [Liu et al., Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)
- [Srinivasan & Thomason, Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Liu et al., Sensing What Surveys Miss (CHI 2026)](https://arxiv.org/abs/2602.00880)
- [Campagna et al., Estimating Trust in Human-Robot Collaboration (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Raees & Papangelis, From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)
- [PRISM: Lightweight Multivariate Time-Series Classification (2025)](https://arxiv.org/abs/2508.04503)
- [Buçinca et al., Cognitive Forcing Functions (CSCW 2021)](https://dl.acm.org/doi/10.1145/3449287)
- [Ghosh et al., Cognitive Forcing Functions for AI-Assisted Writing (2026)](https://arxiv.org/abs/2601.18033)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct the evaluation. Let me compile the analysis.

---

```
【阶段】: Triage

【重要前置说明 — 致命性 venue 不匹配】:
本 proposal 的目标是构建基于浏览器行为信号的 LLM 过度依赖检测与自适应干预系统，
属于纯 HCI / Human-AI Interaction 领域。CoRL 2026（Conference on Robot Learning，
2026年11月9-12日，Austin TX）的 scope 明确限定在"robot learning"——强化学习控制
物理机器人、模仿学习、sim-to-real、机器人感知、操作与运动规划等。本 proposal 不涉及
任何机器人组件、物理具身、或机器人学习问题。投稿 CoRL 大概率被 desk reject 或在
scope 审查阶段直接淘汰。proposal 自身列出的目标 venue（CHI 2027、IUI 2027、CSCW 2027、
IMWUT、AAAI 2027）才是合理选择。

以下评估基于 idea 本身的质量（venue-agnostic），但概率估计会反映 CoRL 的 venue fit。

【领域调研】:
- [Liu et al., arXiv 2602.11567] (CHI 2026): 77名参与者 × 3个任务，通过自编码器聚类
  识别出5种与LLM过度依赖相关的行为模式（频繁复制粘贴、跳过初始理解、反复参考LLM等），
  但明确将实时检测和干预留作future work。本proposal直接建立在此数据集和信号词汇之上。
  
- [Srinivasan & Thomason, arXiv 2502.13321] (IUI 2026): "Adjust for Trust"系统，
  通过自报告信任评级（每次决策后11点量表）自适应调整解释策略，实现最高38%不当依赖降低。
  Appendix D记录了行为信任估计的失败尝试（F1 ≤ 0.5）。本proposal的核心动机之一。
  
- [Ailin Liu et al., arXiv 2602.00880] (CHI 2026): "Sensing What Surveys Miss"，
  最接近的架构类比——使用鼠标动力学+EDA构建闭环系统，但：(a)目标是认知负荷而非过度依赖，
  (b)需要生理传感器，(c)线性回归分类器仅~61%准确率。N=32。
  
- [Campagna et al., arXiv 2601.19856] (RA-L 2025): 人-机器人协作中通过行为指标
  （注视方向、空间位移等）实现84%信任分类准确率。但domain是物理HRI（N=14），
  与对话式LLM交互存在显著领域差距。
  
- [Raees & Papangelis, arXiv 2604.23896] (2026): 测量理论框架，论证信任与适当依赖是
  概念上不同的构念，提倡行为过程指标——为本proposal的方法论选择提供了理论基础。
  
- [PRISM, arXiv 2508.04503] (Neurocomputing 2026): 轻量级多分辨率时序分类架构，
  ~40K参数在UCI-HAR上达97.3%。proposal借鉴其架构用于浏览器端推理。
  
- [Buçinca et al.] (CSCW 2021) + [Ghosh et al., arXiv 2601.18033] (2026): 
  认知强迫函数研究线，表明CFFs可降低过度依赖但可能增加挫折感；Assumption-style CFF最有效。
  
- [Chatsparent, arXiv 2601.11526]: 相关但不同——检测LLM对话中的认知疲劳而非过度依赖。
  
- 调研总结: 该领域在2025-2026年经历了快速发展。行为信号表征（Liu et al.）、
  自适应干预（Adjust for Trust）、多模态闭环（Sensing What Surveys Miss）分别推进了
  各自子问题，但确实没有工作仅用非侵入性浏览器行为信号在对话式LLM场景中实现
  闭环检测+干预。Proposal准确识别了这个gap。然而，这个gap的存在部分原因是
  先前尝试失败了（F1 ≤ 0.5），而非被忽视——这让"能否填补"成为一个有风险的经验性问题。

【Trivial Alternative 检验】:
存在多个更简单的替代方案需要考虑：

1. **固定间隔CFF（已作为baseline之一）**: 如果静态认知强迫函数（每次都触发）的效果与
   行为触发的自适应干预差距不大，那么整个检测管道的增量价值将大大缩水。Buçinca et al. (2021)
   已经证明always-on CFF有效降低过度依赖，区别只在于用户体验（alert fatigue）。
   如果自适应干预的主要优势仅是"减少打扰频率"而非"更准确的时机"，这个contribution就
   更像一个工程优化而非科学发现。

2. **简单启发式阈值触发**: 不需要CNN，直接用"复制粘贴后10秒内无编辑"等规则触发干预。
   Proposal承认Adjust for Trust的Appendix D用简单启发式只达F1 ≤ 0.5，但那是在
   预测信任评级——而预测"何时触发干预"的阈值可能比精确分类更容易。如果一个简单的
   规则引擎在干预效果上接近CNN方案，CNN的增量价值就有限。

3. **随机定时干预**: 如果检测准确率只有65-70%（proposal自己承认的现实场景），
   那么与随机但频率匹配的干预之间的效果差异可能不显著。

增量价值所在: 如果CNN确实能达到≥80%准确率，那么精准时机+降低打扰的组合是有实质价值的。
但这正是核心经验性假设，且先验证据并不乐观。

【前提假设检验】:
核心claim的逻辑链条中存在以下未验证假设：

1. **30秒窗口粒度假设（关键薄弱环节）**: 过度依赖是一种可在30秒滑动窗口内被检测的
   行为状态。Liu et al.的五种模式是通过对整个任务session的post-hoc分析发现的，
   这些模式是否在30秒粒度上有足够区分度是完全未知的。过度依赖可能是一个
   session-level的认知倾向，而非moment-to-moment可切换的状态。

2. **训练数据独立性假设**: 从231个session用5秒步长的滑动窗口生成~26K-40K样本，
   但相邻窗口有83%重叠（25/30秒共享），这些样本高度相关。有效独立样本数远小于
   26K-40K，可能导致严重的过拟合和虚高的交叉验证结果。Proposal提到的
   "sample-to-parameter ratio 0.65-1.0:1"严重高估了有效比率。

3. **行为信号→过度依赖的因果方向假设**: Liu et al.发现的是行为模式与过度依赖
   outcome的相关性，不是因果关系。某些行为模式可能是task difficulty的混杂效应，
   而非过度依赖的因果指标。在streaming预测中，这个问题更为突出——你在看到outcome之前
   就需要判断"过度依赖"，但这个标签本身是outcome-defined的。

4. **领域迁移假设**: 支持"行为信号可以预测信任/依赖"的正面证据（Campagna 84%，
   Kaneko 90%）来自完全不同的领域（物理HRI、无人机/驾驶模拟器），使用的是
   物理行为指标（注视、空间位移、速度同步等）。从这些结果推断到"鼠标/键盘信号
   可以预测对话式LLM过度依赖"需要一个很大的领域迁移跳跃，proposal对此诚实
   但跳跃本身仍是未验证的。

【3 维度打分】:

1. **Novelty: 中** — 
   Proposal准确识别了一个真实存在的gap：无人仅用非侵入性浏览器行为信号在对话式LLM
   场景中构建闭环检测+干预系统。这个gap在Liu et al. (CHI 2026)、Adjust for Trust 
   (IUI 2026)、Sensing What Surveys Miss (CHI 2026)三篇同期工作之间确实存在。
   
   然而，novelty的本质是**系统集成**而非**方法创新**：将Paper A的信号词汇 + Paper B的
   干预策略 + Paper C的架构思路组装为一个完整系统。各个组件——temporal grid特征工程、
   multi-resolution 1D-CNN、MIL+弱监督混合标注、分层干预引擎——均有直接的现有先例。
   混合标注策略是最有方法论novelty的部分（MIL + weak supervision + sparse probes + 
   self-supervised的组合），但其中每个子技术本身都是成熟的（Snorkel弱监督、TimeMIL、
   自监督正则化），组合虽新但并非surprising。
   
   核心问题：如果CNN检测达到80%+，审稿人的反应更可能是"合理，行为信号确实应该有信息量"
   而非"surprising，没想到这能work"。如果只达65-70%，则与prior failures一致。
   两种结果都不太可能被视为deeply surprising。

2. **Significance: 中偏强** — 
   研究问题本身（如何非侵入式地检测和缓解LLM过度依赖）是重要且及时的。LLM使用量爆发式
   增长，过度依赖是一个被广泛关注的问题（Ibrahim et al. 2025的综述明确呼吁
   process-oriented mitigation）。一个可部署的浏览器扩展方案如果work，实际影响大。
   
   但significance受限于：(a) 生态效度——受控注入错误信息 vs. 自然LLM幻觉的差距，
   proposal自身引用Ren et al.承认了这一点；(b) 如果核心检测性能不够好，
   "what behavioral signals can and cannot predict"的characterization贡献虽有价值，
   但更适合作为workshop paper而非主会contribution的核心。
   
   对HCI领域（CHI/IUI）的significance是实质性的；对CoRL完全不相关。

3. **Related Work: 强** — 
   这是proposal最突出的优点。对相关工作的覆盖非常全面且精确：
   - 直接前序工作（Liu et al., Adjust for Trust, Sensing What Surveys Miss, 
     From Text to Trust）的描述准确，差异化定位清晰
   - 正面和负面证据都有引用（Campagna/Kaneko的正面 vs. Dechant/Adjust for Trust 
     Appendix D的负面），没有cherry-pick
   - 测量理论基础（Raees & Papangelis）的引入增强了概念严谨性
   - 所有查证的关键引用（arXiv ID、venue、发现）均真实准确
   - 与最近的Chatsparent (2025)等工作没有overlap
   
   唯一的轻微gap：没有讨论attention-based或transformer方法在类似规模行为数据上的
   表现，只与MiniRocket和BiLSTM做对比，但这属于实验设计层面的问题，不影响related work评分。

【概率估计】: 
- 如投CoRL 2026: [1% - 5%] 中位 2%
- 如投CHI/IUI 2027（proposal实际目标venue）: [25% - 40%] 中位 32%

【估计理由】: 
**CoRL概率（2%）**: 这是一篇纯HCI论文，与CoRL的scope（robot learning）完全不匹配。
无机器人组件、无物理具身、无学习控制物理系统。大概率在scope审查阶段被拒，
即使进入审稿也会因"out of scope"获得强拒。这不是idea质量问题，是venue选择错误。

**CHI/IUI参考概率（32%）**: idea有真实gap、方向正确、related work扎实。
Novelty为"中"（系统集成型novelty，非surprising发现）限制了上界——即使实验完美执行，
核心发现大概率落在"makes sense"而非"surprising"区间。前提假设中30秒窗口粒度和
训练数据独立性问题增加了核心claim不成立的风险。混合标注方法论是加分项。
Dual-outcome设计提供了一定的下限保障。对CHI/IUI，这个idea处于"有实质内核但不
outstanding"的区间。

【主要风险】:
1. **（CoRL层面）致命性venue不匹配**: 本proposal与CoRL的scope完全不符。
   这不是可以通过reframing修复的问题——论文的entire contribution都在HCI领域，
   没有任何组件可以legitimately声称是robot learning contribution。
   
2. **（idea层面）核心经验性假设薄弱**: 30秒窗口内行为信号能否区分过度依赖状态，
   是整个系统的基础假设，但先验证据指向负面（F1 ≤ 0.5、~61%），
   正面证据来自完全不同的领域（物理HRI）。如果这个假设不成立，
   系统的core contribution（闭环检测+干预）就无法兑现。
   虽然proposal的dual-outcome设计提供了保底，但"characterizing what doesn't work"
   作为CHI主会论文的核心卖点说服力有限。
```

---

**总结**: 这个proposal作为HCI研究是一份质量中上的工作——gap真实、related work扎实、方法论设计审慎。但**投稿CoRL 2026是根本性的venue选择错误**。CoRL聚焦于robot learning（强化学习控制物理机器人、模仿学习、sim-to-real等），本proposal不含任何机器人学习组件。建议作者回到其原始目标venue列表（CHI 2027 / IUI 2027），在那些venue中这个idea有合理的竞争力（估计~32%中稿概率）。

Sources:
- [Liu et al. - Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)
- [Srinivasan & Thomason - Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Liu et al. - Sensing What Surveys Miss (CHI 2026)](https://arxiv.org/abs/2602.00880)
- [Campagna et al. - Estimating Trust in HRC (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Raees & Papangelis - From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)
- [PRISM - Multi-Resolution Time Series Classification (2025)](https://arxiv.org/abs/2508.04503)
- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Buçinca et al. - Cognitive Forcing Functions (CSCW 2021)](https://dl.acm.org/doi/abs/10.1145/3449287)


【原始 proposal（允许参考但不是主要依据）】:
# Closing the Loop: From Behavioral Overreliance Detection to Adaptive Intervention in LLM Conversations

## Description
We propose OverrelianceGuard, the first closed-loop system that bridges unobtrusively collected behavioral interaction signals to real-time adaptive interventions in free-form conversational LLM interactions—without requiring self-report interruptions or physiological sensors. A browser extension captures non-invasive interaction events in 30-second sliding windows and transforms them into a temporal grid representation: each window is discretized into 30 one-second bins, with 28 aggregated features per bin capturing action type distribution (over 12 categories), mouse dynamics (distance, velocity), scroll behavior (distance, direction), keypress statistics, copy-paste behavior (including post-paste edit indicators), idle duration, dwell context relative to LLM responses, and page focus. This (30 × 28) temporal grid—derived from but explicitly distinct from Liu et al.'s (CHI 2026) per-event 37-dimensional encoding (15-dim action type one-hot + 1-dim timestamp + 2-dim page type + 19-dim type-specific attributes)—feeds a lightweight multi-resolution 1D-CNN (~40K parameters, <5ms browser inference via ONNX Runtime Web) with three parallel temporal branches capturing short-burst (2s), medium-term (10s), and full-window (30s) behavioral dynamics. We cite PRISM's 97.3% accuracy on UCI-HAR as evidence of architectural efficiency at this parameter scale, not as a performance projection—UCI-HAR involves 6-axis accelerometer data with well-separated activity classes, whereas overreliance classification operates on noisier interaction features with subtler boundaries. The architecture choice is motivated by converging evidence that simple models on behavioral signals are insufficient—Adjust for Trust's Appendix D found F1 ≤ 0.5 with surface-level heuristics, 'Sensing What Surveys Miss' (CHI 2026) achieves only ~61% with linear regression on mouse+EDA—while richer models on multi-dimensional behavioral features show substantially better results: Campagna et al. (RA-L 2025) achieve 84% trust classification (AUC=0.90) from behavioral indicators in HRI, and Kaneko & Yamada (2025) reach 90% in cooperative tasks. A methodological contribution is the hybrid labeling strategy addressing temporal misalignment between Liu et al.'s outcome-based labels and streaming prediction: outcome propagation via Multiple Instance Learning, weak supervision from programmatic heuristics encoding the five identified behavioral patterns, sparse event-triggered metacognitive probes (2–3 per task vs. Adjust for Trust's 30 per-decision self-reports), and self-supervised next-action prediction. Critically, we address the weak supervision circularity risk—where labeling functions encode behavioral patterns from the same feature space the CNN processes—through a four-condition ablation: (i) weak-supervision-only, (ii) MIL+probes-only (circularity-free, as labels derive from task outcomes and self-report), (iii) MIL+probes+self-supervised, and (iv) full multi-signal training. Comparing conditions (iv) vs. (ii) isolates whether the weak supervision provides complementary signal or merely teaches the CNN its own hand-coded rules, with Integrated Gradients feature attribution analysis revealing whether the model discovers temporal patterns beyond those encoded in labeling functions. We frame streaming behavioral overreliance detection as the core hypothesis being tested: if classifier accuracy proves disappointing (e.g., 65–70%), the within-subjects intervention comparison, the labeling methodology, and the characterization of what behavioral signals can and cannot predict all constitute independently publishable contributions. We analyze training data sufficiency: Liu et al.'s 77-participant dataset yields ~26K–40K behavioral windows with our proposed windowing, supplemented by augmentation and a phased training strategy. When overreliance risk exceeds personalized thresholds, the system selects from tiered interventions: metacognitive prompts (Assumption-style CFFs), counter-explanations (per Adjust for Trust), and comprehension checkpoints. Following Raees & Papangelis's (2026) measurement framework distinguishing trust from appropriate reliance, we assess overreliance via both Traditional (acceptance rates) and Appropriateness-view (RAIR/RSR) metrics. A within-subjects study (N≈120) across four LLM-assisted tasks compares four conditions: no intervention, static cognitive forcing, self-report-adaptive (replicating Adjust for Trust), and behaviorally-triggered adaptive (OverrelianceGuard). This work fills the gap between behavioral characterization (Liu et al., CHI 2026), trust-adaptive intervention via self-report (Adjust for Trust, IUI 2026), adaptive explanation selection in structured tasks (Li et al., CHI 2025), and sensor-dependent adaptive support (Sensing What Surveys Miss, CHI 2026)—contributing (1) the first streaming behavioral overreliance classifier for conversational LLM settings with a principled hybrid labeling methodology and explicit circularity analysis, (2) a deployable browser-based closed-loop intervention system requiring neither self-report interruptions nor physiological sensors, (3) head-to-head empirical evidence comparing self-report-based vs. behavior-based adaptive intervention, and (4) a rigorous characterization of what behavioral signals can and cannot predict about overreliance, advancing the field regardless of detection accuracy.

## Core Problem
Can unobtrusively collected behavioral interaction signals (copy-paste patterns, scroll depth, verification dwell time, tab-switch frequency) drive a real-time streaming classifier that triggers adaptive interventions to reduce overreliance on LLM outputs—without requiring self-report interruptions or invasive physiological sensors?

## Opportunity
Liu et al. (CHI 2026, arXiv 2602.11567) identify five behavioral patterns distinguishing high- vs. low-overreliance users in LLM interactions but explicitly leave real-time detection and intervention as future work. Srinivasan & Thomason's 'Adjust for Trust' system (IUI 2026, arXiv 2502.13321) achieves up to 38% reduction in inappropriate reliance through trust-adaptive interventions, but requires self-reported trust ratings on an 11-point scale after every decision—an intrusive approach whose inadequacy the authors themselves confirm in Appendix D, where their attempts at behavioral trust estimation yielded only 0.25–0.51 correlation and F1 ≤ 0.5 using surface-level interaction heuristics. Li et al.'s 'From Text to Trust' (CHI 2025, arXiv 2502.11919) adaptively selects explanations via POMDP-based hidden state estimation, but operates only in structured tabular decision tasks using coarse binary (agree/disagree) feedback—not rich behavioral signals in free-form LLM conversations. Ailin Liu et al.'s 'Sensing What Surveys Miss' (CHI 2026, arXiv 2602.00880) build the closest architectural parallel—a closed-loop system using mouse dynamics and electrodermal activity (EDA) to trigger adaptive LLM-based interventions—but target cognitive load during online surveys (not overreliance in LLM conversations), require physiological sensors (EDA wristbands), and achieve only ~61% detection accuracy with simple linear regression classifiers and max-fusion of two unimodal models; crucially, the paper provides no ablation separating mouse-only from EDA contributions, leaving open the question of whether interaction signals alone—processed with richer temporal modeling than linear regression—can achieve adequate detection without physiological sensing. The evidence for behavioral trust prediction is mixed but increasingly positive: while Dechant et al. (2023) find mouse trajectories alone insufficient and Adjust for Trust's Appendix D reports F1 ≤ 0.5 with surface-level heuristics, Campagna et al. (RA-L 2025, arXiv 2601.19856) achieve 84% accuracy classifying trust from behavioral indicators in human-robot collaboration using ensemble classifiers, and Kaneko & Yamada (IEEE Access, 2025; arXiv 2407.01752) demonstrate 90% accuracy predicting trust dynamics via dynamic structural equation modeling in physical cooperative tasks—both suggesting that behavioral features CAN support useful trust prediction with appropriate modeling depth, even if the domain gap to conversational LLM settings makes these figures proof-of-principle rather than direct benchmarks. Raees & Papangelis ('From Trust to Appropriate Reliance,' arXiv 2604.23896, April 2026) further argue that trust measurements are conceptually distinct from appropriate reliance—the construct we actually target—and advocate for behavioral process metrics over subjective trust ratings, providing measurement-theoretic grounding for our approach. The bridge remains unbuilt: no system uses fine-grained, continuously captured interaction signals alone to detect overreliance and trigger personalized interventions in conversational LLM settings. This is now technically feasible because (1) Liu et al.'s behavioral characterization provides the validated signal vocabulary via per-event interaction encodings, (2) lightweight time series classifiers like PRISM achieve high efficiency with only ~40K parameters and sub-millisecond inference, enabling browser-embedded real-time classification without physiological hardware, and (3) the converging positive evidence from Campagna et al. and Kaneko & Yamada establishes that behavioral trust prediction is achievable with appropriate modeling depth—though whether this generalizes to conversational LLM interactions remains the core empirical hypothesis we test.

## Landscape
Liu et al. (CHI 2026) provide the most comprehensive behavioral characterization of LLM overreliance, identifying five patterns—frequent copy-paste without editing, skipped initial task comprehension, rapid LLM-task alternation, coarse block-pasting vs. fine-grained editing, and hesitation-then-acceptance—via autoencoder clustering of per-event interaction encodings (each event represented as a 37-dimensional vector: 15-dim action type one-hot + 1-dim normalized timestamp + 2-dim page type + 19-dim type-specific attributes) from 77 participants across three tasks with injected misinformation. The 'Adjust for Trust' system (Srinivasan & Thomason, IUI 2026) demonstrates that adapting explanations based on trust level (supporting explanations when trust is low, counter-explanations when high, with enforced reading delays) yields up to 38% reduction in inappropriate reliance and 20% accuracy improvement; however, it relies on self-reported trust on an 11-point scale after every one of 30 decisions per session. Critically, Appendix D documents the authors' failed attempt at replacing self-report with behavioral estimation: simple heuristics (AIAcc5, CapabilityDiff, SmoothOutcomes, SmoothConfs) achieved only 0.25–0.51 correlation and F1 ≤ 0.5, concluding that 'surface-level interaction features' are inadequate for trust modeling. Li et al. ('From Text to Trust,' CHI 2025) use a POMDP framework to adaptively select LLM-generated analyses based on inferred user hidden states, significantly improving accuracy on tabular classification tasks—but their interaction paradigm is structured (sequential agree/disagree on feature-level explanations), their state estimation uses only binary response feedback, and they neither capture behavioral signals nor address free-form conversational LLM use. Ailin Liu et al.'s 'Sensing What Surveys Miss' (CHI 2026, arXiv 2602.00880) is the most architecturally analogous prior work: it builds a closed-loop system where mouse dynamics (vertical direction changes, hover time, hover count) and electrodermal activity (tonic EDA level, EDA peaks) feed personalized linear regression classifiers with rule-based threshold adaptation, triggering LLM-generated clarifications during online surveys. In a within-subjects study (N=32), their aligned-adaptive timing improved survey response accuracy by 21% and reduced false negatives from 50.9% to 22.9%. However, three key differences separate their work from ours: (a) they target cognitive load in knowledge-based survey items, not overreliance on LLM outputs in conversational interaction—fundamentally different constructs requiring different signal vocabularies; (b) they require physiological sensors (EDA wristbands), limiting scalability to any-browser deployment; and (c) their simple linear regression classifiers with max-fusion of two unimodal models achieve only ~61% detection accuracy, and they provide no ablation isolating the contribution of mouse dynamics alone vs. EDA alone—leaving open whether their mouse features would function without the physiological channel. Their finding that even combined mouse+EDA with simple models reaches only 61% accuracy actually reinforces our hypothesis that richer temporal signal processing (multi-resolution CNNs operating on the full behavioral feature space) is needed to compensate for the absence of physiological signals. The evidence landscape for behavioral trust/reliance prediction includes both negative and positive results. On the negative side: Dechant et al. (arXiv 2310.16632, 2023) find that mouse trajectory features alone 'might not explain sufficiently the variance to be used on their own'; Adjust for Trust's Appendix D shows F1 ≤ 0.5 with heuristic behavioral features. On the positive side: Campagna et al. (RA-L 2025, arXiv 2601.19856) achieve 84% trust classification accuracy (Voting Classifier, AUC=0.90, F1=0.84) from seven behavioral indicators—gaze direction, spatial displacement, speed synchronization, reaction time, predictability, and legibility—in a human-robot chemical mixing task (N=14), demonstrating that ensemble classifiers on multi-dimensional behavioral features substantially outperform single-signal approaches, albeit in a physical HRI domain with a small sample; Kaneko & Yamada (IEEE Access, 2025) achieve 90% accuracy predicting over/under-trust using dynamic structural equation modeling on interaction data in drone and driving simulators; and Gurney et al. (Persuasive Technologies, 2023; arXiv 2302.01854) show that behavioral predictors outperform self-report psychometric inventories for predicting AI compliance. This pattern—negative results with simple models on narrow feature sets, positive results with richer models on multi-dimensional behavioral features—is central to our technical hypothesis. Raees & Papangelis ('From Trust to Appropriate Reliance,' arXiv 2604.23896, April 2026) provide important measurement-theoretic context, arguing that trust and appropriate reliance are conceptually distinct constructs: trust reflects subjective perception while reliance concerns observable behavioral decisions. They identify three measurement views (Traditional: over/under-reliance rates; Appropriateness: RAIR/RSR; Dominance: AI influence direction) and recommend behavioral process metrics over subjective ratings—directly supporting our approach of measuring reliance behavior rather than trust attitudes. Sun et al. ('Eyes Can't Always Tell,' arXiv 2604.01741, 2026) demonstrate that eye-tracking-to-cognitive-state mappings shift across AI conditions, arguing for multi-signal, context-dependent approaches. Cognitive forcing functions have been studied extensively: Buçinca et al. (CSCW 2021) showed CFFs reduce overreliance but increase frustration; Ghosh et al. (arXiv 2601.18033, 2026) found Assumption-style CFFs most effective at reducing overreliance without increasing cognitive load. Ibrahim et al. (arXiv 2509.08010, 2025) consolidate measurement gaps and call for process-oriented mitigation. The 'From Calibration to Collaboration' position paper (arXiv 2506.07461, June 2025) argues that current UQ methods are misaligned with real user needs. Key limitation across all works: no system closes the loop from non-invasive behavioral detection to adaptive intervention in free-form conversational LLM interactions. Liu et al. characterize signals but build no real-time system; Adjust for Trust intervenes adaptively but requires intrusive every-decision self-report that their own behavioral estimation attempt failed to replace; From Text to Trust adapts but only in structured tasks with coarse feedback; Sensing What Surveys Miss closes the loop but requires physiological sensors and targets cognitive load in surveys with simple classifiers achieving only 61% accuracy; Campagna et al. predict trust behaviorally in HRI but build no intervention system for conversational AI; and Kaneko & Yamada predict trust in physical cooperative tasks but do not address conversational LLM settings.

## Approach
Build OverrelianceGuard, a browser-extension-based closed-loop system with three components:

(1) INSTRUMENTATION LAYER: A JavaScript layer that unobtrusively captures interaction events in 30-second sliding windows (5-second stride). FEATURE REPRESENTATION CLARIFICATION: Liu et al.'s original 37-dimensional encoding is a per-event representation—each discrete interaction event (click, scroll, keypress, etc.) is encoded as a 37-dimensional vector comprising a 15-dim action type one-hot, 1-dim normalized timestamp, 2-dim page type, and 19-dim type-specific attributes (e.g., mouse movement distance and duration, scroll distance and direction, keypress count). Their transformer autoencoder operates on variable-length sequences of these event vectors per segment. Our CNN requires fixed-size input per window, so we transform Liu et al.'s event sequences into a temporal grid representation: each 30-second window is discretized into T=30 one-second bins, and for each bin we compute K=28 aggregated features from all events occurring within that bin. Specifically, the 28 per-bin features are: (a) action type distribution—proportions over 12 action categories (mouse movement, click, scroll, keypress, copy, paste, highlight, delete, idle, tab switch, prompt input, element switch; 12 features); (b) mouse dynamics—total movement distance and mean velocity (2); (c) scroll dynamics—total distance and direction ratio (up/down; 2); (d) keypress statistics—count and mean inter-key interval (2); (e) copy-paste behavior—copy count, paste count, and post-paste edit indicator (3); (f) idle time—total idle duration within the bin (1); (g) dwell context—time since last LLM response (1); (h) page context—fraction of time on LLM page vs. task page (1); (i) text interaction—highlight text length and delete count (2). This yields a (30 × 28) input tensor per window, where the temporal dimension (30 timesteps) captures within-window behavioral dynamics that the multi-resolution CNN branches process at different scales. Features are z-score normalized per-user via an initial 5-minute calibration phase to account for individual baseline interaction styles.

(2) STREAMING OVERRELIANCE RISK CLASSIFIER: A multi-resolution 1D-CNN inspired by the PRISM architecture (~40K parameters). Three parallel convolutional branches with symmetric FIR filters at different temporal resolutions—2s (kernel size 2, capturing short-burst behaviors like rapid copy-paste), 10s (kernel size 10, capturing medium-term patterns like comprehension scanning), and 30s (kernel size 30, capturing full-window dynamics like engagement trajectory)—operate on the (30 × 28) temporal grid input, feed into per-branch global average pooling, then concatenate into a 2-layer MLP classification head (128→2) outputting an overreliance risk score ∈ [0,1]. This architecture is chosen because: (a) the (30 × 28) input is a moderately-sized temporal grid (not high-dimensional sensor data where ViT/transformers excel), (b) PRISM achieves 97.3% on UCI-HAR with ~40K parameters—we cite this as evidence of architectural efficiency at this parameter scale and sub-millisecond inference capability, not as a performance projection for our task, since UCI-HAR uses 6-axis accelerometer/gyroscope data with 6 well-separated physical activity classes, whereas overreliance classification operates on noisier mouse/keyboard interaction features with subtler class boundaries; (c) 1D-CNNs run in <5ms via ONNX Runtime Web on commodity CPUs; and (d) the Adjust for Trust Appendix D failure with surface-level heuristics and Sensing What Surveys Miss's ~61% accuracy with linear regression on mouse+EDA both suggest that improvement comes from richer temporal feature processing (multi-resolution convolutions capturing dynamics at multiple scales), not larger models or physiological sensors—while Campagna et al.'s 84% accuracy with ensemble classifiers on multi-dimensional behavioral features in HRI confirms that richer modeling on behavioral features can substantially exceed simple-model baselines. We compare against MiniRocket (fixed kernels + linear head, near-zero learnable parameters) and BiLSTM (128 hidden units, ~200K parameters) baselines to isolate the contribution of the multi-resolution architecture.

TRAINING DATA SUFFICIENCY ANALYSIS: Liu et al.'s dataset comprises 77 participants × 3 tasks = 231 sessions. With our proposed 30-second sliding windows at 5-second stride, assuming average task durations of 10–15 minutes (consistent with their protocol), each session yields ~115–175 windows, producing an estimated 26K–40K behavioral windows total. For a 40K-parameter model, this yields a sample-to-parameter ratio of 0.65–1.0:1, which is tight but viable: for comparison, PRISM achieves 97.3% on UCI-HAR with only 7,352 training samples and ~40K parameters (ratio ~0.18:1). Nevertheless, we address overfitting risks through five mitigation strategies: (a) standard time series data augmentation—Gaussian jittering (σ=0.05), window slicing (90% crops), and time warping—which have been shown to substantially improve 1D-CNN accuracy on small behavioral datasets; (b) model regularization via dropout (p=0.3), L2 weight decay (λ=1e-4), and early stopping on a held-out validation set; (c) attention entropy maximization in the MIL pooling layer to prevent attention collapse onto few instances; (d) the weak supervision labeling functions themselves provide soft probabilistic labels that act as implicit label smoothing, reducing overfitting to noisy hard labels; and (e) a phased data strategy leveraging both datasets—train and validate on Liu et al.'s 77-participant data, then fine-tune on a pilot cohort (first ~20 participants of the 120-participant study) and evaluate on the remaining ~100, ensuring the final evaluation is on held-out participants unseen during any training phase. We will report learning curves (accuracy vs. training set fraction) to empirically demonstrate whether ~30K windows are sufficient or whether the model is still data-hungry, and will release the trained model weights and augmentation pipeline for reproducibility.

GROUND TRUTH LABELING STRATEGY: Liu et al.'s overreliance labels are outcome-based—a single per-task label assigned to all behavioral segments regardless of what happened in each specific window. Training a streaming classifier on these temporally misaligned labels would conflate overreliant and non-overreliant moments within the same session. We adopt a hybrid multi-signal labeling approach: (a) OUTCOME PROPAGATION via Multiple Instance Learning: for each accepted misinformation item, trace back to the behavioral window from first exposure through acceptance, treating the session as a 'bag' with the task-level overreliance label, and let an attention-based MIL pooling layer learn which sub-segments are most predictive; (b) WEAK SUPERVISION via programmatic labeling functions encoding Liu et al.'s five behavioral patterns as heuristic rules (e.g., 'copy-paste within 10s of LLM response without scrolling through response → OVERRELIANT'; 'reads task prompt >15s before first LLM query → NOT_OVERRELIANT'; 'pastes LLM content block without subsequent editing → OVERRELIANT'), reconciled via a Snorkel-style generative model into probabilistic training labels; (c) SPARSE METACOGNITIVE PROBES: at 2–3 event-triggered points per task (triggered by detected behavioral state transitions, not fixed intervals), prompt users briefly: 'How carefully are you evaluating the AI's response right now?' (5-point scale)—far less intrusive than Adjust for Trust's 30 every-decision ratings; (d) SELF-SUPERVISED REGULARIZATION: a next-action prediction auxiliary objective captures behavioral dynamics without requiring labels. The classifier is trained with a weighted multi-task loss combining all four signal types, with outcome labels serving as calibration rather than primary supervision.

WEAK SUPERVISION CIRCULARITY ANALYSIS AND ABLATION: We explicitly address the risk that the CNN trained on weak supervision labels may learn to replicate the hand-coded labeling function rules rather than discover deeper temporal patterns—since the labeling functions encode behavioral patterns (e.g., copy-paste frequency, dwell time thresholds) derived from the same interaction features the CNN processes. While the Snorkel literature demonstrates that discriminative end models typically generalize beyond labeling functions (averaging 9.5-point accuracy improvements over the label model alone, as they learn subtle feature combinations and contextual patterns the heuristics miss), this generalization is not guaranteed and must be empirically verified. We design a four-condition ablation to isolate each labeling signal's contribution: (i) WS-ONLY: trained exclusively on weak supervision labels—establishes the upper bound on circularity risk, as the only supervisory signal comes from features the model also takes as input; (ii) MIL+PROBES ONLY: trained on outcome-propagated MIL labels and sparse metacognitive probe labels with NO weak supervision—these labels are derived from task outcomes and self-report respectively, providing supervision entirely independent of the input behavioral features, thereby serving as the circularity-free baseline; (iii) MIL+PROBES+SELF-SUPERVISED: adds the self-supervised next-action prediction objective to condition (ii)—tests whether temporal dynamics learning further improves outcome-based detection; (iv) FULL MULTI-SIGNAL: all four label sources combined. The critical diagnostic comparison is (iv) vs. (ii): if full training substantially outperforms MIL+probes-only training, the weak supervision provides complementary signal beyond what outcome labels alone capture; if (iv) ≈ (i) >> (ii), the model is primarily learning the hand-coded rules (confirming the circularity concern). Additionally, we conduct feature importance analysis using Integrated Gradients attribution on models from each condition, comparing the learned feature importance profiles against the features explicitly encoded in labeling functions. If the full model assigns substantial attribution to features NOT encoded in any labeling function (e.g., temporal velocity patterns, micro-hesitation dynamics, action transition probabilities), this provides positive evidence of generalization beyond the heuristic rules. We will report these ablation results as a primary finding, following the XPASC framework's principle that measuring generalization beyond labeling functions is essential for validating weakly-supervised classifiers.

CONTRIBUTION ROBUSTNESS: WHAT IF DETECTION ACCURACY IS LOW? We explicitly frame streaming behavioral overreliance detection as the core empirical hypothesis being tested, not an assumed capability. The prior evidence is sobering: Adjust for Trust's Appendix D achieves F1 ≤ 0.5 with surface-level behavioral heuristics, Sensing What Surveys Miss reaches only ~61% with linear regression on mouse+EDA, and Dechant et al. find mouse features alone insufficient. Our hypothesis is that multi-resolution temporal processing on richer multi-dimensional behavioral features—following the positive trajectory shown by Campagna et al. (84% in HRI) and Kaneko & Yamada (90% in cooperative tasks)—can substantially improve on these baselines in the LLM conversation domain. However, there exists a realistic scenario where our classifier achieves only 65–70% accuracy—better than prior baselines but potentially insufficient for reliable real-time intervention. We explicitly plan for this contingency: (1) The within-subjects comparison of four intervention conditions (no intervention, static CFF, self-report-adaptive, behaviorally-triggered adaptive) constitutes a valuable empirical contribution REGARDLESS of detection accuracy—it provides the first head-to-head comparison of these paradigms in free-form LLM conversations, with the self-report-adaptive condition serving as an upper-bound benchmark for behavior-triggered approaches. Even a moderate-accuracy classifier may outperform static interventions by reducing alert fatigue and targeting interventions to riskier moments. (2) The hybrid labeling methodology (MIL + weak supervision + sparse probes + self-supervised regularization) is an independent methodological contribution applicable to any streaming behavioral classification task with outcome-level labels, publishable as a methods contribution for the temporal action localization community. (3) Characterizing WHAT behavioral signals can and cannot predict about overreliance—via the four-condition ablation, feature importance analysis, and learning curves—is itself an informative contribution that advances the field's understanding of the behavioral-detection frontier, directly addressing the open question left by Adjust for Trust's Appendix D. (4) The instrumentation layer and temporal grid feature engineering for LLM conversation interactions provides reusable infrastructure for future research. We will report detection accuracy honestly and frame negative or moderate results as informative findings about the boundaries of behavioral sensing for reliance calibration, following Raees & Papangelis's (2026) call for rigorous behavioral measurement of appropriate reliance.

(3) TIERED ADAPTIVE INTERVENTION ENGINE: When the streaming risk score exceeds personalized thresholds (calibrated from the 5-minute baseline), the system selects from escalating interventions: (Tier 1, risk 0.5–0.7) a lightweight Assumption-style metacognitive prompt ('What might be wrong with this answer?') shown as a non-blocking tooltip; (Tier 2, risk 0.7–0.9) a counter-explanation surfacing potential errors in the LLM's response, modeled on Adjust for Trust's strategy, with a 10-second reading delay; (Tier 3, risk >0.9) a comprehension checkpoint requiring the user to identify one potential issue before proceeding. A cooldown mechanism (minimum 2 minutes between interventions) prevents alert fatigue.

ECOLOGICAL VALIDITY CONSIDERATIONS: We acknowledge that our evaluation paradigm—researcher-injected misinformation in controlled tasks—follows the standard methodology employed by both Liu et al. (CHI 2026) and Adjust for Trust (IUI 2026), but has inherent ecological validity limitations. Injected misinformation is typically more blatant, consistently placed, and fact-checkable compared to natural LLM hallucinations, which are subtler, context-dependent, and may involve plausible-sounding but unverifiable claims. As Ren et al. (arXiv 2510.10539) demonstrate with their AuthenHallu benchmark, hallucinations in authentic LLM-human interactions differ qualitatively from artificially constructed errors, occurring in 31.4% of real query-response pairs with highly variable subtlety. Our controlled design is necessary for establishing internal validity—it enables precise measurement of overreliance rates and intervention effects with known ground truth—but a classifier trained solely on controlled-misinformation tasks may not fully generalize to naturalistic LLM use where the 'correct' level of reliance is ambiguous. We address this in two ways: (1) Liu et al.'s misinformation includes varied subtlety levels (hallucinations, outdated knowledge, prompt injection attacks) that partially approximate natural error diversity, and (2) we plan a follow-up naturalistic deployment study where participants use the system during their regular LLM interactions over 2 weeks, with overreliance assessed via retrospective expert review of interaction logs—a design explicitly motivated by ecological validity concerns.

EVALUATION: A within-subjects study (N≈120) across four LLM-assisted decision tasks with injected misinformation (quiz/ranking, article summarization, trip planning, code review), counterbalanced via Latin square across four conditions: (a) no intervention (control), (b) static cognitive forcing (always-on Assumption-CFF per Ghosh et al.), (c) self-report-adaptive (replicating Adjust for Trust's 11-point scale + counter-explanations), and (d) behaviorally-triggered adaptive (OverrelianceGuard). Each participant completes four tasks (~75 min total), one per condition. Primary metrics: overreliance reduction rate (misinformation acceptance, measured via both Traditional over-reliance rate and Appropriateness-view RAIR/RSR metrics per Raees & Papangelis's framework), task accuracy, detection latency (time from overreliance onset to intervention trigger), intervention precision/recall (validated against outcome and metacognitive probe labels), user satisfaction (NASA-TLX + custom intrusiveness scale), and comparative survey interruption burden between conditions (c) and (d). Secondary analysis: per-user classifier calibration curves, learning curves showing accuracy vs. training data fraction, four-condition weak supervision ablation with feature importance analysis, and qualitative analysis of intervention-triggered behavioral shifts.

## Resource Estimate
{'manual': {'gpu_hours': '80', 'timeline': '7-9 months (2 months system dev + labeling pipeline, 1 month IRB + pilot, 2-3 months main study with 120 participants, 2-3 months analysis and writing)', 'estimated_gpu_cost': '$120 (A100 at ~$1.50/hr spot pricing; model is only ~40K params so training is fast; GPU time dominated by hyperparameter search, data augmentation pipeline, Snorkel label model training, and 4-condition ablation)'}, 'human_in_loop': {'gpu_hours': '60', 'timeline': '5-7 months (Claude accelerates extension code, labeling function design, ONNX export pipeline, and statistical analysis)', 'claude_api_cost': '$250 (Sonnet 4.6 for code generation, weak supervision labeling function refinement, intervention prompt engineering, and analysis scripts; ~80M tokens)', 'estimated_gpu_cost': '$90 (A100 at ~$1.50/hr spot pricing)'}, 'auto_research': {'gpu_hours': '50', 'timeline': '4-6 months (automated architecture search across CNN/MiniRocket/LSTM variants, labeling function optimization, and ablation analysis; human study remains irreducible)', 'claude_api_cost': '$500 (Sonnet 4.6 for automated pipeline: architecture comparison, labeling function generation and evaluation, intervention prompt tuning via batch API, paper drafting; ~160M tokens)', 'estimated_gpu_cost': '$75 (A100 at ~$1.50/hr spot pricing)', 'speed_bottleneck': 'IRB approval (4-8 weeks) and sequential participant recruitment for within-subjects study are irreducible human-in-the-loop requirements that cannot be parallelized by automation'}}

## Inspired By
Untried combination: rich behavioral interaction signals from Liu et al. (CHI 2026) + trust-adaptive intervention strategies from 'Adjust for Trust' (IUI 2026), without the physiological sensor requirement of 'Sensing What Surveys Miss' (CHI 2026). Gap validation: Adjust for Trust's Appendix D documents that surface-level behavioral features fail to predict trust (F1 ≤ 0.5), and Sensing What Surveys Miss achieves only ~61% accuracy even with combined mouse+EDA using linear regression—both motivating richer multi-resolution temporal processing via deep learning. Positive evidence from Campagna et al. (84% trust classification in HRI) and Kaneko & Yamada (90% in cooperative tasks) establishes that the failure is in modeling depth, not in behavioral signals per se—justifying our investment in multi-resolution temporal architectures. Measurement-theoretic insight from Raees & Papangelis (2026): appropriate reliance is behaviorally observable and conceptually distinct from trust, grounding our choice to detect reliance behavior rather than infer trust attitudes. Cross-paradigm transfer: extending Li et al.'s adaptive explanation selection principle from structured tabular tasks with coarse feedback to free-form conversational LLM interactions with continuous behavioral sensing. Architecture insight: lightweight time series classifiers (PRISM, ~40K params) demonstrate that efficient sub-millisecond browser-embedded inference is feasible at this parameter scale, making sensor-free any-browser deployment practical where prior approaches (Sensing What Surveys Miss) assumed physiological hardware. Labeling methodology: adapting the hybrid weak-supervision + outcome-propagation approach from fraud detection and temporal action localization, informed by TimeMIL's time-aware MIL pooling for temporal sequence data, to solve the streaming-vs-outcome temporal misalignment problem that Liu et al.'s post-hoc analysis did not address—with explicit ablation design to verify the classifier generalizes beyond hand-coded labeling function rules, informed by the XPASC framework for measuring weak supervision generalization.

## Target Venues
- CHI 2027 (paper deadline: September 10, 2026) — top-tier HCI, ideal fit for closed-loop behavioral+intervention system contribution with within-subjects evaluation
- IUI 2027 (paper deadline: August 20, 2026) — natural successor venue to the Adjust-for-Trust IUI 2026 paper; strong fit for adaptive UI contribution
- CSCW 2027 (rolling submissions, fully open 2027) — strong fit for collaborative human-AI reliance calibration framing and the labeling methodology contribution
- IMWUT / UbiComp (next deadline: November 1, 2026) — fits if emphasizing ubiquitous non-invasive sensing of interaction behavior
- AAAI 2027 (paper deadline: July 28, 2026) — if framing emphasizes the hybrid labeling methodology and streaming classification contribution

## Key References
- Liu, Zhou, Shen, Liu, Wu & Chen. Behavioral Indicators of Overreliance During Interaction with Conversational Language Models (CHI 2026, arXiv 2602.11567)
- Srinivasan & Thomason. Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (IUI 2026, arXiv 2502.13321)
- Li, Zhu, Lu, Xiao & Yin. From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis (CHI 2025, arXiv 2502.11919)
- Ailin Liu, Karoui, Draxler, Kreuter & Chiossi. Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM Support by User Modeling (CHI 2026, arXiv 2602.00880)
- Kaneko & Yamada. Predicting Trust Dynamics with Dynamic SEM in Human-AI Cooperation (IEEE Access 2025, arXiv 2407.01752)
- Campagna, Lagomarsino, Lorenzini, Chrysostomou, Rehm & Ajoudani. Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability (RA-L 2025, arXiv 2601.19856)
- Raees & Papangelis. From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making (arXiv 2604.23896, April 2026)
- Gurney, Pynadath & Wang. Comparing Psychometric and Behavioral Predictors of Compliance During Human-AI Interactions (Persuasive Technologies 2023, arXiv 2302.01854)
- Sun et al. Eyes Can't Always Tell: Fusing Eye Tracking and User Priors for User Modeling under AI Advice Conditions (arXiv 2604.01741, 2026)
- Ibrahim et al. Measuring and Mitigating Overreliance Is Necessary for Building Human-Compatible AI (arXiv 2509.08010, 2025)
- Buçinca, Malaya & Gajos. To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making (CSCW 2021)
- Ghosh et al. An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, 2026)
- PRISM: Multi-Resolution Time Series Classification via Symmetric Dilated Convolutions (Neurocomputing 2026, arXiv 2508.04503)
- From Calibration to Collaboration: LLM Uncertainty Quantification Should Be More Human-Centered (arXiv 2506.07461, June 2025)
- de Jong et al. Cognitive Forcing for Better Decision-Making: Reducing Overreliance on AI Systems Through Partial Explanations (CSCW 2025)
- Ren, Gruhlke & Lauscher. Detecting Hallucinations in Authentic LLM-Human Interactions (arXiv 2510.10539, 2025)
- Dechant, Shukla & Bhatt. Mice, Masks, and Monotones: On the Reliability of Mouse Trajectories as Indicators of Trust (arXiv 2310.16632, 2023)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3efd72c6-2389-4763-8875-41bd3ede279d",
  "type": "user",
  "uuid": "5e5dd3fd-7ebd-40f1-b98d-8a8d75c38159",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:38:36.015Z_

```json
{
  "parentUuid": "5e5dd3fd-7ebd-40f1-b98d-8a8d75c38159",
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
  "uuid": "d112c966-3d07-4589-9017-88256f564d17",
  "timestamp": "2026-05-20T03:38:36.015Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:38:36.015Z_

```json
{
  "parentUuid": "d112c966-3d07-4589-9017-88256f564d17",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "42a9d285-d814-43a3-98d1-c8cd353f07c3",
  "timestamp": "2026-05-20T03:38:36.015Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient field context. Let me compile my evaluat…",
  "leafUuid": "42a9d285-d814-43a3-98d1-c8cd353f07c3",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Behavioral detection system for LLM overreliance",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:39:02.252Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three reviewers' evaluations and synthesize them as a Meta Judge.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [25% - 40%] 中位 30%
- Venue: CoRL is fatal mismatch, evaluated for CHI/IUI

**Reviewer 2:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强


- Probability: [22% - 35%] 中位 28%
- Venue: CoRL is fatal mismatch, evaluated for CHI/IUI

**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability (CHI/IUI): [25% - 40%] 中位 32%
- Probability (CoRL): [1% - 5%] 中位 2%
- Venue: CoRL is fatal mismatch

All three reviewers converge on the same assessment across novelty, significance, and related work. Looking at the acceptance probabilities for CHI/IUI, the medians cluster around 30%, with a mean of 30% and median of 30%.

The standard deviation is quite low at about 1.63%, indicating strong consistency among reviewers. There's clear consensus that CoRL is fundamentally misaligned with this work, and the core concerns are consistent: the behavioral signals may lack sufficient information at the window level, the contribution is more about systems integration than methodological innovation, and there's a trivial alternative threat from rule-based approaches.

A few dimensions stand out as unique observations—R3's detailed analysis of the 83% window overlap inflating effective samples, R2's framing around event-triggered versus random timing alternatives, and R1's specific "seesaw" concern about the CNN performing similarly to hand-coded rules in ablations—but these don't substantially change the overall assessment.

Looking at the probability estimates, the three medians cluster tightly around 28-32% with minimal variance, and their ranges overlap substantially in the [25-35] band. Given this consistency, I'm settling on a narrow interval centered at the median: [24%-35%] with 30% as the midpoint for CHI/IUI. For CoRL, the reviewers align that acceptance is essentially unlikely.

Now I need to pull together the implementation assessment using the resource estimates from the proposal and the feedback provided by reviewers, then format everything according to the guidelines without code fences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42a9d285-d814-43a3-98d1-c8cd353f07c3",
  "isSidechain": false,
  "requestId": "req_011CbD8AGp7JG4HaazHvKQ2x",
  "type": "assistant",
  "uuid": "2361b506-8267-4bb7-8a1e-97c18682faa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6TTKvqdt7JfoArYZnJcej",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24881,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3971,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 24881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24881
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

_source line 9 · 2026-05-20T03:40:13.830Z_

【阶段】: Meta Judge
【三次中位】: [30%, 28%, 32%] std=1.63%
【共识维度】:
- **Novelty: 中** — 3/3 一致。核心贡献是系统集成（Liu et al. 信号词汇 + Adjust for Trust 干预策略 + PRISM 架构 + Snorkel/MIL 标注），非方法论突破。每个组件都有明确的现有先例。
- **Significance: 中偏强** — 3/3 一致。问题本身重要且时效性强（LLM 过度依赖是 2025-2026 HCI 热点），sensor-free browser-based 方案若有效则实用价值高；但核心发现无论正负都缺乏 surprise factor。
- **Related Work: 强** — 3/3 一致。引用全面准确，差异化定位清晰，对负面证据（Adjust for Trust Appendix D、Dechant 2023）的处理诚实。这是 proposal 最突出的维度。
- **CoRL venue 致命不匹配** — 3/3 一致且措辞极为强烈。纯 HCI 工作，无任何机器人学习组件，投 CoRL 大概率 desk reject。
- **核心经验性假设薄弱** — 3/3 一致。30 秒窗口粒度内行为信号能否区分过度依赖状态是整个系统的根基，但同领域证据偏负面（F1 ≤ 0.5, ~61% with EDA），正面证据来自 domain gap 很大的物理 HRI。
- **Trivial alternative 威胁真实** — 3/3 一致。静态 CFF、规则阈值触发、事件触发干预均为更简单的替代方案，如果 CNN 增量不显著则核心技术贡献缩水。
- **"If positive, not surprising" 风险** — 3/3 一致。CNN > heuristic 符合一般直觉；如果 negative 则与已有负面证据一致。两种结果都缺少 surprising finding。
- **Dual-outcome framing 的双刃剑** — 3/3 一致。作为风险管理合理，但暴露了作者对核心 claim 信心不足，characterization study 的 impact 低于 working system。
- **Domain gap 问题** — 3/3 一致。Campagna (84%, N=14, 物理 HRI) 和 Kaneko (90%, 驾驶模拟器) 作为正面证据的说服力因 domain gap 被严重削弱。
- **MIL session→window 标签传播假设强** — 2/3 明确提出（R1, R2）。如果"过度依赖" session 中大部分 windows 行为正常，MIL attention 难以收敛。

【异常维度】:
- R3 详细指出 30 秒窗口 5 秒步长导致 83% 重叠，有效独立样本远小于 26K-40K，sample-to-parameter ratio 被严重高估 → 这是一个有效的技术洞察，但仅 R3 深入展开。因为其论证逻辑清晰且有数学依据，**不应降权**，应视为 R1/R2 未充分展开但隐含认可的风险。
- R2 特别提到 "随机但频率匹配的干预" 作为 trivial alternative → 其他两位提到了类似的 static/event-triggered alternatives，此条是变体，不算真正的 outlier。

【最终概率】: [24% - 35%] 中位 30%

**注：此概率严格基于 CHI/IUI/CSCW 等 HCI 顶会评估。若投 CoRL 2026，概率 ≈ 0-3%（desk reject），三位审稿人对此完全一致。**

【一致性】: 高（std=1.63%，三维度判决完全一致，概率区间高度重叠）

【综合理由】:

三位审稿人的评估高度收敛，在所有三个 rubric 维度上判决完全一致（Novelty 中 / Significance 中偏强 / Related Work 强），概率中位分布在 28-32% 的极窄区间内。这种收敛程度意味着评估的可靠性较高。

**概率锚定逻辑**：
1. **Related Work 强** 保住了概率下界——proposal 的 gap identification 准确、差异化定位清晰、对负面证据处理诚实，不至于被审稿人因 related work 不足而直接击穿。下界 24%。
2. **Novelty 中** 严格限制了概率上界——系统集成型贡献在竞争激烈的 CHI/IUI 中需要靠 impressive empirical results 来补偿 novelty 不足，而核心经验性假设的先验证据偏负面。上界 35%（即使实验执行完美，方法论 novelty 不足以支撑更高概率）。
3. **Significance 中偏强** 使中位数维持在 30% 而非更低——问题重要性和实用潜力为 proposal 提供了一定的"价值底座"，但 surprise factor 不够强，无法将概率推过 35% 天花板。
4. **R3 的窗口重叠问题** 是一个被低估但有效的技术风险——虽然仅 R3 深入展开，但其逻辑成立（83% 重叠导致有效独立样本远小于声称的 26K-40K），这进一步加深了核心检测性能的不确定性，但不足以独立拉低概率（已被"核心假设薄弱"这一共识风险所涵盖）。

**处理原则**：三方高度一致，取中位 30%，区间 [24%-35%] 略窄于三方区间的并集（[22%-40%]），反映了高一致性下的信心收敛。偏向 R2（最严格）的下界但不完全采纳其 22%，因为 R1 和 R3 在 [25%-40%] 上高度一致。

【建议】: 边缘（针对 CHI/IUI venue）/ 如投 CoRL 则 KILL

**具体建议**：
- **立即更正 venue**：CoRL 2026 是致命的 venue 选择错误，三位审稿人一致认定 desk reject 风险极高。应回到 proposal 自身列出的目标 venue（CHI 2027 / IUI 2027 / CSCW 2027）。
- **针对 CHI/IUI**：idea 处于 borderline 区间。Related Work 是明确的加分项；核心瓶颈是 Novelty（系统集成型）和核心经验性假设的不确定性。如果能在以下方向强化，有提升空间：(a) 锐化方法论 novelty（混合标注策略需要被 pitch 为更独立的方法论贡献，而非防御性 ablation），(b) 降低对"检测一定 work"的依赖（dual-outcome 已有但需更主动地将 characterization 贡献前置），(c) 正视并更诚实地 discount 跨领域正面证据的说服力。

【实施评估】:
- **计算资源**: 极低。~40K 参数模型，50-80 GPU 小时（A100），估计 $75-$120。GPU 时间主要用于超参搜索、数据增强、Snorkel 标签模型训练和 4-condition ablation，非模型训练本身。浏览器端推理 <5ms（ONNX Runtime Web），无需持续 GPU 部署。
- **数据需求**: 核心依赖 Liu et al. (CHI 2026) 的 77 参与者数据集（需确认公开可得性）+ 自行招募 N≈120 的 within-subjects study 数据。如 Liu et al. 数据集未公开发布，则需自行复现数据收集，显著增加周期和成本。
- **人工介入**: **高，这是主要瓶颈**。(a) IRB 审批 4-8 周不可压缩；(b) 招募 120 名参与者进行 ~75 分钟 within-subjects study，按 $15-20/人计约 $1,800-2,400 被试费；(c) 弱监督标注函数需要领域专家设计和验证；(d) 可选的后续自然部署研究需要额外 2 周参与者跟踪。
- **训练需求**: 需要训练，但规模极小。40K 参数 CNN + MIL attention 层 + Snorkel 生成模型，训练时间以小时计非天计。主要挑战不在计算而在数据质量和标签策略的有效性。
- **新 Benchmark**: 不需要构建传统意义上的新 benchmark，但需要构建：(a) 浏览器行为事件的 temporal grid 表征管道，(b) 4-condition ablation 的完整评估框架，(c) 干预效果的多维度评估体系（Traditional + Appropriateness-view metrics）。这些构成可复用的评估基础设施。
- **预估周期**: **7-9 个月**（2 个月系统开发 + 标注管道，1 个月 IRB + pilot，2-3 个月主实验 120 参与者，2-3 个月分析写作）。**不可压缩瓶颈**：IRB 审批和顺序参与者招募。如果目标 CHI 2027（deadline 2026 年 9 月），从现在（2026 年 5 月）算起时间极为紧张，几乎不可行；IUI 2027（deadline 约 2026 年 8 月）更紧张。CSCW 2027（rolling submissions）或 IMWUT（2026 年 11 月 deadline）更现实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2361b506-8267-4bb7-8a1e-97c18682faa1",
  "isSidechain": false,
  "requestId": "req_011CbD8AGp7JG4HaazHvKQ2x",
  "type": "assistant",
  "uuid": "6b344b78-7226-4ef6-bd1d-dccde661bc69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6TTKvqdt7JfoArYZnJcej",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24881,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3971,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 24881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24881
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient field context. Let me compile my evaluat…",
  "leafUuid": "6b344b78-7226-4ef6-bd1d-dccde661bc69",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Behavioral detection system for LLM overreliance",
  "sessionId": "1e56692f-e883-4f9b-9710-09e3dca40b3e"
}
```

---
