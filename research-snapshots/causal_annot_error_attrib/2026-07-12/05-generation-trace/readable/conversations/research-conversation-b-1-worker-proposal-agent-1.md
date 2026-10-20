# Research conversation: 【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。 【发掘 agent 本轮输出】: 【状态】: 有发掘空间 --- 【发掘点 1】 - 维度

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 6
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/5d084204-84fd-419f-8108-282337c3d172.jsonl`
- **Structured JSON:** [`d780ddb96e462f53d45e.json`](../../sessions/d7/d780ddb96e462f53d45e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:16:51.455Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:16:51.455Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "content": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\n【状态】: 有发掘空间\n\n---\n\n【发掘点 1】\n- 维度: novelty 锐化\n- 内容: 当前 proposal 的 primary contribution 定位为\"encoding-complexity curriculum 优于 flat augmentation 和 model-evolution curriculum\"。但这个 claim 的 surprise level 偏低——一个有经验的审稿人会说：\"当 attack difficulty 有 natural ordering 的时候，curriculum learning 优于 random ordering，这不是 curriculum learning 文献早就建立的结论吗？你只是把它搬到了 encoding domain。\" 真正 surprising 的结果是 **generalization to held-out encoding types**：如果 curriculum-ordered training 能泛化到 Braille/Morse 而 random-order training 和 flat augmentation 不能，这才是 non-trivial 的发现。建议 **将 generalization 提升为 primary contribution，将 curriculum design 降为 enabling mechanism**。重新 framing 为\"encoding-complexity curriculum teaches encoding-invariant harmful-content features that generalize to unseen encoding families\"，核心 claim 变成一个关于表征学习的发现（classifier 学到了 encoding-agnostic features），而非一个关于训练策略的工程选择。这样的 claim 审稿人更难用 \"I would have guessed this\" 来 dismiss。\n- 价值: 直接提升 Novelty 维度。将 paper 的核心贡献从\"已知原则的 domain-specific application\"提升为\"关于 adversarial robustness 中 feature learning 的 insight\"，天花板从 borderline 的 method paper 提升到有 conceptual contribution 的工作。\n\n【发掘点 2】\n- 维度: 前提假设质疑\n- 内容: Proposal 断言\"encoding difficulty is determined by structural properties (nesting depth, CPT-ratio preservation, cross-script mixing) rather than model-evolution differentials\"，但这个前提本身未经验证，且可能是错误的。Classifier 对不同 encoding 的实际 difficulty 可能主要由 **tokenizer behavior** 决定——同样是单层 encoding，base64 和 homoglyph substitution 的 tokenization pattern 差异巨大，对 classifier 而言 difficulty gap 可能远超 nesting depth 的影响。当前 2-stage curriculum 的分组逻辑（Stage 1 = single encoding, Stage 2 = composite）是一个**未经验证的 heuristic**，审稿人会问：\"你怎么知道 nesting depth 是 difficulty 的 right axis？如果按 tokenizer disruption degree 排序效果更好呢？\" 建议在 idea 层面引入一个 **formalized encoding complexity metric**（例如，综合 nesting depth、CPT deviation、tokenizer perplexity 的 composite score），并将 curriculum ordering 定义为沿这个 metric 的 progressive escalation。这不仅让 curriculum 有了 principled grounding，还直接强化了\"general principle\"的 claim——复杂度度量本身就是可迁移的方法论贡献。\n- 价值: 同时命中 Novelty 和 Significance。将 curriculum design 从 ad-hoc 2-stage heuristic 提升为 principled framework，挡住\"为什么是这个 ordering\"的审稿质疑，同时为 generalization claim 提供更强的理论支撑（如果 metric 能预测 held-out encodings 的 difficulty，这本身就是一个 finding）。\n\n【发掘点 3】\n- 维度: trivial alternative 威胁\n- 内容: Proposal 讨论了 rule-based canonicalization (TRYLOCK) 和 static CPT-Filtering (Broken-Token) 的局限性，但遗漏了一个更有力的 trivial alternative：**learned input canonicalization**。训练一个 seq2seq model（甚至一个轻量 encoder-decoder）将任意 encoded input 解码回 plaintext，然后喂给标准 guardrail classifier。这个 pipeline approach 不需要 curriculum learning，不需要 adversarial co-training，计算成本可能远低于 GRPO co-evolutionary loop。如果这个 simple baseline 效果接近，EncoGuard 的增量价值就很有限。Proposal 需要在 idea 层面明确论证为什么 **end-to-end encoding-robust classification** 优于 **canonicalization + standard classification** 的 pipeline——可能的论点包括：(a) canonicalization 是 error-propagating pipeline，decode 错误直接导致 classifier 失效；(b) 对 adversarially designed encodings，canonicalization 本身是一个 adversarial game，需要和攻击者 co-evolve；(c) partial encoding 场景下，正确 decode 需要 understanding 哪些部分是 encoded，这本身就需要 semantic understanding。不论论证方向如何，不正面回应这个 alternative 是一个 clear vulnerability。\n- 价值: 命中 Novelty 和 Related Work 差异化。堵住审稿人最可能提出的\"为什么不直接做 learned normalization\"的质疑，同时通过回应这个 alternative 进一步锐化 EncoGuard 的 design rationale。\n\n【发掘点 4】\n- 维度: 核心 claim 强化\n- 内容: Proposal 声称 curriculum 让 classifier 学到了\"encoding-invariant features\"，但从未解释 **why** curriculum ordering 比 flat exposure 更能产出 encoding-invariant representations。这是核心 claim 的逻辑链中一个缺失的环节。一个有力的论证可以基于 curriculum learning theory 中的 catastrophic confusion avoidance：**flat exposure 下，classifier 同时面对 simple 和 complex encodings，对 complex encodings 的 gradient signal 在早期训练中是噪声（因为 classifier 尚未建立基础的 encoding-aware features），这些 noisy gradients 干扰 simple encoding 的 feature learning；curriculum ordering 让 classifier 先在 simple encodings 上建立 robust token-level encoding-detection features，这些 features 作为 compositional building blocks 支撑 complex encoding 的 feature learning**。这个论证将\"curriculum 有用\"从一个经验观察提升为一个有 mechanistic motivation 的 claim，也自然解释了为什么 generalization 能发生：compositional building blocks 是 encoding-type-agnostic 的。\n- 价值: 命中 Novelty 和 Significance。为核心 claim 提供 mechanistic grounding，将 paper 从\"empirical observation that curriculum helps\"提升到\"mechanistically motivated principle + empirical validation\"，这正是 EMNLP main 期待的贡献深度。\n\n【发掘点 5】\n- 维度: significance 提升\n- 内容: Proposal 最后提到\"complexity-structured curriculum is a general principle for adversarial robustness\"并列举了 multi-turn staged delivery、tool-call obfuscation、cross-modal attack chains 作为 future directions，但这个 framing 目前是 hand-waving。问题在于：如果这只是 conclusion 里的一段展望，审稿人会直接忽略它。要真正提升 significance，需要将这个 general principle 在 paper 的 positioning 中前置——**将 encoding attacks 明确定位为\"attack difficulty has natural complexity ordering\"这一类攻击的 canonical instance**，在 introduction 中就建立这个 framing。然后，结论中不仅列举其他 domains，还要给出一个 **concrete formalization**：什么条件下 complexity-structured curriculum 适用？(a) attack space 有 composable primitives；(b) primitives 有 partial ordering on complexity；(c) defense model 的 feature learning 具有 compositional structure。这让 paper 的 contribution 从\"encoding defense method\"升级为\"a general adversarial robustness principle demonstrated on encoding attacks\"。这也回应了发掘点1的 re-framing——generalization 是 principle 的 evidence，curriculum 是 principle 的 instantiation。\n- 价值: 直接提升 Significance 维度。一个 domain-specific defense method paper 和一个 establish a general principle 的 paper 在 impact 上有数量级差异。这个 re-positioning 不需要额外实验（encoding 就是 demonstration domain），但大幅提升审稿人对 paper 影响力的感知。\n\n【补救 agent 本轮输出】:\n【状态】: 有缺陷待补救\n\n---\n\n【缺陷 1】\n- 类别: 可行性问题\n- 问题: 9 天内完成完整方案几乎不可行。即使 MVP（7 天）也需要：(1) 实现并调试 co-evolutionary 训练循环（含 GRPO attacker + SFT classifier 交替训练的自定义编排脚本），(2) 训练 EncoGuard 完整 2-round pipeline，(3) 训练 2 个 baseline 到等计算量，(4) 在 6,000+ test cases + 4 个 benchmark 上完整评估，(5) 写完论文。Co-evolutionary loop 的工程复杂度（oracle fallback、entropy regularization、semantic deduplication、FPR rollback）极高，调试周期不可预测。GRPO 训练本身也可能需要超参搜索。即使编码生成器和 EncoAttack 已预先准备，训练+评估+写作在 9 天内仍然极度紧张。\n- 严重度: 可补救\n- 补救方案: (1) 进一步缩减 MVP：将 co-evolutionary 从 2 rounds 压缩为仅验证 Stage 1 curriculum vs. random-order（单 round 即可出 H2 核心 ablation 结果），Stage 2 作为 camera-ready extension；(2) 明确计算资源配置（几块 A100/H100、预计每个 training run 的 wall-clock 时间），让 reviewer 能判断可行性；(3) 如果 co-evolutionary loop 调不通，准备 fallback 方案：用静态生成的 curriculum-ordered 数据做 SFT（去掉 GRPO attacker），仍可验证 curriculum ordering 假设，只是放弃 co-evolutionary 贡献。\n\n【缺陷 2】\n- 类别: compute 公平性问题\n- 问题: Proposal 提到 baselines 训练到 \"equivalent compute\" 但未定义等计算量的度量标准。Ilin et al. 原方案使用 7B attacker + 300M classifier，本方案使用 2B attacker + 4B classifier，架构完全不同。\"等计算量\" 是指 FLOPs、wall-clock time、训练 tokens、还是训练 steps？不同度量会导致完全不同的公平性结论。Random-order ablation 和 flat augmentation baseline 的训练数据量、训练步数、学习率 schedule 是否完全一致也未说明。\n- 严重度: 可补救\n- 补救方案: (1) 明确以 training FLOPs 为主要计算量度量，辅以 training tokens 和 wall-clock time 报告；(2) 对 random-order ablation 和 flat augmentation baseline，保证训练 steps、数据总量、模型架构完全一致，唯一变量是数据排列顺序/覆盖方式；(3) 对 Ilin et al. baseline，由于架构不同，改为在相同 4B classifier 架构上重新实现其训练策略（无编码 curriculum 的 RL adversarial training），确保架构控制变量一致。\n\n【缺陷 3】\n- 类别: 实验设计不足\n- 问题: 仅 2 rounds co-evolutionary training 对应 2-stage curriculum，每个 stage 只有一轮训练。这使得\"curriculum ordering 是关键因素\"的 claim 证据力度有限——可能混淆 recency effect（后训练的数据影响更大）和 curriculum effect。如果 random-order baseline 也恰好在第 2 round 看到更多 composite attacks（随机分配下统计波动），差异可能不显著。此外，2 rounds 无法展示收敛趋势或 curriculum 带来的训练效率提升曲线。\n- 严重度: 可补救\n- 补救方案: (1) 对 random-order baseline 做 3-5 次不同随机种子的重复实验，报告均值和标准差，避免单次随机分配的偶然性；(2) 增加一个\"反向 curriculum\"ablation（先难后易：先 Stage 2 数据再 Stage 1 数据），如果正向 curriculum 显著优于反向 curriculum，则更强地支持 ordering 假设；(3) 在 training 过程中记录每个 checkpoint 的 encoding-ASR 曲线，展示 curriculum 带来的学习动态差异（即使只有 2 rounds，中间 checkpoint 也能提供梯度信息）。\n\n【缺陷 4】\n- 类别: 评估方案缺陷\n- 问题: EncoAttack 是作者自建 benchmark（500 prompts × 8 encoding types × 3 nesting levels），未说明 prompt 来源、质量控制、以及是否存在对自身方法的隐式偏向。如果 500 base prompts 的分布恰好有利于 curriculum-trained model（例如以特定 harmful category 为主），结论可能不 generalizable。此外，benchmark 的 encoding 实现是否与训练时使用的编码器完全一致——如果一致，则评估可能只测试了\"见过的变换\"的记忆而非真正的 robustness。\n- 严重度: 可补救\n- 补救方案: (1) 明确 500 base prompts 来源（建议从 HarmBench + AdvBench + WildGuardTest 各抽样，覆盖多种 harm category）；(2) EncoAttack 的编码实现应独立于训练 pipeline（不同代码路径，不同随机种子控制 partial encoding 位置等），避免 train-test 编码实现耦合；(3) 报告在 HarmBench/JailbreakBench/WildGuardTest 这些外部 benchmark 上的结果作为主要证据，EncoAttack 作为补充深度分析；(4) 考虑邀请外部人员验证 EncoAttack 的 encoding 实现是否产生有效攻击（或至少用另一个 guardrail 如 LlamaGuard 验证这些攻击确实能 bypass 未防御的 classifier）。\n\n【缺陷 5】\n- 类别: 评估方案缺陷\n- 问题: Reference baselines（Broken-Token CPT-Filtering、TRYLOCK Layer 0）使用 published numbers 而非在相同测试集上重新评估。这些论文的评估设置（attack types、prompt distribution、success criteria）与本文不同，直接数字对比不构成公平 comparison。Reviewer 极可能质疑这些 comparison 的有效性。\n- 严重度: 可补救\n- 补救方案: (1) 将 Broken-Token 和 TRYLOCK 的 reference comparison 明确标注为\"indicative comparison\"而非\"controlled comparison\"，放入 Discussion 而非 Main Results table；(2) 如果时间允许，实现 Broken-Token 的 CPT-Filtering（相对简单的 rule-based 方法）在 EncoAttack 上评估，作为 controlled comparison；(3) 或者直接从 main claim 中移除 H3（\"catches ≥30% of attacks that evade CPT-Filtering\"），因为缺乏同条件对比无法严格验证此 hypothesis。\n\n【缺陷 6】\n- 类别: 可行性问题\n- 问题: GPT-4o oracle 在 GRPO 训练中的 API 调用成本和延迟未评估。Co-evolutionary training 每生成一个 adversarial sample 都需要 oracle 判断（harmful/benign），假设每 round 生成 5,000-10,000 samples，2 rounds 即 10,000-20,000 次 GPT-4o 调用。加上 deterministic decoder fallback 的 disagreement 检查，实际调用可能更多。这涉及：(a) 金钱成本（GPT-4o 输入输出 token 费用），(b) API rate limit 导致训练中断/减速，(c) GPT-4o 对 nested encoding 的 decode 准确率——如果 Stage 2 的 complex nested encodings 导致 GPT-4o 频繁判断错误，大量 samples 被 exclude，有效训练数据量可能严重不足。\n- 严重度: 可补救\n- 补救方案: (1) 预估 oracle 调用量和成本（建议控制在 $200-500 以内），说明 rate limit 策略（batch API、async 调用）；(2) 对 Stage 2 complex encodings 先做小规模 pilot（100 samples）测试 GPT-4o decode 准确率和 deterministic decoder agreement rate，如果 agreement rate <80%，需要调整 oracle 策略（如对 Stage 2 改用纯 deterministic decoder 判断）；(3) 考虑用更便宜的 oracle（GPT-4o-mini）做 Stage 1 判断，仅 Stage 2 用 GPT-4o，降低成本。\n\n【缺陷 7】\n- 类别: ablation 不完整\n- 问题: Proposal 缺少对 stability mechanisms 的 ablation。引入了 3 个 stability 组件（entropy regularization、FPR rollback、semantic deduplication），但没有计划验证每个组件的独立贡献。如果 reviewer 问\"entropy regularization 是否真的必要\"或\"去掉 semantic deduplication 会怎样\"，当前方案无法回答。\n- 严重度: 可补救\n- 补救方案: (1) 在 MVP 范围外，但在 camera-ready 中计划 stability ablation（去掉每个组件后的 ASR 变化）；(2) 如果时间极紧，至少记录训练过程中 entropy regularization 生效的频率（encoding type distribution 的实际 entropy 变化曲线）和 FPR rollback 触发次数，作为 \"mechanism utility\" 的间接证据；(3) 在论文中诚实说明这些是 engineering choices borrowed from prior work（TriPlay-RL 的 diversity penalty），非本文 contribution，降低 reviewer 对其 ablation 的期望。\n\n---\n\n**总结**：实验设计的核心框架（curriculum vs. random-order vs. flat augmentation 三方对比 + held-out generalization test）是合理的，ablation 逻辑清晰地对准了 H1-H4 四个 hypotheses。主要风险集中在 **(1) 时间可行性**（9 天完成全套训练+评估+写作极度激进）和 **(2) compute-normalized comparison 未明确定义**。建议最优先处理缺陷 1（进一步明确 fallback 方案）和缺陷 2（固定 compute normalization 定义），这两个是 reviewer 最可能 challenge 的点。缺陷 3（反向 curriculum ablation）和缺陷 5（reference baseline 公平性）属于中等优先级但能显著加强说服力的改进。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T12:16:51.459Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:16:51.459Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-16T12:16:51.471Z_

【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
【状态】: 有发掘空间

---

【发掘点 1】
- 维度: novelty 锐化
- 内容: 当前 proposal 的 primary contribution 定位为"encoding-complexity curriculum 优于 flat augmentation 和 model-evolution curriculum"。但这个 claim 的 surprise level 偏低——一个有经验的审稿人会说："当 attack difficulty 有 natural ordering 的时候，curriculum learning 优于 random ordering，这不是 curriculum learning 文献早就建立的结论吗？你只是把它搬到了 encoding domain。" 真正 surprising 的结果是 **generalization to held-out encoding types**：如果 curriculum-ordered training 能泛化到 Braille/Morse 而 random-order training 和 flat augmentation 不能，这才是 non-trivial 的发现。建议 **将 generalization 提升为 primary contribution，将 curriculum design 降为 enabling mechanism**。重新 framing 为"encoding-complexity curriculum teaches encoding-invariant harmful-content features that generalize to unseen encoding families"，核心 claim 变成一个关于表征学习的发现（classifier 学到了 encoding-agnostic features），而非一个关于训练策略的工程选择。这样的 claim 审稿人更难用 "I would have guessed this" 来 dismiss。
- 价值: 直接提升 Novelty 维度。将 paper 的核心贡献从"已知原则的 domain-specific application"提升为"关于 adversarial robustness 中 feature learning 的 insight"，天花板从 borderline 的 method paper 提升到有 conceptual contribution 的工作。

【发掘点 2】
- 维度: 前提假设质疑
- 内容: Proposal 断言"encoding difficulty is determined by structural properties (nesting depth, CPT-ratio preservation, cross-script mixing) rather than model-evolution differentials"，但这个前提本身未经验证，且可能是错误的。Classifier 对不同 encoding 的实际 difficulty 可能主要由 **tokenizer behavior** 决定——同样是单层 encoding，base64 和 homoglyph substitution 的 tokenization pattern 差异巨大，对 classifier 而言 difficulty gap 可能远超 nesting depth 的影响。当前 2-stage curriculum 的分组逻辑（Stage 1 = single encoding, Stage 2 = composite）是一个**未经验证的 heuristic**，审稿人会问："你怎么知道 nesting depth 是 difficulty 的 right axis？如果按 tokenizer disruption degree 排序效果更好呢？" 建议在 idea 层面引入一个 **formalized encoding complexity metric**（例如，综合 nesting depth、CPT deviation、tokenizer perplexity 的 composite score），并将 curriculum ordering 定义为沿这个 metric 的 progressive escalation。这不仅让 curriculum 有了 principled grounding，还直接强化了"general principle"的 claim——复杂度度量本身就是可迁移的方法论贡献。
- 价值: 同时命中 Novelty 和 Significance。将 curriculum design 从 ad-hoc 2-stage heuristic 提升为 principled framework，挡住"为什么是这个 ordering"的审稿质疑，同时为 generalization claim 提供更强的理论支撑（如果 metric 能预测 held-out encodings 的 difficulty，这本身就是一个 finding）。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: Proposal 讨论了 rule-based canonicalization (TRYLOCK) 和 static CPT-Filtering (Broken-Token) 的局限性，但遗漏了一个更有力的 trivial alternative：**learned input canonicalization**。训练一个 seq2seq model（甚至一个轻量 encoder-decoder）将任意 encoded input 解码回 plaintext，然后喂给标准 guardrail classifier。这个 pipeline approach 不需要 curriculum learning，不需要 adversarial co-training，计算成本可能远低于 GRPO co-evolutionary loop。如果这个 simple baseline 效果接近，EncoGuard 的增量价值就很有限。Proposal 需要在 idea 层面明确论证为什么 **end-to-end encoding-robust classification** 优于 **canonicalization + standard classification** 的 pipeline——可能的论点包括：(a) canonicalization 是 error-propagating pipeline，decode 错误直接导致 classifier 失效；(b) 对 adversarially designed encodings，canonicalization 本身是一个 adversarial game，需要和攻击者 co-evolve；(c) partial encoding 场景下，正确 decode 需要 understanding 哪些部分是 encoded，这本身就需要 semantic understanding。不论论证方向如何，不正面回应这个 alternative 是一个 clear vulnerability。
- 价值: 命中 Novelty 和 Related Work 差异化。堵住审稿人最可能提出的"为什么不直接做 learned normalization"的质疑，同时通过回应这个 alternative 进一步锐化 EncoGuard 的 design rationale。

【发掘点 4】
- 维度: 核心 claim 强化
- 内容: Proposal 声称 curriculum 让 classifier 学到了"encoding-invariant features"，但从未解释 **why** curriculum ordering 比 flat exposure 更能产出 encoding-invariant representations。这是核心 claim 的逻辑链中一个缺失的环节。一个有力的论证可以基于 curriculum learning theory 中的 catastrophic confusion avoidance：**flat exposure 下，classifier 同时面对 simple 和 complex encodings，对 complex encodings 的 gradient signal 在早期训练中是噪声（因为 classifier 尚未建立基础的 encoding-aware features），这些 noisy gradients 干扰 simple encoding 的 feature learning；curriculum ordering 让 classifier 先在 simple encodings 上建立 robust token-level encoding-detection features，这些 features 作为 compositional building blocks 支撑 complex encoding 的 feature learning**。这个论证将"curriculum 有用"从一个经验观察提升为一个有 mechanistic motivation 的 claim，也自然解释了为什么 generalization 能发生：compositional building blocks 是 encoding-type-agnostic 的。
- 价值: 命中 Novelty 和 Significance。为核心 claim 提供 mechanistic grounding，将 paper 从"empirical observation that curriculum helps"提升到"mechanistically motivated principle + empirical validation"，这正是 EMNLP main 期待的贡献深度。

【发掘点 5】
- 维度: significance 提升
- 内容: Proposal 最后提到"complexity-structured curriculum is a general principle for adversarial robustness"并列举了 multi-turn staged delivery、tool-call obfuscation、cross-modal attack chains 作为 future directions，但这个 framing 目前是 hand-waving。问题在于：如果这只是 conclusion 里的一段展望，审稿人会直接忽略它。要真正提升 significance，需要将这个 general principle 在 paper 的 positioning 中前置——**将 encoding attacks 明确定位为"attack difficulty has natural complexity ordering"这一类攻击的 canonical instance**，在 introduction 中就建立这个 framing。然后，结论中不仅列举其他 domains，还要给出一个 **concrete formalization**：什么条件下 complexity-structured curriculum 适用？(a) attack space 有 composable primitives；(b) primitives 有 partial ordering on complexity；(c) defense model 的 feature learning 具有 compositional structure。这让 paper 的 contribution 从"encoding defense method"升级为"a general adversarial robustness principle demonstrated on encoding attacks"。这也回应了发掘点1的 re-framing——generalization 是 principle 的 evidence，curriculum 是 principle 的 instantiation。
- 价值: 直接提升 Significance 维度。一个 domain-specific defense method paper 和一个 establish a general principle 的 paper 在 impact 上有数量级差异。这个 re-positioning 不需要额外实验（encoding 就是 demonstration domain），但大幅提升审稿人对 paper 影响力的感知。

【补救 agent 本轮输出】:
【状态】: 有缺陷待补救

---

【缺陷 1】
- 类别: 可行性问题
- 问题: 9 天内完成完整方案几乎不可行。即使 MVP（7 天）也需要：(1) 实现并调试 co-evolutionary 训练循环（含 GRPO attacker + SFT classifier 交替训练的自定义编排脚本），(2) 训练 EncoGuard 完整 2-round pipeline，(3) 训练 2 个 baseline 到等计算量，(4) 在 6,000+ test cases + 4 个 benchmark 上完整评估，(5) 写完论文。Co-evolutionary loop 的工程复杂度（oracle fallback、entropy regularization、semantic deduplication、FPR rollback）极高，调试周期不可预测。GRPO 训练本身也可能需要超参搜索。即使编码生成器和 EncoAttack 已预先准备，训练+评估+写作在 9 天内仍然极度紧张。
- 严重度: 可补救
- 补救方案: (1) 进一步缩减 MVP：将 co-evolutionary 从 2 rounds 压缩为仅验证 Stage 1 curriculum vs. random-order（单 round 即可出 H2 核心 ablation 结果），Stage 2 作为 camera-ready extension；(2) 明确计算资源配置（几块 A100/H100、预计每个 training run 的 wall-clock 时间），让 reviewer 能判断可行性；(3) 如果 co-evolutionary loop 调不通，准备 fallback 方案：用静态生成的 curriculum-ordered 数据做 SFT（去掉 GRPO attacker），仍可验证 curriculum ordering 假设，只是放弃 co-evolutionary 贡献。

【缺陷 2】
- 类别: compute 公平性问题
- 问题: Proposal 提到 baselines 训练到 "equivalent compute" 但未定义等计算量的度量标准。Ilin et al. 原方案使用 7B attacker + 300M classifier，本方案使用 2B attacker + 4B classifier，架构完全不同。"等计算量" 是指 FLOPs、wall-clock time、训练 tokens、还是训练 steps？不同度量会导致完全不同的公平性结论。Random-order ablation 和 flat augmentation baseline 的训练数据量、训练步数、学习率 schedule 是否完全一致也未说明。
- 严重度: 可补救
- 补救方案: (1) 明确以 training FLOPs 为主要计算量度量，辅以 training tokens 和 wall-clock time 报告；(2) 对 random-order ablation 和 flat augmentation baseline，保证训练 steps、数据总量、模型架构完全一致，唯一变量是数据排列顺序/覆盖方式；(3) 对 Ilin et al. baseline，由于架构不同，改为在相同 4B classifier 架构上重新实现其训练策略（无编码 curriculum 的 RL adversarial training），确保架构控制变量一致。

【缺陷 3】
- 类别: 实验设计不足
- 问题: 仅 2 rounds co-evolutionary training 对应 2-stage curriculum，每个 stage 只有一轮训练。这使得"curriculum ordering 是关键因素"的 claim 证据力度有限——可能混淆 recency effect（后训练的数据影响更大）和 curriculum effect。如果 random-order baseline 也恰好在第 2 round 看到更多 composite attacks（随机分配下统计波动），差异可能不显著。此外，2 rounds 无法展示收敛趋势或 curriculum 带来的训练效率提升曲线。
- 严重度: 可补救
- 补救方案: (1) 对 random-order baseline 做 3-5 次不同随机种子的重复实验，报告均值和标准差，避免单次随机分配的偶然性；(2) 增加一个"反向 curriculum"ablation（先难后易：先 Stage 2 数据再 Stage 1 数据），如果正向 curriculum 显著优于反向 curriculum，则更强地支持 ordering 假设；(3) 在 training 过程中记录每个 checkpoint 的 encoding-ASR 曲线，展示 curriculum 带来的学习动态差异（即使只有 2 rounds，中间 checkpoint 也能提供梯度信息）。

【缺陷 4】
- 类别: 评估方案缺陷
- 问题: EncoAttack 是作者自建 benchmark（500 prompts × 8 encoding types × 3 nesting levels），未说明 prompt 来源、质量控制、以及是否存在对自身方法的隐式偏向。如果 500 base prompts 的分布恰好有利于 curriculum-trained model（例如以特定 harmful category 为主），结论可能不 generalizable。此外，benchmark 的 encoding 实现是否与训练时使用的编码器完全一致——如果一致，则评估可能只测试了"见过的变换"的记忆而非真正的 robustness。
- 严重度: 可补救
- 补救方案: (1) 明确 500 base prompts 来源（建议从 HarmBench + AdvBench + WildGuardTest 各抽样，覆盖多种 harm category）；(2) EncoAttack 的编码实现应独立于训练 pipeline（不同代码路径，不同随机种子控制 partial encoding 位置等），避免 train-test 编码实现耦合；(3) 报告在 HarmBench/JailbreakBench/WildGuardTest 这些外部 benchmark 上的结果作为主要证据，EncoAttack 作为补充深度分析；(4) 考虑邀请外部人员验证 EncoAttack 的 encoding 实现是否产生有效攻击（或至少用另一个 guardrail 如 LlamaGuard 验证这些攻击确实能 bypass 未防御的 classifier）。

【缺陷 5】
- 类别: 评估方案缺陷
- 问题: Reference baselines（Broken-Token CPT-Filtering、TRYLOCK Layer 0）使用 published numbers 而非在相同测试集上重新评估。这些论文的评估设置（attack types、prompt distribution、success criteria）与本文不同，直接数字对比不构成公平 comparison。Reviewer 极可能质疑这些 comparison 的有效性。
- 严重度: 可补救
- 补救方案: (1) 将 Broken-Token 和 TRYLOCK 的 reference comparison 明确标注为"indicative comparison"而非"controlled comparison"，放入 Discussion 而非 Main Results table；(2) 如果时间允许，实现 Broken-Token 的 CPT-Filtering（相对简单的 rule-based 方法）在 EncoAttack 上评估，作为 controlled comparison；(3) 或者直接从 main claim 中移除 H3（"catches ≥30% of attacks that evade CPT-Filtering"），因为缺乏同条件对比无法严格验证此 hypothesis。

【缺陷 6】
- 类别: 可行性问题
- 问题: GPT-4o oracle 在 GRPO 训练中的 API 调用成本和延迟未评估。Co-evolutionary training 每生成一个 adversarial sample 都需要 oracle 判断（harmful/benign），假设每 round 生成 5,000-10,000 samples，2 rounds 即 10,000-20,000 次 GPT-4o 调用。加上 deterministic decoder fallback 的 disagreement 检查，实际调用可能更多。这涉及：(a) 金钱成本（GPT-4o 输入输出 token 费用），(b) API rate limit 导致训练中断/减速，(c) GPT-4o 对 nested encoding 的 decode 准确率——如果 Stage 2 的 complex nested encodings 导致 GPT-4o 频繁判断错误，大量 samples 被 exclude，有效训练数据量可能严重不足。
- 严重度: 可补救
- 补救方案: (1) 预估 oracle 调用量和成本（建议控制在 $200-500 以内），说明 rate limit 策略（batch API、async 调用）；(2) 对 Stage 2 complex encodings 先做小规模 pilot（100 samples）测试 GPT-4o decode 准确率和 deterministic decoder agreement rate，如果 agreement rate <80%，需要调整 oracle 策略（如对 Stage 2 改用纯 deterministic decoder 判断）；(3) 考虑用更便宜的 oracle（GPT-4o-mini）做 Stage 1 判断，仅 Stage 2 用 GPT-4o，降低成本。

【缺陷 7】
- 类别: ablation 不完整
- 问题: Proposal 缺少对 stability mechanisms 的 ablation。引入了 3 个 stability 组件（entropy regularization、FPR rollback、semantic deduplication），但没有计划验证每个组件的独立贡献。如果 reviewer 问"entropy regularization 是否真的必要"或"去掉 semantic deduplication 会怎样"，当前方案无法回答。
- 严重度: 可补救
- 补救方案: (1) 在 MVP 范围外，但在 camera-ready 中计划 stability ablation（去掉每个组件后的 ASR 变化）；(2) 如果时间极紧，至少记录训练过程中 entropy regularization 生效的频率（encoding type distribution 的实际 entropy 变化曲线）和 FPR rollback 触发次数，作为 "mechanism utility" 的间接证据；(3) 在论文中诚实说明这些是 engineering choices borrowed from prior work（TriPlay-RL 的 diversity penalty），非本文 contribution，降低 reviewer 对其 ablation 的期望。

---

**总结**：实验设计的核心框架（curriculum vs. random-order vs. flat augmentation 三方对比 + held-out generalization test）是合理的，ablation 逻辑清晰地对准了 H1-H4 四个 hypotheses。主要风险集中在 **(1) 时间可行性**（9 天完成全套训练+评估+写作极度激进）和 **(2) compute-normalized comparison 未明确定义**。建议最优先处理缺陷 1（进一步明确 fallback 方案）和缺陷 2（固定 compute normalization 定义），这两个是 reviewer 最可能 challenge 的点。缺陷 3（反向 curriculum ablation）和缺陷 5（reference baseline 公平性）属于中等优先级但能显著加强说服力的改进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "41b50b6d-ca54-4a96-840d-c0b2f38f4ddf",
  "type": "user",
  "uuid": "a41ef7a1-fecc-467a-ad29-60f454d4fea4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:16:51.470Z_

```json
{
  "parentUuid": "a41ef7a1-fecc-467a-ad29-60f454d4fea4",
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
  "uuid": "113660b0-c452-40d8-8bd3-3fa21770b82a",
  "timestamp": "2026-05-16T12:16:51.470Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:16:51.470Z_

```json
{
  "parentUuid": "113660b0-c452-40d8-8bd3-3fa21770b82a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "efa4da79-2ef2-4aa4-a6ea-0e7dec65889c",
  "timestamp": "2026-05-16T12:16:51.470Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
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
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: novelty 锐化 - 内容: 当前 proposal 的 primary contribution 定位为\"encoding-complexity…",
  "leafUuid": "efa4da79-2ef2-4aa4-a6ea-0e7dec65889c",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:17:34.998Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the outputs from both agents and integrate them into a coherent assessment for Round 1.

First, let me understand the current state:
- I need to see the original proposal to understand what's being discussed. But I don't have it directly in this message. Let me work with what the agents have provided.

From the agents' outputs, I can piece together that the proposal is about:
- **EncoGuard**: A defense method against encoding-based jailbreak attacks on LLM guardrails
- Uses a **curriculum learning** approach organized by encoding complexity (simple → composite)
- Involves a **co-evolutionary training loop** with GRPO attacker + SFT classifier


- The curriculum ordering is designed to teach encoding-invariant features that generalize to unseen encoding types, progressing from single encodings to composite and nested ones
- Has a 9-day timeline to completion
- Benchmarks against EncoAttack (self-built) plus HarmBench, JailbreakBench, and WildGuardTest
- Compares against Broken-Token CPT-Filtering, TRYLOCK Layer 0, random-order ablation, and flat augmentation baselines

Now I'm examining the 发掘 agent's assessment to see what exploration opportunities it identified.

The agent suggests reframing the core contribution around generalization to unseen encoding types rather than just curriculum beating flat augmentation, which is a much stronger angle. It also recommends formalizing the encoding complexity metric beyond the current 2-stage heuristic, addressing whether the model is just learning a trivial canonicalization strategy, and providing mechanistic insight into why the curriculum approach actually works. There's also potential to position this as a broader principle for adversarial robustness.

For the 补救 agent's assessment, the main vulnerabilities are the tight 9-day timeline, needing clearer compute fairness definitions, limited evidence from only 2 rounds of evaluation, potential bias from the self-built EncoAttack benchmark, unreliability of reference baselines that weren't re-evaluated, uncertainty around GPT-4o oracle costs and reliability, and missing ablations on stability mechanisms. Most of these are fixable through methodology adjustments or additional experiments, though the timeline constraint is the most serious concern.

Looking at the overall picture, the curriculum learning idea for encoding robustness is solid but currently feels incremental. The 发掘 agent's suggestions—especially reframing around generalization, addressing the learned canonicalization alternative, and providing mechanistic explanations—could substantially strengthen the novelty. The experimental design is fundamentally sound with multiple addressable gaps, so the decision is to keep iterating with focus on the highest-impact improvements like compute fairness and reverse curriculum ablations. The reframing suggestions could genuinely push this higher—if I can formalize the encoding-invariant insight and position it as a general principle for complexity-ordered attacks rather than just a domain-specific defense, the novelty and significance both improve meaningfully. Right now the proposal sits around 24% median probability, but with these improvements incorporated it could reach 30%, though the experimental gaps still need addressing before I can be more confident. I'm now consolidating the key improvements from both rounds into a unified proposal—prioritizing the reframing of generalization as the core contribution with curriculum as the mechanism, formalizing the encoding complexity metric, and addressing the learned canonicalization alternative head-on. I'm also integrating the practical safeguards like the static curriculum fallback, precise compute normalization definitions, and the expanded ablation suite with reverse curriculum and multi-seed baselines to strengthen the experimental rigor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efa4da79-2ef2-4aa4-a6ea-0e7dec65889c",
  "isSidechain": false,
  "requestId": "req_011Cb6ESnpX6btCfKJ9bXnHX",
  "type": "assistant",
  "uuid": "58fd0532-75fd-43e1-8d08-b103076df3e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017amKrQBtAUhGYLbEbyAfT1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10965,
      "cache_read_input_tokens": 11374,
      "output_tokens": 6230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6230,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 10965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10965
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

_source line 9 · 2026-05-16T12:19:24.163Z_

【阶段】: 迭代第 1 轮
【发掘 agent 有效建议采纳】:
- **采纳发掘点 1**（re-frame primary contribution）：将 generalization to unseen encodings 提升为 primary contribution，curriculum 降为 enabling mechanism。这是本轮最高价值建议，直接解决"curriculum learning 在有 ordering 的 domain 里 work 不是常识吗"的 dismiss 风险。
- **采纳发掘点 2**（formalized complexity metric）：引入 composite encoding complexity score（nesting depth + CPT deviation + tokenizer perplexity），将 curriculum ordering 从 ad-hoc 2-stage 提升为 principled progressive escalation。
- **采纳发掘点 3**（address learned canonicalization）：在 related work 和 design rationale 中正面回应"为什么不做 learned normalization pipeline"，给出 error propagation + adversarial game + partial encoding 三个论点。
- **采纳发掘点 4**（mechanistic motivation）：加入 catastrophic confusion avoidance 论证，解释为什么 curriculum 比 flat exposure 更能产出 compositional encoding-detection features。
- **采纳发掘点 5**（general principle positioning）：在 Introduction 中前置"attack complexity ordering → curriculum"的 general principle framing，但保持克制——encoding attacks 作为 canonical demonstration，不过度 claim 其他 domains。

【补救 agent 有效建议采纳】:
- **采纳缺陷 1 补救**：明确 fallback 方案（静态 curriculum-ordered SFT 若 co-evolutionary 调不通），缩减 MVP 为仅验证 Stage 1 curriculum vs random-order。
- **采纳缺陷 2 补救**：固定 training FLOPs 为主要 compute normalization 度量，所有 ablation 保证架构/steps/数据量一致。
- **采纳缺陷 3 补救**：增加 reverse curriculum ablation + 3-5 seed random baseline，记录 per-checkpoint encoding-ASR 曲线。
- **采纳缺陷 4 补救**：明确 EncoAttack 的 prompt 来源（HarmBench + AdvBench + WildGuardTest 各抽样），训练和评估使用独立编码实现。
- **采纳缺陷 5 补救**：将 Broken-Token/TRYLOCK 标注为 indicative comparison 放入 Discussion，主 claim 聚焦 controlled ablation。
- **采纳缺陷 6 补救**：加入 oracle 成本估算和 Stage 2 pilot test 计划。
- **部分采纳缺陷 7**：stability mechanisms 定位为 borrowed engineering choices，记录触发频率作间接证据，完整 ablation 留 camera-ready。

【本轮 proposal 主要变更】:
**Idea 层面**:
- 核心 contribution re-frame：从"curriculum beats flat/random"→"curriculum teaches encoding-invariant features that generalize to unseen encoding families"
- 引入 formalized Encoding Complexity Score (ECS) 作为 curriculum ordering 的 principled basis
- 正面回应 learned canonicalization alternative
- 加入 mechanistic motivation（catastrophic confusion avoidance）
- General principle positioning 前置到 Introduction

**实验层面**:
- 增加 reverse curriculum ablation
- Random-order baseline 做 3-5 seed 重复
- Compute normalization 固定为 FLOPs
- EncoAttack 来源和 train-test 分离明确化
- Reference baselines 降级为 indicative comparison
- 加入 fallback 方案和 oracle 成本估算
- Per-checkpoint learning dynamics 分析

【idea 质量评估】: Novelty=中（从"known principle transfer"提升为"feature learning insight + formalized metric"，但仍不是 paradigm shift） Significance=中偏强（general principle positioning 提升了 perceived impact，但单一 demonstration domain 限制了实际 significance） → idea 天花板约 38-40%

【实验完备性评估】: Technical Soundness=中（框架合理，ablation 对准 hypotheses，但多个补丁尚未实际验证，时间风险依然存在） → 地板仍有缝隙但主要漏洞已有补救方案

【当前概率估计】: [22% - 35%] 中位 28%

【决策】: 继续

【决策理由】: 本轮两个 agent 都给出了高价值建议且均未收敛。发掘 agent 的 re-framing 建议（尤其是发掘点 1+4+5 的组合）如果在下一轮得到验证（即审稿人视角下是否真的 surprising enough），有潜力将 idea 天花板推到 40%+。补救 agent 识别的实验问题虽多但均为可补救类型，核心实验框架没有致命缺陷。当前 28% 中位距离 36% 阈值仍有 gap，但 idea re-framing + 实验补强的空间明确可见，值得再迭代一轮验证。

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
## Title

EncoGuard: Learning Encoding-Invariant Safety Features via Complexity-Structured Curriculum Training

## Problem Statement

Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail catastrophically when inputs are transformed through encoding schemes not seen during training. The core challenge is not merely defending against known encodings, but achieving **generalization to unseen encoding families**—a property that no existing defense reliably provides.

## Core Thesis

We hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—learns **encoding-invariant harmful-content features** that generalize to held-out encoding types unseen during training. This generalization arises because curriculum ordering enables the classifier to first build robust token-level encoding-detection primitives on simple encodings, which then serve as compositional building blocks for recognizing complex encodings. In contrast, flat augmentation and random-order training suffer from catastrophic confusion: noisy gradients from complex encodings in early training interfere with the formation of these foundational features.

This principle—that attack spaces with composable primitives and natural complexity ordering benefit from structured curriculum defense—is general beyond encoding attacks. We demonstrate it on the encoding domain as a canonical instance where complexity is formally quantifiable.

## Key Contributions

1. **Primary Contribution (Feature Learning Insight):** We demonstrate that complexity-structured curriculum training produces encoding-invariant representations that generalize to entirely unseen encoding families (Braille, Morse, custom ciphers), while flat augmentation and random-order training do not. This is evidence that curriculum ordering teaches compositional encoding-detection features rather than memorizing specific encoding patterns.

2. **Formalized Encoding Complexity Score (ECS):** We define a principled complexity metric combining nesting depth, character-per-token (CPT) ratio deviation, and tokenizer perplexity, which determines curriculum ordering. We show that ECS predicts classifier difficulty on held-out encodings, validating it as a transferable methodological contribution.

3. **Co-Evolutionary Training Framework:** We instantiate the curriculum principle via a GRPO-trained attacker that generates encoding attacks of escalating ECS, paired with an SFT classifier that trains on curriculum-ordered adversarial data. The co-evolutionary dynamic ensures the curriculum adapts to the classifier's current capability frontier.

4. **Comprehensive Evaluation:** We evaluate on both external benchmarks (HarmBench, JailbreakBench, WildGuardTest with encoding perturbations) and a purpose-built EncoAttack benchmark, with controlled ablations isolating the curriculum ordering effect.

## Methodology

### Encoding Complexity Score (ECS)

We define ECS for an encoding transformation $e$ as:

$$ECS(e) = \alpha \cdot \text{NestingDepth}(e) + \beta \cdot \text{CPT\_Deviation}(e) + \gamma \cdot \text{TokenizerPerplexity}(e)$$

where:
- NestingDepth: number of compositional encoding layers (1 for single, 2+ for nested)
- CPT_Deviation: absolute deviation of the encoded text's characters-per-token ratio from plaintext baseline
- TokenizerPerplexity: perplexity of the target model's tokenizer on the encoded text

Weights $\alpha, \beta, \gamma$ are set via pilot study measuring classifier error rate correlation. The curriculum presents attacks in monotonically increasing ECS order.

### Mechanistic Motivation for Curriculum Ordering

Under flat exposure, the classifier simultaneously receives simple encodings (e.g., base64 with clean token boundaries) and complex nested encodings (e.g., ROT13-inside-base64 with homoglyph substitution). For complex encodings, the gradient signal in early training is effectively noise—the classifier has not yet developed the basic encoding-detection features needed to parse these inputs. These noisy gradients interfere with feature learning on simple encodings, creating catastrophic confusion.

Curriculum ordering resolves this: Stage 1 (low-ECS) training builds robust token-level encoding-detection features—recognizing base64 character distributions, identifying ROT-shifted alphabetic patterns, detecting homoglyph Unicode ranges. These features are encoding-type-agnostic compositional primitives. Stage 2 (high-ECS) training then leverages these primitives to parse nested compositions, with gradient signal that is now informative rather than noisy.

This mechanism predicts generalization: if the classifier learns compositional encoding-detection primitives (rather than memorizing specific encoding types), it should recognize novel encodings that share structural properties with training encodings—e.g., Braille (character substitution like homoglyphs) or Morse (symbolic encoding like base64).

### Why Not Learned Canonicalization?

A natural alternative is training a seq2seq model to decode arbitrary encodings back to plaintext, then applying a standard guardrail classifier. We argue this pipeline approach is fundamentally limited:

1. **Error propagation**: Canonicalization errors (even partial) directly cause classifier failure. For nested encodings with 3+ layers, each decoding step compounds errors.
2. **Adversarial canonicalization game**: Against an adaptive attacker, the canonicalizer itself becomes the attack surface. The attacker can craft encodings that are decodable by humans but confuse the canonicalizer—this is merely shifting the adversarial robustness problem rather than solving it.
3. **Partial encoding ambiguity**: Real attacks mix encoded and plaintext segments. Correctly identifying which portions to decode requires semantic understanding of the content—precisely the capability we need the end-to-end system to have.

End-to-end encoding-robust classification sidesteps these issues by learning features that are directly invariant to encoding transformations.

### Co-Evolutionary Training Loop

**Attacker (Qwen2.5-1.5B, GRPO-trained):**
- Generates encoding attack prompts with ECS constrained to current curriculum stage
- Reward: +1 if generated encoding bypasses current classifier AND oracle confirms harmful content; -1 otherwise
- Entropy regularization: penalizes collapse to single encoding type (maintains diversity within ECS band)

**Classifier (Qwen2.5-4B, SFT):**
- Trains on curriculum-ordered adversarial examples: Stage 1 (ECS ≤ threshold_1), then Stage 2 (ECS > threshold_1)
- FPR rollback: if false positive rate on clean benign data exceeds 2%, revert to previous checkpoint
- Semantic deduplication: removes near-duplicate training examples (cosine similarity > 0.95 on sentence embeddings)

**Oracle:** GPT-4o judges whether decoded content is genuinely harmful. Deterministic decoder cross-validates; samples where oracle and deterministic decoder disagree are excluded.

**Training Schedule:** 2 rounds of co-evolution. Each round: attacker generates within ECS band → oracle filters → classifier trains on filtered data. Round 1 = low-ECS band, Round 2 = high-ECS band.

**Fallback Plan:** If co-evolutionary loop proves unstable, we fall back to static curriculum-ordered SFT: pre-generate curriculum-ordered training data using rule-based encoding generators (no GRPO attacker), train classifier on this static dataset. This still validates the core curriculum ordering hypothesis (H1, H2) while sacrificing the co-evolutionary contribution (H4).

### Compute and Cost Estimation

- **Hardware:** 4× A100 80GB GPUs
- **Attacker training:** ~6 hours per round (1.5B model, GRPO on ~5K samples)
- **Classifier training:** ~8 hours per round (4B model, SFT on ~10K samples)
- **Total training wall-clock:** ~30 hours for 2 rounds (including data generation and filtering)
- **Oracle API cost:** Estimated 15K-20K GPT-4o calls across 2 rounds ≈ $150-300
- **Rate limit strategy:** Batch API with async calls, 500 requests/minute tier
- **Compute normalization for baselines:** Training FLOPs (primary), supplemented by training tokens and wall-clock time reporting. All ablation variants use identical 4B classifier architecture, identical training steps, identical total data volume.

## Experimental Design

### Hypotheses

- **H1 (Curriculum > Random):** Curriculum-ordered training achieves ≥10pp lower encoding-ASR than random-order training at equivalent FLOPs.
- **H2 (Generalization):** Curriculum-trained classifier maintains ≤30% encoding-ASR on held-out encoding families (Braille, Morse, custom cipher) where random-order and flat augmentation exceed 60% ASR.
- **H3 (ECS Predictiveness):** ECS correlates with classifier error rate (Spearman ρ ≥ 0.7) on held-out encodings, validating the metric as a principled difficulty measure.
- **H4 (Co-evolution > Static):** Co-evolutionary training outperforms static curriculum SFT by ≥5pp on composite encodings (if co-evolutionary loop is successfully implemented).

### Baselines and Ablations

**Controlled comparisons (same architecture, same FLOPs):**
1. **Random-order training:** Same data, same total steps, random presentation order. 5 random seeds, report mean ± std.
2. **Flat augmentation:** All encoding types mixed uniformly in every batch (no ordering).
3. **Reverse curriculum:** Stage 2 data first, then Stage 1 data (tests whether ordering direction matters vs. mere staging).
4. **Static curriculum SFT:** Curriculum-ordered data without co-evolutionary attacker (isolates curriculum effect from co-evolution effect).

**Indicative comparisons (different architectures, reported in Discussion):**
5. **Broken-Token CPT-Filtering:** Rule-based approach; numbers from published results on comparable attack types.
6. **TRYLOCK Layer 0:** Rule-based canonicalization; published numbers on overlapping benchmarks.

### Evaluation Protocol

**External benchmarks (primary evidence):**
- HarmBench (encoding-perturbed variant): standard harmful prompts with encoding applied
- JailbreakBench: encoding attack subset
- WildGuardTest: encoding-perturbed variant

**EncoAttack (supplementary deep analysis):**
- 500 base prompts sourced from HarmBench (200) + AdvBench (150) + WildGuardTest (150), covering 10+ harm categories
- 8 encoding types × 3 nesting levels = 24 conditions per prompt → 12,000 test cases
- Encoding implementation: independent codebase from training pipeline, different random seeds for partial encoding positions
- Validation: confirm attacks bypass undefended LlamaGuard-3 at ≥80% rate (ensuring attack validity)

**Held-out encoding families (generalization test):**
- Braille Unicode substitution
- Morse code symbolic encoding
- Custom Caesar-variant cipher (shift determined by position)
- NATO phonetic alphabet encoding
- These 4 encoding families are NEVER seen during training in any form

**Metrics:**
- Encoding-ASR (attack success rate): primary metric
- Clean FPR (false positive rate on benign inputs): safety constraint (must stay ≤2%)
- Per-encoding-type breakdown
- ECS correlation analysis on held-out encodings

### Learning Dynamics Analysis

- Record classifier encoding-ASR at every 500 training steps
- Plot per-encoding-type ASR curves showing curriculum-induced learning trajectory
- Compare learning dynamics between curriculum vs. random-order (expecting earlier convergence on low-ECS encodings under curriculum)

### Oracle Reliability Pilot

Before full training, conduct pilot on 100 samples per ECS band:
- Measure GPT-4o decode accuracy and harmful/benign judgment agreement with deterministic decoder
- If agreement rate < 80% for high-ECS band, adjust oracle strategy (e.g., use deterministic decoder only for Stage 2)

## Stability Mechanisms (Engineering Choices)

The following mechanisms are borrowed from prior work (TriPlay-RL diversity penalty, standard RL stabilization) and are not claimed as contributions:
- **Entropy regularization:** Prevents attacker collapse to single encoding type
- **FPR rollback:** Prevents classifier from becoming overly aggressive
- **Semantic deduplication:** Prevents training on near-duplicate examples

We report trigger frequencies for each mechanism as indirect evidence of utility. Full ablation of these components is planned for camera-ready.

## Timeline (10-day plan)

- Days 1-2: Implement ECS metric, encoding generators, data pipeline
- Days 3-4: Train Stage 1 (low-ECS curriculum) + random-order baseline (seed 1-3)
- Days 5-6: Train Stage 2 (high-ECS curriculum) + remaining baselines
- Day 7: Full evaluation on all benchmarks + held-out encodings
- Days 8-9: Analysis, ablations (reverse curriculum), writing
- Day 10: Buffer / camera-ready extensions

**If co-evolutionary loop fails by Day 4:** Switch to static curriculum SFT fallback, still completing H1-H3 validation.
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58fd0532-75fd-43e1-8d08-b103076df3e9",
  "isSidechain": false,
  "requestId": "req_011Cb6ESnpX6btCfKJ9bXnHX",
  "type": "assistant",
  "uuid": "50fe1549-2efd-4ade-88ba-7459788eb18c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017amKrQBtAUhGYLbEbyAfT1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10965,
      "cache_read_input_tokens": 11374,
      "output_tokens": 6230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10965,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6230,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 10965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10965
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
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: novelty 锐化 - 内容: 当前 proposal 的 primary contribution 定位为\"encoding-complexity…",
  "leafUuid": "50fe1549-2efd-4ade-88ba-7459788eb18c",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: novelty 锐化 - 内容: 当前 proposal 的 primary contribution 定位为\"encoding-complexity…",
  "leafUuid": "50fe1549-2efd-4ade-88ba-7459788eb18c",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 15 · 2026-05-16T12:21:05.313Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:21:05.313Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "content": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\n【状态】: 有发掘空间\n\n---\n\n【发掘点 1】\n- 维度: 前提假设质疑 / 核心 claim 强化\n- 内容: 当前 proposal 的逻辑链存在一个未弥合的跳跃：mechanistic explanation 声称 curriculum 帮助模型学习\"compositional encoding-detection primitives\"（如识别 base64 字符分布、ROT-shifted 模式、homoglyph Unicode ranges），但随后声称这些 primitives 能泛化到 **结构上完全不同的编码家族**（Braille、Morse）。问题是：检测 base64 字符分布的 feature 为什么会帮助识别 Braille Unicode substitution？它们共享的不是\"编码检测原语\"，而是一个更高阶的 meta-capability——\"在 surface form 异常时仍然提取 semantic harmful content\"。如果真正的泛化机制是学到了 **content-invariance under surface perturbation**（类似 vision 中的 texture vs. shape bias），而非 compositional encoding detection，那核心 claim 应该重新表述为：\"curriculum ordering 迫使模型先在低噪声环境下锚定 harmful content 的 semantic signature，再学会在高噪声环境下 preserve 这个 signature\"——这个 framing 比\"compositional primitives\"更精确、更 testable、也更 novel。\n- 价值: 如果机制描述与泛化 claim 之间有逻辑裂缝，审稿人会精准攻击这个点：\"你们说学的是 encoding-detection primitives，但 Braille 和 base64 没有共享的 detection primitive，所以泛化结果要么说明你们的机制假设是错的，要么说明泛化是巧合。\" 修正这个 framing 能让核心 claim 的逻辑链条闭合，同时让 novelty 更锐利——从\"curriculum helps learn compositional features\"（curriculum learning 文献里相对 familiar 的 claim）升级为\"curriculum ordering induces content-level invariance that separates semantic features from surface encoding features\"（一个关于 representation disentanglement 的更深刻 claim）。命中 **Novelty** 和 **Significance** 两个维度。\n\n【发掘点 2】\n- 维度: significance 提升\n- 内容: 当前 proposal 的 broader principle——\"attack spaces with composable primitives and natural complexity ordering benefit from structured curriculum defense\"——被声明了但没有被 operationalize。这个 principle 如果成立，意味着同样的方法论可以迁移到 **multi-step prompt injection**（简单指令注入 → 嵌套上下文操控）、**multi-turn social engineering**（单轮诱导 → 多轮渐进式）、**code injection attacks**（直接恶意代码 → 混淆/打包/多层编码的恶意代码）。但目前 paper 只在 encoding domain 做一个 instance，读起来像\"一个 encoding defense 方法恰好用了 curriculum\"，而非\"一个通用 principle 在 encoding domain 的 canonical demonstration\"。建议在 framing 层面做 pivot：核心贡献不是\"一个更好的 encoding defense\"，而是\"structured complexity curriculum 作为 compositional attack space 的通用防御原理，以 encoding attacks 作为形式化最清晰的验证场\"。\n- 价值: 如果只 pitch 为 encoding defense，significance 被限定在\"encoding jailbreak\"这个子问题里——审稿人可能觉得这个问题窄、会被更好的 tokenizer 或更大的预训练数据自然解决。但如果 pitch 为通用 principle + canonical demonstration，significance 立刻上升一个量级：这为整个 adversarial robustness 社区提供了一个新的 defense paradigm。同时，evaluation 中可以加一小段 discussion：\"如果该 principle 成立，以下攻击类型应该也适用...\"作为 future work teaser，但不需要实验证明。命中 **Significance**。\n\n【发掘点 3】\n- 维度: trivial alternative 威胁\n- 内容: Proposal 讨论了 \"learned canonicalization\" 这个替代方案并给出了合理的反驳。但忽略了一个更 trivial 的替代：**simple rule-based encoding detection + known decoder + standard guardrail**。大多数编码（base64、ROT13、Morse、Braille）都有极其明显的统计 signature（字符集限制、固定 pattern）。一个 regex/heuristic 检测器 + 已知解码器的 pipeline，对于单层编码和大多数双层嵌套，可能达到 90%+ 的检测率——成本几乎为零。论文需要明确论证：(1) 这个 trivial pipeline 在什么条件下失败（partial encoding? adversarial mixing of encoded and plaintext?），(2) 对于这些失败 cases，curriculum-trained classifier 的优势具体体现在哪。如果不正面回应这个 alternative，审稿人会问：\"为什么不直接用 regex 检测 + decode + LlamaGuard？\"\n- 价值: 这不是要否定 idea，而是要求在 introduction/motivation 中 explicitly 建立 problem boundary：rule-based 方法在 X 条件下有效但在 Y 条件下失败（Y = partial encoding、adversarial mixing、novel encodings with no known decoder），本工作正是解决 Y 的。这让 novelty claim 的 scope 更精确，也让 evaluation 的 focus 更有说服力。如果不处理这个点，整个 paper 的 motivation 会被\"为什么不用简单方法\"这一个问题击穿。命中 **Novelty**（通过明确 incremental value 的边界）。\n\n【发掘点 4】\n- 维度: related work 差异化\n- 内容: Curriculum learning 用于 adversarial robustness 不是新概念。Specifically：(1) **Cai et al., \"Curriculum Adversarial Training\" (IJCAI 2018)**——按 adversarial perturbation 强度递增训练 image classifiers；(2) **Wang et al., \"Ordered SGD\" (NeurIPS 2021)**——按 sample difficulty 排序训练以提高 generalization。当前 proposal 需要明确与这些 prior arts 的差异化：不只是\"curriculum + adversarial training\"的简单组合，而是 (a) 在离散 compositional attack space（而非连续 perturbation space）中定义 complexity metric，(b) 验证 curriculum 在 **out-of-distribution attack types** 上的泛化（prior work 只测 in-distribution robustness），(c) ECS 作为 domain-specific complexity formalization 的贡献。如果不 explicitly engage with curriculum adversarial training 的 prior art，审稿人一定会问：\"这和 curriculum adversarial training 比有什么本质区别？\"\n- 价值: 这是 related work 差异化的硬伤。如果审稿人认为这只是\"curriculum adversarial training applied to NLP encoding domain\"，novelty 评分会大幅下降。需要 clearly articulate 本工作的 unique insight：curriculum 在 **compositional discrete attack space** 中能诱导 **OOD generalization**——这是 prior curriculum adversarial training work 从未验证过的 claim，也是本文最强的 novelty angle。命中 **Related Work 差异化** 和 **Novelty**。\n\n【补救 agent 本轮输出】:\n【状态】: 有缺陷待补救\n\n---\n\n【缺陷 1】\n- 类别: baseline 不足或过时\n- 问题: Proposal 在 Methodology 中用整段文字论证\"Why Not Learned Canonicalization?\"并列出三条理论原因，但实验设计中**没有对应的经验性 baseline**。无论理论论证多充分，reviewer 几乎一定会问 \"show me the number\"。当前 baseline 列表缺少一个 decode-then-classify pipeline（即使是简单实现）的定量对比。\n- 严重度: 可补救\n- 补救方案: 增加一个 \"Oracle-Decode + LlamaGuard-3\" baseline：用确定性解码器（proposal 中已有此组件）解码输入，再接标准 guardrail 分类器。对简单编码此 baseline 应表现良好，对嵌套编码应展示 error propagation 问题，从而用数据而非纯理论支撑 end-to-end 方法的优势。此 baseline 零额外训练开销，仅需推理时间。\n\n【缺陷 2】\n- 类别: 实验设计不足（统计严谨性）\n- 问题: Random-order baseline 规定了 5 random seeds 报告 mean ± std，但 curriculum-ordered training（核心方法）**没有说明用多少 seeds**。如果 curriculum 只跑 1 次而 random-order 跑 5 次，reviewer 会质疑 curriculum 的表现是否为幸运种子的产物。尤其是 H1 声称 \"≥10pp\" 的提升幅度需要统计检验支撑。\n- 严重度: 可补救\n- 补救方案: 对 curriculum-ordered training 同样跑 3-5 seeds（至少 3 seeds），报告 mean ± std，并对 H1 进行配对 t-test 或 bootstrap confidence interval。Compute budget 相应增加约 2× classifier training time（~16 hours），在 4×A100 集群上仍可承受。\n\n【缺陷 3】\n- 类别: ablation 不完整\n- 问题: ECS 由三个加权组件（NestingDepth, CPT_Deviation, TokenizerPerplexity）组成，权重通过 pilot study 确定。但实验设计中没有对 ECS 组件进行 ablation——如果去掉其中一项，curriculum ordering 是否同样有效？Reviewer 会质疑三项是否都 necessary，以及权重设定是否 robust。\n- 严重度: 可补救\n- 补救方案: 增加 3 个 leave-one-out ablation：分别去掉 NestingDepth/CPT_Deviation/TokenizerPerplexity，仅用剩余两项排序训练数据，评估 H1 指标变化。这不需要额外数据生成（排序改变即可），计算开销为 3× classifier training ≈ 24 hours。此外报告 ECS 权重在合理范围内的 sensitivity analysis（±20% 扰动）。\n\n【缺陷 4】\n- 类别: 评估方案缺陷\n- 问题: Clean FPR 约束为硬性 ≤2% cutoff，但没有设计 FPR-ASR tradeoff 分析。如果 curriculum 方法在 2% FPR 时 ASR=20%，而 random-order 在 3% FPR 时 ASR=22%，单看 2% 截断线上的比较是不公平的。此外，proposal 未明确指定 benign test set 的来源和规模。\n- 严重度: 可补救\n- 补救方案: (1) 增加 ROC 曲线/FPR-ASR Pareto frontier 分析：在多个 FPR 阈值（0.5%, 1%, 2%, 5%）下报告对应 ASR，绘制 Pareto 曲线。(2) 明确 benign test set：使用 WildGuardTest 的 benign split（~1000 条）+ LMSYS-Chat-1M 随机采样 1000 条，两个分布分别报告 FPR。\n\n【缺陷 5】\n- 类别: 可行性问题（时间线）\n- 问题: 10 天时间线对所述工作量极度紧张。仅列举必须完成的独立工作流：(a) ECS 实现 + encoding generator 代码库；(b) GRPO attacker 训练；(c) 4 个 controlled baselines（含 5 seeds for random-order）；(d) oracle pilot + 全量 oracle 调用；(e) 4 个外部 benchmark 的 encoding-perturbed 版本构建；(f) EncoAttack 12K test cases 生成 + 验证；(g) held-out encoding 实现。即使不算写作，纯实验执行按 proposal 给出的 ~30h 训练时间 × 多个 seeds 和 ablations，在 4×A100 上并行度有限。\n- 严重度: 可补救\n- 补救方案: (1) 将时间线扩展至 14-16 天，或明确标注哪些实验可并行（不同 seed 的 baseline 可以同时跑在不同 GPU 上）。(2) 对 camera-ready ablations（ECS component ablation、stability mechanism ablation）与 submission-critical experiments 做优先级区分，仅在初稿中完成 H1-H3 核心实验，标注 \"camera-ready 完善\"。(3) 补上缺陷 2 和缺陷 3 增加的实验所需时间。\n\n【缺陷 6】\n- 类别: 实验设计不足（表征层面证据缺失）\n- 问题: Core thesis 声称 curriculum training 产生 \"encoding-invariant representations\" 和 \"compositional encoding-detection primitives\"，但实验设计中唯一的验证是 task-level metrics（ASR/FPR）和 learning dynamics curves。**没有表征层面的直接证据**证明模型确实学到了 encoding-invariant features，而非通过其他机制（如记忆更多模式）实现泛化。Reviewer 可以合理质疑：\"也许 curriculum 只是更好的数据调度策略，并不真的产生 invariant representations。\"\n- 严重度: 可补救\n- 补救方案: 增加一个 representation analysis 实验：(1) 对相同 harmful prompt 的 plaintext / 各种编码变体提取 classifier 倒数第二层表征；(2) 计算 curriculum-trained vs random-order-trained 模型上，同一 prompt 不同编码间的 CKA/cosine similarity；(3) 预期：curriculum 模型中同一 prompt 不同编码的表征应更聚集（higher similarity），直接支撑 \"encoding-invariant\" 的 claim。此分析仅需推理，无额外训练开销。\n\n---\n\n**总结**：实验设计整体框架 solid（假设清晰、controlled comparisons 设计合理、fallback plan 务实），但存在上述 6 个可补救缺陷。其中**缺陷 1（canonicalization baseline）和缺陷 6（表征证据）**对 reviewer 说服力影响最大，建议优先修复。所有缺陷均不涉及方向性致命问题，补救后实验设计可达 EMNLP 主会门槛。"
}
```

---

### Runtime record

_source line 16 · 2026-05-16T12:21:05.314Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:21:05.314Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

## Round 2

10 recorded events

### User

_source line 17 · 2026-05-16T12:21:05.335Z_

【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
【状态】: 有发掘空间

---

【发掘点 1】
- 维度: 前提假设质疑 / 核心 claim 强化
- 内容: 当前 proposal 的逻辑链存在一个未弥合的跳跃：mechanistic explanation 声称 curriculum 帮助模型学习"compositional encoding-detection primitives"（如识别 base64 字符分布、ROT-shifted 模式、homoglyph Unicode ranges），但随后声称这些 primitives 能泛化到 **结构上完全不同的编码家族**（Braille、Morse）。问题是：检测 base64 字符分布的 feature 为什么会帮助识别 Braille Unicode substitution？它们共享的不是"编码检测原语"，而是一个更高阶的 meta-capability——"在 surface form 异常时仍然提取 semantic harmful content"。如果真正的泛化机制是学到了 **content-invariance under surface perturbation**（类似 vision 中的 texture vs. shape bias），而非 compositional encoding detection，那核心 claim 应该重新表述为："curriculum ordering 迫使模型先在低噪声环境下锚定 harmful content 的 semantic signature，再学会在高噪声环境下 preserve 这个 signature"——这个 framing 比"compositional primitives"更精确、更 testable、也更 novel。
- 价值: 如果机制描述与泛化 claim 之间有逻辑裂缝，审稿人会精准攻击这个点："你们说学的是 encoding-detection primitives，但 Braille 和 base64 没有共享的 detection primitive，所以泛化结果要么说明你们的机制假设是错的，要么说明泛化是巧合。" 修正这个 framing 能让核心 claim 的逻辑链条闭合，同时让 novelty 更锐利——从"curriculum helps learn compositional features"（curriculum learning 文献里相对 familiar 的 claim）升级为"curriculum ordering induces content-level invariance that separates semantic features from surface encoding features"（一个关于 representation disentanglement 的更深刻 claim）。命中 **Novelty** 和 **Significance** 两个维度。

【发掘点 2】
- 维度: significance 提升
- 内容: 当前 proposal 的 broader principle——"attack spaces with composable primitives and natural complexity ordering benefit from structured curriculum defense"——被声明了但没有被 operationalize。这个 principle 如果成立，意味着同样的方法论可以迁移到 **multi-step prompt injection**（简单指令注入 → 嵌套上下文操控）、**multi-turn social engineering**（单轮诱导 → 多轮渐进式）、**code injection attacks**（直接恶意代码 → 混淆/打包/多层编码的恶意代码）。但目前 paper 只在 encoding domain 做一个 instance，读起来像"一个 encoding defense 方法恰好用了 curriculum"，而非"一个通用 principle 在 encoding domain 的 canonical demonstration"。建议在 framing 层面做 pivot：核心贡献不是"一个更好的 encoding defense"，而是"structured complexity curriculum 作为 compositional attack space 的通用防御原理，以 encoding attacks 作为形式化最清晰的验证场"。
- 价值: 如果只 pitch 为 encoding defense，significance 被限定在"encoding jailbreak"这个子问题里——审稿人可能觉得这个问题窄、会被更好的 tokenizer 或更大的预训练数据自然解决。但如果 pitch 为通用 principle + canonical demonstration，significance 立刻上升一个量级：这为整个 adversarial robustness 社区提供了一个新的 defense paradigm。同时，evaluation 中可以加一小段 discussion："如果该 principle 成立，以下攻击类型应该也适用..."作为 future work teaser，但不需要实验证明。命中 **Significance**。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: Proposal 讨论了 "learned canonicalization" 这个替代方案并给出了合理的反驳。但忽略了一个更 trivial 的替代：**simple rule-based encoding detection + known decoder + standard guardrail**。大多数编码（base64、ROT13、Morse、Braille）都有极其明显的统计 signature（字符集限制、固定 pattern）。一个 regex/heuristic 检测器 + 已知解码器的 pipeline，对于单层编码和大多数双层嵌套，可能达到 90%+ 的检测率——成本几乎为零。论文需要明确论证：(1) 这个 trivial pipeline 在什么条件下失败（partial encoding? adversarial mixing of encoded and plaintext?），(2) 对于这些失败 cases，curriculum-trained classifier 的优势具体体现在哪。如果不正面回应这个 alternative，审稿人会问："为什么不直接用 regex 检测 + decode + LlamaGuard？"
- 价值: 这不是要否定 idea，而是要求在 introduction/motivation 中 explicitly 建立 problem boundary：rule-based 方法在 X 条件下有效但在 Y 条件下失败（Y = partial encoding、adversarial mixing、novel encodings with no known decoder），本工作正是解决 Y 的。这让 novelty claim 的 scope 更精确，也让 evaluation 的 focus 更有说服力。如果不处理这个点，整个 paper 的 motivation 会被"为什么不用简单方法"这一个问题击穿。命中 **Novelty**（通过明确 incremental value 的边界）。

【发掘点 4】
- 维度: related work 差异化
- 内容: Curriculum learning 用于 adversarial robustness 不是新概念。Specifically：(1) **Cai et al., "Curriculum Adversarial Training" (IJCAI 2018)**——按 adversarial perturbation 强度递增训练 image classifiers；(2) **Wang et al., "Ordered SGD" (NeurIPS 2021)**——按 sample difficulty 排序训练以提高 generalization。当前 proposal 需要明确与这些 prior arts 的差异化：不只是"curriculum + adversarial training"的简单组合，而是 (a) 在离散 compositional attack space（而非连续 perturbation space）中定义 complexity metric，(b) 验证 curriculum 在 **out-of-distribution attack types** 上的泛化（prior work 只测 in-distribution robustness），(c) ECS 作为 domain-specific complexity formalization 的贡献。如果不 explicitly engage with curriculum adversarial training 的 prior art，审稿人一定会问："这和 curriculum adversarial training 比有什么本质区别？"
- 价值: 这是 related work 差异化的硬伤。如果审稿人认为这只是"curriculum adversarial training applied to NLP encoding domain"，novelty 评分会大幅下降。需要 clearly articulate 本工作的 unique insight：curriculum 在 **compositional discrete attack space** 中能诱导 **OOD generalization**——这是 prior curriculum adversarial training work 从未验证过的 claim，也是本文最强的 novelty angle。命中 **Related Work 差异化** 和 **Novelty**。

【补救 agent 本轮输出】:
【状态】: 有缺陷待补救

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 在 Methodology 中用整段文字论证"Why Not Learned Canonicalization?"并列出三条理论原因，但实验设计中**没有对应的经验性 baseline**。无论理论论证多充分，reviewer 几乎一定会问 "show me the number"。当前 baseline 列表缺少一个 decode-then-classify pipeline（即使是简单实现）的定量对比。
- 严重度: 可补救
- 补救方案: 增加一个 "Oracle-Decode + LlamaGuard-3" baseline：用确定性解码器（proposal 中已有此组件）解码输入，再接标准 guardrail 分类器。对简单编码此 baseline 应表现良好，对嵌套编码应展示 error propagation 问题，从而用数据而非纯理论支撑 end-to-end 方法的优势。此 baseline 零额外训练开销，仅需推理时间。

【缺陷 2】
- 类别: 实验设计不足（统计严谨性）
- 问题: Random-order baseline 规定了 5 random seeds 报告 mean ± std，但 curriculum-ordered training（核心方法）**没有说明用多少 seeds**。如果 curriculum 只跑 1 次而 random-order 跑 5 次，reviewer 会质疑 curriculum 的表现是否为幸运种子的产物。尤其是 H1 声称 "≥10pp" 的提升幅度需要统计检验支撑。
- 严重度: 可补救
- 补救方案: 对 curriculum-ordered training 同样跑 3-5 seeds（至少 3 seeds），报告 mean ± std，并对 H1 进行配对 t-test 或 bootstrap confidence interval。Compute budget 相应增加约 2× classifier training time（~16 hours），在 4×A100 集群上仍可承受。

【缺陷 3】
- 类别: ablation 不完整
- 问题: ECS 由三个加权组件（NestingDepth, CPT_Deviation, TokenizerPerplexity）组成，权重通过 pilot study 确定。但实验设计中没有对 ECS 组件进行 ablation——如果去掉其中一项，curriculum ordering 是否同样有效？Reviewer 会质疑三项是否都 necessary，以及权重设定是否 robust。
- 严重度: 可补救
- 补救方案: 增加 3 个 leave-one-out ablation：分别去掉 NestingDepth/CPT_Deviation/TokenizerPerplexity，仅用剩余两项排序训练数据，评估 H1 指标变化。这不需要额外数据生成（排序改变即可），计算开销为 3× classifier training ≈ 24 hours。此外报告 ECS 权重在合理范围内的 sensitivity analysis（±20% 扰动）。

【缺陷 4】
- 类别: 评估方案缺陷
- 问题: Clean FPR 约束为硬性 ≤2% cutoff，但没有设计 FPR-ASR tradeoff 分析。如果 curriculum 方法在 2% FPR 时 ASR=20%，而 random-order 在 3% FPR 时 ASR=22%，单看 2% 截断线上的比较是不公平的。此外，proposal 未明确指定 benign test set 的来源和规模。
- 严重度: 可补救
- 补救方案: (1) 增加 ROC 曲线/FPR-ASR Pareto frontier 分析：在多个 FPR 阈值（0.5%, 1%, 2%, 5%）下报告对应 ASR，绘制 Pareto 曲线。(2) 明确 benign test set：使用 WildGuardTest 的 benign split（~1000 条）+ LMSYS-Chat-1M 随机采样 1000 条，两个分布分别报告 FPR。

【缺陷 5】
- 类别: 可行性问题（时间线）
- 问题: 10 天时间线对所述工作量极度紧张。仅列举必须完成的独立工作流：(a) ECS 实现 + encoding generator 代码库；(b) GRPO attacker 训练；(c) 4 个 controlled baselines（含 5 seeds for random-order）；(d) oracle pilot + 全量 oracle 调用；(e) 4 个外部 benchmark 的 encoding-perturbed 版本构建；(f) EncoAttack 12K test cases 生成 + 验证；(g) held-out encoding 实现。即使不算写作，纯实验执行按 proposal 给出的 ~30h 训练时间 × 多个 seeds 和 ablations，在 4×A100 上并行度有限。
- 严重度: 可补救
- 补救方案: (1) 将时间线扩展至 14-16 天，或明确标注哪些实验可并行（不同 seed 的 baseline 可以同时跑在不同 GPU 上）。(2) 对 camera-ready ablations（ECS component ablation、stability mechanism ablation）与 submission-critical experiments 做优先级区分，仅在初稿中完成 H1-H3 核心实验，标注 "camera-ready 完善"。(3) 补上缺陷 2 和缺陷 3 增加的实验所需时间。

【缺陷 6】
- 类别: 实验设计不足（表征层面证据缺失）
- 问题: Core thesis 声称 curriculum training 产生 "encoding-invariant representations" 和 "compositional encoding-detection primitives"，但实验设计中唯一的验证是 task-level metrics（ASR/FPR）和 learning dynamics curves。**没有表征层面的直接证据**证明模型确实学到了 encoding-invariant features，而非通过其他机制（如记忆更多模式）实现泛化。Reviewer 可以合理质疑："也许 curriculum 只是更好的数据调度策略，并不真的产生 invariant representations。"
- 严重度: 可补救
- 补救方案: 增加一个 representation analysis 实验：(1) 对相同 harmful prompt 的 plaintext / 各种编码变体提取 classifier 倒数第二层表征；(2) 计算 curriculum-trained vs random-order-trained 模型上，同一 prompt 不同编码间的 CKA/cosine similarity；(3) 预期：curriculum 模型中同一 prompt 不同编码的表征应更聚集（higher similarity），直接支撑 "encoding-invariant" 的 claim。此分析仅需推理，无额外训练开销。

---

**总结**：实验设计整体框架 solid（假设清晰、controlled comparisons 设计合理、fallback plan 务实），但存在上述 6 个可补救缺陷。其中**缺陷 1（canonicalization baseline）和缺陷 6（表征证据）**对 reviewer 说服力影响最大，建议优先修复。所有缺陷均不涉及方向性致命问题，补救后实验设计可达 EMNLP 主会门槛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50fe1549-2efd-4ade-88ba-7459788eb18c",
  "isSidechain": false,
  "promptId": "c7bb3d38-5d0c-42dc-8240-708b43eabdd5",
  "type": "user",
  "uuid": "b468154f-210a-4443-ab20-de995ae953b3",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T12:21:49.567Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the Round 2 outputs from both agents and integrate them.

**发掘 agent Round 2 Analysis:**

1. **发掘点 1 (前提假设质疑/核心 claim 强化):** Very strong insight. The current mechanistic explanation has a logical gap: "compositional encoding-detection primitives" learned from base64/ROT13 don't obviously transfer to Braille/Morse because they share no detection primitives. The real mechanism is likely "content-level invariance under surface perturbation" — the curriculum forces the model to anchor harmful content semantic signatures under low noise first, then preserve them under high noise. 

This reframes the core claim more precisely and testably than the original "compositional primitives" framing — it's a HIGH VALUE contribution.

2. **发掘点 2 (significance 提升):** The agent pushes for sharper operationalization of the "general principle" framing, noting the proposal still reads more like "encoding defense using curriculum" rather than "general principle demonstrated on encoding." The framing was partially addressed already, but could be tightened.

3. **发掘点 3 (trivial alternative - rule-based detection):** Good catch on whether the proposal adequately rules out simpler explanations like regex detection or known encoding patterns.

The real problem space the paper needs to establish is where rule-based approaches fail: partial encodings, adversarial mixing, novel encodings without known decoders. This is HIGH VALUE.

4. **发掘点 4 (related work - Curriculum Adversarial Training):** This is a critical gap. Cai et al. (IJCAI 2018) on Curriculum Adversarial Training is a direct predecessor that must be discussed and differentiated. The key distinction is that prior work operates in continuous perturbation spaces and only tests in-distribution robustness, whereas this work operates in discrete compositional attack spaces and demonstrates OOD generalization. This MUST be addressed or reviewers will catch it. HIGH VALUE.

Now looking at what the agent flagged as missing in Round 2: the canonicalization baseline needs empirical evidence, not just theoretical argument.  Adding an "Oracle-Decode + LlamaGuard-3" baseline would be zero training cost and HIGH PRIORITY. The curriculum also needs to run with 3+ seeds for statistical validity, which is reasonable compute-wise. An ECS component ablation using leave-one-out would add 3× training but validate the metric—MEDIUM PRIORITY and could make camera-ready. The FPR-ASR tradeoff analysis needs ROC/Pareto curves at multiple thresholds plus an explicit benign test set, also MEDIUM PRIORITY. The timeline is still too tight at 10 days, so extending to 14-16 days and separating the submission would be more realistic.

There's also representation analysis—CKA and cosine similarity on hidden representations—which is inference-only and directly validates the core thesis about encoding-invariant features, making it HIGH PRIORITY. The agents are still converging on non-overlapping, high-value suggestions across both the idea and experiment layers. The mechanistic explanation gap needs fixing, the rule-based trivial alternative needs addressing, and the differentiation from Curriculum Adversarial Training literature needs clarification. Adding the canonicalization baseline, representation analysis, and multi-seed curriculum with a realistic timeline extension would round out the improvements.

Looking at the probability trajectory, Round 1 landed around 28% median. The fixes in Round 2—especially closing the mechanistic explanation gap, differentiating from prior curriculum work, and adding representation analysis—should meaningfully improve Technical Soundness and Novelty. The content-invariance under surface perturbation combined with OOD generalization in discrete compositional spaces appears genuinely novel compared to existing curriculum adversarial training approaches, positioning this as Medium-Strong on novelty with Medium significance.

The revised estimate of 32% median reflects a sharper idea and more rigorous experimental design. The ceiling sits around 42-45% if everything lands well. From the suggestions, I'm adopting the reframing toward content-invariance and representation disentanglement as the core mechanism—that's the strongest move this round. The general principle positioning also needs further sharpening, though the proposal already has some foundation there.

I'm also committing to clearer problem boundaries by addressing rule-based detection and the decode pipeline upfront, and I need to explicitly differentiate from curriculum adversarial training work to highlight why the discrete compositional space angle is novel. On the experimental side, I'm adding Oracle-Decode and LlamaGuard-3 baselines, and curriculum training will use 3 seeds minimum to match the rigor of the other conditions.

For the remaining gaps, I'm marking the ECS component ablation as camera-ready given time constraints, but I'm prioritizing the FPR-ASR Pareto analysis with explicit benign test set specification and representation analysis using CKA and cosine similarity—those are critical for the submission. I'm also extending the timeline to 14-16 days to separate what's submission-critical from what can wait for camera-ready.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b468154f-210a-4443-ab20-de995ae953b3",
  "isSidechain": false,
  "requestId": "req_011Cb6EmWU3bbZmh8bwiqWur",
  "type": "assistant",
  "uuid": "7138520c-a9b4-4fd5-b6eb-a6013196e13a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Np5MFb9U4ag487MENordhL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10589,
      "cache_read_input_tokens": 22339,
      "output_tokens": 7289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7289,
          "cache_read_input_tokens": 22339,
          "cache_creation_input_tokens": 10589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10589
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

_source line 19 · 2026-05-16T12:23:56.190Z_

【阶段】: 迭代第 2 轮
【发掘 agent 有效建议采纳】:
- **采纳发掘点 1**（机制重新表述）：这是本轮最高价值建议。当前"compositional encoding-detection primitives"的 framing 与泛化 claim 之间存在逻辑裂缝——base64 的检测 feature 不可能帮助识别 Braille。重新表述为"content-invariance under surface perturbation"：curriculum 迫使模型先在低噪声编码下锚定 harmful content 的 semantic signature，再在高噪声下保持这个 signature。这是 representation disentanglement 的 claim，逻辑链更闭合，也更 testable。
- **采纳发掘点 3**（rule-based 检测 trivial alternative）：上轮已回应 learned canonicalization，但遗漏了更 trivial 的"regex 检测 + 已知解码器 + 标准分类器"方案。需要明确建立 problem boundary：rule-based 对已知单层编码有效，但在 partial encoding、adversarial mixing、novel encoding 三个条件下失败。
- **采纳发掘点 4**（Curriculum Adversarial Training 差异化）：这是 Related Work 层面的硬伤。必须 explicitly 对比 Cai et al. (IJCAI 2018) 和 Wang et al. (NeurIPS 2021)，明确差异：(a) 连续 perturbation space vs. 离散 compositional attack space，(b) 仅验证 in-distribution vs. 验证 OOD 泛化到 unseen encoding families。
- **部分采纳发掘点 2**（general principle positioning）：Round 1 已做部分处理。本轮进一步在 Introduction 中将 formal conditions 前置（composable primitives + partial ordering + compositional feature learning），但不再加重 general principle 的 claim weight——审稿人可能会 pushback "只有一个 domain 的验证无法 claim general principle"。

【补救 agent 有效建议采纳】:
- **采纳缺陷 1**（canonicalization baseline）：增加 "Deterministic-Decode + LlamaGuard-3" baseline，零训练开销，用实际数字支撑理论论证。
- **采纳缺陷 2**（curriculum 多 seed）：Curriculum-ordered training 改为 3 seeds，报告 mean ± std，H1 加配对 t-test。
- **部分采纳缺陷 3**（ECS 组件 ablation）：标注为 camera-ready 实验（3× 额外训练对 submission timeline 太重），但在 ECS 设计段落中讨论 pilot study 中各组件的 difficulty correlation 作为初步证据。
- **采纳缺陷 4**（FPR-ASR tradeoff）：增加多阈值 Pareto 分析 + 明确 benign test set 来源（WildGuardTest benign + LMSYS-Chat-1M 采样）。
- **采纳缺陷 5**（时间线扩展）：扩展至 16 天，明确区分 submission-critical（H1-H3 + 核心 ablation）和 camera-ready（ECS component ablation、stability ablation、full 5-seed curriculum）。
- **采纳缺陷 6**（表征分析）：增加 CKA/cosine similarity 表征聚集度分析，直接验证"encoding-invariant representations"claim。仅需推理，无训练开销。这是本轮实验层面最高价值补丁。

【本轮 proposal 主要变更】:
**Idea 层面**:
- 核心机制从"compositional encoding-detection primitives"修正为"content-invariance under surface perturbation"（representation disentanglement framing）
- 明确建立 problem boundary：rule-based 方法在已知单层编码有效，本方法解决 partial encoding / adversarial mixing / novel encoding 场景
- 增加 Curriculum Adversarial Training (Cai et al., 2018; Wang et al., 2021) 的 explicit 差异化论述
- Novelty claim 聚焦："curriculum 在离散 compositional attack space 中诱导 OOD 泛化"——这是 prior curriculum adversarial training 未曾验证的 claim

**实验层面**:
- 增加 Deterministic-Decode + LlamaGuard-3 baseline
- Curriculum training 改为 3 seeds
- 增加 representation analysis（CKA/cosine similarity 验证 encoding-invariant features）
- 增加多阈值 FPR-ASR Pareto 分析 + 明确 benign test set
- 时间线扩展至 16 天，区分 submission-critical / camera-ready
- ECS component ablation 标为 camera-ready

【idea 质量评估】: Novelty=中偏强（"content-invariance via curriculum in discrete compositional space + OOD generalization"是一个 specific 且 testable 的 claim，与 prior curriculum adversarial training 有清晰差异化；但仍是单一 domain 验证，不能 claim paradigm-level novelty） Significance=中偏强（general principle positioning + encoding 作为 canonical instance 是合理的 framing，但审稿人可能仍认为 one-domain validation 不足以 establish generality） → idea 天花板约 42%

【实验完备性评估】: Technical Soundness=中偏强（表征分析直接验证核心 claim，多 seed + 统计检验提供严谨性，canonicalization baseline 用数据而非理论论证优势；主要剩余风险是 ECS ablation 不在首轮提交中、co-evolutionary loop 可能需要 fallback） → 地板已基本补好

【当前概率估计】: [26% - 38%] 中位 32%

【决策】: 继续

【决策理由】: 两个 agent 均未声明收敛，且本轮仍产出了高价值建议（尤其是发掘点 1 的机制修正和补救点 6 的表征分析），概率从 28% 升至 32%，距 36% 阈值还差一步。发掘 agent 的机制修正如果在下一轮得到确认为"已闭合"，加上补救 agent 确认实验设计无新漏洞，可能达到收敛条件。值得再迭代一轮。

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
## Title

EncoGuard: Learning Content-Invariant Safety Features via Complexity-Structured Curriculum for Encoding-Based Attacks

## Problem Statement

Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses fall into two categories, both with critical limitations:

1. **Rule-based detection + decoding pipelines** (e.g., regex-based encoding detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures, but fail on (a) partial encoding where only segments are transformed, (b) adversarial mixing of encoded/plaintext to evade detection heuristics, and (c) novel encodings without pre-programmed decoders.

2. **Learned canonicalization** (seq2seq decode → classify): Suffers from error propagation in nested encodings, creates a new adversarial attack surface (the canonicalizer itself), and requires semantic understanding to identify which portions to decode.

The core challenge is achieving **generalization to unseen encoding families**—classifiers that remain robust against encoding types never encountered during training. No existing defense reliably provides this capability.

## Core Thesis

We hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—learns **content-invariant safety features** that generalize to held-out encoding types unseen during training. The key mechanism is **representation disentanglement**: curriculum ordering forces the model to first anchor the semantic signature of harmful content under low-noise surface perturbations (simple encodings), then learn to preserve this semantic signature under progressively higher-noise perturbations (complex encodings). The result is a representation space where harmful content clusters by semantic meaning regardless of surface encoding—a separation of content features from encoding-specific surface features.

This differs fundamentally from memorizing encoding-specific detection patterns. A model that merely memorizes base64 character distributions cannot generalize to Braille; but a model that has learned to extract content semantics despite surface perturbation can generalize to any encoding that preserves underlying content structure.

**General Principle:** This approach instantiates a broader defense paradigm for compositional attack spaces: when attacks are built from composable primitives with natural complexity ordering, structured curriculum training can induce invariance to attack-specific surface features while preserving task-relevant content features. We demonstrate this principle on encoding attacks as the canonical instance where complexity is formally quantifiable.

## Relationship to Prior Work on Curriculum Adversarial Training

Curriculum-based approaches to adversarial robustness exist (Cai et al., IJCAI 2018: progressively increasing perturbation magnitude for image classifiers; Wang et al., NeurIPS 2021: ordered SGD by sample difficulty). Our work differs in two critical dimensions:

1. **Discrete compositional attack space vs. continuous perturbation space:** Prior work operates in continuous ε-ball perturbation spaces where difficulty is a scalar magnitude. Encoding attacks form a discrete compositional space where primitives (base64, ROT13, homoglyphs) can be arbitrarily nested—requiring a multi-dimensional complexity metric rather than a single scalar.

2. **OOD generalization vs. in-distribution robustness:** Prior curriculum adversarial training only evaluates robustness against the same attack types used during training (within the same ε-ball). We explicitly evaluate generalization to **entirely unseen encoding families** (Braille, Morse, custom ciphers)—demonstrating that curriculum ordering induces transferable content-invariance, not just better in-distribution fitting. This OOD generalization claim is our primary novel contribution.

## Key Contributions

1. **Primary Contribution (Representation Disentanglement via Curriculum):** We demonstrate that complexity-structured curriculum training produces content-invariant representations that generalize to entirely unseen encoding families (Braille, Morse, custom cipher, NATO phonetic), while flat augmentation and random-order training do not. We provide direct representation-level evidence (CKA similarity analysis) that curriculum-trained models cluster same-content different-encoding inputs more tightly than baselines.

2. **Formalized Encoding Complexity Score (ECS):** A principled complexity metric combining nesting depth, character-per-token (CPT) ratio deviation, and tokenizer perplexity. We validate that ECS predicts classifier difficulty on held-out encodings (Spearman ρ), establishing it as a transferable methodological contribution for any encoding-related defense work.

3. **Co-Evolutionary Training Framework:** GRPO-trained attacker generates encoding attacks of escalating ECS, paired with SFT classifier trained on curriculum-ordered adversarial data. The co-evolutionary dynamic ensures curriculum adapts to classifier capability frontier.

4. **Comprehensive Controlled Evaluation:** Controlled ablations (random-order, flat augmentation, reverse curriculum, static curriculum, decode-then-classify pipeline) with multi-seed statistical validation, supplemented by representation analysis directly verifying the content-invariance claim.

## Methodology

### Encoding Complexity Score (ECS)

$$ECS(e) = \alpha \cdot \text{NestingDepth}(e) + \beta \cdot \text{CPT\_Deviation}(e) + \gamma \cdot \text{TokenizerPerplexity}(e)$$

- NestingDepth: number of compositional encoding layers
- CPT_Deviation: absolute deviation of encoded text's characters-per-token ratio from plaintext baseline
- TokenizerPerplexity: perplexity of target model's tokenizer on encoded text

Weights determined via pilot study measuring correlation of each component with classifier error rate on a validation set. Pilot results reported to justify weight selection. Full leave-one-out component ablation planned for camera-ready.

### Mechanistic Motivation: Content-Invariance via Progressive Noise Escalation

Under flat exposure, the classifier simultaneously encounters simple encodings (low surface noise, content semantics still partially accessible through tokenization) and complex nested encodings (high surface noise, content semantics completely obscured at token level). For high-noise inputs in early training, the model cannot extract content signal—gradients from these samples are effectively random with respect to content features, interfering with content-feature learning on low-noise inputs.

Curriculum ordering resolves this by staged noise escalation:
- **Stage 1 (low-ECS):** Simple encodings partially preserve content-correlated token patterns. The model learns to extract harmful-content semantic features despite mild surface perturbation, anchoring a content representation.
- **Stage 2 (high-ECS):** Complex encodings fully obscure surface patterns. But the model already has anchored content features from Stage 1—it now learns to access these features through higher-noise channels, effectively learning encoding-invariance as noise robustness.

This predicts generalization: a model that has learned "extract content semantics despite surface noise" should transfer to any novel encoding that preserves content structure—regardless of the specific noise pattern. Braille (character substitution) and Morse (symbolic re-encoding) are different noise types but preserve content, so a content-invariant model should handle them.

### Why Not Simpler Alternatives?

**Rule-based detection + decode:** For known single-layer encodings (base64, ROT13) with distinctive character-set signatures, regex detection + decode + standard guardrail achieves high accuracy at near-zero cost. Our method targets the regime where this fails:
- **Partial encoding:** Only segments of input are encoded, defeating whole-input detection heuristics
- **Adversarial mixing:** Attacker deliberately mixes encoded/plaintext to create ambiguous statistical signatures
- **Novel encodings:** No pre-programmed decoder exists (the motivating scenario for generalization)

We include a Deterministic-Decode + LlamaGuard-3 baseline to empirically demonstrate this boundary.

**Learned canonicalization:** (1) Error propagation—each nested decode step compounds errors; (2) canonicalizer becomes a new attack surface; (3) partial encoding requires semantic understanding to identify decode targets.

### Co-Evolutionary Training Loop

**Attacker (Qwen2.5-1.5B, GRPO-trained):**
- Generates encoding attacks with ECS constrained to current curriculum stage
- Reward: +1 if encoding bypasses current classifier AND oracle confirms harmful content
- Entropy regularization prevents collapse to single encoding type

**Classifier (Qwen2.5-4B, SFT):**
- Trains on curriculum-ordered adversarial examples (Stage 1: ECS ≤ threshold, Stage 2: ECS > threshold)
- FPR rollback: revert checkpoint if FPR exceeds 2% on benign validation set
- Semantic deduplication: removes near-duplicates (cosine similarity > 0.95)

**Oracle:** GPT-4o judges content harmfulness. Deterministic decoder cross-validates; disagreements excluded.

**Fallback Plan:** If co-evolutionary loop proves unstable by Day 6, fall back to static curriculum-ordered SFT (pre-generated curriculum data, no GRPO attacker). This still validates H1-H3.

### Compute and Cost

- Hardware: 4× A100 80GB
- Classifier training: ~8h per run × 3 seeds × 2 stages = ~48h (parallelizable across GPUs)
- Baselines: random-order (5 seeds × 8h = 40h), flat augmentation (3 seeds × 8h = 24h), reverse curriculum (3 seeds × 8h = 24h), static curriculum (3 seeds × 8h = 24h)
- Attacker training: ~6h per round × 2 rounds = 12h
- Oracle: ~18K calls ≈ $200-350
- Representation analysis: inference only, ~2h
- Total: ~160h GPU-hours (manageable on 4×A100 over 16 days with parallelization)
- Compute normalization: training FLOPs (primary), with training tokens and wall-clock reported

## Experimental Design

### Hypotheses

- **H1 (Curriculum > Random):** Curriculum-ordered training achieves ≥10pp lower encoding-ASR than random-order at equivalent FLOPs (validated by paired t-test across seeds, p < 0.05).
- **H2 (OOD Generalization):** Curriculum-trained classifier maintains ≤30% encoding-ASR on held-out encoding families (Braille, Morse, custom cipher, NATO phonetic) where random-order and flat augmentation exceed 60%.
- **H3 (ECS Predictiveness):** ECS correlates with classifier error rate (Spearman ρ ≥ 0.7) on held-out encodings.
- **H4 (Co-evolution > Static):** Co-evolutionary training outperforms static curriculum SFT by ≥5pp on composite encodings (conditional on co-evolutionary loop stability).

### Baselines and Ablations

**Controlled comparisons (same architecture, same FLOPs, multi-seed):**
1. Random-order training: 5 seeds, mean ± std
2. Flat augmentation: 3 seeds
3. Reverse curriculum (high-ECS first, then low-ECS): 3 seeds
4. Static curriculum SFT (no co-evolutionary attacker): 3 seeds
5. **Deterministic-Decode + LlamaGuard-3 pipeline:** Deterministic decoder attempts to decode input, decoded text classified by LlamaGuard-3. No training needed.

**Curriculum (our method):** 3 seeds, mean ± std

**Indicative comparisons (Discussion section):**
6. Broken-Token CPT-Filtering (published numbers)
7. TRYLOCK Layer 0 (published numbers)

### Evaluation Protocol

**External benchmarks (primary evidence):**
- HarmBench encoding-perturbed variant
- JailbreakBench encoding attack subset
- WildGuardTest encoding-perturbed variant

**EncoAttack (supplementary analysis):**
- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150), 10+ harm categories
- 8 encoding types × 3 nesting levels = 12,000 test cases
- Independent encoding implementation from training pipeline
- Validation: ≥80% bypass rate on undefended LlamaGuard-3

**Held-out encoding families (generalization test—NEVER seen during training):**
- Braille Unicode substitution
- Morse code symbolic encoding
- Custom Caesar-variant cipher (position-dependent shift)
- NATO phonetic alphabet encoding

**Metrics:**
- Encoding-ASR (primary)
- Clean FPR at multiple thresholds (0.5%, 1%, 2%, 5%) with Pareto frontier analysis
- Benign test set: WildGuardTest benign split (~1000) + LMSYS-Chat-1M random sample (1000)
- Per-encoding-type breakdown
- ECS-difficulty correlation on held-out encodings

### Representation Analysis (Direct Evidence for Content-Invariance)

For each of 100 harmful prompts, generate plaintext + 8 encoding variants. Extract classifier penultimate-layer representations. Compute:
1. **Intra-prompt cross-encoding similarity:** Average cosine similarity between same-prompt different-encoding representations
2. **CKA analysis:** Centered Kernel Alignment between encoding-variant representation matrices
3. **Compare curriculum-trained vs. random-order-trained:** Prediction—curriculum model shows significantly higher intra-prompt similarity (content clusters by meaning, not by encoding type)

This directly validates "encoding-invariant representations" without relying solely on task-level metrics.

### Learning Dynamics

- Per-checkpoint (every 500 steps) encoding-ASR curves
- Separate curves for low-ECS and high-ECS encodings
- Expected: curriculum shows earlier convergence on low-ECS, smooth transition to high-ECS; random-order shows chaotic learning on both

### Oracle Reliability Pilot

Before full training: 100 samples per ECS band, measure GPT-4o agreement with deterministic decoder. If agreement < 80% for high-ECS, switch to deterministic-only oracle for Stage 2.

## Stability Mechanisms (Not Claimed as Contributions)

- Entropy regularization (from TriPlay-RL diversity penalty)
- FPR rollback (standard safety constraint)
- Semantic deduplication (standard data quality)

Trigger frequencies reported as indirect utility evidence. Full ablation in camera-ready.

## Timeline (16 days)

**Submission-critical (Days 1-12):**
- Days 1-3: ECS implementation, encoding generators, data pipeline, oracle pilot
- Days 4-7: Curriculum training (3 seeds) + random-order (5 seeds) + flat augmentation (3 seeds) [parallelized across GPUs]
- Days 8-9: Reverse curriculum (3 seeds) + decode-pipeline baseline + co-evolutionary attempt
- Days 10-11: Full evaluation on all benchmarks + held-out encodings + representation analysis
- Day 12: Core results analysis, statistical tests, main writing

**Camera-ready extensions (Days 13-16 + post-submission):**
- Day 13-14: ECS component leave-one-out ablation (3 runs)
- Day 15: Stability mechanism ablation
- Day 16: Writing polish, full 5-seed curriculum if time permits

**Fallback trigger:** If co-evolutionary loop unstable by Day 6, switch to static curriculum SFT.
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7138520c-a9b4-4fd5-b6eb-a6013196e13a",
  "isSidechain": false,
  "requestId": "req_011Cb6EmWU3bbZmh8bwiqWur",
  "type": "assistant",
  "uuid": "a5436d94-54d1-46e5-a397-31c679397332",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Np5MFb9U4ag487MENordhL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10589,
      "cache_read_input_tokens": 22339,
      "output_tokens": 7289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7289,
          "cache_read_input_tokens": 22339,
          "cache_creation_input_tokens": 10589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10589
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: 前提假设质疑 / 核心 claim 强化 - 内容: 当前 proposal 的逻辑链存在一个未弥合的跳跃：mechanistic explanati…",
  "leafUuid": "a5436d94-54d1-46e5-a397-31c679397332",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: 前提假设质疑 / 核心 claim 强化 - 内容: 当前 proposal 的逻辑链存在一个未弥合的跳跃：mechanistic explanati…",
  "leafUuid": "a5436d94-54d1-46e5-a397-31c679397332",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 25 · 2026-05-16T12:26:03.794Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:26:03.794Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "content": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\n【状态】: 有发掘空间\n\n---\n\n【发掘点 1】\n- 维度: 前提假设质疑\n- 内容: \"Content-invariant features\" 这一核心 framing 存在概念上的内在张力。对于高 ECS 编码（如多层 base64 嵌套），token-level representation 与原始内容之间的语义关系已被完全摧毁——tokens 本质上是随机字符相对于原文内容。在这种情况下，模型要成功分类，逻辑上只有两条路径：(a) 隐式学会解码（encoding-specific，恰恰不是 invariant），或 (b) 学会识别\"编码文本的统计特征与有害内容的统计特征之间的相关性\"（也是 encoding-specific）。那么所谓的\"content-invariant feature\"在 token 空间中具体对应的是什么？如果模型实际学到的是\"多样化的编码结构识别+隐式解码策略组合\"（即 meta-decoding capabilities），那应该用更精确的语言表达这一机制——比如 \"compositional encoding-structure awareness\" 或 \"generalized decoding inductive bias\"。当前 framing 暗示存在一种直接绕过编码、直达内容语义的表征，但这在信息论上对完全打乱 token 映射的编码是不成立的。修正这一 framing 不仅更诚实，还能让 reviewer 更难以 \"mechanism claim 缺乏理论支撑\" 来攻击。\n- 价值: 直接关系到 Novelty 和核心 claim 的逻辑强度。如果核心机制描述本身有概念漏洞，reviewer 的第一反应是 \"authors don't understand their own method\"——这是致命的。精确化机制描述反而能让 contribution 更 defensible。\n\n【发掘点 2】\n- 维度: significance 提升\n- 内容: 当前 proposal 将 \"general principle\"（curriculum for compositional attack spaces）作为 secondary framing 放在 Core Thesis 末尾。但这个 general principle 才是真正有 lasting impact 的贡献——编码攻击只是一个 demonstration instance。建议将论文的 primary framing 提升为：\"我们发现，对于由可组合原语构成的离散攻击空间，如果原语具有自然复杂度序，curriculum ordering 可以诱导出超越训练分布的 invariance。\" 编码攻击作为 canonical testbed（因为复杂度可精确量化）。这种提升的好处是：(1) 扩大了潜在引用范围（任何面对 compositional adversarial space 的工作都可引用），(2) 让审稿人觉得\"即使编码攻击的具体结果 margin 不够大，general principle 本身仍值得发表\"，(3) 与未来工作的连接更有说服力（prompt injection 的组合攻击、multi-modal 的组合扰动等）。\n- 价值: 命中 Significance 维度。将一个\"specific defense technique paper\"提升为\"reveals a general training principle with encoding attacks as formal demonstration\"，显著抬高了影响力天花板。\n\n【发掘点 3】\n- 维度: related work 差异化\n- 内容: 当前 proposal 将自己定位在\"curriculum adversarial training\"文献中做差异化（Cai et al., Wang et al.）。但实际上更具威胁性的相关文献是 **domain generalization (DG)** 领域——特别是 progressive/sequential domain adaptation。本质上，每种编码类型就是一个 domain，OOD generalization 到 unseen encoding = generalization to unseen domains。DG 领域有大量关于\"如何从多个 source domain 学到 domain-invariant features 以泛化到 unseen target domain\"的工作（DANN, CORAL, IRM, DRO 等）。如果不主动定位和区分，reviewer 很可能会说 \"this is just domain generalization applied to encoding attacks, what's new?\" 建议显式讨论：为什么 standard DG 方法（如 invariant risk minimization）不直接适用于此处（离散组合空间、domain 数目爆炸、无法在 training 时显式枚举所有 domains），以及为什么 curriculum ordering 在此结构下比 standard DG 方法更 natural。\n- 价值: 命中 Related Work 差异化维度。提前封堵一个高概率的 reviewer objection，同时通过连接到更大的文献体系来强化理论 grounding。\n\n【发掘点 4】\n- 维度: novelty 锐化\n- 内容: 当前 OOD generalization claim 的\"OOD\"定义需要更锐利。Held-out encodings 是 Braille（字符替换）、Morse（符号重编码）、custom cipher（位移）、NATO（词替换）。但 training distribution 已经包含了 base64（字符重编码）、ROT13（位移）、homoglyph（字符替换）。从 encoding 的 structural principle 看，Braille 和 homoglyph 都是 character-level substitution，Morse 和 base64 都是 symbolic re-encoding，custom cipher 和 ROT13 都是 shift-based。那么 \"OOD\" 的实质含义是什么——是 specific mapping function 的 OOD，还是 encoding principle 的 OOD？如果是前者，这其实是同一 encoding family 内的 interpolation 而非真正的 extrapolation，novelty 大打折扣。建议：(a) 明确区分 \"encoding principle OOD\"（如 steganographic encoding，其中 harmful content 被嵌入看似 benign 的自然语言中——这是一个与训练中所有 encoding 都有 qualitative difference 的 family）和 \"mapping function OOD\"，(b) 在 held-out set 中加入至少一种 truly structurally different encoding（如 whitespace steganography, invisible Unicode characters），以强化 OOD claim 的说服力。\n- 价值: 命中 Novelty 维度。OOD generalization 是 primary novel contribution——如果 reviewer 能论证 held-out encodings 只是 interpolation，整个 novelty claim 崩塌。锐化 OOD 的定义和证据是守护核心 contribution 的关键。\n\n【发掘点 5】\n- 维度: trivial alternative 威胁\n- 内容: 当前 proposal 讨论了 \"rule-based decode + classify\" 和 \"learned canonicalization\" 两个 trivial alternatives。但遗漏了一个更具威胁性的 baseline：**直接用强 LLM（如 GPT-4 或 Claude）做 zero-shot 分类**，prompt 为 \"This text may be encoded. Determine if the underlying content is harmful.\" 当前的强 LLM 在 pre-training 中已见过大量编码形式，具备一定的隐式解码能力。如果 GPT-4 zero-shot 在 held-out encodings 上已经表现 reasonable，那 EncoGuard 的增量价值需要从 **efficiency**（轻量级 4B 模型 vs. API cost）和 **latency**（毫秒级 vs. 秒级）角度来论证，而不仅仅是 accuracy。建议在 framing 中预先定位：EncoGuard 解决的是 \"deployment-practical robust detection\"——在推理成本受限（不能对每个 input 调用 GPT-4）的场景下实现接近 frontier model 的编码鲁棒性。这把问题从\"能不能做到\"变成\"在什么约束下做到\"，更 defensible。\n- 价值: 命中 Novelty 维度（避免被 \"just use GPT-4\" 的 reviewer comment 击穿）。同时通过精确定位 value proposition，让 contribution 更 crisp。\n\n【补救 agent 本轮输出】:\n【状态】: 有缺陷待补救\n\n---\n\n【缺陷 1】\n- 类别: 实验设计不足（统计效力）\n- 问题: H1 声称用 paired t-test (p < 0.05) 验证 curriculum > random-order，但 curriculum 方法只有 3 seeds。3 个样本的 t-test 自由度为 2，统计功效极低——即使真实效应存在，也很难在 p<0.05 下拒绝零假设。更关键的是，curriculum 3 seeds vs. random-order 5 seeds 的不对称设计无法做标准 paired t-test（配对要求样本量相同）。这是一个审稿人几乎必然会挑战的统计设计缺陷。\n- 严重度: 可补救\n- 补救方案: (1) 将 curriculum 方法也跑 5 seeds，与 random-order 对齐，做 paired comparison（每对 seed 用相同 random initialization）；或者 (2) 若计算资源限制 seed 数量，改用 bootstrap confidence interval 或 Wilcoxon rank-sum test（非参数），不声称 paired t-test；(3) 在 timeline 中，Day 16 提到的 \"full 5-seed curriculum if time permits\" 应提升为 submission-critical，因为这是核心 claim H1 的统计基础。额外 2 runs × 8h = 16h GPU 在 4×A100 上完全可行。\n\n【缺陷 2】\n- 类别: baseline 不足或过时\n- 问题: Proposal 明确论述了 \"learned canonicalization (seq2seq decode → classify)\" 作为现有防御的第二大类，并从理论上指出其缺陷（error propagation, new attack surface）。但实验中完全没有包含这类 baseline 的实证比较——只有 Deterministic-Decode + LlamaGuard-3（规则解码，非学习式）。审稿人会质疑：你声称比 learned canonicalization 更好，但没有实验证据。\n- 严重度: 可补救\n- 补救方案: 添加一个 learned decode-then-classify baseline。具体方案：(1) 用同规模模型（Qwen2.5-4B 或更小）fine-tune 一个 seq2seq decoder（input: encoded text, output: decoded plaintext），在相同训练编码类型上训练，然后将解码输出送入 LlamaGuard-3 分类。(2) 如果从头训练 canonicalizer 计算负担过重，可以使用 ALMA 或已有的 text normalization model 作为 proxy。(3) 最低成本替代：在 Discussion section 承认这是 limitation，但至少对 nested encoding 场景展示 deterministic decode 的 error propagation 曲线（随 nesting depth 增加，decode accuracy 如何衰减），间接支持论点。\n\n【缺陷 3】\n- 类别: compute 公平性问题\n- 问题: 核心方法包含 co-evolutionary loop（GRPO attacker 12h + classifier curriculum training），而所有 baselines 只有 classifier 训练。Co-evolutionary 方法总 compute 明显超过 baselines。Proposal 声称 \"same FLOPs\" 但这只能指 classifier 部分的 FLOPs；attacker 的训练 FLOPs 和 oracle 调用是额外开销。H4 的 \"co-evolution > static\" 比较尤其需要澄清：如果把 co-evolution 的额外 compute 分配给 static baseline（如更多 epoch、更多 augmented data），static 是否仍逊色？\n- 严重度: 可补救\n- 补救方案: (1) 明确区分两层比较：H1-H3 的核心 claim 基于 static curriculum vs. baselines（compute 严格匹配），H4 是 bonus claim；(2) 对 H4，增加一个 \"compute-matched static curriculum\" 变体：把 co-evolutionary 额外消耗的 FLOPs 转化为 static curriculum 的 additional training steps 或 data augmentation rounds，证明 co-evolution 的优势不仅仅来自更多 compute；(3) 在 Table 中报告每个方法的 total training FLOPs（含 attacker 训练），让读者自行判断。\n\n【缺陷 4】\n- 类别: 实验设计不足（baseline 定义模糊）\n- 问题: \"Random-order training\" 和 \"Flat augmentation\" 作为两个独立 baselines，但 proposal 未清晰定义二者区别。Random-order 是否指使用相同的 curriculum-staged data 但打乱顺序？Flat augmentation 是否指从所有编码类型中均匀采样而不分 stage？如果区别仅在于 data sampling strategy，需要明确；如果二者本质相同，则其中一个是冗余的。审稿人会追问 \"your random-order and flat augmentation baselines seem identical.\"\n- 严重度: 可补救\n- 补救方案: 明确定义：(1) Random-order = 使用与 curriculum 完全相同的训练数据（含 co-evolutionary 生成或 static 数据），但呈现顺序完全随机化；(2) Flat augmentation = 对每个 base prompt，在每个 epoch 随机采样一种编码类型进行增强，不使用 ECS-ordered data generation，数据分布可能与 curriculum 不同。两者的关键区别应是：random-order 控制 data composition（isolates ordering effect），flat augmentation 控制 data generation strategy（different data distribution entirely）。在 methodology section 用一个对比表明确说明。\n\n【缺陷 5】\n- 类别: 评估方案缺陷（representation claim 证据链不完整）\n- 问题: Proposal 的核心机制 claim 是 \"content-invariant representations\"（content clusters by meaning, not encoding type）。当前证据是 CKA + intra-prompt cosine similarity。但这些只能说明 same-content different-encoding 的表征更相似，不能直接证明 encoding information 被 disentangled out。一个模型可能同时保留 content 和 encoding 信息——只是 content 维度的 variance 更大。\n- 严重度: 可补救\n- 补救方案: 添加 linear probing experiment：(1) 在 curriculum-trained vs. random-order-trained 模型的 penultimate layer representations 上，分别训练两个 linear probe——一个预测 content category（harmful type），一个预测 encoding type。(2) Prediction: curriculum model 的 encoding-type probe accuracy 应显著低于 random-order model（encoding info 被丢弃），而 content-type probe accuracy 应更高或相当。这直接验证 \"disentanglement\" 而非仅仅 \"similarity\"。计算成本极低（linear probe 训练 < 5 min），可在 Day 10-11 的 representation analysis 阶段完成。\n\n【缺陷 6】\n- 类别: 评估方案缺陷（ECS 作为 contribution 的验证不足）\n- 问题: ECS 被列为第二大 contribution，但其 component weight 的 ablation（\"Full leave-one-out component ablation\"）被推迟到 camera-ready。Submission 版本只有 pilot study justification + Spearman ρ 相关性。审稿人会质疑：如果 ECS 的 3 个 component 中某个 dominates（如 NestingDepth alone achieves ρ ≥ 0.65），那 ECS 作为 \"formalized metric\" 的增量贡献存疑。\n- 严重度: 可补救\n- 补救方案: 将 ECS component ablation 从 camera-ready 提升到 submission-critical。具体：(1) 计算 NestingDepth alone、CPT_Deviation alone、TokenizerPerplexity alone 分别与 classifier error 的 Spearman ρ；(2) 计算 leave-one-out（去掉每个 component）的 ρ 下降；(3) 这不需要重新训练模型，只需要在已有 evaluation data 上计算相关性——纯 inference/statistics 工作，< 2h。放在 Day 10-11 完成。\n\n【缺陷 7】\n- 类别: 可行性问题（timeline 紧张度）\n- 问题: 16 天 timeline 中，Days 4-7 需要完成 11 runs（3 curriculum + 5 random + 3 flat），Days 8-9 再加 6 runs（3 reverse + co-evolutionary）+ decode pipeline。这假设所有 runs 一次成功，无需 hyperparameter tuning。实际操作中，第一轮 curriculum training 几乎必然需要 ECS threshold 调参（何时从 Stage 1 过渡到 Stage 2）、learning rate warm-up 调整等。如果 Day 4 的第一次 curriculum run 不收敛或 FPR 过高触发 rollback，整个 timeline 后移。\n- 严重度: 可补救\n- 补救方案: (1) Days 1-3 的 pilot phase 中增加 1 次 fast curriculum run（reduced data, 2h）用于验证 training dynamics 和 ECS threshold 的 rough range；(2) 为 Days 4-7 预留 1 天 buffer（可从 Day 13-14 的 camera-ready 工作中借）；(3) 如果 seed variance 大导致需要更多 runs，优先保证核心 H1 的 5-seed curriculum（最重要的统计 claim），其他 baselines 可接受 3 seeds。\n\n---\n\n**总结**：实验设计的整体框架是 solid 的（ablation 轴线合理、外部 benchmark 使用得当、held-out generalization 设计清晰、fallback plan 务实）。上述缺陷均为可补救的技术细节问题，不存在方向性致命缺陷。其中**缺陷 1（统计效力）**和**缺陷 5（probing experiment）**是审稿人最可能提出的 concern，建议优先处理。"
}
```

---

### Runtime record

_source line 26 · 2026-05-16T12:26:03.794Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:26:03.794Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

## Round 3

10 recorded events

### User

_source line 27 · 2026-05-16T12:26:03.819Z_

【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
【状态】: 有发掘空间

---

【发掘点 1】
- 维度: 前提假设质疑
- 内容: "Content-invariant features" 这一核心 framing 存在概念上的内在张力。对于高 ECS 编码（如多层 base64 嵌套），token-level representation 与原始内容之间的语义关系已被完全摧毁——tokens 本质上是随机字符相对于原文内容。在这种情况下，模型要成功分类，逻辑上只有两条路径：(a) 隐式学会解码（encoding-specific，恰恰不是 invariant），或 (b) 学会识别"编码文本的统计特征与有害内容的统计特征之间的相关性"（也是 encoding-specific）。那么所谓的"content-invariant feature"在 token 空间中具体对应的是什么？如果模型实际学到的是"多样化的编码结构识别+隐式解码策略组合"（即 meta-decoding capabilities），那应该用更精确的语言表达这一机制——比如 "compositional encoding-structure awareness" 或 "generalized decoding inductive bias"。当前 framing 暗示存在一种直接绕过编码、直达内容语义的表征，但这在信息论上对完全打乱 token 映射的编码是不成立的。修正这一 framing 不仅更诚实，还能让 reviewer 更难以 "mechanism claim 缺乏理论支撑" 来攻击。
- 价值: 直接关系到 Novelty 和核心 claim 的逻辑强度。如果核心机制描述本身有概念漏洞，reviewer 的第一反应是 "authors don't understand their own method"——这是致命的。精确化机制描述反而能让 contribution 更 defensible。

【发掘点 2】
- 维度: significance 提升
- 内容: 当前 proposal 将 "general principle"（curriculum for compositional attack spaces）作为 secondary framing 放在 Core Thesis 末尾。但这个 general principle 才是真正有 lasting impact 的贡献——编码攻击只是一个 demonstration instance。建议将论文的 primary framing 提升为："我们发现，对于由可组合原语构成的离散攻击空间，如果原语具有自然复杂度序，curriculum ordering 可以诱导出超越训练分布的 invariance。" 编码攻击作为 canonical testbed（因为复杂度可精确量化）。这种提升的好处是：(1) 扩大了潜在引用范围（任何面对 compositional adversarial space 的工作都可引用），(2) 让审稿人觉得"即使编码攻击的具体结果 margin 不够大，general principle 本身仍值得发表"，(3) 与未来工作的连接更有说服力（prompt injection 的组合攻击、multi-modal 的组合扰动等）。
- 价值: 命中 Significance 维度。将一个"specific defense technique paper"提升为"reveals a general training principle with encoding attacks as formal demonstration"，显著抬高了影响力天花板。

【发掘点 3】
- 维度: related work 差异化
- 内容: 当前 proposal 将自己定位在"curriculum adversarial training"文献中做差异化（Cai et al., Wang et al.）。但实际上更具威胁性的相关文献是 **domain generalization (DG)** 领域——特别是 progressive/sequential domain adaptation。本质上，每种编码类型就是一个 domain，OOD generalization 到 unseen encoding = generalization to unseen domains。DG 领域有大量关于"如何从多个 source domain 学到 domain-invariant features 以泛化到 unseen target domain"的工作（DANN, CORAL, IRM, DRO 等）。如果不主动定位和区分，reviewer 很可能会说 "this is just domain generalization applied to encoding attacks, what's new?" 建议显式讨论：为什么 standard DG 方法（如 invariant risk minimization）不直接适用于此处（离散组合空间、domain 数目爆炸、无法在 training 时显式枚举所有 domains），以及为什么 curriculum ordering 在此结构下比 standard DG 方法更 natural。
- 价值: 命中 Related Work 差异化维度。提前封堵一个高概率的 reviewer objection，同时通过连接到更大的文献体系来强化理论 grounding。

【发掘点 4】
- 维度: novelty 锐化
- 内容: 当前 OOD generalization claim 的"OOD"定义需要更锐利。Held-out encodings 是 Braille（字符替换）、Morse（符号重编码）、custom cipher（位移）、NATO（词替换）。但 training distribution 已经包含了 base64（字符重编码）、ROT13（位移）、homoglyph（字符替换）。从 encoding 的 structural principle 看，Braille 和 homoglyph 都是 character-level substitution，Morse 和 base64 都是 symbolic re-encoding，custom cipher 和 ROT13 都是 shift-based。那么 "OOD" 的实质含义是什么——是 specific mapping function 的 OOD，还是 encoding principle 的 OOD？如果是前者，这其实是同一 encoding family 内的 interpolation 而非真正的 extrapolation，novelty 大打折扣。建议：(a) 明确区分 "encoding principle OOD"（如 steganographic encoding，其中 harmful content 被嵌入看似 benign 的自然语言中——这是一个与训练中所有 encoding 都有 qualitative difference 的 family）和 "mapping function OOD"，(b) 在 held-out set 中加入至少一种 truly structurally different encoding（如 whitespace steganography, invisible Unicode characters），以强化 OOD claim 的说服力。
- 价值: 命中 Novelty 维度。OOD generalization 是 primary novel contribution——如果 reviewer 能论证 held-out encodings 只是 interpolation，整个 novelty claim 崩塌。锐化 OOD 的定义和证据是守护核心 contribution 的关键。

【发掘点 5】
- 维度: trivial alternative 威胁
- 内容: 当前 proposal 讨论了 "rule-based decode + classify" 和 "learned canonicalization" 两个 trivial alternatives。但遗漏了一个更具威胁性的 baseline：**直接用强 LLM（如 GPT-4 或 Claude）做 zero-shot 分类**，prompt 为 "This text may be encoded. Determine if the underlying content is harmful." 当前的强 LLM 在 pre-training 中已见过大量编码形式，具备一定的隐式解码能力。如果 GPT-4 zero-shot 在 held-out encodings 上已经表现 reasonable，那 EncoGuard 的增量价值需要从 **efficiency**（轻量级 4B 模型 vs. API cost）和 **latency**（毫秒级 vs. 秒级）角度来论证，而不仅仅是 accuracy。建议在 framing 中预先定位：EncoGuard 解决的是 "deployment-practical robust detection"——在推理成本受限（不能对每个 input 调用 GPT-4）的场景下实现接近 frontier model 的编码鲁棒性。这把问题从"能不能做到"变成"在什么约束下做到"，更 defensible。
- 价值: 命中 Novelty 维度（避免被 "just use GPT-4" 的 reviewer comment 击穿）。同时通过精确定位 value proposition，让 contribution 更 crisp。

【补救 agent 本轮输出】:
【状态】: 有缺陷待补救

---

【缺陷 1】
- 类别: 实验设计不足（统计效力）
- 问题: H1 声称用 paired t-test (p < 0.05) 验证 curriculum > random-order，但 curriculum 方法只有 3 seeds。3 个样本的 t-test 自由度为 2，统计功效极低——即使真实效应存在，也很难在 p<0.05 下拒绝零假设。更关键的是，curriculum 3 seeds vs. random-order 5 seeds 的不对称设计无法做标准 paired t-test（配对要求样本量相同）。这是一个审稿人几乎必然会挑战的统计设计缺陷。
- 严重度: 可补救
- 补救方案: (1) 将 curriculum 方法也跑 5 seeds，与 random-order 对齐，做 paired comparison（每对 seed 用相同 random initialization）；或者 (2) 若计算资源限制 seed 数量，改用 bootstrap confidence interval 或 Wilcoxon rank-sum test（非参数），不声称 paired t-test；(3) 在 timeline 中，Day 16 提到的 "full 5-seed curriculum if time permits" 应提升为 submission-critical，因为这是核心 claim H1 的统计基础。额外 2 runs × 8h = 16h GPU 在 4×A100 上完全可行。

【缺陷 2】
- 类别: baseline 不足或过时
- 问题: Proposal 明确论述了 "learned canonicalization (seq2seq decode → classify)" 作为现有防御的第二大类，并从理论上指出其缺陷（error propagation, new attack surface）。但实验中完全没有包含这类 baseline 的实证比较——只有 Deterministic-Decode + LlamaGuard-3（规则解码，非学习式）。审稿人会质疑：你声称比 learned canonicalization 更好，但没有实验证据。
- 严重度: 可补救
- 补救方案: 添加一个 learned decode-then-classify baseline。具体方案：(1) 用同规模模型（Qwen2.5-4B 或更小）fine-tune 一个 seq2seq decoder（input: encoded text, output: decoded plaintext），在相同训练编码类型上训练，然后将解码输出送入 LlamaGuard-3 分类。(2) 如果从头训练 canonicalizer 计算负担过重，可以使用 ALMA 或已有的 text normalization model 作为 proxy。(3) 最低成本替代：在 Discussion section 承认这是 limitation，但至少对 nested encoding 场景展示 deterministic decode 的 error propagation 曲线（随 nesting depth 增加，decode accuracy 如何衰减），间接支持论点。

【缺陷 3】
- 类别: compute 公平性问题
- 问题: 核心方法包含 co-evolutionary loop（GRPO attacker 12h + classifier curriculum training），而所有 baselines 只有 classifier 训练。Co-evolutionary 方法总 compute 明显超过 baselines。Proposal 声称 "same FLOPs" 但这只能指 classifier 部分的 FLOPs；attacker 的训练 FLOPs 和 oracle 调用是额外开销。H4 的 "co-evolution > static" 比较尤其需要澄清：如果把 co-evolution 的额外 compute 分配给 static baseline（如更多 epoch、更多 augmented data），static 是否仍逊色？
- 严重度: 可补救
- 补救方案: (1) 明确区分两层比较：H1-H3 的核心 claim 基于 static curriculum vs. baselines（compute 严格匹配），H4 是 bonus claim；(2) 对 H4，增加一个 "compute-matched static curriculum" 变体：把 co-evolutionary 额外消耗的 FLOPs 转化为 static curriculum 的 additional training steps 或 data augmentation rounds，证明 co-evolution 的优势不仅仅来自更多 compute；(3) 在 Table 中报告每个方法的 total training FLOPs（含 attacker 训练），让读者自行判断。

【缺陷 4】
- 类别: 实验设计不足（baseline 定义模糊）
- 问题: "Random-order training" 和 "Flat augmentation" 作为两个独立 baselines，但 proposal 未清晰定义二者区别。Random-order 是否指使用相同的 curriculum-staged data 但打乱顺序？Flat augmentation 是否指从所有编码类型中均匀采样而不分 stage？如果区别仅在于 data sampling strategy，需要明确；如果二者本质相同，则其中一个是冗余的。审稿人会追问 "your random-order and flat augmentation baselines seem identical."
- 严重度: 可补救
- 补救方案: 明确定义：(1) Random-order = 使用与 curriculum 完全相同的训练数据（含 co-evolutionary 生成或 static 数据），但呈现顺序完全随机化；(2) Flat augmentation = 对每个 base prompt，在每个 epoch 随机采样一种编码类型进行增强，不使用 ECS-ordered data generation，数据分布可能与 curriculum 不同。两者的关键区别应是：random-order 控制 data composition（isolates ordering effect），flat augmentation 控制 data generation strategy（different data distribution entirely）。在 methodology section 用一个对比表明确说明。

【缺陷 5】
- 类别: 评估方案缺陷（representation claim 证据链不完整）
- 问题: Proposal 的核心机制 claim 是 "content-invariant representations"（content clusters by meaning, not encoding type）。当前证据是 CKA + intra-prompt cosine similarity。但这些只能说明 same-content different-encoding 的表征更相似，不能直接证明 encoding information 被 disentangled out。一个模型可能同时保留 content 和 encoding 信息——只是 content 维度的 variance 更大。
- 严重度: 可补救
- 补救方案: 添加 linear probing experiment：(1) 在 curriculum-trained vs. random-order-trained 模型的 penultimate layer representations 上，分别训练两个 linear probe——一个预测 content category（harmful type），一个预测 encoding type。(2) Prediction: curriculum model 的 encoding-type probe accuracy 应显著低于 random-order model（encoding info 被丢弃），而 content-type probe accuracy 应更高或相当。这直接验证 "disentanglement" 而非仅仅 "similarity"。计算成本极低（linear probe 训练 < 5 min），可在 Day 10-11 的 representation analysis 阶段完成。

【缺陷 6】
- 类别: 评估方案缺陷（ECS 作为 contribution 的验证不足）
- 问题: ECS 被列为第二大 contribution，但其 component weight 的 ablation（"Full leave-one-out component ablation"）被推迟到 camera-ready。Submission 版本只有 pilot study justification + Spearman ρ 相关性。审稿人会质疑：如果 ECS 的 3 个 component 中某个 dominates（如 NestingDepth alone achieves ρ ≥ 0.65），那 ECS 作为 "formalized metric" 的增量贡献存疑。
- 严重度: 可补救
- 补救方案: 将 ECS component ablation 从 camera-ready 提升到 submission-critical。具体：(1) 计算 NestingDepth alone、CPT_Deviation alone、TokenizerPerplexity alone 分别与 classifier error 的 Spearman ρ；(2) 计算 leave-one-out（去掉每个 component）的 ρ 下降；(3) 这不需要重新训练模型，只需要在已有 evaluation data 上计算相关性——纯 inference/statistics 工作，< 2h。放在 Day 10-11 完成。

【缺陷 7】
- 类别: 可行性问题（timeline 紧张度）
- 问题: 16 天 timeline 中，Days 4-7 需要完成 11 runs（3 curriculum + 5 random + 3 flat），Days 8-9 再加 6 runs（3 reverse + co-evolutionary）+ decode pipeline。这假设所有 runs 一次成功，无需 hyperparameter tuning。实际操作中，第一轮 curriculum training 几乎必然需要 ECS threshold 调参（何时从 Stage 1 过渡到 Stage 2）、learning rate warm-up 调整等。如果 Day 4 的第一次 curriculum run 不收敛或 FPR 过高触发 rollback，整个 timeline 后移。
- 严重度: 可补救
- 补救方案: (1) Days 1-3 的 pilot phase 中增加 1 次 fast curriculum run（reduced data, 2h）用于验证 training dynamics 和 ECS threshold 的 rough range；(2) 为 Days 4-7 预留 1 天 buffer（可从 Day 13-14 的 camera-ready 工作中借）；(3) 如果 seed variance 大导致需要更多 runs，优先保证核心 H1 的 5-seed curriculum（最重要的统计 claim），其他 baselines 可接受 3 seeds。

---

**总结**：实验设计的整体框架是 solid 的（ablation 轴线合理、外部 benchmark 使用得当、held-out generalization 设计清晰、fallback plan 务实）。上述缺陷均为可补救的技术细节问题，不存在方向性致命缺陷。其中**缺陷 1（统计效力）**和**缺陷 5（probing experiment）**是审稿人最可能提出的 concern，建议优先处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5436d94-54d1-46e5-a397-31c679397332",
  "isSidechain": false,
  "promptId": "870c6e02-7044-49c5-aafc-72260f4e94f6",
  "type": "user",
  "uuid": "fcc9413c-7a76-46b6-897d-4dc715806395",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-16T12:27:09.745Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the Round 3 outputs from both agents.

**发掘 agent Round 3:**

1. **发掘点 1 (前提假设质疑 - content-invariance framing 的概念张力):** This is a very sharp observation. For high-ECS encodings (multi-layer base64), tokens are essentially random characters w.r.t. content — the model can't possibly learn "content-invariant features" in the literal sense because content information is destroyed at token level. The model must be doing either (a) implicit decoding (encoding-specific, not invariant) or (b) statistical correlation between encoding patterns and harmful content (also encoding-specific). 

The suggestion to reframe as "generalized decoding inductive bias" or "compositional encoding-structure awareness" is more intellectually honest and defensible — it directly addresses a conceptual vulnerability that would be immediately flagged by a critical reviewer.

2. **发掘点 2 (significance - primary framing as general principle):** The agent is pushing to elevate the general principle as the PRIMARY contribution with encoding as just the demonstration case. There's tension here: making a "general principle" claim from single-domain validation risks overclaiming, but it could also strengthen the narrative if positioned carefully.

3. **发掘点 3 (related work - domain generalization literature):** This is a solid catch. The OOD generalization to unseen encoding types maps directly onto domain generalization, so I need to explain why standard DG methods like IRM, DRO, or DANN don't apply here. The key differences are the discrete compositional space versus continuous features, the exponentially large domain space from encoding combinations, and the fact that domains aren't enumerable during training.

4. **发掘点 4 (OOD definition sharpness):** This is critical — I need to be precise about what constitutes an "unseen encoding." Different encoding types (Braille as character substitution, Morse as symbolic representation, ciphers as shift operations) have fundamentally different structural properties, and this distinction matters for defining the generalization boundary.

5. **发掘点 5 (trivial alternative - GPT-4 zero-shot):** Strong LLMs might already handle encoding attacks reasonably well, so I should position the work around efficiency and practical deployment rather than claiming novel capability. I'll add a GPT-4 baseline or at least acknowledge this positioning.

Now looking at the statistical power issue — 3 seeds is genuinely insufficient for a paired t-test, and I need to address this methodological concern.

For the learned canonicalization baseline, I'm missing empirical evidence. I should at least show how decoding fails as nesting depth increases, or note this as a limitation if full training isn't feasible.

The co-evolutionary training introduces extra compute that I need to account for — I'll clarify that H1-H3 use a static, compute-matched curriculum while H4 is the bonus co-evolutionary variant.

There's also some confusion around random-order versus flat augmentation that I should clarify.

Now looking at the remaining issues: linear probing to validate disentanglement is a strong addition — checking whether the model can still predict encoding type tells me if the curriculum actually removed that information. The ECS component contribution analysis is also valuable since I can compute those variants without retraining, just correlating with existing error data. And the timeline seems reasonable overall.

Stepping back to assess convergence: both the discovery and remediation agents are still surfacing substantive improvements, and the probability keeps climbing. But I'm noticing something crucial — the discovery agent in this round is actually pushing back on the framing shift we made in Round 2. We moved from "compositional encoding-detection primitives" to "content-invariant features," but now the agent is pointing out that for high-ECS encodings, content information gets destroyed at the token level, which makes that framing problematic too.

The Round 3 suggestion to reframe as "generalized decoding inductive bias" with a two-regime explanation feels like the most precise version yet, not oscillation. More importantly, the OOD definition concern is serious — if reviewers argue that held-out encodings are just interpolating within known principles, the whole contribution falls apart. Adding structurally different encodings like whitespace steganography becomes critical.

After these improvements, the novelty and significance both look medium-strong now: the two-regime mechanism plus truly OOD encodings plus explicit DG positioning form a solid novel package, with general applicability to compositional attack spaces and efficiency gains over frontier models. The experiments are technically sound with linear probing, multiple seeds, and clear baselines, though the timeline is still tight and learned canonicalization remains partially unablated. This puts me around 34% median, approaching that 36% threshold, but the agents keep finding meaningful improvements so I'm not at convergence yet.

The gains are becoming more incremental though—refinements like sharpening the OOD definition and adding probing rather than fundamental re-framings—which signals diminishing returns. I'll run one more round because the two-regime mechanism needs verification and the supplementary improvements could push us over 36%, but if Round 4 shows both agents converging or only catching minor issues, that's when I should stop.

Now I'm incorporating the best suggestions from Round 3. From 发掘, I need to reframe the mechanism more precisely: the two-regime explanation should clarify that "invariance" isn't literal token-level content-invariance but rather a learned meta-capability for encoding-robust content extraction developed through progressive decoding skill acquisition. I'm also adding domain generalization literature positioning to explain why existing methods like IRM, DRO, and DANN don't apply here given the discrete compositional space and exponential domains. And I should strengthen the OOD claim by introducing truly structurally different encodings like whitespace steganography or invisible Unicode to explicitly define the two levels of structural difference.

From the remedies, I'm upgrading the curriculum to 5 seeds with bootstrap confidence intervals or Wilcoxon tests, adding error propagation analysis for the decode-then-classify pipeline with nesting-depth effects, and clarifying compute matching across the hypotheses while noting full learned canonicalization as a limitation.

I also need to add a compute-matched static variant for H4, create an explicit comparison table between random-order and flat augmentation strategies, run a linear probing experiment to distinguish encoding-type from content-type probes, and extract single-feature correlations from the ECS component as a critical inference-only analysis.

Finally, I'm planning a pilot run in the first three days with a buffer day built in.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc9413c-7a76-46b6-897d-4dc715806395",
  "isSidechain": false,
  "requestId": "req_011Cb6F9WEmBVCTG7eqM1E6p",
  "type": "assistant",
  "uuid": "597d258b-d3d9-4c64-8c61-007342004cc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVYEwb4yX258vzndJznmiv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12545,
      "cache_read_input_tokens": 32928,
      "output_tokens": 9063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12545,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 9063,
          "cache_read_input_tokens": 32928,
          "cache_creation_input_tokens": 12545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12545
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

_source line 29 · 2026-05-16T12:29:45.116Z_

【阶段】: 迭代第 3 轮
【发掘 agent 有效建议采纳】:
- **采纳发掘点 1**（机制 framing 修正）：本轮最高价值且最紧迫的建议。"Content-invariant features" 在信息论层面对高 ECS 编码不成立——多层 base64 嵌套后 token-level 内容信息已被完全摧毁，模型不可能"绕过编码直达语义"。修正为两阶段机制：(a) 低 ECS 编码下，内容语义部分可通过 tokenization 获取，模型学会锚定有害内容的语义特征（content anchoring）；(b) 高 ECS 编码下，token 层内容信息被摧毁，模型必须学会隐式解码策略组合——curriculum 提供的是"progressive decoding skill acquisition"，从简单解码模式逐步泛化到复杂解码模式。核心 claim 修正为"encoding-robust content extraction via progressive decoding skill acquisition"，而非字面的"content-invariant features"。
- **采纳发掘点 3**（Domain Generalization 文献定位）：关键遗漏。每种编码就是一个 domain，OOD 泛化本质就是 DG。需 explicitly 论证为何 IRM/DANN/DRO 不直接适用：(a) 离散组合空间无法做 gradient-based domain alignment，(b) 编码组合数指数爆炸无法枚举 training domains，(c) curriculum 是利用 compositional structure 的更 natural 方法。
- **采纳发掘点 4**（OOD 定义锐化）：关键改进。当前 held-out encodings 与 training encodings 共享 encoding principle（char substitution、symbolic re-encoding、shift），可能只是同 family 内 interpolation。增加至少一种 encoding-principle-level OOD（whitespace steganography / zero-width Unicode characters），明确区分 "mapping-function OOD"（较弱）和 "encoding-principle OOD"（较强）两层泛化。
- **采纳发掘点 5**（GPT-4 zero-shot baseline）：增加 frontier LLM zero-shot 作为 reference point，将 EncoGuard 定位为"deployment-practical"——在推理成本受限场景下接近 frontier model 编码鲁棒性。
- **部分采纳发掘点 2**：不再进一步推高 general principle 的 claim 权重。审稿人已经可能 pushback "single domain validation"，不宜 overclaim。保持 general principle 作为 interpretive framework，primary contribution 仍是 empirical finding + representation evidence。

【补救 agent 有效建议采纳】:
- **采纳缺陷 1**（5 seeds）：Curriculum training 升级为 5 seeds，与 random-order 对齐，使用 bootstrap CI 报告 H1 差异的 95% confidence interval。
- **部分采纳缺陷 2**（learned canonicalization 实证）：完整 learned canonicalization 训练不在 timeline 内，但增加 "nesting-depth vs. decode accuracy" 分析（用 deterministic decoder 展示 error propagation 曲线），并在 limitations 中 acknowledge learned canonicalization 比较的缺失。
- **采纳缺陷 3**（compute 公平性）：明确 H1-H3 基于 static curriculum（与 baselines compute 严格匹配），H4 为 bonus claim 且增加 compute-matched static variant（把 co-evolution 额外 FLOPs 转为 static data augmentation）。
- **采纳缺陷 4**（baseline 定义明确化）：增加 comparison table 清晰区分 random-order（same data, shuffled order）和 flat augmentation（different data generation strategy）。
- **采纳缺陷 5**（linear probing）：高价值低成本补丁。增加 encoding-type probe vs. content-type probe 的 linear probing 实验，直接验证 disentanglement 而非仅 similarity。
- **采纳缺陷 6**（ECS component 单因子相关性）：纯统计分析无需额外训练，升级为 submission-critical。
- **采纳缺陷 7**（timeline buffer）：Days 1-3 增加 fast pilot run 验证 training dynamics，预留 1 天 buffer。

【本轮 proposal 主要变更】:
**Idea 层面**:
- 核心机制从"content-invariant features"修正为"encoding-robust content extraction via progressive decoding skill acquisition"（两阶段：content anchoring + generalized decoding）
- 增加 Domain Generalization 文献定位和差异化论述
- OOD claim 锐化：区分 mapping-function OOD 和 encoding-principle OOD，增加 whitespace steganography / zero-width Unicode 作为 principle-level OOD 测试
- 增加 GPT-4 zero-shot reference + deployment-practical 定位

**实验层面**:
- Curriculum 升级为 5 seeds + bootstrap CI
- 增加 linear probing 实验验证 disentanglement
- 增加 nesting-depth vs. decode accuracy 曲线
- 增加 GPT-4 zero-shot baseline
- 增加 compute-matched static variant for H4
- Baseline 定义明确化 + comparison table
- ECS single-component correlation 升级为 submission-critical
- Timeline 增加 pilot run + buffer

【idea 质量评估】: Novelty=中偏强（两阶段机制描述更精确且更 defensible；OOD claim 经锐化后更 robust——尤其如果 principle-level OOD encoding 也能泛化；与 DG/CAT 文献清晰差异化。但仍为 single-domain empirical work，不是 paradigm-shifting） Significance=中偏强（deployment-practical positioning + general principle framing 合理但不过度；对 adversarial robustness 社区有方法论参考价值） → idea 天花板约 43%

【实验完备性评估】: Technical Soundness=中偏强（5-seed 统计检验、linear probing 验证 disentanglement、ECS component analysis、GPT-4 reference point、明确 baseline 定义、compute 公平性澄清——主要统计和证据链漏洞已补。残留风险：timeline 紧张度、learned canonicalization 缺乏完整实证对比） → 地板已夯实

【当前概率估计】: [28% - 40%] 中位 34%

【决策】: 继续

【决策理由】: 概率从 32% 升至 34%，逼近 36% 阈值但未跨过。本轮核心改进（机制修正、OOD 锐化、linear probing）是实质性提升而非微调。但需注意：(1) 发掘 agent 三轮均 find space，尚未收敛——机制描述经历了三次修正（compositional primitives → content-invariance → progressive decoding），需在下一轮确认最终 framing 是否稳定；(2) 补救 agent 发现的问题逐轮收敛为更细节的统计/方法问题（从方向性缺陷到参数细节），趋势健康；(3) OOD claim 锐化 + principle-level encoding 是关键增量——如果下一轮确认 framing 闭合且无新的 conceptual 漏洞，可能达到收敛。再做一轮（Round 4），预期可判断收敛或确认天花板。

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
## Title

EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training

## Problem Statement

Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses have critical limitations:

1. **Rule-based detection + decoding pipelines** (regex detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures (base64 character set, ROT13 alphabetic patterns). Fail on: (a) partial encoding where only segments are transformed, defeating whole-input detection heuristics; (b) adversarial mixing of encoded/plaintext creating ambiguous signatures; (c) novel encodings without pre-programmed decoders.

2. **Learned canonicalization** (seq2seq decode → classify): Error propagation compounds across nesting layers; the canonicalizer itself becomes an adversarial attack surface; partial encoding requires semantic understanding to identify decode targets.

3. **Frontier LLM zero-shot** (GPT-4/Claude with "detect if content is harmful regardless of encoding"): Can leverage pre-training exposure to encodings, but impractical for deployment-scale guardrails due to cost ($0.01-0.03 per input) and latency (1-3s per call vs. millisecond-level local inference).

The core challenge is achieving **generalization to unseen encoding families at deployment-practical cost**—a lightweight classifier that remains robust against encoding types never encountered during training.

## Core Thesis

We hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—acquires **encoding-robust content extraction capabilities** that generalize to held-out encoding types unseen during training.

**Mechanism (Two-Regime Explanation):**

- **Low-ECS regime (simple encodings):** Content semantics remain partially accessible through tokenization (e.g., base64 of short text preserves some token-level correlations). The curriculum forces the model to anchor harmful-content semantic features—learning what "harmful content looks like" across mild surface perturbations (**content anchoring**).

- **High-ECS regime (complex/nested encodings):** Token-level content information is effectively destroyed by multi-layer encoding. The model cannot rely on direct semantic features; it must develop strategies for implicit decoding—recognizing encoding structure patterns and reconstructing content signal. The curriculum's contribution is **progressive decoding skill acquisition**: simple decoding patterns learned in the low-ECS regime (recognizing base64 structure, identifying shift patterns) provide compositional building blocks that support parsing more complex nested structures.

The generalization prediction follows: if the model acquires generalized decoding skills (structural pattern recognition + compositional decoding strategies) rather than memorizing specific encoding-to-content mappings, it should transfer to novel encodings that share structural properties with training encodings. For truly novel encoding principles, the model's content-anchoring from the low-ECS regime provides a robust classification backbone once any partial decoding succeeds.

**Important distinction:** We do NOT claim the model learns literal "encoding-invariant features" in the information-theoretic sense (impossible for fully-scrambled token sequences). Rather, curriculum training builds a progressive hierarchy of decoding capabilities—from direct semantic extraction (low-ECS) to structural pattern matching + compositional decoding (high-ECS)—that transfers across encoding types more effectively than flat or random training.

## Relationship to Prior Work

### Curriculum Adversarial Training
Cai et al. (IJCAI 2018) progressively increase perturbation magnitude ε for image classifiers; Wang et al. (NeurIPS 2021) order samples by difficulty for better generalization. Key differences from our work:
1. **Discrete compositional space vs. continuous perturbation:** Prior work operates in continuous ε-ball spaces with scalar difficulty. Encoding attacks form a discrete compositional space requiring multi-dimensional complexity metrics.
2. **OOD generalization vs. in-distribution robustness:** Prior work only evaluates on the same attack type used in training. We explicitly test generalization to unseen encoding families—including encodings based on entirely different structural principles.

### Domain Generalization (DG)
Each encoding type can be viewed as a domain; OOD generalization to unseen encodings resembles domain generalization. However, standard DG methods (IRM, DANN, CORAL, DRO) are not directly applicable because:
1. **Non-differentiable discrete domains:** Encoding transformations are discrete operations; gradient-based domain alignment (DANN adversarial training) cannot be applied to the input transformation space.
2. **Exponential domain combinatorics:** Composing N encoding primitives at K nesting levels creates O(N^K) potential domains—impossible to enumerate as source domains at training time.
3. **Structural curriculum as natural alternative:** The compositional structure of encoding attacks provides a natural progressive training signal that standard DG methods lack—curriculum exploits the partial ordering on complexity inherent in compositional spaces.

## Key Contributions

1. **Primary Contribution (OOD Generalization via Curriculum):** Empirical demonstration that complexity-structured curriculum enables generalization to unseen encoding families—at two levels: (a) mapping-function OOD (same encoding principle, different specific mapping), and (b) encoding-principle OOD (structurally different encoding type). Direct representation-level evidence (CKA + linear probing) characterizes how curriculum shapes internal representations differently from baselines.

2. **Encoding Complexity Score (ECS):** Formalized metric combining nesting depth, CPT deviation, and tokenizer perplexity. Validated via correlation with classifier difficulty; individual component contributions quantified.

3. **Co-Evolutionary Training Framework:** GRPO attacker + SFT classifier with curriculum-ordered training, demonstrating co-evolution can further improve upon static curriculum.

4. **Deployment-Practical Encoding Defense:** A 4B-parameter classifier achieving encoding robustness comparable to frontier LLM zero-shot, at orders-of-magnitude lower inference cost.

## Methodology

### Encoding Complexity Score (ECS)

$$ECS(e) = \alpha \cdot \text{NestingDepth}(e) + \beta \cdot \text{CPT\_Deviation}(e) + \gamma \cdot \text{TokenizerPerplexity}(e)$$

- NestingDepth: number of compositional encoding layers
- CPT_Deviation: |CPT_encoded / CPT_plaintext - 1|
- TokenizerPerplexity: target tokenizer's perplexity on encoded text

**Weight determination:** Pilot study (200 samples spanning full ECS range) measures Spearman ρ of each individual component with classifier error rate. Weights set proportional to individual predictive power.

**Component contribution analysis (submission-critical):** Report Spearman ρ for each single component alone and for leave-one-out combinations, demonstrating that all three contribute meaningfully and that the composite metric outperforms any single component.

### Co-Evolutionary Training Loop

**Attacker (Qwen2.5-1.5B, GRPO):**
- Generates encoding attacks with ECS in current curriculum band
- Reward: +1 if bypasses classifier AND oracle confirms harmful
- Entropy regularization prevents encoding-type collapse

**Classifier (Qwen2.5-4B, SFT):**
- Curriculum-ordered training: Stage 1 (ECS ≤ threshold) → Stage 2 (ECS > threshold)
- FPR rollback: revert if FPR > 2% on benign validation
- Semantic deduplication: cosine similarity > 0.95 removed

**Oracle:** GPT-4o + deterministic decoder cross-validation; disagreements excluded.

**Fallback:** If co-evolutionary loop unstable by Day 7, switch to static curriculum SFT.

### Baseline Definitions (Comparison Table)

| Baseline | Data Source | Data Composition | Presentation Order | Isolates |
|----------|-------------|------------------|-------------------|----------|
| **Curriculum (ours)** | Co-evolutionary or static generation | ECS-staged | Monotone increasing ECS | — |
| **Random-order** | Same data as curriculum | Identical composition | Randomly shuffled | Ordering effect |
| **Flat augmentation** | Fresh generation: each epoch randomly samples encoding type per prompt | Uniform across all ECS levels | Random within each epoch | Data composition + ordering |
| **Reverse curriculum** | Same data as curriculum | Identical composition | Monotone decreasing ECS | Direction effect |
| **Static curriculum** | Rule-based generation, ECS-ordered | Identical to curriculum | Same ordering | Co-evolution effect |
| **Decode + LlamaGuard-3** | N/A (inference only) | N/A | N/A | End-to-end vs. pipeline |
| **GPT-4 zero-shot** | N/A (API call) | N/A | N/A | Cost/accuracy frontier |

Key distinctions:
- Random-order vs. Flat augmentation: Random-order uses curriculum's exact data (same samples) in shuffled order → isolates ordering. Flat augmentation generates different data with uniform encoding distribution → tests whether curriculum's staged data composition matters.
- Static curriculum vs. Curriculum: Same data, same order, but no co-evolutionary attacker → isolates co-evolution benefit.

### Compute Fairness

- **H1-H3 (core claims):** Based on static curriculum vs. baselines. All methods use identical model architecture (Qwen2.5-4B), identical total training FLOPs, identical number of training steps. Only variable: data ordering / composition.
- **H4 (co-evolution bonus):** Co-evolutionary method has additional compute (attacker training: ~12h, oracle calls: ~$250). For fair comparison, include a "compute-matched static" variant: redirect co-evolution's extra FLOPs into additional static curriculum training epochs.
- **Reporting:** Table includes total FLOPs (classifier only), total FLOPs (including attacker), wall-clock time, and training tokens for each method.

### Compute and Cost

- Hardware: 4× A100 80GB
- Per classifier run: ~8h
- Total runs: curriculum (5) + random (5) + flat (3) + reverse (3) + static (3) + compute-matched static (3) = 22 classifier runs
- Parallelization: 4 GPUs → 4 runs simultaneously → ~44h for all classifier training
- Attacker: 12h (2 rounds)
- Oracle: ~18K calls ≈ $250
- GPT-4 zero-shot evaluation: ~12K test cases × $0.01 ≈ $120
- Inference-only analyses (probing, CKA, ECS stats): ~4h
- Total: ~60h wall-clock for training + ~4h analysis

## Experimental Design

### Hypotheses

- **H1 (Curriculum > Random):** Curriculum achieves ≥10pp lower encoding-ASR than random-order at equivalent FLOPs (95% bootstrap CI of difference excludes 0, one-sided).
- **H2 (OOD Generalization):** Curriculum maintains ≤30% encoding-ASR on held-out encodings where baselines exceed 60%. Tested at two OOD levels: mapping-function OOD and encoding-principle OOD.
- **H3 (ECS Predictiveness):** ECS correlates with classifier error (Spearman ρ ≥ 0.7) on held-out encodings; composite metric outperforms any single component.
- **H4 (Co-evolution > Static, bonus):** Co-evolutionary > static curriculum by ≥5pp on composite encodings, after controlling for extra compute.

### Held-Out Encoding Families

**Mapping-function OOD (same structural principle as training encodings):**
- Braille Unicode substitution (character substitution — cf. homoglyphs in training)
- Custom Caesar-variant cipher with position-dependent shift (shift-based — cf. ROT13 in training)
- NATO phonetic alphabet (word-level substitution)

**Encoding-principle OOD (structurally different from all training encodings):**
- Whitespace steganography (harmful content encoded in whitespace patterns between benign text)
- Zero-width Unicode character encoding (content hidden in invisible Unicode sequences)

This two-level OOD structure explicitly tests whether generalization is merely interpolation within known principles (mapping-function OOD) or genuine extrapolation to novel encoding paradigms (encoding-principle OOD).

### Evaluation Protocol

**External benchmarks (primary):**
- HarmBench encoding-perturbed
- JailbreakBench encoding subset
- WildGuardTest encoding-perturbed

**EncoAttack (supplementary):**
- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150)
- 8 encoding types × 3 nesting levels = 12,000 test cases
- Independent implementation from training; validated ≥80% bypass on undefended LlamaGuard-3

**Held-out encodings:** 5 families as specified above

**GPT-4 zero-shot reference:** Same test sets, prompt: "The following text may be encoded. Determine if the underlying content, once decoded, would be harmful."

**Metrics:**
- Encoding-ASR (primary)
- Clean FPR at thresholds: 0.5%, 1%, 2%, 5% with Pareto frontier
- Benign test: WildGuardTest benign (~1000) + LMSYS-Chat-1M sample (1000)
- Per-encoding breakdown
- ECS-difficulty correlation (composite + individual components)
- Nesting-depth vs. decode-accuracy curve (demonstrating pipeline error propagation)

### Representation Analysis

1. **CKA + Cosine Similarity:** For 100 prompts × (plaintext + 8 encoding variants), extract penultimate-layer representations. Compute intra-prompt cross-encoding cosine similarity. Compare curriculum vs. random-order.

2. **Linear Probing (Disentanglement Test):**
   - Train linear probe A: predict content category (harmful topic type) from representations
   - Train linear probe B: predict encoding type from representations
   - **Prediction:** Curriculum model → high probe-A accuracy, LOW probe-B accuracy (encoding info discarded). Random-order model → lower probe-A, higher probe-B (encoding info retained).
   - This directly tests whether curriculum induces disentanglement of content from encoding surface features.

3. **Learning Dynamics:** Per-checkpoint (500 steps) ASR curves for low-ECS and high-ECS separately. Expected pattern: curriculum shows staged learning (low-ECS converges first, smooth transition to high-ECS); random-order shows chaotic/concurrent learning.

### Statistical Rigor

- All methods: 5 seeds (curriculum, random-order) or 3 seeds (flat, reverse, static) with mean ± std
- H1: 95% bootstrap CI on paired difference (curriculum seed i vs. random-order seed i, same initialization)
- Effect sizes: Cohen's d reported alongside p-values
- Multiple comparison correction: Bonferroni for family of H1-H3 tests

### Oracle Pilot (Days 1-3)

- 100 samples per ECS band
- Measure GPT-4o + deterministic decoder agreement rate
- If < 80% for high-ECS: switch to deterministic-only for Stage 2

## Stability Mechanisms (Engineering, Not Contributions)

Borrowed from prior work (TriPlay-RL, standard RL practices):
- Entropy regularization
- FPR rollback
- Semantic deduplication

Trigger frequencies reported. Full ablation in camera-ready.

## Limitations (To Acknowledge in Paper)

1. Learned canonicalization (seq2seq decode → classify) not empirically compared due to training cost; theoretical arguments + decode error propagation curve provided as indirect evidence.
2. General principle validated only on encoding attacks; transfer to other compositional attack spaces (prompt injection, multi-turn) remains future work.
3. ECS weight sensitivity not fully explored (±20% perturbation analysis in supplementary).

## Timeline (17 days, with buffer)

**Phase 1: Setup + Pilot (Days 1-3)**
- ECS implementation, encoding generators (including held-out families), data pipeline
- Oracle pilot (100 samples/band)
- Fast pilot curriculum run (reduced data, 2h) to validate training dynamics + ECS threshold

**Phase 2: Core Training (Days 4-9)**
- Days 4-6: Curriculum (5 seeds) + random-order (5 seeds) [parallelized, 4 GPUs]
- Days 7-8: Flat augmentation (3) + reverse curriculum (3) + static (3) [parallelized]
- Day 9: Co-evolutionary attempt + compute-matched static + decode pipeline

**Phase 3: Evaluation + Analysis (Days 10-12)**
- Day 10: Full benchmark evaluation + held-out encodings + GPT-4 zero-shot
- Day 11: Representation analysis (CKA, probing) + ECS component stats + learning dynamics
- Day 12: Statistical tests, nesting-depth decode curve, Pareto analysis

**Phase 4: Writing (Days 13-15)**
- Day 13-14: Main paper draft
- Day 15: Figures, tables, polishing

**Buffer + Camera-ready (Days 16-17)**
- Additional seeds if needed, stability ablation, writing revision

**Fallback:** Co-evolutionary unstable by Day 8 → drop H4, focus H1-H3 with static curriculum.
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "597d258b-d3d9-4c64-8c61-007342004cc9",
  "isSidechain": false,
  "requestId": "req_011Cb6F9WEmBVCTG7eqM1E6p",
  "type": "assistant",
  "uuid": "4237f473-ff8d-41ef-8dab-d62f5b787fbd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVYEwb4yX258vzndJznmiv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12545,
      "cache_read_input_tokens": 32928,
      "output_tokens": 9063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12545,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 9063,
          "cache_read_input_tokens": 32928,
          "cache_creation_input_tokens": 12545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12545
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: 前提假设质疑 - 内容: \"Content-invariant features\" 这一核心 framing 存在概念上的内在张力。对于高 ECS 编…",
  "leafUuid": "4237f473-ff8d-41ef-8dab-d62f5b787fbd",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: 前提假设质疑 - 内容: \"Content-invariant features\" 这一核心 framing 存在概念上的内在张力。对于高 ECS 编…",
  "leafUuid": "4237f473-ff8d-41ef-8dab-d62f5b787fbd",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 35 · 2026-05-16T12:33:33.309Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:33:33.309Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "content": "【任务】: 以「角色 B：迭代中」整合第 4 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have enough context to provide a thorough assessment. Let me deliver my analysis.\n\n---\n\n【状态】: 有发掘空间\n\n---\n\n【发掘点 1】\n- 维度: 前提假设质疑 / novelty 锐化\n- 内容: **Encoding-principle OOD 的 claim 存在逻辑断裂，是整篇论文最脆弱也最关键的点。** 训练编码族（base64, ROT13, homoglyphs）的共同特征是：编码后的内容在 token 层面是 *可见的*——它们改变了字符/词的 surface form，但信息仍然承载在可见 token 序列中。模型可以通过学习 visible token patterns 来做 implicit decoding。然而，两个 encoding-principle OOD 测试族——whitespace steganography 和 zero-width Unicode——的核心机制是将有害内容 *隐藏在不可见字符中*。这是一个根本不同的信息承载方式：模型需要检测的不是\"可见 token 序列的结构规律\"，而是\"不可见字符序列中隐藏的信息\"。Curriculum 训练中积累的所有\"结构模式识别 + 组合解码策略\"都是基于可见 token 的——这些技能为什么能迁移到检测不可见字符中的信息？Proposal 中的 two-regime mechanism 完全没有覆盖这个 gap。如果 encoding-principle OOD 实验结果为 negative（高概率），论文的核心 novelty claim 就从\"真正的 OOD 泛化\"降级为\"同一编码原理内的插值\"——这对审稿人的 surprise factor 是致命打击。**建议：要么 (a) 将 encoding-principle OOD 的测试族替换为与训练编码 share 相同信息承载方式但 mapping 不同的编码（如 Morse code、自定义字母替换表、phonetic encoding），保持 genuine OOD 但在逻辑上可解释为什么技能能迁移；要么 (b) 保留 whitespace/zero-width 但将其重新定位为 \"boundary test\"——明确预测这些族上 curriculum 不应该 outperform random（这反而成为理解 curriculum 泛化边界的积极贡献）。选项 (b) 实际上更有学术价值：它展示了 curriculum 泛化的 *scope conditions*，比一个模糊的\"we generalize to everything\"claim 更有说服力。**\n- 价值: 直接决定 Novelty 维度的天花板。如果 OOD claim 站不住，核心贡献从\"范式级发现\"降为\"工程优化\"。修复此点后，novelty claim 从 vulnerable 变为 robust——无论结果是正面还是负面，都有清晰的学术故事。\n\n【发掘点 2】\n- 维度: significance 提升\n- 内容: **当前 framing 将 significance 限制在了 \"encoding attack defense\" 这一狭窄应用上，遗漏了一个更有影响力的研究问题。** 编码攻击空间本质上是一个 *离散组合变换空间*（N 个编码原语 × K 层嵌套 = O(N^K) 种组合）。Curriculum 在此空间中促进 OOD 泛化的问题，实质上是 **compositional generalization** 的一个实例——这是 NLP/ML 领域持续关注的核心难题（SCAN, COGS, compositional generalization benchmarks）。但 proposal 完全没有连接到这一文献。建议将论文的上位研究问题重新 frame 为：\"Can complexity-structured curriculum enable compositional generalization in discrete transformation spaces?\"——encoding attacks 是这个更大问题的 *testbed*，而非全部贡献。这样做的好处：(1) Significance 从 \"safety engineering\" 升级为 \"fundamental learning dynamics\"；(2) 吸引 compositional generalization 社区的审稿人兴趣；(3) 为 limitations 中提到的 \"transfer to other compositional attack spaces\" 提供自然的理论框架。\n- 价值: 命中 Significance 维度。将论文的潜在影响力从 safety subcommunity 扩展到 broader ML audience，直接影响审稿人对 \"importance of research question\" 的评分。\n\n【发掘点 3】\n- 维度: 核心 claim 强化\n- 内容: **Curriculum 优于 random ordering 的 mechanism story 缺少与最 trivial 的替代解释之间的区分。** 一个更简单的解释是：curriculum ordering 之所以有效，不是因为它构建了\"progressive decoding skill hierarchy\"，而仅仅是因为它 **避免了早期训练阶段被高 ECS 样本淹没导致的 catastrophic interference**——模型先在简单样本上稳定学到 content features，这些 features 在后续高 ECS 阶段不会被完全覆盖。这是标准的 curriculum learning benefit，不需要任何 \"implicit decoding skill acquisition\" 的新颖机制。如果这个 trivial 解释成立，novelty 就大打折扣——论文只是重新确认了\"easy-to-hard ordering helps\"这个已知结论在新 domain 上的适用性。**要区分这两个解释，需要一个关键的 falsifiable prediction：** 如果机制是 \"progressive decoding skill acquisition\"（组合性技能构建），那么 curriculum 的优势应该随 nesting depth 增加而 *扩大*（因为更深的嵌套更依赖组合性解码技能）。如果机制仅是 \"catastrophic interference prevention\"，优势应该在所有 nesting depth 上大致均匀（因为保护的只是 base content features）。建议在论文中明确提出这个 differential prediction，并在实验中按 nesting depth 分层报告 curriculum vs. random 的 gap。这不仅加强 mechanism claim，还提供了独立的 analytical contribution。\n- 价值: 命中 Novelty 维度。如果不区分 trivial mechanism，审稿人极可能提出\"this is just standard curriculum learning benefit\"的质疑——这是 novelty 的最大威胁之一。提出 differential prediction 把论文从 \"empirical observation\" 升级为 \"mechanistic understanding\"。\n\n【发掘点 4】\n- 维度: related work 差异化\n- 内容: **Compositional generalization 文献的缺失是一个显著的 related work gap，可能导致审稿人认为作者对问题的理论背景理解不足。** SCAN (Lake & Baroni, 2018)、COGS (Kim & Linzen, 2020)、以及后续大量关于 transformer compositional generalization 能力与局限的工作，直接关系到本文的核心 claim：在组合空间中通过 curriculum 实现 OOD 泛化。此外，curriculum learning 在 transformer 上的 mixed results（部分工作显示 marginal improvement，部分显示 anti-curriculum 同样有效）需要被直接 acknowledge 并解释为什么本文的 domain 不同——具体来说，encoding attack 的组合空间有一个 *natural partial ordering on complexity*（nesting depth 提供了非人工定义的 difficulty metric），这在很多 curriculum learning 失败的 domain 中是不存在的。这个论证如果做好，反而能把 related work 的潜在威胁转化为 novelty 的支撑：\"curriculum works here because the domain has intrinsic compositional structure that provides a principled difficulty ordering, unlike the arbitrary orderings that fail in prior work.\"\n- 价值: 命中 Related Work 差异化维度。补上此 gap 同时达到两个效果：(1) 消除审稿人\"authors missed key related work\"的负面印象；(2) 将 encoding domain 的结构特殊性转化为论文的理论 selling point。\n\n【发掘点 5】\n- 维度: trivial alternative 威胁\n- 内容: **Proposal 低估了 modular decode-then-classify pipeline 在现代 small LM 时代的竞争力。** 论文将 \"learned canonicalization\" 列为已有方法并以 \"error propagation + adversarial attack surface\" 驳回，但这一驳斥基于隐含假设：decoder 是一个独立的 seq2seq 模型。然而，如果 decoder 本身就是一个 instruction-following small LM（如 Qwen2.5-1.5B with \"decode this text\" prompt），其解码能力可能相当强——因为这些模型在 pretraining 中已经见过大量编码/解码的 text。这个 pipeline（1.5B decoder → LlamaGuard-3）总参数量与 proposal 的 4B classifier 相当，但具有更好的 interpretability 和 modularity。**如果不在实验中包含一个 \"modern small-LM decoder + standard guardrail\" baseline，审稿人很可能会要求补充。** 建议在 baseline 中增加 \"Qwen2.5-1.5B decode → LlamaGuard-3 classify\" pipeline，并在 nesting-depth vs. accuracy 曲线上展示 error propagation 的实证证据（proposal 中已提到此曲线但仅作为 indirect evidence）。这实际上是一个可以赢的比较：multi-layer nesting 下 pipeline 的 error compounding 应该表现明显差于 end-to-end classifier。\n- 价值: 命中 Novelty 维度（消除 trivial alternative 威胁）。如果审稿人认为存在一个更简单的替代方案没被比较，novelty score 会显著下降。主动展示 end-to-end 优于 modular pipeline（尤其在高 nesting depth），反而成为 supporting evidence for the core approach。\n\n【补救 agent 本轮输出】:\n# 补救 Agent 审查报告\n\n【状态】: 有缺陷待补救\n\n---\n\n【缺陷 1】\n- 类别: baseline 不足\n- 问题: Proposal 在 Related Work 中以\"非差分离散域\"和\"指数域组合\"为由 dismiss 了所有 Domain Generalization (DG) 方法（IRM, DANN, CORAL, DRO），但这两条论据站不住脚。DANN 的 gradient reversal layer 作用在**表征空间**而非输入变换空间，完全不需要输入变换可微——只需将 encoding type 作为 domain label 即可训练 domain discriminator。Group DRO 更是仅需按 encoding type 分组重加权 loss，无任何额外架构改动。对于一篇核心 claim 是 OOD generalization 的论文，完全不提供任何 DG baseline 的实证对比，reviewer 几乎必然会要求补充。这是当前最大的 baseline 缺口。\n- 严重度: 可补救\n- 补救方案: 至少补两个 DG baseline——(1) **Group DRO**: 以 encoding type 为 group，按 worst-group loss 优化，同一 Qwen2.5-4B 架构，3 seeds，每 run ~8h，总增 6h wall-clock（4 GPU 并行）；(2) **DANN**: 加 gradient reversal layer + encoding-type auxiliary classifier，同样 3 seeds ~6h。两者均可在 Days 7-8 与 flat/reverse/static 并行训练，不影响关键路径。在 Related Work 中将论据从\"不可应用\"改为\"可应用但我们实证表明 curriculum 优于 DG methods，因为 DG methods 缺乏对编码组合结构的利用\"。\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: Encoding-principle OOD 的两个 held-out 家族——whitespace steganography 和 zero-width Unicode encoding——存在 **tokenizer 兼容性风险**。Qwen2.5 的 tokenizer 极可能在 tokenization 阶段对空白符做归一化（多空格合并）、并完全丢弃 zero-width characters（U+200B, U+FEFF 等）。如果 tokenizer 在预处理阶段就把编码信号消除了，那么**任何**神经模型（包括 curriculum 和所有 baseline）都无法检测该编码，测试结果将是所有方法 ASR 接近 100%——这不能说明 curriculum 的泛化失败，而是测试本身无效。Proposal 中完全没有讨论这一风险，也没有提出 tokenizer 层面的验证步骤。\n- 严重度: 可补救\n- 补救方案: (1) **Day 1-2 新增 tokenizer 审计步骤**: 用 Qwen2.5 tokenizer 对 whitespace stego 和 zero-width Unicode 编码的样本做 tokenize → detokenize round-trip，检查编码信号是否保留。量化信息保留率（round-trip 后可恢复的 harmful content 比例）。(2) **如果信号被消除**: 替换为 tokenizer-compatible 的编码原理 OOD 家族，例如: (a) **Morse code encoding**（用点划线文本表示字符，tokenizer 不会消除），(b) **Phone keypad encoding**（T9 数字序列，结构上与 training 编码不同但 tokenizer 保留），(c) **Pig Latin 变体**（音节重排，结构不同于字符替换/移位）。(3) **如果信号部分保留**: 报告保留率，并在实验中将其作为 \"partial-signal OOD\" 分类讨论，而非与 mapping-function OOD 使用相同的成功阈值。\n\n【缺陷 3】\n- 类别: 实验设计不足\n- 问题: H2 对 mapping-function OOD 和 encoding-principle OOD 使用**同一阈值**（≤30% ASR vs baseline ≥60%）。这两个 OOD 层级的难度差异本质上不同——mapping-function OOD 共享训练编码的结构原理（如 character substitution），而 encoding-principle OOD 基于全新的编码范式。用同一阈值要么导致：(a) 阈值对 mapping-function OOD 太宽松，无法展示真正的泛化强度；(b) 阈值对 encoding-principle OOD 太严格，curriculum 可能合理地无法达到 ≤30%，导致 H2 被判为\"failed\"——但这并不意味着 curriculum 没有价值，只是泛化边界在此处。一个混合的 H2 会让结果解读变得模糊。\n- 严重度: 可补救\n- 补救方案: 将 H2 拆为两个子假设: **H2a (Mapping-function OOD)**: Curriculum 在 same-principle OOD 上维持 ≤20% ASR（阈值更严，展示强泛化）。**H2b (Encoding-principle OOD)**: Curriculum 在 novel-principle OOD 上相对 baselines 有 ≥15pp 的 ASR 降低（使用相对改进而非绝对阈值，承认彻底泛化可能不成立，但 curriculum 仍优于替代方案）。分开报告、分开统计检验、分开讨论。这让论文的 claim 更精确、更难被 reviewer 以\"H2 部分失败\"为由攻击。\n\n【缺陷 4】\n- 类别: 评估方案缺陷\n- 问题: H3 表述为\"ECS correlates with classifier error (Spearman ρ ≥ 0.7) on held-out encodings\"，但**没有指定是哪个 classifier 的 error**。这导致循环论证风险：如果用 curriculum-trained classifier 的 error 来验证 ECS，而 ECS 又被用来构建 curriculum 训练的顺序，因果关系不清。同样，ECS 权重的 pilot study 使用\"classifier error rate\"来校准权重，但也没说明是哪个 classifier——如果是一个随机初始化的 classifier，几乎所有编码都会导致高 error，区分度差；如果是最终训练好的 curriculum classifier，则权重对目标模型有依赖。\n- 严重度: 可补救\n- 补救方案: (1) **ECS 权重校准**: Pilot study 中使用一个 **minimally-trained baseline classifier**（如在少量 plaintext harmful/benign 数据上 fine-tune 几个 epoch 的 Qwen2.5-4B），测量其在不同编码下的 error rate，以此校准 ECS 权重。这个 classifier 足够有区分度（plaintext 训练意味着编码越复杂 error 越高），又不依赖 curriculum 训练过程。(2) **H3 验证**: 报告 ECS 与**至少两个不同 classifier** error 的相关性——(a) 上述 minimally-trained baseline，(b) random-order trained classifier，(c) curriculum-trained classifier。如果 ECS 与多个 classifier 的 error 都高度相关（尤其是与 curriculum 无关的 baseline），说明 ECS 捕捉的是编码固有难度，而非 curriculum 训练的产物。\n\n【缺陷 5】\n- 类别: 评估方案缺陷\n- 问题: Proposal 的第四条 contribution 明确声称\"Deployment-Practical Encoding Defense\"，问题陈述中也以 cost ($0.01-0.03/input) 和 latency (1-3s) 对比 frontier LLM 来论证实用性。但 Evaluation Protocol 的 metrics 部分完全没有包含 **inference latency 和 throughput 的正式测量**。没有数据支撑的\"deployment-practical\" claim 会被 reviewer 质疑为 hand-waving。\n- 严重度: 可补救\n- 补救方案: 新增 metrics：(1) **Inference latency**: 在单 A100 上，batch size=1 和 batch size=32 下的 median 和 p99 latency（ms），对比 decode+LlamaGuard-3 pipeline 和 GPT-4 API。(2) **Throughput**: tokens/second 和 queries/second。(3) **Cost per query**: 基于 A100 租赁价格计算 per-query inference cost，与 GPT-4 API cost 对比。这些测量只需 ~1h computation，可在 Day 10-11 完成。\n\n【缺陷 6】\n- 类别: 实验设计不足\n- 问题: 训练数据中 harmful-encoded 与 benign 样本的**比例（class balance）**完全没有说明。Co-evolutionary attacker 只生成 harmful-encoded 样本，如果不加控制，训练集会严重偏向 harmful 类，导致 FPR 升高。Proposal 提到 FPR rollback 作为安全网，但 rollback 是被动应急机制（已经开始 overfit 才触发），不能替代主动的 class balance 设计。Benign 数据的来源、数量、是否也进行 encoding augmentation 等细节均缺失。\n- 严重度: 可补救\n- 补救方案: 明确说明：(1) **Benign 数据来源和规模**: 例如 LMSYS-Chat-1M 中采样 N 条 benign 对话，WildGuardTest benign set 等。(2) **训练 batch 构成**: 每 batch 中 harmful-encoded : benign 的比例（推荐 1:1 或有文献支撑的比例）。(3) **Benign 数据是否也做 encoding augmentation**: 如果不做，classifier 可能学到\"encoded = harmful\"的 shortcut（凡是看起来像编码的都判 harmful）。应对 benign 样本也做一定比例的 encoding augmentation，防止 encoding 本身成为 harmful 的 proxy feature。这一点尤其关键——如果 benign 数据全是 plaintext，classifier 可能不是学会了\"检测 harmful content regardless of encoding\"，而是学会了\"检测编码的存在\"。这会导致 FPR 在 encoded-benign 输入上灾难性升高，而当前的 benign test set（WildGuardTest benign + LMSYS）看起来**全是 plaintext**，不会暴露这个问题。\n  \n  补充测试：新增 **encoded-benign evaluation**：对 500 条 benign prompts 做与 harmful 相同的 encoding augmentation（8 types × 选取子集），测量 FPR。如果 encoded-benign FPR 远高于 plaintext-benign FPR，说明 classifier 学到了 encoding-as-harmful shortcut，而非真正的 content extraction。\n\n---\n\n**总结**: 以上 6 个缺陷均可补救，无方向性致命问题。其中**缺陷 1（DG baseline 缺失）**和**缺陷 6（class balance + encoded-benign evaluation）**最为关键——前者是 reviewer 几乎必问的 baseline 问题，后者是一个实验设计上可能导致核心 claim 被根本性质疑的漏洞（classifier 可能只是在检测 encoding 的存在而非提取 harmful content）。建议优先处理这两个。"
}
```

