# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/397ca181-ea6c-4d96-a7f9-15df35237ee7.jsonl`
- **Structured JSON:** [`0738193968ec89684a14.json`](../../sessions/07/0738193968ec89684a14.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:47:22.210Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:47:22.210Z",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have comprehensive field research results. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【致命问题：投稿会议与 proposal 方向完全不匹配】\n\n在评估 idea 质量之前，必须首先指出一个致命的结构性问题：\n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：\n\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 是一篇纯粹的 HCI (Human-Computer Interaction) 论文——关于在浏览器中通过行为信号检测用户对 LLM 的过度依赖并触发自适应干预。它不涉及任何机器人学习、机器人感知、机器人控制或机器人系统。所有引用的核心相关工作（Liu et al., Adjust for Trust, Sensing What Surveys Miss 等）均发表于 CHI 和 IUI 这类 HCI 会议。\n\n这意味着该 proposal 投稿 CoRL 2026 会被 desk reject（不送审直接退回）。以下我仍按要求评估 idea 本身的质量，但概率估计必须反映这一致命的 venue mismatch。\n\n---\n\n【领域调研】:\n\n- [Liu et al., \"Behavioral Indicators of Overreliance During Interaction with Conversational Language Models\"](https://arxiv.org/abs/2602.11567) (CHI 2026): 确认存在。77 名参与者、3 项任务，通过 autoencoder 聚类识别出 5 种过度依赖行为模式。使用 per-event 37 维编码。明确将实时检测和干预留作 future work。这是本 proposal 的直接上游工作。\n\n- [Srinivasan & Thomason, \"Adjust for Trust\"](https://arxiv.org/abs/2502.13321) (IUI 2026): 确认存在。通过信任自适应干预（支持性/反面解释 + 强制暂停）实现最高 38% 不当依赖减少。但依赖每次决策后的 11 点量表自我报告。Appendix D 记录了行为信号替代自我报告的失败尝试（F1 ≤ 0.5）。\n\n- [Ailin Liu et al., \"Sensing What Surveys Miss\"](https://arxiv.org/abs/2602.00880) (CHI 2026): 确认存在。使用鼠标动态 + EDA（电皮肤活动）构建闭环系统。N=32 的 within-subjects 研究，对齐自适应时机提高 21% 准确率。但需要生理传感器，且简单线性回归仅达 ~61% 检测准确率。\n\n- [Campagna et al., \"Estimating Trust in Human-Robot Collaboration\"](https://arxiv.org/abs/2601.19856) (RA-L 2025): 确认存在。N=14，化学混合任务，Voting Classifier 达 84% 信任分类准确率（AUC=0.90）。但这是物理 HRI 场景，样本极小，行为指标包含凝视方向、空间位移等 LLM 对话中不存在的信号。\n\n- [Raees & Papangelis, \"From Trust to Appropriate Reliance\"](https://arxiv.org/abs/2604.23896) (arXiv, April 2026): 确认存在。区分信任（主观感知）与适当依赖（可观察行为决策），提出三种测量视角（Traditional, Appropriateness, Dominance）。为行为度量而非主观评分提供理论支撑。\n\n- 调研总结: 该领域（LLM 过度依赖的行为检测与自适应干预）目前处于 CHI/IUI 生态圈的早期阶段。Liu et al. (CHI 2026) 刚建立了行为信号词汇表，Adjust for Trust (IUI 2026) 证明了自适应干预的有效性但依赖自我报告，Sensing What Surveys Miss (CHI 2026) 尝试了闭环但需要生理传感器。本 proposal 试图填补\"纯行为信号 → 实时检测 → 自适应干预\"的空白。**这是 HCI 领域的工作，与 CoRL 的机器人学习主题无交集。**\n\n---\n\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁：\n\n1. **规则引擎 baseline**: Liu et al. 已经识别了 5 种过度依赖行为模式。最简单的替代方案是直接将这 5 个模式编码为规则（如 \"10 秒内 copy-paste 且未滚动浏览 → 高风险\"），用阈值触发干预。Proposal 的 weak supervision labeling functions 本质上就是这些规则——那么 CNN 相对于直接使用这些规则作为触发器的增量价值是什么？Proposal 自己也意识到了这个 circularity 问题，设计了 4-condition ablation，但这恰恰说明了 trivial alternative 的威胁是真实的。\n\n2. **简单 ML baseline**: 在同样的 (30×28) 特征上跑 Random Forest 或 XGBoost，不需要 CNN 的时序建模能力，可能已经足够。Proposal 只对比了 MiniRocket 和 BiLSTM，没有包含非时序 ML baseline。\n\n增量价值声称在于\"多分辨率时序处理能捕捉简单模型遗漏的时序动态\"，但这是一个未经验证的假设，而非已知事实。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中存在多个未经验证的关键假设：\n\n1. **\"行为信号在 LLM 对话场景中足以区分过度依赖 vs 适当依赖\"** — 这是最核心也最脆弱的假设。Adjust for Trust 的 Appendix D 直接否定了这一点（F1 ≤ 0.5）。Proposal 辩称那是\"surface-level heuristics\"的失败，更丰富的时序建模会更好——但支撑这一论点的正面证据（Campagna 84%, Kaneko 90%）来自完全不同的领域（物理 HRI、无人机/驾驶模拟），涉及不同的行为信号（凝视方向、空间位移、速度同步）。**从 HRI 到 LLM 对话的 domain gap 巨大，迁移论证薄弱。**\n\n2. **\"30 秒窗口的 28 维聚合特征保留了足够的过度依赖判别信息\"** — Liu et al. 的原始编码是 per-event 的 37 维向量序列，通过 transformer autoencoder 处理。将其聚合为每秒 28 维的 temporal grid 必然丢失信息（尤其是事件间的顺序和依赖关系）。这一表征选择的合理性未被论证。\n\n3. **\"hybrid labeling 能产生足够高质量的训练信号\"** — 四种标注信号（MIL outcome propagation、weak supervision、sparse probes、self-supervised）各有局限：MIL 将 session-level 标签传播到 window-level 是强假设；weak supervision 存在 circularity 风险（proposal 已承认）；sparse probes 每任务仅 2-3 次，信号极度稀疏。这些信号组合后能否收敛到有用的训练信号，是一个 open question。\n\n4. **\"~30K 训练窗口足够训练 40K 参数的 CNN\"** — Proposal 用 PRISM 在 UCI-HAR 上 7,352 样本的先例来论证，但 UCI-HAR 是 6 类清晰分离的物理活动（走路、坐下等），与过度依赖这种微妙行为模式的区分难度完全不在一个量级。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中偏弱** — \n   核心贡献是将 Liu et al. (CHI 2026) 的行为信号 + Adjust for Trust (IUI 2026) 的自适应干预 + Sensing What Surveys Miss (CHI 2026) 的闭环架构组合在一起，去掉生理传感器依赖。这是典型的\"组合创新 + 移除约束\"模式——每个组件都有直接前驱。真正有增量的部分是 hybrid labeling methodology（MIL + weak supervision + probes + self-supervised），但这是方法论层面的贡献，不是核心洞察层面的创新。如果核心检测结果是 positive（比如达到 80% 准确率），审稿人的反应更可能是 \"good engineering, expected given the signal richness\" 而非 \"surprising\"。labeling methodology 的 circularity ablation 设计值得肯定，但它是对自身方法论弱点的防御，不是创新本身。\n\n2. **Significance: 弱（对 CoRL）/ 中（对 HCI 社区）** — \n   对 CoRL 而言：零 significance，没有任何 robotics relevance。\n   如果评估其在 HCI 社区的 significance：问题本身（LLM 过度依赖的实时检测与干预）确实重要且 timely，尤其是 Liu et al. 和 Adjust for Trust 的发表证明了社区关注度。但 proposal 的 contribution 高度依赖于实证结果——如果检测准确率停留在 65-70%，其实际部署价值有限。Proposal 试图通过 \"dual-outcome\" 框架（即使检测不好也有方法论贡献）来对冲风险，但这降低了 single-paper impact：如果主要 claim 不成立，剩余贡献分散且单独来看 incremental。\n\n3. **Related Work: 强** — \n   对相关文献的覆盖非常全面且准确。所有引用的关键论文经调研确认存在，描述准确。差异化定位清晰：与 Liu et al.（有信号但无系统）、Adjust for Trust（有干预但依赖自我报告）、Sensing What Surveys Miss（有闭环但需生理传感器）的区分到位。对负面证据（Dechant et al., Adjust for Trust Appendix D）的诚实引用值得肯定。唯一的问题是正面跨领域证据（Campagna, Kaneko）的 domain gap 论证不够审慎。\n\n---\n\n【概率估计】: [0% - 3%] 中位 1%\n\n【估计理由】: \n概率估计几乎完全由 venue mismatch 决定。CoRL 2026 明确声明 \"submissions without a robotics focus will be returned without review\"。本 proposal 是一篇纯 HCI 论文（浏览器扩展、鼠标/键盘行为信号、LLM 对话场景），不涉及任何机器人学习内容。它几乎必然在 desk review 阶段被退回，不会进入同行评审流程。\n\n如果抛开 venue mismatch，仅评估 idea 在合适 venue（如 CHI 2027, IUI 2027, CSCW 2027）的质量：idea 处于 [20%-30%] 中位 25% 的区间。Novelty 是组合式的而非根本性的，核心经验假设（纯行为信号能否可靠检测 LLM 对话中的过度依赖）存在较大不确定性，且有 trivial alternative 威胁。但问题重要、related work 扎实、研究设计合理（dual-outcome 框架、circularity ablation）。\n\n限制上界的维度：（1）venue mismatch 直接将 CoRL 概率压到接近 0；（2）即使对于 HCI venue，Novelty 的组合性质和核心假设的不确定性限制了上界。\n\n【主要风险】:\n1. **致命 venue mismatch**: CoRL 是机器人学习会议，本 proposal 完全不涉及 robotics，几乎必然 desk reject。\n2. **核心经验假设缺乏支撑**: 从行为信号可靠检测 LLM 对话中过度依赖的假设，唯一直接相关的证据（Adjust for Trust Appendix D）是负面的（F1 ≤ 0.5），而正面证据来自 domain gap 巨大的其他领域（HRI、驾驶模拟）。\n```\n\n---\n\n**强烈建议**：该 proposal 应转投 HCI 相关会议（CHI 2027、IUI 2027、CSCW 2027 或 UIST 2027），而非 CoRL。CoRL 投稿几乎必然导致 desk rejection，浪费宝贵的投稿机会。\n\nSources:\n- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Liu et al., Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)\n- [Srinivasan & Thomason, Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Ailin Liu et al., Sensing What Surveys Miss (CHI 2026)](https://arxiv.org/abs/2602.00880)\n- [Campagna et al., Estimating Trust in HRI (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Raees & Papangelis, From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)\n- [CoRL 2026 - Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to complete the evaluation. Let me note a critical finding from my CoRL search and compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【致命问题：投稿场地根本性错配】\n\n在进入 3 维度评分之前，必须首先指出一个致命的场地错配问题：\n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：\n\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots, and **submissions without a robotics focus will be returned without review**.\"\n\n本 proposal 的内容——浏览器扩展、LLM 对话中的行为过度依赖检测、自适应干预——与机器人学习完全无关。没有任何机器人硬件、控制策略、感知-执行循环、仿真到真实迁移、或机器人学习算法。这是一篇纯 HCI (人机交互) 论文，适合的投稿场地是 CHI、IUI、CSCW、UIST 或 FAccT 等会议。\n\n**投稿 CoRL 将被 desk reject（未送审退回），中稿概率为 0%。**\n\n以下评估假设 proposal 投稿到合适的 HCI 顶会（如 CHI 2027），以便提供有建设性的反馈。\n\n---\n\n【领域调研】:\n\n- [Liu et al., \"Behavioral Indicators of Overreliance During Interaction with Conversational Language Models\"](https://arxiv.org/abs/2602.11567) (CHI 2026): 确认存在。77 名参与者、3 个任务、autoencoder 聚类识别了 5 种行为模式。是本 proposal 的核心数据/信号来源。论文明确将\"实时检测与干预\"列为 future work。\n\n- [Srinivasan & Thomason, \"Adjust for Trust\"](https://arxiv.org/abs/2502.13321) (IUI 2026): 确认存在。信任自适应干预，up to 38% 不当依赖减少，但依赖每次决策后的 11 点量表自报告。Appendix D 确认行为特征预测信任失败 (F1 ≤ 0.5)。\n\n- [Ailin Liu et al., \"Sensing What Surveys Miss\"](https://dl.acm.org/doi/full/10.1145/3772318.3791191) (CHI 2026): 确认存在。鼠标动态 + EDA 闭环系统用于在线问卷，~61% 检测准确率，线性回归分类器。最接近的架构先驱，但目标是认知负荷而非过度依赖，且需要生理传感器。\n\n- [Campagna et al., \"Estimating Trust in Human-Robot Collaboration\"](https://arxiv.org/abs/2601.19856) (RA-L 2025): 确认存在。84% 信任分类准确率 (AUC=0.90)，但是在物理 HRI 领域 (化学混合任务)，N=14，行为指标包括凝视方向、空间位移等——与浏览器交互信号存在巨大领域鸿沟。\n\n- [Raees & Papangelis, \"From Trust to Appropriate Reliance\"](https://arxiv.org/abs/2604.23896) (2026): 确认存在。测量理论框架，区分信任与适当依赖，建议行为过程指标。\n\n- [PRISM](https://arxiv.org/abs/2508.04503) (Neurocomputing 2026): 确认存在。轻量级多分辨率时间序列分类器，~40K 参数。在 UCI-HAR 上达到 97.3%，但 UCI-HAR 的 6 类物理活动分类与过度依赖检测的难度差距巨大。\n\n- **调研总结**: 该领域处于一个明确的\"gap\"阶段：Liu et al. (CHI 2026) 刚刚建立了行为信号词汇表但未做实时系统；Adjust for Trust (IUI 2026) 证明了自适应干预有效但被自报告锁定；Sensing What Surveys Miss (CHI 2026) 建了闭环但需生理传感器且准确率低。本 proposal 定位在这个交叉点上，gap 是真实存在的。但是，**这个 gap 在 2026 年上半年已被多篇 CHI/IUI 论文从不同角度逼近**，竞争窗口正在快速关闭。\n\n---\n\n【Trivial Alternative 检验】:\n\n存在一个明显的 trivial alternative 威胁：**基于规则的阈值系统**。\n\nLiu et al. 已经识别了 5 种行为模式（快速复制粘贴无编辑、跳过初始理解、频繁 LLM-任务切换等）。直接将这些模式编码为 if-then 规则（正是 proposal 自己在 weak supervision 标注函数中做的事），配合简单的滑动窗口统计，就能构建一个 rule-based 干预触发器——不需要 CNN、不需要 MIL、不需要 ONNX 推理。\n\nProposal 对此有部分预防：引用了 Adjust for Trust Appendix D 的 F1 ≤ 0.5 作为\"简单方法不行\"的证据。但这里有一个逻辑漏洞：Adjust for Trust 用的是\"surface-level interaction heuristics\"来预测**信任**（一个主观态度），而本 proposal 要预测的是**过度依赖行为**（可观察的行为模式）。预测主观信任态度当然比识别行为模式更难。如果直接用 Liu et al. 的 5 种模式做规则匹配来检测过度依赖行为本身，准确率可能就不那么低了——这正是 proposal 需要但未提供的对照实验。\n\n增量价值声称在于\"多分辨率时间动态处理能捕获规则无法编码的微妙模式\"，但这是一个未验证的假设，而不是已知的事实。\n\n---\n\n【前提假设检验】:\n\n核心逻辑链中有 **3 个未经验证的关键假设**：\n\n1. **\"行为信号在 LLM 对话中能实时区分过度依赖 vs. 非过度依赖窗口\"（而非仅在事后分析中区分用户群体）**。Liu et al. 的发现是群体级别的聚类分析（高过度依赖用户群 vs. 低过度依赖用户群的行为差异），不是窗口级别的实时分类。从\"不同过度依赖水平的用户有不同的行为模式\"到\"每个 30 秒窗口的行为特征能预测该窗口中是否正在发生过度依赖\"，这是一个巨大的推理跳跃。前者可能反映的是个人特质/习惯差异，而不是可以在同一个人的时间序列中捕捉到的状态变化。\n\n2. **\"从物理 HRI 和合作任务中的行为信任预测 (84%, 90%) 可以推广到 LLM 对话场景\"**。Campagna et al. 的行为指标是凝视方向、空间位移、速度同步——这些是物理空间中的身体行为。Kaneko & Yamada 在无人机/驾驶模拟器中的结果也涉及物理交互。浏览器中的鼠标/键盘交互与物理身体行为在信噪比和信息丰富度上可能存在数量级差异。这些跨域的正面证据实际上非常弱。\n\n3. **\"Liu et al. 的 77 人数据集 + 滑动窗口 ≈ 26K-40K 样本足以训练一个有意义的分类器\"**。Proposal 自己承认 sample-to-parameter 比率是 0.65-1.0:1 \"tight but viable\"，并引用 PRISM 在 UCI-HAR 上 0.18:1 的比率作为先例。但 UCI-HAR 是 6 类清晰分离的物理活动（走、跑、坐、站、上楼、下楼），而过度依赖是一个模糊的、高噪声的二分类问题。更关键的是，滑动窗口产生的样本之间有 83% 的重叠（30 秒窗口、5 秒步长），这些不是独立样本——有效独立样本数远小于 26K-40K。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Gap 定位是真实的：截至 2026 年上半年，确实没有论文同时做到\"纯行为信号 + 实时检测 + 自适应干预 + LLM 对话\"这四个条件的组合。但 novelty 主要是**组合性的**（combining existing pieces），而非**概念性的**。核心组件——行为信号词汇表来自 Liu et al.、自适应干预策略来自 Adjust for Trust、多分辨率 CNN 来自 PRISM、弱监督标注来自 Snorkel——都是已有工作的直接应用或微调。Proposal 的诚实之处在于它自己承认了这一点，但这也意味着核心贡献是\"工程集成 + 实证验证\"，而非方法论创新。如果分类器效果 positive，审稿人大概率会说\"good engineering, expected direction\"而非\"surprising\"。\n\n2. **Significance: 中** — \n   过度依赖是 HCI/AI 领域的热门且重要问题，但本 proposal 的影响力受限于几个因素：(a) 它高度依赖 Liu et al. 的 77 人数据集，而该数据集的任务设计（注入型错误信息）本身存在生态效度问题（proposal 自己也承认）；(b) 即使分类器工作，从受控实验到真实部署的泛化路径不明；(c) 该领域正在快速移动——CHI 2026 同时发表了 Liu et al. 和 Sensing What Surveys Miss，到 CHI 2027 投稿截止时（约 2026 年 9 月），可能已有其他团队在做类似整合。significance 的上限受限于\"这本质上是一个系统论文 + 用户研究\"，而系统的核心技术组件缺乏独立的方法论贡献。\n\n3. **Related Work: 强** — \n   这是 proposal 最突出的优势。Related work 覆盖极为全面且准确：所有引用的关键论文都真实存在、描述准确，包括负面结果（Dechant et al.、Adjust for Trust Appendix D）。差异化定位清晰——逐一与 Liu et al.、Adjust for Trust、Sensing What Surveys Miss、Li et al. 做了精确的对比。对领域格局的理解是深入的。唯一的轻微不足是对跨域证据（Campagna et al., Kaneko & Yamada）的强度存在选择性呈现——强调了正面数字但弱化了领域鸿沟。\n\n---\n\n【概率估计】（假设投稿合适场地如 CHI 2027）: [20% - 32%] 中位 25%\n\n【概率估计】（投稿 CoRL 2026）: 0%（desk reject）\n\n【估计理由】:\n- **CoRL 2026: 0%**。该 proposal 与 CoRL 的 scope（机器人学习）完全无关，会被直接退回不送审。\n- **假设投到 CHI 2027**: Novelty 是组合性的而非概念性的，核心发现即使 positive 也不会让审稿人 surprised——\"用更深的模型在更丰富的行为特征上做更好\"是一个 expected direction。Trivial alternative（规则系统）的威胁真实存在且 proposal 的 weak supervision 循环性分析虽然设计精巧但实际上突显了这个问题。前提假设中\"群体级行为差异 → 窗口级实时检测\"的跳跃是最大的逻辑风险。这些因素将上界限制在 ~32%。下界 20% 是因为 gap 定位清晰、related work 极强、dual-outcome 设计（即使检测失败也有贡献）提供了一定的安全网，加上 120 人用户研究的规模在 CHI 社区是合格的。\n\n【主要风险】:\n1. **场地致命错配**: CoRL 不接受非机器人论文，该 proposal 会被 desk reject。这是唯一且决定性的风险。\n2. **（假设合适场地）核心假设未验证**: \"群体级行为聚类差异\"能否转化为\"窗口级实时分类信号\"是一个未经验证且不显然成立的假设。如果这个假设不成立（即行为差异反映的是个体特质而非可检测的时刻状态），整个技术核心就会崩塌——虽然 proposal 设计了 fallback contributions，但 CHI 审稿人对一篇\"核心 claim 失败但我们有 fallback\"的论文通常不会很宽容。\n```\n\nSources:\n- [Liu et al., Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)\n- [Srinivasan & Thomason, Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Liu et al., Sensing What Surveys Miss (CHI 2026)](https://dl.acm.org/doi/full/10.1145/3772318.3791191)\n- [Campagna et al., Estimating Trust in HRC (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Raees & Papangelis, From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)\n- [PRISM: Lightweight Multivariate Time-Series Classification (2025)](https://arxiv.org/abs/2508.04503)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 【致命前置问题：投稿会议匹配性】\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：\n\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n\"Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 是一篇纯粹的 HCI 论文——浏览器扩展检测用户对 LLM 的过度依赖并触发自适应干预。全文没有任何与机器人学习相关的内容（无机器人平台、无 sim-to-real、无机器人感知/操控/运动规划）。提交至 CoRL 将被 desk reject，概率接近 100%。\n\n本 proposal 的自然目标会议应为：CHI 2027、IUI 2027、CSCW 2027、或 UIST 2027。以下分析基于假设该 proposal 被投至合适的 HCI 顶会（如 CHI），以评估其 idea 内核质量。\n\n═══════════════════════════════════════════════════\n\n【领域调研】:\n\n1. Liu, Zhou, Shen, Liu, Wu & Chen. \"Behavioral Indicators of Overreliance During Interaction with Conversational Language Models\" (CHI 2026, arXiv 2602.11567):\n   - 与本 proposal 的关系：直接上游工作，提供了行为信号词汇表。本 proposal 的整个 signal vocabulary 和 feature engineering 基于此文。\n   - 关键发现：77 名被试、3 个任务，通过 autoencoder clustering 识别出 5 种过度依赖行为模式。论文明确将实时检测和干预留作 future work。\n\n2. Srinivasan & Thomason. \"Adjust for Trust\" (IUI 2026, arXiv 2502.13321):\n   - 与本 proposal 的关系：直接竞争/互补工作。本 proposal 试图用行为信号替代该文的自我报告机制。\n   - 关键发现：通过信任自适应干预实现 38% inappropriate reliance 降低，但需要每次决策后 11 分制自我报告。Appendix D 文档记录了行为估计的失败尝试 (F1 ≤ 0.5)。\n\n3. Ailin Liu et al. \"Sensing What Surveys Miss\" (CHI 2026, arXiv 2602.00880):\n   - 与本 proposal 的关系：最相似的系统架构——闭环 sensing→intervention。但目标构念不同（认知负荷 vs. 过度依赖），且依赖生理传感器 (EDA)。\n   - 关键发现：鼠标 + EDA 结合线性回归仅达 ~61% 检测准确率，N=32，未提供鼠标单独的消融实验。\n\n4. Campagna et al. \"Estimating Trust in Human-Robot Collaboration through Behavioral Indicators\" (RA-L 2025, arXiv 2601.19856):\n   - 与本 proposal 的关系：正面证据——行为信号可以预测信任，但在完全不同的领域 (HRI 物理协作)。\n   - 关键发现：84% 准确率，AUC=0.90，但 N=14，使用了凝视方向、空间位移等 HRI 特有特征。\n\n5. Li, Zhu, Lu, Xiao & Yin. \"From Text to Trust\" (CHI 2025, arXiv 2502.11919):\n   - 与本 proposal 的关系：类似的自适应干预思路，但限于结构化表格任务 + 粗粒度反馈。\n   - 关键发现：POMDP 框架自适应选择 LLM 解释，显著提升准确率，但仅用二元 agree/disagree 反馈。\n\n6. Raees & Papangelis. \"From Trust to Appropriate Reliance\" (arXiv 2604.23896, April 2026):\n   - 与本 proposal 的关系：提供测量理论基础，支持行为过程指标优于主观信任评分。\n   - 关键发现：信任与适当依赖是概念上不同的构念，推荐 RAIR/RSR 等行为过程指标。\n\n- 调研总结：该领域在 2025-2026 年高度活跃，多篇 CHI/IUI 顶会论文分别解决了行为表征（Liu et al.）、信任自适应干预（Adjust for Trust）、传感器闭环系统（Sensing What Surveys Miss）等子问题。但确实没有工作将\"仅基于非侵入式行为信号的实时过度依赖检测\"与\"自适应干预\"在自由对话式 LLM 交互中闭环连接起来。这个 gap 真实存在。\n\n═══════════════════════════════════════════════════\n\n【Trivial Alternative 检验】:\n\n存在一个关键的 trivial alternative 威胁：\n\n直接将 Liu et al. 的 5 个行为模式编码为规则阈值（rule-based detector），配合简单的滑动窗口统计，是否能达到类似效果？\n\nProposal 的论证是：\"Adjust for Trust Appendix D 表明 surface-level heuristics 的 F1 ≤ 0.5，所以需要更复杂的模型。\" 但这里有一个关键区别——Appendix D 使用的是 AIAcc5、CapabilityDiff 等粗粒度交互启发式特征来估计\"信任\"，而非 Liu et al. 识别的 5 种具体过度依赖行为模式。Liu et al. 的模式（如\"快速复制粘贴无编辑\"、\"跳过初始理解\"）本身就可能足以直接编码为高精度规则。\n\n实际上，proposal 自己在 weak supervision 模块中就是在做这件事（将 5 种模式编码为 labeling functions）。如果这些规则本身就有足够的判别力，那么 CNN 的增量价值存疑——proposal 自己也承认了这个 circularity 问题。\n\n增量价值在于：(1) 时间粒度——从 session 级别到 30 秒窗口的流式检测；(2) 泛化——CNN 可能发现 Liu et al. 未识别的隐式模式。但这两点是否成立是纯粹的实证问题，目前没有先验理由强烈支持。\n\n**结论：trivial alternative 威胁中等偏高。如果基于 Liu et al. 5 个模式的简单规则检测器在 30 秒窗口上也能达到 65-70% 准确率，CNN 的增量价值将被大幅稀释。**\n\n═══════════════════════════════════════════════════\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条存在以下未经验证的关键假设：\n\n1. **Session-level patterns → Window-level detectability（最关键假设）**：Liu et al. 的 5 种行为模式是通过对整个 session 的 autoencoder clustering 识别的。这些 session 级别的模式是否在 30 秒的短窗口中仍然可检测，是完全未经验证的。某些模式（如\"跳过初始理解\"）本质上是 session 初期的一次性事件，不适合流式滑动窗口检测。\n\n2. **HRI domain → LLM conversation domain 的迁移假设**：proposal 引用 Campagna et al. (84%) 和 Kaneko & Yamada (90%) 作为\"行为信号可以预测信任\"的正面证据，但这两项工作分别在物理 HRI（化学实验协作，N=14）和无人机/驾驶模拟中进行。它们使用的行为特征（凝视方向、空间位移、速度同步）与浏览器交互特征（鼠标轨迹、复制粘贴）在信号性质上有本质区别。将 84%/90% 的准确率作为\"richer modeling 可以提升检测\"的证据，逻辑链条较弱。\n\n3. **特征信息量假设**：proposal 假设鼠标动态、滚动行为、按键统计等 28 维特征包含足够的信息来区分过度依赖与非过度依赖。但 Dechant et al. (2023) 明确发现鼠标轨迹特征\"might not explain sufficiently the variance\"，Sensing What Surveys Miss 即使加上 EDA 也只有 ~61%。proposal 的核心赌注是\"multi-resolution temporal processing 可以弥补信号本身的不足\"，但这是一个未经验证的假设。\n\n4. **Labeling 质量假设**：hybrid labeling 策略看似稳健，但 MIL 的 outcome propagation 本质上仍是将 task-level label 传播到 window level——如果一个 session 被标记为\"过度依赖\"但其中只有 30% 的时间窗口实际表现出过度依赖行为，MIL 能否正确学到这一点取决于 attention 机制的质量，而训练数据量（~30K windows from 77 participants）可能不足以让 MIL attention 收敛到有意义的模式。\n\n═══════════════════════════════════════════════════\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   理由：gap identification 是真实的——确实没有工作将纯行为信号实时检测与自适应干预在自由对话 LLM 交互中闭环连接（调研验证了 Liu et al.、Adjust for Trust、Sensing What Surveys Miss 各自只覆盖了部分）。labeling methodology（MIL + weak supervision + sparse probes + self-supervised）和 circularity ablation 设计有方法论贡献。但核心技术路线是 **systems integration**——将 Liu et al. 的信号 + 已有 CNN 架构 + Adjust for Trust 的干预策略组合起来。multi-resolution 1D-CNN 在行为序列上的应用是标准的 time-series classification pipeline，不构成算法层面的 novelty。如果审稿人问\"剥离系统集成后，你的 core technical contribution 是什么\"，回答主要是 labeling methodology 和 ablation design——有价值但不够 surprising。相比 Sensing What Surveys Miss（同样是 CHI 2026，也做了闭环 sensing→intervention，只是目标和传感器不同），本 proposal 的架构 novelty 有限。\n\n2. **Significance: 中偏强** — \n   理由：LLM 过度依赖是高度及时且重要的问题（Ibrahim et al. 2025 的综述明确呼吁 process-oriented mitigation；Raees & Papangelis 2026 提供了测量理论支撑）。非侵入式、browser-only 的方案如果可行，实际部署价值很高。head-to-head 比较四种干预条件（无干预、静态 CFF、自我报告自适应、行为自适应）的实验设计本身就有独立的实证价值。但 significance 的天花板受限于核心检测问题的不确定性——如果行为信号确实不足以支撑可靠检测（prior evidence 偏向悲观），整个系统的实际影响力会大幅缩水。proposal 的\"即使检测失败也有贡献\"的 dual-outcome framing 有一定说服力，但\"表征行为信号能预测什么和不能预测什么\"本身作为 main contribution 对 CHI 来说可能偏弱。\n\n3. **Related Work: 强** — \n   理由：覆盖非常全面，几乎穷尽了 2023-2026 年间所有直接相关的工作。对 Liu et al. (CHI 2026)、Adjust for Trust (IUI 2026)、Sensing What Surveys Miss (CHI 2026)、Li et al. (CHI 2025) 的定位清晰且准确（经调研验证）。正面证据（Campagna et al.、Kaneko & Yamada）和负面证据（Dechant et al.、Adjust for Trust Appendix D）都有引用，展示了 balanced perspective。唯一的小瑕疵是对 Campagna et al. (N=14, HRI domain) 和 Kaneko & Yamada (模拟器任务) 的正面结果在论证中的权重可能过高——这些工作的 domain gap 太大，不宜作为\"behavioral trust prediction is achievable\"的强证据。\n\n═══════════════════════════════════════════════════\n\n【概率估计】: \n\n- 若投 CoRL 2026: ~0%（desk reject，不在 scope 内）\n- 若投合适的 HCI 顶会（CHI 2027）: [22% - 32%] 中位 27%\n\n【估计理由】: \n如果投稿 CoRL，这是一个明确的 scope mismatch，会被直接退稿。\n\n假设投稿至 CHI（该 proposal 的自然目标会议）：idea 内核处于\"real gap + reasonable approach, but core contribution is integration rather than deep novelty\"区间。Related Work 覆盖是 asset（强），但 Novelty 受限于 systems integration 性质（中），Significance 受制于核心检测问题的实证不确定性（中偏强但有条件）。Trivial alternative 威胁（规则检测器可能接近 CNN 性能）和前提假设风险（session-level patterns 未必 window-level 可检测）共同限制了上界。如果核心检测结果是 positive (>75% accuracy)，这篇论文有竞争力；如果只有 65-70%，dual-outcome framing 能否说服审稿人取决于执行质量。上界被 Novelty 维度限制——即使实验完美执行，\"组合 A+B+C 的系统\"在 novelty 评分上天花板不高。\n\n【主要风险】:\n1. **Novelty 天花板**：核心贡献是系统集成（已知信号 + 已有架构 + 已有干预策略），审稿人可能认为\"the gap was obvious, the filling is engineering\"——gap 真实但填补方式缺乏 surprising insight。\n2. **核心假设可能不成立**：session-level 行为模式在 30 秒流式窗口中是否可检测、浏览器行为特征是否包含足够信息量来区分过度依赖——这两个前提如果不成立，整篇论文的核心系统价值归零，仅剩\"negative result + methodology contribution\"，这对顶会来说可能不够。\n```\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Liu et al. \"Behavioral Indicators of Overreliance\" (CHI 2026)](https://arxiv.org/abs/2602.11567)\n- [Srinivasan & Thomason \"Adjust for Trust\" (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Ailin Liu et al. \"Sensing What Surveys Miss\" (CHI 2026)](https://arxiv.org/abs/2602.00880)\n- [Campagna et al. \"Estimating Trust in Human-Robot Collaboration\" (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Raees & Papangelis \"From Trust to Appropriate Reliance\" (2026)](https://arxiv.org/abs/2604.23896)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Closing the Loop: From Behavioral Overreliance Detection to Adaptive Intervention in LLM Conversations\n\n## Description\nWe propose OverrelianceGuard, the first closed-loop system that bridges unobtrusively collected behavioral interaction signals to real-time adaptive interventions in free-form conversational LLM interactions—without requiring self-report interruptions or physiological sensors. A browser extension captures non-invasive interaction events in 30-second sliding windows and transforms them into a temporal grid representation: each window is discretized into 30 one-second bins, with 28 aggregated features per bin capturing action type distribution (over 12 categories), mouse dynamics (distance, velocity), scroll behavior (distance, direction), keypress statistics, copy-paste behavior (including post-paste edit indicators), idle duration, dwell context relative to LLM responses, and page focus. This (30 × 28) temporal grid—derived from but explicitly distinct from Liu et al.'s (CHI 2026) per-event 37-dimensional encoding (15-dim action type one-hot + 1-dim timestamp + 2-dim page type + 19-dim type-specific attributes)—feeds a lightweight multi-resolution 1D-CNN (~40K parameters, <5ms browser inference via ONNX Runtime Web) with three parallel temporal branches capturing short-burst (2s), medium-term (10s), and full-window (30s) behavioral dynamics. We cite PRISM's 97.3% accuracy on UCI-HAR as evidence of architectural efficiency at this parameter scale, not as a performance projection—UCI-HAR involves 6-axis accelerometer data with well-separated activity classes, whereas overreliance classification operates on noisier interaction features with subtler boundaries. The architecture choice is motivated by converging evidence that simple models on behavioral signals are insufficient—Adjust for Trust's Appendix D found F1 ≤ 0.5 with surface-level heuristics, 'Sensing What Surveys Miss' (CHI 2026) achieves only ~61% with linear regression on mouse+EDA—while richer models on multi-dimensional behavioral features show substantially better results: Campagna et al. (RA-L 2025) achieve 84% trust classification (AUC=0.90) from behavioral indicators in HRI, and Kaneko & Yamada (2025) reach 90% in cooperative tasks. A methodological contribution is the hybrid labeling strategy addressing temporal misalignment between Liu et al.'s outcome-based labels and streaming prediction: outcome propagation via Multiple Instance Learning, weak supervision from programmatic heuristics encoding the five identified behavioral patterns, sparse event-triggered metacognitive probes (2–3 per task vs. Adjust for Trust's 30 per-decision self-reports), and self-supervised next-action prediction. Critically, we address the weak supervision circularity risk—where labeling functions encode behavioral patterns from the same feature space the CNN processes—through a four-condition ablation: (i) weak-supervision-only, (ii) MIL+probes-only (circularity-free, as labels derive from task outcomes and self-report), (iii) MIL+probes+self-supervised, and (iv) full multi-signal training. Comparing conditions (iv) vs. (ii) isolates whether the weak supervision provides complementary signal or merely teaches the CNN its own hand-coded rules, with Integrated Gradients feature attribution analysis revealing whether the model discovers temporal patterns beyond those encoded in labeling functions. We frame streaming behavioral overreliance detection as the core hypothesis being tested: if classifier accuracy proves disappointing (e.g., 65–70%), the within-subjects intervention comparison, the labeling methodology, and the characterization of what behavioral signals can and cannot predict all constitute independently publishable contributions. We analyze training data sufficiency: Liu et al.'s 77-participant dataset yields ~26K–40K behavioral windows with our proposed windowing, supplemented by augmentation and a phased training strategy. When overreliance risk exceeds personalized thresholds, the system selects from tiered interventions: metacognitive prompts (Assumption-style CFFs), counter-explanations (per Adjust for Trust), and comprehension checkpoints. Following Raees & Papangelis's (2026) measurement framework distinguishing trust from appropriate reliance, we assess overreliance via both Traditional (acceptance rates) and Appropriateness-view (RAIR/RSR) metrics. A within-subjects study (N≈120) across four LLM-assisted tasks compares four conditions: no intervention, static cognitive forcing, self-report-adaptive (replicating Adjust for Trust), and behaviorally-triggered adaptive (OverrelianceGuard). This work fills the gap between behavioral characterization (Liu et al., CHI 2026), trust-adaptive intervention via self-report (Adjust for Trust, IUI 2026), adaptive explanation selection in structured tasks (Li et al., CHI 2025), and sensor-dependent adaptive support (Sensing What Surveys Miss, CHI 2026)—contributing (1) the first streaming behavioral overreliance classifier for conversational LLM settings with a principled hybrid labeling methodology and explicit circularity analysis, (2) a deployable browser-based closed-loop intervention system requiring neither self-report interruptions nor physiological sensors, (3) head-to-head empirical evidence comparing self-report-based vs. behavior-based adaptive intervention, and (4) a rigorous characterization of what behavioral signals can and cannot predict about overreliance, advancing the field regardless of detection accuracy.\n\n## Core Problem\nCan unobtrusively collected behavioral interaction signals (copy-paste patterns, scroll depth, verification dwell time, tab-switch frequency) drive a real-time streaming classifier that triggers adaptive interventions to reduce overreliance on LLM outputs—without requiring self-report interruptions or invasive physiological sensors?\n\n## Opportunity\nLiu et al. (CHI 2026, arXiv 2602.11567) identify five behavioral patterns distinguishing high- vs. low-overreliance users in LLM interactions but explicitly leave real-time detection and intervention as future work. Srinivasan & Thomason's 'Adjust for Trust' system (IUI 2026, arXiv 2502.13321) achieves up to 38% reduction in inappropriate reliance through trust-adaptive interventions, but requires self-reported trust ratings on an 11-point scale after every decision—an intrusive approach whose inadequacy the authors themselves confirm in Appendix D, where their attempts at behavioral trust estimation yielded only 0.25–0.51 correlation and F1 ≤ 0.5 using surface-level interaction heuristics. Li et al.'s 'From Text to Trust' (CHI 2025, arXiv 2502.11919) adaptively selects explanations via POMDP-based hidden state estimation, but operates only in structured tabular decision tasks using coarse binary (agree/disagree) feedback—not rich behavioral signals in free-form LLM conversations. Ailin Liu et al.'s 'Sensing What Surveys Miss' (CHI 2026, arXiv 2602.00880) build the closest architectural parallel—a closed-loop system using mouse dynamics and electrodermal activity (EDA) to trigger adaptive LLM-based interventions—but target cognitive load during online surveys (not overreliance in LLM conversations), require physiological sensors (EDA wristbands), and achieve only ~61% detection accuracy with simple linear regression classifiers and max-fusion of two unimodal models; crucially, the paper provides no ablation separating mouse-only from EDA contributions, leaving open the question of whether interaction signals alone—processed with richer temporal modeling than linear regression—can achieve adequate detection without physiological sensing. The evidence for behavioral trust prediction is mixed but increasingly positive: while Dechant et al. (2023) find mouse trajectories alone insufficient and Adjust for Trust's Appendix D reports F1 ≤ 0.5 with surface-level heuristics, Campagna et al. (RA-L 2025, arXiv 2601.19856) achieve 84% accuracy classifying trust from behavioral indicators in human-robot collaboration using ensemble classifiers, and Kaneko & Yamada (IEEE Access, 2025; arXiv 2407.01752) demonstrate 90% accuracy predicting trust dynamics via dynamic structural equation modeling in physical cooperative tasks—both suggesting that behavioral features CAN support useful trust prediction with appropriate modeling depth, even if the domain gap to conversational LLM settings makes these figures proof-of-principle rather than direct benchmarks. Raees & Papangelis ('From Trust to Appropriate Reliance,' arXiv 2604.23896, April 2026) further argue that trust measurements are conceptually distinct from appropriate reliance—the construct we actually target—and advocate for behavioral process metrics over subjective trust ratings, providing measurement-theoretic grounding for our approach. The bridge remains unbuilt: no system uses fine-grained, continuously captured interaction signals alone to detect overreliance and trigger personalized interventions in conversational LLM settings. This is now technically feasible because (1) Liu et al.'s behavioral characterization provides the validated signal vocabulary via per-event interaction encodings, (2) lightweight time series classifiers like PRISM achieve high efficiency with only ~40K parameters and sub-millisecond inference, enabling browser-embedded real-time classification without physiological hardware, and (3) the converging positive evidence from Campagna et al. and Kaneko & Yamada establishes that behavioral trust prediction is achievable with appropriate modeling depth—though whether this generalizes to conversational LLM interactions remains the core empirical hypothesis we test.\n\n## Related Work / Landscape\nLiu et al. (CHI 2026) provide the most comprehensive behavioral characterization of LLM overreliance, identifying five patterns—frequent copy-paste without editing, skipped initial task comprehension, rapid LLM-task alternation, coarse block-pasting vs. fine-grained editing, and hesitation-then-acceptance—via autoencoder clustering of per-event interaction encodings (each event represented as a 37-dimensional vector: 15-dim action type one-hot + 1-dim normalized timestamp + 2-dim page type + 19-dim type-specific attributes) from 77 participants across three tasks with injected misinformation. The 'Adjust for Trust' system (Srinivasan & Thomason, IUI 2026) demonstrates that adapting explanations based on trust level (supporting explanations when trust is low, counter-explanations when high, with enforced reading delays) yields up to 38% reduction in inappropriate reliance and 20% accuracy improvement; however, it relies on self-reported trust on an 11-point scale after every one of 30 decisions per session. Critically, Appendix D documents the authors' failed attempt at replacing self-report with behavioral estimation: simple heuristics (AIAcc5, CapabilityDiff, SmoothOutcomes, SmoothConfs) achieved only 0.25–0.51 correlation and F1 ≤ 0.5, concluding that 'surface-level interaction features' are inadequate for trust modeling. Li et al. ('From Text to Trust,' CHI 2025) use a POMDP framework to adaptively select LLM-generated analyses based on inferred user hidden states, significantly improving accuracy on tabular classification tasks—but their interaction paradigm is structured (sequential agree/disagree on feature-level explanations), their state estimation uses only binary response feedback, and they neither capture behavioral signals nor address free-form conversational LLM use. Ailin Liu et al.'s 'Sensing What Surveys Miss' (CHI 2026, arXiv 2602.00880) is the most architecturally analogous prior work: it builds a closed-loop system where mouse dynamics (vertical direction changes, hover time, hover count) and electrodermal activity (tonic EDA level, EDA peaks) feed personalized linear regression classifiers with rule-based threshold adaptation, triggering LLM-generated clarifications during online surveys. In a within-subjects study (N=32), their aligned-adaptive timing improved survey response accuracy by 21% and reduced false negatives from 50.9% to 22.9%. However, three key differences separate their work from ours: (a) they target cognitive load in knowledge-based survey items, not overreliance on LLM outputs in conversational interaction—fundamentally different constructs requiring different signal vocabularies; (b) they require physiological sensors (EDA wristbands), limiting scalability to any-browser deployment; and (c) their simple linear regression classifiers with max-fusion of two unimodal models achieve only ~61% detection accuracy, and they provide no ablation isolating the contribution of mouse dynamics alone vs. EDA alone—leaving open whether their mouse features would function without the physiological channel. Their finding that even combined mouse+EDA with simple models reaches only 61% accuracy actually reinforces our hypothesis that richer temporal signal processing (multi-resolution CNNs operating on the full behavioral feature space) is needed to compensate for the absence of physiological signals. The evidence landscape for behavioral trust/reliance prediction includes both negative and positive results. On the negative side: Dechant et al. (arXiv 2310.16632, 2023) find that mouse trajectory features alone 'might not explain sufficiently the variance to be used on their own'; Adjust for Trust's Appendix D shows F1 ≤ 0.5 with heuristic behavioral features. On the positive side: Campagna et al. (RA-L 2025, arXiv 2601.19856) achieve 84% trust classification accuracy (Voting Classifier, AUC=0.90, F1=0.84) from seven behavioral indicators—gaze direction, spatial displacement, speed synchronization, reaction time, predictability, and legibility—in a human-robot chemical mixing task (N=14), demonstrating that ensemble classifiers on multi-dimensional behavioral features substantially outperform single-signal approaches, albeit in a physical HRI domain with a small sample; Kaneko & Yamada (IEEE Access, 2025) achieve 90% accuracy predicting over/under-trust using dynamic structural equation modeling on interaction data in drone and driving simulators; and Gurney et al. (Persuasive Technologies, 2023; arXiv 2302.01854) show that behavioral predictors outperform self-report psychometric inventories for predicting AI compliance. This pattern—negative results with simple models on narrow feature sets, positive results with richer models on multi-dimensional behavioral features—is central to our technical hypothesis. Raees & Papangelis ('From Trust to Appropriate Reliance,' arXiv 2604.23896, April 2026) provide important measurement-theoretic context, arguing that trust and appropriate reliance are conceptually distinct constructs: trust reflects subjective perception while reliance concerns observable behavioral decisions. They identify three measurement views (Traditional: over/under-reliance rates; Appropriateness: RAIR/RSR; Dominance: AI influence direction) and recommend behavioral process metrics over subjective ratings—directly supporting our approach of measuring reliance behavior rather than trust attitudes. Sun et al. ('Eyes Can't Always Tell,' arXiv 2604.01741, 2026) demonstrate that eye-tracking-to-cognitive-state mappings shift across AI conditions, arguing for multi-signal, context-dependent approaches. Cognitive forcing functions have been studied extensively: Buçinca et al. (CSCW 2021) showed CFFs reduce overreliance but increase frustration; Ghosh et al. (arXiv 2601.18033, 2026) found Assumption-style CFFs most effective at reducing overreliance without increasing cognitive load. Ibrahim et al. (arXiv 2509.08010, 2025) consolidate measurement gaps and call for process-oriented mitigation. The 'From Calibration to Collaboration' position paper (arXiv 2506.07461, June 2025) argues that current UQ methods are misaligned with real user needs. Key limitation across all works: no system closes the loop from non-invasive behavioral detection to adaptive intervention in free-form conversational LLM interactions. Liu et al. characterize signals but build no real-time system; Adjust for Trust intervenes adaptively but requires intrusive every-decision self-report that their own behavioral estimation attempt failed to replace; From Text to Trust adapts but only in structured tasks with coarse feedback; Sensing What Surveys Miss closes the loop but requires physiological sensors and targets cognitive load in surveys with simple classifiers achieving only 61% accuracy; Campagna et al. predict trust behaviorally in HRI but build no intervention system for conversational AI; and Kaneko & Yamada predict trust in physical cooperative tasks but do not address conversational LLM settings.\n\n## Approach\nBuild OverrelianceGuard, a browser-extension-based closed-loop system with three components:\n\n(1) INSTRUMENTATION LAYER: A JavaScript layer that unobtrusively captures interaction events in 30-second sliding windows (5-second stride). FEATURE REPRESENTATION CLARIFICATION: Liu et al.'s original 37-dimensional encoding is a per-event representation—each discrete interaction event (click, scroll, keypress, etc.) is encoded as a 37-dimensional vector comprising a 15-dim action type one-hot, 1-dim normalized timestamp, 2-dim page type, and 19-dim type-specific attributes (e.g., mouse movement distance and duration, scroll distance and direction, keypress count). Their transformer autoencoder operates on variable-length sequences of these event vectors per segment. Our CNN requires fixed-size input per window, so we transform Liu et al.'s event sequences into a temporal grid representation: each 30-second window is discretized into T=30 one-second bins, and for each bin we compute K=28 aggregated features from all events occurring within that bin. Specifically, the 28 per-bin features are: (a) action type distribution—proportions over 12 action categories (mouse movement, click, scroll, keypress, copy, paste, highlight, delete, idle, tab switch, prompt input, element switch; 12 features); (b) mouse dynamics—total movement distance and mean velocity (2); (c) scroll dynamics—total distance and direction ratio (up/down; 2); (d) keypress statistics—count and mean inter-key interval (2); (e) copy-paste behavior—copy count, paste count, and post-paste edit indicator (3); (f) idle time—total idle duration within the bin (1); (g) dwell context—time since last LLM response (1); (h) page context—fraction of time on LLM page vs. task page (1); (i) text interaction—highlight text length and delete count (2). This yields a (30 × 28) input tensor per window, where the temporal dimension (30 timesteps) captures within-window behavioral dynamics that the multi-resolution CNN branches process at different scales. Features are z-score normalized per-user via an initial 5-minute calibration phase to account for individual baseline interaction styles.\n\n(2) STREAMING OVERRELIANCE RISK CLASSIFIER: A multi-resolution 1D-CNN inspired by the PRISM architecture (~40K parameters). Three parallel convolutional branches with symmetric FIR filters at different temporal resolutions—2s (kernel size 2, capturing short-burst behaviors like rapid copy-paste), 10s (kernel size 10, capturing medium-term patterns like comprehension scanning), and 30s (kernel size 30, capturing full-window dynamics like engagement trajectory)—operate on the (30 × 28) temporal grid input, feed into per-branch global average pooling, then concatenate into a 2-layer MLP classification head (128→2) outputting an overreliance risk score ∈ [0,1]. This architecture is chosen because: (a) the (30 × 28) input is a moderately-sized temporal grid (not high-dimensional sensor data where ViT/transformers excel), (b) PRISM achieves 97.3% on UCI-HAR with ~40K parameters—we cite this as evidence of architectural efficiency at this parameter scale and sub-millisecond inference capability, not as a performance projection for our task, since UCI-HAR uses 6-axis accelerometer/gyroscope data with 6 well-separated physical activity classes, whereas overreliance classification operates on noisier mouse/keyboard interaction features with subtler class boundaries; (c) 1D-CNNs run in <5ms via ONNX Runtime Web on commodity CPUs; and (d) the Adjust for Trust Appendix D failure with surface-level heuristics and Sensing What Surveys Miss's ~61% accuracy with linear regression on mouse+EDA both suggest that improvement comes from richer temporal feature processing (multi-resolution convolutions capturing dynamics at multiple scales), not larger models or physiological sensors—while Campagna et al.'s 84% accuracy with ensemble classifiers on multi-dimensional behavioral features in HRI confirms that richer modeling on behavioral features can substantially exceed simple-model baselines. We compare against MiniRocket (fixed kernels + linear head, near-zero learnable parameters) and BiLSTM (128 hidden units, ~200K parameters) baselines to isolate the contribution of the multi-resolution architecture.\n\nTRAINING DATA SUFFICIENCY ANALYSIS: Liu et al.'s dataset comprises 77 participants × 3 tasks = 231 sessions. With our proposed 30-second sliding windows at 5-second stride, assuming average task durations of 10–15 minutes (consistent with their protocol), each session yields ~115–175 windows, producing an estimated 26K–40K behavioral windows total. For a 40K-parameter model, this yields a sample-to-parameter ratio of 0.65–1.0:1, which is tight but viable: for comparison, PRISM achieves 97.3% on UCI-HAR with only 7,352 training samples and ~40K parameters (ratio ~0.18:1). Nevertheless, we address overfitting risks through five mitigation strategies: (a) standard time series data augmentation—Gaussian jittering (σ=0.05), window slicing (90% crops), and time warping—which have been shown to substantially improve 1D-CNN accuracy on small behavioral datasets; (b) model regularization via dropout (p=0.3), L2 weight decay (λ=1e-4), and early stopping on a held-out validation set; (c) attention entropy maximization in the MIL pooling layer to prevent attention collapse onto few instances; (d) the weak supervision labeling functions themselves provide soft probabilistic labels that act as implicit label smoothing, reducing overfitting to noisy hard labels; and (e) a phased data strategy leveraging both datasets—train and validate on Liu et al.'s 77-participant data, then fine-tune on a pilot cohort (first ~20 participants of the 120-participant study) and evaluate on the remaining ~100, ensuring the final evaluation is on held-out participants unseen during any training phase. We will report learning curves (accuracy vs. training set fraction) to empirically demonstrate whether ~30K windows are sufficient or whether the model is still data-hungry, and will release the trained model weights and augmentation pipeline for reproducibility.\n\nGROUND TRUTH LABELING STRATEGY: Liu et al.'s overreliance labels are outcome-based—a single per-task label assigned to all behavioral segments regardless of what happened in each specific window. Training a streaming classifier on these temporally misaligned labels would conflate overreliant and non-overreliant moments within the same session. We adopt a hybrid multi-signal labeling approach: (a) OUTCOME PROPAGATION via Multiple Instance Learning: for each accepted misinformation item, trace back to the behavioral window from first exposure through acceptance, treating the session as a 'bag' with the task-level overreliance label, and let an attention-based MIL pooling layer learn which sub-segments are most predictive; (b) WEAK SUPERVISION via programmatic labeling functions encoding Liu et al.'s five behavioral patterns as heuristic rules (e.g., 'copy-paste within 10s of LLM response without scrolling through response → OVERRELIANT'; 'reads task prompt >15s before first LLM query → NOT_OVERRELIANT'; 'pastes LLM content block without subsequent editing → OVERRELIANT'), reconciled via a Snorkel-style generative model into probabilistic training labels; (c) SPARSE METACOGNITIVE PROBES: at 2–3 event-triggered points per task (triggered by detected behavioral state transitions, not fixed intervals), prompt users briefly: 'How carefully are you evaluating the AI's response right now?' (5-point scale)—far less intrusive than Adjust for Trust's 30 every-decision ratings; (d) SELF-SUPERVISED REGULARIZATION: a next-action prediction auxiliary objective captures behavioral dynamics without requiring labels. The classifier is trained with a weighted multi-task loss combining all four signal types, with outcome labels serving as calibration rather than primary supervision.\n\nWEAK SUPERVISION CIRCULARITY ANALYSIS AND ABLATION: We explicitly address the risk that the CNN trained on weak supervision labels may learn to replicate the hand-coded labeling function rules rather than discover deeper temporal patterns—since the labeling functions encode behavioral patterns (e.g., copy-paste frequency, dwell time thresholds) derived from the same interaction features the CNN processes. While the Snorkel literature demonstrates that discriminative end models typically generalize beyond labeling functions (averaging 9.5-point accuracy improvements over the label model alone, as they learn subtle feature combinations and contextual patterns the heuristics miss), this generalization is not guaranteed and must be empirically verified. We design a four-condition ablation to isolate each labeling signal's contribution: (i) WS-ONLY: trained exclusively on weak supervision labels—establishes the upper bound on circularity risk, as the only supervisory signal comes from features the model also takes as input; (ii) MIL+PROBES ONLY: trained on outcome-propagated MIL labels and sparse metacognitive probe labels with NO weak supervision—these labels are derived from task outcomes and self-report respectively, providing supervision entirely independent of the input behavioral features, thereby serving as the circularity-free baseline; (iii) MIL+PROBES+SELF-SUPERVISED: adds the self-supervised next-action prediction objective to condition (ii)—tests whether temporal dynamics learning further improves outcome-based detection; (iv) FULL MULTI-SIGNAL: all four label sources combined. The critical diagnostic comparison is (iv) vs. (ii): if full training substantially outperforms MIL+probes-only training, the weak supervision provides complementary signal beyond what outcome labels alone capture; if (iv) ≈ (i) >> (ii), the model is primarily learning the hand-coded rules (confirming the circularity concern). Additionally, we conduct feature importance analysis using Integrated Gradients attribution on models from each condition, comparing the learned feature importance profiles against the features explicitly encoded in labeling functions. If the full model assigns substantial attribution to features NOT encoded in any labeling function (e.g., temporal velocity patterns, micro-hesitation dynamics, action transition probabilities), this provides positive evidence of generalization beyond the heuristic rules. We will report these ablation results as a primary finding, following the XPASC framework's principle that measuring generalization beyond labeling functions is essential for validating weakly-supervised classifiers.\n\nCONTRIBUTION ROBUSTNESS: WHAT IF DETECTION ACCURACY IS LOW? We explicitly frame streaming behavioral overreliance detection as the core empirical hypothesis being tested, not an assumed capability. The prior evidence is sobering: Adjust for Trust's Appendix D achieves F1 ≤ 0.5 with surface-level behavioral heuristics, Sensing What Surveys Miss reaches only ~61% with linear regression on mouse+EDA, and Dechant et al. find mouse features alone insufficient. Our hypothesis is that multi-resolution temporal processing on richer multi-dimensional behavioral features—following the positive trajectory shown by Campagna et al. (84% in HRI) and Kaneko & Yamada (90% in cooperative tasks)—can substantially improve on these baselines in the LLM conversation domain. However, there exists a realistic scenario where our classifier achieves only 65–70% accuracy—better than prior baselines but potentially insufficient for reliable real-time intervention. We explicitly plan for this contingency: (1) The within-subjects comparison of four intervention conditions (no intervention, static CFF, self-report-adaptive, behaviorally-triggered adaptive) constitutes a valuable empirical contribution REGARDLESS of detection accuracy—it provides the first head-to-head comparison of these paradigms in free-form LLM conversations, with the self-report-adaptive condition serving as an upper-bound benchmark for behavior-triggered approaches. Even a moderate-accuracy classifier may outperform static interventions by reducing alert fatigue and targeting interventions to riskier moments. (2) The hybrid labeling methodology (MIL + weak supervision + sparse probes + self-supervised regularization) is an independent methodological contribution applicable to any streaming behavioral classification task with outcome-level labels, publishable as a methods contribution for the temporal action localization community. (3) Characterizing WHAT behavioral signals can and cannot predict about overreliance—via the four-condition ablation, feature importance analysis, and learning curves—is itself an informative contribution that advances the field's understanding of the behavioral-detection frontier, directly addressing the open question left by Adjust for Trust's Appendix D. (4) The instrumentation layer and temporal grid feature engineering for LLM conversation interactions provides reusable infrastructure for future research. We will report detection accuracy honestly and frame negative or moderate results as informative findings about the boundaries of behavioral sensing for reliance calibration, following Raees & Papangelis's (2026) call for rigorous behavioral measurement of appropriate reliance.\n\n(3) TIERED ADAPTIVE INTERVENTION ENGINE: When the streaming risk score exceeds personalized thresholds (calibrated from the 5-minute baseline), the system selects from escalating interventions: (Tier 1, risk 0.5–0.7) a lightweight Assumption-style metacognitive prompt ('What might be wrong with this answer?') shown as a non-blocking tooltip; (Tier 2, risk 0.7–0.9) a counter-explanation surfacing potential errors in the LLM's response, modeled on Adjust for Trust's strategy, with a 10-second reading delay; (Tier 3, risk >0.9) a comprehension checkpoint requiring the user to identify one potential issue before proceeding. A cooldown mechanism (minimum 2 minutes between interventions) prevents alert fatigue.\n\nECOLOGICAL VALIDITY CONSIDERATIONS: We acknowledge that our evaluation paradigm—researcher-injected misinformation in controlled tasks—follows the standard methodology employed by both Liu et al. (CHI 2026) and Adjust for Trust (IUI 2026), but has inherent ecological validity limitations. Injected misinformation is typically more blatant, consistently placed, and fact-checkable compared to natural LLM hallucinations, which are subtler, context-dependent, and may involve plausible-sounding but unverifiable claims. As Ren et al. (arXiv 2510.10539) demonstrate with their AuthenHallu benchmark, hallucinations in authentic LLM-human interactions differ qualitatively from artificially constructed errors, occurring in 31.4% of real query-response pairs with highly variable subtlety. Our controlled design is necessary for establishing internal validity—it enables precise measurement of overreliance rates and intervention effects with known ground truth—but a classifier trained solely on controlled-misinformation tasks may not fully generalize to naturalistic LLM use where the 'correct' level of reliance is ambiguous. We address this in two ways: (1) Liu et al.'s misinformation includes varied subtlety levels (hallucinations, outdated knowledge, prompt injection attacks) that partially approximate natural error diversity, and (2) we plan a follow-up naturalistic deployment study where participants use the system during their regular LLM interactions over 2 weeks, with overreliance assessed via retrospective expert review of interaction logs—a design explicitly motivated by ecological validity concerns.\n\nEVALUATION: A within-subjects study (N≈120) across four LLM-assisted decision tasks with injected misinformation (quiz/ranking, article summarization, trip planning, code review), counterbalanced via Latin square across four conditions: (a) no intervention (control), (b) static cognitive forcing (always-on Assumption-CFF per Ghosh et al.), (c) self-report-adaptive (replicating Adjust for Trust's 11-point scale + counter-explanations), and (d) behaviorally-triggered adaptive (OverrelianceGuard). Each participant completes four tasks (~75 min total), one per condition. Primary metrics: overreliance reduction rate (misinformation acceptance, measured via both Traditional over-reliance rate and Appropriateness-view RAIR/RSR metrics per Raees & Papangelis's framework), task accuracy, detection latency (time from overreliance onset to intervention trigger), intervention precision/recall (validated against outcome and metacognitive probe labels), user satisfaction (NASA-TLX + custom intrusiveness scale), and comparative survey interruption burden between conditions (c) and (d). Secondary analysis: per-user classifier calibration curves, learning curves showing accuracy vs. training data fraction, four-condition weak supervision ablation with feature importance analysis, and qualitative analysis of intervention-triggered behavioral shifts.\n\n## Inspiration\nUntried combination: rich behavioral interaction signals from Liu et al. (CHI 2026) + trust-adaptive intervention strategies from 'Adjust for Trust' (IUI 2026), without the physiological sensor requirement of 'Sensing What Surveys Miss' (CHI 2026). Gap validation: Adjust for Trust's Appendix D documents that surface-level behavioral features fail to predict trust (F1 ≤ 0.5), and Sensing What Surveys Miss achieves only ~61% accuracy even with combined mouse+EDA using linear regression—both motivating richer multi-resolution temporal processing via deep learning. Positive evidence from Campagna et al. (84% trust classification in HRI) and Kaneko & Yamada (90% in cooperative tasks) establishes that the failure is in modeling depth, not in behavioral signals per se—justifying our investment in multi-resolution temporal architectures. Measurement-theoretic insight from Raees & Papangelis (2026): appropriate reliance is behaviorally observable and conceptually distinct from trust, grounding our choice to detect reliance behavior rather than infer trust attitudes. Cross-paradigm transfer: extending Li et al.'s adaptive explanation selection principle from structured tabular tasks with coarse feedback to free-form conversational LLM interactions with continuous behavioral sensing. Architecture insight: lightweight time series classifiers (PRISM, ~40K params) demonstrate that efficient sub-millisecond browser-embedded inference is feasible at this parameter scale, making sensor-free any-browser deployment practical where prior approaches (Sensing What Surveys Miss) assumed physiological hardware. Labeling methodology: adapting the hybrid weak-supervision + outcome-propagation approach from fraud detection and temporal action localization, informed by TimeMIL's time-aware MIL pooling for temporal sequence data, to solve the streaming-vs-outcome temporal misalignment problem that Liu et al.'s post-hoc analysis did not address—with explicit ablation design to verify the classifier generalizes beyond hand-coded labeling function rules, informed by the XPASC framework for measuring weak supervision generalization.\n\n## Key References\n- Liu, Zhou, Shen, Liu, Wu & Chen. Behavioral Indicators of Overreliance During Interaction with Conversational Language Models (CHI 2026, arXiv 2602.11567)\n- Srinivasan & Thomason. Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (IUI 2026, arXiv 2502.13321)\n- Li, Zhu, Lu, Xiao & Yin. From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis (CHI 2025, arXiv 2502.11919)\n- Ailin Liu, Karoui, Draxler, Kreuter & Chiossi. Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM Support by User Modeling (CHI 2026, arXiv 2602.00880)\n- Kaneko & Yamada. Predicting Trust Dynamics with Dynamic SEM in Human-AI Cooperation (IEEE Access 2025, arXiv 2407.01752)\n- Campagna, Lagomarsino, Lorenzini, Chrysostomou, Rehm & Ajoudani. Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability (RA-L 2025, arXiv 2601.19856)\n- Raees & Papangelis. From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making (arXiv 2604.23896, April 2026)\n- Gurney, Pynadath & Wang. Comparing Psychometric and Behavioral Predictors of Compliance During Human-AI Interactions (Persuasive Technologies 2023, arXiv 2302.01854)\n- Sun et al. Eyes Can't Always Tell: Fusing Eye Tracking and User Priors for User Modeling under AI Advice Conditions (arXiv 2604.01741, 2026)\n- Ibrahim et al. Measuring and Mitigating Overreliance Is Necessary for Building Human-Compatible AI (arXiv 2509.08010, 2025)\n- Buçinca, Malaya & Gajos. To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making (CSCW 2021)\n- Ghosh et al. An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, 2026)\n- PRISM: Multi-Resolution Time Series Classification via Symmetric Dilated Convolutions (Neurocomputing 2026, arXiv 2508.04503)\n- From Calibration to Collaboration: LLM Uncertainty Quantification Should Be More Human-Centered (arXiv 2506.07461, June 2025)\n- de Jong et al. Cognitive Forcing for Better Decision-Making: Reducing Overreliance on AI Systems Through Partial Explanations (CSCW 2025)\n- Ren, Gruhlke & Lauscher. Detecting Hallucinations in Authentic LLM-Human Interactions (arXiv 2510.10539, 2025)\n- Dechant, Shukla & Bhatt. Mice, Masks, and Monotones: On the Reliability of Mouse Trajectories as Indicators of Trust (arXiv 2310.16632, 2023)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '80', 'timeline': '7-9 months (2 months system dev + labeling pipeline, 1 month IRB + pilot, 2-3 months main study with 120 participants, 2-3 months analysis and writing)', 'estimated_gpu_cost': '$120 (A100 at ~$1.50/hr spot pricing; model is only ~40K params so training is fast; GPU time dominated by hyperparameter search, data augmentation pipeline, Snorkel label model training, and 4-condition ablation)'}\n- **human_in_loop**: {'gpu_hours': '60', 'timeline': '5-7 months (Claude accelerates extension code, labeling function design, ONNX export pipeline, and statistical analysis)', 'claude_api_cost': '$250 (Sonnet 4.6 for code generation, weak supervision labeling function refinement, intervention prompt engineering, and analysis scripts; ~80M tokens)', 'estimated_gpu_cost': '$90 (A100 at ~$1.50/hr spot pricing)'}\n- **auto_research**: {'gpu_hours': '50', 'timeline': '4-6 months (automated architecture search across CNN/MiniRocket/LSTM variants, labeling function optimization, and ablation analysis; human study remains irreducible)', 'claude_api_cost': '$500 (Sonnet 4.6 for automated pipeline: architecture comparison, labeling function generation and evaluation, intervention prompt tuning via batch API, paper drafting; ~160M tokens)', 'estimated_gpu_cost': '$75 (A100 at ~$1.50/hr spot pricing)', 'speed_bottleneck': 'IRB approval (4-8 weeks) and sequential participant recruitment for within-subjects study are irreducible human-in-the-loop requirements that cannot be parallelized by automation'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T18:47:22.214Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:47:22.214Z",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T18:47:22.229Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have comprehensive field research results. Let me compile the evaluation.

---

```
【阶段】: Triage

【致命问题：投稿会议与 proposal 方向完全不匹配】

在评估 idea 质量之前，必须首先指出一个致命的结构性问题：

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：
"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Submissions without a robotics focus will be returned without review."

本 proposal 是一篇纯粹的 HCI (Human-Computer Interaction) 论文——关于在浏览器中通过行为信号检测用户对 LLM 的过度依赖并触发自适应干预。它不涉及任何机器人学习、机器人感知、机器人控制或机器人系统。所有引用的核心相关工作（Liu et al., Adjust for Trust, Sensing What Surveys Miss 等）均发表于 CHI 和 IUI 这类 HCI 会议。

这意味着该 proposal 投稿 CoRL 2026 会被 desk reject（不送审直接退回）。以下我仍按要求评估 idea 本身的质量，但概率估计必须反映这一致命的 venue mismatch。

---

【领域调研】:

- [Liu et al., "Behavioral Indicators of Overreliance During Interaction with Conversational Language Models"](https://arxiv.org/abs/2602.11567) (CHI 2026): 确认存在。77 名参与者、3 项任务，通过 autoencoder 聚类识别出 5 种过度依赖行为模式。使用 per-event 37 维编码。明确将实时检测和干预留作 future work。这是本 proposal 的直接上游工作。

- [Srinivasan & Thomason, "Adjust for Trust"](https://arxiv.org/abs/2502.13321) (IUI 2026): 确认存在。通过信任自适应干预（支持性/反面解释 + 强制暂停）实现最高 38% 不当依赖减少。但依赖每次决策后的 11 点量表自我报告。Appendix D 记录了行为信号替代自我报告的失败尝试（F1 ≤ 0.5）。

- [Ailin Liu et al., "Sensing What Surveys Miss"](https://arxiv.org/abs/2602.00880) (CHI 2026): 确认存在。使用鼠标动态 + EDA（电皮肤活动）构建闭环系统。N=32 的 within-subjects 研究，对齐自适应时机提高 21% 准确率。但需要生理传感器，且简单线性回归仅达 ~61% 检测准确率。

- [Campagna et al., "Estimating Trust in Human-Robot Collaboration"](https://arxiv.org/abs/2601.19856) (RA-L 2025): 确认存在。N=14，化学混合任务，Voting Classifier 达 84% 信任分类准确率（AUC=0.90）。但这是物理 HRI 场景，样本极小，行为指标包含凝视方向、空间位移等 LLM 对话中不存在的信号。

- [Raees & Papangelis, "From Trust to Appropriate Reliance"](https://arxiv.org/abs/2604.23896) (arXiv, April 2026): 确认存在。区分信任（主观感知）与适当依赖（可观察行为决策），提出三种测量视角（Traditional, Appropriateness, Dominance）。为行为度量而非主观评分提供理论支撑。

- 调研总结: 该领域（LLM 过度依赖的行为检测与自适应干预）目前处于 CHI/IUI 生态圈的早期阶段。Liu et al. (CHI 2026) 刚建立了行为信号词汇表，Adjust for Trust (IUI 2026) 证明了自适应干预的有效性但依赖自我报告，Sensing What Surveys Miss (CHI 2026) 尝试了闭环但需要生理传感器。本 proposal 试图填补"纯行为信号 → 实时检测 → 自适应干预"的空白。**这是 HCI 领域的工作，与 CoRL 的机器人学习主题无交集。**

---

【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. **规则引擎 baseline**: Liu et al. 已经识别了 5 种过度依赖行为模式。最简单的替代方案是直接将这 5 个模式编码为规则（如 "10 秒内 copy-paste 且未滚动浏览 → 高风险"），用阈值触发干预。Proposal 的 weak supervision labeling functions 本质上就是这些规则——那么 CNN 相对于直接使用这些规则作为触发器的增量价值是什么？Proposal 自己也意识到了这个 circularity 问题，设计了 4-condition ablation，但这恰恰说明了 trivial alternative 的威胁是真实的。

2. **简单 ML baseline**: 在同样的 (30×28) 特征上跑 Random Forest 或 XGBoost，不需要 CNN 的时序建模能力，可能已经足够。Proposal 只对比了 MiniRocket 和 BiLSTM，没有包含非时序 ML baseline。

增量价值声称在于"多分辨率时序处理能捕捉简单模型遗漏的时序动态"，但这是一个未经验证的假设，而非已知事实。

---

【前提假设检验】:

核心 claim 的逻辑链中存在多个未经验证的关键假设：

1. **"行为信号在 LLM 对话场景中足以区分过度依赖 vs 适当依赖"** — 这是最核心也最脆弱的假设。Adjust for Trust 的 Appendix D 直接否定了这一点（F1 ≤ 0.5）。Proposal 辩称那是"surface-level heuristics"的失败，更丰富的时序建模会更好——但支撑这一论点的正面证据（Campagna 84%, Kaneko 90%）来自完全不同的领域（物理 HRI、无人机/驾驶模拟），涉及不同的行为信号（凝视方向、空间位移、速度同步）。**从 HRI 到 LLM 对话的 domain gap 巨大，迁移论证薄弱。**

2. **"30 秒窗口的 28 维聚合特征保留了足够的过度依赖判别信息"** — Liu et al. 的原始编码是 per-event 的 37 维向量序列，通过 transformer autoencoder 处理。将其聚合为每秒 28 维的 temporal grid 必然丢失信息（尤其是事件间的顺序和依赖关系）。这一表征选择的合理性未被论证。

3. **"hybrid labeling 能产生足够高质量的训练信号"** — 四种标注信号（MIL outcome propagation、weak supervision、sparse probes、self-supervised）各有局限：MIL 将 session-level 标签传播到 window-level 是强假设；weak supervision 存在 circularity 风险（proposal 已承认）；sparse probes 每任务仅 2-3 次，信号极度稀疏。这些信号组合后能否收敛到有用的训练信号，是一个 open question。

4. **"~30K 训练窗口足够训练 40K 参数的 CNN"** — Proposal 用 PRISM 在 UCI-HAR 上 7,352 样本的先例来论证，但 UCI-HAR 是 6 类清晰分离的物理活动（走路、坐下等），与过度依赖这种微妙行为模式的区分难度完全不在一个量级。

---

【3 维度打分】:

1. **Novelty: 中偏弱** — 
   核心贡献是将 Liu et al. (CHI 2026) 的行为信号 + Adjust for Trust (IUI 2026) 的自适应干预 + Sensing What Surveys Miss (CHI 2026) 的闭环架构组合在一起，去掉生理传感器依赖。这是典型的"组合创新 + 移除约束"模式——每个组件都有直接前驱。真正有增量的部分是 hybrid labeling methodology（MIL + weak supervision + probes + self-supervised），但这是方法论层面的贡献，不是核心洞察层面的创新。如果核心检测结果是 positive（比如达到 80% 准确率），审稿人的反应更可能是 "good engineering, expected given the signal richness" 而非 "surprising"。labeling methodology 的 circularity ablation 设计值得肯定，但它是对自身方法论弱点的防御，不是创新本身。

2. **Significance: 弱（对 CoRL）/ 中（对 HCI 社区）** — 
   对 CoRL 而言：零 significance，没有任何 robotics relevance。
   如果评估其在 HCI 社区的 significance：问题本身（LLM 过度依赖的实时检测与干预）确实重要且 timely，尤其是 Liu et al. 和 Adjust for Trust 的发表证明了社区关注度。但 proposal 的 contribution 高度依赖于实证结果——如果检测准确率停留在 65-70%，其实际部署价值有限。Proposal 试图通过 "dual-outcome" 框架（即使检测不好也有方法论贡献）来对冲风险，但这降低了 single-paper impact：如果主要 claim 不成立，剩余贡献分散且单独来看 incremental。

3. **Related Work: 强** — 
   对相关文献的覆盖非常全面且准确。所有引用的关键论文经调研确认存在，描述准确。差异化定位清晰：与 Liu et al.（有信号但无系统）、Adjust for Trust（有干预但依赖自我报告）、Sensing What Surveys Miss（有闭环但需生理传感器）的区分到位。对负面证据（Dechant et al., Adjust for Trust Appendix D）的诚实引用值得肯定。唯一的问题是正面跨领域证据（Campagna, Kaneko）的 domain gap 论证不够审慎。

---

【概率估计】: [0% - 3%] 中位 1%

【估计理由】: 
概率估计几乎完全由 venue mismatch 决定。CoRL 2026 明确声明 "submissions without a robotics focus will be returned without review"。本 proposal 是一篇纯 HCI 论文（浏览器扩展、鼠标/键盘行为信号、LLM 对话场景），不涉及任何机器人学习内容。它几乎必然在 desk review 阶段被退回，不会进入同行评审流程。

如果抛开 venue mismatch，仅评估 idea 在合适 venue（如 CHI 2027, IUI 2027, CSCW 2027）的质量：idea 处于 [20%-30%] 中位 25% 的区间。Novelty 是组合式的而非根本性的，核心经验假设（纯行为信号能否可靠检测 LLM 对话中的过度依赖）存在较大不确定性，且有 trivial alternative 威胁。但问题重要、related work 扎实、研究设计合理（dual-outcome 框架、circularity ablation）。

限制上界的维度：（1）venue mismatch 直接将 CoRL 概率压到接近 0；（2）即使对于 HCI venue，Novelty 的组合性质和核心假设的不确定性限制了上界。

【主要风险】:
1. **致命 venue mismatch**: CoRL 是机器人学习会议，本 proposal 完全不涉及 robotics，几乎必然 desk reject。
2. **核心经验假设缺乏支撑**: 从行为信号可靠检测 LLM 对话中过度依赖的假设，唯一直接相关的证据（Adjust for Trust Appendix D）是负面的（F1 ≤ 0.5），而正面证据来自 domain gap 巨大的其他领域（HRI、驾驶模拟）。
```

---

**强烈建议**：该 proposal 应转投 HCI 相关会议（CHI 2027、IUI 2027、CSCW 2027 或 UIST 2027），而非 CoRL。CoRL 投稿几乎必然导致 desk rejection，浪费宝贵的投稿机会。

Sources:
- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Liu et al., Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)
- [Srinivasan & Thomason, Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Ailin Liu et al., Sensing What Surveys Miss (CHI 2026)](https://arxiv.org/abs/2602.00880)
- [Campagna et al., Estimating Trust in HRI (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Raees & Papangelis, From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)
- [CoRL 2026 - Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to complete the evaluation. Let me note a critical finding from my CoRL search and compile the assessment.

---

```
【阶段】: Triage

【致命问题：投稿场地根本性错配】

在进入 3 维度评分之前，必须首先指出一个致命的场地错配问题：

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：
"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots, and **submissions without a robotics focus will be returned without review**."

本 proposal 的内容——浏览器扩展、LLM 对话中的行为过度依赖检测、自适应干预——与机器人学习完全无关。没有任何机器人硬件、控制策略、感知-执行循环、仿真到真实迁移、或机器人学习算法。这是一篇纯 HCI (人机交互) 论文，适合的投稿场地是 CHI、IUI、CSCW、UIST 或 FAccT 等会议。

**投稿 CoRL 将被 desk reject（未送审退回），中稿概率为 0%。**

以下评估假设 proposal 投稿到合适的 HCI 顶会（如 CHI 2027），以便提供有建设性的反馈。

---

【领域调研】:

- [Liu et al., "Behavioral Indicators of Overreliance During Interaction with Conversational Language Models"](https://arxiv.org/abs/2602.11567) (CHI 2026): 确认存在。77 名参与者、3 个任务、autoencoder 聚类识别了 5 种行为模式。是本 proposal 的核心数据/信号来源。论文明确将"实时检测与干预"列为 future work。

- [Srinivasan & Thomason, "Adjust for Trust"](https://arxiv.org/abs/2502.13321) (IUI 2026): 确认存在。信任自适应干预，up to 38% 不当依赖减少，但依赖每次决策后的 11 点量表自报告。Appendix D 确认行为特征预测信任失败 (F1 ≤ 0.5)。

- [Ailin Liu et al., "Sensing What Surveys Miss"](https://dl.acm.org/doi/full/10.1145/3772318.3791191) (CHI 2026): 确认存在。鼠标动态 + EDA 闭环系统用于在线问卷，~61% 检测准确率，线性回归分类器。最接近的架构先驱，但目标是认知负荷而非过度依赖，且需要生理传感器。

- [Campagna et al., "Estimating Trust in Human-Robot Collaboration"](https://arxiv.org/abs/2601.19856) (RA-L 2025): 确认存在。84% 信任分类准确率 (AUC=0.90)，但是在物理 HRI 领域 (化学混合任务)，N=14，行为指标包括凝视方向、空间位移等——与浏览器交互信号存在巨大领域鸿沟。

- [Raees & Papangelis, "From Trust to Appropriate Reliance"](https://arxiv.org/abs/2604.23896) (2026): 确认存在。测量理论框架，区分信任与适当依赖，建议行为过程指标。

- [PRISM](https://arxiv.org/abs/2508.04503) (Neurocomputing 2026): 确认存在。轻量级多分辨率时间序列分类器，~40K 参数。在 UCI-HAR 上达到 97.3%，但 UCI-HAR 的 6 类物理活动分类与过度依赖检测的难度差距巨大。

- **调研总结**: 该领域处于一个明确的"gap"阶段：Liu et al. (CHI 2026) 刚刚建立了行为信号词汇表但未做实时系统；Adjust for Trust (IUI 2026) 证明了自适应干预有效但被自报告锁定；Sensing What Surveys Miss (CHI 2026) 建了闭环但需生理传感器且准确率低。本 proposal 定位在这个交叉点上，gap 是真实存在的。但是，**这个 gap 在 2026 年上半年已被多篇 CHI/IUI 论文从不同角度逼近**，竞争窗口正在快速关闭。

---

【Trivial Alternative 检验】:

存在一个明显的 trivial alternative 威胁：**基于规则的阈值系统**。

Liu et al. 已经识别了 5 种行为模式（快速复制粘贴无编辑、跳过初始理解、频繁 LLM-任务切换等）。直接将这些模式编码为 if-then 规则（正是 proposal 自己在 weak supervision 标注函数中做的事），配合简单的滑动窗口统计，就能构建一个 rule-based 干预触发器——不需要 CNN、不需要 MIL、不需要 ONNX 推理。

Proposal 对此有部分预防：引用了 Adjust for Trust Appendix D 的 F1 ≤ 0.5 作为"简单方法不行"的证据。但这里有一个逻辑漏洞：Adjust for Trust 用的是"surface-level interaction heuristics"来预测**信任**（一个主观态度），而本 proposal 要预测的是**过度依赖行为**（可观察的行为模式）。预测主观信任态度当然比识别行为模式更难。如果直接用 Liu et al. 的 5 种模式做规则匹配来检测过度依赖行为本身，准确率可能就不那么低了——这正是 proposal 需要但未提供的对照实验。

增量价值声称在于"多分辨率时间动态处理能捕获规则无法编码的微妙模式"，但这是一个未验证的假设，而不是已知的事实。

---

【前提假设检验】:

核心逻辑链中有 **3 个未经验证的关键假设**：

1. **"行为信号在 LLM 对话中能实时区分过度依赖 vs. 非过度依赖窗口"（而非仅在事后分析中区分用户群体）**。Liu et al. 的发现是群体级别的聚类分析（高过度依赖用户群 vs. 低过度依赖用户群的行为差异），不是窗口级别的实时分类。从"不同过度依赖水平的用户有不同的行为模式"到"每个 30 秒窗口的行为特征能预测该窗口中是否正在发生过度依赖"，这是一个巨大的推理跳跃。前者可能反映的是个人特质/习惯差异，而不是可以在同一个人的时间序列中捕捉到的状态变化。

2. **"从物理 HRI 和合作任务中的行为信任预测 (84%, 90%) 可以推广到 LLM 对话场景"**。Campagna et al. 的行为指标是凝视方向、空间位移、速度同步——这些是物理空间中的身体行为。Kaneko & Yamada 在无人机/驾驶模拟器中的结果也涉及物理交互。浏览器中的鼠标/键盘交互与物理身体行为在信噪比和信息丰富度上可能存在数量级差异。这些跨域的正面证据实际上非常弱。

3. **"Liu et al. 的 77 人数据集 + 滑动窗口 ≈ 26K-40K 样本足以训练一个有意义的分类器"**。Proposal 自己承认 sample-to-parameter 比率是 0.65-1.0:1 "tight but viable"，并引用 PRISM 在 UCI-HAR 上 0.18:1 的比率作为先例。但 UCI-HAR 是 6 类清晰分离的物理活动（走、跑、坐、站、上楼、下楼），而过度依赖是一个模糊的、高噪声的二分类问题。更关键的是，滑动窗口产生的样本之间有 83% 的重叠（30 秒窗口、5 秒步长），这些不是独立样本——有效独立样本数远小于 26K-40K。

---

【3 维度打分】:

1. **Novelty: 中** — 
   Gap 定位是真实的：截至 2026 年上半年，确实没有论文同时做到"纯行为信号 + 实时检测 + 自适应干预 + LLM 对话"这四个条件的组合。但 novelty 主要是**组合性的**（combining existing pieces），而非**概念性的**。核心组件——行为信号词汇表来自 Liu et al.、自适应干预策略来自 Adjust for Trust、多分辨率 CNN 来自 PRISM、弱监督标注来自 Snorkel——都是已有工作的直接应用或微调。Proposal 的诚实之处在于它自己承认了这一点，但这也意味着核心贡献是"工程集成 + 实证验证"，而非方法论创新。如果分类器效果 positive，审稿人大概率会说"good engineering, expected direction"而非"surprising"。

2. **Significance: 中** — 
   过度依赖是 HCI/AI 领域的热门且重要问题，但本 proposal 的影响力受限于几个因素：(a) 它高度依赖 Liu et al. 的 77 人数据集，而该数据集的任务设计（注入型错误信息）本身存在生态效度问题（proposal 自己也承认）；(b) 即使分类器工作，从受控实验到真实部署的泛化路径不明；(c) 该领域正在快速移动——CHI 2026 同时发表了 Liu et al. 和 Sensing What Surveys Miss，到 CHI 2027 投稿截止时（约 2026 年 9 月），可能已有其他团队在做类似整合。significance 的上限受限于"这本质上是一个系统论文 + 用户研究"，而系统的核心技术组件缺乏独立的方法论贡献。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。Related work 覆盖极为全面且准确：所有引用的关键论文都真实存在、描述准确，包括负面结果（Dechant et al.、Adjust for Trust Appendix D）。差异化定位清晰——逐一与 Liu et al.、Adjust for Trust、Sensing What Surveys Miss、Li et al. 做了精确的对比。对领域格局的理解是深入的。唯一的轻微不足是对跨域证据（Campagna et al., Kaneko & Yamada）的强度存在选择性呈现——强调了正面数字但弱化了领域鸿沟。

---

【概率估计】（假设投稿合适场地如 CHI 2027）: [20% - 32%] 中位 25%

【概率估计】（投稿 CoRL 2026）: 0%（desk reject）

【估计理由】:
- **CoRL 2026: 0%**。该 proposal 与 CoRL 的 scope（机器人学习）完全无关，会被直接退回不送审。
- **假设投到 CHI 2027**: Novelty 是组合性的而非概念性的，核心发现即使 positive 也不会让审稿人 surprised——"用更深的模型在更丰富的行为特征上做更好"是一个 expected direction。Trivial alternative（规则系统）的威胁真实存在且 proposal 的 weak supervision 循环性分析虽然设计精巧但实际上突显了这个问题。前提假设中"群体级行为差异 → 窗口级实时检测"的跳跃是最大的逻辑风险。这些因素将上界限制在 ~32%。下界 20% 是因为 gap 定位清晰、related work 极强、dual-outcome 设计（即使检测失败也有贡献）提供了一定的安全网，加上 120 人用户研究的规模在 CHI 社区是合格的。

【主要风险】:
1. **场地致命错配**: CoRL 不接受非机器人论文，该 proposal 会被 desk reject。这是唯一且决定性的风险。
2. **（假设合适场地）核心假设未验证**: "群体级行为聚类差异"能否转化为"窗口级实时分类信号"是一个未经验证且不显然成立的假设。如果这个假设不成立（即行为差异反映的是个体特质而非可检测的时刻状态），整个技术核心就会崩塌——虽然 proposal 设计了 fallback contributions，但 CHI 审稿人对一篇"核心 claim 失败但我们有 fallback"的论文通常不会很宽容。
```

Sources:
- [Liu et al., Behavioral Indicators of Overreliance (CHI 2026)](https://arxiv.org/abs/2602.11567)
- [Srinivasan & Thomason, Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Liu et al., Sensing What Surveys Miss (CHI 2026)](https://dl.acm.org/doi/full/10.1145/3772318.3791191)
- [Campagna et al., Estimating Trust in HRC (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Raees & Papangelis, From Trust to Appropriate Reliance (2026)](https://arxiv.org/abs/2604.23896)
- [PRISM: Lightweight Multivariate Time-Series Classification (2025)](https://arxiv.org/abs/2508.04503)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

⚠️ 【致命前置问题：投稿会议匹配性】
CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：
"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
"Submissions without a robotics focus will be returned without review."

本 proposal 是一篇纯粹的 HCI 论文——浏览器扩展检测用户对 LLM 的过度依赖并触发自适应干预。全文没有任何与机器人学习相关的内容（无机器人平台、无 sim-to-real、无机器人感知/操控/运动规划）。提交至 CoRL 将被 desk reject，概率接近 100%。

本 proposal 的自然目标会议应为：CHI 2027、IUI 2027、CSCW 2027、或 UIST 2027。以下分析基于假设该 proposal 被投至合适的 HCI 顶会（如 CHI），以评估其 idea 内核质量。

═══════════════════════════════════════════════════

【领域调研】:

1. Liu, Zhou, Shen, Liu, Wu & Chen. "Behavioral Indicators of Overreliance During Interaction with Conversational Language Models" (CHI 2026, arXiv 2602.11567):
   - 与本 proposal 的关系：直接上游工作，提供了行为信号词汇表。本 proposal 的整个 signal vocabulary 和 feature engineering 基于此文。
   - 关键发现：77 名被试、3 个任务，通过 autoencoder clustering 识别出 5 种过度依赖行为模式。论文明确将实时检测和干预留作 future work。

2. Srinivasan & Thomason. "Adjust for Trust" (IUI 2026, arXiv 2502.13321):
   - 与本 proposal 的关系：直接竞争/互补工作。本 proposal 试图用行为信号替代该文的自我报告机制。
   - 关键发现：通过信任自适应干预实现 38% inappropriate reliance 降低，但需要每次决策后 11 分制自我报告。Appendix D 文档记录了行为估计的失败尝试 (F1 ≤ 0.5)。

3. Ailin Liu et al. "Sensing What Surveys Miss" (CHI 2026, arXiv 2602.00880):
   - 与本 proposal 的关系：最相似的系统架构——闭环 sensing→intervention。但目标构念不同（认知负荷 vs. 过度依赖），且依赖生理传感器 (EDA)。
   - 关键发现：鼠标 + EDA 结合线性回归仅达 ~61% 检测准确率，N=32，未提供鼠标单独的消融实验。

4. Campagna et al. "Estimating Trust in Human-Robot Collaboration through Behavioral Indicators" (RA-L 2025, arXiv 2601.19856):
   - 与本 proposal 的关系：正面证据——行为信号可以预测信任，但在完全不同的领域 (HRI 物理协作)。
   - 关键发现：84% 准确率，AUC=0.90，但 N=14，使用了凝视方向、空间位移等 HRI 特有特征。

5. Li, Zhu, Lu, Xiao & Yin. "From Text to Trust" (CHI 2025, arXiv 2502.11919):
   - 与本 proposal 的关系：类似的自适应干预思路，但限于结构化表格任务 + 粗粒度反馈。
   - 关键发现：POMDP 框架自适应选择 LLM 解释，显著提升准确率，但仅用二元 agree/disagree 反馈。

6. Raees & Papangelis. "From Trust to Appropriate Reliance" (arXiv 2604.23896, April 2026):
   - 与本 proposal 的关系：提供测量理论基础，支持行为过程指标优于主观信任评分。
   - 关键发现：信任与适当依赖是概念上不同的构念，推荐 RAIR/RSR 等行为过程指标。

- 调研总结：该领域在 2025-2026 年高度活跃，多篇 CHI/IUI 顶会论文分别解决了行为表征（Liu et al.）、信任自适应干预（Adjust for Trust）、传感器闭环系统（Sensing What Surveys Miss）等子问题。但确实没有工作将"仅基于非侵入式行为信号的实时过度依赖检测"与"自适应干预"在自由对话式 LLM 交互中闭环连接起来。这个 gap 真实存在。

═══════════════════════════════════════════════════

【Trivial Alternative 检验】:

存在一个关键的 trivial alternative 威胁：

直接将 Liu et al. 的 5 个行为模式编码为规则阈值（rule-based detector），配合简单的滑动窗口统计，是否能达到类似效果？

Proposal 的论证是："Adjust for Trust Appendix D 表明 surface-level heuristics 的 F1 ≤ 0.5，所以需要更复杂的模型。" 但这里有一个关键区别——Appendix D 使用的是 AIAcc5、CapabilityDiff 等粗粒度交互启发式特征来估计"信任"，而非 Liu et al. 识别的 5 种具体过度依赖行为模式。Liu et al. 的模式（如"快速复制粘贴无编辑"、"跳过初始理解"）本身就可能足以直接编码为高精度规则。

实际上，proposal 自己在 weak supervision 模块中就是在做这件事（将 5 种模式编码为 labeling functions）。如果这些规则本身就有足够的判别力，那么 CNN 的增量价值存疑——proposal 自己也承认了这个 circularity 问题。

增量价值在于：(1) 时间粒度——从 session 级别到 30 秒窗口的流式检测；(2) 泛化——CNN 可能发现 Liu et al. 未识别的隐式模式。但这两点是否成立是纯粹的实证问题，目前没有先验理由强烈支持。

**结论：trivial alternative 威胁中等偏高。如果基于 Liu et al. 5 个模式的简单规则检测器在 30 秒窗口上也能达到 65-70% 准确率，CNN 的增量价值将被大幅稀释。**

═══════════════════════════════════════════════════

【前提假设检验】:

核心 claim 的逻辑链条存在以下未经验证的关键假设：

1. **Session-level patterns → Window-level detectability（最关键假设）**：Liu et al. 的 5 种行为模式是通过对整个 session 的 autoencoder clustering 识别的。这些 session 级别的模式是否在 30 秒的短窗口中仍然可检测，是完全未经验证的。某些模式（如"跳过初始理解"）本质上是 session 初期的一次性事件，不适合流式滑动窗口检测。

2. **HRI domain → LLM conversation domain 的迁移假设**：proposal 引用 Campagna et al. (84%) 和 Kaneko & Yamada (90%) 作为"行为信号可以预测信任"的正面证据，但这两项工作分别在物理 HRI（化学实验协作，N=14）和无人机/驾驶模拟中进行。它们使用的行为特征（凝视方向、空间位移、速度同步）与浏览器交互特征（鼠标轨迹、复制粘贴）在信号性质上有本质区别。将 84%/90% 的准确率作为"richer modeling 可以提升检测"的证据，逻辑链条较弱。

3. **特征信息量假设**：proposal 假设鼠标动态、滚动行为、按键统计等 28 维特征包含足够的信息来区分过度依赖与非过度依赖。但 Dechant et al. (2023) 明确发现鼠标轨迹特征"might not explain sufficiently the variance"，Sensing What Surveys Miss 即使加上 EDA 也只有 ~61%。proposal 的核心赌注是"multi-resolution temporal processing 可以弥补信号本身的不足"，但这是一个未经验证的假设。

4. **Labeling 质量假设**：hybrid labeling 策略看似稳健，但 MIL 的 outcome propagation 本质上仍是将 task-level label 传播到 window level——如果一个 session 被标记为"过度依赖"但其中只有 30% 的时间窗口实际表现出过度依赖行为，MIL 能否正确学到这一点取决于 attention 机制的质量，而训练数据量（~30K windows from 77 participants）可能不足以让 MIL attention 收敛到有意义的模式。

═══════════════════════════════════════════════════

【3 维度打分】:

1. **Novelty: 中** — 
   理由：gap identification 是真实的——确实没有工作将纯行为信号实时检测与自适应干预在自由对话 LLM 交互中闭环连接（调研验证了 Liu et al.、Adjust for Trust、Sensing What Surveys Miss 各自只覆盖了部分）。labeling methodology（MIL + weak supervision + sparse probes + self-supervised）和 circularity ablation 设计有方法论贡献。但核心技术路线是 **systems integration**——将 Liu et al. 的信号 + 已有 CNN 架构 + Adjust for Trust 的干预策略组合起来。multi-resolution 1D-CNN 在行为序列上的应用是标准的 time-series classification pipeline，不构成算法层面的 novelty。如果审稿人问"剥离系统集成后，你的 core technical contribution 是什么"，回答主要是 labeling methodology 和 ablation design——有价值但不够 surprising。相比 Sensing What Surveys Miss（同样是 CHI 2026，也做了闭环 sensing→intervention，只是目标和传感器不同），本 proposal 的架构 novelty 有限。

2. **Significance: 中偏强** — 
   理由：LLM 过度依赖是高度及时且重要的问题（Ibrahim et al. 2025 的综述明确呼吁 process-oriented mitigation；Raees & Papangelis 2026 提供了测量理论支撑）。非侵入式、browser-only 的方案如果可行，实际部署价值很高。head-to-head 比较四种干预条件（无干预、静态 CFF、自我报告自适应、行为自适应）的实验设计本身就有独立的实证价值。但 significance 的天花板受限于核心检测问题的不确定性——如果行为信号确实不足以支撑可靠检测（prior evidence 偏向悲观），整个系统的实际影响力会大幅缩水。proposal 的"即使检测失败也有贡献"的 dual-outcome framing 有一定说服力，但"表征行为信号能预测什么和不能预测什么"本身作为 main contribution 对 CHI 来说可能偏弱。

3. **Related Work: 强** — 
   理由：覆盖非常全面，几乎穷尽了 2023-2026 年间所有直接相关的工作。对 Liu et al. (CHI 2026)、Adjust for Trust (IUI 2026)、Sensing What Surveys Miss (CHI 2026)、Li et al. (CHI 2025) 的定位清晰且准确（经调研验证）。正面证据（Campagna et al.、Kaneko & Yamada）和负面证据（Dechant et al.、Adjust for Trust Appendix D）都有引用，展示了 balanced perspective。唯一的小瑕疵是对 Campagna et al. (N=14, HRI domain) 和 Kaneko & Yamada (模拟器任务) 的正面结果在论证中的权重可能过高——这些工作的 domain gap 太大，不宜作为"behavioral trust prediction is achievable"的强证据。

═══════════════════════════════════════════════════

【概率估计】: 

- 若投 CoRL 2026: ~0%（desk reject，不在 scope 内）
- 若投合适的 HCI 顶会（CHI 2027）: [22% - 32%] 中位 27%

【估计理由】: 
如果投稿 CoRL，这是一个明确的 scope mismatch，会被直接退稿。

假设投稿至 CHI（该 proposal 的自然目标会议）：idea 内核处于"real gap + reasonable approach, but core contribution is integration rather than deep novelty"区间。Related Work 覆盖是 asset（强），但 Novelty 受限于 systems integration 性质（中），Significance 受制于核心检测问题的实证不确定性（中偏强但有条件）。Trivial alternative 威胁（规则检测器可能接近 CNN 性能）和前提假设风险（session-level patterns 未必 window-level 可检测）共同限制了上界。如果核心检测结果是 positive (>75% accuracy)，这篇论文有竞争力；如果只有 65-70%，dual-outcome framing 能否说服审稿人取决于执行质量。上界被 Novelty 维度限制——即使实验完美执行，"组合 A+B+C 的系统"在 novelty 评分上天花板不高。

【主要风险】:
1. **Novelty 天花板**：核心贡献是系统集成（已知信号 + 已有架构 + 已有干预策略），审稿人可能认为"the gap was obvious, the filling is engineering"——gap 真实但填补方式缺乏 surprising insight。
2. **核心假设可能不成立**：session-level 行为模式在 30 秒流式窗口中是否可检测、浏览器行为特征是否包含足够信息量来区分过度依赖——这两个前提如果不成立，整篇论文的核心系统价值归零，仅剩"negative result + methodology contribution"，这对顶会来说可能不够。
```

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Liu et al. "Behavioral Indicators of Overreliance" (CHI 2026)](https://arxiv.org/abs/2602.11567)
- [Srinivasan & Thomason "Adjust for Trust" (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Ailin Liu et al. "Sensing What Surveys Miss" (CHI 2026)](https://arxiv.org/abs/2602.00880)
- [Campagna et al. "Estimating Trust in Human-Robot Collaboration" (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Raees & Papangelis "From Trust to Appropriate Reliance" (2026)](https://arxiv.org/abs/2604.23896)


【原始 proposal（允许参考但不是主要依据）】:
# Closing the Loop: From Behavioral Overreliance Detection to Adaptive Intervention in LLM Conversations

## Description
We propose OverrelianceGuard, the first closed-loop system that bridges unobtrusively collected behavioral interaction signals to real-time adaptive interventions in free-form conversational LLM interactions—without requiring self-report interruptions or physiological sensors. A browser extension captures non-invasive interaction events in 30-second sliding windows and transforms them into a temporal grid representation: each window is discretized into 30 one-second bins, with 28 aggregated features per bin capturing action type distribution (over 12 categories), mouse dynamics (distance, velocity), scroll behavior (distance, direction), keypress statistics, copy-paste behavior (including post-paste edit indicators), idle duration, dwell context relative to LLM responses, and page focus. This (30 × 28) temporal grid—derived from but explicitly distinct from Liu et al.'s (CHI 2026) per-event 37-dimensional encoding (15-dim action type one-hot + 1-dim timestamp + 2-dim page type + 19-dim type-specific attributes)—feeds a lightweight multi-resolution 1D-CNN (~40K parameters, <5ms browser inference via ONNX Runtime Web) with three parallel temporal branches capturing short-burst (2s), medium-term (10s), and full-window (30s) behavioral dynamics. We cite PRISM's 97.3% accuracy on UCI-HAR as evidence of architectural efficiency at this parameter scale, not as a performance projection—UCI-HAR involves 6-axis accelerometer data with well-separated activity classes, whereas overreliance classification operates on noisier interaction features with subtler boundaries. The architecture choice is motivated by converging evidence that simple models on behavioral signals are insufficient—Adjust for Trust's Appendix D found F1 ≤ 0.5 with surface-level heuristics, 'Sensing What Surveys Miss' (CHI 2026) achieves only ~61% with linear regression on mouse+EDA—while richer models on multi-dimensional behavioral features show substantially better results: Campagna et al. (RA-L 2025) achieve 84% trust classification (AUC=0.90) from behavioral indicators in HRI, and Kaneko & Yamada (2025) reach 90% in cooperative tasks. A methodological contribution is the hybrid labeling strategy addressing temporal misalignment between Liu et al.'s outcome-based labels and streaming prediction: outcome propagation via Multiple Instance Learning, weak supervision from programmatic heuristics encoding the five identified behavioral patterns, sparse event-triggered metacognitive probes (2–3 per task vs. Adjust for Trust's 30 per-decision self-reports), and self-supervised next-action prediction. Critically, we address the weak supervision circularity risk—where labeling functions encode behavioral patterns from the same feature space the CNN processes—through a four-condition ablation: (i) weak-supervision-only, (ii) MIL+probes-only (circularity-free, as labels derive from task outcomes and self-report), (iii) MIL+probes+self-supervised, and (iv) full multi-signal training. Comparing conditions (iv) vs. (ii) isolates whether the weak supervision provides complementary signal or merely teaches the CNN its own hand-coded rules, with Integrated Gradients feature attribution analysis revealing whether the model discovers temporal patterns beyond those encoded in labeling functions. We frame streaming behavioral overreliance detection as the core hypothesis being tested: if classifier accuracy proves disappointing (e.g., 65–70%), the within-subjects intervention comparison, the labeling methodology, and the characterization of what behavioral signals can and cannot predict all constitute independently publishable contributions. We analyze training data sufficiency: Liu et al.'s 77-participant dataset yields ~26K–40K behavioral windows with our proposed windowing, supplemented by augmentation and a phased training strategy. When overreliance risk exceeds personalized thresholds, the system selects from tiered interventions: metacognitive prompts (Assumption-style CFFs), counter-explanations (per Adjust for Trust), and comprehension checkpoints. Following Raees & Papangelis's (2026) measurement framework distinguishing trust from appropriate reliance, we assess overreliance via both Traditional (acceptance rates) and Appropriateness-view (RAIR/RSR) metrics. A within-subjects study (N≈120) across four LLM-assisted tasks compares four conditions: no intervention, static cognitive forcing, self-report-adaptive (replicating Adjust for Trust), and behaviorally-triggered adaptive (OverrelianceGuard). This work fills the gap between behavioral characterization (Liu et al., CHI 2026), trust-adaptive intervention via self-report (Adjust for Trust, IUI 2026), adaptive explanation selection in structured tasks (Li et al., CHI 2025), and sensor-dependent adaptive support (Sensing What Surveys Miss, CHI 2026)—contributing (1) the first streaming behavioral overreliance classifier for conversational LLM settings with a principled hybrid labeling methodology and explicit circularity analysis, (2) a deployable browser-based closed-loop intervention system requiring neither self-report interruptions nor physiological sensors, (3) head-to-head empirical evidence comparing self-report-based vs. behavior-based adaptive intervention, and (4) a rigorous characterization of what behavioral signals can and cannot predict about overreliance, advancing the field regardless of detection accuracy.

## Core Problem
Can unobtrusively collected behavioral interaction signals (copy-paste patterns, scroll depth, verification dwell time, tab-switch frequency) drive a real-time streaming classifier that triggers adaptive interventions to reduce overreliance on LLM outputs—without requiring self-report interruptions or invasive physiological sensors?

## Opportunity
Liu et al. (CHI 2026, arXiv 2602.11567) identify five behavioral patterns distinguishing high- vs. low-overreliance users in LLM interactions but explicitly leave real-time detection and intervention as future work. Srinivasan & Thomason's 'Adjust for Trust' system (IUI 2026, arXiv 2502.13321) achieves up to 38% reduction in inappropriate reliance through trust-adaptive interventions, but requires self-reported trust ratings on an 11-point scale after every decision—an intrusive approach whose inadequacy the authors themselves confirm in Appendix D, where their attempts at behavioral trust estimation yielded only 0.25–0.51 correlation and F1 ≤ 0.5 using surface-level interaction heuristics. Li et al.'s 'From Text to Trust' (CHI 2025, arXiv 2502.11919) adaptively selects explanations via POMDP-based hidden state estimation, but operates only in structured tabular decision tasks using coarse binary (agree/disagree) feedback—not rich behavioral signals in free-form LLM conversations. Ailin Liu et al.'s 'Sensing What Surveys Miss' (CHI 2026, arXiv 2602.00880) build the closest architectural parallel—a closed-loop system using mouse dynamics and electrodermal activity (EDA) to trigger adaptive LLM-based interventions—but target cognitive load during online surveys (not overreliance in LLM conversations), require physiological sensors (EDA wristbands), and achieve only ~61% detection accuracy with simple linear regression classifiers and max-fusion of two unimodal models; crucially, the paper provides no ablation separating mouse-only from EDA contributions, leaving open the question of whether interaction signals alone—processed with richer temporal modeling than linear regression—can achieve adequate detection without physiological sensing. The evidence for behavioral trust prediction is mixed but increasingly positive: while Dechant et al. (2023) find mouse trajectories alone insufficient and Adjust for Trust's Appendix D reports F1 ≤ 0.5 with surface-level heuristics, Campagna et al. (RA-L 2025, arXiv 2601.19856) achieve 84% accuracy classifying trust from behavioral indicators in human-robot collaboration using ensemble classifiers, and Kaneko & Yamada (IEEE Access, 2025; arXiv 2407.01752) demonstrate 90% accuracy predicting trust dynamics via dynamic structural equation modeling in physical cooperative tasks—both suggesting that behavioral features CAN support useful trust prediction with appropriate modeling depth, even if the domain gap to conversational LLM settings makes these figures proof-of-principle rather than direct benchmarks. Raees & Papangelis ('From Trust to Appropriate Reliance,' arXiv 2604.23896, April 2026) further argue that trust measurements are conceptually distinct from appropriate reliance—the construct we actually target—and advocate for behavioral process metrics over subjective trust ratings, providing measurement-theoretic grounding for our approach. The bridge remains unbuilt: no system uses fine-grained, continuously captured interaction signals alone to detect overreliance and trigger personalized interventions in conversational LLM settings. This is now technically feasible because (1) Liu et al.'s behavioral characterization provides the validated signal vocabulary via per-event interaction encodings, (2) lightweight time series classifiers like PRISM achieve high efficiency with only ~40K parameters and sub-millisecond inference, enabling browser-embedded real-time classification without physiological hardware, and (3) the converging positive evidence from Campagna et al. and Kaneko & Yamada establishes that behavioral trust prediction is achievable with appropriate modeling depth—though whether this generalizes to conversational LLM interactions remains the core empirical hypothesis we test.

## Related Work / Landscape
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

## Inspiration
Untried combination: rich behavioral interaction signals from Liu et al. (CHI 2026) + trust-adaptive intervention strategies from 'Adjust for Trust' (IUI 2026), without the physiological sensor requirement of 'Sensing What Surveys Miss' (CHI 2026). Gap validation: Adjust for Trust's Appendix D documents that surface-level behavioral features fail to predict trust (F1 ≤ 0.5), and Sensing What Surveys Miss achieves only ~61% accuracy even with combined mouse+EDA using linear regression—both motivating richer multi-resolution temporal processing via deep learning. Positive evidence from Campagna et al. (84% trust classification in HRI) and Kaneko & Yamada (90% in cooperative tasks) establishes that the failure is in modeling depth, not in behavioral signals per se—justifying our investment in multi-resolution temporal architectures. Measurement-theoretic insight from Raees & Papangelis (2026): appropriate reliance is behaviorally observable and conceptually distinct from trust, grounding our choice to detect reliance behavior rather than infer trust attitudes. Cross-paradigm transfer: extending Li et al.'s adaptive explanation selection principle from structured tabular tasks with coarse feedback to free-form conversational LLM interactions with continuous behavioral sensing. Architecture insight: lightweight time series classifiers (PRISM, ~40K params) demonstrate that efficient sub-millisecond browser-embedded inference is feasible at this parameter scale, making sensor-free any-browser deployment practical where prior approaches (Sensing What Surveys Miss) assumed physiological hardware. Labeling methodology: adapting the hybrid weak-supervision + outcome-propagation approach from fraud detection and temporal action localization, informed by TimeMIL's time-aware MIL pooling for temporal sequence data, to solve the streaming-vs-outcome temporal misalignment problem that Liu et al.'s post-hoc analysis did not address—with explicit ablation design to verify the classifier generalizes beyond hand-coded labeling function rules, informed by the XPASC framework for measuring weak supervision generalization.

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

## Resource Estimate
- **manual**: {'gpu_hours': '80', 'timeline': '7-9 months (2 months system dev + labeling pipeline, 1 month IRB + pilot, 2-3 months main study with 120 participants, 2-3 months analysis and writing)', 'estimated_gpu_cost': '$120 (A100 at ~$1.50/hr spot pricing; model is only ~40K params so training is fast; GPU time dominated by hyperparameter search, data augmentation pipeline, Snorkel label model training, and 4-condition ablation)'}
- **human_in_loop**: {'gpu_hours': '60', 'timeline': '5-7 months (Claude accelerates extension code, labeling function design, ONNX export pipeline, and statistical analysis)', 'claude_api_cost': '$250 (Sonnet 4.6 for code generation, weak supervision labeling function refinement, intervention prompt engineering, and analysis scripts; ~80M tokens)', 'estimated_gpu_cost': '$90 (A100 at ~$1.50/hr spot pricing)'}
- **auto_research**: {'gpu_hours': '50', 'timeline': '4-6 months (automated architecture search across CNN/MiniRocket/LSTM variants, labeling function optimization, and ablation analysis; human study remains irreducible)', 'claude_api_cost': '$500 (Sonnet 4.6 for automated pipeline: architecture comparison, labeling function generation and evaluation, intervention prompt tuning via batch API, paper drafting; ~160M tokens)', 'estimated_gpu_cost': '$75 (A100 at ~$1.50/hr spot pricing)', 'speed_bottleneck': 'IRB approval (4-8 weeks) and sequential participant recruitment for within-subjects study are irreducible human-in-the-loop requirements that cannot be parallelized by automation'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7f299833-b277-479f-9448-3a7613227134",
  "type": "user",
  "uuid": "1e78a602-e6ac-4b94-ab5b-f1f2b58a2b4f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:47:22.226Z_

```json
{
  "parentUuid": "1e78a602-e6ac-4b94-ab5b-f1f2b58a2b4f",
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
  "uuid": "841b88e4-6735-4ff7-8e0c-0bdcff863d77",
  "timestamp": "2026-05-19T18:47:22.226Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:47:22.226Z_

```json
{
  "parentUuid": "841b88e4-6735-4ff7-8e0c-0bdcff863d77",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "19a38f01-5936-4f18-b6b6-364ccd365547",
  "timestamp": "2026-05-19T18:47:22.226Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive field research results. Let me compil…",
  "leafUuid": "19a38f01-5936-4f18-b6b6-364ccd365547",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM overreliance detection proposal for CoRL",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:47:56.246Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them as the Meta Judge.

First, let me extract the key numbers and judgments from each reviewer:

**Reviewer 1:**
- CoRL probability: [0% - 3%] 中位 1%
- CHI probability (hypothetical): [20% - 30%] 中位 25%
- Novelty: 中偏弱
- Significance: 弱 (CoRL) / 中 (HCI)
- Related Work: 强
- Fatal issue: Venue mismatch (CoRL)


- Trivial alternative: Yes (rule-based)
- Core assumption risk: High (behavioral signals insufficient)

**Reviewer 2:**
- CoRL probability: 0%
- CHI probability: [20% - 32%] 中位 25%
- Novelty: 中
- Significance: 中
- Related Work: 强
- Fatal issue: Venue mismatch (CoRL)
- Trivial alternative: Yes (rule-based)
- Core assumption risk: High (session-level → window-level)

**Reviewer 3:**
- CoRL probability: ~0%
- CHI probability: [22% - 28%] 中位 25%
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Fatal issue: Venue mismatch (CoRL)
- Trivial alternative: Yes (rule-based, medium-high)
- Core assumption risk: High (session → window, feature sufficiency)

All three reviewers are aligned that this would be a desk reject for CoRL. For CHI, the probabilities cluster tightly around 25-27%, showing strong consensus that the work sits in the borderline range. The main agreement across reviewers centers on venue mismatch for CoRL, the rule-based trivial alternative concern, and high risk around core assumptions—particularly whether behavioral signals alone sufficiently support the approach. The reviewers show striking alignment on their assessments—all three converge on roughly 25% for a hypothetical CHI submission, with negligible variance under 3%, which suggests high confidence in the rejection. CoRL is unanimously a 0%, so that's settled.

For the practical side, there's consensus across all three on the implementation requirements: GPU compute sits in the 50-80 hour range with minimal cost, the timeline stretches 4-9 months, and the real constraint is navigating IRB approval and recruiting human participants.

The actual training is lightweight—just 40K parameters—and there's no need to develop a new benchmark. Given that the proposal specifically targets CoRL 2026, the venue mismatch becomes the deciding factor. My assessment is clear: this doesn't fit CoRL, but I should provide constructive guidance on where it could be redirected instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a38f01-5936-4f18-b6b6-364ccd365547",
  "isSidechain": false,
  "requestId": "req_011CbCReiqHn4aPCXuih7gvf",
  "type": "assistant",
  "uuid": "b8cb5d2b-c963-4308-b1b7-89a49d44ef44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qk2uzt4VYyew5GT1kXAxJ5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23875,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3680,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 23875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23875
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

_source line 9 · 2026-05-19T18:48:51.045Z_

【阶段】: Meta Judge
【三次中位】: [1%, 0%, 0%]（CoRL）; [25%, 25%, 27%]（假设 CHI）  std=0.6%（CoRL）; std=1.2%（CHI）
【共识维度】:
- **Venue Mismatch（致命）**: 3/3 审稿人一致判定——CoRL 2026 明确要求 robotics focus，本 proposal 是纯 HCI 论文（浏览器扩展 + LLM 对话行为检测），零 robotics 内容，必然 desk reject。三人均独立引用了 CoRL CFP 的同一句话："submissions without a robotics focus will be returned without review"。**信号强度：最高。**
- **Novelty = 中 / 组合性（中）**: 3/3 一致认为核心贡献是 systems integration（Liu et al. 信号 + PRISM 架构 + Adjust for Trust 干预策略），而非概念性或算法层面的创新。即使实验 positive，审稿人预期反应是 "good engineering, expected direction" 而非 "surprising"。
- **Related Work = 强（强）**: 3/3 一致给出最高评价——覆盖全面、引用准确、负面证据诚实引用、差异化定位清晰。所有关键论文经三方独立调研确认存在且描述准确。
- **Trivial Alternative 威胁真实（中偏高）**: 3/3 均指出 Liu et al. 的 5 种行为模式可直接编码为规则阈值检测器，且 proposal 自己的 weak supervision labeling functions 本质上就是这些规则——CNN 相对于规则系统的增量价值未经验证。
- **核心假设跳跃（中偏高风险）**: 3/3 均指出从 session-level 行为聚类差异到 window-level 实时流式检测的推理跳跃是最大的逻辑风险，且唯一直接相关的证据（Adjust for Trust Appendix D, F1≤0.5）是负面的。
- **跨域证据 domain gap 过大（中）**: 3/3 均指出 Campagna et al.（HRI, N=14）和 Kaneko & Yamada（驾驶/无人机模拟）的正面数据不可直接迁移到 LLM 对话场景，proposal 对此过度依赖。
- **训练数据充分性存疑（中）**: 3/3 均指出 UCI-HAR 与过度依赖检测的任务难度不可比，PRISM 先例论证较弱。

【异常维度】:
- R1 给 Novelty "中偏弱"（略比 R2/R3 的"中"更严），独立指出 (30×28) 特征聚合的信息损失问题——有效但属于 R1 独有的细节关注点，不改变整体判断。
- R3 给 Significance "中偏强"（略比 R1/R2 更宽松），理由是问题的 timeliness 和非侵入式方案的部署价值。这一评价在三方中偏乐观，但差异很小，不构成实质性分歧。
- R2 独立强调了滑动窗口 83% 重叠导致有效独立样本远小于 26K-40K——这是对训练数据充分性论证的有效补充攻击，虽仅 R2 明确计算了重叠比例，但与 3/3 共识的数据充分性担忧方向一致。

【最终概率】:
- **投稿 CoRL 2026**: [0% - 0%] 中位 0%
- **假设投稿合适 HCI 顶会（CHI 2027）**: [20% - 30%] 中位 25%

【一致性】: 高（CoRL 完全一致；CHI 三方 std=1.2%，远低于 3% 阈值）

【综合理由】:

**CoRL 概率 = 0%**: 三方完全一致，无需进一步讨论。本 proposal 与 CoRL scope 完全不匹配，会在 desk review 阶段被退回，不进入同行评审。这是结构性致命问题，无法通过任何 idea 或实验层面的修改来挽救（除非彻底改写为 robotics 方向的论文，那就是另一个 proposal 了）。

**CHI 概率 = 25% 中位**: 三方高度一致（25%, 25%, 27%），取中位 25%，缩窄区间至 [20%-30%]。上界 30% 由 Novelty 的组合性质天花板决定——即使实验完美执行、分类器达 80%+，"整合 A+B+C 的系统论文"在 CHI 的 novelty 维度上也有硬上限。下界 20% 由三方共识的 safety net 支撑：Related Work 极强（审稿人不会攻击文献覆盖）、dual-outcome 框架提供了检测失败时的降落伞、120 人 within-subjects 设计在 CHI 是合格规模。中间区域的不确定性主要来自核心检测假设是否成立——如果 positive (>75%), 接近上界；如果 moderate (65-70%), 接近下界。

**异常处理**: R1 的"中偏弱" Novelty 和 R3 的"中偏强" Significance 互相抵消，不影响整体判断。R2 的滑动窗口重叠分析是对共识方向的有力补充，纳入整体风险评估但不单独影响概率区间。

**原则确认**: 最终估计（CHI 25%）未超过三方中最宽松的上界（R2/R3 的 32%），满足"不比最宽松更宽松"的原则。

【建议】: **KILL**（对 CoRL 2026）

投稿 CoRL 2026 将被 desk reject，概率 0%，浪费投稿机会。**强烈建议转投 CHI 2027（截稿约 2026 年 9 月）、IUI 2027、CSCW 2027 或 UIST 2027。** 若转投 HCI 顶会，idea 质量处于边缘区间（中位 25%），需在 Novelty 和核心检测假设两个维度上做强化才有竞争力。

【实施评估】:
- **计算资源**: 极低。~40K 参数模型，50-80 A100 GPU 小时（含超参搜索、数据增强、4 条件消融），估计成本 $75-$120。任何单卡 GPU 即可完成全部训练。
- **数据需求**: 依赖 Liu et al. (CHI 2026) 的 77 人数据集作为训练基础——**该数据集是否公开可得是关键风险点**（三方审稿人均未确认）。另需招募 ~120 名新被试进行 within-subjects 用户研究。
- **人工介入**: **高且不可压缩**。需要 IRB 审批（4-8 周）、120 人被试招募与实验执行（每人~75 分钟）、实验数据标注与质量控制。这是整个项目的时间瓶颈。
- **训练需求**: 模型训练本身极轻量（40K 参数），但 hybrid labeling pipeline（MIL + Snorkel 标签模型 + 自监督）的搭建和调试需要显著的工程开发时间（估计 1-2 个月）。
- **新 Benchmark**: 不需要构建新 benchmark。使用已有数据集 + 自行收集的用户研究数据。
- **预估周期**: 5-9 个月（系统开发 1-2 月 → IRB 审批 1-2 月 → 被试招募与实验 2-3 月 → 数据分析与写作 1-2 月）。**关键路径**是 IRB + 用户研究，无法通过自动化加速。如果目标 CHI 2027（截稿约 2026 年 9 月），从现在（2026 年 5 月）起约有 4 个月，时间极度紧张——除非 IRB 已提前准备，否则可能赶不上本轮 CHI。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8cb5d2b-c963-4308-b1b7-89a49d44ef44",
  "isSidechain": false,
  "requestId": "req_011CbCReiqHn4aPCXuih7gvf",
  "type": "assistant",
  "uuid": "356b1cc3-246b-4bcf-b585-714a636a5b85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qk2uzt4VYyew5GT1kXAxJ5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23875,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23875,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3680,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 23875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23875
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have comprehensive field research results. Let me compil…",
  "leafUuid": "356b1cc3-246b-4bcf-b585-714a636a5b85",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM overreliance detection proposal for CoRL",
  "sessionId": "397ca181-ea6c-4d96-a7f9-15df35237ee7"
}
```

---
