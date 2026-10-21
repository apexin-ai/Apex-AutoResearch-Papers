# Director coordination — Part 2 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination-copy-2.md) · [Structured JSON](../../../sessions/1c/1cb8ce2e50f36ac4efe4.json)

## Round 25

### Tool call

_source line 328 · 2026-05-21T14:20:57.361894+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness 和 Strength，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见：Novelty, Positioning, and Venue Fit\n\n## 1. Summary\n\n本文对 7 个 VLA 模型（450M–7B 参数）在 LIBERO 基准上的视觉 token pruning 进行了跨架构实证研究，发现 vision connector 类型（pixel-shuffle / MLP projector / linear projection）是决定 pruning 容忍度的关键因素。作者提出四类 compressibility taxonomy，用 token importance 的变异系数 (CV) 作为\"零成本\"预测指标，并提出 Vision Token Re-encoder (VTR) 在 SmolVLA 上实现 75% 压缩下 60.1% 成功率。论文实验设计系统、附录详尽，但核心因果声明证据不足，taxonomy 建立在 N=3 connector 类型上，且纯仿真评估与 CoRL venue 期望存在明显差距。\n\n## 2. Strengths\n\n**S1. 系统全面的实证研究。** 覆盖 7 个 VLA 模型、3 个 connector 家族、3 种 pruning 策略（random / importance-based / L2 norm-based）、多个 pruning ratio，每个配置 500 episodes closed-loop 评估。这种广度在 VLA efficiency 文献中少见。（Table 1, Table 2, Appendix B-E）\n\n**S2. 实用的诊断指标。** CV 可从单次 forward pass 计算、无需 closed-loop 评估即可预测 pruning 行为。Table 3 和 Figure 3b 展示了 CV 与降解模式的单调对应关系，对实际部署有指导价值。\n\n**S3. 重要的负面结果。** Linear projection 模型（π₀, π₀.5）即使 10% token removal 也导致崩溃（Table 1: π₀.5 从 baseline 44.8% 降至 r=0.9 时 ≤5%），这对社区避免无效尝试有直接价值。（Section 4.4, Table 8）\n\n**S4. 诚实的方法论处理。** 论文明确标注 CogACT 74.2% SR 来自 EfficientVLA 第三方结果而非自有评估（Section 4.1 脚注），π₀ 仅有 offline 评估也有说明。Appendix 提供了完整的 per-task breakdown（Tables 5-14）和训练超参数（Table 17）。\n\n**S5. 写作清晰，结构合理。** Related Work 覆盖了 ViT token pruning、VLM token reduction、VLA-specific works 三个层面，区分度清楚。Section 5 的 Analysis 将 empirical observations 提升到 mechanistic interpretation。\n\n## 3. Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] 核心因果声明证据不充分——connector type 与多个架构变量混淆。**\n\n论文标题声明 \"Vision Connectors and VLA Token Compressibility\"，正文多处使用因果语言：\n- Section 1: \"The vision connector, not model size or action head, determines pruning behavior\"\n- Section 5.1: \"strongly implicates the connector as the primary factor\"\n\n但实际上，三个 connector 家族的模型在 vision encoder（SigLIP vs DINOv2）、LLM backbone（Qwen2-0.5B vs Llama-2-7B）、action head（flow matching vs autoregressive vs diffusion）、训练数据和训练流程上同时不同。具体地：\n- π₀/π₀.5（linear projection）= SigLIP + flow matching\n- OpenVLA（MLP）= DINOv2 + autoregressive tokens\n- SmolVLA（pixel-shuffle）= SigLIP + Qwen2-0.5B\n\nSection 5.1 的 within-connector 比较（OpenVLA vs OFT vs CogACT vs X-VLA，均为 MLP）支持 connector 在**同一家族内**是一致因素，但无法跨家族隔离 connector 的因果效应。论文需要一个 controlled connector-swap 实验（例如在同一 backbone 上替换 connector 类型）才能支撑 \"determines\" 级别的因果声明。\n\n**N2 [critical] 四类 taxonomy 和 CV-as-predictor 实质上建立在 N=3 个数据点上。**\n\nTaxonomy 包含 4 个类别（uniformly critical / threshold-graded / smooth graded / catastrophic cliff），但只覆盖 3 种 connector 类型。Figure 3b 中 CV 与降解的\"单调关系\"本质上是 3 个簇（linear projection CV≈0.04-0.06，MLP CV≈0.15-0.22，pixel-shuffle CV≈0.55）。从 3 个点声称 predictive power 统计上很弱。\n\n此外，taxonomy 边界定义不严格。\"threshold-graded\"（OpenVLA）和\"smooth graded\"（X-VLA/OFT）的区别依赖于具体 pruning ratio 下的表现差异——Table 1 中 OpenVLA 在 r=0.5 importance-based 得 69.8%，X-VLA 得 60.4%——但没有给出区分两个类别的形式化标准。\n\n**关键缺失：** Perceiver/Q-Former 类 connector 在 related work 中被讨论（Section 2, citing Jaegle 2021, Li 2023 BLIP-2），但未被纳入实证研究。Octo 使用类似 cross-attention 机制，如果包含会增加一个 connector 家族并极大增强 taxonomy 的说服力。\n\n**N3 [critical] 纯仿真评估与 CoRL venue 要求冲突。**\n\nCoRL 2026 Call for Papers 明确要求：\"Authors should report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\" 本文全部实验在 LIBERO simulation 上进行（16 tasks, 500 episodes each），没有任何 real-robot validation，也没有提供 sim-to-real transferability 的证据。\n\n### Should-Fix\n\n**W1 [warning] \"Falsifies the 'immune' assumption\" 是稻草人论证。**\n\n**W2 [warning] VTR 的新颖性有限——本质上是 Perceiver/Q-Former 应用于 VLA token 压缩。**\n\n**W3 [warning] \"七个模型\"的 framing 有夸大成分。**\n\n**W4 [warning] \"Diagnose-then-Compress framework\" 过度包装。**\n\n**W5 [warning] 正文可能超页。**\n\n### Minor\n\nM1-M5 涉及 abstract 密度、标题用词、table 标注、因果语言强度、figure 可读性。\n\n## 4. Questions for Authors\n\nQ1-Q6 涉及 connector-swap 实验、Perceiver VLA 分类、M 值 Pareto frontier、跨 benchmark 验证、error compounding 证据、VTR 统计显著性。\n\n## 6. Overall Score: Weak Reject (borderline), Confidence: High\n\n---\n\n请对 R2 的每个 Weakness（N1-N3, W1-W5）和 Strengths（S1-S5）逐条给出 [AGREE] 或 [REBUT] 回应，引用论文具体位置作为证据。",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness 和 Strength，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 审稿意见：Novelty, Positioning, and Venue Fit\n\n## 1. Summary\n\n本文对 7 个 VLA 模型（450M–7B 参数）在 LIBERO 基准上的视觉 token pruning 进行了跨架构实证研究，发现 vision connector 类型（pixel-shuffle / MLP projector / linear projection）是决定 pruning 容忍度的关键因素。作者提出四类 compressibility taxonomy，用 token importance 的变异系数 (CV) 作为\"零成本\"预测指标，并提出 Vision Token Re-encoder (VTR) 在 SmolVLA 上实现 75% 压缩下 60.1% 成功率。论文实验设计系统、附录详尽，但核心因果声明证据不足，taxonomy 建立在 N=3 connector 类型上，且纯仿真评估与 CoRL venue 期望存在明显差距。\n\n## 2. Strengths\n\n**S1. 系统全面的实证研究。** 覆盖 7 个 VLA 模型、3 个 connector 家族、3 种 pruning 策略（random / importance-based / L2 norm-based）、多个 pruning ratio，每个配置 500 episodes closed-loop 评估。这种广度在 VLA efficiency 文献中少见。（Table 1, Table 2, Appendix B-E）\n\n**S2. 实用的诊断指标。** CV 可从单次 forward pass 计算、无需 closed-loop 评估即可预测 pruning 行为。Table 3 和 Figure 3b 展示了 CV 与降解模式的单调对应关系，对实际部署有指导价值。\n\n**S3. 重要的负面结果。** Linear projection 模型（π₀, π₀.5）即使 10% token removal 也导致崩溃（Table 1: π₀.5 从 baseline 44.8% 降至 r=0.9 时 ≤5%），这对社区避免无效尝试有直接价值。（Section 4.4, Table 8）\n\n**S4. 诚实的方法论处理。** 论文明确标注 CogACT 74.2% SR 来自 EfficientVLA 第三方结果而非自有评估（Section 4.1 脚注），π₀ 仅有 offline 评估也有说明。Appendix 提供了完整的 per-task breakdown（Tables 5-14）和训练超参数（Table 17）。\n\n**S5. 写作清晰，结构合理。** Related Work 覆盖了 ViT token pruning、VLM token reduction、VLA-specific works 三个层面，区分度清楚。Section 5 的 Analysis 将 empirical observations 提升到 mechanistic interpretation。\n\n## 3. Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1 [critical] 核心因果声明证据不充分——connector type 与多个架构变量混淆。**\n\n论文标题声明 \"Vision Connectors and VLA Token Compressibility\"，正文多处使用因果语言：\n- Section 1: \"The vision connector, not model size or action head, determines pruning behavior\"\n- Section 5.1: \"strongly implicates the connector as the primary factor\"\n\n但实际上，三个 connector 家族的模型在 vision encoder（SigLIP vs DINOv2）、LLM backbone（Qwen2-0.5B vs Llama-2-7B）、action head（flow matching vs autoregressive vs diffusion）、训练数据和训练流程上同时不同。具体地：\n- π₀/π₀.5（linear projection）= SigLIP + flow matching\n- OpenVLA（MLP）= DINOv2 + autoregressive tokens\n- SmolVLA（pixel-shuffle）= SigLIP + Qwen2-0.5B\n\nSection 5.1 的 within-connector 比较（OpenVLA vs OFT vs CogACT vs X-VLA，均为 MLP）支持 connector 在**同一家族内**是一致因素，但无法跨家族隔离 connector 的因果效应。论文需要一个 controlled connector-swap 实验（例如在同一 backbone 上替换 connector 类型）才能支撑 \"determines\" 级别的因果声明。\n\n**N2 [critical] 四类 taxonomy 和 CV-as-predictor 实质上建立在 N=3 个数据点上。**\n\nTaxonomy 包含 4 个类别（uniformly critical / threshold-graded / smooth graded / catastrophic cliff），但只覆盖 3 种 connector 类型。Figure 3b 中 CV 与降解的\"单调关系\"本质上是 3 个簇（linear projection CV≈0.04-0.06，MLP CV≈0.15-0.22，pixel-shuffle CV≈0.55）。从 3 个点声称 predictive power 统计上很弱。\n\n此外，taxonomy 边界定义不严格。\"threshold-graded\"（OpenVLA）和\"smooth graded\"（X-VLA/OFT）的区别依赖于具体 pruning ratio 下的表现差异——Table 1 中 OpenVLA 在 r=0.5 importance-based 得 69.8%，X-VLA 得 60.4%——但没有给出区分两个类别的形式化标准。\n\n**关键缺失：** Perceiver/Q-Former 类 connector 在 related work 中被讨论（Section 2, citing Jaegle 2021, Li 2023 BLIP-2），但未被纳入实证研究。Octo 使用类似 cross-attention 机制，如果包含会增加一个 connector 家族并极大增强 taxonomy 的说服力。\n\n**N3 [critical] 纯仿真评估与 CoRL venue 要求冲突。**\n\nCoRL 2026 Call for Papers 明确要求：\"Authors should report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\" 本文全部实验在 LIBERO simulation 上进行（16 tasks, 500 episodes each），没有任何 real-robot validation，也没有提供 sim-to-real transferability 的证据。\n\n### Should-Fix\n\n**W1 [warning] \"Falsifies the 'immune' assumption\" 是稻草人论证。**\n\n**W2 [warning] VTR 的新颖性有限——本质上是 Perceiver/Q-Former 应用于 VLA token 压缩。**\n\n**W3 [warning] \"七个模型\"的 framing 有夸大成分。**\n\n**W4 [warning] \"Diagnose-then-Compress framework\" 过度包装。**\n\n**W5 [warning] 正文可能超页。**\n\n### Minor\n\nM1-M5 涉及 abstract 密度、标题用词、table 标注、因果语言强度、figure 可读性。\n\n## 4. Questions for Authors\n\nQ1-Q6 涉及 connector-swap 实验、Perceiver VLA 分类、M 值 Pareto frontier、跨 benchmark 验证、error compounding 证据、VTR 统计显著性。\n\n## 6. Overall Score: Weak Reject (borderline), Confidence: High\n\n---\n\n请对 R2 的每个 Weakness（N1-N3, W1-W5）和 Strengths（S1-S5）逐条给出 [AGREE] 或 [REBUT] 回应，引用论文具体位置作为证据。",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-21T14:21:36.497963+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 39136
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-21T14:21:37.205506+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness 和 Strength，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见 — CoRL 2026\n\n## 1. Summary\n\n本文系统研究了 7 个 VLA 模型（450M–7B）跨三类 vision connector 的 token pruning 行为，在 LIBERO 仿真基准上提出四类可压缩性分类（uniformly critical, threshold-graded, smooth graded, catastrophic cliff），并声称 token importance 的 CV（变异系数）可同时预测容忍度类别和最优剪枝策略。此外提出 VTR（Vision Token Re-encoder）模块在 pixel-shuffle 架构的 catastrophic cliff 情况下恢复 60%+ 成功率。论文选题有实际价值，实验覆盖面较广，但在实验统计严谨性、CV predictor 的验证充分性、以及 controlled comparison 的 claim 强度方面存在若干需要修正的问题。\n\n## 2. Strengths\n\n**S1. 问题定义精准且有实际意义**：系统研究 VLA token pruning 在不同 connector 架构间的不对称行为，这是一个被忽视但对部署效率至关重要的问题。CoRL 社区高度相关。\n\n**S2. 跨架构覆盖面广**：7 个模型、3 类 connector、从 450M 到 7B 参数，提供了目前该领域最全面的对比。四类分类体系（Table 1）直觉清晰、实用性强。\n\n**S3. 关键实验发现有说服力**：π₀.5 在 k=0.5 处 L2 vs random 的 36pp 差距（Section 4.4）有力地推翻了 π₀ offline-only 评估带来的\"immune\"假设，是本文最有价值的发现之一。SmolVLA 的 catastrophic cliff（5% removal 即 0% SR）也很有说明力。\n\n**S4. 论文写作质量高**：结构清晰，claims 与证据的对应关系明确，limitations section 坦诚地讨论了主要局限（单一 benchmark、offline-only π₀ 评估、CV 验证不足等）。\n\n**S5. VTR 设计有控制意识**：extended training control（45.0% vs 44.8%）排除了额外训练步数的影响，MLP adapter 对照排除了 attention 机制本身的贡献，实验设计思路正确。\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**N1 [critical] SmolVLA baseline 远低于官方结果，严重影响 cliff-edge 结论的可推广性**\n- SmolVLA baseline 44.8% vs 官方 87.3%（42.5pp gap，batch size 4 vs 64）。Official checkpoint (59.2%) 也测了 cliff-edge 但仅一个配置。\n- 如果 cliff-edge 主要建立在 undertrained checkpoint 上，taxonomy 下界和 VTR 实用价值都受质疑。\n- 建议：official checkpoint 完整 pruning sweep。\n\n**N2 [critical] CV predictor 仅在 3 个模型 × 2 个 retention ratio 上验证——数据点严重不足**\n- Table 3 仅 6 个数据点，k=0.3 有 reversal。\n- 3 个模型同时在 connector、backbone、encoder fusion、token count 上不同。\n- CV 范围两端（π₀ CV=0.038, SmolVLA CV=0.314）缺 L2 vs random 对比。\n- 建议：降级 claim 或增加模型验证。\n\n**N3 [critical] π₀ 仅有 offline 评估但被归类为 \"uniformly critical\" 并用于核心 comparison**\n- Table 1 中 π₀ 与 π₀.5 并列但评估协议不同。\n- π₀–OpenVLA 的 63pp gap 实际是 offline loss vs closed-loop SR 的不可比对比。\n- 建议：明显标注 offline-only，降级 π₀ 相关 comparison 的证据强度。\n\n### Should-Fix\n\n**W1** OpenVLA L2 vs random 用不同 seed（seed42 vs seed7），k=0.5 same-seed 验证缺失。\n**W2** VTR p=0.15 不足以声称 \"re-encoding is the operative mechanism\"。\n**W3** π₀ vs OpenVLA \"most controlled comparison\" 实际有三个变量不同。\n**W4** M=96 dip（54.5±3.2%）破坏 \"flat M-curve\" 叙述。\n**W5** X-VLA 的 \"linear projection\" 分类标签与 12-layer BART encoder 不匹配。\n\n### Minor\nm1-m4 涉及 CogACT 计入 7 models、k=0.5 验证措辞、引用核查、figure 位置。\n\n## 4. Questions for Authors\nQ1: Official SmolVLA checkpoint 是否所有 k 值均 0%?\nQ2: CV=0.15 threshold 是否 post-hoc?\nQ3: VTR 在 OpenVLA 上 0% SR 对 workflow 实用性的影响?\nQ4: V-shaped L2 curve 更深入解释?\nQ5: OFT pruning 评估计划?\n\n## 7. Overall: Borderline (倾向 weak reject), Confidence: High\n\n---\n\n请对 R1 的每个 Weakness（N1-N3, W1-W5）和 Strengths（S1-S5）逐条给出 [AGREE] 或 [REBUT] 回应，引用论文具体位置作为证据。",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness 和 Strength，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 审稿意见 — CoRL 2026\n\n## 1. Summary\n\n本文系统研究了 7 个 VLA 模型（450M–7B）跨三类 vision connector 的 token pruning 行为，在 LIBERO 仿真基准上提出四类可压缩性分类（uniformly critical, threshold-graded, smooth graded, catastrophic cliff），并声称 token importance 的 CV（变异系数）可同时预测容忍度类别和最优剪枝策略。此外提出 VTR（Vision Token Re-encoder）模块在 pixel-shuffle 架构的 catastrophic cliff 情况下恢复 60%+ 成功率。论文选题有实际价值，实验覆盖面较广，但在实验统计严谨性、CV predictor 的验证充分性、以及 controlled comparison 的 claim 强度方面存在若干需要修正的问题。\n\n## 2. Strengths\n\n**S1. 问题定义精准且有实际意义**：系统研究 VLA token pruning 在不同 connector 架构间的不对称行为，这是一个被忽视但对部署效率至关重要的问题。CoRL 社区高度相关。\n\n**S2. 跨架构覆盖面广**：7 个模型、3 类 connector、从 450M 到 7B 参数，提供了目前该领域最全面的对比。四类分类体系（Table 1）直觉清晰、实用性强。\n\n**S3. 关键实验发现有说服力**：π₀.5 在 k=0.5 处 L2 vs random 的 36pp 差距（Section 4.4）有力地推翻了 π₀ offline-only 评估带来的\"immune\"假设，是本文最有价值的发现之一。SmolVLA 的 catastrophic cliff（5% removal 即 0% SR）也很有说明力。\n\n**S4. 论文写作质量高**：结构清晰，claims 与证据的对应关系明确，limitations section 坦诚地讨论了主要局限（单一 benchmark、offline-only π₀ 评估、CV 验证不足等）。\n\n**S5. VTR 设计有控制意识**：extended training control（45.0% vs 44.8%）排除了额外训练步数的影响，MLP adapter 对照排除了 attention 机制本身的贡献，实验设计思路正确。\n\n## 3. Weaknesses\n\n### Must-Fix\n\n**N1 [critical] SmolVLA baseline 远低于官方结果，严重影响 cliff-edge 结论的可推广性**\n- SmolVLA baseline 44.8% vs 官方 87.3%（42.5pp gap，batch size 4 vs 64）。Official checkpoint (59.2%) 也测了 cliff-edge 但仅一个配置。\n- 如果 cliff-edge 主要建立在 undertrained checkpoint 上，taxonomy 下界和 VTR 实用价值都受质疑。\n- 建议：official checkpoint 完整 pruning sweep。\n\n**N2 [critical] CV predictor 仅在 3 个模型 × 2 个 retention ratio 上验证——数据点严重不足**\n- Table 3 仅 6 个数据点，k=0.3 有 reversal。\n- 3 个模型同时在 connector、backbone、encoder fusion、token count 上不同。\n- CV 范围两端（π₀ CV=0.038, SmolVLA CV=0.314）缺 L2 vs random 对比。\n- 建议：降级 claim 或增加模型验证。\n\n**N3 [critical] π₀ 仅有 offline 评估但被归类为 \"uniformly critical\" 并用于核心 comparison**\n- Table 1 中 π₀ 与 π₀.5 并列但评估协议不同。\n- π₀–OpenVLA 的 63pp gap 实际是 offline loss vs closed-loop SR 的不可比对比。\n- 建议：明显标注 offline-only，降级 π₀ 相关 comparison 的证据强度。\n\n### Should-Fix\n\n**W1** OpenVLA L2 vs random 用不同 seed（seed42 vs seed7），k=0.5 same-seed 验证缺失。\n**W2** VTR p=0.15 不足以声称 \"re-encoding is the operative mechanism\"。\n**W3** π₀ vs OpenVLA \"most controlled comparison\" 实际有三个变量不同。\n**W4** M=96 dip（54.5±3.2%）破坏 \"flat M-curve\" 叙述。\n**W5** X-VLA 的 \"linear projection\" 分类标签与 12-layer BART encoder 不匹配。\n\n### Minor\nm1-m4 涉及 CogACT 计入 7 models、k=0.5 验证措辞、引用核查、figure 位置。\n\n## 4. Questions for Authors\nQ1: Official SmolVLA checkpoint 是否所有 k 值均 0%?\nQ2: CV=0.15 threshold 是否 post-hoc?\nQ3: VTR 在 OpenVLA 上 0% SR 对 workflow 实用性的影响?\nQ4: V-shaped L2 curve 更深入解释?\nQ5: OFT pruning 评估计划?\n\n## 7. Overall: Borderline (倾向 weak reject), Confidence: High\n\n---\n\n请对 R1 的每个 Weakness（N1-N3, W1-W5）和 Strengths（S1-S5）逐条给出 [AGREE] 或 [REBUT] 回应，引用论文具体位置作为证据。",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-21T14:21:38.769455+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1563
}
```

</details>

---


### Assistant

_source line 332 · 2026-05-21T14:21:44.637567+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 26

## Round 26

2 recorded events


### User

_source line 333 · 2026-05-21T14:21:47.343213+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论：Weak Reject (borderline)，Confidence: High**

三个核心问题：

1. **因果声明 under-identified**（N1）：connector type 与 encoder/backbone/action head 等多个变量混淆，缺乏 controlled connector-swap 实验，"determines" 级因果语言证据不足
2. **Taxonomy 样本量不足**（N2）：四类分类体系仅基于 3 种 connector 类型（pixel-shuffle / MLP / linear projection），Perceiver/Q-Former 类完全缺失，3 个数据点不足以支撑 "generalizable framework"
3. **CoRL venue fit 差距**（N3）：纯 LIBERO 仿真评估，CoRL 2026 明确要求 "report real-robot experiments or provide convincing evidence that simulation experiments are transferable"

次要问题包括 VTR 新颖性有限（W2, 本质是 Perceiver/Q-Former 的直接应用）、"immune" assumption 是稻草人论证（W1）、"七个模型" framing 有夸大（W3）、正文可能超页（W5）。

如果 rebuttal 能提供 connector-swap 实验或 real-robot 初步验证，评分可上调至 borderline accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 334 · 2026-05-21T14:21:52.905978+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 27

## Round 27

2 recorded events


### User

_source line 335 · 2026-05-21T14:26:09.445052+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

## Strengths 回应

**[AGREE] R1-S1: 问题定义精准且有实际意义。**
完全同意。VLA token pruning 的跨架构不对称行为是一个被忽视但部署高度相关的问题。

**[AGREE with caveat] R1-S2: 跨架构覆盖面广。**
同意覆盖面是优势，但需补充一个重要 caveat：7 个模型实际只覆盖 3 种 connector 类型（linear projection / MLP / pixel-shuffle），within-connector 模型间的行为高度一致（如 OpenVLA、OFT、CogACT 的 CV 值均在 0.21-0.22 区间），所以有效独立数据点接近 3 而非 7。R1 在 N2 中也指出了这一点。

**[REBUT] R1-S3: "π₀.5 的 36pp 差距有力推翻了 'immune' 假设"。**
R1 将此列为本文"最有价值的发现之一"，我不同意这一评价。关键问题在于：π₀ 和 π₀.5 的原始论文（Black et al. 2024, 2025）从未声称对 token pruning "immune"。论文 Section 4.4 称要 "falsify the 'immune' interpretation"，但这个 interpretation 是作者自己从 offline metrics 推导出来然后自己推翻的——这是经典的稻草人论证（我的审稿 W1 有详细论述）。

36pp offline-vs-closed-loop 差距本身是一个有价值的 empirical observation（证明 offline proxy 不可靠），但 "falsify immune assumption" 的 framing 人为放大了这个发现的 novelty。建议改为 "demonstrates that offline action-loss metrics are misleading proxies for closed-loop pruning tolerance"。

**[AGREE] R1-S4: 写作质量高。**
同意。结构清晰，claims-evidence 对应关系明确。我的审稿给 Clarity 4/5。

**[AGREE] R1-S5: VTR 控制实验设计好。**
同意。Extended training control（45.0% vs 44.8% baseline, Section 4.5/Table 2）排除了额外训练步数的混淆，MLP adapter 对照排除了参数增加本身的贡献。这体现了良好的实验设计思路。

---

## Must-Fix 回应

**[AGREE] R1-N1: SmolVLA baseline 远低于官方结果。**

完全同意这是一个核心 validity 问题。补充两个观察：

1. **VTR 的实用性直接受影响。** VTR 仅在 44.8% baseline 上训练和评估，达到 60.1% SR。但这个 60.1% 是在一个本身就严重 underperforming 的模型上获得的——实际上 VTR 的恢复效果甚至超过了 unpruned baseline（60.1% > 44.8%），这暗示 VTR 可能部分是在补偿 undertrained model 的缺陷而非真正解决 pruning 损伤。论文虽然在 official checkpoint 上也测了一个配置（Section 4.2："official SmolVLA checkpoint (59.2%) exhibits identical failure"），但 VTR 在 official checkpoint 上的恢复能力未验证。

2. **对 taxonomy 下界的影响。** "Catastrophic cliff" 类别（5% removal → 0% SR）建立在 44.8% baseline 上。如果 official checkpoint（59.2%）在某些较温和的 pruning ratio 下不会完全崩溃到 0%，cliff-edge 的 sharpness 可能被 undertrained checkpoint 放大了。R1 建议的 "official checkpoint 完整 pruning sweep" 是验证 taxonomy robustness 的 minimum requirement。

**[AGREE] R1-N2: CV predictor 数据点严重不足。**

强烈同意。这与我自己审稿的 N2 一致。补充几个 R1 未展开的具体问题：

1. **Table 3 的 reversal 问题比 R1 描述的更严重。** 在 k=0.5 时 OpenVLA 的 Δ(R−L2) 接近零或反转（Table 3, page 10），而在 k=0.7 时方向再次变化。这意味着即使在仅有的 6 个数据点中，CV 对策略选择的预测已经不稳定。

2. **极端 CV 值恰恰是最需要验证的区域。** π₀.5（CV=0.055）和 SmolVLA（CV=0.314）分别处于 CV 范围的两端，但这两个模型在 Table 3 中都没有完整的 L2 vs random closed-loop 对比——π₀.5 只有 partial data，SmolVLA 因为所有 pruning 都导致 0% SR 而无法比较策略。也就是说，CV predictor 在最需要被测试的极端值处恰好没有证据。

3. **统计层面。** 6 个数据点甚至不足以计算有意义的相关系数或进行非参数检验。"Monotonic relationship" 在 N=6 且存在 reversal 的情况下不构成统计证据。

**[AGREE] R1-N3: π₀ offline-only 评估但参与核心 comparison。**

完全同意。补充一个 internal consistency 问题：Section 5.4 ("Offline Methods Underestimate Closed-Loop") 论文自身的分析恰恰说明 offline metrics 系统性低估 pruning 伤害——π₀ 在 offline 评估中 action loss 仅增加 2.4%（Table 1, k=0.1），但论文自己论证了这类 offline 结果不可信。然而 Table 1 仍将 π₀ 的 offline 结果与其他模型的 closed-loop SR 并列展示，且 π₀ 被用于支撑 "uniformly critical" 分类和 "connector determines compressibility" 的核心论证。

更严格地说：论文声称评估了 7 个模型，但具备完整自有 closed-loop evaluation 的仅约 4-5 个（SmolVLA, OpenVLA, X-VLA, π₀.5, 可能 OFT）。π₀ 是 offline-only，CogACT 74.2% 来自 EfficientVLA。Contribution C1 "evaluating seven models" 的表述应当降级。

---

## Should-Fix 回应

**[AGREE] R1-W1: OpenVLA L2 vs random seed 不一致。**
同意。Seed42 vs seed7 引入不必要的混淆变量。虽然 seed 对 aggregate 结果的影响通常较小，但在声称 "L2 outperforms/underperforms random" 的定量对比中，same-seed 是 minimum methodological requirement。这是一个容易修复的问题，不应成为 blocker，但需要在 rebuttal 中 acknowledge 或补充实验。

**[AGREE] R1-W2: VTR p=0.15 dropout ablation 不充分。**
同意。p=0.15 是非常轻的 perturbation，不足以支撑 "re-encoding is the operative mechanism" 的声明。更有说服力的 ablation 应该是：(a) 用 mean pooling 替代 cross-attention，(b) 用 random projection 替代 learned queries，(c) 用更高 dropout（如 p=0.5）测试。

不过，MLP adapter 对照（Table 2）本身是一个更强的 evidence——MLP adapter 无法恢复性能而 cross-attention 可以，这确实暗示 attention 机制的作用。所以 "re-encoding is operative" 的 claim 有部分支撑，只是 dropout ablation 这个具体 evidence 不够强。

**[AGREE] R1-W3: π₀ vs OpenVLA "most controlled comparison" 不成立。**
强烈同意。这与我的审稿 N1（因果声明 under-identified）直接相关。Page 5 将 π₀-OpenVLA 称为 "the most controlled available comparison"，但两者在 vision encoder（SigLIP vs DINOv2）、action head（flow matching vs autoregressive）、LLM backbone（PaliGemma vs Llama-2）上同时不同。三个变量同时变化时，无法将差异归因于 connector。

论文的 within-connector comparison（OpenVLA vs OFT vs CogACT，均为 MLP + 不同 backbone/action head → 相似 CV 和降解模式）实际上是更好的 controlled evidence。建议作者将 narrative 重心从跨 connector 的 "most controlled pair" 转向 within-connector 的一致性。

**[REBUT] R1-W4: M=96 dip 破坏 "flat M-curve" 叙述。**
部分不同意。Table 2 中各 M 值的 SR：M=16 → 60.1%，M=32 → 约 60.4%，M=64 → 约 62.8%，M=96 → 54.5±3.2%，M=128 → 约 53.8%。M=96 的 dip 确实存在，但需注意：
- 54.5±3.2% 的 confidence interval 与相邻 M 值存在重叠
- M=128 也是约 53.8%，说明 M=96 和 M=128 的下降可能是一个连续趋势（过多 query vectors 引入过拟合），而非 M=96 的 anomaly
- 论文应用 "relatively stable" 替代 "flat"，但这不构成核心叙述的根本破坏

R1 指出 M=96 anomaly 是合理的审查，但将其提升为 "破坏叙述" 略过了 CI overlap 的因素。建议作者在 revision 中讨论 M 值增大时的 diminishing/negative returns 趋势。

**[AGREE] R1-W5: X-VLA 的分类标签问题。**
强烈同意。Table 1 将 X-VLA 标注为 "Linear proj†"（带 dagger footnote），但 X-VLA 实际使用 linear projection + 12-layer BART encoder（page 5 明确说明 "the effective pipeline is not purely linear"）。这个分类有两个问题：

1. **标签误导。** 即使有 footnote，将 12-layer BART encoder 归类为 "linear projection" 在 Table 1 的快速浏览中会误导读者。X-VLA 的 CV=0.151 明显高于纯 linear projection 模型（π₀ CV=0.038, π₀.5 CV=0.055），反而更接近 MLP 模型（OpenVLA CV=0.215）。

2. **暴露 taxonomy 粒度不足。** 三分类（linear / MLP / pixel-shuffle）无法容纳 BART encoder 这种 intermediate complexity 的 connector。X-VLA 的行为（threshold-graded, CV=0.151）落在 linear projection（uniformly critical, CV≈0.04-0.06）和 MLP（smooth graded, CV≈0.21-0.22）之间，暗示 connector 复杂度可能是一个连续谱而非离散类别。这直接支持了我在审稿 N2 中提出的 "taxonomy 覆盖不足" 的关注。

---

## Minor 回应

**[AGREE] m1 (CogACT 计入 7 models):** 与 N3 一致。
**[AGREE] m2 (k=0.5 验证措辞):** 合理的表述精确性要求。
**[AGREE] m3 (引用核查):** 我的引用验证显示 41 篇中 5 篇 not_found（均为近期 arXiv 预印本），6 篇 minor first-author mismatch，无虚假引用。
**[AGREE] m4 (figure 位置):** Figure 位置优化是 camera-ready 阶段的标准修改。

---

## 总结

R1 和我的审稿在核心问题上高度一致：(1) 因果声明 under-identified（R1-W3 / 我的 N1），(2) CV predictor 样本量不足（R1-N2 / 我的 N2），(3) π₀ 评估协议不一致（R1-N3 / 我的 W3）。R1 新增了一个我遗漏的重要问题——SmolVLA baseline gap（R1-N1），这直接影响 cliff-edge 结论和 VTR 实用性的可推广性。

主要分歧在两点：
- **R1-S3 (36pp gap 是最有价值发现):** 我认为 "immune falsification" 是稻草人论证，发现本身有价值但 framing 夸大了 novelty。
- **R1-W4 (M=96 dip):** 我认为 CI overlap 使这更可能是 noise 而非 systematic failure，不构成核心叙述的破坏。

综合 R1 审稿，我维持 **weak reject (borderline)** 的评分不变。R1-N1（SmolVLA baseline gap）进一步增强了我对 VTR 实用性的疑虑，但没有改变整体判断的方向。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 336 · 2026-05-21T14:26:16.464838+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 28

## Round 28

12 recorded events


### User

_source line 337 · 2026-05-21T14:26:19.123035+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

## Strengths 回应

**[AGREE] R2-S1: 系统全面的实证研究**
同意。7 个模型 × 多 k 值 × 多策略的组合在 VLA efficiency 文献中确实少见。Table 1 的 taxonomy 结构和 Appendix B-E 的 per-task breakdown（Tables 5-14）提供了高于平均水平的实验详度。

**[REBUT] R2-S3: "Linear projection 模型即使 10% removal 也导致崩溃" — R2 存在严重事实错误**

R2 原文："Linear projection 模型（π₀, π₀.5）即使 10% token removal 也导致崩溃（Table 1: π₀.5 从 baseline 44.8% 降至 r=0.9 时 ≤5%）"

这里至少有三处事实错误：
1. **π₀.5 的 baseline 是 98.2%（Section 3.1），不是 44.8%**。44.8% 是 SmolVLA 的 baseline（Section 4.2, footnote 2）。R2 混淆了两个模型。
2. **论文未测试 π₀.5 在 k=0.9 的结果**。π₀.5 的测试点为 k∈{0.3, 0.5, 0.7}（Section 3.2）。在 k=0.7（30% removal），random 仍有 77.2% SR（Table 3），远非"崩溃"。
3. **R2 引用的 "Table 8" 是 SmolVLA per-task results**（Appendix B.1），不是 π₀.5 的结果。

论文的实际发现恰恰相反：linear projection 模型在 random removal 下表现出较好的鲁棒性（π₀.5: k=0.5 random 69.4%），但在 L2 norm selection 下崩溃（33.4%）。"10% removal 即崩溃" 是 SmolVLA（pixel-shuffle）的行为（k=0.95: 0% SR, Section 4.2），不是 linear projection 模型的行为。R2 将这一发现错误归因到了错误的架构家族。

虽然 S3 的结论方向是对的（"负面结果对社区有价值"），但具体论据有误，如果基于此误读做出的后续 weakness 判断也需要重新审视。

**[AGREE] R2-S2: 实用的诊断指标**
同意 CV 的实用性前景，但需加注我在 R1-N2 中指出的数据点不足问题。

**[AGREE] R2-S4: 诚实的方法论处理**
同意。Table 1 的 †‡§‖ 标注系统和 Section 5.5 的 limitations 讨论在诚实度上高于平均水平。

**[AGREE] R2-S5: 写作清晰**
同意，但有保留——正文中某些 claim 强度与 Limitations 中的 caveats 不匹配（见下方 W3 回应）。

---

## Must-Fix (N1-N3) 回应

**[AGREE] R2-N1: 因果声明与混淆变量**

同意核心论点。我在 R1-W3 中也指出了 π₀–OpenVLA comparison 实际有三个变量同时不同（connector + backbone + encoder fusion，Section 3.2）。R2 将此系统性地扩展到整个跨 connector family 的比较，论证更完整。

补充 R2 的论证：论文中最接近因果隔离的证据是 within-family 的 OFT vs OpenVLA 比较（同一 MLP connector，CV 0.219 vs 0.215，entropy 0.667 vs 0.661，Section 4.3），但这仅证明"在 MLP 家族内，action head 不影响 token structure"，不能推广为"connector determines pruning behavior across families"。论文的 Section 5.1 也承认 "the monotonic CV-degradation relationship across all seven models...holds consistently across connector families regardless of backbone or encoder differences"——但这是 correlation，不是 causation。

R2 提出的 connector-swap 实验建议（同一 backbone 上替换 connector 类型）是正确的方向。如果不可行，至少应将 "determines" 改为 "is strongly associated with"。

**[AGREE] R2-N2: N=3 数据点支撑 taxonomy 和 CV predictor**

强烈同意，这与我的 R1-N2 一致。R2 额外指出了三个有价值的论点：

1. **3 个点实际是 3 个簇**（linear CV≈0.04-0.06, MLP CV≈0.15-0.22, pixel-shuffle CV≈0.31）：这意味着 CV 的"连续 predictor" claim 实际上等价于"按 connector 类型分类"，CV 没有提供超越 connector label 的额外预测力。这一点比我的 R1-N2 更深入。

2. **Taxonomy 边界无形式化标准**：R2 指出 "threshold-graded" 与 "smooth graded" 的区别依赖具体 k 值下的表现差异，没有给出判别公式或 CV 范围定义。我同意这是一个问题——Table 1 列出了 4 个类别名称，但读者无法用任何定量标准判断一个新模型属于哪一类。

3. **Perceiver/Q-Former 缺失**：R2 指出 Related Work（Section 2）讨论了 Perceiver (Jaegle 2021) 和 BLIP-2 (Li 2023) 等 cross-attention connector，但未将其纳入实证研究。加入 Octo 或类似模型将增加第四个 connector 家族，极大增强 taxonomy 的覆盖面。这是我未提到的有价值建议。

**[REBUT] R2-N3: "纯仿真评估与 CoRL venue 要求冲突" — 部分不同意**

R2 声称 "CoRL 2026 Call for Papers 明确要求：'Authors should report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.'" 

对此我有两点保留：

1. **引用准确性存疑**。我搜索了 CoRL 2024 official instruction for reviews（https://2024.corl.org/contributions/instruction-for-reviews）和 CoRL 2023 reviewer guidelines（https://www.corl2023.org/reviewer-guidelines），均未找到 R2 引用的这句话。CoRL 2024 的评审标准仅提及 "significance and novelty of the results, either theoretical or empirical" 和 "their potential for scientific and technological impact, as well as their relevance to robotic learning"。如果 R2 引用的是 CoRL 2026 的新要求，应提供具体出处。**作为 reviewer，我们不应基于未经验证的 venue policy 来 reject 论文。**

2. **CoRL 历史上接受过 simulation-only 的系统性研究**。LIBERO 本身就发表在 NeurIPS 2023 上，并被多篇 CoRL 论文作为主要 benchmark 使用。本文的核心贡献是**架构层面的理解**（connector → pruning behavior），这种研究需要仿真提供的精确控制来隔离变量。要求在 7 个架构 × 多 k 值 × 多策略的组合上都进行 real-robot evaluation，在计算和硬件资源上是不合理的。

3. **但 R2 的担忧有合理内核**：论文确实没有讨论 sim-to-real transferability，也没有提供任何证据表明 LIBERO 中观察到的 compressibility spectrum 在真实环境中成立。Section 5.5 的 Limitations 提到 "real-world deployment conditions (sensor noise, contact dynamics) may alter the compressibility spectrum"，但仅此一句。建议增加 1-2 段 sim-to-real 讨论，说明为什么 connector-level 的 token structure 属性（如 CV）应当在 sim 和 real 之间保持一致（因为它是 architecture 的属性，不是 task/environment 的属性）。

综上，R2-N3 不应作为 critical/must-fix，更适合降为 should-fix。

---

## Should-Fix (W1-W5) 回应

**[REBUT] R2-W1: "falsifies the 'immune' assumption" 是稻草人论证 — 部分不同意**

R2 认为论文 "falsify" 的是一个没有人提出过的 claim。但我认为：

1. **π₀ 的 offline 结果确实会引导 practitioners 做出 "immune" 判断**。Section 4.4 报告 π₀ 在 k=0.1（90% removal）下 offline loss 改善 2.4%。如果一个研究者只看到这个结果（这是公开可用的唯一数据），合理的行动就是"大胆 pruning π₀.5 或类似架构"。π₀.5 closed-loop 结果（L2 at k=0.5: 33.4% SR，−65pp）证明这种推断是危险的。

2. **但 "falsifies" 一词确实过强**。论文没有 falsify 一个被明确提出的 hypothesis，而是 demonstrate 了 offline evaluation 会产生误导性结论。更准确的表述应是 "demonstrates that the 'immune' interpretation of π₀'s offline results does not generalize to closed-loop evaluation of related architectures"。

建议：保留这一发现的核心价值（这确实是论文最有洞察力的结果之一），但将 Introduction 和 Conclusion 中的 "falsifies" 替换为更温和的措辞。

**[AGREE] R2-W2: VTR 新颖性有限**

同意。VTR 的架构（cross-attention pooling with learned queries）本质上是 Perceiver/Q-Former 的 VLA token 压缩版本。MLP adapter 在 M=32 下甚至 SR 更高（63.4% vs 60.1%，Table 2），进一步说明不是 cross-attention 机制本身的贡献。论文的贡献更多在"诊断为什么需要 re-encoding"而非 re-encoding 方法本身。

**[AGREE] R2-W3: "七个模型" framing 有夸大成分**

同意，但有轻微保留。R2 正确指出 CogACT 为文献引用（‖标注）、OFT 仅 entropy/CV 对比（§标注）、π₀ 仅 offline（†标注）。严格来说，有完整 closed-loop pruning sweep 的模型是 4 个（SmolVLA, OpenVLA, X-VLA, π₀.5）。不过 Table 1 中的标注系统确实披露了这些差异——问题在于 Abstract 和 Introduction 中 "seven VLA models" 的表述没有附带这些 caveats，对快速阅读者可能产生误导。

建议：Abstract 中改为 "six VLA models (four with closed-loop evaluation)" 或类似限定表述。

**[AGREE] R2-W4: "Diagnose-then-Compress" 过度包装**

部分同意。Conclusion（Section 6）将 "compute CV → choose method" 包装为 "Diagnose-then-Compress workflow"，但实质上只是一个 single-metric check。对于一个仅在 3 个模型上验证、存在 k=0.3 reversal 的指标来说，"workflow" 或 "framework" 的标签确实过于正式。

不过，如果 CV predictor 未来得到更充分的验证，这个 framing 本身是合理的。当前的问题是验证不足，而非 framing 概念错误。

**[AGREE] R2-W5: 正文可能超页**

经核实，这是一个实质性问题。从 PDF 渲染结果看：
- 正文（Sections 1-6）从第 1 页延续到第 13 页底部
- References 从第 14 页开始
- Appendix 从第 17 页开始

如果 CoRL 2026 限制为 8 页正文 + 无限参考文献/附录，则正文超出约 5 页。Section 5（Analysis and Discussion，共 5 个子节）占据了约 3 页，是超页的主要来源。

建议：将 Section 5 的大部分内容（5.1 Connector Determines Token Independence、5.3 Why Re-Encoding Succeeds、5.4 Offline Metrics Underestimate Closed-Loop）移入 Appendix，正文仅保留 Section 5.2（CV as Dual Predictor）的核心结论和 Section 5.5（Limitations）。这将正文压缩至接近 10 页——仍需进一步精简 Section 4 的叙述密度才能达标。

---

## 总结

| R2 观点 | R1 判断 | 理由 |
|---------|---------|------|
| S1 系统全面 | AGREE | 广度确实出色 |
| S2 实用指标 | AGREE | 但需注明验证不足 |
| S3 负面结果 | REBUT | R2 混淆了 SmolVLA (44.8%) 和 π₀.5 (98.2%) 的 baseline，错误归因了"崩溃"行为 |
| S4 诚实处理 | AGREE | 标注系统到位 |
| S5 写作清晰 | AGREE | 有保留——claim 强度不一致 |
| N1 因果混淆 | AGREE | 与 R1-W3 一致，R2 论证更系统 |
| N2 N=3 数据点 | AGREE | 与 R1-N2 高度一致；R2 的"3 簇 = connector label"论点更深入 |
| N3 纯仿真 | REBUT | R2 引用的 CoRL policy 未经验证；但 sim-to-real 讨论确实缺失，建议降为 should-fix |
| W1 稻草人 | REBUT (部分) | π₀ offline 结果确实会误导；但 "falsifies" 措辞过强 |
| W2 VTR 新颖性 | AGREE | Perceiver/Q-Former 在 VLA 的应用 |
| W3 七模型夸大 | AGREE | 4 个有完整 closed-loop sweep |
| W4 过度包装 | AGREE | 验证不足以支撑 "framework" 标签 |
| W5 超页 | AGREE | 正文约 13 页 vs 8 页限制 |

**R1 与 R2 的主要分歧**：R2-N3（sim-only 是否构成 critical issue）。我认为对于一篇以架构理解为核心贡献的工作，simulation 的控制性是必要的，real-robot 应作为 should-fix 而非 must-fix。

**R1 与 R2 的共识**：因果语言过强（N1）、CV predictor 数据点不足（N2）、部分模型评估不完整（W3）。这些与我的 R1-N2、R1-N3、R1-W3 高度一致。

**R2 未覆盖但 R1 认为重要的问题**：(1) SmolVLA baseline 42.5pp gap 对 cliff-edge 结论的影响（R1-N1）；(2) OpenVLA k=0.5 cross-seed 验证缺失（R1-W1）；(3) M=96 dip 破坏 flat M-curve 叙述（R1-W4）。这三个问题在 R2 的审稿中未被触及。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-21T14:26:52.687266+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool call

_source line 339 · 2026-05-21T14:26:52.738032+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 340 · 2026-05-21T14:26:52.788845+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T14:07:25.513646+00:00\", \"completed_at\": \"2026-05-21T14:10:58.277077+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页纯文本无任何 display item。审稿人在形成第一印象的关键窗口（前 2 分钟）内只看到文字墙。建议将 Figure 1（架构对比图）或一个核心结果 teaser figure 提前到 page 1 底部或 page 2 顶部\"}, {\"severity\": \"warning\", \"dimension\": \"page 11-13\", \"message\": \"Analysis & Discussion + Conclusion 连续 3 页纯文本。这一段是审稿人验证技术贡献的关键区域，缺少辅助理解的 figure/table 会增加认知负荷。建议将部分 appendix 中的分析性图表（如 Figure 4 attention entropy 或 Table 15 ablation）提升到正文\"}, {\"severity\": \"warning\", \"dimension\": \"page 5-6\", \"message\": \"连续 2 页纯文本（Pruning Protocol + VTR + Diagnostic Metrics）。方法描述密集但无视觉辅助。建议考虑为 pruning protocol 或 diagnostic metrics 添加示意图或伪代码\"}, {\"severity\": \"info\", \"dimension\": \"page 1-13\", \"message\": \"正文仅 2 个 figure + 3 个 table = 5 个 display items / 13 页。对于实证为主的论文偏少（通常 5-8 个 / 9 页正文）。大量实验结果（Table 4-18）被推到 appendix，正文的视觉说服力不足\"}, {\"severity\": \"info\", \"dimension\": \"page 10\", \"message\": \"Figure 2 是正文中唯一的结果可视化图。三个子图 (a)(b)(c) 承载了过多信息（pruning response curves + VTR interaction + contextual tokens scaling）。配色可区分，字号可读，但审稿人可能期望更多独立的结果图\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1 架构图清晰专业，配色区分度好，caption 自包含。但仅出现在 page 4，错过了锚定审稿人的最佳时机\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，格式规范。CV 值作为核心指标，排版清楚。最优值加粗标注正确\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Table 2 格式整洁，booktabs 风格，数值精度统一。SR 值和 std 标注完整\"}, {\"severity\": \"info\", \"dimension\": \"page 10\", \"message\": \"Table 3 格式良好，与 Figure 2 同页形成了良好的视觉节奏——这是正文中最丰富的一页\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Appendix 起始页底部约 40% 空白（Table 5 后），空间可以更紧凑\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Table 7 列数较多（6 个 retention ratio），字号偏小但仍可读。建议检查打印时的可读性\"}, {\"sever
…[truncated 243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-21T14:26:52.789401+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-21T14:27:25.923352+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-21T14:27:26.124656+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-21T14:30:09.249070+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "issues_yaml": "issues:\n  # ============================================================\n  # Round 4 (fresh) — updated from Round 4 reviewer findings\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"Scale confound: connector type 与 backbone/encoder/action head 等多变量混淆，因果声明 under-identified\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均列为 Must-Fix。核心因果 claim 的证据链不完整。\"\n      - round: 1\n        action_taken: \"全文弱化因果语言 (determined by → attributable to)；加强 §5.1 discussion；abstract 提及 limitation\"\n        status: done\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 两位 Reviewer 再次一致列为 Must-Fix。'attributable to' 仍被视为过强因果断言。\"\n      - round: 2\n        action_taken: \"将 'attributable to' 进一步降级为 'associated with' 或 'primarily shaped by'\"\n        status: open\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 3 fresh review 两位再次一致列为 critical Must-Fix。\"\n      - round: \"post-R3\"\n        note: \"5-model expansion. π0 vs OpenVLA controlled comparison. OFT vs OpenVLA action head control.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-N1 系统论证：三个 connector 家族的模型在 encoder/backbone/action head 上同时不同，无法跨家族隔离 connector 因果效应。R1-W3 同意：π₀-OpenVLA 'most controlled comparison' 实际有 3 个变量不同。交叉回应中 R1 完全 AGREE R2-N1。当前使用 'determines' 和 'strongly implicates' 仍被视为过强。R2 建议 connector-swap 实验。within-connector 比较（OFT vs OpenVLA）仅证明家族内一致性，不能推广为跨家族因果。\"\n    action_items:\n      - round: 1\n        action: \"全文弱化因果语言\"\n        assigned_to: \"paper_agent\"\n        status: done\n      - round: 2\n        action: \"将 'attributable to' 进一步降级\"\n        assigned_to: \"paper_agent\"\n        status: in_progress\n      - round: 4\n        action: \"将 'determines' 改为 'is strongly associated with'；在 Introduction 和 Results 首次提及 π₀-OpenVLA 比较时加 caveat（而非仅 Limitations）；如可行，补充 connector-swap 实验（同 backbone 不同 connector）\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"SmolVLA baseline 44.8% 远低于官方 87.3%，cliff-edge 和 VTR 结论可推广性存疑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"44.8% vs 87.3%，差异来自 batch_size=4 vs 64。\"\n      - round: 1\n        action_taken: \"下载官方 checkpoint 验证 cliff-edge → 59.2% → 0%\"\n        status: done\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 升级为 Must-Fix。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 3 两层差距——(a) 自训练 44.8% vs 官方 87.3%（b）官方 checkpoint 评估 59.2% vs 官方报告 87.3%。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-N1: 42.5pp gap 是接近一半的绝对性能。Official checkpoint (59.2%) 仅一个 VTR 配置（M=32: 53.4%），无完整 pruning sweep。R2 交叉回应追加：VTR 60.1% > baseline 44.8% 暗示 VTR 可能部分补偿 undertrained 缺陷而非解决 pruning 损伤。Cliff-edge 的 sharpness 可能被 undertrained checkpoint 放大。两位 Reviewer 一致列为 critical。\"\n    action_items:\n      - round: 1\n        action: \"下载官方 checkpoint 验证 cliff-edge\"\n        assigned_to: \"main_agent\"\n        status: done\n      - round: 4\n        action: \"在 official checkpoint (59.2%) 上完成完整 pruning sweep（至少 k∈{0.5, 0.7, 0.9, 0.95}）；更严格讨论 batch size 差异对 cliff-edge 结论边界的影响\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"CV predictor 仅 3 模型 × 2 k 值验证，数据点严重不足，k=0.3 存在 reversal\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"2 个数据点无法建立预测关系。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Section 5.5 的 >0.9 threshold 无 empirical backing。\"\n      - round: \"post-R3\"\n        note: \"4 模型 CV spectrum: π0=0.038, X-VLA=0.151, OpenVLA=0.215, SmolVLA=0.314.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-N2: Table 3 仅 6 个数据点（3 模型 × 2 k），k=0.3 reversal 直接打破 robustness。CV 范围两端（π₀ CV=0.038 和 SmolVLA CV=0.314）缺 L2 vs random 对比。R2-N2: 3 个点实际是 3 个簇 = connector label，CV 无超越 connector 标签的额外预测力。Taxonomy 边界无形式化标准。Perceiver/Q-Former 类 connector 完全缺失。交叉回应中两位完全一致。R2 补充：极端 CV 值（最需验证处）恰好无证据。6 个数据点不足以计算有意义的相关系数。\"\n    action_items:\n      - round: 4\n        action: \"将 claim 从 'CV predicts' 降级为 'CV correlates with' 或 'preliminary evidence suggests'；增加至少 1-2 个模型的 L2 vs random 对比；明确讨论 k=0.3 reversal 对实用性的实质影响；给出 taxonomy 边界的形式化标准或承认缺失\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-N4\"\n    summary: \"π₀ 仅 offline 评估但被归类为 'uniformly critical' 并用于核心 63pp comparison\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-N3: Table 1 中 π₀ 与 π₀.5 并列为 'uniformly critical'，无标注表明基于不同评估协议。π₀-OpenVLA 63pp gap 实际是 offline loss vs closed-loop SR 的不可比对比。Section 5.4 论文自身承认 offline metrics 低估 pruning 伤害，但 π₀ 仍用于核心论证。R2 交叉回应完全 AGREE：论文声称 7 模型但完整 closed-loop 仅 4-5 个。Internal consistency 问题：论文论证 offline 不可信，但用 π₀ offline 结果支撑 taxonomy。\"\n    action_items:\n      - round: 4\n        action: \"Table 1 对 π₀ 加明显标注 'offline only, closed-loop unverified'；将 π₀-OpenVLA 63pp gap 移出核心论证或明确降级证据强度；如有条件补充 π₀ closed-loop 评估\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N1\"\n    summary: \"Simulation-only 评估对 CoRL venue fit 的影响\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"CoRL 偏好 real robot。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。R1 rebut 降为 should-fix。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-N3 列为 critical：纯 LIBERO 仿真，无 real-robot validation。R1 REBUT：(a) R2 引用的 CoRL policy 未经验证——CoRL 2024 评审标准未找到该引文；(b) CoRL 历史接受 sim-only 系统性研究；(c) 要求 7 架构全做 real-robot 不合理。但 R1 同意论文缺乏 sim-to-real transferability 讨论。分歧：R2 认为 critical，R1 认为 should-fix。\"\n    action_items:\n      - round: 4\n        action: \"增加 1-2 段 sim-to-real 讨论，说明 connector-level token structure（CV）是 architecture 属性而非 task/environment 属性，应在 sim 和 real 间保持一致；如可行增加 real-robot pilot 或第二个 sim benchmark\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"VTR 方法新颖性有限，本质是 Perceiver/Q-Former 应用于 VLA token 压缩\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"需明确定位 contribution 在 empirical finding。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 列为 critical（novelty 不足）。R1 降为 should-fix。\"\n      - round: \"post-R3\"\n        note: \"Paper reframed as ANALYSIS + METHOD paper.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W2: VTR 架构（cross-attention pooling with learned queries）与 Perceiver/Q-Former 功能等价。MLP adapter SR 更高（63.4% vs 60.1%）进一步说明非 cross-attention 机制贡献。R1 AGREE：贡献在于诊断 why re-encoding 而非 re-encoding 方法本身。\"\n    action_items:\n      - round: 4\n        action: \"将 VTR 定位为 diagnostic tool 验证 re-encoding 假设，而非新颖方法贡献；明确与 Perceiver/Q-Former 的关系\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W1\"\n    summary: \"OpenVLA L2 vs random 用不同 seed（seed42 vs seed7），k=0.5 same-seed 验证缺失\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-W1: Table 3 中 OpenVLA Δ(R−L2)=−1.8pp 是 cross-seed 结果——这是 CV scaling law 最关键的 crossover point，seed variance 可能翻转符号。R2 AGREE：same-seed 是 minimum requirement。\"\n    action_items:\n      - round: 4\n        action: \"完成 k=0.5 same-seed 验证，或在 Table 3 标注 cross-seed 并讨论 seed variance 对 Δ 符号的影响\"\n        assigned_to: \"main_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"VTR p=0.15 不足以声称 re-encoding is the operative mechanism\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"M=128 passthrough 仍含 22.2M cross-attention 参数。\"\n      - round: \"post-R3\"\n        note: \"MLP adapter control done: 63.4±2.6% vs VTC 60.1±1.3%, p=0.15.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-W2: MLP adapter 实际 SR 更高（63.4% vs 60.1%），p=0.15 不显著。更准确解读是'两者无显著差异'而非'cross-attention is operative'。R2 在交叉回应中 AGREE。建议改 claim 为 'both achieve comparable recovery, benefit from learned re-encoding in general'。\"\n    action_items:\n      - round: 4\n        action: \"改 claim 为 'both architectures achieve comparable recovery, suggesting benefit from learned re-encoding in general rather than cross-attention specifically'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"MLP adapter control done: 63.4±2.6% vs VTC 60.1±1.3%, p=0.15. Both >> 0% hard pruning.\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"X-VLA 'linear projection' 分类标签与 12-layer BART encoder 不匹配\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-W5: Table 1 'Linear proj‡' 标签误导——12-layer BART encoder 引入大量 cross-token interaction。X-VLA CV=0.151 远高于纯 linear（π₀ 0.038, π₀.5 0.055），更接近 MLP（0.215）。R2 强烈 AGREE：暴露 taxonomy 粒度不足，三分类无法容纳 intermediate complexity。暗示 connector 复杂度可能是连续谱而非离散类别。\"\n    action_items:\n      - round: 4\n        action: \"在 Table 1 中为 X-VLA 标注 'Linear proj + 12-layer BART' 或创建独立分类 'linear + encoder'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"M=96 dip（54.5±3.2%）与 flat M-curve 叙述不一致\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未单独提及但作为统计不足的例证。\"\n      - round: \"post-R3\"\n        note: \"3-seed data: 54.5±3.2%. Paper positions as non-monotonic behavior.\"\n      - round: 4\n        reviewers: [1]\n        note: \"R1-W4: M=96 比 M=64 低 7.5pp，比 M=128 低 3.5pp，'flat' 描述不准确。R2 REBUT：CI overlap 使其更可能是 noise，不构成核心叙述破坏。分歧在严重性。\"\n    action_items:\n      - round: 4\n        action: \"将 'flat' 改为 'relatively stable'；讨论 M=96 dip 的可能原因\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"'七个模型' framing 有夸大成分——完整 closed-loop 仅 4 个\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W3: π₀ offline-only, CogACT 文献引用, OFT 仅 entropy/CV。有完整 closed-loop pruning sweep 的仅 SmolVLA, OpenVLA, X-VLA, π₀.5。Abstract 和 Introduction 中 'seven VLA models' 无 caveat。R1 AGREE。\"\n    action_items:\n      - round: 4\n        action: \"Abstract 改为 'seven VLA models (four with closed-loop evaluation)' 或类似限定\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W4\"\n    summary: \"'Falsifies immune assumption' 措辞过强，原始论文未做 immune claim\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W1: π₀/π₀.5 原始论文未声称 pruning immunity，'immune' 是作者自己推导后推翻——稻草人论证。R1 部分 REBUT：π₀ offline 结果确实会误导 practitioners，发现本身有价值，但 'falsifies' 过强。两位均同意措辞需降级。\"\n    action_items:\n      - round: 4\n        action: \"将 'falsifies' 替换为 'demonstrates that the immune interpretation does not generalize to closed-loop evaluation'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W5\"\n    summary: \"'Diagnose-then-Compress framework' 过度包装\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W4: 实质是 single-metric lookup table，不是 framework。R1 AGREE：验证不足以支撑 'framework' 标签，但概念方向正确。建议改为 'practical guidelines' 或 'diagnostic protocol'。\"\n    action_items:\n      - round: 4\n        action: \"将 'framework' 改为 'diagnostic protocol' 或 'practical guidelines'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W6\"\n    summary: \"正文约 13 页，超 CoRL 8 页限制约 5 页\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W5: 正文 Sections 1-6 占 13 页，References 从 page 14 开始。Section 5（Analysis）约 3 页是超页主因。R1 AGREE 并建议将 Section 5.1/5.3/5.4 移入 Appendix，仅保留 5.2（CV as Dual Predictor）和 5.5（Limitations）。仍需进一步精简。\"\n    action_items:\n      - round: 4\n        action: \"将 Section 5 大部分移入 Appendix；精简 Section 4 叙述密度；压缩至 8 页正文\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Previously resolved issues (carried forward)\n  # ============================================================\n\n  - id: \"R2-N3\"\n    summary: \"CogACT 缺 bib 条目，connector 类型未确认\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"CogACT 被用作论据但未引用。\"\n    action_items:\n      - round: 1\n        action: \"确认 CogACT MLP projector + 补 bib\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"CogACT confirmed MLP projector. Bib added via EfficientVLA.\"\n    resolution_round: 1\n\n  - id: \"F1\"\n    summary: \"figures/ 目录为空\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"所有 figure PDF 缺失。\"\n    action_items:\n      - round: 1\n        action: \"同步 figure PDF\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"5 个 PDF 全部同步，编译通过\"\n    resolution_round: 1\n\n  - id: \"F2\"\n    summary: \"无行号\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"\"\n    action_items:\n      - round: 1\n        action: \"添加 lineno\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"CoRL 官方模板 submission 模式自动启用行号\"\n    resolution_round: 1\n\n  - id: \"F3\"\n    summary: \"corl_2026.cls 是 placeholder\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"投稿前必须替换为官方模板。\"\n    action_items:\n      - round: 1\n        action: \"下载官方模板并迁移\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"CoRL 2026 官方 sty + bst 已迁移\"\n    resolution_round: 1\n\n  - id: \"DC5\"\n    summary: \"ACIS k=0.5 只有 300 episodes\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Table 1 中未说明原因。\"\n    action_items:\n      - round: 1\n        action: \"补跑 200 eps\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"已更新为 500 eps\"\n    resolution_round: 1\n\n  - id: \"R1-W6\"\n    summary: \"Cliff-edge 在 k=0.95 未被测试\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"更极端保留率更有说服力。\"\n    action_items:\n      - round: 1\n        action: \"k=0.95 eval\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"k=0.95 = 0% on both checkpoints\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Offline metric disconnect 缺具体数据\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"111.5% relative action error 仅文字提及。\"\n    action_items:\n      - round: 1\n        action: \"Appendix 增加 offline metrics table\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Appendix Table 添加 offline error analysis\"\n    resolution_round: 1\n\n  - id: \"F5\"\n    summary: \"references.bib 中 author mismatch\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"zitkovich2023rt2 等 7 条\"\n    action_items:\n      - round: 1\n        action: \"逐条核查 bib 条目\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"3 条修正，4 条验证正确\"\n    resolution_round: 1\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "issues_yaml": "issues:\n  # ============================================================\n  # Round 4 (fresh) — updated from Round 4 reviewer findings\n  # ============================================================\n\n  - id: \"R1-N1\"\n    summary: \"Scale confound: connector type 与 backbone/encoder/action head 等多变量混淆，因果声明 under-identified\"\n    category: framing\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"两位 Reviewer 均列为 Must-Fix。核心因果 claim 的证据链不完整。\"\n      - round: 1\n        action_taken: \"全文弱化因果语言 (determined by → attributable to)；加强 §5.1 discussion；abstract 提及 limitation\"\n        status: done\n      - round: 2\n        reviewers: [1, 2]\n        note: \"Round 2 两位 Reviewer 再次一致列为 Must-Fix。'attributable to' 仍被视为过强因果断言。\"\n      - round: 2\n        action_taken: \"将 'attributable to' 进一步降级为 'associated with' 或 'primarily shaped by'\"\n        status: open\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 3 fresh review 两位再次一致列为 critical Must-Fix。\"\n      - round: \"post-R3\"\n        note: \"5-model expansion. π0 vs OpenVLA controlled comparison. OFT vs OpenVLA action head control.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-N1 系统论证：三个 connector 家族的模型在 encoder/backbone/action head 上同时不同，无法跨家族隔离 connector 因果效应。R1-W3 同意：π₀-OpenVLA 'most controlled comparison' 实际有 3 个变量不同。交叉回应中 R1 完全 AGREE R2-N1。当前使用 'determines' 和 'strongly implicates' 仍被视为过强。R2 建议 connector-swap 实验。within-connector 比较（OFT vs OpenVLA）仅证明家族内一致性，不能推广为跨家族因果。\"\n    action_items:\n      - round: 1\n        action: \"全文弱化因果语言\"\n        assigned_to: \"paper_agent\"\n        status: done\n      - round: 2\n        action: \"将 'attributable to' 进一步降级\"\n        assigned_to: \"paper_agent\"\n        status: in_progress\n      - round: 4\n        action: \"将 'determines' 改为 'is strongly associated with'；在 Introduction 和 Results 首次提及 π₀-OpenVLA 比较时加 caveat（而非仅 Limitations）；如可行，补充 connector-swap 实验（同 backbone 不同 connector）\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N2\"\n    summary: \"SmolVLA baseline 44.8% 远低于官方 87.3%，cliff-edge 和 VTR 结论可推广性存疑\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"44.8% vs 87.3%，差异来自 batch_size=4 vs 64。\"\n      - round: 1\n        action_taken: \"下载官方 checkpoint 验证 cliff-edge → 59.2% → 0%\"\n        status: done\n      - round: 2\n        reviewers: [1, 2]\n        note: \"R1 升级为 Must-Fix。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Round 3 两层差距——(a) 自训练 44.8% vs 官方 87.3%（b）官方 checkpoint 评估 59.2% vs 官方报告 87.3%。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-N1: 42.5pp gap 是接近一半的绝对性能。Official checkpoint (59.2%) 仅一个 VTR 配置（M=32: 53.4%），无完整 pruning sweep。R2 交叉回应追加：VTR 60.1% > baseline 44.8% 暗示 VTR 可能部分补偿 undertrained 缺陷而非解决 pruning 损伤。Cliff-edge 的 sharpness 可能被 undertrained checkpoint 放大。两位 Reviewer 一致列为 critical。\"\n    action_items:\n      - round: 1\n        action: \"下载官方 checkpoint 验证 cliff-edge\"\n        assigned_to: \"main_agent\"\n        status: done\n      - round: 4\n        action: \"在 official checkpoint (59.2%) 上完成完整 pruning sweep（至少 k∈{0.5, 0.7, 0.9, 0.95}）；更严格讨论 batch size 差异对 cliff-edge 结论边界的影响\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R1-N3\"\n    summary: \"CV predictor 仅 3 模型 × 2 k 值验证，数据点严重不足，k=0.3 存在 reversal\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"2 个数据点无法建立预测关系。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"Section 5.5 的 >0.9 threshold 无 empirical backing。\"\n      - round: \"post-R3\"\n        note: \"4 模型 CV spectrum: π0=0.038, X-VLA=0.151, OpenVLA=0.215, SmolVLA=0.314.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-N2: Table 3 仅 6 个数据点（3 模型 × 2 k），k=0.3 reversal 直接打破 robustness。CV 范围两端（π₀ CV=0.038 和 SmolVLA CV=0.314）缺 L2 vs random 对比。R2-N2: 3 个点实际是 3 个簇 = connector label，CV 无超越 connector 标签的额外预测力。Taxonomy 边界无形式化标准。Perceiver/Q-Former 类 connector 完全缺失。交叉回应中两位完全一致。R2 补充：极端 CV 值（最需验证处）恰好无证据。6 个数据点不足以计算有意义的相关系数。\"\n    action_items:\n      - round: 4\n        action: \"将 claim 从 'CV predicts' 降级为 'CV correlates with' 或 'preliminary evidence suggests'；增加至少 1-2 个模型的 L2 vs random 对比；明确讨论 k=0.3 reversal 对实用性的实质影响；给出 taxonomy 边界的形式化标准或承认缺失\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-N4\"\n    summary: \"π₀ 仅 offline 评估但被归类为 'uniformly critical' 并用于核心 63pp comparison\"\n    category: experiment\n    severity: critical\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-N3: Table 1 中 π₀ 与 π₀.5 并列为 'uniformly critical'，无标注表明基于不同评估协议。π₀-OpenVLA 63pp gap 实际是 offline loss vs closed-loop SR 的不可比对比。Section 5.4 论文自身承认 offline metrics 低估 pruning 伤害，但 π₀ 仍用于核心论证。R2 交叉回应完全 AGREE：论文声称 7 模型但完整 closed-loop 仅 4-5 个。Internal consistency 问题：论文论证 offline 不可信，但用 π₀ offline 结果支撑 taxonomy。\"\n    action_items:\n      - round: 4\n        action: \"Table 1 对 π₀ 加明显标注 'offline only, closed-loop unverified'；将 π₀-OpenVLA 63pp gap 移出核心论证或明确降级证据强度；如有条件补充 π₀ closed-loop 评估\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-N1\"\n    summary: \"Simulation-only 评估对 CoRL venue fit 的影响\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"CoRL 偏好 real robot。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 列为 critical。R1 rebut 降为 should-fix。\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-N3 列为 critical：纯 LIBERO 仿真，无 real-robot validation。R1 REBUT：(a) R2 引用的 CoRL policy 未经验证——CoRL 2024 评审标准未找到该引文；(b) CoRL 历史接受 sim-only 系统性研究；(c) 要求 7 架构全做 real-robot 不合理。但 R1 同意论文缺乏 sim-to-real transferability 讨论。分歧：R2 认为 critical，R1 认为 should-fix。\"\n    action_items:\n      - round: 4\n        action: \"增加 1-2 段 sim-to-real 讨论，说明 connector-level token structure（CV）是 architecture 属性而非 task/environment 属性，应在 sim 和 real 间保持一致；如可行增加 real-robot pilot 或第二个 sim benchmark\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R2-W3\"\n    summary: \"VTR 方法新颖性有限，本质是 Perceiver/Q-Former 应用于 VLA token 压缩\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"需明确定位 contribution 在 empirical finding。\"\n      - round: 3\n        reviewers: [1, 2]\n        note: \"R2 列为 critical（novelty 不足）。R1 降为 should-fix。\"\n      - round: \"post-R3\"\n        note: \"Paper reframed as ANALYSIS + METHOD paper.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W2: VTR 架构（cross-attention pooling with learned queries）与 Perceiver/Q-Former 功能等价。MLP adapter SR 更高（63.4% vs 60.1%）进一步说明非 cross-attention 机制贡献。R1 AGREE：贡献在于诊断 why re-encoding 而非 re-encoding 方法本身。\"\n    action_items:\n      - round: 4\n        action: \"将 VTR 定位为 diagnostic tool 验证 re-encoding 假设，而非新颖方法贡献；明确与 Perceiver/Q-Former 的关系\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W1\"\n    summary: \"OpenVLA L2 vs random 用不同 seed（seed42 vs seed7），k=0.5 same-seed 验证缺失\"\n    category: experiment\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-W1: Table 3 中 OpenVLA Δ(R−L2)=−1.8pp 是 cross-seed 结果——这是 CV scaling law 最关键的 crossover point，seed variance 可能翻转符号。R2 AGREE：same-seed 是 minimum requirement。\"\n    action_items:\n      - round: 4\n        action: \"完成 k=0.5 same-seed 验证，或在 Table 3 标注 cross-seed 并讨论 seed variance 对 Δ 符号的影响\"\n        assigned_to: \"main_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W1\"\n    summary: \"VTR p=0.15 不足以声称 re-encoding is the operative mechanism\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: [1]\n        note: \"M=128 passthrough 仍含 22.2M cross-attention 参数。\"\n      - round: \"post-R3\"\n        note: \"MLP adapter control done: 63.4±2.6% vs VTC 60.1±1.3%, p=0.15.\"\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-W2: MLP adapter 实际 SR 更高（63.4% vs 60.1%），p=0.15 不显著。更准确解读是'两者无显著差异'而非'cross-attention is operative'。R2 在交叉回应中 AGREE。建议改 claim 为 'both achieve comparable recovery, benefit from learned re-encoding in general'。\"\n    action_items:\n      - round: 4\n        action: \"改 claim 为 'both architectures achieve comparable recovery, suggesting benefit from learned re-encoding in general rather than cross-attention specifically'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"MLP adapter control done: 63.4±2.6% vs VTC 60.1±1.3%, p=0.15. Both >> 0% hard pruning.\"\n    resolution_round: null\n\n  - id: \"R4-W2\"\n    summary: \"X-VLA 'linear projection' 分类标签与 12-layer BART encoder 不匹配\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R1-W5: Table 1 'Linear proj‡' 标签误导——12-layer BART encoder 引入大量 cross-token interaction。X-VLA CV=0.151 远高于纯 linear（π₀ 0.038, π₀.5 0.055），更接近 MLP（0.215）。R2 强烈 AGREE：暴露 taxonomy 粒度不足，三分类无法容纳 intermediate complexity。暗示 connector 复杂度可能是连续谱而非离散类别。\"\n    action_items:\n      - round: 4\n        action: \"在 Table 1 中为 X-VLA 标注 'Linear proj + 12-layer BART' 或创建独立分类 'linear + encoder'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R3-W5\"\n    summary: \"M=96 dip（54.5±3.2%）与 flat M-curve 叙述不一致\"\n    category: experiment\n    severity: warning\n    status: in_progress\n    first_raised_round: 1\n    last_seen_round: 4\n    mentions:\n      - round: 3\n        reviewers: []\n        note: \"Round 3 未单独提及但作为统计不足的例证。\"\n      - round: \"post-R3\"\n        note: \"3-seed data: 54.5±3.2%. Paper positions as non-monotonic behavior.\"\n      - round: 4\n        reviewers: [1]\n        note: \"R1-W4: M=96 比 M=64 低 7.5pp，比 M=128 低 3.5pp，'flat' 描述不准确。R2 REBUT：CI overlap 使其更可能是 noise，不构成核心叙述破坏。分歧在严重性。\"\n    action_items:\n      - round: 4\n        action: \"将 'flat' 改为 'relatively stable'；讨论 M=96 dip 的可能原因\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W3\"\n    summary: \"'七个模型' framing 有夸大成分——完整 closed-loop 仅 4 个\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W3: π₀ offline-only, CogACT 文献引用, OFT 仅 entropy/CV。有完整 closed-loop pruning sweep 的仅 SmolVLA, OpenVLA, X-VLA, π₀.5。Abstract 和 Introduction 中 'seven VLA models' 无 caveat。R1 AGREE。\"\n    action_items:\n      - round: 4\n        action: \"Abstract 改为 'seven VLA models (four with closed-loop evaluation)' 或类似限定\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W4\"\n    summary: \"'Falsifies immune assumption' 措辞过强，原始论文未做 immune claim\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W1: π₀/π₀.5 原始论文未声称 pruning immunity，'immune' 是作者自己推导后推翻——稻草人论证。R1 部分 REBUT：π₀ offline 结果确实会误导 practitioners，发现本身有价值，但 'falsifies' 过强。两位均同意措辞需降级。\"\n    action_items:\n      - round: 4\n        action: \"将 'falsifies' 替换为 'demonstrates that the immune interpretation does not generalize to closed-loop evaluation'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W5\"\n    summary: \"'Diagnose-then-Compress framework' 过度包装\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W4: 实质是 single-metric lookup table，不是 framework。R1 AGREE：验证不足以支撑 'framework' 标签，但概念方向正确。建议改为 'practical guidelines' 或 'diagnostic protocol'。\"\n    action_items:\n      - round: 4\n        action: \"将 'framework' 改为 'diagnostic protocol' 或 'practical guidelines'\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R4-W6\"\n    summary: \"正文约 13 页，超 CoRL 8 页限制约 5 页\"\n    category: format\n    severity: warning\n    status: open\n    first_raised_round: 4\n    last_seen_round: 4\n    mentions:\n      - round: 4\n        reviewers: [1, 2]\n        note: \"R2-W5: 正文 Sections 1-6 占 13 页，References 从 page 14 开始。Section 5（Analysis）约 3 页是超页主因。R1 AGREE 并建议将 Section 5.1/5.3/5.4 移入 Appendix，仅保留 5.2（CV as Dual Predictor）和 5.5（Limitations）。仍需进一步精简。\"\n    action_items:\n      - round: 4\n        action: \"将 Section 5 大部分移入 Appendix；精简 Section 4 叙述密度；压缩至 8 页正文\"\n        assigned_to: \"paper_agent\"\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # ============================================================\n  # Previously resolved issues (carried forward)\n  # ============================================================\n\n  - id: \"R2-N3\"\n    summary: \"CogACT 缺 bib 条目，connector 类型未确认\"\n    category: writing\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"CogACT 被用作论据但未引用。\"\n    action_items:\n      - round: 1\n        action: \"确认 CogACT MLP projector + 补 bib\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"CogACT confirmed MLP projector. Bib added via EfficientVLA.\"\n    resolution_round: 1\n\n  - id: \"F1\"\n    summary: \"figures/ 目录为空\"\n    category: format\n    severity: critical\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"所有 figure PDF 缺失。\"\n    action_items:\n      - round: 1\n        action: \"同步 figure PDF\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"5 个 PDF 全部同步，编译通过\"\n    resolution_round: 1\n\n  - id: \"F2\"\n    summary: \"无行号\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"\"\n    action_items:\n      - round: 1\n        action: \"添加 lineno\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"CoRL 官方模板 submission 模式自动启用行号\"\n    resolution_round: 1\n\n  - id: \"F3\"\n    summary: \"corl_2026.cls 是 placeholder\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [2]\n        note: \"投稿前必须替换为官方模板。\"\n    action_items:\n      - round: 1\n        action: \"下载官方模板并迁移\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"CoRL 2026 官方 sty + bst 已迁移\"\n    resolution_round: 1\n\n  - id: \"DC5\"\n    summary: \"ACIS k=0.5 只有 300 episodes\"\n    category: experiment\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"Table 1 中未说明原因。\"\n    action_items:\n      - round: 1\n        action: \"补跑 200 eps\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"已更新为 500 eps\"\n    resolution_round: 1\n\n  - id: \"R1-W6\"\n    summary: \"Cliff-edge 在 k=0.95 未被测试\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"更极端保留率更有说服力。\"\n    action_items:\n      - round: 1\n        action: \"k=0.95 eval\"\n        assigned_to: \"main_agent\"\n        status: done\n    resolution: \"k=0.95 = 0% on both checkpoints\"\n    resolution_round: 1\n\n  - id: \"R1-W5\"\n    summary: \"Offline metric disconnect 缺具体数据\"\n    category: experiment\n    severity: warning\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 2\n    mentions:\n      - round: 1\n        reviewers: [1]\n        note: \"111.5% relative action error 仅文字提及。\"\n    action_items:\n      - round: 1\n        action: \"Appendix 增加 offline metrics table\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"Appendix Table 添加 offline error analysis\"\n    resolution_round: 1\n\n  - id: \"F5\"\n    summary: \"references.bib 中 author mismatch\"\n    category: format\n    severity: info\n    status: resolved\n    first_raised_round: 1\n    last_seen_round: 1\n    mentions:\n      - round: 1\n        reviewers: [1, 2]\n        note: \"zitkovich2023rt2 等 7 条\"\n    action_items:\n      - round: 1\n        action: \"逐条核查 bib 条目\"\n        assigned_to: \"paper_agent\"\n        status: done\n    resolution: \"3 条修正，4 条验证正确\"\n    resolution_round: 1\n"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-21T14:30:09.350255+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml\", \"bytes\": 17213}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-21T14:32:28.981443+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: \"Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility\"\n**Venue**: CoRL 2026 | **Deadline**: 2026-05-29\n**Reviewers**: R1（实验严谨性 + 方法技术）, R2（新颖性 + 定位 + venue fit）\n**审稿模式**: Fresh（独立初审）\n\n---\n\n## Summary\n\n本文系统研究了 7 个 VLA 模型（450M–7B）跨三类 vision connector（linear projection / MLP projector / pixel-shuffle）的 token pruning 行为，在 LIBERO 仿真基准上提出四类可压缩性分类（uniformly critical / threshold-graded / smooth graded / catastrophic cliff），用 token importance CV 作为零成本预测指标，并提出 VTR（Vision Token Re-encoder）在 pixel-shuffle 架构的 catastrophic cliff 下恢复 60%+ 成功率。论文选题精准、实验覆盖广、写作质量高，但核心因果声明证据不足、CV predictor 验证数据点过少、SmolVLA baseline 差距大，且正文超出 CoRL 8 页限制。\n\n---\n\n## Strengths\n\n- **S1 [共识]** 问题定义精准且有实际意义。VLA token pruning 的跨架构不对称行为是被忽视但部署高度相关的问题。CoRL 社区直接相关。\n\n- **S2 [共识]** 跨架构覆盖面在 VLA efficiency 文献中少见：7 个模型、3 类 connector、多 pruning 策略和 ratio、每配置 500 episodes closed-loop 评估。Table 1 taxonomy 直觉清晰。\n\n- **S3 [共识]** π₀.5 在 k=0.5 处 L2 vs random 的 36pp 差距是本文最有价值的实验发现，证明 offline proxy 不可靠且低 CV 模型存在方法依赖性。SmolVLA 的 catastrophic cliff（5% removal → 0% SR）同样有说明力。\n\n- **S4 [共识]** VTR 实验设计有控制意识：extended training control（45.0% vs 44.8%）排除额外训练步数，MLP adapter 对照排除特定架构贡献。\n\n- **S5 [共识]** 写作清晰，结构合理，Table 1 标注系统（†‡§‖）和 Limitations section 诚实度高于平均水平。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-C1 [critical, 共识] 因果声明 under-identified——connector type 与多个架构变量混淆**\n\n论文使用 \"determines\"、\"strongly implicates\" 等因果语言（Section 1, 5.1），但三个 connector 家族的模型同时在 vision encoder、LLM backbone、action head、训练流程上不同。π₀–OpenVLA 被称为 \"most controlled comparison\"（Section 3.2），实际有 connector + backbone + encoder fusion 三变量不同。Within-connector 比较（OFT vs OpenVLA）仅证明家族内一致性，无法推广为跨家族因果。缺乏 controlled connector-swap 实验（同 backbone 不同 connector）。\n\n- R1: AGREE (W3) — \"correlation, not causation\"\n- R2: critical N1 — 核心 contribution 的因果基础不成立\n- 交叉回应：R1 完全 AGREE R2-N1，认为 R2 论证更系统\n\n**W-C2 [critical, 共识] SmolVLA baseline 44.8% 远低于官方 87.3%，cliff-edge 和 VTR 可推广性存疑**\n\n42.5pp gap（batch size 4 vs 64）。Official checkpoint (59.2%) 仅验证了一个 VTR 配置（M=32: 53.4%），无完整 pruning sweep。VTR 的 60.1% > baseline 44.8% 可能部分补偿 undertrained 缺陷。Cliff-edge 的 sharpness 可能被 undertrained checkpoint 放大。\n\n- R1: critical N1\n- R2: 交叉回应中 AGREE 并追加两个观察\n- 共识：official checkpoint 完整 pruning sweep 是 minimum requirement\n\n**W-C3 [critical, 共识] CV predictor 仅 3 模型 × 2 k 值 = 6 数据点，k=0.3 存在 reversal**\n\nTable 3 的 CV scaling law 统计上远未达到可靠结论。3 个数据点实际是 3 个簇（与 connector 标签等价），CV 无超越 connector label 的额外预测力。CV 范围两端（π₀, SmolVLA）缺 L2 vs random 对比。Taxonomy 边界无形式化标准。Perceiver/Q-Former 类 connector 完全缺失。\n\n- R1: critical N2\n- R2: critical N2 — 补充\"3 簇 = connector label\"论点\n- 交叉回应：双方强烈一致\n\n**W-C4 [critical, 共识] π₀ 仅 offline 评估但用于核心论证**\n\nTable 1 中 π₀ 与 π₀.5 并列为 \"uniformly critical\"，无标注区分评估协议。π₀–OpenVLA 63pp gap 是 offline loss vs closed-loop SR 的不可比对比。论文自身论证 offline metrics 不可信（Section 5.4），但 π₀ 仍用于核心 taxonomy 和 \"connector determines\" 论证。有完整 closed-loop pruning sweep 的仅 4 个模型（SmolVLA, OpenVLA, X-VLA, π₀.5），\"seven models\" 表述有夸大。\n\n- R1: critical N3\n- R2: 交叉回应 AGREE — internal consistency 问题\n\n### Should-Fix（影响评分但不一票否决）\n\n**W-S1 [warning, 共识] X-VLA \"linear projection\" 分类标签与 12-layer BART encoder 不匹配**\nTable 1 标签误导。X-VLA CV=0.151 远高于纯 linear（0.038-0.055），更接近 MLP（0.215）。暴露三分类粒度不足，暗示 connector 复杂度是连续谱。（R1-W5, R2 强烈 AGREE）\n\n**W-S2 [warning, 共识] OpenVLA L2 vs random 用不同 seed，k=0.5 same-seed 验证缺失**\nTable 3 中 OpenVLA Δ(R−L2)=−1.8pp 是 CV scaling law 最关键的 crossover point，seed variance 可能翻转符号。（R1-W1, R2 AGREE）\n\n**W-S3 [warning, 共识] VTR 新颖性有限——Perceiver/Q-Former 的 VLA 应用**\nVTR 架构与 Perceiver/Q-Former 功能等价。MLP adapter SR 更高（63.4% vs 60.1%）。贡献在于诊断 why re-encoding 而非方法本身。（R2-W2, R1 AGREE）\n\n**W-S4 [warning, 共识] VTR p=0.15 不足以声称 \"re-encoding is the operative mechanism\"**\nMLP adapter 实际 SR 更高。更准确解读是\"两者无显著差异，benefit from learned re-encoding in general\"。（R1-W2, R2 AGREE）\n\n**W-S5 [warning, 共识] \"Diagnose-then-Compress framework\" 过度包装**\n实质是 single-metric lookup table。验证不足以支撑 \"framework\" 标签。（R2-W4, R1 AGREE）\n\n**W-S6 [warning, 共识] 正文约 13 页，超 CoRL 8 页限制约 5 页**\nSection 5（Analysis）约 3 页是超页主因。需大幅压缩或移入 Appendix。（R2-W5, R1 AGREE）\n\n**W-S7 [warning, 共识] \"Falsifies immune assumption\" 措辞过强**\nπ₀/π₀.5 原始论文未声称 pruning immunity。发现本身有价值但 \"falsifies\" 构成稻草人论证。（R2-W1, R1 部分 AGREE — 同意措辞需降级）\n\n**W-S8 [warning] M=96 dip（54.5±3.2%）与 \"flat M-curve\" 叙述不完全一致**\nR1 认为破坏叙述，R2 认为 CI overlap 可能是 noise。建议改 \"flat\" 为 \"relatively stable\"。（R1-W4, R2 部分 REBUT）\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成完全一致 [AGREE]：\n\n1. **因果声明证据不足**（W-C1）：\"determines\" 需降级为 \"is strongly associated with\"，缺乏 controlled connector-swap 实验\n2. **CV predictor 验证严重不足**（W-C3）：3 个数据点 = 3 个 connector 簇，无超越标签的额外预测力\n3. **π₀ offline-only 问题**（W-C4）：不应与 closed-loop 结果并列用于核心论证\n4. **SmolVLA baseline gap**（W-C2）：official checkpoint 完整 pruning sweep 是 minimum requirement\n5. **VTR 新颖性定位**（W-S3）：贡献在诊断 why re-encoding，非方法本身\n6. **正文超页**（W-S6）：约 13 页 vs 8 页限制，需大幅压缩\n7. **\"七模型\" framing 夸大**（W-C4）：完整 closed-loop 仅 4 个\n\n---\n\n## Reviewer Divergence\n\n**分歧 1：Simulation-only 评估的严重性**\n- R2：列为 critical（N3），引用 CoRL 2026 CFP 要求 real-robot 或 sim-to-real evidence\n- R1：REBUT — R2 引用的 CoRL policy 在公开文档中未找到；CoRL 历史接受 sim-only 分析论文；7 架构全做 real-robot 不合理。但同意缺乏 sim-to-real 讨论\n- **Director 判断**：降为 should-fix。论文核心贡献是架构级理解，simulation 的控制性是必要条件。但需增加 sim-to-real 讨论，说明 CV 是 architecture 属性而非 environment 属性\n\n**分歧 2：M=96 dip 是否破坏 flat M-curve 叙述**\n- R1：W4，认为 7.5pp 差异不可忽略\n- R2：REBUT — CI overlap，更可能是 noise\n- **Director 判断**：将 \"flat\" 改为 \"relatively stable\" 是充分的修复\n\n---\n\n## Questions for Authors\n\n1. SmolVLA official checkpoint (59.2%) 是否在所有 k 值下均 0% SR？（R1-Q1）\n2. CV=0.15 threshold 是 post-hoc 选择还是有先验依据？（R1-Q2）\n3. VTR 在 OpenVLA 上 0% SR（含 passthrough M=128）的机制是什么？对 workflow 实用性的影响？（R1-Q3）\n4. 是否考虑过 controlled connector-swap 实验（同 backbone 不同 connector）？（R2-Q1）\n5. Perceiver-based VLA（如 Octo）会落入 taxonomy 哪个类别？（R2-Q2）\n6. VTR 60.1% vs baseline 59.2% 的统计显著性？（R2-Q6）\n7. π₀.5 V-shaped L2 curve 的 spatial clustering 假设是否有 attention map 或 token position 分析验证？（R1-Q4）\n\n---\n\n## Missing References\n\n- \"Don't Run with Scissors\" (Jabbour et al.)：已引用但对比讨论不充分——该工作也研究 VLA pruning failure and recovery，Related Work 应增加对比\n- FastV (Chen et al., 2024)：VLM token pruning 重要 baseline，仅 Related Work 提及一次，建议增加在 VLA 上的适用性讨论\n- 引用验证结果：41 篇中 30 篇 verified，5 篇 not_found（近期 arXiv 预印本，OpenAlex 未收录），6 篇 minor first-author mismatch，**无虚假引用**\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2026-05-21 14:07 → 14:10）\n\n主要发现（3 warning, 9 info）：\n- **[warning]** 前 3 页（pp.1-3）纯文本无任何 display item，审稿人第一印象窗口内只看到文字墙。Figure 1 应提前到 page 1-2\n- **[warning]** pp.11-13（Analysis + Conclusion）连续 3 页纯文本，缺辅助 figure/table\n- **[warning]** pp.5-6 方法描述密集无视觉辅助（Pruning Protocol + VTR + Diagnostic Metrics）\n- **[info]** 正文仅 2 figure + 3 table = 5 display items / 13 页，对实证论文偏少。大量实验结果被推到 appendix\n- **[info]** Figure 4（attention entropy）仅在 appendix，未被正文利用\n- **[info]** Figure 1 架构图清晰但出现在 page 4，错过锚定时机\n\n注：正文超页（~13 页）是排版问题的根本原因。压缩至 8 页后 display item 密度将大幅改善。\n\n---\n\n## Overall Assessment\n\n### 评分：Weak Reject\n\n### 置信度：High\n\n### 理由\n\n论文选择了一个重要且及时的问题（VLA 架构对 token pruning 的不对称响应），实验执行扎实（多模型、多策略、closed-loop、500 episodes），写作质量在平均水平之上。π₀.5 的 L2 vs random 36pp 差距、SmolVLA 的 catastrophic cliff 发现、以及 offline-vs-closed-loop disconnect 的展示都有实际价值。\n\n但四个结构性问题制约了 contributions 的可靠性：\n\n1. **因果声明缺乏实验基础**（W-C1）：三个 connector 家族的模型在 encoder/backbone/action head 上同时不同，\"determines\" 级因果语言无法成立。这直接影响 Contribution 1 的核心 claim。\n\n2. **CV predictor 验证严重不足**（W-C3）：3 个模型的 CV 值与 3 个 connector 标签一一对应，CV 实际未提供超越 connector 分类的额外预测力。k=0.3 reversal 进一步削弱了 \"dual predictor\" 的稳健性。这直接影响 Contribution 2。\n\n3. **SmolVLA baseline 42.5pp gap**（W-C2）：cliff-edge 和 VTR 结论建立在严重 undertrained 的 checkpoint 上，official checkpoint 仅验证了一个配置。这直接影响 Contribution 3。\n\n4. **π₀ offline-only 用于核心论证**（W-C4）：论文自身论证 offline 不可靠，但 π₀ 的 offline 结果仍用于支撑 taxonomy 分类和跨架构 comparison。\n\n### 升级路径\n\n如果 rebuttal 能提供以下任一：\n- (a) Official SmolVLA checkpoint 完整 pruning sweep（确认 cliff-edge 在更高 baseline 下成立）\n- (b) 将因果语言全面降级为关联性表述\n- (c) k=0.5 same-seed 验证 + 增加 1-2 模型的 CV scaling law 数据点\n- (d) 正文压缩至 8 页\n\n论文有潜力升至 **borderline accept**。核心实验覆盖面和诊断性发现是实质贡献，问题主要在 claim 强度与证据的匹配。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"The vision connector, not model size or action head, determines pruning behavior\" → 改为 \"is strongly associated with\"\n- \"falsifies the 'immune' interpretation\" → π₀/π₀.5 原始论文未做此 claim，改为 \"demonstrates that offline tolerance does not generalize to closed-loop\"\n- \"seven VLA models\" → 加限定 \"(four with closed-loop evaluation)\"\n- π₀-OpenVLA 63pp gap 首次出现时加 caveat（connector + backbone + encoder 三变量不同）\n\n### Section 3 (Methods)\n- Section 3.2: \"most controlled available comparison\" 首次出现时需明确列出三个不同变量，而非仅在 Limitations 讨论\n- Table 1: π₀ 行加 \"offline only\" 标注；X-VLA Connector 列改为 \"Linear proj + 12-layer BART\"；CogACT 行明确标注 \"literature result, not our evaluation\"\n\n### Section 4 (Results)\n- Section 4.2: Official checkpoint 完整 pruning sweep 是 critical requirement\n- Section 4.5: \"flat M-curve\" → \"relatively stable M-curve\"；增加 M=96 dip 讨论\n- Section 4.6: Table 3 的 OpenVLA 行标注 cross-seed；CV predictor claim 降级\n\n### Section 5 (Analysis)\n- 大部分内容（5.1, 5.3, 5.4）移入 Appendix 以满足页数限制\n- Section 5.2: \"CV predicts\" → \"CV correlates with\"\n- Section 5.3: \"re-encoding is the operative mechanism\" → \"both cross-attention and MLP achieve comparable recovery\"\n\n### Section 6 (Conclusion)\n- \"Diagnose-then-Compress framework\" → \"diagnostic protocol\"\n- \"four findings\" 叙述需与降级后的 claim 强度一致",
  "project": "importance_margin_vla_compress",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: \"Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility\"\n**Venue**: CoRL 2026 | **Deadline**: 2026-05-29\n**Reviewers**: R1（实验严谨性 + 方法技术）, R2（新颖性 + 定位 + venue fit）\n**审稿模式**: Fresh（独立初审）\n\n---\n\n## Summary\n\n本文系统研究了 7 个 VLA 模型（450M–7B）跨三类 vision connector（linear projection / MLP projector / pixel-shuffle）的 token pruning 行为，在 LIBERO 仿真基准上提出四类可压缩性分类（uniformly critical / threshold-graded / smooth graded / catastrophic cliff），用 token importance CV 作为零成本预测指标，并提出 VTR（Vision Token Re-encoder）在 pixel-shuffle 架构的 catastrophic cliff 下恢复 60%+ 成功率。论文选题精准、实验覆盖广、写作质量高，但核心因果声明证据不足、CV predictor 验证数据点过少、SmolVLA baseline 差距大，且正文超出 CoRL 8 页限制。\n\n---\n\n## Strengths\n\n- **S1 [共识]** 问题定义精准且有实际意义。VLA token pruning 的跨架构不对称行为是被忽视但部署高度相关的问题。CoRL 社区直接相关。\n\n- **S2 [共识]** 跨架构覆盖面在 VLA efficiency 文献中少见：7 个模型、3 类 connector、多 pruning 策略和 ratio、每配置 500 episodes closed-loop 评估。Table 1 taxonomy 直觉清晰。\n\n- **S3 [共识]** π₀.5 在 k=0.5 处 L2 vs random 的 36pp 差距是本文最有价值的实验发现，证明 offline proxy 不可靠且低 CV 模型存在方法依赖性。SmolVLA 的 catastrophic cliff（5% removal → 0% SR）同样有说明力。\n\n- **S4 [共识]** VTR 实验设计有控制意识：extended training control（45.0% vs 44.8%）排除额外训练步数，MLP adapter 对照排除特定架构贡献。\n\n- **S5 [共识]** 写作清晰，结构合理，Table 1 标注系统（†‡§‖）和 Limitations section 诚实度高于平均水平。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-C1 [critical, 共识] 因果声明 under-identified——connector type 与多个架构变量混淆**\n\n论文使用 \"determines\"、\"strongly implicates\" 等因果语言（Section 1, 5.1），但三个 connector 家族的模型同时在 vision encoder、LLM backbone、action head、训练流程上不同。π₀–OpenVLA 被称为 \"most controlled comparison\"（Section 3.2），实际有 connector + backbone + encoder fusion 三变量不同。Within-connector 比较（OFT vs OpenVLA）仅证明家族内一致性，无法推广为跨家族因果。缺乏 controlled connector-swap 实验（同 backbone 不同 connector）。\n\n- R1: AGREE (W3) — \"correlation, not causation\"\n- R2: critical N1 — 核心 contribution 的因果基础不成立\n- 交叉回应：R1 完全 AGREE R2-N1，认为 R2 论证更系统\n\n**W-C2 [critical, 共识] SmolVLA baseline 44.8% 远低于官方 87.3%，cliff-edge 和 VTR 可推广性存疑**\n\n42.5pp gap（batch size 4 vs 64）。Official checkpoint (59.2%) 仅验证了一个 VTR 配置（M=32: 53.4%），无完整 pruning sweep。VTR 的 60.1% > baseline 44.8% 可能部分补偿 undertrained 缺陷。Cliff-edge 的 sharpness 可能被 undertrained checkpoint 放大。\n\n- R1: critical N1\n- R2: 交叉回应中 AGREE 并追加两个观察\n- 共识：official checkpoint 完整 pruning sweep 是 minimum requirement\n\n**W-C3 [critical, 共识] CV predictor 仅 3 模型 × 2 k 值 = 6 数据点，k=0.3 存在 reversal**\n\nTable 3 的 CV scaling law 统计上远未达到可靠结论。3 个数据点实际是 3 个簇（与 connector 标签等价），CV 无超越 connector label 的额外预测力。CV 范围两端（π₀, SmolVLA）缺 L2 vs random 对比。Taxonomy 边界无形式化标准。Perceiver/Q-Former 类 connector 完全缺失。\n\n- R1: critical N2\n- R2: critical N2 — 补充\"3 簇 = connector label\"论点\n- 交叉回应：双方强烈一致\n\n**W-C4 [critical, 共识] π₀ 仅 offline 评估但用于核心论证**\n\nTable 1 中 π₀ 与 π₀.5 并列为 \"uniformly critical\"，无标注区分评估协议。π₀–OpenVLA 63pp gap 是 offline loss vs closed-loop SR 的不可比对比。论文自身论证 offline metrics 不可信（Section 5.4），但 π₀ 仍用于核心 taxonomy 和 \"connector determines\" 论证。有完整 closed-loop pruning sweep 的仅 4 个模型（SmolVLA, OpenVLA, X-VLA, π₀.5），\"seven models\" 表述有夸大。\n\n- R1: critical N3\n- R2: 交叉回应 AGREE — internal consistency 问题\n\n### Should-Fix（影响评分但不一票否决）\n\n**W-S1 [warning, 共识] X-VLA \"linear projection\" 分类标签与 12-layer BART encoder 不匹配**\nTable 1 标签误导。X-VLA CV=0.151 远高于纯 linear（0.038-0.055），更接近 MLP（0.215）。暴露三分类粒度不足，暗示 connector 复杂度是连续谱。（R1-W5, R2 强烈 AGREE）\n\n**W-S2 [warning, 共识] OpenVLA L2 vs random 用不同 seed，k=0.5 same-seed 验证缺失**\nTable 3 中 OpenVLA Δ(R−L2)=−1.8pp 是 CV scaling law 最关键的 crossover point，seed variance 可能翻转符号。（R1-W1, R2 AGREE）\n\n**W-S3 [warning, 共识] VTR 新颖性有限——Perceiver/Q-Former 的 VLA 应用**\nVTR 架构与 Perceiver/Q-Former 功能等价。MLP adapter SR 更高（63.4% vs 60.1%）。贡献在于诊断 why re-encoding 而非方法本身。（R2-W2, R1 AGREE）\n\n**W-S4 [warning, 共识] VTR p=0.15 不足以声称 \"re-encoding is the operative mechanism\"**\nMLP adapter 实际 SR 更高。更准确解读是\"两者无显著差异，benefit from learned re-encoding in general\"。（R1-W2, R2 AGREE）\n\n**W-S5 [warning, 共识] \"Diagnose-then-Compress framework\" 过度包装**\n实质是 single-metric lookup table。验证不足以支撑 \"framework\" 标签。（R2-W4, R1 AGREE）\n\n**W-S6 [warning, 共识] 正文约 13 页，超 CoRL 8 页限制约 5 页**\nSection 5（Analysis）约 3 页是超页主因。需大幅压缩或移入 Appendix。（R2-W5, R1 AGREE）\n\n**W-S7 [warning, 共识] \"Falsifies immune assumption\" 措辞过强**\nπ₀/π₀.5 原始论文未声称 pruning immunity。发现本身有价值但 \"falsifies\" 构成稻草人论证。（R2-W1, R1 部分 AGREE — 同意措辞需降级）\n\n**W-S8 [warning] M=96 dip（54.5±3.2%）与 \"flat M-curve\" 叙述不完全一致**\nR1 认为破坏叙述，R2 认为 CI overlap 可能是 noise。建议改 \"flat\" 为 \"relatively stable\"。（R1-W4, R2 部分 REBUT）\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键问题上达成完全一致 [AGREE]：\n\n1. **因果声明证据不足**（W-C1）：\"determines\" 需降级为 \"is strongly associated with\"，缺乏 controlled connector-swap 实验\n2. **CV predictor 验证严重不足**（W-C3）：3 个数据点 = 3 个 connector 簇，无超越标签的额外预测力\n3. **π₀ offline-only 问题**（W-C4）：不应与 closed-loop 结果并列用于核心论证\n4. **SmolVLA baseline gap**（W-C2）：official checkpoint 完整 pruning sweep 是 minimum requirement\n5. **VTR 新颖性定位**（W-S3）：贡献在诊断 why re-encoding，非方法本身\n6. **正文超页**（W-S6）：约 13 页 vs 8 页限制，需大幅压缩\n7. **\"七模型\" framing 夸大**（W-C4）：完整 closed-loop 仅 4 个\n\n---\n\n## Reviewer Divergence\n\n**分歧 1：Simulation-only 评估的严重性**\n- R2：列为 critical（N3），引用 CoRL 2026 CFP 要求 real-robot 或 sim-to-real evidence\n- R1：REBUT — R2 引用的 CoRL policy 在公开文档中未找到；CoRL 历史接受 sim-only 分析论文；7 架构全做 real-robot 不合理。但同意缺乏 sim-to-real 讨论\n- **Director 判断**：降为 should-fix。论文核心贡献是架构级理解，simulation 的控制性是必要条件。但需增加 sim-to-real 讨论，说明 CV 是 architecture 属性而非 environment 属性\n\n**分歧 2：M=96 dip 是否破坏 flat M-curve 叙述**\n- R1：W4，认为 7.5pp 差异不可忽略\n- R2：REBUT — CI overlap，更可能是 noise\n- **Director 判断**：将 \"flat\" 改为 \"relatively stable\" 是充分的修复\n\n---\n\n## Questions for Authors\n\n1. SmolVLA official checkpoint (59.2%) 是否在所有 k 值下均 0% SR？（R1-Q1）\n2. CV=0.15 threshold 是 post-hoc 选择还是有先验依据？（R1-Q2）\n3. VTR 在 OpenVLA 上 0% SR（含 passthrough M=128）的机制是什么？对 workflow 实用性的影响？（R1-Q3）\n4. 是否考虑过 controlled connector-swap 实验（同 backbone 不同 connector）？（R2-Q1）\n5. Perceiver-based VLA（如 Octo）会落入 taxonomy 哪个类别？（R2-Q2）\n6. VTR 60.1% vs baseline 59.2% 的统计显著性？（R2-Q6）\n7. π₀.5 V-shaped L2 curve 的 spatial clustering 假设是否有 attention map 或 token position 分析验证？（R1-Q4）\n\n---\n\n## Missing References\n\n- \"Don't Run with Scissors\" (Jabbour et al.)：已引用但对比讨论不充分——该工作也研究 VLA pruning failure and recovery，Related Work 应增加对比\n- FastV (Chen et al., 2024)：VLM token pruning 重要 baseline，仅 Related Work 提及一次，建议增加在 VLA 上的适用性讨论\n- 引用验证结果：41 篇中 30 篇 verified，5 篇 not_found（近期 arXiv 预印本，OpenAlex 未收录），6 篇 minor first-author mismatch，**无虚假引用**\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置，未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（2026-05-21 14:07 → 14:10）\n\n主要发现（3 warning, 9 info）：\n- **[warning]** 前 3 页（pp.1-3）纯文本无任何 display item，审稿人第一印象窗口内只看到文字墙。Figure 1 应提前到 page 1-2\n- **[warning]** pp.11-13（Analysis + Conclusion）连续 3 页纯文本，缺辅助 figure/table\n- **[warning]** pp.5-6 方法描述密集无视觉辅助（Pruning Protocol + VTR + Diagnostic Metrics）\n- **[info]** 正文仅 2 figure + 3 table = 5 display items / 13 页，对实证论文偏少。大量实验结果被推到 appendix\n- **[info]** Figure 4（attention entropy）仅在 appendix，未被正文利用\n- **[info]** Figure 1 架构图清晰但出现在 page 4，错过锚定时机\n\n注：正文超页（~13 页）是排版问题的根本原因。压缩至 8 页后 display item 密度将大幅改善。\n\n---\n\n## Overall Assessment\n\n### 评分：Weak Reject\n\n### 置信度：High\n\n### 理由\n\n论文选择了一个重要且及时的问题（VLA 架构对 token pruning 的不对称响应），实验执行扎实（多模型、多策略、closed-loop、500 episodes），写作质量在平均水平之上。π₀.5 的 L2 vs random 36pp 差距、SmolVLA 的 catastrophic cliff 发现、以及 offline-vs-closed-loop disconnect 的展示都有实际价值。\n\n但四个结构性问题制约了 contributions 的可靠性：\n\n1. **因果声明缺乏实验基础**（W-C1）：三个 connector 家族的模型在 encoder/backbone/action head 上同时不同，\"determines\" 级因果语言无法成立。这直接影响 Contribution 1 的核心 claim。\n\n2. **CV predictor 验证严重不足**（W-C3）：3 个模型的 CV 值与 3 个 connector 标签一一对应，CV 实际未提供超越 connector 分类的额外预测力。k=0.3 reversal 进一步削弱了 \"dual predictor\" 的稳健性。这直接影响 Contribution 2。\n\n3. **SmolVLA baseline 42.5pp gap**（W-C2）：cliff-edge 和 VTR 结论建立在严重 undertrained 的 checkpoint 上，official checkpoint 仅验证了一个配置。这直接影响 Contribution 3。\n\n4. **π₀ offline-only 用于核心论证**（W-C4）：论文自身论证 offline 不可靠，但 π₀ 的 offline 结果仍用于支撑 taxonomy 分类和跨架构 comparison。\n\n### 升级路径\n\n如果 rebuttal 能提供以下任一：\n- (a) Official SmolVLA checkpoint 完整 pruning sweep（确认 cliff-edge 在更高 baseline 下成立）\n- (b) 将因果语言全面降级为关联性表述\n- (c) k=0.5 same-seed 验证 + 增加 1-2 模型的 CV scaling law 数据点\n- (d) 正文压缩至 8 页\n\n论文有潜力升至 **borderline accept**。核心实验覆盖面和诊断性发现是实质贡献，问题主要在 claim 强度与证据的匹配。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"The vision connector, not model size or action head, determines pruning behavior\" → 改为 \"is strongly associated with\"\n- \"falsifies the 'immune' interpretation\" → π₀/π₀.5 原始论文未做此 claim，改为 \"demonstrates that offline tolerance does not generalize to closed-loop\"\n- \"seven VLA models\" → 加限定 \"(four with closed-loop evaluation)\"\n- π₀-OpenVLA 63pp gap 首次出现时加 caveat（connector + backbone + encoder 三变量不同）\n\n### Section 3 (Methods)\n- Section 3.2: \"most controlled available comparison\" 首次出现时需明确列出三个不同变量，而非仅在 Limitations 讨论\n- Table 1: π₀ 行加 \"offline only\" 标注；X-VLA Connector 列改为 \"Linear proj + 12-layer BART\"；CogACT 行明确标注 \"literature result, not our evaluation\"\n\n### Section 4 (Results)\n- Section 4.2: Official checkpoint 完整 pruning sweep 是 critical requirement\n- Section 4.5: \"flat M-curve\" → \"relatively stable M-curve\"；增加 M=96 dip 讨论\n- Section 4.6: Table 3 的 OpenVLA 行标注 cross-seed；CV predictor claim 降级\n\n### Section 5 (Analysis)\n- 大部分内容（5.1, 5.3, 5.4）移入 Appendix 以满足页数限制\n- Section 5.2: \"CV predicts\" → \"CV correlates with\"\n- Section 5.3: \"re-encoding is the operative mechanism\" → \"both cross-attention and MLP achieve comparable recovery\"\n\n### Section 6 (Conclusion)\n- \"Diagnose-then-Compress framework\" → \"diagnostic protocol\"\n- \"four findings\" 叙述需与降级后的 claim 强度一致",
    "project": "importance_margin_vla_compress",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-21T14:32:33.148614+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6ea0e93e255655758819bea2ab1f224d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4167
}
```

</details>

---


### Assistant

_source line 348 · 2026-05-21T14:32:45.097354+00:00_

审稿报告已投递。

---

**审稿完成总结**

**评分：Weak Reject** | 置信度：High

两位 Reviewer 在核心问题上高度一致（7/11 个 weakness 完全共识），最终汇总四个 critical 问题：

| # | 问题 | 影响 |
|---|------|------|
| W-C1 | 因果声明 under-identified（connector vs backbone/encoder/action head 混淆） | Contribution 1 核心 claim |
| W-C2 | SmolVLA baseline 42.5pp gap，official checkpoint 未完整验证 | Contribution 3 (VTR) 可推广性 |
| W-C3 | CV predictor 仅 3 数据点 = 3 connector 簇，k=0.3 reversal | Contribution 2 核心 claim |
| W-C4 | π₀ offline-only 用于核心论证，与论文自身 "offline 不可信" 矛盾 | Taxonomy 完整性 |

唯一实质分歧在 sim-only 评估的严重性（R2: critical vs R1: should-fix），Director 判定为 should-fix。

**升级路径明确**：因果语言降级 + official SmolVLA 完整 pruning sweep + k=0.5 same-seed 验证 + 正文压缩至 8 页 → 有潜力升至 borderline accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 349 · 2026-05-21T14:32:46.245841+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。主要判断：

- **R2-S3 存在严重事实错误**：R2 将 SmolVLA 的 baseline（44.8%）和 cliff-edge 行为错误归因给了 π₀.5（实际 baseline 98.2%），且引用了错误的 Table。
- **R2-N1（因果混淆）和 N2（N=3 数据点）**：与我的 R1-W3 和 R1-N2 高度一致，AGREE。R2 的"3 个点 = 3 个 connector 簇"论点比我的分析更深入。
- **R2-N3（sim-only = critical）**：REBUT。R2 引用的 CoRL policy 在公开文档中未找到，且架构理解类研究需要 simulation 的控制性。建议降为 should-fix。
- **R2-W5（超页）**：经核实 AGREE——正文约 13 页，超出 8 页限制约 5 页。

---

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

对 R1 的 15 个具体论点的回应总结：
- **10 个 [AGREE]**：N1（SmolVLA baseline gap）、N2（CV 数据点不足）、N3（π₀ offline-only）、W1（seed 不一致）、W2（dropout ablation 不充分）、W3（"most controlled" 不成立）、W5（X-VLA 分类错误）、S1、S4、S5
- **2 个 [REBUT]**：S3（"immune falsification" 是稻草人论证）、W4（M=96 dip 有 CI overlap，不构成核心叙述破坏）
- **1 个 [AGREE with caveat]**：S2（7 模型实际 3 connector 类型）

主要新增发现：R1-N1 揭示的 SmolVLA baseline gap 进一步削弱了 VTR 实用性声明（VTR 60.1% 可能部分在补偿 undertrained model 缺陷而非真正解决 pruning 损伤）。维持 weak reject (borderline) 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 350 · 2026-05-21T14:33:03.282578+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿完成摘要**：

- **评分**：Weak Reject
- **置信度**：High
- **Reviewer 1**：Borderline（倾向 weak reject）
- **Reviewer 2**：Weak Reject（borderline）
- **交叉回应**：15 个论点中 10 个 AGREE，2 个 REBUT，核心问题高度收敛

**四个 critical 问题**：
1. 因果声明缺乏 controlled experiment 支撑（"determines" → "is associated with"）
2. SmolVLA baseline 42.5pp gap，cliff-edge 和 VTR 可推广性存疑
3. CV predictor 仅 6 个数据点且存在 reversal
4. π₀ offline-only 用于核心论证，与论文自身 "offline 不可靠" 论证矛盾

**升级路径**：official SmolVLA 完整 pruning sweep + 因果语言降级 + k=0.5 same-seed 验证 + 正文压缩至 8 页 → 有潜力升至 borderline accept。

Issue Tracker 已同步更新（16 个 issue，含 4 critical / 8 warning / 4 resolved）。视觉审查结果已纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 30

## Round 30

34 recorded events


### User

_source line 351 · 2026-05-22T08:04:14.073520+00:00_

[Round 5 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/importance_margin_vla_compress/artifacts/review_reports/round_4.md`
跨轮次问题追踪: `projects/importance_margin_vla_compress/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: importance_margin_vla_compress
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29
- **引用验证**: ❌ 未启用

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-22T08:04:37.297032+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-22T08:04:37.297452+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-22T08:04:42.478317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_reports/round_4.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_reports/round_4.md"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-22T08:04:43.081300+00:00_

1	---
2	round: 4
3	review_mode: fresh
4	overall_score: weak reject
5	timestamp: 2026-05-21T14:32:28.972562+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 4 (Fresh Review)
12	
13	**论文**: "Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility"
14	**Venue**: CoRL 2026 | **Deadline**: 2026-05-29
15	**Reviewers**: R1（实验严谨性 + 方法技术）, R2（新颖性 + 定位 + venue fit）
16	**审稿模式**: Fresh（独立初审）
17	
18	---
19	
20	## Summary
21	
22	本文系统研究了 7 个 VLA 模型（450M–7B）跨三类 vision connector（linear projection / MLP projector / pixel-shuffle）的 token pruning 行为，在 LIBERO 仿真基准上提出四类可压缩性分类（uniformly critical / threshold-graded / smooth graded / catastrophic cliff），用 token importance CV 作为零成本预测指标，并提出 VTR（Vision Token Re-encoder）在 pixel-shuffle 架构的 catastrophic cliff 下恢复 60%+ 成功率。论文选题精准、实验覆盖广、写作质量高，但核心因果声明证据不足、CV predictor 验证数据点过少、SmolVLA baseline 差距大，且正文超出 CoRL 8 页限制。
23	
24	---
25	
26	## Strengths
27	
28	- **S1 [共识]** 问题定义精准且有实际意义。VLA token pruning 的跨架构不对称行为是被忽视但部署高度相关的问题。CoRL 社区直接相关。
29	
30	- **S2 [共识]** 跨架构覆盖面在 VLA efficiency 文献中少见：7 个模型、3 类 connector、多 pruning 策略和 ratio、每配置 500 episodes closed-loop 评估。Table 1 taxonomy 直觉清晰。
31	
32	- **S3 [共识]** π₀.5 在 k=0.5 处 L2 vs random 的 36pp 差距是本文最有价值的实验发现，证明 offline proxy 不可靠且低 CV 模型存在方法依赖性。SmolVLA 的 catastrophic cliff（5% removal → 0% SR）同样有说明力。
33	
34	- **S4 [共识]** VTR 实验设计有控制意识：extended training control（45.0% vs 44.8%）排除额外训练步数，MLP adapter 对照排除特定架构贡献。
35	
36	- **S5 [共识]** 写作清晰，结构合理，Table 1 标注系统（†‡§‖）和 Limitations section 诚实度高于平均水平。
37	
38	---
39	
40	## Weaknesses
41	
42	### Must-Fix（影响接收决定）
43	
44	**W-C1 [critical, 共识] 因果声明 under-identified——connector type 与多个架构变量混淆**
45	
46	论文使用 "determines"、"strongly implicates" 等因果语言（Section 1, 5.1），但三个 connector 家族的模型同时在 vision encoder、LLM backbone、action head、训练流程上不同。π₀–OpenVLA 被称为 "most controlled comparison"（Section 3.2），实际有 connector + backbone + encoder fusion 三变量不同。Within-connector 比较（OFT vs Op
…[truncated 8422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-22T08:04:43.232250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-22T08:04:43.233026+00:00_

1	- id: "R4-C1"
2	  summary: "Causal claim under-identified — connector vs backbone/encoder/action confound"
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 4
7	  last_seen_round: 4
8	  mentions:
9	    - {round: 4, reviewers: "R1+R2 consensus", note: "determines needs downgrade to associated with"}
10	  action_items:
11	    - {round: 4, action: "Full-text causal language downgrade (determines→associated, controlled→closest available)", assigned_to: "paper_agent", status: "done"}
12	  resolution: "All causal language downgraded: determines→associated, controlled→closest available, immunity→dispensable, operative mechanism→key factor. Not immune retained in intro/conclusion (negation, core finding)."
13	  resolution_round: 4
14	
15	- id: "R4-C2"
16	  summary: "SmolVLA baseline 44.8% vs official 87.3% — cliff and VTR on undertrained checkpoint"
17	  category: experiment
18	  severity: critical
19	  status: resolved
20	  first_raised_round: 4
21	  last_seen_round: 4
22	  mentions:
23	    - {round: 4, reviewers: "R1+R2 consensus", note: "Official checkpoint full pruning sweep is minimum requirement"}
24	  action_items:
25	    - {round: 4, action: "SmolVLA official checkpoint pruning sweep (10 configs)", assigned_to: "main_agent", status: "done", note: "D148: baseline 57.2%, L2norm k=0.9=0%, k=0.5=0%, random k=0.95=0%. All pruning=0%. seed43 running."}
26	    - {round: 4, action: "Write official results into paper", assigned_to: "paper_agent", status: "done", note: "Integrated into results.tex §4.1 main text + appendix dual-protocol table."}
27	  resolution: "Official HF checkpoint (57.2% baseline) shows identical 0% cliff at all pruning configs. Cliff is architectural, not training artifact. Data in main text Results section."
28	  resolution_round: 4
29	
30	- id: "R4-C3"
31	  summary: "CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal"
32	  category: framing
33	  severity: critical
34	  status: resolved
35	  first
…[truncated 8864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-22T08:04:43.685311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-22T08:04:43.735912+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	
13	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
14	
15	\begin{document}
16	\maketitle
17	
18	\input{abstract}
19	
20	\keywords{vision-language-action models, token pruning, robot learning}
21	
22	\input{introduction}
23	
24	\input{related_work}
25	
26	\input{experimental_setup}
27	
28	\input{results}
29	
30	\input{analysis}
31	
32	\input{conclusion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-22T08:04:58.790077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-22T08:04:59.143319+00:00_

1	\begin{abstract}
2	Vision token pruning accelerates Vision Transformer inference with negligible accuracy loss, but whether this robustness transfers to Vision-Language-Action (VLA) models remains untested across architectures. We study seven VLA models (450M--7B parameters) spanning three vision connector families, evaluating four in closed-loop robotic manipulation (LIBERO) and analyzing three via offline metrics or literature. The vision connector is strongly associated with pruning behavior along a four-class compressibility spectrum. Uniformly critical models ($\pi_0$, $\pi_0.5$; CV $< 0.06$) tolerate random subsampling but collapse under importance-based selection: $\pi_0.5$ retains 69.4\% success rate with random removal at 50\% retention but drops to 33.4\% under L2 norm selection, a 36 percentage-point gap demonstrating that offline pruning tolerance does not guarantee closed-loop robustness. Threshold-graded models (X-VLA; CV $= 0.151$) maintain $97.8 \pm 0.4$\% through 90\% retention before cliffing at 85\% ($-$31\,pp). Smooth graded models (OpenVLA, OFT; CV $\approx 0.22$) degrade proportionally. Catastrophic cliff models (SmolVLA; CV $= 0.314$) collapse to 0\% at 5\% removal across all seven tested configurations. The coefficient of variation (CV) of token L2 norms serves as a zero-cost diagnostic metric that correlates with both the tolerance class and the optimal pruning strategy from a single forward pass. The gap between random and L2 norm selection scales monotonically with CV at both 50\% and 70\% retention across three models. For catastrophic-cliff architectures, Vision Token Re-encoder (VTR) recovers 60\%+ success rate at 75\% compression where all deletion methods yield 0\%, with a relatively stable M-curve ($M{=}16 \approx M{=}128$) confirming learned re-encoding as the key factor. CV diagnosis followed by connector-appropriate compression forms a diagnostic protocol for safe VLA token reduction.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-22T08:04:59.143785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-22T08:04:59.595749+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
7	\caption{Vision connector comparison. SmolVLA's pixel-shuffle folds $4{\times}4$ patches into single tokens (128 total, spatially entangled). OpenVLA's MLP projector maps each patch independently (256 tokens, per-token independence). The connector design is strongly associated with token compressibility.}
8	\label{fig:architecture}
9	\end{figure}
10	
11	Vision token pruning reliably accelerates Vision Transformers with negligible accuracy loss~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}. Vision-Language-Action (VLA) models~\cite{kim2024openvla,black2024pi0,shukor2025smolvla} use the same ViT encoders and produce hundreds of vision tokens that dominate the language backbone's input, making token reduction attractive for real-time robotic control at 5--10\,Hz. Yet applying pruning to VLAs yields wildly inconsistent results: SmolVLA~\cite{shukor2025smolvla} collapses to 0\% task success at 5\% token removal, while $\pi_0$~\cite{black2024pi0} shows a 2.4\% \emph{improvement} in offline action loss at 90\% removal (offline metrics only; no closed-loop evaluation available). No existing work explains which outcome a given architecture will produce.
12	
13	The critical architectural variable is the vision connector that transforms ViT patches into tokens for the language backbone. Pixel-shuffle connectors~\cite{shukor2025smolvla,chen2024internvl} fold spatial patches so each token encodes a $4{\times}4$ receptive field. MLP projectors~\cite{liu2023llava,kim2024openvla} map patches independently through learned nonlinearities. Linear projections~\cite{black2024pi0,black2025pi05} apply a single matrix multiplication. Recent VLA-specific works~\cite{chen2024fastv,xu2025vlacache,cheng2026vlaiap} evaluate individual architectures without testing whether pruning behaves consistently across connector designs (F
…[truncated 2448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-22T08:04:59.596124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-22T08:05:00.148819+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Vision token efficiency.}
5	Token pruning in ViTs removes 30--60\% of tokens with $<$1\% accuracy loss on classification, via learned masks~\cite{rao2021dynamicvit}, attention-guided reorganization~\cite{liang2022evit}, bipartite matching~\cite{bolya2023tome}, window-level sparsity~\cite{chen2023sparsevit}, adaptive halting~\cite{yin2022avit,meng2022adavit}, or learned spatial selection~\cite{ryoo2021tokenlearner}. For VLMs, pruning extends to the language backbone: FastV~\cite{chen2024fastv} removes tokens after early LLM layers, LLaVA-PruMerge~\cite{shang2024prumerge} and FasterVLM~\cite{zhang2024fastervlm} use CLS-token attention as an importance signal, FitPrune~\cite{ye2025fitprune} minimizes attention-distribution divergence without training, and CrossGET~\cite{shi2024crossget} applies cross-modal token merging; TokenPacker~\cite{li2024tokenpacker} re-encodes compressed representations. All evaluate on classification or VQA benchmarks; we test whether these results transfer to closed-loop VLA control, where action errors compound across timesteps.
6	
7	\paragraph{VLA-specific token reduction.}
8	VLA-Cache~\cite{xu2025vlacache} caches vision KV states across timesteps for 1.7$\times$ speedup without removing tokens. VLA-IAP~\cite{cheng2026vlaiap} uses interaction-aligned pruning on OpenVLA; EfficientVLA~\cite{yang2025efficientvla} combines layer pruning and token selection on CogACT~\cite{li2024cogact}; VLA-Pruner~\cite{liu2025vlapruner} uses dual-level importance criteria for temporal-aware pruning. All evaluate on MLP-projector architectures. None reports the cliff-edge failure we observe on pixel-shuffle VLAs; their positive results may not generalize to spatially entangled connectors.
9	
10	\paragraph{Vision connectors.}
11	Linear projections~\cite{black2024pi0,black2025pi05} apply no cross-token mixing, producing independently addressable tokens; $\pi_{0.5}$~\cite{black2025pi05} adds a lea
…[truncated 2850 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-22T08:05:00.149322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-22T08:05:00.200017+00:00_

1	\section{Methods and Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\subsection{Architectures and Benchmark}
5	\label{sec:setup_overview}
6	
7	Seven VLA architectures spanning three vision connector families provide the testbed (Table~\ref{tab:taxonomy}).
8	
9	\textbf{Linear projection.} $\pi_0$~\cite{black2024pi0} (3.3B, 256 tokens) maps SigLIP~\cite{zhai2023siglip} patches through a single linear layer; $\pi_0.5$~\cite{black2025pi05} (4B, 768 tokens from three cameras) adds a learned $\times\!\sqrt{d}$ scaling; X-VLA~\cite{zheng2025xvla} (880M, 50 tokens) augments its linear projection with a 12-layer BART encoder~\cite{lewis2020bart} that introduces cross-token mixing. \textbf{MLP projector.} OpenVLA~\cite{kim2024openvla} (7B, 256 tokens) fuses DINOv2~\cite{oquab2023dinov2} and SigLIP through a three-layer MLP; OFT~\cite{kim2025openoft} shares this connector (entropy comparison only); CogACT~\cite{li2024cogact} retains 74.2\% SR under 78\% pruning per EfficientVLA~\cite{yang2025efficientvla} (literature corroboration, not our evaluation). \textbf{Spatial folding.} SmolVLA~\cite{shukor2025smolvla} (450M, 128 tokens) applies pixel-shuffle ($4{\times}4$ folding) so each token encodes 16 contiguous patches.
10	
11	We evaluate on LIBERO~\cite{liu2023libero} (Object: 10 tasks $\times$ 50 episodes = 500 total; Spatial and Goal for cross-suite validation). Closed-loop success rate (SR) with Wilson 95\% CIs is the primary metric; multi-seed results report mean $\pm$ std. Baselines: SmolVLA 44.8\%, OpenVLA 74.0\%, X-VLA 99.2\%, $\pi_0.5$ 98.2\%.
12	
13	\subsection{Pruning Protocol}
14	\label{sec:pruning_protocol}
15	
16	Two methods bracket robustness. \textbf{L2 norm-based removal} ranks tokens by L2 norm and physically removes the lowest-norm fraction, providing a favorable test. \textbf{Random removal} selects tokens uniformly at random, providing a conservative lower bound. Both physically remove tokens (not zero-masking); remaining tokens retain spatial or
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-22T08:05:09.158898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-22T08:05:10.012696+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$: offline metrics only, no clo
…[truncated 15698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-22T08:05:10.013212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-22T08:05:10.065322+00:00_

1	\section{Discussion}
2	\label{sec:analysis}
3	
4	\paragraph{Re-encoding and CV diagnostics.}
5	Both cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels: X-VLA shares a linear projection with $\pi_0$ yet its BART encoder yields CV$\,{=}\,$0.151 and threshold-graded behavior, correctly differentiating it from $\pi_0$'s CV$\,{=}\,$0.038. The CV-strategy interaction partially reverses at $k{=}0.3$ (Appendices~\ref{app:cv_strategy_interaction},~\ref{app:cv_extended}).
6	
7	\paragraph{Limitations.}
8	All closed-loop experiments use LIBERO simulation; the seven models differ in backbone and encoder fusion, preventing clean causal isolation (Appendix~\ref{app:confounders}). $\pi_0$ is offline only; the CV correlation spans three models and two retention ratios; the hypergeometric cliff model captures onset sharpness (RMSE$\,{=}\,$0.025) but does not explain V-shape recovery at $k \leq 0.7$.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-22T08:05:10.065758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-22T08:05:10.118337+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We studied vision token pruning across seven VLA models (450M--7B) spanning three connector families on closed-loop LIBERO. The vision connector is strongly associated with pruning behavior along a four-class spectrum; token importance CV correlates with both tolerance class and optimal strategy. Low-CV models are uniformly critical, not immune ($\pi_0.5$: 36\,pp gap at $k{=}0.5$); for pixel-shuffle architectures, learned re-encoding recovers 60\%+ SR at 75\% compression where deletion yields 0\%.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-22T08:05:16.301314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-22T08:05:17.005017+00:00_

1	\appendix
2	
3	\section{Pruning Protocol Details}
4	\label{app:pruning_details}
5	
6	Both pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.
7	
8	Model-specific retention ratios reflect each architecture's token count and expected sensitivity. $\pi_0$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\pi_0.5$ uses $k \in \{0.3, 0.5, 0.7\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \in \{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \in \{0.3, 0.5, 0.7, 0.9, 0.95\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\cite{bolya2023tome}).
9	
10	The $\pi_0$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\ three-layer MLP), backbone (PaliGemma vs.\ Llama-2), and encoder fusion strategy (single SigLIP vs.\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all 
…[truncated 8254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-22T08:05:17.178233+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && wc -l abstract.tex introduction.tex related_work.tex experimental_setup.tex results.tex analysis.tex conclusion.tex appendix.tex 2>/dev/null",
  "description": "Count lines per section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && wc -l abstract.tex introduction.tex related_work.tex experimental_setup.tex results.tex analysis.tex conclusion.tex appendix.tex 2>/dev/null",
    "description": "Count lines per section"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-22T08:05:17.400565+00:00_

    3 abstract.tex
   22 introduction.tex
   13 related_work.tex
   26 experimental_setup.tex
  123 results.tex
    8 analysis.tex
    4 conclusion.tex
  686 appendix.tex
  885 total
Shell cwd was reset to /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_director_d59e3b5c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 222
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-22T08:06:08.989281+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-22T08:06:34.191300+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 25202
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-22T08:06:34.395053+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "5",
  "text": "你是 Reviewer 1（实验严谨性 + 方法技术），这是 Round 5 继续审稿。\n\n## 投稿信息\n- **Venue**: CoRL 2026 | **Deadline**: 2026-05-29\n- **格式**: 8 页正文 + 附录/参考文献不计入 | Double-blind | corl_2026.sty\n\n## 论文路径\n- 主文件: `projects/importance_margin_vla_compress/docs/paper/main.tex`\n- 各章节在同目录下\n\n## 上一轮（Round 4）你的主要发现\n\n以下是你在 Round 4 提出的问题清单。请逐条检查论文修改，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n### Must-Fix (Critical)\n\n**R4-N1 [SmolVLA baseline 44.8% vs 官方 87.3%]**\n- 要求：official checkpoint 完整 pruning sweep\n- Issue Tracker 状态：resolved — \"Official HF checkpoint (57.2% baseline) shows identical 0% cliff at all pruning configs\"\n- 请验证：论文是否包含 official checkpoint 的多 k 值 pruning 结果，数据是否在主文或附录中\n\n**R4-N2 [CV predictor 仅 3 模型 × 2 k 值]**\n- 要求：降级 claim 或增加模型验证\n- Issue Tracker 状态：resolved — \"CV reframed as correlational (predicts→correlates)\"\n- 请验证：全文是否已将 \"predicts\" 替换为 \"correlates\"，Section 标题是否修改\n\n**R4-N3 [π₀ offline-only 用于核心 comparison]**\n- 要求：Table 1 加 offline-only 标注，63pp gap 降级\n- Issue Tracker 状态：resolved — \"Table 1 π0 has †offline-only footnote\"\n- 请验证：Table 1 标注、Introduction 和 Results 中的 π₀ 相关叙述\n\n### Should-Fix (Warning)\n\n**R4-W1 [OpenVLA L2 vs random cross-seed, k=0.5 same-seed 缺失]**\n- Issue Tracker: resolved — \"seed42 random k=0.5 = 35.8%\"\n- 请验证：footnote 中是否报告 same-seed k=0.5 结果\n\n**R4-W2 [VTR p=0.15 claim 过强]**\n- Issue Tracker: resolved — \"comparable (not equivalent)\"\n- 请验证：Section 4.5 和 Discussion 中的措辞\n\n**R4-W3 [π₀ vs OpenVLA \"most controlled comparison\" 不成立]**\n- Issue Tracker: resolved via R4-C1 — causal language downgrade\n- 请验证：\"most controlled\" 是否已删除或加 caveat\n\n**R4-W4 [M=96 dip vs \"flat M-curve\"]**\n- Issue Tracker: resolved — \"flat→relatively stable\"\n- 请验证：全文是否一致\n\n**R4-W5 [X-VLA \"linear projection\" 标签]**\n- Issue Tracker: resolved — \"Linear + BART (12L)\"\n- 请验证：Table 1 Connector 列\n\n### 新增审查\n\n除了验证上述修复外，请特别关注：\n1. **新增内容是否引入新问题**：Section 4.7 Cross-Suite Generalization 和 hypergeometric cliff model 是全新内容\n2. **正文是否符合 8 页限制**\n3. **统计报告是否完整和一致**\n4. **修改是否过度降级**：claim 降级是否合理，还是矫枉过正\n\n请按以下格式输出：\n1. Round 4 Issue 逐条验证（[RESOLVED] / [STILL_OPEN]）\n2. 新发现的问题（如有）\n3. Overall Score（与 Round 4 对比是否变化）+ Confidence",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "5",
    "text": "你是 Reviewer 1（实验严谨性 + 方法技术），这是 Round 5 继续审稿。\n\n## 投稿信息\n- **Venue**: CoRL 2026 | **Deadline**: 2026-05-29\n- **格式**: 8 页正文 + 附录/参考文献不计入 | Double-blind | corl_2026.sty\n\n## 论文路径\n- 主文件: `projects/importance_margin_vla_compress/docs/paper/main.tex`\n- 各章节在同目录下\n\n## 上一轮（Round 4）你的主要发现\n\n以下是你在 Round 4 提出的问题清单。请逐条检查论文修改，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n### Must-Fix (Critical)\n\n**R4-N1 [SmolVLA baseline 44.8% vs 官方 87.3%]**\n- 要求：official checkpoint 完整 pruning sweep\n- Issue Tracker 状态：resolved — \"Official HF checkpoint (57.2% baseline) shows identical 0% cliff at all pruning configs\"\n- 请验证：论文是否包含 official checkpoint 的多 k 值 pruning 结果，数据是否在主文或附录中\n\n**R4-N2 [CV predictor 仅 3 模型 × 2 k 值]**\n- 要求：降级 claim 或增加模型验证\n- Issue Tracker 状态：resolved — \"CV reframed as correlational (predicts→correlates)\"\n- 请验证：全文是否已将 \"predicts\" 替换为 \"correlates\"，Section 标题是否修改\n\n**R4-N3 [π₀ offline-only 用于核心 comparison]**\n- 要求：Table 1 加 offline-only 标注，63pp gap 降级\n- Issue Tracker 状态：resolved — \"Table 1 π0 has †offline-only footnote\"\n- 请验证：Table 1 标注、Introduction 和 Results 中的 π₀ 相关叙述\n\n### Should-Fix (Warning)\n\n**R4-W1 [OpenVLA L2 vs random cross-seed, k=0.5 same-seed 缺失]**\n- Issue Tracker: resolved — \"seed42 random k=0.5 = 35.8%\"\n- 请验证：footnote 中是否报告 same-seed k=0.5 结果\n\n**R4-W2 [VTR p=0.15 claim 过强]**\n- Issue Tracker: resolved — \"comparable (not equivalent)\"\n- 请验证：Section 4.5 和 Discussion 中的措辞\n\n**R4-W3 [π₀ vs OpenVLA \"most controlled comparison\" 不成立]**\n- Issue Tracker: resolved via R4-C1 — causal language downgrade\n- 请验证：\"most controlled\" 是否已删除或加 caveat\n\n**R4-W4 [M=96 dip vs \"flat M-curve\"]**\n- Issue Tracker: resolved — \"flat→relatively stable\"\n- 请验证：全文是否一致\n\n**R4-W5 [X-VLA \"linear projection\" 标签]**\n- Issue Tracker: resolved — \"Linear + BART (12L)\"\n- 请验证：Table 1 Connector 列\n\n### 新增审查\n\n除了验证上述修复外，请特别关注：\n1. **新增内容是否引入新问题**：Section 4.7 Cross-Suite Generalization 和 hypergeometric cliff model 是全新内容\n2. **正文是否符合 8 页限制**\n3. **统计报告是否完整和一致**\n4. **修改是否过度降级**：claim 降级是否合理，还是矫枉过正\n\n请按以下格式输出：\n1. Round 4 Issue 逐条验证（[RESOLVED] / [STILL_OPEN]）\n2. 新发现的问题（如有）\n3. Overall Score（与 Round 4 对比是否变化）+ Confidence",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-22T08:06:51.717839+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17322
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-22T08:06:52.173528+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "5",
  "text": "你是 Reviewer 2（新颖性 + 定位 + venue fit），这是 Round 5 继续审稿。\n\n## 投稿信息\n- **Venue**: CoRL 2026 | **Deadline**: 2026-05-29\n- **格式**: 8 页正文 + 附录/参考文献不计入 | Double-blind | corl_2026.sty\n\n## 论文路径\n- 主文件: `projects/importance_margin_vla_compress/docs/paper/main.tex`\n- 各章节在同目录下\n\n## 上一轮（Round 4）你的主要发现\n\n以下是你在 Round 4 提出的问题清单。请逐条检查论文修改，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n### Must-Fix (Critical)\n\n**R4-N1 [因果声明 under-identified — connector vs 多变量混淆]**\n- 要求：降级为 \"associated with\"，或补充 connector-swap 实验\n- Issue Tracker 状态：resolved — \"All causal language downgraded: determines→associated\"\n- 请验证：Abstract, Introduction, Results, Discussion, Conclusion 中的因果语言\n\n**R4-N2 [Taxonomy 和 CV predictor 仅 N=3 connector 类型]**\n- 要求：增加 Perceiver/Q-Former 类，或降级 claim\n- Issue Tracker 状态：resolved — \"CV reframed as correlational\"\n- 请验证：claim 降级是否充分；Perceiver/Q-Former 是否在 Related Work 讨论更充分\n\n**R4-N3 [纯仿真评估与 CoRL venue 要求]**\n- Director Round 4 判断：降为 should-fix\n- 请验证：是否增加了 sim-to-real transferability 讨论\n\n### Should-Fix (Warning)\n\n**R4-W1 [\"Falsifies immune assumption\" 是稻草人论证]**\n- Issue Tracker: resolved — \"All 'falsifies' removed\"\n- 请验证：Introduction 和 Results 中的措辞\n\n**R4-W2 [VTR 新颖性有限]**\n- Issue Tracker: resolved — \"VTR framed as diagnostic protocol contribution\"\n- 请验证：Introduction contributions 和 Discussion 中的定位\n\n**R4-W3 [\"七个模型\" framing 夸大]**\n- Issue Tracker: resolved\n- 请验证：Abstract 和 Introduction 是否区分 closed-loop vs offline/literature\n\n**R4-W4 [\"Diagnose-then-Compress framework\" 过度包装]**\n- Issue Tracker: resolved — \"All 'framework' replaced with 'diagnostic protocol'\"\n- 请验证：全文一致性\n\n**R4-W5 [正文超页]**\n- Issue Tracker: resolved — \"Paper compressed to 8 pages\"\n- 请验证：正文页数\n\n### 新增审查\n\n除了验证上述修复外，请特别关注：\n1. **Related Work 是否已充分扩展**：Round 4 建议增加 15+ citations，Don't Run with Scissors 对比讨论\n2. **新增 Section 4.7 Cross-Suite Generalization 的 novelty 贡献**：hypergeometric cliff model 是否过度拟合？\n3. **整体 positioning 是否改善**：从 \"framework paper\" 到 \"diagnostic empirical study\" 的转型是否成功\n4. **标题是否仍然合适**：在 claim 降级后，\"Why Token Pruning Crashes\" 是否与内容匹配\n\n请按以下格式输出：\n1. Round 4 Issue 逐条验证（[RESOLVED] / [STILL_OPEN]）\n2. 新发现的问题（如有）\n3. Overall Score（与 Round 4 对比是否变化）+ Confidence",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "5",
    "text": "你是 Reviewer 2（新颖性 + 定位 + venue fit），这是 Round 5 继续审稿。\n\n## 投稿信息\n- **Venue**: CoRL 2026 | **Deadline**: 2026-05-29\n- **格式**: 8 页正文 + 附录/参考文献不计入 | Double-blind | corl_2026.sty\n\n## 论文路径\n- 主文件: `projects/importance_margin_vla_compress/docs/paper/main.tex`\n- 各章节在同目录下\n\n## 上一轮（Round 4）你的主要发现\n\n以下是你在 Round 4 提出的问题清单。请逐条检查论文修改，标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。\n\n### Must-Fix (Critical)\n\n**R4-N1 [因果声明 under-identified — connector vs 多变量混淆]**\n- 要求：降级为 \"associated with\"，或补充 connector-swap 实验\n- Issue Tracker 状态：resolved — \"All causal language downgraded: determines→associated\"\n- 请验证：Abstract, Introduction, Results, Discussion, Conclusion 中的因果语言\n\n**R4-N2 [Taxonomy 和 CV predictor 仅 N=3 connector 类型]**\n- 要求：增加 Perceiver/Q-Former 类，或降级 claim\n- Issue Tracker 状态：resolved — \"CV reframed as correlational\"\n- 请验证：claim 降级是否充分；Perceiver/Q-Former 是否在 Related Work 讨论更充分\n\n**R4-N3 [纯仿真评估与 CoRL venue 要求]**\n- Director Round 4 判断：降为 should-fix\n- 请验证：是否增加了 sim-to-real transferability 讨论\n\n### Should-Fix (Warning)\n\n**R4-W1 [\"Falsifies immune assumption\" 是稻草人论证]**\n- Issue Tracker: resolved — \"All 'falsifies' removed\"\n- 请验证：Introduction 和 Results 中的措辞\n\n**R4-W2 [VTR 新颖性有限]**\n- Issue Tracker: resolved — \"VTR framed as diagnostic protocol contribution\"\n- 请验证：Introduction contributions 和 Discussion 中的定位\n\n**R4-W3 [\"七个模型\" framing 夸大]**\n- Issue Tracker: resolved\n- 请验证：Abstract 和 Introduction 是否区分 closed-loop vs offline/literature\n\n**R4-W4 [\"Diagnose-then-Compress framework\" 过度包装]**\n- Issue Tracker: resolved — \"All 'framework' replaced with 'diagnostic protocol'\"\n- 请验证：全文一致性\n\n**R4-W5 [正文超页]**\n- Issue Tracker: resolved — \"Paper compressed to 8 pages\"\n- 请验证：正文页数\n\n### 新增审查\n\n除了验证上述修复外，请特别关注：\n1. **Related Work 是否已充分扩展**：Round 4 建议增加 15+ citations，Don't Run with Scissors 对比讨论\n2. **新增 Section 4.7 Cross-Suite Generalization 的 novelty 贡献**：hypergeometric cliff model 是否过度拟合？\n3. **整体 positioning 是否改善**：从 \"framework paper\" 到 \"diagnostic empirical study\" 的转型是否成功\n4. **标题是否仍然合适**：在 claim 降级后，\"Why Token Pruning Crashes\" 是否与内容匹配\n\n请按以下格式输出：\n1. Round 4 Issue 逐条验证（[RESOLVED] / [STILL_OPEN]）\n2. 新发现的问题（如有）\n3. Overall Score（与 Round 4 对比是否变化）+ Confidence",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-22T08:06:54.393663+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2220
}
```

</details>

---


### Assistant

_source line 384 · 2026-05-22T08:09:13.261840+00:00_

Round 5 审稿进行中。Reviewer 1 和 Reviewer 2 已派发任务，等待审稿结果返回。视觉审查也已同步派发。

当前状态：
- **Reviewer 1**: 已派发（验证 Round 4 全部 15 项 issue 修复情况 + 新增内容审查）
- **Reviewer 2**: 已派发（同上）
- **Visual Check**: 已派发（并行执行，不阻塞）

收到两位 Reviewer 的 Round 5 审稿结果后，将进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 385 · 2026-05-22T08:13:37.064409+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 5 审稿报告

---

## Part 1: Round 4 Issue 逐条验证

### Must-Fix (Critical)

**R4-N1 [SmolVLA baseline 44.8% vs 官方] → [RESOLVED]**

论文现已包含 official HF checkpoint 的多 k 值 pruning 数据：
- Section 4.2 明确写道："the official SmolVLA HF checkpoint (57.2% SR unpruned, CI [52.9%, 61.4%]) also collapses to 0% under random k=0.95 (5% removal), L2 norm k=0.9 (10% removal), and L2 norm k=0.5"
- Table 3（Appendix B）展示了两个独立评估协议（protocol A: 59.2% baseline, protocol B: 57.2% baseline），在 k∈{0.95, 0.9, 0.5} 下均为 0% SR，附 Wilson 95% CI
- Page 27 还补充了 VTR 对 official checkpoint 的对比："Smart Compress at M=32 (60.1 ± 1.3%) recovers...comparable to the official SmolVLA checkpoint (59.2%)"

虽然不是我原始要求的完整 k∈{0.5, 0.7, 0.9, 0.95} sweep（缺 k=0.7），但已有的 3 个 k 值全部为 0%，足以论证 cliff-edge 是架构属性而非训练 artifact。

**R4-N2 [CV predictor 仅 3 模型 × 2 k 值，claim 过强] → [RESOLVED]**

全面降级，修改一致：
- Section 4.6 标题：~~"CV Predicts Optimal Pruning Strategy"~~ → **"CV Correlates with Optimal Pruning Strategy"** ✓
- Introduction: "CV correlates with both the tolerance class and the optimal strategy" ✓
- Contribution 2: ~~"CV as dual predictor"~~ → **"CV as diagnostic metric"** ✓
- Introduction 新增限定："evaluating four in closed-loop and analyzing three via offline metrics or literature" ✓
- Section 5 (Discussion): 明确指出 "the CV correlation spans three models and two retention ratios" ✓
- Table 3 从正文移至 Appendix P，正文仅引用关键数值 ✓
- Abstract: "correlates with both the tolerance class and the optimal pruning strategy" ✓

降级程度恰当——没有矫枉过正，核心发现仍然清楚，但 claim 强度与数据支撑匹配。

**R4-N3 [π₀ offline-only 用于核心 comparison] → [RESOLVED]**

三处修改全部到位：
1. Table 1 footnote: "†π₀: offline metrics only, no closed-loop evaluation; the 63 pp gap vs. OpenVLA at k=0.1 mixes offline loss with closed-loop SR." ✓
2. Introduction: "(offline metrics only; no closed-loop evaluation available)" ✓ ；"evaluating four in closed-loop and analyzing three via offline metrics or literature" ✓
3. Section 4.4: ~~"This result falsifies the 'immune' assumption"~~ → **"This result demonstrates that models showing offline pruning tolerance can exhibit severe closed-loop degradation."** ✓
4. π₀–OpenVLA comparison 加了明确 caveat: "This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation." ✓

### Should-Fix (Warning)

**R4-W1 [OpenVLA k=0.5 same-seed 缺失] → [RESOLVED]**

Footnote 5 现在报告："same-seed at k=0.5: 35.8% random vs. 39.2% L2 (gap 3.4 pp)." ✓ 三个 k 值（0.3, 0.5, 0.7）的 same-seed 验证现已完整。

**R4-W2 [VTR p=0.15 claim "re-encoding is the operative mechanism" 过强] → [RESOLVED]**

- Table 2 caption: "comparable SR (p = 0.15 vs. cross-attention)" ✓
- Section 4.5: 删除了旧版 "re-encoding itself, not the attention mechanism, is the operative factor" ✓
- Section 5: "Both cross-attention and MLP modules achieve comparable recovery (p = 0.15)" ✓
- Appendix F.3: MLP adapter 架构详细描述已补充（"3-layer feed-forward network with expansion ratio 4, using average pooling for token reduction"）✓

**R4-W3 [π₀ vs OpenVLA "most controlled comparison" 不成立] → [RESOLVED]**

- Grep 确认全文不再包含 "most controlled" 短语 ✓
- Section 4.4 尾部加了 caveat: "This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation." ✓
- Contribution 1: "though confounded by backbone differences (Appendix N)" ✓
- Appendix A (Pruning Protocol Details): "This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship" ✓

**R4-W4 [M=96 dip vs "flat M-curve"] → [RESOLVED]**

- Table 2 caption: ~~"flat"~~ → **"relatively stable"** ✓
- Section 4.5: "The M-curve is relatively stable" ✓
- Abstract: "relatively stable M-curve" ✓
- Appendix D: "The M=96 dip (mean 54.5% across three seeds) may reflect an intermediate bottleneck" → 提供了可能的解释 ✓

**R4-W5 [X-VLA "linear projection" 标签] → [RESOLVED]**

- Table 1 Connector 列：~~"Linear proj‡"~~ → **"Linear + BART (12L)‡"** ✓

---

## Part 2: 新发现的问题

### NEW-1 [warning] **π₀.5 在 k=0.85 的非单调 cliff 需要更多讨论**

- 具体位置：Section 4.4, paragraph 3
- 问题：新增数据显示 π₀.5 under random removal 在 LIBERO-Object 上出现极端非单调性：k=0.95 (69.4%) → k=0.85 (**5.0%**) → k=0.7 (77.2%)，72pp swing。这意味着移除 15% 的 token 导致崩溃，但移除 30% 反而恢复。Section 4.7 引入了 hypergeometric model H(N=768, C=91, T=6) 解释 cliff onset（RMSE=0.025），但该模型本质上预测：当移除更多 token 时，击中 critical token 的概率只会更高——因此无法解释 k=0.7 处的恢复。Section 5 坦承 "does not explain V-shape recovery at k≤0.7"，但这一承认不够：如果移除 30% token 的结果（77.2%）优于移除 15%（5.0%），这从根本上挑战了"每个 critical token 的移除都是不可逆损失"的前提，而 hypergeometric model 正是建立在这一前提上。

- 建议：(a) 在正文 Section 4.7 中增加一句明确说明模型的适用边界（"captures onset sharpness at high retention but does not generalize to moderate retention where compensatory mechanisms may emerge"）；(b) 讨论为什么 k=0.7 能恢复的可能机制（例如：大量 token 被移除后模型进入不同的计算 regime，或 position re-indexing 的影响）。

### NEW-2 [minor] **SmolVLA official checkpoint baseline 数字在不同位置不一致**

- Section 4.2: "57.2% SR unpruned"
- Table 2 (VTR results): "Official checkpoint (59.2% baseline)"
- Table 3 (Appendix B): 列出了两个评估协议（59.2% 和 57.2%）

原因是两个独立评估协议（A 和 B）给出了略有不同的 baseline。但正文 Section 4.2 仅提及 57.2%，而 Table 2 使用 59.2%（VTR 的 official checkpoint 对比行）。读者首次遇到时会困惑。建议在 Section 4.2 首次提及时写 "57.2%–59.2% SR across two evaluation protocols" 或类似表述。

### NEW-3 [minor] **Discussion section 可能过度压缩**

- Section 5 从旧版的 ~5 个 subsection、~3 页内容压缩为 2 段文字（~10 行）。虽然这解决了 R2 提出的超页问题（现在正文约 8 页），但旧版中几个有价值的 mechanistic insights（特别是 Section 5.1 "Connector Determines Token Independence" 对三种 connector 如何创造不同 token structure 的系统性分析）完全从正文消失。这些内容现在在 Appendix J（Connector Architecture and Token Independence），但正文的 Discussion 未给出足够的指引让读者意识到这些分析存在。

- 建议：在 Section 5 增加一句引导："Full mechanistic analysis of how connector architecture creates the observed independence structure appears in Appendix J."

### NEW-4 [minor] **hypergeometric model 的 C=91 参数来源**

- Section 4.7 引入 C=91（critical tokens）作为 hypergeometric model 的参数，但正文未解释这个数字是如何确定的。Appendix C.8 说 "C=91 critical tokens"，从 token importance heatmap 推导。C=91/768 ≈ 11.8% 的 token 被标记为 critical——这个比例的确定方法（阈值选择）决定了 cliff model 的预测。如果 C 是 post-hoc 拟合的自由参数，模型的预测力就弱于如果 C 有独立依据。建议在 Appendix C.8 中明确说明 C 的确定方法（是从 heatmap 用某个阈值得到的，还是从 SR 数据反向拟合的）。

---

## Part 3: 整体评估

### 修改质量总结

| Issue | 状态 | 修改质量 |
|-------|------|----------|
| R4-N1 SmolVLA baseline | RESOLVED | 多 k 值 + dual protocol，充分 |
| R4-N2 CV claim 降级 | RESOLVED | 全文一致，降级恰当 |
| R4-N3 π₀ offline-only | RESOLVED | Table 1 + Introduction + Results 三处到位 |
| R4-W1 cross-seed k=0.5 | RESOLVED | 3.4pp gap 已报告 |
| R4-W2 VTR p=0.15 | RESOLVED | 语言修正 + MLP 架构描述 |
| R4-W3 causal language | RESOLVED | "most controlled" 删除 + caveat 添加 |
| R4-W4 flat → stable | RESOLVED | 全文一致 |
| R4-W5 X-VLA label | RESOLVED | "Linear + BART (12L)" |

### 与 Round 4 对比的关键改进

1. **因果语言全面降级**：Grep 确认 "determines" 和 "falsifies" 已从所有活跃 tex 文件中移除，替换为 "strongly associated with"/"correlates with"/"demonstrates"。这是本轮最重要的系统性修改。

2. **正文大幅压缩**：从 ~13 页压缩到 ~8 页（Conclusion 略微溢出到第 9 页顶部几行）。Discussion 从 5 个 subsection 压缩为 2 段。大量内容（confounders, token position analysis, extended CV analysis, reencoding analysis）移入 Appendix。

3. **新增实证**：Cross-suite generalization（Section 4.7）、hypergeometric cliff model、token importance heatmaps、official checkpoint 完整 pruning 数据——这些不仅回应了审稿意见，还增加了论文的实质贡献。

4. **Abstract 重写**：新版 abstract 明确了 "evaluating four in closed-loop...analyzing three via offline/literature"、使用 "correlates" 而非 "predicts"、"relatively stable" 而非 "flat"。

### 是否存在矫枉过正？

Discussion section 的压缩略显过度（NEW-3），但考虑到页数限制这是合理的权衡。Contribution 2 从 "CV as dual predictor" 改为 "CV as diagnostic metric" 是恰当的降级，没有丢失核心信息。整体来说，修改校准良好——没有矫枉过正。

### Overall Score

**Round 4**: Borderline (倾向 weak reject)
**Round 5**: **Weak Accept**

**Confidence**: High

**理由**：Round 4 的三个 critical issues 全部 resolved，五个 should-fix 全部 resolved。论文现在的 claim 强度与数据支撑匹配：
- "Strongly associated" 而非 "determines"
- "Correlates with" 而非 "predicts"  
- "Demonstrates" 而非 "falsifies"
- π₀ 明确标注 offline-only
- Official checkpoint 有多 k 值验证

剩余弱点（hypergeometric model 的局限性、Discussion 过度压缩、N=3 模型的 CV 验证广度）是真实的局限，但不影响接收决定。论文对 CoRL 社区的核心价值——系统性揭示 VLA connector 与 pruning 行为的关联，并提供实用的 CV 诊断指标——是清晰的、有证据支撑的、且被适度表述的。NEW-1 关于 π₀.5 非单调 cliff 的问题值得 camera-ready 时补充讨论，但不构成额外的 must-fix。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 386 · 2026-05-22T08:13:56.065670+00:00_

Reviewer 1 Round 5 审稿已收到。关键发现：

- **Round 4 全部 8 个 issue：RESOLVED**
- **4 个新发现**：NEW-1（warning：π₀.5 非单调 cliff 与 hypergeometric model 矛盾）、NEW-2/3/4（minor）
- **评分**：Borderline weak reject → **Weak Accept**

等待 Reviewer 2 Round 5 审稿返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 32

## Round 32

8 recorded events


### User

_source line 387 · 2026-05-22T08:13:58.866695+00:00_

[Reviewer 1 审稿结果]:
Round 5 审稿报告已提交。

核心结论：Round 4 的全部 8 个 issues（3 critical + 5 warning）均已 **RESOLVED**。论文的因果语言、统计报告、claim 强度与数据支撑现已匹配。新增内容（cross-suite generalization、hypergeometric cliff model、official checkpoint 多 k 值验证）增强了贡献。发现 4 个新的 minor issues（π₀.5 非单调 cliff 解释不足、baseline 数字不一致、Discussion 过度压缩、C=91 来源不明），但均不影响接收决定。

评分从 **Borderline (weak reject)** 上调至 **Weak Accept**。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 5 审稿报告

---

## 1. Round 4 Issue 逐条验证

### Must-Fix (Critical)

**R4-N1 [因果声明 under-identified] → [RESOLVED]**

因果语言全文彻底降级，验证如下：
- **Abstract (p1):** "The vision connector is **strongly associated** with pruning behavior" ✓（原 "determines"）
- **Introduction C1 (p2):** "consistent with the connector being a primary factor, **though confounded by backbone differences** (Appendix N)" ✓
- **Figure 1 caption (p2):** "strongly associated with token compressibility" ✓
- **Section 4.5 (p7):** "This completion interleaves differences in connector, backbone, and encoder fusion, **limiting causal interpretation**" ✓
- **Section 5 Limitations (p8):** "preventing clean causal isolation (Appendix N)" ✓
- **Conclusion (p8):** "Token importance CV **correlates** with both tolerance class and optimal strategy" ✓
- **Appendix N (p25):** 新增完整 "Confounding Analysis"，逐条讨论 connector / backbone / encoder 混淆、seed 差异、within-connector vs cross-connector 比较的证据强度

全文未发现残留的 "determines" 因果语言。降级一致且彻底。

**R4-N2 [Taxonomy N=3 + CV predictor 样本不足] → [RESOLVED]**

Claim 降级充分：
- CV 从 "zero-cost dual **predictor**" 降为 "zero-cost **diagnostic metric** that **correlates** with" ✓
- Contribution C2 (p2): "Token importance CV **correlates** with both tolerance class and optimal pruning method" ✓
- Section 5 Limitations (p8): 明确承认 "the CV correlation spans **three models** and **two retention ratios**" ✓
- Related Work (p3): 新增 Q-Former [25]、Perceiver [32]、Flamingo [26]、RoboFlamingo [8] 作为 cross-attention connector 类别的讨论，并讨论了它们与 taxonomy 的关系 ✓
- **新增 Appendix K (p23-24):** "CV as Diagnostic Metric: Extended Analysis" 扩展讨论了 CV 的连续谱特性以及 X-VLA 作为 intermediate case

Taxonomy 本身仍然是 4 类 / 3 connector 类型，但 claims 已恰当限定。Perceiver/Q-Former 未纳入实验但在 Related Work 中作为 limitation 讨论。

**R4-N3 [纯仿真评估 vs CoRL 要求] → [RESOLVED]**

（Director Round 4 降为 should-fix）
- Section 5 Limitations (p8): "All closed-loop experiments use **LIBERO simulation**" 明确承认 ✓
- **新增 Section 4.7 Cross-Suite Generalization (p8):** 在 LIBERO-Object 之外验证了 Spatial 和 Goal 两个任务 suite，展示 cliff 行为的 suite 依赖性，部分回应了 generalizability 关切
- Appendix D (p17): Smart Compress 跨 3 个 suite 的 per-task 结果
- 未新增 sim-to-real transferability 的专门讨论，但 simulation-only 已作为 limitation 明确列出

考虑到 Director 的降级决定和论文的改善，标记为 resolved。但仍希望 camera-ready 版补充一段 sim-to-real transferability 讨论（即使仅引用他人工作的 sim-to-real 结论）。

### Should-Fix (Warning)

**R4-W1 ["Falsifies immune assumption"] → [RESOLVED]**

- 全文搜索未发现 "falsifies" 或 "falsify"
- Abstract (p1) 保留了 "low-CV models are not immune to pruning but uniformly critical"，但这是描述性表述，不再将 "immune" 归因于先前文献的声明
- Section 4.4 (p6) 改为 "low CV does not imply tokens are dispensable; it implies uniform criticality" ✓
- 稻草人论证问题已解决

**R4-W2 [VTR 新颖性有限] → [RESOLVED]**

- Contribution C3 (p2): "forms a **diagnostic protocol**" ✓（原 "framework"）
- Section 4.5 (p7): VTR 定位为实用的 diagnostic tool，不再声称架构新颖性
- Appendix L (p19): MLP adapter 对照实验保留，evidence 结构合理
- **Page 27 新增官方 checkpoint 对比：** Smart Compress M=32 达到 60.1±1.3% vs 官方 59.2%（CI [54.8%, 63.4%]），t-test p≈0.72 不显著。论文诚实表述："The primary contribution of VTR is recovering functional performance where all deletion methods yield 0%, not matching the official baseline." 这是恰当的定位。

**R4-W3 ["七个模型" framing 夸大] → [RESOLVED]**

- Table 1 (p5): π₀ 行有明确脚注 "†π₀ reports offline normalized L1 action loss (pending closed-loop evaluation)"；CogACT 行有脚注 "†literature result from EfficientVLA [22], not our evaluation" ✓
- Abstract (p1) 仍说 "seven VLA models" 但未强调全部为 closed-loop，结合 Table 1 脚注已足够透明
- Appendix N (p25) 进一步讨论了不同模型的评估协议差异

**R4-W4 ["Framework" 过度包装] → [RESOLVED]**

全文 "framework" 已替换为 "diagnostic protocol"：
- Abstract (p1): "forms a diagnostic protocol" ✓
- Contribution C3 (p2): "diagnostic protocol" ✓
- Conclusion (p8): 未使用 "framework" ✓

**R4-W5 [正文超页] → [RESOLVED]**

- Pages 1-8: 正文（Abstract → Section 6 Conclusion）✓
- Page 9 起: References
- Page 12 起: Appendix A-R
- 符合 CoRL 8 页正文 + 附录/引用不计限制 ✓

---

## 2. 新发现的问题

### 2.1 Section 4.7 Cross-Suite Generalization 评估

**新增贡献：** Section 4.7 (p8) 引入了 hypergeometric cliff model R(N=504, C=r₀, T=46, c) 来形式化 SmolVLA 的 cliff 行为。模型预测 cliff onset 在 k∈[0.899, 0.926]，RMSE=0.025。通过对比 Object (c*=91) vs Spatial (c*=5) 的 concentrated criticality 差异解释了 suite 间的 cliff profile 不同。

**评价：**
- (+) 将定性的 "cliff" 观察提升为定量可测试的假说，是有意义的分析深化
- (+) Cross-suite validation（Object / Spatial / Goal, Table 9 p17）提供了超出 LIBERO-Object 的 generalization evidence
- (+) Limitations 中诚实承认 "hypergeometric cliff model captures onset sharpness (RMSE = 0.025) but does not explain V-shape recovery at k ≤ 0.7"
- (−) 模型仅在一个架构（SmolVLA）× 两个 suite 上验证。c* 参数从 5 到 91 的变化范围很大，但仅有 2 个数据点来 "验证" 模型的 suite 泛化能力
- (−) 是否过拟合？4 个参数（N, C, T, c）拟合 2 个 suite 的 cliff profile——参数数量接近数据点数量

**判断：** 不构成新的 must-fix。模型定位恰当（explanatory, 非 predictive），Limitations 承认了局限。但 camera-ready 应明确 c* 是 post-hoc fitted 还是 independently measurable。如果 c* 可以从 attention heatmap 独立计算（Figure 4 暗示可以），那模型就有真正的预测价值；如果是拟合出来的，就只是 curve fitting。

### 2.2 Related Work 扩展程度

Round 4 建议增加 15+ citations。实际增加约 5 篇（41→~46）。但检查后发现：
- Round 1 已引用了大部分 key works（Compressor-VLA, SpecPrune-VLA, LightVLA, See What Matters, VLA-IAP, EfficientVLA, VLA-Pruner, VLA-Cache, Don't Run with Scissors）
- 新增的引用补充了 cross-attention connector 和 vision token compression 的覆盖
- Related Work 段落本身重写/扩展了 concurrent works 讨论（p3），特别是 Don't Run with Scissors 的 "recover via fine-tuning" 定位与本文的 "diagnose connector" 定位之间的区分
- **判断：** 覆盖度足够。数量未达 15 篇但 quality 和 relevance 到位。

### 2.3 Positioning 转型评估

从 "framework paper" 到 "diagnostic empirical study" 的转型整体成功：
- 所有 overclaiming 语言降级到位
- Limitations 部分（p8）是我审过的论文中最诚实的之一——明确列出仿真-only、N=3 connector、CV 样本量、π₀ offline-only、hypergeometric 模型局限
- Appendix N 的 confound analysis 是实质性的分析而非走过场
- VTR 从 "novel architecture" 重新定位为 "diagnostic tool showing re-encoding overcomes the cliff"

**残余小问题：** Section 4.4 (p6) "All tokens carry equal weight, removing any token equals removing all of them" 是一个未经证明的强声明。CV≈0.04 说明 importance 近似均匀，但 "removing any = removing all" 是逻辑跳跃，应改为 "near-uniform importance makes the model unable to identify dispensable tokens"。

### 2.4 标题适配性

标题 "Why Token Pruning **Crashes** Some Robot Policies but Not Others" 在 claim 降级后仍然合适：
- "Crashes" 是对 empirical phenomenon 的准确描述（SmolVLA 5% removal → 0% SR，π₀.5 10% removal → ≤5% SR）
- 副标题 "Vision Connectors and VLA Token Compressibility" 不含因果声明
- 正文不再声称 connector "determines" 而是 "is associated with"
- **判断：** 标题可接受，无需修改

---

## 3. Overall Score

### 与 Round 4 对比

| 维度 | Round 4 | Round 5 | 变化理由 |
|------|---------|---------|--------|
| Originality | 2/5 | 2.5/5 | Cross-suite generalization + hypergeometric model 增加了分析深度；但 N=3 connector 的基本限制未变 |
| Quality | 3.5/5 | 4/5 | 因果语言降级、confound analysis (Appendix N)、Limitations 改善显著提升了 methodological rigor |
| Clarity | 4/5 | 4/5 | 写作质量保持高水平，8 页压缩后结构紧凑 |
| Significance | 2.5/5 | 3/5 | Cross-suite validation 和官方 checkpoint 对比增强了 practical relevance |
| Relevance | 3/5 | 3/5 | 仍为 simulation-only，但已明确承认 |
| Limitations | 3/5 | 4.5/5 | Limitations section 现在是典范级别的诚实——逐条列出所有已知局限 |

### Overall Score: **Borderline** (leaning weak accept)
### Confidence: **High**

**与 Round 4 对比：Weak Reject → Borderline，上调一档。**

**理由：** 论文在五个 round 中展现了出色的迭代改进能力。Round 4 的所有 must-fix 和 should-fix issues 均已 resolved。核心改善：

1. **诚实的定位：** 从 overclaiming "framework" + "determines" 转型为恰当 scoped 的 "diagnostic empirical study" + "associated with"
2. **新增分析深度：** Section 4.7 cross-suite generalization + hypergeometric cliff model 提供了超越 descriptive observation 的 analytical contribution
3. **Confound transparency：** Appendix N 是实质性的方法论贡献，而非敷衍的 caveat

**仍然存在的 fundamental limitations（不阻碍接收但限制 impact）：**
- N=3 connector 类型仍然是核心瓶颈——在 rebuttal 或 camera-ready 中增加 Perceiver-based VLA 将显著增强说服力
- Simulation-only 仍是 CoRL venue fit 的短板，但论文定位为 "diagnostic analysis" 而非 "system deployment"，部分缓解了此问题
- VTR 贡献仍然 incremental，但定位已诚实

**给 AC 的建议：** 如果需要在 borderline 论文中做取舍，本文的优势在于：(1) 覆盖广度（7 models, 3 connectors, 3 suites）在该领域无出其右，(2) negative results（linear projection 不可 prune）有高实用价值，(3) Limitations 的诚实度高于平均水平。劣势在于 simulation-only 和 N=3 的 inherent limitation。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-22T08:14:12.844893+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-22T08:14:12.859690+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 14
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-22T08:14:34.911957+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "# 交叉分享：Reviewer 2 的 Round 5 审稿意见\n\n请逐条回应 Reviewer 2 的新发现，使用 [AGREE] 或 [REBUT] 标记。\n\n---\n\n## R2 新发现摘要\n\n**R2-2.1 [Section 4.7 hypergeometric model]**\n- (+) 将定性 cliff 观察提升为定量假说，有意义\n- (+) Cross-suite validation 提供了泛化证据\n- (−) 模型仅在 SmolVLA × 2 suite 上验证，c* 从 5 到 91 变化但仅 2 个数据点\n- (−) 4 参数拟合 2 suite 的 cliff profile，接近过拟合\n- 判断：不构成 must-fix，但 camera-ready 应明确 c* 是 post-hoc fitted 还是 independently measurable\n\n**R2-2.3 残余小问题**\nSection 4.4 \"All tokens carry equal weight, removing any token equals removing all of them\" 是未经证明的强声明。建议改为 \"near-uniform importance makes the model unable to identify dispensable tokens\"。\n\n**R2-2.2 Related Work**\nRound 4 建议增加 15+ citations，实际增加约 5 篇。但 quality 和 relevance 到位，覆盖度足够。\n\n**R2 评分：Borderline (leaning weak accept)，从 Weak Reject 上调一档。**\n\n---\n\n请对比你自己的 Round 5 发现（NEW-1 到 NEW-4），对 R2 的每个观点给出 [AGREE] 或 [REBUT]，特别关注：\n1. 你的 NEW-1（π₀.5 非单调 cliff）与 R2-2.1（hypergeometric model 过拟合）是否指向同一问题？\n2. R2 的 \"removing any = removing all\" 语言修正建议是否合理？\n3. 两人评分差异（你 Weak Accept vs R2 Borderline leaning weak accept）——你是否维持原评分？",
  "reviewer_id": "1",
  "project": "importance_margin_vla_compress",
  "round_number": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "# 交叉分享：Reviewer 2 的 Round 5 审稿意见\n\n请逐条回应 Reviewer 2 的新发现，使用 [AGREE] 或 [REBUT] 标记。\n\n---\n\n## R2 新发现摘要\n\n**R2-2.1 [Section 4.7 hypergeometric model]**\n- (+) 将定性 cliff 观察提升为定量假说，有意义\n- (+) Cross-suite validation 提供了泛化证据\n- (−) 模型仅在 SmolVLA × 2 suite 上验证，c* 从 5 到 91 变化但仅 2 个数据点\n- (−) 4 参数拟合 2 suite 的 cliff profile，接近过拟合\n- 判断：不构成 must-fix，但 camera-ready 应明确 c* 是 post-hoc fitted 还是 independently measurable\n\n**R2-2.3 残余小问题**\nSection 4.4 \"All tokens carry equal weight, removing any token equals removing all of them\" 是未经证明的强声明。建议改为 \"near-uniform importance makes the model unable to identify dispensable tokens\"。\n\n**R2-2.2 Related Work**\nRound 4 建议增加 15+ citations，实际增加约 5 篇。但 quality 和 relevance 到位，覆盖度足够。\n\n**R2 评分：Borderline (leaning weak accept)，从 Weak Reject 上调一档。**\n\n---\n\n请对比你自己的 Round 5 发现（NEW-1 到 NEW-4），对 R2 的每个观点给出 [AGREE] 或 [REBUT]，特别关注：\n1. 你的 NEW-1（π₀.5 非单调 cliff）与 R2-2.1（hypergeometric model 过拟合）是否指向同一问题？\n2. R2 的 \"removing any = removing all\" 语言修正建议是否合理？\n3. 两人评分差异（你 Weak Accept vs R2 Borderline leaning weak accept）——你是否维持原评分？",
    "reviewer_id": "1",
    "project": "importance_margin_vla_compress",
    "round_number": "5"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-22T08:14:50.657932+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15745
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-22T08:14:50.859426+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "# 交叉分享：Reviewer 1 的 Round 5 审稿意见\n\n请逐条回应 Reviewer 1 的新发现，使用 [AGREE] 或 [REBUT] 标记。\n\n---\n\n## R1 新发现摘要\n\n**R1-NEW-1 [warning] π₀.5 非单调 cliff**\n- π₀.5 在 LIBERO-Object 上：k=0.95 (69.4%) → k=0.85 (5.0%) → k=0.7 (77.2%)，72pp swing\n- hypergeometric model 预测移除更多 token 时击中 critical token 概率只会更高，无法解释 k=0.7 恢复\n- Section 5 承认 \"does not explain V-shape recovery at k≤0.7\" 但不够充分\n- 建议：(a) 正文 Section 4.7 增加模型适用边界说明；(b) 讨论 k=0.7 恢复的可能机制\n\n**R1-NEW-2 [minor] SmolVLA baseline 数字不一致**\n- Section 4.2: \"57.2% SR\"，Table 2: \"59.2% baseline\"，Appendix Table 3: 两个协议（59.2% / 57.2%）\n- 建议首次提及时写 \"57.2%–59.2% across two evaluation protocols\"\n\n**R1-NEW-3 [minor] Discussion 过度压缩**\n- 从 ~3 页压缩为 2 段（~10 行），旧版 mechanistic insights 完全消失\n- 建议增加一句引导到 Appendix J 的 pointer\n\n**R1-NEW-4 [minor] C=91 参数来源不明**\n- hypergeometric model 的 C=91 critical tokens 是 post-hoc 拟合还是独立测量？\n- 建议在 Appendix C.8 明确确定方法\n\n**R1 评分：Weak Accept，从 Borderline (weak reject) 上调。**\n\n---\n\n请对比你自己的 Round 5 发现，对 R1 的每个观点给出 [AGREE] 或 [REBUT]，特别关注：\n1. R1-NEW-1 的 V-shape recovery 问题——你是否同意这比你的 \"c* 过拟合\" 担忧更严重？\n2. R1-NEW-2 baseline 不一致——你是否注意到同一问题？\n3. R1-NEW-4 与你的 R2-2.1 是否指向同一根本问题（C/c* 参数的确定方法）？\n4. 两人评分差异（R1 Weak Accept vs 你 Borderline leaning weak accept）——你是否调整评分？",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress",
  "round_number": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "# 交叉分享：Reviewer 1 的 Round 5 审稿意见\n\n请逐条回应 Reviewer 1 的新发现，使用 [AGREE] 或 [REBUT] 标记。\n\n---\n\n## R1 新发现摘要\n\n**R1-NEW-1 [warning] π₀.5 非单调 cliff**\n- π₀.5 在 LIBERO-Object 上：k=0.95 (69.4%) → k=0.85 (5.0%) → k=0.7 (77.2%)，72pp swing\n- hypergeometric model 预测移除更多 token 时击中 critical token 概率只会更高，无法解释 k=0.7 恢复\n- Section 5 承认 \"does not explain V-shape recovery at k≤0.7\" 但不够充分\n- 建议：(a) 正文 Section 4.7 增加模型适用边界说明；(b) 讨论 k=0.7 恢复的可能机制\n\n**R1-NEW-2 [minor] SmolVLA baseline 数字不一致**\n- Section 4.2: \"57.2% SR\"，Table 2: \"59.2% baseline\"，Appendix Table 3: 两个协议（59.2% / 57.2%）\n- 建议首次提及时写 \"57.2%–59.2% across two evaluation protocols\"\n\n**R1-NEW-3 [minor] Discussion 过度压缩**\n- 从 ~3 页压缩为 2 段（~10 行），旧版 mechanistic insights 完全消失\n- 建议增加一句引导到 Appendix J 的 pointer\n\n**R1-NEW-4 [minor] C=91 参数来源不明**\n- hypergeometric model 的 C=91 critical tokens 是 post-hoc 拟合还是独立测量？\n- 建议在 Appendix C.8 明确确定方法\n\n**R1 评分：Weak Accept，从 Borderline (weak reject) 上调。**\n\n---\n\n请对比你自己的 Round 5 发现，对 R1 的每个观点给出 [AGREE] 或 [REBUT]，特别关注：\n1. R1-NEW-1 的 V-shape recovery 问题——你是否同意这比你的 \"c* 过拟合\" 担忧更严重？\n2. R1-NEW-2 baseline 不一致——你是否注意到同一问题？\n3. R1-NEW-4 与你的 R2-2.1 是否指向同一根本问题（C/c* 参数的确定方法）？\n4. 两人评分差异（R1 Weak Accept vs 你 Borderline leaning weak accept）——你是否调整评分？",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress",
    "round_number": "5"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-22T08:14:54.370320+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3510
}
```

</details>

---


### Assistant

_source line 394 · 2026-05-22T08:15:03.051987+00:00_

交叉分享已发送。两位 Reviewer 将逐条回应对方的新发现，重点比对：
- hypergeometric model 的 V-shape recovery 解释缺失 vs 过拟合风险（R1-NEW-1 / R2-2.1）
- C=91 参数来源（R1-NEW-4 / R2-2.1 同一根本问题）
- 评分差异收敛（R1 Weak Accept vs R2 Borderline leaning weak accept）

等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 395 · 2026-05-22T08:15:04.565691+00:00_

[Reviewer 2 审稿结果]:
Round 5 审稿完成。

**核心结论：** Round 4 的 6 个 must-fix/should-fix issues 全部 **[RESOLVED]**。因果语言降级彻底（"determines"→"strongly associated with"），CV 定位从 "predictor" 降为 "diagnostic metric that correlates with"，"framework" 替换为 "diagnostic protocol"，正文压缩至 8 页，新增 confound analysis（Appendix N）和 cross-suite generalization（Section 4.7）。

评分从 **Weak Reject → Borderline (leaning weak accept)**，上调一档。论文展现了出色的迭代改进能力和少见的 Limitations 诚实度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 396 · 2026-05-22T08:15:08.856765+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 397 · 2026-05-22T08:16:21.296751+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 Round 5 新发现的逐条回应

---

## R2-2.1 [Hypergeometric cliff model]

**[AGREE] 整体方向——但我和 R2 指向的是同一个问题的不同面。**

R2 的关注点是**过拟合**："4 参数拟合 2 suite 的 cliff profile，c* 从 5 到 91 变化但仅 2 个数据点"。我在 R1-NEW-1 中的关注点是**模型的解释力缺口**：hypergeometric model 本质上预测"移除越多 token → 命中 critical token 概率越高 → 性能越差"，但 π₀.5 的实际数据显示 k=0.85 (5.0% SR) 远差于 k=0.7 (77.2% SR)——移除更多 token 反而更好。这从根本上违反了模型的单调假设。

两者指向同一根本问题：hypergeometric model 是对 cliff onset 的有用描述性工具，但不是一个可推广的预测模型。具体地：

1. **R2 的过拟合论证是正确的**。N=768, C, T 三个参数中，C 是 per-suite 拟合的自由参数（Object: C=91, Spatial: C≈5），T 由 k 值决定。用 1 个自由参数拟合 1 条 cliff curve 的 onset 位置，统计上无法区分真实预测力和曲线匹配。R2 建议在 camera-ready 时明确 C 是 post-hoc fitted 还是 independently measurable——我同意这一建议，且在 R1-NEW-4 中也独立提出了同样的问题。

2. **我的 V-shape recovery 问题是更深层的缺陷**。即使 C 的拟合过程没问题，模型仍然无法解释为什么 k=0.7 恢复到 77.2%。论文在 Section 5 承认了这一点（"does not explain V-shape recovery at k≤0.7"），但 Section 4.7 正文中对模型的呈现过于正面（"RMSE=0.025"），可能给读者留下模型完善的错误印象。RMSE=0.025 仅衡量 cliff onset 附近的拟合质量，不反映 k<0.85 区间的失败。

3. **但两人都同意这不构成 must-fix**。hypergeometric model 是新增内容（Round 4 中不存在），它增加了论文的分析深度，即使有局限。Camera-ready 增加一句 "The model is fit to per-suite critical token counts; independent measurement of C (e.g., from attention maps or ablation) would strengthen its predictive validity" 即可。

---

## R2-2.3 ["All tokens carry equal weight" 语言修正]

**[REBUT] R2 误引了原文，但修正方向部分合理。**

R2 称 Section 4.4 有 "All tokens carry equal weight, removing any token equals removing all of them" 的表述。实际原文是（results.tex line 54）：

> "Because all tokens carry equal weight, removing 90% at random preserves spatial coverage and the model compensates."

R2 的引文与原文含义相反：
- 原文说的是：equal weight → random removal **保持** spatial coverage → model compensates（正面结果）
- R2 的引文说的是：equal weight → removing any = removing all（灾难性结果）

所以 R2 对论文 claim 的理解有误，原文在此处的逻辑是自洽的——π₀ 在 k=0.1 offline loss 改善 2.4% 正是因为 random removal 保持了 coverage。

**但 R2 的修正方向有合理之处**："all tokens carry equal weight" 是从 CV=0.038（near-uniform L2 norms）推导出的，而 L2 norm 均匀不等同于 task-relevant information 均匀。更准确的表述应为 "CV=0.038 indicates near-uniform L2 norms, suggesting comparable per-token information density" 而非直接等同于 "equal weight"。这是措辞精确度的问题，不是逻辑错误。

建议：将 "all tokens carry equal weight" 改为 "near-uniform L2 norms (CV=0.038) suggest that no token subset carries disproportionate information, so random removal preserves spatial coverage"。

---

## R2-2.2 [Related Work citations]

**[AGREE]** 

R2 指出 Round 4 建议增加 15+ citations 但实际增加约 5 篇，但认为 quality 和 relevance 到位。我同意——审稿的目标不是计数 citations，而是确保关键 related work 被覆盖。当前的 Related Work 覆盖了 ViT pruning、VLM token reduction、VLA-specific works、vision connectors 四个层面，对本文定位的区分度足够。

---

## 评分差异分析

| | R1 | R2 |
|---|---|---|
| Round 4 | Borderline (leaning weak reject) | Weak Reject (borderline) |
| Round 5 | **Weak Accept** | **Borderline (leaning weak accept)** |
| 变化幅度 | +1 档 | +1 档 |

两人均上调一档，且方向一致。差异主要来自两个维度：

1. **Venue fit（sim-only for CoRL）**：R2 在 Round 4 将此列为 critical issue（N3），虽然我 rebutted 了 R2 引用的 CoRL policy 的准确性，但 R2 可能仍将 sim-only 作为降分因素。我对此的权重更低——认为架构理解类研究需要仿真的控制性。

2. **VTR novelty**：R2 认为 VTR 本质是 Perceiver/Q-Former 的 VLA 应用，novelty 有限。我同意这一判断但对其影响评分的权重较低——论文的主要贡献在诊断（taxonomy + CV），VTR 是配套 remedy 而非核心 contribution。

**我维持 Weak Accept 评分。**

核心依据：
- 8/8 Round 4 issues 全部 resolved，修改质量一致且校准良好
- 因果语言的系统性降级（determines → associated, predicts → correlates, falsifies → demonstrates）体现了对审稿意见的认真对待
- 新增内容（cross-suite, heatmaps, confounders appendix）增加了实质价值
- 剩余弱点（hypergeometric model 局限、N=3 CV 验证、Discussion 压缩）均为 camera-ready 可修复项，不影响接收决定
- 论文对 CoRL 社区的核心价值——揭示 connector type 与 pruning 行为的系统性关联，提供 CV 作为零成本诊断指标——清晰、有证据支撑、且被适度表述

如果 R2 也在 borderline 倾向 accept 的位置，两人的实质分歧很小。共同的 camera-ready 建议（hypergeometric C 的来源说明、π₀.5 V-shape 的讨论补充、"equal weight" 措辞精确化）可以作为 conditional accept 的 meta-review 条件。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 398 · 2026-05-22T08:16:31.512247+00:00_

R1 交叉回应已收到。等待 R2 交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 35

## Round 35

14 recorded events


### User

_source line 399 · 2026-05-22T08:16:32.917511+00:00_

[Reviewer 1 审稿结果]:


---

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 Reviewer 1 Round 5 新发现

---

## 逐条回应

**[AGREE] R1-NEW-1: π₀.5 非单调 V-shape recovery (k=0.95→69.4%, k=0.85→5.0%, k=0.7→77.2%)**

强烈同意，且认为这比我自己提出的 "c* 过拟合" 担忧更严重。理由：

1. **问题层次不同。** 我的 R2-2.1 关注的是 hypergeometric model 的统计效力（4 参数拟合 2 个 suite），这是 model validation 问题。R1-NEW-1 指出的是模型的 **explanatory scope** 缺陷——一个 monotonic collapse probability 模型在逻辑上就无法解释非单调恢复。这是结构性的，不是样本量可以解决的。

2. **72pp swing 是一个值得独立讨论的经验现象。** π₀.5 在 k=0.85 崩溃到 5% 但在 k=0.7 恢复到 77.2%，这暗示存在某种 regime transition——可能在极端压缩下模型 "放弃" 视觉信息转而依赖语言/proprioception prior，或者 L2 ranking 在不同 k 值下的 effective selection pattern 发生质变（例如极端压缩下 L2 选出的 token subset 反而覆盖了更多 unique spatial regions）。论文 Section 5 Limitations 一句带过 "does not explain V-shape recovery at k ≤ 0.7" 确实不够。

3. **对 actionability 的影响。** 如果 practitioner 按照 CV diagnostic protocol 指导在 k=0.85 处 prune π₀.5，会得到 5% SR；但继续 prune 到 k=0.7 反而可用。这种非单调性直接削弱了 "CV correlates with optimal strategy" 的实用性——因为最优 k 值不是从 CV 单调推导的。

**建议：** Section 4.7 应增加 1-2 句明确 hypergeometric model 的适用边界（"valid for cliff onset prediction near the critical threshold; does not model recovery regimes"），并在 Section 4.4 或 Appendix 讨论 V-shape 的可能机制（即使是 speculative 也比沉默好）。

**[AGREE] R1-NEW-2: SmolVLA baseline 数字不一致 (57.2% vs 59.2%)**

我在 Round 5 审稿中未单独标记这个问题，是我的疏漏。Section 4.2 的 "57.2%" 与 Table 2 的 "59.2% baseline" 之间的差异如果来自不同评估协议（例如不同 seed、不同 episode 数、不同 LIBERO 版本），应在首次提及时明确说明。R1 建议的 "57.2%–59.2% across two evaluation protocols" 是清晰且低成本的修复。

同时，这类看似小的数字不一致在 peer review 中容易引发 "数据管理不严" 的信任疑虑——特别是当论文的核心贡献是 quantitative comparison 时。Camera-ready 必须统一。

**[AGREE] R1-NEW-3: Discussion 过度压缩**

同意这是 8 页压缩的一个代价。旧版 Section 5 约 3 页（pages 11-13），包含 connector mechanism 的 mechanistic interpretation、CV 的连续谱讨论、re-encoding 成功的原因分析。现在压缩为 2 段约 10 行，这些 insight 完全消失于正文。

论文已将相关内容移入 Appendix J-K，但正文没有显式指引。增加一句 "For extended mechanistic analysis, see Appendices J–K" 是零成本的改善。

**[AGREE] R1-NEW-4: C=91 参数来源不明**

完全同意，且这与我 R2-2.1 中 "camera-ready 应明确 c* 是 post-hoc fitted 还是 independently measurable" 的关注是**同一根本问题的两种表述**。

R1 问的是 "C=91 是拟合还是独立测量"，我问的是 "c* 能否从 attention heatmap 独立计算"。本质上：如果 c* 可以从 Figure 4 的 attention heatmap 独立量化（例如定义一个 threshold 计算 "concentrated critical tokens" 的数量），那 hypergeometric model 就有独立的预测价值；如果 c* 是通过最小化 RMSE 从 collapse curve 反向拟合的，那模型就退化为 curve fitting，没有独立验证。

两位 reviewer 独立收敛于同一问题，说明这是论文应在 camera-ready 中优先 clarify 的点。

---

## 评分差异讨论

**R1: Weak Accept | R2 (我): Borderline (leaning weak accept)**

两人均从 Round 4 上调一档，方向一致。半档差异来源：

1. **我对 N=3 connector 的 inherent limitation 权重略高。** Taxonomy 和 CV diagnostic 是论文的两个核心 contribution，都建立在 3 个 connector 类型上。即使 claim 降级到位，这个 sample size 对 CoRL reviewer 来说仍是一个可预见的批评点。R1 似乎认为 claim 降级充分弥补了这一点；我认为降级是必要条件但非充分条件。

2. **Simulation-only 的 venue fit 权重。** R1 升至 weak accept 暗示认为 CoRL 可以接受 simulation-only 的 diagnostic study；我对此稍保守——CoRL CFP 明确要求 "real-robot experiments or convincing evidence that simulation experiments are transferable to real robots"，论文未提供 transferability evidence。

3. **VTR 贡献的评估。** 我们一致认为 VTR incremental 但定位诚实。但 VTR 的 t-test p≈0.72（vs 官方 checkpoint）意味着恢复效果与官方 baseline 无统计差异——这既是优点（"能恢复到 baseline 水平"）也是弱点（"没有实质提升"）。

**是否调整评分：** 不调整。我维持 **Borderline (leaning weak accept)**。与 R1 的半档差异反映了对 simulation-only venue fit 和 N=3 limitation 的合理不同权重。两人的实质判断一致：论文在 intensive revision 后达到了 borderline acceptable 的水平，所有 overclaiming 已修复，remaining limitations 是 inherent 的而非 sloppy 的。

**给 AC 的建议保持不变：** 如果 conference 需要在 borderline 论文中取舍，本文的核心价值在于 (1) 跨架构覆盖的广度无出其右，(2) negative results 有高实用价值，(3) Limitations 的诚实度高于平均水平。主要 risk 是 CoRL audience 可能期望 real-robot validation。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-22T08:16:55.040035+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-22T08:16:55.090893+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-22T08:16:58.620216+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-22T08:16:59.072125+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T08:06:14.044094+00:00\", \"completed_at\": \"2026-05-22T08:08:56.257100+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 17\", \"message\": \"Figure 4 为占位符——显示 \\\"[Placeholder: token importance heatmap]\\\" 灰底文字框，未替换为实际图片。已提交的论文中出现 placeholder 是严重疏忽，审稿人会立即注意到。必须在 camera-ready 前替换为实际 token importance heatmap 可视化。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 3-4\", \"message\": \"连续 2 页纯文本（Related Work + Methods 开头），无任何 display item（figure/table/equation）。虽然内容性质使然，但审稿人快速翻阅时可能感到单调。建议考虑在 Method 段插入一个关键公式的 display math 或小型示意图来打破纯文本节奏。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-9\", \"message\": \"正文仅 4 个 display items（2 figures + 2 tables），对于实证为主的论文偏少。核心实验结果（如 per-task breakdown、pruning curves）大量放在附录中，正文缺乏直观的数据可视化。建议将附录中的 Figure 3（cross-suite pruning profiles）或一个关键 per-task 表格提升到正文。\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"整页纯文本分析，夹在 Table 1（p5）和 Table 2（p7）之间。虽然分析内容重要，但视觉上缺乏锚点，审稿人可能跳过细节。\"}, {\"severity\": \"warning\", \"dimension\": \"page 27\", \"message\": \"末页底部约 35% 空白。虽然这是附录最后一页，影响较小，但可通过调整前文间距或添加内容来充分利用空间。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 的两个子图 axis label 和 legend 字号偏小（约正文 60-65%），在打印或缩放查看时可能不够清晰。建议放大至正文字号的 70%+。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 格式良好——booktabs 风格、最优值加粗、CI 区间标注清晰。全文表格风格一致，是亮点。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 架构图清晰专业，颜色区分度好（蓝色/绿色区分两种架构），caption 自包含。作为审稿人的第一视觉锚点效果很好。\"}, {\"severity\": \"info\", \"dimension\": \"pages 13-15\", \"message\": \"附录表格密度高（每页 2 个表格），per-task breakdown 数据完整。但部分表格列数较多（Table 6 有 7 列含多个 removal ratio），可考虑是否需要全部展示。\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"Figure 7（per-layer attention entropy）双面板图，配色方案清晰（蓝/橙/绿区分三个模型），与 Figure 2 颜色语义基本一致。\"}, {\"severity\": \"info\", \"dimension\": \"pag
…[truncated 171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-22T08:16:59.072687+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "artifacts/review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "artifacts/review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-22T08:16:59.125478+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-22T08:17:03.445838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-22T08:17:03.496755+00:00_

1	- id: "R4-C1"
2	  summary: "Causal claim under-identified — connector vs backbone/encoder/action confound"
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 4
7	  last_seen_round: 4
8	  mentions:
9	    - {round: 4, reviewers: "R1+R2 consensus", note: "determines needs downgrade to associated with"}
10	  action_items:
11	    - {round: 4, action: "Full-text causal language downgrade (determines→associated, controlled→closest available)", assigned_to: "paper_agent", status: "done"}
12	  resolution: "All causal language downgraded: determines→associated, controlled→closest available, immunity→dispensable, operative mechanism→key factor. Not immune retained in intro/conclusion (negation, core finding)."
13	  resolution_round: 4
14	
15	- id: "R4-C2"
16	  summary: "SmolVLA baseline 44.8% vs official 87.3% — cliff and VTR on undertrained checkpoint"
17	  category: experiment
18	  severity: critical
19	  status: resolved
20	  first_raised_round: 4
21	  last_seen_round: 4
22	  mentions:
23	    - {round: 4, reviewers: "R1+R2 consensus", note: "Official checkpoint full pruning sweep is minimum requirement"}
24	  action_items:
25	    - {round: 4, action: "SmolVLA official checkpoint pruning sweep (10 configs)", assigned_to: "main_agent", status: "done", note: "D148: baseline 57.2%, L2norm k=0.9=0%, k=0.5=0%, random k=0.95=0%. All pruning=0%. seed43 running."}
26	    - {round: 4, action: "Write official results into paper", assigned_to: "paper_agent", status: "done", note: "Integrated into results.tex §4.1 main text + appendix dual-protocol table."}
27	  resolution: "Official HF checkpoint (57.2% baseline) shows identical 0% cliff at all pruning configs. Cliff is architectural, not training artifact. Data in main text Results section."
28	  resolution_round: 4
29	
30	- id: "R4-C3"
31	  summary: "CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal"
32	  category: framing
33	  severity: critical
34	  status: resolved
35	  first
…[truncated 8864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-22T08:19:10.493639+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "issues_yaml": "- id: \"R4-C1\"\n  summary: \"Causal claim under-identified — connector vs backbone/encoder/action confound\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"determines needs downgrade to associated with\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — full-text causal language downgrade confirmed. No residual 'determines' found.\"}\n  action_items:\n    - {round: 4, action: \"Full-text causal language downgrade (determines→associated, controlled→closest available)\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Round 5 verified: determines→strongly associated with, predicts→correlates, falsifies→demonstrates. Appendix N confound analysis added. Both reviewers confirm thorough and consistent.\"\n  resolution_round: 5\n\n- id: \"R4-C2\"\n  summary: \"SmolVLA baseline 44.8% vs official — cliff and VTR on undertrained checkpoint\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Official checkpoint full pruning sweep is minimum requirement\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — official checkpoint (57.2% baseline) multi-k verification complete. Dual evaluation protocol in Appendix Table 3.\"}\n  action_items:\n    - {round: 4, action: \"SmolVLA official checkpoint pruning sweep (10 configs)\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Write official results into paper\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Official HF checkpoint (57.2% baseline) shows 0% at k=0.95/0.9/0.5. Dual protocol (59.2%/57.2%) both confirm cliff. VTR M=32 recovers to 60.1±1.3%.\"\n  resolution_round: 5\n\n- id: \"R4-C3\"\n  summary: \"CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"3 data points = 3 connector clusters, CV adds no predictive power beyond label\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — CV reframed as correlational diagnostic. Section 4.6 title changed. Limitations explicit about N=3, 2 k values.\"}\n  action_items:\n    - {round: 4, action: \"Reframe CV as correlational diagnostic, add X-VLA within-family variance argument\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"CV reframed as 'diagnostic metric that correlates with' (not 'predictor'). Contribution C2 updated. Section 5 Limitations: 'the CV correlation spans three models and two retention ratios'.\"\n  resolution_round: 5\n\n- id: \"R4-C4\"\n  summary: \"π0 offline-only used in core taxonomy argument\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Internal consistency: paper argues offline unreliable but uses π0 offline for taxonomy\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Table 1 footnote, Introduction caveat, 4-in-closed-loop framing all confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Table 1 π0 offline-only label, caveat on π0-OpenVLA 63pp gap, CogACT literature label\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Table 1: †offline metrics only. Introduction: 'evaluating four in closed-loop and analyzing three via offline metrics or literature'. π0-OpenVLA comparison has causal interpretation caveat.\"\n  resolution_round: 5\n\n- id: \"R4-S1\"\n  summary: \"X-VLA linear projection label misleading (has 12-layer BART encoder)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Table 1 label should reflect BART encoder\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Linear + BART (12L)‡ confirmed in Table 1.\"}\n  action_items:\n    - {round: 4, action: \"Table 1 connector column update + continuous spectrum discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Table 1: Linear + BART (12L)‡. Footnote explains effective pipeline.\"\n  resolution_round: 5\n\n- id: \"R4-S2\"\n  summary: \"OpenVLA L2 vs random cross-seed, k=0.5 same-seed missing\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2\", note: \"CV scaling law crossover point based on cross-seed comparison\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Footnote 5: same-seed k=0.5: 35.8% random vs 39.2% L2 (gap 3.4pp).\"}\n  action_items:\n    - {round: 4, action: \"OpenVLA random k=0.5 seed42 completed\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Three k values (0.3, 0.5, 0.7) same-seed verified. k=0.5 gap = 3.4pp.\"\n  resolution_round: 5\n\n- id: \"R4-S3\"\n  summary: \"VTR novelty limited — Perceiver/Q-Former VLA application\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 agree\", note: \"Contribution is diagnostic (why re-encoding works), not method\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — diagnostic protocol framing confirmed throughout.\"}\n  action_items:\n    - {round: 4, action: \"Reframe VTR as diagnostic contribution\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"VTR framed as diagnostic tool. 'The primary contribution of VTR is recovering functional performance where all deletion methods yield 0%, not matching the official baseline.'\"\n  resolution_round: 5\n\n- id: \"R4-S4\"\n  summary: \"VTR p=0.15 insufficient for re-encoding is operative mechanism claim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 agree\", note: \"MLP adapter SR higher, claim should be about re-encoding in general\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 'comparable recovery (p=0.15)' confirmed, no operative mechanism claim.\"}\n  action_items:\n    - {round: 4, action: \"Soften claim to both architectures achieve comparable recovery\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"p=0.15 reported as 'comparable'. MLP adapter architecture details in Appendix F.3.\"\n  resolution_round: 5\n\n- id: \"R4-S5\"\n  summary: \"Diagnose-then-Compress framework overpackaged\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 agree\", note: \"Single-metric lookup table, not a framework\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — all 'framework' replaced with 'diagnostic protocol'.\"}\n  action_items:\n    - {round: 4, action: \"Replace framework with diagnostic protocol globally\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Global replacement confirmed in abstract, contributions, conclusion.\"\n  resolution_round: 5\n\n- id: \"R4-S6\"\n  summary: \"Paper ~13 pages vs CoRL 8-page limit\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Section 5 Analysis ~3 pages is main excess\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 8 pages main text confirmed. Discussion compressed to 2 paragraphs.\"}\n  action_items:\n    - {round: 4, action: \"Major restructure: Analysis→Appendix, target 8 pages\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Pages 1-8 main text, page 9+ references, page 12+ appendix. CoRL compliant.\"\n  resolution_round: 5\n\n- id: \"R4-S7\"\n  summary: \"Falsifies immune assumption — straw man\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 partial agree\", note: \"Soften to demonstrates offline tolerance does not generalize\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — no 'falsifies' in paper. 'not immune' retained as descriptive.\"}\n  action_items:\n    - {round: 4, action: \"Replace falsifies with demonstrates offline tolerance caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"All 'falsifies' removed. 'low CV does not imply tokens are dispensable; it implies uniform criticality'.\"\n  resolution_round: 5\n\n- id: \"R4-S8\"\n  summary: \"M=96 dip vs flat M-curve narrative\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1 warning, R2 partial rebut\", note: \"Change flat to relatively stable\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 'relatively stable' confirmed in abstract, results, discussion.\"}\n  action_items:\n    - {round: 4, action: \"flat→relatively stable, add M=96 dip discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"All 'flat' replaced. Appendix D: M=96 dip explained as possible intermediate bottleneck.\"\n  resolution_round: 5\n\n- id: \"R4-M1\"\n  summary: \"Related Work citation count insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer assessment\", note: \"Need 15-20 additional citations\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — ~46 citations, quality and relevance sufficient.\"}\n  action_items:\n    - {round: 4, action: \"Expand Related Work with 15+ citations\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"30+ citations across 4 categories. Don't Run with Scissors comparison expanded. Perceiver/Q-Former covered.\"\n  resolution_round: 5\n\n- id: \"R4-M3\"\n  summary: \"VTR vs official baseline statistical significance p=0.72\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer calculation\", note: \"Remove any claim VTR matches official\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — framed as recovery from 0%, not matching official.\"}\n  action_items:\n    - {round: 4, action: \"Fix VTR vs official framing\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Primary contribution: recovering from 0% where deletion fails. p≈0.72 reported honestly.\"\n  resolution_round: 5\n\n- id: \"R4-M4\"\n  summary: \"D141 token position visualization not written into paper\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer assessment\", note: \"High ROI — spatial clustering evidence\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Appendix Token Position Analysis with DBSCAN clustering.\"}\n  action_items:\n    - {round: 4, action: \"Write D141 visualization into appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix with DBSCAN clustering at k=0.7/0.5/0.3.\"\n  resolution_round: 5\n\n# ===== Round 5 New Issues =====\n\n- id: \"R5-W1\"\n  summary: \"π₀.5 V-shape non-monotonic recovery (k=0.85→5%, k=0.7→77%) unexplained by hypergeometric model\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus (R1 raised, R2 AGREE as more severe than own overfitting concern)\", note: \"Hypergeometric model predicts monotonic collapse but data shows 72pp recovery at higher pruning. Section 5 acknowledges but Section 4.7 presentation too positive.\"}\n  action_items:\n    - {round: 5, action: \"Add 1-2 sentences in Section 4.7 on model applicability boundary (onset only, not recovery regimes)\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 5, action: \"Discuss V-shape recovery mechanism (speculative) in Section 4.4 or Appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"SmolVLA baseline 57.2% vs 59.2% inconsistency across sections (dual evaluation protocol)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus (R1 raised, R2 AGREE — acknowledged as own oversight)\", note: \"Section 4.2 uses 57.2%, Table 2 uses 59.2%. Both from different protocols but not explained at first mention.\"}\n  action_items:\n    - {round: 5, action: \"Clarify at first mention in Section 4.2: '57.2%–59.2% across two evaluation protocols (Appendix B)'\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Discussion section over-compressed (2 paragraphs), missing pointer to Appendix J-K mechanistic analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"Valuable mechanistic insights (connector→token independence) moved to appendix but no explicit cross-reference from Discussion.\"}\n  action_items:\n    - {round: 5, action: \"Add one sentence in Discussion pointing to Appendices J-K for extended mechanistic analysis\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"Hypergeometric model C=91 parameter — post-hoc fitted vs independently measurable unclear\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 independent convergence (R1-NEW-4 + R2-2.1)\", note: \"If C is fitted from SR curve, model is curve fitting with no predictive power. If independently measurable from attention heatmaps, model has genuine predictive validity.\"}\n  action_items:\n    - {round: 5, action: \"Clarify C determination method in Appendix C.8 (fitted from data vs measured from heatmap)\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'All tokens carry equal weight' imprecise — L2 norm uniformity ≠ task-relevant information uniformity\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R2 raised, R1 partial REBUT (R2 misquoted original) but AGREE on precision improvement\", note: \"R2 misquoted the sentence but the underlying concern about L2→weight equivalence is valid. R1 suggests: 'near-uniform L2 norms (CV=0.038) suggest no token subset carries disproportionate information'.\"}\n  action_items:\n    - {round: 5, action: \"Revise 'all tokens carry equal weight' to reference CV directly\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-V1\"\n  summary: \"Figure 4 placeholder on page 17 — not replaced with actual token importance heatmap\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"Visual Check Agent\", note: \"Displays '[Placeholder: token importance heatmap]' gray text box. Submitted paper with placeholder is serious oversight.\"}\n  action_items:\n    - {round: 5, action: \"Replace Figure 4 placeholder with actual token importance heatmap visualization\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "issues_yaml": "- id: \"R4-C1\"\n  summary: \"Causal claim under-identified — connector vs backbone/encoder/action confound\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"determines needs downgrade to associated with\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — full-text causal language downgrade confirmed. No residual 'determines' found.\"}\n  action_items:\n    - {round: 4, action: \"Full-text causal language downgrade (determines→associated, controlled→closest available)\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Round 5 verified: determines→strongly associated with, predicts→correlates, falsifies→demonstrates. Appendix N confound analysis added. Both reviewers confirm thorough and consistent.\"\n  resolution_round: 5\n\n- id: \"R4-C2\"\n  summary: \"SmolVLA baseline 44.8% vs official — cliff and VTR on undertrained checkpoint\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Official checkpoint full pruning sweep is minimum requirement\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — official checkpoint (57.2% baseline) multi-k verification complete. Dual evaluation protocol in Appendix Table 3.\"}\n  action_items:\n    - {round: 4, action: \"SmolVLA official checkpoint pruning sweep (10 configs)\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Write official results into paper\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Official HF checkpoint (57.2% baseline) shows 0% at k=0.95/0.9/0.5. Dual protocol (59.2%/57.2%) both confirm cliff. VTR M=32 recovers to 60.1±1.3%.\"\n  resolution_round: 5\n\n- id: \"R4-C3\"\n  summary: \"CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"3 data points = 3 connector clusters, CV adds no predictive power beyond label\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — CV reframed as correlational diagnostic. Section 4.6 title changed. Limitations explicit about N=3, 2 k values.\"}\n  action_items:\n    - {round: 4, action: \"Reframe CV as correlational diagnostic, add X-VLA within-family variance argument\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"CV reframed as 'diagnostic metric that correlates with' (not 'predictor'). Contribution C2 updated. Section 5 Limitations: 'the CV correlation spans three models and two retention ratios'.\"\n  resolution_round: 5\n\n- id: \"R4-C4\"\n  summary: \"π0 offline-only used in core taxonomy argument\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Internal consistency: paper argues offline unreliable but uses π0 offline for taxonomy\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Table 1 footnote, Introduction caveat, 4-in-closed-loop framing all confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Table 1 π0 offline-only label, caveat on π0-OpenVLA 63pp gap, CogACT literature label\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Table 1: †offline metrics only. Introduction: 'evaluating four in closed-loop and analyzing three via offline metrics or literature'. π0-OpenVLA comparison has causal interpretation caveat.\"\n  resolution_round: 5\n\n- id: \"R4-S1\"\n  summary: \"X-VLA linear projection label misleading (has 12-layer BART encoder)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Table 1 label should reflect BART encoder\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Linear + BART (12L)‡ confirmed in Table 1.\"}\n  action_items:\n    - {round: 4, action: \"Table 1 connector column update + continuous spectrum discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Table 1: Linear + BART (12L)‡. Footnote explains effective pipeline.\"\n  resolution_round: 5\n\n- id: \"R4-S2\"\n  summary: \"OpenVLA L2 vs random cross-seed, k=0.5 same-seed missing\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2\", note: \"CV scaling law crossover point based on cross-seed comparison\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Footnote 5: same-seed k=0.5: 35.8% random vs 39.2% L2 (gap 3.4pp).\"}\n  action_items:\n    - {round: 4, action: \"OpenVLA random k=0.5 seed42 completed\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Three k values (0.3, 0.5, 0.7) same-seed verified. k=0.5 gap = 3.4pp.\"\n  resolution_round: 5\n\n- id: \"R4-S3\"\n  summary: \"VTR novelty limited — Perceiver/Q-Former VLA application\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 agree\", note: \"Contribution is diagnostic (why re-encoding works), not method\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — diagnostic protocol framing confirmed throughout.\"}\n  action_items:\n    - {round: 4, action: \"Reframe VTR as diagnostic contribution\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"VTR framed as diagnostic tool. 'The primary contribution of VTR is recovering functional performance where all deletion methods yield 0%, not matching the official baseline.'\"\n  resolution_round: 5\n\n- id: \"R4-S4\"\n  summary: \"VTR p=0.15 insufficient for re-encoding is operative mechanism claim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 agree\", note: \"MLP adapter SR higher, claim should be about re-encoding in general\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 'comparable recovery (p=0.15)' confirmed, no operative mechanism claim.\"}\n  action_items:\n    - {round: 4, action: \"Soften claim to both architectures achieve comparable recovery\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"p=0.15 reported as 'comparable'. MLP adapter architecture details in Appendix F.3.\"\n  resolution_round: 5\n\n- id: \"R4-S5\"\n  summary: \"Diagnose-then-Compress framework overpackaged\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 agree\", note: \"Single-metric lookup table, not a framework\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — all 'framework' replaced with 'diagnostic protocol'.\"}\n  action_items:\n    - {round: 4, action: \"Replace framework with diagnostic protocol globally\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Global replacement confirmed in abstract, contributions, conclusion.\"\n  resolution_round: 5\n\n- id: \"R4-S6\"\n  summary: \"Paper ~13 pages vs CoRL 8-page limit\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Section 5 Analysis ~3 pages is main excess\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 8 pages main text confirmed. Discussion compressed to 2 paragraphs.\"}\n  action_items:\n    - {round: 4, action: \"Major restructure: Analysis→Appendix, target 8 pages\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Pages 1-8 main text, page 9+ references, page 12+ appendix. CoRL compliant.\"\n  resolution_round: 5\n\n- id: \"R4-S7\"\n  summary: \"Falsifies immune assumption — straw man\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 partial agree\", note: \"Soften to demonstrates offline tolerance does not generalize\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — no 'falsifies' in paper. 'not immune' retained as descriptive.\"}\n  action_items:\n    - {round: 4, action: \"Replace falsifies with demonstrates offline tolerance caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"All 'falsifies' removed. 'low CV does not imply tokens are dispensable; it implies uniform criticality'.\"\n  resolution_round: 5\n\n- id: \"R4-S8\"\n  summary: \"M=96 dip vs flat M-curve narrative\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1 warning, R2 partial rebut\", note: \"Change flat to relatively stable\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 'relatively stable' confirmed in abstract, results, discussion.\"}\n  action_items:\n    - {round: 4, action: \"flat→relatively stable, add M=96 dip discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"All 'flat' replaced. Appendix D: M=96 dip explained as possible intermediate bottleneck.\"\n  resolution_round: 5\n\n- id: \"R4-M1\"\n  summary: \"Related Work citation count insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer assessment\", note: \"Need 15-20 additional citations\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — ~46 citations, quality and relevance sufficient.\"}\n  action_items:\n    - {round: 4, action: \"Expand Related Work with 15+ citations\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"30+ citations across 4 categories. Don't Run with Scissors comparison expanded. Perceiver/Q-Former covered.\"\n  resolution_round: 5\n\n- id: \"R4-M3\"\n  summary: \"VTR vs official baseline statistical significance p=0.72\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer calculation\", note: \"Remove any claim VTR matches official\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — framed as recovery from 0%, not matching official.\"}\n  action_items:\n    - {round: 4, action: \"Fix VTR vs official framing\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Primary contribution: recovering from 0% where deletion fails. p≈0.72 reported honestly.\"\n  resolution_round: 5\n\n- id: \"R4-M4\"\n  summary: \"D141 token position visualization not written into paper\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer assessment\", note: \"High ROI — spatial clustering evidence\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Appendix Token Position Analysis with DBSCAN clustering.\"}\n  action_items:\n    - {round: 4, action: \"Write D141 visualization into appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix with DBSCAN clustering at k=0.7/0.5/0.3.\"\n  resolution_round: 5\n\n# ===== Round 5 New Issues =====\n\n- id: \"R5-W1\"\n  summary: \"π₀.5 V-shape non-monotonic recovery (k=0.85→5%, k=0.7→77%) unexplained by hypergeometric model\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus (R1 raised, R2 AGREE as more severe than own overfitting concern)\", note: \"Hypergeometric model predicts monotonic collapse but data shows 72pp recovery at higher pruning. Section 5 acknowledges but Section 4.7 presentation too positive.\"}\n  action_items:\n    - {round: 5, action: \"Add 1-2 sentences in Section 4.7 on model applicability boundary (onset only, not recovery regimes)\", assigned_to: \"paper_agent\", status: \"open\"}\n    - {round: 5, action: \"Discuss V-shape recovery mechanism (speculative) in Section 4.4 or Appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"SmolVLA baseline 57.2% vs 59.2% inconsistency across sections (dual evaluation protocol)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus (R1 raised, R2 AGREE — acknowledged as own oversight)\", note: \"Section 4.2 uses 57.2%, Table 2 uses 59.2%. Both from different protocols but not explained at first mention.\"}\n  action_items:\n    - {round: 5, action: \"Clarify at first mention in Section 4.2: '57.2%–59.2% across two evaluation protocols (Appendix B)'\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Discussion section over-compressed (2 paragraphs), missing pointer to Appendix J-K mechanistic analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"Valuable mechanistic insights (connector→token independence) moved to appendix but no explicit cross-reference from Discussion.\"}\n  action_items:\n    - {round: 5, action: \"Add one sentence in Discussion pointing to Appendices J-K for extended mechanistic analysis\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"Hypergeometric model C=91 parameter — post-hoc fitted vs independently measurable unclear\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 independent convergence (R1-NEW-4 + R2-2.1)\", note: \"If C is fitted from SR curve, model is curve fitting with no predictive power. If independently measurable from attention heatmaps, model has genuine predictive validity.\"}\n  action_items:\n    - {round: 5, action: \"Clarify C determination method in Appendix C.8 (fitted from data vs measured from heatmap)\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W5\"\n  summary: \"'All tokens carry equal weight' imprecise — L2 norm uniformity ≠ task-relevant information uniformity\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R2 raised, R1 partial REBUT (R2 misquoted original) but AGREE on precision improvement\", note: \"R2 misquoted the sentence but the underlying concern about L2→weight equivalence is valid. R1 suggests: 'near-uniform L2 norms (CV=0.038) suggest no token subset carries disproportionate information'.\"}\n  action_items:\n    - {round: 5, action: \"Revise 'all tokens carry equal weight' to reference CV directly\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-V1\"\n  summary: \"Figure 4 placeholder on page 17 — not replaced with actual token importance heatmap\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"Visual Check Agent\", note: \"Displays '[Placeholder: token importance heatmap]' gray text box. Submitted paper with placeholder is serious oversight.\"}\n  action_items:\n    - {round: 5, action: \"Replace Figure 4 placeholder with actual token importance heatmap visualization\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-22T08:19:10.595463+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml\", \"bytes\": 15548}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-22T08:21:00.517245+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 5 审稿报告 — importance_margin_vla_compress\n\n**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Continue（基于 Round 4）\n**Reviewer 1**: 方法严谨性 + 实验验证 | **Reviewer 2**: 新颖性 + 完整性 + venue fit\n**交叉分享**: 完成（R1↔R2 逐条 AGREE/REBUT）| **收敛**: 1 轮达成\n\n---\n\n## Summary\n\n本轮为 Round 4（Weak Reject）后的修订评估。论文对 Round 4 提出的 15 个 issues（4 critical + 11 should-fix/info）进行了全面回应，两位 Reviewer 一致确认**全部 15 个 issues 已 RESOLVED**。核心修改包括：(1) 因果语言系统性降级（determines→associated, predicts→correlates, falsifies→demonstrates），(2) SmolVLA 官方 checkpoint 多 k 值验证确认 cliff 为架构属性，(3) 正文从 ~13 页压缩至 8 页，(4) 新增 Section 4.7 cross-suite generalization 与 hypergeometric cliff model，(5) Appendix N confound analysis。两位 Reviewer 均上调评分一档。新发现 5 个 warning 级问题和 1 个 critical 级视觉问题（Figure 4 placeholder），均为 camera-ready 可修复项。\n\n---\n\n## Strengths\n\n**S1. 系统性因果语言降级（R1+R2 共识）**\n论文对 claim 强度进行了全文一致的校准：\"determines\"→\"strongly associated with\"，\"predicts\"→\"correlates with\"，\"falsifies\"→\"demonstrates\"，\"framework\"→\"diagnostic protocol\"。Grep 确认无残留。降级幅度恰当——核心发现仍然清晰，但不再超出数据支撑。这是本轮最重要的改进。\n\n**S2. 官方 checkpoint 多 k 值验证（R1+R2 共识）**\nSmolVLA 官方 HF checkpoint（57.2% SR baseline）在 k∈{0.95, 0.9, 0.5} 下均为 0% SR，dual evaluation protocol（59.2% / 57.2%）交叉验证。VTR M=32 恢复至 60.1±1.3%。彻底解决了 Round 4 \"cliff 可能是 undertrained checkpoint artifact\" 的核心质疑。\n\n**S3. Limitations 的诚实度（R2 特别指出）**\nSection 5 Limitations 明确列出：simulation-only、N=3 connector 类型、CV 仅 3 模型 × 2 k 值、π₀ offline-only、hypergeometric model 不解释 V-shape recovery。R2 评价：\"我审过的论文中最诚实的 Limitations 之一。\"\n\n**S4. 新增分析深度（R1+R2 共识）**\nSection 4.7 cross-suite generalization（Object/Spatial/Goal）+ hypergeometric cliff model H(N=768, C=91, T=6) 将定性 cliff 观察提升为定量假说。Appendix N confound analysis 是实质性的方法论贡献。\n\n**S5. 正文压缩与结构重组（R1+R2 共识）**\n从 ~13 页压缩至 8 页正文，Discussion 从 5 subsection 压缩为 2 段，大量 mechanistic analysis 移入 Appendix。符合 CoRL 8 页限制。\n\n---\n\n## Weaknesses\n\n### Camera-Ready Must-Fix\n\n**W-V1 [critical] Figure 4 占位符未替换（视觉审查）**\nPage 17 的 Figure 4 显示 \"[Placeholder: token importance heatmap]\" 灰底文字框，未替换为实际图片。已提交论文中出现 placeholder 是严重疏忽。必须在提交前替换为实际 token importance heatmap 可视化。\n\n### Camera-Ready Should-Fix\n\n**W-N1 [warning] π₀.5 V-shape 非单调 recovery 与 hypergeometric model 解释力缺口（R1 提出, R2 强烈 AGREE）**\nπ₀.5 在 LIBERO-Object 上：k=0.95 (69.4%) → k=0.85 (5.0%) → k=0.7 (77.2%)，72pp swing。Hypergeometric model 预测单调 collapse probability，从逻辑上无法解释 k=0.7 处的恢复。Section 5 一句带过 \"does not explain V-shape recovery at k≤0.7\" 不够充分。R2 指出这直接削弱了 CV diagnostic 的实用性——最优 k 值不是从 CV 单调推导的。\n- **建议**: Section 4.7 增加模型适用边界说明；Section 4.4 或 Appendix 讨论 V-shape 可能机制。\n\n**W-N2 [warning] Hypergeometric model C=91 参数来源不明（R1+R2 独立收敛）**\nC=91（critical tokens）是 hypergeometric model 的关键自由参数，但正文和 Appendix C.8 均未说明其确定方法。如果 C 从 SR 曲线反向拟合，模型退化为 curve fitting，无独立预测力；如果从 attention heatmap 独立测量，模型有真正的预测价值。两位 Reviewer 独立收敛于此问题。\n- **建议**: Appendix C.8 明确 C 的确定方法。\n\n**W-N3 [warning] SmolVLA baseline 数字不一致（R1 提出, R2 AGREE）**\nSection 4.2: \"57.2% SR\"，Table 2: \"59.2% baseline\"。来自不同评估协议但首次提及时未说明。\n- **建议**: Section 4.2 首次提及时写 \"57.2%–59.2% across two evaluation protocols (Appendix B)\"。\n\n**W-N4 [warning] Discussion 过度压缩（R1 提出, R2 AGREE）**\n旧版 ~3 页的 mechanistic insights（connector→token independence 系统性分析）压缩为 2 段 ~10 行。内容移入 Appendix J-K 但正文无显式指引。\n- **建议**: Discussion 增加一句 \"For extended mechanistic analysis, see Appendices J–K\"。\n\n**W-N5 [warning] \"All tokens carry equal weight\" 措辞不精确（R2 提出, R1 部分 REBUT 但 AGREE on precision）**\nSection 4.4 中 L2 norm 均匀被等同于 \"equal weight\"，但 L2 norm 均匀不等于 task-relevant information 均匀。R1 指出 R2 误引了原文语境，但同意措辞应更精确。\n- **建议**: 改为 \"near-uniform L2 norms (CV=0.038) suggest no token subset carries disproportionate information\"。\n\n---\n\n## Questions\n\n1. Hypergeometric model 的 C 参数是从 collapse curve 反向拟合的，还是从 token importance heatmap（Figure 4）独立测量的？如果是后者，阈值如何选择？\n2. π₀.5 在 k=0.7 恢复到 77.2% 的机制假说是什么？是否可能与 position re-indexing 或 computation regime transition 有关？\n3. VTR 的 M=32 vs M=128 在 official checkpoint 上的 SR 差异是多少？（当前数据仅报告了 M=32 的 60.1%）\n\n---\n\n## Missing References\n\nRound 5 无新增缺失引用。Round 4 建议的引用已基本覆盖（~46 citations）。R1+R2 共识：质量和相关性到位。\n\n---\n\n## External Review\n\n未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（2026-05-22 08:06→08:09）。\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| **Critical** | p17 | **Figure 4 为占位符**——灰底文字框 \"[Placeholder: token importance heatmap]\"，未替换为实际图片 |\n| Warning | pp3-4 | 连续 2 页纯文本（Related Work + Methods 开头），无 display item |\n| Warning | pp1-9 | 正文仅 4 个 display items（2 figures + 2 tables），对实证论文偏少 |\n| Warning | p6 | 整页纯文本，夹在 Table 1 (p5) 和 Table 2 (p7) 之间 |\n| Warning | p27 | 末页底部约 35% 空白 |\n| Info | p8 | Figure 2 axis label 和 legend 字号偏小（~60-65% 正文字号） |\n| Info | p5 | Table 1 格式良好——booktabs 风格、加粗、CI 标注清晰（亮点）|\n| Info | p2 | Figure 1 架构图清晰专业，颜色区分度好 |\n| Info | pp13-15 | 附录表格密度高，per-task breakdown 完整 |\n| Info | p23 | Figure 7 双面板图配色方案与 Figure 2 一致 |\n| Info | pp9-11 | References 无未解析引用，格式统一 |\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| Reviewer | Round 4 | Round 5 | 变化 |\n|----------|---------|---------|------|\n| R1 | Borderline (leaning weak reject) | **Weak Accept** | +1 档 |\n| R2 | Weak Reject (borderline) | **Borderline (leaning weak accept)** | +1 档 |\n\n### 共识与分歧\n\n**完全共识（无分歧）：**\n- Round 4 全部 15 个 issues 已 RESOLVED\n- 因果语言降级彻底且一致\n- 新增内容（cross-suite、hypergeometric model、official checkpoint）增强了贡献\n- Limitations 诚实度高于平均水平\n- 论文展现了出色的迭代改进能力\n- W-N1 到 W-N4 均为 camera-ready 可修复项，不影响接收决定\n\n**半档评分差异的来源（已解释，非未解决分歧）：**\n1. **Venue fit**: R2 对 simulation-only 在 CoRL 的适配度权重更高；R1 认为架构理解类研究合理使用仿真\n2. **N=3 limitation**: R2 认为 claim 降级是必要非充分条件；R1 认为降级已充分弥补\n3. **VTR 贡献评估**: 一致认为 incremental 但定位诚实；对评分影响的权重略有差异\n\n### Camera-Ready 条件\n\n如果接收，以下为 camera-ready 必须完成的修改：\n1. ★ 替换 Figure 4 placeholder 为实际 token importance heatmap\n2. Section 4.7 增加 hypergeometric model 适用边界说明\n3. Appendix C.8 明确 C 参数确定方法\n4. Section 4.2 统一 SmolVLA baseline 数字表述\n5. Discussion 增加 Appendix J-K 指引\n6. Section 4.4 精确化 \"equal weight\" 措辞\n\n### 综合评分: **Weak Accept**\n\n**Confidence**: High\n\n**理由**: 两位 Reviewer 均从 reject 区间上调至 accept 边界。Round 4 的 4 个 critical issues 全部彻底修复，claim 强度与数据支撑现已匹配。新增实证（cross-suite、official checkpoint）和分析（hypergeometric model、confound analysis）增加了实质价值。剩余弱点（N=3 connector、sim-only、hypergeometric model 局限）是 inherent scope limitations，非方法论缺陷，且已在 Limitations 中诚实承认。论文对 CoRL 社区的核心价值——系统性揭示 VLA connector 与 pruning 行为的关联，并提供 CV 零成本诊断指标——清晰、有证据支撑、且被适度表述。Figure 4 placeholder 是提交前必须修复的严重疏忽，但不影响学术评价。\n\n---\n\n## Detailed Comments\n\n### 对作者的建议（按优先级排序）\n\n1. **Figure 4 placeholder**（提交前必修）: 当前为灰底文字框，需替换为实际 heatmap。如果数据已有（D141 visualization），应立即集成。\n\n2. **Hypergeometric model 边界**（camera-ready）: Section 4.7 在报告 RMSE=0.025 后增加：\"The model captures onset sharpness at high retention but does not generalize to moderate retention where compensatory mechanisms may emerge (see §5 Limitations).\"\n\n3. **C 参数透明化**（camera-ready）: Appendix C.8 增加一段说明 C 的来源——是从 Figure 4 heatmap 用某个 importance threshold 独立计算的，还是从 SR 数据最小化 RMSE 反向拟合的。如果是前者，说明 threshold 选择；如果是后者，承认这是 curve fitting。\n\n4. **Baseline 数字统一**（camera-ready）: Section 4.2 首次提及 SmolVLA 时改为 \"57.2%–59.2% SR across two evaluation protocols (Appendix B)\"，避免读者在 Section 4.2 和 Table 2 之间产生困惑。\n\n5. **Discussion 指引**（camera-ready）: 在 Section 5 第一段末尾增加 \"Full mechanistic analysis of how connector architecture creates the observed token independence structure appears in Appendices J–K.\"\n\n6. **\"Equal weight\" 精确化**（camera-ready）: Section 4.4 的 \"all tokens carry equal weight\" 改为 \"near-uniform L2 norms (CV = 0.038) suggest that no token subset carries disproportionate information, so random removal preserves spatial coverage.\"\n\n### 给 AC 的建议\n\n本文在 5 轮审稿中展现了持续的、高质量的改进。如果需要在 borderline 论文中取舍：\n\n**优势**:\n- 跨架构覆盖广度（7 models, 3 connectors, 3 suites）在 VLA token compression 领域无出其右\n- Negative results（linear projection 不可 prune、low-CV models 的 uniform criticality）有高实用价值\n- Limitations 的诚实度和 confound transparency 高于平均水平\n- CV 作为零成本诊断指标有明确的实践路径\n\n**风险**:\n- N=3 connector 类型是基本瓶颈——增加 Perceiver-based VLA（如 RoboFlamingo）将显著增强说服力\n- Simulation-only 在 CoRL 的 venue fit 有短板，但论文定位为 diagnostic analysis 而非 system deployment\n- Hypergeometric model 的预测力未经独立验证（C 参数来源不明）",
  "project": "importance_margin_vla_compress",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak accept",
  "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 5 审稿报告 — importance_margin_vla_compress\n\n**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Continue（基于 Round 4）\n**Reviewer 1**: 方法严谨性 + 实验验证 | **Reviewer 2**: 新颖性 + 完整性 + venue fit\n**交叉分享**: 完成（R1↔R2 逐条 AGREE/REBUT）| **收敛**: 1 轮达成\n\n---\n\n## Summary\n\n本轮为 Round 4（Weak Reject）后的修订评估。论文对 Round 4 提出的 15 个 issues（4 critical + 11 should-fix/info）进行了全面回应，两位 Reviewer 一致确认**全部 15 个 issues 已 RESOLVED**。核心修改包括：(1) 因果语言系统性降级（determines→associated, predicts→correlates, falsifies→demonstrates），(2) SmolVLA 官方 checkpoint 多 k 值验证确认 cliff 为架构属性，(3) 正文从 ~13 页压缩至 8 页，(4) 新增 Section 4.7 cross-suite generalization 与 hypergeometric cliff model，(5) Appendix N confound analysis。两位 Reviewer 均上调评分一档。新发现 5 个 warning 级问题和 1 个 critical 级视觉问题（Figure 4 placeholder），均为 camera-ready 可修复项。\n\n---\n\n## Strengths\n\n**S1. 系统性因果语言降级（R1+R2 共识）**\n论文对 claim 强度进行了全文一致的校准：\"determines\"→\"strongly associated with\"，\"predicts\"→\"correlates with\"，\"falsifies\"→\"demonstrates\"，\"framework\"→\"diagnostic protocol\"。Grep 确认无残留。降级幅度恰当——核心发现仍然清晰，但不再超出数据支撑。这是本轮最重要的改进。\n\n**S2. 官方 checkpoint 多 k 值验证（R1+R2 共识）**\nSmolVLA 官方 HF checkpoint（57.2% SR baseline）在 k∈{0.95, 0.9, 0.5} 下均为 0% SR，dual evaluation protocol（59.2% / 57.2%）交叉验证。VTR M=32 恢复至 60.1±1.3%。彻底解决了 Round 4 \"cliff 可能是 undertrained checkpoint artifact\" 的核心质疑。\n\n**S3. Limitations 的诚实度（R2 特别指出）**\nSection 5 Limitations 明确列出：simulation-only、N=3 connector 类型、CV 仅 3 模型 × 2 k 值、π₀ offline-only、hypergeometric model 不解释 V-shape recovery。R2 评价：\"我审过的论文中最诚实的 Limitations 之一。\"\n\n**S4. 新增分析深度（R1+R2 共识）**\nSection 4.7 cross-suite generalization（Object/Spatial/Goal）+ hypergeometric cliff model H(N=768, C=91, T=6) 将定性 cliff 观察提升为定量假说。Appendix N confound analysis 是实质性的方法论贡献。\n\n**S5. 正文压缩与结构重组（R1+R2 共识）**\n从 ~13 页压缩至 8 页正文，Discussion 从 5 subsection 压缩为 2 段，大量 mechanistic analysis 移入 Appendix。符合 CoRL 8 页限制。\n\n---\n\n## Weaknesses\n\n### Camera-Ready Must-Fix\n\n**W-V1 [critical] Figure 4 占位符未替换（视觉审查）**\nPage 17 的 Figure 4 显示 \"[Placeholder: token importance heatmap]\" 灰底文字框，未替换为实际图片。已提交论文中出现 placeholder 是严重疏忽。必须在提交前替换为实际 token importance heatmap 可视化。\n\n### Camera-Ready Should-Fix\n\n**W-N1 [warning] π₀.5 V-shape 非单调 recovery 与 hypergeometric model 解释力缺口（R1 提出, R2 强烈 AGREE）**\nπ₀.5 在 LIBERO-Object 上：k=0.95 (69.4%) → k=0.85 (5.0%) → k=0.7 (77.2%)，72pp swing。Hypergeometric model 预测单调 collapse probability，从逻辑上无法解释 k=0.7 处的恢复。Section 5 一句带过 \"does not explain V-shape recovery at k≤0.7\" 不够充分。R2 指出这直接削弱了 CV diagnostic 的实用性——最优 k 值不是从 CV 单调推导的。\n- **建议**: Section 4.7 增加模型适用边界说明；Section 4.4 或 Appendix 讨论 V-shape 可能机制。\n\n**W-N2 [warning] Hypergeometric model C=91 参数来源不明（R1+R2 独立收敛）**\nC=91（critical tokens）是 hypergeometric model 的关键自由参数，但正文和 Appendix C.8 均未说明其确定方法。如果 C 从 SR 曲线反向拟合，模型退化为 curve fitting，无独立预测力；如果从 attention heatmap 独立测量，模型有真正的预测价值。两位 Reviewer 独立收敛于此问题。\n- **建议**: Appendix C.8 明确 C 的确定方法。\n\n**W-N3 [warning] SmolVLA baseline 数字不一致（R1 提出, R2 AGREE）**\nSection 4.2: \"57.2% SR\"，Table 2: \"59.2% baseline\"。来自不同评估协议但首次提及时未说明。\n- **建议**: Section 4.2 首次提及时写 \"57.2%–59.2% across two evaluation protocols (Appendix B)\"。\n\n**W-N4 [warning] Discussion 过度压缩（R1 提出, R2 AGREE）**\n旧版 ~3 页的 mechanistic insights（connector→token independence 系统性分析）压缩为 2 段 ~10 行。内容移入 Appendix J-K 但正文无显式指引。\n- **建议**: Discussion 增加一句 \"For extended mechanistic analysis, see Appendices J–K\"。\n\n**W-N5 [warning] \"All tokens carry equal weight\" 措辞不精确（R2 提出, R1 部分 REBUT 但 AGREE on precision）**\nSection 4.4 中 L2 norm 均匀被等同于 \"equal weight\"，但 L2 norm 均匀不等于 task-relevant information 均匀。R1 指出 R2 误引了原文语境，但同意措辞应更精确。\n- **建议**: 改为 \"near-uniform L2 norms (CV=0.038) suggest no token subset carries disproportionate information\"。\n\n---\n\n## Questions\n\n1. Hypergeometric model 的 C 参数是从 collapse curve 反向拟合的，还是从 token importance heatmap（Figure 4）独立测量的？如果是后者，阈值如何选择？\n2. π₀.5 在 k=0.7 恢复到 77.2% 的机制假说是什么？是否可能与 position re-indexing 或 computation regime transition 有关？\n3. VTR 的 M=32 vs M=128 在 official checkpoint 上的 SR 差异是多少？（当前数据仅报告了 M=32 的 60.1%）\n\n---\n\n## Missing References\n\nRound 5 无新增缺失引用。Round 4 建议的引用已基本覆盖（~46 citations）。R1+R2 共识：质量和相关性到位。\n\n---\n\n## External Review\n\n未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（2026-05-22 08:06→08:09）。\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| **Critical** | p17 | **Figure 4 为占位符**——灰底文字框 \"[Placeholder: token importance heatmap]\"，未替换为实际图片 |\n| Warning | pp3-4 | 连续 2 页纯文本（Related Work + Methods 开头），无 display item |\n| Warning | pp1-9 | 正文仅 4 个 display items（2 figures + 2 tables），对实证论文偏少 |\n| Warning | p6 | 整页纯文本，夹在 Table 1 (p5) 和 Table 2 (p7) 之间 |\n| Warning | p27 | 末页底部约 35% 空白 |\n| Info | p8 | Figure 2 axis label 和 legend 字号偏小（~60-65% 正文字号） |\n| Info | p5 | Table 1 格式良好——booktabs 风格、加粗、CI 标注清晰（亮点）|\n| Info | p2 | Figure 1 架构图清晰专业，颜色区分度好 |\n| Info | pp13-15 | 附录表格密度高，per-task breakdown 完整 |\n| Info | p23 | Figure 7 双面板图配色方案与 Figure 2 一致 |\n| Info | pp9-11 | References 无未解析引用，格式统一 |\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| Reviewer | Round 4 | Round 5 | 变化 |\n|----------|---------|---------|------|\n| R1 | Borderline (leaning weak reject) | **Weak Accept** | +1 档 |\n| R2 | Weak Reject (borderline) | **Borderline (leaning weak accept)** | +1 档 |\n\n### 共识与分歧\n\n**完全共识（无分歧）：**\n- Round 4 全部 15 个 issues 已 RESOLVED\n- 因果语言降级彻底且一致\n- 新增内容（cross-suite、hypergeometric model、official checkpoint）增强了贡献\n- Limitations 诚实度高于平均水平\n- 论文展现了出色的迭代改进能力\n- W-N1 到 W-N4 均为 camera-ready 可修复项，不影响接收决定\n\n**半档评分差异的来源（已解释，非未解决分歧）：**\n1. **Venue fit**: R2 对 simulation-only 在 CoRL 的适配度权重更高；R1 认为架构理解类研究合理使用仿真\n2. **N=3 limitation**: R2 认为 claim 降级是必要非充分条件；R1 认为降级已充分弥补\n3. **VTR 贡献评估**: 一致认为 incremental 但定位诚实；对评分影响的权重略有差异\n\n### Camera-Ready 条件\n\n如果接收，以下为 camera-ready 必须完成的修改：\n1. ★ 替换 Figure 4 placeholder 为实际 token importance heatmap\n2. Section 4.7 增加 hypergeometric model 适用边界说明\n3. Appendix C.8 明确 C 参数确定方法\n4. Section 4.2 统一 SmolVLA baseline 数字表述\n5. Discussion 增加 Appendix J-K 指引\n6. Section 4.4 精确化 \"equal weight\" 措辞\n\n### 综合评分: **Weak Accept**\n\n**Confidence**: High\n\n**理由**: 两位 Reviewer 均从 reject 区间上调至 accept 边界。Round 4 的 4 个 critical issues 全部彻底修复，claim 强度与数据支撑现已匹配。新增实证（cross-suite、official checkpoint）和分析（hypergeometric model、confound analysis）增加了实质价值。剩余弱点（N=3 connector、sim-only、hypergeometric model 局限）是 inherent scope limitations，非方法论缺陷，且已在 Limitations 中诚实承认。论文对 CoRL 社区的核心价值——系统性揭示 VLA connector 与 pruning 行为的关联，并提供 CV 零成本诊断指标——清晰、有证据支撑、且被适度表述。Figure 4 placeholder 是提交前必须修复的严重疏忽，但不影响学术评价。\n\n---\n\n## Detailed Comments\n\n### 对作者的建议（按优先级排序）\n\n1. **Figure 4 placeholder**（提交前必修）: 当前为灰底文字框，需替换为实际 heatmap。如果数据已有（D141 visualization），应立即集成。\n\n2. **Hypergeometric model 边界**（camera-ready）: Section 4.7 在报告 RMSE=0.025 后增加：\"The model captures onset sharpness at high retention but does not generalize to moderate retention where compensatory mechanisms may emerge (see §5 Limitations).\"\n\n3. **C 参数透明化**（camera-ready）: Appendix C.8 增加一段说明 C 的来源——是从 Figure 4 heatmap 用某个 importance threshold 独立计算的，还是从 SR 数据最小化 RMSE 反向拟合的。如果是前者，说明 threshold 选择；如果是后者，承认这是 curve fitting。\n\n4. **Baseline 数字统一**（camera-ready）: Section 4.2 首次提及 SmolVLA 时改为 \"57.2%–59.2% SR across two evaluation protocols (Appendix B)\"，避免读者在 Section 4.2 和 Table 2 之间产生困惑。\n\n5. **Discussion 指引**（camera-ready）: 在 Section 5 第一段末尾增加 \"Full mechanistic analysis of how connector architecture creates the observed token independence structure appears in Appendices J–K.\"\n\n6. **\"Equal weight\" 精确化**（camera-ready）: Section 4.4 的 \"all tokens carry equal weight\" 改为 \"near-uniform L2 norms (CV = 0.038) suggest that no token subset carries disproportionate information, so random removal preserves spatial coverage.\"\n\n### 给 AC 的建议\n\n本文在 5 轮审稿中展现了持续的、高质量的改进。如果需要在 borderline 论文中取舍：\n\n**优势**:\n- 跨架构覆盖广度（7 models, 3 connectors, 3 suites）在 VLA token compression 领域无出其右\n- Negative results（linear projection 不可 prune、low-CV models 的 uniform criticality）有高实用价值\n- Limitations 的诚实度和 confound transparency 高于平均水平\n- CV 作为零成本诊断指标有明确的实践路径\n\n**风险**:\n- N=3 connector 类型是基本瓶颈——增加 Perceiver-based VLA（如 RoboFlamingo）将显著增强说服力\n- Simulation-only 在 CoRL 的 venue fit 有短板，但论文定位为 diagnostic analysis 而非 system deployment\n- Hypergeometric model 的预测力未经独立验证（C 参数来源不明）",
    "project": "importance_margin_vla_compress",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak accept",
    "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-22T08:21:05.286268+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6ea0e93e255655758819bea2ab1f224d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4769
}
```

</details>

---


### Assistant

_source line 412 · 2026-05-22T08:21:11.933479+00:00_

Round 5 审稿报告已投递。

**结论**: 评分从 Round 4 的 **Weak Reject** 上调至 **Weak Accept**。Round 4 全部 15 个 issues 经两位 Reviewer 逐条验证均已 RESOLVED。新发现 5 个 warning + 1 个 critical（Figure 4 placeholder），均为 camera-ready 可修复项。Issue tracker 已同步更新（15 resolved + 6 new open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 413 · 2026-05-22T08:21:13.443395+00:00_

[Reviewer 2 审稿结果]:
Round 5 交叉回应已提交。

核心结论：与 R1 在所有 4 个新发现上达成一致（全部 [AGREE]）。最重要的共识是 R1-NEW-1 的 V-shape recovery 问题——比我自己提出的 c* 过拟合担忧更根本，因为它挑战的是 hypergeometric model 的 explanatory scope 而非统计效力。R1-NEW-4 与我的 R2-2.1 指向同一根本问题（c* 参数确定方法），两位 reviewer 独立收敛。

评分维持 Borderline (leaning weak accept)，不调整。与 R1 (Weak Accept) 的半档差异来自对 simulation-only venue fit 和 N=3 limitation 的权重分配不同，实质判断一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 414 · 2026-05-22T08:21:22.443546+00:00_

Round 5 审稿已完成。审稿报告已投递至 Research Director。

**结果摘要：**
- Round 4 全部 15 个 issues：**RESOLVED**（R1+R2 一致确认）
- 评分：R1 Weak Accept，R2 Borderline (leaning weak accept) → 综合 **Weak Accept**
- 新发现 5 个 warning + 1 个 critical（Figure 4 placeholder），均为 camera-ready 可修复
- Issue tracker 已更新（15 个 resolved + 6 个 open）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 37

## Round 37

70 recorded events


### User

_source line 415 · 2026-05-23T05:40:27.473814+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: importance_margin_vla_compress
- 论文路径: projects/importance_margin_vla_compress/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-23T05:40:33.504037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-23T05:40:33.705702+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-23T05:40:47.265650+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-23T05:40:47.266007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-23T05:40:51.912200+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-23T05:40:52.465781+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-23T05:40:53.220730+00:00_

{"result":"# 项目 importance_margin_vla_compress 概况\n\n## 实验状态 (483 个)\n\n- **mvp_imm_anchor_v7_1**: DONE (failed) — \n- **mvp_imm_anchor_v6**: DONE (failed) — \n- **mvp_imm_anchor_v5**: DONE (failed) — \n- **mvp_baseline_v4**: DONE (killed) — \n- **mvp_imm_anchor_v4**: DONE (failed) — \n- **mvp_baseline_v3**: DONE (failed) — \n- **mvp_imm_anchor_v2**: DONE (failed) — \n- **mvp_baseline_v2**: DONE (failed) — \n- **mvp_imm_anchor**: DONE (failed) — \n- **mvp_baseline**: DONE (failed) — \n- **eval_openvla_prune_l2norm_k095_seed42**: DONE (success) — \n- **eval_openvla_prune_l2norm_k09_seed42**: DONE (success) — \n- **eval_openvla_prune_l2norm_k05_seed42**: DONE (success) — \n- **eval_openvla_prune_l2norm_k03_seed42**: DONE (success) — \n- **eval_oft_baseline_object_seed42_v2**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- eval_pi05_l2norm_k095_object_seed42_v2: π0.5 L2norm k=0.95 Object seed42 v2: 补充 registry 缺失数据点。k=0.9 L2=98.2%, k=0.85 L2=98.0% 形成 plateau，k=0.95 预期 ≥98.0%。v1 卡在 PREPARING 从未执行。（准备中）\n- eval_pi05_random_k05_long_seed43_v3: π0.5 Random k=0.5 Long seed43 验证。seed42=50.2%。（准备中）\n- eval_pi05_random_k085_long_seed43_v2: π0.5 Random k=0.85 Long seed43 验证。seed42=44.4%。anomaly 验证。（准备中）\n- eval_pi05_l2norm_k085_long_seed43_v3: π0.5 L2Norm k=0.85 Long seed43 验证。seed42=78.0%。L2norm 单调下降验证。（准备中）\n- eval_pi05_random_k03_long_seed43_v4: π0.5 Random k=0.3 Long seed43 验证。seed42=29.0%。V-shape floor 验证。（准备中）\n- eval_pi05_l2norm_k07_long_seed43_v3: π0.5 L2Norm k=0.7 Long seed43 验证。seed42=60.0%, Random k=0.7=64.6%。验证 crossover 在 seed43 是否复现。（准备中）\n- eval_pi05_random_k09_object_seed43_v4: π0.5 Random k=0.9 Object seed43 cliff 验证 v4。seed42=12.0%。v1/v2/v3 均因环境问题失败。本次确保 HF 离线环境变量完整。（准备中）\n- eval_pi05_random_k03_long_seed43_v2（准备中）\n- eval_pi05_l2norm_k07_goal_seed43（准备中）\n- eval_xvla_random_k095_object_seed42（准备中）\n- …另有 28 项\n\n## 近期结论\n- **eval_pi05_random_k095_goal_seed43** (success): π0.5 Random k=0.9
…[truncated 1883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-23T05:40:53.221272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-23T05:40:59.646215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-23T05:41:00.550067+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	
13	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
14	
15	\begin{document}
16	\maketitle
17	
18	\input{abstract}
19	
20	\keywords{vision-language-action models, token pruning, robot learning}
21	
22	\input{introduction}
23	
24	\input{related_work}
25	
26	\input{method}
27	
28	\input{experiments}
29	
30	\input{conclusion}
31	
32	\bibliography{references}
33	
34	\input{appendix}
35	
36	\end{document}
37	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-23T05:41:00.550452+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-23T05:41:01.654896+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-23T05:41:07.428085+00:00_

Web search results for query: "CoRL 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"}]

Based on the search results, here are the key submission guidelines and author instructions for CoRL 2026:

## Paper Format and Length

The page limit is 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit. Reviewers are not required to read the Appendix.

## Required Content

All submissions must include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

Authors are encouraged to submit video, code and data as supplementary materials.

## Generative AI Policy

LLMs or other generative AI tools do not qualify for authorship, and during the paper submission process, authors will be asked to briefly di
…[truncated 680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "WebSearch",
  "elapsed_ms": 6877
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-23T05:41:07.428598+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5773
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-23T05:41:12.098985+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 submission deadline dates 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 submission deadline dates 2026"
  }
}
```

</details>

---


### Tool call

_source line 431 · 2026-05-23T05:41:12.609221+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 instruction for authors template double blind anonymity policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 instruction for authors template double blind anonymity policy"
  }
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-23T05:41:13.262186+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-23T05:41:13.313098+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-23T05:41:15.723679+00:00_

Web search results for query: "CoRL 2026 submission deadline dates 2026"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here are the CoRL 2026 submission deadline dates:

**Abstract Submission Deadline:** May 26, 2026 11:59 UTC

**Paper Submission Deadline:** Thursday (5/28) EOD (Note: One source mentions May 29, 2026 11:59 UTC, but the official instructions clarify the deadline is May 28, not May 29)

**Conference Dates:** November 9–12, 2026 at the JW Marriott Austin in Austin, TX, with a workshop day on November 9 and the main conference on November 10–12


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "WebSearch",
  "elapsed_ms": 3624
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-23T05:41:20.091969+00:00_

Web search results for query: "CoRL 2026 instruction for authors template double blind anonymity policy"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"WACV 2026 Author Reviewer Guides","url":"https://wacv.thecvf.com/Conferences/2026/AuthorReviewerGuides"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CVPR 2026 Author Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"}]

Based on the search results, here is the information about CoRL 2026's double-blind anonymity policy:

CoRL is double-blind, which means all papers must be anonymized. The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced.

The conference also has specific review requirements: The aim is to have at least two reviewers per paper. Additionally, all submissions must include at least one author who agrees to serve as a CoRL reviewer.

Papers may be submitted through OpenReview via the link at https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference.

The instructions for authors page provides the official guidelines for the submission process and anonymity requirements for CoRL 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "WebSearch",
  "elapsed_ms": 7482
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-23T05:41:29.033320+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-23T05:41:29.083969+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-23T05:41:35.663320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-23T05:41:36.015322+00:00_

1	- id: "R4-C1"
2	  summary: "Causal claim under-identified — connector vs backbone/encoder/action confound"
3	  category: framing
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 4
7	  last_seen_round: 5
8	  mentions:
9	    - {round: 4, reviewers: "R1+R2 consensus", note: "determines needs downgrade to associated with"}
10	    - {round: 5, reviewers: "R1+R2 consensus", note: "RESOLVED — full-text causal language downgrade confirmed. No residual 'determines' found."}
11	  action_items:
12	    - {round: 4, action: "Full-text causal language downgrade (determines→associated, controlled→closest available)", assigned_to: "paper_agent", status: "done"}
13	  resolution: "Round 5 verified: determines→strongly associated with, predicts→correlates, falsifies→demonstrates. Appendix N confound analysis added. Both reviewers confirm thorough and consistent."
14	  resolution_round: 5
15	
16	- id: "R4-C2"
17	  summary: "SmolVLA baseline 44.8% vs official — cliff and VTR on undertrained checkpoint"
18	  category: experiment
19	  severity: critical
20	  status: resolved
21	  first_raised_round: 4
22	  last_seen_round: 5
23	  mentions:
24	    - {round: 4, reviewers: "R1+R2 consensus", note: "Official checkpoint full pruning sweep is minimum requirement"}
25	    - {round: 5, reviewers: "R1+R2 consensus", note: "RESOLVED — official checkpoint (57.2% baseline) multi-k verification complete. Dual evaluation protocol in Appendix Table 3."}
26	  action_items:
27	    - {round: 4, action: "SmolVLA official checkpoint pruning sweep (10 configs)", assigned_to: "main_agent", status: "done"}
28	    - {round: 4, action: "Write official results into paper", assigned_to: "paper_agent", status: "done"}
29	  resolution: "Official HF checkpoint (57.2% baseline) shows 0% at k=0.95/0.9/0.5. Dual protocol (59.2%/57.2%) both confirm cliff. VTR M=32 recovers to 60.1±1.3%."
30	  resolution_round: 5
31	
32	- id: "R4-C3"
33	  summary: "CV predictor only 3 models x 2 k = 6 data points, k=0.
…[truncated 14141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-23T05:41:36.166326+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-23T05:41:36.267235+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/results_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments_deprecated.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/related_work_draft.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex
/home/ubuntu/.agent-ml-
…[truncated 792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-23T05:41:45.769550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-23T05:41:46.070989+00:00_

1	\begin{abstract}
2	Removing 5\% of vision tokens collapses SmolVLA from 59.2\% to 0.0\% success rate, while the same reduction on $\pi_0.5$ retains 98.2\% under importance-based selection but only 69.4\% under random selection. Token pruning, well-established for Vision Transformers, transfers unpredictably across Vision-Language-Action (VLA) models because the vision connector governs token compressibility. We analyze this sensitivity along two axes: connector coupling (token-independent vs.\ token-entangling) and task complexity (single-step vs.\ multi-step manipulation). The coefficient of variation (CV) of post-connector token L2 norms, ranging from 0.038 to 0.314 across models, serves as a single-pass diagnostic that correlates with both pruning tolerance and method sensitivity across all three connector families. Token-entangling connectors exhibit task-amplified collapse: X-VLA loses just 1.4 percentage points on single-step Object at 90\% retention but 27.8 percentage points on multi-step Goal tasks (both under random pruning), a $20{\times}$ task-complexity amplification. Low-CV models show 15$\times$ greater sensitivity to pruning method choice than higher-CV models, and at aggressive compression random selection outperforms L2 norm ranking by 36 percentage points for low-CV architectures. For pixel-shuffle connectors where all pruning strategies yield 0.0\%, Vision Token Re-encoder (VTR), a lightweight cross-attention module, recovers over 60\% success rate at 75\% compression through learned re-encoding. Evaluation spans six VLA architectures (450M to 7B parameters), three connector families, and four LIBERO task suites.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-23T05:41:46.071378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-23T05:41:46.122264+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_teaser.pdf}
7	\caption{Two-axis framework for VLA token compressibility. Pruning robustness depends on both connector coupling (token-independent vs.\ token-entangling) and task complexity (single-step vs.\ multi-step). X-VLA loses 1.4\,pp on Object at $k{=}0.9$ but 27.8\,pp on Goal (random pruning), a $20{\times}$ task-complexity amplification.}
8	\label{fig:teaser}
9	\end{figure*}
10	
11	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to 0.0\% across all task suites and pruning methods. Apply the same 5\% reduction to $\pi_0.5$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\ 4B parameters) but the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and a growing body of work extends it to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture.
12	
13	These methods implicitly assume that pruning transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}. Each imposes distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure. No prior work evaluates pruning robustness across both connector architectures and task complexity.
14	
15	We propose a two-axis analysis of VLA token compr
…[truncated 2036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-23T05:41:46.574502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-23T05:41:46.976795+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss. Their success rests on classification's insensitivity to spatial layout; robotic manipulation inverts this assumption, as grasping depends on spatial arrangement. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using language-backbone attention signals. VLA-specific methods have emerged in parallel: VLA-IAP~\cite{cheng2026vlaiap} aligns pruning with action-prediction importance, VLA-Cache~\cite{xu2025vlacache} compresses at the KV-cache level, EfficientVLA~\cite{yang2025efficientvla} combines pruning with merging, and VLA-Pruner~\cite{liu2025vlapruner} learns a pruning policy jointly with the action head. Each validates on a single architecture; no study compares pruning robustness across connector designs.
9	
10	\paragraph{Vision connectors.}
11	The connector between ViT and language backbone governs how spatial information distributes across tokens. LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels, adopted by SmolVLA~\cite{shukor2025smolvla}. These create qualitatively different token dependencies; independent connectors leave patch information separable, while entangling connectors distribute content across tokens. The pruning consequences have not been characterized.
12	
13	We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility, introducing CV of token norms as a single-pass diagnostic that corr
…[truncated 63 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-23T05:41:46.977192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-23T05:41:47.981314+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \emph{coupling}.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_0$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_0.5$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft}, an OpenVLA fine-tuning variant evaluated offline, shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches into each output token's channel dimension (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models ($\pi_0.5$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_0$ and OFT are analyzed via offline metrics only.
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone
…[truncated 4081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-23T05:41:48.082224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-23T05:41:48.183289+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on the LIBERO benchmark~\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.
8	
9	Four models are evaluated in closed-loop robotic control: $\pi_0.5$~\cite{black2025pi05} (4B parameters, linear projection with $\times\!\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\cite{lewis2020bart}, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$ folding, 128 tokens, CV$\,{=}\,$0.314). Two additional models are analyzed via offline metrics only: $\pi_0$~\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\,{=}\,$0.038) and OFT~\cite{kim2025openoft} (7B, three-layer MLP, 512 tokens, CV$\,{=}\,$0.219). All six architectures contribute to the CV diagnostic (Section~\ref{sec:cv_sensitivity}). Table~\ref{tab:model_properties} summarizes model properties and connector details.
10	
11	The pruning protocol applies post-connector token pruning at retention ratios $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$. Two strategies bracket the robustness range: \textbf{L2 norm selection} ranks tokens by L2 norm and retains the top-$k$ fraction, providing an importance-based favorable test; \textbf{random subsampling} selects tokens uniformly at random, providing a conservative lower bound. Both strategies physically remove tokens and re-index position IDs. All results report mean s
…[truncated 12480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-23T05:41:48.183783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-23T05:41:48.234257+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Vision token pruning in VLAs is not a uniform operation: its outcome depends on the interaction between connector architecture and task complexity. Across six VLA architectures (450M--7B) and four LIBERO suites, connector coupling is the primary determinant of pruning robustness. Token-independent connectors degrade proportionally to the fraction removed; token-entangling connectors exhibit task-amplified collapse. SmolVLA's pixel-shuffle produces 0.0\% SR when just 5\% of tokens are removed; X-VLA loses 1.4\,pp on Object at $k{=}0.9$ but 27.8\,pp on Goal under random pruning, a $20{\times}$ amplification. The CV of token L2 norms serves as a single-pass diagnostic that correlates with both pruning tolerance and method sensitivity across all three connector families. For architectures where all pruning strategies fail, VTR recovers a pixel-shuffle VLA from 0.0\% to over 60\% SR at 75\% compression.
5	
6	Two directions remain open: real-robot validation to confirm the connector-complexity interaction transfers beyond simulation, and adaptive per-task pruning schedules that adjust retention ratio to estimated task complexity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-23T05:41:52.771065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-23T05:41:53.776883+00:00_

1	\appendix
2	
3	\section{Extended Discussion}
4	\label{app:discussion}
5	
6	\paragraph{Limitations (extended).}
7	All closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\pi_0$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\pi_0.5$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\% official, 44.8\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.
8	
9	\paragraph{Non-monotonicity as structural property.}
10	X-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\% (L2) and 54.0\% (random), while $k{=}0.9$ recovers to 70.2\% under L2 selection (Table~\ref{tab:main_results}). The 0.2\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.
11	
12	\paragraph{$\pi_0.5$ random subsampling anomaly.}
13	Random selection on $\pi_0.5$ Object collapses from 69.4\% at $k{=}0.95$ to 12.0\% at $k{=}0.9$, then recovers to 77.2\% at $k{=}0.7$ (Table~\ref{tab:main_results}). The V-shaped recovery at more aggressive pruning remains unexplained.
14	
15	\paragraph{Small-$N$ interactions.}
16	X-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\,pp on Goal and $-$47.0\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is s
…[truncated 59151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-23T05:41:54.731497+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-23T05:41:55.284185+00:00_

-rw-r--r-- 1 ubuntu ubuntu 553859 May 23 04:35 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-23T05:41:55.485557+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-23T05:41:55.536690+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'importance_margin_vla_compress'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-23T05:42:01.912034+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-23T05:42:02.615639+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Token Compression (concurrent work)
8	% ============================================================
9	
10	@article{gao2025compressorvla,
11	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
12	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
13	  journal={arXiv preprint arXiv:2511.18950},
14	  year={2025},
15	  eprint={2511.18950},
16	  archivePrefix={arXiv}
17	}
18	
19	@article{wang2025specprunevla,
20	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
21	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
22	  journal={arXiv preprint arXiv:2509.05614},
23	  year={2025},
24	  eprint={2509.05614},
25	  archivePrefix={arXiv}
26	}
27	
28	@inproceedings{jiang2026lightvla,
29	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
30	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
31	  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
32	  year={2026},
33	  eprint={2509.12594},
34	  archivePrefix={arXiv}
35	}
36	
37	@inproceedings{feng2026seewhatmatters,
38	  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},
39	  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},
40	  booktitle={Proceedings of the Forty-Third International C
…[truncated 22880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-23T05:42:03.118336+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/ 2>/dev/null | head -30",
  "description": "List figure files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/ 2>/dev/null | head -30",
    "description": "List figure files"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-23T05:42:04.022307+00:00_

_pdf_images
fig_action_divergence.pdf
fig_architecture.pdf
fig_architecture_v2.pdf
fig_architecture_v2.png
fig_attention_heatmap.pdf
fig_cliff_edge.pdf
fig_cliff_model.pdf
fig_compression_curve.pdf
fig_crosssuite.pdf
fig_crosssuite.png
fig_degradation_curve.pdf
fig_degradation_curve.png
fig_degradation_overview.png
fig_entropy_layers.pdf
fig_entropy_layers.png
fig_method_gap.pdf
fig_method_gap.png
fig_pixel_shuffle.pdf
fig_pruning_overview.pdf
fig_pruning_overview.png
fig_teaser.pdf
fig_teaser.png
fig_token_heatmap.pdf
gen_fig_crosssuite.py
gen_fig_degradation_curve_v4.py
gen_fig_method_gap.py
gen_fig_pruning_overview.py
gen_fig_teaser.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-23T05:42:04.173344+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review configuration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review configuration"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-23T05:42:04.223981+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-23T05:42:08.994264+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/agent/config.yaml 2>/dev/null | head -60",
  "description": "Read project config head"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/agent/config.yaml 2>/dev/null | head -60",
    "description": "Read project config head"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-23T05:42:09.044917+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-23T05:42:12.771005+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
  "description": "Find config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-23T05:42:12.922635+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-23T05:42:17.391219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
  "description": "Find config files in workspace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2 -maxdepth 3 -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -10",
    "description": "Find config files in workspace"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-23T05:42:17.642621+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-23T05:42:22.119682+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2 -maxdepth 4 -name \"*.yaml\" -path \"*/importance_margin*\" 2>/dev/null | head -15",
  "description": "Find YAML files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2 -maxdepth 4 -name \"*.yaml\" -path \"*/importance_margin*\" 2>/dev/null | head -15",
    "description": "Find YAML files in project"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-23T05:42:22.255992+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/dream_registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/writing_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/registry.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/constraints.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/mistakes.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/decisions.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/config/projects/importance_margin_vla_compress.yaml
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/config/secrets/importance_margin_vla_compress/manifest.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 136
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-23T05:42:25.168643+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/config/projects/importance_margin_vla_compress.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check external review in project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/config/projects/importance_margin_vla_compress.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review in project config"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-23T05:42:25.369885+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-23T05:43:02.145807+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-23T05:43:24.803268+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22657
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-23T05:43:24.853971+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "importance_margin_vla_compress",
  "text": "你是 Reviewer 1，负责**方法严谨性和实验有效性**的审查。\n\n## 投稿信息\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **Deadline**: 2026-05-29\n- **页数限制**: 8 页正文（附录/参考文献不计入）\n- **匿名规则**: Double-blind\n- **模板**: CoRL 2026 (`\\usepackage{corl_2026}`)\n- **必须包含**: Limitations section（计入 8 页）\n\n## 论文文件\n- LaTeX 源码: `projects/importance_margin_vla_compress/docs/paper/main.tex`（含 `\\input{abstract}`, `\\input{introduction}`, `\\input{related_work}`, `\\input{method}`, `\\input{experiments}`, `\\input{conclusion}`, `\\input{appendix}`）\n- PDF: `projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. Pruning Protocol 有效性\n- L2 norm selection 和 random subsampling 作为\"bracket\"是否充分？是否遗漏了更有意义的 baseline（如 attention-based scoring、gradient-based 等）？\n- Post-connector pruning 的选择是否有合理 justification？为什么不在 pre-connector 或其他位置 pruning？\n- Position re-indexing after removal 的影响是否被充分讨论？\n\n### 2. CV Diagnostic 的统计基础\n- CV 作为 diagnostic metric 的理论基础是否充分？为什么 L2 norm 的 CV 而非其他统计量（如 entropy、kurtosis）？\n- N=6 models（其中只有 4 个 closed-loop）是否足以建立 CV 与 pruning tolerance 的相关性？\n- CV 的 monotonic relationship 声明（Table scaling_law）是否 overfit 于有限数据点？\n\n### 3. VTR 评估严谨性\n- VTR 训练条件与 baseline 的公平性：batch size 4 vs official 64，是否引入系统偏差？\n- MLP adapter control 的 p=0.15 解读：是否应该用更大的 sample size 来区分？\n- M-curve \"flat\" 的声明——M=96 dip 存在，说 flat 是否过于简化？\n- VTR 在 Goal suite 性能下降 6.6pp，是否应更突出这个限制？\n\n### 4. 统计方法\n- Wilson 95% CI 是否适用于所有条件？\n- Multi-seed 验证覆盖是否充分？哪些关键 claim 只有 single-seed？\n- Table 2 中大量 \"--\" 缺失数据对结论的影响\n- 同一 model 不同条件使用不同 seed（如 OpenVLA L2=seed42, random=seed7）的合理性\n\n### 5. Causal Claims vs Correlational Evidence\n- 论文是否在 connector→pruning tolerance 的关系上做了超出证据支持的因果推断？\n- 注意 confounder analysis（Appendix N）的充分性\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 分 Must-Fix / Should-Fix / Minor） → Questions → Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "importance_margin_vla_compress",
    "text": "你是 Reviewer 1，负责**方法严谨性和实验有效性**的审查。\n\n## 投稿信息\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **Deadline**: 2026-05-29\n- **页数限制**: 8 页正文（附录/参考文献不计入）\n- **匿名规则**: Double-blind\n- **模板**: CoRL 2026 (`\\usepackage{corl_2026}`)\n- **必须包含**: Limitations section（计入 8 页）\n\n## 论文文件\n- LaTeX 源码: `projects/importance_margin_vla_compress/docs/paper/main.tex`（含 `\\input{abstract}`, `\\input{introduction}`, `\\input{related_work}`, `\\input{method}`, `\\input{experiments}`, `\\input{conclusion}`, `\\input{appendix}`）\n- PDF: `projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. Pruning Protocol 有效性\n- L2 norm selection 和 random subsampling 作为\"bracket\"是否充分？是否遗漏了更有意义的 baseline（如 attention-based scoring、gradient-based 等）？\n- Post-connector pruning 的选择是否有合理 justification？为什么不在 pre-connector 或其他位置 pruning？\n- Position re-indexing after removal 的影响是否被充分讨论？\n\n### 2. CV Diagnostic 的统计基础\n- CV 作为 diagnostic metric 的理论基础是否充分？为什么 L2 norm 的 CV 而非其他统计量（如 entropy、kurtosis）？\n- N=6 models（其中只有 4 个 closed-loop）是否足以建立 CV 与 pruning tolerance 的相关性？\n- CV 的 monotonic relationship 声明（Table scaling_law）是否 overfit 于有限数据点？\n\n### 3. VTR 评估严谨性\n- VTR 训练条件与 baseline 的公平性：batch size 4 vs official 64，是否引入系统偏差？\n- MLP adapter control 的 p=0.15 解读：是否应该用更大的 sample size 来区分？\n- M-curve \"flat\" 的声明——M=96 dip 存在，说 flat 是否过于简化？\n- VTR 在 Goal suite 性能下降 6.6pp，是否应更突出这个限制？\n\n### 4. 统计方法\n- Wilson 95% CI 是否适用于所有条件？\n- Multi-seed 验证覆盖是否充分？哪些关键 claim 只有 single-seed？\n- Table 2 中大量 \"--\" 缺失数据对结论的影响\n- 同一 model 不同条件使用不同 seed（如 OpenVLA L2=seed42, random=seed7）的合理性\n\n### 5. Causal Claims vs Correlational Evidence\n- 论文是否在 connector→pruning tolerance 的关系上做了超出证据支持的因果推断？\n- 注意 confounder analysis（Appendix N）的充分性\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 分 Must-Fix / Should-Fix / Minor） → Questions → Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-23T05:43:48.022272+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23168
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-23T05:43:48.124960+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "importance_margin_vla_compress",
  "text": "你是 Reviewer 2，负责**新颖性、相关工作覆盖和论文定位**的审查。\n\n## 投稿信息\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **Deadline**: 2026-05-29\n- **页数限制**: 8 页正文（附录/参考文献不计入）\n- **匿名规则**: Double-blind\n- **模板**: CoRL 2026 (`\\usepackage{corl_2026}`)\n- **必须包含**: Limitations section（计入 8 页）\n\n## 论文文件\n- LaTeX 源码: `projects/importance_margin_vla_compress/docs/paper/main.tex`\n- PDF: `projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. Novelty 评估\n- \"Two-axis framework\"（connector coupling × task complexity）是否构成真正的 intellectual contribution，还是对已知现象的重新包装？\n- CV as diagnostic metric：L2 norm 的 CV 是一个简单的统计量——这是否足以作为一篇 CoRL 论文的核心 contribution？\n- VTR：cross-attention re-encoding 已在 Perceiver/Q-Former/BLIP-2 中广泛使用，VTR 的 novelty 在哪里？\n- 整篇论文的核心发现\"不同 connector 对 pruning 的响应不同\"是否过于 obvious？\n\n### 2. 相关工作覆盖\n- **Concurrent VLA pruning work**：检查是否遗漏关键 concurrent work。特别关注：\n  - \"Don't Run with Scissors\" (Jabbour et al. 2025) — 已引用，但讨论是否充分？该工作也研究 pruning breaks VLA\n  - Compressor-VLA, SpecPrune-VLA, LightVLA, See What Matters (ICML 2026) — 检查引用和对比\n  - VLA-Cache, VLA-IAP, EfficientVLA, VLA-Pruner — 已引用\n- **Vision connector 相关工作**：TokenPacker, InternVL pixel-shuffle, 其他使用 pixel-shuffle 的 VLM/VLA\n- **VLM token pruning**：FastV, PruMerge, SparseVLM, SparseVILA, FitPrune, CrossGET — 检查覆盖\n- 是否有重要的 missing references？\n\n### 3. Contribution Claims 合理性\n- C1 \"two-axis compressibility analysis\"：cross-architecture analysis 的 scope 是否与 claim 匹配？只在 LIBERO 上测，只用了 4 个 closed-loop models\n- C2 \"CV as diagnostic\"：声称 \"enabling connector-appropriate compression strategy selection without downstream evaluation\" 但只有 3 data points 的 correlation\n- C3 \"VTR recovers pixel-shuffle VLA\"：只在 SmolVLA 一个模型上验证，generalization 未知\n\n### 4. 论文定位\n- 这篇论文的 primary identity 是什么？empirical study? diagnostic tool? new method?\n- 对 CoRL 审稿人来说，这篇论文的 actionable takeaway 是什么？\n- 与 \"Don't Run with Scissors\" 的差异化是否清晰？\n\n### 5. 对 CoRL Community 的价值\n- CoRL 读者关心的是 real robot deployment。论文完全基于 LIBERO simulation，这对 CoRL 的价值如何？\n- 实用建议的 actionability：CV diagnostic 需要什么信息？practitioner 真的会用它吗？\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 分 Must-Fix / Should-Fix / Minor） → Questions → Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "importance_margin_vla_compress",
    "text": "你是 Reviewer 2，负责**新颖性、相关工作覆盖和论文定位**的审查。\n\n## 投稿信息\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **Deadline**: 2026-05-29\n- **页数限制**: 8 页正文（附录/参考文献不计入）\n- **匿名规则**: Double-blind\n- **模板**: CoRL 2026 (`\\usepackage{corl_2026}`)\n- **必须包含**: Limitations section（计入 8 页）\n\n## 论文文件\n- LaTeX 源码: `projects/importance_margin_vla_compress/docs/paper/main.tex`\n- PDF: `projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. Novelty 评估\n- \"Two-axis framework\"（connector coupling × task complexity）是否构成真正的 intellectual contribution，还是对已知现象的重新包装？\n- CV as diagnostic metric：L2 norm 的 CV 是一个简单的统计量——这是否足以作为一篇 CoRL 论文的核心 contribution？\n- VTR：cross-attention re-encoding 已在 Perceiver/Q-Former/BLIP-2 中广泛使用，VTR 的 novelty 在哪里？\n- 整篇论文的核心发现\"不同 connector 对 pruning 的响应不同\"是否过于 obvious？\n\n### 2. 相关工作覆盖\n- **Concurrent VLA pruning work**：检查是否遗漏关键 concurrent work。特别关注：\n  - \"Don't Run with Scissors\" (Jabbour et al. 2025) — 已引用，但讨论是否充分？该工作也研究 pruning breaks VLA\n  - Compressor-VLA, SpecPrune-VLA, LightVLA, See What Matters (ICML 2026) — 检查引用和对比\n  - VLA-Cache, VLA-IAP, EfficientVLA, VLA-Pruner — 已引用\n- **Vision connector 相关工作**：TokenPacker, InternVL pixel-shuffle, 其他使用 pixel-shuffle 的 VLM/VLA\n- **VLM token pruning**：FastV, PruMerge, SparseVLM, SparseVILA, FitPrune, CrossGET — 检查覆盖\n- 是否有重要的 missing references？\n\n### 3. Contribution Claims 合理性\n- C1 \"two-axis compressibility analysis\"：cross-architecture analysis 的 scope 是否与 claim 匹配？只在 LIBERO 上测，只用了 4 个 closed-loop models\n- C2 \"CV as diagnostic\"：声称 \"enabling connector-appropriate compression strategy selection without downstream evaluation\" 但只有 3 data points 的 correlation\n- C3 \"VTR recovers pixel-shuffle VLA\"：只在 SmolVLA 一个模型上验证，generalization 未知\n\n### 4. 论文定位\n- 这篇论文的 primary identity 是什么？empirical study? diagnostic tool? new method?\n- 对 CoRL 审稿人来说，这篇论文的 actionable takeaway 是什么？\n- 与 \"Don't Run with Scissors\" 的差异化是否清晰？\n\n### 5. 对 CoRL Community 的价值\n- CoRL 读者关心的是 real robot deployment。论文完全基于 LIBERO simulation，这对 CoRL 的价值如何？\n- 实用建议的 actionability：CV diagnostic 需要什么信息？practitioner 真的会用它吗？\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 分 Must-Fix / Should-Fix / Minor） → Questions → Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-23T05:44:05.973263+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17848
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-23T05:44:06.025352+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "project": "importance_margin_vla_compress",
  "text": "你是 Reviewer 3，负责**写作质量、格式合规和 Limitations/Ethics**的审查。\n\n## 投稿信息\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **Deadline**: 2026-05-29\n- **页数限制**: 8 页正文（附录/参考文献不计入，审稿人不要求读附录）\n- **匿名规则**: Double-blind\n- **模板**: CoRL 2026 (`\\usepackage{corl_2026}`)\n- **必须包含**: Limitations section（计入 8 页）\n- **Generative AI policy**: 需要披露 AI 工具使用\n\n## 论文文件\n- LaTeX 源码: `projects/importance_margin_vla_compress/docs/paper/main.tex`\n- PDF: `projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 格式合规\n- 正文是否在 8 页以内？检查 main text 的 page count\n- 是否使用了正确的 CoRL 2026 模板（`\\usepackage{corl_2026}`，submission 版本而非 camera-ready）？\n- 是否有 double-blind violation？检查作者信息、自引用方式、致谢、代码/数据链接\n- Limitations section 是否存在且在正文中？\n- `\\keywords{}` 是否合规？\n\n### 2. 写作质量\n- Abstract 是否自包含、信息密度是否合适？（当前约 150 词）\n- Introduction 的论证逻辑是否清晰？problem statement → gap → approach → contributions 的流程\n- 术语一致性：CV, token pruning, retention ratio, success rate 等术语是否全文一致？\n- Figure/Table 引用是否正确？每个 Figure/Table 是否在文中被引用？\n- 数字精度：百分比是否一致使用小数位？pp 单位是否正确使用？\n- 语法和拼写检查\n\n### 3. Figure 和 Table 质量\n- Figure 1 (teaser)：是否清晰传达 two-axis framework？\n- Figure 2 (pruning overview)：degradation curve 是否易读？\n- Figure 3 (method gap)：是否有效展示 CV-sensitivity relationship？\n- Table 1 (model properties)：信息是否完整且准确？\n- Table 2 (main results)：布局是否清晰？\"--\" 缺失数据是否过多？\n\n### 4. Limitations 评估\n- 当前 Limitations 是否充分覆盖主要弱点？\n- 是否遗漏了重要 limitation（如 sim-only, single benchmark, limited model diversity within connector type）？\n- Future Work 方向是否合理？\n\n### 5. Reproducibility\n- 训练超参数是否充分披露？\n- 评估协议是否足够详细以支持复现？\n- 是否提到代码/数据发布计划？（注意 double-blind 约束）\n- Checkpoint 来源是否清晰？\n\n### 6. 叙事一致性\n- Abstract 中的数字是否与正文一致？\n- Introduction 中的 contribution 是否与 Experiments 中的证据对齐？\n- Conclusion 是否 overstate findings？\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 分 Must-Fix / Should-Fix / Minor） → Questions → Formatting Issues。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "project": "importance_margin_vla_compress",
    "text": "你是 Reviewer 3，负责**写作质量、格式合规和 Limitations/Ethics**的审查。\n\n## 投稿信息\n- **Venue**: CoRL 2026（Conference on Robot Learning）\n- **Deadline**: 2026-05-29\n- **页数限制**: 8 页正文（附录/参考文献不计入，审稿人不要求读附录）\n- **匿名规则**: Double-blind\n- **模板**: CoRL 2026 (`\\usepackage{corl_2026}`)\n- **必须包含**: Limitations section（计入 8 页）\n- **Generative AI policy**: 需要披露 AI 工具使用\n\n## 论文文件\n- LaTeX 源码: `projects/importance_margin_vla_compress/docs/paper/main.tex`\n- PDF: `projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 格式合规\n- 正文是否在 8 页以内？检查 main text 的 page count\n- 是否使用了正确的 CoRL 2026 模板（`\\usepackage{corl_2026}`，submission 版本而非 camera-ready）？\n- 是否有 double-blind violation？检查作者信息、自引用方式、致谢、代码/数据链接\n- Limitations section 是否存在且在正文中？\n- `\\keywords{}` 是否合规？\n\n### 2. 写作质量\n- Abstract 是否自包含、信息密度是否合适？（当前约 150 词）\n- Introduction 的论证逻辑是否清晰？problem statement → gap → approach → contributions 的流程\n- 术语一致性：CV, token pruning, retention ratio, success rate 等术语是否全文一致？\n- Figure/Table 引用是否正确？每个 Figure/Table 是否在文中被引用？\n- 数字精度：百分比是否一致使用小数位？pp 单位是否正确使用？\n- 语法和拼写检查\n\n### 3. Figure 和 Table 质量\n- Figure 1 (teaser)：是否清晰传达 two-axis framework？\n- Figure 2 (pruning overview)：degradation curve 是否易读？\n- Figure 3 (method gap)：是否有效展示 CV-sensitivity relationship？\n- Table 1 (model properties)：信息是否完整且准确？\n- Table 2 (main results)：布局是否清晰？\"--\" 缺失数据是否过多？\n\n### 4. Limitations 评估\n- 当前 Limitations 是否充分覆盖主要弱点？\n- 是否遗漏了重要 limitation（如 sim-only, single benchmark, limited model diversity within connector type）？\n- Future Work 方向是否合理？\n\n### 5. Reproducibility\n- 训练超参数是否充分披露？\n- 评估协议是否足够详细以支持复现？\n- 是否提到代码/数据发布计划？（注意 double-blind 约束）\n- Checkpoint 来源是否清晰？\n\n### 6. 叙事一致性\n- Abstract 中的数字是否与正文一致？\n- Introduction 中的 contribution 是否与 Experiments 中的证据对齐？\n- Conclusion 是否 overstate findings？\n\n请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 severity 分 Must-Fix / Should-Fix / Minor） → Questions → Formatting Issues。"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-23T05:44:07.636798+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 484 · 2026-05-23T05:44:17.413069+00:00_

Round 1 已启动：

- **视觉审查 Agent**：已派发（fire-and-forget，不阻塞）
- **Reviewer 1**（方法/实验）：已分配
- **Reviewer 2**（新颖性/相关工作）：已分配
- **Reviewer 3**（写作/格式/Limitations）：已分配

等待三位 Reviewer 返回初审报告，收齐后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 485 · 2026-05-23T05:49:04.575340+00:00_

[Reviewer 3 审稿意见]:
## Reviewer 3 审稿报告：写作质量、格式合规与 Limitations/Ethics

**论文标题**: Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility
**Venue**: CoRL 2026

---

## 总体评分
**Overall**: 6/10（Marginally above acceptance threshold）
**一句话总结**: 论文写作整体清晰、论证有条理，但存在一项可能触发 desk rejection 的合规缺失（Generative AI 披露）、主文与附录术语不一致、以及 Limitations 覆盖不充分等问题。

## 官方维度打分（基于 CoRL review form：Originality / Quality / Clarity / Significance / Relevance / Limitations）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Clarity | 3.5/5 | 整体结构清晰，但 VTR/Smart Compress 命名不一致严重影响可读性；LaTeX 渲染错误贯穿全文 |
| Relevance | 4/5 | 直接关系机器人学习中的 VLA 部署效率，符合 CoRL 核心议题 |
| Limitations | 2.5/5 | 主文 Limitations 仅 3 句话，关键局限（sim-only、单 benchmark、connector type 内样本不足）认识不够充分 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 缺少 Generative AI 使用披露
- 具体位置：全文（main.tex 中无任何 AI disclosure 段落）
- 问题：CoRL 2026 Author Instructions 明确要求 "Disclose how generative AI tools were used for research and writing"（https://www.corl.org/contributions/instruction-for-authors）。论文全文无任何相关披露。
- 为什么影响接收：CoRL 2026 明确声明 "Papers with non-existent citations will be desk-rejected"，AI disclosure 同样列为合规要求。缺失可能导致 desk rejection 或至少引发 AC 质疑。
- 建议修改方向：在 Acknowledgments 或 Limitations 末尾添加 AI 工具使用说明（即使未使用也应显式声明）。

**N2** [critical] "VTR" 与 "Smart Compress" 命名不一致
- 具体位置：主文 Section 3.4 定义为 "Vision Token Re-encoder (VTR)"、Section 4.5 使用 "VTR Recovery"；但附录中大量使用 "Smart Compress"——Appendix E (Table 8) "Full Smart Compress ablation"、Appendix F (Table 9) "Smart Compress ($M{=}32$) evaluation"、Appendix G "Smart Compress Training Details"、Table 7 标题 "Smart Compress per-task..."
- 问题：同一模块在主文和附录中使用两个完全不同的名称，读者无法确定 "Smart Compress" 和 "VTR" 是否为同一组件。这不是简称的问题——两个名字没有任何词汇重叠，构成术语混淆。
- 为什么影响接收：术语不一致是 reviewer 降分的常见原因。对于论文的核心贡献之一（VTR），命名混乱直接损害可信度和可理解性。
- 建议修改方向：统一为一个名称（建议 VTR），全文搜索替换 "Smart Compress"。

**N3** [critical] Table 2 缺失数据过多（"--" 条目）
- 具体位置：Table 2（main results，experiments.tex lines 37-67）
- 问题：在核心结果表中，存在大量 "--" 条目：
  - π₀.₅ Goal: k=0.9 Random 缺失, k=0.7 L2 缺失
  - X-VLA Spatial: k=0.7 Random 缺失
  - X-VLA Goal: k=0.5 Random 缺失
  - X-VLA Long: k=0.9 Random 缺失, k=0.7 L2 和 Random 均缺失, k=0.5 L2 和 Random 均缺失
  - OpenVLA: 仅报告 Object 一个 suite（其余三个 suite 完全缺失）
  共计约 11 个 "--" 单元格，占非 SmolVLA 有效数据的约 20%。
- 为什么影响接收：论文声称进行 "cross-architecture, cross-suite analysis"，但最重要的结果表数据严重不完整。特别是 X-VLA Long suite 几乎没有中低 retention ratio 的数据，OpenVLA 只有 Object 一个 suite，无法支撑 "cross-suite" 的 claim。Reviewer 会质疑这些数据是否有意省略了不利结果。
- 建议修改方向：补全缺失实验，或在表格注释中明确解释每个 "--" 的原因（如 "实验未完成" vs "结果为 0%"）。如果是资源限制，应在 Limitations 中承认。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] LaTeX 渲染错误：`$\pi_0.5$` 应为 `$\pi_{0.5}$`
- 具体位置：全文贯穿出现（abstract.tex, introduction.tex, method.tex, experiments.tex 等，超过 50 处）
- 问题：`$\pi_0.5$` 在 LaTeX 中仅将 `0` 作为下标，`.5` 以正文字体显示。正确写法为 `$\pi_{0.5}$`，将 `0.5` 整体下标。同样的问题出现在 `$\pi_0$`（应为 `$\pi_{0}$`，虽然效果相同但不规范）。在 PDF 中，这导致 π₀.5 中的 ".5" 与下标 "0" 不在同一基线，视觉上显得像是数学乘法 π₀ × 0.5。
- 建议：全局搜索替换 `$\pi_0.5$` → `$\pi_{0.5}$`，以及 `$\pi_0$` → `$\pi_{0}$`。

**W2** [warning] Limitations section 过于简短且格式不够突出
- 具体位置：experiments.tex lines 105-106（主文末尾的 `\paragraph{Limitations.}`）
- 问题：CoRL 2026 要求 Limitations section "describe limiting assumptions, failure modes, and other limitations"。当前主文 Limitations 仅 3 句话（约 60 词），以 `\paragraph{}` 而非 `\subsection{}` 或 `\section{}` 形式呈现，在 PDF 中视觉上不够醒目。虽然 Appendix A 有 Extended Discussion 补充，但 CoRL reviewer "not required to read appendix"，意味着 reviewer 可能只看到这 3 句话。
- 遗漏的重要 limitations：
  1. **单一 benchmark**：仅使用 LIBERO，未在其他机器人操控 benchmark（如 RLBench、MetaWorld）验证
  2. **仅 simulation**：CoRL Call for Papers 明确强调 "prioritize real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots"——论文完全缺少 sim-to-real transferability 论证
  3. **Connector type 内样本不足**：pixel-shuffle 仅测试 SmolVLA 一个模型，无法排除 SmolVLA 自身的缺陷（而非 pixel-shuffle 的固有问题）
  4. **VTR 仅在一个架构上验证**：VTR 只在 SmolVLA 上测试，对其他 entangling connector（如 X-VLA 的 BART）是否有效未知
  5. **单种子问题**：Table 2 中多数条件为单种子实验（exceptions: VTR 3-seed, 部分 X-VLA 3-seed）
- 建议：将 Limitations 提升为独立 `\section{Limitations}` 或至少 `\subsection{}`，扩展至 150-200 词覆盖以上关键局限。

**W3** [warning] 缺少代码/数据发布计划
- 具体位置：全文（无任何 code/data availability 声明）
- 问题：CoRL 2026 鼓励提交 code 和 data。论文未提及代码是否会开源、实验数据是否可获取。虽然 double-blind 阶段不应包含可识别链接，但可以声明 "Code and data will be released upon acceptance" 或提供匿名链接。
- 建议：在 Limitations 或 Conclusion 末尾添加代码发布计划声明。

**W4** [warning] Abstract 信息密度过高
- 具体位置：abstract.tex（约 180 词）
- 问题：Abstract 在约 180 词中塞入了过多具体数字（59.2%, 0.0%, 98.2%, 69.4%, 0.038, 0.314, 1.4 pp, 27.8 pp, 20×, 15×, 36 pp, 22M, 5%, 60%, 75%, 450M, 7B），共计约 17 个数字/百分比。信息过载使读者难以把握核心 message。
- 建议：保留 3-4 个最关键数字（如 SmolVLA 5% pruning → 0%、VTR 恢复 60%、6 architectures），其余用定性描述替代。

**W5** [warning] Figure 3 (Method sensitivity) 可读性问题
- 具体位置：Figure 3（experiments.tex line 91-96，PDF page 7）
- 问题：条形图中 X-VLA 和 OpenVLA 的 bar 值均 < 2pp，在与 π₀.₅ 的 15-29pp bars 同尺度下几乎不可见。"1.4" 和 "0.2" 标签字体极小。15× 标注虽然有用但增加了视觉噪音。
- 建议：考虑使用 broken axis 或 log scale，或在 bar 旁用大字标注具体数值。

---

## 小问题（不影响接收）

- abstract.tex line 2：`$\pi_0.5$` 前有 `on` 缺少空格（"reduction on$\pi_0.5$" → "reduction on $\pi_0.5$"）——实际渲染可能正常，但源码不清晰
- experiments.tex line 40 caption："``--'' indicates data not yet collected" 承认数据未收集，这比 "--" 无解释好，但在正式投稿中不够专业
- method.tex line 9：`$\times\!\sqrt{d}$-scaled` 中 `\!` 负间距的使用是否必要？视觉上较紧凑
- related_work.tex：Related Work 段落较短（约 200 词），对 VLA pruning 的相关工作（VLA-IAP, VLA-Cache, EfficientVLA, VLA-Pruner）仅一句话带过，缺少具体方法对比
- 附录中部分 table caption 过长（如 Table 14 caption 超过 5 行），可精简

---

## 叙事一致性检查

| 检查项 | 结果 |
|--------|------|
| Abstract 数字与正文一致 | ✅ "59.2% to 0.0%"、"98.2%"、"60% at 75%" 均与 experiments section 一致 |
| Introduction contributions 与 Experiments 证据对齐 | ✅ 三条 contribution 均有对应实验支撑 |
| Conclusion 是否 overstate | ⚠️ Conclusion 说 "connector coupling is the primary determinant"，但 confounders（backbone, encoder, scale）未充分控制，"primary" 过强——Appendix I 自己也承认 "preventing clean isolation" |
| 术语一致性 | ❌ VTR vs Smart Compress（见 N2）；其余术语（CV, SR, pp, retention ratio）全文一致 |
| Figure/Table 引用完整 | ✅ 主文中所有 Figure 和 Table 均被引用 |

---

## 格式合规总结

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 8 页限制 | ✅ | 主文 8 页，References 从 page 9 开始 |
| CoRL 2026 模板 | ✅ | `\usepackage{corl_2026}` submission 版本 |
| Double-blind | ✅ | "Anonymous Authors"，无可识别自引或致谢 |
| Limitations section | ⚠️ | 存在但过短（3 句话），格式为 paragraph 而非 section |
| `\keywords{}` | ✅ | 合规 |
| Generative AI 披露 | ❌ | **完全缺失** |
| 代码/数据声明 | ❌ | 未提及 |

---

## 主要优势

- **结构清晰**：Introduction 的 problem → gap → approach → contributions 流程逻辑严密，读者能快速理解 motivation
- **数据呈现规范**：Wilson 95% CI、多种子验证（VTR 3-seed）、per-task breakdown 均体现了实验严谨性
- **附录详尽**：18 页附录提供了丰富的 ablation、per-task 分析、超参数细节，远超 CoRL 平均水平
- **Figure 1 (teaser) 效果好**：两轴框架的可视化直观传达了核心 message，connector coupling × task complexity 的交互一目了然
- **Table 1 (model properties) 设计精简**：6 个模型的关键属性一目了然，CV 排序的呈现方式支持论文论点

---

## 总结

写作整体水准较高，论证逻辑清晰，数据呈现规范。但存在三个影响接收决定的问题：(1) Generative AI 披露缺失可能触发合规审查；(2) VTR/Smart Compress 命名不一致损害论文核心贡献的可信度；(3) Table 2 缺失数据过多，削弱 cross-suite analysis 的 claim。Limitations section 需要实质性扩展以满足 CoRL 的要求。建议在提交前优先修复 N1-N3。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 486 · 2026-05-23T05:49:21.623656+00:00_

收到 Reviewer 3 的审稿报告，记录关键发现。等待 Reviewer 1 和 Reviewer 2 的报告后进入交叉分享阶段。

**R3 要点摘要：**
- **N1** [critical]: 缺少 Generative AI 披露（CoRL 合规要求）
- **N2** [critical]: VTR vs Smart Compress 命名不一致
- **N3** [critical]: Table 2 缺失数据 ~20%，削弱 cross-suite claim
- **W1-W5**: LaTeX 渲染错误（π₀.₅）、Limitations 过短、无代码发布计划、Abstract 数字过多、Figure 3 可读性
- **评分**: 6/10

当前状态：R3 ✅ | R1 ⏳ | R2 ⏳ | 视觉审查 ⏳

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 39

## Round 39

2 recorded events


### User

_source line 487 · 2026-05-23T05:49:24.278937+00:00_

[Reviewer 3 审稿结果]:
审稿报告已提交给 Review Director。

**审查结论**：Overall 6/10。发现 3 个 Must-Fix 问题：

1. **Generative AI 披露完全缺失** — CoRL 2026 明确要求，可能触发 desk rejection
2. **VTR vs Smart Compress 命名不一致** — 主文用 "VTR"，附录用 "Smart Compress"，核心贡献术语混乱
3. **Table 2 缺失数据过多** — 约 20% 条目为 "--"，削弱 cross-suite analysis 的 claim

另有 5 个 Should-Fix：LaTeX 渲染错误（`$\pi_0.5$` 全文 50+ 处）、Limitations 过短（3 句话）、无代码发布声明、Abstract 信息过载、Figure 3 可读性差。

写作整体水准较高，结构清晰，附录详尽（18 页），但合规问题和术语不一致需在提交前优先修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_3"
}
```

</details>

---


### Assistant

_source line 488 · 2026-05-23T05:49:29.477471+00:00_

收到 Reviewer 3 的报告。等待 Reviewer 1 和 Reviewer 2 的结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 40

## Round 40

2 recorded events


### User

_source line 489 · 2026-05-23T05:50:03.624664+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others

**审查侧重**：新颖性、相关工作覆盖、Contribution Claims 合理性、论文定位、CoRL Community 价值

---

## 总体评分

**Overall**: 5/10（Borderline — 有价值的 empirical observations 但 contributions 各自不够深入）

**一句话总结**：论文提出了有意义的 empirical 发现（connector coupling 决定 pruning robustness），但三个 contribution 各自的 evidence base 都偏薄——two-axis framework 是合理的 organizational lens 而非 intellectual contribution，CV diagnostic 只有 3 个有效数据点，VTR 只在一个模型上验证。

---

## 官方维度打分（基于 CoRL 2023 Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 2/5 | Two-axis framework 是 organizing principle 而非发现；CV 是标准统计量的直接应用；VTR 的 cross-attention 机制在 Perceiver/Q-Former/BLIP-2 中已广泛使用 |
| Quality | 3/5 | 实验设计系统但有明显空缺（Table 2 大量 "--" 数据、OpenVLA 只评了 Object suite）；CV diagnostic 的 correlation 证据不足 |
| Clarity | 4/5 | 写作清晰，结构合理，Figure 1 teaser 有效传达核心信息；附录详尽 |
| Significance | 2/5 | 对 CoRL 的 actionable impact 有限——仅 simulation，CV diagnostic 的实用门槛不明确，practitioner 难以直接使用 |
| Relevance | 3/5 | 与 robot learning 相关但缺乏 real-robot 验证；LIBERO simulation 是合理 benchmark 但不足以支撑 CoRL 级别的 significance |
| Limitations | 4/5 | 论文诚实承认了 simulation-only 和 causal isolation 的局限；Appendix A 的 extended discussion 有价值 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] CV Diagnostic 的 Evidence Base 严重不足——3 个数据点不能建立可靠的 diagnostic tool

- 具体位置：Section 4.4 (CV as Sensitivity Indicator)、Table 1
- 问题：论文声称 CV "enables connector-appropriate compression strategy selection without downstream evaluation"（Introduction, C2），但支撑这一 claim 的 closed-loop 数据仅来自 3 个模型（π₀.5 CV=0.055, X-VLA CV=0.151, OpenVLA CV=0.215）。SmolVLA (CV=0.314) 在所有条件下均为 0% SR，无法提供 method sensitivity 信息。离线模型 π₀ 和 OFT 贡献了 CV 值但无 closed-loop 验证。用 3 个数据点建立"无需下游评估即可选择压缩策略"的 diagnostic tool，在统计上不可靠，在实践中不可用。
- 为什么影响接收：C2 是论文的核心 contribution 之一。如果 CV diagnostic 的 evidence 不足以支撑其 claim，论文的 contribution 显著缩水。一个需要 CoRL 读者信任但只有 3 个 calibration 点的 diagnostic tool，在 rigorous review 下难以通过。
- 建议修改方向：(a) 大幅降低 CV diagnostic 的 claim 强度，将其定位为 "preliminary observation" 而非 "enabling diagnostic"；(b) 增加更多 VLA 架构的 closed-loop 评估（如 RT-2, CogACT 等），至少达到 6+ 个数据点；(c) 或者将 CV 从核心 contribution 降级为 analysis tool。

**N2** [critical] 论文 identity 分裂——empirical study / diagnostic tool / method 三者均不够深入

- 具体位置：Contributions list (Introduction, lines 19-24)
- 问题：论文同时声称三个 contribution：(C1) two-axis compressibility analysis, (C2) CV diagnostic, (C3) VTR method。但每个都不够深入独立成文：C1 只在 LIBERO 上测了 4 个 closed-loop 模型，Table 2 大量 "--" 缺失数据；C2 只有 3 个有效数据点（见 N1）；C3 只在 SmolVLA 一个模型上验证，且 MLP adapter 达到 comparable 性能（63.4% vs 60.1%, p=0.15, Section 4.5）说明 cross-attention 并非关键机制。这种"三个 shallow contribution 拼凑"的结构容易被 reviewer 认为每个 contribution 都是 incremental。
- 为什么影响接收：CoRL reviewer 期望看到一个 deep contribution 或一个 thorough empirical study。当前状态下论文两头不靠——method contribution 太薄（单模型验证 + MLP adapter 平替），empirical study 不够 thorough（数据缺失 + 模型数量少）。
- 建议修改方向：选定一个 primary identity 并深化。如果定位为 empirical study，补全 Table 2 所有缺失数据并增加模型/benchmark；如果定位为 method paper，在多个 entangling-connector 模型上验证 VTR。

**N3** [critical] Table 2 数据大量缺失，削弱 cross-architecture analysis 的可信度

- 具体位置：Table 2 (Section 4.2)
- 问题：Table 2 是论文核心实验表格，但存在大量 "--" 条目：π₀.5 的 Goal suite 在 k=0.9 (Random) 和 k=0.7 (L2) 缺失；X-VLA 的 Long suite 在 k=0.9, 0.7, 0.5 大部分缺失；X-VLA 的 Goal 和 Spatial 也有缺失；OpenVLA 只评估了 Object 一个 suite。论文声称进行 "cross-architecture analysis across four LIBERO suites"，但实际数据矩阵的填充率不足 70%。
- 为什么影响接收：数据缺失直接损害论文的核心 claim。"Two-axis framework" 需要 connector × complexity 的完整交叉数据来验证。缺失的恰恰是高复杂度任务（Long, Goal）的数据，而这些正是 task-complexity axis 的关键证据。
- 建议修改方向：补全所有缺失的实验数据。这是一篇 empirical 论文，数据完整性是底线。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] VTR 的 novelty 不足——cross-attention re-encoding 是已知技术，MLP adapter 达到 comparable 性能

- 具体位置：Section 3.4, Section 4.5
- 问题：VTR 使用 learned queries 通过 cross-attention 聚合源 tokens——这与 Perceiver（Jaegle et al. 2021, 论文已引用）、Q-Former/BLIP-2（Li et al. 2023, 已引用）的机制本质相同。论文自身的消融实验显示 parameter-matched MLP adapter 达到 63.4% vs VTR 的 60.1%（p=0.15），说明 cross-attention 并非关键——任何 re-encoding 都能恢复。VTR 的 contribution 因此降级为"对 pixel-shuffle VLA 应用已知 re-encoding 技术"。
- 建议：(a) 诚实承认 VTR 的 mechanism novelty 有限，强调 finding 的价值（即"pixel-shuffle collapse 可通过任何 re-encoding 恢复"）；(b) 探索 VTR 是否可以泛化到 X-VLA 的 BART encoder 等其他 entangling connector。

**W2** [warning] 与 "Don't Run with Scissors" (Jabbour et al. 2025) 的差异化讨论不足

- 具体位置：Section 2 (Related Work), Section 1 (Introduction)
- 问题：Jabbour et al. 也发现 pruning breaks VLA 并提出 recovery method (GLUESTICK)。当前论文在 Related Work 中仅列出引用（Section 2, paragraph 2 中与其他 VLA-specific methods 一起提及），没有专门的比较段落。两篇论文的核心发现重叠度高：都发现 pruning 对 VLA 有破坏性影响。本文的差异化（connector architecture 作为 root cause 解释、CV diagnostic、VTR vs GLUESTICK 的不同 recovery 路线）应在正文中明确讨论。
- 建议：在 Related Work 或 Introduction 中增加一个专门段落，对比本文与 Jabbour et al. 在 (1) 问题诊断维度、(2) recovery 方法、(3) 实验范围 上的差异。

**W3** [warning] Two-axis framework 可能是对已知现象的 re-packaging

- 具体位置：Section 4.2, Figure 1
- 问题：(a) Connector coupling axis："pixel-shuffle 破坏空间信息因此不可 pruning"——这从 pixel-shuffle 的定义就可以直接推导出来（4×4 folding 使每个 token 编码 16 个 patch，任何移除都丢失 6.25% 的空间场），Section 4.3 实际上确认了这一点。(b) Task complexity axis："多步任务比单步任务对 pruning 更敏感"——这是 error compounding 的标准结论。将这两个已知现象组合成 "two-axis framework" 并声称为 contribution，有过度包装之嫌。
- 建议：(a) 承认各轴的 individual observation 并非完全新颖，强调 cross-architecture systematic validation 和两轴交互的量化（如 20× amplification）才是贡献；(b) 讨论为什么 practitioner 之前没有系统验证过这些假设。

**W4** [warning] 仅在 LIBERO simulation 上评估，缺乏 real-robot 验证——对 CoRL 论文价值有折扣

- 具体位置：Section 4.1, Limitations (Section 4.5 末尾)
- 问题：CoRL 的核心受众关心 real robot deployment。论文完全基于 LIBERO simulation benchmark（4 个 task suite × 10 tasks × 50 episodes）。虽然 Limitations 中承认了这一点，但缺乏任何对 sim-to-real transfer 的讨论。Compressor-VLA（concurrent work）已包含 real-robot 验证，这使得本文在 practical relevance 上处于劣势。
- 建议：至少在 1-2 个真实机器人任务上验证核心发现（即 connector type 确实影响 pruning robustness），或详细讨论为什么 LIBERO 上的发现应该 transfer 到真实场景。

**W5** [warning] OpenVLA 仅评估了 Object suite，未扩展到其他 LIBERO suites

- 具体位置：Table 2
- 问题：OpenVLA 是论文中唯一的 high-CV independent-connector 模型（CV=0.215），对于验证 "independent connector degrade gracefully across task complexity" 至关重要。但 Table 2 仅报告了 Object suite 的结果。缺少 Spatial/Goal/Long 数据意味着 OpenVLA 在 task-complexity axis 上完全没有验证。
- 建议：补全 OpenVLA 在 Spatial、Goal、Long suites 的数据。

---

## 小问题（不影响接收）

- **M1**: Table 2 中 π₀.5 在 k=0.9 的 Random SR 为 12.0%（Object），但在 k=0.7 反弹至 77.2%，k=0.5 为 69.4%。这种非单调性在正文中简要提及但未充分解释。建议讨论是否为统计波动（单 seed）或系统性现象。
- **M2**: 论文使用 "single-seed" 评估（500 episodes per condition），但部分结论（如 20× amplification）依赖于精确的 SR 数值。建议报告多 seed 结果或至少在附录中验证关键发现的 seed 稳定性。Section 4.5 VTR 用了 3 seeds，但主实验没有。
- **M3**: Abstract 中说 "six VLA architectures (450M to 7B)"，但只有 4 个做了 closed-loop 评估，另外 2 个（π₀, OFT）仅有 offline metrics。应在 abstract 中更精确地描述。
- **M4**: 引用格式小问题——π₀.5 在论文中写作 "$\pi_0.5$"，但标准写法应为 "$\pi_{0.5}$"（下标）。当前形式在某些渲染中可能出现歧义。

---

## Questions to Authors

**Q1**: Table 2 中 π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0%，但 k=0.7 和 k=0.5 时 Random SR 反弹到 77.2% 和 69.4%。这是否为单一 seed 的随机波动？是否在其他 seed 上复现？

**Q2**: MLP adapter 达到与 VTR comparable 的性能（63.4% vs 60.1%, p=0.15）。作者如何看待这一结果？这是否说明 cross-attention 机制并非关键，而是"任何 re-encoding 都足以恢复 pixel-shuffle collapse"？如果是这样，VTR 作为 contribution 的 value proposition 是什么？

**Q3**: CV diagnostic 的 practical workflow 是什么？一个 practitioner 拿到新的 VLA 模型，计算了 CV 值，然后呢？具体的 decision threshold 是多少？论文是否建议 CV < X 用 L2 norm, X < CV < Y 用 random, CV > Y 不要 prune？3 个数据点如何确定这些 threshold？

**Q4**: "Don't Run with Scissors" 的 GLUESTICK 是 training-free 的 recovery 方法，VTR 需要训练。作者是否在 SmolVLA 上比较过 GLUESTICK 和 VTR？如果没有，为什么？

**Q5**: 论文在 Section 4.2 报告 X-VLA Long suite 在 k=0.95 就从 94.0% 崩溃到 47.0%（仅移除 3 个 token 中的约 2.5 个），但 BART encoder 的 50 token 序列长度本身就很短。是否有可能 X-VLA 的脆弱性主要来自极短的 token 序列（50 tokens, 移除 2-3 个即占 5%），而非 BART entangling 本身？

---

## Missing References

所有 16 个 Director 指定检查的 concurrent work 均已引用。以下为建议补充：

1. **A Survey on Efficient Vision-Language-Action Models** (2025, arXiv:2510.24795) — 提供 VLA efficiency 方向的全景综述，有助于读者定位本文。
2. **ATP-LLaVA** (Adaptive Token Pruning for Large Vision Language Models) — 与 FastV/PruMerge 同方向的 VLM pruning work，可在 ViT token pruning 段落补充。

---

## 主要优势

- **S1**: 系统性的 cross-architecture 实验设计（6 个模型 × 3 种 connector family × 2 种 pruning 策略 × 6 个 retention ratio），在 VLA pruning 文献中范围最广。
- **S2**: SmolVLA pixel-shuffle 在 5% pruning 即 catastrophic collapse 的发现是 non-trivial 的，对 practitioners 有直接预警价值。
- **S3**: 写作质量高，结构清晰，Figure 1 teaser 有效传达核心信息，附录详尽（27 页包括大量 per-task 分析）。
- **S4**: Limitations section 诚实且有实质内容，承认了 simulation-only 和 confounders 的问题。
- **S5**: VTR 在 SmolVLA 上从 0% 恢复到 ~60% SR（与 baseline 59.2% 持平），在 75% compression 下实现，这是一个有价值的 proof-of-concept。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 490 · 2026-05-23T05:50:21.603630+00:00_

Reviewer 2 报告已收录（5/10 Borderline）。Reviewer 3 报告已收录（6/10 Marginally above threshold）。

等待 Reviewer 1 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 491 · 2026-05-23T05:50:24.308125+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心评价：论文提出了有价值的 empirical 发现（connector coupling 是 pruning robustness 的主要决定因素），但三个 contribution 各自证据不足：

1. **CV diagnostic 只有 3 个有效数据点**，不足以建立可靠的 diagnostic tool
2. **Table 2 数据大量缺失**（填充率不足 70%），削弱 cross-architecture analysis 的说服力
3. **VTR 仅在 SmolVLA 一个模型上验证**，且 MLP adapter 达到 comparable 性能（p=0.15），说明 cross-attention 并非关键机制

总体评分 5/10（Borderline），主要因为论文 identity 分裂（empirical study / diagnostic / method 三者均不够深），且纯 simulation 评估对 CoRL 的 practical relevance 打折。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 492 · 2026-05-23T05:50:29.490556+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 42

## Round 42

8 recorded events


### User

_source line 493 · 2026-05-23T05:51:48.602522+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性与实验有效性

### 总体评分

**Overall**: 5/10（略低于接收线）
**Confidence**: 4/5

**一句话总结**: 论文提出的 pixel-shuffle 崩溃机制解释清晰且可验证，但核心 CV diagnostic claim 仅基于 N=4 个闭环模型，统计支撑不足以建立通用诊断工具；因果叙事在 connector 与 backbone/训练数据/token 数量等混淆因子未被控制的情况下被过度推断。

### 官方维度打分（基于 CoRL/OpenReview 评审维度）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Originality | 6/10 | Token pruning for VLAs 已有先行工作（VLA-Cache, VLA-Prompt），但 connector-centric 两轴分析框架和 pixel-shuffle 崩溃机制是新贡献 |
| Quality | 4/10 | CV diagnostic 仅 N=4 闭环数据点，monotonic claim 统计不可靠；因果推断超出证据范围；缺少 attention-based pruning baseline |
| Clarity | 7/10 | 写作清晰，Figure 1-3 信息密度高，Two-axis framework 直观，Appendix 组织有序 |
| Significance | 5/10 | 对 VLA 部署有实用参考价值，但 CV diagnostic 泛化性存疑，VTR 贡献被 MLP adapter 控制实验削弱 |
| Relevance | 8/10 | 直接关联机器人学习中的模型压缩与部署效率 |
| Limitations | 7/10 | 诚实报告了 simulation-only、架构混淆等限制，但部分关键限制在正文中被淡化 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] CV diagnostic 的统计基础不足：N=4 闭环模型无法建立可靠的诊断关系

- 具体位置：Section 3.3, Section 4.4, Table 1 (p.4), Appendix S Table 20 (p.26)
- 问题：论文声称 CV 是"single-pass diagnostic that correlates with both pruning tolerance and method sensitivity"（Section 3.3），但闭环验证仅覆盖 4 个模型（π₀.5, X-VLA, OpenVLA, SmolVLA），加上 2 个开环模型共 6 个数据点。任何 4-6 个单调排列的数据点都可以被几乎任何单调函数拟合，"monotonic relationship"声明在统计上等价于观察到一个排列的概率 ≤ 1/4! = 1/24。论文未提供正式的相关性检验（如 Spearman rank correlation 及其 p-value），也未讨论所需样本量。
- 为什么影响接收：论文核心贡献之一是将 CV 作为无需闭环评估的诊断工具，但基于 4 个数据点的经验关系缺乏泛化可信度。
- 建议修改方向：(a) 增加至少 3-5 个额外 VLA 架构验证，(b) 提供正式统计检验，(c) 或将 claim 降级为"initial observation"。

**N2** [critical] 因果叙事超出证据范围：Connector → pruning tolerance 因果推断缺乏控制

- 具体位置：Title, Section 1, Section 5, Appendix N (p.25)
- 问题：标题和核心叙事强烈暗示 connector 架构因果决定 pruning tolerance 差异，但被比较的模型同时在 LLM backbone（Phi/Gemma/Llama-2/Qwen）、预训练数据、vision token 数量（768 vs. 256 vs. 126）、训练策略上不同。Appendix N 承认"a matched backbone experiment remains the ideal control"，但正文 Section 5 仍使用"primary determinant"措辞。
- 为什么影响接收：无匹配实验（同一 backbone + 不同 connector）无法排除混淆因子。如果 pruning tolerance 实际由 backbone 或 token 数量主导（如 π₀.5 的 768 tokens 本身提供更多冗余），则 connector-centric 框架核心前提不成立。
- 建议修改方向：(a) 进行 matched-backbone 实验，或 (b) 将因果语言全面降级为相关性语言。

**N3** [critical] 缺少关键 pruning baseline：L2 norm 和 random 不构成充分的方法 bracket

- 具体位置：Section 3.2, Table 2, Appendix E.10 (p.16)
- 问题：更有意义的 importance scoring 方法未被评估——attention-based scoring（VLA-Cache 和 FastV 已采用的标准方法）和 gradient-based importance 完全缺失。Appendix E.10 进一步表明在 OpenVLA 上 L2 norm 和 random 表现相近（差距 <3pp），说明 L2 norm 并非总是有效的 importance score。
- 为什么影响接收：attention-based pruning 是 VLA token pruning 最自然的竞争方法。如果 attention-based 大幅优于 L2 norm，论文关于 method gap 小的核心发现可能不成立。
- 建议修改方向：至少在主要模型上加入 attention-based scoring baseline。

---

### Should-Fix 问题

**W1** [warning] VTR 贡献被 MLP adapter 控制实验严重削弱
- Section 4.5: MLP adapter 达到统计不可区分的性能（p=0.15），意味着 VTR 的 cross-attention 架构无显著优势。正文仍以 VTR 为主角展开，造成误导。

**W2** [warning] VTR 训练条件不公平：batch size 4 vs. 64
- Section 4.5, Appendix U: VTR 用 batch size 4 单 GPU 训练，官方 SmolVLA 用 batch size 64/8 GPU。60%+ SR 恢复率与 59.2% baseline 的直接对比存在系统偏差。

**W3** [warning] 跨条件使用不同 seed 引入潜在混淆
- Table 2, Appendix C: OpenVLA L2 pruning 用 seed 42，random 用 seed 7。仅 Appendix E.9 提供 OpenVLA 的 2-seed 一致性检查，其余三个模型未验证。

**W4** [warning] Table 2 大量缺失数据限制跨模型比较
- SmolVLA 全部 0.0% 显示为"--"，应报告具体数值。建议补充更细粒度 k 值（k=0.98, 0.99）精确定位崩溃阈值。

**W5** [warning] Post-connector pruning 缺乏系统 justification
- Section 3.2: 未讨论 pre-connector pruning 的可能性。Position re-indexing 影响仅在 SmolVLA 上分析，未系统测试保持原始 position ID 的替代方案。

**W6** [warning] CV 选择的理论动机不足
- Section 3.3, Appendix I: 未比较 CV vs. entropy/kurtosis/Gini coefficient 作为 diagnostic 的效果。Appendix I 的 attention entropy 分析与 CV 互补但独立，为何不采用？

---

### 小问题
- Section 4.4: "method gap" 术语未在 Section 3.2 中正式定义
- Figure 2: 低 CV 模型曲线在高 retention ratio 端难以区分
- Appendix E.7: 空间分布分析仅对 π₀.5 进行
- 正文 p.1 "99.4%" 与 Table 2 中 π₀.5 的 98.2% (k=0.95) 不完全一致

### Questions to Authors
1. 同一 LLM backbone 搭配不同 connector，CV-pruning tolerance 关系是否成立？
2. Attention-based scoring 是否改变 Figure 3 中 method gap？
3. SmolVLA k=0.99（仅移除 1 token）是否仍崩溃？
4. VTR 在 batch size 64 下是否达到相同性能？
5. Pruning 后保持原始 position ID（不 re-index）结果是否变化？

### Missing References
- SparseVLM [Zhang et al., 2024]: text-informed vision token selection
- LLaVA-PruMerge [Shang et al., 2024]: pruning + merging
- TokenPacker [Li et al., 2024]: coarse-to-fine 视觉 token 压缩

### 主要优势
- SmolVLA pixel-shuffle 崩溃机制（Section 4.3）发现扎实，经双 checkpoint 验证
- Two-axis framework 提供有用的分析组织结构
- Appendix 实验覆盖面广（hypergeometric 模型、attention entropy、confounder 分析）
- Wilson CI + 500 episodes/condition 是合理的统计实践
- 诚实报告关键限制

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-23T05:52:20.818538+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "importance_margin_vla_compress",
  "text": "## 交叉分享：请逐条回应 Reviewer 2 和 Reviewer 3 的审稿意见\n\n请对以下两份审稿报告中的每个 Must-Fix 和 Should-Fix 条目逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 的审稿报告（新颖性/定位/相关工作）\n\n### Must-Fix:\n**R2-N1**: CV Diagnostic 的 Evidence Base 严重不足——3 个数据点不能建立可靠的 diagnostic tool。论文声称 CV \"enables connector-appropriate compression strategy selection without downstream evaluation\"，但支撑这一 claim 的 closed-loop 数据仅来自 3 个模型（π₀.5 CV=0.055, X-VLA CV=0.151, OpenVLA CV=0.215）。SmolVLA (CV=0.314) 在所有条件下均为 0% SR，无法提供 method sensitivity 信息。\n\n**R2-N2**: 论文 identity 分裂——empirical study / diagnostic tool / method 三者均不够深入。C1 只在 LIBERO 上测了 4 个 closed-loop 模型，Table 2 大量缺失数据；C2 只有 3 个有效数据点；C3 只在 SmolVLA 一个模型上验证，且 MLP adapter 达到 comparable 性能。\n\n**R2-N3**: Table 2 数据大量缺失（填充率不足 70%），削弱 cross-architecture analysis 的可信度。\n\n### Should-Fix:\n**R2-W1**: VTR 的 novelty 不足——cross-attention re-encoding 是已知技术，MLP adapter 达到 comparable 性能。\n**R2-W2**: 与 \"Don't Run with Scissors\" 差异化讨论不足。\n**R2-W3**: Two-axis framework 可能是对已知现象的 re-packaging。\n**R2-W4**: 仅在 LIBERO simulation 上评估，缺乏 real-robot 验证。\n**R2-W5**: OpenVLA 仅评估了 Object suite。\n\n---\n\n## Reviewer 3 的审稿报告（写作/格式/Limitations）\n\n### Must-Fix:\n**R3-N1**: 缺少 Generative AI 使用披露——CoRL 2026 明确要求。\n**R3-N2**: \"VTR\" 与 \"Smart Compress\" 命名不一致——主文用 VTR，附录大量使用 Smart Compress。\n**R3-N3**: Table 2 缺失数据过多（约 20% 条目为 \"--\"）。\n\n### Should-Fix:\n**R3-W1**: LaTeX 渲染错误 `$\\pi_0.5$` 全文 50+ 处。\n**R3-W2**: Limitations section 过于简短（3 句话），遗漏关键局限。\n**R3-W3**: 缺少代码/数据发布计划。\n**R3-W4**: Abstract 信息密度过高（17 个数字/百分比）。\n**R3-W5**: Figure 3 可读性问题。\n\n---\n\n请逐条回应，重点关注你的专长领域（方法严谨性/实验有效性）的交叉点。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "importance_margin_vla_compress",
    "text": "## 交叉分享：请逐条回应 Reviewer 2 和 Reviewer 3 的审稿意见\n\n请对以下两份审稿报告中的每个 Must-Fix 和 Should-Fix 条目逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 的审稿报告（新颖性/定位/相关工作）\n\n### Must-Fix:\n**R2-N1**: CV Diagnostic 的 Evidence Base 严重不足——3 个数据点不能建立可靠的 diagnostic tool。论文声称 CV \"enables connector-appropriate compression strategy selection without downstream evaluation\"，但支撑这一 claim 的 closed-loop 数据仅来自 3 个模型（π₀.5 CV=0.055, X-VLA CV=0.151, OpenVLA CV=0.215）。SmolVLA (CV=0.314) 在所有条件下均为 0% SR，无法提供 method sensitivity 信息。\n\n**R2-N2**: 论文 identity 分裂——empirical study / diagnostic tool / method 三者均不够深入。C1 只在 LIBERO 上测了 4 个 closed-loop 模型，Table 2 大量缺失数据；C2 只有 3 个有效数据点；C3 只在 SmolVLA 一个模型上验证，且 MLP adapter 达到 comparable 性能。\n\n**R2-N3**: Table 2 数据大量缺失（填充率不足 70%），削弱 cross-architecture analysis 的可信度。\n\n### Should-Fix:\n**R2-W1**: VTR 的 novelty 不足——cross-attention re-encoding 是已知技术，MLP adapter 达到 comparable 性能。\n**R2-W2**: 与 \"Don't Run with Scissors\" 差异化讨论不足。\n**R2-W3**: Two-axis framework 可能是对已知现象的 re-packaging。\n**R2-W4**: 仅在 LIBERO simulation 上评估，缺乏 real-robot 验证。\n**R2-W5**: OpenVLA 仅评估了 Object suite。\n\n---\n\n## Reviewer 3 的审稿报告（写作/格式/Limitations）\n\n### Must-Fix:\n**R3-N1**: 缺少 Generative AI 使用披露——CoRL 2026 明确要求。\n**R3-N2**: \"VTR\" 与 \"Smart Compress\" 命名不一致——主文用 VTR，附录大量使用 Smart Compress。\n**R3-N3**: Table 2 缺失数据过多（约 20% 条目为 \"--\"）。\n\n### Should-Fix:\n**R3-W1**: LaTeX 渲染错误 `$\\pi_0.5$` 全文 50+ 处。\n**R3-W2**: Limitations section 过于简短（3 句话），遗漏关键局限。\n**R3-W3**: 缺少代码/数据发布计划。\n**R3-W4**: Abstract 信息密度过高（17 个数字/百分比）。\n**R3-W5**: Figure 3 可读性问题。\n\n---\n\n请逐条回应，重点关注你的专长领域（方法严谨性/实验有效性）的交叉点。"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-23T05:52:33.601358+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12782
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-23T05:52:33.652074+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "importance_margin_vla_compress",
  "text": "## 交叉分享：请逐条回应 Reviewer 1 和 Reviewer 3 的审稿意见\n\n请对以下两份审稿报告中的每个 Must-Fix 和 Should-Fix 条目逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 的审稿报告（方法严谨性/实验有效性）\n\n### Must-Fix:\n**R1-N1**: CV diagnostic 的统计基础不足：N=4 闭环模型无法建立可靠的诊断关系。4 个单调排列的数据点的概率 ≤ 1/4! = 1/24。未提供 Spearman rank correlation 及 p-value。\n\n**R1-N2**: 因果叙事超出证据范围：Connector → pruning tolerance 因果推断缺乏控制。模型同时在 backbone、预训练数据、token 数量上不同。正文 Section 5 使用\"primary determinant\"。\n\n**R1-N3**: 缺少关键 pruning baseline：L2 norm 和 random 不构成充分的方法 bracket。Attention-based scoring（VLA-Cache/FastV 采用）和 gradient-based importance 完全缺失。\n\n### Should-Fix:\n**R1-W1**: VTR 贡献被 MLP adapter 控制实验严重削弱（p=0.15）。\n**R1-W2**: VTR 训练条件不公平：batch size 4 vs. 64。\n**R1-W3**: 跨条件使用不同 seed 引入潜在混淆。\n**R1-W4**: Table 2 大量缺失数据限制跨模型比较。\n**R1-W5**: Post-connector pruning 缺乏系统 justification。\n**R1-W6**: CV 选择的理论动机不足——未比较 CV vs. entropy/kurtosis/Gini。\n\n---\n\n## Reviewer 3 的审稿报告（写作/格式/Limitations）\n\n### Must-Fix:\n**R3-N1**: 缺少 Generative AI 使用披露。\n**R3-N2**: \"VTR\" 与 \"Smart Compress\" 命名不一致。\n**R3-N3**: Table 2 缺失数据过多。\n\n### Should-Fix:\n**R3-W1**: LaTeX 渲染错误 `$\\pi_0.5$` 全文 50+ 处。\n**R3-W2**: Limitations section 过于简短（3 句话）。\n**R3-W3**: 缺少代码/数据发布计划。\n**R3-W4**: Abstract 信息密度过高。\n**R3-W5**: Figure 3 可读性问题。\n\n---\n\n请逐条回应，重点关注你的专长领域（新颖性/定位/相关工作）的交叉点。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "importance_margin_vla_compress",
    "text": "## 交叉分享：请逐条回应 Reviewer 1 和 Reviewer 3 的审稿意见\n\n请对以下两份审稿报告中的每个 Must-Fix 和 Should-Fix 条目逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 的审稿报告（方法严谨性/实验有效性）\n\n### Must-Fix:\n**R1-N1**: CV diagnostic 的统计基础不足：N=4 闭环模型无法建立可靠的诊断关系。4 个单调排列的数据点的概率 ≤ 1/4! = 1/24。未提供 Spearman rank correlation 及 p-value。\n\n**R1-N2**: 因果叙事超出证据范围：Connector → pruning tolerance 因果推断缺乏控制。模型同时在 backbone、预训练数据、token 数量上不同。正文 Section 5 使用\"primary determinant\"。\n\n**R1-N3**: 缺少关键 pruning baseline：L2 norm 和 random 不构成充分的方法 bracket。Attention-based scoring（VLA-Cache/FastV 采用）和 gradient-based importance 完全缺失。\n\n### Should-Fix:\n**R1-W1**: VTR 贡献被 MLP adapter 控制实验严重削弱（p=0.15）。\n**R1-W2**: VTR 训练条件不公平：batch size 4 vs. 64。\n**R1-W3**: 跨条件使用不同 seed 引入潜在混淆。\n**R1-W4**: Table 2 大量缺失数据限制跨模型比较。\n**R1-W5**: Post-connector pruning 缺乏系统 justification。\n**R1-W6**: CV 选择的理论动机不足——未比较 CV vs. entropy/kurtosis/Gini。\n\n---\n\n## Reviewer 3 的审稿报告（写作/格式/Limitations）\n\n### Must-Fix:\n**R3-N1**: 缺少 Generative AI 使用披露。\n**R3-N2**: \"VTR\" 与 \"Smart Compress\" 命名不一致。\n**R3-N3**: Table 2 缺失数据过多。\n\n### Should-Fix:\n**R3-W1**: LaTeX 渲染错误 `$\\pi_0.5$` 全文 50+ 处。\n**R3-W2**: Limitations section 过于简短（3 句话）。\n**R3-W3**: 缺少代码/数据发布计划。\n**R3-W4**: Abstract 信息密度过高。\n**R3-W5**: Figure 3 可读性问题。\n\n---\n\n请逐条回应，重点关注你的专长领域（新颖性/定位/相关工作）的交叉点。"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-23T05:52:40.591313+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 6939
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-23T05:52:40.591749+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "3",
  "round_number": "1",
  "project": "importance_margin_vla_compress",
  "text": "## 交叉分享：请逐条回应 Reviewer 1 和 Reviewer 2 的审稿意见\n\n请对以下两份审稿报告中的每个 Must-Fix 和 Should-Fix 条目逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 的审稿报告（方法严谨性/实验有效性）\n\n### Must-Fix:\n**R1-N1**: CV diagnostic 的统计基础不足：N=4 闭环模型无法建立可靠的诊断关系。论文未提供 Spearman rank correlation 及 p-value。\n\n**R1-N2**: 因果叙事超出证据范围：Connector → pruning tolerance 因果推断缺乏控制。Title 和 Section 5 使用\"primary determinant\"措辞过强。\n\n**R1-N3**: 缺少关键 pruning baseline：attention-based scoring 和 gradient-based importance 完全缺失。\n\n### Should-Fix:\n**R1-W1**: VTR 贡献被 MLP adapter 控制实验严重削弱。\n**R1-W2**: VTR 训练条件不公平：batch size 4 vs. 64。\n**R1-W3**: 跨条件使用不同 seed 引入潜在混淆。\n**R1-W4**: Table 2 大量缺失数据。\n**R1-W5**: Post-connector pruning 缺乏系统 justification。\n**R1-W6**: CV 选择的理论动机不足。\n\n---\n\n## Reviewer 2 的审稿报告（新颖性/定位/相关工作）\n\n### Must-Fix:\n**R2-N1**: CV Diagnostic 的 Evidence Base 严重不足——3 个数据点不能建立可靠的 diagnostic tool。\n\n**R2-N2**: 论文 identity 分裂——empirical study / diagnostic tool / method 三者均不够深入。\n\n**R2-N3**: Table 2 数据大量缺失（填充率不足 70%）。\n\n### Should-Fix:\n**R2-W1**: VTR 的 novelty 不足——cross-attention re-encoding 是已知技术。\n**R2-W2**: 与 \"Don't Run with Scissors\" 差异化讨论不足。\n**R2-W3**: Two-axis framework 可能是对已知现象的 re-packaging。\n**R2-W4**: 仅在 LIBERO simulation 上评估。\n**R2-W5**: OpenVLA 仅评估了 Object suite。\n\n---\n\n请逐条回应，重点关注你的专长领域（写作质量/格式/Limitations）的交叉点。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "3",
    "round_number": "1",
    "project": "importance_margin_vla_compress",
    "text": "## 交叉分享：请逐条回应 Reviewer 1 和 Reviewer 2 的审稿意见\n\n请对以下两份审稿报告中的每个 Must-Fix 和 Should-Fix 条目逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 的审稿报告（方法严谨性/实验有效性）\n\n### Must-Fix:\n**R1-N1**: CV diagnostic 的统计基础不足：N=4 闭环模型无法建立可靠的诊断关系。论文未提供 Spearman rank correlation 及 p-value。\n\n**R1-N2**: 因果叙事超出证据范围：Connector → pruning tolerance 因果推断缺乏控制。Title 和 Section 5 使用\"primary determinant\"措辞过强。\n\n**R1-N3**: 缺少关键 pruning baseline：attention-based scoring 和 gradient-based importance 完全缺失。\n\n### Should-Fix:\n**R1-W1**: VTR 贡献被 MLP adapter 控制实验严重削弱。\n**R1-W2**: VTR 训练条件不公平：batch size 4 vs. 64。\n**R1-W3**: 跨条件使用不同 seed 引入潜在混淆。\n**R1-W4**: Table 2 大量缺失数据。\n**R1-W5**: Post-connector pruning 缺乏系统 justification。\n**R1-W6**: CV 选择的理论动机不足。\n\n---\n\n## Reviewer 2 的审稿报告（新颖性/定位/相关工作）\n\n### Must-Fix:\n**R2-N1**: CV Diagnostic 的 Evidence Base 严重不足——3 个数据点不能建立可靠的 diagnostic tool。\n\n**R2-N2**: 论文 identity 分裂——empirical study / diagnostic tool / method 三者均不够深入。\n\n**R2-N3**: Table 2 数据大量缺失（填充率不足 70%）。\n\n### Should-Fix:\n**R2-W1**: VTR 的 novelty 不足——cross-attention re-encoding 是已知技术。\n**R2-W2**: 与 \"Don't Run with Scissors\" 差异化讨论不足。\n**R2-W3**: Two-axis framework 可能是对已知现象的 re-packaging。\n**R2-W4**: 仅在 LIBERO simulation 上评估。\n**R2-W5**: OpenVLA 仅评估了 Object suite。\n\n---\n\n请逐条回应，重点关注你的专长领域（写作质量/格式/Limitations）的交叉点。"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-23T05:52:42.150703+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_3\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1558
}
```

</details>

---


### Assistant

_source line 500 · 2026-05-23T05:52:45.064473+00:00_

交叉分享已发送给全部 3 位 Reviewer。等待交叉回应返回后进入收敛判断（Step 3）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 501 · 2026-05-23T05:52:47.718771+00:00_

[Reviewer 1 审稿结果]:
审稿完成。报告已提交至 Review Director，评分 5/10。核心问题：

1. **N1** CV diagnostic 仅 N=4 闭环模型，统计支撑不足
2. **N2** Connector → pruning tolerance 因果推断缺乏 matched-backbone 控制
3. **N3** 缺少 attention-based pruning baseline，L2 norm + random 不构成充分 bracket

主要优势是 SmolVLA pixel-shuffle 崩溃机制的发现（Section 4.3），经双 checkpoint 验证，解释逻辑清晰。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 502 · 2026-05-23T05:52:52.750854+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 503 · 2026-05-23T05:54:50.417456+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应：逐条回应 R2 和 R3

---

### 回应 Reviewer 2（新颖性/定位/相关工作）

#### Must-Fix

**[AGREE] R2-N1**: CV diagnostic evidence base 不足
同意，且 R2 的量化比我更精确：pruning tolerance 有效数据 4 个，但 method sensitivity 仅 3 个（SmolVLA 两种方法均 0%，无法提供 method gap 信息）。我的 N1 将两个维度合并计数，R2 正确区分了这一点。

**[AGREE] R2-N2**: 论文 identity 分裂
从实验有效性角度同意三个贡献各自验证不完整。但补充：pixel-shuffle 崩溃机制（Section 4.3）是架构层面的演绎论证，不需要大量数据点验证，经双 checkpoint 确认，单独有足够价值——问题在于论文将其定位为 C1 的一个 case 而非独立贡献。

**[AGREE] R2-N3**: Table 2 数据缺失
同意。SmolVLA 的 0%/「--」虽然本身是重要发现，但无法提供 method sensitivity 或 degradation curve 形状信息，使"cross-architecture analysis"的 framing 名不副实。

#### Should-Fix

**[AGREE] R2-W1**: VTR novelty 不足
MLP adapter 控制实验 p=0.15 直接证明 cross-attention 架构无显著优势。论文自己的数据表明 key insight 是 learned re-encoding 而非 VTR 设计，但正文仍以 VTR 为主角叙事——claim 与 evidence 不匹配。

**[REBUT] R2-W2**: 与 "Don't Run with Scissors" 差异化不足
从方法角度看，两者差异较大：本文聚焦 closed-loop robotic control 中 connector 架构对 pruning 的影响（action prediction, SR 崩溃），"Don't Run with Scissors" 主要讨论 VLM 的 token pruning（视觉问答, accuracy 下降）。Evaluation protocol、failure mode、downstream task 性质不同。Section 2 有覆盖，但可以更显式对比实验设置差异。

**[AGREE] R2-W3**: Two-axis framework 可能是 re-packaging
部分同意。Connector coupling 维度是已知架构差异的重新命名。但 task complexity × connector coupling 的交互效应（Section 4.2, Figure 2）是有实验支撑的新观察，只是仅在 LIBERO 4 个 suite 上验证，泛化性存疑。

**[AGREE] R2-W4**: 仅 LIBERO simulation 评估
同意。LIBERO 观察空间简单（固定视角、有限物体种类），真实场景中 vision token 冗余度可能完全不同。

**[AGREE] R2-W5**: OpenVLA 仅评估 Object suite
这是我原始审稿遗漏的重要缺陷。OpenVLA 在 Spatial/Goal/Long 上缺乏闭环数据，削弱了 two-axis framework 在 MLP connector 上的验证。

---

### 回应 Reviewer 3（写作/格式/Limitations）

#### Must-Fix

**[AGREE] R3-N1**: 缺少 Generative AI 使用披露
如果 CoRL 2026 明确要求此披露，这是合规性问题。技术上不影响评判，但可能导致 desk reject。

**[AGREE] R3-N2**: VTR vs. Smart Compress 命名不一致
主文 Section 4.5 用"VTR"，附录 Table 15-18 全部用"Smart Compress"，且 Smart Compress 包含 VTR + 额外 pruning 策略。这不仅是命名问题，更是概念混淆——影响对 VTR 实验有效性的验证。

**[REBUT] R3-N3**: Table 2 缺失数据过多
认为应为 Should-Fix 级别，非 Must-Fix。SmolVLA 的 0% 本身是论文最重要发现之一（Section 4.3 pixel-shuffle 崩溃），不是"缺失"数据而是"极端"数据。真正的问题在于缺乏更细粒度 k 值（k=0.98/0.99）来定位崩溃阈值，以及 X-VLA/OpenVLA 在低 k 条件下的缺失。但不应是一票否决级别。

#### Should-Fix

**[AGREE] R3-W1**: LaTeX 渲染错误 `$\pi_0.5$`，50+ 处。反映稿件准备粗糙度。

**[AGREE] R3-W2**: Limitations section 过于简短。遗漏关键方法论局限：N=4 闭环模型不足（我的 N1）、无 matched-backbone 控制（我的 N2）、VTR 训练条件不公平（我的 W2）、OpenVLA 仅 Object suite（R2-W5）。

**[AGREE] R3-W3**: 缺少代码/数据发布计划。多个结论依赖具体实现细节（position re-indexing、evaluation seed、checkpoint 版本），无代码公开承诺影响可复现性。

**[AGREE] R3-W4**: Abstract 信息密度过高。建议保留最具冲击力的 3-4 个数字，其余移至 Section 4。

**[REBUT] R3-W5**: Figure 3 可读性问题。Figure 3 的 bar chart 在我阅读中可读性尚可——数值标签直接标在 bar 上方，虚线 15× 标注有效传达关键信息。如果 R3 指具体渲染问题需更具体描述。

---

### 三位 Reviewer 共识汇总

以下问题获得至少 2/3 reviewers 一致认定：
1. **CV diagnostic 数据不足**：R1-N1 + R2-N1（三人共识）
2. **Table 2 数据缺失**：R1-W4 + R2-N3 + R3-N3（三人共识，严重程度有分歧）
3. **VTR 贡献被 MLP adapter 削弱**：R1-W1 + R2-W1（两人共识）
4. **因果叙事过度**：R1-N2（R2 的 identity 分裂间接支持）
5. **Limitations 过于简短**：R1 implied + R3-W2（两人共识）
6. **仅 LIBERO 评估**：R2-W4（两人关注）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 504 · 2026-05-23T05:54:57.119900+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 45

## Round 45

10 recorded events


### User

_source line 505 · 2026-05-23T05:54:58.272979+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：逐条回应 Reviewer 1 和 Reviewer 3

---

## 回应 Reviewer 1（方法严谨性/实验有效性）

### Must-Fix

**[AGREE] R1-N1: CV diagnostic 的统计基础不足**

完全同意。这与我的 R2-N1 一致。N=4 闭环模型（实际有效数据点仅 3 个，SmolVLA 全 0% 无 method sensitivity 信息）不足以建立可靠 diagnostic。R1 提出的 1/4!=1/24 概率分析进一步量化了这一问题——4 个单调排列的数据点在随机排列下出现概率约 4.2%，即使算作"显著"也处于边缘。补充一点：即使增加 Spearman rank correlation，N=4 时的 p-value 在统计意义上也极为有限（Spearman N=4 的最小可能 p-value 约 0.083，无法达到 0.05 显著性水平）。这意味着仅靠当前 4 个模型，CV diagnostic 在统计上**原则上不可能**被严格验证。必须增加模型数量至 6+ 才有意义。

**[AGREE] R1-N2: 因果叙事超出证据范围**

同意，且与我的审查侧重（论文定位）直接相关。论文在 Conclusion（Section 5）使用 "connector coupling is the primary determinant of pruning robustness" 这样的因果语言，但实验设计无法支撑因果推断。6 个模型在 backbone 架构（Qwen2-VL 0.5B vs. PaliGemma 3B vs. LLaMA 7B）、参数量（450M-7B，16× 范围）、预训练数据、vision encoder（SigLIP vs. DINOv2 vs. SigLIP-SO400M）、token 数量（50-768，15× 范围）上全部不同。Connector 是其中一个变量，但 confounders 使得无法分离其因果效应。

从定位角度补充：如果论文降级为 "observational study"（观察到 connector 与 pruning robustness 的 correlation），而非 "causal analysis"，其 contribution 就更加诚实但也更弱——这进一步加剧了我在 R2-N2 中指出的 identity 问题。

**[AGREE] R1-N3: 缺少关键 pruning baseline**

同意，从 novelty/positioning 角度补充。论文将自己定位为 "cross-architecture analysis of token compressibility"，但只用了两种最简单的 pruning 策略（L2 norm 和 random）。这相当于用最粗糙的工具来做精细诊断。具体而言：

- **Attention-based scoring**（FastV、VLA-Cache 采用）：论文在 Related Work 中引用了 FastV 和 VLA-Cache（Section 2），但自己不用 attention-based scoring，这在 related work positioning 上造成矛盾——既认可这些方法的重要性又不将其纳入 baseline。
- **Gradient-based importance**：完全缺失。对于声称研究 "which tokens matter" 的论文，不测试 gradient-based 方法是重大遗漏。
- 从 novelty 角度看，如果 attention-based scoring 在 entangling connectors 上也同样失败，这将大幅加强论文的核心 narrative（"问题在 connector 而非 scoring function"）。缺少这一 baseline 反而削弱了论文的说服力。

### Should-Fix

**[AGREE] R1-W1: VTR 贡献被 MLP adapter 控制实验削弱**

同意，这与我的 R2-W1 完全一致。Section 4.5 报告 MLP adapter 63.4% vs VTR 60.1%（p=0.15），不仅无法拒绝零假设，MLP adapter 的点估计还更高。这说明 VTR 的 contribution 不是 cross-attention 机制本身，而是 "re-encoding 这一类操作对 pixel-shuffle collapse 有效" 这一 finding。从 novelty 角度看，这实际上是一个更有趣但更弱的 contribution——它说明 pixel-shuffle 的 catastrophic failure 可被几乎任何参数量匹配的 re-encoding 模块修复。

**[REBUT] R1-W2: VTR 训练条件不公平（batch size 4 vs. 64）**

部分不同意。R1 指出 VTR 使用 batch size 4 而基线 SmolVLA fine-tuning 使用 batch size 64，认为这构成不公平比较。但这里需要区分两个问题：(1) VTR 的比较对象不是 SmolVLA baseline（59.2%），而是 pruning 后的 SmolVLA（0.0%）。VTR 从 0.0% 恢复到 60.1%，无论 batch size 如何，这个 recovery 都是实质性的。(2) VTR 与 MLP adapter 的消融比较中，二者使用相同训练条件（Section 4.5 "parameter-matched"），这个内部比较是公平的。

不过 R1 的关切仍有价值：如果 VTR 在 batch size 64 下训练，其性能可能更高，这会改变与 MLP adapter 的比较结论。建议作者在附录中补充 batch size sensitivity 分析。

**[AGREE] R1-W3: 跨条件使用不同 seed 引入混淆**

同意。这与我的 Minor issue M2 一致。Table 2 的主实验为单 seed（500 episodes），而 VTR 用了 3 seeds。跨条件的 seed 不一致使得跨模型比较的精确数值（如 "20× amplification"）的可靠性存疑。特别是 π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0% 这一异常值（我在 R2 Q1 中也提出了质疑），可能就是单 seed 波动。

**[AGREE] R1-W4: Table 2 大量缺失数据**

完全同意，这与我的 R2-N3 一致。Table 2 的数据缺失严重影响 cross-architecture claim 的可信度。不再重复。

**[AGREE] R1-W5: Post-connector pruning 缺乏系统 justification**

同意，从 positioning 角度补充一个重要观点。论文选择在 post-connector 位置 pruning，但 concurrent work（VLA-Cache、EfficientVLA）在 KV-cache 或 pre-connector 位置操作。论文没有解释为什么 post-connector pruning 是 the right level of abstraction。

从 novelty 角度看：如果 pre-connector pruning 和 post-connector pruning 的行为不同（例如 pre-connector pruning 对 pixel-shuffle 可能不那么 catastrophic），那么论文的核心发现（"pixel-shuffle = catastrophic collapse"）就只适用于 post-connector pruning 这一特定设定，generality 大打折扣。论文应至少讨论这一 limitation。

**[REBUT] R1-W6: CV 选择的理论动机不足——未比较 CV vs. entropy/kurtosis/Gini**

部分不同意。R1 要求比较 CV 与 entropy/kurtosis/Gini 等替代指标。但鉴于 N=4（实际 N=3）的数据量，任何指标比较都缺乏统计意义——在 3 个数据点上比较不同 metric 的 correlation 是 overfitting，不是 validation。我认为问题不在于"该选哪个 metric"而在于"sample size 太小以至于任何 metric 都无法被验证"。这回到 R1-N1/R2-N1 的核心问题。

如果作者增加到 6+ 模型，那么 R1-W6 的比较就变得有意义且必要。在当前 N=3 下，补充其他 metric 的比较只是增加了复杂度而非证据。

---

## 回应 Reviewer 3（写作/格式/Limitations）

### Must-Fix

**[AGREE] R3-N1: 缺少 Generative AI 使用披露**

同意。CoRL 2026 如果遵循 NeurIPS/ICML 的趋势，很可能要求 AI usage disclosure。这是一个 checkbox 级别的合规问题，容易修复但不应遗漏。从 reviewer 角度，缺少 disclosure 不影响技术评价，但在审稿流程中可能被标记为 non-compliance。

**[AGREE] R3-N2: "VTR" 与 "Smart Compress" 命名不一致**

同意。我在阅读论文时也注意到附录中出现 "Smart Compress" 和 "Smart Compressor"（Appendix E.12, E.13, G, H），但正文只使用 "VTR"。这造成混淆——读者无法确定这是同一方法还是不同方法。从 positioning 角度看，统一命名对论文的 contribution 清晰度至关重要：如果 "Smart Compress" 是 VTR 的扩展（加入了 pruning 策略选择逻辑），那是一个额外 contribution 但未在正文中 claim；如果只是别名，应统一为 "VTR"。

**[AGREE] R3-N3: Table 2 缺失数据过多**

同意，与 R1-W4 和 R2-N3 一致。三位 reviewer 均提出同一问题，说明这是 consensus issue。

### Should-Fix

**[AGREE] R3-W1: `$\pi_0.5$` LaTeX 渲染错误**

同意。这与我的 Minor M4 一致。正确写法为 `$\pi_{0.5}$`。全文 50+ 处出现说明是 systematic error，但修复简单。

**[AGREE] R3-W2: Limitations section 过于简短**

同意。Section 4.5 末尾的 Limitations 段落确实只有 3 句话（约 60 words）。对于一篇 empirical 论文，应该更充分地讨论以下限制：(a) simulation-only，无 real-robot 验证（我在 R2-W4 中也提出）；(b) confounders 使因果推断不可能（R1-N2）；(c) CV diagnostic 的 N=3 evidence base（R1-N1/R2-N1）；(d) post-connector pruning 作为唯一 pruning point 的局限性（R1-W5）。当前的 Limitations 仅提及 (a) 和 (b)，遗漏了对论文核心 contribution 的 self-critique。

但我在 R2 评分中已给 Limitations 维度 4/5，因为 Appendix A 包含了更详细的 extended discussion，补充了正文中的不足。问题是 reviewer 和读者可能只看正文而不翻附录。

**[AGREE] R3-W3: 缺少代码/数据发布计划**

同意。可复现性对 empirical 论文至关重要。CoRL 虽然没有 mandatory code release 要求，但在 anonymous review 期间声明"camera-ready 后发布代码和 checkpoint"是标准做法。特别是本文包含 VTR 训练和 SmolVLA fine-tuning 等需要精确复现的实验。

**[REBUT] R3-W4: Abstract 信息密度过高**

部分不同意。R3 认为 abstract 塞入了太多具体数字（"5%"、"0.0%"、"98.2%"、"20×"、"22M"、"60%"、"75%"等），建议精简。但从 novelty/positioning 角度看，这些具体数字恰恰是论文最有冲击力的卖点——"移除 5% token 即从 59.2% 崩溃到 0.0%" 比 "少量 pruning 导致 catastrophic failure" 在传达效果上强得多。对于一篇 empirical 论文，abstract 中的具体量化是优势而非劣势。

我的建议是保持核心数字（5% → 0.0% collapse, 20× amplification, VTR recovery to 60%），但删减次要数字（22M parameters, 三种 connector family 的详细枚举），以在信息密度和可读性之间取得平衡。

**[AGREE] R3-W5: Figure 3 可读性问题**

同意。Figure 3（page 8, "Method sensitivity at k=0.95"）使用柱状图显示 method gap，但 π₀.5 的两个 bar（Object 28.8pp 和 Spatial 21.4pp）与 X-VLA/OpenVLA 的 bar（0.2-1.4pp）尺度差异约 20×，导致后者在视觉上几乎不可见。从 positioning 角度看，这张图应该是论文的 key selling point（CV 低 → method sensitivity 高），但当前可视化反而让 X-VLA 和 OpenVLA 的数据难以辨认。建议使用 log scale y-axis 或 broken axis。

---

## 三位 Reviewer 的共识总结

以下问题被 2-3 位 reviewer 共同指出，应视为 high-confidence 共识：

| 问题 | R1 | R2 | R3 | 共识强度 |
|------|-----|-----|-----|---------|
| CV diagnostic evidence 不足 (N=3/4) | N1 | N1 | — | 2/3 |
| Table 2 数据大量缺失 | W4 | N3 | N3 | 3/3 |
| VTR 被 MLP adapter 平替 | W1 | W1 | — | 2/3 |
| `π_0.5` 渲染错误 | — | M4 | W1 | 2/3 |
| Limitations 讨论不足 | — | — | W2 | 1/3（但 R1-N2 和 R2-W4 间接触及）|
| 缺少代码发布计划 | — | — | W3 | 1/3 |

最强共识（3/3）：**Table 2 数据缺失**——这是所有 reviewer 的底线问题，必须在 revision 中完全解决。


---

[Reviewer 3 审稿意见]:
## Reviewer 3 交叉回应：逐条回应 R1 和 R2 意见

---

## 回应 Reviewer 1（方法严谨性/实验有效性）

### Must-Fix

**[AGREE] R1-N1: CV diagnostic 统计基础不足**
从写作角度完全同意。论文对 CV 的定位存在表述膨胀：Section 3.3 将 CV 称为 "single-pass diagnostic that correlates with both pruning tolerance and method sensitivity"（method.tex line 61），Abstract 中重复此 claim，Introduction contributions 第二条也将其列为核心贡献。但支撑这一 claim 的闭环数据仅有 3 个可比较模型（π₀.₅, X-VLA, OpenVLA；SmolVLA 全部 0% 无法参与 method sensitivity 比较）。从叙事角度，"correlates" 这个词暗示统计关系，但论文未报告任何相关系数或 p-value。这不是统计方法的问题——是写作中 claim 的强度与证据的强度不匹配。建议：要么降级措辞为 "is consistent with" / "tracks"，要么补充更多模型数据点以支撑 "correlates" 的 claim。

**[AGREE] R1-N2: 因果叙事超出证据范围**
这与我在叙事一致性检查中标记的问题一致。Conclusion（conclusion.tex line 4）写道 "connector coupling is the primary determinant of pruning robustness"，但论文自己在 Appendix I（appendix.tex line 681）承认 "preventing clean isolation of the connector effect from backbone differences"。主文 Title 中 "Vision Connectors and VLA Token Compressibility" 也隐含因果方向。更严重的是，主文 Limitations 段（experiments.tex lines 105-106）仅用一句话 "the connector effect cannot be causally isolated" 带过，而 Conclusion 紧接其后的 Section 5 却使用了 "primary determinant" 这一因果性极强的措辞。从写作一致性角度，Conclusion 的 claim 强度与 Limitations 的 caveat 直接矛盾。建议：将 "primary determinant" 改为 "primary correlate" 或 "strongest observed factor"，并在 Conclusion 中加入一句 confounder caveat。

**[AGREE with nuance] R1-N3: 缺少关键 pruning baseline**
从 Limitations 覆盖角度同意。当前 Limitations 段（主文）完全未提及仅使用了 L2 norm 和 random 两种 pruning 方法。论文的 Related Work 列举了 attention-based（FastV, VLA-IAP）和 gradient-based（VLA-Pruner）方法（related_work.tex lines 7-8），但实验中未与这些方法对比。从写作角度，Related Work 提到的方法未在 Experiments 中出现，构成了叙事缺口。不过，论文的核心 claim 是关于 connector architecture 对 pruning sensitivity 的影响，而非评比 pruning 方法，因此缺少这些 baseline 的严重性取决于论文的最终定位。我建议至少在 Limitations 中显式承认这一局限。

### Should-Fix

**[AGREE] R1-W1: VTR 贡献被 MLP adapter 削弱**
论文的处理是诚实的——experiments.tex line 103 报告 MLP adapter 63.4±2.6% vs. VTR 60.1±1.3%，p=0.15。但从写作 framing 角度，Introduction 将 VTR 列为第三条独立 contribution（introduction.tex line 23: "Vision Token Re-encoder (VTR), which recovers a pixel-shuffle VLA from 0.0% to over 60%"），没有提及 MLP adapter 同样有效。这种 framing 让读者以为 cross-attention 是关键机制，但实验数据表明 any learned re-encoding 都能 work。建议：修改 contribution 表述，将 contribution 聚焦在 "learned re-encoding recovers pixel-shuffle VLAs" 而非 VTR 本身。

**[AGREE] R1-W2: VTR 训练条件不公平**
从写作透明度角度同意。batch size 差异（4 vs 64）导致 LoRA baseline 仅 44.8% vs. 官方 59.2%，这一关键信息仅出现在 Appendix G 的表格脚注中（appendix.tex line 530: "Our batch size 4 on a single GPU contributes to the lower baseline SR (44.8% vs. 87.3%)"）。注意这里甚至提到官方 LIBERO 全套成绩是 87.3%——与主文报告的 59.2% 之间的巨大差距仅在脚注中披露。建议将此信息提升至主文 Limitations 或 Section 4.5 中。

**[AGREE] R1-W3: 跨条件不同 seed**
Appendix I（appendix.tex lines 685-686）披露了 OpenVLA L2/random 使用不同 seed，并提供了 same-seed 控制。从写作角度，这种控制实验是好的，但主文 Table 2 没有注明哪些结果来自不同 seed——读者在不读附录的情况下无法知道 L2 vs Random 的比较可能受 seed 混淆。Table 2 caption 应增加 seed 信息。

**[AGREE] R1-W4: Table 2 缺失数据**
与我的 R3-N3 完全一致。三位 reviewer 均独立指出此问题，说明这是共识性缺陷。

**[AGREE with nuance] R1-W5: Post-connector pruning 缺乏 justification**
从写作结构角度，Section 3.2（Pruning Protocol）直接描述了 post-connector pruning 的操作，但未解释为什么选择在 connector 之后而非之前进行 pruning。这是一个叙事缺口：论文的核心论点是 connector 架构决定 pruning 鲁棒性，但如果在 connector 之前 pruning，connector 的影响可能完全不同。至少需要一段 justification 解释 post-connector 是更贴近实际部署场景的选择。不过我认为这是 should-fix 而非 must-fix——post-connector pruning 在实践中是合理的默认选择。

**[AGREE] R1-W6: CV 选择的理论动机不足**
Section 3.3 引入 CV 时（method.tex lines 51-61）的 motivation 基本是操作性的（"We quantify the heterogeneity..."），没有解释为什么选择 CV 而非其他度量（如 entropy、kurtosis、Gini coefficient）。从写作角度，一个被定位为核心 contribution 的 diagnostic metric 应该有更强的动机论证。至少需要一段讨论 CV 相对于替代指标的优势。

---

## 回应 Reviewer 2（新颖性/定位/相关工作）

### Must-Fix

**[AGREE] R2-N1: CV Diagnostic evidence base 不足**
与 R1-N1 一致，从写作角度补充一个观察：论文在不同位置对 CV 的描述强度不一致。Abstract 说 "serves as a single-pass diagnostic"（abstract.tex line 2），Section 3.3 标题直接写 "Compressibility Diagnostic: Importance CV"（method.tex line 51），但 Appendix H（appendix.tex line 639）标题是 "CV as Diagnostic Metric: Extended Analysis"——在 extended analysis 中才提供更细致的讨论。这意味着 CV 作为 diagnostic 的核心 claim 在主文中缺乏充分论证，关键分析被放到了 reviewer 不一定会读的附录中。

**[AGREE] R2-N2: 论文 identity 分裂**
从写作结构角度，这是一个合理的批评。Introduction 的三条 contributions（introduction.tex lines 19-24）分别对应：(1) empirical study（two-axis analysis across 6 architectures），(2) diagnostic tool（CV metric），(3) method（VTR）。这三个方向各自的深度不足以独立成文：empirical study 缺数据（Table 2 的 "--"），diagnostic tool 缺统计验证（N=3-4），method 被 MLP adapter 控制实验削弱。论文的叙事试图将三者统一为 "understand → diagnose → fix" 的递进关系，这个叙事弧线是合理的，但每一步的执行力度都略显不足。

我的建议（从写作角度）：论文应该明确主次。如果定位为 empirical study，则 CV 和 VTR 应降级为 secondary findings；如果定位为 diagnostic tool paper，需要更多模型验证 CV 的预测力。当前的 equal-weight 三 contribution 结构分散了论文的力量。

**[AGREE] R2-N3: Table 2 数据缺失**
三位 reviewer 共识。不再重复。

### Should-Fix

**[AGREE with nuance] R2-W1: VTR novelty 不足**
从写作角度，Related Work（related_work.tex line 11）提到了 BLIP-2 的 cross-attention queries，但未讨论 VTR 与 BLIP-2 Q-Former 的区别。如果 VTR 本质上是 Q-Former 应用于 VLA token compression 的场景，论文应该显式 acknowledge 这一联系并说明 contribution 在于 application context 而非 architecture novelty。当前写作给读者的印象是 VTR 是一个全新的模块设计，但实际上 cross-attention pooling 是一个成熟技术。

**[AGREE] R2-W2: 与 "Don't Run with Scissors" 差异化不足**
Related Work 中未出现对这篇论文的引用或讨论。如果 "Don't Run with Scissors" 确实研究了类似问题（VLA/VLM 中 token pruning 的 architecture-dependent 效果），那么缺少对比讨论是 Related Work 的重要遗漏。从写作完整性角度，应增加一段讨论说明本文与其的差异（例如 connector-specific analysis、task complexity axis、CV diagnostic 等本文的独特贡献）。

**[AGREE] R2-W3: Two-axis framework 可能是 re-packaging**
从写作角度，"connector coupling × task complexity" 的 two-axis framing 在概念层面是直观的——独立处理的 token 比纠缠的 token 更容易 prune，复杂任务比简单任务更 sensitive。论文需要更清晰地论证 two-axis 的新颖性在于 (a) 首次在 VLA 上系统验证了这一交互效应，以及 (b) 量化了 20× amplification 这类具体数字。当前写作在 Introduction 中将 two-axis framework 隐含为概念性贡献，但实际贡献更多是实证性的。

**[AGREE] R2-W4: 仅 LIBERO simulation**
与我的 R3-W2 一致。补充一点：CoRL 2026 Call for Papers 明确写 "Authors should prioritize real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots"。论文未提供任何 sim-to-real transferability 的论证——Conclusion（conclusion.tex line 6）仅将 "real-robot validation" 列为 future work，没有讨论 LIBERO 结论是否可能 transfer 到真实机器人。从 CoRL venue 匹配度角度，这是一个写作和定位上的明显缺陷。

**[AGREE] R2-W5: OpenVLA 仅评估 Object suite**
与 R3-N3 一致。从写作角度补充：论文 Abstract 声称 "Evaluation spans six VLA architectures... three connector families, and four LIBERO task suites"（abstract.tex line 2），但 OpenVLA（7B，论文中最大的模型）仅有 Object 一个 suite 的数据。Abstract 的表述让读者预期所有模型都覆盖了四个 suite，实际情况远非如此。这构成了 abstract 与正文之间的叙事落差。

---

## 三位 Reviewer 的共识汇总

| 问题 | R1 | R2 | R3 | 共识强度 |
|------|----|----|----|---------| 
| Table 2 数据大量缺失 | W4 | N3 | N3 | ⭐⭐⭐ 全员一致，两人列为 Must-Fix |
| CV diagnostic 证据不足（N=3-4） | N1 | N1 | AGREE | ⭐⭐⭐ 全员一致 |
| 因果 claim 过强 | N2 | — | 叙事不一致 | ⭐⭐ R1+R3 |
| 仅 LIBERO simulation | — | W4 | W2 | ⭐⭐ R2+R3 |
| VTR 贡献被 MLP adapter 削弱 | W1 | W1 | AGREE | ⭐⭐⭐ 全员一致 |
| 论文定位/identity 问题 | — | N2 | AGREE | ⭐⭐ R2+R3 |
| Generative AI 披露缺失 | — | — | N1 | ⭐ 仅 R3（格式合规专属） |
| VTR/Smart Compress 命名不一致 | — | — | N2 | ⭐ 仅 R3（写作专属） |

从写作和格式角度，我认为以下问题应列为 rebuttal/revision 的最高优先级：
1. **Table 2 补全**（全员共识）
2. **CV claim 降级措辞**（全员共识）
3. **Conclusion 因果表述修正**（R1+R3）
4. **VTR/Smart Compress 命名统一**（R3）
5. **Generative AI 披露**（CoRL 合规硬要求）
6. **Limitations 扩展**（覆盖 sim-only、单 benchmark、pruning 方法有限等全员关切）

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

核心共识：三位 Reviewer 在 CV diagnostic 数据不足（N=3-4）和 Table 2 缺失数据上达成一致。我对 R2 的 7 条中同意 6 条、反驳 1 条（"Don't Run with Scissors" 差异化），对 R3 的 8 条中同意 6 条、反驳 2 条（Table 2 缺失应降为 Should-Fix；Figure 3 可读性尚可）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-23T05:55:24.372092+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-23T05:55:24.372604+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T05:43:05.900209+00:00\", \"completed_at\": \"2026-05-23T05:46:54.306572+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 2\", \"message\": \"Figure 1 子面板内 axis label 和 legend 字号偏小（估计 ~6-7pt），接近可读性下限。特别是左侧 bar chart 的 y 轴标签和散点图 legend 文字，打印后可能低于 8pt 最低建议\"}, {\"severity\": \"warning\", \"dimension\": \"pages 23-25\", \"message\": \"附录连续 3 页纯文本（无 figure/table/equation），缺乏视觉锚点。审稿人快速翻阅时易跳过这些重要分析内容\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"正文中唯一纯文本整页，讨论四个模型的逐一结果（π0.5 / X-VLA / OpenVLA / SmolVLA）。内容密度高但无视觉节奏中断；如能将关键 per-model 数字提炼为 inline summary table 或 compact figure 可改善\"}, {\"severity\": \"info\", \"dimension\": \"page 27\", \"message\": \"末页内容约 50%，下半部空白。可考虑将 Section U（Inference Cost-Benefit）内容上移或补充一个 summary figure 填充空间\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 最优结果已加粗，格式正确。但未见次优下划线或 ↑/↓ 方向标记——对审稿人快速解读多列数值有帮助\"}, {\"severity\": \"info\", \"dimension\": \"page 16\", \"message\": \"Figure 5（token importance spatial distribution）两个子图并排，axis label 字号偏小。打印时 column index 标注可能难读\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 legend 含 CV 值（如 \\\"CV=0.055\\\"），信息量好但字号略小于正文 70%\"}, {\"severity\": \"info\", \"dimension\": \"pages 12-15\", \"message\": \"附录 per-task breakdown 连续 4 页表格（Tables 3-10），表格密度高但每个表 caption 清晰自包含，审稿人可选择性查阅\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 使用 booktabs 风格，有脚注，格式专业。OpenVLA 行的 \\\"Flash-attn unfold\\\" 脚注标记清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3 bar chart 简洁有效，dashed reference line 帮助阅读。Caption 自包含\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-23T05:55:24.372924+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-23T05:55:24.423350+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-23T05:58:22.901782+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "issues_yaml": "\n# ===== Round 4-5 Issues (all resolved) =====\n\n- id: \"R4-C1\"\n  summary: \"Causal claim under-identified — connector vs backbone/encoder/action confound\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"determines needs downgrade to associated with\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — full-text causal language downgrade confirmed. No residual 'determines' found.\"}\n  action_items:\n    - {round: 4, action: \"Full-text causal language downgrade (determines→associated, controlled→closest available)\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Round 5 verified: determines→strongly associated with, predicts→correlates, falsifies→demonstrates. Appendix N confound analysis added. Both reviewers confirm thorough and consistent.\"\n  resolution_round: 5\n\n- id: \"R4-C2\"\n  summary: \"SmolVLA baseline 44.8% vs official — cliff and VTR on undertrained checkpoint\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Official checkpoint full pruning sweep is minimum requirement\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — official checkpoint (57.2% baseline) multi-k verification complete. Dual evaluation protocol in Appendix Table 3.\"}\n  action_items:\n    - {round: 4, action: \"SmolVLA official checkpoint pruning sweep (10 configs)\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Write official results into paper\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Official HF checkpoint (57.2% baseline) shows 0% at k=0.95/0.9/0.5. Dual protocol (59.2%/57.2%) both confirm cliff. VTR M=32 recovers to 60.1±1.3%.\"\n  resolution_round: 5\n\n- id: \"R4-C3\"\n  summary: \"CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"3 data points = 3 connector clusters, CV adds no predictive power beyond label\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — CV reframed as correlational diagnostic. Section 4.6 title changed. Limitations explicit about N=3, 2 k values.\"}\n  action_items:\n    - {round: 4, action: \"Reframe CV as correlational diagnostic, add X-VLA within-family variance argument\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"CV reframed as 'diagnostic metric that correlates with' (not 'predictor'). Contribution C2 updated. Section 5 Limitations: 'the CV correlation spans three models and two retention ratios'.\"\n  resolution_round: 5\n\n- id: \"R4-C4\"\n  summary: \"π0 offline-only used in core taxonomy argument\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Internal consistency: paper argues offline unreliable but uses π0 offline for taxonomy\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Table 1 footnote, Introduction caveat, 4-in-closed-loop framing all confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Table 1 π0 offline-only label, caveat on π0-OpenVLA 63pp gap, CogACT literature label\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Table 1: †offline metrics only. Introduction: 'evaluating four in closed-loop and analyzing three via offline metrics or literature'. π0-OpenVLA comparison has causal interpretation caveat.\"\n  resolution_round: 5\n\n- id: \"R4-S1\"\n  summary: \"X-VLA linear projection label misleading (has 12-layer BART encoder)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Table 1 label should reflect BART encoder\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Linear + BART (12L)‡ confirmed in Table 1.\"}\n  action_items:\n    - {round: 4, action: \"Table 1 connector column update + continuous spectrum discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Table 1: Linear + BART (12L)‡. Footnote explains effective pipeline.\"\n  resolution_round: 5\n\n- id: \"R4-S2\"\n  summary: \"OpenVLA L2 vs random cross-seed, k=0.5 same-seed missing\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2\", note: \"CV scaling law crossover point based on cross-seed comparison\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Footnote 5: same-seed k=0.5: 35.8% random vs 39.2% L2 (gap 3.4pp).\"}\n  action_items:\n    - {round: 4, action: \"OpenVLA random k=0.5 seed42 completed\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Three k values (0.3, 0.5, 0.7) same-seed verified. k=0.5 gap = 3.4pp.\"\n  resolution_round: 5\n\n- id: \"R4-S3\"\n  summary: \"VTR novelty limited — Perceiver/Q-Former VLA application\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 agree\", note: \"Contribution is diagnostic (why re-encoding works), not method\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — diagnostic protocol framing confirmed throughout.\"}\n  action_items:\n    - {round: 4, action: \"Reframe VTR as diagnostic contribution\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"VTR framed as diagnostic tool.\"\n  resolution_round: 5\n\n- id: \"R4-S4\"\n  summary: \"VTR p=0.15 insufficient for re-encoding is operative mechanism claim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 agree\", note: \"MLP adapter SR higher, claim should be about re-encoding in general\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 'comparable recovery (p=0.15)' confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Soften claim to both architectures achieve comparable recovery\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"p=0.15 reported as 'comparable'. MLP adapter architecture details in Appendix F.3.\"\n  resolution_round: 5\n\n- id: \"R4-S5\"\n  summary: \"Diagnose-then-Compress framework overpackaged\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 agree\", note: \"Single-metric lookup table, not a framework\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — all 'framework' replaced with 'diagnostic protocol'.\"}\n  action_items:\n    - {round: 4, action: \"Replace framework with diagnostic protocol globally\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Global replacement confirmed.\"\n  resolution_round: 5\n\n- id: \"R4-S6\"\n  summary: \"Paper ~13 pages vs CoRL 8-page limit\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Section 5 Analysis ~3 pages is main excess\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 8 pages main text confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Major restructure: Analysis→Appendix, target 8 pages\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Pages 1-8 main text. CoRL compliant.\"\n  resolution_round: 5\n\n- id: \"R4-S7\"\n  summary: \"Falsifies immune assumption — straw man\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 partial agree\", note: \"Soften to demonstrates offline tolerance does not generalize\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — no 'falsifies' in paper.\"}\n  action_items:\n    - {round: 4, action: \"Replace falsifies with demonstrates offline tolerance caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"All 'falsifies' removed.\"\n  resolution_round: 5\n\n- id: \"R4-S8\"\n  summary: \"M=96 dip vs flat M-curve narrative\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1 warning, R2 partial rebut\", note: \"Change flat to relatively stable\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 'relatively stable' confirmed.\"}\n  action_items:\n    - {round: 4, action: \"flat→relatively stable, add M=96 dip discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"All 'flat' replaced. Appendix D: M=96 dip explained.\"\n  resolution_round: 5\n\n- id: \"R4-M1\"\n  summary: \"Related Work citation count insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer assessment\", note: \"Need 15-20 additional citations\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — ~46 citations.\"}\n  action_items:\n    - {round: 4, action: \"Expand Related Work with 15+ citations\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"30+ citations across 4 categories.\"\n  resolution_round: 5\n\n- id: \"R4-M3\"\n  summary: \"VTR vs official baseline statistical significance p=0.72\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer calculation\", note: \"Remove any claim VTR matches official\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — framed as recovery from 0%.\"}\n  action_items:\n    - {round: 4, action: \"Fix VTR vs official framing\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Primary contribution: recovering from 0% where deletion fails.\"\n  resolution_round: 5\n\n- id: \"R4-M4\"\n  summary: \"D141 token position visualization not written into paper\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer assessment\", note: \"High ROI — spatial clustering evidence\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Appendix Token Position Analysis with DBSCAN clustering.\"}\n  action_items:\n    - {round: 4, action: \"Write D141 visualization into appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix with DBSCAN clustering at k=0.7/0.5/0.3.\"\n  resolution_round: 5\n\n- id: \"R5-V1\"\n  summary: \"Figure 4 placeholder on page 17 — not replaced with actual token importance heatmap\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"Visual Check Agent\", note: \"Displays '[Placeholder: token importance heatmap]' gray text box.\"}\n  action_items:\n    - {round: 5, action: \"Replace Figure 4 placeholder with actual token importance heatmap\", assigned_to: \"director+agent\", status: \"done\"}\n  resolution: \"Real dual-panel heatmap generated. Reviewer visual check confirmed.\"\n  resolution_round: 5\n\n- id: \"R5-W1\"\n  summary: \"π₀.5 V-shape non-monotonic recovery unexplained by hypergeometric model\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"Hypergeometric model predicts monotonic collapse but data shows 72pp recovery at k≤0.7.\"}\n  action_items:\n    - {round: 5, action: \"§4.7: added model applicability boundary sentence\", assigned_to: \"director\", status: \"done\"}\n    - {round: 5, action: \"Appendix: added single hypothesis (computation regime shift) + 'remains untested'\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Results.tex §4.7: model boundary statement added. Appendix C.8: V-shape hypothesis with 'remains untested' caveat.\"\n  resolution_round: 5\n\n- id: \"R5-W2\"\n  summary: \"SmolVLA baseline 57.2% vs 59.2% inconsistency\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"Section 4.2 uses 57.2%, Table 2 uses 59.2%. Not explained at first mention.\"}\n  action_items:\n    - {round: 5, action: \"§4.2 first mention changed to '57.2%–59.2% across two evaluation protocols (Appendix B)'\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Section 4.2 now reads '57.2%--59.2% SR across two evaluation protocols; Appendix B'.\"\n  resolution_round: 5\n\n- id: \"R5-W3\"\n  summary: \"Discussion over-compressed, missing Appendix pointer\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"Mechanistic insights moved to appendix but no cross-reference.\"}\n  action_items:\n    - {round: 5, action: \"Added 'see Appendices J and L' sentence in Discussion\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Discussion §5 now includes cross-reference to Appendices J and L.\"\n  resolution_round: 5\n\n- id: \"R5-W4\"\n  summary: \"Hypergeometric model C=91 parameter origin unclear\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 independent convergence\", note: \"Is C fitted or independently measured?\"}\n  action_items:\n    - {round: 5, action: \"Appendix: honest description — C and T jointly fit\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Appendix C.8: 'C and T are jointly fit by minimizing RMSE against four cliff-zone data points.'\"\n  resolution_round: 5\n\n- id: \"R5-W5\"\n  summary: \"'All tokens carry equal weight' imprecise wording\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R2 raised, R1 partial REBUT but AGREE on precision\", note: \"L2 norm uniformity ≠ task-relevant information uniformity.\"}\n  action_items:\n    - {round: 5, action: \"Changed to precise formulation linking CV=0.038 to spatial downsampling argument\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Section 4.4 π0 paragraph: wording updated.\"\n  resolution_round: 5\n\n# ===== Round 6 New Issues =====\n\n- id: \"R6-C1\"\n  summary: \"CV diagnostic evidence base insufficient — N=3-4 closed-loop models cannot establish reliable diagnostic\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1+R2+R3 consensus\", note: \"Method sensitivity data from only 3 models (SmolVLA 0% excluded). Spearman N=4 minimum p≈0.083, cannot reach significance. Claim 'enables strategy selection without downstream evaluation' unsupported.\"}\n  action_items:\n    - {round: 6, action: \"Option A: Add 3+ VLA architectures for closed-loop CV validation. Option B: Downgrade claim from 'diagnostic' to 'preliminary observation/correlate'. Option C: Add formal Spearman test + acknowledge statistical limitation.\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C2\"\n  summary: \"Table 2 data heavily missing — ~20% entries are '--', OpenVLA only Object suite\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(W4)+R2(N3)+R3(N3) — 3/3 consensus\", note: \"π₀.5 Goal k=0.9R/k=0.7L missing; X-VLA Long mostly empty; OpenVLA only Object. 'Cross-suite analysis' claim unsupported. R1 argues severity=warning (SmolVLA 0% is a finding not missing data); R2/R3 argue Must-Fix.\"}\n  action_items:\n    - {round: 6, action: \"Complete all missing experiments in Table 2, especially OpenVLA Spatial/Goal/Long and X-VLA Long suite\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C3\"\n  summary: \"Causal narrative overreach — 'primary determinant' unsupported without matched-backbone control\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(N2)+R3 AGREE, R2 indirect support\", note: \"Conclusion uses 'primary determinant' but Appendix I admits 'preventing clean isolation'. Title implies causal direction. 6 models differ in backbone/encoder/scale/data simultaneously.\"}\n  action_items:\n    - {round: 6, action: \"'primary determinant' → 'strongest observed correlate' or 'primary correlate' in Conclusion. Add confounder caveat sentence in Conclusion.\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C4\"\n  summary: \"Missing attention-based pruning baseline — L2 norm + random insufficient bracket\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(N3)+R2 AGREE\", note: \"Attention-based scoring (FastV/VLA-Cache standard) and gradient-based importance absent. Related Work cites these methods but experiments don't use them — narrative gap. If attention-based also fails on entangling connectors, it would strengthen the paper's core claim.\"}\n  action_items:\n    - {round: 6, action: \"Add attention-based scoring baseline on at least 2-3 models, OR explicitly justify exclusion in Limitations with discussion of why L2+random bracket is sufficient\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C5\"\n  summary: \"Generative AI usage disclosure missing — CoRL 2026 compliance requirement\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(N1)+R2 AGREE\", note: \"CoRL 2026 requires explicit AI tool disclosure. Completely absent. Potential desk rejection risk.\"}\n  action_items:\n    - {round: 6, action: \"Add Generative AI disclosure in Acknowledgments or after Limitations\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C6\"\n  summary: \"VTR vs Smart Compress naming inconsistency — core contribution has two unrelated names\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(N2)+R2 AGREE+R1 AGREE\", note: \"Main text uses 'VTR', Appendix E/F/G/H uses 'Smart Compress'. No lexical overlap between names. Readers cannot determine if they refer to the same component.\"}\n  action_items:\n    - {round: 6, action: \"Global search-replace 'Smart Compress' → 'VTR' throughout appendix\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"VTR contribution weakened by MLP adapter control — cross-attention not the key mechanism\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(W1)+R2(W1)+R3 AGREE — 3/3 consensus\", note: \"MLP adapter 63.4% vs VTR 60.1% (p=0.15). Introduction C3 frames VTR as contribution but evidence shows any re-encoding works. Should reframe C3 as 'learned re-encoding recovers pixel-shuffle collapse'.\"}\n  action_items:\n    - {round: 6, action: \"Reframe C3 contribution: 'learned re-encoding' not 'VTR architecture'. Acknowledge VTR=Q-Former application in Related Work.\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"LaTeX rendering error: $\\\\pi_0.5$ should be $\\\\pi_{0.5}$ — 50+ occurrences\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(W1)+R2(M4)+R1 AGREE — 3/3 consensus\", note: \"Only '0' subscripted, '.5' renders in text font. Systematic error across all .tex files.\"}\n  action_items:\n    - {round: 6, action: \"Global replace $\\\\pi_0.5$ → $\\\\pi_{0.5}$ in all .tex files\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Limitations section too short — 3 sentences, missing key limitations\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(W2)+R2 AGREE+R1 implied\", note: \"Only 60 words as \\\\paragraph. Missing: single benchmark, pruning method limitation, CV N=3 caveat, VTR single-model, single-seed for most conditions. CoRL requires substantive Limitations section.\"}\n  action_items:\n    - {round: 6, action: \"Expand Limitations to 150-200 words, upgrade to \\\\subsection or \\\\section, cover sim-only + single benchmark + N=3 CV + pruning method scope + single-seed\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"Simulation-only evaluation — no real-robot validation, no sim-to-real discussion\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2(W4)+R3 AGREE\", note: \"CoRL CFP: 'prioritize real-robot experiments or provide convincing sim-to-real evidence'. Paper has neither. Compressor-VLA (concurrent) includes real-robot validation.\"}\n  action_items:\n    - {round: 6, action: \"Add sim-to-real transferability discussion in Limitations, or conduct minimal real-robot validation\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"OpenVLA only evaluated on Object suite — no cross-suite data for high-CV independent connector\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2(W5)+R1 AGREE\", note: \"OpenVLA is the only high-CV independent-connector model. Missing Spatial/Goal/Long data means task-complexity axis unvalidated for MLP connector.\"}\n  action_items:\n    - {round: 6, action: \"Run OpenVLA evaluation on Spatial, Goal, Long suites\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"No code/data release plan stated\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(W3)+R2 AGREE\", note: \"Empirical paper with implementation-dependent results. No anonymous repo or release commitment.\"}\n  action_items:\n    - {round: 6, action: \"Add 'Code and data will be released upon acceptance' statement\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Post-connector pruning choice not justified — pre-connector pruning could yield different conclusions\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(W5)+R2 AGREE\", note: \"Concurrent work (VLA-Cache, EfficientVLA) operates at KV-cache or pre-connector. Pre-connector pruning might not cause pixel-shuffle catastrophe. Paper's findings may be specific to post-connector pruning.\"}\n  action_items:\n    - {round: 6, action: \"Add justification paragraph in Section 3.2, or discuss as limitation\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W8\"\n  summary: \"Cross-condition seed inconsistency — Table 2 comparisons use different seeds without annotation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(W3)+R2 AGREE\", note: \"OpenVLA L2=seed42, random=seed7. Same-seed control in Appendix only. Table 2 caption should note seed differences.\"}\n  action_items:\n    - {round: 6, action: \"Add seed annotation to Table 2 caption or footnote\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I1\"\n  summary: \"Paper identity split — three contributions each insufficiently deep\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2(N2)+R3 AGREE\", note: \"Empirical study / diagnostic tool / method — each too shallow. Need to choose primary identity and deepen.\"}\n  action_items:\n    - {round: 6, action: \"Clarify primary identity — recommend empirical study with CV and VTR as secondary findings\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I2\"\n  summary: \"Abstract information density too high — 17 numbers/percentages\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(W4), R2 partial REBUT (specific numbers are selling point)\", note: \"Divergence on severity. Consensus: keep 3-4 key numbers, reduce secondary ones.\"}\n  action_items:\n    - {round: 6, action: \"Reduce Abstract to 4-5 key numbers, replace secondary numbers with qualitative descriptions\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I3\"\n  summary: \"'Don't Run with Scissors' differentiation discussion insufficient in Related Work\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2(W2), R1 REBUT (different domain: closed-loop robotic vs VLM VQA)\", note: \"Divergence. R1 argues sufficient differentiation exists. R2 wants explicit comparison paragraph.\"}\n  action_items:\n    - {round: 6, action: \"Add 1-2 sentence explicit comparison in Related Work\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "issues_yaml": "\n# ===== Round 4-5 Issues (all resolved) =====\n\n- id: \"R4-C1\"\n  summary: \"Causal claim under-identified — connector vs backbone/encoder/action confound\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"determines needs downgrade to associated with\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — full-text causal language downgrade confirmed. No residual 'determines' found.\"}\n  action_items:\n    - {round: 4, action: \"Full-text causal language downgrade (determines→associated, controlled→closest available)\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Round 5 verified: determines→strongly associated with, predicts→correlates, falsifies→demonstrates. Appendix N confound analysis added. Both reviewers confirm thorough and consistent.\"\n  resolution_round: 5\n\n- id: \"R4-C2\"\n  summary: \"SmolVLA baseline 44.8% vs official — cliff and VTR on undertrained checkpoint\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Official checkpoint full pruning sweep is minimum requirement\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — official checkpoint (57.2% baseline) multi-k verification complete. Dual evaluation protocol in Appendix Table 3.\"}\n  action_items:\n    - {round: 4, action: \"SmolVLA official checkpoint pruning sweep (10 configs)\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Write official results into paper\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Official HF checkpoint (57.2% baseline) shows 0% at k=0.95/0.9/0.5. Dual protocol (59.2%/57.2%) both confirm cliff. VTR M=32 recovers to 60.1±1.3%.\"\n  resolution_round: 5\n\n- id: \"R4-C3\"\n  summary: \"CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"3 data points = 3 connector clusters, CV adds no predictive power beyond label\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — CV reframed as correlational diagnostic. Section 4.6 title changed. Limitations explicit about N=3, 2 k values.\"}\n  action_items:\n    - {round: 4, action: \"Reframe CV as correlational diagnostic, add X-VLA within-family variance argument\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"CV reframed as 'diagnostic metric that correlates with' (not 'predictor'). Contribution C2 updated. Section 5 Limitations: 'the CV correlation spans three models and two retention ratios'.\"\n  resolution_round: 5\n\n- id: \"R4-C4\"\n  summary: \"π0 offline-only used in core taxonomy argument\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Internal consistency: paper argues offline unreliable but uses π0 offline for taxonomy\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Table 1 footnote, Introduction caveat, 4-in-closed-loop framing all confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Table 1 π0 offline-only label, caveat on π0-OpenVLA 63pp gap, CogACT literature label\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Table 1: †offline metrics only. Introduction: 'evaluating four in closed-loop and analyzing three via offline metrics or literature'. π0-OpenVLA comparison has causal interpretation caveat.\"\n  resolution_round: 5\n\n- id: \"R4-S1\"\n  summary: \"X-VLA linear projection label misleading (has 12-layer BART encoder)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Table 1 label should reflect BART encoder\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Linear + BART (12L)‡ confirmed in Table 1.\"}\n  action_items:\n    - {round: 4, action: \"Table 1 connector column update + continuous spectrum discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Table 1: Linear + BART (12L)‡. Footnote explains effective pipeline.\"\n  resolution_round: 5\n\n- id: \"R4-S2\"\n  summary: \"OpenVLA L2 vs random cross-seed, k=0.5 same-seed missing\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2\", note: \"CV scaling law crossover point based on cross-seed comparison\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Footnote 5: same-seed k=0.5: 35.8% random vs 39.2% L2 (gap 3.4pp).\"}\n  action_items:\n    - {round: 4, action: \"OpenVLA random k=0.5 seed42 completed\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Three k values (0.3, 0.5, 0.7) same-seed verified. k=0.5 gap = 3.4pp.\"\n  resolution_round: 5\n\n- id: \"R4-S3\"\n  summary: \"VTR novelty limited — Perceiver/Q-Former VLA application\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 agree\", note: \"Contribution is diagnostic (why re-encoding works), not method\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — diagnostic protocol framing confirmed throughout.\"}\n  action_items:\n    - {round: 4, action: \"Reframe VTR as diagnostic contribution\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"VTR framed as diagnostic tool.\"\n  resolution_round: 5\n\n- id: \"R4-S4\"\n  summary: \"VTR p=0.15 insufficient for re-encoding is operative mechanism claim\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 agree\", note: \"MLP adapter SR higher, claim should be about re-encoding in general\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 'comparable recovery (p=0.15)' confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Soften claim to both architectures achieve comparable recovery\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"p=0.15 reported as 'comparable'. MLP adapter architecture details in Appendix F.3.\"\n  resolution_round: 5\n\n- id: \"R4-S5\"\n  summary: \"Diagnose-then-Compress framework overpackaged\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 agree\", note: \"Single-metric lookup table, not a framework\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — all 'framework' replaced with 'diagnostic protocol'.\"}\n  action_items:\n    - {round: 4, action: \"Replace framework with diagnostic protocol globally\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Global replacement confirmed.\"\n  resolution_round: 5\n\n- id: \"R4-S6\"\n  summary: \"Paper ~13 pages vs CoRL 8-page limit\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"Section 5 Analysis ~3 pages is main excess\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 8 pages main text confirmed.\"}\n  action_items:\n    - {round: 4, action: \"Major restructure: Analysis→Appendix, target 8 pages\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Pages 1-8 main text. CoRL compliant.\"\n  resolution_round: 5\n\n- id: \"R4-S7\"\n  summary: \"Falsifies immune assumption — straw man\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2+R1 partial agree\", note: \"Soften to demonstrates offline tolerance does not generalize\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — no 'falsifies' in paper.\"}\n  action_items:\n    - {round: 4, action: \"Replace falsifies with demonstrates offline tolerance caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"All 'falsifies' removed.\"\n  resolution_round: 5\n\n- id: \"R4-S8\"\n  summary: \"M=96 dip vs flat M-curve narrative\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1 warning, R2 partial rebut\", note: \"Change flat to relatively stable\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — 'relatively stable' confirmed.\"}\n  action_items:\n    - {round: 4, action: \"flat→relatively stable, add M=96 dip discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"All 'flat' replaced. Appendix D: M=96 dip explained.\"\n  resolution_round: 5\n\n- id: \"R4-M1\"\n  summary: \"Related Work citation count insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer assessment\", note: \"Need 15-20 additional citations\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — ~46 citations.\"}\n  action_items:\n    - {round: 4, action: \"Expand Related Work with 15+ citations\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"30+ citations across 4 categories.\"\n  resolution_round: 5\n\n- id: \"R4-M3\"\n  summary: \"VTR vs official baseline statistical significance p=0.72\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer calculation\", note: \"Remove any claim VTR matches official\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — framed as recovery from 0%.\"}\n  action_items:\n    - {round: 4, action: \"Fix VTR vs official framing\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Primary contribution: recovering from 0% where deletion fails.\"\n  resolution_round: 5\n\n- id: \"R4-M4\"\n  summary: \"D141 token position visualization not written into paper\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"Reviewer assessment\", note: \"High ROI — spatial clustering evidence\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — Appendix Token Position Analysis with DBSCAN clustering.\"}\n  action_items:\n    - {round: 4, action: \"Write D141 visualization into appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Appendix with DBSCAN clustering at k=0.7/0.5/0.3.\"\n  resolution_round: 5\n\n- id: \"R5-V1\"\n  summary: \"Figure 4 placeholder on page 17 — not replaced with actual token importance heatmap\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"Visual Check Agent\", note: \"Displays '[Placeholder: token importance heatmap]' gray text box.\"}\n  action_items:\n    - {round: 5, action: \"Replace Figure 4 placeholder with actual token importance heatmap\", assigned_to: \"director+agent\", status: \"done\"}\n  resolution: \"Real dual-panel heatmap generated. Reviewer visual check confirmed.\"\n  resolution_round: 5\n\n- id: \"R5-W1\"\n  summary: \"π₀.5 V-shape non-monotonic recovery unexplained by hypergeometric model\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"Hypergeometric model predicts monotonic collapse but data shows 72pp recovery at k≤0.7.\"}\n  action_items:\n    - {round: 5, action: \"§4.7: added model applicability boundary sentence\", assigned_to: \"director\", status: \"done\"}\n    - {round: 5, action: \"Appendix: added single hypothesis (computation regime shift) + 'remains untested'\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Results.tex §4.7: model boundary statement added. Appendix C.8: V-shape hypothesis with 'remains untested' caveat.\"\n  resolution_round: 5\n\n- id: \"R5-W2\"\n  summary: \"SmolVLA baseline 57.2% vs 59.2% inconsistency\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"Section 4.2 uses 57.2%, Table 2 uses 59.2%. Not explained at first mention.\"}\n  action_items:\n    - {round: 5, action: \"§4.2 first mention changed to '57.2%–59.2% across two evaluation protocols (Appendix B)'\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Section 4.2 now reads '57.2%--59.2% SR across two evaluation protocols; Appendix B'.\"\n  resolution_round: 5\n\n- id: \"R5-W3\"\n  summary: \"Discussion over-compressed, missing Appendix pointer\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"Mechanistic insights moved to appendix but no cross-reference.\"}\n  action_items:\n    - {round: 5, action: \"Added 'see Appendices J and L' sentence in Discussion\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Discussion §5 now includes cross-reference to Appendices J and L.\"\n  resolution_round: 5\n\n- id: \"R5-W4\"\n  summary: \"Hypergeometric model C=91 parameter origin unclear\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1+R2 independent convergence\", note: \"Is C fitted or independently measured?\"}\n  action_items:\n    - {round: 5, action: \"Appendix: honest description — C and T jointly fit\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Appendix C.8: 'C and T are jointly fit by minimizing RMSE against four cliff-zone data points.'\"\n  resolution_round: 5\n\n- id: \"R5-W5\"\n  summary: \"'All tokens carry equal weight' imprecise wording\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R2 raised, R1 partial REBUT but AGREE on precision\", note: \"L2 norm uniformity ≠ task-relevant information uniformity.\"}\n  action_items:\n    - {round: 5, action: \"Changed to precise formulation linking CV=0.038 to spatial downsampling argument\", assigned_to: \"director\", status: \"done\"}\n  resolution: \"Section 4.4 π0 paragraph: wording updated.\"\n  resolution_round: 5\n\n# ===== Round 6 New Issues =====\n\n- id: \"R6-C1\"\n  summary: \"CV diagnostic evidence base insufficient — N=3-4 closed-loop models cannot establish reliable diagnostic\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1+R2+R3 consensus\", note: \"Method sensitivity data from only 3 models (SmolVLA 0% excluded). Spearman N=4 minimum p≈0.083, cannot reach significance. Claim 'enables strategy selection without downstream evaluation' unsupported.\"}\n  action_items:\n    - {round: 6, action: \"Option A: Add 3+ VLA architectures for closed-loop CV validation. Option B: Downgrade claim from 'diagnostic' to 'preliminary observation/correlate'. Option C: Add formal Spearman test + acknowledge statistical limitation.\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C2\"\n  summary: \"Table 2 data heavily missing — ~20% entries are '--', OpenVLA only Object suite\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(W4)+R2(N3)+R3(N3) — 3/3 consensus\", note: \"π₀.5 Goal k=0.9R/k=0.7L missing; X-VLA Long mostly empty; OpenVLA only Object. 'Cross-suite analysis' claim unsupported. R1 argues severity=warning (SmolVLA 0% is a finding not missing data); R2/R3 argue Must-Fix.\"}\n  action_items:\n    - {round: 6, action: \"Complete all missing experiments in Table 2, especially OpenVLA Spatial/Goal/Long and X-VLA Long suite\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C3\"\n  summary: \"Causal narrative overreach — 'primary determinant' unsupported without matched-backbone control\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(N2)+R3 AGREE, R2 indirect support\", note: \"Conclusion uses 'primary determinant' but Appendix I admits 'preventing clean isolation'. Title implies causal direction. 6 models differ in backbone/encoder/scale/data simultaneously.\"}\n  action_items:\n    - {round: 6, action: \"'primary determinant' → 'strongest observed correlate' or 'primary correlate' in Conclusion. Add confounder caveat sentence in Conclusion.\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C4\"\n  summary: \"Missing attention-based pruning baseline — L2 norm + random insufficient bracket\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(N3)+R2 AGREE\", note: \"Attention-based scoring (FastV/VLA-Cache standard) and gradient-based importance absent. Related Work cites these methods but experiments don't use them — narrative gap. If attention-based also fails on entangling connectors, it would strengthen the paper's core claim.\"}\n  action_items:\n    - {round: 6, action: \"Add attention-based scoring baseline on at least 2-3 models, OR explicitly justify exclusion in Limitations with discussion of why L2+random bracket is sufficient\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C5\"\n  summary: \"Generative AI usage disclosure missing — CoRL 2026 compliance requirement\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(N1)+R2 AGREE\", note: \"CoRL 2026 requires explicit AI tool disclosure. Completely absent. Potential desk rejection risk.\"}\n  action_items:\n    - {round: 6, action: \"Add Generative AI disclosure in Acknowledgments or after Limitations\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C6\"\n  summary: \"VTR vs Smart Compress naming inconsistency — core contribution has two unrelated names\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(N2)+R2 AGREE+R1 AGREE\", note: \"Main text uses 'VTR', Appendix E/F/G/H uses 'Smart Compress'. No lexical overlap between names. Readers cannot determine if they refer to the same component.\"}\n  action_items:\n    - {round: 6, action: \"Global search-replace 'Smart Compress' → 'VTR' throughout appendix\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"VTR contribution weakened by MLP adapter control — cross-attention not the key mechanism\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(W1)+R2(W1)+R3 AGREE — 3/3 consensus\", note: \"MLP adapter 63.4% vs VTR 60.1% (p=0.15). Introduction C3 frames VTR as contribution but evidence shows any re-encoding works. Should reframe C3 as 'learned re-encoding recovers pixel-shuffle collapse'.\"}\n  action_items:\n    - {round: 6, action: \"Reframe C3 contribution: 'learned re-encoding' not 'VTR architecture'. Acknowledge VTR=Q-Former application in Related Work.\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"LaTeX rendering error: $\\\\pi_0.5$ should be $\\\\pi_{0.5}$ — 50+ occurrences\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(W1)+R2(M4)+R1 AGREE — 3/3 consensus\", note: \"Only '0' subscripted, '.5' renders in text font. Systematic error across all .tex files.\"}\n  action_items:\n    - {round: 6, action: \"Global replace $\\\\pi_0.5$ → $\\\\pi_{0.5}$ in all .tex files\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Limitations section too short — 3 sentences, missing key limitations\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(W2)+R2 AGREE+R1 implied\", note: \"Only 60 words as \\\\paragraph. Missing: single benchmark, pruning method limitation, CV N=3 caveat, VTR single-model, single-seed for most conditions. CoRL requires substantive Limitations section.\"}\n  action_items:\n    - {round: 6, action: \"Expand Limitations to 150-200 words, upgrade to \\\\subsection or \\\\section, cover sim-only + single benchmark + N=3 CV + pruning method scope + single-seed\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"Simulation-only evaluation — no real-robot validation, no sim-to-real discussion\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2(W4)+R3 AGREE\", note: \"CoRL CFP: 'prioritize real-robot experiments or provide convincing sim-to-real evidence'. Paper has neither. Compressor-VLA (concurrent) includes real-robot validation.\"}\n  action_items:\n    - {round: 6, action: \"Add sim-to-real transferability discussion in Limitations, or conduct minimal real-robot validation\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"OpenVLA only evaluated on Object suite — no cross-suite data for high-CV independent connector\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2(W5)+R1 AGREE\", note: \"OpenVLA is the only high-CV independent-connector model. Missing Spatial/Goal/Long data means task-complexity axis unvalidated for MLP connector.\"}\n  action_items:\n    - {round: 6, action: \"Run OpenVLA evaluation on Spatial, Goal, Long suites\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"No code/data release plan stated\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(W3)+R2 AGREE\", note: \"Empirical paper with implementation-dependent results. No anonymous repo or release commitment.\"}\n  action_items:\n    - {round: 6, action: \"Add 'Code and data will be released upon acceptance' statement\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Post-connector pruning choice not justified — pre-connector pruning could yield different conclusions\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(W5)+R2 AGREE\", note: \"Concurrent work (VLA-Cache, EfficientVLA) operates at KV-cache or pre-connector. Pre-connector pruning might not cause pixel-shuffle catastrophe. Paper's findings may be specific to post-connector pruning.\"}\n  action_items:\n    - {round: 6, action: \"Add justification paragraph in Section 3.2, or discuss as limitation\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W8\"\n  summary: \"Cross-condition seed inconsistency — Table 2 comparisons use different seeds without annotation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1(W3)+R2 AGREE\", note: \"OpenVLA L2=seed42, random=seed7. Same-seed control in Appendix only. Table 2 caption should note seed differences.\"}\n  action_items:\n    - {round: 6, action: \"Add seed annotation to Table 2 caption or footnote\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I1\"\n  summary: \"Paper identity split — three contributions each insufficiently deep\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2(N2)+R3 AGREE\", note: \"Empirical study / diagnostic tool / method — each too shallow. Need to choose primary identity and deepen.\"}\n  action_items:\n    - {round: 6, action: \"Clarify primary identity — recommend empirical study with CV and VTR as secondary findings\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I2\"\n  summary: \"Abstract information density too high — 17 numbers/percentages\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3(W4), R2 partial REBUT (specific numbers are selling point)\", note: \"Divergence on severity. Consensus: keep 3-4 key numbers, reduce secondary ones.\"}\n  action_items:\n    - {round: 6, action: \"Reduce Abstract to 4-5 key numbers, replace secondary numbers with qualitative descriptions\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I3\"\n  summary: \"'Don't Run with Scissors' differentiation discussion insufficient in Related Work\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2(W2), R1 REBUT (different domain: closed-loop robotic vs VLM VQA)\", note: \"Divergence. R1 argues sufficient differentiation exists. R2 wants explicit comparison paragraph.\"}\n  action_items:\n    - {round: 6, action: \"Add 1-2 sentence explicit comparison in Related Work\", assigned_to: \"research_director\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-23T05:58:23.003088+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml\", \"bytes\": 25948}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-23T06:01:04.523377+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "reviewer_ids_acknowledged": "[1, 2, 3]",
  "cross_response_reviewer_ids": "[1, 2, 3]",
  "overall_score": "weak reject",
  "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd",
  "report": "\n# Round 6 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others\n\n**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n论文研究 vision token pruning 在不同 VLA 架构上的表现差异，提出 connector architecture 是 pruning robustness 的主要关联因素。核心发现：(1) pixel-shuffle connector (SmolVLA) 在仅移除 5% token 即崩溃至 0% SR，经双 checkpoint 验证；(2) token-entangling connectors 展现 task-complexity amplified collapse（X-VLA 在 Object 仅损失 1.4pp 但 Goal 损失 27.8pp）；(3) CV of L2 norms 作为 diagnostic 与 pruning tolerance 相关；(4) VTR (cross-attention re-encoding) 在 SmolVLA 上从 0% 恢复至 ~60% SR。实验覆盖 6 个 VLA 架构（450M-7B），4 个 LIBERO task suite，2 种 pruning 策略。\n\n---\n\n## Strengths\n\n**S1** [3/3 共识] **Pixel-shuffle 崩溃机制发现扎实且有价值。** SmolVLA 在 k=0.95（仅移除 6/128 tokens）即从 59.2% 崩溃至 0.0% SR，经 LoRA fine-tuned 和官方 checkpoint 双重验证，7 种 pruning 配置（ACIS/random/L2 × zero-mask/true removal/ToMe）均为 0%。这是从 pixel-shuffle 架构定义可演绎推导但首次被系统实证的结果，对 practitioners 有直接预警价值。(Section 4.3, Table 3/Appendix D)\n\n**S2** [3/3 共识] **实验设计系统性在 VLA pruning 文献中范围最广。** 6 个架构 × 3 种 connector family × 2 种 pruning 策略 × 6 个 retention ratio，附录详尽（27 页，含 per-task breakdown、multi-seed validation、hypergeometric model、attention entropy analysis）。Wilson 95% CI + 500 episodes/condition 是合理的统计实践。\n\n**S3** [3/3 共识] **写作清晰，结构合理。** Figure 1 teaser 有效传达 two-axis framework，Table 1 model properties 设计精简，Introduction 的 problem→gap→approach→contributions 流程逻辑严密。\n\n**S4** [2/3 共识] **Limitations 态度诚实。** 论文承认 simulation-only、causal isolation 不可能、CV data points 有限等核心局限（虽然主文过短，扩展讨论在 Appendix A）。\n\n**S5** **VTR 从 0% 恢复至 ~60% SR 是有价值的 proof-of-concept。** 在所有 hard pruning 方法均失败的条件下，22M 参数的 re-encoding 模块在 75% 压缩下恢复功能性能。MLP adapter 达到 comparable 性能 (p=0.15) 的发现本身也有价值——说明 re-encoding 而非特定架构是关键。\n\n---\n\n## Weaknesses (Must-Fix)\n\n**W-MF1** [3/3 全员共识] **CV diagnostic 证据严重不足——N=3-4 闭环模型无法建立可靠诊断工具。**\n- 论文声称 CV \"enables connector-appropriate compression strategy selection without downstream evaluation\" (Introduction C2, Section 3.3)\n- 实际闭环验证仅 4 个模型；method sensitivity 有效数据点仅 3 个（SmolVLA 全 0% 无法参与 method gap 比较）\n- Spearman rank correlation N=4 时最小可能 p≈0.083，**原则上无法达到 0.05 显著性**\n- 论文未报告任何正式相关性检验\n- **R1 量化**：4 个单调排列概率 ≤ 1/24 ≈ 4.2%，统计边缘\n- **严重性**：C2 是论文核心 contribution 之一，evidence base 不足直接削弱论文价值\n\n**W-MF2** [3/3 全员共识] **Table 2（核心结果表）数据大量缺失，削弱 cross-architecture, cross-suite analysis 的 claim。**\n- π₀.5 Goal: k=0.9 Random 和 k=0.7 L2 缺失\n- X-VLA Long: k=0.9/0.7/0.5 大部分缺失\n- X-VLA Spatial/Goal: 部分缺失\n- **OpenVLA 仅评估 Object 一个 suite**——论文中唯一的 high-CV independent-connector 模型在 task-complexity axis 上完全无验证\n- Abstract 声称 \"Evaluation spans six VLA architectures... and four LIBERO task suites\"，与实际数据矩阵填充率不足 70% 形成叙事落差\n- **严重性分歧**：R2/R3 列为 Must-Fix，R1 列为 Should-Fix（认为 SmolVLA 0% 是 finding 不是缺失）。Review Director 裁定 Must-Fix——对 empirical study 而言数据完整性是底线\n\n**W-MF3** [2/3 共识 + 1/3 间接支持] **因果叙事超出证据范围——\"primary determinant\" 在无 matched-backbone 控制下不可支撑。**\n- Conclusion: \"connector coupling is the primary determinant of pruning robustness\"\n- 6 个模型同时在 backbone (Qwen2/PaliGemma/Llama-2)、参数量 (450M-7B, 16×)、vision encoder (SigLIP variants/DINOv2)、token 数量 (50-768, 15×) 上不同\n- Appendix N 承认 \"preventing clean isolation of the connector effect from backbone differences\"\n- **Conclusion 与 Limitations 直接矛盾**（R3 叙事一致性检查确认）\n- Title \"Vision Connectors and VLA Token Compressibility\" 隐含因果方向\n\n**W-MF4** [2/3 共识] **缺少 attention-based pruning baseline——论文引用但不测试的标准方法。**\n- Attention-based scoring 是 VLA/VLM token pruning 最自然的竞争方法（FastV、VLA-Cache 采用）\n- Related Work 引用了 FastV 和 VLA-Cache，但实验不使用 attention-based scoring——叙事缺口\n- 如果 attention-based 在 entangling connectors 上也失败，会大幅加强论文核心 narrative\n- L2 norm 在 OpenVLA 上与 random 差距 <3pp (Appendix E.10)，说明 L2 并非总是有效的 importance score\n- Gradient-based importance 也完全缺失\n\n**W-MF5** [2/3 共识] **Generative AI 使用披露完全缺失——CoRL 2026 合规硬要求。**\n- CoRL 2026 Author Instructions 明确要求披露 AI 工具使用\n- 论文全文无任何相关声明\n- 可能触发 desk rejection 或 AC 质疑\n\n**W-MF6** [3/3 全员共识] **VTR 与 Smart Compress 命名不一致——核心贡献术语混乱。**\n- 主文 Section 3.4/4.5 使用 \"Vision Token Re-encoder (VTR)\"\n- Appendix E/F/G/H 大量使用 \"Smart Compress\"/\"Smart Compressor\"\n- 两个名字无任何词汇重叠，读者无法确定是否为同一组件\n- 损害核心贡献（C3）的可信度和可理解性\n\n---\n\n## Weaknesses (Should-Fix)\n\n**W-SF1** [3/3 全员共识] **VTR 贡献被 MLP adapter 控制实验严重削弱。**\n- MLP adapter 63.4±2.6% vs VTR 60.1±1.3% (p=0.15)，MLP 点估计更高\n- Introduction C3 以 VTR 为主角，但证据表明 cross-attention 非关键——任何 learned re-encoding 都能恢复 pixel-shuffle collapse\n- VTR ≈ Q-Former/BLIP-2 applied to VLA token compression，architecture novelty 有限\n- 建议：将 C3 reframe 为 \"learned re-encoding recovers pixel-shuffle VLAs\"\n\n**W-SF2** [3/3 全员共识] **LaTeX 渲染错误 `$\\pi_0.5$` 全文 50+ 处。**\n- 正确写法 `$\\pi_{0.5}$`，当前仅 \"0\" 下标，\".5\" 以正文字体显示\n- 反映稿件准备粗糙度\n\n**W-SF3** [2/3 共识] **Limitations section 过于简短——3 句话（~60 词），格式为 \\\\paragraph。**\n- CoRL 要求 \"describe limiting assumptions, failure modes, and other limitations\"\n- 遗漏关键局限：单一 benchmark (LIBERO only)、N=3 CV evidence base、pruning 方法范围有限（仅 L2+random）、VTR 单模型验证、主实验多为单 seed\n- Appendix A 有 extended discussion 但 reviewer 不要求读附录\n\n**W-SF4** [2/3 共识] **仅 LIBERO simulation 评估，无 real-robot 验证或 sim-to-real 讨论。**\n- CoRL CFP: \"prioritize real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots\"\n- Compressor-VLA (concurrent work) 已含 real-robot 验证\n- Conclusion 仅将 real-robot 列为 future work，无 transferability 论证\n\n**W-SF5** [2/3 共识] **Post-connector pruning 选择缺乏系统 justification。**\n- 未讨论 pre-connector pruning 可能性\n- Concurrent work (VLA-Cache, EfficientVLA) 在 KV-cache 或 pre-connector 操作\n- Pre-connector pruning 对 pixel-shuffle 可能不 catastrophic，论文核心发现可能限于 post-connector 这一特定设定\n\n**W-SF6** [2/3 共识] **跨条件使用不同 seed，Table 2 未标注。**\n- OpenVLA L2=seed42, random=seed7\n- Same-seed 控制仅在 Appendix 提供\n- Table 2 caption 无 seed 信息\n\n**W-SF7** [2/3 共识] **论文 identity 分裂——empirical study / diagnostic tool / method 三者各自不够深入。**\n- C1 empirical study 数据缺失 (Table 2)\n- C2 diagnostic tool N=3 不可靠\n- C3 method 被 MLP adapter 平替\n- \"三个 shallow contribution 拼凑\" 结构削弱整体力量\n\n**W-SF8** **No code/data release plan.** 对 empirical 论文的 reproducibility 有影响。建议添加 \"Code and data will be released upon acceptance\" 声明。\n\n---\n\n## Reviewer Consensus\n\n以下问题经交叉分享后达成共识：\n\n| 问题 | R1 | R2 | R3 | 共识 |\n|------|-----|-----|-----|------|\n| CV diagnostic N=3-4 不足 | Must-Fix (N1) | Must-Fix (N1) | AGREE | ★★★ |\n| Table 2 数据缺失 | Should-Fix (W4) | Must-Fix (N3) | Must-Fix (N3) | ★★★ |\n| VTR 被 MLP adapter 削弱 | Should-Fix (W1) | Should-Fix (W1) | AGREE | ★★★ |\n| VTR/Smart Compress 命名 | AGREE | AGREE | Must-Fix (N2) | ★★★ |\n| π₀.₅ LaTeX 错误 | AGREE | Minor (M4) | Should-Fix (W1) | ★★★ |\n| 因果叙事过强 | Must-Fix (N2) | indirect | AGREE | ★★☆ |\n| Simulation-only | — | Should-Fix (W4) | AGREE | ★★☆ |\n| Attention-based baseline 缺失 | Must-Fix (N3) | AGREE | nuance | ★★☆ |\n| Limitations 过短 | implied | AGREE | Should-Fix (W2) | ★★☆ |\n| AI disclosure 缺失 | AGREE | AGREE | Must-Fix (N1) | ★★☆ |\n\n## Reviewer Divergence\n\n| 分歧点 | 立场 | 裁定 |\n|--------|------|------|\n| Table 2 严重性 | R1: Should-Fix (SmolVLA 0% 是 finding); R2/R3: Must-Fix | **Must-Fix**——empirical study 数据完整性是底线 |\n| \"Don't Run with Scissors\" 差异化 | R1: REBUT (不同 domain); R2: Should-Fix | 记录为 info——建议加 1-2 句对比但非关键 |\n| Abstract 信息密度 | R3: Should-Fix (17 个数字); R2: partial REBUT (数字是卖点) | 折中——保留 4-5 个关键数字 |\n| Figure 3 可读性 | R3: Should-Fix; R1: REBUT (尚可) | 记录为 info |\n| VTR 训练 batch size | R1: Should-Fix (不公平); R2: partial REBUT (比较对象是 0% 不是 baseline) | Should-Fix——VTR 内部消融公平，但与 baseline 比较需 caveat |\n| CV vs 替代 metric | R1: Should-Fix (未比较); R2: REBUT (N=3 比较无意义) | 取决于是否增加模型数量 |\n\n---\n\n## Questions\n\n1. **[R1-Q1, R2-Q1]** π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0%，但 k=0.7 反弹至 77.2%。这是否为单 seed 随机波动？multi-seed 复现了吗？\n2. **[R2-Q2, 3/3 共识]** MLP adapter 达到 63.4% vs VTR 60.1% (p=0.15)。作者如何看待这一结果？C3 的 value proposition 是什么？\n3. **[R2-Q3]** CV diagnostic 的 practical workflow 是什么？decision threshold 如何确定？3 个数据点如何建立可操作的指导？\n4. **[R2-Q4]** 是否在 SmolVLA 上比较过 GLUESTICK (Don't Run with Scissors 的 training-free recovery) 和 VTR？\n5. **[R1-Q5]** 同一 LLM backbone 搭配不同 connector，CV-pruning tolerance 关系是否成立？\n6. **[R1-Q3]** SmolVLA k=0.99（仅移除 1 token）是否仍崩溃？是否测试了更精细的崩溃阈值？\n7. **[R1-Q5b]** Pruning 后保持原始 position ID（不 re-index）结果是否变化？\n\n---\n\n## Missing References\n\n以下引用已被 Reviewer 确认覆盖（16 个指定检查的 concurrent work 全部已引用）。建议补充：\n- A Survey on Efficient Vision-Language-Action Models (2025, arXiv:2510.24795)\n- ATP-LLaVA (Adaptive Token Pruning for Large Vision Language Models)\n\n---\n\n## External Review\n\n**状态**：未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2 warning, 8 info, 0 critical）\n\n**Warnings:**\n1. **Page 2**: Figure 1 子面板内 axis label 和 legend 字号偏小（估计 ~6-7pt），接近可读性下限。打印后可能低于 8pt 最低建议。\n2. **Pages 23-25**: 附录连续 3 页纯文本无 figure/table/equation，缺乏视觉锚点。\n\n**Info items:**\n- Page 6: 正文唯一纯文本整页（四模型逐一结果），建议考虑 inline summary table\n- Page 27: 末页内容约 50%，下半部空白\n- Page 7: Table 2 格式正确（最优加粗），但无次优下划线或方向标记\n- Page 16: Figure 5 axis label 字号偏小\n- Page 5: Figure 2 legend 含 CV 值，字号略小\n- Pages 12-15: 附录 per-task breakdown 4 页连续表格，caption 清晰自包含\n- Page 4: Table 1 booktabs 风格专业\n- Page 8: Figure 3 bar chart 简洁有效\n\n---\n\n## Overall Assessment\n\n**评分：Weak Reject (5/10)**\n**置信度：4/5（High）**\n**Reviewer 评分：R1=5/10, R2=5/10, R3=6/10**\n\n论文发现了一个有价值的现象（pixel-shuffle connector 在 5% pruning 即 catastrophic collapse，经双 checkpoint 验证），实验设计的系统性在 VLA pruning 文献中范围最广，写作清晰。但存在以下结构性问题阻碍接收：\n\n1. **核心 contribution (CV diagnostic) 的统计基础不足**：N=3-4 闭环模型，Spearman N=4 原则上无法达到显著性。论文将 \"preliminary observation\" 包装为 \"diagnostic tool\"，claim 强度与 evidence 不匹配。\n2. **数据完整性不足**：核心结果表 (Table 2) 约 20% 条目缺失，OpenVLA 仅评估一个 suite，与 \"cross-architecture, cross-suite analysis\" 的 claim 矛盾。\n3. **因果推断超出证据范围**：6 个模型在 connector 外的多个维度同时不同，无 matched-backbone 控制实验。\n4. **Pruning baseline 不完整**：仅用 L2 norm + random，未测试 attention-based scoring。\n5. **论文 identity 分裂**：empirical study / diagnostic / method 三者各自不够深入。\n\n**修改路径建议**（Review Director 裁定，非建议作者）：\n- **最小修改（deadline 前可行）**：AI disclosure、命名统一、LaTeX 修复、Limitations 扩展、因果语言降级、CV claim 降级、Abstract 精简——这些纯文字修改可在 6 天内完成\n- **实质性修改（可能需要更多时间）**：Table 2 补全（需要 GPU 资源和实验时间）、attention-based baseline（需要新实验）、更多 VLA 架构验证 CV diagnostic\n- **理想但可能超出 deadline**：real-robot validation、matched-backbone control experiment\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract** (abstract.tex): 信息密度过高（17 个数字），建议精简至 4-5 个核心数字。\"six VLA architectures\" 应明确 \"four in closed-loop, two via offline metrics\"。\n\n**Introduction** (introduction.tex): 论证逻辑清晰。C2 的 claim \"enabling connector-appropriate compression strategy selection without downstream evaluation\" 过强，应降级。C3 应 reframe 为 learned re-encoding 而非 VTR 本身。\n\n**Related Work** (related_work.tex): 覆盖范围合理（~46 citations），但对 \"Don't Run with Scissors\" 的差异化讨论不足（仅在 VLA-specific methods 列表中一笔带过）。建议增加 1-2 句显式对比。VTR 与 Q-Former/BLIP-2 的关系未讨论。\n\n**Method** (method.tex): Section 3.2 pruning protocol 清晰但缺少 post-connector 选择的 justification。Section 3.3 CV 引入缺少与替代 metric (entropy/kurtosis/Gini) 的对比讨论或排除理由。Section 3.4 VTR 描述清晰。\n\n**Experiments** (experiments.tex): Table 2 数据缺失是核心问题。Section 4.2 的 four-model analysis 详尽但纯文本占据整页，建议提炼 inline summary。Section 4.4 CV sensitivity analysis 仅 3 个有效数据点，\"correlates\" 措辞过强。Section 4.5 VTR recovery 的 MLP adapter 结果应在 Introduction C3 中反映。Limitations 段落需大幅扩展。\n\n**Conclusion** (conclusion.tex): \"primary determinant\" 需改为 \"primary correlate\" 或 \"strongest observed factor\"。Future work 方向合理但缺少 sim-to-real transferability 讨论。\n\n**Appendix** (appendix.tex): 详尽且有价值。命名不一致 (Smart Compress vs VTR) 需全局修复。Pages 23-25 连续纯文本缺乏视觉锚点。Appendix G 脚注中的 batch size 差异信息应提升至主文。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "reviewer_ids_acknowledged": "[1, 2, 3]",
    "cross_response_reviewer_ids": "[1, 2, 3]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd",
    "report": "\n# Round 6 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others\n\n**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Fresh (重新审稿)\n\n---\n\n## Summary\n\n论文研究 vision token pruning 在不同 VLA 架构上的表现差异，提出 connector architecture 是 pruning robustness 的主要关联因素。核心发现：(1) pixel-shuffle connector (SmolVLA) 在仅移除 5% token 即崩溃至 0% SR，经双 checkpoint 验证；(2) token-entangling connectors 展现 task-complexity amplified collapse（X-VLA 在 Object 仅损失 1.4pp 但 Goal 损失 27.8pp）；(3) CV of L2 norms 作为 diagnostic 与 pruning tolerance 相关；(4) VTR (cross-attention re-encoding) 在 SmolVLA 上从 0% 恢复至 ~60% SR。实验覆盖 6 个 VLA 架构（450M-7B），4 个 LIBERO task suite，2 种 pruning 策略。\n\n---\n\n## Strengths\n\n**S1** [3/3 共识] **Pixel-shuffle 崩溃机制发现扎实且有价值。** SmolVLA 在 k=0.95（仅移除 6/128 tokens）即从 59.2% 崩溃至 0.0% SR，经 LoRA fine-tuned 和官方 checkpoint 双重验证，7 种 pruning 配置（ACIS/random/L2 × zero-mask/true removal/ToMe）均为 0%。这是从 pixel-shuffle 架构定义可演绎推导但首次被系统实证的结果，对 practitioners 有直接预警价值。(Section 4.3, Table 3/Appendix D)\n\n**S2** [3/3 共识] **实验设计系统性在 VLA pruning 文献中范围最广。** 6 个架构 × 3 种 connector family × 2 种 pruning 策略 × 6 个 retention ratio，附录详尽（27 页，含 per-task breakdown、multi-seed validation、hypergeometric model、attention entropy analysis）。Wilson 95% CI + 500 episodes/condition 是合理的统计实践。\n\n**S3** [3/3 共识] **写作清晰，结构合理。** Figure 1 teaser 有效传达 two-axis framework，Table 1 model properties 设计精简，Introduction 的 problem→gap→approach→contributions 流程逻辑严密。\n\n**S4** [2/3 共识] **Limitations 态度诚实。** 论文承认 simulation-only、causal isolation 不可能、CV data points 有限等核心局限（虽然主文过短，扩展讨论在 Appendix A）。\n\n**S5** **VTR 从 0% 恢复至 ~60% SR 是有价值的 proof-of-concept。** 在所有 hard pruning 方法均失败的条件下，22M 参数的 re-encoding 模块在 75% 压缩下恢复功能性能。MLP adapter 达到 comparable 性能 (p=0.15) 的发现本身也有价值——说明 re-encoding 而非特定架构是关键。\n\n---\n\n## Weaknesses (Must-Fix)\n\n**W-MF1** [3/3 全员共识] **CV diagnostic 证据严重不足——N=3-4 闭环模型无法建立可靠诊断工具。**\n- 论文声称 CV \"enables connector-appropriate compression strategy selection without downstream evaluation\" (Introduction C2, Section 3.3)\n- 实际闭环验证仅 4 个模型；method sensitivity 有效数据点仅 3 个（SmolVLA 全 0% 无法参与 method gap 比较）\n- Spearman rank correlation N=4 时最小可能 p≈0.083，**原则上无法达到 0.05 显著性**\n- 论文未报告任何正式相关性检验\n- **R1 量化**：4 个单调排列概率 ≤ 1/24 ≈ 4.2%，统计边缘\n- **严重性**：C2 是论文核心 contribution 之一，evidence base 不足直接削弱论文价值\n\n**W-MF2** [3/3 全员共识] **Table 2（核心结果表）数据大量缺失，削弱 cross-architecture, cross-suite analysis 的 claim。**\n- π₀.5 Goal: k=0.9 Random 和 k=0.7 L2 缺失\n- X-VLA Long: k=0.9/0.7/0.5 大部分缺失\n- X-VLA Spatial/Goal: 部分缺失\n- **OpenVLA 仅评估 Object 一个 suite**——论文中唯一的 high-CV independent-connector 模型在 task-complexity axis 上完全无验证\n- Abstract 声称 \"Evaluation spans six VLA architectures... and four LIBERO task suites\"，与实际数据矩阵填充率不足 70% 形成叙事落差\n- **严重性分歧**：R2/R3 列为 Must-Fix，R1 列为 Should-Fix（认为 SmolVLA 0% 是 finding 不是缺失）。Review Director 裁定 Must-Fix——对 empirical study 而言数据完整性是底线\n\n**W-MF3** [2/3 共识 + 1/3 间接支持] **因果叙事超出证据范围——\"primary determinant\" 在无 matched-backbone 控制下不可支撑。**\n- Conclusion: \"connector coupling is the primary determinant of pruning robustness\"\n- 6 个模型同时在 backbone (Qwen2/PaliGemma/Llama-2)、参数量 (450M-7B, 16×)、vision encoder (SigLIP variants/DINOv2)、token 数量 (50-768, 15×) 上不同\n- Appendix N 承认 \"preventing clean isolation of the connector effect from backbone differences\"\n- **Conclusion 与 Limitations 直接矛盾**（R3 叙事一致性检查确认）\n- Title \"Vision Connectors and VLA Token Compressibility\" 隐含因果方向\n\n**W-MF4** [2/3 共识] **缺少 attention-based pruning baseline——论文引用但不测试的标准方法。**\n- Attention-based scoring 是 VLA/VLM token pruning 最自然的竞争方法（FastV、VLA-Cache 采用）\n- Related Work 引用了 FastV 和 VLA-Cache，但实验不使用 attention-based scoring——叙事缺口\n- 如果 attention-based 在 entangling connectors 上也失败，会大幅加强论文核心 narrative\n- L2 norm 在 OpenVLA 上与 random 差距 <3pp (Appendix E.10)，说明 L2 并非总是有效的 importance score\n- Gradient-based importance 也完全缺失\n\n**W-MF5** [2/3 共识] **Generative AI 使用披露完全缺失——CoRL 2026 合规硬要求。**\n- CoRL 2026 Author Instructions 明确要求披露 AI 工具使用\n- 论文全文无任何相关声明\n- 可能触发 desk rejection 或 AC 质疑\n\n**W-MF6** [3/3 全员共识] **VTR 与 Smart Compress 命名不一致——核心贡献术语混乱。**\n- 主文 Section 3.4/4.5 使用 \"Vision Token Re-encoder (VTR)\"\n- Appendix E/F/G/H 大量使用 \"Smart Compress\"/\"Smart Compressor\"\n- 两个名字无任何词汇重叠，读者无法确定是否为同一组件\n- 损害核心贡献（C3）的可信度和可理解性\n\n---\n\n## Weaknesses (Should-Fix)\n\n**W-SF1** [3/3 全员共识] **VTR 贡献被 MLP adapter 控制实验严重削弱。**\n- MLP adapter 63.4±2.6% vs VTR 60.1±1.3% (p=0.15)，MLP 点估计更高\n- Introduction C3 以 VTR 为主角，但证据表明 cross-attention 非关键——任何 learned re-encoding 都能恢复 pixel-shuffle collapse\n- VTR ≈ Q-Former/BLIP-2 applied to VLA token compression，architecture novelty 有限\n- 建议：将 C3 reframe 为 \"learned re-encoding recovers pixel-shuffle VLAs\"\n\n**W-SF2** [3/3 全员共识] **LaTeX 渲染错误 `$\\pi_0.5$` 全文 50+ 处。**\n- 正确写法 `$\\pi_{0.5}$`，当前仅 \"0\" 下标，\".5\" 以正文字体显示\n- 反映稿件准备粗糙度\n\n**W-SF3** [2/3 共识] **Limitations section 过于简短——3 句话（~60 词），格式为 \\\\paragraph。**\n- CoRL 要求 \"describe limiting assumptions, failure modes, and other limitations\"\n- 遗漏关键局限：单一 benchmark (LIBERO only)、N=3 CV evidence base、pruning 方法范围有限（仅 L2+random）、VTR 单模型验证、主实验多为单 seed\n- Appendix A 有 extended discussion 但 reviewer 不要求读附录\n\n**W-SF4** [2/3 共识] **仅 LIBERO simulation 评估，无 real-robot 验证或 sim-to-real 讨论。**\n- CoRL CFP: \"prioritize real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots\"\n- Compressor-VLA (concurrent work) 已含 real-robot 验证\n- Conclusion 仅将 real-robot 列为 future work，无 transferability 论证\n\n**W-SF5** [2/3 共识] **Post-connector pruning 选择缺乏系统 justification。**\n- 未讨论 pre-connector pruning 可能性\n- Concurrent work (VLA-Cache, EfficientVLA) 在 KV-cache 或 pre-connector 操作\n- Pre-connector pruning 对 pixel-shuffle 可能不 catastrophic，论文核心发现可能限于 post-connector 这一特定设定\n\n**W-SF6** [2/3 共识] **跨条件使用不同 seed，Table 2 未标注。**\n- OpenVLA L2=seed42, random=seed7\n- Same-seed 控制仅在 Appendix 提供\n- Table 2 caption 无 seed 信息\n\n**W-SF7** [2/3 共识] **论文 identity 分裂——empirical study / diagnostic tool / method 三者各自不够深入。**\n- C1 empirical study 数据缺失 (Table 2)\n- C2 diagnostic tool N=3 不可靠\n- C3 method 被 MLP adapter 平替\n- \"三个 shallow contribution 拼凑\" 结构削弱整体力量\n\n**W-SF8** **No code/data release plan.** 对 empirical 论文的 reproducibility 有影响。建议添加 \"Code and data will be released upon acceptance\" 声明。\n\n---\n\n## Reviewer Consensus\n\n以下问题经交叉分享后达成共识：\n\n| 问题 | R1 | R2 | R3 | 共识 |\n|------|-----|-----|-----|------|\n| CV diagnostic N=3-4 不足 | Must-Fix (N1) | Must-Fix (N1) | AGREE | ★★★ |\n| Table 2 数据缺失 | Should-Fix (W4) | Must-Fix (N3) | Must-Fix (N3) | ★★★ |\n| VTR 被 MLP adapter 削弱 | Should-Fix (W1) | Should-Fix (W1) | AGREE | ★★★ |\n| VTR/Smart Compress 命名 | AGREE | AGREE | Must-Fix (N2) | ★★★ |\n| π₀.₅ LaTeX 错误 | AGREE | Minor (M4) | Should-Fix (W1) | ★★★ |\n| 因果叙事过强 | Must-Fix (N2) | indirect | AGREE | ★★☆ |\n| Simulation-only | — | Should-Fix (W4) | AGREE | ★★☆ |\n| Attention-based baseline 缺失 | Must-Fix (N3) | AGREE | nuance | ★★☆ |\n| Limitations 过短 | implied | AGREE | Should-Fix (W2) | ★★☆ |\n| AI disclosure 缺失 | AGREE | AGREE | Must-Fix (N1) | ★★☆ |\n\n## Reviewer Divergence\n\n| 分歧点 | 立场 | 裁定 |\n|--------|------|------|\n| Table 2 严重性 | R1: Should-Fix (SmolVLA 0% 是 finding); R2/R3: Must-Fix | **Must-Fix**——empirical study 数据完整性是底线 |\n| \"Don't Run with Scissors\" 差异化 | R1: REBUT (不同 domain); R2: Should-Fix | 记录为 info——建议加 1-2 句对比但非关键 |\n| Abstract 信息密度 | R3: Should-Fix (17 个数字); R2: partial REBUT (数字是卖点) | 折中——保留 4-5 个关键数字 |\n| Figure 3 可读性 | R3: Should-Fix; R1: REBUT (尚可) | 记录为 info |\n| VTR 训练 batch size | R1: Should-Fix (不公平); R2: partial REBUT (比较对象是 0% 不是 baseline) | Should-Fix——VTR 内部消融公平，但与 baseline 比较需 caveat |\n| CV vs 替代 metric | R1: Should-Fix (未比较); R2: REBUT (N=3 比较无意义) | 取决于是否增加模型数量 |\n\n---\n\n## Questions\n\n1. **[R1-Q1, R2-Q1]** π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0%，但 k=0.7 反弹至 77.2%。这是否为单 seed 随机波动？multi-seed 复现了吗？\n2. **[R2-Q2, 3/3 共识]** MLP adapter 达到 63.4% vs VTR 60.1% (p=0.15)。作者如何看待这一结果？C3 的 value proposition 是什么？\n3. **[R2-Q3]** CV diagnostic 的 practical workflow 是什么？decision threshold 如何确定？3 个数据点如何建立可操作的指导？\n4. **[R2-Q4]** 是否在 SmolVLA 上比较过 GLUESTICK (Don't Run with Scissors 的 training-free recovery) 和 VTR？\n5. **[R1-Q5]** 同一 LLM backbone 搭配不同 connector，CV-pruning tolerance 关系是否成立？\n6. **[R1-Q3]** SmolVLA k=0.99（仅移除 1 token）是否仍崩溃？是否测试了更精细的崩溃阈值？\n7. **[R1-Q5b]** Pruning 后保持原始 position ID（不 re-index）结果是否变化？\n\n---\n\n## Missing References\n\n以下引用已被 Reviewer 确认覆盖（16 个指定检查的 concurrent work 全部已引用）。建议补充：\n- A Survey on Efficient Vision-Language-Action Models (2025, arXiv:2510.24795)\n- ATP-LLaVA (Adaptive Token Pruning for Large Vision Language Models)\n\n---\n\n## External Review\n\n**状态**：未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2 warning, 8 info, 0 critical）\n\n**Warnings:**\n1. **Page 2**: Figure 1 子面板内 axis label 和 legend 字号偏小（估计 ~6-7pt），接近可读性下限。打印后可能低于 8pt 最低建议。\n2. **Pages 23-25**: 附录连续 3 页纯文本无 figure/table/equation，缺乏视觉锚点。\n\n**Info items:**\n- Page 6: 正文唯一纯文本整页（四模型逐一结果），建议考虑 inline summary table\n- Page 27: 末页内容约 50%，下半部空白\n- Page 7: Table 2 格式正确（最优加粗），但无次优下划线或方向标记\n- Page 16: Figure 5 axis label 字号偏小\n- Page 5: Figure 2 legend 含 CV 值，字号略小\n- Pages 12-15: 附录 per-task breakdown 4 页连续表格，caption 清晰自包含\n- Page 4: Table 1 booktabs 风格专业\n- Page 8: Figure 3 bar chart 简洁有效\n\n---\n\n## Overall Assessment\n\n**评分：Weak Reject (5/10)**\n**置信度：4/5（High）**\n**Reviewer 评分：R1=5/10, R2=5/10, R3=6/10**\n\n论文发现了一个有价值的现象（pixel-shuffle connector 在 5% pruning 即 catastrophic collapse，经双 checkpoint 验证），实验设计的系统性在 VLA pruning 文献中范围最广，写作清晰。但存在以下结构性问题阻碍接收：\n\n1. **核心 contribution (CV diagnostic) 的统计基础不足**：N=3-4 闭环模型，Spearman N=4 原则上无法达到显著性。论文将 \"preliminary observation\" 包装为 \"diagnostic tool\"，claim 强度与 evidence 不匹配。\n2. **数据完整性不足**：核心结果表 (Table 2) 约 20% 条目缺失，OpenVLA 仅评估一个 suite，与 \"cross-architecture, cross-suite analysis\" 的 claim 矛盾。\n3. **因果推断超出证据范围**：6 个模型在 connector 外的多个维度同时不同，无 matched-backbone 控制实验。\n4. **Pruning baseline 不完整**：仅用 L2 norm + random，未测试 attention-based scoring。\n5. **论文 identity 分裂**：empirical study / diagnostic / method 三者各自不够深入。\n\n**修改路径建议**（Review Director 裁定，非建议作者）：\n- **最小修改（deadline 前可行）**：AI disclosure、命名统一、LaTeX 修复、Limitations 扩展、因果语言降级、CV claim 降级、Abstract 精简——这些纯文字修改可在 6 天内完成\n- **实质性修改（可能需要更多时间）**：Table 2 补全（需要 GPU 资源和实验时间）、attention-based baseline（需要新实验）、更多 VLA 架构验证 CV diagnostic\n- **理想但可能超出 deadline**：real-robot validation、matched-backbone control experiment\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract** (abstract.tex): 信息密度过高（17 个数字），建议精简至 4-5 个核心数字。\"six VLA architectures\" 应明确 \"four in closed-loop, two via offline metrics\"。\n\n**Introduction** (introduction.tex): 论证逻辑清晰。C2 的 claim \"enabling connector-appropriate compression strategy selection without downstream evaluation\" 过强，应降级。C3 应 reframe 为 learned re-encoding 而非 VTR 本身。\n\n**Related Work** (related_work.tex): 覆盖范围合理（~46 citations），但对 \"Don't Run with Scissors\" 的差异化讨论不足（仅在 VLA-specific methods 列表中一笔带过）。建议增加 1-2 句显式对比。VTR 与 Q-Former/BLIP-2 的关系未讨论。\n\n**Method** (method.tex): Section 3.2 pruning protocol 清晰但缺少 post-connector 选择的 justification。Section 3.3 CV 引入缺少与替代 metric (entropy/kurtosis/Gini) 的对比讨论或排除理由。Section 3.4 VTR 描述清晰。\n\n**Experiments** (experiments.tex): Table 2 数据缺失是核心问题。Section 4.2 的 four-model analysis 详尽但纯文本占据整页，建议提炼 inline summary。Section 4.4 CV sensitivity analysis 仅 3 个有效数据点，\"correlates\" 措辞过强。Section 4.5 VTR recovery 的 MLP adapter 结果应在 Introduction C3 中反映。Limitations 段落需大幅扩展。\n\n**Conclusion** (conclusion.tex): \"primary determinant\" 需改为 \"primary correlate\" 或 \"strongest observed factor\"。Future work 方向合理但缺少 sim-to-real transferability 讨论。\n\n**Appendix** (appendix.tex): 详尽且有价值。命名不一致 (Smart Compress vs VTR) 需全局修复。Pages 23-25 连续纯文本缺乏视觉锚点。Appendix G 脚注中的 batch size 差异信息应提升至主文。\n"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-23T06:01:08.992776+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6ea0e93e255655758819bea2ab1f224d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4469
}
```

</details>

---


### Assistant

_source line 514 · 2026-05-23T06:01:20.139316+00:00_

审稿报告已投递至 Research Director。

**Round 6 审稿完成。**

总评 **Weak Reject (5/10)**，置信度 4/5。三位 Reviewer 评分：R1=5, R2=5, R3=6。

**核心问题（6 个 Must-Fix）：**
1. CV diagnostic 仅 N=3-4 闭环模型，统计上原则不可能达到显著性
2. Table 2 数据缺失 ~20%，OpenVLA 仅 Object suite
3. "primary determinant" 因果叙事无 matched-backbone 控制支撑
4. 缺 attention-based pruning baseline
5. Generative AI 披露缺失（CoRL 合规）
6. VTR/Smart Compress 命名不一致

**主要优势：** pixel-shuffle 崩溃机制发现扎实（双 checkpoint 验证）、实验系统性在 VLA pruning 文献中最广、写作清晰。

Issue Tracker 已同步更新至 `review_issues.yaml`（Round 6: 6 critical, 8 warning, 3 info 新增）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 515 · 2026-05-23T06:01:21.303889+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

总结：在 R1 的 9 个条目中，我 AGREE 了 7 个、REBUT 了 2 个（R1-W2 VTR batch size 公平性——部分反驳因 VTR 的比较对象是 0% 而非 baseline；R1-W6 替代 metric 比较——在 N=3 下无统计意义）。在 R3 的 8 个条目中，AGREE 了 7 个、REBUT 了 1 个（R3-W4 Abstract 信息密度——具体数字是 empirical 论文的卖点）。三位 reviewer 最强共识是 Table 2 数据缺失（3/3），其次是 CV diagnostic evidence 不足和 VTR 被 MLP adapter 平替（均 2/3）。

---

[Reviewer 3 审稿结果]:
交叉回应已提交。对 R1 的 3 条 Must-Fix 和 6 条 Should-Fix、R2 的 3 条 Must-Fix 和 5 条 Should-Fix 均逐条给出了 [AGREE] 或 [AGREE with nuance]，无 [REBUT]。三位 reviewer 在 Table 2 数据缺失、CV diagnostic 证据不足、VTR 被 MLP adapter 削弱三个问题上形成全员共识。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 516 · 2026-05-23T06:01:46.966220+00:00_

审稿流程已全部完成。

**Round 6 审稿总结：**
- 3 位 Reviewer 独立初审 → 交叉分享 → 逐条回应，1 轮即达成收敛
- **最终评分：Weak Reject (5/10)**，R1=5, R2=5, R3=6
- 审稿报告已投递至 Research Director
- Issue Tracker 已更新：6 critical / 8 warning / 3 info（新增），15 个历史 issue 维持 resolved

**全员共识问题（3/3）：**
1. CV diagnostic 证据不足（N=3-4，统计上原则不可能达到显著性）
2. Table 2 数据大量缺失（~20%，OpenVLA 仅 Object suite）
3. VTR 被 MLP adapter 控制实验削弱（p=0.15，cross-attention 非关键机制）
4. VTR/Smart Compress 命名不一致
5. π₀.₅ LaTeX 渲染错误（50+ 处）

**核心判断：** 论文有一个扎实的发现（pixel-shuffle catastrophic collapse），但将其包装为三个独立 contribution 导致每个都不够深入。CV diagnostic 的 claim 强度与 evidence 严重不匹配，Table 2 数据不完整与 "cross-architecture, cross-suite analysis" 的定位矛盾。修改路径分为文字修改（deadline 前可行）和实质性实验补充（需额外时间）两层。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 47

## Round 47

56 recorded events


### User

_source line 517 · 2026-05-29T00:37:47.818724+00:00_

[Round 7 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/importance_margin_vla_compress/artifacts/review_reports/round_6.md`
跨轮次问题追踪: `projects/importance_margin_vla_compress/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: importance_margin_vla_compress
- 论文路径: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex
- 目标 venue: CoRL 2026
- 截止日期: 2026-05-29
- **引用验证**: ❌ 未启用

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-29T00:37:59.394113+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-29T00:37:59.444840+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-29T00:38:05.011013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_reports/round_6.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_reports/round_6.md"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-29T00:38:05.011809+00:00_

1	---
2	round: 6
3	review_mode: fresh
4	overall_score: weak reject
5	timestamp: 2026-05-23T06:01:04.550275+00:00
6	reviewer_ids: [1, 2, 3]
7	cross_response_reviewer_ids: [1, 2, 3]
8	force_resubmit: False
9	---
10	
11	
12	# Round 6 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others
13	
14	**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Fresh (重新审稿)
15	
16	---
17	
18	## Summary
19	
20	论文研究 vision token pruning 在不同 VLA 架构上的表现差异，提出 connector architecture 是 pruning robustness 的主要关联因素。核心发现：(1) pixel-shuffle connector (SmolVLA) 在仅移除 5% token 即崩溃至 0% SR，经双 checkpoint 验证；(2) token-entangling connectors 展现 task-complexity amplified collapse（X-VLA 在 Object 仅损失 1.4pp 但 Goal 损失 27.8pp）；(3) CV of L2 norms 作为 diagnostic 与 pruning tolerance 相关；(4) VTR (cross-attention re-encoding) 在 SmolVLA 上从 0% 恢复至 ~60% SR。实验覆盖 6 个 VLA 架构（450M-7B），4 个 LIBERO task suite，2 种 pruning 策略。
21	
22	---
23	
24	## Strengths
25	
26	**S1** [3/3 共识] **Pixel-shuffle 崩溃机制发现扎实且有价值。** SmolVLA 在 k=0.95（仅移除 6/128 tokens）即从 59.2% 崩溃至 0.0% SR，经 LoRA fine-tuned 和官方 checkpoint 双重验证，7 种 pruning 配置（ACIS/random/L2 × zero-mask/true removal/ToMe）均为 0%。这是从 pixel-shuffle 架构定义可演绎推导但首次被系统实证的结果，对 practitioners 有直接预警价值。(Section 4.3, Table 3/Appendix D)
27	
28	**S2** [3/3 共识] **实验设计系统性在 VLA pruning 文献中范围最广。** 6 个架构 × 3 种 connector family × 2 种 pruning 策略 × 6 个 retention ratio，附录详尽（27 页，含 per-task breakdown、multi-seed validation、hypergeometric model、attention entropy analysis）。Wilson 95% CI + 500 episodes/condition 是合理的统计实践。
29	
30	**S3** [3/3 共识] **写作清晰，结构合理。** Figure 1 teaser 有效传达 two-axis framework，Table 1 model properties 设计精简，Introduction 的 problem→gap→approach→contributions 流程逻辑严密。
31	
32	**S4** [2/3 共识] **Limitations 态度诚实。** 论文承认 simulation-only、causal isolation 不可能、CV data points 有限等核心局限（虽然主文过短，扩展讨论在 Appendix A）。
33	
34	**S5** **VTR 从 0% 恢复至 ~60% SR 是有价值的 proof-of-concept。** 在所有 hard pruning 方法均失败的条件下，22M 参数的 re-encoding 模块在 75% 压缩下恢复功能性能。MLP adapter 达到 comparable 性能 (p=0.15) 的发现本身也有价值——说明 re-enc
…[truncated 10418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-29T00:38:06.016028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-29T00:38:06.066855+00:00_

1	
2	# ===== Round 4-5 Recurring Issues =====
3	
4	- id: "R4-C3"
5	  summary: "CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal"
6	  category: framing
7	  severity: critical
8	  status: in_progress
9	  first_raised_round: 4
10	  last_seen_round: 6
11	  mentions:
12	    - {round: 4, reviewers: "R1+R2 consensus", note: "3 data points = 3 connector clusters"}
13	    - {round: 5, reviewers: "R1+R2 consensus", note: "RESOLVED — CV reframed as correlational diagnostic"}
14	    - {round: 6, reviewers: "R1+R2+R3 consensus", note: "RECURRED as R6-C1. Writing fix insufficient."}
15	  action_items:
16	    - {round: 4, action: "Reframe CV as correlational diagnostic", assigned_to: "paper_agent", status: "done"}
17	    - {round: 6, action: "C2 → coarse indicator + 3-bucket classifier", assigned_to: "paper_agent", status: "done"}
18	    - {round: 6, action: "E3 cosine similarity mechanism explanation", assigned_to: "main_agent", status: "done"}
19	    - {round: 6, action: "Add more VLA models for CV N expansion", assigned_to: "main_agent", status: "in_progress"}
20	  resolution: ""
21	  resolution_round: null
22	
23	- id: "R4-C1"
24	  summary: "Causal claim under-identified"
25	  category: framing
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 4
29	  last_seen_round: 6
30	  mentions:
31	    - {round: 4, reviewers: "R1+R2", note: "determines needs downgrade"}
32	    - {round: 5, reviewers: "R1+R2", note: "RESOLVED"}
33	    - {round: 6, reviewers: "R1+R3+R2", note: "RECURRED: 'primary determinant' in Conclusion"}
34	  action_items:
35	    - {round: 4, action: "Full-text causal language downgrade", assigned_to: "paper_agent", status: "done"}
36	    - {round: 6, action: "'most consistent structural factor' + confounder caveat", assigned_to: "paper_agent", status: "done"}
37	  resolution: "Round 6 Reviewer verified: Conclusion uses 'most consistent structural factor' + Appendix confounders cross-ref. 12/12 PASS."
38	  resolution_round: 6
39	
40	
…[truncated 10232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-29T00:38:06.067275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-29T00:38:06.168089+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	\usepackage{wrapfig}
13	
14	% Tighten float spacing for page limit
15	\setlength{\textfloatsep}{6pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{6pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{3pt}
19	\setlength{\belowcaptionskip}{0pt}
20	\setlength{\abovedisplayskip}{6pt plus 2pt minus 4pt}
21	\setlength{\belowdisplayskip}{6pt plus 2pt minus 4pt}
22	
23	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	
30	\keywords{vision-language-action models, token pruning, robot learning}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{experiments}
39	
40	\input{conclusion}
41	
42	\input{limitations}
43	
44	\bibliography{references}
45	
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-29T00:38:29.664041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-29T00:38:30.116080+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across six VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. No scoring method is universally safe: task complexity amplifies connector-dependent patterns (up to $20{\times}$ from Object to Goal at $k{=}0.9$). A zero-mask ablation isolates the mechanism: zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion fails, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-29T00:38:30.166702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-29T00:38:30.618719+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to near-zero (${\leq}$6.6\%). Apply the same reduction to $\pi_{0.5}$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a ViT encoder feeding tokens through a connector into a language model backbone; the critical difference is the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and extends to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture, implicitly assuming pruning transfers across designs.
15	
16	Yet current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure.
17	
18	We present an empirical study of VLA 
…[truncated 1597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-29T00:38:30.669420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-29T00:38:31.121524+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using attention signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, and Compressor-VLA~\cite{gao2025compressorvla}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Vision connectors.}
11	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-29T00:38:31.121857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-29T00:38:31.473553+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). \textbf{Linear projection} applies a per-patch matrix multiplication ($\pi_{0}$~\cite{black2024pi0}, $\pi_{0.5}$~\cite{black2025pi05}; CV$\,{<}\,$0.06). \textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\cite{kim2024openvla}, OFT~\cite{kim2025openoft}; CV$\,{\approx}\,$0.22). \textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\cite{zheng2025xvla} uses a 12-layer BART encoder~\cite{lewis2020bart} (CV$\,{=}\,$0.151); SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 patches per token (CV$\,{=}\,$0.314). We classify coupling as \emph{independent} (one patch per output) or \emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
8	
9	\begin{figure*}[t]
10	\centering
11	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
12	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}
13	\label{fig:architecture}
14	\end{figure*}
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{VLA models evaluated. Coupling indicates independent vs.\ cross-token processing. $N$ = vision tokens input to the LLM. $^\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}
20	\label{tab:model_properties}
21	\begin{tabular}{lrlcrll}
22	\toprule
23	Model & Params & Connector & $N$ & CV & Coupling & Eval \\
24	\midrule
25	$\pi_{0.5}$ & 4B & Linear ($\times\!\sqrt{d}$) & 768 & 0.055 
…[truncated 5703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-29T00:38:37.729789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-29T00:38:38.081638+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
8	
9	\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.
10	
11	\paragraph{Protocol.} We prune at $k \in \{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\}$ and report mean SR over 500 episodes. Multi-seed results ($\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\pm$ s.d.\ with per-seed breakdowns in the appendix.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
19	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
20	\label{fig:pruning_overview}
21	\end{figure}
22	
23	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
24	
25	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. On Obje
…[truncated 7667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-29T00:38:38.082018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-29T00:38:38.232934+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector---L2 leads on $\pi_{0.5}$ Object but inverts on Long; on X-VLA, attention recovers near-baseline while L2 is anti-informative (Appendix~\ref{app:extended_discussion}). The V-shaped random recovery on $\pi_{0.5}$ Long reflects position encoding sensitivity: scattered gaps maximally disrupt RoPE at $k{\approx}0.9$, recovering as surviving positions become approximately uniform.
6	
7	Connector architecture is the primary factor governing VLA token compressibility. Token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity (up to $20{\times}$ from Object to Goal at $k{=}0.9$). CV partitions models in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and $k$-dependent. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression. Real-robot validation and adaptive per-task pruning schedules remain open.
8	
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-29T00:38:38.434125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-29T00:38:38.484938+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	All evaluations use LIBERO simulation; no sim-to-real evidence is provided; real-robot evaluation with domain shift would strengthen practical applicability. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing full causal isolation of the connector effect; controlled studies varying only the connector within a fixed backbone would sharpen causal claims. The CV--SR correlation relies on four closed-loop models, too few for a general law; expanding the model pool as new VLA architectures emerge will test whether CV generalizes as a universal diagnostic. VTR is validated on SmolVLA only; extending to other entangling connectors (e.g., cross-attention encoders) would test generality of the re-encoding approach. Only L2-norm and random scoring are systematically compared; gradient-based importance scoring or learned pruning masks could yield better token selection. Most conditions use a single seed; $\pi_{0.5}$ Long uses five-seed means ($n{=}5$, s.d.\ ${\leq}$2.7\,pp); future work should adopt multi-seed evaluation across all conditions to quantify variance. \textbf{AI disclosure:} This work used AI tools (Claude) for code development and manuscript drafting; all scientific claims are the authors' own.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-29T00:40:44.014206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-29T00:40:44.466272+00:00_

File content (27322 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-29T00:40:44.518442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-29T00:40:44.519203+00:00_

1	
2	# ===== Round 4-5 Recurring Issues =====
3	
4	- id: "R4-C3"
5	  summary: "CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal"
6	  category: framing
7	  severity: critical
8	  status: in_progress
9	  first_raised_round: 4
10	  last_seen_round: 6
11	  mentions:
12	    - {round: 4, reviewers: "R1+R2 consensus", note: "3 data points = 3 connector clusters"}
13	    - {round: 5, reviewers: "R1+R2 consensus", note: "RESOLVED — CV reframed as correlational diagnostic"}
14	    - {round: 6, reviewers: "R1+R2+R3 consensus", note: "RECURRED as R6-C1. Writing fix insufficient."}
15	  action_items:
16	    - {round: 4, action: "Reframe CV as correlational diagnostic", assigned_to: "paper_agent", status: "done"}
17	    - {round: 6, action: "C2 → coarse indicator + 3-bucket classifier", assigned_to: "paper_agent", status: "done"}
18	    - {round: 6, action: "E3 cosine similarity mechanism explanation", assigned_to: "main_agent", status: "done"}
19	    - {round: 6, action: "Add more VLA models for CV N expansion", assigned_to: "main_agent", status: "in_progress"}
20	  resolution: ""
21	  resolution_round: null
22	
23	- id: "R4-C1"
24	  summary: "Causal claim under-identified"
25	  category: framing
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 4
29	  last_seen_round: 6
30	  mentions:
31	    - {round: 4, reviewers: "R1+R2", note: "determines needs downgrade"}
32	    - {round: 5, reviewers: "R1+R2", note: "RESOLVED"}
33	    - {round: 6, reviewers: "R1+R3+R2", note: "RECURRED: 'primary determinant' in Conclusion"}
34	  action_items:
35	    - {round: 4, action: "Full-text causal language downgrade", assigned_to: "paper_agent", status: "done"}
36	    - {round: 6, action: "'most consistent structural factor' + confounder caveat", assigned_to: "paper_agent", status: "done"}
37	  resolution: "Round 6 Reviewer verified: Conclusion uses 'most consistent structural factor' + Appendix confounders cross-ref. 12/12 PASS."
38	  resolution_round: 6
39	
40	
…[truncated 10232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-29T00:40:48.636058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-29T00:40:48.686967+00:00_

1	\appendix
2	
3	\section{Full Pruning Results}
4	\label{app:full_results}
5	
6	Table~\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\ref{tab:main_results} for space.
7	
8	\begin{table*}[ht]
9	\centering
10	\footnotesize
11	\caption{Full closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
12	\label{tab:full_results}
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{llccccc}
15	\toprule
16	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
17	\midrule
18	\multirow{4}{*}{$\pi_{0.5}$}
19	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
20	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
21	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
22	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\
23	\midrule
24	\multirow{4}{*}{X-VLA}
25	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
26	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
27	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
28	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
29	\midrule
30	\multirow{4}{*}{OpenVLA}
31	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
32	& Goal    & \textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\texts
…[truncated 18866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-29T00:40:52.903284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-29T00:40:52.954122+00:00_

200	milk & 62 \\
201	orange\_juice & 38 \\
202	salad\_dressing & 50 \\
203	tomato\_sauce & 52 \\
204	\midrule
205	\textbf{Overall} & \textbf{44.8} \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	\subsection{Official SmolVLA Checkpoint Per-Task Results}
211	
212	Table~\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\_libero). Under 50\% random token removal, all tasks produce 0\% SR, identical to the fine-tuned checkpoint results.
213	
214	\begin{table}[ht]
215	\centering
216	\small
217	\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\%. Under 50\% random pruning, all tasks collapse to 0\%. An independent evaluation (protocol B) yields 57.2\% baseline with identical cliff-edge (Table~\ref{tab:smolvla_ablation}).}
218	\label{tab:smolvla_official_pertask}
219	\begin{tabular}{lcc}
220	\toprule
221	Task & Baseline SR (\%) & $k{=}0.5$ SR (\%) \\
222	\midrule
223	alphabet\_soup & 64 & 0 \\
224	bbq\_sauce & 38 & 0 \\
225	butter & 78 & 0 \\
226	chocolate\_pudding & 90 & 0 \\
227	cream\_cheese & 40 & 0 \\
228	ketchup & 60 & 0 \\
229	milk & 52 & 0 \\
230	orange\_juice & 80 & 0 \\
231	salad\_dressing & 44 & 0 \\
232	tomato\_sauce & 46 & 0 \\
233	\midrule
234	\textbf{Overall} & \textbf{59.2} & \textbf{0.0} \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
239	\subsection{OpenVLA Per-Task Results Under Pruning}
240	
241	\begin{table}[ht]
242	\centering
243	\small
244	\caption{OpenVLA per-task success rates (\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\%. Tasks requiring fine-grained discrimination (butter, cream\_cheese) degrade earliest; visually distinctive targets (orange\_juice, salad\_dressing) are most resilient.}
245	\label{tab:openvla_pertask}
246	\begin{tabular}{lccccc}
247	\toprule
248	Task
…[truncated 16654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-29T00:40:57.270756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "500",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "500",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-29T00:40:57.574627+00:00_

500	\toprule
501	$M$ & Seed 42 & Seed 43 & Seed 44 & Mean $\pm$ Std \\
502	\midrule
503	32 & 61.6 & 59.2 & 59.6 & 60.1 $\pm$ 1.3 \\
504	64 & 61.6 & 60.0 & 64.4 & 62.0 $\pm$ 2.3 \\
505	96 & 52.6 & 58.2 & 52.8 & 54.5 $\pm$ 3.2 \\
506	128 & 59.8 & 54.0 & 60.2 & 58.0 $\pm$ 3.5 \\
507	\bottomrule
508	\end{tabular}
509	\end{table}
510	
511	
512	\section{VTR Full Results}
513	\label{app:vtr_full}
514	
515	\begin{table}[ht]
516	\centering
517	\small
518	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (passthrough) within 1.1\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}
519	\label{tab:vtr_results}
520	\begin{tabular}{lccr}
521	\toprule
522	Configuration & $M$ & Compression & SR (\%) \\
523	\midrule
524	\textit{SmolVLA-Base (LoRA)} & 128 & 0\% & 44.8 \\
525	\textit{SmolVLA official} & 128 & 0\% & 59.2 \\
526	\textit{Baseline control (+100K steps)} & 128 & 0\% & 45.0 \\
527	\textit{Hard pruning (any $k$)} & -- & 5--50\% & 0.0 \\
528	\midrule
529	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
530	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
531	Cross-attn VTR & 64 & 50\% & \textbf{62.0 $\pm$ 2.2} \\
532	Cross-attn VTR & 96 & 25\% & 54.5 $\pm$ 3.2 \\
533	Cross-attn VTR & 128 & 0\% & 58.0 $\pm$ 3.5 \\
534	\midrule
535	MLP adapter ($\sim$22M) & 32 & 75\% & 63.4 $\pm$ 2.6 \\
536	\bottomrule
537	\end{tabular}
538	\end{table}
539	
540	
541	\section{Full VTR Ablation}
542	\label{app:smart_compress_full}
543	
544	Table~\ref{tab:smart_compress_full} reports all five VTR configurations. The cross-attention module improves performance regardless of compression: $M \in \{32, 64, 128\}$ all achieve $\sim$60\% SR, exceeding the 44.8\% baseline by 15--17 points ($p < 0.001$, two-proportion $z$-test). Only at $M = 16$ (87.5
…[truncated 25430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-29T00:41:02.496925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "800",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "800",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-29T00:41:02.551827+00:00_

800	OpenVLA main-text results use seed 42 for both L2 and random. Cross-seed (seed 7) random comparison in Table~\ref{tab:openvla_l2_vs_random} confirms the L2 advantage is seed-independent: the gap ranges from $+$0.8 to $+$8.6\,pp across retention ratios regardless of random seed.
801	
802	
803	\section{Token Position Analysis}
804	\label{app:token_position}
805	
806	To validate the spatial clustering hypothesis for L2 norm failure on low-CV models, we analyze the spatial distribution of tokens selected by L2 norm ranking on $\pi_{0.5}$ across three retention ratios.
807	
808	At $k{=}0.7$ (538 of 768 tokens retained): DBSCAN clustering identifies 2 spatial clusters, with 97\% of retained tokens in the largest cluster and 100\% spatial coverage of the original image grid. The broad coverage explains why L2 selection still achieves 55.0\% SR at this retention ratio.
809	
810	At $k{=}0.5$ (384 tokens retained): a single dominant cluster contains 100\% of retained tokens with only 78\% spatial coverage. The complete concentration into one spatial region confirms the clustering hypothesis: L2 norm ranking selects tokens from a contiguous high-norm region while abandoning 22\% of the spatial field. This is the retention ratio where L2 performance reaches its minimum (33.4\% SR, the V-shape valley).
811	
812	At $k{=}0.3$ (230 tokens retained): 3 clusters emerge, with 86\% in the largest and 78\% spatial coverage. The fragmentation into multiple clusters at extreme compression is consistent with the partial L2 recovery observed at this ratio ($53.2 \pm 3.1$\% SR): when the budget is very small, L2 selection is forced to sample from multiple spatial regions, partially restoring coverage.
813	
814	These results directly confirm that L2 norm ranking on low-CV models introduces spatial bias that degrades performance, and that the severity peaks at intermediate retention ratios where concentration is maximal.
815	
816	
817	\section{CV Scaling Law: Full Data}
818	\label{app:cv_s
…[truncated 11634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-29T00:41:32.403093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-29T00:41:32.905636+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector---L2 leads on $\pi_{0.5}$ Object but inverts on Long; on X-VLA, attention recovers near-baseline while L2 is anti-informative (Appendix~\ref{app:extended_discussion}). The V-shaped random recovery on $\pi_{0.5}$ Long reflects position encoding sensitivity: scattered gaps maximally disrupt RoPE at $k{\approx}0.9$, recovering as surviving positions become approximately uniform.
6	
7	Connector architecture is the primary factor governing VLA token compressibility. Token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity (up to $20{\times}$ from Object to Goal at $k{=}0.9$). CV partitions models in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and $k$-dependent. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression. Real-robot validation and adaptive per-task pruning schedules remain open.
8	
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-29T00:41:32.906044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-29T00:41:33.458461+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using attention signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, and Compressor-VLA~\cite{gao2025compressorvla}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Vision connectors.}
11	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-29T00:41:33.458832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-29T00:41:33.560316+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across six VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. No scoring method is universally safe: task complexity amplifies connector-dependent patterns (up to $20{\times}$ from Object to Goal at $k{=}0.9$). A zero-mask ablation isolates the mechanism: zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion fails, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-29T00:42:04.153342+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,dispatch_visual_check,get_external_review_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,dispatch_visual_check,get_external_review_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-29T00:42:04.254061+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-29T00:42:06.653324+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer dispatch_visual_check",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer dispatch_visual_check",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-29T00:42:06.653764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-29T00:42:09.957392+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "get_external_review_status get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "get_external_review_status get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-29T00:42:10.024841+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 67
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-29T00:42:14.352521+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
  }
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-29T00:42:14.827301+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 566 · 2026-05-29T00:42:52.745337+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 38392
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-29T00:42:52.745760+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 37918
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-29T00:42:53.298270+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 7 继续审稿 — Reviewer 1 任务\n\n**角色**：Issue 追踪审查 + 回归检测\n**Venue**：CoRL 2026（8 页正文限制，双盲，需 Limitations section + AI disclosure）\n\n你是 Round 7 继续审稿的 Reviewer 1。上一轮（Round 6）给出 Weak Reject 5/10。论文已根据 Round 6 意见修改。你的核心任务是**逐条验证 4 个 in_progress issue 是否已充分解决**，并检查已 resolved 的 issue 是否有回归。\n\n### 论文文件\n- LaTeX 源文件目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`\n- 主文件：`main.tex`（入口），各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `limitations.tex`, `appendix.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/submitted.pdf`\n\n### 4 个 In-Progress Issue（逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由）\n\n**R6-C1 / R4-C3: CV diagnostic N 扩展**（critical）\n- Round 6 共识：N=3-4 closed-loop 模型验证 CV 诊断不足，无法达到统计显著性\n- 已完成：CV reframed 为 coarse indicator + 3-bucket classifier；cosine similarity 机制解释\n- 待验证：是否新增了 VLA 模型（如 Octo, CogACT 等）的 CV 实验数据？\n- **关键检查**：Table 1 模型数量是否增加？CV spectrum 描述是否包含新数据点？附录是否有新增模型的 CV 值？\n\n**R6-C2: Table 2 数据完整性**（critical）\n- Round 6 共识：~20% 数据缺失 + OpenVLA 仅 Object\n- 已完成：E1（9 个 Table 2 gap 填充）\n- 待验证：主表是否还有 \"--\" 空缺？OpenVLA 是移至附录还是已补全多 suite 数据？附录 full_results 表的 \"--\" 数量？\n\n**R6-C4: Attention-based scoring baseline**（critical）\n- Round 6 共识：引用了 FastV/VLA-Cache 但未测试 attention scoring\n- 已完成：E5（X-VLA BART attention-based pruning 实验）\n- 待验证：attention 数据是否已整合进论文（主文/附录）？是否有 Table？是否覆盖多模型（X-VLA + π₀.5）？结果讨论是否充分？\n\n**R6-W5: OpenVLA multi-suite**（warning）\n- Round 6 共识：OpenVLA 仅 Object 数据，task-complexity axis 对 MLP connector 未验证\n- 待验证：OpenVLA 是否有 Spatial/Goal/Long 数据？数据在哪里展示（主表 vs 附录）？\n\n### 回归检查（已 resolved issue，抽查以下关键项）\n\n**R6-C3: Causal narrative overreach**\n- Round 6 修复声明：\"most consistent structural factor\" + confounder caveat\n- **⚠️ Director 发现**：Introduction 仍使用 \"primary determinant of pruning robustness\"，Abstract 使用 \"primary architectural factor\"，Conclusion 使用 \"primary factor\"。请核实全文中 \"primary determinant\" 是否已被替换，causal language 是否一致。\n\n**R6-C5: AI disclosure** — 验证 Limitations section 中是否有 AI 使用声明\n**R6-C6: VTR/Smart Compress naming** — Grep 确认 \"Smart Compress\" 是否已清零\n**R6-W2: LaTeX pi_0.5 rendering** — 抽查是否仍有未修复的 `pi_0.5`（应为 `\\pi_{0.5}`）\n**R6-W3: Limitations 长度** — 验证 Limitations section 是否独立、>=6 项、含 sim-to-real\n\n### 输出格式\n```\n## Issue 追踪审查\n\n### R6-C1: [RESOLVED / STILL_OPEN]\n理由：...\n\n### R6-C2: [RESOLVED / STILL_OPEN]\n理由：...\n\n### R6-C4: [RESOLVED / STILL_OPEN]\n理由：...\n\n### R6-W5: [RESOLVED / STILL_OPEN]\n理由：...\n\n## 回归检查\n- R6-C3: [PASS / REGRESSION] — ...\n- R6-C5: [PASS / REGRESSION] — ...\n- R6-C6: [PASS / REGRESSION] — ...\n- R6-W2: [PASS / REGRESSION] — ...\n- R6-W3: [PASS / REGRESSION] — ...\n\n## 新发现问题（如有）\n...\n\n## 评分建议\nRound 7 建议评分：X/10（基于修改充分程度）\n```",
  "reviewer_id": "1",
  "round_number": "7"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 7 继续审稿 — Reviewer 1 任务\n\n**角色**：Issue 追踪审查 + 回归检测\n**Venue**：CoRL 2026（8 页正文限制，双盲，需 Limitations section + AI disclosure）\n\n你是 Round 7 继续审稿的 Reviewer 1。上一轮（Round 6）给出 Weak Reject 5/10。论文已根据 Round 6 意见修改。你的核心任务是**逐条验证 4 个 in_progress issue 是否已充分解决**，并检查已 resolved 的 issue 是否有回归。\n\n### 论文文件\n- LaTeX 源文件目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`\n- 主文件：`main.tex`（入口），各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `limitations.tex`, `appendix.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/submitted.pdf`\n\n### 4 个 In-Progress Issue（逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由）\n\n**R6-C1 / R4-C3: CV diagnostic N 扩展**（critical）\n- Round 6 共识：N=3-4 closed-loop 模型验证 CV 诊断不足，无法达到统计显著性\n- 已完成：CV reframed 为 coarse indicator + 3-bucket classifier；cosine similarity 机制解释\n- 待验证：是否新增了 VLA 模型（如 Octo, CogACT 等）的 CV 实验数据？\n- **关键检查**：Table 1 模型数量是否增加？CV spectrum 描述是否包含新数据点？附录是否有新增模型的 CV 值？\n\n**R6-C2: Table 2 数据完整性**（critical）\n- Round 6 共识：~20% 数据缺失 + OpenVLA 仅 Object\n- 已完成：E1（9 个 Table 2 gap 填充）\n- 待验证：主表是否还有 \"--\" 空缺？OpenVLA 是移至附录还是已补全多 suite 数据？附录 full_results 表的 \"--\" 数量？\n\n**R6-C4: Attention-based scoring baseline**（critical）\n- Round 6 共识：引用了 FastV/VLA-Cache 但未测试 attention scoring\n- 已完成：E5（X-VLA BART attention-based pruning 实验）\n- 待验证：attention 数据是否已整合进论文（主文/附录）？是否有 Table？是否覆盖多模型（X-VLA + π₀.5）？结果讨论是否充分？\n\n**R6-W5: OpenVLA multi-suite**（warning）\n- Round 6 共识：OpenVLA 仅 Object 数据，task-complexity axis 对 MLP connector 未验证\n- 待验证：OpenVLA 是否有 Spatial/Goal/Long 数据？数据在哪里展示（主表 vs 附录）？\n\n### 回归检查（已 resolved issue，抽查以下关键项）\n\n**R6-C3: Causal narrative overreach**\n- Round 6 修复声明：\"most consistent structural factor\" + confounder caveat\n- **⚠️ Director 发现**：Introduction 仍使用 \"primary determinant of pruning robustness\"，Abstract 使用 \"primary architectural factor\"，Conclusion 使用 \"primary factor\"。请核实全文中 \"primary determinant\" 是否已被替换，causal language 是否一致。\n\n**R6-C5: AI disclosure** — 验证 Limitations section 中是否有 AI 使用声明\n**R6-C6: VTR/Smart Compress naming** — Grep 确认 \"Smart Compress\" 是否已清零\n**R6-W2: LaTeX pi_0.5 rendering** — 抽查是否仍有未修复的 `pi_0.5`（应为 `\\pi_{0.5}`）\n**R6-W3: Limitations 长度** — 验证 Limitations section 是否独立、>=6 项、含 sim-to-real\n\n### 输出格式\n```\n## Issue 追踪审查\n\n### R6-C1: [RESOLVED / STILL_OPEN]\n理由：...\n\n### R6-C2: [RESOLVED / STILL_OPEN]\n理由：...\n\n### R6-C4: [RESOLVED / STILL_OPEN]\n理由：...\n\n### R6-W5: [RESOLVED / STILL_OPEN]\n理由：...\n\n## 回归检查\n- R6-C3: [PASS / REGRESSION] — ...\n- R6-C5: [PASS / REGRESSION] — ...\n- R6-C6: [PASS / REGRESSION] — ...\n- R6-W2: [PASS / REGRESSION] — ...\n- R6-W3: [PASS / REGRESSION] — ...\n\n## 新发现问题（如有）\n...\n\n## 评分建议\nRound 7 建议评分：X/10（基于修改充分程度）\n```",
    "reviewer_id": "1",
    "round_number": "7"
  }
}
````

</details>

---


### Tool result

_source line 569 · 2026-05-29T00:43:21.746079+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28447
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-29T00:43:21.947832+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 7 继续审稿 — Reviewer 2 任务\n\n**角色**：新增内容质量 + 整体叙事连贯性审查\n**Venue**：CoRL 2026（8 页正文限制，双盲，需 Limitations section + AI disclosure）\n\n你是 Round 7 继续审稿的 Reviewer 2。上一轮（Round 6）给出 Weak Reject 5/10。论文已进行大幅修改，新增了多个实验和分析。你的核心任务是**评估新增内容的质量和论文整体连贯性**。\n\n### 论文文件\n- LaTeX 源文件目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`\n- 主文件：`main.tex`（入口），各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `limitations.tex`, `appendix.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/submitted.pdf`\n\n### 审查重点 1：新增实验内容质量\n\n**A. Zero-mask ablation（Section 4.3）**\n- 这是 Round 7 新增的核心贡献之一\n- 检查：实验设计是否 sound？\"89pp gap entirely attributable to position disruption\" 的声明是否 justified？是否有替代解释未讨论？仅在 π₀.5 Object 上验证是否够？\n\n**B. Attention-based scoring（Section 4.4 + Appendix）**\n- 检查：Table tab:attention_pruning 数据质量。X-VLA Goal 为何合并为单个值 \"98.2*\"？\n- 检查：π₀.5 attention 结果（tab:pi05_attention_crosssuite）是否讨论了 Object 上 attention 失败的机制？\n- 检查：\"architecture-dependent scoring\" 的结论是否有足够证据支撑？\n\n**C. Importance margin 分析**\n- 检查：Δ(k) 的 inverted-U 形状是否有 π₀.5 Long 以外的验证？\n- 检查：fig_cliff_highlight 和 fig_margin_profile 是否与文字描述一致？\n\n**D. π₀.5 Long multi-seed（n=5）**\n- 检查：5-seed 结果（Table tab:pi05_long_multiseed）s.d. 是否合理？是否所有 claim 都正确引用了 n=5？\n\n### 审查重点 2：叙事连贯性和 Contribution 清晰度\n\n**E. 三个 Contribution 的清晰度**\n- C1：六架构 compressibility 分析 → 是否清楚说明了什么新发现？\n- C2：CV 单次诊断 → 是否过度声明？\"validated on four closed-loop architectures\" 是否准确？\n- C3：Zero-mask + VTR → 两个不同的结果绑定在一个 contribution 是否合理？\n\n**F. 主表 vs 附录分配**\n- OpenVLA 移至附录是否合理？是否导致主文叙事不完整？\n- 主文 Table 2 只有 3 个模型（π₀.5, X-VLA, SmolVLA），是否足以支撑 \"six architectures\" 的声明？\n\n**G. 页数合规**\n- 检查 PDF 页数：正文是否 ≤ 8 页（不含 references 和 appendix）？\n- 检查正文密度：是否有挤压排版的痕迹（float spacing 调整、过小字号等）？\n\n**H. Abstract 质量**\n- Round 6 要求减少数字密度（从 17 个降到 ~5 个）。检查现版本数字数量和可读性。\n\n### 审查重点 3：写作质量\n\n- 全文扫描：是否有 AI 生成痕迹（过度结构化、\"delve into\"、\"it is worth noting\" 等短语）？\n- 术语一致性：VTR 命名是否全文一致？\"importance margin\" 是否有清晰定义后一致使用？\n- 图表引用完整性：所有 Figure/Table 是否在正文中被引用？\n\n### 输出格式\n```\n## 新增内容质量\n\n### A. Zero-mask ablation\n评价：...\n\n### B. Attention-based scoring\n评价：...\n\n### C. Importance margin\n评价：...\n\n### D. Multi-seed\n评价：...\n\n## 叙事连贯性\n\n### E. Contributions\n评价：...\n\n### F. 主表 vs 附录\n评价：...\n\n### G. 页数合规\n评价：...\n\n### H. Abstract\n评价：...\n\n## 写作质量\n评价：...\n\n## 新发现问题（Must-Fix / Should-Fix / Info）\n...\n\n## 评分建议\nRound 7 建议评分：X/10\n```",
  "reviewer_id": "2",
  "round_number": "7"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 7 继续审稿 — Reviewer 2 任务\n\n**角色**：新增内容质量 + 整体叙事连贯性审查\n**Venue**：CoRL 2026（8 页正文限制，双盲，需 Limitations section + AI disclosure）\n\n你是 Round 7 继续审稿的 Reviewer 2。上一轮（Round 6）给出 Weak Reject 5/10。论文已进行大幅修改，新增了多个实验和分析。你的核心任务是**评估新增内容的质量和论文整体连贯性**。\n\n### 论文文件\n- LaTeX 源文件目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`\n- 主文件：`main.tex`（入口），各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `limitations.tex`, `appendix.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/submitted.pdf`\n\n### 审查重点 1：新增实验内容质量\n\n**A. Zero-mask ablation（Section 4.3）**\n- 这是 Round 7 新增的核心贡献之一\n- 检查：实验设计是否 sound？\"89pp gap entirely attributable to position disruption\" 的声明是否 justified？是否有替代解释未讨论？仅在 π₀.5 Object 上验证是否够？\n\n**B. Attention-based scoring（Section 4.4 + Appendix）**\n- 检查：Table tab:attention_pruning 数据质量。X-VLA Goal 为何合并为单个值 \"98.2*\"？\n- 检查：π₀.5 attention 结果（tab:pi05_attention_crosssuite）是否讨论了 Object 上 attention 失败的机制？\n- 检查：\"architecture-dependent scoring\" 的结论是否有足够证据支撑？\n\n**C. Importance margin 分析**\n- 检查：Δ(k) 的 inverted-U 形状是否有 π₀.5 Long 以外的验证？\n- 检查：fig_cliff_highlight 和 fig_margin_profile 是否与文字描述一致？\n\n**D. π₀.5 Long multi-seed（n=5）**\n- 检查：5-seed 结果（Table tab:pi05_long_multiseed）s.d. 是否合理？是否所有 claim 都正确引用了 n=5？\n\n### 审查重点 2：叙事连贯性和 Contribution 清晰度\n\n**E. 三个 Contribution 的清晰度**\n- C1：六架构 compressibility 分析 → 是否清楚说明了什么新发现？\n- C2：CV 单次诊断 → 是否过度声明？\"validated on four closed-loop architectures\" 是否准确？\n- C3：Zero-mask + VTR → 两个不同的结果绑定在一个 contribution 是否合理？\n\n**F. 主表 vs 附录分配**\n- OpenVLA 移至附录是否合理？是否导致主文叙事不完整？\n- 主文 Table 2 只有 3 个模型（π₀.5, X-VLA, SmolVLA），是否足以支撑 \"six architectures\" 的声明？\n\n**G. 页数合规**\n- 检查 PDF 页数：正文是否 ≤ 8 页（不含 references 和 appendix）？\n- 检查正文密度：是否有挤压排版的痕迹（float spacing 调整、过小字号等）？\n\n**H. Abstract 质量**\n- Round 6 要求减少数字密度（从 17 个降到 ~5 个）。检查现版本数字数量和可读性。\n\n### 审查重点 3：写作质量\n\n- 全文扫描：是否有 AI 生成痕迹（过度结构化、\"delve into\"、\"it is worth noting\" 等短语）？\n- 术语一致性：VTR 命名是否全文一致？\"importance margin\" 是否有清晰定义后一致使用？\n- 图表引用完整性：所有 Figure/Table 是否在正文中被引用？\n\n### 输出格式\n```\n## 新增内容质量\n\n### A. Zero-mask ablation\n评价：...\n\n### B. Attention-based scoring\n评价：...\n\n### C. Importance margin\n评价：...\n\n### D. Multi-seed\n评价：...\n\n## 叙事连贯性\n\n### E. Contributions\n评价：...\n\n### F. 主表 vs 附录\n评价：...\n\n### G. 页数合规\n评价：...\n\n### H. Abstract\n评价：...\n\n## 写作质量\n评价：...\n\n## 新发现问题（Must-Fix / Should-Fix / Info）\n...\n\n## 评分建议\nRound 7 建议评分：X/10\n```",
    "reviewer_id": "2",
    "round_number": "7"
  }
}
````

</details>

---


### Tool result

_source line 571 · 2026-05-29T00:43:23.512430+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1564
}
```

</details>

---


### Assistant

_source line 572 · 2026-05-29T00:43:29.738531+00:00_

Round 7 继续审稿已启动：

- **视觉审查**：已派发，并行执行
- **外部审稿**：未请求（本轮为继续审稿，沿用上轮配置）
- **Reviewer 1**：Issue 追踪审查 + 回归检测（逐条验证 4 个 in_progress issue）
- **Reviewer 2**：新增内容质量 + 叙事连贯性审查（zero-mask / attention / importance margin / 页数合规）

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 573 · 2026-05-29T00:49:33.064050+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 7 Issue 追踪审查报告

### Issue 追踪

**R6-C1: [STILL_OPEN]** — CV diagnostic N 扩展未完成
Table 1 仍为 6 个模型（4 closed-loop + 2 offline），未新增任何 VLA 架构。method.tex 诚实地将措辞改为 "three closed-loop models"（排除 SmolVLA 的 0%），但核心证据基础未扩展。limitations.tex 承认 "too few for a general law" 是正确降级，但 abstract/intro 的 claim 语气未同步降级（见 R6-C3 回归）。考虑到修改周期客观限制，将严重程度从 critical 降级为 major weakness，前提是正文 claim 语气一致。

**R6-C2: [PARTIALLY_RESOLVED]** — Table 2 主表改善显著
主表 SmolVLA 从 "--" 改为实际数值（0.0/0.0, 6.6/4.2 等），主表无 "--"。OpenVLA 移至 Appendix Table 4 并新增 Goal/Spatial/Long 在 k=0.9 的完整数据。但 Table 4 仍有约 23/160 个 "--"（14%），集中在 OpenVLA k=0.95/0.7/0.5。降级为 minor。

**R6-C4: [RESOLVED]** — Attention baseline 已添加
覆盖 3 个 closed-loop 模型（X-VLA/π₀.5/OpenVLA）：(1) 主文 Section 4.5 报告 X-VLA attention 恢复 ≥92.8%、π₀.5 Object −30.4pp；(2) Table 4 含 OpenVLA 4 suite 的 attention† 数据；(3) 附录 Table 8 专用 X-VLA BART attention 表。结果实质性增强了论文——揭示 "no single scoring method is universally safe"。

**R6-W5: [RESOLVED]** — OpenVLA multi-suite 数据已添加
主文 Section 4.2 提及 OpenVLA Spatial/Goal 结果；Appendix Table 4 含 4 suite 完整 k=0.9 数据；新增 Figure 6 跨 4 suite scoring 比较图 + 详细讨论。

### 回归检查

**R6-C3: [REGRESSION]** — ⚠️ Causal language 未修正
Director 警告准确。Grep 确认：
- abstract.tex: "primary architectural factor"
- introduction.tex ×2: "primary determinant of pruning robustness"
- conclusion.tex: "primary factor governing"
- background.tex: "primary factor" (有 "We hypothesize" 限定)
Round 6 要求替换为 "most consistent structural factor" 但未执行。limitations.tex 说 "cannot be causally isolated" 与主文 "primary determinant" 自相矛盾。

**R6-C5: [PASS]** — AI disclosure: "This work used AI tools (Claude) for code development and manuscript drafting"
**R6-C6: [PASS]** — Smart Compress 仅存于 2 个 draft 文件，活跃文件统一 VTR
**R6-W2: [PASS]** — 活跃 tex 文件均用 `$\pi_{0.5}$`（correct braces），15 处 malformed 在废弃文件
**R6-W3: [PASS]** — Limitations 扩展至 6 项 + AI disclosure，覆盖 sim-to-real/causal isolation/N=4/VTR generalization/scoring methods/single-seed

### 新发现
- [minor] Abstract 用 π₀ (offline-only) 的 CV=0.038 作为 spectrum 下界，未标注 offline
- [minor] Table 4 OpenVLA Object k=0.95 缺 Random 数据，无法计算 method gap

### 评分建议
**Round 7: 6/10（Borderline Accept）**，从 Round 6 的 5/10 上调。
升分理由：attention baseline（C4 resolved）、OpenVLA multi-suite（W5 resolved）、Table 2 改善、Limitations 扩展。
阻碍因素：N=4 未扩展（C1 open）+ "primary determinant" 因果语言未替换（C3 regression）。
从 6→7 需要：(1) 全文统一非因果措辞；(2) 补充新模型或进一步降级 CV claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 574 · 2026-05-29T00:49:45.484163+00:00_

Reviewer 1 已提交。核心发现：R6-C4 和 R6-W5 已 RESOLVED，R6-C1 仍 STILL_OPEN，R6-C3 出现 REGRESSION（"primary determinant" 未替换）。评分 6/10。等待 Reviewer 2 提交后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 49

## Round 49

6 recorded events


### User

_source line 575 · 2026-05-29T00:49:48.633414+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 7 审稿报告

**角色**：新颖性 / 相关工作 / 论文定位（延续 Round 6 职责）+ 新增内容质量 + 叙事连贯性
**Round 6 评分**：5/10 (Weak Reject)

---

## 新增内容质量

### A. Zero-mask ablation（Section 4.3）

**评价：Strong addition。** 实验设计清晰地分离了两个因素：信息丢失 vs. 位置扰动。Zero-masking 将 10% token 的 embedding 置零（100% 信息损失，0% 位置变化）保留 98.0% SR；hard pruning 移除相同 token 并 re-index（部分信息损失 + 位置变化）崩溃到 9.0%。89pp 的差距归因于位置扰动而非信息丢失，这一结论在实验设计上是 justified 的——如果信息丢失是主因，zero-masking 应该比 hard pruning 更差（信息丢失更严重），但实际结果相反。

**局限性**：仅在 π₀.5 Object k=0.9 一个条件上验证。该发现与 RoPE positional encoding 高度相关（论文在 Appendix 中承认了这一点），因此可能不 generalize 到非 RoPE 架构（如 X-VLA 的 BART encoder 使用 learned positional embeddings）。Section 4.3 的声明 "entirely attributable to position disruption" 应加限定语 "on π₀.5"。不过作为 diagnostic finding 而非 general claim，在单个模型上的验证已足够。

### B. Attention-based scoring（Section 4.4 + Appendix）

**评价：Substantial improvement。** 这是 Round 6 R1-N3（缺少 attention baseline）的直接回应。

**X-VLA 结果（Table tab:attention_pruning）**：Attention scoring 在 k=0.5 恢复 ≥92.8% SR（所有 suite），而 L2 在所有 suite 上低于 random（-8.2 到 -27.2pp）。这个 double dissociation 是论文最强的新发现之一：L2 对 independent connectors 有效，attention 对 entangling connectors 有效，且两者不可互换。

**问题：X-VLA Goal 合并为 "98.2*"**：Table tab:attention_pruning 中 Goal 行将三种 attention variant 合并为单一数值 "98.2*"（标注 "Best of three attention variants"），而其他三个 suite 分别报告了三种 variant 的结果。这种不一致可能暗示：(a) 三种 variant 在 Goal 上差异极小不值得展开，或 (b) 某些 variant 在 Goal 上表现较差被隐藏。如果是 (a)，应标注 "all three variants ≥X%"；如果三种 variant 结果一致，应和其他行一样展开。当前处理方式有 cherry-picking 嫌疑（Should-Fix）。

**π₀.5 attention 结果（Table tab:pi05_attention_crosssuite）**：Attention 在 Object 上 catastrophic (-31.6pp vs random)，3/4 suite 中性。论文给出了机制解释（linear connector 的 attention score 范围极窄 [2×10⁻⁶, 3.6×10⁻³]，systematic position bias），但解释仅在附录中。主文 Section 4.4 对 π₀.5 attention 的讨论非常简略（"attention is catastrophically harmful on Object (−30.4pp)"），未解释为什么。

**"Architecture-dependent scoring" 结论**：Table tab:scoring_crossover_summary 的 double dissociation 提供了清晰证据。这个发现比 Round 6 论文提供的任何 contribution 都更有 insight。

### C. Importance margin 分析

**评价：Adequate。** Importance margin Δ(k) 的 inverted-U 形状在 π₀.5 Long 上有 n=5 seed 验证（Table tab:pi05_long_multiseed），峰值在 k=0.9 (+46.9pp)，k≈0.71 处 cross zero。Figure fig_margin_profile 与文字描述一致。

**局限**：inverted-U 仅在 π₀.5 Long 上有完整验证。Appendix 提到 OpenVLA 也有类似模式（L2 在 Object 上 leads at k=0.9 but staggered cliffs），但没有系统的 Δ(k) profile。π₀.5 Object 的 Δ(k) profile 也缺失（从 Table 数据可推断：k=0.95 Δ=+24.2, k=0.9 Δ=+89.2, k=0.5 Δ=−36.0，形状与 Long 类似但峰值更尖锐）。作为 observation 是 ok 的，但如果要作为 contribution 的一部分，需要更多 cross-model 验证。

### D. π₀.5 Long multi-seed（n=5）

**评价：Good。** Table tab:pi05_long_multiseed 的 s.d. 在 0.5–2.7pp 之间，对 500-episode 评估合理。关键 claims 正确标注了 n=5：
- 主文 Table 2 caption："π₀.5 Long: five-seed mean (n=5)" ✓
- 主文 Section 4.1 Protocol："Multi-seed results (π₀.5 Long: n=5; VTR: n=3)" ✓
- Figure 5 caption："n=5, mean ± s.d." ✓

Multi-seed validation 消除了 Round 6 中关于 π₀.5 Long random 非单调性是否为统计波动的质疑（Round 6 R2-Q1）。k=0.9 random 的 33.6±1.2% 和 k=0.7 的 64.6±1.8% 的非单调性在所有 5 个 seed 中一致复现，确认为 structural property。

---

## 叙事连贯性

### E. Contributions 清晰度

**C1**："A compressibility analysis across six VLA architectures..."
- 仍使用 "identifying connector architecture as the primary determinant"——这是 Round 6 R1-N2 指出的因果语言问题，Round 7 Limitations 虽然承认了 confounders 但 C1 的措辞没有软化。建议改为 "associated with" 或 "the strongest predictor of"。
- "six architectures" 准确但有误导：只有 4 个 closed-loop，2 个仅 offline。

**C2**："CV of token L2 norms as a single-pass diagnostic... validated on four closed-loop architectures"
- 相比 Round 6 的 "enabling connector-appropriate compression strategy selection without downstream evaluation"，claim 大幅收窄。这是正确方向。
- "validated on four" 诚实但也暴露了 sample size 仍然有限。

**C3** 将 zero-mask 发现和 VTR 绑在一起：
- 逻辑连接是："pruning 失败有两种机制——position disruption (π₀.5) 和 spatial entanglement (SmolVLA)——C3 分别提供了诊断 (zero-mask) 和修复 (VTR)"
- 作为叙事是连贯的，但作为 contribution 有点 overloaded。Zero-mask 发现足以独立成 contribution。

### F. 主表 vs 附录分配

**问题：OpenVLA 移至附录造成主文叙事断裂。**

Table 2（主文）仅包含 π₀.5, X-VLA, SmolVLA 三个模型。OpenVLA 是唯一的 high-CV independent connector 模型（CV=0.215），对验证 "CV predicts compressibility" 的连续谱至关重要。将其移至附录意味着：
- 主文中 CV 连续谱 (0.055 → 0.151 → 0.314) 缺少 0.215 的 calibration 点
- Section 4.2 对 OpenVLA 的讨论只有一句话，读者无法从主文判断 MLP connector 的行为
- 论文声称 "six architectures" 但主表仅 3 个模型（50% 模型在附录中）

建议：至少在 Table 2 中加入 OpenVLA Object 行（一行数据不影响页数）。

### G. 页数合规

**合规。** 正文 8 页（p1-p8），References 从 p9 开始，Appendix 从 p10 开始。正文包含 Limitations section（Section 6，含 AI disclosure）。

排版检查：
- 无明显字号压缩
- Float spacing 正常
- Table/Figure 大小合理
- \begin{itemize}[nosep] 用于 contributions list 是标准做法

### H. Abstract 质量

**仍然 number-dense。** 我数了约 16 个不同的数值（k=0.95, 98%, 0%, 0.038, 0.314, 450M-7B, 6/128, 93pp, 5%, 98%, 36pp, 20×, 10%, 98.0%, 9.0%, 89pp, ~5%, >60%, 75%）。Round 6 R3-W4 要求从 ~17 个减少到 ~5 个，当前版本几乎未减少。

正面变化：Abstract 新增了 zero-mask 发现的描述（"zeroing 10% of tokens preserves 98.0% SR while physical removal collapses to 9.0%"），和 scoring reversal（"random outperforms L2 by up to 36pp"），这些是有价值的新信息。但整体信息密度仍然过高。

---

## 写作质量

**术语一致性**：
- "VTR" 在正文和附录中一致使用 ✓（Round 6 R3-N2 已修复）
- "importance margin" 在 Section 3.2 有清晰定义（Δ(k) = SR_L2(k) − SR_Random(k)），后续使用一致 ✓
- $\pi_{0.5}$ 渲染已修复（不再是 $\pi_0.5$）✓（Round 6 R3-W1 已修复）

**AI 痕迹**：未发现典型 AI 生成短语（"delve into", "it is worth noting", "in conclusion"）。写作风格紧凑、技术化。

**图表引用完整性**：所有 main text Figure (1, 2, 3, 4, 5) 和 Table (1, 2, 3) 均在正文中引用 ✓

**代码/数据发布**：未提及代码发布计划（Round 6 R3-W3 未解决）。

---

## 新发现问题

### Must-Fix

**N1** [critical] **7+ concurrent works 从引用中被删除——相关工作覆盖严重退化**

- 具体位置：Section 2 (Related Work), references.bib
- 问题：Round 6 论文引用了所有 16 个 Director 指定的 concurrent work。Round 7 中以下引用被完全移除（.bib 中存在但正文无 \cite{}）：
  - **"Don't Run with Scissors" (Jabbour et al. 2025)** — 这是最关键的 concurrent work，也发现 pruning breaks VLA 并提出 recovery method。我在 Round 6 R2-W2 中明确要求**增加**讨论，而非删除引用。
  - **SpecPrune-VLA** — 2025 VLA pruning 方法
  - **"See What Matters" (ICML 2026)** — ICML 2026 VLA pruning concurrent work
  - **SparseVLM, SparseVILA** — VLM token sparsification
  - **FitPrune, CrossGET** — VLM/ViT token pruning
- 为什么影响接收：删除 7+ concurrent work 的引用在 blind review 中是危险操作。如果有 reviewer 了解这些工作（尤其是 "Don't Run with Scissors"），论文会被视为故意回避比较。CoRL reviewers 期望 thorough related work coverage。
- 建议：立即恢复所有被删除的引用。"Don't Run with Scissors" 需要专门段落对比差异。

### Should-Fix

**W1** [warning] **X-VLA Goal attention 结果在 Table tab:attention_pruning 中合并为 "98.2*"**
- Table 中 Object/Spatial/Long 都分别列出了 attn_last/attn_mean/attn_rollout，但 Goal 合并为单一值 "98.2*" (best of three variants)。
- 这种不一致暗示数据选择性报告。应展开为三列或标注 "all three ≥X%"。

**W2** [warning] **C1 仍使用因果语言 "primary determinant"**
- Introduction line 18 和 Conclusion 都写 "identifying the vision-language connector as the primary determinant of pruning robustness"
- Round 6 R1-N2 已指出无法做因果推断（confounders）。Round 7 Limitations 承认了这一问题但 C1 措辞未修改。
- 建议："the strongest predictor of" 或 "the primary architectural factor associated with"

**W3** [warning] **OpenVLA 附录 full results 仍有大量 "--" 缺失数据**
- Appendix Table tab:full_results 中 OpenVLA 的 Goal/Spatial/Long 在 k=0.95, 0.7, 0.5 均为 "--"。仅有 k=0.9 的数据（含 attention）。
- 主文 Table 2 现已完整（GOOD），但 Appendix 承诺 "Full results including OpenVLA" 却数据不全。
- 建议：要么补全，要么将 table caption 改为 "available results" 而非 "full results"。

**W4** [warning] **Appendix full_results table 中 X-VLA 仍有 "--"**
- X-VLA k=0.7 Spatial 和 Long 仍为 "--"。主文 Table 2 省略了 k=0.7（只报告 k=0.95, 0.9, 0.5），但 Appendix 表格标题暗示 "complete" results。

### Info

**I1** Zero-mask ablation 的声明 "entirely attributable to position disruption" 应限定为 "on π₀.5"，因为机制与 RoPE 高度相关，不一定 generalize 到所有 VLA 架构。

**I2** Abstract 数字密度仍高（~16 个数值），Round 6 R3-W4 未充分回应。

**I3** 代码/数据发布计划仍缺失（Round 6 R3-W3 未回应）。

---

## Round 6 问题修复状态

| Round 6 问题 | 状态 | 说明 |
|---|---|---|
| R2-N1: CV diagnostic N=3 数据点 | ⚠️ 部分改善 | Claim 收窄为 "validated on four"，但 sample size 未增加 |
| R2-N2: 论文 identity 分裂 | ✅ 改善 | Zero-mask + attention scoring 使三个 contribution 各有实质内容 |
| R2-N3: Table 2 数据缺失 | ✅ 修复 | 主文 Table 2 现已完整 |
| R2-W1: VTR 被 MLP 平替 | ⚠️ 未变 | p=0.15 事实不变，但论文现在诚实表述为 "re-encoding, not cross-attention" |
| R2-W2: "Don't Run with Scissors" 讨论不足 | ❌ 退化 | 引用被完全删除！ |
| R2-W3: Two-axis framework 可能是 re-packaging | ⚠️ 部分改善 | 新增 attention scoring + zero-mask 使分析更有深度 |
| R2-W4: 仅 LIBERO simulation | ⚠️ 未变 | Limitations 承认但无行动 |
| R2-W5: OpenVLA 仅 Object suite | ✅ 改善 | OpenVLA 现有全 4 suite 数据（Appendix Table tab:full_results k=0.9） |
| R3-N1: AI disclosure | ✅ 修复 | Limitations 末尾包含 AI disclosure |
| R3-N2: VTR/Smart Compress 命名 | ✅ 修复 | 全文统一为 VTR |
| R3-W1: π₀.5 渲染错误 | ✅ 修复 | 现为 $\pi_{0.5}$ |
| R3-W2: Limitations 过短 | ✅ 修复 | 现为 7 句话 + AI disclosure + extended discussion in Appendix |
| R3-W3: 代码发布计划 | ❌ 未回应 | |
| R3-W4: Abstract 数字密度 | ⚠️ 微改 | 新增内容使 Abstract 更丰富但数字未减少 |

---

## 主要优势（Round 7 新增或增强）

- **S1-NEW**: Zero-mask ablation 提供了 position disruption vs. information loss 的清晰分离，是论文最 elegant 的实验设计。
- **S2-NEW**: Attention scoring double dissociation（Table tab:scoring_crossover_summary）是论文最有 insight 的发现：connector type 决定了哪种 scoring method 有效，没有 universal winner。
- **S3-IMPROVED**: Table 2 主文现已完整，不再有 "--" 缺失数据。
- **S4-IMPROVED**: Multi-seed validation (n=5) 消除了关键数据点的统计疑虑。
- **S5-IMPROVED**: Limitations section 诚实且全面，CV diagnostic claim 适当收窄。
- **S6-IMPROVED**: 论文 identity 更清晰——empirical study 定位明确，不再过度 claim methodological contribution。

---

## 评分建议

**Round 7 建议评分：6/10（Borderline Accept）**

**从 5/10 → 6/10 的理由**：
- Zero-mask ablation 和 attention scoring double dissociation 是两个 genuine insights，使论文从 "观察到 connector 影响 pruning" 提升为 "理解了 why 和 how"
- Table 2 完整化和 multi-seed validation 大幅提高了实验可信度
- Limitations section 和 CV claim 的收窄表明了学术诚实

**未达 7/10 的理由**：
- 7+ concurrent works 被删除是 unacceptable regression——必须在提交前修复
- 仍然 simulation-only，对 CoRL community 的 practical impact 有限
- CV diagnostic 仍然只有 4 个 closed-loop 模型的 validation
- VTR 仍然只在 SmolVLA 上验证，MLP adapter 平替问题未解决
- OpenVLA 移至附录使主文叙事不完整


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-29T00:50:35.950965+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 7 交叉分享 — Reviewer 1 请回应 Reviewer 2 的发现\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应关键发现，标注 [AGREE] 或 [REBUT] + 理由。\n\n---\n\n### Reviewer 2 核心发现\n\n**[N1 — CRITICAL] 7+ concurrent works 引用被删除**\nReviewer 2 发现 Round 7 版本中以下引用被从正文中完全移除（.bib 存在但无 \\cite{}）：\n- \"Don't Run with Scissors\" (Jabbour et al. 2025)\n- SpecPrune-VLA, \"See What Matters\" (ICML 2026), SparseVLM, SparseVILA, FitPrune, CrossGET\nReviewer 2 认为这在 blind review 中极其危险，尤其 \"Don't Run with Scissors\" 是最接近的 concurrent work。\n\n**请验证**：检查 references.bib 和正文中的 \\cite{} 命令，确认这些引用是否确实被移除。Round 6 论文是否引用了这些工作？\n\n**[W1] X-VLA Goal attention 结果 \"98.2*\" 合并问题**\nTable tab:attention_pruning 中 Goal 行将三种 attention variant 合并为 \"98.2*\"（best of three），而其他行展开。Reviewer 2 认为有 cherry-picking 嫌疑。你同意吗？\n\n**[W2] 因果语言 — 与你的 R6-C3 REGRESSION 发现一致**\n你已独立发现。是否有补充？\n\n**[Zero-mask ablation 质量]**\nReviewer 2 认为实验设计 sound 但声明应限定为 \"on π₀.5\"。你是否同意？\n\n**[Abstract 数字密度]**\nReviewer 2 数了 ~16 个数值，认为 Round 6 R3-W4 未充分回应。你的看法？\n\n**[OpenVLA 移至附录]**\nReviewer 2 认为 OpenVLA 是 CV spectrum 中 0.215 的 calibration 点，移至附录造成主文叙事断裂。你同意吗？\n\n### 输出格式\n```\n## 交叉回应\n\n### N1 (concurrent works 删除): [AGREE / REBUT]\n理由 + 验证结果：...\n\n### W1 (Goal attention 合并): [AGREE / REBUT]\n理由：...\n\n### W2 (因果语言): [AGREE / REBUT]\n理由：...\n\n### Zero-mask 限定: [AGREE / REBUT]\n理由：...\n\n### Abstract 数字密度: [AGREE / REBUT]\n理由：...\n\n### OpenVLA 附录: [AGREE / REBUT]\n理由：...\n\n### 是否调整评分？\n原评分：6/10\n调整后：X/10\n理由：...\n```",
  "reviewer_id": "1",
  "round_number": "7"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 7 交叉分享 — Reviewer 1 请回应 Reviewer 2 的发现\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应关键发现，标注 [AGREE] 或 [REBUT] + 理由。\n\n---\n\n### Reviewer 2 核心发现\n\n**[N1 — CRITICAL] 7+ concurrent works 引用被删除**\nReviewer 2 发现 Round 7 版本中以下引用被从正文中完全移除（.bib 存在但无 \\cite{}）：\n- \"Don't Run with Scissors\" (Jabbour et al. 2025)\n- SpecPrune-VLA, \"See What Matters\" (ICML 2026), SparseVLM, SparseVILA, FitPrune, CrossGET\nReviewer 2 认为这在 blind review 中极其危险，尤其 \"Don't Run with Scissors\" 是最接近的 concurrent work。\n\n**请验证**：检查 references.bib 和正文中的 \\cite{} 命令，确认这些引用是否确实被移除。Round 6 论文是否引用了这些工作？\n\n**[W1] X-VLA Goal attention 结果 \"98.2*\" 合并问题**\nTable tab:attention_pruning 中 Goal 行将三种 attention variant 合并为 \"98.2*\"（best of three），而其他行展开。Reviewer 2 认为有 cherry-picking 嫌疑。你同意吗？\n\n**[W2] 因果语言 — 与你的 R6-C3 REGRESSION 发现一致**\n你已独立发现。是否有补充？\n\n**[Zero-mask ablation 质量]**\nReviewer 2 认为实验设计 sound 但声明应限定为 \"on π₀.5\"。你是否同意？\n\n**[Abstract 数字密度]**\nReviewer 2 数了 ~16 个数值，认为 Round 6 R3-W4 未充分回应。你的看法？\n\n**[OpenVLA 移至附录]**\nReviewer 2 认为 OpenVLA 是 CV spectrum 中 0.215 的 calibration 点，移至附录造成主文叙事断裂。你同意吗？\n\n### 输出格式\n```\n## 交叉回应\n\n### N1 (concurrent works 删除): [AGREE / REBUT]\n理由 + 验证结果：...\n\n### W1 (Goal attention 合并): [AGREE / REBUT]\n理由：...\n\n### W2 (因果语言): [AGREE / REBUT]\n理由：...\n\n### Zero-mask 限定: [AGREE / REBUT]\n理由：...\n\n### Abstract 数字密度: [AGREE / REBUT]\n理由：...\n\n### OpenVLA 附录: [AGREE / REBUT]\n理由：...\n\n### 是否调整评分？\n原评分：6/10\n调整后：X/10\n理由：...\n```",
    "reviewer_id": "1",
    "round_number": "7"
  }
}
````

</details>

---


### Tool result

_source line 577 · 2026-05-29T00:50:56.195173+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20244
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-29T00:50:56.499664+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 7 交叉分享 — Reviewer 2 请回应 Reviewer 1 的发现\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应关键发现，标注 [AGREE] 或 [REBUT] + 理由。\n\n---\n\n### Reviewer 1 核心发现\n\n**R6-C1: [STILL_OPEN] — CV diagnostic N 扩展未完成**\nTable 1 仍为 6 个模型（4 closed-loop + 2 offline），未新增任何 VLA 架构。Reviewer 1 将严重程度从 critical 降级为 major weakness，因为措辞已收窄（\"validated on four closed-loop architectures\"）且 Limitations 承认了局限。\n你是否同意降级？还是认为应保持 critical？\n\n**R6-C2: [PARTIALLY_RESOLVED] — Table 2 主表改善，附录仍有 ~14% \"--\"**\n主表 3 个模型完整无 \"--\"。Appendix Table 4 仍有约 23/160 个 \"--\"（集中在 OpenVLA k=0.95/0.7/0.5）。Reviewer 1 将此降级为 minor。\n你是否同意？你的 W3/W4 发现与此相关——附录 caption 说 \"Full results\" 但数据不全。\n\n**R6-C4: [RESOLVED] — Attention baseline 已添加**\n覆盖 3 个 closed-loop 模型（X-VLA/π₀.5/OpenVLA），主文 Section 4.5 + 附录 Table 8。\n你同意 RESOLVED 吗？\n\n**R6-W5: [RESOLVED] — OpenVLA multi-suite 数据已添加**\nAppendix Table 4 含 4 suite 完整 k=0.9 数据 + Figure 6 跨 suite 比较图。\n你同意 RESOLVED 吗？\n\n**R6-C3: [REGRESSION] — 因果语言未修正**\n- abstract.tex: \"primary architectural factor\"\n- introduction.tex ×2: \"primary determinant of pruning robustness\"\n- conclusion.tex: \"primary factor governing\"\n你已独立发现（W2）。是否有补充意见？\n\n**[SmolVLA k=0.95 残余值]**\nReviewer 1 未专门提及，但 Table 2 SmolVLA k=0.95 现在显示 Spatial 6.6/4.2, Goal 3.4/4.2（非全 0.0%）。你认为这些非零残余值是改善还是可能的实验噪声？\n\n**[新增 minor: Abstract 使用 π₀ (offline-only) 的 CV=0.038 作为 spectrum 下界]**\nReviewer 1 指出 Abstract 未标注 π₀ 是 offline-only 模型。你同意这是问题吗？\n\n### 输出格式\n```\n## 交叉回应\n\n### R6-C1 降级为 major: [AGREE / REBUT]\n理由：...\n\n### R6-C2 降级为 minor: [AGREE / REBUT]\n理由：...\n\n### R6-C4 RESOLVED: [AGREE / REBUT]\n理由：...\n\n### R6-W5 RESOLVED: [AGREE / REBUT]\n理由：...\n\n### R6-C3 REGRESSION: [AGREE / REBUT]\n理由：...\n\n### SmolVLA 残余值: 评价\n...\n\n### π₀ offline 标注: [AGREE / REBUT]\n理由：...\n\n### 是否调整评分？\n原评分：6/10\n调整后：X/10\n理由：...\n```",
  "reviewer_id": "2",
  "round_number": "7"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 7 交叉分享 — Reviewer 2 请回应 Reviewer 1 的发现\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应关键发现，标注 [AGREE] 或 [REBUT] + 理由。\n\n---\n\n### Reviewer 1 核心发现\n\n**R6-C1: [STILL_OPEN] — CV diagnostic N 扩展未完成**\nTable 1 仍为 6 个模型（4 closed-loop + 2 offline），未新增任何 VLA 架构。Reviewer 1 将严重程度从 critical 降级为 major weakness，因为措辞已收窄（\"validated on four closed-loop architectures\"）且 Limitations 承认了局限。\n你是否同意降级？还是认为应保持 critical？\n\n**R6-C2: [PARTIALLY_RESOLVED] — Table 2 主表改善，附录仍有 ~14% \"--\"**\n主表 3 个模型完整无 \"--\"。Appendix Table 4 仍有约 23/160 个 \"--\"（集中在 OpenVLA k=0.95/0.7/0.5）。Reviewer 1 将此降级为 minor。\n你是否同意？你的 W3/W4 发现与此相关——附录 caption 说 \"Full results\" 但数据不全。\n\n**R6-C4: [RESOLVED] — Attention baseline 已添加**\n覆盖 3 个 closed-loop 模型（X-VLA/π₀.5/OpenVLA），主文 Section 4.5 + 附录 Table 8。\n你同意 RESOLVED 吗？\n\n**R6-W5: [RESOLVED] — OpenVLA multi-suite 数据已添加**\nAppendix Table 4 含 4 suite 完整 k=0.9 数据 + Figure 6 跨 suite 比较图。\n你同意 RESOLVED 吗？\n\n**R6-C3: [REGRESSION] — 因果语言未修正**\n- abstract.tex: \"primary architectural factor\"\n- introduction.tex ×2: \"primary determinant of pruning robustness\"\n- conclusion.tex: \"primary factor governing\"\n你已独立发现（W2）。是否有补充意见？\n\n**[SmolVLA k=0.95 残余值]**\nReviewer 1 未专门提及，但 Table 2 SmolVLA k=0.95 现在显示 Spatial 6.6/4.2, Goal 3.4/4.2（非全 0.0%）。你认为这些非零残余值是改善还是可能的实验噪声？\n\n**[新增 minor: Abstract 使用 π₀ (offline-only) 的 CV=0.038 作为 spectrum 下界]**\nReviewer 1 指出 Abstract 未标注 π₀ 是 offline-only 模型。你同意这是问题吗？\n\n### 输出格式\n```\n## 交叉回应\n\n### R6-C1 降级为 major: [AGREE / REBUT]\n理由：...\n\n### R6-C2 降级为 minor: [AGREE / REBUT]\n理由：...\n\n### R6-C4 RESOLVED: [AGREE / REBUT]\n理由：...\n\n### R6-W5 RESOLVED: [AGREE / REBUT]\n理由：...\n\n### R6-C3 REGRESSION: [AGREE / REBUT]\n理由：...\n\n### SmolVLA 残余值: 评价\n...\n\n### π₀ offline 标注: [AGREE / REBUT]\n理由：...\n\n### 是否调整评分？\n原评分：6/10\n调整后：X/10\n理由：...\n```",
    "reviewer_id": "2",
    "round_number": "7"
  }
}
````

</details>

---


### Tool result

_source line 579 · 2026-05-29T00:51:01.826623+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 5326
}
```

</details>

---


### Assistant

_source line 580 · 2026-05-29T00:51:12.798399+00:00_

交叉分享已发送。等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 50

## Round 50

18 recorded events


### User

_source line 581 · 2026-05-29T00:51:14.000916+00:00_

[Reviewer 1 审稿结果]:
Round 7 审查完成。

**核心结论**：论文从 Round 6 的 5/10 改善到 6/10。Attention baseline 和 OpenVLA multi-suite 是实质性改进，解决了两个 critical issue。但 **两个关键问题未解决**：(1) CV diagnostic 仍仅 N=4 闭环模型，无新数据；(2) "primary determinant" 因果语言在 abstract/intro/conclusion 中未被替换，与 limitations 中 "cannot be causally isolated" 的表述自相矛盾——这是 Round 6 明确要求但未执行的修改。

---

[Reviewer 2 审稿结果]:
Round 7 审稿报告已提交。

核心结论：论文从 5/10 提升至 6/10。Zero-mask ablation 和 attention scoring double dissociation 是两个实质性新贡献，Table 2 完整化和 multi-seed 验证大幅提高可信度。但发现一个严重退化——7+ concurrent works（包括 "Don't Run with Scissors"）被从引用中删除，这是 Must-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-29T00:51:21.332033+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-29T00:51:21.433014+00:00_

&lt;persisted-output>
Output too large (28.6KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress--claude-sessions-review-director-d59e3b5c/bbf7c623-fc4a-4a39-a04d-ce10b286bd1d/tool-results/toolu_013dksyE3UACaYR98sMrnMeo.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex:11:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex:7:\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences).
…[truncated 90 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-29T00:51:26.000092+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "jabbour|scissors|specprune|seewhat|sparsevlm|sparsevila|fitprune|crossget|cogact",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "jabbour|scissors|specprune|seewhat|sparsevlm|sparsevila|fitprune|crossget|cogact",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-29T00:51:26.401607+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.bbl:180:  Wang, Liu, Fu, Bao, Chen, Shi, Yang, and Guo]{li2024cogact}
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.bbl:184:\newblock Cogact: A foundational vision-language-action model for synergizing
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex:11:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex:16:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex:27:CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex:45:OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, determines token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex:749:MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\% SR under 78\% prunin
…[truncated 7631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Grep",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-29T00:51:27.004693+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "primary determinant|primary factor|primary architectural",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "primary determinant|primary factor|primary architectural",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-29T00:51:27.105324+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex:18:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex:18:We present an empirical study of VLA token compressibility across six architectures (450M--7B) and four LIBERO manipulation suites, identifying the vision-language connector as the primary determinant of pruning robustness (Figure~\ref{fig:teaser}). Three findings emerge:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-29T00:51:55.049443+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-29T00:51:55.100203+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-29T00:42:19.202438+00:00\", \"completed_at\": \"2026-05-29T00:46:21.205032+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点，第一个 display item 在 page 2。建议考虑将 Figure 1 的精简版或 teaser 提到 page 1 右上角以增强审稿人首页印象，但当前安排也在合理范围内\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1(b) 架构图中的组件标签（\\\"Linear Projection\\\"、\\\"MLP\\\"、\\\"Pixel Shuffle\\\" 等）字号偏小（约 6-7pt），在打印时可能需要仔细辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 2 中 connector 内部组件标签字号偏小，与正文字号比例约 60%，建议适当放大\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 4(b) 散点图中模型名称标注和轴标签字号偏小，建议增大至 ≥8pt 确保打印可读\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 主结果表：最优值已加粗 ✓，booktabs 风格 ✓，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 10\", \"message\": \"Table 4（附录完整结果）列数多、字号偏小，密度较高但附录中可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Figure 9 线图使用了颜色+标记符号双重编码区分曲线，打印友好 ✓\"}, {\"severity\": \"info\", \"dimension\": \"page 19\", \"message\": \"Figure 10 热力图双 panel 布局清晰，颜色梯度可辨 ✓；Figure 11 多 panel 图信息丰富\"}, {\"severity\": \"info\", \"dimension\": \"page 31\", \"message\": \"末页内容约占 50%，但作为附录末页可接受\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 9}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-29T00:52:02.030366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_reports/round_6.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_reports/round_6.md",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-29T00:52:02.081054+00:00_

1	---
2	round: 6
3	review_mode: fresh
4	overall_score: weak reject
5	timestamp: 2026-05-23T06:01:04.550275+00:00
6	reviewer_ids: [1, 2, 3]
7	cross_response_reviewer_ids: [1, 2, 3]
8	force_resubmit: False
9	---
10	
11	
12	# Round 6 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others
13	
14	**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Fresh (重新审稿)
15	
16	---
17	
18	## Summary
19	
20	论文研究 vision token pruning 在不同 VLA 架构上的表现差异，提出 connector architecture 是 pruning robustness 的主要关联因素。核心发现：(1) pixel-shuffle connector (SmolVLA) 在仅移除 5% token 即崩溃至 0% SR，经双 checkpoint 验证；(2) token-entangling connectors 展现 task-complexity amplified collapse（X-VLA 在 Object 仅损失 1.4pp 但 Goal 损失 27.8pp）；(3) CV of L2 norms 作为 diagnostic 与 pruning tolerance 相关；(4) VTR (cross-attention re-encoding) 在 SmolVLA 上从 0% 恢复至 ~60% SR。实验覆盖 6 个 VLA 架构（450M-7B），4 个 LIBERO task suite，2 种 pruning 策略。
21	
22	---
23	
24	## Strengths
25	
26	**S1** [3/3 共识] **Pixel-shuffle 崩溃机制发现扎实且有价值。** SmolVLA 在 k=0.95（仅移除 6/128 tokens）即从 59.2% 崩溃至 0.0% SR，经 LoRA fine-tuned 和官方 checkpoint 双重验证，7 种 pruning 配置（ACIS/random/L2 × zero-mask/true removal/ToMe）均为 0%。这是从 pixel-shuffle 架构定义可演绎推导但首次被系统实证的结果，对 practitioners 有直接预警价值。(Section 4.3, Table 3/Appendix D)
27	
28	**S2** [3/3 共识] **实验设计系统性在 VLA pruning 文献中范围最广。** 6 个架构 × 3 种 connector family × 2 种 pruning 策略 × 6 个 retention ratio，附录详尽（27 页，含 per-task breakdown、multi-seed validation、hypergeometric model、attention entropy analysis）。Wilson 95% CI + 500 episodes/condition 是合理的统计实践。
29	
30	**S3** [3/3 共识] **写作清晰，结构合理。** Figure 1 teaser 有效传达 two-axis framework，Table 1 model properties 设计精简，Introduction 的 problem→gap→approach→contributions 流程逻辑严密。
31	
32	**S4** [2/3 共识] **Limitations 态度诚实。** 论文承认 simulation-only、causal isolation 不可能、CV data points 有限等核心局限（虽然主文过短，扩展讨论在 Appendix A）。
33	
34	**S5** **VTR 从 0% 恢复至 ~60% SR 是有价值的 proof-of-concept。** 在所有 hard pruning 方法均失败的条件下，22M 参数的 re-encoding 模块在 75% 压缩下恢复功能性能。MLP adapter 达到 comparable 性能 (p=0.15) 的发现本身也有价值——说明 re-enc
…[truncated 737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-29T00:52:14.892328+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update_review_issues submit_review_report",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update_review_issues submit_review_report",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-29T00:52:15.010395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "ToolSearch",
  "elapsed_ms": 118
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-29T00:53:41.899473+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "issues_yaml": "\n# ===== Round 4-5 Recurring Issues =====\n\n- id: \"R4-C3\"\n  summary: \"CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"3 data points = 3 connector clusters\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — CV reframed as correlational diagnostic\"}\n    - {round: 6, reviewers: \"R1+R2+R3 consensus\", note: \"RECURRED as R6-C1. Writing fix insufficient.\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"N still=4 closed-loop. Claims narrowed but no new data. Downgraded from critical to major.\"}\n  action_items:\n    - {round: 4, action: \"Reframe CV as correlational diagnostic\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"C2 → coarse indicator + 3-bucket classifier\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"E3 cosine similarity mechanism explanation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Add more VLA models for CV N expansion\", assigned_to: \"main_agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-C1\"\n  summary: \"Causal claim under-identified\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R1+R2\", note: \"determines needs downgrade\"}\n    - {round: 5, reviewers: \"R1+R2\", note: \"RESOLVED\"}\n    - {round: 6, reviewers: \"R1+R3+R2\", note: \"RECURRED: 'primary determinant' in Conclusion\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"REGRESSION: intro still uses 'primary determinant', contradicts limitations 'cannot be causally isolated'\"}\n  action_items:\n    - {round: 4, action: \"Full-text causal language downgrade\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"'most consistent structural factor' + confounder caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 7, action: \"Replace 'primary determinant' in intro with non-causal language; unify abstract/conclusion\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ===== Round 6 Issues =====\n\n- id: \"R6-C1\"\n  summary: \"CV diagnostic N=3-4 insufficient [RECURRING]\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"N=3-4 cannot reach significance\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"N unchanged. Claims narrowed ('validated on four'). Downgraded to major warning.\"}\n  action_items:\n    - {round: 6, action: \"C2 → coarse indicator + 3-bucket\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"E3 cosine similarity\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Add VLA models (Octo/CogACT/etc)\", assigned_to: \"main_agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C2\"\n  summary: \"Table 2 ~20% missing + OpenVLA Object-only\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"Data completeness baseline\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"Main table clean (0 gaps). Appendix ~14% gaps remain but acceptable. Caption should say 'available' not 'full'.\"}\n  action_items:\n    - {round: 6, action: \"E1: 9 Table 2 gaps\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"E2: OpenVLA multi-suite\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Main Table 2 fully populated. OpenVLA multi-suite data in Appendix Table 4 (k=0.9 all 4 suites). Minor: appendix caption says 'Full results' but ~14% gaps remain.\"\n  resolution_round: 7\n\n- id: \"R6-C3\"\n  summary: \"Causal narrative overreach [RECURRING]\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R1+R3+R2\", note: \"'primary determinant' contradicts Appendix N\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"REGRESSION: intro.tex still has 'primary determinant'. abstract 'primary architectural factor'. conclusion 'primary factor'. Not unified to non-causal language.\"}\n  action_items:\n    - {round: 6, action: \"'most consistent structural factor' + confounder caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 7, action: \"Replace all 'primary determinant/factor' with 'strongest predictor' or 'most consistent structural factor'\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C4\"\n  summary: \"Missing attention-based pruning baseline\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R1+R2\", note: \"FastV/VLA-Cache cited but not tested\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"RESOLVED. Table tab:attention_pruning (X-VLA 4 suites), Table tab:pi05_attention_crosssuite (π₀.5 4 suites), OpenVLA attention† in full_results. Double dissociation finding is paper's strongest new insight.\"}\n  action_items:\n    - {round: 6, action: \"E5: X-VLA BART attention-based pruning\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"E5 data integration into paper (method×task interaction)\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Comprehensive attention scoring across 3 closed-loop models. X-VLA attention recovers ≥92.8% at k=0.5. π₀.5 attention catastrophic on Object (-31.6pp). Architecture-dependent scoring reversal confirmed.\"\n  resolution_round: 7\n\n- id: \"R6-C5\"\n  summary: \"AI disclosure missing\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3+R2\", note: \"CoRL compliance\"}\n  action_items:\n    - {round: 6, action: \"Add AI disclosure\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Reviewer verified PASS. Limitations section contains AI disclosure.\"\n  resolution_round: 6\n\n- id: \"R6-C6\"\n  summary: \"VTR/Smart Compress naming — 25+ sites\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"Two unrelated names\"}\n  action_items:\n    - {round: 6, action: \"Global replace Smart Compress → VTR\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Reviewer verified PASS. Active tex files unified to VTR.\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"VTR weakened by MLP adapter [RECURRING]\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"C3 about re-encoding not architecture\"}\n  action_items:\n    - {round: 6, action: \"C3 → 'learned re-encoding regardless of architecture'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Reviewer verified PASS. 4 locations consistent.\"\n  resolution_round: 6\n\n- id: \"R6-W2\"\n  summary: \"LaTeX pi_0.5 rendering error\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"39+ occurrences\"}\n    - {round: 7, reviewers: \"R1\", note: \"PASS. Active files all use correct braces.\"}\n  action_items:\n    - {round: 6, action: \"Global fix pi_{0.5} and pi_{0}\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Active tex files all use $\\\\pi_{0.5}$.\"\n  resolution_round: 6\n\n- id: \"R6-W3\"\n  summary: \"Limitations too short\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R3+R2+R1\", note: \"60 words, missing key limitations\"}\n    - {round: 7, reviewers: \"R1\", note: \"PASS. 7 sentences + AI disclosure, covers sim-to-real/causal/N=4/VTR/scoring/seed.\"}\n  action_items:\n    - {round: 6, action: \"Expand to 6-item paragraph\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Standalone section, 7 sentences, 6 substantive items + AI disclosure.\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Simulation-only — no sim-to-real discussion\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2+R3\", note: \"CoRL prioritizes real-robot\"}\n  action_items:\n    - {round: 6, action: \"Limitations sim-to-real sentence\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Covered in Limitations first item.\"\n  resolution_round: 6\n\n- id: \"R6-W5\"\n  summary: \"OpenVLA Object-only — task-complexity axis unvalidated for MLP\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R2+R1\", note: \"Structural weakness\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"RESOLVED. Appendix Table 4 has 4-suite k=0.9 data. Appendix extended discussion with fig_openvla_sweep.\"}\n  action_items:\n    - {round: 6, action: \"E2: OpenVLA multi-suite\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"OpenVLA baselines: Object 74.0%, Goal 74.8%, Spatial 80.0%, Long 52.8%. k=0.9 data for all 4 suites with attention scoring. Extended discussion with per-suite scoring analysis in Appendix.\"\n  resolution_round: 7\n\n- id: \"R6-W6\"\n  summary: \"No code/data release plan\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R3+R2\", note: \"Reproducibility\"}\n    - {round: 7, reviewers: \"R2\", note: \"Still not mentioned in paper.\"}\n  action_items:\n    - {round: 6, action: \"Add release statement\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 7, action: \"Verify release statement exists in paper\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Post-connector pruning not justified\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1+R2\", note: \"Pre-connector might differ\"}\n  action_items:\n    - {round: 6, action: \"§3.2 justification paragraph\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"VLA-Cache cited as pre-connector contrast.\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Cross-condition seed inconsistency\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1+R2\", note: \"OpenVLA L2=seed42, random=seed7\"}\n  action_items:\n    - {round: 6, action: \"Table 2 seed footnote\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Caption + appendix cross-ref.\"\n  resolution_round: 6\n\n- id: \"R6-I1\"\n  summary: \"Paper identity split\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2+R3\", note: \"Need primary = empirical study\"}\n  action_items:\n    - {round: 6, action: \"Intro: 'empirical study'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Abstract + Intro consistent.\"\n  resolution_round: 6\n\n- id: \"R6-I2\"\n  summary: \"Abstract density — 17 numbers\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R3, R2 partial REBUT\", note: \"Keep 4-5 key numbers\"}\n    - {round: 7, reviewers: \"R2\", note: \"Still ~16 numbers. Content improved but density unchanged.\"}\n  action_items:\n    - {round: 6, action: \"Reduce to ~5 core numbers + 3-bucket qualitative\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 7, action: \"Further reduce abstract numbers to ~8-10\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I3\"\n  summary: \"'Don't Run with Scissors' differentiation\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2, R1 REBUT\", note: \"1-2 sentences\"}\n  action_items:\n    - {round: 6, action: \"Related Work comparison sentence\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Comparison sentence added.\"\n  resolution_round: 6\n\n# ===== Round 7 New Issues =====\n\n- id: \"R7-N1\"\n  summary: \"7+ concurrent works deleted from citations (including Don't Run with Scissors)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: \"R2, R1 AGREE\", note: \"bib entries exist but no \\\\cite{} in active tex files. Includes jabbour2025dontrun, specprunevla, seewhatmatters, sparsevlm, sparsevila, fitprune, crossget. Dangerous in blind review.\"}\n  action_items:\n    - {round: 7, action: \"Restore all deleted concurrent work citations in Related Work\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"X-VLA Goal attention merged as '98.2*' in Table — selective reporting concern\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: \"R2\", note: \"Other suites show 3 variants separately; Goal merges to single 'best of three'. Either expand or annotate 'all three ≥X%'.\"}\n  action_items:\n    - {round: 7, action: \"Expand X-VLA Goal attention to 3 columns or add annotation\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-I1\"\n  summary: \"Zero-mask 'entirely attributable' should be scoped to π₀.5\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: \"R2\", note: \"Mechanism tied to RoPE; may not generalize to non-RoPE architectures (X-VLA BART uses learned PE).\"}\n  action_items:\n    - {round: 7, action: \"Add 'on π₀.5' qualifier to zero-mask claim\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "issues_yaml": "\n# ===== Round 4-5 Recurring Issues =====\n\n- id: \"R4-C3\"\n  summary: \"CV predictor only 3 models x 2 k = 6 data points, k=0.3 reversal\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R1+R2 consensus\", note: \"3 data points = 3 connector clusters\"}\n    - {round: 5, reviewers: \"R1+R2 consensus\", note: \"RESOLVED — CV reframed as correlational diagnostic\"}\n    - {round: 6, reviewers: \"R1+R2+R3 consensus\", note: \"RECURRED as R6-C1. Writing fix insufficient.\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"N still=4 closed-loop. Claims narrowed but no new data. Downgraded from critical to major.\"}\n  action_items:\n    - {round: 4, action: \"Reframe CV as correlational diagnostic\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"C2 → coarse indicator + 3-bucket classifier\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"E3 cosine similarity mechanism explanation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Add more VLA models for CV N expansion\", assigned_to: \"main_agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-C1\"\n  summary: \"Causal claim under-identified\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - {round: 4, reviewers: \"R1+R2\", note: \"determines needs downgrade\"}\n    - {round: 5, reviewers: \"R1+R2\", note: \"RESOLVED\"}\n    - {round: 6, reviewers: \"R1+R3+R2\", note: \"RECURRED: 'primary determinant' in Conclusion\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"REGRESSION: intro still uses 'primary determinant', contradicts limitations 'cannot be causally isolated'\"}\n  action_items:\n    - {round: 4, action: \"Full-text causal language downgrade\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"'most consistent structural factor' + confounder caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 7, action: \"Replace 'primary determinant' in intro with non-causal language; unify abstract/conclusion\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ===== Round 6 Issues =====\n\n- id: \"R6-C1\"\n  summary: \"CV diagnostic N=3-4 insufficient [RECURRING]\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"N=3-4 cannot reach significance\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"N unchanged. Claims narrowed ('validated on four'). Downgraded to major warning.\"}\n  action_items:\n    - {round: 6, action: \"C2 → coarse indicator + 3-bucket\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"E3 cosine similarity\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Add VLA models (Octo/CogACT/etc)\", assigned_to: \"main_agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C2\"\n  summary: \"Table 2 ~20% missing + OpenVLA Object-only\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"Data completeness baseline\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"Main table clean (0 gaps). Appendix ~14% gaps remain but acceptable. Caption should say 'available' not 'full'.\"}\n  action_items:\n    - {round: 6, action: \"E1: 9 Table 2 gaps\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"E2: OpenVLA multi-suite\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Main Table 2 fully populated. OpenVLA multi-suite data in Appendix Table 4 (k=0.9 all 4 suites). Minor: appendix caption says 'Full results' but ~14% gaps remain.\"\n  resolution_round: 7\n\n- id: \"R6-C3\"\n  summary: \"Causal narrative overreach [RECURRING]\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R1+R3+R2\", note: \"'primary determinant' contradicts Appendix N\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"REGRESSION: intro.tex still has 'primary determinant'. abstract 'primary architectural factor'. conclusion 'primary factor'. Not unified to non-causal language.\"}\n  action_items:\n    - {round: 6, action: \"'most consistent structural factor' + confounder caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 7, action: \"Replace all 'primary determinant/factor' with 'strongest predictor' or 'most consistent structural factor'\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C4\"\n  summary: \"Missing attention-based pruning baseline\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R1+R2\", note: \"FastV/VLA-Cache cited but not tested\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"RESOLVED. Table tab:attention_pruning (X-VLA 4 suites), Table tab:pi05_attention_crosssuite (π₀.5 4 suites), OpenVLA attention† in full_results. Double dissociation finding is paper's strongest new insight.\"}\n  action_items:\n    - {round: 6, action: \"E5: X-VLA BART attention-based pruning\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"E5 data integration into paper (method×task interaction)\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Comprehensive attention scoring across 3 closed-loop models. X-VLA attention recovers ≥92.8% at k=0.5. π₀.5 attention catastrophic on Object (-31.6pp). Architecture-dependent scoring reversal confirmed.\"\n  resolution_round: 7\n\n- id: \"R6-C5\"\n  summary: \"AI disclosure missing\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R3+R2\", note: \"CoRL compliance\"}\n  action_items:\n    - {round: 6, action: \"Add AI disclosure\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Reviewer verified PASS. Limitations section contains AI disclosure.\"\n  resolution_round: 6\n\n- id: \"R6-C6\"\n  summary: \"VTR/Smart Compress naming — 25+ sites\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"Two unrelated names\"}\n  action_items:\n    - {round: 6, action: \"Global replace Smart Compress → VTR\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Reviewer verified PASS. Active tex files unified to VTR.\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"VTR weakened by MLP adapter [RECURRING]\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"C3 about re-encoding not architecture\"}\n  action_items:\n    - {round: 6, action: \"C3 → 'learned re-encoding regardless of architecture'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Reviewer verified PASS. 4 locations consistent.\"\n  resolution_round: 6\n\n- id: \"R6-W2\"\n  summary: \"LaTeX pi_0.5 rendering error\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"3/3 consensus\", note: \"39+ occurrences\"}\n    - {round: 7, reviewers: \"R1\", note: \"PASS. Active files all use correct braces.\"}\n  action_items:\n    - {round: 6, action: \"Global fix pi_{0.5} and pi_{0}\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Active tex files all use $\\\\pi_{0.5}$.\"\n  resolution_round: 6\n\n- id: \"R6-W3\"\n  summary: \"Limitations too short\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R3+R2+R1\", note: \"60 words, missing key limitations\"}\n    - {round: 7, reviewers: \"R1\", note: \"PASS. 7 sentences + AI disclosure, covers sim-to-real/causal/N=4/VTR/scoring/seed.\"}\n  action_items:\n    - {round: 6, action: \"Expand to 6-item paragraph\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Standalone section, 7 sentences, 6 substantive items + AI disclosure.\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Simulation-only — no sim-to-real discussion\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2+R3\", note: \"CoRL prioritizes real-robot\"}\n  action_items:\n    - {round: 6, action: \"Limitations sim-to-real sentence\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Covered in Limitations first item.\"\n  resolution_round: 6\n\n- id: \"R6-W5\"\n  summary: \"OpenVLA Object-only — task-complexity axis unvalidated for MLP\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R2+R1\", note: \"Structural weakness\"}\n    - {round: 7, reviewers: \"R1+R2 consensus\", note: \"RESOLVED. Appendix Table 4 has 4-suite k=0.9 data. Appendix extended discussion with fig_openvla_sweep.\"}\n  action_items:\n    - {round: 6, action: \"E2: OpenVLA multi-suite\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"OpenVLA baselines: Object 74.0%, Goal 74.8%, Spatial 80.0%, Long 52.8%. k=0.9 data for all 4 suites with attention scoring. Extended discussion with per-suite scoring analysis in Appendix.\"\n  resolution_round: 7\n\n- id: \"R6-W6\"\n  summary: \"No code/data release plan\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R3+R2\", note: \"Reproducibility\"}\n    - {round: 7, reviewers: \"R2\", note: \"Still not mentioned in paper.\"}\n  action_items:\n    - {round: 6, action: \"Add release statement\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 7, action: \"Verify release statement exists in paper\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W7\"\n  summary: \"Post-connector pruning not justified\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1+R2\", note: \"Pre-connector might differ\"}\n  action_items:\n    - {round: 6, action: \"§3.2 justification paragraph\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"VLA-Cache cited as pre-connector contrast.\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Cross-condition seed inconsistency\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1+R2\", note: \"OpenVLA L2=seed42, random=seed7\"}\n  action_items:\n    - {round: 6, action: \"Table 2 seed footnote\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Caption + appendix cross-ref.\"\n  resolution_round: 6\n\n- id: \"R6-I1\"\n  summary: \"Paper identity split\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2+R3\", note: \"Need primary = empirical study\"}\n  action_items:\n    - {round: 6, action: \"Intro: 'empirical study'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Abstract + Intro consistent.\"\n  resolution_round: 6\n\n- id: \"R6-I2\"\n  summary: \"Abstract density — 17 numbers\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - {round: 6, reviewers: \"R3, R2 partial REBUT\", note: \"Keep 4-5 key numbers\"}\n    - {round: 7, reviewers: \"R2\", note: \"Still ~16 numbers. Content improved but density unchanged.\"}\n  action_items:\n    - {round: 6, action: \"Reduce to ~5 core numbers + 3-bucket qualitative\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 7, action: \"Further reduce abstract numbers to ~8-10\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I3\"\n  summary: \"'Don't Run with Scissors' differentiation\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2, R1 REBUT\", note: \"1-2 sentences\"}\n  action_items:\n    - {round: 6, action: \"Related Work comparison sentence\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Comparison sentence added.\"\n  resolution_round: 6\n\n# ===== Round 7 New Issues =====\n\n- id: \"R7-N1\"\n  summary: \"7+ concurrent works deleted from citations (including Don't Run with Scissors)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: \"R2, R1 AGREE\", note: \"bib entries exist but no \\\\cite{} in active tex files. Includes jabbour2025dontrun, specprunevla, seewhatmatters, sparsevlm, sparsevila, fitprune, crossget. Dangerous in blind review.\"}\n  action_items:\n    - {round: 7, action: \"Restore all deleted concurrent work citations in Related Work\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"X-VLA Goal attention merged as '98.2*' in Table — selective reporting concern\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: \"R2\", note: \"Other suites show 3 variants separately; Goal merges to single 'best of three'. Either expand or annotate 'all three ≥X%'.\"}\n  action_items:\n    - {round: 7, action: \"Expand X-VLA Goal attention to 3 columns or add annotation\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-I1\"\n  summary: \"Zero-mask 'entirely attributable' should be scoped to π₀.5\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - {round: 7, reviewers: \"R2\", note: \"Mechanism tied to RoPE; may not generalize to non-RoPE architectures (X-VLA BART uses learned PE).\"}\n  action_items:\n    - {round: 7, action: \"Add 'on π₀.5' qualifier to zero-mask claim\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-29T00:53:42.000496+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_issues.yaml\", \"bytes\": 14297}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-29T00:55:29.566650+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 7 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others\n\n**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Continue (基于 Round 6)\n**Round 6 评分**: 5/10 (Weak Reject) | **Round 7 评分**: 6/10 (Borderline Accept)\n\n---\n\n## Summary\n\n论文从 Round 6 显著改进。新增 zero-mask ablation（分离 position disruption vs information loss，89pp gap）、attention-based scoring double dissociation（connector 决定哪种 scoring 有效）、π₀.5 Long 5-seed 验证、OpenVLA 全 4 suite 数据。Table 2 主表完整化，Limitations section 独立且全面。两个 Round 6 critical issue 已 resolved（attention baseline、OpenVLA multi-suite）。但发现一个严重退化——7+ concurrent works 被从引用中删除——以及因果语言 \"primary determinant\" 仍未替换，与 Limitations 中 \"cannot be causally isolated\" 自相矛盾。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **Attention scoring double dissociation 是论文最有 insight 的新发现。** L2 对 independent connectors 有效（π₀.5 Goal +35.2pp），attention 对 entangling connectors 有效（X-VLA ≥92.8%），且两者不可互换（π₀.5 Object attention −31.6pp, X-VLA L2 −27.2pp）。Table tab:scoring_crossover_summary 的 2×2 矩阵清晰展示了 connector-dependent scoring reversal。这比 Round 6 提供的任何 contribution 都更有 depth。\n\n**S2** [R1+R2 共识] **Zero-mask ablation 实验设计 elegant。** 将 10% token embedding 置零（100% 信息损失，0% 位置变化）保留 98.0% SR vs hard pruning（位置变化）崩溃到 9.0%——如果信息丢失是主因，zero-masking 应更差，但实际结果相反，清晰归因于 position disruption。\n\n**S3** [R1+R2 共识] **Table 2 主表完整化 + multi-seed 验证大幅提高可信度。** 主表 3 模型 × 4 suite × 3 k-values 无缺失。π₀.5 Long n=5 seeds（s.d. ≤2.7pp）确认 V-shaped random recovery 是 structural property。\n\n**S4** [R1+R2 共识] **Limitations section 扎实诚实。** 独立 section，7 句话覆盖 sim-only/causal isolation/N=4/VTR generalization/scoring methods/single-seed + AI disclosure。\n\n**S5** [R2] **论文 identity 更清晰。** 从 Round 6 的 \"observation-heavy empirical study\" 进化为有 mechanistic insight 的分析——zero-mask 和 attention scoring 各自提供了 WHY 层面的解释。\n\n---\n\n## Weaknesses (Must-Fix)\n\n**W-MF1** [R2 发现, R1 AGREE, Director 独立验证] **7+ concurrent works 被从引用中删除——Related Work 覆盖严重退化。**\n\nDirector 独立验证确认：`references.bib` 中存在以下条目但活跃 .tex 文件中无 `\\cite{}`：\n- **jabbour2025dontrun** (\"Don't Run with Scissors\") — 最接近的 concurrent work，也发现 pruning breaks VLA 并提出 recovery method\n- **wang2025specprunevla** (SpecPrune-VLA) — VLA pruning 方法\n- **feng2026seewhatmatters** (\"See What Matters\", ICML 2026) — VLA pruning\n- **zhang2025sparsevlm** (SparseVLM) — VLM token sparsification\n- **khaki2025sparsevila** (SparseVILA) — VLM token sparsification\n- **ye2025fitprune** (FitPrune) — VLM token pruning\n- **shi2024crossget** (CrossGET) — ViT token pruning\n\nRound 6 论文引用了这些工作；Round 7 修改中被移除。在 blind review 中删除最接近的 concurrent work 极其危险——reviewer 若了解 \"Don't Run with Scissors\" 会认为故意回避比较。\n\n**W-MF2** [R1+R2 全员共识] **因果语言 \"primary determinant\" 未替换——Round 6 明确要求但未执行。**\n\nDirector 独立 grep 确认：\n- `introduction.tex`: \"identifying the vision-language connector as the **primary determinant** of pruning robustness\"\n- `abstract.tex`: \"the **primary architectural factor** governing pruning tolerance\"\n- `conclusion.tex`: \"Connector architecture is the **primary factor** governing VLA token compressibility\"\n\nRound 6 修复声明称已替换为 \"most consistent structural factor\"，但实际未执行。`limitations.tex` 写 \"preventing full causal isolation of the connector effect\"——与主文 \"primary determinant\" 自相矛盾。这是第三轮提出此问题（Round 4 → 5 → 6 → 7），属于反复回归。\n\n---\n\n## Weaknesses (Should-Fix)\n\n**W-SF1** [R1+R2 共识] **CV diagnostic 仍仅 N=4 闭环模型，无新数据。**\n\nTable 1 不变：π₀.5, X-VLA, OpenVLA, SmolVLA（闭环）+ π₀, OFT（offline）。CogACT 仅从文献引用（74.2% SR under 78% pruning），无原始 CV 数据。论文已将 claim 收窄为 \"validated on four closed-loop architectures\"，Limitations 承认 \"too few for a general law\"，属正确降级。从 Round 6 的 critical 降级为 major warning——claims 已适当收窄，但 evidence base 未增加的事实不变。\n\n**W-SF2** [R2] **X-VLA Goal attention 结果在 Table tab:attention_pruning 中合并为 \"98.2*\"。** 其他三个 suite 分别列出 attn_last/attn_mean/attn_rollout，Goal 合并为 \"Best of three attention variants\"。不一致暗示选择性报告。应展开为三列或标注 \"all three ≥X%\"。\n\n**W-SF3** [R2] **OpenVLA 移至附录造成主文叙事断裂。** Table 2 仅 3 个模型（π₀.5, X-VLA, SmolVLA），CV spectrum 缺少 0.215 的 MLP calibration 点。论文声称 \"six architectures\" 但主表仅 50% 模型。建议至少加入 OpenVLA Object 行。\n\n**W-SF4** [R2] **Appendix Table 4 caption 说 \"Full results\" 但仍有 ~14% \"--\" 缺失。** OpenVLA k=0.95/0.7/0.5 大部分缺失；X-VLA k=0.7 Spatial/Long 缺失。应改 caption 为 \"available results\" 或补全。\n\n**W-SF5** [R2] **代码/数据发布计划仍缺失。** Round 6 R3-W3 要求添加发布声明，Round 7 未见。\n\n---\n\n## Weaknesses (Info / Minor)\n\n**I1** [R2] Abstract 数字密度仍高（~16 个数值），Round 6 要求从 ~17 降到 ~5 未充分回应。新增内容（zero-mask, scoring reversal）有价值但数字未精简。\n\n**I2** [R2] Zero-mask ablation 的 \"entirely attributable to position disruption\" 应限定为 \"on π₀.5\"，因机制与 RoPE 相关，不一定 generalize 到 non-RoPE 架构。\n\n**I3** [R1] Abstract 使用 π₀ (offline-only) 的 CV=0.038 作为 spectrum 下界，未标注 offline。\n\n---\n\n## Questions\n\n**Q1** X-VLA Goal attention 三种 variant 各自的 SR 是多少？如果差异 <2pp 为何不展开？如果差异大为何只报告 best？\n\n**Q2** Zero-mask 是否在其他模型（X-VLA、OpenVLA）上测试过？如果是，结果如何？如果否，为什么不？\n\n**Q3** Round 7 Related Work 为何删除了 7+ concurrent works 的引用？是有意精简还是修改过程中的疏忽？\n\n---\n\n## Missing References\n\n以下引用在 `references.bib` 中存在但未在正文引用——应恢复：\n\n1. Jabbour et al., \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered,\" 2025\n2. Wang et al., SpecPrune-VLA, 2025\n3. Feng et al., \"See What Matters,\" ICML 2026\n4. Zhang et al., SparseVLM, 2025\n5. Khaki et al., SparseVILA, 2025\n6. Ye et al., FitPrune, 2025\n7. Shi et al., CrossGET, 2024\n\n---\n\n## External Review\n\n外部审稿未请求（Round 7 为 continue 模式）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（4 分钟）。结果：**0 critical, 0 warning, 9 info**。\n\n- 首页无 display item（Figure 1 在 page 2），建议但非必须\n- Figure 1(b)/Figure 2 架构图组件标签字号偏小（~6-7pt），建议放大\n- Figure 4(b) 散点图标注字号偏小，建议 ≥8pt\n- Table 2 格式规范 ✓（booktabs + 加粗最优值）\n- 附录 Table 4 密度高但可接受\n- Figure 9 使用颜色+标记双编码，打印友好 ✓\n- 正文 8 页合规 ✓\n\n---\n\n## Round 6 → Round 7 Issue 追踪总结\n\n| Issue | Round 6 状态 | Round 7 状态 | 变化 |\n|-------|-------------|-------------|------|\n| R6-C1 (CV N=4) | critical/in_progress | warning/in_progress | Claims 收窄，降级 |\n| R6-C2 (Table 2 gaps) | critical/in_progress | info/resolved | 主表完整 |\n| R6-C3 (Causal language) | critical/resolved | critical/in_progress | **REGRESSION** |\n| R6-C4 (Attention baseline) | critical/in_progress | **resolved** | 3 模型全覆盖 |\n| R6-W5 (OpenVLA multi-suite) | warning/in_progress | **resolved** | 4 suite 数据 |\n| R6-W6 (Code release) | warning/resolved | warning/in_progress | 回归 |\n| R6-I2 (Abstract density) | info/resolved | info/in_progress | 未改善 |\n| R7-N1 (Citations deleted) | — | **critical/open** | 新发现 |\n| R7-W1 (Goal attention merge) | — | warning/open | 新发现 |\n\n**净变化**：+2 resolved (C4, W5)，+1 regression (C3)，+1 new critical (N1)，1 downgraded (C1)\n\n---\n\n## Overall Assessment\n\n**Round 7 评分：6/10（Borderline Accept）**\n\n**升分理由（5→6）**：\n- Attention scoring double dissociation 是 genuine insight（S1）——connector 决定哪种 scoring 有效，没有 universal winner\n- Zero-mask ablation 实验设计 elegant，清晰分离 position disruption vs information loss（S2）\n- Table 2 完整化 + π₀.5 Long n=5 multi-seed 消除关键统计疑虑（S3）\n- 两个 Round 6 critical issue resolved（attention baseline、OpenVLA multi-suite）\n- Limitations section 扎实诚实\n\n**未达 7/10 的理由**：\n- **7+ concurrent works 被删除是 unacceptable regression**——必须在提交前修复（W-MF1）\n- **\"Primary determinant\" 因果语言第三轮未修正**——与 Limitations 自相矛盾（W-MF2）\n- CV diagnostic 仍仅 N=4 闭环模型，evidence base 未增加（W-SF1）\n- Simulation-only 对 CoRL 的 practical impact 有限\n- VTR 仅在 SmolVLA 验证，MLP adapter 达到 comparable 性能\n\n**从 6→7 需要**：\n1. 恢复所有被删除的 concurrent work 引用，\"Don't Run with Scissors\" 需专门段落\n2. 全文统一非因果措辞（\"strongest predictor\" 或 \"most consistent structural factor\"）\n3. 展开 X-VLA Goal attention 数据\n\n---\n\n## Detailed Comments\n\n### Round 7 修改亮点\n\n论文在实验深度上有显著进步。Attention scoring 从 zero 覆盖扩展到 3 个模型 × 4 个 suite 的系统比较，揭示了 connector-dependent scoring reversal——这是 Round 6 版本完全缺失的 mechanistic insight。Zero-mask ablation 用优雅的实验设计回答了 \"为什么 10% token 移除会导致 89pp 崩溃\" 这个核心问题。π₀.5 Long 的 5-seed 验证将关键数据点从单一观察提升为可重复发现。\n\n### 遗留问题优先级\n\n1. **P0（阻止提交）**：恢复 7+ concurrent work 引用。\"Don't Run with Scissors\" 是最近的 concurrent work——在 blind review 中遗漏它等同于放弃通过 novelty 检查的机会。\n2. **P0（阻止提交）**：统一因果语言。这是第三轮相同问题，abstract/intro/conclusion 各用不同措辞且与 limitations 矛盾。30 分钟文本替换即可解决。\n3. **P1**：展开 X-VLA Goal attention 数据。\n4. **P2**：Appendix table caption 修正（\"available\" not \"full\"）；Abstract 数字精简。",
  "project": "importance_margin_vla_compress",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline accept",
  "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 7 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others\n\n**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Continue (基于 Round 6)\n**Round 6 评分**: 5/10 (Weak Reject) | **Round 7 评分**: 6/10 (Borderline Accept)\n\n---\n\n## Summary\n\n论文从 Round 6 显著改进。新增 zero-mask ablation（分离 position disruption vs information loss，89pp gap）、attention-based scoring double dissociation（connector 决定哪种 scoring 有效）、π₀.5 Long 5-seed 验证、OpenVLA 全 4 suite 数据。Table 2 主表完整化，Limitations section 独立且全面。两个 Round 6 critical issue 已 resolved（attention baseline、OpenVLA multi-suite）。但发现一个严重退化——7+ concurrent works 被从引用中删除——以及因果语言 \"primary determinant\" 仍未替换，与 Limitations 中 \"cannot be causally isolated\" 自相矛盾。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **Attention scoring double dissociation 是论文最有 insight 的新发现。** L2 对 independent connectors 有效（π₀.5 Goal +35.2pp），attention 对 entangling connectors 有效（X-VLA ≥92.8%），且两者不可互换（π₀.5 Object attention −31.6pp, X-VLA L2 −27.2pp）。Table tab:scoring_crossover_summary 的 2×2 矩阵清晰展示了 connector-dependent scoring reversal。这比 Round 6 提供的任何 contribution 都更有 depth。\n\n**S2** [R1+R2 共识] **Zero-mask ablation 实验设计 elegant。** 将 10% token embedding 置零（100% 信息损失，0% 位置变化）保留 98.0% SR vs hard pruning（位置变化）崩溃到 9.0%——如果信息丢失是主因，zero-masking 应更差，但实际结果相反，清晰归因于 position disruption。\n\n**S3** [R1+R2 共识] **Table 2 主表完整化 + multi-seed 验证大幅提高可信度。** 主表 3 模型 × 4 suite × 3 k-values 无缺失。π₀.5 Long n=5 seeds（s.d. ≤2.7pp）确认 V-shaped random recovery 是 structural property。\n\n**S4** [R1+R2 共识] **Limitations section 扎实诚实。** 独立 section，7 句话覆盖 sim-only/causal isolation/N=4/VTR generalization/scoring methods/single-seed + AI disclosure。\n\n**S5** [R2] **论文 identity 更清晰。** 从 Round 6 的 \"observation-heavy empirical study\" 进化为有 mechanistic insight 的分析——zero-mask 和 attention scoring 各自提供了 WHY 层面的解释。\n\n---\n\n## Weaknesses (Must-Fix)\n\n**W-MF1** [R2 发现, R1 AGREE, Director 独立验证] **7+ concurrent works 被从引用中删除——Related Work 覆盖严重退化。**\n\nDirector 独立验证确认：`references.bib` 中存在以下条目但活跃 .tex 文件中无 `\\cite{}`：\n- **jabbour2025dontrun** (\"Don't Run with Scissors\") — 最接近的 concurrent work，也发现 pruning breaks VLA 并提出 recovery method\n- **wang2025specprunevla** (SpecPrune-VLA) — VLA pruning 方法\n- **feng2026seewhatmatters** (\"See What Matters\", ICML 2026) — VLA pruning\n- **zhang2025sparsevlm** (SparseVLM) — VLM token sparsification\n- **khaki2025sparsevila** (SparseVILA) — VLM token sparsification\n- **ye2025fitprune** (FitPrune) — VLM token pruning\n- **shi2024crossget** (CrossGET) — ViT token pruning\n\nRound 6 论文引用了这些工作；Round 7 修改中被移除。在 blind review 中删除最接近的 concurrent work 极其危险——reviewer 若了解 \"Don't Run with Scissors\" 会认为故意回避比较。\n\n**W-MF2** [R1+R2 全员共识] **因果语言 \"primary determinant\" 未替换——Round 6 明确要求但未执行。**\n\nDirector 独立 grep 确认：\n- `introduction.tex`: \"identifying the vision-language connector as the **primary determinant** of pruning robustness\"\n- `abstract.tex`: \"the **primary architectural factor** governing pruning tolerance\"\n- `conclusion.tex`: \"Connector architecture is the **primary factor** governing VLA token compressibility\"\n\nRound 6 修复声明称已替换为 \"most consistent structural factor\"，但实际未执行。`limitations.tex` 写 \"preventing full causal isolation of the connector effect\"——与主文 \"primary determinant\" 自相矛盾。这是第三轮提出此问题（Round 4 → 5 → 6 → 7），属于反复回归。\n\n---\n\n## Weaknesses (Should-Fix)\n\n**W-SF1** [R1+R2 共识] **CV diagnostic 仍仅 N=4 闭环模型，无新数据。**\n\nTable 1 不变：π₀.5, X-VLA, OpenVLA, SmolVLA（闭环）+ π₀, OFT（offline）。CogACT 仅从文献引用（74.2% SR under 78% pruning），无原始 CV 数据。论文已将 claim 收窄为 \"validated on four closed-loop architectures\"，Limitations 承认 \"too few for a general law\"，属正确降级。从 Round 6 的 critical 降级为 major warning——claims 已适当收窄，但 evidence base 未增加的事实不变。\n\n**W-SF2** [R2] **X-VLA Goal attention 结果在 Table tab:attention_pruning 中合并为 \"98.2*\"。** 其他三个 suite 分别列出 attn_last/attn_mean/attn_rollout，Goal 合并为 \"Best of three attention variants\"。不一致暗示选择性报告。应展开为三列或标注 \"all three ≥X%\"。\n\n**W-SF3** [R2] **OpenVLA 移至附录造成主文叙事断裂。** Table 2 仅 3 个模型（π₀.5, X-VLA, SmolVLA），CV spectrum 缺少 0.215 的 MLP calibration 点。论文声称 \"six architectures\" 但主表仅 50% 模型。建议至少加入 OpenVLA Object 行。\n\n**W-SF4** [R2] **Appendix Table 4 caption 说 \"Full results\" 但仍有 ~14% \"--\" 缺失。** OpenVLA k=0.95/0.7/0.5 大部分缺失；X-VLA k=0.7 Spatial/Long 缺失。应改 caption 为 \"available results\" 或补全。\n\n**W-SF5** [R2] **代码/数据发布计划仍缺失。** Round 6 R3-W3 要求添加发布声明，Round 7 未见。\n\n---\n\n## Weaknesses (Info / Minor)\n\n**I1** [R2] Abstract 数字密度仍高（~16 个数值），Round 6 要求从 ~17 降到 ~5 未充分回应。新增内容（zero-mask, scoring reversal）有价值但数字未精简。\n\n**I2** [R2] Zero-mask ablation 的 \"entirely attributable to position disruption\" 应限定为 \"on π₀.5\"，因机制与 RoPE 相关，不一定 generalize 到 non-RoPE 架构。\n\n**I3** [R1] Abstract 使用 π₀ (offline-only) 的 CV=0.038 作为 spectrum 下界，未标注 offline。\n\n---\n\n## Questions\n\n**Q1** X-VLA Goal attention 三种 variant 各自的 SR 是多少？如果差异 <2pp 为何不展开？如果差异大为何只报告 best？\n\n**Q2** Zero-mask 是否在其他模型（X-VLA、OpenVLA）上测试过？如果是，结果如何？如果否，为什么不？\n\n**Q3** Round 7 Related Work 为何删除了 7+ concurrent works 的引用？是有意精简还是修改过程中的疏忽？\n\n---\n\n## Missing References\n\n以下引用在 `references.bib` 中存在但未在正文引用——应恢复：\n\n1. Jabbour et al., \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered,\" 2025\n2. Wang et al., SpecPrune-VLA, 2025\n3. Feng et al., \"See What Matters,\" ICML 2026\n4. Zhang et al., SparseVLM, 2025\n5. Khaki et al., SparseVILA, 2025\n6. Ye et al., FitPrune, 2025\n7. Shi et al., CrossGET, 2024\n\n---\n\n## External Review\n\n外部审稿未请求（Round 7 为 continue 模式）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查 Agent 已完成（4 分钟）。结果：**0 critical, 0 warning, 9 info**。\n\n- 首页无 display item（Figure 1 在 page 2），建议但非必须\n- Figure 1(b)/Figure 2 架构图组件标签字号偏小（~6-7pt），建议放大\n- Figure 4(b) 散点图标注字号偏小，建议 ≥8pt\n- Table 2 格式规范 ✓（booktabs + 加粗最优值）\n- 附录 Table 4 密度高但可接受\n- Figure 9 使用颜色+标记双编码，打印友好 ✓\n- 正文 8 页合规 ✓\n\n---\n\n## Round 6 → Round 7 Issue 追踪总结\n\n| Issue | Round 6 状态 | Round 7 状态 | 变化 |\n|-------|-------------|-------------|------|\n| R6-C1 (CV N=4) | critical/in_progress | warning/in_progress | Claims 收窄，降级 |\n| R6-C2 (Table 2 gaps) | critical/in_progress | info/resolved | 主表完整 |\n| R6-C3 (Causal language) | critical/resolved | critical/in_progress | **REGRESSION** |\n| R6-C4 (Attention baseline) | critical/in_progress | **resolved** | 3 模型全覆盖 |\n| R6-W5 (OpenVLA multi-suite) | warning/in_progress | **resolved** | 4 suite 数据 |\n| R6-W6 (Code release) | warning/resolved | warning/in_progress | 回归 |\n| R6-I2 (Abstract density) | info/resolved | info/in_progress | 未改善 |\n| R7-N1 (Citations deleted) | — | **critical/open** | 新发现 |\n| R7-W1 (Goal attention merge) | — | warning/open | 新发现 |\n\n**净变化**：+2 resolved (C4, W5)，+1 regression (C3)，+1 new critical (N1)，1 downgraded (C1)\n\n---\n\n## Overall Assessment\n\n**Round 7 评分：6/10（Borderline Accept）**\n\n**升分理由（5→6）**：\n- Attention scoring double dissociation 是 genuine insight（S1）——connector 决定哪种 scoring 有效，没有 universal winner\n- Zero-mask ablation 实验设计 elegant，清晰分离 position disruption vs information loss（S2）\n- Table 2 完整化 + π₀.5 Long n=5 multi-seed 消除关键统计疑虑（S3）\n- 两个 Round 6 critical issue resolved（attention baseline、OpenVLA multi-suite）\n- Limitations section 扎实诚实\n\n**未达 7/10 的理由**：\n- **7+ concurrent works 被删除是 unacceptable regression**——必须在提交前修复（W-MF1）\n- **\"Primary determinant\" 因果语言第三轮未修正**——与 Limitations 自相矛盾（W-MF2）\n- CV diagnostic 仍仅 N=4 闭环模型，evidence base 未增加（W-SF1）\n- Simulation-only 对 CoRL 的 practical impact 有限\n- VTR 仅在 SmolVLA 验证，MLP adapter 达到 comparable 性能\n\n**从 6→7 需要**：\n1. 恢复所有被删除的 concurrent work 引用，\"Don't Run with Scissors\" 需专门段落\n2. 全文统一非因果措辞（\"strongest predictor\" 或 \"most consistent structural factor\"）\n3. 展开 X-VLA Goal attention 数据\n\n---\n\n## Detailed Comments\n\n### Round 7 修改亮点\n\n论文在实验深度上有显著进步。Attention scoring 从 zero 覆盖扩展到 3 个模型 × 4 个 suite 的系统比较，揭示了 connector-dependent scoring reversal——这是 Round 6 版本完全缺失的 mechanistic insight。Zero-mask ablation 用优雅的实验设计回答了 \"为什么 10% token 移除会导致 89pp 崩溃\" 这个核心问题。π₀.5 Long 的 5-seed 验证将关键数据点从单一观察提升为可重复发现。\n\n### 遗留问题优先级\n\n1. **P0（阻止提交）**：恢复 7+ concurrent work 引用。\"Don't Run with Scissors\" 是最近的 concurrent work——在 blind review 中遗漏它等同于放弃通过 novelty 检查的机会。\n2. **P0（阻止提交）**：统一因果语言。这是第三轮相同问题，abstract/intro/conclusion 各用不同措辞且与 limitations 矛盾。30 分钟文本替换即可解决。\n3. **P1**：展开 X-VLA Goal attention 数据。\n4. **P2**：Appendix table caption 修正（\"available\" not \"full\"）；Abstract 数字精简。",
    "project": "importance_margin_vla_compress",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline accept",
    "review_chat_id": "oc_83179cdc26b856fbbaf531d145edb3bd"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-29T00:55:33.632509+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_6ea0e93e255655758819bea2ab1f224d:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4065
}
```

</details>

---


### Assistant

_source line 598 · 2026-05-29T00:55:42.373262+00:00_

Round 7 审稿完成。

**评分：6/10（Borderline Accept）**，从 Round 6 的 5/10 上调。

**两个 Must-Fix（阻止提交）**：
1. **7+ concurrent works 引用被删除**（包括 "Don't Run with Scissors"）——bib 中存在但正文无 `\cite{}`，已独立 grep 验证
2. **"primary determinant" 因果语言第三轮未修正**——intro/abstract/conclusion 各用不同措辞，与 limitations "cannot be causally isolated" 自相矛盾

**两个 Resolved**：R6-C4（Attention baseline）和 R6-W5（OpenVLA multi-suite）。Attention scoring double dissociation 和 zero-mask ablation 是论文最有价值的新增内容。

报告和 Issue Tracker 已同步更新并投递。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 599 · 2026-05-29T00:55:42.381240+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 回应 Reviewer 1 Round 7 发现

---

## 交叉回应

### R6-C1 降级为 major: [AGREE]

同意降级。理由：

1. **措辞收窄是实质性改善**。Round 6 C2 声称 "enabling connector-appropriate compression strategy selection without downstream evaluation"——这是一个 general diagnostic tool 的 claim，N=4 完全不够。Round 7 改为 "validated on four closed-loop architectures"——这是一个 observation scope 的描述，N=4 是事实而非 overclaim。
2. **Limitations 明确承认了局限**（Section 6: "The CV–SR correlation relies on four closed-loop models, too few for a general law"）。自我限定比外部质疑的杀伤力小得多。
3. **统计上 N=4 仍无法做 formal validation**（Spearman N=4 最小 p≈0.083），但论文不再 claim formal validation——它 claim observation + directional consistency，这在 empirical study 中是可接受的。

保留为 major weakness 而非 minor 的理由：即使措辞收窄，CV diagnostic 仍是论文三个 contribution 之一（C2）。一个只在 4 个模型上 "validated" 的 diagnostic 作为 CoRL contribution，其 significance 仍然有限。如果降为 observation/analysis tool 而非 contribution，可以进一步降级为 minor。

### R6-C2 降级为 minor: [AGREE]

同意。主文 Table 2 是读者的 primary reference，现已完整——这是 Round 6 三位 reviewer 的共识 Must-Fix，已修复。附录 "--" 集中在 OpenVLA 的非 k=0.9 retention ratios，不影响核心 claims。

补充我的 W3/W4：附录 Table caption 仍写 "Full closed-loop success rates"（Appendix Table 4），但 OpenVLA 在 k=0.95/0.7/0.5 以及 X-VLA k=0.7 Long/Spatial 仍为 "--"。建议将 caption 改为 "Available closed-loop success rates" 或在脚注说明 "OpenVLA conditions beyond k=0.9 are pending"。这是 editorial fix，不影响评分。

### R6-C4 RESOLVED: [AGREE]

同意。Attention-based scoring 是 Round 6 R1-N3 的直接回应，覆盖了三个 closed-loop 模型：
- X-VLA: 三种 attention variant（last/mean/rollout）在 k=0.5 四个 suite 上（Table tab:attention_pruning）
- π₀.5: attention vs random 在 k=0.5 四个 suite 上（Table tab:pi05_attention_crosssuite）
- OpenVLA: attention 在 k=0.9 四个 suite 上（Appendix Table 4 脚注 †）

关键发现——attention 对 entangling connectors 有效但对 independent connectors 无效（甚至 harmful），L2 反之——是论文 Round 7 最有价值的新贡献之一。完全同意 RESOLVED。

我保留一个 minor concern：X-VLA Goal 在 Table tab:attention_pruning 中合并为 "98.2*"（best of three variants），未展开三种 variant 的具体数值。其他三个 suite 都分别列出了三种 variant，Goal 的合并处理不一致。但这不影响 RESOLVED 判定。

### R6-W5 RESOLVED: [AGREE]

同意。OpenVLA 现有全 4 suite k=0.9 数据（Appendix Table 4），包括 L2/Random/Attention 三种 scoring。Figure fig_openvla_sweep 提供了跨 suite 比较的可视化。这满足了 Round 6 R2-W5 "补全 OpenVLA Spatial/Goal/Long 数据" 的要求。

唯一保留意见：OpenVLA 仍不在主文 Table 2 中，我认为至少 Object 行应在主文出现（我的 review 中 F 部分已提出）。但这是叙事选择而非数据完整性问题。

### R6-C3 REGRESSION: [AGREE]

完全同意，且我独立发现了同一问题（我的 W2）。

补充具体位置：
- Introduction line 18: "identifying the vision-language connector as **the primary determinant** of pruning robustness"
- Introduction C1: "identifying connector architecture as **the primary determinant** of pruning robustness"
- Conclusion: "Connector architecture is **the primary factor governing** VLA token compressibility"
- Abstract: "the vision-language connector as **the primary architectural factor** governing pruning tolerance"

四处使用了因果性语言。Limitations Section 6 承认 "preventing full causal isolation of the connector effect"，与正文的因果 claim 直接矛盾。

建议统一修改为 "the strongest predictor of" 或 "the primary architectural correlate of"。这是文字替换，不需要新实验。

### SmolVLA 残余值: 评价

SmolVLA k=0.95 的非零值（Spatial 6.6/4.2, Goal 3.4/4.2）**更可能是 genuine 但接近 noise floor 的真实信号，而非实验噪声**。理由：

1. **模式一致**：非零值只出现在 k=0.95（最温和的 pruning），k=0.9 及以下全为 0.0%。如果是纯噪声，应在各 retention ratio 随机出现。
2. **数值与 Wilson CI 一致**：6.6% 在 500 episodes 中对应 33/500 成功，Wilson 95% CI ≈ [4.7%, 9.2%]，与 0% 基线有统计学差异。
3. **Suite 差异合理**：Object 和 Long 仍为 0.0%，而 Spatial 和 Goal 有残余——Spatial/Goal 的部分 task 可能对少量 token 丢失有更高容忍度（某些 task 可能不依赖被移除的特定空间区域）。

**影响**：这使论文的核心 narrative 更精确——从 "SmolVLA 在任何 pruning 下 catastrophic collapse 到 0%" 变为 "SmolVLA 在 k≤0.9 下 collapse 到 0%，k=0.95 下有 ≤6.6% 的残余"。论文已适当更新措辞为 "≤6.6%"（Introduction）和 "collapses to near-zero" 而非 "0.0%"。这是一个改善——更诚实的数据报告。

### π₀ offline 标注: [AGREE]

同意这是问题。Abstract 写 "The coefficient of variation (CV) of post-connector token norms captures this on a continuous spectrum (0.038 to 0.314)"。0.038 来自 π₀，一个仅有 offline evaluation 的模型——没有 closed-loop SR 数据来验证其 pruning tolerance。将 offline-only 模型的 CV 作为 spectrum 下界，在 Abstract 中不加标注，会让读者认为 0.038 也有 closed-loop 验证。

建议：将 Abstract 中的 spectrum 范围改为 closed-loop 模型的范围（0.055 到 0.314），或标注 "0.038 [offline] to 0.314"。考虑到 0.055 和 0.038 差异很小，使用 closed-loop 范围 (0.055–0.314) 更干净且不损失 narrative impact。

### 是否调整评分？

**原评分：6/10**
**调整后：6/10（维持不变）**

理由：Reviewer 1 的发现与我的独立评估高度一致。交叉审查没有揭示我遗漏的重大问题，也没有发现我过度严厉的地方。关键共识点：

- Table 2 完整化 + attention baseline + multi-seed = 实质性改善 → 从 5 到 6 ✓
- 因果语言未修正 = persistent but fixable weakness → 不影响评分
- CV diagnostic N=4 = major but appropriately scoped weakness → 不影响评分
- 我独立发现的 7+ concurrent works 被删除（N1 Must-Fix）是唯一可能影响评分的新问题，但因为这是 fixable editorial issue（恢复引用即可），我暂不因此降分。如果最终提交仍缺少这些引用，我会降至 5/10。

6/10 = Borderline Accept，含义是：论文有 genuine insights（zero-mask, scoring double dissociation）但 evidence base 仍偏薄（4 models, 1 benchmark, simulation-only），且有 fixable-but-unacceptable editorial issues（missing citations, causal language）。


---

[Reviewer 2 审稿结果]:
交叉回应已提交。评分维持 6/10 不变。与 Reviewer 1 的判断高度一致：Table 2 完整化和 attention baseline 是实质改善，因果语言和 CV diagnostic sample size 是 persistent weaknesses。我独立发现的 7+ missing citations 是最严重的 editorial regression，但因可修复而暂不降分。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应：回应 Reviewer 2 Round 7 发现

### N1 (concurrent works 删除): [AGREE]
独立验证确认：7 个 bib entry 全部存在于 references.bib 但零 \cite{} 命令。related_work.tex 同时声称 "We provide the first cross-architecture analysis"。bib 条目存在说明作者知道这些工作但未引用。"Don't Run with Scissors" (Jabbour et al. 2025) 标题包含 "Pruning Breaks VLA Models"，是最接近的 concurrent work，遗漏同时声称 "first" 不可接受。

### W1 (Goal attention 合并): [AGREE]
验证 appendix.tex:891：Goal 行使用 `\multicolumn{3}{c}{98.2*}` 合并三个 variant，而 Object/Spatial/Long 均展开。选择性合并暗示个别 variant 在 Goal 上表现较差。建议展开所有行。

### W2 (因果语言): [AGREE]
与我的 R6-C3 REGRESSION 发现完全一致。abstract/intro/conclusion 均未修改 "primary determinant/factor"。

### Zero-mask 限定: [AGREE]
实验仅在 π₀.5 Object k=0.9 执行，但 abstract 表述未限定模型。应明确为 "on π₀.5" 或 "For linear connectors"。SmolVLA 的崩溃机制不同（spatial entanglement 而非 position disruption）。

### Abstract 数字密度: [AGREE]
计数约 20 个数值，R3-W4 在 Round 7 未回应。

### OpenVLA 附录: [PARTIALLY AGREE]
OpenVLA 是 MLP connector 唯一闭环代表，移至附录造成叙事断裂，但有空间合理性。建议主表加 OpenVLA k=0.9 汇总行。

### 评分
维持 6/10，条件注释：若 AC 认定 Jabbour et al. 与本文重叠度 >50%，建议降至 5/10。N1 属 related work 维度（R2 专业领域），在我的方法/实验框架中影响 Originality（6→5）但不独立改变总分。W1 cherry-picking 嫌疑限于附录一表，不足以改分。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 600 · 2026-05-29T00:56:01.337484+00:00_

Round 7 审稿圆桌已完成。

**最终结果**：两位 Reviewer 交叉分享后评分均维持 **6/10（Borderline Accept）**，完全收敛。

报告已投递给 Research Director。关键行动项：

| 优先级 | Issue | 操作 |
|--------|-------|------|
| **P0** | R7-N1: 7+ concurrent works 被删除 | 恢复所有引用，"Don't Run with Scissors" 需专门段落 |
| **P0** | R6-C3: "primary determinant" 因果语言 | 全文替换为 "strongest predictor" 或 "most consistent structural factor" |
| P1 | R7-W1: X-VLA Goal attention "98.2*" | 展开三种 variant 或标注 "all three ≥X%" |
| P2 | Appendix caption "Full results" | 改为 "Available results" |
| P2 | Abstract 数字密度 | 精简至 ~10 个 |

两个 P0 均为文本修改，无需新实验，30 分钟内可完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director"
}
```

</details>

---