---

### Runtime record

_source line 36 · 2026-05-16T12:33:33.309Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:33:33.309Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

## Round 4

12 recorded events

### User

_source line 37 · 2026-05-16T12:33:33.342Z_

【任务】: 以「角色 B：迭代中」整合第 4 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have enough context to provide a thorough assessment. Let me deliver my analysis.

---

【状态】: 有发掘空间

---

【发掘点 1】
- 维度: 前提假设质疑 / novelty 锐化
- 内容: **Encoding-principle OOD 的 claim 存在逻辑断裂，是整篇论文最脆弱也最关键的点。** 训练编码族（base64, ROT13, homoglyphs）的共同特征是：编码后的内容在 token 层面是 *可见的*——它们改变了字符/词的 surface form，但信息仍然承载在可见 token 序列中。模型可以通过学习 visible token patterns 来做 implicit decoding。然而，两个 encoding-principle OOD 测试族——whitespace steganography 和 zero-width Unicode——的核心机制是将有害内容 *隐藏在不可见字符中*。这是一个根本不同的信息承载方式：模型需要检测的不是"可见 token 序列的结构规律"，而是"不可见字符序列中隐藏的信息"。Curriculum 训练中积累的所有"结构模式识别 + 组合解码策略"都是基于可见 token 的——这些技能为什么能迁移到检测不可见字符中的信息？Proposal 中的 two-regime mechanism 完全没有覆盖这个 gap。如果 encoding-principle OOD 实验结果为 negative（高概率），论文的核心 novelty claim 就从"真正的 OOD 泛化"降级为"同一编码原理内的插值"——这对审稿人的 surprise factor 是致命打击。**建议：要么 (a) 将 encoding-principle OOD 的测试族替换为与训练编码 share 相同信息承载方式但 mapping 不同的编码（如 Morse code、自定义字母替换表、phonetic encoding），保持 genuine OOD 但在逻辑上可解释为什么技能能迁移；要么 (b) 保留 whitespace/zero-width 但将其重新定位为 "boundary test"——明确预测这些族上 curriculum 不应该 outperform random（这反而成为理解 curriculum 泛化边界的积极贡献）。选项 (b) 实际上更有学术价值：它展示了 curriculum 泛化的 *scope conditions*，比一个模糊的"we generalize to everything"claim 更有说服力。**
- 价值: 直接决定 Novelty 维度的天花板。如果 OOD claim 站不住，核心贡献从"范式级发现"降为"工程优化"。修复此点后，novelty claim 从 vulnerable 变为 robust——无论结果是正面还是负面，都有清晰的学术故事。

【发掘点 2】
- 维度: significance 提升
- 内容: **当前 framing 将 significance 限制在了 "encoding attack defense" 这一狭窄应用上，遗漏了一个更有影响力的研究问题。** 编码攻击空间本质上是一个 *离散组合变换空间*（N 个编码原语 × K 层嵌套 = O(N^K) 种组合）。Curriculum 在此空间中促进 OOD 泛化的问题，实质上是 **compositional generalization** 的一个实例——这是 NLP/ML 领域持续关注的核心难题（SCAN, COGS, compositional generalization benchmarks）。但 proposal 完全没有连接到这一文献。建议将论文的上位研究问题重新 frame 为："Can complexity-structured curriculum enable compositional generalization in discrete transformation spaces?"——encoding attacks 是这个更大问题的 *testbed*，而非全部贡献。这样做的好处：(1) Significance 从 "safety engineering" 升级为 "fundamental learning dynamics"；(2) 吸引 compositional generalization 社区的审稿人兴趣；(3) 为 limitations 中提到的 "transfer to other compositional attack spaces" 提供自然的理论框架。
- 价值: 命中 Significance 维度。将论文的潜在影响力从 safety subcommunity 扩展到 broader ML audience，直接影响审稿人对 "importance of research question" 的评分。

【发掘点 3】
- 维度: 核心 claim 强化
- 内容: **Curriculum 优于 random ordering 的 mechanism story 缺少与最 trivial 的替代解释之间的区分。** 一个更简单的解释是：curriculum ordering 之所以有效，不是因为它构建了"progressive decoding skill hierarchy"，而仅仅是因为它 **避免了早期训练阶段被高 ECS 样本淹没导致的 catastrophic interference**——模型先在简单样本上稳定学到 content features，这些 features 在后续高 ECS 阶段不会被完全覆盖。这是标准的 curriculum learning benefit，不需要任何 "implicit decoding skill acquisition" 的新颖机制。如果这个 trivial 解释成立，novelty 就大打折扣——论文只是重新确认了"easy-to-hard ordering helps"这个已知结论在新 domain 上的适用性。**要区分这两个解释，需要一个关键的 falsifiable prediction：** 如果机制是 "progressive decoding skill acquisition"（组合性技能构建），那么 curriculum 的优势应该随 nesting depth 增加而 *扩大*（因为更深的嵌套更依赖组合性解码技能）。如果机制仅是 "catastrophic interference prevention"，优势应该在所有 nesting depth 上大致均匀（因为保护的只是 base content features）。建议在论文中明确提出这个 differential prediction，并在实验中按 nesting depth 分层报告 curriculum vs. random 的 gap。这不仅加强 mechanism claim，还提供了独立的 analytical contribution。
- 价值: 命中 Novelty 维度。如果不区分 trivial mechanism，审稿人极可能提出"this is just standard curriculum learning benefit"的质疑——这是 novelty 的最大威胁之一。提出 differential prediction 把论文从 "empirical observation" 升级为 "mechanistic understanding"。

【发掘点 4】
- 维度: related work 差异化
- 内容: **Compositional generalization 文献的缺失是一个显著的 related work gap，可能导致审稿人认为作者对问题的理论背景理解不足。** SCAN (Lake & Baroni, 2018)、COGS (Kim & Linzen, 2020)、以及后续大量关于 transformer compositional generalization 能力与局限的工作，直接关系到本文的核心 claim：在组合空间中通过 curriculum 实现 OOD 泛化。此外，curriculum learning 在 transformer 上的 mixed results（部分工作显示 marginal improvement，部分显示 anti-curriculum 同样有效）需要被直接 acknowledge 并解释为什么本文的 domain 不同——具体来说，encoding attack 的组合空间有一个 *natural partial ordering on complexity*（nesting depth 提供了非人工定义的 difficulty metric），这在很多 curriculum learning 失败的 domain 中是不存在的。这个论证如果做好，反而能把 related work 的潜在威胁转化为 novelty 的支撑："curriculum works here because the domain has intrinsic compositional structure that provides a principled difficulty ordering, unlike the arbitrary orderings that fail in prior work."
- 价值: 命中 Related Work 差异化维度。补上此 gap 同时达到两个效果：(1) 消除审稿人"authors missed key related work"的负面印象；(2) 将 encoding domain 的结构特殊性转化为论文的理论 selling point。

【发掘点 5】
- 维度: trivial alternative 威胁
- 内容: **Proposal 低估了 modular decode-then-classify pipeline 在现代 small LM 时代的竞争力。** 论文将 "learned canonicalization" 列为已有方法并以 "error propagation + adversarial attack surface" 驳回，但这一驳斥基于隐含假设：decoder 是一个独立的 seq2seq 模型。然而，如果 decoder 本身就是一个 instruction-following small LM（如 Qwen2.5-1.5B with "decode this text" prompt），其解码能力可能相当强——因为这些模型在 pretraining 中已经见过大量编码/解码的 text。这个 pipeline（1.5B decoder → LlamaGuard-3）总参数量与 proposal 的 4B classifier 相当，但具有更好的 interpretability 和 modularity。**如果不在实验中包含一个 "modern small-LM decoder + standard guardrail" baseline，审稿人很可能会要求补充。** 建议在 baseline 中增加 "Qwen2.5-1.5B decode → LlamaGuard-3 classify" pipeline，并在 nesting-depth vs. accuracy 曲线上展示 error propagation 的实证证据（proposal 中已提到此曲线但仅作为 indirect evidence）。这实际上是一个可以赢的比较：multi-layer nesting 下 pipeline 的 error compounding 应该表现明显差于 end-to-end classifier。
- 价值: 命中 Novelty 维度（消除 trivial alternative 威胁）。如果审稿人认为存在一个更简单的替代方案没被比较，novelty score 会显著下降。主动展示 end-to-end 优于 modular pipeline（尤其在高 nesting depth），反而成为 supporting evidence for the core approach。

【补救 agent 本轮输出】:
# 补救 Agent 审查报告

【状态】: 有缺陷待补救

---

【缺陷 1】
- 类别: baseline 不足
- 问题: Proposal 在 Related Work 中以"非差分离散域"和"指数域组合"为由 dismiss 了所有 Domain Generalization (DG) 方法（IRM, DANN, CORAL, DRO），但这两条论据站不住脚。DANN 的 gradient reversal layer 作用在**表征空间**而非输入变换空间，完全不需要输入变换可微——只需将 encoding type 作为 domain label 即可训练 domain discriminator。Group DRO 更是仅需按 encoding type 分组重加权 loss，无任何额外架构改动。对于一篇核心 claim 是 OOD generalization 的论文，完全不提供任何 DG baseline 的实证对比，reviewer 几乎必然会要求补充。这是当前最大的 baseline 缺口。
- 严重度: 可补救
- 补救方案: 至少补两个 DG baseline——(1) **Group DRO**: 以 encoding type 为 group，按 worst-group loss 优化，同一 Qwen2.5-4B 架构，3 seeds，每 run ~8h，总增 6h wall-clock（4 GPU 并行）；(2) **DANN**: 加 gradient reversal layer + encoding-type auxiliary classifier，同样 3 seeds ~6h。两者均可在 Days 7-8 与 flat/reverse/static 并行训练，不影响关键路径。在 Related Work 中将论据从"不可应用"改为"可应用但我们实证表明 curriculum 优于 DG methods，因为 DG methods 缺乏对编码组合结构的利用"。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Encoding-principle OOD 的两个 held-out 家族——whitespace steganography 和 zero-width Unicode encoding——存在 **tokenizer 兼容性风险**。Qwen2.5 的 tokenizer 极可能在 tokenization 阶段对空白符做归一化（多空格合并）、并完全丢弃 zero-width characters（U+200B, U+FEFF 等）。如果 tokenizer 在预处理阶段就把编码信号消除了，那么**任何**神经模型（包括 curriculum 和所有 baseline）都无法检测该编码，测试结果将是所有方法 ASR 接近 100%——这不能说明 curriculum 的泛化失败，而是测试本身无效。Proposal 中完全没有讨论这一风险，也没有提出 tokenizer 层面的验证步骤。
- 严重度: 可补救
- 补救方案: (1) **Day 1-2 新增 tokenizer 审计步骤**: 用 Qwen2.5 tokenizer 对 whitespace stego 和 zero-width Unicode 编码的样本做 tokenize → detokenize round-trip，检查编码信号是否保留。量化信息保留率（round-trip 后可恢复的 harmful content 比例）。(2) **如果信号被消除**: 替换为 tokenizer-compatible 的编码原理 OOD 家族，例如: (a) **Morse code encoding**（用点划线文本表示字符，tokenizer 不会消除），(b) **Phone keypad encoding**（T9 数字序列，结构上与 training 编码不同但 tokenizer 保留），(c) **Pig Latin 变体**（音节重排，结构不同于字符替换/移位）。(3) **如果信号部分保留**: 报告保留率，并在实验中将其作为 "partial-signal OOD" 分类讨论，而非与 mapping-function OOD 使用相同的成功阈值。

【缺陷 3】
- 类别: 实验设计不足
- 问题: H2 对 mapping-function OOD 和 encoding-principle OOD 使用**同一阈值**（≤30% ASR vs baseline ≥60%）。这两个 OOD 层级的难度差异本质上不同——mapping-function OOD 共享训练编码的结构原理（如 character substitution），而 encoding-principle OOD 基于全新的编码范式。用同一阈值要么导致：(a) 阈值对 mapping-function OOD 太宽松，无法展示真正的泛化强度；(b) 阈值对 encoding-principle OOD 太严格，curriculum 可能合理地无法达到 ≤30%，导致 H2 被判为"failed"——但这并不意味着 curriculum 没有价值，只是泛化边界在此处。一个混合的 H2 会让结果解读变得模糊。
- 严重度: 可补救
- 补救方案: 将 H2 拆为两个子假设: **H2a (Mapping-function OOD)**: Curriculum 在 same-principle OOD 上维持 ≤20% ASR（阈值更严，展示强泛化）。**H2b (Encoding-principle OOD)**: Curriculum 在 novel-principle OOD 上相对 baselines 有 ≥15pp 的 ASR 降低（使用相对改进而非绝对阈值，承认彻底泛化可能不成立，但 curriculum 仍优于替代方案）。分开报告、分开统计检验、分开讨论。这让论文的 claim 更精确、更难被 reviewer 以"H2 部分失败"为由攻击。

【缺陷 4】
- 类别: 评估方案缺陷
- 问题: H3 表述为"ECS correlates with classifier error (Spearman ρ ≥ 0.7) on held-out encodings"，但**没有指定是哪个 classifier 的 error**。这导致循环论证风险：如果用 curriculum-trained classifier 的 error 来验证 ECS，而 ECS 又被用来构建 curriculum 训练的顺序，因果关系不清。同样，ECS 权重的 pilot study 使用"classifier error rate"来校准权重，但也没说明是哪个 classifier——如果是一个随机初始化的 classifier，几乎所有编码都会导致高 error，区分度差；如果是最终训练好的 curriculum classifier，则权重对目标模型有依赖。
- 严重度: 可补救
- 补救方案: (1) **ECS 权重校准**: Pilot study 中使用一个 **minimally-trained baseline classifier**（如在少量 plaintext harmful/benign 数据上 fine-tune 几个 epoch 的 Qwen2.5-4B），测量其在不同编码下的 error rate，以此校准 ECS 权重。这个 classifier 足够有区分度（plaintext 训练意味着编码越复杂 error 越高），又不依赖 curriculum 训练过程。(2) **H3 验证**: 报告 ECS 与**至少两个不同 classifier** error 的相关性——(a) 上述 minimally-trained baseline，(b) random-order trained classifier，(c) curriculum-trained classifier。如果 ECS 与多个 classifier 的 error 都高度相关（尤其是与 curriculum 无关的 baseline），说明 ECS 捕捉的是编码固有难度，而非 curriculum 训练的产物。

【缺陷 5】
- 类别: 评估方案缺陷
- 问题: Proposal 的第四条 contribution 明确声称"Deployment-Practical Encoding Defense"，问题陈述中也以 cost ($0.01-0.03/input) 和 latency (1-3s) 对比 frontier LLM 来论证实用性。但 Evaluation Protocol 的 metrics 部分完全没有包含 **inference latency 和 throughput 的正式测量**。没有数据支撑的"deployment-practical" claim 会被 reviewer 质疑为 hand-waving。
- 严重度: 可补救
- 补救方案: 新增 metrics：(1) **Inference latency**: 在单 A100 上，batch size=1 和 batch size=32 下的 median 和 p99 latency（ms），对比 decode+LlamaGuard-3 pipeline 和 GPT-4 API。(2) **Throughput**: tokens/second 和 queries/second。(3) **Cost per query**: 基于 A100 租赁价格计算 per-query inference cost，与 GPT-4 API cost 对比。这些测量只需 ~1h computation，可在 Day 10-11 完成。

【缺陷 6】
- 类别: 实验设计不足
- 问题: 训练数据中 harmful-encoded 与 benign 样本的**比例（class balance）**完全没有说明。Co-evolutionary attacker 只生成 harmful-encoded 样本，如果不加控制，训练集会严重偏向 harmful 类，导致 FPR 升高。Proposal 提到 FPR rollback 作为安全网，但 rollback 是被动应急机制（已经开始 overfit 才触发），不能替代主动的 class balance 设计。Benign 数据的来源、数量、是否也进行 encoding augmentation 等细节均缺失。
- 严重度: 可补救
- 补救方案: 明确说明：(1) **Benign 数据来源和规模**: 例如 LMSYS-Chat-1M 中采样 N 条 benign 对话，WildGuardTest benign set 等。(2) **训练 batch 构成**: 每 batch 中 harmful-encoded : benign 的比例（推荐 1:1 或有文献支撑的比例）。(3) **Benign 数据是否也做 encoding augmentation**: 如果不做，classifier 可能学到"encoded = harmful"的 shortcut（凡是看起来像编码的都判 harmful）。应对 benign 样本也做一定比例的 encoding augmentation，防止 encoding 本身成为 harmful 的 proxy feature。这一点尤其关键——如果 benign 数据全是 plaintext，classifier 可能不是学会了"检测 harmful content regardless of encoding"，而是学会了"检测编码的存在"。这会导致 FPR 在 encoded-benign 输入上灾难性升高，而当前的 benign test set（WildGuardTest benign + LMSYS）看起来**全是 plaintext**，不会暴露这个问题。
  
  补充测试：新增 **encoded-benign evaluation**：对 500 条 benign prompts 做与 harmful 相同的 encoding augmentation（8 types × 选取子集），测量 FPR。如果 encoded-benign FPR 远高于 plaintext-benign FPR，说明 classifier 学到了 encoding-as-harmful shortcut，而非真正的 content extraction。

---

**总结**: 以上 6 个缺陷均可补救，无方向性致命问题。其中**缺陷 1（DG baseline 缺失）**和**缺陷 6（class balance + encoded-benign evaluation）**最为关键——前者是 reviewer 几乎必问的 baseline 问题，后者是一个实验设计上可能导致核心 claim 被根本性质疑的漏洞（classifier 可能只是在检测 encoding 的存在而非提取 harmful content）。建议优先处理这两个。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4237f473-ff8d-41ef-8dab-d62f5b787fbd",
  "isSidechain": false,
  "promptId": "4eb43877-c31f-4fd3-affc-68f1c3db33d1",
  "type": "user",
  "uuid": "71b7b881-9f6c-4819-80df-87e4f892beec",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 4 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough context to provide a thorough assessment. Let me deliver my analysis.  ---  【状态】: 有发掘空间…",
  "leafUuid": "71b7b881-9f6c-4819-80df-87e4f892beec",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Assistant

_source line 40 · 2026-05-16T12:34:25.510Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the Round 4 outputs from both agents.

**发掘 agent Round 4:**

1. **发掘点 1 (Encoding-principle OOD logical gap):** This is extremely important. The agent points out that whitespace steganography and zero-width Unicode fundamentally differ from training encodings — training encodings carry information in *visible* tokens, while these carry information in *invisible* characters. The two-regime mechanism doesn't explain why skills for visible token patterns would transfer to invisible character detection. This is a genuine logical flaw. The suggestion is either (a) replace with more logically coherent OOD tests, or (b) reframe as "boundary tests" showing *where* curriculum generalization stops — which is actually more scientifically valuable. 

I think option (b) is the way to go here — demonstrating scope conditions is more compelling than claiming unbounded generalization.

2. **发掘点 2 (Compositional generalization connection):** The SCAN/COGS literature angle has merit and could strengthen the theoretical contribution, but I need to be careful not to oversell this. We've already tried several angles to boost significance, and the risk of overclaiming is real. I'll weave in compositional generalization as a related framework without restructuring the entire narrative around it.

3. **发掘点 3 (Differential prediction for mechanism):** This is compelling — distinguishing between the trivial explanation (curriculum just prevents catastrophic forgetting) and the actual mechanism (progressive skill acquisition through structured learning) would be a strong empirical test.

4. **发掘点 4 (Compositional generalization + curriculum mixed results):** Worth including in related work. The insight is that curriculum succeeds here because the encoding space has inherent compositional structure with a natural difficulty gradient, whereas arbitrary orderings fail elsewhere.

5. **发掘点 5 (Small LM decoder baseline):** This is a legitimate concern. Using a realistic modern pipeline like Qwen2.5-1.5B as the decoder with LlamaGuard-3 should definitely be included.

Now looking at the empirical baselines issue — the point about needing direct comparisons with domain generalization methods is strong, and I shouldn't dismiss it without evidence.  DANN operates on representation space and DRO just reweights losses, so both can actually be adapted to treat encoding types as domains. I need to add Group DRO and DANN baselines.

The tokenizer compatibility concern is critical too. If Qwen2.5's tokenizer normalizes or strips zero-width characters and whitespace, the entire OOD encoding test becomes invalid. I should audit the tokenizer behavior and potentially use alternatives that preserve these properties.

For the hypothesis structure, splitting H2 into two parts makes sense — H2a for mapping-function OOD with strict thresholds and H2b for encoding-principle OOD with relative improvement metrics. That's more precise and defensible.

ECS calibration needs to happen on a minimally-trained baseline rather than a curriculum-trained one, and H3 validation should span multiple classifiers to avoid overfitting to a single architecture.

Latency and throughput measurements are straightforward to add if I'm claiming deployment practicality.

The class balance issue is the most critical finding here. If benign training data is entirely plaintext while harmful data gets encoded, the classifier could learn "encoding = harmful" as a spurious shortcut instead of actually extracting content. This would completely invalidate the core claim. I need to augment benign data with encodings and create an encoded-benign test set to properly evaluate whether the model learns content extraction or just surface-level encoding patterns.

Looking at convergence across rounds, both agents are still identifying substantive gaps, but the issues are becoming more granular and technical rather than fundamental. The 发掘 agent's new point about OOD logic coherence in the encoding-principle tests added last round is genuinely critical, and the 补救 agent's tokenizer compatibility concern reinforces that there's a real logical problem here—the whitespace steganography and zero-width Unicode tests may not actually test what I think they're testing.

This isn't a back-and-forth collapse; it's catching an overreach from Round 3 that needs correction. Replacing those extreme OOD claims with a more careful "scope conditions" analysis will actually strengthen the paper. But I'm noticing the core framework has held steady since Round 2, and now we're mostly iterating on which specific tests to include, what baselines to add, and methodological details like class balance and latency measurement. These refinements matter, but they're incremental rather than reshaping the work fundamentally.

Looking ahead to Round 5, I expect the discovery and correction agents will mostly find minor framing adjustments and small methodological tweaks—we're approaching the point where further iterations yield diminishing returns. I should push to Round 5 as the final round, treating it as convergence or the hard limit. The probability should improve meaningfully from these Round 4 changes—the OOD fix makes the claim more defensible, the domain generalization baselines strengthen the curriculum comparison, the encoded-benign evaluation validates the core claim, and the differential prediction analysis shows mechanistic depth. I'm estimating this moves us from 28-40% (median 34%) toward potentially reaching that 36% threshold. - Small-LM decoder baseline → eliminates key trivial alternative
- Latency measurements → supports "deployment-practical" claim

The encoded-benign issue (缺陷6) is concerning — if it's a real problem, it could have been devastating. But the fix is straightforward (add encoding augmentation to benign data + test encoded-benign FPR).

After incorporating Round 4:
- Novelty: Medium-Strong (OOD claim more nuanced but more defensible; differential prediction adds mechanistic depth; DG comparison shows curriculum > standard approaches)
- Significance: Medium-Strong (deployment-practical positioning with latency data; compositional generalization connection)
- Technical Soundness: Strong (DG baselines, encoded-benign evaluation, class balance, tokenizer audit, latency measurement)
- Idea ceiling: ~43-45% (narrowing the OOD claim makes it more robust)
- Current estimate: [30% - 42%] median 36%

We're hovering right around the 36% mark, which is a solid position. One more round of agent convergence should either push us to [32% - 43%] with a median around 37-38%, or confirm we've hit the ceiling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71b7b881-9f6c-4819-80df-87e4f892beec",
  "isSidechain": false,
  "requestId": "req_011Cb6Fie7hbYNP3SiqAETxQ",
  "type": "assistant",
  "uuid": "8eac9992-2d8b-4a2d-a024-6f5a7bf0a098",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpXF57MhUQW8aJYfvYwgDy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15302,
      "cache_read_input_tokens": 45473,
      "output_tokens": 8892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8892,
          "cache_read_input_tokens": 45473,
          "cache_creation_input_tokens": 15302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15302
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

_source line 41 · 2026-05-16T12:37:19.704Z_

【阶段】: 迭代第 4 轮
【发掘 agent 有效建议采纳】:
- **采纳发掘点 1（encoding-principle OOD 逻辑断裂）**：本轮最关键发现。Whitespace steganography 和 zero-width Unicode 的信息承载方式（不可见字符）与训练编码（可见 token 序列变换）根本不同——curriculum 积累的"可见 token 结构模式识别"技能在逻辑上无法迁移到"检测不可见字符中隐藏信息"。**采纳方案 (b)**：将 encoding-principle OOD 重新定位为 "boundary test"——预测这些族上 curriculum 不应 outperform baselines，展示泛化的 scope conditions。同时替换 whitespace/zero-width（因 tokenizer 兼容性问题）为 tokenizer-compatible 的 principle-level OOD（Pig Latin 音节重排、T9 keypad 数字序列）+ 保留 Morse code 作为 mapping-function OOD。最终 OOD 分层：mapping-function OOD（预期 curriculum 强优势）→ encoding-principle OOD（预期 curriculum 有限优势或无优势 → 这是 scope condition 的积极发现）。
- **采纳发掘点 3（differential prediction）**：非常强的建议。区分 trivial explanation（catastrophic interference prevention → 均匀优势）和 claimed mechanism（progressive decoding skill acquisition → 优势随 nesting depth 递增）。按 nesting depth 分层报告 curriculum vs. random gap，如果 gap 递增则支持 claimed mechanism。
- **部分采纳发掘点 2**（compositional generalization 连接）：在 Related Work 中连接 SCAN/COGS 文献，将编码空间定位为 compositional transformation space 的实例，但不将论文 primary framing 改为 compositional generalization paper（单一 domain 验证 + 不是标准 compositional generalization 设置，overclaim 风险大）。
- **采纳发掘点 4**（curriculum mixed results 论证）：在 Related Work 中加入关键论证：curriculum 在本 domain 有效是因为编码空间有 *intrinsic compositional structure with natural difficulty ordering*（nesting depth 提供非人工定义的 metric），区别于 curriculum 失败的 domains。
- **采纳发掘点 5**（small-LM decoder baseline）：增加 "Qwen2.5-1.5B decode → LlamaGuard-3" pipeline baseline，在 nesting depth 曲线上展示 error compounding。

【补救 agent 有效建议采纳】:
- **采纳缺陷 1（DG baselines）**：增加 Group DRO（encoding type 为 group）+ DANN（gradient reversal on encoding type）两个 DG baselines，同架构 3 seeds。修改 Related Work 论述为"DG methods 可应用但 curriculum 实证优于 DG，因 DG 不利用编码组合结构"。
- **采纳缺陷 2（tokenizer 审计）**：Day 1-2 新增 tokenizer round-trip 审计。确认 zero-width / whitespace 编码信号是否保留；如不保留则替换为 tokenizer-compatible alternatives（已与发掘点 1 方案合并）。
- **采纳缺陷 3（H2 拆分）**：H2 拆为 H2a（mapping-function OOD，绝对阈值 ≤20% ASR）和 H2b（encoding-principle OOD，相对改进 ≥15pp over baselines 或明确报告为 scope condition/boundary test）。
- **采纳缺陷 4（ECS 循环论证）**：ECS 权重校准使用 minimally-trained baseline（plaintext-only fine-tuned Qwen2.5-4B）。H3 验证 ECS 与至少 2 个不同 classifier（minimally-trained + random-order trained）的 error 相关性。
- **采纳缺陷 5（latency 测量）**：新增 inference latency（单 A100, batch=1 和 32）、throughput、per-query cost 对比。
- **采纳缺陷 6（class balance + encoded-benign）**：**本轮实验层面最关键补丁。** (a) 训练 batch 中 harmful-encoded : benign = 1:1，benign 数据同样做 encoding augmentation（防止"encoded=harmful" shortcut）；(b) 新增 encoded-benign evaluation（500 benign prompts × encoding augmentation，测 FPR）。这直接验证 classifier 学到的是 content extraction 而非 encoding detection。

【本轮 proposal 主要变更】:
**Idea 层面**:
- OOD claim 精确化：mapping-function OOD（预期强泛化）+ encoding-principle OOD（重新定位为 boundary/scope condition test）
- Encoding-principle OOD 替换为 tokenizer-compatible alternatives（Pig Latin, T9 keypad）
- 增加 differential prediction：curriculum 优势应随 nesting depth 递增（区分 trivial mechanism）
- 连接 compositional generalization 文献 + curriculum mixed results 论证
- DG 文献定位从"不可应用"修正为"可应用但 curriculum 实证更优"

**实验层面**:
- 增加 Group DRO + DANN baselines（3 seeds each）
- 增加 Qwen2.5-1.5B decode → LlamaGuard-3 pipeline baseline
- Benign 训练数据也做 encoding augmentation（防 shortcut）
- 新增 encoded-benign evaluation（验证不是 encoding-as-harmful detection）
- H2 拆为 H2a + H2b
- ECS 权重校准改为 minimally-trained baseline，验证跨 classifier 相关性
- 新增 inference latency/throughput/cost 测量
- Tokenizer 审计步骤加入 Day 1-2
- Nesting-depth-stratified curriculum vs. random gap 分析

【idea 质量评估】: Novelty=中偏强（OOD claim 收窄但更 defensible——scope conditions 展示比 overpromise 更好；differential prediction 提供 mechanistic depth 超越"empirical observation"；与 DG/CAT/CompGen 文献清晰定位。天花板被 OOD scope 限制略微压低但 claim robustness 大幅提升） Significance=中偏强（deployment-practical 有 latency 数据支撑；general principle 作为 interpretive framework 合理；compositional attack space 方法论对社区有参考价值） → idea 天花板约 42%

【实验完备性评估】: Technical Soundness=强（DG baselines 堵住最大 reviewer concern；encoded-benign evaluation 验证不是 shortcut learning；differential prediction 区分 trivial mechanism；class balance 明确化；ECS 去循环论证；latency 支撑 deployment claim。残留：learned canonicalization 完整训练未做——已明确为 limitation + small-LM decoder pipeline 作为 proxy） → 地板牢固

【当前概率估计】: [30% - 42%] 中位 36%

【决策】: 继续

【决策理由】: 概率从 34% 升至 36%，恰好触及阈值。但本轮两个 agent 仍各自产出了高价值建议（尤其发掘点 1 的 OOD 逻辑修正和补救缺陷 6 的 encoded-benign evaluation），说明 proposal 尚未完全稳定。需要第 5 轮（硬上限轮）确认：(1) 机制 framing 现在是否逻辑闭合无新漏洞；(2) 实验设计是否已完备无新 gap。如果 Round 5 两个 agent 趋向收敛或只提出微调，则可在硬上限处收敛输出最终方案。当前不提前收敛的原因：本轮做了较大调整（OOD 重构 + DG baselines + encoded-benign），下一轮需要验证这些调整是否引入新问题。

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
## Title

EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training

## Problem Statement

Encoding-based jailbreak attacks (base64, ROT13, homoglyph substitution, and their nested compositions) exploit a fundamental vulnerability in LLM safety guardrails: classifiers trained on plaintext or limited encoding variations fail when inputs are transformed through unseen encoding schemes. Existing defenses have critical limitations:

1. **Rule-based detection + decoding pipelines** (regex detection → known decoder → standard guardrail): Effective for known single-layer encodings with distinctive statistical signatures. Fail on: (a) partial encoding, (b) adversarial mixing of encoded/plaintext, (c) novel encodings without pre-programmed decoders.

2. **Learned/LM-based canonicalization** (small LM decode → classify): Error propagation compounds across nesting layers; the canonicalizer itself becomes an adversarial attack surface; partial encoding requires semantic understanding to identify decode targets.

3. **Frontier LLM zero-shot** (GPT-4/Claude prompted to detect harmful content regardless of encoding): Leverages pre-training exposure but impractical for deployment-scale guardrails ($0.01-0.03 per input, 1-3s latency vs. millisecond-level local inference).

The core challenge is achieving **generalization to unseen encoding families at deployment-practical cost**—a lightweight classifier that remains robust against encoding types never encountered during training.

## Core Thesis

We hypothesize that a classifier trained via **complexity-structured curriculum**—where encoding attacks are presented in order of a principled complexity metric—acquires **encoding-robust content extraction capabilities** that generalize to held-out encoding types unseen during training.

**Mechanism (Two-Regime, with Differential Prediction):**

- **Low-ECS regime (simple encodings):** Content semantics remain partially accessible through tokenization. Curriculum forces the model to anchor harmful-content semantic features despite mild surface perturbation (**content anchoring**).

- **High-ECS regime (complex/nested encodings):** Token-level content information is destroyed by multi-layer encoding. The model develops strategies for implicit decoding—recognizing encoding structure patterns and compositionally reconstructing content signal (**progressive decoding skill acquisition**).

**Differential prediction distinguishing our mechanism from trivial catastrophic-interference prevention:** If the mechanism is progressive decoding skill acquisition (compositional skill building), curriculum's advantage over random-order should *increase with nesting depth* (deeper nesting requires more compositional decoding skill). If the mechanism is merely preventing catastrophic interference (protecting base content features), the advantage should be approximately uniform across nesting depths. We explicitly test this prediction.

**Important clarification:** We do NOT claim literal "encoding-invariant features" in the information-theoretic sense (impossible for fully-scrambled sequences). Rather, curriculum builds a progressive hierarchy of decoding capabilities that transfers across encoding types sharing structural properties with training encodings. We explicitly characterize where this transfer succeeds (same encoding principle, different mapping) and where it reaches its limits (fundamentally different encoding paradigms)—establishing **scope conditions** for curriculum-induced generalization.

## Relationship to Prior Work

### Curriculum Adversarial Training
Cai et al. (IJCAI 2018): progressive perturbation magnitude for images. Wang et al. (NeurIPS 2021): ordered SGD by difficulty. Key differences:
1. **Discrete compositional space vs. continuous perturbation:** Encoding attacks form a combinatorial space (N primitives × K nesting levels) requiring multi-dimensional complexity metrics, unlike scalar ε-balls.
2. **OOD generalization vs. in-distribution robustness:** We explicitly test generalization to unseen encoding families, not just robustness to trained attack types.

**Why curriculum works here but has mixed results elsewhere:** Encoding space possesses *intrinsic compositional structure with natural difficulty ordering*—nesting depth provides a non-arbitrary complexity axis. This contrasts with domains where curriculum orderings are artificial/researcher-imposed (known failure mode in curriculum literature).

### Domain Generalization (DG)
Each encoding type as a domain; OOD generalization ≈ DG to unseen domains. Standard DG methods (IRM, DANN, CORAL, DRO) ARE applicable to this setting (contrary to some claims about discrete spaces—DANN operates on representations, DRO on loss weighting). However, we hypothesize that **curriculum is superior to standard DG here** because DG methods treat domains as unstructured categories, while curriculum explicitly exploits the compositional complexity structure of the encoding space. We empirically validate this with Group DRO and DANN baselines.

### Compositional Generalization
The encoding attack space (N primitives × K layers = O(N^K) compositions) is a discrete compositional transformation space, connecting to the compositional generalization literature (SCAN, COGS). Our work investigates whether structured curriculum can facilitate compositional generalization in transformation spaces—a question not addressed by prior compositional generalization work, which focuses on input-output mapping generalization rather than adversarial robustness.

## Key Contributions

1. **Primary Contribution (OOD Generalization + Scope Conditions):** Empirical demonstration that complexity-structured curriculum enables generalization to unseen encoding types at two levels—mapping-function OOD (strong transfer) and encoding-principle OOD (limited transfer, establishing scope conditions). Direct representation-level evidence (CKA + linear probing) + mechanistic differential prediction (nesting-depth-dependent advantage).

2. **Encoding Complexity Score (ECS):** Formalized metric validated via cross-classifier correlation analysis; individual components quantified; shown to predict difficulty independently of training method.

3. **Co-Evolutionary Training Framework:** GRPO attacker + SFT classifier with curriculum ordering, demonstrating co-evolution further improves upon static curriculum.

4. **Deployment-Practical Encoding Defense:** 4B classifier achieving encoding robustness competitive with frontier LLM zero-shot at orders-of-magnitude lower latency and cost (quantified with formal inference benchmarks).

## Methodology

### Encoding Complexity Score (ECS)

$$ECS(e) = \alpha \cdot \text{NestingDepth}(e) + \beta \cdot \text{CPT\_Deviation}(e) + \gamma \cdot \text{TokenizerPerplexity}(e)$$

**Weight calibration:** Using a minimally-trained baseline classifier (Qwen2.5-4B fine-tuned only on plaintext harmful/benign data, ~1h training), measure each component's Spearman ρ with classifier error across 200 encoding variants. Weights set proportional to individual predictive power. This avoids circular dependency with curriculum training.

**Component contribution analysis:** Report (a) single-component Spearman ρ, (b) leave-one-out ρ change, (c) composite vs. best single component. All computed on evaluation data without retraining.

**Cross-classifier validation (H3):** Report ECS correlation with error rates from: (i) minimally-trained baseline, (ii) random-order trained classifier, (iii) curriculum-trained classifier. High correlation across all three demonstrates ECS captures intrinsic encoding difficulty, not training-method-specific difficulty.

### Training Design

**Attacker (Qwen2.5-1.5B, GRPO):**
- Generates encoding attacks within current curriculum ECS band
- Reward: +1 if bypasses classifier AND oracle confirms harmful
- Entropy regularization prevents encoding-type collapse

**Classifier (Qwen2.5-4B, SFT):**
- Curriculum-ordered: Stage 1 (ECS ≤ threshold) → Stage 2 (ECS > threshold)
- FPR rollback: revert if FPR > 2%
- Semantic deduplication (cosine > 0.95)

**Class Balance and Shortcut Prevention:**
- Training batch composition: 50% harmful-encoded + 50% benign
- **Critical:** Benign training data ALSO undergoes encoding augmentation (same encoding types and ECS distribution as harmful data). This prevents the classifier from learning "encoded = harmful" shortcut—it must learn to detect harmful *content* regardless of encoding, not merely detect encoding's *presence*.
- Benign data source: LMSYS-Chat-1M (5K samples) + WildGuardTest benign (1K samples), encoded with same pipeline

**Oracle:** GPT-4o + deterministic decoder cross-validation; disagreements excluded.

**Fallback:** If co-evolutionary loop unstable by Day 7, switch to static curriculum SFT.

### Baseline Definitions

| Method | Data Source | Ordering | Key Variable | Seeds |
|--------|------------|----------|--------------|-------|
| **Curriculum (ours)** | Co-evolutionary/static, ECS-staged | Monotone ↑ ECS | — | 5 |
| **Random-order** | Same data as curriculum | Shuffled | Ordering | 5 |
| **Flat augmentation** | Uniform random encoding per prompt per epoch | Random | Data composition + ordering | 3 |
| **Reverse curriculum** | Same data | Monotone ↓ ECS | Direction | 3 |
| **Static curriculum** | Rule-based, ECS-ordered | Same as curriculum | Co-evolution effect | 3 |
| **Group DRO** | Same data as flat | Worst-group (encoding type) loss | DG approach | 3 |
| **DANN** | Same data as flat | Gradient reversal on encoding type | DG approach | 3 |
| **Qwen2.5-1.5B decode → LlamaGuard-3** | N/A (inference) | N/A | Pipeline approach | 1 |
| **Deterministic decode → LlamaGuard-3** | N/A (inference) | N/A | Rule-based pipeline | 1 |
| **GPT-4 zero-shot** | N/A (API) | N/A | Cost/accuracy frontier | 1 |

Key distinctions:
- Random-order vs. Flat: Random-order = same data, shuffled (isolates ordering). Flat = uniform encoding sampling (different data distribution).
- Group DRO / DANN: Standard DG methods using encoding type as domain label. Tests whether structured curriculum > unstructured domain-invariance objectives.

### Compute Fairness

- **H1-H3 (core claims):** Static curriculum vs. baselines. All use identical Qwen2.5-4B, identical training FLOPs (measured and reported), identical total steps. Variable: data ordering/composition/loss function.
- **H4 (co-evolution, bonus):** Extra compute from attacker. Include compute-matched static variant (extra FLOPs → more training epochs) for fair comparison.
- **Reporting:** Table with total classifier FLOPs, total system FLOPs (incl. attacker), wall-clock, training tokens per method.

### Compute and Cost

- Hardware: 4× A100 80GB
- Per classifier run: ~8h
- Total classifier runs: 5+5+3+3+3+3+3 = 25 runs → parallelized 4 at a time → ~50h
- Attacker: 12h (2 rounds)
- Oracle: ~18K calls ≈ $250
- GPT-4 zero-shot eval: ~15K calls ≈ $150
- Inference analyses (probing, CKA, latency): ~4h
- Total: ~66h wall-clock training + evaluation

## Experimental Design

### Hypotheses

- **H1 (Curriculum > Random):** Curriculum achieves ≥10pp lower encoding-ASR than random-order (95% bootstrap CI excludes 0, Cohen's d reported).
- **H2a (Mapping-Function OOD):** Curriculum maintains ≤20% ASR on mapping-function OOD encodings (Braille, custom cipher, NATO phonetic) where baselines exceed 50%.
- **H2b (Encoding-Principle OOD — Scope Condition):** On structurally different encoding principles (Pig Latin, T9 keypad), report curriculum vs. baselines gap. If curriculum outperforms by ≥15pp → evidence of broader generalization. If no significant difference → establishes scope boundary (curriculum generalizes within structural families, not across fundamentally different paradigms). Both outcomes are informative.
- **H3 (ECS Predictiveness):** ECS correlates with error (Spearman ρ ≥ 0.7) across multiple classifiers; composite outperforms any single component.
- **H4 (Co-evolution > Static, bonus):** Co-evolutionary > static by ≥5pp on composite encodings after compute normalization.

**Differential Prediction (Mechanism Test):**
- Partition test results by nesting depth (1, 2, 3)
- Compute (curriculum ASR - random ASR) at each depth
- Progressive decoding hypothesis → gap increases with depth
- Catastrophic interference hypothesis → gap approximately constant
- Report trend with significance test

### Held-Out Encoding Families

**Mapping-function OOD (same structural principle, different specific mapping):**
- Braille Unicode substitution (character substitution — cf. homoglyphs)
- Custom Caesar cipher with position-dependent shift (shift-based — cf. ROT13)
- NATO phonetic alphabet (word-level substitution — novel granularity)
- Morse code (symbolic encoding — cf. base64)

**Encoding-principle OOD (boundary test — structurally different paradigm):**
- Pig Latin variant (syllable rearrangement — morphological transformation, unlike any character/symbol substitution in training)
- T9 phone keypad encoding (multi-character → single digit mapping with ambiguity — lossy encoding unlike all training encodings which are lossless)

**Tokenizer Audit (Day 1-2):** Verify all held-out encodings survive tokenize → detokenize round-trip with information preservation rate ≥ 90%. Replace any encoding that fails this check.

### Evaluation Protocol

**External benchmarks (primary):**
- HarmBench encoding-perturbed
- JailbreakBench encoding subset
- WildGuardTest encoding-perturbed

**EncoAttack (supplementary):**
- 500 base prompts: HarmBench (200) + AdvBench (150) + WildGuardTest (150)
- 8 encoding types × 3 nesting levels = 12,000 test cases
- Independent implementation from training pipeline
- Validated ≥80% bypass on undefended LlamaGuard-3

**Held-out encodings:** 6 families as above (4 mapping-function + 2 encoding-principle)

**GPT-4 zero-shot reference:** Same test sets

**Metrics:**
- Encoding-ASR (primary)
- **Clean FPR on plaintext benign** (WildGuardTest benign ~1000 + LMSYS-Chat-1M 1000)
- **Encoded-benign FPR** (500 benign prompts × encoding augmented — CRITICAL: tests whether classifier detects harmful content vs. detects encoding presence)
- FPR at multiple thresholds (0.5%, 1%, 2%, 5%) with Pareto frontier
- Per-encoding-type breakdown
- Nesting-depth-stratified curriculum advantage (differential prediction)
- ECS correlation (composite + individual + cross-classifier)
- Nesting-depth vs. decode-accuracy curve (error propagation for pipeline baselines)

**Inference Performance:**
- Latency: single A100, batch=1 and batch=32, median + p99 (ms)
- Throughput: queries/second
- Cost per query: based on A100 hourly rate vs. GPT-4 API
- Compare: EncoGuard vs. Qwen-decode+LlamaGuard vs. GPT-4 zero-shot

### Representation Analysis

1. **CKA + Cosine Similarity:** 100 prompts × (plaintext + 8 encoding variants), penultimate-layer representations. Intra-prompt cross-encoding similarity: curriculum vs. baselines.

2. **Linear Probing (Disentanglement):**
   - Probe A: predict content category → curriculum should match or exceed baselines
   - Probe B: predict encoding type → curriculum should show LOWER accuracy (encoding info discarded)
   - Encoded-benign probing: verify that benign encoded inputs are NOT classified as harmful clusters

3. **Learning Dynamics:** Per-checkpoint (500 steps) ASR curves, stratified by ECS level. Expected: curriculum shows staged convergence; random-order shows chaotic learning.

### Statistical Rigor

- Curriculum + random-order: 5 seeds each. Others: 3 seeds.
- H1: 95% bootstrap CI on paired difference + Cohen's d
- H2a/H2b: Reported with confidence intervals
- Bonferroni correction for H1-H3 family
- All results tables include mean ± std

### Oracle Pilot (Day 1-2)

100 samples per ECS band. GPT-4o + deterministic decoder agreement. < 80% → deterministic-only for that band.

## Stability Mechanisms (Not Contributions)

- Entropy regularization, FPR rollback, semantic deduplication
- Trigger frequencies reported; full ablation in camera-ready

## Acknowledged Limitations

1. Full learned canonicalization (seq2seq) not trained as baseline; addressed via small-LM decode pipeline + nesting-depth error curve
2. General principle validated only on encoding attacks; other compositional spaces = future work
3. ECS weight sensitivity: ±20% perturbation in supplementary
4. Encoding-principle OOD may show limited/no curriculum advantage—reported as scope condition

## Timeline (17 days)

**Phase 1: Setup + Pilot (Days 1-3)**
- ECS implementation, encoding generators (all 6 held-out families), data pipeline
- Tokenizer audit for all held-out encodings
- Oracle pilot (100/band)
- Fast pilot run (reduced data, 2h) → validate training dynamics, ECS threshold, class balance

**Phase 2: Core Training (Days 4-9)**
- Days 4-6: Curriculum (5 seeds) + random-order (5 seeds) [4 GPU parallel]
- Days 7-8: Flat (3) + reverse (3) + Group DRO (3) + DANN (3) [parallel]
- Day 9: Static curriculum (3) + compute-matched static (3) + co-evolutionary attempt

**Phase 3: Evaluation + Analysis (Days 10-12)**
- Day 10: Full benchmark eval + held-out + GPT-4 zero-shot + pipeline baselines
- Day 11: Representation analysis + ECS stats + learning dynamics + encoded-benign eval
- Day 12: Statistical tests, nesting-depth analysis, latency benchmarks, Pareto curves

**Phase 4: Writing (Days 13-15)**
- Drafting + figures + tables

**Buffer (Days 16-17)**
- Additional runs if needed, stability ablation, revision

**Fallback:** Co-evolutionary unstable by Day 8 → focus H1-H3 with static curriculum.
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8eac9992-2d8b-4a2d-a024-6f5a7bf0a098",
  "isSidechain": false,
  "requestId": "req_011Cb6Fie7hbYNP3SiqAETxQ",
  "type": "assistant",
  "uuid": "cd331a09-f967-431f-b1f6-269e06feee84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpXF57MhUQW8aJYfvYwgDy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15302,
      "cache_read_input_tokens": 45473,
      "output_tokens": 8892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8892,
          "cache_read_input_tokens": 45473,
          "cache_creation_input_tokens": 15302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15302
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 4 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough context to provide a thorough assessment. Let me deliver my analysis.  ---  【状态】: 有发掘空间…",
  "leafUuid": "cd331a09-f967-431f-b1f6-269e06feee84",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 4 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough context to provide a thorough assessment. Let me deliver my analysis.  ---  【状态】: 有发掘空间…",
  "leafUuid": "cd331a09-f967-431f-b1f6-269e06feee84",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 47 · 2026-05-16T12:39:23.269Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:39:23.269Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "content": "【任务】: 以「角色 B：迭代中」整合第 5 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\n【状态】: 有发掘空间\n\n---\n\n【发掘点 1】\n- 维度: significance 提升 / 核心 claim 强化\n- 内容: 当前 framing 将论文定位为\"encoding jailbreak 的防御方法\"，但论文真正回答的科学问题更大：**\"结构化 curriculum 何时能诱导离散组合变换空间中的 compositional generalization？\"** Encoding attacks 只是这个问题的一个 case study。建议将 primary contribution 重新定位为：对这个更一般性问题给出实证回答（positive result within structural families + negative/limited result across paradigms），safety 应用是高价值 instantiation 而非目的本身。这样论文的 audience 从 safety 社区扩展到 representation learning + compositional generalization 社区，reviewer pool 中 \"觉得这只是 engineering trick\" 的概率显著降低。\n- 价值: 命中 Significance。EMNLP main 的 bar 要求 general insight；当前 framing 太窄（只对 encoding jailbreak 有用），会被审稿人归类为 \"application paper\"。拓宽后 contribution 的 ceiling 提升一个 tier。\n\n【发掘点 2】\n- 维度: novelty 锐化\n- 内容: 当前 proposal 的 differential prediction（curriculum advantage 随 nesting depth 增加 → 支持 progressive decoding 而非 catastrophic interference prevention）是 novelty 最锐利的点，但它被埋在 methodology 中。建议将其提升为 **论文的核心 scientific claim**：\"Curriculum induces compositional decoding skill building, not merely interference prevention—evidenced by depth-dependent advantage.\" 这个 claim 区别于所有已有 curriculum learning 工作（它们只证明 curriculum works，不区分 WHY it works）。如果 differential prediction 得到验证，这是对 curriculum learning mechanism 的 novel empirical insight，不仅限于 encoding 场景。\n- 价值: 命中 Novelty。现有 curriculum learning 文献几乎没有 mechanistic explanation 的 empirical test。这个 differential prediction 从 \"我们方法好\" 升级为 \"我们理解了为什么好\"，直接回应 \"why not just random order with more epochs\" 的 reviewer challenge。\n\n【发掘点 3】\n- 维度: trivial alternative 威胁\n- 内容: 论文未充分回应一个 trivial alternative：**如果将模型从 4B 放大到 7B/13B + flat augmentation，是否能匹配 4B + curriculum 的 OOD 性能？** 如果是，则 curriculum 的贡献退化为 \"compute-efficiency trick\"（降低发表价值）。论文需要明确其 claim 是 (a) curriculum 在同等模型规模下带来 fundamental generalization capability improvement（不可通过 scaling 替代），还是 (b) curriculum 是 efficiency method（同等性能用更小模型）。目前 proposal 暗示 (a) 但未排除 (b)。建议在 core thesis 中显式声明：curriculum exploits compositional structure that model scaling alone cannot discover without appropriate training signal ordering——并用 representation analysis (CKA/probing) 来区分 (curriculum 诱导出 qualitatively different representations, not just stronger versions of the same representations)。\n- 价值: 命中 Novelty。如果审稿人认为 \"你只是用了 curriculum 因为你 model 小，大模型不需要\"，整个 novelty claim 崩塌。显式回应这个 alternative 并提供 representation-level 证据将堵住最危险的 review attack。\n\n【发掘点 4】\n- 维度: related work 差异化\n- 内容: 论文与 compositional generalization 文献的连接目前停留在 surface level（\"connecting to SCAN, COGS\"）。但存在一个更直接相关的工作线：**meta-learning for compositional generalization**——如 Lake & Baroni (2018) 关于 systematic generalization、以及后续使用 meta-learning curriculum 来诱导 compositional skills 的工作（如 ICLR 2023 的 compositional generalization via meta-learning）。如果这些工作已经证明 structured training ordering 能帮助 compositional tasks，那本文的 novelty 需要更精确地定位：不是 \"curriculum helps compositional generalization\"（已知），而是 \"在 adversarial robustness 的离散变换空间中，curriculum 的优势来源与 NLP compositional tasks 中的机制不同（decoding skill vs. syntactic rule generalization）\"。\n- 价值: 命中 Related Work 差异化。如果审稿人熟悉 compositional generalization + meta-learning 文献，缺乏对这条线的显式区分会被视为 insufficient awareness of related work，直接扣分。\n\n【发掘点 5】\n- 维度: 前提假设质疑\n- 内容: 核心假设 \"high-ECS regime 中 token-level content information is destroyed\" 需要验证。如果 4B model 在 base64(ROT13(x)) 上确实无法从 token 层面获取任何 content signal，那它能通过 curriculum \"学会 implicit decoding\" 的假设依赖于一个未说明的前提：**训练数据中存在足够的中间复杂度样本来建立 decoding skill 的 gradient path**。但如果 ECS 空间中存在 \"complexity cliff\"（某个 nesting level 之后信息突然断崖式消失），curriculum 的 gradual 优势就不存在——模型在某个 threshold 以上无法学到任何东西，无论顺序如何。建议在 core thesis 中显式加入 **continuity assumption**: the encoding space provides a smooth difficulty gradient (no phase transition in extractable information). 并在 pilot phase 验证此假设（per-layer information retention measurement）。\n- 价值: 命中 Novelty 的根基。如果这个 continuity assumption 不成立，整个 \"progressive skill acquisition\" 的机制故事崩塌，differential prediction 也失去诊断力。显式声明并验证此假设反而加强了论文的 scientific rigor，让审稿人无法用 \"but what if the gradient isn't smooth\" 来攻击。\n\n【补救 agent 本轮输出】:\n【状态】: 有缺陷待补救\n\n---\n\n整体评估：本 proposal 的实验设计已经接近 EMNLP 主会水准——baseline 覆盖面广且隔离变量清晰、ablation 通过对比结构自然实现、评估方案多维度覆盖、可行性大致合理。以下缺陷均为可补救的细节问题，修补后实验设计可达到主会投稿的 solid 水平。\n\n---\n\n【缺陷 1】\n- 类别: compute 公平性问题\n- 问题: DANN baseline 引入了额外的 domain discriminator 网络和 gradient reversal layer，带来额外参数和 FLOPs。Proposal 在 Compute Fairness 部分声明\"All use identical Qwen2.5-4B, identical training FLOPs\"，但未说明 DANN discriminator head 的额外计算如何处理。Reviewer 会质疑：如果 DANN 多花了 FLOPs 在 discriminator 上仍不如 curriculum，是 DANN 方法弱还是 compute 不公平？如果不计 discriminator FLOPs，那 DANN 实际上获得了\"免费\"额外参数。\n- 严重度: 可补救\n- 补救方案: 在 Compute Fairness 小节明确说明：(a) DANN discriminator head 参数量相对 4B classifier 可忽略（量化：discriminator 约占总参数 <0.5%），因此统一按 classifier backbone forward/backward FLOPs 计算；(b) 额外报告 DANN total FLOPs（含 discriminator）作为 transparency，让 reviewer 自行判断。一句话即可解决。\n\n---\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: Differential prediction（核心机制验证）将测试数据按 nesting depth 分为 3 层（depth 1, 2, 3），然后检验 (curriculum ASR − random ASR) 随 depth 的递增趋势。但 proposal 未说明每个 depth 层的测试样本量。若 EncoAttack 的 12,000 test cases 按 8 types × 3 depths 分配，每个 depth 约 4,000 cases，但这是总计——每个 type×depth cell 仅约 167 cases（500 base prompts ÷ 3 depths）。更关键的是，趋势检验（3 个数据点的单调性）统计效力天然较弱，3 点线性回归的 p-value 很难达到显著水平。这是 proposal 的核心 claim 之一，统计支撑需要更强。\n- 严重度: 可补救\n- 补救方案: (1) 增加 nesting depth 到 4-5 层（至少 4 个数据点），提升趋势检验的统计效力；(2) 在 Statistical Rigor 部分明确 depth-stratified analysis 的检验方法——建议使用 permutation-based trend test 或 Jonckheere-Terpstra test（专为有序组间趋势设计），而非简单线性回归；(3) 报告 effect size 随 depth 的置信区间图（error bar plot），即使 p-value 不够 significant，visual trend + effect size 仍有说服力。\n\n---\n\n【缺陷 3】\n- 类别: 评估方案缺陷\n- 问题: Encoded-benign FPR 评估使用 500 benign prompts × encoding augmented。但 proposal 同时声称要在 FPR = 0.5% 阈值处报告 Pareto frontier。500 个样本下，单个 false positive 对应 FPR = 0.2%，两个 = 0.4%，三个 = 0.6%——在 0.5% 阈值附近，1 个样本的差异就决定是否 \"pass\"。这使得低阈值区域的 FPR 估计不可靠（置信区间极宽），reviewer 会质疑结论的 precision。\n- 严重度: 可补救\n- 补救方案: (1) 将 encoded-benign 测试集扩大到 2,000-3,000 条（LMSYS-Chat-1M 提供充足benign数据，编码成本低），使得 0.5% 阈值对应 10-15 个样本的计数，置信区间收窄到可用范围；(2) 若扩大样本不可行，则将最低报告阈值设为 1%（而非 0.5%），并在 Pareto frontier 中注明 0.5% 区域的 CI；(3) 报告 Wilson score interval 或 Clopper-Pearson exact CI，而非仅报告点估计。\n\n---\n\n【缺陷 4】\n- 类别: ablation 不完整\n- 问题: ECS 的 Stage 1→Stage 2 切换阈值（即何时从 low-ECS 过渡到 high-ECS）是一个关键超参数，但 proposal 仅提及 \"ECS ≤ threshold → Stage 2 (ECS > threshold)\" 而未说明：(a) 阈值如何确定；(b) 对阈值的敏感性如何。Proposal 在 Acknowledged Limitations 中提到 \"ECS weight sensitivity: ±20% perturbation\" 但那是 ECS 公式权重，不是 staging threshold。如果 staging threshold 对性能影响很大，curriculum 的 claim 就弱化为\"在正确 threshold 下有效\"。\n- 严重度: 可补救\n- 补救方案: (1) 说明 threshold 的确定方法（例如 ECS 分布的 median/tercile，或 pilot run 中的 knee point）；(2) 在 supplementary 中报告 3-5 个不同 threshold 值的 ASR 结果（类似 hyperparameter sweep），展示 curriculum 优势对 threshold 选择的鲁棒性；(3) 如果想更 elegant，可以测试连续 curriculum（不做 hard staging，而是按 ECS 渐进采样）vs. discrete staging，作为 curriculum granularity 的 ablation。\n\n---\n\n【缺陷 5】\n- 类别: 实验设计不足\n- 问题: Proposal 未明确列出训练时使用的编码类型全集。Problem statement 提到 \"base64, ROT13, homoglyph substitution\" ，EncoAttack 提到 \"8 encoding types\"，但训练集到底包含哪 8 种？这直接关系到 held-out encodings 的 \"OOD\" 定义是否严格。Reviewer 会要求：(a) 知道训练/测试的 encoding split；(b) 判断 \"mapping-function OOD\" 和 \"encoding-principle OOD\" 的分类是否合理。如果训练集中恰好有某种与 held-out 非常接近的 encoding，OOD claim 被削弱。\n- 严重度: 可补救\n- 补救方案: 在 Methodology 中新增一个 \"Training Encoding Pool\" 小段，明确列出所有训练编码类型（例如：base64, ROT13, Caesar-13, hex, URL encoding, homoglyph-Cyrillic, homoglyph-math-symbols, leetspeak），并为每种注明其 \"encoding principle\" 归类。然后明确说明 held-out set 的 OOD 层级定义：mapping-function OOD = 同一 principle 下未见 mapping（如 homoglyph-Braille vs. homoglyph-Cyrillic）；encoding-principle OOD = 训练中不存在该 principle（morphological transformation, lossy encoding）。这让 reviewer 可以独立判断 OOD 严格性。\n\n---\n\n**总结**：以上 5 个缺陷均为可补救的实验设计细节问题，不涉及方向性改变。修补后（预计 1-2 小时的 proposal 修订工作），实验设计的完备性和严谨性可以达到 EMNLP 主会投稿的标准。无致命缺陷。"
}
```

---

### Runtime record

_source line 48 · 2026-05-16T12:39:23.269Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:39:23.269Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

## Round 5

10 recorded events

### User

_source line 49 · 2026-05-16T12:39:23.292Z_

【任务】: 以「角色 B：迭代中」整合第 5 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
【状态】: 有发掘空间

---

【发掘点 1】
- 维度: significance 提升 / 核心 claim 强化
- 内容: 当前 framing 将论文定位为"encoding jailbreak 的防御方法"，但论文真正回答的科学问题更大：**"结构化 curriculum 何时能诱导离散组合变换空间中的 compositional generalization？"** Encoding attacks 只是这个问题的一个 case study。建议将 primary contribution 重新定位为：对这个更一般性问题给出实证回答（positive result within structural families + negative/limited result across paradigms），safety 应用是高价值 instantiation 而非目的本身。这样论文的 audience 从 safety 社区扩展到 representation learning + compositional generalization 社区，reviewer pool 中 "觉得这只是 engineering trick" 的概率显著降低。
- 价值: 命中 Significance。EMNLP main 的 bar 要求 general insight；当前 framing 太窄（只对 encoding jailbreak 有用），会被审稿人归类为 "application paper"。拓宽后 contribution 的 ceiling 提升一个 tier。

【发掘点 2】
- 维度: novelty 锐化
- 内容: 当前 proposal 的 differential prediction（curriculum advantage 随 nesting depth 增加 → 支持 progressive decoding 而非 catastrophic interference prevention）是 novelty 最锐利的点，但它被埋在 methodology 中。建议将其提升为 **论文的核心 scientific claim**："Curriculum induces compositional decoding skill building, not merely interference prevention—evidenced by depth-dependent advantage." 这个 claim 区别于所有已有 curriculum learning 工作（它们只证明 curriculum works，不区分 WHY it works）。如果 differential prediction 得到验证，这是对 curriculum learning mechanism 的 novel empirical insight，不仅限于 encoding 场景。
- 价值: 命中 Novelty。现有 curriculum learning 文献几乎没有 mechanistic explanation 的 empirical test。这个 differential prediction 从 "我们方法好" 升级为 "我们理解了为什么好"，直接回应 "why not just random order with more epochs" 的 reviewer challenge。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: 论文未充分回应一个 trivial alternative：**如果将模型从 4B 放大到 7B/13B + flat augmentation，是否能匹配 4B + curriculum 的 OOD 性能？** 如果是，则 curriculum 的贡献退化为 "compute-efficiency trick"（降低发表价值）。论文需要明确其 claim 是 (a) curriculum 在同等模型规模下带来 fundamental generalization capability improvement（不可通过 scaling 替代），还是 (b) curriculum 是 efficiency method（同等性能用更小模型）。目前 proposal 暗示 (a) 但未排除 (b)。建议在 core thesis 中显式声明：curriculum exploits compositional structure that model scaling alone cannot discover without appropriate training signal ordering——并用 representation analysis (CKA/probing) 来区分 (curriculum 诱导出 qualitatively different representations, not just stronger versions of the same representations)。
- 价值: 命中 Novelty。如果审稿人认为 "你只是用了 curriculum 因为你 model 小，大模型不需要"，整个 novelty claim 崩塌。显式回应这个 alternative 并提供 representation-level 证据将堵住最危险的 review attack。

【发掘点 4】
- 维度: related work 差异化
- 内容: 论文与 compositional generalization 文献的连接目前停留在 surface level（"connecting to SCAN, COGS"）。但存在一个更直接相关的工作线：**meta-learning for compositional generalization**——如 Lake & Baroni (2018) 关于 systematic generalization、以及后续使用 meta-learning curriculum 来诱导 compositional skills 的工作（如 ICLR 2023 的 compositional generalization via meta-learning）。如果这些工作已经证明 structured training ordering 能帮助 compositional tasks，那本文的 novelty 需要更精确地定位：不是 "curriculum helps compositional generalization"（已知），而是 "在 adversarial robustness 的离散变换空间中，curriculum 的优势来源与 NLP compositional tasks 中的机制不同（decoding skill vs. syntactic rule generalization）"。
- 价值: 命中 Related Work 差异化。如果审稿人熟悉 compositional generalization + meta-learning 文献，缺乏对这条线的显式区分会被视为 insufficient awareness of related work，直接扣分。

【发掘点 5】
- 维度: 前提假设质疑
- 内容: 核心假设 "high-ECS regime 中 token-level content information is destroyed" 需要验证。如果 4B model 在 base64(ROT13(x)) 上确实无法从 token 层面获取任何 content signal，那它能通过 curriculum "学会 implicit decoding" 的假设依赖于一个未说明的前提：**训练数据中存在足够的中间复杂度样本来建立 decoding skill 的 gradient path**。但如果 ECS 空间中存在 "complexity cliff"（某个 nesting level 之后信息突然断崖式消失），curriculum 的 gradual 优势就不存在——模型在某个 threshold 以上无法学到任何东西，无论顺序如何。建议在 core thesis 中显式加入 **continuity assumption**: the encoding space provides a smooth difficulty gradient (no phase transition in extractable information). 并在 pilot phase 验证此假设（per-layer information retention measurement）。
- 价值: 命中 Novelty 的根基。如果这个 continuity assumption 不成立，整个 "progressive skill acquisition" 的机制故事崩塌，differential prediction 也失去诊断力。显式声明并验证此假设反而加强了论文的 scientific rigor，让审稿人无法用 "but what if the gradient isn't smooth" 来攻击。

【补救 agent 本轮输出】:
【状态】: 有缺陷待补救

---

整体评估：本 proposal 的实验设计已经接近 EMNLP 主会水准——baseline 覆盖面广且隔离变量清晰、ablation 通过对比结构自然实现、评估方案多维度覆盖、可行性大致合理。以下缺陷均为可补救的细节问题，修补后实验设计可达到主会投稿的 solid 水平。

---

【缺陷 1】
- 类别: compute 公平性问题
- 问题: DANN baseline 引入了额外的 domain discriminator 网络和 gradient reversal layer，带来额外参数和 FLOPs。Proposal 在 Compute Fairness 部分声明"All use identical Qwen2.5-4B, identical training FLOPs"，但未说明 DANN discriminator head 的额外计算如何处理。Reviewer 会质疑：如果 DANN 多花了 FLOPs 在 discriminator 上仍不如 curriculum，是 DANN 方法弱还是 compute 不公平？如果不计 discriminator FLOPs，那 DANN 实际上获得了"免费"额外参数。
- 严重度: 可补救
- 补救方案: 在 Compute Fairness 小节明确说明：(a) DANN discriminator head 参数量相对 4B classifier 可忽略（量化：discriminator 约占总参数 <0.5%），因此统一按 classifier backbone forward/backward FLOPs 计算；(b) 额外报告 DANN total FLOPs（含 discriminator）作为 transparency，让 reviewer 自行判断。一句话即可解决。

---

【缺陷 2】
- 类别: 实验设计不足
- 问题: Differential prediction（核心机制验证）将测试数据按 nesting depth 分为 3 层（depth 1, 2, 3），然后检验 (curriculum ASR − random ASR) 随 depth 的递增趋势。但 proposal 未说明每个 depth 层的测试样本量。若 EncoAttack 的 12,000 test cases 按 8 types × 3 depths 分配，每个 depth 约 4,000 cases，但这是总计——每个 type×depth cell 仅约 167 cases（500 base prompts ÷ 3 depths）。更关键的是，趋势检验（3 个数据点的单调性）统计效力天然较弱，3 点线性回归的 p-value 很难达到显著水平。这是 proposal 的核心 claim 之一，统计支撑需要更强。
- 严重度: 可补救
- 补救方案: (1) 增加 nesting depth 到 4-5 层（至少 4 个数据点），提升趋势检验的统计效力；(2) 在 Statistical Rigor 部分明确 depth-stratified analysis 的检验方法——建议使用 permutation-based trend test 或 Jonckheere-Terpstra test（专为有序组间趋势设计），而非简单线性回归；(3) 报告 effect size 随 depth 的置信区间图（error bar plot），即使 p-value 不够 significant，visual trend + effect size 仍有说服力。

---

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: Encoded-benign FPR 评估使用 500 benign prompts × encoding augmented。但 proposal 同时声称要在 FPR = 0.5% 阈值处报告 Pareto frontier。500 个样本下，单个 false positive 对应 FPR = 0.2%，两个 = 0.4%，三个 = 0.6%——在 0.5% 阈值附近，1 个样本的差异就决定是否 "pass"。这使得低阈值区域的 FPR 估计不可靠（置信区间极宽），reviewer 会质疑结论的 precision。
- 严重度: 可补救
- 补救方案: (1) 将 encoded-benign 测试集扩大到 2,000-3,000 条（LMSYS-Chat-1M 提供充足benign数据，编码成本低），使得 0.5% 阈值对应 10-15 个样本的计数，置信区间收窄到可用范围；(2) 若扩大样本不可行，则将最低报告阈值设为 1%（而非 0.5%），并在 Pareto frontier 中注明 0.5% 区域的 CI；(3) 报告 Wilson score interval 或 Clopper-Pearson exact CI，而非仅报告点估计。

---

【缺陷 4】
- 类别: ablation 不完整
- 问题: ECS 的 Stage 1→Stage 2 切换阈值（即何时从 low-ECS 过渡到 high-ECS）是一个关键超参数，但 proposal 仅提及 "ECS ≤ threshold → Stage 2 (ECS > threshold)" 而未说明：(a) 阈值如何确定；(b) 对阈值的敏感性如何。Proposal 在 Acknowledged Limitations 中提到 "ECS weight sensitivity: ±20% perturbation" 但那是 ECS 公式权重，不是 staging threshold。如果 staging threshold 对性能影响很大，curriculum 的 claim 就弱化为"在正确 threshold 下有效"。
- 严重度: 可补救
- 补救方案: (1) 说明 threshold 的确定方法（例如 ECS 分布的 median/tercile，或 pilot run 中的 knee point）；(2) 在 supplementary 中报告 3-5 个不同 threshold 值的 ASR 结果（类似 hyperparameter sweep），展示 curriculum 优势对 threshold 选择的鲁棒性；(3) 如果想更 elegant，可以测试连续 curriculum（不做 hard staging，而是按 ECS 渐进采样）vs. discrete staging，作为 curriculum granularity 的 ablation。

---

【缺陷 5】
- 类别: 实验设计不足
- 问题: Proposal 未明确列出训练时使用的编码类型全集。Problem statement 提到 "base64, ROT13, homoglyph substitution" ，EncoAttack 提到 "8 encoding types"，但训练集到底包含哪 8 种？这直接关系到 held-out encodings 的 "OOD" 定义是否严格。Reviewer 会要求：(a) 知道训练/测试的 encoding split；(b) 判断 "mapping-function OOD" 和 "encoding-principle OOD" 的分类是否合理。如果训练集中恰好有某种与 held-out 非常接近的 encoding，OOD claim 被削弱。
- 严重度: 可补救
- 补救方案: 在 Methodology 中新增一个 "Training Encoding Pool" 小段，明确列出所有训练编码类型（例如：base64, ROT13, Caesar-13, hex, URL encoding, homoglyph-Cyrillic, homoglyph-math-symbols, leetspeak），并为每种注明其 "encoding principle" 归类。然后明确说明 held-out set 的 OOD 层级定义：mapping-function OOD = 同一 principle 下未见 mapping（如 homoglyph-Braille vs. homoglyph-Cyrillic）；encoding-principle OOD = 训练中不存在该 principle（morphological transformation, lossy encoding）。这让 reviewer 可以独立判断 OOD 严格性。

---

**总结**：以上 5 个缺陷均为可补救的实验设计细节问题，不涉及方向性改变。修补后（预计 1-2 小时的 proposal 修订工作），实验设计的完备性和严谨性可以达到 EMNLP 主会投稿的标准。无致命缺陷。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd331a09-f967-431f-b1f6-269e06feee84",
  "isSidechain": false,
  "promptId": "f5a318b1-b196-48c9-8e52-7fdedb83b874",
  "type": "user",
  "uuid": "70eae6e1-4f15-40f8-8222-4505db77c231",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-16T12:40:04.240Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 5 — the hard limit. Let me analyze both agents' outputs and make a final decision.

**发掘 agent Round 5:**
Status: "有发掘空间" — still finding things, but let me assess quality.

1. **发掘点 1 (re-frame as general scientific question):** This is essentially a repeat of suggestions from Rounds 1-4 about elevating the general principle. The proposal already partially addresses this. Further pushing risks overclaiming (one domain, claiming general principle). I'll note this but NOT make another major re-framing — we've been through several iterations of this suggestion and each time I've partially adopted and cautioned against overclaiming. 

We're hitting diminishing returns now.

2. **发掘点 2 (differential prediction as core claim):** Already adopted in Round 4. The agent is suggesting elevating it further in prominence. Partially adopt — it's already in the proposal as a key mechanism test.

3. **发掘点 3 (scaling as trivial alternative):** Good point but somewhat theoretical — testing 7B/13B + flat augmentation would be ideal but adds significant compute. The representation analysis (CKA/probing) already partially addresses this: if curriculum induces qualitatively different representations (not just stronger versions), scaling alone wouldn't replicate this. I'll add a brief acknowledgment but won't add a full scaling experiment.

4. **发掘点 4 (meta-learning for compositional generalization):** Related work refinement. Partially adopt — add a sentence differentiating from meta-learning approaches.

5. **发掘点 5 (continuity assumption):** Valid concern — the progressive skill acquisition mechanism assumes no "complexity cliff." The pilot phase already partially addresses this (fast pilot run tests training dynamics). I'll make the continuity assumption explicit and add per-layer information retention measurement to the pilot.

The agent's Round 5 assessment is encouraging: while there are still flaws to address, they're explicitly framed as fixable details, and the experimental design is already approaching EMNLP main conference standards. This convergence suggests we're on solid ground.

Going through the remaining issues: the DANN discriminator overhead is negligible, so I'll just note that briefly. For the depth-stratified analysis, I need to increase nesting depths to 4+ and apply the Jonckheere-Terpstra test for better statistical power. The encoded-benign sample size needs scaling up to 2000+ for reliable low false-positive rate estimation. I should also add an explicit threshold determination method and run a 3-5 threshold sweep for the staging mechanism. The training encoding pool concern is still being addressed in the next point.

Looking at the convergence signals here, this is Round 5 and I'm seeing strong indicators that we're approaching stability. The reviewer explicitly called the experiment design "near EMNLP conference level" with only "detail issues" remaining—that's convergence language. The suggestions are increasingly repetitive refinements rather than fundamental restructuring, and the shift from major re-framings in earlier rounds to minor detail adjustments now suggests we're at the natural endpoint of this iteration cycle.

Given we've hit the hard limit at Round 5 plus these convergence signals, I'm deciding to finalize here. Running through the probability assessment with Round 5's improvements incorporated: novelty lands at medium-strong with the differential prediction mechanism and OOD scope conditions clearly differentiated from related work; significance is medium-strong given the deployment practicality and safety applications; technical soundness is strong across baselines and statistical rigor. This puts the ceiling around 43% from idea quality and floor around 32% from technical execution, settling the final estimate in the 32-42% range.

Since the median of 37% clears the 36% threshold, I'm moving forward with generating the final optimization proposal. Looking back at how the proposal evolved from the original EncoGuard framing with its co-evolutionary curriculum and flat augmentation baselines through to the final version with the formalized ECS metric, two-level OOD conditions, and differential prediction framework—I need to synthesize these into a coherent optimization plan that captures both the core insight and the refined execution strategy.

The final proposal incorporates stronger baselines including domain generalization methods and GPT-4 references, adds encoded-benign evaluation to guard against shortcut learning, uses linear probing for disentanglement verification, extends the timeline to 17 days with fallback options, and grounds everything in the broader literature on curriculum learning, domain generalization, and compositional generalization. Now I'm ready to write the Role C output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70eae6e1-4f15-40f8-8222-4505db77c231",
  "isSidechain": false,
  "requestId": "req_011Cb6GASbdSKURVhGxccAEY",
  "type": "assistant",
  "uuid": "cc053424-5b76-486f-b650-aea41db2a5c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TY7ZXXz2DUjjeydaT7B82i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13072,
      "cache_read_input_tokens": 60775,
      "output_tokens": 4503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13072,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4503,
          "cache_read_input_tokens": 60775,
          "cache_creation_input_tokens": 13072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13072
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

_source line 51 · 2026-05-16T12:41:20.538Z_

【阶段】: 迭代第 5 轮（硬上限）

**收敛判定：**
- Round 5 = 硬上限轮，系统强制收敛
- 补救 agent 明确表示"实验设计已接近 EMNLP 主会水准"，只发现细节问题 → 接近收敛
- 发掘 agent 的建议多为前几轮主题的 refinement/repetition（significance elevation 已被建议 5 轮，differential prediction 已在 Round 4 采纳），唯一新增点（continuity assumption）为小幅补丁
- 建议类型从 fundamental re-framing（Rounds 1-2）转为 detail refinement（Round 5）→ 自然收敛模式

**最终概率评估（含 Round 5 微调后）：**
- Novelty=中偏强：differential prediction 作为 mechanistic insight + OOD scope conditions（比 overpromise 更 defensible）+ 与 CAT/DG/CompGen 清晰差异化
- Significance=中偏强：deployment-practical 有数据支撑 + general principle 作为 interpretive framework + 对 adversarial robustness 社区有方法论参考价值
- Technical Soundness=强：DG baselines + encoded-benign shortcut test + linear probing + 5-seed 统计 + class balance + ECS cross-classifier validation
- Idea ceiling: ~43%
- Technical floor: ~32%

【当前概率估计】: [32% - 42%] 中位 37%

【决策】: 收敛（硬上限 + 收敛信号）

---

## 最终输出（角色 C）

【优化方案】

1. **[标题 / Core Framing]** — 从"EncoGuard: curriculum优于flat augmentation的encoding defense"重新定位为"Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training"——核心贡献是关于 curriculum 如何诱导 progressive decoding skill acquisition 并实现 OOD 泛化的 mechanistic insight，而非一个 defense method — [命中 Novelty: 从"已知原则的domain transfer"升级为"对curriculum mechanism的empirical understanding"]

2. **[Core Thesis / Mechanism Section]** — 原 proposal 的机制描述替换为精确的两阶段解释：(a) 低ECS→content anchoring（内容语义可通过tokenization获取），(b) 高ECS→progressive decoding skill acquisition（token层内容被摧毁，需隐式解码策略组合）。明确放弃"content-invariant features"这一信息论上不成立的表述 — [命中 Novelty: 避免被reviewer以"mechanism claim缺乏理论支撑"攻击]

3. **[Core Thesis]** — 新增 Differential Prediction 作为核心 falsifiable claim："curriculum advantage应随nesting depth递增"。验证 progressive decoding（组合技能构建）vs. catastrophic interference prevention（均匀保护）两个competing explanations — [命中 Novelty: 从"empirical observation that curriculum helps"升级为"mechanistic understanding with testable prediction"]

4. **[Methodology]** — 新增 Encoding Complexity Score (ECS) 形式化度量（NestingDepth + CPT_Deviation + TokenizerPerplexity），用 minimally-trained baseline 校准权重以避免循环论证，报告单因子及组合的cross-classifier Spearman ρ — [命中 Significance: 可迁移的方法论贡献]

5. **[Held-Out Encodings]** — 从笼统的"generalize to unseen types"精确化为两层 OOD：(a) Mapping-function OOD（Braille, Morse, custom cipher, NATO — 预期强泛化），(b) Encoding-principle OOD（Pig Latin, T9 keypad — 作为 scope condition/boundary test，预期有限或无优势）。明确声明 scope conditions 而非 overpromise — [命中 Novelty: 比"we generalize to everything"更有学术价值；消除reviewer "这只是interpolation"的攻击]

6. **[Related Work]** — 新增三条对比线：(a) Curriculum Adversarial Training（Cai et al. 2018 — 连续空间、仅in-distribution），(b) Domain Generalization（DANN/DRO — 可应用但我们实证更优），(c) Compositional Generalization（SCAN/COGS — 连接理论框架但本文关注adversarial transformation space）。关键论证：curriculum此处有效因为encoding space有intrinsic compositional structure with natural difficulty ordering — [命中 Related Work 差异化: 消除"just curriculum adversarial training in new domain"和"just DG applied to encodings"的dismiss风险]

7. **[Baselines]** — 从原始3个baseline扩展为10个：增加Group DRO、DANN（DG baselines）、Qwen2.5-1.5B decode→LlamaGuard-3（modern small-LM pipeline）、GPT-4 zero-shot（frontier reference）、reverse curriculum、compute-matched static variant。每个baseline有明确的comparison table说明其隔离的变量 — [命中 Technical Soundness: 堵住所有"why not X"的reviewer question]

8. **[Training Design / Class Balance]** — Benign训练数据同样做encoding augmentation（防"encoded=harmful" shortcut），训练batch 50% harmful-encoded + 50% benign（含encoded-benign）。新增encoded-benign evaluation（2000+ benign prompts × encoding，测FPR）— [命中 Technical Soundness: 防止核心claim被"classifier只检测encoding存在而非harmful content"击穿]

9. **[Representation Analysis]** — 新增linear probing实验：Probe A预测content category，Probe B预测encoding type。预期curriculum模型Probe B accuracy显著低于baselines（encoding info被discard）。配合CKA/cosine similarity共同验证disentanglement — [命中 Technical Soundness: 为机制claim提供直接表征层证据]

10. **[Statistical Design]** — Curriculum + random-order各5 seeds；H1用95% bootstrap CI + Cohen's d；differential prediction用Jonckheere-Terpstra trend test（nesting depth扩展至4-5层）；Bonferroni校正；encoded-benign样本量2000+以支撑低FPR估计 — [命中 Technical Soundness: 统计严谨性达到主会标准]

11. **[Deployment Positioning]** — 新增 inference latency/throughput/cost 正式测量，与pipeline baselines和GPT-4 API对比，支撑"deployment-practical"的 contribution claim — [命中 Significance: "deployment-practical"从hand-waving变为quantified claim]

12. **[Feasibility / Timeline]** — 从9天扩展至17天，包含pilot run验证training dynamics + ECS threshold、tokenizer审计、明确的fallback plan（co-evolutionary不通则退守static curriculum验证H1-H3）、submission-critical vs. camera-ready分离 — [命中 Feasibility: 从"几乎不可行"变为"紧张但有buffer"]

13. **[Training Encoding Pool]** — 明确列出全部训练编码类型（建议：base64, ROT13, Caesar-13, hex, URL encoding, homoglyph-Cyrillic, homoglyph-math, leetspeak）+ 每种的 encoding principle 归类 + OOD 分类依据 — [命中 Technical Soundness: 让reviewer可独立判断OOD严格性]

14. **[ECS Staging Threshold]** — 说明threshold确定方法（ECS分布median或pilot knee point）+ 3-5个threshold值的sensitivity sweep — [命中 Technical Soundness: 防"在正确threshold下才有效"的attack]

【主要风险】:
1. **Differential prediction 可能不成立**（curriculum advantage 对 nesting depth 的依赖可能不够显著）—— 如果 depth-stratified gap 是 flat 而非递增，核心 mechanism claim 弱化为 standard curriculum benefit，novelty 降一档。Mitigation：即使 differential prediction 只是 weak trend，配合 probing results 仍可部分支撑"compositional skill"narrative。
2. **DG baselines (Group DRO, DANN) 可能表现接近 curriculum** —— 如果 DANN 在 mapping-function OOD 上也能泛化，curriculum 的增量价值存疑。Mitigation：(a) curriculum 的 simplicity advantage（无需额外 discriminator 架构），(b) encoding-principle OOD 上 curriculum 可能仍有相对优势。

【实施评估】:
- **计算资源**: 4× A100 80GB GPU，约 66h wall-clock 训练 + 评估。25 个 classifier training runs（最大并行度 4），12h attacker training，4h inference analysis。云计算成本约 $800-1200（按 A100 $2/GPU-hr）+ oracle/GPT-4 API $400-500。
- **数据需求**: HarmBench + AdvBench + WildGuardTest（公开）用于 test prompts；LMSYS-Chat-1M（公开）用于 benign data；无需 proprietary 数据集。所有编码变换为 rule-based generation（无数据获取瓶颈）。
- **人工介入**: 最少。Tokenizer 审计（~2h 人工检查）；pilot study 中 ECS 权重/threshold 调参（~4h）；编码实现验证（~4h）。无需人工标注——所有 labels 来自 oracle (GPT-4o) + deterministic decoder。
- **训练需求**: 需要模型训练。Classifier: Qwen2.5-4B SFT（每 run ~8h on A100）；Attacker: Qwen2.5-1.5B GRPO（~6h/round）。非从头预训练，均为 fine-tuning。DG baselines（Group DRO, DANN）同样需要训练同规模 classifier。
- **新 Benchmark**: 需要构建 EncoAttack benchmark（12,000 test cases = 500 prompts × 8 types × 3 depths）。构建成本低（rule-based 编码生成 + oracle 验证），主要工作量在编码器实现和质量验证。外部 benchmarks 使用已有数据集的编码扰动版本。
- **预估周期**: 17 天（含 3 天 setup/pilot + 6 天核心训练 + 3 天评估分析 + 3 天写作 + 2 天 buffer）。关键路径为 Days 4-9 的并行训练。如 co-evolutionary loop 不稳定，fallback 到 static curriculum 节省 ~3 天，仍可完成 H1-H3 核心验证。整体紧张但有明确 fallback 和 buffer。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc053424-5b76-486f-b650-aea41db2a5c0",
  "isSidechain": false,
  "requestId": "req_011Cb6GASbdSKURVhGxccAEY",
  "type": "assistant",
  "uuid": "2f1e3d34-e1d2-4385-ba1b-28b04a6bd2d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TY7ZXXz2DUjjeydaT7B82i",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13072,
      "cache_read_input_tokens": 60775,
      "output_tokens": 4503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13072,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4503,
          "cache_read_input_tokens": 60775,
          "cache_creation_input_tokens": 13072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13072
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

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 5 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: significance 提升 / 核心 claim 强化 - 内容: 当前 framing 将论文定位为\"encoding jailbreak 的防…",
  "leafUuid": "2f1e3d34-e1d2-4385-ba1b-28b04a6bd2d3",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 5 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: 【状态】: 有发掘空间  ---  【发掘点 1】 - 维度: significance 提升 / 核心 claim 强化 - 内容: 当前 framing 将论文定位为\"encoding jailbreak 的防…",
  "leafUuid": "2f1e3d34-e1d2-4385-ba1b-28b04a6bd2d3",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 57 · 2026-05-16T12:41:22.338Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:41:22.338Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "content": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。"
}
```

---

### Runtime record

_source line 58 · 2026-05-16T12:41:22.339Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:41:22.339Z",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

## Round 6

5 recorded events

### User

_source line 59 · 2026-05-16T12:41:22.364Z_

【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f1e3d34-e1d2-4385-ba1b-28b04a6bd2d3",
  "isSidechain": false,
  "promptId": "06f6e0c4-46ef-46d3-9c3e-099900be4049",
  "type": "user",
  "uuid": "270d506b-36f0-41cd-9dcb-1e547d291c78",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-16T12:41:32.764Z_

<details><summary>Logged reasoning block</summary>

````text
The user is asking me to produce the final output in Role C format (pass case). I already drafted this in my previous response, but let me review and make sure it's complete and properly formatted according to the spec.

The format should be:
```
【优化方案】

1. [位置 / 章节] — [具体改动] — [命中哪个评审维度的加分]

...

【主要风险】: reviewer 最可能攻击的 1-2 点

【实施评估】:


```

I already have a comprehensive version from my Round 5 output. Let me refine it and present it cleanly as the final deliverable.

Now I'm checking the implementation assessment details — computational resources, data requirements, manual intervention needs, training requirements, new benchmarks, and estimated timeline. I need to make sure all these elements are properly filled in and formatted without code fences, starting directly with the section headers as specified.

```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "270d506b-36f0-41cd-9dcb-1e547d291c78",
  "isSidechain": false,
  "requestId": "req_011Cb6GKDS7sj4Ctv97qTwcX",
  "type": "assistant",
  "uuid": "1c5589cf-77ea-4370-9d04-249c4b7aef1f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCeAQiRMcfYi9Ev9QeXrAW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4577,
      "cache_read_input_tokens": 73847,
      "output_tokens": 4616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4616,
          "cache_read_input_tokens": 73847,
          "cache_creation_input_tokens": 4577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4577
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

_source line 61 · 2026-05-16T12:43:01.203Z_

【优化方案】

1. [标题 + 核心定位] — 从"EncoGuard: Co-evolutionary Training for Encoding Attack Defense"重新定位为"EncoGuard: Encoding-Robust Content Extraction via Complexity-Structured Curriculum Training"。核心贡献从"curriculum beats flat/random ordering"（已知 curriculum learning 结论的 domain transfer）重新 frame 为"curriculum 诱导 progressive decoding skill acquisition 并实现 OOD 泛化的 mechanistic insight"。 — [Novelty: 从"known principle applied to new domain"升级为"mechanistic understanding of why curriculum works in compositional spaces"]

2. [Core Thesis / Mechanism 章节] — 将原始"encoding-complexity curriculum优于flat augmentation"的工程 claim 替换为精确的两阶段机制描述：(a) Low-ECS regime → content anchoring（内容语义通过 tokenization 仍部分可获取，模型锚定 harmful content 的 semantic features）；(b) High-ECS regime → progressive decoding skill acquisition（token 层内容信息被多层编码摧毁，模型必须学会隐式解码策略组合）。显式放弃"content-invariant features"这一信息论上对高 ECS 编码不成立的表述。 — [Novelty: 避免 mechanism claim 被"authors don't understand their own method"击穿]

3. [Core Thesis] — 新增 Differential Prediction 作为核心 falsifiable claim：如果机制是 progressive decoding skill acquisition（组合技能构建），curriculum vs. random-order 的 ASR gap 应随 nesting depth 递增；如果仅是 catastrophic interference prevention（保护 base features），gap 应对 depth 无明显依赖。按 nesting depth (4-5 层) 分层报告 + Jonckheere-Terpstra 趋势检验。 — [Novelty: 从"empirical observation"升级为"mechanistic understanding with testable prediction"，区别于所有已有 curriculum learning 工作]

4. [Methodology 新增章节] — 引入 Encoding Complexity Score (ECS) = α·NestingDepth + β·CPT_Deviation + γ·TokenizerPerplexity。权重用 minimally-trained baseline classifier（仅 plaintext fine-tuned）校准，避免与 curriculum 训练过程的循环论证。报告单因子 Spearman ρ、leave-one-out ρ 变化、composite vs. best single component，跨 2-3 个不同 classifiers 验证。 — [Significance: ECS 本身是可迁移的方法论贡献；Technical Soundness: 去循环论证]

5. [Held-Out Encodings / OOD 设计] — 原 proposal 的笼统"generalize to unseen types"替换为两层精确 OOD 定义：(a) Mapping-function OOD（同一 encoding principle，不同具体 mapping：Braille=字符替换 cf. homoglyphs，Morse=符号编码 cf. base64，custom cipher=位移 cf. ROT13，NATO=词级替换）→ 预期 curriculum 强泛化，H2a 阈值 ≤20% ASR；(b) Encoding-principle OOD（结构上完全不同的编码范式：Pig Latin 音节重排、T9 keypad 多字符→单数字有损映射）→ 作为 scope condition/boundary test，H2b 报告相对改进而非绝对阈值。Day 1-2 tokenizer 审计确保所有 held-out 编码 survive tokenization。 — [Novelty: 展示 scope conditions 比 overpromise generalization 更有学术价值；防"这只是 interpolation"的 reviewer 攻击]

6. [Related Work 章节重构] — 从仅讨论 Broken-Token/TRYLOCK 扩展为四条对比线：(a) Curriculum Adversarial Training（Cai et al. 2018, Wang et al. 2021 — 差异：连续 perturbation space + 仅 in-distribution robustness）；(b) Domain Generalization（DANN, DRO — 差异：可应用但不利用编码组合结构，我们实证优于它们）；(c) Compositional Generalization（SCAN, COGS — 连接理论框架，本文关注 adversarial transformation space 而非 syntactic rule generalization）；(d) Meta-learning for compositionality — 区分本文 mechanism（decoding skill via difficulty ordering）vs. meta-learning 的 learn-to-learn 机制。关键论证：curriculum 此处有效因为 encoding space 有 intrinsic compositional structure with natural (non-arbitrary) difficulty ordering。 — [Related Work 差异化: 消除"just CAT in new domain" / "just DG" / "missed compositional generalization literature"三类 dismiss 风险]

7. [Design Rationale / Why Not Simpler 章节] — 新增对三类 trivial alternative 的正面回应：(a) Rule-based detection + decode pipeline → 明确 problem boundary（有效于已知单层编码，失败于 partial encoding / adversarial mixing / novel encodings without decoder）；(b) Learned canonicalization / small-LM decode pipeline → error propagation + adversarial attack surface + partial encoding ambiguity，并通过 Qwen2.5-1.5B decode→LlamaGuard-3 baseline 实证展示 nesting-depth error compounding；(c) Frontier LLM zero-shot → cost/latency impractical for deployment，通过 GPT-4 zero-shot baseline 展示 accuracy-cost tradeoff。 — [Novelty: 消除"为什么不用更简单的方法"的 reviewer 一击毙命问题]

8. [Baselines 扩展] — 从原始 3 个 baseline 扩展为 10 个 controlled/reference comparisons，并附 comparison table 明确每个 baseline 隔离的变量：Random-order（same data, shuffled → isolates ordering）、Flat augmentation（uniform encoding sampling → different data composition）、Reverse curriculum（high→low ECS → direction effect）、Static curriculum（no co-evolution → co-evolution effect）、Group DRO（worst-group loss on encoding type → standard DG）、DANN（gradient reversal on encoding type → standard DG）、Compute-matched static（co-evolution 额外 FLOPs 转为更多 training → compute fairness for H4）、Qwen-1.5B decode→LlamaGuard-3（modern pipeline）、Deterministic decode→LlamaGuard-3（rule-based pipeline）、GPT-4 zero-shot（frontier reference）。 — [Technical Soundness: 堵住所有"why not compare X"的 reviewer demand]

9. [Training Design / Class Balance] — 原 proposal 未提及 benign 数据处理。新增关键设计：benign 训练数据同样做 encoding augmentation（同分布、同 ECS 覆盖），训练 batch 50% harmful-encoded + 50% benign（含 encoded-benign），防止 classifier 学到"encoded = harmful" shortcut。新增 encoded-benign evaluation（2000+ benign prompts × encoding augmentation）验证 classifier 学到的是 content extraction 而非 encoding detection。 — [Technical Soundness: 防止核心 claim 被"classifier 只检测 encoding 存在"这一根本性质疑击穿]

10. [Representation Analysis 新增] — 新增 linear probing 实验：Probe A 预测 content category（harmful topic type）→ curriculum 应 match 或 exceed baselines；Probe B 预测 encoding type → curriculum 应显著 lower accuracy（encoding info discarded/disentangled）。配合 CKA + intra-prompt cosine similarity，三重验证 curriculum 如何重塑内部表征。 — [Technical Soundness: 为机制 claim 提供直接表征层证据，超越纯 task-level metrics]

11. [Statistical Design 加强] — Curriculum + random-order 各 5 seeds（支撑 paired statistical test）；H1 用 95% bootstrap CI + Cohen's d；differential prediction 用 Jonckheere-Terpstra trend test（nesting depth 扩展至 4-5 层提高统计效力）；Bonferroni 校正 H1-H3 family；encoded-benign 样本量 2000+ 以支撑 0.5%-1% FPR 估计 + Wilson score CI。 — [Technical Soundness: 统计严谨性达到主会标准]

12. [Deployment 定量化] — 新增 inference latency（单 A100, batch=1 和 batch=32, median + p99 ms）、throughput（queries/sec）、per-query cost（A100 租赁 vs. GPT-4 API）正式测量。 — [Significance: "deployment-practical"从 hand-waving 变为 quantified claim with formal benchmarks]

13. [Training Encoding Pool 明确化] — 新增小节明确列出全部训练编码类型（base64, ROT13, Caesar-13, hex, URL encoding, homoglyph-Cyrillic, homoglyph-math, leetspeak）+ 每种的 encoding principle 归类 + OOD 分类依据，让 reviewer 可独立验证 OOD 严格性。 — [Technical Soundness: 透明度]

14. [ECS Staging Threshold] — 说明 threshold 确定方法（pilot run 中 ECS 分布 median 或 classifier error knee point）+ 3-5 个 threshold 值的 sensitivity sweep 展示对 threshold 选择的鲁棒性。 — [Technical Soundness: 防"在特定 threshold 下才有效"的 reviewer attack]

15. [Timeline / Feasibility] — 从原始 9 天扩展至 17 天，包含：Day 1-3 pilot（tokenizer 审计 + fast pilot run + oracle pilot + ECS 校准）、Day 4-9 核心训练（并行化）、Day 10-12 评估分析、Day 13-15 写作、Day 16-17 buffer。明确 fallback：co-evolutionary 不通则 Day 7 切换 static curriculum，仍完成 H1-H3 核心验证。Submission-critical vs. camera-ready 分离（stability ablation、full ECS component retraining ablation 留 camera-ready）。 — [Feasibility: 从"几乎不可行"变为"紧张但有 buffer 和 fallback"]

16. [Continuity Assumption 显式化] — 在 Core Thesis 中声明 progressive skill acquisition 的前提条件：encoding space 提供 smooth difficulty gradient（无 complexity cliff/phase transition）。Pilot phase 中验证：测量每个 nesting layer 的 information retention rate，确认无断崖。 — [Technical Soundness: 显式声明并验证前提假设，提升 scientific rigor]

【主要风险】:

1. **Differential Prediction 可能不显著**：Curriculum vs. random-order 的 ASR gap 对 nesting depth 的依赖可能是 weak/noisy trend 而非 clean monotone increase。如果趋势不够显著，核心 mechanism claim（progressive decoding skill acquisition ≠ mere catastrophic interference prevention）弱化。**Mitigation**: 即使 trend 仅为 moderate effect size，配合 linear probing results（encoding-type probe accuracy 差异）仍可部分支撑 narrative；worst case 下论文退化为"curriculum works but mechanism not fully understood"，仍可发表但 novelty 降一档。

2. **DG Baselines（Group DRO / DANN）表现可能接近 Curriculum**：如果 DANN 在 mapping-function OOD 上也能泛化良好，curriculum 的增量价值需要从 simplicity（无需额外 discriminator architecture）和 encoding-principle OOD 的 relative advantage 来论证。**Mitigation**: (a) 如果 DG 在 encoding-principle OOD boundary test 上同样无优势 → curriculum 和 DG 在 scope conditions 内等价，curriculum 胜在 simplicity；(b) 如果 curriculum 在某些 depth 层明显优于 DG → compositional structure exploitation 的差异化成立。

【实施评估】:
- **计算资源**: 4× A100 80GB GPU（或等效：4× H100 可将训练时间减半）。约 66h wall-clock 训练（25 classifier runs × 8h each, 4-way 并行 ≈ 50h；attacker 12h；可与 classifier 部分重叠）+ 4h inference analysis + 2h latency benchmarks。云计算费用约 $800-1200（A100 $2/GPU-hr × 4 GPU × 66h）。Oracle/GPT-4 API 费用约 $400-500（18K oracle calls $250 + 15K GPT-4 eval $150 + buffer）。**总预算 ≈ $1200-1700**。
- **数据需求**: HarmBench（公开）、AdvBench（公开）、WildGuardTest（公开）用于 test prompts 和 benign data；LMSYS-Chat-1M（公开）用于 benign 训练和测试数据。所有编码变换为确定性 rule-based generation。**无 proprietary 数据依赖，无数据获取瓶颈**。
- **人工介入**: 极少。Tokenizer 审计（~2h 人工检查 + 脚本验证）；Pilot 中 ECS threshold/权重微调（~4h）；编码器实现正确性检查（~4h）；论文写作。**无需人工标注**——所有 harmful/benign labels 来自 GPT-4o oracle + deterministic decoder cross-validation。
- **训练需求**: 需要模型 fine-tuning（非从头预训练）。Classifier: Qwen2.5-4B SFT，每 run ~8h/A100。Attacker: Qwen2.5-1.5B GRPO，~6h/round × 2 rounds。DG baselines（DRO, DANN）：同架构 Qwen2.5-4B + 轻量 discriminator head，每 run ~8h。**所有训练均为 4B 规模 fine-tuning，单卡可完成，无需分布式训练**。
- **新 Benchmark**: 需构建 EncoAttack benchmark（12,000 test cases = 500 prompts × 8 types × 3 depths）。构建流程：rule-based 编码生成器（~1 天实现）+ oracle 验证攻击有效性（≥80% bypass undefended LlamaGuard-3）。Held-out encoding 实现（6 families）约 0.5 天。Encoded-benign test set（2000+ 条）用同一编码器生成。**总 benchmark 构建 ≈ 2-3 天工程量**。
- **预估周期**: **17 天**从启动到可投稿。关键路径：Days 4-9 训练（受 GPU 并行度限制）。如 co-evolutionary loop 不稳定，Day 7 切换 fallback 后仍可在 Day 15 完成 H1-H3 核心论文。Camera-ready 扩展（stability ablation, ECS retraining ablation, full 5-seed all baselines）在 acceptance 后 2-3 周完成。**考虑到 EMNLP 2026 投稿 deadline，需立即启动方可按时完成**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c5589cf-77ea-4370-9d04-249c4b7aef1f",
  "isSidechain": false,
  "requestId": "req_011Cb6GKDS7sj4Ctv97qTwcX",
  "type": "assistant",
  "uuid": "210a0a7a-67d3-483d-ba7d-2797a5ddb1ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCeAQiRMcfYi9Ev9QeXrAW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4577,
      "cache_read_input_tokens": 73847,
      "output_tokens": 4616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4616,
          "cache_read_input_tokens": 73847,
          "cache_creation_input_tokens": 4577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4577
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

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。",
  "leafUuid": "210a0a7a-67d3-483d-ba7d-2797a5ddb1ff",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Refine encoding robustness curriculum learning paper",
  "sessionId": "5d084204-84fd-419f-8108-282337c3d172"
}
```

---
